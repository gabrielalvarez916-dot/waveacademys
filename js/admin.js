// Panel de administración: navegación y sección Familias y alumnos.
(function () {
  var sb = Wave.sb;
  var vista = document.getElementById('vista');
  var enlaces = document.querySelectorAll('.nav-admin a');

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // ---------- Utilidades ----------
  function haceCuanto(iso) {
    if (!iso) return 'Nunca ingresó';
    var min = Math.floor((Date.now() - new Date(iso).getTime()) / 60000);
    if (min < 2) return 'Recién';
    if (min < 60) return 'Hace ' + min + ' min';
    var h = Math.floor(min / 60);
    if (h < 24) return 'Hace ' + h + (h === 1 ? ' hora' : ' horas');
    var d = Math.floor(h / 24);
    if (d < 31) return 'Hace ' + d + (d === 1 ? ' día' : ' días');
    return new Date(iso).toLocaleDateString('es-AR');
  }

  function toast(texto, error) {
    var t = document.createElement('div');
    t.className = 'wv-toast' + (error ? ' error' : '');
    t.textContent = texto;
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, 3500);
  }

  // La función devuelve el motivo del error en el cuerpo de la respuesta
  async function accion(body) {
    var r = await sb.functions.invoke('admin-actions', { body: body });
    if (r.error) {
      var msg = 'No se pudo completar la acción. Intentá de nuevo.';
      try {
        if (r.error.context && typeof r.error.context.json === 'function') {
          var c = await r.error.context.json();
          if (c && c.error) msg = c.error;
        }
      } catch (e) { /* mensaje genérico */ }
      throw new Error(msg);
    }
    return r.data;
  }

  // ---------- Modal ----------
  var modalEl = null;
  function cerrarModal() {
    if (modalEl) { modalEl.remove(); modalEl = null; }
    document.removeEventListener('keydown', teclaModal);
  }
  function teclaModal(ev) { if (ev.key === 'Escape') cerrarModal(); }
  function abrirModal(html) {
    cerrarModal();
    modalEl = document.createElement('div');
    modalEl.className = 'wv-modal';
    modalEl.innerHTML = '<div class="wv-modal-caja" role="dialog" aria-modal="true">' + html + '</div>';
    modalEl.addEventListener('mousedown', function (ev) { if (ev.target === modalEl) cerrarModal(); });
    document.body.appendChild(modalEl);
    document.addEventListener('keydown', teclaModal);
    return modalEl.querySelector('.wv-modal-caja');
  }

  function confirmar(titulo, texto, textoBoton, peligro, alAceptar) {
    var caja = abrirModal(
      '<h2>' + esc(titulo) + '</h2><p>' + esc(texto) + '</p>' +
      '<p class="mensaje" id="m-error" hidden></p>' +
      '<div class="wv-modal-pie"><button type="button" class="wv-btn suave" data-no>Cancelar</button>' +
      '<button type="button" class="wv-btn' + (peligro ? ' peligro' : '') + '" data-si>' + esc(textoBoton) + '</button></div>');
    caja.querySelector('[data-no]').onclick = cerrarModal;
    var si = caja.querySelector('[data-si]');
    si.onclick = async function () {
      si.disabled = true;
      try { await alAceptar(); }
      catch (e) {
        var er = caja.querySelector('#m-error');
        er.textContent = e.message; er.hidden = false; si.disabled = false;
      }
    };
  }

  function mostrarCredenciales(titulo, usuario, clave) {
    var caja = abrirModal(
      '<h2>' + esc(titulo) + '</h2>' +
      '<p>Pasale estos datos. Al ingresar por primera vez le va a pedir que cambie la contraseña.</p>' +
      '<div class="wv-cred-fila"><div><small>Usuario</small><b>' + esc(usuario) + '</b></div>' +
        '<button type="button" class="wv-btn mini" data-copiar="' + esc(usuario) + '">Copiar</button></div>' +
      '<div class="wv-cred-fila"><div><small>Contraseña inicial</small><b>' + esc(clave) + '</b></div>' +
        '<button type="button" class="wv-btn mini" data-copiar="' + esc(clave) + '">Copiar</button></div>' +
      '<div class="wv-modal-pie"><button type="button" class="wv-btn" data-no>Listo</button></div>');
    caja.onclick = function (ev) {
      if (ev.target.closest('[data-no]')) { cerrarModal(); return; }
      var b = ev.target.closest('[data-copiar]');
      if (b && navigator.clipboard) {
        navigator.clipboard.writeText(b.getAttribute('data-copiar')).then(function () {
          b.textContent = '¡Copiado!'; setTimeout(function () { b.textContent = 'Copiar'; }, 1500);
        }, function () {});
      }
    };
  }

  // ---------- Estado de cuota ----------
  var ESTADO = {
    active:    { txt: 'Al día',     cls: 'ok',    peso: 3 },
    past_due:  { txt: 'Con deuda',  cls: 'deuda', peso: 5 },
    pending:   { txt: 'Pendiente',  cls: 'pend',  peso: 4 },
    suspended: { txt: 'Suspendida', cls: 'off',   peso: 2 },
    cancelled: { txt: 'Cancelada',  cls: 'off',   peso: 1 }
  };

  function pill(status) {
    var e = ESTADO[status];
    if (!e) return '<span class="wv-pill off">Sin suscripción</span>';
    return '<span class="wv-pill ' + e.cls + '">' + e.txt + '</span>';
  }

  // El estado de la familia es el más urgente entre sus suscripciones
  function estadoFamilia(subs) {
    var mejor = null;
    subs.forEach(function (s) {
      if (!mejor || (ESTADO[s.status] ? ESTADO[s.status].peso : 0) > (ESTADO[mejor] ? ESTADO[mejor].peso : 0)) mejor = s.status;
    });
    return mejor;
  }

  // ---------- Datos ----------
  async function cargarDatos() {
    var res = await Promise.all([
      sb.from('families')
        .select('id, phone, created_at, profiles!families_profile_id_fkey(id, full_name, email, is_suspended, last_seen_at)')
        .order('created_at', { ascending: false }),
      sb.from('students')
        .select('id, family_id, first_name, last_name, curriculum, pais, modalidad, grades(name, levels(name)), profiles!students_profile_id_fkey(id, email, is_suspended, last_seen_at)')
        .order('created_at', { ascending: true }),
      sb.from('subscriptions')
        .select('id, family_id, student_id, status, amount, currency, created_at, modalidad, nivel, proveedor')
        .order('created_at', { ascending: true }),
      sb.rpc('tutores_admin'),
      sb.from('tutor_students').select('tutor_id, student_id')
    ]);
    res.forEach(function (r) { if (r.error) throw r.error; });
    TUTORES = res[3].data || [];
    var tutorDe = {}; (res[4].data || []).forEach(function (t) { tutorDe[t.student_id] = t.tutor_id; });

    var alumnos = res[1].data || [], subs = res[2].data || [];
    return (res[0].data || []).map(function (f) {
      var misSubs = subs.filter(function (s) { return s.family_id === f.id; });
      return {
        id: f.id, phone: f.phone, perfil: f.profiles || {},
        subs: misSubs,
        libres: misSubs.filter(function (s) { return !s.student_id; }),
        alumnos: alumnos.filter(function (a) { return a.family_id === f.id; }).map(function (a) {
          return {
            id: a.id, nombre: a.first_name + ' ' + a.last_name, curriculum: a.curriculum || 'argentina', pais: a.pais || 'Argentina',
            anio: a.grades ? ((a.grades.levels && a.grades.levels.name !== a.grades.name ? a.grades.levels.name + ' · ' : '') + a.grades.name) : '',
            perfil: a.profiles || {},
            sub: misSubs.filter(function (s) { return s.student_id === a.id; })[0] || null,
            modManual: a.modalidad || null, tutor: tutorDe[a.id] || null
          };
        }),
        estado: estadoFamilia(misSubs)
      };
    });
  }

  // ---------- Familias y alumnos ----------
  var estado = { datos: [], filtro: 'todas', busqueda: '' };

  function coincide(f) {
    var q = estado.busqueda.trim().toLowerCase();
    if (q) {
      var texto = [f.perfil.full_name, f.perfil.email, f.phone].concat(f.alumnos.map(function (a) {
        return a.nombre + ' ' + (a.perfil.email || '');
      })).join(' ').toLowerCase();
      if (texto.indexOf(q) === -1) return false;
    }
    switch (estado.filtro) {
      case 'aldia': return f.estado === 'active';
      case 'deuda': return f.estado === 'past_due';
      case 'sin': return !f.estado || f.estado === 'cancelled' || f.estado === 'suspended' || f.estado === 'pending';
      case 'susp': return !!f.perfil.is_suspended;
      default: return true;
    }
  }

  // ---------- Modalidad (Libre / Guiada / Completa) y tutor de cada alumno ----------
  var TUTORES = [];
  var MODS = { libre: 'Libre', guiada: 'Guiada', completa: 'Completa', personalizada: 'Personalizada' };
  function modalidadDe(a) { return a.modManual || (a.sub && (a.sub.status === 'active' || a.sub.status === 'past_due') && a.sub.modalidad) || 'libre'; }
  function selModalidad(a) {
    var auto = (a.sub && a.sub.modalidad) ? MODS[a.sub.modalidad] : 'Libre';
    return '<select class="wv-cur" data-mod="' + a.id + '" aria-label="Modalidad de ' + esc(a.nombre) + '">' +
      '<option value=""' + (!a.modManual ? ' selected' : '') + '>Según su cuota (' + esc(auto) + ')</option>' +
      ['libre', 'guiada', 'completa'].map(function (m) { return '<option value="' + m + '"' + (a.modManual === m ? ' selected' : '') + '>' + MODS[m] + ' (a mano)</option>'; }).join('') +
      '</select>';
  }
  function selTutor(a) {
    var con = modalidadDe(a) !== 'libre';
    if (!con && !a.tutor) return '<span class="wv-dato">— (Libre)</span>';
    return '<select class="wv-cur" data-tut="' + a.id + '" aria-label="Tutor de ' + esc(a.nombre) + '">' +
      '<option value="">Sin tutor</option>' +
      TUTORES.map(function (t) { return '<option value="' + t.id + '"' + (a.tutor === t.id ? ' selected' : '') + '>' + esc(t.nombre || t.email) + '</option>'; }).join('') +
      '</select>';
  }
  async function cambiarModalidad(sel) {
    var r = await sb.rpc('set_student_modalidad', { p_student: sel.getAttribute('data-mod'), p_modalidad: sel.value || null });
    if (r.error) { toast(r.error.message, true); } else toast('Modalidad actualizada');
    await recargar();
  }
  async function cambiarTutor(sel) {
    var r = await sb.rpc('asignar_tutor', { p_student: sel.getAttribute('data-tut'), p_tutor: sel.value || null });
    if (r.error) { toast(r.error.message, true); } else toast(sel.value ? 'Tutor asignado' : 'Tutor quitado');
    await recargar();
  }

  function htmlAlumno(a, f) {
    var susp = a.perfil.is_suspended;
    return '<div class="wv-alu">' +
      '<div><div class="wv-nombre">' + esc(a.nombre) + (susp ? '<span class="wv-pill susp">Suspendido</span>' : '') + '</div>' +
        '<div class="wv-dato">' + esc(a.anio) + (a.perfil.email ? ' · ' + esc(a.perfil.email) : '') + '</div></div>' +
      '<div><span class="wv-rot">Cuota</span>' + (a.sub ? pill(a.sub.status) : '<span class="wv-pill off">Sin cupo vinculado</span>') + '</div>' +
      '<div><span class="wv-rot">Último acceso</span><span class="wv-dato">' + esc(haceCuanto(a.perfil.last_seen_at)) + '</span></div>' +
      '<div><span class="wv-rot">País</span>' +
        '<select class="wv-cur" data-cur="' + a.id + '" data-nom="' + esc(a.nombre) + '" data-pais="' + esc(a.pais) + '" aria-label="País de ' + esc(a.nombre) + '">' +
          PAISES.concat(PAISES.indexOf(a.pais) < 0 ? [a.pais] : []).map(function (p) { return '<option' + (p === a.pais ? ' selected' : '') + '>' + esc(p) + '</option>'; }).join('') +
        '</select></div>' +
      '<div><span class="wv-rot">Modalidad</span>' + selModalidad(a) + '</div>' +
      '<div><span class="wv-rot">Tutor</span>' + selTutor(a) + '</div>' +
      '<div class="wv-acc">' +
        '<button type="button" class="wv-btn mini suave" data-tray="' + a.id + '" data-nom="' + esc(a.nombre) + '">Trayectoria</button>' +
        (!a.sub ? '<button type="button" class="wv-btn mini suave" data-vincular="' + a.id + '" data-fam="' + f.id + '">Vincular cupo</button>' : '') +
        (a.perfil.id ? '<button type="button" class="wv-btn mini suave" data-reset="' + a.perfil.id + '" data-nom="' + esc(a.nombre) + '">Resetear clave</button>' +
          '<button type="button" class="wv-btn mini ' + (susp ? '' : 'peligro') + '" data-susp="' + a.perfil.id + '" data-a="' + (susp ? 0 : 1) + '" data-nom="' + esc(a.nombre) + '">' + (susp ? 'Reactivar' : 'Suspender') + '</button>' : '') +
      '</div></div>';
  }

  // ---------- Trayectoria del alumno (informe por materia, solo admin) ----------
  var EST = { bien: ['Lo maneja bien', 'ok'], en_proceso: ['En proceso', 'med'], flojo: ['Flojo', 'bajo'], sin_datos: ['Sin datos', 'nada'] };
  function nota(n) { return n == null ? '—' : String(Math.round(Number(n))); }
  function htmlTrayectoria(materias) {
    if (!materias.length) return '<div class="wv-sin">Este alumno todavía no tiene materias asignadas.</div>';
    return materias.map(function (m) {
      var lecs = [];
      m.topics.forEach(function (t) { t.lessons.forEach(function (l) { l.tema = t.title; lecs.push(l); }); });
      var con = lecs.filter(function (l) { return l.status !== 'sin_datos'; });
      var cuenta = { bien: 0, en_proceso: 0, flojo: 0 };
      con.forEach(function (l) { cuenta[l.status]++; });
      var flojas = con.filter(function (l) { return l.status !== 'bien' || l.final_attempts > 1; })
        .sort(function (a, b) { return (a.mastery - b.mastery) || (b.final_attempts - a.final_attempts); }).slice(0, 5);
      var fuertes = con.filter(function (l) { return l.status === 'bien'; }).sort(function (a, b) { return b.mastery - a.mastery; }).slice(0, 5);
      var rp = m.repasos || {};
      var cab = '<summary><span class="wv-tr-pt" style="background:' + esc(m.color || '#087E83') + '"></span><b>' + esc(m.name) + '</b>' +
        (con.length ? '<span class="wv-tr-chips"><span class="wv-tr-chip ok">' + cuenta.bien + ' bien</span><span class="wv-tr-chip med">' + cuenta.en_proceso + ' en proceso</span><span class="wv-tr-chip bajo">' + cuenta.flojo + (cuenta.flojo === 1 ? ' floja' : ' flojas') + '</span></span>'
          : '<span class="wv-tr-chips"><span class="wv-tr-chip nada">Sin actividad todavía</span></span>') + '</summary>';
      if (!con.length) return '<details class="wv-tr-mat">' + cab + '<div class="wv-sin">Cuando haga actividades o repasos de esta materia, acá vas a ver qué maneja bien y qué le cuesta.</div></details>';
      var lista = function (titulo, arr, vacio) {
        return '<div class="wv-tr-col"><h4>' + titulo + '</h4>' + (arr.length ? arr.map(function (l) {
          return '<div class="wv-tr-it"><span class="wv-tr-n ' + EST[l.status][1] + '">' + nota(l.mastery) + '</span><div><b>' + esc(l.title) + '</b><small>' + esc(l.tema) +
            (l.final_attempts > 1 ? ' · ' + l.final_attempts + ' intentos en la actividad' : '') + '</small></div></div>';
        }).join('') : '<small class="wv-tr-vac">' + vacio + '</small>') + '</div>';
      };
      var h = '<div class="wv-tr-dos">' + lista('Para reforzar', flojas, 'Nada flojo por ahora.') + lista('Lo que maneja bien', fuertes, 'Todavía no hay lecciones con dominio alto.') + '</div>' +
        '<p class="wv-tr-rep">Repasos hechos: <b>' + (rp.hechos || 0) + '</b>' + (rp.promedio != null ? ' · promedio <b>' + nota(rp.promedio) + '</b> de 100' : '') + '</p>';
      m.topics.forEach(function (t) {
        var filas = t.lessons.filter(function (l) { return l.status !== 'sin_datos' || l.done; });
        if (!filas.length && !(t.exam && t.exam.intentos)) return;
        h += '<h4 class="wv-tr-tema">' + esc(t.title) + (t.exam && t.exam.intentos ? '<small>Examen: mejor nota ' + nota(t.exam.mejor) + ' · ' + t.exam.intentos + (t.exam.intentos === 1 ? ' intento' : ' intentos') + (t.exam.aprobado ? ' · aprobado' : ' · sin aprobar') + '</small>' : '') + '</h4>';
        if (filas.length) h += '<div class="wv-tr-tabla"><table><thead><tr><th>Lección</th><th>Dominio</th><th>Actividad</th><th>Interactiva</th><th>Repasos</th><th>Estado</th></tr></thead><tbody>' +
          filas.map(function (l) {
            return '<tr><td>' + esc(l.title) + '</td><td><span class="wv-tr-barra"><i class="' + EST[l.status][1] + '" style="width:' + (l.mastery == null ? 0 : Math.round(l.mastery)) + '%"></i></span> ' + nota(l.mastery) + '</td>' +
              '<td>' + nota(l.final_score) + (l.final_attempts > 1 ? ' <small>(' + l.final_attempts + ' intentos)</small>' : '') + '</td><td>' + nota(l.interactive_score) + '</td>' +
              '<td>' + (l.review_total ? l.review_ok + ' de ' + l.review_total : '—') + '</td><td><span class="wv-tr-chip ' + EST[l.status][1] + '">' + EST[l.status][0] + '</span></td></tr>';
          }).join('') + '</tbody></table></div>';
      });
      return '<details class="wv-tr-mat" open>' + cab + h + '</details>';
    }).join('');
  }
  async function trayectoria(alumnoId, nombreAlu) {
    var caja = abrirModal('<h2>Trayectoria de ' + esc(nombreAlu) + '</h2><p>Qué conocimientos maneja bien y cuáles hay que reforzar, por materia. Solo lo ve el admin.</p><div id="tr-cuerpo"><div class="wv-sin">Cargando…</div></div>' +
      '<div class="wv-modal-pie"><button type="button" class="wv-btn" data-cerrar-modal="1">Cerrar</button></div>');
    caja.classList.add('ancha');
    caja.querySelector('[data-cerrar-modal]').onclick = cerrarModal;
    var r = await sb.rpc('student_trajectory', { p_student: alumnoId });
    var cuerpo = caja.querySelector('#tr-cuerpo');
    if (!cuerpo) return;
    if (r.error) { cuerpo.innerHTML = '<div class="wv-sin">No se pudo cargar la trayectoria.</div>'; return; }
    var mats = (r.data || []).slice().sort(function (a, b) {
      var da = a.topics.some(function (t) { return t.lessons.some(function (l) { return l.status !== 'sin_datos'; }); });
      var db = b.topics.some(function (t) { return t.lessons.some(function (l) { return l.status !== 'sin_datos'; }); });
      return (db ? 1 : 0) - (da ? 1 : 0);
    });
    cuerpo.innerHTML = '<p class="wv-tr-ley">El dominio va de 0 a 100 y combina la nota de la actividad, la actividad interactiva y los aciertos en los repasos. Baja un poco cuando tuvo que reintentar la actividad.</p>' + htmlTrayectoria(mats);
  }

  function htmlFamilia(f) {
    var p = f.perfil, susp = p.is_suspended;
    var nombre = p.full_name || p.email || 'Sin nombre';
    return '<section class="wv-fam' + (susp ? ' susp' : '') + '">' +
      '<div class="wv-fam-cab">' +
        '<div><div class="wv-nombre">' + esc(nombre) + (susp ? '<span class="wv-pill susp">Suspendida</span>' : '') + '</div>' +
          '<div class="wv-dato">' + esc(p.email || '') + (f.phone ? ' · ' + esc(f.phone) : '') + '</div></div>' +
        '<div><span class="wv-rot">Cuota</span>' + pill(f.estado) +
          '<div class="wv-dato" style="margin-top:4px">' + f.subs.length + (f.subs.length === 1 ? ' cupo' : ' cupos') +
          (f.libres.length ? ' · ' + f.libres.length + (f.libres.length === 1 ? ' libre' : ' libres') : '') + '</div></div>' +
        '<div><span class="wv-rot">Último acceso</span><span class="wv-dato">' + esc(haceCuanto(p.last_seen_at)) + '</span></div>' +
        '<div class="wv-acc">' +
          '<button type="button" class="wv-btn mini suave" data-cupo="' + f.id + '">Agregar cupo</button>' +
          '<button type="button" class="wv-btn mini suave" data-reset="' + p.id + '" data-nom="' + esc(nombre) + '">Resetear clave</button>' +
          '<button type="button" class="wv-btn mini ' + (susp ? '' : 'peligro') + '" data-susp="' + p.id + '" data-a="' + (susp ? 0 : 1) + '" data-nom="' + esc(nombre) + '" data-fam-susp="1">' + (susp ? 'Reactivar' : 'Suspender') + '</button>' +
        '</div>' +
      '</div>' +
      '<div class="wv-alumnos">' +
        (f.alumnos.length ? f.alumnos.map(function (a) { return htmlAlumno(a, f); }).join('')
          : '<div class="wv-sin">Todavía no dio de alta a ningún alumno.</div>') +
      '</div></section>';
  }

  function pintarLista() {
    var cont = document.getElementById('wv-lista');
    var vis = estado.datos.filter(coincide);
    cont.innerHTML = vis.length ? vis.map(htmlFamilia).join('')
      : '<div class="wv-vacio">' + (estado.datos.length ? 'No hay resultados para esa búsqueda.' : 'Todavía no hay familias. Creá la primera con “Nueva familia”.') + '</div>';
  }

  function pintarResumen() {
    var d = estado.datos, alumnos = 0, deuda = 0, libres = 0;
    d.forEach(function (f) {
      alumnos += f.alumnos.length; libres += f.libres.length;
      if (f.estado === 'past_due') deuda++;
    });
    document.getElementById('wv-resumen').innerHTML =
      [['Familias', d.length], ['Alumnos', alumnos], ['Con deuda', deuda], ['Cupos libres', libres]].map(function (x) {
        return '<div class="wv-stat"><small>' + x[0] + '</small><b>' + x[1] + '</b></div>';
      }).join('');
  }

  async function recargar() {
    estado.datos = await cargarDatos();
    pintarResumen();
    pintarLista();
  }

  // ----- Acciones -----
  function nuevaFamilia() {
    var caja = abrirModal(
      '<h2>Nueva familia</h2><p>Se crea el usuario con el correo y una contraseña inicial.</p>' +
      '<div class="campo"><label for="nf-mail">Correo (será el usuario)</label><input id="nf-mail" type="email" autocomplete="off" placeholder="correo@ejemplo.com"></div>' +
      '<div class="campo"><label for="nf-nom">Nombre y apellido</label><input id="nf-nom" type="text" autocomplete="off" maxlength="80" placeholder="Nombre del padre, madre o tutor"></div>' +
      '<div class="campo"><label for="nf-tel">Teléfono (opcional)</label><input id="nf-tel" type="tel" autocomplete="off" maxlength="30" placeholder="+54 9 ..."></div>' +
      '<p class="mensaje" id="m-error" hidden></p>' +
      '<div class="wv-modal-pie"><button type="button" class="wv-btn suave" data-no>Cancelar</button><button type="button" class="wv-btn" data-si>Crear familia</button></div>');
    caja.querySelector('[data-no]').onclick = cerrarModal;
    var si = caja.querySelector('[data-si]'), er = caja.querySelector('#m-error');
    si.onclick = async function () {
      var mail = caja.querySelector('#nf-mail').value.trim();
      var nom = caja.querySelector('#nf-nom').value.trim();
      var tel = caja.querySelector('#nf-tel').value.trim();
      if (!mail || mail.indexOf('@') < 1) { er.textContent = 'Ingresá un correo válido.'; er.hidden = false; return; }
      if (!nom) { er.textContent = 'Ingresá el nombre.'; er.hidden = false; return; }
      si.disabled = true; er.hidden = true;
      try {
        var r = await accion({ action: 'create_family', email: mail, full_name: nom, phone: tel || null });
        await recargar();
        mostrarCredenciales('¡Familia creada!', r.username, r.initial_password);
      } catch (e) { er.textContent = e.message; er.hidden = false; si.disabled = false; }
    };
  }

  function agregarCupo(familiaId) {
    var caja = abrirModal(
      '<h2>Agregar cupo</h2><p>Crea una suscripción manual para la familia. Después se puede usar para dar de alta o vincular a un alumno.</p>' +
      '<div class="campo"><label for="cu-monto">Monto mensual (opcional)</label><input id="cu-monto" type="number" min="0" step="0.01" inputmode="decimal" placeholder="Ej: 25000"></div>' +
      '<div class="campo"><label for="cu-est">Estado</label><select id="cu-est"><option value="active">Al día</option><option value="pending">Pendiente</option></select></div>' +
      '<p class="mensaje" id="m-error" hidden></p>' +
      '<div class="wv-modal-pie"><button type="button" class="wv-btn suave" data-no>Cancelar</button><button type="button" class="wv-btn" data-si>Agregar cupo</button></div>');
    caja.querySelector('[data-no]').onclick = cerrarModal;
    var si = caja.querySelector('[data-si]'), er = caja.querySelector('#m-error');
    si.onclick = async function () {
      var monto = caja.querySelector('#cu-monto').value;
      si.disabled = true; er.hidden = true;
      try {
        await accion({ action: 'create_subscription', family_id: familiaId, amount: monto === '' ? null : Number(monto), status: caja.querySelector('#cu-est').value });
        await recargar(); cerrarModal(); toast('Cupo agregado');
      } catch (e) { er.textContent = e.message; er.hidden = false; si.disabled = false; }
    };
  }

  function vincular(alumnoId, familiaId) {
    var f = estado.datos.filter(function (x) { return x.id === familiaId; })[0];
    var a = f && f.alumnos.filter(function (x) { return x.id === alumnoId; })[0];
    if (!f || !a) return;
    if (!f.libres.length) {
      abrirModal('<h2>No hay cupos libres</h2><p>Esta familia no tiene suscripciones sin alumno. Agregá un cupo primero y después vinculalo.</p>' +
        '<div class="wv-modal-pie"><button type="button" class="wv-btn" data-no>Entendido</button></div>')
        .querySelector('[data-no]').onclick = cerrarModal;
      return;
    }
    var opts = f.libres.map(function (s, i) {
      return '<option value="' + s.id + '">Cupo ' + (i + 1) + ' · ' + (ESTADO[s.status] ? ESTADO[s.status].txt : s.status) +
        (s.amount ? ' · $' + Number(s.amount).toLocaleString('es-AR') : '') + '</option>';
    }).join('');
    var caja = abrirModal(
      '<h2>Vincular cupo</h2><p>Elegí qué suscripción le corresponde a ' + esc(a.nombre) + '.</p>' +
      '<div class="campo"><label for="vi-sub">Cupo libre</label><select id="vi-sub">' + opts + '</select></div>' +
      '<p class="mensaje" id="m-error" hidden></p>' +
      '<div class="wv-modal-pie"><button type="button" class="wv-btn suave" data-no>Cancelar</button><button type="button" class="wv-btn" data-si>Vincular</button></div>');
    caja.querySelector('[data-no]').onclick = cerrarModal;
    var si = caja.querySelector('[data-si]'), er = caja.querySelector('#m-error');
    si.onclick = async function () {
      si.disabled = true; er.hidden = true;
      try {
        await accion({ action: 'link_subscription', subscription_id: caja.querySelector('#vi-sub').value, student_id: alumnoId });
        await recargar(); cerrarModal(); toast('Cupo vinculado');
      } catch (e) { er.textContent = e.message; er.hidden = false; si.disabled = false; }
    };
  }

  var PAISES = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'España', 'Estados Unidos', 'Guatemala', 'Honduras', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'Puerto Rico', 'República Dominicana', 'Uruguay', 'Venezuela', 'Otro'];
  function cambiarCurriculo(sel) { // el país define el idioma (Argentina: voseo; otro país: español neutro) y la versión de Ciencias Sociales
    var id = sel.getAttribute('data-cur'), nom = sel.getAttribute('data-nom'), nuevo = sel.value, previo = sel.getAttribute('data-pais');
    sel.value = previo;
    var cambiaCur = (nuevo === 'Argentina') !== (previo === 'Argentina');
    var txt = (nuevo === 'Argentina' ? 'Va a ver las clases y los PDF con voseo argentino.' : 'Va a ver las clases y los PDF en español neutro latinoamericano.') +
      (cambiaCur ? (nuevo === 'Argentina' ? ' También pasa a la versión argentina de Ciencias Sociales.' : ' También pasa a la versión internacional de Ciencias Sociales.') +
        ' El avance que ya tenga en Ciencias Sociales de la otra versión no se traslada, porque las lecciones son distintas.' : '');
    confirmar('Cambiar el país de ' + nom + ' a ' + nuevo, txt, 'Cambiar', false, async function () {
      var r = await sb.rpc('set_student_pais', { p_student: id, p_pais: nuevo });
      if (r.error) throw r.error;
      await recargar(); cerrarModal(); toast('País actualizado');
    });
  }

  function resetear(profileId, nombre) {
    confirmar('Resetear contraseña', 'Se le va a asignar la contraseña inicial a ' + nombre + ' y tendrá que cambiarla al ingresar.', 'Resetear', false, async function () {
      var r = await accion({ action: 'reset_password', profile_id: profileId });
      var p = null;
      estado.datos.forEach(function (f) {
        if (f.perfil.id === profileId) p = f.perfil;
        f.alumnos.forEach(function (a) { if (a.perfil.id === profileId) p = a.perfil; });
      });
      mostrarCredenciales('Contraseña reseteada', (p && p.email) || nombre, r.initial_password);
    });
  }

  function suspender(profileId, suspender, nombre, esFamilia) {
    var txt = suspender
      ? 'No va a poder ingresar a la plataforma hasta que lo reactives.' + (esFamilia ? ' También se suspende a todos sus hijos.' : '')
      : 'Va a volver a poder ingresar.' + (esFamilia ? ' También se reactiva a todos sus hijos.' : '');
    confirmar((suspender ? 'Suspender a ' : 'Reactivar a ') + nombre, txt, suspender ? 'Suspender' : 'Reactivar', suspender, async function () {
      await accion({ action: 'set_suspended', profile_id: profileId, suspended: suspender });
      await recargar(); cerrarModal(); toast(suspender ? 'Cuenta suspendida' : 'Cuenta reactivada');
    });
  }

  async function vistaFamilias() {
    vista.innerHTML =
      '<h1 class="wv-titulo">Familias y alumnos</h1>' +
      '<p class="wv-sub">Estado de cuota, último acceso y acciones de cada cuenta.</p>' +
      '<div class="wv-resumen" id="wv-resumen"></div>' +
      '<div class="wv-tools">' +
        '<input id="wv-buscar" class="wv-buscar" type="text" name="filtro-lista" placeholder="Buscar familia, alumno o correo" autocomplete="off" autocapitalize="off" spellcheck="false" readonly>' +
        '<div class="wv-filtros" id="wv-filtros">' +
          [['todas', 'Todas'], ['aldia', 'Al día'], ['deuda', 'Con deuda'], ['sin', 'Sin cuota activa'], ['susp', 'Suspendidas']].map(function (x) {
            return '<button type="button" class="wv-chip' + (estado.filtro === x[0] ? ' on' : '') + '" data-f="' + x[0] + '">' + x[1] + '</button>';
          }).join('') +
        '</div>' +
        '<button type="button" class="wv-btn" id="wv-nueva">+ Nueva familia</button>' +
      '</div>' +
      '<div id="wv-lista"><div class="wv-vacio">Cargando…</div></div>';

    var buscar = document.getElementById('wv-buscar');
    // Evita que el navegador lo autocomplete con el correo guardado (filtraba la lista y la dejaba vacía)
    estado.busqueda = '';
    buscar.value = '';
    buscar.addEventListener('focus', function () { buscar.removeAttribute('readonly'); });
    buscar.oninput = function () {
      // Solo filtra si lo está escribiendo la persona (un autocompletado no tiene el foco)
      if (document.activeElement !== buscar) { buscar.value = estado.busqueda; return; }
      estado.busqueda = buscar.value; pintarLista();
    };
    document.getElementById('wv-nueva').onclick = nuevaFamilia;
    document.getElementById('wv-filtros').onclick = function (ev) {
      var b = ev.target.closest('[data-f]'); if (!b) return;
      estado.filtro = b.getAttribute('data-f');
      document.querySelectorAll('#wv-filtros .wv-chip').forEach(function (c) { c.classList.toggle('on', c === b); });
      pintarLista();
    };
    document.getElementById('wv-lista').onchange = function (ev) {
      var c = ev.target.closest('[data-mod]'); if (c) return cambiarModalidad(c);
      c = ev.target.closest('[data-tut]'); if (c) return cambiarTutor(c);
      c = ev.target.closest('[data-cur]'); if (c) cambiarCurriculo(c);
    };
    document.getElementById('wv-lista').onclick = function (ev) {
      var b;
      if ((b = ev.target.closest('[data-cupo]'))) return agregarCupo(b.getAttribute('data-cupo'));
      if ((b = ev.target.closest('[data-tray]'))) return trayectoria(b.getAttribute('data-tray'), b.getAttribute('data-nom'));
      if ((b = ev.target.closest('[data-vincular]'))) return vincular(b.getAttribute('data-vincular'), b.getAttribute('data-fam'));
      if ((b = ev.target.closest('[data-reset]'))) return resetear(b.getAttribute('data-reset'), b.getAttribute('data-nom'));
      if ((b = ev.target.closest('[data-susp]'))) return suspender(b.getAttribute('data-susp'), b.getAttribute('data-a') === '1', b.getAttribute('data-nom'), b.hasAttribute('data-fam-susp'));
    };

    try { await recargar(); }
    catch (e) {
      console.error(e);
      var lista = document.getElementById('wv-lista');
      if (lista) lista.innerHTML = '<div class="wv-vacio">No pudimos cargar los datos.<br><small>' + esc((e && (e.message || e.details)) || e) + '</small></div>';
    }
  }


  // ---------- Facturación ----------
  var fac = { tab: 'subs', filtro: 'todas', busqueda: '', subs: [], pagos: [], eventos: [], gracia: 15 };

  function dinero(n, moneda) {
    if (n == null || n === '') return '—';
    var t = '$' + Number(n).toLocaleString('es-AR', { maximumFractionDigits: 2 });
    return moneda && moneda !== 'ARS' ? t + ' ' + moneda : t;
  }
  function fechaCorta(iso) { return iso ? new Date(iso).toLocaleDateString('es-AR') : '—'; }
  function fechaHora(iso) {
    if (!iso) return '—';
    var d = new Date(iso);
    return d.toLocaleDateString('es-AR') + ' ' + d.toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' });
  }
  function diasHasta(iso) {
    var hoy = new Date(); hoy.setHours(0, 0, 0, 0);
    var f = new Date(iso); f.setHours(0, 0, 0, 0);
    return Math.round((f - hoy) / 86400000);
  }
  function textoProximo(sub) {
    if (!sub.next_payment_date || sub.status === 'cancelled' || sub.status === 'suspended') return '—';
    var d = diasHasta(sub.next_payment_date);
    var rel = d < 0 ? 'venció hace ' + (-d) + (d === -1 ? ' día' : ' días') : d === 0 ? 'hoy' : d === 1 ? 'mañana' : 'en ' + d + ' días';
    return fechaCorta(sub.next_payment_date) + ' · ' + rel;
  }

  var ESTADO_PAGO = {
    approved:   { txt: 'Aprobado',  cls: 'ok' },
    processed:  { txt: 'Aprobado',  cls: 'ok' },
    rejected:   { txt: 'Rechazado', cls: 'deuda' },
    cancelled:  { txt: 'Cancelado', cls: 'off' },
    refunded:   { txt: 'Reintegrado', cls: 'off' },
    charged_back: { txt: 'Contracargo', cls: 'deuda' },
    pending:    { txt: 'Pendiente', cls: 'pend' },
    in_process: { txt: 'En proceso', cls: 'pend' },
    scheduled:  { txt: 'Programado', cls: 'pend' }
  };
  function pillPago(st) {
    var e = ESTADO_PAGO[st];
    return '<span class="wv-pill ' + (e ? e.cls : 'off') + '">' + esc(e ? e.txt : (st || '—')) + '</span>';
  }
  function esAprobado(st) { return st === 'approved' || st === 'processed'; }

  function quien(sub) {
    var fam = sub && sub.families && sub.families.profiles ? sub.families.profiles : {};
    var alu = sub && sub.students ? sub.students.first_name + ' ' + sub.students.last_name : null;
    return { familia: fam.full_name || fam.email || 'Familia sin nombre', correo: fam.email || '', alumno: alu };
  }

  async function cargarFacturacion() {
    var res = await Promise.all([
      sb.from('subscriptions')
        .select('id, status, amount, currency, mp_preapproval_id, next_payment_date, last_payment_at, past_due_since, cancelled_at, created_at, families(profiles!families_profile_id_fkey(full_name, email)), students(first_name, last_name)')
        .order('created_at', { ascending: false }),
      sb.from('payments')
        .select('id, mp_payment_id, status, amount, paid_at, created_at, subscriptions(families(profiles!families_profile_id_fkey(full_name, email)), students(first_name, last_name))')
        .order('created_at', { ascending: false }).limit(200),
      sb.from('mp_webhook_events')
        .select('id, topic, resource_id, received_at, processed_at, error, payload')
        .order('received_at', { ascending: false }).limit(100),
      sb.from('app_settings').select('value').eq('key', 'grace_days').maybeSingle()
    ]);
    if (res[0].error) throw res[0].error;
    if (res[1].error) throw res[1].error;
    if (res[2].error) throw res[2].error;
    fac.subs = res[0].data || [];
    fac.pagos = res[1].data || [];
    fac.eventos = res[2].data || [];
    if (res[3].data && Number(res[3].data.value) > 0) fac.gracia = Number(res[3].data.value);
  }

  function pintarResumenFac() {
    var activas = 0, deuda = 0, pend = 0, esperado = 0, prox7 = 0, cobradoMes = 0, errores = 0;
    var ahora = new Date();
    fac.subs.forEach(function (s) {
      if (s.status === 'active') activas++;
      if (s.status === 'past_due') deuda++;
      if (s.status === 'pending') pend++;
      if (s.status === 'active' || s.status === 'past_due') esperado += Number(s.amount || 0);
      if (s.status === 'active' && s.next_payment_date) {
        var d = diasHasta(s.next_payment_date);
        if (d >= 0 && d <= 7) prox7++;
      }
    });
    fac.pagos.forEach(function (p) {
      if (!esAprobado(p.status) || !p.paid_at) return;
      var f = new Date(p.paid_at);
      if (f.getFullYear() === ahora.getFullYear() && f.getMonth() === ahora.getMonth()) cobradoMes += Number(p.amount || 0);
    });
    fac.eventos.forEach(function (e) { if (e.error) errores++; });

    document.getElementById('wv-resumen-fac').innerHTML = [
      ['Activas', activas, ''], ['Con deuda', deuda, deuda ? 'alerta' : ''], ['Pendientes', pend, ''],
      ['Ingreso mensual esperado', dinero(esperado), ''], ['Cobrado este mes', dinero(cobradoMes), ''],
      ['Cobros en 7 días', prox7, ''], ['Avisos con error', errores, errores ? 'alerta' : '']
    ].map(function (x) {
      return '<div class="wv-stat' + (x[2] ? ' ' + x[2] : '') + '"><small>' + x[0] + '</small><b>' + x[1] + '</b></div>';
    }).join('');
  }

  function subCoincide(s) {
    var q = fac.busqueda.trim().toLowerCase();
    if (q) {
      var w = quien(s);
      var t = [w.familia, w.correo, w.alumno || '', s.mp_preapproval_id || '', s.id].join(' ').toLowerCase();
      if (t.indexOf(q) === -1) return false;
    }
    switch (fac.filtro) {
      case 'activas': return s.status === 'active';
      case 'deuda': return s.status === 'past_due';
      case 'pend': return s.status === 'pending';
      case 'baja': return s.status === 'cancelled' || s.status === 'suspended';
      default: return true;
    }
  }

  function htmlSub(s) {
    var w = quien(s);
    var mora = '';
    if (s.status === 'past_due' && s.past_due_since) {
      var dias = Math.floor((Date.now() - new Date(s.past_due_since).getTime()) / 86400000);
      var quedan = fac.gracia - dias;
      mora = '<div class="wv-dato wv-mora">En mora hace ' + dias + (dias === 1 ? ' día' : ' días') +
        (quedan > 0 ? ' · quedan ' + quedan + ' de gracia' : ' · gracia vencida') + '</div>';
    }
    return '<div class="wv-fila">' +
      '<div><div class="wv-nombre">' + esc(w.familia) + '</div>' +
        '<div class="wv-dato">' + esc(w.correo) + '</div>' +
        '<div class="wv-dato">' + (w.alumno ? 'Alumno: ' + esc(w.alumno) : '<i>Cupo sin alumno vinculado</i>') + '</div></div>' +
      '<div><span class="wv-rot">Estado</span>' + pill(s.status) + mora +
        (s.status === 'cancelled' && s.cancelled_at ? '<div class="wv-dato">Desde ' + fechaCorta(s.cancelled_at) + '</div>' : '') + '</div>' +
      '<div><span class="wv-rot">Monto</span><span class="wv-monto">' + esc(dinero(s.amount, s.currency)) + '</span><div class="wv-dato">por mes</div></div>' +
      '<div><span class="wv-rot">Próximo cobro</span><span class="wv-dato-fuerte">' + esc(textoProximo(s)) + '</span>' +
        '<div class="wv-dato">Último pago: ' + (s.last_payment_at ? fechaCorta(s.last_payment_at) : 'ninguno') + '</div></div>' +
      '<div><span class="wv-rot">Mercado Pago</span><span class="wv-dato">' + (s.mp_preapproval_id ? 'ID ' + esc(s.mp_preapproval_id) : 'Sin vincular') + '</span>' +
        '<div class="wv-dato">Alta: ' + fechaCorta(s.created_at) + '</div>' +
        '<button type="button" class="wv-btn mini suave" style="margin-top:6px" data-copiar-id="' + esc(s.id) + '">Copiar ID de cupo</button></div>' +
      '</div>';
  }

  function htmlPago(p) {
    var w = quien(p.subscriptions);
    return '<div class="wv-fila pago">' +
      '<div><div class="wv-nombre">' + esc(w.familia) + '</div><div class="wv-dato">' + (w.alumno ? esc(w.alumno) : esc(w.correo)) + '</div></div>' +
      '<div><span class="wv-rot">Estado</span>' + pillPago(p.status) + '</div>' +
      '<div><span class="wv-rot">Monto</span><span class="wv-monto">' + esc(dinero(p.amount)) + '</span></div>' +
      '<div><span class="wv-rot">Fecha</span><span class="wv-dato-fuerte">' + esc(fechaHora(p.paid_at || p.created_at)) + '</span></div>' +
      '<div><span class="wv-rot">ID de pago</span><span class="wv-dato">' + esc(p.mp_payment_id || '—') + '</span></div>' +
      '</div>';
  }

  var TOPICS = {
    subscription_preapproval: 'Suscripción', preapproval: 'Suscripción',
    subscription_authorized_payment: 'Cobro de suscripción', authorized_payment: 'Cobro de suscripción',
    payment: 'Pago'
  };
  function htmlEvento(e) {
    var estadoE = e.error ? '<span class="wv-pill deuda">Revisar</span>'
      : e.processed_at ? '<span class="wv-pill ok">Procesado</span>' : '<span class="wv-pill pend">Pendiente</span>';
    var json = '';
    try { json = JSON.stringify(e.payload, null, 2); } catch (x) { json = ''; }
    return '<div class="wv-fila evento">' +
      '<div><div class="wv-nombre">' + esc(TOPICS[e.topic] || e.topic || '(sin tipo)') + '</div><div class="wv-dato">ID ' + esc(e.resource_id || '—') + '</div></div>' +
      '<div><span class="wv-rot">Estado</span>' + estadoE + '</div>' +
      '<div><span class="wv-rot">Recibido</span><span class="wv-dato-fuerte">' + esc(fechaHora(e.received_at)) + '</span></div>' +
      '<div class="wv-ancho">' + (e.error ? '<div class="wv-error-txt">' + esc(e.error) + '</div>' : '<div class="wv-dato">Sin errores</div>') +
        '<details><summary>Ver contenido del aviso</summary><pre class="wv-json">' + esc(json) + '</pre></details></div>' +
      '</div>';
  }

  function pintarListaFac() {
    var cont = document.getElementById('wv-lista-fac');
    var vacio = function (t) { return '<div class="wv-vacio">' + t + '</div>'; };
    if (fac.tab === 'subs') {
      var orden = { past_due: 0, pending: 1, active: 2, suspended: 3, cancelled: 4 };
      var vis = fac.subs.filter(subCoincide).sort(function (a, b) {
        var o = (orden[a.status] != null ? orden[a.status] : 9) - (orden[b.status] != null ? orden[b.status] : 9);
        if (o) return o;
        var fa = a.next_payment_date ? new Date(a.next_payment_date).getTime() : Infinity;
        var fb = b.next_payment_date ? new Date(b.next_payment_date).getTime() : Infinity;
        return fa - fb;
      });
      cont.innerHTML = vis.length ? vis.map(htmlSub).join('')
        : vacio(fac.subs.length ? 'No hay suscripciones con ese filtro.' : 'Todavía no hay suscripciones. Aparecen acá cuando una familia se suscribe en Mercado Pago o cuando agregás un cupo.');
    } else if (fac.tab === 'pagos') {
      cont.innerHTML = fac.pagos.length ? fac.pagos.map(htmlPago).join('') : vacio('Todavía no se registró ningún pago.');
    } else {
      var evs = fac.filtro === 'errores' ? fac.eventos.filter(function (e) { return e.error; }) : fac.eventos;
      cont.innerHTML = evs.length ? evs.map(htmlEvento).join('')
        : vacio(fac.eventos.length ? 'No hay avisos con errores.' : 'Todavía no llegó ningún aviso de Mercado Pago.');
    }
  }

  function pintarControlesFac() {
    var cont = document.getElementById('wv-tools-fac');
    var chips = function (lista, actual) {
      return lista.map(function (x) {
        return '<button type="button" class="wv-chip' + (actual === x[0] ? ' on' : '') + '" data-ff="' + x[0] + '">' + x[1] + '</button>';
      }).join('');
    };
    var filtros = '';
    if (fac.tab === 'subs') {
      filtros = '<input id="wv-buscar-fac" class="wv-buscar" type="text" name="filtro-facturacion" placeholder="Buscar familia, alumno, correo o ID" autocomplete="off" autocapitalize="off" spellcheck="false" readonly>' +
        '<div class="wv-filtros">' + chips([['todas', 'Todas'], ['activas', 'Al día'], ['deuda', 'Con deuda'], ['pend', 'Pendientes'], ['baja', 'Canceladas']], fac.filtro) + '</div>';
    } else if (fac.tab === 'avisos') {
      filtros = '<div class="wv-filtros">' + chips([['todas', 'Todos'], ['errores', 'Solo con error']], fac.filtro) + '</div>';
    }
    cont.innerHTML = filtros + '<button type="button" class="wv-btn suave" id="wv-act-fac">Actualizar</button>';

    var b = document.getElementById('wv-buscar-fac');
    if (b) {
      b.value = fac.busqueda;
      b.addEventListener('focus', function () { b.removeAttribute('readonly'); });
      b.oninput = function () {
        if (document.activeElement !== b) { b.value = fac.busqueda; return; }
        fac.busqueda = b.value; pintarListaFac();
      };
    }
    document.getElementById('wv-act-fac').onclick = async function () {
      this.disabled = true;
      try { await cargarFacturacion(); pintarResumenFac(); pintarListaFac(); toast('Datos actualizados'); }
      catch (e) { toast('No se pudo actualizar', true); }
      this.disabled = false;
    };
  }

  async function vistaFacturacion() {
    vista.innerHTML =
      '<h1 class="wv-titulo">Facturación</h1>' +
      '<p class="wv-sub">Suscripciones, próximos cobros, pagos y avisos de Mercado Pago.</p>' +
      '<div class="wv-resumen" id="wv-resumen-fac"></div>' +
      '<div class="wv-tabs" id="wv-tabs-fac">' +
        [['subs', 'Suscripciones'], ['pagos', 'Pagos'], ['avisos', 'Avisos de Mercado Pago']].map(function (x) {
          return '<button type="button" class="wv-tab' + (fac.tab === x[0] ? ' on' : '') + '" data-tab="' + x[0] + '">' + x[1] + '</button>';
        }).join('') +
      '</div>' +
      '<div class="wv-tools" id="wv-tools-fac"></div>' +
      '<div id="wv-lista-fac"><div class="wv-vacio">Cargando…</div></div>';

    document.getElementById('wv-tabs-fac').onclick = function (ev) {
      var t = ev.target.closest('[data-tab]'); if (!t) return;
      fac.tab = t.getAttribute('data-tab'); fac.filtro = 'todas';
      document.querySelectorAll('#wv-tabs-fac .wv-tab').forEach(function (x) { x.classList.toggle('on', x === t); });
      pintarControlesFac(); pintarListaFac();
    };
    document.getElementById('wv-tools-fac').onclick = function (ev) {
      var b = ev.target.closest('[data-ff]'); if (!b) return;
      fac.filtro = b.getAttribute('data-ff');
      document.querySelectorAll('#wv-tools-fac .wv-chip').forEach(function (c) { c.classList.toggle('on', c === b); });
      pintarListaFac();
    };
    document.getElementById('wv-lista-fac').onclick = function (ev) {
      var b = ev.target.closest('[data-copiar-id]'); if (!b) return;
      if (navigator.clipboard) {
        navigator.clipboard.writeText(b.getAttribute('data-copiar-id')).then(function () {
          b.textContent = '¡Copiado!'; setTimeout(function () { b.textContent = 'Copiar ID de cupo'; }, 1500);
        }, function () {});
      }
    };

    fac.busqueda = '';
    pintarControlesFac();
    try {
      await cargarFacturacion();
      pintarResumenFac();
      pintarListaFac();
    } catch (e) {
      console.error(e);
      var l = document.getElementById('wv-lista-fac');
      if (l) l.innerHTML = '<div class="wv-vacio">No pudimos cargar la facturación.<br><small>' + esc((e && (e.message || e.details)) || e) + '</small></div>';
    }
  }

  // ---------- Secciones que vienen después ----------
  function proximamente(titulo) {
    return function () {
      vista.innerHTML = '<h1 class="wv-titulo">' + titulo + '</h1><div class="wv-prox">Estamos armando esta sección. Muy pronto vas a encontrarla acá.</div>';
    };
  }

  // ---------- Tutores ----------
  async function vistaTutores() {
    vista.innerHTML = '<h1 class="vista-titulo">Tutores</h1>' +
      '<p class="wv-dato">Los tutores acompañan a los alumnos de las modalidades Guiada y Completa: dan las tutorías y corrigen proyectos y escritura. Se asignan a cada alumno en Familias y alumnos.</p>' +
      '<form id="wv-tut-form" class="wv-tut-form"><input id="wv-tut-nom" placeholder="Nombre y apellido" required> <input id="wv-tut-mail" type="email" placeholder="Correo" required> ' +
      '<button class="wv-btn" type="submit">Crear tutor</button></form><div id="wv-tut-cred"></div><div id="wv-tut-lista"><div class="wv-vacio">Cargando…</div></div>';
    async function pintar() {
      var r = await sb.rpc('tutores_admin');
      var l = document.getElementById('wv-tut-lista');
      if (r.error) { l.innerHTML = '<div class="wv-vacio">' + esc(r.error.message) + '</div>'; return; }
      l.innerHTML = !r.data.length ? '<div class="wv-vacio">Todavía no hay tutores.</div>' :
        '<div class="wv-alus">' + r.data.map(function (t) {
          return '<div class="wv-alu"><div><div class="wv-nombre">' + esc(t.nombre) + '</div><div class="wv-dato">' + esc(t.email) + '</div></div>' +
            '<div><span class="wv-rot">Alumnos</span><span class="wv-dato">' + t.alumnos + '</span></div></div>';
        }).join('') + '</div>';
    }
    document.getElementById('wv-tut-form').onsubmit = async function (ev) {
      ev.preventDefault();
      var b = this.querySelector('button'); b.disabled = true;
      var r = await sb.functions.invoke('admin-tutores', { body: { nombre: document.getElementById('wv-tut-nom').value, email: document.getElementById('wv-tut-mail').value } });
      b.disabled = false;
      if (r.error || (r.data && r.data.error)) { toast((r.data && r.data.error) || 'No se pudo crear el tutor', true); return; }
      document.getElementById('wv-tut-cred').innerHTML = '<div class="wv-vacio">Tutor creado. Usuario: <b>' + esc(r.data.email) + '</b> · Clave inicial: <b>' + esc(r.data.initial_password) + '</b> (la cambia al entrar). Entra por la misma página de ingreso.</div>';
      this.reset(); pintar();
    };
    pintar();
  }

  // ---------- Agenda de dirección: horarios y turnos con las familias ----------
  async function vistaAgenda() {
    var DIAS = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
    function fh(v) { var d = new Date(v); return d.toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · ' + d.toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + ' h'; }
    vista.innerHTML = '<h1 class="vista-titulo">Agenda de dirección</h1>' +
      '<p class="wv-dato">Las familias (de cualquier modalidad) piden turno de videollamada con dirección dentro de estos horarios (hora de Argentina). No descuentan de sus tutorías. Para que la sala se abra, entrá vos primero con tu cuenta de Google.</p>' +
      '<form id="wv-ag-form" class="wv-tut-form"><select id="wv-ag-dia">' + DIAS.slice(1).map(function (d, i) { return '<option value="' + (i + 1) + '">' + d + '</option>'; }).join('') + '</select> ' +
      'de <input id="wv-ag-desde" type="time" value="10:00" required> a <input id="wv-ag-hasta" type="time" value="13:00" required> turnos de <select id="wv-ag-dur"><option>15</option><option selected>30</option><option>45</option><option>60</option></select> min ' +
      '<button class="wv-btn" type="submit">Agregar horario</button></form><div id="wv-ag-horas"></div><div id="wv-ag-turnos"><div class="wv-vacio">Cargando…</div></div>';
    var ses = await sb.auth.getSession(), yo = ses.data.session.user.id;
    async function horas() {
      var r = await sb.from('tutor_disponibilidad').select('id, dia_semana, desde, hasta, duracion_min').eq('tutor_id', yo).order('dia_semana').order('desde');
      var c = document.getElementById('wv-ag-horas');
      c.innerHTML = !(r.data || []).length ? '<div class="wv-vacio">Todavía no cargaste horarios: sin horarios, las familias no pueden pedir turno.</div>' :
        '<div class="wv-alus">' + r.data.map(function (h) {
          return '<div class="wv-alu"><div class="wv-dato"><b>' + DIAS[h.dia_semana] + '</b> de ' + h.desde.slice(0, 5) + ' a ' + h.hasta.slice(0, 5) + ' h · turnos de ' + h.duracion_min + ' min</div>' +
            '<button type="button" class="wv-btn" data-borrar="' + h.id + '">Quitar</button></div>';
        }).join('') + '</div>';
    }
    async function turnos() {
      var r = await sb.rpc('agenda_direccion'), c = document.getElementById('wv-ag-turnos');
      if (r.error) { c.innerHTML = '<div class="wv-vacio">' + esc(r.error.message) + '</div>'; return; }
      var ahora = Date.now();
      var prox = r.data.filter(function (t) { return t.estado === 'reservada' && new Date(t.fin).getTime() > ahora; });
      var cerrar = r.data.filter(function (t) { return t.estado === 'reservada' && new Date(t.fin).getTime() <= ahora; });
      var hechas = r.data.filter(function (t) { return t.estado !== 'reservada'; }).reverse().slice(0, 15);
      function card(t, modo) {
        return '<div class="wv-alu wv-ag-turno" data-id="' + t.id + '"><div style="flex:1"><div class="wv-nombre">' + esc(t.familia || t.email) + (t.alumno ? ' · ' + esc(t.alumno) : '') + '</div>' +
          '<div class="wv-dato">' + esc(fh(t.inicio)) + ' · <b>' + esc(t.motivo) + '</b>' + (t.tema ? ' · ' + esc(t.tema) : '') + '</div>' +
          '<div class="wv-dato">' + esc(t.email || '') + (t.telefono ? ' · ' + esc(t.telefono) : '') + '</div>' +
          (modo === 'hecha' ? '<div class="wv-dato">' + (t.estado === 'ausente' ? 'No se presentó.' : 'Realizado.') + (t.notas ? ' ' + esc(t.notas) : '') + '</div>' : '') +
          (modo === 'cerrar' ? '<textarea class="wv-ag-notas" placeholder="Notas (la familia las ve)"></textarea>' : '') + '</div><div>' +
          (modo === 'prox' ? '<a class="wv-btn" href="' + esc(t.link) + '" target="_blank" rel="noopener">Entrar</a> <button type="button" class="wv-btn" data-cancelar="' + t.id + '">Cancelar</button>' : '') +
          (modo === 'cerrar' ? '<button type="button" class="wv-btn" data-cerrar="realizada">Se hizo</button> <button type="button" class="wv-btn" data-cerrar="ausente">No se presentó</button>' : '') +
          '</div></div>';
      }
      c.innerHTML = (cerrar.length ? '<h2 class="wv-sub">Para cerrar</h2><div class="wv-alus">' + cerrar.map(function (t) { return card(t, 'cerrar'); }).join('') + '</div>' : '') +
        '<h2 class="wv-sub">Próximos turnos</h2>' + (prox.length ? '<div class="wv-alus">' + prox.map(function (t) { return card(t, 'prox'); }).join('') + '</div>' : '<div class="wv-vacio">No hay turnos pedidos.</div>') +
        (hechas.length ? '<h2 class="wv-sub">Últimos</h2><div class="wv-alus">' + hechas.map(function (t) { return card(t, 'hecha'); }).join('') + '</div>' : '');
    }
    document.getElementById('wv-ag-form').onsubmit = async function (ev) {
      ev.preventDefault();
      var r = await sb.from('tutor_disponibilidad').insert({ tutor_id: yo, dia_semana: +document.getElementById('wv-ag-dia').value,
        desde: document.getElementById('wv-ag-desde').value, hasta: document.getElementById('wv-ag-hasta').value, duracion_min: +document.getElementById('wv-ag-dur').value });
      if (r.error) { toast(/hasta/.test(r.error.message) ? 'La hora de fin tiene que ser después de la de inicio' : 'No se pudo guardar', true); return; }
      toast('Horario agregado'); horas();
    };
    var clicAgenda = async function (ev) {
      var b;
      if ((b = ev.target.closest('[data-borrar]'))) {
        var r = await sb.from('tutor_disponibilidad').delete().eq('id', b.getAttribute('data-borrar'));
        if (r.error) toast('No se pudo quitar', true); else horas();
      } else if ((b = ev.target.closest('[data-cancelar]'))) {
        if (!confirm('¿Cancelar este turno? Avisale a la familia.')) return;
        var x = await sb.rpc('cancelar_tutoria', { p_id: b.getAttribute('data-cancelar') });
        if (x.error) toast(x.error.message, true); else turnos();
      } else if ((b = ev.target.closest('[data-cerrar]'))) {
        var card = b.closest('[data-id]');
        var y = await sb.rpc('cerrar_tutoria', { p_id: card.getAttribute('data-id'), p_estado: b.getAttribute('data-cerrar'), p_notas: card.querySelector('.wv-ag-notas').value });
        if (y.error) toast(y.error.message, true); else turnos();
      }
    };
    document.getElementById('wv-ag-horas').onclick = clicAgenda;
    document.getElementById('wv-ag-turnos').onclick = clicAgenda;
    horas(); turnos();
  }

  var VISTAS = {
    familias: vistaFamilias,
    facturacion: vistaFacturacion,
    tutores: vistaTutores,
    agenda: vistaAgenda,
    contenido: function () { return WaveContenido.abrir(vista); },
    curricular: function () { return WaveCurricular.abrir(vista); },
    fabrica: function () { return WaveFabrica.abrir(vista); },
    videos: function () { return WaveVideos.abrir(vista); },
    seguimiento: proximamente('Seguimiento de alumnos'),
    registro: proximamente('Registro de actividad')
  };

  function ruta() {
    cerrarModal();
    var nombre = (location.hash || '#familias').slice(1);
    if (!VISTAS[nombre]) nombre = 'familias';
    enlaces.forEach(function (a) { a.classList.toggle('activo', a.getAttribute('href') === '#' + nombre); });
    try { Promise.resolve(VISTAS[nombre]()).catch(mostrarFallo); } catch (e) { mostrarFallo(e); }
  }

  // Si algo falla, lo mostramos en pantalla en vez de dejarla en blanco
  function mostrarFallo(e) {
    console.error(e);
    vista.innerHTML = '<div class="wv-vacio">Ocurrió un error al armar el panel.<br><small>' + esc((e && (e.message || e)) || 'Error') + '</small></div>';
  }
  window.addEventListener('error', function (ev) { if (!vista.innerHTML.trim()) mostrarFallo(ev.error || ev.message); });
  window.addEventListener('unhandledrejection', function (ev) { if (!vista.innerHTML.trim()) mostrarFallo(ev.reason); });

  window.addEventListener('hashchange', ruta);
  ruta();
  // Red de seguridad: si por cualquier motivo la vista quedó vacía, se vuelve a armar
  setTimeout(function () { if (!vista.innerHTML.trim()) ruta(); }, 1500);
})();
