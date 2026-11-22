/* Trayecto Lectura: práctica de lectura en voz alta (palabras → frases → textos cortos) con registro.
   Sin IA: las palabras y frases salen de las mismas lecciones del alumno (o de una lista básica). */
(function () {
  'use strict';
  var sb = window.Wave && Wave.sb;
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function hoy() { return new Date().toLocaleDateString('en-CA', { timeZone: 'America/Argentina/Buenos_Aires' }); }
  function norm(t) { return String(t).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-zñ0-9\s]/g, ' ').replace(/\s+/g, ' ').trim(); }

  var NOMBRES = ['', 'Palabras cortas', 'Palabras más largas', 'Frases cortas', 'Frases más largas', 'Texto corto', 'Texto de un párrafo'];

  // Lista básica por si todavía no hay lecciones con texto
  var BASE = {
    1: 'sol mesa casa luna pato gato nube flor agua mano pelo libro lápiz silla perro cielo playa verde rojo dedo tarde noche puerta cama mapa piso lago rana'.split(' '),
    2: 'mariposa elefante escuela cuaderno ventana bicicleta cocina naranja estrella montaña semáforo teléfono chocolate computadora biblioteca zapatilla paraguas heladera tortuga camioneta'.split(' '),
    3: ['El gato duerme.', 'Mi mamá cocina rico.', 'La luna es redonda.', 'Hoy hace mucho sol.', 'Me gusta el mar.', 'El perro corre feliz.', 'Tengo un libro nuevo.', 'La nube es blanca.'],
    4: ['El perro de mi vecina corre por el parque.', 'Todas las tardes leo un cuento antes de dormir.', 'En la escuela aprendemos cosas nuevas cada día.', 'Mi abuela prepara una torta muy rica los domingos.', 'Cuando llueve me gusta mirar por la ventana.', 'El colectivo pasa por la puerta de mi casa.'],
    5: ['Ayer fuimos a la plaza con mis primos. Jugamos a la pelota hasta que se hizo de noche.', 'Mi gata se llama Luna. Le gusta dormir sobre el sillón cuando hace frío.', 'Hoy me levanté temprano. Tomé la leche y me fui a la escuela con mi mochila.'],
    6: ['Los sábados voy a la casa de mi abuelo. Él tiene una huerta con tomates, lechuga y zapallo. Me enseña a regar las plantas y a cuidar que crezcan fuertes. Después almorzamos todos juntos.', 'El río pasa cerca de mi barrio. Cuando hay sol, muchas familias se juntan en la orilla. Algunos pescan y otros solo miran cómo se mueve el agua. A mí me gusta escuchar los pájaros.']
  };

  // ---------- Armado de ítems a partir de las lecciones ----------
  var cacheTexto = null;
  async function fuentes() {
    if (cacheTexto) return cacheTexto;
    var pal = { 1: [], 2: [] }, fr = { 3: [], 4: [], 5: [], 6: [] };
    try {
      var q = await sb.from('lesson_steps').select('extracted_text').not('extracted_text', 'is', null).limit(8);
      var vistas = {};
      (q.data || []).forEach(function (r) {
        var t = String(r.extracted_text || '').slice(0, 30000).replace(/\s+/g, ' ');
        var orac = (t.match(/[^.!?]+[.!?]/g) || []).map(function (x) { return x.trim(); }).filter(function (x) { return /^[A-ZÁÉÍÓÚÑ¿¡"]/.test(x) && !/[0-9=_|\/\\]/.test(x) && x.length < 220; });
        orac.forEach(function (o, i) {
          var n = o.split(' ').length;
          if (n >= 3 && n <= 5) fr[3].push(o);
          else if (n >= 6 && n <= 10) fr[4].push(o);
          if (n >= 6 && n <= 14 && orac[i + 1]) { var o2 = orac[i + 1], n2 = o2.split(' ').length; if (n2 <= 14 && n + n2 <= 26) fr[5].push(o + ' ' + o2); }
          if (n <= 14 && orac[i + 2]) { var t3 = o + ' ' + orac[i + 1] + ' ' + orac[i + 2]; if (t3.split(' ').length <= 45 && t3.split(' ').length >= 25) fr[6].push(t3); }
        });
        (t.toLowerCase().match(/[a-záéíóúüñ]{3,12}/g) || []).forEach(function (w) {
          if (vistas[w]) return; vistas[w] = 1;
          if (w.length <= 5) pal[1].push(w); else if (w.length >= 6) pal[2].push(w);
        });
      });
    } catch (e) { /* queda la lista básica */ }
    cacheTexto = { pal: pal, fr: fr };
    return cacheTexto;
  }
  function mezclar(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var x = a[i]; a[i] = a[j]; a[j] = x; } return a; }
  function pedir(F, nivel, n) {
    var lecc = nivel <= 2 ? F.pal[nivel] : F.fr[nivel];
    var base = BASE[nivel];
    var pool = lecc.length >= 12 ? mezclar(lecc) : mezclar(lecc).concat(mezclar(base));
    var vistos = {}, r = [];
    pool.forEach(function (x) { if (r.length < n && !vistos[x]) { vistos[x] = 1; r.push(x); } });
    return r;
  }

  // ---------- Ventana ----------
  var abierta = null, reco = null;
  function parar() { try { if (reco) reco.abort(); } catch (e) { /* nada */ } reco = null; try { window.speechSynthesis && speechSynthesis.cancel(); } catch (e) { /* nada */ } }
  function cerrar() { parar(); if (abierta) { abierta.remove(); abierta = null; document.removeEventListener('keydown', alTeclado); } }
  function alTeclado(e) { if (e.key === 'Escape') cerrar(); }
  function ventana(titulo) {
    cerrar();
    var ov = document.createElement('div');
    ov.className = 'num-ov';
    ov.innerHTML = '<div class="num-box" role="dialog" aria-modal="true" aria-label="' + esc(titulo) + '" style="max-width:640px"><div class="num-cab"><h2>' + esc(titulo) + '</h2><button type="button" class="num-x" aria-label="Cerrar">×</button></div><div class="num-cuerpo"></div></div>';
    ov.addEventListener('click', function (e) { if (e.target === ov || e.target.closest('.num-x')) cerrar(); });
    document.body.appendChild(ov);
    document.addEventListener('keydown', alTeclado);
    abierta = ov;
    return ov.querySelector('.num-cuerpo');
  }

  function formato() {
    var L = { t: 1.25, i: 1.9, p: 0.3 };
    try { var g = JSON.parse(localStorage.getItem('wave_modo_lectura') || 'null'); if (g) { L.t = +g.t || L.t; L.i = +g.i || L.i; L.p = g.p === 0 ? 0 : (+g.p || L.p); } } catch (e) { /* nada */ }
    return 'font-size:' + (L.t + 0.25) + 'rem;line-height:' + L.i + ';word-spacing:' + L.p + 'em';
  }

  // ---------- Comparación de lo leído con lo pedido ----------
  function comparar(objetivo, dicho) {
    var pal = objetivo.split(/\s+/), bolsa = {};
    norm(dicho).split(' ').forEach(function (w) { if (w) bolsa[w] = (bolsa[w] || 0) + 1; });
    var marcas = pal.map(function (w) {
      var k = norm(w); if (!k) return true;
      if (bolsa[k] > 0) { bolsa[k]--; return true; }
      return false;
    });
    var bien = marcas.filter(Boolean).length;
    return { marcas: marcas, pal: pal, bien: bien, ok: bien / pal.length >= 0.8 };
  }

  async function estado(sid) {
    var r = await sb.from('practica_lectura').select('dia, nivel, total, bien, dificiles, ppm, created_at').eq('student_id', sid).order('created_at', { ascending: false }).limit(2);
    var f = r.data || [], h = hoy();
    return { hoy: f.filter(function (x) { return x.dia === h; })[0] || null, ultima: f[0] || null };
  }

  async function practica(sid) {
    var cuerpo = ventana('Práctica de lectura');
    cuerpo.innerHTML = '<p class="num-info">Preparando tu práctica…</p>';
    var st = { ultima: null }, F;
    try { st = await estado(sid); } catch (e) { /* empieza en el nivel 1 */ }
    F = await fuentes();
    if (!abierta) return;
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    var nivel = st.ultima ? Math.max(1, Math.min(6, st.ultima.nivel)) : 1, nivelMax = nivel;
    var S = { i: 0, bien: 0, racha: 0, fallas: 0, difs: [], seg: 0, palOk: 0, cola: [], total: 0, items: [] };
    var previas = ((st.ultima && st.ultima.dificiles) || []).slice(0, 3);
    function cuantos(n) { return n <= 2 ? 12 : n <= 4 ? 8 : 3; }
    S.total = cuantos(nivel);
    S.items = pedir(F, nivel, S.total);

    function siguiente() {
      if (S.i >= S.total) return fin();
      var item;
      if (previas.length && nivel <= 2 && (S.i === 3 || S.i === 7)) item = previas.shift(); else item = S.items[S.i % S.items.length] || BASE[nivel][0];
      S.actual = item; S.i++;
      var largo = item.split(/\s+/).length > 6;
      cuerpo.innerHTML = '<div class="pc-barra" role="progressbar"><span style="width:' + Math.round(((S.i - 1) / S.total) * 100) + '%"></span></div>' +
        '<p class="pc-prog">' + esc(NOMBRES[nivel]) + ' · ' + S.i + ' de ' + S.total + '</p>' +
        '<div class="lc-item" style="' + formato() + '">' + esc(item) + '</div>' +
        '<div class="num-fila lc-bot"><button type="button" class="num-b" data-a="oir">🔊 Escuchar</button>' +
        (SR ? '<button type="button" class="num-b num-b2" data-a="leer">🎤 Leer' + (largo ? '' : '') + '</button>' : '<button type="button" class="num-b num-b2" data-a="bien">Lo leí bien</button><button type="button" class="num-b" data-a="costo">Me costó</button>') +
        '</div><div class="pc-fb" aria-live="polite">' + (SR ? '<p class="num-info">Tocá 🎤 y leé en voz alta. Cuando termines, tocá de nuevo.</p>' : '<p class="num-info">Tu navegador no registra la voz. Leé en voz alta y marcá cómo te fue.</p>') + '</div>';
    }

    function resultado(cmp, segundos) {
      S.seg += segundos;
      var ok = cmp.ok;
      if (ok) { S.bien++; S.palOk += cmp.pal.length; S.racha++; S.fallas = 0; if (S.racha >= 3 && nivel < 6) { nivel++; nivelMax = Math.max(nivelMax, nivel); S.racha = 0; S.items = pedir(F, nivel, 12); S.total = S.i + cuantos(nivel); } }
      else { S.racha = 0; S.fallas++; cmp.pal.forEach(function (w, k) { if (!cmp.marcas[k]) { var c = norm(w); if (c && S.difs.indexOf(c) < 0 && S.difs.length < 10) S.difs.push(c); } }); if (S.fallas >= 3 && nivel > 1) { nivel--; S.fallas = 0; S.items = pedir(F, nivel, 12); S.total = S.i + cuantos(nivel); } }
      var vista = cmp.pal.map(function (w, k) { return '<span class="' + (cmp.marcas[k] ? 'lc-ok' : 'lc-no') + '">' + esc(w) + '</span>'; }).join(' ');
      var fb = cuerpo.querySelector('.pc-fb');
      cuerpo.querySelector('.lc-bot').remove();
      cuerpo.querySelector('.lc-item').innerHTML = vista;
      fb.innerHTML = '<div class="pc-res ' + (ok ? 'ok' : 'mal') + '">' + (ok ? '¡Muy bien!' : 'Casi. Las palabras en naranja son las que vamos a practicar.') + '</div>' +
        (ok ? '' : '<button type="button" class="num-b" data-a="siBien">Sí la leí bien</button> ') +
        '<button type="button" class="num-b num-b2" data-a="sig">' + (S.i >= S.total ? 'Terminar' : 'Siguiente') + '</button>';
      fb.querySelector('[data-a="sig"]').focus();
    }

    function escuchar() {
      var t0 = Date.now(), dicho = '', cortado = false;
      reco = new SR(); reco.lang = 'es-AR'; reco.continuous = true; reco.interimResults = false;
      reco.onresult = function (e) { for (var i = e.resultIndex; i < e.results.length; i++) dicho += ' ' + e.results[i][0].transcript; };
      reco.onerror = function (e) { cortado = true; if (e.error === 'not-allowed' || e.error === 'service-not-allowed') { SR = null; cuerpo.querySelector('.pc-fb').innerHTML = '<p class="num-info">No pudimos usar el micrófono. Leé en voz alta y marcá cómo te fue.</p><button type="button" class="num-b num-b2" data-a="bien">Lo leí bien</button> <button type="button" class="num-b" data-a="costo">Me costó</button>'; } };
      reco.onend = function () { if (cortado) return; var seg = Math.max(1, Math.round((Date.now() - t0) / 1000)); reco = null; if (!abierta) return; resultado(comparar(S.actual, dicho), seg); };
      try { reco.start(); } catch (e) { return; }
      var b = cuerpo.querySelector('[data-a="leer"]'); b.dataset.a = 'listo'; b.textContent = '✔ Listo';
      cuerpo.querySelector('.pc-fb').innerHTML = '<p class="num-info">Escuchando… leé en voz alta.</p>';
    }
    function oir() {
      try {
        speechSynthesis.cancel();
        var u = new SpeechSynthesisUtterance(S.actual); u.lang = 'es-AR'; u.rate = 0.85;
        var v = (speechSynthesis.getVoices() || []).filter(function (x) { return /^es/i.test(x.lang); })[0]; if (v) u.voice = v;
        speechSynthesis.speak(u);
      } catch (e) { /* sin voz */ }
    }
    function manual(ok) {
      var pal = S.actual.split(/\s+/);
      resultado({ pal: pal, marcas: pal.map(function () { return ok; }), bien: ok ? pal.length : 0, ok: ok }, 0);
    }

    cuerpo.addEventListener('click', function (e) {
      var b = e.target.closest('[data-a]'); if (!b) return;
      var a = b.dataset.a;
      if (a === 'oir') oir();
      else if (a === 'leer') escuchar();
      else if (a === 'listo') { try { reco.stop(); } catch (x) { /* nada */ } }
      else if (a === 'bien') manual(true);
      else if (a === 'costo') manual(false);
      else if (a === 'siBien') {
        // la voz se equivocó: se corrige lo anotado
        S.bien++; S.palOk += S.actual.split(/\s+/).length; S.fallas = 0; var k = S.difs.length; S.difs = S.difs.filter(function (w) { return S.actual.toLowerCase().indexOf(w) < 0 && norm(S.actual).split(' ').indexOf(w) < 0; });
        b.remove(); cuerpo.querySelector('.pc-res').className = 'pc-res ok'; cuerpo.querySelector('.pc-res').textContent = '¡Muy bien! Lo anotamos como bien leído.';
      }
      else if (a === 'sig') siguiente();
    });

    async function fin() {
      var minutos = S.seg / 60, ppm = S.seg > 0 && S.palOk > 0 ? Math.round(S.palOk / minutos) : null;
      var ant = st.ultima && st.ultima.ppm ? Math.round(st.ultima.ppm) : null;
      cuerpo.innerHTML = '<div class="pc-fin"><div class="pc-trofeo" aria-hidden="true">🌟</div><h3>¡Listo por hoy!</h3><p>Leíste bien <b>' + S.bien + '</b> de ' + S.i + '.</p>' +
        (ppm ? '<p>Leíste unas <b>' + ppm + '</b> palabras por minuto' + (ant ? (ppm > ant ? ' — ¡más que la última vez!' : '.') : '.') + '</p>' : '') +
        (S.difs.length ? '<p class="num-info">Vamos a repasar: ' + esc(S.difs.slice(0, 5).join(', ')) + '. Van a volver mañana.</p>' : '') +
        '<button type="button" class="num-b num-b2" data-cerrar="1">Cerrar</button></div>';
      cuerpo.querySelector('[data-cerrar]').addEventListener('click', function () { cerrar(); document.dispatchEvent(new CustomEvent('wave-num-practica')); });
      try {
        await sb.from('practica_lectura').insert({ student_id: sid, dia: hoy(), nivel: nivelMax, total: S.i, bien: S.bien, dificiles: S.difs, segundos: S.seg, ppm: ppm, con_voz: !!SR });
      } catch (e) { /* si no se guarda, igual terminó */ }
    }
    siguiente();
  }

  async function tarjetaPractica(sid) {
    var h = null;
    try { h = (await estado(sid)).hoy; } catch (e) { /* sin estado */ }
    return '<section class="num-card"><div><h2>Práctica de lectura de hoy</h2><p>' + (h ? 'Hecha hoy ✓ Leíste bien ' + h.bien + ' de ' + h.total + '.' : 'Unos 10 minutos. Empezás con palabras y vas pasando a frases y textos.') + '</p></div>' +
      '<button type="button" class="num-b num-b2" data-lec-practica="1" data-sid="' + esc(sid) + '">' + (h ? 'Hacer otra vez' : 'Empezar') + '</button></section>';
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-lec-practica]');
    if (b && b.getAttribute('data-sid')) practica(b.getAttribute('data-sid'));
  });

  window.WaveLectura = { practica: practica, tarjetaPractica: tarjetaPractica, comparar: comparar };
})();
