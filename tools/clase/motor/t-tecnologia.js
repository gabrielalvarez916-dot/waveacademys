/* PLANTILLAS · TECNOLOGÍA (diagramas de bloques con flujos y vistas de una pieza) */
(function () {
  var w = W, C = w.C;

  // sistema: diagrama de bloques de un proceso con tres tipos de flujo (materia, energía, información).
  // {titulo, proceso:{txt, emoji}, entradas:[{tipo:'materia'|'energia'|'info', txt}] (1-4), salidas:[{tipo, txt}] (1-4)}
  // Pasos: 1 (el proceso) + entradas + salidas, en ese orden (cada flecha entra con su frase).
  var TIPOS = { materia: { col: C.sol, nom: 'Materia' }, energia: { col: C.coral, nom: 'Energía' }, info: { col: C.azul, nom: 'Información' } };
  T.sistema = { n: function (d) { return 1 + d.entradas.length + d.salidas.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), cx = 960, cy = 610;
    var bloque = w.pieza(g, cx, cy); w.caja(bloque, 0, 0, 440, 280, 'url(#gCard)', C.aqua, 36, 8).setAttribute('filter', 'url(#sombra)');
    if (d.proceso.emoji) w.emoji(bloque, 0, -62, d.proceso.emoji, 90);
    w.multi(bloque, 0, d.proceso.emoji ? 60 : 0, d.proceso.txt, 38, C.txt, 400);
    var lg = w.pieza(g, cx, 895); // leyenda de colores
    Object.keys(TIPOS).forEach(function (k, i) { var x = (i - 1) * 380; w.el('circle', { cx: x - 110, cy: 0, r: 13, fill: TIPOS[k].col }, lg); w.txt(lg, x - 85, 2, TIPOS[k].nom, 30, C.suave, { 'text-anchor': 'start' }); });
    function lado(lista, xc, entra) {
      var n = lista.length, gap = Math.min(150, 560 / n), tw = 360, th = 104;
      return lista.map(function (it, k) {
        var tp = TIPOS[it.tipo] || TIPOS.materia, y = cy + (k - (n - 1) / 2) * gap;
        var p = w.pieza(g, xc, y); w.tarjeta(p, 0, 0, tw, th, tp.col); w.multi(p, 0, 0, it.txt, 30, C.txt, tw - 34);
        var x1 = entra ? xc + tw / 2 + 8 : cx + 228, x2 = entra ? cx - 228 : xc - tw / 2 - 8;
        var f = w.flecha(g, x1, y + (entra ? 0 : 0), x2, cy + (y - cy) * .35, tp.col, 9);
        return { p: p, f: f };
      });
    }
    var E = lado(d.entradas, 330, true), S = lado(d.salidas, 1590, false);
    B(0); w.IN(tl, ti, 0); w.IN(tl, bloque, '<.15', { scale: .8, y: 0 }); w.IN(tl, lg, '>-.1', { y: 20 });
    var k = 1;
    E.forEach(function (o) { B(k++); w.IN(tl, o.p, 0, { x: -60, y: 0 }); w.dibujarFlecha(tl, o.f, '>-.1'); });
    S.forEach(function (o) { B(k++); w.dibujarFlecha(tl, o.f, 0); w.IN(tl, o.p, '>-.2', { x: 60, y: 0 }); });
  } };

  // vistas: una pieza hecha de cubos, en perspectiva y en sus tres vistas (frente, superior, lateral).
  // {titulo, cubos:[[x,y,z],...]} (x a la derecha, y hacia el observador, z hacia arriba; máx. 4×4×4). 4 pasos: perspectiva, frente, superior, lateral.
  T.vistas = { n: function () { return 4; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), K = {}, mx = 0, my = 0, mz = 0;
    d.cubos.forEach(function (c) { K[c.join()] = 1; mx = Math.max(mx, c[0]); my = Math.max(my, c[1]); mz = Math.max(mz, c[2]); });
    var has = function (x, y, z) { return !!K[[x, y, z].join()]; };
    var s = 74, cs = Math.cos(Math.PI / 6) * s, sn = Math.sin(Math.PI / 6) * s;
    function P(x, y, z) { return [(x - y) * cs, (x + y) * sn - z * s]; }
    function pts(a) { return a.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' '); }
    var iso = w.pieza(g, 520, 640), caras = { frente: [], superior: [], lateral: [] };
    var ord = d.cubos.slice().sort(function (a, b) { return (a[0] + a[1]) - (b[0] + b[1]) || a[2] - b[2]; });
    var X = [], Y = []; [[0, 0, 0], [mx + 1, 0, 0], [0, my + 1, 0], [mx + 1, my + 1, 0], [0, 0, mz + 1], [mx + 1, 0, mz + 1], [0, my + 1, mz + 1], [mx + 1, my + 1, mz + 1]].forEach(function (q) { var r = P(q[0], q[1], q[2]); X.push(r[0]); Y.push(r[1]); });
    var dx = -(Math.min.apply(null, X) + Math.max.apply(null, X)) / 2, dy = -(Math.min.apply(null, Y) + Math.max.apply(null, Y)) / 2;
    var og = w.el('g', { transform: 'translate(' + dx + ' ' + dy + ')' }, iso);
    function cara(arr, clave, base) { var pl = w.el('polygon', { points: pts(arr), fill: base, stroke: '#0b1c1d', 'stroke-width': 3, 'stroke-linejoin': 'round' }, og); caras[clave].push(pl); }
    ord.forEach(function (c) { var x = c[0], y = c[1], z = c[2];
      if (!has(x, y, z + 1)) cara([P(x, y, z + 1), P(x + 1, y, z + 1), P(x + 1, y + 1, z + 1), P(x, y + 1, z + 1)], 'superior', '#d9ece9');
      if (!has(x, y + 1, z)) cara([P(x, y + 1, z), P(x + 1, y + 1, z), P(x + 1, y + 1, z + 1), P(x, y + 1, z + 1)], 'frente', '#a9cfca');
      if (!has(x + 1, y, z)) cara([P(x + 1, y, z), P(x + 1, y + 1, z), P(x + 1, y + 1, z + 1), P(x + 1, y, z + 1)], 'lateral', '#79aaa5'); });
    var u = 66;
    function vista(cx, cy, celdas, W_, H_, nombre) {
      var p = w.pieza(g, cx, cy), ox = -W_ * u / 2, oy = -H_ * u / 2;
      w.caja(p, 0, 0, W_ * u + 60, H_ * u + 120, 'url(#gCard)', C.linea, 24, 4);
      celdas.forEach(function (q) { w.el('rect', { x: ox + q[0] * u, y: oy + q[1] * u - 10, width: u, height: u, fill: '#a9cfca', stroke: '#0b1c1d', 'stroke-width': 3 }, p); });
      w.txt(p, 0, H_ * u / 2 + 38, nombre, 30, C.sol, { 'letter-spacing': 2 });
      return p;
    }
    function celdas(fx) { var S = {}; d.cubos.forEach(function (c) { var q = fx(c); S[q.join()] = q; }); return Object.keys(S).map(function (k) { return S[k]; }); }
    var VF = vista(1180, 510, celdas(function (c) { return [c[0], mz - c[2]]; }), mx + 1, mz + 1, 'FRENTE');
    var VS = vista(1180, 812, celdas(function (c) { return [c[0], c[1]]; }), mx + 1, my + 1, 'SUPERIOR');
    var VL = vista(1560, 510, celdas(function (c) { return [my - c[1], mz - c[2]]; }), my + 1, mz + 1, 'LATERAL');
    var COL = { frente: C.coral, superior: C.verde, lateral: C.azul };
    function resaltar(clave, pos) { caras[clave].forEach(function (pl) { tl.to(pl, { attr: { fill: COL[clave] }, duration: .35 }, pos); }); }
    B(0); w.IN(tl, ti, 0); w.IN(tl, iso, '<.1', { scale: .85, y: 0 });
    B(1); resaltar('frente', 0); w.IN(tl, VF, '<', { x: 60, y: 0 });
    B(2); resaltar('superior', 0); w.IN(tl, VS, '<', { y: 60 });
    B(3); resaltar('lateral', 0); w.IN(tl, VL, '<', { x: 60, y: 0 });
  } };
})();
