/* REPRODUCTOR: arma cada escena con su plantilla, la sincroniza con el audio de cada frase y maneja los controles. */
(function () {
  var w = W, C = w.C, $ = w.$, el = w.el, CL = window.CLASE, E = CL.escenas;
  var st = { e: -1, f: 0, play: false, gen: 0 }, esc = null, tl = null, errores = [];
  E.forEach(function (e, i) { var t = T[e.t]; if (!t) errores.push('Escena ' + (i + 1) + ': no existe la plantilla "' + e.t + '"'); else if (t.n(e) !== e.voz.length) errores.push('Escena ' + (i + 1) + ' (' + e.t + '): tiene ' + e.voz.length + ' frases y la plantilla pide ' + t.n(e)); });
  window.CLASE_ERRORES = errores; if (errores.length && window.console) console.error(errores.join('\n'));

  // ambiente
  for (var i = 0; i < 9; i++) { var yy = 830 + i * i * 3.2; el('line', { x1: 0, y1: yy, x2: 1920, y2: yy, stroke: C.aqua, 'stroke-opacity': .06 + i * .012, 'stroke-width': 2 }, $('piso')); }
  for (i = -10; i <= 10; i++) el('line', { x1: 960 + i * 70, y1: 830, x2: 960 + i * 420, y2: 1080, stroke: C.aqua, 'stroke-opacity': .09, 'stroke-width': 2 }, $('piso'));
  for (i = 0; i < 16; i++) { var pp = el('circle', { cx: Math.random() * 1920, cy: Math.random() * 1080, r: 2 + Math.random() * 3.5, fill: i % 4 ? C.aqua : C.sol, opacity: .12 + Math.random() * .3 }, $('particulas')); gsap.to(pp, { attr: { cy: '-=' + (150 + Math.random() * 250) }, opacity: 0, duration: 7 + Math.random() * 6, repeat: -1, delay: -Math.random() * 12, ease: 'none' }); }
  $('barra').innerHTML = E.map(function (_, k) { return '<i data-ir="' + k + '"><b></b></i>'; }).join('');
  [].forEach.call(document.querySelectorAll('#barra i'), function (b) { b.onclick = function () { irA(+b.dataset.ir); }; });

  function barra() { [].forEach.call(document.querySelectorAll('#barra b'), function (b, k) { b.style.width = k < st.e ? '100%' : k > st.e ? '0' : Math.round(st.f / E[k].voz.length * 100) + '%'; }); $('pp').textContent = st.play ? '❚❚' : '▶'; }
  function limpio(s) { return s.replace(/\*/g, '').replace(/\s*\+\s*/g, ' más ').replace(/\s*×\s*/g, ' por '); }
  // subtítulos de a 3 palabras, la clave en amarillo. Primeros años (1.º a 3.º del Nivel Medio): de a 2 palabras y en imprenta mayúscula (CSS del shell)
  var PRIM = CL.estilo === 'primeros', palabras = [], GRUPO = PRIM ? 2 : 3;
  // primeros años: más tiempo entre frases, entre escenas y para pensar la respuesta de una pregunta
  function pausaFrase(e, k) { if (!PRIM) return 30; return e.t === 'pregunta' && k === 1 ? 3500 : 700; }
  function subs(frase) { marcar.a = -1; marcar.ult = -1; var raw = frase.split(' '), cl = false; palabras = raw.map(function (r) { if (r[0] === '*') cl = true; var p = { w: r.replace(/\*/g, ''), k: cl }; if (r.replace(/[.,:;!?…]+$/, '').slice(-1) === '*') cl = false; return p; }); marcar(0); }
  function marcar(k) {
    var s = $('subs'); s.innerHTML = ''; if (!palabras.length) return;
    k = Math.max(0, Math.min(k, palabras.length - 1));
    // cada palabra que se dice avisa a la escena (así los números aparecen justo cuando la voz los cuenta)
    if (esc && esc.alDecir) for (var j = marcar.ult + 1; j <= k; j++) esc.alDecir(palabras[j].w, st.f);
    marcar.ult = Math.max(marcar.ult, k);
    var a = Math.floor(k / GRUPO) * GRUPO, t = el('text', { x: 960, y: 125, 'font-size': 76, stroke: 'rgba(0,0,0,.55)', 'stroke-width': 12, 'paint-order': 'stroke', 'stroke-linejoin': 'round' }, s);
    palabras.slice(a, a + GRUPO).forEach(function (p, j) { var sp = el('tspan', { fill: p.k ? C.sol : '#fff', opacity: a + j <= k ? 1 : 0 }, t); sp.textContent = (j ? ' ' : '') + p.w; });
    if (a !== marcar.a) { marcar.a = a; gsap.fromTo(t, { scale: .82, transformOrigin: '960px 105px' }, { scale: 1, duration: .22, ease: 'back.out(3)' }); }
  }
  // voz: un audio por frase (window.VOZ_AUDIO). Sin audio: solo subtítulos con tiempo estimado.
  var AUD = new Audio(); AUD.preload = 'auto'; MUSICA.hablando = function () { return !AUD.paused; };
  function cortar() { st.gen++; try { AUD.pause(); } catch (_) {} }
  function decir(txt, g, fin, k) {
    var n = txt.split(' ').length, v = window.VOZ_AUDIO && VOZ_AUDIO[st.e] && VOZ_AUDIO[st.e][k], hecho = false;
    function listo() { if (hecho || g !== st.gen) return; hecho = true; marcar(999); fin(); }
    if (!v) { var x = 0, iv = setInterval(function () { if (g !== st.gen) return clearInterval(iv); marcar(x++); if (x > n) { clearInterval(iv); listo(); } }, 260); return; }
    AUD.onended = listo; AUD.onerror = listo; AUD.src = 'data:audio/mpeg;base64,' + v.a; AUD.currentTime = 0;
    var Wd = v.w || [], cap = palabras.length || n;
    (function tic() { if (g !== st.gen || hecho) return; var ms = AUD.currentTime * 1000, c = 0; while (c < Wd.length && Wd[c] <= ms) c++; marcar(Wd.length ? Math.round((c - 1) * cap / Wd.length) : 0); requestAnimationFrame(tic); })();
    AUD.play().catch(function () { pausa(); });
    AUD.onloadedmetadata = function () { var dd = AUD.duration; if (isFinite(dd)) setTimeout(function () { if (!AUD.paused && g === st.gen && AUD.currentTime >= dd - .05) listo(); }, (dd + 2) * 1000); };
  }
  function frase(k) {
    var e = E[st.e], g = st.gen;
    if (k >= e.voz.length) return setTimeout(function () { if (g === st.gen && st.play) { if (st.e < E.length - 1) irA(st.e + 1); else { st.play = false; MUSICA.pausa(); barra(); try { parent.postMessage({ tipo: 'wave-clase-fin', puntaje: 100 }, '*'); } catch (_) {} } } }, PRIM ? 900 : 150);
    st.f = k; barra(); subs(e.voz[k]);
    if (tl.labels['b' + k] != null) tl.play('b' + k);
    decir(limpio(e.voz[k]), g, function () { if (g === st.gen && st.play) setTimeout(function () { if (g === st.gen && st.play) frase(k + 1); }, pausaFrase(e, k)); }, k);
  }
  function armarEscena(i) {
    var vieja = esc; if (vieja) gsap.to(vieja, { opacity: 0, duration: .2, onComplete: function () { vieja.remove(); } });
    esc = el('g', {}, $('escena')); tl = gsap.timeline({ paused: true }); tl.timeScale(PRIM ? 1 : 1.45); var n = 0, e = E[i];
    try { (T[e.t] || T.frase).armar(esc, tl, function (k) { if (n++) tl.addPause(); tl.addLabel('b' + k); }, e); }
    catch (err) { errores.push('Escena ' + (i + 1) + ' (' + e.t + '): ' + err.message); if (window.console) console.error(err); }
    gsap.set(esc.querySelectorAll('[data-c]'), { transformOrigin: '50% 50%', smoothOrigin: false });
    gsap.fromTo(esc, { opacity: 0, scale: 1.04, transformOrigin: '960px 560px' }, { opacity: 1, scale: 1, duration: .3, delay: vieja ? .12 : 0, ease: 'power2.out' });
  }
  function irA(i) { cortar(); st.e = i; st.f = 0; gsap.set('#cam', { x: 0 }); $('flash').setAttribute('opacity', 0); armarEscena(i); barra(); if (st.play) setTimeout(function () { frase(0); }, 220); else subs(E[i].voz[0]); }
  function pausa() { st.play = false; MUSICA.pausa(); cortar(); if (tl) tl.pause(); barra(); }
  function seguir() { st.play = true; MUSICA.seguir(); var k = st.f; tl.pause(); if (tl.labels['b' + k] != null) tl.seek('b' + k); frase(k); }
  $('go').onclick = function () { $('ui').remove(); $('ctl').classList.add('ver'); setTimeout(function () { $('ctl').classList.remove('ver'); }, 2500); st.play = true; AUD.play().catch(function () {}); MUSICA.iniciar(); irA(0); };
  $('mus').onclick = function () { $('mus').style.opacity = MUSICA.alternar() ? 1 : .4; };
  $('pp').onclick = function () { st.play ? pausa() : seguir(); };
  $('ant').onclick = function () { irA(Math.max(0, st.e - (st.f <= 1 ? 1 : 0))); };
  $('sig').onclick = function () { if (st.e < E.length - 1) irA(st.e + 1); };
  function apagar() { if (st.play) pausa(); else cortar(); }
  window.addEventListener('pagehide', apagar); window.addEventListener('beforeunload', apagar);
  document.addEventListener('visibilitychange', function () { if (document.hidden) apagar(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') apagar(); if (e.key === ' ') { e.preventDefault(); st.play ? pausa() : seguir(); } });
  window.addEventListener('message', function (e) { if (e.data && e.data.tipo === 'wave-clase-stop') apagar(); });
  window.LECCION = { E: E, irA: irA, tl: function () { return tl; }, errores: errores };
})();
