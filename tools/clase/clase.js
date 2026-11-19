/* REPRODUCTOR DE CLASES ANIMADAS DE WAVE ACADEMY
   Toma window.CLASE (de tools/clase/convertir.mjs) y la reproduce como un video: escenas animadas + voz + subtítulos palabra por palabra.
   Voz: si la escena trae "audio" (ElevenLabs, ver voz.mjs) usa ese archivo con sus tiempos exactos;
   si no, usa la voz gratis del dispositivo (speechSynthesis). Al terminar avisa a la plataforma con postMessage. */
(function () {
  var C = window.CLASE, E = C.escenas, app = document.getElementById('app');
  var st = { e: 0, f: -1, play: false, gen: 0 }, audio = null, vozDisp = null;

  function S(t) {
    return String(t == null ? '' : t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/&lt;(\/?)(b|i|sub|sup|br)&gt;/g, '<$1$2>');
  }
  function di(i, html, cls, tag) { tag = tag || 'div'; return '<' + tag + ' class="' + (cls || '') + '" data-i="' + i + '">' + html + '</' + tag + '>'; }

  // ---------- cómo se dibuja cada tipo de escena (data-i = con qué frase aparece) ----------
  var V = {
    portada: function (e) { return '<div class="ola" data-i="0">🌊</div>' + di(0, S(e.titulo), 'grande') + di(1, S(e.sub), 'sub'); },
    seccion: function (e) { return di(0, 'Nuevo tema', 'etq') + di(0, S(e.titulo), 'grande'); },
    lista: function (e) { return di(0, S(e.titulo), 'etq') + '<div class="lista">' + e.items.map(function (x, j) { return di(j + 1, '<i>' + (j + 1) + '</i><span>' + S(x) + '</span>', 'item'); }).join('') + '</div>'; },
    definicion: function (e) { return di(0, 'Definición', 'etq') + '<div style="text-align:center">' + di(0, S(e.palabra), 'palabra') + '</div>' + di(1, S(e.texto), 'tarjeta'); },
    parrafo: function (e) { return di(0, S(e.texto), 'tarjeta'); },
    importante: function (e) { return di(0, '<span class="ico">' + (e.icono || '⚠️') + '</span><h3>' + S(e.titulo) + '</h3>' + S(e.texto), 'tarjeta alerta'); },
    tabla: function (e) {
      var h = '<table class="tabla"><tr>' + e.columnas.map(function (c) { return '<th>' + S(c) + '</th>'; }).join('') + '</tr>';
      e.filas.forEach(function (f, r) { h += '<tr data-i="' + (r + 1) + '">' + f.map(function (c) { return '<td>' + S(c) + '</td>'; }).join('') + '</tr>'; });
      return di(0, S(e.titulo), 'etq') + h + '</table>' + (e.nota ? di(e.filas.length + 1, S(e.nota), 'sub') : '');
    },
    pasos: function (e) { return di(0, S(e.etq || 'Ejemplo') + ' · ' + S(e.titulo), 'etq') + '<div class="lista">' + e.items.map(function (x, j) { return di(j + 1, '<i>' + (j + 1) + '</i><span>' + S(x) + '</span>', 'item'); }).join('') + '</div>'; },
    ojo: function (e) { return di(0, '👀 ' + S(e.titulo), 'etq') + '<div class="lista">' + e.items.map(function (x, j) { return di(j + 1, '<i>✗</i><span>' + S(x) + '</span>', 'item mal'); }).join('') + '</div>'; },
    resumen: function (e) { return di(0, S(e.titulo), 'etq') + '<div class="res">' + e.items.map(function (x, j) { return di(j + 1, '<h3>' + S(x.titulo) + '</h3>' + S(x.texto), 'tarjeta'); }).join('') + '</div>'; },
    cierre: function (e) { return '<div class="ola" data-i="0">🏆</div>' + di(0, S(e.titulo), 'grande') + di(0, S(e.sub), 'sub'); }
  };

  // ---------- pantalla ----------
  function base() {
    app.innerHTML = '<div class="barra">' + E.map(function (_, i) { return '<i data-ir="' + i + '"><b></b></i>'; }).join('') + '</div>' +
      '<div class="subs" id="subs"></div><div class="escena" id="esc"></div>' +
      '<div class="control"><button class="cb" id="ant" aria-label="Anterior">⏮</button><button class="cb play" id="pp" aria-label="Pausa">❚❚</button><button class="cb" id="sig" aria-label="Siguiente">⏭</button></div>' +
      '<div class="inicio" id="ini"><div class="ola">🌊</div><div class="grande" style="font-size:1.8rem">' + S(C.titulo) + '</div><button class="btn" id="go">▶ Empezar clase</button></div>';
    document.getElementById('go').onclick = function () { document.getElementById('ini').remove(); st.play = true; irA(0); };
    document.getElementById('pp').onclick = function () { st.play ? pausa() : seguir(); };
    document.getElementById('ant').onclick = function () { irA(Math.max(0, st.e - (st.f <= 0 ? 1 : 0))); };
    document.getElementById('sig').onclick = function () { if (st.e < E.length - 1) irA(st.e + 1); };
    [].forEach.call(app.querySelectorAll('[data-ir]'), function (b) { b.onclick = function () { irA(+b.dataset.ir); }; });
  }
  function barra() {
    [].forEach.call(app.querySelectorAll('.barra b'), function (b, i) {
      b.style.width = i < st.e ? '100%' : i > st.e ? '0' : Math.round((st.f + 1) / E[i].voz.length * 100) + '%';
    });
    document.getElementById('pp').textContent = st.play ? '❚❚' : '▶';
  }
  function mostrar(k) { [].forEach.call(document.querySelectorAll('#esc [data-i]'), function (el) { el.classList.toggle('on', +el.dataset.i <= k); }); }
  function subs(txt) { document.getElementById('subs').innerHTML = '<div>' + txt.split(' ').map(function (w) { return '<span>' + S(w) + '</span>'; }).join(' ') + '</div>'; }
  function marcar(w) { [].forEach.call(document.querySelectorAll('#subs span'), function (s, i) { s.className = i < w ? 'ya' : i === w ? 'ahora' : ''; }); }

  // ---------- voz ----------
  function cortar() { st.gen++; if (audio) { audio.pause(); } if (window.speechSynthesis) speechSynthesis.cancel(); }
  function elegirVoz() {
    if (!window.speechSynthesis) return null;
    var vs = speechSynthesis.getVoices().filter(function (v) { return /^es/i.test(v.lang); });
    var pref = function (re) { return vs.filter(function (v) { return re.test(v.lang + ' ' + v.name); })[0]; };
    return pref(/es-AR/i) || pref(/natural|online|google/i) || pref(/es-(419|MX|US)/i) || vs[0] || null;
  }
  // frase k de la escena con voz del dispositivo; marca palabras por evento o por estimación
  function decirDispositivo(txt, g, fin) {
    var u = new SpeechSynthesisUtterance(txt), n = txt.split(' ').length, t0 = Date.now(), porEvento = false, iv;
    u.lang = 'es-AR'; if (vozDisp) u.voice = vozDisp; u.rate = 1;
    u.onboundary = function (ev) { if (ev.name !== 'word' && ev.name) return; porEvento = true; marcar(txt.slice(0, ev.charIndex).split(' ').length - 1); };
    iv = setInterval(function () { if (g !== st.gen) return clearInterval(iv); if (!porEvento) marcar(Math.min(n - 1, Math.floor((Date.now() - t0) / 330))); }, 80);
    u.onend = u.onerror = function () { clearInterval(iv); if (g === st.gen) { marcar(n); fin(); } };
    speechSynthesis.speak(u);
  }
  function decirSinVoz(txt, g, fin) { // último recurso: solo subtítulos con tiempo estimado
    var n = txt.split(' ').length, w = 0, iv = setInterval(function () { if (g !== st.gen) return clearInterval(iv); marcar(w++); if (w > n) { clearInterval(iv); fin(); } }, 330);
  }

  function frase(k) { // reproduce la frase k de la escena actual
    var e = E[st.e], g = st.gen;
    if (k >= e.voz.length) return siguienteEscena();
    st.f = k; mostrar(k); subs(e.voz[k]); barra();
    var sigue = function () { if (g === st.gen && st.play) setTimeout(function () { if (g === st.gen && st.play) frase(k + 1); }, 250); };
    if (e.audio) return; // con audio, el reloj del archivo maneja todo (ver tic)
    if (window.speechSynthesis && (vozDisp || (vozDisp = elegirVoz()))) decirDispositivo(e.voz[k], g, sigue);
    else decirSinVoz(e.voz[k], g, sigue);
  }
  function tic(g) { // modo audio: sincroniza frase y palabra con el tiempo del archivo
    if (g !== st.gen || !audio) return;
    var e = E[st.e], t = audio.currentTime, A = e.audio.frases, k = 0;
    while (k + 1 < A.length && t >= A[k + 1].t0) k++;
    if (k !== st.f) { st.f = k; mostrar(k); subs(e.voz[k]); barra(); }
    var w = 0, W = A[k].w || []; while (w + 1 < W.length && t >= W[w + 1]) w++;
    marcar(t >= A[k].t1 ? 999 : w);
    if (!audio.ended) requestAnimationFrame(function () { tic(g); });
  }
  function arrancarEscena(desde) {
    var e = E[st.e], g = st.gen;
    if (!e.audio) return frase(desde || 0);
    audio = new Audio(e.audio.src); audio.currentTime = desde ? e.audio.frases[desde].t0 : 0;
    audio.onended = function () { if (g === st.gen) setTimeout(function () { if (g === st.gen && st.play) siguienteEscena(); }, 400); };
    st.f = -1; audio.play().catch(function () { pausa(); }); tic(g);
  }
  function irA(i) {
    cortar(); st.e = i; st.f = -1;
    var esc = document.getElementById('esc'); esc.innerHTML = (V[E[i].t] || V.parrafo)(E[i]);
    esc.style.animation = 'none'; void esc.offsetWidth; esc.style.animation = '';
    barra(); if (st.play) arrancarEscena(0); else { mostrar(0); subs(E[i].voz[0] || ''); }
  }
  function siguienteEscena() {
    if (st.e < E.length - 1) return irA(st.e + 1);
    st.play = false; barra(); marcar(999);
    try { parent.postMessage({ tipo: 'wave-clase-fin', puntaje: 100 }, '*'); } catch (_) {}
  }
  function pausa() { st.play = false; if (audio && E[st.e].audio) { st.gen++; audio.pause(); } else cortar(); barra(); }
  function seguir() {
    st.play = true;
    if (audio && E[st.e].audio && !audio.ended) { var g = ++st.gen; audio.onended = function () { if (g === st.gen) setTimeout(function () { if (g === st.gen && st.play) siguienteEscena(); }, 400); }; audio.play(); tic(g); }
    else arrancarEscena(Math.max(0, st.f));
    barra();
  }

  if (window.speechSynthesis) speechSynthesis.onvoiceschanged = function () { vozDisp = elegirVoz(); };
  base(); irA(0);
})();
