/* PLANTILLAS · PROCESOS, TIEMPO, MAPAS Y DATOS */
(function () {
  var w = W, C = w.C;

  // pasos: {titulo, items:[txt | {txt, emoji}]} (máx 6) — 1 + n pasos
  T.pasos = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), n = d.items.length, h = Math.min(120, 640 / n), y0 = 400 + h / 2 - 20;
    var I = d.items.map(function (it, k) { it = typeof it === 'string' ? { txt: it } : it; var p = w.pieza(g, 960, y0 + k * h);
      w.caja(p, 0, 0, 1400, h - 18, 'url(#gCard)', C.linea, 22, 4); w.el('circle', { cx: -640, cy: 0, r: (h - 18) / 2 - 8, fill: 'url(#gAqua)' }, p);
      w.txt(p, -640, 2, it.emoji || String(k + 1), it.emoji ? 40 : 38, '#06282a', it.emoji ? { 'font-family': '"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji"', 'font-weight': 400 } : null);
      w.txt(p, -570, 2, it.txt, Math.min(42, h * .36), C.txt, { 'text-anchor': 'start' }); return p; });
    B(0); w.IN(tl, ti, 0); I.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { x: -120, y: 0 }); });
  } };

  // ciclo: {titulo, items:[txt | {txt, emoji}]} (3-6) — 1 + n pasos, al final gira
  T.ciclo = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo, 255), n = d.items.length, cx = 960, cy = 660, R = 230;
    var aro = w.pieza(g, cx, cy); w.el('circle', { r: R, fill: 'none', stroke: C.linea, 'stroke-width': 10, 'stroke-dasharray': '30 20' }, aro);
    var I = d.items.map(function (it, k) { it = typeof it === 'string' ? { txt: it } : it; var a = -Math.PI / 2 + k * 2 * Math.PI / n, p = w.pieza(g, cx + R * Math.cos(a), cy + R * Math.sin(a));
      w.el('circle', { r: 95, fill: 'url(#gCard)', stroke: W.PAL[k % W.PAL.length], 'stroke-width': 6, filter: 'url(#sombra)' }, p);
      if (it.emoji) w.emoji(p, 0, -22, it.emoji, 60); w.multi(p, 0, it.emoji ? 42 : 0, it.txt, 26, C.txt, 170); return p; });
    B(0); w.IN(tl, ti, 0); w.IN(tl, aro, '<', { scale: .5, y: 0 });
    I.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { scale: 0, y: 0, ease: 'back.out(2.5)' }); if (k === n - 1) tl.to(aro, { rotation: 360, svgOrigin: cx + ' ' + cy, duration: 2, ease: 'power2.inOut' }, '>'); });
  } };

  // flujo: {titulo, items:[txt | {txt, emoji}]} (2-5, en fila con flechas) — n pasos (el título va con el primero)
  T.flujo = { n: function (d) { return d.items.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, n = d.items.length, gap = 1560 / n, x0 = 960 - (n - 1) * gap / 2, bw = Math.min(300, gap - 70);
    var I = d.items.map(function (it, k) { it = typeof it === 'string' ? { txt: it } : it; var p = w.pieza(g, x0 + k * gap, 620); w.tarjeta(p, 0, 0, bw, 300, W.PAL[k % W.PAL.length]);
      if (it.emoji) w.emoji(p, 0, -60, it.emoji, 90); w.multi(p, 0, it.emoji ? 70 : 0, it.txt, 32, C.txt, bw - 30); return p; });
    var F = []; for (var k = 0; k < n - 1; k++) F.push(w.flecha(g, x0 + k * gap + bw / 2 + 8, 620, x0 + (k + 1) * gap - bw / 2 - 8, 620, C.sol, 8));
    I.forEach(function (p, k) { B(k); if (k === 0 && ti) w.IN(tl, ti, 0); if (k) w.dibujarFlecha(tl, F[k - 1], 0); w.IN(tl, p, k ? '>' : (ti ? '<.1' : 0), { scale: .6, y: 0 }); });
  } };

  // causas: {causa:{txt, emoji}, items:[txt | {txt, emoji}] (2-4 consecuencias)} — 1 + n pasos
  T.causas = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var c = w.pieza(g, 960, 380); w.caja(c, 0, 0, 760, 170, 'url(#gSol)', '#ffe7a8', 40, 6).setAttribute('filter', 'url(#sombra)');
    if (d.causa.emoji) w.emoji(c, -300, 0, d.causa.emoji, 80); w.multi(c, d.causa.emoji ? 50 : 0, 0, d.causa.txt, 44, '#3a2a00', 580);
    var n = d.items.length, P = W.rejilla(n, 960, 800, 1560 / n, 0, n);
    var I = d.items.map(function (it, k) { it = typeof it === 'string' ? { txt: it } : it; var p = w.pieza(g, P[k][0], 800); w.tarjeta(p, 0, 0, Math.min(440, 1560 / n - 40), 230, C.aqua);
      if (it.emoji) w.emoji(p, 0, -50, it.emoji, 70); w.multi(p, 0, it.emoji ? 50 : 0, it.txt, 32, C.txt, Math.min(400, 1560 / n - 80)); p.f = w.flecha(g, 960, 470, P[k][0], 680, C.sol, 7); return p; });
    B(0); w.IN(tl, c, 0, { scale: .6, y: 0 });
    I.forEach(function (p, k) { B(k + 1); w.dibujarFlecha(tl, p.f, 0); w.IN(tl, p, '>', { y: 60 }); });
  } };

  // linea: {titulo, eventos:[{fecha, txt, emoji}] (2-6)} — n pasos (el título va con el primero)
  T.linea = { n: function (d) { return d.eventos.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, n = d.eventos.length, gap = 1280 / Math.max(1, n - 1), x0 = 960 - (n - 1) * gap / 2;
    var eje = w.pieza(g, 0, 0); var L = w.el('line', { x1: 190, y1: 640, x2: 1730, y2: 640, stroke: C.linea, 'stroke-width': 10, 'stroke-linecap': 'round' }, eje);
    var E = d.eventos.map(function (e, k) { var x = n === 1 ? 960 : x0 + k * gap, arriba = k % 2 === 0, p = w.pieza(g, x, 640);
      w.el('circle', { r: 22, fill: C.sol, stroke: '#ffe7a8', 'stroke-width': 5 }, p); w.el('line', { x1: 0, y1: arriba ? -30 : 30, x2: 0, y2: arriba ? -90 : 90, stroke: C.sol, 'stroke-width': 4 }, p);
      var yb = arriba ? -200 : 200, cw = Math.min(330, gap - 20); w.tarjeta(p, 0, yb, cw, 200, C.aqua);
      var ft = w.txt(p, e.emoji ? 26 : 0, yb - 58, e.fecha, 38, C.sol); if (e.emoji) w.emoji(p, -String(e.fecha).length * 11 - 20, yb - 58, e.emoji, 42);
      w.multi(p, 0, yb + 28, e.txt, 30, C.txt, cw - 40); return p; });
    E.forEach(function (p, k) { B(k); if (k === 0) { if (ti) w.IN(tl, ti, 0); w.IN(tl, eje, ti ? '<' : 0, { scaleX: 0, y: 0, d: .5, ease: 'power2.out' }); } w.IN(tl, p, k ? 0 : '>', { scale: .4, y: 0, ease: 'back.out(2)' }); });
  } };

  // mapa: {zona:'mundo'|'america'|'sudamerica'|'argentina', pasos:[{resaltar:['Argentina'], color, marcas:[{lon, lat, txt}], ruta:[[lon,lat],[lon,lat]], texto}]} — 1 + pasos
  T.mapa = { n: function (d) { return 1 + (d.pasos || []).length; }, armar: function (g, tl, B, d) {
    var M = (window.MAPAS || {})[d.zona || 'mundo']; if (!M) { B(0); (d.pasos || []).forEach(function (_, k) { B(k + 1); }); return; }
    var ox = 160, oy = 250, pro = function (lon, lat) { var l = lon * Math.PI / 180, f = lat * Math.PI / 180; return [ox + M.s * l + M.t[0], oy - M.s * Math.log(Math.tan(Math.PI / 4 + f / 2)) + M.t[1]]; };
    var mapa = w.pieza(g, 0, 0), P = {};
    var clip = w.el('clipPath', { id: 'clipMapa' }, mapa); w.el('rect', { x: ox, y: oy, width: 1600, height: 720, rx: 30 }, clip);
    var cont = w.el('g', { 'clip-path': 'url(#clipMapa)' }, mapa); w.el('rect', { x: ox, y: oy, width: 1600, height: 720, rx: 30, fill: 'rgba(0,0,0,.2)' }, cont);
    var gp = w.el('g', { transform: 'translate(' + ox + ' ' + oy + ')' }, cont);
    for (var nm in M.paises) P[nm] = w.el('path', { d: M.paises[nm], fill: '#1e474b', stroke: '#2f6468', 'stroke-width': 1.5 }, gp);
    B(0); w.IN(tl, mapa, 0, { scale: 1.05, y: 0, d: .8, ease: 'power2.out' });
    (d.pasos || []).forEach(function (s, k) { B(k + 1); var col = s.color || W.PAL[k % W.PAL.length], first = true;
      (s.resaltar || []).forEach(function (nm) { if (P[nm]) { tl.to(P[nm], { attr: { fill: col }, duration: .4 }, first ? '>' : '<.08'); first = false; } });
      if (s.ruta) { var a = pro(s.ruta[0][0], s.ruta[0][1]), b = pro(s.ruta[1][0], s.ruta[1][1]), f = w.flecha(g, a[0], a[1], b[0], b[1], col, 8); w.dibujarFlecha(tl, f, first ? 0 : '<'); first = false; }
      (s.marcas || []).forEach(function (m) { var q = pro(m.lon, m.lat), p = w.pieza(g, q[0], q[1]); w.el('circle', { r: 14, fill: col, stroke: '#fff', 'stroke-width': 4 }, p);
        var tw = m.txt.length * 17 + 40; w.caja(p, 0, -50, tw, 56, 'rgba(6,20,22,.85)', col, 28, 3); w.txt(p, 0, -50, m.txt, 28, '#fff'); w.IN(tl, p, first ? 0 : '<.1', { scale: 0, y: 0, ease: 'back.out(3)' }); first = false; });
      if (s.texto) { var t = w.chip(g, 960, 930, Math.min(1500, s.texto.length * 22 + 100), 80, s.texto, { size: 36, fill: 'rgba(6,20,22,.9)', stroke: col }); w.IN(tl, t, first ? 0 : '<.1'); }
    });
  } };

  // barras: {titulo, unidad, items:[{txt, valor}] (2-7)} — 1 + n pasos (cada paso crece una barra)
  T.barras = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), n = d.items.length, max = Math.max.apply(null, d.items.map(function (i) { return i.valor; })), gap = 1400 / n, x0 = 960 - (n - 1) * gap / 2, bw = Math.min(170, gap - 40), y0 = 900, H = 470;
    var eje = w.pieza(g, 0, 0); w.el('line', { x1: 220, y1: y0, x2: 1700, y2: y0, stroke: C.suave, 'stroke-width': 4 }, eje);
    var I = d.items.map(function (it, k) { var x = x0 + k * gap, h = Math.max(6, it.valor / max * H), p = w.el('g', {}, g);
      var r = w.el('rect', { x: x - bw / 2, y: y0 - h, width: bw, height: h, rx: 14, fill: W.PAL[k % W.PAL.length], transform: 'translate(0 0)' }, p);
      w.txt(p, x, y0 + 40, it.txt, 28, C.txt); var v = w.txt(p, x, y0 - h - 36, (it.valor).toLocaleString('es-AR') + (d.unidad ? ' ' + d.unidad : ''), 34, C.sol, { opacity: 0 });
      return { r: r, v: v, h: h, x: x, p: p }; });
    I.forEach(function (b) { b.r.setAttribute('height', 0); b.r.setAttribute('y', y0); b.p.setAttribute('opacity', 0); });
    B(0); w.IN(tl, ti, 0); w.IN(tl, eje, '<');
    I.forEach(function (b, k) { B(k + 1); tl.to(b.p, { opacity: 1, duration: .1 }); tl.to(b.r, { attr: { height: b.h, y: y0 - b.h }, duration: .7, ease: 'power3.out' }, '<'); tl.to(b.v, { opacity: 1, duration: .3 }, '>-.2'); });
  } };

  // torta: {titulo, items:[{txt, valor}] (2-6)} — 1 + n pasos
  T.torta = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), tot = d.items.reduce(function (a, i) { return a + i.valor; }, 0), cx = 760, cy = 640, R = 280, a0 = -Math.PI / 2;
    var base = w.pieza(g, cx, cy); w.el('circle', { r: R, fill: '#12302f', stroke: C.linea, 'stroke-width': 6 }, base);
    var I = d.items.map(function (it, k) { var a1 = a0 + it.valor / tot * 2 * Math.PI, la = a1 - a0 > Math.PI ? 1 : 0, col = W.PAL[k % W.PAL.length];
      var p = w.pieza(g, cx, cy); w.el('path', { d: 'M0 0 L' + R * Math.cos(a0) + ' ' + R * Math.sin(a0) + ' A' + R + ' ' + R + ' 0 ' + la + ' 1 ' + R * Math.cos(a1) + ' ' + R * Math.sin(a1) + ' Z', fill: col, stroke: '#0c292b', 'stroke-width': 4 }, p);
      var l = w.pieza(g, 1350, 420 + k * 95); w.el('rect', { x: -260, y: -26, width: 52, height: 52, rx: 12, fill: col }, l); w.txt(l, -190, 0, it.txt + ' · ' + Math.round(it.valor / tot * 100) + '%', 36, C.txt, { 'text-anchor': 'start' });
      a0 = a1; return [p, l]; });
    B(0); w.IN(tl, ti, 0); w.IN(tl, base, '<', { scale: 0, y: 0 });
    I.forEach(function (q, k) { B(k + 1); w.IN(tl, q[0], 0, { scale: .3, y: 0, ease: 'back.out(1.8)' }); w.IN(tl, q[1], '<.1', { x: 60, y: 0 }); });
  } };

  // curva: {titulo, x:'tiempo (s)', y:'distancia (m)', puntos:[[x,y]...], marcas:[{x, y, txt}]} — 2 + marcas pasos
  T.curva = { n: function (d) { return 2 + (d.marcas || []).length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 270) : null, X0 = 300, X1 = 1650, Y0 = 930, Y1 = 380, pts = d.puntos;
    var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; }), mnx = Math.min.apply(null, xs.concat(d.xmin != null ? [d.xmin] : [])), mxx = Math.max.apply(null, xs), mny = Math.min.apply(null, ys.concat([0])), mxy = Math.max.apply(null, ys);
    var sx = function (v) { return X0 + (v - mnx) / (mxx - mnx || 1) * (X1 - X0); }, sy = function (v) { return Y0 - (v - mny) / (mxy - mny || 1) * (Y0 - Y1); };
    var ejes = w.pieza(g, 0, 0); w.el('line', { x1: X0, y1: Y0, x2: X1 + 30, y2: Y0, stroke: C.suave, 'stroke-width': 5 }, ejes); w.el('line', { x1: X0, y1: Y0, x2: X0, y2: Y1 - 30, stroke: C.suave, 'stroke-width': 5 }, ejes);
    w.txt(ejes, X1, Y0 + 45, d.x || 'x', 30, C.aqua, { 'text-anchor': 'end' }); w.txt(ejes, X0 + 20, Y1 - 50, d.y || 'y', 30, C.aqua, { 'text-anchor': 'start' });
    var dd = pts.map(function (p, i) { return (i ? 'L' : 'M') + sx(p[0]).toFixed(1) + ' ' + sy(p[1]).toFixed(1); }).join(' ');
    var c = w.el('path', { d: dd, fill: 'none', stroke: C.sol, 'stroke-width': 9, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', filter: 'url(#brillo)' }, g); var L = 6000; c.setAttribute('stroke-dasharray', L); c.setAttribute('stroke-dashoffset', L);
    var MK = (d.marcas || []).map(function (m) { var p = w.pieza(g, sx(m.x), sy(m.y)); w.el('circle', { r: 16, fill: C.coral, stroke: '#fff', 'stroke-width': 4 }, p); var tw = m.txt.length * 17 + 40; w.caja(p, 0, -56, tw, 58, 'rgba(6,20,22,.88)', C.coral, 28, 3); w.txt(p, 0, -56, m.txt, 28, '#fff'); return p; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, ejes, ti ? '<' : 0);
    B(1); tl.to(c, { attr: { 'stroke-dashoffset': 0 }, duration: 1.6, ease: 'power1.inOut' });
    MK.forEach(function (p, k) { B(k + 2); w.IN(tl, p, 0, { scale: 0, y: 0, ease: 'back.out(3)' }); });
  } };

  // porcentaje: {valor: 24, txt:'VOLUNTAD', emoji} — 2 pasos: se llena, explicación
  T.porcentaje = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var p = w.pieza(g, 700, 620); w.caja(p, 0, 0, 300, 560, '#0b1c1d', C.suave, 40, 8); w.caja(p, 0, -300, 120, 40, C.suave, C.suave, 10, 2);
    var col = d.valor < 30 ? C.coral : d.valor < 65 ? C.sol : C.verde, H = 520, fill = w.el('rect', { x: -130, y: 260, width: 260, height: 0, rx: 28, fill: col }, p);
    var num = w.txt(p, 0, -40, '0%', 110, '#fff');
    var tx = w.pieza(g, 1300, 620); if (d.emoji) w.emoji(tx, 0, -120, d.emoji, 120); w.multi(tx, 0, 60, d.txt, 48, C.txt, 700);
    B(0); w.IN(tl, p, 0); tl.to(fill, { attr: { height: H * d.valor / 100, y: 260 - H * d.valor / 100 }, duration: 1.3, ease: 'power2.out' }); w.contador(tl, num, 0, d.valor, '<', 1.3, function (v) { return Math.round(v) + '%'; });
    B(1); w.IN(tl, tx, 0, { x: 100, y: 0 });
  } };
})();
