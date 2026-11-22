// Ajustes opcionales de accesibilidad (nada viene activado). Se guardan por dispositivo y, si se puede, en students.apoyos.
(function () {
  var KEY = 'wave_apoyos';
  var DEF = { voz: false, letra: 0, contraste: false, sinAnim: false, dictado: false, velocidad: 1 };
  var A = Object.assign({}, DEF);
  try { Object.assign(A, JSON.parse(localStorage.getItem(KEY) || '{}')); } catch (e) {}
  var raiz = document.documentElement;

  function aplicar() {
    raiz.classList.toggle('ap-letra-1', A.letra === 1);
    raiz.classList.toggle('ap-letra-2', A.letra === 2);
    raiz.classList.toggle('ap-contraste', !!A.contraste);
    raiz.classList.toggle('ap-sin-anim', !!A.sinAnim);
    lectorUI(); dictadoUI(); iframes();
  }
  function guardar() {
    try { localStorage.setItem(KEY, JSON.stringify(A)); } catch (e) {}
    try {
      var sb = window.Wave && window.Wave.sb;
      if (sb) sb.auth.getSession().then(function (r) {
        var u = r.data && r.data.session && r.data.session.user;
        if (u) sb.from('students').update({ apoyos: A }).eq('profile_id', u.id).then(function () {}, function () {});
      });
    } catch (e) {}
  }
  function cargarRemoto() {
    try {
      var sb = window.Wave && window.Wave.sb; if (!sb) return;
      sb.auth.getSession().then(function (r) {
        var u = r.data && r.data.session && r.data.session.user; if (!u) return;
        sb.from('students').select('apoyos').eq('profile_id', u.id).maybeSingle().then(function (q) {
          var d = q && q.data && q.data.apoyos;
          if (d && Object.keys(d).length) { Object.assign(A, d); try { localStorage.setItem(KEY, JSON.stringify(A)); } catch (e) {} aplicar(); }
        });
      });
    } catch (e) {}
  }

  // ---------- Menos animación dentro de las clases/actividades (iframes) ----------
  function iframes() {
    document.querySelectorAll('iframe').forEach(function (f) {
      function poner() {
        try {
          var d = f.contentDocument; if (!d || !d.head) return;
          var s = d.getElementById('ap-estilo');
          if (A.sinAnim && !s) { s = d.createElement('style'); s.id = 'ap-estilo'; s.textContent = '*,*::before,*::after{animation:none!important;transition:none!important}'; d.head.appendChild(s); }
          if (!A.sinAnim && s) s.remove();
          if (A.contraste) d.documentElement.style.filter = 'contrast(1.35) saturate(1.1)'; else d.documentElement.style.filter = '';
        } catch (e) {}
      }
      poner();
      if (!f._apL) { f._apL = 1; f.addEventListener('load', poner); }
    });
  }

  // ---------- Lectura en voz alta con el fragmento resaltado ----------
  var hablando = false, pausado = false, cola = [], idx = 0, vozES = null;
  function elegirVoz() {
    var vs = speechSynthesis.getVoices();
    vozES = vs.filter(function (v) { return /^es[-_]AR/i.test(v.lang); })[0] || vs.filter(function (v) { return /^es/i.test(v.lang); })[0] || null;
  }
  function nodosTexto(raizEl) {
    var w = document.createTreeWalker(raizEl, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentElement; if (!p) return NodeFilter.FILTER_REJECT;
        if (p.closest('script,style,noscript,textarea,input,select,button,.ap-lector,.ap-fab,.ap-panel-fondo,[aria-hidden="true"],[hidden]')) return NodeFilter.FILTER_REJECT;
        if (p.getClientRects().length === 0) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var out = [], n; while ((n = w.nextNode())) out.push(n); return out;
  }
  function armarCola() {
    var cont = document.getElementById('vista') || document.body;
    var nodos = nodosTexto(cont), sel = window.getSelection && String(window.getSelection()).trim();
    var texto = '', mapa = [];
    nodos.forEach(function (n) { mapa.push({ n: n, ini: texto.length }); texto += n.nodeValue.replace(/\s+/g, ' ') + ' '; });
    var partes = [], re = /[^.!?¿¡:;\n]+[.!?:;]*/g, m;
    while ((m = re.exec(texto))) { if (m[0].trim().length > 1) partes.push({ t: m[0].trim(), ini: m.index, fin: m.index + m[0].length }); }
    if (sel) partes = sel.split(/(?<=[.!?])\s+/).map(function (s) { return { t: s, ini: -1, fin: -1 }; });
    function aRango(p) {
      if (p.ini < 0 || !window.CSS || !CSS.highlights) return null;
      var r = document.createRange(), a = null, b = null;
      for (var i = 0; i < mapa.length; i++) {
        var o = mapa[i], largo = o.n.nodeValue.replace(/\s+/g, ' ').length;
        if (a === null && p.ini < o.ini + largo + 1) { a = [o.n, Math.max(0, Math.min(p.ini - o.ini, o.n.nodeValue.length))]; }
        if (p.fin <= o.ini + largo + 1) { b = [o.n, Math.max(0, Math.min(p.fin - o.ini, o.n.nodeValue.length))]; break; }
      }
      if (!a || !b) return null;
      try { r.setStart(a[0], a[1]); r.setEnd(b[0], b[1]); return r; } catch (e) { return null; }
    }
    return partes.map(function (p) { return { t: p.t, r: aRango(p) }; });
  }
  function marcar(r) {
    if (!window.CSS || !CSS.highlights) return;
    if (r) { CSS.highlights.set('ap-leyendo', new Highlight(r)); var el = r.startContainer.parentElement; if (el && el.scrollIntoView) el.scrollIntoView({ block: 'center', behavior: A.sinAnim ? 'auto' : 'smooth' }); }
    else CSS.highlights.delete('ap-leyendo');
  }
  function decir() {
    if (idx >= cola.length) { parar(); return; }
    var it = cola[idx]; marcar(it.r);
    var u = new SpeechSynthesisUtterance(it.t);
    u.lang = (vozES && vozES.lang) || 'es-AR'; if (vozES) u.voice = vozES; u.rate = A.velocidad || 1;
    u.onend = function () { if (hablando && !pausado) { idx++; decir(); } };
    u.onerror = function () { if (hablando && !pausado) { idx++; decir(); } };
    speechSynthesis.speak(u);
  }
  function leer() {
    if (!('speechSynthesis' in window)) { alert('Este navegador no tiene lectura en voz alta.'); return; }
    parar(); elegirVoz(); cola = armarCola(); if (!cola.length) return;
    hablando = true; pausado = false; idx = 0; actualizarBtns(); decir();
  }
  function pausa() {
    if (!hablando) return;
    if (pausado) { pausado = false; speechSynthesis.cancel(); decir(); } else { pausado = true; speechSynthesis.cancel(); }
    actualizarBtns();
  }
  function parar() { hablando = false; pausado = false; try { speechSynthesis.cancel(); } catch (e) {} marcar(null); actualizarBtns(); }
  var barra = null;
  function actualizarBtns() {
    if (!barra) return;
    barra.querySelector('.ap-leer').textContent = hablando ? '↺ Desde el inicio' : '🔊 Escuchar';
    barra.querySelector('.ap-pausa').textContent = pausado ? '▶ Seguir' : '⏸ Pausa';
    barra.querySelector('.ap-pausa').style.display = hablando ? '' : 'none';
    barra.querySelector('.ap-stop').style.display = hablando ? '' : 'none';
  }
  function lectorUI() {
    if (A.voz && !barra) {
      barra = document.createElement('div'); barra.className = 'ap-lector'; barra.setAttribute('role', 'region'); barra.setAttribute('aria-label', 'Lectura en voz alta');
      barra.innerHTML = '<button type="button" class="ap-leer">🔊 Escuchar</button><button type="button" class="sec ap-pausa" style="display:none">⏸ Pausa</button><button type="button" class="sec ap-stop" style="display:none">■ Parar</button>';
      barra.querySelector('.ap-leer').onclick = leer; barra.querySelector('.ap-pausa').onclick = pausa; barra.querySelector('.ap-stop').onclick = parar;
      document.body.appendChild(barra);
    } else if (!A.voz && barra) { parar(); barra.remove(); barra = null; }
  }

  // ---------- Dictado por voz ----------
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition, rec = null, micActivo = null;
  function candidatos() {
    return Array.prototype.slice.call(document.querySelectorAll('textarea, input[type=text]')).filter(function (e) {
      return !e.closest('.ap-panel-fondo') && !e.classList.contains('mt-hueco') && !e.classList.contains('mt-celda') && !e._apMic;
    });
  }
  function dictadoUI() {
    document.querySelectorAll('.ap-mic').forEach(function (b) { if (!A.dictado || !SR) { if (b._campo) b._campo._apMic = false; b.remove(); } });
    if (!A.dictado || !SR) return;
    candidatos().forEach(function (c) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'ap-mic'; b.textContent = '🎤'; b.title = 'Dictar con la voz'; b.setAttribute('aria-label', 'Dictar con la voz');
      b._campo = c; c._apMic = true;
      b.onclick = function () { dictar(c, b); };
      c.insertAdjacentElement('afterend', b);
    });
  }
  function dictar(campo, btn) {
    if (micActivo) { try { rec.stop(); } catch (e) {} if (micActivo === btn) return; }
    rec = new SR(); rec.lang = 'es-AR'; rec.interimResults = false; rec.continuous = false;
    rec.onresult = function (ev) {
      var t = ''; for (var i = ev.resultIndex; i < ev.results.length; i++) t += ev.results[i][0].transcript;
      campo.value = (campo.value ? campo.value + ' ' : '') + t.trim();
      campo.dispatchEvent(new Event('input', { bubbles: true }));
    };
    rec.onend = function () { btn.classList.remove('on'); btn.textContent = '🎤'; if (micActivo === btn) micActivo = null; };
    rec.onerror = function () { rec.onend(); };
    micActivo = btn; btn.classList.add('on'); btn.textContent = '● Escuchando…';
    try { rec.start(); } catch (e) { rec.onend(); }
  }

  // ---------- Panel para elegir ----------
  function panel() {
    var f = document.createElement('div'); f.className = 'ap-panel-fondo';
    f.innerHTML = '<div class="ap-panel" role="dialog" aria-label="Ajustes de lectura y pantalla"><h2>Ajustes para estudiar a tu manera</h2><p class="ap-sub">Todo es opcional y está apagado hasta que lo elijas. Podés cambiarlo cuando quieras.</p>' +
      op('voz', 'Lectura en voz alta', 'Aparece un botón para escuchar la lección y se marca lo que se va leyendo.') +
      '<div class="ap-op"><div><b>Tamaño de letra</b><span>Agranda todo el contenido.</span><br><select id="ap-letra"><option value="0">Normal</option><option value="1">Grande</option><option value="2">Muy grande</option></select></div></div>' +
      op('contraste', 'Más contraste', 'Colores más marcados y bordes más fuertes.') +
      op('sinAnim', 'Menos animación', 'Quita movimientos y transiciones de la pantalla y de las clases.') +
      op('dictado', 'Dictado por voz', 'Aparece un 🎤 junto a las respuestas escritas para hablar en vez de tipear.') +
      '<div class="ap-op"><div><b>Velocidad de la voz</b><br><select id="ap-vel"><option value="0.8">Lenta</option><option value="1">Normal</option><option value="1.2">Rápida</option></select></div></div>' +
      '<button class="ap-cerrar" type="button">Listo</button></div>';
    document.body.appendChild(f);
    f.querySelectorAll('input[data-k]').forEach(function (i) { i.checked = !!A[i.dataset.k]; i.onchange = function () { A[i.dataset.k] = i.checked; guardar(); aplicar(); }; });
    var sl = f.querySelector('#ap-letra'); sl.value = String(A.letra); sl.onchange = function () { A.letra = +sl.value; guardar(); aplicar(); };
    var sv = f.querySelector('#ap-vel'); sv.value = String(A.velocidad || 1); sv.onchange = function () { A.velocidad = +sv.value; guardar(); };
    f.querySelector('.ap-cerrar').onclick = function () { f.remove(); };
    f.onclick = function (e) { if (e.target === f) f.remove(); };
  }
  function op(k, t, d) { return '<label class="ap-op"><input type="checkbox" data-k="' + k + '"><div><b>' + t + '</b><span>' + d + '</span></div></label>'; }

  function iniciar() {
    var b = document.createElement('button'); b.className = 'ap-fab'; b.type = 'button'; b.textContent = 'Ajustes de lectura'; b.onclick = panel; document.body.appendChild(b);
    aplicar(); cargarRemoto();
    new MutationObserver(function () { if (A.dictado) dictadoUI(); if (A.sinAnim || A.contraste) iframes(); }).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
  window.WaveApoyos = { get: function () { return A; }, leer: leer, parar: parar };
})();
