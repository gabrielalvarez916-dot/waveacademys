// Factura C con el diseño de ARCA (monotributo). Si todavía no está conectada a ARCA, se marca "sin validez fiscal".
(function () {
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function pad(n, l) { return String(n).padStart(l, '0'); }
  function dmy(v) { if (!v) return ''; var p = String(v).slice(0, 10).split('-'); return p[2] + '/' + p[1] + '/' + p[0]; }
  function money(n) { return Number(n || 0).toLocaleString('es-AR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }

  function html(f, e) {
    e = e || {};
    var fiscal = f.estado === 'emitida' && f.cae;
    var nro = pad(f.punto_venta, 5) + '-' + pad(f.numero, 8);
    var fila = function (a, b) { return '<p><b>' + a + '</b> ' + esc(b || '') + '</p>'; };
    return '<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Factura C ' + nro + '</title><style>' +
      '@page{size:A4;margin:12mm}*{box-sizing:border-box}body{font:13px/1.35 Arial,Helvetica,sans-serif;color:#111;margin:0;background:#eee}' +
      '.hoja{width:190mm;margin:10px auto;background:#fff;border:1px solid #111;padding:0}.barra{max-width:190mm;margin:10px auto;display:flex;gap:8px;justify-content:flex-end}' +
      '.barra button{padding:10px 18px;border:0;border-radius:8px;background:#087E83;color:#fff;font-weight:700;cursor:pointer}' +
      '.orig{text-align:center;font-weight:700;font-size:16px;padding:6px;border-bottom:1px solid #111}' +
      '.cab{display:grid;grid-template-columns:1fr 70px 1fr;border-bottom:1px solid #111}.cab>div{padding:10px 12px}.cab h1{margin:0 0 6px;font-size:22px}' +
      '.letra{border-left:1px solid #111;border-right:1px solid #111;text-align:center;padding:4px!important}.letra b{display:block;font-size:34px;line-height:1.1}.letra small{font-size:10px}' +
      'p{margin:2px 0}.per,.rec{padding:8px 12px;border-bottom:1px solid #111}table{width:100%;border-collapse:collapse}' +
      'th{background:#ddd;border:1px solid #111;padding:5px;font-size:11px;text-align:left}td{padding:6px 5px;border-bottom:1px solid #ccc;vertical-align:top}.num{text-align:right;white-space:nowrap}' +
      '.tot{display:flex;justify-content:flex-end;padding:10px 12px;border-top:1px solid #111;margin-top:140px}.tot div{min-width:240px}.tot p{display:flex;justify-content:space-between}' +
      '.pie{display:flex;justify-content:space-between;gap:12px;padding:10px 12px;border-top:1px solid #111;font-size:13px}.aviso{background:#B3261E;color:#fff;text-align:center;font-weight:700;padding:7px;font-size:12px}' +
      '@media print{body{background:#fff}.barra{display:none}.hoja{margin:0;width:auto}}</style></head><body>' +
      '<div class="barra"><button onclick="window.print()">Imprimir o guardar como PDF</button></div><div class="hoja">' +
      (fiscal ? '' : '<div class="aviso">COMPROBANTE SIN VALIDEZ FISCAL · todavía no emitido en ARCA</div>') +
      '<div class="orig">ORIGINAL</div><div class="cab"><div><h1>' + esc(e.razon_social || 'Wave Academy') + '</h1>' + fila('Razón social:', e.razon_social) + fila('Domicilio comercial:', e.domicilio) + fila('Condición frente al IVA:', e.condicion || 'Responsable Monotributo') + '</div>' +
      '<div class="letra"><b>C</b><small>COD. 011</small></div><div><h1>FACTURA</h1>' + fila('Punto de venta:', pad(f.punto_venta, 5) + '  Comp. Nro: ' + pad(f.numero, 8)) + fila('Fecha de emisión:', dmy(f.fecha)) + fila('CUIT:', e.cuit) + fila('Ingresos Brutos:', e.iibb) + fila('Fecha de inicio de actividades:', e.inicio_actividades ? dmy(e.inicio_actividades) : '') + '</div></div>' +
      '<div class="per"><b>Período facturado Desde:</b> ' + dmy(f.fecha) + ' &nbsp; <b>Hasta:</b> ' + dmy(f.fecha) + ' &nbsp; <b>Fecha de Vto. para el pago:</b> ' + dmy(f.fecha) + '</div>' +
      '<div class="rec">' + fila('CUIT/DNI:', f.receptor_doc || '—') + fila('Apellido y Nombre / Razón Social:', f.receptor_nombre) + fila('Condición frente al IVA:', f.receptor_condicion) + fila('Condición de venta:', 'Transferencia bancaria') + '</div>' +
      '<table><thead><tr><th>Código</th><th>Producto / Servicio</th><th class="num">Cantidad</th><th>U. medida</th><th class="num">Precio Unit.</th><th class="num">% Bonif</th><th class="num">Imp. Bonif.</th><th class="num">Subtotal</th></tr></thead><tbody>' +
      '<tr><td>1</td><td>' + esc(f.concepto) + '</td><td class="num">1,00</td><td>unidades</td><td class="num">' + money(f.importe) + '</td><td class="num">0,00</td><td class="num">0,00</td><td class="num">' + money(f.importe) + '</td></tr></tbody></table>' +
      '<div class="tot"><div><p><b>Subtotal: $</b><span>' + money(f.importe) + '</span></p><p><b>Importe Otros Tributos: $</b><span>0,00</span></p><p><b>Importe Total: $</b><span>' + money(f.importe) + '</span></p></div></div>' +
      '<div class="pie"><div><p><b>Comprobante autorizado</b></p><small>' + (fiscal ? 'Esta factura fue emitida en ARCA.' : 'Documento interno de Wave Academy. No es una factura fiscal hasta conectarse a ARCA.') + '</small></div>' +
      '<div><p><b>CAE N°:</b> ' + esc(f.cae || '—') + '</p><p><b>Fecha de Vto. de CAE:</b> ' + (f.cae_vence ? dmy(f.cae_vence) : '—') + '</p></div></div></div></body></html>';
  }

  function abrir(f, emisor) {
    var w = window.open('', '_blank');
    if (!w) { alert('El navegador bloqueó la ventana. Permití ventanas emergentes para ver la factura.'); return; }
    w.document.open(); w.document.write(html(f, emisor)); w.document.close();
  }
  window.WaveFactura = { abrir: abrir };
})();
