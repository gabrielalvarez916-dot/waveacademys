// Panel admin · Videos: revisar los videos candidatos de cada lección y elegir el mejor.
// Lee video_candidatos (los llena el script buscar_videos.py). Se pueden elegir uno o más videos por lección:
// los elegidos pasan solos a la clase de la lección (Contenido) y desde acá se pueden editar (recortar) antes de publicar.
(function () {
  var sb = Wave.sb;
  var vista = null;
  var B = null;   // { levels, grades, subjects, totales }
  var D = null;   // { temas: [{ id, title, lecs: [] }], cands: { lessonId: [] }, busq: { lessonId: estado } }
  var E = { grade: '', subject: '', estado: 'sin_elegir' };

  var ESTADOS = [
    { id: 'sin_elegir', txt: 'Sin elegir' },
    { id: 'elegidas', txt: 'Elegidas' },
    { id: 'sin_cand', txt: 'Sin candidatos' },
    { id: 'sin_buscar', txt: 'Sin buscar' },
    { id: 'todas', txt: 'Todas' }
  ];

  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function minutos(seg) {
    if (!seg) return '';
    var m = Math.floor(seg / 60), s = seg % 60;
    return m + ':' + (s < 10 ? '0' : '') + s;
  }
  function nombreGrado(g) {
    var nivel = B.levels.filter(function (l) { return l.id === g.level_id; })[0];
    return (nivel ? nivel.name + ' · ' : '') + (g.name || (g.year_number + '.º año'));
  }
  function aviso(txt, error) {
    var t = document.createElement('div');
    t.className = 'wv-toast' + (error ? ' error' : '');
    t.textContent = txt;
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, 2600);
  }

  async function cargarBase() {
    var r = await Promise.all([
      sb.from('levels').select('id, name, position').order('position'),
      sb.from('grades').select('id, level_id, year_number, name').order('year_number'),
      sb.from('subjects').select('id, grade_id, name, variant, position').order('position').limit(1000),
      sb.from('lessons').select('id', { count: 'exact', head: true }).is('twin_of', null),
      sb.from('video_busqueda').select('lesson_id', { count: 'exact', head: true }),
      sb.from('video_candidatos').select('id', { count: 'exact', head: true }).eq('elegido', true)
    ]);
    r.forEach(function (x) { if (x.error) throw x.error; });
    var niveles = r[0].data;
    var grados = r[1].data.slice().sort(function (a, b) {
      var pa = niveles.map(function (n) { return n.id; }).indexOf(a.level_id);
      var pb = niveles.map(function (n) { return n.id; }).indexOf(b.level_id);
      return pa - pb || a.year_number - b.year_number;
    });
    B = { levels: niveles, grades: grados, subjects: r[2].data, totales: { maestras: r[3].count, buscadas: r[4].count, elegidas: r[5].count } };
    if (!E.grade && grados.length) E.grade = grados[0].id;
  }

  async function refrescarTotales() {
    var r = await Promise.all([
      sb.from('video_busqueda').select('lesson_id', { count: 'exact', head: true }),
      sb.from('video_candidatos').select('id', { count: 'exact', head: true }).eq('elegido', true)
    ]);
    if (!r[0].error) B.totales.buscadas = r[0].count;
    if (!r[1].error) B.totales.elegidas = r[1].count;
    var el = document.getElementById('vd-resumen');
    if (el) el.innerHTML = htmlResumen();
  }

  function materiasDelAnio() { return B.subjects.filter(function (s) { return s.grade_id === E.grade; }); }

  async function cargarMateria() {
    D = { temas: [], cands: {}, busq: {}, biblio: {} };
    if (!E.subject) return;
    var t = await sb.from('topics').select('id, title, position, lessons(id, title, position, twin_of)').eq('subject_id', E.subject).order('position');
    if (t.error) throw t.error;
    var ids = [];
    D.temas = t.data.map(function (tema) {
      var lecs = (tema.lessons || []).filter(function (l) { return !l.twin_of; }).sort(function (a, b) { return a.position - b.position; });
      lecs.forEach(function (l) { ids.push(l.id); });
      return { id: tema.id, title: tema.title, lecs: lecs };
    });
    if (!ids.length) return;
    var r = await Promise.all([
      sb.from('video_candidatos').select('id, lesson_id, youtube_id, titulo, canal, duracion_seg, miniatura, orden, elegido').in('lesson_id', ids).order('orden').limit(5000),
      sb.from('video_busqueda').select('lesson_id, estado').in('lesson_id', ids).limit(2000),
      sb.from('biblioteca_items').select('id, candidato_id').eq('subject_id', E.subject).not('candidato_id', 'is', null)
    ]);
    r.forEach(function (x) { if (x.error) throw x.error; });
    r[0].data.forEach(function (c) { (D.cands[c.lesson_id] = D.cands[c.lesson_id] || []).push(c); });
    r[1].data.forEach(function (b) { D.busq[b.lesson_id] = b.estado; });
    r[2].data.forEach(function (b) { D.biblio[b.candidato_id] = b.id; });
  }

  function estadoLeccion(id) {
    var cs = D.cands[id] || [];
    if (cs.some(function (c) { return c.elegido; })) return 'elegidas';
    if (cs.length) return 'sin_elegir';
    if (D.busq[id]) return 'sin_cand';
    return 'sin_buscar';
  }

  function htmlResumen() {
    var t = B.totales;
    return '<div class="wv-stat"><small>Lecciones a resolver</small><b>' + t.maestras + '</b></div>' +
      '<div class="wv-stat"><small>Ya buscadas</small><b>' + t.buscadas + '</b></div>' +
      '<div class="wv-stat"><small>Con video elegido</small><b>' + t.elegidas + '</b></div>';
  }

  function htmlCand(c) {
    return '<div class="vd-cand' + (c.elegido ? ' sel' : '') + '" data-cand="' + c.id + '">' +
      '<button type="button" class="vd-thumb" data-ver="' + esc(c.youtube_id) + '" aria-label="Ver el video">' +
        '<img src="' + esc(c.miniatura || ('https://i.ytimg.com/vi/' + c.youtube_id + '/hqdefault.jpg')) + '" alt="" loading="lazy">' +
        '<span class="vd-play">▶</span>' +
        (c.duracion_seg ? '<span class="vd-dur">' + minutos(c.duracion_seg) + '</span>' : '') +
      '</button>' +
      '<div class="vd-ctit" title="' + esc(c.titulo) + '">' + esc(c.titulo) + '</div>' +
      '<div class="vd-ccanal">' + esc(c.canal) + '</div>' +
      '<div class="vd-cacc">' +
        (c.elegido
          ? '<button type="button" class="wv-btn mini" data-editar="' + c.id + '">✂️ Editar</button><button type="button" class="wv-btn mini suave" data-archivo="' + c.id + '" title="Reemplaza el video incrustado por el archivo que te dio el dueño">' + (c.conArchivo ? '⬆ Cambiar archivo' : '⬆ Subir archivo del dueño') + '</button><button type="button" class="wv-btn mini peligro" data-quitar="' + c.id + '">Quitar elección</button>'
          : '<button type="button" class="wv-btn mini" data-elegir="' + c.id + '">Elegir este</button>') +
        '<button type="button" class="wv-btn mini suave" data-biblio="' + c.id + '" title="Lo ven todos los alumnos como recurso opcional, sin ponerlo en la misión">' + (D.biblio[c.id] ? '📚 En la biblio-videoteca ✓' : '📚 A la biblio-videoteca') + '</button>' +
        '<a class="vd-yt" href="https://www.youtube.com/watch?v=' + esc(c.youtube_id) + '" target="_blank" rel="noopener">Abrir en YouTube</a>' +
      '</div></div>';
  }

  function htmlLeccion(l, tema) {
    var est = estadoLeccion(l.id);
    var pill = { elegidas: ['ok', 'Video elegido'], sin_elegir: ['pend', 'Sin elegir'], sin_cand: ['deuda', 'Sin candidatos'], sin_buscar: ['off', 'Sin buscar'] }[est];
    var cs = D.cands[l.id] || [];
    return '<article class="vd-lec" data-lec="' + l.id + '">' +
      '<header class="vd-lec-cab"><div><small class="vd-tema">' + esc(tema.title) + '</small><b class="vd-lec-t">' + esc(l.title) + '</b></div>' +
      '<span class="wv-pill ' + pill[0] + '">' + pill[1] + '</span></header>' +
      (cs.length ? '<div class="vd-cands">' + cs.map(htmlCand).join('') + '</div>'
        : '<div class="vd-nada">' + (est === 'sin_buscar' ? 'Todavía no se buscaron videos para esta lección.' : 'La búsqueda no encontró videos para esta lección.') + '</div>') +
      '</article>';
  }

  function pintarLista() {
    var cont = document.getElementById('vd-lista');
    if (!cont) return;
    if (!E.subject) { cont.innerHTML = '<div class="wv-vacio">Elegí una materia para ver sus lecciones.</div>'; return; }
    var html = '', n = 0, total = 0;
    D.temas.forEach(function (tema) {
      tema.lecs.forEach(function (l) {
        total++;
        if (E.estado !== 'todas' && estadoLeccion(l.id) !== E.estado) return;
        n++;
        html += htmlLeccion(l, tema);
      });
    });
    var hechas = 0;
    D.temas.forEach(function (tema) { tema.lecs.forEach(function (l) { if (estadoLeccion(l.id) === 'elegidas') hechas++; }); });
    var cab = '<p class="wv-sub vd-prog">' + hechas + ' de ' + total + ' lecciones de esta materia ya tienen video elegido.</p>';
    cont.innerHTML = cab + (html || '<div class="wv-vacio">No hay lecciones con este filtro en esta materia.</div>');
  }

  function pintarControles() {
    var grados = B.grades.map(function (g) { return '<option value="' + g.id + '"' + (g.id === E.grade ? ' selected' : '') + '>' + esc(nombreGrado(g)) + '</option>'; }).join('');
    var materias = '<option value="">Elegí una materia…</option>' + materiasDelAnio().map(function (s) {
      return '<option value="' + s.id + '"' + (s.id === E.subject ? ' selected' : '') + '>' + esc(s.name + (s.variant ? ' · ' + s.variant : '')) + '</option>';
    }).join('');
    var chips = ESTADOS.map(function (e) { return '<button type="button" class="wv-chip' + (e.id === E.estado ? ' on' : '') + '" data-estado="' + e.id + '">' + e.txt + '</button>'; }).join('');
    document.getElementById('vd-controles').innerHTML =
      '<select id="vd-grado" class="vd-sel" aria-label="Año">' + grados + '</select>' +
      '<select id="vd-materia" class="vd-sel" aria-label="Materia">' + materias + '</select>' +
      '<div class="wv-filtros">' + chips + '</div>';
  }

  function ponerReproductor(btn) {
    var id = btn.getAttribute('data-ver');
    var caja = document.createElement('div');
    caja.className = 'vd-player';
    caja.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0" title="Video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
    btn.replaceWith(caja);
  }

  // ---- Conexión con la lección: lo elegido pasa a la Clase explicativa ----
  async function pasoVideo(lecId, crear) {
    var r = await sb.from('lesson_steps').select('id, stream_uid, content').eq('lesson_id', lecId).eq('step_type', 'video').maybeSingle();
    if (r.error) throw r.error;
    if (r.data || !crear) return r.data;
    var ins = await sb.from('lesson_steps').insert({ lesson_id: lecId, step_type: 'video', position: 1 }).select('id, stream_uid, content').single();
    if (ins.error) throw ins.error;
    return ins.data;
  }
  function listaDe(paso) {
    var c = (paso && paso.content) || {};
    if (Array.isArray(c.videos) && c.videos.length) return c.videos.map(function (x) { var o = Object.assign({}, x); o.nombre = x.nombre || ''; o.tramos = x.tramos || []; return o; });
    return paso && paso.stream_uid ? [{ uid: paso.stream_uid, nombre: '', tramos: (c.tramos && c.tramos.length ? c.tramos : (c.inicio || c.fin ? [{ i: c.inicio || 0, f: c.fin || 0 }] : [])) }] : [];
  }
  async function guardarLista(paso, lista) {
    var ct = Object.assign({}, paso.content || {}); // conserva la clase animada si la hay
    if (lista.length) ct.videos = lista; else delete ct.videos;
    delete ct.tramos; delete ct.inicio; delete ct.fin;
    var r = await sb.from('lesson_steps').update({ stream_uid: lista.length ? lista[0].uid : null, content: ct }).eq('id', paso.id);
    if (r.error) throw r.error;
  }
  // Posición de un video elegido dentro de la lección: incrustado (yt:ID) o ya reemplazado por el archivo del dueño
  function posDe(lista, ytId) {
    for (var i = 0; i < lista.length; i++) { if (!lista[i].intro && (lista[i].uid === 'yt:' + ytId || lista[i].yt === ytId)) return i; }
    return -1;
  }
  async function subidas(body) {
    var r = await sb.functions.invoke('content-upload', { body: body });
    if (r.error) {
      var msg = 'No se pudo completar. Intentá de nuevo.';
      try { var c = await r.error.context.json(); if (c && c.error) msg = c.error; } catch (e) { /* genérico */ }
      throw new Error(msg);
    }
    if (r.data && r.data.error) throw new Error(r.data.error);
    return r.data;
  }
  function enviar(url, cuerpo, onProg) {
    return new Promise(function (ok, mal) {
      var x = new XMLHttpRequest();
      x.open('PUT', url);
      x.upload.onprogress = function (ev) { if (ev.lengthComputable && onProg) onProg(Math.round(ev.loaded * 100 / ev.total)); };
      x.onload = function () { (x.status >= 200 && x.status < 300) ? ok() : mal(new Error('El servidor rechazó el archivo (' + x.status + ').')); };
      x.onerror = function () { mal(new Error('No se pudo subir el archivo. Revisá tu conexión.')); };
      x.send(cuerpo);
    });
  }
  // Reemplaza el video incrustado por el archivo que te dio el dueño (sin anuncios, con los mismos recortes)
  async function subirArchivo(candId, archivo, btn) {
    var cand = null, lecId = null;
    Object.keys(D.cands).forEach(function (k) { D.cands[k].forEach(function (c) { if (c.id === candId) { cand = c; lecId = k; } }); });
    if (!cand) return;
    var rv = await WaveEditor.revisarMp4(archivo);
    if (!rv.ok && !confirm(WaveEditor.avisoMp4)) throw new Error('Subida cancelada');
    var d = await subidas({ action: 'r2_upload_url', lesson_id: lecId, filename: archivo.name });
    await enviar(d.url, archivo, function (pc) { btn.textContent = 'Subiendo… ' + pc + '%'; });
    var paso = await pasoVideo(lecId, true), lista = listaDe(paso), pos = posDe(lista, cand.youtube_id);
    var nuevo = { uid: d.key, nombre: archivo.name, tramos: pos >= 0 ? lista[pos].tramos : [], yt: cand.youtube_id };
    var viejo = pos >= 0 ? lista[pos] : null;
    if (pos >= 0) lista[pos] = nuevo; else lista.push(nuevo);
    await guardarLista(paso, lista);
    if (viejo && viejo.yt && !/^yt:/.test(viejo.uid)) { try { await subidas({ action: 'stream_delete', uid: viejo.uid }); } catch (e) { /* huérfano */ } }
    cand.conArchivo = true;
    repintarLeccion(lecId);
    aviso('Archivo subido: esta lección ya usa el video del dueño, sin anuncios');
  }

  async function pasarALeccion(lecId, ytId, poner) {
    var paso = await pasoVideo(lecId, poner);
    if (!paso) return;
    var lista = listaDe(paso), pos = posDe(lista, ytId);
    if (poner && pos < 0) lista.push({ uid: 'yt:' + ytId, nombre: '', tramos: [] });
    else if (!poner && pos >= 0) {
      var quitado = lista[pos], key = quitado.uid;
      lista = lista.filter(function (x) { return !((x.uid === key && !x.intro) || (x.intro && x.grp === key)); });
      var sigue = lista.some(function (x) { return x.uid === key; });
      if (quitado.yt && !/^yt:/.test(key) && !sigue) { try { await subidas({ action: 'stream_delete', uid: key }); } catch (e) { /* archivo huérfano */ } }
    } else return;
    await guardarLista(paso, lista);
  }
  async function editar(candId) {
    var cand = null, lecId = null;
    Object.keys(D.cands).forEach(function (k) { D.cands[k].forEach(function (c) { if (c.id === candId) { cand = c; lecId = k; } }); });
    if (!cand) return;
    await pasarALeccion(lecId, cand.youtube_id, true);
    var paso = await pasoVideo(lecId, false), lista = listaDe(paso), item = lista[posDe(lista, cand.youtube_id)];
    if (!item) return;
    var key = item.uid, blq = WaveEditor.bloque(lista, key);
    var ri = await sb.from('app_settings').select('value').eq('key', 'intro_wave').maybeSingle();
    var introW = ri.data && ri.data.value && ri.data.value.uid ? ri.data.value : null;
    var itemVisor = function (e) {
      return /^yt:/.test(e.uid) ? { youtube: e.uid.slice(3), tramos: e.tramos }
        : { tramos: e.tramos, url: async function () { return (await subidas({ action: 'stream_token', uid: e.uid, preview: true })).url; } };
    };
    var conf = {
      titulo: cand.titulo, tramos: blq.tramos, inserts: blq.inserts, intro: !!introW,
      guardar: async function (tramos, ins, dur) {
        var p2 = await pasoVideo(lecId, false), l2 = listaDe(p2), q = posDe(l2, cand.youtube_id);
        if (q < 0) return;
        var src = { uid: l2[q].uid, nombre: l2[q].nombre, yt: l2[q].yt };
        var nuevas = WaveEditor.secuencia(src, tramos, ins, dur, introW || { uid: '', tramos: [] });
        if (!ins.length) nuevas.forEach(function (n) { delete n.grp; });
        await guardarLista(p2, WaveEditor.reemplazar(l2, src.uid, nuevas));
        aviso(ins.length ? 'Guardado, con la intro en ' + ins.length + (ins.length > 1 ? ' lugares' : ' lugar') : (tramos.length ? 'Recorte guardado' : 'Se muestra el video entero'));
      },
      vistaPrevia: function (tr, ins, dur) { return WaveEditor.secuencia({ uid: key }, tr, ins, dur, introW).map(itemVisor); }
    };
    if (!/^yt:/.test(key)) conf.url = async function () { return (await subidas({ action: 'stream_token', uid: key, preview: true })).url; };
    else conf.youtube = cand.youtube_id;
    WaveEditor.abrir(conf);
  }

  async function elegir(candId) {
    var cand = null, lecId = null;
    Object.keys(D.cands).forEach(function (k) { D.cands[k].forEach(function (c) { if (c.id === candId) { cand = c; lecId = k; } }); });
    if (!cand) return;
    var r2 = await sb.from('video_candidatos').update({ elegido: true }).eq('id', candId);
    if (r2.error) throw r2.error;
    cand.elegido = true;
    await pasarALeccion(lecId, cand.youtube_id, true);
    repintarLeccion(lecId);
    aviso('Video elegido y agregado a la lección');
    refrescarTotales();
  }

  // Va a la biblio-videoteca de la materia (recurso opcional para todos los alumnos), sin ponerlo en la misión
  async function biblio(candId) {
    var cand = null, lecId = null, temaId = null;
    Object.keys(D.cands).forEach(function (k) { D.cands[k].forEach(function (c) { if (c.id === candId) { cand = c; lecId = k; } }); });
    if (!cand) return;
    D.temas.forEach(function (t) { t.lecs.forEach(function (l) { if (l.id === lecId) temaId = t.id; }); });
    if (D.biblio[candId]) {
      var d = await sb.from('biblioteca_items').delete().eq('id', D.biblio[candId]);
      if (d.error) throw d.error;
      delete D.biblio[candId];
      aviso('Quitado de la biblio-videoteca');
    } else {
      var i = await sb.from('biblioteca_items').insert({ tipo: 'video', titulo: cand.titulo, descripcion: cand.canal, url: 'https://www.youtube.com/watch?v=' + cand.youtube_id, subject_id: E.subject, topic_id: temaId, candidato_id: candId }).select('id').single();
      if (i.error) throw i.error;
      D.biblio[candId] = i.data.id;
      aviso('Agregado a la biblio-videoteca');
    }
    repintarLeccion(lecId);
  }

  async function quitar(candId) {
    var cand = null, lecId = null;
    Object.keys(D.cands).forEach(function (k) { D.cands[k].forEach(function (c) { if (c.id === candId) { cand = c; lecId = k; } }); });
    if (!cand) return;
    var r = await sb.from('video_candidatos').update({ elegido: false }).eq('id', candId);
    if (r.error) throw r.error;
    cand.elegido = false;
    await pasarALeccion(lecId, cand.youtube_id, false);
    repintarLeccion(lecId);
    aviso('Elección quitada (también de la lección)');
    refrescarTotales();
  }

  function repintarLeccion(lecId) {
    var nodo = document.querySelector('[data-lec="' + lecId + '"]');
    if (!nodo) return;
    var l = null, tema = null;
    D.temas.forEach(function (t) { t.lecs.forEach(function (x) { if (x.id === lecId) { l = x; tema = t; } }); });
    if (!l) return;
    // Si el filtro actual ya no la incluye, se deja visible hasta la próxima vez para no perder el lugar
    var tmp = document.createElement('div');
    tmp.innerHTML = htmlLeccion(l, tema);
    nodo.replaceWith(tmp.firstChild);
  }

  async function cambiarMateria() {
    var cont = document.getElementById('vd-lista');
    if (cont) cont.innerHTML = '<div class="wv-vacio">Cargando…</div>';
    try {
      await cargarMateria();
      pintarLista();
    } catch (e) {
      console.error(e);
      if (cont) cont.innerHTML = '<div class="wv-vacio">No pudimos cargar las lecciones.<br><small>' + esc((e && (e.message || e.details)) || e) + '</small></div>';
    }
  }

  function enlazar() {
    vista.addEventListener('change', function (ev) {
      if (ev.target.id === 'vd-grado') {
        E.grade = ev.target.value; E.subject = '';
        pintarControles(); D = { temas: [], cands: {}, busq: {} }; pintarLista();
      } else if (ev.target.id === 'vd-materia') {
        E.subject = ev.target.value;
        cambiarMateria();
      }
    });
    vista.addEventListener('click', function (ev) {
      var b = ev.target.closest('button');
      if (!b) return;
      if (b.hasAttribute('data-estado')) { E.estado = b.getAttribute('data-estado'); pintarControles(); pintarLista(); return; }
      if (b.hasAttribute('data-ver')) { ponerReproductor(b); return; }
      if (b.hasAttribute('data-biblio')) { b.disabled = true; biblio(b.getAttribute('data-biblio')).catch(function (e) { console.error(e); b.disabled = false; aviso('No se pudo guardar: ' + ((e && e.message) || e), true); }); return; }
      if (b.hasAttribute('data-elegir')) {
        b.disabled = true;
        elegir(b.getAttribute('data-elegir')).catch(function (e) { console.error(e); b.disabled = false; aviso('No se pudo guardar: ' + ((e && e.message) || e), true); });
        return;
      }
      if (b.hasAttribute('data-archivo')) {
        var idc = b.getAttribute('data-archivo'), inp = document.createElement('input');
        inp.type = 'file'; inp.accept = 'video/*';
        inp.addEventListener('change', function () {
          var f = inp.files && inp.files[0]; if (!f) return;
          var txt = b.textContent; b.disabled = true; b.textContent = 'Preparando…';
          subirArchivo(idc, f, b).catch(function (e) { console.error(e); b.disabled = false; b.textContent = txt; aviso('No se pudo subir: ' + ((e && e.message) || e), true); });
        });
        inp.click();
        return;
      }
      if (b.hasAttribute('data-editar')) {
        editar(b.getAttribute('data-editar')).catch(function (e) { console.error(e); aviso('No se pudo abrir el editor: ' + ((e && e.message) || e), true); });
        return;
      }
      if (b.hasAttribute('data-quitar')) {
        b.disabled = true;
        quitar(b.getAttribute('data-quitar')).catch(function (e) { console.error(e); b.disabled = false; aviso('No se pudo guardar: ' + ((e && e.message) || e), true); });
      }
    });
  }

  // ---- Optimizar videos: reordena los MP4 subidos para que abran al instante en el editor (sin recodificar, sin costo de IA) ----
  async function contarOpt() {
    var r = await sb.functions.invoke('optimizar-videos', { body: { action: 'contar' } });
    if (r.error || !r.data || r.data.error) throw new Error((r.data && r.data.error) || (r.error && r.error.message) || 'No se pudo consultar');
    return r.data;
  }
  function textoOpt(c) {
    return c.pendientes ? c.pendientes + ' de ' + c.total + ' videos todavía sin preparar. Tocá el botón UNA vez y esperá.' : (c.total ? 'Todos los videos subidos están preparados ✔ (el editor abre rápido)' : 'Todavía no hay videos subidos como archivo.');
  }
  var _optT = null;
  // Mientras corre en GitHub: el botón queda bloqueado y se muestra el avance
  function vigilarOpt(total0, inicio, hechos0) {
    var btn = document.getElementById('vd-opt-btn'), txt = document.getElementById('vd-opt-txt');
    if (!btn || !txt) return;
    if (_optT) clearInterval(_optT);
    btn.disabled = true;
    var LINK = ' <a href="https://github.com/gabrielalvarez916-dot/waveacademys/actions/workflows/optimizar-videos.yml" target="_blank" rel="noopener">Ver el avance en GitHub</a>';
    var pinta = function (hechos) {
      var min = Math.floor((Date.now() - inicio) / 60000);
      txt.innerHTML = '⏳ Procesando en segundo plano: ' + hechos + ' de ' + total0 + ' terminados (hace ' + (min < 1 ? 'menos de 1' : min) + ' min). No toques nada: el número sube cuando termina cada video. Podés seguir trabajando.' + LINK;
    };
    var vueltas = 0;
    var tic = async function () {
      vueltas++;
      try {
        var c2 = await contarOpt();
        if (!c2.pendientes) { clearInterval(_optT); _optT = null; txt.textContent = 'Listo: ' + total0 + ' video(s) preparados ✔ Ya podés abrir el editor.'; return; }
        if (!c2.corriendo && vueltas > 2) { clearInterval(_optT); _optT = null; txt.innerHTML = 'El proceso terminó pero quedaron ' + c2.pendientes + ' sin preparar (puede haber fallado alguno).' + LINK; btn.disabled = false; return; }
        pinta(Math.max(0, total0 - c2.pendientes));
      } catch (e) { /* sigue */ }
      if (vueltas > 120) { clearInterval(_optT); _optT = null; btn.disabled = false; }
    };
    pinta(hechos0 || 0);
    tic();
    _optT = setInterval(tic, 15000);
  }
  async function iniciarOptimizar() {
    var btn = document.getElementById('vd-opt-btn'), txt = document.getElementById('vd-opt-txt');
    if (!btn || !txt) return;
    try {
      var c = await contarOpt();
      if (c.corriendo && c.pendientes) { vigilarOpt(c.total, Date.now(), c.total - c.pendientes); }
      else { txt.textContent = textoOpt(c); btn.disabled = !c.pendientes; }
    } catch (e) { txt.textContent = 'No se pudo consultar: ' + ((e && e.message) || e); }
    btn.onclick = async function () {
      btn.disabled = true; txt.textContent = 'Lanzando…';
      try {
        var r = await sb.functions.invoke('optimizar-videos', { body: { action: 'pedir' } });
        if (r.error || !r.data || r.data.error) throw new Error((r.data && r.data.error) || (r.error && r.error.message) || 'No se pudo lanzar');
        if (!r.data.pendientes) { txt.textContent = 'No hay videos para preparar ✔'; return; }
        if (!r.data.lanzado) { txt.textContent = 'No se pudo lanzar solo (' + (r.data.aviso || 'error') + '). Hacelo a mano: GitHub > Actions > "Optimizar videos" > Run workflow.'; btn.disabled = false; return; }
        vigilarOpt(r.data.pendientes, Date.now());
      } catch (e) { txt.textContent = 'Error: ' + ((e && e.message) || e); btn.disabled = false; }
    };
  }

  async function abrir(contenedor) {
    vista = contenedor;
    vista.innerHTML = '<h1 class="wv-titulo">Videos de las lecciones</h1>' +
      '<p class="wv-sub">Para cada lección, el sistema encontró hasta 4 videos de YouTube. Mirá cada uno y elegí el mejor.</p>' +
      '<div class="wv-vacio">Cargando…</div>';
    try {
      await cargarBase();
    } catch (e) {
      console.error(e);
      vista.innerHTML = '<div class="wv-vacio">No pudimos cargar los videos.<br><small>' + esc((e && (e.message || e.details)) || e) + '</small></div>';
      return;
    }
    vista.innerHTML = '<h1 class="wv-titulo">Videos de las lecciones</h1>' +
      '<p class="wv-sub">Para cada lección, el sistema encontró hasta 4 videos de YouTube. Mirá cada uno y elegí el mejor.</p>' +
      '<div class="wv-resumen" id="vd-resumen">' + htmlResumen() + '</div>' +
      '<div class="wv-tools" id="vd-optimizar"><button type="button" class="wv-btn" id="vd-opt-btn">⚡ Optimizar MIS videos cargados (no toca los de YouTube)</button> <span id="vd-opt-txt" class="wv-sub">Revisando…</span></div>' +
      '<div class="wv-tools vd-tools" id="vd-controles"></div>' +
      '<details class="vd-bib" style="margin:14px 0"><summary style="cursor:pointer;font-weight:800">📚 Biblioteca: subir PDF y actividades</summary><div id="bl-caja" style="margin-top:10px"></div></details>' +
      '<div id="vd-lista"></div>';
    BL = { nivel: '', grado: '', materia: '', mision: '', tipo: 'texto', temas: [], items: [] };
    pintarBiblio(); enlazarBiblio();
    pintarControles();
    iniciarOptimizar();
    D = { temas: [], cands: {}, busq: {} };
    if (E.subject) { cambiarMateria(); } else { pintarLista(); }
    if (!vista.__vdEnlazado) { enlazar(); vista.__vdEnlazado = true; }
  }

  // ---------- Biblioteca: subir y catalogar PDF y actividades (por nivel, año, materia y misión) ----------
  var BL = { nivel: '', grado: '', materia: '', mision: '', tipo: 'texto', temas: [], items: [] };
  function nomGrado2(g) { return g.name || ('Año ' + g.year_number); }
  function selOpts(lista, sel, vacio) { return '<option value="">' + vacio + '</option>' + lista.map(function (o) { return '<option value="' + esc(o[0]) + '"' + (o[0] === sel ? ' selected' : '') + '>' + esc(o[1]) + '</option>'; }).join(''); }
  function pintarBiblio() {
    var cont = document.getElementById('bl-caja');
    if (!cont) return;
    var gr = B.grades.filter(function (g) { return !BL.nivel || g.level_id === BL.nivel; });
    var ms = B.subjects.filter(function (x) { return BL.grado && x.grade_id === BL.grado; });
    cont.innerHTML =
      '<div class="wv-tools vd-tools">' +
        '<select id="bl-tipo" class="vd-sel" aria-label="Qué es"><option value="texto"' + (BL.tipo === 'texto' ? ' selected' : '') + '>PDF (para todos)</option><option value="actividad"' + (BL.tipo === 'actividad' ? ' selected' : '') + '>Actividad (solo Desafío)</option></select>' +
        '<select id="bl-nivel" class="vd-sel" aria-label="Nivel">' + selOpts(B.levels.map(function (l) { return [l.id, l.name]; }), BL.nivel, 'Nivel…') + '</select>' +
        '<select id="bl-grado" class="vd-sel" aria-label="Año">' + selOpts(gr.map(function (g) { return [g.id, nomGrado2(g)]; }), BL.grado, 'Año…') + '</select>' +
        '<select id="bl-materia" class="vd-sel" aria-label="Materia">' + selOpts(ms.map(function (x) { return [x.id, x.name + (x.variant ? ' · ' + x.variant : '')]; }), BL.materia, 'Materia…') + '</select>' +
        '<select id="bl-mision" class="vd-sel" aria-label="Misión">' + selOpts(BL.temas.map(function (t) { return [t.id, t.title]; }), BL.mision, 'Misión…') + '</select>' +
      '</div>' +
      '<div class="wv-tools vd-tools"><input id="bl-titulo" class="vd-sel" type="text" placeholder="Título" style="flex:1;min-width:200px"><input id="bl-desc" class="vd-sel" type="text" placeholder="Descripción corta (opcional)" style="flex:2;min-width:220px"></div>' +
      '<div class="wv-tools"><input id="bl-archivo" type="file" accept="application/pdf"> <button type="button" class="wv-btn" id="bl-subir">⬆ Subir a la biblioteca</button> <span id="bl-txt" class="wv-sub"></span></div>' +
      '<div id="bl-lista"></div>';
    pintarItemsBiblio();
  }
  async function cargarItemsBiblio() {
    if (!BL.materia) { BL.items = []; return pintarItemsBiblio(); }
    var r = await sb.from('biblioteca_items').select('id, tipo, titulo, descripcion, url, topic_id, candidato_id').eq('subject_id', BL.materia).order('created_at');
    BL.items = r.error ? [] : r.data;
    pintarItemsBiblio();
  }
  function pintarItemsBiblio() {
    var el = document.getElementById('bl-lista');
    if (!el) return;
    if (!BL.materia) { el.innerHTML = '<div class="wv-vacio">Elegí nivel, año y materia para ver lo que ya hay en la biblioteca.</div>'; return; }
    var tit = {}; BL.temas.forEach(function (t) { tit[t.id] = t.title; });
    var ET = { video: '🎬 Video', texto: '📄 PDF', actividad: '🧩 Actividad' };
    el.innerHTML = BL.items.length ? BL.items.map(function (x) {
      return '<div class="wv-fila" style="display:flex;gap:10px;align-items:center;padding:8px 0;border-bottom:1px solid rgba(0,0,0,.08)"><span>' + ET[x.tipo] + '</span><div style="flex:1"><b>' + esc(x.titulo) + '</b><br><small>' + esc(x.topic_id && tit[x.topic_id] ? tit[x.topic_id] : 'Toda la materia') + '</small></div>' +
        '<a class="vd-yt" href="' + esc(x.url) + '" target="_blank" rel="noopener">Ver</a><button type="button" class="wv-btn mini suave" data-bl-borrar="' + x.id + '">Quitar</button></div>';
    }).join('') : '<div class="wv-vacio">Todavía no hay nada cargado para esta materia.</div>';
  }
  async function subirBiblio(btn) {
    var tit = document.getElementById('bl-titulo').value.trim(), desc = document.getElementById('bl-desc').value.trim();
    var f = document.getElementById('bl-archivo').files[0], txt = document.getElementById('bl-txt');
    if (!BL.materia) return aviso('Elegí nivel, año y materia.', true);
    if (!tit) return aviso('Poné un título.', true);
    if (!f) return aviso('Elegí el PDF.', true);
    if (f.type !== 'application/pdf' && !/\.pdf$/i.test(f.name)) return aviso('Tiene que ser un PDF.', true);
    btn.disabled = true; txt.textContent = 'Subiendo…';
    try {
      var ruta = BL.materia + '/' + Date.now() + '-' + f.name.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^A-Za-z0-9._-]+/g, '_');
      var u = await sb.storage.from('biblioteca').upload(ruta, f, { contentType: 'application/pdf', upsert: false });
      if (u.error) throw u.error;
      var url = sb.storage.from('biblioteca').getPublicUrl(ruta).data.publicUrl;
      var i = await sb.from('biblioteca_items').insert({ tipo: BL.tipo, titulo: tit, descripcion: desc || null, url: url, subject_id: BL.materia, topic_id: BL.mision || null }).select('id, tipo, titulo, descripcion, url, topic_id, candidato_id').single();
      if (i.error) { await sb.storage.from('biblioteca').remove([ruta]); throw i.error; }
      BL.items.push(i.data);
      document.getElementById('bl-titulo').value = ''; document.getElementById('bl-desc').value = ''; document.getElementById('bl-archivo').value = '';
      txt.textContent = ''; pintarItemsBiblio(); aviso('Subido a la biblioteca');
    } catch (e) { console.error(e); txt.textContent = ''; aviso('No se pudo subir: ' + ((e && e.message) || e), true); }
    btn.disabled = false;
  }
  async function borrarBiblio(id) {
    var x = BL.items.filter(function (y) { return y.id === id; })[0];
    if (!x || !confirm('¿Quitar "' + x.titulo + '" de la biblioteca?')) return;
    var d = await sb.from('biblioteca_items').delete().eq('id', id);
    if (d.error) return aviso('No se pudo quitar: ' + d.error.message, true);
    var m = /\/object\/public\/biblioteca\/(.+)$/.exec(x.url || '');
    if (m) { try { await sb.storage.from('biblioteca').remove([decodeURIComponent(m[1])]); } catch (e) { /* archivo huérfano */ } }
    BL.items = BL.items.filter(function (y) { return y.id !== id; });
    pintarItemsBiblio(); aviso('Quitado');
  }
  function enlazarBiblio() {
    var caja = document.getElementById('bl-caja');
    caja.addEventListener('change', async function (ev) {
      var id = ev.target.id;
      if (id === 'bl-tipo') { BL.tipo = ev.target.value; return; }
      if (id === 'bl-nivel') { BL.nivel = ev.target.value; BL.grado = ''; BL.materia = ''; BL.mision = ''; BL.temas = []; BL.items = []; return pintarBiblio(); }
      if (id === 'bl-grado') { BL.grado = ev.target.value; BL.materia = ''; BL.mision = ''; BL.temas = []; BL.items = []; return pintarBiblio(); }
      if (id === 'bl-materia') {
        BL.materia = ev.target.value; BL.mision = ''; BL.temas = [];
        if (BL.materia) { var t = await sb.from('topics').select('id, title, position').eq('subject_id', BL.materia).order('position'); BL.temas = t.error ? [] : t.data; }
        pintarBiblio(); return cargarItemsBiblio();
      }
      if (id === 'bl-mision') { BL.mision = ev.target.value; }
    });
    caja.addEventListener('click', function (ev) {
      var b = ev.target.closest('button'); if (!b) return;
      if (b.id === 'bl-subir') subirBiblio(b);
      else if (b.hasAttribute('data-bl-borrar')) borrarBiblio(b.getAttribute('data-bl-borrar'));
    });
  }

  window.WaveVideos = { abrir: abrir };
})();
