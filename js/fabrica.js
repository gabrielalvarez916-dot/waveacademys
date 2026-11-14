// Panel admin · Fábrica de lecciones: elegís qué lecciones arma la máquina y ves cuánto gastó cada una.
// Todo es manual: la máquina solo trabaja las lecciones que lanzás desde acá.
(function () {
  var sb = Wave.sb;
  var vista = null, timer = null;
  var B = { levels: [], grades: [], subjects: [], topics: [] };
  var E = { level: '', grade: '', subject: '', topic: '', filas: [], elegidas: {} };
  var PASOS = { contenido: 'Escribiendo la lección', consignas: 'Armando las consignas', revision: 'Revisando', correccion: 'Corrigiendo', revision2: 'Revisando de nuevo', repaso: 'Armando el repaso' };

  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function usd(n) { return 'US$ ' + Number(n || 0).toFixed(2).replace('.', ','); }
  function usd3(n) { return Number(n || 0) === 0 ? '—' : 'US$ ' + Number(n).toFixed(3).replace('.', ','); }
  function toast(texto, error) {
    var t = document.createElement('div'); t.className = 'wv-toast' + (error ? ' error' : ''); t.textContent = texto;
    document.body.appendChild(t); setTimeout(function () { t.remove(); }, 4000);
  }
  function opciones(lista, actual, vacio) {
    return '<option value="">' + vacio + '</option>' + lista.map(function (x) { return '<option value="' + esc(x.id) + '"' + (x.id === actual ? ' selected' : '') + '>' + esc(x.nombre) + '</option>'; }).join('');
  }

  async function cargarBase() {
    var r = await Promise.all([
      sb.from('levels').select('id, name, position').order('position'),
      sb.from('grades').select('id, level_id, year_number, name').order('year_number'),
      sb.from('subjects').select('id, grade_id, name, position').order('position').limit(1000),
      sb.from('topics').select('id, subject_id, title, position').order('position').limit(1000)
    ]);
    r.forEach(function (x) { if (x.error) throw x.error; });
    B.levels = r[0].data; B.grades = r[1].data; B.subjects = r[2].data; B.topics = r[3].data;
  }

  function estadoTexto(f) {
    if (!f.draft_id) return f.ficha ? '<span class="fb-tag">Sin empezar</span>' : '<span class="fb-tag fb-no">Falta la ficha</span>';
    if (f.estado === 'error') return '<span class="fb-tag fb-err" title="' + esc(f.error) + '">Error (' + f.intentos + ' intentos)</span>';
    if (f.estado === 'borrador' && f.paso === 'listo') return '<span class="fb-tag fb-ok">Lista para revisar</span>';
    return '<span class="fb-tag fb-work">' + esc(PASOS[f.paso] || f.paso) + '…</span>';
  }
  function marca(v) { return v ? '<span class="fb-si">✓</span>' : '<span class="fb-nada">—</span>'; }
  function elegible(f) { return f.ficha && (!f.draft_id || f.estado === 'error'); }

  async function resumen() {
    var r = await sb.rpc('fabrica_resumen');
    if (r.error) throw r.error;
    var s = r.data || {};
    document.getElementById('fb-resumen').innerHTML =
      '<div class="fb-card"><small>Gasto medido en total</small><b>' + usd(s.gasto_total) + '</b></div>' +
      '<div class="fb-card"><small>Promedio por lección completa</small><b>' + (Number(s.lecciones_completas_medidas) ? usd(s.promedio_completas) : '—') + '</b><span>' + (s.lecciones_completas_medidas || 0) + ' lecciones medidas</span></div>' +
      '<div class="fb-card"><small>Trabajando ahora</small><b>' + (s.en_marcha || 0) + '</b></div>' +
      '<div class="fb-card"><small>Lecciones listas sin PDF</small><b>' + (s.pdf_pendientes || 0) + '</b></div>';
    E.pdfPend = Number(s.pdf_pendientes) || 0;
  }

  async function lecciones() {
    var cont = document.getElementById('fb-tabla');
    if (!E.topic) { cont.innerHTML = '<div class="wv-vacio">Elegí un tema para ver sus lecciones.</div>'; return; }
    var r = await sb.rpc('fabrica_panel', { p_topic_id: E.topic });
    if (r.error) throw r.error;
    E.filas = r.data || [];
    var trabajando = E.filas.some(function (f) { return f.estado === 'en_cola' || f.estado === 'generando'; });
    clearTimeout(timer);
    if (trabajando) timer = setTimeout(function () { if (document.getElementById('fb-tabla')) refrescar(); }, 20000);
    if (!E.filas.length) { cont.innerHTML = '<div class="wv-vacio">Este tema todavía no tiene lecciones.</div>'; return; }
    cont.innerHTML = '<table class="fb-t"><thead><tr><th></th><th>Lección</th><th>Estado</th><th>Consignas</th><th>Repaso</th><th>PDF</th><th>Gasto</th></tr></thead><tbody>' +
      E.filas.map(function (f) {
        var puede = elegible(f);
        return '<tr><td>' + (puede ? '<input type="checkbox" data-el="' + f.id + '"' + (E.elegidas[f.id] ? ' checked' : '') + '>' : '') + '</td>' +
          '<td><b>' + esc(f.posicion) + '.</b> ' + esc(f.titulo) + (f.publicada ? ' <span class="fb-tag fb-ok">Publicada</span>' : '') + '</td>' +
          '<td>' + estadoTexto(f) + '</td><td>' + marca(f.consignas_cargadas) + '</td><td>' + marca(f.repaso_cargado) + '</td><td>' + marca(f.pdf) + '</td>' +
          '<td title="' + (f.tokens_in || 0) + ' tokens de entrada, ' + (f.tokens_out || 0) + ' de salida, ' + (f.llamadas || 0) + ' llamadas">' + usd3(f.costo_usd) + '</td></tr>';
      }).join('') + '</tbody></table>';
    contar();
  }

  function contar() {
    var n = Object.keys(E.elegidas).filter(function (k) { return E.elegidas[k]; }).length;
    var b = document.getElementById('fb-lanzar');
    if (b) { b.disabled = !n; b.textContent = n ? 'Generar ' + n + (n === 1 ? ' lección' : ' lecciones') : 'Generar las seleccionadas'; }
  }

  async function refrescar() { try { await Promise.all([resumen(), lecciones()]); } catch (e) { toast('No se pudo actualizar: ' + (e.message || e), true); } }

  async function lanzar() {
    var ids = Object.keys(E.elegidas).filter(function (k) { return E.elegidas[k]; });
    if (!ids.length) return;
    if (ids.length > 10) return toast('Elegí hasta 10 lecciones por vez.', true);
    var s = (await sb.rpc('fabrica_resumen')).data || {};
    var aprox = Number(s.lecciones_completas_medidas) ? ' Según lo medido hasta ahora, cada lección cuesta cerca de ' + usd(s.promedio_completas) + '.' : ' Todavía no hay un promedio medido.';
    if (!confirm('Vas a mandar ' + ids.length + (ids.length === 1 ? ' lección' : ' lecciones') + ' a la máquina. Cada una usa la IA y se cobra de tu saldo de Anthropic.' + aprox + '\n\n¿Seguimos?')) return;
    var b = document.getElementById('fb-lanzar'); b.disabled = true;
    var r = await sb.rpc('fabrica_lanzar', { p_lesson_ids: ids });
    if (r.error) { toast(r.error.message || 'No se pudo lanzar', true); return contar(); }
    E.elegidas = {};
    var d = r.data || {};
    toast('Lanzadas: ' + d.lanzadas + (d.sin_ficha ? ' · sin ficha: ' + d.sin_ficha : '') + (d.ya_hechas_o_en_marcha ? ' · ya hechas o en marcha: ' + d.ya_hechas_o_en_marcha : ''));
    setTimeout(refrescar, 1500);
  }

  function pintarFiltros() {
    var grados = B.grades.filter(function (g) { return !E.level || g.level_id === E.level; });
    var mats = B.subjects.filter(function (m) { return E.grade && m.grade_id === E.grade; });
    var temas = B.topics.filter(function (t) { return E.subject && t.subject_id === E.subject; });
    document.getElementById('fb-sel').innerHTML =
      '<select id="fb-nivel">' + opciones(B.levels.map(function (x) { return { id: x.id, nombre: x.name }; }), E.level, 'Nivel') + '</select>' +
      '<select id="fb-grado">' + opciones(grados.map(function (x) { return { id: x.id, nombre: x.name || (x.year_number + '.º año') }; }), E.grade, 'Año') + '</select>' +
      '<select id="fb-materia">' + opciones(mats.map(function (x) { return { id: x.id, nombre: x.name }; }), E.subject, 'Materia') + '</select>' +
      '<select id="fb-tema">' + opciones(temas.map(function (x) { return { id: x.id, nombre: x.position + '. ' + x.title }; }), E.topic, 'Tema') + '</select>';
  }

  async function abrir(el) {
    vista = el; clearTimeout(timer);
    vista.innerHTML = '<h1 class="wv-titulo">Fábrica de lecciones</h1>' +
      '<p class="fb-ayuda">Elegí las lecciones que querés que arme la máquina. <b>No hace nada por su cuenta</b>: solo trabaja las que marcás acá. Cada una pasa sola por todo el proceso: borrador, revisión, actividad con consignas, repaso y PDF. Usa la IA y se cobra de tu saldo de Anthropic; el gasto que ves es el medido por la propia máquina, para que lo compares con tu saldo.</p>' +
      '<div id="fb-resumen" class="fb-resumen"></div><div id="fb-sel" class="fb-sel"></div>' +
      '<div class="fb-barra"><button id="fb-lanzar" class="wv-btn" type="button" disabled>Generar las seleccionadas</button><button id="fb-act" class="wv-chip" type="button">Actualizar</button></div>' +
      '<div id="fb-tabla"></div>';
    await cargarBase();
    pintarFiltros();
    vista.onchange = function (ev) {
      var t = ev.target;
      if (t.id === 'fb-nivel') { E.level = t.value; E.grade = E.subject = E.topic = ''; E.elegidas = {}; pintarFiltros(); lecciones().catch(function (e) { toast(e.message, true); }); }
      else if (t.id === 'fb-grado') { E.grade = t.value; E.subject = E.topic = ''; E.elegidas = {}; pintarFiltros(); lecciones().catch(function (e) { toast(e.message, true); }); }
      else if (t.id === 'fb-materia') { E.subject = t.value; E.topic = ''; E.elegidas = {}; pintarFiltros(); lecciones().catch(function (e) { toast(e.message, true); }); }
      else if (t.id === 'fb-tema') { E.topic = t.value; E.elegidas = {}; lecciones().catch(function (e) { toast(e.message, true); }); }
      else if (t.dataset && t.dataset.el) { E.elegidas[t.dataset.el] = t.checked; contar(); }
    };
    vista.onclick = function (ev) {
      var t = ev.target.closest('button'); if (!t) return;
      if (t.id === 'fb-lanzar') lanzar().catch(function (e) { toast(e.message || e, true); });
      if (t.id === 'fb-act') refrescar();
    };
    await refrescar();
  }

  window.WaveFabrica = { abrir: abrir };
})();
