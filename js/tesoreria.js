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
  var ESTADO = { bloqueado: 'Bloqueado', al_dia: 'Al día', en_plazo: 'En plazo', en_revision: 'En revisión', atrasado: 'Atrasado', adelantado: 'Adelantado', sin_cuota: 'Sin cuota' };
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
      return '<div class="te-card"><div><h3>' + esc(p.familia) + ' · ' + ars(p.monto) + '</h3><p>' + (p.tipo === 'matricula' ? 'Matrícula anual · ' + esc(p.alumnos || '') : 'Cuota de ' + esc(mesTxt(new Date(p.periodo + 'T12:00:00')))) + ' · enviado el ' + fecha(p.created_at) + '</p>' +
        (p.nota_familia ? '<p>Nota de la familia: ' + esc(p.nota_familia) + '</p>' : '') + (p.nota_tesoreria ? '<p>Tesorería: ' + esc(p.nota_tesoreria) + '</p>' : '') + '</div>' +
        '<div class="te-acc">' + sello(p.estado, { pendiente: 'Por revisar', aprobado: 'Aprobado', rechazado: 'Rechazado' }[p.estado]) +
        '<button class="te-btn" data-ver="' + esc(p.comprobante_path) + '">Ver comprobante</button>' +
        (p.estado === 'aprobado' ? (p.factura_id ? '<button class="te-btn" data-factura="' + p.factura_id + '">Ver factura</button>' : '<button class="te-btn principal" data-facturar="' + p.id + '">Generar factura</button>') : '') +
        (p.estado === 'pendiente' ? '<button class="te-btn principal" data-aprobar="' + p.id + '">Aprobar</button><button class="te-btn peligro" data-rechazar="' + p.id + '">Rechazar</button>' : '') + '</div></div>';
    }).join('') : '<div class="te-vacio">' + (filtroComp ? 'No hay comprobantes por revisar.' : 'Todavía no hay comprobantes.') + '</div>';
  }

  // ---------- Ingresos y gastos ----------
  var PRESETS = [['Supabase', 'Plataforma', 'Supabase'], ['Vercel', 'Plataforma', 'Vercel'], ['Claude (suscripción)', 'IA', 'Anthropic'], ['API de Claude', 'IA', 'Anthropic'], ['Monotributo', 'Impuestos', 'AFIP/ARCA'], ['Publicidad en Meta', 'Publicidad', 'Meta'], ['Honorarios tutores', 'Personal', ''], ['Inscripción anual en Royal Hollow (por alumno)', 'Inscripción', 'Royal Hollow', true]];
  var CATS0 = null;
  var CATS = ['Plataforma', 'IA', 'Impuestos', 'Publicidad', 'Personal', 'Inscripción', 'Comisiones de cobro', 'Otro'];
  function gastoMes(g, m, altas, usd) {
    var ini = m, fin = new Date(m.getFullYear(), m.getMonth() + 1, 0, 23, 59, 59);
    var base = g.moneda === 'USD' ? g.monto * usd : +g.monto, d0 = new Date(g.desde + 'T00:00:00'), d1 = g.hasta ? new Date(g.hasta + 'T23:59:59') : null;
    var mult = 1;
    if (g.por_alumno && g.frecuencia === 'anual') { // una vez por año por cada alumno: en el mes de su alta y en cada aniversario
      var n = altas.filter(function (a) { return a <= fin && a.getMonth() === m.getMonth(); }).length;
      return d0 <= fin && (!d1 || d1 >= ini) ? base * n : 0;
    }
    if (g.por_alumno) mult = altas.filter(function (a) { return g.frecuencia === 'unico' ? (a >= ini && a <= fin) : a <= fin; }).length;
    if (g.frecuencia === 'unico') return d0 >= ini && d0 <= fin && !g.por_alumno ? base : g.por_alumno && d0 <= fin ? base * mult : 0;
    return d0 <= fin && (!d1 || d1 >= ini) ? base * mult / (g.frecuencia === 'anual' ? 12 : 1) : 0;
  }
  async function vistaFinanzas() {
    vista.innerHTML = '<h1 class="vista-titulo">Ingresos y gastos</h1><div class="te-vacio">Cargando…</div>';
    var hoy = new Date(), desde = new Date(hoy.getFullYear(), hoy.getMonth() - 5, 1);
    var res = await Promise.all([sb.rpc('tesoreria_ingresos', { p_desde: iso(desde) }), sb.from('gastos').select('*').order('created_at', { ascending: false }), sb.from('app_settings').select('value').eq('key', 'dolar').maybeSingle(), sb.rpc('tesoreria_alumnos_alta')]);
    if (res[0].error || res[1].error) { vista.innerHTML = '<h1 class="vista-titulo">Ingresos y gastos</h1><div class="te-vacio">No pudimos cargar los datos.</div>'; return; }
    var altas = (res[3].data || []).map(function (a) { return new Date(a.alta); }), ing = res[0].data || [], gas = res[1].data || [], usd = res[2].data && res[2].data.value ? +res[2].data.value.ars_por_usd : 0;
    var meses = []; for (var i = 5; i >= 0; i--) meses.push(new Date(hoy.getFullYear(), hoy.getMonth() - i, 1));
    var filas = meses.map(function (m) {
      var ini = m, fin = new Date(m.getFullYear(), m.getMonth() + 1, 0, 23, 59, 59);
      var i1 = 0; ing.forEach(function (x) { var d = new Date(x.fecha); if (d >= ini && d <= fin) i1 += +x.monto_ars; });
      var g1 = 0; gas.forEach(function (g) { g1 += gastoMes(g, m, altas, usd); });
      return { m: m, i: i1, g: g1 };
    });
    var tI = 0, tG = 0; filas.forEach(function (f) { tI += f.i; tG += f.g; });
    var fijoMes = 0; gas.forEach(function (g) { if (g.frecuencia !== 'unico') fijoMes += gastoMes(g, new Date(hoy.getFullYear(), hoy.getMonth(), 1), altas, usd); });
    vista.innerHTML = '<h1 class="vista-titulo">Ingresos y gastos</h1>' +
      '<div class="te-barra"><button class="te-btn principal" data-excel>Exportar a Excel</button></div>' +
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
      '<label>Nota<input name="nota" maxlength="200"></label><label style="grid-auto-flow:column;justify-content:start;align-items:center;gap:8px"><input name="poralu" type="checkbox" style="width:auto;min-height:0"> Es por cada alumno</label><button class="te-btn principal" type="submit">Guardar gasto</button></form><p class="te-err" id="te-gerr" hidden></p>' +
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
      if (ev.target.closest('[data-excel]')) return exportarExcel(filas, ing, gas, usd, altas);
      if ((b = ev.target.closest('[data-preset]'))) { var p = PRESETS[+b.getAttribute('data-preset')]; form.concepto.value = p[0]; form.cat.value = p[1]; form.prov.value = p[2]; form.poralu.checked = !!p[3]; if (p[3]) form.frec.value = 'anual'; form.monto.focus(); }
      else if ((b = ev.target.closest('[data-borrar-gasto]'))) { if (!confirm('¿Borrar este gasto? Desaparece de todos los meses.')) return; var r = await sb.from('gastos').delete().eq('id', b.getAttribute('data-borrar-gasto')); if (r.error) toast('No se pudo borrar', true); else vistaFinanzas(); }
      else if ((b = ev.target.closest('[data-cerrar-gasto]'))) { var r2 = await sb.from('gastos').update({ hasta: new Date().toISOString().slice(0, 10) }).eq('id', b.getAttribute('data-cerrar-gasto')); if (r2.error) toast('No se pudo dar de baja', true); else vistaFinanzas(); }
    };
    form.onsubmit = async function (ev) {
      ev.preventDefault(); var er = document.getElementById('te-gerr'); er.hidden = true;
      var r = await sb.from('gastos').insert({ concepto: form.concepto.value.trim(), categoria: form.cat.value, proveedor: form.prov.value.trim() || null, monto: +form.monto.value, moneda: form.mon.value, frecuencia: form.frec.value, desde: form.desde.value, hasta: form.hasta.value || null, nota: form.nota.value.trim() || null, por_alumno: form.poralu.checked });
      if (r.error) { er.textContent = 'No se pudo guardar el gasto.'; er.hidden = false; return; }
      toast('Gasto guardado'); vistaFinanzas();
    };
  }

  // ---------- Facturas ----------
  async function vistaFacturas() {
    vista.innerHTML = '<h1 class="vista-titulo">Facturas</h1><p class="te-nota">Se generan desde Comprobantes, con el botón "Generar factura" en un pago aprobado. Las familias las ven en su sección Pagos.</p><div id="te-fac"><div class="te-vacio">Cargando…</div></div>';
    var r = await sb.rpc('tesoreria_facturas'), c = document.getElementById('te-fac');
    if (r.error) { c.innerHTML = '<div class="te-vacio">' + esc(r.error.message) + '</div>'; return; }
    var lst = r.data || [];
    c.innerHTML = lst.length ? '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Número</th><th>Fecha</th><th>Receptor</th><th>Concepto</th><th class="num">Importe</th><th>Estado</th><th></th></tr></thead><tbody>' + lst.map(function (f) {
      return '<tr><td>C ' + ('0000' + f.punto_venta).slice(-5) + '-' + ('00000000' + f.numero).slice(-8) + '</td><td>' + fecha(f.fecha + 'T12:00:00') + '</td><td>' + esc(f.receptor_nombre) + '</td><td>' + esc(f.concepto) + '</td><td class="num">' + ars(f.importe) + '</td><td>' + sello(f.estado === 'emitida' ? 'al_dia' : 'en_plazo', f.estado === 'emitida' ? 'Emitida en ARCA' : 'Sin validez fiscal') + '</td><td><button class="te-btn" data-factura="' + f.id + '">Ver / imprimir</button></td></tr>';
    }).join('') + '</tbody></table></div>' : '<div class="te-vacio">Todavía no se generó ninguna factura.</div>';
  }

  // ---------- Exportar a Excel ----------
  async function exportarExcel(filas, ing, gas, usd, altas) {
    if (!window.XLSX) { toast('No cargó la librería de Excel. Recargá la página.', true); return; }
    var res = await Promise.all([sb.rpc('tesoreria_cuotas', { p_periodo: iso(new Date()) }), sb.rpc('tesoreria_matriculas')]);
    var wb = XLSX.utils.book_new();
    function hoja(nombre, datos) { XLSX.utils.book_append_sheet(wb, XLSX.utils.json_to_sheet(datos.length ? datos : [{ '': 'Sin datos' }]), nombre); }
    hoja('Resumen mensual', filas.map(function (f) { return { Mes: mesTxt(f.m), Ingresos: Math.round(f.i), Gastos: Math.round(f.g), Resultado: Math.round(f.i - f.g) }; }));
    hoja('Ingresos', ing.map(function (x) { return { Fecha: fecha(x.fecha), Familia: x.familia, Origen: x.origen, Detalle: x.detalle, 'Monto (ARS)': Math.round(x.monto_ars) }; }));
    hoja('Gastos', gas.map(function (g) { return { Concepto: g.concepto, Categoría: g.categoria, Proveedor: g.proveedor || '', Monto: +g.monto, Moneda: g.moneda, Frecuencia: g.frecuencia, 'Por alumno': g.por_alumno ? 'Sí' : 'No', Desde: g.desde, Hasta: g.hasta || '', Nota: g.nota || '' }; }));
    hoja('Cuotas ' + mesTxt(new Date()), (res[0].data || []).map(function (x) { return { Familia: x.familia, Email: x.email, WhatsApp: x.telefono || '', Alumnos: x.alumnos, Cuota: +x.cuota, Pagado: +x.aprobado, Estado: ESTADO[x.estado] || x.estado }; }));
    hoja('Matrículas', (res[1].data || []).map(function (x) { return { Alumno: x.alumno, Familia: x.familia, Email: x.email, 'Último pago': x.ultimo_pago ? fecha(x.ultimo_pago) : '', Vence: x.vence || '', Estado: x.estado, 'Monto actual': +x.monto_actual }; }));
    XLSX.writeFile(wb, 'Wave-Academy-tesoreria-' + new Date().toISOString().slice(0, 10) + '.xlsx');
  }

  // ---------- Proyección ----------
  var tasaCobro = 100;
  async function vistaProyeccion() {
    vista.innerHTML = '<h1 class="vista-titulo">Proyección</h1><div class="te-vacio">Calculando…</div>';
    var hoy = new Date(), p1 = new Date(hoy.getFullYear(), hoy.getMonth() + 1, 1);
    var res = await Promise.all([sb.rpc('tesoreria_cuotas', { p_periodo: iso(hoy) }), sb.rpc('tesoreria_matriculas'), sb.from('gastos').select('*'), sb.rpc('tesoreria_alumnos_alta'), sb.from('app_settings').select('value').eq('key', 'dolar').maybeSingle()]);
    if (res[0].error) { vista.innerHTML = '<h1 class="vista-titulo">Proyección</h1><div class="te-vacio">No pudimos calcular la proyección.</div>'; return; }
    var cuotas = res[0].data || [], mats = res[1].data || [], gas = res[2].data || [], altas = (res[3].data || []).map(function (a) { return new Date(a.alta); }), usd = res[4].data && res[4].data.value ? +res[4].data.value.ars_por_usd : 0;
    var cuotaMes = 0; cuotas.forEach(function (c) { cuotaMes += +c.cuota; });
    var meses = []; for (var i = 0; i < 6; i++) meses.push(new Date(p1.getFullYear(), p1.getMonth() + i, 1));
    function pintar() {
      var acum = 0;
      var filas = meses.map(function (m) {
        var fin = new Date(m.getFullYear(), m.getMonth() + 1, 0, 23, 59, 59);
        var c = cuotaMes * tasaCobro / 100, mat = 0;
        mats.forEach(function (x) { if (x.vence && new Date(x.vence + 'T12:00:00') >= m && new Date(x.vence + 'T12:00:00') <= fin) mat += +x.monto_actual; });
        var g = 0; gas.forEach(function (x) { g += gastoMes(x, m, altas, usd); });
        acum += c + mat - g;
        return { m: m, c: c, mat: mat, g: g, r: c + mat - g, acum: acum };
      });
      document.getElementById('te-proy').innerHTML = '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Mes</th><th class="num">Cuotas</th><th class="num">Matrículas que vencen</th><th class="num">Gastos</th><th class="num">Resultado</th><th class="num">Acumulado</th></tr></thead><tbody>' + filas.map(function (f) {
        return '<tr><td>' + esc(mesTxt(f.m)) + '</td><td class="num">' + ars(f.c) + '</td><td class="num">' + ars(f.mat) + '</td><td class="num">' + ars(f.g) + '</td><td class="num"><b style="color:' + (f.r >= 0 ? '#14663A' : '#A12C1F') + '">' + ars(f.r) + '</b></td><td class="num">' + ars(f.acum) + '</td></tr>';
      }).join('') + '</tbody></table></div>';
    }
    vista.innerHTML = '<h1 class="vista-titulo">Proyección</h1><p class="te-nota">Próximos 6 meses con los alumnos y gastos de hoy. No incluye alumnos nuevos. Las matrículas se cuentan en el mes en que vencen las actuales (a 12 meses de su pago).</p>' +
      '<div class="te-form una"><label>¿Qué porcentaje de las cuotas calculás que se cobra? (' + ars(cuotaMes) + ' por mes si todos pagan)<input id="te-tasa" type="number" min="0" max="100" value="' + tasaCobro + '"></label></div><div id="te-proy"></div>';
    document.getElementById('te-tasa').oninput = function () { tasaCobro = Math.max(0, Math.min(100, +this.value || 0)); pintar(); };
    pintar();
  }

  // ---------- Altas ----------
  async function vistaAltas() {
    vista.innerHTML = '<h1 class="vista-titulo">Altas recientes</h1><p class="te-nota">Alumnos que se sumaron en los últimos 90 días, con su cuota y el estado de la matrícula.</p><div id="te-altas"><div class="te-vacio">Cargando…</div></div>';
    var rr = await Promise.all([sb.rpc('tesoreria_altas', { p_dias: 90 }), sb.rpc('tesoreria_matriculas')]), r = rr[0], c = document.getElementById('te-altas');
    if (r.error) { c.innerHTML = '<div class="te-vacio">' + esc(r.error.message) + '</div>'; return; }
    c.innerHTML = (r.data || []).length ? '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Alumno/a</th><th>Familia</th><th>Contacto</th><th>Nivel</th><th class="num">Cuota</th><th>Matrícula</th><th>Alta</th></tr></thead><tbody>' + r.data.map(function (a) {
      return '<tr><td><b>' + esc(a.alumno) + '</b></td><td>' + esc(a.familia) + '</td><td>' + esc(a.email || '') + '<br><small>' + esc(a.telefono || 'sin WhatsApp') + '</small></td><td>' + esc(a.nivel || '—') + '</td><td class="num">' + (+a.cuota ? ars(a.cuota) : '—') + '</td><td>' + esc({ vigente: 'Vigente', vencida: 'Vencida', sin_pago: 'Sin pagar' }[a.matricula] || a.matricula || '—') + (a.matricula_vence ? '<br><small>hasta ' + fecha(a.matricula_vence + 'T12:00:00') + '</small>' : '') + '</td><td>' + fecha(a.alta) + '</td></tr>';
    }).join('') + '</tbody></table></div>' : '<div class="te-vacio">No hay altas en los últimos 90 días.</div>';
    var ms = rr[1].data || [];
    c.innerHTML += '<h2 class="te-sub">Matrículas anuales</h2>' + (ms.length ? '<div class="te-envoltorio"><table class="te-tabla"><thead><tr><th>Alumno/a</th><th>Estado</th><th>Último pago</th><th>Vence / próxima matrícula</th><th class="num">Monto actual</th></tr></thead><tbody>' + ms.map(function (x) {
      return '<tr><td><b>' + esc(x.alumno) + '</b><br><small>' + esc(x.familia) + '</small></td><td>' + sello(x.estado === 'vigente' ? 'al_dia' : x.estado === 'vencida' ? 'atrasado' : 'en_plazo', { vigente: 'Vigente', vencida: 'Vencida', sin_pago: 'Sin pagar' }[x.estado]) + (x.en_revision ? ' ' + sello('en_revision') : '') + '</td><td>' + (x.ultimo_pago ? fecha(x.ultimo_pago) : '—') + '</td><td>' + (x.vence ? fecha(x.vence + 'T12:00:00') : '—') + '</td><td class="num">' + ars(x.monto_actual) + '</td></tr>';
    }).join('') + '</tbody></table></div>' : '<div class="te-vacio">Todavía no hay alumnos.</div>');
  }

  // ---------- Datos fiscales ----------
  async function vistaFiscales() {
    var rf = await sb.rpc('datos_facturacion'), df = rf.data || {};
    vista.innerHTML = '<h1 class="vista-titulo">Datos fiscales</h1><p class="te-nota">Aparecen en las facturas que reciben las familias.</p>' +
      '<form id="te-fisc" class="te-form una"><label>Razón social / nombre<input name="razon_social" maxlength="120" value="' + esc(df.razon_social) + '"></label><label>CUIT<input name="cuit" maxlength="20" value="' + esc(df.cuit) + '"></label>' +
      '<label>Domicilio comercial<input name="domicilio" maxlength="200" value="' + esc(df.domicilio) + '"></label><label>Condición frente al IVA<input name="condicion" maxlength="60" value="' + esc(df.condicion || 'Responsable Monotributo') + '"></label>' +
      '<label>Ingresos Brutos<input name="iibb" maxlength="30" value="' + esc(df.iibb) + '"></label><label>Inicio de actividades<input name="inicio_actividades" type="date" value="' + esc(df.inicio_actividades) + '"></label>' +
      '<label>Punto de venta<input name="punto_venta" type="number" min="1" value="' + esc(df.punto_venta || 1) + '"></label>' +
      '<label style="grid-auto-flow:column;justify-content:start;align-items:center;gap:10px"><input name="arca_activo" type="checkbox" style="width:auto;min-height:0"' + (df.arca_activo ? ' checked' : '') + '> Facturar de verdad con ARCA</label>' +
      '<p class="te-nota">Todavía no está conectada a ARCA: hasta que se conecte, las facturas salen como comprobante sin validez fiscal. Este botón queda guardado para cuando hagamos la conexión.</p><button class="te-btn principal" type="submit">Guardar datos fiscales</button></form>';
    document.getElementById('te-fisc').onsubmit = async function (ev) { ev.preventDefault(); var f = ev.target; var x = await sb.rpc('guardar_datos_facturacion', { p: { razon_social: f.razon_social.value, cuit: f.cuit.value, domicilio: f.domicilio.value, condicion: f.condicion.value, iibb: f.iibb.value, inicio_actividades: f.inicio_actividades.value, punto_venta: +f.punto_venta.value || 1, arca_activo: f.arca_activo.checked } }); toast(x.error ? 'No se pudo guardar' : 'Datos fiscales guardados', !!x.error); };
  }

  // ---------- Datos de transferencia ----------
  async function vistaTransferencia() {
    var rb = await sb.rpc('bloqueo_mora_activo'), r = await sb.rpc('datos_transferencia'), d = r.data || {};
    vista.innerHTML = '<h1 class="vista-titulo">Datos de transferencia</h1><p class="te-nota">Esto es lo que ven las familias en su sección Pagos.</p>' +
      '<form id="te-tf" class="te-form una"><label>Banco o billetera<input name="banco" maxlength="80" value="' + esc(d.banco) + '"></label><label>Titular de la cuenta<input name="titular" maxlength="120" value="' + esc(d.titular) + '"></label>' +
      '<label>CUIT/CUIL<input name="cuit" maxlength="20" value="' + esc(d.cuit) + '"></label><label>CBU/CVU<input name="cbu" maxlength="30" value="' + esc(d.cbu) + '"></label><label>Alias<input name="alias" maxlength="40" value="' + esc(d.alias) + '"></label>' +
      '<label>Nota para las familias (opcional)<input name="nota" maxlength="300" value="' + esc(d.nota) + '" placeholder="Ej: poné el apellido de la familia en el concepto"></label><button class="te-btn principal" type="submit">Guardar</button></form>' +
      '<h2 class="te-sub">Bloqueo por mora</h2><div class="te-form una"><label style="grid-auto-flow:column;justify-content:start;align-items:center;gap:10px"><input id="te-bloq" type="checkbox" style="width:auto;min-height:0"' + (rb.data === true ? ' checked' : '') + '> Bloquear el acceso de los alumnos cuando la familia pasa el plazo de gracia</label>' +
      '<p class="te-nota">La cuota vence el 10. Pasado el 10 la familia figura atrasada; cuando terminan los días de gracia (hoy 15) figura bloqueada. Con esto activado, los alumnos de familias bloqueadas no pueden entrar hasta regularizar. Está apagado por defecto: activalo cuando ya estén cargados los datos de transferencia y las cuotas reales.</p></div>';
    document.getElementById('te-bloq').onchange = async function () { var x = await sb.rpc('guardar_bloqueo_mora', { p_activo: this.checked }); toast(x.error ? 'No se pudo guardar' : this.checked ? 'Bloqueo por mora activado' : 'Bloqueo por mora desactivado', !!x.error); };
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
    else if ((b = ev.target.closest('[data-facturar]'))) { b.disabled = true; var fx = await sb.rpc('emitir_factura', { p_pago: b.getAttribute('data-facturar') }); if (fx.error) { toast(fx.error.message, true); b.disabled = false; } else { toast('Factura generada. La familia ya puede verla.'); vistaComprobantes(); } }
    else if ((b = ev.target.closest('[data-factura]'))) { var fr = await Promise.all([sb.rpc('tesoreria_facturas'), sb.rpc('datos_facturacion')]); var ff = (fr[0].data || []).filter(function (z) { return z.id === b.getAttribute('data-factura'); })[0]; if (ff) WaveFactura.abrir(ff, fr[1].data); }
    else if ((b = ev.target.closest('[data-aprobar]'))) { b.disabled = true; var r = await sb.rpc('revisar_pago', { p_id: b.getAttribute('data-aprobar'), p_estado: 'aprobado', p_nota: null }); if (r.error) toast(r.error.message, true); else toast('Pago aprobado. Se avisó a la familia.'); vistaComprobantes(); }
    else if ((b = ev.target.closest('[data-rechazar]'))) {
      var motivo = prompt('Motivo del rechazo (se lo mostramos a la familia):'); if (motivo === null) return;
      var r2 = await sb.rpc('revisar_pago', { p_id: b.getAttribute('data-rechazar'), p_estado: 'rechazado', p_nota: motivo }); if (r2.error) toast(r2.error.message, true); else toast('Comprobante rechazado. Se avisó a la familia.'); vistaComprobantes();
    }
  });

  var VISTAS = { cuotas: vistaCuotas, comprobantes: vistaComprobantes, finanzas: vistaFinanzas, proyeccion: vistaProyeccion, facturas: vistaFacturas, fiscales: vistaFiscales, altas: vistaAltas, transferencia: vistaTransferencia };
  function ruta() {
    var h = (location.hash || '#cuotas').slice(1); if (!VISTAS[h]) h = 'cuotas';
    enlaces.forEach(function (a) { a.classList.toggle('activo', a.getAttribute('href') === '#' + h); });
    vista.onclick = null; VISTAS[h]();
  }
  window.addEventListener('hashchange', ruta);
  ruta();
})();
