// Convierte un nivel de lección (contenido/<materia>/<mision>/nivel-N.json) en el guion de una CLASE ANIMADA.
// No usa ninguna IA: arma las escenas y la narración directo del contenido que ya existe. Costo: $0.
// Uso: node tools/clase/convertir.mjs contenido/matematica-1/mision-1/nivel-1.json salida.json
import fs from 'node:fs';

const limpiar = (t) => String(t == null ? '' : t).replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
// Lo que se LEE en voz alta (los símbolos se dicen con palabras)
export const hablar = (t) => limpiar(t)
  .replace(/\s*×\s*/g, ' por ').replace(/\s*÷\s*/g, ' dividido ').replace(/\s*=\s*/g, ' es igual a ')
  .replace(/\s*\+\s*/g, ' más ').replace(/(\d)\s*[−-]\s*(\d)/g, '$1 menos $2').replace(/_{2,}/g, ' tanto ')
  .replace(/Ej\.:/g, 'Por ejemplo:').replace(/\s+/g, ' ').trim();
const frases = (t) => limpiar(t).split(/(?<=[.!?:;])\s+/).map((s) => s.trim()).filter(Boolean); // corta solo si hay espacio después (no rompe 2.026)

export function convertir(n, meta = {}) {
  const E = [];
  // cada escena: { t: tipo visual, ...datos, voz: [frases que se dicen] } — el ítem i del visual aparece con la frase i
  E.push({ t: 'portada', titulo: meta.titulo || 'Clase', sub: limpiar(n.objetivo), voz: [meta.titulo ? meta.titulo + '.' : '', hablar(n.objetivo)].filter(Boolean) });
  if (n.vas_a_ver?.length) E.push({ t: 'lista', titulo: 'Hoy vas a ver', items: n.vas_a_ver.map(limpiar), voz: ['Hoy vas a ver:', ...n.vas_a_ver.map((x) => hablar(x) + '.')] });

  for (const s of n.secciones || []) {
    E.push({ t: 'seccion', titulo: limpiar(s.titulo), voz: [hablar(s.titulo)] });
    for (const b of s.bloques || []) {
      if (b.tipo === 'definicion') E.push({ t: 'definicion', palabra: limpiar(b.titulo), texto: b.texto, voz: [hablar(b.titulo) + '.', ...frases(b.texto).map(hablar)] });
      else if (b.tipo === 'parrafo') E.push({ t: 'parrafo', texto: b.texto, voz: frases(b.texto).map(hablar) });
      else if (b.tipo === 'importante') E.push({ t: 'importante', titulo: limpiar(b.titulo), texto: b.texto, voz: ['Atención: ' + hablar(b.titulo) + '.', ...frases(b.texto).map(hablar)] });
      else if (b.tipo === 'tabla') E.push({ t: 'tabla', titulo: limpiar(b.titulo), columnas: (b.columnas || []).map(limpiar), filas: (b.filas || []).map((f) => f.map(limpiar)), nota: limpiar(b.texto), voz: [hablar(b.titulo) + '.', ...(b.filas || []).map((f) => hablar(f.join(', ')) + '.'), ...frases(b.texto).map(hablar)] });
      else if (b.tipo === 'ejemplo') E.push({ t: 'pasos', etq: 'Ejemplo', titulo: limpiar(b.titulo), items: (b.items || []).map(limpiar), voz: ['Veamos un ejemplo con ' + hablar(b.titulo) + '.', ...(b.items || []).map(hablar)] });
      // 'imagen' y tipos desconocidos se saltean (la figura queda en el PDF)
    }
  }
  const ec = n.ejemplo_completo;
  if (ec) {
    if (ec.columnas && ec.filas) E.push({ t: 'tabla', titulo: 'Ejemplo: ' + limpiar(ec.titulo), columnas: ec.columnas.map(limpiar), filas: ec.filas.map((f) => f.map(limpiar)), nota: limpiar(ec.planteo), voz: ['Hagamos un ejemplo completo.', hablar(ec.planteo), ...ec.filas.map((f) => hablar(f.join(', ')) + '.')] });
    E.push({ t: 'pasos', etq: 'Paso a paso', titulo: limpiar(ec.titulo), items: (ec.pasos || []).map(limpiar), voz: ['Vamos paso a paso.', ...(ec.pasos || []).map(hablar)] });
  }
  if (n.tip) E.push({ t: 'importante', icono: '💡', titulo: limpiar(n.tip.titulo), texto: n.tip.texto, voz: ['Un consejo: ' + hablar(n.tip.titulo) + '.', ...frases(n.tip.texto).map(hablar)] });
  if (n.ojo?.length) E.push({ t: 'ojo', titulo: 'Errores comunes', items: n.ojo.map(limpiar), voz: ['Ojo con estos errores comunes.', ...n.ojo.map(hablar)] });
  if (n.resumen?.length) E.push({ t: 'resumen', titulo: 'Resumen', items: n.resumen.map((r) => ({ titulo: limpiar(r.titulo), texto: limpiar(r.texto) })), voz: ['Repasemos lo más importante.', ...n.resumen.map((r) => hablar(r.titulo) + ': ' + hablar(r.texto))] });
  E.push({ t: 'cierre', titulo: '¡Clase terminada!', sub: 'Ahora pasá a practicar con las actividades.', voz: ['¡Muy bien! Terminaste la clase. Ahora pasá a practicar con las actividades.'] });
  E.forEach((e, i) => { e.id = 'e' + String(i + 1).padStart(2, '0'); });
  return { titulo: meta.titulo || 'Clase', escenas: E };
}

if (process.argv[1]?.endsWith('convertir.mjs') && process.argv[2]) {
  const n = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const spec = convertir(n, { titulo: process.argv[4] || n.titulo || 'Clase' });
  fs.writeFileSync(process.argv[3], JSON.stringify(spec, null, 1));
  const car = spec.escenas.reduce((a, e) => a + e.voz.join(' ').length, 0);
  console.log('listo', process.argv[3], spec.escenas.length, 'escenas,', car, 'caracteres de narración');
}
