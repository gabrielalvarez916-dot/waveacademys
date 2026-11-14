import { createClient } from "npm:@supabase/supabase-js@2";

// FÁBRICA DE LECCIONES (versión mínima)
// Toma la ficha de una lección (lesson_fichas) y genera, en 3 pasos encadenados, un BORRADOR en lesson_drafts:
//   1) contenido de la lección  2) las 8 consignas con criterios  3) revisión crítica de errores.
// Nunca publica nada: el borrador lo revisa la admin.
// Acciones (POST, header x-gen-token): { action:"encolar", tema_id } | { action:"procesar", draft_id } | { action:"reintentar", draft_id } | { action:"estado", tema_id }
declare const EdgeRuntime: { waitUntil(p: Promise<unknown>): void } | undefined;

const MODEL = "claude-sonnet-5-5";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type, x-gen-token",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

// ---------------- Claude con salida estructurada ----------------
async function claudeTool(system: string, user: string, tool: any, max_tokens: number) {
  let ultimo = "";
  for (let intento = 0; intento < 2; intento++) {
    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "content-type": "application/json", "x-api-key": Deno.env.get("ANTHROPIC_API_KEY")!, "anthropic-version": "2023-06-01" },
      body: JSON.stringify({
        model: MODEL, max_tokens, system: system + `\n\nIMPORTANTE: entregá el resultado ÚNICAMENTE llamando a la herramienta "${tool.name}". No escribas texto fuera de la herramienta.`, messages: [{ role: "user", content: user }],
        tools: [tool], tool_choice: { type: "auto" },
      }),
    });
    if (!r.ok) {
      ultimo = "Claude API " + r.status + ": " + (await r.text());
      if (r.status === 429 || r.status >= 500) { await new Promise((ok) => setTimeout(ok, 4000)); continue; }
      throw new Error(ultimo);
    }
    const d = await r.json();
    const b = d.content.find((x: any) => x.type === "tool_use");
    if (!b) throw new Error("La IA no devolvió datos estructurados");
    if (d.stop_reason === "max_tokens") throw new Error("La respuesta de la IA se cortó por largo");
    return b.input;
  }
  throw new Error(ultimo || "Falló la llamada a la IA");
}

// ---------------- herramientas (esquemas) ----------------
const TOOL_CONTENIDO = {
  name: "guardar_leccion",
  description: "Guarda el material de estudio de la lección.",
  input_schema: {
    type: "object",
    properties: {
      objetivo: { type: "string", description: "1 o 2 frases: qué va a entender el alumno" },
      vas_a_ver: { type: "array", items: { type: "string" }, description: "4 a 6 puntos cortos" },
      secciones: {
        type: "array",
        description: "De 4 a 6 secciones numeradas por el sistema",
        items: {
          type: "object",
          properties: {
            titulo: { type: "string" },
            bloques: {
              type: "array",
              items: {
                type: "object",
                properties: {
                  tipo: { type: "string", enum: ["parrafo", "definicion", "importante", "tip", "ojo", "ejemplo", "pasos", "lista", "tabla"] },
                  titulo: { type: "string", description: "Para importante, ejemplo y tabla (opcional en los demás)" },
                  texto: { type: "string", description: "Texto del bloque. Se permite <b>negrita</b> para términos clave. En ejemplo: el planteo del ejemplo. En tabla: pie explicativo." },
                  items: { type: "array", items: { type: "string" }, description: "Para pasos, lista y ejemplo (los pasos de resolución)" },
                  columnas: { type: "array", items: { type: "string" }, description: "Solo tabla" },
                  filas: { type: "array", items: { type: "array", items: { type: "string" } }, description: "Solo tabla" },
                },
                required: ["tipo"],
              },
            },
          },
          required: ["titulo", "bloques"],
        },
      },
      resumen: {
        type: "array",
        items: { type: "object", properties: { titulo: { type: "string" }, texto: { type: "string" } }, required: ["titulo", "texto"] },
        description: "4 a 6 tarjetas de resumen",
      },
      glosario: {
        type: "array",
        items: { type: "object", properties: { palabra: { type: "string" }, significado: { type: "string" } }, required: ["palabra", "significado"] },
        description: "5 a 8 términos",
      },
    },
    required: ["objetivo", "vas_a_ver", "secciones", "resumen", "glosario"],
  },
};

