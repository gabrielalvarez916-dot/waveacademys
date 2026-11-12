// Panel de familias: navegación y sección Altas.
(function () {
  var sb = Wave.sb;
  var vista = document.getElementById('vista');
  var enlaces = document.querySelectorAll('.nav-familia a');

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // "Nivel Medio · Año 3" (el Nivel Inicial tiene un único año y se muestra solo)
  function etiquetaAnio(g) {
    var nivel = g.levels ? g.levels.name : '';
    if (!nivel || nivel === g.name) return g.name;
    return nivel + ' · ' + g.name;
  }

  // ---------- Datos ----------
  async function cargarDatos() {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;

    var fam = await sb.from('families').select('id').eq('profile_id', uid).maybeSingle();
    if (fam.error) throw fam.error;
    if (!fam.data) throw new Error('Sin familia');

    var res = await Promise.all([
      sb.from('subscriptions').select('id, student_id, status').eq('family_id', fam.data.id),
      sb.from('students')
        .select('id, first_name, last_name, grade_id, created_at, grades(name, levels(name)), profiles!students_profile_id_fkey(email)')
        .eq('family_id', fam.data.id)
        .order('created_at', { ascending: true }),
      sb.from('grades').select('id, year_number, name, levels(name, position)')
    ]);
    res.forEach(function (r) { if (r.error) throw r.error; });

    var cupos = (res[0].data || []).filter(function (s) {
      return !s.student_id && (s.status === 'active' || s.status === 'past_due');
    }).length;

    var anios = (res[2].data || []).slice().sort(function (a, b) {
      var pa = a.levels ? a.levels.position : 0, pb = b.levels ? b.levels.position : 0;
      return pa - pb || a.year_number - b.year_number;
    });

    return { cupos: cupos, hijos: res[1].data || [], anios: anios };
  }

  // La función devuelve el motivo del error en el cuerpo de la respuesta
  async function mensajeDeError(err) {
    try {
      if (err && err.context && typeof err.context.json === 'function') {
        var cuerpo = await err.context.json();
        if (cuerpo && cuerpo.error) return cuerpo.error;
      }
    } catch (e) { /* cae al mensaje genérico */ }
    return 'No se pudo dar de alta al estudiante. Intentá de nuevo.';
  }

  // ---------- Altas ----------
  function pintarCredenciales(cont, c, nombre) {
    cont.innerHTML =
      '<section class="cred" aria-live="polite">' +
        '<h2>¡' + esc(nombre) + ' ya está dado/a de alta!</h2>' +
        '<p>Guardá estos datos: son los que va a usar para ingresar. Al entrar por primera vez le va a pedir que cambie la contraseña.</p>' +
        '<div class="cred-fila"><div><small>Usuario</small><b>' + esc(c.username) + '</b></div>' +
          '<button type="button" class="cred-copiar" data-copiar="' + esc(c.username) + '">Copiar</button></div>' +
        '<div class="cred-fila"><div><small>Contraseña inicial</small><b>' + esc(c.initial_password) + '</b></div>' +
          '<button type="button" class="cred-copiar" data-copiar="' + esc(c.initial_password) + '">Copiar</button></div>' +
        '<button type="button" class="cred-cerrar" data-cerrar>Listo, ya los guardé</button>' +
      '</section>';

    cont.onclick = function (ev) {
      var btn = ev.target.closest('[data-copiar]');
      if (btn) {
        var texto = btn.getAttribute('data-copiar');
        var ok = function () { btn.textContent = '¡Copiado!'; setTimeout(function () { btn.textContent = 'Copiar'; }, 1500); };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(texto).then(ok, function () {});
        }
        return;
      }
      if (ev.target.closest('[data-cerrar]')) cont.innerHTML = '';
    };
  }

  function pintarAltas(cont, d) {
    var sinCupo = d.cupos < 1;

    var cupos =
      '<div class="cupos' + (sinCupo ? ' sin' : '') + '">' +
        '<div><span class="cupos-rotulo">Cupos disponibles</span><span class="cupos-valor">' + d.cupos + '</span></div>' +
        '<p class="cupos-txt">' + (sinCupo
          ? 'No tenés suscripciones pagas libres. Para dar de alta a un hijo, primero abonás su suscripción en Facturación.'
          : 'Cada cupo corresponde a una suscripción paga y se usa al dar de alta a un hijo.') + '</p>' +
      '</div>';

    var opciones = '<option value="" disabled selected>Elegí el año</option>' +
      d.anios.map(function (g) { return '<option value="' + esc(g.id) + '">' + esc(etiquetaAnio(g)) + '</option>'; }).join('');

    var dis = sinCupo ? ' disabled' : '';
    var form =
      '<form class="alta-form" id="alta-form" novalidate>' +
        '<h2>Dar de alta a un hijo</h2>' +
        '<p class="bajada">Completá sus datos y le creamos el usuario para ingresar a su aula.</p>' +
        '<div class="alta-grilla">' +
          '<div class="campo"><label for="a-nombre">Nombre</label><input id="a-nombre" type="text" autocomplete="off" maxlength="60" placeholder="Nombre"' + dis + '></div>' +
          '<div class="campo"><label for="a-apellido">Apellido</label><input id="a-apellido" type="text" autocomplete="off" maxlength="60" placeholder="Apellido"' + dis + '></div>' +
          '<div class="campo"><label for="a-nac">Fecha de nacimiento</label><input id="a-nac" type="date"' + dis + '></div>' +
          '<div class="campo"><label for="a-dni">DNI</label><input id="a-dni" type="text" inputmode="numeric" autocomplete="off" maxlength="15" placeholder="Número de documento"' + dis + '></div>' +
          '<div class="campo ancho"><label for="a-anio">Año que cursa</label><select id="a-anio"' + dis + '>' + opciones + '</select></div>' +
        '</div>' +
        '<p class="mensaje" id="a-error" hidden></p>' +
        '<button class="boton" type="submit" id="a-enviar"' + dis + '>Dar de alta</button>' +
      '</form>';

    var lista = d.hijos.length
      ? '<h2 class="vista-subtitulo">Tus hijos</h2><div class="hijos">' + d.hijos.map(function (h) {
          var ini = (h.first_name || '?').charAt(0) + (h.last_name || '').charAt(0);
          var usuario = h.profiles && h.profiles.email ? h.profiles.email : '';
          return '<div class="hijo"><div class="hijo-ini">' + esc(ini.toUpperCase()) + '</div>' +
            '<div class="hijo-info"><b>' + esc(h.first_name + ' ' + h.last_name) + '</b>' +
            '<span>' + esc(h.grades ? etiquetaAnio(h.grades) : '') + '</span>' +
            (usuario ? '<span>' + esc(usuario) + '</span>' : '') + '</div></div>';
        }).join('') + '</div>'
      : '';

    cont.innerHTML = cupos + '<div id="cred"></div>' + form + lista;

    var f = document.getElementById('alta-form');
    var err = document.getElementById('a-error');
    var btn = document.getElementById('a-enviar');

    function mostrarError(t) { err.textContent = t; err.hidden = false; }

    f.addEventListener('submit', async function (ev) {
      ev.preventDefault();
      if (sinCupo) return;
      err.hidden = true;

      var nombre = document.getElementById('a-nombre').value.trim();
      var apellido = document.getElementById('a-apellido').value.trim();
      var nac = document.getElementById('a-nac').value;
      var dni = document.getElementById('a-dni').value.trim();
      var anio = document.getElementById('a-anio').value;

      if (!nombre || !apellido || !anio) { mostrarError('Completá nombre, apellido y el año que cursa.'); return; }
      if (nac && nac > new Date().toISOString().slice(0, 10)) { mostrarError('La fecha de nacimiento no puede ser futura.'); return; }

      btn.disabled = true; btn.textContent = 'Dando de alta…';
      var r = await sb.functions.invoke('create-student', {
        body: { first_name: nombre, last_name: apellido, birth_date: nac || null, document_number: dni || null, grade_id: anio }
      });

      if (r.error || !r.data || r.data.error) {
        mostrarError(r.error ? await mensajeDeError(r.error) : ((r.data && r.data.error) || 'No se pudo dar de alta. Intentá de nuevo.'));
        btn.disabled = false; btn.textContent = 'Dar de alta';
        return;
      }

      // Se vuelve a pintar la vista (cupos y lista actualizados) y se muestran las credenciales
      await vistaAltas();
      var credCont = document.getElementById('cred');
      if (credCont) {
        pintarCredenciales(credCont, r.data, nombre);
        credCont.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }

  async function vistaAltas() {
    vista.innerHTML = '<h1 class="vista-titulo">Altas</h1><div id="altas"></div>';
    var cont = document.getElementById('altas');
    cont.innerHTML = '<div class="vacio">Cargando…</div>';
    try {
      pintarAltas(cont, await cargarDatos());
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar esta sección. Probá recargar la página.</div>';
    }
  }

  // ---------- Progreso ----------
  function colorSeguro(c) {
    return /^#[0-9a-fA-F]{6}$/.test(c || '') ? c : '#6366F1';
  }

  // "Hoy, 20:43" · "Ayer, 09:10" · "Hace 3 días" · "Todavía no ingresó"
  function textoConexion(iso) {
    if (!iso) return 'Todavía no ingresó';
    var f = new Date(iso);
    if (isNaN(f.getTime())) return 'Sin datos';
    var ahora = new Date();
    var d0 = new Date(ahora.getFullYear(), ahora.getMonth(), ahora.getDate());
    var d1 = new Date(f.getFullYear(), f.getMonth(), f.getDate());
    var dias = Math.round((d0 - d1) / 86400000);
    var hora = String(f.getHours()).padStart(2, '0') + ':' + String(f.getMinutes()).padStart(2, '0');
    if (dias <= 0) return 'Hoy, ' + hora;
    if (dias === 1) return 'Ayer, ' + hora;
    if (dias < 7) return 'Hace ' + dias + ' días';
    return f.toLocaleDateString('es-AR', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  async function cargarProgreso() {
    var res = await Promise.all([
      sb.from('students')
        .select('id, first_name, last_name, created_at, grades(name, levels(name)), profiles!students_profile_id_fkey(last_seen_at)')
        .order('created_at', { ascending: true }),
      sb.rpc('family_progress')
    ]);
    res.forEach(function (r) { if (r.error) throw r.error; });

    var porHijo = {};
    (res[1].data || []).forEach(function (r) {
      (porHijo[r.student_id] = porHijo[r.student_id] || []).push(r);
    });

    return (res[0].data || []).map(function (h) {
      var materias = (porHijo[h.id] || []).map(function (r) {
        return {
          nombre: r.subject_name, color: colorSeguro(r.color), orden: r.subject_position,
          total: r.total_topics, hechas: r.done_topics,
          suma: Number(r.score_sum), notas: r.score_count,
          promedio: r.score_count ? Math.round(Number(r.score_sum) / r.score_count) : null
        };
      }).sort(function (a, b) { return a.orden - b.orden; });

      var total = 0, hechas = 0, suma = 0, notas = 0;
      materias.forEach(function (m) { total += m.total; hechas += m.hechas; suma += m.suma; notas += m.notas; });

      return {
        id: h.id, nombre: h.first_name + ' ' + h.last_name,
        anio: h.grades ? etiquetaAnio(h.grades) : '',
        conexion: h.profiles ? h.profiles.last_seen_at : null,
        materias: materias,
        pct: total ? Math.round((hechas / total) * 100) : 0,
        promedio: notas ? Math.round(suma / notas) : null
      };
    });
  }

  function pintarProgreso(cont, hijos) {
    if (!hijos.length) {
      cont.innerHTML = '<div class="vacio">Todavía no diste de alta a ningún hijo. Cuando lo hagas, acá vas a ver cómo avanza.</div>';
      return;
    }

    cont.innerHTML = hijos.map(function (h) {
      var ini = h.nombre.split(' ').map(function (p) { return p.charAt(0); }).slice(0, 2).join('').toUpperCase();

      var filas = h.materias.map(function (m) {
        var pct = m.total ? Math.round((m.hechas / m.total) * 100) : 0;
        return '<div class="pm-fila" style="--c:' + m.color + '">' +
          '<div class="pm-cab"><span class="pm-nombre">' + esc(m.nombre) + '</span>' +
            '<span class="pm-prom"><small>Promedio</small><b>' + (m.promedio == null ? '—' : m.promedio + '%') + '</b></span></div>' +
          '<div class="pm-barra" role="progressbar" aria-label="Progreso en ' + esc(m.nombre) + '" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct + '"><span style="width:' + pct + '%"></span></div>' +
          '<div class="pm-pie"><span>' + m.hechas + ' de ' + m.total + (m.total === 1 ? ' tema' : ' temas') + '</span><b>' + pct + '%</b></div>' +
        '</div>';
      }).join('');

      return '<section class="pr-hijo">' +
        '<div class="pr-hero">' +
          '<div class="pr-hero-top"><div class="hijo-ini pr-ini">' + esc(ini) + '</div>' +
            '<div><h2>' + esc(h.nombre) + '</h2><span class="pr-anio">' + esc(h.anio) + '</span></div></div>' +
          '<div class="pr-stats">' +
            '<div class="pr-stat"><small>Última conexión</small><b>' + esc(textoConexion(h.conexion)) + '</b></div>' +
            '<div class="pr-stat"><small>Progreso</small><b>' + h.pct + '%</b></div>' +
            '<div class="pr-stat"><small>Promedio general</small><b>' + (h.promedio == null ? '—' : h.promedio + '%') + '</b></div>' +
          '</div>' +
        '</div>' +
        '<div class="pr-materias">' +
          (filas || '<div class="vacio">Todavía no tiene materias habilitadas.</div>') +
        '</div>' +
      '</section>';
    }).join('');
  }

  async function vistaProgreso() {
    vista.innerHTML = '<h1 class="vista-titulo">Progreso</h1><div id="progreso"></div>';
    var cont = document.getElementById('progreso');
    cont.innerHTML = '<div class="vacio">Cargando…</div>';
    try {
      pintarProgreso(cont, await cargarProgreso());
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar el progreso. Probá recargar la página.</div>';
    }
  }

  // ---------- Programación (una por cada hijo, igual a la del panel estudiante) ----------
  var DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'];

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
    var n = String(nombre || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
    var clave = 'lengua';
    for (var i = 0; i < REGLAS.length; i++) {
      if (n.indexOf(REGLAS[i][0]) !== -1) { clave = REGLAS[i][1]; break; }
    }
    return '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + P[clave] + '</svg>';
  }

  function fechaLarga(d) {
    return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'long', year: 'numeric' });
  }
  function fechaCorta(d) {
    return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'short', year: 'numeric' });
  }
  function textoTemas(n) { return n + (n === 1 ? ' tema' : ' temas'); }

  // Día en que se terminan los temas que faltan, siguiendo el programa (de lunes a viernes)
  // Se cuentan 40 semanas activas por año (hay vacaciones y feriados): el calendario real es 52/40 más largo
  var FACTOR_CALENDARIO = 52 / 40;

  // Inicio (primer ingreso) + plazo elegido = fecha objetivo
  function fechaObjetivo(inicio, meses) {
    if (!inicio || !meses) return null;
    var f = new Date(inicio);
    f.setMonth(f.getMonth() + meses);
    f.setHours(12, 0, 0, 0);
    return isNaN(f.getTime()) ? null : f;
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

  // Cuántas veces por semana va cada materia: Lengua y Matemática 3, el resto 2
  function vecesPorSemana(nombre) {
    var n = String(nombre || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
    if (n.indexOf('lengua') !== -1 || n.indexOf('matemat') !== -1) return 3;
    return 2;
  }

  // Reparte las materias en la semana: cada una con sus días, parejo y evitando días seguidos
  function armarSemana(cursos) {
    var carga = [0, 0, 0, 0, 0, 0];
    var orden = cursos.map(function (c, i) { return { c: c, i: i, v: vecesPorSemana(c.nombre) }; })
      .sort(function (a, b) { return b.v - a.v || a.i - b.i; });
    var filas = [];
    orden.forEach(function (o) {
      var elegidos = [];
      for (var k = 0; k < Math.min(o.v, 5); k++) {
        var mejor = 0, mejorPuntaje = Infinity;
        for (var d = 1; d <= 5; d++) {
          if (elegidos.indexOf(d) !== -1) continue;
          var vecinos = (elegidos.indexOf(d - 1) !== -1 ? 1 : 0) + (elegidos.indexOf(d + 1) !== -1 ? 1 : 0);
          var puntaje = carga[d] * 100 + vecinos * 10 + d;
          if (puntaje < mejorPuntaje) { mejorPuntaje = puntaje; mejor = d; }
        }
        elegidos.push(mejor);
        filas.push({ weekday: mejor, subject_id: o.c.id, position: carga[mejor] });
        carga[mejor]++;
      }
    });
    return filas;
  }

  var COLS_PROG = 'id, weekday, subject_id, lessons_target, position';

  async function cargarProgramaciones() {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;

    var res = await Promise.all([
      sb.from('students')
        .select('id, first_name, last_name, created_at, started_at, target_months, grades(name, levels(name))')
        .order('created_at', { ascending: true }),
      sb.rpc('family_progress'),
      sb.from('study_schedule').select('student_id, ' + COLS_PROG).order('position')
    ]);
    res.forEach(function (r) { if (r.error) throw r.error; });

    var cursosDe = {}, filasDe = {};
    (res[1].data || []).forEach(function (r) {
      (cursosDe[r.student_id] = cursosDe[r.student_id] || []).push({
        id: r.subject_id, nombre: r.subject_name, color: colorSeguro(r.color), orden: r.subject_position,
        total: r.total_topics, completas: r.done_topics
      });
    });
    (res[2].data || []).forEach(function (f) {
      (filasDe[f.student_id] = filasDe[f.student_id] || []).push(f);
    });

    var hijos = (res[0].data || []).map(function (h) {
      return {
        id: h.id, nombre: h.first_name + ' ' + h.last_name, primerNombre: h.first_name,
        anio: h.grades ? etiquetaAnio(h.grades) : '',
        iniciado: h.started_at, meses: h.target_months,
        finAnio: fechaObjetivo(h.started_at, h.target_months),
        cursos: (cursosDe[h.id] || []).sort(function (a, b) { return a.orden - b.orden; }),
        filas: filasDe[h.id] || []
      };
    });
    return { hijos: hijos, uid: uid };
  }

  // Programación de un hijo: dibuja y edita sobre su propio contenedor
  function crearProgramacion(cont, hijo, uid) {
    var prog = { cursos: hijo.cursos, filas: hijo.filas, ocupado: false };

    function cursoPorId(id) {
      return prog.cursos.filter(function (c) { return c.id === id; })[0];
    }

    function trayectoria() {
      var finAnio = hijo.finAnio;
      var filasCursos = [], finGlobal = null, sinProgramar = [], restantesTotal = 0, hayLecciones = false;

      prog.cursos.forEach(function (c) {
        var porDia = [0, 0, 0, 0, 0, 0], semanal = 0;
        prog.filas.forEach(function (f) {
          if (f.subject_id === c.id) { porDia[f.weekday] += f.lessons_target; semanal += f.lessons_target; }
        });
        var restantes = Math.max(0, c.total - c.completas);
        var r = { curso: c, restantes: restantes, semanal: semanal, estado: '', clase: 'neutro', texto: '' };

        if (c.total === 0) {
          r.texto = 'Todavía no tiene temas cargados';
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
              r.texto = 'Termina el ' + fechaLarga(fin) + ' · ' + textoTemas(semanal) + ' por semana';
              if (finAnio && fin > finAnio) {
                r.estado = 'Se retrasa ' + semanasDeRetraso(fin, finAnio) + ' sem.'; r.clase = 'atraso';
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

    function htmlHero(t) {
      var finAnio = hijo.finAnio;
      var hoy = new Date();
      hoy.setHours(12, 0, 0, 0);
      var nota = t.sinProgramar.length
        ? '<p class="tray-nota">Falta programar: ' + esc(t.sinProgramar.join(', ')) + '.</p>' : '';

      if (!t.hayLecciones) {
        return '<div class="tray-hero"><p class="tray-vacio">Todavía no hay temas cargados en sus materias. ' +
          'Cuando las haya, acá vas a ver cuándo terminaría el año con este programa.</p></div>';
      }
      if (t.restantesTotal === 0) {
        return '<div class="tray-hero ok"><b class="tray-fecha">¡Completó todos los temas del año!</b></div>';
      }
      if (!t.finGlobal) {
        return '<div class="tray-hero atraso"><b class="tray-fecha">Programá sus materias para calcular cuándo termina</b>' + nota + '</div>';
      }

      var atrasado = finAnio && t.finGlobal > finAnio;
      var pill = '';
      if (finAnio) {
        pill = atrasado
          ? '<span class="tray-pill atraso">+' + semanasDeRetraso(t.finGlobal, finAnio) + ' semanas de retraso</span>'
          : '<span class="tray-pill ok">Llega a tiempo</span>';
      }

      var linea = '';
      if (finAnio && finAnio > hoy) {
        var pos = Math.min(100, Math.max(0, ((t.finGlobal - hoy) / (finAnio - hoy)) * 100));
        linea = '<div class="tray-linea"><div class="tray-relleno" style="width:' + pos.toFixed(1) + '%"></div>' +
          '<span class="tray-pin" style="left:' + pos.toFixed(1) + '%"></span></div>' +
          '<div class="tray-extremos"><span>Hoy</span><span>Fecha objetivo · ' + esc(fechaCorta(finAnio)) + '</span></div>';
      }

      return '<div class="tray-hero ' + (atrasado ? 'atraso' : 'ok') + '">' +
        '<div class="tray-hero-top"><div><span class="tray-etiqueta">Terminaría el año el</span>' +
        '<b class="tray-fecha">' + esc(fechaLarga(t.finGlobal)) + '</b></div>' + pill + '</div>' +
        linea +
        '<p class="tray-faltan">Le faltan <b>' + textoTemas(t.restantesTotal) + '</b> en total.' +
        (atrasado ? ' Para llegar a tiempo, sumá temas por día.' : '') + '</p>' + nota + '</div>';
    }

    // Fecha objetivo de finalización: la elige solo la familia
    function htmlMeta(t) {
      var OPC = [[12, 'Un año'], [18, 'Año y medio'], [24, 'Dos años']];
      var botones = OPC.map(function (o) {
        var sel = hijo.meses === o[0];
        return '<button type="button" class="meta-btn' + (sel ? ' sel' : '') + '" data-a="plazo" data-m="' + o[0] + '" aria-pressed="' + sel + '">' + o[1] + '</button>';
      }).join('');

      var estado;
      if (!hijo.iniciado) {
        estado = 'El plazo empieza a correr cuando ' + esc(hijo.primerNombre) + ' ingrese por primera vez.';
      } else if (!hijo.meses || !hijo.finAnio) {
        estado = 'Elegí un plazo para ver si llega a tiempo.';
      } else {
        estado = 'Fecha objetivo: <b>' + esc(fechaLarga(hijo.finAnio)) + '</b> · contando desde su primer ingreso (' + esc(fechaCorta(new Date(hijo.iniciado))) + ').';
        var hoy = new Date();
        var semanas = ((hijo.finAnio - hoy) / 86400000 / 7) / FACTOR_CALENDARIO;
        if (t.restantesTotal > 0) {
          if (semanas <= 0) {
            estado += ' <b>El plazo ya venció.</b>';
          } else {
            var necesario = t.restantesTotal / semanas;
            var programado = 0;
            t.filas.forEach(function (r) { if (r.restantes > 0) programado += r.semanal; });
            estado += ' Para llegar a tiempo necesita unos <b>' + necesario.toLocaleString('es-AR', { maximumFractionDigits: 1 }) +
              ' temas por semana</b> en total; hoy tiene programados <b>' + programado + '</b>.';
          }
        }
      }

      return '<section class="meta">' +
        '<div><span class="meta-rot">Fecha objetivo de finalización</span>' +
        '<p class="meta-preg">¿En cuánto tiempo querés que ' + esc(hijo.primerNombre) + ' termine el año completo?</p></div>' +
        '<div class="meta-opc" role="group" aria-label="Plazo">' + botones + '</div>' +
        '<p class="meta-estado">' + estado + '</p></section>';
    }

    function pintar() {
      var hoySemana = new Date().getDay();

      var dias = DIAS.map(function (nombre, i) {
        var wd = i + 1;
        var delDia = prog.filas.filter(function (f) { return f.weekday === wd; })
          .sort(function (a, b) { return a.position - b.position; });
        var usadas = {}, suma = 0;
        delDia.forEach(function (f) { usadas[f.subject_id] = true; suma += f.lessons_target; });

        var items = delDia.map(function (f) {
          var c = cursoPorId(f.subject_id);
          if (!c) return '';
          return '<div class="prog-item" style="--c:' + c.color + '">' +
            '<button type="button" class="prog-x" data-a="quitar" data-id="' + f.id + '" aria-label="Quitar ' + esc(c.nombre) + '">×</button>' +
            '<span class="prog-ico">' + iconoMateria(c.nombre) + '</span>' +
            '<b class="prog-nombre">' + esc(c.nombre) + '</b>' +
            '<div class="prog-cant">' +
            '<button type="button" data-a="menos" data-id="' + f.id + '" aria-label="Un tema menos">−</button>' +
            '<span><strong>' + f.lessons_target + '</strong> ' + (f.lessons_target === 1 ? 'tema' : 'temas') + '</span>' +
            '<button type="button" data-a="mas" data-id="' + f.id + '" aria-label="Un tema más">+</button>' +
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
          '<small>' + (suma ? textoTemas(suma) : 'Sin temas') + '</small></header>' +
          '<div class="dia-cuerpo">' + items + agregar + '</div></section>';
      }).join('');

      var t = trayectoria();
      var filasT = t.filas.map(function (r) {
        var c = r.curso;
        var pct = c.total ? Math.round((c.completas / c.total) * 100) : 0;
        var info = r.texto || (r.restantes === 0 ? 'Sin temas pendientes' : '');
        return '<div class="tray-fila" style="--c:' + c.color + '">' +
          '<span class="tray-ico">' + iconoMateria(c.nombre) + '</span>' +
          '<div class="tray-info"><b>' + esc(c.nombre) + '</b>' +
          (info ? '<span>' + esc(info) + '</span>' : '') +
          (c.total ? '<div class="tray-mini"><span style="width:' + pct + '%"></span></div>' : '') + '</div>' +
          (r.estado ? '<span class="tray-estado ' + r.clase + '">' + esc(r.estado) + '</span>' : '') +
          '</div>';
      }).join('');

      cont.innerHTML =
        htmlMeta(t) +
        '<div class="semana">' + dias + '</div>' +
        '<h3 class="vista-subtitulo">Trayectoria</h3>' +
        htmlHero(t) +
        '<div class="tray-lista">' + filasT + '</div>';
    }

    function filaPorId(id) {
      return prog.filas.filter(function (f) { return String(f.id) === String(id); })[0];
    }

    async function guardar(fn) {
      if (prog.ocupado) return;
      prog.ocupado = true;
      try { await fn(); }
      catch (e) { alert('No pudimos guardar el cambio. Probá de nuevo.'); }
      prog.ocupado = false;
      pintar();
    }

    async function cambiarCantidad(id, delta) {
      var f = filaPorId(id);
      if (!f) return;
      var n = Math.max(1, Math.min(20, f.lessons_target + delta));
      if (n === f.lessons_target) return;
      var r = await sb.from('study_schedule').update({ lessons_target: n, updated_by: uid })
        .eq('id', f.id).select('id');
      if (r.error || !r.data.length) throw (r.error || new Error('sin permiso'));
      f.lessons_target = n;
    }

    async function quitarFila(id) {
      var r = await sb.from('study_schedule').delete().eq('id', id).select('id');
      if (r.error || !r.data.length) throw (r.error || new Error('sin permiso'));
      prog.filas = prog.filas.filter(function (f) { return String(f.id) !== String(id); });
    }

    async function elegirPlazo(meses) {
      var r = await sb.rpc('set_student_target', { p_student: hijo.id, p_months: meses });
      if (r.error) throw r.error;
      hijo.meses = meses;
      hijo.finAnio = fechaObjetivo(hijo.iniciado, meses);
    }

    async function agregarFila(dia, materiaId) {
      var pos = prog.filas.filter(function (f) { return f.weekday === dia; }).length;
      var r = await sb.from('study_schedule').insert({
        student_id: hijo.id, weekday: dia, subject_id: materiaId,
        lessons_target: 1, position: pos, updated_by: uid
      }).select(COLS_PROG);
      if (r.error) throw r.error;
      prog.filas = prog.filas.concat(r.data);
    }

    // Primera vez: el programa viene armado, después se edita
    async function sugerirPrograma() {
      var filas = armarSemana(prog.cursos).map(function (f) {
        return { student_id: hijo.id, weekday: f.weekday, subject_id: f.subject_id,
                 lessons_target: 1, position: f.position, updated_by: uid };
      });
      var r = await sb.from('study_schedule').insert(filas).select(COLS_PROG);
      if (r.error) throw r.error;
      prog.filas = prog.filas.concat(r.data);
    }

    cont.addEventListener('click', function (ev) {
      var b = ev.target.closest('button[data-a]');
      if (!b || b.getAttribute('data-a') !== 'menu') {
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
      else if (a === 'plazo') {
        var meses = Number(b.getAttribute('data-m'));
        guardar(function () { return elegirPlazo(meses); });
      }
      else if (a === 'agregar') {
        var dia = Number(b.getAttribute('data-dia'));
        var mat = b.getAttribute('data-mat');
        guardar(function () { return agregarFila(dia, mat); });
      }
    });

    return {
      iniciar: async function () {
        if (!prog.filas.length && prog.cursos.length) {
          try { await sugerirPrograma(); } catch (e) { /* queda vacío y se agrega a mano */ }
        }
        pintar();
      }
    };
  }

  async function vistaProgramacion() {
    vista.innerHTML = '<h1 class="vista-titulo">Programación</h1><div id="programacion"></div>';
    var cont = document.getElementById('programacion');
    cont.innerHTML = '<div class="vacio">Cargando…</div>';
    try {
      var d = await cargarProgramaciones();
      if (!d.hijos.length) {
        cont.innerHTML = '<div class="vacio">Todavía no diste de alta a ningún hijo. Cuando lo hagas, acá vas a armar su programación.</div>';
        return;
      }
      cont.innerHTML = d.hijos.map(function (h, i) {
        var ini = h.nombre.split(' ').map(function (p) { return p.charAt(0); }).slice(0, 2).join('').toUpperCase();
        return '<section class="pg-hijo">' +
          '<div class="pg-cab"><div class="hijo-ini">' + esc(ini) + '</div>' +
          '<div><h2>' + esc(h.nombre) + '</h2><span>' + esc(h.anio) + '</span></div></div>' +
          '<div id="prog-' + i + '">' +
            (h.cursos.length ? '' : '<div class="vacio">Todavía no tiene materias habilitadas.</div>') +
          '</div></section>';
      }).join('');

      for (var i = 0; i < d.hijos.length; i++) {
        var h = d.hijos[i];
        if (!h.cursos.length) continue;
        await crearProgramacion(document.getElementById('prog-' + i), h, d.uid).iniciar();
      }
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar la programación. Probá recargar la página.</div>';
    }
  }

  // ---------- Secciones que vienen después ----------
  function proximamente(titulo) {
    return function () {
      vista.innerHTML = '<h1 class="vista-titulo">' + titulo + '</h1>' +
        '<div class="proximamente">Estamos armando esta sección. Muy pronto vas a encontrarla acá.</div>';
    };
  }

  var VISTAS = {
    altas: vistaAltas,
    progreso: vistaProgreso,
    programacion: vistaProgramacion,
    facturacion: proximamente('Facturación')
  };

  function ruta() {
    var nombre = (location.hash || '#altas').slice(1);
    if (!VISTAS[nombre]) nombre = 'altas';
    enlaces.forEach(function (a) {
      a.classList.toggle('activo', a.getAttribute('href') === '#' + nombre);
    });
    VISTAS[nombre]();
  }

  window.addEventListener('hashchange', ruta);
  ruta();
})();
