/* ACTIVIDADES-JUEGO (solo pantalla; la corrección no cambia, se usan tipos que ya existen):
   [[crucigrama:f,c,d,l;f,c,d,l;...]] en una pregunta fill_blank → crucigrama. Cada palabra es un hueco (en el mismo orden de los ___):
        fila, columna, dirección (h|v) y largo. Las letras que escribe el alumno llenan los huecos, así que se corrige igual que fill_blank.
   [[sopa]] en una pregunta multi_select → sopa de letras con las opciones (todas son palabras a encontrar). Al encontrar una palabra se marca
        su casilla, así que se corrige igual que multi_select.
   [[escape]] en cualquier pregunta de una actividad → escape room: un candado por pregunta que se abre al comprobarla bien; con todos abiertos, ¡escapaste! */
(function () {
  var MARCA = /\[\[(crucigrama(?::[^\]]*)?|sopa(?::\d+)?|escape)\]\]\s*/g;
  function quitarMarcas(el) {
    var w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), n, L = [];
    while ((n = w.nextNode())) if (n.nodeValue.indexOf('[[') >= 0) L.push(n);
    L.forEach(function (n) { MARCA.lastIndex = 0; n.nodeValue = n.nodeValue.replace(MARCA, ''); }); MARCA.lastIndex = 0;
  }
  function marcaDe(el) { var m = /\[\[(crucigrama(?::([^\]]*))?|sopa(?::(\d+))?|escape)\]\]/.exec(el.textContent || ''); return m; }
  function fire(i) { i.dispatchEvent(new Event('input', { bubbles: true })); i.dispatchEvent(new Event('change', { bubbles: true })); }
  function norm(s) { return String(s).toUpperCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^A-ZÑ]/g, ''); }
  function rng(seed) { var a = 0; for (var i = 0; i < seed.length; i++) a = (a * 31 + seed.charCodeAt(i)) >>> 0; return function () { a = (a * 1664525 + 1013904223) >>> 0; return a / 4294967296; }; }
  function sonar(n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }

  // ---------- CRUCIGRAMA ----------
  function crucigrama(blk, spec) {
    var ps = blk.querySelector('.mt-hueco-p'); if (!ps) return;
    var H = [].slice.call(ps.querySelectorAll('.mt-hueco')), P = String(spec || '').split(';').map(function (s) { var x = s.split(','); return { f: +x[0], c: +x[1], d: x[2], l: +x[3] }; }).filter(function (p) { return p.l > 0; });
    if (!P.length || P.length !== H.length) return;
    var F = 0, Cc = 0; P.forEach(function (p) { F = Math.max(F, p.f + (p.d === 'v' ? p.l : 1)); Cc = Math.max(Cc, p.c + (p.d === 'h' ? p.l : 1)); });
    var cel = {}, num = {};
    P.forEach(function (p, k) { num[p.f + '|' + p.c] = num[p.f + '|' + p.c] || (k + 1); for (var j = 0; j < p.l; j++) { var f = p.f + (p.d === 'v' ? j : 0), c = p.c + (p.d === 'h' ? j : 0); (cel[f + '|' + c] = cel[f + '|' + c] || []).push([k, j]); } });
    var g = document.createElement('div'); g.className = 'ja-cruci'; g.style.gridTemplateColumns = 'repeat(' + Cc + ', var(--ja-c))';
    for (var f = 0; f < F; f++) for (var c = 0; c < Cc; c++) { var k = f + '|' + c, d = document.createElement('div');
      if (cel[k]) { d.className = 'ja-cel'; d.innerHTML = (num[k] ? '<small>' + num[k] + '</small>' : '') + '<input maxlength="1" autocomplete="off" autocapitalize="characters" data-k="' + k + '">'; } else d.className = 'ja-vacio';
      g.appendChild(d); }
    H.forEach(function (h) { h.style.display = 'none'; });
    var tx = (ps.textContent || '').replace(/\s+/g, ' ').trim(), cortes = tx.split(/\s*(\d+)\)\s*/), cons = cortes[0], items = [];
    for (var z = 1; z < cortes.length; z += 2) items.push('<li><b>' + cortes[z] + '.</b> ' + String(cortes[z + 1] || '').replace(/[&<>]/g, '') + '</li>');
    var wr = document.createElement('div'); wr.className = 'ja-cruci-w'; wr.appendChild(g);
    var pl = document.createElement('div'); pl.innerHTML = '<p>' + cons.replace(/[&<>]/g, '') + '</p>'; ps.parentNode.insertBefore(pl, ps); ps.parentNode.insertBefore(wr, ps);
    var ol = document.createElement('ol'); ol.className = 'ja-pistas-l'; ol.innerHTML = items.join(''); ps.parentNode.insertBefore(ol, ps); ps.style.display = 'none';
    var I = {}; [].forEach.call(g.querySelectorAll('input'), function (i) { I[i.getAttribute('data-k')] = i; });
    function volcar() { P.forEach(function (p, k) { var s = '', algo = false; for (var j = 0; j < p.l; j++) { var v = (I[(p.f + (p.d === 'v' ? j : 0)) + '|' + (p.c + (p.d === 'h' ? j : 0))].value || ' ').toUpperCase(); if (v.trim()) algo = true; s += v; }
      H[k].value = algo ? s.replace(/ /g, '·').replace(/·+$/, '') : ''; fire(H[k]); }); }
    // dirección de escritura: la de la palabra que empieza o pasa por la celda (prioriza horizontal)
    g.addEventListener('input', function (e) { var i = e.target; if (!i.matches('input')) return; i.value = norm(i.value).slice(-1); volcar();
      if (i.value) { var k = i.getAttribute('data-k').split('|'), f = +k[0], c = +k[1], sig = I[f + '|' + (c + 1)] && cel[f + '|' + c].some(function (x) { return P[x[0]].d === 'h'; }) ? I[f + '|' + (c + 1)] : I[(f + 1) + '|' + c]; if (sig) sig.focus(); } });
    g.addEventListener('keydown', function (e) { var i = e.target; if (e.key === 'Backspace' && !i.value) { var k = i.getAttribute('data-k').split('|'), a = I[k[0] + '|' + (+k[1] - 1)] || I[(+k[0] - 1) + '|' + k[1]]; if (a) a.focus(); } });
  }

  // ---------- SOPA DE LETRAS ----------
  function sopa(blk, tam) {
    var cajas = [].slice.call(blk.querySelectorAll('input[type=checkbox]')); if (!cajas.length) return;
    var pals = cajas.map(function (c) { return { v: c.value, w: norm(c.value), c: c }; }).filter(function (p) { return p.w.length >= 2; });
    var N = Math.max(+tam || 0, 10, Math.max.apply(null, pals.map(function (p) { return p.w.length; })) + 2), R = rng(pals.map(function (p) { return p.w; }).join('|')), G = [], pos = {};
    for (var f = 0; f < N; f++) { G.push([]); for (var c = 0; c < N; c++) G[f].push(''); }
    var DIRS = [[0, 1], [1, 0], [1, 1]];
    pals.forEach(function (p) { for (var t = 0; t < 300; t++) { var d = DIRS[Math.floor(R() * 3)], f0 = Math.floor(R() * N), c0 = Math.floor(R() * N), ok = true;
      for (var j = 0; j < p.w.length; j++) { var f1 = f0 + d[0] * j, c1 = c0 + d[1] * j; if (f1 >= N || c1 >= N || (G[f1][c1] && G[f1][c1] !== p.w[j])) { ok = false; break; } }
      if (!ok) continue; for (j = 0; j < p.w.length; j++) G[f0 + d[0] * j][c0 + d[1] * j] = p.w[j]; p.ini = [f0, c0]; p.fin = [f0 + d[0] * (p.w.length - 1), c0 + d[1] * (p.w.length - 1)]; break; } });
    var AB = 'ABCDEFGHIJLMNOPRSTUVZ';
    for (f = 0; f < N; f++) for (c = 0; c < N; c++) if (!G[f][c]) G[f][c] = AB[Math.floor(R() * AB.length)];
    var lst = blk.querySelectorAll('.mt-op, label'); [].forEach.call(lst, function (l) { if (l.querySelector('input[type=checkbox]')) l.style.display = 'none'; });
    var cont = document.createElement('div'); cont.className = 'ja-sopa-box';
    cont.innerHTML = '<small class="mt-ayuda">Tocá la primera y la última letra de cada palabra.</small><div class="ja-sopa" style="grid-template-columns:repeat(' + N + ',var(--ja-s))"></div><div class="ja-lista"></div>';
    var gr = cont.querySelector('.ja-sopa'), li = cont.querySelector('.ja-lista');
    for (f = 0; f < N; f++) for (c = 0; c < N; c++) { var b = document.createElement('button'); b.type = 'button'; b.className = 'ja-l'; b.textContent = G[f][c]; b.setAttribute('data-f', f); b.setAttribute('data-c', c); gr.appendChild(b); }
    pals.forEach(function (p) { var s = document.createElement('span'); s.className = 'ja-pal'; s.textContent = p.v; p.s = s; li.appendChild(s); });
    var host = cajas[0].closest('.mt-preg-c') || blk, comp = host.querySelector('.ap-comp'); host.insertBefore(cont, comp || null);
    var ay = host.querySelector('.mt-ayuda'); if (ay && ay !== cont.firstChild) ay.style.display = 'none';
    var ini = null;
    function celda(f, c) { return gr.querySelector('[data-f="' + f + '"][data-c="' + c + '"]'); }
    function linea(a, b) { var df = Math.sign(b[0] - a[0]), dc = Math.sign(b[1] - a[1]), n = Math.max(Math.abs(b[0] - a[0]), Math.abs(b[1] - a[1]));
      if (!(a[0] === b[0] || a[1] === b[1] || Math.abs(b[0] - a[0]) === Math.abs(b[1] - a[1]))) return null; var L = []; for (var j = 0; j <= n; j++) L.push([a[0] + df * j, a[1] + dc * j]); return L; }
    gr.addEventListener('click', function (e) { var b = e.target.closest('.ja-l'); if (!b) return; var p = [+b.getAttribute('data-f'), +b.getAttribute('data-c')];
      if (!ini) { ini = p; b.classList.add('sel'); return; }
      var L = linea(ini, p); celda(ini[0], ini[1]).classList.remove('sel'); ini = null; if (!L) return;
      var palabra = L.map(function (x) { return G[x[0]][x[1]]; }).join(''), rev = palabra.split('').reverse().join('');
      var hit = pals.filter(function (q) { return !q.ok && (q.w === palabra || q.w === rev); })[0];
      if (hit) { hit.ok = true; L.forEach(function (x) { celda(x[0], x[1]).classList.add('ok'); }); hit.s.classList.add('ok'); if (!hit.c.checked) { hit.c.checked = true; fire(hit.c); } sonar('bien');
        if (pals.every(function (q) { return q.ok; })) { sonar('fanfarria'); try { WaveJuego.confeti(gr); } catch (_) {} } }
      else { sonar('mal'); L.forEach(function (x) { var el = celda(x[0], x[1]); el.classList.add('mal'); setTimeout(function () { el.classList.remove('mal'); }, 450); }); } });
  }

  // ---------- ESCAPE ROOM ----------
  function escape(cuerpo) {
    if (cuerpo.querySelector('.ja-escape')) return actualizarEscape(cuerpo);
    var bl = cuerpo.querySelectorAll(':scope > .mt-preg'); if (!bl.length) return;
    cuerpo.classList.add('ap-ver-comp');
    var e = document.createElement('div'); e.className = 'ja-escape';
    e.innerHTML = '<div class="ja-puerta">🚪</div><div class="ja-cand">' + [].map.call(bl, function (_, i) { return '<span data-cand="' + i + '">🔒</span>'; }).join('') + '</div><div class="ja-esc-txt">Comprobá cada respuesta para abrir su candado</div>';
    var top = cuerpo.querySelector('[data-cn-top]') || cuerpo.firstChild; cuerpo.insertBefore(e, top ? top.nextSibling : null);
  }
  function actualizarEscape(cuerpo) {
    var e = cuerpo.querySelector('.ja-escape'); if (!e || e.getAttribute('data-fin')) return;
    var bl = cuerpo.querySelectorAll(':scope > .mt-preg'), todos = bl.length > 0;
    [].forEach.call(bl, function (b, i) { var r = b.querySelector('.ap-comp-res'), s = e.querySelector('[data-cand="' + i + '"]'); if (!s) return;
      var ok = r && /\bok\b/.test(r.className), no = r && /\b(no|med)\b/.test(r.className);
      if (ok && s.textContent !== '🔓') { s.textContent = '🔓'; s.className = 'abierto'; }
      else if (no) s.className = 'trabado';
      if (!ok) todos = false; });
    if (todos) { e.setAttribute('data-fin', '1'); e.querySelector('.ja-puerta').textContent = '🏃💨'; e.querySelector('.ja-esc-txt').textContent = '¡ESCAPASTE! Ahora entregá la actividad.'; e.classList.add('fin');
      sonar('fanfarria'); try { WaveJuego.confeti(e, true); } catch (_) {} }
  }

  function recorrer() {
    [].forEach.call(document.querySelectorAll('.mt-preg:not([data-ja])'), function (blk) {
      blk.setAttribute('data-ja', '1'); var tx = blk.textContent || '', re = /\[\[(crucigrama(?::([^\]]*))?|sopa(?::(\d+))?|escape)\]\]/g, m, ms = [];
      while ((m = re.exec(tx))) ms.push(m); if (!ms.length) return;
      quitarMarcas(blk);
      ms.forEach(function (m) { var tipo = m[1].split(':')[0];
        if (tipo === 'crucigrama') crucigrama(blk, m[2]);
        if (tipo === 'sopa') sopa(blk, m[3]);
        if (tipo === 'escape') { var cu = blk.closest('.mt-cuest'); if (cu) cu.setAttribute('data-escape', '1'); } });
    });
    [].forEach.call(document.querySelectorAll('.mt-cuest[data-escape]'), function (cu) { if (cu.querySelector(':scope > .mt-preg')) escape(cu); else cu.removeAttribute('data-escape'); });
  }
  var css = document.createElement('style');
  css.textContent = '.ja-cruci{--ja-c:clamp(26px,7vw,40px);display:inline-grid;gap:3px;margin:12px 0}.ja-cruci-w{overflow-x:auto;padding-bottom:4px}.ja-pistas-l{margin:6px 0 0;padding-left:0;list-style:none;line-height:1.7}.ja-pistas-l b{color:#087E83}.ja-vacio{width:var(--ja-c);height:var(--ja-c)}' +
    '.ja-cel{position:relative;width:var(--ja-c);height:var(--ja-c);background:#fff;border:2px solid #1d474a;border-radius:6px}.ja-cel small{position:absolute;left:3px;top:1px;font-size:10px;font-weight:800;color:#087E83}' +
    '.ja-cel input{width:100%;height:100%;border:0;background:transparent;text-align:center;font:inherit;font-weight:900;font-size:calc(var(--ja-c)*.5);text-transform:uppercase;color:#0c292b;padding:0}' +
    '.ja-pistas{line-height:1.9}.ja-sopa{--ja-s:clamp(24px,7.4vw,36px);display:grid;gap:2px;margin:10px 0;width:max-content;max-width:100%;user-select:none}' +
    '.ja-l{width:var(--ja-s);height:var(--ja-s);border:1px solid #c9dcda;background:#fff;border-radius:6px;font:inherit;font-weight:800;font-size:calc(var(--ja-s)*.48);color:#0c292b;padding:0;cursor:pointer}' +
    '.ja-l.sel{background:#7FD3C4}.ja-l.ok{background:#8be38f}.ja-l.mal{background:#ffb3a8}.ja-lista{display:flex;flex-wrap:wrap;gap:6px}.ja-pal{border:2px solid #7FD3C4;border-radius:99px;padding:3px 10px;font-weight:800}.ja-pal.ok{text-decoration:line-through;opacity:.55;border-color:#8be38f}' +
    '.ja-escape{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:8px 0 14px;padding:12px 16px;border-radius:16px;background:linear-gradient(135deg,#3b2a1a,#5a3a22);color:#fff}.ja-puerta{font-size:42px}.ja-cand{display:flex;gap:6px;font-size:28px}' +
    '.ja-cand .abierto{filter:drop-shadow(0 0 6px #8be38f)}.ja-cand .trabado{filter:drop-shadow(0 0 6px #ff7a66)}.ja-esc-txt{font-weight:800}.ja-escape.fin{background:linear-gradient(135deg,#2e8b57,#087E83)}';
  document.head.appendChild(css);
  var pend = false;
  function prog() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; try { recorrer(); [].forEach.call(document.querySelectorAll('.mt-cuest[data-escape]'), actualizarEscape); } catch (e) {} }); }
  function iniciar() { new MutationObserver(prog).observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['class'] }); prog(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
