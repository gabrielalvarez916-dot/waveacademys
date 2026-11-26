// MÁQUINA DE LA LECCIÓN INTERACTIVA (Matemática). Sin IA: lee el borrador de cada nivel (mision-N.json) y arma la lección:
//  - temas: cada sección con contenido propio es un tema; las secciones cortas (un párrafo suelto) se juntan con la anterior;
//  - a cada tema le elige del BANCO DE LA LECCIÓN (js/leccion-banco.js, separado del de actividades) un ejemplo vivo y un ejercicio,
//    según de qué trata el tema; si ningún motor corresponde, el tema queda con la explicación sola.
// Uso: node tools/interactiva/armar.js [--json salida.json] contenido/matematica-*/mision-N/mision-N.json ...
'use strict';
const fs = require('fs');
const N = s => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/<[^>]+>/g, ' ');
const texto = sec => N((sec.bloques || []).map(b => [b.titulo, b.texto, (b.items || []).join(' ')].join(' ')).join(' '));
const pesado = sec => (sec.bloques || []).some(b => ['tabla', 'imagen', 'definicion', 'ejemplo', 'pasos'].includes(b.tipo));

// [condición sobre (título, contexto del nivel), motor] — el primero que coincide gana
const EJEMPLO = [
  [(t) => /maximo comun divisor|\bmcd\b|divisores comunes|coprimos|repartos sin resto/.test(t), { motor: 'explorador2', p: { modo: 'mcd' } }],
  [(t) => /minimo comun multiplo|\bmcm\b|multiplos comunes|coincidencias/.test(t), { motor: 'explorador2', p: { modo: 'mcm' } }],
  [(t) => /factores primos|descomposicion|siempre la misma|con potencias/.test(t), { motor: 'escalera_factores', p: {} }, (t, c) => /primo|divisor|factor/.test(c)],
  [(t) => /primo|compuesto|criba/.test(t), { motor: 'explorador', p: { modo: 'primo' } }],
  [(t) => /divisor|repartos sin sobrantes/.test(t), { motor: 'explorador', p: { modo: 'divisores' } }],
  [(t) => /multiplo|cosas que se repiten|patrones que se repiten/.test(t), { motor: 'explorador', p: { modo: 'multiplos' } }, (t, c) => /multiplo/.test(c)],
  [(t) => /de decimal a binario/.test(t), { motor: 'pasoapaso', p: { u: '/actividades/pasoapaso/decimal-a-binario.html' } }],
  [(t) => /de binario a decimal/.test(t), { motor: 'pasoapaso', p: { u: '/actividades/pasoapaso/binario-a-decimal.html' } }],
  [(t) => /descomponer un numero/.test(t), { motor: 'pasoapaso', p: { u: '/actividades/pasoapaso/descomposicion-aditiva.html' } }],
  [(t) => /descomponer con potencias/.test(t), { motor: 'pasoapaso', p: { u: '/actividades/pasoapaso/descomposicion-multiplicativa.html' } }],
  [(t) => /unidades de longitud|todo en la misma unidad/.test(t), { motor: 'escalera_unidades', p: { magnitud: 'longitud' } }],
  [(t) => /capacidad/.test(t), { motor: 'escalera_unidades', p: { magnitud: 'capacidad' } }],
  [(t) => /unidades de masa|gramo/.test(t), { motor: 'escalera_unidades', p: { magnitud: 'masa' } }],
  [(t) => /balanza|operaciones inversas|igualdad y ecuacion|x en los dos miembros|pasar.{0,3} un termino|^solucion$/.test(t), { motor: 'balanza', p: {} }, (t, c) => /ecuacion/.test(c)],
];
const EJERCICIO = [
  [(t) => /maximo comun divisor|\bmcd\b|divisores comunes|repartos sin resto/.test(t), { motor: 'mcd_guiado', p: {} }],
  [(t) => /minimo comun multiplo|\bmcm\b|multiplos comunes|coincidencias/.test(t), { motor: 'cajas', p: { modo: 'multiplos' } }],
  [(t) => /criterio|divisib|por 2, 5|por 3 y 9|por 4 y|por 6 y|por 11|combinar criterios|la ultima cifra|suma de las cifras/.test(t), { motor: 'cajas', p: { modo: 'divisible' } }],
  [(t) => /primo|compuesto|criba|factores primos/.test(t), { motor: 'cajas', p: { modo: 'primos' } }],
  [(t) => /divisor/.test(t), { motor: 'cajas', p: { modo: 'divisores' } }],
  [(t) => /multiplo/.test(t), { motor: 'cajas', p: { modo: 'multiplos' } }],
  [(t) => /equivalente|amplificar/.test(t), { motor: 'llevar', p: { modo: 'equivalentes' } }, (t, c) => /fraccion/.test(c)],
  [(t) => /irreducible|simplificar/.test(t), { motor: 'llevar', p: { modo: 'irreducibles' } }, (t, c) => /fraccion/.test(c)],
  [(t) => /propias|impropias|referentes|mixtos/.test(t), { motor: 'cajas', p: { modo: 'fraccion1' } }, (t, c) => /fraccion/.test(c)],
  [(t) => /parte de un todo|fraccion como cociente|como se lee/.test(t), { motor: 'letras', p: { modo: 'fraccion' } }, (t, c) => /fraccion/.test(c)],
  [(t) => /raices de enteros|raiz cuadrada|raiz de/.test(t), { motor: 'llevar', p: { modo: 'raices' } }],
  [(t) => /potencia|cuadrados y cubos|base negativa|−3²|-3²|ojo con los parentesis/.test(t), { motor: 'llevar', p: { modo: 'potencias' } }, (t, c) => !/fraccion|notacion cientifica/.test(t)],
  [(t) => /sumar en la recta|las reglas|varios sumandos|restar es sumar|suma algebraica|suprimir parentesis|diferencias|agrupar por signo/.test(t), { motor: 'llevar', p: { modo: 'sumas' } }, (t, c) => /entero/.test(c)],
  [(t) => /recta|simetria|distancia entre|opuesto|valor absoluto/.test(t), { motor: 'recta', p: {} }, (t, c) => /entero/.test(c)],
  [(t) => /ordenar|comparar|enteros de un intervalo|anterior y siguiente/.test(t), { motor: 'ordenar', p: { modo: 'enteros' } }, (t, c) => /entero/.test(c) && !/decimal|fraccion/.test(c)],
  [(t) => /comparar decimales|ordenar/.test(t), { motor: 'ordenar', p: { modo: 'decimales' } }, (t, c) => /decimal/.test(c) && !/fraccion|entero/.test(t)],
  [(t) => /ordenar varias|comparar fracciones|mismo denominador o mismo numerador/.test(t), { motor: 'ordenar', p: { modo: 'fracciones' } }],
  [(t) => /^suma y resta$|suma y resta de decimales/.test(t), { motor: 'columnas', p: { op: 'mixta' } }, (t, c) => /decimal/.test(c)],
  [(t) => /fracciones decimales|de decimal a fraccion|de fraccion a decimal|comparar decimales/.test(t), { motor: 'posicional', p: { modo: 'decimal' } }, (t, c) => !/periodic/.test(c)],
  [(t) => /numeros grandes/.test(t), { motor: 'letras', p: { modo: 'pagare' } }],
  [(t) => /valor posicional|posicion y valor|cada lugar es/.test(t), { motor: 'posicional', p: { modo: 'ubicar' } }],
  [(t) => /proporcionalidad directa|la constante|regla de tres directa|con la constante/.test(t), { motor: 'proporcional', p: {} }],
];
function elegir(reglas, t, c) { for (const [cond, m, extra] of reglas) if (cond(t, c) && (!extra || extra(t, c))) return JSON.parse(JSON.stringify(m)); return null; }

