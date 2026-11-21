// Pagos por transferencia (panel de familias): datos para transferir, estado de la cuota y carga de comprobantes.
(function () {
  var sb = Wave.sb;
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function ars(n) { return '$ ' + Number(n || 0).toLocaleString('es-AR', { maximumFractionDigits: 0 }); }
  function mes(p) { var d = new Date(p + 'T12:00:00'); var t = d.toLocaleDateString('es-AR', { month: 'long', year: 'numeric' }); return t.charAt(0).toUpperCase() + t.slice(1); }
  var ESTADOS = {
    al_dia: ['Al día', 'ok', 'Tu cuota de este mes está paga. ¡Gracias!'],
    en_plazo: ['En plazo', 'plazo', 'Podés pagar hasta el día 10.'],
    en_revision: ['Comprobante en revisión', 'plazo', 'Recibimos tu comprobante y lo estamos revisando.'],
    atrasado: ['Atrasado', 'atraso', 'El plazo de pago era del 1 al 10. Cargá tu comprobante apenas puedas.'],
    adelantado: ['Adelantado', 'plazo', ''],
    sin_cuota: ['Sin cuota asignada', 'plazo', 'Todavía no tenemos una cuota cargada para tu familia.']
  };
  var PAGO = { pendiente: ['En revisión', 'plazo'], aprobado: ['Confirmado', 'ok'], rechazado: ['Rechazado', 'atraso'] };

  function mesesOpciones() {
    var a = [], h = new Date(); h.setDate(1);
    for (var i = 0; i < 3; i++) { var d = new Date(h.getFullYear(), h.getMonth() - i, 1); a.push(d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-01'); }
    return a;
  }

  async function vista(cont) {
    cont.innerHTML = '<h1 class="vista-titulo">Pagos</h1><div class="vacio">Cargando…</div>';
    var ses = await sb.auth.getSession();
    var res = await Promise.all([
      sb.rpc('mi_cuota'), sb.rpc('datos_transferencia'),
      sb.from('families').select('id').eq('profile_id', ses.data.session.user.id).maybeSingle(),
      sb.from('pagos_transferencia').select('id, periodo, monto, estado, nota_tesoreria, created_at').order('created_at', { ascending: false }).limit(24)
    ]);
    var q = (res[0].data || [])[0] || {}, d = res[1].data || {}, fam = res[2].data, hist = res[3].data || [];
    if (res[0].error || !fam) { cont.innerHTML = '<h1 class="vista-titulo">Pagos</h1><div class="vacio">No pudimos cargar tus pagos. Probá de nuevo en un rato.</div>'; return; }
    var e = ESTADOS[q.estado] || ESTADOS.sin_cuota, falta = Math.max(0, Number(q.cuota || 0) - Number(q.aprobado || 0));
    var hay = d && (d.cbu || d.alias);
    var datos = hay ? '<div class="pf-datos">' + [['Banco', d.banco], ['Titular', d.titular], ['CUIT/CUIL', d.cuit], ['CBU/CVU', d.cbu], ['Alias', d.alias]].filter(function (x) { return x[1]; }).map(function (x) {
      return '<div class="pf-dato"><small>' + x[0] + '</small><b>' + esc(x[1]) + '</b>' + (x[0] === 'CBU/CVU' || x[0] === 'Alias' ? '<button type="button" class="pf-copiar" data-copiar="' + esc(x[1]) + '">Copiar</button>' : '') + '</div>';
    }).join('') + '</div>' + (d.nota ? '<p class="fa-aviso">' + esc(d.nota) + '</p>' : '') : '<p class="fa-aviso">Todavía no cargamos los datos para transferir. Te avisamos apenas estén.</p>';

    cont.innerHTML = '<h1 class="vista-titulo">Pagos</h1>' +
      '<p class="fa-intro">La cuota se paga por transferencia, del <b>1 al 10 de cada mes</b>. Después de transferir, subí acá el comprobante.</p>' +
      '<section class="fa-card pf-estado"><div><small>' + esc(mes(q.periodo)) + '</small><h2>' + ars(q.cuota) + '</h2><p>' + (q.alumnos || 0) + (q.alumnos === 1 ? ' alumno/a' : ' alumnos/as') + '</p></div>' +
      '<div class="pf-sello ' + e[1] + '">' + e[0] + '</div></section>' +
      (e[2] ? '<p class="fa-aviso ' + (e[1] === 'atraso' ? 'atraso' : '') + '">' + e[2] + (falta > 0 && q.estado !== 'sin_cuota' && q.aprobado > 0 ? ' Falta ' + ars(falta) + '.' : '') + '</p>' : '') +
      '<h3 class="fa-sub">Datos para transferir</h3>' + datos +
      '<h3 class="fa-sub">Subir comprobante</h3>' +
      '<form id="pf-form" class="pf-form"><label>Mes que pagás<select name="per">' + mesesOpciones().map(function (m) { return '<option value="' + m + '">' + esc(mes(m)) + '</option>'; }).join('') + '</select></label>' +
      '<label>Monto transferido ($)<input name="monto" type="number" min="1" step="0.01" required value="' + (falta > 0 ? Math.round(falta) : '') + '"></label>' +
      '<label>Comprobante (foto o PDF, hasta 6 MB)<input name="arch" type="file" accept="image/*,application/pdf" required></label>' +
      '<label>Nota <span class="fa-aviso" style="margin:0">(opcional)</span><input name="nota" type="text" maxlength="300"></label>' +
      '<p class="fa-aviso atraso" id="pf-err" hidden></p><button class="boton" type="submit">Enviar comprobante</button></form>' +
      '<h3 class="fa-sub">Mis comprobantes</h3>' + (hist.length ? '<ul class="fa-hist">' + hist.map(function (p) {
        var s = PAGO[p.estado] || ['—', 'plazo'];
        return '<li><div><b>' + esc(mes(p.periodo)) + '</b> · ' + ars(p.monto) + '<br><small>Enviado el ' + new Date(p.created_at).toLocaleDateString('es-AR') + (p.nota_tesoreria ? ' · ' + esc(p.nota_tesoreria) : '') + '</small></div><span class="pf-sello chico ' + s[1] + '">' + s[0] + '</span></li>';
      }).join('') + '</ul>' : '<p class="fa-sin-pagos">Todavía no cargaste comprobantes.</p>');

    cont.onclick = function (ev) {
      var b = ev.target.closest('[data-copiar]'); if (!b) return;
      var v = b.getAttribute('data-copiar');
      (navigator.clipboard ? navigator.clipboard.writeText(v) : Promise.reject()).then(function () { b.textContent = '¡Copiado!'; }, function () { b.textContent = v; });
      setTimeout(function () { b.textContent = 'Copiar'; }, 2000);
    };
    document.getElementById('pf-form').onsubmit = async function (ev) {
      ev.preventDefault();
      var f = ev.target, er = document.getElementById('pf-err'), btn = f.querySelector('button'), file = f.arch.files[0];
      er.hidden = true;
      if (!file) return;
      if (file.size > 6 * 1024 * 1024) { er.textContent = 'El archivo pesa más de 6 MB.'; er.hidden = false; return; }
      btn.disabled = true; btn.textContent = 'Enviando…';
      var ext = (file.name.split('.').pop() || 'jpg').toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 5);
      var path = fam.id + '/' + f.per.value + '-' + Date.now() + '.' + ext;
      var up = await sb.storage.from('comprobantes').upload(path, file, { contentType: file.type });
      var r = up.error ? up : await sb.rpc('registrar_pago_transferencia', { p_periodo: f.per.value, p_monto: +f.monto.value, p_path: path, p_nota: f.nota.value || null });
      if (r.error) { er.textContent = up.error ? 'No se pudo subir el archivo. Probá de nuevo.' : r.error.message; er.hidden = false; btn.disabled = false; btn.textContent = 'Enviar comprobante'; return; }
      vista(cont);
    };
  }
  window.WavePagos = { vista: vista };
})();
