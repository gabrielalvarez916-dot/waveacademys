// Panel de Tesorería: cuotas por transferencia, comprobantes, ingresos y gastos, altas y datos de transferencia.
(function () {
  var sb = Wave.sb;
  var vista = document.getElementById('vista');
  var enlaces = document.querySelectorAll('.nav-tes a');

  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function ars(n) { return '$ ' + Number(n || 0).toLocaleString('es-AR', { maximumFractionDigits: 0 }); }
  function toast(t, err) { var e = document.createElement('div'); e.className = 'te-toast' + (err ? ' err' : ''); e.textContent = t; document.body.appendChild(e); setTimeout(function () { e.remove(); }, 3500); }
  function iso(d) { return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-01'; }
  function mesTxt(d) { var t = d.toLocaleDateString('es-AR', { month: 'long', year: 'numeric' }); return t.charAt(0).toUpperCase() + t.slice(1); }
  function fecha(v) { return new Date(v).toLocaleDateString('es-AR', { day: 'numeric', month: 'short', year: 'numeric' }); }
  function soloNum(t) { return String(t || '').replace(/\D/g, ''); }
  var ESTADO = { al_dia: 'Al día', en_plazo: 'En plazo', en_revision: 'En revisión', atrasado: 'Atrasado', adelantado: 'Adelantado', sin_cuota: 'Sin cuota' };
  function sello(e, t) { return '<span class="te-sello ' + e + '">' + esc(t || ESTADO[e] || e) + '</span>'; }

  // ---------- Cuotas ----------
  var mesActual = new Date(); mesActual.setDate(1); mesActual.setHours(12, 0, 0, 0);
  async function vistaCuotas() {
    vista.innerHTML = '<h1 class="vista-titulo">Cuotas</h1>' +
      '<p class="te-nota">Se paga del 1 al 10 de cada mes. Pasado el 10, quien no tiene el pago confirmado figura como atrasada.</p>' +
      '<div class="te-barra"><button class="te-btn" data-mes="-1" aria-label="Mes anterior">‹</button><button class="te-btn" data-mes="0">Este mes</button><button class="te-btn" data-mes="1" aria-label="Mes siguiente">›</button>' +
      '<div class="te-mes">' + esc(mesTxt(mesActual)) + '</div></div><div id="te-cuotas"><div class="te-vacio">Cargando…</div></div>';
    var r = await sb.rpc('tesoreria_cuotas', { p_periodo: iso(mesActual) });
    var c = document.getElementById('te-cuotas');
    if (r.error) { c.innerHTML = '<div class="te-vacio">' + esc(r.error.message) + '</div>'; return; }
    var f = r.data || [], esperado = 0, cobrado = 0, atras = 0, rev = 0;
    f.forEach(function (x) { esperado += +x.cuota; cobrado += Math.min(+x.aprobado, +x.cuota); if (x.estado === 'atrasado') atras++; rev += x.en_revision; });
    c.innerHTML = '<div class="te-kpis">' + [['A cobrar', ars(esperado), ''], ['Cobrado', ars(cobrado), 'pos'], ['Falta cobrar', ars(Math.max(0, esperado - cobrado)), esperado > cobrado ? 'neg' : ''], ['Familias atrasadas', atras, atras ? 'neg' : ''], ['Comprobantes por revisar', rev, '']]
      .map(function (k) { return '<div class="te-kpi"><small>' + k[0] + '</small><b class="' + k[2] + '">' + k[1] + '</b></div>'; }).join('') + '</div>' +
      (f.length ? '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Familia</th><th>Contacto</th><th class="num">Alumnos</th><th class="num">Cuota</th><th class="num">Pagado</th><th>Estado</th><th></th></tr></thead><tbody>' + f.map(function (x) {
        var tel = soloNum(x.telefono), msg = 'Hola ' + (x.familia || '') + ', te escribimos de Wave Academy. Te recordamos que la cuota de ' + mesTxt(mesActual) + ' se paga del 1 al 10 de cada mes. Si ya transferiste, subí el comprobante en la plataforma. ¡Gracias!';
        return '<tr><td><b>' + esc(x.familia) + '</b></td><td>' + esc(x.email || '') + '<br><small>' + esc(x.telefono || 'sin WhatsApp') + '</small></td><td class="num">' + x.alumnos + '</td><td class="num">' + ars(x.cuota) + '</td><td class="num">' + ars(x.aprobado) + '</td><td>' + sello(x.estado) + '</td>' +
          '<td>' + (tel && (x.estado === 'atrasado' || x.estado === 'en_plazo') ? '<a class="te-btn" target="_blank" rel="noopener" href="https://wa.me/' + tel + '?text=' + encodeURIComponent(msg) + '">Recordar por WhatsApp</a>' : '') + '</td></tr>';
      }).join('') + '</tbody></table></div>' : '<div class="te-vacio">Todavía no hay familias con alumnos.</div>');
  }

  // ---------- Comprobantes ----------
  var filtroComp = 'pendiente';
  async function vistaComprobantes() {
    vista.innerHTML = '<h1 class="vista-titulo">Comprobantes</h1><div class="te-barra"><button class="te-btn' + (filtroComp === 'pendiente' ? ' principal' : '') + '" data-filtro="pendiente">Por revisar</button>' +
      '<button class="te-btn' + (filtroComp === '' ? ' principal' : '') + '" data-filtro="">Todos</button></div><div id="te-comp"><div class="te-vacio">Cargando…</div></div>';
    var r = await sb.rpc('tesoreria_comprobantes', { p_estado: filtroComp || null });
    var c = document.getElementById('te-comp');
    if (r.error) { c.innerHTML = '<div class="te-vacio">' + esc(r.error.message) + '</div>'; return; }
    c.innerHTML = (r.data || []).length ? r.data.map(function (p) {
      return '<div class="te-card"><div><h3>' + esc(p.familia) + ' · ' + ars(p.monto) + '</h3><p>Cuota de ' + esc(mesTxt(new Date(p.periodo + 'T12:00:00'))) + ' · enviado el ' + fecha(p.created_at) + '</p>' +
        (p.nota_familia ? '<p>Nota de la familia: ' + esc(p.nota_familia) + '</p>' : '') + (p.nota_tesoreria ? '<p>Tesorería: ' + esc(p.nota_tesoreria) + '</p>' : '') + '</div>' +
        '<div class="te-acc">' + sello(p.estado, { pendiente: 'Por revisar', aprobado: 'Aprobado', rechazado: 'Rechazado' }[p.estado]) +
        '<button class="te-btn" data-ver="' + esc(p.comprobante_path) + '">Ver comprobante</button>' +
        (p.estado === 'pendiente' ? '<button class="te-btn principal" data-aprobar="' + p.id + '">Aprobar</button><button class="te-btn peligro" data-rechazar="' + p.id + '">Rechazar</button>' : '') + '</div></div>';
    }).join('') : '<div class="te-vacio">' + (filtroComp ? 'No hay comprobantes por revisar.' : 'Todavía no hay comprobantes.') + '</div>';
  }

  // ---------- Ingresos y gastos ----------
  var PRESETS = [['Supabase', 'Plataforma', 'Supabase'], ['Vercel', 'Plataforma', 'Vercel'], ['Claude (suscripción)', 'IA', 'Anthropic'], ['API de Claude', 'IA', 'Anthropic'], ['Monotributo', 'Impuestos', 'AFIP/ARCA'], ['Publicidad en Meta', 'Publicidad', 'Meta'], ['Honorarios tutores', 'Personal', '']];
  var CATS = ['Plataforma', 'IA', 'Impuestos', 'Publicidad', 'Personal', 'Comisiones de cobro', 'Otro'];
  async function vistaFinanzas() {
    vista.innerHTML = '<h1 class="vista-titulo">Ingresos y gastos</h1><div class="te-vacio">Cargando…</div>';
    var hoy = new Date(), desde = new Date(hoy.getFullYear(), hoy.getMonth() - 5, 1);
    var res = await Promise.all([sb.rpc('tesoreria_ingresos', { p_desde: iso(desde) }), sb.from('gastos').select('*').order('created_at', { ascending: false }), sb.from('app_settings').select('value').eq('key', 'dolar').maybeSingle()]);
    if (res[0].error || res[1].error) { vista.innerHTML = '<h1 class="vista-titulo">Ingresos y gastos</h1><div class="te-vacio">No pudimos cargar los datos.</div>'; return; }
    var ing = res[0].data || [], gas = res[1].data || [], usd = res[2].data && res[2].data.value ? +res[2].data.value.ars_por_usd : 0;
    function aArs(g) { return g.moneda === 'USD' ? g.monto * usd : +g.monto; }
    var meses = []; for (var i = 5; i >= 0; i--) meses.push(new Date(hoy.getFullYear(), hoy.getMonth() - i, 1));
    var filas = meses.map(function (m) {
      var ini = m, fin = new Date(m.getFullYear(), m.getMonth() + 1, 0, 23, 59, 59);
      var i1 = 0; ing.forEach(function (x) { var d = new Date(x.fecha); if (d >= ini && d <= fin) i1 += +x.monto_ars; });
      var g1 = 0; gas.forEach(function (g) {
        var d0 = new Date(g.desde + 'T00:00:00'), d1 = g.hasta ? new Date(g.hasta + 'T23:59:59') : null;
        if (g.frecuencia === 'unico') { if (d0 >= ini && d0 <= fin) g1 += aArs(g); }
        else if (d0 <= fin && (!d1 || d1 >= ini)) g1 += aArs(g) / (g.frecuencia === 'anual' ? 12 : 1);
      });
      return { m: m, i: i1, g: g1 };
    });
    var tI = 0, tG = 0; filas.forEach(function (f) { tI += f.i; tG += f.g; });
    var fijoMes = 0; gas.forEach(function (g) { if (g.frecuencia !== 'unico' && (!g.hasta || new Date(g.hasta) >= hoy)) fijoMes += aArs(g) / (g.frecuencia === 'anual' ? 12 : 1); });
    vista.innerHTML = '<h1 class="vista-titulo">Ingresos y gastos</h1>' +
      '<div class="te-kpis">' + [['Ingresos (6 meses)', ars(tI), 'pos'], ['Gastos (6 meses)', ars(tG), ''], ['Resultado (6 meses)', ars(tI - tG), tI - tG >= 0 ? 'pos' : 'neg'], ['Gasto fijo mensual', ars(fijoMes), '']]
        .map(function (k) { return '<div class="te-kpi"><small>' + k[0] + '</small><b class="' + k[2] + '">' + k[1] + '</b></div>'; }).join('') + '</div>' +
      '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Mes</th><th class="num">Ingresos</th><th class="num">Gastos</th><th class="num">Resultado</th></tr></thead><tbody>' + filas.map(function (f) {
        return '<tr><td>' + esc(mesTxt(f.m)) + '</td><td class="num">' + ars(f.i) + '</td><td class="num">' + ars(f.g) + '</td><td class="num"><b style="color:' + (f.i - f.g >= 0 ? '#14663A' : '#A12C1F') + '">' + ars(f.i - f.g) + '</b></td></tr>';
      }).join('') + '</tbody></table></div>' +
      '<p class="te-nota">Ingresos: transferencias confirmadas, Mercado Pago/PayPal y matrículas. Los gastos en USD se pasan a pesos con el dólar cargado en la plataforma' + (usd ? ' (' + ars(usd) + ')' : ' (todavía no hay dólar cargado)') + '. Los gastos anuales se reparten en 12 meses.</p>' +
      '<h2 class="te-sub">Cargar un gasto</h2><div class="te-presets">' + PRESETS.map(function (p, i) { return '<button type="button" class="te-btn" data-preset="' + i + '">' + esc(p[0]) + '</button>'; }).join('') + '</div>' +
      '<form id="te-gasto" class="te-form"><label>Concepto<input name="concepto" required maxlength="100"></label><label>Categoría<select name="cat">' + CATS.map(function (c) { return '<option>' + c + '</option>'; }).join('') + '</select></label>' +
      '<label>Proveedor<input name="prov" maxlength="80"></label><label>Monto<input name="monto" type="number" min="0" step="0.01" required></label><label>Moneda<select name="mon"><option>ARS</option><option>USD</option></select></label>' +
      '<label>Frecuencia<select name="frec"><option value="mensual">Todos los meses</option><option value="anual">Una vez al año</option><option value="unico">Una sola vez</option></select></label>' +
      '<label>Desde<input name="desde" type="date" required value="' + hoy.toISOString().slice(0, 10) + '"></label><label>Hasta (opcional)<input name="hasta" type="date"></label>' +
      '<label>Nota<input name="nota" maxlength="200"></label><button class="te-btn principal" type="submit">Guardar gasto</button></form><p class="te-err" id="te-gerr" hidden></p>' +
      '<h2 class="te-sub">Gastos cargados</h2>' + (gas.length ? '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Concepto</th><th>Categoría</th><th>Frecuencia</th><th class="num">Monto</th><th>Vigencia</th><th></th></tr></thead><tbody>' + gas.map(function (g) {
        return '<tr><td><b>' + esc(g.concepto) + '</b>' + (g.proveedor ? '<br><small>' + esc(g.proveedor) + '</small>' : '') + '</td><td>' + esc(g.categoria) + '</td><td>' + { mensual: 'Mensual', anual: 'Anual', unico: 'Único' }[g.frecuencia] + '</td><td class="num">' + (g.moneda === 'USD' ? 'US$ ' + Number(g.monto).toLocaleString('es-AR') : ars(g.monto)) + '</td><td>' + fecha(g.desde + 'T12:00:00') + (g.hasta ? ' → ' + fecha(g.hasta + 'T12:00:00') : g.frecuencia === 'unico' ? '' : ' → sigue') + '</td>' +
          '<td>' + (g.frecuencia !== 'unico' && !g.hasta ? '<button class="te-btn" data-cerrar-gasto="' + g.id + '">Dar de baja</button> ' : '') + '<button class="te-btn peligro" data-borrar-gasto="' + g.id + '">Borrar</button></td></tr>';
      }).join('') + '</tbody></table></div>' : '<div class="te-vacio">Todavía no cargaste gastos.</div>') +
      '<h2 class="te-sub">Últimos ingresos</h2>' + (ing.length ? '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Fecha</th><th>Familia</th><th>Origen</th><th>Detalle</th><th class="num">Monto</th></tr></thead><tbody>' + ing.slice(0, 40).map(function (x) {
        return '<tr><td>' + fecha(x.fecha) + '</td><td>' + esc(x.familia) + '</td><td>' + esc(x.origen) + '</td><td>' + esc(x.detalle) + '</td><td class="num">' + ars(x.monto_ars) + '</td></tr>';
      }).join('') + '</tbody></table></div>' : '<div class="te-vacio">Todavía no hay ingresos registrados.</div>');
    var form = document.getElementById('te-gasto');
    vista.onclick = async function (ev) {
      var b;
      if ((b = ev.target.closest('[data-preset]'))) { var p = PRESETS[+b.getAttribute('data-preset')]; form.concepto.value = p[0]; form.cat.value = p[1]; form.prov.value = p[2]; form.monto.focus(); }
      else if ((b = ev.target.closest('[data-borrar-gasto]'))) { if (!confirm('¿Borrar este gasto? Desaparece de todos los meses.')) return; var r = await sb.from('gastos').delete().eq('id', b.getAttribute('data-borrar-gasto')); if (r.error) toast('No se pudo borrar', true); else vistaFinanzas(); }
      else if ((b = ev.target.closest('[data-cerrar-gasto]'))) { var r2 = await sb.from('gastos').update({ hasta: new Date().toISOString().slice(0, 10) }).eq('id', b.getAttribute('data-cerrar-gasto')); if (r2.error) toast('No se pudo dar de baja', true); else vistaFinanzas(); }
    };
    form.onsubmit = async function (ev) {
      ev.preventDefault(); var er = document.getElementById('te-gerr'); er.hidden = true;
      var r = await sb.from('gastos').insert({ concepto: form.concepto.value.trim(), categoria: form.cat.value, proveedor: form.prov.value.trim() || null, monto: +form.monto.value, moneda: form.mon.value, frecuencia: form.frec.value, desde: form.desde.value, hasta: form.hasta.value || null, nota: form.nota.value.trim() || null });
      if (r.error) { er.textContent = 'No se pudo guardar el gasto.'; er.hidden = false; return; }
      toast('Gasto guardado'); vistaFinanzas();
    };
  }

  // ---------- Altas ----------
  async function vistaAltas() {
    vista.innerHTML = '<h1 class="vista-titulo">Altas recientes</h1><p class="te-nota">Alumnos que se sumaron en los últimos 90 días, con su cuota y el estado de la matrícula.</p><div id="te-altas"><div class="te-vacio">Cargando…</div></div>';
    var r = await sb.rpc('tesoreria_altas', { p_dias: 90 }), c = document.getElementById('te-altas');
    if (r.error) { c.innerHTML = '<div class="te-vacio">' + esc(r.error.message) + '</div>'; return; }
    c.innerHTML = (r.data || []).length ? '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Alumno/a</th><th>Familia</th><th>Contacto</th><th>Nivel</th><th class="num">Cuota</th><th>Matrícula</th><th>Alta</th></tr></thead><tbody>' + r.data.map(function (a) {
      return '<tr><td><b>' + esc(a.alumno) + '</b></td><td>' + esc(a.familia) + '</td><td>' + esc(a.email || '') + '<br><small>' + esc(a.telefono || 'sin WhatsApp') + '</small></td><td>' + esc(a.nivel || '—') + '</td><td class="num">' + (+a.cuota ? ars(a.cuota) : '—') + '</td><td>' + esc(a.matricula) + '</td><td>' + fecha(a.alta) + '</td></tr>';
    }).join('') + '</tbody></table></div>' : '<div class="te-vacio">No hay altas en los últimos 90 días.</div>';
  }

  // ---------- Datos de transferencia ----------
  async function vistaTransferencia() {
    var r = await sb.rpc('datos_transferencia'), d = r.data || {};
    vista.innerHTML = '<h1 class="vista-titulo">Datos de transferencia</h1><p class="te-nota">Esto es lo que ven las familias en su sección Pagos.</p>' +
      '<form id="te-tf" class="te-form una"><label>Banco o billetera<input name="banco" maxlength="80" value="' + esc(d.banco) + '"></label><label>Titular de la cuenta<input name="titular" maxlength="120" value="' + esc(d.titular) + '"></label>' +
      '<label>CUIT/CUIL<input name="cuit" maxlength="20" value="' + esc(d.cuit) + '"></label><label>CBU/CVU<input name="cbu" maxlength="30" value="' + esc(d.cbu) + '"></label><label>Alias<input name="alias" maxlength="40" value="' + esc(d.alias) + '"></label>' +
      '<label>Nota para las familias (opcional)<input name="nota" maxlength="300" value="' + esc(d.nota) + '" placeholder="Ej: poné el apellido de la familia en el concepto"></label><button class="te-btn principal" type="submit">Guardar</button></form>';
    document.getElementById('te-tf').onsubmit = async function (ev) {
      ev.preventDefault(); var f = ev.target, x = await sb.rpc('guardar_datos_transferencia', { p: { banco: f.banco.value, titular: f.titular.value, cuit: f.cuit.value, cbu: f.cbu.value, alias: f.alias.value, nota: f.nota.value } });
      toast(x.error ? 'No se pudo guardar' : 'Datos guardados', !!x.error);
    };
  }

  // ---------- Acciones y navegación ----------
  document.addEventListener('click', async function (ev) {
    var b;
    if ((b = ev.target.closest('[data-mes]'))) { var n = +b.getAttribute('data-mes'); if (n === 0) { mesActual = new Date(); mesActual.setDate(1); mesActual.setHours(12, 0, 0, 0); } else mesActual = new Date(mesActual.getFullYear(), mesActual.getMonth() + n, 1, 12); vistaCuotas(); }
    else if ((b = ev.target.closest('[data-filtro]'))) { filtroComp = b.getAttribute('data-filtro'); vistaComprobantes(); }
    else if ((b = ev.target.closest('[data-ver]'))) {
      var w = window.open('', '_blank'); var s = await sb.storage.from('comprobantes').createSignedUrl(b.getAttribute('data-ver'), 300);
      if (s.error) { if (w) w.close(); toast('No se pudo abrir el comprobante', true); } else if (w) w.location = s.data.signedUrl;
    }
    else if ((b = ev.target.closest('[data-aprobar]'))) { b.disabled = true; var r = await sb.rpc('revisar_pago', { p_id: b.getAttribute('data-aprobar'), p_estado: 'aprobado', p_nota: null }); if (r.error) toast(r.error.message, true); else toast('Pago aprobado. Se avisó a la familia.'); vistaComprobantes(); }
    else if ((b = ev.target.closest('[data-rechazar]'))) {
      var motivo = prompt('Motivo del rechazo (se lo mostramos a la familia):'); if (motivo === null) return;
      var r2 = await sb.rpc('revisar_pago', { p_id: b.getAttribute('data-rechazar'), p_estado: 'rechazado', p_nota: motivo }); if (r2.error) toast(r2.error.message, true); else toast('Comprobante rechazado. Se avisó a la familia.'); vistaComprobantes();
    }
  });

  var VISTAS = { cuotas: vistaCuotas, comprobantes: vistaComprobantes, finanzas: vistaFinanzas, altas: vistaAltas, transferencia: vistaTransferencia };
  function ruta() {
    var h = (location.hash || '#cuotas').slice(1); if (!VISTAS[h]) h = 'cuotas';
    enlaces.forEach(function (a) { a.classList.toggle('activo', a.getAttribute('href') === '#' + h); });
    vista.onclick = null; VISTAS[h]();
  }
  window.addEventListener('hashchange', ruta);
  ruta();
})();