function armarNivel(nv) {
  const secs = nv.secciones || [], ctx = N([nv.objetivo, (nv.vas_a_ver || []).join(' '), secs.map(s => s.titulo).join(' ')].join(' '));
  const temas = [];
  secs.forEach((s, i) => {
    const t = N(s.titulo).trim(), tx = texto(s), ej = elegir(EJEMPLO, t, ctx), ex = elegir(EJERCICIO, t, ctx);
    const corta = !ej && !ex && !pesado(s) && tx.length < 180 && !s.practica;
    if (corta && temas.length) { temas[temas.length - 1].secs.push(i); return; }   // un párrafo suelto se junta con el tema anterior
    temas.push({ titulo: s.titulo, secs: [i], ejemplo: ej || undefined, ejercicio: ex || undefined });
  });
  // dos temas seguidos con el mismo ejemplo y el mismo ejercicio no se repiten: el segundo se suma al primero
  for (let k = temas.length - 1; k > 0; k--) {
    const a = temas[k - 1], b = temas[k];
    if (a.ejemplo && b.ejemplo && JSON.stringify(a.ejemplo) === JSON.stringify(b.ejemplo) && JSON.stringify(a.ejercicio) === JSON.stringify(b.ejercicio)) { a.secs = a.secs.concat(b.secs); temas.splice(k, 1); }
  }
  return { v: 1, temas };
}

const args = process.argv.slice(2); let salida = null;
if (args[0] === '--json') { salida = args[1]; args.splice(0, 2); }
const out = [], sinMotor = [];
let nt = 0, nej = 0, nex = 0;
for (const ruta of args) {
  if (!/contenido\/matematica-/.test(ruta)) continue;   // por ahora el banco es de Matemática
  const M = JSON.parse(fs.readFileSync(ruta, 'utf8')), niveles = {};
  for (const n of Object.keys(M.niveles || {})) {
    const L = armarNivel(M.niveles[n]); niveles[n] = L;
    L.temas.forEach(t => { nt++; if (t.ejemplo) nej++; if (t.ejercicio) nex++; if (!t.ejemplo && !t.ejercicio) sinMotor.push(ruta.split('/')[1] + ' M' + M.tema + ' N' + n + ' · ' + t.titulo); });
  }
  const r = { subject_id: M.subject_id, tema: M.tema, niveles };
  if (M.alternativa && M.alternativa.niveles) { r.alternativa = { niveles: {} }; for (const n of Object.keys(M.alternativa.niveles)) r.alternativa.niveles[n] = armarNivel(M.alternativa.niveles[n]); }
  out.push(r);
}
console.log(`Misiones: ${out.length} · temas: ${nt} · con ejemplo vivo: ${nej} · con ejercicio: ${nex} · solo explicación: ${sinMotor.length}`);
if (process.env.VER_SIN_MOTOR) sinMotor.forEach(x => console.log('  sin motor ·', x));
if (salida) fs.writeFileSync(salida, JSON.stringify(out));
