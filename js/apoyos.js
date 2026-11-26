// Accesibilidad global (letra, contraste, animación) + dictado por voz junto a los campos de respuesta.
// La lectura en voz alta vive dentro del visor de PDF (js/visor-pdf.js), no acá.
(function () {
  var KEY = 'wave_accesibilidad';
  var A = { letra: 0, contraste: 0, sinAnim: false, deAUna: false, comprobar: false, sinCrono: false }; // contraste: 0 normal, 1 más alto, 2 más suave
  try { Object.assign(A, JSON.parse(localStorage.getItem(KEY) || '{}')); } catch (e) {}
  var raiz = document.documentElement;
  var FILTRO = { 1: 'contrast(1.35) saturate(1.1)', 2: 'contrast(0.85)' };

  function aplicar() {
    raiz.classList.toggle('ap-letra-1', A.letra === 1);
    raiz.classList.toggle('ap-letra-2', A.letra === 2);
    raiz.classList.toggle('ap-contraste-1', A.contraste === 1);
    raiz.classList.toggle('ap-contraste-2', A.contraste === 2);
    raiz.classList.toggle('ap-sin-anim', !!A.sinAnim);
    iframes();
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
          if (d && Object.keys(d).length) {
            A.letra = d.letra || 0; A.contraste = typeof d.contraste === 'number' ? d.contraste : (d.contraste ? 1 : 0); A.sinAnim = !!d.sinAnim;
            A.deAUna = !!d.deAUna; A.comprobar = !!d.comprobar; A.sinCrono = !!d.sinCrono;
            try { localStorage.setItem(KEY, JSON.stringify(A)); } catch (e) {}
            aplicar();
          }
        });
      });
    } catch (e) {}
  }

  // Dentro de las clases y actividades interactivas (iframes) también se aplica
  function iframes() {
    document.querySelectorAll('iframe').forEach(function (f) {
      function poner() {
        try {
          var d = f.contentDocument; if (!d || !d.head) return;
          var s = d.getElementById('ap-estilo');
          if (A.sinAnim && !s) { s = d.createElement('style'); s.id = 'ap-estilo'; s.textContent = '*,*::before,*::after{animation:none!important;transition:none!important}'; d.head.appendChild(s); }
          if (!A.sinAnim && s) s.remove();
          d.documentElement.style.filter = FILTRO[A.contraste] || '';
        } catch (e) {}
      }
      poner();
      if (!f._apL) { f._apL = 1; f.addEventListener('load', poner); }
    });
  }

  // ---------- Dictado por voz: el 🎤 está siempre junto a los campos donde se escribe una respuesta ----------
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition, rec = null, micActivo = null;
  function candidatos() {
    return Array.prototype.slice.call(document.querySelectorAll('textarea, input[type=text], input:not([type])')).filter(function (e) {
      return !e._apMic && !e.closest('.ap-panel-fondo, .wvp-chat, .wt-cuerpo') && !e.classList.contains('mt-hueco') && !e.classList.contains('mt-celda');
    });
  }
  function decir(txt, fin) {
    var ss = window.speechSynthesis;
    if (!ss) return fin();
    var hecho = false, f = function () { if (!hecho) { hecho = true; fin(); } };
    try {
      ss.cancel();
      var u = new SpeechSynthesisUtterance(txt); u.lang = 'es-AR';
      var vs = ss.getVoices() || [], v = vs.filter(function (x) { return /^es-AR/i.test(x.lang); })[0] || vs.filter(function (x) { return /^es/i.test(x.lang); })[0];
      if (v) u.voice = v;
      u.onend = f; u.onerror = f; ss.speak(u);
      setTimeout(f, 2500);
    } catch (e) { f(); }
  }
  function dictadoUI() {
    if (!SR) return;
    candidatos().forEach(function (c) {
      // En la lección interactiva (ejemplos y prácticas con muchas casillas chicas) el micrófono va chiquito, adentro de la casilla: no desarma el dibujo
      var mini = !!c.closest('.li2');
      var b = document.createElement('button'); b.type = 'button'; b.className = 'ap-mic' + (mini ? ' mini' : ''); b.textContent = mini ? '🎤' : '🎤 Dictar respuesta'; if (mini) c.classList.add('ap-con-mic'); b.title = 'Hablá y se escribe tu respuesta'; b.setAttribute('aria-label', 'Dictar respuesta con la voz');
      c._apMic = true;
      b.onclick = function () { dictar(c, b); };
      c.insertAdjacentElement('afterend', b);
    });
  }
  // Campos de número (ejemplos y ejercicios de la lección, cuentas): lo dictado reemplaza lo que había y se pasa a cifras
  function esNumero(c) { return /numeric|decimal/.test(c.inputMode || c.getAttribute('inputmode') || ''); }
  var NUM = { cero: 0, un: 1, uno: 1, una: 1, dos: 2, tres: 3, cuatro: 4, cinco: 5, seis: 6, siete: 7, ocho: 8, nueve: 9, diez: 10, once: 11, doce: 12, trece: 13, catorce: 14, quince: 15, dieciseis: 16, diecisiete: 17, dieciocho: 18, diecinueve: 19, veinte: 20, veintiun: 21, veintiuno: 21, veintidos: 22, veintitres: 23, veinticuatro: 24, veinticinco: 25, veintiseis: 26, veintisiete: 27, veintiocho: 28, veintinueve: 29, treinta: 30, cuarenta: 40, cincuenta: 50, sesenta: 60, setenta: 70, ochenta: 80, noventa: 90, cien: 100, ciento: 100, doscientos: 200, trescientos: 300, cuatrocientos: 400, quinientos: 500, seiscientos: 600, setecientos: 700, ochocientos: 800, novecientos: 900 };
  function aNumero(t) {
    var s = String(t).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim();
    var d = s.replace(/(\d)[\s.](?=\d{3}\b)/g, '$1');
    if (/^[\d\s,\/]+$/.test(d)) return d.replace(/\s+/g, '');
    var tot = 0, cur = 0, ok = false;
    s.split(/[\s-]+/).forEach(function (w) {
      if (w === 'y' || w === 'con' || !w) return;
      if (/^\d+$/.test(w)) { cur += Number(w); ok = true; }
      else if (NUM[w] != null) { cur += NUM[w]; ok = true; }
      else if (w === 'mil') { cur = (cur || 1) * 1000; ok = true; if (tot % 1e6 === 0 && tot) { tot += cur; cur = 0; } }
      else if (w === 'millon' || w === 'millones') { tot += (cur || 1) * 1e6; cur = 0; ok = true; }
    });
    return ok ? String(tot + cur) : t.trim();
  }
  function dictar(campo, btn) {
    var estabaEste = micActivo === btn;
    if (micActivo) { try { rec.stop(); } catch (e) {} }
    if (estabaEste) return;
    var cerrado = false, r = new SR(); rec = r; r.lang = 'es-AR'; r.interimResults = false; r.continuous = false;
    r.onresult = function (ev) {
      var t = ''; for (var i = ev.resultIndex; i < ev.results.length; i++) t += ev.results[i][0].transcript;
      campo.value = esNumero(campo) ? aNumero(t) : (campo.value ? campo.value + ' ' : '') + t.trim();
      campo.dispatchEvent(new Event('input', { bubbles: true }));
    };
    r.onend = function () {
      if (cerrado) return; cerrado = true;
      btn.classList.remove('on'); btn.textContent = btn.classList.contains('mini') ? '🎤' : '🎤 Dictar respuesta'; if (micActivo === btn) micActivo = null;
      decir('Listo', function () {});
    };
    r.onerror = function () { r.onend(); };
    micActivo = btn; btn.classList.add('on'); btn.textContent = btn.classList.contains('mini') ? '🔊' : '🔊 Te escucho…';
    // primero habla ("Te escucho, hablá") y recién después abre el micrófono, para que no se grabe a sí misma
    decir('Te escucho, hablá', function () {
      if (micActivo !== btn || cerrado) return;
      btn.textContent = '● Escuchando… tocá para terminar';
      try { r.start(); } catch (e) { r.onend(); }
    });
  }

  // ---------- Botón y ventana "Accesibilidad": solo lo global ----------
  function panel() {
    var f = document.createElement('div'); f.className = 'ap-panel-fondo';
    f.innerHTML = '<div class="ap-panel" role="dialog" aria-label="Accesibilidad"><h2>Accesibilidad</h2><p class="ap-sub">Cambios para toda la pantalla. Se guardan para la próxima vez.</p>' +
      '<div class="ap-op"><div><b>Tamaño de letra</b><br><select id="ap-letra"><option value="0">Normal</option><option value="1">Grande</option><option value="2">Muy grande</option></select></div></div>' +
      '<div class="ap-op"><div><b>Contraste</b><br><select id="ap-contraste"><option value="0">Normal</option><option value="1">Más alto</option><option value="2">Más suave</option></select></div></div>' +
      '<label class="ap-op"><input type="checkbox" id="ap-anim"><div><b>Menos animación</b><span>Quita movimientos y transiciones, también dentro de las clases.</span></div></label>' +
      '<label class="ap-op"><input type="checkbox" id="ap-sonido"><div><b>Sin sonidos</b><span>Apaga los sonidos de las actividades y del examen.</span></div></label>' +
      '<button class="ap-cerrar" type="button">Listo</button></div>';
    document.body.appendChild(f);
    var l = f.querySelector('#ap-letra'), c = f.querySelector('#ap-contraste'), a = f.querySelector('#ap-anim');
    l.value = String(A.letra); c.value = String(A.contraste); a.checked = !!A.sinAnim;
    l.onchange = function () { A.letra = +l.value; guardar(); aplicar(); };
    c.onchange = function () { A.contraste = +c.value; guardar(); aplicar(); };
    a.onchange = function () { A.sinAnim = a.checked; guardar(); aplicar(); };
    var so = f.querySelector('#ap-sonido'); so.checked = !!A.sinSonido; so.onchange = function () { A.sinSonido = so.checked; guardar(); aplicar(); };
    f.querySelector('.ap-cerrar').onclick = function () { f.remove(); };
    f.onclick = function (e) { if (e.target === f) f.remove(); };
  }

  function iniciar() {
    var b = document.createElement('button'); b.className = 'ap-fab'; b.type = 'button'; b.textContent = 'Accesibilidad'; b.onclick = panel; document.body.appendChild(b);
    aplicar(); cargarRemoto(); dictadoUI();
    new MutationObserver(function () { dictadoUI(); if (A.sinAnim || A.contraste) iframes(); }).observe(document.body, { childList: true, subtree: true });
  }
  window.WaveApoyos = { get: function (k) { return A[k]; }, set: function (k, v) { A[k] = v; guardar(); aplicar(); } };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
