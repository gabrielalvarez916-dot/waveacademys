// Entrevista de admisión: se reserva sin cuenta. Quien reserva guarda un link para cambiarla o cancelarla.
(function () {
  var cfg = window.WAVE_CONFIG;
  var sb = window.supabase.createClient(cfg.SUPABASE_URL, cfg.SUPABASE_KEY, { auth: { persistSession: false, autoRefreshToken: false, detectSessionInUrl: false } });
  var main = document.getElementById('ag-main');
  var WSP = '5493447519836';
  var TZ_LOCAL = (function () { try { return Intl.DateTimeFormat().resolvedOptions().timeZone; } catch (e) { return ''; } })();
  var TZ_AR = 'America/Argentina/Buenos_Aires';
  var params = new URLSearchParams(location.search);
  var estado = { slots: [], dia: null, elegido: null, modo: 'reservar', reserva: null };

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function wsp(msg) { return 'https://wa.me/' + WSP + '?text=' + encodeURIComponent(msg); }
  function fmt(iso, tz, opts) { return new Date(iso).toLocaleString('es-AR', Object.assign({ timeZone: tz || undefined }, opts)); }
  function diaLargo(iso, tz) { return fmt(iso, tz, { weekday: 'long', day: 'numeric', month: 'long' }); }
  function hora(iso, tz) { return fmt(iso, tz, { hour: '2-digit', minute: '2-digit', hour12: false }) + ' h'; }
  function claveDia(iso) { var d = new Date(iso); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  function cuando(iso) {
    var s = diaLargo(iso) + ', ' + hora(iso);
    var ar = diaLargo(iso, TZ_AR) + ', ' + hora(iso, TZ_AR);
    return s + (ar !== s ? ' (en tu zona horaria; en Argentina: ' + hora(iso, TZ_AR) + ')' : '');
  }
  function mensaje(t, cuerpo) { main.innerHTML = '<div class="ag-card"><h1 class="ag-titulo">' + t + '</h1>' + cuerpo + '</div>'; }
  function guardarLocal(r) { try { localStorage.setItem('wave_entrevista', JSON.stringify(r)); } catch (e) { /* sin almacenamiento */ } }

  // ---------- Selector de día y horario ----------
  function pickerHtml() {
    var porDia = {}, orden = [];
    estado.slots.forEach(function (s) { var k = claveDia(s.inicio); if (!porDia[k]) { porDia[k] = []; orden.push(k); } porDia[k].push(s); });
    if (!estado.dia || !porDia[estado.dia]) estado.dia = orden[0];
    var dias = '<div class="ag-dias" role="tablist" aria-label="Día">' + orden.map(function (k) {
      var d = new Date(porDia[k][0].inicio);
      return '<button type="button" class="ag-dia' + (k === estado.dia ? ' on' : '') + '" data-dia="' + k + '" role="tab" aria-selected="' + (k === estado.dia) + '"><small>' +
        esc(d.toLocaleDateString('es-AR', { weekday: 'short' }).replace('.', '')) + '</small><b>' + d.getDate() + '</b><small>' + esc(d.toLocaleDateString('es-AR', { month: 'short' }).replace('.', '')) + '</small></button>';
    }).join('') + '</div>';
    var horas = '<div class="ag-horas">' + porDia[estado.dia].map(function (s) {
      return '<button type="button" class="ag-hora' + (s.inicio === estado.elegido ? ' on' : '') + '" data-ini="' + esc(s.inicio) + '">' + esc(hora(s.inicio)) + '</button>';
    }).join('') + '</div>';
    var min = Math.round((new Date(estado.slots[0].fin) - new Date(estado.slots[0].inicio)) / 60000);
    return '<h2 class="ag-sub">1. Elegí el día</h2>' + dias + '<h2 class="ag-sub">2. Elegí el horario <span class="ag-ayuda">(duración: ' + min + ' min' + (TZ_LOCAL ? ' · tu zona horaria: ' + esc(TZ_LOCAL.replace(/_/g, ' ')) : '') + ')</span></h2>' + horas +
      (estado.elegido ? '<p class="ag-elegido"><b>Elegiste:</b> ' + esc(cuando(estado.elegido)) + '</p>' : '');
  }

  async function cargarSlots() {
    var r = await sb.rpc('admision_turnos', { p_dias: 28 });
    if (r.error) throw r.error;
    estado.slots = r.data || [];
  }
  function sinHorarios() {
    mensaje('Por ahora no hay horarios libres',
      '<p class="ag-intro">Estamos completos en los próximos días. Escribinos por WhatsApp y coordinamos un horario con vos.</p>' +
      '<div class="ag-acciones"><a class="btn btn-tur" href="' + wsp('Hola, quiero agendar una entrevista con Wave Academy.') + '" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>');
  }

  // ---------- Reservar ----------
  function vistaReservar() {
    if (!estado.slots.length) return sinHorarios();
    main.innerHTML = '<div class="ag-card"><h1 class="ag-titulo">Agendá tu entrevista</h1>' +
      '<p class="ag-intro">Una videollamada con la dirección de Wave Academy para conocernos, contarte cómo funciona la escuela y charlar sobre tu hijo o hija. No hace falta crear una cuenta.</p>' +
      '<div id="ag-picker">' + pickerHtml() + '</div>' +
      '<h2 class="ag-sub">3. Tus datos</h2>' +
      '<form class="ag-form" id="ag-form" novalidate>' +
        '<label>Tu nombre<input name="nombre" autocomplete="name" maxlength="80" required></label>' +
        '<label>WhatsApp <span class="ag-ayuda">Con código de país y área, por ejemplo 54 9 11 1234 5678</span><input name="tel" type="tel" autocomplete="tel" inputmode="tel" maxlength="25" required></label>' +
        '<label>Correo electrónico<input name="email" type="email" autocomplete="email" maxlength="120" required></label>' +
        '<label>¿Querés contarnos algo? <span class="ag-ayuda">Opcional: la edad de tu hijo o hija, qué estás buscando…</span><textarea name="detalle" maxlength="500"></textarea></label>' +
        '<div class="ag-trampa" aria-hidden="true"><label>No completar<input name="web" tabindex="-1" autocomplete="off"></label></div>' +
        '<p class="ag-err" hidden></p>' +
        '<div class="ag-acciones"><button class="btn btn-tur" type="submit">Confirmar entrevista</button></div></form></div>';
    var picker = document.getElementById('ag-picker'), form = document.getElementById('ag-form'), err = form.querySelector('.ag-err');
    function repintar() { picker.innerHTML = pickerHtml(); }
    picker.onclick = function (ev) {
      var b;
      if ((b = ev.target.closest('[data-dia]'))) { estado.dia = b.getAttribute('data-dia'); estado.elegido = null; repintar(); }
      else if ((b = ev.target.closest('[data-ini]'))) { estado.elegido = b.getAttribute('data-ini'); repintar(); }
    };
    form.onsubmit = async function (ev) {
      ev.preventDefault();
      err.hidden = true;
      var f = new FormData(form);
      if (f.get('web')) return; // trampa para robots
      if (!estado.elegido) { err.textContent = 'Elegí un día y un horario.'; err.hidden = false; return; }
      var btn = form.querySelector('button[type="submit"]'); btn.disabled = true; btn.textContent = 'Reservando…';
      var r = await sb.rpc('reservar_admision', { p_nombre: f.get('nombre'), p_telefono: f.get('tel'), p_email: f.get('email'), p_inicio: estado.elegido, p_detalle: f.get('detalle') || null });
      if (r.error) {
        err.textContent = r.error.message || 'No pudimos reservar. Probá de nuevo o escribinos por WhatsApp.'; err.hidden = false;
        btn.disabled = false; btn.textContent = 'Confirmar entrevista';
        if (/horario|ocupar/i.test(err.textContent)) { await cargarSlots().catch(function () {}); estado.elegido = null; repintar(); }
        return;
      }
      var x = Array.isArray(r.data) ? r.data[0] : r.data;
      guardarLocal({ id: x.id, token: x.token });
      history.replaceState(null, '', '?id=' + x.id + '&t=' + x.token);
      vistaGestion({ id: x.id, token: x.token }, true);
    };
  }

  // ---------- Ver, cambiar o cancelar ----------
  async function vistaGestion(ref, recien) {
    var r = await sb.rpc('admision_ver', { p_id: ref.id, p_token: ref.token });
    var e = r.data && r.data[0];
    if (r.error || !e) return mensaje('No encontramos esa entrevista', '<p class="ag-intro">Revisá que el link esté completo. Si el problema sigue, escribinos por WhatsApp.</p><div class="ag-acciones"><a class="btn btn-tur" href="' + wsp('Hola, necesito ayuda con mi entrevista en Wave Academy.') + '" target="_blank" rel="noopener">Escribir por WhatsApp</a><a class="btn ag-btn-sec" href="/agendar.html">Agendar una nueva</a></div>');
    estado.reserva = ref;
    var gestionUrl = location.origin + '/agendar.html?id=' + encodeURIComponent(ref.id) + '&t=' + encodeURIComponent(ref.token);
    if (e.estado === 'cancelada') {
      return mensaje('Entrevista cancelada', '<p class="ag-intro">Esta entrevista fue cancelada. Si querés, agendá otra.</p><div class="ag-acciones"><a class="btn btn-tur" href="/agendar.html">Agendar otra entrevista</a></div>');
    }
    if (e.estado !== 'reservada') {
      return mensaje('Entrevista finalizada', '<p class="ag-intro">Gracias por conversar con nosotros. Si querés seguir en contacto, escribinos por WhatsApp.</p><div class="ag-acciones"><a class="btn btn-tur" href="' + wsp('Hola, tuve una entrevista con Wave Academy.') + '" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>');
    }
    var pasada = new Date(e.fin).getTime() < Date.now();
    main.innerHTML = '<div class="ag-card">' + (recien ? '<span class="ag-ok">Entrevista confirmada</span>' : '') +
      '<h1 class="ag-titulo">' + (recien ? '¡Listo, ' + esc((e.nombre || '').split(' ')[0]) + '!' : 'Tu entrevista') + '</h1>' +
      '<p class="ag-dato"><b>' + esc(cuando(e.inicio)) + '</b></p>' +
      '<p class="ag-dato">Será por videollamada con la dirección de Wave Academy. El día de la entrevista, entrá desde este mismo link: no hace falta crear una cuenta.</p>' +
      '<div class="ag-acciones"><a class="btn btn-tur" href="' + esc(e.link) + '" target="_blank" rel="noopener">Entrar a la videollamada</a>' +
      '<button class="btn ag-btn-sec" type="button" data-cambiar>Cambiar el horario</button>' +
      '<button class="btn ag-btn-peligro" type="button" data-cancelar>Cancelar</button></div>' +
      '<div class="ag-nota"><b>Guardá este link.</b> Es la única forma de volver a ver, cambiar o cancelar tu entrevista. Todavía no enviamos recordatorios por correo, así que copialo o guardalo en favoritos.' +
      '<div class="ag-link"><input readonly value="' + esc(gestionUrl) + '" aria-label="Link para gestionar tu entrevista"><button class="btn btn-osc" type="button" data-copiar>Copiar</button></div></div>' +
      '<p class="ag-ayuda" style="margin-top:16px">¿Necesitás ayuda? <a href="' + wsp('Hola, tengo una consulta sobre mi entrevista en Wave Academy.') + '" target="_blank" rel="noopener">Escribinos por WhatsApp</a>.</p></div>';
    if (pasada) main.querySelector('.ag-acciones').remove();
    main.onclick = async function (ev) {
      var b;
      if ((b = ev.target.closest('[data-copiar]'))) {
        var inp = main.querySelector('.ag-link input'); inp.select();
        try { await navigator.clipboard.writeText(inp.value); b.textContent = 'Copiado'; } catch (x) { document.execCommand('copy'); b.textContent = 'Copiado'; }
      } else if ((b = ev.target.closest('[data-cancelar]'))) {
        if (!confirm('¿Cancelar la entrevista?')) return;
        var x = await sb.rpc('admision_cancelar', { p_id: ref.id, p_token: ref.token });
        if (x.error) { alert(x.error.message); return; }
        vistaGestion(ref);
      } else if ((b = ev.target.closest('[data-cambiar]'))) {
        vistaCambiar(ref, e);
      }
    };
  }

  async function vistaCambiar(ref, e) {
    try { await cargarSlots(); } catch (x) { alert('No pudimos cargar los horarios.'); return; }
    estado.elegido = null; estado.dia = null;
    if (!estado.slots.length) { alert('No hay horarios libres por ahora. Escribinos por WhatsApp.'); return; }
    main.innerHTML = '<div class="ag-card"><h1 class="ag-titulo">Cambiar el horario</h1>' +
      '<p class="ag-intro">Ahora: <b>' + esc(cuando(e.inicio)) + '</b></p><div id="ag-picker">' + pickerHtml() + '</div><p class="ag-err" hidden></p>' +
      '<div class="ag-acciones"><button class="btn btn-tur" type="button" data-confirmar>Confirmar el nuevo horario</button><button class="btn ag-btn-sec" type="button" data-volver>Volver</button></div></div>';
    var picker = document.getElementById('ag-picker'), err = main.querySelector('.ag-err');
    function repintar() { picker.innerHTML = pickerHtml(); }
    main.onclick = async function (ev) {
      var b;
      if ((b = ev.target.closest('[data-dia]'))) { estado.dia = b.getAttribute('data-dia'); estado.elegido = null; repintar(); }
      else if ((b = ev.target.closest('[data-ini]'))) { estado.elegido = b.getAttribute('data-ini'); repintar(); }
      else if (ev.target.closest('[data-volver]')) { vistaGestion(ref); }
      else if ((b = ev.target.closest('[data-confirmar]'))) {
        if (!estado.elegido) { err.textContent = 'Elegí un día y un horario.'; err.hidden = false; return; }
        b.disabled = true;
        var x = await sb.rpc('admision_reagendar', { p_id: ref.id, p_token: ref.token, p_inicio: estado.elegido });
        if (x.error) { err.textContent = x.error.message; err.hidden = false; b.disabled = false; return; }
        vistaGestion(ref);
      }
    };
  }

  // ---------- Inicio ----------
  (async function () {
    try {
      var id = params.get('id'), t = params.get('t');
      if (id && t) return await vistaGestion({ id: id, token: t });
      await cargarSlots();
      vistaReservar();
    } catch (e) {
      mensaje('No pudimos cargar los horarios', '<p class="ag-intro">Probá de nuevo en un momento o escribinos por WhatsApp.</p><div class="ag-acciones"><a class="btn btn-tur" href="' + wsp('Hola, quiero agendar una entrevista con Wave Academy.') + '" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>');
    }
  })();
})();
