/* EXTRAS PARA QUE LA CLASE SEA MÁS DIVERTIDA (va después de todas las plantillas):
   1) SFX: efectos de sonido livianos hechos con WebAudio (sin archivos): whoosh al entrar cada escena, ding al revelar una respuesta,
      pop de los stickers, redoble, fanfarria, candado. Van bajitos, por debajo de la voz.
   2) STICKERS: cualquier escena puede llevar "sticker": {txt, paso, x?, y?, rot?} o una lista de ellos. Aparecen de golpe en el paso indicado
      (txt puede ser un emoji, ej. "🤯", o un texto corto, ej. "¡PLOT TWIST!").
   3) Plantillas nuevas: datoloco, ranking, escape. */
var SFX = (function () {
  var ctx = null, out = null, VOL = .22;
  function c() { try { if (!ctx) { var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return null; ctx = new AC(); out = ctx.createGain(); out.gain.value = VOL; out.connect(ctx.destination); }
    if (ctx.state === 'suspended') ctx.resume(); return ctx; } catch (_) { return null; } }
  function tono(f, t, d, tipo, v, f2) { var o = ctx.createOscillator(), g = ctx.createGain(); o.type = tipo || 'sine'; o.frequency.setValueAtTime(f, t); if (f2) o.frequency.exponentialRampToValueAtTime(f2, t + d);
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v || .5, t + .01); g.gain.exponentialRampToValueAtTime(.0001, t + d); o.connect(g); g.connect(out); o.start(t); o.stop(t + d + .05); }
  function ruido(t, d, f1, f2, v, tipo) { var n = ctx.createBufferSource(), b = ctx.createBuffer(1, Math.max(1, ctx.sampleRate * d), ctx.sampleRate), x = b.getChannelData(0);
    for (var i = 0; i < x.length; i++) x[i] = Math.random() * 2 - 1; n.buffer = b; var fl = ctx.createBiquadFilter(), g = ctx.createGain(); fl.type = tipo || 'bandpass'; fl.Q.value = 1.2;
    fl.frequency.setValueAtTime(f1, t); fl.frequency.exponentialRampToValueAtTime(f2, t + d); g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v || .4, t + d * .3); g.gain.exponentialRampToValueAtTime(.0001, t + d);
    n.connect(fl); fl.connect(g); g.connect(out); n.start(t); n.stop(t + d + .05); }
  var S = {
    whoosh: function (t) { ruido(t, .35, 400, 2600, .18); },
    ding: function (t) { tono(1318, t, .5, 'sine', .35); tono(1760, t + .09, .6, 'sine', .3); },
    pop: function (t) { tono(520, t, .12, 'sine', .45, 1100); },
    boom: function (t) { tono(140, t, .5, 'sine', .7, 45); ruido(t, .3, 900, 200, .25, 'lowpass'); },
    redoble: function (t) { for (var i = 0; i < 14; i++) ruido(t + i * .06, .05, 2500, 1800, .12 + i * .012); },
    fanfarria: function (t) { [523, 659, 784, 1046].forEach(function (f, i) { tono(f, t + i * .11, .35, 'triangle', .3); }); tono(1046, t + .48, .7, 'triangle', .3); },
    candado: function (t) { ruido(t, .06, 3000, 2500, .35); tono(880, t + .07, .12, 'square', .12); tono(1320, t + .15, .25, 'sine', .25); },
    tic: function (t) { tono(1600, t, .04, 'square', .08); },
    error: function (t) { tono(220, t, .25, 'sawtooth', .12, 180); }
  };
  return { play: function (n) { if (!c() || !S[n]) return; try { S[n](ctx.currentTime + .01); } catch (_) {} } };
})();

