/* BANCO DE LA LECCIÓN INTERACTIVA (Matemática). SEPARADO del banco de actividades: estos motores solo se usan
   dentro de la lección (js/leccion-interactiva.js) y nunca en actividades ni exámenes.
   Cada motor: { tipo: 'ejemplo' | 'ejercicio', nombre, render(el, p, api) }.
   - ejemplo: escena viva al lado de la explicación (el alumno cambia el número y la escena responde).
   - ejercicio: lo abre el botón del tema; "Otros números" lo regenera; "Comprobar" corrige en el momento (no lleva nota).
   La máquina (tools/interactiva/armar.js) elige motor y modo para cada tema. */
window.WaveLeccionBanco = (function () {
  'use strict';
  // ---------- utilidades ----------
  function R(a, b) { return a + Math.floor(Math.random() * (b - a + 1)); }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function mezclar(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function divisores(n) { var r = []; for (var i = 1; i <= n; i++) if (n % i === 0) r.push(i); return r; }
  function esPrimo(n) { if (n < 2) return false; for (var i = 2; i * i <= n; i++) if (n % i === 0) return false; return true; }
  function mcd(a, b) { while (b) { var t = b; b = a % b; a = t; } return a; }
  function mcm(a, b) { return a / mcd(a, b) * b; }
  function fmt(n) { var neg = n < 0, s = String(Math.abs(Math.round(n * 1e6) / 1e6)).split('.'); return (neg ? '−' : '') + s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.') + (s[1] ? ',' + s[1] : ''); }
  function sig(n) { return n > 0 ? '+' + n : n < 0 ? '−' + Math.abs(n) : '0'; }
  function num(s) { s = String(s).trim().replace(/−/g, '-').replace(/\s+/g, ''); if (/,/.test(s)) s = s.replace(/\./g, '').replace(',', '.'); else if (/^-?\d{1,3}(\.\d{3})+$/.test(s)) s = s.replace(/\./g, ''); return s === '' ? NaN : Number(s); }
  function norm(s) { return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9ñ ]/g, ' ').replace(/\s+/g, ' ').trim(); }
  // números en letras (hasta 999.999.999)
  var U = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve',
    'veinte', 'veintiuno', 'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis', 'veintisiete', 'veintiocho', 'veintinueve'];
  var DE = ['', '', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'];
  var CE = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos'];
  function menor1000(n) {
    if (n === 100) return 'cien';
    var c = Math.floor(n / 100), r = n % 100, out = c ? CE[c] : '';
    if (r) out += (out ? ' ' : '') + (r < 30 ? U[r] : DE[Math.floor(r / 10)] + (r % 10 ? ' y ' + U[r % 10] : ''));
    return out || 'cero';
  }
  function apocope(s) { return s.replace(/veintiuno$/, 'veintiún').replace(/(^|\s)uno$/, '$1un'); }
  function letras(n) {
    if (n === 0) return 'cero';
    var m = Math.floor(n / 1e6), k = Math.floor(n % 1e6 / 1000), r = n % 1000, out = [];
    if (m) out.push(m === 1 ? 'un millón' : apocope(menor1000(m)) + ' millones');
    if (k) out.push(k === 1 ? 'mil' : apocope(menor1000(k)) + ' mil');
    if (r) out.push(menor1000(r));
    return out.join(' ');
  }
  var PARTES = ['', '', 'medios', 'tercios', 'cuartos', 'quintos', 'sextos', 'séptimos', 'octavos', 'novenos', 'décimos'];
  function partes(d, uno) {
    var s = d <= 10 ? PARTES[d] : norm(letras(d)).replace(/ /g, '') + 'avos';
    return uno ? s.replace(/s$/, '').replace(/avo$/, 'avo') : s;
  }
  function fraccionEnLetras(a, d) { return (a === 1 ? 'un' : apocope(letras(a))) + ' ' + partes(d, a === 1); }

  // ---------- piezas comunes de pantalla ----------
  // junta 'n' elementos distintos alternando dos generadores, con tope de intentos (nunca se cuelga)
  function juntar(n, genA, genB) { var s = {}, out = [], t = 0; while (out.length < n && t++ < 3000) { var x = (out.length % 2 && genB ? genB : genA)(); if (!s[x]) { s[x] = 1; out.push(x); } } return out; }
  function chip(v, txt, extra) { return '<button type="button" class="lb-chip"' + (extra || '') + ' data-v="' + esc(v) + '">' + (txt != null ? txt : esc(v)) + '</button>'; }
  function fr(a, b) { return '<span class="lb-fr"><i>' + a + '</i><i>' + b + '</i></span>'; }
  // Esqueleto de ejercicio: consigna + cuerpo + Comprobar + Otros números. armar(cuerpo) devuelve { comprobar(): {ok, msg}, resolver() }
  function ejercicio(el, api, consigna, armar) {
    var ctl = null;
    el.innerHTML = '<p class="lb-cons">' + consigna + '</p><div class="lb-cuerpo"></div><div class="lb-fb" aria-live="polite"></div>' +
      '<div class="lb-pie"><button type="button" class="lb-btn" data-lb="comp">Comprobar</button><button type="button" class="lb-btn suave" data-lb="otro">🔄 Otros números</button></div>';
    var cuerpo = el.querySelector('.lb-cuerpo'), fb = el.querySelector('.lb-fb');
    function nuevo() { fb.innerHTML = ''; cuerpo.innerHTML = ''; var cc = document.createElement('div'); cuerpo.appendChild(cc); ctl = armar(cc); }
    el.onclick = function (e) {
      var b = e.target.closest('[data-lb]'); if (!b) return;
      if (b.getAttribute('data-lb') === 'otro') return nuevo();
      if (b.getAttribute('data-lb') === 'comp' && ctl) {
        var r = ctl.comprobar(); api.sonar(r.ok ? 'bien' : 'mal'); if (r.ok) api.confeti(fb);
        fb.innerHTML = '<div class="' + (r.ok ? 'lb-ok' : 'lb-no') + '">' + (r.ok ? '✔ ' : '✘ ') + r.msg + '</div>';
        if (api.alResultado && !/^(Te faltan|Completá|Escribí|Tocá una)/.test(r.msg)) api.alResultado(r.ok); // incompleto: no cuenta como intento
      }
    };
    nuevo();
    el._lb = { resolver: function () { ctl.resolver(); }, comprobar: function () { return ctl.comprobar(); }, nuevo: nuevo };
  }
  // Tocar una ficha y después el lugar (o volver a tocarla para devolverla al banco)
  function tocarYUbicar(cont, alMover) {
    var sel = null;
    cont.addEventListener('click', function (e) {
      var c = e.target.closest('.lb-chip'), dest = e.target.closest('[data-dest]'), banco = cont.querySelector('.lb-banco');
      if (c && c.parentNode !== banco && !sel) { banco.appendChild(c); c.classList.remove('bien', 'mal'); if (alMover) alMover(); return; }
      if (c && c.parentNode === banco) { if (sel) sel.classList.remove('on'); sel = sel === c ? null : c; if (sel) sel.classList.add('on'); return; }
      if (dest && sel) {
        var max = +dest.getAttribute('data-max') || 0;
        if (max && dest.querySelectorAll('.lb-chip').length >= max) { var viejo = dest.querySelector('.lb-chip'); banco.appendChild(viejo); }
        (dest.querySelector('.lb-dest-c') || dest).appendChild(sel); sel.classList.remove('on'); sel = null; if (alMover) alMover();
      }
    });
  }

  var M = {};

  // =============== EJEMPLOS (escena viva) ===============
  // 1. Explorador de un número: múltiplos, divisores o primo
  M.explorador = { tipo: 'ejemplo', nombre: 'Explorador de un número', render: function (el, p) {
    var modo = p.modo || 'multiplos', n0 = modo === 'multiplos' ? R(3, 15) : pick([12, 18, 20, 24, 30, 36, 13, 17, 28, 45]);
    el.innerHTML = '<div class="lb-in-f"><label>Escribí un número</label><input type="text" inputmode="numeric" class="lb-inp" value="' + n0 + '" maxlength="4"></div><div class="lb-vista"></div>';
    var inp = el.querySelector('input'), v = el.querySelector('.lb-vista');
    function pintar() {
      var n = Math.floor(num(inp.value));
      if (!(n >= 1 && n <= 9999)) { v.innerHTML = '<p class="lb-ayuda">Probá con un número del 1 al 9999.</p>'; return; }
      if (modo === 'multiplos') {
        v.innerHTML = '<h5>Los múltiplos de ' + fmt(n) + ' son:</h5><div class="lb-grilla">' + Array.apply(null, Array(30)).map(function (_, k) { return '<span>' + fmt(n * k) + '</span>'; }).join('') + '<span>…</span></div><p class="lb-nota">Tiene infinitos múltiplos: se obtienen multiplicando ' + fmt(n) + ' por 0, 1, 2, 3…</p>';
      } else {
        var d = divisores(n), pr = d.length === 2;
        v.innerHTML = '<h5>Los divisores de ' + fmt(n) + ' son:</h5><div class="lb-grilla">' + d.map(function (x) { return '<span class="on">' + fmt(x) + '</span>'; }).join('') + '</div>' +
          '<p class="lb-nota">Tiene <b>' + d.length + '</b> divisor' + (d.length === 1 ? '' : 'es') + '.' + (modo === 'primo' ? (n === 1 ? ' El 1 no es primo ni compuesto.' : pr ? ' Solo se divide por 1 y por sí mismo: <b>es primo</b>.' : ' Tiene más de dos divisores: <b>es compuesto</b>.') : '') + '</p>';
      }
    }
    inp.addEventListener('input', pintar); pintar();
  } };

  // 2. Explorador de dos números: mcd (divisores comunes) o mcm (múltiplos comunes)
  M.explorador2 = { tipo: 'ejemplo', nombre: 'Explorador de dos números', render: function (el, p) {
    var modo = p.modo === 'mcm' ? 'mcm' : 'mcd', a0 = modo === 'mcd' ? pick([12, 18, 24, 30, 36, 40]) : pick([4, 6, 8, 9, 10, 12]), b0 = modo === 'mcd' ? pick([16, 20, 27, 42, 45, 60]) : pick([6, 10, 14, 15, 16]);
    el.innerHTML = '<div class="lb-in-f dos"><label>Un número</label><input type="text" inputmode="numeric" class="lb-inp" value="' + a0 + '" maxlength="3"><label>Otro número</label><input type="text" inputmode="numeric" class="lb-inp" value="' + b0 + '" maxlength="3"></div><div class="lb-vista"></div>';
    var ins = el.querySelectorAll('input'), v = el.querySelector('.lb-vista');
    function pintar() {
      var a = Math.floor(num(ins[0].value)), b = Math.floor(num(ins[1].value));
      if (!(a >= 1 && a <= 200 && b >= 1 && b <= 200)) { v.innerHTML = '<p class="lb-ayuda">Probá con números del 1 al 200.</p>'; return; }
      if (modo === 'mcd') {
        var da = divisores(a), db = divisores(b), m = mcd(a, b);
        function fila(n, d, o) { return '<h5>Divisores de ' + n + '</h5><div class="lb-grilla">' + d.map(function (x) { return '<span class="' + (o.indexOf(x) >= 0 ? 'com' : '') + (x === m ? ' max' : '') + '">' + x + '</span>'; }).join('') + '</div>'; }
        v.innerHTML = fila(a, da, db) + fila(b, db, da) + '<p class="lb-nota">Los marcados son <b>divisores comunes</b>. El mayor es el <b>m.c.d.(' + a + ', ' + b + ') = ' + m + '</b>' + (m === 1 ? ': son primos entre sí.' : '.') + '</p>';
      } else {
        var m2 = mcm(a, b), tope = Math.max(m2 * 2, a * 6, b * 6), ma = [], mb = [];
        for (var x = a; x <= tope && ma.length < 14; x += a) ma.push(x);
        for (var y = b; y <= tope && mb.length < 14; y += b) mb.push(y);
        function fila2(n, l, o) { return '<h5>Múltiplos de ' + n + '</h5><div class="lb-grilla">' + l.map(function (x) { return '<span class="' + (o.indexOf(x) >= 0 ? 'com' : '') + (x === m2 ? ' max' : '') + '">' + fmt(x) + '</span>'; }).join('') + '<span>…</span></div>'; }
        v.innerHTML = fila2(a, ma, mb) + fila2(b, mb, ma) + '<p class="lb-nota">Los marcados son <b>múltiplos comunes</b> (sin contar el 0). El más chico es el <b>m.c.m.(' + a + ', ' + b + ') = ' + fmt(m2) + '</b>.</p>';
      }
    }
    [].forEach.call(ins, function (i) { i.addEventListener('input', pintar); }); pintar();
  } };

  // 3. Escalera de factores primos: el alumno pone cada factor
  M.escalera_factores = { tipo: 'ejemplo', nombre: 'Descomposición en factores primos', render: function (el, p, api) {
    var POOL = [12, 18, 24, 30, 36, 42, 45, 48, 60, 63, 72, 84, 90, 96, 100, 108, 120, 126, 150, 180, 210, 252, 300, 360];
    el.innerHTML = '<div class="lb-esc-w"></div><div class="lb-pie"><button type="button" class="lb-btn suave" data-e="otro">🔄 Otro número</button></div>';
    var w = el.querySelector('.lb-esc-w');
    function nuevo(n) {
      var filas = [n], fac = [];
      function pintar(msg) {
        var resto = filas[filas.length - 1], fin = resto === 1;
        var cuenta = {}; fac.forEach(function (f) { cuenta[f] = (cuenta[f] || 0) + 1; });
        w.innerHTML = '<div class="lb-esc"><div class="lb-esc-l">' + filas.map(function (x) { return '<span>' + fmt(x) + '</span>'; }).join('') + '</div><div class="lb-esc-r">' + fac.map(function (f) { return '<span>' + f + '</span>'; }).join('') +
          (fin ? '' : '<input type="text" inputmode="numeric" class="lb-inp chico" aria-label="Factor primo" placeholder="?" maxlength="3">') + '</div></div>' +
          (fin ? '<p class="lb-nota lb-res">' + fmt(n) + ' = ' + Object.keys(cuenta).map(function (k) { return k + (cuenta[k] > 1 ? '<sup>' + cuenta[k] + '</sup>' : ''); }).join(' · ') + '</p>'
            : '<p class="lb-ayuda">' + (msg || 'Escribí un número primo que divida a ' + fmt(resto) + ' y apretá Enter.') + '</p>');
        var i = w.querySelector('input'); if (i) { i.focus(); i.addEventListener('keydown', function (e) { if (e.key === 'Enter') probar(i.value); }); }
      }
      function probar(s) {
        var f = Math.floor(num(s)), r = filas[filas.length - 1];
        if (!esPrimo(f)) return pintar(f >= 1 ? f + ' no es primo. Usá 2, 3, 5, 7…' : 'Escribí un número primo.');
        if (r % f) return pintar(fmt(r) + ' no se puede dividir por ' + f + '. Probá con otro primo.');
        fac.push(f); filas.push(r / f); api.sonar('bien'); pintar();
      }
      pintar();
    }
    el.addEventListener('click', function (e) { if (e.target.closest('[data-e="otro"]')) nuevo(pick(POOL)); });
    nuevo(pick(POOL));
  } };

  // 4. Escalera de unidades (longitud, capacidad, masa)
  var UNI = { longitud: ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'], capacidad: ['kl', 'hl', 'dal', 'l', 'dl', 'cl', 'ml'], masa: ['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'],
    superficie: ['km²', 'hm²', 'dam²', 'm²', 'dm²', 'cm²', 'mm²'], volumen: ['km³', 'hm³', 'dam³', 'm³', 'dm³', 'cm³', 'mm³'] };
  var BASE_U = { superficie: 100, volumen: 1000 };
  M.escalera_unidades = { tipo: 'ejemplo', nombre: 'Escalera de unidades', render: function (el, p) {
    var us = UNI[p.magnitud] || UNI.longitud, base = BASE_U[p.magnitud] || 10, de = 3, a = 5;
    el.innerHTML = '<p class="lb-ayuda">Tocá la unidad de partida y después la de llegada.</p><div class="lb-esca"></div><div class="lb-in-f"><label>Cantidad</label><input type="text" inputmode="decimal" class="lb-inp" value="' + R(2, 90) + '"></div><div class="lb-vista"></div>';
    var esca = el.querySelector('.lb-esca'), inp = el.querySelector('input'), v = el.querySelector('.lb-vista'), paso = 0;
    function pintar() {
      esca.innerHTML = us.map(function (u, k) { return '<button type="button" class="lb-esc-u' + (k === de ? ' de' : '') + (k === a ? ' a' : '') + '" data-u="' + k + '" style="margin-left:' + k * 7 + '%">' + u + '</button>'; }).join('');
      var x = num(inp.value), d = a - de, f = Math.pow(base, Math.abs(d));
      if (!isFinite(x)) { v.innerHTML = '<p class="lb-ayuda">Escribí una cantidad.</p>'; return; }
      v.innerHTML = '<p class="lb-nota">Desde <b>' + us[de] + '</b> hasta <b>' + us[a] + '</b>: ' + (d === 0 ? 'es la misma unidad.' : (d > 0 ? 'bajás ' + d + ' escalón' + (d > 1 ? 'es' : '') + ': <b>× ' + fmt(f) + '</b>' : 'subís ' + (-d) + ' escalón' + (d < -1 ? 'es' : '') + ': <b>: ' + fmt(f) + '</b>')) + '</p>' +
        (d ? '<p class="lb-res">' + fmt(x) + ' ' + us[de] + ' = ' + fmt(d > 0 ? x * f : x / f) + ' ' + us[a] + '</p>' : '');
    }
    esca.addEventListener('click', function (e) { var b = e.target.closest('[data-u]'); if (!b) return; var k = +b.getAttribute('data-u'); if (paso === 0) { de = k; paso = 1; } else { a = k; paso = 0; } pintar(); });
    inp.addEventListener('input', pintar); pintar();
  } };

  // 5. Balanza de ecuaciones (inventada): a·x + b = c
  M.balanza = { tipo: 'ejemplo', nombre: 'Balanza de ecuaciones', render: function (el, p, api) {
    el.innerHTML = '<div class="lb-bal-w"></div><div class="lb-pie"><button type="button" class="lb-btn suave" data-b="otro">🔄 Otra ecuación</button></div>';
    var w = el.querySelector('.lb-bal-w');
    function nueva() {
      var a = R(2, 6), x = R(1, 12), b = R(1, 20), c = a * x + b, paso = 0;
      function pintar() {
        var izq = paso === 0 ? a + 'x + ' + b : paso === 1 ? a + 'x' : 'x', der = paso === 0 ? c : paso === 1 ? c - b : x;
        w.innerHTML = '<div class="lb-bal"><div class="lb-plato">' + izq + '</div><div class="lb-fiel">=</div><div class="lb-plato">' + fmt(der) + '</div></div>' +
          (paso === 0 ? '<button type="button" class="lb-btn" data-b="p">Sacar ' + b + ' de los dos platos</button>' : paso === 1 ? '<button type="button" class="lb-btn" data-b="p">Repartir los dos platos en ' + a + '</button>' : '<p class="lb-res">x = ' + x + '</p><p class="lb-nota">Comprobación: ' + a + ' · ' + x + ' + ' + b + ' = ' + c + ' ✔</p>');
      }
      w.onclick = function (e) { if (e.target.closest('[data-b="p"]')) { paso++; api.sonar('bien'); pintar(); } };
      pintar();
    }
    el.addEventListener('click', function (e) { if (e.target.closest('[data-b="otro"]')) nueva(); });
    nueva();
  } };

  // 6. Tu Paso a paso (HTML ya armado por herramientas/pasoapaso), en un marco aislado
  M.pasoapaso = { tipo: 'ejemplo', nombre: 'Paso a paso', render: function (el, p) {
    if (!/^\/actividades\/pasoapaso\/[a-z0-9-]+\.html$/.test(p.u || '')) { el.innerHTML = ''; return; }
    el.innerHTML = '<iframe class="lb-marco" title="Paso a paso" src="' + esc(p.u) + '" sandbox="allow-scripts allow-same-origin"></iframe>';
  } };

  // =============== EJERCICIOS ===============
  // 7. Cajas para clasificar
  M.cajas = { tipo: 'ejercicio', nombre: 'Cajas para clasificar', render: function (el, p, api) {
    var modo = p.modo || 'multiplos';
    function datos() {
      if (modo === 'multiplos') { var n = R(3, 9), L1 = juntar(12, function () { return n * R(2, Math.floor(99 / n)); }, function () { return R(2, 99); });
        return { tit: 'Ubicá cada número: ¿es múltiplo de <b>' + n + '</b>?', cajas: ['Múltiplos de ' + n, 'No múltiplos'], items: L1.map(function (x) { return { v: x, t: x, c: x % n === 0 ? 0 : 1 }; }) }; }
      if (modo === 'divisores') { var N = pick([24, 30, 36, 40, 42, 48, 60, 72, 84, 90]), d = divisores(N), L2 = juntar(12, function () { return pick(d); }, function () { return R(2, N); });
        return { tit: 'Ubicá cada número: ¿es divisor de <b>' + N + '</b>?', cajas: ['Divisores de ' + N, 'No son divisores'], items: L2.map(function (x) { return { v: x, t: x, c: N % x === 0 ? 0 : 1 }; }) }; }
      if (modo === 'primos') { var pr = [], co = []; for (var i = 2; i < 100; i++) (esPrimo(i) ? pr : co).push(i); var L3 = juntar(12, function () { return pick(co); }, function () { return pick(pr); });
        return { tit: 'Separá los números <b>primos</b> de los <b>compuestos</b>.', cajas: ['Primos', 'Compuestos'], items: L3.map(function (x) { return { v: x, t: x, c: esPrimo(x) ? 0 : 1 }; }) }; }
      if (modo === 'divisible') { var M2 = R(1000, 99999), cs = [2, 3, 4, 5, 6, 8, 9, 10, 11];
        return { tit: 'El número <b>' + fmt(M2) + '</b>: ¿por cuáles es divisible?', cajas: ['Es divisible por', 'No es divisible por'], items: cs.map(function (x) { return { v: x, t: x, c: M2 % x === 0 ? 0 : 1 }; }) }; }
      // fraccion1: menor que 1, igual a 1, mayor que 1
      var s4 = {}, it = [], tope = 0; while (it.length < 12 && tope++ < 3000) { var b = R(2, 10), t = it.length % 3, a = t === 0 ? R(1, b - 1) : t === 1 ? b : R(b + 1, 2 * b + 3), k = a + '/' + b; if (!s4[k]) { s4[k] = 1; it.push({ v: k, t: fr(a, b), c: t }); } }
      return { tit: 'Ubicá cada fracción según su valor.', cajas: ['vale < 1', 'vale = 1', 'vale > 1'], items: it };
    }
    ejercicio(el, api, '', function (c) {
      var D = datos(); el.querySelector('.lb-cons').innerHTML = D.tit;
      c.innerHTML = '<div class="lb-cajas n' + D.cajas.length + '">' + D.cajas.map(function (t, k) { return '<div class="lb-caja" data-dest="' + k + '"><b>' + t + '</b><div class="lb-dest-c"></div></div>'; }).join('') + '</div>' +
        '<div class="lb-banco">' + mezclar(D.items).map(function (x) { return chip(x.v, x.t, ' data-c="' + x.c + '"'); }).join('') + '</div><p class="lb-ayuda">Tocá un número y después la caja donde va.</p>';
      tocarYUbicar(c);
      return {
        comprobar: function () {
          var mal = 0, faltan = c.querySelector('.lb-banco').querySelectorAll('.lb-chip').length;
          [].forEach.call(c.querySelectorAll('.lb-caja .lb-chip'), function (ch) { var ok = ch.getAttribute('data-c') === ch.closest('[data-dest]').getAttribute('data-dest'); ch.classList.toggle('bien', ok); ch.classList.toggle('mal', !ok); if (!ok) mal++; });
          if (faltan) return { ok: false, msg: 'Te faltan ubicar ' + faltan + '.' };
          return mal ? { ok: false, msg: 'Hay ' + mal + ' mal ubicado' + (mal > 1 ? 's' : '') + ' (los marcados). Tocalos para devolverlos y probá de nuevo.' } : { ok: true, msg: '¡Todos bien ubicados!' };
        },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-chip'), function (ch) { c.querySelector('[data-dest="' + ch.getAttribute('data-c') + '"] .lb-dest-c').appendChild(ch); }); }
      };
    });
  } };

  // 8. Llevar cada ficha a su lugar (parejas)
  M.llevar = { tipo: 'ejercicio', nombre: 'Llevar cada ficha a su lugar', render: function (el, p, api) {
    var modo = p.modo || 'equivalentes';
    function datos() {
      var pares = [], vistos = {}, it = 0;
      function add(izq, res, txt) { if (vistos[res]) return; vistos[res] = 1; pares.push({ izq: izq, res: res, txt: txt != null ? txt : res }); }
      var tope3 = 0; while (pares.length < 6 && tope3++ < 3000) {
        if (modo === 'equivalentes') { var a = R(1, 9), b = R(2, 9), k = R(2, 7); if (mcd(a, b) === 1 && a !== b) add(fr(a, b), (a * k) + '/' + (b * k), fr(a * k, b * k)); }
        else if (modo === 'irreducibles') { var a2 = R(1, 9), b2 = R(2, 9), k2 = R(2, 7); if (mcd(a2, b2) === 1 && a2 !== b2) add(fr(a2 * k2, b2 * k2), a2 + '/' + b2, fr(a2, b2)); }
        else if (modo === 'potencias') { var bs = R(2, 7) * pick([1, -1]), ex = R(2, bs > 4 || bs < -4 ? 3 : 4), neg = Math.random() < .3, val = neg ? -Math.pow(Math.abs(bs), ex) : Math.pow(bs, ex);
          add(neg ? '−' + Math.abs(bs) + '<sup>' + ex + '</sup>' : (bs < 0 ? '(' + sig(bs) + ')' : bs) + '<sup>' + ex + '</sup>', String(val), fmt(val)); }
        else if (modo === 'raices') { var r = R(1, 19), ng = Math.random() < .25; add('√' + (ng ? '−' + r * r : r * r), ng ? 'no' : String(r), ng ? 'No existe' : '±' + r); if (ng) vistos.no = 0; }
        else { var x = R(-12, 12), y = R(-12, 12), op = pick(['+', '−']), v = op === '+' ? x + y : x - y; add('(' + sig(x) + ') ' + op + ' (' + sig(y) + ')', String(v), sig(v)); }
      }
      var tit = { equivalentes: 'Llevá cada fracción de abajo al lado de su <b>fracción equivalente</b>.', irreducibles: 'Llevá cada fracción <b>irreducible</b> al lado de la fracción que simplifica.',
        potencias: 'Llevá cada número al lado de la <b>potencia de igual valor</b>.', raices: 'Colocá el resultado de cada <b>raíz cuadrada</b>.', sumas: 'Llevá cada resultado al lado de su <b>cuenta</b>.' }[modo] || '';
      return { tit: tit, pares: pares };
    }
    ejercicio(el, api, '', function (c) {
      var D = datos(); el.querySelector('.lb-cons').innerHTML = D.tit;
      c.innerHTML = '<div class="lb-pares">' + D.pares.map(function (x, k) { return '<div class="lb-par"><span class="lb-izq">' + x.izq + '</span><span class="lb-ig">=</span><span class="lb-hueco" data-dest="' + k + '" data-max="1"></span></div>'; }).join('') + '</div>' +
        '<div class="lb-banco">' + mezclar(D.pares.map(function (x, k) { return chip(x.res, x.txt, ' data-c="' + k + '"'); })).join('') + '</div><p class="lb-ayuda">Tocá una ficha y después el lugar.</p>';
      tocarYUbicar(c);
      return {
        comprobar: function () {
          var mal = 0, falt = 0;
          D.pares.forEach(function (x, k) { var h = c.querySelector('[data-dest="' + k + '"]'), ch = h.querySelector('.lb-chip'); if (!ch) { falt++; return; } var ok = ch.getAttribute('data-v') === x.res; ch.classList.toggle('bien', ok); ch.classList.toggle('mal', !ok); if (!ok) mal++; });
          if (falt) return { ok: false, msg: 'Te faltan completar ' + falt + '.' };
          return mal ? { ok: false, msg: 'Hay ' + mal + ' que no va' + (mal > 1 ? 'n' : '') + ' ahí (marcadas). Tocalas para devolverlas.' } : { ok: true, msg: '¡Todas bien!' };
        },
        resolver: function () { D.pares.forEach(function (x, k) { var ch = c.querySelector('.lb-banco [data-v="' + CSS.escape(x.res) + '"]') || c.querySelector('[data-c="' + k + '"]'); c.querySelector('[data-dest="' + k + '"]').appendChild(ch); }); }
      };
    });
  } };

  // 9. Ordenar de menor a mayor en casilleros con <
  M.ordenar = { tipo: 'ejercicio', nombre: 'Ordenar de menor a mayor', render: function (el, p, api) {
    var modo = p.modo || 'enteros';
    ejercicio(el, api, 'Colocá los números de forma que queden ordenados <b>de menor a mayor</b>.', function (c) {
      var vals = {}, L = [];
      var tope2 = 0; while (L.length < 4 && tope2++ < 3000) { var v = modo === 'decimales' ? Math.round(R(-20, 80) * 10 + R(0, 9) * (Math.random() < .5 ? 1 : 0)) / (Math.random() < .5 ? 10 : 100) : modo === 'fracciones' ? null : R(-99, 99), t;
        if (modo === 'fracciones') { var b = R(2, 9), a = R(1, 2 * b); v = a / b; t = fr(a, b); } else t = modo === 'enteros' ? sig(v) : fmt(v);
        var key = v.toFixed(6); if (!vals[key]) { vals[key] = 1; L.push({ v: v, t: t }); } }
      c.innerHTML = '<div class="lb-orden">' + L.map(function (_, k) { return (k ? '<span class="lb-menor">&lt;</span>' : '') + '<span class="lb-hueco" data-dest="' + k + '" data-max="1"></span>'; }).join('') + '</div>' +
        '<div class="lb-banco">' + mezclar(L.map(function (x) { return chip(x.v, x.t); })).join('') + '</div>';
      tocarYUbicar(c);
      return {
        comprobar: function () {
          var hs = c.querySelectorAll('.lb-hueco'), vs = [].map.call(hs, function (h) { var ch = h.querySelector('.lb-chip'); return ch ? +ch.getAttribute('data-v') : null; });
          if (vs.some(function (x) { return x === null; })) return { ok: false, msg: 'Completá todos los casilleros.' };
          var ok = vs.every(function (x, k) { return !k || vs[k - 1] < x; });
          return ok ? { ok: true, msg: '¡Bien ordenados!' } : { ok: false, msg: 'Todavía no están de menor a mayor. Fijate el signo de cada uno.' };
        },
        resolver: function () { var chs = [].slice.call(c.querySelectorAll('.lb-chip')).sort(function (x, y) { return +x.getAttribute('data-v') - +y.getAttribute('data-v'); }); chs.forEach(function (ch, k) { c.querySelector('[data-dest="' + k + '"]').appendChild(ch); }); }
      };
    });
  } };

  // 10. Recta numérica: ¿cuánto valen A y B?
  M.recta = { tipo: 'ejercicio', nombre: 'Recta numérica', render: function (el, p, api) {
    ejercicio(el, api, '¿Cuál es el valor de <b>A</b> y de <b>B</b>?', function (c) {
      var paso = pick([1, 1, 2, 5]), n = 12, ini = paso * R(-10, -1), ka = R(0, n), kb = R(0, n); while (kb === ka) kb = R(0, n);
      var A = ini + ka * paso, B = ini + kb * paso, W = 560, Mx = 20, sx = (W - 2 * Mx) / n;
      var svg = '<svg viewBox="0 0 ' + W + ' 90" class="lb-recta"><line x1="8" y1="45" x2="' + (W - 8) + '" y2="45"/>';
      for (var k = 0; k <= n; k++) { var x = Mx + k * sx, v = ini + k * paso; svg += '<line x1="' + x + '" y1="38" x2="' + x + '" y2="52"/>' + (v === 0 ? '<text x="' + x + '" y="30">0</text>' : ''); }
      if (!(ini <= 0 && ini + n * paso >= 0)) svg += '<text x="' + (Mx) + '" y="30">' + ini + '</text>';
      [['A', ka], ['B', kb]].forEach(function (q) { var x = Mx + q[1] * sx; svg += '<circle cx="' + x + '" cy="45" r="6" class="pt"/><text x="' + x + '" y="76" class="pt">' + q[0] + '</text>'; });
      c.innerHTML = svg + '</svg><p class="lb-ayuda">Cada rayita vale ' + paso + '.</p><div class="lb-in-f dos"><label>A =</label><input type="text" inputmode="numeric" class="lb-inp" data-r="A"><label>B =</label><input type="text" inputmode="numeric" class="lb-inp" data-r="B"></div>';
      return {
        comprobar: function () {
          var a = num(c.querySelector('[data-r="A"]').value), b = num(c.querySelector('[data-r="B"]').value);
          if (!isFinite(a) || !isFinite(b)) return { ok: false, msg: 'Escribí los dos valores.' };
          return a === A && b === B ? { ok: true, msg: '¡Exacto! A = ' + sig(A) + ' y B = ' + sig(B) + '.' } : { ok: false, msg: 'Revisalo: contá las rayitas desde el 0. ' + (a !== A ? 'A no es ' + a + '. ' : '') + (b !== B ? 'B no es ' + b + '.' : '') };
        },
        resolver: function () { c.querySelector('[data-r="A"]').value = A; c.querySelector('[data-r="B"]').value = B; }
      };
    });
  } };

  // 11. Tabla de valor posicional
  var POS = ['unidades', 'decenas', 'centenas', 'unidades de mil', 'decenas de mil', 'centenas de mil', 'unidades de millón'];
  var DEC = ['décimos', 'centésimos', 'milésimos'];
  M.posicional = { tipo: 'ejercicio', nombre: 'Valor posicional', render: function (el, p, api) {
    var modo = p.modo || 'ubicar';
    if (modo === 'decimal') return ejercicio(el, api, '', function (c) {
      var ent = R(0, 99), nd = R(1, 3), dec = R(1, Math.pow(10, nd) - 1), val = ent + dec / Math.pow(10, nd), haciaNum = Math.random() < .5;
      var nom = ['', 'décimos', 'centésimos', 'milésimos'][nd], leer = (ent ? ent + ' unidad' + (ent === 1 ? '' : 'es') + ' y ' : '') + dec + ' ' + (dec === 1 ? nom.replace(/s$/, '') : nom), cifra = fmt(Number(val.toFixed(nd)));
      el.querySelector('.lb-cons').innerHTML = haciaNum ? 'Escribí con cifras: <b>' + leer + '</b>' : '¿Cómo se lee <b>' + cifra + '</b>? Completá.';
      c.innerHTML = haciaNum ? '<div class="lb-in-f"><input type="text" inputmode="decimal" class="lb-inp" placeholder="Por ejemplo 32,67"></div><p class="lb-ayuda">Usá la coma para los decimales.</p>'
        : '<div class="lb-in-f dos"><input type="text" inputmode="numeric" class="lb-inp" data-k="e" aria-label="Unidades" value="' + (ent ? '' : '0') + '"><label>unidades y</label><input type="text" inputmode="numeric" class="lb-inp" data-k="d" aria-label="Parte decimal"><label>' + nom + '</label></div>';
      return {
        comprobar: function () {
          if (haciaNum) { var x = num(c.querySelector('input').value); return Math.abs(x - val) < 1e-9 ? { ok: true, msg: '¡Bien! ' + leer + ' = ' + cifra } : { ok: false, msg: 'No es ' + (isFinite(x) ? fmt(x) : 'eso') + '. Fijate cuántas cifras van después de la coma: ' + nom + ' = ' + nd + ' cifra' + (nd > 1 ? 's' : '') + '.' }; }
          var e = num(c.querySelector('[data-k="e"]').value), d = num(c.querySelector('[data-k="d"]').value);
          return e === ent && d === dec ? { ok: true, msg: '¡Bien! Se lee ' + leer + '.' } : { ok: false, msg: 'Revisalo: se lee ' + leer + '.' };
        },
        resolver: function () { if (haciaNum) c.querySelector('input').value = cifra; else { c.querySelector('[data-k="e"]').value = ent; c.querySelector('[data-k="d"]').value = dec; } }
      };
    });
    ejercicio(el, api, '', function (c) {
      var n = String(R(10000, 9999999)), pos = R(0, n.length - 1), idx = n.length - 1 - pos;
      el.querySelector('.lb-cons').innerHTML = 'Tocá la cifra de las <b>' + POS[pos] + '</b>.';
      c.innerHTML = '<div class="lb-cifras">' + n.split('').map(function (d, k) { return (k && (n.length - k) % 3 === 0 ? '<span class="lb-pto">.</span>' : '') + '<button type="button" class="lb-cifra" data-k="' + k + '">' + d + '</button>'; }).join('') + '</div>';
      var elegido = null;
      c.addEventListener('click', function (e) { var b = e.target.closest('.lb-cifra'); if (!b) return; [].forEach.call(c.querySelectorAll('.lb-cifra'), function (x) { x.classList.toggle('on', x === b); }); elegido = +b.getAttribute('data-k'); });
      return {
        comprobar: function () {
          if (elegido == null) return { ok: false, msg: 'Tocá una cifra.' };
          return elegido === idx ? { ok: true, msg: '¡Sí! El ' + n[idx] + ' está en las ' + POS[pos] + ': vale ' + fmt(+n[idx] * Math.pow(10, pos)) + '.' } : { ok: false, msg: 'Esa cifra está en las ' + POS[n.length - 1 - elegido] + '. Contá los lugares desde la derecha: unidades, decenas, centenas…' };
        },
        resolver: function () { c.querySelector('[data-k="' + idx + '"]').click(); }
      };
    });
  } };

  // 12. Cuenta en columnas (suma o resta de decimales)
  M.columnas = { tipo: 'ejercicio', nombre: 'Cuenta en columnas', render: function (el, p, api) {
    ejercicio(el, api, '', function (c) {
      var resta = p.op === 'resta' || (p.op === 'mixta' && Math.random() < .5);
      el.querySelector('.lb-cons').innerHTML = (resta ? 'Restá' : 'Sumá') + ' encolumnando: <b>coma debajo de coma</b>. Escribí una cifra en cada casillero del resultado.';
      var d1 = R(1, 3), d2 = R(1, 3), a = R(100, 9999) / Math.pow(10, d1), b = R(100, 9999) / Math.pow(10, d2);
      if (resta && b > a) { var t = a; a = b; b = t; var td = d1; d1 = d2; d2 = td; }
      var nd = Math.max(d1, d2), res = Math.round((resta ? a - b : a + b) * Math.pow(10, nd)) / Math.pow(10, nd);
      function partes(x) { var s = x.toFixed(nd).split('.'); return { e: s[0], d: s[1] }; }
      var A = partes(a), B = partes(b), Rr = partes(res), ne = Math.max(A.e.length, B.e.length, Rr.e.length);
      function fila(P, signo, inputs) {
        var e = P.e.padStart(ne, ' '), cells = '';
        for (var i = 0; i < ne; i++) cells += inputs ? '<input class="lb-cel" maxlength="1" inputmode="numeric" data-i="e' + i + '">' : '<span class="lb-cel">' + (e[i] === ' ' ? '' : e[i]) + '</span>';
        cells += '<span class="lb-coma">,</span>';
        for (var j = 0; j < nd; j++) cells += inputs ? '<input class="lb-cel" maxlength="1" inputmode="numeric" data-i="d' + j + '">' : '<span class="lb-cel">' + P.d[j] + '</span>';
        return '<div class="lb-fila' + (inputs ? ' res' : '') + '"><span class="lb-sig">' + signo + '</span>' + cells + '</div>';
      }
      c.innerHTML = '<div class="lb-cuenta">' + fila(A, '') + fila(B, resta ? '−' : '+') + fila(Rr, '', true) + '</div><p class="lb-ayuda">Si falta alguna cifra decimal, pensala como un 0.</p>';
      var esp = Rr.e.padStart(ne, ' ') + Rr.d;
      return {
        comprobar: function () {
          var ins = c.querySelectorAll('input'), escrito = [].map.call(ins, function (i) { return i.value.trim() || ' '; }).join(''), ok = escrito.replace(/^ +/, '') === esp.replace(/^ +/, '') && escrito.length === esp.length;
          return ok ? { ok: true, msg: '¡Bien! ' + fmt(a) + (resta ? ' − ' : ' + ') + fmt(b) + ' = ' + fmt(res) } : { ok: false, msg: 'Revisá columna por columna, de derecha a izquierda, y acordate de lo que te llevás.' };
        },
        resolver: function () { var ins = c.querySelectorAll('input'); esp.split('').forEach(function (ch, k) { ins[k].value = ch === ' ' ? '' : ch; }); }
      };
    });
  } };

  // 13. Números en letras y en audio: pagaré, dictado y fracción en letras
  M.letras = { tipo: 'ejercicio', nombre: 'Números en letras', render: function (el, p, api) {
    var modo = p.modo || 'pagare';
    if (modo === 'dictado') return ejercicio(el, api, 'Escuchá el número y escribilo <b>con cifras</b>.', function (c) {
      var n = pick([R(1000, 99999), R(100000, 9999999)]);
      function decir() { try { var u = new SpeechSynthesisUtterance(letras(n)); u.lang = 'es-AR'; u.rate = .85; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (_) {} }
      c.innerHTML = '<button type="button" class="lb-btn suave lb-oir">🔊 Escuchar</button><div class="lb-in-f"><input type="text" inputmode="numeric" class="lb-inp" placeholder="Escribí el número"></div>';
      c.querySelector('.lb-oir').onclick = decir; setTimeout(decir, 300);
      return {
        comprobar: function () { var x = num(c.querySelector('input').value); return x === n ? { ok: true, msg: '¡Bien! Era ' + fmt(n) + '.' } : { ok: false, msg: 'No era ' + (isFinite(x) ? fmt(x) : 'eso') + '. Era ' + fmt(n) + ': «' + letras(n) + '».' }; },
        resolver: function () { c.querySelector('input').value = n; }
      };
    });
    if (modo === 'fraccion') return ejercicio(el, api, '', function (c) {
      var d = R(2, 20), a = R(1, 3 * d); while (a === d) a = R(1, 3 * d);
      el.querySelector('.lb-cons').innerHTML = 'Escribí con números la fracción: <b>' + fraccionEnLetras(a, d) + '</b>';
      c.innerHTML = '<div class="lb-fr-in"><input type="text" inputmode="numeric" class="lb-inp chico" data-k="n" aria-label="Numerador"><i></i><input type="text" inputmode="numeric" class="lb-inp chico" data-k="d" aria-label="Denominador"></div>';
      return {
        comprobar: function () { var x = num(c.querySelector('[data-k="n"]').value), y = num(c.querySelector('[data-k="d"]').value); return x === a && y === d ? { ok: true, msg: '¡Bien! ' + fraccionEnLetras(a, d) + ' = ' + a + '/' + d } : { ok: false, msg: 'Se escribe ' + a + '/' + d + ': el número de partes arriba (numerador) y en cuántas partes se divide abajo (denominador).' }; },
        resolver: function () { c.querySelector('[data-k="n"]').value = a; c.querySelector('[data-k="d"]').value = d; }
      };
    });
    ejercicio(el, api, 'Completá el pagaré: escribí el monto <b>con letras</b>.', function (c) {
      var n = pick([R(1000, 99999), R(100000, 999999), R(1000000, 9999999)]), ok1 = norm(letras(n)), ok2 = norm(letras(n).replace(/veintiuno mil/, 'veintiún mil'));
      c.innerHTML = '<div class="lb-pagare"><div class="lb-pg-h"><b>PAGARÉ</b><span>$ ' + fmt(n) + '</span></div><p>Por este pagaré me comprometo a pagar la suma de:</p><textarea class="lb-inp lb-pg-in" rows="2" placeholder="Escribí el monto con letras"></textarea><p class="lb-pg-f">pesos.</p></div><p class="lb-ayuda">No hace falta usar mayúsculas ni tildes.</p>';
      return {
        comprobar: function () { var t = norm(c.querySelector('textarea').value).replace(/ pesos$/, ''); return t === ok1 || t === ok2 ? { ok: true, msg: '¡Perfecto! ' + fmt(n) + ': ' + letras(n) + '.' } : { ok: false, msg: 'Así se escribe: «' + letras(n) + '». Leelo por grupos: millones, miles y lo que queda.' }; },
        resolver: function () { c.querySelector('textarea').value = letras(n); }
      };
    });
  } };

  // 14. m.c.d. guiado paso a paso
  M.mcd_guiado = { tipo: 'ejercicio', nombre: 'm.c.d. guiado', render: function (el, p, api) {
    ejercicio(el, api, 'Calculá el <b>máximo común divisor</b> paso a paso. Separá los números con comas.', function (c) {
      var a = pick([12, 18, 20, 24, 28, 30, 36, 40, 42, 45]), b = pick([16, 21, 27, 32, 35, 48, 54, 60, 63]); while (b === a) b = pick([16, 21, 27, 32, 48, 54, 60]);
      var da = divisores(a), db = divisores(b), co = da.filter(function (x) { return db.indexOf(x) >= 0; }), m = mcd(a, b);
      c.innerHTML = '<div class="lb-guia"><label>1. Divisores de ' + a + '</label><input type="text" class="lb-inp" data-k="a"><label>2. Divisores de ' + b + '</label><input type="text" class="lb-inp" data-k="b">' +
        '<label>3. Divisores comunes</label><input type="text" class="lb-inp" data-k="c"><label>4. m.c.d.(' + a + ', ' + b + ')</label><input type="text" inputmode="numeric" class="lb-inp chico" data-k="m"></div>';
      function lista(s) { return String(s).split(/[^0-9]+/).filter(Boolean).map(Number).sort(function (x, y) { return x - y; }).join(','); }
      return {
        comprobar: function () {
          var v = function (k) { return c.querySelector('[data-k="' + k + '"]').value; }, msgs = [];
          if (lista(v('a')) !== da.join(',')) msgs.push('Los divisores de ' + a + ' no están completos o hay alguno que no va.');
          else if (lista(v('b')) !== db.join(',')) msgs.push('Revisá los divisores de ' + b + '.');
          else if (lista(v('c')) !== co.join(',')) msgs.push('Los comunes son los que aparecen en las dos listas.');
          else if (num(v('m')) !== m) msgs.push('El m.c.d. es el mayor de los divisores comunes.');
          return msgs.length ? { ok: false, msg: msgs[0] } : { ok: true, msg: '¡Bien! m.c.d.(' + a + ', ' + b + ') = ' + m + '.' };
        },
        resolver: function () { var s = function (k, x) { c.querySelector('[data-k="' + k + '"]').value = x; }; s('a', da.join(', ')); s('b', db.join(', ')); s('c', co.join(', ')); s('m', m); }
      };
    });
  } };

  // 15. Tabla de proporcionalidad (inventada)
  M.proporcional = { tipo: 'ejercicio', nombre: 'Tabla de proporcionalidad', render: function (el, p, api) {
    ejercicio(el, api, 'Las dos magnitudes son <b>directamente proporcionales</b>. Completá los casilleros vacíos.', function (c) {
      var ctx = pick([['Kilos de pan', 'Precio ($)', [800, 1200, 1500, 2000]], ['Litros de nafta', 'Kilómetros', [12, 14, 15, 16]], ['Horas', 'Páginas leídas', [15, 20, 25, 30]], ['Entradas', 'Precio ($)', [2500, 3000, 4000]]]);
      var k = pick(ctx[2]), xs = mezclar([1, 2, 3, 4, 5, 6, 8, 10]).slice(0, 5).sort(function (x, y) { return x - y; }), hueco = mezclar([0, 1, 2, 3, 4]).slice(0, 2);
      c.innerHTML = '<div class="lb-prop-w"><table class="lb-prop"><tr><th>' + ctx[0] + '</th>' + xs.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr><th>' + ctx[1] + '</th>' +
        xs.map(function (x, i) { return '<td>' + (hueco.indexOf(i) >= 0 ? '<input class="lb-inp chico" inputmode="numeric" data-i="' + i + '">' : fmt(x * k)) + '</td>'; }).join('') + '</tr></table></div>';
      return {
        comprobar: function () {
          var ok = hueco.every(function (i) { return num(c.querySelector('[data-i="' + i + '"]').value) === xs[i] * k; });
          return ok ? { ok: true, msg: '¡Bien! La constante es ' + fmt(k) + ': cada valor de abajo es el de arriba × ' + fmt(k) + '.' } : { ok: false, msg: 'Buscá cuánto vale para 1 (dividí un valor de abajo por el de arriba) y multiplicá.' };
        },
        resolver: function () { hueco.forEach(function (i) { c.querySelector('[data-i="' + i + '"]').value = xs[i] * k; }); }
      };
    });
  } };

  // ---------- estilos (prefijo lb-, solo lección) ----------
  var css = document.createElement('style');
  css.textContent = [
    '.lb-cons{font-weight:800;margin:0 0 12px;line-height:1.45}.lb-ayuda{font-size:.86rem;color:#4b6a6c;margin:8px 0 0}.lb-nota{margin:10px 0 0;line-height:1.5}.lb-res{font-weight:800;font-size:1.15rem;color:#066A6E;margin:10px 0 0}',
    '.lb-in-f{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:10px}.lb-in-f label{font-weight:700;color:#4b6a6c}.lb-inp{padding:9px 12px;border:2px solid #E3ECEA;border-radius:12px;font:inherit;font-weight:800;font-size:1.05rem;min-width:0;width:110px;color:#253638;background:#fff}',
    '.lb-inp:focus{outline:none;border-color:#087E83;box-shadow:0 0 0 3px #D7F0E9}.lb-inp.chico{width:64px;text-align:center}textarea.lb-inp{width:100%;box-sizing:border-box;font-weight:700}',
    '.lb-vista h5{margin:10px 0 6px;font-size:.92rem;color:#066A6E}.lb-grilla{display:flex;flex-wrap:wrap;gap:4px}.lb-grilla span{min-width:34px;padding:4px 6px;border-radius:8px;background:#F3FBF7;text-align:center;font-weight:700;font-size:.9rem}',
    '.lb-grilla span.on{background:#D7F0E9}.lb-grilla span.com{background:#087E83;color:#fff}.lb-grilla span.max{box-shadow:0 0 0 3px #253638}',
    '.lb-esc{display:flex;justify-content:center;font-weight:800;font-size:1.2rem}.lb-esc-l,.lb-esc-r{display:flex;flex-direction:column;gap:4px;padding:4px 12px}.lb-esc-l{text-align:right;border-right:3px solid #253638}.lb-esc-r{color:#087E83}.lb-esc-r .lb-inp{width:64px;padding:2px 6px}',
    '.lb-esca{display:flex;flex-direction:column;gap:3px;margin-bottom:10px}.lb-esc-u{width:62px;padding:5px 0;border:2px solid #9dbdb9;border-radius:8px;background:#fff;font:inherit;font-weight:800;cursor:pointer;color:#253638}.lb-esc-u.de{background:#087E83;color:#fff;border-color:#087E83}.lb-esc-u.a{background:#253638;color:#fff;border-color:#253638}',
    '.lb-bal{display:flex;align-items:flex-end;justify-content:center;gap:10px;margin:6px 0 12px}.lb-plato{min-width:110px;padding:14px 10px;border-bottom:6px solid #253638;border-radius:0 0 40px 40px;background:#D7F0E9;text-align:center;font-weight:800;font-size:1.2rem}.lb-fiel{font-weight:900;font-size:1.5rem;color:#087E83;padding-bottom:14px}',
    '.lb-marco{width:100%;height:420px;border:0;border-radius:14px;background:#fff}',
    '.lb-btn{padding:10px 16px;border:0;border-radius:14px;background:#087E83;color:#fff;font:inherit;font-weight:800;cursor:pointer}.lb-btn.suave{background:#fff;color:#066A6E;border:2px solid #087E83}.lb-pie{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px}',
    '.lb-fb{margin-top:10px}.lb-ok,.lb-no{padding:10px 12px;border-radius:12px;font-weight:700}.lb-ok{background:#D7F0E9}.lb-no{background:#E3ECEA}',
    '.lb-chip{min-width:46px;min-height:46px;padding:6px 10px;border:2px solid #9dbdb9;border-radius:99px;background:#fff;font:inherit;font-weight:800;font-size:1.05rem;color:#253638;cursor:pointer;display:inline-flex;align-items:center;justify-content:center}',
    '.lb-chip.on{border-color:#087E83;background:#D7F0E9;box-shadow:0 0 0 3px #087E83}.lb-chip.bien{border-color:#087E83;background:#087E83;color:#fff}.lb-chip.mal{border:2px dashed #253638;background:#E3ECEA}.lb-chip.mal::after{content:" ✘";font-size:.8rem}',
    '.lb-banco{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px;padding:12px;border-radius:16px;background:#087E83}.lb-banco .lb-chip{border-color:#fff}',
    '.lb-cajas{display:grid;gap:10px}.lb-cajas.n2{grid-template-columns:1fr 1fr}.lb-cajas.n3{grid-template-columns:1fr 1fr 1fr}.lb-caja{min-height:130px;padding:8px;border:3px solid #087E83;border-radius:16px;background:#F3FBF7;cursor:pointer}.lb-caja:nth-child(2){border-color:#253638;background:#E3ECEA}.lb-caja:nth-child(3){border-color:#9dbdb9}',
    '.lb-caja>b{display:block;text-align:center;margin-bottom:6px}.lb-dest-c{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}',
    '.lb-fr{display:inline-flex;flex-direction:column;align-items:center;line-height:1.05;font-weight:800}.lb-fr i{font-style:normal}.lb-fr i:first-child{border-bottom:2px solid currentColor;padding:0 2px}',
    '.lb-pares{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px}.lb-par{display:flex;align-items:center;justify-content:center;gap:8px;padding:8px;border-radius:14px;background:#F3FBF7;font-weight:800;font-size:1.1rem}',
    '.lb-hueco{display:inline-flex;align-items:center;justify-content:center;min-width:54px;min-height:54px;border:2px dashed #9dbdb9;border-radius:50%;background:#fff;cursor:pointer}.lb-hueco .lb-chip{border-radius:99px}',
    '.lb-orden{display:flex;align-items:center;justify-content:center;gap:6px;flex-wrap:wrap}.lb-menor{font-weight:900;font-size:1.4rem;color:#087E83}',
    '.lb-recta{width:100%;max-width:580px}.lb-recta line{stroke:#253638;stroke-width:2}.lb-recta text{font-weight:800;font-size:14px;text-anchor:middle;fill:#253638}.lb-recta circle.pt{fill:#087E83}.lb-recta text.pt{fill:#087E83;font-size:16px}',
    '.lb-cifras{display:flex;justify-content:center;align-items:flex-end;gap:4px;margin:8px 0}.lb-cifra{width:46px;height:58px;border:2px solid #E3ECEA;border-radius:12px;background:#fff;font:inherit;font-weight:900;font-size:1.8rem;color:#253638;cursor:pointer}.lb-cifra.on{background:#087E83;color:#fff;border-color:#087E83}.lb-pto{font-weight:900;font-size:1.6rem}',
    '.lb-cuenta{display:inline-flex;flex-direction:column;gap:4px;padding:10px;border-radius:14px;background:#F3FBF7}.lb-fila{display:flex;align-items:center;gap:3px}.lb-fila.res{border-top:3px solid #253638;padding-top:6px}',
    '.lb-cel{width:34px;height:38px;display:inline-flex;align-items:center;justify-content:center;font-weight:800;font-size:1.2rem;border:2px solid transparent;border-radius:8px;text-align:center;font-family:inherit;color:#253638}input.lb-cel{border-color:#9dbdb9;background:#fff;padding:0}input.lb-cel:focus{outline:none;border-color:#087E83}',
    '.lb-coma{font-weight:900;font-size:1.3rem;width:8px;text-align:center}.lb-sig{width:18px;font-weight:900;font-size:1.2rem}',
    '.lb-pagare{padding:14px 16px;border:2px solid #9dbdb9;border-radius:14px;background:repeating-linear-gradient(0deg,#fff,#fff 26px,#F3FBF7 27px)}.lb-pg-h{display:flex;justify-content:space-between;align-items:center;font-size:1.1rem;color:#066A6E}.lb-pg-h span{font-weight:900;color:#253638;padding:4px 10px;border:2px solid #253638;border-radius:8px}.lb-pagare p{margin:8px 0}.lb-pg-f{text-align:right;font-weight:700}',
    '.lb-oir{margin-bottom:10px}.lb-fr-in{display:inline-flex;flex-direction:column;align-items:center;gap:4px}.lb-fr-in i{width:80px;height:3px;background:#253638}',
    '.lb-guia{display:grid;grid-template-columns:auto 1fr;gap:8px 10px;align-items:center}.lb-guia label{font-weight:700;color:#253638}.lb-guia .lb-inp{width:100%;box-sizing:border-box}.lb-guia .lb-inp.chico{width:80px}',
    '.lb-prop-w{overflow-x:auto}.lb-prop{border-collapse:collapse;background:#fff}.lb-prop th{background:#087E83;color:#fff;text-align:left;padding:8px 10px;font-size:.9rem}.lb-prop td{border:2px solid #E3ECEA;padding:6px 8px;text-align:center;font-weight:800;min-width:56px}',
    '@media (max-width:560px){.lb-cajas.n3{grid-template-columns:1fr}.lb-guia{grid-template-columns:1fr}.lb-cifra{width:38px;height:50px;font-size:1.5rem}}'
  ].join('');
  document.head.appendChild(css);

  var api0 = { sonar: function (n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }, confeti: function (e) { try { if (window.WaveJuego) WaveJuego.confeti(e); } catch (_) {} } };
  return {
    motores: M,
    tiene: function (id) { return !!M[id]; },
    render: function (el, cfg, api) { var m = M[cfg && cfg.motor]; if (!m) return false; m.render(el, cfg.p || {}, Object.assign({}, api0, api || {})); return true; },
    util: { letras: letras, fraccionEnLetras: fraccionEnLetras, divisores: divisores, esPrimo: esPrimo },
    // herramientas internas para los motores de js/leccion-banco2.js (mismo banco, solo lección)
    _h: { R: R, pick: pick, mezclar: mezclar, esc: esc, divisores: divisores, esPrimo: esPrimo, mcd: mcd, mcm: mcm, fmt: fmt, sig: sig, num: num, norm: norm, chip: chip, fr: fr, ejercicio: ejercicio, tocarYUbicar: tocarYUbicar }
  };
})();
