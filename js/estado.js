/* Estado de envíos: GitHub (corridas) + base (misiones). Solo lectura. */
(function () {
  var REPO = 'gabrielalvarez916-dot/waveacademys';
  var T = null;
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
  async function cargar(el) {
    var sb = Wave.sb, h = '';
    var runs = [], err = '';
    try {
      var r = await fetch('https://api.github.com/repos/' + REPO + '/actions/runs?per_page=30');
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
    h += '<div class="est-res">' + chip(pend + ' en curso o en espera', pend ? 'amar' : 'verde') + chip(canc + ' canceladas sin reemplazo (últimas 30)', canc ? 'rojo' : 'verde') + '<small> Actualiza solo cada 90 s · ' + new Date().toLocaleTimeString('es-AR') + '</small></div>';
    if (err) h += '<p class="est-err">' + esc(err) + '</p>';
    h += '<h3>Lo que se mandó a GitHub</h3><table class="est-t"><thead><tr><th>Qué</th><th>Estado</th><th>Cuándo</th><th>Cambio</th><th></th></tr></thead><tbody>' +
      runs.map(function (r) { var e = estadoRun(r, runs); return '<tr><td>' + esc(tipo(r.name)) + '</td><td>' + chip(e[0], e[1]) + '</td><td>' + hace(r.created_at) + '</td><td>' + esc(((r.head_commit && r.head_commit.message) || '').split('\n')[0].slice(0, 90)) + '</td><td>' + (r.status === 'completed' && e[1] !== 'verde' ? '<button type="button" class="est-btn" data-run="' + r.id + '">Reenviar</button>' : '') + '</td></tr>'; }).join('') + '</tbody></table>';
    h += '<h3>Misiones (lo último que se tocó en la base)</h3><table class="est-t"><thead><tr><th>Materia</th><th>Misión</th><th>Examen</th><th>PDFs</th><th>Publicada</th><th>Actualizada</th></tr></thead><tbody>' +
      tops.map(function (t) {
        var e = ex.filter(function (x) { return x.topic_id === t.id; }), np = pdfs[t.id] || 0;
        return '<tr><td>' + esc(t.subjects && t.subjects.name) + '</td><td>' + esc(t.position + '. ' + t.title) + '</td><td>' + (e.length ? chip(e[0].publicado ? 'Cargado y publicado' : 'Cargado', e[0].publicado ? 'verde' : 'amar') : chip('Sin examen', 'rojo')) + '</td><td>' + chip(np + ' PDF', np >= 4 ? 'verde' : np ? 'amar' : 'rojo') + '</td><td>' + (t.is_published ? chip('Sí', 'verde') : chip('No', 'rojo')) + '</td><td>' + hace(t.updated_at) + '</td></tr>';
      }).join('') + '</tbody></table>';
    el.innerHTML = h;
    el.onclick = async function (ev) {
      var b = ev.target.closest('.est-btn'); if (!b) return;
      if (!confirm('¿Reenviar esta corrida a GitHub?')) return;
      b.disabled = true; b.textContent = 'Enviando…';
      var r = await sb.functions.invoke('reenviar-github', { body: { run_id: b.getAttribute('data-run') } });
      var msg = (r.data && r.data.error) || (r.error && 'No se pudo reenviar') || null;
      if (msg) { b.disabled = false; b.textContent = 'Reenviar'; alert(msg); return; }
      b.textContent = 'Reenviada ✔'; setTimeout(function () { cargar(el); }, 4000);
    };
  }
  window.WaveEstado = {
    abrir: function (vista) {
      clearInterval(T);
      vista.innerHTML = '<style>.est-chip{display:inline-block;padding:2px 10px;border-radius:12px;font-weight:700;font-size:.8rem;margin-right:6px}.est-verde{background:#d6f5df;color:#17692f}.est-amar{background:#fff0c2;color:#8a5a00}.est-rojo{background:#fddada;color:#a11}.est-gris{background:#e8eaed;color:#444}.est-t{width:100%;border-collapse:collapse;margin:8px 0 24px;font-size:.9rem}.est-t th,.est-t td{text-align:left;padding:7px 8px;border-bottom:1px solid #e3e6ea}.est-err{color:#a11;font-weight:700}.est-res{margin:10px 0}.est-btn{background:#087E83;color:#fff;border:0;border-radius:8px;padding:5px 12px;font-weight:700;cursor:pointer}.est-btn[disabled]{opacity:.5}</style><h2>Estado de envíos</h2><div id="est-c">Cargando…</div>';
      var el = document.getElementById('est-c');
      cargar(el).catch(function (e) { el.textContent = 'Error: ' + e.message; });
      T = setInterval(function () { if (!document.getElementById('est-c')) return clearInterval(T); cargar(document.getElementById('est-c')).catch(function () { }); }, 90000);
    }
  };
})();
