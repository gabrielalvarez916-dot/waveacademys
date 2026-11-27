/* PLANTILLAS DE ARTE para las clases animadas (dibujos propios de las clases, distintos de los de la lección).
   mezcla, circulo, perspectiva, luz, ritmo, teclado. Pasos = frases de voz (ver tools/clase/revisar_pasos.py y GUIA.md). */
(function () {
  var w = W, C = w.C;
  // sonido propio (notas del teclado y golpes del ritmo), bajito para no tapar la voz
  var AU = (function () { var ctx = null; function c() { try { if (!ctx) { var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return null; ctx = new AC(); } if (ctx.state === 'suspended') ctx.resume(); return ctx; } catch (_) { return null; } }
    return { nota: function (m, d) { var x = c(); if (!x) return; var o = x.createOscillator(), g = x.createGain(), t = x.currentTime + .02; o.type = 'triangle'; o.frequency.value = 440 * Math.pow(2, (m - 69) / 12); g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.18, t + .02); g.gain.linearRampToValueAtTime(0, t + (d || .6)); o.connect(g); g.connect(x.destination); o.start(t); o.stop(t + (d || .6) + .05); },
      golpe: function (fuerte) { var x = c(); if (!x) return; var n = x.createBufferSource(), b = x.createBuffer(1, x.sampleRate * .06, x.sampleRate), d = b.getChannelData(0); for (var i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / d.length); n.buffer = b; var g = x.createGain(); g.gain.value = fuerte ? .35 : .15; n.connect(g); g.connect(x.destination); n.start(); } }; })();
  function ahora(tl, f) { tl.call(f, null, '>'); }

  // mezcla: {titulo, a:{color, nombre}, b:{color, nombre}, resultado:{color, nombre}} — 3 pasos: aparece A, aparece B, se mezclan
  T.mezcla = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, cy = 620;
    var a = w.pieza(g, 640, cy); w.el('circle', { r: 170, fill: d.a.color, opacity: .92 }, a); w.txt(a, 0, 230, d.a.nombre, 44, C.txt);
    var b = w.pieza(g, 1280, cy); w.el('circle', { r: 170, fill: d.b.color, opacity: .92 }, b); w.txt(b, 0, 230, d.b.nombre, 44, C.txt);
    var r = w.pieza(g, 960, cy); w.el('circle', { r: 210, fill: d.resultado.color, filter: 'url(#sombra)' }, r); w.txt(r, 0, 290, d.resultado.nombre, 60, C.sol, { 'font-weight': 900 });
    var mas = w.pieza(g, 960, cy); w.txt(mas, 0, 0, '+', 120, C.txt);
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, a, ti ? '<.1' : 0, { x: -200, y: 0 });
    B(1); w.IN(tl, b, 0, { x: 200, y: 0 }); w.IN(tl, mas, '<', { scale: 0 });
    B(2); tl.to(a.parentNode, { attr: { transform: 'translate(860 ' + cy + ')' }, duration: .9, ease: 'power2.inOut' }, '>'); tl.to(b.parentNode, { attr: { transform: 'translate(1060 ' + cy + ')' }, duration: .9, ease: 'power2.inOut' }, '<'); w.OUT(tl, mas, '<');
    tl.to([a, b], { opacity: 0, duration: .4 }, '>-.2'); w.IN(tl, r, '<', { scale: .3, y: 0, ease: 'back.out(2)' }); ahora(tl, function () { if (window.SFX) SFX.play('ding'); });
  } };

  // circulo: {titulo} — 3 pasos: primarios, secundarios, terciarios (y el círculo gira)
  var CIR = ['#FDD835', '#FFB300', '#FB8C00', '#F4511E', '#E53935', '#C2185B', '#8E24AA', '#5E35B1', '#1E88E5', '#00897B', '#43A047', '#9CCC65'], TIPO = [0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 1, 2];
  T.circulo = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'EL CÍRCULO CROMÁTICO'), cx = 960, cy = 640, R = 300, ri = 140, rueda = w.pieza(g, cx, cy), seg = [[], [], []];
    CIR.forEach(function (col, i) { var a0 = (i - .5) / 12 * 2 * Math.PI - Math.PI / 2, a1 = (i + .5) / 12 * 2 * Math.PI - Math.PI / 2, P = function (r, a) { return (r * Math.cos(a)).toFixed(1) + ' ' + (r * Math.sin(a)).toFixed(1); };
      var p = w.el('path', { d: 'M' + P(ri, a0) + ' L' + P(R, a0) + ' A' + R + ' ' + R + ' 0 0 1 ' + P(R, a1) + ' L' + P(ri, a1) + ' A' + ri + ' ' + ri + ' 0 0 0 ' + P(ri, a0) + ' Z', fill: col, stroke: '#0b1f21', 'stroke-width': 6, opacity: 0 }, rueda); seg[TIPO[i]].push(p); });
    var et = ['PRIMARIOS', 'SECUNDARIOS', 'TERCIARIOS'].map(function (s) { var p = w.pieza(g, cx, cy); w.txt(p, 0, 0, s, 34, C.sol, { 'font-weight': 900 }); return p; });
    B(0); w.IN(tl, ti, 0); tl.set(rueda, { opacity: 1 }, '<'); tl.to(seg[0], { opacity: 1, duration: .5, stagger: .25 }, '>'); w.IN(tl, et[0], '<');
    B(1); w.OUT(tl, et[0], 0); tl.to(seg[1], { opacity: 1, duration: .5, stagger: .25 }, '>'); w.IN(tl, et[1], '<');
    B(2); w.OUT(tl, et[1], 0); tl.to(seg[2], { opacity: 1, duration: .4, stagger: .12 }, '>'); w.IN(tl, et[2], '<'); tl.to(rueda, { rotation: 360, svgOrigin: '0 0', duration: 2.4, ease: 'power2.inOut' }, '>');
  } };

  // perspectiva: {titulo, fuga: 1 | 2} — 4 pasos: horizonte, punto(s) de fuga, líneas de fuga, volumen
  T.perspectiva = { n: function () { return 4; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, hz = 470, dos = d.fuga === 2, PF = dos ? [[220, hz], [1700, hz]] : [[1250, hz]];
    var hor = w.el('line', { x1: 160, y1: hz, x2: 1760, y2: hz, stroke: C.aqua, 'stroke-width': 6, 'stroke-dasharray': 1600, 'stroke-dashoffset': 1600 }, g); var lh = w.pieza(g, dos ? 960 : 330, hz - 34); w.txt(lh, 0, 0, 'línea de horizonte', 30, C.aqua);
    var pf = PF.map(function (q, i) { var p = w.pieza(g, q[0], q[1]); w.el('circle', { r: 18, fill: C.coral }, p); w.txt(p, 0, -48, dos ? 'PF' + (i + 1) : 'PUNTO DE FUGA', 30, C.coral, { 'font-weight': 900 }); return p; });
    var V = dos ? [[960, 560], [960, 900]] : [[620, 640], [960, 640], [620, 900], [960, 900]], L = [];
    V.forEach(function (v) { PF.forEach(function (q) { L.push(w.el('line', { x1: v[0], y1: v[1], x2: q[0], y2: q[1], stroke: C.sol, 'stroke-width': 4, 'stroke-dasharray': 2000, 'stroke-dashoffset': 2000, opacity: .8 }, g)); }); });
    var vol = w.pieza(g, 0, 0), t = dos ? null : .38, cara;
    if (dos) { var a = function (v, q, k) { return [v[0] + (q[0] - v[0]) * k, v[1] + (q[1] - v[1]) * k]; }, a1 = a(V[0], PF[0], .3), a2 = a(V[1], PF[0], .3), b1 = a(V[0], PF[1], .3), b2 = a(V[1], PF[1], .3);
      w.el('path', { d: 'M' + V[0] + ' L' + a1 + ' L' + a2 + ' L' + V[1] + ' Z', fill: '#FFB74D', stroke: '#0b1f21', 'stroke-width': 5 }, vol); w.el('path', { d: 'M' + V[0] + ' L' + b1 + ' L' + b2 + ' L' + V[1] + ' Z', fill: '#FFCC80', stroke: '#0b1f21', 'stroke-width': 5 }, vol); cara = w.el('line', { x1: 960, y1: 560, x2: 960, y2: 900, stroke: '#fff', 'stroke-width': 8 }, g); }
    else { var P = function (v) { return [v[0] + (PF[0][0] - v[0]) * t, v[1] + (PF[0][1] - v[1]) * t]; }; w.el('path', { d: 'M620 640 L' + P([620, 640]) + ' L' + P([960, 640]) + ' L960 640 Z', fill: '#FFE0B2', stroke: '#0b1f21', 'stroke-width': 5 }, vol); w.el('path', { d: 'M960 640 L' + P([960, 640]) + ' L' + P([960, 900]) + ' L960 900 Z', fill: '#FFB74D', stroke: '#0b1f21', 'stroke-width': 5 }, vol);
      cara = w.el('rect', { x: 620, y: 640, width: 340, height: 260, fill: '#FFCC80', stroke: '#0b1f21', 'stroke-width': 5, opacity: 0 }, g); }
    B(0); if (ti) w.IN(tl, ti, 0); tl.to(hor, { attr: { 'stroke-dashoffset': 0 }, duration: 1, ease: 'power2.inOut' }, ti ? '<.2' : '>'); w.IN(tl, lh, '<.4');
    B(1); pf.forEach(function (p, i) { w.IN(tl, p, i ? '<.2' : 0, { scale: 0, y: 0, ease: 'back.out(3)' }); }); if (!dos) tl.to(cara, { opacity: 1, duration: .4 }, '<'); else tl.from(cara, { opacity: 0, duration: .4 }, '<');
    B(2); tl.to(L, { attr: { 'stroke-dashoffset': 0 }, duration: .8, stagger: .15, ease: 'power2.out' }, '>');
    B(3); w.IN(tl, vol, 0, { scale: 1, y: 0 }); tl.to(L, { opacity: .25, duration: .5 }, '<'); ahora(tl, function () { if (window.SFX) SFX.play('ding'); });
  } };

  // luz: {titulo} — 4 pasos: esfera plana, luz, brillo y sombra propia, sombra proyectada (la luz se mueve)
  T.luz = { n: function () { return 4; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, defs = w.el('defs', {}, g), id = 'luzE' + Math.round(Math.random() * 1e6), gr = w.el('radialGradient', { id: id, cx: '35%', cy: '30%', r: '75%' }, defs);
    var s0 = w.el('stop', { offset: '0', 'stop-color': '#9E9E9E' }, gr), s1 = w.el('stop', { offset: '.3', 'stop-color': '#9E9E9E' }, gr), s2 = w.el('stop', { offset: '1', 'stop-color': '#9E9E9E' }, gr);
    var piso = w.el('ellipse', { cx: 1080, cy: 870, rx: 260, ry: 40, fill: 'rgba(0,0,0,.55)', opacity: 0 }, g), bola = w.pieza(g, 960, 620); w.el('circle', { r: 220, fill: 'url(#' + id + ')' }, bola);
    var lamp = w.pieza(g, 560, 300); w.emoji(lamp, 0, 0, '💡', 120); var rayo = w.flecha(g, 620, 340, 820, 470, C.sol, 8);
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, bola, ti ? '<.1' : 0, { scale: .6, y: 0 });
    B(1); w.IN(tl, lamp, 0, { scale: 0, y: 0 }); w.dibujarFlecha(tl, rayo, '>');
    B(2); tl.to(s0, { attr: { 'stop-color': '#FFFFFF' }, duration: .7 }, '>'); tl.to(s2, { attr: { 'stop-color': '#212121' }, duration: .9 }, '<');
    B(3); tl.to(piso, { opacity: 1, duration: .6 }, '>'); tl.to(lamp.parentNode, { attr: { transform: 'translate(1360 300)' }, duration: 1.6, ease: 'power1.inOut' }, '>'); tl.to(gr, { attr: { cx: '65%' }, duration: 1.6, ease: 'power1.inOut' }, '<'); tl.to(piso, { attr: { cx: 840 }, duration: 1.6, ease: 'power1.inOut' }, '<'); tl.to(rayo, { opacity: 0, duration: .3 }, '<');
  } };

  // ritmo: {titulo, compas: 4, figuras: [1, .5, .5, 2]} — 1 + figuras pasos: pentagrama y pulso, después cada figura (suena)
  function notaClase(p, x, y, v) { w.el('ellipse', { cx: x, cy: y, rx: 26, ry: 19, transform: 'rotate(-20 ' + x + ' ' + y + ')', fill: v >= 2 ? 'none' : C.txt, stroke: C.txt, 'stroke-width': 7 }, p); if (v < 4) w.el('line', { x1: x + 24, y1: y - 6, x2: x + 24, y2: y - 130, stroke: C.txt, 'stroke-width': 7 }, p); if (v === .5) w.el('path', { d: 'M' + (x + 24) + ' ' + (y - 130) + ' q34 26 26 76', fill: 'none', stroke: C.txt, 'stroke-width': 7 }, p); }
  T.ritmo = { n: function (d) { return 1 + d.figuras.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, c = d.compas || 4, tot = Math.max(c, d.figuras.reduce(function (a, b) { return a + b; }, 0)), pen = w.pieza(g, 0, 0), y0 = 520;
    for (var i = 0; i < 5; i++) w.el('line', { x1: 220, y1: y0 + i * 40, x2: 1700, y2: y0 + i * 40, stroke: C.suave, 'stroke-width': 4 }, pen); w.el('line', { x1: 1700, y1: y0, x2: 1700, y2: y0 + 160, stroke: C.txt, 'stroke-width': 8 }, pen);
    w.txt(pen, 290, y0 + 45, String(c), 90, C.txt, { 'font-weight': 900 }); w.txt(pen, 290, y0 + 125, '4', 90, C.txt, { 'font-weight': 900 });
    var pul = w.pieza(g, 0, 0); for (var k = 0; k < c; k++) { w.el('circle', { cx: 420 + k * 1200 / c + 60, cy: 860, r: k ? 26 : 36, fill: k ? C.aqua : C.coral }, pul); }
    var x = 430, F = d.figuras.map(function (v) { var p = w.pieza(g, 0, 0); notaClase(p, x + 30, y0 + 100, v); var nom = { 4: 'redonda', 2: 'blanca', 1: 'negra', .5: 'corchea' }[v]; w.txt(p, x + 30, y0 + 230, nom, 30, C.sol); x += 1200 * v / tot; return p; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, pen, ti ? '<.1' : 0, { y: 30 }); w.IN(tl, pul, '>'); for (var j = 0; j < c; j++) (function (j) { tl.call(function () { AU.golpe(j === 0); }, null, '>' + (j ? .45 : .05)); })(j);
    F.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { scale: .4, y: 0, ease: 'back.out(2.5)' }); ahora(tl, function () { AU.nota(76, Math.min(.5, d.figuras[k] * .3)); }); });
  } };

  // teclado: {titulo, notas: [60, 64, 67], acorde: true?} — 1 + notas pasos: el teclado, cada tecla se ilumina y suena (con acorde: al final suenan juntas)
  T.teclado = { n: function (d) { return 1 + d.notas.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, NOM = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si'], neg = [1, 3, 6, 8, 10], tec = w.pieza(g, 0, 0), K = {}, x = 300, y = 450;
    for (var m = 60; m <= 76; m++) if (neg.indexOf(m % 12) < 0) { K[m] = w.el('rect', { x: x, y: y, width: 128, height: 420, rx: 14, fill: '#f4f7f6', stroke: '#0b1f21', 'stroke-width': 6 }, tec); K[m].lab = w.txt(tec, x + 64, y + 380, NOM[m % 12], 32, '#0b1f21', { 'font-weight': 800 }); K[m].px = x; x += 132; }
    for (var m2 = 60; m2 <= 76; m2++) if (neg.indexOf(m2 % 12) >= 0) K[m2] = w.el('rect', { x: K[m2 - 1].px + 92, y: y, width: 80, height: 260, rx: 10, fill: '#0b1f21' }, tec);
    var L = d.notas.map(function (n, k) { var p = w.pieza(g, (K[n].px != null ? K[n].px + 64 : K[n - 1].px + 132), y - 60); w.txt(p, 0, 0, NOM[n % 12], 46, C.sol, { 'font-weight': 900 }); return p; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, tec, ti ? '<.1' : 0, { y: 40 });
    d.notas.forEach(function (n, k) { B(k + 1); tl.to(K[n], { attr: { fill: neg.indexOf(n % 12) >= 0 ? C.coral : C.sol }, duration: .25 }, '>'); w.IN(tl, L[k], '<', { scale: 0, y: 0 }); ahora(tl, function () { AU.nota(n, .7); if (d.acorde && k === d.notas.length - 1) setTimeout(function () { d.notas.forEach(function (x2) { AU.nota(x2, 1.4); }); }, 700); }); });
  } };
})();
