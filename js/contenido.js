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
    if (f.lessons >= LEC_POR_TEMA && f.completas >= LEC_POR_TEMA && f.tiene_examen) return 'ok';
    if (f.completas === 0 && f.con_algo === 0 && !f.tiene_examen) return 'vacia';
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
    if (Array.isArray(c.videos) && c.videos.length) return c.videos.map(function (x) { return { uid: x.uid, nombre: x.nombre || '', tramos: x.tramos || [] }; });
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
    return h + '<div class="wv-rec-b">' + boton('video-editar:' + vi, '🎞️ Editar mirando el video', '') + boton('video-rec-mas:' + vi, '+ Agregar otra parte', 'suave') + boton('video-rec:' + vi, 'Guardar recorte', 'suave') + '</div><small>Minutos:segundos. Todo vacío = video entero. Para quitar una parte, dejá su fila vacía y guardá.</small></div>';
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
      var det = (c ? S.tiers[c.tier] + ' · ' : '') + ts.length + (c ? ' de ' + c.topics_total : '') + ' temas · ' + ls + ' lecciones';
      return carpeta('subject', s.id, s.name, det, estadoMateria(s.id));
    }).join('') + '</div>';
  }
  function vTemas() {
    var ts = temasDe(R.subject);
    var c = S.cargas[R.subject], h = '';
    if (c) {
      h += '<div class="wv-rango">Rango <b>' + esc(S.tiers[c.tier]) + '</b>: ' + c.hours_total + ' horas · ' + c.topics_total + ' temas · ' +
        c.topics_total * LEC_POR_TEMA + ' lecciones (' + LEC_POR_TEMA + ' por tema)</div>';
      if (ts.length < c.topics_total) {
        h += '<div class="wv-aviso">Faltan ' + (c.topics_total - ts.length) + ' temas para completar el rango. ' +
          '<button class="wv-btn mini" type="button" data-acc="temas-completar">Crear los temas que faltan</button></div>';
      } else if (ts.length > c.topics_total) {
        h += '<div class="wv-aviso">Hay ' + (ts.length - c.topics_total) + ' temas de más respecto del rango.</div>';
      }
    }
    var sj = S.subjects.filter(function (x) { return x.id === R.subject; })[0] || {};
    var tieneIntro = !!sj.intro_video_uid;
    h += '<div class="wv-intro">' + fila('🎬', 'Introducción de la materia', tieneIntro ? 'Video cargado' : 'Sin video: el alumno ve "Próximamente"',
      (tieneIntro ? boton('intro-ver', 'Ver') : '') + boton('intro-up', tieneIntro ? 'Reemplazar' : 'Subir video', tieneIntro ? 'suave' : '') + (tieneIntro ? boton('intro-del', 'Quitar', 'peligro') : ''), 'wv-i-intro') + '</div>';
    if (!ts.length) return h + '<div class="wv-vacio">Esta materia todavía no tiene temas.</div>';
    var nPub = ts.filter(function (t) { return t.is_published; }).length;
    h += '<div class="wv-rango">Visibles para el alumno: <b>' + nPub + ' de ' + ts.length + ' temas</b>. Lo que está oculto el alumno no lo ve. ' +
      boton('pub-todo:1', 'Publicar todos') + ' ' + boton('pub-todo:0', 'Ocultar todos') + '</div>';
    return h + '<div class="wv-carps">' + ts.map(function (t, i) {
      var f = S.info[t.id] || {};
      var pub = '<button type="button" class="wv-ico wv-pub ' + (t.is_published ? 'on' : '') + '" data-acc="pub:topic:' + t.id + '" title="' + (t.is_published ? 'Visible para el alumno (tocá para ocultar)' : 'Oculto para el alumno (tocá para publicar)') + '">' + (t.is_published ? '👁 Visible' : '🚫 Oculto') + '</button>';
      return carpeta('topic', t.id, t.title, (f.lessons || 0) + ' lecciones · examen ' + (f.tiene_examen ? 'creado' : 'sin crear'), estadoTema(t.id), herr('topic', t.id, i, ts.length, pub));
    }).join('') + '</div>';
  }
  function vLecciones() {
    var nl = (S.info[R.topic] || {}).lessons || 0;
    var h = '<div class="wv-rango">' + LEC_POR_TEMA + ' lecciones por tema (según el rango)' +
      (nl < LEC_POR_TEMA ? ' · faltan ' + (LEC_POR_TEMA - nl) + ' <button class="wv-btn suave mini" type="button" data-acc="nuevo:lesson">+ Nueva lección</button>' : '') +
      (nl > LEC_POR_TEMA ? ' · hay ' + (nl - LEC_POR_TEMA) + ' de más' : '') + '</div><div id="wv-lec-lista" class="wv-carps"><div class="wv-vacio">Cargando…</div></div>';
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
    ids.forEach(function (id) { m[id] = { v: 0, p: 0, i: 0, c: 0, f: 0 }; });
    r.data.forEach(function (s) {
      var x = m[s.lesson_id];
      if (s.step_type === 'video' && s.stream_uid) x.v = 1;
      if (s.step_type === 'pdf' && s.r2_key) x.p = 1;
      if (s.step_type === 'interactive_activity' && s.content && Object.keys(s.content).length) x.i = 1;
      if (s.step_type === 'complementary_activity' && s.content && s.content.files && s.content.files.length) x.c = 1;
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
      var h = r.data.map(function (l, i) {
        var e = est[l.id], n = e.v + e.p + e.i + e.f;
        var estado = n === 4 ? 'ok' : (n === 0 && !e.c) ? 'vacia' : 'falta';
        return carpeta('lesson', l.id, l.title, n + ' de 4 partes' + (e.c ? ' · con complementarios' : ''), estado, herr('lesson', l.id, i, r.data.length));
      }).join('');
      var examen = (S.info[R.topic] || {}).tiene_examen, borrador = examen && !(S.info[R.topic] || {}).examen_publicado;
      h += '<div class="wv-carp examen"><div class="wv-carp-b static"><span class="wv-carp-ico">📝</span><span class="wv-carp-t"><b>Examen del tema</b>' +
        '<small>' + (borrador ? 'Borrador: los alumnos todavía no lo ven. Revisalo y publicalo. Cada intento sortea 8 preguntas del banco.' : 'Se arma acá mismo o con IA. Cada intento sortea 8 preguntas distintas del banco, con preguntas de opción múltiple, verdadero/falso o abiertas') + '</small></span>' + etiqueta(examen ? 'ok' : 'vacia') +
        (borrador ? boton('examen-pub', 'Publicar examen', '') : '') + (!examen ? boton('examen-ia', 'Armar con IA', 'suave') : '') +
        boton('examen', examen ? 'Editar examen' : 'Armar examen', examen ? 'suave' : '') + (examen ? boton('examen-del', 'Quitar examen', 'peligro') : '') + '</div></div>';
      cont.innerHTML = r.data.length ? h : '<div class="wv-vacio">Este tema todavía no tiene lecciones.</div>' + h;
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
      var q = await sb.from('questions').select('id', { count: 'exact', head: true }).eq('lesson_step_id', pasos.final_activity.id);
      var bd = await sb.from('lesson_drafts').select('status, paso, revision, revision_inicial, updated_at').eq('lesson_id', R.lesson).maybeSingle();
      L = { pasos: pasos, preguntas: q.count || 0, recTmp: {}, recN: {}, borrador: bd.error ? null : bd.data };
      pintarLeccion();
    } catch (e) {
      console.error(e);
      document.getElementById('wv-les').innerHTML = 'No pudimos cargar la lección.<br><small>' + esc(e.message || e) + '</small>';
    }
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
      var nom = esYt(x.uid) ? 'Video de YouTube incrustado' : (x.nombre || x.uid.split('/').pop().replace(/^[a-z0-9]{8}-/, ''));
      clase += fila('🎬', vids.length > 1 ? 'Video ' + (i + 1) + ' de ' + vids.length : 'Video de la clase', esc(nom),
        boton('video-ver:' + i, 'Ver') +
        (vids.length > 1 ? '<button type="button" class="wv-ico" title="Subir" data-acc="video-mov:' + i + ':-1"' + (i === 0 ? ' disabled' : '') + '>▲</button><button type="button" class="wv-ico" title="Bajar" data-acc="video-mov:' + i + ':1"' + (i === vids.length - 1 ? ' disabled' : '') + '>▼</button>' : '') +
        (esYt(x.uid) ? boton('video-introdef:' + i, '⭐ Usar como intro', 'suave') : '') +
        boton('video-del:' + i, 'Quitar', 'peligro')) + recorteHtml(x, i);
    });
    if (S.introWave && !(vids[0] && vids[0].uid === S.introWave.uid)) {
      clase += fila('⭐', 'Intro de Wave', 'Se agrega al principio de la clase, antes de los demás videos', boton('video-intro', 'Agregar intro', ''), 'wv-i-introwave');
    }
    clase += fila(tieneV ? '➕' : '🎬', tieneV ? 'Agregar otro video' : 'Video de la clase', tieneV ? 'El alumno los ve en orden, uno después del otro' : 'Sin video',
      boton('video-up', 'Subir video', tieneV ? 'suave' : '') + boton('video-yt', 'Enlace de YouTube', 'suave'), 'wv-i-video') +
      fila('📄', 'PDF descargable', tieneP ? esc(pdfNom) : 'Sin PDF', (tieneP ? boton('pdf-get', 'Ver') : '') + boton('pdf-up', tieneP ? 'Reemplazar' : 'Subir PDF', tieneP ? 'suave' : '') + (tieneP ? boton('pdf-del', 'Quitar', 'peligro') : ''), 'wv-i-pdf');
    var cE = tieneV && tieneP ? 'ok' : (tieneV || tieneP) ? 'falta' : 'vacia';
    h += casillero(1, '🎬', 'Clase explicativa', 'Video + PDF de la clase', cE, clase);

    // 2 · Interactiva
    var ct = p.interactive_activity.content || {};
    var tieneI = Object.keys(ct).length > 0;
    var iTxt = !tieneI ? 'Sin actividad' : ct.kind === 'html' ? 'Código HTML cargado (' + kb((ct.html || '').length) + ')' : 'Actividad de prueba (quiz de ejemplo)';
    var inter = fila('🧩', 'Actividad interactiva', iTxt,
      (ct.kind === 'html' ? boton('html-ver', 'Probar') : '') + boton('html-up', tieneI ? 'Reemplazar .html' : 'Subir .html', tieneI ? 'suave' : '') + (tieneI ? boton('html-del', 'Quitar', 'peligro') : ''), 'wv-i-html') +
      '<details class="wv-pegar"><summary>O pegá el código acá</summary><textarea id="wv-html-txt" rows="7" placeholder="Pegá el código HTML completo de la actividad"></textarea>' + boton('html-save', 'Guardar código', '') + '</details>';
    h += casillero(2, '🧩', 'Actividad interactiva', 'Archivo .html que se usa tal cual', tieneI ? 'ok' : 'vacia', inter);

    // 3 · Descargables
    var fs = (p.complementary_activity.content || {}).files || [];
    var desc = fs.length ? fs.map(function (f, i) {
      return '<div class="wv-item"><span class="wv-item-ico">📎</span><div class="wv-item-t"><b>' + esc(f.name) + '</b><small>' + kb(f.size || 0) + '</small></div><div class="wv-item-b">' +
        '<button type="button" class="wv-ico" data-acc="desc-mov:' + i + ':-1"' + (i === 0 ? ' disabled' : '') + '>▲</button>' +
        '<button type="button" class="wv-ico" data-acc="desc-mov:' + i + ':1"' + (i === fs.length - 1 ? ' disabled' : '') + '>▼</button>' +
        boton('desc-get:' + i, 'Ver') + boton('desc-del:' + i, 'Quitar', 'peligro') + '</div></div>';
    }).join('') : '<div class="wv-item"><span class="wv-item-ico">📎</span><div class="wv-item-t"><b>Sin archivos</b><small>Podés subir uno o más</small></div></div>';
    desc += '<div class="wv-pie-cas">' + boton('desc-up', '+ Subir archivos', fs.length ? 'suave' : '') + '<small id="wv-i-desc"></small></div>';
    h += casillero(3, '📎', 'Actividades descargables', 'Opcional · archivos extra para practicar (uno o más)', fs.length ? 'ok' : 'vacia', desc);

    // 4 · Consigna
    var cons = fila('✏️', 'Actividad por consigna', L.preguntas ? L.preguntas + (L.preguntas === 1 ? ' consigna armada' : ' consignas armadas') : 'Sin consignas',
      boton('consignas', L.preguntas ? 'Editar consignas' : 'Armar consignas', L.preguntas ? 'suave' : '') + (L.preguntas ? boton('consignas-del', 'Quitar todas', 'peligro') : ''));
    h += casillero(4, '✏️', 'Actividad por consigna', 'Se arma dentro de la plataforma; la corrige la IA', L.preguntas ? 'ok' : 'vacia', cons);
    h += casillero(5, '🔁', 'Repaso obligatorio', 'Automático · no hay que cargar nada', 'ok',
      '<div class="wv-item"><span class="wv-item-ico">🤖</span><div class="wv-item-t"><b>Lo arma la IA para cada alumno</b><small>6 preguntas distintas cada vez: 1 de esta lección y 5 de lecciones anteriores de la materia, priorizando las que ese alumno tiene más flojas. Sin preguntas abiertas. Usa el texto de los PDF, así que las lecciones sin PDF no entran. La primera lección de la materia no tiene repaso.</small></div></div>');

    var tit = nombre('lesson', R.lesson);
    var cont = document.getElementById('wv-les');
    if (!cont) return;
    cont.className = '';
    cont.innerHTML = '<div class="wv-lec-cab"><h2>' + esc(tit) + '</h2>' + botonCorrecciones() + '</div>' + aviso + '<div class="wv-cass">' + h + '</div>';
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
      msg('wv-i-video', 'Preparando subida…');
      var d = await subidas({ action: 'r2_upload_url', lesson_id: R.lesson, filename: f.name });
      await enviar(d.url, 'PUT', f, function (p) { msg('wv-i-video', 'Subiendo… ' + p + '%'); });
      d.uid = d.key;
      await guardarVideos(videosDe(L.pasos.video).concat([{ uid: d.uid, nombre: f.name, tramos: [] }]));
      toast('Video subido');
      await refrescarEstados(); await abrirLeccion();
    } catch (e) { toast(e.message, true); pintarLeccion(); }
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
      if (a === 'video-introdef') {
        var xi = videosDe(L.pasos.video)[+p[1]];
        if (!xi || !esYt(xi.uid)) return;
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
        if (lw[0] && lw[0].uid === S.introWave.uid) return toast('Esta lección ya empieza con la intro.');
        lw.unshift({ uid: S.introWave.uid, nombre: 'Intro de Wave', tramos: S.introWave.tramos || [] });
        L.recTmp = {}; L.recN = {};
        await guardarVideos(lw);
        toast('Intro agregada al principio');
        await refrescarEstados(); return abrirLeccion();
      }
      if (a === 'video-editar') {
        var ve = +p[1], xe = videosDe(L.pasos.video)[ve];
        if (!xe) return;
        var guardarEd = async function (tr) {
          var le = videosDe(L.pasos.video);
          if (!le[ve]) return;
          le[ve].tramos = tr; L.recN[ve] = 0; L.recTmp[ve] = null;
          await guardarVideos(le);
          toast(tr.length ? 'Recorte guardado' : 'Se muestra el video entero');
          pintarLeccion();
        };
        if (esYt(xe.uid)) return WaveEditor.abrir({ titulo: nombre('lesson', R.lesson), youtube: xe.uid.slice(3), tramos: xe.tramos, guardar: guardarEd });
        var ste = await subidas({ action: 'stream_status', uid: xe.uid });
        if (!ste.ready) return toast('No se encontró el archivo del video.', true);
        return WaveEditor.abrir({ titulo: nombre('lesson', R.lesson), tramos: xe.tramos, guardar: guardarEd,
          url: async function () { return (await subidas({ action: 'stream_token', uid: xe.uid })).url; } });
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
      if (a === 'video-up') return elegirArchivo('video/*', false, function (fs) { subirVideo(fs[0]); });
      if (a === 'video-del') {
        var ld = videosDe(L.pasos.video), xd = ld[+p[1]];
        if (!xd || !confirm(ld.length > 1 ? '¿Quitar el video ' + (+p[1] + 1) + ' de esta lección?' : '¿Quitar el video de esta lección?')) return;
        ld.splice(+p[1], 1);
        L.recTmp = {}; L.recN = {};
        await guardarVideos(ld);
        if (!esYt(xd.uid)) { try { await subidas({ action: 'stream_delete', uid: xd.uid }); } catch (e) { /* huérfano */ } }
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
    if (n >= LEC_POR_TEMA) return toast('Este tema ya tiene sus ' + LEC_POR_TEMA + ' lecciones', true);
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

  // ---------- Editor de preguntas (consignas de la lección y examen del tema) ----------
  var ED = null;
  var TIPOS_PREG = { open: 'Respuesta abierta', short_answer: 'Respuesta corta', multiple_choice: 'Opción múltiple', true_false: 'Verdadero / Falso' };
  // Tipos que arma la máquina: se editan el enunciado, la respuesta y los criterios; la estructura (opciones, pares, tabla) se ve y edita como texto.
  var TIPOS_MAQ = { fill_blank: 'Completar espacios', ordering: 'Ordenar pasos', matching: 'Unir columnas', classify: 'Clasificar', table_fill: 'Completar tabla', multi_select: 'Selección múltiple', solve_complete: 'Resolver y completar', odd_one_out: 'Encontrar el intruso' };
  function nombreTipo(t) { return TIPOS_PREG[t] || TIPOS_MAQ[t] || t; }

  function pregVacia(tipo) {
    return {
      id: null, type: tipo, prompt: '', points: 1, correct: -1, ref: '', expl: '', rubric: '',
      options: tipo === 'multiple_choice' ? ['', '', ''] : tipo === 'true_false' ? ['Verdadero', 'Falso'] : []
    };
  }

  async function abrirEditor(ctx) {
    var col = ctx.kind === 'exam' ? 'exam_id' : 'lesson_step_id';
    var id = ctx.kind === 'exam' ? (ctx.exam && ctx.exam.id) : ctx.stepId;
    var qs = [];
    if (id) {
      var r = await sb.from('questions').select('id, question_type, prompt, options, points, position').eq(col, id).order('position');
      if (r.error) throw r.error;
      var ids = r.data.map(function (x) { return x.id; });
      var rb = ids.length ? await sb.from('question_rubrics').select('question_id, reference_answer, explanation, rubric').in('question_id', ids) : { data: [] };
      if (rb.error) throw rb.error;
      var mapa = {};
      rb.data.forEach(function (x) { mapa[x.question_id] = x; });
      qs = r.data.map(function (q) {
        var u = mapa[q.id] || {};
        var ref = typeof u.reference_answer === 'string' ? u.reference_answer : '';
        var o = Array.isArray(q.options) ? q.options.map(String) : [];
        var cerrada = q.question_type === 'multiple_choice' || q.question_type === 'true_false';
        var maq = !!TIPOS_MAQ[q.question_type];
        return { id: q.id, type: q.question_type, prompt: q.prompt, points: q.points, options: o,
          correct: cerrada ? o.indexOf(ref) : -1, ref: cerrada ? '' : ref, expl: u.explanation || '', rubric: u.rubric || '',
          maq: maq, estructura: maq && q.options != null ? JSON.stringify(q.options, null, 1) : '' };
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
    if (!cerrada) {
      h += '<label class="wv-lbl-e">Respuesta de referencia (opcional, la usa la IA para corregir)</label>' +
        '<textarea rows="2" data-q="' + i + '" data-f="ref">' + esc(q.ref) + '</textarea>';
    }
    h += '<details class="wv-pegar"><summary>Criterios y explicación (opcional)</summary>' +
      '<label class="wv-lbl-e">Criterios de corrección para la IA</label><textarea rows="2" data-q="' + i + '" data-f="rubric">' + esc(q.rubric) + '</textarea>' +
      '<label class="wv-lbl-e">Explicación de la respuesta</label><textarea rows="2" data-q="' + i + '" data-f="expl">' + esc(q.expl) + '</textarea></details></div>';
    return h;
  }

  function pintarEditor() {
    var c = ED.ctx, exam = c.kind === 'exam';
    var h = '<h2>' + (exam ? 'Examen del tema' : 'Actividad por consigna') + '</h2><p>' + esc(c.sub) + '</p>';
    if (exam) h += '<label class="wv-puntos wv-pasa">Nota mínima para aprobar <input type="number" min="0" max="100" data-ed="pasa" value="' + ED.pasa + '"></label>';
    h += ED.qs.map(function (q, i) { return cardPreg(q, i, ED.qs.length); }).join('') ||
      '<div class="wv-vacio">Todavía no hay preguntas. Agregá la primera.</div>';
    h += '<div class="wv-ed-nuevo"><b>Agregar:</b> ' + Object.keys(TIPOS_PREG).map(function (k) { return boton('ed-add:' + k, '+ ' + TIPOS_PREG[k], 'suave'); }).join('') + '</div>';
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
        var fila = { question_type: x.type, prompt: x.prompt.trim(), options: opts.length ? opts : null, points: x.points, position: k + 1 };
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
        var rb = await sb.from('question_rubrics').upsert({ question_id: x.id, reference_answer: ref || null, explanation: x.expl.trim() || null, rubric: x.rubric.trim() || null }, { onConflict: 'question_id' });
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
    }
    pintar();
  }

  // Solo para pruebas visuales de la pantalla de una lección con datos de ejemplo
  function _probar(el, pasos) { vista = el; L = { pasos: pasos, preguntas: 0, recTmp: {}, recN: {} }; el.innerHTML = '<div id="wv-les"></div>'; el.onclick = function (ev) { var b = ev.target.closest('[data-acc]'); if (b && !b.disabled) accion(b.getAttribute('data-acc')); }; pintarLeccion(); }

  window.WaveContenido = { abrir: abrir, _probar: _probar };
})();
