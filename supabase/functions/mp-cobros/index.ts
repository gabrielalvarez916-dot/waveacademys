import { createClient } from "npm:@supabase/supabase-js@2";
// Matrícula: desde noviembre se cobra la del año siguiente. Pagando antes de febrero de ese año, va el precio anticipado.
function matriculaHoy(mat: any) {
  const hoy = new Date(), mes = hoy.getMonth() + 1, anioHoy = hoy.getFullYear();
  const anio = mes >= (Number(mat.abre_mes) || 11) ? anioHoy + 1 : anioHoy;
  const anticipada = anio > anioHoy || mes < (Number(mat.anticipado_hasta_mes) || 2);
  const usd = anticipada && Number(mat.monto_anticipado_usd) ? Number(mat.monto_anticipado_usd) : Number(mat.monto_usd) || 0;
  return { anio, usd, anticipada };
}

// COBROS CON MERCADO PAGO, desde las tarifas de la base (tabla tarifas + app_settings 'matricula' y 'dolar').
// Lo llama el panel de la familia (con su sesión). Acciones (POST):
//   { action: "precios" }                      -> tarifas por nivel y modalidad, matrícula y cotización, y si la familia ya pagó la matrícula del año
//   { action: "suscribir", nivel, modalidad }  -> crea la suscripción mensual (cupo) en Mercado Pago y devuelve el link para pagar
//   { action: "matricula" }                    -> crea el pago de la matrícula anual (hasta 2 cuotas) y devuelve el link
//   { action: "ajustar_dolar", ars_por_usd }   -> (admin, o header x-gen-token) guarda la cotización y actualiza el monto en pesos
//                                                  de cada suscripción de Mercado Pago que tiene precio en USD
// Las tarifas están en USD; Mercado Pago cobra en pesos con la cotización de app_settings 'dolar'.
// Secreto necesario: MP_ACCESS_TOKEN. Los avisos de pago los procesa mp-webhook.

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

