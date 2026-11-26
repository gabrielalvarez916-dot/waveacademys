// CONTROL DE CALIDAD de la lección interactiva (lo corre la máquina de misiones antes de cargar; si algo falla, no se carga nada).
// La "practica" escrita a mano es opcional; si una sección la trae, se prueba en 60 sorteos (ver docs/leccion-interactiva.md).
// Uso: node tools/interactiva/validar.js contenido/<materia>/mision-N/mision-N.json [...]
'use strict';
const fs = require('fs'), path = require('path');
require(path.join(__dirname, '..', '..', 'js', 'wave-calc.js'));
const W = globalThis.WaveCalc;
let errores = 0;
const mal = (donde, m) => { errores++; console.log('  ✘', donde, '·', m); };
const quedan = s => /\{[A-Za-z_][A-Za-z_0-9]*\}/.test(String(s));

function caso(src, vars, donde) {
  const P = s => vars ? W.plantilla(String(s), vars) : String(s == null ? '' : s);
  if (!src.enunciado || String(src.enunciado).trim().length < 8) return mal(donde, 'falta el enunciado');
  if (!Array.isArray(src.pasos) || src.pasos.length < 2 || src.pasos.length > 8) return mal(donde, 'los pasos tienen que ser entre 2 y 8');
  const r = src.respuesta || {};
  const textos = [src.enunciado].concat(src.pasos, r.acepta || [], r.opciones || [], r.correcta != null ? [r.correcta] : []).map(P);
  if (textos.some(quedan)) return mal(donde, 'queda una {variable} sin reemplazar: ' + textos.filter(quedan)[0].slice(0, 80));
  if (r.formula == null && !(r.acepta || []).length && !(r.opciones || []).length) return mal(donde, 'la respuesta tiene que tener formula, acepta u opciones');
  if (r.formula != null) {
    let v; try { v = W.evaluar(String(r.formula), vars || {}); } catch (e) { return mal(donde, 'la fórmula no se puede calcular: ' + e.message); }
    if (!isFinite(v)) return mal(donde, 'la fórmula da un resultado inválido');
    const ult = P(src.pasos[src.pasos.length - 1]), f = W.fmtNum(v);
    if (ult.indexOf(f) < 0 && !(r.acepta || []).some(a => ult.indexOf(P(a)) >= 0)) return mal(donde, 'el último paso no llega al resultado (' + f + '): «' + ult.slice(0, 90) + '»');
  }
  if ((r.opciones || []).length) {
    const ops = r.opciones.map(P);
    if (ops.length < 2 || new Set(ops).size !== ops.length) return mal(donde, 'las opciones tienen que ser 2 o más y distintas');
    if (ops.indexOf(P(r.correcta)) < 0) return mal(donde, 'la correcta no está entre las opciones');
  }
  return true;
}

function practica(pr, donde) {
  if (!pr || typeof pr !== 'object') return mal(donde, 'falta "practica"');
  // la práctica es solo para temas prácticos: tiene que ser una cuenta (respuesta con fórmula), no una pregunta de concepto
  const casos = Array.isArray(pr.variantes) ? pr.variantes : [pr];
  if (casos.some(v => !(v.respuesta && v.respuesta.formula != null))) return mal(donde, 'la práctica tiene que ser una cuenta u operación (respuesta con "formula"); los temas de concepto van solo con la explicación');
  if (Array.isArray(pr.variantes)) {
    if (pr.variantes.length < 3) return mal(donde, 'con variantes hacen falta 3 o más ejemplos');
    return pr.variantes.forEach((v, i) => caso(v, null, donde + ' · variante ' + (i + 1)));
  }
  if (!pr.vars) return mal(donde, 'sin "vars" (números al azar) hacen falta "variantes" (3 o más)');
  let ok = 0, vistos = new Set();
  for (let i = 0; i < 60; i++) {
    const vars = W.instanciar(pr, 's' + i); if (!vars) continue;
    if (caso(pr, vars, donde + ' · sorteo ' + i) !== true) return;
    ok++; vistos.add(W.plantilla(String(pr.enunciado), vars));
  }
  if (ok < 54) return mal(donde, 'las reglas descartan demasiados sorteos (' + ok + ' de 60 salen bien)');
  if (vistos.size < 5) return mal(donde, 'los números casi no cambian (' + vistos.size + ' ejercicios distintos)');
}