const TOOL_CONSIGNAS = {
  name: "guardar_consignas",
  description: "Guarda las 8 consignas de la actividad por consigna.",
  input_schema: {
    type: "object",
    properties: {
      consignas: {
        type: "array",
        items: {
          type: "object",
          properties: {
            tipo: { type: "string", enum: ["true_false", "multiple_choice", "short_answer", "open"] },
            enunciado: { type: "string" },
            opciones: { type: "array", items: { type: "string" }, description: "multiple_choice: 4 opciones. true_false: [\"Verdadero\",\"Falso\"]. Resto: omitir." },
            respuesta: { type: "string", description: "Respuesta correcta o de referencia. En multiple_choice y true_false, idéntica a una de las opciones." },
            puntos: { type: "integer" },
            criterios: { type: "string", description: "Cómo corregir, con puntaje parcial" },
            explicacion: { type: "string", description: "Por qué es esa la respuesta (didáctica)" },
          },
          required: ["tipo", "enunciado", "respuesta", "puntos", "criterios", "explicacion"],
        },
      },
    },
    required: ["consignas"],
  },
};

const TOOL_REVISION = {
  name: "guardar_revision",
  description: "Guarda el resultado de la revisión del borrador.",
  input_schema: {
    type: "object",
    properties: {
      apto: { type: "boolean", description: "true si no hay errores graves ni medios" },
      resumen: { type: "string", description: "Veredicto general en 2 o 3 frases" },
      problemas: {
        type: "array",
        items: {
          type: "object",
          properties: {
            donde: { type: "string", description: "Sección o consigna donde está" },
            descripcion: { type: "string" },
            correccion: { type: "string", description: "Cómo debería decir" },
            gravedad: { type: "string", enum: ["alta", "media", "baja"] },
          },
          required: ["donde", "descripcion", "gravedad"],
        },
      },
    },
    required: ["apto", "resumen", "problemas"],
  },
};

// ---------------- instrucciones ----------------
const ESTILO = `Sos un docente de matemática argentino, muy claro, que escribe material de estudio para Wave Academy, una escuela de educación en casa (homeschooling).
Escribís para chicos y chicas de 12 a 13 años. Español rioplatense con voseo (podés, fijate, mirá, hacé). Tono cálido y directo, sin infantilizar ni usar jerga innecesaria.
Notación argentina: punto para separar miles (1.250) y coma para los decimales (3,5). Las cuentas se muestran paso a paso.
Reglas de contenido: 1) Todo lo que afirmás tiene que ser matemáticamente correcto: recalculá cada cuenta antes de escribirla. 2) Respetá la ficha: tratá solo los contenidos indicados y NO incluyas lo que figura como "no entra". 3) Usá lo que el alumno ya vio, sin volver a explicarlo y sin adelantar lo que se ve en lecciones posteriores. 4) No incluyas ejercicios para resolver (hay actividades aparte): sí ejemplos resueltos. 5) No inventes datos históricos ni anécdotas; si no estás seguro, no lo pongas. 6) Texto plano; solo se permite <b>negrita</b> en términos clave.`;

type Ctx = { ficha: any; titulo: string; tema: string; materia: string; anio: number; vistas: string[]; siguientes: string[] };

