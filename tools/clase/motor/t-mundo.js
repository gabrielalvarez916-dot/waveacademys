/* PLANTILLA MUNDO: escenas vivas para Ciencias (escenario dibujado + objetos que se mueven + cámara que entra).
   {t:'mundo', fondo:'jardin'|'suelo'|'lab'|'espacio'|'agua'|'celula'|'cielo', entrada:'zoom' (opcional, la cámara "cae" en la escena),
    tuneles:[[[x,y],...],...], camaras:[{x,y,rx,ry}] (para 'suelo'),
    pasos:[{acc:[...], txt}]}  — n = pasos. Coordenadas del escenario: 1920 × 1080.
   Acciones: {pon:id, e:'🐜', x, y, s:90, etq}  {mueve:id, ruta:[[x,y],...], dur, loop}  {etq:id, txt}  {late:id}  {crece:id, s}  {sale:id}
             {zoom:[x,y,factor]} (la cámara se acerca)  {dib:'elipse'|'flecha'|'texto'|'rect', ...} */
(function () {
  var w = W, C = w.C, NS = 'http://www.w3.org/2000/svg';
  function el(t, a, p) { return w.el(t, a, p); }
  function grad(g, id, stops, vertical) { var d = el('defs', {}, g), lg = el('linearGradient', { id: id, x1: 0, y1: 0, x2: vertical === false ? 1 : 0, y2: vertical === false ? 0 : 1 }, d);
    stops.forEach(function (s) { el('stop', { offset: s[0], 'stop-color': s[1] }, lg); }); return 'url(#' + id + ')'; }
  var uid = 0;
  var FONDOS = {
    jardin: function (g, d) { var k = 'm' + (uid++);
      el('rect', { x: 0, y: 0, width: 1920, height: 1080, fill: grad(g, k + 's', [[0, '#7cc8f0'], [0.7, '#d6f1ff']]) }, g);
      el('circle', { cx: 1650, cy: 190, r: 90, fill: '#ffe27a' }, g); el('circle', { cx: 1650, cy: 190, r: 130, fill: '#ffe27a', opacity: .25 }, g);
      el('rect', { x: 0, y: 780, width: 1920, height: 300, fill: grad(g, k + 'p', [[0, '#79c25a'], [1, '#3f8a34']]) }, g);
      for (var i = 0; i < 70; i++) { var x = i * 28 + (i * 37) % 13; el('path', { d: 'M' + x + ' 790 q 6 -30 ' + (i % 2 ? 10 : -6) + ' -46', stroke: '#2f7a2c', 'stroke-width': 4, fill: 'none' }, g); } },
    suelo: function (g, d) { var k = 'm' + (uid++);
      el('rect', { x: 0, y: 0, width: 1920, height: 300, fill: grad(g, k + 's', [[0, '#8fd0f2'], [1, '#d8f2ff']]) }, g);
      el('rect', { x: 0, y: 270, width: 1920, height: 50, fill: '#5daa45' }, g);
      el('rect', { x: 0, y: 310, width: 1920, height: 770, fill: grad(g, k + 't', [[0, '#8a5a35'], [0.5, '#6e4527'], [1, '#4b2e19']]) }, g);
      for (var i = 0; i < 60; i++) el('ellipse', { cx: (i * 157) % 1920, cy: 360 + (i * 89) % 700, rx: 8 + i % 9, ry: 5 + i % 5, fill: '#5a3a20', opacity: .55 }, g);
      (d.tuneles || []).forEach(function (t) { var pd = 'M' + t.map(function (p) { return p[0] + ' ' + p[1]; }).join(' L');
        el('path', { d: pd, stroke: '#2e1b0d', 'stroke-width': 74, fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, g);
        el('path', { d: pd, stroke: '#3d2512', 'stroke-width': 58, fill: 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, g); });
      (d.camaras || []).forEach(function (c) { el('ellipse', { cx: c.x, cy: c.y, rx: c.rx + 8, ry: c.ry + 8, fill: '#2e1b0d' }, g); el('ellipse', { cx: c.x, cy: c.y, rx: c.rx, ry: c.ry, fill: '#3d2512' }, g); }); },
    lab: function (g, d) { var k = 'm' + (uid++);
      el('rect', { x: 0, y: 0, width: 1920, height: 1080, fill: grad(g, k + 'w', [[0, '#e9f3ee'], [1, '#cfe3d9']]) }, g);
      el('rect', { x: 0, y: 760, width: 1920, height: 40, fill: '#9c7550' }, g); el('rect', { x: 0, y: 800, width: 1920, height: 280, fill: grad(g, k + 'm', [[0, '#7a5a3c'], [1, '#5a4029']]) }, g); },
    espacio: function (g, d) { el('rect', { x: 0, y: 0, width: 1920, height: 1080, fill: '#050818' }, g);
      for (var i = 0; i < 160; i++) el('circle', { cx: (i * 389) % 1920, cy: (i * 211) % 1080, r: (i % 5) / 2 + .6, fill: '#fff', opacity: .3 + (i % 7) / 10 }, g); },
    agua: function (g, d) { var k = 'm' + (uid++);
      el('rect', { x: 0, y: 0, width: 1920, height: 260, fill: '#bfe7fb' }, g);
      el('rect', { x: 0, y: 240, width: 1920, height: 840, fill: grad(g, k + 'a', [[0, '#4fb3dc'], [1, '#14506e']]) }, g);
      el('path', { d: 'M0 940 Q 480 900 960 950 T 1920 930 L1920 1080 L0 1080 Z', fill: '#d9c08a' }, g);
      for (var i = 0; i < 24; i++) el('circle', { cx: (i * 173) % 1920, cy: 300 + (i * 97) % 600, r: 4 + i % 6, fill: '#fff', opacity: .25 }, g); },
    celula: function (g, d) { el('rect', { x: 0, y: 0, width: 1920, height: 1080, fill: '#e9f6ef' }, g);
      el('ellipse', { cx: 960, cy: 600, rx: 760, ry: 400, fill: '#cdeedd', stroke: '#5aa985', 'stroke-width': 14 }, g); },
    cielo: function (g, d) { var k = 'm' + (uid++); el('rect', { x: 0, y: 0, width: 1920, height: 1080, fill: grad(g, k + 'c', [[0, '#5aa8e6'], [1, '#cdeaff']]) }, g); }
  };

  T.mundo = { n: function (d) { return d.pasos.length; }, armar: function (g, tl, B, d) {
    var mundo = w.pieza(g, 0, 0), cam = mundo; // la cámara mueve al grupo entero
    (FONDOS[d.fondo] || FONDOS.cielo)(el('g', {}, mundo), d);
    var capa = el('g', {}, mundo), S = {}, cap = null;
    function sprite(a) { var p = el('g', { transform: 'translate(' + a.x + ' ' + a.y + ')' }, capa), q = el('g', { opacity: 0 }, p);
      w.emoji(q, 0, 0, a.e, a.s || 90); if (a.rot) q.setAttribute('transform', 'rotate(' + a.rot + ')'); return { p: p, q: q, x: a.x, y: a.y, s: a.s || 90, etq: null }; }
    function etiqueta(sp, txt) { var t = el('g', { opacity: 0 }, sp.p), ww = txt.length * 22 + 50, dy = -(sp.s * 0.75 + 30);
      w.caja(t, 0, dy, ww, 58, 'rgba(255,255,255,.94)', C.aqua, 26, 4); w.txt(t, 0, dy, txt, 32, '#14300c'); el('line', { x1: 0, y1: dy + 29, x2: 0, y2: -sp.s * 0.4, stroke: C.aqua, 'stroke-width': 3 }, t); return t; }
    B(0);
    if (d.entrada === 'zoom') tl.fromTo(mundo, { opacity: 0, scale: .35, svgOrigin: '960 540' }, { opacity: 1, scale: 1, svgOrigin: '960 540', duration: 1.1, ease: 'power3.out' }, 0);
    else tl.fromTo(mundo, { opacity: 0 }, { opacity: 1, duration: .5 }, 0);
    d.pasos.forEach(function (p, k) { if (k) B(k);
      (p.acc || []).forEach(function (a, j) { var pos = j ? '<.15' : '>';
        if (a.pon) { var sp = S[a.pon] = sprite(a); tl.fromTo(sp.q, { opacity: 0, scale: 0, transformOrigin: '50% 50%' }, { opacity: 1, scale: 1, transformOrigin: '50% 50%', duration: .5, ease: 'back.out(2)' }, pos);
          if (a.etq) { sp.etq = etiqueta(sp, a.etq); tl.to(sp.etq, { opacity: 1, duration: .3 }, '>-.1'); } }
        else if (a.mueve && S[a.mueve]) { var s2 = S[a.mueve], ruta = a.ruta, dur = (a.dur || 2) / ruta.length, tw = gsap.timeline({ repeat: a.loop ? -1 : 0 });
          var px = s2.x; ruta.forEach(function (pt) { var izq = pt[0] < px; px = pt[0]; tw.set(s2.q, { scaleX: (a.mira === false) ? 1 : (izq ? 1 : -1), transformOrigin: '50% 50%' }); tw.to(s2.p, { attr: { transform: 'translate(' + pt[0] + ' ' + pt[1] + ')' }, duration: dur, ease: 'none' }); });
          if (a.loop) tl.call(function () { tw.play(0); }, null, pos); else { tw.pause(); tl.add(tw.play(), pos); }
          if (!a.loop) { s2.x = ruta[ruta.length - 1][0]; s2.y = ruta[ruta.length - 1][1]; } }
        else if (a.etq && S[a.etq]) { var s3 = S[a.etq]; if (s3.etq) tl.to(s3.etq, { opacity: 0, duration: .2 }, pos); s3.etq = etiqueta(s3, a.txt); tl.to(s3.etq, { opacity: 1, duration: .35 }, '>'); }
        else if (a.late && S[a.late]) { var s4 = S[a.late]; tl.call(function () { gsap.to(s4.q, { scale: 1.15, transformOrigin: '50% 50%', duration: .5, yoyo: true, repeat: -1, ease: 'sine.inOut' }); }, null, pos); }
        else if (a.crece && S[a.crece]) tl.to(S[a.crece].q, { scale: a.s || 1.6, transformOrigin: '50% 50%', duration: .8, ease: 'power2.out' }, pos);
        else if (a.sale && S[a.sale]) tl.to(S[a.sale].p, { opacity: 0, duration: .4 }, pos);
        else if (a.zoom) tl.to(cam, { scale: a.zoom[2], svgOrigin: a.zoom[0] + ' ' + a.zoom[1], duration: 1.4, ease: 'power2.inOut' }, pos);
        else if (a.dib) { var gg = el('g', { opacity: 0 }, capa);
          if (a.dib === 'elipse') el('ellipse', { cx: a.x, cy: a.y, rx: a.rx, ry: a.ry, fill: a.fill || 'none', stroke: a.color || C.sol, 'stroke-width': a.ancho || 8, 'stroke-dasharray': a.dash ? '18 12' : null }, gg);
          else if (a.dib === 'rect') el('rect', { x: a.x, y: a.y, width: a.w, height: a.h, rx: a.r || 12, fill: a.fill || 'none', stroke: a.color || C.sol, 'stroke-width': a.ancho || 6 }, gg);
          else if (a.dib === 'flecha') { var f = w.flecha(gg, a.de[0], a.de[1], a.a[0], a.a[1], a.color || C.sol, a.ancho || 9); tl.set(gg, { opacity: 1 }, pos); w.dibujarFlecha(tl, f, '>'); return; }
          else if (a.dib === 'texto') { w.caja(gg, a.x, a.y, String(a.s).length * (a.size || 40) * .55 + 60, (a.size || 40) * 1.6, 'rgba(255,255,255,.92)', a.color || C.aqua, 22, 4); w.txt(gg, a.x, a.y, a.s, a.size || 40, '#14300c'); }
          tl.to(gg, { opacity: 1, duration: .4 }, pos); }
      });
      if (cap) w.OUT(tl, cap, '<'); cap = null;
      if (p.txt) { cap = w.chip(g, 960, 985, Math.min(1600, p.txt.length * 25 + 120), 84, p.txt, { size: 40, stroke: C.aqua }); w.IN(tl, cap, '<.1'); }
    });
  } };
})();
