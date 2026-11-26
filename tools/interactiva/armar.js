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
// Motores de js/leccion-banco2.js: [condición sobre el título, condición sobre el contexto del nivel (opcional), ejemplo, ejercicio]
const P = (m, p) => ({ motor: m, p: p || {} });
const PARES = [
  [/complementari|suplementari|relaciones entre angulos|angulos entre secantes|opuestos por el vertice/, null, P('transportador'), P('angulo_falta', { modo: 'suplementario' })],
  [/angulo|transportador|clasificacion/, /angulo/, P('transportador'), P('angulo_tipo')],
  [/suma es 180|angulo que falta|angulo exterior|isosceles y equilateros|con ecuaciones/, /triangulo/, P('triangulo'), P('angulo_falta', { modo: 'triangulo' })],
  [/triangulo|desigualdad triangular|segun sus lados|segun sus angulos|dos nombres|siempre se puede|tres lados/, null, P('triangulo'), P('angulo_falta', { modo: 'triangulo' })],
  [/360|cuadrilatero|paralelogramo|rectangulo, rombo|diagonales/, /cuadrilatero|paralelogramo/, P('poligono_angulos'), P('angulo_falta', { modo: 'cuadrilatero' })],
  [/vuelta a un circulo|circulo|circunferencia/, null, P('circulo'), P('area_perimetro', { que: 'perimetro' })],
  [/perimetro|figuras compuestas/, /perimetro/, P('area_figura', { figura: 'rectangulo' }), P('area_perimetro', { que: 'perimetro' })],
  [/unidades de superficie/, null, P('escalera_unidades', { magnitud: 'superficie' }), P('convertir_unidades', { magnitud: 'superficie' })],
  [/unidades de volumen/, null, P('escalera_unidades', { magnitud: 'volumen' }), P('convertir_unidades', { magnitud: 'volumen' })],
  [/unidades de longitud|todo en la misma unidad/, null, P('escalera_unidades', { magnitud: 'longitud' }), P('convertir_unidades', { magnitud: 'longitud' })],
  [/volumen y capacidad|capacidad/, null, P('escalera_unidades', { magnitud: 'capacidad' }), P('convertir_unidades', { magnitud: 'capacidad' })],
  [/triangulo y paralelogramo/, null, P('area_figura', { figura: 'triangulo' }), P('area_perimetro', { que: 'area' })],
  [/rombo y trapecio/, null, P('area_figura', { figura: 'trapecio' }), P('area_perimetro', { que: 'area' })],
  [/area|figuras compuestas|baldosas/, null, P('area_figura', { figura: 'rectangulo' }), P('area_perimetro', { que: 'area' })],
  [/volumen|cubo unidad|prisma y cubo|cajas/, null, P('volumen_cubitos'), P('volumen')],
  [/porcentaje|descuento|aumento|interes|variacion|precio final|factor de/, null, P('porcentaje_barra', { modo: 'parte' }), P('porcentaje')],
  [/notacion cientifica|ajustar el resultado/, null, P('notacion_cientifica'), P('notacion')],
  [/periodic|exactos y periodicos|puros y mixtos/, null, P('periodo'), P('decimal_tipo')],
  [/fraccion de una fraccion|producto de fracciones|el producto|simplificar antes/, /fraccion/, P('fraccion_area'), P('fraccion_operar', { op: 'producto' })],
  [/inverso|dividir con|cuantas veces entra/, /fraccion/, P('fraccion_area'), P('fraccion_operar', { op: 'division' })],
  [/igual denominador|distinto denominador|denominador comun|suma y resta|numeros mixtos|subdividir/, /fraccion/, P('fraccion_barras', { op: 'suma' }), P('fraccion_operar', { op: 'suma' })],
  [/redonde|estimar|truncamiento|aproximacion/, null, P('redondeo'), P('redondear')],
  [/agrupar de a 60|sumar y restar tiempos|grados y minutos|pasar de una unidad a otra/, /60|tiempo|sexagesimal|hora/, P('sexagesimal'), P('sexagesimal_conv')],
  [/base 2|como se escribe y se lee/, /binario|base 2/, P('binario_lamparas'), P('binario_conv')],
  [/regla de los signos|menos por menos|varios factores|division con resto|suma repetida/, /entero|negativ/, P('signos'), P('combinadas')],
  [/jerarquia|operaciones|parentesis|signos de agrupacion|calculos largos|enunciado a calculo|mismo nivel|separar en terminos|adentro hacia afuera|el orden completo|calculadora|errores de tipeo|la raiz agrupa|combinadas|todo a fraccion|todo a decimal|un mismo formato/, null, P('jerarquia'), P('combinadas')],
  [/potencia|cuadrados y cubos|exponente|base negativa|igual base|crecen rapido|base fraccionaria/, null, P('potencias_explorar'), null],
  [/raiz|cuadrados perfectos|estimar una raiz|raices/, null, P('raiz_explorar'), null],
  [/positivos, negativos|el opuesto|los numeros enteros|la recta entera|simetria|distancia|valor absoluto|los negativos|situaciones|por que hacen falta|saldos|temperaturas/, /entero|negativ/, P('recta_explorar'), null],
  [/inversa|producto constante/, /proporcional/, P('proporcionalidad', { modo: 'inversa' }), P('regla_de_tres', { modo: 'inversa' })],
  [/proporci|razon|regla de tres|la constante|termino desconocido|el grafico|no todo lo que crece|problemas|compuesta|directa o inversa/, /proporci|razon/, P('proporcionalidad', { modo: 'directa' }), P('regla_de_tres', { modo: 'directa' })],
  [/plano cartesiano|ubicar un punto|graficar|interpretar un grafico/, null, P('plano'), P('coordenadas')],
  [/funcion|tabla de valores|calcular y|creciente|ordenada al origen|hallar x|completar|y = kx|encontrar k/, /funcion/, P('funcion_lineal'), P('funcion_tabla')],
  [/valor numerico|con negativos|formulas|tablas de valores|variables y constantes|leer expresiones|un valor no alcanza/, /expresion|algebra|variable|letra/, P('valor_numerico'), P('valor_numerico_x')],
  [/traducir|lenguaje/, null, P('valor_numerico'), P('traducir')],
  [/terminos semejantes|simplificar|expresiones equivalentes/, /expresion|algebra|termino/, P('terminos_semejantes'), P('reducir_terminos')],
  [/patron|recursiva|terminos lejanos|posicion y valor|generalizar|secuencia/, /patron|secuencia|regularidad/, P('patron_figuras'), P('patron_termino')],
  [/ecuacion|solucion|verificar|paso a paso|con enteros|cinco pasos|edades|dinero|geometria/, /ecuacion/, P('balanza'), P('ecuacion')],
  [/mas chica o mas grande|el limite de las palabras|problemas mixtos|verificar y armar/, /mcd|mcm/, P('explorador2', { modo: 'mcm' }), P('mcd_mcm_problemas')],
  [/leer y plantear|fraccion de una cantidad|repartir en partes iguales/, /fraccion/, P('fraccion_cantidad'), P('fraccion_cantidad_x')],
  [/regla de tres compuesta|con una inversa/, null, P('proporcionalidad', { modo: 'directa' }), P('regla_tres_compuesta')],
  [/escala|del plano a la realidad|de la realidad al plano|pasar unidades/, /escala/, P('escala'), P('escala_x')],
  [/velocidad|densidad|despejar|convertir/, /velocidad/, P('velocidad'), P('velocidad_x')],
  [/monomio|semejantes|sumar semejantes|multiplicar/, /monomio/, P('monomio'), P('monomio_x')],
  [/polinomio|suma|resta|ejemplos/, /polinomio/, P('terminos_semejantes'), P('polinomio_operar')],
  [/distributiva|monomio por polinomio|binomio por binomio|ejemplos/, /distributiva/, P('distributiva'), P('distributiva_x')],
  [/denominadores|un denominador|dos denominadores|ejemplos/, /denominador/, P('balanza'), P('ecuacion_denominadores')],
  [/tabla de frecuencias|variables y datos/, null, P('frecuencias'), P('tabla_frecuencias')],
  [/barras|grafico de lineas|circular/, /frecuencia|grafico|estadistic/, P('frecuencias'), P('barras_armar')],
  [/media|moda|mediana|valores extremos|que dice cada una/, null, P('medidas'), P('media_moda_mediana')],
  [/espacio muestral|contar casos|combinacion|azar o no|sucesos/, /azar|probabil|muestral/, P('combinaciones_tabla'), P('combinaciones')],
  [/favorables|probabilidad|fraccion, decimal y porcentaje|entre 0 y 1|comparar y experimentar/, /probabil|azar/, P('urna'), P('probabilidad')],
];
function elegirPar(t, c) { for (const [rt, rc, ej, ex] of PARES) if (rt.test(t) && (!rc || rc.test(c))) return { ej: ej && JSON.parse(JSON.stringify(ej)), ex: ex && JSON.parse(JSON.stringify(ex)) }; return {}; }
function elegir(reglas, t, c) { for (const [cond, m, extra] of reglas) if (cond(t, c) && (!extra || extra(t, c))) return JSON.parse(JSON.stringify(m)); return null; }

