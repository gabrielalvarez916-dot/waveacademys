import { createClient } from "npm:@supabase/supabase-js@2";

// Webhook de Mercado Pago (suscripciones y matrícula). Es público: la autenticidad se verifica con la firma x-signature.
// Secretos necesarios en Supabase: MP_ACCESS_TOKEN y MP_WEBHOOK_SECRET.

const ok = (b: unknown = { ok: true }, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { "content-type": "application/json" } });

const hex = (buf: ArrayBuffer) => [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");

async function firmaValida(req: Request, dataId: string, secret: string): Promise<boolean> {
  const sig = req.headers.get("x-signature") ?? "";
  const requestId = req.headers.get("x-request-id") ?? "";
  const partes = Object.fromEntries(sig.split(",").map((p) => p.trim().split("=").map((x) => x.trim()) as [string, string]));
  const ts = partes["ts"], v1 = partes["v1"];
  if (!ts || !v1) return false;
  let manifest = "";
  if (dataId) manifest += `id:${dataId.toLowerCase()};`;
  if (requestId) manifest += `request-id:${requestId};`;
  manifest += `ts:${ts};`;
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const calc = hex(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(manifest)));
  if (calc.length !== v1.length) return false;
  let diff = 0;
  for (let i = 0; i < calc.length; i++) diff |= calc.charCodeAt(i) ^ v1.charCodeAt(i);
  return diff === 0;
}

const ESTADO_SUSCRIPCION: Record<string, string> = {
  authorized: "active", pending: "pending", paused: "suspended", cancelled: "cancelled",
};

