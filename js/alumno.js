// Panel de estudiante: navegación y lista de cursos.
(function () {
  var sb = Wave.sb;
  var vista = document.getElementById('vista');
  var enlaces = document.querySelectorAll('.nav-alumno a');
  var estudianteId = null;

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function colorSeguro(c) {
    return /^#[0-9a-fA-F]{6}$/.test(c || '') ? c : '#6366F1';
  }


  // ---------- Íconos por materia ----------
  var P = {
    mate: '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h.01M12 12h.01M16 12h.01M8 16h.01M12 16h.01M16 16h.01"/>',
    lengua: '<path d="M2 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H2zM22 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8z"/>',
    natural: '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6C9.5 14.5 12 13 13 12"/>',
    fisica: '<circle cx="12" cy="12" r="1.5"/><ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120 12 12)"/>',
    quimica: '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7.5 15h9"/>',
    historia: '<path d="M3 21h18M5 21V10M9 21V10M15 21V10M19 21V10M2 10l10-6 10 6z"/>',
    geografia: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/>',
    ingles: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
    arte: '<path d="M12 22a10 10 0 1 1 10-10c0 3-2 4-4 4h-2a2 2 0 0 0-1.5 3.3c.6.7.4 2.7-2.5 2.7z"/><path d="M7.5 11h.01M10.5 7h.01M15.5 8h.01"/>',
    bienestar: '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7z"/>',
    ciudadania: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    economia: '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>',
    tecnologia: '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    oficios: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
    proyecto: '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5M9 18h6M10 22h4"/>'
  };

  // El orden importa: lo más específico primero.
  var REGLAS = [
    ['fisico', 'quimica'], ['quimic', 'quimica'], ['fisic', 'fisica'],
    ['biolog', 'natural'], ['naturales', 'natural'],
    ['sociales', 'historia'], ['histor', 'historia'],
    ['geograf', 'geografia'], ['ingles', 'ingles'],
    ['matemat', 'mate'], ['lengua', 'lengua'], ['literatura', 'lengua'],
    ['arte', 'arte'], ['bienestar', 'bienestar'],
    ['ciudadan', 'ciudadania'], ['filosof', 'ciudadania'],
    ['econom', 'economia'], ['tecnolog', 'tecnologia'],
    ['oficio', 'oficios'], ['taller', 'oficios'], ['proyecto', 'proyecto']
  ];

  function iconoMateria(nombre) {
    var n = String(nombre || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    var clave = 'lengua';
    for (var i = 0; i < REGLAS.length; i++) {
      if (n.indexOf(REGLAS[i][0]) !== -1) { clave = REGLAS[i][1]; break; }
    }
    return '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + P[clave] + '</svg>';
  }


  // Rueda de progreso: frac entre 0 y 1, texto dentro y rótulo abajo
  function rueda(frac, texto, rotulo) {
    var r = 17, c = 2 * Math.PI * r;
    var f = Math.max(0, Math.min(1, frac || 0));
    return '<div class="rueda">' +
      '<svg viewBox="0 0 44 44" width="58" height="58" aria-hidden="true">' +
      '<circle cx="22" cy="22" r="' + r + '" fill="none" stroke="rgba(0,0,0,0.25)" stroke-width="4"/>' +
      '<circle cx="22" cy="22" r="' + r + '" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"' +
      ' stroke-dasharray="' + (c * f).toFixed(1) + ' ' + c.toFixed(1) + '" transform="rotate(-90 22 22)"/>' +
      '</svg><b>' + texto + '</b><span>' + rotulo + '</span></div>';
  }

  // ---------- Datos ----------
  async function cargarCursos() {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;

    var est = await sb.from('students').select('id').eq('profile_id', uid).maybeSingle();
    if (est.error) throw est.error;
    if (!est.data) return [];
    estudianteId = est.data.id;

    var mats = await sb.from('student_subjects')
      .select('subjects(id, name, color, position)')
      .eq('student_id', estudianteId);
    if (mats.error) throw mats.error;

    var materias = (mats.data || [])
      .map(function (r) { return r.subjects; })
      .filter(Boolean)
      .sort(function (a, b) { return a.position - b.position; });
    if (!materias.length) return [];

    var ids = materias.map(function (m) { return m.id; });

    var les = await sb.from('lessons')
      .select('id, topics!inner(subject_id)')
      .in('topics.subject_id', ids);
    if (les.error) throw les.error;

    var prog = await sb.from('student_lesson_progress')
      .select('lesson_id')
      .eq('student_id', estudianteId);
    if (prog.error) throw prog.error;

    var hechas = {};
    (prog.data || []).forEach(function (p) { hechas[p.lesson_id] = true; });

    var total = {}, completas = {};
    (les.data || []).forEach(function (l) {
      var sid = l.topics.subject_id;
      total[sid] = (total[sid] || 0) + 1;
      if (hechas[l.id]) completas[sid] = (completas[sid] || 0) + 1;
    });

    // Actividades (interactivas y finales) de cada materia
    var pasos = await sb.from('lesson_steps')
      .select('id, lessons!inner(topics!inner(subject_id))')
      .in('step_type', ['interactive_activity', 'final_activity'])
      .in('lessons.topics.subject_id', ids);
    if (pasos.error) throw pasos.error;

    var pp = await sb.from('student_step_progress')
      .select('lesson_step_id, score')
      .eq('student_id', estudianteId);
    if (pp.error) throw pp.error;
    var puntajePaso = {};
    (pp.data || []).forEach(function (p) { puntajePaso[p.lesson_step_id] = p.score; });

    // Exámenes de cada materia y los intentos del alumno
    var exs = await sb.from('exams')
      .select('id, topics!inner(subject_id)')
      .in('topics.subject_id', ids);
    if (exs.error) throw exs.error;

    var ints = await sb.from('exam_attempts')
      .select('exam_id, score, passed, grading_status')
      .eq('student_id', estudianteId);
    if (ints.error) throw ints.error;

    var examenMateria = {};
    var stats = {};
    ids.forEach(function (id) {
      stats[id] = { act: 0, actHechas: 0, ex: 0, exAprob: 0, suma: 0, n: 0 };
    });

    (pasos.data || []).forEach(function (s) {
      var st = stats[s.lessons.topics.subject_id];
      st.act++;
      if (s.id in puntajePaso) {
        st.actHechas++;
        if (puntajePaso[s.id] != null) { st.suma += Number(puntajePaso[s.id]); st.n++; }
      }
    });

    (exs.data || []).forEach(function (e) {
      examenMateria[e.id] = e.topics.subject_id;
      stats[e.topics.subject_id].ex++;
    });

    var aprobados = {};
    (ints.data || []).forEach(function (i) {
      var sid = examenMateria[i.exam_id];
      if (!sid) return;
      if (i.grading_status === 'graded' && i.score != null) {
        stats[sid].suma += Number(i.score); stats[sid].n++;
      }
      if (i.passed && !aprobados[i.exam_id]) {
        aprobados[i.exam_id] = true;
        stats[sid].exAprob++;
      }
    });

    return materias.map(function (m) {
      var st = stats[m.id];
      return { id: m.id, nombre: m.name, color: colorSeguro(m.color),
               total: total[m.id] || 0, completas: completas[m.id] || 0,
               promedio: st.n ? Math.round(st.suma / st.n) : null,
               examenes: st.ex, examenesAprob: st.exAprob,
               actividades: st.act, actividadesHechas: st.actHechas };
    });
  }

  // ---------- Vistas ----------
  async function vistaCursos() {
    vista.innerHTML = '<h1 class="vista-titulo">Mis cursos</h1><div id="cursos"></div>';
    var cont = document.getElementById('cursos');
    cont.innerHTML = '<div class="vacio">Cargando tus cursos…</div>';
    try {
      var cursos = await cargarCursos();
      if (!cursos.length) {
        cont.innerHTML = '<div class="vacio">Todavía no tenés materias habilitadas.</div>';
        return;
      }
      cont.className = 'cursos-grilla';
      cont.innerHTML = cursos.map(function (c) {
        var pct = c.total ? Math.round((c.completas / c.total) * 100) : 0;
        return '<article class="curso" style="--c:' + c.color + '">' +
          '<div class="curso-cabeza"><div class="curso-icono">' + iconoMateria(c.nombre) + '</div>' +
          '<h2>' + esc(c.nombre) + '</h2></div>' +
          '<p class="curso-lecciones">' + c.completas + ' de ' + c.total + ' lecciones</p>' +
          '<div class="curso-fila"><span>Progreso</span><b>' + pct + '%</b></div>' +
          '<div class="curso-barra" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct + '"><span style="width:' + pct + '%"></span></div>' +
          '<div class="ruedas">' +
            rueda(c.promedio == null ? 0 : c.promedio / 100, c.promedio == null ? '—' : c.promedio + '%', 'Promedio') +
            rueda(c.examenes ? c.examenesAprob / c.examenes : 0, c.examenesAprob + '/' + c.examenes, 'Exámenes') +
            rueda(c.actividades ? c.actividadesHechas / c.actividades : 0, c.actividadesHechas + '/' + c.actividades, 'Actividades') +
          '</div>' +
          '</article>';
      }).join('');
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar tus cursos. Probá recargar la página.</div>';
    }
  }

  function vistaProximamente(titulo) {
    vista.innerHTML = '<h1 class="vista-titulo">' + esc(titulo) + '</h1>' +
      '<div class="proximamente">Esta sección está en construcción.</div>';
  }

  // ---------- Programación ----------
  var DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'];
  var prog = { cursos: [], filas: [], finAnio: null, uid: null, ocupado: false };

  function fechaLarga(d) {
    return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'long', year: 'numeric' });
  }

  function textoLecciones(n) { return n + (n === 1 ? ' lección' : ' lecciones'); }

  function cursoPorId(id) {
    return prog.cursos.filter(function (c) { return c.id === id; })[0];
  }

  // Día en que se terminan las lecciones que faltan, siguiendo el programa (de lunes a viernes)
  function fechaFin(restantes, porDia) {
    var d = new Date();
    d.setHours(12, 0, 0, 0);
    for (var i = 0; i < 3650; i++) {
      var wd = d.getDay();
      if (wd >= 1 && wd <= 5) {
        restantes -= porDia[wd];
        if (restantes <= 0) return new Date(d);
      }
      d.setDate(d.getDate() + 1);
    }
    return null;
  }

  function semanasDeRetraso(fin, limite) {
    return Math.ceil((fin - limite) / 86400000 / 7);
  }

  function trayectoria() {
    var filasCursos = [];
    var finGlobal = null;
    var sinProgramar = [];
    var restantesTotal = 0;
    var hayLecciones = false;

    prog.cursos.forEach(function (c) {
      var porDia = [0, 0, 0, 0, 0, 0];
      var semanal = 0;
      prog.filas.forEach(function (f) {
        if (f.subject_id === c.id) { porDia[f.weekday] += f.lessons_target; semanal += f.lessons_target; }
      });
      var restantes = Math.max(0, c.total - c.completas);
      var r = { curso: c, restantes: restantes, semanal: semanal, estado: '', clase: 'neutro', texto: '' };

      if (c.total === 0) {
        r.texto = 'Todavía no tiene lecciones cargadas';
      } else {
        hayLecciones = true;
        restantesTotal += restantes;
        if (restantes === 0) {
          r.estado = 'Completada'; r.clase = 'ok';
        } else if (semanal === 0) {
          r.texto = 'No está en la programación'; r.clase = 'atraso';
          sinProgramar.push(c.nombre);
        } else {
          var fin = fechaFin(restantes, porDia);
          if (!fin) {
            r.texto = 'Con este ritmo tardaría más de 10 años'; r.clase = 'atraso';
          } else {
            if (!finGlobal || fin > finGlobal) finGlobal = fin;
            r.texto = 'Termina el ' + fechaLarga(fin) + ' · ' + textoLecciones(semanal) + ' por semana';
            if (prog.finAnio && fin > prog.finAnio) {
              r.estado = 'Se retrasa ' + semanasDeRetraso(fin, prog.finAnio) + ' sem.'; r.clase = 'atraso';
            } else {
              r.estado = 'A tiempo'; r.clase = 'ok';
            }
          }
        }
      }
      filasCursos.push(r);
    });

    return { filas: filasCursos, finGlobal: finGlobal, sinProgramar: sinProgramar,
             restantesTotal: restantesTotal, hayLecciones: hayLecciones };
  }

  function htmlResumen(t) {
    var limite = prog.finAnio ? fechaLarga(prog.finAnio) : null;
    if (!t.hayLecciones) {
      return '<p>Todavía no hay lecciones cargadas en tus materias. Cuando las haya, acá vas a ver cuándo terminarías tu año siguiendo este programa.</p>';
    }
    if (t.restantesTotal === 0) {
      return '<p><b>¡Completaste todas las lecciones de tu año!</b></p>';
    }
    var html = '<p>Te faltan <b>' + textoLecciones(t.restantesTotal) + '</b> en total.</p>';
    if (t.finGlobal) {
      html += '<p>Siguiendo este programa, terminarías el <b>' + fechaLarga(t.finGlobal) + '</b>.</p>';
      if (limite) {
        if (t.finGlobal > prog.finAnio) {
          html += '<p class="resumen-atraso">Eso es <b>' + semanasDeRetraso(t.finGlobal, prog.finAnio) +
            ' semanas después</b> del fin del año escolar (' + esc(limite) + '). Para llegar a tiempo, sumá lecciones por día.</p>';
        } else {
          html += '<p class="resumen-ok">Llegás a tiempo: el año escolar termina el ' + esc(limite) + '.</p>';
        }
      }
    }
    if (t.sinProgramar.length) {
      html += '<p class="resumen-atraso">Falta programar: ' + esc(t.sinProgramar.join(', ')) + '.</p>';
    }
    return html;
  }

  function pintarProgramacion() {
    var cont = document.getElementById('prog');
    if (!cont) return;

    var dias = DIAS.map(function (nombre, i) {
      var wd = i + 1;
      var delDia = prog.filas.filter(function (f) { return f.weekday === wd; })
        .sort(function (a, b) { return a.position - b.position; });
      var usadas = {};
      delDia.forEach(function (f) { usadas[f.subject_id] = true; });

      var items = delDia.map(function (f) {
        var c = cursoPorId(f.subject_id);
        if (!c) return '';
        return '<div class="prog-item" style="--c:' + c.color + '">' +
          '<div class="prog-item-top"><span class="prog-ico">' + iconoMateria(c.nombre) + '</span>' +
          '<b>' + esc(c.nombre) + '</b>' +
          '<button type="button" class="prog-x" data-a="quitar" data-id="' + f.id + '" aria-label="Quitar materia">×</button></div>' +
          '<div class="prog-cant">' +
          '<button type="button" data-a="menos" data-id="' + f.id + '" aria-label="Una lección menos">−</button>' +
          '<span>' + textoLecciones(f.lessons_target) + '</span>' +
          '<button type="button" data-a="mas" data-id="' + f.id + '" aria-label="Una lección más">+</button>' +
          '</div></div>';
      }).join('');

      var opciones = prog.cursos.filter(function (c) { return !usadas[c.id]; }).map(function (c) {
        return '<option value="' + c.id + '">' + esc(c.nombre) + '</option>';
      }).join('');

      var agregar = opciones
        ? '<select class="prog-agregar" data-a="agregar" data-dia="' + wd + '" aria-label="Agregar materia el ' + nombre + '">' +
          '<option value="">+ Agregar materia</option>' + opciones + '</select>'
        : '';

      return '<section class="dia"><h2>' + nombre + '</h2>' + items + agregar + '</section>';
    }).join('');

    var sugerir = prog.filas.length === 0
      ? '<div class="prog-sugerir"><p>Todavía no armaste tu programa.</p>' +
        '<button type="button" data-a="sugerir">Armar programa sugerido</button></div>'
      : '';

    var t = trayectoria();
    var filasT = t.filas.map(function (r) {
      return '<div class="tray-fila" style="--c:' + r.curso.color + '">' +
        '<span class="tray-punto"></span>' +
        '<div class="tray-info"><b>' + esc(r.curso.nombre) + '</b><span>' +
        (r.texto ? esc(r.texto) : (r.restantes === 0 ? 'Sin lecciones pendientes' : '')) + '</span></div>' +
        (r.estado ? '<span class="tray-estado ' + r.clase + '">' + esc(r.estado) + '</span>' : '') +
        '</div>';
    }).join('');

    cont.className = '';
    cont.innerHTML = sugerir +
      '<div class="semana">' + dias + '</div>' +
      '<h2 class="vista-subtitulo">Trayectoria</h2>' +
      '<div class="tray"><div class="tray-resumen">' + htmlResumen(t) + '</div>' + filasT + '</div>';
  }

  async function guardar(fn) {
    if (prog.ocupado) return;
    prog.ocupado = true;
    try { await fn(); }
    catch (e) { alert('No pudimos guardar el cambio. Probá de nuevo.'); }
    prog.ocupado = false;
    pintarProgramacion();
  }

  function filaPorId(id) {
    return prog.filas.filter(function (f) { return String(f.id) === String(id); })[0];
  }

  async function cambiarCantidad(id, delta) {
    var f = filaPorId(id);
    if (!f) return;
    var n = Math.max(1, Math.min(20, f.lessons_target + delta));
    if (n === f.lessons_target) return;
    var r = await sb.from('study_schedule').update({ lessons_target: n, updated_by: prog.uid })
      .eq('id', f.id).select('id');
    if (r.error || !r.data.length) throw (r.error || new Error('sin permiso'));
    f.lessons_target = n;
  }

  async function quitarFila(id) {
    var r = await sb.from('study_schedule').delete().eq('id', id).select('id');
    if (r.error || !r.data.length) throw (r.error || new Error('sin permiso'));
    prog.filas = prog.filas.filter(function (f) { return String(f.id) !== String(id); });
  }

  async function agregarFila(dia, materiaId) {
    var pos = prog.filas.filter(function (f) { return f.weekday === dia; }).length;
    var r = await sb.from('study_schedule').insert({
      student_id: estudianteId, weekday: dia, subject_id: materiaId,
      lessons_target: 1, position: pos, updated_by: prog.uid
    }).select('id, weekday, subject_id, lessons_target, position');
    if (r.error) throw r.error;
    prog.filas = prog.filas.concat(r.data);
  }

  // Reparte las materias rotando: cada día tiene hasta 3 y todas aparecen parejo en la semana
  async function sugerirPrograma() {
    var n = prog.cursos.length;
    var porDia = Math.min(3, n);
    var filas = [];
    for (var d = 0; d < 5; d++) {
      for (var k = 0; k < porDia; k++) {
        var c = prog.cursos[(d * porDia + k) % n];
        filas.push({ student_id: estudianteId, weekday: d + 1, subject_id: c.id,
                     lessons_target: 1, position: k, updated_by: prog.uid });
      }
    }
    var r = await sb.from('study_schedule').insert(filas)
      .select('id, weekday, subject_id, lessons_target, position');
    if (r.error) throw r.error;
    prog.filas = prog.filas.concat(r.data);
  }

  function engancharProgramacion(cont) {
    cont.addEventListener('click', function (ev) {
      var b = ev.target.closest('button[data-a]');
      if (!b) return;
      var a = b.getAttribute('data-a');
      var id = b.getAttribute('data-id');
      if (a === 'mas') guardar(function () { return cambiarCantidad(id, 1); });
      else if (a === 'menos') guardar(function () { return cambiarCantidad(id, -1); });
      else if (a === 'quitar') guardar(function () { return quitarFila(id); });
      else if (a === 'sugerir') guardar(sugerirPrograma);
    });
    cont.addEventListener('change', function (ev) {
      var s = ev.target;
      if (s.getAttribute('data-a') !== 'agregar' || !s.value) return;
      var dia = Number(s.getAttribute('data-dia'));
      var materia = s.value;
      guardar(function () { return agregarFila(dia, materia); });
    });
  }

  async function vistaProgramacion() {
    vista.innerHTML = '<h1 class="vista-titulo">Programación</h1><div id="prog"><div class="vacio">Cargando tu programación…</div></div>';
    var cont = document.getElementById('prog');
    try {
      prog.cursos = await cargarCursos();
      if (!prog.cursos.length || !estudianteId) {
        cont.innerHTML = '<div class="vacio">Todavía no tenés materias habilitadas.</div>';
        return;
      }
      var ses = await sb.auth.getSession();
      prog.uid = ses.data.session.user.id;

      var r = await sb.from('study_schedule')
        .select('id, weekday, subject_id, lessons_target, position')
        .eq('student_id', estudianteId).order('position');
      if (r.error) throw r.error;
      prog.filas = r.data || [];

      var cfg = await sb.from('app_settings').select('value').eq('key', 'school_year_end').maybeSingle();
      prog.finAnio = (cfg.data && cfg.data.value) ? new Date(String(cfg.data.value) + 'T12:00:00') : null;
      if (prog.finAnio && isNaN(prog.finAnio.getTime())) prog.finAnio = null;

      engancharProgramacion(cont);
      pintarProgramacion();
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar tu programación. Probá recargar la página.</div>';
    }
  }

  var VISTAS = {
    cursos: vistaCursos,
    programacion: vistaProgramacion,
    estadisticas: function () { vistaProximamente('Estadísticas'); },
    perfil: function () { vistaProximamente('Perfil'); }
  };

  function ruta() {
    var nombre = (location.hash || '#cursos').slice(1);
    if (!VISTAS[nombre]) nombre = 'cursos';
    enlaces.forEach(function (a) {
      a.classList.toggle('activo', a.getAttribute('href') === '#' + nombre);
    });
    VISTAS[nombre]();
  }

  window.addEventListener('hashchange', ruta);
  ruta();
})();
