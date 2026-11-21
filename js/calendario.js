// Calendario de reuniones (tutorías, dirección, admisión y cobranzas): vista semanal, detalle, reagendar, cancelar, cerrar,
// días sin atención y reagendar del lado de la familia. Lo usan los paneles de admin, tutor y familia.
(function () {
  var sb = Wave.sb;
  var ALTO = 46; // px por hora
  var TIPOS = {
    tutoria: { n: 'Tutoría', c: '#087E83' },
    direccion: { n: 'Dirección', c: '#16393B' },
    admision: { n: 'Admisión', c: '#B97A12' },
    cobranzas: { n: 'Cobranzas', c: '#7A4FA0' },
    individual: { n: 'Tutoría individual', c: '#C2410C' }
  };
  var ESTADOS = { pendiente_pago: 'Pendiente de pago', reservada: 'Pendiente', realizada: 'Realizada', ausente: 'No se presentó', cancelada: 'Cancelada' };
  var DIAS = ['lun', 'mar', 'mié', 'jue', 'vie', 'sáb', 'dom'];

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function toast(t, err) {
    var el = document.createElement('div'); el.className = 'cal-toast' + (err ? ' err' : ''); el.textContent = t;
    document.body.appendChild(el); setTimeout(function () { el.remove(); }, 3500);
  }
  function lunes(d) { var x = new Date(d); x.setHours(0, 0, 0, 0); x.setDate(x.getDate() - ((x.getDay() + 6) % 7)); return x; }
  function hh(iso) { return new Date(iso).toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit', hour12: false }); }
  function cuando(iso) {
    return new Date(iso).toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · ' + hh(iso) + ' h';
  }
  function aInput(d) { // fecha local para <input type="datetime-local">
    var x = new Date(d); x.setMinutes(x.getMinutes() - x.getTimezoneOffset()); return x.toISOString().slice(0, 16);
  }
  function mins(e) { return Math.round((new Date(e.fin) - new Date(e.inicio)) / 60000); }

  // ---------- Modal ----------
  function modal(html, alCerrar) {
    var f = document.createElement('div'); f.className = 'cal-fondo';
    f.innerHTML = '<div class="cal-modal" role="dialog" aria-modal="true">' + html + '</div>';
    function cerrar() { document.removeEventListener('keydown', tecla); f.remove(); if (alCerrar) alCerrar(); }
    function tecla(ev) { if (ev.key === 'Escape') cerrar(); }
    f.addEventListener('mousedown', function (ev) { if (ev.target === f) cerrar(); });
    document.addEventListener('keydown', tecla);
    document.body.appendChild(f);
    return { el: f.firstChild, cerrar: cerrar };
  }

  // ---------- Vista semanal ----------
  function semana(cont, opts) {
    var st = { sem: lunes(new Date()), eventos: [], ocultos: {} };

    async function recargar() {
      try { st.eventos = await opts.cargar(); } catch (e) { cont.innerHTML = '<div class="cal-vacio">' + esc((e && e.message) || 'No pudimos cargar la agenda.') + '</div>'; return; }
      pintar();
    }

    function distribuir(lista) {
      var cols = [], cluster = [], finCluster = 0;
      function cerrar() { var n = cols.length; cluster.forEach(function (e) { e._n = n; }); cols = []; cluster = []; finCluster = 0; }
      lista.forEach(function (e) {
        var s = +new Date(e.inicio), f = +new Date(e.fin);
        if (cluster.length && s >= finCluster) cerrar();
        var c = 0; while (cols[c] !== undefined && cols[c] > s) c++;
        cols[c] = f; e._c = c; cluster.push(e); finCluster = Math.max(finCluster, f);
      });
      cerrar();
    }

    function pintar() {
      var ini = st.sem, fin = new Date(ini); fin.setDate(fin.getDate() + 7);
      var evs = st.eventos.filter(function (e) {
        var s = new Date(e.inicio);
        return e.estado !== 'cancelada' && !st.ocultos[e.tipo] && s >= ini && s < fin;
      }).sort(function (a, b) { return new Date(a.inicio) - new Date(b.inicio) || new Date(b.fin) - new Date(a.fin); });
      var h0 = 8, h1 = 20;
      evs.forEach(function (e) { h0 = Math.min(h0, new Date(e.inicio).getHours()); h1 = Math.max(h1, Math.ceil((+new Date(e.fin) - +new Date(e.inicio)) / 3600000 + new Date(e.inicio).getHours() + new Date(e.inicio).getMinutes() / 60)); });
      h0 = Math.max(0, h0); h1 = Math.min(24, Math.max(h1, h0 + 6));
      var porDia = [[], [], [], [], [], [], []];
      evs.forEach(function (e) { porDia[(new Date(e.inicio).getDay() + 6) % 7].push(e); });
      porDia.forEach(distribuir);
      var hoy = new Date(); hoy.setHours(0, 0, 0, 0);
      var ult = new Date(fin); ult.setDate(ult.getDate() - 1);
      var etiqueta = ini.toLocaleDateString('es-AR', { day: 'numeric', month: 'long' }) + ' al ' + ult.toLocaleDateString('es-AR', { day: 'numeric', month: 'long', year: 'numeric' });

      var tipos = {}; st.eventos.forEach(function (e) { tipos[e.tipo] = true; });
      var chips = opts.filtros ? '<div class="cal-chips">' + Object.keys(TIPOS).filter(function (k) { return tipos[k]; }).map(function (k) {
        return '<button type="button" class="cal-chip' + (st.ocultos[k] ? '' : ' on') + '" data-filtro="' + k + '" style="--c:' + TIPOS[k].c + '">' + TIPOS[k].n + '</button>';
      }).join('') + '</div>' : '';

      var horas = ''; for (var h = h0; h < h1; h++) horas += '<div class="cal-hora" style="height:' + ALTO + 'px"><span>' + (h < 10 ? '0' : '') + h + ':00</span></div>';
      var cols = porDia.map(function (lista, i) {
        var dia = new Date(ini); dia.setDate(dia.getDate() + i);
        var bloques = lista.map(function (e) {
          var s = new Date(e.inicio), top = ((s.getHours() * 60 + s.getMinutes()) - h0 * 60) / 60 * ALTO, alto = Math.max(mins(e) / 60 * ALTO, 28);
          var w = 100 / e._n;
          return '<button type="button" class="cal-ev ' + esc(e.estado) + '" data-id="' + esc(e.id) + '" style="top:' + top + 'px;height:' + alto + 'px;left:calc(' + (e._c * w) + '% + 2px);width:calc(' + w + '% - 4px);--c:' + (TIPOS[e.tipo] || TIPOS.tutoria).c + '">' +
            '<b>' + hh(e.inicio) + '</b> ' + esc(e.titulo || '') + (e.sub ? '<small>' + esc(e.sub) + '</small>' : '') + '</button>';
        }).join('');
        return '<div class="cal-col' + (+dia === +hoy ? ' hoy' : '') + '"><div class="cal-dia"><small>' + DIAS[i] + '</small> <b>' + dia.getDate() + '</b></div>' +
          '<div class="cal-cuerpo" style="height:' + ((h1 - h0) * ALTO) + 'px">' + bloques + '</div></div>';
      }).join('');
      var lista = porDia.map(function (l, i) {
        var dia = new Date(ini); dia.setDate(dia.getDate() + i);
        return '<div class="cal-lista-dia' + (+dia === +hoy ? ' hoy' : '') + '"><h3>' + esc(dia.toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' })) + '</h3>' +
          (l.length ? l.map(function (e) {
            return '<button type="button" class="cal-item ' + esc(e.estado) + '" data-id="' + esc(e.id) + '" style="--c:' + (TIPOS[e.tipo] || TIPOS.tutoria).c + '"><b>' + hh(e.inicio) + ' – ' + hh(e.fin) + '</b> ' + esc(e.titulo || '') +
              '<small>' + esc((TIPOS[e.tipo] || {}).n || '') + (e.sub ? ' · ' + esc(e.sub) : '') + '</small></button>';
          }).join('') : '<p class="cal-nada">Sin reuniones</p>') + '</div>';
      }).join('');

      cont.innerHTML = '<div class="cal">' +
        '<div class="cal-barra"><div class="cal-nav"><button type="button" class="cal-btn" data-nav="-1" aria-label="Semana anterior">‹</button>' +
        '<button type="button" class="cal-btn" data-nav="0">Hoy</button><button type="button" class="cal-btn" data-nav="1" aria-label="Semana siguiente">›</button></div>' +
        '<div class="cal-rango">' + esc(etiqueta) + '</div>' + (opts.nuevo ? '<button type="button" class="cal-btn principal" data-nuevo>+ Agendar reunión</button>' : '') + '</div>' +
        chips +
        '<div class="cal-grid"><div class="cal-horas"><div class="cal-dia"></div>' + horas + '</div>' + cols + '</div>' +
        '<div class="cal-lista">' + lista + '</div></div>';
    }

    cont.onclick = function (ev) {
      var b;
      if ((b = ev.target.closest('[data-nav]'))) {
        var n = +b.getAttribute('data-nav');
        if (n === 0) st.sem = lunes(new Date()); else { st.sem = new Date(st.sem); st.sem.setDate(st.sem.getDate() + 7 * n); }
        pintar();
      } else if ((b = ev.target.closest('[data-filtro]'))) {
        var k = b.getAttribute('data-filtro'); st.ocultos[k] = !st.ocultos[k]; pintar();
      } else if ((b = ev.target.closest('[data-id]'))) {
        var id = b.getAttribute('data-id');
        var e = st.eventos.filter(function (x) { return String(x.id) === id; })[0];
        if (e) detalle(e, opts, recargar);
      } else if (ev.target.closest('[data-nuevo]')) {
        opts.nuevo(recargar);
      }
    };
    recargar();
    return { recargar: recargar };
  }

  // ---------- Detalle de una reunión ----------
  function detalle(e, opts, recargar) {
    var t = TIPOS[e.tipo] || TIPOS.tutoria;
    var pasada = new Date(e.fin).getTime() <= Date.now();
    var filas = [];
    if (e.participante && e.tipo !== 'tutoria') filas.push(['Con', e.participante]);
    if (e.alumno) filas.push(['Alumno/a', e.alumno]);
    if (e.tutor && opts.mostrarTutor) filas.push(['Atiende', e.tutor]);
    if (e.motivo && e.tipo !== 'tutoria') filas.push(['Motivo', e.motivo]);
    if (e.tema) filas.push([e.tipo === 'tutoria' ? 'Quiere ver' : 'Detalle', e.tema]);
    if (opts.contacto && (e.email || e.telefono)) filas.push(['Contacto', [e.email, e.telefono].filter(Boolean).join(' · ')]);
    if (e.reag) filas.push(['Reagendada', e.reag + (e.reag === 1 ? ' vez' : ' veces')]);
    var m = modal('<button type="button" class="cal-x" data-x aria-label="Cerrar">×</button>' +
      '<span class="cal-tag" style="--c:' + t.c + '">' + t.n + '</span> <span class="cal-est">' + esc(ESTADOS[e.estado] || e.estado) + '</span>' +
      '<h2>' + esc(e.titulo || t.n) + '</h2><p class="cal-cuando">' + esc(cuando(e.inicio)) + ' · ' + mins(e) + ' min</p>' +
      filas.map(function (f) { return '<p class="cal-fila"><b>' + esc(f[0]) + ':</b> ' + esc(f[1]) + '</p>'; }).join('') +
      (e.notas && e.estado !== 'reservada' ? '<p class="cal-notas">' + esc(e.notas) + '</p>' : '') +
      '<div id="cal-acc"></div>');
    var acc = m.el.querySelector('#cal-acc');
    m.el.querySelector('[data-x]').onclick = m.cerrar;

    function botones() {
      if (e.estado === 'reservada' && !pasada) {
        acc.innerHTML = '<p class="cal-aviso">Entrá vos primero a la videollamada: hasta que entres, la sala no se abre.</p>' +
          '<div class="cal-acciones"><a class="cal-btn principal" href="' + esc(e.link) + '" target="_blank" rel="noopener">Entrar a la videollamada</a>' +
          '<button type="button" class="cal-btn" data-reag>Reagendar</button><button type="button" class="cal-btn peligro" data-canc>Cancelar</button></div>';
      } else if (e.estado === 'reservada') {
        acc.innerHTML = '<textarea class="cal-ta" placeholder="Notas de la reunión (qué se habló, qué quedó pendiente)"></textarea>' +
          '<div class="cal-acciones"><button type="button" class="cal-btn principal" data-cerrar="realizada">Se hizo</button>' +
          '<button type="button" class="cal-btn" data-cerrar="ausente">No se presentó</button>' +
          '<button type="button" class="cal-btn" data-reag>Reagendar</button></div>';
      } else acc.innerHTML = '';
    }
    botones();

    acc.onclick = async function (ev) {
      var b;
      if (ev.target.closest('[data-reag]')) {
        var base = new Date(e.inicio); if (base < new Date()) base = new Date(Date.now() + 86400000);
        acc.innerHTML = '<label class="cal-lab">Nuevo día y horario<input type="datetime-local" id="cal-nuevo" step="300" value="' + aInput(base) + '"></label>' +
          '<label class="cal-lab">Motivo del cambio (se les avisa)<input type="text" id="cal-motivo" maxlength="300" placeholder="Opcional"></label>' +
          '<p class="cal-err" hidden></p><div class="cal-acciones"><button type="button" class="cal-btn principal" data-conf>Confirmar</button><button type="button" class="cal-btn" data-volver>Volver</button></div>';
      } else if (ev.target.closest('[data-volver]')) {
        botones();
      } else if ((b = ev.target.closest('[data-conf]'))) {
        var v = document.getElementById('cal-nuevo').value, er = acc.querySelector('.cal-err');
        if (!v) { er.textContent = 'Elegí el día y el horario.'; er.hidden = false; return; }
        b.disabled = true;
        var r = await sb.rpc('reagendar_tutoria', { p_id: e.id, p_inicio: new Date(v).toISOString(), p_motivo: document.getElementById('cal-motivo').value || null });
        if (r.error) { er.textContent = r.error.message; er.hidden = false; b.disabled = false; return; }
        toast('Reunión reagendada. Se avisó a las partes.'); m.cerrar(); recargar();
      } else if (ev.target.closest('[data-canc]')) {
        if (!confirm('¿Cancelar esta reunión? Se les avisa a las partes.')) return;
        var x = await sb.rpc('cancelar_tutoria', { p_id: e.id });
        if (x.error) return toast(x.error.message, true);
        toast('Reunión cancelada'); m.cerrar(); recargar();
      } else if ((b = ev.target.closest('[data-cerrar]'))) {
        var y = await sb.rpc('cerrar_tutoria', { p_id: e.id, p_estado: b.getAttribute('data-cerrar'), p_notas: acc.querySelector('.cal-ta') ? acc.querySelector('.cal-ta').value : '' });
        if (y.error) return toast(y.error.message, true);
        toast('Listo'); m.cerrar(); recargar();
      }
    };
  }

  // ---------- Agendar una reunión con una familia (admin) ----------
  async function nuevaReunion(recargar) {
    var m = modal('<button type="button" class="cal-x" data-x aria-label="Cerrar">×</button><h2>Agendar reunión</h2><p class="cal-fila">Cargando familias…</p>');
    m.el.querySelector('[data-x]').onclick = m.cerrar;
    var r = await Promise.all([
      sb.from('families').select('id, profiles!families_profile_id_fkey(full_name, email)').order('created_at', { ascending: false }),
      sb.from('students').select('id, family_id, first_name, last_name').order('first_name')
    ]);
    if (r[0].error || r[1].error) { m.el.innerHTML += '<p class="cal-err">No pudimos cargar las familias.</p>'; return; }
    var fams = r[0].data || [], alus = r[1].data || [];
    var manana = new Date(); manana.setDate(manana.getDate() + 1); manana.setHours(10, 0, 0, 0);
    m.el.innerHTML = '<button type="button" class="cal-x" data-x aria-label="Cerrar">×</button><h2>Agendar reunión</h2>' +
      '<p class="cal-aviso">Sirve para reuniones que arma el equipo: cobranzas, seguimiento o una consulta con dirección. Se les avisa a la familia.</p>' +
      '<form id="cal-form" class="cal-form">' +
      '<label class="cal-lab">Tipo<select name="tipo"><option value="cobranzas">Cobranzas</option><option value="direccion">Dirección</option></select></label>' +
      '<label class="cal-lab">Familia<select name="fam" required><option value="">Elegí una familia…</option>' + fams.map(function (f) {
        var p = f.profiles || {}; return '<option value="' + esc(f.id) + '">' + esc(p.full_name || p.email || 'Sin nombre') + (p.email ? ' · ' + esc(p.email) : '') + '</option>'; }).join('') + '</select></label>' +
      '<label class="cal-lab">Alumno/a <span class="cal-ayuda">(opcional)</span><select name="alu"><option value="">Sobre la familia en general</option></select></label>' +
      '<label class="cal-lab">Día y horario<input type="datetime-local" name="cuando" step="300" required value="' + aInput(manana) + '"></label>' +
      '<label class="cal-lab">Duración<select name="dur"><option value="15">15 min</option><option value="30" selected>30 min</option><option value="45">45 min</option><option value="60">60 min</option></select></label>' +
      '<label class="cal-lab">Motivo<input type="text" name="motivo" maxlength="200" required value="Cobranzas"></label>' +
      '<label class="cal-lab">Detalle <span class="cal-ayuda">(opcional)</span><input type="text" name="tema" maxlength="500"></label>' +
      '<p class="cal-err" hidden></p><div class="cal-acciones"><button type="submit" class="cal-btn principal">Agendar</button></div></form>';
    m.el.querySelector('[data-x]').onclick = m.cerrar;
    var form = document.getElementById('cal-form');
    form.fam.onchange = function () {
      form.alu.innerHTML = '<option value="">Sobre la familia en general</option>' + alus.filter(function (a) { return a.family_id === form.fam.value; })
        .map(function (a) { return '<option value="' + esc(a.id) + '">' + esc(a.first_name + ' ' + a.last_name) + '</option>'; }).join('');
    };
    form.tipo.onchange = function () { form.motivo.value = form.tipo.value === 'cobranzas' ? 'Cobranzas' : 'Consulta con dirección'; };
    form.onsubmit = async function (ev) {
      ev.preventDefault();
      var er = form.querySelector('.cal-err'); er.hidden = true;
      var btn = form.querySelector('button[type="submit"]'); btn.disabled = true;
      var x = await sb.rpc('agendar_reunion_admin', { p_tipo: form.tipo.value, p_family: form.fam.value, p_student: form.alu.value || null,
        p_inicio: new Date(form.cuando.value).toISOString(), p_duracion: +form.dur.value, p_motivo: form.motivo.value, p_tema: form.tema.value || null });
      if (x.error) { er.textContent = x.error.message; er.hidden = false; btn.disabled = false; return; }
      toast('Reunión agendada. Se avisó a la familia.'); m.cerrar(); recargar();
    };
  }

  // ---------- Días sin atención ----------
  async function bloqueos(cont) {
    var ses = await sb.auth.getSession(), yo = ses.data.session.user.id;
    var hoy = new Date().toISOString().slice(0, 10);
    cont.innerHTML = '<section class="cal-bloq"><h2>Días sin atención</h2>' +
      '<p class="cal-ayuda">Vacaciones, feriados o imprevistos: en esos días no se ofrecen turnos nuevos. Si ya tenés reuniones esos días, reagendalas o cancelalas desde el calendario.</p>' +
      '<form id="cal-bloq-form" class="cal-bloq-form"><label>Desde<input type="date" name="d" min="' + hoy + '" required></label><label>Hasta<input type="date" name="h" min="' + hoy + '" required></label>' +
      '<label class="amplio">Motivo<input type="text" name="m" maxlength="100" placeholder="Opcional (feriado, vacaciones…)"></label><button type="submit" class="cal-btn principal">Bloquear</button></form>' +
      '<p class="cal-err" hidden></p><div id="cal-bloq-lista"></div></section>';
    var lista = document.getElementById('cal-bloq-lista'), er = cont.querySelector('.cal-err');
    async function pintar() {
      var r = await sb.from('tutor_bloqueos').select('id, desde, hasta, motivo').eq('tutor_id', yo).gte('hasta', new Date().toISOString()).order('desde');
      if (r.error) { lista.innerHTML = '<p class="cal-ayuda">No pudimos cargar los días bloqueados.</p>'; return; }
      lista.innerHTML = (r.data || []).length ? r.data.map(function (b) {
        var d = new Date(b.desde), h = new Date(b.hasta); h.setDate(h.getDate() - 1);
        var rango = d.toDateString() === h.toDateString() ? d.toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }) :
          d.toLocaleDateString('es-AR', { day: 'numeric', month: 'long' }) + ' al ' + h.toLocaleDateString('es-AR', { day: 'numeric', month: 'long' });
        return '<div class="cal-bloq-item"><span><b>' + esc(rango) + '</b>' + (b.motivo ? ' · ' + esc(b.motivo) : '') + '</span><button type="button" class="cal-btn" data-quitar="' + esc(b.id) + '">Quitar</button></div>';
      }).join('') : '<p class="cal-ayuda">No hay días bloqueados.</p>';
    }
    document.getElementById('cal-bloq-form').onsubmit = async function (ev) {
      ev.preventDefault(); er.hidden = true;
      var f = ev.target, d = new Date(f.d.value + 'T00:00:00'), h = new Date(f.h.value + 'T00:00:00');
      if (h < d) { er.textContent = 'La fecha final no puede ser anterior a la inicial.'; er.hidden = false; return; }
      h.setDate(h.getDate() + 1);
      var r = await sb.from('tutor_bloqueos').insert({ tutor_id: yo, desde: d.toISOString(), hasta: h.toISOString(), motivo: f.m.value || null });
      if (r.error) { er.textContent = 'No se pudo guardar.'; er.hidden = false; return; }
      f.reset(); toast('Días bloqueados'); pintar();
    };
    lista.onclick = async function (ev) {
      var b = ev.target.closest('[data-quitar]'); if (!b) return;
      var r = await sb.from('tutor_bloqueos').delete().eq('id', b.getAttribute('data-quitar'));
      if (r.error) return toast('No se pudo quitar', true);
      pintar();
    };
    pintar();
  }

  // ---------- Reagendar desde la familia (solo entre los turnos libres) ----------
  async function reagendarFamilia(ref, alTerminar) {
    var m = modal('<button type="button" class="cal-x" data-x aria-label="Cerrar">×</button><h2>Reagendar</h2><p class="cal-fila">Buscando turnos libres…</p>');
    m.el.querySelector('[data-x]').onclick = m.cerrar;
    var r = ref.tipo === 'tutoria' ? await sb.rpc('turnos_disponibles', { p_student: ref.student, p_dias: 21 }) : await sb.rpc('turnos_direccion', { p_dias: 21 });
    var slots = r.data || [];
    if (r.error || !slots.length) { m.el.innerHTML = '<button type="button" class="cal-x" data-x>×</button><h2>Reagendar</h2><p class="cal-fila">No hay turnos libres en las próximas 3 semanas. Volvé a mirar en unos días o cancelá este turno para pedir otro más adelante.</p>'; m.el.querySelector('[data-x]').onclick = m.cerrar; return; }
    var porDia = {}, orden = [];
    slots.forEach(function (s) { var k = new Date(s.inicio).toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }); if (!porDia[k]) { porDia[k] = []; orden.push(k); } porDia[k].push(s); });
    m.el.innerHTML = '<button type="button" class="cal-x" data-x aria-label="Cerrar">×</button><h2>Reagendar</h2><p class="cal-fila">Elegí el nuevo día y horario. Solo se puede hasta 12 horas antes y hasta 2 veces por turno.</p>' +
      orden.slice(0, 10).map(function (d) {
        return '<p class="cal-dia-fam">' + esc(d) + '</p><div class="cal-slots">' + porDia[d].map(function (s) { return '<button type="button" class="cal-slot" data-ini="' + esc(s.inicio) + '">' + hh(s.inicio) + '</button>'; }).join('') + '</div>';
      }).join('') + '<p class="cal-err" hidden></p><div class="cal-acciones"><button type="button" class="cal-btn principal" data-conf disabled>Confirmar</button></div>';
    m.el.querySelector('[data-x]').onclick = m.cerrar;
    var elegido = null;
    m.el.onclick = async function (ev) {
      var s = ev.target.closest('.cal-slot');
      if (s) { m.el.querySelectorAll('.cal-slot').forEach(function (x) { x.classList.toggle('on', x === s); }); elegido = s.getAttribute('data-ini'); m.el.querySelector('[data-conf]').disabled = false; return; }
      var b = ev.target.closest('[data-conf]'); if (!b || !elegido) return;
      b.disabled = true;
      var x = await sb.rpc('reagendar_tutoria', { p_id: ref.id, p_inicio: elegido, p_motivo: null });
      if (x.error) { var er = m.el.querySelector('.cal-err'); er.textContent = x.error.message; er.hidden = false; b.disabled = false; return; }
      toast('Listo, reagendamos tu turno.'); m.cerrar(); if (alTerminar) alTerminar();
    };
  }

  window.WaveCal = { semana: semana, nuevaReunion: nuevaReunion, bloqueos: bloqueos, reagendarFamilia: reagendarFamilia, TIPOS: TIPOS };
})();
