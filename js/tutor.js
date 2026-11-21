// Panel del tutor: alumnos, agenda de tutorías, horarios disponibles y corrección de proyectos y escritura.
(function () {
  var sb = Wave.sb;
  var vista = document.getElementById('vista');
  var enlaces = document.querySelectorAll('.nav-familia a');
  var DIAS = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
  var MODS = { libre: 'Libre', guiada: 'Guiada', completa: 'Completa', personalizada: 'Personalizada' };

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function fecha(v) {
    var d = new Date(v);
    return d.toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · ' +
      d.toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + ' h';
  }
  function aviso(cont, txt) { cont.innerHTML = '<div class="vacio">' + esc(txt) + '</div>'; }
  function toast(t, err) {
    var el = document.createElement('div'); el.className = 'tu-toast' + (err ? ' err' : ''); el.textContent = t;
    document.body.appendChild(el); setTimeout(function () { el.remove(); }, 3500);
  }

  // ---------- Mis alumnos ----------
  async function vistaAlumnos() {
    vista.innerHTML = '<h1 class="vista-titulo">Mis alumnos</h1><div id="tu-cont"><div class="vacio">Cargando…</div></div>';
    var c = document.getElementById('tu-cont');
    var r = await sb.rpc('tutor_mis_alumnos');
    var TOPES = (await sb.rpc('tutorias_por_mes')).data || {};
    if (r.error) return aviso(c, 'No pudimos cargar tus alumnos.');
    if (!r.data.length) return aviso(c, 'Todavía no tenés alumnos asignados. Cuando el administrador te asigne alumnos, van a aparecer acá.');
    c.innerHTML = '<div class="tu-grilla">' + r.data.map(function (a) {
      return '<section class="fa-card tu-alu"><h2>' + esc(a.nombre) + '</h2><span class="tu-sub">' + esc(a.anio) + ' · ' + esc(MODS[a.modalidad] || a.modalidad) + '</span>' +
        '<div class="fa-datos">' +
          '<div class="fa-dato"><small>Correcciones pendientes</small><b>' + a.pendientes + '</b></div>' +
          '<div class="fa-dato"><small>Tutorías este mes</small><b>' + a.tutorias_mes + ' de ' + (TOPES[a.modalidad] || 2) + '</b></div>' +
          '<div class="fa-dato"><small>Próxima tutoría</small><b>' + (a.proxima ? esc(fecha(a.proxima)) : '—') + '</b></div>' +
        '</div></section>';
    }).join('') + '</div>';
  }

  // ---------- Agenda ----------
  async function vistaAgenda() {
    vista.innerHTML = '<h1 class="vista-titulo">Agenda de tutorías</h1>' +
      '<p class="fa-intro">Tocá una tutoría para entrar, reagendarla, cancelarla o cerrarla con tus notas para la familia. Entrá vos primero a la videollamada, con tu cuenta de Google: hasta que entres, la sala no se abre y la familia queda esperando.</p>' +
      '<div id="tu-cal"></div>';
    WaveCal.semana(document.getElementById('tu-cal'), {
      cargar: async function () {
        var r = await sb.rpc('tutor_agenda');
        if (r.error) throw r;
        return (r.data || []).map(function (t) {
          return { id: t.id, tipo: 'tutoria', titulo: t.alumno, sub: '', inicio: t.inicio, fin: t.fin, estado: t.estado, link: t.link,
            alumno: t.alumno, tema: t.tema, notas: t.notas_tutor };
        });
      }
    });
  }

  // ---------- Mis horarios ----------
  async function vistaHorarios() {
    vista.innerHTML = '<h1 class="vista-titulo">Mis horarios</h1>' +
      '<p class="fa-intro">Cargá los horarios de cada semana en que podés dar tutorías (hora de Argentina). Las familias eligen turno dentro de estos horarios. Cada alumno tiene 2 tutorías por mes en Libre y 4 en Guiada y Completa.</p>' +
      '<form id="tu-form" class="fa-card tu-form">' +
        '<select id="tu-dia" aria-label="Día">' + DIAS.slice(1).map(function (d, i) { return '<option value="' + (i + 1) + '">' + d + '</option>'; }).join('') + '</select>' +
        '<label>De <input id="tu-desde" type="time" value="15:00" required></label>' +
        '<label>a <input id="tu-hasta" type="time" value="18:00" required></label>' +
        '<label>Turnos de <select id="tu-dur"><option>30</option><option selected>45</option><option>60</option></select> min</label>' +
        '<button class="boton fa-boton" type="submit">Agregar</button></form>' +
      '<div id="tu-cont"><div class="vacio">Cargando…</div></div><div id="tu-bloq"></div>';
    var c = document.getElementById('tu-cont');
    WaveCal.bloqueos(document.getElementById('tu-bloq'));
    async function pintar() {
      var r = await sb.from('tutor_disponibilidad').select('id, dia_semana, desde, hasta, duracion_min').order('dia_semana').order('desde');
      if (r.error) return aviso(c, 'No pudimos cargar tus horarios.');
      c.innerHTML = !r.data.length ? '<div class="vacio">Todavía no cargaste horarios: sin horarios, las familias no pueden reservar.</div>' :
        r.data.map(function (h) {
          return '<div class="fa-card tu-hora"><b>' + DIAS[h.dia_semana] + '</b> de ' + h.desde.slice(0, 5) + ' a ' + h.hasta.slice(0, 5) +
            ' h · turnos de ' + h.duracion_min + ' min <button type="button" class="tu-link" data-borrar="' + h.id + '">Quitar</button></div>';
        }).join('');
    }
    document.getElementById('tu-form').onsubmit = async function (ev) {
      ev.preventDefault();
      var ses = await sb.auth.getSession();
      var r = await sb.from('tutor_disponibilidad').insert({ tutor_id: ses.data.session.user.id, dia_semana: +document.getElementById('tu-dia').value,
        desde: document.getElementById('tu-desde').value, hasta: document.getElementById('tu-hasta').value, duracion_min: +document.getElementById('tu-dur').value });
      if (r.error) return toast(/hasta/.test(r.error.message) ? 'La hora de fin tiene que ser después de la de inicio' : 'No se pudo guardar', true);
      toast('Horario agregado'); pintar();
    };
    c.onclick = async function (ev) {
      var b = ev.target.closest('[data-borrar]'); if (!b) return;
      var r = await sb.from('tutor_disponibilidad').delete().eq('id', b.getAttribute('data-borrar'));
      if (r.error) return toast('No se pudo quitar', true);
      pintar();
    };
    pintar();
  }

  // ---------- Correcciones ----------
  async function vistaCorrecciones(estado) {
    estado = estado || 'pendiente';
    vista.innerHTML = '<h1 class="vista-titulo">Correcciones</h1>' +
      '<p class="fa-intro">Proyectos y respuestas escritas de tus alumnos. La IA ya las corrigió: revisá, ajustá la nota si hace falta y dejales un comentario.</p>' +
      '<div class="tu-filtro"><button type="button" class="tu-chip' + (estado === 'pendiente' ? ' on' : '') + '" data-est="pendiente">Pendientes</button>' +
      '<button type="button" class="tu-chip' + (estado === 'revisada' ? ' on' : '') + '" data-est="revisada">Ya revisadas</button></div>' +
      '<div id="tu-cont"><div class="vacio">Cargando…</div></div>';
    vista.querySelector('.tu-filtro').onclick = function (ev) { var b = ev.target.closest('[data-est]'); if (b) vistaCorrecciones(b.getAttribute('data-est')); };
    var c = document.getElementById('tu-cont');
    var r = await sb.rpc('tutor_revisiones', { p_estado: estado });
    if (r.error) return aviso(c, 'No pudimos cargar las correcciones.');
    if (!r.data.length) return aviso(c, estado === 'pendiente' ? '¡Al día! No hay nada para corregir.' : 'Todavía no revisaste nada.');
    c.innerHTML = r.data.map(function (v) {
      var nota = v.nota_tutor != null ? v.nota_tutor : v.nota_ia;
      return '<section class="fa-card tu-rev" data-id="' + v.id + '">' +
        '<span class="tu-sub">' + esc(v.alumno) + ' · ' + esc(v.materia) + ' · ' + esc(v.mision) + (v.es_proyecto ? ' · <b>Proyecto</b>' : '') + '</span>' +
        '<h2 class="tu-preg">' + esc(v.pregunta) + '</h2>' +
        '<div class="tu-resp">' + esc(v.respuesta || '(sin respuesta)') + '</div>' +
        '<p class="tu-ia"><b>Corrección de la IA: ' + Math.round(v.nota_ia || 0) + '/100.</b> ' + esc(v.devolucion_ia || '') + '</p>' +
        '<div class="tu-calif"><label>Nota <input type="number" min="0" max="100" class="tu-nota" value="' + Math.round(nota || 0) + '">/100</label></div>' +
        '<textarea class="tu-notas" placeholder="Comentario para el alumno (lo ve en su devolución)">' + esc(v.comentario || '') + '</textarea>' +
        '<button type="button" class="boton fa-boton" data-guardar>' + (estado === 'pendiente' ? 'Guardar corrección' : 'Actualizar') + '</button></section>';
    }).join('');
    c.onclick = async function (ev) {
      var b = ev.target.closest('[data-guardar]'); if (!b) return;
      var card = b.closest('[data-id]'), n = Number(card.querySelector('.tu-nota').value);
      if (!(n >= 0 && n <= 100)) return toast('La nota va de 0 a 100', true);
      b.disabled = true;
      var x = await sb.rpc('revisar_respuesta', { p_id: card.getAttribute('data-id'), p_nota: n, p_comentario: card.querySelector('.tu-notas').value });
      if (x.error) { b.disabled = false; return toast(x.error.message, true); }
      toast('Corrección guardada');
      if (estado === 'pendiente') card.remove(); else b.disabled = false;
      if (!c.querySelector('[data-id]')) aviso(c, '¡Al día! No hay nada para corregir.');
    };
  }

  var VISTAS = { alumnos: vistaAlumnos, agenda: vistaAgenda, horarios: vistaHorarios, correcciones: function () { return vistaCorrecciones(); } };
  function ruta() {
    var n = (location.hash || '#alumnos').slice(1);
    if (!VISTAS[n]) n = 'alumnos';
    enlaces.forEach(function (a) { a.classList.toggle('activo', a.getAttribute('href') === '#' + n); });
    VISTAS[n]();
  }
  window.addEventListener('hashchange', ruta);
  ruta();
})();
