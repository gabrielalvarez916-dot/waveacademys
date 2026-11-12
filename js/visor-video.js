// Reproductor de video reutilizable (archivo de video en R2, sin botón de descarga).
// Trae pausa, barra para adelantar/atrasar, volumen, velocidad y pantalla completa (PC y celular).
// Los videos son privados: "url" devuelve el enlace temporal y firmado del archivo.
// Uso: WaveVisor.abrirVideo({ titulo: 'Clase 1', url: async function () { return 'https://...'; }, alTerminar })
//      WaveVisor.montarVideo(elemento, { titulo, url, alTerminar }) para mostrarlo dentro de una página.
(function () {
  window.WaveVisor = window.WaveVisor || {};

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function montarVideo(cont, opts) {
    cont.innerHTML =
      '<div class="wvv">' +
        '<div class="wvv-marco"><div class="wvv-estado">Cargando video…</div></div>' +
        '<div class="wvv-barra" hidden>' +
          '<button type="button" class="wvp-b" data-v="atras">⟲ 10 s</button>' +
          '<button type="button" class="wvp-b" data-v="adelante">10 s ⟳</button>' +
        '</div>' +
      '</div>';
    var marco = cont.querySelector('.wvv-marco');
    var barra = cont.querySelector('.wvv-barra');
    var video = null, vivo = true, avisado = false;
    // Recorte: se muestran solo los tramos indicados (en segundos), uno detrás del otro; sin tramos, el video entero
    var segs = (opts.tramos && opts.tramos.length ? opts.tramos : (opts.inicio || opts.fin ? [{ i: opts.inicio, f: opts.fin }] : []))
      .map(function (s) { var i = Math.max(0, Number(s.i) || 0), f = Number(s.f) > i ? Number(s.f) : 0; return { i: i, f: f }; })
      .sort(function (a, b) { return a.i - b.i; });
    var ini = segs.length ? segs[0].i : 0, fin = segs.length ? segs[segs.length - 1].f : 0;
    // Dónde tiene que estar el video si está en el segundo t: {t: segundo permitido, fin: true si ya pasó el último tramo}
    function ubicar(t, m) {
      for (var k = 0; k < segs.length; k++) {
        var s = segs[k];
        if (!s.f || t < s.f) return { t: t < s.i - m ? s.i : t, fin: false };
      }
      return { t: fin, fin: true };
    }

    function error(msg) {
      marco.innerHTML = '<div class="wvv-estado error">' + esc(msg) + '</div>';
      barra.hidden = true;
    }

    // Video de YouTube incrustado (no se descarga ni se copia: se reproduce desde YouTube)
    if (opts.youtube) {
      var terminar = function () { if (avisado || !opts.alTerminar) return; avisado = true; try { opts.alTerminar(); } catch (e0) { /* nada */ } };
      var fr = document.createElement('iframe');
      fr.className = 'wvv-yt';
      fr.title = opts.titulo || 'Video';
      fr.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      fr.allowFullscreen = true;
      fr.referrerPolicy = 'strict-origin-when-cross-origin';
      fr.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(opts.youtube) + '?enablejsapi=1&rel=0&modestbranding=1&playsinline=1' + (ini ? '&start=' + Math.floor(ini) : '') + (fin && segs.length === 1 ? '&end=' + Math.ceil(fin) : '') + '&origin=' + encodeURIComponent(location.origin);
      var oir = function (ev) {
        if (ev.source !== fr.contentWindow) return;
        try { var d = typeof ev.data === 'string' ? JSON.parse(ev.data) : ev.data; if (d && d.info && d.info.playerState === 0) terminar();
          var ct = d && d.info ? d.info.currentTime : null;
          if (typeof ct === 'number') {
            var man = function (f, a) { fr.contentWindow.postMessage(JSON.stringify({ event: 'command', func: f, args: a || [] }), '*'); };
            var u = segs.length ? ubicar(ct, 1.5) : null;
            if (u && u.fin) { man('pauseVideo'); if (ct > fin + 1.5) man('seekTo', [fin, true]); terminar(); }
            else if (u && u.t !== ct) man('seekTo', [u.t, true]);
          } } catch (e1) { /* otro mensaje */ }
      };
      window.addEventListener('message', oir);
      fr.addEventListener('load', function () { try { fr.contentWindow.postMessage(JSON.stringify({ event: 'listening', id: 1, channel: 'widget' }), '*'); } catch (e2) { /* nada */ } });
      marco.innerHTML = ''; marco.classList.add('yt'); marco.appendChild(fr);
      if (opts.alTerminar) {
        barra.innerHTML = '<button type="button" class="wvp-b wvv-listo">✔ Ya vi el video</button>';
        barra.hidden = false;
        barra.querySelector('.wvv-listo').addEventListener('click', function (ev) { terminar(); ev.currentTarget.disabled = true; ev.currentTarget.textContent = '✔ ¡Listo!'; });
      }
      return { destruir: function () { vivo = false; window.removeEventListener('message', oir); cont.innerHTML = ''; } };
    }

    Promise.resolve().then(function () { return opts.url(); }).then(function (enlace) {
      if (!vivo) return;
      video = document.createElement('video');
      video.src = enlace + (segs.length ? '#t=' + ini + (fin && segs.length === 1 ? ',' + fin : '') : '');
      video.controls = true;
      video.playsInline = true;
      video.preload = 'metadata';
      video.setAttribute('controlslist', 'nodownload noremoteplayback');
      video.setAttribute('disablepictureinpicture', '');
      video.title = opts.titulo || 'Video';
      video.addEventListener('contextmenu', function (ev) { ev.preventDefault(); });
      video.addEventListener('error', function () { error('No se pudo reproducir el video. Puede que todavía no esté disponible; probá de nuevo en un momento.'); });
      var alFinal = function () {
        if (avisado || !opts.alTerminar) return;
        avisado = true;
        try { opts.alTerminar(); } catch (e2) { /* nada */ }
      };
      video.addEventListener('ended', alFinal);
      if (segs.length) {
        video.addEventListener('loadedmetadata', function () { if (ini && video.currentTime < ini) video.currentTime = ini; });
        var cuidar = function () {
          var u = ubicar(video.currentTime, 0.3);
          if (u.fin) { if (video.currentTime > fin + 0.3) video.currentTime = fin; if (!video.paused) video.pause(); alFinal(); }
          else if (u.t !== video.currentTime) video.currentTime = u.t;
        };
        video.addEventListener('timeupdate', cuidar);
        video.addEventListener('seeking', function () {
          var u = ubicar(video.currentTime, 0.3);
          if (u.fin ? video.currentTime > fin + 0.3 : u.t !== video.currentTime) video.currentTime = u.t;
        });
        video.addEventListener('play', function () { if (fin && video.currentTime >= fin - 0.2) video.currentTime = ini; });
      }
      marco.innerHTML = '';
      marco.appendChild(video);
      barra.hidden = false;
    }).catch(function (e) {
      console.error(e);
      error((e && e.message) || 'No se pudo cargar el video.');
    });

    barra.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-v]');
      if (!b || !video) return;
      var atras = b.getAttribute('data-v') !== 'adelante', nt = Math.max(0, (video.currentTime || 0) + (atras ? -10 : 10));
      if (segs.length) {
        if (atras) { // si cae en una parte quitada, va al final del tramo anterior
          for (var k = segs.length - 1; k >= 0; k--) { if (nt >= segs[k].i) { if (segs[k].f && nt >= segs[k].f) nt = Math.max(segs[k].i, segs[k].f - 3); break; } }
          if (nt < ini) nt = ini;
        } else nt = ubicar(nt, 0).t;
      }
      video.currentTime = nt;
    });

    return { destruir: function () { vivo = false; if (video) { try { video.pause(); video.removeAttribute('src'); video.load(); } catch (e3) { /* nada */ } } cont.innerHTML = ''; } };
  }

  function abrirVideo(opts) {
    var el = document.createElement('div');
    el.className = 'wvp';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', 'Reproductor de video');
    el.innerHTML =
      '<div class="wvp-caja wvv-caja">' +
        '<div class="wvp-barra"><b class="wvp-titulo">' + esc(opts.titulo || 'Video') + '</b>' +
        '<button type="button" class="wvp-b wvp-x" data-v="cerrar" aria-label="Cerrar">✕</button></div>' +
        '<div class="wvv-cuerpo"></div>' +
      '</div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');
    var mont = montarVideo(el.querySelector('.wvv-cuerpo'), opts);

    function cerrar() {
      mont.destruir();
      document.removeEventListener('keydown', tecla);
      document.body.classList.remove('wvp-abierto');
      el.remove();
    }
    function tecla(ev) { if (ev.key === 'Escape') cerrar(); }
    document.addEventListener('keydown', tecla);
    el.addEventListener('click', function (ev) {
      if (ev.target === el || ev.target.closest('[data-v="cerrar"]')) cerrar();
    });
    return { cerrar: cerrar };
  }

  window.WaveVisor.montarVideo = montarVideo;
  window.WaveVisor.abrirVideo = abrirVideo;
})();
