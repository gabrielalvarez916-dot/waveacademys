/* ACTIVIDADES PARA LOS MÁS CHICOS (Nivel Medio, 1.º a 3.º). Banco de ACTIVIDADES: solo actividades de nivel y generales, nunca examen.
   Mismo mecanismo que js/actividades-soc.js: la marca va al principio del enunciado y lo que arma el alumno se escribe en el campo de siempre.
     [[armar:MANZANA:🍎]]      short_answer (acepta: MANZANA)     · arma la palabra tocando las letras mezcladas
     [[silabas:MARIPOSA:🦋]]   numeric (4)                         · dice la palabra y aplaude 👏 una vez por sílaba
     [[escuchar:PERRO]]        multiple_choice (opciones con dibujo: "🐶 PERRO", "🐱 GATO"…) · escucha la palabra y toca el dibujo
     [[escuchar:dog:en]]       igual, con voz en inglés */
(function () {
  'use strict';
  var RE = /\[\[(armar|silabas|escuchar)(?::([^\]]*))?\]\]\s*/g;
  var NOMBRE = { armar: ['🔤', 'Armá la palabra'], silabas: ['👏', 'Aplaudí las sílabas'], escuchar: ['👂', 'Escuchá y tocá'] };
  var A = {};
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fire(el) { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }
  function setVal(el, v) { if (!el) return; el.value = v; fire(el); }
  function sonar(n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }
  function mk(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function enun(blk) { return blk.querySelector('.mt-preg-c > p, .mt-preg-c > .mt-hueco-p'); }
  function despues(blk, el) { var p = enun(blk); if (p && p.parentNode) p.parentNode.insertBefore(el, p.nextSibling); else blk.querySelector('.mt-preg-c').appendChild(el); }
  function ocultar(el) { if (el) el.classList.add('an-oculto'); }
  function hablar(t, en) { try { var u = new SpeechSynthesisUtterance(t); u.lang = en ? 'en-US' : 'es-AR'; u.rate = 0.8; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (_) {} }
  function mezclar(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function partes(arg) { var a = String(arg || '').split(':'); return { w: (a[0] || '').trim().toUpperCase(), e: (a[1] || '').trim(), en: /^en$/i.test((a[2] || a[1] || '').trim()) }; }

  // 1) ARMAR LA PALABRA ------------------------------------------------------------------------------
  A.armar = function (blk, arg) { var inp = blk.querySelector('input.mt-txt'), q = partes(arg); if (!inp || !q.w) return; ocultar(inp);
    var letras = q.w.replace(/\s+/g, '').split(''), orden = mezclar(letras.map(function (_, i) { return i; })); if (letras.length > 1 && orden.every(function (x, i) { return x === i; })) orden.reverse();
    var usadas = [], w = mk('div', 'an-caja amd'), ay = mk('small', 'mt-ayuda', 'Tocá las letras en orden. Tocá una letra de arriba para sacarla.');
    function pintar() { w.innerHTML = (q.e ? '<div class="amd-emo">' + q.e + '</div>' : '') + '<div class="amd-huecos">' + letras.map(function (_, i) { var k = usadas[i]; return '<button type="button" class="amd-h' + (k != null ? ' on' : '') + '" data-h="' + i + '">' + (k != null ? esc(letras[k]) : '') + '</button>'; }).join('') + '</div><div class="amd-letras">' + orden.map(function (k) { return '<button type="button" class="amd-l"' + (usadas.indexOf(k) >= 0 ? ' disabled' : '') + ' data-l="' + k + '">' + esc(letras[k]) + '</button>'; }).join('') + '</div>'; w.appendChild(ay);
      setVal(inp, usadas.map(function (k) { return letras[k]; }).join('')); }
    w.addEventListener('click', function (e) { var l = e.target.closest('[data-l]'), h = e.target.closest('[data-h]'); if (l && !l.disabled && usadas.length < letras.length) { usadas.push(+l.getAttribute('data-l')); sonar('bien'); pintar(); } else if (h && usadas[+h.getAttribute('data-h')] != null) { usadas = usadas.slice(0, +h.getAttribute('data-h')); pintar(); } });
    pintar(); despues(blk, w); };

  // 2) APLAUDIR LAS SÍLABAS -------------------------------------------------------------------------
  A.silabas = function (blk, arg) { var inp = blk.querySelector('input.nu-in') || blk.querySelector('input.mt-txt'), q = partes(arg); if (!inp || !q.w) return; ocultar(inp.closest('.nu-fila') || inp);
    var n = 0, w = mk('div', 'an-caja amd');
    function pintar() { w.innerHTML = (q.e ? '<div class="amd-emo">' + q.e + '</div>' : '') + '<p class="amd-pal">' + esc(q.w) + ' <button type="button" class="amd-oir" data-oir="1">🔊</button></p><div class="amd-aplausos">' + (n ? Array(n + 1).join('<span>👏</span>') : '<em>Decí la palabra despacio y aplaudí en cada golpe de voz.</em>') + '</div><div class="amd-bots"><button type="button" class="amd-clap" data-c="1">👏 Aplaudir</button><button type="button" class="an-btn" data-c="0">↺ Empezar de nuevo</button></div><p class="amd-n">' + n + (n === 1 ? ' sílaba' : ' sílabas') + '</p>'; setVal(inp, n ? String(n) : ''); }
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-c],[data-oir]'); if (!b) return; if (b.hasAttribute('data-oir')) { hablar(q.w.toLowerCase()); return; } if (b.getAttribute('data-c') === '1') { if (n < 8) n++; sonar('bien'); } else n = 0; pintar(); });
    pintar(); despues(blk, w); };

  // 3) ESCUCHAR Y TOCAR EL DIBUJO -------------------------------------------------------------------
  A.escuchar = function (blk, arg) { var rs = [].slice.call(blk.querySelectorAll('.mt-op input[type=radio]')), q = partes(arg); if (!rs.length || !q.w) return;
    var w = mk('div', 'an-caja amd'), dicho = q.w.toLowerCase();
    rs.forEach(function (r) { var op = r.closest('.mt-op'); if (op) ocultar(op); });
    w.innerHTML = '<button type="button" class="amd-escu" data-oir="1">🔊 Escuchar</button><div class="amd-dibs">' + rs.map(function (r, i) { var t = (r.closest('.mt-op') || r.parentNode).textContent.trim(), m = /^(\S+)\s+(.*)$/.exec(t), e = m && /\p{Extended_Pictographic}/u.test(m[1]) ? m[1] : '', pal = e ? m[2] : t; return '<button type="button" class="amd-dib" data-i="' + i + '">' + (e ? '<i>' + e + '</i>' : '') + '<b>' + esc(pal) + '</b></button>'; }).join('') + '</div>';
    w.addEventListener('click', function (e) { if (e.target.closest('[data-oir]')) { hablar(dicho, q.en); return; } var b = e.target.closest('[data-i]'); if (!b) return; var r = rs[+b.getAttribute('data-i')]; r.checked = true; fire(r); [].forEach.call(w.querySelectorAll('.amd-dib'), function (x) { x.classList.toggle('on', x === b); }); sonar('bien'); });
    despues(blk, w); var lanz = function () { hablar(dicho, q.en); document.removeEventListener('pointerdown', lanz, true); }; document.addEventListener('pointerdown', lanz, true); };

  function quitar(root) { var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), nn, L = []; while ((nn = tw.nextNode())) if (nn.nodeValue.indexOf('[[') >= 0) L.push(nn); L.forEach(function (x) { RE.lastIndex = 0; x.nodeValue = x.nodeValue.replace(RE, ''); }); RE.lastIndex = 0; }
  function recorrer() {
    [].forEach.call(document.querySelectorAll('.wvp.act .mt-preg:not([data-amd])'), function (blk) { var m = new RegExp(RE.source).exec(blk.textContent || ''); if (!m) return; blk.setAttribute('data-amd', '1');
      quitar(blk); var tp = blk.querySelector('.mt-tipo'), nm = NOMBRE[m[1]]; if (tp && nm) tp.innerHTML = '<span aria-hidden="true">' + nm[0] + '</span> ' + esc(nm[1]);
      try { A[m[1]](blk, m[2]); } catch (e) { if (window.console) console.warn('Actividad de Medio', m[1], e); } });
  }
  var css = document.createElement('style');
  css.textContent = ['.amd{text-align:center}.amd-emo{font-size:4rem;line-height:1.2}.amd-huecos,.amd-letras,.amd-aplausos,.amd-bots,.amd-dibs{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:8px 0}',
    '.amd-h{width:48px;height:56px;border:2px dashed #9dbdb9;border-radius:12px;background:#fff;font:inherit;font-size:1.7rem;font-weight:900}.amd-h.on{border-style:solid;border-color:#087E83;background:#D7F0E9}',
    '.amd-l{width:52px;height:56px;border:2px solid #E3ECEA;border-bottom-width:5px;border-radius:12px;background:#FFE082;font:inherit;font-size:1.7rem;font-weight:900;cursor:pointer}.amd-l:disabled{opacity:.25}',
    '.amd-pal{font-size:2rem;font-weight:900;letter-spacing:.06em}.amd-oir,.amd-escu{border:0;border-radius:999px;background:#D7F0E9;padding:8px 14px;font:inherit;font-weight:800;cursor:pointer}.amd-escu{font-size:1.2rem;padding:12px 22px;background:#087E83;color:#fff}',
    '.amd-aplausos{min-height:48px;font-size:2rem}.amd-aplausos em{font-size:.95rem}.amd-clap{border:0;border-radius:999px;background:#C2552E;color:#fff;padding:12px 22px;font:inherit;font-size:1.2rem;font-weight:900;cursor:pointer}.amd-n{font-weight:900;color:#087E83}',
    '.amd-dib{min-width:110px;padding:12px;border:3px solid #E3ECEA;border-radius:18px;background:#fff;font:inherit;cursor:pointer;display:flex;flex-direction:column;align-items:center}.amd-dib i{font-style:normal;font-size:3rem}.amd-dib b{font-size:.95rem}.amd-dib.on{border-color:#087E83;background:#D7F0E9}'].join('');
  document.head.appendChild(css);
  var pend = false;
  function prog() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; try { recorrer(); } catch (e) {} }); }
  function iniciar() { new MutationObserver(prog).observe(document.body, { childList: true, subtree: true }); prog(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
