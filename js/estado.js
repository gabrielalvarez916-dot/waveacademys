/* Estado de envíos: GitHub (corridas) + base (misiones). Solo lectura. */
(function () {
  var REPO = 'gabrielalvarez916-dot/waveacademys';
  var T = null, CACHE = {}, PEND = null, PENDERR = '', PENDCARGANDO = false;
  var AYUDA = { 'Cargar borradores, actividades y examen': 'La base tardó demasiado o rechazó la carga de la misión. Suele pasar si la base está ocupada: reenviar.', 'Control de calidad': 'El contenido no pasó el control de calidad: hay que corregir la misión.', 'Generar PDFs': 'Falló el armado de PDF.', 'Publicar': 'Falló la publicación.' };
  async function motivo(r, runs) {
    if (r.conclusion === 'cancelled') {
      var sig = runs.filter(function (x) { return x.name === r.name && new Date(x.created_at) > new Date(r.created_at); }).sort(function (a, b) { return new Date(a.created_at) - new Date(b.created_at); })[0];
      return sig ? 'Entró una corrida más nueva (n.º ' + sig.run_number + ') y GitHub descartó esta; su trabajo lo hace la nueva.' : 'GitHub la canceló y no hay otra posterior: revisar.';
    }
    if (r.conclusion !== 'failure' && r.conclusion !== 'timed_out') return '';
    if (CACHE[r.id] != null) return CACHE[r.id];
    var txt = 'Falló (no pude ver el paso).';
    try {
      var j = await (await fetch('https://api.github.com/repos/' + REPO + '/actions/runs/' + r.id + '/jobs')).json();
      var paso = ''; (j.jobs || []).forEach(function (jb) { (jb.steps || []).forEach(function (st) { if (!paso && st.conclusion === 'failure') paso = st.name; }); });
      if (paso) txt = 'Falló en el paso «' + paso + '». ' + (AYUDA[paso] || '');
      CACHE[r.id] = txt;
    } catch (e) { }
    return txt;
  }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function hace(f) { var m = Math.round((Date.now() - new Date(f)) / 60000); return m < 1 ? 'recién' : m < 60 ? 'hace ' + m + ' min' : m < 1440 ? 'hace ' + Math.round(m / 60) + ' h' : 'hace ' + Math.round(m / 1440) + ' d'; }
  function estadoRun(r, runs) {
    if (r.status === 'in_progress') return ['En curso', 'amar'];
    if (r.status === 'queued' || r.status === 'waiting' || r.status === 'pending') return ['En espera', 'amar'];
    if (r.conclusion === 'success') return ['Hecho', 'verde'];
    if (r.conclusion === 'cancelled') {
      var sig = (runs || []).some(function (x) { return x.name === r.name && x.conclusion === 'success' && new Date(x.created_at) > new Date(r.created_at); });
      return sig ? ['Reemplazada por una más nueva ✔', 'verde'] : ['Cancelado (revisar)', 'rojo'];
    }
    if (r.conclusion === 'failure') return ['Falló', 'rojo'];
    return [r.conclusion || r.status, 'gris'];
  }
  function tipo(n) { n = n || ''; return /voz/i.test(n) ? 'Voces' : /avanzado/i.test(n) ? 'Misiones Avanzado' : /medio/i.test(n) ? 'Misiones Medio' : /pdf/i.test(n) ? 'PDF' : n; }
  function chip(t, c) { return '<span class="est-chip est-' + c + '">' + esc(t) + '</span>'; }
  async function pendientes(el, forzar) {
    if (PENDCARGANDO || (PEND && !forzar)) return;
    PENDCARGANDO = true;
    try {
      var r = await Wave.sb.functions.invoke('enviar-mision', { body: { accion: 'pendientes' } });
      PEND = (r.data && r.data.pendientes) || null; PENDERR = (r.data && r.data.error) || (r.error && 'No pude leer lo pendiente') || '';
    } catch (e) { PENDERR = 'No pude leer lo pendiente'; }
    PENDCARGANDO = false; cargar(el);
  }
  function cajaEnviar(runs) {
    var h = '<div class="est-env"><h3>📤 Para enviar' + (PEND ? ' (' + PEND.length + ')' : '') + '</h3>';
    if (PENDERR) h += '<p class="est-err">' + esc(PENDERR) + '</p>';
    if (PEND == null && !PENDERR) h += '<p>Buscando lo que está subido a GitHub y todavía no se cargó…</p>';
    if (PEND && !PEND.length) h += '<p>Todo lo subido ya está cargado. ✔</p>';
    if (PEND && PEND.length) {
      h += '<p><small>Subido a GitHub, pero sin examen cargado en la base. Marcá lo que querés mandar. Ya no se manda solo.</small></p><table class="est-t"><thead><tr><th></th><th>Nivel</th><th>Materia</th><th>Misión</th></tr></thead><tbody>' +
        PEND.map(function (p, i) { return '<tr><td><input type="checkbox" class="est-ck" data-i="' + i + '"></td><td>' + esc(p.nivel) + '</td><td>' + esc(p.materia) + '</td><td>' + esc(p.mision) + '</td></tr>'; }).join('') + '</tbody></table>' +
        '<button type="button" class="est-btn" id="est-todas">Marcar todas</button> <button type="button" class="est-btn" id="est-enviar">Enviar las marcadas</button>';
    }
    h += ' <button type="button" class="est-btn" id="est-rev">Volver a buscar</button></div>';
    return h;
  }
  async function cargar(el) {
    var sb = Wave.sb, h = '';
    var runs = [], err = '';
    try {
      var r = await fetch('https://api.github.com/repos/' + REPO + '/actions/runs?per_page=30&t=' + Date.now(), { cache: 'no-store' });
      if (!r.ok) throw new Error('GitHub ' + r.status);
      runs = (await r.json()).workflow_runs || [];
    } catch (e) { err = 'No pude leer GitHub (' + e.message + '). Si dice 403, esperá unos minutos.'; }
    var tq = await sb.from('topics').select('id,title,position,is_published,updated_at,subjects(name)').order('updated_at', { ascending: false }).limit(24);
    var tops = tq.data || [];
    var ids = tops.map(function (t) { return t.id; });
    var ex = ids.length ? (await sb.from('exams').select('topic_id,publicado').in('topic_id', ids)).data || [] : [];
    var ls = ids.length ? (await sb.from('lessons').select('id,topic_id').in('topic_id', ids)).data || [] : [];
    var st = ls.length ? (await sb.from('lesson_steps').select('lesson_id,step_type,r2_key').in('lesson_id', ls.map(function (l) { return l.id; }))).data || [] : [];
    var l2t = {}; ls.forEach(function (l) { l2t[l.id] = l.topic_id; });
    var pdfs = {}; st.forEach(function (s) { if (s.r2_key && /pdf/i.test(s.step_type || '')) pdfs[l2t[s.lesson_id]] = (pdfs[l2t[s.lesson_id]] || 0) + 1; });
    var pend = runs.filter(function (r) { return ['in_progress', 'queued', 'waiting', 'pending'].indexOf(r.status) >= 0; }).length;
    var canc = runs.filter(function (r) { return r.conclusion === 'cancelled' && estadoRun(r, runs)[1] === 'rojo'; }).length;
    h += '<div class="est-res">' + chip(runs.filter(function (r) { return r.status === 'in_progress'; }).length + ' en curso', 'amar') + chip(runs.filter(function (r) { return ['queued', 'waiting', 'pending'].indexOf(r.status) >= 0; }).length + ' en espera', 'gris') + chip(canc + ' canceladas sin reemplazo (últimas 30)', canc ? 'rojo' : 'verde') + '<button type="button" class="est-btn" id="est-act">Actualizar ahora</button><small> Actualiza solo cada 75 s · ' + new Date().toLocaleTimeString('es-AR') + '</small></div>';
    var ahora = runs.filter(function (r) { return r.status === 'in_progress'; }), espera = runs.filter(function (r) { return ['queued', 'waiting', 'pending'].indexOf(r.status) >= 0; });
    function li(r) { return '<li><b>' + esc(tipo(r.name)) + '</b> · ' + esc(((r.head_commit && r.head_commit.message) || '').split('\n')[0].slice(0, 80)) + ' <small>(desde ' + hace(r.created_at) + ')</small></li>'; }
    h = '<div class="est-ahora"><div><h3>⚙️ Haciéndose ahora (' + ahora.length + ')</h3>' + (ahora.length ? '<ul>' + ahora.map(li).join('') + '</ul>' : '<p>Nada en curso.</p>') + '</div><div><h3>⏳ En espera (' + espera.length + ')</h3>' + (espera.length ? '<ul>' + espera.map(li).join('') + '</ul>' : '<p>Nada esperando.</p>') + '</div></div>' + h;
    if (err) h += '<p class="est-err">' + esc(err) + '</p>';
    var MOT = {};
    for (var i = 0; i < runs.length; i++) { if (runs[i].status === 'completed' && runs[i].conclusion !== 'success') MOT[runs[i].id] = await motivo(runs[i], runs); }
    h = cajaEnviar(runs) + h;
    h += '<h3>Lo que se mandó a GitHub</h3><table class="est-t"><thead><tr><th>Qué</th><th>Estado</th><th>Cuándo</th><th>Cambio</th><th>Motivo</th><th></th></tr></thead><tbody>' +
      runs.map(function (r) { var e = estadoRun(r, runs); return '<tr><td>' + esc(tipo(r.name)) + '</td><td>' + chip(e[0], e[1]) + '</td><td>' + hace(r.created_at) + '</td><td>' + esc(((r.head_commit && r.head_commit.message) || '').split('\n')[0].slice(0, 90)) + '</td><td>' + esc(MOT[r.id] || '') + '</td><td>' + (r.status === 'completed' && e[1] !== 'verde' ? '<button type="button" class="est-btn" data-run="' + r.id + '">Reenviar</button>' : '') + '</td></tr>'; }).join('') + '</tbody></table>';
    h += '<h3>Misiones (lo último que se tocó en la base)</h3><table class="est-t"><thead><tr><th>Materia</th><th>Misión</th><th>Examen</th><th>PDFs</th><th>Publicada</th><th>Actualizada</th></tr></thead><tbody>' +
      tops.map(function (t) {
        var e = ex.filter(function (x) { return x.topic_id === t.id; }), np = pdfs[t.id] || 0;
        return '<tr><td>' + esc(t.subjects && t.subjects.name) + '</td><td>' + esc(t.position + '. ' + t.title) + '</td><td>' + (e.length ? chip(e[0].publicado ? 'Cargado y publicado' : 'Cargado', e[0].publicado ? 'verde' : 'amar') : chip('Sin examen', 'rojo')) + '</td><td>' + chip(np + ' PDF', np >= 4 ? 'verde' : np ? 'amar' : 'rojo') + '</td><td>' + (t.is_published ? chip('Sí', 'verde') : chip('No', 'rojo')) + '</td><td>' + hace(t.updated_at) + '</td></tr>';
      }).join('') + '</tbody></table>';
    var marc = [].slice.call(el.querySelectorAll('.est-ck')).filter(function (c) { return c.checked; }).map(function (c) { return c.getAttribute('data-i'); });
    el.innerHTML = h;
    marc.forEach(function (i) { var c = el.querySelector('.est-ck[data-i="' + i + '"]'); if (c) c.checked = true; });
    var ba = document.getElementById('est-act'); if (ba) ba.onclick = function () { ba.textContent = 'Actualizando…'; cargar(el); };
    el.onclick = async function (ev) {
      if (ev.target.id === 'est-act') return;
      if (ev.target.id === 'est-rev') { ev.target.textContent = 'Buscando…'; PEND = null; pendientes(el, true); return; }
      if (ev.target.id === 'est-todas') { el.querySelectorAll('.est-ck').forEach(function (c) { c.checked = true; }); return; }
      if (ev.target.id === 'est-enviar') {
        var sel = [].slice.call(el.querySelectorAll('.est-ck')).filter(function (c) { return c.checked; }).map(function (c) { return PEND[+c.getAttribute('data-i')]; });
        if (!sel.length) { alert('Marcá al menos una misión.'); return; }
        var avisos = '';
        ['Avanzado', 'Medio'].forEach(function (nv) {
          if (!sel.some(function (x) { return x.nivel === nv; })) return;
          var rr = runs.filter(function (x) { return new RegExp(nv, 'i').test(x.name) && /misi/i.test(x.name); });
          var enc = rr.filter(function (x) { return x.status === 'in_progress'; }).length, esp = rr.filter(function (x) { return ['queued', 'waiting', 'pending'].indexOf(x.status) >= 0; }).length;
          if (!esp && !enc) avisos += '✅ Ahora no hay nada corriendo de ' + nv + ': podés enviar tranquila.\n';
          if (esp) avisos += '⛔ Hay una corrida de ' + nv + ' EN ESPERA: esperá a que arranque, si no se pierde.\n';
          else if (enc) avisos += '⚠️ Hay una corrida de ' + nv + ' EN CURSO: la tuya queda esperando hasta que termine.\n';
        });
        if (avisos.indexOf('⛔') >= 0) { alert(avisos); return; }
        if (!confirm(avisos + (avisos ? '\n' : '') + '¿Enviar ' + sel.length + ' misión(es)?\n' + sel.map(function (x) { return '• ' + x.nivel + ' · ' + x.materia + ' · misión ' + x.mision; }).join('\n'))) return;
        ev.target.disabled = true; ev.target.textContent = 'Enviando…';
        var r2 = await sb.functions.invoke('enviar-mision', { body: { accion: 'enviar', archivos: sel.map(function (x) { return x.path; }) } });
        var m2 = (r2.data && r2.data.error) || (r2.error && 'No se pudo enviar') || null;
        if (m2) { ev.target.disabled = false; ev.target.textContent = 'Enviar las marcadas'; alert(m2); return; }
        ev.target.textContent = 'Enviado ✔'; setTimeout(function () { cargar(el); }, 4000); setTimeout(function () { PEND = null; pendientes(el, true); }, 90000);
        return;
      }
      var b = ev.target.closest('.est-btn'); if (!b) return;
      var rid = b.getAttribute('data-run'), cur = runs.filter(function (x) { return String(x.id) === rid; })[0];
      var mismos = runs.filter(function (x) { return cur && x.name === cur.name && ['in_progress', 'queued', 'waiting', 'pending'].indexOf(x.status) >= 0; });
      var aviso = '';
      if (mismos.length) {
        var enc = mismos.filter(function (x) { return x.status === 'in_progress'; }).length, esp = mismos.length - enc;
        aviso = '⚠️ OJO: de este mismo tipo (' + tipo(cur.name) + ') hay ' + (enc ? enc + ' en curso' : '') + (enc && esp ? ' y ' : '') + (esp ? esp + ' en espera' : '') + '.\n' +
          (esp ? 'Si reenviás ahora, la que está en espera puede ser reemplazada por esta (GitHub guarda una sola en espera).\n' : 'Si reenviás ahora, esta va a quedar en espera hasta que termine la que está en curso.\n') +
          'Conviene esperar a que termine.\n\n';
      }
      if (!confirm(aviso + '¿Reenviar esta corrida a GitHub?')) return;
      b.disabled = true; b.textContent = 'Enviando…';
      var r = await sb.functions.invoke('reenviar-github', { body: { run_id: b.getAttribute('data-run') } });
      var msg = (r.data && r.data.error) || (r.error && 'No se pudo reenviar') || null;
      if (msg) { b.disabled = false; b.textContent = 'Reenviar'; alert(msg); return; }
      b.textContent = 'Reenviada ✔'; setTimeout(function () { cargar(el); }, 3000); setTimeout(function () { cargar(el); }, 9000);
    };
  }
  window.WaveEstado = {
    abrir: function (vista) {
      clearInterval(T);
      vista.innerHTML = '<style>.est-chip{display:inline-block;padding:2px 10px;border-radius:12px;font-weight:700;font-size:.8rem;margin-right:6px}.est-verde{background:#d6f5df;color:#17692f}.est-amar{background:#fff0c2;color:#8a5a00}.est-rojo{background:#fddada;color:#a11}.est-gris{background:#e8eaed;color:#444}.est-t{width:100%;border-collapse:collapse;margin:8px 0 24px;font-size:.9rem}.est-t th,.est-t td{text-align:left;padding:7px 8px;border-bottom:1px solid #e3e6ea}.est-err{color:#a11;font-weight:700}.est-res{margin:10px 0}.est-env{background:#fff8e6;border-radius:12px;padding:6px 16px 14px;margin-bottom:14px}.est-ahora{display:grid;grid-template-columns:1fr 1fr;gap:16px;background:#f3f8f8;border-radius:12px;padding:6px 16px;margin-bottom:12px}.est-ahora ul{margin:0;padding-left:18px}.est-ahora li{margin-bottom:4px}.est-btn{background:#087E83;color:#fff;border:0;border-radius:8px;padding:5px 12px;font-weight:700;cursor:pointer}.est-btn[disabled]{opacity:.5}</style><h2>Estado de envíos</h2><div id="est-c">Cargando…</div>';
      var el = document.getElementById('est-c');
      cargar(el).catch(function (e) { el.textContent = 'Error: ' + e.message; });
      pendientes(el);
      T = setInterval(function () { if (!document.getElementById('est-c')) return clearInterval(T); cargar(document.getElementById('est-c')).catch(function () { }); }, 75000);
    }
  };
})();
