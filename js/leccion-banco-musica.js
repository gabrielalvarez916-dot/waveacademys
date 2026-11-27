/* BANCO DE LA LECCIÓN INTERACTIVA · ARTE II (música). Con sonido real (WebAudio, sin archivos): ▶ en cada ejemplo.
   Mismo banco que js/leccion-banco*.js (SOLO lección). Cada ejemplo es PASO A PASO y tiene su práctica (_x). */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h || !B._h.nat) return;
  var H = B._h, M = B.motores, N = H.nat, R = H.R, pick = H.pick, mezclar = H.mezclar, fmt = H.fmt;
  var escena = H.escena, respuesta = H.respuesta, cajas = H.cajas, C = N.C, S = N.S, tx = N.tx, ln = N.ln, fl = N.fl, ci = N.ci, rc = N.rc, em = N.em, sel = N.sel, otro = N.otro, elegir = N.elegir, ordenar = N.ordenar, tocar = N.tocar, rot = N.rot, nota = N.nota;
  function card(t, cls) { return '<p class="nat-card ' + (cls || '') + '">' + t + '</p>'; }

  // ---------- sonido ----------
  var ctx = null, maestro = null;
  function A() { try { if (!ctx) { var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return null; ctx = new AC(); maestro = ctx.createGain(); maestro.gain.value = .5; maestro.connect(ctx.destination); } if (ctx.state === 'suspended') ctx.resume(); return ctx; } catch (e) { return null; } }
  function tono(f, t, d, o) { o = o || {}; var c = A(); if (!c) return; var os = c.createOscillator(), g = c.createGain(), t0 = c.currentTime + .03 + (t || 0); os.type = o.tipo || 'triangle'; os.frequency.value = f; var v = o.vol == null ? .35 : o.vol;
    g.gain.setValueAtTime(0, t0); g.gain.linearRampToValueAtTime(v, t0 + .015); g.gain.setValueAtTime(v * .8, t0 + Math.max(.02, d - .05)); g.gain.linearRampToValueAtTime(0, t0 + d); os.connect(g); g.connect(o.dest || maestro); os.start(t0); os.stop(t0 + d + .02); }
  function golpe(t, fuerte, o) { var c = A(); if (!c) return; o = o || {}; var t0 = c.currentTime + .03 + t, n = c.createBufferSource(), b = c.createBuffer(1, c.sampleRate * .08, c.sampleRate), x = b.getChannelData(0); for (var i = 0; i < x.length; i++) x[i] = (Math.random() * 2 - 1) * (1 - i / x.length);
    n.buffer = b; var g = c.createGain(); g.gain.value = fuerte ? .7 : .3; var f = c.createBiquadFilter(); f.type = 'highpass'; f.frequency.value = o.grave ? 80 : 1800; n.connect(f); f.connect(g); g.connect(o.dest || maestro); n.start(t0); }
  var NOTAS = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si'];
  function frec(m) { return 440 * Math.pow(2, (m - 69) / 12); } // m = número MIDI (60 = Do central)
  function boton(id, txt) { return '<button type="button" class="mus-play" data-play="' + id + '">▶ ' + (txt || 'Escuchar') + '</button>'; }
  function conPlay(el, fn) { el._play = fn; if (el._mus) return; el._mus = 1; el.addEventListener('click', function (e) { var b = e.target.closest('[data-play],[data-tecla]'); if (!b) return; if (b.hasAttribute('data-tecla')) { tono(frec(+b.getAttribute('data-tecla')), 0, .5); b.classList.add('on'); setTimeout(function () { b.classList.remove('on'); }, 300); return; } if (el._play) el._play(b.getAttribute('data-play')); }); }
  H.musica = { tono: tono, golpe: golpe, frec: frec, NOTAS: NOTAS };

  // =====================================================================================
  // 1) PARÁMETROS DEL SONIDO: altura, duración, intensidad, timbre
  // =====================================================================================
  var PAR = [['Altura', 'grave o agudo', 'depende de cuántas vibraciones por segundo (frecuencia, en Hz)'], ['Duración', 'largo o corto', 'cuánto tiempo dura el sonido'], ['Intensidad', 'fuerte (forte) o suave (piano)', 'depende de la amplitud: qué tan grande es la vibración'], ['Timbre', 'el «color» del sonido', 'lo que distingue una flauta de un violín aunque toquen la misma nota']];
  var TIMB = ['sine', 'triangle', 'square', 'sawtooth'], TNOM = ['suave (flauta)', 'cálido', 'hueco (videojuego)', 'brillante (metal)'];
  function onda(f, amp, dur, tb) { var d = '', W2 = 380 * dur / 2; for (var x = 0; x <= W2; x += 2) { var ph = x / W2 * f / 110 * 6 * Math.PI, y; y = tb === 1 ? (2 / Math.PI) * Math.asin(Math.sin(ph)) : tb === 2 ? (Math.sin(ph) >= 0 ? 1 : -1) : tb === 3 ? ((ph / Math.PI) % 2) - 1 : Math.sin(ph); d += (x ? 'L' : 'M') + N.r1(20 + x) + ',' + N.r1(90 - y * amp * 60); } return S(420, 180, rc(10, 20, 400, 140, '#FAFAFA', C.gris, 8) + ln(20, 90, 410, 90, '#E0E0E0', 1) + '<path d="' + d + '" fill="none" stroke="' + C.teal + '" stroke-width="2.5"/>'); }
  M.sonido_param = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, H.ctrl('f', 'Altura (Hz)', 110, 880, 10, 220) + H.ctrl('d', 'Duración (s)', .25, 2, .25, 1) + H.ctrl('i', 'Intensidad', .1, 1, .1, .6) + sel('t', 'Timbre', TIMB.map(function (t, i) { return [i, TNOM[i]]; }), 1), function (o) { var f = +o.f, d = +o.d, it = +o.i, tb = +(o.t || 0);
      conPlay(el, function () { tono(f, 0, d, { tipo: TIMB[tb], vol: it * .5 }); });
      var v = onda(f, it, d, tb) + '<p style="text-align:center">' + boton('s', 'Escuchar este sonido') + '</p>';
      return PAR.map(function (q, k) { var extra = k === 0 ? (f < 300 ? 'Ahora es <b>grave</b>.' : f > 500 ? 'Ahora es <b>agudo</b>.' : 'Ahora está en el medio.') : k === 1 ? 'Ahora dura ' + fmt(d) + ' s.' : k === 2 ? (it > .6 ? 'Ahora suena <b>fuerte</b>.' : 'Ahora suena <b>suave</b>.') : 'Ahora el timbre es ' + TNOM[tb] + '.'; return { vis: v, txt: '<b>' + q[0] + '</b> (' + q[1] + '): ' + q[2] + '. ' + extra + ' Mové la barra y escuchá.' }; }); });
  } };
  M.sonido_param_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var k = rot(4, u), a = { f: 262, d: .6, i: .5, t: 1 }, b2 = { f: 262, d: .6, i: .5, t: 1 }; if (k === 0) b2.f = 660; if (k === 1) b2.d = 1.6; if (k === 2) b2.i = 1; if (k === 3) b2.t = 3;
      conPlay(el, function (id) { var q = id === 'a' ? a : b2; tono(q.f, 0, q.d, { tipo: TIMB[q.t], vol: q.i * .5 }); });
      return { cons: 'Escuchá los dos sonidos. ¿Qué cambió del primero al segundo?', html: '<p style="text-align:center">' + boton('a', 'Sonido 1') + ' ' + boton('b', 'Sonido 2') + '</p>', ops: PAR.map(function (q) { return q[0]; }), ok: PAR[k][0], ayuda: '¿Es más agudo? ¿Más largo? ¿Más fuerte? ¿Suena a otro instrumento?', bien: '¡Bien! Cambió la ' + PAR[k][0].toLowerCase() + '.' }; });
  } };

  // =====================================================================================
  // 2) RITMO: pulso, compás y figuras
  // =====================================================================================
  var FIG = [['Redonda', 4, '𝅝'], ['Blanca', 2, '𝅗𝅥'], ['Negra', 1, '♩'], ['Corchea', .5, '♪']];
  var PATRONES = [[1, 1, 1, 1], [2, 1, 1], [.5, .5, 1, 2], [1, .5, .5, 1, 1], [4], [2, 2], [.5, .5, .5, .5, 1, 1]];
  function figuraDe(v) { return FIG.filter(function (f) { return f[1] === v; })[0]; }
  // figura dibujada: cabeza (llena o hueca), plica y corchete
  function notaSvg(x, y, v, col) { var s = '<ellipse cx="' + x + '" cy="' + y + '" rx="7.5" ry="5.5" transform="rotate(-20 ' + x + ' ' + y + ')" fill="' + (v >= 2 ? '#fff' : col) + '" stroke="' + col + '" stroke-width="2.2"/>';
    if (v < 4) s += ln(x + 7, y - 2, x + 7, y - 36, col, 2.2); if (v === .5) s += '<path d="M' + (x + 7) + ',' + (y - 36) + ' q10,8 8,22" fill="none" stroke="' + col + '" stroke-width="2.2"/>'; return s; }
  function pentagrama(pat, comp, marca) { var s = ''; for (var i = 0; i < 5; i++) s += ln(20, 50 + i * 10, 440, 50 + i * 10, '#90A4AE', 1); s += tx(36, 72, comp, { a: 'middle', s: 22, w: 900 }) + ln(440, 50, 440, 90, C.osc, 2);
    var x = 70, tot = Math.max(pat.reduce(function (a, b) { return a + b; }, 0), parseInt(comp, 10) || 0); pat.forEach(function (v, k) { s += notaSvg(x + 10, 80, v, marca === k ? C.coral : C.osc); x += 360 * v / tot; });
    return S(460, 110, s); }
  function tocarRitmo(pat, bpm, compas) { var t = 0, b = 60 / bpm, tot = 0; pat.forEach(function (v) { tono(660, t, Math.min(.25, v * b * .8), { tipo: 'square', vol: .18 }); t += v * b; }); for (var k = 0; k < Math.ceil(t / b); k++) golpe(k * b, k % compas === 0); }
  M.ritmo = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('c', 'Compás', [['4', '4/4'], ['3', '3/4'], ['2', '2/4']], p.compas || '4') + H.ctrl('v', 'Tempo (pulsos por minuto)', 60, 140, 10, 90), function (o) { var c = +o.c || 4, v = +o.v, pat = c === 4 ? [1, .5, .5, 1, 1] : c === 3 ? [2, 1] : [.5, .5, 1];
      conPlay(el, function (id) { if (id === 'pulso') { for (var k = 0; k < c * 2; k++) golpe(k * 60 / v, k % c === 0); } else tocarRitmo(pat, v, c); });
      var pul = '<div class="mus-pul">' + Array.apply(null, Array(c)).map(function (_, k) { return '<span class="' + (k === 0 ? 'fuerte' : '') + '">' + (k + 1) + '</span>'; }).join('') + '</div>';
      return [{ vis: pul + '<p style="text-align:center">' + boton('pulso', 'Escuchar el pulso') + '</p>', txt: 'El <b>pulso</b> es el latido parejo de la música: lo que marcás con el pie. Su velocidad es el <b>tempo</b> (' + v + ' por minuto).' },
        { vis: pul, txt: 'Los pulsos se agrupan en <b>compases</b>: en ' + c + '/4 el primero de cada grupo es más fuerte (acento). ' + (c === 3 ? 'Es el compás del vals.' : c === 2 ? 'Es el compás de la marcha.' : 'Es el más común en canciones.') },
        { vis: '<div class="mus-figs">' + FIG.map(function (f) { return '<span>' + S(40, 50, notaSvg(16, 38, f[1], C.osc)) + '<b>' + f[0] + '</b><small>' + fmt(f[1]) + ' pulso' + (f[1] === 1 ? '' : 's') + '</small></span>'; }).join('') + '</div>', txt: 'Las <b>figuras</b> dicen cuánto dura cada sonido, contado en pulsos (con la negra como unidad).' },
        { vis: pentagrama(pat, c + '/4') + '<p style="text-align:center">' + boton('r', 'Escuchar el ritmo') + '</p>', txt: 'Un compás completo: las figuras suman exactamente ' + c + ' pulsos (' + pat.map(function (x) { return fmt(x); }).join(' + ') + ' = ' + c + ').' }]; });
  } };
  M.ritmo_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    respuesta(el, api, function () { var c = pick([3, 4]), L = [[2], [1, 1], [.5, .5, 1], [2, .5, .5], [1, .5, .5]].filter(function (x) { return x.reduce(function (a, b) { return a + b; }, 0) < c; }), pat = L[rot(L.length, u)], suma = pat.reduce(function (a, b) { return a + b; }, 0), falta = c - suma;
      return { cons: 'Un compás de <b>' + c + '/4</b> empieza con: ' + pat.map(function (x) { return figuraDe(x)[0].toLowerCase(); }).join(', ') + '. ¿Cuántas <b>negras</b> faltan para completarlo?', html: pentagrama(pat, c + '/4'), campos: [{ lab: 'Negras:', v: falta }], ayuda: 'Sumá: ' + pat.map(fmt).join(' + ') + ' = ' + fmt(suma) + ' pulsos; faltan ' + c + ' − ' + fmt(suma) + '.', bien: '¡Bien! Faltan ' + fmt(falta) + '.' }; }); otro(el);
  } };

  // =====================================================================================
  // 3) TECLADO: escalas, intervalos y melodía
  // =====================================================================================
  function teclado(on, desde, hasta, num) { desde = desde || 60; hasta = hasta || 72; var s = '', blancas = [], x = 10, neg = [1, 3, 6, 8, 10];
    for (var m = desde; m <= hasta; m++) if (neg.indexOf(m % 12) < 0) { blancas.push([m, x]); x += 34; }
    blancas.forEach(function (b) { var o2 = on.indexOf(b[0]); s += '<g data-tecla="' + b[0] + '" class="mus-t">' + rc(b[1], 20, 32, 120, o2 >= 0 ? '#FFE082' : '#fff', C.osc, 4) + '</g>' + tx(b[1] + 16, 130, NOTAS[b[0] % 12], { a: 'middle', s: 9, w: 800 }) + (o2 >= 0 && num ? tx(b[1] + 16, 112, o2 + 1, { a: 'middle', s: 12, w: 900, c: C.coral }) : ''); });
    for (var m2 = desde; m2 <= hasta; m2++) if (neg.indexOf(m2 % 12) >= 0) { var prev = blancas.filter(function (b) { return b[0] === m2 - 1; })[0]; if (prev) s += '<g data-tecla="' + m2 + '" class="mus-t">' + rc(prev[1] + 22, 20, 22, 72, on.indexOf(m2) >= 0 ? '#C2552E' : '#263238', null, 3) + '</g>'; }
    return S(x + 20, 150, s); }
  var ESCALAS = { 'Do mayor': [60, 62, 64, 65, 67, 69, 71, 72], 'La menor': [57, 59, 60, 62, 64, 65, 67, 69] };
  var INTERV = [['2.ª (segunda)', 2], ['3.ª (tercera)', 4], ['4.ª (cuarta)', 5], ['5.ª (quinta)', 7], ['8.ª (octava)', 12]];
  var MELO = [[60, 1], [60, 1], [67, 1], [67, 1], [69, 1], [69, 1], [67, 2], [65, 1], [65, 1], [64, 1], [64, 1], [62, 1], [62, 1], [60, 2]];
  M.teclado = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Qué vemos', [['escala', 'Escalas'], ['intervalo', 'Intervalos'], ['melodia', 'Melodía']], p.modo || 'escala'), function (o) { var m = o.m || 'escala';
      if (m === 'escala') { conPlay(el, function (id) { (ESCALAS[id] || ESCALAS['Do mayor']).forEach(function (n, k) { tono(frec(n), k * .35, .32); }); });
        return [{ vis: teclado([], 57, 72), txt: 'Un teclado repite siempre 7 notas blancas: <b>Do, Re, Mi, Fa, Sol, La, Si</b>, y entre algunas, teclas negras (sostenidos #). Tocá las teclas.' }, { vis: teclado(ESCALAS['Do mayor'], 57, 72, true) + '<p style="text-align:center">' + boton('Do mayor', 'Escuchar Do mayor') + '</p>', txt: 'Una <b>escala</b> es una serie de notas en orden. La de <b>Do mayor</b> usa solo las blancas, de Do a Do: suena luminosa.' }, { vis: teclado(ESCALAS['La menor'], 57, 72, true) + '<p style="text-align:center">' + boton('La menor', 'Escuchar La menor') + '</p>', txt: 'La de <b>La menor</b> usa las mismas teclas, pero empieza en La: suena más oscura o melancólica.' }]; }
      if (m === 'intervalo') { conPlay(el, function (id) { var k = +id; tono(frec(60), 0, .5); tono(frec(60 + INTERV[k][1]), .55, .6); });
        return INTERV.map(function (iv, k) { return { vis: teclado([60, 60 + iv[1]], 57, 74, true) + '<p style="text-align:center">' + boton(k, 'Escuchar ' + iv[0]) + '</p>', txt: (k ? '' : 'Un <b>intervalo</b> es la distancia entre dos notas, contando las dos puntas. ') + 'De Do a ' + NOTAS[(60 + iv[1]) % 12] + ': <b>' + iv[0] + '</b>.' }; }); }
      conPlay(el, function () { var t = 0; MELO.forEach(function (n) { tono(frec(n[0]), t, n[1] * .38); t += n[1] * .42; }); });
      return [{ vis: teclado(MELO.map(function (n) { return n[0]; }).filter(function (x, i, a) { return a.indexOf(x) === i; }), 57, 72) + '<p style="text-align:center">' + boton('m', 'Escuchar la melodía') + '</p>', txt: 'Una <b>melodía</b> es una sucesión de notas con ritmo: lo que tarareás de una canción.' }, { vis: '<div class="mus-contorno">' + MELO.map(function (n) { return '<span style="height:' + (20 + (n[0] - 58) * 7) + 'px;flex:' + n[1] + '">' + NOTAS[n[0] % 12] + '</span>'; }).join('') + '</div>', txt: 'Su <b>contorno</b>: sube, se queda, baja. Este dibujo es la melodía vista como alturas.' }, { vis: card('🎶 Movimiento por grado conjunto (notas vecinas) o por salto (notas lejanas). Esta melodía empieza con un salto Do → Sol y después baja por grados.'), txt: 'Las melodías combinan pasos cortos y saltos.' }]; });
  } };
  M.teclado_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var k = rot(INTERV.length, u), iv = INTERV[k]; conPlay(el, function () { tono(frec(60), 0, .5); tono(frec(60 + iv[1]), .55, .6); });
      return { cons: 'Contá las notas en el teclado (incluidas las dos puntas): ¿qué intervalo es?', html: teclado([60, 60 + iv[1]], 57, 74, true) + '<p style="text-align:center">' + boton('x') + '</p>', ops: mezclar(INTERV.map(function (x) { return x[0]; })).slice(0, 3).concat([iv[0]]).filter(function (x, i, a) { return a.indexOf(x) === i; }).slice(-3), ok: iv[0], ayuda: 'Do, Re, Mi… contá desde Do (1) hasta la nota marcada.', bien: '¡Sí! ' + iv[0] + '.' }; });
  } };

  // =====================================================================================
  // 4) ACORDES: mayor y menor
  // =====================================================================================
  var ACO = [['Do mayor', 60, 4, 'alegre, luminoso'], ['La menor', 57, 3, 'triste, melancólico'], ['Sol mayor', 55, 4, 'alegre'], ['Re menor', 62, 3, 'serio, oscuro']];
  M.acordes = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('a', 'Acorde', ACO.map(function (a, i) { return [i, a[0]]; }), 0), function (o) { var a = ACO[+(o.a || 0)] || ACO[0], n = [a[1], a[1] + a[2], a[1] + 7];
      conPlay(el, function (id) { if (id === 'arp') n.forEach(function (x, k) { tono(frec(x), k * .35, .6); }); else n.forEach(function (x) { tono(frec(x), 0, 1.4, { vol: .22 }); }); });
      return [{ vis: teclado([n[0]], 52, 72, true), txt: 'Un <b>acorde</b> son varias notas sonando juntas. Empieza por la <b>fundamental</b>: ' + NOTAS[n[0] % 12] + '.' }, { vis: teclado(n.slice(0, 2), 52, 72, true), txt: 'Le sumamos una <b>tercera</b>: ' + (a[2] === 4 ? '4 semitonos arriba (tercera mayor)' : '3 semitonos arriba (tercera menor)') + ': ' + NOTAS[n[1] % 12] + '.' }, { vis: teclado(n, 52, 72, true) + '<p style="text-align:center">' + boton('arp', 'Nota por nota') + ' ' + boton('j', 'Todas juntas') + '</p>', txt: 'Y una <b>quinta</b>: ' + NOTAS[n[2] % 12] + '. Tres notas = una <b>tríada</b>: ' + n.map(function (x) { return NOTAS[x % 12]; }).join(' – ') + '.' }, { vis: card((a[2] === 4 ? '☀️ ' : '🌧️ ') + a[0] + ': suena ' + a[3]), txt: 'La tercera decide el carácter: con tercera mayor el acorde es <b>mayor</b> (suena alegre); con tercera menor, <b>menor</b> (suena triste). Esa diferencia es la <b>armonía</b>.' }]; });
  } };
  M.acordes_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var a = ACO[rot(ACO.length, u)], n = [a[1], a[1] + a[2], a[1] + 7]; conPlay(el, function () { n.forEach(function (x) { tono(frec(x), 0, 1.4, { vol: .22 }); }); });
      return { cons: 'Escuchá el acorde. ¿Es mayor o menor?', html: '<p style="text-align:center">' + boton('x', 'Escuchar el acorde') + '</p>', ops: ['☀️ Mayor (alegre)', '🌧️ Menor (triste)'], ok: a[2] === 4 ? '☀️ Mayor (alegre)' : '🌧️ Menor (triste)', ayuda: 'Volvé a escucharlo: ¿suena luminoso u oscuro?', bien: '¡Sí! Era ' + a[0] + '.' }; });
  } };

  // =====================================================================================
  // 5) FORMA MUSICAL: AB, ABA, rondó, estrofa y estribillo
  // =====================================================================================
  var MOT = { A: [[60, .5], [64, .5], [67, .5], [64, .5], [65, .5], [62, .5], [60, 1]], B: [[69, 1], [67, .5], [65, .5], [64, 1], [62, 1]], C: [[72, .5], [71, .5], [69, .5], [67, .5], [69, 1], [72, 1]] };
  var FORMAS = [['Binaria', 'AB'], ['Ternaria', 'ABA'], ['Rondó', 'ABACA'], ['Canción', 'ABAB']];
  function tocarForma(f) { var t = 0; f.split('').forEach(function (l) { MOT[l].forEach(function (n) { tono(frec(n[0]), t, n[1] * .34); t += n[1] * .38; }); t += .25; }); }
  function bloquesF(f, n) { var col = { A: '#4DB6AC', B: '#FFB74D', C: '#BA68C8' }; return '<div class="mus-forma">' + f.split('').map(function (l, k) { return '<span style="background:' + (k < n ? col[l] : '#ECEFF1') + '">' + (k < n ? l : '?') + '</span>'; }).join('') + '</div>'; }
  M.forma_musical = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('f', 'Forma', FORMAS.map(function (f, i) { return [i, f[0] + ' (' + f[1] + ')']; }), 1), function (o) { var f = FORMAS[+(o.f || 0)] || FORMAS[1];
      conPlay(el, function (id) { if (id === 'todo') tocarForma(f[1]); else tocarForma(id); });
      var P = [{ vis: bloquesF(f[1], 0) + '<p style="text-align:center">' + boton('A', 'Sección A') + ' ' + boton('B', 'Sección B') + '</p>', txt: 'Una obra se arma con <b>secciones</b>. Las nombramos con letras: si vuelve una igual, repite la letra.' }];
      f[1].split('').forEach(function (l, k) { P.push({ vis: bloquesF(f[1], k + 1), txt: (k + 1) + '.ª parte: <b>' + l + '</b>' + (f[1].indexOf(l) < k ? ' (¡vuelve!)' : ' (nueva)') + '.' }); });
      P.push({ vis: bloquesF(f[1], 9) + '<p style="text-align:center">' + boton('todo', 'Escuchar ' + f[1]) + '</p>', txt: 'Forma <b>' + f[0].toLowerCase() + ' (' + f[1] + ')</b>. ' + (f[1] === 'ABAB' ? 'En las canciones: estrofa (A) y estribillo (B), que se repite y se recuerda.' : 'Repetir da unidad; contrastar da variedad.') }); return P; });
  } };
  M.forma_musical_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var f = FORMAS[rot(3, u)]; conPlay(el, function () { tocarForma(f[1]); }); return { cons: 'Escuchá: ¿qué forma tiene?', html: '<p style="text-align:center">' + boton('x', 'Escuchar la obra') + '</p>', ops: FORMAS.slice(0, 3).map(function (x) { return x[1]; }), ok: f[1], ayuda: 'Contá cuántas secciones hay y cuáles vuelven.', bien: '¡Sí! ' + f[0] + ' (' + f[1] + ').' }; });
  } };

  // =====================================================================================
  // 6) INSTRUMENTOS: familias y cómo producen el sonido
  // =====================================================================================
  var INS = [['Cuerda frotada', '🎻', 'violín, viola, violonchelo', 'un arco frota las cuerdas', 'sawtooth'], ['Cuerda pulsada', '🎸', 'guitarra, arpa, charango', 'se pellizca la cuerda con el dedo o una púa', 'triangle'], ['Viento madera', '🪈', 'flauta, clarinete, quena', 'el aire vibra en un tubo; se cambia la nota tapando agujeros', 'sine'], ['Viento metal', '🎺', 'trompeta, trombón, tuba', 'los labios vibran contra una boquilla', 'square'], ['Percusión', '🥁', 'bombo, redoblante, xilofón', 'se golpea, se sacude o se raspa', 'golpe'], ['Electrófonos', '🎹', 'sintetizador, guitarra eléctrica', 'el sonido se produce o se amplifica con electricidad', 'square']];
  M.instrumentos = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, '', function () { conPlay(el, function (id) { var q = INS[+id]; if (q[4] === 'golpe') [0, .3, .6, .75, .9].forEach(function (t, k) { golpe(t, k % 2 === 0, { grave: k % 2 === 0 }); }); else [60, 64, 67, 72].forEach(function (n, k) { tono(frec(n), k * .3, .5, { tipo: q[4], vol: .25 }); }); });
      return INS.map(function (q, k) { return { vis: '<div class="mus-ins">' + INS.map(function (x, j) { return '<span class="' + (j === k ? 'on' : j < k ? 'ya' : '') + '"><i>' + x[1] + '</i><b>' + x[0] + '</b>' + (j === k ? '<small>' + x[2] + '</small>' : '') + '</span>'; }).join('') + '</div><p style="text-align:center">' + boton(k, 'Escuchar un timbre parecido') + '</p>', txt: '<b>' + q[0] + '</b>: ' + q[3] + '. Por ejemplo: ' + q[2] + '.' }; }); });
  } };
  M.instrumentos_x = { tipo: 'ejercicio', render: function (el, p, api) { cajas(el, api, function () { var it = [['Violín', 0], ['Charango', 1], ['Guitarra criolla', 1], ['Quena', 2], ['Trompeta', 3], ['Bombo legüero', 4], ['Sintetizador', 5], ['Violonchelo', 0], ['Tuba', 3]], k = mezclar([0, 1, 2, 3, 4, 5]).slice(0, 3).sort(), sel2 = mezclar(it.filter(function (q) { return k.indexOf(q[1]) >= 0; })).slice(0, 6);
      return { tit: '¿A qué familia pertenece cada instrumento?', cajas: k.map(function (j) { return INS[j][1] + ' ' + INS[j][0]; }), items: sel2.map(function (q, i) { return { v: 'i' + i, t: q[0], c: k.indexOf(q[1]) }; }) }; }); otro(el); } };

  // =====================================================================================
  // 7) ESTUDIO DIGITAL: pistas, volumen, mezcla
  // =====================================================================================
  var PIS = [['🥁 Batería', '#E57373'], ['🎸 Bajo', '#64B5F6'], ['🎹 Acordes', '#81C784'], ['🎤 Melodía', '#FFD54F']];
  function mezcladora(vol, n) { var s = ''; PIS.forEach(function (q, k) { var y = 14 + k * 46, on = k < n; s += tx(10, y + 20, q[0], { s: 11, w: 800, c: on ? C.osc : '#B0BEC5' }); for (var i = 0; i < 16; i++) { var h = on ? 6 + ((i * (k + 3) * 7) % 22) * vol[k] : 3; s += rc(110 + i * 15, y + 18 - h / 2, 11, h, on ? q[1] : '#ECEFF1', null, 2); } s += rc(360, y + 4, 60, 28, '#fff', C.gris, 6) + tx(390, y + 23, Math.round(vol[k] * 100) + '%', { a: 'middle', s: 10, w: 800 }); }); return S(430, 200, s); }
  function sonarMezcla(vol) { var c = A(); if (!c) return; var bpm = 100, b = 60 / bpm; for (var k = 0; k < 8; k++) { if (vol[0]) { var g = c.createGain(); g.gain.value = vol[0]; g.connect(maestro); golpe(k * b, k % 2 === 0, { grave: k % 2 === 0, dest: g }); }
      if (vol[1] && k % 2 === 0) tono(frec([36, 36, 41, 43][Math.floor(k / 2)]), k * b, b * 1.8, { tipo: 'triangle', vol: .45 * vol[1] }); if (vol[2] && k % 2 === 0) [48, 52, 55].forEach(function (n) { tono(frec(n + [0, 0, 5, 7][Math.floor(k / 2)]), k * b, b * 1.9, { tipo: 'sine', vol: .12 * vol[2] }); }); if (vol[3]) tono(frec([72, 74, 76, 74, 72, 71, 72, 72][k]), k * b, b * .9, { tipo: 'square', vol: .1 * vol[3] }); } }
  M.estudio = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, H.ctrl('b', 'Batería', 0, 1, .1, .8) + H.ctrl('j', 'Bajo', 0, 1, .1, .8) + H.ctrl('c', 'Acordes', 0, 1, .1, .6) + H.ctrl('m', 'Melodía', 0, 1, .1, 1), function (o) { var vol = [+o.b, +o.j, +o.c, +o.m]; conPlay(el, function (id) { var v = vol.slice(); if (id !== 'todo') v = v.map(function (x, k) { return k < +id ? x : 0; }); sonarMezcla(v); });
      return [1, 2, 3, 4].map(function (n) { return { vis: mezcladora(vol, n) + '<p style="text-align:center">' + boton(n, 'Escuchar ' + n + ' pista' + (n > 1 ? 's' : '')) + '</p>', txt: n === 1 ? 'En un <b>estudio digital</b> (DAW) la canción se graba en <b>pistas</b> separadas. Primero la base: la batería.' : n === 2 ? 'Encima se graba el <b>bajo</b>: cada instrumento en su pista, por <b>capas</b>.' : n === 3 ? 'Los <b>acordes</b> rellenan la armonía.' : 'Y la <b>melodía</b> (la voz). Como están separadas, se puede corregir una sin tocar las otras.' }; }).concat([{ vis: mezcladora(vol, 4) + '<p style="text-align:center">' + boton('todo', 'Escuchar la mezcla') + '</p>', txt: 'La <b>mezcla</b> equilibra los volúmenes para que todo se escuche bien. Mové las barras: si la batería tapa la voz, la mezcla está mal.' }]); });
  } };
  M.estudio_x = { tipo: 'ejercicio', render: function (el, p, api) { ordenar(el, api, function () { return { cons: 'Ordená el trabajo en un estudio digital, del primero al último.', items: ['🎼 Componer y armar la maqueta', '🥁 Grabar la base rítmica', '🎤 Grabar las otras pistas por capas', '🎚️ Mezclar (volúmenes y efectos)', '💿 Masterizar y exportar'], bien: '¡Listo para publicar!' }; }); } };

  // =====================================================================================
  // 8) REGISTROS DE LA VOZ
  // =====================================================================================
  var VOC = [['Soprano', 60, 81, 'mujeres y niños, la más aguda'], ['Mezzosoprano', 57, 77, 'mujeres, media'], ['Contralto', 53, 74, 'mujeres, la más grave'], ['Tenor', 48, 69, 'varones, la más aguda'], ['Barítono', 45, 65, 'varones, media'], ['Bajo', 40, 62, 'varones, la más grave']];
  function rangos(k) { var s = ln(40, 180, 440, 180, C.osc, 1.5); [40, 48, 60, 72, 81].forEach(function (m) { var x = 40 + (m - 40) * 9.5; s += ln(x, 176, x, 184, C.osc, 1.5) + tx(x, 196, NOTAS[m % 12] + (Math.floor(m / 12) - 1), { a: 'middle', s: 9 }); });
    VOC.forEach(function (v, i) { var x1 = 40 + (v[1] - 40) * 9.5, x2 = 40 + (v[2] - 40) * 9.5, y = 14 + i * 26; s += rc(x1, y, x2 - x1, 18, i === k ? C.coral : i < 3 ? '#F8BBD0' : '#BBDEFB', null, 9) + tx(i === k ? x1 - 4 : x1 - 4, y + 13, v[0], { a: 'end', s: 10, w: i === k ? 900 : 600 }); });
    return S(460, 205, s); }
  M.registros_voz = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('v', 'Voz', VOC.map(function (v, i) { return [i, v[0]]; }), 0), function (o) { var k = +(o.v || 0), v = VOC[k]; conPlay(el, function () { [v[1] + 3, Math.round((v[1] + v[2]) / 2), v[2] - 3].forEach(function (m, j) { tono(frec(m), j * .6, .55, { tipo: 'sine', vol: .35 }); }); });
      return [{ vis: rangos(-1), txt: 'Cada voz llega cómodamente a ciertas notas: es su <b>registro</b> (o tesitura). Se clasifican de la más aguda a la más grave.' }, { vis: rangos(k) + '<p style="text-align:center">' + boton('x', 'Escuchar grave, medio y agudo') + '</p>', txt: '<b>' + v[0] + '</b>: ' + v[3] + '.' }, { vis: rangos(k), txt: 'Los registros se <b>superponen</b>: por eso en un coro las voces se reparten y suenan juntas. En la adolescencia la voz cambia (la «muda»): es normal.' }]; });
  } };
  M.registros_voz_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; elegir(el, api, function () { var v = VOC[rot(VOC.length, u)]; return { cons: '¿Qué voz es? <b>' + v[3].charAt(0).toUpperCase() + v[3].slice(1) + '</b>.', ops: VOC.map(function (x) { return x[0]; }).filter(function (x, i) { return (i < 3) === (VOC.indexOf(v) < 3); }), ok: v[0], bien: '¡Sí! ' + v[0] + '.' }; }); } };

  // =====================================================================================
  // 9) MÚSICA E IMAGEN: la misma escena con tres músicas
  // =====================================================================================
  var BANDAS = [['😱 Suspenso', function () { for (var k = 0; k < 8; k++) tono(frec(k % 2 ? 41 : 40), k * .45, .4, { tipo: 'sawtooth', vol: .2 }); tono(frec(76), 1.8, 1.4, { tipo: 'sine', vol: .12 }); }, 'notas graves que se repiten y un agudo tenso: algo malo va a pasar'],
    ['😄 Aventura alegre', function () { [60, 64, 67, 72, 67, 64, 65, 69, 72, 77].forEach(function (n, k) { tono(frec(n), k * .22, .2, { tipo: 'square', vol: .12 }); }); }, 'rápida, en tono mayor y saltarina: es un paseo divertido'],
    ['😢 Nostalgia', function () { [57, 60, 64, 62, 60, 59, 57].forEach(function (n, k) { tono(frec(n), k * .55, .6, { tipo: 'sine', vol: .3 }); }); }, 'lenta y en tono menor: la escena se vuelve triste']];
  function bosque(k) { return S(400, 160, rc(0, 0, 400, 160, k === 0 ? '#37474F' : k === 1 ? '#B3E5FC' : '#CFD8DC') + rc(0, 120, 400, 40, '#558B2F') + [40, 120, 300, 360].map(function (x) { return em(x, 95, '🌲', 46); }).join('') + em(200, 110, '🚶', 40)); }
  M.musica_imagen = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, '', function () { conPlay(el, function (id) { BANDAS[+id][1](); }); return [{ vis: bosque(-1), txt: 'Una escena muda: alguien camina por un bosque. ¿Es una escena de miedo, alegre o triste? Todavía no se sabe.' }].concat(BANDAS.map(function (b2, k) { return { vis: bosque(k) + '<p style="text-align:center">' + boton(k, 'Escuchar: ' + b2[0]) + '</p>', txt: 'Con música de <b>' + b2[0].slice(3).toLowerCase() + '</b>: ' + b2[2] + '.' }; })).concat([{ vis: card('🎬 La música de una película o un videojuego no acompaña: <b>cambia el significado</b>. Un tema que vuelve cada vez que aparece un personaje se llama <b>leitmotiv</b>.'), txt: 'Misma imagen, distinta música: distinto sentido.' }]); });
  } };
  M.musica_imagen_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; elegir(el, api, function () { var k = rot(3, u); conPlay(el, function () { BANDAS[k][1](); }); return { cons: 'Escuchá la música de esta escena. ¿Qué emoción busca?', html: bosque(-1) + '<p style="text-align:center">' + boton('x', 'Escuchar') + '</p>', ops: BANDAS.map(function (b2) { return b2[0]; }), ok: BANDAS[k][0], bien: '¡Sí! ' + BANDAS[k][2] + '.' }; }); } };

  // =====================================================================================
  // 10) INDUSTRIA MUSICAL: de la idea al público
  // =====================================================================================
  var IND = [['✍️', 'Autor/a y compositor/a', 'crea la letra y la música; tiene derechos de autor'], ['🎤', 'Intérpretes', 'tocan y cantan la obra'], ['🎚️', 'Producción', 'graba, mezcla y masteriza en el estudio'], ['💿', 'Sello o distribuidora', 'publica y sube la música a las plataformas'], ['📲', 'Plataformas, radio y shows', 'hacen llegar la música y generan ingresos'], ['🎧', 'Público', 'escucha, comparte, va a los recitales']];
  M.industria = { tipo: 'ejemplo', pasos: true, render: function (el, p) { escena(el, '', function () { return IND.map(function (q, k) { return { vis: '<div class="art-lin">' + IND.map(function (x, j) { return '<span class="' + (j === k ? 'on' : '') + '" style="' + (j > k ? 'opacity:.35' : '') + '"><b>' + x[0] + '</b>' + x[1] + '</span>'; }).join('<em>➜</em>') + '</div>', txt: (k + 1) + '. <b>' + q[1] + '</b>: ' + q[2] + '.' + (k === 5 ? ' Cada vez que una canción suena en público, una parte del dinero vuelve a quienes la crearon: por eso existen las sociedades de autores.' : '') }; }); }); } };
  M.industria_x = { tipo: 'ejercicio', render: function (el, p, api) { ordenar(el, api, function () { return { cons: 'Ordená el camino de una canción, desde la idea hasta el público.', items: IND.map(function (q) { return q[0] + ' ' + q[1]; }), bien: '¡La canción llegó!' }; }); } };

  var css = document.createElement('style');
  css.textContent = ['.mus-play{border:0;border-radius:999px;background:#087E83;color:#fff;padding:8px 16px;font:inherit;font-weight:800;cursor:pointer;margin:4px}.mus-t{cursor:pointer}.mus-t.on rect{fill:#4DB6AC}',
    '.mus-pul{display:flex;gap:10px;justify-content:center;margin:8px 0}.mus-pul span{width:44px;height:44px;border-radius:50%;background:#B2DFDB;display:flex;align-items:center;justify-content:center;font-weight:900}.mus-pul span.fuerte{background:#C2552E;color:#fff;transform:scale(1.15)}',
    '.mus-figs{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}.mus-figs span{display:flex;flex-direction:column;align-items:center;min-width:80px;padding:8px;border:2px solid #E3ECEA;border-radius:14px}.mus-figs svg{width:40px}.mus-figs small{color:#4b6a6c}',
    '.mus-contorno{display:flex;align-items:flex-end;gap:3px;height:150px;padding:8px;border-radius:12px;background:#F5F9F8}.mus-contorno span{background:#4DB6AC;border-radius:6px 6px 0 0;font-size:.65rem;font-weight:800;color:#fff;text-align:center;padding-top:2px}',
    '.mus-forma{display:flex;gap:6px;justify-content:center;margin:8px 0}.mus-forma span{width:60px;height:60px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.6rem;font-weight:900;color:#fff}',
    '.mus-ins{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.mus-ins span{padding:8px;border:2px solid #E3ECEA;border-radius:14px;display:flex;flex-direction:column;align-items:center;text-align:center;opacity:.45}.mus-ins span.ya{opacity:.8}.mus-ins span.on{opacity:1;border-color:#087E83;background:#F3FBF7}.mus-ins i{font-style:normal;font-size:1.8rem}.mus-ins small{font-size:.75rem;color:#4b6a6c}'].join('');
  document.head.appendChild(css);
})();
