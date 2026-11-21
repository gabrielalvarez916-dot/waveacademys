import { createClient } from "npm:@supabase/supabase-js@2";
const RECARGO = 1.05;
// Matrícula: desde noviembre se cobra la del año siguiente. Pagando antes de febrero de ese año, va el precio anticipado.
function matriculaHoy(mat: any) {
  const hoy = new Date(), mes = hoy.getMonth() + 1, anioHoy = hoy.getFullYear();
  const anio = mes >= (Number(mat.abre_mes) || 11) ? anioHoy + 1 : anioHoy;
  const anticipada = anio > anioHoy || mes < (Number(mat.anticipado_hasta_mes) || 2);
  const base = anticipada && Number(mat.monto_anticipado_usd) ? Number(mat.monto_anticipado_usd) : Number(mat.monto_usd) || 0;
  const usd = Math.round(base * RECARGO * 100) / 100; // +5% por el costo del cobro internacional
  return { anio, usd, anticipada };
}

// COBROS CON PAYPAL, EN DÓLARES (familias de otros países). Precios de la tabla tarifas y de app_settings 'matricula'.
// Desde el panel de la familia (con su sesión), POST:
//   { action: "suscribir", nivel, modalidad } -> suscripción mensual en USD; devuelve el link de PayPal para aprobarla
//   { action: "matricula" }                   -> pago único de la matrícula anual en USD; devuelve el link
//   { action: "tutoria", tutoria_id }          -> pago de una tutoría individual (precio en USD + recargo); al cobrarse queda confirmada sola
// Webhook de PayPal (mismo URL, sin action): activa, suspende o cancela suscripciones, registra cobros y cobra la matrícula aprobada.
// Credenciales en gen_config: paypal_client_id, paypal_secret, paypal_webhook_id y paypal_env ("live" o "sandbox").
// El producto y los planes de PayPal se crean solos la primera vez (uno por precio) y se guardan en tarifas.paypal_plan_id.

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });
const NIVEL = { inicial: "Nivel Inicial", medio: "Nivel Medio", avanzado: "Nivel Avanzado" } as Record<string, string>;
const MODALIDAD = { libre: "Libre", guiada: "Guiada", completa: "Completa", personalizada: "Personalizada" } as Record<string, string>;
const ESTADO: Record<string, string> = {
  "BILLING.SUBSCRIPTION.ACTIVATED": "active", "BILLING.SUBSCRIPTION.RE-ACTIVATED": "active",
  "BILLING.SUBSCRIPTION.SUSPENDED": "suspended", "BILLING.SUBSCRIPTION.CANCELLED": "cancelled",
  "BILLING.SUBSCRIPTION.EXPIRED": "cancelled", "BILLING.SUBSCRIPTION.PAYMENT.FAILED": "past_due",
};

