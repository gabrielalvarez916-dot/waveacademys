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
      var tw = String(m.txt).length * 19 + 50; w.caja(p, 0, -90, tw, 70, 'rgba(6,20,22,.88)', col, 30, 4); w.txt(p, 0, -90, m.txt, 34, '#fff'); return p; });
    B(0); w.IN(tl, eje, 0, { scaleX: 0, y: 0, ease: 'power2.out' });
    M.forEach(function (p, k) { B(k + 1); w.IN(tl, p, 0, { y: -200, ease: 'bounce.out', d: .7 }); });
  } };

  // cuenta: {filas:['4.205','1.380'], op:'+', resultado:'5.585'} — 2 pasos: la cuenta, el resultado
  T.cuenta = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var p = w.pieza(g, 960, 560), n = d.filas.length, xr = 230, h = 130;
    d.filas.forEach(function (f, k) { w.txt(p, xr, (k - n / 2) * h, f, 120, C.txt, { 'text-anchor': 'end', 'font-family': 'ui-monospace,Menlo,Consolas,monospace' }); });
    w.txt(p, -330, (n - 1 - n / 2) * h, d.op || '+', 110, C.sol); var yl = (n - n / 2) * h - 55; w.el('line', { x1: -360, y1: yl, x2: xr + 20, y2: yl, stroke: C.sol, 'stroke-width': 8 }, p);
    var r = w.pieza(g, 960, 560); var rt = w.txt(r, xr, yl + 85, d.resultado, 120, C.verde, { 'text-anchor': 'end', 'font-family': 'ui-monospace,Menlo,Consolas,monospace', filter: 'url(#brillo)' });
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
    var E = d.pasos.map(function (s, k) { var p = w.pieza(g, 960, 420); w.txt(p, 0, 0, s, 120, k === d.pasos.length - 1 ? C.verde : C.txt); if (d.notas && d.notas[k]) w.txt(p, 0, 110, d.notas[k], 40, C.sol); return p; });
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
})();
