// Pestaña "Juana" del panel de la familia: informes semanales de seguimiento de cada estudiante.
(function () {
  var sb = Wave.sb;
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function dia(v) { return new Date(v + 'T12:00:00').toLocaleDateString('es-AR', { day: 'numeric', month: 'long' }); }

  async function vista(cont) {
    cont.innerHTML = '<h1 class="vista-titulo">Juana</h1><p class="fa-intro">Juana es quien acompaña el seguimiento de cada estudiante. Cada domingo a la noche prepara un informe breve con lo que avanzó, lo que mejor le fue y lo que le costó.</p><div id="ju-lista"><div class="vacio">Cargando…</div></div>';
    var r = await sb.from('seguimiento_informes').select('id,student_id,semana,texto,datos,leido_at,students(first_name,apodo)').order('semana', { ascending: false }).limit(40);
    var lista = document.getElementById('ju-lista');
    if (r.error) { lista.innerHTML = '<div class="vacio">No pudimos cargar los informes. Probá de nuevo en un rato.</div>'; return; }
    var inf = r.data || [];
    if (!inf.length) { lista.innerHTML = '<div class="vacio">Todavía no hay informes. El primero llega el próximo domingo a la noche.</div>'; return; }
    lista.innerHTML = inf.map(function (i, n) {
      var a = Array.isArray(i.students) ? i.students[0] : i.students, nombre = a ? (a.apodo || a.first_name) : 'Estudiante', d = i.datos || {};
      var chips = i.datos && !d.sin_actividad ? '<div class="ju-chips"><span>' + (d.lecciones_completadas || 0) + ' lecciones</span><span>' + (d.dias_activos || 0) + ' días activo</span>' + (d.promedio_actividades != null ? '<span>Promedio ' + esc(d.promedio_actividades) + '</span>' : '') + '</div>' : '';
      return '<section class="fa-card ju-informe' + (i.leido_at ? '' : ' nuevo') + '" data-id="' + esc(i.id) + '"><div class="pg-cab"><b>' + esc(nombre) + '</b> · semana del ' + esc(dia(d.desde || i.semana)) + ' al ' + esc(dia(d.hasta || i.semana)) + (i.leido_at ? '' : ' <span class="ju-nuevo">Nuevo</span>') + '</div>' + chips +
        '<p class="ju-texto">' + esc(i.texto || '').replace(/\n+/g, '<br>') + '</p></section>';
    }).join('');
    var sin = inf.filter(function (i) { return !i.leido_at; }).map(function (i) { return i.id; });
    if (sin.length) sb.from('seguimiento_informes').update({ leido_at: new Date().toISOString() }).in('id', sin).then(function () {});
  }
  // ---------- Chat con Juana ----------
  function hora(v) { var d = new Date(v); return d.toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · ' + d.toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + ' h'; }
  async function chat(cont) {
    var al = await sb.from('students').select('id,first_name,apodo').order('created_at');
    var alumnos = al.data || [];
    if (!alumnos.length) return;
    cont.innerHTML = '<h2 class="wv-sub" style="margin:0 0 6px">Conversá con Juana</h2><p class="fa-aviso" style="margin:0 0 10px">Juana responde con los datos reales del seguimiento. Si no tiene un dato, te lo dice.</p>' +
      (alumnos.length > 1 ? '<label class="ju-sel">Sobre quién querés consultar <select id="ju-alu">' + alumnos.map(function (a) { return '<option value="' + esc(a.id) + '">' + esc(a.apodo || a.first_name) + '</option>'; }).join('') + '</select></label>' : '') +
      '<div class="ju-msgs" id="ju-msgs"></div>' +
      '<div class="ju-botones"><button type="button" class="fa-link" data-acc="informe">¿Cómo le fue esta semana?</button><button type="button" class="fa-link" data-acc="costo">¿Qué le cuesta más?</button><button type="button" class="fa-link" data-acc="reunion">Pedir reunión con Dirección</button></div>' +
      '<form class="ju-form" id="ju-form"><input id="ju-in" type="text" maxlength="1000" placeholder="Escribile a Juana…" autocomplete="off"><button class="boton" type="submit">Enviar</button></form><p class="fa-aviso atraso" id="ju-err" hidden></p>';
    var cajaM = document.getElementById('ju-msgs'), err = document.getElementById('ju-err'), sel = document.getElementById('ju-alu'), ocupado = false;
    function alumno() { return sel ? sel.value : alumnos[0].id; }
    function globo(rol, texto) { var g = document.createElement('div'); g.className = 'ju-msg ' + rol; g.innerHTML = esc(texto).replace(/\n/g, '<br>'); cajaM.appendChild(g); cajaM.scrollTop = cajaM.scrollHeight; return g; }
    async function historial() {
      cajaM.innerHTML = '';
      var h = await sb.from('seguimiento_chat').select('role,content').eq('student_id', alumno()).order('created_at', { ascending: false }).limit(20);
      var l = (h.data || []).reverse();
      if (!l.length) globo('assistant', 'Hola, soy Juana. Te cuento cómo le va, qué le cuesta y te ayudo a pedir una reunión con Dirección. ¿Qué querés saber?');
      l.forEach(function (m) { globo(m.role, m.content); });
    }
    function pintarTurnos(g, turnos) {
      var w = document.createElement('div'); w.className = 'ju-turnos';
      turnos.forEach(function (t) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'fa-link'; b.textContent = hora(t.inicio);
        b.onclick = async function () { w.remove(); await enviar({ reservar_inicio: t.inicio }, 'Elegí: ' + hora(t.inicio)); };
        w.appendChild(b);
      });
      g.appendChild(w);
    }
    async function enviar(cuerpo, etiqueta) {
      if (ocupado) return; ocupado = true; err.hidden = true;
      if (etiqueta) globo('user', etiqueta);
      var p = globo('assistant', 'Juana está escribiendo…');
      var x = await sb.functions.invoke('seguimiento', { body: Object.assign({ action: 'chat', student_id: alumno() }, cuerpo) });
      ocupado = false;
      var d = x.data;
      if (x.error || !d || d.error) {
        p.remove(); var m = d && d.error; if (!m && x.error && x.error.context && x.error.context.json) { try { m = (await x.error.context.json()).error; } catch (e) {} }
        err.textContent = m || 'Juana no pudo responder ahora. Probá de nuevo en un momento.'; err.hidden = false; return;
      }
      p.innerHTML = esc(d.reply).replace(/\n/g, '<br>');
      if (d.turnos && d.turnos.length) pintarTurnos(p, d.turnos);
      if (d.reservada && window.WaveCal && WaveCal.refrescar) WaveCal.refrescar();
      cajaM.scrollTop = cajaM.scrollHeight;
    }
    cont.querySelectorAll('[data-acc]').forEach(function (b) { b.onclick = function () { enviar({ accion: b.getAttribute('data-acc') }, b.textContent); }; });
    document.getElementById('ju-form').onsubmit = function (ev) { ev.preventDefault(); var i = document.getElementById('ju-in'), t = i.value.trim(); if (!t) return; i.value = ''; enviar({ message: t }, t); };
    if (sel) sel.onchange = historial;
    historial();
  }

  window.WaveJuana = { vista: async function (cont) {
    await vista(cont);
    var c = document.createElement('section'); c.className = 'fa-card ju-chat'; cont.insertBefore(c, cont.querySelector('#ju-lista'));
    chat(c);
  } };
})();
