/* ACTIVIDADES DE INGLÉS PARA HABLAR (banco de ACTIVIDADES; actividades de nivel y generales, nunca examen).
   Completan a js/ingles-duo.js ([[audio]], [[hablar]], [[memorama]]). La marca va al principio del enunciado; lo que dice el alumno
   (lo que entendió el navegador) se escribe en el campo de siempre y la corrección no cambia. Sin micrófono, el alumno escribe.
     [[repetir:Where is the library?]]                 short_answer (acepta la frase)  · escucha, repite y ve palabra por palabra qué se le entendió
     [[dialogo:A: Hi! How are you?|B|A: Nice to meet you!|B]]  open o keywords      · role play: la app dice las líneas de A y el alumno responde las de B
     [[describir:🏖️ ☀️ 👨‍👩‍👧 ⚽]]                       open o keywords (palabras clave) · describe la imagen en voz alta
     [[pares:sheep]]                                   multiple_choice (ship / sheep)  · escucha la palabra, elige cuál es y después la dice
     [[entrevista:What's your name?|How old are you?]] open o keywords                · la app pregunta en voz alta y el alumno contesta hablando
     [[trabalenguas:She sells seashells by the seashore]] short_answer (acepta el trabalenguas) · lo dice, con reloj, y prueba hacerlo más rápido */
