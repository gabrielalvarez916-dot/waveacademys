import { createClient } from "npm:@supabase/supabase-js@2";
import * as L from "./logica.js";

const MODEL = "claude-haiku-5-5";
const MAX_MATERIAL = 9000; // solo la misión abierta, nunca todas
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });
const uno = (x: any) => (Array.isArray(x) ? x[0] : x);

async function claude(system: any[], messages: any[]) {
  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "content-type": "application/json", "x-api-key": Deno.env.get("ANTHROPIC_API_KEY")!, "anthropic-version": "2023-06-01" },
    body: JSON.stringify({ model: MODEL, max_tokens: 450, system, messages }),
  });
  if (!r.ok) throw new Error("Claude API " + r.status + ": " + (await r.text()));
  const d = await r.json();
  return {
    texto: L.limpiar(d.content.filter((b: any) => b.type === "text").map((b: any) => b.text).join("")),
    inTok: (d.usage?.input_tokens ?? 0) + (d.usage?.cache_creation_input_tokens ?? 0) + (d.usage?.cache_read_input_tokens ?? 0),
    outTok: d.usage?.output_tokens ?? 0,
  };
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const url = Deno.env.get("SUPABASE_URL")!;
    const userClient = createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, {
      global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } },
    });
    const admin = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
    const { data: { user } } = await userClient.auth.getUser();
    if (!user) return json({ error: "No autenticado" }, 401);

    const body = await req.json();
    const { data: student } = await admin.from("students")
      .select("id,first_name,apodo,tutor_nombre,tutor_personalidad,birth_date,curriculum,grades(name,levels(name))")
      .eq("profile_id", user.id).maybeSingle();
    if (!student) return json({ error: "El chat es solo para estudiantes" }, 403);
    const nombre = student.apodo || student.first_name;
    const tutor = student.tutor_nombre || "Tutor Wave";

    // ---------- Reservar tutoría (la confirma el alumno con un botón; el tutor solo sugiere) ----------
    if (body.reservar_inicio) {
      const { error } = await userClient.rpc("reservar_tutoria", { p_student: student.id, p_inicio: body.reservar_inicio, p_tema: String(body.tema ?? "Consulta desde el tutor").slice(0, 200) });
      if (error) return json({ error: error.message }, 400);
      return json({ reply: `Listo, ${nombre}. Tu tutoría quedó agendada. Te va a llegar el aviso.`, reservada: true });
    }

    const message = String(body.message ?? "").trim().slice(0, 1500);
    const accion: string | null = L.ACCIONES[body.accion as keyof typeof L.ACCIONES] ? body.accion : null;
    if (!message && !accion) return json({ error: "Escribí tu consulta o tocá un botón" }, 400);

    // ---------- Contexto: SOLO la misión abierta ----------
    let lessonId: string | null = body.lesson_id ?? null;
    const stepId: string | null = body.lesson_step_id ?? null;
    const topicId: string | null = body.topic_id ?? null;
    let etiqueta = "";
    let material = "";
    let subjectId: string | null = null;

    if (stepId) {
      const { data: st } = await userClient.from("lesson_steps").select("id,lesson_id,title,step_type").eq("id", stepId).maybeSingle();
      if (!st) return json({ error: "Sin acceso a este contenido" }, 403);
      lessonId = st.lesson_id;
      if (st.step_type === "pdf") {
        const { data: tx } = await admin.from("lesson_steps").select("extracted_text").eq("id", stepId).maybeSingle();
        material = (tx?.extracted_text ?? "").slice(0, MAX_MATERIAL);
      }
    }
    let lessonIds: string[] = [];
    if (lessonId) {
      const { data: lesson } = await userClient.from("lessons").select("id,title,position,topic_id,topics(title,subject_id,subjects(name))").eq("id", lessonId).maybeSingle();
      if (!lesson) return json({ error: "Sin acceso a este contenido" }, 403);
      const tp: any = uno((lesson as any).topics), sj: any = tp ? uno(tp.subjects) : null;
      subjectId = tp?.subject_id ?? null;
      etiqueta = `Materia: ${sj?.name ?? ""} | Misión: ${tp?.title ?? ""} | Lección: ${lesson.title}`;
      lessonIds = [lesson.id];
      if ((lesson as any).position > 4 && lesson.topic_id) { // práctica general: el material son las 4 lecciones de la misión
        const { data: ls } = await userClient.from("lessons").select("id,position").eq("topic_id", lesson.topic_id).lte("position", 4).order("position");
        if (ls?.length) { lessonIds = ls.map((l: any) => l.id); etiqueta += " (práctica general de la misión)"; }
      }
    } else if (topicId) {
      const { data: tp } = await userClient.from("topics").select("id,title,subject_id,subjects(name),lessons(id,position)").eq("id", topicId).maybeSingle();
      if (!tp) return json({ error: "Sin acceso a este contenido" }, 403);
      const sj: any = uno((tp as any).subjects);
      subjectId = (tp as any).subject_id;
      etiqueta = `Materia: ${sj?.name ?? ""} | Misión: ${(tp as any).title}`;
      lessonIds = ((tp as any).lessons ?? []).filter((l: any) => l.position <= 4).sort((a: any, b: any) => a.position - b.position).map((l: any) => l.id);
      lessonId = lessonIds[0] ?? null;
    }
    if (!material && lessonIds.length) {
      const { data: pdfs } = await admin.from("lesson_steps").select("lesson_id,extracted_text").in("lesson_id", lessonIds).eq("step_type", "pdf");
      const orden = new Map(lessonIds.map((id, i) => [id, i]));
      material = (pdfs ?? []).sort((a: any, b: any) => (orden.get(a.lesson_id) ?? 0) - (orden.get(b.lesson_id) ?? 0))
        .map((p: any) => p.extracted_text ?? "").filter(Boolean).join("\n---\n").slice(0, MAX_MATERIAL);
    }
    const pantalla = ["pdf", "clase", "actividad", "practica", "jefe"].includes(body.pantalla) ? body.pantalla : "pdf";
    const textoPregunta = String(body.pregunta_texto ?? "").slice(0, 600);
    if (textoPregunta) etiqueta += ` | Pregunta que está resolviendo: ${textoPregunta}`;
    etiqueta += ` | Pantalla: ${pantalla}`;

    // Respuesta correcta (solo servidor): para guiar sin regalarla y para controlar que no se escape
    let secretas: string[] = [];
    if (body.question_id) {
      const { data: q } = await userClient.from("questions").select("id,prompt").eq("id", body.question_id).maybeSingle();
      if (q) {
        const { data: rb } = await admin.from("question_rubrics").select("reference_answer").eq("question_id", q.id).maybeSingle();
        secretas = L.respuestasSecretas(rb?.reference_answer, q.prompt);
      }
    }

    // ---------- Tutoría con el tutor humano: sin IA ----------
    if (accion === "tutoria" || /(tutor humano|hablar con (mi )?tutor|quiero una tutor|agendar.{0,15}tutor)/.test(L.norm(message))) {
      const { data: turnos, error } = await userClient.rpc("turnos_disponibles", { p_student: student.id, p_dias: 14 });
      if (error || !turnos?.length) {
        return json({ reply: `${nombre}, por ahora no tengo horarios libres de tu tutor para ofrecerte. Pedile a tu familia que lo vea desde su panel, en Tutorías.`, remaining: null });
      }
      return json({ reply: `${nombre}, estos son los próximos horarios de tu tutor. Elegí uno y lo agendamos.`, turnos: turnos.slice(0, 6), remaining: null });
    }

    // ---------- Topes de uso ----------
    const { data: cfg } = await admin.from("app_settings").select("key,value").in("key", ["chat_daily_message_limit", "chat_history_max", "chat_monthly_token_limit"]);
    const cv = (k: string, d: number) => Number(cfg?.find((c: any) => c.key === k)?.value ?? d);
    const limite = cv("chat_daily_message_limit", 30), histMax = cv("chat_history_max", 6), topeMes = cv("chat_monthly_token_limit", 400000);
    const ba = new Date(Date.now() - 3 * 3600 * 1000);
    const iniDia = new Date(Date.UTC(ba.getUTCFullYear(), ba.getUTCMonth(), ba.getUTCDate(), 3)).toISOString();
    const iniMes = new Date(Date.UTC(ba.getUTCFullYear(), ba.getUTCMonth(), 1, 3)).toISOString();
    const { data: convs } = await admin.from("chat_conversations").select("id").eq("student_id", student.id);
    const convIds = (convs ?? []).map((c: any) => c.id);
    let usados = 0, tokensMes = 0;
    if (convIds.length) {
      const { count } = await admin.from("chat_messages").select("id", { count: "exact", head: true }).in("conversation_id", convIds).eq("role", "user").gte("created_at", iniDia);
      usados = count ?? 0;
      const { data: tk } = await admin.from("chat_messages").select("input_tokens,output_tokens").in("conversation_id", convIds).eq("role", "assistant").gte("created_at", iniMes);
      tokensMes = (tk ?? []).reduce((a: number, m: any) => a + (m.input_tokens ?? 0) + (m.output_tokens ?? 0), 0);
    }
    if (usados >= limite) return json({ error: `Llegaste al límite de ${limite} mensajes de hoy. Mañana podés seguir consultando.`, remaining: 0 }, 429);
    if (tokensMes >= topeMes) return json({ error: "Llegaste al límite de consultas de este mes. Hablá con tu tutor o con tu familia para seguir.", remaining: 0 }, 429);

    // ---------- Conversación ----------
    let convId: string | null = body.conversation_id ?? null;
    let conv: any = null;
    if (convId) {
      const { data: c } = await admin.from("chat_conversations").select("id,ayudas,pistas,escalado").eq("id", convId).eq("student_id", student.id).maybeSingle();
      if (!c) return json({ error: "Conversación no encontrada" }, 404);
      conv = c;
    } else {
      const { data: c, error } = await admin.from("chat_conversations").insert({
        student_id: student.id, lesson_step_id: stepId, lesson_id: lessonId, subject_id: subjectId, pantalla, title: (message || accion || "").slice(0, 60),
      }).select("id,ayudas,pistas,escalado").single();
      if (error) throw error;
      conv = c; convId = c.id;
    }
    const guardar = async (usuario: string, respuesta: string, inTok: number | null, outTok: number | null) => {
      await admin.from("chat_messages").insert([
        { conversation_id: convId, role: "user", content: usuario },
        { conversation_id: convId, role: "assistant", content: respuesta, input_tokens: inTok, output_tokens: outTok },
      ]);
      await admin.from("chat_conversations").update({ updated_at: new Date().toISOString() }).eq("id", convId);
    };
    const textoUsuario = message || `[Botón: ${L.ACCIONES[accion as keyof typeof L.ACCIONES].diag}]`;

    // ---------- Fuera de tema: respuesta fija, sin IA ----------
    if (L.esFueraDeTema(message, etiqueta + " " + material.slice(0, 3000), accion)) {
      const r = L.FUERA_DE_TEMA(nombre);
      await guardar(textoUsuario, r, null, null);
      return json({ conversation_id: convId, reply: r, remaining: limite - usados - 1, tutor: tutor });
    }

    // ---------- Contadores y señales (por reglas) ----------
    const ayudas = (conv.ayudas ?? 0) + 1;
    const pistas = (conv.pistas ?? 0) + (accion === "pista" ? 1 : 0);
    const escalar = L.debeEscalar({ ayudas, pistas, escalado: !!conv.escalado });
    const perfil = L.perfilEdad({ birth_date: student.birth_date, nivel: uno(uno((student as any).grades)?.levels)?.name });
    const neutro = L.norm(student.curriculum) === "internacional";

    const { data: hist } = await admin.from("chat_messages").select("role,content").eq("conversation_id", convId).order("created_at", { ascending: false }).limit(histMax);
    const mensajes = (hist ?? []).reverse().map((m: any) => ({ role: m.role, content: m.content }));
    while (mensajes.length && mensajes[0].role !== "user") mensajes.shift();
    mensajes.push({ role: "user", content: textoUsuario });

    const sistema = L.armarSistema({ alumno: nombre, tutor, personalidad: student.tutor_personalidad, perfil, neutro, accion, pistas, contexto: etiqueta, material, secretas, escalar });
    let r = await claude(sistema, mensajes);
    let inTok = r.inTok, outTok = r.outTok;
    if (secretas.length && L.revelaRespuesta(r.texto, secretas)) {
      const sist2 = [...sistema]; sist2[0] = { type: "text", text: sistema[0].text + "\nATENCIÓN: tu respuesta anterior revelaba la respuesta correcta. Rehacela SIN decirla ni insinuarla, usando un ejemplo con otros datos." };
      r = await claude(sist2, mensajes);
      inTok += r.inTok; outTok += r.outTok;
      if (L.revelaRespuesta(r.texto, secretas)) r.texto = L.SIN_RESPUESTA;
    }
    await guardar(textoUsuario, r.texto, inTok, outTok);
    await admin.from("chat_conversations").update({ ayudas, pistas, escalado: !!conv.escalado || escalar }).eq("id", convId);

    // ---------- Memoria de lo que le cuesta ----------
    if (lessonId) {
      for (const senal of L.senalesDe({ accion, ayudas, pistas })) {
        const { data: f } = await admin.from("alumno_dificultades").select("veces").eq("student_id", student.id).eq("lesson_id", lessonId).eq("senal", senal).maybeSingle();
        if (f) await admin.from("alumno_dificultades").update({ veces: f.veces + 1, ultima_at: new Date().toISOString(), resuelta: false }).eq("student_id", student.id).eq("lesson_id", lessonId).eq("senal", senal);
        else await admin.from("alumno_dificultades").insert({ student_id: student.id, lesson_id: lessonId, senal });
      }
    }
    return json({ conversation_id: convId, reply: r.texto, remaining: limite - usados - 1, ofrecer_tutoria: escalar, tutor });
  } catch (e) {
    console.error(e);
    return json({ error: "El tutor no pudo responder ahora. Intentá de nuevo en un momento." }, 500);
  }
});
