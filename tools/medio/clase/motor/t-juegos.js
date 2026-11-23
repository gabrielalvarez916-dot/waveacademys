/* PLANTILLAS · JUEGOS: verdadero o falso (vof), este o ese (versus), jefe final (jefe) e historieta (historieta). */
(function () {
  var w = W, C = w.C;
  function ancho(s, f, min, max) { return Math.max(min || 160, Math.min(max || 1600, String(s).length * f + 80)); }

  // vof: verdadero o falso con sello. {afirmacion, emoji?, verdadero: true|false, explicacion} — 3 pasos: afirmación · ¿V o F? · sello y explicación
  T.vof = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var a = w.pieza(g, 960, 360); w.tarjeta(a, 0, 0, 1500, 220, C.aqua); if (d.emoji) w.emoji(a, -640, 0, d.emoji, 100); w.multi(a, d.emoji ? 60 : 0, 0, '«' + d.afirmacion + '»', 50, C.txt, d.emoji ? 1260 : 1400);
    var V = w.chip(g, 660, 640, 480, 130, '✅ VERDADERO', { r: 30, size: 46, stroke: C.verde }), F = w.chip(g, 1260, 640, 480, 130, '❌ FALSO', { r: 30, size: 46, stroke: C.coral });
    var ok = d.verdadero ? V : F, no = d.verdadero ? F : V;
    var se = w.pieza(g, 960, 520); w.caja(se, 0, 0, 620, 170, 'none', d.verdadero ? C.verde : C.coral, 30, 12); w.txt(se, 0, 4, d.verdadero ? 'VERDADERO' : 'FALSO', 92, d.verdadero ? C.verde : C.coral, { 'font-weight': 900, 'letter-spacing': 6 });
    se.parentNode.setAttribute('transform', 'translate(960 520) rotate(-8)');
    var ex = w.pieza(g, 960, 830); w.caja(ex, 0, 0, 1500, 150, 'url(#gCard)', C.sol, 30, 5); w.multi(ex, 0, 0, d.explicacion, 40, C.txt, 1400);
    B(0); w.IN(tl, a, 0, { y: -40 });
    B(1); w.IN(tl, V, 0, { x: -80, y: 0 }); w.IN(tl, F, '<.1', { x: 80, y: 0 });
    B(2); tl.to(no, { opacity: .2, duration: .25 }, '>'); tl.to(ok, { opacity: .2, duration: .25 }, '<'); w.IN(tl, se, '>', { scale: 3, y: 0, d: .35, ease: 'power4.in' }); w.sacudir(tl, '>'); w.IN(tl, ex, '>', { y: 40 });
  } };

  // versus: este o ese, cara a cara. {titulo?, a:{txt, emoji, datos:[...] (1-3)}, b:{...}, gana:'a'|'b'|'empate', veredicto} — 4 pasos
  T.versus = { n: function () { return 4; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'ESTE O ESE');
    function lado(x, o, col, sg) { var p = w.pieza(g, x, 590); w.tarjeta(p, 0, 0, 640, 560, col); w.emoji(p, 0, -170, o.emoji || '⭐', 130); w.txt(p, 0, -50, o.txt, 50, col, { 'font-weight': 900 });
      var ds = (o.datos || []).map(function (s, k) { var q = w.pieza(p, 0, 50 + k * 80); w.multi(q, 0, 0, '• ' + s, 34, C.txt, 560); return q; }); return { p: p, ds: ds }; }
    var A = lado(520, d.a, C.azul), Bd = lado(1400, d.b, C.coral);
    var vs = w.pieza(g, 960, 560); w.el('circle', { r: 90, fill: 'url(#gSol)', stroke: '#fff', 'stroke-width': 8 }, vs); w.txt(vs, 0, 4, 'VS', 72, '#3a2a00', { 'font-weight': 900 });
    var ver = w.pieza(g, 960, 930); w.caja(ver, 0, 0, 1500, 100, 'url(#gSol)', '#ffe7a8', 50, 5); w.multi(ver, 0, 0, (d.gana === 'empate' ? '🤝 ' : '🏆 ') + d.veredicto, 40, '#3a2a00', 1400);
    var co = w.pieza(g, d.gana === 'b' ? 1400 : 520, 300); w.emoji(co, 0, 0, '👑', 90);
    B(0); w.IN(tl, ti, 0); w.IN(tl, A.p, '<.1', { x: -400, y: 0, ease: 'power3.out' }); w.IN(tl, Bd.p, '<', { x: 400, y: 0, ease: 'power3.out' }); w.IN(tl, vs, '>', { scale: 3, y: 0, ease: 'back.out(2)' }); w.sacudir(tl, '>');
    B(1); A.ds.forEach(function (q) { w.IN(tl, q, '<.15', { x: -30, y: 0 }); });
    B(2); Bd.ds.forEach(function (q) { w.IN(tl, q, '<.15', { x: 30, y: 0 }); });
    B(3); if (d.gana !== 'empate') { tl.to(d.gana === 'b' ? A.p : Bd.p, { opacity: .45, duration: .3 }, '>'); w.IN(tl, co, '>', { y: -60, scale: .3, ease: 'bounce.out', d: .6 }); } w.IN(tl, ver, '>', { y: 30 });
  } };

  // jefe: jefe final con barra de vida; cada pregunta acertada le saca vida. {jefe:{nombre, emoji}, preguntas:[{p, r}] (2-4)} — 2 + preguntas pasos
  T.jefe = { n: function (d) { return 2 + d.preguntas.length; }, armar: function (g, tl, B, d) {
    var n = d.preguntas.length, j = w.pieza(g, 380, 560); w.el('circle', { r: 190, fill: 'rgba(226,69,60,.12)', stroke: C.coral, 'stroke-width': 6 }, j); var cara = w.emoji(j, 0, 0, d.jefe.emoji || '👾', 220);
    var nb = w.pieza(g, 380, 820); w.txt(nb, 0, 0, d.jefe.nombre || 'EL JEFE FINAL', 40, C.coral, { 'font-weight': 900, 'letter-spacing': 2 });
    var hp = w.pieza(g, 960, 270); w.txt(hp, -620, 0, 'VIDA', 30, C.coral, { 'font-weight': 900 }); w.el('rect', { x: -560, y: -20, width: 1240, height: 40, rx: 20, fill: 'rgba(0,0,0,.35)', stroke: '#fff', 'stroke-width': 4 }, hp);
    var barra = w.el('rect', { x: -556, y: -16, width: 1232, height: 32, rx: 16, fill: C.coral }, hp);
    var Q = d.preguntas.map(function (q, k) { var p = w.pieza(g, 1160, 560); w.tarjeta(p, 0, -50, 1000, 260, W.PAL[(k + 1) % W.PAL.length]); w.txt(p, -440, -150, 'GOLPE ' + (k + 1) + ' DE ' + n, 26, C.suave, { 'text-anchor': 'start', 'letter-spacing': 3 });
      w.multi(p, 0, -40, q.p, 46, C.txt, 900); var r = w.pieza(p, 0, 160); w.caja(r, 0, 0, 760, 100, 'url(#gSol)', '#ffe7a8', 50, 5); w.multi(r, 0, 0, '⚔️ ' + q.r, 42, '#3a2a00', 700); p.r = r; return p; });
    var fin = w.pieza(g, 1160, 560); w.emoji(fin, 0, -80, '🏆', 150); w.txt(fin, 0, 90, '¡JEFE DERROTADO!', 80, C.sol, { 'font-weight': 900 });
    B(0); w.IN(tl, j, 0, { scale: .2, y: 0, ease: 'back.out(1.6)', d: .7 }); w.IN(tl, nb, '<.2'); w.IN(tl, hp, '<.1', { y: -30 }); w.temblar(tl, j, '>');
    Q.forEach(function (q, k) { B(k + 1); if (k) w.OUT(tl, Q[k - 1], 0, { x: 120 }); w.IN(tl, q, k ? '>' : 0, { x: 150, y: 0 }); w.IN(tl, q.r, '>+.9', { scale: .3, y: 0, ease: 'back.out(2.4)' });
      tl.to(barra, { attr: { width: 1232 * (1 - (k + 1) / n) }, duration: .4 }, '>'); w.temblar(tl, j, '<'); tl.call(function () { try { SFX.play('pop'); } catch (_) {} }, null, '<'); });
    B(n + 1); w.OUT(tl, Q[n - 1], 0); tl.to(j, { rotation: 90, y: 60, opacity: .4, duration: .6, ease: 'power2.in' }, '>'); tl.call(function () { try { SFX.play('fanfarria'); } catch (_) {} if (window.CONFETI) CONFETI(); }, null, '>'); w.IN(tl, fin, '<', { scale: .3, y: 0, ease: 'elastic.out(1,.5)', d: 1 });
  } };

  // historieta: la explicación en viñetas con globos. {titulo?, vinetas:[{emojis:[...] (1-3), txt, quien?}] (2-4)} — un paso por viñeta
  T.historieta = { n: function (d) { return d.vinetas.length; }, armar: function (g, tl, B, d) {
    var n = d.vinetas.length, ti = d.titulo ? w.titulo(g, d.titulo) : null, cols = n <= 2 ? n : 2, filas = Math.ceil(n / cols);
    var pw = cols === 1 ? 1000 : 780, ph = filas === 1 ? 600 : 290, P = W.rejilla(n, 960, filas === 1 ? 600 : 640, pw + 30, ph + 30, cols);
    var V = d.vinetas.map(function (v, k) { var p = w.pieza(g, P[k][0], P[k][1]); w.caja(p, 0, 0, pw, ph, '#f7f2e6', '#1a1a1a', 10, 8).setAttribute('filter', 'url(#sombra)');
      var em = v.emojis || [v.emoji || '🙂'], es = Math.min(ph * .42, 150), ex = W.rejilla(em.length, 0, 0, es * 1.2, 0, em.length);
      em.forEach(function (e, j) { w.emoji(p, -pw * .22 + ex[j][0], ph * .14, e, es); });
      var gw = pw * .52, gh = ph * .5, gx = pw * .2, gy = -ph * .18; w.el('ellipse', { cx: gx, cy: gy, rx: gw / 2, ry: gh / 2, fill: '#fff', stroke: '#1a1a1a', 'stroke-width': 5 }, p);
      w.el('path', { d: 'M' + (gx - gw * .25) + ' ' + (gy + gh * .38) + ' L' + (gx - gw * .45) + ' ' + (gy + gh * .75) + ' L' + (gx - gw * .08) + ' ' + (gy + gh * .45) + ' Z', fill: '#fff', stroke: '#1a1a1a', 'stroke-width': 5 }, p);
      w.multi(p, gx, gy, v.txt, Math.min(36, ph * .1), '#1a1a1a', gw * .8);
      if (v.quien) w.txt(p, -pw / 2 + 24, -ph / 2 + 30, v.quien, 24, '#5a4a2a', { 'text-anchor': 'start', 'font-weight': 900, 'letter-spacing': 2 });
      w.txt(p, pw / 2 - 30, ph / 2 - 24, String(k + 1), 24, '#5a4a2a', { 'font-weight': 900 }); return p; });
    V.forEach(function (p, k) { B(k); if (!k && ti) w.IN(tl, ti, 0); w.IN(tl, p, k || !ti ? 0 : '<.1', { scale: .7, rotation: k % 2 ? 3 : -3, y: 0, ease: 'back.out(1.6)' }); });
  } };
})();