function aTextoFicha(c: Ctx) {
  const f = c.ficha;
  return [
    `Materia: ${c.materia} (${c.anio}.º año de secundaria). Tema: ${c.tema}. Lección: ${c.titulo}.`,
    `OBJETIVO: ${f.objetivo}`,
    `CONTENIDOS QUE ENTRAN: ${(f.contenidos || []).join("; ")}`,
    f.no_entra ? `NO ENTRA: ${f.no_entra}` : "",
    f.previos ? `LO QUE EL ALUMNO YA VIO: ${f.previos}` : "",
    `ERRORES TÍPICOS A MOSTRAR: ${(f.errores_tipicos || []).join("; ")}`,
    c.vistas.length ? `LECCIONES YA VISTAS (en orden): ${c.vistas.join(" | ")}` : "",
    c.siguientes.length ? `LECCIONES QUE VIENEN DESPUÉS (no adelantes su contenido): ${c.siguientes.join(" | ")}` : "",
    f.notas ? `NOTAS: ${f.notas}` : "",
  ].filter(Boolean).join("\n");
}

function aTextoLeccion(c: any): string {
  const out: string[] = [`OBJETIVO: ${c.objetivo}`];
  (c.secciones || []).forEach((s: any, i: number) => {
    out.push(`\n## ${i + 1}. ${s.titulo}`);
    (s.bloques || []).forEach((b: any) => {
      const cab = b.titulo ? `[${b.tipo}: ${b.titulo}] ` : `[${b.tipo}] `;
      let t = cab + (b.texto || "");
      if (b.items?.length) t += "\n" + b.items.map((x: string) => "  - " + x).join("\n");
      if (b.columnas?.length) t += "\n  | " + b.columnas.join(" | ") + " |\n" + (b.filas || []).map((f: string[]) => "  | " + f.join(" | ") + " |").join("\n");
      out.push(t);
    });
  });
  if (c.glosario?.length) out.push("\nGLOSARIO: " + c.glosario.map((g: any) => `${g.palabra}: ${g.significado}`).join(" · "));
  return out.join("\n");
}

async function contexto(lessonId: string): Promise<Ctx> {
  const { data: f } = await admin.from("lesson_fichas").select("*").eq("lesson_id", lessonId).single();
  if (!f) throw new Error("La lección no tiene ficha");
  const { data: l } = await admin.from("lessons").select("id, title, position, topic_id").eq("id", lessonId).single();
  const { data: t } = await admin.from("topics").select("id, title, position, subject_id").eq("id", l!.topic_id).single();
  const { data: su } = await admin.from("subjects").select("name, grade_id").eq("id", t!.subject_id).single();
  const { data: g } = await admin.from("grades").select("year_number").eq("id", su!.grade_id).single();
  const { data: temas } = await admin.from("topics").select("id, title, position").eq("subject_id", t!.subject_id).order("position");
  const { data: lecs } = await admin.from("lessons").select("title, position, topic_id").in("topic_id", temas!.map((x: any) => x.id));
  const orden = (temas as any[]).flatMap((tm) =>
    (lecs as any[]).filter((x) => x.topic_id === tm.id).sort((a, b) => a.position - b.position).map((x) => ({ id: tm.id, tema: tm.title, titulo: x.title, pos: x.position })),
  );
  const i = orden.findIndex((x) => x.id === t!.id && x.pos === l!.position);
  return {
    ficha: f, titulo: l!.title, tema: t!.title, materia: su!.name, anio: g!.year_number,
    vistas: orden.slice(0, i).map((x) => `${x.tema}: ${x.titulo}`),
    siguientes: orden.slice(i + 1, i + 7).map((x) => `${x.tema}: ${x.titulo}`),
  };
}

// ---------------- pasos ----------------
async function pasoContenido(c: Ctx) {
  const user = `${aTextoFicha(c)}\n\nEscribí el material de estudio de esta lección: de 4 a 6 secciones, con ejemplos resueltos paso a paso, recuadros de "importante", "tip" y "ojo con esto" (error común, tomado de los errores típicos), al menos una definición y, si ayuda, una tabla. Largo total: entre 1.100 y 1.700 palabras. Terminá con un resumen en tarjetas y un glosario.`;
  const r = await claudeTool(ESTILO, user, TOOL_CONTENIDO, 10000);
  if (!Array.isArray(r.secciones) || r.secciones.length < 3) throw new Error("El contenido salió con muy pocas secciones");
  return r;
}

