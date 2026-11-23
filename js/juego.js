/* JUEGO EN ACTIVIDADES Y EXAMEN: sonidos, confeti, racha, combo, estrellas, puntos y el jefe con barra de vida.
   Es solo una capa visual y sonora: NO toca la corrección ni lo que se guarda.
   Respeta Accesibilidad: "Menos animación" (sin confeti ni movimientos) y "Sin sonidos". */
(function () {
  function ap(k) { return !!(window.WaveApoyos && WaveApoyos.get(k)); }
  // ---------- sonidos (WebAudio, sin archivos) ----------
  var ctx = null, out = null;
  function c() { if (ap('sinSonido')) return null; try { if (!ctx) { var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return null; ctx = new AC(); out = ctx.createGain(); out.gain.value = .25; out.connect(ctx.destination); }
    if (ctx.state === 'suspended') ctx.resume(); return ctx; } catch (_) { return null; } }
  function tono(f, t, d, tipo, v, f2) { var o = ctx.createOscillator(), g = ctx.createGain(); o.type = tipo || 'sine'; o.frequency.setValueAtTime(f, t); if (f2) o.frequency.exponentialRampToValueAtTime(f2, t + d);
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v || .4, t + .01); g.gain.exponentialRampToValueAtTime(.0001, t + d); o.connect(g); g.connect(out); o.start(t); o.stop(t + d + .05); }
  var SON = {
    bien: function (t) { tono(880, t, .18, 'sine', .35); tono(1320, t + .09, .3, 'sine', .3); },
    mal: function (t) { tono(260, t, .22, 'triangle', .25, 200); },
    racha: function (t) { [660, 880, 1100].forEach(function (f, i) { tono(f, t + i * .07, .2, 'triangle', .25); }); },
    estrella: function (t) { tono(1400, t, .25, 'sine', .3, 1800); },
    golpe: function (t) { tono(150, t, .2, 'square', .18, 70); },
    fanfarria: function (t) { [523, 659, 784, 1046].forEach(function (f, i) { tono(f, t + i * .12, .35, 'triangle', .28); }); tono(1046, t + .5, .8, 'triangle', .28); },
    triste: function (t) { [440, 392, 330].forEach(function (f, i) { tono(f, t + i * .18, .3, 'triangle', .2); }); }
  };
  function sonar(n) { if (!c() || !SON[n]) return; try { SON[n](ctx.currentTime + .01); } catch (_) {} }

  // ---------- confeti (canvas liviano, 1,5 s) ----------
  function confeti(cerca, mucho) {
    if (ap('sinAnim') || document.documentElement.classList.contains('ap-sin-anim')) return;
    var cv = document.createElement('canvas'), W = innerWidth, H = innerHeight; cv.width = W; cv.height = H;
    cv.style.cssText = 'position:fixed;inset:0;pointer-events:none;z-index:99999'; document.body.appendChild(cv);
    var g = cv.getContext('2d'), r = cerca && cerca.getBoundingClientRect ? cerca.getBoundingClientRect() : { left: W / 2, top: H / 3, width: 0, height: 0 };
    var x0 = r.left + r.width / 2, y0 = r.top + Math.min(r.height, 80) / 2, cols = ['#F4B63F', '#7FD3C4', '#ff7a66', '#b9a6ff', '#8be38f', '#7fb6ff'];
    var P = []; for (var i = 0; i < (mucho ? 160 : 60); i++) P.push({ x: mucho ? Math.random() * W : x0, y: mucho ? -20 - Math.random() * H * .3 : y0, vx: (Math.random() - .5) * (mucho ? 4 : 10), vy: mucho ? 2 + Math.random() * 4 : -4 - Math.random() * 7, s: 5 + Math.random() * 6, c: cols[i % cols.length], r: Math.random() * 6, vr: (Math.random() - .5) * .3 });
    var t0 = performance.now(), dur = mucho ? 2600 : 1500;
    (function paso(t) { var k = t - t0; g.clearRect(0, 0, W, H); P.forEach(function (p) { p.vy += .25; p.x += p.vx; p.y += p.vy; p.r += p.vr; g.save(); g.globalAlpha = Math.max(0, 1 - k / dur); g.translate(p.x, p.y); g.rotate(p.r); g.fillStyle = p.c; g.fillRect(-p.s / 2, -p.s / 4, p.s, p.s / 2); g.restore(); });
      if (k < dur) requestAnimationFrame(paso); else cv.remove(); })(t0);
  }

  // ---------- estilos ----------
  var css = document.createElement('style');
  css.textContent = '.wj-racha{position:fixed;left:50%;top:18px;transform:translateX(-50%);z-index:9999;background:#F4B63F;color:#3a2a00;font-weight:900;border-radius:99px;padding:8px 18px;box-shadow:0 6px 20px rgba(0,0,0,.25);font-size:18px;animation:wjPop .35s ease-out}' +
    '@keyframes wjPop{0%{transform:translateX(-50%) scale(.4)}70%{transform:translateX(-50%) scale(1.12)}100%{transform:translateX(-50%) scale(1)}}' +
    '.wj-panel{margin:14px auto 4px;max-width:560px;text-align:center}.wj-est{font-size:44px;letter-spacing:6px;line-height:1}.wj-est i{font-style:normal;display:inline-block;opacity:.18;transition:opacity .2s,transform .25s}.wj-est i.on{opacity:1;transform:scale(1.15)}' +
    '.wj-chips{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}.wj-chip{background:rgba(127,211,196,.14);border:2px solid rgba(127,211,196,.5);border-radius:99px;padding:5px 12px;font-weight:800;font-size:15px}' +
    '.wj-jefe{margin:12px auto 0;max-width:420px;text-align:center}.wj-jefe-cara{font-size:64px;display:inline-block;transition:transform .2s,filter .4s}.wj-jefe-cara.golpe{transform:translateX(6px) rotate(-8deg)}.wj-jefe-cara.ko{filter:grayscale(1);transform:rotate(90deg) translateY(10px)}' +
    '.wj-vida{height:16px;border-radius:99px;background:rgba(0,0,0,.15);overflow:hidden;margin-top:6px;border:2px solid rgba(0,0,0,.15)}.wj-vida b{display:block;height:100%;width:100%;background:linear-gradient(90deg,#ff7a66,#e2453c);transition:width .35s ease-out}' +
    '.wj-jefe small{display:block;margin-top:6px;font-weight:800}.wj-medalla{font-size:56px;margin-top:6px;display:inline-block;animation:wjPop2 .6s ease-out}@keyframes wjPop2{0%{transform:scale(.2) rotate(-30deg)}100%{transform:scale(1) rotate(0)}}' +
    '.ap-sin-anim .wj-racha,.ap-sin-anim .wj-medalla{animation:none}';
  document.head.appendChild(css);

  // ---------- racha en vivo (al comprobar de a una) ----------
  var racha = 0, mejor = 0;
  function cartel(txt) { var v = document.querySelector('.wj-racha'); if (v) v.remove(); var d = document.createElement('div'); d.className = 'wj-racha'; d.textContent = txt; document.body.appendChild(d); setTimeout(function () { d.remove(); }, 1800); }
  function respuesta(ok, el) {
    if (ok) { racha++; mejor = Math.max(mejor, racha); sonar(racha >= 3 ? 'racha' : 'bien'); confeti(el); if (racha >= 3) cartel('🔥 ¡' + racha + ' seguidas!'); }
    else { racha = 0; sonar('mal'); }
  }
  function reiniciar() { racha = 0; mejor = 0; }

  // ---------- pantalla de resultado ----------
  // o: {nota, ok, examen, scores:[0..100 por pregunta, en orden], tiempos:[seg] (Relámpago), limites:[seg]}
  function estrellas(nota) { return nota >= 90 ? 3 : nota >= 70 ? 2 : nota >= 40 ? 1 : 0; }
  function resultado(cuerpo, o) {
    var box = cuerpo.querySelector('.mt-res'); if (!box) return;
    var sc = o.scores || [], bien = sc.filter(function (s) { return s >= 100; }).length, r = 0, mr = 0;
    sc.forEach(function (s) { if (s >= 100) { r++; mr = Math.max(mr, r); } else r = 0; });
    var combo = 0; if (o.tiempos && o.limites) sc.forEach(function (s, i) { if (s >= 100 && o.tiempos[i] != null && o.tiempos[i] <= (o.limites[i] || 20) / 2) combo++; });
    var est = estrellas(o.nota), pts = Math.round(o.nota * 10 + bien * 5 + mr * 10 + combo * 15);
    var p = document.createElement('div'); p.className = 'wj-panel';
    var h = '';
    if (o.examen && sc.length) h += '<div class="wj-jefe"><span class="wj-jefe-cara">👾</span><div class="wj-vida"><b></b></div><small class="wj-jefe-txt">El jefe de la misión</small></div>';
    h += '<div class="wj-est" aria-label="' + est + ' de 3 estrellas"><i>⭐</i><i>⭐</i><i>⭐</i></div>';
    if (o.examen && o.ok) h += '<div class="wj-medalla">' + (o.nota >= 90 ? '🥇' : o.nota >= 80 ? '🥈' : '🥉') + '</div>';
    h += '<div class="wj-chips"><span class="wj-chip">✨ ' + pts + ' puntos</span>' + (mr >= 2 ? '<span class="wj-chip">🔥 Mejor racha: ' + mr + '</span>' : '') + (combo >= 2 ? '<span class="wj-chip">⚡ Combo x' + combo + '</span>' : '') + '</div>';
    p.innerHTML = h; box.appendChild(p);
    var cara = p.querySelector('.wj-jefe-cara'), vida = p.querySelector('.wj-vida b'), jt = p.querySelector('.wj-jefe-txt'), I = p.querySelectorAll('.wj-est i');
    var sinAnim = ap('sinAnim') || document.documentElement.classList.contains('ap-sin-anim'), t = 300, dt = sinAnim ? 0 : 450;
    function luego(f, ms) { if (sinAnim) f(); else setTimeout(f, ms); }
    if (cara) { var v = 100; sc.forEach(function (s, i) { luego(function () { if (s >= 100 || s > 0) { v = Math.max(0, v - 100 * (s / 100) / sc.length); vida.style.width = v + '%'; cara.classList.add('golpe'); sonar('golpe'); setTimeout(function () { cara.classList.remove('golpe'); }, 180); } }, t + i * dt); });
      t += sc.length * dt + 200;
      luego(function () { if (o.ok) { vida.style.width = '0%'; cara.classList.add('ko'); jt.textContent = '¡Derrotaste al jefe!'; } else jt.textContent = 'El jefe sigue en pie: ¡revancha cuando quieras!'; }, t); t += 250; }
    for (var k = 0; k < 3; k++) (function (k) { if (k < est) luego(function () { I[k].classList.add('on'); sonar('estrella'); }, t + k * (sinAnim ? 0 : 280)); })(k);
    luego(function () { if (o.ok || est >= 2) { sonar('fanfarria'); confeti(null, true); } else sonar('triste'); }, t + 3 * (sinAnim ? 0 : 280) + 150);
    reiniciar();
  }
  window.WaveJuego = { respuesta: respuesta, resultado: resultado, reiniciar: reiniciar, sonar: sonar, confeti: confeti };
})();
