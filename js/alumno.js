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
          '<div class="curso-cabeza"><div class="curso-icono">' + esc(c.nombre.charAt(0)) + '</div>' +
          '<h2>' + esc(c.nombre) + '</h2></div>' +
          '<div class="curso-fila"><span>Progreso</span><b>' + c.completas + ' de ' + c.total + ' · ' + pct + '%</b></div>' +
          '<div class="curso-barra" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct + '"><span style="width:' + pct + '%"></span></div>' +
          '<p class="curso-pie">lecciones completadas</p>' +
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