async function pasoConsignas(c: Ctx, contenido: any) {
  const system = ESTILO + `\nAhora escribís la actividad por consigna de la lección. Las respuestas las corrige luego una IA, por eso cada consigna lleva criterios claros con puntaje parcial.`;
  const user = `${aTextoFicha(c)}\n\nMATERIAL DE LA LECCIÓN (las consignas se apoyan SOLO en esto):\n${aTextoLeccion(contenido)}\n\nArmá exactamente 8 consignas, de lo más simple a lo más pensado, con esta distribución y estos puntos: 1 verdadero/falso (1 punto), 2 de opción múltiple con 4 opciones y una sola correcta (1 punto cada una), 3 de respuesta corta con respuesta verificable (2 puntos cada una), 2 abiertas (3 puntos cada una). Al menos dos consignas deben apuntar a los errores típicos. Las opciones incorrectas tienen que ser errores plausibles, nunca absurdas. En "respuesta" de multiple_choice y true_false va el texto exacto de una opción. En las abiertas, la respuesta de referencia es un ejemplo completo y los criterios dividen el puntaje en ideas.`;
  const r = await claudeTool(system, user, TOOL_CONSIGNAS, 8000);
  const cs = r.consignas;
  if (!Array.isArray(cs) || cs.length !== 8) throw new Error("La IA no devolvió exactamente 8 consignas");
  for (const q of cs) {
    if (q.tipo === "multiple_choice" && (!Array.isArray(q.opciones) || q.opciones.length !== 4 || !q.opciones.includes(q.respuesta))) throw new Error("Una consigna de opción múltiple quedó mal armada");
    if (q.tipo === "true_false") q.opciones = ["Verdadero", "Falso"];
  }
  return cs;
}

async function pasoRevision(c: Ctx, contenido: any, consignas: any[]) {
  const system = `Sos un revisor de matemática de secundaria, exigente y desconfiado. Tu trabajo es encontrar errores, no elogiar. Recalculá TODAS las cuentas, una por una, y verificá cada respuesta de referencia. Controlá además: que cada consigna tenga una única respuesta correcta, que la respuesta de referencia y los criterios coincidan con el material, que el material no incluya nada de "NO ENTRA", que no adelante lecciones posteriores, y que la notación sea la argentina (punto en los miles, coma en los decimales). Si todo está bien, devolvé la lista de problemas vacía y apto=true. "apto" solo es true si no hay problemas de gravedad alta ni media.`;
  const user = `${aTextoFicha(c)}\n\nMATERIAL:\n${aTextoLeccion(contenido)}\n\nCONSIGNAS:\n` +
    consignas.map((q, i) => `${i + 1}. [${q.tipo}, ${q.puntos} pts] ${q.enunciado}${q.opciones?.length ? "\n   Opciones: " + q.opciones.join(" / ") : ""}\n   Respuesta: ${q.respuesta}\n   Criterios: ${q.criterios}\n   Explicación: ${q.explicacion}`).join("\n");
  return await claudeTool(system, user, TOOL_REVISION, 5000);
}

