import { createClient } from "npm:@supabase/supabase-js@2";
import { AwsClient } from "npm:aws4fetch@1";
import { decodeBase64 } from "jsr:@std/encoding@1/base64";

// MÁQUINA DEL NIVEL MEDIO · PDF (separada de fabrica-pdf, que es del Avanzado y no se toca).
// El proceso de GitHub (tools/medio/pdf/generar.py) arma los PDF desde el repo y los sube por acá.
// Solo acepta lecciones de materias del Nivel Medio, no publicadas. No usa lesson_drafts.
// Acciones (POST, header x-medio-token):
//   { action: "lecciones", subject_id, tema, internacional? }         -> las lecciones 1 a 5 de esa misión (la 5 es la Práctica general: lleva un PDF de repaso) (o de su par internacional), con lo necesario para armar el PDF
//   { action: "subir", lesson_id, pdf_base64, contenido, neutro? }   -> guarda el PDF en R2 y lo carga en el paso PDF (y la carpeta con su clave)
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type, x-medio-token" };
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });
const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const r2url = (key: string) => `https://${Deno.env.get("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com/${Deno.env.get("R2_BUCKET")}/${key.split("/").map(encodeURIComponent).join("/")}`;
const r2 = () => new AwsClient({ accessKeyId: Deno.env.get("R2_ACCESS_KEY_ID")!, secretAccessKey: Deno.env.get("R2_SECRET_ACCESS_KEY")!, service: "s3", region: "auto" });

// datos de la lección + control de que sea del Nivel Medio
async function datos(lessonId: string) {
  const { data: l } = await admin.from("lessons").select("id, title, position, topic_id, is_published").eq("id", lessonId).maybeSingle();
  if (!l) return null;
  const { data: t } = await admin.from("topics").select("id, title, position, subject_id").eq("id", l.topic_id).single();
  const { data: su } = await admin.from("subjects").select("name, grade_id").eq("id", t!.subject_id).single();
  const { data: g } = await admin.from("grades").select("year_number, level_id").eq("id", su!.grade_id).single();
  const { data: lv } = await admin.from("levels").select("name").eq("id", g!.level_id).single();
  const { data: temas } = await admin.from("topics").select("id, position").eq("subject_id", t!.subject_id).order("position");
  const { data: lecs } = await admin.from("lessons").select("topic_id").in("topic_id", (temas || []).map((x: any) => x.id));
  const previas = (temas || []).filter((x: any) => x.position < t!.position).reduce((n: number, x: any) => n + (lecs || []).filter((y: any) => y.topic_id === x.id).length, 0);
  return { medio: lv?.name === "Nivel Medio", publicada: l.is_published,
    meta: { lesson_id: l.id, materia: su!.name, anio: g!.year_number, tema_num: t!.position, tema: t!.title, leccion_num: previas + l.position, nivel: l.position, titulo: l.title } };
}

