// Panel de Josefina (agente de Admisión) para Administración y Dirección: contactos, conocimiento y consola de prueba.
(function () {
  var sb = Wave.sb;
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  var ESTADOS = { nuevo: 'Nuevo', en_conversacion: 'En conversación', entrevista_agendada: 'Entrevista agendada', derivado_humano: 'Para atender por una persona', cerrado: 'Cerrado' };
  var CANALES = { whatsapp: 'WhatsApp', instagram: 'Instagram', web: 'Web', prueba: 'Prueba' };
  function cuando(v) { return new Date(v).toLocaleString('es-AR', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }); }

  async function vista(cont) {
    cont.innerHTML = '<h1 class="vista-titulo">Josefina · Admisión</h1>' +
      '<p class="wv-dato">Josefina atiende a las familias nuevas por WhatsApp e Instagram (la conexión con esos canales se hace aparte), responde solo con la información cargada acá y con los precios reales, y les agenda la entrevista con Dirección. Si una persona tiene que intervenir, te avisa.</p>' +
      '<div class="wv-tabs" id="ad-tabs"><button class="wv-tab on" data-t="contactos">Contactos</button><button class="wv-tab" data-t="conocimiento">Lo que sabe Josefina</button><button class="wv-tab" data-t="probar">Probar</button></div><div id="ad-cuerpo"></div>';
    var cuerpo = document.getElementById('ad-cuerpo');
    var tabs = { contactos: contactos, conocimiento: conocimiento, probar: probar };
    function ir(t) { document.querySelectorAll('#ad-tabs .wv-tab').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-t') === t); }); tabs[t](cuerpo); }
    document.getElementById('ad-tabs').onclick = function (e) { var b = e.target.closest('[data-t]'); if (b) ir(b.getAttribute('data-t')); };
    ir('contactos');
  }

  // ---------- Contactos ----------
  async function contactos(c) {
    c.innerHTML = '<div class="wv-vacio">Cargando…</div>';
    var r = await sb.from('admision_contactos').select('*').neq('canal', 'prueba').order('ultimo_mensaje_at', { ascending: false }).limit(100);
    if (r.error) { c.innerHTML = '<div class="wv-vacio">' + esc(r.error.message) + '</div>'; return; }
    var l = r.data || [];
    if (!l.length) { c.innerHTML = '<div class="wv-vacio">Todavía no hay conversaciones. Cuando se conecte WhatsApp o Instagram, van a aparecer acá.</div>'; return; }
    c.innerHTML = '<div class="wv-alus">' + l.map(function (x) {
      return '<div class="wv-alu" data-id="' + esc(x.id) + '" style="cursor:pointer"><div><div class="wv-nombre">' + esc(x.nombre || 'Sin nombre') + '</div><div class="wv-dato">' + esc(CANALES[x.canal]) + (x.telefono ? ' · ' + esc(x.telefono) : '') + (x.email ? ' · ' + esc(x.email) : '') + '</div></div>' +
        '<div><span class="wv-rot">' + esc(ESTADOS[x.estado]) + '</span><span class="wv-dato">' + esc(x.interes || '') + '</span></div><div class="wv-dato">' + esc(cuando(x.ultimo_mensaje_at)) + '</div></div>';
    }).join('') + '</div>';
    c.onclick = function (e) { var f = e.target.closest('[data-id]'); if (f) conversacion(c, f.getAttribute('data-id')); };
  }
  async function conversacion(c, id) {
    var res = await Promise.all([sb.from('admision_contactos').select('*').eq('id', id).single(), sb.from('admision_mensajes').select('role,content,created_at').eq('contacto_id', id).order('created_at')]);
    var x = res[0].data, m = res[1].data || [];
    c.onclick = null;
    c.innerHTML = '<button class="wv-btn" id="ad-volver" type="button">← Volver</button><h2 class="wv-sub">' + esc(x.nombre || 'Sin nombre') + ' · ' + esc(CANALES[x.canal]) + '</h2>' +
      '<p class="wv-dato">' + esc([x.telefono, x.email, x.interes].filter(Boolean).join(' · ')) + '</p>' +
      '<label class="wv-dato">Estado <select id="ad-estado">' + Object.keys(ESTADOS).map(function (k) { return '<option value="' + k + '"' + (k === x.estado ? ' selected' : '') + '>' + esc(ESTADOS[k]) + '</option>'; }).join('') + '</select></label> ' +
      '<label class="wv-dato">Notas <input id="ad-notas" type="text" maxlength="300" value="' + esc(x.notas || '') + '" style="min-width:260px"></label> <button class="wv-btn" id="ad-g" type="button">Guardar</button>' +
      '<div class="ju-msgs" style="max-height:none;margin-top:12px">' + m.map(function (k) { return '<div class="ju-msg ' + (k.role === 'user' ? 'assistant' : 'user') + '" title="' + esc(cuando(k.created_at)) + '">' + esc(k.content).replace(/\n/g, '<br>') + '</div>'; }).join('') + '</div>';
    document.getElementById('ad-volver').onclick = function () { contactos(c); };
    document.getElementById('ad-g').onclick = async function () {
      var r = await sb.from('admision_contactos').update({ estado: document.getElementById('ad-estado').value, notas: document.getElementById('ad-notas').value || null }).eq('id', id);
      this.textContent = r.error ? 'Error' : '¡Guardado!';
    };
  }

  // ---------- Conocimiento ----------
  async function conocimiento(c) {
    c.innerHTML = '<div class="wv-vacio">Cargando…</div>';
    var res = await Promise.all([sb.from('admision_conocimiento').select('*').order('orden'), sb.from('app_settings').select('value').eq('key', 'admision').maybeSingle()]);
    var l = res[0].data || [], cfg = (res[1].data && res[1].data.value) || {};
    c.innerHTML = '<p class="wv-dato">Josefina responde <b>solo</b> con lo que está acá y con los precios reales de la plataforma (se actualizan solos). Si algo no está cargado, dice que se ve en la entrevista. Lo que se marque como inactivo no lo usa.</p>' +
      '<label class="wv-dato">Dirección web de la escuela (para los links de cambiar o cancelar la entrevista) <input id="ad-web" type="url" placeholder="https://…" value="' + esc(cfg.web_url || '') + '" style="min-width:280px"></label> <button class="wv-btn" id="ad-webg" type="button">Guardar</button>' +
      '<div id="ad-lista">' + l.map(fila).join('') + '</div><button class="wv-btn" id="ad-nuevo" type="button" style="margin-top:14px">+ Agregar un tema</button>';
    function fila(k) {
      return '<section class="fa-card" data-k="' + esc(k.id) + '" style="margin-top:12px"><input class="ad-tema" type="text" maxlength="80" value="' + esc(k.tema) + '" style="font-weight:700;width:100%;margin-bottom:6px">' +
        '<textarea class="ad-cont" rows="6" style="width:100%">' + esc(k.contenido) + '</textarea><label class="wv-dato"><input class="ad-act" type="checkbox"' + (k.activo ? ' checked' : '') + '> Activo</label> ' +
        '<button class="wv-btn" data-g type="button">Guardar</button> <button class="fa-link" data-b type="button">Borrar</button></section>';
    }
    c.onclick = async function (e) {
      if (e.target.id === 'ad-webg') { var w = document.getElementById('ad-web').value.trim(); var r0 = await sb.from('app_settings').upsert({ key: 'admision', value: Object.assign({}, cfg, { web_url: w }), updated_at: new Date().toISOString() }); e.target.textContent = r0.error ? 'Error' : '¡Guardado!'; return; }
      if (e.target.id === 'ad-nuevo') { var r1 = await sb.from('admision_conocimiento').insert({ tema: 'Nuevo tema', contenido: 'Escribí acá la información.', orden: 500 }); if (!r1.error) conocimiento(c); return; }
      var s = e.target.closest('[data-k]'); if (!s) return; var id = s.getAttribute('data-k');
      if (e.target.hasAttribute('data-g')) {
        var r = await sb.from('admision_conocimiento').update({ tema: s.querySelector('.ad-tema').value, contenido: s.querySelector('.ad-cont').value, activo: s.querySelector('.ad-act').checked, updated_at: new Date().toISOString() }).eq('id', id);
        e.target.textContent = r.error ? 'Error' : '¡Guardado!';
      } else if (e.target.hasAttribute('data-b')) { if (confirm('¿Borrar este tema?')) { await sb.from('admision_conocimiento').delete().eq('id', id); conocimiento(c); } }
    };
  }

  // ---------- Consola de prueba (no reserva nada de verdad) ----------
  function probar(c) {
    var sesion = String(Date.now());
    c.innerHTML = '<p class="wv-dato">Escribile como si fueras una familia. Es una prueba: no reserva entrevistas ni avisa a nadie, <b>pero cada mensaje usa la IA y tiene un costo mínimo</b>.</p><div class="ju-msgs" id="ad-msgs" style="min-height:180px"></div>' +
      '<form class="ju-form" id="ad-form"><input id="ad-in" type="text" maxlength="1000" placeholder="Escribile a Josefina…" autocomplete="off"><button class="boton" type="submit">Enviar</button></form><p class="fa-aviso atraso" id="ad-err" hidden></p>';
    var caja = document.getElementById('ad-msgs'), ocupado = false;
    function globo(rol, t) { var g = document.createElement('div'); g.className = 'ju-msg ' + rol; g.innerHTML = esc(t).replace(/\n/g, '<br>'); caja.appendChild(g); caja.scrollTop = caja.scrollHeight; return g; }
    document.getElementById('ad-form').onsubmit = async function (ev) {
      ev.preventDefault(); if (ocupado) return; var i = document.getElementById('ad-in'), t = i.value.trim(); if (!t) return; i.value = ''; ocupado = true;
      var er = document.getElementById('ad-err'); er.hidden = true; globo('user', t); var p = globo('assistant', 'Josefina está escribiendo…');
      var x = await sb.functions.invoke('admision', { body: { action: 'probar', sesion: sesion, mensaje: t } }); ocupado = false;
      if (x.error || !x.data || x.data.error) { p.remove(); er.textContent = (x.data && x.data.error) || 'Josefina no pudo responder ahora.'; er.hidden = false; return; }
      p.innerHTML = esc(x.data.reply).replace(/\n/g, '<br>');
    };
  }
  window.WaveAdmision = { vista: vista };
})();
