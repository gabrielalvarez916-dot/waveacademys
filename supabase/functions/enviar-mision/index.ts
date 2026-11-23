import { createClient } from "npm:@supabase/supabase-js@2";

// Envío manual de misiones (solo administrador).
//  { accion: "pendientes" } -> misiones subidas a GitHub que todavía no tienen examen cargado en la base.
//  { accion: "enviar", archivos: [...] } -> lanza la máquina de Avanzado y/o la de Medio con esas misiones.
// Usa el secreto GITHUB_TOKEN_REENVIAR (Actions: lectura y escritura).
const REPO = "gabrielalvarez916-dot/waveacademys";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });
const RUTA = /^contenido\/(?:medio\/)?[a-z0-9-]+\/mision-\d+\/mision-\d+\.json$/;
const CACHE = new Map<string, { subject_id: string; tema: number } | null>();

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
    if (yo?.is_suspended || yo?.role !== "admin") return json({ error: "Solo el administrador puede enviar" }, 403);
    const token = Deno.env.get("GITHUB_TOKEN_REENVIAR");
    if (!token) return json({ error: "Falta guardar el token de GitHub (GITHUB_TOKEN_REENVIAR)" }, 412);
    const H = { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" };
    const { accion, archivos } = await req.json();

    if (accion === "enviar") {
      const lista: string[] = (Array.isArray(archivos) ? archivos : []).map(String);
      if (!lista.length || lista.some((f) => !RUTA.test(f))) return json({ error: "Lista de misiones inválida" }, 400);
      const grupos: Record<string, string[]> = { "mision-avanzado.yml": [], "mision-medio.yml": [] };
      for (const f of lista) grupos[f.startsWith("contenido/medio/") ? "mision-medio.yml" : "mision-avanzado.yml"].push(f);
      const enviados: string[] = [];
      for (const [wf, fs] of Object.entries(grupos)) {
        if (!fs.length) continue;
        const runs = await (await fetch(`https://api.github.com/repos/${REPO}/actions/workflows/${wf}/runs?per_page=10`, { headers: H })).json();
        const enEspera = (runs.workflow_runs || []).some((r: any) => ["queued", "waiting", "pending"].includes(r.status));
        if (enEspera) return json({ error: `Ya hay una corrida en espera de ${wf.includes("medio") ? "Medio" : "Avanzado"}. Esperá a que arranque: si mandás otra, la que espera se pierde.` }, 409);
        const r = await fetch(`https://api.github.com/repos/${REPO}/actions/workflows/${wf}/dispatches`, {
          method: "POST", headers: H, body: JSON.stringify({ ref: "main", inputs: { mision: fs.join(" ") } }),
        });
        if (!r.ok) return json({ error: "GitHub no aceptó el envío (" + r.status + "): " + (await r.text()).slice(0, 160) }, 502);
        enviados.push(wf);
      }
      return json({ ok: true, enviados });
    }

    // pendientes
    const tree = await (await fetch(`https://api.github.com/repos/${REPO}/git/trees/main?recursive=1`, { headers: H })).json();
    const files: { path: string; sha: string }[] = (tree.tree || []).filter((t: any) => t.type === "blob" && RUTA.test(t.path));
    const faltan = files.filter((f) => !CACHE.has(f.sha));
    for (let i = 0; i < faltan.length; i += 15) {
      await Promise.all(faltan.slice(i, i + 15).map(async (f) => {
        try {
          const d = await (await fetch(`https://raw.githubusercontent.com/${REPO}/main/${f.path}`)).json();
          CACHE.set(f.sha, d.subject_id && d.tema ? { subject_id: d.subject_id, tema: Number(d.tema) } : null);
        } catch { CACHE.set(f.sha, null); }
      }));
    }
    const info = files.map((f) => ({ path: f.path, ...(CACHE.get(f.sha) || { subject_id: "", tema: 0 }) })).filter((f) => f.subject_id);
    const subs = [...new Set(info.map((i) => i.subject_id))];
    const { data: topics } = await admin.from("topics").select("id, subject_id, position").in("subject_id", subs);
    const tids = (topics || []).map((t: any) => t.id);
    const conExamen = new Set<string>();
    for (let i = 0; i < tids.length; i += 200) {
      const { data: ex } = await admin.from("exams").select("topic_id").in("topic_id", tids.slice(i, i + 200));
      (ex || []).forEach((e: any) => conExamen.add(e.topic_id));
    }
    const hecho = new Set((topics || []).filter((t: any) => conExamen.has(t.id)).map((t: any) => t.subject_id + "|" + t.position));
    const { data: sj } = await admin.from("subjects").select("id, name").in("id", subs);
    const nombre: Record<string, string> = {}; (sj || []).forEach((s: any) => nombre[s.id] = s.name);
    const pendientes = info.filter((i) => !hecho.has(i.subject_id + "|" + i.tema)).map((i) => ({
      path: i.path, nivel: i.path.startsWith("contenido/medio/") ? "Medio" : "Avanzado", materia: nombre[i.subject_id] || i.path.split("/").slice(-3, -2)[0], mision: i.tema,
    })).sort((a, b) => (a.nivel + a.materia).localeCompare(b.nivel + b.materia) || a.mision - b.mision);
    return json({ pendientes });
  } catch (e) {
    console.error(e);
    return json({ error: "No se pudo completar. Probá de nuevo." }, 500);
  }
});
