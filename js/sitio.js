// Sitio público: texto grande, versión de la clase, actividad de muestra y planes con los precios reales de la base.
(function () {
  var cfg = window.WAVE_CONFIG;

  // Texto más grande (se recuerda en este navegador)
  var aa = document.querySelectorAll('.aa');
  function aplicarGrande(on) {
    document.body.classList.toggle('grande', on);
    aa.forEach(function (b) { b.setAttribute('aria-pressed', on ? 'true' : 'false'); });
  }
  try { aplicarGrande(localStorage.getItem('wave-grande') === '1'); } catch (e) {}
  aa.forEach(function (b) {
    b.addEventListener('click', function () {
      var on = !document.body.classList.contains('grande');
      aplicarGrande(on);
      try { localStorage.setItem('wave-grande', on ? '1' : '0'); } catch (e) {}
    });
  });

  // Clase: versión argentina o neutra
  var SUB = {
    ar: 'Imaginá una fábrica de alfajores. Cada alfajor suelto es una unidad. Cuando juntás 10 alfajores se arma un paquete: una decena.',
    ne: 'Imagina una fábrica de alfajores. Cada alfajor suelto es una unidad. Cuando juntas 10 alfajores se arma un paquete: una decena.'
  };
  var voz = 'ar';
  var sub = document.getElementById('clase-sub');
  var consigna = document.getElementById('act-consigna');
  document.querySelectorAll('[data-voz]').forEach(function (b) {
    b.addEventListener('click', function () {
      voz = b.getAttribute('data-voz');
      document.querySelectorAll('[data-voz]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      if (sub) sub.textContent = SUB[voz];
      if (consigna) consigna.textContent = voz === 'ar' ? 'Pasá 1010₂ a decimal.' : 'Pasa 1010₂ a decimal.';
    });
  });

  // Actividad real de Matemática I, misión 1
  var form = document.getElementById('act-form');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var v = document.getElementById('act-resp').value.trim();
      var out = document.getElementById('act-devolucion');
      var n = parseFloat(v.replace(',', '.'));
      out.hidden = false;
      out.classList.toggle('ok', n === 10);
      if (!v) out.innerHTML = '<b>Falta la respuesta.</b> ' + (voz === 'ar' ? 'Escribí un número y corregí.' : 'Escribe un número y corrige.');
      else if (n === 10) out.innerHTML = '<b>Correcto.</b> 0 × 1 + 1 × 2 + 0 × 4 + 1 × 8 = 10.';
      else out.innerHTML = '<b>No es correcto.</b> La respuesta es 10: 0 × 1 + 1 × 2 + 0 × 4 + 1 × 8 = 10.';
    });
  }

  // Planes: precios reales desde la base
  var tabla = document.getElementById('planes-tabla');
  if (!tabla) return;
  var NIVEL_FIJO = tabla.getAttribute('data-nivel');
  var estado = { pais: 'ar', nivel: NIVEL_FIJO || 'avanzado' };
  var datos = null;
  var MODS = [['libre', 'Libre'], ['guiada', 'Guiada'], ['completa', 'Completa']];
  var FILAS = [
    ['Programa completo, clases, material y exámenes', ['Incluido', 'Incluido', 'Incluido']],
    ['Tutor con inteligencia artificial', ['Incluido', 'Incluido', 'Incluido']],
    ['Tutorías individuales por videollamada', ['2 por mes', '4 por mes', '4 por mes']],
    ['Corrección de proyectos y escritura por el tutor', ['No', 'Incluida', 'Incluida']],
    ['Oficios', ['No', 'No', 'Talleres y trayecto']],
    ['Panel de la familia y turnos con dirección', ['Incluido', 'Incluido', 'Incluido']]
  ];
  function ars(usd) { return '$' + Math.round(usd * datos.dolar).toLocaleString('es-AR'); }
  function pintar() {
    if (!datos) return;
    var ar = estado.pais === 'ar';
    var precio = {};
    datos.tarifas.forEach(function (t) { if (t.nivel === estado.nivel) precio[t.modalidad] = Number(t.usd); });
    var cols = MODS.filter(function (m) { return !NIVEL_FIJO || precio[m[0]] != null; });
    var head = '<tr><th scope="col" style="width: 34%"></th>' + cols.map(function (m) {
      var u = precio[m[0]], hay = u != null;
      return '<th scope="col" class="' + (hay ? '' : 'apagado') + '"><span class="plan-nombre">' + m[1] + '</span>' +
        '<span class="plan-precio">' + (!hay ? 'No disponible' : (ar ? ars(u) : 'USD ' + u)) + '</span>' +
        '<span class="plan-nota">' + (!hay ? (m[0] === 'completa' ? 'solo secundaria' : 'primaria y secundaria') : (ar ? 'por mes, USD ' + u : 'por mes')) + '</span></th>';
    }).join('') + '</tr>';
    var body = FILAS.filter(function (f) { return !(NIVEL_FIJO && f[0] === 'Oficios' && precio.completa == null); }).map(function (f) {
      return '<tr><th scope="row">' + f[0] + '</th>' + cols.map(function (m) {
        var i = MODS.findIndex(function (x) { return x[0] === m[0]; });
        return '<td class="' + (precio[m[0]] != null ? '' : 'apagado') + '">' + f[1][i] + '</td>';
      }).join('') + '</tr>';
    }).join('');
    tabla.innerHTML = '<thead>' + head + '</thead><tbody>' + body + '</tbody>';
    var mat = document.getElementById('planes-matricula');
    if (mat && datos.matricula) mat.textContent = 'Matrícula anual: ' + (ar ? ars(datos.matricula) + ' (USD ' + datos.matricula + ')' : 'USD ' + datos.matricula) + ', en hasta ' + (datos.cuotas_matricula || 2) + ' cuotas.';
  }
  document.querySelectorAll('[data-pais],[data-nivel-btn]').forEach(function (b) {
    b.addEventListener('click', function () {
      var grupo = b.hasAttribute('data-pais') ? 'pais' : 'nivel';
      estado[grupo] = b.getAttribute(grupo === 'pais' ? 'data-pais' : 'data-nivel-btn');
      document.querySelectorAll(grupo === 'pais' ? '[data-pais]' : '[data-nivel-btn]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      pintar();
    });
  });
  fetch(cfg.SUPABASE_URL + '/rest/v1/rpc/precios_publicos', {
    method: 'POST', headers: { apikey: cfg.SUPABASE_KEY, 'Content-Type': 'application/json' }, body: '{}'
  }).then(function (r) { return r.json(); }).then(function (d) { datos = d; pintar(); })
    .catch(function () { tabla.innerHTML = '<tbody><tr><td>No pudimos cargar los precios. Escribinos y te los pasamos.</td></tr></tbody>'; });
})();
