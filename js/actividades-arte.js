/* ACTIVIDADES DE ARTE (banco de ACTIVIDADES; actividades de nivel y generales, nunca examen).
   La marca va al principio del enunciado; lo que arma el alumno se escribe en el campo de siempre (la corrección no cambia).
   Usa los dibujos y sonidos del banco de la lección (H.nat.arte, H.musica).
     [[mezclar:#E07B39]]           multiple_choice (opciones: "1 rojo + 3 amarillo", "2 rojo + 1 azul"…) · cada opción muestra su mezcla al lado del color pedido
     [[paleta]]                    multi_select (nombres del círculo: Rojo, Verde, Azul violáceo…) · se marcan tocando el círculo cromático
     [[fuga]]                      multiple_choice (A, B, C, D)                · toca el punto donde convergen las líneas de fuga
     [[tercios]]                   multiple_choice (A, B, C, D)                · toca el punto fuerte para ubicar al protagonista
     [[dictado:1,0.5,0.5,2]]       short_answer (acepta: "negra corchea corchea blanca") · escucha el ritmo y lo arma con figuras
     [[melodia:60,62,64,60]]       short_answer (acepta: "Do Re Mi Do")         · escucha la melodía y la toca en el teclado
     [[forma:ABA]]                 multiple_choice (AB, ABA, ABACA…)           · escucha la obra y elige la forma en bloques de colores */
