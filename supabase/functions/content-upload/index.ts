import { createClient } from "npm:@supabase/supabase-js@2";
import { AwsClient } from "npm:aws4fetch@1";

// Subida de contenido desde el panel de administración.
// Todo (videos, PDF y descargables) va a Cloudflare R2 con URL firmada temporal.
// Secretos: R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY y R2_BUCKET.

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

const env = (k: string) => (Deno.env.get(k) ?? "").trim().replace(/^["']|["']$/g, "").trim();
const R2_KEYS = ["R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET"];
const faltan = (ks: string[]) => ks.filter((k) => !env(k));

function r2() {
  const aws = new AwsClient({
    accessKeyId: env("R2_ACCESS_KEY_ID"), secretAccessKey: env("R2_SECRET_ACCESS_KEY"), service: "s3", region: "auto",
  });
  const base = (key: string) =>
    `https://${env("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com/${env("R2_BUCKET")}/${key.split("/").map(encodeURIComponent).join("/")}`;
  return { aws, base };
}

async function firmar(method: string, key: string, segundos: number) {
  const { aws, base } = r2();
  const u = new URL(base(key));
  u.searchParams.set("X-Amz-Expires", String(segundos));
  const signed = await aws.sign(new Request(u, { method }), { aws: { signQuery: true } });
  return signed.url;
}

// Copia liviana (720p) que usa el editor: lessons/<lec>/_edicion/<nombre>.mp4 (la genera el botón "Optimizar" de Videos)
const proxyDe = (key: string) => key.replace(/^(lessons\/[^/]+\/)(.*?)(\.[^./]+)?$/, "$1_edicion/$2.mp4");

const limpiarNombre = (n: string) =>
  n.normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-zA-Z0-9._-]+/g, "-").replace(/^-+|-+$/g, "").slice(-80) || "archivo";

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
    const { data: me } = await admin.from("profiles").select("role").eq("id", user.id).maybeSingle();
    if (me?.role !== "admin") return json({ error: "Solo administradores" }, 403);

    const body = await req.json();
    const sinR2 = () => json({ error: "Faltan secretos en Supabase: " + faltan(R2_KEYS).join(", ") }, 400);
    const claveOk = (k: unknown) => String(k ?? "").startsWith("lessons/");

    switch (body.action) {
      case "config": {
        const f = faltan(R2_KEYS);
        return json({ archivos: f.length === 0, videos: f.length === 0, faltan_archivos: f, faltan_videos: f });
      }

      case "r2_upload_url": {
        if (faltan(R2_KEYS).length) return sinR2();
        if (!body.lesson_id || !body.filename) return json({ error: "Faltan datos" }, 400);
        const key = `lessons/${body.lesson_id}/${crypto.randomUUID().slice(0, 8)}-${limpiarNombre(String(body.filename))}`;
        return json({ url: await firmar("PUT", key, 6 * 3600), key });
      }

      case "r2_download_url": {
        if (faltan(R2_KEYS).length) return sinR2();
        if (!claveOk(body.key)) return json({ error: "Clave inválida" }, 400);
        return json({ url: await firmar("GET", body.key, 600) });
      }

      case "r2_delete": {
        if (faltan(R2_KEYS).length) return sinR2();
        if (!claveOk(body.key)) return json({ error: "Clave inválida" }, 400);
        const { aws, base } = r2();
        const r = await aws.fetch(base(body.key), { method: "DELETE" });
        return json({ ok: r.ok || r.status === 404 });
      }

      // Videos: el "uid" del video es la clave del archivo en R2
      case "stream_status": {
        if (faltan(R2_KEYS).length) return sinR2();
        if (!claveOk(body.uid)) return json({ error: "Este video no está cargado" }, 404);
        const { aws, base } = r2();
        const r = await aws.fetch(base(String(body.uid)), { method: "HEAD" });
        if (!r.ok) return json({ error: "No se encontró el video" }, 404);
        return json({ ready: true, size: Number(r.headers.get("content-length") ?? 0) });
      }

      case "stream_token": {
        if (faltan(R2_KEYS).length) return sinR2();
        if (!claveOk(body.uid)) return json({ error: "Este video no está cargado" }, 404);
        // Con preview: si existe la copia liviana de edición, el editor abre esa (el alumno siempre ve el original)
        if (body.preview) {
          const { aws, base } = r2();
          const pk = proxyDe(String(body.uid));
          const h = await aws.fetch(base(pk), { method: "HEAD" });
          if (h.ok) return json({ url: await firmar("GET", pk, 4 * 3600), liviano: true });
        }
        return json({ url: await firmar("GET", String(body.uid), 4 * 3600) });
      }

      case "stream_delete": {
        if (faltan(R2_KEYS).length) return sinR2();
        if (!claveOk(body.uid)) return json({ ok: true });
        const { aws, base } = r2();
        const r = await aws.fetch(base(String(body.uid)), { method: "DELETE" });
        await aws.fetch(base(proxyDe(String(body.uid))), { method: "DELETE" }).catch(() => null);
        return json({ ok: r.ok || r.status === 404 });
      }

      default:
        return json({ error: "Acción desconocida" }, 400);
    }
  } catch (e) {
    console.error(e);
    return json({ error: "Error inesperado" }, 500);
  }
});