(function () {
  'use strict';
  var RE = /\[\[(repetir|dialogo|describir|pares|entrevista|trabalenguas)(?::([^\]]*))?\]\]\s*/g;
  var NOMBRE = { repetir: ['🗣️', 'Listen and repeat'], dialogo: ['💬', 'Role play'], describir: ['🖼️', 'Describe the picture'], pares: ['👂', 'Minimal pairs'], entrevista: ['🎙️', 'Interview'], trabalenguas: ['👅', 'Tongue twister'] };
  var A = {};
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fire(el) { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }
  function setVal(el, v) { if (!el) return; el.value = v; fire(el); }
  function sonar(n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }
  function mk(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function enun(blk) { return blk.querySelector('.mt-preg-c > p, .mt-preg-c > .mt-hueco-p'); }
  function despues(blk, el) { var p = enun(blk); if (p && p.parentNode) p.parentNode.insertBefore(el, p.nextSibling); else blk.querySelector('.mt-preg-c').appendChild(el); }
  function campo(blk) { return blk.querySelector('textarea.mt-txt') || blk.querySelector('input.mt-txt'); }
  function norm(s) { return String(s || '').toLowerCase().replace(/[’']/g, '').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim(); }
  function decir(t, lento, fin) { try { var u = new SpeechSynthesisUtterance(t); u.lang = 'en-US'; u.rate = lento ? 0.7 : 0.95; var v = speechSynthesis.getVoices().filter(function (x) { return /^en/i.test(x.lang); })[0]; if (v) u.voice = v; if (fin) { u.onend = fin; u.onerror = fin; } speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) { if (fin) fin(); } }
  // Micrófono: devuelve lo que entendió el navegador (en inglés). Si no hay reconocimiento de voz, avisa y el alumno escribe.
  function escuchar(est, cb) { var SR = window.SpeechRecognition || window.webkitSpeechRecognition; if (!SR) { est.textContent = 'Este navegador no puede escuchar: escribilo en el casillero.'; cb(null); return; }
    try { var r = new SR(); r.lang = 'en-US'; r.interimResults = false; r.maxAlternatives = 1; est.textContent = '🎤 Te escucho…'; est.classList.add('on');
      r.onresult = function (e) { var t = e.results[0][0].transcript; est.textContent = ''; est.classList.remove('on'); cb(t); };
      r.onerror = function () { est.textContent = 'No te escuché bien. Probá de nuevo o escribilo.'; est.classList.remove('on'); cb(null); };
      r.onend = function () { est.classList.remove('on'); }; r.start(); } catch (e) { est.textContent = 'No se pudo usar el micrófono: escribilo.'; cb(null); } }
  function botones(t) { return '<button type="button" class="ain-b" data-oir="1">🔊 Listen</button><button type="button" class="ain-b" data-oir="lento">🐢 Slow</button>'; }
  function compara(meta, dicho) { var d = norm(dicho).split(' '); return norm(meta).split(' ').map(function (w) { return '<span class="' + (d.indexOf(w) >= 0 ? 'ok' : 'no') + '">' + esc(w) + '</span>'; }).join(' '); }

  // 1) LISTEN AND REPEAT --------------------------------------------------------------------------------
  A.repetir = function (blk, arg) { var inp = campo(blk), meta = String(arg || '').trim(); if (!inp || !meta) return;
    var w = mk('div', 'an-caja ain'), est = mk('small', 'ain-est'), res = mk('p', 'ain-res');
    w.innerHTML = '<p class="ain-meta">' + esc(meta) + '</p><div class="ain-bots">' + botones() + '<button type="button" class="ain-mic" data-mic="1">🎤 Speak</button></div>'; w.appendChild(est); w.appendChild(res);
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-oir],[data-mic]'); if (!b) return; if (b.hasAttribute('data-oir')) return decir(meta, b.getAttribute('data-oir') === 'lento');
      escuchar(est, function (t) { if (t == null) return; setVal(inp, t); res.innerHTML = 'Te entendí: <b>' + esc(t) + '</b><br>' + compara(meta, t); var ok = norm(meta).split(' ').every(function (x) { return norm(t).split(' ').indexOf(x) >= 0; }); if (ok) sonar('bien'); }); });
    despues(blk, w); };

  // 2) ROLE PLAY -----------------------------------------------------------------------------------------
  A.dialogo = function (blk, arg) { var ta = campo(blk), L = String(arg || '').split('|').map(function (x) { return x.trim(); }).filter(Boolean); if (!ta || !L.length) return;
    var paso = 0, resp = [], w = mk('div', 'an-caja ain'), chat = mk('div', 'ain-chat'), est = mk('small', 'ain-est'), bots = mk('div', 'ain-bots');
    function pintar() { chat.innerHTML = L.slice(0, paso + 1).map(function (l, i) { var esA = /^A\s*:/i.test(l); if (esA) return '<p class="a">🧑 ' + esc(l.replace(/^A\s*:\s*/i, '')) + '</p>'; return '<p class="b">🙂 ' + (resp[i] ? esc(resp[i]) : '<em>Tu turno: respondé hablando…</em>') + '</p>'; }).join('');
      var l = L[paso] || '', esB = l && !/^A\s*:/i.test(l); bots.innerHTML = paso >= L.length ? '<b>✔ ¡Diálogo completo!</b> <button type="button" class="an-btn" data-re="1">↺ Otra vez</button>' : esB ? '<button type="button" class="ain-mic" data-mic="1">🎤 Speak</button><input class="ain-esc" placeholder="…o escribí tu respuesta" aria-label="Tu respuesta"><button type="button" class="an-btn" data-ok="1">✔</button>' : '<button type="button" class="ain-b" data-sig="1">▶ Escuchar</button>';
      setVal(ta, L.map(function (x, i) { return resp[i] ? 'B: ' + resp[i] : ''; }).filter(Boolean).join('\n')); }
    function avanzar() { paso++; pintar(); var l = L[paso]; if (l && /^A\s*:/i.test(l)) decir(l.replace(/^A\s*:\s*/i, ''), false, function () { if (L[paso] === l) { paso++; pintar(); } }); }
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-mic],[data-sig],[data-ok],[data-re]'); if (!b) return;
      if (b.hasAttribute('data-re')) { paso = 0; resp = []; pintar(); return; }
      if (b.hasAttribute('data-sig')) { var l = L[paso]; decir(l.replace(/^A\s*:\s*/i, ''), false, function () { if (L[paso] === l) avanzar(); }); return; }
      if (b.hasAttribute('data-ok')) { var v = w.querySelector('.ain-esc').value.trim(); if (v) { resp[paso] = v; sonar('bien'); avanzar(); } return; }
      escuchar(est, function (t) { if (t == null) return; resp[paso] = t; sonar('bien'); avanzar(); }); });
    w.appendChild(chat); w.appendChild(bots); w.appendChild(est); pintar(); despues(blk, w); };

  // 3) DESCRIBE THE PICTURE ------------------------------------------------------------------------------
  A.describir = function (blk, arg) { var ta = campo(blk), img = String(arg || '').trim(); if (!ta || !img) return; var dicho = [], w = mk('div', 'an-caja ain'), est = mk('small', 'ain-est'), tr = mk('p', 'ain-res');
    w.innerHTML = '<div class="ain-img">' + esc(img) + '</div><p class="ain-tip">Decí todo lo que ves: <i>There is…, There are…, I can see…, He is…ing</i></p><div class="ain-bots"><button type="button" class="ain-mic" data-mic="1">🎤 Speak</button><button type="button" class="an-btn" data-x="1">↺ Borrar</button></div>'; w.appendChild(est); w.appendChild(tr);
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-mic],[data-x]'); if (!b) return; if (b.hasAttribute('data-x')) { dicho = []; tr.innerHTML = ''; setVal(ta, ''); return; }
      escuchar(est, function (t) { if (t == null) return; dicho.push(t); tr.innerHTML = dicho.map(function (x) { return '🗨️ ' + esc(x); }).join('<br>'); setVal(ta, dicho.join('. ')); sonar('bien'); }); });
    despues(blk, w); };

  // 4) MINIMAL PAIRS --------------------------------------------------------------------------------------
  A.pares = function (blk, arg) { var rs = [].slice.call(blk.querySelectorAll('.mt-op input[type=radio]')), meta = String(arg || '').trim(); if (!rs.length || !meta) return;
    var w = mk('div', 'an-caja ain'), est = mk('small', 'ain-est'), res = mk('p', 'ain-res');
    rs.forEach(function (r) { var op = r.closest('.mt-op'); if (op) op.classList.add('an-oculto'); });
    w.innerHTML = '<div class="ain-bots">' + botones() + '</div><div class="ain-pares">' + rs.map(function (r, i) { return '<button type="button" class="ain-par" data-i="' + i + '">' + esc((r.closest('.mt-op') || r.parentNode).textContent.trim()) + '</button>'; }).join('') + '</div><div class="ain-bots"><button type="button" class="ain-mic" data-mic="1">🎤 Ahora decilo vos</button></div>'; w.appendChild(est); w.appendChild(res);
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-oir],[data-i],[data-mic]'); if (!b) return; if (b.hasAttribute('data-oir')) return decir(meta, b.getAttribute('data-oir') === 'lento');
      if (b.hasAttribute('data-i')) { var r = rs[+b.getAttribute('data-i')]; r.checked = true; fire(r); [].forEach.call(w.querySelectorAll('.ain-par'), function (x) { x.classList.toggle('on', x === b); }); sonar('bien'); return; }
      escuchar(est, function (t) { if (t == null) return; res.innerHTML = 'Te entendí: <b>' + esc(t) + '</b> ' + (norm(t).split(' ').indexOf(norm(meta)) >= 0 ? '✅' : '🔁 Probá de nuevo, más despacio.'); }); });
    despues(blk, w); setTimeout(function () { decir(meta); }, 0); };

  // 5) INTERVIEW ----------------------------------------------------------------------------------------
  A.entrevista = function (blk, arg) { var ta = campo(blk), Q = String(arg || '').split('|').map(function (x) { return x.trim(); }).filter(Boolean); if (!ta || !Q.length) return;
    var k = 0, R = [], w = mk('div', 'an-caja ain'), est = mk('small', 'ain-est'), cont = mk('div', 'ain-chat'), bots = mk('div', 'ain-bots');
    function pintar() { cont.innerHTML = Q.slice(0, k + 1).map(function (q, i) { return '<p class="a">🎙️ ' + esc(q) + '</p>' + (R[i] ? '<p class="b">🙂 ' + esc(R[i]) + '</p>' : ''); }).join(''); bots.innerHTML = k >= Q.length ? '<b>✔ ¡Entrevista completa!</b>' : '<button type="button" class="ain-b" data-q="1">🔊 Question</button><button type="button" class="ain-mic" data-mic="1">🎤 Answer</button><input class="ain-esc" placeholder="…o escribí tu respuesta" aria-label="Tu respuesta"><button type="button" class="an-btn" data-ok="1">✔</button>';
      setVal(ta, Q.map(function (q, i) { return R[i] ? q + ' ' + R[i] : ''; }).filter(Boolean).join('\n')); }
    function guardar(t) { R[k] = t; k++; sonar('bien'); pintar(); if (k < Q.length) decir(Q[k]); }
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-q],[data-mic],[data-ok]'); if (!b) return; if (b.hasAttribute('data-q')) return decir(Q[k]);
      if (b.hasAttribute('data-ok')) { var v = w.querySelector('.ain-esc').value.trim(); if (v) guardar(v); return; } escuchar(est, function (t) { if (t != null) guardar(t); }); });
    w.appendChild(cont); w.appendChild(bots); w.appendChild(est); pintar(); despues(blk, w); };

  // 6) TONGUE TWISTER -----------------------------------------------------------------------------------
  A.trabalenguas = function (blk, arg) { var inp = campo(blk), meta = String(arg || '').trim(); if (!inp || !meta) return; var mejor = null, t0 = 0;
    var w = mk('div', 'an-caja ain'), est = mk('small', 'ain-est'), res = mk('p', 'ain-res');
    w.innerHTML = '<p class="ain-meta">👅 ' + esc(meta) + '</p><div class="ain-bots">' + botones() + '<button type="button" class="ain-mic" data-mic="1">🎤 ¡Ya!</button></div>'; w.appendChild(est); w.appendChild(res);
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-oir],[data-mic]'); if (!b) return; if (b.hasAttribute('data-oir')) return decir(meta, b.getAttribute('data-oir') === 'lento');
      t0 = Date.now(); escuchar(est, function (t) { if (t == null) return; var seg = Math.max(0.5, (Date.now() - t0) / 1000), ok = norm(meta).split(' ').filter(function (x) { return norm(t).split(' ').indexOf(x) >= 0; }).length, tot = norm(meta).split(' ').length; setVal(inp, t);
        if (ok === tot && (mejor == null || seg < mejor)) mejor = seg; res.innerHTML = compara(meta, t) + '<br>⏱️ ' + seg.toFixed(1).replace('.', ',') + ' s · ' + ok + ' de ' + tot + ' palabras' + (mejor ? ' · 🏆 mejor: ' + mejor.toFixed(1).replace('.', ',') + ' s' : '') + (ok === tot ? ' — ¡ahora más rápido!' : ''); if (ok === tot) sonar('bien'); }); });
    despues(blk, w); };

  function quitar(root) { var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), nn, L = []; while ((nn = tw.nextNode())) if (nn.nodeValue.indexOf('[[') >= 0) L.push(nn); L.forEach(function (x) { RE.lastIndex = 0; x.nodeValue = x.nodeValue.replace(RE, ''); }); RE.lastIndex = 0; }
  function recorrer() {
    [].forEach.call(document.querySelectorAll('.wvp.act .mt-preg:not([data-ain])'), function (blk) { var m = new RegExp(RE.source).exec(blk.textContent || ''); if (!m) return; blk.setAttribute('data-ain', '1');
      quitar(blk); var tp = blk.querySelector('.mt-tipo'), nm = NOMBRE[m[1]]; if (tp && nm) tp.innerHTML = '<span aria-hidden="true">' + nm[0] + '</span> ' + esc(nm[1]);
      try { A[m[1]](blk, m[2]); } catch (e) { if (window.console) console.warn('Actividad de Inglés', m[1], e); } });
  }
  var css = document.createElement('style');
  css.textContent = ['.ain{text-align:center}.ain-meta{font-size:1.35rem;font-weight:900;margin:6px 0}.ain-bots{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;align-items:center;margin:8px 0}.ain-b{border:2px solid #9dbdb9;border-radius:999px;background:#fff;padding:8px 14px;font:inherit;font-weight:800;cursor:pointer}',
    '.ain-mic{border:0;border-radius:999px;background:#C2552E;color:#fff;padding:10px 18px;font:inherit;font-weight:900;cursor:pointer}.ain-est{display:block;min-height:1.2em;color:#4b6a6c}.ain-est.on{color:#C2552E;font-weight:800;animation:ainp 1s infinite}@keyframes ainp{50%{opacity:.4}}',
    '.ain-res{line-height:1.8}.ain-res span{padding:2px 6px;border-radius:6px;margin:1px}.ain-res span.ok{background:#C8E6C9}.ain-res span.no{background:#FFCDD2}',
    '.ain-chat{max-width:440px;margin:0 auto;padding:10px;border-radius:16px;background:#ECEFF1;text-align:left}.ain-chat p{max-width:80%;margin:6px 0;padding:8px 12px;border-radius:14px;background:#fff}.ain-chat p.b{margin-left:auto;background:#D7F0E9}.ain-esc{flex:1 1 180px;max-width:260px;padding:8px 10px;border:2px solid #E3ECEA;border-radius:12px;font:inherit}',
    '.ain-img{font-size:3.4rem;letter-spacing:.2em;line-height:1.3;padding:10px;border-radius:16px;background:#FFF8E1}.ain-tip{color:#4b6a6c}.ain-pares{display:flex;gap:10px;justify-content:center}.ain-par{min-width:120px;padding:14px;border:3px solid #E3ECEA;border-radius:16px;background:#fff;font:inherit;font-size:1.3rem;font-weight:900;cursor:pointer}.ain-par.on{border-color:#087E83;background:#D7F0E9}'].join('');
  document.head.appendChild(css);
  var pend = false;
  function prog() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; try { recorrer(); } catch (e) {} }); }
  function iniciar() { new MutationObserver(prog).observe(document.body, { childList: true, subtree: true }); prog(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