function aTexto(c: any): string { // texto plano del material (para el Tutor y el repaso)
  const out: string[] = [String(c.objetivo ?? "")];
  (c.secciones || []).forEach((s: any, i: number) => {
    out.push(`\n${i + 1}. ${s.titulo}`);
    (s.bloques || []).forEach((b: any) => {
      let t = b.tipo === "imagen" ? `Imagen${b.titulo ? " (" + b.titulo + ")" : ""}${b.texto ? ": " + b.texto : ""}` : (b.titulo ? b.titulo + ". " : "") + (b.texto || "");
      if (b.items?.length) t += "\n" + b.items.map((x: string, k: number) => `${k + 1}. ${x}`).join("\n");
      out.push(t.replace(/<\/?b>/g, ""));
    });
  });
  if (c.resumen?.length) out.push("\nResumen\n" + c.resumen.map((r: any) => `${r.titulo}: ${r.texto}`).join("\n"));
  if (c.glosario?.length) out.push("\nGlosario\n" + c.glosario.map((g: any) => `${g.palabra}: ${g.significado}`).join("\n"));
  return out.join("\n");
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const { data: cfg } = await admin.from("gen_config").select("valor").eq("clave", "medio_token").single();
    if (!cfg || req.headers.get("x-medio-token") !== cfg.valor) return json({ error: "No autorizado" }, 401);
    const b = await req.json().catch(() => ({}));

    if (b.action === "lecciones") {
      // internacional: la misión par de una ALTERNATIVA (su version_par, que puede estar en otra materia del Medio; o la internacional de la misma materia)
      const { data: t0 } = await admin.from("topics").select("id, version_par").eq("subject_id", b.subject_id).eq("position", b.tema)
        .or("solo_para.is.null,solo_para.neq.internacional").limit(1).maybeSingle();
      let t: any = t0;
      if (b.internacional) {
        t = t0?.version_par ? { id: t0.version_par }
          : (await admin.from("topics").select("id").eq("subject_id", b.subject_id).eq("position", b.tema).eq("solo_para", "internacional").limit(1).maybeSingle()).data;
      }
      if (!t) return json({ error: "No existe esa misión" }, 404);
      const { data: ls } = await admin.from("lessons").select("id").eq("topic_id", t.id).lte("position", 5).order("position");
      const out: any[] = [];
      for (const l of ls || []) {
        const d = await datos(l.id);
        if (!d?.medio) return json({ error: "Esa materia no es del Nivel Medio: no se toca" }, 403);
        const { data: paso } = await admin.from("lesson_steps").select("r2_key, content").eq("lesson_id", l.id).eq("step_type", "pdf").maybeSingle();
        out.push({ ...d.meta, publicada: d.publicada, tiene_pdf: !!paso?.r2_key, pdf_medio: !!(paso?.content as any)?.pdf_medio });
      }
      return json({ lecciones: out });
    }

    if (b.action === "subir") {
      const d = await datos(b.lesson_id);
      if (!d) return json({ ok: false, motivo: "No existe la lección" }, 404);
      if (!d.medio) return json({ ok: false, motivo: "La lección no es del Nivel Medio: no se toca" }, 403);
      if (d.publicada) return json({ ok: false, motivo: "La lección está publicada: no se toca" }, 409);
      const { data: paso } = await admin.from("lesson_steps").select("id, r2_key, content").eq("lesson_id", b.lesson_id).eq("step_type", "pdf").maybeSingle();
      if (!paso) return json({ ok: false, motivo: "La lección no tiene el paso PDF" }, 409);
      const c0: any = (paso.content as any) || {};
      const bytes = decodeBase64(String(b.pdf_base64 || ""));
      if (bytes.length < 5000 || bytes.length > 20 * 1024 * 1024 || new TextDecoder().decode(bytes.slice(0, 5)) !== "%PDF-") return json({ ok: false, motivo: "PDF inválido" }, 400);
      const faltan = ["R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET"].filter((k) => !Deno.env.get(k));
      if (faltan.length) return json({ ok: false, motivo: "Faltan secretos de R2: " + faltan.join(", ") }, 500);
      const aws = r2(); const con = b.contenido || {};
      const cons: string[] = (con.carpeta || []).map((x: any) => String(typeof x === "string" ? x : x?.consigna ?? "").trim());

      if (b.neutro) { // segundo PDF (alumnos de otros países): solo si el principal lo cargó esta máquina
        if (!paso.r2_key || !c0.pdf_medio) return json({ ok: false, motivo: "Primero tiene que estar el PDF principal del Medio" }, 409);
        const key = paso.r2_key.replace(/\.pdf$/, "") + "_neutro.pdf";
        const put = await aws.fetch(r2url(key), { method: "PUT", body: bytes, headers: { "content-type": "application/pdf" } });
        if (!put.ok) return json({ ok: false, motivo: `R2 rechazó la subida (${put.status})` }, 502);
        const up = await admin.from("lesson_steps").update({ content: { ...c0, r2_key_neutro: key, ...(cons.length ? { carpeta_neutro: cons } : {}) } }).eq("id", paso.id).select("id");
        if (up.error || !up.data?.length) return json({ ok: false, motivo: "No se pudo guardar" }, 500);
        return json({ ok: true, key, bytes: bytes.length });
      }

      if (paso.r2_key && !c0.pdf_medio) return json({ ok: false, motivo: "El paso PDF ya tiene un archivo que no armó esta máquina: no se pisa" }, 409);
      const limpio = (t: string) => t.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "");
      const key = `lessons/${b.lesson_id}/${crypto.randomUUID().slice(0, 8)}-${limpio(d.meta.materia)}_Leccion-${d.meta.leccion_num}_${limpio(d.meta.titulo)}.pdf`;
      const put = await aws.fetch(r2url(key), { method: "PUT", body: bytes, headers: { "content-type": "application/pdf" } });
      if (!put.ok) return json({ ok: false, motivo: `R2 rechazó la subida (${put.status})` }, 502);
      const c: any = { ...c0, pdf_medio: true, ...(cons.length ? { carpeta: cons } : {}) }; delete c.r2_key_neutro; delete c.carpeta_neutro;
      const up = await admin.from("lesson_steps").update({ r2_key: key, extracted_text: aTexto(con), content: c }).eq("id", paso.id).select("id");
      if (up.error || !up.data?.length) return json({ ok: false, motivo: "No se pudo cargar el PDF en la lección" }, 500);
      // clave de corrección de la carpeta (el alumno no la ve)
      const resp: any[] = con.respuestas_carpeta || [], sols: any[] = con.soluciones?.carpeta || [];
      const items = cons.map((_, i) => ({ acepta: ([] as any[]).concat(resp[i] ?? []).map((s) => String(s).trim()).filter(Boolean), solucion: String(sols[i] ?? "").trim() }));
      let carpeta = "sin carpeta";
      if (cons.length && !items.some((it) => !it.acepta.length)) {
        const ck = await admin.from("carpeta_claves").upsert({ lesson_step_id: paso.id, items, updated_at: new Date().toISOString() });
        carpeta = ck.error ? "error: " + ck.error.message : `${cons.length} consignas con su clave`;
      }
      if (paso.r2_key) { // se reemplazó un PDF que había armado esta misma máquina: se borran el anterior y su neutro
        await aws.fetch(r2url(paso.r2_key), { method: "DELETE" }).catch(() => {});
        if (c0.r2_key_neutro) await aws.fetch(r2url(c0.r2_key_neutro), { method: "DELETE" }).catch(() => {});
      }
      return json({ ok: true, key, bytes: bytes.length, carpeta });
    }
    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    return json({ error: String((e as Error).message || e) }, 500);
  }
});
