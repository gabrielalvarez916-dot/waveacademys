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
      todo(function () { return sb.from('topics').select('id, subject_id, title, position').order('position').order('id'); }),
      todo(function () { return sb.from('subject_load_config').select('subject_id, tier, hours_total, topics_total').order('subject_id'); }),
      sb.from('load_tiers').select('tier, label')
    ]);
    if (res[0].error) throw res[0].error;
    if (res[1].error) throw res[1].error;
    if (res[5].error) throw res[5].error;
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
  function herr(tipo, id, i, n) {
    return '<span class="wv-herr">' +
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
    return h + '<div class="wv-carps">' + ts.map(function (t, i) {
      var f = S.info[t.id] || {};
      return carpeta('topic', t.id, t.title, (f.lessons || 0) + ' lecciones · examen ' + (f.tiene_examen ? 'creado' : 'sin crear'), estadoTema(t.id), herr('topic', t.id, i, ts.length));
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
      var examen = (S.info[R.topic] || {}).tiene_examen;
      h += '<div class="wv-carp examen"><div class="wv-carp-b static"><span class="wv-carp-ico">📝</span><span class="wv-carp-t"><b>Examen del tema</b>' +
        '<small>Se arma acá mismo, con preguntas de opción múltiple, verdadero/falso o abiertas</small></span>' + etiqueta(examen ? 'ok' : 'vacia') + boton('examen', examen ? 'Editar examen' : 'Armar examen', examen ? 'suave' : '') + (examen ? boton('examen-del', 'Quitar examen', 'peligro') : '') + '</div></div>';
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
      L = { pasos: pasos, preguntas: q.count || 0, video: null };
      if (pasos.video.stream_uid) {
        try { L.video = await subidas({ action: 'stream_status', uid: pasos.video.stream_uid }); } catch (e) { L.video = null; }
      }
      pintarLeccion();
    } catch (e) {
      console.error(e);
      document.getElementById('wv-les').innerHTML = 'No pudimos cargar la lección.<br><small>' + esc(e.message || e) + '</small>';
    }
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
    var v = p.video, tieneV = !!v.stream_uid;
    var vEst = !tieneV ? 'Sin video' : (L.video && L.video.ready ? 'Video listo' : 'Procesando… (puede tardar unos minutos)');
    var pdf = p.pdf, tieneP = !!pdf.r2_key;
    var pdfNom = tieneP ? (pdf.title || pdf.r2_key.split('/').pop().replace(/^[a-z0-9]{8}-/, '')) : '';
    var clase = fila('🎬', 'Video de la clase', vEst, (tieneV ? boton('video-ver', 'Ver') : '') + boton('video-up', tieneV ? 'Reemplazar' : 'Subir video', tieneV ? 'suave' : '') + (tieneV ? boton('video-del', 'Quitar', 'peligro') : ''), 'wv-i-video') +
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

    var tit = nombre('lesson', R.lesson);
    var cont = document.getElementById('wv-les');
    if (!cont) return;
    cont.className = '';
    cont.innerHTML = '<div class="wv-lec-cab"><h2>' + esc(tit) + '</h2></div>' + aviso + '<div class="wv-cass">' + h + '</div>';
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
      var d = await subidas({ action: 'stream_upload_url', name: nombre('lesson', R.lesson) });
      var fd = new FormData(); fd.append('file', f);
      await enviar(d.upload_url, 'POST', fd, function (p) { msg('wv-i-video', 'Subiendo… ' + p + '%'); });
      var viejo = L.pasos.video.stream_uid;
      await guardarPaso('video', { stream_uid: d.uid });
      if (viejo) { try { await subidas({ action: 'stream_delete', uid: viejo }); } catch (e) { /* queda huérfano */ } }
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
      if (a === 'video-ver') {
        var uidv = L.pasos.video.stream_uid;
        var stv = await subidas({ action: 'stream_status', uid: uidv });
        if (!stv.ready) return toast('El video todavía se está procesando. Probá en unos minutos.', true);
        return WaveVisor.abrirVideo({
          titulo: nombre('lesson', R.lesson),
          token: async function () { return (await subidas({ action: 'stream_token', uid: uidv })).token; }
        });
      }
      if (a === 'intro-up') return elegirArchivo('video/*', false, function (fs) { subirIntro(fs[0]); });
      if (a === 'intro-ver') {
        var sj0 = S.subjects.filter(function (x) { return x.id === R.subject; })[0];
        var sti = await subidas({ action: 'stream_status', uid: sj0.intro_video_uid });
        if (!sti.ready) return toast('El video todavía se está procesando. Probá en unos minutos.', true);
        return WaveVisor.abrirVideo({
          titulo: 'Introducción · ' + nombre('subject', R.subject),
          token: async function () { return (await subidas({ action: 'stream_token', uid: sj0.intro_video_uid })).token; }
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
        if (!confirm('¿Quitar el video de esta lección?')) return;
        var uid = L.pasos.video.stream_uid;
        await guardarPaso('video', { stream_uid: null });
        try { await subidas({ action: 'stream_delete', uid: uid }); } catch (e) { /* huérfano */ }
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
      if (a === 'del') return eliminar(p[1], p[2]);
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
    } catch (e) { console.error(e); toast((e && e.message) || 'No se pudo completar', true); }
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
    var t = await sb.from('topics').insert(filas).select('id, subject_id, title, position');
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
      var d = await subidas({ action: 'stream_upload_url', name: 'Introducción · ' + nombre('subject', R.subject) });
      var fd = new FormData(); fd.append('file', f);
      await enviar(d.upload_url, 'POST', fd, function (p) { msg('wv-i-intro', 'Subiendo… ' + p + '%'); });
      var viejo = sj.intro_video_uid;
      var u = await sb.from('subjects').update({ intro_video_uid: d.uid }).eq('id', R.subject);
      if (u.error) throw u.error;
      sj.intro_video_uid = d.uid;
      if (viejo) { try { await subidas({ action: 'stream_delete', uid: viejo }); } catch (e) { /* huérfano */ } }
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
      if (st.stream_uid) { try { await subidas({ action: 'stream_delete', uid: st.stream_uid }); } catch (e) { /* queda huérfano */ } }
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
        return { id: q.id, type: q.question_type, prompt: q.prompt, points: q.points, options: o,
          correct: cerrada ? o.indexOf(ref) : -1, ref: cerrada ? '' : ref, expl: u.explanation || '', rubric: u.rubric || '' };
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
    var h = '<div class="wv-preg"><div class="wv-preg-cab"><b>' + (i + 1) + '.</b><span class="wv-etq vacia">' + TIPOS_PREG[q.type] + '</span>' +
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

  window.WaveContenido = { abrir: abrir };
})();
