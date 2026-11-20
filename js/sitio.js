// Sitio público: texto grande, recorrido por la plataforma, temario real y planes con los precios de la base.
(function () {
  var cfg = window.WAVE_CONFIG;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

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

  // ---------- Recorrido por la plataforma (capturas reales) ----------
  var plat = document.getElementById('plat');
  if (plat) {
    var P = '/assets/plataforma/';
    var VISTAS = [
      { id: 'misiones', tab: 'Misiones', tit: 'Cada materia es un viaje de misiones.',
        txt: 'Ordenadas de lo más simple a lo más complejo. Cada misión tiene sus niveles y cada nivel tiene siempre el mismo recorrido, para que el alumno sepa dónde está parado.',
        items: ['Introducción en video de cada materia', 'Niveles que se abren de a uno', 'Nivel jefe al final de cada misión'],
        imgs: [['misiones', 'Misiones de Matemática I'], ['niveles', 'Niveles de la misión 1']] },
      { id: 'clase', tab: 'Clase animada', tit: 'Una clase animada de pocos minutos.',
        txt: 'Presenta el tema desde una situación real, con la voz y la imagen trabajando juntas y una sola idea por vez.',
        items: ['Se pausa, se repite y se ve en pantalla completa', 'Versión argentina y versión neutra para otros países', 'Matemática I, misión 1, nivel 1'],
        imgs: [['clase', 'Clase: el sistema decimal'], ['clase-2', 'Clase: unidades y decenas']] },
      { id: 'pdf', tab: 'Material en PDF', tit: 'Un material para leer con la carpeta al lado.',
        txt: 'Con ejemplos resueltos, ejemplos para completar y ejemplos para hacer solo. Se lee en la plataforma o se descarga.',
        items: ['Resumen y glosario en cada lección', 'Tips y errores comunes antes de que aparezcan', 'Respuestas de los ejemplos al final'],
        hojas: ['pdf-portada', 'pdf-pagina', 'pdf-carpeta'] },
      { id: 'carpeta', tab: 'Carpeta', tit: 'Consignas de carpeta que se entregan.',
        txt: 'El alumno resuelve en su carpeta y carga sus respuestas. Las soluciones aparecen cuando entrega todo bien.',
        items: ['Se aprueba aunque algo haya salido mal', 'Cada respuesta trae su explicación'],
        imgs: [['carpeta', 'Entrega de carpeta']] },
      { id: 'actividad', tab: 'Actividades', tit: 'Actividades con devolución inmediata.',
        txt: 'Para practicar y sumar puntos. Cada misión cierra con una práctica general que mezcla todo lo visto y con el nivel jefe.',
        items: ['Números al azar en cada intento', 'Respuestas de opción múltiple, numéricas y escritas', 'Las respuestas escritas las corrige la inteligencia artificial'],
        imgs: [['actividad', 'Actividad de Matemática I']] },
      { id: 'alumno', tab: 'Panel del alumno', tit: 'Todo lo suyo, en un solo lugar.',
        txt: 'Sus materias con el avance y el promedio de cada una, la programación de la semana, sus estadísticas y su perfil.',
        items: ['Tiempo de estudio de la semana', 'Promedio por materia', 'Avatar que elige el alumno'],
        imgs: [['cursos', 'Mis cursos'], ['estadisticas', 'Estadísticas'], ['programacion', 'Programación'], ['perfil', 'Perfil']] },
      { id: 'familia', tab: 'Panel de la familia', tit: 'Nadie tiene que adivinar cómo va su hijo.',
        txt: 'La familia arma la programación semanal de cada hijo y ve, en todo momento, el avance y el promedio de cada materia.',
        items: ['Última conexión, progreso y promedio general', 'Programación semanal y fecha objetivo', 'Turnos con dirección y tutorías', 'Facturación'],
        imgs: [['familia', 'Progreso'], ['programacion', 'Programación']] }
    ];
    function marco(im, chico) {
      return '<figure class="marco' + (chico ? ' marco-chico' : '') + '"><div class="marco-barra"><i></i><i></i><i></i></div><img src="' + P + im[0] + '.webp" alt="' + esc(im[1]) + '" loading="lazy"><figcaption>' + esc(im[1]) + '</figcaption></figure>';
    }
    plat.innerHTML = VISTAS.map(function (v, n) {
      var texto = '<div class="plat-texto"><p class="plat-num">' + (n + 1 < 10 ? '0' : '') + (n + 1) + ' · ' + v.tab + '</p><h3>' + v.tit + '</h3><p class="p">' + v.txt + '</p><ul>' + v.items.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul></div>';
      var foto = v.hojas
        ? '<div class="plat-hojas">' + v.hojas.map(function (h) { return '<img src="' + P + h + '.webp" alt="Página del PDF de la lección 1 de Matemática I" loading="lazy" width="900" height="1273">'; }).join('') + '</div>'
        : marco(v.imgs[0]) + (v.imgs.length > 1 ? '<div class="plat-extra">' + v.imgs.slice(1).map(function (im) { return marco(im, true); }).join('') + '</div>' : '');
      return '<div class="plat-fila' + (n % 2 ? ' al-reves' : '') + '">' + texto + '<div class="plat-vista">' + foto + '</div></div>';
    }).join('');
  }

  // ---------- Temario real (misiones de cada materia, por año) ----------
  var tem = document.getElementById('temario');
  var reparto = document.getElementById('reparto');
  if (tem || reparto) {
    fetch('/js/temario.json?v=11202300').then(function (r) { return r.json(); }).then(function (T) {
      if (reparto) pintarReparto(T, reparto);
      if (tem) pintarTemario(T, tem);
      var of = document.getElementById('oficios');
      if (of && T.oficios) of.innerHTML = T.oficios.trayectos.map(function (o) { return '<span style="border-color: rgba(22,57,59,.35)">' + esc(o) + '</span>'; }).join('');
    }).catch(function () {});
  }
  function pintarReparto(T, box) {
    var nivel = box.getAttribute('data-nivel');
    var porMat = {}, orden = [];
    Object.keys(T[nivel]).forEach(function (a) {
      T[nivel][a].forEach(function (m) {
        var base = m.m.replace(/\s+(\d+|[IVX]+)$/, '');
        if (/^Ciencias Naturales/.test(base) || /^Biolog|^F[ií]sic|^Qu[ií]mica/.test(base)) base = 'Ciencias Naturales y exactas';
        if (/^Ciencias Sociales|^Historia|^Geograf/.test(base)) base = 'Ciencias Sociales, Historia y Geografía';
        if (/^Ciudadan|^Formaci[oó]n Ciudadana/.test(base)) base = 'Ciudadanía';
        if (!porMat[base]) { porMat[base] = { n: 0, c: m.c }; orden.push(base); }
        porMat[base].n += m.t.length;
      });
    });
    var total = orden.reduce(function (s, k) { return s + porMat[k].n; }, 0);
    orden.sort(function (a, b) { return porMat[b].n - porMat[a].n; });
    box.innerHTML = '<p class="reparto-tit">Cómo se reparten las ' + total.toLocaleString('es-AR') + ' misiones <span>por área</span></p>' +
      '<div class="barra-rep">' + orden.map(function (k) {
        var pct = porMat[k].n / total * 100;
        return '<div style="flex: ' + porMat[k].n + '; background: ' + porMat[k].c + '" title="' + esc(k) + ': ' + porMat[k].n + '">' + (pct > 9 ? porMat[k].n : '') + '</div>';
      }).join('') + '</div>' +
      '<ul class="leyenda">' + orden.map(function (k) { return '<li><i style="background: ' + porMat[k].c + '"></i>' + esc(k) + ' · ' + porMat[k].n + '</li>'; }).join('') + '</ul>';
  }
  function pintarTemario(T, box) {
    var nivel = box.getAttribute('data-nivel'), anios = Object.keys(T[nivel]).sort();
    var sel = box.querySelector('.anios'), cuerpo = box.querySelector('.tem-cuerpo');
    if (anios.length > 1) {
      sel.innerHTML = anios.map(function (a, i) { return '<button type="button" data-anio="' + a + '" aria-pressed="' + (i ? 'false' : 'true') + '">' + a + '.º año</button>'; }).join('');
      sel.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function () {
          sel.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
          anio(b.getAttribute('data-anio'));
        });
      });
    } else sel.remove();
    function anio(a) {
      var mats = T[nivel][a], total = mats.reduce(function (s, m) { return s + m.t.length; }, 0);
      cuerpo.innerHTML = '<p class="tem-resumen">' + mats.length + ' materias · ' + total + ' misiones</p><div class="materias">' + mats.map(function (m) {
        var corto = m.t.length > 8;
        return '<article class="mat" style="--c: ' + m.c + '"><div class="mat-cab" style="background: ' + m.c + '"><h3>' + esc(m.m) + '</h3><span>' + m.t.length + ' misiones</span></div>' +
          '<ol>' + m.t.map(function (t, i) { return '<li' + (corto && i >= 8 ? ' hidden' : '') + '>' + esc(t) + '</li>'; }).join('') + '</ol>' +
          (corto ? '<button type="button" class="mat-mas" aria-expanded="false">Ver las ' + m.t.length + ' misiones</button>' : '<div style="height: 12px"></div>') + '</article>';
      }).join('') + '</div>';
      cuerpo.querySelectorAll('.mat-mas').forEach(function (b) {
        b.addEventListener('click', function () {
          var abierto = b.getAttribute('aria-expanded') === 'true';
          b.closest('.mat').querySelectorAll('li').forEach(function (li, i) { if (i >= 8) li.hidden = abierto; });
          b.setAttribute('aria-expanded', abierto ? 'false' : 'true');
          b.textContent = abierto ? 'Ver las ' + b.closest('.mat').querySelectorAll('li').length + ' misiones' : 'Ver menos';
        });
      });
    }
    anio(anios[0]);
  }

  // ---------- Planes: precios reales desde la base (solo en la página de cada nivel) ----------
  var tabla = document.getElementById('planes-tabla');
  if (!tabla) return;
  var NIVEL = tabla.getAttribute('data-nivel');
  var estado = { pais: 'ar' };
  var datos = null;
  var MODS = [['libre', 'Libre'], ['guiada', 'Guiada'], ['completa', 'Completa']];
  var FILAS = [
    ['Programa completo: clases, material, actividades y exámenes', ['Incluido', 'Incluido', 'Incluido']],
    ['Tutor con inteligencia artificial', ['Incluido', 'Incluido', 'Incluido']],
    ['Tutorías individuales por videollamada', ['2 por mes', '4 por mes', '4 por mes']],
    ['Corrección de proyectos y escritura por el tutor', ['No', 'Incluida', 'Incluida']],
    ['Oficios', ['No', 'No', 'Talleres y trayecto']],
    ['Panel de la familia y turnos con dirección', ['Incluido', 'Incluido', 'Incluido']]
  ];
  function ars(usd) { return '$' + Math.round(usd * datos.dolar).toLocaleString('es-AR'); }
  function m$(u) { return estado.pais === 'ar' ? ars(u) + ' (USD ' + u + ')' : 'USD ' + u; }
  function pintar() {
    if (!datos) return;
    var ar = estado.pais === 'ar', precio = {};
    datos.tarifas.forEach(function (t) { if (t.nivel === NIVEL) precio[t.modalidad] = Number(t.usd); });
    var cols = MODS.filter(function (m) { return precio[m[0]] != null; });
    var head = '<tr><th scope="col" style="width: 36%"></th>' + cols.map(function (m) {
      var u = precio[m[0]];
      return '<th scope="col"><span class="plan-nombre">' + m[1] + '</span><span class="plan-precio">' + (ar ? ars(u) : 'USD ' + u) + '</span>' +
        '<span class="plan-nota">' + (ar ? 'por mes · USD ' + u : 'por mes') + '</span></th>';
    }).join('') + '</tr>';
    var body = FILAS.filter(function (f) { return !(f[0] === 'Oficios' && precio.completa == null); }).map(function (f) {
      return '<tr><th scope="row">' + f[0] + '</th>' + cols.map(function (m) {
        return '<td>' + f[1][MODS.findIndex(function (x) { return x[0] === m[0]; })] + '</td>';
      }).join('') + '</tr>';
    }).join('');
    tabla.innerHTML = '<thead>' + head + '</thead><tbody>' + body + '</tbody>';
    var mat = document.getElementById('planes-matricula');
    if (mat && datos.matricula) mat.textContent = 'Matrícula anual: ' + m$(datos.matricula) + (datos.matricula_anticipada ? '. Pagando antes de febrero: ' + m$(datos.matricula_anticipada) : '') + (ar ? '. Hasta ' + (datos.cuotas_matricula || 2) + ' cuotas.' : '.');
  }
  document.querySelectorAll('[data-pais]').forEach(function (b) {
    b.addEventListener('click', function () {
      estado.pais = b.getAttribute('data-pais');
      document.querySelectorAll('[data-pais]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      pintar();
    });
  });
  fetch(cfg.SUPABASE_URL + '/rest/v1/rpc/precios_publicos', {
    method: 'POST', headers: { apikey: cfg.SUPABASE_KEY, 'Content-Type': 'application/json' }, body: '{}'
  }).then(function (r) { return r.json(); }).then(function (d) { datos = d; pintar(); })
    .catch(function () { tabla.innerHTML = '<tbody><tr><td>No pudimos cargar los precios. Escribinos y te los pasamos.</td></tr></tbody>'; });
})();