async function correrPaso(draftId: string) {
  const { data: tomado } = await admin.from("lesson_drafts").update({ status: "generando", updated_at: new Date().toISOString() })
    .eq("id", draftId).eq("status", "en_cola").select("*").maybeSingle();
  if (!tomado) return; // ya lo está procesando otra llamada
  try {
    const c = await contexto(tomado.lesson_id);
    let patch: Record<string, unknown>;
    if (tomado.paso === "contenido") {
      const contenido = await pasoContenido(c);
      patch = { contenido, paso: "consignas", status: "en_cola" };
    } else if (tomado.paso === "consignas") {
      const consignas = await pasoConsignas(c, tomado.contenido);
      patch = { consignas, paso: "revision", status: "en_cola" };
    } else {
      const revision = await pasoRevision(c, tomado.contenido, tomado.consignas);
      patch = { revision, paso: "listo", status: "borrador" };
    }
    await admin.from("lesson_drafts").update({ ...patch, modelo: MODEL, error: null, updated_at: new Date().toISOString() }).eq("id", draftId);
    if (patch.paso !== "listo") await llamarSeMismo({ action: "procesar", draft_id: draftId });
  } catch (e) {
    await admin.from("lesson_drafts").update({
      status: "error", error: String((e as Error).message || e).slice(0, 600),
      intentos: (tomado.intentos || 0) + 1, updated_at: new Date().toISOString(),
    }).eq("id", draftId);
  }
}

async function llamarSeMismo(body: unknown) {
  const { data: cfg } = await admin.from("gen_config").select("valor").eq("clave", "token").single();
  await fetch(Deno.env.get("SUPABASE_URL")! + "/functions/v1/generar-leccion", {
    method: "POST",
    headers: { "content-type": "application/json", "x-gen-token": cfg!.valor, authorization: "Bearer " + Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")! },
    body: JSON.stringify(body),
  });
}

function enSegundoPlano(p: Promise<unknown>) {
  if (typeof EdgeRuntime !== "undefined") EdgeRuntime.waitUntil(p); else p.catch(() => {});
}

// ---------------- entrada ----------------
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const { data: cfg } = await admin.from("gen_config").select("valor").eq("clave", "token").single();
    if (!cfg || req.headers.get("x-gen-token") !== cfg.valor) return json({ error: "No autorizado" }, 401);
    const b = await req.json().catch(() => ({}));

    if (b.action === "encolar") {
      const { data: lecs } = await admin.from("lessons").select("id, position").eq("topic_id", b.tema_id).order("position");
      const ids = (lecs || []).map((l: any) => l.id);
      const { data: fichas } = await admin.from("lesson_fichas").select("lesson_id").in("lesson_id", ids);
      const conFicha = new Set((fichas || []).map((f: any) => f.lesson_id));
      const { data: previos } = await admin.from("lesson_drafts").select("lesson_id").in("lesson_id", ids);
      const yaHay = new Set((previos || []).map((p: any) => p.lesson_id));
      const nuevos = ids.filter((id: string) => conFicha.has(id) && !yaHay.has(id));
      if (nuevos.length) await admin.from("lesson_drafts").insert(nuevos.map((lesson_id: string) => ({ lesson_id })));
      const { data: cola } = await admin.from("lesson_drafts").select("id").in("lesson_id", ids).eq("status", "en_cola").eq("paso", "contenido");
      for (const d of cola || []) enSegundoPlano(llamarSeMismo({ action: "procesar", draft_id: d.id }));
      return json({ ok: true, encoladas: (cola || []).length, sin_ficha: ids.length - conFicha.size });
    }
    if (b.action === "procesar") {
      enSegundoPlano(correrPaso(b.draft_id));
      return json({ ok: true });
    }
    if (b.action === "reintentar") {
      await admin.from("lesson_drafts").update({ status: "en_cola", error: null }).eq("id", b.draft_id).eq("status", "error");
      enSegundoPlano(llamarSeMismo({ action: "procesar", draft_id: b.draft_id }));
      return json({ ok: true });
    }
    if (b.action === "estado") {
      const { data: lecs } = await admin.from("lessons").select("id, title, position").eq("topic_id", b.tema_id).order("position");
      const { data: ds } = await admin.from("lesson_drafts").select("id, lesson_id, status, paso, error").in("lesson_id", (lecs || []).map((l: any) => l.id));
      return json({ lecciones: (lecs || []).map((l: any) => ({ titulo: l.title, ...(ds || []).find((d: any) => d.lesson_id === l.id) })) });
    }
    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    return json({ error: String((e as Error).message || e) }, 500);
  }
});