// Credenciales: tabla gen_config (claves paypal_client_id, paypal_secret, paypal_webhook_id, paypal_env) o secretos del mismo nombre en mayúsculas
let CFG: Record<string, string> | null = null;
async function cfg(admin: any) {
  if (CFG) return CFG;
  const { data } = await admin.from("gen_config").select("clave, valor").like("clave", "paypal_%");
  const c: Record<string, string> = {};
  (data || []).forEach((x: any) => { c[x.clave] = x.valor; });
  for (const k of ["paypal_client_id", "paypal_secret", "paypal_webhook_id", "paypal_env"]) c[k] = c[k] || Deno.env.get(k.toUpperCase()) || "";
  return (CFG = c);
}
const BASE = () => (CFG?.paypal_env === "sandbox" ? "https://api-m.sandbox.paypal.com" : "https://api-m.paypal.com");
async function token(admin: any): Promise<string> {
  const c = await cfg(admin);
  if (!c.paypal_client_id || !c.paypal_secret) throw new Error("SIN_CONFIGURAR");
  const r = await fetch(`${BASE()}/v1/oauth2/token`, {
    method: "POST", headers: { Authorization: "Basic " + btoa(`${c.paypal_client_id}:${c.paypal_secret}`), "content-type": "application/x-www-form-urlencoded" },
    body: "grant_type=client_credentials",
  });
  if (!r.ok) throw new Error(`PayPal token ${r.status}`);
  return (await r.json()).access_token;
}
async function pp(tk: string, path: string, body?: unknown, method = "POST") {
  const r = await fetch(`${BASE()}${path}`, {
    method, headers: { Authorization: `Bearer ${tk}`, "content-type": "application/json", Prefer: "return=representation" },
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  const d = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(`PayPal ${path}: ${d.message || d.name || r.status}`);
  return d;
}
const enlace = (d: any, rel: string) => (d.links || []).find((l: any) => l.rel === rel)?.href;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method === "GET") return json({ ok: true, servicio: "Pagos con PayPal de Wave Academy (esta dirección la usa PayPal)" });
  const url = Deno.env.get("SUPABASE_URL")!;
  const admin = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const b = await req.json().catch(() => ({}));

  // ---------- Webhook de PayPal ----------
  if (!b.action && req.headers.get("paypal-transmission-id")) {
    try {
      const tk = await token(admin);
      const v = await pp(tk, "/v1/notifications/verify-webhook-signature", {
        auth_algo: req.headers.get("paypal-auth-algo"), cert_url: req.headers.get("paypal-cert-url"),
        transmission_id: req.headers.get("paypal-transmission-id"), transmission_sig: req.headers.get("paypal-transmission-sig"),
        transmission_time: req.headers.get("paypal-transmission-time"), webhook_id: (await cfg(admin)).paypal_webhook_id, webhook_event: b,
      });
      if (v.verification_status !== "SUCCESS") return json({ error: "Firma inválida" }, 401);
      const tipo = String(b.event_type || ""), r = b.resource || {};
      if (ESTADO[tipo]) {
        const cambios: Record<string, unknown> = { status: ESTADO[tipo], paypal_subscription_id: r.id };
        if (ESTADO[tipo] === "cancelled") cambios.cancelled_at = new Date().toISOString();
        if (ESTADO[tipo] === "active") cambios.past_due_since = null;
        if (ESTADO[tipo] === "past_due") cambios.past_due_since = new Date().toISOString();
        if (r.billing_info?.next_billing_time) cambios.next_payment_date = r.billing_info.next_billing_time;
        const q = admin.from("subscriptions").update(cambios);
        await (r.custom_id ? q.eq("id", r.custom_id) : q.eq("paypal_subscription_id", r.id));
      } else if (tipo === "PAYMENT.SALE.COMPLETED" && r.billing_agreement_id) {
        const { data: sub } = await admin.from("subscriptions").select("id").eq("paypal_subscription_id", r.billing_agreement_id).maybeSingle();
        if (sub) {
          const fecha = r.create_time || new Date().toISOString();
          await admin.from("payments").upsert({ subscription_id: sub.id, mp_payment_id: `pp-${r.id}`, status: "approved",
            amount: Number(r.amount?.total) || null, paid_at: fecha, raw: r }, { onConflict: "mp_payment_id" });
          await admin.from("subscriptions").update({ status: "active", last_payment_at: fecha, past_due_since: null }).eq("id", sub.id);
        }
      } else if (tipo === "CHECKOUT.ORDER.APPROVED") {
        const cid = String(r.purchase_units?.[0]?.custom_id || "");
        if (cid.startsWith("matricula:") || cid.startsWith("tutoria:")) await pp(tk, `/v2/checkout/orders/${r.id}/capture`, {});
      } else if (tipo === "PAYMENT.CAPTURE.COMPLETED" || tipo === "PAYMENT.CAPTURE.DENIED") {
        const ref = String(r.custom_id || "");
        if (ref.startsWith("matricula:")) {
          const ok = tipo === "PAYMENT.CAPTURE.COMPLETED";
          await admin.from("matriculas").update({ status: ok ? "approved" : "rejected", paid_at: ok ? (r.create_time || new Date().toISOString()) : null })
            .eq("id", ref.slice("matricula:".length));
        } else if (ref.startsWith("tutoria:")) {
          // Tutoría individual: el pago con PayPal la confirma sola (no pasa por Tesorería)
          const id = ref.slice("tutoria:".length), ok = tipo === "PAYMENT.CAPTURE.COMPLETED";
          const { data: t } = await admin.from("tutorias").select("id,tutor_id,family_id,estado").eq("id", id).maybeSingle();
          if (t && ok) {
            const { data: fam } = await admin.from("families").select("profile_id").eq("id", t.family_id).maybeSingle();
            const { data: upd } = await admin.from("tutorias").update({ estado: "reservada", medio: "paypal", updated_at: new Date().toISOString() }).eq("id", id).eq("estado", "pendiente_pago").select("id");
            if (upd?.length) {
              await admin.from("notificaciones").insert([
                { profile_id: fam?.profile_id, tipo: "pago", titulo: "Tutoría confirmada", texto: "Recibimos tu pago con PayPal y la tutoría individual quedó confirmada.", tutoria_id: id },
                { profile_id: t.tutor_id, tipo: "tutoria", titulo: "Nueva tutoría individual", texto: "Se confirmó una tutoría individual en tu agenda.", tutoria_id: id },
              ]);
            } else {
              // el horario ya se había liberado: avisamos a la familia y a Tesorería para resolverlo a mano
              const { data: tes } = await admin.from("profiles").select("id").eq("role", "tesorero").eq("is_suspended", false);
              await admin.from("notificaciones").insert([
                { profile_id: fam?.profile_id, tipo: "pago", titulo: "Pago de tutoría recibido", texto: "Recibimos tu pago, pero el horario ya se había liberado. Te contactamos para darte otro.", tutoria_id: id },
                ...(tes || []).map((x: any) => ({ profile_id: x.id, tipo: "pago", titulo: "Pago de tutoría sin horario", texto: "Entró un pago de PayPal de una tutoría cuyo horario ya se liberó. Hay que reubicarla o devolver el pago.", tutoria_id: id })),
              ]);
            }
          }
        }
      }
      return json({ ok: true });
    } catch (e) {
      console.error(e);
      return json({ error: "Error al procesar" }, 500); // PayPal reintenta
    }
  }

  // ---------- Pedidos de la familia ----------
  try {
    const userClient = createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, {
      global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } },
    });
    const { data: { user } } = await userClient.auth.getUser();
    if (!user) return json({ error: "No autenticado" }, 401);
    const { data: fam } = await admin.from("families").select("id").eq("profile_id", user.id).maybeSingle();
    if (!fam) return json({ error: "Solo una familia puede pagar suscripciones" }, 403);
    const { data: perfil } = await admin.from("profiles").select("email").eq("id", user.id).single();
    const origen = req.headers.get("origin") || new URL(req.headers.get("referer") || "https://example.com").origin;
    const volver = `${origen}/familia.html#facturacion`;
    let tk: string;
    try { tk = await token(admin); } catch { return json({ error: "Los pagos con PayPal todavía no están configurados. Escribinos y te ayudamos." }, 503); }

    if (b.action === "suscribir") {
      const { data: t } = await admin.from("tarifas").select("id, cuota_mensual_usd, paypal_plan_id, paypal_plan_usd")
        .eq("nivel", b.nivel).eq("modalidad", b.modalidad).eq("activa", true).maybeSingle();
      if (!t) return json({ error: "Esa modalidad no está disponible para ese nivel" }, 400);
      const usd = Math.round(Number(t.cuota_mensual_usd) * RECARGO * 100) / 100; // +5% por el costo del cobro internacional
      let plan = t.paypal_plan_id;
      if (!plan || Number(t.paypal_plan_usd) !== usd) { // un plan por precio: si el precio cambió, se crea otro
        const { data: cfg } = await admin.from("app_settings").select("value").eq("key", "paypal").maybeSingle();
        let producto = (cfg?.value as any)?.product_id;
        if (!producto) {
          producto = (await pp(tk, "/v1/catalogs/products", { name: "Wave Academy", type: "SERVICE", category: "EDUCATIONAL_AND_TEXTBOOKS" })).id;
          await admin.from("app_settings").upsert({ key: "paypal", value: { ...((cfg?.value as any) || {}), product_id: producto }, updated_at: new Date().toISOString() });
        }
        plan = (await pp(tk, "/v1/billing/plans", {
          product_id: producto, name: `${NIVEL[b.nivel] || b.nivel} · ${MODALIDAD[b.modalidad] || b.modalidad}`, status: "ACTIVE",
          billing_cycles: [{ frequency: { interval_unit: "MONTH", interval_count: 1 }, tenure_type: "REGULAR", sequence: 1, total_cycles: 0,
            pricing_scheme: { fixed_price: { value: usd.toFixed(2), currency_code: "USD" } } }],
          payment_preferences: { auto_bill_outstanding: true, payment_failure_threshold: 3 },
        })).id;
        await admin.from("tarifas").update({ paypal_plan_id: plan, paypal_plan_usd: usd }).eq("id", t.id);
      }
      const { data: sub, error } = await admin.from("subscriptions")
        .insert({ family_id: fam.id, status: "pending", proveedor: "paypal", nivel: b.nivel, modalidad: b.modalidad, monto_usd: usd, amount: usd, currency: "USD" })
        .select("id").single();
      if (error) throw error;
      try {
        const s = await pp(tk, "/v1/billing/subscriptions", {
          plan_id: plan, custom_id: sub.id, subscriber: { email_address: perfil?.email },
          application_context: { brand_name: "Wave Academy", locale: "es-419", user_action: "SUBSCRIBE_NOW", return_url: volver, cancel_url: volver },
        });
        await admin.from("subscriptions").update({ paypal_subscription_id: s.id }).eq("id", sub.id);
        return json({ url: enlace(s, "approve"), monto_usd: usd });
      } catch (e) {
        await admin.from("subscriptions").delete().eq("id", sub.id);
        throw e;
      }
    }

    if (b.action === "matricula") {
      const { data: c } = await admin.from("app_settings").select("value").eq("key", "matricula").single();
      const { anio, usd } = matriculaHoy(c?.value || {});
      const { data: ya } = await admin.from("matriculas").select("status").eq("family_id", fam.id).eq("anio", anio);
      if ((ya || []).some((x: any) => x.status === "approved")) return json({ error: `La matrícula ${anio} ya está paga` }, 409);
      if (!usd) return json({ error: "Falta el monto de la matrícula en la configuración" }, 500);
      const { data: m, error } = await admin.from("matriculas")
        .insert({ family_id: fam.id, anio, monto_usd: usd, monto_ars: 0, cuotas_max: 1, proveedor: "paypal" }).select("id").single();
      if (error) throw error;
      const o = await pp(tk, "/v2/checkout/orders", {
        intent: "CAPTURE",
        purchase_units: [{ custom_id: `matricula:${m.id}`, description: `Matrícula anual ${anio} · Wave Academy`, amount: { currency_code: "USD", value: usd.toFixed(2) } }],
        application_context: { brand_name: "Wave Academy", locale: "es-419", user_action: "PAY_NOW", return_url: volver, cancel_url: volver },
      });
      await admin.from("matriculas").update({ paypal_order_id: o.id }).eq("id", m.id);
      return json({ url: enlace(o, "approve") || enlace(o, "payer-action"), monto_usd: usd });
    }

    if (b.action === "tutoria") {
      const { data: t } = await admin.from("tutorias").select("id,family_id,estado,tipo,precio_usd,vence_pago_at,area").eq("id", String(b.tutoria_id || "")).maybeSingle();
      if (!t || t.family_id !== fam.id || t.tipo !== "individual") return json({ error: "No encontramos esa tutoría" }, 404);
      if (t.estado !== "pendiente_pago") return json({ error: "Esa tutoría ya no espera el pago" }, 409);
      if (new Date(t.vence_pago_at).getTime() < Date.now()) return json({ error: "Venció el plazo de pago de esta tutoría" }, 409);
      const { data: c } = await admin.from("app_settings").select("value").eq("key", "tutoria_individual").maybeSingle();
      const recargo = 1 + (Number(c?.value?.recargo_pct ?? 5) / 100);
      const usd = Math.round(Number(t.precio_usd || 0) * recargo * 100) / 100;
      if (!usd) return json({ error: "Falta el precio en dólares de la tutoría" }, 500);
      const o = await pp(tk, "/v2/checkout/orders", {
        intent: "CAPTURE",
        purchase_units: [{ custom_id: `tutoria:${t.id}`, description: "Tutoría individual · Wave Academy", amount: { currency_code: "USD", value: usd.toFixed(2) } }],
        application_context: { brand_name: "Wave Academy", locale: "es-419", user_action: "PAY_NOW", return_url: `${origen}/familia.html#tutorias`, cancel_url: `${origen}/familia.html#tutorias` },
      });
      await admin.from("tutorias").update({ paypal_order_id: o.id, medio: "paypal" }).eq("id", t.id);
      return json({ url: enlace(o, "approve") || enlace(o, "payer-action"), monto_usd: usd });
    }

    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: "No se pudo preparar el pago con PayPal. Probá de nuevo en un rato." }, 500);
  }
});
