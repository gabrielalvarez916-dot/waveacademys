import { createClient } from "npm:@supabase/supabase-js@2";

// COBROS CON MERCADO PAGO, desde las tarifas de la base (tabla tarifas + app_settings 'matricula' y 'dolar').
// Lo llama el panel de la familia (con su sesión). Acciones (POST):
//   { action: "precios" }                      -> tarifas por nivel y modalidad, matrícula y cotización, y si la familia ya pagó la matrícula del año
//   { action: "suscribir", nivel, modalidad }  -> crea la suscripción mensual (cupo) en Mercado Pago y devuelve el link para pagar
//   { action: "matricula" }                    -> crea el pago de la matrícula anual (hasta 2 cuotas) y devuelve el link
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
    const { data: { user } } = await userClient.auth.getUser();
    if (!user) return json({ error: "No autenticado" }, 401);
    const { data: fam } = await admin.from("families").select("id").eq("profile_id", user.id).maybeSingle();
    if (!fam) return json({ error: "Solo una familia puede pagar suscripciones" }, 403);

    const b = await req.json().catch(() => ({}));
    const { data: cfg } = await admin.from("app_settings").select("key, value").in("key", ["dolar", "matricula"]);
    const dolar = Number((cfg || []).find((c: any) => c.key === "dolar")?.value?.ars_por_usd) || 0;
    const mat = (cfg || []).find((c: any) => c.key === "matricula")?.value || {};
    const anio = new Date().getFullYear();
    const aPesos = (usd: number) => Math.round(usd * dolar);

    if (b.action === "precios") {
      const { data: t } = await admin.from("tarifas").select("nivel, modalidad, cuota_mensual_usd").eq("activa", true);
      const { data: m } = await admin.from("matriculas").select("status").eq("family_id", fam.id).eq("anio", anio);
      return json({
        tarifas: (t || []).map((x: any) => ({ ...x, cuota_mensual_ars: aPesos(Number(x.cuota_mensual_usd)) })),
        matricula: { monto_usd: Number(mat.monto_usd) || 0, monto_ars: aPesos(Number(mat.monto_usd) || 0), cuotas_max: Number(mat.cuotas_max) || 1,
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
      const usd = Number(mat.monto_usd) || 0, ars = aPesos(usd), cuotas = Number(mat.cuotas_max) || 1;
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
