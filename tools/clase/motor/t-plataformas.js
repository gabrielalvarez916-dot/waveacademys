/* PLANTILLAS · ESTILO PLATAFORMAS (ideas de cómo enseñan apps y canales educativos, con diseño propio de Wave):
   juego de idiomas (fichas, completa, personaje, logro) · pizarra de clase (pizarra, pistas) · exploración (deslizador, prediccion, patron)
   · entrenamiento mental (contrarreloj, memoria) · repaso (unir, mazo, tipeo) · documental (documental, escala) · historia con dilema (dilema)
   · quiz de colores (quiz4) · transformaciones animadas (transforma). Todas livianas: emojis, SVG y GSAP. */
(function () {
  var w = W, C = w.C, uid = 0;
  function id(s) { return 'pl' + s + (++uid); }
  function ancho(s, f, min, max) { return Math.max(min || 160, Math.min(max || 1600, String(s).length * f + 80)); }

  // ======================= JUEGO DE IDIOMAS =======================
  // fichas: armar una frase tocando fichas. {consigna, fichas:[en el orden correcto] (2-7), desorden:[índices] opcional, traduccion} — 3 pasos:
  // fichas mezcladas en el banco · vuelan a la línea en orden · ✓ y traducción.
  T.fichas = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var F = d.fichas, n = F.length, des = d.desorden || F.map(function (_, k) { return (k * 3 + 1) % n; });
    if (des.slice().sort().join() !== F.map(function (_, k) { return k; }).join()) des = F.map(function (_, k) { return n - 1 - k; });
    var q = w.pieza(g, 960, 300); w.multi(q, 0, 0, d.consigna || 'Armá la frase', 46, C.txt, 1500);
    var linea = w.pieza(g, 960, 560); w.el('line', { x1: -700, y1: 60, x2: 700, y2: 60, stroke: C.linea, 'stroke-width': 6, 'stroke-linecap': 'round' }, linea);
    var ws = F.map(function (f) { return ancho(f, 26, 130, 420); }), gap = 22, tot = ws.reduce(function (a, b) { return a + b; }, 0) + gap * (n - 1);
    var esc = tot > 1500 ? 1500 / tot : 1; ws = ws.map(function (x) { return x * esc; }); tot = tot * esc;
    var xs = [], x = 960 - tot / 2; ws.forEach(function (v) { xs.push(x + v / 2); x += v + gap * esc; });
    var bw = ws.slice(), banco = [], bx = 960 - tot / 2; des.forEach(function (k) { banco[k] = bx + bw[k] / 2; bx += bw[k] + gap * esc; });
    var P = F.map(function (f, k) { var p = w.chip(g, banco[k], 800, ws[k], 96, f, { r: 22, size: 40 * Math.max(.8, esc), stroke: W.PAL[k % W.PAL.length] }); return p; });
    var ok = w.pieza(g, 960, 410); w.txt(ok, 0, 0, '✓ ¡Bien!', 50, C.verde, { 'font-weight': 800 });
    var tr = w.pieza(g, 960, 700); w.multi(tr, 0, 0, '«' + (d.traduccion || '') + '»', 40, C.suave, 1500);
    B(0); w.IN(tl, q, 0); w.IN(tl, linea, '<.1', { y: 0 }); P.forEach(function (p, k) { w.IN(tl, p, '<.08', { y: 60, scale: .6 }); });
    B(1); P.forEach(function (p, k) { tl.to(p.parentNode, { attr: { transform: 'translate(' + xs[k] + ' 560)' }, duration: .45, ease: 'power3.inOut' }, k ? '>-.2' : '>'); });
    B(2); P.forEach(function (p) { tl.to(p.r, { attr: { stroke: C.verde }, duration: .2 }, '<.04'); }); w.IN(tl, ok, '>', { scale: .4, y: 0, ease: 'back.out(3)' }); if (d.traduccion) w.IN(tl, tr, '>-.1', { y: 20 });
  } };

  // completa: frase con hueco y opciones; la correcta vuela al hueco. {antes, despues, opciones (2-4), correcta (índice), traduccion?} — 3 pasos
  T.completa = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var hw = Math.max(220, Math.max.apply(null, d.opciones.map(function (o) { return ancho(o, 30, 160, 520); }))), a = String(d.antes || ''), b = String(d.despues || '');
    var la = a.length * 31, lb = b.length * 31, tot = la + hw + lb + 40, x0 = 960 - tot / 2, f = w.pieza(g, 960, 470);
    var sc = tot > 1640 ? 1640 / tot : 1, f0 = f; f = w.el('g', { transform: 'scale(' + sc + ')' }, f0);
    if (a) w.txt(f, x0 - 960 + la / 2, 0, a, 60, C.txt); var hx = x0 - 960 + la + 20 + hw / 2;
    var hueco = w.caja(f, hx, 0, hw, 110, 'rgba(255,255,255,.04)', C.sol, 22, 5); hueco.setAttribute('stroke-dasharray', '18 12');
    if (b) w.txt(f, x0 - 960 + la + 40 + hw + lb / 2, 0, b, 60, C.txt);
    var P = W.rejilla(d.opciones.length, 960, 770, 470, 140, 4), O = d.opciones.map(function (o, k) { return w.chip(g, P[k][0], P[k][1], hw, 104, o, { r: 24, size: 44 }); });
    var tr = w.pieza(g, 960, 610); w.multi(tr, 0, 0, d.traduccion ? '«' + d.traduccion + '»' : '', 38, C.suave, 1500);
    B(0); w.IN(tl, f0, 0, { y: 30 });
    B(1); O.forEach(function (o, k) { w.IN(tl, o, k ? '<.1' : 0, { y: 60 }); });
    B(2); var c = O[d.correcta] || O[0]; O.forEach(function (o) { if (o !== c) tl.to(o, { opacity: .25, duration: .25 }, '<'); });
    tl.to(c.parentNode, { attr: { transform: 'translate(' + (960 + (hx) * sc) + ' 470)' }, duration: .5, ease: 'back.out(1.4)' }, '>');
    tl.to(c.r, { attr: { stroke: C.verde, 'stroke-width': 8 }, duration: .2 }, '>'); tl.to(hueco, { opacity: 0, duration: .2 }, '<'); if (d.traduccion) w.IN(tl, tr, '>', { y: 16 });
  } };

  // personaje: un personaje que habla y reacciona. {personaje:{nombre, emoji}, lineas:[{txt, animo:'feliz'|'sorpresa'|'piensa'|'ojo'|'triste'}] (1-4)} — un paso por línea
  var ANIMO = { feliz: '✨', sorpresa: '❗', piensa: '💭', ojo: '⚠️', triste: '💧' };
  T.personaje = { n: function (d) { return d.lineas.length; }, armar: function (g, tl, B, d) {
    var pj = w.pieza(g, 400, 640); w.el('circle', { cx: 0, cy: 0, r: 210, fill: 'url(#gCard)', stroke: C.aqua, 'stroke-width': 6 }, pj); w.emoji(pj, 0, -10, d.personaje.emoji, 230);
    var nom = w.chip(g, 400, 900, ancho(d.personaje.nombre, 26, 200, 500), 70, d.personaje.nombre, { size: 34, fill: 'url(#gAqua)', color: '#06282a', stroke: '#d8fff7' });
    var badge = w.pieza(g, 560, 470), bt = w.emoji(badge, 0, 0, '', 110);
    var gl = d.lineas.map(function (l) { var p = w.pieza(g, 1180, 600); w.caja(p, 0, 0, 1060, 380, 'url(#gCard)', C.sol, 50, 6).setAttribute('filter', 'url(#sombra)');
      w.el('path', { d: 'M-530 40 L-610 90 L-530 100 Z', fill: '#17393b', stroke: C.sol, 'stroke-width': 6 }, p); w.multi(p, 0, 0, l.txt, 52, C.txt, 940); return p; });
    gl.forEach(function (p, k) { var a = d.lineas[k].animo;
      B(k); if (!k) { w.IN(tl, pj, 0, { y: 120, scale: .5 }); w.IN(tl, nom, '<.2', { y: 30 }); } else w.OUT(tl, gl[k - 1], 0, { duration: .2 });
      w.IN(tl, p, k ? '>' : '<.1', { scale: .5, x: -120, y: 0, ease: 'back.out(1.8)' });
      if (a === 'sorpresa' || a === 'ojo') w.temblar(tl, pj, '>'); else if (a === 'feliz') tl.to(pj, { y: -40, duration: .2, yoyo: true, repeat: 3, ease: 'power1.out' }, '>'); else tl.to(pj, { rotation: -6, duration: .4, yoyo: true, repeat: 1 }, '>');
      if (ANIMO[a]) { tl.call(function (s) { bt.textContent = s; }, [ANIMO[a]], '<'); w.IN(tl, badge, '<', { scale: 0, y: 0, ease: 'back.out(3)' }); } else tl.to(badge, { opacity: 0, duration: .1 }, '<');
    });
  } };

  // logro: pantalla de lección superada, con racha y puntos. {titulo, items:[txt] (1-4), xp} — 1 + items pasos
  T.logro = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var top = w.pieza(g, 960, 330), tt = d.titulo || '¡NIVEL SUPERADO!', tw = String(tt).length * 40; w.emoji(top, -tw / 2 - 40, 0, '🔥', 110); w.txt(top, 50, 0, tt, 64, C.sol, { 'font-weight': 900 });
    var xp = w.pieza(g, 960, 880); w.caja(xp, 0, 0, 480, 110, 'url(#gSol)', '#ffe7a8', 55, 5); var xt = w.txt(xp, 0, 2, '+0 XP', 54, '#3a2a00', { 'font-weight': 900 });
    var n = d.items.length, it = d.items.map(function (s, k) { var p = w.pieza(g, 960, 600 - (n - 1) * 60 + k * 120);
      w.caja(p, 0, 0, 1200, 96, 'url(#gCard)', C.verde, 48, 4); w.txt(p, -540, 0, '✅', 46, '#fff', { 'font-family': 'sans-serif' }); w.multi(p, 30, 0, s, 40, C.txt, 1000); return p; });
    var tot = +d.xp || 10 * n, paso = tot / n;
    B(0); w.IN(tl, top, 0, { scale: .3, y: 0, ease: 'elastic.out(1,.5)', d: 1 }); w.IN(tl, xp, '<.2', { y: 60 });
    it.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { x: -80, y: 0 }); w.contador(tl, xt, paso * k, paso * (k + 1), '<', .6, function (v) { return '+' + Math.round(v) + ' XP'; }); w.pop(tl, xp, '>'); });
  } };

  // ======================= PIZARRA DE CLASE =======================
  // pizarra: la explicación se escribe a mano en un pizarrón oscuro. {titulo?, lineas:[{txt, color?:'sol'|'coral'|'verde'|'azul'|'lila', marca?:'circulo'|'subraya'}] (1-5)} — un paso por línea
  T.pizarra = { n: function (d) { return d.lineas.length; }, armar: function (g, tl, B, d) {
    var pz = w.pieza(g, 960, 610); w.caja(pz, 0, 0, 1640, 760, '#0d1716', '#3b2a1a', 26, 18).setAttribute('filter', 'url(#sombra)');
    if (d.titulo) w.txt(pz, -780, -330, d.titulo, 34, C.suave, { 'text-anchor': 'start', 'letter-spacing': 3 });
    var n = d.lineas.length, gap = Math.min(150, 560 / Math.max(1, n)), y0 = -((n - 1) * gap) / 2 + (d.titulo ? 30 : 0), lapiz = w.pieza(g, 0, 0); w.emoji(lapiz, 0, 0, '✏️', 64);
    var L = d.lineas.map(function (l, k) { var y = y0 + k * gap, col = C[l.color] || C.txt, cid = id('c');
      var cp = w.el('clipPath', { id: cid }, pz), r = w.el('rect', { x: -800, y: y - 70, width: 0, height: 140 }, cp);
      var t = w.txt(pz, 0, y, l.txt, Math.min(70, 1500 / Math.max(8, String(l.txt).length * .55)), col, { 'font-style': 'italic', 'font-family': '"Comic Sans MS","Segoe Print","Bradley Hand",cursive', 'clip-path': 'url(#' + cid + ')' });
      var lw = Math.min(1520, String(l.txt).length * (Math.min(70, 1500 / Math.max(8, String(l.txt).length * .55))) * .52 + 40), m = null;
      if (l.marca === 'circulo') m = w.el('ellipse', { cx: 0, cy: y, rx: lw / 2 + 30, ry: 62, fill: 'none', stroke: C.sol, 'stroke-width': 6, 'stroke-dasharray': 3000, 'stroke-dashoffset': 3000 }, pz);
      if (l.marca === 'subraya') m = w.el('path', { d: 'M' + (-lw / 2) + ' ' + (y + 46) + ' Q 0 ' + (y + 62) + ' ' + (lw / 2) + ' ' + (y + 42), fill: 'none', stroke: C.sol, 'stroke-width': 7, 'stroke-linecap': 'round', 'stroke-dasharray': 3000, 'stroke-dashoffset': 3000 }, pz);
      return { r: r, y: y, m: m, lw: lw }; });
    L.forEach(function (o, k) { B(k); if (!k) w.IN(tl, pz, 0, { y: 0, scale: .96, d: .4 });
      tl.set(lapiz.parentNode, { attr: { transform: 'translate(' + (960 - o.lw / 2) + ' ' + (610 + o.y - 40) + ')' } }, '>'); tl.to(lapiz, { opacity: 1, duration: .1 }, '<');
      tl.to(o.r, { attr: { width: 1600 }, duration: 1.1, ease: 'none' }, '>'); tl.to(lapiz.parentNode, { attr: { transform: 'translate(' + (960 + o.lw / 2) + ' ' + (610 + o.y - 40) + ')' }, duration: .9, ease: 'none' }, '<');
      if (o.m) tl.to(o.m, { attr: { 'stroke-dashoffset': 0 }, duration: .6, ease: 'power1.inOut' }, '>');
      tl.to(lapiz, { opacity: 0, duration: .15 }, '>'); });
  } };

  // pistas: un problema con pistas que se destapan de a una y la respuesta al final. {problema, pistas:[...] (1-3), respuesta} — 2 + pistas pasos
  T.pistas = { n: function (d) { return 2 + d.pistas.length; }, armar: function (g, tl, B, d) {
    var pr = w.pieza(g, 960, 320); w.caja(pr, 0, 0, 1600, 150, 'url(#gCard)', C.aqua, 30, 5); w.multi(pr, 0, 0, d.problema, 46, C.txt, 1500);
    var n = d.pistas.length, P = d.pistas.map(function (s, k) { var p = w.pieza(g, 960, 480 + k * 130); w.caja(p, 0, 0, 1500, 104, 'rgba(244,182,63,.08)', C.sol, 24, 4);
      w.txt(p, -660, 0, '💡 ' + (k + 1), 38, C.sol, { 'font-weight': 800 }); w.multi(p, 60, 0, s, 38, C.txt, 1240); return p; });
    var rs = w.pieza(g, 960, Math.min(900, 520 + n * 130)); w.caja(rs, 0, 0, 1100, 120, 'url(#gSol)', '#ffe7a8', 60, 5); w.multi(rs, 0, 0, '✔ ' + d.respuesta, 48, '#3a2a00', 1000);
    B(0); w.IN(tl, pr, 0);
    P.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { rotationX: 0, scaleY: 0, y: 0, d: .45 }); });
    B(n + 1); w.IN(tl, rs, 0, { scale: .4, y: 0, ease: 'back.out(2.2)' });
  } };

  // ======================= EXPLORAR (antes de explicar) =======================
  // deslizador: un control que se mueve y cambia lo que se ve. {titulo, min, max, unidad?, emoji, paradas:[{v, txt}] (2-5)} — un paso por parada
  T.deslizador = { n: function (d) { return d.paradas.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), mn = +d.min, mx = +d.max, X = function (v) { return 360 + (v - mn) / (mx - mn || 1) * 1200; };
    var pista = w.pieza(g, 0, 0); w.el('rect', { x: 360, y: 790, width: 1200, height: 18, rx: 9, fill: C.linea }, pista); var lleno = w.el('rect', { x: 360, y: 790, width: 0, height: 18, rx: 9, fill: C.aqua }, pista);
    w.txt(pista, 360, 850, mn + (d.unidad ? ' ' + d.unidad : ''), 30, C.suave); w.txt(pista, 1560, 850, mx + (d.unidad ? ' ' + d.unidad : ''), 30, C.suave);
    var pe = w.el('g', { transform: 'translate(' + X(mn) + ' 799)' }, pista); w.el('circle', { r: 38, fill: C.sol, stroke: '#fff', 'stroke-width': 6, filter: 'url(#sombra)' }, pe);
    var vis = w.pieza(g, 960, 520), em = w.emoji(vis, 0, 0, d.emoji || '⚪', 150), val = w.pieza(g, 960, 690), vt = w.txt(val, 0, 0, '', 64, C.sol, { 'font-weight': 900 });
    var cap = w.pieza(g, 960, 930), ct = w.txt(cap, 0, 0, '', 38, C.txt);
    var fmt = function (v) { return (Math.round(v * 10) / 10).toLocaleString('es-AR') + (d.unidad ? ' ' + d.unidad : ''); }, ant = mn;
    d.paradas.forEach(function (p, k) { var v = +p.v, s = .5 + (v - mn) / (mx - mn || 1) * 1.1;
      B(k); if (!k) { w.IN(tl, ti, 0); w.IN(tl, pista, '<.1', { y: 0 }); w.IN(tl, vis, '<.1'); w.IN(tl, val, '<'); w.IN(tl, cap, '<'); }
      tl.to(pe, { attr: { transform: 'translate(' + X(v) + ' 799)' }, duration: .8, ease: 'power2.inOut' }, '>'); tl.to(lleno, { attr: { width: X(v) - 360 }, duration: .8, ease: 'power2.inOut' }, '<');
      tl.to(em, { scale: s, transformOrigin: '50% 50%', duration: .8, ease: 'power2.inOut' }, '<'); w.contador(tl, vt, ant, v, '<', .8, fmt);
      tl.call(function (s2) { ct.textContent = s2; }, [p.txt || ''], '<'); tl.fromTo(ct, { opacity: 0 }, { opacity: 1, duration: .3, immediateRender: false }, '<'); ant = v; });
  } };

  // prediccion: ¿qué creés que pasa? Dos opciones, cuenta regresiva y el resultado. {pregunta, a:{txt, emoji}, b:{txt, emoji}, correcta:'a'|'b', resultado} — 3 pasos
  T.prediccion = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var q = w.pieza(g, 960, 300); w.multi(q, 0, 0, '🔮 ' + d.pregunta, 54, C.txt, 1600);
    function op(x, o, l, col) { var p = w.pieza(g, x, 590); w.tarjeta(p, 0, 0, 640, 330, col); w.txt(p, -270, -125, l, 40, col, { 'font-weight': 900 }); w.emoji(p, 0, -40, o.emoji || '❓', 100); w.multi(p, 0, 90, o.txt, 38, C.txt, 560); return p; }
    var A = op(560, d.a, 'A', C.azul), Bb = op(1360, d.b, 'B', C.coral), cu = w.pieza(g, 960, 590), ct = w.txt(cu, 0, 0, '3', 110, C.sol, { 'font-weight': 900 });
    var ok = d.correcta === 'b' ? Bb : A, no = ok === A ? Bb : A, rs = w.pieza(g, 960, 880); w.caja(rs, 0, 0, 1500, 130, 'url(#gSol)', '#ffe7a8', 40, 5); w.multi(rs, 0, 0, d.resultado, 40, '#3a2a00', 1400);
    B(0); w.IN(tl, q, 0); w.IN(tl, A, '<.15', { x: -80, y: 0 }); w.IN(tl, Bb, '<.1', { x: 80, y: 0 });
    B(1); w.IN(tl, cu, 0, { scale: .2, y: 0 }); ['2', '1', '🤔'].forEach(function (s) { tl.call(function () { ct.textContent = s; }, null, '>+.45'); w.pop(tl, cu, '<'); });
    B(2); w.OUT(tl, cu, 0); tl.to(no, { opacity: .25, scale: .9, duration: .3 }, '<'); w.pop(tl, ok, '>'); tl.to(ok.querySelector('rect'), { attr: { stroke: C.verde, 'stroke-width': 10 }, duration: .3 }, '<'); w.IN(tl, rs, '>', { y: 40 });
  } };

  // patron: ¿qué sigue? Una secuencia con un hueco. {titulo, items:[...] (3-6, se muestran antes del hueco), falta, regla} — 3 pasos
  T.patron = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || '¿QUÉ SIGUE?'), all = d.items.concat(['?']), n = all.length, P = W.rejilla(n, 960, 560, Math.min(260, 1600 / n), 0, n);
    var it = all.map(function (s, k) { var q = k === n - 1, p = w.pieza(g, P[k][0], 560); w.caja(p, 0, 0, Math.min(230, 1600 / n - 20), 200, q ? 'rgba(244,182,63,.1)' : 'url(#gCard)', q ? C.sol : W.PAL[k % 4], 30, 6).setAttribute('filter', 'url(#sombra)');
      var t = w.txt(p, 0, 4, s, /\p{Extended_Pictographic}/u.test(s) ? 90 : 64, q ? C.sol : C.txt, /\p{Extended_Pictographic}/u.test(s) ? { 'font-family': '"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif', 'font-weight': 400 } : { 'font-weight': 800 }); p.t = t; return p; });
    var rg = w.pieza(g, 960, 820); w.multi(rg, 0, 0, '🧠 ' + d.regla, 42, C.txt, 1500);
    B(0); w.IN(tl, ti, 0); it.forEach(function (p, k) { w.IN(tl, p, '<.12', { y: 80, scale: .5 }); });
    B(1); var last = it[n - 1]; tl.to(last, { scale: 1.1, duration: .35, yoyo: true, repeat: 3 }, '>');
    B(2); tl.call(function () { last.t.textContent = d.falta; }, null, '>'); tl.to(last.querySelector('rect'), { attr: { stroke: C.verde, fill: 'rgba(139,227,143,.12)' }, duration: .3 }, '<'); w.pop(tl, last, '<'); w.IN(tl, rg, '>', { y: 30 });
  } };

  // ======================= ENTRENAMIENTO MENTAL =======================
  // contrarreloj: ronda rápida con reloj. {titulo, segundos, items:[{p, r}] (2-5)} — 1 + items pasos
  T.contrarreloj = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'RONDA RÁPIDA'), rel = w.pieza(g, 1620, 300), R = 70, L = 2 * Math.PI * R;
    w.el('circle', { r: R, fill: 'none', stroke: C.linea, 'stroke-width': 14 }, rel); var arco = w.el('circle', { r: R, fill: 'none', stroke: C.coral, 'stroke-width': 14, 'stroke-dasharray': L, 'stroke-dashoffset': 0, transform: 'rotate(-90)', 'stroke-linecap': 'round' }, rel);
    var seg = +d.segundos || 30, st = w.txt(rel, 0, 4, seg + '', 54, C.txt, { 'font-weight': 900 }), n = d.items.length, cuenta = w.pieza(g, 300, 300), cnt = w.txt(cuenta, 0, 0, '0/' + n, 48, C.sol, { 'font-weight': 900 });
    var it = d.items.map(function (o) { var p = w.pieza(g, 960, 600); w.tarjeta(p, 0, -60, 1300, 240, C.azul); w.multi(p, 0, -60, o.p, 58, C.txt, 1200);
      var r = w.pieza(p, 0, 180); w.caja(r, 0, 0, 900, 110, 'url(#gSol)', '#ffe7a8', 55, 5); w.multi(r, 0, 0, o.r, 48, '#3a2a00', 840); p.r = r; return p; });
    B(0); w.IN(tl, ti, 0); w.IN(tl, rel, '<.1', { scale: .3, y: 0 }); w.IN(tl, cuenta, '<');
    var paso = seg / n;
    it.forEach(function (p, k) { B(k + 1); if (k) w.OUT(tl, it[k - 1], 0, { x: -200, duration: .25 }); w.IN(tl, p, k ? '>' : 0, { x: 200, y: 0, d: .35 });
      tl.to(arco, { attr: { 'stroke-dashoffset': L * (k + 1) / n }, duration: .9, ease: 'none' }, '>'); w.contador(tl, st, seg - paso * k, seg - paso * (k + 1), '<', .9);
      w.IN(tl, p.r, '>', { scale: .3, y: 0, ease: 'back.out(2.5)', d: .35 }); tl.call(function (s) { cnt.textContent = s; }, [(k + 1) + '/' + n], '<'); w.pop(tl, cuenta, '<'); });
  } };

  // memoria: mirar, tapar y adivinar cuál falta. {titulo?, items:[...] (4-6), falta: índice} — 3 pasos
  T.memoria = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'MEMORIA'), n = d.items.length, P = W.rejilla(n, 960, 610, 440, 220, 3), f = (+d.falta || 0) % n;
    var it = d.items.map(function (s, k) { var p = w.pieza(g, P[k][0], P[k][1]); w.tarjeta(p, 0, 0, 400, 180, W.PAL[k % W.PAL.length]); w.multi(p, 0, 0, s, 46, C.txt, 360);
      var tapa = w.pieza(p, 0, 0); w.caja(tapa, 0, 0, 400, 180, 'url(#gAqua)', '#d8fff7', 30, 5); w.txt(tapa, 0, 0, '?', 90, '#06282a', { 'font-weight': 900 }); p.tapa = tapa; return p; });
    var preg = w.pieza(g, 960, 900); w.txt(preg, 0, 0, '¿Cuál desapareció?', 46, C.sol, { 'font-weight': 800 });
    B(0); w.IN(tl, ti, 0); it.forEach(function (p) { w.IN(tl, p, '<.08', { scale: .5, y: 0 }); });
    B(1); it.forEach(function (p) { w.IN(tl, p.tapa, '<.05', { scaleY: 0, y: 0, d: .3 }); }); tl.to(it[f], { opacity: .15, duration: .3 }, '>'); w.IN(tl, preg, '<');
    B(2); it.forEach(function (p, k) { if (k !== f) w.OUT(tl, p.tapa, '<.03', { scaleY: 0 }); }); tl.to(it[f], { opacity: 1, duration: .3 }, '>'); w.OUT(tl, it[f].tapa, '<'); w.pop(tl, it[f], '>'); tl.to(it[f].querySelector('rect'), { attr: { stroke: C.sol, 'stroke-width': 10 }, duration: .3 }, '<');
  } };

  // ======================= REPASO =======================
  // unir: dos columnas que se conectan con líneas. {titulo, pares:[[izq, der]] (2-5), mezclar?:true} — 1 + pares pasos
  T.unir = { n: function (d) { return 1 + d.pares.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), n = d.pares.length, gap = Math.min(150, 600 / n), y0 = 600 - (n - 1) * gap / 2, ord = d.pares.map(function (_, k) { return d.mezclar === false ? k : (k * 2 + 1) % n; });
    if (ord.slice().sort().join() !== d.pares.map(function (_, k) { return k; }).join()) ord = d.pares.map(function (_, k) { return n - 1 - k; });
    var Iz = d.pares.map(function (p, k) { return w.chip(g, 560, y0 + k * gap, 560, gap - 30, p[0], { r: 22, size: 38 }); });
    var De = d.pares.map(function (p, k) { var j = ord.indexOf(k); return w.chip(g, 1360, y0 + j * gap, 560, gap - 30, p[1], { r: 22, size: 38 }); });
    var Ls = d.pares.map(function (p, k) { var j = ord.indexOf(k), x1 = 840, y1 = y0 + k * gap, x2 = 1080, y2 = y0 + j * gap, len = Math.hypot(x2 - x1, y2 - y1);
      return w.el('line', { x1: x1, y1: y1, x2: x2, y2: y2, stroke: W.PAL[k % W.PAL.length], 'stroke-width': 8, 'stroke-linecap': 'round', 'stroke-dasharray': len, 'stroke-dashoffset': len }, g); });
    B(0); w.IN(tl, ti, 0); Iz.forEach(function (o) { w.IN(tl, o, '<.06', { x: -60, y: 0 }); }); De.forEach(function (o) { w.IN(tl, o, '<.06', { x: 60, y: 0 }); });
    Ls.forEach(function (l, k) { B(k + 1); var c = W.PAL[k % W.PAL.length]; tl.to(Iz[k].r, { attr: { stroke: c }, duration: .2 }, '>'); tl.to(l, { attr: { 'stroke-dashoffset': 0 }, duration: .5 }, '>'); tl.to(De[k].r, { attr: { stroke: c }, duration: .2 }, '>'); w.pop(tl, De[k], '<'); });
  } };

  // mazo: un mazo de tarjetas que se dan vuelta y pasan a la pila de aprendidas. {titulo?, items:[{frente, dorso, emoji?}] (1-5)} — un paso por tarjeta
  T.mazo = { n: function (d) { return d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'REPASO'), n = d.items.length, pila = w.pieza(g, 1620, 860), pt = w.txt(pila, 0, 0, '✔ 0/' + n, 40, C.verde, { 'font-weight': 800 });
    var Ts = d.items.map(function (it, k) { var j = n - 1 - k, base = w.el('g', { transform: 'translate(' + (900 + j * 10) + ' ' + (600 - j * 10) + ')', opacity: 0 }, g);
      var fr = w.el('g', { 'data-c': 1 }, base); w.tarjeta(fr, 0, 0, 820, 460, W.PAL[k % W.PAL.length]); if (it.emoji) w.emoji(fr, 0, -100, it.emoji, 110); w.multi(fr, 0, it.emoji ? 70 : 0, it.frente, 64, C.txt, 740); w.txt(fr, 330, -190, 'FRENTE', 22, C.suave);
      var bk = w.el('g', { 'data-c': 1, opacity: 0 }, base); w.tarjeta(bk, 0, 0, 820, 460, C.sol); w.txt(bk, 330, -190, 'DORSO', 22, C.suave); w.multi(bk, 0, 0, it.dorso, 54, C.txt, 740);
      return { b: base, fr: fr, bk: bk }; });
    Ts.slice().reverse().forEach(function (t) { g.appendChild(t.b); });
    Ts.forEach(function (t, k) { B(k); if (!k) { w.IN(tl, ti, 0); Ts.forEach(function (u) { tl.fromTo(u.b, { opacity: 0 }, { opacity: 1, duration: .3 }, '<.05'); }); w.IN(tl, pila, '<'); }
      tl.to(t.b, { attr: { transform: 'translate(900 600)' }, duration: .25 }, '>'); tl.to(t.fr, { scaleX: 0, duration: .25, ease: 'power1.in' }, '>+.4'); tl.set(t.fr, { opacity: 0 }); tl.fromTo(t.bk, { scaleX: 0, opacity: 1 }, { scaleX: 1, duration: .25, ease: 'power1.out' }, '>');
      if (k < n - 1) tl.to(t.b, { x: '+=720', y: '+=260', scale: .15, opacity: 0, duration: .5, ease: 'power2.in' }, '>+1.2'); tl.call(function (s) { pt.textContent = s; }, ['✔ ' + (k + 1) + '/' + n], '>'); w.pop(tl, pila, '<'); });
  } };

  // tipeo: la respuesta se escribe letra por letra, como en un repaso de escritura. {titulo?, items:[{p, r}] (1-4)} — un paso por item
  T.tipeo = { n: function (d) { return d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'ESCRIBÍ LA RESPUESTA'), n = d.items.length, gap = Math.min(190, 640 / n), y0 = 600 - (n - 1) * gap / 2;
    var R = d.items.map(function (it, k) { var y = y0 + k * gap, p = w.pieza(g, 960, y); w.txt(p, -420, 0, it.p, 44, C.txt, { 'text-anchor': 'end' }); w.txt(p, -380, 0, '→', 44, C.suave);
      w.caja(p, 220, 0, 1080, gap - 40, 'rgba(255,255,255,.05)', C.linea, 18, 4); var t = w.txt(p, -300, 0, '', 46, C.sol, { 'text-anchor': 'start', 'font-weight': 800 }), ck = w.txt(p, 720, 0, '', 46, C.verde); return { p: p, t: t, ck: ck, r: String(it.r) }; });
    R.forEach(function (o, k) { B(k); if (!k) w.IN(tl, ti, 0); w.IN(tl, o.p, 0, { x: -60, y: 0 }); var obj = { v: 0 };
      tl.to(obj, { v: o.r.length, duration: Math.min(1.6, .06 * o.r.length + .3), ease: 'none', onUpdate: function () { o.t.textContent = o.r.slice(0, Math.round(obj.v)) + (obj.v < o.r.length ? '|' : ''); } }, '>');
      tl.call(function () { o.ck.textContent = '✔'; }, null, '>'); w.pop(tl, o.p, '<'); });
  } };

  // ======================= DOCUMENTAL =======================
  // documental: escena con bandas de cine, zoom lento y rótulos. {emojis:[...] (1-4), lugar?, rotulos:[{txt, sub?}] (1-4)} — un paso por rótulo
  T.documental = { n: function (d) { return d.rotulos.length; }, armar: function (g, tl, B, d) {
    var esc = w.pieza(g, 960, 540), E = d.emojis || [d.emoji || '🌍'], P = W.rejilla(E.length, 0, -40, 420, 0, E.length);
    E.forEach(function (e, k) { w.emoji(esc, P[k][0], P[k][1] + (k % 2 ? 40 : -20), e, E.length > 2 ? 230 : 320); });
    var bs = w.el('rect', { x: 0, y: -140, width: 1920, height: 140, fill: '#000' }, g), bi = w.el('rect', { x: 0, y: 1080, width: 1920, height: 140, fill: '#000' }, g);
    var lugar = w.pieza(g, 210, 190); if (d.lugar) w.txt(lugar, 0, 0, '📍 ' + d.lugar, 34, C.txt, { 'text-anchor': 'start', 'letter-spacing': 2 });
    var R = d.rotulos.map(function (r) { var p = w.pieza(g, 160, 810); w.el('rect', { x: 0, y: -70, width: 14, height: r.sub ? 140 : 90, fill: C.sol }, p);
      w.txt(p, 40, -30, r.txt, 54, '#fff', { 'text-anchor': 'start', 'font-weight': 800 }); if (r.sub) w.txt(p, 40, 34, r.sub, 34, C.suave, { 'text-anchor': 'start' }); return p; });
    R.forEach(function (p, k) { B(k);
      if (!k) { tl.to(bs, { attr: { y: 0 }, duration: .5 }, '>'); tl.to(bi, { attr: { y: 940 }, duration: .5 }, '<'); w.IN(tl, esc, '<', { scale: 1.25, y: 0, d: 1.2, ease: 'power2.out' }); tl.to(esc, { scale: 1.08, x: k % 2 ? -30 : 30, duration: 6, ease: 'none' }, '>'); if (d.lugar) w.IN(tl, lugar, '<', { x: -40, y: 0 }); }
      else { w.OUT(tl, R[k - 1], 0, { x: -60 }); tl.to(esc, { x: k % 2 ? -40 : 40, scale: 1 + .06 * (k + 1), duration: 4, ease: 'none' }, '<'); }
      w.IN(tl, p, k ? '<.2' : '<.3', { x: -80, y: 0, ease: 'power3.out' }); });
  } };

  // escala: objetos que crecen para comparar tamaños o cantidades. {titulo, items:[{txt, emoji, valor}] (2-5, de menor a mayor)} — un paso por item
  T.escala = { n: function (d) { return d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), n = d.items.length, mx = Math.max.apply(null, d.items.map(function (i) { return +i.valor || 1; })), x0 = 960 - (n - 1) * 170;
    var piso = w.el('line', { x1: 200, y1: 860, x2: 1720, y2: 860, stroke: C.linea, 'stroke-width': 6, opacity: 0 }, g);
    var I = d.items.map(function (it, k) { var s = 60 + 360 * Math.sqrt((+it.valor || 1) / mx), x = n > 1 ? 960 + (k - (n - 1) / 2) * Math.min(360, 1500 / n) : 960, p = w.pieza(g, x, 860);
      w.emoji(p, 0, -s / 2, it.emoji, s); var c = w.pieza(p, 0, 50); w.txt(c, 0, 0, it.txt, 32, C.sol, { 'font-weight': 800 }); return p; });
    I.forEach(function (p, k) { B(k); if (!k) { w.IN(tl, ti, 0); tl.to(piso, { opacity: 1, duration: .3 }, '<'); } w.IN(tl, p, 0, { scale: 0, y: 0, ease: 'back.out(1.6)', d: .7 }); });
  } };

  // ======================= HISTORIA CON DILEMA =======================
  // dilema: una situación con dos caminos y sus consecuencias. {situacion, emoji, a:{txt, consecuencia, emoji?}, b:{...}} — 3 pasos
  T.dilema = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var s = w.pieza(g, 960, 330); w.tarjeta(s, 0, 0, 1300, 190, C.aqua); w.emoji(s, -560, 0, d.emoji || '🤔', 100); w.multi(s, 60, 0, d.situacion, 44, C.txt, 1050);
    function cam(x, o, col, sg) { var f = w.flecha(g, 960, 440, x, 560, col, 8), p = w.pieza(g, x, 700); w.tarjeta(p, 0, 0, 700, 300, col);
      w.emoji(p, -270, -90, o.emoji || (sg ? '➡️' : '⬅️'), 60); w.multi(p, 30, -80, o.txt, 40, C.txt, 560); w.el('line', { x1: -300, y1: -20, x2: 300, y2: -20, stroke: C.linea, 'stroke-width': 3 }, p); w.multi(p, 0, 70, '→ ' + o.consecuencia, 36, col, 620); return { f: f, p: p }; }
    var A = cam(540, d.a, C.azul, 0), Bb = cam(1380, d.b, C.coral, 1);
    B(0); w.IN(tl, s, 0, { y: -40 });
    B(1); w.dibujarFlecha(tl, A.f, 0); w.IN(tl, A.p, '>', { x: -60, y: 0 });
    B(2); w.dibujarFlecha(tl, Bb.f, 0); w.IN(tl, Bb.p, '>', { x: 60, y: 0 });
  } };

  // ======================= QUIZ DE COLORES =======================
  // quiz4: pregunta con 2 a 4 opciones de color y forma, barra de tiempo y revelación. {pregunta, opciones (2-4), correcta (índice)} — 3 pasos
  var FORMAS = [['▲', '#e2453c'], ['◆', '#1f72d6'], ['●', '#d89e00'], ['■', '#26890c']];
  T.quiz4 = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var q = w.pieza(g, 960, 300); w.caja(q, 0, 0, 1640, 160, '#fff', '#fff', 24, 2); w.multi(q, 0, 0, d.pregunta, 50, '#1a1a1a', 1560);
    var bar = w.el('rect', { x: 140, y: 400, width: 1640, height: 16, rx: 8, fill: C.sol, opacity: 0 }, g);
    var n = d.opciones.length, P = W.rejilla(n, 960, 660, 820, 200, 2), O = d.opciones.map(function (o, k) { var p = w.pieza(g, P[k][0], P[k][1]), f = FORMAS[k % 4];
      w.caja(p, 0, 0, 790, 170, f[1], f[1], 18, 2).setAttribute('filter', 'url(#sombra)'); w.txt(p, -330, 0, f[0], 70, '#fff'); w.multi(p, 40, 0, o, 42, '#fff', 640); return p; });
    B(0); w.IN(tl, q, 0, { y: -30 });
    B(1); O.forEach(function (o, k) { w.IN(tl, o, k ? '<.08' : 0, { scale: .5, y: 0, ease: 'back.out(2)' }); }); tl.to(bar, { opacity: 1, duration: .1 }, '>'); tl.to(bar, { attr: { width: 0, x: 960 }, duration: 2.6, ease: 'none' }, '>');
    B(2); O.forEach(function (o, k) { if (k !== d.correcta) tl.to(o, { opacity: .2, scale: .95, duration: .3 }, '<'); }); var c = O[d.correcta] || O[0]; w.pop(tl, c, '>'); w.IN(tl, (function () { var t = w.pieza(c, 330, -60); w.emoji(t, 0, 0, '✅', 70); return t; })(), '<', { scale: 0, y: 0 });
  } };

  // ======================= TRANSFORMACIONES =======================
  // transforma: una expresión que se transforma paso a paso (cuentas, contracciones, fórmulas). {titulo, pasos:[{txt, nota?}] (2-5)} — un paso por item
  T.transforma = { n: function (d) { return d.pasos.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), n = d.pasos.length;
    var Ps = d.pasos.map(function (p, k) { var e = w.pieza(g, 960, 560), t = w.txt(e, 0, 0, p.txt, Math.min(96, 1600 / Math.max(6, String(p.txt).length * .56)), k === n - 1 ? C.sol : C.txt, { 'font-weight': 800 });
      var nt = w.pieza(g, 960, 760); if (p.nota) w.multi(nt, 0, 0, p.nota, 40, C.aqua, 1400); return { e: e, nt: nt }; });
    var hist = [];
    Ps.forEach(function (o, k) { B(k); if (!k) w.IN(tl, ti, 0);
      if (k) { var prev = Ps[k - 1]; w.OUT(tl, prev.nt, 0, { duration: .2 }); tl.to(prev.e, { scale: .45, opacity: .45, duration: .5, ease: 'power2.inOut' }, '<'); tl.to(prev.e.parentNode, { attr: { transform: 'translate(960 ' + (390 + (k - 1) * 0) + ')' }, duration: .5 }, '<');
        hist.forEach(function (h) { tl.to(h, { opacity: 0, duration: .2 }, '<'); }); hist.push(prev.e); }
      w.IN(tl, o.e, k ? '<.25' : 0, { scale: 1.6, y: 0, d: .6, ease: 'power3.out' }); if (d.pasos[k].nota) w.IN(tl, o.nt, '>', { y: 20 }); });
  } };
})();
