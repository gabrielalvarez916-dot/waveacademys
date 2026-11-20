import { createClient } from "npm:@supabase/supabase-js@2";
import { AwsClient } from "npm:aws4fetch@1";
import { decodeBase64, encodeBase64 } from "jsr:@std/encoding@1/base64";

// FÁBRICA DE LECCIONES · PDF
// El proceso de GitHub (tools/pdf/generar.py) arma el PDF de cada borrador listo y lo sube por acá.
// Nunca publica: carga el PDF en el paso "PDF" de la lección SOLO si la lección no está publicada y ese paso está vacío.
// Al subir el PDF también deja cargada la carpeta del nivel (consignas + clave de corrección) desde el mismo borrador.
// Acciones (POST, header x-gen-token):
//   { action: "pendientes" }                       -> borradores listos sin PDF, con todo lo necesario para armarlo
//   { action: "pendientes_neutro", limite?, excluir? } / { action: "subir_neutro", draft_id, pdf_base64, carpeta? } -> segundo PDF en español neutro
//   { action: "subir", draft_id, pdf_base64 }      -> guarda el PDF en R2 y lo carga en la lección (si el PDF actual lo armó la máquina, lo reemplaza: así entran las imágenes cargadas desde el admin)
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type, x-gen-token",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

// texto plano del material (sirve para el Tutor y el repaso, igual que el texto extraído de un PDF)
function aTexto(c: any): string {
  const out: string[] = [String(c.objetivo ?? "")];
  (c.secciones || []).forEach((s: any, i: number) => {
    out.push(`\n${i + 1}. ${s.titulo}`);
    (s.bloques || []).forEach((b: any) => {
      let t = b.tipo === "imagen"
        ? `Imagen${b.titulo ? " (" + b.titulo + ")" : ""}: ${b.imagen_descripcion || ""}${b.texto ? " " + b.texto : ""}`
        : (b.titulo ? b.titulo + ". " : "") + (b.texto || "");
      if (b.items?.length) t += "\n" + b.items.map((x: string, k: number) => `${k + 1}. ${x}`).join("\n");
      if (b.columnas?.length) t += "\n" + b.columnas.join(" | ") + "\n" + (b.filas || []).map((f: string[]) => f.join(" | ")).join("\n");
      out.push(t.replace(/<\/?b>/g, ""));
    });
  });
  if (c.resumen?.length) out.push("\nResumen\n" + c.resumen.map((r: any) => `${r.titulo}: ${r.texto}`).join("\n"));
  if (c.glosario?.length) out.push("\nGlosario\n" + c.glosario.map((g: any) => `${g.palabra}: ${g.significado}`).join("\n"));
  return out.join("\n");
}

async function numeroDeLeccion(lessonId: string) {
  const { data: l } = await admin.from("lessons").select("id, title, position, topic_id, is_published").eq("id", lessonId).single();
  const { data: t } = await admin.from("topics").select("id, title, position, subject_id").eq("id", l!.topic_id).single();
  const { data: su } = await admin.from("subjects").select("name, grade_id").eq("id", t!.subject_id).single();
  const { data: g } = await admin.from("grades").select("year_number").eq("id", su!.grade_id).single();
  const { data: temas } = await admin.from("topics").select("id, position").eq("subject_id", t!.subject_id).order("position");
  const { data: lecs } = await admin.from("lessons").select("topic_id").in("topic_id", (temas || []).map((x: any) => x.id));
  const previas = (temas || []).filter((x: any) => x.position < t!.position)
    .reduce((n: number, x: any) => n + (lecs || []).filter((y: any) => y.topic_id === x.id).length, 0);
  return {
    materia: su!.name, anio: g!.year_number, tema_num: t!.position, tema: t!.title,
    leccion_num: previas + l!.position, titulo: l!.title, publicada: l!.is_published,
  };
}

