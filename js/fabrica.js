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
    if (f.estado === 'borrador' && f.paso === 'listo' && f.interactiva_estado === 'generando') return '<span class="fb-tag fb-work">Armando el juego interactivo…</span>';
    if (f.estado === 'borrador' && f.paso === 'listo' && f.interactiva_estado === 'error') return '<span class="fb-tag fb-err" title="' + esc(f.interactiva_error) + '">Falló el juego interactivo</span>';
    if (f.estado === 'borrador' && f.paso === 'listo') return '<span class="fb-tag fb-ok">Lista para revisar</span>';
    return '<span class="fb-tag fb-work">' + esc(PASOS[f.paso] || f.paso) + '…</span>';
  }
  function marca(v) { return v ? '<span class="fb-si">✓</span>' : '<span class="fb-nada">—</span>'; }
  function elegible(f) { return f.ficha && (!f.draft_id || f.estado === 'error'); }
  function sinJuego(f) { return f.draft_id && f.estado === 'borrador' && f.paso === 'listo' && !f.interactiva && f.interactiva_estado !== 'generando'; }
  function idsElegidos(filtro) { return (E.filas || []).filter(function (f) { return E.elegidas[f.id] && filtro(f); }).map(function (f) { return f.id; }); }

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
    var lt = await sb.rpc('fabrica_lotes_estado');
    if (!lt.error && lt.data && Number(lt.data.lotes)) {
      document.getElementById('fb-resumen').insertAdjacentHTML('beforeend', '<div class="fb-card"><small>Esperando en lote</small><b>' + lt.data.lecciones + '</b><span>Anthropic los devuelve en minutos u horas; se siguen solos</span></div>');
    }
  }

  async function lecciones() {
    var cont = document.getElementById('fb-tabla');
    if (!E.topic) { cont.innerHTML = '<div class="wv-vacio">Elegí un tema para ver sus lecciones.</div>'; return; }
    var r = await sb.rpc('fabrica_panel', { p_topic_id: E.topic });
    if (r.error) throw r.error;
    E.filas = r.data || [];
    var trabajando = E.filas.some(function (f) { return f.estado === 'en_cola' || f.estado === 'generando' || f.interactiva_estado === 'generando'; });
    clearTimeout(timer);
    if (trabajando) timer = setTimeout(function () { if (document.getElementById('fb-tabla')) refrescar(); }, 20000);
    if (!E.filas.length) { cont.innerHTML = '<div class="wv-vacio">Este tema todavía no tiene lecciones.</div>'; return; }
    cont.innerHTML = '<table class="fb-t"><thead><tr><th></th><th>Lección</th><th>Estado</th><th>Consignas</th><th>Repaso</th><th>Interactiva</th><th>PDF</th><th>Gasto</th></tr></thead><tbody>' +
      E.filas.map(function (f) {
        var puede = elegible(f) || sinJuego(f);
        return '<tr><td>' + (puede ? '<input type="checkbox" data-el="' + f.id + '"' + (E.elegidas[f.id] ? ' checked' : '') + '>' : '') + '</td>' +
          '<td><b>' + esc(f.posicion) + '.</b> ' + esc(f.titulo) + (f.publicada ? ' <span class="fb-tag fb-ok">Publicada</span>' : '') + '</td>' +
          '<td>' + estadoTexto(f) + '</td><td>' + marca(f.consignas_cargadas) + '</td><td>' + marca(f.repaso_cargado) + '</td><td>' + marca(f.interactiva) + '</td><td>' + marca(f.pdf) + '</td>' +
          '<td title="' + (f.tokens_in || 0) + ' tokens de entrada, ' + (f.tokens_out || 0) + ' de salida, ' + (f.llamadas || 0) + ' llamadas">' + usd3(f.costo_usd) + '</td></tr>';
      }).join('') + '</tbody></table>';
    contar();
  }

  function contar() {
    var n = idsElegidos(elegible).length, j = idsElegidos(sinJuego).length;
    var b = document.getElementById('fb-lanzar');
    if (b) { b.disabled = !n; b.textContent = n ? 'Generar ' + n + (n === 1 ? ' lección' : ' lecciones') : 'Generar las seleccionadas'; }
    var bl = document.getElementById('fb-lote');
    if (bl) { bl.disabled = !n; bl.textContent = n ? 'Enviar lote de ' + n + (n === 1 ? ' lección' : ' lecciones') + ' (mitad de precio)' : 'Enviar lote (mitad de precio)'; }
    var bj = document.getElementById('fb-juego');
    if (bj) { bj.disabled = !j; bj.textContent = j ? 'Armar juego interactivo de ' + j + (j === 1 ? ' lección' : ' lecciones') : 'Armar juego interactivo'; }
  }

  var BUCKET = 'lesson-images';
  var TIPO_IMG = { mapa: 'Mapa', foto: 'Foto', ilustracion: 'Ilustración', diagrama: 'Diagrama', esquema: 'Esquema', grafico: 'Gráfico', linea_de_tiempo: 'Línea de tiempo', figura_geometrica: 'Figura', obra_de_arte: 'Obra de arte', otro: 'Imagen' };

  // Imágenes que pidió la máquina en cada lección: se carga la imagen y el PDF se rearma solo
  async function imagenes() {
    var cont = document.getElementById('fb-imagenes'); if (!cont) return;
    if (!E.topic) { cont.innerHTML = ''; return; }
    var r = await sb.rpc('fabrica_imagenes', { p_topic_id: E.topic });
    if (r.error) throw r.error;
    var lista = r.data || [];
    var titulo = '<h2 class="fb-h2">Imágenes de las lecciones</h2>';
    if (!lista.length) { cont.innerHTML = titulo + '<div class="wv-vacio">Ninguna lección lista de este tema pide imágenes.</div>'; return; }
    var paths = [];
    lista.forEach(function (l) { (l.imagenes || []).forEach(function (im) { if (im.path) paths.push(im.path); }); });
    var urls = {};
    if (paths.length) {
      var sg = await sb.storage.from(BUCKET).createSignedUrls(paths, 3600);
      (sg.data || []).forEach(function (x) { if (x.signedUrl) urls[x.path] = x.signedUrl; });
    }
    var total = 0, faltan = 0;
    var html = lista.map(function (l) {
      return '<div class="fb-lec"><h3>Lección ' + esc(l.posicion) + ' · ' + esc(l.titulo) + (l.publicada ? ' <span class="fb-tag fb-no">Publicada: su PDF no se toca</span>' : '') + '</h3>' +
        (l.imagenes || []).map(function (im) {
          total++; if (!im.path) faltan++;
          var datos = 'data-d="' + esc(l.draft_id) + '" data-s="' + im.sec + '" data-b="' + im.bloque + '" data-p="' + esc(im.path || '') + '"';
          return '<div class="fb-img">' +
            '<div class="fb-img-txt"><b>' + esc(TIPO_IMG[im.tipo] || 'Imagen') + (im.titulo ? ': ' + esc(im.titulo) : '') + '</b>' +
            '<p><b>Qué tiene que mostrar:</b> ' + esc(im.descripcion) + '</p>' +
            (im.fuente ? '<p><b>Dónde conseguirla:</b> ' + esc(im.fuente) + '</p>' : '') +
            (im.pie ? '<p class="fb-img-pie">Pie: ' + esc(im.pie) + '</p>' : '') + '</div>' +
            '<div class="fb-img-acc">' +
              (im.path && urls[im.path] ? '<img class="fb-img-vista" src="' + esc(urls[im.path]) + '" alt="Imagen cargada">' : '<div class="fb-img-falta">Falta la imagen</div>') +
              '<label class="wv-chip fb-img-subir">' + (im.path ? 'Cambiar imagen' : 'Cargar imagen') + '<input type="file" class="fb-file" accept="image/png,image/jpeg" hidden ' + datos + '></label>' +
              (im.path ? '<button type="button" class="wv-chip fb-img-quitar" ' + datos + '>Quitar</button>' : '') +
            '</div></div>';
        }).join('') + '</div>';
    }).join('');
    cont.innerHTML = titulo + '<p class="fb-ayuda">Cargá una imagen PNG o JPG (hasta 5 MB) por cada recuadro. Al cargarla, el PDF de la lección se rearma solo en unos minutos y la imagen aparece en el lugar que pidió la máquina. ' + faltan + ' de ' + total + ' todavía sin imagen.</p>' + html;
  }

  function avisoImagen(d) {
    if (d && d.rearma_pdf) toast('Listo. El PDF se rearma solo en unos minutos.');
    else if (d && d.publicada) toast('Imagen guardada. La lección ya está publicada, así que su PDF no se modificó.');
    else toast('Listo.');
  }

  async function subirImagen(inp) {
    var f = inp.files && inp.files[0]; if (!f) return;
    if (!/^image\/(png|jpeg)$/.test(f.type)) { inp.value = ''; return toast('La imagen tiene que ser PNG o JPG.', true); }
    if (f.size > 5 * 1024 * 1024) { inp.value = ''; return toast('La imagen pesa más de 5 MB.', true); }
    var d = inp.dataset, ext = f.type === 'image/png' ? 'png' : 'jpg';
    var path = d.d + '/' + d.s + '-' + d.b + '-' + Date.now() + '.' + ext;
    var up = await sb.storage.from(BUCKET).upload(path, f, { contentType: f.type });
    if (up.error) throw up.error;
    var g = await sb.rpc('fabrica_imagen_guardar', { p_draft: d.d, p_sec: Number(d.s), p_bloque: Number(d.b), p_path: path });
    if (g.error) { await sb.storage.from(BUCKET).remove([path]); throw g.error; }
    if (g.data && g.data.anterior) sb.storage.from(BUCKET).remove([g.data.anterior]);
    avisoImagen(g.data);
    await Promise.all([imagenes(), lecciones(), resumen()]);
  }

  async function quitarImagen(btn) {
    var d = btn.dataset;
    if (!confirm('¿Quitar esta imagen? El PDF se va a rearmar sin ella.')) return;
    var g = await sb.rpc('fabrica_imagen_quitar', { p_draft: d.d, p_sec: Number(d.s), p_bloque: Number(d.b) });
    if (g.error) throw g.error;
    if (g.data && g.data.anterior) sb.storage.from(BUCKET).remove([g.data.anterior]);
    avisoImagen(g.data);
    await Promise.all([imagenes(), lecciones(), resumen()]);
  }

  async function refrescar() { try { await Promise.all([resumen(), lecciones(), imagenes()]); } catch (e) { toast('No se pudo actualizar: ' + (e.message || e), true); } }

  async function lanzar() {
    var ids = idsElegidos(elegible);
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

  var COSTO_LOTE_APROX = 0.3; // USD por lección en lote: estimación hasta tener el primer lote medido

  async function lote() {
    var ids = idsElegidos(elegible);
    if (!ids.length) return;
    var s = (await sb.rpc('fabrica_resumen')).data || {};
    var aprox = ids.length * COSTO_LOTE_APROX;
    if (!confirm('Vas a enviar un LOTE de ' + ids.length + (ids.length === 1 ? ' lección' : ' lecciones') + '.\n\nEl lote se cobra a mitad de precio, pero tarda: Anthropic lo devuelve en minutos u horas (hasta 24). Una vez enviado sigue solo, etapa por etapa, hasta dejar los borradores listos. No publica nada ni arma el juego interactivo.\n\nCosto estimado: unos ' + usd(aprox) + ' en total (estimación; el primer lote sirve para medir el costo real). Se cobra de tu saldo de Anthropic.\n\n¿Enviamos?')) return;
    var b = document.getElementById('fb-lote'); b.disabled = true;
    var r = await sb.rpc('fabrica_lote_enviar', { p_lesson_ids: ids });
    if (r.error) { toast(r.error.message || 'No se pudo enviar el lote', true); return contar(); }
    E.elegidas = {};
    var d = r.data || {};
    toast('Lote enviado: ' + d.enviadas + (d.sin_ficha ? ' · sin ficha: ' + d.sin_ficha : '') + (d.ya_hechas_o_en_marcha ? ' · ya hechas o en marcha: ' + d.ya_hechas_o_en_marcha : '') + '. Los resultados aparecen solos.');
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

  async function juego() {
    var ids = idsElegidos(sinJuego);
    if (!ids.length) return;
    if (ids.length > 10) return toast('Elegí hasta 10 lecciones por vez.', true);
    if (!confirm('Vas a pedir el juego interactivo de ' + ids.length + (ids.length === 1 ? ' lección' : ' lecciones') + '. Usa la IA (dos llamadas por lección, un guion y su revisión) y se cobra de tu saldo de Anthropic.\n\nEl juego queda cargado sin publicar.\n\n¿Seguimos?')) return;
    var bj = document.getElementById('fb-juego'); bj.disabled = true;
    var r = await sb.rpc('fabrica_pedir_interactiva', { p_lesson_ids: ids });
    if (r.error) { toast(r.error.message || 'No se pudo pedir', true); return contar(); }
    E.elegidas = {};
    toast('Pedidos: ' + ((r.data || {}).pedidas || 0));
    setTimeout(refrescar, 1500);
  }

  async function abrir(el) {
    vista = el; clearTimeout(timer);
    vista.innerHTML = '<h1 class="wv-titulo">Fábrica de lecciones</h1>' +
      '<p class="fb-ayuda">Elegí las lecciones que querés que arme la máquina. <b>No hace nada por su cuenta</b>: solo trabaja las que marcás acá. Podés generarlas ya (precio completo) o enviarlas en lote (mitad de precio, tarda minutos u horas). Cada una pasa sola por todo el proceso: borrador, revisión, actividad con consignas, repaso, juego interactivo y PDF. Usa la IA y se cobra de tu saldo de Anthropic; el gasto que ves es el medido por la propia máquina, para que lo compares con tu saldo.</p>' +
      '<div id="fb-resumen" class="fb-resumen"></div><div id="fb-sel" class="fb-sel"></div>' +
      '<div class="fb-barra"><button id="fb-lanzar" class="wv-btn" type="button" disabled>Generar las seleccionadas</button><button id="fb-lote" class="wv-btn" type="button" disabled>Enviar lote (mitad de precio)</button><button id="fb-juego" class="wv-chip" type="button" disabled>Armar juego interactivo</button><button id="fb-act" class="wv-chip" type="button">Actualizar</button></div>' +
      '<div id="fb-tabla"></div><div id="fb-imagenes"></div>';
    await cargarBase();
    pintarFiltros();
    vista.onchange = function (ev) {
      var t = ev.target;
      if (t.id === 'fb-nivel') { E.level = t.value; E.grade = E.subject = E.topic = ''; E.elegidas = {}; pintarFiltros(); lecciones().then(imagenes).catch(function (e) { toast(e.message, true); }); }
      else if (t.id === 'fb-grado') { E.grade = t.value; E.subject = E.topic = ''; E.elegidas = {}; pintarFiltros(); lecciones().then(imagenes).catch(function (e) { toast(e.message, true); }); }
      else if (t.id === 'fb-materia') { E.subject = t.value; E.topic = ''; E.elegidas = {}; pintarFiltros(); lecciones().then(imagenes).catch(function (e) { toast(e.message, true); }); }
      else if (t.id === 'fb-tema') { E.topic = t.value; E.elegidas = {}; lecciones().then(imagenes).catch(function (e) { toast(e.message, true); }); }
      else if (t.classList && t.classList.contains('fb-file')) { subirImagen(t).catch(function (e) { toast(e.message || e, true); }); }
      else if (t.dataset && t.dataset.el) { E.elegidas[t.dataset.el] = t.checked; contar(); }
    };
    vista.onclick = function (ev) {
      var t = ev.target.closest('button'); if (!t) return;
      if (t.id === 'fb-lanzar') lanzar().catch(function (e) { toast(e.message || e, true); });
      if (t.id === 'fb-lote') lote().catch(function (e) { toast(e.message || e, true); });
      if (t.id === 'fb-juego') juego().catch(function (e) { toast(e.message || e, true); });
      if (t.id === 'fb-act') refrescar();
      if (t.classList.contains('fb-img-quitar')) quitarImagen(t).catch(function (e) { toast(e.message || e, true); });
    };
    await refrescar();
  }

  window.WaveFabrica = { abrir: abrir };
})();
