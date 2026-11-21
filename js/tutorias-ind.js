// Panel de familias: tutorías individuales (pagas). Las pide el alumno desde el tutor del chat; acá la familia las paga.
// Argentina: transferencia + comprobante (lo aprueba Tesorería). Otros países: PayPal (se confirma sola).
(function () {
  var sb = Wave.sb;
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function ars(n) { return '$ ' + Number(n || 0).toLocaleString('es-AR', { maximumFractionDigits: 0 }); }
  function usd(n) { return 'US$ ' + Number(n || 0).toLocaleString('es-AR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  function fecha(v) {
    var d = new Date(v);
    return d.toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · ' + d.toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + ' h';
  }
  function vence(v) {
    var d = new Date(v); return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'long' }) + ' a las ' + d.toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + ' h';
  }
  var AREAS = { exactas: 'Exactas y Tecnología', humanidades: 'Humanidades', ingles: 'Inglés', creatividad: 'Creatividad y Vida' };

  async function pintar(cont, extranjera) {
    cont.innerHTML = '<h2>Tutorías individuales</h2><div class="vacio">Cargando…</div>';
    var ses = await sb.auth.getSession();
    var res = await Promise.all([
      sb.rpc('mis_tutorias_individuales'), sb.rpc('tutoria_individual_config'), sb.rpc('datos_transferencia'),
      sb.from('families').select('id').eq('profile_id', ses.data.session.user.id).maybeSingle()
    ]);
    var lista = res[0].data || [], cfg = res[1].data || {}, d = res[2].data || {}, fam = res[3].data;
    if (res[0].error || !fam) { cont.innerHTML = '<h2>Tutorías individuales</h2><div class="vacio">No pudimos cargarlas. Probá de nuevo en un rato.</div>'; return; }
    var recargo = 1 + (Number(cfg.recargo_pct || 5) / 100), precioUsd = Math.round(Number(cfg.precio_usd || 0) * recargo * 100) / 100;
    var datos = (d.cbu || d.alias) ? '<div class="pf-datos">' + [['Banco', d.banco], ['Titular', d.titular], ['CBU/CVU', d.cbu], ['Alias', d.alias]].filter(function (x) { return x[1]; })
      .map(function (x) { return '<div class="pf-dato"><small>' + x[0] + '</small><b>' + esc(x[1]) + '</b></div>'; }).join('') + '</div>' : '<p class="fa-aviso">Todavía no cargamos los datos para transferir.</p>';

    cont.innerHTML = '<h2>Tutorías individuales</h2>' +
      '<p class="fa-intro">Son clases uno a uno con un tutor del área que elija el estudiante. ' + (cfg.precio_ars ? 'Cada una cuesta <b>' + (extranjera ? usd(precioUsd) : ars(cfg.precio_ars)) + '</b>' + (extranjera ? ' <small>(incluye el 5% de la comisión de PayPal)</small>' : '') + '. ' : '') +
      'El estudiante las pide desde el tutor, dentro de la misión. El horario queda reservado ' + (cfg.horas_para_pagar || 48) + ' horas: si no se paga en ese plazo, se libera.</p>' +
      (lista.length ? lista.map(function (t) {
        var h = '<div class="tuf-turno" data-tut="' + esc(t.id) + '"><b>' + esc(fecha(t.inicio)) + '</b> · ' + esc(t.alumno) + ' · ' + esc(AREAS[t.area] || t.area);
        if (t.estado === 'reservada') return h + '<br><small>✓ Confirmada' + (t.tutor ? ' · con ' + esc(t.tutor) : '') + '</small>' + (t.link ? ' <a class="boton" href="' + esc(t.link) + '" target="_blank" rel="noopener">Entrar</a>' : '') + '</div>';
        if (t.estado === 'realizada') return h + '<br><small>Realizada</small></div>';
        if (t.estado === 'ausente') return h + '<br><small>No se presentó</small></div>';
        // pendiente_pago
        var pie = '<br><small class="atraso">Esperando el pago · se libera el ' + esc(vence(t.vence_pago_at)) + '</small>';
        if (t.pago_estado === 'pendiente') return h + '<br><small>Comprobante en revisión. Apenas Tesorería lo apruebe, queda confirmada.</small></div>';
        if (extranjera) return h + pie + '<div style="margin-top:8px"><button type="button" class="boton" data-paypal="' + esc(t.id) + '">Pagar ' + esc(usd(precioUsd)) + ' con PayPal</button> <button type="button" class="fa-link" data-cancelar="' + esc(t.id) + '">Cancelar</button><p class="fa-aviso atraso" hidden data-err></p></div></div>';
        return h + pie + '<details style="margin-top:8px"><summary><b>Pagar ' + esc(ars(t.precio_ars)) + ' por transferencia</b></summary>' + datos +
          '<form class="pf-form" data-pagar="' + esc(t.id) + '"><label>Comprobante (foto, captura o PDF, hasta 6 MB)<input name="arch" type="file" accept="image/*,application/pdf" required></label>' +
          '<label>Nota <span class="fa-aviso" style="margin:0">(opcional)</span><input name="nota" type="text" maxlength="300"></label>' +
          '<p class="fa-aviso atraso" hidden data-err></p><button class="boton" type="submit">Enviar comprobante</button></form>' +
          '<button type="button" class="fa-link" data-cancelar="' + esc(t.id) + '">Cancelar esta tutoría</button></details></div>';
      }).join('') : '<p class="fa-sin-pagos">Todavía no hay tutorías individuales pedidas.</p>');

    cont.onclick = async function (ev) {
      var pp = ev.target.closest('[data-paypal]'), ca = ev.target.closest('[data-cancelar]');
      if (pp) {
        var er = pp.parentNode.querySelector('[data-err]'); er.hidden = true; pp.disabled = true; var txt = pp.textContent; pp.textContent = 'Preparando el pago…';
        var x = await sb.functions.invoke('paypal', { body: { action: 'tutoria', tutoria_id: pp.getAttribute('data-paypal') } });
        if (x.error || !x.data || x.data.error || !x.data.url) {
          er.textContent = (x.data && x.data.error) || 'No se pudo preparar el pago. Probá de nuevo en un rato.'; er.hidden = false; pp.disabled = false; pp.textContent = txt; return;
        }
        window.location.href = x.data.url;
      } else if (ca) {
        if (!confirm('¿Cancelar esta tutoría? El horario se libera.')) return;
        var r = await sb.rpc('cancelar_tutoria', { p_id: ca.getAttribute('data-cancelar') });
        if (r.error) { alert(r.error.message); return; }
        pintar(cont, extranjera);
      }
    };
    cont.onsubmit = async function (ev) {
      var f = ev.target; if (!f.getAttribute('data-pagar')) return;
      ev.preventDefault();
      var er = f.querySelector('[data-err]'), btn = f.querySelector('button[type=submit]'), file = f.arch.files[0], txt = btn.textContent; er.hidden = true;
      if (!file) return;
      if (file.size > 6 * 1024 * 1024) { er.textContent = 'El archivo pesa más de 6 MB.'; er.hidden = false; return; }
      btn.disabled = true; btn.textContent = 'Enviando…';
      var ext = (file.name.split('.').pop() || 'jpg').toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 5);
      var path = fam.id + '/tutoria-' + f.getAttribute('data-pagar') + '-' + Date.now() + '.' + ext;
      var up = await sb.storage.from('comprobantes').upload(path, file, { contentType: file.type });
      var r = up.error ? up : await sb.rpc('registrar_pago_tutoria', { p_tutoria: f.getAttribute('data-pagar'), p_path: path, p_nota: f.nota.value || null });
      if (r.error) { er.textContent = up.error ? 'No se pudo subir el archivo. Probá de nuevo.' : r.error.message; er.hidden = false; btn.disabled = false; btn.textContent = txt; return; }
      pintar(cont, extranjera);
    };
  }
  window.WaveTutInd = { pintar: pintar };
})();