function armarNivel(nv) {
  const secs = nv.secciones || [], ctx = N([nv.objetivo, (nv.vas_a_ver || []).join(' '), secs.map(s => s.titulo).join(' ')].join(' '));
  // Cada tema es PRÁCTICO (tiene ejemplo o ejercicio). Lo de concepto no es un tema propio: se acopla al tema práctico siguiente
  // (o al anterior si es lo último), como en CIDEAD. Si en todo el nivel no hay ningún tema práctico, queda una sola pantalla y se avisa.
  const temas = []; let pend = [];
  secs.forEach((s, i) => {
    const t = N(s.titulo).trim(), par = elegirPar(t, ctx), ej = elegir(EJEMPLO, t, ctx) || par.ej, ex = elegir(EJERCICIO, t, ctx) || par.ex;
    if (!ej && !ex && !s.practica) { pend.push(i); return; }
    temas.push({ titulo: s.titulo, secs: pend.concat([i]), ejemplo: ej || undefined, ejercicio: ex || undefined }); pend = [];
  });
  if (pend.length) { if (temas.length) temas[temas.length - 1].secs = temas[temas.length - 1].secs.concat(pend); else temas.push({ titulo: (secs[0] || {}).titulo, secs: pend, sinMotor: true }); }
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
    const escrita = M.niveles[n].leccion && Array.isArray(M.niveles[n].leccion.temas) && M.niveles[n].leccion.temas.some(t => t.explicacion);
    const L = escrita ? M.niveles[n].leccion : armarNivel(M.niveles[n]); niveles[n] = L;   // la lección escrita en sesión manda
    L.temas.forEach(t => { nt++; if (t.ejemplo) nej++; if (t.ejercicio) nex++; if (!t.ejemplo && !t.ejercicio && !t.secs.some(i => (M.niveles[n].secciones[i] || {}).practica)) sinMotor.push(ruta.split('/')[1] + ' M' + M.tema + ' N' + n + ' · ' + t.titulo); });
  }
  const r = { subject_id: M.subject_id, tema: M.tema, niveles };
  if (M.alternativa && M.alternativa.niveles) { r.alternativa = { niveles: {} }; for (const n of Object.keys(M.alternativa.niveles)) r.alternativa.niveles[n] = armarNivel(M.alternativa.niveles[n]); }
  out.push(r);
}
console.log(`Misiones: ${out.length} · temas: ${nt} · con ejemplo vivo: ${nej} · con ejercicio: ${nex} · niveles sin ningún motor (faltan en el banco): ${sinMotor.length}`);
if (process.env.VER_SIN_MOTOR) sinMotor.forEach(x => console.log('  sin motor ·', x));
if (salida) fs.writeFileSync(salida, JSON.stringify(out));
