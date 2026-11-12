// Visor de PDF reutilizable (PDF.js, igual que el de Indómita Love Club).
// Uso: WaveVisor.abrirPdf({ titulo: 'Clase 1', url: async function (descarga) { return 'https://...'; }, descargable: true })
// "url" devuelve el enlace temporal del archivo; cada panel decide cómo conseguirlo.
(function () {
  var LIB = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js';
  var WORKER = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
  var promesaLib = null;

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function cargarLib() {
    if (window.pdfjsLib) return Promise.resolve();
    if (promesaLib) return promesaLib;
    promesaLib = new Promise(function (ok, mal) {
      var s = document.createElement('script');
      s.src = LIB;
      s.onload = function () { window.pdfjsLib.GlobalWorkerOptions.workerSrc = WORKER; ok(); };
      s.onerror = function () { promesaLib = null; mal(new Error('No se pudo cargar el visor de PDF. Revisá tu conexión.')); };
      document.head.appendChild(s);
    });
    return promesaLib;
  }

  function abrirPdf(opts) {
    var pdf = null, total = 0, n = 1, zoom = 1, tarea = null, ficha = 0, cerrado = false, avisado = false;

    var el = document.createElement('div');
    el.className = 'wvp';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', 'Visor de PDF');
    var conChat = typeof opts.chat === 'function';
    el.innerHTML =
      '<div class="wvp-caja' + (conChat ? ' con-chat' : '') + '">' +
       '<div class="wvp-doc">' +
        '<div class="wvp-barra">' +
          '<b class="wvp-titulo">' + esc(opts.titulo || 'PDF') + '</b>' +
          '<div class="wvp-ctrl wvp-pag">' +
            '<button type="button" class="wvp-b" data-v="ant" aria-label="Página anterior">‹</button>' +
            '<span class="wvp-num">–</span>' +
            '<button type="button" class="wvp-b" data-v="sig" aria-label="Página siguiente">›</button>' +
          '</div>' +
          '<div class="wvp-ctrl">' +
            '<button type="button" class="wvp-b" data-v="menos" aria-label="Alejar">−</button>' +
            '<button type="button" class="wvp-b wvp-ancho" data-v="ajustar" aria-label="Ajustar al ancho">Ajustar</button>' +
            '<button type="button" class="wvp-b" data-v="mas" aria-label="Acercar">+</button>' +
          '</div>' +
          (conChat ? '<button type="button" class="wvp-b wvp-bchat" data-v="chat">💬 Tutor</button>' : '') +
          (opts.descargable ? '<button type="button" class="wvp-b wvp-desc" data-v="bajar">⬇ Descargar</button>' : '') +
          '<button type="button" class="wvp-b wvp-x" data-v="cerrar" aria-label="Cerrar">✕</button>' +
        '</div>' +
        '<div class="wvp-cuerpo">' +
          '<div class="wvp-estado">Cargando PDF…</div>' +
          '<canvas class="wvp-canvas" hidden></canvas>' +
        '</div>' +
       '</div>' +
       (conChat ?
        '<aside class="wvp-chat" aria-label="Tutor">' +
          '<div class="wvp-chat-cab"><b>💬 Tutor Wave</b><small>Preguntale lo que no entiendas de este material</small>' +
            '<button type="button" class="wvp-chat-x" data-v="chat" aria-label="Cerrar chat">✕</button></div>' +
          '<div class="wvp-chat-msgs" aria-live="polite">' +
            '<div class="wvp-m bot">¡Hola! Soy tu tutor. Leí este material: preguntame lo que no te quede claro y lo vemos juntos.</div>' +
          '</div>' +
          '<div class="wvp-chat-rest" hidden></div>' +
          '<form class="wvp-chat-form"><textarea rows="1" maxlength="2000" placeholder="Escribí tu duda…" aria-label="Tu duda"></textarea>' +
            '<button type="submit" class="wvp-b wvp-env" aria-label="Enviar">➤</button></form>' +
        '</aside>' : '') +
      '</div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');

    var cuerpo = el.querySelector('.wvp-cuerpo');
    var canvas = el.querySelector('.wvp-canvas');
    var estado = el.querySelector('.wvp-estado');
    var num = el.querySelector('.wvp-num');
    var ctx = canvas.getContext('2d');

    function mostrarError(msg) {
      canvas.hidden = true;
      estado.hidden = false;
      estado.className = 'wvp-estado error';
      estado.textContent = msg;
    }

    function actualizarControles() {
      num.textContent = n + ' / ' + total;
      el.querySelector('[data-v="ant"]').disabled = n <= 1;
      el.querySelector('[data-v="sig"]').disabled = n >= total;
      el.querySelector('[data-v="menos"]').disabled = zoom <= 0.5;
      el.querySelector('[data-v="mas"]').disabled = zoom >= 3;
    }

    async function pintar() {
      if (!pdf || cerrado) return;
      var mia = ++ficha;
      if (tarea) { try { tarea.cancel(); } catch (e) { /* ya terminó */ } try { await tarea.promise; } catch (e) { /* cancelada */ } }
      if (mia !== ficha || cerrado) return;
      try {
        var pagina = await pdf.getPage(n);
        if (mia !== ficha || cerrado) return;
        var base = pagina.getViewport({ scale: 1 });
        var ancho = Math.max(200, cuerpo.clientWidth - 24);
        var escala = (ancho / base.width) * zoom;
        var dpr = Math.min(window.devicePixelRatio || 1, 2);
        var vp = pagina.getViewport({ scale: escala * dpr });
        canvas.width = vp.width;
        canvas.height = vp.height;
        canvas.style.width = Math.round(vp.width / dpr) + 'px';
        canvas.style.height = Math.round(vp.height / dpr) + 'px';
        tarea = pagina.render({ canvasContext: ctx, viewport: vp });
        await tarea.promise;
        cuerpo.scrollTo(0, 0);
        if (n === total && !avisado && opts.alTerminar) { avisado = true; try { opts.alTerminar(); } catch (e2) { /* nada */ } }
      } catch (e) {
        if (e && e.name === 'RenderingCancelledException') return;
        console.error(e);
        mostrarError('No se pudo mostrar esta página.');
      }
    }

    function ir(nueva) {
      nueva = Math.min(total, Math.max(1, nueva));
      if (nueva === n) return;
      n = nueva;
      actualizarControles();
      pintar();
    }
    function cambiarZoom(z) {
      zoom = Math.min(3, Math.max(0.5, Math.round(z * 100) / 100));
      actualizarControles();
      pintar();
    }

    async function descargar() {
      try {
        var u = await opts.url(true);
        var a = document.createElement('a');
        a.href = u; a.rel = 'noopener'; a.download = '';
        document.body.appendChild(a); a.click(); a.remove();
      } catch (e) { mostrarError(e.message || 'No se pudo descargar el archivo.'); }
    }

    function cerrar() {
      cerrado = true;
      if (tarea) { try { tarea.cancel(); } catch (e) { /* nada */ } }
      if (pdf) { try { pdf.destroy(); } catch (e) { /* nada */ } }
      document.removeEventListener('keydown', tecla);
      window.removeEventListener('resize', alCambiarTamano);
      document.body.classList.remove('wvp-abierto');
      el.remove();
    }

    function tecla(ev) {
      if (ev.target && /^(TEXTAREA|INPUT)$/.test(ev.target.tagName)) return;
      if (ev.key === 'Escape') cerrar();
      else if (ev.key === 'ArrowRight' || ev.key === 'PageDown') ir(n + 1);
      else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp') ir(n - 1);
    }
    var temporizador = null;
    function alCambiarTamano() { clearTimeout(temporizador); temporizador = setTimeout(pintar, 150); }

    // ---------- Chat con el tutor ----------
    var conv = null, enviando = false;
    if (conChat) {
      var msgs = el.querySelector('.wvp-chat-msgs');
      var form = el.querySelector('.wvp-chat-form');
      var campo = form.querySelector('textarea');
      var btnEnv = form.querySelector('.wvp-env');
      var rest = el.querySelector('.wvp-chat-rest');
      var agregar = function (clase, texto) {
        var d = document.createElement('div');
        d.className = 'wvp-m ' + clase;
        d.textContent = texto;
        msgs.appendChild(d);
        msgs.scrollTop = msgs.scrollHeight;
        return d;
      };
      campo.addEventListener('input', function () { campo.style.height = 'auto'; campo.style.height = Math.min(campo.scrollHeight, 120) + 'px'; });
      campo.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter' && !ev.shiftKey) { ev.preventDefault(); form.requestSubmit(); }
        ev.stopPropagation(); // no cambiar de página mientras escribe
      });
      form.addEventListener('submit', async function (ev) {
        ev.preventDefault();
        var t = campo.value.trim();
        if (!t || enviando) return;
        enviando = true; btnEnv.disabled = true;
        agregar('yo', t);
        campo.value = ''; campo.style.height = 'auto';
        var pensando = agregar('bot pensando', 'Pensando…');
        try {
          var r = await opts.chat(t, conv);
          conv = r.conversation_id || conv;
          pensando.className = 'wvp-m bot'; pensando.textContent = r.reply;
          if (typeof r.remaining === 'number') {
            rest.hidden = false;
            rest.textContent = r.remaining > 0 ? 'Te quedan ' + r.remaining + ' consultas hoy' : 'Esta fue tu última consulta de hoy';
          }
        } catch (e) {
          pensando.className = 'wvp-m bot error'; pensando.textContent = e.message || 'El tutor no pudo responder ahora.';
        }
        msgs.scrollTop = msgs.scrollHeight;
        enviando = false; btnEnv.disabled = false; campo.focus();
      });
    }

    el.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-v]');
      if (!b) { if (ev.target === el) cerrar(); return; }
      var v = b.getAttribute('data-v');
      if (v === 'cerrar') cerrar();
      else if (v === 'ant') ir(n - 1);
      else if (v === 'sig') ir(n + 1);
      else if (v === 'mas') cambiarZoom(zoom + 0.25);
      else if (v === 'menos') cambiarZoom(zoom - 0.25);
      else if (v === 'ajustar') cambiarZoom(1);
      else if (v === 'bajar') descargar();
      else if (v === 'chat') { el.classList.toggle('chat-abierto'); setTimeout(pintar, 50); if (el.classList.contains('chat-abierto')) { var c = el.querySelector('.wvp-chat textarea'); if (c) c.focus(); } }
    });
    document.addEventListener('keydown', tecla);
    window.addEventListener('resize', alCambiarTamano);

    // Deslizar con el dedo para cambiar de página (solo sin zoom)
    var x0 = null;
    cuerpo.addEventListener('touchstart', function (ev) { x0 = ev.touches.length === 1 ? ev.touches[0].clientX : null; }, { passive: true });
    cuerpo.addEventListener('touchend', function (ev) {
      if (x0 === null || zoom !== 1) return;
      var dx = ev.changedTouches[0].clientX - x0;
      x0 = null;
      if (Math.abs(dx) > 60) ir(n + (dx < 0 ? 1 : -1));
    }, { passive: true });

    (async function () {
      try {
        await cargarLib();
        var url = await opts.url(false);
        if (cerrado) return;
        pdf = await window.pdfjsLib.getDocument(url).promise;
        if (cerrado) { pdf.destroy(); return; }
        total = pdf.numPages;
        estado.hidden = true;
        canvas.hidden = false;
        actualizarControles();
        await pintar();
      } catch (e) {
        console.error(e);
        mostrarError((e && e.message && !/^(Missing|Invalid|Unexpected)/.test(e.message) ? e.message : 'No se pudo abrir el PDF. Probá de nuevo en unos minutos.'));
      }
    })();

    return { cerrar: cerrar };
  }

  window.WaveVisor = window.WaveVisor || {};
  window.WaveVisor.abrirPdf = abrirPdf;
})();
