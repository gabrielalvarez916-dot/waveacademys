// Pantalla de materia del alumno, estilo Simply Piano:
// Introducción + un rectángulo por tema, con las lecciones en círculos. Cada círculo abre sus recuadros de archivos.
(function () {
  var sb = Wave.sb;
  var vista = null;
  var D = null;          // datos de la materia abierta
  var hojaAbierta = null; // id de la lección que se está viendo
  var verPaso = {};
  var CUENTAS_PRUEBA = ['c7cce4c1-587d-42e1-8406-5a68b6a27194', '2b236b9d-d577-41fd-abbf-382b902e274e', '7c118754-b3ba-4334-bb4e-47a12783bb7a', 'd138161a-a48a-40c6-8251-bf2449000549']; // Alumno Primero: todo desbloqueado y puede saltear pasos (cuenta de prueba) // paso que el alumno eligió mirar dentro de un nivel (para volver atrás)

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

  // Tutor IA: cada pantalla le dice qué está mirando (solo esa misión); nunca se monta en el examen
  function tutorOps(pantalla, ctx) {
    return {
      pantalla: pantalla,
      enviar: function (payload) { return llamar('chat-tutor', payload); },
      ctx: function () { return typeof ctx === 'function' ? ctx() : ctx; },
      config: {
        ver: async function () { var r = await sb.rpc('tutor_config_ver', { p_student: D.sid }); return r.data && r.data[0]; },
        guardar: async function (apodo, nombre, pers) {
          var r = await sb.rpc('tutor_config_guardar', { p_student: D.sid, p_apodo: apodo, p_tutor_nombre: nombre, p_personalidad: pers });
          if (r.error) throw new Error(r.error.message || 'No se pudo guardar.');
        }
      }
    };
  }

  async function llamar(nombre, body) {
    var r = await sb.functions.invoke(nombre, { body: body });
    if (r.error) {
      var msg = 'No se pudo completar. Probá de nuevo en un momento.';
      var st = null;
      try { st = r.error.context && r.error.context.status; var c = await r.error.context.json(); if (c && c.error) msg = c.error; } catch (e) { /* genérico */ }
      if (st === 401 || msg === 'No autenticado') {  // la sesión se cerró (por ejemplo, en otra pestaña): se vuelve a entrar en vez de mostrar un error técnico
        msg = 'Tu sesión se cerró. Volvé a entrar para ver el contenido.';
        try { await sb.auth.signOut(); } catch (e2) { /* nada */ }
        setTimeout(function () { location.reload(); }, 2500);
      }
      throw new Error(msg);
    }
    if (r.data && r.data.error) throw new Error(r.data.error);
    return r.data;
  }

  // Trayecto Anticipación, modo calmo: las clases y actividades corren sin música ni efectos de sonido (la voz de la clase queda) y sin transiciones
  function calmar(html) {
    if (!D || !D.adaptaciones || D.adaptaciones.indexOf('ant_calmo') < 0 || typeof html !== 'string') return html;
    var cod = '<script>try{window.AudioContext=undefined;window.webkitAudioContext=undefined;}catch(e){}</script><style>*,*::before,*::after{transition:none!important}</style>';
    return /<head[^>]*>/i.test(html) ? html.replace(/<head[^>]*>/i, function (m) { return m + cod; }) : cod + html;
  }

  // ---------- Datos ----------
  async function cargar(materiaId) {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;
    var est = await sb.from('students').select('id, pais').eq('profile_id', uid).maybeSingle();
    if (est.error) throw est.error;
    if (!est.data) throw new Error('Esta cuenta no es de un estudiante.');
    var sid = est.data.id;
    var neutro = !!est.data.pais && est.data.pais !== 'Argentina'; // alumnos de otros países: clases y PDF en español neutro

    var mat = await sb.from('subjects').select('id, name, color, intro_video_uid, intro_clase').eq('id', materiaId).maybeSingle();
    if (mat.error) throw mat.error;
    if (!mat.data) throw new Error('No encontramos esta materia.');
    var iw = await sb.from('app_settings').select('value').eq('key', 'intro_wave').maybeSingle();
    var introWave = iw.data && iw.data.value && iw.data.value.uid ? iw.data.value : null;

    var tem = await sb.from('topics').select('id, title, position, solo_para, lessons(id, title, position)').eq('subject_id', materiaId).order('position');
    if (tem.error) throw tem.error;
    var temas = tem.data.filter(function (t) { // misiones alternativas: cada alumno ve la de su país
      return !t.solo_para || t.solo_para === (neutro ? 'internacional' : 'argentina');
    }).map(function (t) {
      return { id: t.id, titulo: t.title, posicion: t.position,
        lecciones: (t.lessons || []).slice().sort(function (a, b) { return a.position - b.position; })
          .map(function (l) { return { id: l.id, titulo: l.title, tema: t.id }; }) };
    }).sort(function (a, b) { return a.posicion - b.posicion; });

    var pasos = await sb.rpc('materia_pasos', { p_materia: materiaId });
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
        carpeta: k === 'pdf' && Array.isArray(neutro && Array.isArray(p.carpeta_neutro) ? p.carpeta_neutro : p.carpeta) ? (neutro && Array.isArray(p.carpeta_neutro) ? p.carpeta_neutro : p.carpeta) : []
      };
    });

    var progreso = {};
    prog.data.forEach(function (p) { progreso[p.lesson_step_id] = { score: p.score, estado: p.grading_status }; });
    var hechas = {};
    lp.data.forEach(function (l) { hechas[l.lesson_id] = true; });

    var examen = {};
    var saltosQ = await sb.from('saltos_mision').select('topic_id, estado').eq('student_id', sid);
    var stQ = await sb.from('students').select('trayectos_apoyo, adaptaciones').eq('id', sid).maybeSingle();
    var saltos = {}; (saltosQ.error ? [] : saltosQ.data || []).forEach(function (x) { saltos[x.topic_id] = x.estado; });
    var desafio = !!(stQ.data && (stQ.data.trayectos_apoyo || []).indexOf('desafio') >= 0);
    var adaptaciones = (stQ.data && stQ.data.adaptaciones) || [];
    exs.data.forEach(function (e) {
      var mias = ints.data.filter(function (i) { return i.exam_id === e.id; });
      var graded = mias.filter(function (i) { return i.grading_status === 'graded' && i.score != null; });
      examen[e.topic_id] = { id: e.id, aprobar: e.passing_score, intentos: mias.length, tienePreguntas: !!exConPreg[e.id],
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
      neutro: neutro,
      adaptaciones: adaptaciones, sid: sid, prueba: CUENTAS_PRUEBA.indexOf(sid) >= 0, introWave: introWave, materia: mat.data, temas: temas, pasos: porLeccion, carpeta: carpeta, progreso: progreso, repaso: repaso, hechas: hechas, examen: examen, saltos: saltos, desafio: desafio,
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
        if (D.saltos && D.saltos[t.id] === 'saltada' && !l.est.vacia) { l.est.completa = true; l.est.hechos = l.est.total; l.est.frac = 1; } // misión saltada por examen
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
    if (D.prueba) D.temas.forEach(function (t) { // cuenta de prueba: todo abierto
      t.bloqueado = false; t.examenDisponible = !!t.examen;
      t.lecciones.forEach(function (l) { l.bloqueada = false; });
    });
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
      '<div class="mt-card-t">' + (o.kicker ? '<span class="mt-card-k">' + esc(o.kicker) + '</span>' : '') + '<h2>' + esc(o.titulo) + '</h2><p>' + esc(o.texto) + '</p>' +
      (o.boton ? '<span class="mt-card-btn">' + o.boton + '</span>' : '') + '</div>' +
      '<div class="mt-card-fig">' + (o.figura || '') + '</div>' +
      (o.trofeo ? '<span class="mt-trofeo">' + ico('trophy', 34, 1.8) + '</span>' : '') +
      (o.estado === 'bloq' ? '<span class="mt-cand">' + ico('lock', 26, 2.8) + '</span>' : '');
    var estilo = ' style="--k:' + o.color + '"';
    if (o.href) return '<a class="' + cls + '" href="' + o.href + '"' + estilo + '>' + interior + '</a>';
    return '<button type="button" class="' + cls + '"' + estilo + (o.aviso ? ' data-aviso="' + esc(o.aviso) + '"' : '') + (o.intro ? ' data-intro="1"' : '') + (o.biblio ? ' data-biblio="1"' : '') + '>' + interior + '</button>';
  }

  function pantallaTemas() {
    var m = D.materia, icono = window.WaveIconos ? WaveIconos.materia(m.name) : '';
    var cards = [];
    cards.push(m.intro_video_uid || m.intro_clase
      ? tarjeta({ titulo: 'Introducción', texto: 'Conocé la materia antes de empezar', boton: 'VER VIDEO', color: colorSeguro(m.color), figura: icono, intro: true })
      : tarjeta({ titulo: 'Introducción', texto: 'El video de introducción estará disponible muy pronto', color: colorSeguro(m.color), figura: icono, estado: 'pronto' }));
    D.temas.forEach(function (t, i) {
      var c = tono(i), o = { titulo: t.titulo, kicker: 'Misión ' + (i + 1), color: c, figura: icono };
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
    var abierto = (t.completo || D.prueba) && !sig.vacio;
    var cls = abierto ? 'libre actual' : 'bloq', contenido = ico('chevron', 52, 3.2);
    if (!abierto) contenido = ico('lock', 34, 2.6);
    var burbuja = abierto ? '<span class="mt-burbuja">¡Misión cumplida!</span>' : '';
    return nodo(cls, burbuja + discoNodo(cls, contenido, 0) + '<span class="mt-nombre">Siguiente misión</span>',
      abierto ? base() + '/' + sig.id : null, abierto ? '' : (sig.vacio ? 'La próxima misión está en preparación.' : 'Superá el nivel jefe para pasar a la siguiente misión.'));
  }

  // Mapa de la misión: todo el recorrido de un vistazo y dónde está parado el alumno
  var ROT_PASO = { video: 'Clase en video', pdf: 'Leer el PDF', carpeta: 'Entregar la carpeta', final: 'Práctica' };
  // Trayecto Anticipación: el camino en dibujos y el cartel «Ahora / Después» (sin listas de texto)
  function esAnt() { return !!(D && D.adaptaciones && D.adaptaciones.indexOf('ant_mapa') >= 0); }
  var ANT_ICO = { video: ['🎬', 'Clase', 'Mirar la clase'], pdf: ['📄', 'PDF', 'Leer el PDF'], carpeta: ['📁', 'Carpeta', 'Entregar la carpeta'], interactive: ['🎮', 'Juego', 'Hacer la actividad'], final: ['✏️', 'Práctica', 'Hacer la práctica'], examen: ['🏆', 'Examen', 'Hacer el examen'] };
  function antPasos(t) {
    var out = [], marcado = false;
    function add(k, hecho, bloq, nivel) {
      var est = hecho ? 'hecho' : bloq ? 'bloq' : (!marcado ? 'ahora' : 'sigue');
      if (est === 'ahora') marcado = true;
      var ic = ANT_ICO[k] || ['⭐', 'Paso', 'Hacer el paso'];
      out.push({ k: k, ico: ic[0], corto: ic[1], largo: ic[2], est: est, nivel: nivel });
    }
    t.niveles.concat(t.generales ? [t.generales] : []).forEach(function (l, i) {
      var nom = t.generales && l === t.generales ? 'Generales' : 'Nivel ' + (i + 1);
      if (l.est.vacia) return;
      (l.est.req || []).forEach(function (k) { add(k, hechoK(l, k), l.bloqueada, nom); });
    });
    if (t.examen) add('examen', !!t.examen.aprobado, !t.examenDisponible && !t.examen.aprobado, 'Jefe');
    return out;
  }
  function antAhoraDespues(t) {
    var P = antPasos(t), i = -1;
    P.forEach(function (x, j) { if (i < 0 && x.est === 'ahora') i = j; });
    function cuadro(cls, rot, x, vacio) {
      return '<div class="ant-ad-c ' + cls + '"><small>' + rot + '</small>' + (x ? '<span class="ant-ad-i" aria-hidden="true">' + x.ico + '</span><b>' + esc(x.largo) + '</b>' : '<span class="ant-ad-i" aria-hidden="true">' + vacio[0] + '</span><b>' + esc(vacio[1]) + '</b>') + '</div>';
    }
    if (i < 0) {
      var todo = P.length && P.every(function (x) { return x.est === 'hecho'; });
      return '<div class="ant-ad">' + cuadro('ahora', 'AHORA', null, todo ? ['🎉', '¡Terminaste la misión!'] : ['🔒', 'Todavía no se puede']) + '</div>';
    }
    return '<div class="ant-ad" aria-label="Qué hacer ahora y qué viene después">' + cuadro('ahora', 'AHORA', P[i]) +
      '<span class="ant-ad-f" aria-hidden="true">➜</span>' + cuadro('despues', 'DESPUÉS', P[i + 1], ['🎉', '¡Listo!']) + '</div>';
  }
  function antMapaHtml(t) {
    var P = antPasos(t), grupos = [], ult = null;
    P.forEach(function (x) { if (x.nivel !== ult) { grupos.push({ nom: x.nivel, xs: [] }); ult = x.nivel; } grupos[grupos.length - 1].xs.push(x); });
    if (!grupos.length) return '<p class="ant-vacio">Esta misión todavía está en preparación.</p>';
    return grupos.map(function (g) {
      return '<div class="ant-tramo"><h3>' + esc(g.nom) + '</h3><div class="ant-camino">' + g.xs.map(function (x, j) {
        return (j ? '<span class="ant-lin" aria-hidden="true"></span>' : '') + '<div class="ant-p ant-' + x.est + '">' +
          (x.est === 'ahora' ? '<em>Estás acá</em>' : '') +
          '<span class="ant-pc">' + (x.est === 'hecho' ? '✔' : x.est === 'bloq' ? '🔒' : x.ico) + '</span><small>' + esc(x.corto) + '</small></div>';
      }).join('') + '</div></div>';
    }).join('');
  }

  function abrirMapa(temaId) {
    var t = D.temas.filter(function (x) { return x.id === temaId; })[0]; if (!t) return;
    if (esAnt()) {
      var ea = document.createElement('div'); ea.className = 'ap-panel-fondo';
      ea.innerHTML = '<div class="ap-panel ant-panel" role="dialog" aria-label="Mapa de la misión"><h2>' + esc(t.titulo) + '</h2>' + antMapaHtml(t) + '<button class="ap-cerrar" type="button">Cerrar</button></div>';
      document.body.appendChild(ea);
      ea.onclick = function (e) { if (e.target === ea || e.target.closest('.ap-cerrar')) ea.remove(); };
      return;
    }
    var marcado = false;
    function fila(txt, hecho, bloq) {
      var est = hecho ? 'hecho' : bloq ? 'bloq' : (!marcado ? 'ahora' : 'sigue');
      if (!hecho && !bloq && !marcado) marcado = true;
      return '<li class="ap-mp-' + est + '"><span class="ap-mp-i">' + (hecho ? '✔' : est === 'ahora' ? '▶' : bloq ? '🔒' : '○') + '</span><span>' + esc(txt) + (est === 'ahora' ? ' <b>(estás acá)</b>' : '') + '</span></li>';
    }
    var h = '';
    t.niveles.concat(t.generales ? [t.generales] : []).forEach(function (l, i) {
      var esGen = t.generales && l === t.generales;
      var req = l.est.req;
      h += '<div class="ap-mp-nivel"><h3>' + (esGen ? 'Las 4 generales' : 'Nivel ' + (i + 1) + ': ' + esc(l.titulo)) + '</h3><ul>' +
        (l.est.vacia ? '<li class="ap-mp-bloq"><span class="ap-mp-i">…</span><span>En preparación</span></li>'
          : req.map(function (k) { return fila(ROT_PASO[k] || k, hechoK(l, k), l.bloqueada); }).join('')) + '</ul></div>';
    });
    if (t.examen) h += '<div class="ap-mp-nivel"><h3>Nivel jefe</h3><ul>' + fila('Examen corto de la misión', !!t.examen.aprobado, !t.examenDisponible && !t.examen.aprobado) + '</ul></div>';
    var el = document.createElement('div'); el.className = 'ap-panel-fondo';
    el.innerHTML = '<div class="ap-panel" role="dialog" aria-label="Mapa de la misión"><h2>Mapa · ' + esc(t.titulo) + '</h2><p class="ap-sub">Todo lo que vas a hacer en esta misión, en orden.</p>' + h + '<button class="ap-cerrar" type="button">Cerrar</button></div>';
    document.body.appendChild(el);
    el.onclick = function (e) { if (e.target === el || e.target.closest('.ap-cerrar')) el.remove(); };
  }

  // Trayecto Desafío: rendir primero el examen de la misión (una sola oportunidad). Si aprueba, la misión queda saltada.
  function ofertaSalto(t) {
    if (D.saltos && D.saltos[t.id] === 'saltada') return '<div class="ap-salto ok"><b>Misión saltada por examen ✓</b> Ya demostraste que dominás este tema.</div>';
    if (!D.desafio || !t.examen || t.bloqueado || (D.saltos && D.saltos[t.id]) || t.examen.intentos > 0) return '';
    var hizo = t.lecciones.some(function (l) { return l.est && l.est.hechos > 0; });
    if (hizo) return '';
    return '<div class="ap-salto"><div><b>Rendí primero</b><span>Hacé ya el examen de esta misión. Si aprobás, la salteás. Tenés una sola oportunidad: si no aprobás, hacés la misión normal.</span></div>' +
      '<button type="button" class="mt-boton" data-salto="' + t.id + '">Rendir primero</button></div>';
  }

  function pantallaTema(t) {
    var idx = D.temas.indexOf(t), c = tono(idx);
    var nodos = t.niveles.map(function (l, i) { return nodoNivel(l, i, t, false); }).join('') +
      (t.generales ? nodoNivel(t.generales, 0, t, true) : '') +
      (t.examen ? nodoExamen(t) : '') + nodoSiguiente(t, idx);
    vista.innerHTML = '<div class="mt mt-p2" style="--c:' + c + '">' +
      '<div class="mt-escena"><div class="mt-escena-top"><a class="mt-volver claro" href="' + base() + '">' + ico('back', 20, 3) + ' ' + esc(D.materia.name) + '</a>' +
      '<div class="mt-escena-tit"><span>Misión ' + (idx + 1) + '</span><h1>' + esc(t.titulo) + '</h1></div>' +
      '<button type="button" class="ap-mapa-btn" data-mapa="' + t.id + '">🗺 Mapa</button></div>' + (esAnt() ? antAhoraDespues(t) : '') + ofertaSalto(t) + profundizar(t) +
      '<div class="mt-fila"><div class="mt-fila-int">' + nodos + '</div></div></div></div>';
    // arranca en el primer círculo abierto y sin terminar de ESTA misión (nivel 1 si nunca se tocó; si no, donde quedó)
    var fila = vista.querySelector('.mt-fila'), act = vista.querySelector('.mt-nodo.libre');
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

  function pantallaPaso(k, f, esGen, n, total, yaHecho) {
    var u = PASO_UI[k], l = f.l, p = D.pasos[l.id] || {};
    var titulo = u.titulo, sub = u.sub, icono = u.icono;
    if (yaHecho) { // repaso de un paso terminado: se puede volver a ver, sin rehacer la entrega
      var hechoTxt = k === 'carpeta' ? 'Ya entregaste tu carpeta ✓ Podés volver a mirar el PDF.' : 'Ya hiciste este paso ✓ Podés volver a verlo cuando quieras.';
      var kk = k === 'carpeta' ? 'pdf' : k, bt = k === 'carpeta' ? 'VER EL PDF' : u.boton.replace('EMPEZAR', 'VOLVER A HACERLAS');
      return '<div class="rc-cuerpo"><span class="rc-disco" style="--k:#1FB57A">' + ico('check', 56, 3) + '</span>' +
        '<small class="rc-kick">PASO ' + n + ' DE ' + total + '</small><h1>' + esc(titulo) + '</h1><p class="rc-sub">' + esc(hechoTxt) + '</p>' +
        '<div class="rc-pie"><button type="button" class="rc-btn" style="--k:' + u.color + '" data-rc="abrir" data-k="' + kk + '">' + bt + '</button></div></div>';
    }
    if (k === 'final' && esGen) { titulo = 'Las 4 generales'; sub = 'Mezclan todo lo de la misión y repasan lo anterior.'; icono = 'bolt'; }
    var extra = '';
    if (k === 'carpeta') {
      extra = '<div class="ap-barra-cuest"><button type="button" class="ap-tg" data-cp-tg="1" aria-pressed="false">Ver de a una</button></div><div class="rl-top" data-cp-top style="display:none"><span class="rl-cont"></span></div><div class="rc-items">' + p.pdf.carpeta.map(function (x, i) {
        return '<label class="rc-item"><span class="mt-preg-n">' + (i + 1) + '</span><span class="rc-item-c"><span class="rc-consigna">' + esc(consigna(x)) +
          '</span><input type="text" class="rc-in" data-i="' + i + '" maxlength="120" autocomplete="off" placeholder="Tu respuesta"></span></label>';
      }).join('') + '</div><div class="rc-nav" data-cp-nav style="display:none"><button type="button" class="rc-btn" data-cp-n="-1">‹ Anterior</button><button type="button" class="rc-btn" data-cp-n="1">Siguiente ›</button></div>';
    }
    return '<div class="rc-cuerpo"><span class="rc-disco" style="--k:' + u.color + '">' + ico(icono, 56, 2.2) + '</span>' +
      '<small class="rc-kick">PASO ' + n + ' DE ' + total + '</small>' + faltan(n, total) + '<h1>' + esc(titulo) + '</h1><p class="rc-sub">' + esc(sub) + '</p>' + extra +
      '<div class="rc-pie"><button type="button" class="rc-btn" style="--k:' + u.color + '" data-rc="' + (k === 'carpeta' ? 'entregar' : 'abrir') + '" data-k="' + k + '">' + u.boton + '</button></div></div>';
  }

  // ----- Foco: bloques cortos (cuánto falta) y pausa sugerida al terminar cada nivel -----
  function esFoco() { return !!(D && D.adaptaciones && D.adaptaciones.indexOf('foc_bloques') >= 0); }
  function faltan(n, total) {
    if (!esFoco()) return '';
    var q = total - n + 1;
    return '<p class="fb-falta">' + (q === 1 ? 'Este es el último paso del nivel' : 'Te faltan ' + q + ' pasos para terminar el nivel') + '</p>';
  }
  function pausaHtml() {
    if (!esFoco()) return '';
    return '<div class="fb-pausa"><b>Hacé una pausa de 5 minutos</b><span>Tomá agua, estirate o mirá por la ventana. Después volvé.</span>' +
      '<button type="button" class="fb-pausa-b" data-pausa="1">Empezar la pausa</button><output class="fb-reloj" aria-live="off"></output></div>';
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-pausa]');
    if (!b || b.disabled) return;
    var out = b.parentNode.querySelector('.fb-reloj'), resto = 300;
    b.disabled = true;
    function pinta() {
      if (!document.body.contains(out)) return clearInterval(t);
      if (resto <= 0) { clearInterval(t); out.textContent = 'Listo. Cuando quieras, seguí.'; b.textContent = 'Pausa terminada'; return; }
      out.textContent = Math.floor(resto / 60) + ':' + ('0' + (resto % 60)).slice(-2);
      resto--;
    }
    var t = setInterval(pinta, 1000); pinta();
  });

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
      '<p class="rc-sub">Completaste todos los pasos. Se abre lo que sigue.</p>' + pausaHtml() + '<div class="rc-pie">' + boton + '</div></div>';
  }

  function pantallaNivel(f) {
    var l = f.l, t = f.t, esGen = !!t.generales && t.generales.id === l.id;
    var ks = pasosNivel(l);
    var pend = ks.filter(function (k) { return !hechoK(l, k); });
    var hasta = pend.length ? ks.indexOf(pend[0]) : ks.length; // hasta dónde llegó (abre acá)
    var tope = hasta;
    var i = verPaso[l.id] != null && verPaso[l.id] <= tope ? verPaso[l.id] : hasta; // o el paso anterior que eligió mirar
    var segs = ks.concat(['fin']).map(function (k, j) {
      var cls = 'rc-seg ' + (j === i ? 'cur' : j < hasta ? 'on' : '');
      return j <= tope ? '<i class="' + cls + '" data-ver="' + j + '" style="cursor:pointer" title="' + (j < ks.length ? esc(PASO_UI[k].titulo) : 'Final') + '"></i>' : '<i class="' + cls + '"></i>';
    }).join('');
    var nav = '<div class="rc-nav" style="display:flex;justify-content:space-between;gap:10px;margin:8px 0 0">' +
      (i > 0 ? '<button type="button" class="rc-b2" data-ver="' + (i - 1) + '" style="border:0;background:none;font:inherit;font-weight:800;color:var(--c);cursor:pointer;padding:6px 0">‹ Paso anterior</button>' : '<span></span>') +
      (i < tope ? '<button type="button" class="rc-b2" data-ver="' + (i + 1) + '" style="border:0;background:none;font:inherit;font-weight:800;color:var(--c);cursor:pointer;padding:6px 0">' + (i + 1 === hasta ? 'Seguir donde quedé ›' : 'Paso siguiente ›') + '</button>' : '<span></span>') + '</div>';
    var cuerpo = i >= ks.length ? pantallaFin(f, esGen) : pantallaPaso(ks[i], f, esGen, i + 1, ks.length, hechoK(l, ks[i]));
    vista.innerHTML = '<div class="mt mt-rc" style="--c:' + tono(D.temas.indexOf(t)) + '">' +
      '<div class="rc-top"><a class="rc-x" href="' + base() + '/' + t.id + '" aria-label="Volver a la misión">' + ico('close', 22, 3) + '</a><div class="rc-bar">' + segs + '</div></div>' + nav + cuerpo + '</div>';
  }

  // ----- Router interno -----
  var ruta = { tema: null, leccion: null };
  function pintar() {
    if (window.WaveNum) WaveNum.botonHerramientas(/^#materia\//.test(location.hash) && !!D && !!D.adaptaciones && D.adaptaciones.indexOf('num_componentes') >= 0);
    if (!/^#materia\//.test(location.hash)) return; // el alumno ya salió de la materia (ej. «Mis cursos»): no volver a dibujarla encima
    calcular();
    hojaAbierta = null;
    var t = ruta.tema ? D.temas.filter(function (x) { return x.id === ruta.tema; })[0] : null;
    if (t && (t.bloqueado || t.vacio || D.sinAcceso)) { t = null; ruta.leccion = null; location.replace(base()); }
    var f = t && ruta.leccion ? buscarLeccion(ruta.leccion) : null;
    if (f && (f.t.id !== t.id || f.l.bloqueada || f.l.est.vacia)) { f = null; location.replace(base() + '/' + t.id); }
    if (!f) pintar.ult = null;
    else if (pintar.ult !== f.l.id) { delete verPaso[f.l.id]; pintar.ult = f.l.id; } // al entrar a un nivel abre donde quedó
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
    delete verPaso[paso.lesson_id]; // al terminar un paso, sigue donde quedó
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
    if (D.prueba && !hecho(paso) && k !== 'complementary' && k !== 'review') marcar(paso, k === 'final' ? 100 : null); // cuenta de prueba: avanza sin completar
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
        WaveVisor.abrirPdf({ titulo: f.l.titulo + ' · PDF', descargable: true, modoLectura: !!D && (D.adaptaciones || []).indexOf('lec_modo') >= 0, alTerminar: function () { marcar(paso); },
          chat: function (payload) { return llamar('chat-tutor', payload); }, chatCtx: function () { return { lesson_step_id: paso.id }; }, chatConfig: tutorOps('pdf', {}).config,
          url: async function (desc) { return (await llamar('content-access', { action: 'pdf', step_id: paso.id, descarga: !!desc, neutro: !!D.neutro })).url; } });
      } else if (k === 'interactive') {
        var r = await sb.from('lesson_steps').select('content').eq('id', paso.id).maybeSingle();
        if (r.error || !r.data || !r.data.content || !r.data.content.html) throw new Error('No pudimos abrir la actividad.');
        abrirInteractiva(paso, f.l.titulo, r.data.content.html);
      } else if (k === 'final') {
        abrirCuestionario({
          titulo: 'Actividad · ' + f.l.titulo, examen: false, tutor: { lesson_id: paso.lesson_id },
          cargar: function () { return preguntas('lesson_step_id', paso.id); },
          enviar: function (resp) { return llamar('corregir', { modo: 'actividad', lesson_step_id: paso.id, answers: resp }); },
          comprobar: function (q, a, seed) { return llamar('comprobar', { origen: 'actividad', lesson_step_id: paso.id, question_id: q.id, answer: a, seed: seed }); },
          alTerminar: function (res) {
            D.progreso[paso.id] = { score: res.score, estado: 'graded' };
            revisarLeccion(paso.lesson_id).then(refrescar);
          }
        });
      } else if (k === 'review') {
        var intento = null;
        abrirCuestionario({
          titulo: 'Repaso · ' + f.l.titulo, examen: false, repaso: true, tutor: { lesson_id: f.l.id },
          cargando: 'Estamos armando tu repaso…', cargandoSub: 'Son 6 preguntas nuevas, de esta lección y de las anteriores. Tené tu carpeta a mano.',
          cargar: async function () { var d = await llamar('review', { action: 'start', lesson_id: f.l.id }); intento = d.attempt_id; return d.questions; },
          enviar: function (resp) { return llamar('review', { action: 'submit', attempt_id: intento, answers: resp }); },
          comprobar: function (q, a) { return llamar('comprobar', { origen: 'repaso', attempt_id: intento, question_id: q.id, answer: a }); },
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

  // Carpeta: "Ver de a una" (opcional, lo activa el alumno acá mismo)
  function carpetaVer(n) {
    var it = vista.querySelectorAll('.rc-item'), tot = it.length, tg = vista.querySelector('[data-cp-tg]');
    if (!tot || !tg) return;
    var una = !!(window.WaveApoyos && WaveApoyos.get('deAUna'));
    n = Math.max(0, Math.min(tot - 1, n)); vista._cp = n;
    tg.setAttribute('aria-pressed', una ? 'true' : 'false');
    [].forEach.call(it, function (e, k) { e.style.display = (!una || k === n) ? '' : 'none'; });
    var top = vista.querySelector('[data-cp-top]'), nav = vista.querySelector('[data-cp-nav]'), pie = vista.querySelector('.rc-pie');
    if (top) { top.style.display = una ? '' : 'none'; top.querySelector('.rl-cont').textContent = 'Consigna ' + (n + 1) + ' de ' + tot; }
    if (nav) {
      nav.style.display = una ? 'flex' : 'none'; nav.style.marginTop = una ? 'auto' : '';
      nav.querySelector('[data-cp-n="-1"]').style.visibility = n ? '' : 'hidden';
      nav.querySelector('[data-cp-n="1"]').style.display = n < tot - 1 ? '' : 'none';
    }
    if (pie) pie.style.display = (!una || n === tot - 1) ? '' : 'none';
  }
  new MutationObserver(function () {
    if (vista && vista.querySelector('[data-cp-tg]') && !vista.querySelector('[data-cp-tg]')._ok) { vista.querySelector('[data-cp-tg]')._ok = 1; carpetaVer(0); }
  }).observe(document.documentElement, { childList: true, subtree: true });

  // Entrega de la carpeta: se corrige acá, sin IA. Se aprueba con hasta 1 mal; al aprobar se muestran las soluciones.
  async function entregarCarpeta(btn) {
    var f = buscarLeccion(hojaAbierta), paso = f && (D.pasos[f.l.id] || {}).pdf;
    if (!paso) return;
    if (D.prueba) { D.carpeta[paso.id] = true; delete verPaso[f.l.id]; await revisarLeccion(f.l.id); return refrescar(); } // cuenta de prueba: pasa sin responder
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
  async function abrirClase(paso, titulo) { // paso null = introducción de la materia
    var r;
    if (paso) { // el HTML de la clase vive en lesson_step_clases (liviano para las listas); si no está ahí, se busca en el paso (clases viejas)
      r = await sb.from('lesson_step_clases').select(D.neutro ? 'html, neutro:html_neutro' : 'html').eq('step_id', paso.id).maybeSingle();
      if (r.error || !r.data || !r.data.html) r = await sb.from('lesson_steps').select(D.neutro ? 'html:content->>clase_html, neutro:content->>clase_html_neutro' : 'html:content->>clase_html').eq('id', paso.id).maybeSingle();
    } else r = await sb.from('subjects').select(D.neutro ? 'html:intro_clase_html, neutro:intro_clase_html_neutro' : 'html:intro_clase_html').eq('id', D.materia.id).maybeSingle();
    if (r.data && r.data.neutro) r.data.html = r.data.neutro; // versión en español neutro
    if (r.error || !r.data || !r.data.html) throw new Error('No pudimos abrir la clase.');
    var el = document.createElement('div');
    el.className = 'wvp';
    el.innerHTML =
      '<div class="wvp-caja"><div class="wvp-barra"><b class="wvp-titulo">' + esc(titulo) + ' · Clase</b>' +
      '<button type="button" class="wvp-b" data-full="1" aria-label="Pantalla completa" title="Pantalla completa">⛶</button>' +
      '<button type="button" class="wvp-b wvp-x" data-cerrar="1" aria-label="Cerrar">✕</button></div>' +
      '<div class="mt-marco"><iframe title="Clase" allow="autoplay; fullscreen" sandbox="allow-scripts allow-forms"></iframe></div></div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');
    var frame = el.querySelector('iframe');
    frame.srcdoc = calmar(r.data.html);
    if (paso && window.WaveTutor) WaveTutor.flotante(el.querySelector('.wvp-caja'), tutorOps('clase', { lesson_id: paso.lesson_id }));
    function enFull() { return document.fullscreenElement || document.webkitFullscreenElement; }
    function pantallaCompleta() { // API de pantalla completa; si no existe (iPhone), ocupa toda la pantalla y gira en vertical
      var c = el.querySelector('.wvp-caja');
      if (enFull()) { (document.exitFullscreen || document.webkitExitFullscreen).call(document); return; }
      if (el.classList.contains('wvp-full')) { el.classList.remove('wvp-full'); return; }
      var rq = c.requestFullscreen || c.webkitRequestFullscreen;
      if (!rq) { el.classList.add('wvp-full'); return; }
      Promise.resolve(rq.call(c)).then(function () { try { screen.orientation.lock('landscape').catch(function () {}); } catch (_) {} })
        .catch(function () { el.classList.add('wvp-full'); });
    }
    function cerrar() {
      if (enFull()) try { (document.exitFullscreen || document.webkitExitFullscreen).call(document); } catch (_) {}
      window.removeEventListener('message', alMensaje);
      try { frame.contentWindow.postMessage({ tipo: 'wave-clase-stop' }, '*'); } catch (_) {}
      try { window.speechSynthesis && window.speechSynthesis.cancel(); } catch (_) {}
      document.body.classList.remove('wvp-abierto');
      setTimeout(function () { frame.src = 'about:blank'; el.remove(); }, 150);
    }
    function alMensaje(ev) {
      if (ev.source !== frame.contentWindow || !ev.data || ev.data.tipo !== 'wave-clase-fin') return;
      if (paso) marcar(paso); toast(paso ? '¡Clase terminada! 🎉' : '¡Listo! Ahora empezá la misión 1 🚀');
    }
    window.addEventListener('message', alMensaje);
    el.addEventListener('click', function (ev) { if (ev.target.closest('[data-full]')) return pantallaCompleta(); if (ev.target === el || ev.target.closest('[data-cerrar]')) cerrar(); });
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
    frame.srcdoc = calmar(html);
    if (paso && window.WaveTutor) WaveTutor.flotante(el.querySelector('.wvp-caja'), tutorOps('actividad', { lesson_id: paso.lesson_id }));

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
    var r = await sb.from('questions').select('id, prompt, question_type, options, points, position, tiempo_seg, neutro').eq(col, id).order('position');
    if (r.error) throw r.error;
    if (!r.data.length) throw new Error('Todavía no hay preguntas cargadas.');
    if (D && D.neutro) r.data.forEach(function (q) { if (q.neutro && q.neutro.p) q.prompt = q.neutro.p; }); // variante para extranjeros: el enunciado
    return r.data;
  }

  // Pantalla de aviso (Anticipación): cada tipo de pregunta con una línea de texto y una mini-versión dibujada de cómo se responde
  function dmO(l, on) { return '<span class="dm-op' + (on ? ' on' : '') + '">' + l + '</span>'; }
  function dmC(l, on) { return '<span class="dm-chip' + (on ? ' on' : '') + '">' + l + '</span>'; }
  var AVISOS = {
    multiple_choice: { n: 'Elegir una opción', i: '🔘', c: '#087E83', t: 'Tocá la única respuesta correcta.', d: '<div class="dm-q">¿Cuántos lados tiene un triángulo?</div>' + dmO('2') + dmO('3', 1) + dmO('4') },
    true_false: { n: 'Verdadero o falso', i: '✅', c: '#2E8B57', t: 'Decidí si la frase es verdadera o falsa.', d: '<div class="dm-q">El sol sale por el oeste.</div><div class="dm-fila">' + dmO('Verdadero') + dmO('Falso', 1) + '</div>' },
    short_answer: { n: 'Respuesta corta', i: '✏️', c: '#E59A1B', t: 'Escribí la respuesta en una palabra o frase corta.', d: '<div class="dm-q">¿Cómo se llama el resultado de una suma?</div><div class="dm-in">suma</div>' },
    open: { n: 'Respuesta escrita', i: '📝', c: '#7C5CE0', t: 'Explicalo con tus palabras, completo pero sin apuro.', d: '<div class="dm-q">Explicá qué es un ecosistema.</div><div class="dm-in alto">Es un conjunto de seres vivos que viven juntos y se relacionan con su ambiente…</div>' },
    multi_select: { n: 'Marcar varias', i: '☑️', c: '#087E83', t: 'Marcá todas las correctas. Puede haber más de una.', d: '<div class="dm-q">¿Cuáles son números pares?</div><div class="dm-fila">' + dmC('☑ 2', 1) + dmC('☐ 3') + dmC('☑ 4', 1) + dmC('☐ 7') + '</div>' },
    odd_one_out: { n: 'Encontrar el intruso', i: '🕵️', c: '#E4572E', t: 'Elegí lo que no pertenece al grupo.', d: '<div class="dm-fila">' + dmC('perro') + dmC('gato') + dmC('mesa', 1) + dmC('caballo') + '</div>' },
    ordering: { n: 'Ordenar', i: '↕️', c: '#7C5CE0', t: 'Con las flechas ▲ ▼ poné todo en orden.', d: '<div class="dm-q">De menor a mayor:</div><div class="dm-fila">' + dmC('2 ▲▼', 1) + dmC('5 ▲▼') + dmC('9 ▲▼') + '</div>' },
    matching: { n: 'Unir parejas', i: '🔗', c: '#2E8B57', t: 'Elegí la pareja de cada elemento.', d: '<div class="dm-par"><b>Argentina</b><span>→</span>' + dmO('Buenos Aires ▾', 1) + '</div><div class="dm-par"><b>Chile</b><span>→</span>' + dmO('Santiago ▾', 1) + '</div>' },
    classify: { n: 'Clasificar', i: '🗂️', c: '#E59A1B', t: 'Elegí la categoría de cada elemento.', d: '<div class="dm-par"><b>Manzana</b><span>→</span>' + dmO('Fruta ▾', 1) + '</div><div class="dm-par"><b>Zanahoria</b><span>→</span>' + dmO('Verdura ▾', 1) + '</div>' },
    table_fill: { n: 'Completar una tabla', i: '🔢', c: '#087E83', t: 'Escribí lo que falta en las celdas vacías.', d: '<div class="dm-tab"><span>2 × 2</span><span>4</span><span>2 × 3</span><span class="dm-in">6</span></div>' },
    fill_blank: { n: 'Completar huecos', i: '🧩', c: '#E4572E', t: 'Escribí lo que falta en cada hueco.', d: '<div class="dm-q">El agua hierve a <span class="dm-in en">100</span> grados.</div>' },
    solve_complete: { n: 'Resolver y responder', i: '🧮', c: '#7C5CE0', t: 'Contá cómo lo resolviste y poné el resultado.', d: '<div class="dm-q">12 + 8</div><div class="dm-in">Sumé 12 y 8</div><div class="dm-in">Resultado: 20</div>' },
    numeric: { n: 'Escribir un número', i: '🔟', c: '#2E8B57', t: 'Hacé la cuenta (en tu carpeta si querés) y escribí solo el resultado.', d: '<div class="dm-q">6 × 7 = <span class="dm-in en">42</span></div>' },
    tap_text: { n: 'Tocar en el texto', i: '👆', c: '#E59A1B', t: 'Tocá en el texto lo que pide la consigna. Volvé a tocar para sacarlo.', d: '<div class="dm-q">Tocá el sustantivo:</div><div class="dm-q">El <span class="dm-sub">perro</span> corre.</div>' },
    tokens: { n: 'Armar con fichas', i: '🧱', c: '#087E83', t: 'Tocá las fichas en el orden que corresponde.', d: '<div class="dm-fila">' + dmC('el', 1) + dmC('sol', 1) + dmC('brilla', 1) + '</div><div class="dm-in">el sol brilla</div>' },
    keywords: { n: 'Explicar con ideas clave', i: '🔑', c: '#7C5CE0', t: 'Escribí una explicación corta con las ideas importantes.', d: '<div class="dm-q">¿Qué es la fotosíntesis?</div><div class="dm-in alto">La planta usa la <b>luz</b> del sol para fabricar su alimento.</div>' },
    label_image: { n: 'Rotular un dibujo', i: '🏷️', c: '#E4572E', t: 'Elegí el nombre que corresponde a cada punto del dibujo.', d: '<div class="dm-img"><span class="dm-cel"><i></i></span>' + dmO('núcleo ▾', 1) + '</div>' }
  };

  function abrirCuestionario(op) {
    var el = document.createElement('div');
    el.className = 'wvp';
    el.innerHTML = '<div class="wvp-caja"><div class="wvp-barra"><b class="wvp-titulo">' + esc(op.titulo) + '</b>' +
      '<button type="button" class="wvp-b wvp-x" data-cerrar="1" aria-label="Cerrar">✕</button></div>' +
      '<div class="mt-cuest"></div></div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');
    var cuerpo = el.querySelector('.mt-cuest');
    var lista = [], enviando = false, entregado = false, relamp = null, qActual = null;
    // Qué pregunta está mirando el alumno ahora: el tutor la recibe con sus opciones visibles (nunca la respuesta)
    function preguntaTutor() {
      var q = qActual; if (!q) return {};
      var o = q.options, vis = '';
      if (Array.isArray(o)) vis = ' Opciones: ' + o.map(String).join(' / ');
      else if (o && (o.elementos || o.izquierda || o.columnas)) vis = ' ' + JSON.stringify(o.elementos ? { elementos: o.elementos, categorias: o.categorias } : o.izquierda ? { izquierda: o.izquierda, derecha: o.derecha } : { columnas: o.columnas });
      var r = { pregunta_texto: (pr(q) + vis).slice(0, 600) };
      if (!(o && o.vars)) r.question_id = q.id; // con números al azar la respuesta depende del sorteo: no se la damos
      return r;
    }
    if (op.tutor && !op.examen && window.WaveTutor) WaveTutor.flotante(el.querySelector('.wvp-caja'), tutorOps('actividad', function () { return Object.assign({}, op.tutor, preguntaTutor()); }));
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
      var tg = ev.target.closest('[data-ap]');
      if (tg) { var kk = tg.getAttribute('data-ap'); if (window.WaveApoyos) WaveApoyos.set(kk, !WaveApoyos.get(kk)); pintarToggles(); verConsigna(cuerpo._cn || 0); return; }
      var cb = ev.target.closest('[data-comprobar]'); if (cb) { comprobar(Number(cb.getAttribute('data-comprobar')), cb); return; }
      if (ev.target.closest('[data-sincrono]')) { if (window.WaveApoyos) WaveApoyos.set('sinCrono', !WaveApoyos.get('sinCrono')); formulario(); return; }
      var cn = ev.target.closest('[data-cn]'); if (cn) { verConsigna((cuerpo._cn || 0) + Number(cn.getAttribute('data-cn'))); return; }
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
        var der = listaOp(o.derecha).slice();
        if (!/\[\[memorama\]\]/.test(pr(q))) { // mezcla fija por pregunta: la pareja no queda en la misma posición (el memorama necesita el orden original)
          var sm = 0; String(q.id || pr(q)).split('').forEach(function (ch) { sm = (sm * 31 + ch.charCodeAt(0)) >>> 0; });
          for (var mm = der.length - 1; mm > 0; mm--) { sm = (sm * 1103515245 + 12345) >>> 0; var rr = sm % (mm + 1), tm = der[mm]; der[mm] = der[rr]; der[rr] = tm; }
        }
        return enun + '<small class="mt-ayuda">Elegí la pareja de cada elemento.</small><div class="mt-pares">' + listaOp(o.izquierda).map(function (x, k) {
          return '<div class="mt-par"><span>' + esc(x) + '</span>' + selectDe(i, k, der) + '</div>';
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
        var ops = (q.options || []).slice();
        if (q.question_type === 'multiple_choice') { // mezcla fija por pregunta: la correcta no queda siempre primera
          var sem = 0; String(q.id || pr(q)).split('').forEach(function (ch) { sem = (sem * 31 + ch.charCodeAt(0)) >>> 0; });
          for (var m = ops.length - 1; m > 0; m--) { sem = (sem * 1103515245 + 12345) >>> 0; var r = sem % (m + 1), tmp = ops[m]; ops[m] = ops[r]; ops[r] = tmp; }
        }
        h += ops.map(function (o, j) {
          return '<label class="mt-op"><input type="radio" name="q' + i + '" value="' + esc(o) + '"><span>' + esc(o) + '</span></label>';
        }).join('');
        if (op.justificar) h += '<div class="ap-just"><label>¿Por qué elegiste esa respuesta?</label><textarea class="mt-just" data-just="' + i + '" rows="2" maxlength="500" placeholder="Explicalo con tus palabras"></textarea></div>';
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
    function justif(i) { var t = cuerpo.querySelector('[data-just="' + i + '"]'); return t ? t.value.trim() : undefined; }
    function mostrarResp(q, a) { return window.WaveTipos && WaveTipos.soporta(q.question_type) ? WaveTipos.mostrar(q, a) : a; }

    function ap(k) { return !!(window.WaveApoyos && WaveApoyos.get(k)); }
    function pintarToggles() {
      [].forEach.call(cuerpo.querySelectorAll('[data-ap]'), function (b) { b.setAttribute('aria-pressed', ap(b.getAttribute('data-ap')) ? 'true' : 'false'); });
      cuerpo.classList.toggle('ap-ver-comp', ap('comprobar'));
    }
    function compHtml(i) {
      return '<div class="ap-comp"><button type="button" class="mt-boton suave" data-comprobar="' + i + '">Comprobar</button><div class="ap-comp-res" aria-live="polite"></div></div>';
    }
    function formulario() {
      sembrar();
      if (relamp) clearInterval(relamp.t);
      relamp = null;
      if (!ap('sinCrono') && lista.some(function (q) { return q.tiempo_seg; })) { relampago(); return; }
      var barra = '<div class="ap-barra-cuest"><button type="button" class="ap-tg" data-ap="deAUna" aria-pressed="false">Ver de a una</button>' +
        (lista.some(function (q) { return q.tiempo_seg; }) ? '<button type="button" class="ap-tg" data-sincrono="1" aria-pressed="true">Sin cronómetro</button>' : '') +
        (op.comprobar ? '<button type="button" class="ap-tg" data-ap="comprobar" aria-pressed="false">Comprobar cada respuesta</button>' : '') + '</div>';
      // Todas las consignas quedan armadas (así se entregan juntas). Se muestran todas o de a una, a elección del alumno.
      cuerpo.innerHTML = barra + '<div class="rl-top" data-cn-top><span class="rl-cont"></span></div>' + lista.map(function (q, i) {
        var h = campo(q, i), k = h.lastIndexOf('</div></div>');
        return op.comprobar && k > 0 ? h.slice(0, k) + compHtml(i) + h.slice(k) : h;
      }).join('') +
        '<div class="mt-cuest-pie" style="display:flex;justify-content:space-between;gap:12px">' +
        '<button type="button" class="mt-boton" data-cn="-1" style="background:transparent;color:inherit;box-shadow:none;border:2px solid currentColor;opacity:.75">‹ Anterior</button>' +
        '<button type="button" class="mt-boton" data-cn="1">Siguiente ›</button>' +
        '<button type="button" class="mt-boton" data-enviar="1">Entregar</button></div>';
      pintarToggles();
      verConsigna(0);
    }
    function verConsigna(n) {
      var ps = cuerpo.querySelectorAll(':scope > .mt-preg'), tot = ps.length, una = ap('deAUna');
      if (!tot) return;
      n = Math.max(0, Math.min(tot - 1, n)); cuerpo._cn = n; qActual = lista[n] || null;
      [].forEach.call(ps, function (p, k) { p.style.display = (!una || k === n) ? '' : 'none'; });
      var top = cuerpo.querySelector('[data-cn-top] .rl-cont'); if (top) top.textContent = una ? 'Consigna ' + (n + 1) + ' de ' + tot : tot + (tot === 1 ? ' consigna' : ' consignas');
      var ant = cuerpo.querySelector('[data-cn="-1"]'), sig = cuerpo.querySelector('[data-cn="1"]'), env = cuerpo.querySelector('[data-enviar]');
      if (ant) { ant.style.display = una ? '' : 'none'; ant.style.visibility = n ? '' : 'hidden'; }
      if (sig) sig.style.display = una && n < tot - 1 ? '' : 'none';
      if (env) env.style.display = (!una || n === tot - 1) ? '' : 'none';
      cuerpo.scrollTo(0, 0);
    }

    // Comprobar una respuesta al instante: queda bloqueada y cuenta como la respuesta del alumno
    async function comprobar(i, btn) {
      var q = lista[i], blk = cuerpo.querySelectorAll(':scope > .mt-preg')[i]; if (!q || !blk) return;
      var res = blk.querySelector('.ap-comp-res'), a = leerResp(q, i);
      if (!String(a).trim()) { res.textContent = 'Primero escribí o elegí tu respuesta.'; return; }
      btn.disabled = true; res.textContent = 'Comprobando…';
      try {
        var r = await op.comprobar(q, a, q._seed);
        if (r.pendiente) res.innerHTML = '<b>Respuesta guardada.</b> Esta consigna se corrige al entregar.';
        else {
          var s = Number(r.score);
          res.className = 'ap-comp-res ' + (s >= 100 ? 'ok' : s > 0 ? 'med' : 'no');
          res.innerHTML = '<b>' + (s >= 100 ? '✔ Correcta' : s > 0 ? '◐ A medias' : '✘ Incorrecta') + '</b> ' + esc(r.feedback || '');
          if (window.WaveJuego) WaveJuego.respuesta(s >= 100, blk);
        }
        var c = blk.querySelector('.mt-preg-c');
        [].forEach.call(c.children, function (ch) { if (!ch.classList.contains('ap-comp')) ch.inert = true; });
        btn.hidden = true;
      } catch (e) {
        res.textContent = (e && e.message) || 'No se pudo comprobar. Probá de nuevo.'; btn.disabled = false;
      }
    }

    // Modo Relámpago: una pregunta por vez, con cronómetro. Si se acaba el tiempo pasa sola a la siguiente.
    function relampago() {
      relamp = { i: 0, resp: [], t: null };
      mostrarRel();
    }
    function mostrarRel() {
      var i = relamp.i, q = lista[i], seg = q.tiempo_seg || 20, resto = seg; qActual = q; relamp.t0 = Date.now();
      cuerpo.innerHTML = '<div class="rl-top"><span class="rl-cont">Pregunta ' + (i + 1) + ' de ' + lista.length + '</span><span class="rl-seg"><b>' + seg + '</b> s</span></div>' +
        '<div class="rl-barra"><i style="animation-duration:' + seg + 's"></i></div>' + campo(q, i) +
        '<div class="ap-barra-cuest"><button type="button" class="ap-tg" data-sincrono="1" aria-pressed="false">Sin cronómetro</button></div>' +
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
      (relamp.tiempos = relamp.tiempos || []).push((Date.now() - relamp.t0) / 1000);
      relamp.resp.push({ question_id: q.id, answer: leerResp(q, i), seed: q._seed, justificacion: op.justificar ? justif(i) : undefined });
      relamp.i++;
      if (relamp.i < lista.length) mostrarRel(); else enviar(relamp.resp);
    }

    async function enviar(pre) {
      var resp = pre || lista.map(function (q, i) { return { question_id: q.id, answer: leerResp(q, i), seed: q._seed, justificacion: op.justificar ? justif(i) : undefined }; });
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
      if (window.WaveJuego) WaveJuego.resultado(cuerpo, { nota: nota, ok: ok, examen: !!op.examen, scores: lista.map(function (q) { return Math.round((porId[q.id] || {}).score || 0); }),
        tiempos: relamp && relamp.tiempos, limites: lista.map(function (q) { return q.tiempo_seg || 20; }) });
    }

    // Trayecto Anticipación: antes de cada actividad, una pantalla que dice qué viene, qué hay que hacer en cada tipo de pregunta y cómo saber que terminó
    function conAviso() { return !!(D.adaptaciones && D.adaptaciones.indexOf('ant_aviso') >= 0 && lista.length); }
    function avisoPrevio() {
      var vistos = {}; try { vistos = JSON.parse(localStorage.getItem('wave-avisos-' + D.sid) || '{}'); } catch (e) { vistos = {}; }
      var tipos = [], cuenta = {};
      lista.forEach(function (q) { var k = AVISOS[q.question_type] ? q.question_type : 'open'; if (!cuenta[k]) { cuenta[k] = 0; tipos.push(k); } cuenta[k]++; });
      var rel = lista.some(function (q) { return q.tiempo_seg; }) && !ap('sinCrono');
      var nuevos = tipos.filter(function (k) { return !vistos[k]; }), conocidos = tipos.filter(function (k) { return vistos[k]; });
      var h = '<div class="ap-aviso"><h2>Antes de empezar</h2><div class="av-chips">' +
        '<span class="av-chip">📋 ' + lista.length + (lista.length === 1 ? ' pregunta' : ' preguntas') + '</span>' +
        '<span class="av-chip">' + (rel ? '⏱️ Con tiempo (se puede sacar)' : '🐢 Sin apuro, a tu ritmo') + '</span>' +
        '<span class="av-chip">🏁 Al final ves tu resultado</span></div>';
      if (nuevos.length) h += '<p class="av-sub">Así se responde cada tipo de pregunta:</p><div class="av-grilla">' + nuevos.map(function (k) { var a = AVISOS[k];
        return '<div class="av-card" style="--c:' + a.c + '"><div class="av-cab"><span>' + a.i + '</span><b>' + esc(a.n) + '</b><small>' + cuenta[k] + (cuenta[k] === 1 ? ' pregunta' : ' preguntas') + '</small></div>' +
          '<p>' + esc(a.t) + '</p><div class="av-demo" aria-hidden="true">' + a.d + '</div></div>'; }).join('') + '</div>';
      if (conocidos.length) h += '<p class="av-conoc">Ya conocés: ' + conocidos.map(function (k) { return AVISOS[k].i + ' ' + esc(AVISOS[k].n); }).join(' · ') + '</p>';
      h += '<button type="button" class="mt-boton av-ok" data-avisook="1">¡Listo, empezar!</button></div>';
      cuerpo.innerHTML = h;
      cuerpo.querySelector('[data-avisook]').addEventListener('click', function () {
        tipos.forEach(function (k) { vistos[k] = 1; });
        try { localStorage.setItem('wave-avisos-' + D.sid, JSON.stringify(vistos)); } catch (e) { /* sin almacenamiento */ }
        formulario();
      });
    }
    function traer() {
      entregado = false; if (window.WaveJuego) WaveJuego.reiniciar();
      cuerpo.innerHTML = '<div class="mt-cuest-estado">' + (op.cargando ? '<div class="mt-girar"></div><b>' + esc(op.cargando) + '</b><small>' + esc(op.cargandoSub || '') + '</small>' : 'Cargando…') + '</div>';
      op.cargar().then(function (qs) { lista = qs; if (conAviso()) avisoPrevio(); else formulario(); }).catch(function (e) {
        cuerpo.innerHTML = '<div class="mt-cuest-estado error"><b>' + esc(e.message || 'No se pudo cargar.') + '</b></div>';
      });
    }
    traer();
  }

  function abrirExamen(temaId, salto) {
    var t = D.temas.filter(function (x) { return x.id === temaId; })[0];
    if (!t || !t.examen) return;
    if (salto && (!D.desafio || (D.saltos && D.saltos[t.id]) || t.examen.intentos > 0)) { toast('Ya no podés rendir primero esta misión.', true); return; }
    if (!salto && !t.examenDisponible) { toast('Primero superá todos los niveles de la misión.', true); return; }
    var sorteo = null; // cada vez que se abre, el examen sortea preguntas distintas del banco del tema
    abrirCuestionario({
      titulo: (salto ? 'Rendir primero · ' : 'Nivel jefe · ') + t.titulo, examen: true, justificar: !!salto,
      cargar: async function () {
        var r = await sb.rpc('sortear_examen', { p_exam: t.examen.id });
        if (r.error) throw new Error(r.error.message || 'No se pudo armar el examen.');
        sorteo = r.data.sorteo_id || null;
        if (!r.data.questions || !r.data.questions.length) throw new Error('Todavía no hay preguntas cargadas.');
        return r.data.questions;
      },
      enviar: function (resp) { return salto ? llamar('salto', { exam_id: t.examen.id, answers: resp, sorteo_id: sorteo }) : llamar('corregir', { modo: 'examen', exam_id: t.examen.id, answers: resp, sorteo_id: sorteo }); },
      comprobar: salto ? null : function (q, a, seed) { return llamar('comprobar', { origen: 'examen', exam_id: t.examen.id, sorteo_id: sorteo, question_id: q.id, answer: a, seed: seed }); },
      alTerminar: function (res) {
        t.examen.mejor = Math.max(t.examen.mejor || 0, res.score);
        t.examen.intentos = (t.examen.intentos || 0) + 1;
        if (res.passed) t.examen.aprobado = true;
        if (salto) { D.saltos[t.id] = res.salto || (res.passed ? 'saltada' : 'no_aprobada'); toast(res.passed ? '¡Misión saltada! Pasás directo a la siguiente.' : 'No alcanzó para saltarla. Hacé la misión normal: ¡vas a poder!', !res.passed); }
        refrescar();
      }
    });
  }

  // ---------- Biblio-videoteca: recursos opcionales de la materia (las actividades solo las ven los alumnos con Desafío) ----------
  function ytId(u) { var m = /(?:youtu\.be\/|[?&]v=|embed\/)([A-Za-z0-9_-]{6,15})/.exec(String(u || '')); return m ? m[1] : null; }
  // Página más del panel (menú «Biblioteca»), con filtros por nivel, año, materia y misión. Nada de esto es obligatorio.
  async function abrirBiblioteca(raiz, pre) {
    pre = pre || {};
    raiz.innerHTML = '<div class="bib-pag"><h1 class="vista-titulo">Biblio-videoteca</h1><p class="bib-sub">Recursos opcionales por si querés ver más o algo no te quedó claro.</p><div class="bib-filtros"></div><div class="bib-cont">Cargando…</div></div>';
    var f = raiz.firstChild;
    var cont = f.querySelector('.bib-cont'), fil = f.querySelector('.bib-filtros');
    f.addEventListener('click', function (ev) {
      var v = ev.target.closest('[data-bib-ver]');
      if (v) { var c = document.createElement('div'); c.className = 'bib-player'; c.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + encodeURIComponent(v.getAttribute('data-bib-ver')) + '?autoplay=1&rel=0" title="Video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>'; v.replaceWith(c); }
    });
    var r = await Promise.all([
      sb.from('biblioteca_items').select('id, tipo, titulo, descripcion, url, subject_id, topic_id').order('created_at'),
      sb.from('levels').select('id, name, position').order('position'),
      sb.from('grades').select('id, level_id, year_number, name').order('year_number'),
      sb.from('subjects').select('id, grade_id, name, variant').limit(1000),
      sb.from('topics').select('id, subject_id, title, position').order('position').limit(3000),
      sb.from('students').select('trayectos_apoyo').limit(50)
    ]);
    if (r[0].error) { cont.textContent = 'No se pudo cargar. Probá de nuevo.'; return; }
    var desafio = (r[5].data || []).some(function (x) { return (x.trayectos_apoyo || []).indexOf('desafio') >= 0; });
    var items = (r[0].data || []).filter(function (x) { return x.tipo !== 'actividad' || desafio; });
    var niv = {}, gr = {}, mat = {}, top = {};
    (r[1].data || []).forEach(function (x) { niv[x.id] = x; });
    (r[2].data || []).forEach(function (x) { gr[x.id] = x; });
    (r[3].data || []).forEach(function (x) { mat[x.id] = x; });
    (r[4].data || []).forEach(function (x) { top[x.id] = x; });
    items = items.filter(function (x) { return mat[x.subject_id]; });
    var F = { nivel: '', grado: '', materia: pre.materia || '', mision: pre.mision || '' };
    var m0 = mat[F.materia]; if (m0 && gr[m0.grade_id]) { F.grado = m0.grade_id; F.nivel = gr[m0.grade_id].level_id; }
    var nomMat = function (m) { return m.name + (m.variant ? ' · ' + m.variant : ''); };
    var nomGr = function (g) { return g.name || ('Año ' + g.year_number); };
    function opts(lista, sel, todos) { return '<option value="">' + todos + '</option>' + lista.map(function (o) { return '<option value="' + esc(o[0]) + '"' + (o[0] === sel ? ' selected' : '') + '>' + esc(o[1]) + '</option>'; }).join(''); }
    function pasa(x, hasta) {
      var m = mat[x.subject_id], g = gr[m.grade_id];
      if (F.nivel && (!g || g.level_id !== F.nivel)) return false;
      if (hasta === 'nivel') return true;
      if (F.grado && m.grade_id !== F.grado) return false;
      if (hasta === 'grado') return true;
      if (F.materia && x.subject_id !== F.materia) return false;
      if (hasta === 'materia') return true;
      if (F.mision && x.topic_id !== F.mision) return false;
      return true;
    }
    function uniq(lista, fn) { var v = {}, o = []; lista.forEach(function (x) { var p = fn(x); if (p && !v[p[0]]) { v[p[0]] = 1; o.push(p); } }); return o; }
    function pintar() {
      var n = uniq(items, function (x) { var g = gr[mat[x.subject_id].grade_id], l = g && niv[g.level_id]; return l ? [l.id, l.name] : null; });
      var g = uniq(items.filter(function (x) { return pasa(x, 'nivel'); }), function (x) { var q = gr[mat[x.subject_id].grade_id]; return q ? [q.id, nomGr(q)] : null; });
      var m = uniq(items.filter(function (x) { return pasa(x, 'grado'); }), function (x) { return [x.subject_id, nomMat(mat[x.subject_id])]; });
      var t = uniq(items.filter(function (x) { return pasa(x, 'materia') && x.topic_id && top[x.topic_id]; }), function (x) { return [x.topic_id, top[x.topic_id].title]; });
      fil.innerHTML = '<select data-f="nivel" aria-label="Nivel">' + opts(n, F.nivel, 'Todos los niveles') + '</select>' +
        '<select data-f="grado" aria-label="Año">' + opts(g, F.grado, 'Todos los años') + '</select>' +
        '<select data-f="materia" aria-label="Materia">' + opts(m, F.materia, 'Todas las materias') + '</select>' +
        '<select data-f="mision" aria-label="Misión">' + opts(t, F.mision, 'Todas las misiones') + '</select>';
      var xs = items.filter(function (x) { return pasa(x); });
      if (!xs.length) { cont.innerHTML = '<p class="bib-vacio">No hay recursos con estos filtros todavía.</p>'; return; }
      cont.innerHTML = [['video', 'Videos'], ['texto', 'PDF y lecturas'], ['actividad', 'Actividades para vos']].map(function (gp) {
        var ys = xs.filter(function (x) { return x.tipo === gp[0]; });
        if (!ys.length) return '';
        return '<h3>' + gp[1] + '</h3><div class="bib-lista">' + ys.map(function (x) {
          var id = x.tipo === 'video' ? ytId(x.url) : null;
          var cab = id ? '<button type="button" class="bib-thumb" data-bib-ver="' + esc(id) + '" aria-label="Ver el video"><img src="https://i.ytimg.com/vi/' + esc(id) + '/hqdefault.jpg" alt="" loading="lazy"><span>▶</span></button>' : '';
          var ms = mat[x.subject_id];
          return '<div class="bib-item">' + cab + '<div class="bib-tx"><b>' + esc(x.titulo) + '</b><small>' + esc(nomMat(ms)) + (x.topic_id && top[x.topic_id] ? ' · ' + esc(top[x.topic_id].title) : '') + '</small>' + (x.descripcion ? '<p>' + esc(x.descripcion) + '</p>' : '') +
            (!id ? '<a class="bib-abrir" href="' + esc(x.url) + '" target="_blank" rel="noopener">Abrir</a>' : '') + '</div></div>';
        }).join('') + '</div>';
      }).join('');
    }
    fil.addEventListener('change', function (ev) {
      var k = ev.target.getAttribute('data-f'); if (!k) return;
      F[k] = ev.target.value;
      if (k === 'nivel') { F.grado = ''; F.materia = ''; F.mision = ''; }
      if (k === 'grado') { F.materia = ''; F.mision = ''; }
      if (k === 'materia') F.mision = '';
      pintar();
    });
    pintar();
  }

  // Solo Desafío: al terminar una misión, la puerta a la biblioteca para seguir profundizando
  function profundizar(t) {
    if (!D.desafio || !t.completo) return '';
    return '<div class="ap-salto ok"><div><b>Seguir profundizando</b><span>Misión cumplida. Si querés ir más lejos en este tema, mirá la biblio-videoteca.</span></div>' +
      '<button type="button" class="mt-boton" data-biblio="1" data-bib-materia="' + esc(D.materia.id) + '" data-bib-mision="' + esc(t.id) + '">Seguir profundizando</button></div>';
  }
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest('[data-biblio]');
    if (!b) return;
    ev.preventDefault();
    var m = b.getAttribute('data-bib-materia') || '', t = b.getAttribute('data-bib-mision') || '';
    location.hash = '#biblioteca' + (m ? '/' + m + (t ? '/' + t : '') : '');
  });

  // ---------- Introducción ----------
  function abrirIntro() {
    if (D.materia.intro_clase) return abrirClase(null, 'Introducción · ' + D.materia.name).catch(function (e) { toast(e.message || 'No se pudo abrir.', true); });
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
      var ct = ev.target.closest('[data-cp-tg]');
      if (ct) { if (window.WaveApoyos) WaveApoyos.set('deAUna', !WaveApoyos.get('deAUna')); return carpetaVer(vista._cp || 0); }
      var cn = ev.target.closest('[data-cp-n]');
      if (cn) return carpetaVer((vista._cp || 0) + Number(cn.getAttribute('data-cp-n')));
      var mp = ev.target.closest('[data-mapa]');
      if (mp) return abrirMapa(mp.getAttribute('data-mapa'));
      var rc = ev.target.closest('[data-rc]');
      if (rc) {
        var a = rc.getAttribute('data-rc');
        if (a === 'abrir') return abrirPaso(rc.getAttribute('data-k'));
        if (a === 'entregar') return entregarCarpeta(rc);
        if (a === 'continuar') return refrescar();
      }
      var vp = ev.target.closest('[data-ver]');
      if (vp && hojaAbierta) { verPaso[hojaAbierta] = +vp.getAttribute('data-ver'); return refrescar(); }
      var vd = ev.target.closest('[data-video]');
      if (vd) return abrirVideoMision(ruta.tema, vd.getAttribute('data-video'));
      var sl = ev.target.closest('[data-salto]');
      if (sl) { if (window.confirm('Tenés UNA sola oportunidad para rendir primero esta misión. Si aprobás, la salteás; si no, la hacés normal. ¿Empezamos?')) abrirExamen(sl.getAttribute('data-salto'), true); return; }
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
    if (D && D.materia.id === materiaId) {
      pintar();
      // si los datos tienen más de 1 minuto, se vuelven a leer en segundo plano (así aparecen las clases nuevas sin recargar)
      if (Date.now() - (D.leido || 0) > 60000 && !document.querySelector('.wvp')) cargar(materiaId).then(function (d) { if (D && D.materia.id === materiaId) { d.leido = Date.now(); D = d; pintar(); } }).catch(function () {});
      return;
    }
    vista.innerHTML = '<div class="mt"><div class="mt-vacio">Cargando tu materia…</div></div>';
    try {
      var datos = await cargar(materiaId);
      datos.leido = Date.now(); D = datos;
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

  window.WaveMateria = { abrir: abrir, biblioteca: abrirBiblioteca, _probar: _probar, _cuest: abrirCuestionario };
})();
