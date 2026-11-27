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
const MAX_COPIA = 0.10;  // 26/11/2026: el texto de la lección es original, no se copia del PDF ni de la clase
const EXISTENTES = new Set((() => { try { return fs.readFileSync(path.join(__dirname, '..', 'calidad_existentes.txt'), 'utf8').split('\n').map(x => x.trim()).filter(x => x && !x.startsWith('#')); } catch (e) { return []; } })());
// Reglas por etapa (mismo modelo, adaptado a la edad). Primaria = contenido/medio/<materia>-<grado>/: 1.º a 3.º es el primer ciclo.
const ETAPAS = {
  secundaria: { nombre: 'secundaria', min: 60, max: 160, def: 15, parrafo: true, temas: 3, rec: [4, 8], recDef: 10 },
  ciclo2: { nombre: 'primaria, segundo ciclo (4.º a 6.º)', min: 40, max: 110, def: 10, parrafo: true, temas: 3, rec: [3, 6], recDef: 8 },
  ciclo1: { nombre: 'primaria, primer ciclo (1.º a 3.º)', min: 12, max: 60, def: 6, parrafo: false, temas: 2, rec: [2, 4], recDef: 5 }
};
function etapa(ruta) { const m = String(ruta).replace(/\\/g, '/').match(/contenido\/medio\/[a-z]+-(\d+)\//); if (!m) return ETAPAS.secundaria; return Number(m[1]) <= 3 ? ETAPAS.ciclo1 : ETAPAS.ciclo2; }
const EJEMPLO_CON_TEXTO = ['pasoapaso'];
// Ejemplos que ya muestran el procedimiento PASO A PASO (marcados con "pasos: true" en el banco). Solo esos van en una lección.
const PASO_A_PASO = new Set((() => { const o = []; ['leccion-banco.js', 'leccion-banco2.js', 'leccion-banco-nat.js', 'leccion-banco-nat2.js', 'leccion-banco-nat3.js'].forEach(f => { try { const t = fs.readFileSync(path.join(__dirname, '..', '..', 'js', f), 'utf8'); let m; const re = /M\.(\w+)\s*=\s*\{\s*tipo:\s*'ejemplo',\s*pasos:\s*true/g; while ((m = re.exec(t))) o.push(m[1]); } catch (e) {} }); return o; })());
// Ejercicios que mezclan contenidos: en la lección se elige SIEMPRE el modo, para que la práctica pida solo lo explicado en esa pantalla (o antes)
const MODO_OBLIGATORIO = { binario_conv: ['a_binario', 'a_decimal', 'ambos'], sexagesimal_conv: ['convertir', 'ambos'], llevar: null, ordenar: null, posicional: null, letras: null, descomponer_x: null, naturales_x: null, potencias_n_x: null, combinadas: null, calculadora_x: null, divis_x: null, criterios_x: null, factores_x: null, fracciones_x: null, primeros_x: null, decimales_x: null, enteros_x: null, razones_x: null, algebra_x: null, ecuaciones_x: null, geometria_x: null, figuras_x: null, medida_x: null, datos_x: null, racionales_x: null, porcentajes_x: null, ecuaciones2_x: null, funciones_x: null, geometria2_x: null };  // ejemplos que repiten la explicación en texto: no van en la lección
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
  let total = 0; const fu = fuentes(ruta, M, n), E = etapa(ruta), MIN_TEMA = E.min, MAX_TEMA = E.max;
  L.temas.forEach((t, i) => {
    const d = donde + ' · tema ' + (i + 1) + ' «' + (t.titulo || '') + '»', bs = t.explicacion || [], tipos = bs.map(b => b.tipo), txt = textoBloques(bs), np = palabras(txt).length;
    total += np;
    if (np < MIN_TEMA) mal(d, 'explicación de ' + np + ' palabras: el mínimo es ' + MIN_TEMA);
    if (np > MAX_TEMA) mal(d, 'explicación de ' + np + ' palabras: el máximo es ' + MAX_TEMA + ' (modelo CIDEAD: texto corto, el ejemplo vivo hace el resto; si hay más, es otra pantalla)');
    const def = bs.find(b => b.tipo === 'definicion'); if (!def || palabras(def.texto).length < E.def) mal(d, 'falta la definición (bloque definicion de ' + E.def + ' palabras o más, ' + E.nombre + ')');
    if (E.parrafo && !tipos.includes('parrafo')) mal(d, 'falta el párrafo que explica por qué es así o para qué sirve');
    if (E === ETAPAS.ciclo1 && tipos.filter(x => x === 'parrafo' || x === 'lista').length > 1) mal(d, 'primer ciclo: poco texto, todo visual. Definición corta y, como mucho, un párrafo o una lista corta');
    ['ejemplo', 'pasos', 'error'].forEach(k => { if (tipos.includes(k)) mal(d, 'no lleva bloque «' + k + '»: el procedimiento y el caso los muestra el ejemplo vivo de al lado (no se explica dos veces)'); });
    if (/\b(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)\b/i.test(txt)) mal(d, 'menciona meses del calendario');
    if (/como (vimos|viste) en la clase/i.test(txt)) mal(d, 'remite a la clase en vez de explicar');
    const g = grams(txt); let rep = 0; g.forEach(x => { if (fu.has(x)) rep++; });
    if (g.size && rep / g.size > MAX_COPIA) mal(d, 'copia el borrador o la clase (' + Math.round(rep / g.size * 100) + ' % de frases repetidas; máximo ' + MAX_COPIA * 100 + ' %)');
    ['ejemplo', 'ejercicio'].forEach(k => { if (t[k] && !t[k].motor) mal(d, k + ' sin motor'); });
    if (t.ejemplo && EJEMPLO_CON_TEXTO.includes(t.ejemplo.motor)) mal(d, 'el ejemplo «' + t.ejemplo.motor + '» repite en texto lo que ya dice la explicación: usá un ejemplo visual del banco (o agregalo al banco)');
    if (t.ejercicio && t.ejercicio.motor in MODO_OBLIGATORIO) { const ok = MODO_OBLIGATORIO[t.ejercicio.motor], md = (t.ejercicio.p || {}).modo;
      if (!md && t.ejercicio.motor !== 'descomponer_x') mal(d, 'el ejercicio «' + t.ejercicio.motor + '» mezcla contenidos: elegí el modo que corresponde a ESTA pantalla (p.modo)');
      else if (ok && md && !ok.includes(md)) mal(d, 'modo «' + md + '» no existe para ' + t.ejercicio.motor + ' (' + ok.join(', ') + ')'); }
    if (!t.ejercicio || !t.ejercicio.motor) mal(d, 'todo tema lleva su ejercicio de práctica del banco (ejercicio con motor, con "Otros números")');
    if (t.ejemplo && t.ejemplo.motor && !PASO_A_PASO.has(t.ejemplo.motor)) mal(d, 'el ejemplo «' + t.ejemplo.motor + '» todavía no muestra el paso a paso: convertilo en el banco (pasoAPaso + "pasos: true") antes de usarlo');
    if (!t.ejemplo || !t.ejemplo.motor) mal(d, 'todo tema lleva su ejemplo vivo del banco (ejemplo con motor), sin excepción. Lo de concepto no es un tema propio: se acopla al tema práctico que corresponde');
  });
  // "Recordá lo más importante" (formato CIDEAD): tarjetas con concepto + definición completa + ejemplo concreto
  const R = L.recuerda || [];
  if (R.length < E.rec[0] || R.length > E.rec[1]) mal(donde, '"Recordá lo más importante" lleva de ' + E.rec[0] + ' a ' + E.rec[1] + ' tarjetas (' + E.nombre + ')');
  R.forEach((r, i) => {
    const d = donde + ' · recordá ' + (i + 1);
    if (!r.concepto) mal(d, 'falta el concepto');
    if (palabras((r.concepto || '') + ' ' + (r.definicion || '')).length < E.recDef + 2) mal(d, 'la definición tiene que ser una oración completa (' + E.recDef + ' palabras o más), no dos palabras');
    if (!r.ejemplo || palabras(r.ejemplo).length < 2) mal(d, 'falta el ejemplo concreto (ej.: "D(18) = {1, 2, 3, 6, 9, 18}")');
  });
  // 26/11/2026: los ejemplos son propios: ninguna cuenta del PDF o de la clase de ese nivel se repite en la lección.
  { const fuente = ' ' + limpio(JSON.stringify(((M.niveles[n] || {}).secciones || []))).toLowerCase().replace(/\\u2212/g, '−') + ' ';
    const todo = L.temas.map(t => textoBloques(t.explicacion || [])).concat((L.recuerda || []).map(r => (r.definicion || '') + ' ' + (r.ejemplo || ''))).join(' ');
    const re = /\d[\d.,]*\s?(?:[×x+−\-÷:/]|y|por|de)\s?\d[\d.,]*/g, comunes = new Set(['60', '90', '100', '180', '360', '1.000', '10.000', '10']); const vistas = new Set();
    (limpio(todo).toLowerCase().match(re) || []).forEach(g => { const nums = g.match(/\d[\d.,]*/g).map(x => x.replace(/[.,]$/, '')); if (!nums.some(x => parseFloat(x.replace(/\./g, '').replace(',', '.')) >= 13 && !comunes.has(x))) return;
      const g2 = g.replace(/[.,]$/, ''); if (!vistas.has(g2) && fuente.includes(g2)) { vistas.add(g2); mal(donde, 'el ejemplo «' + g2 + '» es la misma cuenta del PDF del nivel: los ejemplos tienen que ser propios'); } }); }
  // 26/11/2026: NO hay mínimo de pantallas. Una pantalla = un saber nuevo con ejemplo y práctica PROPIOS.
  // Advertencias, contraejemplos, casos especiales y "verificar" van dentro de la pantalla a la que pertenecen.
  const vistos = {};
  L.temas.forEach((t, i) => { ['ejemplo', 'ejercicio'].forEach(k => { if (!t[k]) return; const key = k + JSON.stringify(t[k]);
    if (vistos[key] !== undefined) mal(donde + ' · tema ' + (i + 1) + ' «' + (t.titulo || '') + '»', 'repite el ' + k + ' del tema ' + (vistos[key] + 1) + ': si no tiene ' + k + ' propio no es una pantalla, va dentro de la otra (como paso, contraejemplo o «Cuidado»)');
    else vistos[key] = i; }); });
  if (E.parrafo) L.temas.forEach((t, i) => { (t.explicacion || []).filter(b => b.tipo === 'parrafo' || b.tipo === 'definicion').forEach(b => { limpio(b.texto).split(/(?<=[.!?])\s+/).forEach(o => { const w = palabras(o).length; if (w && w < 6 && !/[=×÷√∛]/.test(o)) mal(donde + ' · tema ' + (i + 1) + ' «' + (t.titulo || '') + '»', 'oración de relleno o incompleta: «' + o.trim() + '» (' + w + ' palabras). Explicá, no rellenes'); }); }); });
}

for (const ruta of process.argv.slice(2)) {
  const M = JSON.parse(fs.readFileSync(ruta, 'utf8')), antes = errores;
  console.log(ruta);
  const revisar = (niveles, extra) => Object.keys(niveles || {}).forEach(n => {
    const secs = (niveles[n] || {}).secciones || [];
    if (!secs.length && !(niveles[n] || {}).pdf_en_otra_mision && !(niveles[n] || {}).leccion) mal(extra + 'nivel ' + n, 'no tiene secciones');
    secs.forEach((s, i) => {
      if (s.practica) practica(s.practica, extra + 'nivel ' + n + ' · tema ' + (i + 1) + ' «' + (s.titulo || '') + '»'); // opcional: la lección la arma la máquina con el banco
      if (s.practica && s.practica.neutro) practica(Object.assign({}, s.practica, s.practica.neutro, { neutro: undefined }), extra + 'nivel ' + n + ' · tema ' + (i + 1) + ' (neutro)');
    });
  });
  revisar(M.niveles, '');
  // Misión nueva (no está en tools/calidad_existentes.txt): cada nivel 1 a 4 trae su lección interactiva escrita en sesión. La máquina ya no la inventa.
  if (!EXISTENTES.has(ruta.replace(/\\/g, '/').replace(/^\.\//, ''))) Object.keys(M.niveles || {}).forEach(n => {
    if (Number(n) >= 1 && Number(n) <= 4 && !(M.niveles[n].leccion && (M.niveles[n].leccion.temas || []).length)) mal('nivel ' + n, 'falta la lección interactiva (niveles.' + n + '.leccion), escrita en sesión con las reglas de docs/reglas-leccion-interactiva.md');
  });
  Object.keys(M.niveles || {}).forEach(n => { const L = M.niveles[n].leccion; if (L && Array.isArray(L.temas) && L.temas.some(t => t.explicacion)) leccion(ruta, M, n, L, 'lección nivel ' + n); });
  if (M.alternativa && M.alternativa.niveles) revisar(M.alternativa.niveles, 'alternativa · ');
  // Misión VARIANTE (trae bloques "neutro" o "variante": true): la lección, las actividades y el examen no pueden tener palabras
  // que solo se usan en la Argentina sin su versión para alumnos de otros países ("neutro": {"campo": ".."} al lado).
  if (M.variante === true || JSON.stringify({ n: M.niveles, a: M.act, e: M.examen }).includes('"neutro"')) {
    const LOC = /(^|[^a-záéíóúñ])(pesos?|vuelto|argentin[oa]s?|colectivos?|subtes?)(?![a-záéíóúñ])/i;
    const mirar = (o, donde) => { if (!o || typeof o !== 'object' || o.motor) return; if (Array.isArray(o)) return o.forEach(x => mirar(x, donde));
      Object.keys(o).forEach(k => { if (k === 'neutro') return; const v = o[k];
        if (typeof v === 'string') { const m = LOC.exec(limpio(v)); if (m && !(o.neutro && o.neutro[k] !== undefined)) mal(donde, 'misión VARIANTE: «' + m[2] + '» se usa solo en la Argentina y falta su versión para otros países ("neutro": {"' + k + '": ".."} al lado)'); }
        else mirar(v, donde); }); };
    Object.keys(M.niveles || {}).forEach(n => mirar((M.niveles[n] || {}).leccion, 'variante · lección nivel ' + n));
    Object.keys(M.act || {}).forEach(n => mirar(M.act[n], 'variante · actividades nivel ' + n));
    mirar(M.examen, 'variante · examen');
  }
  console.log(errores === antes ? '  ✔ lección interactiva OK' : '  ' + (errores - antes) + ' problema(s)');
}
process.exit(errores ? 1 : 0);
