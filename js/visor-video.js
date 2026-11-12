// Reproductor de video reutilizable (Cloudflare Stream).
// Trae pausa, barra para adelantar/atrasar, volumen, velocidad y pantalla completa (PC y celular), sin botón de descarga.
// Los videos son privados: "token" devuelve el token temporal del video.
// Uso: WaveVisor.abrirVideo({ titulo: 'Clase 1', token: async function () { return 'token...'; } })
//      WaveVisor.montarVideo(elemento, { titulo, token }) para mostrarlo dentro de una página.
(function () {
  var SDK = 'https://embed.videodelivery.net/embed/sdk.latest.js';
  var promesaSdk = null;
  window.WaveVisor = window.WaveVisor || {};

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function cargarSdk() {
    if (window.Stream) return Promise.resolve();
    if (promesaSdk) return promesaSdk;
    promesaSdk = new Promise(function (ok, mal) {
      var s = document.createElement('script');
      s.src = SDK;
      s.onload = function () { window.Stream ? ok() : mal(new Error('sdk')); };
      s.onerror = function () { promesaSdk = null; mal(new Error('sdk')); };
      document.head.appendChild(s);
    });
    return promesaSdk;
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
    var player = null, vivo = true;

    function error(msg) {
      marco.innerHTML = '<div class="wvv-estado error">' + esc(msg) + '</div>';
      barra.hidden = true;
    }

    Promise.resolve().then(function () { return opts.token(); }).then(function (token) {
      if (!vivo) return;
      var f = document.createElement('iframe');
      f.src = 'https://iframe.videodelivery.net/' + encodeURIComponent(token) + '?primaryColor=087E83&letterboxColor=000000&preload=auto';
      f.title = opts.titulo || 'Video';
      f.setAttribute('allow', 'accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture; fullscreen');
      f.setAttribute('allowfullscreen', '');
      marco.innerHTML = '';
      marco.appendChild(f);
      barra.hidden = false;
      cargarSdk().then(function () { player = window.Stream(f); }).catch(function () { barra.hidden = true; });
    }).catch(function (e) {
      console.error(e);
      error((e && e.message) || 'No se pudo cargar el video.');
    });

    barra.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-v]');
      if (!b || !player) return;
      var t = player.currentTime || 0;
      player.currentTime = Math.max(0, t + (b.getAttribute('data-v') === 'adelante' ? 10 : -10));
    });

    return { destruir: function () { vivo = false; cont.innerHTML = ''; } };
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
