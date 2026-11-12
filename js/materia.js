// Pantalla de materia del alumno, estilo Simply Piano:
// Introducción + un rectángulo por tema, con las lecciones en círculos. Cada círculo abre sus recuadros de archivos.
(function () {
  var sb = Wave.sb;
  var vista = null;
  var D = null;          // datos de la materia abierta
  var hojaAbierta = null; // id de la lección cuyo detalle está abierto

  var CLAVES = ['video', 'pdf', 'interactive', 'final'];
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
    star: '<path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z" fill="currentColor"/>',
    chevron: '<path d="M9 6l6 6-6 6"/>',
    back: '<path d="M15 6l-6 6 6 6"/>',
    close: '<path d="M6 6l12 12M18 6L6 18"/>',
    down: '<path d="M12 4v11m0 0l-4-4m4 4l4-4M5 20h14"/>',
    dots: '<path d="M6 12h.01M12 12h.01M18 12h.01"/>'
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

    var tem = await sb.from('topics').select('id, title, position, lessons(id, title, position)').eq('subject_id', materiaId).order('position');
    if (tem.error) throw tem.error;
    var temas = tem.data.map(function (t) {
      return { id: t.id, titulo: t.title, posicion: t.position,
        lecciones: (t.lessons || []).slice().sort(function (a, b) { return a.position - b.position; })
          .map(function (l) { return { id: l.id, titulo: l.title, tema: t.id }; }) };
    }).sort(function (a, b) { return a.posicion - b.posicion; });

    var pasos = await sb.from('lesson_steps')
      .select('id, lesson_id, step_type, title, stream_uid, r2_key, kind:content->>kind, files:content->files, lessons!inner(topics!inner(subject_id))')
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
      var tiene = k === 'video' ? !!p.stream_uid
        : k === 'pdf' ? !!p.r2_key
        : k === 'interactive' ? p.kind === 'html'
        : k === 'complementary' ? (Array.isArray(p.files) && p.files.length > 0)
        : !!conPreg[p.id];
      (porLeccion[p.lesson_id] = porLeccion[p.lesson_id] || {})[k] = {
        id: p.id, lesson_id: p.lesson_id, step_type: p.step_type, titulo: p.title, tiene: tiene,
        files: k === 'complementary' && Array.isArray(p.files) ? p.files : []
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

    var sus = await sb.from('subscriptions').select('status').eq('student_id', sid);
    var susOk = !sus.error && (sus.data || []).some(function (x) { return x.status === 'active' || x.status === 'past_due'; });

    return {
      sid: sid, materia: mat.data, temas: temas, pasos: porLeccion, progreso: progreso, hechas: hechas, examen: examen,
      sinAcceso: !susOk || (temas.some(function (t) { return t.lecciones.length; }) && !pasos.data.length)
    };
  }

  // ---------- Estados ----------
  function hecho(p) {
    var pr = D.progreso[p.id];
    if (!pr) return false;
    return p.step_type === 'final_activity' ? pr.estado === 'graded' : true;
  }

  function estadoLeccion(l) {
    var p = D.pasos[l.id] || {};
    var req = CLAVES.filter(function (k) { return p[k] && p[k].tiene; });
    var hs = req.filter(function (k) { return hecho(p[k]); }).length;
    return { total: req.length, hechos: hs, vacia: req.length === 0, completa: req.length > 0 && hs === req.length,
      frac: req.length ? hs / req.length : 0, req: req };
  }

  function calcular() {
    var previoOk = true, actual = null;
    D.temas.forEach(function (t) {
      t.bloqueado = !previoOk || D.sinAcceso;
      var ok = true;
      t.lecciones.forEach(function (l) {
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
      t.vacio = !D.sinAcceso && todasVacias && !t.examen;
      t.completo = !t.vacio && ok && t.lecciones.length > 0 && (!t.examen || t.examen.aprobado);
      if (t.examenDisponible && !t.examen.aprobado && !actual) actual = 'examen:' + t.id;
      t.hechas = t.lecciones.filter(function (l) { return l.est.completa; }).length;
      t.conContenido = t.lecciones.filter(function (l) { return !l.est.vacia; }).length;
      previoOk = previoOk && (t.vacio || t.completo);
    });
    D.actual = actual;
  }

  // ---------- Pantalla de la materia ----------
  function aro(frac, grande) {
    var r = 44, c = 2 * Math.PI * r, f = Math.max(0, Math.min(1, frac || 0));
    return '<svg class="mt-anillo" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="' + r + '" class="mt-pista"/>' +
      (f > 0 ? '<circle cx="50" cy="50" r="' + r + '" class="mt-avance" stroke-dasharray="' + (c * f).toFixed(1) + ' ' + c.toFixed(1) + '" transform="rotate(-90 50 50)"/>' : '') + '</svg>';
  }

  function nodoLeccion(l, i) {
    var e = l.est, cls, contenido, ayuda = '';
    if (l.bloqueada && !e.vacia) { cls = 'bloq'; contenido = ico('lock', 30, 2.6); }
    else if (e.vacia) { cls = 'pronto'; contenido = ico('dots', 30, 3.2); }
    else if (e.completa) { cls = 'hecha'; contenido = ico('check', 38, 3.4); }
    else { cls = 'libre' + (D.actual === l.id ? ' actual' : ''); contenido = '<span class="mt-num">' + (i + 1) + '</span>'; }
    var burbuja = D.actual === l.id ? '<span class="mt-burbuja">¡Empezá!</span>' : '';
    return '<button type="button" class="mt-nodo ' + cls + '" data-leccion="' + l.id + '" aria-label="' + esc(l.titulo) + '">' +
      burbuja + '<span class="mt-aro">' + aro(e.completa ? 1 : e.frac) + '<span class="mt-disco">' + contenido + '</span></span>' +
      '<span class="mt-nombre">' + esc(l.titulo) + '</span>' + ayuda + '</button>';
  }

  function nodoExamen(t) {
    var ex = t.examen, cls, contenido;
    if (ex.aprobado) { cls = 'hecha'; contenido = ico('star', 34, 1.5); }
    else if (t.examenDisponible) { cls = 'libre actual'; contenido = ico('star', 34, 1.5); }
    else { cls = 'bloq'; contenido = ico('lock', 30, 2.6); }
    var burbuja = t.examenDisponible && !ex.aprobado && D.actual === 'examen:' + t.id ? '<span class="mt-burbuja">¡Examen!</span>' : '';
    return '<button type="button" class="mt-nodo examen ' + cls + '" data-examen="' + t.id + '" aria-label="Examen del tema">' +
      burbuja + '<span class="mt-aro">' + aro(ex.aprobado ? 1 : 0) + '<span class="mt-disco">' + contenido + '</span></span>' +
      '<span class="mt-nombre">Examen' + (ex.aprobado && ex.mejor != null ? ' · ' + Math.round(ex.mejor) : '') + '</span></button>';
  }

  function htmlTema(t, i) {
    var estado = t.vacio ? 'pronto' : t.bloqueado ? 'bloq' : t.completo ? 'hecho' : '';
    var chip = t.vacio ? '<span class="mt-chip">Próximamente</span>'
      : t.bloqueado ? '<span class="mt-chip">' + ico('lock', 14, 2.8) + ' Bloqueado</span>'
      : t.completo ? '<span class="mt-chip ok">' + ico('check', 14, 3.2) + ' Completo</span>'
      : '<span class="mt-chip">' + t.hechas + ' de ' + t.conContenido + '</span>';
    var camino = t.lecciones.map(nodoLeccion).join('') + (t.examen ? nodoExamen(t) : '');
    var aviso = t.bloqueado && !D.sinAcceso
      ? '<p class="mt-aviso">' + ico('lock', 16, 2.6) + ' Terminá el tema anterior y aprobá su examen para abrir este.</p>' : '';
    return '<article class="mt-tema ' + estado + '">' +
      '<header class="mt-tema-cab"><div><span class="mt-tema-num">Tema ' + (i + 1) + '</span><h2>' + esc(t.titulo) + '</h2></div>' + chip + '</header>' +
      (t.vacio ? '<p class="mt-pronto-txt">Estamos preparando las lecciones de este tema.</p>' : '<div class="mt-camino">' + camino + '</div>') + aviso + '</article>';
  }

  function pintar() {
    calcular();
    var m = D.materia, color = colorSeguro(m.color);
    var total = D.temas.filter(function (t) { return !t.vacio; }).length;
    var comp = D.temas.filter(function (t) { return t.completo; }).length;
    var pct = total ? Math.round(comp / total * 100) : 0;
    var icono = window.WaveIconos ? WaveIconos.materia(m.name) : '';
    var intro = m.intro_video_uid
      ? '<button type="button" class="mt-intro" data-intro="1"><span class="mt-intro-disco">' + ico('play', 30) + '</span>' +
        '<span class="mt-intro-t"><b>Introducción</b><small>Mirá este video antes de empezar</small></span><span class="mt-intro-flecha">' + ico('chevron', 22, 3) + '</span></button>'
      : '<div class="mt-intro pronto"><span class="mt-intro-disco">' + ico('play', 30) + '</span>' +
        '<span class="mt-intro-t"><b>Introducción</b><small>Próximamente</small></span></div>';
    var banner = D.sinAcceso
      ? '<div class="mt-banner">' + ico('lock', 20, 2.6) + '<span><b>Hay un problema con la suscripción.</b> Para ver el contenido tiene que estar al día. Pedile a tu familia que revise la sección Facturación.</span></div>' : '';
    vista.innerHTML =
      '<div class="mt" style="--c:' + color + '">' +
        '<a class="mt-volver" href="#cursos">' + ico('back', 20, 3) + ' Mis cursos</a>' +
        '<header class="mt-hero"><div class="mt-hero-ico">' + icono + '</div><div class="mt-hero-t"><h1>' + esc(m.name) + '</h1>' +
          '<p>' + comp + ' de ' + total + (total === 1 ? ' tema completo' : ' temas completos') + '</p>' +
          '<div class="mt-hero-barra" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct + '"><span style="width:' + pct + '%"></span></div></div></header>' +
        banner + intro +
        (D.temas.length ? D.temas.map(htmlTema).join('') : '<div class="mt-vacio">Esta materia todavía no tiene temas.</div>') +
      '</div>';
  }

  // ---------- Detalle de la lección (recuadros de archivos) ----------
  var TIPOS = {
    video:         { icono: 'play',   color: '#087E83', titulo: 'Clase explicativa', sub: 'Video de la clase' },
    pdf:           { icono: 'doc',    color: '#E4572E', titulo: 'PDF de la clase', sub: 'Leelo en pantalla o descargalo' },
    interactive:   { icono: 'puzzle', color: '#7C5CE0', titulo: 'Actividad interactiva', sub: 'Practicá jugando' },
    final:         { icono: 'pencil', color: '#E59A1B', titulo: 'Actividad', sub: 'Respondé las consignas' },
    complementary: { icono: 'clip',   color: '#5B7C80', titulo: 'Actividades complementarias', sub: 'Opcional · para practicar más' }
  };
  var ORDEN = ['video', 'pdf', 'interactive', 'final', 'complementary'];

  function buscarLeccion(id) {
    for (var i = 0; i < D.temas.length; i++) for (var j = 0; j < D.temas[i].lecciones.length; j++) {
      if (D.temas[i].lecciones[j].id === id) return { l: D.temas[i].lecciones[j], t: D.temas[i], n: j + 1 };
    }
    return null;
  }

  var hojaEl = null, comp_abierto = false;

  function pintarHoja() {
    if (!hojaAbierta) return;
    var f = buscarLeccion(hojaAbierta);
    if (!f) return cerrarHoja();
    var l = f.l, p = D.pasos[l.id] || {}, e = l.est;
    var color = colorSeguro(D.materia.color);
    var siguiente = null;
    ORDEN.forEach(function (k) { if (!siguiente && k !== 'complementary' && p[k] && p[k].tiene && !hecho(p[k])) siguiente = k; });
    var cards = ORDEN.map(function (k) {
      var t = TIPOS[k], paso = p[k];
      var listo = paso && paso.tiene && k !== 'complementary' && hecho(paso);
      var pr = paso ? D.progreso[paso.id] : null;
      var sub = t.sub, cls = '';
      if (!paso || !paso.tiene) { cls = ' pronto'; sub = 'Próximamente'; }
      else if (listo) { cls = ' hecho'; sub = k === 'final' && pr && pr.score != null ? 'Hecha · nota ' + Math.round(pr.score)
        : k === 'interactive' && pr && pr.score != null ? 'Hecha · ' + Math.round(pr.score) + ' puntos' : 'Hecho'; }
      else if (k === siguiente) cls = ' siguiente';
      var derecha = !paso || !paso.tiene ? '' : listo ? '<span class="mt-rec-check">' + ico('check', 18, 3.6) + '</span>' : '<span class="mt-rec-flecha">' + ico('chevron', 20, 3) + '</span>';
      var tarjeta = '<button type="button" class="mt-rec' + cls + '" data-paso="' + k + '"' + (!paso || !paso.tiene ? ' disabled' : '') + ' style="--k:' + t.color + '">' +
        '<span class="mt-rec-ico">' + ico(t.icono, 26) + '</span><span class="mt-rec-t"><b>' + t.titulo + '</b><small>' + sub + '</small></span>' + derecha + '</button>';
      if (k === 'complementary' && paso && paso.tiene && comp_abierto) {
        tarjeta += '<div class="mt-archivos">' + paso.files.map(function (a, i) {
          return '<div class="mt-archivo"><span class="mt-archivo-n">' + esc(a.name || 'Archivo') + '</span>' +
            '<button type="button" class="mt-desc" data-bajar="' + i + '">' + ico('down', 18, 2.6) + ' Descargar</button></div>';
        }).join('') + '</div>';
      }
      return tarjeta;
    }).join('');
    var estadoTxt = e.completa ? '¡Lección completa!' : e.total ? e.hechos + ' de ' + e.total + ' partes listas' : 'Próximamente';
    hojaEl.querySelector('.mt-hoja').innerHTML =
      '<button type="button" class="mt-cerrar" data-cerrar="1" aria-label="Cerrar">' + ico('close', 20, 3) + '</button>' +
      '<div class="mt-hoja-cab"><span class="mt-aro grande ' + (e.completa ? 'hecha' : '') + '">' + aro(e.completa ? 1 : e.frac) +
        '<span class="mt-disco">' + (e.completa ? ico('check', 40, 3.4) : '<span class="mt-num">' + f.n + '</span>') + '</span></span>' +
        '<div><small>' + esc(f.t.titulo) + '</small><h3>' + esc(l.titulo) + '</h3><span class="mt-hoja-est">' + estadoTxt + '</span></div></div>' +
      '<div class="mt-recs">' + cards + '</div>';
  }

  function abrirHoja(id) {
    hojaAbierta = id;
    comp_abierto = false;
    if (!hojaEl) {
      hojaEl = document.createElement('div');
      hojaEl.className = 'mt-hoja-fondo';
      hojaEl.style.setProperty('--c', colorSeguro(D.materia.color));
      hojaEl.innerHTML = '<div class="mt-hoja" role="dialog" aria-modal="true"></div>';
      document.body.appendChild(hojaEl);
      document.body.classList.add('mt-bloqueado');
      hojaEl.addEventListener('click', function (ev) {
        if (ev.target === hojaEl || ev.target.closest('[data-cerrar]')) return cerrarHoja();
        var b = ev.target.closest('[data-paso]');
        if (b && !b.disabled) return abrirPaso(b.getAttribute('data-paso'));
        var d = ev.target.closest('[data-bajar]');
        if (d) return descargar(+d.getAttribute('data-bajar'));
      });
    }
    pintarHoja();
  }

  function cerrarHoja() {
    hojaAbierta = null;
    if (hojaEl) { hojaEl.remove(); hojaEl = null; }
    document.body.classList.remove('mt-bloqueado');
  }

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
      toast('¡Lección completada! 🎉');
      await sb.from('student_lesson_progress').insert({ student_id: D.sid, lesson_id: lessonId });
    }
  }

  function refrescar() { pintar(); if (hojaAbierta) pintarHoja(); }

  // ---------- Abrir cada recuadro ----------
  function pasoActual(k) { var f = buscarLeccion(hojaAbierta); return f && (D.pasos[f.l.id] || {})[k]; }

  async function abrirPaso(k) {
    var f = buscarLeccion(hojaAbierta), paso = pasoActual(k);
    if (!f || !paso) return;
    try {
      if (k === 'video') {
        WaveVisor.abrirVideo({ titulo: f.l.titulo, alTerminar: function () { marcar(paso); },
          token: async function () { return (await llamar('content-access', { action: 'video', step_id: paso.id })).token; } });
      } else if (k === 'pdf') {
        WaveVisor.abrirPdf({ titulo: f.l.titulo + ' · PDF', descargable: true, alTerminar: function () { marcar(paso); },
          url: async function (desc) { return (await llamar('content-access', { action: 'pdf', step_id: paso.id, descarga: !!desc })).url; } });
      } else if (k === 'interactive') {
        var r = await sb.from('lesson_steps').select('content').eq('id', paso.id).maybeSingle();
        if (r.error || !r.data || !r.data.content || !r.data.content.html) throw new Error('No pudimos abrir la actividad.');
        abrirInteractiva(paso, f.l.titulo, r.data.content.html);
      } else if (k === 'final') {
        abrirCuestionario({
          titulo: 'Actividad · ' + f.l.titulo, examen: false,
          cargar: function () { return preguntas('lesson_step_id', paso.id); },
          enviar: function (resp) { return llamar('grade-final-activity', { lesson_step_id: paso.id, answers: resp }); },
          alTerminar: function (res) {
            D.progreso[paso.id] = { score: res.score, estado: 'graded' };
            revisarLeccion(paso.lesson_id).then(refrescar);
          }
        });
      } else if (k === 'complementary') {
        comp_abierto = !comp_abierto;
        pintarHoja();
      }
    } catch (e) { toast(e.message || 'No se pudo abrir.', true); }
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
    var r = await sb.from('questions').select('id, prompt, question_type, options, points, position').eq(col, id).order('position');
    if (r.error) throw r.error;
    if (!r.data.length) throw new Error('Todavía no hay preguntas cargadas.');
    return r.data;
  }

  function abrirCuestionario(op) {
    var el = document.createElement('div');
    el.className = 'wvp';
    el.innerHTML = '<div class="wvp-caja"><div class="wvp-barra"><b class="wvp-titulo">' + esc(op.titulo) + '</b>' +
      '<button type="button" class="wvp-b wvp-x" data-cerrar="1" aria-label="Cerrar">✕</button></div>' +
      '<div class="mt-cuest"><div class="mt-cuest-estado">Cargando…</div></div></div>';
    document.body.appendChild(el);
    document.body.classList.add('wvp-abierto');
    var cuerpo = el.querySelector('.mt-cuest');
    var lista = [], enviando = false;

    function cerrar() { document.body.classList.remove('wvp-abierto'); el.remove(); }
    el.addEventListener('click', function (ev) {
      if (ev.target === el || ev.target.closest('[data-cerrar]')) { if (!enviando) cerrar(); return; }
      if (ev.target.closest('[data-enviar]')) enviar();
      else if (ev.target.closest('[data-otra]')) formulario();
    });

    function campo(q, i) {
      var h = '<div class="mt-preg"><div class="mt-preg-n">' + (i + 1) + '</div><div class="mt-preg-c"><p>' + esc(q.prompt) + '</p>';
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

    function formulario() {
      cuerpo.innerHTML = lista.map(campo).join('') +
        '<div class="mt-cuest-pie"><button type="button" class="mt-boton" data-enviar="1">Entregar</button></div>';
      cuerpo.scrollTo(0, 0);
    }

    async function enviar() {
      var resp = lista.map(function (q, i) {
        var c = cuerpo.querySelector('[name="q' + i + '"]:checked') || cuerpo.querySelector('.mt-txt[name="q' + i + '"]');
        return { question_id: q.id, answer: c ? c.value : '' };
      });
      var vacias = resp.filter(function (r) { return !String(r.answer).trim(); }).length;
      if (vacias && !confirm('Te quedaron ' + vacias + (vacias === 1 ? ' pregunta' : ' preguntas') + ' sin responder. ¿Entregar igual?')) return;
      enviando = true;
      cuerpo.innerHTML = '<div class="mt-cuest-estado"><div class="mt-girar"></div><b>Estamos corrigiendo tus respuestas…</b><small>Puede tardar unos segundos. No cierres esta ventana.</small></div>';
      try {
        var res = await op.enviar(resp);
        enviando = false;
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
          return '<div class="mt-res-item"><div class="mt-res-cab"><span class="mt-preg-n">' + (i + 1) + '</span><b>' + esc(q.prompt) + '</b><span class="mt-chip-n ' + (sc >= 70 ? 'ok' : sc >= 40 ? 'med' : 'bajo') + '">' + sc + '</span></div>' +
            '<p class="mt-res-tu"><small>Tu respuesta</small>' + esc(mias[q.id] || '(sin responder)') + '</p>' +
            (r.feedback ? '<p class="mt-res-dev">' + esc(r.feedback) + '</p>' : '') + '</div>';
        }).join('') + '</div>' +
        '<div class="mt-cuest-pie">' + (ok && op.examen ? '' : '<button type="button" class="mt-boton suave" data-otra="1">Intentar de nuevo</button>') +
        '<button type="button" class="mt-boton" data-cerrar="1">Listo</button></div>';
      cuerpo.scrollTo(0, 0);
    }

    op.cargar().then(function (qs) { lista = qs; formulario(); }).catch(function (e) {
      cuerpo.innerHTML = '<div class="mt-cuest-estado error"><b>' + esc(e.message || 'No se pudo cargar.') + '</b></div>';
    });
  }

  function abrirExamen(temaId) {
    var t = D.temas.filter(function (x) { return x.id === temaId; })[0];
    if (!t || !t.examen) return;
    if (!t.examenDisponible) { toast('Primero terminá todas las lecciones del tema.', true); return; }
    abrirCuestionario({
      titulo: 'Examen · ' + t.titulo, examen: true,
      cargar: function () { return preguntas('exam_id', t.examen.id); },
      enviar: function (resp) { return llamar('grade-exam', { exam_id: t.examen.id, answers: resp }); },
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
      token: async function () { return (await llamar('content-access', { action: 'intro', subject_id: D.materia.id })).token; } });
  }

  // ---------- Entrada ----------
  var enlazado = false;
  function enlazar() {
    if (enlazado) return;
    enlazado = true;
    vista.addEventListener('click', function (ev) {
      if (!D || !vista.querySelector('.mt')) return;
      var n = ev.target.closest('[data-leccion]');
      if (n) {
        var f = buscarLeccion(n.getAttribute('data-leccion'));
        if (!f) return;
        if (D.sinAcceso) return toast('La suscripción tiene que estar al día para ver el contenido.', true);
        if (f.l.bloqueada) return toast(f.t.bloqueado ? 'Primero terminá el tema anterior y aprobá su examen.' : 'Primero terminá la lección anterior.', true);
        if (f.l.est.vacia) return toast('Esta lección está en preparación.');
        return abrirHoja(f.l.id);
      }
      var x = ev.target.closest('[data-examen]');
      if (x) return abrirExamen(x.getAttribute('data-examen'));
      if (ev.target.closest('[data-intro]')) return abrirIntro();
    });
  }

  async function abrir(el, materiaId) {
    vista = el;
    cerrarHoja();
    vista.innerHTML = '<div class="mt"><div class="mt-vacio">Cargando tu materia…</div></div>';
    enlazar();
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
  function _probar(el, datos) { vista = el; D = datos; enlazar(); pintar(); }

  window.WaveMateria = { abrir: abrir, _probar: _probar };
})();