(function () {
  var w = W, C = w.C;
  // ---- sonido de revelación por plantilla: [paso, efecto]
  var REVELA = { pregunta: [2, 'ding'], quiz4: [2, 'ding'], prediccion: [2, 'ding'], completa: [2, 'ding'], fichas: [2, 'ding'], patron: [2, 'ding'], memoria: [2, 'ding'],
    reto: [1, 'ding'], errores: [1, 'error'], logro: [0, 'fanfarria'], resumen: [-1, 'fanfarria'], datoloco: [0, 'boom'] };
  function enPaso(tl, k, f, dt) { tl.call(f, null, 'b' + k + '+=' + (dt || .05)); }
  function sticker(g, s) { var x = s.x || 1560, y = s.y || 330, rot = s.rot == null ? -10 : s.rot, p = w.pieza(g, x, y), emo = /^\p{Extended_Pictographic}/u.test(String(s.txt)) && String(s.txt).length <= 4;
    if (emo) w.emoji(p, 0, 0, s.txt, 170);
    else { var ww = Math.max(220, String(s.txt).length * 30 + 70); w.caja(p, 0, 0, ww + 16, 106, '#fff', '#fff', 22, 2).setAttribute('filter', 'url(#sombra)'); w.caja(p, 0, 0, ww, 90, 'url(#gSol)', '#3a2a00', 18, 4); w.txt(p, 0, 2, s.txt, 44, '#3a2a00', { 'font-weight': 900 }); }
    p.setAttribute('transform', 'rotate(' + rot + ')'); return p; }
  // ======================= DATO LOCO =======================
  // datoloco: «¿Sabías que…?» con explosión y el dato. {texto, emoji, numero?, unidad?} — 2 pasos: estallido y título · el dato (con número que cuenta si hay)
  T.datoloco = { n: function () { return 2; }, armar: function (g, tl, B, d) {
    var rayos = w.pieza(g, 960, 470); for (var i = 0; i < 16; i++) { var a = i * Math.PI / 8; w.el('path', { d: 'M0 0 L' + Math.cos(a - .09) * 900 + ' ' + Math.sin(a - .09) * 900 + ' L' + Math.cos(a + .09) * 900 + ' ' + Math.sin(a + .09) * 900 + ' Z', fill: i % 2 ? 'rgba(244,182,63,.10)' : 'rgba(127,211,196,.07)' }, rayos); }
    var ti = w.pieza(g, 960, 360); w.emoji(ti, -440, 0, '🤯', 120); w.txt(ti, 60, 0, '¿SABÍAS QUÉ…?', 84, C.sol, { 'font-weight': 900, 'letter-spacing': 2 });
    var em = w.pieza(g, 960, 560); w.emoji(em, 0, 0, d.emoji || '💡', 150);
    var num = w.pieza(g, 960, 560), nt = d.numero != null ? w.txt(num, 0, 0, isFinite(+d.numero) ? '0' : String(d.numero) + (d.unidad ? ' ' + d.unidad : ''), 130, C.sol, { 'font-weight': 900 }) : null, numOk = d.numero != null && isFinite(+d.numero);
    var tx = w.pieza(g, 960, 790); w.caja(tx, 0, 0, 1600, 210, 'url(#gCard)', C.sol, 36, 6).setAttribute('filter', 'url(#sombra)'); w.multi(tx, 0, 0, d.texto, 48, C.txt, 1500);
    B(0); w.IN(tl, rayos, 0, { scale: .2, y: 0, d: .5 }); tl.to(rayos, { rotation: 25, duration: 8, ease: 'none' }, '<'); w.IN(tl, ti, '<.1', { scale: 3, y: 0, ease: 'back.out(1.6)', d: .5 }); w.sacudir(tl, '>');
    B(1); if (nt) { w.IN(tl, num, 0, { scale: .3, y: 0 }); if (numOk) w.contador(tl, nt, 0, +d.numero, '<', 1.1, function (v) { return Math.round(v).toLocaleString('es-AR') + (d.unidad ? ' ' + d.unidad : ''); }); } else w.IN(tl, em, 0, { scale: .2, y: 0, ease: 'elastic.out(1,.5)', d: .9 });
    w.IN(tl, tx, nt ? '>-.3' : '<.2', { y: 60 });
  } };

  // ======================= RANKING =======================
  // ranking: top con cuenta regresiva, del último al primero. {titulo, items:[{txt, emoji, dato?}] en orden del 1.º al último (3-5)} — 1 + items pasos
  T.ranking = { n: function (d) { return 1 + d.items.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, '🏆 ' + d.titulo), n = d.items.length, gap = Math.min(135, 640 / n), y0 = 420;
    var F = d.items.map(function (it, k) { var y = y0 + k * gap, p = w.pieza(g, 960, y), oro = k === 0, col = oro ? C.sol : k === 1 ? '#cfd8dc' : k === 2 ? '#e0a070' : C.linea;
      w.caja(p, 0, 0, 1400, gap - 18, oro ? 'url(#gSol)' : 'url(#gCard)', col, 28, oro ? 6 : 4).setAttribute('filter', 'url(#sombra)');
      w.txt(p, -620, 0, '#' + (k + 1), 52, oro ? '#3a2a00' : k > 2 ? C.suave : col, { 'font-weight': 900 }); w.emoji(p, -500, 0, it.emoji || '⭐', 70);
      w.txt(p, -430, it.dato ? -18 : 0, it.txt, 44, oro ? '#3a2a00' : C.txt, { 'text-anchor': 'start', 'font-weight': 800 }); if (it.dato) w.txt(p, -430, 28, it.dato, 30, oro ? '#5a4300' : C.suave, { 'text-anchor': 'start' });
      return p; });
    B(0); w.IN(tl, ti, 0);
    for (var j = n - 1; j >= 0; j--) { B(n - j); if (j === 0) { tl.call(function () { SFX.play('redoble'); }, null, '>'); w.IN(tl, F[0], '>+.85', { scale: .4, y: 0, ease: 'back.out(2)', d: .5 }); tl.call(function () { SFX.play('fanfarria'); }, null, '<'); w.pop(tl, F[0], '>'); }
      else { w.IN(tl, F[j], 0, { x: 300, y: 0, d: .45 }); tl.call(function () { SFX.play('pop'); }, null, '<'); } }
  } };

  // ======================= ESCAPE ROOM =======================
  // escape: una puerta con candados que se abren respondiendo. {titulo?, candados:[{p, r}] (2-3)} — 2 + candados pasos: puerta · cada candado · ¡escapaste!
  T.escape = { n: function (d) { return 2 + d.candados.length; }, armar: function (g, tl, B, d) {
    var ti = w.titulo(g, '🔐 ' + (d.titulo || 'ESCAPE ROOM')), n = d.candados.length;
    var pu = w.pieza(g, 400, 640); w.caja(pu, 0, 0, 380, 560, '#5a3a22', '#8a5a34', 16, 10).setAttribute('filter', 'url(#sombra)'); w.caja(pu, 0, 0, 300, 480, 'none', '#7a4c2c', 10, 5); w.el('circle', { cx: 120, cy: 20, r: 16, fill: C.sol }, pu);
    var L = d.candados.map(function (_, k) { var p = w.pieza(g, 400, 640 + (k - (n - 1) / 2) * 140), t = w.emoji(p, 0, 0, '🔒', 96); p.t = t; return p; });
    var Q = d.candados.map(function (c, k) { var p = w.pieza(g, 1180, 560); w.tarjeta(p, 0, -60, 1080, 250, W.PAL[(k + 1) % W.PAL.length]); w.txt(p, -470, -150, 'CANDADO ' + (k + 1), 26, C.suave, { 'text-anchor': 'start', 'letter-spacing': 3 }); w.multi(p, 0, -50, c.p, 46, C.txt, 980);
      var r = w.pieza(p, 0, 150); w.caja(r, 0, 0, 760, 100, 'url(#gSol)', '#ffe7a8', 50, 5); w.multi(r, 0, 0, '🔑 ' + c.r, 42, '#3a2a00', 700); p.r = r; return p; });
    var fin = w.pieza(g, 1180, 600); w.emoji(fin, 0, -90, '🏃💨', 130); w.txt(fin, 0, 70, '¡ESCAPASTE!', 90, C.sol, { 'font-weight': 900 });
    B(0); w.IN(tl, ti, 0); w.IN(tl, pu, '<.1', { y: 60 }); L.forEach(function (l) { w.IN(tl, l, '<.1', { scale: .3, y: 0 }); });
    Q.forEach(function (q, k) { B(k + 1); if (k) w.OUT(tl, Q[k - 1], 0, { x: -100 }); w.IN(tl, q, k ? '>' : 0, { x: 120, y: 0 }); w.IN(tl, q.r, '>+.9', { scale: .3, y: 0, ease: 'back.out(2.4)' });
      tl.call(function (kk) { L[kk].t.textContent = '🔓'; SFX.play('candado'); }, [k], '>+.1'); w.pop(tl, L[k], '<'); });
    B(n + 1); w.OUT(tl, Q[n - 1], 0); tl.to(pu, { scaleX: .15, transformOrigin: '0% 50%', duration: .6, ease: 'power2.in' }, '>'); tl.call(function () { SFX.play('fanfarria'); }, null, '<'); w.IN(tl, fin, '>', { scale: .3, y: 0, ease: 'elastic.out(1,.5)', d: 1 });
  } };
  Object.keys(T).forEach(function (nom) {
    var orig = T[nom].armar;
    T[nom].armar = function (g, tl, B, d) {
      var pasos = 0; orig.call(this, g, tl, function (k) { pasos++; B(k); }, d);
      try {
        enPaso(tl, 0, function () { SFX.play('whoosh'); }, .02);
        var r = REVELA[nom]; if (r) { var k = r[0] < 0 ? pasos - 1 : r[0]; if (k < pasos) enPaso(tl, k, function () { SFX.play(r[1]); if (r[1] === 'ding' && nom !== 'reto' && window.CONFETI) CONFETI(); }, nom === 'pregunta' || nom === 'quiz4' ? .35 : .25); }
        [].concat(d.sticker || []).forEach(function (s) { if (!s || !s.txt) return; var k = Math.min(pasos - 1, Math.max(0, +s.paso || 0)), p = sticker(g, s);
          tl.fromTo(p, { opacity: 0, scale: 2.4 }, { opacity: 1, scale: 1, duration: .28, ease: 'back.out(2.5)', immediateRender: false }, 'b' + k + '+=.6'); enPaso(tl, k, function () { SFX.play('pop'); }, .62); });
      } catch (_) {}
    };
  });

})();

