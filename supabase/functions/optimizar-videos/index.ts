import { createClient } from "npm:@supabase/supabase-js@2";
import { AwsClient } from "npm:aws4fetch@1";

// OPTIMIZAR VIDEOS · reordena los MP4 cargados para que abran al instante (ffmpeg -c copy -movflags +faststart, sin recodificar, sin perder calidad).
// Lo hace GitHub Actions (tools/optimizar/optimizar.py) y SOLO cuando el admin toca el botón en Videos.
// Desde el panel (sesión de administrador): { action: "contar" } | { action: "pedir" }
// Desde el proceso (header x-gen-token):    { action: "lote" } | { action: "listo", key, estado, nota }
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
const claveOk = (k: unknown) => typeof k === "string" && k.startsWith("lessons/");

// Todos los archivos de video cargados en la plataforma (no los de YouTube) que todavía no se revisaron
async function pendientes(): Promise<{ total: number; faltan: string[] }> {
  const { data: pasos, error } = await admin.from("lesson_steps").select("stream_uid, content").eq("step_type", "video");
  if (error) throw error;
  const claves = new Set<string>();
  for (const p of pasos ?? []) {
    if (claveOk(p.stream_uid)) claves.add(p.stream_uid);
    const vs = (p as any).content?.videos;
    if (Array.isArray(vs)) for (const v of vs) if (claveOk(v?.uid)) claves.add(v.uid);
  }
  const { data: hechos } = await admin.from("video_optimizados").select("key");
  const ya = new Set((hechos ?? []).map((h: any) => h.key));
  const faltan = [...claves].filter((k) => !ya.has(k)).sort();
  return { total: claves.size, faltan };
}

const REPO = "gabrielalvarez916-dot/waveacademys";
async function lanzarProceso(): Promise<string | null> {
  const tk = Deno.env.get("GITHUB_TOKEN_RENDER") || Deno.env.get("GITHUB_TOKEN_PDF");
  if (!tk) return "Falta el token de GitHub en Supabase";
  const r = await fetch(`https://api.github.com/repos/${REPO}/actions/workflows/optimizar-videos.yml/dispatches`, {
    method: "POST",
    headers: { Authorization: `Bearer ${tk.trim()}`, Accept: "application/vnd.github+json", "Content-Type": "application/json", "User-Agent": "wave-academy" },
    body: JSON.stringify({ ref: "main" }),
  });
  return r.status === 204 ? null : `GitHub respondió ${r.status}`;
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    // ---- Desde el panel de administración ----
    if (req.headers.get("x-gen-token") == null) {
      const userClient = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } } });
      const { data: { user } } = await userClient.auth.getUser();
      if (!user) return json({ error: "No autenticado" }, 401);
      const { data: me } = await admin.from("profiles").select("role").eq("id", user.id).maybeSingle();
      if (me?.role !== "admin") return json({ error: "Solo administradores" }, 403);
      const q = await req.json().catch(() => ({}));
      if (q.action === "contar") {
        const p = await pendientes();
        return json({ total: p.total, pendientes: p.faltan.length });
      }
      if (q.action === "pedir") {
        const p = await pendientes();
        if (!p.faltan.length) return json({ ok: true, lanzado: false, pendientes: 0 });
        const falla = await lanzarProceso().catch((e) => String(e?.message || e));
        return json({ ok: true, lanzado: !falla, aviso: falla, pendientes: p.faltan.length });
      }
      return json({ error: "Acción desconocida" }, 400);
    }

    // ---- Desde el proceso de GitHub ----
    const { data: cfg } = await admin.from("gen_config").select("valor").eq("clave", "token").single();
    if (!cfg || req.headers.get("x-gen-token") !== cfg.valor) return json({ error: "No autorizado" }, 401);
    const b = await req.json().catch(() => ({}));

    if (b.action === "lote") {
      const p = await pendientes();
      const lote = [];
      for (const key of p.faltan.slice(0, 10)) {
        lote.push({ key, get_url: await firmar("GET", key, 4 * 3600), put_url: await firmar("PUT", key, 4 * 3600) });
      }
      return json({ lote, quedan: p.faltan.length });
    }

    if (b.action === "listo") {
      if (!claveOk(b.key)) return json({ error: "Clave inválida" }, 400);
      const estado = ["ok", "optimizado", "omitido", "error"].includes(b.estado) ? b.estado : "error";
      const { error } = await admin.from("video_optimizados").upsert({ key: b.key, estado, nota: String(b.nota ?? "").slice(0, 500), updated_at: new Date().toISOString() });
      if (error) return json({ error: error.message }, 500);
      return json({ ok: true });
    }
    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: "Error inesperado" }, 500);
  }
});
