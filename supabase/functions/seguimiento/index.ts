import { createClient } from "npm:@supabase/supabase-js@2";

// JUANA, el agente de seguimiento. Cada domingo a la noche arma el informe semanal de cada alumno.
// Los números los calcula la base por reglas (seguimiento_datos). La IA solo redacta, y solo si hubo actividad.
// POST con header x-gen-token (lo llama el cron):  { action: "generar", desde?: "YYYY-MM-DD" (un lunes) }
const MODEL = "claude-haiku-5-5";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type, x-gen-token",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

// Lunes de la semana que está terminando (hora de Buenos Aires)
function lunesActual(): string {
  const ba = new Date(Date.now() - 3 * 3600 * 1000);
  const dow = ba.getUTCDay(); // 0 = domingo
  const lunes = new Date(Date.UTC(ba.getUTCFullYear(), ba.getUTCMonth(), ba.getUTCDate() - ((dow + 6) % 7)));
  return lunes.toISOString().slice(0, 10);
}

const FIJO_SIN_ACTIVIDAD = (n: string) =>
  `Esta semana ${n} no tuvo actividad en la plataforma. Si algo se le complica para empezar o no sabe por dónde seguir, escribime desde esta pestaña y lo pensamos juntas. También podés pedir una reunión con Dirección.`;

const SISTEMA = (neutro: boolean) => `Sos Juana, la persona de Seguimiento de Wave Academy. Escribís el informe semanal para la familia de un estudiante, en ${neutro ? "español neutro latinoamericano (tuteo)" : "español rioplatense (voseo)"}.
Reglas:
- Usá SOLO los datos del JSON. No inventes notas, materias, días ni hechos. Si un dato no está, no lo menciones.
- Tono cálido y claro, hablándole a la familia sobre su hijo o hija, por su nombre. Entre 5 y 7 oraciones.
- Primero lo bueno (lo que avanzó y lo que mejor le fue), después lo que le costó, con una sugerencia concreta y simple para acompañarlo en casa.
- Si hay notas bajas o dificultades, no alarmes ni dramatices: explicalas como una parte normal de aprender y decí qué se va a reforzar.
- Si "costaron" está vacío, no inventes dificultades: decilo con naturalidad.
- Podés mencionar que puede pedir una tutoría individual o una reunión con Dirección si lo ven necesario, en una sola oración y solo si hay dificultades.
- Texto plano: sin asteriscos, sin listas, sin títulos, sin emojis. Firmá al final solamente: Juana.`;

async function claude(system: string, datos: unknown) {
  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "content-type": "application/json", "x-api-key": Deno.env.get("ANTHROPIC_API_KEY")!, "anthropic-version": "2023-06-01" },
    body: JSON.stringify({ model: MODEL, max_tokens: 400, system, messages: [{ role: "user", content: "Datos de la semana:\n" + JSON.stringify(datos) }] }),
  });
  if (!r.ok) throw new Error("Claude API " + r.status + ": " + (await r.text()));
  const d = await r.json();
  const limpio = d.content.filter((b: any) => b.type === "text").map((b: any) => b.text).join("")
    .replace(/\*\*(.+?)\*\*/gs, "$1").replace(/^#{1,6}\s+/gm, "").replace(/^\s*[*•-]\s+/gm, "").trim();
  return { texto: limpio, inTok: d.usage?.input_tokens ?? 0, outTok: d.usage?.output_tokens ?? 0 };
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
    const b = await req.json().catch(() => ({}));
    const { data: cfg } = await admin.from("gen_config").select("valor").eq("clave", "token").maybeSingle();
    if (!cfg || req.headers.get("x-gen-token") !== cfg.valor) return json({ error: "No autorizado" }, 401);

    if (b.action === "generar") {
      const desde = /^\d{4}-\d{2}-\d{2}$/.test(String(b.desde ?? "")) ? String(b.desde) : lunesActual();
      if (new Date(desde + "T00:00:00Z").getUTCDay() !== 1) return json({ error: "La semana tiene que empezar un lunes" }, 400);
      const { data: alumnos } = await admin.from("students").select("id,family_id,first_name,apodo,curriculum").not("family_id", "is", null);
      const { data: hechos } = await admin.from("seguimiento_informes").select("student_id").eq("semana", desde);
      const ya = new Set((hechos ?? []).map((x: any) => x.student_id));
      let creados = 0, conIA = 0, errores = 0;
      for (const a of alumnos ?? []) {
        if (ya.has(a.id)) continue;
        try {
          const { data: datos, error } = await admin.rpc("seguimiento_datos", { p_student: a.id, p_desde: desde });
          if (error || !datos) throw error ?? new Error("sin datos");
          const nombre = a.apodo || a.first_name;
          let texto: string, origen = "ia", tIn: number | null = null, tOut: number | null = null;
          if (datos.sin_actividad) { texto = FIJO_SIN_ACTIVIDAD(nombre); origen = "fijo"; }
          else {
            const r = await claude(SISTEMA(String(a.curriculum ?? "").toLowerCase() === "internacional"), datos);
            texto = r.texto; tIn = r.inTok; tOut = r.outTok; conIA++;
          }
          const { error: e2 } = await admin.from("seguimiento_informes").insert({ student_id: a.id, semana: desde, datos, texto, origen, tokens_in: tIn, tokens_out: tOut });
          if (e2) throw e2;
          creados++;
          // Aviso dentro del panel (por ahora sin mail) a la familia y al tutor humano
          const { data: fam } = await admin.from("families").select("profile_id").eq("id", a.family_id).maybeSingle();
          const { data: tuts } = await admin.from("tutor_students").select("tutor_id").eq("student_id", a.id);
          const avisos = [
            ...(fam?.profile_id ? [{ profile_id: fam.profile_id, texto: `Juana preparó el informe semanal de ${nombre}. Lo ves en la pestaña Juana.` }] : []),
            ...(tuts ?? []).map((t: any) => ({ profile_id: t.tutor_id, texto: `Informe semanal de ${nombre}, preparado por Juana.` })),
          ].map((x) => ({ ...x, tipo: "seguimiento", titulo: `Informe semanal de ${nombre}`, email_pendiente: false }));
          if (avisos.length) await admin.from("notificaciones").insert(avisos);
        } catch (e) { errores++; console.error("informe", a.id, e); }
      }
      return json({ ok: true, semana: desde, creados, con_ia: conIA, errores });
    }
    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: "No se pudo generar" }, 500);
  }
});
