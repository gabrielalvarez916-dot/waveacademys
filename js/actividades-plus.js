/* ACTIVIDADES PLUS (solo actividades, no examen). Cambian la pantalla; la corrección es la de un tipo que ya existe.
   Se activan con una marca dentro del enunciado (se borra al mostrar). Ver docs/tipos-de-pregunta.md, sección "Actividades plus".
   Grupo 1 (dibujo nuevo sobre tipos existentes)
     [[error]]               tap_text (modo lineas)  · encontrá el paso con error en una cuenta o procedimiento
     [[secuencia]]           fill_blank              · pasos separados por → con huecos en los que faltan
     [[comparar]]            multiple_choice         · resoluciones lado a lado (" | " = salto de línea dentro de una opción)
     [[causas]]              matching                · causa → consecuencia
     [[etapas]] [[linea]]    ordering                · ordenar etapas / línea de tiempo
     [[oracion:Sujeto,Verbo,Complemento]]  tokens    · armar una oración por partes (guía de partes)
     [[problema]]            numeric/short_answer/solve_complete · problema verbal: datos resaltados y borrador
   Grupo 2 (manipular; el valor que arma el alumno va al campo del tipo)
     [[piezas:4]] [[piezas:4:circulo]] [[piezas:4:barra:2]]  numeric · arma la fracción con piezas → escribe "3/4"
     [[repartir:12:3:🍎]]    numeric                 · reparte objetos en grupos → escribe cuántos hay en cada grupo (si son iguales)
     [[recta:0:2:1/4]]       numeric                 · ubica el punto en la recta → escribe el valor ("5/4" o "1,25")
     [[esquema]] [[esquema:arbol]]  matching/classify · completa un esquema tocando nombres
     [[arrastrar]]           label_image             · rotula tocando el nombre y después el punto
     [[geoplano:6:area]] [[geoplano:6:perimetro]]  numeric · construye una figura en la cuadrícula → escribe el área o el perímetro
     [[funcion]] [[funcion:5]]  fill_blank con 2 huecos (y = ___x + ___) · marca 2 puntos y se completan pendiente y ordenada
   Grupo 3 (versión simplificada y reutilizable)
     [[molecula:H,O,C]]      short_answer            · arma la molécula con átomos → escribe la fórmula ("H2O", en el orden de la marca)
     [[circuito]] [[sistema]]  multi_select          · arma el circuito o el sistema con las piezas elegidas
     [[simulador:Temperatura,0,100,10,°C;Tiempo,120-x,s]]  cualquier tipo · mové el control y mirá qué pasa; después respondé
     [[capas:Introducción|Desarrollo|Cierre]]  open/keywords · escribí el texto por capas */
