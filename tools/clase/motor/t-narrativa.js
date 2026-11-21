/* PLANTILLAS · NARRATIVA Y COMPARAR (sirven para todas las materias) */
(function () {
  var w = W, C = w.C;

  // gancho: {grande:'2' | emoji, final:'200' (opcional), titulo, sub} — 3 pasos: aparece, se transforma, título
  T.gancho = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var largo = Math.max(String(d.grande || '').length, d.emoji ? 0 : String(d.final || '').length), a = w.pieza(g, 960, 600), t = d.emoji ? w.emoji(a, 0, 0, d.emoji, 340) : w.txt(a, 0, 0, d.grande, Math.min(420, Math.floor(1500 / (largo * .6))), C.txt, { filter: 'url(#brillo)' });
    var tt = w.pieza(g, 960, 600); w.tarjeta(tt, 0, 0, 1200, 260, C.aqua); w.txt(tt, 0, -45, d.titulo, 70, C.txt); if (d.sub) w.txt(tt, 0, 50, d.sub, 42, C.aqua);
    B(0); w.IN(tl, a, 0, { scale: 0, rotation: -20, y: 0, d: 1, ease: 'elastic.out(1,.55)' });
    B(1); w.temblar(tl, a, 0);
    var nf = Number(String(d.final || '').replace(/\./g, '')), ni = Number(String(d.grande || '').replace(/\./g, ''));
    if (d.final && isFinite(nf) && isFinite(ni) && !d.emoji) { w.contador(tl, t, ni, nf, '>', 1.1); tl.to(t, { attr: { fill: C.sol }, duration: .4 }, '<.5').to(a, { scale: .8, duration: .4 }, '<'); }
    else if (d.final) { tl.to(a, { scaleX: 0, duration: .2 }); tl.call(function () { t.textContent = d.final; }); tl.to(a, { scaleX: 1, duration: .25, ease: 'back.out(2)' }); }
    else tl.to(a, { scale: 1.15, y: -30, duration: .5, ease: 'power2.out' });
    B(2); w.OUT(tl, a, 0, { scale: 1.6 }); w.IN(tl, tt, '<.2', { scale: .6, y: 0 });
  } };

  // ---- GANCHOS VARIADOS (todos terminan con la tarjeta del título) ----
  function tarjetaTitulo(g, d) { var tt = w.pieza(g, 960, 600); w.tarjeta(tt, 0, 0, 1200, 260, C.aqua); w.txt(tt, 0, -45, d.titulo, 70, C.txt); if (d.sub) w.txt(tt, 0, 50, d.sub, 42, C.aqua); return tt; }

  // historia: {personaje:{nombre, emoji}, lugar: emoji (opcional), lineas:['Juan fue al kiosco…', ...] (1-3), titulo, sub} — lineas + 1 pasos
  T.historia = { n: function (d) { return d.lineas.length + 1; }, armar: function (g, tl, B, d) {
    var pj = w.pieza(g, 450, 600); if (d.lugar) w.emoji(pj, 120, -170, d.lugar, 130); w.emoji(pj, 0, 0, d.personaje.emoji, 300);
    w.caja(pj, 0, 230, Math.max(220, d.personaje.nombre.length * 34 + 80), 76, 'url(#gSol)', '#ffe7a8', 38, 4); w.txt(pj, 0, 230, d.personaje.nombre, 40, '#3a2a00');
    var n = d.lineas.length, L = d.lineas.map(function (s, k) { var p = w.pieza(g, 1240, 600 + (k - (n - 1) / 2) * 200); w.caja(p, 0, 0, 900, 170, 'url(#gCard)', W.PAL[(k + 1) % W.PAL.length], 30, 5).setAttribute('filter', 'url(#sombra)'); w.multi(p, 0, 0, s, 44, C.txt, 820); return p; });
    var tt = tarjetaTitulo(g, d);
    L.forEach(function (p, k) { B(k); if (!k) w.IN(tl, pj, 0, { x: -300, y: 0, ease: 'back.out(1.6)', d: .7 }); w.IN(tl, p, k ? 0 : '<.3', { x: 120, y: 0 }); if (k === n - 1) w.temblar(tl, pj, '>'); });
    B(n); w.OUT(tl, [pj].concat(L), 0, { scale: .8 }); w.IN(tl, tt, '>-.1', { scale: .6, y: 0 });
  } };

  // chat: {contacto:{nombre, emoji}, mensajes:[{yo: true|false, txt}] (2-5), titulo, sub} — mensajes + 1 pasos (un chat de celular)
  T.chat = { n: function (d) { return d.mensajes.length + 1; }, armar: function (g, tl, B, d) {
    var tel = w.pieza(g, 960, 610); w.caja(tel, 0, 0, 760, 760, '#0b1f21', C.linea, 56, 8); w.caja(tel, 0, -320, 760, 120, '#14403f', 'none', 50, 0);
    w.emoji(tel, -300, -320, d.contacto.emoji, 64); w.txt(tel, -240, -320, d.contacto.nombre, 40, C.txt, { 'text-anchor': 'start' }); w.txt(tel, 300, -320, '💬', 40, C.txt);
    var n = d.mensajes.length, h = Math.min(140, 560 / n), M = d.mensajes.map(function (m, k) { var ww = Math.min(560, Math.max(220, m.txt.length * 22 + 70)), x = m.yo ? 340 - ww / 2 : -340 + ww / 2;
      var p = w.pieza(g, 960 + x, 370 + h / 2 + k * h); w.caja(p, 0, 0, ww, h - 26, m.yo ? '#1f6b52' : '#22393b', 'none', 28, 0); w.multi(p, 0, 0, m.txt, 32, '#fff', ww - 50); return p; });
    var tt = tarjetaTitulo(g, d);
    M.forEach(function (p, k) { B(k); if (!k) w.IN(tl, tel, 0, { y: 300, ease: 'back.out(1.4)', d: .6 }); w.IN(tl, p, k ? 0 : '>-.1', { scale: .5, y: 20, ease: 'back.out(2.5)' }); });
    B(n); w.OUT(tl, [tel].concat(M), 0, { y: 200 }); w.IN(tl, tt, '>-.1', { scale: .6, y: 0 });
  } };

  // noticia: {cinta:'ÚLTIMO MOMENTO', titular, bajada, emoji, titulo, sub} — 3 pasos (placa de noticiero)
  T.noticia = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var ci = w.pieza(g, 960, 330); w.caja(ci, 0, 0, 1500, 110, C.coral, '#ffd2c9', 14, 4); w.txt(ci, 0, 0, '🔴 ' + (d.cinta || 'ÚLTIMO MOMENTO'), 52, '#fff', { 'letter-spacing': 6 });
    var e = w.pieza(g, 960, 540); w.emoji(e, 0, 0, d.emoji || '📰', 200);
    var tit = w.pieza(g, 960, 790); w.caja(tit, 0, 0, 1600, 190, 'rgba(6,20,22,.92)', C.sol, 18, 5); w.multi(tit, 0, d.bajada ? -28 : 0, d.titular, 54, C.txt, 1500); if (d.bajada) w.txt(tit, 0, 58, d.bajada, 34, C.sol);
    var tt = tarjetaTitulo(g, d);
    B(0); w.IN(tl, ci, 0, { scaleX: 0, y: 0, ease: 'power3.out' }); w.IN(tl, e, '<.2', { scale: 0, y: 0, ease: 'back.out(2)' }); tl.to(ci, { opacity: .6, duration: .25, yoyo: true, repeat: 3 }, '>');
    B(1); w.IN(tl, tit, 0, { y: 120 }); w.pop(tl, e, '>');
    B(2); w.OUT(tl, [ci, e, tit], 0, { scale: .8 }); w.IN(tl, tt, '>-.1', { scale: .6, y: 0 });
  } };

  // reto: {texto, segundos: 5, respuesta, emoji, titulo, sub} — 3 pasos: el desafío con cuenta regresiva, la respuesta, el título
  T.reto = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var tx = w.pieza(g, 960, 400); w.multi(tx, 0, 0, d.texto, 60, C.txt, 1500);
    var s = d.segundos || 5, re = w.pieza(g, 960, 720), cir = w.el('circle', { r: 130, fill: 'none', stroke: C.sol, 'stroke-width': 16, 'stroke-dasharray': 817, 'stroke-dashoffset': 0, transform: 'rotate(-90)' }, re);
    var num = w.txt(re, 0, 0, String(s), 130, C.sol);
    var rs = w.pieza(g, 960, 720); w.caja(rs, 0, 0, Math.min(1500, Math.max(500, String(d.respuesta).length * 40 + 140)), 180, 'url(#gCard)', C.verde, 40, 6); w.txt(rs, 0, 0, (d.emoji ? d.emoji + ' ' : '') + d.respuesta, 64, C.verde, { filter: 'url(#brillo)' });
    var tt = tarjetaTitulo(g, d);
    B(0); w.IN(tl, tx, 0, { y: -60 }); w.IN(tl, re, '<.2', { scale: 0, y: 0, ease: 'back.out(2)' }); tl.to(cir, { attr: { 'stroke-dashoffset': 817 }, duration: s, ease: 'none' }, '>');
    w.contador(tl, num, s, 0, '<', s);
    B(1); w.OUT(tl, re, 0, { scale: 0 }); w.IN(tl, rs, '>', { scale: .4, y: 0, ease: 'back.out(2)' }); w.sacudir(tl, '<.2');
    B(2); w.OUT(tl, [tx, rs], 0, { scale: .8 }); w.IN(tl, tt, '>-.1', { scale: .6, y: 0 });
  } };

  // portada: {texto, sub, emoji} — 1 paso
  T.portada = { n: function () { return 1; }, armar: function (g, tl, B, d) {
    var e = d.emoji ? w.pieza(g, 960, 470) : null; if (e) w.emoji(e, 0, 0, d.emoji, 200);
    var t = w.pieza(g, 960, d.emoji ? 700 : 600); w.multi(t, 0, 0, d.texto, 80, C.txt, 1400); if (d.sub) w.txt(t, 0, 110, d.sub, 42, C.aqua);
    B(0); if (e) w.IN(tl, e, 0, { scale: 0, y: 0, ease: 'back.out(2.5)' }); w.IN(tl, t, e ? '<.2' : 0);
  } };

  // definicion: {palabra, texto, emoji} — 2 pasos: la palabra, la explicación
  T.definicion = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var e = d.emoji ? w.pieza(g, 960, 380) : null; if (e) w.emoji(e, 0, 0, d.emoji, 150);
    var p = w.chip(g, 960, d.emoji ? 540 : 440, Math.max(420, d.palabra.length * 40 + 120), 120, d.palabra, { fill: 'url(#gSol)', stroke: '#ffe7a8', color: '#3a2a00', size: 64 });
    var tx = w.pieza(g, 960, 780); w.tarjeta(tx, 0, 0, 1400, 220, C.linea); w.multi(tx, 0, 0, d.texto, 46, C.txt, 1250);
    B(0); if (e) w.IN(tl, e, 0, { scale: 0, y: 0, ease: 'back.out(2.5)' }); w.IN(tl, p, e ? '<.15' : 0, { scale: .5, y: 0 });
    B(1); w.IN(tl, tx, 0);
  } };

  // dato: {numero: 7000000, antes:'', despues:'', texto, emoji} — 2 pasos: cuenta, explicación
  T.dato = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var e = d.emoji ? w.pieza(g, 960, 360) : null; if (e) w.emoji(e, 0, 0, d.emoji, 140);
    var largo = ((d.antes || '') + Math.round(d.numero).toLocaleString('es-AR') + (d.despues || '')).length, n = w.pieza(g, 960, 570), t = w.txt(n, 0, 0, '0', Math.min(190, Math.floor(1500 / (largo * .58))), C.sol, { filter: 'url(#brillo)' });
    var tx = w.pieza(g, 960, 820); w.multi(tx, 0, 0, d.texto, 48, C.txt, 1400);
    var fmt = function (v) { return (d.antes || '') + Math.round(v).toLocaleString('es-AR') + (d.despues || ''); };
    B(0); if (e) w.IN(tl, e, 0, { scale: 0, y: 0 }); w.IN(tl, n, '<'); w.contador(tl, t, 0, d.numero, '<', 1.4, fmt);
    B(1); w.IN(tl, tx, 0);
  } };

  // frase: {texto, emoji, color} — 1 paso (una idea fuerte en pantalla)
  T.frase = { n: function () { return 1; }, armar: function (g, tl, B, d) {
    var e = d.emoji ? w.pieza(g, 960, 420) : null; if (e) w.emoji(e, 0, 0, d.emoji, 170);
    var t = w.pieza(g, 960, d.emoji ? 700 : 600); w.multi(t, 0, 0, d.texto, 70, d.color || C.txt, 1400);
    B(0); if (e) w.IN(tl, e, 0, { scale: 0, y: 0, ease: 'back.out(2.5)' }); w.IN(tl, t, e ? '<.15' : 0, { scale: .7, y: 0 });
  } };

  // consejo: {titulo, texto, emoji:'💡'} — 1 paso
  T.consejo = { n: function () { return 1; }, armar: function (g, tl, B, d) {
    var p = w.pieza(g, 960, 600); w.tarjeta(p, 0, 0, 1400, 320, C.sol);
    w.el('circle', { cx: -560, cy: 0, r: 90, fill: 'url(#gSol)' }, p); w.emoji(p, -560, 4, d.emoji || '💡', 100);
    w.txt(p, 90, -70, d.titulo, 42, C.sol, { 'letter-spacing': 5 }); w.multi(p, 90, 40, d.texto, 44, C.txt, 1000);
    B(0); w.IN(tl, p, 0, { scale: .7, y: 0 });
  } };

  // imagen: {src:'data:image/png;base64,...', ancho, alto, titulo, marcas:[{x, y (0 a 1 sobre la imagen), txt}]} — 1 + n pasos: aparece la imagen y se va señalando cada marca con un aro y su rótulo
  T.imagen = { n: function (d) { return 1 + (d.marcas || []).length; }, armar: function (g, tl, B, d) {
    var k = Math.min(1500 / d.ancho, 600 / d.alto), Wd = d.ancho * k, Hd = d.alto * k, cy = 120 + 70 + Hd / 2 + 10;
    var ti = w.pieza(g, 960, 100); w.txt(ti, 0, 0, d.titulo || '', 52, C.sol, { 'letter-spacing': 4 });
    var im = w.pieza(g, 960, cy); w.el('rect', { x: -Wd / 2 - 10, y: -Hd / 2 - 10, width: Wd + 20, height: Hd + 20, rx: 22, fill: '#ffffff' }, im);
    var img = w.el('image', { x: -Wd / 2, y: -Hd / 2, width: Wd, height: Hd, preserveAspectRatio: 'xMidYMid meet' }, im); img.setAttributeNS('http://www.w3.org/1999/xlink', 'href', d.src); img.setAttribute('href', d.src);
    B(0); w.IN(tl, ti, 0); w.IN(tl, im, '<.15', { scale: .85, y: 0 });
    var prev = null;
    (d.marcas || []).forEach(function (m, i) {
      var ring = w.pieza(g, 960 - Wd / 2 + m.x * Wd, cy - Hd / 2 + m.y * Hd); w.el('circle', { r: 40, fill: 'rgba(255,200,60,.15)', stroke: C.sol, 'stroke-width': 7 }, ring);
      var lab = w.chip(g, 960, cy + Hd / 2 + 80, Math.min(1500, String(m.txt).length * 28 + 120), 96, m.txt, { r: 30, size: 44 });
      B(i + 1); if (prev) { tl.to(prev[0], { opacity: 0, duration: .25 }); tl.to(prev[1], { opacity: 0, duration: .25 }, '<'); }
      w.IN(tl, ring, prev ? '>' : 0, { scale: 2.2, y: 0 }); w.IN(tl, lab, '<.1'); prev = [ring, lab];
    });
  } };

  // errores: {items:[{mal, bien}]} (máx 3) — 1 + n pasos: aparecen, se corrige cada uno
  T.errores = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var n = d.items.length, H = n > 2 ? 200 : 230, Y = W.rejilla(n, 960, 610, 0, H + 30, 1);
    var E = d.items.map(function (it, k) { var p = w.pieza(g, 960, Y[k][1]); w.caja(p, 0, 0, 1440, H, 'url(#gCard)', C.coral, 36, 5).setAttribute('filter', 'url(#sombra)');
      w.el('circle', { cx: -620, cy: 0, r: 50, fill: C.coral }, p); w.txt(p, -620, 4, '✗', 56, '#3a0f08');
      w.txt(p, 60, -40, it.mal, 44, C.txt); var L = it.mal.length * 11.5;
      p.tach = w.el('line', { x1: 60 - L, y1: -40, x2: 60 + L, y2: -40, stroke: C.coral, 'stroke-width': 8, 'stroke-dasharray': 2 * L, 'stroke-dashoffset': 2 * L }, p);
      p.b = w.txt(p, 60, 45, '✓ ' + it.bien, 44, C.verde, { opacity: 0 }); return p; });
    B(0); E.forEach(function (p, k) { w.IN(tl, p, k ? '<.2' : 0, { x: k % 2 ? 300 : -300, y: 0 }); });
    E.forEach(function (p, k) { B(k + 1); tl.to(p.tach, { attr: { 'stroke-dashoffset': 0 }, duration: .4 }); tl.to(p.b, { opacity: 1, duration: .3 }, '>'); });
  } };

  // pregunta: {pregunta, opciones:[...], correcta: índice} — 3 pasos: pregunta, opciones, respuesta
  T.pregunta = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var q = w.pieza(g, 960, 330); w.multi(q, 0, 0, '🤔 ' + d.pregunta, 60, C.txt, 1500);
    var largo = Math.max.apply(null, d.opciones.map(function (o) { return String(o).length + 3; })), una = largo > 24; // opciones largas: una debajo de otra
    var P = una ? d.opciones.map(function (_, k) { return [960, 560 + k * 130]; }) : W.rejilla(d.opciones.length, 960, 680, 720, 170, 2);
    var O = d.opciones.map(function (o, k) { var c = w.chip(g, P[k][0], P[k][1], una ? Math.min(1700, largo * 21 + 100) : 660, una ? 108 : 130, String.fromCharCode(65 + k) + ') ' + o, { r: 30, size: una ? 36 : 42 }); return c; });
    B(0); w.IN(tl, q, 0);
    B(1); O.forEach(function (o, k) { w.IN(tl, o, k ? '<.12' : 0); });
    B(2); O.forEach(function (o, k) { if (k === d.correcta) { tl.to(o.r, { attr: { stroke: C.verde, 'stroke-width': 10 }, duration: .3 }, k ? '<' : '>'); w.pop(tl, o, '<'); } else tl.to(o, { opacity: .35, duration: .3 }, '<'); });
  } };

  // resumen: {items:[[cab, txt]...] (máx 6), fin:{titulo, sub}} — 1 + n + 1 pasos
  T.resumen = { n: function (d) { return 2 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo || 'RESUMEN'), n = d.items.length, P = W.rejilla(n, 960, n > 3 ? 645 : 600, 500, 250, 3);
    var Tt = d.items.map(function (r, k) { var p = w.pieza(g, P[k][0], P[k][1]), col = W.PAL[k % 2]; w.tarjeta(p, 0, 0, 460, 210, col); w.txt(p, 0, -50, r[0], 28, col, { 'letter-spacing': 3 }); w.multi(p, 0, 30, r[1], 34, C.txt, 400); return p; });
    var fin = w.pieza(g, 960, 600); w.caja(fin, 0, 0, 1000, 300, 'url(#gSol)', '#ffe7a8', 50, 6).setAttribute('filter', 'url(#sombra)');
    w.txt(fin, 0, -40, (d.fin && d.fin.titulo) || '¡CLASE TERMINADA!', 76, '#3a2a00'); w.txt(fin, 0, 60, (d.fin && d.fin.sub) || 'Ahora, a practicar 🚀', 46, '#3a2a00');
    B(0); w.IN(tl, ti, 0);
    Tt.forEach(function (t, k) { B(k + 1); w.IN(tl, t, 0, { scale: .6, y: 0 }); });
    B(n + 1); w.OUT(tl, Tt.concat(ti), 0, { stagger: .04 }); w.IN(tl, fin, '>', { scale: .3, y: 0, ease: 'elastic.out(1,.6)', d: 1.1 });
  } };

  // comparar: {a:{cab, texto, emoji, estilo:'piedra'}, b:{...}, signo:'=', def:{cab, texto}} — 3 o 4 pasos
  T.comparar = { n: function (d) { return d.def ? 4 : 3; }, armar: function (g, tl, B, d) {
    function lado(x, o, col) { var p = w.pieza(g, x, 520), pied = o.estilo === 'piedra';
      w.caja(p, 0, 0, 600, 340, pied ? 'url(#gPiedra)' : 'url(#gCard)', pied ? '#d8d0c0' : col, 34, 6).setAttribute('filter', 'url(#sombra)');
      w.txt(p, 0, -125, o.cab, 28, pied ? '#4a4438' : col, { 'letter-spacing': 4 });
      if (o.emoji) w.emoji(p, 0, -30, o.emoji, 110);
      w.multi(p, 0, o.emoji ? 85 : 20, o.texto, o.emoji ? 44 : (String(o.texto).length > 12 ? 50 : 104), pied ? '#3d382f' : C.txt, 540, pied ? { 'font-family': 'Georgia,serif' } : null); return p; }
    var A = lado(560, d.a, C.aqua), Bb = lado(1360, d.b, C.sol), s = w.pieza(g, 960, 520); w.txt(s, 0, 0, d.signo || 'vs', d.signo && d.signo.length < 2 ? 140 : 70, C.sol, { filter: 'url(#brillo)' });
    var de = null; if (d.def) { de = w.pieza(g, 960, 850); w.tarjeta(de, 0, 0, 1440, 180, C.sol); w.txt(de, 0, -40, d.def.cab, 32, C.sol, { 'letter-spacing': 4 }); w.multi(de, 0, 30, d.def.texto, 40, C.txt, 1340); }
    B(0); w.IN(tl, A, 0, { x: -200, y: 0 });
    B(1); w.IN(tl, Bb, 0, { x: 200, y: 0 });
    B(2); w.IN(tl, s, 0, { scale: 0, y: 0 }); w.pop(tl, A, '>'); w.pop(tl, Bb, '<');
    if (de) { B(3); tl.to([A, Bb, s], { y: -60, scale: .85, duration: .5, ease: 'power2.inOut' }); w.IN(tl, de, '<.1'); }
  } };

  // antesdespues: {antes:{cab, emoji, texto}, despues:{...}} — 2 pasos
  T.antesdespues = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    function lado(x, o, col, cab) { var p = w.pieza(g, x, 590); w.tarjeta(p, 0, 0, 640, 520, col); w.txt(p, 0, -210, o.cab || cab, 34, col, { 'letter-spacing': 5 }); w.emoji(p, 0, -50, o.emoji || '', 150); w.multi(p, 0, 130, o.texto, 40, C.txt, 560); return p; }
    var A = lado(560, d.antes, C.suave, 'ANTES'), D = lado(1360, d.despues, C.sol, 'DESPUÉS'), f = w.flecha(g, 900, 590, 1030, 590, C.sol, 10);
    B(0); w.IN(tl, A, 0, { x: -200, y: 0 });
    B(1); w.dibujarFlecha(tl, f, 0); w.IN(tl, D, '>', { x: 200, y: 0 });
  } };

  // clasificar: {cajas:[{cab, emoji}] (2-4), fichas:[{txt, caja}]} — 1 + cajas pasos (cada paso llena una caja)
  T.clasificar = { n: function (d) { return 1 + d.cajas.length; }, armar: function (g, tl, B, d) {
    var n = d.cajas.length, ancho = Math.min(440, 1560 / n - 30), X = W.rejilla(n, 960, 0, ancho + 30, 0, n);
    var K = d.cajas.map(function (c, k) { var p = w.pieza(g, X[k][0], 640), col = W.PAL[k % W.PAL.length]; w.caja(p, 0, 0, ancho, 600, 'rgba(0,0,0,.18)', col, 30, 5).setAttribute('stroke-dasharray', '18 12');
      w.txt(p, 0, -255, (c.emoji ? c.emoji + ' ' : '') + c.cab, 32, col, { 'letter-spacing': 2 }); return p; });
    var cuenta = d.cajas.map(function () { return 0; });
    var F = d.fichas.map(function (f) { var k = f.caja, i = cuenta[k]++, c = w.chip(g, X[k][0], 470 + i * 92, ancho - 50, 76, f.txt, { size: 32, r: 20, stroke: W.PAL[k % W.PAL.length] }); c.k = k; return c; });
    B(0); K.forEach(function (p, k) { w.IN(tl, p, k ? '<.1' : 0); });
    d.cajas.forEach(function (_, k) { B(k + 1); F.filter(function (f) { return f.k === k; }).forEach(function (f, j) { w.IN(tl, f, j ? '<.18' : 0, { y: -400, ease: 'bounce.out', d: .7 }); }); });
  } };

  // tabla: {titulo, columnas:[...], filas:[[...]...]} — 1 + filas pasos
  T.tabla = { n: function (d) { return 1 + d.filas.length; }, armar: function (g, tl, B, d) {
    var nc = d.columnas.length, cw = Math.min(420, 1560 / nc), x0 = 960 - (nc - 1) * cw / 2, nf = d.filas.length, rh = Math.min(110, 560 / (nf + 1)), y0 = 420;
    var ti = d.titulo ? w.titulo(g, d.titulo) : null, H = w.pieza(g, 0, 0);
    d.columnas.forEach(function (c, k) { w.caja(H, x0 + k * cw, y0, cw - 12, rh - 14, 'url(#gAqua)', '#d8fff7', 16, 3); w.txt(H, x0 + k * cw, y0, c, Math.min(30, (cw - 30) / (String(c).length * .58)), '#06282a', { 'letter-spacing': 1 }); });
    var R = d.filas.map(function (f, r) { var p = w.pieza(g, 0, 0); f.forEach(function (c, k) { w.caja(p, x0 + k * cw, y0 + (r + 1) * rh, cw - 12, rh - 14, 'url(#gCard)', C.linea, 16, 3); w.txt(p, x0 + k * cw, y0 + (r + 1) * rh, c, Math.min(40, rh * .38, (cw - 30) / (String(c).length * .55)), C.txt); }); return p; });
    B(0); if (ti) w.IN(tl, ti, 0); w.IN(tl, H, ti ? '<.1' : 0);
    R.forEach(function (p, r) { B(r + 1); w.IN(tl, p, 0, { x: -80, y: 0 }); });
  } };

  // venn: {a, b, itemsA:[], itemsB:[], ambos:[]} — 4 pasos
  T.venn = { n: function () { return 4; }, armar: function (g, tl, B, d) {
    var A = w.pieza(g, 760, 620), Bc = w.pieza(g, 1160, 620);
    w.el('circle', { r: 330, fill: 'rgba(127,211,196,.18)', stroke: C.aqua, 'stroke-width': 6 }, A); w.txt(A, -60, -280, d.a, 40, C.aqua);
    w.el('circle', { r: 330, fill: 'rgba(244,182,63,.16)', stroke: C.sol, 'stroke-width': 6 }, Bc); w.txt(Bc, 60, -280, d.b, 40, C.sol);
    function lista(x, it) { var p = w.pieza(g, x, 640); it.forEach(function (s, i) { w.txt(p, 0, (i - (it.length - 1) / 2) * 62, s, 34, C.txt); }); return p; }
    var LA = lista(600, d.itemsA || []), LB = lista(1320, d.itemsB || []), LM = lista(960, d.ambos || []);
    B(0); w.IN(tl, A, 0, { scale: 0, y: 0 }); w.IN(tl, Bc, '<.15', { scale: 0, y: 0 });
    B(1); w.IN(tl, LA, 0); B(2); w.IN(tl, LB, 0); B(3); w.IN(tl, LM, 0, { scale: .5, y: 0 });
  } };

  // balanza: {izq:{cab, items}, der:{cab, items}, gana:'izq'|'der'|null} — 3 pasos
  T.balanza = { n: function () { return 3; }, armar: function (g, tl, B, d) {
    var base = w.pieza(g, 960, 480); w.el('path', { d: 'M-60 380 L60 380 L0 40 Z', fill: C.linea }, base); w.el('circle', { cx: 0, cy: 40, r: 22, fill: C.sol }, base);
    var brazo = w.pieza(g, 960, 520);
    w.el('rect', { x: -620, y: -12, width: 1240, height: 24, rx: 12, fill: C.sol }, brazo);
    function plato(x, o, col) { var p = w.el('g', { transform: 'translate(' + x + ' 0)' }, brazo); w.el('line', { x1: 0, y1: 0, x2: 0, y2: 60, stroke: col, 'stroke-width': 5 }, p);
      w.caja(p, 0, 190, 480, 260, 'url(#gCard)', col, 28, 5); w.txt(p, 0, 90, o.cab, 34, col, { 'letter-spacing': 3 });
      var L = w.el('g', { opacity: 0 }, p); (o.items || []).forEach(function (s, i) { w.txt(L, 0, 150 + i * 52, s, 32, C.txt); }); return L; }
    var LI = plato(-480, d.izq, C.aqua), LD = plato(480, d.der, C.coral);
    B(0); w.IN(tl, base, 0); w.IN(tl, brazo, '<'); tl.to(LI, { opacity: 1, duration: .4 });
    B(1); tl.to(LD, { opacity: 1, duration: .4 });
    B(2); tl.to(brazo, { rotation: d.gana === 'izq' ? -5 : d.gana === 'der' ? 5 : 0, svgOrigin: '960 520', duration: .9, ease: 'elastic.out(1,.5)' });
  } };

  // matriz: {titulo, celdas:[{cab, txt}x4]} (FODA, 2x2) — 1 + 4 pasos
  T.matriz = { n: function (d) { return 1 + d.celdas.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), P = [[580, 500], [1340, 500], [580, 800], [1340, 800]];
    var Cc = d.celdas.map(function (c, k) { var p = w.pieza(g, P[k][0], P[k][1]), col = W.PAL[k]; w.tarjeta(p, 0, 0, 720, 270, col); w.txt(p, 0, -90, c.cab, 34, col, { 'letter-spacing': 4 }); w.multi(p, 0, 25, c.txt, 36, C.txt, 640); return p; });
    B(0); w.IN(tl, ti, 0); Cc.forEach(function (c, k) { B(k + 1); w.IN(tl, c, 0, { scale: .7, y: 0 }); });
  } };
})();
