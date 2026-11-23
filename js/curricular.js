// Panel admin · Diseño curricular: todo el mapa (temas y lecciones) ordenado por nivel, año y materia.
// Es solo lectura: se alimenta de la tabla mapa_curricular, que es la copia guardada del diseño.
(function () {
  var sb = Wave.sb;
  var vista = null;
  var B = null; // { levels, grades, subjects, filas }
  var E = { level: '', grade: '', q: '', rel: '' };

  var REL = {
    Nuevo: { cls: 'nuevo', ayuda: 'Contenido que aparece por primera vez' },
    Retoma: { cls: 'retoma', ayuda: 'Vuelve sobre algo ya visto en un año anterior' },
    Profundiza: { cls: 'prof', ayuda: 'Amplía algo ya visto, con más exigencia' }
  };

  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function norm(t) { return String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function nombreGrado(g) { return g.name || (g.year_number + '.º año'); }

  // Supabase entrega como máximo 1000 filas por pedido: se pide por tandas hasta traer todo el mapa.
  async function traerMapa() {
    var todo = [], desde = 0, paso = 1000;
    for (;;) {
      var x = await sb.from('mapa_curricular_completo').select('subject_id, posicion, tema, que_se_trabaja, relacion, lecciones, nota')
        .order('subject_id').order('posicion').range(desde, desde + paso - 1);
      if (x.error) throw x.error;
      todo = todo.concat(x.data);
      if (x.data.length < paso) break;
      desde += paso;
    }
    return todo;
  }

  async function cargar() {
    var r = await Promise.all([
      sb.from('levels').select('id, name, position').order('position'),
      sb.from('grades').select('id, level_id, year_number, name').order('year_number'),
      sb.from('subjects').select('id, grade_id, name, position').order('position').limit(1000),
      traerMapa()
    ]);
    r.slice(0, 3).forEach(function (x) { if (x.error) throw x.error; });
    var porMateria = {};
    r[3].forEach(function (f) { (porMateria[f.subject_id] = porMateria[f.subject_id] || []).push(f); });
    B = { levels: r[0].data, grades: r[1].data, subjects: r[2].data, porMateria: porMateria };
    if (!E.level && B.levels.length) E.level = B.levels[0].id;
  }

  function gradosDelNivel() { return B.grades.filter(function (g) { return g.level_id === E.level; }); }

  function coincide(f) {
    if (E.rel && f.relacion !== E.rel) return false;
    if (!E.q) return true;
    var texto = norm([f.tema, f.que_se_trabaja, f.nota, (f.lecciones || []).join(' ')].join(' '));
    return E.q.split(/\s+/).every(function (p) { return texto.indexOf(p) !== -1; });
  }

  function barraRel(filas) {
    var n = { Nuevo: 0, Retoma: 0, Profundiza: 0 };
    filas.forEach(function (f) { if (n[f.relacion] != null) n[f.relacion]++; });
    var t = filas.length || 1;
    return '<span class="dc-barra" title="Nuevo ' + n.Nuevo + ' · Retoma ' + n.Retoma + ' · Profundiza ' + n.Profundiza + '">' +
      ['Nuevo', 'Retoma', 'Profundiza'].map(function (k) { return '<i class="dc-' + REL[k].cls + '" style="width:' + (n[k] * 100 / t) + '%"></i>'; }).join('') + '</span>';
  }

  function tema(f) {
    var rel = REL[f.relacion] || { cls: 'nuevo', ayuda: '' };
    return '<li class="dc-tema">' +
      '<div class="dc-num">' + esc(f.posicion) + '</div>' +
      '<div class="dc-cuerpo">' +
        '<div class="dc-fila1"><b class="dc-nombre">' + esc(f.tema) + '</b><span class="dc-pill dc-' + rel.cls + '" title="' + esc(rel.ayuda) + '">' + esc(f.relacion) + '</span></div>' +
        '<div class="dc-que">' + esc(f.que_se_trabaja) + '</div>' +
        '<ol class="dc-lecs">' + (f.lecciones || []).map(function (l) { return '<li>' + esc(l) + '</li>'; }).join('') + '</ol>' +
        (f.nota ? '<div class="dc-nota">' + esc(f.nota) + '</div>' : '') +
      '</div></li>';
  }

  function materia(m, filas, abierta) {
    var todas = filas.length, vistas = filas.filter(coincide);
    var lecs = filas.reduce(function (a, f) { return a + (f.lecciones ? f.lecciones.length : 0); }, 0);
    if (!vistas.length) return '';
    return '<details class="dc-mat"' + (abierta ? ' open' : '') + '>' +
      '<summary><span class="dc-mat-nombre">' + esc(m.name) + '</span>' +
      '<span class="dc-mat-dato">' + todas + ' temas · ' + lecs + ' lecciones' + (vistas.length !== todas ? ' · ' + vistas.length + ' coinciden' : '') + '</span>' +
      barraRel(filas) + '</summary>' +
      '<ul class="dc-temas">' + vistas.map(tema).join('') + '</ul></details>';
  }

  function pintar() {
    var cab = '<div class="dc-cab"><div><h1 class="wv-titulo">Diseño curricular</h1>' +
      '<p class="wv-sub">Cada año con sus materias, temas y lecciones. Es la copia guardada del mapa: lo que ves acá es lo que se carga en la plataforma.</p></div>' +
      '<button type="button" class="wv-btn suave" id="dc-imprimir">Imprimir o guardar PDF</button></div>';

    var niveles = '<div class="wv-filtros dc-niveles">' + B.levels.map(function (n) {
      return '<button type="button" class="wv-chip' + (n.id === E.level ? ' on' : '') + '" data-nivel="' + esc(n.id) + '">' + esc(n.name) + '</button>';
    }).join('') + '</div>';

    var grados = gradosDelNivel();
    if (!grados.some(function (g) { return g.id === E.grade; })) E.grade = grados.length ? grados[0].id : '';
    var anios = grados.length > 1 ? '<div class="wv-filtros dc-anios">' + grados.map(function (g) {
      return '<button type="button" class="wv-chip' + (g.id === E.grade ? ' on' : '') + '" data-grado="' + esc(g.id) + '">' + esc(nombreGrado(g)) + '</button>';
    }).join('') + '</div>' : '';

    var herr = '<div class="wv-tools dc-tools"><input id="dc-q" class="wv-buscar" type="search" placeholder="Buscar un tema, una lección o un contenido…" value="' + esc(E.qCrudo || '') + '">' +
      '<div class="wv-filtros">' + ['', 'Nuevo', 'Retoma', 'Profundiza'].map(function (k) {
        return '<button type="button" class="wv-chip' + (E.rel === k ? ' on' : '') + '" data-rel="' + k + '">' + (k || 'Todos') + '</button>';
      }).join('') + '</div>' +
      '<button type="button" class="wv-btn mini suave" id="dc-abrir">Abrir todo</button><button type="button" class="wv-btn mini suave" id="dc-cerrar">Cerrar todo</button></div>';

    var materias = B.subjects.filter(function (m) { return m.grade_id === E.grade; });
    var conMapa = materias.filter(function (m) { return B.porMateria[m.id]; });
    var sinMapa = materias.filter(function (m) { return !B.porMateria[m.id]; });
    var totT = 0, totL = 0;
    conMapa.forEach(function (m) { var f = B.porMateria[m.id]; totT += f.length; f.forEach(function (x) { totL += x.lecciones ? x.lecciones.length : 0; }); });

    var grado = B.grades.filter(function (g) { return g.id === E.grade; })[0];
    var resumen = '<div class="dc-resumen"><div><small>Año</small><b>' + esc(grado ? nombreGrado(grado) : '—') + '</b></div>' +
      '<div><small>Materias con mapa</small><b>' + conMapa.length + ' de ' + materias.length + '</b></div>' +
      '<div><small>Temas</small><b>' + totT + '</b></div><div><small>Lecciones</small><b>' + totL + '</b></div></div>';

    var hayBusqueda = !!(E.q || E.rel);
    var cuerpo = conMapa.map(function (m) { return materia(m, B.porMateria[m.id], hayBusqueda || conMapa.length === 1); }).join('');
    if (!cuerpo) cuerpo = '<div class="wv-vacio">' + (conMapa.length ? 'No hay temas que coincidan con la búsqueda.' : 'Este año todavía no tiene ninguna materia con mapa.') + '</div>';

    var pend = sinMapa.length ? '<div class="dc-pend"><b>Todavía sin mapa</b>' + sinMapa.map(function (m) { return '<span>' + esc(m.name) + '</span>'; }).join('') + '</div>' : '';

    var leyenda = '<div class="dc-leyenda">' + Object.keys(REL).map(function (k) {
      return '<span><i class="dc-pill dc-' + REL[k].cls + '">' + k + '</i> ' + esc(REL[k].ayuda) + '</span>';
    }).join('') + '</div>';

    vista.innerHTML = cab + niveles + anios + herr + resumen + leyenda + '<div id="dc-lista">' + cuerpo + '</div>' + pend;
    enlazar();
  }

  function enlazar() {
    vista.querySelectorAll('[data-nivel]').forEach(function (b) { b.onclick = function () { E.level = b.getAttribute('data-nivel'); E.grade = ''; pintar(); }; });
    vista.querySelectorAll('[data-grado]').forEach(function (b) { b.onclick = function () { E.grade = b.getAttribute('data-grado'); pintar(); }; });
    vista.querySelectorAll('[data-rel]').forEach(function (b) { b.onclick = function () { E.rel = b.getAttribute('data-rel'); pintar(); }; });
    var q = document.getElementById('dc-q'), t = null;
    q.oninput = function () {
      E.qCrudo = q.value;
      clearTimeout(t);
      t = setTimeout(function () {
        E.q = norm(E.qCrudo).trim();
        var pos = q.selectionStart;
        pintar();
        var n = document.getElementById('dc-q'); n.focus(); try { n.setSelectionRange(pos, pos); } catch (e) { /* sin selección */ }
      }, 220);
    };
    document.getElementById('dc-abrir').onclick = function () { vista.querySelectorAll('.dc-mat').forEach(function (d) { d.open = true; }); };
    document.getElementById('dc-cerrar').onclick = function () { vista.querySelectorAll('.dc-mat').forEach(function (d) { d.open = false; }); };
    document.getElementById('dc-imprimir').onclick = function () {
      vista.querySelectorAll('.dc-mat').forEach(function (d) { d.open = true; });
      window.print();
    };
  }

  async function abrir(el) {
    vista = el;
    vista.innerHTML = '<div class="wv-vacio">Cargando el diseño curricular…</div>';
    if (!B) await cargar();
    pintar();
  }

  window.WaveCurricular = { abrir: abrir, recargar: function () { B = null; } };
})();
