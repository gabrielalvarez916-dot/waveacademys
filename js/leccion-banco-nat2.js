/* BANCO DE LA LECCIÓN · NATURALES (parte 2): materia, química y herramientas del laboratorio (medir, tamaños, gráficos, experimentos).
   Usa las herramientas comunes de js/leccion-banco-nat.js (H.nat). Todos los ejemplos son PASO A PASO y cada uno con su propio formato visual. */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h || !B._h.nat) return;
  var H = B._h, M = B.motores, R = H.R, pick = H.pick, mezclar = H.mezclar, fmt = H.fmt, num = H.num, N = H.nat;
  var escena = H.escena, ctrl = H.ctrl, respuesta = H.respuesta, cajas = H.cajas;
  var C = N.C, S = N.S, tx = N.tx, txw = N.txw, ln = N.ln, fl = N.fl, ci = N.ci, rc = N.rc, em = N.em, r1 = N.r1, sel = N.sel, otro = N.otro, rot = N.rot, nota = N.nota, elegir = N.elegir, ordenar = N.ordenar, tocar = N.tocar;
  function r2(x) { return Math.round(x * 100) / 100; }
  function caja(x, y, w, h) { return rc(x, y, w, h, '#F3FBF7', C.osc, 6, ' stroke-width="3"'); }

  // 1) MODELO DE PARTÍCULAS: sólido, líquido y gas según la temperatura
  var SUST = [['Agua', 0, 100], ['Alcohol', -114, 78], ['Hierro', 1538, 2862], ['Nitrógeno', -210, -196], ['Mercurio', -39, 357]];
  function estado(s, t) { return t < s[1] ? 'sólido' : t < s[2] ? 'líquido' : 'gaseoso'; }
  function cajaPart(x, y, est, sem) { var b = caja(x, y, 150, 130), pts = [];
    if (est === 'sólido') for (var i = 0; i < 5; i++) for (var j = 0; j < 4; j++) pts.push([x + 30 + i * 22, y + 50 + j * 20]);
    else if (est === 'líquido') for (i = 0; i < 20; i++) pts.push([x + 14 + ((i * 37 + sem * 11) % 120), y + 64 + ((i * 23 + sem * 7) % 56)]);
    else for (i = 0; i < 12; i++) pts.push([x + 12 + ((i * 53 + sem * 13) % 124), y + 12 + ((i * 41 + sem * 5) % 104)]);
    pts.forEach(function (q, k) { b += ci(q[0], q[1], 8, '#8FB8E3', C.azul); if (k % 4 === 0) b += est === 'sólido' ? '<path d="M' + (q[0] - 12) + ',' + (q[1] - 12) + ' l4,0 M' + (q[0] + 12) + ',' + (q[1] - 12) + ' l-4,0" stroke="' + C.coral + '" stroke-width="2"/>' : fl(q[0] + 8, q[1], q[0] + (est === 'gaseoso' ? 26 : 16), q[1] - (est === 'gaseoso' ? 14 : 4), C.coral, 2); });
    return b; }
  function termo(x, y, t, min, max) { var h = 120, f = Math.max(0, Math.min(1, (t - min) / (max - min))); return rc(x - 6, y, 12, h, '#fff', C.osc, 6) + ci(x, y + h + 8, 11, C.coral, C.osc) + rc(x - 3, y + h - f * h, 6, f * h + 4, C.coral) + tx(x + 16, y + h - f * h + 4, fmt(t) + ' °C', { s: 12, w: 900 }); }
  M.particulas = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('s', 'Sustancia', SUST.map(function (s, i) { return [i, s[0]]; }), 0) + ctrl('f', 'Calentar (0 = muy frío · 100 = muy caliente)', 0, 100, 1, 40), function (o) { var s = SUST[+(o.s || 0)], f = o.f == null ? 40 : o.f, t = Math.round(s[1] - 40 + f / 100 * (s[2] - s[1] + 80)), e = estado(s, t), P = [], tmin = s[1] - 40, tmax = s[2] + 40;
      var mov = { 'sólido': 'vibran en su lugar, muy juntas y ordenadas: forma y volumen propios', 'líquido': 'están juntas pero se deslizan unas sobre otras: el líquido toma la forma del recipiente', 'gaseoso': 'están muy separadas y se mueven libres y rápido: el gas ocupa todo el recipiente' };
      P.push({ vis: S(470, 170, termo(60, 20, t, tmin, tmax) + tx(60, 165, s[0], { a: 'middle', s: 12, w: 800 }) + rc(130, 30, 320, 90, '#fff', C.gris, 10) + tx(290, 62, 'Funde a ' + fmt(s[1]) + ' °C', { a: 'middle', s: 14, w: 800 }) + tx(290, 92, 'Hierve a ' + fmt(s[2]) + ' °C', { a: 'middle', s: 14, w: 800 })), txt: 'Cada sustancia tiene su <b>punto de fusión</b> y su <b>punto de ebullición</b>. El ' + s[0].toLowerCase() + ' está a ' + fmt(t) + ' °C.' });
      P.push({ vis: S(470, 170, termo(60, 20, t, tmin, tmax) + cajaPart(160, 20, e, t % 5) + tx(235, 166, 'estado ' + e, { a: 'middle', s: 13, w: 900, c: C.coral })), txt: 'Comparamos: a ' + fmt(t) + ' °C está en estado <b>' + e + '</b>.' });
      P.push({ vis: S(470, 170, cajaPart(20, 20, 'sólido', 1) + cajaPart(170, 20, 'líquido', 2) + cajaPart(320, 20, 'gaseoso', 3) + ['sólido', 'líquido', 'gaseoso'].map(function (q, i) { return tx(95 + i * 150, 166, q, { a: 'middle', s: 12, w: 900, c: q === e ? C.coral : C.osc }); }).join('')), txt: 'En estado ' + e + ', las partículas ' + mov[e] + '.' });
      var cs = [['sólido', 'líquido', 'fusión'], ['líquido', 'gaseoso', 'vaporización'], ['gaseoso', 'líquido', 'condensación'], ['líquido', 'sólido', 'solidificación']], pos = { 'sólido': 70, 'líquido': 235, 'gaseoso': 400 };
      var g = ['sólido', 'líquido', 'gaseoso'].map(function (q) { return rc(pos[q] - 55, 70, 110, 40, q === e ? '#FFF3C4' : C.claro, q === e ? C.coral : C.teal, 12) + tx(pos[q], 95, q, { a: 'middle', s: 13, w: 900 }); }).join('');
      g += fl(125, 78, 180, 78, C.coral, 2) + tx(152, 70, 'fusión', { a: 'middle', s: 10.5 }) + fl(180, 104, 125, 104, C.azul, 2) + tx(152, 124, 'solidificación', { a: 'middle', s: 10.5 }) + fl(290, 78, 345, 78, C.coral, 2) + tx(318, 70, 'vaporización', { a: 'middle', s: 10.5 }) + fl(345, 104, 290, 104, C.azul, 2) + tx(318, 124, 'condensación', { a: 'middle', s: 10.5 }) + '<path d="M70,70 C120,10 350,10 400,70" fill="none" stroke="' + C.lila + '" stroke-width="2" marker-end="url(#natfl)"/>' + tx(235, 30, 'sublimación', { a: 'middle', s: 10.5, c: C.lila });
      P.push({ vis: S(470, 140, g), txt: 'Los <b>cambios de estado</b>: con calor (rojo) las partículas se separan; al enfriar (azul) se acercan. Son cambios físicos: la sustancia sigue siendo la misma.' });
      return P; });
  } };
  M.particulas_x = { tipo: 'ejercicio', render: function (el, p, api) {
    elegir(el, api, function () { var s = pick(SUST), t = pick([s[1] - 30, Math.round((s[1] + s[2]) / 2), s[2] + 40]), e = estado(s, t);
      return { cons: 'El <b>' + s[0].toLowerCase() + '</b> funde a ' + fmt(s[1]) + ' °C y hierve a ' + fmt(s[2]) + ' °C. ¿En qué estado está a <b>' + fmt(t) + ' °C</b>?', ops: ['sólido', 'líquido', 'gaseoso'], ok: e, ayuda: 'Por debajo del punto de fusión es sólido; entre los dos puntos, líquido; por encima del de ebullición, gas.', bien: '¡Bien! A ' + fmt(t) + ' °C está ' + e + '.' }; });
  } };

  // 2) MEZCLAS: cómo separarlas, con el aparato dibujado
  var MEZ = [['Arena y agua', 'heterogénea', 'la arena no se disuelve y sus granos son más grandes que los poros del papel', 'Filtración', 'filtro'], ['Sal disuelta en agua', 'homogénea (solución)', 'el agua se evapora con el calor y la sal no', 'Evaporación', 'evapora'], ['Limaduras de hierro y arena', 'heterogénea', 'el hierro es atraído por el imán y la arena no', 'Imantación', 'iman'],
    ['Aceite y agua', 'heterogénea', 'el aceite es menos denso y no se mezcla: queda arriba', 'Decantación', 'decanta'], ['Piedras y arena', 'heterogénea', 'las piedras son más grandes que los agujeros de la malla', 'Tamización', 'tamiz']];
  function aparato(k, fin) { var b = '';
    if (k === 'filtro') b = '<path d="M180,20 L290,20 L250,80 L220,80 Z" fill="#fff" stroke="' + C.osc + '" stroke-width="2"/><path d="M190,26 L280,26 L245,72 L225,72 Z" fill="#F5F0E1" stroke="#C29A1E" stroke-width="1.5"/>' + (fin ? '<path d="M200,40 L270,40 L250,62 L220,62 Z" fill="#D7B98E"/>' : '') + ln(235, 80, 235, 110, C.osc, 3) + rc(195, 110, 80, 60, '#EAF6FB', C.osc, 6) + (fin ? rc(197, 135, 76, 33, '#BBDEFB') : '') + tx(235, 188, fin ? 'arena en el papel · agua abajo' : 'embudo con papel de filtro', { a: 'middle', s: 11, w: 800 });
    if (k === 'evapora') b = rc(190, 70, 90, 40, '#EAF6FB', C.osc, 6) + (fin ? '<g fill="#fff" stroke="#999">' + [0, 1, 2, 3, 4].map(function (i) { return '<rect x="' + (198 + i * 15) + '" y="98" width="8" height="8"/>'; }).join('') + '</g>' : rc(192, 85, 86, 23, '#BBDEFB')) + em(235, 140, '🔥', 28) + (fin ? '' : em(215, 50, '💨', 18) + em(255, 45, '💨', 16)) + tx(235, 188, fin ? 'quedan los cristales de sal' : 'se calienta: el agua se va como vapor', { a: 'middle', s: 11, w: 800 });
    if (k === 'iman') b = rc(160, 120, 150, 40, '#F5F0E1', C.osc, 6) + '<g fill="#555">' + [0, 1, 2, 3, 4, 5].map(function (i) { return '<circle cx="' + (175 + i * 22) + '" cy="' + (fin ? 60 : 135) + '" r="3"/>'; }).join('') + '</g><g fill="#D7B98E">' + [0, 1, 2, 3, 4].map(function (i) { return '<circle cx="' + (185 + i * 22) + '" cy="145" r="4"/>'; }).join('') + '</g><path d="M200,20 L200,50 Q235,75 270,50 L270,20" fill="none" stroke="' + C.rosa + '" stroke-width="12"/>' + tx(235, 188, fin ? 'el hierro quedó pegado al imán' : 'acercamos un imán', { a: 'middle', s: 11, w: 800 });
    if (k === 'decanta') b = '<path d="M205,20 L265,20 L265,100 L240,140 L230,140 L205,100 Z" fill="#fff" stroke="' + C.osc + '" stroke-width="2"/><path d="M206,' + (fin ? 60 : 50) + ' L264,' + (fin ? 60 : 50) + ' L264,100 L240,138 L230,138 L206,100 Z" fill="#BBDEFB"/>' + rc(206, fin ? 30 : 22, 58, fin ? 30 : 28, '#F5D33B') + ln(235, 140, 235, 165, C.osc, 3) + (fin ? rc(205, 160, 60, 24, '#BBDEFB', C.osc, 4) : '') + tx(235, 196, fin ? 'el agua sale por abajo; el aceite queda' : 'ampolla de decantación: el aceite flota', { a: 'middle', s: 11, w: 800 });
    if (k === 'tamiz') b = ln(160, 70, 310, 70, C.osc, 3) + '<g stroke="#999">' + [0, 1, 2, 3, 4, 5, 6].map(function (i) { return '<line x1="' + (170 + i * 20) + '" y1="66" x2="' + (170 + i * 20) + '" y2="74"/>'; }).join('') + '</g>' + (fin ? '<g fill="#888"><circle cx="200" cy="58" r="8"/><circle cx="235" cy="56" r="10"/><circle cx="270" cy="58" r="7"/></g>' + rc(180, 140, 110, 20, '#D7B98E', null, 4) : '<g fill="#888"><circle cx="210" cy="40" r="8"/><circle cx="250" cy="36" r="10"/></g><g fill="#D7B98E"><circle cx="230" cy="44" r="3"/><circle cx="240" cy="48" r="3"/><circle cx="220" cy="50" r="3"/></g>') + tx(235, 188, fin ? 'piedras arriba · arena abajo' : 'tamiz: una malla con agujeros', { a: 'middle', s: 11, w: 800 });
    return S(470, 205, b); }
  M.mezclas = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Mezcla', MEZ.map(function (m, i) { return [i, m[0]]; }), 0), function (o) { var m = MEZ[+(o.i || 0)];
      return [{ vis: aparato(m[4], false), txt: 'Mezcla: <b>' + m[0].toLowerCase() + '</b>. Es una mezcla <b>' + m[1] + '</b>.' }, { vis: aparato(m[4], false) + nota('¿En qué se diferencian sus componentes?'), txt: 'Para separar, buscamos una <b>propiedad distinta</b>: ' + m[2] + '.' }, { vis: aparato(m[4], true), txt: 'Método: <b>' + m[3] + '</b>. Cada componente queda por su lado y no cambia: es un proceso físico.' }]; });
  } };
  M.mezclas_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    elegir(el, api, function () { var m = MEZ[rot(MEZ.length, u)]; return { cons: '¿Con qué método separarías <b>' + m[0].toLowerCase() + '</b>?', html: aparato(m[4], false).replace(/<text[^>]*>[^<]*<\/text>$/, ''), ops: MEZ.map(function (q) { return q[3]; }), ok: m[3], ayuda: 'Pensá qué propiedad distingue a los componentes.', bien: '¡Bien! ' + m[3] + ': ' + m[2] + '.' }; });
  } };

  // 3) DENSIDAD: un objeto en un vaso que flota o se hunde
  var LIQ = [['Agua', 1], ['Aceite', 0.92], ['Agua salada', 1.03], ['Miel', 1.4], ['Alcohol', 0.79]];
  function vaso(dObj, dLiq, nom, col) { var flota = dObj < dLiq, y = flota ? 72 - 10 : 168, b = rc(150, 50, 170, 150, '#fff', C.osc, 6) + rc(152, 80, 166, 118, col || '#BBDEFB') + tx(235, 216, nom + ': ' + fmt(dLiq) + ' g/cm³', { a: 'middle', s: 11.5, w: 800 });
    return b + rc(210, y - 22, 50, 40, '#E07A2F', C.osc, 6) + tx(235, y + 3, fmt(r2(dObj)), { a: 'middle', s: 12, w: 900, c: '#fff' }); }
  M.densidad = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('m', 'Masa del objeto (g)', 10, 500, 5, 120) + ctrl('v', 'Volumen del objeto (cm³)', 10, 500, 5, 150) + sel('l', 'Líquido', LIQ.map(function (l, i) { return [i, l[0]]; }), 0), function (o) { var m = o.m || 120, v = o.v || 150, d = m / v, L = LIQ[+(o.l || 0)], P = [];
      P.push({ vis: S(470, 90, rc(60, 15, 120, 60, '#FFF3C4', C.sol, 10) + tx(120, 42, fmt(m) + ' g', { a: 'middle', s: 18, w: 900 }) + tx(120, 64, 'masa (balanza)', { a: 'middle', s: 11 }) + rc(290, 15, 120, 60, '#EAF6FB', C.azul, 10) + tx(350, 42, fmt(v) + ' cm³', { a: 'middle', s: 18, w: 900 }) + tx(350, 64, 'volumen (probeta)', { a: 'middle', s: 11 })), txt: 'Medimos la <b>masa</b> y el <b>volumen</b> del objeto.' });
      P.push({ vis: S(470, 70, tx(235, 42, 'd = m / V = ' + fmt(m) + ' g ÷ ' + fmt(v) + ' cm³ = ' + fmt(r2(d)) + ' g/cm³', { a: 'middle', s: 17, w: 900 })), txt: 'La <b>densidad</b> dice cuánta masa hay en cada cm³: d = masa ÷ volumen.' });
      P.push({ vis: S(470, 225, vaso(d, L[1], L[0])), txt: d < L[1] ? 'Su densidad (' + fmt(r2(d)) + ') es <b>menor</b> que la del ' + L[0].toLowerCase() + ' (' + fmt(L[1]) + '): <b>flota</b>.' : 'Su densidad (' + fmt(r2(d)) + ') es <b>mayor</b> que la del ' + L[0].toLowerCase() + ' (' + fmt(L[1]) + '): <b>se hunde</b>.' });
      P.push({ vis: S(470, 140, LIQ.map(function (l, i) { var x = 20 + i * 90; return rc(x, 20, 80, 70, d < l[1] ? '#E8F5E9' : '#FCE4EC', d < l[1] ? C.verde : C.rosa, 10) + tx(x + 40, 48, l[0], { a: 'middle', s: 11, w: 800 }) + tx(x + 40, 70, fmt(l[1]), { a: 'middle', s: 12 }) + tx(x + 40, 112, d < l[1] ? 'flota' : 'se hunde', { a: 'middle', s: 12, w: 900, c: d < l[1] ? C.verde : C.rosa }); }).join('')), txt: 'El mismo objeto puede flotar en un líquido y hundirse en otro: depende de cuál es más denso.' });
      return P; });
  } };
  M.densidad_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var v = pick([10, 20, 25, 40, 50, 100]), d = pick([0.5, 0.8, 1.2, 2, 2.7, 7.9, 11.3]), m = r2(d * v);
      return { cons: 'Un objeto tiene una masa de <b>' + fmt(m) + ' g</b> y un volumen de <b>' + v + ' cm³</b>. ¿Cuál es su densidad? ¿Flota en agua (1 g/cm³)?', campos: [{ lab: 'Densidad', v: d, un: 'g/cm³', tol: 0.01 }, { tipo: 'texto', lab: '¿Flota? (sí / no)', v: d < 1 ? ['sí', 'si'] : ['no'] }], ayuda: 'd = masa ÷ volumen. Flota si es menos denso que el agua.', bien: '¡Bien! d = ' + fmt(d) + ' g/cm³: ' + (d < 1 ? 'flota.' : 'se hunde.') }; });
  } };

  // 4) ÁTOMO (modelo de Bohr) a partir de Z, con iones
  var EL = [['H', 'Hidrógeno', 1], ['He', 'Helio', 4], ['Li', 'Litio', 7], ['Be', 'Berilio', 9], ['B', 'Boro', 11], ['C', 'Carbono', 12], ['N', 'Nitrógeno', 14], ['O', 'Oxígeno', 16], ['F', 'Flúor', 19], ['Ne', 'Neón', 20], ['Na', 'Sodio', 23], ['Mg', 'Magnesio', 24], ['Al', 'Aluminio', 27], ['Si', 'Silicio', 28], ['P', 'Fósforo', 31], ['S', 'Azufre', 32], ['Cl', 'Cloro', 35], ['Ar', 'Argón', 40], ['K', 'Potasio', 39], ['Ca', 'Calcio', 40]];
  function capas(e) { var c = [], cap = [2, 8, 8, 2]; for (var i = 0; e > 0; i++) { var n = Math.min(e, cap[i] || 8); c.push(n); e -= n; } return c; }
  function bohr(Z, A, e, hasta) { var cx = 150, cy = 120, b = ci(cx, cy, 24, '#FFE0B2', C.coral) + tx(cx, cy - 2, Z + ' p⁺', { a: 'middle', s: 11, w: 900 }) + tx(cx, cy + 12, (A - Z) + ' n', { a: 'middle', s: 11, w: 900 }), cs = capas(e);
    cs.forEach(function (n, k) { if (k >= hasta) return; var rr = 42 + k * 24; b += ci(cx, cy, rr, 'none', C.gris); for (var j = 0; j < n; j++) { var a = -Math.PI / 2 + j * 2 * Math.PI / n; b += ci(cx + rr * Math.cos(a), cy + rr * Math.sin(a), 5, C.azul); } });
    return b; }
  M.atomo = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('z', 'Elemento', EL.map(function (x, i) { return [i + 1, (i + 1) + ' · ' + x[1]]; }), p.z || 11) + sel('q', 'Carga', [[0, 'átomo neutro'], [1, 'catión +1 (pierde 1 e⁻)'], [2, 'catión +2'], [-1, 'anión −1 (gana 1 e⁻)'], [-2, 'anión −2']], 0), function (o) { var Z = +(o.z || 11), x = EL[Z - 1], A = x[2], q = +(o.q || 0), e = Z - q, P = [], cs = capas(e);
      var ficha = function () { return rc(320, 40, 120, 130, '#fff', C.teal, 12) + tx(380, 70, A, { a: 'end', s: 12, w: 800 }) + tx(380, 140, Z, { a: 'end', s: 12, w: 800 }) + tx(385, 115, x[0] + (q ? '<tspan font-size="14" dy="-18">' + (Math.abs(q) > 1 ? Math.abs(q) : '') + (q > 0 ? '+' : '−') + '</tspan>' : ''), { s: 40, w: 900 }) + tx(380, 162, x[1], { a: 'middle', s: 11 }); };
      P.push({ vis: S(470, 240, bohr(Z, A, e, 0) + ficha()), txt: '<b>' + x[1] + '</b>: número atómico Z = ' + Z + ' → tiene <b>' + Z + ' protones</b> en el núcleo.' });
      P.push({ vis: S(470, 240, bohr(Z, A, e, 0) + ficha()), txt: 'Número másico A = ' + A + ' → neutrones = A − Z = ' + A + ' − ' + Z + ' = <b>' + (A - Z) + '</b>.' });
      cs.forEach(function (n, k) { P.push({ vis: S(470, 240, bohr(Z, A, e, k + 1) + ficha()), txt: 'Capa ' + (k + 1) + ': <b>' + n + ' electrones</b>' + (k === 0 ? ' (en la primera entran como máximo 2).' : k === 1 ? ' (en la segunda, hasta 8).' : '.') }); });
      P.push({ vis: S(470, 240, bohr(Z, A, e, 9) + ficha()), txt: q ? 'Como es un ion ' + (q > 0 ? 'positivo, perdió ' + q : 'negativo, ganó ' + (-q)) + ' electrón' + (Math.abs(q) > 1 ? 'es' : '') + ': tiene ' + e + ' electrones y ' + Z + ' protones.' : 'Átomo neutro: tantos electrones como protones (' + Z + '). Tiene <b>' + cs[cs.length - 1] + ' electr' + (cs[cs.length - 1] === 1 ? 'ón' : 'ones') + ' en la última capa</b>.' });
      return P; });
  } };
  M.atomo_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var Z = R(1, 20), x = EL[Z - 1], A = x[2], q = pick([0, 0, 1, -1, 2]); if (Z < 3) q = 0; var e = Z - q;
      return { cons: 'El ' + (q ? 'ion ' : 'átomo de ') + x[1].toLowerCase() + ' <b>' + x[0] + (q ? (Math.abs(q) > 1 ? Math.abs(q) : '') + (q > 0 ? '+' : '−') : '') + '</b> tiene Z = ' + Z + ' y A = ' + A + '. ¿Cuántos protones, neutrones y electrones tiene?', campos: [{ lab: 'Protones', v: Z }, { lab: 'Neutrones', v: A - Z }, { lab: 'Electrones', v: e }], ayuda: 'Protones = Z; neutrones = A − Z; electrones = Z menos la carga.', bien: '¡Bien! ' + Z + ' p⁺, ' + (A - Z) + ' n, ' + e + ' e⁻.' }; });
  } };

  // 5) TABLA PERIÓDICA (los primeros 20): período, grupo, electrones de valencia y tendencias
  var GR = [1, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2], PE = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4];
  function tipoEl(z) { return GR[z - 1] === 18 ? 'gas noble' : [1, 6, 7, 8, 9, 15, 16, 17].indexOf(z) >= 0 ? 'no metal' : z === 5 || z === 14 ? 'metaloide' : 'metal'; }
  var TCOL = { 'metal': '#FFE0B2', 'no metal': '#C8E6C9', 'gas noble': '#E1BEE7', 'metaloide': '#FFF9C4' };
  function colX(g) { return 14 + (g <= 2 ? g - 1 : g - 11) * 56; }
  function tabla(z, modo, tap) { var b = '';
    EL.forEach(function (x, i) { var zz = i + 1, X = colX(GR[i]), Y = 20 + (PE[i] - 1) * 50, on = zz === z, hl = modo === 'per' ? PE[i] === PE[z - 1] : modo === 'gru' ? GR[i] === GR[z - 1] : false;
      b += (tap ? '<g data-t="' + zz + '" class="nat-tap">' : '') + rc(X, Y, 48, 46, modo === 'tipo' ? TCOL[tipoEl(zz)] : hl ? '#FFF3C4' : '#fff', on ? C.coral : C.gris, 6, on ? ' stroke-width="3"' : '') + tx(X + 24, Y + 28, x[0], { a: 'middle', s: 16, w: 900 }) + tx(X + 5, Y + 12, zz, { s: 9 }) + (tap ? '</g>' : ''); });
    [1, 2, 13, 14, 15, 16, 17, 18].forEach(function (g) { b += tx(colX(g) + 24, 12, g, { a: 'middle', s: 9, c: C.teal, w: 800 }); });
    return S(470, 225, b); }
  M.tabla_periodica = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('z', 'Elemento', EL.map(function (x, i) { return [i + 1, x[0] + ' · ' + x[1]]; }), p.z || 16), function (o) { var z = +(o.z || 16), x = EL[z - 1], g = GR[z - 1], pe = PE[z - 1], val = g <= 2 ? g : g - 10, P = [];
      P.push({ vis: tabla(z), txt: 'Buscamos el <b>' + x[1].toLowerCase() + '</b> (Z = ' + z + '): los elementos están ordenados por su número atómico.' });
      P.push({ vis: tabla(z, 'per'), txt: 'Está en el <b>período ' + pe + '</b> (fila): sus electrones ocupan ' + pe + ' capa' + (pe > 1 ? 's' : '') + '.' });
      P.push({ vis: tabla(z, 'gru'), txt: 'Está en el <b>grupo ' + g + '</b> (columna): ' + (z === 2 ? 'el helio tiene 2 electrones de valencia y su capa está completa.' : 'tiene <b>' + val + ' electrones de valencia</b>, como todos los de su grupo; por eso se parecen químicamente.') });
      P.push({ vis: tabla(z, 'tipo') + S(470, 30, ['metal', 'no metal', 'metaloide', 'gas noble'].map(function (t, i) { return rc(20 + i * 112, 6, 14, 14, TCOL[t], C.gris, 3) + tx(40 + i * 112, 18, t, { s: 11, w: 800 }); }).join('')), txt: 'Es un <b>' + tipoEl(z) + '</b>. Los metales están a la izquierda; los no metales, arriba a la derecha; los gases nobles, en la última columna.' });
      P.push({ vis: tabla(z) + S(470, 70, fl(60, 20, 60, 55, C.coral, 3) + fl(440, 55, 120, 55, C.coral, 3) + tx(70, 40, 'el radio crece hacia abajo y a la izquierda', { s: 11, w: 800, c: C.coral }) + fl(120, 20, 440, 20, C.azul, 3) + tx(280, 14, 'la electronegatividad crece hacia arriba y a la derecha', { a: 'middle', s: 11, w: 800, c: C.azul })), txt: 'Las <b>tendencias</b>: el tamaño del átomo y la tendencia a atraer electrones cambian con la posición en la tabla.' });
      return P; });
  } };
  M.tabla_periodica_x = { tipo: 'ejercicio', render: function (el, p, api) {
    tocar(el, api, function () { var z = R(1, 20), x = EL[z - 1], g = GR[z - 1], q = pick(['pg', 'val']); if (z === 2) q = 'pg';
      var cons = q === 'pg' ? 'Tocá el elemento del <b>período ' + PE[z - 1] + '</b> y el <b>grupo ' + g + '</b>.' : 'Tocá el elemento del <b>período ' + PE[z - 1] + '</b> que tiene <b>' + (g <= 2 ? g : g - 10) + ' electrones de valencia</b>.';
      return { cons: cons, svg: tabla(0, null, true), ok: z, ayuda: 'El período es la fila; el grupo, la columna (los electrones de valencia salen del grupo).', bien: '¡Bien! Es el ' + x[1].toLowerCase() + ' (' + x[0] + ').' }; });
  } };

  // 6) ENLACES: iónico (transferencia) y covalente (compartir) con puntos de Lewis
  var MOL = [['Cloruro de sodio (NaCl)', 'ionico', ['Na', 1], ['Cl', 7], 'El sodio (metal) le cede su electrón al cloro (no metal): quedan Na⁺ y Cl⁻, que se atraen.'],
    ['Agua (H₂O)', 'cov', 'O', 6, [['H', 1], ['H', 1]], 'El oxígeno comparte un par de electrones con cada hidrógeno: dos enlaces simples.'],
    ['Oxígeno (O₂)', 'cov', 'O', 6, [['O', 6, 2]], 'Los dos oxígenos comparten dos pares de electrones: un enlace doble.'],
    ['Dióxido de carbono (CO₂)', 'cov', 'C', 4, [['O', 6, 2], ['O', 6, 2]], 'El carbono forma un enlace doble con cada oxígeno.'],
    ['Metano (CH₄)', 'cov', 'C', 4, [['H', 1], ['H', 1], ['H', 1], ['H', 1]], 'El carbono comparte un par con cada uno de los 4 hidrógenos.']];
  function puntosL(x, y, n, evitar) { var s = '', pos = [[0, -1], [1, 0], [0, 1], [-1, 0]].filter(function (d) { return !evitar || !evitar.some(function (e) { return e[0] === d[0] && e[1] === d[1]; }); }), k = 0;
    for (var i = 0; i < n; i++) { var d = pos[k % pos.length], par = Math.floor(i / pos.length); var ox = d[0] * 24 + (d[1] ? (par ? 5 : -5) : 0), oy = d[1] * 24 + (d[0] ? (par ? 5 : -5) : 0); s += ci(x + ox, y + oy, 3, C.azul); k++; } return s; }
  function atomoL(x, y, sim, col) { return ci(x, y, 17, col || '#fff', C.osc) + tx(x, y + 6, sim, { a: 'middle', s: 16, w: 900 }); }
  M.enlace = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Sustancia', MOL.map(function (m, i) { return [i, m[0]]; }), 0), function (o) { var m = MOL[+(o.i || 0)], P = [];
      if (m[1] === 'ionico') { var a = m[2], b = m[3];
        P.push({ vis: S(470, 140, atomoL(150, 70, a[0], '#FFE0B2') + puntosL(150, 70, a[1]) + atomoL(320, 70, b[0], '#C8E6C9') + puntosL(320, 70, b[1])), txt: 'Electrones de valencia: ' + a[0] + ' tiene ' + a[1] + ' y ' + b[0] + ' tiene ' + b[1] + '. Los dos buscan completar 8 (regla del octeto).' });
        P.push({ vis: S(470, 140, atomoL(150, 70, a[0], '#FFE0B2') + atomoL(320, 70, b[0], '#C8E6C9') + puntosL(320, 70, b[1]) + '<path d="M170,50 C220,10 260,10 300,48" fill="none" stroke="' + C.coral + '" stroke-width="2.5" marker-end="url(#natfl)"/>' + ci(296, 47, 3.5, C.coral)), txt: 'El ' + a[0] + ' <b>cede</b> su electrón y el ' + b[0] + ' lo <b>recibe</b>.' });
        P.push({ vis: S(470, 140, atomoL(150, 70, a[0] + '⁺', '#FFE0B2') + atomoL(320, 70, b[0] + '⁻', '#C8E6C9') + puntosL(320, 70, 8) + tx(235, 76, '+  −  atracción', { a: 'middle', s: 12, w: 900, c: C.coral })), txt: m[4] + ' Es un <b>enlace iónico</b>.' });
        return P; }
      var cen = m[2], vc = m[3], L = m[4], n = L.length, dirs = n === 1 ? [[1, 0]] : n === 2 ? (cen === 'O' ? [[-1, 0.6], [1, 0.6]] : [[-1, 0], [1, 0]]) : [[0, -1], [1, 0], [0, 1], [-1, 0]], cx = 235, cy = 90, d = 70;
      var dib = function (fase) { var s = '';
        L.forEach(function (q, i) { var x = cx + dirs[i][0] * d, y = cy + dirs[i][1] * d * (n === 4 ? 1 : 1), ord = q[2] || 1;
          if (fase >= 1) for (var k = 0; k < ord; k++) { var off = (k - (ord - 1) / 2) * 7, nx = -dirs[i][1], ny = dirs[i][0]; s += ln(cx + dirs[i][0] * 18 + nx * off, cy + dirs[i][1] * 18 + ny * off, x - dirs[i][0] * 18 + nx * off, y - dirs[i][1] * 18 + ny * off, C.teal, 3); }
          s += atomoL(x, y, q[0], '#E3F2FD') + (fase === 0 ? puntosL(x, y, q[1]) : puntosL(x, y, Math.max(0, q[1] - ord), [[-dirs[i][0] > 0 ? 1 : -dirs[i][0] < 0 ? -1 : 0, -dirs[i][1] > 0 ? 1 : -dirs[i][1] < 0 ? -1 : 0]])); });
        var usados = L.reduce(function (a, q) { return a + (q[2] || 1); }, 0);
        s += atomoL(cx, cy, cen, '#FFF3C4') + (fase === 0 ? puntosL(cx, cy, vc) : puntosL(cx, cy, Math.max(0, vc - usados), dirs.slice(0, n).map(function (q) { return [q[0] > 0 ? 1 : q[0] < 0 ? -1 : 0, q[1] > 0 ? 1 : q[1] < 0 ? -1 : 0]; })));
        return S(470, 185, s); };
      P.push({ vis: dib(0), txt: 'Electrones de valencia: ' + cen + ' tiene ' + vc + (L.map(function (q) { return q[0]; }).indexOf('H') >= 0 ? ' y cada H tiene 1' : ' y cada O tiene 6') + '. Son no metales: ninguno quiere ceder electrones.' });
      P.push({ vis: dib(1), txt: 'Entonces los <b>comparten</b>: cada línea es un par de electrones compartido.' });
      P.push({ vis: dib(1), txt: m[5] + ' Es un <b>enlace covalente</b>. Así cada átomo completa su capa (8 electrones, o 2 el hidrógeno).' });
      return P; });
  } };
  var PARES = [['Na', 'Cl', 'Iónico'], ['K', 'Br', 'Iónico'], ['Mg', 'O', 'Iónico'], ['Ca', 'F', 'Iónico'], ['H', 'Cl', 'Covalente'], ['C', 'O', 'Covalente'], ['N', 'H', 'Covalente'], ['O', 'O', 'Covalente'], ['Cu', 'Cu', 'Metálico'], ['Fe', 'Fe', 'Metálico'], ['Al', 'Al', 'Metálico'], ['Na', 'Na', 'Metálico']];
  M.enlace_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = mezclar(PARES.slice()).slice(0, 6); return { tit: '¿Qué tipo de enlace se forma? (metal + no metal: iónico; no metal + no metal: covalente; metal + metal: metálico)', cajas: ['Iónico', 'Covalente', 'Metálico'], items: it.map(function (q, i) { return { v: 'p' + i, t: q[0] + ' + ' + q[1], c: ['Iónico', 'Covalente', 'Metálico'].indexOf(q[2]) }; }) }; }); otro(el);
  } };

  // 7) ECUACIÓN QUÍMICA: balancear contando átomos a cada lado (conservación de la masa)
  var ECU = [['Formación del agua', [['H₂', { H: 2 }], ['O₂', { O: 2 }]], [['H₂O', { H: 2, O: 1 }]], [2, 1, 2]], ['Combustión del metano', [['CH₄', { C: 1, H: 4 }], ['O₂', { O: 2 }]], [['CO₂', { C: 1, O: 2 }], ['H₂O', { H: 2, O: 1 }]], [1, 2, 1, 2]],
    ['Síntesis del amoníaco', [['N₂', { N: 2 }], ['H₂', { H: 2 }]], [['NH₃', { N: 1, H: 3 }]], [1, 3, 2]], ['Oxidación del hierro', [['Fe', { Fe: 1 }], ['O₂', { O: 2 }]], [['Fe₂O₃', { Fe: 2, O: 3 }]], [4, 3, 2]], ['Combustión del propano', [['C₃H₈', { C: 3, H: 8 }], ['O₂', { O: 2 }]], [['CO₂', { C: 1, O: 2 }], ['H₂O', { H: 2, O: 1 }]], [1, 5, 3, 4]]];
  function cuentaAt(L, co) { var c = {}; L.forEach(function (q, i) { Object.keys(q[1]).forEach(function (a) { c[a] = (c[a] || 0) + q[1][a] * co[i]; }); }); return c; }
  function dibEc(e, co) { var re = e[1], pr = e[2], cr = co.slice(0, re.length), cp = co.slice(re.length), A = cuentaAt(re, cr), Bq = cuentaAt(pr, cp), at = Object.keys(A), s = '';
    var str = re.map(function (q, i) { return (cr[i] > 1 ? cr[i] + ' ' : '') + q[0]; }).join(' + ') + '  →  ' + pr.map(function (q, i) { return (cp[i] > 1 ? cp[i] + ' ' : '') + q[0]; }).join(' + ');
    s += tx(235, 30, str, { a: 'middle', s: 20, w: 900 });
    at.forEach(function (a, i) { var y = 60 + i * 28, ok = A[a] === Bq[a]; s += tx(60, y + 14, a, { a: 'middle', s: 14, w: 900 }) + rc(80, y, A[a] * 12, 18, ok ? '#C8E6C9' : '#FFCDD2', null, 4) + tx(84 + A[a] * 12, y + 14, A[a], { s: 12, w: 800 }) + rc(270, y, Bq[a] * 12, 18, ok ? '#C8E6C9' : '#FFCDD2', null, 4) + tx(274 + Bq[a] * 12, y + 14, Bq[a], { s: 12, w: 800 }) + tx(255, y + 14, ok ? '=' : '≠', { a: 'middle', s: 14, w: 900, c: ok ? C.verde : C.rosa }); });
    s += tx(140, 56, 'reactivos', { a: 'middle', s: 10.5, c: C.teal, w: 800 }) + tx(330, 56, 'productos', { a: 'middle', s: 10.5, c: C.teal, w: 800 });
    return S(470, 70 + at.length * 28, s); }
  M.ecuacion_quimica = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Reacción', ECU.map(function (e, i) { return [i, e[0]]; }), 0), function (o) { var e = ECU[+(o.i || 0)], n = e[3].length, co = e[3].map(function () { return 1; }), P = [];
      P.push({ vis: dibEc(e, co), txt: 'Escribimos la ecuación sin coeficientes y <b>contamos los átomos</b> de cada elemento a cada lado.' });
      var orden = []; for (var i = n - 1; i >= 0; i--) orden.push(i); orden.sort(function (a, b) { return Object.keys((a < e[1].length ? e[1][a] : e[2][a - e[1].length])[1]).length - Object.keys((b < e[1].length ? e[1][b] : e[2][b - e[1].length])[1]).length; }).reverse();
      orden.forEach(function (k) { if (e[3][k] === 1) return; co = co.slice(); co[k] = e[3][k]; var f = k < e[1].length ? e[1][k][0] : e[2][k - e[1].length][0]; P.push({ vis: dibEc(e, co), txt: 'Ponemos un <b>' + e[3][k] + '</b> delante de ' + f + ' (nunca se cambian los subíndices de la fórmula).' }); });
      P.push({ vis: dibEc(e, e[3]), txt: 'Quedó <b>balanceada</b>: hay la misma cantidad de cada átomo a los dos lados. La masa se conserva (ley de Lavoisier).' });
      return P; });
  } };
  M.ecuacion_quimica_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var e = ECU[rot(ECU.length, u)], fs = e[1].concat(e[2]).map(function (q) { return q[0]; });
      return { cons: 'Balanceá: <b>' + e[1].map(function (q) { return '__ ' + q[0]; }).join(' + ') + ' → ' + e[2].map(function (q) { return '__ ' + q[0]; }).join(' + ') + '</b> (usá los números enteros más chicos; si es 1, escribí 1).', campos: fs.map(function (f, i) { return { lab: f, v: e[3][i] }; }), ayuda: 'Contá cada elemento a los dos lados y empezá por el que aparece en menos fórmulas.', bien: '¡Bien! ' + fs.map(function (f, i) { return e[3][i] + ' ' + f; }).join(', ') + '.' }; });
  } };

  // 8) pH: la escala de colores con sustancias de la casa
  var PHS = [['Jugo gástrico', 1.5], ['Limón', 2], ['Vinagre', 3], ['Gaseosa', 3.5], ['Café', 5], ['Agua pura', 7], ['Sangre', 7.4], ['Bicarbonato', 8.5], ['Jabón', 10], ['Lavandina', 12.5], ['Soda cáustica', 14]];
  var PCOL = ['#d7191c', '#e8432d', '#f46d43', '#fd9e5c', '#fdc875', '#fee99a', '#ffffbf', '#e1f3a0', '#b7e18b', '#83cc82', '#52b36f', '#2f9a6e', '#2b7f8e', '#3a5fa8', '#5e3c99'];
  function escalaPH(v, marcas) { var s = ''; for (var i = 0; i <= 14; i++) s += rc(20 + i * 29, 70, 29, 36, PCOL[i]) + tx(34.5 + i * 29, 122, i, { a: 'middle', s: 11, w: 800 });
    (marcas || []).forEach(function (m, k) { var x = 20 + (m[1] + 0.5) * 29; s += ln(x, 66, x, 60 - (k % 4) * 13, C.osc, 1) + tx(x, 57 - (k % 4) * 13, m[0], { a: m[1] >= 12.5 ? 'end' : m[1] <= 1.5 ? 'start' : 'middle', s: 9.5, w: 800 }); });
    if (v != null) { var x = 20 + (v + 0.5) * 29; s += '<path d="M' + r1(x) + ',110 l-8,16 l16,0 z" fill="' + C.osc + '"/>' + tx(Math.min(430, Math.max(40, x)), 146, 'pH ' + fmt(v), { a: 'middle', s: 13, w: 900, c: C.coral }); }
    s += tx(60, 168, 'ÁCIDO', { a: 'middle', s: 12, w: 900, c: '#d7191c' }) + tx(235, 168, 'NEUTRO', { a: 'middle', s: 12, w: 900 }) + tx(410, 168, 'BÁSICO', { a: 'middle', s: 12, w: 900, c: '#3a5fa8' });
    return S(470, 178, s); }
  M.ph = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Sustancia', PHS.map(function (q, i) { return [i, q[0]]; }), 1), function (o) { var q = PHS[+(o.i || 0)], v = q[1], P = [], tipo = v < 7 ? 'ácida' : v > 7 ? 'básica (alcalina)' : 'neutra', veces = Math.round(Math.pow(10, Math.abs(7 - v)));
      P.push({ vis: escalaPH(null), txt: 'La <b>escala de pH</b> va de 0 a 14. El indicador universal toma un color distinto para cada valor.' });
      P.push({ vis: escalaPH(v), txt: 'El ' + q[0].toLowerCase() + ' tiene pH ' + fmt(v) + ': es una sustancia <b>' + tipo + '</b>.' });
      P.push({ vis: escalaPH(v), txt: v === 7 ? 'Neutra: ni ácida ni básica.' : 'Cada punto de la escala es 10 veces más: pH ' + fmt(v) + ' es unas <b>' + fmt(veces) + ' veces más ' + (v < 7 ? 'ácido' : 'básico') + '</b> que el agua pura.' });
      P.push({ vis: escalaPH(null, PHS), txt: 'Sustancias de todos los días. Al mezclar un ácido con una base se <b>neutralizan</b>: por eso el bicarbonato calma la acidez del estómago.' });
      return P; });
  } };
  M.ph_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = mezclar(PHS.slice()).slice(0, 6); return { tit: 'Clasificá cada sustancia según su pH.', cajas: ['Ácida (pH < 7)', 'Neutra (pH 7)', 'Básica (pH > 7)'], items: it.map(function (q, i) { return { v: 'h' + i, t: q[0] + ' (pH ' + fmt(q[1]) + ')', c: q[1] < 7 ? 0 : q[1] > 7 ? 1 + 1 : 1 }; }) }; }); otro(el);
  } };

  // 9) GASES: el pistón (Boyle, Charles y Gay-Lussac)
  function piston(V, P, T, sem) { var h = 30 + V / 10 * 110, y = 170 - h, s = rc(150, 20, 120, 152, 'none', C.osc, 4, ' stroke-width="3"') + rc(152, y, 116, h, '#EAF6FB') + rc(146, y - 12, 128, 12, '#9E9E9E', C.osc, 3) + ln(210, y - 12, 210, 10, C.osc, 4);
    var n = 14; for (var i = 0; i < n; i++) { var px = 160 + ((i * 37 + sem * 7) % 100), py = y + 8 + ((i * 29 + sem * 5) % Math.max(10, h - 16)); s += ci(px, py, 4, C.azul); }
    s += ci(360, 70, 34, '#fff', C.osc) + ln(360, 70, 360 + 26 * Math.cos(Math.PI * (1.2 - P / 5)), 70 - 26 * Math.sin(Math.PI * (1.2 - P / 5)), C.coral, 3) + tx(360, 122, fmt(P) + ' atm', { a: 'middle', s: 12, w: 900 }) + tx(70, 80, fmt(T) + ' K', { a: 'middle', s: 14, w: 900, c: C.coral }) + tx(70, 100, '(' + fmt(T - 273) + ' °C)', { a: 'middle', s: 11 }) + tx(210, 190, fmt(V) + ' L', { a: 'middle', s: 13, w: 900 });
    return S(470, 200, s); }
  M.gases = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('l', 'Ley', [['boyle', 'Boyle: T constante'], ['charles', 'Charles: P constante'], ['gay', 'Gay-Lussac: V constante']], p.ley || 'boyle') + ctrl('f', 'Cambiamos la variable por ×', 0.5, 3, 0.5, 2), function (o) { var l = o.l || 'boyle', f = o.f || 2, V1 = 4, P1 = 1, T1 = 300, V2 = V1, P2 = P1, T2 = T1, Pp = [];
      if (l === 'boyle') { V2 = r2(V1 / f); P2 = r2(P1 * f); } else if (l === 'charles') { T2 = Math.round(T1 * f); V2 = r2(V1 * f); } else { T2 = Math.round(T1 * f); P2 = r2(P1 * f); }
      var ley = { boyle: ['P₁ · V₁ = P₂ · V₂', 'Si la presión se multiplica, el volumen se divide: son inversamente proporcionales.', 'presión'], charles: ['V₁ / T₁ = V₂ / T₂', 'Si la temperatura (en kelvin) aumenta, el volumen aumenta en la misma proporción.', 'temperatura'], gay: ['P₁ / T₁ = P₂ / T₂', 'Si la temperatura (en kelvin) aumenta, la presión aumenta en la misma proporción.', 'temperatura'] }[l];
      Pp.push({ vis: piston(V1, P1, T1, 1), txt: 'Estado inicial: ' + V1 + ' L, ' + P1 + ' atm y ' + T1 + ' K. Las partículas chocan contra las paredes: eso es la presión.' });
      Pp.push({ vis: piston(V2, P2, T2, 2), txt: 'Multiplicamos la ' + ley[2] + ' por ' + fmt(f) + (l === 'boyle' ? ' (con la temperatura fija).' : l === 'charles' ? ' (con la presión fija).' : ' (con el volumen fijo).') });
      Pp.push({ vis: S(470, 80, tx(235, 34, ley[0], { a: 'middle', s: 20, w: 900 }) + tx(235, 64, l === 'boyle' ? P1 + ' · ' + V1 + ' = ' + fmt(P2) + ' · V₂ → V₂ = ' + fmt(V2) + ' L' : l === 'charles' ? V1 + ' / ' + T1 + ' = V₂ / ' + T2 + ' → V₂ = ' + fmt(V2) + ' L' : P1 + ' / ' + T1 + ' = P₂ / ' + T2 + ' → P₂ = ' + fmt(P2) + ' atm', { a: 'middle', s: 14, w: 800, c: C.teal })), txt: ley[1] });
      Pp.push({ vis: piston(V2, P2, T2, 3), txt: l === 'boyle' ? 'Al achicar el volumen, las partículas chocan más seguido contra las paredes: más presión.' : 'Más temperatura: las partículas se mueven más rápido y chocan con más fuerza.' });
      return Pp; });
  } };
  M.gases_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var k = rot(3, u);
      if (k === 0) { var P1 = pick([1, 2, 3]), V1 = pick([6, 12, 24]), P2 = pick([2, 4, 6].filter(function (x) { return x !== P1; })), V2 = r2(P1 * V1 / P2); return { cons: 'Un gas ocupa <b>' + V1 + ' L</b> a <b>' + P1 + ' atm</b>. Si la temperatura no cambia y la presión pasa a <b>' + P2 + ' atm</b>, ¿qué volumen ocupa?', campos: [{ lab: 'V₂', v: V2, un: 'L', tol: 0.01 }], ayuda: 'Ley de Boyle: P₁ · V₁ = P₂ · V₂.', bien: '¡Bien! V₂ = ' + P1 + ' · ' + V1 + ' ÷ ' + P2 + ' = ' + fmt(V2) + ' L.' }; }
      var T1 = pick([200, 250, 300, 400]), f = pick([1.5, 2, 3]), T2 = T1 * f, V = pick([2, 4, 5, 10]);
      if (k === 1) return { cons: 'Un globo tiene <b>' + V + ' L</b> a <b>' + T1 + ' K</b>. A presión constante se calienta hasta <b>' + T2 + ' K</b>. ¿Cuál es su nuevo volumen?', campos: [{ lab: 'V₂', v: r2(V * f), un: 'L', tol: 0.01 }], ayuda: 'Ley de Charles: V₁ / T₁ = V₂ / T₂.', bien: '¡Bien! V₂ = ' + fmt(r2(V * f)) + ' L.' };
      return { cons: 'Un gas en un recipiente rígido está a <b>' + V / 2 + ' atm</b> y <b>' + T1 + ' K</b>. Si se calienta hasta <b>' + T2 + ' K</b>, ¿cuál es la nueva presión?', campos: [{ lab: 'P₂', v: r2(V / 2 * f), un: 'atm', tol: 0.01 }], ayuda: 'Ley de Gay-Lussac: P₁ / T₁ = P₂ / T₂.', bien: '¡Bien! P₂ = ' + fmt(r2(V / 2 * f)) + ' atm.' }; });
  } };

  // 10) MOLÉCULAS DE CARBONO: armar la cadena, completar hidrógenos y nombrar
  var PREF = ['', 'met', 'et', 'prop', 'but', 'pent', 'hex'];
  function nombreC(n, t, g) { var base = PREF[n], suf = t === 'eno' ? 'eno' : t === 'ino' ? 'ino' : 'ano';
    if (g === 'oh') return base + (t === 'ano' ? 'anol' : t === 'eno' ? 'enol' : 'inol'); if (g === 'cooh') return 'ácido ' + base + (t === 'ano' ? 'anoico' : t === 'eno' ? 'enoico' : 'inoico'); return base + suf; }
  function hidC(n, t, g) { var h = 2 * n + 2 - (t === 'eno' ? 2 : t === 'ino' ? 4 : 0); return g === 'cooh' ? h - 2 : h; }
  function formula(n, t, g) { var h = hidC(n, t, g); if (g === 'oh') return 'C' + sub(n) + 'H' + sub(h - 1) + 'OH'; if (g === 'cooh') return 'C' + sub(n - 1) + 'H' + sub(h - 1) + 'COOH'; return 'C' + sub(n) + 'H' + sub(h); }
  function sub(k) { return k === 1 ? '' : String(k).split('').map(function (d) { return '₀₁₂₃₄₅₆₇₈₉'[d]; }).join(''); }
  function cadena(n, t, g, fase) { var s = '', x0 = 235 - (n - 1) * 34, y = 100;
    for (var i = 0; i < n; i++) { var x = x0 + i * 68; if (i < n - 1) { var o = i === 0 && t !== 'ano' ? (t === 'eno' ? 2 : 3) : 1; for (var k = 0; k < o; k++) s += ln(x + 15, y + (k - (o - 1) / 2) * 7, x + 53, y + (k - (o - 1) / 2) * 7, C.osc, 2.5); } }
    for (i = 0; i < n; i++) { x = x0 + i * 68; var usado = (i > 0 ? (i === 1 && t !== 'ano' ? (t === 'eno' ? 2 : 3) : 1) : 0) + (i < n - 1 ? (i === 0 && t !== 'ano' ? (t === 'eno' ? 2 : 3) : 1) : 0), libres = 4 - usado, ult = i === n - 1;
      if (fase >= 1) { var dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]].filter(function (d) { return !(d[0] === -1 && i > 0) && !(d[0] === 1 && i < n - 1); }), hs = libres;
        if (ult && g === 'oh') { s += ln(x, y - 15, x, y - 38, C.osc, 2.5) + tx(x, y - 44, 'OH', { a: 'middle', s: 13, w: 900, c: C.rosa }); dirs = dirs.filter(function (d) { return !(d[1] === -1); }); hs--; }
        if (ult && g === 'cooh') { s += ln(x - 4, y - 15, x - 4, y - 38, C.osc, 2.5) + ln(x + 4, y - 15, x + 4, y - 38, C.osc, 2.5) + tx(x, y - 44, 'O', { a: 'middle', s: 13, w: 900, c: C.rosa }) + ln(x + 15, y, x + 38, y, C.osc, 2.5) + tx(x + 52, y + 5, 'OH', { a: 'middle', s: 13, w: 900, c: C.rosa }); dirs = dirs.filter(function (d) { return d[1] !== -1 && d[0] !== 1; }); hs -= 3; }
        for (var j = 0; j < hs && j < dirs.length; j++) { var d = dirs[j]; s += ln(x + d[0] * 15, y + d[1] * 15, x + d[0] * 34, y + d[1] * 34, C.gris, 2) + tx(x + d[0] * 44, y + d[1] * 44 + 5, 'H', { a: 'middle', s: 13, w: 800 }); } }
      s += ci(x, y, 15, '#455A64') + tx(x, y + 5, 'C', { a: 'middle', s: 14, w: 900, c: '#fff' }); }
    return S(470, 200, s); }
  M.carbono = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('n', 'Carbonos en la cadena', 1, 6, 1, 3) + sel('t', 'Enlace entre C1 y C2', [['ano', 'simple (alcano)'], ['eno', 'doble (alqueno)'], ['ino', 'triple (alquino)']], 'ano') + sel('g', 'Grupo funcional', [['', 'ninguno (hidrocarburo)'], ['oh', '−OH (alcohol)'], ['cooh', '−COOH (ácido)']], ''), function (o) { var n = o.n || 3, t = o.t || 'ano', g = o.g || '', P = []; if (n === 1) t = 'ano';
      P.push({ vis: cadena(n, t, g, 0), txt: 'El carbono forma <b>4 enlaces</b> y puede unirse a otros carbonos en cadena. Esta tiene ' + n + ' carbono' + (n > 1 ? 's' : '') + (n > 1 && t !== 'ano' ? ' con un enlace ' + (t === 'eno' ? 'doble' : 'triple') : '') + '.' });
      P.push({ vis: cadena(n, t, g, 1), txt: 'Completamos con hidrógenos hasta que cada carbono tenga 4 enlaces' + (g ? ' y agregamos el grupo funcional, que le da propiedades nuevas' : '') + '.' });
      P.push({ vis: cadena(n, t, g, 1) + nota('Fórmula: ' + formula(n, t, g)), txt: 'Contamos: la fórmula molecular es <b>' + formula(n, t, g) + '</b>.' });
      P.push({ vis: cadena(n, t, g, 1) + nota(nombreC(n, t, g)), txt: 'Nombre: el prefijo dice cuántos carbonos (<b>' + PREF[n] + '-</b> = ' + n + ') y la terminación, el tipo: <b>' + nombreC(n, t, g) + '</b>.' });
      return P; });
  } };
  M.carbono_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var n = R(1, 6), t = n === 1 ? 'ano' : pick(['ano', 'ano', 'eno', 'ino']), g = pick(['', '', 'oh']), nm = nombreC(n, t, g);
      return { cons: '¿Cómo se llama este compuesto? (prefijos: met-, et-, prop-, but-, pent-, hex-)', html: cadena(n, t, g, 1), campos: [{ tipo: 'texto', lab: 'Nombre', v: [nm] }], ayuda: 'Contá los carbonos para el prefijo; el enlace da -ano, -eno o -ino; si tiene −OH termina en -ol.', bien: '¡Bien! Es el ' + nm + ' (' + formula(n, t, g) + ').' }; });
  } };

  // 11) RADIACTIVIDAD: semivida con una grilla de átomos que se desintegran
  var ISO = [['Carbono-14', 5730, 'años'], ['Yodo-131', 8, 'días'], ['Cobalto-60', 5.3, 'años'], ['Uranio-238', 4500, 'millones de años']];
  function grilla(vivos) { var s = ''; for (var i = 0; i < 100; i++) s += rc(80 + (i % 10) * 31, 10 + Math.floor(i / 10) * 19, 26, 15, i < vivos ? C.sol : '#E0E0E0', null, 4); return S(470, 205, s); }
  M.radiactividad = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Isótopo', ISO.map(function (q, i) { return [i, q[0]]; }), 0) + ctrl('n', 'Semividas que pasan', 1, 5, 1, 4), function (o) { var q = ISO[+(o.i || 0)], n = o.n || 4, P = [{ vis: grilla(100), txt: 'Empezamos con 100 átomos de <b>' + q[0].toLowerCase() + '</b> (amarillos). Su <b>semivida</b> es de ' + fmt(q[1]) + ' ' + q[2] + '.' }];
      for (var k = 1; k <= n; k++) { var v = Math.round(100 / Math.pow(2, k)); P.push({ vis: grilla(v), txt: 'Pasaron ' + k + ' semivida' + (k > 1 ? 's' : '') + ' (' + fmt(r2(q[1] * k)) + ' ' + q[2] + '): queda la mitad de lo que había → <b>' + fmt(100 / Math.pow(2, k)) + '</b> átomos.' }); }
      P.push({ vis: grilla(Math.round(100 / Math.pow(2, n))), txt: 'Nunca se sabe cuál átomo se desintegra, pero sí cuántos: por eso el carbono-14 sirve para <b>datar</b> fósiles y restos antiguos.' });
      return P; });
  } };
  M.radiactividad_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var q = pick(ISO), m0 = pick([80, 160, 200, 400, 640]), k = R(1, 4), v = m0 / Math.pow(2, k);
      return { cons: 'Hay <b>' + m0 + ' g</b> de ' + q[0].toLowerCase() + ', cuya semivida es de ' + fmt(q[1]) + ' ' + q[2] + '. ¿Cuántos gramos quedan después de <b>' + fmt(r2(q[1] * k)) + ' ' + q[2] + '</b>?', campos: [{ lab: 'Quedan', v: v, un: 'g', tol: 0.01 }], ayuda: 'Calculá cuántas semividas pasaron y dividí por 2 esa cantidad de veces.', bien: '¡Bien! ' + k + ' semividas: ' + m0 + ' → ' + fmt(v) + ' g.' }; });
  } };

  // 12) INSTRUMENTOS: leer un termómetro, una probeta, una regla o una balanza
  function instrumento(t, v, fase) { var s = '';
    if (t === 'termometro') { var y0 = 190, esc = 1.4; s += rc(220, 20, 30, 175, '#fff', C.osc, 14) + ci(235, 200, 16, C.coral, C.osc); for (var g = 0; g <= 120; g += 2) { var y = y0 - g * esc; s += ln(250, y, g % 10 ? 258 : 266, y, C.osc, g % 10 ? 1 : 2) + (g % 10 === 0 && fase >= 1 ? tx(272, y + 4, g - 10, { s: 10 }) : ''); } s += rc(231, y0 - (v + 10) * esc, 8, (v + 10) * esc + 6, C.coral) + (fase >= 1 ? tx(300, 30, '°C', { s: 14, w: 900 }) : ''); }
    if (t === 'probeta') { s += '<path d="M200,20 L200,190 L270,190 L270,20" fill="#fff" stroke="' + C.osc + '" stroke-width="2.5"/>'; var yb = 185, e2 = 1.6; s += rc(202, yb - v * e2, 66, v * e2 + 3, '#BBDEFB'); for (g = 0; g <= 100; g += 2) { y = yb - g * e2; s += ln(200, y, g % 10 ? 210 : 218, y, C.osc, g % 10 ? 1 : 2) + (g % 10 === 0 && fase >= 1 ? tx(190, y + 4, g, { a: 'end', s: 10 }) : ''); } s += (fase >= 1 ? tx(290, 30, 'mL', { s: 14, w: 900 }) : '') + '<path d="M202,' + r1(yb - v * e2) + ' q33,8 66,0" fill="none" stroke="' + C.azul + '" stroke-width="2"/>'; }
    if (t === 'regla') { s += rc(40, 100, 400, 40, '#FFF9C4', C.osc, 4); for (g = 0; g <= 100; g++) { var x = 50 + g * 3.8; s += ln(x, 100, x, g % 10 ? (g % 5 ? 108 : 113) : 120, C.osc, g % 10 ? 1 : 2) + (g % 10 === 0 && fase >= 1 ? tx(x, 133, g / 10, { a: 'middle', s: 10 }) : ''); } s += rc(50, 70, v * 3.8, 22, C.verde, null, 6) + (fase >= 1 ? tx(430, 160, 'cm', { s: 13, w: 900 }) : ''); }
    if (t === 'balanza') { s += '<path d="M120,180 L350,180 L330,150 L140,150 Z" fill="#CFD8DC" stroke="' + C.osc + '" stroke-width="2"/>' + ci(235, 95, 60, '#fff', C.osc); for (g = 0; g <= 1000; g += 50) { var a = Math.PI * (1.25 - g / 1000 * 1.5); s += ln(235 + 52 * Math.cos(a), 95 - 52 * Math.sin(a), 235 + (g % 100 ? 47 : 43) * Math.cos(a), 95 - (g % 100 ? 47 : 43) * Math.sin(a), C.osc, g % 100 ? 1 : 2) + (g % 200 === 0 && fase >= 1 ? tx(235 + 33 * Math.cos(a), 99 - 33 * Math.sin(a), g, { a: 'middle', s: 8.5 }) : ''); } a = Math.PI * (1.25 - v / 1000 * 1.5); s += ln(235, 95, 235 + 45 * Math.cos(a), 95 - 45 * Math.sin(a), C.coral, 3) + (fase >= 1 ? tx(235, 140, 'g', { a: 'middle', s: 12, w: 900 }) : ''); }
    return S(470, 210, s); }
  var INS = { termometro: ['Termómetro', 'temperatura', '°C', 1, 'cada rayita vale 2 °C', 2, function () { return R(0, 55) * 2; }], probeta: ['Probeta', 'volumen de un líquido', 'mL', 1, 'cada rayita vale 2 mL (se lee en la parte baja de la curva)', 2, function () { return R(5, 48) * 2; }], regla: ['Regla', 'longitud', 'cm', 1, 'cada rayita vale 1 mm = 0,1 cm', 0.1, function () { return R(10, 100); }], balanza: ['Balanza de aguja', 'masa', 'g', 1, 'cada rayita vale 50 g', 50, function () { return R(1, 19) * 50; }] };
  function lectura(t, v) { return t === 'regla' ? v / 10 : v; }
  M.instrumento = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = p.instrumentos || Object.keys(INS);
    escena(el, sel('t', 'Instrumento', L.map(function (k) { return [k, INS[k][0]]; }), L[0]) + ctrl('v', 'Valor', 0, 100, 1, 46), function (o) { var t = o.t || L[0], I = INS[t], v = t === 'balanza' ? Math.round((o.v || 46) / 5) * 50 : t === 'termometro' || t === 'probeta' ? Math.round((o.v || 46) / 2) * 2 : Math.max(1, o.v || 46), lec = lectura(t, v);
      return [{ vis: instrumento(t, v, 0), txt: 'El <b>' + I[0].toLowerCase() + '</b> mide ' + I[1] + '.' }, { vis: instrumento(t, v, 1), txt: 'Miramos la escala y la <b>unidad</b> (' + I[2] + '). La <b>apreciación</b> es lo que vale la menor división: ' + I[4] + '.' }, { vis: instrumento(t, v, 1) + nota('Lectura: ' + fmt(lec) + ' ' + I[2] + ' ± ' + fmt(I[5] / 2) + ' ' + I[2]), txt: 'Leemos de frente, a la altura de los ojos: <b>' + fmt(lec) + ' ' + I[2] + '</b>. Toda medición tiene un margen de error.' }]; });
  } };
  M.instrumento_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = p.instrumentos || Object.keys(INS);
    respuesta(el, api, function () { var t = pick(L), I = INS[t], v = I[6](), lec = lectura(t, v);
      return { cons: '¿Qué indica este instrumento (' + I[0].toLowerCase() + ')?', html: instrumento(t, v, 1), campos: [{ lab: 'Lectura', v: lec, un: I[2], tol: I[5] / 2 + 1e-9 }], ayuda: 'Fijate cuánto vale cada rayita (' + I[4] + ') y contá desde el número marcado más cercano.', bien: '¡Bien! ' + fmt(lec) + ' ' + I[2] + '.' }; });
  } };

  // 13) TAMAÑOS: zoom en potencias de 10, de una persona a un átomo
  var TAM = [['Persona', 1.7, '🧍'], ['Huevo de gallina', 0.05, '🥚'], ['Hormiga', 0.004, '🐜'], ['Óvulo humano', 0.0001, '⚪'], ['Célula de la piel', 0.00003, '🔵'], ['Bacteria', 0.000002, '🦠'], ['Virus', 0.0000001, '🦠'], ['Proteína', 0.00000001, '🧶'], ['Átomo', 0.0000000001, '⚛️']];
  function unid(m) { return m >= 1 ? fmt(m) + ' m' : m >= 0.01 ? fmt(Math.round(m * 1000) / 10) + ' cm' : m >= 0.001 ? fmt(Math.round(m * 10000) / 10) + ' mm' : m >= 0.000001 ? fmt(Math.round(m * 1e7) / 10) + ' µm' : fmt(Math.round(m * 1e10) / 10) + ' nm'; }
  function eje(k) { var s = ln(30, 150, 440, 150, C.osc, 2); for (var e = 0; e >= -10; e--) { var x = 440 + e * 41; s += ln(x, 145, x, 155, C.osc, 2) + tx(x, 172, e ? '10' + '<tspan dy="-6" font-size="9">' + e + '</tspan>' : '1 m', { a: 'middle', s: 10.5 }); }
    TAM.forEach(function (t, j) { if (j > k) return; var x = 440 + Math.log10(t[1]) * 41, on = j === k; s += ln(x, 150, x, 118 - (j % 2) * 30, on ? C.coral : C.gris, on ? 2.5 : 1.2) + em(x, 108 - (j % 2) * 30, t[2], on ? 22 : 14); });
    if (k >= 0) s += tx(235, 30, TAM[k][0] + ': ' + unid(TAM[k][1]), { a: 'middle', s: 17, w: 900, c: C.coral }); return S(470, 185, s); }
  M.tamanos = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, '', function () { var P = [{ vis: eje(-1), txt: 'Una regla especial: cada rayita es <b>10 veces más chica</b> que la anterior (potencias de 10 en metros).' }];
      TAM.forEach(function (t, j) { P.push({ vis: eje(j), txt: '<b>' + t[0] + '</b>: ' + unid(t[1]) + (j === 3 ? ' (apenas visible a simple vista).' : j === 4 ? ': hace falta un microscopio óptico.' : j === 6 ? ': solo se ve con microscopio electrónico.' : '.') }); }); return P; });
  } };
  M.tamanos_x = { tipo: 'ejercicio', render: function (el, p, api) {
    ordenar(el, api, function () { var L = mezclar(TAM.slice()).slice(0, 4).sort(function (a, b) { return b[1] - a[1]; }); return { cons: 'Ordená del <b>más grande</b> al más chico.', items: L.map(function (t) { return t[2] + ' ' + t[0]; }), ayuda: 'Recordá: célula > bacteria > virus > átomo.', bien: '¡Bien! ' + L.map(function (t) { return t[0] + ' (' + unid(t[1]) + ')'; }).join(' > ') + '.' }; });
  } };

  // 14) GRÁFICO DE DATOS: se dibuja punto por punto y se interpreta (curva de calentamiento, temperatura en un día, crecimiento de plantas)
  var GRAF = [{ nombre: 'Calentamiento de hielo', x: 'tiempo (min)', y: 'temperatura (°C)', series: [{ n: 'agua', pts: [[0, -20], [2, -10], [4, 0], [6, 0], [8, 0], [10, 25], [12, 50], [14, 75], [16, 100], [18, 100], [20, 100]] }], marcas: [[6, 0, 'meseta: se funde (0 °C)'], [18, 100, 'meseta: hierve (100 °C)']], cierre: 'En las mesetas la temperatura no sube: el calor se usa para cambiar de estado.' },
    { nombre: 'Temperatura durante un día', x: 'hora', y: 'temperatura (°C)', series: [{ n: 'temperatura', pts: [[0, 12], [3, 10], [6, 9], [9, 15], [12, 22], [15, 25], [18, 20], [21, 15], [24, 12]] }], marcas: [[15, 25, 'máxima: 15 h'], [6, 9, 'mínima: 6 h']], cierre: 'La máxima llega después del mediodía y la mínima, cerca del amanecer.' },
    { nombre: 'Plantas con y sin luz', x: 'días', y: 'altura (cm)', series: [{ n: 'con luz', pts: [[0, 0], [5, 2], [10, 6], [15, 11], [20, 15]] }, { n: 'sin luz', pts: [[0, 0], [5, 2], [10, 3], [15, 3], [20, 3]] }], marcas: [[20, 15, 'con luz: 15 cm'], [20, 3, 'sin luz: se detiene']], cierre: 'Sin luz no hay fotosíntesis: la planta usa sus reservas y deja de crecer.' }];
  function graf(G, hasta, marcas) { var x0 = 55, y0 = 190, W = 380, Hh = 160, xs = [], ys = []; G.series.forEach(function (s) { s.pts.forEach(function (q) { xs.push(q[0]); ys.push(q[1]); }); });
    var xmx = Math.max.apply(null, xs), ymn = Math.min(0, Math.min.apply(null, ys)), ymx = Math.max.apply(null, ys), X = function (v) { return x0 + v / xmx * W; }, Y = function (v) { return y0 - (v - ymn) / (ymx - ymn) * Hh; };
    var s = ln(x0, y0, x0 + W, y0) + ln(x0, y0, x0, y0 - Hh - 6) + tx(x0 + W, y0 + 30, G.x, { a: 'end', s: 11 }) + tx(x0 + 4, y0 - Hh - 10, G.y, { s: 11 });
    [0, 0.5, 1].forEach(function (f) { var v = Math.round(ymn + f * (ymx - ymn)); s += ln(x0 - 4, Y(v), x0 + W, Y(v), '#eee', 1) + tx(x0 - 7, Y(v) + 4, v, { a: 'end', s: 10 }); });
    G.series[0].pts.forEach(function (q) { s += tx(X(q[0]), y0 + 14, q[0], { a: 'middle', s: 10 }); });
    G.series.forEach(function (se, k) { var pts = se.pts.slice(0, hasta), col = [C.teal, C.coral][k]; s += '<polyline points="' + pts.map(function (q) { return r1(X(q[0])) + ',' + r1(Y(q[1])); }).join(' ') + '" fill="none" stroke="' + col + '" stroke-width="3"/>' + pts.map(function (q) { return ci(X(q[0]), Y(q[1]), 3.5, col); }).join(''); if (G.series.length > 1) s += rc(330, 10 + k * 18, 12, 12, col, null, 3) + tx(348, 20 + k * 18, se.n, { s: 11, w: 800 }); });
    if (marcas) G.marcas.forEach(function (m) { s += ci(X(m[0]), Y(m[1]), 7, 'none', C.sol, ' stroke-width="3"') + tx(Math.min(X(m[0]), 380), Y(m[1]) - 12, m[2], { a: 'middle', s: 10.5, w: 800, c: C.sol }); });
    return S(470, 225, s); }
  M.grafico = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = p.items && p.items.length ? p.items : GRAF;
    escena(el, L.length > 1 ? sel('i', 'Gráfico', L.map(function (g, i) { return [i, g.nombre]; }), 0) : '', function (o) { var G = L[+(o.i || 0)] || L[0], n = G.series[0].pts.length, P = [{ vis: graf(G, 0), txt: 'Antes de mirar los datos, leemos los <b>ejes</b>: abajo, ' + G.x + '; a la izquierda, ' + G.y + '.' }];
      P.push({ vis: graf(G, Math.ceil(n / 2)), txt: 'Ubicamos los puntos: cada uno es un par de valores medidos.' }); P.push({ vis: graf(G, n), txt: 'Unimos los puntos: ahora se ve cómo cambia ' + G.y.replace(/ \(.*/, '') + ' a lo largo ' + (G.x.indexOf('tiempo') >= 0 || G.x === 'días' ? 'del tiempo' : 'del día') + '.' });
      P.push({ vis: graf(G, n, true), txt: 'Interpretamos: ' + G.cierre }); return P; });
  } };
  M.grafico_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = p.items && p.items.length ? p.items : GRAF;
    respuesta(el, api, function () { var G = pick(L), se = pick(G.series), q = pick(se.pts); return { cons: 'Leé el gráfico: ¿cuánto vale ' + G.y + (G.series.length > 1 ? ' (' + se.n + ')' : '') + ' cuando ' + G.x.replace(/ \(.*/, '') + ' = <b>' + q[0] + '</b>?', html: graf(G, 99), campos: [{ lab: 'Valor', v: q[1] }], ayuda: 'Subí desde el ' + q[0] + ' del eje horizontal hasta la línea y mirá a qué altura está.', bien: '¡Bien! ' + q[1] + '.' }; });
  } };

  // 15) EXPERIMENTO CONTROLADO: pregunta, hipótesis, variables, montaje, resultados y conclusión
  var EXP = [{ nombre: '¿La luz influye en el crecimiento de las plantas?', hip: 'Si una planta no recibe luz, crecerá menos.', ind: 'la luz', dep: 'la altura de la planta', ctl: 'la misma especie, maceta, tierra y agua', a: ['☀️🌱', 'con luz', 15], b: ['🌑🌱', 'sin luz', 3], u: 'cm', conc: 'La hipótesis se confirma: sin luz la planta casi no creció.' },
    { nombre: '¿El azúcar se disuelve más rápido en agua caliente?', hip: 'En agua caliente el azúcar se disuelve en menos tiempo.', ind: 'la temperatura del agua', dep: 'el tiempo que tarda en disolverse', ctl: 'la misma cantidad de agua y de azúcar, y revolver igual', a: ['🔥🥛', 'agua caliente', 20], b: ['🧊🥛', 'agua fría', 90], u: 's', conc: 'Se confirma: con más temperatura las partículas se mueven más y se disuelve más rápido.' },
    { nombre: '¿La levadura necesita azúcar para inflar un globo?', hip: 'Con azúcar, la levadura produce gas e infla el globo.', ind: 'el azúcar', dep: 'cuánto se infla el globo', ctl: 'la misma levadura, agua tibia, botella y globo', a: ['🍬🎈', 'con azúcar', 18], b: ['🚫🎈', 'sin azúcar', 2], u: 'cm', conc: 'Se confirma: la levadura usa el azúcar y libera dióxido de carbono.' }];
  function montaje(E, res) { var s = ''; [E.a, E.b].forEach(function (m, i) { var x = 120 + i * 230; s += rc(x - 85, 15, 170, 110, i ? '#F3FBF7' : '#FFF3C4', i ? C.teal : C.sol, 12) + em(x, 55, m[0], 34) + tx(x, 105, m[1], { a: 'middle', s: 13, w: 900 }) + tx(x, 140, i ? 'control (sin cambio)' : 'con la variable cambiada', { a: 'middle', s: 10.5, c: C.teal });
      if (res) { var mx = Math.max(E.a[2], E.b[2]); s += rc(x - 22, 230 - m[2] / mx * 70, 44, m[2] / mx * 70, i ? C.teal : C.sol, null, 4) + tx(x, 226 - m[2] / mx * 70, m[2] + ' ' + E.u, { a: 'middle', s: 12, w: 900 }); } });
    return S(470, res ? 240 : 150, s); }
  M.experimento = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = p.items && p.items.length ? p.items : EXP;
    escena(el, L.length > 1 ? sel('i', 'Experimento', L.map(function (e, i) { return [i, e.nombre]; }), 0) : '', function (o) { var E = L[+(o.i || 0)] || L[0];
      return [{ vis: '<p class="nat-card">❓ ' + E.nombre + '</p>', txt: 'Todo empieza con una <b>pregunta</b> que se pueda responder midiendo.' }, { vis: '<p class="nat-card">💡 ' + E.hip + '</p>', txt: 'La <b>hipótesis</b> es una respuesta posible, que el experimento va a poner a prueba.' },
        { vis: S(470, 120, rc(10, 10, 140, 90, '#FFF3C4', C.sol, 10) + txw(80, 40, 'Cambia:', { a: 'middle', s: 11, w: 900 }) + txw(80, 74, E.ind, { a: 'middle', s: 11 }, 18) + rc(165, 10, 140, 90, C.claro, C.teal, 10) + tx(235, 40, 'Se mide:', { a: 'middle', s: 11, w: 900 }) + txw(235, 74, E.dep, { a: 'middle', s: 11 }, 18) + rc(320, 10, 140, 90, '#F3E5F5', C.lila, 10) + tx(390, 40, 'Igual en todo:', { a: 'middle', s: 11, w: 900 }) + txw(390, 74, E.ctl.length > 36 ? E.ctl.slice(0, 34) + '…' : E.ctl, { a: 'middle', s: 10 }, 18)),
          txt: 'Variables: la <b>independiente</b> es la que cambiamos (' + E.ind + '); la <b>dependiente</b>, la que medimos (' + E.dep + '); las <b>controladas</b> quedan iguales (' + E.ctl + ').' },
        { vis: montaje(E, false), txt: 'Armamos <b>dos montajes</b> iguales en todo, salvo en la variable independiente. El de control sirve para comparar.' },
        { vis: montaje(E, true), txt: '<b>Resultados</b>: ' + E.a[1] + ', ' + E.a[2] + ' ' + E.u + '; ' + E.b[1] + ', ' + E.b[2] + ' ' + E.u + '.' }, { vis: montaje(E, true), txt: '<b>Conclusión</b>: ' + E.conc }]; });
  } };
  M.experimento_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = p.items && p.items.length ? p.items : EXP, u = { v: -1 }, uq = { v: -1 };
    elegir(el, api, function () { var E = L[rot(L.length, u)], q = rot(2, uq), ok = q ? E.dep : E.ind, ops = [E.ind, E.dep, E.ctl.split(',')[0]];
      return { cons: 'Experimento: <b>' + E.nombre + '</b> ¿Cuál es la variable <b>' + (q ? 'dependiente (la que se mide)' : 'independiente (la que se cambia)') + '</b>?', html: montaje(E, false), ops: ops, ok: ok, ayuda: 'La independiente es lo que el investigador cambia a propósito; la dependiente, lo que mide para ver el efecto.' }; });
  } };
  N.d = N.d || {}; N.d.aparato = aparato; N.d.MEZ = MEZ; N.d.instrumento = instrumento; N.d.INS = INS; N.d.bohr = bohr; N.d.EL = EL; N.d.tabla = tabla; N.d.PCOL = PCOL; N.d.vaso = vaso; N.d.LIQ = LIQ;
})();
