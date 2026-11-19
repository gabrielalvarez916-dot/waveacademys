/* MOTOR DE CLASES ANIMADAS DE WAVE ACADEMY — base: herramientas de dibujo + reproductor.
   La clase viene en window.CLASE = { titulo, sub, escenas: [ { t: 'plantilla', voz: [frases], ...datos } ] }.
   Cada plantilla (T.nombre) dice cuántos pasos tiene (n) y cómo se arma (armar). Cada paso arranca con su frase.
   El audio de cada frase viene en window.VOZ_AUDIO (lo graba GitHub). ZONA SEGURA: x 160–1760, y 230–980. */
var W = (function () {
  var NS = 'http://www.w3.org/2000/svg', $ = function (id) { return document.getElementById(id); };
  var C = { aqua: '#7FD3C4', sol: '#F4B63F', coral: '#ff7a66', verde: '#8be38f', lila: '#b9a6ff', azul: '#7fb6ff', rosa: '#ff9fcf', txt: '#eaf7f4', suave: '#9dbdb9', linea: '#2c5a5e' };
  var PAL = [C.aqua, C.sol, C.coral, C.lila, C.verde, C.azul, C.rosa];
  var EMO = '"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif';
  function el(tag, at, p) { var e = document.createElementNS(NS, tag); for (var k in at) if (at[k] != null) e.setAttribute(k, at[k]); if (p) p.appendChild(e); return e; }
  function txt(p, x, y, s, size, fill, extra) { var t = el('text', Object.assign({ x: x, y: y, 'text-anchor': 'middle', 'dominant-baseline': 'central', 'font-size': size, fill: fill || C.txt }, extra || {}), p); t.textContent = s; return t; }
  function multi(p, x, y, s, size, fill, ancho, extra) { // texto en varias líneas (corta por palabras)
    var max = Math.max(8, Math.floor((ancho || 1200) / (size * .52))), w = String(s).split(' '), L = [], cur = '';
    w.forEach(function (x2) { if ((cur + ' ' + x2).trim().length > max) { L.push(cur.trim()); cur = x2; } else cur += ' ' + x2; }); if (cur.trim()) L.push(cur.trim());
    var g = el('g', {}, p); L.forEach(function (l, i) { txt(g, x, y + (i - (L.length - 1) / 2) * size * 1.22, l, size, fill, extra); }); g.lineas = L.length; return g;
  }
  function emoji(p, x, y, e, size) { return txt(p, x, y, e, size, '#fff', { 'font-family': EMO, 'font-weight': 400 }); }
  function caja(p, x, y, w, h, fill, stroke, r, sw) { return el('rect', { x: x - w / 2, y: y - h / 2, width: w, height: h, rx: r == null ? 24 : r, fill: fill || 'url(#gCard)', stroke: stroke || C.linea, 'stroke-width': sw || 4 }, p); }
  function pieza(p, x, y) { var w = el('g', { transform: 'translate(' + x + ' ' + y + ')' }, p); return el('g', { 'data-c': 1, opacity: 0 }, w); }
  function mover(g, x, y) { g.parentNode.setAttribute('transform', 'translate(' + x + ' ' + y + ')'); }
  function usar(p, id, s) { return el('use', { href: '#' + id, transform: s ? 'scale(' + s + ')' : null }, p); }
  function tarjeta(p, x, y, w, h, color, sombra) { var r = caja(p, x, y, w, h, 'url(#gCard)', color || C.linea, 30, 5); if (sombra !== false) r.setAttribute('filter', 'url(#sombra)'); return r; }
  function chip(p, x, y, w, h, s, o) { o = o || {}; var g = pieza(p, x, y); var r = caja(g, 0, 0, w, h, o.fill || 'url(#gCard)', o.stroke || C.linea, o.r == null ? h / 2 : o.r, o.sw || 4); r.setAttribute('filter', 'url(#sombra)'); g.r = r; g.t = txt(g, 0, 2, s, o.size || 44, o.color || C.txt, o.ls ? { 'letter-spacing': o.ls } : null); return g; }
  function etiqueta(p, x, y, s) { return chip(p, x, y, Math.max(260, String(s).length * 24 + 80), 70, s, { fill: 'url(#gSol)', stroke: '#ffe7a8', color: '#3a2a00', size: 32, ls: 3 }); }
  function titulo(p, s, y) { return chip(p, 960, y || 280, Math.min(1500, Math.max(420, String(s).length * 28 + 110)), 84, s, { fill: 'url(#gAqua)', stroke: '#d8fff7', color: '#06282a', size: 36, ls: 4 }); }
  function flecha(p, x1, y1, x2, y2, color, ancho) { var g = el('g', {}, p), a = Math.atan2(y2 - y1, x2 - x1), L = Math.hypot(x2 - x1, y2 - y1);
    var l = el('line', { x1: x1, y1: y1, x2: x2 - Math.cos(a) * 18, y2: y2 - Math.sin(a) * 18, stroke: color || C.sol, 'stroke-width': ancho || 8, 'stroke-linecap': 'round', 'stroke-dasharray': L, 'stroke-dashoffset': L }, g);
    var pu = el('path', { d: 'M0 0 L-26 -14 L-26 14 Z', fill: color || C.sol, transform: 'translate(' + x2 + ' ' + y2 + ') rotate(' + a * 180 / Math.PI + ')', opacity: 0 }, g); g.l = l; g.pu = pu; return g; }
  function dibujarFlecha(tl, f, pos) { if (pos === 0) pos = '>'; tl.to(f.l, { attr: { 'stroke-dashoffset': 0 }, duration: .45, ease: 'power2.inOut' }, pos); return tl.to(f.pu, { opacity: 1, duration: .15 }, '>-.1'); }
  // ---- animaciones (suaves, profesionales). pos 0 = al arrancar el paso ----
  function IN(tl, g, pos, f) { f = f || {}; if (pos === 0) pos = '>'; var fr = Object.assign({ opacity: 0, y: 40, scale: .92 }, f); delete fr.d; delete fr.ease; return tl.fromTo(g, fr, { opacity: 1, y: 0, x: 0, scale: 1, rotation: 0, duration: f.d || .6, ease: f.ease || 'back.out(1.5)' }, pos); }
  function OUT(tl, g, pos, f) { if (pos === 0) pos = '>'; return tl.to(g, Object.assign({ opacity: 0, scale: .9, duration: .35, ease: 'power2.in' }, f || {}), pos); }
  function pop(tl, g, pos) { if (pos === 0) pos = '>'; return tl.to(g, { scale: 1.12, duration: .18, yoyo: true, repeat: 1, ease: 'power2.out' }, pos); }
  function brillar(tl, r, color, pos) { if (pos === 0) pos = '>'; return tl.to(r, { attr: { stroke: color || C.sol, 'stroke-width': 10 }, duration: .3 }, pos); }
  function contador(tl, t, desde, hasta, pos, dur, fmt) { var o = { v: desde }; fmt = fmt || function (v) { return Math.round(v).toLocaleString('es-AR'); }; return tl.to(o, { v: hasta, duration: dur || 1, ease: 'power2.inOut', onUpdate: function () { t.textContent = fmt(o.v); } }, pos); }
  function temblar(tl, g, pos) { if (pos === 0) pos = '>'; return tl.to(g, { rotation: 8, duration: .08, yoyo: true, repeat: 7 }, pos); }
  function sacudir(tl, pos) { tl.fromTo('#flash', { opacity: .45 }, { opacity: 0, duration: .5, immediateRender: false }, pos); tl.to('#cam', { x: 18, duration: .05, repeat: 7, yoyo: true }, '<'); return tl.set('#cam', { x: 0 }); }
  function fila(p, cx, y, cab, dig, w, vy) { // estante de lugares (casilleros con encabezado, cifra y valor)
    w = w || 190; var gap = 26, n = cab.length, x0 = cx - ((n - 1) * (w + gap)) / 2, R = { slots: [], digs: [], vals: [], cabs: [], xs: [] };
    cab.forEach(function (c, k) {
      var x = x0 + k * (w + gap); R.xs.push(x);
      var hc = pieza(p, x, y - 150); txt(hc, 0, 0, c, w < 180 ? 19 : 24, C.aqua, { 'letter-spacing': 2 }); R.cabs.push(hc);
      var s = pieza(p, x, y); s.r = caja(s, 0, 0, w, 220, 'url(#gCard)', C.linea, 28, 6); R.slots.push(s);
      var d = pieza(p, x, y); d.t = txt(d, 0, 6, dig[k], 170, C.txt); R.digs.push(d);
      var v = pieza(p, x, y + (vy || 160)); v.t = txt(v, 0, 0, '', 50, C.sol); R.vals.push(v);
    });
    return R;
  }
  function rejilla(n, cx, cy, w, h, cols) { cols = cols || Math.min(n, n <= 3 ? n : n === 4 ? 2 : 3); var rows = Math.ceil(n / cols), P = []; for (var i = 0; i < n; i++) { var c = i % cols, r = Math.floor(i / cols), enFila = Math.min(cols, n - r * cols); P.push([cx + (c - (enFila - 1) / 2) * w, cy + (r - (rows - 1) / 2) * h]); } return P; }
  return { NS: NS, $: $, C: C, PAL: PAL, el: el, txt: txt, multi: multi, emoji: emoji, caja: caja, pieza: pieza, mover: mover, usar: usar, tarjeta: tarjeta, chip: chip, etiqueta: etiqueta, titulo: titulo, flecha: flecha, dibujarFlecha: dibujarFlecha,
    IN: IN, OUT: OUT, pop: pop, brillar: brillar, contador: contador, temblar: temblar, sacudir: sacudir, fila: fila, rejilla: rejilla };
})();
var T = {}; // banco de plantillas: T.nombre = { n: function (d) { return pasos }, armar: function (g, tl, B, d) {} }
