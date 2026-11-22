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
        '<div class="wvp-barra wvp-barra-pdf">' +
         '<div class="wvp-f1"><b class="wvp-titulo">' + esc(opts.titulo || 'PDF') + '</b>' +
          '<button type="button" class="wvp-b wvp-x" data-v="cerrar" aria-label="Cerrar">✕</button></div>' +
         '<div class="wvp-f2">' +
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
          (opts.modoLectura ? '<button type="button" class="wvp-b wvp-blec" data-lec="tog" aria-pressed="false">Aa Modo lectura</button>' : '') +
          (conChat ? '<button type="button" class="wvp-b wvp-bchat" data-v="chat">💬 Tutor</button>' : '') +
          (opts.descargable ? '<button type="button" class="wvp-b wvp-desc" data-v="bajar">⬇ Descargar</button>' : '') +
         '</div>' +
         '<div class="wvp-f3">' +
          '<div class="wvp-ctrl wvp-voz">' +
            '<button type="button" class="wvp-b wvp-leer" data-v="leer">🔊 Escuchar</button>' +
            '<button type="button" class="wvp-b" data-v="pausa" hidden>⏸ Pausa</button>' +
            '<button type="button" class="wvp-b" data-v="parar" hidden>■ Parar</button>' +
            '<select class="wvp-vel" aria-label="Velocidad de la voz"><option value="0.8">Lenta</option><option value="1" selected>Normal</option><option value="1.25">Rápida</option></select>' +
          '</div>' +
         '</div>' +
        '</div>' +
        '<div class="wvp-cuerpo">' +
          '<div class="wvp-estado">Cargando PDF…</div>' +
          '<div class="wvp-pagina"><canvas class="wvp-canvas" hidden></canvas><div class="wvp-texto"></div></div>' +
          (opts.modoLectura ? '<div class="wvp-lector" hidden></div>' : '') +
        '</div>' +
       '</div>' +
       (conChat ?
        '<aside class="wvp-chat" aria-label="Tutor">' +
          '<div class="wvp-chat-cab"><b>💬 Tutor Wave</b><small>Preguntale lo que no entiendas de este material</small>' +
            '<button type="button" class="wvp-chat-x" data-v="chat" aria-label="Achicar el tutor" title="Achicar el tutor">✕</button></div>' +
          '<div class="wt-cuerpo"></div>' +
        '</aside>' : '') +
      '</div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');

    var cuerpo = el.querySelector('.wvp-cuerpo');
    var canvas = el.querySelector('.wvp-canvas');
    var estado = el.querySelector('.wvp-estado');
    var num = el.querySelector('.wvp-num');
    var ctx = canvas.getContext('2d');
    var capa = el.querySelector('.wvp-texto');
    var pagina_el = el.querySelector('.wvp-pagina');
    var capaDivs = [], capaStrs = [];

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
        await pintarTexto(pagina, escala);
        if (mia !== ficha || cerrado) return;
        cuerpo.scrollTo(0, 0);
        if (voz.hablando) remarcar();
        if (lecOn) lecArmar();
        if (n === total && !avisado && opts.alTerminar) { avisado = true; try { opts.alTerminar(); } catch (e2) { /* nada */ } }
      } catch (e) {
        if (e && e.name === 'RenderingCancelledException') return;
        console.error(e);
        mostrarError('No se pudo mostrar esta página.');
      }
    }

    // Capa de texto invisible encima del PDF: sirve para saber dónde está cada línea y marcarla mientras se lee.
    async function pintarTexto(pagina, escala) {
      capa.innerHTML = ''; capaDivs = []; capaStrs = [];
      try {
        var vpc = pagina.getViewport({ scale: escala });
        capa.style.width = Math.round(vpc.width) + 'px';
        capa.style.height = Math.round(vpc.height) + 'px';
        capa.style.setProperty('--scale-factor', String(vpc.scale)); // sin esto pdf.js no ubica las líneas y no se puede marcar nada
        var contenido = await pagina.getTextContent();
        var t = window.pdfjsLib.renderTextLayer({ textContentSource: contenido, container: capa, viewport: vpc, textDivs: capaDivs, textContentItemsStr: capaStrs });
        await t.promise;
      } catch (e) { /* sin capa de texto: el PDF se ve igual, solo no se puede leer en voz alta */ }
    }

    function ir(nueva) {
      nueva = Math.min(total, Math.max(1, nueva));
      if (nueva === n) return Promise.resolve();
      n = nueva;
      actualizarControles();
      return pintar();
    }

    // ---------- Modo lectura: el texto de la página con letra, interlineado y espacio entre palabras a medida ----------
    var lector = el.querySelector('.wvp-lector'), lecOn = false, lecPag = null;
    var LEC = { t: 1.25, i: 1.9, p: 0.3, f: 'lexend' };
    var FUENTES = { lexend: ['Lexend', '"Lexend", Verdana, sans-serif', 'https://fonts.googleapis.com/css2?family=Lexend:wght@400;600&display=swap'], atkinson: ['Atkinson Hyperlegible', '"Atkinson Hyperlegible", Verdana, sans-serif', 'https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap'], opendys: ['OpenDyslexic', '"OpenDyslexic", "Comic Sans MS", sans-serif', 'https://cdn.jsdelivr.net/npm/@fontsource/opendyslexic@5/400.css'], arial: ['Arial', 'Arial, Helvetica, sans-serif', ''], verdana: ['Verdana', 'Verdana, Geneva, sans-serif', ''] };
    function cargarFuente(k) {
      var f = FUENTES[k]; if (!f || !f[2] || document.querySelector('link[data-wfuente="' + k + '"]')) return;
      var ln = document.createElement('link'); ln.rel = 'stylesheet'; ln.href = f[2]; ln.setAttribute('data-wfuente', k); document.head.appendChild(ln);
    }
    try { var g = JSON.parse(localStorage.getItem('wave_modo_lectura') || 'null'); if (g) { if (g.f && FUENTES[g.f]) LEC.f = g.f; LEC.t = +g.t || LEC.t; LEC.i = +g.i || LEC.i; LEC.p = g.p === 0 ? 0 : (+g.p || LEC.p); } } catch (e) { /* nada */ }
    function lecGuardar() { try { localStorage.setItem('wave_modo_lectura', JSON.stringify(LEC)); } catch (e) { /* nada */ } }
    // Una línea del PDF: junta los pedazos de texto según la posición, y recompone los títulos con letras separadas (W A V E → WAVE)
    function lecLinea(l) {
      var LET = /^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]$/;
      var T = l.toks.filter(function (k) { return k.s.trim() !== ''; });
      var out = T.map(function (k, i) { var pr = T[i - 1]; return { s: k.s, gap: pr ? k.x - (pr.x + pr.w) : 0 }; });
      var res = '', i = 0;
      while (i < out.length) {
        if (LET.test(out[i].s.trim())) {
          var j = i; while (j < out.length && LET.test(out[j].s.trim())) j++;
          if (j - i >= 3) {
            var gaps = []; for (var q = i + 1; q < j; q++) gaps.push(out[q].gap);
            var ord = gaps.slice().sort(function (x, y) { return x - y; }), med = ord[Math.floor(ord.length / 2)];
            var corte = Math.max(med * 1.7, med + l.h * 0.35), txt = out[i].s.trim();
            for (q = i + 1; q < j; q++) txt += (out[q].gap > corte ? ' ' : '') + out[q].s.trim();
            res += (res && !/\s$/.test(res) ? ' ' : '') + txt + ' ';
            i = j; continue;
          }
        }
        var sp = i > 0 && out[i].gap > l.h * 0.28 && !/\s$/.test(res) && !/^\s/.test(out[i].s);
        res += (sp ? ' ' : '') + out[i].s; i++;
      }
      return res;
    }
    function lecParrafos(items) {
      var L = [], cur = null;
      items.forEach(function (it) {
        if (typeof it.str !== 'string') return;
        var y = it.transform[5], tk = { s: it.str, x: it.transform[4], w: it.width || 0 };
        if (cur && Math.abs(cur.y - y) < 2.5) { cur.toks.push(tk); }
        else { cur = { y: y, h: Math.abs(it.height) || Math.abs(it.transform[3]) || 10, toks: [tk] }; L.push(cur); }
      });
      var P = [], act = '', prev = null;
      L.forEach(function (l) {
        var t = lecLinea(l).replace(/\s+/g, ' ').trim();
        if (!t) { if (act) { P.push(act); act = ''; } prev = null; return; }
        var corte = prev && (prev.y - l.y > prev.h * 1.75 || l.y > prev.y + 2);
        if (corte && act) { P.push(act); act = ''; }
        act = act ? (/[-‐]$/.test(act) ? act.slice(0, -1) + t : act + ' ' + t) : t;
        prev = l;
      });
      if (act) P.push(act);
      return P;
    }
    async function lecArmar() {
      if (!lecOn || !lector || !pdf) return;
      var pg = await pdf.getPage(n), cont = await pg.getTextContent();
      if (!lecOn) return;
      var P = lecParrafos(cont.items);
      lector.style.setProperty('--lt', LEC.t + 'rem');
      lector.style.setProperty('--li', String(LEC.i));
      lector.style.setProperty('--lp', LEC.p + 'em');
      lector.style.setProperty('--lf', FUENTES[LEC.f][1]); cargarFuente(LEC.f);
      var ctl = '<div class="wvp-lec-ctl" role="group" aria-label="Ajustes de lectura">' +
        '<span>Tipo de letra <select class="wvp-lec-f" data-lec-f="1" aria-label="Tipo de letra">' + Object.keys(FUENTES).map(function (k) { return '<option value="' + k + '"' + (k === LEC.f ? ' selected' : '') + '>' + FUENTES[k][0] + '</option>'; }).join('') + '</select></span>' +
        '<span>Letra <button type="button" class="wvp-b" data-lec="t-">A−</button><button type="button" class="wvp-b" data-lec="t+">A+</button></span>' +
        '<span>Líneas <button type="button" class="wvp-b" data-lec="i-">−</button><button type="button" class="wvp-b" data-lec="i+">+</button></span>' +
        '<span>Palabras <button type="button" class="wvp-b" data-lec="p-">−</button><button type="button" class="wvp-b" data-lec="p+">+</button></span></div>';
      lector.innerHTML = ctl + (P.length
        ? P.map(function (x) { return '<p>' + esc(x) + '</p>'; }).join('')
        : '<p class="wvp-lec-vacio">Esta página no tiene texto para mostrar así (puede ser una imagen). Volvé al PDF para verla.</p>');
      cuerpo.scrollTo(0, 0);
    }
    function lecAjustar(a) {
      if (a === 't-') LEC.t = Math.max(1, +(LEC.t - 0.15).toFixed(2)); else if (a === 't+') LEC.t = Math.min(2.4, +(LEC.t + 0.15).toFixed(2));
      else if (a === 'i-') LEC.i = Math.max(1.4, +(LEC.i - 0.2).toFixed(2)); else if (a === 'i+') LEC.i = Math.min(3, +(LEC.i + 0.2).toFixed(2));
      else if (a === 'p-') LEC.p = Math.max(0, +(LEC.p - 0.1).toFixed(2)); else if (a === 'p+') LEC.p = Math.min(1, +(LEC.p + 0.1).toFixed(2));
      lecGuardar();
      lector.style.setProperty('--lt', LEC.t + 'rem'); lector.style.setProperty('--li', String(LEC.i)); lector.style.setProperty('--lp', LEC.p + 'em');
    }
    if (lector) el.addEventListener('change', function (ev) {
      var sel = ev.target.closest && ev.target.closest('[data-lec-f]'); if (!sel || !FUENTES[sel.value]) return;
      LEC.f = sel.value; lecGuardar(); cargarFuente(LEC.f); lector.style.setProperty('--lf', FUENTES[LEC.f][1]);
    });
    if (lector) el.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-lec]'); if (!b) return;
      var a = b.getAttribute('data-lec');
      if (a === 'tog') {
        lecOn = !lecOn;
        b.setAttribute('aria-pressed', lecOn ? 'true' : 'false');
        b.textContent = lecOn ? '📄 Ver el PDF' : 'Aa Modo lectura';
        lector.hidden = !lecOn;
        pagina_el.style.display = lecOn ? 'none' : '';
        if (lecOn) lecArmar(); else cuerpo.scrollTo(0, 0);
      } else lecAjustar(a);
    });

    // ---------- Lectura en voz alta del PDF, con la oración marcada encima ----------
    var voz = { hablando: false, pausado: false, cola: [], idx: 0, vozES: null, marcados: [], sesion: 0 };
    var selVel = el.querySelector('.wvp-vel');
    try { selVel.value = localStorage.getItem('wave_voz_vel') || '1'; } catch (e) { /* nada */ }
    selVel.addEventListener('change', function () { try { localStorage.setItem('wave_voz_vel', selVel.value); } catch (e) { /* nada */ } });

    function botonesVoz() {
      el.querySelector('[data-v="leer"]').textContent = voz.hablando ? '↺ Desde el inicio' : '🔊 Escuchar';
      var p = el.querySelector('[data-v="pausa"]'), x = el.querySelector('[data-v="parar"]');
      p.hidden = x.hidden = !voz.hablando;
      p.textContent = voz.pausado ? '▶ Seguir' : '⏸ Pausa';
    }
    function desmarcar() { voz.marcados.forEach(function (d) { d.classList.remove('wvp-lee'); }); voz.marcados = []; }
    function marcar(divs) {
      desmarcar();
      divs.forEach(function (d) { if (d) { d.classList.add('wvp-lee'); voz.marcados.push(d); } });
      var d0 = divs.filter(Boolean)[0];
      if (d0) {
        var cr = cuerpo.getBoundingClientRect(), dr = d0.getBoundingClientRect();
        if (dr.top < cr.top + 40 || dr.bottom > cr.bottom - 40) cuerpo.scrollTo({ top: cuerpo.scrollTop + (dr.top - cr.top) - cr.height / 3, behavior: 'smooth' });
      }
    }
    function remarcar() { var it = voz.cola[voz.idx]; if (it) marcar(it.divs.map(function (i) { return capaDivs[i]; })); }

    // Arma las oraciones de la página que se está viendo y a qué líneas del PDF corresponde cada una.
    // El PDF guarda títulos y etiquetas con las letras separadas ("W A V E"): se juntan para que la voz lea palabras, no letras.
    // El encabezado y el pie de cada página (WAVE ACADEMY · materia · lección, "Material de estudio…", número) no se leen.
    function textoLeible(i) {
      var s = String(capaStrs[i] || ''), d = capaDivs[i];
      if (!s.trim() || !d) return '';
      var cr = capa.getBoundingClientRect(), r = d.getBoundingClientRect();
      if (cr.height > 0) { var arriba = (r.top - cr.top) / cr.height, abajo = (r.bottom - cr.top) / cr.height; if (arriba < 0.07 || abajo > 0.94) return ''; }
      var t = s.trim();
      if (/^\S( \S)+$/.test(t)) t = t.replace(/ /g, '').toLowerCase(); // letras separadas -> palabra
      else if (t.length === 1 && /[A-ZÁÉÍÓÚÑ]/.test(t)) t = t.toLowerCase();
      t = t.replace(/[▶►•■□●○◆▪→←↑↓✔✘★·|]/g, ' ').replace(/(\d)\.º/g, '$1º').replace(/\b[a-zñ]+\.º/gi, '').replace(/^(\d+)\.\s+/, '$1, ').replace(/\s+/g, ' ').trim();
      return /[A-Za-zÁÉÍÓÚáéíóúÑñ0-9]/.test(t) ? t : '';
    }
    function armarCola() {
      var FIN = '\u0001', texto = '', mapa = [], prev = null, prevT = '', cr = capa.getBoundingClientRect();
      capaStrs.forEach(function (_, i) {
        var t = textoLeible(i);
        if (t && prevT && t.toLowerCase() === prevT.toLowerCase()) t = ''; // etiqueta repetida
        var r = t ? capaDivs[i].getBoundingClientRect() : null;
        if (r && prev) {
          var mismaLinea = Math.abs(r.top - prev.top) < Math.max(2, prev.height * 0.5);
          if (!mismaLinea) {
            var paso = r.top - prev.top, cambioAlto = Math.abs(r.height - prev.height) > Math.max(1.5, prev.height * 0.12);
            var anteriorLarga = prev.width > cr.width * 0.55; // una línea de párrafo que sigue en la de abajo suele ocupar casi todo el ancho
            if (cambioAlto || Math.abs(r.left - prev.left) > 4 || paso < 0 || paso > prev.height * 3 || (paso > prev.height * 1.2 && !anteriorLarga)) texto += FIN; // otro bloque: título, lista, párrafo nuevo
          }
        }
        mapa.push({ i: i, ini: texto.length, fin: texto.length + t.length }); texto += t + ' ';
        if (t) { prev = r; prevT = t; }
      });
      var out = [], re = /[^.!?¿¡:;\u0001]+[.!?:;]*/g, m;
      while ((m = re.exec(texto))) {
        var t = m[0].replace(/\s+/g, ' ').trim();
        if (t.length < 2 || !/[A-Za-zÁÉÍÓÚáéíóúÑñ0-9]/.test(t)) continue;
        var a = m.index, b = m.index + m[0].length;
        out.push({ t: t, divs: mapa.filter(function (x) { return x.fin > x.ini && x.ini < b && x.fin > a; }).map(function (x) { return x.i; }) });
      }
      return out;
    }
    function elegirVoz() {
      var vs = speechSynthesis.getVoices();
      voz.vozES = vs.filter(function (v) { return /^es[-_]AR/i.test(v.lang); })[0] || vs.filter(function (v) { return /^es[-_]419|^es[-_]MX|^es[-_]US/i.test(v.lang); })[0] || vs.filter(function (v) { return /^es/i.test(v.lang); })[0] || null;
    }
    async function leerPagina(ses) {
      if (ses !== voz.sesion || cerrado) return;
      voz.cola = armarCola(); voz.idx = 0;
      if (!voz.cola.length) { await siguientePagina(ses); return; }
      decir(ses);
    }
    async function siguientePagina(ses) {
      if (ses !== voz.sesion || cerrado) return;
      if (n >= total) { pararVoz(); return; }
      await ir(n + 1);
      await leerPagina(ses);
    }
    function decir(ses) {
      if (ses !== voz.sesion || !voz.hablando || voz.pausado || cerrado) return;
      if (voz.idx >= voz.cola.length) { siguientePagina(ses); return; }
      var it = voz.cola[voz.idx];
      marcar(it.divs.map(function (i) { return capaDivs[i]; }));
      var u = new SpeechSynthesisUtterance(it.t);
      u.lang = (voz.vozES && voz.vozES.lang) || 'es-AR'; if (voz.vozES) u.voice = voz.vozES;
      u.rate = parseFloat(selVel.value) || 1;
      var sigue = function () { if (ses === voz.sesion && voz.hablando && !voz.pausado) { voz.idx++; decir(ses); } };
      u.onend = sigue; u.onerror = sigue;
      speechSynthesis.speak(u);
    }
    function leerVoz() {
      if (!('speechSynthesis' in window)) { mostrarError('Este navegador no puede leer en voz alta.'); return; }
      if (!capaStrs.length) { return; }
      try { speechSynthesis.cancel(); } catch (e) { /* nada */ }
      elegirVoz(); voz.sesion++; voz.hablando = true; voz.pausado = false; botonesVoz();
      leerPagina(voz.sesion);
    }
    function pausaVoz() {
      if (!voz.hablando) return;
      if (voz.pausado) { voz.pausado = false; botonesVoz(); decir(voz.sesion); }
      else { voz.pausado = true; try { speechSynthesis.cancel(); } catch (e) { /* nada */ } botonesVoz(); }
    }
    function pararVoz() { voz.sesion++; voz.hablando = false; voz.pausado = false; try { speechSynthesis.cancel(); } catch (e) { /* nada */ } desmarcar(); botonesVoz(); }
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
      pararVoz();
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

    // ---------- Chat con el tutor (componente compartido js/tutor-ia.js) ----------
    if (conChat) {
      WaveTutor.montar({ contenedor: el.querySelector('.wt-cuerpo'), pantalla: 'pdf', enviar: opts.chat, ctx: opts.chatCtx, config: opts.chatConfig });
    }

    el.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-v]');
      if (!b) { if (ev.target === el) cerrar(); return; }
      var v = b.getAttribute('data-v');
      if (v === 'cerrar') cerrar();
      else if (v === 'ant') { if (voz.hablando) pararVoz(); ir(n - 1); }
      else if (v === 'sig') { if (voz.hablando) pararVoz(); ir(n + 1); }
      else if (v === 'mas') cambiarZoom(zoom + 0.25);
      else if (v === 'menos') cambiarZoom(zoom - 0.25);
      else if (v === 'ajustar') cambiarZoom(1);
      else if (v === 'bajar') descargar();
      else if (v === 'leer') leerVoz();
      else if (v === 'pausa') pausaVoz();
      else if (v === 'parar') pararVoz();
      else if (v === 'chat') { if (window.innerWidth > 860) { el.classList.toggle('chat-oculto'); setTimeout(pintar, 50); return; } el.classList.toggle('chat-abierto'); setTimeout(pintar, 50); if (el.classList.contains('chat-abierto')) { var c = el.querySelector('.wvp-chat textarea'); if (c) c.focus(); } }
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
