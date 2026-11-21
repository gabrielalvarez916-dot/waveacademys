// Tutor IA del alumno: un solo panel que se monta en cada pantalla de la misión (PDF, clase, actividad, práctica).
// El contexto (qué está mirando) lo da cada pantalla; el servidor solo lee esa misión.
(function () {
  var BOTONES = {
    pdf: [['consigna', 'No entiendo la consigna'], ['simple', 'Explicámelo más simple'], ['ejemplo', 'Un ejemplo de la vida real'], ['visual', 'Mostrámelo con un dibujo'], ['resumen', 'Resumime esto'], ['tutoria', 'Pedir tutoría individual']],
    clase: [['simple', 'No entendí esta parte'], ['ejemplo', 'Un ejemplo de la vida real'], ['visual', 'Mostrámelo con un dibujo'], ['resumen', 'Resumime la clase'], ['tutoria', 'Pedir tutoría individual']],
    actividad: [['consigna', 'No entiendo la consigna'], ['pista', 'Dame una pista'], ['paso', 'Un ejemplo guiado'], ['otra_forma', 'Otra forma de hacerlo'], ['concreto', 'Con objetos de casa'], ['tutoria', 'Pedir tutoría individual']]
  };
  BOTONES.practica = BOTONES.actividad;
  var PERSONALIDADES = [['calido', 'Cálido'], ['divertido', 'Divertido'], ['calmado', 'Calmado'], ['curioso', 'Curioso'], ['motivador', 'Motivador']];

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function cuando(iso) {
    try { return new Date(iso).toLocaleString('es-AR', { weekday: 'short', day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit', timeZone: 'America/Argentina/Buenos_Aires' }); } catch (e) { return iso; }
  }

  // op: { contenedor, pantalla, enviar(payload)->Promise, ctx()->{...}, sid, config:{ver(),guardar(apodo,tutor,pers)} }
  function montar(op) {
    var cont = op.contenedor, conv = null, enviando = false, nombreTutor = 'Tutor Wave';
    var botones = BOTONES[op.pantalla] || BOTONES.pdf;
    cont.innerHTML =
      '<div class="wvp-chat-msgs" aria-live="polite"><div class="wvp-m bot wt-saludo">¡Hola! Soy tu tutor. Tocá un botón o escribime lo que no te quede claro de esta misión.</div></div>' +
      '<div class="wt-botones">' + botones.map(function (b) { return '<button type="button" class="wt-b" data-a="' + b[0] + '">' + esc(b[1]) + '</button>'; }).join('') + '</div>' +
      '<div class="wvp-chat-rest" hidden></div>' +
      '<button type="button" class="wt-cfg-abrir">⚙ Mi tutor: ponele nombre y personalidad</button>' +
      '<div class="wt-cfg" hidden>' +
        '<label>¿Cómo te llamo?<input class="wt-apodo" maxlength="30" placeholder="Tu apodo"></label>' +
        '<label>Nombre de tu tutor<input class="wt-tnombre" maxlength="30" placeholder="Por ejemplo: Nova"></label>' +
        '<label>Personalidad<select class="wt-pers">' + PERSONALIDADES.map(function (p) { return '<option value="' + p[0] + '">' + p[1] + '</option>'; }).join('') + '</select></label>' +
        '<div class="wt-cfg-acc"><button type="button" class="wt-b wt-guardar">Guardar</button><button type="button" class="wt-b wt-cancelar">Cancelar</button></div>' +
      '</div>' +
      '<form class="wvp-chat-form"><textarea rows="1" maxlength="1500" placeholder="Escribí tu duda…" aria-label="Tu duda"></textarea>' +
        '<button type="submit" class="wvp-b wvp-env" aria-label="Enviar">➤</button></form>';

    var msgs = cont.querySelector('.wvp-chat-msgs'), form = cont.querySelector('.wvp-chat-form'), campo = form.querySelector('textarea');
    var envBtn = form.querySelector('.wvp-env'), rest = cont.querySelector('.wvp-chat-rest'), cfg = cont.querySelector('.wt-cfg');

    function agregar(clase, texto) { var d = document.createElement('div'); d.className = 'wvp-m ' + clase; d.textContent = texto; msgs.appendChild(d); msgs.scrollTop = msgs.scrollHeight; return d; }
    function bloquear(b) { enviando = b; envBtn.disabled = b; Array.prototype.forEach.call(cont.querySelectorAll('.wt-b[data-a]'), function (x) { x.disabled = b; }); }

    function pintarTurnos(globo, turnos, area) {
      var w = document.createElement('div'); w.className = 'wt-turnos';
      turnos.forEach(function (t) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'wt-b wt-turno'; b.textContent = cuando(t.inicio);
        b.onclick = async function () {
          w.querySelectorAll('button').forEach(function (x) { x.disabled = true; });
          try { var r = await op.enviar({ reservar_inicio: t.inicio, area: area, tema: 'Consulta desde el tutor' }); agregar('bot', r.reply); w.remove(); }
          catch (e) { agregar('bot error', e.message || 'No se pudo agendar.'); w.querySelectorAll('button').forEach(function (x) { x.disabled = false; }); }
        };
        w.appendChild(b);
      });
      globo.appendChild(w);
    }

    function pintarAreas(globo, areas, sugerida) {
      var w = document.createElement('div'); w.className = 'wt-turnos';
      areas.forEach(function (a) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'wt-b wt-turno'; b.textContent = a.nombre + (a.id === sugerida ? ' (la de esta misión)' : '');
        b.onclick = function () { w.remove(); consultar('', 'tutoria', 'Tutoría de ' + a.nombre, { area: a.id }); };
        w.appendChild(b);
      });
      globo.appendChild(w);
    }

    async function consultar(texto, accion, etiqueta, extra) {
      if (enviando) return;
      if (!texto && !accion) return;
      bloquear(true);
      agregar('yo', texto || etiqueta);
      campo.value = ''; campo.style.height = 'auto';
      var pensando = agregar('bot pensando', 'Pensando…');
      try {
        var payload = Object.assign({ pantalla: op.pantalla, conversation_id: conv || undefined }, op.ctx ? op.ctx() : {}, { message: texto || '', accion: accion || undefined }, extra || {});
        var r = await op.enviar(payload);
        conv = r.conversation_id || conv;
        pensando.className = 'wvp-m bot'; pensando.textContent = r.reply;
        if (r.areas && r.areas.length) pintarAreas(pensando, r.areas, r.area_sugerida);
        else if (r.turnos && r.turnos.length) pintarTurnos(pensando, r.turnos, r.area);
        else if (r.ofrecer_tutoria) {
          var o = document.createElement('button'); o.type = 'button'; o.className = 'wt-b wt-ofrecer'; o.textContent = 'Pedir una tutoría individual';
          o.onclick = function () { o.remove(); consultar('', 'tutoria', 'Pedir una tutoría individual'); };
          pensando.appendChild(o);
        }
        if (typeof r.remaining === 'number') { rest.hidden = false; rest.textContent = r.remaining > 0 ? 'Te quedan ' + r.remaining + ' consultas hoy' : 'Esta fue tu última consulta de hoy'; }
      } catch (e) { pensando.className = 'wvp-m bot error'; pensando.textContent = e.message || 'El tutor no pudo responder ahora.'; }
      msgs.scrollTop = msgs.scrollHeight;
      bloquear(false);
    }

    campo.addEventListener('input', function () { campo.style.height = 'auto'; campo.style.height = Math.min(campo.scrollHeight, 120) + 'px'; });
    campo.addEventListener('keydown', function (ev) { if (ev.key === 'Enter' && !ev.shiftKey) { ev.preventDefault(); form.requestSubmit(); } ev.stopPropagation(); });
    form.addEventListener('submit', function (ev) { ev.preventDefault(); consultar(campo.value.trim(), null); });
    cont.addEventListener('click', function (ev) {
      var b = ev.target.closest('.wt-b[data-a]');
      if (b) consultar('', b.getAttribute('data-a'), b.textContent);
    });

    // ----- Nombre del tutor, personalidad y apodo -----
    var abrirCfg = cont.querySelector('.wt-cfg-abrir');
    if (!op.config) { abrirCfg.hidden = true; }
    else {
      op.config.ver().then(function (c) {
        if (!c) return;
        cont.querySelector('.wt-apodo').value = c.apodo || '';
        cont.querySelector('.wt-tnombre').value = c.tutor_nombre || '';
        if (c.tutor_personalidad) cont.querySelector('.wt-pers').value = c.tutor_personalidad;
        if (c.tutor_nombre) { nombreTutor = c.tutor_nombre; abrirCfg.textContent = '⚙ Cambiar nombre o personalidad de ' + nombreTutor; msgs.querySelector('.wt-saludo').textContent = '¡Hola' + (c.apodo ? ' ' + c.apodo : '') + '! Soy ' + nombreTutor + '. Tocá un botón o escribime lo que no te quede claro de esta misión.'; }
      }).catch(function () {});
      abrirCfg.onclick = function () { cfg.hidden = !cfg.hidden; };
      cont.querySelector('.wt-cancelar').onclick = function () { cfg.hidden = true; };
      cont.querySelector('.wt-guardar').onclick = async function () {
        try {
          await op.config.guardar(cont.querySelector('.wt-apodo').value, cont.querySelector('.wt-tnombre').value, cont.querySelector('.wt-pers').value);
          cfg.hidden = true; agregar('bot', 'Listo, guardado. Desde ahora me vas a ver con ese nombre y personalidad.');
        } catch (e) { agregar('bot error', e.message || 'No se pudo guardar.'); }
      };
    }
    return { enfocar: function () { campo.focus(); } };
  }

  // Botón flotante + panel para pantallas que no son el PDF (clase, actividad, práctica)
  function flotante(el, op) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'wt-flot'; b.textContent = '💬 Tutor'; b.setAttribute('aria-label', 'Abrir el tutor');
    var p = document.createElement('aside'); p.className = 'wt-panel'; p.hidden = true;
    p.innerHTML = '<div class="wvp-chat-cab"><b>💬 Tutor Wave</b><small>Preguntale lo que no entiendas de esta misión</small><button type="button" class="wvp-chat-x" aria-label="Cerrar el tutor">✕</button></div><div class="wt-cuerpo"></div>';
    el.appendChild(b); el.appendChild(p);
    var montado = null;
    function alternar() {
      p.hidden = !p.hidden;
      if (!p.hidden && !montado) { op.contenedor = p.querySelector('.wt-cuerpo'); montado = montar(op); }
      if (!p.hidden && montado) montado.enfocar();
    }
    b.onclick = alternar;
    p.querySelector('.wvp-chat-x').onclick = alternar;
  }

  window.WaveTutor = { montar: montar, flotante: flotante };
})();
