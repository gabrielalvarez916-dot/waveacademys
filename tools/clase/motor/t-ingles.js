/* PLANTILLAS · INGLÉS (tarjetas que se dan vuelta, frases armadas por colores y pronunciación) */
(function () {
  var w = W, C = w.C;

  // tarjetas: flashcards. {titulo, items:[{en, es, emoji?}] (1-4)}. Un paso por tarjeta: aparece en inglés y se da vuelta para mostrar el español.
  T.tarjetas = { n: function (d) { return d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), n = d.items.length, P = w.rejilla(n, 960, 640, 520, 360, 2);
    var F = d.items.map(function (it, k) {
      var col = w.PAL[k % w.PAL.length], x = P[k][0], y = P[k][1];
      var fr = w.pieza(g, x, y); w.tarjeta(fr, 0, 0, 470, 330, col);
      if (it.emoji) w.emoji(fr, 0, -85, it.emoji, 100);
      w.multi(fr, 0, it.emoji ? 55 : 0, it.en, 56, C.txt, 420); w.txt(fr, 190, -130, '🔊', 40, C.txt);
      var bk = w.pieza(g, x, y); w.tarjeta(bk, 0, 0, 470, 330, C.sol);
      w.txt(bk, 0, -95, 'EN ESPAÑOL', 26, C.suave); w.multi(bk, 0, 30, it.es, 54, C.txt, 420);
      return { fr: fr, bk: bk };
    });
    B(0); w.IN(tl, ti, 0);
    F.forEach(function (c, k) {
      if (k) B(k);
      w.IN(tl, c.fr, k ? 0 : '<.15', { y: 0, scale: .85 });
      tl.to(c.fr, { scaleX: 0, duration: .25, ease: 'power1.in' }, '>+.6');
      w.IN(tl, c.bk, '>', { scaleX: 0, y: 0, scale: 1, d: .3, ease: 'power1.out' });
    });
  } };

  // oracion: una frase armada pieza por pieza, cada una con su rol en color. {titulo, partes:[{txt, rol}] (2-5), traduccion}
  // rol: sujeto | verbo | complemento | lugar | tiempo (cualquier otra cosa se pinta con el color por defecto). Pasos: una por parte + la traducción.
  var ROLES = { sujeto: { col: C.azul, nom: 'QUIÉN' }, verbo: { col: C.coral, nom: 'ACCIÓN' }, complemento: { col: C.sol, nom: 'QUÉ' }, lugar: { col: C.verde, nom: 'DÓNDE' }, tiempo: { col: C.lila, nom: 'CUÁNDO' } };
  T.oracion = { n: function (d) { return d.partes.length + 1; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), gap = 26, ws = d.partes.map(function (p) { return Math.max(190, String(p.txt).length * 30 + 70); });
    var tot = ws.reduce(function (a, b) { return a + b; }, 0) + gap * (ws.length - 1), x = 960 - tot / 2, y = 560;
    var B2 = d.partes.map(function (p, k) {
      var r = ROLES[p.rol] || { col: C.aqua, nom: String(p.rol || '').toUpperCase() }, cx = x + ws[k] / 2; x += ws[k] + gap;
      var pz = w.pieza(g, cx, y); w.caja(pz, 0, 0, ws[k], 130, 'url(#gCard)', r.col, 28, 8).setAttribute('filter', 'url(#sombra)'); w.txt(pz, 0, 0, p.txt, 52, C.txt);
      var lb = w.pieza(g, cx, y + 112); w.txt(lb, 0, 0, r.nom, 28, r.col, { 'font-weight': 800 });
      return { pz: pz, lb: lb };
    });
    var tr = w.pieza(g, 960, 830); w.multi(tr, 0, 0, '«' + d.traduccion + '»', 44, C.suave, 1500);
    B(0); w.IN(tl, ti, 0);
    B2.forEach(function (o, k) { if (k) B(k); w.IN(tl, o.pz, k ? 0 : '<.15', { x: -50, y: 0 }); w.IN(tl, o.lb, '>-.3', { y: 14 }); });
    B(d.partes.length); w.IN(tl, tr, 0, { y: 20 });
  } };

  // pronunciacion: palabras con cómo se leen en español. {titulo, palabras:[{en, como, es?}] (1-3)}. Un paso por palabra.
  T.pronunciacion = { n: function (d) { return d.palabras.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, d.titulo), n = d.palabras.length, gap = 215, y0 = 640 - (n - 1) * gap / 2;
    var R = d.palabras.map(function (p, k) {
      var col = w.PAL[k % w.PAL.length], pz = w.pieza(g, 960, y0 + k * gap);
      w.tarjeta(pz, 0, 0, 1500, 170, col);
      w.txt(pz, -640, 0, '🔊', 62, C.txt); w.txt(pz, -250, 0, p.en, 66, C.txt, { 'font-weight': 800 });
      w.txt(pz, 250, -28, 'SE LEE', 24, C.suave); w.txt(pz, 250, 28, p.como, 50, C.sol, { 'font-weight': 800 });
      if (p.es) w.txt(pz, 610, 0, p.es, 36, C.suave);
      return pz;
    });
    B(0); w.IN(tl, ti, 0);
    R.forEach(function (pz, k) { if (k) B(k); w.IN(tl, pz, k ? 0 : '<.15', { x: -60, y: 0 }); });
  } };
})();