// ---------- LECCIÓN ESCRITA EN SESIÓN (docs/reglas-leccion-interactiva.md) ----------
const MIN_TEMA = 170, MIN_LECCION = 650, PROP_PROMEDIO = 0.9, MAX_COPIA = 0.25;
const limpio = s => String(s || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
const palabras = s => limpio(s).split(' ').filter(w => /[a-záéíóúñü0-9]/i.test(w));
const textoBloques = bs => (bs || []).map(b => [b.texto, (b.items || []).join(' '), (b.filas || []).map(f => f.join(' ')).join(' ')].join(' ')).join(' ');
function grams(txt) { const w = palabras(txt).map(x => x.toLowerCase()), g = new Set(); for (let i = 0; i + 6 <= w.length; i++) g.add(w.slice(i, i + 6).join(' ')); return g; }
function fuentes(ruta, M, n) {   // borrador del nivel + narración y textos de la clase animada de ese nivel
  let t = textoBloques([].concat(...((M.niveles[n] || {}).secciones || []).map(s => s.bloques || [])));
  const mat = (ruta.match(/contenido\/([a-z]+)-(\d)/) || []), pref = mat[1] ? mat[1].slice(0, 3) + mat[2] : '';
  const f = path.join(__dirname, '..', 'clase', 'lecciones', pref + '-m' + M.tema + '-n' + n + '.json');
  try { const C = JSON.parse(fs.readFileSync(f, 'utf8')); t += ' ' + JSON.stringify(C.escenas || []).replace(/[{}\[\]"]/g, ' '); } catch (_) {}
  return grams(t);
}
function promedioMateria(ruta) {  // palabras promedio de las lecciones ya escritas de la misma materia (otras misiones)
  const dir = path.dirname(path.dirname(ruta)), tot = [];
  for (const d of fs.readdirSync(dir)) {
    const f = path.join(dir, d, d + '.json'); if (!fs.existsSync(f) || path.resolve(f) === path.resolve(ruta)) continue;
    try { const M = JSON.parse(fs.readFileSync(f, 'utf8')); Object.values(M.niveles || {}).forEach(nv => { if (nv.leccion && nv.leccion.temas) tot.push(palabras(nv.leccion.temas.map(t => textoBloques(t.explicacion)).join(' ')).length); }); } catch (_) {}
  }
  return tot.length >= 3 ? tot.reduce((a, b) => a + b, 0) / tot.length : 0;
}
function leccion(ruta, M, n, L, donde) {
  if (!Array.isArray(L.temas) || !L.temas.length) return mal(donde, 'la lección no tiene temas');
  let total = 0; const prom = promedioMateria(ruta), fu = fuentes(ruta, M, n);
  L.temas.forEach((t, i) => {
    const d = donde + ' · tema ' + (i + 1) + ' «' + (t.titulo || '') + '»', bs = t.explicacion || [], tipos = bs.map(b => b.tipo), txt = textoBloques(bs), np = palabras(txt).length;
    total += np;
    if (np < MIN_TEMA) mal(d, 'explicación de ' + np + ' palabras: el mínimo es ' + MIN_TEMA);
    if (!tipos.includes('definicion')) mal(d, 'falta la definición (bloque definicion)');
    if (!tipos.includes('parrafo')) mal(d, 'falta el párrafo que explica por qué es así / para qué sirve');
    const ej = bs.find(b => b.tipo === 'ejemplo'); if (!ej || (ej.items || []).length < 3) mal(d, 'falta un ejemplo resuelto propio con 3 o más pasos');
    if (!tipos.includes('error')) mal(d, 'falta el error típico (bloque error)');
    const pa = bs.find(b => b.tipo === 'pasos'); if (pa && (pa.items || []).length < 3) mal(d, 'el procedimiento tiene menos de 3 pasos');
    if (/\b(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)\b/i.test(txt)) mal(d, 'menciona meses del calendario');
    if (/como (vimos|viste) en la clase/i.test(txt)) mal(d, 'remite a la clase en vez de explicar');
    const g = grams(txt); let rep = 0; g.forEach(x => { if (fu.has(x)) rep++; });
    if (g.size && rep / g.size > MAX_COPIA) mal(d, 'copia el borrador o la clase (' + Math.round(rep / g.size * 100) + ' % de frases repetidas; máximo ' + MAX_COPIA * 100 + ' %)');
    ['ejemplo', 'ejercicio'].forEach(k => { if (t[k] && !t[k].motor) mal(d, k + ' sin motor'); });
    if ((t.ejemplo || t.ejercicio) && !tipos.includes('pasos')) mal(d, 'lleva ejemplo o ejercicio pero no es un tema práctico (su explicación no tiene un procedimiento con pasos). Los temas de concepto van solo con la explicación');
  });
  if (total < MIN_LECCION) mal(donde, 'la lección tiene ' + total + ' palabras: el mínimo es ' + MIN_LECCION);
  if (prom && total < prom * PROP_PROMEDIO) mal(donde, 'la lección es más corta que las anteriores de la materia (' + total + ' palabras; el promedio es ' + Math.round(prom) + ', mínimo ' + Math.round(prom * PROP_PROMEDIO) + '). Se completa, no se acorta.');
}

for (const ruta of process.argv.slice(2)) {
  const M = JSON.parse(fs.readFileSync(ruta, 'utf8')), antes = errores;
  console.log(ruta);
  const revisar = (niveles, extra) => Object.keys(niveles || {}).forEach(n => {
    const secs = (niveles[n] || {}).secciones || [];
    if (!secs.length) mal(extra + 'nivel ' + n, 'no tiene secciones');
    secs.forEach((s, i) => {
      if (s.practica) practica(s.practica, extra + 'nivel ' + n + ' · tema ' + (i + 1) + ' «' + (s.titulo || '') + '»'); // opcional: la lección la arma la máquina con el banco
      if (s.practica && s.practica.neutro) practica(Object.assign({}, s.practica, s.practica.neutro, { neutro: undefined }), extra + 'nivel ' + n + ' · tema ' + (i + 1) + ' (neutro)');
    });
  });
  revisar(M.niveles, '');
  Object.keys(M.niveles || {}).forEach(n => { const L = M.niveles[n].leccion; if (L && Array.isArray(L.temas) && L.temas.some(t => t.explicacion)) leccion(ruta, M, n, L, 'lección nivel ' + n); });
  if (M.alternativa && M.alternativa.niveles) revisar(M.alternativa.niveles, 'alternativa · ');
  console.log(errores === antes ? '  ✔ lección interactiva OK' : '  ' + (errores - antes) + ' problema(s)');
}
process.exit(errores ? 1 : 0);
