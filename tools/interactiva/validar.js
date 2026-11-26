// CONTROL DE CALIDAD de la lección interactiva (lo corre la máquina de misiones antes de cargar; si algo falla, no se carga nada).
// Cada sección de cada nivel tiene que traer "practica" (ver docs/leccion-interactiva.md). Prueba 60 sorteos de cada plantilla.
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

for (const ruta of process.argv.slice(2)) {
  const M = JSON.parse(fs.readFileSync(ruta, 'utf8')), antes = errores;
  console.log(ruta);
  const revisar = (niveles, extra) => Object.keys(niveles || {}).forEach(n => {
    const secs = (niveles[n] || {}).secciones || [];
    if (!secs.length) mal(extra + 'nivel ' + n, 'no tiene secciones');
    secs.forEach((s, i) => {
      practica(s.practica, extra + 'nivel ' + n + ' · tema ' + (i + 1) + ' «' + (s.titulo || '') + '»');
      if (s.practica && s.practica.neutro) practica(Object.assign({}, s.practica, s.practica.neutro, { neutro: undefined }), extra + 'nivel ' + n + ' · tema ' + (i + 1) + ' (neutro)');
    });
  });
  revisar(M.niveles, '');
  if (M.alternativa && M.alternativa.niveles) revisar(M.alternativa.niveles, 'alternativa · ');
  console.log(errores === antes ? '  ✔ lección interactiva OK' : '  ' + (errores - antes) + ' problema(s)');
}
process.exit(errores ? 1 : 0);
