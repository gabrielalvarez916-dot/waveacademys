import { createClient } from "npm:@supabase/supabase-js@2";
import { AwsClient } from "npm:aws4fetch@1";

// VIDEO FINAL · une los cortes y la intro en un solo MP4 (lo hace GitHub Actions con ffmpeg: tools/render/render.py).
// Acciones (POST, header x-gen-token):
//   { action: "siguiente" }            -> toma el pedido pendiente más viejo y devuelve enlaces firmados (bajar partes, subir el resultado)
//   { action: "listo", id }            -> el video final ya está subido: reemplaza los videos de la lección por ese único archivo
//   { action: "error", id, error }     -> marca el pedido con error
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type, x-gen-token",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const env = (k: string) => (Deno.env.get(k) ?? "").trim().replace(/^["']|["']$/g, "").trim();

function r2() {
  const aws = new AwsClient({ accessKeyId: env("R2_ACCESS_KEY_ID"), secretAccessKey: env("R2_SECRET_ACCESS_KEY"), service: "s3", region: "auto" });
  const base = (key: string) =>
    `https://${env("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com/${env("R2_BUCKET")}/${key.split("/").map(encodeURIComponent).join("/")}`;
  return { aws, base };
}
async function firmar(method: string, key: string, segundos: number) {
  const { aws, base } = r2();
  const u = new URL(base(key));
  u.searchParams.set("X-Amz-Expires", String(segundos));
  return (await aws.sign(new Request(u, { method }), { aws: { signQuery: true } })).url;
}
const claveOk = (k: unknown) => String(k ?? "").startsWith("lessons/");

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const { data: cfg } = await admin.from("gen_config").select("valor").eq("clave", "token").single();
    if (!cfg || req.headers.get("x-gen-token") !== cfg.valor) return json({ error: "No autorizado" }, 401);
    const b = await req.json().catch(() => ({}));

    if (b.action === "siguiente") {
      const { data: r } = await admin.from("video_renders").select("id, lesson_id, plan").eq("status", "pendiente").order("created_at").limit(1).maybeSingle();
      if (!r) return json({ pedido: null });
      const plan = [];
      for (const p of r.plan as any[]) {
        if (!claveOk(p.key)) { await admin.from("video_renders").update({ status: "error", error: "Una parte no es un archivo cargado en la plataforma (los videos de YouTube no se pueden unir)", updated_at: new Date().toISOString() }).eq("id", r.id); return json({ pedido: null, saltado: r.id }); }
        plan.push({ url: await firmar("GET", p.key, 4 * 3600), i: p.i || 0, f: p.f || 0, key: p.key });
      }
      const salida = `lessons/${r.lesson_id}/${crypto.randomUUID().slice(0, 8)}-video-final.mp4`;
      await admin.from("video_renders").update({ status: "procesando", output_key: salida, updated_at: new Date().toISOString() }).eq("id", r.id);
      return json({ pedido: { id: r.id, plan, put_url: await firmar("PUT", salida, 4 * 3600) } });
    }

    if (b.action === "listo") {
      const { data: r } = await admin.from("video_renders").select("id, step_id, output_key, status").eq("id", b.id).single();
      if (!r || r.status !== "procesando" || !r.output_key) return json({ error: "Pedido inválido" }, 400);
      const { aws, base } = r2();
      const h = await aws.fetch(base(r.output_key), { method: "HEAD" });
      if (!h.ok) return json({ error: "El video final no está en el almacenamiento" }, 400);
      const { data: paso } = await admin.from("lesson_steps").select("stream_uid, content").eq("id", r.step_id).single();
      await admin.from("video_renders").update({ fuentes: { stream_uid: paso?.stream_uid ?? null, content: paso?.content ?? {} } }).eq("id", r.id);
      const u = await admin.from("lesson_steps").update({ stream_uid: r.output_key, content: { videos: [{ uid: r.output_key, nombre: "Video final.mp4", tramos: [], final: true }] } }).eq("id", r.step_id);
      if (u.error) return json({ error: u.error.message }, 500);
      await admin.from("video_renders").update({ status: "listo", error: null, updated_at: new Date().toISOString() }).eq("id", r.id);
      return json({ ok: true });
    }

    if (b.action === "error") {
      await admin.from("video_renders").update({ status: "error", error: String(b.error ?? "Error").slice(0, 500), updated_at: new Date().toISOString() }).eq("id", b.id);
      return json({ ok: true });
    }
    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: "Error inesperado" }, 500);
  }
});