(function () {
  'use strict';
  var RE = /\[\[(mezclar|paleta|fuga|tercios|dictado|melodia|forma)(?::([^\]]*))?\]\]\s*/g;
  var NOMBRE = { mezclar: ['🎨', 'Mezclá el color'], paleta: ['🌈', 'Armá la paleta'], fuga: ['📐', 'Encontrá el punto de fuga'], tercios: ['🖼️', 'Componé con los tercios'], dictado: ['🥁', 'Dictado rítmico'], melodia: ['🎹', 'Tocá la melodía'], forma: ['🔁', '¿Qué forma tiene?'] };
  var A = {};
  function H() { return window.WaveLeccionBanco && WaveLeccionBanco._h; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fire(el) { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }
  function setVal(el, v) { if (!el) return; el.value = v; fire(el); }
  function sonar(n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }
  function mk(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function enun(blk) { return blk.querySelector('.mt-preg-c > p, .mt-preg-c > .mt-hueco-p'); }
  function despues(blk, el) { var p = enun(blk); if (p && p.parentNode) p.parentNode.insertBefore(el, p.nextSibling); else blk.querySelector('.mt-preg-c').appendChild(el); }
  function caja(t) { return mk('div', 'an-caja aar', t ? '<small class="mt-ayuda">' + t + '</small>' : ''); }
  function radios(blk) { return [].slice.call(blk.querySelectorAll('.mt-op input[type=radio]')); }
  function textoOp(r) { return (r.closest('.mt-op') || r.parentNode).textContent.trim(); }
  function ocultarOps(L) { L.forEach(function (r) { var op = r.closest('.mt-op'); if (op) op.classList.add('an-oculto'); }); }
  function elegirRadio(rs, r, w, sel) { r.checked = true; fire(r); [].forEach.call(w.querySelectorAll(sel), function (x) { x.classList.toggle('on', x.getAttribute('data-i') === String(rs.indexOf(r))); }); sonar('bien'); }
  function norm(s) { return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').trim(); }

  // 1) MEZCLAR ----------------------------------------------------------------------------------------
  A.mezclar = function (blk, arg) { var h = H(), rs = radios(blk); if (!h || !h.nat.arte || !rs.length) return; var pig = h.nat.arte.pig, meta = String(arg || '').trim(), w = caja('Compará cada mezcla con el color pedido y elegí la que da igual.');
    function partes(t) { var n = function (re) { var m = re.exec(norm(t)); return m ? +m[1] : 0; }; return [n(/(\d+)\s*(de\s*)?rojo/), n(/(\d+)\s*(de\s*)?amarillo/), n(/(\d+)\s*(de\s*)?azul/)]; }
    ocultarOps(rs);
    w.innerHTML += '<div class="aar-meta"><span style="background:' + esc(meta) + '"></span><b>Color pedido</b></div><div class="aar-mezclas">' + rs.map(function (r, i) { var q = partes(textoOp(r)); return '<button type="button" class="aar-mz" data-i="' + i + '"><span style="background:' + pig(q[0], q[1], q[2]) + '"></span>' + esc(textoOp(r)) + '</button>'; }).join('') + '</div>';
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-i]'); if (b) elegirRadio(rs, rs[+b.getAttribute('data-i')], w, '.aar-mz'); }); despues(blk, w); };

  // 2) PALETA (círculo cromático) ------------------------------------------------------------------
  A.paleta = function (blk) { var h = H(), cb = [].slice.call(blk.querySelectorAll('.mt-op input[type=checkbox]')); if (!h || !h.nat.arte || !cb.length) return; var CI = h.nat.arte.CIRC, w = caja('Tocá los colores en el círculo para marcarlos (otra vez para desmarcarlos).'), vis = mk('div', 'aar-circ');
    cb.forEach(function (c) { var op = c.closest('.mt-op'); if (op) op.classList.add('an-oculto'); });
    function pintar() { vis.innerHTML = h.nat.arte.circulo(-1, 2, true); [].forEach.call(vis.querySelectorAll('[data-t]'), function (g) { var nom = CI[+g.getAttribute('data-t')][0], c = cb.filter(function (x) { return norm(textoOp(x)) === norm(nom); })[0]; if (!c) { g.style.opacity = .25; g.style.pointerEvents = 'none'; } else if (c.checked) g.classList.add('nat-sel'); });
      lab.textContent = cb.filter(function (c) { return c.checked; }).map(textoOp).join(' · ') || 'Ninguno marcado'; }
    var lab = mk('div', 'an-val'); vis.addEventListener('click', function (e) { var g = e.target.closest('[data-t]'); if (!g) return; var nom = CI[+g.getAttribute('data-t')][0], c = cb.filter(function (x) { return norm(textoOp(x)) === norm(nom); })[0]; if (!c) return; c.checked = !c.checked; fire(c); sonar('bien'); pintar(); });
    w.appendChild(vis); w.appendChild(lab); pintar(); despues(blk, w); };

  // 3 y 4) PUNTO DE FUGA y TERCIOS: puntos con letras sobre el dibujo --------------------------------
  function puntos(blk, svgBase, P) { var rs = radios(blk); if (!rs.length) return; var w = caja('Tocá el punto en el dibujo.'), vis = mk('div'); ocultarOps(rs);
    var s = svgBase.replace('</svg>', P.map(function (q) { var r = rs.filter(function (x) { return norm(textoOp(x)) === norm(q[2]); })[0]; return r ? '<g data-i="' + rs.indexOf(r) + '" class="nat-tap aar-pt"><circle cx="' + q[0] + '" cy="' + q[1] + '" r="13" fill="rgba(8,126,131,.15)" stroke="#087E83" stroke-width="2"/><text x="' + q[0] + '" y="' + (q[1] + 4) + '" text-anchor="middle" font-size="12" font-weight="900">' + q[2] + '</text></g>' : ''; }).join('') + '</svg>');
    vis.innerHTML = s; vis.addEventListener('click', function (e) { var g = e.target.closest('[data-i]'); if (!g) return; [].forEach.call(vis.querySelectorAll('[data-i]'), function (x) { x.classList.toggle('nat-sel', x === g); }); var r = rs[+g.getAttribute('data-i')]; r.checked = true; fire(r); sonar('bien'); });
    w.appendChild(vis); despues(blk, w); }
  A.fuga = function (blk) { var h = H(); if (!h || !h.nat.arte) return; var vx = 250, base = h.nat.arte.persp(vx, false, 4).replace(/<circle cx="[\d.]+" cy="90" r="5"[^>]*\/>/, '').replace(/<text[^>]*>PF<\/text>/, '');
    puntos(blk, base, [[80, 90, 'A'], [vx, 90, 'B'], [400, 90, 'C'], [vx, 200, 'D']]); };
  A.tercios = function (blk) { var h = H(); if (!h || !h.nat) return; var N = h.nat, s = N.rc(20, 10, 300, 200, '#FFF8E1', N.C.osc, 4) + N.rc(20, 150, 300, 60, '#A5D6A7') + N.em(80, 40, '☁️', 26);
    [120, 220].forEach(function (x) { s += N.ln(x, 10, x, 210, N.C.coral, 1, ' stroke-dasharray="5 4"'); }); [77, 143].forEach(function (y) { s += N.ln(20, y, 320, y, N.C.coral, 1, ' stroke-dasharray="5 4"'); });
    puntos(blk, N.S(340, 220, s), [[170, 110, 'A'], [220, 77, 'B'], [40, 195, 'C'], [300, 25, 'D']]); };

  // 5) DICTADO RÍTMICO --------------------------------------------------------------------------------
  var FIGN = { 4: 'redonda', 2: 'blanca', 1: 'negra', .5: 'corchea' };
  A.dictado = function (blk, arg) { var h = H(), inp = blk.querySelector('input.mt-txt'); if (!h || !h.musica || !inp) return; var pat = String(arg || '').split(',').map(Number).filter(function (x) { return FIGN[x]; }), arm = [], m = h.musica, w = caja('Escuchá el ritmo y armalo con las figuras, en orden.');
    inp.classList.add('an-oculto');
    function tocar(L) { var t = 0, b = .6; L.forEach(function (v) { m.tono(660, t, Math.min(.25, v * b * .8), { tipo: 'square', vol: .18 }); t += v * b; }); for (var k = 0; k < Math.ceil(t / b); k++) m.golpe(k * b, k % 4 === 0); }
    function pintar() { var tot = arm.reduce(function (a, b) { return a + b; }, 0); w.querySelector('.aar-ritmo').innerHTML = arm.map(function (v) { return '<span>' + FIGN[v] + '</span>'; }).join('') || '<em>Todavía no pusiste figuras</em>'; w.querySelector('.aar-tot').textContent = 'Pulsos: ' + String(tot).replace('.', ','); setVal(inp, arm.map(function (v) { return FIGN[v]; }).join(' ')); }
    w.innerHTML += '<div class="aar-bots"><button type="button" class="mus-play" data-o="1">▶ Escuchar el ritmo</button><button type="button" class="mus-play" data-p="1">▶ Escuchar lo que armé</button></div><div class="aar-figs">' + [4, 2, 1, .5].map(function (v) { return '<button type="button" class="aar-fig" data-v="' + v + '">' + FIGN[v] + '</button>'; }).join('') + '<button type="button" class="an-btn" data-x="1">⌫</button></div><div class="aar-ritmo"></div><small class="aar-tot"></small>';
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-o],[data-p],[data-v],[data-x]'); if (!b) return; if (b.hasAttribute('data-o')) return tocar(pat); if (b.hasAttribute('data-p')) return tocar(arm); if (b.hasAttribute('data-x')) arm.pop(); else if (arm.length < 12) arm.push(+b.getAttribute('data-v')); pintar(); });
    despues(blk, w); pintar(); };

  // 6) MELODÍA EN EL TECLADO --------------------------------------------------------------------------
  A.melodia = function (blk, arg) { var h = H(), inp = blk.querySelector('input.mt-txt'); if (!h || !h.musica || !inp) return; var m = h.musica, mel = String(arg || '').split(',').map(Number).filter(Boolean), toc = [], w = caja('Escuchá la melodía y tocala en el teclado, nota por nota.');
    inp.classList.add('an-oculto'); var neg = [1, 3, 6, 8, 10], teclas = ''; for (var n = 60; n <= 72; n++) teclas += '<button type="button" class="aar-tec' + (neg.indexOf(n % 12) >= 0 ? ' neg' : '') + '" data-n="' + n + '">' + (neg.indexOf(n % 12) >= 0 ? '' : m.NOTAS[n % 12]) + '</button>';
    w.innerHTML += '<div class="aar-bots"><button type="button" class="mus-play" data-o="1">▶ Escuchar la melodía</button><button type="button" class="an-btn" data-x="1">↺ Borrar</button></div><div class="aar-teclado">' + teclas + '</div><div class="aar-ritmo"></div>';
    function pintar() { w.querySelector('.aar-ritmo').innerHTML = toc.map(function (n2) { return '<span>' + m.NOTAS[n2 % 12] + '</span>'; }).join('') || '<em>Tocá las teclas</em>'; setVal(inp, toc.map(function (n2) { return m.NOTAS[n2 % 12]; }).join(' ')); }
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-o],[data-x],[data-n]'); if (!b) return; if (b.hasAttribute('data-o')) { mel.forEach(function (n2, k) { m.tono(m.frec(n2), k * .45, .4); }); return; } if (b.hasAttribute('data-x')) toc = []; else { var n2 = +b.getAttribute('data-n'); m.tono(m.frec(n2), 0, .4); if (toc.length < 16) toc.push(n2); } pintar(); });
    despues(blk, w); pintar(); };

  // 7) FORMA MUSICAL ------------------------------------------------------------------------------------
  A.forma = function (blk, arg) { var h = H(), rs = radios(blk); if (!h || !h.musica || !rs.length) return; var m = h.musica, f = String(arg || 'ABA').toUpperCase().replace(/[^ABC]/g, ''), w = caja('Escuchá la obra completa y elegí cómo se ordenan sus secciones.');
    var MOT = { A: [[60, .5], [64, .5], [67, .5], [64, .5], [65, .5], [62, .5], [60, 1]], B: [[69, 1], [67, .5], [65, .5], [64, 1], [62, 1]], C: [[72, .5], [71, .5], [69, .5], [67, .5], [69, 1], [72, 1]] }, col = { A: '#4DB6AC', B: '#FFB74D', C: '#BA68C8' };
    ocultarOps(rs);
    w.innerHTML += '<div class="aar-bots"><button type="button" class="mus-play" data-o="1">▶ Escuchar la obra</button></div><div class="aar-formas">' + rs.map(function (r, i) { var t = textoOp(r).toUpperCase(); return '<button type="button" class="aar-fo" data-i="' + i + '">' + t.split('').map(function (l) { return '<span style="background:' + (col[l] || '#90A4AE') + '">' + esc(l) + '</span>'; }).join('') + '</button>'; }).join('') + '</div>';
    w.addEventListener('click', function (e) { if (e.target.closest('[data-o]')) { var t = 0; f.split('').forEach(function (l) { MOT[l].forEach(function (n) { m.tono(m.frec(n[0]), t, n[1] * .34); t += n[1] * .38; }); t += .25; }); return; } var b = e.target.closest('[data-i]'); if (b) elegirRadio(rs, rs[+b.getAttribute('data-i')], w, '.aar-fo'); });
    despues(blk, w); };

  function quitar(root) { var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), nn, L = []; while ((nn = tw.nextNode())) if (nn.nodeValue.indexOf('[[') >= 0) L.push(nn); L.forEach(function (x) { RE.lastIndex = 0; x.nodeValue = x.nodeValue.replace(RE, ''); }); RE.lastIndex = 0; }
  function recorrer() {
    [].forEach.call(document.querySelectorAll('.wvp.act .mt-preg:not([data-aar])'), function (blk) { var m = new RegExp(RE.source).exec(blk.textContent || ''); if (!m) return; blk.setAttribute('data-aar', '1');
      quitar(blk); var tp = blk.querySelector('.mt-tipo'), nm = NOMBRE[m[1]]; if (tp && nm) tp.innerHTML = '<span aria-hidden="true">' + nm[0] + '</span> ' + esc(nm[1]);
      try { A[m[1]](blk, m[2]); } catch (e) { if (window.console) console.warn('Actividad de Arte', m[1], e); } });
  }
  var css = document.createElement('style');
  css.textContent = ['.aar{text-align:center}.aar-meta{display:flex;align-items:center;justify-content:center;gap:10px;margin:8px 0}.aar-meta span{width:70px;height:50px;border-radius:12px;border:3px solid #253638}',
    '.aar-mezclas,.aar-formas,.aar-figs,.aar-bots,.aar-ritmo{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:8px 0}.aar-mz{display:flex;flex-direction:column;align-items:center;gap:4px;padding:8px;border:3px solid #E3ECEA;border-radius:14px;background:#fff;font:inherit;font-weight:700;cursor:pointer}.aar-mz span{width:60px;height:40px;border-radius:10px;border:2px solid #253638}.aar-mz.on,.aar-fo.on{border-color:#C2552E;background:#FFF3C4}',
    '.aar-circ svg{max-width:320px}.aar-fig{padding:10px 14px;border:2px solid #9dbdb9;border-radius:12px;background:#fff;font:inherit;font-weight:800;cursor:pointer}.aar-ritmo span{padding:6px 10px;border-radius:10px;background:#D7F0E9;font-weight:800}.aar-tot{color:#4b6a6c}',
    '.aar-teclado{display:flex;justify-content:center;margin:8px 0;position:relative}.aar-tec{width:38px;height:120px;border:2px solid #253638;border-radius:0 0 8px 8px;background:#fff;font:inherit;font-size:.7rem;font-weight:800;display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px;cursor:pointer}.aar-tec.neg{width:26px;height:76px;margin:0 -13px;z-index:2;background:#263238}.aar-tec:active{background:#FFE082}',
    '.aar-fo{display:flex;gap:4px;padding:8px;border:3px solid #E3ECEA;border-radius:14px;background:#fff;cursor:pointer}.aar-fo span{width:38px;height:38px;border-radius:8px;color:#fff;font-weight:900;display:flex;align-items:center;justify-content:center}'].join('');
  document.head.appendChild(css);
  var pend = false;
  function prog() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; try { recorrer(); } catch (e) {} }); }
  function iniciar() { new MutationObserver(prog).observe(document.body, { childList: true, subtree: true }); prog(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
