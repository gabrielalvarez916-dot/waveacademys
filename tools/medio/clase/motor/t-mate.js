/* PLANTILLAS · MATEMÁTICA */
(function () {
  var w = W, C = w.C;

  // agrupar: {niveles:[{nombre, valor, icono:'alf'|'pack'|'caja'|'camion'|emoji}] (2-4), salto:'×10'} — n + 1 pasos
  T.agrupar = { n: function (d) { return d.niveles.length + 1; }, armar: function (g, tl, B, d) {
    var N = d.niveles, n = N.length, X = W.rejilla(n, 960, 0, 400, 0, n).map(function (p) { return p[0]; }), Y = 560, ESC = { alf: 1.9, pack: 2, caja: 1.8, camion: 1.1 }, MINI = { alf: .55, pack: .85, caja: .36, camion: .3 };
    function icono(p, ic, s) { if (ESC[ic]) w.usar(p, ic, s); else w.emoji(p, 0, 0, ic, 150 * s / 1.9); }
    var lab = X.map(function (x, k) { var p = w.pieza(g, x, 820); w.caja(p, 0, 0, 340, 120, 'url(#gCard)', C.linea, 24, 4); w.txt(p, 0, -22, N[k].nombre, 28, C.aqua, { 'letter-spacing': 3 }); w.txt(p, 0, 28, N[k].valor, 48, C.txt); return p; });
    var grandes = X.map(function (x, k) { var p = w.pieza(g, x, Y); icono(p, N[k].icono, ESC[N[k].icono] || 1.9); return p; });
    var minis = X.map(function (x, k) { if (!k) return []; var ic = N[k - 1].icono, m = []; for (var j = 0; j < 10; j++) { var cols = ic === 'pack' ? 2 : 5, dx = ic === 'pack' ? 132 : ic === 'alf' ? 56 : 62, dy = ic === 'pack' ? 64 : 60;
      var q = w.pieza(g, x + (j % cols - (cols - 1) / 2) * dx, Y - (ic === 'pack' ? 128 : 30) + Math.floor(j / cols) * dy); icono(q, ic, MINI[ic] || .5); m.push(q); } return m; });
    var fl = X.slice(0, -1).map(function (x, k) { var f = w.pieza(g, (x + X[k + 1]) / 2, Y); w.el('circle', { r: 46, fill: C.sol }, f); w.txt(f, 0, 2, d.salto || '×10', 30, '#3a2a00'); return f; });
    X.forEach(function (x, k) { B(k);
      if (!k) { w.IN(tl, grandes[0], 0, { scale: 0, y: 0, ease: 'back.out(2.2)' }); w.IN(tl, lab[0], '<.3'); return; }
      minis[k].forEach(function (m, j) { w.IN(tl, m, j ? '<.06' : 0, { x: -400, y: -100, scale: .3, ease: 'power3.out', d: .5 }); });
      w.IN(tl, grandes[k], '>.1', N[k].icono === 'camion' ? { x: 500, y: 0, ease: 'power3.out', d: .8 } : N[k].icono === 'caja' ? { y: -500, ease: 'bounce.out', d: .8 } : { scaleY: 0, y: 0 });
      tl.to(minis[k], { opacity: 0, duration: .2 }, '<.3'); w.IN(tl, lab[k], '<.2'); });
    B(n); fl.forEach(function (f, k) { w.IN(tl, f, k ? '<.25' : 0, { scale: 0, y: 0, ease: 'back.out(3)' }); });
  } };

  // estante: {numero, cab:[...], dig:[...], val:[...], flechas:'×10' (opcional), destacar: índice, etiqueta} — 5 pasos
  T.estante = { n: function () { return 5; }, armar: function (g, tl, B, d) {
    var n = w.pieza(g, 960, 300); w.txt(n, 0, 0, d.numero, 130, C.txt);
    var ancho = d.cab.length > 4 ? 170 : 190, F = w.fila(g, 960, 580, d.cab, d.dig, ancho);
    var fl = d.flechas ? F.xs.slice(0, -1).map(function (x, k) { var f = w.pieza(g, (x + F.xs[k + 1]) / 2, 700); w.el('circle', { r: 30, fill: C.sol }, f); w.txt(f, 0, 2, d.flechas, 22, '#3a2a00'); return f; }) : [];
    d.val.forEach(function (v, k) { F.vals[k].t.textContent = v; });
    var et = d.etiqueta ? w.etiqueta(g, 960, 930, d.etiqueta) : null;
    B(0); w.IN(tl, n, 0, { scale: .5, y: 0 });
    B(1); F.slots.forEach(function (s, k) { w.IN(tl, s, k ? '<.08' : 0); w.IN(tl, F.cabs[k], '<'); }); F.digs.forEach(function (dd, k) { w.IN(tl, dd, k ? '<.22' : '>-.1', { y: -500, ease: 'bounce.out', d: .7 }); });
    B(2); fl.slice().reverse().forEach(function (f, j) { w.IN(tl, f, j ? '<.3' : 0, { scale: 0, y: 0, ease: 'back.out(3)' }); });
    B(3); if (fl.length) w.OUT(tl, fl, 0); F.vals.forEach(function (v, k) { w.IN(tl, v, k ? '<.7' : (fl.length ? '<.2' : 0), { y: -60 }); tl.to(F.slots[k].r, { attr: { stroke: C.sol }, duration: .2, yoyo: true, repeat: 1 }, '<'); });
    B(4); if (d.destacar != null) { w.brillar(tl, F.slots[d.destacar].r, C.sol, 0); w.pop(tl, F.digs[d.destacar], '<'); } if (et) w.IN(tl, et, d.destacar != null ? '<.2' : 0);
  } };

  // quitar: {tarjetas:[{cab, val}, {cab, val}], cab, dig, quitar: índice, resultado, sello, etiqueta} — 5 pasos
  T.quitar = { n: function () { return 5; }, armar: function (g, tl, B, d) {
    function tarj(x, t, col) { var p = w.pieza(g, x, 580); w.tarjeta(p, 0, 0, 560, 440, col); w.txt(p, 0, -150, t.cab, 40, col, { 'letter-spacing': 6 }); w.txt(p, 0, 30, t.val, t.val.length > 4 ? 120 : 190, C.txt); return p; }
    var c1 = tarj(620, d.tarjetas[0], C.aqua), c2 = tarj(1300, d.tarjetas[1], C.sol), q = d.quitar;
    var F = w.fila(g, 960, 560, d.cab, d.dig), resto = F.slots.concat(F.cabs, F.digs.filter(function (_, k) { return k !== q; }));
    var r = w.pieza(g, 960, 580); w.txt(r, 0, 0, d.resultado, 260, C.coral, { filter: 'url(#brillo)' });
    var se = w.pieza(g, 960, 850); w.caja(se, 0, 0, Math.max(520, d.sello.length * 40), 120, 'none', C.coral, 20, 10); w.txt(se, 0, 4, d.sello, 64, C.coral, { 'letter-spacing': 4 });
    var lv = w.etiqueta(g, F.xs[q], 880, d.etiqueta);
    B(0); w.IN(tl, c1, 0, { x: -200, y: 0 });
    B(1); w.IN(tl, c2, 0, { x: 200, y: 0 });
    B(2); w.OUT(tl, [c1, c2], 0); F.slots.forEach(function (s, k) { w.IN(tl, s, '<.05'); w.IN(tl, F.cabs[k], '<'); w.IN(tl, F.digs[k], '<'); }); tl.to(F.slots[q].r, { attr: { stroke: C.coral, 'stroke-width': 10 }, duration: .3 }); w.temblar(tl, F.digs[q], '>');
    B(3); tl.to(F.digs[q], { y: -700, rotation: 360, opacity: 0, duration: .6, ease: 'power3.in' }); w.OUT(tl, resto, '>', { duration: .2 });
    w.IN(tl, r, '>', { scale: 2, y: 0, ease: 'power4.in', d: .3 }); w.sacudir(tl, '>'); w.IN(tl, se, '<.3', { scale: 2.5, rotation: -10, y: 0, ease: 'power4.in', d: .3 }); tl.set(se, { rotation: -4 });
    B(4); w.OUT(tl, [r, se], 0); resto.forEach(function (x) { tl.to(x, { opacity: 1, scale: 1, duration: .3 }, '<'); });
    tl.to(F.digs[q], { y: 0, rotation: 0, opacity: 1, duration: .7, ease: 'bounce.out' }); tl.to(F.slots[q].r, { attr: { stroke: C.verde }, duration: .3 }, '<.4'); w.IN(tl, lv, '<');
  } };

  // descomponer: {numero:'4.205', titulo, partes:['4.000','200','0','5'], signo:'+', tachar: índice (opcional), resultado:'= 4.205 ✓'} — 5 pasos
  T.descomponer = { n: function () { return 5; }, armar: function (g, tl, B, d) {
    var ch = String(d.numero).split(''), nd = w.pieza(g, 960, 470), paso = 70, x0 = -(ch.length - 1) * paso / 2;
    var D = ch.map(function (c, k) { return w.txt(nd, x0 + k * paso, 0, c, 170, C.txt); });
    var ti = w.titulo(g, d.titulo), P = d.partes, n = P.length, sg = d.signo || '+';
    var W2 = P.map(function (p) { return Math.max(150, p.length * 38 + 60); }), gap = 70, tot = W2.reduce(function (a, b) { return a + b; }, 0) + gap * (n - 1), xs = [], acc = 960 - tot / 2;
    W2.forEach(function (ww) { xs.push(acc + ww / 2); acc += ww + gap; });
    var chs = P.map(function (p, k) { return w.chip(g, xs[k], 760, W2[k], 120, p, { size: 60, stroke: C.sol, r: 28 }); });
    var mas = xs.slice(0, -1).map(function (x, k) { var m = w.pieza(g, x + W2[k] / 2 + gap / 2, 760); w.txt(m, 0, 0, sg, 76, C.sol); return m; });
    var ok = w.pieza(g, 960, 470); w.txt(ok, 0, 0, d.resultado, 90, C.verde, { filter: 'url(#brillo)' });
    B(0); w.IN(tl, nd, 0, { scale: .5, y: 0 }); D.forEach(function (t, k) { if (ch[k] === '.' || ch[k] === ',') tl.to(t, { opacity: 0, duration: .3 }, k ? '<' : '>.3'); else tl.to(t, { attr: { x: x0 * 1.7 + k * paso * 1.7 }, duration: .5 }, k ? '<' : '>.3'); });
    B(1); w.IN(tl, ti, 0);
    B(2); chs.forEach(function (c, k) { w.IN(tl, c, k ? '<.45' : 0, { y: -260, scale: .5 }); if (k) w.IN(tl, mas[k - 1], '<'); });
    B(3); var t = d.tachar; if (t != null) { w.temblar(tl, chs[t], 0); w.OUT(tl, [chs[t], mas[Math.max(0, t - 1)]], '>', { scale: 0 }); } else tl.to({}, { duration: .1 });
    B(4); w.OUT(tl, nd, 0); w.IN(tl, ok, '<.2', { scale: .5, y: 0 }); tl.to(chs.filter(function (_, k) { return k !== t; }), { y: -10, duration: .2, stagger: .1, yoyo: true, repeat: 1 }, '<');
  } };

  // multiplicar: {titulo, cab:['× 1.000',...], dig:[...], val:['4 × 1.000',...], apagar: índice (opcional), ecuacion} — 3 + n (− 1 si apaga) pasos
  T.multiplicar = { n: function (d) { return 3 + d.dig.length - (d.apagar != null ? 1 : 0); }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), F = w.fila(g, 960, 560, d.cab, d.dig, d.dig.length > 4 ? 160 : 170);
    F.cabs.forEach(function (c) { var t = c.querySelector('text'); t.setAttribute('font-size', 32); t.setAttribute('fill', C.sol); });
    F.vals.forEach(function (v, k) { v.t.setAttribute('font-size', 38); v.t.textContent = d.val[k]; });
    var eq = w.chip(g, 960, 905, Math.min(1560, d.ecuacion.length * 30 + 120), 120, d.ecuacion, { size: d.ecuacion.length > 34 ? 46 : 56, stroke: C.verde, r: 30 });
    var b = 0; B(b++); w.IN(tl, ti, 0);
    B(b++); F.slots.forEach(function (s, k) { w.IN(tl, s, k ? '<.08' : 0); w.IN(tl, F.digs[k], '<'); w.IN(tl, F.cabs[k], '<.1', { scale: 0, y: 0, ease: 'back.out(3)' }); });
    d.dig.forEach(function (_, k) { if (d.apagar == null || k - 1 !== d.apagar) B(b++);
      if (k === d.apagar) { w.IN(tl, F.vals[k], 0, { y: -50 }); tl.to([F.vals[k], F.slots[k]], { opacity: .3, duration: .4 }, '>.5'); }
      else { w.brillar(tl, F.slots[k].r, C.sol, (k - 1 === d.apagar) ? '>' : 0); w.IN(tl, F.vals[k], '<', { y: -50 }); } });
    B(b++); w.IN(tl, eq, 0, { scale: .6, y: 0 });
  } };

  // canje: {titulo, grande:{n:4, txt:'1.000'}, chico:{n:2, txt:'100'}, sueltos:5, ec1, ec2} — 5 pasos
  T.canje = { n: function () { return 5; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'CANJES'), ng = d.grande.n, nc = d.chico.n;
    var G = []; for (var k = 0; k < ng; k++) { var p = w.pieza(g, 330 + k * 200, 560); w.caja(p, 0, 0, 170, 170, 'url(#gAqua)', '#d8fff7', 26, 5); w.txt(p, 0, 4, d.grande.txt, 44, '#06282a'); G.push(p); }
    var CH = []; for (k = 0; k < nc + 10; k++) { var q = w.pieza(g, 1180 + (k % 4) * 125, 420 + Math.floor(k / 4) * 112); w.caja(q, 0, 0, 108, 96, 'url(#gCaja)', '#f3d29a', 18, 4); w.txt(q, 0, 3, d.chico.txt, 34, '#fff8ea'); CH.push(q); }
    var su = w.pieza(g, 960, 790); for (k = 0; k < (d.sueltos || 0); k++) w.el('circle', { cx: (k - ((d.sueltos || 1) - 1) / 2) * 46, cy: 0, r: 18, fill: C.sol }, su);
    var e1 = w.chip(g, 960, 790, 760, 100, d.ec1, { size: 54, stroke: C.linea, r: 30 }), e2 = w.chip(g, 960, 920, 760, 100, d.ec2, { size: 54, stroke: C.sol, r: 30 });
    B(0); w.IN(tl, ti, 0);
    B(1); G.forEach(function (m, k) { w.IN(tl, m, k ? '<.12' : 0); }); CH.slice(0, nc).forEach(function (c) { w.IN(tl, c, '<.12'); }); w.IN(tl, su, '<.2');
    B(2); var ul = G[ng - 1]; w.temblar(tl, ul, 0); w.OUT(tl, ul, '>', { scale: 1.5, duration: .3 });
    CH.slice(nc).forEach(function (c, j) { var i = nc + j; tl.fromTo(c, { opacity: 0, x: 330 + (ng - 1) * 200 - (1180 + (i % 4) * 125), y: 560 - (420 + Math.floor(i / 4) * 112), scale: .3 }, { opacity: 1, x: 0, y: 0, scale: 1, duration: .55, ease: 'power3.out' }, j ? '<.06' : '>-.1'); });
    B(3); w.OUT(tl, su, 0); w.IN(tl, e1, '<'); w.IN(tl, e2, '>.4');
    B(4); tl.to(e1, { opacity: .45, duration: .4 }); w.pop(tl, e2, '>');
  } };

  // ejemplo: {numero, cab, dig, val, lineas:['Aditiva: ...','Multiplicativa: ...'], suma:[50000, 53000, 53600, 53608], destacar, etiqueta} — 7 pasos
  T.ejemplo = { n: function () { return 7; }, armar: function (g, tl, B, d) {
    var n = w.pieza(g, 960, 260); w.txt(n, 0, 0, d.numero, 110, C.txt);
    var F = w.fila(g, 960, 520, d.cab, d.dig, d.cab.length > 4 ? 170 : 190, 135);
    F.slots.forEach(function (s) { s.r.setAttribute('height', 190); s.r.setAttribute('y', -95); }); F.digs.forEach(function (x) { x.t.setAttribute('font-size', 140); }); F.vals.forEach(function (v, k) { v.t.setAttribute('font-size', 42); v.t.textContent = d.val[k]; });
    var L = d.lineas.map(function (l, k) { return w.chip(g, 960, 790 + k * 120, 1300, 100, l, { size: l.length > 40 ? 40 : 48, stroke: k ? C.aqua : C.sol, r: 26 }); });
    var cu = w.pieza(g, 960, 850); w.caja(cu, 0, 0, 760, 170, 'url(#gCard)', C.verde, 34, 6); var S = d.suma || [0], ct = w.txt(cu, 0, 4, S[0].toLocaleString('es-AR'), 110, C.verde);
    var tr = d.etiqueta ? w.etiqueta(g, 960, 940, d.etiqueta) : null;
    B(0); w.IN(tl, n, 0, { scale: .5, y: 0 });
    B(1); F.slots.forEach(function (s, k) { w.IN(tl, s, k ? '<.06' : 0); w.IN(tl, F.cabs[k], '<'); }); F.digs.forEach(function (x, k) { w.IN(tl, x, k ? '<.2' : '>-.1', { y: -400, ease: 'bounce.out', d: .6 }); });
    B(2); F.vals.forEach(function (v, k) { w.IN(tl, v, k ? '<.6' : 0, { y: -40 }); });
    B(3); w.IN(tl, L[0], 0);
    B(4); if (L[1]) w.IN(tl, L[1], 0); else tl.to({}, { duration: .1 });
    B(5); w.OUT(tl, L, 0); w.IN(tl, cu, '>'); for (var i = 1; i < S.length; i++) w.contador(tl, ct, S[i - 1], S[i], '>.4', .7); w.pop(tl, cu, '>');
    B(6); w.OUT(tl, cu, 0); if (d.destacar != null) { w.brillar(tl, F.slots[d.destacar].r, C.sol, '>'); w.pop(tl, F.digs[d.destacar], '<'); } if (tr) w.IN(tl, tr, '<.2');
  } };

  // fichas: {fichas:['0',...,'9'], grande:'7.093.582.461', etiqueta:'GRUPOS DE 10'} — 3 pasos: caen las fichas, número grande, se agrupan
  T.fichas = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var n = d.fichas.length, gap = Math.min(140, 1500 / n), F = d.fichas.map(function (f, k) { return w.chip(g, 960 + (k - (n - 1) / 2) * gap, 520, gap - 24, 150, f, { r: 26, size: f.length > 2 ? 44 : 86, stroke: C.aqua }); });
    var gr = w.pieza(g, 960, 800); w.txt(gr, 0, 0, d.grande, 110, C.sol, { filter: 'url(#brillo)' });
    var an = w.pieza(g, 960, 520); w.el('rect', { x: -n * gap / 2 - 30, y: -110, width: n * gap + 60, height: 220, rx: 110, fill: 'none', stroke: C.sol, 'stroke-width': 8, 'stroke-dasharray': '24 18' }, an);
    var et = w.etiqueta(g, 960, 790, d.etiqueta);
    B(0); F.forEach(function (c, k) { w.IN(tl, c, k ? '<.09' : 0, { y: -300, ease: 'bounce.out', d: .7 }); });
    B(1); w.IN(tl, gr, 0, { scale: .4, y: 0 }); tl.to(F, { y: -20, duration: .25, stagger: { each: .05, yoyo: true, repeat: 1 } }, '<');
    B(2); w.OUT(tl, gr, 0); w.IN(tl, an, '<.2', { scale: 1.2, y: 0 }); w.IN(tl, et, '<.3');
  } };

  // recta: {min, max, paso, marcas:[{v, txt}], salto:[desde, hasta] (opcional)} — 1 + marcas pasos
  T.recta = { n: function (d) { return 1 + d.marcas.length; }, armar: function (g, tl, B, d) {
    var X0 = 220, X1 = 1700, Y = 640, sx = function (v) { return X0 + (v - d.min) / (d.max - d.min) * (X1 - X0); };
    var eje = w.pieza(g, 0, 0); w.el('line', { x1: X0 - 40, y1: Y, x2: X1 + 40, y2: Y, stroke: C.txt, 'stroke-width': 6, 'stroke-linecap': 'round' }, eje);
    for (var v = d.min; v <= d.max + 1e-9; v += d.paso) { w.el('line', { x1: sx(v), y1: Y - 22, x2: sx(v), y2: Y + 22, stroke: C.suave, 'stroke-width': 4 }, eje); w.txt(eje, sx(v), Y + 60, String(+v.toFixed(4)).replace('.', ','), 30, C.suave); }
    var M = d.marcas.map(function (m, k) { var p = w.pieza(g, sx(m.v), Y), col = W.PAL[(k + 1) % W.PAL.length]; w.el('circle', { r: 20, fill: col, stroke: '#fff', 'stroke-width': 5 }, p);
      var tw = String(m.txt).length * 19 + 50, ly = k % 2 ? -175 : -90; if (k % 2) w.el('line', { x1: 0, y1: -20, x2: 0, y2: ly + 35, stroke: col, 'stroke-width': 3 }, p); w.caja(p, 0, ly, tw, 70, 'rgba(6,20,22,.88)', col, 30, 4); w.txt(p, 0, ly, m.txt, 34, '#fff'); return p; });
    B(0); w.IN(tl, eje, 0, { scaleX: 0, y: 0, ease: 'power2.out' });
    M.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { y: -200, ease: 'bounce.out', d: .7 }); });
  } };

  // cuenta: {filas:['4.205','1.380'], op:'+', resultado:'5.585'} — 2 pasos: la cuenta, el resultado
  T.cuenta = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var L = Math.max.apply(null, d.filas.concat([d.resultado]).map(function (f) { return String(f).length; })), size = Math.min(120, Math.floor(1100 / (L * .6))), cw = size * .6;
    var p = w.pieza(g, 960, 560), n = d.filas.length, xr = L * cw / 2 + 40, h = size * 1.08, xo = xr - L * cw - 70;
    d.filas.forEach(function (f, k) { w.txt(p, xr, (k - n / 2) * h, f, size, C.txt, { 'text-anchor': 'end', 'font-family': 'ui-monospace,Menlo,Consolas,monospace' }); });
    w.txt(p, xo, (n - 1 - n / 2) * h, d.op || '+', size * .9, C.sol); var yl = (n - n / 2) * h - size * .45; w.el('line', { x1: xo - 40, y1: yl, x2: xr + 20, y2: yl, stroke: C.sol, 'stroke-width': 8 }, p);
    var r = w.pieza(g, 960, 560); w.txt(r, xr, yl + size * .7, d.resultado, size, C.verde, { 'text-anchor': 'end', 'font-family': 'ui-monospace,Menlo,Consolas,monospace', filter: 'url(#brillo)' });
    B(0); w.IN(tl, p, 0); B(1); w.IN(tl, r, 0, { y: 60 });
  } };

  // fraccion: {num, den, forma:'pizza'|'barra', txt} — 2 pasos: se divide, se pintan las partes
  T.fraccion = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var p = w.pieza(g, 760, 600), partes = [], n = d.den, i;
    if (d.forma === 'barra') { var bw = 900 / n; for (i = 0; i < n; i++) partes.push(w.el('rect', { x: -450 + i * bw, y: -110, width: bw, height: 220, fill: '#1e474b', stroke: '#0c292b', 'stroke-width': 6 }, p)); }
    else { var R = 280; for (i = 0; i < n; i++) { var a0 = -Math.PI / 2 + i * 2 * Math.PI / n, a1 = a0 + 2 * Math.PI / n; partes.push(w.el('path', { d: 'M0 0 L' + R * Math.cos(a0) + ' ' + R * Math.sin(a0) + ' A' + R + ' ' + R + ' 0 ' + (n === 1 ? 1 : 0) + ' 1 ' + R * Math.cos(a1) + ' ' + R * Math.sin(a1) + ' Z', fill: '#1e474b', stroke: '#0c292b', 'stroke-width': 6 }, p)); } }
    var f = w.pieza(g, 1450, 600); w.txt(f, 0, -110, String(d.num), 150, C.sol); w.el('line', { x1: -100, y1: 0, x2: 100, y2: 0, stroke: C.txt, 'stroke-width': 10 }, f); w.txt(f, 0, 110, String(d.den), 150, C.txt); if (d.txt) w.multi(f, 0, 270, d.txt, 36, C.suave, 500);
    B(0); w.IN(tl, p, 0, { scale: .6, y: 0 }); w.IN(tl, f, '<.2', { x: 100, y: 0 });
    B(1); partes.slice(0, d.num).forEach(function (q, k) { tl.to(q, { attr: { fill: C.sol }, duration: .25 }, k ? '<.15' : '>'); });
  } };

  // ecuacion: {pasos:['2x + 3 = 11', '2x = 8', 'x = 4'], notas:['restamos 3', 'dividimos por 2', '']} — n pasos (la balanza muestra la igualdad)
  T.ecuacion = { n: function (d) { return d.pasos.length; }, armar: function (g, tl, B, d) {
    var bal = w.pieza(g, 960, 760); w.el('path', { d: 'M-50 200 L50 200 L0 20 Z', fill: C.linea }, bal); w.el('rect', { x: -520, y: 0, width: 1040, height: 20, rx: 10, fill: C.sol }, bal);
    w.caja(bal, -400, -40, 300, 70, 'rgba(127,211,196,.2)', C.aqua, 16, 4); w.caja(bal, 400, -40, 300, 70, 'rgba(244,182,63,.2)', C.sol, 16, 4);
    var E = d.pasos.map(function (s, k) { var p = w.pieza(g, 960, 420); w.txt(p, 0, 0, s, Math.min(120, Math.floor(1500 / (String(s).length * .58))), k === d.pasos.length - 1 ? C.verde : C.txt); if (d.notas && d.notas[k]) w.txt(p, 0, 110, d.notas[k], 40, C.sol); return p; });
    E.forEach(function (p, k) { B(k); if (!k) w.IN(tl, bal, 0); else w.OUT(tl, E[k - 1], 0, { y: -80 }); w.IN(tl, p, k ? '>' : '<', { y: 80 }); tl.to(bal, { rotation: 3, svgOrigin: '960 760', duration: .15, yoyo: true, repeat: 1 }, '<'); });
  } };

  // figura: {tipo:'triangulo'|'cuadrado'|'rectangulo'|'circulo'|'angulo', grados, etiquetas:[...]} — 2 pasos
  T.figura = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var p = w.pieza(g, 960, 620), dd = { triangulo: 'M-300 200 L300 200 L0 -260 Z', cuadrado: 'M-250 -250 H250 V250 H-250 Z', rectangulo: 'M-380 -220 H380 V220 H-380 Z' }[d.tipo], path;
    if (d.tipo === 'circulo') path = w.el('circle', { r: 280, fill: 'rgba(127,211,196,.15)', stroke: C.aqua, 'stroke-width': 10 }, p);
    else if (d.tipo === 'angulo') { var a = (d.grados || 60) * Math.PI / 180; path = w.el('path', { d: 'M400 200 L-300 200 L' + (-300 + 700 * Math.cos(a)) + ' ' + (200 - 700 * Math.sin(a)), fill: 'none', stroke: C.aqua, 'stroke-width': 10, 'stroke-linejoin': 'round' }, p);
      w.el('path', { d: 'M-160 200 A140 140 0 0 0 ' + (-300 + 140 * Math.cos(a)) + ' ' + (200 - 140 * Math.sin(a)), fill: 'none', stroke: C.sol, 'stroke-width': 8 }, p); w.txt(p, -90, 140, (d.grados || 60) + '°', 50, C.sol); }
    else path = w.el('path', { d: dd, fill: 'rgba(127,211,196,.15)', stroke: C.aqua, 'stroke-width': 10, 'stroke-linejoin': 'round' }, p);
    path.setAttribute('stroke-dasharray', 4000); path.setAttribute('stroke-dashoffset', 4000);
    var L = w.pieza(g, 960, 940); w.txt(L, 0, 0, (d.etiquetas || []).join('   ·   '), 40, C.sol);
    B(0); tl.set(p, { opacity: 1 }); tl.to(path, { attr: { 'stroke-dashoffset': 0 }, duration: 1.2, ease: 'power2.inOut' });
    B(1); w.IN(tl, L, 0);
  } };

  // grilla: {filas:10, cols:10, titulo, resaltar:[{fila, col, txt}] } — 1 + resaltar pasos (tabla pitagórica, etc.)
  T.grilla = { n: function (d) { return 1 + (d.resaltar || []).length; }, armar: function (g, tl, B, d) {
    var nf = d.filas || 10, nc = d.cols || 10, s = Math.min(54, 560 / (nf + 1), 1300 / (nc + 1)), x0 = 960 - (nc) * s / 2, y0 = 340;
    var ti = d.titulo ? w.titulo(g, d.titulo, 250) : null, G = w.pieza(g, 0, 0), celdas = {};
    for (var r = 0; r <= nf; r++) for (var c = 0; c <= nc; c++) { var head = !r || !c, v = !r && !c ? '×' : !r ? c : !c ? r : r * c;
      celdas[r + ',' + c] = w.el('rect', { x: x0 + (c - .5) * s, y: y0 + (r - .5) * s, width: s - 4, height: s - 4, rx: 8, fill: head ? '#2c7f78' : '#17383b' }, G); w.txt(G, x0 + c * s - 2, y0 + r * s - 2, String(v), s * .42, head ? '#06282a' : C.txt); }
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, G, ti ? '<' : 0, { scale: .9, y: 0 });
    (d.resaltar || []).forEach(function (h, k) { B(k + 1); var col = W.PAL[(k + 1) % W.PAL.length];
      for (var c2 = 0; c2 <= h.col; c2++) tl.to(celdas[h.fila + ',' + c2], { attr: { fill: c2 === h.col ? col : 'rgba(127,211,196,.35)' }, duration: .12 }, c2 ? '<.04' : '>');
      for (var r2 = 0; r2 < h.fila; r2++) tl.to(celdas[r2 + ',' + h.col], { attr: { fill: 'rgba(127,211,196,.35)' }, duration: .12 }, '<.04');
      if (h.txt) { var t = w.chip(g, 960, 960, h.txt.length * 26 + 100, 76, h.txt, { size: 38, stroke: col }); w.IN(tl, t, '>'); } });
  } };

  function esPrimo(v) { if (v < 2) return false; for (var i = 2; i * i <= v; i++) if (v % i === 0) return false; return true; }

  // criba: {hasta:50, cols:10, tachar:[2,3,5,7], txt} — 2 + tachar pasos: el tablero, se tachan los múltiplos de cada primo, brillan los primos
  T.criba = { n: function (d) { return 2 + d.tachar.length; }, armar: function (g, tl, B, d) {
    var N = d.hasta || 50, nc = d.cols || 10, nf = Math.ceil(N / nc), s = Math.min(112, 560 / nf, 1400 / nc), x0 = 960 - (nc - 1) * s / 2, y0 = 590 - (nf - 1) * s / 2 - 40;
    var G = w.pieza(g, 0, 0), R = {}, X = {}, fuera = {}, v, j, yb = y0 + (nf - 1) * s + s / 2 + 70;
    for (v = 1; v <= N; v++) { var x = x0 + ((v - 1) % nc) * s, y = y0 + Math.floor((v - 1) / nc) * s;
      R[v] = w.el('rect', { x: x - s / 2 + 5, y: y - s / 2 + 5, width: s - 10, height: s - 10, rx: 14, fill: '#17383b', stroke: C.linea, 'stroke-width': 3 }, G); X[v] = w.txt(G, x, y, String(v), s * .42, C.txt); }
    B(0); w.IN(tl, G, 0, { scale: .92, y: 0 }); tl.to([R[1], X[1]], { opacity: .25, duration: .3 }, '>');
    var prev = null;
    d.tachar.forEach(function (p, k) { B(k + 1); var col = W.PAL[(k + 1) % W.PAL.length], ch = w.chip(g, 960, yb, 520, 76, 'Múltiplos de ' + p, { size: 38, stroke: col });
      if (prev) w.OUT(tl, prev, 0); w.IN(tl, ch, prev ? '<' : 0); prev = ch;
      tl.to(R[p], { attr: { fill: col, stroke: '#fff', 'stroke-width': 6 }, duration: .3 }, '<'); tl.to(X[p], { attr: { fill: '#06282a' }, duration: .3 }, '<');
      for (var m = 2 * p, j = 0; m <= N; m += p) if (!fuera[m]) { fuera[m] = 1; tl.to(R[m], { attr: { fill: 'rgba(0,0,0,.3)', stroke: col }, duration: .12 }, j++ ? '<.05' : '>'); tl.to(X[m], { opacity: .22, duration: .12 }, '<'); } });
    B(d.tachar.length + 1); if (prev) w.OUT(tl, prev, 0);
    for (v = 2, j = 0; v <= N; v++) if (!fuera[v]) { tl.to(R[v], { attr: { fill: C.sol, stroke: '#ffe7a8', 'stroke-width': 5 }, duration: .15 }, j++ ? '<.06' : '>'); tl.to(X[v], { attr: { fill: '#3a2a00' }, duration: .15 }, '<'); }
    if (d.txt) { var fin = w.etiqueta(g, 960, yb, d.txt); w.IN(tl, fin, '>.1'); }
  } };

  // geo: dibujo geométrico paso a paso. {titulo, vista:[xmin,xmax,ymin,ymax], pasos:[{el:[...], txt}]} — n = pasos (cada paso dibuja sus elementos y muestra su texto abajo)
  // elementos (coordenadas en unidades de la vista, y hacia arriba):
  //  {seg:[[x,y],[x,y]], color, dash, flechas}  {pol:[[x,y],...], fill}  {pt:[x,y], txt, dx, dy}  {txt:[x,y], s:'texto', color, size}
  //  {ang:[x,y], a1, a2, r, txt, recto, color} (grados, antihorario desde el eje x)  {arco:[x,y], r, a1, a2} (arco de compás, punteado)  {marca:[[x,y],[x,y]], n}
  T.geo = { n: function (d) { return d.pasos.length; }, armar: function (g, tl, B, d) {
    var v = d.vista || [0, 10, 0, 6], top = d.titulo ? 340 : 270, bot = 880, s = Math.min(1440 / (v[1] - v[0]), (bot - top) / (v[3] - v[2]));
    var cx = 960 - (v[0] + v[1]) / 2 * s, cy = (top + bot) / 2 + (v[2] + v[3]) / 2 * s;
    function X(p) { return cx + p[0] * s; } function Y(p) { return cy - p[1] * s; }
    var ti = d.titulo ? w.titulo(g, d.titulo, 270) : null, cap = null;
    function linea(G, a, b, col, dash, ancho) { return w.el('line', { x1: X(a), y1: Y(a), x2: X(b), y2: Y(b), stroke: col || C.txt, 'stroke-width': ancho || 6, 'stroke-linecap': 'round', 'stroke-dasharray': dash ? '16 12' : null }, G); }
    function arcoPath(c, r, a1, a2) { var R = r * s, p1 = [X(c) + R * Math.cos(a1 * Math.PI / 180), Y(c) - R * Math.sin(a1 * Math.PI / 180)], p2 = [X(c) + R * Math.cos(a2 * Math.PI / 180), Y(c) - R * Math.sin(a2 * Math.PI / 180)];
      return 'M' + p1[0] + ' ' + p1[1] + ' A' + R + ' ' + R + ' 0 ' + (((a2 - a1) % 360 + 360) % 360 > 180 ? 1 : 0) + ' 0 ' + p2[0] + ' ' + p2[1]; }
    var grupos = d.pasos.map(function (p, k) { var G = w.pieza(g, 0, 0), trazos = [], textos = [];
      (p.el || []).forEach(function (e) { var col = e.color || (k ? W.PAL[k % W.PAL.length] : C.txt), t;
        if (e.pol) { t = w.el('polygon', { points: e.pol.map(function (q) { return X(q) + ',' + Y(q); }).join(' '), fill: e.fill || 'rgba(127,211,196,.16)', stroke: e.color || C.aqua, 'stroke-width': 6, 'stroke-linejoin': 'round' }, G); trazos.push(t); }
        else if (e.seg) { t = linea(G, e.seg[0], e.seg[1], col, e.dash, e.ancho); trazos.push(t);
          if (e.flechas) e.seg.forEach(function (q, j) { var o = e.seg[1 - j], a = Math.atan2(Y(q) - Y(o), X(q) - X(o)); var h = w.el('path', { d: 'M0 0 L-26 -13 L-26 13 Z', fill: col, transform: 'translate(' + X(q) + ' ' + Y(q) + ') rotate(' + a * 180 / Math.PI + ')' }, G); textos.push(h); }); }
        else if (e.arco) { t = w.el('path', { d: arcoPath(e.arco, e.r, e.a1, e.a2), fill: 'none', stroke: e.color || C.sol, 'stroke-width': 4, 'stroke-dasharray': '14 10' }, G); textos.push(t); }
        else if (e.ang) { var r = e.r || 0.8, col2 = e.color || C.sol;
          if (e.recto) { var u = [Math.cos(e.a1 * Math.PI / 180), Math.sin(e.a1 * Math.PI / 180)], q = [Math.cos(e.a2 * Math.PI / 180), Math.sin(e.a2 * Math.PI / 180)], m = r * 0.6, c0 = e.ang;
            t = w.el('path', { d: 'M' + X([c0[0] + u[0] * m, c0[1] + u[1] * m]) + ' ' + Y([c0[0] + u[0] * m, c0[1] + u[1] * m]) + ' L' + X([c0[0] + (u[0] + q[0]) * m, c0[1] + (u[1] + q[1]) * m]) + ' ' + Y([c0[0] + (u[0] + q[0]) * m, c0[1] + (u[1] + q[1]) * m]) + ' L' + X([c0[0] + q[0] * m, c0[1] + q[1] * m]) + ' ' + Y([c0[0] + q[0] * m, c0[1] + q[1] * m]), fill: 'none', stroke: col2, 'stroke-width': 5 }, G); }
          else t = w.el('path', { d: arcoPath(e.ang, r, e.a1, e.a2), fill: 'none', stroke: col2, 'stroke-width': 6 }, G);
          textos.push(t);
          if (e.txt) { var am = (e.a1 + e.a2) / 2 * Math.PI / 180, rt = r + (e.dt || 0.55); textos.push(w.txt(G, X(e.ang) + rt * s * Math.cos(am), Y(e.ang) - rt * s * Math.sin(am), e.txt, e.size || 46, col2)); } }
        else if (e.marca) { var a0 = e.marca[0], b0 = e.marca[1], mx = (a0[0] + b0[0]) / 2, my = (a0[1] + b0[1]) / 2, dx = b0[0] - a0[0], dy = b0[1] - a0[1], L = Math.hypot(dx, dy), nx = -dy / L, ny = dx / L, ux = dx / L, uy = dy / L, n = e.n || 1, h2 = 0.18;
          for (var j = 0; j < n; j++) { var o = (j - (n - 1) / 2) * 0.16; textos.push(linea(G, [mx + ux * o - nx * h2, my + uy * o - ny * h2], [mx + ux * o + nx * h2, my + uy * o + ny * h2], e.color || C.sol, false, 5)); } }
        else if (e.pt) { textos.push(w.el('circle', { cx: X(e.pt), cy: Y(e.pt), r: 11, fill: e.color || C.sol }, G)); if (e.txt) textos.push(w.txt(G, X(e.pt) + (e.dx == null ? -34 : e.dx * s), Y(e.pt) + (e.dy == null ? 34 : -e.dy * s), e.txt, 44, e.color || C.txt)); }
        else if (e.txt) textos.push(w.txt(G, X(e.txt), Y(e.txt), e.s, e.size || 44, e.color || C.txt));
      });
      return { G: G, trazos: trazos, textos: textos, txt: p.txt }; });
    grupos.forEach(function (q, k) { B(k);
      if (!k && ti) w.IN(tl, ti, 0);
      tl.set(q.G, { opacity: 1 }, k ? '>' : '<');
      q.trazos.forEach(function (t, j) { var L = 4000; t.setAttribute('stroke-dasharray', L); t.setAttribute('stroke-dashoffset', L); tl.to(t, { attr: { 'stroke-dashoffset': 0 }, duration: .7, ease: 'power2.inOut' }, j ? '<.15' : '>'); });
      if (q.textos.length) tl.fromTo(q.textos, { opacity: 0 }, { opacity: 1, duration: .35, stagger: .08 }, q.trazos.length ? '>-.2' : '>');
      if (cap) w.OUT(tl, cap, '<'); cap = null;
      if (q.txt) { cap = w.chip(g, 960, 960, Math.min(1500, q.txt.length * 24 + 110), 80, q.txt, { size: 40, stroke: W.PAL[(k + 1) % W.PAL.length] }); w.IN(tl, cap, '<.1'); }
    });
  } };

  // saltos: {titulo, min, max, cada (cada cuánto se rotula, 1 por defecto), inicio, saltos:[{a, txt}]} — 1 + saltos pasos. Flechas curvas sobre la recta: positivas arriba (verdes), negativas abajo (coral).
  T.saltos = { n: function (d) { return 1 + d.saltos.length; }, armar: function (g, tl, B, d) {
    var X0 = 220, X1 = 1700, Y = 660, sx = function (v) { return X0 + (v - d.min) / (d.max - d.min) * (X1 - X0); }, cada = d.cada || 1;
    var ti = d.titulo ? w.titulo(g, d.titulo, 290) : null, eje = w.pieza(g, 0, 0);
    w.el('line', { x1: X0 - 40, y1: Y, x2: X1 + 40, y2: Y, stroke: C.txt, 'stroke-width': 6, 'stroke-linecap': 'round' }, eje);
    for (var v = d.min; v <= d.max; v++) { var rot = v % cada === 0; w.el('line', { x1: sx(v), y1: Y - (rot ? 20 : 11), x2: sx(v), y2: Y + (rot ? 20 : 11), stroke: v === 0 ? C.sol : C.suave, 'stroke-width': v === 0 ? 6 : 4 }, eje);
      if (rot) w.txt(eje, sx(v), Y + 58, String(v).replace('-', '−'), (d.max - d.min) / cada > 24 ? 26 : 32, v === 0 ? C.sol : C.suave); }
    var pos = d.inicio, dot = w.pieza(g, sx(pos), Y); w.el('circle', { r: 22, fill: C.sol, stroke: '#fff', 'stroke-width': 5 }, dot);
    var et = w.pieza(g, sx(pos), Y); w.caja(et, 0, -70, 110, 58, 'rgba(6,20,22,.9)', C.sol, 20, 3); var etT = w.txt(et, 0, -70, String(pos).replace('-', '−'), 34, C.sol);
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, eje, ti ? '<' : 0, { scaleX: 0, y: 0 }); w.IN(tl, dot, '>', { scale: 0, y: 0 }); w.IN(tl, et, '<');
    d.saltos.forEach(function (s, k) { B(k + 1); var a = sx(pos), b = sx(pos + s.a), arriba = s.a >= 0, col = arriba ? C.verde : C.coral, h = Math.min(230, 70 + Math.abs(b - a) * 0.35) * (arriba ? -1 : 1);
      var arc = w.el('path', { d: 'M' + a + ' ' + Y + ' Q' + (a + b) / 2 + ' ' + (Y + h * 2) + ' ' + b + ' ' + Y, fill: 'none', stroke: col, 'stroke-width': 7, 'stroke-linecap': 'round', 'stroke-dasharray': 3000, 'stroke-dashoffset': 3000 }, g);
      var lab = w.pieza(g, (a + b) / 2, Y + h + (arriba ? -45 : 45)); w.txt(lab, 0, 0, s.txt || ((s.a > 0 ? '+' : '−') + Math.abs(s.a)), 46, col);
      var hasta = pos + s.a; pos = hasta;
      tl.set(arc, { opacity: 1 }, '>'); tl.to(arc, { attr: { 'stroke-dashoffset': 0 }, duration: .8, ease: 'power2.inOut' }, '>'); w.IN(tl, lab, '<.3', { scale: .5, y: 0 });
      tl.to([dot.parentNode, et.parentNode], { attr: { transform: 'translate(' + b + ' ' + Y + ')' }, duration: .8, ease: 'power2.inOut' }, '<-.3');
      tl.call(function () { etT.textContent = String(hasta).replace('-', '−'); }, null, '>'); w.pop(tl, et, '>'); });
  } };

  // platillos: balanza con objetos. {titulo, estados:[{izq:['🛍️','🛍️','2 kg'], der:['14 kg'], txt:'3x + 2 = 14'}]} — n = estados (cada paso cambia lo que hay en los platillos; la balanza queda en equilibrio)
  T.platillos = { n: function (d) { return d.estados.length; }, armar: function (g, tl, B, d) {
    var ti = d.titulo ? w.titulo(g, d.titulo, 270) : null, base = w.pieza(g, 960, 560);
    w.el('path', { d: 'M-60 380 L60 380 L0 40 Z', fill: C.linea }, base); w.el('circle', { cx: 0, cy: 40, r: 22, fill: C.sol }, base);
    w.el('rect', { x: -620, y: 28, width: 1240, height: 24, rx: 12, fill: C.sol }, base);
    [-470, 470].forEach(function (x) { w.el('line', { x1: x, y1: 52, x2: x, y2: 230, stroke: C.suave, 'stroke-width': 4 }, base); w.el('path', { d: 'M' + (x - 230) + ' 230 Q' + x + ' 300 ' + (x + 230) + ' 230 Z', fill: 'rgba(127,211,196,.18)', stroke: C.aqua, 'stroke-width': 5 }, base); });
    function lado(items, x0) { var p = w.pieza(g, 960 + x0, 740), n = items.length, gap = Math.min(110, 440 / Math.max(1, n));
      items.forEach(function (it, k) { var x = (k - (n - 1) / 2) * gap; if (/^\p{Extended_Pictographic}/u.test(it)) w.emoji(p, x, -10, it, Math.min(100, gap * 0.95)); else { w.caja(p, x, -10, Math.max(gap - 10, String(it).length * 24 + 30), 80, 'url(#gSol)', '#ffe7a8', 18, 3); w.txt(p, x, -10, it, 36, '#3a2a00'); } }); return p; }
    var prev = null;
    d.estados.forEach(function (e, k) { B(k); var L = lado(e.izq, -470), R = lado(e.der, 470), cap = e.txt ? w.chip(g, 960, 420, Math.min(1200, e.txt.length * 32 + 120), 96, e.txt, { size: 50, stroke: C.verde, r: 30 }) : null;
      if (!k) { if (ti) w.IN(tl, ti, 0); w.IN(tl, base, ti ? '<' : 0); }
      if (prev) w.OUT(tl, prev, k ? 0 : '<', { y: -60 });
      var nuevos = [L, R].concat(cap ? [cap] : []); nuevos.forEach(function (q, j) { w.IN(tl, q, j ? '<.1' : '>', { y: -120, ease: 'bounce.out', d: .6 }); });
      tl.to(base, { rotation: 2, svgOrigin: '960 600', duration: .15, yoyo: true, repeat: 1 }, '>-.2'); prev = nuevos; });
  } };

  // arbol: {numero:72, ramas:[[2,36],[2,18],[2,9],[3,3]], resultado:'72 = 2³ × 3²'} — 2 + ramas pasos: el número, cada división (primo a la izquierda, sigue el cociente), el resultado
  T.arbol = { n: function (d) { return 2 + d.ramas.length; }, armar: function (g, tl, B, d) {
    var L = d.ramas.length, dy = Math.min(135, 560 / L), dx = Math.min(150, 640 / L), x = 960 - L * dx / 2 - 60, y = 300;
    function nodo(nx, ny, val) { var p = w.pieza(g, nx, ny), pr = esPrimo(val);
      if (pr) w.el('circle', { r: 56, fill: 'url(#gSol)', stroke: '#ffe7a8', 'stroke-width': 5 }, p); else w.caja(p, 0, 0, Math.max(130, String(val).length * 42 + 60), 100, 'url(#gCard)', C.aqua, 24, 5);
      w.txt(p, 0, 0, String(val), 54, pr ? '#3a2a00' : C.txt); return p; }
    B(0); w.IN(tl, nodo(x, y, d.numero), 0, { scale: .5, y: 0 });
    d.ramas.forEach(function (r, k) { B(k + 1); var yn = y + dy, ra = w.pieza(g, 0, 0);
      w.el('line', { x1: x - 20, y1: y + 50, x2: x - dx + 20, y2: yn - 56, stroke: C.suave, 'stroke-width': 6, 'stroke-linecap': 'round' }, ra);
      w.el('line', { x1: x + 20, y1: y + 50, x2: x + dx - 20, y2: yn - 50, stroke: C.suave, 'stroke-width': 6, 'stroke-linecap': 'round' }, ra);
      w.IN(tl, ra, 0, { y: -20 }); w.IN(tl, nodo(x - dx, yn, r[0]), '>-.1', { y: -120, ease: 'bounce.out', d: .6 }); w.IN(tl, nodo(x + dx, yn, r[1]), '<.15', { y: -120, ease: 'bounce.out', d: .6 });
      x += dx; y = yn; });
    B(L + 1); var res = w.chip(g, 1470, 300, Math.min(560, String(d.resultado).length * 30 + 110), 96, d.resultado, { size: 46, stroke: C.verde, r: 30 }); w.IN(tl, res, 0, { scale: .6, y: 0 }); w.pop(tl, res, '>');
  } };
  // ---------- PRIMEROS AÑOS (1.º a 3.º del Nivel Medio): contar y comparar colecciones con dibujos ----------
  function coleccion(g, emo, n, cx, cy, ancho, alto, max) { // n emojis repartidos en filas dentro de un rectángulo
    var cols = Math.min(n, Math.max(1, Math.ceil(n / Math.max(1, Math.round(n / 5 + .49))))), filas = Math.ceil(n / cols);
    var paso = Math.min(max || 170, ancho / cols, alto / filas), P = w.rejilla(n, cx, cy, paso, paso, cols);
    return P.map(function (q) { var o = w.pieza(g, q[0], q[1]); w.emoji(o, 0, 0, emo, paso * .78); o.px = q[0]; o.py = q[1]; o.paso = paso; return o; });
  }
  // contar: {titulo, emoji:'🍎', cantidad: 1-10, etiqueta} — 3 pasos: aparecen los objetos · se cuentan uno por uno (número debajo de cada uno) · el último número dice cuántos hay
  T.contar = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var n = d.cantidad, ti = d.titulo ? w.titulo(g, d.titulo, 270) : null, cols = n > 5 ? Math.ceil(n / 2) : n, filas = Math.ceil(n / cols);
    var paso = Math.min(200, 1400 / cols), alto = paso * .7 + 110, P = w.rejilla(n, 960, filas > 1 ? 520 : 520, paso, alto, cols);
    var O = P.map(function (q) { var o = w.pieza(g, q[0], q[1]); w.emoji(o, 0, 0, d.emoji, paso * .66); o.px = q[0]; o.py = q[1]; return o; });
    var nums = O.map(function (o, k) { var q = w.pieza(g, o.px, o.py + paso * .35 + 44); w.el('circle', { r: 32, fill: C.sol }, q); w.txt(q, 0, 2, String(k + 1), 38, '#3a2a00'); return q; });
    var tot = w.pieza(g, 960, filas > 1 ? 875 : 840); w.caja(tot, 0, 0, 280, 140, 'url(#gCard)', C.sol, 34, 6); w.txt(tot, 0, 4, String(n), 110, C.sol, { filter: 'url(#brillo)' });
    var et = d.etiqueta ? w.etiqueta(g, 960, 900, d.etiqueta) : null;
    B(0); if (ti) w.IN(tl, ti, 0); O.forEach(function (o, k) { w.IN(tl, o, k ? '<.1' : (ti ? '<.2' : 0), { y: -260, scale: .5, ease: 'bounce.out', d: .6 }); });
    // cada número aparece cuando la voz lo dice (paso 2: "1, 2, 3…"), como en los dibujitos para chicos
    var visto = {}; g.alDecir = function (p, paso) { var v = parseInt(String(p).replace(/[^0-9]/g, ''), 10); if (paso < 1 || !(v >= 1 && v <= n) || visto[v]) return; visto[v] = 1;
      gsap.fromTo(nums[v - 1], { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: .4, ease: 'back.out(3)' }); gsap.fromTo(O[v - 1], { scale: 1 }, { scale: 1.22, duration: .2, yoyo: true, repeat: 1 }); };
    B(1); tl.to({}, { duration: .01 });
    B(2); tl.set(nums, { opacity: 1, scale: 1 }, '>+0.05'); w.IN(tl, tot, '>', { scale: .3, y: 0, ease: 'back.out(2.5)' }); w.pop(tl, nums[n - 1], '<.2');
    if (et) { w.OUT(tl, tot, '>.6'); w.IN(tl, et, '<.1'); }
  } };
  // monedas: {titulo, items:[valores], texto, simbolo:'$'} — 3 pasos: aparecen las monedas (≤10) y billetes (≥20) · la voz cuenta sumando ("10, 20, 25") y cada una brilla con su subtotal · total
  T.monedas = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var it = d.items, n = it.length, sim = d.simbolo || '$', ti = d.titulo ? w.titulo(g, d.titulo, 250) : null, paso = Math.min(250, 1500 / n), x0 = 960 - (n - 1) * paso / 2, Y = 520, ac = 0;
    var O = it.map(function (v, k) { var o = w.pieza(g, x0 + k * paso, Y), bill = v >= 20, sz = bill ? Math.min(220, paso * .9) : Math.min(170, paso * .78);
      if (bill) { w.caja(o, 0, 0, sz, sz * .55, '#2f8f5b', '#bff0c9', 18, 5); w.txt(o, 0, 6, sim + v, sz * .26, '#ffffff'); }
      else { w.el('circle', { r: sz / 2, fill: v >= 5 ? '#e7b53c' : '#c9ccd3', stroke: '#fff3c4', 'stroke-width': 6 }, o); w.txt(o, 0, 4, sim + v, sz * .3, '#3a2a00'); }
      return o; });
    var sub = it.map(function (v, k) { ac += v; var q = w.pieza(g, x0 + k * paso, Y + 170); w.el('circle', { r: 44, fill: C.sol }, q); w.txt(q, 0, 2, String(ac), ac >= 100 ? 30 : 38, '#3a2a00'); q.v = ac; return q; });
    var tot = w.pieza(g, 960, 880); w.caja(tot, 0, 0, 520, 140, 'url(#gCard)', C.sol, 34, 6); w.txt(tot, 0, 4, d.texto || (sim + ac), 64, C.sol, { filter: 'url(#brillo)' });
    B(0); if (ti) w.IN(tl, ti, 0); O.forEach(function (o, k) { w.IN(tl, o, k ? '<.12' : (ti ? '<.2' : 0), { y: -240, scale: .5, ease: 'bounce.out', d: .6 }); });
    var visto = {}; g.alDecir = function (p, pa) { var v = parseInt(String(p).replace(/[^0-9]/g, ''), 10); if (pa < 1) return;
      for (var k = 0; k < n; k++) if (sub[k].v === v && !visto[k]) { visto[k] = 1; gsap.fromTo(sub[k], { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: .4, ease: 'back.out(3)' }); gsap.fromTo(O[k], { scale: 1 }, { scale: 1.2, duration: .2, yoyo: true, repeat: 1 }); break; } };
    B(1); tl.to({}, { duration: .01 });
    B(2); tl.set(sub, { opacity: 1, scale: 1 }, '>+0.05'); w.IN(tl, tot, '>', { scale: .3, y: 0, ease: 'back.out(2.5)' });
  } };
  // parejas: {a:{emoji, n}, b:{emoji, n}, texto} — 3 pasos: dos filas · se unen de a uno (uno con uno) · lo que sobra brilla y sale el texto ("¡HAY MÁS 🐶!" o "¡HAY IGUAL!")
  T.parejas = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var na = d.a.n, nb = d.b.n, m = Math.max(na, nb), paso = Math.min(170, 1500 / m), x0 = 960 - (m - 1) * paso / 2, YA = 380, YB = 700;
    function fila(e, n, y) { var arr = []; for (var k = 0; k < n; k++) { var o = w.pieza(g, x0 + k * paso, y); w.emoji(o, 0, 0, e, paso * .72); arr.push(o); } return arr; }
    var A = fila(d.a.emoji, na, YA), Bf = fila(d.b.emoji, nb, YB), par = Math.min(na, nb);
    var L = []; for (var k = 0; k < par; k++) L.push(w.flecha(g, x0 + k * paso, YA + paso * .42, x0 + k * paso, YB - paso * .42, C.aqua, 7));
    L.forEach(function (f) { f.pu.remove(); });
    var sobran = na > nb ? A.slice(nb) : Bf.slice(na);
    var cap = d.texto ? w.chip(g, 960, 905, Math.min(1500, d.texto.length * 34 + 140), 100, d.texto, { size: 52, stroke: C.sol, r: 34 }) : null;
    B(0); A.forEach(function (o, k) { w.IN(tl, o, k ? '<.07' : 0, { y: -200, ease: 'bounce.out', d: .5 }); }); Bf.forEach(function (o, k) { w.IN(tl, o, k ? '<.07' : '>-.1', { y: 200, ease: 'bounce.out', d: .5 }); });
    B(1); L.forEach(function (f, k) { tl.to(f.l, { attr: { 'stroke-dashoffset': 0 }, duration: .3, ease: 'power2.inOut' }, k ? '>-.1' : '>'); });
    B(2); sobran.forEach(function (o, k) { tl.to(o, { scale: 1.25, duration: .25, yoyo: true, repeat: 3 }, k ? '<.05' : '>'); }); if (cap) w.IN(tl, cap, sobran.length ? '<.3' : 0, { scale: .6, y: 0 });
  } };
  // igualar: {a:{emoji, n}, b:{emoji, n}, accion:'agregar'|'quitar', texto} — 3 pasos: dos grupos con su número · se agregan a la más chica (o se quitan de la más grande) hasta que haya igual · signo = y texto
  T.igualar = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var na = d.a.n, nb = d.b.n, ag = d.accion !== 'quitar', meta = ag ? Math.max(na, nb) : Math.min(na, nb);
    function grupo(e, n, cx, cant) { var p = w.pieza(g, cx, 570); w.caja(p, 0, 0, 640, 500, 'rgba(127,211,196,.08)', C.linea, 40, 5); var O = coleccion(g, e, cant, cx, 560, 560, 400, 150); return { caja: p, O: O }; }
    var GA = grupo(d.a.emoji, na, 560, ag ? meta : na), GB = grupo(d.b.emoji, nb, 1360, ag ? meta : nb);
    function num(cx, v) { var q = w.pieza(g, cx, 900); w.el('circle', { r: 58, fill: C.sol }, q); q.t = w.txt(q, 0, 4, String(v), 64, '#3a2a00'); return q; }
    var nA = num(560, na), nB = num(1360, nb), cA = num(560, meta), cB = num(1360, meta);
    var ig = w.pieza(g, 960, 560); w.txt(ig, 0, 0, '=', 200, C.sol, { filter: 'url(#brillo)' });
    var cap = d.texto ? w.chip(g, 960, 245, Math.min(1500, d.texto.length * 32 + 140), 90, d.texto, { size: 46, stroke: C.verde, r: 32 }) : null;
    var extraA = ag ? GA.O.slice(na) : GA.O.slice(meta), extraB = ag ? GB.O.slice(nb) : GB.O.slice(meta), baseA = GA.O.slice(0, ag ? na : na), baseB = GB.O.slice(0, nb);
    B(0); w.IN(tl, GA.caja, 0); w.IN(tl, GB.caja, '<'); (ag ? GA.O.slice(0, na) : GA.O).concat(ag ? GB.O.slice(0, nb) : GB.O).forEach(function (o, k) { w.IN(tl, o, k ? '<.05' : '>-.2', { scale: 0, y: 0, ease: 'back.out(2)', d: .4 }); }); w.IN(tl, nA, '>'); w.IN(tl, nB, '<');
    B(1); var cambian = extraA.concat(extraB);
    // agregar: cada objeto nuevo cae cuando la voz cuenta su número ("4, 5"); si la frase no cuenta, caen solos
    var chico = na < nb ? GA.O : GB.O, nchico = Math.min(na, nb), cayo = {};
    if (ag) g.alDecir = function (p, paso) { var v = parseInt(String(p).replace(/[^0-9]/g, ''), 10); if (paso !== 1 || !(v > nchico && v <= meta) || cayo[v]) return; cayo[v] = 1;
      gsap.fromTo(chico[v - 1], { opacity: 0, y: -400 }, { opacity: 1, y: 0, duration: .6, ease: 'bounce.out' }); };
    if (ag) tl.to({}, { duration: .01 });
    else cambian.forEach(function (o, k) { tl.to(o, { y: 500, opacity: 0, rotation: 40, duration: .5, ease: 'power2.in' }, k ? '>-.2' : '>'); });
    if (!ag) { w.OUT(tl, nA, '>'); w.OUT(tl, nB, '<'); w.IN(tl, cA, '>'); w.IN(tl, cB, '<'); }
    B(2); if (ag) { tl.set(cambian, { opacity: 1, y: 0 }, '>+0.05'); w.OUT(tl, nA, '>'); w.OUT(tl, nB, '<'); w.IN(tl, cA, '>'); w.IN(tl, cB, '<'); }
    w.IN(tl, ig, '>', { scale: 0, y: 0, ease: 'back.out(3)' }); if (cap) w.IN(tl, cap, '<.2');
  } };
  // juntar: {a:{emoji, n}, b:{emoji, n}, texto} (a + b ≤ 10) — 3 pasos: dos grupos con su número y el + · se juntan en una sola caja · el total y el texto ("3 + 2 = 5")
  T.juntar = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var na = d.a.n, nb = d.b.n, tot = na + nb;
    function grupo(e, n, cx) { var p = w.pieza(g, cx, 520); w.caja(p, 0, 0, 600, 420, 'rgba(127,211,196,.08)', C.linea, 40, 5); return { caja: p, O: coleccion(g, e, n, cx, 520, 520, 340, 140) }; }
    var GA = grupo(d.a.emoji, na, 520), GB = grupo(d.b.emoji, nb, 1400);
    function num(cx, y, v, r) { var q = w.pieza(g, cx, y); w.el('circle', { r: r || 58, fill: C.sol }, q); w.txt(q, 0, 4, String(v), (r || 58) * 1.1, '#3a2a00'); return q; }
    var nA = num(520, 800, na), nB = num(1400, 800, nb), mas = w.pieza(g, 960, 520); w.txt(mas, 0, 0, '+', 170, C.sol, { filter: 'url(#brillo)' });
    var grande = w.pieza(g, 960, 520); w.caja(grande, 0, 0, 1300, 440, 'rgba(255,214,102,.08)', C.sol, 44, 6);
    var O = GA.O.concat(GB.O), cols = tot > 5 ? Math.ceil(tot / 2) : tot, paso = Math.min(170, 1150 / cols), P = w.rejilla(tot, 960, 520, paso, paso, cols);
    var nT = num(960, 830, tot, 70), cap = d.texto ? w.chip(g, 960, 250, Math.min(1500, d.texto.length * 32 + 140), 90, d.texto, { size: 46, stroke: C.verde, r: 32 }) : null;
    B(0); w.IN(tl, GA.caja, 0); w.IN(tl, GB.caja, '<'); O.forEach(function (o, k) { w.IN(tl, o, k ? '<.05' : '>-.2', { scale: 0, y: 0, ease: 'back.out(2)', d: .4 }); }); w.IN(tl, nA, '>'); w.IN(tl, nB, '<'); w.IN(tl, mas, '<.1', { scale: 0, y: 0 });
    B(1); w.OUT(tl, GA.caja, 0); w.OUT(tl, GB.caja, '<'); w.OUT(tl, nA, '<'); w.OUT(tl, nB, '<'); w.OUT(tl, mas, '<'); w.IN(tl, grande, '>-.1', { scale: .8, y: 0 });
    O.forEach(function (o, k) { tl.to(o, { x: P[k][0] - o.px, y: P[k][1] - o.py, duration: .6, ease: 'power2.inOut' }, k ? '<.04' : '>-.3'); });
    B(2); w.IN(tl, nT, 0, { scale: .3, y: 0, ease: 'back.out(2.5)' }); if (cap) w.IN(tl, cap, '<.2');
  } };
  // agregar: {emoji, n, mas, texto} (n + mas ≤ 10) — 3 pasos: el grupo con su número · llegan los nuevos (cada uno cae cuando la voz cuenta su número: "4, 5") · el total y el texto
  T.agregar = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var n = d.n, tot = n + d.mas, caja = w.pieza(g, 960, 520); w.caja(caja, 0, 0, 1300, 440, 'rgba(127,211,196,.08)', C.linea, 44, 5);
    var O = coleccion(g, d.emoji, tot, 960, 520, 1150, 360, 160), viejos = O.slice(0, n), nuevos = O.slice(n);
    function num(v, r) { var q = w.pieza(g, 960, 830); w.el('circle', { r: r, fill: C.sol }, q); w.txt(q, 0, 4, String(v), r * 1.1, '#3a2a00'); return q; }
    var nI = num(n, 58), nT = num(tot, 70), cap = d.texto ? w.chip(g, 960, 250, Math.min(1500, d.texto.length * 32 + 140), 90, d.texto, { size: 46, stroke: C.verde, r: 32 }) : null;
    B(0); w.IN(tl, caja, 0); viejos.forEach(function (o, k) { w.IN(tl, o, k ? '<.06' : '>-.2', { scale: 0, y: 0, ease: 'back.out(2)', d: .4 }); }); w.IN(tl, nI, '>');
    var cayo = {}; g.alDecir = function (p, paso) { var v = parseInt(String(p).replace(/[^0-9]/g, ''), 10); if (paso !== 1 || !(v > n && v <= tot) || cayo[v]) return; cayo[v] = 1;
      gsap.fromTo(O[v - 1], { opacity: 0, y: -400 }, { opacity: 1, y: 0, duration: .6, ease: 'bounce.out' }); };
    B(1); tl.to({}, { duration: .01 });
    B(2); tl.set(nuevos, { opacity: 1, y: 0 }, '>+0.05'); w.OUT(tl, nI, '>'); w.IN(tl, nT, '>', { scale: .3, y: 0, ease: 'back.out(2.5)' }); if (cap) w.IN(tl, cap, '<.2');
  } };
  // sacar: {emoji, n, menos, texto} (n ≤ 10) — 3 pasos: el grupo con su número · se van los que sacamos (se tachan y salen volando) · lo que queda y el texto ("7 MENOS 3 SON 4")
  T.sacar = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var n = d.n, q = n - d.menos, caja = w.pieza(g, 960, 520); w.caja(caja, 0, 0, 1300, 440, 'rgba(127,211,196,.08)', C.linea, 44, 5);
    var O = coleccion(g, d.emoji, n, 960, 520, 1150, 360, 160), quedan = O.slice(0, q), van = O.slice(q);
    var X = van.map(function (o) { var x = w.pieza(g, o.px, o.py), s = o.paso * .36; w.el('line', { x1: -s, y1: -s, x2: s, y2: s, stroke: C.coral, 'stroke-width': 12, 'stroke-linecap': 'round' }, x); w.el('line', { x1: -s, y1: s, x2: s, y2: -s, stroke: C.coral, 'stroke-width': 12, 'stroke-linecap': 'round' }, x); return x; });
    function num(v, r) { var p = w.pieza(g, 960, 830); w.el('circle', { r: r, fill: C.sol }, p); w.txt(p, 0, 4, String(v), r * 1.1, '#3a2a00'); return p; }
    var nI = num(n, 58), nF = num(q, 70), cap = d.texto ? w.chip(g, 960, 250, Math.min(1500, d.texto.length * 32 + 140), 90, d.texto, { size: 46, stroke: C.verde, r: 32 }) : null;
    B(0); w.IN(tl, caja, 0); O.forEach(function (o, k) { w.IN(tl, o, k ? '<.06' : '>-.2', { scale: 0, y: 0, ease: 'back.out(2)', d: .4 }); }); w.IN(tl, nI, '>');
    B(1); X.forEach(function (x, k) { w.IN(tl, x, k ? '>-.1' : '>', { scale: 0, y: 0, ease: 'back.out(3)', d: .35 }); });
    van.forEach(function (o, k) { tl.to([o, X[k]], { y: -700, opacity: 0, rotation: 30, duration: .6, ease: 'power2.in' }, k ? '<.1' : '>.3'); });
    B(2); w.OUT(tl, nI, 0); w.IN(tl, nF, '>', { scale: .3, y: 0, ease: 'back.out(2.5)' }); quedan.forEach(function (o, k) { w.pop(tl, o, k ? '<.05' : '<'); }); if (cap) w.IN(tl, cap, '<.2');
  } };
  // calculadora: {teclas:['1','2','+','5'], resultado:'17', texto, titulo} — 3 pasos: aparece la calculadora · se aprietan las teclas (brillan y van a la pantalla) · se aprieta = y sale el resultado
  T.calculadora = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var cx = 700, cy = 575, F = [['7', '8', '9', '−'], ['4', '5', '6', '+'], ['1', '2', '3', '='], ['0', 'C']];
    var cuerpo = w.pieza(g, cx, cy); w.caja(cuerpo, 0, 0, 560, 760, '#24343a', C.aqua, 46, 6); w.caja(cuerpo, 0, -250, 470, 150, '#cfe8c9', '#7fa77a', 18, 5);
    var pant = w.txt(cuerpo, 205, -235, '0', 92, '#1f3a1c', { 'text-anchor': 'end', 'font-family': 'ui-monospace,Menlo,Consolas,monospace' });
    var K = {};
    F.forEach(function (fila, r) { fila.forEach(function (k, c) { var x = -165 + c * 110, y = -95 + r * 105, p = w.pieza(cuerpo, x, y);
      p.r = w.caja(p, 0, 0, 92, 86, /[0-9]/.test(k) ? '#3c5158' : (k === '=' ? C.sol : '#4f6f63'), '#0d1b1e', 18, 3); w.txt(p, 0, 4, k, 48, k === '=' ? '#3a2a00' : '#ffffff'); K[k] = p; }); });
    Object.keys(K).forEach(function (k) { K[k].setAttribute('opacity', 1); });
    var ti = d.titulo ? w.titulo(g, d.titulo, 140) : null, cap = d.texto ? w.chip(g, 1400, 575, Math.min(820, d.texto.length * 32 + 140), 100, d.texto, { size: 46, stroke: C.verde, r: 32 }) : null;
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, cuerpo, ti ? '<.1' : 0, { scale: .8, y: 0 });
    B(1); var s = '';
    d.teclas.forEach(function (k, i) { var tk = K[k === '-' ? '−' : k]; s += (/[0-9]/.test(k) ? k : ' ' + (k === '-' ? '−' : k) + ' '); var v = s.trim();
      if (tk) tl.to(tk, { scale: .85, duration: .12, yoyo: true, repeat: 1 }, i ? '>.25' : '>');
      tl.call(function () { pant.textContent = v; }, null, '<'); });
    B(2); if (K['=']) tl.to(K['='], { scale: .85, duration: .12, yoyo: true, repeat: 1 }, '>');
    tl.call(function () { pant.textContent = String(d.resultado); }, null, '>'); w.pop(tl, cuerpo, '>'); if (cap) w.IN(tl, cap, '<.2');
  } };
  function numDe(p) { var v = parseInt(String(p).replace(/[^0-9]/g, ''), 10); return isFinite(v) ? v : null; }
  // tren: {desde, hasta, paso (1 por defecto; 10 o 100 para contar de 10 en 10 o de 100 en 100), faltan:[números], titulo} (hasta 10 vagones) — 3 pasos: llega el tren · cada vagón se ilumina cuando la voz dice su número · aparecen los que faltaban
  T.tren = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var N = [], k, fmt = function (v) { return v >= 1000 ? v.toLocaleString('es-AR') : String(v); }; for (k = d.desde; k <= d.hasta; k += (d.paso || 1)) N.push(k); var falta = d.faltan || [], cant = N.length, paso = Math.min(150, 1380 / (cant + 1)), x0 = 960 - (cant * paso) / 2 + paso * .35, Y = 560;
    var ti = d.titulo ? w.titulo(g, d.titulo, 285) : null, tren = w.pieza(g, 0, 0);
    w.el('line', { x1: 140, y1: Y + 92, x2: 1780, y2: Y + 92, stroke: C.suave, 'stroke-width': 6 }, tren);
    w.emoji(tren, x0 - paso * 1.12, Y - 10, '🚂', paso * 1.0);
    var V = N.map(function (v, j) { var x = x0 + j * paso, p = w.pieza(g, x, Y), es = falta.indexOf(v) >= 0;
      p.r = w.caja(p, 0, 0, paso - 16, paso * .9, es ? 'rgba(255,255,255,.06)' : 'url(#gCard)', es ? C.coral : W.PAL[j % W.PAL.length], 18, 5);
      if (es) p.r.setAttribute('stroke-dasharray', '14 10');
      w.el('circle', { cx: -paso * .25, cy: paso * .48, r: 13, fill: '#0b1c1d', stroke: C.suave, 'stroke-width': 4 }, p); w.el('circle', { cx: paso * .25, cy: paso * .48, r: 13, fill: '#0b1c1d', stroke: C.suave, 'stroke-width': 4 }, p);
      p.q = es ? w.txt(p, 0, 4, '?', paso * .42, C.coral) : null; p.t = w.txt(p, 0, 4, fmt(v), paso * (fmt(v).length > 3 ? .26 : fmt(v).length === 3 ? .34 : .42), C.txt, es ? { opacity: 0 } : null); p.v = v; p.falta = es; return p; });
    var dicho = {}; g.alDecir = function (pal, f) { var v = numDe(pal); if (f !== 1 || v == null || dicho[v]) return; var p = V[N.indexOf(v)]; if (!p || p.falta) return; dicho[v] = 1;
      gsap.to(p.r, { attr: { stroke: C.sol, 'stroke-width': 10 }, duration: .2 }); gsap.fromTo(p, { y: 0 }, { y: -26, duration: .18, yoyo: true, repeat: 1 }); };
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, tren, ti ? '<' : 0, { x: 900, y: 0, ease: 'power3.out', d: 1 }); V.forEach(function (p, j) { w.IN(tl, p, j ? '<.06' : '<', { x: 900, y: 0, ease: 'power3.out', d: 1 }); });
    B(1); tl.to({}, { duration: .01 });
    B(2); V.forEach(function (p) { if (!p.falta) return; tl.to(p.q, { opacity: 0, duration: .2 }, '>+0.05'); tl.to(p.t, { opacity: 1, duration: .3 }, '<'); tl.to(p.r, { attr: { stroke: C.verde, 'stroke-width': 10 }, duration: .3 }, '<'); w.pop(tl, p, '<'); });
    if (!falta.length) V.forEach(function (p, j) { tl.to(p.r, { attr: { stroke: C.sol, 'stroke-width': 10 }, duration: .1 }, j ? '<' : '>+0.05'); });
  } };
  // diezymas: {emoji, n (11-20), texto:'10 y 3 son 13'} — 3 pasos: caja de 10 · los sueltos aparecen cuando la voz cuenta 11, 12… · el resultado
  T.diezymas = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var n = d.n, sueltos = n - 10, caja = w.pieza(g, 560, 520), cab = 92;
    w.caja(caja, 0, 0, 560, 300, 'rgba(244,182,63,.10)', C.sol, 34, 6);
    for (var k = 0; k < 10; k++) w.emoji(caja, (k % 5 - 2) * cab, (Math.floor(k / 5) - .5) * 110, d.emoji, 78);
    var e10 = w.pieza(g, 560, 735); w.el('circle', { r: 50, fill: C.sol }, e10); w.txt(e10, 0, 4, '10', 52, '#3a2a00');
    var cols = sueltos > 5 ? 5 : sueltos, S = [];
    var y0 = sueltos > 5 ? 440 : 500; for (k = 0; k < sueltos; k++) { var o = w.pieza(g, 1180 + (k % 5) * 105, y0 + Math.floor(k / 5) * 155); w.emoji(o, 0, 0, d.emoji, 86); S.push(o); }
    var nums = S.map(function (o, k) { var q = w.pieza(g, 1180 + (k % 5) * 105, y0 + Math.floor(k / 5) * 155 + 62); w.el('circle', { r: 24, fill: C.aqua }, q); w.txt(q, 0, 2, String(11 + k), 26, '#06282a'); return q; });
    var mas = w.pieza(g, 960, 520); w.txt(mas, 0, 0, '+', 120, C.sol, { filter: 'url(#brillo)' });
    var cap = d.texto ? w.chip(g, 960, 880, Math.min(1400, d.texto.length * 34 + 140), 104, d.texto, { size: 56, stroke: C.verde, r: 36 }) : null;
    var dicho = {}; g.alDecir = function (pal, f) { var v = numDe(pal); if (f !== 1 || v == null || v < 11 || v > n || dicho[v]) return; dicho[v] = 1;
      gsap.fromTo(S[v - 11], { opacity: 0, y: -260 }, { opacity: 1, y: 0, duration: .5, ease: 'bounce.out' }); gsap.fromTo(nums[v - 11], { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: .35, ease: 'back.out(3)', delay: .15 }); };
    B(0); w.IN(tl, caja, 0, { scale: .6, y: 0 }); w.IN(tl, e10, '>', { scale: 0, y: 0, ease: 'back.out(3)' });
    B(1); w.IN(tl, mas, 0, { scale: 0, y: 0 });
    B(2); tl.set(S.concat(nums), { opacity: 1, y: 0, scale: 1 }, '>+0.05'); if (cap) w.IN(tl, cap, '>', { scale: .6, y: 0 });
  } };
  // cdu: {c (opcional), d, u, texto, cabD, cabU} — 5 pasos (4 sin c): presentación · cajas de 100 (aparecen al decir 100, 200…) · paquetes de 10 (al decir 210, 220…) · sueltos (al decir 241, 242…) · el total
  T.cdu = { n: function (d) { return d.c == null ? 4 : 5; }, armar: function (g, tl, B, d) {
    // sin "c" (primer grado): solo bolsitas de 10 y sueltos, en dos columnas
    var sinC = d.c == null, c = sinC ? 0 : d.c;
    var TODAS = [{ x: 470, ic: 'caja', s: .82, n: c, cab: 'CENTENAS', dx: 142, dy: 112 }, { x: 960, ic: 'pack', s: .92, n: d.d, cab: d.cabD || 'DECENAS', dx: 138, dy: 74 }, { x: 1450, ic: 'alf', s: 1, n: d.u, cab: d.cabU || 'UNIDADES', dx: 104, dy: 100 }];
    var COL = sinC ? [Object.assign({}, TODAS[1], { x: 700 }), Object.assign({}, TODAS[2], { x: 1220 })] : TODAS;
    var base = sinC ? [0, d.d * 10] : [0, c * 100, c * 100 + d.d * 10], salto = sinC ? [10, 1] : [100, 10, 1], NC = COL.length;
    var cabs = COL.map(function (cl) { var p = w.pieza(g, cl.x, 300); w.caja(p, 0, 0, 330, 70, 'url(#gCard)', C.linea, 30, 4); w.txt(p, 0, 2, cl.cab, 30, C.aqua, { 'letter-spacing': 3 }); return p; });
    var obj = COL.map(function (cl) { var arr = []; for (var k = 0; k < cl.n; k++) { var cols = 3, o = w.pieza(g, cl.x + ((k % cols) - 1) * cl.dx, 420 + Math.floor(k / cols) * cl.dy); w.usar(o, cl.ic, cl.s); arr.push(o); } return arr; });
    var cnt = COL.map(function (cl) { var p = w.pieza(g, cl.x, 800); w.el('circle', { r: 46, fill: C.sol }, p); w.txt(p, 0, 4, String(cl.n), 50, '#3a2a00'); return p; });
    var fin = d.texto ? w.chip(g, 960, 905, Math.min(1500, d.texto.length * 34 + 140), 100, d.texto, { size: 54, stroke: C.verde, r: 34 }) : null;
    var visto = {}; g.alDecir = function (pal, f) { var j = f - 1; if (j < 0 || j > NC - 1) return; var v = parseInt(String(pal).replace(/[^0-9]/g, ''), 10); if (!isFinite(v)) return;
      var k = (v - base[j]) / salto[j]; if (k !== Math.floor(k) || k < 1 || k > COL[j].n || visto[j + ':' + k]) return; visto[j + ':' + k] = 1;
      gsap.fromTo(obj[j][k - 1], { opacity: 0, y: -300, scale: .5 }, { opacity: 1, y: 0, scale: 1, duration: .55, ease: 'bounce.out' }); };
    B(0); cabs.forEach(function (cb, k) { w.IN(tl, cb, k ? '<.15' : 0); });
    for (var f = 1; f <= NC; f++) { B(f); if (f > 1) { tl.set(obj[f - 2], { opacity: 1, y: 0, scale: 1 }, '>+0.05'); w.IN(tl, cnt[f - 2], '>', { scale: 0, y: 0, ease: 'back.out(3)' }); } else tl.to({}, { duration: .01 }); }
    B(NC + 1); tl.set(obj[NC - 1], { opacity: 1, y: 0, scale: 1 }, '>+0.05'); w.IN(tl, cnt[NC - 1], '>', { scale: 0, y: 0, ease: 'back.out(3)' }); if (fin) w.IN(tl, fin, '>', { scale: .6, y: 0 });
  } };
  // cuadro: {hasta (10-100), desde (0 o 1, por defecto 1), faltan:[números], titulo} — cuadro de números de a 10 por fila (con desde 0, los redondos 10, 20, 30… quedan a la izquierda). 3 pasos: aparece el cuadro · cada número se ilumina cuando la voz lo dice · aparecen los que faltaban
  T.cuadro = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var n = d.hasta, d0 = d.desde === 0 ? 0 : 1, filas = Math.ceil((n - d0 + 1) / 10), cw = 142, ch = Math.min(108, 610 / filas), x0 = 960 - 4.5 * cw, y0 = (filas > 6 ? 625 : 560) - (filas - 1) * ch / 2 + (d.titulo && filas <= 6 ? 25 : 0), falta = d.faltan || [], fs = Math.min(ch * .6, 46);
    var ti = d.titulo ? w.titulo(g, d.titulo, filas > 6 ? 258 : 262) : null, C2 = [];
    for (var v = d0; v <= n; v++) { var k = v - d0, p = w.pieza(g, x0 + (k % 10) * cw, y0 + Math.floor(k / 10) * ch), es = falta.indexOf(v) >= 0;
      p.r = w.caja(p, 0, 0, cw - 12, ch - 12, es ? 'rgba(255,255,255,.05)' : 'url(#gCard)', es ? C.coral : C.linea, 16, 4); if (es) p.r.setAttribute('stroke-dasharray', '12 8');
      p.q = es ? w.txt(p, 0, 3, '?', fs, C.coral) : null; p.t = w.txt(p, 0, 3, String(v), fs, C.txt, es ? { opacity: 0 } : null); p.falta = es; C2.push(p); }
    var dicho = {}; g.alDecir = function (pal, f) { var v = parseInt(String(pal).replace(/[^0-9]/g, ''), 10); if (f !== 1 || !(v >= d0 && v <= n) || dicho[v]) return; var p = C2[v - d0]; if (p.falta) return; dicho[v] = 1;
      gsap.to(p.r, { attr: { stroke: C.sol, 'stroke-width': 9, fill: 'rgba(244,182,63,.25)' }, duration: .2 }); gsap.fromTo(p, { scale: 1 }, { scale: 1.18, duration: .18, yoyo: true, repeat: 1 }); };
    B(0); if (ti) w.IN(tl, ti, 0); C2.forEach(function (p, k) { w.IN(tl, p, k ? '<.012' : (ti ? '<.2' : 0), { scale: .4, y: 0, d: .35 }); });
    B(1); tl.to({}, { duration: .01 });
    B(2); C2.forEach(function (p) { if (!p.falta) return; tl.to(p.q, { opacity: 0, duration: .2 }, '>+0.05'); tl.to(p.t, { opacity: 1, duration: .3 }, '<'); tl.to(p.r, { attr: { stroke: C.verde, 'stroke-width': 9 }, duration: .3 }, '<'); w.pop(tl, p, '<'); });
    if (!falta.length) tl.to({}, { duration: .01 }, '>+0.05');
  } };
})();
