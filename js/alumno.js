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

    return materias.map(function (m) {
      return { id: m.id, nombre: m.name, color: colorSeguro(m.color),
               total: total[m.id] || 0, completas: completas[m.id] || 0 };
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
          '<div class="curso-fila"><span>' + c.completas + ' de ' + c.total + ' lecciones</span><b>' + pct + '%</b></div>' +
          '<div class="curso-barra" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct + '"><span style="width:' + pct + '%"></span></div>' +
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

  var VISTAS = {
    cursos: vistaCursos,
    programacion: function () { vistaProximamente('Programación'); },
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
