import { createClient } from "npm:@supabase/supabase-js@2";

// Reenvía una corrida de GitHub Actions (solo administrador). POST { run_id } -> vuelve a correr los pasos que fallaron
// (o toda la corrida si fue cancelada). Usa el secreto GITHUB_TOKEN_REENVIAR (token con permiso de Actions: lectura y escritura).
const REPO = "gabrielalvarez916-dot/waveacademys";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

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
    const { data: yo } = await admin.from("profiles").select("role, is_suspended").eq("id", user.id).single();
    if (yo?.is_suspended || yo?.role !== "admin") return json({ error: "Solo el administrador puede reenviar" }, 403);

    const token = Deno.env.get("GITHUB_TOKEN_REENVIAR");
    if (!token) return json({ error: "Falta guardar el token de GitHub (GITHUB_TOKEN_REENVIAR)" }, 412);
    const { run_id } = await req.json();
    if (!/^\d+$/.test(String(run_id))) return json({ error: "Corrida inválida" }, 400);
    const gh = (path: string) => fetch(`https://api.github.com/repos/${REPO}/actions/runs/${run_id}/${path}`, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" },
    });
    const info = await fetch(`https://api.github.com/repos/${REPO}/actions/runs/${run_id}`, {
      headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json" },
    });
    if (!info.ok) return json({ error: "No encontré esa corrida en GitHub (" + info.status + ")" }, 404);
    const run = await info.json();
    if (run.status !== "completed") return json({ error: "Esa corrida todavía no terminó" }, 409);
    let r = await gh(run.conclusion === "failure" ? "rerun-failed-jobs" : "rerun");
    if (!r.ok) {
      const t = await r.text();
      return json({ error: "GitHub no aceptó el reenvío (" + r.status + "): " + t.slice(0, 160) }, 502);
    }
    return json({ ok: true });
  } catch (e) {
    console.error(e);
    return json({ error: "No se pudo reenviar. Probá de nuevo." }, 500);
  }
});