/* ---- CONFETI al revelar, "3, 2, 1… pensá" antes de la respuesta y BOTÓN DE VELOCIDAD ---- */
(function () {
  var calma = window.AudioContext === undefined && window.webkitAudioContext === undefined; // modo calmo de la plataforma (Menos animación)
  try { if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) calma = true; } catch (_) {}
  window.CONFETI = function () {
    if (calma) return; var cv = document.createElement('canvas'), W = innerWidth, H = innerHeight; cv.width = W; cv.height = H;
    cv.style.cssText = 'position:fixed;inset:0;pointer-events:none;z-index:50'; document.body.appendChild(cv);
    var g = cv.getContext('2d'), cols = ['#F4B63F', '#7FD3C4', '#ff7a66', '#b9a6ff', '#8be38f', '#7fb6ff'], P = [];
    for (var i = 0; i < 90; i++) P.push({ x: W / 2 + (Math.random() - .5) * W * .3, y: H * .55, vx: (Math.random() - .5) * 12, vy: -6 - Math.random() * 9, s: 5 + Math.random() * 7, c: cols[i % 6], r: Math.random() * 6, vr: (Math.random() - .5) * .3 });
    var t0 = performance.now();
    (function paso(t) { var k = t - t0; g.clearRect(0, 0, W, H); P.forEach(function (p) { p.vy += .3; p.x += p.vx; p.y += p.vy; p.r += p.vr; g.save(); g.globalAlpha = Math.max(0, 1 - k / 1600); g.translate(p.x, p.y); g.rotate(p.r); g.fillStyle = p.c; g.fillRect(-p.s / 2, -p.s / 4, p.s, p.s / 2); g.restore(); });
      if (k < 1600) requestAnimationFrame(paso); else cv.remove(); })(t0);
  };
  // pensá: el reproductor lo llama al terminar cada frase; devuelve cuántos ms esperar antes de la siguiente
  var PIENSA = { pregunta: 1, quiz4: 1, completa: 1, vof: 1 };
  window.PENSAR = function (e, k) {
    if (!e || !PIENSA[e.t] || k !== 1) return 0;
    var esc = document.getElementById('escena'); if (!esc) return 0; esc = esc.lastElementChild || esc;
    var NS = 'http://www.w3.org/2000/svg', gg = document.createElementNS(NS, 'g'); gg.setAttribute('transform', 'translate(1690 300)'); esc.appendChild(gg);
    var c = document.createElementNS(NS, 'circle'); c.setAttribute('r', 78); c.setAttribute('fill', '#F4B63F'); c.setAttribute('stroke', '#fff'); c.setAttribute('stroke-width', 6); gg.appendChild(c);
    var t = document.createElementNS(NS, 'text'); t.setAttribute('text-anchor', 'middle'); t.setAttribute('dominant-baseline', 'central'); t.setAttribute('font-size', 76); t.setAttribute('font-weight', 900); t.setAttribute('fill', '#3a2a00'); gg.appendChild(t);
    var s = document.createElementNS(NS, 'text'); s.setAttribute('y', 118); s.setAttribute('text-anchor', 'middle'); s.setAttribute('font-size', 34); s.setAttribute('font-weight', 800); s.setAttribute('fill', '#F4B63F'); s.textContent = 'PENSÁ…'; gg.appendChild(s);
    var n = 3; (function tic() { if (!gg.parentNode) return; if (n === 0) { gg.remove(); return; } t.textContent = n; try { SFX.play('tic'); } catch (_) {}
      if (!calma && window.gsap) gsap.fromTo(gg, { scale: 1.3, svgOrigin: '1690 300' }, { scale: 1, duration: .3, svgOrigin: '1690 300' }); n--; setTimeout(tic, 1000); })();
    return 3000;
  };
  // velocidad: 1x → 1,25x → 1,5x → 0,75x (voz y animaciones). Se recuerda para la próxima clase.
  var V = [1, 1.25, 1.5, .75], vel = 1; try { vel = +localStorage.getItem('wave-vel') || 1; } catch (_) {}
  var play0 = HTMLMediaElement.prototype.play;
  HTMLMediaElement.prototype.play = function () { try { this.playbackRate = vel; } catch (_) {} return play0.apply(this, arguments); };
  function aplicar() { try { if (window.gsap) gsap.globalTimeline.timeScale(vel); } catch (_) {} var b = document.getElementById('vel'); if (b) b.textContent = String(vel).replace('.', ',') + 'x'; }
  function boton() { var ctl = document.getElementById('ctl'); if (!ctl || document.getElementById('vel')) return; var b = document.createElement('button'); b.id = 'vel'; b.setAttribute('aria-label', 'Velocidad');
    b.style.cssText = 'min-width:64px;font-weight:800'; b.onclick = function () { vel = V[(V.indexOf(vel) + 1) % V.length]; try { localStorage.setItem('wave-vel', vel); } catch (_) {} aplicar(); }; ctl.insertBefore(b, document.getElementById('mus') || null); aplicar(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boton); else boton();
})();