Deno.serve(async (req) => {
  if (req.method !== "POST") return ok({ ok: true, service: "mp-webhook" });

  const secret = Deno.env.get("MP_WEBHOOK_SECRET");
  const token = Deno.env.get("MP_ACCESS_TOKEN");
  if (!secret || !token) return ok({ error: "Webhook sin configurar (faltan secretos)" }, 503);

  const url = new URL(req.url);
  let body: any = {};
  try { body = await req.json(); } catch { /* algunos avisos vienen sin cuerpo */ }

  const topic: string = body.type ?? body.topic ?? url.searchParams.get("type") ?? url.searchParams.get("topic") ?? "";
  const dataId: string = String(body?.data?.id ?? url.searchParams.get("data.id") ?? url.searchParams.get("id") ?? "");

  if (!(await firmaValida(req, dataId, secret))) return ok({ error: "Firma inválida" }, 401);

  const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

  const { data: ev } = await db.from("mp_webhook_events")
    .insert({ topic, resource_id: dataId || null, payload: { body, query: Object.fromEntries(url.searchParams) } })
    .select("id").single();
  const cerrar = async (error: string | null) => {
    if (ev) await db.from("mp_webhook_events").update({ processed_at: new Date().toISOString(), error }).eq("id", ev.id);
  };

  const mp = async (path: string) => {
    const r = await fetch(`https://api.mercadopago.com${path}`, { headers: { Authorization: `Bearer ${token}` } });
    if (!r.ok) throw new Error(`Mercado Pago respondió ${r.status} en ${path}`);
    return await r.json();
  };

  // Encuentra (o crea) la suscripción local de una suscripción de Mercado Pago
  async function suscripcionLocal(pre: any): Promise<string | null> {
    const { data: porId } = await db.from("subscriptions").select("id").eq("mp_preapproval_id", pre.id).maybeSingle();
    if (porId) return porId.id;

    // 1) external_reference = id de una suscripción local sin vincular (las crea mp-cobros)
    if (pre.external_reference) {
      const { data: porRef } = await db.from("subscriptions").select("id, mp_preapproval_id")
        .eq("id", pre.external_reference).maybeSingle();
      if (porRef && !porRef.mp_preapproval_id) {
        await db.from("subscriptions").update({ mp_preapproval_id: pre.id }).eq("id", porRef.id);
        return porRef.id;
      }
    }
    // 2) por el correo del pagador: familia con ese correo
    const mail = (pre.payer_email ?? "").toLowerCase();
    if (mail) {
      const { data: perfil } = await db.from("profiles").select("id").ilike("email", mail).eq("role", "family").maybeSingle();
      const { data: fam } = perfil
        ? await db.from("families").select("id").eq("profile_id", perfil.id).maybeSingle()
        : { data: null };
      if (fam) {
        const { data: libre } = await db.from("subscriptions").select("id")
          .eq("family_id", fam.id).is("mp_preapproval_id", null).is("student_id", null)
          .order("created_at", { ascending: true }).limit(1).maybeSingle();
        if (libre) {
          await db.from("subscriptions").update({ mp_preapproval_id: pre.id }).eq("id", libre.id);
          return libre.id;
        }
        const { data: nueva } = await db.from("subscriptions")
          .insert({ family_id: fam.id, mp_preapproval_id: pre.id, status: "pending" }).select("id").single();
        return nueva?.id ?? null;
      }
    }
    return null;
  }

  try {
    if (topic === "subscription_preapproval" || topic === "preapproval") {
      const pre = await mp(`/preapproval/${dataId}`);
      const subId = await suscripcionLocal(pre);
      if (!subId) { await cerrar(`Suscripción ${pre.id} sin familia asociada (correo: ${pre.payer_email ?? "?"})`); return ok(); }
      const estado = ESTADO_SUSCRIPCION[pre.status] ?? "pending";
      const cambios: Record<string, unknown> = {
        status: estado,
        amount: pre.auto_recurring?.transaction_amount ?? null,
        currency: pre.auto_recurring?.currency_id ?? "ARS",
        next_payment_date: pre.next_payment_date ?? null,
      };
      if (estado === "cancelled") cambios.cancelled_at = pre.date_cancelled ?? new Date().toISOString();
      if (estado === "active") cambios.past_due_since = null;
      await db.from("subscriptions").update(cambios).eq("id", subId);
      await cerrar(null);
      return ok();
    }

    if (topic === "subscription_authorized_payment" || topic === "authorized_payment") {
      const ap = await mp(`/authorized_payments/${dataId}`);
      const { data: sub } = await db.from("subscriptions").select("id, past_due_since")
        .eq("mp_preapproval_id", ap.preapproval_id).maybeSingle();
      if (!sub) { await cerrar(`Cobro ${ap.id} de una suscripción desconocida (${ap.preapproval_id})`); return ok(); }

      const pagado = ["approved", "processed"].includes(ap.status) || ap.payment?.status === "approved";
      const rechazado = ["rejected", "cancelled"].includes(ap.status) || ["rejected", "cancelled"].includes(ap.payment?.status);
      const mpPaymentId = String(ap.payment?.id ?? `ap-${ap.id}`);
      const fechaPago = pagado ? (ap.last_modified ?? ap.date_created ?? new Date().toISOString()) : null;

      await db.from("payments").upsert({
        subscription_id: sub.id, mp_payment_id: mpPaymentId,
        status: ap.payment?.status ?? ap.status, amount: ap.transaction_amount ?? null,
        paid_at: fechaPago, raw: ap,
      }, { onConflict: "mp_payment_id" });

      if (pagado) {
        await db.from("subscriptions").update({ status: "active", last_payment_at: fechaPago, past_due_since: null }).eq("id", sub.id);
      } else if (rechazado) {
        await db.from("subscriptions").update({ status: "past_due", past_due_since: sub.past_due_since ?? new Date().toISOString() }).eq("id", sub.id);
      }
      await cerrar(null);
      return ok();
    }

    if (topic === "payment") {
      const pago = await mp(`/v1/payments/${dataId}`);
      // Matrícula anual (la crea mp-cobros con external_reference "matricula:<id>")
      const ref = String(pago.external_reference ?? "");
      if (ref.startsWith("matricula:")) {
        const cambios: Record<string, unknown> = { status: pago.status, mp_payment_id: String(pago.id) };
        if (pago.status === "approved") cambios.paid_at = pago.date_approved ?? new Date().toISOString();
        await db.from("matriculas").update(cambios).eq("id", ref.slice("matricula:".length));
        await cerrar(null);
        return ok();
      }
      const preId = pago.metadata?.preapproval_id ?? pago.point_of_interaction?.transaction_data?.subscription_id ?? null;
      const { data: sub } = preId
        ? await db.from("subscriptions").select("id").eq("mp_preapproval_id", preId).maybeSingle()
        : { data: null };
      if (!sub) { await cerrar("Pago no asociado a una suscripción (se procesa por el aviso de cobro de suscripción)"); return ok(); }
      await db.from("payments").upsert({
        subscription_id: sub.id, mp_payment_id: String(pago.id), status: pago.status,
        amount: pago.transaction_amount ?? null,
        paid_at: pago.status === "approved" ? (pago.date_approved ?? null) : null, raw: pago,
      }, { onConflict: "mp_payment_id" });
      await cerrar(null);
      return ok();
    }

    await cerrar(`Tipo de aviso no procesado: ${topic || "(vacío)"}`);
    return ok();
  } catch (e) {
    console.error(e);
    await cerrar(String((e as Error).message ?? e));
    return ok({ error: "Error al procesar" }, 500); // Mercado Pago reintenta
  }
});