const NIVEL = { inicial: "Nivel Inicial", medio: "Nivel Medio", avanzado: "Nivel Avanzado" } as Record<string, string>;
const MODALIDAD = { libre: "Libre", guiada: "Guiada", completa: "Completa", personalizada: "Personalizada" } as Record<string, string>;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const url = Deno.env.get("SUPABASE_URL")!;
    const admin = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
    const userClient = createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, {
      global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } },
    });
    const b0 = await req.clone().json().catch(() => ({}));
    if (b0.action === "ajustar_dolar") {
      const { data: g } = await admin.from("gen_config").select("valor").eq("clave", "token").maybeSingle();
      let autorizado = !!g && req.headers.get("x-gen-token") === g.valor;
      if (!autorizado) {
        const { data: { user: u } } = await userClient.auth.getUser();
        const { data: pr } = u ? await admin.from("profiles").select("role").eq("id", u.id).maybeSingle() : { data: null };
        autorizado = pr?.role === "admin";
      }
      if (!autorizado) return json({ error: "Solo el administrador" }, 403);
      const nuevo = Number(b0.ars_por_usd);
      if (!(nuevo > 100)) return json({ error: "Cotización inválida" }, 400);
      const { data: d0 } = await admin.from("app_settings").select("value").eq("key", "dolar").single();
      await admin.from("app_settings").update({ value: { ...(d0?.value || {}), ars_por_usd: nuevo }, updated_at: new Date().toISOString() }).eq("key", "dolar");
      const token0 = Deno.env.get("MP_ACCESS_TOKEN");
      const { data: subs } = await admin.from("subscriptions").select("id, mp_preapproval_id, monto_usd, amount")
        .eq("proveedor", "mercadopago").not("mp_preapproval_id", "is", null).not("monto_usd", "is", null).in("status", ["active", "past_due", "pending"]);
      const res: any[] = [];
      for (const s of subs || []) {
        const ars = Math.round(Number(s.monto_usd) * nuevo);
        if (Number(s.amount) === ars) { res.push({ id: s.id, igual: true }); continue; }
        if (!token0) { res.push({ id: s.id, error: "sin MP_ACCESS_TOKEN" }); continue; }
        const r = await fetch(`https://api.mercadopago.com/preapproval/${s.mp_preapproval_id}`, {
          method: "PUT", headers: { Authorization: `Bearer ${token0}`, "content-type": "application/json" },
          body: JSON.stringify({ auto_recurring: { transaction_amount: ars, currency_id: "ARS" } }),
        });
        if (r.ok) { await admin.from("subscriptions").update({ amount: ars }).eq("id", s.id); res.push({ id: s.id, antes: s.amount, ahora: ars }); }
        else res.push({ id: s.id, error: `Mercado Pago ${r.status}` });
      }
      return json({ ok: true, ars_por_usd: nuevo, suscripciones: res });
    }

    const { data: { user } } = await userClient.auth.getUser();
    if (!user) return json({ error: "No autenticado" }, 401);
    const { data: fam } = await admin.from("families").select("id").eq("profile_id", user.id).maybeSingle();
    if (!fam) return json({ error: "Solo una familia puede pagar suscripciones" }, 403);

    const b = await req.json().catch(() => ({}));
    const { data: cfg } = await admin.from("app_settings").select("key, value").in("key", ["dolar", "matricula"]);
    const dolar = Number((cfg || []).find((c: any) => c.key === "dolar")?.value?.ars_por_usd) || 0;
    const mat = (cfg || []).find((c: any) => c.key === "matricula")?.value || {};
    const { anio, usd: matUsd, anticipada } = matriculaHoy(mat);
    const aPesos = (usd: number) => Math.round(usd * dolar);

    if (b.action === "precios") {
      const { data: t } = await admin.from("tarifas").select("nivel, modalidad, cuota_mensual_usd").eq("activa", true);
      const { data: m } = await admin.from("matriculas").select("status").eq("family_id", fam.id).eq("anio", anio);
      return json({
        tarifas: (t || []).map((x: any) => ({ ...x, cuota_mensual_ars: aPesos(Number(x.cuota_mensual_usd)) })),
        matricula: { anio, anticipada, monto_usd: matUsd, monto_ars: aPesos(matUsd), monto_lleno_usd: Number(mat.monto_usd) || 0, cuotas_max: Number(mat.cuotas_max) || 1,
          pagada: (m || []).some((x: any) => x.status === "approved") },
        dolar,
      });
    }

    const token = Deno.env.get("MP_ACCESS_TOKEN");
    if (!token) return json({ error: "Los pagos todavía no están configurados. Escribinos y te ayudamos." }, 503);
    if (!dolar) return json({ error: "Falta la cotización del dólar en la configuración" }, 500);
    const origen = req.headers.get("origin") || new URL(req.headers.get("referer") || "https://example.com").origin;
    const volver = `${origen}/familia.html#facturacion`;
    const { data: perfil } = await admin.from("profiles").select("email").eq("id", user.id).single();
    const mp = async (path: string, body: unknown) => {
      const r = await fetch(`https://api.mercadopago.com${path}`, {
        method: "POST", headers: { Authorization: `Bearer ${token}`, "content-type": "application/json" }, body: JSON.stringify(body),
      });
      const d = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(`Mercado Pago: ${d.message || r.status}`);
      return d;
    };

    if (b.action === "suscribir") {
      const { data: t } = await admin.from("tarifas").select("cuota_mensual_usd").eq("nivel", b.nivel).eq("modalidad", b.modalidad).eq("activa", true).maybeSingle();
      if (!t) return json({ error: "Esa modalidad no está disponible para ese nivel" }, 400);
      const usd = Number(t.cuota_mensual_usd), ars = aPesos(usd);
      // la suscripción local se crea primero: Mercado Pago la devuelve en external_reference y mp-webhook la vincula
      const { data: sub, error } = await admin.from("subscriptions")
        .insert({ family_id: fam.id, status: "pending", nivel: b.nivel, modalidad: b.modalidad, monto_usd: usd, amount: ars, currency: "ARS" })
        .select("id").single();
      if (error) throw error;
      try {
        const pre = await mp("/preapproval", {
          reason: `Wave Academy · ${NIVEL[b.nivel] || b.nivel} · ${MODALIDAD[b.modalidad] || b.modalidad}`,
          external_reference: sub.id, payer_email: perfil?.email, back_url: volver, status: "pending",
          auto_recurring: { frequency: 1, frequency_type: "months", transaction_amount: ars, currency_id: "ARS" },
        });
        await admin.from("subscriptions").update({ mp_preapproval_id: pre.id }).eq("id", sub.id);
        return json({ url: pre.init_point, monto_ars: ars, monto_usd: usd });
      } catch (e) {
        await admin.from("subscriptions").delete().eq("id", sub.id);
        throw e;
      }
    }

    if (b.action === "matricula") {
      const { data: ya } = await admin.from("matriculas").select("id, status").eq("family_id", fam.id).eq("anio", anio);
      if ((ya || []).some((x: any) => x.status === "approved")) return json({ error: `La matrícula ${anio} ya está paga` }, 409);
      const usd = matUsd, ars = aPesos(usd), cuotas = Number(mat.cuotas_max) || 1;
      if (!usd) return json({ error: "Falta el monto de la matrícula en la configuración" }, 500);
      const { data: m, error } = await admin.from("matriculas")
        .insert({ family_id: fam.id, anio, monto_usd: usd, monto_ars: ars, cuotas_max: cuotas }).select("id").single();
      if (error) throw error;
      const pref = await mp("/checkout/preferences", {
        items: [{ title: `Matrícula anual ${anio} · Wave Academy`, quantity: 1, unit_price: ars, currency_id: "ARS" }],
        payer: { email: perfil?.email }, external_reference: `matricula:${m.id}`,
        payment_methods: { installments: cuotas },
        back_urls: { success: volver, failure: volver, pending: volver }, auto_return: "approved",
        notification_url: `${url}/functions/v1/mp-webhook?source_news=webhooks`,
      });
      await admin.from("matriculas").update({ mp_preference_id: pref.id }).eq("id", m.id);
      return json({ url: pref.init_point, monto_ars: ars, monto_usd: usd, cuotas_max: cuotas });
    }

    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: "No se pudo preparar el pago. Probá de nuevo en un rato." }, 500);
  }
});