// imágenes cargadas desde el admin para los bloques de imagen del borrador (solo si siguen siendo las del bloque actual)
async function imagenesDe(draftId: string, contenido: any) {
  const { data: ims } = await admin.from("lesson_draft_images").select("sec, bloque, descripcion, path").eq("draft_id", draftId);
  const out: any[] = [];
  for (const im of ims || []) {
    const blk = contenido?.secciones?.[im.sec]?.bloques?.[im.bloque];
    if (!blk || blk.tipo !== "imagen" || (blk.imagen_descripcion || "") !== im.descripcion) continue;
    const { data: f, error } = await admin.storage.from("lesson-images").download(im.path);
    if (error || !f) continue;
    const bytes = new Uint8Array(await f.arrayBuffer());
    out.push({ sec: im.sec, bloque: im.bloque, mime: f.type || "image/png", b64: encodeBase64(bytes) });
  }
  return out;
}

// Carpeta del nivel: consignas (las ve el alumno) + clave de corrección (solo la lee la función entregar_carpeta)
async function cargarCarpeta(pasoId: string, c: any): Promise<string> {
  try {
    const cons: string[] = (c?.carpeta || []).map((x: any) => String(typeof x === "string" ? x : x?.consigna ?? "").trim());
    if (!cons.length) return "sin carpeta en el borrador";
    const resp: any[] = c?.respuestas_carpeta || [];
    const sols: any[] = c?.soluciones?.carpeta || [];
    const items = cons.map((_, i) => ({
      acepta: ([] as any[]).concat(resp[i] ?? []).map((s) => String(s).trim()).filter(Boolean),
      solucion: String(sols[i] ?? "").trim(),
    }));
    if (cons.some((x) => !x) || items.some((it) => !it.acepta.length)) return "omitida: falta alguna consigna o respuesta válida (respuestas_carpeta)";
    const { data: ps } = await admin.from("lesson_steps").select("content").eq("id", pasoId).single();
    const up = await admin.from("lesson_steps").update({ content: { ...((ps?.content as any) || {}), carpeta: cons } }).eq("id", pasoId);
    if (up.error) return "error: " + up.error.message;
    const ck = await admin.from("carpeta_claves").upsert({ lesson_step_id: pasoId, items, updated_at: new Date().toISOString() });
    if (ck.error) return "error: " + ck.error.message;
    return `${cons.length} consignas con su clave`;
  } catch (e) {
    return "error: " + String((e as Error).message || e);
  }
}

