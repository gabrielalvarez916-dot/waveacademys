// Panel de dirección (Primaria e Inicial / Secundaria): alumnos de su nivel, tutores y agenda propia.
(function () {
  var sb = Wave.sb;
  var vista = document.getElementById('vista');
  var enlaces = document.querySelectorAll('.nav-dir a');
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function toast(t, err) { var e = document.createElement('div'); e.className = 'cal-toast' + (err ? ' err' : ''); e.textContent = t; document.body.appendChild(e); setTimeout(function () { e.remove(); }, 3500); }
  function haceCuanto(iso) {
    if (!iso) return 'Nunca ingresó';
    var d = Math.floor((Date.now() - new Date(iso).getTime()) / 86400000);
    return d <= 0 ? 'Hoy' : d === 1 ? 'Ayer' : 'Hace ' + d + ' días';
  }

  // ---------- Familias y alumnos (solo de su nivel) ----------
  async function vistaAlumnos() {
    vista.innerHTML = '<h1 class="vista-titulo">Familias y alumnos</h1><div class="wv-vacio">Cargando…</div>';
    var r = await sb.rpc('dir_alumnos');
    if (r.error) { vista.innerHTML = '<h1 class="vista-titulo">Familias y alumnos</h1><div class="wv-vacio">' + esc(r.error.message) + '</div>'; return; }
    var a = r.data || [], porNivel = {};
    a.forEach(function (x) { (porNivel[x.nivel] = porNivel[x.nivel] || []).push(x); });
    var niveles = Object.keys(porNivel);
    vista.innerHTML = '<h1 class="vista-titulo">Familias y alumnos</h1>' +
      '<div class="wv-resumen"><div class="wv-stat"><small>Alumnos</small><b>' + a.length + '</b></div>' + niveles.map(function (n) { return '<div class="wv-stat"><small>' + esc(n) + '</small><b>' + porNivel[n].length + '</b></div>'; }).join('') + '</div>' +
      '<input id="dir-buscar" class="wv-buscar" type="search" placeholder="Buscar por alumno, familia o correo" style="width:100%;max-width:420px;min-height:44px;padding:0 14px;margin:0 0 14px;border:2px solid #cfdcdb;border-radius:12px;font:inherit">' +
      '<div id="dir-lista"></div>';
    function pintar() {
      var q = document.getElementById('dir-buscar').value.trim().toLowerCase();
      var f = a.filter(function (x) { return !q || [x.alumno, x.familia, x.email].join(' ').toLowerCase().indexOf(q) >= 0; });
      document.getElementById('dir-lista').innerHTML = f.length ? '<div class="wv-alus">' + f.map(function (x) {
        return '<div class="wv-alu"><div><div class="wv-nombre">' + esc(x.alumno) + '</div><div class="wv-dato">' + esc(x.nivel.replace('Nivel ', '')) + (x.anio !== x.nivel ? ' · ' + esc(x.anio) : '') + '</div></div>' +
          '<div><div class="wv-dato"><b>' + esc(x.familia || '') + '</b></div><div class="wv-dato">' + esc(x.email || '') + (x.telefono ? ' · ' + esc(x.telefono) : '') + '</div></div>' +
          '<div><span class="wv-rot">Último ingreso</span><span class="wv-dato">' + esc(haceCuanto(x.ultimo_ingreso)) + '</span></div></div>';
      }).join('') + '</div>' : '<div class="wv-vacio">No hay alumnos para mostrar.</div>';
    }
    document.getElementById('dir-buscar').oninput = pintar; pintar();
  }

  // ---------- Tutores: alta y listado ----------
  async function vistaEquipo() {
    vista.innerHTML = '<h1 class="vista-titulo">Tutores</h1>' +
      '<p class="wv-dato">Dás de alta a los tutores, que acompañan a los alumnos de las modalidades Guiada y Completa. Se les crea el usuario con una clave inicial que deben cambiar al ingresar.</p>' +
      '<form id="dir-tut" class="wv-tut-form"><input id="dir-tut-nom" placeholder="Nombre y apellido" required> <input id="dir-tut-mail" type="email" placeholder="Correo" required> <button class="wv-btn" type="submit">Crear tutor</button></form>' +
      '<div id="dir-cred"></div><div id="dir-tutores"><div class="wv-vacio">Cargando…</div></div>';
    async function pintar() {
      var r = await sb.rpc('tutores_equipo'), c = document.getElementById('dir-tutores');
      if (r.error) { c.innerHTML = '<div class="wv-vacio">' + esc(r.error.message) + '</div>'; return; }
      c.innerHTML = (r.data || []).length ? '<div class="wv-alus">' + r.data.map(function (t) {
        return '<div class="wv-alu"><div><div class="wv-nombre">' + esc(t.nombre || t.email) + '</div><div class="wv-dato">' + esc(t.email) + '</div></div><div><span class="wv-rot">Alumnos</span><span class="wv-dato">' + t.alumnos + '</span></div></div>';
      }).join('') + '</div>' : '<div class="wv-vacio">Todavía no hay tutores.</div>';
    }
    document.getElementById('dir-tut').onsubmit = async function (ev) {
      ev.preventDefault(); var b = this.querySelector('button'); b.disabled = true;
      var r = await sb.functions.invoke('admin-tutores', { body: { nombre: document.getElementById('dir-tut-nom').value, email: document.getElementById('dir-tut-mail').value, rol: 'tutor' } });
      b.disabled = false;
      if (r.error || (r.data && r.data.error)) { toast((r.data && r.data.error) || 'No se pudo crear el tutor', true); return; }
      document.getElementById('dir-cred').innerHTML = '<div class="wv-vacio">Tutor creado. Usuario: <b>' + esc(r.data.email) + '</b> · Clave inicial: <b>' + esc(r.data.initial_password) + '</b> (anotala: no se vuelve a mostrar).</div>';
      this.reset(); pintar();
    };
    pintar();
  }

  // ---------- Agenda propia ----------
  var DIAS = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
  async function vistaAgenda() {
    vista.innerHTML = '<h1 class="vista-titulo">Agenda</h1>' +
      '<p class="wv-dato">Tus reuniones en un calendario. Tocá una para entrar a la videollamada, reagendarla, cancelarla o cerrarla. Entrá vos primero: hasta que entres, la sala no se abre.</p><div id="dir-cal"></div>' +
      '<h2 class="wv-sub" style="margin-top:28px">Mis horarios de atención</h2>' +
      '<form id="dir-hf" class="wv-tut-form"><select id="dir-dia">' + DIAS.slice(1).map(function (d, i) { return '<option value="' + (i + 1) + '">' + d + '</option>'; }).join('') + '</select> de <input id="dir-desde" type="time" value="10:00" required> a <input id="dir-hasta" type="time" value="13:00" required> turnos de <select id="dir-dur"><option>15</option><option selected>30</option><option>45</option><option>60</option></select> min <button class="wv-btn" type="submit">Agregar horario</button></form><div id="dir-horas"></div><div id="dir-bloq"></div>';
    var ses = await sb.auth.getSession(), yo = ses.data.session.user.id;
    WaveCal.semana(document.getElementById('dir-cal'), {
      filtros: true, contacto: true,
      cargar: async function () {
        var r = await sb.rpc('mi_agenda'); if (r.error) throw r.error;
        return (r.data || []).map(function (t) {
          return { id: t.id, tipo: t.tipo, titulo: t.tipo === 'tutoria' ? (t.alumno || 'Tutoría') : (t.participante || 'Reunión'), sub: t.tipo === 'tutoria' ? '' : (t.motivo || ''), inicio: t.inicio, fin: t.fin, estado: t.estado, link: t.link,
            participante: t.participante, alumno: t.alumno, motivo: t.motivo, tema: t.tema, notas: t.notas, email: t.email, telefono: t.telefono, reag: t.reagendada_veces };
        });
      }
    });
    WaveCal.bloqueos(document.getElementById('dir-bloq'));
    async function horas() {
      var r = await sb.from('tutor_disponibilidad').select('id, dia_semana, desde, hasta, duracion_min').eq('tutor_id', yo).order('dia_semana').order('desde');
      document.getElementById('dir-horas').innerHTML = !(r.data || []).length ? '<div class="wv-vacio">Todavía no cargaste horarios.</div>' : '<div class="wv-alus">' + r.data.map(function (h) {
        return '<div class="wv-alu"><div class="wv-dato"><b>' + DIAS[h.dia_semana] + '</b> de ' + h.desde.slice(0, 5) + ' a ' + h.hasta.slice(0, 5) + ' h · turnos de ' + h.duracion_min + ' min</div><button type="button" class="wv-btn" data-borrar="' + h.id + '">Quitar</button></div>';
      }).join('') + '</div>';
    }
    document.getElementById('dir-hf').onsubmit = async function (ev) {
      ev.preventDefault();
      var r = await sb.from('tutor_disponibilidad').insert({ tutor_id: yo, dia_semana: +document.getElementById('dir-dia').value, desde: document.getElementById('dir-desde').value, hasta: document.getElementById('dir-hasta').value, duracion_min: +document.getElementById('dir-dur').value });
      if (r.error) toast('No se pudo guardar el horario', true); else { toast('Horario agregado'); horas(); }
    };
    document.getElementById('dir-horas').onclick = async function (ev) {
      var b = ev.target.closest('[data-borrar]'); if (!b) return;
      var r = await sb.from('tutor_disponibilidad').delete().eq('id', b.getAttribute('data-borrar'));
      if (r.error) toast('No se pudo quitar', true); else horas();
    };
    horas();
  }

  var VISTAS = { alumnos: vistaAlumnos, equipo: vistaEquipo, agenda: vistaAgenda };
  function ruta() {
    var h = (location.hash || '#alumnos').slice(1); if (!VISTAS[h]) h = 'alumnos';
    enlaces.forEach(function (a) { a.classList.toggle('activo', a.getAttribute('href') === '#' + h); });
    Promise.resolve(VISTAS[h]()).catch(function (e) { console.error(e); vista.innerHTML = '<div class="wv-vacio">Ocurrió un error al armar el panel.</div>'; });
  }
  window.addEventListener('hashchange', ruta);
  ruta();
})();
