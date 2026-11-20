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

  // libro: {titulo, libro:{titulo, autor, editorial, emoji}, partes:[{parte:'contratapa'|'lomo'|'tapa'|'indice', txt}]} — dibuja el libro y marca cada parte (1 + partes pasos)
  T.libro = { n: function (d) { return 1 + d.partes.length; }, armar: function (g, tl, B, d) {
    var L = d.libro || {}, ti = d.titulo ? w.titulo(g, d.titulo, 250) : null, o = w.pieza(g, 0, 0), y0 = 310, h = 450;
    var Z = { contratapa: [300, 400], lomo: [712, 76], tapa: [800, 400], indice: [1250, 370] };
    w.el('rect', { x: 300, y: y0, width: 400, height: h, rx: 14, fill: '#5b3f8c' }, o);
    for (var i = 0; i < 9; i++) w.el('rect', { x: 340, y: y0 + 70 + i * 34, width: i === 8 ? 180 : 320, height: 12, rx: 6, fill: '#d6c4ff', opacity: .7 }, o);
    for (var j = 0; j < 14; j++) w.el('rect', { x: 560 + j * 8, y: y0 + h - 90, width: j % 3 ? 4 : 2, height: 56, fill: '#fff' }, o);
    w.el('rect', { x: 712, y: y0, width: 76, height: h, rx: 6, fill: '#3f2a66' }, o);
    var lt = w.txt(o, 750, y0 + h / 2, (L.titulo || 'MI LIBRO').toUpperCase(), 26, '#f1eaff'); lt.setAttribute('transform', 'rotate(-90 750 ' + (y0 + h / 2) + ')');
    w.el('rect', { x: 800, y: y0, width: 400, height: h, rx: 14, fill: '#7458c4' }, o);
    w.txt(o, 1000, y0 + 80, L.titulo || 'Mi libro', 40, '#fff'); w.emoji(o, 1000, y0 + 215, L.emoji || '📖', 150);
    w.txt(o, 1000, y0 + 355, L.autor || 'Autor', 32, '#f1eaff'); w.txt(o, 1000, y0 + 405, L.editorial || 'Editorial', 26, '#d6c4ff');
    w.el('rect', { x: 1250, y: y0, width: 370, height: h, rx: 10, fill: '#fbf8ff', stroke: '#bdb2d6', 'stroke-width': 3 }, o);
    w.txt(o, 1435, y0 + 60, 'ÍNDICE', 34, '#3a2a63');
    for (var k = 0; k < 6; k++) { w.txt(o, 1300, y0 + 120 + k * 52, (k + 1) + '. ……………', 26, '#4b3c74').setAttribute('text-anchor', 'start'); w.txt(o, 1585, y0 + 120 + k * 52, String(5 + k * 12), 26, '#4b3c74'); }
    var P = d.partes.map(function (pt, k) { var z = Z[pt.parte] || Z.tapa, col = W.PAL[k % W.PAL.length], gr = w.pieza(g, 0, 0), cx = z[0] + z[1] / 2;
      w.el('rect', { x: z[0] - 8, y: y0 - 8, width: z[1] + 16, height: h + 16, rx: 18, fill: 'none', stroke: col, 'stroke-width': 8 }, gr);
      var tw = Math.max(220, pt.txt.length * 19 + 50), lx = Math.max(tw / 2 + 20, Math.min(1900 - tw / 2, cx));
      var ly = y0 + h + 70 + (k % 2) * 88; w.el('line', { x1: cx, y1: y0 + h + 8, x2: lx, y2: ly - 36, stroke: col, 'stroke-width': 4 }, gr);
      w.caja(gr, lx, ly, tw, 72, 'rgba(14,10,26,.92)', col, 30, 4); w.txt(gr, lx, ly, pt.txt, 30, '#fff'); return gr; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, o, ti ? '<.1' : 0, { scale: .9, y: 0 });
    P.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { scale: .95, y: 0, d: .4 }); });
  } };

  // parrafo: {titulo, lineas:[...], marcas:[{linea, pos:'inicio'|'fin', txt}]} — un párrafo real con sus marcas (1 + marcas pasos)
  T.parrafo = { n: function (d) { return 1 + d.marcas.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 250) : null, o = w.pieza(g, 0, 0), x0 = 380, y0 = 360;
    w.el('rect', { x: 340, y: 320, width: 1240, height: 90 + d.lineas.length * 72, rx: 16, fill: '#fbf8ff', stroke: '#bdb2d6', 'stroke-width': 3 }, o);
    var X = d.lineas.map(function (t, i) { var x = x0 + (d.sangria !== false && i === 0 ? 70 : 0), tx = w.txt(o, x, y0 + 40 + i * 72, t, 38, '#241a40'); tx.setAttribute('text-anchor', 'start'); var lw = 0; try { lw = tx.getComputedTextLength(); } catch (e) {} return [x, x + (lw > 0 ? lw : t.length * 17.5)]; });
    var P = d.marcas.map(function (m, k) { var col = W.PAL[k % W.PAL.length], gr = w.pieza(g, 0, 0), i = m.linea, mx = m.pos === 'fin' ? X[i][1] - 14 : X[i][0] + 12, my = y0 + 30 + i * 72;
      if (m.tras) { var tt = w.txt(o, X[i][0], -500, m.tras, 38, '#000'); tt.setAttribute('text-anchor', 'start'); var tw0 = 0; try { tw0 = tt.getComputedTextLength(); } catch (e) {} tt.remove(); mx = X[i][0] + (tw0 > 0 ? tw0 : m.tras.length * 17.5) - 14; }
      if (m.pos === 'sangria') { mx = x0 + 35; w.el('line', { x1: x0, y1: my, x2: x0 + 60, y2: my, stroke: col, 'stroke-width': 6, 'marker-end': '' }, gr); }
      else w.el('circle', { cx: mx, cy: my + 6, r: (m.pos === 'fin' || m.tras) ? 18 : 30, fill: 'none', stroke: col, 'stroke-width': 6 }, gr);
      var ly = 320 + 90 + d.lineas.length * 72 + 45 + k * 74, tw = Math.max(220, m.txt.length * 19 + 50), lx = Math.max(tw / 2 + 20, Math.min(1900 - tw / 2, mx));
      w.el('line', { x1: mx, y1: my + 32, x2: lx, y2: ly - 36, stroke: col, 'stroke-width': 4 }, gr); w.caja(gr, lx, ly, tw, 72, 'rgba(14,10,26,.92)', col, 30, 4); w.txt(gr, lx, ly, m.txt, 30, '#fff'); return gr; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, o, ti ? '<.1' : 0, { scale: .95, y: 0 });
    P.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { scale: .95, y: 0, d: .4 }); });
  } };

  // ficha: {titulo, campos:[[cab, valor]]} — una ficha de cartulina que se completa de a un dato (1 + campos pasos)
  T.ficha = { n: function (d) { return 1 + d.campos.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 250) : null, o = w.pieza(g, 0, 0), y0 = 340, hh = 110 + d.campos.length * 100;
    w.el('rect', { x: 520, y: y0, width: 880, height: hh, rx: 18, fill: '#fffbea', stroke: '#e6d38a', 'stroke-width': 4, filter: 'url(#sombra)' }, o);
    w.el('rect', { x: 520, y: y0, width: 880, height: 70, rx: 18, fill: '#f4b63f' }, o); w.txt(o, 960, y0 + 36, 'FICHA BIBLIOGRÁFICA', 32, '#3a2a10');
    var P = d.campos.map(function (c, k) { var y = y0 + 130 + k * 100, gr = w.pieza(g, 0, 0); w.el('line', { x1: 570, y1: y + 30, x2: 1350, y2: y + 30, stroke: '#e6d38a', 'stroke-width': 3 }, o);
      var a = w.txt(gr, 580, y, c[0] + ':', 34, '#7458c4'); a.setAttribute('text-anchor', 'start'); var b = w.txt(gr, 820, y, c[1], 38, '#241a40'); b.setAttribute('text-anchor', 'start'); return gr; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, o, ti ? '<.1' : 0, { scale: .95, y: 0 });
    P.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { x: -20, y: 0, d: .4 }); });
  } };

  // orden: {titulo, items:[{txt, emoji}] (en orden cronológico, 3-5), relato:[índices en el orden en que se cuenta]} — 3 pasos: se cuenta así → pasó así
  T.orden = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var n = d.items.length, wC = Math.min(320, 1700 / n - 30), paso = wC + 30, x0 = 960 - (n - 1) * paso / 2, ti = d.titulo ? w.titulo(g, d.titulo, 250) : null;
    var et = w.etiqueta ? w.etiqueta(g, 960, 400, d.etq1 || 'ASÍ SE CUENTA') : null, et2 = w.etiqueta ? w.etiqueta(g, 960, 400, d.etq2 || 'ASÍ PASÓ') : null;
    var rel = d.relato || d.items.map(function (_, i) { return i; });
    var cards = d.items.map(function (it, i) { var col = W.PAL[i % W.PAL.length], gr = w.pieza(g, x0 + rel.indexOf(i) * paso, 620); gr._dx = (i - rel.indexOf(i)) * paso;
      w.caja(gr, 0, 0, wC, 230, 'rgba(14,10,26,.85)', col, 26, 5); if (it.emoji) w.emoji(gr, 0, -45, it.emoji, 80); w.txt(gr, 0, 55, it.txt, 30, '#fff');
      var nb = w.el('g', { opacity: 0 }, gr); w.el('circle', { cx: -wC / 2 + 12, cy: -103, r: 30, fill: col }, nb); w.txt(nb, -wC / 2 + 12, -101, String(i + 1), 32, '#14101f'); gr._nb = nb; return gr; });
    B(0); if (ti) w.IN(tl, ti, 0);
    B(1); if (et) w.IN(tl, et, 0); cards.forEach(function (c, k) { w.IN(tl, c, k ? '<.12' : 0, { scale: .8, y: 0 }); });
    B(2); if (et) w.OUT(tl, et, 0); if (et2) w.IN(tl, et2, '<');
    cards.forEach(function (c) { tl.to(c, { x: c._dx, duration: 1, ease: 'power2.inOut' }, '<'); });
    cards.forEach(function (c) { tl.to(c._nb, { opacity: 1, duration: .3 }, '>-.1'); });
  } };

  // corrige: {titulo, cambios:[{antes, despues, motivo}] (máx 3)} — tacha lo que está mal y escribe lo correcto (1 + cambios pasos)
  T.corrige = { n: function (d) { return 1 + d.cambios.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 250) : null;
    var F = d.cambios.map(function (c, k) { var y = 400 + k * 200, gr = w.pieza(g, 0, 0);
      var a = w.txt(gr, 560, y, c.antes, 40, '#ff9f9f'); var la = c.antes.length * 21 + 20;
      var tachon = w.el('line', { x1: 560 - la / 2, y1: y, x2: 560 + la / 2, y2: y, stroke: '#ff5a4f', 'stroke-width': 6, 'stroke-dasharray': la, 'stroke-dashoffset': la }, gr);
      w.txt(gr, 960, y, '→', 50, '#C3A8FF'); var bb = w.txt(gr, 1360, y, c.despues, 40, '#8be38f');
      var mo = c.motivo ? w.txt(gr, 960, y + 62, c.motivo, 28, '#bdb2d6') : null; gr._t = tachon; gr._b = bb; gr._m = mo; return gr; });
    B(0); if (ti) w.IN(tl, ti, 0);
    F.forEach(function (f, k) { B(k + 1); tl.set([f._b, f._m].filter(Boolean), { opacity: 0 }, 0); w.IN(tl, f, 0, { y: 0, d: .3 });
      tl.to(f._t, { attr: { 'stroke-dashoffset': 0 }, duration: .5 }, '>'); tl.to([f._b, f._m].filter(Boolean), { opacity: 1, duration: .4 }, '>'); });
  } };

  // experimento: {titulo, variable, a:{cab, emojis:[...], txt, res}, b:{...}} — control vs cambio (3 pasos: montajes, variable, resultados)
  T.experimento = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 250) : null;
    function lado(o, x, col) { var gr = w.pieza(g, x, 560); w.caja(gr, 0, 0, 640, 380, 'rgba(10,25,12,.55)', col, 30, 4); w.chip(gr, 0, -160, Math.max(240, o.cab.length * 22 + 70), 62, o.cab, { size: 30, stroke: col });
      (o.emojis || []).forEach(function (e, k, arr) { w.emoji(gr, (k - (arr.length - 1) / 2) * 150, -10, e, 120); });
      if (o.txt) w.txt(gr, 0, 120, o.txt, 30, '#efffdc'); var r = o.res ? w.pieza(g, x, 820) : null; if (r) { w.caja(r, 0, 0, Math.max(300, o.res.length * 20 + 60), 70, 'rgba(14,30,10,.92)', col, 30, 4); w.txt(r, 0, 0, o.res, 32, '#fff'); } return [gr, r]; }
    var A = lado(d.a, 560, C.aqua), Bb = lado(d.b, 1360, C.sol);
    var v = d.variable ? w.etiqueta(g, 960, 905, d.variable) : null;
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, A[0], ti ? '<.1' : 0, { y: 0 }); w.IN(tl, Bb[0], '<.15', { y: 0 });
    B(1); if (v) w.IN(tl, v, 0, { scale: .6, y: 0 });
    B(2); [A[1], Bb[1]].forEach(function (r, k) { if (r) w.IN(tl, r, k ? '<.2' : 0, { y: 20 }); });
  } };

  // medidor: {titulo, tipo:'termometro'|'regla'|'probeta', min, max, valor, unidad, nota} — instrumento dibujado con su lectura (3 pasos: instrumento, lectura, nota)
  T.medidor = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 250) : null, o = w.pieza(g, 0, 0), mk = w.pieza(g, 0, 0), lo = d.min || 0, hi = d.max || 100, f = (d.valor - lo) / (hi - lo), tipo = d.tipo || 'termometro', px, py;
    if (tipo === 'regla') { var x0 = 360, x1 = 1560, y = 600; w.el('rect', { x: x0 - 20, y: y - 70, width: x1 - x0 + 40, height: 110, rx: 10, fill: '#f4e3b5', stroke: '#8a6a2a', 'stroke-width': 3 }, o);
      var n = Math.round((hi - lo) * 10); for (var i = 0; i <= n; i++) { var x = x0 + (x1 - x0) * i / n, h = i % 10 === 0 ? 50 : (i % 5 === 0 ? 34 : 20); w.el('line', { x1: x, y1: y - 70, x2: x, y2: y - 70 + h, stroke: '#3a2a10', 'stroke-width': 2 }, o); if (i % 10 === 0) w.txt(o, x, y + 10, String(lo + i / 10), 26, '#3a2a10'); }
      px = x0 + (x1 - x0) * f; py = y - 70; w.el('rect', { x: x0 - 20, y: y - 140, width: px - x0 + 20, height: 46, rx: 8, fill: '#f2b33d', stroke: '#3a2a10', 'stroke-width': 3 }, mk); }
    else if (tipo === 'probeta') { var cx = 960, top = 330, bot = 860, wd = 160; w.el('rect', { x: cx - wd / 2, y: top, width: wd, height: bot - top, rx: 14, fill: 'rgba(255,255,255,.12)', stroke: '#d8f0ea', 'stroke-width': 5 }, o);
      for (var j = 0; j <= 10; j++) { var yy = bot - (bot - top) * j / 10; w.el('line', { x1: cx + wd / 2 - 40, y1: yy, x2: cx + wd / 2, y2: yy, stroke: '#d8f0ea', 'stroke-width': 3 }, o); w.txt(o, cx + wd / 2 + 50, yy, String(Math.round(lo + (hi - lo) * j / 10)), 26, '#d8f0ea'); }
      py = bot - (bot - top) * f; px = cx; w.el('rect', { x: cx - wd / 2 + 6, y: py, width: wd - 12, height: bot - py - 6, rx: 8, fill: '#4fb3dc', opacity: .85 }, mk); }
    else { var cx2 = 960, top2 = 300, bot2 = 820; w.el('rect', { x: cx2 - 34, y: top2, width: 68, height: bot2 - top2, rx: 34, fill: 'rgba(255,255,255,.15)', stroke: '#fff', 'stroke-width': 5 }, o); w.el('circle', { cx: cx2, cy: bot2 + 40, r: 62, fill: '#e2453c', stroke: '#fff', 'stroke-width': 5 }, o);
      for (var k = 0; k <= 10; k++) { var y3 = bot2 - (bot2 - top2 - 30) * k / 10; w.el('line', { x1: cx2 + 40, y1: y3, x2: cx2 + 70, y2: y3, stroke: '#fff', 'stroke-width': 3 }, o); w.txt(o, cx2 + 120, y3, String(Math.round(lo + (hi - lo) * k / 10)), 26, '#fff'); }
      py = bot2 - (bot2 - top2 - 30) * f; px = cx2; w.el('rect', { x: cx2 - 18, y: py, width: 36, height: bot2 - py + 20, fill: '#e2453c' }, mk); }
    var lec = w.pieza(g, 0, 0), lx = tipo === 'regla' ? px : px - 330, ly = tipo === 'regla' ? py - 170 : py;
    w.caja(lec, lx, ly, 280, 76, 'rgba(14,30,10,.92)', C.sol, 30, 4); w.txt(lec, lx, ly, String(d.valor).replace('.', ',') + ' ' + (d.unidad || ''), 38, '#fff');
    var nt = d.nota ? w.etiqueta(g, 960, 905, d.nota) : null;
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, o, ti ? '<.1' : 0, { y: 0 });
    B(1); w.IN(tl, mk, 0, { y: 0, d: .8 }); w.IN(tl, lec, '>-.2', { y: 0 });
    B(2); if (nt) w.IN(tl, nt, 0, { y: 0 });
  } };

  // celula: {titulo, tipo:'animal'|'vegetal', partes:[{p:'membrana'|'citoplasma'|'nucleo'|'mitocondria'|'pared'|'cloroplasto'|'vacuola', txt}]} — célula dibujada y sus partes (1 + partes pasos)
  T.celula = { n: function (d) { return 1 + d.partes.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 250) : null, o = w.pieza(g, 0, 0), veg = d.tipo === 'vegetal', A;
    if (veg) { w.el('rect', { x: 640, y: 350, width: 640, height: 480, rx: 34, fill: '#d9f2cf', stroke: '#3f7a3a', 'stroke-width': 16 }, o);
      w.el('rect', { x: 660, y: 370, width: 600, height: 440, rx: 26, fill: 'none', stroke: '#86c96f', 'stroke-width': 5 }, o);
      w.el('ellipse', { cx: 1030, cy: 590, rx: 165, ry: 140, fill: '#bfe6ff', stroke: '#5aa9d6', 'stroke-width': 4 }, o);
      [[740, 740], [1190, 430], [1200, 760], [860, 430]].forEach(function (c) { w.el('ellipse', { cx: c[0], cy: c[1], rx: 42, ry: 22, fill: '#2e8b3a', stroke: '#1d5e26', 'stroke-width': 3 }, o); });
      w.el('circle', { cx: 770, cy: 560, r: 70, fill: '#9c7bd6', stroke: '#5b3f8c', 'stroke-width': 5 }, o); w.el('circle', { cx: 780, cy: 555, r: 22, fill: '#5b3f8c' }, o);
      w.el('ellipse', { cx: 900, cy: 760, rx: 42, ry: 20, fill: '#f4a259' }, o);
      A = { pared: [640, 460], membrana: [660, 690], citoplasma: [930, 470], nucleo: [770, 560], cloroplasto: [1190, 430], vacuola: [1100, 620], mitocondria: [900, 760] }; }
    else { w.el('ellipse', { cx: 960, cy: 590, rx: 330, ry: 245, fill: '#f8d7dd', stroke: '#c2566b', 'stroke-width': 9 }, o);
      w.el('circle', { cx: 900, cy: 570, r: 90, fill: '#9c7bd6', stroke: '#5b3f8c', 'stroke-width': 5 }, o); w.el('circle', { cx: 915, cy: 560, r: 28, fill: '#5b3f8c' }, o);
      [[1110, 500], [1090, 700], [790, 720], [1160, 610]].forEach(function (c) { w.el('ellipse', { cx: c[0], cy: c[1], rx: 48, ry: 22, fill: '#f4a259', stroke: '#b86a1c', 'stroke-width': 3 }, o); });
      A = { membrana: [1286, 620], citoplasma: [1010, 420], nucleo: [900, 570], mitocondria: [1110, 500] }; }
    var izq = [], der = [], P = d.partes.map(function (pt, k) { var a = A[pt.p] || [960, 590], lado = a[0] < 960 ? izq : der; lado.push({ k: k, a: a, txt: pt.txt }); return null; });
    [izq, der].forEach(function (L, s) { L.sort(function (u, v) { return u.a[1] - v.a[1]; }); var y = 330; L.forEach(function (it) { it.y = Math.max(y, Math.min(870, it.a[1])); y = it.y + 92; }); L.forEach(function (it) {
      var col = W.PAL[it.k % W.PAL.length], gr = w.pieza(g, 0, 0), tw = Math.max(200, it.txt.length * 15 + 40), lx = s ? Math.min(1905 - tw / 2, 1325 + tw / 2) : Math.max(15 + tw / 2, 595 - tw / 2), ex = s ? lx - tw / 2 : lx + tw / 2;
      w.el('circle', { cx: it.a[0], cy: it.a[1], r: 10, fill: col, stroke: '#fff', 'stroke-width': 3 }, gr); w.el('polyline', { points: it.a[0] + ',' + it.a[1] + ' ' + ex + ',' + it.y, fill: 'none', stroke: col, 'stroke-width': 4 }, gr);
      w.caja(gr, lx, it.y, tw, 64, 'rgba(8,20,8,.92)', col, 28, 4); w.txt(gr, lx, it.y, it.txt, 24, '#fff'); P[it.k] = gr; }); });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, o, ti ? '<.1' : 0, { scale: .9, y: 0 });
    P.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { y: 0, d: .4 }); });
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
    var N = d.niveles.map(function (nv) { var p = w.pieza(g, 960, 540); w.el('circle', { r: 280, fill: 'rgba(127,211,196,.08)', stroke: C.aqua, 'stroke-width': 4, 'stroke-dasharray': '16 12' }, p); w.emoji(p, 0, -20, nv.emoji, 280); var t = w.chip(g, 960, 880, nv.txt.length * 26 + 120, 84, nv.txt, { size: 40, stroke: C.sol }); return [p, t]; });
    N.forEach(function (q, k) { B(k); if (k) { tl.to(N[k - 1][0], { scale: 6, opacity: 0, duration: .6, ease: 'power3.in' }); w.OUT(tl, N[k - 1][1], '<'); }
      w.IN(tl, q[0], k ? '>-.2' : 0, { scale: .15, y: 0, ease: 'power3.out', d: .7 }); w.IN(tl, q[1], '<.2'); });
  } };

  // texto: {oracion:'El perro de mi vecino ladra fuerte.', marcas:[{desde, hasta, etiqueta, color}] (índices de palabras)} — 1 + marcas pasos
  T.texto = { n: function (d) { return 1 + d.marcas.length; }, armar: function (g, tl, B, d) {
    var pal = d.oracion.split(' '), size = Math.min(80, Math.floor(1720 / (d.oracion.length * .52))), cw = size * .52, tot = d.oracion.length * cw, x = 960 - tot / 2, Y = 560, X = [];
    var o = w.pieza(g, 0, 0), T0 = pal.map(function (p) { var t = w.txt(o, 0, Y, p, size, C.txt); t.setAttribute('text-anchor', 'start'); var lw = 0; try { lw = t.getComputedTextLength(); } catch (e) {} return [t, lw > 0 ? lw : p.length * cw]; });
    var esp = size * .32, total = T0.reduce(function (a, r) { return a + r[1]; }, 0) + esp * (T0.length - 1); x = 960 - total / 2;
    T0.forEach(function (r) { r[0].setAttribute('x', x); X.push([x, x + r[1]]); x += r[1] + esp; });
    var FA = [], FB = [];
    var M = d.marcas.map(function (m, k) { var col = m.color || W.PAL[k % W.PAL.length], x0 = X[m.desde][0] - 10, x1 = X[m.hasta][1] + 10, arriba = k % 2 === 1, gp = w.pieza(g, 0, 0);
      w.el('path', { d: arriba ? 'M' + x0 + ' ' + (Y - 60) + ' Q' + (x0 + x1) / 2 + ' ' + (Y - 110) + ' ' + x1 + ' ' + (Y - 60) : 'M' + x0 + ' ' + (Y + 60) + ' L' + x1 + ' ' + (Y + 60), fill: 'none', stroke: col, 'stroke-width': 10, 'stroke-linecap': 'round' }, gp);
      var lw = m.etiqueta.length * 19 + 50, cx = Math.max(lw / 2 + 20, Math.min(1900 - lw / 2, (x0 + x1) / 2)), lado = arriba ? FA : FB, fila = 0;
      while (lado.some(function (r) { return r[2] === fila && cx - lw / 2 < r[1] + 12 && cx + lw / 2 > r[0] - 12; })) fila++;
      lado.push([cx - lw / 2, cx + lw / 2, fila]); var ly = arriba ? Y - 160 - fila * 78 : Y + 130 + fila * 78;
      w.caja(gp, cx, ly, lw, 66, 'rgba(6,20,22,.9)', col, 30, 4); w.txt(gp, cx, ly, m.etiqueta, 32, col); return gp; });
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
