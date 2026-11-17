// Editor visual de recorte de video (admin). Funciona con videos de YouTube incrustados y con archivos de video.
// No toca el video original: guarda solo qué partes se muestran ("tramos" en segundos, igual que el recorte por tiempos).
// Uso: WaveEditor.abrir({ titulo, youtube: 'ID' | url: async () => 'https://...', tramos: [{i, f}], guardar: async (tramos) => {} })
(function () {
  window.WaveEditor = window.WaveEditor || {};

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function reloj(s) {
    s = Math.max(0, Math.round(Number(s) || 0));
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
    return (h ? h + ':' + ('0' + m).slice(-2) : m) + ':' + ('0' + r).slice(-2);
  }
  function aSeg(t) {
    t = String(t || '').trim();
    if (!/^\d+(:\d{1,2}){0,2}$/.test(t)) return NaN;
    return t.split(':').reduce(function (a, x) { return a * 60 + Number(x); }, 0);
  }

  // Une partes quitadas que se tocan o se pisan, las deja ordenadas y dentro del video
  function limpiar(cuts, dur) {
    var c = cuts.map(function (x) { return { a: Math.max(0, Math.min(x.a, x.b)), b: Math.min(dur, Math.max(x.a, x.b)) }; })
      .filter(function (x) { return x.b - x.a >= 0.5; })
      .sort(function (x, y) { return x.a - y.a; });
    var out = [];
    c.forEach(function (x) {
      var u = out[out.length - 1];
      if (u && x.a <= u.b + 0.25) u.b = Math.max(u.b, x.b); else out.push({ a: x.a, b: x.b });
    });
    return out;
  }
  // Tramos que se muestran -> partes quitadas (los huecos entre tramos)
  function cortesDe(tramos, dur) {
    if (!tramos || !tramos.length) return [];
    var t = tramos.map(function (s) { var i = Math.max(0, Number(s.i) || 0); return { i: i, f: Number(s.f) > i ? Math.min(Number(s.f), dur) : dur }; })
      .sort(function (x, y) { return x.i - y.i; });
    var cuts = [], pos = 0;
    t.forEach(function (s) { if (s.i > pos) cuts.push({ a: pos, b: s.i }); pos = Math.max(pos, s.f); });
    if (pos < dur) cuts.push({ a: pos, b: dur });
    return limpiar(cuts, dur);
  }
  // Partes quitadas -> tramos que se muestran (f = 0 significa "hasta el final")
  function tramosDe(cuts, dur) {
    if (!cuts.length) return [];
    var keep = [], pos = 0;
    cuts.forEach(function (c) { if (c.a - pos >= 0.5) keep.push({ i: pos, f: c.a }); pos = c.b; });
    if (dur - pos >= 0.5) keep.push({ i: pos, f: dur });
    return keep.map(function (k) {
      return { i: k.i < 0.5 ? 0 : Math.round(k.i * 10) / 10, f: k.f >= dur - 0.5 ? 0 : Math.round(k.f * 10) / 10 };
    });
  }

  function abrir(opts) {
    var el = document.createElement('div');
    el.className = 'wvp';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-label', 'Editar video');
    el.innerHTML =
      '<div class="wvp-caja wve-caja">' +
        '<div class="wvp-barra"><b class="wvp-titulo">✂️ Editar video · ' + esc(opts.titulo || '') + '</b>' +
        '<button type="button" class="wvp-b wvp-x" data-e="cerrar" aria-label="Cerrar">✕</button></div>' +
        '<div class="wve-cuerpo">' +
          '<div class="wve-marco"><div class="wvv-estado">Cargando video…</div></div>' +
          '<div class="wve-ctl">' +
            '<button type="button" class="wvp-b" data-e="atras">⟲ 5 s</button>' +
            '<button type="button" class="wvp-b wve-play" data-e="play">▶ Reproducir</button>' +
            '<button type="button" class="wvp-b" data-e="adelante">5 s ⟳</button>' +
            '<span class="wve-reloj">0:00 / 0:00</span>' +
          '</div>' +
          '<div class="wve-linea" title="Tocá acá para ir a ese momento"><div class="wve-base"></div><div class="wve-cabezal"></div></div>' +
          '<p class="wve-ayuda">Reproducí hasta donde empieza la parte que no querés y tocá <b>Empezar a quitar acá</b>. Después seguí hasta donde termina y tocá <b>Terminar de quitar acá</b>.</p>' +
          '<div class="wve-acc">' +
            '<button type="button" class="wve-btn" data-e="ini">✂️ Empezar a quitar acá</button>' +
            '<button type="button" class="wve-btn suave" data-e="cancelar" hidden>Cancelar</button>' +
            '<button type="button" class="wve-btn suave" data-e="principio">Quitar el principio hasta acá</button>' +
            '<button type="button" class="wve-btn suave" data-e="final">Quitar desde acá hasta el final</button>' +
          '</div>' +
          '<div class="wve-lista"></div>' +
          '<div class="wve-pie">' +
            '<span class="wve-resumen"></span>' +
            '<button type="button" class="wve-btn suave" data-e="probar">▶ Probar como lo ve el alumno</button>' +
            '<button type="button" class="wve-btn" data-e="guardar">Guardar</button>' +
          '</div>' +
        '</div>' +
      '</div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');

    var marco = el.querySelector('.wve-marco'), linea = el.querySelector('.wve-linea');
    var base = el.querySelector('.wve-base'), cab = el.querySelector('.wve-cabezal');
    var reloj$ = el.querySelector('.wve-reloj'), lista = el.querySelector('.wve-lista'), resumen = el.querySelector('.wve-resumen');
    var bIni = el.querySelector('[data-e="ini"]'), bCan = el.querySelector('[data-e="cancelar"]'), bPlay = el.querySelector('.wve-play');
    var dur = 0, ahora = 0, suena = false, cuts = [], pend = null, vivo = true, player = null, tramosIni = opts.tramos || [];

    function listo() { return dur > 0; }
    function pintar() {
      if (!listo()) return;
      var pct = function (s) { return (Math.max(0, Math.min(dur, s)) / dur * 100).toFixed(3) + '%'; };
      base.innerHTML = cuts.map(function (c) { return '<i class="wve-quitado" style="left:' + pct(c.a) + ';width:' + ((c.b - c.a) / dur * 100).toFixed(3) + '%"></i>'; }).join('') +
        (pend != null ? '<i class="wve-pend" style="left:' + pct(pend) + ';width:' + (Math.max(0, ahora - pend) / dur * 100).toFixed(3) + '%"></i>' : '');
      cab.style.left = pct(ahora);
      reloj$.textContent = reloj(ahora) + ' / ' + reloj(dur);
      bPlay.textContent = suena ? '⏸ Pausar' : '▶ Reproducir';
      bIni.textContent = pend == null ? '✂️ Empezar a quitar acá' : '✂️ Terminar de quitar acá (desde ' + reloj(pend) + ')';
      bCan.hidden = pend == null;
      var quit = cuts.reduce(function (a, c) { return a + (c.b - c.a); }, 0);
      resumen.textContent = cuts.length ? 'Queda de ' + reloj(dur - quit) + ' (se quitan ' + reloj(quit) + ' de ' + reloj(dur) + ')' : 'Sin recortes: se muestra el video entero (' + reloj(dur) + ')';
      lista.innerHTML = cuts.length
        ? '<b>Partes quitadas</b>' + cuts.map(function (c, i) {
            return '<div class="wve-fila"><span>' + reloj(c.a) + ' → ' + reloj(c.b) + '</span>' +
              '<button type="button" class="wvp-b" data-e="ir" data-i="' + i + '">Ir ahí</button>' +
              '<button type="button" class="wvp-b" data-e="ajustar" data-i="' + i + '">Cambiar tiempos</button>' +
              '<button type="button" class="wvp-b wve-x" data-e="devolver" data-i="' + i + '">Volver a incluir</button></div>';
          }).join('')
        : '';
    }
    function alListo() {
      if (!listo()) return;
      cuts = cortesDe(tramosIni, dur);
      pintar();
    }
    // Reproductor: se maneja igual con YouTube que con archivo de video
    function onTick(t, d, estado) {
      if (typeof t === 'number') ahora = t;
      if (typeof d === 'number' && d > 0 && !listo()) { dur = d; alListo(); }
      if (typeof estado === 'number') suena = estado === 1;
      pintar();
    }
    var detener = function () { /* se completa al montar */ };

    if (opts.youtube) {
      var fr = document.createElement('iframe');
      fr.className = 'wvv-yt';
      fr.title = 'Video';
      fr.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      fr.allowFullscreen = true;
      fr.referrerPolicy = 'strict-origin-when-cross-origin';
      fr.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(opts.youtube) + '?enablejsapi=1&rel=0&modestbranding=1&playsinline=1&origin=' + encodeURIComponent(location.origin);
      var man = function (f, a) { try { fr.contentWindow.postMessage(JSON.stringify({ event: 'command', func: f, args: a || [] }), '*'); } catch (e) { /* nada */ } };
      var oir = function (ev) {
        if (ev.source !== fr.contentWindow) return;
        try {
          var d = typeof ev.data === 'string' ? JSON.parse(ev.data) : ev.data;
          if (d && d.info) onTick(d.info.currentTime, d.info.duration, d.info.playerState);
        } catch (e) { /* otro mensaje */ }
      };
      window.addEventListener('message', oir);
      fr.addEventListener('load', function () { try { fr.contentWindow.postMessage(JSON.stringify({ event: 'listening', id: 1, channel: 'widget' }), '*'); } catch (e) { /* nada */ } });
      marco.innerHTML = ''; marco.classList.add('yt'); marco.appendChild(fr);
      player = {
        play: function () { man('playVideo'); },
        pause: function () { man('pauseVideo'); },
        seek: function (t) { ahora = t; man('seekTo', [t, true]); pintar(); }
      };
      detener = function () { window.removeEventListener('message', oir); };
    } else {
      Promise.resolve().then(function () { return opts.url(); }).then(function (enlace) {
        if (!vivo) return;
        var v = document.createElement('video');
        v.src = enlace; v.controls = false; v.playsInline = true; v.preload = 'metadata';
        v.setAttribute('controlslist', 'nodownload');
        v.addEventListener('error', function () { marco.innerHTML = '<div class="wvv-estado error">No se pudo cargar el video.</div>'; });
        v.addEventListener('loadedmetadata', function () { onTick(v.currentTime, v.duration, v.paused ? 2 : 1); });
        v.addEventListener('timeupdate', function () { onTick(v.currentTime, v.duration, v.paused ? 2 : 1); });
        v.addEventListener('play', function () { onTick(v.currentTime, v.duration, 1); });
        v.addEventListener('pause', function () { onTick(v.currentTime, v.duration, 2); });
        marco.innerHTML = ''; marco.appendChild(v);
        player = {
          play: function () { v.play(); }, pause: function () { v.pause(); },
          seek: function (t) { v.currentTime = t; ahora = t; pintar(); }
        };
        detener = function () { try { v.pause(); v.removeAttribute('src'); v.load(); } catch (e) { /* nada */ } };
      }).catch(function (e) { marco.innerHTML = '<div class="wvv-estado error">' + esc((e && e.message) || 'No se pudo cargar el video.') + '</div>'; });
    }

    // Si YouTube no informa la duración, se pide a mano
    var espera = setTimeout(function () {
      if (listo() || !vivo) return;
      var t = prompt('No pudimos leer la duración del video. Escribila (minutos:segundos), por ejemplo 12:30:');
      var d = aSeg(t);
      if (d === d && d > 0) { dur = d; alListo(); }
    }, 8000);

    function ir(t) { if (player) player.seek(Math.max(0, Math.min(dur || t, t))); }
    function agregarCorte(a, b) {
      if (Math.abs(b - a) < 0.5) return toast('Esa parte es demasiado corta.');
      cuts = limpiar(cuts.concat([{ a: a, b: b }]), dur);
      pend = null; pintar();
    }
    function toast(t) { try { window.alert(t); } catch (e) { /* nada */ } }
    function cerrar() {
      vivo = false; clearTimeout(espera); detener();
      document.removeEventListener('keydown', tecla);
      el.remove();
      if (!document.querySelector('.wvp')) document.body.classList.remove('wvp-abierto');
    }
    function tecla(ev) {
      var tag = (ev.target && ev.target.tagName) || '';
      if (ev.key === 'Escape' && !document.querySelector('.wvp ~ .wvp')) cerrar();
      else if (ev.key === 'ArrowLeft' && !/INPUT|TEXTAREA/.test(tag)) ir(ahora - 5);
      else if (ev.key === 'ArrowRight' && !/INPUT|TEXTAREA/.test(tag)) ir(ahora + 5);
    }
    document.addEventListener('keydown', tecla);

    linea.addEventListener('click', function (ev) {
      if (!listo()) return;
      var r = linea.getBoundingClientRect();
      ir(((ev.clientX - r.left) / r.width) * dur);
    });

    el.addEventListener('click', async function (ev) {
      var b = ev.target.closest('[data-e]');
      if (!b) { if (ev.target === el) cerrar(); return; }
      var a = b.getAttribute('data-e'), i = +b.getAttribute('data-i');
      if (a === 'cerrar') return cerrar();
      if (!listo()) return;
      if (a === 'play') return suena ? player.pause() : player.play();
      if (a === 'atras') return ir(ahora - 5);
      if (a === 'adelante') return ir(ahora + 5);
      if (a === 'ini') { if (pend == null) { pend = ahora; return pintar(); } return agregarCorte(pend, ahora); }
      if (a === 'cancelar') { pend = null; return pintar(); }
      if (a === 'principio') return agregarCorte(0, ahora);
      if (a === 'final') return agregarCorte(ahora, dur);
      if (a === 'ir' && cuts[i]) return ir(Math.max(0, cuts[i].a - 2));
      if (a === 'devolver' && cuts[i]) { cuts.splice(i, 1); return pintar(); }
      if (a === 'ajustar' && cuts[i]) {
        var t = prompt('Parte quitada. Escribí desde y hasta separados por un guion, en minutos:segundos. Ejemplo: 1:20 - 2:05', reloj(cuts[i].a) + ' - ' + reloj(cuts[i].b));
        if (t == null) return;
        var p = t.split(/\s*[-–—]\s*/), x = aSeg(p[0]), y = aSeg(p[1]);
        if (!(x === x && y === y) || y <= x) return toast('Escribilo así: 1:20 - 2:05 (el final tiene que ser después del inicio).');
        cuts.splice(i, 1); cuts = limpiar(cuts.concat([{ a: x, b: y }]), dur); return pintar();
      }
      if (a === 'probar') {
        if (player) player.pause();
        var tr = tramosDe(cuts, dur);
        return window.WaveVisor.abrirVideo({ titulo: opts.titulo, youtube: opts.youtube, url: opts.url, tramos: tr });
      }
      if (a === 'guardar') {
        if (pend != null) return toast('Falta terminar la parte que empezaste a quitar (o tocá Cancelar).');
        b.disabled = true; b.textContent = 'Guardando…';
        try { await opts.guardar(tramosDe(cuts, dur)); cerrar(); }
        catch (e) { b.disabled = false; b.textContent = 'Guardar'; toast((e && e.message) || 'No se pudo guardar.'); }
      }
    });
    return { cerrar: cerrar };
  }

  window.WaveEditor.abrir = abrir;
  window.WaveEditor._calc = { limpiar: limpiar, cortesDe: cortesDe, tramosDe: tramosDe };
})();
