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
          total: r.total_lessons, hechas: r.done_lessons,
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
          '<div class="pm-pie"><span>' + m.hechas + ' de ' + m.total + ' lecciones</span><b>' + pct + '%</b></div>' +
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
    programacion: proximamente('Programación'),
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
