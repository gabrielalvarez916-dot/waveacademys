// Pantalla de materia del alumno, estilo Simply Piano:
// Introducción + un rectángulo por tema, con las lecciones en círculos. Cada círculo abre sus recuadros de archivos.
(function () {
  var sb = Wave.sb;
  var vista = null;
  var D = null;          // datos de la materia abierta
  var hojaAbierta = null; // id de la lección que se está viendo

  var CLAVES = ['video', 'pdf', 'interactive', 'final'];
  // El repaso obligatorio no es un paso cargado: lo arma la IA. Cuenta para completar la lección cuando corresponde.
  var TIPO_PASO = { video: 'video', pdf: 'pdf', interactive_activity: 'interactive', complementary_activity: 'complementary', final_activity: 'final' };

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function colorSeguro(c) { return /^#[0-9a-fA-F]{6}$/.test(c || '') ? c : '#087E83'; }

  // ---------- Íconos ----------
  var IC = {
    play: '<path d="M8 5.5v13l11-6.5z" fill="currentColor" stroke="none"/>',
    doc: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    puzzle: '<path d="M10 3a2 2 0 0 1 4 0v1h4a1 1 0 0 1 1 1v4h-1a2 2 0 0 0 0 4h1v4a1 1 0 0 1-1 1h-4v-1a2 2 0 0 0-4 0v1H6a1 1 0 0 1-1-1v-4h1a2 2 0 0 0 0-4H5V5a1 1 0 0 1 1-1h4z"/>',
    pencil: '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    clip: '<path d="M21 12.5l-8.6 8.6a5 5 0 0 1-7.1-7.1l9.2-9.2a3.3 3.3 0 0 1 4.7 4.7l-9.2 9.2a1.7 1.7 0 0 1-2.4-2.4l8.5-8.5"/>',
    lock: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    trophy: '<path d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H5a2 2 0 0 0 2 4M16 6h3a2 2 0 0 1-2 4M12 13v4M8 20h8M10 17h4v3h-4z"/>',
    star: '<path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z" fill="currentColor"/>',
    chevron: '<path d="M9 6l6 6-6 6"/>',
    back: '<path d="M15 6l-6 6 6 6"/>',
    close: '<path d="M6 6l12 12M18 6L6 18"/>',
    down: '<path d="M12 4v11m0 0l-4-4m4 4l4-4M5 20h14"/>',
    dots: '<path d="M6 12h.01M12 12h.01M18 12h.01"/>',
    bolt: '<path d="M13 2L4 14h7l-1 8 9-12h-7z" fill="currentColor" stroke="none"/>',
    repaso: '<path d="M4 12a8 8 0 0 1 13.7-5.6L20 9"/><path d="M20 4v5h-5"/><path d="M20 12a8 8 0 0 1-13.7 5.6L4 15"/><path d="M4 20v-5h5"/>'
  };
  function ico(k, px, grosor) {
    return '<svg viewBox="0 0 24 24" width="' + (px || 24) + '" height="' + (px || 24) + '" fill="none" stroke="currentColor" stroke-width="' + (grosor || 2.4) +
      '" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + IC[k] + '</svg>';
  }

  function toast(texto, error) {
    var t = document.createElement('div');
    t.className = 'mt-toast' + (error ? ' error' : '');
    t.textContent = texto;
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, 3600);
  }

  async function llamar(nombre, body) {
    var r = await sb.functions.invoke(nombre, { body: body });
    if (r.error) {
      var msg = 'No se pudo completar. Probá de nuevo en un momento.';
      try { var c = await r.error.context.json(); if (c && c.error) msg = c.error; } catch (e) { /* genérico */ }
      throw new Error(msg);
    }
    if (r.data && r.data.error) throw new Error(r.data.error);
    return r.data;
  }

  // ---------- Datos ----------
  async function cargar(materiaId) {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;
    var est = await sb.from('students').select('id').eq('profile_id', uid).maybeSingle();
    if (est.error) throw est.error;
    if (!est.data) throw new Error('Esta cuenta no es de un estudiante.');
    var sid = est.data.id;

    var mat = await sb.from('subjects').select('id, name, color, intro_video_uid').eq('id', materiaId).maybeSingle();
    if (mat.error) throw mat.error;
    if (!mat.data) throw new Error('No encontramos esta materia.');
    var iw = await sb.from('app_settings').select('value').eq('key', 'intro_wave').maybeSingle();
    var introWave = iw.data && iw.data.value && iw.data.value.uid ? iw.data.value : null;

    var tem = await sb.from('topics').select('id, title, position, lessons(id, title, position)').eq('subject_id', materiaId).order('position');
    if (tem.error) throw tem.error;
    var temas = tem.data.map(function (t) {
      return { id: t.id, titulo: t.title, posicion: t.position,
        lecciones: (t.lessons || []).slice().sort(function (a, b) { return a.position - b.position; })
          .map(function (l) { return { id: l.id, titulo: l.title, tema: t.id }; }) };
    }).sort(function (a, b) { return a.posicion - b.posicion; });

    var pasos = await sb.from('lesson_steps')
      .select('id, lesson_id, step_type, title, stream_uid, r2_key, kind:content->>kind, files:content->files, carpeta:content->carpeta, inicio:content->inicio, fin:content->fin, tramos:content->tramos, videos:content->videos, clase:content->clase, lessons!inner(topics!inner(subject_id))')
      .eq('lessons.topics.subject_id', materiaId);
    if (pasos.error) throw pasos.error;

    var finIds = pasos.data.filter(function (p) { return p.step_type === 'final_activity'; }).map(function (p) { return p.id; });
    var qs = finIds.length ? await sb.from('questions').select('lesson_step_id').in('lesson_step_id', finIds) : { data: [] };
    if (qs.error) throw qs.error;
    var conPreg = {};
    qs.data.forEach(function (q) { conPreg[q.lesson_step_id] = true; });

    var topIds = temas.map(function (t) { return t.id; });
    var exs = topIds.length ? await sb.from('exams').select('id, topic_id, passing_score').in('topic_id', topIds) : { data: [] };
    if (exs.error) throw exs.error;
    var exIds = exs.data.map(function (e) { return e.id; });
    var exq = exIds.length ? await sb.from('questions').select('exam_id').in('exam_id', exIds) : { data: [] };
    if (exq.error) throw exq.error;
    var exConPreg = {};
    exq.data.forEach(function (q) { exConPreg[q.exam_id] = true; });

    var prog = await sb.from('student_step_progress').select('lesson_step_id, score, grading_status').eq('student_id', sid);
    if (prog.error) throw prog.error;
    var lp = await sb.from('student_lesson_progress').select('lesson_id').eq('student_id', sid);
    if (lp.error) throw lp.error;
    var ints = exIds.length ? await sb.from('exam_attempts').select('exam_id, passed, score, grading_status').eq('student_id', sid).in('exam_id', exIds) : { data: [] };
    if (ints.error) throw ints.error;

    var porLeccion = {};
    pasos.data.forEach(function (p) {
      var k = TIPO_PASO[p.step_type];
      if (!k) return;
      var tiene = k === 'video' ? (!!p.stream_uid || p.clase === true)
        : k === 'pdf' ? !!p.r2_key
        : k === 'interactive' ? p.kind === 'html'
        : k === 'complementary' ? (Array.isArray(p.files) && p.files.length > 0)
        : !!conPreg[p.id];
      (porLeccion[p.lesson_id] = porLeccion[p.lesson_id] || {})[k] = {
        id: p.id, lesson_id: p.lesson_id, step_type: p.step_type, titulo: p.title, tiene: tiene, clase: k === 'video' && p.clase === true,
        videos: k !== 'video' || !p.stream_uid ? [] : (Array.isArray(p.videos) && p.videos.length ? p.videos
          : [{ uid: p.stream_uid, tramos: p.tramos || (p.inicio || p.fin ? [{ i: p.inicio || 0, f: p.fin || 0 }] : []) }]),
        files: k === 'complementary' && Array.isArray(p.files) ? p.files : [],
        carpeta: k === 'pdf' && Array.isArray(p.carpeta) ? p.carpeta : []
      };
    });

    var progreso = {};
    prog.data.forEach(function (p) { progreso[p.lesson_step_id] = { score: p.score, estado: p.grading_status }; });
    var hechas = {};
    lp.data.forEach(function (l) { hechas[l.lesson_id] = true; });

    var examen = {};
    exs.data.forEach(function (e) {
      var mias = ints.data.filter(function (i) { return i.exam_id === e.id; });
      var graded = mias.filter(function (i) { return i.grading_status === 'graded' && i.score != null; });
      examen[e.topic_id] = { id: e.id, aprobar: e.passing_score, tienePreguntas: !!exConPreg[e.id],
        aprobado: mias.some(function (i) { return i.passed; }),
        mejor: graded.length ? Math.max.apply(null, graded.map(function (i) { return Number(i.score); })) : null };
    });

    // Repaso obligatorio: en qué lecciones corresponde y cuáles ya hizo
    var rep = await sb.rpc('my_review_status', { p_subject: materiaId });
    var repaso = {};
    (rep.error ? [] : rep.data || []).forEach(function (r) { repaso[r.lesson_id] = { req: !!r.required, done: !!r.done, score: r.last_score }; });
    Object.keys(porLeccion).forEach(function (lid) {
      var p = porLeccion[lid];
      var conContenido = CLAVES.some(function (k) { return p[k] && p[k].tiene; });
      p.review = { id: 'repaso:' + lid, lesson_id: lid, step_type: 'review', titulo: 'Repaso', tiene: conContenido && !!(repaso[lid] && repaso[lid].req), files: [] };
    });

    // Carpeta ya entregada (el alumno carga sus respuestas y la app las corrige sin IA)
    var pdfIds = [];
    Object.keys(porLeccion).forEach(function (lid) { var pp = porLeccion[lid].pdf; if (pp && pp.tiene && pp.carpeta.length) pdfIds.push(pp.id); });
    var carpeta = {};
    if (pdfIds.length) {
      var ce = await sb.rpc('carpeta_estado', { p_steps: pdfIds });
      (ce.error ? [] : ce.data || []).forEach(function (c) { if (c.entregada) carpeta[c.lesson_step_id] = true; });
    }

    var acc = await sb.rpc('my_content_access');
    var susOk = !acc.error && acc.data === true;

    return {
      sid: sid, introWave: introWave, materia: mat.data, temas: temas, pasos: porLeccion, carpeta: carpeta, progreso: progreso, repaso: repaso, hechas: hechas, examen: examen,
      sinAcceso: !susOk || (temas.some(function (t) { return t.lecciones.length; }) && !pasos.data.length)
    };
  }

  // ---------- Estados ----------
  function hecho(p) {
    if (p.step_type === 'review') return !!(D.repaso && D.repaso[p.lesson_id] && D.repaso[p.lesson_id].done);
    var pr = D.progreso[p.id];
    if (!pr) return false;
    return p.step_type === 'final_activity' ? pr.estado === 'graded' : true;
  }

  // Un nivel = PDF, entrega de la carpeta y actividades (las "generales" son solo actividades)
  function pasosNivel(l) {
    var p = D.pasos[l.id] || {}, r = [];
    if (p.video && p.video.tiene) r.push('video');
    if (p.pdf && p.pdf.tiene) r.push('pdf');
    if (p.pdf && p.pdf.tiene && p.pdf.carpeta.length) r.push('carpeta');
    if (p.final && p.final.tiene) r.push('final');
    return r;
  }
  function hechoK(l, k) {
    var p = D.pasos[l.id] || {};
    if (k === 'carpeta') return !!(p.pdf && D.carpeta[p.pdf.id]);
    return !!(p[k] && hecho(p[k]));
  }
  function estadoLeccion(l) {
    var req = pasosNivel(l);
    var hs = req.filter(function (k) { return hechoK(l, k); }).length;
    return { total: req.length, hechos: hs, vacia: req.length === 0, completa: req.length > 0 && hs === req.length,
      frac: req.length ? hs / req.length : 0, req: req };
  }

  function calcular() {
    var previoOk = true, actual = null;
    D.temas.forEach(function (t) {
      t.bloqueado = !previoOk || D.sinAcceso;
      var ok = true;
      var ls = t.lecciones, conGen = ls.length >= 4;
      t.niveles = conGen ? ls.slice(0, ls.length - 1) : ls;
      t.generales = conGen ? ls[ls.length - 1] : null;
      // El video (clase animada) es el primer paso de cada nivel (ver pasosNivel)
      t.videoPaso = null;
      t.lecciones.forEach(function (l) {
        var pp = D.pasos[l.id] || {};
        if (pp.video && pp.video.tiene && !t.videoPaso) t.videoPaso = pp.video;
        l.est = estadoLeccion(l);
        if (D.sinAcceso) l.est.vacia = false;
        l.bloqueada = t.bloqueado || !ok;
        if (!l.bloqueada && !l.est.completa && !l.est.vacia && !actual) { actual = l.id; }
        if (!l.est.vacia && !l.est.completa) ok = false;
      });
      var ex = D.examen[t.id];
      t.examen = ex && ex.tienePreguntas ? ex : null;
      t.examenDisponible = !!t.examen && !t.bloqueado && ok;
      var todasVacias = t.lecciones.every(function (l) { return l.est.vacia; });
      t.vacio = !D.sinAcceso && todasVacias && !t.examen && !t.videoPaso;
      t.completo = !t.vacio && ok && t.lecciones.length > 0 && (!t.examen || t.examen.aprobado);
      if (t.examenDisponible && !t.examen.aprobado && !actual) actual = 'examen:' + t.id;
      t.hechas = t.lecciones.filter(function (l) { return l.est.completa; }).length;
      t.conContenido = t.lecciones.filter(function (l) { return !l.est.vacia; }).length;
      previoOk = previoOk && (t.vacio || t.completo);
    });
    D.actual = actual;
  }

  // ---------- Pantallas ----------
  // 1) #materia/<id>              → Introducción + un rectángulo por tema
  // 2) #materia/<id>/<tema>       → las lecciones en círculos
  // 3) #materia/<id>/<tema>/<lec> → los recuadros de archivos de la lección
  var TONOS = ['#087E83', '#7C5CE0', '#E4572E', '#D6457F', '#2F7BD9', '#E59A1B'];
  function tono(i) { return TONOS[i % TONOS.length]; }
  function base() { return '#materia/' + D.materia.id; }

  function aro(frac) {
    var r = 44, c = 2 * Math.PI * r, f = Math.max(0, Math.min(1, frac || 0));
    return '<svg class="mt-anillo" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="' + r + '" class="mt-pista"/>' +
      (f > 0 ? '<circle cx="50" cy="50" r="' + r + '" class="mt-avance" stroke-dasharray="' + (c * f).toFixed(1) + ' ' + c.toFixed(1) + '" transform="rotate(-90 50 50)"/>' : '') + '</svg>';
  }

  function banner() {
    return D.sinAcceso
      ? '<div class="mt-banner">' + ico('lock', 20, 2.6) + '<span><b>Hay un problema con la suscripción.</b> Para ver el contenido tiene que estar al día. Pedile a tu familia que revise la sección Facturación.</span></div>' : '';
  }

  // ----- Pantalla 1: temas -----
  function tarjeta(o) {
    var cls = 'mt-card' + (o.estado ? ' ' + o.estado : '');
    var interior =
      '<div class="mt-card-t"><h2>' + esc(o.titulo) + '</h2><p>' + esc(o.texto) + '</p>' +
      (o.boton ? '<span class="mt-card-btn">' + o.boton + '</span>' : '') + '</div>' +
      '<div class="mt-card-fig">' + (o.figura || '') + '</div>' +
      (o.trofeo ? '<span class="mt-trofeo">' + ico('trophy', 34, 1.8) + '</span>' : '') +
      (o.estado === 'bloq' ? '<span class="mt-cand">' + ico('lock', 26, 2.8) + '</span>' : '');
    var estilo = ' style="--k:' + o.color + '"';
    if (o.href) return '<a class="' + cls + '" href="' + o.href + '"' + estilo + '>' + interior + '</a>';
    return '<button type="button" class="' + cls + '"' + estilo + (o.aviso ? ' data-aviso="' + esc(o.aviso) + '"' : '') + (o.intro ? ' data-intro="1"' : '') + '>' + interior + '</button>';
  }

  function pantallaTemas() {
    var m = D.materia, icono = window.WaveIconos ? WaveIconos.materia(m.name) : '';
    var cards = [];
    cards.push(m.intro_video_uid
      ? tarjeta({ titulo: 'Introducción', texto: 'Conocé la materia antes de empezar', boton: 'VER VIDEO', color: colorSeguro(m.color), figura: icono, intro: true })
      : tarjeta({ titulo: 'Introducción', texto: 'El video de introducción estará disponible muy pronto', color: colorSeguro(m.color), figura: icono, estado: 'pronto' }));
    D.temas.forEach(function (t, i) {
      var c = tono(i), o = { titulo: t.titulo, color: c, figura: icono };
      var nl = t.lecciones.length;
      if (t.vacio) { o.texto = 'Estamos preparando esta misión'; o.estado = 'pronto'; }
      else if (t.bloqueado) { o.texto = nl + (nl === 1 ? ' nivel' : ' niveles') + (t.examen ? ' y nivel jefe' : ''); o.estado = 'bloq'; o.aviso = D.sinAcceso ? 'La suscripción tiene que estar al día para ver el contenido.' : 'Terminá la misión anterior y superá su nivel jefe para abrir esta.'; }
      else {
        o.texto = t.completo ? '¡Misión cumplida! ' + t.hechas + ' de ' + t.conContenido + ' niveles' + (t.examen ? ' y nivel jefe superado' : '')
          : t.hechas + ' de ' + t.conContenido + ' niveles' + (t.examen ? ' · nivel jefe al final' : '');
        o.boton = t.completo ? 'REPASAR' : t.hechas ? 'SEGUIR' : 'EMPEZAR';
        o.trofeo = t.completo; o.href = base() + '/' + t.id;
      }
      cards.push(tarjeta(o));
    });
    vista.innerHTML = '<div class="mt mt-p1" style="--c:' + colorSeguro(m.color) + '">' +
      '<div class="mt-top"><a class="mt-volver" href="#cursos">' + ico('back', 20, 3) + ' Mis cursos</a><h1>' + esc(m.name) + '</h1></div>' +
      banner() + '<div class="mt-cards">' + (D.temas.length ? cards.join('') : '<div class="mt-vacio">Esta materia todavía no tiene temas.</div>') + '</div></div>';
  }

  // ----- Pantalla 2: la misión (círculos) -----
  function discoNodo(cls, contenido, frac) {
    return '<span class="mt-aro">' + aro(cls.indexOf('hecha') >= 0 ? 1 : frac) + '<span class="mt-disco">' + contenido + '</span></span>';
  }
  function nodo(cls, interior, href, aviso, extra) {
    return href ? '<a class="mt-nodo ' + cls + '" href="' + href + '"' + (extra || '') + '>' + interior + '</a>'
      : '<button type="button" class="mt-nodo ' + cls + '"' + (extra || '') + (aviso ? ' data-aviso="' + esc(aviso) + '"' : '') + '>' + interior + '</button>';
  }

  function nodoVideo(l, i, t, esGen) {
    var cls, contenido, aviso = '', extra = '';
    if (l.videoHecho) { cls = 'hecha'; contenido = ico('check', 56, 3.2); extra = ' data-video="' + l.id + '"'; }
    else if (l.videoBloq) { cls = 'bloq'; contenido = ico('lock', 40, 2.6); aviso = D.sinAcceso ? 'La suscripción tiene que estar al día.' : t.bloqueado ? 'Terminá la misión anterior.' : 'Primero superá el nivel anterior.'; }
    else { cls = 'libre' + (D.actual === 'video:' + l.id ? ' actual' : ''); contenido = ico('play', 52, 2.4); extra = ' data-video="' + l.id + '"'; }
    var burbuja = cls.indexOf('actual') >= 0 ? '<span class="mt-burbuja">¡Empezá!</span>' : '';
    return nodo(cls, burbuja + discoNodo(cls, contenido, 0) + '<span class="mt-nombre">' + (esGen ? 'Video de las generales' : 'Video del nivel ' + (i + 1)) + '</span>', null, aviso, extra);
  }

  function nodoNivel(l, i, t, esGen) {
    var e = l.est, cls, contenido, href = null, aviso = '';
    if (D.sinAcceso) { cls = 'bloq'; contenido = ico('lock', 40, 2.6); aviso = 'La suscripción tiene que estar al día para ver el contenido.'; }
    else if (e.vacia) { cls = 'pronto'; contenido = ico('dots', 40, 3.2); aviso = 'Este nivel está en preparación.'; }
    else if (l.bloqueada) { cls = 'bloq'; contenido = ico('lock', 40, 2.6); aviso = 'Primero superá el nivel anterior.'; }
    else if (e.completa) { cls = 'hecha'; contenido = ico('check', 56, 3.2); href = base() + '/' + t.id + '/' + l.id; }
    else { cls = 'libre' + (D.actual === l.id ? ' actual' : ''); contenido = esGen ? ico('bolt', 50) : '<span class="mt-num">' + (i + 1) + '</span>'; href = base() + '/' + t.id + '/' + l.id; }
    var burbuja = D.actual === l.id ? '<span class="mt-burbuja">¡Empezá!</span>' : '';
    var nombre = esGen ? 'Las 4 generales' : 'Nivel ' + (i + 1) + ': ' + l.titulo;
    return nodo(cls, burbuja + discoNodo(cls, contenido, e.completa ? 1 : e.frac) + '<span class="mt-nombre">' + esc(nombre) + '</span>', href, aviso);
  }

  function nodoExamen(t) {
    var ex = t.examen, cls, contenido;
    if (ex.aprobado) { cls = 'hecha'; contenido = ico('trophy', 46, 1.8); }
    else if (t.examenDisponible) { cls = 'libre actual'; contenido = ico('trophy', 46, 1.8); }
    else { cls = 'bloq'; contenido = ico('lock', 34, 2.6); }
    var burbuja = t.examenDisponible && !ex.aprobado ? '<span class="mt-burbuja">¡Nivel jefe!</span>' : '';
    var data = t.examenDisponible ? ' data-examen="' + t.id + '"' : ' data-aviso="Primero superá todos los niveles de la misión."';
    return '<button type="button" class="mt-nodo examen ' + cls + '"' + data + '>' + burbuja +
      '<span class="mt-aro">' + aro(ex.aprobado ? 1 : 0) + '<span class="mt-disco">' + contenido + '</span></span>' +
      '<span class="mt-nombre">Nivel jefe' + (ex.aprobado && ex.mejor != null ? ' · ' + Math.round(ex.mejor) : '') + '</span></button>';
  }

  function nodoSiguiente(t, idx) {
    var sig = D.temas[idx + 1];
    if (!sig) return '';
    var abierto = t.completo && !sig.vacio;
    var cls = abierto ? 'libre actual' : 'bloq', contenido = ico('chevron', 52, 3.2);
    if (!abierto) contenido = ico('lock', 34, 2.6);
    var burbuja = abierto ? '<span class="mt-burbuja">¡Misión cumplida!</span>' : '';
    return nodo(cls, burbuja + discoNodo(cls, contenido, 0) + '<span class="mt-nombre">Siguiente misión</span>',
      abierto ? base() + '/' + sig.id : null, abierto ? '' : (sig.vacio ? 'La próxima misión está en preparación.' : 'Superá el nivel jefe para pasar a la siguiente misión.'));
  }

  function pantallaTema(t) {
    var idx = D.temas.indexOf(t), c = tono(idx);
    var nodos = t.niveles.map(function (l, i) { return nodoNivel(l, i, t, false); }).join('') +
      (t.generales ? nodoNivel(t.generales, 0, t, true) : '') +
      (t.examen ? nodoExamen(t) : '') + nodoSiguiente(t, idx);
    vista.innerHTML = '<div class="mt mt-p2" style="--c:' + c + '">' +
      '<div class="mt-escena"><div class="mt-escena-top"><a class="mt-volver claro" href="' + base() + '">' + ico('back', 20, 3) + ' ' + esc(D.materia.name) + '</a>' +
      '<div class="mt-escena-tit"><span>Misión ' + (idx + 1) + '</span><h1>' + esc(t.titulo) + '</h1></div></div>' +
      '<div class="mt-fila"><div class="mt-fila-int">' + nodos + '</div></div></div></div>';
    var fila = vista.querySelector('.mt-fila'), act = vista.querySelector('.mt-nodo.actual');
    if (fila && act) setTimeout(function () { fila.scrollLeft = Math.max(0, act.offsetLeft - fila.clientWidth / 2 + act.offsetWidth / 2); }, 0);
  }

  // ----- Pantalla 3: el nivel, paso por paso (como un juego: una pantalla, un botón) -----
  var PASO_UI = {
    video:   { icono: 'play',   color: '#087E83', titulo: 'Mirá la clase', sub: 'Una clase animada que te explica todo el nivel. Después vas a leer el PDF y practicar.', boton: 'VER LA CLASE' },
    pdf:     { icono: 'doc',    color: '#E4572E', titulo: 'Leé el PDF', sub: 'Con la explicación, los ejemplos y las consignas de tu carpeta. Tené la carpeta a mano.', boton: 'ABRIR EL PDF' },
    carpeta: { icono: 'pencil', color: '#7C5CE0', titulo: 'Entregá tu carpeta', sub: 'Escribí lo que te dio en cada consigna. Las soluciones aparecen cuando entregás todo bien.', boton: 'ENTREGAR RESPUESTAS' },
    final:   { icono: 'puzzle', color: '#E59A1B', titulo: 'Actividades', sub: 'Practicá lo que aprendiste en este nivel.', boton: 'EMPEZAR' }
  };

  function buscarLeccion(id) {
    for (var i = 0; i < D.temas.length; i++) for (var j = 0; j < D.temas[i].lecciones.length; j++) {
      if (D.temas[i].lecciones[j].id === id) return { l: D.temas[i].lecciones[j], t: D.temas[i], n: j + 1 };
    }
    return null;
  }

  function consigna(x) { return typeof x === 'string' ? x : (x && (x.consigna || x.texto)) || ''; }

  function pantallaPaso(k, f, esGen, n, total) {
    var u = PASO_UI[k], l = f.l, p = D.pasos[l.id] || {};
    var titulo = u.titulo, sub = u.sub, icono = u.icono;
    if (k === 'final' && esGen) { titulo = 'Las 4 generales'; sub = 'Mezclan todo lo de la misión y repasan lo anterior.'; icono = 'bolt'; }
    var extra = '';
    if (k === 'carpeta') {
      extra = '<div class="rc-items">' + p.pdf.carpeta.map(function (x, i) {
        return '<label class="rc-item"><span class="mt-preg-n">' + (i + 1) + '</span><span class="rc-item-c"><span class="rc-consigna">' + esc(consigna(x)) +
          '</span><input type="text" class="rc-in" data-i="' + i + '" maxlength="120" autocomplete="off" placeholder="Tu respuesta"></span></label>';
      }).join('') + '</div>';
    }
    return '<div class="rc-cuerpo"><span class="rc-disco" style="--k:' + u.color + '">' + ico(icono, 56, 2.2) + '</span>' +
      '<small class="rc-kick">PASO ' + n + ' DE ' + total + '</small><h1>' + esc(titulo) + '</h1><p class="rc-sub">' + esc(sub) + '</p>' + extra +
      '<div class="rc-pie"><button type="button" class="rc-btn" style="--k:' + u.color + '" data-rc="' + (k === 'carpeta' ? 'entregar' : 'abrir') + '" data-k="' + k + '">' + u.boton + '</button></div></div>';
  }

  function pantallaFin(f, esGen) {
    var t = f.t, l = f.l, sig = null, boton;
    if (esGen) boton = '<a class="rc-btn amber" href="' + base() + '/' + t.id + '">' + (t.examen ? 'IR AL NIVEL JEFE' : 'VOLVER A LA MISIÓN') + '</a>';
    else {
      var pos = t.niveles.indexOf(l), prox = t.niveles[pos + 1] || t.generales;
      boton = prox && !prox.est.vacia
        ? '<a class="rc-btn amber" href="' + base() + '/' + t.id + '/' + prox.id + '">' + (t.niveles[pos + 1] ? 'SEGUIR AL NIVEL ' + (pos + 2) : 'IR A LAS GENERALES') + '</a>'
        : '<a class="rc-btn amber" href="' + base() + '/' + t.id + '">VOLVER A LA MISIÓN</a>';
    }
    var nombre = esGen ? '¡Generales superadas!' : '¡Nivel ' + (t.niveles.indexOf(l) + 1) + ' superado!';
    return '<div class="rc-cuerpo"><span class="rc-disco fin">' + ico('trophy', 64, 1.8) + '</span><small class="rc-kick">LO LOGRASTE</small><h1>' + nombre + '</h1>' +
      '<p class="rc-sub">Completaste todos los pasos. Se abre lo que sigue.</p><div class="rc-pie">' + boton + '</div></div>';
  }

  function pantallaNivel(f) {
    var l = f.l, t = f.t, esGen = !!t.generales && t.generales.id === l.id;
    var ks = pasosNivel(l);
    var pend = ks.filter(function (k) { return !hechoK(l, k); });
    var i = pend.length ? ks.indexOf(pend[0]) : ks.length;
    var segs = ks.concat(['fin']).map(function (k, j) { return '<i class="rc-seg ' + (j < i ? 'on' : j === i ? 'cur' : '') + '"></i>'; }).join('');
    var cuerpo = i >= ks.length ? pantallaFin(f, esGen) : pantallaPaso(ks[i], f, esGen, i + 1, ks.length);
    vista.innerHTML = '<div class="mt mt-rc" style="--c:' + tono(D.temas.indexOf(t)) + '">' +
      '<div class="rc-top"><a class="rc-x" href="' + base() + '/' + t.id + '" aria-label="Volver a la misión">' + ico('close', 22, 3) + '</a><div class="rc-bar">' + segs + '</div></div>' + cuerpo + '</div>';
  }

  // ----- Router interno -----
  var ruta = { tema: null, leccion: null };
  function pintar() {
    calcular();
    hojaAbierta = null;
    var t = ruta.tema ? D.temas.filter(function (x) { return x.id === ruta.tema; })[0] : null;
    if (t && (t.bloqueado || t.vacio || D.sinAcceso)) { t = null; ruta.leccion = null; location.replace(base()); }
    var f = t && ruta.leccion ? buscarLeccion(ruta.leccion) : null;
    if (f && (f.t.id !== t.id || f.l.bloqueada || f.l.est.vacia)) { f = null; location.replace(base() + '/' + t.id); }
    if (f) { hojaAbierta = f.l.id; pantallaNivel(f); }
    else if (t) pantallaTema(t);
    else pantallaTemas();
  }
  function refrescar() { var y = window.scrollY; pintar(); window.scrollTo(0, y); }

  // ---------- Avance ----------
  async function marcar(paso, puntaje) {
    var ya = D.progreso[paso.id];
    if (ya && (puntaje == null || (ya.score != null && Number(ya.score) >= puntaje))) return;
    var fila = { student_id: D.sid, lesson_step_id: paso.id, lesson_id: paso.lesson_id,
      score: puntaje == null ? null : Math.max(0, Math.min(100, puntaje)), grading_status: 'graded' };
    var r = await sb.from('student_step_progress').upsert(fila, { onConflict: 'student_id,lesson_step_id' });
    if (r.error) { toast('No pudimos guardar tu avance. Revisá tu conexión.', true); return; }
    D.progreso[paso.id] = { score: fila.score, estado: 'graded' };
    await revisarLeccion(paso.lesson_id);
    refrescar();
  }

  async function revisarLeccion(lessonId) {
    var f = buscarLeccion(lessonId);
    if (!f) return;
    var e = estadoLeccion(f.l);
    if (e.completa && !D.hechas[lessonId]) {
      D.hechas[lessonId] = true;
      toast('¡Nivel superado! 🎉');
      await sb.from('student_lesson_progress').insert({ student_id: D.sid, lesson_id: lessonId });
    }
  }

  // ---------- Abrir cada recuadro ----------
  function pasoActual(k) { var f = buscarLeccion(hojaAbierta); return f && (D.pasos[f.l.id] || {})[k]; }

  async function abrirPaso(k) {
    var f = buscarLeccion(hojaAbierta), paso = pasoActual(k);
    if (!f || !paso) return;
    try {
      if (k === 'video' && paso.clase) {
        abrirClase(paso, f.l.titulo);
      } else if (k === 'video') {
        WaveVisor.abrirVideo({ titulo: f.l.titulo, alTerminar: function () { marcar(paso); },
          lista: paso.videos.map(function (v, n) {
            return /^yt:/.test(v.uid || '') ? { youtube: v.uid.slice(3), tramos: v.tramos }
              : { tramos: v.tramos, url: async function () { return (await llamar('content-access', { action: 'video', step_id: paso.id, index: n })).url; } };
          }) });
      } else if (k === 'pdf') {
        WaveVisor.abrirPdf({ titulo: f.l.titulo + ' · PDF', descargable: true, alTerminar: function () { marcar(paso); },
          chat: function (mensaje, conv) { return llamar('chat-tutor', { message: mensaje, lesson_step_id: paso.id, conversation_id: conv || undefined }); },
          url: async function (desc) { return (await llamar('content-access', { action: 'pdf', step_id: paso.id, descarga: !!desc })).url; } });
      } else if (k === 'interactive') {
        var r = await sb.from('lesson_steps').select('content').eq('id', paso.id).maybeSingle();
        if (r.error || !r.data || !r.data.content || !r.data.content.html) throw new Error('No pudimos abrir la actividad.');
        abrirInteractiva(paso, f.l.titulo, r.data.content.html);
      } else if (k === 'final') {
        abrirCuestionario({
          titulo: 'Actividad · ' + f.l.titulo, examen: false,
          cargar: function () { return preguntas('lesson_step_id', paso.id); },
          enviar: function (resp) { return llamar('corregir', { modo: 'actividad', lesson_step_id: paso.id, answers: resp }); },
          alTerminar: function (res) {
            D.progreso[paso.id] = { score: res.score, estado: 'graded' };
            revisarLeccion(paso.lesson_id).then(refrescar);
          }
        });
      } else if (k === 'review') {
        var intento = null;
        abrirCuestionario({
          titulo: 'Repaso · ' + f.l.titulo, examen: false, repaso: true,
          cargando: 'Estamos armando tu repaso…', cargandoSub: 'Son 6 preguntas nuevas, de esta lección y de las anteriores. Tené tu carpeta a mano.',
          cargar: async function () { var d = await llamar('review', { action: 'start', lesson_id: f.l.id }); intento = d.attempt_id; return d.questions; },
          enviar: function (resp) { return llamar('review', { action: 'submit', attempt_id: intento, answers: resp }); },
          alTerminar: function (res) {
            D.repaso[f.l.id] = { req: true, done: true, score: res.score };
            revisarLeccion(f.l.id).then(refrescar);
          }
        });
      } else if (k === 'complementary') {
        comp_abierto = !comp_abierto;
        refrescar();
      }
    } catch (e) { toast(e.message || 'No se pudo abrir.', true); }
  }

  function abrirVideoMision(temaId, lecId) {
    var tm = D.temas.filter(function (x) { return x.id === temaId; })[0];
    var lec = tm && tm.lecciones.filter(function (x) { return x.id === lecId; })[0], paso = lec && lec.videoPaso;
    if (!paso) return;
    if (paso.clase) return abrirClase(paso, lec.titulo).catch(function (e) { toast(e.message || 'No se pudo abrir.', true); });
    // La intro de Wave se carga una sola vez (admin) y va siempre delante de todos los videos de la misión
    var lista = paso.videos.map(function (v, n) {
      return /^yt:/.test(v.uid || '') ? { youtube: v.uid.slice(3), tramos: v.tramos }
        : { tramos: v.tramos, url: async function () { return (await llamar('content-access', { action: 'video', step_id: paso.id, index: n })).url; } };
    });
    if (D.introWave && tm.lecciones[0] === lec && !(paso.videos[0] && (paso.videos[0].intro || paso.videos[0].final))) {
      lista.unshift({ tramos: D.introWave.tramos || [], url: async function () { return (await llamar('content-access', { action: 'intro_wave' })).url; } });
    }
    WaveVisor.abrirVideo({ titulo: 'Video · ' + lec.titulo, alTerminar: function () { marcar(paso); }, lista: lista });
  }

  // Entrega de la carpeta: se corrige acá, sin IA. Se aprueba con hasta 1 mal; al aprobar se muestran las soluciones.
  async function entregarCarpeta(btn) {
    var f = buscarLeccion(hojaAbierta), paso = f && (D.pasos[f.l.id] || {}).pdf;
    if (!paso) return;
    var inputs = Array.prototype.slice.call(vista.querySelectorAll('.rc-in'));
    var resp = inputs.map(function (x) { return x.value.trim(); });
    if (resp.some(function (x) { return !x; })) { toast('Completá todas las respuestas antes de entregar.', true); return; }
    btn.disabled = true;
    var r = await sb.rpc('entregar_carpeta', { p_step: paso.id, p_respuestas: resp });
    btn.disabled = false;
    if (r.error) { toast(r.error.message || 'No pudimos entregar. Probá de nuevo.', true); return; }
    var d = r.data;
    inputs.forEach(function (x, i) {
      var fila = x.closest('.rc-item');
      fila.classList.toggle('ok', !!d.items[i]); fila.classList.toggle('no', !d.items[i]);
      if (d.items[i]) x.readOnly = true;
    });
    var aviso = vista.querySelector('.rc-aviso');
    if (aviso) aviso.remove();
    if (!d.todas) {
      var mal = d.items.map(function (o, i) { return o ? null : i + 1; }).filter(Boolean);
      var m = document.createElement('div');
      m.className = 'rc-aviso no';
      m.textContent = (mal.length === 1 ? 'La consigna ' + mal[0] + ' no coincide' : 'Las consignas ' + mal.join(' y ') + ' no coinciden') + '. Volvé a tu carpeta, revisá el procedimiento y probá de nuevo.';
      vista.querySelector('.rc-pie').before(m);
      return;
    }
    D.carpeta[paso.id] = true;
    var sols = (d.soluciones || []).map(function (s, i) { return s ? '<li><b>' + (i + 1) + '.</b> ' + esc(s) + '</li>' : ''; }).join('');
    var ok = document.createElement('div');
    ok.className = 'rc-aviso ok';
    var titOk = d.errores ? '¡Aprobada! Tuviste una sola mal: mirá su solución abajo.' : '¡Todas correctas!';
    ok.innerHTML = '<b>' + titOk + '</b>' + (sols ? '<ul class="rc-sols">' + sols + '</ul>' : '');
    vista.querySelector('.rc-pie').before(ok);
    btn.textContent = 'CONTINUAR'; btn.setAttribute('data-rc', 'continuar');
  }

  async function descargar(i) {
    var paso = pasoActual('complementary');
    try {
      var d = await llamar('content-access', { action: 'file', step_id: paso.id, index: i, descarga: true });
      var a = document.createElement('a');
      a.href = d.url; a.rel = 'noopener'; a.download = '';
      document.body.appendChild(a); a.click(); a.remove();
    } catch (e) { toast(e.message || 'No se pudo descargar.', true); }
  }

  // ---------- Clase animada (reemplaza al video): HTML en un marco aislado, con voz del dispositivo ----------
  async function abrirClase(paso, titulo) {
    var r = await sb.from('lesson_steps').select('html:content->>clase_html').eq('id', paso.id).maybeSingle();
    if (r.error || !r.data || !r.data.html) throw new Error('No pudimos abrir la clase.');
    var el = document.createElement('div');
    el.className = 'wvp';
    el.innerHTML =
      '<div class="wvp-caja"><div class="wvp-barra"><b class="wvp-titulo">' + esc(titulo) + ' · Clase</b>' +
      '<button type="button" class="wvp-b wvp-x" data-cerrar="1" aria-label="Cerrar">✕</button></div>' +
      '<div class="mt-marco"><iframe title="Clase" allow="autoplay; fullscreen" sandbox="allow-scripts allow-forms"></iframe></div></div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');
    var frame = el.querySelector('iframe');
    frame.srcdoc = r.data.html;
    function cerrar() {
      window.removeEventListener('message', alMensaje);
      try { frame.contentWindow.postMessage({ tipo: 'wave-clase-stop' }, '*'); } catch (_) {}
      try { window.speechSynthesis && window.speechSynthesis.cancel(); } catch (_) {}
      document.body.classList.remove('wvp-abierto');
      setTimeout(function () { frame.src = 'about:blank'; el.remove(); }, 150);
    }
    function alMensaje(ev) {
      if (ev.source !== frame.contentWindow || !ev.data || ev.data.tipo !== 'wave-clase-fin') return;
      marcar(paso); toast('¡Clase terminada! 🎉');
    }
    window.addEventListener('message', alMensaje);
    el.addEventListener('click', function (ev) { if (ev.target === el || ev.target.closest('[data-cerrar]')) cerrar(); });
  }

  // ---------- Actividad interactiva (HTML en un marco aislado) ----------
  function abrirInteractiva(paso, titulo, html) {
    var el = document.createElement('div');
    el.className = 'wvp';
    el.innerHTML =
      '<div class="wvp-caja"><div class="wvp-barra"><b class="wvp-titulo">' + esc(titulo) + ' · Actividad interactiva</b>' +
      '<button type="button" class="wvp-b wvp-desc" data-fin="1">Terminé ✓</button>' +
      '<button type="button" class="wvp-b wvp-x" data-cerrar="1" aria-label="Cerrar">✕</button></div>' +
      '<div class="mt-marco"><iframe title="Actividad interactiva" sandbox="allow-scripts allow-forms allow-modals"></iframe></div></div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');
    var frame = el.querySelector('iframe');
    frame.srcdoc = html;

    function cerrar() {
      window.removeEventListener('message', alMensaje);
      document.body.classList.remove('wvp-abierto');
      el.remove();
    }
    function alMensaje(ev) {
      if (ev.source !== frame.contentWindow || !ev.data || ev.data.tipo !== 'wave-resultado') return;
      var pt = Number(ev.data.puntaje);
      marcar(paso, isFinite(pt) ? pt : null);
      toast('¡Actividad terminada! 🎉');
    }
    window.addEventListener('message', alMensaje);
    el.addEventListener('click', function (ev) {
      if (ev.target.closest('[data-fin]')) { marcar(paso, null); toast('¡Actividad terminada! 🎉'); cerrar(); }
      else if (ev.target === el || ev.target.closest('[data-cerrar]')) cerrar();
    });
  }

  // ---------- Cuestionario (actividad por consigna y examen) ----------
  async function preguntas(col, id) {
    var r = await sb.from('questions').select('id, prompt, question_type, options, points, position, tiempo_seg').eq(col, id).order('position');
    if (r.error) throw r.error;
    if (!r.data.length) throw new Error('Todavía no hay preguntas cargadas.');
    return r.data;
  }

  function abrirCuestionario(op) {
    var el = document.createElement('div');
    el.className = 'wvp';
    el.innerHTML = '<div class="wvp-caja"><div class="wvp-barra"><b class="wvp-titulo">' + esc(op.titulo) + '</b>' +
      '<button type="button" class="wvp-b wvp-x" data-cerrar="1" aria-label="Cerrar">✕</button></div>' +
      '<div class="mt-cuest"></div></div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');
    var cuerpo = el.querySelector('.mt-cuest');
    var lista = [], enviando = false, entregado = false, relamp = null;
    if (window.WaveTipos) WaveTipos.enlazar(cuerpo);
    // Enunciado que ve el alumno: si la pregunta tiene números al azar, ya viene con los números sorteados
    function pr(q) { return q._prompt != null ? q._prompt : q.prompt; }
    function sembrar() {
      lista.forEach(function (q) {
        q._seed = Math.random().toString(36).slice(2, 10);
        q._prompt = null;
        if (q.options && q.options.vars && window.WaveCalc) {
          var v = WaveCalc.instanciar(q.options, q._seed);
          q._prompt = v ? WaveCalc.plantilla(q.prompt, v) : q.prompt;
        }
      });
    }

    function cerrar() { if (relamp) clearInterval(relamp.t); document.body.classList.remove('wvp-abierto'); el.remove(); }
    el.addEventListener('click', function (ev) {
      var fl = ev.target.closest('[data-mov]');
      if (fl) {
        var li = fl.closest('li'), ol = li && li.parentNode;
        if (fl.getAttribute('data-mov') === 'up' && li.previousElementSibling) ol.insertBefore(li, li.previousElementSibling);
        else if (fl.getAttribute('data-mov') === 'down' && li.nextElementSibling) ol.insertBefore(li.nextElementSibling, li);
        return;
      }
      if (ev.target === el || ev.target.closest('[data-cerrar]')) { if (!enviando) cerrar(); return; }
      if (ev.target.closest('[data-rel]')) { siguienteRel(); return; }
      if (ev.target.closest('[data-enviar]')) enviar();
      else if (ev.target.closest('[data-otra]')) { if (op.repaso && entregado) traer(); else formulario(); }
    });

    var NUEVOS = ['fill_blank', 'ordering', 'matching', 'classify', 'table_fill', 'multi_select', 'solve_complete', 'odd_one_out', 'numeric', 'tap_text', 'tokens', 'keywords', 'label_image'];
    function listaOp(o) { return Array.isArray(o) ? o.map(String) : []; }
    function selectDe(i, k, opciones) {
      return '<select class="mt-sel" data-w="' + i + '" data-k="' + k + '"><option value="">Elegí…</option>' +
        opciones.map(function (x) { return '<option value="' + esc(x) + '">' + esc(x) + '</option>'; }).join('') + '</select>';
    }
    // Devuelve el HTML del cuerpo del campo para los tipos nuevos, o null si la estructura no sirve (se muestra como respuesta libre)
    function campoNuevo(q, i) {
      var t = q.question_type, o = q.options, w = ' data-w="' + i + '"';
      if (window.WaveTipos && WaveTipos.soporta(t)) return WaveTipos.html(q, i, pr(q));
      if (t === 'fill_blank') {
        var partes = esc(pr(q)).split('___');
        if (partes.length < 2) partes.push('');
        var n = 0;
        return '<p class="mt-hueco-p"' + w + '>' + partes.map(function (x, k) {
          return k < partes.length - 1 ? x + '<input type="text" class="mt-hueco" data-h="' + (n++) + '" maxlength="80" autocomplete="off">' : x;
        }).join('') + '</p>';
      }
      var enun = '<p>' + esc(pr(q)) + '</p>';
      if (t === 'multi_select' && listaOp(o).length) {
        return enun + '<small class="mt-ayuda">Marcá todas las que sean correctas.</small>' + listaOp(o).map(function (x) {
          return '<label class="mt-op"><input type="checkbox"' + w + ' value="' + esc(x) + '"><span>' + esc(x) + '</span></label>';
        }).join('');
      }
      if (t === 'odd_one_out' && listaOp(o).length) {
        return enun + listaOp(o).map(function (x) {
          return '<label class="mt-op"><input type="radio" name="q' + i + '" value="' + esc(x) + '"><span>' + esc(x) + '</span></label>';
        }).join('');
      }
      if (t === 'ordering' && listaOp(o).length) {
        return enun + '<small class="mt-ayuda">Usá las flechas para poner los elementos en orden.</small><ol class="mt-orden"' + w + '>' +
          listaOp(o).map(function (x) {
            return '<li data-v="' + esc(x) + '"><span class="mt-orden-t">' + esc(x) + '</span><span class="mt-orden-b"><button type="button" class="mt-flecha" data-mov="up" aria-label="Subir">▲</button><button type="button" class="mt-flecha" data-mov="down" aria-label="Bajar">▼</button></span></li>';
          }).join('') + '</ol>';
      }
      if (t === 'matching' && o && listaOp(o.izquierda).length && listaOp(o.derecha).length) {
        return enun + '<small class="mt-ayuda">Elegí la pareja de cada elemento.</small><div class="mt-pares">' + listaOp(o.izquierda).map(function (x, k) {
          return '<div class="mt-par"><span>' + esc(x) + '</span>' + selectDe(i, k, listaOp(o.derecha)) + '</div>';
        }).join('') + '</div>';
      }
      if (t === 'classify' && o && listaOp(o.elementos).length && listaOp(o.categorias).length) {
        return enun + '<small class="mt-ayuda">Elegí la categoría de cada elemento.</small><div class="mt-pares">' + listaOp(o.elementos).map(function (x, k) {
          return '<div class="mt-par"><span>' + esc(x) + '</span>' + selectDe(i, k, listaOp(o.categorias)) + '</div>';
        }).join('') + '</div>';
      }
      if (t === 'table_fill' && o && listaOp(o.columnas).length && Array.isArray(o.filas) && o.filas.length) {
        return enun + '<small class="mt-ayuda">Completá las celdas vacías.</small><div class="mt-tabla-w"><table class="mt-tabla"' + w + '><thead><tr>' +
          listaOp(o.columnas).map(function (c) { return '<th>' + esc(c) + '</th>'; }).join('') + '</tr></thead><tbody>' +
          o.filas.map(function (f, r) {
            return '<tr>' + listaOp(f).map(function (c, k) {
              return c === '' ? '<td><input type="text" class="mt-celda" data-r="' + r + '" data-c="' + k + '" maxlength="40" autocomplete="off"></td>' : '<td>' + esc(c) + '</td>';
            }).join('') + '</tr>';
          }).join('') + '</tbody></table></div>';
      }
      if (t === 'solve_complete') {
        return enun + '<label class="mt-lbl">Procedimiento</label><textarea class="mt-txt" data-w="' + i + '" data-k="proc" rows="3" maxlength="2000" placeholder="Escribí cómo lo resolviste"></textarea>' +
          '<label class="mt-lbl">Resultado</label><input type="text" class="mt-txt" data-w="' + i + '" data-k="res" maxlength="200" placeholder="Tu resultado">';
      }
      return null;
    }

    // Lee lo que respondió el alumno y lo pasa a texto (así lo recibe el corrector)
    function leerNuevo(q, i) {
      var t = q.question_type, o = q.options, sel = '[data-w="' + i + '"]', out = [];
      if (window.WaveTipos && WaveTipos.soporta(t)) return WaveTipos.leer(q, i, cuerpo);
      if (t === 'fill_blank') {
        var hs = Array.prototype.slice.call(cuerpo.querySelectorAll(sel + ' .mt-hueco'));
        var llenos = hs.some(function (h) { return h.value.trim(); });
        return llenos ? hs.map(function (h, k) { return (k + 1) + ') ' + h.value.trim(); }).join(' | ') : '';
      }
      if (t === 'multi_select') {
        return Array.prototype.map.call(cuerpo.querySelectorAll(sel + ':checked'), function (c) { return c.value; }).join(' | ');
      }
      if (t === 'odd_one_out') { var c1 = cuerpo.querySelector('[name="q' + i + '"]:checked'); return c1 ? c1.value : ''; }
      if (t === 'ordering') {
        return Array.prototype.map.call(cuerpo.querySelectorAll(sel + ' li'), function (li) { return li.getAttribute('data-v'); }).join(' → ');
      }
      if (t === 'matching' || t === 'classify') {
        var izq = t === 'matching' ? listaOp(o.izquierda) : listaOp(o.elementos), sep = t === 'matching' ? ' = ' : ' → ', alguno = false;
        izq.forEach(function (x, k) {
          var s = cuerpo.querySelector('select' + sel + '[data-k="' + k + '"]');
          var v = s ? s.value : '';
          if (v) alguno = true;
          out.push(x + sep + (v || '(sin elegir)'));
        });
        return alguno ? out.join('\n') : '';
      }
      if (t === 'table_fill') {
        Array.prototype.forEach.call(cuerpo.querySelectorAll(sel + ' .mt-celda'), function (c) {
          if (c.value.trim()) out.push('Fila ' + (+c.dataset.r + 1) + ', columna ' + listaOp(o.columnas)[+c.dataset.c] + ': ' + c.value.trim());
        });
        return out.join('\n');
      }
      if (t === 'solve_complete') {
        var pr = cuerpo.querySelector('textarea' + sel), rs = cuerpo.querySelector('input' + sel);
        var a = pr ? pr.value.trim() : '', b = rs ? rs.value.trim() : '';
        return (a || b) ? 'Procedimiento: ' + (a || '(vacío)') + '\nResultado: ' + (b || '(vacío)') : '';
      }
      return null;
    }

    function campo(q, i) {
      var nuevo = NUEVOS.indexOf(q.question_type) >= 0 ? campoNuevo(q, i) : null;
      if (nuevo !== null) return '<div class="mt-preg"><div class="mt-preg-n">' + (i + 1) + '</div><div class="mt-preg-c">' + nuevo + '</div></div>';
      var h = '<div class="mt-preg"><div class="mt-preg-n">' + (i + 1) + '</div><div class="mt-preg-c"><p>' + esc(pr(q)) + '</p>';
      if (q.question_type === 'multiple_choice' || q.question_type === 'true_false') {
        h += (q.options || []).map(function (o, j) {
          return '<label class="mt-op"><input type="radio" name="q' + i + '" value="' + esc(o) + '"><span>' + esc(o) + '</span></label>';
        }).join('');
      } else if (q.question_type === 'short_answer') {
        h += '<input type="text" class="mt-txt" name="q' + i + '" maxlength="400" placeholder="Tu respuesta">';
      } else {
        h += '<textarea class="mt-txt" name="q' + i + '" rows="4" maxlength="4000" placeholder="Escribí tu respuesta"></textarea>';
      }
      return h + '</div></div>';
    }

    function leerResp(q, i) {
      if (NUEVOS.indexOf(q.question_type) >= 0 && campoNuevo(q, i) !== null) { var a = leerNuevo(q, i); return a == null ? '' : a; }
      var c = cuerpo.querySelector('[name="q' + i + '"]:checked') || cuerpo.querySelector('.mt-txt[name="q' + i + '"]');
      return c ? c.value : '';
    }
    function mostrarResp(q, a) { return window.WaveTipos && WaveTipos.soporta(q.question_type) ? WaveTipos.mostrar(q, a) : a; }

    function formulario() {
      sembrar();
      if (relamp) clearInterval(relamp.t);
      relamp = null;
      if (lista.some(function (q) { return q.tiempo_seg; })) { relampago(); return; }
      cuerpo.innerHTML = lista.map(campo).join('') +
        '<div class="mt-cuest-pie"><button type="button" class="mt-boton" data-enviar="1">Entregar</button></div>';
      cuerpo.scrollTo(0, 0);
    }

    // Modo Relámpago: una pregunta por vez, con cronómetro. Si se acaba el tiempo pasa sola a la siguiente.
    function relampago() {
      relamp = { i: 0, resp: [], t: null };
      mostrarRel();
    }
    function mostrarRel() {
      var i = relamp.i, q = lista[i], seg = q.tiempo_seg || 20, resto = seg;
      cuerpo.innerHTML = '<div class="rl-top"><span class="rl-cont">⚡ Relámpago · ' + (i + 1) + ' de ' + lista.length + '</span><span class="rl-seg"><b>' + seg + '</b> s</span></div>' +
        '<div class="rl-barra"><i style="animation-duration:' + seg + 's"></i></div>' + campo(q, i) +
        '<div class="mt-cuest-pie"><button type="button" class="mt-boton" data-rel="1">' + (i === lista.length - 1 ? 'Terminar' : 'Siguiente') + '</button></div>';
      cuerpo.scrollTo(0, 0);
      var num = cuerpo.querySelector('.rl-seg b');
      clearInterval(relamp.t);
      relamp.t = setInterval(function () {
        resto--;
        if (num) num.textContent = Math.max(resto, 0);
        if (resto <= 0 && !enviando) siguienteRel();
      }, 1000);
    }
    function siguienteRel() {
      if (!relamp) return;
      clearInterval(relamp.t);
      var i = relamp.i, q = lista[i];
      relamp.resp.push({ question_id: q.id, answer: leerResp(q, i), seed: q._seed });
      relamp.i++;
      if (relamp.i < lista.length) mostrarRel(); else enviar(relamp.resp);
    }

    async function enviar(pre) {
      var resp = pre || lista.map(function (q, i) { return { question_id: q.id, answer: leerResp(q, i), seed: q._seed }; });
      var vacias = resp.filter(function (r) { return !String(r.answer).trim(); }).length;
      if (!pre && vacias && !confirm('Te quedaron ' + vacias + (vacias === 1 ? ' pregunta' : ' preguntas') + ' sin responder. ¿Entregar igual?')) return;
      enviando = true;
      cuerpo.innerHTML = '<div class="mt-cuest-estado"><div class="mt-girar"></div><b>Estamos corrigiendo tus respuestas…</b><small>Puede tardar unos segundos. No cierres esta ventana.</small></div>';
      try {
        var res = await op.enviar(resp);
        enviando = false; entregado = true;
        resultado(res, resp);
        op.alTerminar(res);
      } catch (e) {
        enviando = false;
        cuerpo.innerHTML = '<div class="mt-cuest-estado error"><b>' + esc(e.message || 'No se pudo entregar.') + '</b>' +
          '<div class="mt-cuest-pie"><button type="button" class="mt-boton" data-otra="1">Volver a la actividad</button></div></div>';
      }
    }

    function resultado(res, resp) {
      var nota = Math.round(res.score);
      var ok = op.examen ? res.passed : nota >= 70;
      var titulo = op.examen ? (res.passed ? '¡Aprobaste!' : 'Todavía no llegaste') : (nota >= 70 ? '¡Muy bien!' : '¡Seguí practicando!');
      var detalle = op.examen ? (res.passed ? 'Superaste los ' + res.passing_score + ' puntos que pide este examen.' : 'Necesitás ' + res.passing_score + ' o más para aprobar. Podés intentarlo de nuevo cuando quieras.') : '';
      var porId = {};
      (res.results || []).forEach(function (r) { porId[r.question_id] = r; });
      var mias = {};
      resp.forEach(function (r) { mias[r.question_id] = r.answer; });
      cuerpo.innerHTML =
        '<div class="mt-res ' + (ok ? 'ok' : 'no') + '"><div class="mt-res-nota"><b>' + nota + '</b><span>de 100</span></div><h3>' + titulo + '</h3>' +
        (detalle ? '<p>' + detalle + '</p>' : '') + (res.overall_feedback ? '<p class="mt-res-fb">' + esc(res.overall_feedback) + '</p>' : '') + '</div>' +
        '<div class="mt-res-lista">' + lista.map(function (q, i) {
          var r = porId[q.id] || {}, sc = Math.round(r.score || 0);
          return '<div class="mt-res-item"><div class="mt-res-cab"><span class="mt-preg-n">' + (i + 1) + '</span><b>' + esc(pr(q)) + '</b><span class="mt-chip-n ' + (sc >= 70 ? 'ok' : sc >= 40 ? 'med' : 'bajo') + '">' + sc + '</span></div>' +
            '<p class="mt-res-tu"><small>Tu respuesta</small>' + esc(mostrarResp(q, mias[q.id]) || '(sin responder)') + '</p>' +
            (r.feedback ? '<p class="mt-res-dev">' + esc(r.feedback) + '</p>' : '') + '</div>';
        }).join('') + '</div>' +
        '<div class="mt-cuest-pie">' + (ok && op.examen ? '' : '<button type="button" class="mt-boton suave" data-otra="1">' + (op.repaso ? 'Hacer otro repaso' : 'Intentar de nuevo') + '</button>') +
        '<button type="button" class="mt-boton" data-cerrar="1">Listo</button></div>';
      cuerpo.scrollTo(0, 0);
    }

    function traer() {
      entregado = false;
      cuerpo.innerHTML = '<div class="mt-cuest-estado">' + (op.cargando ? '<div class="mt-girar"></div><b>' + esc(op.cargando) + '</b><small>' + esc(op.cargandoSub || '') + '</small>' : 'Cargando…') + '</div>';
      op.cargar().then(function (qs) { lista = qs; formulario(); }).catch(function (e) {
        cuerpo.innerHTML = '<div class="mt-cuest-estado error"><b>' + esc(e.message || 'No se pudo cargar.') + '</b></div>';
      });
    }
    traer();
  }

  function abrirExamen(temaId) {
    var t = D.temas.filter(function (x) { return x.id === temaId; })[0];
    if (!t || !t.examen) return;
    if (!t.examenDisponible) { toast('Primero superá todos los niveles de la misión.', true); return; }
    var sorteo = null; // cada vez que se abre, el examen sortea preguntas distintas del banco del tema
    abrirCuestionario({
      titulo: 'Nivel jefe · ' + t.titulo, examen: true,
      cargar: async function () {
        var r = await sb.rpc('sortear_examen', { p_exam: t.examen.id });
        if (r.error) throw new Error(r.error.message || 'No se pudo armar el examen.');
        sorteo = r.data.sorteo_id || null;
        if (!r.data.questions || !r.data.questions.length) throw new Error('Todavía no hay preguntas cargadas.');
        return r.data.questions;
      },
      enviar: function (resp) { return llamar('corregir', { modo: 'examen', exam_id: t.examen.id, answers: resp, sorteo_id: sorteo }); },
      alTerminar: function (res) {
        t.examen.mejor = Math.max(t.examen.mejor || 0, res.score);
        if (res.passed) t.examen.aprobado = true;
        refrescar();
      }
    });
  }

  // ---------- Introducción ----------
  function abrirIntro() {
    WaveVisor.abrirVideo({ titulo: 'Introducción · ' + D.materia.name,
      url: async function () { return (await llamar('content-access', { action: 'intro', subject_id: D.materia.id })).url; } });
  }

  // ---------- Entrada ----------
  var enlazado = false;
  function enlazar() {
    if (enlazado) return;
    enlazado = true;
    vista.addEventListener('click', function (ev) {
      if (!D || !vista.querySelector('.mt')) return;
      var av = ev.target.closest('[data-aviso]');
      if (av) return toast(av.getAttribute('data-aviso'), true);
      var rc = ev.target.closest('[data-rc]');
      if (rc) {
        var a = rc.getAttribute('data-rc');
        if (a === 'abrir') return abrirPaso(rc.getAttribute('data-k'));
        if (a === 'entregar') return entregarCarpeta(rc);
        if (a === 'continuar') return refrescar();
      }
      var vd = ev.target.closest('[data-video]');
      if (vd) return abrirVideoMision(ruta.tema, vd.getAttribute('data-video'));
      var x = ev.target.closest('[data-examen]');
      if (x) return abrirExamen(x.getAttribute('data-examen'));
      if (ev.target.closest('[data-intro]')) return abrirIntro();
      var b = ev.target.closest('[data-paso]');
      if (b && !b.disabled) return abrirPaso(b.getAttribute('data-paso'));
      var d = ev.target.closest('[data-bajar]');
      if (d) return descargar(+d.getAttribute('data-bajar'));
    });
  }

  async function abrir(el, materiaId, temaId, leccionId) {
    vista = el;
    enlazar();
    ruta = { tema: temaId || null, leccion: leccionId || null };
    comp_abierto = false;
    window.scrollTo(0, 0);
    if (D && D.materia.id === materiaId) { pintar(); return; }
    vista.innerHTML = '<div class="mt"><div class="mt-vacio">Cargando tu materia…</div></div>';
    try {
      D = await cargar(materiaId);
      pintar();
    } catch (e) {
      console.error(e);
      D = null;
      vista.innerHTML = '<div class="mt"><a class="mt-volver" href="#cursos">' + ico('back', 20, 3) + ' Mis cursos</a>' +
        '<div class="mt-vacio">No pudimos abrir esta materia.<br><small>' + esc(e.message || '') + '</small></div></div>';
    }
  }

  // Solo para pruebas visuales con datos de ejemplo
  function _probar(el, datos, r) { vista = el; D = datos; ruta = r || { tema: null, leccion: null }; enlazar(); pintar(); }

  window.WaveMateria = { abrir: abrir, _probar: _probar, _cuest: abrirCuestionario };
})();
