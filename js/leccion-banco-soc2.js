/* BANCO DE LA LECCIÓN INTERACTIVA · SOCIALES (parte 2): Geografía física, mapas históricos, comparación de períodos, Filosofía y Constitución.
   Mismo banco que js/leccion-banco*.js (SOLO lección). Cada ejemplo tiene un dibujo propio y es PASO A PASO; cada uno con su práctica (_x).
   Los datos de clima son valores aproximados de promedios, para aprender a leer el gráfico. */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h || !B._h.nat) return;
  var H = B._h, M = B.motores, N = H.nat, R = H.R, pick = H.pick, mezclar = H.mezclar, fmt = H.fmt;
  var escena = H.escena, respuesta = H.respuesta, cajas = H.cajas, C = N.C, S = N.S, tx = N.tx, txw = N.txw, ln = N.ln, fl = N.fl, ci = N.ci, rc = N.rc, em = N.em, sel = N.sel, otro = N.otro, elegir = N.elegir, ordenar = N.ordenar, tocar = N.tocar, rot = N.rot, nota = N.nota;
  function card(t, cls) { return '<p class="nat-card ' + (cls || '') + '">' + t + '</p>'; }

  // =====================================================================================
  // 1) RELIEVE: curvas de nivel y perfil topográfico
  // =====================================================================================
  var FORMAS = { cerro: { nom: 'Un cerro', h: function (x) { return 520 * Math.exp(-Math.pow((x - 0.5) / 0.2, 2)); }, cs: [[0.5, 0.5, 1]] },
    dos: { nom: 'Dos cerros y un valle', h: function (x) { return 480 * Math.exp(-Math.pow((x - 0.28) / 0.13, 2)) + 360 * Math.exp(-Math.pow((x - 0.74) / 0.11, 2)); }, cs: [[0.28, 0.5, 1], [0.74, 0.5, 0.75]] },
    asim: { nom: 'Ladera suave y ladera abrupta', h: function (x) { return x < 0.66 ? 500 * Math.pow(x / 0.66, 1.6) : 500 * Math.exp(-Math.pow((x - 0.66) / 0.09, 2)); }, cs: [[0.66, 0.5, 1]] } };
  function curvas(f, conCorte, puntos) { var s = rc(10, 10, 300, 200, '#F1F8E9', C.gris, 8), cols = ['#DCEDC8', '#C5E1A5', '#AED581', '#9CCC65', '#8BC34A'];
    for (var lv = 1; lv <= 5; lv++) { var alt = lv * 100, xs = []; for (var i = 0; i <= 300; i++) { var x = i / 300; if (f.h(x) >= alt) xs.push(x); }
      if (!xs.length) continue; var tramos = [], ini = xs[0], prev = xs[0]; xs.forEach(function (x) { if (x - prev > 0.01) { tramos.push([ini, prev]); ini = x; } prev = x; }); tramos.push([ini, prev]);
      tramos.forEach(function (t) { var cx = 10 + (t[0] + t[1]) / 2 * 300, rx = Math.max(4, (t[1] - t[0]) / 2 * 300); s += '<ellipse cx="' + N.r1(cx) + '" cy="110" rx="' + N.r1(rx) + '" ry="' + N.r1(Math.min(88, rx * 0.75)) + '" fill="' + cols[lv - 1] + '" stroke="#5D4037" stroke-width="1.4"/>' + tx(cx + rx * 0.72, 110 + Math.min(88, rx * 0.75) * 0.72 + 3, alt, { a: 'middle', s: 8.5, w: 800, c: '#5D4037' }); }); }
    if (conCorte) s += ln(10, 110, 310, 110, C.coral, 2.5, ' stroke-dasharray="6 4"') + tx(16, 104, 'A', { s: 13, w: 900, c: C.coral }) + tx(302, 104, 'B', { s: 13, w: 900, c: C.coral });
    (puntos || []).forEach(function (p) { s += ci(10 + p[0] * 300, 110, 3.5, C.coral); });
    return s; }
  function cortes(f) { var P = [], ant = 0; for (var i = 1; i <= 300; i++) { var x = i / 300, h = f.h(x), lv = Math.floor(h / 100), lv0 = Math.floor(f.h((i - 1) / 300) / 100); if (lv !== lv0) P.push([x, Math.max(lv, lv0) * 100]); } return P; }
  function perfil(f, hasta) { var s = rc(330, 10, 140, 200, '#fff', C.gris, 8) + ln(345, 190, 460, 190, C.osc, 1.5) + ln(345, 190, 345, 25, C.osc, 1.5); for (var k = 1; k <= 5; k++) { var y = 190 - k * 30; s += ln(342, y, 460, y, '#E0E0E0', 1) + tx(340, y + 3, k * 100, { a: 'end', s: 7.5 }); }
    var d = ''; for (var i = 0; i <= 100 * hasta; i++) { var x = i / 100; d += (i ? 'L' : 'M') + N.r1(345 + x * 115) + ',' + N.r1(190 - f.h(x) * 0.3); } if (hasta > 0) s += '<path d="' + d + '" fill="none" stroke="#6D4C41" stroke-width="2.5"/>';
    return s + tx(400, 205, 'perfil A → B', { a: 'middle', s: 9, w: 800 }) + tx(334, 20, 'm', { s: 8 }); }
  M.relieve = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var ks = Object.keys(FORMAS);
    escena(el, sel('f', 'Relieve', ks.map(function (k) { return [k, FORMAS[k].nom]; }), p.forma && FORMAS[p.forma] ? p.forma : 'cerro'), function (o) { var f = FORMAS[o.f] || FORMAS.cerro, pc = cortes(f), max = Math.round(Math.max.apply(null, Array.apply(null, Array(301)).map(function (_, i) { return f.h(i / 300); })));
      return [{ vis: S(480, 220, curvas(f) + perfil(f, 0)), txt: 'Un mapa topográfico muestra el relieve con <b>curvas de nivel</b>: cada línea une puntos de la misma altura. Acá van cada 100 m (la <b>equidistancia</b>).' },
        { vis: S(480, 220, curvas(f, true) + perfil(f, 0)), txt: 'Para ver el relieve "de costado" trazamos una línea de corte de <b>A a B</b>.' },
        { vis: S(480, 220, curvas(f, true, pc) + perfil(f, 0)), txt: 'Marcamos cada lugar donde la línea corta una curva: ' + pc.length + ' cortes, cada uno con su altura.' },
        { vis: S(480, 220, curvas(f, true, pc) + perfil(f, 1)), txt: 'Pasamos esas alturas a un gráfico y las unimos: es el <b>perfil topográfico</b>. Llega a unos ' + (Math.floor(max / 100) * 100) + ' m.' },
        { vis: S(480, 220, curvas(f, true, pc) + perfil(f, 1)), txt: 'Regla de lectura: donde las curvas están <b>juntas</b> la pendiente es fuerte (ladera abrupta); donde están <b>separadas</b>, suave.' }]; });
  } };
  M.relieve_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, ks = Object.keys(FORMAS);
    respuesta(el, api, function () { var f = FORMAS[ks[rot(ks.length, u)]], top = 0; for (var i = 0; i <= 300; i++) top = Math.max(top, Math.floor(f.h(i / 300) / 100) * 100);
      return { cons: 'Las curvas van cada 100 m. ¿Cuál es la <b>curva más alta</b> que corta la línea A–B?', html: S(330, 220, curvas(f, true, cortes(f))), campos: [{ lab: 'Altura:', v: top, un: 'm' }], ayuda: 'Contá las curvas desde afuera hacia adentro: 100, 200, 300…', bien: '¡Bien! ' + top + ' m.' }; }); otro(el);
  } };

  // =====================================================================================
  // 2) CLIMOGRAMA (valores aproximados)
  // =====================================================================================
  var CLI = [['Buenos Aires', [24.5, 23.5, 21.5, 17.5, 14, 11, 10.5, 12, 14, 17, 20, 23], [120, 120, 140, 110, 90, 60, 60, 65, 70, 120, 110, 110], 'templado húmedo', 'S'],
    ['Ushuaia', [9.5, 9, 7.5, 5, 2.5, 0.5, 0, 1.5, 3.5, 6, 7.5, 9], [50, 45, 50, 50, 45, 45, 40, 40, 35, 35, 40, 45], 'frío húmedo', 'S'],
    ['Manaos (Brasil)', [27, 27, 27, 27, 27.5, 27.5, 27.5, 28, 28.5, 28.5, 28, 27.5], [260, 290, 310, 290, 220, 110, 80, 60, 80, 110, 160, 220], 'cálido ecuatorial (selva)', 'S'],
    ['Mendoza', [25, 24, 21, 16, 12, 8, 8, 10, 13, 18, 21, 24], [30, 30, 25, 10, 8, 5, 8, 7, 12, 15, 20, 25], 'árido (seco)', 'S']];
  var MES = ['E', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'];
  function climo(c, paso) { var s = rc(40, 15, 380, 180, '#fff', C.gris, 4), T = c[1], P = c[2];
    for (var k = 0; k <= 5; k++) { var y = 195 - k * 30; s += ln(40, y, 420, y, '#EEE', 1) + tx(36, y + 3, k * 60, { a: 'end', s: 8, c: C.azul }) + tx(424, y + 3, k * 6, { s: 8, c: C.coral }); }
    s += tx(14, 12, 'mm', { s: 8.5, c: C.azul, w: 800 }) + tx(424, 12, '°C', { s: 8.5, c: C.coral, w: 800 });
    MES.forEach(function (m, i) { var x = 50 + i * 30.5; s += tx(x + 10, 208, m, { a: 'middle', s: 9, w: 800 }); if (paso >= 1) s += rc(x + 2, 195 - P[i] / 2, 18, P[i] / 2, '#64B5F6'); });
    if (paso >= 2) { var d = T.map(function (t, i) { return (i ? 'L' : 'M') + (60 + i * 30.5) + ',' + N.r1(195 - t * 5); }).join(' '); s += '<path d="' + d + '" fill="none" stroke="' + C.coral + '" stroke-width="3"/>' + T.map(function (t, i) { return ci(60 + i * 30.5, 195 - t * 5, 3, C.coral); }).join(''); }
    if (paso >= 3) { var mx = T.indexOf(Math.max.apply(null, T)), mn = T.indexOf(Math.min.apply(null, T)); s += tx(60 + mx * 30.5, 188 - T[mx] * 5, 'máx ' + fmt(T[mx]), { a: 'middle', s: 9, w: 900, c: C.coral }) + tx(60 + mn * 30.5, 210 - T[mn] * 5, 'mín ' + fmt(T[mn]), { a: 'middle', s: 9, w: 900, c: C.coral }); }
    return S(460, 215, s); }
  M.climograma = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('c', 'Lugar', CLI.map(function (c, i) { return [i, c[0]]; }), 0), function (o) { var c = CLI[+(o.c || 0)] || CLI[0], T = c[1], P = c[2], mx = Math.max.apply(null, T), mn = Math.min.apply(null, T), tot = P.reduce(function (a, b) { return a + b; }, 0);
      return [{ vis: climo(c, 0), txt: 'Un <b>climograma</b> resume el clima de un lugar en un año: los meses abajo, las lluvias (mm) a la izquierda y la temperatura (°C) a la derecha.' },
        { vis: climo(c, 1), txt: 'Las <b>barras azules</b> son las precipitaciones de cada mes. En ' + c[0] + ' suman unos <b>' + fmt(tot) + ' mm</b> al año.' },
        { vis: climo(c, 2), txt: 'La <b>línea roja</b> es la temperatura media de cada mes.' },
        { vis: climo(c, 3), txt: 'La <b>amplitud térmica</b> anual es la diferencia entre el mes más cálido y el más frío: ' + fmt(mx) + ' − ' + fmt(mn) + ' = <b>' + fmt(Math.round((mx - mn) * 10) / 10) + ' °C</b>.' },
        { vis: climo(c, 3) + nota('Valores aproximados de promedios.'), txt: 'Con la temperatura y las lluvias reconocemos el tipo de clima: <b>' + c[3] + '</b>. ' + (tot < 300 ? 'Llueve muy poco.' : mx - mn < 3 ? 'Hace calor todo el año y casi no cambia.' : mx < 12 ? 'Es frío todo el año.' : 'Tiene estaciones marcadas y lluvias repartidas.') }]; });
  } };
  M.climograma_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    if (p.modo === 'tipo') { elegir(el, api, function () { var c = CLI[rot(CLI.length, u)]; return { cons: '¿Qué tipo de clima muestra este climograma?', html: climo(c, 3), ops: CLI.map(function (x) { return x[3]; }), ok: c[3], ayuda: 'Mirá cuánto llueve (barras) y si la temperatura cambia mucho o poco.', bien: '¡Bien! Es ' + c[0] + '.' }; }); return; }
    respuesta(el, api, function () { var c = CLI[rot(CLI.length, u)], T = c[1], mx = Math.max.apply(null, T), mn = Math.min.apply(null, T); return { cons: 'Leé el climograma de <b>' + c[0] + '</b>: ¿cuál es la amplitud térmica anual?', html: climo(c, 3), campos: [{ lab: 'Amplitud:', v: Math.round((mx - mn) * 10) / 10, un: '°C', tol: 0.05 }], ayuda: 'Mes más cálido menos mes más frío: ' + fmt(mx) + ' − ' + fmt(mn) + '.', bien: '¡Bien!' }; }); otro(el);
  } };

  // =====================================================================================
  // 3) BIOMAS: paisaje, clima, vegetación y fauna
  // =====================================================================================
  var BIO = [['Selva', '#1B5E20', '#81C784', ['🌴', '🌳', '🌿'], ['🐒', '🦜', '🐆'], 'cálido y muy lluvioso todo el año', 'árboles altísimos en pisos, lianas y muchísimas especies', 'Selva misionera, Amazonia'],
    ['Desierto', '#F9A825', '#FFE082', ['🌵', '🪨'], ['🦎', '🐍', '🦂'], 'muy seco: llueve menos de 250 mm al año', 'cactus y arbustos con espinas que guardan agua', 'Atacama (Chile), Sahara'],
    ['Pastizal', '#7CB342', '#C5E1A5', ['🌾', '🌱'], ['🦌', '🐦', '🐄'], 'templado, con lluvias moderadas', 'pastos y casi sin árboles', 'Llanura pampeana'],
    ['Bosque templado', '#2E7D32', '#A5D6A7', ['🌲', '🌳', '🍄'], ['🦊', '🦉', '🦌'], 'templado o frío, con lluvias y nieve', 'árboles altos como lengas, coihues y pinos', 'Bosque andino patagónico'],
    ['Estepa', '#A1887F', '#D7CCC8', ['🌿', '🪨'], ['🐑', '🦙', '🦅'], 'frío, seco y ventoso', 'arbustos bajos y pastos duros, en matas', 'Meseta patagónica'],
    ['Tundra', '#90A4AE', '#ECEFF1', ['🌱', '🪨'], ['🦌', '🐻‍❄️', '🦊'], 'muy frío, con el suelo congelado gran parte del año', 'musgos, líquenes y plantas muy bajas', 'Norte de Canadá y Siberia']];
  function paisaje(b, n) { var s = rc(0, 0, 460, 200, b[2]) + rc(0, 150, 460, 50, b[1]); if (n >= 1) b[3].forEach(function (e, i) { for (var k = 0; k < 3; k++) s += em(30 + (i * 3 + k) * 47 % 400, 130 + (k % 2) * 16, e, 30); }); if (n >= 2) b[4].forEach(function (e, i) { s += em(90 + i * 130, 172, e, 30); }); return S(460, 200, s); }
  M.biomas = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('b', 'Bioma', BIO.map(function (b, i) { return [i, b[0]]; }), 0), function (o) { var b = BIO[+(o.b || 0)] || BIO[0];
      return [{ vis: paisaje(b, 0), txt: 'Un <b>bioma</b> es una gran región con un clima parecido, y por eso con plantas y animales parecidos. Empecemos por el clima de la <b>' + b[0].toLowerCase() + '</b>: ' + b[5] + '.' },
        { vis: paisaje(b, 1), txt: 'Ese clima decide la <b>vegetación</b>: ' + b[6] + '.' },
        { vis: paisaje(b, 2), txt: 'Y la vegetación decide la <b>fauna</b>: animales adaptados a ese lugar.' },
        { vis: paisaje(b, 2) + card('📍 Ejemplos: ' + b[7]), txt: 'Clima → vegetación → fauna: es una cadena. Si cambia el clima, cambia todo el bioma.' }]; });
  } };
  M.biomas_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var b = BIO[rot(BIO.length, u)]; return { cons: 'Clima: <b>' + b[5] + '</b>. Vegetación: <b>' + b[6] + '</b>. ¿Qué bioma es?', ops: mezclar([b[0]].concat(mezclar(BIO.filter(function (x) { return x !== b; })).slice(0, 2).map(function (x) { return x[0]; }))), ok: b[0], bien: '¡Sí! ' + b[0] + '. Por ejemplo: ' + b[7] + '.' }; });
  } };

  // =====================================================================================
  // 4) CUENCA HIDROGRÁFICA: partes del río y cursos
  // =====================================================================================
  var CUE = [['Naciente', 60, 40, 'donde nace el río, en lo alto (manantial, deshielo o lago)'], ['Afluente', 200, 70, 'un río más chico que desemboca en el principal'], ['Curso superior', 110, 70, 'mucha pendiente: el agua corre rápido y erosiona'], ['Curso medio', 240, 120, 'menos pendiente: el río transporta lo que arrastró'], ['Curso inferior', 360, 150, 'casi plano: el agua va lenta y deposita sedimentos'], ['Desembocadura', 430, 172, 'donde el río termina: en el mar, un lago u otro río'], ['Divisoria de aguas', 250, 22, 'las partes altas que separan una cuenca de otra']];
  function cuenca(marca, tap) { var s = rc(0, 0, 470, 210, '#F1F8E9') + '<path d="M20,30 Q140,5 250,18 T450,40 L460,200 L10,200 Z" fill="#E8F5E9" stroke="#8D6E63" stroke-width="2" stroke-dasharray="7 5"/>' + rc(400, 160, 70, 50, '#90CAF9') + tx(436, 205, 'mar', { a: 'middle', s: 9, w: 800, c: C.azul }) +
      '<path d="M60,40 C100,60 120,80 170,100 S300,140 360,150 S420,168 430,172" fill="none" stroke="#1E88E5" stroke-width="5"/>' + '<path d="M200,30 C210,50 205,60 200,70 S195,90 190,100" fill="none" stroke="#42A5F5" stroke-width="3"/>' + '<path d="M300,60 C310,90 320,120 330,145" fill="none" stroke="#42A5F5" stroke-width="3"/>' + em(60, 26, '⛰️', 22) + em(150, 22, '⛰️', 18);
    CUE.forEach(function (q, k) { if (tap) s += '<g data-t="' + q[0] + '" class="nat-tap">' + ci(q[1], q[2], 12, 'rgba(8,126,131,.15)', C.teal) + tx(q[1], q[2] + 4, k + 1, { a: 'middle', s: 10, w: 900 }) + '</g>'; else if (marca != null && k <= marca) s += ci(q[1], q[2], 5, k === marca ? C.coral : C.teal) + tx(q[1] + (q[1] > 380 ? -8 : 8), q[2] - 8, q[0], { a: q[1] > 380 ? 'end' : 'start', s: 10, w: 900, c: k === marca ? C.coral : C.osc }); });
    return S(470, 210, s); }
  M.cuenca = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, '', function () { return [{ vis: cuenca(null), txt: 'Una <b>cuenca hidrográfica</b> es todo el territorio cuyas aguas (lluvia, arroyos, ríos) van a parar a un mismo río principal.' }].concat(CUE.map(function (q, k) { return { vis: cuenca(k), txt: '<b>' + q[0] + '</b>: ' + q[3] + '.' }; })); });
  } };
  M.cuenca_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    tocar(el, api, function () { var q = CUE[rot(CUE.length, u)]; return { cons: 'Tocá el número de: <b>' + q[0] + '</b> (' + q[3] + ').', svg: cuenca(null, true), ok: q[0], bien: '¡Sí! ' + q[0] + '.' }; });
  } };

  // =====================================================================================
  // 5) PLACAS TECTÓNICAS: bordes y lo que producen
  // =====================================================================================
  var PLA = { convergente: ['Convergente', 'las placas chocan: la más pesada (oceánica) se hunde debajo de la otra (subducción)', 'se forman cordilleras y volcanes, y hay sismos', 'La placa de Nazca se hunde bajo la Sudamericana: así se levantó la cordillera de los Andes'], divergente: ['Divergente', 'las placas se separan y sube magma desde abajo', 'se forma corteza nueva: dorsales en el fondo del océano y valles de rift', 'En el medio del océano Atlántico, América y África se separan unos centímetros por año'], transformante: ['Transformante', 'las placas se deslizan de costado, una al lado de la otra', 'no se crea ni se destruye corteza, pero hay sismos fuertes', 'La falla de San Andrés, en California (Estados Unidos)'] };
  function placas(t, paso) { var s = rc(0, 0, 460, 200, '#E3F2FD') + rc(0, 140, 460, 60, '#FF8A65');
    if (t === 'convergente') { s += '<path d="M0,95 L230,95 L300,175 L280,180 L215,110 L0,110 Z" fill="#78909C"/>' + '<path d="M230,90 L460,90 L460,120 L250,120 Z" fill="#A1887F"/>' + rc(0, 80, 230, 15, '#64B5F6'); if (paso >= 1) s += fl(60, 70, 140, 70, C.osc, 4) + fl(420, 70, 340, 70, C.osc, 4); if (paso >= 2) s += '<path d="M250,90 L290,30 L330,90 Z" fill="#8D6E63"/>' + em(290, 26, '🌋', 26) + em(200, 130, '💥', 18); }
    else if (t === 'divergente') { s += rc(0, 95, 210, 25, '#78909C') + rc(250, 95, 210, 25, '#78909C') + rc(0, 80, 460, 15, '#64B5F6'); if (paso >= 1) s += fl(190, 70, 100, 70, C.osc, 4) + fl(270, 70, 360, 70, C.osc, 4); if (paso >= 2) s += '<path d="M210,140 Q230,100 250,140" fill="#FF7043"/>' + '<path d="M215,95 L230,72 L245,95 Z" fill="#6D4C41"/>' + fl(230, 170, 230, 125, '#BF360C', 3); }
    else { s += rc(0, 90, 460, 30, '#A1887F') + ln(230, 70, 230, 140, C.osc, 2, ' stroke-dasharray="6 4"'); if (paso >= 1) s += fl(200, 80, 120, 80, C.osc, 4) + fl(260, 130, 340, 130, C.osc, 4); if (paso >= 2) s += em(230, 105, '💥', 22) + em(300, 70, '🏚️', 22); }
    return S(460, 200, s + tx(10, 194, 'manto (roca caliente)', { s: 9, w: 800, c: '#fff' })); }
  M.placas = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var ks = Object.keys(PLA);
    escena(el, sel('t', 'Borde', ks.map(function (k) { return [k, PLA[k][0]]; }), p.borde && PLA[p.borde] ? p.borde : 'convergente'), function (o) { var k = PLA[o.t] ? o.t : 'convergente', q = PLA[k];
      return [{ vis: placas(k, 0), txt: 'La capa de afuera de la Tierra está partida en <b>placas</b> que flotan sobre el manto y se mueven unos centímetros por año.' }, { vis: placas(k, 1), txt: 'Borde <b>' + q[0].toLowerCase() + '</b>: ' + q[1] + '.' }, { vis: placas(k, 2), txt: 'Resultado: ' + q[2] + '.' }, { vis: placas(k, 2) + card('📍 ' + q[3]), txt: 'Un caso real. Por eso los volcanes y los sismos se concentran en los bordes de las placas.' }]; });
  } };
  M.placas_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, ks = Object.keys(PLA);
    elegir(el, api, function () { var k = ks[rot(ks.length, u)]; return { cons: '¿Qué tipo de borde de placas es?', html: placas(k, 2), ops: ks.map(function (x) { return PLA[x][0]; }), ok: PLA[k][0], ayuda: 'Mirá las flechas: ¿se acercan, se separan o pasan de costado?', bien: '¡Sí! ' + PLA[k][2] + '.' }; });
  } };

  // =====================================================================================
  // 6) MAPA TEMÁTICO (coroplético): datos → rangos → colores → lectura
  // =====================================================================================
  var REG = [[20, 20, 110, 70], [130, 20, 120, 60], [250, 20, 90, 90], [20, 90, 80, 80], [100, 80, 110, 70], [210, 110, 130, 60], [20, 170, 140, 40], [160, 150, 90, 60], [250, 170, 90, 40]];
  var TEMAS = [['Habitantes por km² (densidad)', [45, 120, 380, 15, 90, 250, 8, 60, 30], 'hab/km²', [50, 150]], ['Hogares con agua de red (%)', [72, 88, 97, 40, 81, 93, 35, 66, 58], '%', [60, 85]]];
  var PAL = ['#FFF3E0', '#FFB74D', '#E65100'];
  function clase(v, cortes) { return v < cortes[0] ? 0 : v < cortes[1] ? 1 : 2; }
  function mapaT(t, paso, tap) { var s = ''; REG.forEach(function (r, i) { var v = t[1][i], c = paso >= 2 ? PAL[clase(v, t[3])] : '#ECEFF1';
      s += (tap ? '<g data-t="' + i + '" class="nat-tap">' : '<g>') + rc(r[0], r[1], r[2], r[3], c, '#fff', 4, ' stroke-width="3"') + tx(r[0] + r[2] / 2, r[1] + r[3] / 2 - 2, String.fromCharCode(65 + i), { a: 'middle', s: 11, w: 900 }) + (paso >= 1 || tap ? tx(r[0] + r[2] / 2, r[1] + r[3] / 2 + 12, v, { a: 'middle', s: 10, w: 800 }) : '') + '</g>'; });
    if (paso >= 2) ['menos de ' + t[3][0], t[3][0] + ' a ' + t[3][1], 'más de ' + t[3][1]].forEach(function (l, k) { s += rc(360, 40 + k * 28, 20, 18, PAL[k], C.gris) + tx(386, 53 + k * 28, l, { s: 9.5, w: 700 }); });
    return S(470, 215, s + (paso >= 2 ? tx(360, 30, t[2], { s: 10, w: 900 }) : '')); }
  M.tematico = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('t', 'Dato', TEMAS.map(function (t, i) { return [i, t[0]]; }), 0), function (o) { var t = TEMAS[+(o.t || 0)] || TEMAS[0], mx = t[1].indexOf(Math.max.apply(null, t[1]));
      return [{ vis: mapaT(t, 0), txt: 'Un <b>mapa temático</b> muestra un solo dato sobre un territorio. Acá, un país de ejemplo con 9 regiones (A a I).' }, { vis: mapaT(t, 1), txt: 'Primero, el dato de cada región: <b>' + t[0].toLowerCase() + '</b>.' }, { vis: mapaT(t, 1), txt: 'Armamos <b>3 rangos</b>: menos de ' + t[3][0] + ', de ' + t[3][0] + ' a ' + t[3][1] + ' y más de ' + t[3][1] + ' ' + t[2] + '.' }, { vis: mapaT(t, 2), txt: 'Pintamos cada región según su rango: <b>más oscuro = más</b>. La referencia explica los colores.' }, { vis: mapaT(t, 2), txt: 'Ahora se lee de un vistazo: el valor más alto está en la región <b>' + String.fromCharCode(65 + mx) + '</b> y se ve si los valores altos están juntos o dispersos.' }]; });
  } };
  M.tematico_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var t = TEMAS[rot(TEMAS.length, u)], i = R(0, 8), v = t[1][i], k = clase(v, t[3]), L = ['☐ claro (menos de ' + t[3][0] + ')', '▣ medio (' + t[3][0] + ' a ' + t[3][1] + ')', '■ oscuro (más de ' + t[3][1] + ')'];
      return { cons: 'La región <b>' + String.fromCharCode(65 + i) + '</b> tiene ' + v + ' ' + t[2] + '. ¿Con qué color se pinta?', html: mapaT(t, 1), ops: L, ok: L[k], ayuda: 'Fijate en qué rango cae ' + v + '.', bien: '¡Bien!' }; });
  } };

  // =====================================================================================
  // 7) MAPA HISTÓRICO: territorio que cambia con los años y rutas
  // =====================================================================================
  var INCA = [[1438, -15, -12, 'Pachacútec empieza la expansión desde el Cusco'], [1471, -18, -4, 'Tupac Yupanqui avanza hacia el norte y el sur'], [1493, -35, -1, 'Huayna Cápac llega hasta el actual Ecuador y el centro de Chile'], [1532, -35, 2, 'Máxima extensión: unos 4.000 km de norte a sur. Llegan los españoles']];
  var CRUCE = [['Mendoza', 300, 120, 'enero de 1817: el Ejército de los Andes sale del campamento de El Plumerillo'], ['Paso de Los Patos y Uspallata', 230, 110, 'el ejército cruza la cordillera dividido en columnas, a más de 3.000 m de altura'], ['Chacabuco', 165, 118, 'febrero de 1817: batalla de Chacabuco, triunfo patriota'], ['Santiago de Chile', 150, 140, 'los patriotas entran en Santiago']];
  function sudam(extra) { return '<path d="M200,10 C260,15 330,40 350,80 C360,110 320,140 300,170 C280,200 250,240 235,290 C225,320 210,330 205,300 C195,250 180,200 170,160 C160,120 150,70 165,40 Z" fill="#E8F5E9" stroke="#9dbdb9" stroke-width="2"/>' + '<path d="M178,30 C168,80 172,140 190,200 C200,250 205,285 208,300" fill="none" stroke="#8D6E63" stroke-width="7" stroke-linecap="round" opacity=".55"/>' + (extra || ''); }
  function latY(l) { return 40 - l * 7.4; }
  function andesX(y) { var P = [[20, 180], [80, 170], [140, 175], [200, 190], [250, 201], [310, 209]]; for (var i = 1; i < P.length; i++) if (y <= P[i][0]) { var a = P[i - 1], b2 = P[i], t = (y - a[0]) / (b2[0] - a[0]); return a[1] + (b2[1] - a[1]) * t; } return 209; }
  function franja(l1, l2) { var y1 = latY(l2), y2 = latY(l1), izq = [], der = []; for (var k = 0; k <= 8; k++) { var y = y1 + (y2 - y1) * k / 8, x = andesX(y); izq.push(N.r1(x - 14) + ',' + N.r1(y)); der.unshift(N.r1(x + 22) + ',' + N.r1(y)); } return '<path d="M' + izq.concat(der).join(' L') + ' Z" fill="rgba(194,85,46,.45)" stroke="' + C.coral + '" stroke-width="2"/>'; }
  M.mapa_historico = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    if (p.modo === 'ruta') { escena(el, '', function () { return CRUCE.map(function (q, k) { var s = sudam(); for (var j = 1; j <= k; j++) s += fl(CRUCE[j - 1][1], CRUCE[j - 1][2], CRUCE[j][1], CRUCE[j][2], C.coral, 3); CRUCE.slice(0, k + 1).forEach(function (c, j) { s += ci(c[1], c[2], 5, j === k ? C.coral : C.teal) + tx(c[1] + (c[1] > 200 ? 8 : -8), c[2] - 6, c[0], { a: c[1] > 200 ? 'start' : 'end', s: 10, w: 900 }); });
        return { vis: S(420, 320, s + tx(100, 300, '🗺️ Cruce de los Andes (esquema)', { s: 10, w: 800 })), txt: (k + 1) + '. <b>' + q[0] + '</b>: ' + q[3] + '.' }; }).concat([{ vis: S(420, 320, sudam() + CRUCE.map(function (c, j) { return (j ? fl(CRUCE[j - 1][1], CRUCE[j - 1][2], c[1], c[2], C.coral, 3) : '') + ci(c[1], c[2], 5, C.teal); }).join('')), txt: 'Un mapa histórico con <b>ruta</b> cuenta un proceso en el espacio: de dónde salen, por dónde pasan y a dónde llegan.' }]); }); return; }
    escena(el, '', function () { return INCA.map(function (q, k) { var s = sudam(franja(q[1], q[2])) + ci(andesX(latY(-13.5)) + 4, latY(-13.5), 5, C.osc) + tx(150, latY(-13.5) + 4, 'Cusco', { a: 'end', s: 10, w: 900 });
        INCA.forEach(function (x, j) { s += tx(300, 230 + j * 18, (j <= k ? '■ ' : '□ ') + x[0], { s: 11, w: j === k ? 900 : 600, c: j === k ? C.coral : C.osc }); });
        return { vis: S(420, 320, s + tx(300, 214, 'Imperio inca', { s: 11, w: 900 })), txt: '<b>' + q[0] + '</b>: ' + q[3] + '.' + (k === 0 ? ' Un mapa histórico muestra cómo cambia un territorio con el tiempo.' : '') }; }); });
  } };
  M.mapa_historico_x = { tipo: 'ejercicio', render: function (el, p, api) {
    if (p.modo === 'ruta') { ordenar(el, api, function () { return { cons: 'Ordená la ruta del Cruce de los Andes, desde la salida hasta la llegada.', html: S(420, 320, sudam() + CRUCE.map(function (c) { return ci(c[1], c[2], 5, C.teal); }).join('')), items: CRUCE.map(function (c) { return c[0]; }), bien: '¡Ruta completa!' }; }); return; }
    ordenar(el, api, function () { return { cons: 'Ordená la expansión del Imperio inca, del territorio más chico al más grande.', items: INCA.map(function (q) { return q[0] + ': ' + q[3].split(':')[0].split('.')[0]; }), ayuda: 'Fijate en los años.', bien: '¡Bien! Creció durante casi un siglo.' }; });
  } };

  // =====================================================================================
  // 8) PERÍODOS: comparar dos momentos (cambios y continuidades)
  // =====================================================================================
  var PER = [['Colonia (siglo XVIII)', 'Después de 1810', [['🏛️', 'Gobierno', 'el rey de España y sus funcionarios (virrey)', 'gobiernos elegidos en el territorio (juntas y triunviratos)', 'c'], ['💰', 'Comercio', 'monopolio: solo con España', 'libre comercio con otros países, sobre todo Gran Bretaña', 'c'], ['👥', 'Sociedad', 'grupos con distintos derechos según el origen', 'siguieron las grandes diferencias sociales', 'p'], ['🙏', 'Religión', 'religión católica oficial', 'la religión católica siguió siendo la oficial', 'p'], ['🐄', 'Economía', 'ganadería y producción para el mercado interno', 'la ganadería siguió siendo la actividad principal', 'p']]],
    ['Modelo agroexportador (1880-1930)', 'Industrialización por sustitución (1930-1976)', [['🌾', 'Qué se produce', 'carne y cereales para exportar', 'productos industriales para el mercado interno', 'c'], ['🏛️', 'Rol del Estado', 'interviene poco en la economía', 'el Estado interviene y protege a la industria', 'c'], ['👷', 'Trabajadores', 'peones rurales e inmigrantes', 'crece la clase obrera industrial', 'c'], ['🏙️', 'Dónde vive la gente', 'crecen las ciudades del puerto', 'siguen creciendo las ciudades, por las migraciones internas', 'p'], ['🌎', 'Exportaciones', 'productos agropecuarios', 'los productos agropecuarios siguen siendo lo que más se exporta', 'p']]]];
  function compara(q, n, conMarca) { return '<div class="soc2-per"><div class="soc2-per-h"><b>' + q[0] + '</b><b>' + q[1] + '</b></div>' + q[2].slice(0, n).map(function (a, k) { return '<div class="soc2-per-f' + (k === n - 1 ? ' on' : '') + '"><span>' + a[2] + '</span><i>' + a[0] + '<small>' + a[1] + '</small>' + (conMarca ? '<em class="' + a[4] + '">' + (a[4] === 'c' ? '≠ CAMBIO' : '= CONTINÚA') + '</em>' : '') + '</i><span>' + a[3] + '</span></div>'; }).join('') + '</div>'; }
  M.periodos = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('c', 'Comparar', PER.map(function (q, i) { return [i, ['Colonia / después de 1810', 'Agroexportador / industrialización'][i]]; }), 0), function (o) { var q = PER[+(o.c || 0)] || PER[0], P = [{ vis: compara(q, 0), txt: 'Para comparar dos <b>períodos</b> miramos los mismos <b>aspectos</b> en uno y en otro.' }];
      q[2].forEach(function (a, k) { P.push({ vis: compara(q, k + 1, true), txt: '<b>' + a[1] + '</b>: ' + (a[4] === 'c' ? 'hay un <b>cambio</b>.' : 'hay una <b>continuidad</b>: sigue igual o parecido.') }); });
      P.push({ vis: compara(q, q[2].length, true), txt: 'La historia no cambia todo de golpe: siempre hay <b>cambios</b> y <b>continuidades</b> al mismo tiempo.' }); return P; });
  } };
  M.periodos_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    cajas(el, api, function () { var q = PER[rot(PER.length, u)]; return { tit: q[0] + ' → ' + q[1] + ': ¿cambio o continuidad?', cajas: ['≠ Cambio', '= Continuidad'], items: q[2].map(function (a, i) { return { v: 'p' + i, t: a[0] + ' ' + a[1] + ': ' + a[3], c: a[4] === 'c' ? 0 : 1 }; }) }; }); otro(el);
  } };

  // =====================================================================================
  // 9) ARGUMENTO: premisas, conclusión e indicadores
  // =====================================================================================
  var ARG = [[['Todos los mamíferos respiran con pulmones', 'La ballena es un mamífero'], 'la ballena respira con pulmones', 'por lo tanto', 'deductivo', 'si las premisas son verdaderas, la conclusión tiene que serlo'],
    [['Los últimos cinco veranos fueron muy calurosos', 'Las temperaturas vienen subiendo cada año'], 'el próximo verano probablemente será caluroso', 'en consecuencia', 'inductivo', 'la conclusión es probable, no segura: se apoya en casos observados'],
    [['La escuela debería tener más árboles', 'porque dan sombra en los recreos', 'y bajan la temperatura del patio'], null, 'porque', 'con conclusión al principio', 'la conclusión puede ir primero y las razones después del "porque"']];
  function argDib(a, paso) { var pr = a[1] ? a[0] : a[0].slice(1), con = a[1] || a[0][0], s = '';
    pr.forEach(function (t, i) { s += rc(10 + i * 230, 10, 215, 56, paso >= 1 ? '#E3F2FD' : '#F5F5F5', C.azul, 10) + txw(118 + i * 230, 40, (paso >= 1 ? 'P' + (i + 1) + ': ' : '') + t, { a: 'middle', s: 10.5, w: 700 }, 34); if (paso >= 3) s += fl(118 + i * 230, 68, 235, 112, C.osc, 2.5); });
    s += rc(60, 114, 350, 50, paso >= 2 ? '#FFE0B2' : '#F5F5F5', C.coral, 10) + txw(235, 143, (paso >= 2 ? 'C: ' : '') + con, { a: 'middle', s: 11, w: 900 }, 48);
    if (paso >= 3) s += tx(330, 96, '«' + a[2] + '»', { a: 'middle', s: 11, w: 900, c: C.lila });
    return S(470, 172, s); }
  M.argumento = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('a', 'Argumento', ARG.map(function (a, i) { return [i, a[3]]; }), 0), function (o) { var a = ARG[+(o.a || 0)] || ARG[0];
      return [{ vis: argDib(a, 0), txt: 'Un <b>argumento</b> es un conjunto de oraciones donde unas dan razones para aceptar otra.' }, { vis: argDib(a, 1), txt: 'Las razones son las <b>premisas</b> (P). Son el punto de partida.' }, { vis: argDib(a, 2), txt: 'Lo que se quiere demostrar es la <b>conclusión</b> (C).' }, { vis: argDib(a, 3), txt: 'Palabras como «' + a[2] + '» son <b>indicadores</b>: avisan dónde está la conclusión o dónde están las razones.' }, { vis: argDib(a, 3), txt: 'Este argumento es <b>' + a[3] + '</b>: ' + a[4] + '.' }]; });
  } };
  M.argumento_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, L = [['Hoy no hay clases porque es feriado.', 'Hoy no hay clases', ['es feriado']], ['Leer mejora el vocabulario. Por lo tanto, conviene leer todos los días.', 'conviene leer todos los días', ['Leer mejora el vocabulario']], ['El hielo es agua sólida y el agua sólida se derrite por encima de 0 °C; entonces, a 5 °C el hielo se derrite.', 'a 5 °C el hielo se derrite', ['El hielo es agua sólida', 'el agua sólida se derrite por encima de 0 °C']], ['Como el museo es gratis los domingos, vamos el domingo.', 'vamos el domingo', ['el museo es gratis los domingos']]];
    elegir(el, api, function () { var q = L[rot(L.length, u)];
      return { cons: '«' + q[0] + '» ¿Cuál es la <b>conclusión</b>?', ops: mezclar([q[1]].concat(q[2])), ok: q[1], ayuda: 'Buscá lo que se quiere demostrar; los indicadores (porque, por lo tanto, entonces, como) ayudan.', bien: '¡Sí! Eso es lo que se quiere demostrar; lo otro son las premisas.' }; });
  } };

  // =====================================================================================
  // 10) FALACIAS: el truco, el nombre y cómo responder
  // =====================================================================================
  var FAL = [['Ad hominem (contra la persona)', '🎯', '—Hay que cuidar el agua. —¿Y vos qué sabés, si sos un chico?', 'ataca a la persona en vez de discutir lo que dice', '¿Y qué pensás de lo que dije, más allá de quién lo diga?'],
    ['Hombre de paja', '🧍', '—Quiero menos tarea los fines de semana. —O sea que no querés estudiar nunca más.', 'deforma lo que el otro dijo para que sea fácil atacarlo', 'Yo no dije eso: dije menos tarea, no ninguna.'],
    ['Generalización apresurada', '🔍', 'Dos turistas me trataron mal: los turistas son maleducados.', 'saca una regla general de muy pocos casos', '¿Dos casos alcanzan para hablar de todos?'],
    ['Falsa causa', '🔗', 'Usé mis zapatillas rojas y ganamos: las zapatillas traen suerte.', 'cree que una cosa causa otra solo porque pasaron juntas', 'Que pasen juntas no prueba que una cause la otra.'],
    ['Apelación a la mayoría', '👥', 'Todos mis compañeros lo creen, así que tiene que ser verdad.', 'da algo por verdadero porque mucha gente lo cree', 'Que mucha gente lo crea no lo hace verdadero: ¿qué pruebas hay?'],
    ['Falso dilema', '⚖️', 'O estás con nosotros o estás en contra.', 'presenta solo dos opciones cuando hay más', '¿No hay otras opciones posibles?']];
  M.falacias = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('f', 'Falacia', FAL.map(function (f, i) { return [i, f[0]]; }), 0), function (o) { var f = FAL[+(o.f || 0)] || FAL[0], burb = function (n) { return '<div class="soc2-chat">' + f[2].split(/ (?=—)/).map(function (t, i) { return '<p class="' + (i ? 'der' : 'izq') + '">' + t.replace(/^—/, '') + '</p>'; }).join('') + (n >= 1 ? '<span class="soc2-sello">' + f[1] + ' ' + f[0] + '</span>' : '') + '</div>'; };
      return [{ vis: burb(0), txt: 'Una <b>falacia</b> es un razonamiento que parece convincente pero tiene una trampa. Leé este diálogo: ¿convence?' }, { vis: burb(1), txt: 'Es una falacia de <b>' + f[0].toLowerCase() + '</b>.' }, { vis: burb(1) + card('🪤 La trampa: ' + f[3] + '.'), txt: 'La trampa: ' + f[3] + '.' }, { vis: burb(1) + card('💬 «' + f[4] + '»'), txt: 'Cómo responder sin pelear: señalar la trampa y volver a las razones.' }]; });
  } };
  M.falacias_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var f = FAL[rot(FAL.length, u)]; return { cons: '«' + f[2] + '» ¿Qué falacia es?', ops: mezclar([f[0]].concat(mezclar(FAL.filter(function (x) { return x !== f; })).slice(0, 2).map(function (x) { return x[0]; }))), ok: f[0], bien: '¡Sí! ' + f[3] + '.' }; });
  } };

  // =====================================================================================
  // 11) CORRIENTES FILOSÓFICAS: una pregunta, varias respuestas (mesa de debate)
  // =====================================================================================
  var MESA = [['¿Qué hace que una acción sea buena?', [['Aristóteles', 'siglo IV a. C.', 'La que haría una persona virtuosa: buscar el término medio entre dos extremos (ni cobarde ni temerario: valiente).', 'Ética de la virtud'], ['Kant', 'siglo XVIII', 'La que se hace por deber, siguiendo una regla que podría valer para todos.', 'Ética del deber'], ['Mill', 'siglo XIX', 'La que produce la mayor felicidad para la mayor cantidad de personas.', 'Utilitarismo']]],
    ['¿Cómo conocemos la verdad?', [['Platón', 'siglo IV a. C.', 'Con la razón: lo que vemos son sombras de las Ideas verdaderas.', 'Idealismo'], ['Descartes', 'siglo XVII', 'Dudando de todo hasta encontrar algo seguro: «pienso, luego existo».', 'Racionalismo'], ['Hume', 'siglo XVIII', 'Por la experiencia: todo lo que sabemos empieza por los sentidos.', 'Empirismo']]],
    ['¿Por qué las personas viven bajo un gobierno?', [['Hobbes', 'siglo XVII', 'Sin un poder fuerte habría una guerra de todos contra todos; por seguridad, se acepta obedecer.', 'Contractualismo'], ['Locke', 'siglo XVII', 'Para proteger derechos que ya tenemos: vida, libertad y propiedad. Si el gobierno no los cuida, puede ser reemplazado.', 'Liberalismo'], ['Rousseau', 'siglo XVIII', 'Para vivir según la voluntad general: las leyes las decide el pueblo.', 'Soberanía popular']]]];
  function mesa(q, n) { return '<div class="soc2-mesa"><p class="soc2-preg">❓ ' + q[0] + '</p><div class="soc2-sillas">' + q[1].map(function (f, k) { return '<div class="' + (k < n ? (k === n - 1 ? 'on' : 'ya') : '') + '"><i>🧑‍🏫</i><b>' + f[0] + '</b><small>' + f[1] + ' · ' + f[3] + '</small>' + (k < n ? '<p>«' + f[2] + '»</p>' : '') + '</div>'; }).join('') + '</div></div>'; }
  M.corrientes = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('q', 'Pregunta', MESA.map(function (q, i) { return [i, q[0]]; }), 0), function (o) { var q = MESA[+(o.q || 0)] || MESA[0];
      return [{ vis: mesa(q, 0), txt: 'La filosofía empieza con <b>preguntas</b>. Sentamos a tres pensadores de distintas épocas frente a la misma.' }].concat(q[1].map(function (f, k) { return { vis: mesa(q, k + 1), txt: '<b>' + f[0] + '</b> (' + f[1] + ', ' + f[3].toLowerCase() + ') responde: ' + f[2] }; })).concat([{ vis: mesa(q, 3), txt: 'Cada respuesta es una <b>corriente</b> distinta. Comparar respuestas nos ayuda a armar la nuestra, con razones.' }]); });
  } };
  M.corrientes_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, L = []; MESA.forEach(function (q) { q[1].forEach(function (f) { L.push([q, f]); }); });
    elegir(el, api, function () { var x = L[rot(L.length, u)], q = x[0], f = x[1]; return { cons: 'Ante «' + q[0] + '», ¿quién respondió: <b>«' + f[2] + '»</b>?', ops: q[1].map(function (y) { return y[0]; }), ok: f[0], bien: '¡Sí! ' + f[0] + ' (' + f[3].toLowerCase() + ').' }; });
  } };

  // =====================================================================================
  // 12) CONSTITUCIÓN NACIONAL: estructura, derechos y garantías
  // =====================================================================================
  var CN = [['Preámbulo', '📜', 'presenta quiénes la hacen y para qué: unión nacional, justicia, paz interior, defensa común, bienestar general y libertad'], ['Primera parte: declaraciones, derechos y garantías', '🧑‍🤝‍🧑', 'los derechos de todos los habitantes (art. 14: trabajar, peticionar a las autoridades, entrar y salir del país, publicar sus ideas, asociarse, enseñar y aprender) y la igualdad ante la ley (art. 16)'], ['Nuevos derechos y garantías (reforma de 1994)', '🌱', 'derecho a un ambiente sano (art. 41), derechos de consumidores (art. 42) y las acciones de amparo, hábeas corpus y hábeas data (art. 43)'], ['Segunda parte: autoridades de la Nación', '🏛️', 'cómo se organiza el gobierno federal: Poder Legislativo, Ejecutivo y Judicial, y los gobiernos de provincia']];
  var DG = [['Trabajar y ejercer una industria lícita', 0], ['Publicar las ideas por la prensa sin censura previa', 0], ['Enseñar y aprender', 0], ['Vivir en un ambiente sano', 0], ['Hábeas corpus: pedir a un juez que revise si una detención es legal', 1], ['Amparo: pedir a un juez que frene algo que viola un derecho', 1], ['Nadie puede ser penado sin juicio previo (art. 18)', 1], ['Hábeas data: conocer y corregir los datos que tienen sobre uno', 1]];
  function libro(n) { return '<div class="soc2-libro">' + CN.map(function (c, k) { return '<div class="' + (k < n ? (k === n - 1 ? 'on' : 'ya') : '') + '"><i>' + c[1] + '</i><b>' + c[0] + '</b>' + (k === n - 1 ? '<p>' + c[2] + '</p>' : '') + '</div>'; }).join('') + '</div>'; }
  M.constitucion = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    if (p.modo === 'garantias') { escena(el, '', function () { return [{ vis: card('🧑‍🤝‍🧑 <b>DERECHO</b>: lo que podemos hacer o recibir. Ej.: publicar nuestras ideas.') , txt: 'Un <b>derecho</b> es una facultad que la Constitución reconoce a todas las personas.' }, { vis: card('🧑‍🤝‍🧑 <b>DERECHO</b>: publicar nuestras ideas.') + card('🛡️ <b>GARANTÍA</b>: la herramienta para defenderlo si alguien lo viola. Ej.: el amparo.', 'on'), txt: 'Una <b>garantía</b> es la herramienta para proteger un derecho cuando no se respeta: se reclama ante un juez.' }, { vis: card('🛡️ <b>Hábeas corpus</b> → protege la libertad (detenciones ilegales)') + card('🛡️ <b>Amparo</b> → protege cualquier derecho constitucional') + card('🛡️ <b>Hábeas data</b> → protege los datos personales'), txt: 'Las tres garantías del artículo 43. Sin garantías, los derechos quedarían solo en el papel.' }]; }); return; }
    escena(el, '', function () { return [{ vis: libro(0), txt: 'La <b>Constitución Nacional</b> es la ley más importante del país: ninguna otra ley puede contradecirla. La de Argentina es de 1853 y su última reforma, de 1994.' }].concat(CN.map(function (c, k) { return { vis: libro(k + 1), txt: '<b>' + c[0] + '</b>: ' + c[2] + '.' }; })); });
  } };
  M.constitucion_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = mezclar(DG.filter(function (d) { return !d[1]; })).slice(0, 3).concat(mezclar(DG.filter(function (d) { return d[1]; })).slice(0, 3)); return { tit: '¿Es un derecho o una garantía?', cajas: ['🧑‍🤝‍🧑 Derecho', '🛡️ Garantía'], items: mezclar(it).map(function (d, i) { return { v: 'd' + i, t: d[0], c: d[1] }; }) }; }); otro(el);
  } };

  N.soc2 = { climo: climo, CLI: CLI, placas: placas, PLA: PLA, cuenca: cuenca, CUE: CUE, BIO: BIO, paisaje: paisaje, FAL: FAL, CN: CN, argDib: argDib };
  var css = document.createElement('style');
  css.textContent = ['.soc2-per{display:flex;flex-direction:column;gap:6px}.soc2-per-h{display:grid;grid-template-columns:1fr 1fr;gap:90px;text-align:center}.soc2-per-h b{padding:6px;border-radius:10px;background:#087E83;color:#fff;font-size:.85rem}.soc2-per-f{display:grid;grid-template-columns:1fr 84px 1fr;gap:6px;align-items:center;opacity:.6}.soc2-per-f.on{opacity:1}.soc2-per-f span{padding:6px 8px;border-radius:10px;background:#F5F9F8;font-size:.85rem}.soc2-per-f i{font-style:normal;text-align:center;font-size:1.3rem;display:flex;flex-direction:column}.soc2-per-f small{font-size:.7rem;font-weight:800}.soc2-per-f em{font-style:normal;font-size:.65rem;font-weight:900;border-radius:6px;padding:1px 3px}.soc2-per-f em.c{background:#FFE0B2;color:#C2552E}.soc2-per-f em.p{background:#D7F0E9;color:#066A6E}',
    '.soc2-chat{position:relative;max-width:440px;margin:0 auto;padding:10px;border-radius:16px;background:#ECEFF1}.soc2-chat p{max-width:78%;margin:6px 0;padding:8px 12px;border-radius:14px;background:#fff}.soc2-chat p.der{margin-left:auto;background:#D7F0E9}.soc2-sello{display:inline-block;margin-top:6px;padding:4px 10px;border:3px solid #C2552E;border-radius:8px;color:#C2552E;font-weight:900;transform:rotate(-4deg);background:#fff}',
    '.soc2-preg{text-align:center;font-weight:900;font-size:1.05rem}.soc2-sillas{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.soc2-sillas div{padding:8px;border-radius:14px;border:2px solid #E3ECEA;opacity:.5;display:flex;flex-direction:column;align-items:center;text-align:center}.soc2-sillas div.ya{opacity:1}.soc2-sillas div.on{opacity:1;border-color:#087E83;background:#F3FBF7}.soc2-sillas i{font-style:normal;font-size:1.8rem}.soc2-sillas small{font-size:.7rem;color:#4b6a6c}.soc2-sillas p{margin:6px 0 0;font-size:.82rem}',
    '.soc2-libro{display:flex;flex-direction:column;gap:6px;max-width:460px;margin:0 auto;padding:10px;border-left:10px solid #8D6E63;border-radius:6px 14px 14px 6px;background:#FFFDF5;box-shadow:0 2px 6px rgba(0,0,0,.1)}.soc2-libro div{padding:6px 10px;border-radius:10px;opacity:.45}.soc2-libro div.ya{opacity:1}.soc2-libro div.on{opacity:1;background:#FFF3C4}.soc2-libro i{font-style:normal;margin-right:6px}.soc2-libro p{margin:4px 0 0;font-size:.88rem}'].join('');
  document.head.appendChild(css);
})();
