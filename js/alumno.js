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
      .select('id, topic_id, topics!inner(subject_id)')
      .in('topics.subject_id', ids);
    if (les.error) throw les.error;

    var prog = await sb.from('student_lesson_progress')
      .select('lesson_id')
      .eq('student_id', estudianteId);
    if (prog.error) throw prog.error;

    var hechas = {};
    (prog.data || []).forEach(function (p) { hechas[p.lesson_id] = true; });

    // El avance se cuenta en TEMAS: un tema se completa cuando están hechas todas sus
    // lecciones y aprobado su examen (si tiene). Se calcula más abajo, con los exámenes.
    var temas = {};
    (les.data || []).forEach(function (l) {
      var t = temas[l.topic_id] = temas[l.topic_id] || { sid: l.topics.subject_id, todas: true, examen: null };
      if (!hechas[l.id]) t.todas = false;
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
      .select('id, topic_id, topics!inner(subject_id)')
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
      if (temas[e.topic_id]) temas[e.topic_id].examen = e.id;
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

    var total = {}, completas = {};
    Object.keys(temas).forEach(function (tid) {
      var t = temas[tid];
      total[t.sid] = (total[t.sid] || 0) + 1;
      if (t.todas && (!t.examen || aprobados[t.examen])) completas[t.sid] = (completas[t.sid] || 0) + 1;
    });

    return materias.map(function (m) {
      var st = stats[m.id];
      return { id: m.id, nombre: m.name, color: colorSeguro(m.color),
               total: total[m.id] || 0, completas: completas[m.id] || 0,
               promedio: st.n ? Math.round(st.suma / st.n) : null,
               examenes: st.ex, examenesAprob: st.exAprob,
               actividades: st.act, actividadesHechas: st.actHechas,
               suma: st.suma, notas: st.n };
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
          '<p class="curso-lecciones">' + c.completas + ' de ' + c.total + (c.total === 1 ? ' tema' : ' temas') + '</p>' +
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
  var prog = { cursos: [], filas: [], finAnio: null, uid: null, ocupado: false, inicio: null, meses: null, lecciones: {}, hechasLecc: {} };

  function fechaLarga(d) {
    return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'long', year: 'numeric' });
  }

  function textoLecciones(n) { return n + (n === 1 ? ' lección' : ' lecciones'); }

  function cursoPorId(id) {
    return prog.cursos.filter(function (c) { return c.id === id; })[0];
  }

  // Día en que se terminan los temas que faltan, siguiendo el programa (de lunes a viernes)
  // Se cuentan 40 semanas activas por año (hay vacaciones y feriados): el calendario real es 52/40 más largo
  var FACTOR_CALENDARIO = 52 / 40;

  // Fecha objetivo = primer ingreso + semanas que pide la tabla del año con la programación semanal:
  // lecciones del año de cada materia ÷ lecciones por semana (manda la materia que más tarda)
  function recalcularObjetivo() {
    prog.finAnio = null;
    if (!prog.inicio || !prog.meses) return;
    var semanas = 0;
    prog.cursos.forEach(function (c) {
      var total = prog.lecciones[c.id];
      if (!total) return;
      var sem = 0;
      prog.filas.forEach(function (f) { if (f.subject_id === c.id) sem += f.lessons_target; });
      if (sem > 0) semanas = Math.max(semanas, Math.ceil(total / sem));
    });
    var f = new Date(prog.inicio);
    f.setHours(12, 0, 0, 0);
    if (isNaN(f.getTime())) return;
    if (semanas) f.setDate(f.getDate() + Math.round(semanas * 7 * FACTOR_CALENDARIO));
    else f.setMonth(f.getMonth() + prog.meses);
    prog.finAnio = f;
  }

  function fechaFin(restantes, porDia) {
    var hoy = new Date();
    hoy.setHours(12, 0, 0, 0);
    var d = new Date(hoy);
    for (var i = 0; i < 3650; i++) {
      var wd = d.getDay();
      if (wd >= 1 && wd <= 5) {
        restantes -= porDia[wd];
        if (restantes <= 0) return new Date(hoy.getTime() + (d - hoy) * FACTOR_CALENDARIO);
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
      var tot = prog.lecciones[c.id] || 0;
        var hechasL = prog.hechasLecc[c.id] || 0;
        var restantes = Math.max(0, tot - hechasL);
      var r = { curso: c, tot: tot, hechas: hechasL, restantes: restantes, semanal: semanal, estado: '', clase: 'neutro', texto: '' };

      if (tot === 0) {
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

  function fechaCorta(d) {
    return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  function htmlHero(t) {
    var hoy = new Date();
    hoy.setHours(12, 0, 0, 0);
    var nota = t.sinProgramar.length
      ? '<p class="tray-nota">Falta programar: ' + esc(t.sinProgramar.join(', ')) + '.</p>' : '';

    if (!t.hayLecciones) {
      return '<div class="tray-hero"><p class="tray-vacio">Todavía no hay lecciones cargadas en tus materias. ' +
        'Cuando las haya, acá vas a ver cuándo terminarías tu año con este programa.</p></div>';
    }
    if (t.restantesTotal === 0) {
      return '<div class="tray-hero ok"><b class="tray-fecha">¡Completaste todas las lecciones de tu año!</b></div>';
    }
    if (!t.finGlobal) {
      return '<div class="tray-hero atraso"><b class="tray-fecha">Programá tus materias para calcular cuándo terminás</b>' + nota + '</div>';
    }

    var atrasado = prog.finAnio && t.finGlobal > prog.finAnio;
    var pill = '';
    if (prog.finAnio) {
      pill = atrasado
        ? '<span class="tray-pill atraso">+' + semanasDeRetraso(t.finGlobal, prog.finAnio) + ' semanas de retraso</span>'
        : '<span class="tray-pill ok">Llegás a tiempo</span>';
    }

    var linea = '';
    if (prog.finAnio && prog.finAnio > hoy) {
      var pos = Math.min(100, Math.max(0, ((t.finGlobal - hoy) / (prog.finAnio - hoy)) * 100));
      linea = '<div class="tray-linea"><div class="tray-relleno" style="width:' + pos.toFixed(1) + '%"></div>' +
        '<span class="tray-pin" style="left:' + pos.toFixed(1) + '%"></span></div>' +
        '<div class="tray-extremos"><span>Hoy</span><span>Fecha objetivo · ' + esc(fechaCorta(prog.finAnio)) + '</span></div>';
    }

    return '<div class="tray-hero ' + (atrasado ? 'atraso' : 'ok') + '">' +
      '<div class="tray-hero-top"><div><span class="tray-etiqueta">Terminarías tu año el</span>' +
      '<b class="tray-fecha">' + esc(fechaLarga(t.finGlobal)) + '</b></div>' + pill + '</div>' +
      linea +
      '<p class="tray-faltan">Te faltan <b>' + textoLecciones(t.restantesTotal) + '</b> en total.' +
      (atrasado ? ' Para llegar a tiempo, sumá lecciones por día.' : '') + '</p>' + nota + '</div>';
  }

  function pintarProgramacion() {
    var cont = document.getElementById('prog');
    if (!cont) return;
    recalcularObjetivo();
    var hoySemana = new Date().getDay();

    var dias = DIAS.map(function (nombre, i) {
      var wd = i + 1;
      var delDia = prog.filas.filter(function (f) { return f.weekday === wd; })
        .sort(function (a, b) { return a.position - b.position; });
      var usadas = {};
      var suma = 0;
      delDia.forEach(function (f) { usadas[f.subject_id] = true; suma += f.lessons_target; });

      var items = delDia.map(function (f) {
        var c = cursoPorId(f.subject_id);
        if (!c) return '';
        return '<div class="prog-item" style="--c:' + c.color + '">' +
          '<button type="button" class="prog-x" data-a="quitar" data-id="' + f.id + '" aria-label="Quitar ' + esc(c.nombre) + '">×</button>' +
          '<span class="prog-ico">' + iconoMateria(c.nombre) + '</span>' +
          '<b class="prog-nombre">' + esc(c.nombre) + '</b>' +
          '<div class="prog-cant">' +
          '<button type="button" data-a="menos" data-id="' + f.id + '" aria-label="Una lección menos">−</button>' +
          '<span><strong>' + f.lessons_target + '</strong> ' + (f.lessons_target === 1 ? 'lección' : 'lecciones') + '</span>' +
          '<button type="button" data-a="mas" data-id="' + f.id + '" aria-label="Una lección más">+</button>' +
          '</div></div>';
      }).join('');

      var libres = prog.cursos.filter(function (c) { return !usadas[c.id]; });
      var agregar = libres.length
        ? '<div class="prog-add"><button type="button" class="prog-add-btn" data-a="menu">+ Agregar materia</button>' +
          '<div class="prog-menu" hidden>' + libres.map(function (c) {
            return '<button type="button" data-a="agregar" data-dia="' + wd + '" data-mat="' + c.id + '">' +
              '<i style="background:' + c.color + '"></i>' + esc(c.nombre) + '</button>';
          }).join('') + '</div></div>'
        : '';

      return '<section class="dia' + (hoySemana === wd ? ' hoy' : '') + '">' +
        '<header class="dia-cab"><h2>' + nombre + '</h2>' +
        (hoySemana === wd ? '<span class="dia-hoy">Hoy</span>' : '') +
        '<small>' + (suma ? textoLecciones(suma) : 'Sin lecciones') + '</small></header>' +
        '<div class="dia-cuerpo">' + items + agregar + '</div></section>';
    }).join('');

    var t = trayectoria();
    var filasT = t.filas.map(function (r) {
      var c = r.curso;
      var pct = r.tot ? Math.min(100, Math.round((r.hechas / r.tot) * 100)) : 0;
      var info = r.texto || (r.restantes === 0 ? 'Sin lecciones pendientes' : '');
      return '<div class="tray-fila" style="--c:' + c.color + '">' +
        '<span class="tray-ico">' + iconoMateria(c.nombre) + '</span>' +
        '<div class="tray-info"><b>' + esc(c.nombre) + '</b>' +
        (info ? '<span>' + esc(info) + '</span>' : '') +
        (r.tot ? '<div class="tray-mini"><span style="width:' + pct + '%"></span></div>' : '') + '</div>' +
        (r.estado ? '<span class="tray-estado ' + r.clase + '">' + esc(r.estado) + '</span>' : '') +
        '</div>';
    }).join('');

    cont.innerHTML =
      '<div class="prog-acciones"><button type="button" class="prog-reset" data-a="restablecer">Restablecer programación recomendada</button></div>' +
      '<div class="semana">' + dias + '</div>' +
      '<h2 class="vista-subtitulo">Trayectoria</h2>' +
      htmlHero(t) +
      '<div class="tray-lista">' + filasT + '</div>';
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

  // Trae de nuevo la programación guardada
  async function recargarFilas() {
    var r = await sb.from('study_schedule').select('id, weekday, subject_id, lessons_target, position')
      .eq('student_id', estudianteId).order('position');
    if (r.error) throw r.error;
    prog.filas = r.data || [];
  }

  // Programa recomendado: lo arma la base según la carga de cada materia y el plazo elegido
  async function armarProgramaRecomendado() {
    var r = await sb.rpc('apply_recommended_schedule', { p_student: estudianteId });
    if (r.error) throw r.error;
    await recargarFilas();
  }

  async function restablecer() {
    if (prog.filas.length && !confirm('Se reemplaza tu programación actual por la recomendada. ¿Seguimos?')) return;
    await armarProgramaRecomendado();
  }

  function engancharProgramacion(cont) {
    cont.addEventListener('click', function (ev) {
      var b = ev.target.closest('button[data-a]');
      var cerrar = !b || b.getAttribute('data-a') !== 'menu';
      if (cerrar) {
        cont.querySelectorAll('.prog-menu').forEach(function (m) { m.hidden = true; });
      }
      if (!b) return;
      var a = b.getAttribute('data-a');
      var id = b.getAttribute('data-id');
      if (a === 'menu') {
        var menu = b.nextElementSibling;
        var abrir = menu.hidden;
        cont.querySelectorAll('.prog-menu').forEach(function (m) { m.hidden = true; });
        menu.hidden = !abrir;
      }
      else if (a === 'mas') guardar(function () { return cambiarCantidad(id, 1); });
      else if (a === 'menos') guardar(function () { return cambiarCantidad(id, -1); });
      else if (a === 'quitar') guardar(function () { return quitarFila(id); });
      else if (a === 'restablecer') guardar(restablecer);
      else if (a === 'agregar') {
        var dia = Number(b.getAttribute('data-dia'));
        var mat = b.getAttribute('data-mat');
        guardar(function () { return agregarFila(dia, mat); });
      }
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

      var cols = 'id, weekday, subject_id, lessons_target, position';
      var r = await sb.from('study_schedule').select(cols).eq('student_id', estudianteId).order('position');
      if (r.error) throw r.error;
      prog.filas = r.data || [];

      // Fecha objetivo: primer ingreso + semanas de la tabla del año según la programación (si la familia no eligió plazo, no se compara)
      var yo = await sb.from('students').select('started_at, target_months').eq('id', estudianteId).maybeSingle();
      prog.inicio = yo.data ? yo.data.started_at : null;
      prog.meses = yo.data ? yo.data.target_months : null;

      var cfg = await sb.from('subject_load_config').select('subject_id, lessons_total');
      prog.lecciones = {};
      (cfg.data || []).forEach(function (x) { prog.lecciones[x.subject_id] = x.lessons_total; });

      var avance = await sb.from('student_subject_progress').select('subject_id, completed_lessons').eq('student_id', estudianteId);
      prog.hechasLecc = {};
      (avance.data || []).forEach(function (x) { prog.hechasLecc[x.subject_id] = x.completed_lessons; });

      // Primera vez: el programa viene armado por la base, después se edita
      if (!prog.filas.length) {
        try { await armarProgramaRecomendado(); } catch (e) { /* queda vacío y se agrega a mano */ }
      }

      engancharProgramacion(cont);
      pintarProgramacion();
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar tu programación. Probá recargar la página.</div>';
    }
  }

  // ---------- Estadísticas ----------
  var DIAS_CORTOS = ['L', 'M', 'M', 'J', 'V'];

  function fechaISO(d) {
    var m = String(d.getMonth() + 1).padStart(2, '0');
    var dd = String(d.getDate()).padStart(2, '0');
    return d.getFullYear() + '-' + m + '-' + dd;
  }

  function textoTiempo(seg) {
    var min = Math.round(seg / 60);
    if (min < 60) return min + ' min';
    var h = Math.floor(min / 60), r = min % 60;
    return r ? h + ' h ' + r + ' min' : h + ' h';
  }

  async function cargarEstadisticas() {
    var cursos = await cargarCursos();
    var hoy = new Date();
    var lunes = new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate());
    lunes.setDate(lunes.getDate() - ((lunes.getDay() + 6) % 7));
    var viernes = new Date(lunes); viernes.setDate(lunes.getDate() + 4);
    var manana = new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate() + 1);
    var inicioHoy = new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate());

    var tiempo = { dias: [0, 0, 0, 0, 0], total: 0 };
    var lecciones = 0;
    if (estudianteId) {
      var t = await sb.from('student_study_time').select('study_date, seconds')
        .eq('student_id', estudianteId)
        .gte('study_date', fechaISO(lunes)).lte('study_date', fechaISO(viernes));
      if (t.error) throw t.error;
      (t.data || []).forEach(function (r) {
        var i = Math.round((new Date(r.study_date + 'T00:00:00') - lunes) / 86400000);
        if (i >= 0 && i <= 4) { tiempo.dias[i] += r.seconds; tiempo.total += r.seconds; }
      });

      var l = await sb.from('student_lesson_progress')
        .select('lesson_id', { count: 'exact', head: true })
        .eq('student_id', estudianteId)
        .gte('completed_at', inicioHoy.toISOString()).lt('completed_at', manana.toISOString());
      if (l.error) throw l.error;
      lecciones = l.count || 0;
    }

    var suma = 0, notas = 0;
    cursos.forEach(function (c) { suma += c.suma; notas += c.notas; });
    return { cursos: cursos, tiempo: tiempo, lecciones: lecciones,
             promedio: notas ? Math.round(suma / notas) : null,
             hoyIdx: (hoy.getDay() + 6) % 7 };
  }

  async function vistaEstadisticas() {
    vista.innerHTML = '<h1 class="vista-titulo">Estadísticas</h1><div id="estad"></div>';
    var cont = document.getElementById('estad');
    cont.innerHTML = '<div class="vacio">Cargando tus estadísticas…</div>';
    try {
      var d = await cargarEstadisticas();
      var max = Math.max.apply(null, d.tiempo.dias.concat([1]));
      var barras = d.tiempo.dias.map(function (seg, i) {
        var alto = seg ? Math.max(10, Math.round((seg / max) * 100)) : 4;
        return '<div class="est-dia' + (d.hoyIdx === i ? ' hoy' : '') + '">' +
          '<span class="est-dia-barra"><i style="height:' + alto + '%"></i></span>' +
          '<small>' + DIAS_CORTOS[i] + '</small></div>';
      }).join('');

      var r = 34, circ = 2 * Math.PI * r;
      var frac = d.promedio == null ? 0 : d.promedio / 100;
      var anillo = '<svg class="est-anillo" viewBox="0 0 80 80" width="92" height="92" aria-hidden="true">' +
        '<circle cx="40" cy="40" r="' + r + '" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="8"/>' +
        '<circle cx="40" cy="40" r="' + r + '" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"' +
        ' stroke-dasharray="' + (circ * frac).toFixed(1) + ' ' + circ.toFixed(1) + '" transform="rotate(-90 40 40)"/></svg>';

      var resumen =
        '<div class="est-resumen">' +
          '<article class="est-card tiempo">' +
            '<p class="est-rotulo">Tiempo de estudio · esta semana</p>' +
            '<p class="est-valor">' + textoTiempo(d.tiempo.total) + '</p>' +
            '<div class="est-dias" aria-hidden="true">' + barras + '</div>' +
          '</article>' +
          '<article class="est-card hoy">' +
            '<p class="est-rotulo">Hoy</p>' +
            '<p class="est-valor">' + d.lecciones + '</p>' +
            '<p class="est-sub">' + (d.lecciones === 1 ? 'lección completada' : 'lecciones completadas') + '</p>' +
          '</article>' +
          '<article class="est-card prom">' +
            '<p class="est-rotulo">Promedio general</p>' +
            '<div class="est-prom-fila">' + anillo +
              '<p class="est-valor">' + (d.promedio == null ? '—' : d.promedio + '%') + '</p></div>' +
            '<p class="est-sub">Actividades, finales y exámenes</p>' +
          '</article>' +
        '</div>';

      var ordenadas = d.cursos.slice().sort(function (x, y) {
        return (y.promedio == null ? -1 : y.promedio) - (x.promedio == null ? -1 : x.promedio);
      });
      var filas = ordenadas.map(function (c) {
        var pct = c.promedio == null ? 0 : c.promedio;
        return '<div class="est-fila" style="--c:' + c.color + '">' +
          '<span class="est-fila-nombre">' + esc(c.nombre) + '</span>' +
          '<div class="est-barra" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct + '"><span style="width:' + pct + '%"></span></div>' +
          '<b class="est-fila-pct">' + (c.promedio == null ? '—' : c.promedio + '%') + '</b></div>';
      }).join('');

      cont.innerHTML = resumen +
        '<section class="est-panel"><h2 class="est-panel-tit">Promedio por materia</h2>' +
        (filas || '<div class="vacio">Todavía no tenés materias habilitadas.</div>') + '</section>';
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar tus estadísticas. Probá recargar la página.</div>';
    }
  }

  // ---------- Perfil ----------
  function fechaNac(iso) {
    if (!iso) return null;
    var p = String(iso).split('-');
    return new Date(Number(p[0]), Number(p[1]) - 1, Number(p[2]));
  }

  function edadDe(d) {
    var hoy = new Date();
    var e = hoy.getFullYear() - d.getFullYear();
    if (hoy.getMonth() < d.getMonth() || (hoy.getMonth() === d.getMonth() && hoy.getDate() < d.getDate())) e--;
    return e;
  }

  async function cargarPerfil() {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;
    var est = await sb.from('students')
      .select('id, first_name, last_name, birth_date, document_number, grades(name, year_number, levels(slug, name))')
      .eq('profile_id', uid).maybeSingle();
    if (est.error) throw est.error;
    var pf = await sb.from('profiles').select('avatar_config').eq('id', uid).maybeSingle();
    if (pf.error) throw pf.error;
    var g = est.data && est.data.grades;
    var nivel = g && g.levels ? g.levels.slug : null;
    return { uid: uid, est: est.data, nivel: nivel, grado: g,
             avatar: Wave.avatar.limpiar(pf.data && pf.data.avatar_config, nivel) };
  }

  function dato(icono, rotulo, valor, extra) {
    return '<div class="perfil-dato"><span class="perfil-dato-ico">' + icono + '</span>' +
      '<div><small>' + rotulo + '</small><b>' + (valor ? esc(valor) : '—') + '</b>' +
      (extra ? '<em>' + esc(extra) + '</em>' : '') + '</div></div>';
  }

  var ICO = {
    user: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg>',
    cal: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>',
    id: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="9" cy="11" r="2"/><path d="M6 16c.6-1.6 1.8-2.4 3-2.4s2.4.8 3 2.4M15 10h3M15 14h3"/></svg>',
    cap: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5"/></svg>',
    lapiz: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>'
  };

  function pintarPerfil(cont, d) {
    var e = d.est || {};
    var nombreCompleto = ((e.first_name || '') + ' ' + (e.last_name || '')).trim();
    var g = d.grado;
    var nivelTxt = g && g.levels ? g.levels.name : '';
    var gradoTxt = g ? (g.levels && g.levels.slug === 'inicial' ? g.levels.name : g.name + ' · ' + nivelTxt) : '';
    var nac = fechaNac(e.birth_date);
    var nacTxt = nac ? nac.toLocaleDateString('es-AR', { day: 'numeric', month: 'long', year: 'numeric' }) : '';
    var edadTxt = nac ? edadDe(nac) + ' años' : '';

    cont.innerHTML =
      '<section class="perfil-hero">' +
        '<div class="perfil-avatar-wrap"><div class="perfil-avatar" id="perfil-avatar">' + Wave.avatar.svg(d.avatar, d.nivel, 132) + '</div>' +
        '<button type="button" class="perfil-avatar-btn" id="perfil-cambiar" aria-label="Cambiar avatar">' + ICO.lapiz + '</button></div>' +
        '<div class="perfil-hero-txt">' +
          '<h2>' + esc(nombreCompleto || 'Mi perfil') + '</h2>' +
          (gradoTxt ? '<span class="perfil-chip">' + esc(gradoTxt) + '</span>' : '') +
          '<button type="button" class="perfil-cambiar-txt" id="perfil-cambiar-2">Cambiar mi avatar</button>' +
        '</div>' +
      '</section>' +
      '<h2 class="vista-subtitulo">Mis datos</h2>' +
      '<div class="perfil-datos">' +
        dato(ICO.user, 'Nombre', e.first_name) +
        dato(ICO.user, 'Apellido', e.last_name) +
        dato(ICO.cal, 'Fecha de nacimiento', nacTxt, edadTxt) +
        dato(ICO.id, 'Documento', e.document_number) +
        dato(ICO.cap, 'Año', g ? (g.levels && g.levels.slug === 'inicial' ? g.levels.name : g.name) : '', g && g.levels && g.levels.slug !== 'inicial' ? nivelTxt : '') +
      '</div>' +
      '<p class="perfil-nota">Estos datos los completa tu familia. Si ves algo para corregir, avisales a ellos.</p>';

    var abrir = function () { abrirEditorAvatar(d, function (nuevo) {
      d.avatar = nuevo;
      document.getElementById('perfil-avatar').innerHTML = Wave.avatar.svg(nuevo, d.nivel, 132);
    }); };
    document.getElementById('perfil-cambiar').addEventListener('click', abrir);
    document.getElementById('perfil-cambiar-2').addEventListener('click', abrir);
  }

  function swatches(nombre, colores, actual) {
    return '<div class="av-swatches">' + colores.map(function (c, i) {
      return '<button type="button" class="av-sw' + (actual === i || actual === c ? ' sel' : '') + '" data-k="' + nombre + '" data-v="' + (typeof actual === 'string' ? c : i) + '" style="background:' + c + '" aria-label="Opción ' + (i + 1) + '"></button>';
    }).join('') + '</div>';
  }

  function abrirEditorAvatar(d, alGuardar) {
    var A = Wave.avatar;
    var cfg = JSON.parse(JSON.stringify(d.avatar));
    var veil = document.createElement('div');
    veil.className = 'av-veil';
    veil.innerHTML = '<div class="av-modal" role="dialog" aria-modal="true" aria-label="Elegí tu avatar"></div>';
    document.body.appendChild(veil);
    document.body.classList.add('av-abierto');
    var modal = veil.firstChild;

    function cerrar() { document.body.classList.remove('av-abierto'); veil.remove(); }

    function dibujar() {
      var cuerpo = '';
      if (cfg.t === 'animal') {
        cuerpo += '<p class="av-rotulo">Elegí tu animalito</p><div class="av-grilla">' +
          A.ANIMALES.map(function (a) {
            var c = { t: 'animal', a: a[0], f: cfg.f };
            return '<button type="button" class="av-op' + (cfg.a === a[0] ? ' sel' : '') + '" data-k="a" data-v="' + a[0] + '">' +
              A.svg(c, d.nivel, 64) + '<span>' + a[1] + '</span></button>';
          }).join('') + '</div>';
      } else {
        cuerpo += '<p class="av-rotulo">Peinado</p><div class="av-grilla">' +
          A.ESTILOS.map(function (n, i) {
            var c = JSON.parse(JSON.stringify(cfg)); c.estilo = i;
            return '<button type="button" class="av-op' + (cfg.estilo === i ? ' sel' : '') + '" data-k="estilo" data-v="' + i + '">' +
              A.svg(c, d.nivel, 64) + '<span>' + n + '</span></button>';
          }).join('') + '</div>' +
          '<p class="av-rotulo">Piel</p>' + swatches('piel', A.PIELES, cfg.piel) +
          '<p class="av-rotulo">Color de pelo</p>' + swatches('pelo', A.PELOS, cfg.pelo) +
          '<p class="av-rotulo">Ropa</p>' + swatches('ropa', A.ROPAS, cfg.ropa);
      }
      cuerpo += '<p class="av-rotulo">Fondo</p>' + swatches('f', A.FONDOS, cfg.f);

      modal.innerHTML =
        '<div class="av-cab"><h3>Elegí tu avatar</h3><button type="button" class="av-x" data-a="cerrar" aria-label="Cerrar">×</button></div>' +
        '<div class="av-previa">' + A.svg(cfg, d.nivel, 120) + '</div>' +
        '<div class="av-cuerpo">' + cuerpo + '</div>' +
        '<p class="av-error" id="av-error" hidden></p>' +
        '<div class="av-pie"><button type="button" class="av-btn sec" data-a="cerrar">Cancelar</button>' +
        '<button type="button" class="av-btn" data-a="guardar" id="av-guardar">Guardar</button></div>';
    }

    veil.addEventListener('click', async function (ev) {
      if (ev.target === veil) { cerrar(); return; }
      var b = ev.target.closest('[data-k],[data-a]');
      if (!b) return;
      if (b.hasAttribute('data-k')) {
        var k = b.getAttribute('data-k'), v = b.getAttribute('data-v');
        cfg[k] = (k === 'a' || k === 'f') ? v : Number(v);
        var sc = modal.querySelector('.av-cuerpo').scrollTop;
        dibujar();
        modal.querySelector('.av-cuerpo').scrollTop = sc;
        return;
      }
      var acc = b.getAttribute('data-a');
      if (acc === 'cerrar') { cerrar(); return; }
      if (acc === 'guardar') {
        var btn = document.getElementById('av-guardar');
        btn.disabled = true; btn.textContent = 'Guardando…';
        var limpio = A.limpiar(cfg, d.nivel);
        var r = await sb.from('profiles').update({ avatar_config: limpio }).eq('id', d.uid);
        if (r.error) {
          var er = document.getElementById('av-error');
          er.textContent = 'No pudimos guardar tu avatar. Probá de nuevo.'; er.hidden = false;
          btn.disabled = false; btn.textContent = 'Guardar';
          return;
        }
        cerrar();
        alGuardar(limpio);
      }
    });
    dibujar();
  }

  async function vistaPerfil() {
    vista.innerHTML = '<h1 class="vista-titulo">Perfil</h1><div id="perfil"></div>';
    var cont = document.getElementById('perfil');
    cont.innerHTML = '<div class="vacio">Cargando tu perfil…</div>';
    try {
      pintarPerfil(cont, await cargarPerfil());
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar tu perfil. Probá recargar la página.</div>';
    }
  }

  var VISTAS = {
    cursos: vistaCursos,
    programacion: vistaProgramacion,
    estadisticas: vistaEstadisticas,
    perfil: vistaPerfil
  };

  function ruta() {
    var nombre = (location.hash || '#cursos').slice(1);
    if (!VISTAS[nombre]) nombre = 'cursos';
    enlaces.forEach(function (a) {
      a.classList.toggle('activo', a.getAttribute('href') === '#' + nombre);
    });
    VISTAS[nombre]();
  }

  // Marca el primer ingreso: desde ahí corre el plazo objetivo (la base lo guarda solo una vez)
  sb.rpc('mark_student_started').then(function () {}, function () {});

  window.addEventListener('hashchange', ruta);
  ruta();
})();
