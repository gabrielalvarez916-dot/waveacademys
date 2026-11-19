/* PLANTILLAS · CIENCIAS, LENGUA E INGLÉS */
(function () {
  var w = W, C = w.C;

  // partes: {emoji (o dibujo grande), titulo, partes:[{txt, x, y}] (x, y entre -1 y 1 respecto del dibujo)} — 1 + partes pasos
  T.partes = { n: function (d) { return 1 + d.partes.length; }, armar: function (g, tl, B, d) {
    var cx = 960, cy = 620, R = 230, ti = d.titulo ? w.titulo(g, d.titulo, 270) : null;
    var o = w.pieza(g, cx, cy); w.el('circle', { r: R + 30, fill: 'rgba(127,211,196,.08)', stroke: C.linea, 'stroke-width': 4 }, o); w.emoji(o, 0, 10, d.emoji, 340);
    var P = d.partes.map(function (p, k) { var px = cx + p.x * R, py = cy + p.y * R, der = p.x >= 0, lx = der ? 1420 : 500, ly = Math.max(330, Math.min(930, py)), col = W.PAL[k % W.PAL.length];
      var gr = w.pieza(g, 0, 0); w.el('circle', { cx: px, cy: py, r: 12, fill: col, stroke: '#fff', 'stroke-width': 4 }, gr);
      w.el('polyline', { points: px + ',' + py + ' ' + (der ? lx - 170 : lx + 170) + ',' + ly + ' ' + (der ? lx - 150 : lx + 150) + ',' + ly, fill: 'none', stroke: col, 'stroke-width': 4 }, gr);
      var tw = Math.max(200, p.txt.length * 20 + 50); w.caja(gr, lx + (der ? tw / 2 - 150 : -tw / 2 + 150), ly, tw, 70, 'rgba(6,20,22,.9)', col, 30, 4); w.txt(gr, lx + (der ? tw / 2 - 150 : -tw / 2 + 150), ly, p.txt, 32, '#fff'); return gr; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, o, ti ? '<.1' : 0, { scale: .4, y: 0, ease: 'back.out(1.8)' });
    P.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { scale: .9, y: 0, d: .4 }); });
  } };

  // molecula: {titulo, atomos:[{el:'C', x, y}] (x, y en px desde el centro), enlaces:[[i, j, orden]], nombre} — 3 pasos
  T.molecula = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var COL = { C: '#3a3a3a', H: '#f0f0f0', O: '#ff5a4f', N: '#5f8bff', Cl: '#5fd35f', S: '#ffd34f', P: '#ff9f40', Na: '#b48cff' }, cx = 960, cy = 600;
    var ti = d.titulo ? w.titulo(g, d.titulo, 270) : null, E = w.el('g', {}, g), A = [];
    (d.enlaces || []).forEach(function (e) { var a = d.atomos[e[0]], b = d.atomos[e[1]], o = e[2] || 1;
      for (var k = 0; k < o; k++) { var off = (k - (o - 1) / 2) * 16, ang = Math.atan2(b.y - a.y, b.x - a.x) + Math.PI / 2;
        var l = w.el('line', { x1: cx + a.x + Math.cos(ang) * off, y1: cy + a.y + Math.sin(ang) * off, x2: cx + b.x + Math.cos(ang) * off, y2: cy + b.y + Math.sin(ang) * off, stroke: C.suave, 'stroke-width': 10, 'stroke-linecap': 'round' }, E);
        var L = Math.hypot(b.x - a.x, b.y - a.y); l.setAttribute('stroke-dasharray', L); l.setAttribute('stroke-dashoffset', L); } });
    d.atomos.forEach(function (a) { var p = w.pieza(g, cx + a.x, cy + a.y), r = a.el === 'H' ? 46 : 68; w.el('circle', { r: r, fill: COL[a.el] || C.lila, stroke: '#fff', 'stroke-opacity': .5, 'stroke-width': 4, filter: 'url(#sombra)' }, p);
      w.el('circle', { cx: -r * .35, cy: -r * .35, r: r * .3, fill: '#fff', opacity: .25 }, p); w.txt(p, 0, 3, a.el, r * .8, a.el === 'H' ? '#333' : '#fff'); A.push(p); });
    var nm = d.nombre ? w.etiqueta(g, 960, 940, d.nombre) : null;
    B(0); if (ti) w.IN(tl, ti, 0); A.forEach(function (a, k) { w.IN(tl, a, k ? '<.08' : (ti ? '<' : 0), { scale: 0, y: 0, ease: 'back.out(3)' }); });
    B(1); tl.to(E.querySelectorAll('line'), { attr: { 'stroke-dashoffset': 0 }, duration: .5, stagger: .08 });
    B(2); if (nm) w.IN(tl, nm, 0); else tl.to({}, { duration: .1 }); tl.to(A, { y: -8, duration: .5, yoyo: true, repeat: 3, ease: 'sine.inOut', stagger: .05 }, '<');
  } };

  // fuerzas: {cuerpo:'📦', inclinado: grados (opcional), fuerzas:[{txt, ang (grados, 0 = derecha, 90 = arriba), largo, color}]} — 1 + fuerzas pasos
  T.fuerzas = { n: function (d) { return 1 + d.fuerzas.length; }, armar: function (g, tl, B, d) {
    var cx = 960, cy = 600, inc = d.inclinado || 0, piso = w.pieza(g, 0, 0), a = inc * Math.PI / 180;
    if (inc) w.el('path', { d: 'M' + (cx - 650) + ' ' + (cy + 120 + 650 * Math.tan(a)) + ' L' + (cx + 650) + ' ' + (cy + 120 + 650 * Math.tan(a)) + ' L' + (cx + 650) + ' ' + (cy + 120 - 650 * Math.tan(a)) + ' Z', fill: '#1e474b', stroke: C.linea, 'stroke-width': 5 }, piso);
    else w.el('line', { x1: cx - 650, y1: cy + 110, x2: cx + 650, y2: cy + 110, stroke: C.suave, 'stroke-width': 8 }, piso);
    var cu = w.pieza(g, cx, cy); w.el('g', { transform: 'rotate(' + (-inc) + ')' }, cu).appendChild(w.emoji(null, 0, 0, d.cuerpo || '📦', 200));
    var F = d.fuerzas.map(function (f, k) { var an = f.ang * Math.PI / 180, L = f.largo || 260, col = f.color || W.PAL[(k + 1) % W.PAL.length];
      var fl = w.flecha(g, cx, cy, cx + L * Math.cos(an), cy - L * Math.sin(an), col, 12); var lb = w.pieza(g, cx + (L + 70) * Math.cos(an), cy - (L + 70) * Math.sin(an)); w.txt(lb, 0, 0, f.txt, 40, col); return [fl, lb]; });
    B(0); w.IN(tl, piso, 0); w.IN(tl, cu, '<', { y: -200, ease: 'bounce.out', d: .7 });
    F.forEach(function (f, k) { B(k + 1); w.dibujarFlecha(tl, f[0], 0); w.IN(tl, f[1], '>', { scale: 0, y: 0 }); });
  } };

  // zoom: {niveles:[{emoji, txt}] (2-5)} — n pasos: cada paso "entra" al siguiente nivel (del cuerpo a la célula al ADN)
  T.zoom = { n: function (d) { return d.niveles.length; }, armar: function (g, tl, B, d) {
    var N = d.niveles.map(function (nv) { var p = w.pieza(g, 960, 600); w.el('circle', { r: 300, fill: 'rgba(127,211,196,.08)', stroke: C.aqua, 'stroke-width': 4, 'stroke-dasharray': '16 12' }, p); w.emoji(p, 0, -20, nv.emoji, 300); var t = w.chip(g, 960, 940, nv.txt.length * 26 + 120, 84, nv.txt, { size: 40, stroke: C.sol }); return [p, t]; });
    N.forEach(function (q, k) { B(k); if (k) { tl.to(N[k - 1][0], { scale: 6, opacity: 0, duration: .6, ease: 'power3.in' }); w.OUT(tl, N[k - 1][1], '<'); }
      w.IN(tl, q[0], k ? '>-.2' : 0, { scale: .15, y: 0, ease: 'power3.out', d: .7 }); w.IN(tl, q[1], '<.2'); });
  } };

  // texto: {oracion:'El perro de mi vecino ladra fuerte.', marcas:[{desde, hasta, etiqueta, color}] (índices de palabras)} — 1 + marcas pasos
  T.texto = { n: function (d) { return 1 + d.marcas.length; }, armar: function (g, tl, B, d) {
    var pal = d.oracion.split(' '), size = pal.length > 9 ? 64 : 80, cw = size * .52, tot = d.oracion.length * cw, x = 960 - tot / 2, Y = 560, X = [];
    var o = w.pieza(g, 0, 0); pal.forEach(function (p) { X.push([x, x + p.length * cw]); w.txt(o, x + p.length * cw / 2, Y, p, size, C.txt); x += (p.length + 1) * cw; });
    var M = d.marcas.map(function (m, k) { var col = m.color || W.PAL[k % W.PAL.length], x0 = X[m.desde][0] - 10, x1 = X[m.hasta][1] + 10, arriba = k % 2 === 1, gp = w.pieza(g, 0, 0);
      w.el('path', { d: arriba ? 'M' + x0 + ' ' + (Y - 60) + ' Q' + (x0 + x1) / 2 + ' ' + (Y - 110) + ' ' + x1 + ' ' + (Y - 60) : 'M' + x0 + ' ' + (Y + 60) + ' L' + x1 + ' ' + (Y + 60), fill: 'none', stroke: col, 'stroke-width': 10, 'stroke-linecap': 'round' }, gp);
      var lw = m.etiqueta.length * 19 + 50; w.caja(gp, (x0 + x1) / 2, arriba ? Y - 160 : Y + 130, lw, 66, 'rgba(6,20,22,.9)', col, 30, 4); w.txt(gp, (x0 + x1) / 2, arriba ? Y - 160 : Y + 130, m.etiqueta, 32, col); return gp; });
    B(0); w.IN(tl, o, 0); M.forEach(function (m, k) { B(k + 1); w.IN(tl, m, 0, { scaleX: 0, y: 0, d: .4, ease: 'power2.out' }); });
  } };

  // silabas: {palabra:'camión', silabas:['ca','mión'], tonica: 1, tipo:'AGUDA'} — 3 pasos
  T.silabas = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var pw = w.pieza(g, 960, 420); w.txt(pw, 0, 0, d.palabra, 150, C.txt);
    var n = d.silabas.length, P = W.rejilla(n, 960, 680, 300, 0, n);
    var S = d.silabas.map(function (s, k) { return w.chip(g, P[k][0], 680, 260, 150, s, { size: 80, r: 34, stroke: C.linea }); });
    var tp = d.tipo ? w.etiqueta(g, 960, 900, d.tipo) : null;
    B(0); w.IN(tl, pw, 0, { scale: .5, y: 0 });
    B(1); tl.to(pw, { opacity: .25, duration: .3 }); S.forEach(function (s, k) { w.IN(tl, s, k ? '<.15' : '<', { y: -200, scale: .5 }); });
    B(2); var t = S[d.tonica]; tl.to(t.r, { attr: { fill: 'url(#gSol)', stroke: '#ffe7a8' }, duration: .3 }); tl.to(t.t, { attr: { fill: '#3a2a00' }, duration: .3 }, '<'); w.pop(tl, t, '>'); if (tp) w.IN(tl, tp, '<.2');
  } };

  // bloques: {titulo, items:[{cab, txt}] (2-5)} — estructura de un texto (titular, copete, cuerpo...) — 1 + n pasos
  T.bloques = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo, 260), n = d.items.length, alto = [130, 110, 240, 120, 110], y = 370, P = [];
    var hoja = w.pieza(g, 860, 660); w.caja(hoja, 0, 0, 900, 620, '#eef6f4', '#d8fff7', 20, 4).setAttribute('filter', 'url(#sombra)');
    d.items.forEach(function (it, k) { var h = alto[k] || 120, col = W.PAL[k % W.PAL.length], p = w.pieza(g, 0, 0);
      w.caja(p, 860, y + h / 2, 840, h - 16, col, col, 12, 2).setAttribute('opacity', .85); w.multi(p, 860, y + h / 2, it.txt, k ? 28 : 40, '#06282a', 780);
      w.caja(p, 1560, y + h / 2, 300, 62, 'rgba(6,20,22,.9)', col, 30, 4); w.txt(p, 1560, y + h / 2, it.cab, 30, col, { 'letter-spacing': 2 }); P.push(p); y += h; });
    B(0); w.IN(tl, ti, 0); w.IN(tl, hoja, '<');
    P.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { x: 100, y: 0 }); });
  } };

  // dialogo: {personas:[{nombre, emoji}] (2), lineas:[{quien: 0|1, txt, trad}]} — n pasos (máx 4 líneas)
  T.dialogo = { n: function (d) { return d.lineas.length; }, armar: function (g, tl, B, d) {
    var per = d.personas.map(function (p, k) { var q = w.pieza(g, k ? 1640 : 280, 820); w.emoji(q, 0, -20, p.emoji, 150); w.txt(q, 0, 90, p.nombre, 34, k ? C.sol : C.aqua); return q; });
    var n = d.lineas.length, L = d.lineas.map(function (l, k) { var der = l.quien === 1, y = 330 + k * (560 / Math.max(1, n - 1 || 1)) * (n > 1 ? 1 : 0), col = der ? C.sol : C.aqua, ww = Math.min(1000, Math.max(420, l.txt.length * 26 + 100));
      var p = w.pieza(g, der ? 1480 - ww / 2 : 440 + ww / 2, Math.min(y, 820)); w.caja(p, 0, 0, ww, l.trad ? 150 : 110, 'url(#gCard)', col, 40, 5).setAttribute('filter', 'url(#sombra)');
      w.txt(p, 0, l.trad ? -22 : 0, l.txt, 42, C.txt); if (l.trad) w.txt(p, 0, 38, l.trad, 30, C.suave); return p; });
    L.forEach(function (p, k) { B(k); if (!k) per.forEach(function (q, j) { w.IN(tl, q, j ? '<.1' : 0, { y: 100 }); }); w.IN(tl, p, k ? 0 : '<.1', { scale: .6, y: 30, ease: 'back.out(2)' }); });
  } };

  // vocab: {items:[{palabra, emoji, trad, pron}] (2-6)} — n pasos (cada tarjeta se da vuelta)
  T.vocab = { n: function (d) { return d.items.length; }, armar: function (g, tl, B, d) {
    var n = d.items.length, P = W.rejilla(n, 960, 620, 520, 340, 3);
    var V = d.items.map(function (it, k) { var p = w.pieza(g, P[k][0], P[k][1]); w.tarjeta(p, 0, 0, 470, 310, W.PAL[k % W.PAL.length]);
      w.emoji(p, 0, -70, it.emoji || '', 100); w.txt(p, 0, 40, it.palabra, 52, C.txt); if (it.pron) w.txt(p, 0, 88, '/' + it.pron + '/', 28, C.suave); w.txt(p, 0, it.pron ? 126 : 100, it.trad || '', 32, C.sol); return p; });
    V.forEach(function (p, k) { B(k); w.IN(tl, p, 0, { scaleX: 0, y: 0, d: .5, ease: 'back.out(1.6)' }); });
  } };
})();
