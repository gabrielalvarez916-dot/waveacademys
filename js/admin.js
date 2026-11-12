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
    t.className = 'ad-toast' + (error ? ' error' : '');
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
    modalEl.className = 'ad-modal';
    modalEl.innerHTML = '<div class="ad-modal-caja" role="dialog" aria-modal="true">' + html + '</div>';
    modalEl.addEventListener('mousedown', function (ev) { if (ev.target === modalEl) cerrarModal(); });
    document.body.appendChild(modalEl);
    document.addEventListener('keydown', teclaModal);
    return modalEl.querySelector('.ad-modal-caja');
  }

  function confirmar(titulo, texto, textoBoton, peligro, alAceptar) {
    var caja = abrirModal(
      '<h2>' + esc(titulo) + '</h2><p>' + esc(texto) + '</p>' +
      '<p class="mensaje" id="m-error" hidden></p>' +
      '<div class="ad-modal-pie"><button type="button" class="ad-btn suave" data-no>Cancelar</button>' +
      '<button type="button" class="ad-btn' + (peligro ? ' peligro' : '') + '" data-si>' + esc(textoBoton) + '</button></div>');
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
      '<div class="ad-cred-fila"><div><small>Usuario</small><b>' + esc(usuario) + '</b></div>' +
        '<button type="button" class="ad-btn mini" data-copiar="' + esc(usuario) + '">Copiar</button></div>' +
      '<div class="ad-cred-fila"><div><small>Contraseña inicial</small><b>' + esc(clave) + '</b></div>' +
        '<button type="button" class="ad-btn mini" data-copiar="' + esc(clave) + '">Copiar</button></div>' +
      '<div class="ad-modal-pie"><button type="button" class="ad-btn" data-no>Listo</button></div>');
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
    if (!e) return '<span class="ad-pill off">Sin suscripción</span>';
    return '<span class="ad-pill ' + e.cls + '">' + e.txt + '</span>';
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
        .select('id, family_id, first_name, last_name, grades(name, levels(name)), profiles!students_profile_id_fkey(id, email, is_suspended, last_seen_at)')
        .order('created_at', { ascending: true }),
      sb.from('subscriptions')
        .select('id, family_id, student_id, status, amount, currency, created_at')
        .order('created_at', { ascending: true })
    ]);
    res.forEach(function (r) { if (r.error) throw r.error; });

    var alumnos = res[1].data || [], subs = res[2].data || [];
    return (res[0].data || []).map(function (f) {
      var misSubs = subs.filter(function (s) { return s.family_id === f.id; });
      return {
        id: f.id, phone: f.phone, perfil: f.profiles || {},
        subs: misSubs,
        libres: misSubs.filter(function (s) { return !s.student_id; }),
        alumnos: alumnos.filter(function (a) { return a.family_id === f.id; }).map(function (a) {
          return {
            id: a.id, nombre: a.first_name + ' ' + a.last_name,
            anio: a.grades ? ((a.grades.levels && a.grades.levels.name !== a.grades.name ? a.grades.levels.name + ' · ' : '') + a.grades.name) : '',
            perfil: a.profiles || {},
            sub: misSubs.filter(function (s) { return s.student_id === a.id; })[0] || null
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

  function htmlAlumno(a, f) {
    var susp = a.perfil.is_suspended;
    return '<div class="ad-alu">' +
      '<div><div class="ad-nombre">' + esc(a.nombre) + (susp ? '<span class="ad-pill susp">Suspendido</span>' : '') + '</div>' +
        '<div class="ad-dato">' + esc(a.anio) + (a.perfil.email ? ' · ' + esc(a.perfil.email) : '') + '</div></div>' +
      '<div><span class="ad-rot">Cuota</span>' + (a.sub ? pill(a.sub.status) : '<span class="ad-pill off">Sin cupo vinculado</span>') + '</div>' +
      '<div><span class="ad-rot">Último acceso</span><span class="ad-dato">' + esc(haceCuanto(a.perfil.last_seen_at)) + '</span></div>' +
      '<div class="ad-acc">' +
        (!a.sub ? '<button type="button" class="ad-btn mini suave" data-vincular="' + a.id + '" data-fam="' + f.id + '">Vincular cupo</button>' : '') +
        (a.perfil.id ? '<button type="button" class="ad-btn mini suave" data-reset="' + a.perfil.id + '" data-nom="' + esc(a.nombre) + '">Resetear clave</button>' +
          '<button type="button" class="ad-btn mini ' + (susp ? '' : 'peligro') + '" data-susp="' + a.perfil.id + '" data-a="' + (susp ? 0 : 1) + '" data-nom="' + esc(a.nombre) + '">' + (susp ? 'Reactivar' : 'Suspender') + '</button>' : '') +
      '</div></div>';
  }

  function htmlFamilia(f) {
    var p = f.perfil, susp = p.is_suspended;
    var nombre = p.full_name || p.email || 'Sin nombre';
    return '<section class="ad-fam' + (susp ? ' susp' : '') + '">' +
      '<div class="ad-fam-cab">' +
        '<div><div class="ad-nombre">' + esc(nombre) + (susp ? '<span class="ad-pill susp">Suspendida</span>' : '') + '</div>' +
          '<div class="ad-dato">' + esc(p.email || '') + (f.phone ? ' · ' + esc(f.phone) : '') + '</div></div>' +
        '<div><span class="ad-rot">Cuota</span>' + pill(f.estado) +
          '<div class="ad-dato" style="margin-top:4px">' + f.subs.length + (f.subs.length === 1 ? ' cupo' : ' cupos') +
          (f.libres.length ? ' · ' + f.libres.length + (f.libres.length === 1 ? ' libre' : ' libres') : '') + '</div></div>' +
        '<div><span class="ad-rot">Último acceso</span><span class="ad-dato">' + esc(haceCuanto(p.last_seen_at)) + '</span></div>' +
        '<div class="ad-acc">' +
          '<button type="button" class="ad-btn mini suave" data-cupo="' + f.id + '">Agregar cupo</button>' +
          '<button type="button" class="ad-btn mini suave" data-reset="' + p.id + '" data-nom="' + esc(nombre) + '">Resetear clave</button>' +
          '<button type="button" class="ad-btn mini ' + (susp ? '' : 'peligro') + '" data-susp="' + p.id + '" data-a="' + (susp ? 0 : 1) + '" data-nom="' + esc(nombre) + '" data-fam-susp="1">' + (susp ? 'Reactivar' : 'Suspender') + '</button>' +
        '</div>' +
      '</div>' +
      '<div class="ad-alumnos">' +
        (f.alumnos.length ? f.alumnos.map(function (a) { return htmlAlumno(a, f); }).join('')
          : '<div class="ad-sin">Todavía no dio de alta a ningún alumno.</div>') +
      '</div></section>';
  }

  function pintarLista() {
    var cont = document.getElementById('ad-lista');
    var vis = estado.datos.filter(coincide);
    cont.innerHTML = vis.length ? vis.map(htmlFamilia).join('')
      : '<div class="ad-vacio">' + (estado.datos.length ? 'No hay resultados para esa búsqueda.' : 'Todavía no hay familias. Creá la primera con “Nueva familia”.') + '</div>';
  }

  function pintarResumen() {
    var d = estado.datos, alumnos = 0, deuda = 0, libres = 0;
    d.forEach(function (f) {
      alumnos += f.alumnos.length; libres += f.libres.length;
      if (f.estado === 'past_due') deuda++;
    });
    document.getElementById('ad-resumen').innerHTML =
      [['Familias', d.length], ['Alumnos', alumnos], ['Con deuda', deuda], ['Cupos libres', libres]].map(function (x) {
        return '<div class="ad-stat"><small>' + x[0] + '</small><b>' + x[1] + '</b></div>';
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
      '<div class="ad-modal-pie"><button type="button" class="ad-btn suave" data-no>Cancelar</button><button type="button" class="ad-btn" data-si>Crear familia</button></div>');
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
      '<div class="ad-modal-pie"><button type="button" class="ad-btn suave" data-no>Cancelar</button><button type="button" class="ad-btn" data-si>Agregar cupo</button></div>');
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
        '<div class="ad-modal-pie"><button type="button" class="ad-btn" data-no>Entendido</button></div>')
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
      '<div class="ad-modal-pie"><button type="button" class="ad-btn suave" data-no>Cancelar</button><button type="button" class="ad-btn" data-si>Vincular</button></div>');
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
      '<h1 class="ad-titulo">Familias y alumnos</h1>' +
      '<p class="ad-sub">Estado de cuota, último acceso y acciones de cada cuenta.</p>' +
      '<div class="ad-resumen" id="ad-resumen"></div>' +
      '<div class="ad-tools">' +
        '<input id="ad-buscar" class="ad-buscar" type="search" placeholder="Buscar familia, alumno o correo" autocomplete="off">' +
        '<div class="ad-filtros" id="ad-filtros">' +
          [['todas', 'Todas'], ['aldia', 'Al día'], ['deuda', 'Con deuda'], ['sin', 'Sin cuota activa'], ['susp', 'Suspendidas']].map(function (x) {
            return '<button type="button" class="ad-chip' + (estado.filtro === x[0] ? ' on' : '') + '" data-f="' + x[0] + '">' + x[1] + '</button>';
          }).join('') +
        '</div>' +
        '<button type="button" class="ad-btn" id="ad-nueva">+ Nueva familia</button>' +
      '</div>' +
      '<div id="ad-lista"><div class="ad-vacio">Cargando…</div></div>';

    var buscar = document.getElementById('ad-buscar');
    buscar.value = estado.busqueda;
    buscar.oninput = function () { estado.busqueda = buscar.value; pintarLista(); };
    document.getElementById('ad-nueva').onclick = nuevaFamilia;
    document.getElementById('ad-filtros').onclick = function (ev) {
      var b = ev.target.closest('[data-f]'); if (!b) return;
      estado.filtro = b.getAttribute('data-f');
      document.querySelectorAll('#ad-filtros .ad-chip').forEach(function (c) { c.classList.toggle('on', c === b); });
      pintarLista();
    };
    document.getElementById('ad-lista').onclick = function (ev) {
      var b;
      if ((b = ev.target.closest('[data-cupo]'))) return agregarCupo(b.getAttribute('data-cupo'));
      if ((b = ev.target.closest('[data-vincular]'))) return vincular(b.getAttribute('data-vincular'), b.getAttribute('data-fam'));
      if ((b = ev.target.closest('[data-reset]'))) return resetear(b.getAttribute('data-reset'), b.getAttribute('data-nom'));
      if ((b = ev.target.closest('[data-susp]'))) return suspender(b.getAttribute('data-susp'), b.getAttribute('data-a') === '1', b.getAttribute('data-nom'), b.hasAttribute('data-fam-susp'));
    };

    try { await recargar(); }
    catch (e) { document.getElementById('ad-lista').innerHTML = '<div class="ad-vacio">No pudimos cargar los datos. Probá recargar la página.</div>'; }
  }

  // ---------- Secciones que vienen después ----------
  function proximamente(titulo) {
    return function () {
      vista.innerHTML = '<h1 class="ad-titulo">' + titulo + '</h1><div class="ad-prox">Estamos armando esta sección. Muy pronto vas a encontrarla acá.</div>';
    };
  }

  var VISTAS = {
    familias: vistaFamilias,
    facturacion: proximamente('Facturación'),
    contenido: proximamente('Contenido'),
    seguimiento: proximamente('Seguimiento de alumnos'),
    registro: proximamente('Registro de actividad')
  };

  function ruta() {
    cerrarModal();
    var nombre = (location.hash || '#familias').slice(1);
    if (!VISTAS[nombre]) nombre = 'familias';
    enlaces.forEach(function (a) { a.classList.toggle('activo', a.getAttribute('href') === '#' + nombre); });
    VISTAS[nombre]();
  }

  window.addEventListener('hashchange', ruta);
  ruta();
})();
