/* BANCO DE LA LECCIÓN · SOCIALES (Historia, Geografía, Ciudadanía, Filosofía, Economía, Ciencias Sociales de primaria y Aplicadas).
   Solo lección (separado del banco de actividades). Cada ejemplo con su formato visual propio y PASO A PASO; cada uno con su práctica.
   Usa las herramientas de dibujo comunes (H.nat, de js/leccion-banco-nat.js). */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h || !B._h.nat) return;
  var H = B._h, M = B.motores, R = H.R, pick = H.pick, mezclar = H.mezclar, fmt = H.fmt, N = H.nat;
  var escena = H.escena, ctrl = H.ctrl, respuesta = H.respuesta, cajas = H.cajas;
  var C = N.C, S = N.S, tx = N.tx, txw = N.txw, ln = N.ln, fl = N.fl, ci = N.ci, rc = N.rc, em = N.em, r1 = N.r1, sel = N.sel, otro = N.otro, rot = N.rot, nota = N.nota, elegir = N.elegir, ordenar = N.ordenar, tocar = N.tocar;
  function lineas(x, y, t, o, max) { var w = t.split(' '), L = [''], k = 0; w.forEach(function (q) { if ((L[k] + ' ' + q).trim().length > max && L[k]) L[++k] = q; else L[k] = (L[k] + ' ' + q).trim(); }); o = o || {}; return '<text x="' + x + '" y="' + r1(y - (L.length - 1) * 5.5) + '" text-anchor="' + (o.a || 'middle') + '" font-size="' + (o.s || 9) + '" font-weight="' + (o.w || 700) + '"' + (o.c ? ' fill="' + o.c + '"' : '') + '>' + L.map(function (l, i) { return '<tspan x="' + x + '"' + (i ? ' dy="1.2em"' : '') + '>' + l + '</tspan>'; }).join('') + '</text>'; }
  function card(t) { return '<p class="nat-card">' + t + '</p>'; }
  function romano(n) { var v = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']], s = ''; v.forEach(function (q) { while (n >= q[0]) { s += q[1]; n -= q[0]; } }); return s; }
  function anio(a) { return a < 0 ? (-a) + ' a. C.' : String(a); }
  function siglo(a) { return a < 0 ? romano(Math.ceil(-a / 100)) + ' a. C.' : romano(Math.ceil(a / 100)); }
  function entre(a, b) { return a < 0 && b > 0 ? b - a - 1 : b - a; }

  // 1) LÍNEA DE TIEMPO: siglos, antes y después de Cristo, años transcurridos
  var LINEAS = { antigua: [['Primeras ciudades en Mesopotamia', -3500, '🏛️'], ['Pirámides de Guiza', -2560, '🔺'], ['Democracia en Atenas', -508, '🗳️'], ['Fundación de Roma', -753, '🐺'], ['Caída del Imperio romano de Occidente', 476, '🏚️']],
    america: [['Llegada de Colón a América', 1492, '⛵'], ['Fundación de Buenos Aires (segunda)', 1580, '🏘️'], ['Revolución de Mayo', 1810, '🎗️'], ['Declaración de la Independencia', 1816, '📜'], ['Constitución Nacional', 1853, '⚖️']],
    contemporanea: [['Revolución Francesa', 1789, '🇫🇷'], ['Primera Guerra Mundial', 1914, '💥'], ['Crisis de 1929', 1929, '📉'], ['Segunda Guerra Mundial', 1939, '✈️'], ['Caída del Muro de Berlín', 1989, '🧱']] };
  function linea(L, hasta, marcaA, marcaB) { var mn = Math.min.apply(null, L.map(function (e) { return e[1]; })), mx = Math.max.apply(null, L.map(function (e) { return e[1]; })), pad = (mx - mn) * 0.08 + 10; mn -= pad; mx += pad;
    var X = function (a) { return 25 + (a - mn) / (mx - mn) * 420; }, s = ln(20, 130, 450, 130, C.osc, 3), paso = mx - mn > 2000 ? 1000 : mx - mn > 600 ? 100 : mx - mn > 150 ? 50 : 10;
    for (var a = Math.ceil(mn / paso) * paso; a <= mx; a += paso) { s += ln(X(a), 124, X(a), 136, C.osc, 1.5) + tx(X(a), 152, a === 0 ? '0' : anio(a), { a: 'middle', s: 9.5 }); }
    if (mn < 0 && mx > 0) s += ln(X(0), 100, X(0), 140, C.coral, 2) + tx(X(0), 96, 'nacimiento de Cristo', { a: 'middle', s: 9.5, c: C.coral, w: 800 });
    L.forEach(function (e, j) { if (j >= hasta) return; var x = X(e[1]), y = 110 - (j % 3) * 30, on = j === hasta - 1 || j === marcaA || j === marcaB; s += ln(x, y + 8, x, 130, on ? C.coral : C.gris, 1.5) + em(x, y - 4, e[2], on ? 20 : 15) + (on ? txw(Math.min(360, Math.max(110, x)), y - 22, e[0] + ' (' + anio(e[1]) + ')', { a: 'middle', s: 10.5, w: 800, c: C.coral }, 24) : ''); });
    if (marcaA != null && marcaB != null) { var xa = X(L[marcaA][1]), xb = X(L[marcaB][1]); s += '<path d="M' + r1(xa) + ',168 L' + r1(xb) + ',168" stroke="' + C.teal + '" stroke-width="3" marker-start="url(#natfl)" marker-end="url(#natfl)"/>' + tx((xa + xb) / 2, 186, fmt(entre(L[marcaA][1], L[marcaB][1])) + ' años', { a: 'middle', s: 13, w: 900, c: C.teal }); }
    return S(470, 195, s); }
  M.linea_historica = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L0 = p.items ? p.items.map(function (e) { return [e.t, e.a, e.e || '📌']; }) : LINEAS[p.linea || 'america'] || LINEAS.america;
    escena(el, '', function () { var L = L0.slice().sort(function (a, b) { return a[1] - b[1]; }), P = [{ vis: linea(L, 0), txt: 'Una <b>línea de tiempo</b> ordena los hechos de izquierda a derecha, de lo más antiguo a lo más reciente, con una escala pareja.' }];
      L.forEach(function (e, j) { P.push({ vis: linea(L, j + 1), txt: '<b>' + e[0] + '</b>: año ' + anio(e[1]) + ', siglo <b>' + siglo(e[1]) + '</b>.' }); });
      var a = 0, b = L.length - 1; P.push({ vis: linea(L, L.length, a, b), txt: 'Entre «' + L[a][0].toLowerCase() + '» y «' + L[b][0].toLowerCase() + '» pasaron <b>' + fmt(entre(L[a][1], L[b][1])) + ' años</b>' + (L[a][1] < 0 && L[b][1] > 0 ? ' (sumamos los dos y restamos 1, porque no existe el año 0).' : ' (restamos el más antiguo al más reciente).') });
      P.push({ vis: linea(L, L.length) + card('Siglo = año ÷ 100, redondeando hacia arriba: 1810 → 18,1 → siglo <b>XIX</b>. Los años 1801 a 1900 son el siglo XIX.'), txt: 'Para saber el siglo, dividimos el año por 100 y redondeamos hacia arriba. Se escribe con números romanos.' });
      return P; });
  } };
  M.linea_historica_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var k = rot(3, u);
      if (k === 0) { var a = pick([R(101, 2025), R(101, 2025), -R(101, 3000)]); return { cons: '¿A qué siglo pertenece el año <b>' + anio(a) + '</b>? Escribilo en números romanos' + (a < 0 ? ' (sin «a. C.»)' : '') + '.', campos: [{ tipo: 'texto', lab: 'Siglo', v: [romano(Math.ceil(Math.abs(a) / 100))] }], ayuda: 'Dividí el año por 100 y redondeá hacia arriba.', bien: '¡Bien! Siglo ' + siglo(a) + '.' }; }
      if (k === 1) { var x = R(1500, 1990), y = x + R(5, 200); return { cons: '¿Cuántos años pasaron entre <b>' + x + '</b> y <b>' + y + '</b>?', campos: [{ lab: 'Años', v: y - x }], ayuda: 'Restá el año más antiguo al más reciente.', bien: '¡Bien! ' + (y - x) + ' años.' }; }
      var aa = -R(50, 800), bb = R(10, 500); return { cons: '¿Cuántos años pasaron entre el año <b>' + anio(aa) + '</b> y el año <b>' + anio(bb) + '</b>?', campos: [{ lab: 'Años', v: entre(aa, bb) }], ayuda: 'Sumá ' + (-aa) + ' + ' + bb + ' y restá 1, porque no existe el año 0.', bien: '¡Bien! ' + (-aa) + ' + ' + bb + ' − 1 = ' + entre(aa, bb) + ' años.' }; });
  } };

  // 2) COORDENADAS GEOGRÁFICAS: latitud y longitud sobre la grilla
  var CIU = [['Buenos Aires', -34.6, -58.4], ['Ushuaia', -54.8, -68.3], ['Lima', -12, -77], ['Ciudad de México', 19.4, -99.1], ['Nueva York', 40.7, -74], ['Madrid', 40.4, -3.7], ['El Cairo', 30, 31.2], ['Moscú', 55.8, 37.6], ['Tokio', 35.7, 139.7], ['Sídney', -33.9, 151.2], ['Ciudad del Cabo', -33.9, 18.4], ['Nairobi', -1.3, 36.8]];
  function gx(lo) { return 35 + (lo + 180) / 360 * 400; } function gy(la) { return 20 + (90 - la) / 180 * 200; }
  function grilla(fase, c, tap) { var s = rc(35, 20, 400, 200, '#EAF6FB', C.gris, 0);
    for (var la = -60; la <= 60; la += 30) s += ln(35, gy(la), 435, gy(la), '#cfe3ea', 1) + tx(30, gy(la) + 4, Math.abs(la) + '°' + (la > 0 ? 'N' : la < 0 ? 'S' : ''), { a: 'end', s: 9 });
    for (var lo = -150; lo <= 150; lo += 30) s += ln(gx(lo), 20, gx(lo), 220, '#cfe3ea', 1) + tx(gx(lo), 234, Math.abs(lo) + '°' + (lo > 0 ? 'E' : lo < 0 ? 'O' : ''), { a: 'middle', s: 8.5 });
    if (fase >= 1) s += ln(35, gy(0), 435, gy(0), C.coral, 2.5) + tx(432, gy(0) - 5, 'Ecuador', { a: 'end', s: 10, w: 800, c: C.coral }) + ln(gx(0), 20, gx(0), 220, C.lila, 2.5) + tx(gx(0) + 4, 32, 'Greenwich', { s: 10, w: 800, c: C.lila });
    if (fase >= 2 && !tap) s += tx(60, 40, 'Norte', { s: 10, c: C.teal, w: 800 }) + tx(60, 212, 'Sur', { s: 10, c: C.teal, w: 800 }) + tx(400, 120, 'Este', { a: 'end', s: 10, c: C.teal, w: 800 }) + tx(70, 120, 'Oeste', { s: 10, c: C.teal, w: 800 });
    if (c && fase >= 3) s += ln(35, gy(c[1]), 435, gy(c[1]), C.azul, 2, ' stroke-dasharray="5 3"');
    if (c && fase >= 4) s += ln(gx(c[2]), 20, gx(c[2]), 220, C.verde, 2, ' stroke-dasharray="5 3"');
    if (c && fase >= 5) s += ci(gx(c[2]), gy(c[1]), 6, C.coral) + tx(gx(c[2]) + 8, gy(c[1]) - 6, c[0], { s: 11, w: 900, c: C.coral });
    if (tap) CIU.forEach(function (q, j) { s += '<g data-t="' + j + '" class="nat-tap">' + ci(gx(q[2]), gy(q[1]), 7, '#fff', C.osc) + '</g>'; });
    return S(470, 242, s); }
  function coord(c) { return Math.abs(Math.round(c[1])) + '° ' + (c[1] >= 0 ? 'N' : 'S') + ', ' + Math.abs(Math.round(c[2])) + '° ' + (c[2] >= 0 ? 'E' : 'O'); }
  M.coordenadas = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('c', 'Ciudad', CIU.map(function (c, i) { return [i, c[0]]; }), 0), function (o) { var c = CIU[+(o.c || 0)];
      return [{ vis: grilla(0), txt: 'La <b>red de coordenadas</b>: líneas imaginarias sobre la Tierra. Los <b>paralelos</b> van de oeste a este y los <b>meridianos</b>, de polo a polo.' },
        { vis: grilla(1), txt: 'Dos líneas de referencia: el <b>Ecuador</b> (latitud 0°) y el <b>meridiano de Greenwich</b> (longitud 0°).' }, { vis: grilla(2), txt: 'Dividen la Tierra en hemisferios: norte y sur, este y oeste.' },
        { vis: grilla(3, c), txt: '<b>Latitud</b>: cuántos grados al norte o al sur del Ecuador. ' + c[0] + ': ' + Math.abs(Math.round(c[1])) + '° ' + (c[1] >= 0 ? 'norte' : 'sur') + '.' },
        { vis: grilla(4, c), txt: '<b>Longitud</b>: cuántos grados al este o al oeste de Greenwich: ' + Math.abs(Math.round(c[2])) + '° ' + (c[2] >= 0 ? 'este' : 'oeste') + '.' },
        { vis: grilla(5, c), txt: 'Donde se cruzan está la ciudad: <b>' + coord(c) + '</b>. Cada lugar del planeta tiene un solo par de coordenadas.' }]; });
  } };
  M.coordenadas_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    tocar(el, api, function () { var k = rot(CIU.length, u), c = CIU[k]; return { cons: 'Tocá el punto que está en <b>' + coord(c) + '</b>.', svg: grilla(2, null, true), ok: k, ayuda: 'Primero buscá la latitud (arriba o abajo del Ecuador) y después la longitud (a la derecha o a la izquierda de Greenwich).', bien: '¡Bien! Es ' + c[0] + '.' }; });
  } };

  // 3) ESCALA DEL MAPA: medir con regla y pasar a kilómetros
  function mapaEsc(cm, esc, fase) { var s = rc(20, 20, 430, 150, '#F1F8E9', C.gris, 10) + '<path d="M40,140 C120,60 200,150 300,80 S420,60 440,40" fill="none" stroke="#90CAF9" stroke-width="6"/>', x1 = 70, x2 = 70 + cm * 36;
    s += ci(x1, 110, 6, C.coral) + tx(x1, 98, 'A', { a: 'middle', s: 12, w: 900 }) + ci(x2, 110, 6, C.coral) + tx(x2, 98, 'B', { a: 'middle', s: 12, w: 900 });
    if (fase >= 1) { s += rc(60, 122, Math.max(cm, 1) * 36 + 30, 26, '#FFF9C4', C.osc, 3); for (var k = 0; k <= cm; k++) s += ln(70 + k * 36, 122, 70 + k * 36, 134, C.osc, 1.5) + tx(70 + k * 36, 145, k, { a: 'middle', s: 9 }); }
    s += tx(440, 190, 'Escala 1 : ' + fmt(esc), { a: 'end', s: 12, w: 900 }) + rc(30, 180, 72, 8, C.osc) + rc(102, 180, 72, 8, '#fff', C.osc) + tx(30, 202, '0', { s: 9 }) + tx(174, 202, fmt(esc * 2 / 100000) + ' km', { a: 'middle', s: 9 });
    return S(470, 210, s); }
  M.escala_mapa = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('cm', 'Distancia medida en el mapa (cm)', 1, 10, 1, 6) + sel('e', 'Escala', [[100000, '1 : 100.000 (una región)'], [1000000, '1 : 1.000.000 (una provincia)'], [5000000, '1 : 5.000.000 (un país)']], 1000000), function (o) { var cm = o.cm || 6, e = +(o.e || 1000000), real = cm * e, km = real / 100000;
      return [{ vis: mapaEsc(cm, e, 0), txt: 'Un mapa es una reducción. La <b>escala 1 : ' + fmt(e) + '</b> dice que 1 cm del mapa equivale a ' + fmt(e) + ' cm de la realidad.' },
        { vis: mapaEsc(cm, e, 1), txt: 'Medimos con la regla la distancia entre A y B: <b>' + cm + ' cm</b>.' },
        { vis: mapaEsc(cm, e, 1) + nota(cm + ' cm × ' + fmt(e) + ' = ' + fmt(real) + ' cm'), txt: 'Multiplicamos por la escala: ' + fmt(real) + ' cm en la realidad.' },
        { vis: mapaEsc(cm, e, 1) + nota(fmt(real) + ' cm ÷ 100.000 = ' + fmt(km) + ' km'), txt: 'Pasamos a kilómetros: 1 km tiene 100.000 cm. A y B están a <b>' + fmt(km) + ' km</b>.' }]; });
  } };
  M.escala_mapa_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var cm = R(2, 12), e = pick([100000, 250000, 500000, 1000000, 2000000]), km = cm * e / 100000;
      return { cons: 'En un mapa a escala <b>1 : ' + fmt(e) + '</b>, dos ciudades están a <b>' + cm + ' cm</b>. ¿Cuántos kilómetros las separan en la realidad?', campos: [{ lab: 'Distancia', v: km, un: 'km' }], ayuda: 'Multiplicá los cm por la escala y dividí por 100.000 para pasar a km.', bien: '¡Bien! ' + cm + ' × ' + fmt(e) + ' = ' + fmt(cm * e) + ' cm = ' + fmt(km) + ' km.' }; });
  } };

  // 4) HUSOS HORARIOS: relojes de distintas ciudades
  var HUS = [['Buenos Aires', -3], ['Ciudad de México', -6], ['Nueva York', -5], ['Londres', 0], ['Madrid', 1], ['Moscú', 3], ['Nueva Delhi', 5.5], ['Tokio', 9], ['Sídney', 10]];
  function reloj(x, y, h, nom) { var a = (h % 12) / 12 * 2 * Math.PI - Math.PI / 2, m = (h % 1) * 2 * Math.PI - Math.PI / 2, dia = h >= 7 && h < 20; return ci(x, y, 38, dia ? '#FFF9C4' : '#263238', C.osc) + ln(x, y, x + 20 * Math.cos(a), y + 20 * Math.sin(a), dia ? C.osc : '#fff', 4) + ln(x, y, x + 30 * Math.cos(m), y + 30 * Math.sin(m), dia ? C.osc : '#fff', 2) + tx(x, y + 58, nom, { a: 'middle', s: 11, w: 800 }) + tx(x, y + 74, hh(h), { a: 'middle', s: 13, w: 900, c: C.coral }); }
  function hh(h) { h = ((h % 24) + 24) % 24; var hr = Math.floor(h), mi = Math.round((h - hr) * 60); return (hr < 10 ? '0' : '') + hr + ':' + (mi < 10 ? '0' : '') + mi; }
  M.husos = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('h', 'Hora en Buenos Aires', 0, 23, 1, 10) + sel('d', 'Otra ciudad', HUS.slice(1).map(function (q, i) { return [i + 1, q[0]]; }), 7), function (o) { var h = o.h == null ? 10 : o.h, d = HUS[+(o.d || 7)], dif = d[1] - (-3), h2 = h + dif, fran = '';
      for (var k = -12; k < 12; k++) fran += rc(20 + (k + 12) * 18.3, 10, 18.3, 26, k % 2 ? '#E3F2FD' : '#fff', C.gris) ;
      fran += ln(20 + (-3 + 12.5) * 18.3, 6, 20 + (-3 + 12.5) * 18.3, 40, C.coral, 3) + ln(20 + (d[1] + 12.5) * 18.3, 6, 20 + (d[1] + 12.5) * 18.3, 40, C.teal, 3) + tx(235, 56, '24 husos de 15° cada uno', { a: 'middle', s: 10.5 });
      return [{ vis: S(470, 64, fran), txt: 'La Tierra gira 360° en 24 horas: cada hora gira <b>15°</b>. Por eso el mundo se divide en <b>24 husos horarios</b>.' },
        { vis: S(470, 64, fran) + nota(d[0] + ': UTC ' + (d[1] >= 0 ? '+' : '') + fmt(d[1]) + ' · Buenos Aires: UTC −3'), txt: 'Hacia el <b>este</b> (donde sale antes el Sol) la hora es más tarde; hacia el oeste, más temprano. Diferencia: <b>' + (dif >= 0 ? '+' : '') + fmt(dif) + ' h</b>.' },
        { vis: S(470, 140, reloj(130, 50, h, 'Buenos Aires') + reloj(340, 50, h2, d[0])), txt: 'Si en Buenos Aires son las ' + hh(h) + ', en ' + d[0] + ' son las <b>' + hh(h2) + '</b>' + (h2 >= 24 ? ' del día siguiente' : h2 < 0 ? ' del día anterior' : '') + '.' }]; });
  } };
  M.husos_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = pick(HUS.filter(function (q) { return q[1] % 1 === 0; })), b; do { b = pick(HUS.filter(function (q) { return q[1] % 1 === 0; })); } while (b === a); var h = R(0, 23), h2 = ((h + b[1] - a[1]) % 24 + 24) % 24;
      return { cons: 'En <b>' + a[0] + '</b> (UTC ' + (a[1] >= 0 ? '+' : '') + a[1] + ') son las <b>' + h + ' h</b>. ¿Qué hora es en <b>' + b[0] + '</b> (UTC ' + (b[1] >= 0 ? '+' : '') + b[1] + ')? Escribí solo la hora, de 0 a 23.', campos: [{ lab: 'Hora', v: h2, un: 'h' }], ayuda: 'Calculá la diferencia de husos y sumala (si pasa de 24, restá 24).', bien: '¡Bien! Diferencia ' + (b[1] - a[1]) + ' h: son las ' + h2 + ' h.' }; });
  } };

  // 5) PIRÁMIDE DE POBLACIÓN (datos aproximados, en %)
  var PIR = [['Níger (joven)', [[25, 24], [15, 15], [7, 7], [3, 3], [1, 1], [0.3, 0.4]], 'joven o progresiva: base ancha, muchos nacimientos y vida más corta'], ['Argentina (adulta)', [[11, 11], [11, 11], [10, 10], [8, 8], [6, 7], [2, 3]], 'adulta o estacionaria: forma de campana, natalidad en baja'], ['Japón (envejecida)', [[6, 6], [7, 7], [8, 8], [10, 10], [10, 11], [7, 10]], 'envejecida o regresiva: base angosta y muchos mayores']];
  var EDAD = ['0-14', '15-29', '30-44', '45-59', '60-74', '75+'];
  function piramide(P, hasta) { var s = ln(235, 15, 235, 200, C.osc, 2) + tx(140, 214, 'varones %', { a: 'middle', s: 10.5, w: 800, c: C.azul }) + tx(330, 214, 'mujeres %', { a: 'middle', s: 10.5, w: 800, c: C.rosa });
    P[1].forEach(function (g, i) { var y = 172 - i * 30; s += tx(235, y + 16, EDAD[i], { a: 'middle', s: 9.5, w: 800 }); if (i >= hasta) return; s += rc(215 - g[0] * 7, y, g[0] * 7, 24, '#90CAF9', null, 3) + rc(255, y, g[1] * 7, 24, '#F48FB1', null, 3); });
    return S(470, 222, s.replace(/<text x="235"/g, '<text x="235"')); }
  M.piramide_poblacion = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'País', PIR.map(function (q, i) { return [i, q[0]]; }), 0), function (o) { var P = PIR[+(o.i || 0)], j = P[1][0][0] + P[1][0][1], m = P[1][4][0] + P[1][4][1] + P[1][5][0] + P[1][5][1];
      return [{ vis: piramide(P, 0), txt: 'Una <b>pirámide de población</b>: en el centro, las edades; a la izquierda, los varones; a la derecha, las mujeres. Cada barra es el % de la población.' },
        { vis: piramide(P, 2), txt: 'Abajo están los más jóvenes: menores de 15 años, <b>' + fmt(j) + ' %</b> de la población.' }, { vis: piramide(P, 6), txt: 'Arriba, los mayores de 60: <b>' + fmt(m) + ' %</b>.' },
        { vis: piramide(P, 6), txt: 'Por su forma es una pirámide <b>' + P[2] + '</b>.' }]; });
  } };
  M.piramide_poblacion_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    elegir(el, api, function () { var k = rot(3, u), P = PIR[k], ops = ['Joven (progresiva)', 'Adulta (estacionaria)', 'Envejecida (regresiva)']; return { cons: '¿Qué tipo de pirámide de población es esta?', html: piramide(P, 6), ops: ops, ok: ops[k], ayuda: 'Mirá si la base es ancha (muchos chicos) o angosta, y cuántos mayores hay arriba.', bien: '¡Bien! ' + P[2][0].toUpperCase() + P[2].slice(1) + '.' }; });
  } };

  // 6) INDICADORES DE POBLACIÓN: densidad, natalidad, mortalidad y crecimiento
  function barrasT(tn, tm, h) { var mx = Math.max(tn, tm, 1), s = ''; [['Natalidad', tn, C.verde], ['Mortalidad', tm, C.rosa]].forEach(function (q, i) { if (i >= h) return; var w = q[1] / mx * 300; s += tx(100, 32 + i * 34, q[0], { a: 'end', s: 11, w: 800 }) + rc(108, 18 + i * 34, w, 20, q[2], null, 5) + tx(114 + w, 33 + i * 34, fmt(Math.round(q[1] * 10) / 10) + ' ‰', { s: 11, w: 900 }); });
    if (h >= 3) s += tx(235, 100, (tn - tm >= 0 ? '+' : '') + fmt(Math.round((tn - tm) * 10) / 10) + ' ‰ por año', { a: 'middle', s: 14, w: 900, c: tn >= tm ? C.verde : C.rosa }); return S(470, 110, s); }
  M.indicadores = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('pob', 'Habitantes (miles)', 10, 2000, 10, 400) + ctrl('sup', 'Superficie (km²)', 100, 50000, 100, 8000) + ctrl('nac', 'Nacimientos en un año', 100, 40000, 100, 6000) + ctrl('def', 'Defunciones en un año', 100, 40000, 100, 3200), function (o) { var pob = (o.pob || 400) * 1000, sup = o.sup || 8000, d = pob / sup, tn = o.nac / pob * 1000, tm = o.def / pob * 1000, cn = tn - tm;
      var cuad = ''; for (var i = 0; i < 25; i++) cuad += rc(150 + (i % 5) * 34, 10 + Math.floor(i / 5) * 34, 32, 32, '#F1F8E9', C.gris, 3) + em(166 + (i % 5) * 34, 26 + Math.floor(i / 5) * 34, '🧍', Math.min(20, 6 + d / 10));
      return [{ vis: S(470, 185, cuad) + nota('Densidad = ' + fmt(pob) + ' hab ÷ ' + fmt(sup) + ' km² ≈ ' + fmt(Math.round(d * 10) / 10) + ' hab/km²'), txt: 'La <b>densidad de población</b> dice cuántas personas viven, en promedio, en cada km². Cada cuadrado es 1 km².' },
        { vis: barrasT(tn, tm, 1) + nota('Natalidad = ' + fmt(o.nac) + ' ÷ ' + fmt(pob) + ' × 1000 ≈ ' + fmt(Math.round(tn * 10) / 10) + ' ‰'), txt: 'La <b>tasa de natalidad</b> cuenta los nacimientos de un año por cada 1.000 habitantes (‰ = por mil).' },
        { vis: barrasT(tn, tm, 2) + nota('Mortalidad = ' + fmt(o.def) + ' ÷ ' + fmt(pob) + ' × 1000 ≈ ' + fmt(Math.round(tm * 10) / 10) + ' ‰'), txt: 'La <b>tasa de mortalidad</b>: las defunciones por cada 1.000 habitantes.' },
        { vis: barrasT(tn, tm, 3) + nota('Crecimiento natural = ' + fmt(Math.round(tn * 10) / 10) + ' − ' + fmt(Math.round(tm * 10) / 10) + ' = ' + fmt(Math.round(cn * 10) / 10) + ' ‰'), txt: cn > 0 ? 'Nacen más de los que mueren: la población <b>crece</b> (sin contar las migraciones).' : cn < 0 ? 'Mueren más de los que nacen: la población <b>disminuye</b>, salvo que lleguen migrantes.' : 'Nacen tantos como mueren: la población se mantiene.' }]; });
  } };
  M.indicadores_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { if (rot(2, u)) { var sup = pick([200, 500, 1000, 2500]), d = pick([4, 10, 25, 40, 120]); return { cons: 'Una provincia tiene <b>' + fmt(sup * d) + ' habitantes</b> y <b>' + fmt(sup) + ' km²</b>. ¿Cuál es su densidad?', campos: [{ lab: 'Densidad', v: d, un: 'hab/km²' }], ayuda: 'Densidad = habitantes ÷ km².', bien: '¡Bien! ' + d + ' hab/km².' }; }
      var pob = pick([10000, 50000, 200000]), t = pick([8, 12, 15, 20, 25]); return { cons: 'En una ciudad de <b>' + fmt(pob) + '</b> habitantes nacieron <b>' + fmt(pob * t / 1000) + '</b> bebés en un año. ¿Cuál es la tasa de natalidad (por mil)?', campos: [{ lab: 'Natalidad', v: t, un: '‰' }], ayuda: 'Nacimientos ÷ habitantes × 1000.', bien: '¡Bien! ' + t + ' ‰.' }; });
  } };

  // 7) CIRCUITO PRODUCTIVO: sectores y valor agregado
  var CIRC = { pan: ['Circuito del pan', [['Cultivo de trigo', 'primario', '🌾', 20], ['Molino harinero', 'secundario', '🏭', 45], ['Panadería', 'secundario', '🥖', 80], ['Transporte y venta en el almacén', 'terciario', '🚚', 100]]],
    yerba: ['Circuito de la yerba mate', [['Cosecha de la yerba', 'primario', '🌿', 15], ['Secado y molienda', 'secundario', '🔥', 50], ['Envasado', 'secundario', '📦', 70], ['Distribución y supermercado', 'terciario', '🛒', 100]]],
    remera: ['Circuito de una remera de algodón', [['Cultivo de algodón', 'primario', '☁️', 10], ['Hilandería', 'secundario', '🧵', 30], ['Confección', 'secundario', '👕', 65], ['Publicidad y venta en el local', 'terciario', '🏬', 100]]] };
  var SEC = { primario: ['Primario', '#8BC34A', 'obtiene recursos de la naturaleza'], secundario: ['Secundario', '#FFB74D', 'transforma la materia prima en productos'], terciario: ['Terciario', '#64B5F6', 'brinda servicios: transporte, comercio']};
  function circDib(L, hasta) { var s = ''; L.forEach(function (e, j) { if (j >= hasta) return; var x = 30 + j * 110, sc = SEC[e[1]]; s += rc(x, 30, 96, 90, sc[1], null, 12, ' fill-opacity=".35"') + em(x + 48, 60, e[2], 28) + txw(x + 48, 100, e[0], { a: 'middle', s: 9.5, w: 800 }, 16) + tx(x + 48, 140, sc[0], { a: 'middle', s: 10, w: 900, c: C.teal }) + rc(x + 20, 210 - e[3] * 0.5, 56, e[3] * 0.5, C.sol, null, 4) + tx(x + 48, 205 - e[3] * 0.5, '$' + e[3], { a: 'middle', s: 10.5, w: 900 }) + (j ? fl(x - 12, 75, x - 2, 75, C.osc, 2) : ''); });
    return S(470, 225, s + tx(10, 222, 'precio acumulado', { s: 9.5, c: C.sol, w: 800 })); }
  M.circuito_productivo = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Producto', Object.keys(CIRC).map(function (k) { return [k, CIRC[k][0]]; }), p.producto || 'pan'), function (o) { var c = CIRC[o.i || 'pan'], L = c[1], P = [{ vis: circDib(L, 0), txt: '<b>' + c[0] + '</b>: las etapas que recorre un producto desde la naturaleza hasta el consumidor.' }];
      L.forEach(function (e, j) { P.push({ vis: circDib(L, j + 1), txt: '<b>' + e[0] + '</b>: sector ' + e[1] + ' (' + SEC[e[1]][2] + '). Precio acumulado: $' + e[3] + '.' }); });
      P.push({ vis: circDib(L, L.length), txt: 'En cada etapa se suma <b>valor agregado</b>: la materia prima vale $' + L[0][3] + ' y el producto final, $' + L[L.length - 1][3] + '.' }); return P; });
  } };
  M.circuito_productivo_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = []; Object.keys(CIRC).forEach(function (k) { CIRC[k][1].forEach(function (e) { it.push(e); }); }); it = mezclar(it).slice(0, 6); return { tit: '¿A qué sector económico pertenece cada actividad?', cajas: ['Primario', 'Secundario', 'Terciario'], items: it.map(function (e, i) { return { v: 's' + i, t: e[2] + ' ' + e[0], c: ['primario', 'secundario', 'terciario'].indexOf(e[1]) }; }) }; }); otro(el);
  } };

  // 8) OFERTA Y DEMANDA: el precio de equilibrio
  function mercado(pr, hasta) { var x0 = 60, y0 = 200, W = 360, Hh = 170, X = function (q) { return x0 + q / 100 * W; }, Y = function (p) { return y0 - p / 100 * Hh; }, s = ln(x0, y0, x0 + W, y0) + ln(x0, y0, x0, y0 - Hh - 6) + tx(x0 + W, y0 + 18, 'cantidad', { a: 'end', s: 10.5 }) + tx(x0 + 4, y0 - Hh - 10, 'precio', { s: 10.5 });
    s += ln(X(10), Y(90), X(90), Y(10), C.azul, 3) + tx(X(90), Y(10) + 16, 'demanda', { a: 'middle', s: 10.5, w: 800, c: C.azul });
    if (hasta >= 1) s += ln(X(10), Y(10), X(90), Y(90), C.coral, 3) + tx(X(90), Y(90) - 8, 'oferta', { a: 'middle', s: 10.5, w: 800, c: C.coral });
    if (hasta >= 2) { var qd = 100 - pr, qo = pr; s += ln(x0, Y(pr), X(Math.max(qd, qo)), Y(pr), C.osc, 1.5, ' stroke-dasharray="4 3"') + ci(X(qd), Y(pr), 5, C.azul) + ci(X(qo), Y(pr), 5, C.coral) + tx(x0 - 6, Y(pr) + 4, '$' + pr, { a: 'end', s: 10.5, w: 900 });
      if (qd !== qo) s += '<path d="M' + r1(X(Math.min(qd, qo))) + ',' + r1(Y(pr) - 12) + ' L' + r1(X(Math.max(qd, qo))) + ',' + r1(Y(pr) - 12) + '" stroke="' + C.sol + '" stroke-width="3" marker-start="url(#natfl)" marker-end="url(#natfl)"/>' + tx((X(qd) + X(qo)) / 2, Y(pr) - 18, pr > 50 ? 'sobra (exceso de oferta)' : 'falta (escasez)', { a: 'middle', s: 10.5, w: 900, c: C.sol }); }
    if (hasta >= 3) s += ci(X(50), Y(50), 7, 'none', C.verde, ' stroke-width="3"') + tx(X(50) + 12, Y(50) + 4, 'equilibrio: $50', { s: 11, w: 900, c: C.verde });
    return S(470, 220, s); }
  M.mercado = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('p', 'Precio ($)', 10, 90, 5, 70), function (o) { var pr = o.p || 70, qd = 100 - pr, qo = pr;
      return [{ vis: mercado(pr, 0), txt: 'La <b>demanda</b>: cuánto quieren comprar los consumidores. Cuanto más caro, menos compran.' }, { vis: mercado(pr, 1), txt: 'La <b>oferta</b>: cuánto quieren vender los productores. Cuanto más caro, más quieren vender.' },
        { vis: mercado(pr, 2), txt: 'Con precio $' + pr + ' se demandan ' + qd + ' unidades y se ofrecen ' + qo + ': ' + (qd === qo ? '¡coinciden!' : qd > qo ? 'falta producto (<b>escasez</b>) y el precio tiende a <b>subir</b>.' : 'sobra producto (<b>exceso de oferta</b>) y el precio tiende a <b>bajar</b>.') },
        { vis: mercado(pr, 3), txt: 'El <b>precio de equilibrio</b> es donde se cruzan: lo que se quiere comprar es igual a lo que se quiere vender.' }]; });
  } };
  M.mercado_x = { tipo: 'ejercicio', render: function (el, p, api) {
    elegir(el, api, function () { var pr = pick([20, 30, 40, 60, 70, 80]); return { cons: 'Con precio <b>$' + pr + '</b>, ¿qué pasa en este mercado?', html: mercado(pr, 2).replace(/<text[^>]*>(sobra|falta)[^<]*<\/text>/, ''), ops: ['Hay escasez y el precio tiende a subir', 'Hay exceso de oferta y el precio tiende a bajar', 'Está en equilibrio'], ok: pr < 50 ? 'Hay escasez y el precio tiende a subir' : 'Hay exceso de oferta y el precio tiende a bajar', ayuda: 'Compará el punto azul (demanda) con el rojo (oferta) en ese precio.' }; });
  } };

  // 9) INFLACIÓN: la canasta que se encarece
  var CAN = [['Pan (1 kg)', 1800, '🥖'], ['Leche (1 L)', 1300, '🥛'], ['Yerba (1 kg)', 4500, '🧉'], ['Fideos (500 g)', 1100, '🍝'], ['Manzanas (1 kg)', 2200, '🍎']];
  M.inflacion = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('i', 'Inflación del período (%)', 5, 200, 5, 50) + ctrl('s', 'Dinero disponible ($)', 5000, 50000, 1000, 20000), function (o) { var inf = o.i || 50, din = o.s || 20000, tot = CAN.reduce(function (a, c) { return a + c[1]; }, 0), tot2 = Math.round(tot * (1 + inf / 100));
      var tabla = function (f) { return S(470, 40 + CAN.length * 26, CAN.map(function (c, j) { var y = 30 + j * 26; return em(30, y - 4, c[2], 18) + tx(50, y, c[0], { s: 11.5, w: 700 }) + tx(300, y, '$' + fmt(c[1]), { a: 'end', s: 11.5 }) + (f ? tx(440, y, '$' + fmt(Math.round(c[1] * (1 + inf / 100))), { a: 'end', s: 11.5, w: 900, c: C.coral }) : ''); }).join('') + tx(300, 14, 'antes', { a: 'end', s: 10, w: 800 }) + (f ? tx(440, 14, 'después', { a: 'end', s: 10, w: 800, c: C.coral }) : '')); };
      return [{ vis: tabla(false) + nota('Canasta: $' + fmt(tot)), txt: 'Una <b>canasta</b> de productos de todos los días cuesta $' + fmt(tot) + '.' },
        { vis: tabla(true) + nota('Canasta: $' + fmt(tot2)), txt: 'Con una <b>inflación</b> del ' + inf + ' %, los precios suben en general: la misma canasta cuesta $' + fmt(tot2) + '.' },
        { vis: nota('Con $' + fmt(din) + ': antes ' + fmt(Math.floor(din / tot * 10) / 10) + ' canastas → ahora ' + fmt(Math.floor(din / tot2 * 10) / 10)), txt: 'Si el sueldo no aumenta, con el mismo dinero se compra menos: baja el <b>poder adquisitivo</b>.' },
        { vis: nota('Aumento % = (nuevo − viejo) ÷ viejo × 100'), txt: 'Para medir cuánto subió un precio: la diferencia dividida por el precio viejo, por 100.' }]; });
  } };
  M.inflacion_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var c = pick(CAN), i = pick([10, 20, 25, 40, 50, 100]), n = Math.round(c[1] * (1 + i / 100)); return { cons: '<b>' + c[0] + '</b> costaba <b>$' + fmt(c[1]) + '</b> y ahora cuesta <b>$' + fmt(n) + '</b>. ¿Qué porcentaje aumentó?', campos: [{ lab: 'Aumento', v: i, un: '%', tol: 0.6 }], ayuda: '(precio nuevo − precio viejo) ÷ precio viejo × 100.', bien: '¡Bien! Aumentó un ' + i + ' %.' }; });
  } };

  // 10) FLUJO CIRCULAR DE LA ECONOMÍA
  var FLU = [['Familias', 'Empresas', 'trabajo', C.verde], ['Empresas', 'Familias', 'salarios', C.sol], ['Empresas', 'Familias', 'bienes y servicios', C.azul], ['Familias', 'Empresas', 'pagos por lo que compran', C.coral], ['Familias', 'Estado', 'impuestos', C.lila], ['Estado', 'Familias', 'salud, educación, seguridad', C.teal]];
  var POSF = { Familias: [90, 150], Empresas: [380, 150], Estado: [235, 40] };
  function flujo(h) { var s = ''; ['Familias', 'Empresas', 'Estado'].forEach(function (k) { var q = POSF[k]; if (k === 'Estado' && h < 5) return; s += rc(q[0] - 55, q[1] - 22, 110, 44, '#fff', C.osc, 12) + em(q[0] - 34, q[1], k === 'Familias' ? '👨‍👩‍👧' : k === 'Empresas' ? '🏭' : '🏛️', 18) + tx(q[0] + 12, q[1] + 5, k, { a: 'middle', s: 12, w: 900 }); });
    FLU.forEach(function (f, j) { if (j >= h) return; var a = POSF[f[0]], b = POSF[f[1]], off = (j % 2 ? 1 : -1) * (j < 2 ? 30 : 82), est = f[0] === 'Estado' || f[1] === 'Estado';
      if (!est) s += '<path d="M' + (a[0] + (b[0] > a[0] ? 55 : -55)) + ',' + (a[1] + off * 0.3) + ' Q235,' + (150 + off) + ' ' + (b[0] + (b[0] > a[0] ? -55 : 55)) + ',' + (b[1] + off * 0.3) + '" fill="none" stroke="' + f[3] + '" stroke-width="3" marker-end="url(#natfl)"/>' + tx(235, 150 + off / 2 + (off > 0 ? 12 : -4), f[2], { a: 'middle', s: 10.5, w: 900, c: f[3] });
      else s += fl(f[0] === 'Estado' ? 200 : 120, f[0] === 'Estado' ? 62 : 128, f[0] === 'Estado' ? 120 : 190, f[0] === 'Estado' ? 128 : 62, f[3], 3) + txw(f[0] === 'Estado' ? 12 : 150, f[0] === 'Estado' ? 104 : 74, f[2], { a: f[0] === 'Estado' ? 'start' : 'end', s: 10, w: 900, c: f[3] }, 16); });
    return S(470, 240, s); }
  M.flujo_circular = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, '', function () { var P = [{ vis: flujo(0), txt: 'Los <b>agentes económicos</b>: familias y empresas (después se suma el Estado).' }];
      FLU.forEach(function (f, j) { P.push({ vis: flujo(j + 1), txt: '<b>' + f[0] + ' → ' + f[1] + '</b>: ' + f[2] + '.' }); });
      P.push({ vis: flujo(6), txt: 'Es un <b>flujo circular</b>: los bienes y el trabajo van en un sentido; el dinero, en el otro. Si un agente gasta menos, los demás lo sienten.' }); return P; });
  } };
  M.flujo_circular_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    elegir(el, api, function () { var f = FLU[rot(FLU.length, u)], otros = FLU.filter(function (x) { return x !== f; }).map(function (x) { return x[2]; }); return { cons: 'En el flujo circular, ¿qué va de <b>' + f[0].toLowerCase() + '</b> a <b>' + f[1].toLowerCase() + '</b>?', html: flujo(1).replace(/<path[^>]*\/>|<text[^>]*>trabajo<\/text>/g, ''), ops: mezclar(otros).slice(0, 3).concat(f[2]), ok: f[2], ayuda: 'Pensá qué entrega cada uno y qué recibe a cambio.' }; });
  } };

  // 11) DESIGUALDAD: el reparto del ingreso por quintiles
  var QUI = [['Un país más igualitario', [10, 15, 19, 24, 32]], ['Un país muy desigual', [4, 8, 13, 21, 54]]];
  function quint(Q, h) { var s = ''; Q.forEach(function (v, i) { if (i >= h) return; var x = 30 + i * 88; s += em(x + 40, 40, '🧍', 20) + tx(x + 40, 66, (i + 1) + '.º quinto', { a: 'middle', s: 10, w: 800 }) + rc(x + 10, 200 - v * 2.4, 60, v * 2.4, i === 4 ? C.coral : C.teal, null, 6) + tx(x + 40, 194 - v * 2.4, v + ' %', { a: 'middle', s: 13, w: 900 }); }); return S(470, 210, s); }
  M.desigualdad = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, sel('i', 'Caso', QUI.map(function (q, i) { return [i, q[0]]; }), 1), function (o) { var Q = QUI[+(o.i || 0)][1];
      return [{ vis: quint(Q, 0), txt: 'Ordenamos a toda la población de menor a mayor ingreso y la partimos en <b>5 grupos iguales</b> (quintiles), cada uno con el 20 % de las personas.' },
        { vis: quint(Q, 5), txt: 'Si todo fuera igualitario, cada quinto tendría el 20 % del ingreso. Acá el más pobre recibe el <b>' + Q[0] + ' %</b> y el más rico, el <b>' + Q[4] + ' %</b>.' },
        { vis: quint(Q, 5) + nota('Brecha: ' + Q[4] + ' ÷ ' + Q[0] + ' = ' + fmt(Math.round(Q[4] / Q[0] * 10) / 10) + ' veces'), txt: 'La <b>brecha</b> compara los extremos: el quinto más rico recibe ' + fmt(Math.round(Q[4] / Q[0] * 10) / 10) + ' veces más que el más pobre.' }]; });
  } };
  M.desigualdad_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = pick([4, 5, 6, 8, 10]), k = pick([3, 4, 5, 6, 8]); return { cons: 'En un país, el quinto más pobre recibe el <b>' + a + ' %</b> del ingreso y el más rico, el <b>' + a * k + ' %</b>. ¿Cuántas veces más recibe el más rico?', campos: [{ lab: 'Veces', v: k }], ayuda: 'Dividí el % del más rico por el % del más pobre.', bien: '¡Bien! ' + a * k + ' ÷ ' + a + ' = ' + k + ' veces.' }; });
  } };

  // 12) ORGANIZACIÓN DEL ESTADO: tres poderes en tres niveles
  var PODER = { nacional: [['Ejecutivo', 'Presidente y ministros', '🏛️'], ['Legislativo', 'Congreso: Diputados y Senado', '📜'], ['Judicial', 'Corte Suprema y jueces federales', '⚖️']], provincial: [['Ejecutivo', 'Gobernador', '🏛️'], ['Legislativo', 'Legislatura provincial', '📜'], ['Judicial', 'Superior Tribunal y jueces provinciales', '⚖️']], municipal: [['Ejecutivo', 'Intendente', '🏛️'], ['Legislativo', 'Concejo Deliberante', '📜'], ['Judicial', 'Juzgado de faltas', '⚖️']] };
  var FUN = { Ejecutivo: 'administra y ejecuta las leyes', Legislativo: 'hace las leyes', Judicial: 'resuelve conflictos aplicando las leyes' };
  function organi(nv, h) { var L = PODER[nv], s = rc(150, 10, 170, 36, C.claro, C.teal, 10) + tx(235, 33, 'Gobierno ' + nv, { a: 'middle', s: 12, w: 900 }); L.forEach(function (q, i) { if (i >= h) return; var x = 20 + i * 150; s += ln(235, 46, x + 65, 70, C.gris, 2) + rc(x, 70, 130, 110, '#fff', C.osc, 12) + em(x + 65, 92, q[2], 22) + tx(x + 65, 120, q[0], { a: 'middle', s: 12, w: 900, c: C.teal }) + txw(x + 65, 148, q[1], { a: 'middle', s: 10, w: 700 }, 20) + txw(x + 65, 200, FUN[q[0]], { a: 'middle', s: 9.5, c: C.coral }, 22); }); return S(470, 215, s); }
  M.estado = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('n', 'Nivel', [['nacional', 'Nacional'], ['provincial', 'Provincial'], ['municipal', 'Municipal']], p.nivel || 'nacional'), function (o) { var nv = o.n || 'nacional';
      return [{ vis: organi(nv, 0), txt: 'La Argentina es una república <b>federal</b>: hay gobierno nacional, provincial y municipal. Elegiste el nivel <b>' + nv + '</b>.' }].concat(PODER[nv].map(function (q, i) { return { vis: organi(nv, i + 1), txt: 'Poder <b>' + q[0] + '</b>: ' + q[1] + '. ' + FUN[q[0]][0].toUpperCase() + FUN[q[0]].slice(1) + '.' }; })).concat([{ vis: organi(nv, 3), txt: 'La <b>división de poderes</b> evita que una sola persona concentre todo el poder: cada uno controla a los otros.' }]); });
  } };
  M.estado_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = []; Object.keys(PODER).forEach(function (nv) { PODER[nv].forEach(function (q) { it.push([q[1], q[0]]); }); }); it = mezclar(it).slice(0, 6); return { tit: '¿A qué poder pertenece cada uno?', cajas: ['Ejecutivo', 'Legislativo', 'Judicial'], items: it.map(function (q, i) { return { v: 'p' + i, t: q[0], c: ['Ejecutivo', 'Legislativo', 'Judicial'].indexOf(q[1]) }; }) }; }); otro(el);
  } };

  // 13) CÓMO SE HACE UNA LEY: el proyecto viaja entre las cámaras
  var LEY = [['Proyecto', 'Lo presenta un legislador, el Poder Ejecutivo o los ciudadanos (iniciativa popular).', '📄', 40, 120], ['Cámara de origen', 'Lo estudian las comisiones y se vota en el recinto.', '🏛️', 140, 60], ['Cámara revisora', 'La otra cámara lo revisa: lo aprueba, lo modifica o lo rechaza.', '🏛️', 260, 60], ['Sanción', 'Aprobado por las dos cámaras, el Congreso sanciona la ley.', '✅', 360, 120], ['Promulgación o veto', 'El Poder Ejecutivo la promulga (o la veta, total o parcialmente).', '✍️', 260, 190], ['Publicación', 'Se publica en el Boletín Oficial y empieza a regir.', '📰', 140, 190]];
  function leyDib(h) { var s = ''; LEY.forEach(function (q, i) { if (i >= h) return; s += (i ? fl(LEY[i - 1][3] + (q[3] > LEY[i - 1][3] ? 30 : q[3] < LEY[i - 1][3] ? -30 : 0), LEY[i - 1][4] + (q[4] > LEY[i - 1][4] ? 22 : q[4] < LEY[i - 1][4] ? -22 : 0), q[3] - (q[3] > LEY[i - 1][3] ? 30 : q[3] < LEY[i - 1][3] ? -30 : 0), q[4] - (q[4] > LEY[i - 1][4] ? 22 : q[4] < LEY[i - 1][4] ? -22 : 0), C.teal, 2.5) : '') + ci(q[3], q[4], 24, i === h - 1 ? '#FFF3C4' : '#fff', i === h - 1 ? C.coral : C.teal) + em(q[3], q[4], q[2], 20) + txw(q[3], q[4] + 40, q[0], { a: 'middle', s: 10.5, w: 900 }, 16); }); return S(470, 240, s); }
  M.ley = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, '', function () { return [{ vis: leyDib(0), txt: 'Las leyes las hace el <b>Congreso</b>, que tiene dos cámaras: Diputados y Senado. Sigamos el camino de un proyecto.' }].concat(LEY.map(function (q, i) { return { vis: leyDib(i + 1), txt: '<b>' + q[0] + '</b>: ' + q[1] }; })); });
  } };
  M.ley_x = { tipo: 'ejercicio', render: function (el, p, api) {
    ordenar(el, api, function () { return { cons: 'Ordená el camino de una ley, del principio al final.', items: LEY.map(function (q) { return q[2] + ' ' + q[0]; }), ayuda: 'Primero el proyecto; después las dos cámaras; al final el Ejecutivo y el Boletín Oficial.' }; });
  } };

  // 14) REPARTO DE BANCAS (sistema D'Hondt)
  function dhondt(V, n) { var Q = []; V.forEach(function (v, i) { for (var d = 1; d <= n; d++) Q.push({ p: i, d: d, q: v / d }); }); Q.sort(function (a, b) { return b.q - a.q; }); var g = Q.slice(0, n), ban = V.map(function () { return 0; }); g.forEach(function (x) { ban[x.p]++; }); return { g: g, ban: ban }; }
  var PART = ['Partido A', 'Partido B', 'Partido C', 'Partido D'], PCOL = ['#c2416b', '#2a7ab8', '#3c8d2f', '#C29A1E'];
  function tablaDH(V, n, marcar) { var r = dhondt(V, n), s = tx(110, 22, '÷1', { a: 'middle', s: 10.5, w: 900 }); for (var d = 1; d <= n; d++) s += tx(70 + d * 70, 22, '÷' + d, { a: 'middle', s: 10.5, w: 900 });
    V.forEach(function (v, i) { var y = 46 + i * 30; s += tx(10, y + 4, PART[i], { s: 11, w: 900, c: PCOL[i] }); for (var d = 1; d <= n; d++) { var gana = marcar && r.g.some(function (x) { return x.p === i && x.d === d; }); s += rc(42 + d * 70, y - 13, 60, 22, gana ? PCOL[i] : '#fff', C.gris, 5) + tx(72 + d * 70, y + 3, fmt(Math.round(v / d)), { a: 'middle', s: 10.5, w: 800, c: gana ? '#fff' : C.osc }); } });
    return S(470, 60 + V.length * 30, s.replace(/<text x="110" y="22"[^>]*>÷1<\/text>/, '')); }
  M.dhondt = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'Votos del Partido A', 1000, 60000, 1000, 42000) + ctrl('b', 'Votos del Partido B', 1000, 60000, 1000, 31000) + ctrl('c', 'Votos del Partido C', 1000, 60000, 1000, 15000) + ctrl('d', 'Votos del Partido D', 1000, 60000, 1000, 8000) + ctrl('n', 'Bancas a repartir', 3, 5, 1, 5), function (o) { var V = [o.a, o.b, o.c, o.d], n = o.n || 5, r = dhondt(V, n);
      return [{ vis: S(470, 140, V.map(function (v, i) { return tx(10, 30 + i * 30, PART[i], { s: 11, w: 900, c: PCOL[i] }) + rc(100, 18 + i * 30, v / 60000 * 300, 18, PCOL[i], null, 4) + tx(106 + v / 60000 * 300, 32 + i * 30, fmt(v) + ' votos', { s: 10.5, w: 800 }); }).join('')), txt: 'Hay <b>' + n + ' bancas</b> para repartir según los votos. En la Argentina, Diputados usa el <b>sistema D\'Hondt</b>.' },
        { vis: tablaDH(V, n, false), txt: 'Dividimos los votos de cada partido por 1, por 2, por 3… hasta la cantidad de bancas.' },
        { vis: tablaDH(V, n, true), txt: 'Marcamos los <b>' + n + ' cocientes más grandes</b>: cada uno es una banca.' },
        { vis: tablaDH(V, n, true) + nota(PART.map(function (q, i) { return q.replace('Partido ', '') + ': ' + r.ban[i]; }).join(' · ')), txt: 'Resultado: ' + PART.map(function (q, i) { return q + ' ' + r.ban[i]; }).join(', ') + '. Es un sistema <b>proporcional</b>, aunque favorece un poco a los partidos grandes.' }]; });
  } };
  M.dhondt_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var V = [R(30, 60) * 1000, R(15, 35) * 1000, R(5, 15) * 1000], n = pick([3, 4, 5]), r = dhondt(V, n); return { cons: 'Se reparten <b>' + n + ' bancas</b> por D\'Hondt. Votos: A ' + fmt(V[0]) + ', B ' + fmt(V[1]) + ', C ' + fmt(V[2]) + '. ¿Cuántas bancas obtiene cada partido?', campos: [{ lab: 'A', v: r.ban[0] }, { lab: 'B', v: r.ban[1] }, { lab: 'C', v: r.ban[2] }], ayuda: 'Dividí los votos de cada uno por 1, 2, 3… y quedate con los ' + n + ' cocientes más grandes.', bien: '¡Bien! A ' + r.ban[0] + ', B ' + r.ban[1] + ', C ' + r.ban[2] + '.' }; });
  } };

  // 15) ANÁLISIS DE FUENTES: primaria o secundaria; autor, fecha, intención (textos de ejemplo escritos para la lección)
  var FUE = [{ nombre: 'Carta de un soldado (texto de ejemplo)', tipo: 'primaria', doc: 'Mendoza, 1816. Querida madre: seguimos preparando mulas y víveres para cruzar la cordillera. Hace mucho frío, pero el general nos dice que la libertad de toda América depende de nosotros…', autor: 'un soldado del Ejército de los Andes', fecha: '1816, el mismo tiempo de los hechos', intencion: 'contar a su familia cómo vivía la campaña' },
    { nombre: 'Página de un libro escolar actual', tipo: 'secundaria', doc: 'En 1817, el Ejército de los Andes cruzó la cordillera en una de las campañas militares más difíciles de la historia americana. Los historiadores coinciden en que la logística fue clave…', autor: 'una historiadora', fecha: 'hoy, mucho después de los hechos', intencion: 'explicar los hechos a estudiantes, a partir de otras fuentes' },
    { nombre: 'Aviso de un diario de 1910 (texto de ejemplo)', tipo: 'primaria', doc: '¡Gran liquidación por el Centenario! Sombreros y bastones a precios nunca vistos. Calle Florida, frente a la plaza. Visite nuestra tienda.', autor: 'una tienda de Buenos Aires', fecha: '1910, durante los festejos', intencion: 'vender productos: muestra costumbres y modas de la época' }];
  function docDib(F, fase) { var s = '<div class="soc-doc' + (F.tipo === 'primaria' ? ' viejo' : '') + '"><b>' + F.nombre + '</b><p>' + F.doc + '</p>' + (fase >= 1 ? '<div class="soc-et"><span>🖋️ Autor: ' + F.autor + '</span>' + (fase >= 2 ? '<span>📅 Cuándo: ' + F.fecha + '</span>' : '') + (fase >= 3 ? '<span>🎯 Para qué: ' + F.intencion + '</span>' : '') + '</div>' : '') + '</div>'; return s; }
  M.fuente = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, sel('i', 'Fuente', FUE.map(function (f, i) { return [i, f.nombre]; }), 0), function (o) { var F = FUE[+(o.i || 0)];
      return [{ vis: docDib(F, 0), txt: 'Una <b>fuente histórica</b> es cualquier rastro del pasado que nos permite conocerlo. La leemos como detectives.' }, { vis: docDib(F, 1), txt: '¿Quién la produjo? <b>' + F.autor[0].toUpperCase() + F.autor.slice(1) + '</b>.' }, { vis: docDib(F, 2), txt: '¿Cuándo? <b>' + F.fecha + '</b>.' }, { vis: docDib(F, 3), txt: '¿Para qué? Para <b>' + F.intencion + '</b>.' },
        { vis: docDib(F, 3) + nota('Fuente ' + F.tipo.toUpperCase()), txt: F.tipo === 'primaria' ? 'Es una fuente <b>primaria</b>: se produjo en la época que estudiamos.' : 'Es una fuente <b>secundaria</b>: alguien la escribió después, interpretando otras fuentes.' }]; });
  } };
  var FUE2 = [['Una foto de la Plaza de Mayo en 1910', 'primaria'], ['Un documental hecho este año sobre la Revolución de Mayo', 'secundaria'], ['El acta de la Declaración de la Independencia', 'primaria'], ['Un artículo de Wikipedia sobre San Martín', 'secundaria'], ['Una vasija hecha por los diaguitas', 'primaria'], ['Un libro de historia escrito en 2015', 'secundaria'], ['El diario de viaje de un explorador del siglo XVI', 'primaria'], ['Un mapa actual que muestra las rutas de la conquista', 'secundaria']];
  M.fuente_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = mezclar(FUE2.slice()).slice(0, 6); return { tit: '¿Fuente primaria (de la época) o secundaria (posterior)?', cajas: ['Primaria', 'Secundaria'], items: it.map(function (q, i) { return { v: 'f' + i, t: q[0], c: q[1] === 'primaria' ? 0 : 1 }; }) }; }); otro(el);
  } };

  // 16) ÁRBOL DE CAUSAS Y CONSECUENCIAS
  var PROC = { mayo: ['Revolución de Mayo (1810)', [['La Corona española cayó en manos de Napoleón', 'política'], ['Los criollos querían más participación en el gobierno', 'social'], ['El monopolio comercial limitaba el comercio', 'económica'], ['Ideas de la Ilustración y de la Revolución Francesa', 'política']], ['Primera Junta de gobierno', 'Guerras de independencia', 'Libre comercio con otros países']],
    industrial: ['Revolución Industrial', [['Nuevas máquinas como la de vapor', 'tecnológica'], ['Capitales acumulados con el comercio', 'económica'], ['Campesinos que migraron a las ciudades', 'social'], ['Carbón y hierro abundantes en Inglaterra', 'económica']], ['Fábricas y producción en serie', 'Crecimiento de las ciudades', 'Nueva clase obrera']],
    crisis29: ['Crisis de 1929', [['Especulación en la bolsa de Nueva York', 'económica'], ['Superproducción que no se vendía', 'económica'], ['Créditos fáciles que no se podían pagar', 'económica']], ['Quiebra de bancos y empresas', 'Desocupación masiva', 'Caída del comercio mundial']] };
  var TCOL = { 'política': C.azul, social: C.verde, 'económica': C.sol, 'tecnológica': C.lila };
  function arbol(Pr, h) { var s = rc(150, 104, 170, 40, C.coral, null, 12) + txw(235, 128, Pr[0], { a: 'middle', s: 11.5, w: 900, c: '#fff' }, 26), cs = Pr[1], co = Pr[2];
    cs.forEach(function (c, i) { if (i >= h) return; var x = 10 + i * (450 / cs.length), w = 450 / cs.length - 8; s += rc(x, 6, w, 70, '#fff', TCOL[c[1]], 10, ' stroke-width="3"') + lineas(r1(x + w / 2), 34, c[0], { s: 8.5 }, Math.floor(w / 5.2)) + tx(x + w / 2, 70, c[1], { a: 'middle', s: 9, w: 900, c: TCOL[c[1]] }) + fl(x + w / 2, 76, 235, 102, TCOL[c[1]], 2); });
    if (h > cs.length) co.forEach(function (c, i) { var x = 15 + i * 150; s += fl(235, 146, x + 65, 176, C.coral, 2) + rc(x, 178, 130, 44, '#FFF3C4', C.coral, 10) + txw(x + 65, 204, c, { a: 'middle', s: 9.5, w: 800 }, 22); });
    return S(470, 230, s); }
  M.causas = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Proceso', Object.keys(PROC).map(function (k) { return [k, PROC[k][0]]; }), p.proceso || 'mayo'), function (o) { var Pr = PROC[o.i || 'mayo'], P = [{ vis: arbol(Pr, 0), txt: 'Los procesos históricos tienen <b>muchas causas</b>, de distinto tipo. Analizamos: <b>' + Pr[0] + '</b>.' }];
      Pr[1].forEach(function (c, i) { P.push({ vis: arbol(Pr, i + 1), txt: 'Causa <b>' + c[1] + '</b>: ' + c[0].toLowerCase() + '.' }); });
      P.push({ vis: arbol(Pr, 99), txt: 'Y trae <b>consecuencias</b>: ' + Pr[2].join(', ').toLowerCase() + '.' }); return P; });
  } };
  M.causas_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = []; Object.keys(PROC).forEach(function (k) { PROC[k][1].forEach(function (c) { if (c[1] !== 'tecnológica') it.push(c); }); }); it = mezclar(it).slice(0, 6); return { tit: '¿Qué tipo de causa es cada una?', cajas: ['Política', 'Económica', 'Social'], items: it.map(function (c, i) { return { v: 'c' + i, t: c[0], c: ['política', 'económica', 'social'].indexOf(c[1]) }; }) }; }); otro(el);
  } };

  // 17) PIRÁMIDES SOCIALES: estamentos feudales y sociedad colonial
  var SOCS = { feudal: ['Sociedad feudal', [['Rey', 'gobierna, pero depende de los nobles'], ['Nobleza y alto clero', 'dueños de la tierra; guerrean y rezan'], ['Caballeros y bajo clero', 'protegen y sirven a los señores'], ['Campesinos y siervos', 'trabajan la tierra y pagan tributos']]],
    colonial: ['Sociedad colonial hispanoamericana', [['Españoles peninsulares', 'altos cargos de gobierno y de la Iglesia'], ['Criollos', 'hijos de españoles nacidos en América; comerciantes y hacendados'], ['Mestizos y castas', 'artesanos, peones, pequeños comerciantes'], ['Indígenas', 'tributo y trabajo obligatorio (mita, encomienda)'], ['Africanos esclavizados', 'sin libertad; trabajo forzado']]] };
  function piraSoc(L, h) { var n = L.length, s = ''; L.forEach(function (q, i) { if (i >= h) return; var y = 15 + i * (200 / n), w = 90 + i * (330 / n), hh2 = 200 / n - 4; s += '<path d="M' + r1(235 - w / 2) + ',' + r1(y + hh2) + ' L' + r1(235 - w / 2 + 14) + ',' + r1(y) + ' L' + r1(235 + w / 2 - 14) + ',' + r1(y) + ' L' + r1(235 + w / 2) + ',' + r1(y + hh2) + ' Z" fill="' + ['#B39DDB', '#9FA8DA', '#90CAF9', '#A5D6A7', '#FFE082'][i] + '" stroke="#fff" stroke-width="2"/>' + tx(235, y + hh2 / 2 + 4, q[0], { a: 'middle', s: 11, w: 900 }); }); return S(470, 225, s + tx(462, 30, 'más privilegios ▲', { a: 'end', s: 9.5, c: C.teal, w: 800 }) + tx(462, 215, 'más trabajo ▼', { a: 'end', s: 9.5, c: C.teal, w: 800 })); }
  M.piramide_social = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Sociedad', [['feudal', 'Feudal'], ['colonial', 'Colonial']], p.sociedad || 'feudal'), function (o) { var Sc = SOCS[o.i || 'feudal'], L = Sc[1], P = [{ vis: piraSoc(L, 0), txt: '<b>' + Sc[0] + '</b>: una sociedad <b>jerárquica</b>, donde el lugar de cada uno depende sobre todo del nacimiento.' }];
      L.forEach(function (q, i) { P.push({ vis: piraSoc(L, i + 1), txt: '<b>' + q[0] + '</b>: ' + q[1] + '.' }); });
      P.push({ vis: piraSoc(L, 99), txt: 'Pocos arriba con muchos privilegios; muchos abajo que sostienen a todos con su trabajo. Era casi imposible cambiar de grupo.' }); return P; });
  } };
  M.piramide_social_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    ordenar(el, api, function () { var k = rot(2, u) ? 'colonial' : 'feudal', Sc = SOCS[k]; return { cons: '<b>' + Sc[0] + '</b>: ordená los grupos desde el de <b>más privilegios</b> hasta el de menos.', items: Sc[1].map(function (q) { return q[0]; }), ayuda: 'Arriba, los que gobernaban y tenían la tierra; abajo, los que trabajaban.' }; });
  } };

  // 18) MIGRACIONES: origen, destino y factores de expulsión y atracción
  var MIG = { europea: ['Inmigración europea a la Argentina (1880-1930)', 'Italia y España', 'Argentina', [['Pobreza y falta de tierras en el campo', 'exp'], ['Guerras y persecuciones', 'exp'], ['Demanda de trabajadores para el campo y las ciudades', 'atr'], ['Leyes que promovían la inmigración', 'atr']]],
    regional: ['Migración regional actual', 'Paraguay, Bolivia, Perú y Venezuela', 'Argentina', [['Crisis económicas y desempleo', 'exp'], ['Inestabilidad política', 'exp'], ['Educación y salud públicas', 'atr'], ['Redes de familiares que ya viven allí', 'atr']]],
    campo: ['Migración del campo a la ciudad', 'Zonas rurales', 'Grandes ciudades', [['Mecanización del campo: menos trabajo', 'exp'], ['Pocos servicios en los pueblos', 'exp'], ['Más empleos en industria y servicios', 'atr'], ['Acceso a escuelas y hospitales', 'atr']]] };
  function migDib(m, h) { var s = rc(20, 70, 130, 70, '#FCE4EC', C.rosa, 14) + txw(85, 108, m[1], { a: 'middle', s: 11, w: 900 }, 18) + rc(320, 70, 130, 70, '#E8F5E9', C.verde, 14) + txw(385, 108, m[2], { a: 'middle', s: 11, w: 900 }, 18);
    if (h >= 1) s += '<path d="M150,105 C220,40 250,40 320,105" fill="none" stroke="' + C.teal + '" stroke-width="5" marker-end="url(#natfl)"/>' + em(235, 60, '🧳', 22);
    var ex = m[3].filter(function (f) { return f[1] === 'exp'; }), at = m[3].filter(function (f) { return f[1] === 'atr'; });
    if (h >= 2) ex.forEach(function (f, i) { s += txw(85, 170 + i * 34, '⬅ ' + f[0], { a: 'middle', s: 9.5, w: 800, c: C.rosa }, 26); });
    if (h >= 3) at.forEach(function (f, i) { s += txw(385, 170 + i * 34, f[0] + ' ➡', { a: 'middle', s: 9.5, w: 800, c: C.verde }, 26); });
    return S(470, 240, s); }
  M.migraciones = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Caso', Object.keys(MIG).map(function (k) { return [k, MIG[k][0]]; }), p.caso || 'europea'), function (o) { var m = MIG[o.i || 'europea'];
      return [{ vis: migDib(m, 0), txt: '<b>' + m[0] + '</b>. Toda migración tiene un lugar de <b>origen</b> y uno de <b>destino</b>.' }, { vis: migDib(m, 1), txt: 'Las personas se trasladan para vivir en otro lugar: emigran desde el origen e inmigran en el destino.' },
        { vis: migDib(m, 2), txt: '<b>Factores de expulsión</b>: lo que empuja a irse del origen.' }, { vis: migDib(m, 3), txt: '<b>Factores de atracción</b>: lo que hace elegir el destino.' }]; });
  } };
  M.migraciones_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = []; Object.keys(MIG).forEach(function (k) { MIG[k][3].forEach(function (f) { it.push(f); }); }); it = mezclar(it).slice(0, 6); return { tit: '¿Factor de expulsión (empuja a irse) o de atracción (atrae al destino)?', cajas: ['Expulsión', 'Atracción'], items: it.map(function (f, i) { return { v: 'm' + i, t: f[0], c: f[1] === 'exp' ? 0 : 1 }; }) }; }); otro(el);
  } };

  // 19) BALANZA DE ARGUMENTOS
  var DEB = { uniforme: ['¿Tiene que ser obligatorio el uniforme escolar?', [['Evita la competencia por las marcas', 'favor', 2], ['Da sentido de pertenencia', 'favor', 1], ['Limita la expresión personal', 'contra', 2], ['Es un gasto extra para las familias', 'contra', 2]]],
    celulares: ['¿Hay que prohibir los celulares en el aula?', [['Mejora la concentración', 'favor', 2], ['Reduce el ciberacoso en horario escolar', 'favor', 1], ['Son útiles para investigar', 'contra', 2], ['Hay que enseñar a usarlos, no prohibirlos', 'contra', 2]]],
    voto16: ['¿Está bien que se pueda votar desde los 16 años?', [['Amplía la participación democrática', 'favor', 2], ['Los jóvenes ya tienen responsabilidades', 'favor', 1], ['Pueden tener poca información', 'contra', 1], ['Es fácil influir en ellos', 'contra', 1]]] };
  function balanza(D, h) { var A = D[1].slice(0, h), f = A.filter(function (a) { return a[1] === 'favor'; }).reduce(function (s, a) { return s + a[2]; }, 0), c = A.filter(function (a) { return a[1] === 'contra'; }).reduce(function (s, a) { return s + a[2]; }, 0), ang = Math.max(-14, Math.min(14, (c - f) * 4)), r = ang * Math.PI / 180;
    var xl = 235 - 150 * Math.cos(r), yl = 70 - 150 * Math.sin(r), xr = 235 + 150 * Math.cos(r), yr = 70 + 150 * Math.sin(r), s = '<polygon points="235,70 215,215 255,215" fill="#B0BEC5"/>' + ln(xl, yl, xr, yr, C.osc, 5) + ln(xl, yl, xl, yl + 30, C.osc, 1.5) + ln(xr, yr, xr, yr + 30, C.osc, 1.5) + rc(xl - 70, yl + 30, 140, 8, C.verde, null, 3) + rc(xr - 70, yr + 30, 140, 8, C.rosa, null, 3) + tx(xl, yl - 10, 'A FAVOR', { a: 'middle', s: 11, w: 900, c: C.verde }) + tx(xr, yr - 10, 'EN CONTRA', { a: 'middle', s: 11, w: 900, c: C.rosa });
    var kf = 0, kc = 0; A.forEach(function (a) { var izq = a[1] === 'favor', k = izq ? kf++ : kc++; s += txw((izq ? xl : xr), (izq ? yl : yr) + 56 + k * 26, a[0] + ' (' + '●'.repeat(a[2]) + ')', { a: 'middle', s: 9, w: 700 }, 26); });
    return S(470, 240, s); }
  M.balanza_argumentos = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('i', 'Debate', Object.keys(DEB).map(function (k) { return [k, DEB[k][0]]; }), p.debate || 'uniforme'), function (o) { var D = DEB[o.i || 'uniforme'], P = [{ vis: balanza(D, 0), txt: 'Pregunta del debate: <b>' + D[0] + '</b> Vamos a pesar los argumentos.' }];
      D[1].forEach(function (a, i) { P.push({ vis: balanza(D, i + 1), txt: 'Argumento <b>' + (a[1] === 'favor' ? 'a favor' : 'en contra') + '</b>: ' + a[0].toLowerCase() + '. Peso: ' + a[2] + ' (según qué tan sólido y bien fundamentado es).' }); });
      P.push({ vis: balanza(D, 9), txt: 'Pensar críticamente es pesar los argumentos de los dos lados <b>antes</b> de tomar posición, y poder explicar por qué uno pesa más.' }); return P; });
  } };
  M.balanza_argumentos_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var D = DEB[pick(Object.keys(DEB))]; return { tit: D[0] + ' Ubicá cada argumento.', cajas: ['A favor', 'En contra'], items: mezclar(D[1].slice()).map(function (a, i) { return { v: 'a' + i, t: a[0], c: a[1] === 'favor' ? 0 : 1 }; }) }; }); otro(el);
  } };

  // 20) DILEMA ÉTICO: tres miradas (consecuencias, deber, virtud)
  var DIL = [['La billetera', 'Encontrás una billetera con mucho dinero y el documento del dueño. Nadie te vio.', ['Devolverla trae más bienestar: el dueño la necesita y se evita un daño.', 'Hay que devolverla porque es lo correcto, aunque nadie lo sepa: no se toma lo ajeno.', 'Una persona honesta la devuelve: así se forma un buen carácter.']],
    ['El examen', 'Un amigo te pide que le pases las respuestas en el examen.', ['Si lo ayudo, aprueba hoy, pero no aprende y puede perjudicarse después.', 'Copiar es engañar y no se puede querer que todos lo hagan.', 'Un buen amigo lo ayuda a estudiar antes, no a hacer trampa.']],
    ['El secreto', 'Una amiga te contó en secreto que alguien la está molestando en redes.', ['Contarle a un adulto puede evitar un daño mayor.', 'Prometí guardar el secreto, pero el deber de proteger a otro es más fuerte.', 'Ser leal también es cuidar a la amiga, aunque cueste.']]];
  var TEO = [['Ética de las consecuencias (utilitarismo)', 'buscar el mayor bienestar para la mayoría', '⚖️'], ['Ética del deber (Kant)', 'actuar por deber, siguiendo reglas que valgan para todos', '📏'], ['Ética de la virtud (Aristóteles)', 'actuar como lo haría una persona buena y prudente', '🌱']];
  M.dilema = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, sel('i', 'Dilema', DIL.map(function (d, i) { return [i, d[0]]; }), 0), function (o) { var D = DIL[+(o.i || 0)], P = [{ vis: card('🤔 <b>' + D[0] + '</b>: ' + D[1]), txt: 'Un <b>dilema ético</b>: una situación en la que hay que decidir qué es lo correcto.' }];
      TEO.forEach(function (t, i) { P.push({ vis: card('🤔 ' + D[1]) + '<div class="soc-teo">' + TEO.slice(0, i + 1).map(function (q, j) { return '<div><b>' + q[2] + ' ' + q[0] + '</b><small>' + q[1] + '</small><em>«' + D[2][j] + '»</em></div>'; }).join('') + '</div>', txt: '<b>' + t[0] + '</b>: ' + t[1] + '.' }); });
      P.push({ vis: card('🤔 ' + D[1]), txt: 'Las tres miradas pueden llegar a la misma decisión por <b>razones distintas</b>. Argumentar es explicar desde qué mirada decidimos.' }); return P; });
  } };
  M.dilema_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    elegir(el, api, function () { var D = pick(DIL), k = rot(3, u); return { cons: 'Dilema «' + D[0].toLowerCase() + '»: ' + D[1] + ' ¿Desde qué mirada ética está este razonamiento?<br><b>«' + D[2][k] + '»</b>', ops: TEO.map(function (t) { return t[0]; }), ok: TEO[k][0], ayuda: '¿Habla de los resultados, de una regla o deber, o de qué haría una buena persona?' }; });
  } };

  // Piezas de dibujo que reusan las actividades de Sociales (js/actividades-soc.js). Solo dibujos y datos.
  N.soc = { grilla: grilla, CIU: CIU, mapaEsc: mapaEsc, reloj: reloj, hh: hh, piramide: piramide, PIR: PIR, dhondt: dhondt, leyDib: leyDib, LEY: LEY, piraSoc: piraSoc, SOCS: SOCS, lineas: lineas };

  var css = document.createElement('style');
  css.textContent = '.soc-doc{margin:6px auto;max-width:460px;padding:14px 16px;border:2px solid #d8c9a3;border-radius:6px;background:#fff;text-align:left;font-size:.95rem;line-height:1.5}.soc-doc.viejo{background:#FBF3DF;font-family:Georgia,serif}.soc-doc p{margin:6px 0}.soc-et{display:flex;flex-direction:column;gap:4px;margin-top:8px;font-family:inherit}.soc-et span{padding:4px 8px;border-radius:8px;background:#FFF3C4;font-weight:700;font-size:.88rem}' +
    '.soc-teo{display:grid;gap:8px;margin-top:6px}.soc-teo div{padding:8px 10px;border-radius:12px;background:#F3FBF7;border:2px solid #D7F0E9;text-align:left}.soc-teo small{display:block;color:#066A6E}.soc-teo em{display:block;margin-top:4px}';
  document.head.appendChild(css);
})();