(function () {
  'use strict';
  var RE = /\[\[(error|secuencia|comparar|causas|etapas|linea|oracion|problema|piezas|repartir|recta|esquema|arrastrar|geoplano|funcion|molecula|circuito|sistema|simulador|capas)(?::([^\]]*))?\]\]\s*/g;
  var NOMBRE = { error: ['🔍', 'Encontrá el error'], secuencia: ['🪜', 'Completá la secuencia'], comparar: ['⚖️', 'Compará soluciones'], causas: ['➡️', 'Causas y consecuencias'],
    etapas: ['🔢', 'Ordená las etapas'], linea: ['🕰️', 'Línea de tiempo'], oracion: ['🧱', 'Armá la oración'], problema: ['📘', 'Problema'], piezas: ['🧩', 'Armá con piezas'],
    repartir: ['🍽️', 'Repartí'], recta: ['📏', 'Recta numérica'], esquema: ['🗺️', 'Completá el esquema'], arrastrar: ['🏷️', 'Rotulá el dibujo'], geoplano: ['📐', 'Construí la figura'],
    funcion: ['📈', 'Construí la función'], molecula: ['⚛️', 'Armá la molécula'], circuito: ['🔌', 'Armá el circuito'], sistema: ['⚙️', 'Armá el sistema'], simulador: ['🧪', 'Experimento'], capas: ['📝', 'Escribí por capas'] };

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fire(el) { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }
  function setVal(el, v) { if (!el) return; el.value = v; fire(el); }
  function sonar(n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }
  function mcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = b; b = a % b; a = t; } return a || 1; }
  function frac(n, d) { if (d < 0) { n = -n; d = -d; } var g = mcd(n, d); n /= g; d /= g; return d === 1 ? String(n) : n + '/' + d; }
  function dec(v) { return String(Math.round(v * 1000) / 1000).replace('.', ','); }
  function mk(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function enun(blk) { return blk.querySelector('.mt-preg-c > p, .mt-preg-c > .mt-hueco-p'); }
  function despuesDe(blk, el) { var p = enun(blk); if (p && p.parentNode) p.parentNode.insertBefore(el, p.nextSibling); else blk.querySelector('.mt-preg-c').appendChild(el); }
  function quitar(root) {
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), n, L = [];
    while ((n = w.nextNode())) if (n.nodeValue.indexOf('[[') >= 0) L.push(n);
    L.forEach(function (n) { RE.lastIndex = 0; n.nodeValue = n.nodeValue.replace(RE, ''); }); RE.lastIndex = 0;
  }
  function campoNum(blk) { var i = blk.querySelector('input.nu-in'); if (i) { var f = i.closest('.nu-fila'); if (f) f.classList.add('ap2-oculto'); } return i; }

  // ---------- Grupo 1 ----------
  var A = {};
  A.error = function (blk) { var t = blk.querySelector('.tp-texto'); if (t) t.classList.add('ap2-pasos'); };
  A.secuencia = function (blk) {
    var p = blk.querySelector('.mt-hueco-p'); if (!p) return;
    var pasos = [], cur = mk('span', 'ap2-paso');
    Array.prototype.slice.call(p.childNodes).forEach(function (n) {
      if (n.nodeType === 3) {
        var partes = n.nodeValue.split('→');
        partes.forEach(function (x, k) { if (k) { pasos.push(cur); cur = mk('span', 'ap2-paso'); } if (x.trim()) cur.appendChild(document.createTextNode(x.trim())); });
      } else cur.appendChild(n);
    });
    pasos.push(cur);
    p.innerHTML = ''; p.classList.add('ap2-sec');
    pasos.forEach(function (s, k) { if (k) p.appendChild(mk('span', 'ap2-flecha', '➜')); p.appendChild(s); });
  };
  A.comparar = function (blk) {
    var ops = blk.querySelector('.mt-ops'); if (!ops) return; ops.classList.add('ap2-comp');
    [].forEach.call(ops.querySelectorAll('.mt-op'), function (o, k) {
      var s = o.querySelector('span'); if (s) s.innerHTML = s.textContent.split(' | ').map(esc).join('<br>');
      var l = o.querySelector('.mt-op-l'); if (l) l.textContent = String.fromCharCode(65 + k);
      o.insertBefore(mk('small', 'ap2-comp-t', 'Solución ' + String.fromCharCode(65 + k)), o.firstChild);
    });
  };
  A.causas = function (blk) {
    var ps = blk.querySelector('.mt-pares'); if (!ps) return; ps.classList.add('ap2-causas');
    ps.insertBefore(mk('div', 'ap2-causas-h', '<span>Causa</span><span>Consecuencia</span>'), ps.firstChild);
    [].forEach.call(ps.querySelectorAll('.mt-par'), function (r) { var s = r.querySelector('select'); if (s) r.insertBefore(mk('b', 'ap2-flecha', '➜'), s); });
  };
  A.etapas = function (blk) { var o = blk.querySelector('.mt-orden'); if (o) o.classList.add('ap2-etapas'); };
  A.linea = function (blk) { var o = blk.querySelector('.mt-orden'); if (o) o.classList.add('ap2-linea'); };
  A.oracion = function (blk, arg) {
    var arm = blk.querySelector('.tk-arm'); if (!arm) return;
    var roles = String(arg || '').split(',').map(function (x) { return x.trim(); }).filter(Boolean); if (!roles.length) return;
    var g = mk('div', 'ap2-roles', roles.map(function (r) { return '<span>' + esc(r) + '</span>'; }).join('<i>+</i>'));
    arm.parentNode.insertBefore(g, arm);
    function pintar() { var n = arm.querySelectorAll('.tk-f').length; [].forEach.call(g.querySelectorAll('span'), function (s, k) { s.classList.toggle('on', k < n); }); }
    new MutationObserver(pintar).observe(arm, { childList: true }); pintar();
  };
  A.problema = function (blk) {
    var p = enun(blk); if (!p) return;
    var w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT), n, L = [];
    while ((n = w.nextNode())) L.push(n);
    L.forEach(function (t) {
      var re = /\d+(?:[.,]\d+)*(?:\/\d+)?/g; if (!re.test(t.nodeValue)) return; re.lastIndex = 0;
      var f = document.createDocumentFragment(), s = t.nodeValue, last = 0, m;
      while ((m = re.exec(s))) { f.appendChild(document.createTextNode(s.slice(last, m.index))); f.appendChild(mk('mark', 'ap2-dato', esc(m[0]))); last = m.index + m[0].length; }
      f.appendChild(document.createTextNode(s.slice(last))); t.parentNode.replaceChild(f, t);
    });
    if (blk.querySelector('input.nu-in, input.mt-txt')) {
      var b = mk('details', 'ap2-borr', '<summary>✏️ Borrador para hacer la cuenta (no se entrega)</summary><textarea rows="3" maxlength="1000" placeholder="Hacé acá tus cuentas"></textarea>');
      despuesDe(blk, b);
    }
  };

  // ---------- Grupo 2 ----------
  A.piezas = function (blk, arg) {
    var inp = campoNum(blk); if (!inp) return;
    var a = String(arg || '').split(':'), d = Math.max(1, Math.min(24, parseInt(a[0], 10) || 4)), forma = a[1] === 'circulo' ? 'circulo' : 'barra', ent = Math.max(1, Math.min(4, parseInt(a[2], 10) || 1));
    var box = mk('div', 'ap2-piezas'), lab = mk('div', 'ap2-val', '0/' + d);
    for (var e = 0; e < ent; e++) {
      if (forma === 'circulo') {
        var svg = '<svg viewBox="-1.05 -1.05 2.1 2.1" class="ap2-circ" role="group" aria-label="Entero ' + (e + 1) + '">';
        for (var k = 0; k < d; k++) {
          var a0 = 2 * Math.PI * k / d - Math.PI / 2, a1 = 2 * Math.PI * (k + 1) / d - Math.PI / 2;
          var path = d === 1 ? 'M -1 0 A 1 1 0 1 1 1 0 A 1 1 0 1 1 -1 0 Z' : 'M0 0 L' + Math.cos(a0).toFixed(4) + ' ' + Math.sin(a0).toFixed(4) + ' A1 1 0 ' + (a1 - a0 > Math.PI ? 1 : 0) + ' 1 ' + Math.cos(a1).toFixed(4) + ' ' + Math.sin(a1).toFixed(4) + ' Z';
          svg += '<path class="ap2-pz" tabindex="0" role="button" aria-label="Pieza" d="' + path + '"/>';
        }
        box.insertAdjacentHTML('beforeend', svg + '</svg>');
      } else {
        box.insertAdjacentHTML('beforeend', '<div class="ap2-barra" role="group">' + Array(d + 1).join('<button type="button" class="ap2-pz" aria-label="Pieza"></button>') + '</div>');
      }
    }
    function act() { var n = box.querySelectorAll('.ap2-pz.on').length; lab.textContent = n + '/' + d; setVal(inp, n ? n + '/' + d : ''); }
    box.addEventListener('click', function (ev) { var p = ev.target.closest('.ap2-pz'); if (!p) return; p.classList.toggle('on'); sonar('bien'); act(); });
    box.addEventListener('keydown', function (ev) { if ((ev.key === 'Enter' || ev.key === ' ') && ev.target.classList.contains('ap2-pz')) { ev.preventDefault(); ev.target.classList.toggle('on'); act(); } });
    var w = mk('div', 'ap2-caja'); w.appendChild(mk('small', 'mt-ayuda', 'Tocá las piezas para pintarlas. Tocá de nuevo para despintar.')); w.appendChild(box); w.appendChild(lab);
    despuesDe(blk, w);
  };
  A.repartir = function (blk, arg) {
    var inp = campoNum(blk); if (!inp) return;
    var a = String(arg || '').split(':'), tot = Math.max(1, Math.min(40, parseInt(a[0], 10) || 12)), gr = Math.max(2, Math.min(8, parseInt(a[1], 10) || 3)), ob = a[2] || '🍎', sel = 0;
    var w = mk('div', 'ap2-caja');
    w.innerHTML = '<small class="mt-ayuda">Elegí un grupo y tocá los objetos para ponerlos ahí. Tocá un objeto de un grupo para devolverlo.</small>' +
      '<div class="ap2-pool">' + Array(tot + 1).join('<button type="button" class="ap2-ob">' + esc(ob) + '</button>') + '</div>' +
      '<div class="ap2-platos">' + Array.apply(null, Array(gr)).map(function (_, k) { return '<div class="ap2-plato' + (k ? '' : ' sel') + '" data-g="' + k + '" tabindex="0" role="button"><b>Grupo ' + (k + 1) + ' · <span>0</span></b><div class="ap2-pl-c"></div></div>'; }).join('') + '</div>';
    var pool = w.querySelector('.ap2-pool'), pls = w.querySelectorAll('.ap2-plato');
    function act() {
      var cs = [].map.call(pls, function (p) { var c = p.querySelectorAll('.ap2-ob').length; p.querySelector('span').textContent = c; return c; });
      var igual = cs[0] > 0 && cs.every(function (c) { return c === cs[0]; });
      setVal(inp, igual ? String(cs[0]) : '');
    }
    w.addEventListener('click', function (ev) {
      var pl = ev.target.closest('.ap2-plato'), o = ev.target.closest('.ap2-ob');
      if (o && o.parentNode === pool) { pls[sel].querySelector('.ap2-pl-c').appendChild(o); sonar('bien'); act(); return; }
      if (o) { pool.appendChild(o); act(); return; }
      if (pl) { sel = +pl.getAttribute('data-g'); [].forEach.call(pls, function (p, k) { p.classList.toggle('sel', k === sel); }); }
    });
    despuesDe(blk, w);
  };
  A.recta = function (blk, arg) {
    var inp = campoNum(blk); if (!inp) return;
    var a = String(arg || '').split(':'), mn = parseFloat(a[0]) || 0, mx = parseFloat(a[1]); if (!(mx > mn)) mx = mn + 10;
    var pn = 1, pd = 1, ps = String(a[2] || '1').trim(), fm = /^(\d+)\/(\d+)$/.exec(ps);
    if (fm) { pn = +fm[1]; pd = +fm[2]; } else { var pf = parseFloat(ps.replace(',', '.')) || 1; pd = 1; while (Math.round(pf * pd) !== pf * pd && pd < 1000) pd *= 10; pn = Math.round(pf * pd); }
    var paso = pn / pd, n = Math.round((mx - mn) / paso); if (n < 1 || n > 60) n = Math.min(60, Math.max(1, n));
    var W = 600, M = 30, sx = (W - 2 * M) / n, svg = '<svg viewBox="0 0 ' + W + ' 90" class="ap2-recta" role="group" aria-label="Recta numérica"><line x1="' + (M - 14) + '" y1="45" x2="' + (W - M + 14) + '" y2="45" class="ap2-r-l"/>';
    for (var k = 0; k <= n; k++) {
      var v = mn + k * paso, x = M + k * sx, ent = Math.abs(v - Math.round(v)) < 1e-9;
      svg += '<line x1="' + x + '" y1="' + (ent ? 32 : 37) + '" x2="' + x + '" y2="' + (ent ? 58 : 53) + '" class="ap2-r-t"/>';
      if (ent || n <= 12) svg += '<text x="' + x + '" y="80" class="ap2-r-n' + (ent ? '' : ' chico') + '">' + esc(ent ? String(Math.round(v)) : fm ? frac(Math.round(mn * pd) + k * pn, pd) : dec(v)) + '</text>';
      svg += '<rect x="' + (x - sx / 2) + '" y="10" width="' + sx + '" height="60" class="ap2-r-hit" data-k="' + k + '" tabindex="0" role="button" aria-label="Marcar en este lugar"/>';
    }
    svg += '<g class="ap2-r-pt" style="display:none"><circle r="11" cy="45"/><path d="M0 28 L-7 16 L7 16 Z"/></g></svg>';
    var w = mk('div', 'ap2-caja', '<small class="mt-ayuda">Tocá la recta en el lugar del número.</small>' + svg + '<div class="ap2-val">—</div>'), lab = w.querySelector('.ap2-val'), pt = w.querySelector('.ap2-r-pt');
    function marcar(k) {
      var x = M + k * sx, v = mn + k * paso; pt.style.display = ''; pt.setAttribute('transform', 'translate(' + x + ',0)');
      var t = fm ? frac(Math.round(mn * pd) + k * pn, pd) : dec(v); lab.textContent = t; setVal(inp, t); sonar('bien');
    }
    w.addEventListener('click', function (ev) { var h = ev.target.closest('.ap2-r-hit'); if (h) marcar(+h.getAttribute('data-k')); });
    w.addEventListener('keydown', function (ev) { var h = ev.target.closest && ev.target.closest('.ap2-r-hit'); if (h && (ev.key === 'Enter' || ev.key === ' ')) { ev.preventDefault(); marcar(+h.getAttribute('data-k')); } });
    despuesDe(blk, w);
  };
  // Esquema y rótulos: tocar un nombre y después el lugar (los desplegables quedan como alternativa)
  function bancoNombres(blk, layout) {
    var sels = blk.querySelectorAll('select.mt-sel'); if (!sels.length) return;
    var vals = []; [].forEach.call(sels[0].options, function (o) { if (o.value && vals.indexOf(o.value) < 0) vals.push(o.value); });
    var ps = blk.querySelector('.mt-pares'); if (layout && ps) ps.classList.add('ap2-esq', layout === 'arbol' ? 'arbol' : 'grilla');
    var banco = mk('div', 'ap2-banco', vals.map(function (v) { return '<button type="button" class="ap2-chip" data-v="' + esc(v) + '">' + esc(v) + '</button>'; }).join(''));
    var guia = mk('small', 'mt-ayuda', 'Tocá un nombre y después el lugar donde va.');
    var ref = ps || sels[0].closest('.mt-par'); ref.parentNode.insertBefore(guia, ref); ref.parentNode.insertBefore(banco, ref);
    var elegido = null;
    function usados() { if (vals.length < sels.length) return; var u = [].map.call(sels, function (s) { return s.value; }); [].forEach.call(banco.children, function (c) { c.classList.toggle('usado', u.indexOf(c.getAttribute('data-v')) >= 0); }); }
    banco.addEventListener('click', function (ev) { var c = ev.target.closest('.ap2-chip'); if (!c) return; elegido = c.getAttribute('data-v'); [].forEach.call(banco.children, function (x) { x.classList.toggle('on', x === c); }); });
    blk.addEventListener('click', function (ev) {
      if (elegido == null || ev.target.closest('.ap2-banco')) return;
      var par = ev.target.closest('.mt-par'), pt = ev.target.closest('.li-pt'), s = null;
      if (par) s = par.querySelector('select.mt-sel'); else if (pt) s = blk.querySelector('select.mt-sel[data-pt="' + pt.getAttribute('data-id') + '"]');
      if (!s) return; setVal(s, elegido); sonar('bien'); elegido = null; [].forEach.call(banco.children, function (x) { x.classList.remove('on'); }); usados();
    });
    blk.addEventListener('change', function (ev) { if (ev.target.matches('select.mt-sel')) usados(); });
    blk.addEventListener('mousedown', function (ev) { if (elegido != null && ev.target.matches('select.mt-sel')) ev.preventDefault(); }); // con un nombre elegido, tocar el desplegable lo completa
  }
  A.esquema = function (blk, arg) { bancoNombres(blk, arg === 'arbol' ? 'arbol' : 'grilla'); };
  A.arrastrar = function (blk) { bancoNombres(blk, null); };
  A.geoplano = function (blk, arg) {
    var inp = campoNum(blk); if (!inp) return;
    var a = String(arg || '').split(':'), n = Math.max(3, Math.min(10, parseInt(a[0], 10) || 6)), modo = a[1] === 'perimetro' ? 'perimetro' : 'area', S = 40, M = 20, Wd = M * 2 + S * (n - 1);
    var svg = '<svg viewBox="0 0 ' + Wd + ' ' + Wd + '" class="ap2-geo" role="group" aria-label="Cuadrícula"><polygon class="ap2-g-f"/><polyline class="ap2-g-l"/>';
    for (var y = 0; y < n; y++) for (var x = 0; x < n; x++) svg += '<circle class="ap2-g-p" cx="' + (M + x * S) + '" cy="' + (M + y * S) + '" r="7" data-x="' + x + '" data-y="' + y + '" tabindex="0" role="button" aria-label="Punto ' + (x + 1) + ', ' + (y + 1) + '"/>';
    var w = mk('div', 'ap2-caja', '<small class="mt-ayuda">Tocá los puntos uno por uno para hacer los lados. Para cerrar la figura, tocá el primer punto.</small>' + svg + '</svg>' +
      '<div class="ap2-val">—</div><div class="tk-pie"><button type="button" class="mt-boton suave chico" data-g="des">Deshacer</button> <button type="button" class="mt-boton suave chico" data-g="bor">Borrar</button></div>');
    var P = [], cerrada = false, lab = w.querySelector('.ap2-val');
    function dib() {
      var pts = P.map(function (p) { return (M + p[0] * S) + ',' + (M + p[1] * S); }).join(' ');
      w.querySelector('.ap2-g-l').setAttribute('points', pts + (cerrada && P.length ? ' ' + (M + P[0][0] * S) + ',' + (M + P[0][1] * S) : ''));
      w.querySelector('.ap2-g-f').setAttribute('points', cerrada ? pts : '');
      [].forEach.call(w.querySelectorAll('.ap2-g-p'), function (c) { c.classList.toggle('on', P.some(function (p) { return p[0] === +c.getAttribute('data-x') && p[1] === +c.getAttribute('data-y'); })); });
      if (!cerrada) { lab.textContent = P.length ? 'Seguí: cerrá la figura tocando el primer punto' : '—'; setVal(inp, ''); return; }
      var ar = 0, per = 0; P.forEach(function (p, k) { var q = P[(k + 1) % P.length]; ar += p[0] * q[1] - q[0] * p[1]; per += Math.hypot(q[0] - p[0], q[1] - p[1]); });
      ar = Math.abs(ar) / 2; var v = modo === 'area' ? ar : per;
      lab.textContent = (modo === 'area' ? 'Área: ' : 'Perímetro: ') + dec(v) + (modo === 'area' ? ' cuadraditos' : ' lados de cuadradito');
      setVal(inp, dec(v)); sonar('bien');
    }
    function tocar(c) {
      var p = [+c.getAttribute('data-x'), +c.getAttribute('data-y')];
      if (cerrada) return;
      if (P.length >= 3 && p[0] === P[0][0] && p[1] === P[0][1]) { cerrada = true; dib(); return; }
      if (P.some(function (q) { return q[0] === p[0] && q[1] === p[1]; })) return;
      P.push(p); dib();
    }
    w.addEventListener('click', function (ev) {
      var c = ev.target.closest('.ap2-g-p'); if (c) return tocar(c);
      var b = ev.target.closest('[data-g]'); if (!b) return;
      if (b.getAttribute('data-g') === 'des') { if (cerrada) cerrada = false; else P.pop(); } else { P = []; cerrada = false; } dib();
    });
    w.addEventListener('keydown', function (ev) { if ((ev.key === 'Enter' || ev.key === ' ') && ev.target.classList && ev.target.classList.contains('ap2-g-p')) { ev.preventDefault(); tocar(ev.target); } });
    despuesDe(blk, w);
  };
  A.funcion = function (blk, arg) {
    var hs = blk.querySelectorAll('.mt-hueco'); if (hs.length < 2) return;
    var r = Math.max(3, Math.min(8, parseInt(arg, 10) || 5)), S = 30, M = 18, Wd = M * 2 + S * 2 * r;
    function X(v) { return M + (v + r) * S; } function Y(v) { return M + (r - v) * S; }
    var svg = '<svg viewBox="0 0 ' + Wd + ' ' + Wd + '" class="ap2-fn" role="group" aria-label="Plano cartesiano">';
    for (var k = -r; k <= r; k++) svg += '<line class="ap2-fn-g' + (k === 0 ? ' eje' : '') + '" x1="' + X(k) + '" y1="' + Y(-r) + '" x2="' + X(k) + '" y2="' + Y(r) + '"/><line class="ap2-fn-g' + (k === 0 ? ' eje' : '') + '" x1="' + X(-r) + '" y1="' + Y(k) + '" x2="' + X(r) + '" y2="' + Y(k) + '"/>' +
      (k && k % 1 === 0 ? '<text class="ap2-fn-n" x="' + X(k) + '" y="' + (Y(0) + 14) + '">' + k + '</text><text class="ap2-fn-n" x="' + (X(0) - 10) + '" y="' + (Y(k) + 4) + '">' + k + '</text>' : '');
    svg += '<line class="ap2-fn-l" style="display:none"/>';
    for (var x = -r; x <= r; x++) for (var y = -r; y <= r; y++) svg += '<circle class="ap2-fn-p" cx="' + X(x) + '" cy="' + Y(y) + '" r="6" data-x="' + x + '" data-y="' + y + '" tabindex="0" role="button" aria-label="Punto (' + x + ', ' + y + ')"/>';
    var w = mk('div', 'ap2-caja', '<small class="mt-ayuda">Marcá dos puntos de la recta. Se completan solos la pendiente y la ordenada al origen.</small>' + svg + '</svg><div class="ap2-val">—</div>');
    var P = [], lab = w.querySelector('.ap2-val'), ln = w.querySelector('.ap2-fn-l');
    function act() {
      [].forEach.call(w.querySelectorAll('.ap2-fn-p'), function (c) { c.classList.toggle('on', P.some(function (p) { return p[0] === +c.getAttribute('data-x') && p[1] === +c.getAttribute('data-y'); })); });
      if (P.length < 2) { ln.style.display = 'none'; lab.textContent = P.length ? 'Marcá el segundo punto' : '—'; return; }
      var dx = P[1][0] - P[0][0], dy = P[1][1] - P[0][1];
      if (!dx) { ln.style.display = 'none'; lab.textContent = 'Esa recta es vertical: no es una función. Probá con otros puntos.'; setVal(hs[0], ''); setVal(hs[1], ''); return; }
      var bn = P[0][1] * dx - dy * P[0][0], m = frac(dy, dx), b = frac(bn, dx);
      var m0 = dy / dx, b0 = bn / dx; ln.style.display = '';
      ln.setAttribute('x1', X(-r)); ln.setAttribute('y1', Y(m0 * -r + b0)); ln.setAttribute('x2', X(r)); ln.setAttribute('y2', Y(m0 * r + b0));
      lab.textContent = 'y = ' + m + 'x ' + (b0 < 0 ? '− ' + frac(-bn, dx) : '+ ' + b); setVal(hs[0], m); setVal(hs[1], b); sonar('bien');
    }
    function tocar(c) { var p = [+c.getAttribute('data-x'), +c.getAttribute('data-y')]; if (P.length >= 2) P = []; if (!P.some(function (q) { return q[0] === p[0] && q[1] === p[1]; })) P.push(p); act(); }
    w.addEventListener('click', function (ev) { var c = ev.target.closest('.ap2-fn-p'); if (c) tocar(c); });
    w.addEventListener('keydown', function (ev) { if ((ev.key === 'Enter' || ev.key === ' ') && ev.target.classList && ev.target.classList.contains('ap2-fn-p')) { ev.preventDefault(); tocar(ev.target); } });
    var p = blk.querySelector('.mt-hueco-p'); p.parentNode.insertBefore(w, p.nextSibling);
  };

  // ---------- Grupo 3 (simplificados) ----------
  var COL_AT = { H: '#e9f1f0', O: '#ff8a7a', C: '#4a5a5c', N: '#7fb6ff', Cl: '#8be38f', Na: '#b9a6ff', S: '#ffe27a' };
  A.molecula = function (blk, arg) {
    var inp = blk.querySelector('input.mt-txt'); if (!inp) return;
    var el = String(arg || 'H,O').split(',').map(function (x) { return x.trim(); }).filter(Boolean);
    inp.readOnly = true; inp.classList.add('ap2-oculto');
    var w = mk('div', 'ap2-caja', '<small class="mt-ayuda">Tocá los átomos para sumarlos a la molécula. Tocá un átomo de la molécula para sacarlo.</small>' +
      '<div class="ap2-at-banco">' + el.map(function (e) { return '<button type="button" class="ap2-at" data-e="' + esc(e) + '" style="--a:' + (COL_AT[e] || '#7FD3C4') + '">' + esc(e) + '</button>'; }).join('') + '</div>' +
      '<div class="ap2-mol" aria-live="polite"></div><div class="ap2-val">—</div>');
    var mol = w.querySelector('.ap2-mol'), lab = w.querySelector('.ap2-val');
    function act() {
      var c = {}; [].forEach.call(mol.children, function (a) { var e = a.getAttribute('data-e'); c[e] = (c[e] || 0) + 1; });
      var f = el.filter(function (e) { return c[e]; }).map(function (e) { return e + (c[e] > 1 ? c[e] : ''); }).join('');
      lab.innerHTML = f ? esc(f).replace(/(\d+)/g, '<sub>$1</sub>') : '—'; setVal(inp, f);
    }
    w.addEventListener('click', function (ev) {
      var b = ev.target.closest('.ap2-at'); if (!b) return;
      if (b.parentNode === mol) b.remove(); else { if (mol.children.length >= 16) return; mol.appendChild(b.cloneNode(true)); sonar('bien'); }
      act();
    });
    despuesDe(blk, w);
  };
  var ICO_PZ = [[/pila|bater/i, '🔋'], [/lampar|foco|bombi|luz/i, '💡'], [/interrup|llave|switch/i, '🔘'], [/cable|conduct/i, '〰️'], [/motor/i, '⚙️'], [/timbre/i, '🔔'], [/resist/i, '▭'], [/goma|madera|pl[aá]stic|aislant/i, '🚫']];
  function icoPz(t) { for (var k = 0; k < ICO_PZ.length; k++) if (ICO_PZ[k][0].test(t)) return ICO_PZ[k][1]; return '●'; }
  function armar(blk, circuito) {
    var ops = blk.querySelector('.mt-ops'); if (!ops) return;
    var w = mk('div', 'ap2-caja ap2-sis' + (circuito ? ' circ' : ''), '<small class="mt-ayuda">' + (circuito ? 'Elegí las piezas: se van armando en el circuito.' : 'Elegí las partes: se van armando en el sistema.') + '</small><div class="ap2-sis-c"></div>');
    var cont = w.querySelector('.ap2-sis-c'), orden = [];
    function act() {
      [].forEach.call(ops.querySelectorAll('input'), function (i) { var v = i.value, k = orden.indexOf(v); if (i.checked && k < 0) orden.push(v); if (!i.checked && k >= 0) orden.splice(k, 1); });
      cont.innerHTML = orden.length ? orden.map(function (v) { return '<span class="ap2-sis-p">' + (circuito ? '<i aria-hidden="true">' + icoPz(v) + '</i>' : '') + esc(v) + '</span>'; }).join('<b class="ap2-sis-u" aria-hidden="true">' + (circuito ? '' : '➜') + '</b>') : '<em>Todavía no elegiste nada</em>';
    }
    ops.addEventListener('change', act); ops.parentNode.insertBefore(w, ops); act();
  }
  A.circuito = function (blk) { armar(blk, true); };
  A.sistema = function (blk) { armar(blk, false); };
  A.simulador = function (blk, arg) {
    var partes = String(arg || '').split(';'), ent = partes[0].split(','), nom = (ent[0] || 'x').trim(), mn = parseFloat(ent[1]) || 0, mx = parseFloat(ent[2]), st = parseFloat(ent[3]) || 1, un = (ent[4] || '').trim();
    if (!(mx > mn)) mx = mn + 10;
    var sal = partes.slice(1).map(function (s) { var x = s.split(','); return { n: (x[0] || '').trim(), f: (x[1] || '').trim(), u: (x[2] || '').trim() }; }).filter(function (s) { return s.n && s.f; });
    if (!sal.length || !window.WaveCalc || !WaveCalc.evaluar) return;
    function ev(f, x) { try { var v = WaveCalc.evaluar(f, { x: x }); return isFinite(v) ? v : NaN; } catch (_) { return NaN; } }
    sal.forEach(function (s) { var a = [], v; for (v = mn; v <= mx + 1e-9; v += st) a.push(ev(s.f, v)); a = a.filter(isFinite); s.lo = Math.min.apply(null, a.concat(0)); s.hi = Math.max.apply(null, a.concat(1)); });
    var w = mk('div', 'ap2-caja ap2-sim', '<small class="mt-ayuda">Mové el control y mirá qué cambia. Después respondé.</small>' +
      '<label class="ap2-sim-in"><b>' + esc(nom) + ': <span></span> ' + esc(un) + '</b><input type="range" min="' + mn + '" max="' + mx + '" step="' + st + '" value="' + mn + '"></label>' +
      sal.map(function (s, k) { return '<div class="ap2-sim-o" data-k="' + k + '"><span>' + esc(s.n) + '</span><div class="ap2-sim-b"><i></i></div><b></b></div>'; }).join(''));
    var rg = w.querySelector('input[type=range]');
    function act() {
      var x = parseFloat(rg.value); w.querySelector('.ap2-sim-in span').textContent = dec(x);
      sal.forEach(function (s, k) { var o = w.querySelector('.ap2-sim-o[data-k="' + k + '"]'), v = ev(s.f, x);
        o.querySelector('b').textContent = isFinite(v) ? dec(v) + (s.u ? ' ' + s.u : '') : '—';
        o.querySelector('i').style.width = isFinite(v) && s.hi > s.lo ? Math.max(2, Math.round((v - s.lo) / (s.hi - s.lo) * 100)) + '%' : '0'; });
    }
    rg.addEventListener('input', act); despuesDe(blk, w); act();
  };
  A.capas = function (blk, arg) {
    var ta = blk.querySelector('textarea.mt-txt'); if (!ta) return;
    var cs = String(arg || '').split('|').map(function (x) { return x.trim(); }).filter(Boolean); if (cs.length < 2) return;
    ta.classList.add('ap2-oculto');
    var w = mk('div', 'ap2-capas', '<div class="ap2-capas-h">' + cs.map(function (c, k) { return '<span data-c="' + k + '">' + (k + 1) + '. ' + esc(c) + '</span>'; }).join('') + '</div>' +
      cs.map(function (c, k) { return '<label class="mt-lbl">' + (k + 1) + '. ' + esc(c) + '</label><textarea class="mt-txt ap2-capa" data-c="' + k + '" rows="3" maxlength="1500" placeholder="Escribí esta parte"></textarea>'; }).join(''));
    w.addEventListener('input', function (ev) {
      if (!ev.target.classList.contains('ap2-capa')) return;
      var tx = [].map.call(w.querySelectorAll('.ap2-capa'), function (t, k) { w.querySelector('.ap2-capas-h [data-c="' + k + '"]').classList.toggle('on', !!t.value.trim()); return t.value.trim() ? cs[k] + ': ' + t.value.trim() : ''; }).filter(Boolean).join('\n\n');
      setVal(ta, tx);
    });
    ta.parentNode.insertBefore(w, ta);
  };

  // ---------- Recorrido ----------
  function recorrer() {
    [].forEach.call(document.querySelectorAll('.wvp.act .mt-preg:not([data-ap2])'), function (blk) {
      blk.setAttribute('data-ap2', '1');
      var tx = blk.textContent || '', re = new RegExp(RE.source, 'g'), m, ms = [];
      while ((m = re.exec(tx))) ms.push(m);
      if (!ms.length) return;
      quitar(blk);
      var tp = blk.querySelector('.mt-tipo'), nm = NOMBRE[ms[0][1]]; if (tp && nm) tp.innerHTML = '<span aria-hidden="true">' + nm[0] + '</span> ' + esc(nm[1]);
      ms.forEach(function (x) { try { A[x[1]](blk, x[2]); } catch (e) { if (window.console) console.warn('Actividad plus', x[1], e); } });
    });
    [].forEach.call(document.querySelectorAll('.wvp'), function (v) { if ((v.textContent || '').indexOf('[[') >= 0) quitar(v); });
  }
  var css = document.createElement('style');
  css.textContent = [
    '.ap2-oculto{position:absolute!important;width:1px!important;height:1px!important;opacity:0!important;pointer-events:none!important;overflow:hidden!important}',
    '.ap2-caja{margin:8px 0 4px;text-align:center}.ap2-caja .mt-ayuda{text-align:left}.ap2-val{margin-top:10px;font-weight:800;font-size:1.3rem;color:var(--turquesa-oscuro,#066A6E)}',
    '.ap2-pasos{counter-reset:ap2p}.ap2-pasos .tp-seg{counter-increment:ap2p;font-family:inherit}.ap2-pasos .tp-seg::before{content:"Paso " counter(ap2p);display:block;font-size:.75rem;font-weight:800;color:#066A6E;margin-bottom:2px}',
    '.ap2-sec{display:flex;flex-wrap:wrap;align-items:center;gap:8px;line-height:1.6}.ap2-paso{display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap;padding:10px 12px;border:2px solid #E3ECEA;border-radius:14px;background:#fff}.ap2-flecha{color:#087E83;font-weight:900}',
    '.ap2-comp{grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}.ap2-comp .mt-op{flex-direction:column;align-items:flex-start!important;text-align:left}.ap2-comp-t{font-weight:800;color:#066A6E;font-size:.78rem}.ap2-comp .mt-op-l{position:absolute;top:10px;right:10px}.ap2-comp .mt-op span{font-family:inherit;line-height:1.55}',
    '.ap2-causas-h{display:flex;justify-content:space-between;padding:0 14px;font-size:.78rem;font-weight:800;color:#066A6E}.ap2-causas .mt-par .ap2-flecha{flex:none}',
    '.wvp.act .ap2-etapas li::before{content:"Etapa " counter(ord);width:auto;padding:0 10px;border-radius:99px}',
    '.wvp.act .ap2-linea{position:relative;padding-left:26px}.wvp.act .ap2-linea::before{content:"";position:absolute;left:9px;top:8px;bottom:8px;width:4px;border-radius:4px;background:#D7F0E9}.wvp.act .ap2-linea li{position:relative}.wvp.act .ap2-linea li::after{content:"";position:absolute;left:-23px;top:50%;width:14px;height:14px;margin-top:-7px;border-radius:50%;background:#087E83;border:3px solid #fff}',
    '.ap2-roles{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:10px;font-weight:800;font-size:.85rem}.ap2-roles span{padding:4px 12px;border-radius:99px;border:2px dashed #9dbdb9;color:#4b6a6c}.ap2-roles span.on{border-style:solid;border-color:#087E83;background:#D7F0E9;color:#253638}.ap2-roles i{font-style:normal;color:#9dbdb9}',
    'mark.ap2-dato{background:#D7F0E9;color:#253638;padding:0 4px;border-radius:6px;font-weight:900}.ap2-borr{margin:0 0 12px}.ap2-borr summary{cursor:pointer;font-weight:800;font-size:.88rem;color:#066A6E}.ap2-borr textarea{width:100%;margin-top:8px;padding:10px 12px;border:2px dashed #9dbdb9;border-radius:14px;font:inherit;box-sizing:border-box;background:#fff}',
    '.ap2-piezas{display:flex;flex-direction:column;gap:10px;align-items:center}.ap2-barra{display:flex;width:100%;max-width:520px;height:58px;border:3px solid #253638;border-radius:12px;overflow:hidden}.ap2-barra .ap2-pz{flex:1;border:0;border-right:2px solid #253638;background:#fff;cursor:pointer;padding:0}.ap2-barra .ap2-pz:last-child{border-right:0}',
    '.ap2-pz.on{background:#087E83!important;fill:#087E83!important}.ap2-piezas:has(.ap2-circ){flex-direction:row;flex-wrap:wrap;justify-content:center}.ap2-circ{width:170px;height:170px}.ap2-circ .ap2-pz{fill:#fff;stroke:#253638;stroke-width:.03;cursor:pointer}.ap2-pz:focus-visible{outline:3px solid #087E83}',
    '.ap2-pool{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;min-height:52px;padding:10px;border:2px dashed #9dbdb9;border-radius:16px}.ap2-ob{font-size:26px;line-height:1;border:0;background:none;cursor:pointer;padding:4px}',
    '.ap2-platos{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-top:12px}.ap2-plato{min-height:96px;padding:8px;border:2px solid #E3ECEA;border-radius:18px;background:#fff;cursor:pointer}.ap2-plato.sel{border-color:#087E83;background:#F3FBF7;box-shadow:0 0 0 2px #087E83 inset}.ap2-plato b{display:block;font-size:.82rem;color:#253638}.ap2-pl-c{display:flex;flex-wrap:wrap;justify-content:center}',
    '.ap2-recta{width:100%;max-width:620px}.ap2-r-l{stroke:#253638;stroke-width:3}.ap2-r-t{stroke:#253638;stroke-width:2}.ap2-r-n{font-weight:800;font-size:15px;fill:#253638;text-anchor:middle}.ap2-r-n.chico{font-size:12px;fill:#4b6a6c}.ap2-r-hit{fill:transparent;cursor:pointer}.ap2-r-hit:hover{fill:rgba(8,126,131,.08)}.ap2-r-pt circle,.ap2-r-pt path{fill:#087E83}',
    '.ap2-banco{display:flex;flex-wrap:wrap;gap:8px;margin:4px 0 12px}.ap2-chip{padding:8px 14px;border:2px solid #E3ECEA;border-bottom-width:4px;border-radius:14px;background:#fff;font:inherit;font-weight:800;cursor:pointer;color:#253638}.ap2-chip.on{border-color:#087E83;background:#D7F0E9}.ap2-chip.usado{opacity:.45}',
    '.wvp.act .ap2-esq .mt-par .mt-sel{min-width:0;width:100%;max-width:100%}.ap2-esq.grilla{grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}.ap2-esq .mt-par{flex-direction:column;align-items:stretch;text-align:center;cursor:pointer}.ap2-esq .mt-par .mt-sel{max-width:100%;min-width:0}.ap2-esq.arbol{grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}.ap2-esq.arbol .mt-par:first-child{grid-column:1/-1;justify-self:center;min-width:240px;border-color:#087E83}',
    '.ap2-geo{width:100%;max-width:320px}.ap2-g-p{fill:#9dbdb9;cursor:pointer}.ap2-g-p.on{fill:#087E83}.ap2-g-l{fill:none;stroke:#087E83;stroke-width:4;stroke-linejoin:round}.ap2-g-f{fill:rgba(8,126,131,.18)}',
    '.ap2-fn{width:100%;max-width:340px}.ap2-fn-g{stroke:#E3ECEA;stroke-width:1}.ap2-fn-g.eje{stroke:#253638;stroke-width:2}.ap2-fn-n{font-weight:700;font-size:10px;fill:#4b6a6c;text-anchor:middle}.ap2-fn-p{fill:transparent;cursor:pointer}.ap2-fn-p:hover{fill:rgba(8,126,131,.25)}.ap2-fn-p.on{fill:#087E83}.ap2-fn-l{stroke:#087E83;stroke-width:3}',
    '.ap2-at-banco{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}.ap2-at{width:56px;height:56px;border-radius:50%;border:3px solid #253638;background:var(--a);font:inherit;font-weight:900;font-size:1.1rem;cursor:pointer;color:#253638}',
    '.ap2-mol{display:flex;flex-wrap:wrap;gap:4px;justify-content:center;align-items:center;min-height:72px;margin-top:12px;padding:10px;border:2px dashed #9dbdb9;border-radius:18px}.ap2-mol .ap2-at{width:46px;height:46px}',
    '.ap2-sis-c{display:flex;flex-wrap:wrap;gap:6px;align-items:center;justify-content:center;min-height:70px;padding:12px;border:2px dashed #9dbdb9;border-radius:18px;margin-bottom:12px}.ap2-sis-c em{color:#4b6a6c}.ap2-sis-p{display:inline-flex;align-items:center;gap:6px;padding:8px 12px;border:2px solid #087E83;border-radius:14px;background:#fff;font-weight:800}.ap2-sis-p i{font-style:normal;font-size:22px}',
    '.ap2-sis.circ .ap2-sis-c{border:4px solid #253638;border-radius:26px}.ap2-sis.circ .ap2-sis-u{width:22px;height:4px;background:#253638}.ap2-sis-u{color:#087E83}',
    '.ap2-sim{text-align:left;padding:14px;border:2px solid #E3ECEA;border-radius:18px;background:#fff;margin-bottom:12px}.ap2-sim-in{display:block}.ap2-sim-in input{width:100%;accent-color:#087E83;margin:8px 0}.ap2-sim-o{display:grid;grid-template-columns:minmax(90px,auto) 1fr auto;gap:10px;align-items:center;margin-top:8px;font-weight:800}.ap2-sim-b{height:14px;border-radius:99px;background:#E3ECEA;overflow:hidden}.ap2-sim-b i{display:block;height:100%;background:#087E83;transition:width .2s}',
    '.ap2-capas-h{display:flex;flex-wrap:wrap;gap:6px}.ap2-capas-h span{padding:4px 12px;border-radius:99px;background:#E3ECEA;font-weight:800;font-size:.8rem;color:#4b6a6c}.ap2-capas-h span.on{background:#087E83;color:#fff}',
    '.ap-sin-anim .ap2-sim-b i{transition:none}'
  ].join('');
  document.head.appendChild(css);
  var pend = false;
  function prog() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; try { recorrer(); } catch (e) {} }); }
  function iniciar() { new MutationObserver(prog).observe(document.body, { childList: true, subtree: true }); prog(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