const r2url = (key: string) => `https://${Deno.env.get("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com/${Deno.env.get("R2_BUCKET")}/${key.split("/").map(encodeURIComponent).join("/")}`;
const r2 = () => new AwsClient({ accessKeyId: Deno.env.get("R2_ACCESS_KEY_ID")!, secretAccessKey: Deno.env.get("R2_SECRET_ACCESS_KEY")!, service: "s3", region: "auto" });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const { data: cfg } = await admin.from("gen_config").select("valor").eq("clave", "token").single();
    if (!cfg || req.headers.get("x-gen-token") !== cfg.valor) return json({ error: "No autorizado" }, 401);
    const b = await req.json().catch(() => ({}));

    if (b.action === "pendientes") {
      const { data: ds } = await admin.from("lesson_drafts").select("id, lesson_id, contenido, pdf_draft_key")
        .eq("status", "borrador").eq("paso", "listo").is("pdf_at", null).order("created_at");
      const out: any[] = [];
      for (const d of ds || []) {
        const meta = await numeroDeLeccion(d.lesson_id);
        if (meta.publicada) continue; // una lección ya publicada no se toca
        const { data: paso } = await admin.from("lesson_steps").select("r2_key").eq("lesson_id", d.lesson_id).eq("step_type", "pdf").maybeSingle();
        if (paso?.r2_key && paso.r2_key !== d.pdf_draft_key) continue; // tiene un PDF que no armó la máquina: no se pisa
        delete (meta as any).publicada;
        out.push({ draft_id: d.id, meta, contenido: d.contenido, imagenes: await imagenesDe(d.id, d.contenido) });
      }
      return json({ pendientes: out });
    }

    if (b.action === "subir") {
      const { data: d } = await admin.from("lesson_drafts").select("id, lesson_id, status, paso, contenido, pdf_at, pdf_draft_key").eq("id", b.draft_id).maybeSingle();
      if (!d) return json({ ok: false, motivo: "No existe el borrador" }, 404);
      if (d.status !== "borrador" || d.paso !== "listo") return json({ ok: false, motivo: "El borrador no está listo" }, 409);
      if (d.pdf_at) return json({ ok: false, motivo: "Ya tiene PDF cargado" }, 409);
      const meta = await numeroDeLeccion(d.lesson_id);
      if (meta.publicada) return json({ ok: false, motivo: "La lección está publicada: no se toca" }, 409);
      const { data: paso } = await admin.from("lesson_steps").select("id, r2_key").eq("lesson_id", d.lesson_id).eq("step_type", "pdf").maybeSingle();
      if (!paso) return json({ ok: false, motivo: "La lección no tiene el paso PDF (abrila una vez en Contenidos)" }, 409);
      if (paso.r2_key && paso.r2_key !== d.pdf_draft_key) return json({ ok: false, motivo: "El paso PDF ya tiene un archivo que no armó la máquina: no se pisa" }, 409);

      const bytes = decodeBase64(String(b.pdf_base64 || ""));
      if (bytes.length < 5000 || bytes.length > 20 * 1024 * 1024) return json({ ok: false, motivo: "El PDF no tiene un tamaño razonable" }, 400);
      if (new TextDecoder().decode(bytes.slice(0, 5)) !== "%PDF-") return json({ ok: false, motivo: "El archivo no es un PDF" }, 400);

      const faltan = ["R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET"].filter((k) => !Deno.env.get(k));
      if (faltan.length) return json({ ok: false, motivo: "Faltan secretos de R2: " + faltan.join(", ") }, 500);
      const aws = new AwsClient({ accessKeyId: Deno.env.get("R2_ACCESS_KEY_ID")!, secretAccessKey: Deno.env.get("R2_SECRET_ACCESS_KEY")!, service: "s3", region: "auto" });
      const limpio = (t: string) => t.normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "");
      const nombre = `${limpio(meta.materia)}_Leccion-${meta.leccion_num}_${limpio(meta.titulo)}.pdf`;
      const key = `lessons/${d.lesson_id}/${crypto.randomUUID().slice(0, 8)}-${nombre}`;
      const url = `https://${Deno.env.get("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com/${Deno.env.get("R2_BUCKET")}/${key.split("/").map(encodeURIComponent).join("/")}`;
      const put = await aws.fetch(url, { method: "PUT", body: bytes, headers: { "content-type": "application/pdf" } });
      if (!put.ok) return json({ ok: false, motivo: `R2 rechazó la subida (${put.status})` }, 502);

      // se carga en el paso PDF sin pisar nada (condición: sigue vacío)
      let q = admin.from("lesson_steps").update({ r2_key: key, extracted_text: aTexto(d.contenido) }).eq("id", paso.id);
      q = paso.r2_key ? q.eq("r2_key", paso.r2_key) : q.is("r2_key", null);
      const up = await q.select("id");
      if (up.error || !up.data?.length) return json({ ok: false, motivo: "No se pudo cargar el PDF en la lección" }, 500);
      await admin.from("lesson_drafts").update({ pdf_draft_key: key, pdf_at: new Date().toISOString() }).eq("id", d.id);
      const carpeta = await cargarCarpeta(paso.id, d.contenido);
      { // el PDF neutro viejo ya no corresponde: se borra para que se arme de nuevo
        const { data: ps } = await admin.from("lesson_steps").select("content").eq("id", paso.id).single();
        const viejoN = (ps?.content as any)?.r2_key_neutro;
        if (viejoN) {
          const c = { ...((ps?.content as any) || {}) }; delete c.r2_key_neutro;
          await admin.from("lesson_steps").update({ content: c }).eq("id", paso.id);
          await aws.fetch(r2url(viejoN), { method: "DELETE" }).catch(() => {});
        }
      }
      if (paso.r2_key) { // se reemplazó un PDF armado por la máquina: se borra el anterior
        const viejo = `https://${Deno.env.get("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com/${Deno.env.get("R2_BUCKET")}/${paso.r2_key.split("/").map(encodeURIComponent).join("/")}`;
        await aws.fetch(viejo, { method: "DELETE" }).catch(() => {});
      }
      return json({ ok: true, key, bytes: bytes.length, carpeta });
    }

    // Versión neutra (alumnos de otros países): un segundo PDF por lección, armado por la máquina con el texto en español neutro.
    // No toca el PDF principal ni el estado de publicación; vale también para lecciones publicadas.
    if (b.action === "pendientes_neutro") {
      const { data: ds } = await admin.from("lesson_drafts").select("id, lesson_id, contenido, pdf_draft_key").not("pdf_at", "is", null).order("created_at");
      const out: any[] = [];
      for (const d of ds || []) {
        if (out.length >= (Number(b.limite) || 25)) break;
        if ((b.excluir || []).includes(d.id)) continue;
        const { data: paso } = await admin.from("lesson_steps").select("r2_key, content").eq("lesson_id", d.lesson_id).eq("step_type", "pdf").maybeSingle();
        if (!paso?.r2_key || paso.r2_key !== d.pdf_draft_key || (paso.content as any)?.r2_key_neutro) continue;
        const meta = await numeroDeLeccion(d.lesson_id); delete (meta as any).publicada;
        out.push({ draft_id: d.id, meta, contenido: d.contenido, imagenes: await imagenesDe(d.id, d.contenido) });
      }
      return json({ pendientes: out });
    }

    if (b.action === "subir_neutro") {
      const { data: d } = await admin.from("lesson_drafts").select("id, lesson_id, pdf_draft_key").eq("id", b.draft_id).maybeSingle();
      if (!d) return json({ ok: false, motivo: "No existe el borrador" }, 404);
      const { data: paso } = await admin.from("lesson_steps").select("id, r2_key, content").eq("lesson_id", d.lesson_id).eq("step_type", "pdf").maybeSingle();
      if (!paso?.r2_key || paso.r2_key !== d.pdf_draft_key) return json({ ok: false, motivo: "El PDF principal no lo armó la máquina" }, 409);
      const bytes = decodeBase64(String(b.pdf_base64 || ""));
      if (bytes.length < 5000 || new TextDecoder().decode(bytes.slice(0, 5)) !== "%PDF-") return json({ ok: false, motivo: "PDF inválido" }, 400);
      const aws = r2();
      const key = paso.r2_key.replace(/\.pdf$/, "") + "_neutro.pdf";
      const put = await aws.fetch(r2url(key), { method: "PUT", body: bytes, headers: { "content-type": "application/pdf" } });
      if (!put.ok) return json({ ok: false, motivo: `R2 rechazó la subida (${put.status})` }, 502);
      const c: any = { ...((paso.content as any) || {}), r2_key_neutro: key };
      if (Array.isArray(b.carpeta) && b.carpeta.length) c.carpeta_neutro = b.carpeta.map((x: any) => String(x));
      const up = await admin.from("lesson_steps").update({ content: c }).eq("id", paso.id).eq("r2_key", paso.r2_key).select("id");
      if (up.error || !up.data?.length) return json({ ok: false, motivo: "No se pudo guardar" }, 500);
      return json({ ok: true, key, bytes: bytes.length });
    }
    return json({ error: "Acción desconocida" }, 400);
  } catch (e) {
    console.error(e);
    return json({ error: String((e as Error).message || e) }, 500);
  }
});
