// Panel admin · Contenido: explorador de carpetas Nivel › Año › Materia › Tema › Lección.
// Cada lección tiene 4 casilleros fijos: Clase (video + PDF), Actividad interactiva,
// Actividades descargables y Actividad por consigna. El examen es una tarjeta aparte del tema.
(function () {
  var sb = Wave.sb;
  var vista = null;
  var S = { cargas: {}, tiers: {}, listo: false, levels: [], grades: [], subjects: [], topics: [], info: {}, lessons: {}, cfg: null };
  var R = { level: null, grade: null, subject: null, topic: null, lesson: null };
  var pendiente = null;

  var LEC_POR_TEMA = 4; // según la tabla de rangos: 4 lecciones por tema
  var TIPOS = ['video', 'pdf', 'interactive_activity', 'complementary_activity', 'final_activity'];

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function toast(texto, error) {
    var t = document.createElement('div');
    t.className = 'wv-toast' + (error ? ' error' : '');
    t.textContent = texto;
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, 3500);
  }
  function kb(n) { return n > 1048576 ? (n / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB'; }

  // ---------- Datos ----------
  async function todo(armar) {
    var out = [], desde = 0;
    for (;;) {
      var r = await armar().range(desde, desde + 999);
      if (r.error) throw r.error;
      out = out.concat(r.data || []);
      if (!r.data || r.data.length < 1000) break;
      desde += 1000;
    }
    return out;
  }

  async function cargarBase() {
    var res = await Promise.all([
      sb.from('levels').select('id, slug, name, position').order('position'),
      sb.from('grades').select('id, level_id, year_number, name').order('year_number'),
      todo(function () { return sb.from('subjects').select('id, grade_id, name, color, position, intro_video_uid').order('position').order('id'); }),
      todo(function () { return sb.from('topics').select('id, subject_id, title, position, is_published').order('position').order('id'); }),
      todo(function () { return sb.from('subject_load_config').select('subject_id, tier, hours_total, topics_total').order('subject_id'); }),
      sb.from('load_tiers').select('tier, label'),
      sb.from('app_settings').select('value').eq('key', 'intro_wave').maybeSingle()
    ]);
    if (res[0].error) throw res[0].error;
    if (res[1].error) throw res[1].error;
    if (res[5].error) throw res[5].error;
    S.introWave = res[6] && res[6].data && res[6].data.value && res[6].data.value.uid ? res[6].data.value : null;
    S.cargas = {}; res[4].forEach(function (c) { S.cargas[c.subject_id] = c; });
    S.tiers = {}; res[5].data.forEach(function (t) { S.tiers[t.tier] = t.label; });
    S.levels = res[0].data; S.grades = res[1].data; S.subjects = res[2]; S.topics = res[3];
    await cargarInfo();
    S.listo = true;
  }

  async function cargarInfo() {
    var filas = await todo(function () { return sb.rpc('content_overview'); });
    S.info = {};
    filas.forEach(function (f) { S.info[f.topic_id] = f; });
  }

  function estadoTema(tid) {
    var f = S.info[tid];
    if (!f || !f.lessons) return 'vacia';
    if (f.lessons >= LEC_POR_TEMA && f.completas >= f.lessons && f.tiene_examen && f.tiene_video) return 'ok';
    if (f.completas === 0 && f.con_algo === 0 && !f.tiene_examen && !f.tiene_video) return 'vacia';
    return 'falta';
  }
  function rollup(estados) {
    if (!estados.length) return 'vacia';
    if (estados.every(function (e) { return e === 'ok'; })) return 'ok';
    if (estados.every(function (e) { return e === 'vacia'; })) return 'vacia';
    return 'falta';
  }
  function temasDe(sid) { return S.topics.filter(function (t) { return t.subject_id === sid; }); }
  function estadoMateria(sid) {
    var ts = temasDe(sid), c = S.cargas[sid];
    var e = rollup(ts.map(function (t) { return estadoTema(t.id); }));
    // Si faltan temas respecto del rango, la materia no puede estar completa
    if (c && ts.length < c.topics_total && e === 'ok') return 'falta';
    return e;
  }
  function materiasDe(gid) { return S.subjects.filter(function (s) { return s.grade_id === gid; }); }
  function estadoAnio(gid) { return rollup(materiasDe(gid).map(function (s) { return estadoMateria(s.id); })); }
  function aniosDe(lid) { return S.grades.filter(function (g) { return g.level_id === lid; }); }
  function estadoNivel(lid) { return rollup(aniosDe(lid).map(function (g) { return estadoAnio(g.id); })); }

  function etiqueta(e) {
    var t = e === 'ok' ? 'Completa' : e === 'falta' ? 'Falta algo' : 'Vacía';
    return '<span class="wv-etq ' + e + '">' + t + '</span>';
  }

  // ---------- Llamada a las funciones de subida ----------
  // "1:25" / "1:02:03" / "85" -> segundos (null si está vacío, NaN si está mal escrito)
  function aSeg(t) {
    t = String(t || '').trim(); if (!t) return null;
    if (!/^\d+(:\d{1,2}){0,2}$/.test(t)) return NaN;
    return t.split(':').reduce(function (a, x) { return a * 60 + Number(x); }, 0);
  }
  function aReloj(s) {
    if (s == null || s === '') return '';
    s = Math.round(Number(s)); var m = Math.floor(s / 60), r = s % 60;
    return (m >= 60 ? Math.floor(m / 60) + ':' + ('0' + (m % 60)).slice(-2) : m) + ':' + ('0' + r).slice(-2);
  }
  // Recorte del video: una fila "desde / hasta" por tramo
  function tramosDe(ct) { return ct.tramos && ct.tramos.length ? ct.tramos : (ct.inicio || ct.fin ? [{ i: ct.inicio || 0, f: ct.fin || 0 }] : []); }
  // Lista de videos del paso (formato nuevo: content.videos; formato viejo: un solo video en stream_uid)
  function videosDe(v) {
    var c = (v && v.content) || {};
    if (Array.isArray(c.videos) && c.videos.length) return c.videos.map(function (x) { var o = Object.assign({}, x); o.nombre = x.nombre || ''; o.tramos = x.tramos || []; return o; });
    return v && v.stream_uid ? [{ uid: v.stream_uid, nombre: '', tramos: tramosDe(c) }] : [];
  }
  async function guardarVideos(lista) {
    await guardarPaso('video', { stream_uid: lista.length ? lista[0].uid : null, content: lista.length ? { videos: lista } : {} });
  }
  function recorteHtml(x, vi) {
    var tmp = (L.recTmp || {})[vi], nn = (L.recN || {})[vi] || 0;
    var filas = tmp || (x.tramos || []).map(function (t) { return [t.i ? aReloj(t.i) : '', t.f ? aReloj(t.f) : '']; });
    var n = Math.max(1, nn, filas.length), h = '<div class="wv-recorte" data-vi="' + vi + '"><b>✂️ Mostrar solo estas partes del video</b>';
    for (var i = 0; i < n; i++) {
      var f = filas[i] || ['', ''];
      h += '<div class="wv-rec-fila"><span>' + (n > 1 ? 'Parte ' + (i + 1) + ': desde' : 'Desde') + '</span><input class="wv-rec-i" type="text" inputmode="numeric" placeholder="0:00" value="' + esc(f[0]) + '"><span>hasta</span><input class="wv-rec-f" type="text" inputmode="numeric" placeholder="final" value="' + esc(f[1]) + '"></div>';
    }
    return h + '<div class="wv-rec-b">' + (x.intro ? '' : boton('video-editar:' + vi, '🎞️ Editar mirando el video', '')) + boton('video-rec-mas:' + vi, '+ Agregar otra parte', 'suave') + boton('video-rec:' + vi, 'Guardar recorte', 'suave') + '</div><small>Minutos:segundos. Todo vacío = video entero. Para quitar una parte, dejá su fila vacía y guardá.</small></div>';
  }
  function leerRecorte(vi) {
    var r = { tramos: [], crudo: [], mal: false };
    [].forEach.call(document.querySelectorAll('.wv-recorte[data-vi="' + vi + '"] .wv-rec-fila'), function (fl) {
      var a = fl.querySelector('.wv-rec-i').value, b = fl.querySelector('.wv-rec-f').value, i = aSeg(a), f = aSeg(b);
      r.crudo.push([a, b]);
      if (i !== i || f !== f) { r.mal = true; return; }
      if (i == null && f == null) return;
      r.tramos.push({ i: i || 0, f: f || 0 });
    });
    return r;
  }
  function esYt(uid) { return /^yt:/.test(uid || ''); }
  function idYoutube(t) {
    t = String(t || '').trim();
    var m = t.match(/(?:youtu\.be\/|youtube(?:-nocookie)?\.com\/(?:watch\?(?:.*&)?v=|embed\/|shorts\/|live\/))([A-Za-z0-9_-]{11})/) || t.match(/^([A-Za-z0-9_-]{11})$/);
    return m ? m[1] : null;
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

  function enviar(url, metodo, cuerpo, onProg) {
    return new Promise(function (ok, mal) {
      var x = new XMLHttpRequest();
      x.open(metodo, url);
      x.upload.onprogress = function (ev) { if (ev.lengthComputable && onProg) onProg(Math.round(ev.loaded * 100 / ev.total)); };
      x.onload = function () { (x.status >= 200 && x.status < 300) ? ok() : mal(new Error('El servidor rechazó el archivo (' + x.status + ').')); };
      x.onerror = function () { mal(new Error('No se pudo subir el archivo. Revisá tu conexión (y que R2 permita subidas desde este sitio).')); };
      x.send(cuerpo);
    });
  }

  // ---------- Navegación ----------
  function nombre(tipo, id) {
    var l;
    if (tipo === 'level') { l = S.levels.filter(function (x) { return x.id === id; })[0]; return l ? l.name : ''; }
    if (tipo === 'grade') { l = S.grades.filter(function (x) { return x.id === id; })[0]; return l ? l.name : ''; }
    if (tipo === 'subject') { l = S.subjects.filter(function (x) { return x.id === id; })[0]; return l ? l.name : ''; }
    if (tipo === 'topic') { l = S.topics.filter(function (x) { return x.id === id; })[0]; return l ? l.title : ''; }
    if (tipo === 'lesson') { var ls = S.lessons[R.topic] || []; l = ls.filter(function (x) { return x.id === id; })[0]; return l ? l.title : ''; }
    return '';
  }

  function migas() {
    var orden = ['level', 'grade', 'subject', 'topic', 'lesson'];
    var h = '<nav class="wv-migas"><a data-ir="raiz">Contenido</a>';
    var hasta = -1;
    orden.forEach(function (k, i) { if (R[k]) hasta = i; });
    orden.forEach(function (k, i) {
      if (i > hasta) return;
      h += '<span>›</span>';
      h += i === hasta ? '<b>' + esc(nombre(k, R[k])) + '</b>'
        : '<a data-ir="' + k + ':' + R[k] + '">' + esc(nombre(k, R[k])) + '</a>';
    });
    return h + '</nav>';
  }

  function ir(spec) {
    var p = spec.split(':'), k = p[0];
    var orden = ['level', 'grade', 'subject', 'topic', 'lesson'];
    if (k === 'raiz') { orden.forEach(function (o) { R[o] = null; }); }
    else {
      var i = orden.indexOf(k);
      R[k] = p[1];
      orden.forEach(function (o, j) { if (j > i) R[o] = null; });
    }
    pintar();
  }

  function carpeta(tipo, id, titulo, detalle, estado, extra) {
    return '<div class="wv-carp"><button type="button" class="wv-carp-b" data-ir="' + tipo + ':' + id + '">' +
      '<span class="wv-carp-ico">📁</span><span class="wv-carp-t"><b>' + esc(titulo) + '</b><small>' + esc(detalle) + '</small></span>' +
      etiqueta(estado) + '</button>' + (extra || '') + '</div>';
  }
  function herr(tipo, id, i, n, extra) {
    return '<span class="wv-herr">' + (extra || '') +
      '<button type="button" class="wv-ico" title="Subir" data-acc="mov:' + tipo + ':' + id + ':-1"' + (i === 0 ? ' disabled' : '') + '>▲</button>' +
      '<button type="button" class="wv-ico" title="Bajar" data-acc="mov:' + tipo + ':' + id + ':1"' + (i === n - 1 ? ' disabled' : '') + '>▼</button>' +
      '<button type="button" class="wv-ico" title="Renombrar" data-acc="ren:' + tipo + ':' + id + '">✎</button>' +
      '<button type="button" class="wv-ico" title="Eliminar" data-acc="del:' + tipo + ':' + id + '">🗑</button></span>';
  }

  // ---------- Vistas de carpetas ----------
  function pintar() {
    if (!S.listo) return;
    try { localStorage.setItem('wv-contenido-ruta', JSON.stringify(R)); } catch (e) { /* sin almacenamiento: no pasa nada */ }
    var h = '<h1 class="wv-titulo">Contenido</h1>' + migas();
    if (!R.level) h += vNiveles();
    else if (!R.grade) h += vAnios();
    else if (!R.subject) h += vMaterias();
    else if (!R.topic) h += vTemas();
    else if (!R.lesson) h += vLecciones();
    else { vista.innerHTML = h + '<div id="wv-les" class="wv-vacio">Cargando lección…</div>'; abrirLeccion(); return; }
    vista.innerHTML = h;
  }

  function vNiveles() {
    return '<p class="wv-sub">Elegí un nivel para entrar.</p><div class="wv-carps">' + S.levels.map(function (l) {
      return carpeta('level', l.id, l.name, aniosDe(l.id).length + (aniosDe(l.id).length === 1 ? ' año' : ' años'), estadoNivel(l.id));
    }).join('') + '</div>';
  }
  function vAnios() {
    return '<div class="wv-carps">' + aniosDe(R.level).map(function (g) {
      return carpeta('grade', g.id, g.name, materiasDe(g.id).length + ' materias', estadoAnio(g.id));
    }).join('') + '</div>';
  }
  function vMaterias() {
    var ms = materiasDe(R.grade);
    if (!ms.length) return '<div class="wv-vacio">Este año todavía no tiene materias.</div>';
    return '<div class="wv-carps">' + ms.map(function (s) {
      var ts = temasDe(s.id);
      var ls = ts.reduce(function (a, t) { return a + ((S.info[t.id] || {}).lessons || 0); }, 0);
      var c = S.cargas[s.id];
      var det = (c ? S.tiers[c.tier] + ' · ' : '') + ts.length + (c ? ' de ' + c.topics_total : '') + ' misiones · ' + ls + ' niveles';
      return carpeta('subject', s.id, s.name, det, estadoMateria(s.id));
    }).join('') + '</div>';
  }
  function vTemas() {
    var ts = temasDe(R.subject);
    var c = S.cargas[R.subject], h = '';
    if (c) {
      h += '<div class="wv-rango">Rango <b>' + esc(S.tiers[c.tier]) + '</b>: ' + c.hours_total + ' horas · ' + c.topics_total + ' misiones · ' +
        'cada misión: 3 o 4 niveles y las 4 generales</div>';
      if (ts.length < c.topics_total) {
        h += '<div class="wv-aviso">Faltan ' + (c.topics_total - ts.length) + ' misiones para completar el rango. ' +
          '<button class="wv-btn mini" type="button" data-acc="temas-completar">Crear las misiones que faltan</button></div>';
      } else if (ts.length > c.topics_total) {
        h += '<div class="wv-aviso">Hay ' + (ts.length - c.topics_total) + ' misiones de más respecto del rango.</div>';
      }
    }
    var sj = S.subjects.filter(function (x) { return x.id === R.subject; })[0] || {};
    var tieneIntro = !!sj.intro_video_uid;
    h += '<div class="wv-intro">' + fila('🎬', 'Introducción de la materia', tieneIntro ? 'Video cargado' : 'Sin video: el alumno ve "Próximamente"',
      (tieneIntro ? boton('intro-ver', 'Ver') : '') + boton('intro-up', tieneIntro ? 'Reemplazar' : 'Subir video', tieneIntro ? 'suave' : '') + (tieneIntro ? boton('intro-del', 'Quitar', 'peligro') : ''), 'wv-i-intro') + '</div>';
    if (!ts.length) return h + '<div class="wv-vacio">Esta materia todavía no tiene misiones.</div>';
    var nPub = ts.filter(function (t) { return t.is_published; }).length;
    h += '<div class="wv-rango">Visibles para el alumno: <b>' + nPub + ' de ' + ts.length + ' misiones</b>. Lo que está oculto el alumno no lo ve. ' +
      boton('pub-todo:1', 'Publicar todos') + ' ' + boton('pub-todo:0', 'Ocultar todos') + '</div>';
    return h + '<div class="wv-carps">' + ts.map(function (t, i) {
      var f = S.info[t.id] || {};
      var pub = '<button type="button" class="wv-ico wv-pub ' + (t.is_published ? 'on' : '') + '" data-acc="pub:topic:' + t.id + '" title="' + (t.is_published ? 'Visible para el alumno (tocá para ocultar)' : 'Oculto para el alumno (tocá para publicar)') + '">' + (t.is_published ? '👁 Visible' : '🚫 Oculto') + '</button>';
      return carpeta('topic', t.id, t.title, (f.lessons || 0) + ' niveles · videos ' + (f.tiene_video ? 'cargados' : 'sin cargar') + ' · nivel jefe ' + (f.tiene_examen ? 'creado' : 'sin crear'), estadoTema(t.id), herr('topic', t.id, i, ts.length, pub));
    }).join('') + '</div>';
  }
  function vLecciones() {
    var nl = (S.info[R.topic] || {}).lessons || 0;
    var h = '<div class="wv-rango">' + 'Cada misión tiene 3 o 4 niveles (PDF, carpeta y 2 actividades cada uno) y, como última lección, las 4 generales (no cuentan como nivel). Los videos de la misión se cargan en el Nivel 1.' +
      (nl < LEC_POR_TEMA ? ' · faltan ' + (LEC_POR_TEMA - nl) + ' <button class="wv-btn suave mini" type="button" data-acc="nuevo:lesson">+ Nuevo nivel</button>' : '') +
      (nl > LEC_POR_TEMA + 1 ? ' · hay ' + (nl - LEC_POR_TEMA - 1) + ' de más' : '') + '</div><div id="wv-lec-lista" class="wv-carps"><div class="wv-vacio">Cargando…</div></div>';
    setTimeout(cargarLecciones, 0);
    return h;
  }

  async function lecEstados(ids) {
    var r = await sb.from('lesson_steps').select('lesson_id, step_type, stream_uid, r2_key, content, id').in('lesson_id', ids);
    if (r.error) throw r.error;
    var fin = r.data.filter(function (s) { return s.step_type === 'final_activity'; }).map(function (s) { return s.id; });
    var q = fin.length ? await sb.from('questions').select('lesson_step_id').in('lesson_step_id', fin) : { data: [] };
    var conP = {};
    (q.data || []).forEach(function (x) { conP[x.lesson_step_id] = true; });
    var m = {};
    ids.forEach(function (id) { m[id] = { v: 0, p: 0, k: 0, f: 0 }; });
    var pdfIds = r.data.filter(function (s) { return s.step_type === 'pdf'; }).map(function (s) { return s.id; });
    var cl = pdfIds.length ? await sb.from('carpeta_claves').select('lesson_step_id, items').in('lesson_step_id', pdfIds) : { data: [] };
    var conClave = {};
    (cl.data || []).forEach(function (x) { if (Array.isArray(x.items) && x.items.length) conClave[x.lesson_step_id] = true; });
    r.data.forEach(function (s) {
      var x = m[s.lesson_id];
      if (s.step_type === 'pdf' && conClave[s.id] && s.content && Array.isArray(s.content.carpeta) && s.content.carpeta.length) x.k = 1;
      if (s.step_type === 'video' && s.stream_uid) x.v = 1;
      if (s.step_type === 'pdf' && s.r2_key) x.p = 1;
      if (s.step_type === 'final_activity' && conP[s.id]) x.f = 1;
    });
    return m;
  }

  async function cargarLecciones() {
    var cont = document.getElementById('wv-lec-lista');
    try {
      var r = await sb.from('lessons').select('id, title, position').eq('topic_id', R.topic).order('position').order('created_at');
      if (r.error) throw r.error;
      S.lessons[R.topic] = r.data;
      var est = r.data.length ? await lecEstados(r.data.map(function (l) { return l.id; })) : {};
      var nn = r.data.length;
      var h = r.data.map(function (l, i) {
        var e = est[l.id], gen = nn >= 4 && i === nn - 1;
        var partes = gen ? e.f : e.p + e.k + e.f, tot = gen ? 1 : 3;
        var estado = partes === tot ? 'ok' : partes === 0 ? 'vacia' : 'falta';
        var det = gen ? 'Las 4 generales · ' + (e.f ? 'actividades cargadas' : 'sin actividades')
          : 'Nivel ' + (i + 1) + ' · ' + partes + ' de 3 partes (PDF, carpeta, actividades)' + (i === 0 ? ' · videos ' + (e.v ? 'cargados' : 'sin cargar') : '');
        return carpeta('lesson', l.id, l.title, det, estado, herr('lesson', l.id, i, nn));
      }).join('');
      var examen = (S.info[R.topic] || {}).tiene_examen, borrador = examen && !(S.info[R.topic] || {}).examen_publicado;
      h += '<div class="wv-carp examen"><div class="wv-carp-b static"><span class="wv-carp-ico">📝</span><span class="wv-carp-t"><b>Nivel jefe (examen corto)</b>' +
        '<small>' + (borrador ? 'Borrador: los alumnos todavía no lo ven. Revisalo y publicalo. Cada intento sortea preguntas del banco.' : 'Se arma acá mismo. Cada intento sortea preguntas distintas del banco: es el jefe final de la misión.') + '</small></span>' + etiqueta(examen ? 'ok' : 'vacia') +
        (borrador ? boton('examen-pub', 'Publicar examen', '') : '') +
        boton('examen', examen ? 'Editar nivel jefe' : 'Armar nivel jefe', examen ? 'suave' : '') + (examen ? boton('examen-del', 'Quitar nivel jefe', 'peligro') : '') + '</div></div>';
      cont.innerHTML = r.data.length ? h : '<div class="wv-vacio">Esta misión todavía no tiene niveles.</div>' + h;
    } catch (e) {
      console.error(e);
      cont.innerHTML = '<div class="wv-vacio">No pudimos cargar las lecciones.<br><small>' + esc(e.message || e) + '</small></div>';
    }
  }

  // ---------- Lección ----------
  var L = null; // { pasos: {tipo: fila}, preguntas: n }

  async function abrirLeccion() {
    try {
      if (!S.cfg) { try { S.cfg = await subidas({ action: 'config' }); } catch (e) { S.cfg = { error: e.message }; } }
      var r = await sb.from('lesson_steps').select('id, step_type, stream_uid, r2_key, content, title').eq('lesson_id', R.lesson);
      if (r.error) throw r.error;
      var pasos = {};
      r.data.forEach(function (s) { pasos[s.step_type] = s; });
      var faltan = [];
      TIPOS.forEach(function (t, i) { if (!pasos[t]) faltan.push({ lesson_id: R.lesson, step_type: t, position: i + 1 }); });
      if (faltan.length) {
        var ins = await sb.from('lesson_steps').insert(faltan).select('id, step_type, stream_uid, r2_key, content, title');
        if (ins.error) throw ins.error;
        ins.data.forEach(function (s) { pasos[s.step_type] = s; });
      }
      var lst = S.lessons[R.topic];
      if (!lst) { var rl = await sb.from('lessons').select('id, title, position').eq('topic_id', R.topic).order('position').order('created_at'); if (rl.error) throw rl.error; lst = S.lessons[R.topic] = rl.data; }
      var idx = lst.map(function (x) { return x.id; }).indexOf(R.lesson);
      var gen = lst.length >= 4 && idx === lst.length - 1;
      var kc = await sb.from('carpeta_claves').select('items').eq('lesson_step_id', pasos.pdf.id).maybeSingle();
      var q = await sb.from('questions').select('id', { count: 'exact', head: true }).eq('lesson_step_id', pasos.final_activity.id);
      var bd = await sb.from('lesson_drafts').select('status, paso, revision, revision_inicial, updated_at').eq('lesson_id', R.lesson).maybeSingle();
      var rr = await sb.from('video_renders').select('id, status, error, created_at').eq('lesson_id', R.lesson).order('created_at', { ascending: false }).limit(1).maybeSingle();
      var claves = videosDe(pasos.video).map(function (x) { return x.uid; }).filter(function (k) { return /^lessons\//.test(k || ''); }), opt = {};
      if (claves.length) { var ro = await sb.from('video_optimizados').select('key, estado, nota').in('key', claves); (ro.data || []).forEach(function (o) { opt[o.key] = o; }); }
      var tr = null, fichas = [];
      if (idx === 0) {
        var rt = await sb.from('video_transcripciones').select('estado, texto, nota').eq('step_id', pasos.video.id).maybeSingle();
        tr = rt.error ? null : rt.data;
        var rf = await sb.from('lesson_fichas').select('lesson_id, contenidos, no_entra').in('lesson_id', lst.map(function (x) { return x.id; }));
        fichas = lst.map(function (l) { return (rf.data || []).filter(function (f) { return f.lesson_id === l.id; })[0] || null; });
      }
      L = { tr: tr, fichas: fichas, opt: opt, pasos: pasos, idx: idx, gen: gen, primera: idx === 0, claves: (kc.data && Array.isArray(kc.data.items)) ? kc.data.items : [], preguntas: q.count || 0, recTmp: {}, recN: {}, borrador: bd.error ? null : bd.data, render: rr.error ? null : rr.data };
      pintarLeccion();
      vigilarRender();
    } catch (e) {
      console.error(e);
      document.getElementById('wv-les').innerHTML = 'No pudimos cargar la lección.<br><small>' + esc(e.message || e) + '</small>';
    }
  }

  // Mientras un video final se está generando, revisa cada 20 s y recién recarga la lección cuando cambia el estado
  var sondeo = null;
  function vigilarRender() {
    if (sondeo) { clearTimeout(sondeo); sondeo = null; }
    if (!L || !L.render || (L.render.status !== 'pendiente' && L.render.status !== 'procesando')) return;
    var lec = R.lesson, id = L.render.id, antes = L.render.status;
    sondeo = setTimeout(async function () {
      sondeo = null;
      if (R.lesson !== lec || !document.getElementById('wv-i-render')) return;
      var r = await sb.from('video_renders').select('status').eq('id', id).maybeSingle();
      if (r.data && r.data.status !== antes) abrirLeccion(); else vigilarRender();
    }, 20000);
  }

  // ---------- Correcciones del revisor (lecciones armadas por la máquina) ----------
  var GRAVEDAD = { alta: 'Grave', media: 'Importante', baja: 'Menor' };
  function pendientes() { var r = (L && L.borrador && L.borrador.revision) || {}; return Array.isArray(r.problemas) ? r.problemas : []; }
  function botonCorrecciones() {
    if (!L || !L.borrador || !L.borrador.revision) return '';
    var n = pendientes().length, ini = L.borrador.revision_inicial && L.borrador.revision_inicial.problemas ? L.borrador.revision_inicial.problemas.length : 0;
    var txt = n ? '⚠ Correcciones (' + n + ' pendientes)' : (ini ? '✔ Correcciones (' + ini + ' arregladas solas)' : '✔ Correcciones (sin observaciones)');
    return '<button type="button" class="wv-btn mini ' + (n ? '' : 'suave') + ' wv-corr-btn" data-acc="correcciones">' + txt + '</button>';
  }
  function listaProblemas(ps) {
    return ps.map(function (p) {
      return '<div class="wv-corr-item g-' + esc(p.gravedad) + '"><div class="wv-corr-h"><b>' + esc(p.donde) + '</b><span>' + esc(GRAVEDAD[p.gravedad] || p.gravedad) + '</span></div>' +
        '<p>' + esc(p.descripcion) + '</p>' + (p.correccion ? '<p class="wv-corr-fix"><b>Cómo debería decir:</b> ' + esc(p.correccion) + '</p>' : '') + '</div>';
    }).join('');
  }
  function abrirCorrecciones() {
    var b = L && L.borrador; if (!b || !b.revision) return;
    var fin = pendientes(), ini = (b.revision_inicial && b.revision_inicial.problemas) || [];
    var h = '<h2>Correcciones del revisor</h2><p>Esta lección la escribió la máquina. Otra IA la revisó, recalculó las cuentas y controló el vocabulario. <b>No reemplaza tu lectura:</b> sirve para saber dónde mirar con más cuidado.</p>';
    h += '<div class="wv-corr-estado ' + (b.revision.apto ? 'ok' : 'no') + '">' + (b.revision.apto ? '✔ El revisor la considera apta' : '⚠ El revisor la marcó como NO apta: revisala antes de publicar') + '</div>';
    if (b.revision.resumen) h += '<h3>Opinión del revisor</h3><p>' + esc(b.revision.resumen) + '</p>';
    if (b.revision_inicial) {
      h += '<h3>Qué encontró al principio y se corrigió sola (' + ini.length + ')</h3>' + (ini.length ? listaProblemas(ini) : '<p>Nada.</p>');
      h += '<h3>Qué sigue marcado después de corregir (' + fin.length + ')</h3>' + (fin.length ? listaProblemas(fin) : '<p>Nada: la segunda revisión no encontró problemas.</p>');
    } else {
      h += '<h3>Observaciones (' + fin.length + ')</h3>' + (fin.length ? listaProblemas(fin) : '<p>El revisor no encontró nada para corregir.</p>');
    }
    var el = document.createElement('div'); el.className = 'wv-modal'; el.id = 'wv-corr';
    el.innerHTML = '<div class="wv-modal-caja ancha">' + h + '<div class="wv-modal-pie">' + boton('corr-cerrar', 'Cerrar', '') + '</div></div>';
    el.addEventListener('click', function (ev) { if (ev.target === el || ev.target.closest('[data-acc="corr-cerrar"]')) el.remove(); });
    document.body.appendChild(el);
  }

  function casillero(num, icono, titulo, ayuda, estado, cuerpo) {
    return '<section class="wv-cas ' + estado + '"><header><span class="wv-num">' + num + '</span><span class="wv-cas-ico">' + icono + '</span>' +
      '<div><h3>' + titulo + '</h3><small>' + ayuda + '</small></div>' + etiqueta(estado === 'ok' ? 'ok' : estado === 'falta' ? 'falta' : 'vacia') + '</header>' +
      '<div class="wv-cas-c">' + cuerpo + '</div></section>';
  }
  function fila(icono, nom, estadoTxt, botones, id) {
    return '<div class="wv-item"' + (id ? ' id="' + id + '"' : '') + '><span class="wv-item-ico">' + icono + '</span><div class="wv-item-t"><b>' + nom + '</b><small>' + estadoTxt + '</small></div><div class="wv-item-b">' + botones + '</div></div>';
  }
  function boton(acc, txt, cls) { return '<button type="button" class="wv-btn mini ' + (cls || 'suave') + '" data-acc="' + acc + '">' + txt + '</button>'; }

  function pintarLeccion() {
    var p = L.pasos, h = '';
    var aviso = '';
    if (S.cfg && S.cfg.error) aviso = '<div class="wv-aviso">No pudimos comprobar la configuración de subidas: ' + esc(S.cfg.error) + '</div>';
    else if (S.cfg && (!S.cfg.archivos || !S.cfg.videos)) {
      aviso = '<div class="wv-aviso">Falta configurar en Supabase: ' + esc((S.cfg.faltan_archivos || []).concat(S.cfg.faltan_videos || []).filter(function (x, i, a) { return a.indexOf(x) === i; }).join(', ')) + '. Hasta entonces esas subidas no van a funcionar.</div>';
    }

    // 1 · Clase
    var vids = videosDe(p.video), tieneV = vids.length > 0;
    var pdf = p.pdf, tieneP = !!pdf.r2_key;
    var pdfNom = tieneP ? (pdf.title || pdf.r2_key.split('/').pop().replace(/^[a-z0-9]{8}-/, '')) : '';
    var clase = '';
    vids.forEach(function (x, i) {
      var nom = x.intro ? '🎬 Intro de Wave' : esYt(x.uid) ? 'Video de YouTube incrustado' : (x.nombre || x.uid.split('/').pop().replace(/^[a-z0-9]{8}-/, ''));
      var ob = (L.opt || {})[x.uid];
      var est = x.intro || esYt(x.uid) ? '' : !ob ? ' · ⏳ Sin optimizar todavía (se hace solo en unos minutos)' : ob.estado === 'ok' ? ' · ✅ Optimizado' : ob.estado === 'error' ? ' · ⚠️ No se pudo optimizar' : ' · ⏳ Optimizando…';
      clase += fila('🎬', vids.length > 1 ? 'Video ' + (i + 1) + ' de ' + vids.length : 'Video de la clase', esc(nom) + est,
        boton('video-ver:' + i, 'Ver') +
        (vids.length > 1 ? '<button type="button" class="wv-ico" title="Subir" data-acc="video-mov:' + i + ':-1"' + (i === 0 ? ' disabled' : '') + '>▲</button><button type="button" class="wv-ico" title="Bajar" data-acc="video-mov:' + i + ':1"' + (i === vids.length - 1 ? ' disabled' : '') + '>▼</button>' : '') +
        (x.intro ? '' : boton('video-introdef:' + i, '⭐ Usar como intro', 'suave')) +
        boton('video-del:' + i, 'Quitar', 'peligro')) + recorteHtml(x, i);
    });
    if (tieneV) {
      var rn = L.render, enCola = rn && (rn.status === 'pendiente' || rn.status === 'procesando');
      var armado = vids.length > 1 || vids.some(function (x) { return (x.tramos && x.tramos.length) || x.intro; });
      var pesado = vids.some(function (x) { return !esYt(x.uid) && !x.final; });
      var rTxt = enCola ? (rn.status === 'procesando' ? 'Se está generando… (puede tardar unos minutos)' : 'En cola: arranca solo en un momento')
        : rn && rn.status === 'error' ? 'El último intento falló: ' + esc(rn.error || '') : rn && rn.status === 'listo' && !armado ? 'Video final generado ✔ (un solo archivo, carga rápido)' : armado ? 'Une los cortes y la intro en UN solo video que carga rápido' : pesado ? 'Si el video es pesado o tarda en cargar: lo comprime y lo deja listo para internet' : 'Ya es un solo video';
      if (armado || pesado || enCola || (rn && rn.status !== 'listo')) clase += fila('🎞️', 'Video final', rTxt, (enCola ? '' : boton('render-pedir', 'Generar video final', '')) + boton('render-estado', 'Actualizar estado', 'suave'), 'wv-i-render');
      else if (rn && rn.status === 'listo') clase += fila('🎞️', 'Video final', rTxt, boton('render-estado', 'Actualizar estado', 'suave'), 'wv-i-render');
    }
    clase += S.introWave
      ? fila('⭐', 'Intro de Wave', 'Ya cargada: aparece sola al principio de los videos de todas las misiones. No hace falta agregarla acá.', boton('introw-up', 'Reemplazar intro', 'suave'), 'wv-i-introwave')
      : fila('⭐', 'Intro de Wave', 'Todavía no cargaste tu intro. Se sube una sola vez y aparece sola al principio de los videos de todas las misiones.', boton('introw-up', 'Subir mi intro', ''), 'wv-i-introwave');
    clase += fila(tieneV ? '➕' : '🎬', tieneV ? 'Agregar otro video' : 'Video de la clase', tieneV ? 'El alumno los ve en orden, uno después del otro' : 'Sin video',
      boton('video-up', 'Subir videos', tieneV ? 'suave' : '') + boton('video-yt', 'Enlace de YouTube', 'suave'), 'wv-i-video');
    if (tieneV) clase += filaTranscripcion();
    clase += fila('🔎', 'Revisar otro video', 'Pegá una transcripción y te dice cuánto de la misión cubre (sin IA, no gasta créditos)', boton('video-revisar', 'Revisar transcripción', 'suave'), 'wv-i-revisar');
    var num = 0;
    if (L.primera) h += casillero(++num, '🎬', 'Videos de la misión', 'Se ven todos juntos al principio de la misión, en este orden', tieneV ? 'ok' : 'vacia', clase);
    if (!L.gen) {
      var filaPdf = fila('📄', 'PDF del nivel', tieneP ? esc(pdfNom) : 'Sin PDF', (tieneP ? boton('pdf-get', 'Ver') : '') + boton('pdf-up', tieneP ? 'Reemplazar' : 'Subir PDF', tieneP ? 'suave' : '') + (tieneP ? boton('pdf-del', 'Quitar', 'peligro') : ''), 'wv-i-pdf');
      h += casillero(++num, '📄', 'PDF del nivel', 'Máximo 4 hojas más la portada. Trae las consignas de la carpeta, sin las soluciones', tieneP ? 'ok' : 'vacia', filaPdf);
      var nc = (pdf.content && Array.isArray(pdf.content.carpeta)) ? pdf.content.carpeta.length : 0, okC = nc > 0 && L.claves.length >= nc;
      var filaCar = fila('✏️', 'Actividad de carpeta', nc ? nc + (nc === 1 ? ' consigna' : ' consignas') + (okC ? ' con su clave de corrección' : ' · falta la clave de alguna') : 'Sin consignas',
        boton('carpeta-ed', nc ? 'Editar carpeta' : 'Armar carpeta', nc ? 'suave' : ''), 'wv-i-carpeta');
      h += casillero(++num, '✏️', 'Carpeta: consignas y clave', 'Lo que el alumno entrega en la app. Se corrige sin IA y las soluciones se muestran recién después de entregar', okC ? 'ok' : nc ? 'falta' : 'vacia', filaCar);
    }

    var esperadas = L.gen ? 4 : 2;
    var cons = fila('🧩', L.gen ? 'Las 4 generales' : 'Actividades del nivel', L.preguntas ? L.preguntas + (L.preguntas === 1 ? ' actividad armada' : ' actividades armadas') + (L.preguntas !== esperadas ? ' · el plan son ' + esperadas : '') : 'Sin actividades',
      boton('consignas', L.preguntas ? 'Editar' : 'Armar', L.preguntas ? 'suave' : '') + (L.preguntas ? boton('consignas-del', 'Quitar todas', 'peligro') : ''));
    h += casillero(++num, '🧩', L.gen ? 'Las 4 generales' : 'Las 2 actividades', L.gen ? 'Mezclan los niveles y repasan misiones anteriores. Se arman acá mismo' : 'Preguntas sobre el PDF de este nivel. Se arman acá mismo', L.preguntas ? 'ok' : 'vacia', cons);

    var tit = nombre('lesson', R.lesson);
    var cont = document.getElementById('wv-les');
    if (!cont) return;
    cont.className = '';
    cont.innerHTML = '<div class="wv-lec-cab"><h2>' + esc(tit) + '</h2>' + botonCorrecciones() + '</div>' + aviso + '<div class="wv-cass">' + h + '</div>';
  }

  // ---------- Revisar la transcripción de un video contra los PDF de la misión (sin IA) ----------
  var VACIAS = ' de la las los el en y a un una unos unas por para con del al que se su sus es son o como mas más entre sin sobre lo le cada otro otra este esta '.split(' ');
  function normT(t) { return String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/<[^>]+>/g, ' ').replace(/[^a-z0-9ñ ]+/g, ' ').replace(/\s+/g, ' ').trim(); }
  function raices(t) { return normT(t).split(' ').filter(function (w) { return w.length > 2 && VACIAS.indexOf(w) < 0; }).map(function (w) { return w.replace(/(es|s)$/, '').replace(/z/g, 'c').slice(0, 6); }); }
  function aparece(frase, bolsa) { var r = raices(frase); if (!r.length) return false; var n = r.filter(function (x) { return bolsa[x]; }).length; return n / r.length >= 0.6; }
  // Compara un texto con los contenidos de las fichas (lo que pide el mapa curricular) de las 4 lecciones
  function cobertura(txt, fichas) {
    var bolsa = {}; raices(txt).forEach(function (r) { bolsa[r] = 1; });
    var lst = S.lessons[R.topic] || [], tot = 0, ok = 0, falta = [], fuera = [], niveles = [];
    (fichas || []).forEach(function (f, i) {
      if (!f || !Array.isArray(f.contenidos)) return;
      var si = [], no = [];
      f.contenidos.forEach(function (c) { var t = String(c).replace(/\(.*?\)/g, '').trim(); if (!t) return; (aparece(t, bolsa) ? si : no).push(t); });
      tot += si.length + no.length; ok += si.length; falta = falta.concat(no);
      niveles.push({ n: i + 1, tit: (lst[i] || {}).title || '', si: si, no: no });
      String(f.no_entra || '').split(/[.;]/).forEach(function (fr) { fr = fr.replace(/\(.*?\)/g, '').trim(); if (fr.length > 4 && aparece(fr, bolsa)) fuera.push(fr); });
    });
    return { pct: tot ? Math.round(ok * 100 / tot) : 0, falta: falta, fuera: fuera, niveles: niveles };
  }
  function veredicto(p) { return p >= 60 ? '✅ El video sirve' : p >= 40 ? '🟡 Sirve, el PDF completa lo que falta (si lo que falta es difícil, sumá un video corto)' : '❌ Probablemente no es el video de esta misión'; }
  function detalleCobertura(c) {
    return '<p style="font-size:1.1rem"><b>' + veredicto(c.pct) + '</b> — cubre ' + c.pct + '% de la misión</p>' +
      (c.fuera.length ? '<p>⚠️ Habla de temas que no son de esta misión: ' + c.fuera.map(esc).join(' · ') + '</p>' : '') +
      c.niveles.map(function (n) { return '<div style="margin:10px 0"><b>Lección ' + n.n + ' · ' + esc(n.tit) + '</b> — ' + n.si.length + ' de ' + (n.si.length + n.no.length) + '<br>' + (n.si.length ? '<small>✅ ' + n.si.map(esc).join(' · ') + '</small><br>' : '') + (n.no.length ? '<small>❌ ' + n.no.map(esc).join(' · ') + '</small>' : '') + '</div>'; }).join('') +
      '<p class="wv-sub">Compara palabras con lo que pide el mapa curricular: sirve para decidir rápido.</p>';
  }
  function filaTranscripcion() {
    var t = L.tr;
    if (!t) return fila('📝', 'Transcripción', '⏳ Se transcribe sola en unos minutos (cuando el video esté subido o generado)', '', 'wv-i-trans');
    if (t.estado === 'error') return fila('📝', 'Transcripción', '⚠️ No se pudo transcribir: ' + esc(t.nota || ''), '', 'wv-i-trans');
    if (t.estado !== 'ok') return fila('📝', 'Transcripción', '⏳ Transcribiendo…', '', 'wv-i-trans');
    var c = cobertura(t.texto, L.fichas);
    return fila('📝', 'Cubre ' + c.pct + '% de la misión', veredicto(c.pct) + (c.falta.length ? ' · Falta: ' + esc(c.falta.slice(0, 4).join(' · ')) + (c.falta.length > 4 ? '…' : '') : ''), boton('trans-ver', 'Ver detalle', 'suave'), 'wv-i-trans');
  }
  function verTranscripcion() {
    var el = document.createElement('div');
    el.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px';
    el.innerHTML = '<div style="background:#fff;border-radius:14px;max-width:760px;width:100%;max-height:90vh;overflow:auto;padding:20px"><h3 style="margin:0 0 8px">Cuánto de la misión cubre el video</h3>' + detalleCobertura(cobertura(L.tr.texto, L.fichas)) +
      '<details><summary>Ver transcripción</summary><p style="white-space:pre-wrap">' + esc(L.tr.texto) + '</p></details><button type="button" class="wv-btn suave" style="margin-top:10px">Cerrar</button></div>';
    document.body.appendChild(el);
    el.querySelector('button').onclick = function () { el.remove(); };
  }
  async function revisarTranscripcion() {
    var el = document.createElement('div');
    el.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px';
    el.innerHTML = '<div style="background:#fff;border-radius:14px;max-width:760px;width:100%;max-height:90vh;overflow:auto;padding:20px">' +
      '<h3 style="margin:0 0 8px">Revisar transcripción del video</h3><p class="wv-sub" style="margin:0 0 10px">Pegá el texto del video. Se compara con lo que pide el mapa curricular para esta misión.</p>' +
      '<textarea id="wv-tr" style="width:100%;min-height:180px;padding:10px;border-radius:10px;border:1px solid #ccd"></textarea>' +
      '<div style="display:flex;gap:8px;margin:10px 0"><button type="button" class="wv-btn" id="wv-tr-ok">Revisar</button><button type="button" class="wv-btn suave" id="wv-tr-x">Cerrar</button></div><div id="wv-tr-res"></div></div>';
    document.body.appendChild(el);
    el.querySelector('#wv-tr-x').onclick = function () { el.remove(); };
    el.querySelector('#wv-tr-ok').onclick = async function () {
      var res = el.querySelector('#wv-tr-res'), txt = el.querySelector('#wv-tr').value;
      if (txt.trim().length < 100) { res.innerHTML = '<p>Pegá una transcripción más larga.</p>'; return; }
      res.innerHTML = '<p>Revisando…</p>';
      try {
        if (!L.fichas || !L.fichas.length) { var lst = S.lessons[R.topic] || []; var rf = await sb.from('lesson_fichas').select('lesson_id, contenidos, no_entra').in('lesson_id', lst.map(function (x) { return x.id; })); L.fichas = lst.map(function (l) { return (rf.data || []).filter(function (f) { return f.lesson_id === l.id; })[0] || null; }); }
        res.innerHTML = detalleCobertura(cobertura(txt, L.fichas));
      } catch (e) { res.innerHTML = '<p>No se pudo revisar: ' + esc(e.message || e) + '</p>'; }
    };
  }

  // ---------- Acciones ----------
  function elegirArchivo(accept, multiple, alElegir) {
    var inp = document.getElementById('wv-file');
    if (!inp) { inp = document.createElement('input'); inp.type = 'file'; inp.id = 'wv-file'; inp.hidden = true; document.body.appendChild(inp); inp.addEventListener('change', function () { var f = inp.files; if (f && f.length && pendiente) pendiente(Array.prototype.slice.call(f)); inp.value = ''; }); }
    inp.accept = accept; inp.multiple = !!multiple; pendiente = alElegir; inp.click();
  }
  function msg(id, txt) { var e = document.getElementById(id); if (e) { var s = e.querySelector('small') || e; s.textContent = txt; } }
  async function guardarPaso(tipo, campos) {
    var r = await sb.from('lesson_steps').update(campos).eq('id', L.pasos[tipo].id).select('id, step_type, stream_uid, r2_key, content, title').single();
    if (r.error) throw r.error;
    L.pasos[tipo] = r.data;
  }
  async function refrescarEstados() { try { await cargarInfo(); } catch (e) { /* se actualiza al volver */ } }

  async function subirVideo(f) {
    try {
      var rv = await WaveEditor.revisarMp4(f);
      if (!rv.ok && !confirm(WaveEditor.avisoMp4)) return;
      msg('wv-i-video', 'Preparando subida…');
      var d = await subidas({ action: 'r2_upload_url', lesson_id: R.lesson, filename: f.name });
      await enviar(d.url, 'PUT', f, function (p) { msg('wv-i-video', 'Subiendo… ' + p + '%'); });
      d.uid = d.key;
      await guardarVideos(videosDe(L.pasos.video).concat([{ uid: d.uid, nombre: f.name, tramos: [] }]));
      toast('Video subido');
      await refrescarEstados(); await abrirLeccion();
    } catch (e) { toast(e.message, true); pintarLeccion(); }
  }
  // Intro de Wave: se sube una sola vez y queda disponible para cualquier lección
  async function subirIntroWave(f) {
    try {
      var rw = await WaveEditor.revisarMp4(f);
      if (!rw.ok && !confirm(WaveEditor.avisoMp4)) return;
      msg('wv-i-introwave', 'Preparando subida…');
      var d = await subidas({ action: 'r2_upload_url', lesson_id: R.lesson, filename: f.name });
      await enviar(d.url, 'PUT', f, function (p) { msg('wv-i-introwave', 'Subiendo… ' + p + '%'); });
      var val = { uid: d.key, nombre: f.name, tramos: [] };
      var ri = await sb.from('app_settings').upsert({ key: 'intro_wave', value: val }, { onConflict: 'key' });
      if (ri.error) throw new Error('El archivo se subió pero no se pudo guardar como intro: ' + ri.error.message);
      S.introWave = val;
      toast('Intro de Wave guardada. Ya la podés agregar a cualquier lección.');
    } catch (e) { toast(e.message, true); }
    pintarLeccion();
  }
  async function subirPdf(f) {
    try {
      msg('wv-i-pdf', 'Subiendo…');
      var d = await subidas({ action: 'r2_upload_url', lesson_id: R.lesson, filename: f.name });
      await enviar(d.url, 'PUT', f, function (p) { msg('wv-i-pdf', 'Subiendo… ' + p + '%'); });
      var viejo = L.pasos.pdf.r2_key;
      await guardarPaso('pdf', { r2_key: d.key, title: f.name });
      await sb.from('lesson_steps').update({ extracted_text: null }).eq('id', L.pasos.pdf.id);
      // El tutor lee el PDF a través de su texto: se extrae en segundo plano
      msg('wv-i-pdf', 'Preparando el tutor con este PDF…');
      sb.functions.invoke('extract-pdf-text', { body: { lesson_step_id: L.pasos.pdf.id } }).then(function (x) {
        var m = x.error ? 'El PDF se subió, pero no se pudo preparar el tutor. Volvé a subirlo.' : (x.data && x.data.error);
        if (m) toast(m, true); else toast('Tutor listo con este PDF');
      });
      if (viejo) { try { await subidas({ action: 'r2_delete', key: viejo }); } catch (e) { /* huérfano */ } }
      toast('PDF subido');
      await refrescarEstados(); pintarLeccion();
    } catch (e) { toast(e.message, true); pintarLeccion(); }
  }
  async function guardarHtml(texto) {
    if (!texto || !texto.trim()) { toast('No hay código para guardar', true); return; }
    if (texto.length > 2000000) { toast('El archivo es demasiado grande (máximo 2 MB)', true); return; }
    try {
      await guardarPaso('interactive_activity', { content: { kind: 'html', html: texto } });
      toast('Actividad guardada');
      await refrescarEstados(); pintarLeccion();
    } catch (e) { toast(e.message || 'No se pudo guardar', true); }
  }
  async function subirDescargables(archivos) {
    var fs = ((L.pasos.complementary_activity.content || {}).files || []).slice();
    try {
      for (var i = 0; i < archivos.length; i++) {
        var f = archivos[i];
        msg('wv-i-desc', 'Subiendo ' + (i + 1) + ' de ' + archivos.length + '…');
        var d = await subidas({ action: 'r2_upload_url', lesson_id: R.lesson, filename: f.name });
        await enviar(d.url, 'PUT', f, function (p) { msg('wv-i-desc', 'Subiendo ' + (i + 1) + ' de ' + archivos.length + '… ' + p + '%'); });
        fs.push({ key: d.key, name: f.name, size: f.size });
        await guardarPaso('complementary_activity', { content: { files: fs } });
      }
      toast(archivos.length === 1 ? 'Archivo subido' : 'Archivos subidos');
    } catch (e) { toast(e.message, true); }
    await refrescarEstados(); pintarLeccion();
  }

  async function abrirLink(key) {
    var w = window.open('', '_blank');
    try { var d = await subidas({ action: 'r2_download_url', key: key }); if (w) w.location = d.url; }
    catch (e) { if (w) w.close(); toast(e.message, true); }
  }

  async function renumerar(tabla, lista) {
    for (var i = 0; i < lista.length; i++) {
      if (lista[i].position !== i + 1) {
        var r = await sb.from(tabla).update({ position: i + 1 }).eq('id', lista[i].id);
        if (r.error) throw r.error;
        lista[i].position = i + 1;
      }
    }
  }

  async function accion(acc) {
    var p = acc.split(':'), a = p[0];
    try {
      if (a === 'video-rec-mas') { var vm = +p[1]; L.recN[vm] = document.querySelectorAll('.wv-recorte[data-vi="' + vm + '"] .wv-rec-fila').length + 1; L.recTmp[vm] = leerRecorte(vm).crudo; return pintarLeccion(); }
      if (a === 'render-estado') { await abrirLeccion(); return; }
      if (a === 'render-pedir') {
        var lr = videosDe(L.pasos.video);
        if (lr.some(function (x) { return esYt(x.uid); })) return toast('Hay videos de YouTube: no se pueden unir. Reemplazalos primero por el archivo del dueño (Videos → Subir archivo del dueño).', true);
        var plan = [];
        lr.forEach(function (x) {
          var tr = x.tramos && x.tramos.length ? x.tramos : [{ i: 0, f: 0 }];
          tr.forEach(function (t) { plan.push({ key: x.uid, i: Number(t.i) || 0, f: Number(t.f) || 0 }); });
        });
        // la intro de Wave va adentro del video final (así el alumno no tiene que volver a darle play)
        if (S.introWave && !(lr[0] && lr[0].intro)) {
          var ti = S.introWave.tramos && S.introWave.tramos.length ? S.introWave.tramos : [{ i: 0, f: 0 }];
          plan = ti.map(function (t) { return { key: S.introWave.uid, i: Number(t.i) || 0, f: Number(t.f) || 0 }; }).concat(plan);
        }
        if (!confirm('Se va a generar UN solo video con los cortes y la intro, listo para internet. Reemplaza los videos de esta lección cuando termine y puede tardar unos minutos. ¿Pedirlo?')) return;
        var ped = await sb.functions.invoke('render-videos', { body: { action: 'pedir', lesson_id: R.lesson, step_id: L.pasos.video.id, plan: plan } });
        if (ped.error) { var mp = 'No se pudo pedir. Intentá de nuevo.'; try { var cj = await ped.error.context.json(); if (cj && cj.error) mp = cj.error; } catch (e0) { /* genérico */ } throw new Error(mp); }
        toast(ped.data && ped.data.lanzado ? 'Pedido enviado: se está generando solo.' : 'Pedido guardado, pero no se pudo arrancar solo (' + ((ped.data && ped.data.aviso) || 'sin detalle') + '). Corré "Video final" en GitHub.', !(ped.data && ped.data.lanzado));
        await abrirLeccion(); return;
      }
      if (a === 'introw-up') return elegirArchivo('video/*', false, function (fs) { subirIntroWave(fs[0]); });
      if (a === 'video-introdef') {
        var xi = videosDe(L.pasos.video)[+p[1]];
        if (!xi || xi.intro) return;
        if (!confirm('¿Usar este video como la intro de Wave? Después la podés agregar con un clic al principio de cualquier lección (con el recorte que tenga ahora).')) return;
        var ri = await sb.from('app_settings').upsert({ key: 'intro_wave', value: { uid: xi.uid, tramos: xi.tramos || [] } }, { onConflict: 'key' });
        if (ri.error) throw new Error('No se pudo guardar la intro: ' + ri.error.message);
        S.introWave = { uid: xi.uid, tramos: xi.tramos || [] };
        toast('Intro de Wave guardada');
        return pintarLeccion();
      }
      if (a === 'video-intro') {
        if (!S.introWave) return toast('Todavía no elegiste la intro de Wave.', true);
        var lw = videosDe(L.pasos.video);
        if (lw[0] && lw[0].intro) return toast('Esta lección ya empieza con la intro.');
        lw.unshift({ uid: S.introWave.uid, nombre: 'Intro de Wave', tramos: S.introWave.tramos || [], intro: true });
        L.recTmp = {}; L.recN = {};
        await guardarVideos(lw);
        toast('Intro agregada al principio');
        await refrescarEstados(); return abrirLeccion();
      }
      if (a === 'video-editar') {
        var ve = +p[1], lista0 = videosDe(L.pasos.video), xe = lista0[ve];
        if (!xe || xe.intro) return;
        var key = xe.uid, blq = WaveEditor.bloque(lista0, key);
        var itemVisor = function (e) {
          return esYt(e.uid) ? { youtube: e.uid.slice(3), tramos: e.tramos }
            : { tramos: e.tramos, url: async function () { return (await subidas({ action: 'stream_token', uid: e.uid, preview: true })).url; } };
        };
        var guardarEd = async function (tr, ins, dur) {
          var le = videosDe(L.pasos.video), src = le.filter(function (x) { return x.uid === key && !x.intro; })[0];
          if (!src) return;
          var srcLimpio = { uid: src.uid, nombre: src.nombre, yt: src.yt };
          var nuevas = WaveEditor.secuencia(srcLimpio, tr, ins, dur, S.introWave || { uid: '', tramos: [] });
          if (!ins.length) nuevas.forEach(function (n) { delete n.grp; });
          L.recN = {}; L.recTmp = {};
          await guardarVideos(WaveEditor.reemplazar(le, key, nuevas));
          toast(ins.length ? 'Guardado, con la intro en ' + ins.length + (ins.length > 1 ? ' lugares' : ' lugar') : (tr.length ? 'Recorte guardado' : 'Se muestra el video entero'));
          pintarLeccion();
        };
        var conf = {
          titulo: nombre('lesson', R.lesson), tramos: blq.tramos, inserts: blq.inserts, guardar: guardarEd,
          intro: !!S.introWave,
          vistaPrevia: function (tr, ins, dur) {
            var src = { uid: key, nombre: '', yt: null };
            return WaveEditor.secuencia(src, tr, ins, dur, S.introWave).map(itemVisor);
          }
        };
        if (esYt(key)) { conf.youtube = key.slice(3); return WaveEditor.abrir(conf); }
        var ste = await subidas({ action: 'stream_status', uid: key });
        if (!ste.ready) return toast('No se encontró el archivo del video.', true);
        conf.url = async function () { return (await subidas({ action: 'stream_token', uid: key, preview: true })).url; };
        return WaveEditor.abrir(conf);
      }
      if (a === 'video-rec') {
        var vr = +p[1], lr = leerRecorte(vr), tr = lr.tramos;
        if (lr.mal) return toast('Escribí los tiempos como minutos:segundos, por ejemplo 0:25', true);
        tr.sort(function (x, y) { return x.i - y.i; });
        for (var q = 0; q < tr.length; q++) {
          if (tr[q].f && tr[q].f <= tr[q].i) return toast('En cada tramo, el final tiene que ser después del inicio.', true);
          if (q < tr.length - 1 && (!tr[q].f || tr[q].f > tr[q + 1].i)) return toast('Los tramos no se pueden pisar: cada uno tiene que terminar antes de que empiece el siguiente.', true);
        }
        var lv = videosDe(L.pasos.video);
        if (!lv[vr]) return;
        lv[vr].tramos = tr;
        L.recN[vr] = 0; L.recTmp[vr] = null;
        await guardarVideos(lv);
        toast(tr.length ? (tr.length > 1 ? 'Recorte guardado (' + tr.length + ' tramos)' : 'Recorte guardado') : 'Se muestra el video entero');
        return pintarLeccion();
      }
      if (a === 'video-revisar') return revisarTranscripcion();
      if (a === 'trans-ver') return verTranscripcion();
      if (a === 'video-yt') {
        var enl = prompt('Pegá el enlace del video de YouTube:');
        if (enl == null) return;
        var idy = idYoutube(enl);
        if (!idy) return toast('Ese enlace no parece de un video de YouTube.', true);
        await guardarVideos(videosDe(L.pasos.video).concat([{ uid: 'yt:' + idy, nombre: '', tramos: [] }]));
        toast('Video de YouTube agregado');
        await refrescarEstados(); return abrirLeccion();
      }
      if (a === 'video-mov') {
        var lm = videosDe(L.pasos.video), de = +p[1], a2 = de + (+p[2]);
        if (!lm[de] || !lm[a2]) return;
        var tmpv = lm[de]; lm[de] = lm[a2]; lm[a2] = tmpv;
        L.recTmp = {}; L.recN = {};
        await guardarVideos(lm);
        return pintarLeccion();
      }
      if (a === 'video-ver') {
        var xv = videosDe(L.pasos.video)[+p[1]];
        if (!xv) return;
        if (esYt(xv.uid)) return WaveVisor.abrirVideo({ titulo: nombre('lesson', R.lesson), youtube: xv.uid.slice(3), tramos: xv.tramos });
        var stv = await subidas({ action: 'stream_status', uid: xv.uid });
        if (!stv.ready) return toast('No se encontró el archivo del video.', true);
        return WaveVisor.abrirVideo({
          titulo: nombre('lesson', R.lesson), tramos: xv.tramos,
          url: async function () { return (await subidas({ action: 'stream_token', uid: xv.uid })).url; }
        });
      }
      if (a === 'intro-up') return elegirArchivo('video/*', false, function (fs) { subirIntro(fs[0]); });
      if (a === 'intro-ver') {
        var sj0 = S.subjects.filter(function (x) { return x.id === R.subject; })[0];
        var sti = await subidas({ action: 'stream_status', uid: sj0.intro_video_uid });
        if (!sti.ready) return toast('No se encontró el archivo del video.', true);
        return WaveVisor.abrirVideo({
          titulo: 'Introducción · ' + nombre('subject', R.subject),
          url: async function () { return (await subidas({ action: 'stream_token', uid: sj0.intro_video_uid })).url; }
        });
      }
      if (a === 'intro-del') {
        if (!confirm('¿Quitar el video de introducción de esta materia?')) return;
        var sj1 = S.subjects.filter(function (x) { return x.id === R.subject; })[0];
        var uid1 = sj1.intro_video_uid;
        chk(await sb.from('subjects').update({ intro_video_uid: null }).eq('id', R.subject));
        sj1.intro_video_uid = null;
        try { await subidas({ action: 'stream_delete', uid: uid1 }); } catch (e) { /* queda huérfano */ }
        return pintar();
      }
      if (a === 'video-up') return elegirArchivo('video/*', true, async function (fs) {
        for (var k = 0; k < fs.length; k++) await subirVideo(fs[k]);
        // optimiza solo lo recién subido (copia liviana para editar y versión que abre rápido)
        try { await sb.functions.invoke('optimizar-videos', { body: { action: 'pedir' } }); toast('Videos subidos: se están optimizando solos (unos minutos).'); } catch (e) { /* queda el botón manual */ }
      });
      if (a === 'video-del') {
        var ld = videosDe(L.pasos.video), xd = ld[+p[1]];
        if (!xd || !confirm(ld.length > 1 ? '¿Quitar el video ' + (+p[1] + 1) + ' de esta lección?' : '¿Quitar el video de esta lección?')) return;
        ld.splice(+p[1], 1);
        L.recTmp = {}; L.recN = {};
        await guardarVideos(ld);
        var enUso = xd.intro || (S.introWave && S.introWave.uid === xd.uid) || ld.some(function (o) { return o.uid === xd.uid; });
        if (!esYt(xd.uid) && !enUso) { try { await subidas({ action: 'stream_delete', uid: xd.uid }); } catch (e) { /* huérfano */ } }
        await refrescarEstados(); return abrirLeccion();
      }
      if (a === 'pdf-up') return elegirArchivo('application/pdf,.pdf', false, function (fs) { subirPdf(fs[0]); });
      if (a === 'pdf-get') {
        var kp = L.pasos.pdf.r2_key;
        return WaveVisor.abrirPdf({
          titulo: L.pasos.pdf.title || 'PDF de la clase',
          url: async function () { return (await subidas({ action: 'r2_download_url', key: kp })).url; }
        });
      }
      if (a === 'pdf-del') {
        if (!confirm('¿Quitar el PDF de esta lección?')) return;
        var k = L.pasos.pdf.r2_key;
        await guardarPaso('pdf', { r2_key: null, title: null });
        await sb.from('lesson_steps').update({ extracted_text: null }).eq('id', L.pasos.pdf.id);
        try { await subidas({ action: 'r2_delete', key: k }); } catch (e) { /* huérfano */ }
        await refrescarEstados(); return pintarLeccion();
      }
      if (a === 'html-up') return elegirArchivo('.html,.htm,text/html', false, function (fs) { fs[0].text().then(guardarHtml); });
      if (a === 'html-save') return guardarHtml((document.getElementById('wv-html-txt') || {}).value);
      if (a === 'html-ver') {
        var u = URL.createObjectURL(new Blob([L.pasos.interactive_activity.content.html || ''], { type: 'text/html' }));
        window.open(u, '_blank'); return;
      }
      if (a === 'html-del') {
        if (!confirm('¿Quitar la actividad interactiva?')) return;
        await guardarPaso('interactive_activity', { content: {} });
        await refrescarEstados(); return pintarLeccion();
      }
      var fs = ((L && L.pasos.complementary_activity.content) || {}).files || [];
      if (a === 'desc-up') return elegirArchivo('*/*', true, subirDescargables);
      if (a === 'desc-get') return abrirLink(fs[+p[1]].key);
      if (a === 'desc-del') {
        if (!confirm('¿Quitar este archivo?')) return;
        var q = fs.splice(+p[1], 1)[0];
        await guardarPaso('complementary_activity', { content: { files: fs } });
        try { await subidas({ action: 'r2_delete', key: q.key }); } catch (e) { /* huérfano */ }
        await refrescarEstados(); return pintarLeccion();
      }
      if (a === 'desc-mov') {
        var i = +p[1], j = i + (+p[2]);
        if (j < 0 || j >= fs.length) return;
        var t = fs[i]; fs[i] = fs[j]; fs[j] = t;
        await guardarPaso('complementary_activity', { content: { files: fs } });
        return pintarLeccion();
      }
      if (a === 'consignas-del') return quitarConsignas();
      if (a === 'examen-del') return quitarExamen();
      if (a === 'examen-pub') {
        var ex0 = chk(await sb.from('exams').select('id').eq('topic_id', R.topic).maybeSingle());
        if (!ex0.data) return;
        if (!confirm('¿Publicar el examen? Desde ahora lo van a ver los alumnos del tema.')) return;
        chk(await sb.rpc('fabrica_publicar_examen', { p_exam: ex0.data.id, p_publicado: true }));
        await refrescarEstados(); toast('Examen publicado'); return pintar();
      }
      if (a === 'examen-ia') {
        if (!confirm('La IA arma un banco de preguntas con el material de las lecciones del tema (un pedido, cobra uso). Queda como borrador hasta que lo publiques. ¿Seguir?')) return;
        chk(await sb.rpc('fabrica_pedir_examen', { p_topic: R.topic }));
        return toast('Pedido enviado. En unos minutos aparece como borrador (si falla, queda el motivo en examen_generacion).');
      }
      if (a === 'del') return eliminar(p[1], p[2]);
      if (a === 'correcciones') return abrirCorrecciones();
      if (a === 'carpeta-ed') return abrirCarpetaEd();
      if (a === 'consignas') return abrirEditor({ kind: 'step', stepId: L.pasos.final_activity.id, sub: nombre('lesson', R.lesson) });
      if (a === 'examen') {
        var ex = await sb.from('exams').select('id, passing_score').eq('topic_id', R.topic).maybeSingle();
        if (ex.error) throw ex.error;
        return abrirEditor({ kind: 'exam', exam: ex.data, sub: nombre('topic', R.topic) });
      }
      if (a === 'mov') return mover(p[1], p[2], +p[3]);
      if (a === 'ren') return renombrar(p[1], p[2]);
      if (a === 'nuevo') return nuevaLeccion();
      if (a === 'temas-completar') return completarTemas();
      if (a === 'pub') return publicarTema(p[2]);
      if (a === 'pub-todo') return publicarTodos(p[1] === '1');
    } catch (e) { console.error(e); toast((e && e.message) || 'No se pudo completar', true); }
  }

  async function fijarPublicado(ids, valor) {
    chk(await sb.from('topics').update({ is_published: valor }).in('id', ids));
    chk(await sb.from('lessons').update({ is_published: valor }).in('topic_id', ids));
    S.topics.forEach(function (t) { if (ids.indexOf(t.id) >= 0) t.is_published = valor; });
    pintar();
  }
  async function publicarTema(id) {
    var t = S.topics.filter(function (x) { return x.id === id; })[0];
    if (!t) return;
    await fijarPublicado([id], !t.is_published);
    toast(t.is_published ? 'Tema publicado: el alumno ya lo ve' : 'Tema oculto para el alumno');
  }
  async function publicarTodos(valor) {
    var ids = temasDe(R.subject).map(function (t) { return t.id; });
    if (!ids.length) return;
    if (!confirm((valor ? 'Publicar' : 'Ocultar') + ' los ' + ids.length + ' temas de esta materia (con todas sus lecciones)?')) return;
    await fijarPublicado(ids, valor);
    toast(valor ? 'Materia publicada' : 'Materia oculta para el alumno');
  }

  async function mover(tipo, id, dir) {
    var tabla = tipo === 'topic' ? 'topics' : 'lessons';
    var lista = tipo === 'topic' ? temasDe(R.subject) : S.lessons[R.topic];
    var i = lista.map(function (x) { return x.id; }).indexOf(id), j = i + dir;
    if (i < 0 || j < 0 || j >= lista.length) return;
    var t = lista[i]; lista[i] = lista[j]; lista[j] = t;
    await renumerar(tabla, lista);
    if (tipo === 'topic') { S.topics.sort(function (a, b) { return a.subject_id === b.subject_id ? a.position - b.position : 0; }); }
    pintar();
  }

  async function renombrar(tipo, id) {
    var lista = tipo === 'topic' ? S.topics : S.lessons[R.topic];
    var it = lista.filter(function (x) { return x.id === id; })[0];
    var nuevoT = prompt('Nuevo nombre:', it.title);
    if (!nuevoT || !nuevoT.trim() || nuevoT.trim() === it.title) return;
    var r = await sb.from(tipo === 'topic' ? 'topics' : 'lessons').update({ title: nuevoT.trim() }).eq('id', id);
    if (r.error) throw r.error;
    it.title = nuevoT.trim();
    pintar();
  }

  async function nuevaLeccion() {
    var n = (S.info[R.topic] || {}).lessons || 0;
    if (n >= LEC_POR_TEMA + 1) return toast('Esta misión ya tiene el máximo de niveles más las generales', true);
    var t = prompt('Nombre de la nueva lección:', 'Lección ' + (n + 1));
    if (!t || !t.trim()) return;
    var l = await sb.from('lessons').insert({ topic_id: R.topic, title: t.trim(), position: n + 1 }).select('id').single();
    if (l.error) throw l.error;
    var ps = await sb.from('lesson_steps').insert(TIPOS.map(function (s, i) { return { lesson_id: l.data.id, step_type: s, position: i + 1 }; }));
    if (ps.error) throw ps.error;
    await refrescarEstados();
    pintar();
  }

  // Crea los temas que faltan para llegar a lo que define el rango de la materia (cada uno con sus 4 lecciones)
  async function completarTemas() {
    var ts = temasDe(R.subject), c = S.cargas[R.subject];
    var faltan = c ? c.topics_total - ts.length : 0;
    if (faltan <= 0) return;
    if (!confirm('Se van a crear ' + faltan + ' temas, cada uno con ' + LEC_POR_TEMA + ' lecciones, para completar el rango. ¿Seguimos?')) return;
    var filas = [];
    for (var k = 0; k < faltan; k++) filas.push({ subject_id: R.subject, title: 'Tema ' + (ts.length + k + 1), position: ts.length + k + 1 });
    var t = await sb.from('topics').insert(filas).select('id, subject_id, title, position, is_published');
    if (t.error) throw t.error;
    var lecs = [];
    t.data.forEach(function (tp) { for (var j = 1; j <= LEC_POR_TEMA; j++) lecs.push({ topic_id: tp.id, title: 'Lección ' + j, position: j }); });
    var l = await sb.from('lessons').insert(lecs).select('id');
    if (l.error) throw l.error;
    var pasos = [];
    l.data.forEach(function (le) { TIPOS.forEach(function (s, i) { pasos.push({ lesson_id: le.id, step_type: s, position: i + 1 }); }); });
    var p = await sb.from('lesson_steps').insert(pasos);
    if (p.error) throw p.error;
    S.topics = S.topics.concat(t.data);
    await refrescarEstados();
    toast('Temas creados');
    pintar();
  }

  // Video de introducción de la materia
  async function subirIntro(f) {
    var sj = S.subjects.filter(function (x) { return x.id === R.subject; })[0];
    try {
      msg('wv-i-intro', 'Preparando subida…');
      var d = await subidas({ action: 'r2_upload_url', lesson_id: R.subject, filename: f.name });
      await enviar(d.url, 'PUT', f, function (p) { msg('wv-i-intro', 'Subiendo… ' + p + '%'); });
      d.uid = d.key;
      var viejo = sj.intro_video_uid;
      var u = await sb.from('subjects').update({ intro_video_uid: d.uid }).eq('id', R.subject);
      if (u.error) throw u.error;
      sj.intro_video_uid = d.uid;
      if (viejo && !esYt(viejo)) { try { await subidas({ action: 'stream_delete', uid: viejo }); } catch (e) { /* huérfano */ } }
      toast('Introducción subida');
    } catch (e) { toast(e.message || 'No se pudo subir', true); }
    pintar();
  }

  // ---------- Eliminar ----------
  function chk(r) {
    if (r.error) throw new Error(r.error.code === '23503' ? 'No se puede eliminar: tiene avance o respuestas de alumnos asociados.' : (r.error.message || 'No se pudo eliminar'));
    return r;
  }

  // Borra las preguntas (y sus guías) de una actividad o de un examen
  async function borrarPreguntas(col, id) {
    var q = chk(await sb.from('questions').select('id').eq(col, id));
    var ids = q.data.map(function (x) { return x.id; });
    if (!ids.length) return;
    chk(await sb.from('question_rubrics').delete().in('question_id', ids));
    chk(await sb.from('questions').delete().in('id', ids));
  }

  async function borrarArchivos(pasos) {
    for (var i = 0; i < pasos.length; i++) {
      var st = pasos[i], claves = [];
      if (st.r2_key) claves.push(st.r2_key);
      ((st.content && st.content.files) || []).forEach(function (f) { if (f.key) claves.push(f.key); });
      var vs = st.step_type === 'video' ? videosDe(st) : [];
      for (var j = 0; j < vs.length; j++) { if (!esYt(vs[j].uid)) { try { await subidas({ action: 'stream_delete', uid: vs[j].uid }); } catch (e) { /* queda huérfano */ } } }
      for (var k = 0; k < claves.length; k++) { try { await subidas({ action: 'r2_delete', key: claves[k] }); } catch (e) { /* queda huérfano */ } }
    }
  }

  async function quitarConsignas() {
    if (!confirm('¿Quitar todas las consignas de esta lección?')) return;
    await borrarPreguntas('lesson_step_id', L.pasos.final_activity.id);
    L.preguntas = 0;
    await refrescarEstados();
    toast('Consignas quitadas');
    pintarLeccion();
  }

  async function quitarExamen() {
    if (!confirm('¿Quitar el examen de este tema con todas sus preguntas?')) return;
    var ex = chk(await sb.from('exams').select('id').eq('topic_id', R.topic).maybeSingle());
    if (ex.data) {
      await borrarPreguntas('exam_id', ex.data.id);
      chk(await sb.from('exams').delete().eq('id', ex.data.id));
    }
    await refrescarEstados();
    toast('Examen quitado');
    pintar();
  }

  async function eliminarLeccion(id) {
    var st = chk(await sb.from('lesson_steps').select('id, step_type, stream_uid, r2_key, content').eq('lesson_id', id));
    var ids = st.data.map(function (x) { return x.id; });
    if (ids.length) {
      var q = chk(await sb.from('questions').select('id').in('lesson_step_id', ids));
      var qids = q.data.map(function (x) { return x.id; });
      if (qids.length) {
        chk(await sb.from('question_rubrics').delete().in('question_id', qids));
        chk(await sb.from('questions').delete().in('id', qids));
      }
    }
    chk(await sb.from('lesson_steps').delete().eq('lesson_id', id));
    chk(await sb.from('lessons').delete().eq('id', id));
    await borrarArchivos(st.data);
  }

  async function eliminar(tipo, id) {
    if (tipo === 'lesson') {
      if (!confirm('¿Eliminar esta lección y todo lo que tiene cargado? No se puede deshacer.')) return;
      await eliminarLeccion(id);
      var restantes = (S.lessons[R.topic] || []).filter(function (x) { return x.id !== id; });
      S.lessons[R.topic] = restantes;
      await renumerar('lessons', restantes);
      toast('Lección eliminada');
    } else {
      if (!confirm('¿Eliminar este tema con sus lecciones, el examen y todo lo cargado? No se puede deshacer.')) return;
      var ls = chk(await sb.from('lessons').select('id').eq('topic_id', id));
      for (var i = 0; i < ls.data.length; i++) await eliminarLeccion(ls.data[i].id);
      var ex = chk(await sb.from('exams').select('id').eq('topic_id', id).maybeSingle());
      if (ex.data) {
        await borrarPreguntas('exam_id', ex.data.id);
        chk(await sb.from('exams').delete().eq('id', ex.data.id));
      }
      chk(await sb.from('topics').delete().eq('id', id));
      S.topics = S.topics.filter(function (x) { return x.id !== id; });
      await renumerar('topics', temasDe(R.subject));
      toast('Tema eliminado');
    }
    await refrescarEstados();
    pintar();
  }

  // ---------- Carpeta: consignas que ve el alumno + clave con la que la app las corrige (sin IA) ----------
  var CE = null;
  function carpetaItems() {
    var cs = (L.pasos.pdf.content && Array.isArray(L.pasos.pdf.content.carpeta)) ? L.pasos.pdf.content.carpeta : [];
    return cs.map(function (c, i) {
      var k = L.claves[i] || {};
      return { consigna: typeof c === 'string' ? c : (c && c.consigna) || '', acepta: (k.acepta || []).join(' | '), solucion: k.solucion || '' };
    });
  }
  function abrirCarpetaEd() {
    CE = { items: carpetaItems() };
    if (!CE.items.length) CE.items.push({ consigna: '', acepta: '', solucion: '' });
    CE.el = document.createElement('div'); CE.el.className = 'wv-modal';
    CE.caja = document.createElement('div'); CE.caja.className = 'wv-modal-caja ancha';
    CE.el.appendChild(CE.caja); document.body.appendChild(CE.el);
    CE.caja.addEventListener('input', function (ev) { var t = ev.target; if (t.dataset.ci !== undefined) CE.items[+t.dataset.ci][t.dataset.f] = t.value; });
    CE.caja.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-acc]'); if (!b || b.disabled) return;
      carpetaAccion(b.getAttribute('data-acc'));
    });
    pintarCarpetaEd();
  }
  function cerrarCarpetaEd() { if (CE && CE.el) CE.el.remove(); CE = null; }
  function pintarCarpetaEd() {
    var h = '<h2>Carpeta del nivel</h2><p>' + esc(nombre('lesson', R.lesson)) + '</p>' +
      '<p class="wv-ayuda-e">El alumno ve la consigna y escribe una respuesta corta. La app la compara con las respuestas válidas (no importan mayúsculas, espacios ni puntos: 4.205 = 4205). Si hay más de una forma correcta, separalas con |. La solución se muestra cuando entrega todo bien.</p>';
    h += CE.items.map(function (it, i) {
      return '<div class="wv-preg"><div class="wv-preg-cab"><b>' + (i + 1) + '.</b><span class="wv-preg-herr">' +
        '<button type="button" class="wv-ico" data-acc="ce-mov:' + i + ':-1"' + (i === 0 ? ' disabled' : '') + '>▲</button>' +
        '<button type="button" class="wv-ico" data-acc="ce-mov:' + i + ':1"' + (i === CE.items.length - 1 ? ' disabled' : '') + '>▼</button>' +
        '<button type="button" class="wv-ico" title="Quitar" data-acc="ce-del:' + i + '">🗑</button></span></div>' +
        '<label class="wv-lbl-e">Consigna (lo que ve el alumno)</label><textarea rows="2" data-ci="' + i + '" data-f="consigna">' + esc(it.consigna) + '</textarea>' +
        '<label class="wv-lbl-e">Respuestas válidas (separadas con |)</label><input type="text" data-ci="' + i + '" data-f="acepta" value="' + esc(it.acepta) + '">' +
        '<label class="wv-lbl-e">Solución que se muestra después de entregar</label><textarea rows="2" data-ci="' + i + '" data-f="solucion">' + esc(it.solucion) + '</textarea></div>';
    }).join('');
    h += '<div class="wv-ed-nuevo">' + boton('ce-add', '+ Agregar consigna', 'suave') + '</div>' +
      '<details class="wv-pegar"><summary>Cargar todo pegando un JSON</summary><textarea id="wv-ce-json" rows="6" placeholder=\'[{"consigna":"...","acepta":["11"],"solucion":"..."}]\'></textarea>' + boton('ce-json', 'Cargar JSON', 'suave') + '</details>' +
      '<div class="wv-modal-pie">' + boton('ce-cancel', 'Cancelar', 'suave') + boton('ce-save', 'Guardar', '') + '</div>';
    CE.caja.innerHTML = h;
  }
  async function carpetaAccion(acc) {
    var p = acc.split(':'), a = p[0], i = +p[1];
    if (a === 'ce-cancel') return cerrarCarpetaEd();
    if (a === 'ce-add') { CE.items.push({ consigna: '', acepta: '', solucion: '' }); return pintarCarpetaEd(); }
    if (a === 'ce-del') { if (!confirm('¿Quitar esta consigna?')) return; CE.items.splice(i, 1); return pintarCarpetaEd(); }
    if (a === 'ce-mov') { var j = i + (+p[2]); if (j < 0 || j >= CE.items.length) return; var x = CE.items[i]; CE.items[i] = CE.items[j]; CE.items[j] = x; return pintarCarpetaEd(); }
    if (a === 'ce-json') {
      try {
        var arr = JSON.parse((document.getElementById('wv-ce-json') || {}).value || '[]');
        if (!Array.isArray(arr) || !arr.length) throw new Error('vacío');
        CE.items = arr.map(function (o) { return { consigna: String(o.consigna || ''), acepta: [].concat(o.acepta || []).join(' | '), solucion: String(o.solucion || '') }; });
        return pintarCarpetaEd();
      } catch (e) { return toast('El JSON no es válido. Tiene que ser una lista de {consigna, acepta, solucion}.', true); }
    }
    if (a === 'ce-save') {
      var items = CE.items.filter(function (it) { return it.consigna.trim() || it.acepta.trim() || it.solucion.trim(); });
      if (!items.length) return toast('Agregá al menos una consigna.', true);
      for (var k = 0; k < items.length; k++) {
        if (!items[k].consigna.trim()) return toast('La consigna ' + (k + 1) + ' no tiene texto.', true);
        if (!items[k].acepta.split('|').some(function (s) { return s.trim(); })) return toast('La consigna ' + (k + 1) + ' no tiene respuesta válida.', true);
      }
      try {
        var claves = items.map(function (it) { return { acepta: it.acepta.split('|').map(function (s) { return s.trim(); }).filter(Boolean), solucion: it.solucion.trim() }; });
        await guardarPaso('pdf', { content: Object.assign({}, L.pasos.pdf.content || {}, { carpeta: items.map(function (it) { return it.consigna.trim(); }) }) });
        var r = await sb.from('carpeta_claves').upsert({ lesson_step_id: L.pasos.pdf.id, items: claves, updated_at: new Date().toISOString() });
        if (r.error) throw r.error;
        L.claves = claves;
        cerrarCarpetaEd();
        await refrescarEstados();
        pintarLeccion();
        toast('Carpeta guardada');
      } catch (e) { console.error(e); toast('No pudimos guardar la carpeta: ' + (e.message || e), true); }
    }
  }

  // ---------- Editor de preguntas (actividades de cada nivel y nivel jefe) ----------
  var ED = null;
  var TIPOS_PREG = { open: 'Respuesta abierta', short_answer: 'Respuesta corta', multiple_choice: 'Opción múltiple', true_false: 'Verdadero / Falso' };
  // Tipos que arma la máquina: se editan el enunciado, la respuesta y los criterios; la estructura (opciones, pares, tabla) se ve y edita como texto.
  var TIPOS_MAQ = { fill_blank: 'Completar espacios', ordering: 'Ordenar pasos', matching: 'Unir columnas', classify: 'Clasificar', table_fill: 'Completar tabla', multi_select: 'Selección múltiple', solve_complete: 'Resolver y completar', odd_one_out: 'Encontrar el intruso' };
  // Tipos nuevos: se corrigen sin IA. La estructura (lo que ve el alumno) y la clave (lo correcto, que el alumno nunca ve) se escriben como JSON.
  var TIPOS_AUTO = { numeric: 'Número (resultado)', tap_text: 'Tocá el texto / Subrayá y clasificá / Detective del error', tokens: 'Armá con fichas / Reto de armado', keywords: 'Palabras clave', label_image: 'Rotulá el dibujo' };
  var AYUDA_TIPO = {
    numeric: { est: '{"unidad":"min"}  ·  números al azar: {"vars":{"a":{"min":12,"max":90},"b":{"min":3,"max":9}},"reglas":["a%10!=0"]} y en el enunciado usá {a} y {b}',
      clave: '{"acepta":[6000]}  ·  con azar: {"formula":"a*b"}  ·  opcional "tolerancia":0.5, "unidad":"min", "modo":"texto" (para binario: {"acepta":["1101"],"modo":"texto"})' },
    tap_text: { est: '{"segmentos":["palabra1","palabra2"],"modo":"palabras"}  ·  clasificar: sumá "categorias":["Sujeto","Predicado"]  ·  detective: "modo":"lineas","categorias":["Error de cuenta","No hay error"],"pide_correccion":"¿Cuál es el valor correcto?"',
      clave: '{"tocar":[1,3]}  ·  con categorías: {"categorias":{"1":"Sujeto","2":"Predicado"}}  ·  detective: {"categorias":{"1":"Error de cuenta"},"correccion":["60"]}  (los números son la posición del segmento, empezando en 0)' },
    tokens: { est: 'Armar en orden: {"fichas":["4","×","1.000","+","2","×","100","10"]}  ·  Reto: {"fichas":["8","8","3","3"],"objetivo":24,"usar_todas":true}',
      clave: 'Armar en orden: {"soluciones":[["4","×","1.000","+","2","×","100"]]}  ·  Reto: {"ejemplo":"8 ÷ ( 3 − 8 ÷ 3 )"} (solo para mostrar; cualquier cuenta que dé el objetivo vale)' },
    keywords: { est: '{"ayuda":"Una o dos oraciones."}',
      clave: '{"grupos":[["lugar","posicion*"],["valor"],["diez","10"]],"minimo":3}  (cada grupo son sinónimos; con * acepta cualquier terminación)' },
    label_image: { est: '{"imagen":"data:image/png;base64,...","alt":"descripción","puntos":[{"id":"1","x":50,"y":50}],"rotulos":["Núcleo","Membrana"]}  (x e y en % de la imagen)',
      clave: '{"puntos":{"1":"Núcleo","2":"Membrana"}}' }
  };
  // Los tipos de arriba y estos viejos tienen su clave en JSON (reference_answer); open y solve_complete siguen con la IA
  var CLAVE_JSON = { numeric: 1, tap_text: 1, tokens: 1, keywords: 1, label_image: 1, fill_blank: 1, ordering: 1, matching: 1, classify: 1, table_fill: 1, multi_select: 1, short_answer: 1 };
  var CLAVE_VIEJOS = {
    fill_blank: '{"huecos":[["2.000","2000"],["400"]]}', ordering: '{"orden":["paso 1","paso 2","paso 3"]}', matching: '{"pares":{"izquierda 1":"derecha 1"}}',
    classify: '{"categorias":{"elemento":"categoría"}}', table_fill: '{"celdas":{"1|Valor":["200"]}}  (fila|columna)', multi_select: '{"correctas":["opción A","opción C"]}', short_answer: '{"acepta":["respuesta","otra forma"]}'
  };
  function nombreTipo(t) { return TIPOS_PREG[t] || TIPOS_MAQ[t] || TIPOS_AUTO[t] || t; }

  function jsonOTexto(s, tolerante) { try { return JSON.parse(s); } catch (e) { if (tolerante) return s; throw e; } }
  function pregVacia(tipo) {
    return {
      id: null, type: tipo, prompt: '', points: 1, correct: -1, ref: '', expl: '', rubric: '', tiempo: '', maq: !!TIPOS_AUTO[tipo], estructura: '',
      options: tipo === 'multiple_choice' ? ['', '', ''] : tipo === 'true_false' ? ['Verdadero', 'Falso'] : []
    };
  }

  async function abrirEditor(ctx) {
    var col = ctx.kind === 'exam' ? 'exam_id' : 'lesson_step_id';
    var id = ctx.kind === 'exam' ? (ctx.exam && ctx.exam.id) : ctx.stepId;
    var qs = [];
    if (id) {
      var r = await sb.from('questions').select('id, question_type, prompt, options, points, position, tiempo_seg').eq(col, id).order('position');
      if (r.error) throw r.error;
      var ids = r.data.map(function (x) { return x.id; });
      var rb = ids.length ? await sb.from('question_rubrics').select('question_id, reference_answer, explanation, rubric').in('question_id', ids) : { data: [] };
      if (rb.error) throw rb.error;
      var mapa = {};
      rb.data.forEach(function (x) { mapa[x.question_id] = x; });
      qs = r.data.map(function (q) {
        var u = mapa[q.id] || {};
        var ref = typeof u.reference_answer === 'string' ? u.reference_answer : (u.reference_answer ? JSON.stringify(u.reference_answer, null, 1) : '');
        var o = Array.isArray(q.options) ? q.options.map(String) : [];
        var cerrada = q.question_type === 'multiple_choice' || q.question_type === 'true_false';
        var maq = !!TIPOS_MAQ[q.question_type] || !!TIPOS_AUTO[q.question_type];
        return { id: q.id, type: q.question_type, prompt: q.prompt, points: q.points, options: o,
          correct: cerrada ? o.indexOf(ref) : -1, ref: cerrada ? '' : ref, expl: u.explanation || '', rubric: u.rubric || '',
          tiempo: q.tiempo_seg || '', maq: maq, estructura: maq && q.options != null ? JSON.stringify(q.options, null, 1) : '' };
      });
    }
    ED = { ctx: ctx, qs: qs, quitadas: [], pasa: ctx.kind === 'exam' && ctx.exam ? ctx.exam.passing_score : 70 };
    ED.el = document.createElement('div');
    ED.el.className = 'wv-modal';
    ED.caja = document.createElement('div');
    ED.caja.className = 'wv-modal-caja ancha';
    ED.el.appendChild(ED.caja);
    document.body.appendChild(ED.el);
    ED.caja.addEventListener('input', editorCambio);
    ED.caja.addEventListener('change', editorCambio);
    ED.caja.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-acc]');
      if (b && !b.disabled) editorAccion(b.getAttribute('data-acc'));
    });
    pintarEditor();
  }

  function cerrarEditor() { if (ED && ED.el) ED.el.remove(); ED = null; }

  function editorCambio(ev) {
    var t = ev.target;
    if (t.dataset.ed === 'pasa') { ED.pasa = +t.value; return; }
    if (t.dataset.q === undefined) return;
    var q = ED.qs[+t.dataset.q], f = t.dataset.f;
    if (f === 'points') q.points = Math.max(1, Math.round(+t.value) || 1);
    else if (f === 'opt') q.options[+t.dataset.j] = t.value;
    else if (f === 'correct') q.correct = +t.value;
    else q[f] = t.value;
  }

  function cardPreg(q, i, n) {
    var cerrada = q.type === 'multiple_choice' || q.type === 'true_false';
    var h = '<div class="wv-preg"><div class="wv-preg-cab"><b>' + (i + 1) + '.</b><span class="wv-etq vacia">' + nombreTipo(q.type) + '</span>' +
      '<label class="wv-puntos">Puntos <input type="number" min="1" max="100" data-q="' + i + '" data-f="points" value="' + q.points + '"></label>' +
      '<span class="wv-preg-herr"><button type="button" class="wv-ico" data-acc="ed-mov:' + i + ':-1"' + (i === 0 ? ' disabled' : '') + '>▲</button>' +
      '<button type="button" class="wv-ico" data-acc="ed-mov:' + i + ':1"' + (i === n - 1 ? ' disabled' : '') + '>▼</button>' +
      '<button type="button" class="wv-ico" title="Quitar pregunta" data-acc="ed-del:' + i + '">🗑</button></span></div>' +
      '<textarea rows="2" data-q="' + i + '" data-f="prompt" placeholder="Escribí la pregunta o la consigna">' + esc(q.prompt) + '</textarea>';
    if (q.type === 'multiple_choice') {
      h += '<small class="wv-ayuda-e">Marcá con el círculo cuál es la respuesta correcta.</small>';
      q.options.forEach(function (o, j) {
        h += '<div class="wv-opc"><input type="radio" name="c' + i + '" data-q="' + i + '" data-f="correct" value="' + j + '"' + (q.correct === j ? ' checked' : '') + '>' +
          '<input type="text" data-q="' + i + '" data-f="opt" data-j="' + j + '" value="' + esc(o) + '" placeholder="Opción ' + (j + 1) + '">' +
          '<button type="button" class="wv-ico" data-acc="ed-optdel:' + i + ':' + j + '"' + (q.options.length <= 2 ? ' disabled' : '') + '>✕</button></div>';
      });
      h += '<button type="button" class="wv-btn mini suave" data-acc="ed-optadd:' + i + '">+ Agregar opción</button>';
    } else if (q.type === 'true_false') {
      h += '<small class="wv-ayuda-e">¿Cuál es la respuesta correcta?</small><div class="wv-opc">';
      q.options.forEach(function (o, j) {
        h += '<label class="wv-tf"><input type="radio" name="c' + i + '" data-q="' + i + '" data-f="correct" value="' + j + '"' + (q.correct === j ? ' checked' : '') + '> ' + esc(o) + '</label>';
      });
      h += '</div>';
    }
    if (q.maq) {
      h += '<label class="wv-lbl-e">Estructura de la consigna (opciones, pares o tabla). Si no estás segura, no la toques.</label>' +
        '<textarea rows="4" data-q="' + i + '" data-f="estructura" spellcheck="false">' + esc(q.estructura) + '</textarea>';
    }
    var ay = AYUDA_TIPO[q.type];
    if (q.maq && ay) h += '<small class="wv-ayuda-e">Ejemplo de estructura: ' + esc(ay.est) + '</small>';
    if (CLAVE_JSON[q.type]) {
      h += '<label class="wv-lbl-e">Clave de corrección (JSON). La app corrige sola con esto, sin IA; el alumno nunca la ve.</label>' +
        '<textarea rows="3" data-q="' + i + '" data-f="ref" spellcheck="false">' + esc(q.ref) + '</textarea>' +
        '<small class="wv-ayuda-e">Ejemplo: ' + esc(ay ? ay.clave : CLAVE_VIEJOS[q.type] || '') + '</small>';
    } else if (!cerrada) {
      h += '<label class="wv-lbl-e">Respuesta de referencia (opcional, la usa la IA para corregir)</label>' +
        '<textarea rows="2" data-q="' + i + '" data-f="ref">' + esc(q.ref) + '</textarea>';
    }
    h += '<label class="wv-puntos">⚡ Relámpago: segundos para responder (vacío = sin tiempo) <input type="number" min="3" max="300" data-q="' + i + '" data-f="tiempo" value="' + esc(q.tiempo) + '"></label>';
    h += '<details class="wv-pegar"><summary>Criterios y explicación (opcional)</summary>' +
      '<label class="wv-lbl-e">Criterios de corrección para la IA</label><textarea rows="2" data-q="' + i + '" data-f="rubric">' + esc(q.rubric) + '</textarea>' +
      '<label class="wv-lbl-e">Explicación de la respuesta</label><textarea rows="2" data-q="' + i + '" data-f="expl">' + esc(q.expl) + '</textarea></details></div>';
    return h;
  }

  function pintarEditor() {
    var c = ED.ctx, exam = c.kind === 'exam';
    var h = '<h2>' + (exam ? 'Nivel jefe (examen corto)' : (L && L.gen ? 'Las 4 generales' : 'Las 2 actividades del nivel')) + '</h2><p>' + esc(c.sub) + '</p>';
    if (exam) h += '<label class="wv-puntos wv-pasa">Nota mínima para aprobar <input type="number" min="0" max="100" data-ed="pasa" value="' + ED.pasa + '"></label>';
    h += ED.qs.map(function (q, i) { return cardPreg(q, i, ED.qs.length); }).join('') ||
      '<div class="wv-vacio">Todavía no hay preguntas. Agregá la primera.</div>';
    h += '<div class="wv-ed-nuevo"><b>Agregar:</b> ' + Object.keys(TIPOS_PREG).map(function (k) { return boton('ed-add:' + k, '+ ' + TIPOS_PREG[k], 'suave'); }).join('') + '</div>' +
      '<div class="wv-ed-nuevo"><b>Sin IA:</b> ' + Object.keys(TIPOS_AUTO).map(function (k) { return boton('ed-add:' + k, '+ ' + TIPOS_AUTO[k].split(' / ')[0], 'suave'); }).join('') + '</div>';
    h += '<div class="wv-modal-pie">' + boton('ed-cancel', 'Cancelar', 'suave') + boton('ed-save', 'Guardar', '') + '</div>';
    ED.caja.innerHTML = h;
  }

  function editorAccion(acc) {
    var p = acc.split(':'), a = p[0], i = +p[1];
    if (a === 'ed-cancel') return cerrarEditor();
    if (a === 'ed-save') return guardarEditor();
    if (a === 'ed-add') {
      ED.qs.push(pregVacia(p[1]));
      pintarEditor();
      var cards = ED.caja.querySelectorAll('.wv-preg');
      if (cards.length) cards[cards.length - 1].scrollIntoView({ block: 'center' });
      return;
    }
    var q = ED.qs[i];
    if (a === 'ed-del') {
      if (!confirm('¿Quitar esta pregunta?')) return;
      if (q.id) ED.quitadas.push(q.id);
      ED.qs.splice(i, 1);
    } else if (a === 'ed-mov') {
      var j = i + (+p[2]);
      if (j < 0 || j >= ED.qs.length) return;
      ED.qs[i] = ED.qs[j]; ED.qs[j] = q;
    } else if (a === 'ed-optadd') {
      q.options.push('');
    } else if (a === 'ed-optdel') {
      var k = +p[2];
      q.options.splice(k, 1);
      if (q.correct === k) q.correct = -1; else if (q.correct > k) q.correct--;
    }
    pintarEditor();
  }

  async function guardarEditor() {
    var c = ED.ctx, qs = ED.qs, exam = c.kind === 'exam';
    for (var i = 0; i < qs.length; i++) {
      var q = qs[i], n = i + 1;
      if (!q.prompt.trim()) return toast('La pregunta ' + n + ' está vacía', true);
      if (q.type === 'multiple_choice') {
        if (q.options.filter(function (o) { return o.trim(); }).length < 2) return toast('La pregunta ' + n + ' necesita al menos 2 opciones', true);
        if (q.correct < 0 || !(q.options[q.correct] || '').trim()) return toast('Marcá la respuesta correcta en la pregunta ' + n, true);
      }
      if (q.type === 'true_false' && q.correct < 0) return toast('Marcá la respuesta correcta en la pregunta ' + n, true);
      if (q.maq && q.estructura.trim()) { try { JSON.parse(q.estructura); } catch (e1) { return toast('La estructura de la pregunta ' + n + ' no está bien escrita', true); } }
      if (TIPOS_AUTO[q.type] && !q.estructura.trim()) return toast('Falta la estructura de la pregunta ' + n, true);
      if (CLAVE_JSON[q.type] && q.type !== 'short_answer' && q.ref.trim()) { try { JSON.parse(q.ref); } catch (e2) { return toast('La clave de corrección de la pregunta ' + n + ' no está bien escrita', true); } }
      if (CLAVE_JSON[q.type] && !q.ref.trim() && TIPOS_AUTO[q.type]) return toast('Falta la clave de corrección de la pregunta ' + n, true);
    }
    if (exam && !qs.length) return toast('El examen necesita al menos una pregunta', true);
    var btn = ED.caja.querySelector('[data-acc="ed-save"]');
    if (btn) { btn.disabled = true; btn.textContent = 'Guardando…'; }
    try {
      var clave, col;
      if (exam) {
        var pasa = Math.min(100, Math.max(0, Math.round(ED.pasa)));
        if (isNaN(pasa)) pasa = 70;
        col = 'exam_id';
        if (c.exam && c.exam.id) {
          clave = c.exam.id;
          var u = await sb.from('exams').update({ passing_score: pasa }).eq('id', clave);
          if (u.error) throw u.error;
        } else {
          var e = await sb.from('exams').insert({ topic_id: R.topic, title: 'Examen: ' + nombre('topic', R.topic), passing_score: pasa }).select('id').single();
          if (e.error) throw e.error;
          clave = e.data.id;
          c.exam = { id: clave, passing_score: pasa };
        }
      } else { col = 'lesson_step_id'; clave = c.stepId; }

      if (ED.quitadas.length) {
        var d1 = await sb.from('question_rubrics').delete().in('question_id', ED.quitadas);
        if (d1.error) throw d1.error;
        var d2 = await sb.from('questions').delete().in('id', ED.quitadas);
        if (d2.error) throw d2.error;
        ED.quitadas = [];
      }
      for (var k = 0; k < qs.length; k++) {
        var x = qs[k], cerrada = x.type === 'multiple_choice' || x.type === 'true_false';
        var ref = cerrada ? (x.options[x.correct] || '').trim() : x.ref.trim();
        var opts = cerrada ? x.options.map(function (o) { return o.trim(); }).filter(Boolean) : [];
        var fila = { question_type: x.type, prompt: x.prompt.trim(), options: opts.length ? opts : null, points: x.points, position: k + 1, tiempo_seg: x.tiempo ? +x.tiempo : null };
        if (x.maq) fila.options = x.estructura.trim() ? JSON.parse(x.estructura) : null;
        if (x.id) {
          var up = await sb.from('questions').update(fila).eq('id', x.id);
          if (up.error) throw up.error;
        } else {
          fila[col] = clave;
          var ins = await sb.from('questions').insert(fila).select('id').single();
          if (ins.error) throw ins.error;
          x.id = ins.data.id;
        }
        var rb = await sb.from('question_rubrics').upsert({ question_id: x.id, reference_answer: !ref ? null : (CLAVE_JSON[x.type] ? jsonOTexto(ref, x.type === 'short_answer') : ref), explanation: x.expl.trim() || null, rubric: x.rubric.trim() || null }, { onConflict: 'question_id' });
        if (rb.error) throw rb.error;
      }
      toast(exam ? 'Examen guardado' : 'Consignas guardadas');
      cerrarEditor();
      if (exam) { await refrescarEstados(); pintar(); }
      else { L.preguntas = qs.length; pintarLeccion(); }
    } catch (err) {
      console.error(err);
      toast((err && (err.message || err.details)) || 'No se pudo guardar', true);
      if (btn) { btn.disabled = false; btn.textContent = 'Guardar'; }
    }
  }

  // ---------- Entrada ----------
  var enlazado = false;
  async function abrir(el) {
    vista = el;
    if (!enlazado) {
      enlazado = true;
      vista.addEventListener('click', function (ev) {
        var a = ev.target.closest('[data-ir]');
        if (a) { ev.preventDefault(); ir(a.getAttribute('data-ir')); return; }
        var b = ev.target.closest('[data-acc]');
        if (b && !b.disabled) accion(b.getAttribute('data-acc'));
      });
    }
    if (!S.listo) {
      vista.innerHTML = '<h1 class="wv-titulo">Contenido</h1><div class="wv-vacio">Cargando…</div>';
      await cargarBase();
      // al recargar la página (F5) se vuelve a la carpeta donde estabas
      try { var g = JSON.parse(localStorage.getItem('wv-contenido-ruta') || 'null'); if (g) Object.keys(R).forEach(function (k) { R[k] = g[k] || null; }); } catch (e) { /* ruta guardada inválida: se arranca de cero */ }
    }
    pintar();
  }

  // Solo para pruebas visuales de la pantalla de una lección con datos de ejemplo
  function _probar(el, pasos) { vista = el; L = { pasos: pasos, preguntas: 0, recTmp: {}, recN: {} }; el.innerHTML = '<div id="wv-les"></div>'; el.onclick = function (ev) { var b = ev.target.closest('[data-acc]'); if (b && !b.disabled) accion(b.getAttribute('data-acc')); }; pintarLeccion(); }

  window.WaveContenido = { abrir: abrir, _probar: _probar };
})();
