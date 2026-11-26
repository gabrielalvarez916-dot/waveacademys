/* BANCO DE LA LECCIÓN INTERACTIVA · parte 2 (Matemática): geometría, álgebra, números, funciones, estadística y probabilidad.
   Mismo banco que js/leccion-banco.js (SOLO lección, separado del de actividades). Ejemplos = escena para explorar cambiando los números;
   ejercicios = botón del tema, con "Comprobar" y "Otros números". */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h) return;
  var H = B._h, M = B.motores, R = H.R, pick = H.pick, mezclar = H.mezclar, esc = H.esc, fmt = H.fmt, sig = H.sig, num = H.num, mcd = H.mcd, fr = H.fr, chip = H.chip;
  var PI = 3.14;
  function r2(x) { return Math.round(x * 100) / 100; }
  function frs(a, b) { if (b < 0) { a = -a; b = -b; } var g = mcd(Math.abs(a), Math.abs(b)) || 1; a /= g; b /= g; return b === 1 ? String(a) : a + '/' + b; }
  function frHtml(a, b) { if (b < 0) { a = -a; b = -b; } var g = mcd(Math.abs(a), Math.abs(b)) || 1; a /= g; b /= g; return b === 1 ? String(a) : fr(a, b); }
  function ctrl(k, lab, min, max, step, val, suf) { return '<label class="lb2-ctl"><span>' + lab + ': <b data-o="' + k + '">' + fmt(val) + '</b>' + (suf || '') + '</span><input type="range" data-k="' + k + '" min="' + min + '" max="' + max + '" step="' + step + '" value="' + val + '"></label>'; }
  // Escena para explorar: controles (sliders/inputs con data-k) + dibujo que se recalcula
  function escena(el, ctrls, dibujar, extra) {
    el.innerHTML = '<div class="lb2-ctls">' + ctrls + '</div><div class="lb-vista"></div>' + (extra || '');
    var v = el.querySelector('.lb-vista');
    function val() { var o = {}; [].forEach.call(el.querySelectorAll('[data-k]'), function (i) { o[i.getAttribute('data-k')] = i.type === 'range' || i.inputMode === 'numeric' || i.inputMode === 'decimal' ? num(i.value) : i.value; var out = el.querySelector('[data-o="' + i.getAttribute('data-k') + '"]'); if (out) out.textContent = fmt(num(i.value)); }); return o; }
    function pintar() { v.innerHTML = dibujar(val()); }
    el.addEventListener('input', function (e) { if (e.target.matches('[data-k]')) pintar(); });
    el._pintar = pintar; pintar();
  }
  // Ejercicio de respuesta: campos numéricos / fracción / texto
  function respuesta(el, api, datos) {
    H.ejercicio(el, api, '', function (c) {
      var D = datos(); el.querySelector('.lb-cons').innerHTML = D.cons;
      c.innerHTML = (D.html || '') + '<div class="lb2-campos">' + D.campos.map(function (f, i) {
        return '<label class="lb2-campo">' + (f.lab ? '<span>' + f.lab + '</span>' : '') + (f.tipo === 'frac' ? '<span class="lb-fr-in"><input class="lb-inp chico" inputmode="numeric" data-i="' + i + '" data-p="n"><i></i><input class="lb-inp chico" inputmode="numeric" data-i="' + i + '" data-p="d"></span>'
          : '<input class="lb-inp' + (f.tipo === 'texto' ? ' largo' : '') + '" ' + (f.tipo === 'texto' ? '' : 'inputmode="decimal"') + ' data-i="' + i + '">') + (f.un ? '<em>' + f.un + '</em>' : '') + '</label>';
      }).join('') + '</div>';
      function leer(i) { var f = D.campos[i]; if (f.tipo === 'frac') { var n = num(c.querySelector('[data-i="' + i + '"][data-p="n"]').value), d = num(c.querySelector('[data-i="' + i + '"][data-p="d"]').value); return d ? n / d : NaN; } var x = c.querySelector('[data-i="' + i + '"]').value; return f.tipo === 'texto' ? H.norm(x) : num(x); }
      return {
        comprobar: function () {
          var vacio = D.campos.some(function (f, i) { var x = leer(i); return f.tipo === 'texto' ? !x : !isFinite(x); });
          if (vacio) return { ok: false, msg: 'Completá todos los casilleros.' };
          var ok = D.campos.every(function (f, i) { var x = leer(i); if (f.tipo === 'texto') return [].concat(f.v).some(function (v) { return H.norm(v) === x; }); return Math.abs(x - f.v) <= (f.tol || 1e-9) + Math.abs(f.v) * 1e-9; });
          return ok ? { ok: true, msg: D.bien || '¡Bien!' } : { ok: false, msg: D.ayuda || 'Revisalo.' };
        },
        resolver: function () { D.campos.forEach(function (f, i) { if (f.tipo === 'frac') { c.querySelector('[data-i="' + i + '"][data-p="n"]').value = f.n; c.querySelector('[data-i="' + i + '"][data-p="d"]').value = f.d; } else c.querySelector('[data-i="' + i + '"]').value = f.tipo === 'texto' ? [].concat(f.v)[0] : String(f.v).replace('.', ','); }); }
      };
    });
  }
  // Ejercicio de clasificar en cajas (genérico)
  function cajas(el, api, datos) {
    H.ejercicio(el, api, '', function (c) {
      var D = datos(); el.querySelector('.lb-cons').innerHTML = D.tit;
      c.innerHTML = '<div class="lb-cajas n' + D.cajas.length + '">' + D.cajas.map(function (t, k) { return '<div class="lb-caja" data-dest="' + k + '"><b>' + t + '</b><div class="lb-dest-c"></div></div>'; }).join('') + '</div>' +
        '<div class="lb-banco">' + mezclar(D.items).map(function (x) { return chip(x.v, x.t, ' data-c="' + x.c + '"'); }).join('') + '</div><p class="lb-ayuda">Tocá una ficha y después la caja donde va.</p>';
      H.tocarYUbicar(c);
      return {
        comprobar: function () {
          var mal = 0, falt = c.querySelector('.lb-banco').querySelectorAll('.lb-chip').length;
          [].forEach.call(c.querySelectorAll('.lb-caja .lb-chip'), function (ch) { var ok = ch.getAttribute('data-c') === ch.closest('[data-dest]').getAttribute('data-dest'); ch.classList.toggle('bien', ok); ch.classList.toggle('mal', !ok); if (!ok) mal++; });
          if (falt) return { ok: false, msg: 'Te faltan ubicar ' + falt + '.' };
          return mal ? { ok: false, msg: 'Hay ' + mal + ' mal ubicada' + (mal > 1 ? 's' : '') + ' (marcadas). Tocalas para devolverlas.' } : { ok: true, msg: '¡Todas bien ubicadas!' };
        },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-chip'), function (ch) { c.querySelector('[data-dest="' + ch.getAttribute('data-c') + '"] .lb-dest-c').appendChild(ch); }); }
      };
    });
  }
  function svgAng(g, w, h, rr) {
    w = w || 240; h = h || 150; var cx = w / 2, cy = h - 22, r = rr || 95, a = g * Math.PI / 180, x2 = cx + r * Math.cos(a), y2 = cy - r * Math.sin(a), ra = 30;
    var arco = g >= 360 ? '<circle cx="' + cx + '" cy="' + cy + '" r="' + ra + '" class="arc"/>' : '<path class="arc" d="M' + (cx + ra) + ' ' + cy + ' A' + ra + ' ' + ra + ' 0 ' + (g > 180 ? 1 : 0) + ' 0 ' + (cx + ra * Math.cos(a)) + ' ' + (cy - ra * Math.sin(a)) + '"/>';
    return '<svg viewBox="0 0 ' + w + ' ' + h + '" class="lb2-svg">' + arco + '<line x1="' + cx + '" y1="' + cy + '" x2="' + (cx + r) + '" y2="' + cy + '" class="rayo"/><line x1="' + cx + '" y1="' + cy + '" x2="' + x2.toFixed(1) + '" y2="' + y2.toFixed(1) + '" class="rayo"/>' + (g === 90 ? '<rect x="' + cx + '" y="' + (cy - 12) + '" width="12" height="12" class="recto"/>' : '') + '</svg>';
  }
  function tipoAng(g) { return g === 0 ? 'nulo' : g < 90 ? 'agudo' : g === 90 ? 'recto' : g < 180 ? 'obtuso' : g === 180 ? 'llano' : g < 360 ? 'cóncavo' : 'de un giro'; }

  // ======================= GEOMETRÍA =======================
  M.transportador = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('g', 'Abertura', 0, 360, 5, R(4, 30) * 5, '°'), function (o) { return svgAng(o.g, 260, 160) + '<p class="lb-res">' + o.g + '° · ángulo ' + tipoAng(o.g) + '</p><p class="lb-nota">Agudo: menos de 90°. Recto: 90°. Obtuso: entre 90° y 180°. Llano: 180°. Cóncavo: más de 180°.</p>'; });
  } };
  M.triangulo = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('a', 'Lado a', 1, 12, 1, 5, ' cm') + ctrl('b', 'Lado b', 1, 12, 1, 5, ' cm') + ctrl('c', 'Lado c', 1, 12, 1, 6, ' cm'), function (o) {
      var a = o.a, b = o.b, c = o.c;
      if (!(a < b + c && b < a + c && c < a + b)) return '<p class="lb-res">No se puede armar</p><p class="lb-nota">Cada lado tiene que ser menor que la suma de los otros dos (desigualdad triangular): ' + Math.max(a, b, c) + ' no es menor que ' + (a + b + c - Math.max(a, b, c)) + '.</p>';
      var A = Math.acos((b * b + c * c - a * a) / (2 * b * c)), Bg = Math.acos((a * a + c * c - b * b) / (2 * a * c)), Cg = Math.PI - A - Bg, deg = function (x) { return Math.round(x * 180 / Math.PI); };
      var s = 200 / Math.max(a, b, c), P = [[20, 150], [20 + c * s, 150], [20 + b * s * Math.cos(A), 150 - b * s * Math.sin(A)]];
      var lados = a === b && b === c ? 'equilátero' : (a === b || b === c || a === c) ? 'isósceles' : 'escaleno', mx = Math.max(deg(A), deg(Bg), deg(Cg)), ang = Math.abs(Math.max(a, b, c) ** 2 - (a * a + b * b + c * c - Math.max(a, b, c) ** 2)) < 1e-9 ? 'rectángulo' : mx > 90 ? 'obtusángulo' : 'acutángulo';
      return '<svg viewBox="0 0 250 165" class="lb2-svg"><polygon class="fig" points="' + P.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' ') + '"/></svg>' +
        '<p class="lb-res">Triángulo ' + lados + ' y ' + ang + '</p><p class="lb-nota">Ángulos: ' + deg(A) + '° + ' + deg(Bg) + '° + ' + deg(Cg) + '° = 180°.</p>';
    });
  } };
  M.poligono_angulos = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('n', 'Cantidad de lados', 3, 10, 1, 4), function (o) {
      var n = o.n, P = [], cx = 120, cy = 95, r = 80; for (var i = 0; i < n; i++) { var t = -Math.PI / 2 + 2 * Math.PI * i / n; P.push([cx + r * Math.cos(t), cy + r * Math.sin(t)]); }
      var diag = ''; for (var j = 2; j < n - 1; j++) diag += '<line class="diag" x1="' + P[0][0].toFixed(1) + '" y1="' + P[0][1].toFixed(1) + '" x2="' + P[j][0].toFixed(1) + '" y2="' + P[j][1].toFixed(1) + '"/>';
      return '<svg viewBox="0 0 240 190" class="lb2-svg"><polygon class="fig" points="' + P.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' ') + '"/>' + diag + '</svg>' +
        '<p class="lb-nota">Desde un vértice salen ' + (n - 3) + ' diagonal' + (n - 3 === 1 ? '' : 'es') + ' que lo parten en <b>' + (n - 2) + ' triángulos</b>.</p><p class="lb-res">Suma de ángulos = ' + (n - 2) + ' × 180° = ' + fmt((n - 2) * 180) + '°</p>';
    });
  } };
  var FIG = { rectangulo: ['Rectángulo', 'base × altura'], triangulo: ['Triángulo', '(base × altura) ÷ 2'], paralelogramo: ['Paralelogramo', 'base × altura'], rombo: ['Rombo', '(D × d) ÷ 2'], trapecio: ['Trapecio', '(B + b) × altura ÷ 2'] };
  function dibFig(f, b, h, b2) {
    var u = Math.min(22, 200 / Math.max(b, b2 || 0, 1), 130 / h), x0 = 15, y0 = 15 + h * u, grid = '';
    for (var i = 0; i <= Math.max(b, b2 || 0) + 2; i++) grid += '<line class="grid" x1="' + (x0 + i * u) + '" y1="10" x2="' + (x0 + i * u) + '" y2="' + y0 + '"/>';
    for (var j = 0; j <= h; j++) grid += '<line class="grid" x1="' + x0 + '" y1="' + (y0 - j * u) + '" x2="' + (x0 + (Math.max(b, b2 || 0) + 2) * u) + '" y2="' + (y0 - j * u) + '"/>';
    var pts = f === 'triangulo' ? [[0, 0], [b, 0], [b / 2, h]] : f === 'paralelogramo' ? [[0, 0], [b, 0], [b + 2, h], [2, h]] : f === 'rombo' ? [[b / 2, 0], [b, h / 2], [b / 2, h], [0, h / 2]] : f === 'trapecio' ? [[0, 0], [b, 0], [(b + b2) / 2, h], [(b - b2) / 2, h]] : [[0, 0], [b, 0], [b, h], [0, h]];
    return '<svg viewBox="0 0 ' + (x0 * 2 + (Math.max(b, b2 || 0) + 2) * u) + ' ' + (y0 + 12) + '" class="lb2-svg">' + grid + '<polygon class="fig" points="' + pts.map(function (p) { return (x0 + p[0] * u).toFixed(1) + ',' + (y0 - p[1] * u).toFixed(1); }).join(' ') + '"/></svg>';
  }
  function areaFig(f, b, h, b2) { return f === 'triangulo' || f === 'rombo' ? b * h / 2 : f === 'trapecio' ? (b + b2) * h / 2 : b * h; }
  M.area_figura = { tipo: 'ejemplo', render: function (el, p) {
    var f = FIG[p.figura] ? p.figura : 'rectangulo';
    escena(el, ctrl('b', f === 'rombo' ? 'Diagonal mayor D' : f === 'trapecio' ? 'Base mayor B' : 'Base', 2, 10, 1, 6, ' cm') + (f === 'trapecio' ? ctrl('c', 'Base menor b', 1, 9, 1, 3, ' cm') : '') + ctrl('h', f === 'rombo' ? 'Diagonal menor d' : 'Altura', 1, 6, 1, 4, ' cm'), function (o) {
      var b2 = f === 'trapecio' ? Math.min(o.c, o.b - 1) : 0, A = areaFig(f, o.b, o.h, b2);
      return dibFig(f, o.b, o.h, b2) + '<p class="lb-nota">' + FIG[f][0] + ': área = ' + FIG[f][1] + '. Cada cuadradito es 1 cm².</p><p class="lb-res">A = ' + (f === 'trapecio' ? '(' + o.b + ' + ' + b2 + ') × ' + o.h + ' ÷ 2' : f === 'triangulo' || f === 'rombo' ? o.b + ' × ' + o.h + ' ÷ 2' : o.b + ' × ' + o.h) + ' = ' + fmt(A) + ' cm²</p>';
    });
  } };
  M.volumen_cubitos = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('a', 'Largo', 1, 6, 1, 4) + ctrl('b', 'Ancho', 1, 5, 1, 3) + ctrl('c', 'Alto', 1, 5, 1, 2), function (o) {
      var s = 16, cubos = '', ox = 30, oy = 170;
      function cubo(x, y, z) { var px = ox + (x - y) * s * .87 + o.b * s * .87, py = oy - (x + y) * s * .5 - z * s;
        return '<polygon class="cT" points="' + [[px, py - s], [px + s * .87, py - s * 1.5], [px, py - s * 2], [px - s * .87, py - s * 1.5]].map(function (q) { return q.join(','); }).join(' ') + '"/><polygon class="cL" points="' + [[px - s * .87, py - s * 1.5], [px, py - s], [px, py], [px - s * .87, py - s * .5]].map(function (q) { return q.join(','); }).join(' ') + '"/><polygon class="cR" points="' + [[px, py - s], [px + s * .87, py - s * 1.5], [px + s * .87, py - s * .5], [px, py]].map(function (q) { return q.join(','); }).join(' ') + '"/>'; }
      for (var z = 0; z < o.c; z++) for (var y = o.b - 1; y >= 0; y--) for (var x = o.a - 1; x >= 0; x--) cubos += cubo(x, y, z);
      return '<svg viewBox="0 0 260 190" class="lb2-svg">' + cubos + '</svg><p class="lb-nota">Una capa tiene ' + o.a + ' × ' + o.b + ' = ' + o.a * o.b + ' cubitos, y hay ' + o.c + ' capa' + (o.c > 1 ? 's' : '') + '.</p><p class="lb-res">V = ' + o.a + ' × ' + o.b + ' × ' + o.c + ' = ' + o.a * o.b * o.c + ' cm³</p>';
    });
  } };
  M.circulo = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('r', 'Radio', 1, 10, 1, 4, ' cm'), function (o) {
      return '<svg viewBox="0 0 240 230" class="lb2-svg"><circle class="fig" cx="120" cy="115" r="' + o.r * 10 + '"/><line class="rayo" x1="120" y1="115" x2="' + (120 + o.r * 10) + '" y2="115"/></svg>' +
        '<p class="lb-nota">Diámetro = 2 × radio = ' + 2 * o.r + ' cm. Usamos π ≈ 3,14.</p><p class="lb-res">Longitud = 2 × π × r = ' + fmt(r2(2 * PI * o.r)) + ' cm · Área = π × r² = ' + fmt(r2(PI * o.r * o.r)) + ' cm²</p>';
    });
  } };
  // ejercicios de geometría
  M.angulo_tipo = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () {
      var T = ['agudo', 'recto', 'obtuso', 'llano'], it = [], vis = {};
      while (it.length < 8) { var t = it.length % 4, g = t === 0 ? R(1, 17) * 5 : t === 1 ? 90 : t === 2 ? R(19, 35) * 5 : 180; if (vis[g] && t !== 1 && t !== 3) continue; vis[g] = 1; it.push({ v: g + '_' + it.length, t: g + '°', c: t }); }
      return { tit: 'Ubicá cada ángulo según su tipo.', cajas: T.map(function (x) { return x.charAt(0).toUpperCase() + x.slice(1); }), items: it };
    });
  } };
  M.angulo_falta = { tipo: 'ejercicio', render: function (el, p, api) {
    var modo = p.modo || 'triangulo';
    respuesta(el, api, function () {
      if (modo === 'complementario' || modo === 'suplementario') { var tot = modo === 'complementario' ? 90 : 180, a = R(5, tot / 5 - 1) * 5;
        return { cons: '¿Cuánto mide el ángulo <b>' + modo + '</b> de uno de <b>' + a + '°</b>?', html: svgAng(a), campos: [{ v: tot - a, un: '°' }], ayuda: (modo === 'complementario' ? 'Los complementarios suman 90°' : 'Los suplementarios suman 180°') + ': ' + tot + '° − ' + a + '°.', bien: '¡Bien! ' + tot + '° − ' + a + '° = ' + (tot - a) + '°.' }; }
      if (modo === 'cuadrilatero') { var x, y, z, w, tt = 0; do { x = R(50, 130); y = R(50, 130); z = R(50, 120); w = 360 - x - y - z; } while ((w < 30 || w > 200) && tt++ < 500);
        return { cons: 'Un cuadrilátero tiene ángulos de <b>' + x + '°</b>, <b>' + y + '°</b> y <b>' + z + '°</b>. ¿Cuánto mide el cuarto?', campos: [{ v: w, un: '°' }], ayuda: 'Los ángulos de un cuadrilátero suman 360°: 360° − ' + x + '° − ' + y + '° − ' + z + '°.', bien: '¡Bien! Suman 360°.' }; }
      var A = R(25, 95), Bg = R(25, 150 - A);
      return { cons: 'Un triángulo tiene ángulos de <b>' + A + '°</b> y <b>' + Bg + '°</b>. ¿Cuánto mide el tercero?', campos: [{ v: 180 - A - Bg, un: '°' }], ayuda: 'Los ángulos de un triángulo suman 180°: 180° − ' + A + '° − ' + Bg + '°.', bien: '¡Bien! 180° − ' + A + '° − ' + Bg + '° = ' + (180 - A - Bg) + '°.' };
    });
  } };
  M.area_perimetro = { tipo: 'ejercicio', render: function (el, p, api) {
    var que = p.que === 'perimetro' ? 'perimetro' : 'area';
    respuesta(el, api, function () {
      var f = p.figura && FIG[p.figura] ? p.figura : pick(que === 'perimetro' ? ['rectangulo'] : ['rectangulo', 'triangulo', 'paralelogramo', 'rombo', 'trapecio']), b = R(3, 10), h = R(2, 6), b2 = f === 'trapecio' ? R(1, b - 1) : 0;
      if (f === 'triangulo' || f === 'rombo') { if ((b * h) % 2) b++; }
      if (f === 'trapecio' && ((b + b2) * h) % 2) h++;
      if (que === 'perimetro') { var lados = [b, h, b, h]; return { cons: 'Un rectángulo mide <b>' + b + ' cm</b> de base y <b>' + h + ' cm</b> de altura. ¿Cuál es su <b>perímetro</b>?', html: dibFig('rectangulo', b, h), campos: [{ v: 2 * (b + h), un: 'cm' }], ayuda: 'El perímetro es la suma de todos los lados: ' + lados.join(' + ') + '.', bien: '¡Bien! ' + lados.join(' + ') + ' = ' + 2 * (b + h) + ' cm.' }; }
      var dato = f === 'rombo' ? 'diagonales <b>' + b + ' cm</b> y <b>' + h + ' cm</b>' : f === 'trapecio' ? 'bases <b>' + b + ' cm</b> y <b>' + b2 + ' cm</b> y altura <b>' + h + ' cm</b>' : 'base <b>' + b + ' cm</b> y altura <b>' + h + ' cm</b>';
      return { cons: 'Calculá el <b>área</b> del ' + FIG[f][0].toLowerCase() + ' de ' + dato + '.', html: dibFig(f, b, h, b2), campos: [{ v: areaFig(f, b, h, b2), un: 'cm²' }], ayuda: 'Área del ' + FIG[f][0].toLowerCase() + ' = ' + FIG[f][1] + '.', bien: '¡Bien! A = ' + fmt(areaFig(f, b, h, b2)) + ' cm².' };
    });
  } };
  M.volumen = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var cubo = Math.random() < .3, a = R(2, 9), b = cubo ? a : R(2, 8), c = cubo ? a : R(2, 7);
      return { cons: cubo ? 'Calculá el volumen de un <b>cubo</b> de <b>' + a + ' cm</b> de arista.' : 'Calculá el volumen de una caja (prisma) de <b>' + a + ' cm</b> × <b>' + b + ' cm</b> × <b>' + c + ' cm</b>.', campos: [{ v: a * b * c, un: 'cm³' }], ayuda: cubo ? 'V = arista × arista × arista.' : 'V = largo × ancho × alto.', bien: '¡Bien! V = ' + a + ' × ' + b + ' × ' + c + ' = ' + a * b * c + ' cm³.' }; });
  } };
  var UN = { longitud: [['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'], 10], capacidad: [['kl', 'hl', 'dal', 'l', 'dl', 'cl', 'ml'], 10], masa: [['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'], 10],
    superficie: [['km²', 'hm²', 'dam²', 'm²', 'dm²', 'cm²', 'mm²'], 100], volumen: [['km³', 'hm³', 'dam³', 'm³', 'dm³', 'cm³', 'mm³'], 1000] };
  M.convertir_unidades = { tipo: 'ejercicio', render: function (el, p, api) {
    var U = UN[p.magnitud] || UN.longitud;
    respuesta(el, api, function () { var i = R(0, 6), j = R(0, 6); while (Math.abs(i - j) < 1 || Math.abs(i - j) > (U[1] > 10 ? 2 : 3)) j = R(0, 6);
      var x = R(1, 99) * (j < i ? Math.pow(U[1], i - j) : 1), f = Math.pow(U[1], Math.abs(j - i)), v = j > i ? x * f : x / f;
      return { cons: 'Pasá <b>' + fmt(x) + ' ' + U[0][i] + '</b> a <b>' + U[0][j] + '</b>.', campos: [{ v: v, un: U[0][j] }], ayuda: 'De ' + U[0][i] + ' a ' + U[0][j] + ' hay ' + Math.abs(j - i) + ' escalón' + (Math.abs(j - i) > 1 ? 'es' : '') + ': ' + (j > i ? 'bajás, multiplicás' : 'subís, dividís') + ' por ' + fmt(f) + '.', bien: '¡Bien! ' + fmt(x) + ' ' + U[0][i] + ' = ' + fmt(v) + ' ' + U[0][j] + '.' }; });
  } };

  // ======================= ÁLGEBRA =======================
  var EXPR = [['3x + 2', function (x) { return 3 * x + 2; }], ['2x − 5', function (x) { return 2 * x - 5; }], ['x² + 1', function (x) { return x * x + 1; }], ['2(x + 3)', function (x) { return 2 * (x + 3); }], ['x² − 2x', function (x) { return x * x - 2 * x; }], ['10 − 3x', function (x) { return 10 - 3 * x; }], ['(x + 1)²', function (x) { return (x + 1) * (x + 1); }]];
  M.valor_numerico = { tipo: 'ejemplo', render: function (el) {
    var e = pick(EXPR);
    escena(el, ctrl('x', 'x', -5, 10, 1, 2), function (o) { var x = o.x, xs = x < 0 ? '(' + sig(x) + ')' : String(x);
      return '<p class="lb-res">' + e[0] + '</p><p class="lb-nota">Reemplazamos x por ' + xs + ': <b>' + e[0].replace(/x/g, xs) + ' = ' + sig(e[1](x)).replace('+', '') + '</b></p><table class="lb2-tab"><tr><th>x</th>' + [-2, -1, 0, 1, 2, 3].map(function (k) { return '<td' + (k === x ? ' class="on"' : '') + '>' + k + '</td>'; }).join('') + '</tr><tr><th>valor</th>' + [-2, -1, 0, 1, 2, 3].map(function (k) { return '<td' + (k === x ? ' class="on"' : '') + '>' + e[1](k) + '</td>'; }).join('') + '</tr></table>'; },
      '<div class="lb-pie"><button type="button" class="lb-btn suave" data-otra="1">🔄 Otra expresión</button></div>');
    el.addEventListener('click', function (ev) { if (ev.target.closest('[data-otra]')) { e = pick(EXPR); el._pintar(); } });
  } };
  function terminos() { var L = [], g = { x2: 0, x: 0, c: 0 }; for (var i = 0; i < 6; i++) { var t = pick(['x2', 'x', 'x', 'c']), k = R(1, 9) * pick([1, -1]); g[t] += k; L.push([t, k]); } return { L: L, g: g }; }
  function termTxt(t, k, primero) { var a = Math.abs(k), s = k < 0 ? '− ' : primero ? '' : '+ ', lit = t === 'x2' ? 'x²' : t === 'x' ? 'x' : ''; return s + (lit && a === 1 ? '' : a) + lit; }
  M.terminos_semejantes = { tipo: 'ejemplo', render: function (el) {
    var T = terminos();
    function pintar() { var orden = ['x2', 'x', 'c'], col = { x2: 't0', x: 't1', c: 't2' };
      el.innerHTML = '<p class="lb-res">' + T.L.map(function (q, i) { return '<span class="lb2-term ' + col[q[0]] + '">' + termTxt(q[0], q[1], !i) + '</span>'; }).join(' ') + '</p><p class="lb-nota">Mismo color = misma parte literal: son <b>semejantes</b> y se suman sus coeficientes.</p>' +
        orden.map(function (t) { var ks = T.L.filter(function (q) { return q[0] === t; }); if (!ks.length) return ''; return '<p class="lb-nota"><span class="lb2-term ' + col[t] + '">' + (t === 'x2' ? 'x²' : t === 'x' ? 'x' : 'números') + '</span>: ' + ks.map(function (q) { return sig(q[1]); }).join(' ') + ' = <b>' + sig(T.g[t]) + '</b></p>'; }).join('') +
        '<p class="lb-res">= ' + orden.filter(function (t) { return T.g[t]; }).map(function (t, i) { return termTxt(t, T.g[t], !i); }).join(' ') + '</p><div class="lb-pie"><button type="button" class="lb-btn suave" data-otra="1">🔄 Otra expresión</button></div>'; }
    el.onclick = function (e) { if (e.target.closest('[data-otra]')) { T = terminos(); pintar(); } }; pintar();
  } };
  M.patron_figuras = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('n', 'Figura número', 1, 8, 1, 3), function (o) { var n = o.n, s = 22, lin = '';
      for (var i = 0; i <= n; i++) lin += '<line class="fosf" x1="' + (10 + i * s) + '" y1="10" x2="' + (10 + i * s) + '" y2="' + (10 + s) + '"/>';
      for (var j = 0; j < n; j++) lin += '<line class="fosf" x1="' + (10 + j * s) + '" y1="10" x2="' + (10 + (j + 1) * s) + '" y2="10"/><line class="fosf" x1="' + (10 + j * s) + '" y1="' + (10 + s) + '" x2="' + (10 + (j + 1) * s) + '" y2="' + (10 + s) + '"/>';
      return '<svg viewBox="0 0 ' + (20 + n * s) + ' 45" class="lb2-svg" style="max-height:90px">' + lin + '</svg><table class="lb2-tab"><tr><th>Figura</th>' + [1, 2, 3, 4, 5].map(function (k) { return '<td' + (k === n ? ' class="on"' : '') + '>' + k + '</td>'; }).join('') + '</tr><tr><th>Fósforos</th>' + [1, 2, 3, 4, 5].map(function (k) { return '<td' + (k === n ? ' class="on"' : '') + '>' + (3 * k + 1) + '</td>'; }).join('') + '</tr></table>' +
        '<p class="lb-nota">Cada cuadradito nuevo agrega 3 fósforos al primero: la fórmula es <b>3n + 1</b>.</p><p class="lb-res">Figura ' + n + ': 3 × ' + n + ' + 1 = ' + (3 * n + 1) + ' fósforos</p>'; });
  } };
  M.valor_numerico_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var e = pick(EXPR), x = R(-4, 6), xs = x < 0 ? '(' + sig(x) + ')' : x;
      return { cons: 'Calculá el valor de <b>' + e[0] + '</b> para <b>x = ' + x + '</b>.', campos: [{ v: e[1](x) }], ayuda: 'Reemplazá x por ' + xs + ': ' + e[0].replace(/x/g, xs) + '. Primero potencias, después multiplicaciones y al final sumas y restas.', bien: '¡Bien! ' + e[0].replace(/x/g, xs) + ' = ' + e[1](x) + '.' }; });
  } };
  M.reducir_terminos = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var T = terminos(), ts = ['x2', 'x', 'c'].filter(function (t) { return T.L.some(function (q) { return q[0] === t; }); });
      return { cons: 'Reducí: <b>' + T.L.map(function (q, i) { return termTxt(q[0], q[1], !i); }).join(' ') + '</b>. Escribí cuánto queda de cada parte.', campos: ts.map(function (t) { return { lab: t === 'x2' ? 'x²:' : t === 'x' ? 'x:' : 'número:', v: T.g[t] }; }), ayuda: 'Sumá por separado los coeficientes de los términos semejantes (los que tienen la misma parte literal), con su signo.', bien: '¡Bien reducido!' }; });
  } };
  M.patron_termino = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = R(1, 9), d = R(2, 7), n = R(8, 20), seq = [0, 1, 2, 3].map(function (k) { return a + k * d; });
      return { cons: 'La secuencia sigue así: <b>' + seq.join(', ') + ', …</b> ¿Qué número va en el lugar <b>' + n + '</b>?', campos: [{ v: a + (n - 1) * d }], ayuda: 'Cada vez se suma ' + d + '. El lugar n vale ' + a + ' + (n − 1) × ' + d + '.', bien: '¡Bien! ' + a + ' + ' + (n - 1) + ' × ' + d + ' = ' + (a + (n - 1) * d) + '.' }; });
  } };
  M.ecuacion = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var x = R(-6, 12), a = R(2, 7), b = R(-15, 20), dos = p.modo === 'dos_miembros' || (p.modo !== 'simple' && Math.random() < .4);
      if (dos) { var c2 = R(1, a - 1) || 1, d = a * x + b - c2 * x; return { cons: 'Resolvé: <b>' + a + 'x ' + (b < 0 ? '− ' + (-b) : '+ ' + b) + ' = ' + (c2 === 1 ? '' : c2) + 'x ' + (d < 0 ? '− ' + (-d) : '+ ' + d) + '</b>', campos: [{ lab: 'x =', v: x }], ayuda: 'Juntá las x de un lado y los números del otro, y después dividí.', bien: '¡Bien! x = ' + x + '.' }; }
      return { cons: 'Resolvé: <b>' + a + 'x ' + (b < 0 ? '− ' + (-b) : '+ ' + b) + ' = ' + (a * x + b) + '</b>', campos: [{ lab: 'x =', v: x }], ayuda: 'Primero ' + (b < 0 ? 'sumá ' + (-b) : 'restá ' + b) + ' en los dos miembros y después dividí por ' + a + '.', bien: '¡Bien! x = ' + x + '. Verificación: ' + a + ' · ' + x + (b < 0 ? ' − ' + (-b) : ' + ' + b) + ' = ' + (a * x + b) + '.' }; });
  } };
  M.traducir = { tipo: 'ejercicio', render: function (el, p, api) {
    var F = [['El doble de un número', '2x'], ['Un número aumentado en 5', 'x + 5'], ['La mitad de un número', 'x/2'], ['El triple de un número, menos 1', '3x − 1'], ['El cuadrado de un número', 'x²'], ['El siguiente de un número', 'x + 1'], ['Un número disminuido en 4', 'x − 4'], ['El doble de la suma de un número y 3', '2(x + 3)'], ['El anterior de un número', 'x − 1'], ['La cuarta parte de un número', 'x/4']];
    H.ejercicio(el, api, 'Llevá cada expresión <b>simbólica</b> al lado de su frase.', function (c) {
      var S = mezclar(F).slice(0, 5);
      c.innerHTML = '<div class="lb-pares uno">' + S.map(function (x, k) { return '<div class="lb-par"><span class="lb-izq">' + x[0] + '</span><span class="lb-ig">→</span><span class="lb-hueco" data-dest="' + k + '" data-max="1"></span></div>'; }).join('') + '</div><div class="lb-banco">' + mezclar(S.map(function (x) { return chip(x[1]); })).join('') + '</div>';
      H.tocarYUbicar(c);
      return { comprobar: function () { var mal = 0, falt = 0; S.forEach(function (x, k) { var ch = c.querySelector('[data-dest="' + k + '"] .lb-chip'); if (!ch) { falt++; return; } var ok = ch.getAttribute('data-v') === x[1]; ch.classList.toggle('bien', ok); ch.classList.toggle('mal', !ok); if (!ok) mal++; });
          return falt ? { ok: false, msg: 'Te faltan completar ' + falt + '.' } : mal ? { ok: false, msg: 'Hay ' + mal + ' que no corresponde' + (mal > 1 ? 'n' : '') + '.' } : { ok: true, msg: '¡Todas bien traducidas!' }; },
        resolver: function () { S.forEach(function (x, k) { c.querySelector('[data-dest="' + k + '"]').appendChild(c.querySelector('.lb-banco [data-v="' + CSS.escape(x[1]) + '"]')); }); } };
    });
  } };

  // ======================= NÚMEROS =======================
  M.porcentaje_barra = { tipo: 'ejemplo', render: function (el, p) {
    var modo = p.modo || 'parte';
    escena(el, ctrl('p', 'Porcentaje', 5, 95, 5, 25, ' %') + ctrl('t', 'Cantidad', 100, 5000, 100, 2400), function (o) { var parte = o.t * o.p / 100;
      var barra = '<div class="lb2-barra"><i style="width:' + o.p + '%"></i><span>' + o.p + ' %</span></div><div class="lb2-esc"><span>0</span><span>' + fmt(o.t) + ' = 100 %</span></div>';
      if (modo === 'aumento' || modo === 'descuento') { var fin = modo === 'aumento' ? o.t + parte : o.t - parte;
        return barra + '<p class="lb-nota">' + (modo === 'aumento' ? 'Aumento' : 'Descuento') + ': ' + o.p + ' % de ' + fmt(o.t) + ' = ' + fmt(parte) + '. También: ' + fmt(o.t) + ' × ' + fmt((modo === 'aumento' ? 100 + o.p : 100 - o.p) / 100) + '.</p><p class="lb-res">Precio final: $' + fmt(fin) + '</p>'; }
      return barra + '<p class="lb-nota">El ' + o.p + ' % es ' + o.p + ' de cada 100: ' + fmt(o.t) + ' × ' + o.p + ' ÷ 100.</p><p class="lb-res">' + o.p + ' % de ' + fmt(o.t) + ' = ' + fmt(parte) + '</p>'; });
  } };
  M.porcentaje = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var m = p.modo || pick(['parte', 'que', 'descuento', 'aumento']), pc = pick([5, 10, 15, 20, 25, 30, 40, 50, 75]), t = R(2, 60) * 100, parte = t * pc / 100;
      if (m === 'que') return { cons: '¿Qué porcentaje es <b>' + fmt(parte) + '</b> de <b>' + fmt(t) + '</b>?', campos: [{ v: pc, un: '%' }], ayuda: 'Dividí la parte por el total y multiplicá por 100.', bien: '¡Bien! ' + fmt(parte) + ' ÷ ' + fmt(t) + ' × 100 = ' + pc + ' %.' };
      if (m === 'descuento' || m === 'aumento') return { cons: 'Un producto de <b>$' + fmt(t) + '</b> tiene un <b>' + (m === 'aumento' ? 'aumento' : 'descuento') + ' del ' + pc + ' %</b>. ¿Cuál es el precio final?', campos: [{ v: m === 'aumento' ? t + parte : t - parte, un: '$' }], ayuda: 'Calculá el ' + pc + ' % de ' + fmt(t) + ' y ' + (m === 'aumento' ? 'sumalo' : 'restalo') + '.', bien: '¡Bien! Precio final: $' + fmt(m === 'aumento' ? t + parte : t - parte) + '.' };
      return { cons: 'Calculá el <b>' + pc + ' %</b> de <b>' + fmt(t) + '</b>.', campos: [{ v: parte }], ayuda: 'Multiplicá ' + fmt(t) + ' × ' + pc + ' y dividí por 100.', bien: '¡Bien! ' + fmt(parte) + '.' }; });
  } };
  // operaciones combinadas: genera expresión con jerarquía y la resuelve paso a paso
  function expresion() {
    var a = R(2, 9), b = R(2, 9), c = R(2, 9), d = R(1, 9), t = R(0, 3);
    if (t === 0) return { e: a + ' + ' + b + ' × ' + c, pasos: [a + ' + ' + (b * c), String(a + b * c)], v: a + b * c };
    if (t === 1) return { e: '(' + a + ' + ' + b + ') × ' + c + ' − ' + d, pasos: [(a + b) + ' × ' + c + ' − ' + d, (a + b) * c + ' − ' + d, String((a + b) * c - d)], v: (a + b) * c - d };
    if (t === 2) { var q = b * c; return { e: a * d + ' − ' + q + ' ÷ ' + c + ' + ' + b, pasos: [a * d + ' − ' + b + ' + ' + b, String(a * d - b + b)], v: a * d }; }
    return { e: a + '² − ' + b + ' × ' + (c > 1 ? '(' + c + ' − 1)' : c), pasos: [a * a + ' − ' + b + ' × ' + (c - 1), a * a + ' − ' + b * (c - 1), String(a * a - b * (c - 1))], v: a * a - b * (c - 1) };
  }
  M.jerarquia = { tipo: 'ejemplo', render: function (el) {
    var X = expresion(), k = 0;
    function pintar() { el.innerHTML = '<p class="lb-res">' + X.e + '</p><ol class="lb2-pasos">' + X.pasos.slice(0, k).map(function (s, i) { return '<li>= ' + s + (i === X.pasos.length - 1 ? ' ✔' : '') + '</li>'; }).join('') + '</ol>' +
      '<p class="lb-nota">Orden: 1) paréntesis, 2) potencias y raíces, 3) multiplicaciones y divisiones, 4) sumas y restas (de izquierda a derecha).</p><div class="lb-pie">' + (k < X.pasos.length ? '<button type="button" class="lb-btn" data-s="1">Siguiente paso</button>' : '') + '<button type="button" class="lb-btn suave" data-o="1">🔄 Otra cuenta</button></div>'; }
    el.onclick = function (e) { if (e.target.closest('[data-s]')) { k++; pintar(); } if (e.target.closest('[data-o]')) { X = expresion(); k = 0; pintar(); } }; pintar();
  } };
  M.combinadas = { tipo: 'ejercicio', render: function (el, p, api) { respuesta(el, api, function () { var X = expresion(); return { cons: 'Resolvé respetando la jerarquía: <b>' + X.e + '</b>', campos: [{ v: X.v }], ayuda: 'Paso a paso: ' + X.pasos.join(' = ') + '.', bien: '¡Bien! ' + X.e + ' = ' + X.v + '.' }; }); } };
  function periodo(a, b) { var ent = Math.floor(a / b), r = a % b, vistos = {}, dig = '', pos = 0; while (r && vistos[r] == null && pos < 40) { vistos[r] = pos++; r *= 10; dig += Math.floor(r / b); r %= b; } return { ent: ent, dig: dig, ini: r ? vistos[r] : -1 }; }
  M.periodo = { tipo: 'ejemplo', render: function (el) {
    el.innerHTML = '<div class="lb2-ctls"><label class="lb2-ctl">Fracción: <input class="lb-inp chico" data-k="a" inputmode="numeric" value="' + pick([1, 2, 5, 7]) + '"> / <input class="lb-inp chico" data-k="b" inputmode="numeric" value="' + pick([3, 6, 7, 9, 11, 12]) + '"></label></div><div class="lb-vista"></div>';
    var v = el.querySelector('.lb-vista');
    function pintar() { var a = Math.floor(num(el.querySelector('[data-k="a"]').value)), b = Math.floor(num(el.querySelector('[data-k="b"]').value));
      if (!(a >= 0 && b >= 1 && b <= 99 && a <= 999)) { v.innerHTML = '<p class="lb-ayuda">Probá con números chicos (denominador hasta 99).</p>'; return; }
      var P = periodo(a, b), d = P.dig, txt = P.ini < 0 ? P.ent + (d ? ',' + d : '') : P.ent + ',' + d.slice(0, P.ini) + '<span class="lb2-per">' + d.slice(P.ini) + '</span>';
      v.innerHTML = '<p class="lb-res">' + a + '/' + b + ' = ' + txt + (P.ini < 0 ? '' : '…') + '</p><p class="lb-nota">' + (P.ini < 0 ? 'La división termina: es un <b>decimal exacto</b>.' : 'Al dividir, un resto se repite y desde ahí las cifras se repiten: el <b>período</b> (marcado) es ' + d.slice(P.ini) + '. ' + (P.ini === 0 ? 'Empieza enseguida: <b>periódico puro</b>.' : 'Antes hay cifras que no se repiten: <b>periódico mixto</b>.')) + '</p>'; }
    el.addEventListener('input', pintar); pintar();
  } };
  M.decimal_tipo = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = [], vis = {}, tope = 0;
      while (it.length < 9 && tope++ < 2000) { var b = R(2, 30), a = R(1, b * 2), P = periodo(a, b), t = P.ini < 0 ? 0 : P.ini === 0 ? 1 : 2, k = a + '/' + b; if (vis[k] || it.filter(function (x) { return x.c === t; }).length >= 3 || mcd(a, b) !== 1) continue; vis[k] = 1; it.push({ v: k, t: fr(a, b), c: t }); }
      return { tit: 'Ubicá cada fracción según el decimal que da.', cajas: ['Exacto', 'Periódico puro', 'Periódico mixto'], items: it }; });
  } };
  function cientif(x) { var e = Math.floor(Math.log10(Math.abs(x))), m = Math.round(x / Math.pow(10, e) * 1000) / 1000; if (m >= 10) { m /= 10; e++; } return { m: m, e: e }; }
  M.notacion_cientifica = { tipo: 'ejemplo', render: function (el) {
    el.innerHTML = '<div class="lb2-ctls"><label class="lb2-ctl">Número: <input class="lb-inp largo" data-k="n" inputmode="decimal" value="' + pick(['3.450.000', '0,00072', '58.000.000', '0,0305']) + '"></label></div><div class="lb-vista"></div>';
    var v = el.querySelector('.lb-vista');
    function pintar() { var x = num(el.querySelector('[data-k="n"]').value); if (!isFinite(x) || !x) { v.innerHTML = '<p class="lb-ayuda">Escribí un número distinto de 0.</p>'; return; }
      var C = cientif(x); v.innerHTML = '<p class="lb-nota">Movemos la coma hasta dejar <b>una sola cifra distinta de 0</b> antes de ella: ' + Math.abs(C.e) + ' lugar' + (Math.abs(C.e) === 1 ? '' : 'es') + ' hacia la ' + (C.e >= 0 ? 'izquierda (número grande: exponente positivo)' : 'derecha (número chico: exponente negativo)') + '.</p><p class="lb-res">' + fmt(x) + ' = ' + fmt(C.m) + ' × 10<sup>' + C.e + '</sup></p>'; }
    el.addEventListener('input', pintar); pintar();
  } };
  M.notacion = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var m = R(11, 99) / 10, e = pick([R(3, 8), -R(2, 6)]), x = Math.round(m * Math.pow(10, e) * 1e8) / 1e8;
      return { cons: 'Escribí <b>' + fmt(x) + '</b> en notación científica: mantisa × 10 elevado al exponente.', campos: [{ lab: 'Mantisa', v: m }, { lab: '× 10 elevado a', v: e }], ayuda: 'La mantisa tiene una sola cifra antes de la coma; el exponente es cuántos lugares corriste la coma (negativo si el número es menor que 1).', bien: '¡Bien! ' + fmt(m) + ' × 10^' + e + '.' }; });
  } };
  M.fraccion_barras = { tipo: 'ejemplo', render: function (el, p) {
    var resta = p.op === 'resta';
    escena(el, ctrl('a', 'Numerador 1', 1, 5, 1, 1) + ctrl('b', 'Denominador 1', 2, 6, 1, 2) + ctrl('c', 'Numerador 2', 1, 5, 1, 1) + ctrl('d', 'Denominador 2', 2, 6, 1, 3), function (o) {
      var den = o.b * o.d / mcd(o.b, o.d), n1 = o.a * den / o.b, n2 = o.c * den / o.d, res = resta ? n1 - n2 : n1 + n2;
      function barra(n, cls) { var s = ''; for (var i = 0; i < Math.max(den, n); i++) s += '<i class="' + (i < n ? cls : '') + (i >= den ? ' fuera' : '') + '"></i>'; return '<div class="lb2-fb">' + s + '</div>'; }
      return barra(n1, 'p1') + barra(n2, 'p2') + '<p class="lb-nota">Con denominador común ' + den + ': ' + fr(o.a, o.b) + ' = ' + fr(n1, den) + ' y ' + fr(o.c, o.d) + ' = ' + fr(n2, den) + '.</p><p class="lb-res">' + fr(n1, den) + (resta ? ' − ' : ' + ') + fr(n2, den) + ' = ' + fr(res, den) + (mcd(Math.abs(res), den) > 1 && res ? ' = ' + frHtml(res, den) : '') + '</p>'; });
  } };
  M.fraccion_area = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('a', 'Tomo', 1, 5, 1, 2) + ctrl('b', 'de', 2, 6, 1, 3) + ctrl('c', 'partes de', 1, 5, 1, 3) + ctrl('d', 'de', 2, 6, 1, 4), function (o) {
      var a = Math.min(o.a, o.b), c = Math.min(o.c, o.d), s = 26, g = '';
      for (var i = 0; i < o.d; i++) for (var j = 0; j < o.b; j++) g += '<rect x="' + (5 + i * s) + '" y="' + (5 + j * s) + '" width="' + s + '" height="' + s + '" class="' + (i < c && j < a ? 'c2' : i < c ? 'c1' : 'c0') + '"/>';
      return '<svg viewBox="0 0 ' + (10 + o.d * s) + ' ' + (10 + o.b * s) + '" class="lb2-svg" style="max-height:170px">' + g + '</svg><p class="lb-nota">Columnas pintadas: ' + fr(c, o.d) + '. De eso tomo ' + fr(a, o.b) + ' (lo más oscuro): ' + a * c + ' de ' + o.b * o.d + ' cuadraditos.</p><p class="lb-res">' + fr(a, o.b) + ' de ' + fr(c, o.d) + ' = ' + fr(a * c, o.b * o.d) + '</p>'; });
  } };
  M.fraccion_operar = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var op = p.op || pick(['suma', 'resta', 'producto', 'division']), a, b, c, d, n, dd, s, tt = 0;
      do { a = R(1, 7); b = R(2, 9); c = R(1, 7); d = R(2, 9); } while (op === 'resta' && a * d === c * b && tt++ < 200);
      if (op === 'suma') { n = a * d + c * b; dd = b * d; s = '+'; } else if (op === 'resta') { if (a * d < c * b) { var t = a; a = c; c = t; t = b; b = d; d = t; } n = a * d - c * b; dd = b * d; s = '−'; } else if (op === 'producto') { n = a * c; dd = b * d; s = '×'; } else { n = a * d; dd = b * c; s = '÷'; }
      return { cons: 'Resolvé: <b>' + fr(a, b) + ' ' + s + ' ' + fr(c, d) + '</b> (podés simplificar o no).', campos: [{ tipo: 'frac', v: n / dd, n: n, d: dd }], ayuda: op === 'suma' || op === 'resta' ? 'Buscá un denominador común y ' + (op === 'suma' ? 'sumá' : 'restá') + ' los numeradores.' : op === 'producto' ? 'Multiplicá numerador por numerador y denominador por denominador.' : 'Multiplicá por la inversa de la segunda fracción.', bien: '¡Bien! = ' + frs(n, dd) + '.' }; });
  } };
  var POSD = [['unidades', 1], ['décimos', .1], ['centésimos', .01]];
  M.redondeo = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('x', 'Número', 0, 20, .01, 7.36) + '<label class="lb2-ctl"><span>Redondear a</span><select class="lb-inp largo" data-k="p">' + POSD.map(function (q, i) { return '<option value="' + i + '"' + (i === 1 ? ' selected' : '') + '>' + q[0] + '</option>'; }).join('') + '</select></label>', function (o) {
      var u = POSD[+o.p][1], lo = Math.floor(o.x / u + 1e-9) * u, hi = lo + u, r = (o.x - lo) < u / 2 - 1e-9 ? lo : hi, W = 260, X = function (v) { return 20 + (v - lo) / u * (W - 40); };
      return '<svg viewBox="0 0 ' + W + ' 70" class="lb2-svg"><line class="rayo" x1="10" y1="35" x2="' + (W - 10) + '" y2="35"/><line class="rayo" x1="' + X(lo) + '" y1="27" x2="' + X(lo) + '" y2="43"/><line class="rayo" x1="' + X(hi) + '" y1="27" x2="' + X(hi) + '" y2="43"/><line class="diag" x1="' + X(lo + u / 2) + '" y1="25" x2="' + X(lo + u / 2) + '" y2="45"/><circle cx="' + X(o.x).toFixed(1) + '" cy="35" r="6" class="pt"/><text x="' + X(lo) + '" y="62">' + fmt(r2(lo)) + '</text><text x="' + X(hi) + '" y="62">' + fmt(r2(hi)) + '</text></svg>' +
        '<p class="lb-nota">' + fmt(o.x) + ' está entre ' + fmt(r2(lo)) + ' y ' + fmt(r2(hi)) + '. La rayita del medio es ' + fmt(r2(lo + u / 2)) + ': si llega o pasa, se redondea para arriba.</p><p class="lb-res">' + fmt(o.x) + ' ≈ ' + fmt(r2(r)) + '</p>'; });
  } };
  M.redondear = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var i = R(0, 2), u = POSD[i][1], x = R(100, 99999) / 1000, r = Math.round(x / u) * u;
      return { cons: 'Redondeá <b>' + fmt(x) + '</b> a los <b>' + POSD[i][0] + '</b>.', campos: [{ v: r2(r) }], ayuda: 'Mirá la cifra que sigue a los ' + POSD[i][0] + ': si es 5 o más, sube; si es menos de 5, queda igual.', bien: '¡Bien! ' + fmt(x) + ' ≈ ' + fmt(r2(r)) + '.' }; });
  } };
  M.sexagesimal = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('s', 'Segundos', 60, 20000, 1, 7384), function (o) { var h = Math.floor(o.s / 3600), m = Math.floor(o.s % 3600 / 60), s = o.s % 60;
      return '<p class="lb-nota">Se agrupa de a 60: 60 segundos forman 1 minuto y 60 minutos forman 1 hora.</p><p class="lb-nota">' + fmt(o.s) + ' s ÷ 60 = ' + Math.floor(o.s / 60) + ' min y sobran ' + s + ' s · ' + Math.floor(o.s / 60) + ' min ÷ 60 = ' + h + ' h y sobran ' + m + ' min.</p><p class="lb-res">' + fmt(o.s) + ' s = ' + h + ' h ' + m + ' min ' + s + ' s</p>'; });
  } };
  M.sexagesimal_conv = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { if (Math.random() < .5) { var t = R(3700, 30000), h = Math.floor(t / 3600), m = Math.floor(t % 3600 / 60), s = t % 60;
        return { cons: 'Pasá <b>' + fmt(t) + ' segundos</b> a horas, minutos y segundos.', campos: [{ lab: 'h', v: h }, { lab: 'min', v: m }, { lab: 's', v: s }], ayuda: 'Dividí por 60 para pasar a minutos (lo que sobra son segundos) y otra vez por 60 para pasar a horas.', bien: '¡Bien! ' + h + ' h ' + m + ' min ' + s + ' s.' }; }
      var h1 = R(0, 3), m1 = R(10, 59), s1 = R(10, 59), h2 = R(0, 3), m2 = R(10, 59), s2 = R(10, 59), T = (h1 + h2) * 3600 + (m1 + m2) * 60 + s1 + s2;
      return { cons: 'Sumá: <b>' + h1 + ' h ' + m1 + ' min ' + s1 + ' s</b> + <b>' + h2 + ' h ' + m2 + ' min ' + s2 + ' s</b>.', campos: [{ lab: 'h', v: Math.floor(T / 3600) }, { lab: 'min', v: Math.floor(T % 3600 / 60) }, { lab: 's', v: T % 60 }], ayuda: 'Sumá cada columna; si los segundos o minutos pasan de 60, cambiá 60 por 1 de la columna de al lado.', bien: '¡Bien sumado!' }; });
  } };
  M.binario_lamparas = { tipo: 'ejemplo', render: function (el) {
    var on = [0, 0, 1, 0, 1, 1, 0, 1];
    function pintar() { var v = 0; on.forEach(function (b, i) { if (b) v += Math.pow(2, 7 - i); });
      el.innerHTML = '<p class="lb-ayuda">Tocá las lámparas para prenderlas (1) o apagarlas (0).</p><div class="lb2-lamps">' + on.map(function (b, i) { return '<button type="button" class="lb2-lamp' + (b ? ' on' : '') + '" data-l="' + i + '"><i>' + (b ? '💡' : '○') + '</i><b>' + b + '</b><small>' + Math.pow(2, 7 - i) + '</small></button>'; }).join('') + '</div>' +
        '<p class="lb-nota">Cada lugar vale el doble que el de su derecha. Sumamos los prendidos: ' + (on.map(function (b, i) { return b ? Math.pow(2, 7 - i) : null; }).filter(function (x) { return x !== null; }).join(' + ') || '0') + '.</p><p class="lb-res">' + on.join('') + ' (binario) = ' + v + ' (decimal)</p>'; }
    el.onclick = function (e) { var b = e.target.closest('[data-l]'); if (b) { var i = +b.getAttribute('data-l'); on[i] = on[i] ? 0 : 1; pintar(); } }; pintar();
  } };
  M.binario_conv = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var n = R(5, 200), b = n.toString(2);
      if (Math.random() < .5) return { cons: 'Pasá a decimal el número binario <b>' + b + '</b>.', campos: [{ v: n }], ayuda: 'Cada lugar desde la derecha vale 1, 2, 4, 8, 16…: sumá los que tienen 1.', bien: '¡Bien! ' + b + ' = ' + n + '.' };
      return { cons: 'Pasá a binario el número <b>' + n + '</b>.', campos: [{ tipo: 'texto', v: b }], ayuda: 'Dividí por 2 una y otra vez y leé los restos de abajo hacia arriba. Es ' + b + '.', bien: '¡Bien! ' + n + ' = ' + b + '.' }; });
  } };
  M.recta_explorar = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('x', 'Número', -10, 10, 1, -4), function (o) { var X = function (v) { return 130 + v * 11; }, t = '';
      for (var k = -10; k <= 10; k++) t += '<line class="rayo" x1="' + X(k) + '" y1="' + (k ? 32 : 26) + '" x2="' + X(k) + '" y2="' + (k ? 40 : 46) + '"/>';
      return '<svg viewBox="0 0 260 70" class="lb2-svg"><line class="rayo" x1="5" y1="36" x2="255" y2="36"/>' + t + '<text x="130" y="62">0</text><circle cx="' + X(o.x) + '" cy="36" r="6" class="pt"/><circle cx="' + X(-o.x) + '" cy="36" r="5" class="pt2"/></svg>' +
        '<p class="lb-nota">El opuesto de ' + sig(o.x) + ' es ' + sig(-o.x) + ' (mismo lugar del otro lado del 0). El valor absoluto es la distancia al 0.</p><p class="lb-res">|' + sig(o.x) + '| = ' + Math.abs(o.x) + '</p>'; });
  } };
  M.signos = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('a', 'Primer factor', -9, 9, 1, -3) + ctrl('b', 'Segundo factor', -9, 9, 1, 4), function (o) { var a = o.a, b = o.b, s = a * b;
      return '<table class="lb2-tab"><tr><th>×</th><th>+</th><th>−</th></tr><tr><th>+</th><td class="' + (a > 0 && b > 0 ? 'on' : '') + '">+</td><td class="' + (a > 0 && b < 0 ? 'on' : '') + '">−</td></tr><tr><th>−</th><td class="' + (a < 0 && b > 0 ? 'on' : '') + '">−</td><td class="' + (a < 0 && b < 0 ? 'on' : '') + '">+</td></tr></table>' +
        '<p class="lb-nota">Signos iguales dan +; signos distintos dan −. Para dividir vale la misma regla.</p><p class="lb-res">(' + sig(a) + ') × (' + sig(b) + ') = ' + sig(s) + (b && a % b === 0 ? ' · (' + sig(a) + ') ÷ (' + sig(b) + ') = ' + sig(a / b) : '') + '</p>'; });
  } };
  M.potencias_explorar = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('b', 'Base', -6, 10, 1, -2) + ctrl('e', 'Exponente', 0, 6, 1, 3), function (o) { var b = o.b, e = o.e, v = Math.pow(b, e), bs = b < 0 ? '(' + sig(b) + ')' : b;
      return '<p class="lb-res">' + bs + '<sup>' + e + '</sup> = ' + (e === 0 ? '1' : Array(e + 1).join(bs + ' · ').slice(0, -3) + ' = ' + fmt(v)) + '</p><p class="lb-nota">' + (e === 0 ? 'Todo número (distinto de 0) elevado a 0 da 1.' : e === 1 ? 'Elevado a 1 da la misma base.' : 'El exponente dice cuántas veces se multiplica la base.') + (b < 0 && e > 0 ? ' Base negativa: exponente ' + (e % 2 ? 'impar → resultado negativo.' : 'par → resultado positivo.') : '') + '</p>'; });
  } };
  M.raiz_explorar = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('n', 'Número', 1, 200, 1, 49), function (o) { var n = o.n, k = Math.floor(Math.sqrt(n)), exacta = k * k === n, s = Math.min(10, 140 / Math.max(k, 1)), g = '';
      for (var i = 0; i < k; i++) for (var j = 0; j < k; j++) g += '<rect x="' + (5 + i * s) + '" y="' + (5 + j * s) + '" width="' + s + '" height="' + s + '" class="c1"/>';
      return '<svg viewBox="0 0 ' + (10 + k * s) + ' ' + (10 + k * s) + '" class="lb2-svg" style="max-height:150px">' + g + '</svg>' + (exacta ? '<p class="lb-res">√' + n + ' = ' + k + ' (porque ' + k + ' × ' + k + ' = ' + n + ')</p><p class="lb-nota">' + n + ' es un cuadrado perfecto: con ' + n + ' cuadraditos se arma un cuadrado de lado ' + k + '.</p>'
        : '<p class="lb-res">√' + n + ' está entre ' + k + ' y ' + (k + 1) + '</p><p class="lb-nota">' + k * k + ' < ' + n + ' < ' + (k + 1) * (k + 1) + ': con ' + n + ' cuadraditos no se arma un cuadrado justo (el más grande es de lado ' + k + ').</p>'); });
  } };
  M.proporcionalidad = { tipo: 'ejemplo', render: function (el, p) {
    var inv = p.modo === 'inversa';
    escena(el, ctrl('k', inv ? 'Producto constante' : 'Constante k', inv ? 12 : 1, inv ? 60 : 8, inv ? 12 : 1, inv ? 24 : 3), function (o) { var xs = [1, 2, 3, 4, 6], k = o.k, ys = xs.map(function (x) { return inv ? r2(k / x) : k * x; }), W = 230, Hh = 140, my = Math.max.apply(null, ys);
      var pts = xs.map(function (x, i) { return (20 + x * 32) + ',' + (Hh - 10 - ys[i] / my * (Hh - 30)).toFixed(1); });
      return '<table class="lb2-tab"><tr><th>x</th>' + xs.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr><th>y</th>' + ys.map(function (y) { return '<td>' + fmt(y) + '</td>'; }).join('') + '</tr></table>' +
        '<svg viewBox="0 0 ' + W + ' ' + Hh + '" class="lb2-svg"><line class="rayo" x1="20" y1="' + (Hh - 10) + '" x2="' + (W - 5) + '" y2="' + (Hh - 10) + '"/><line class="rayo" x1="20" y1="5" x2="20" y2="' + (Hh - 10) + '"/><polyline class="graf" points="' + (inv ? '' : '20,' + (Hh - 10) + ' ') + pts.join(' ') + '"/>' + pts.map(function (q) { return '<circle r="4" class="pt" cx="' + q.split(',')[0] + '" cy="' + q.split(',')[1] + '"/>'; }).join('') + '</svg>' +
        '<p class="lb-nota">' + (inv ? 'Inversa: si x se duplica, y se reduce a la mitad. Siempre x · y = ' + k + '.' : 'Directa: si x se duplica, y también. Siempre y ÷ x = ' + k + ' (la constante): y = ' + k + 'x.') + '</p>'; });
  } };
  M.regla_de_tres = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var inv = p.modo === 'inversa' || (p.modo !== 'directa' && Math.random() < .35);
      if (inv) { var ob = R(2, 6), dias = R(2, 6) * 6, ob2 = pick([2, 3, 4, 6, 8, 12].filter(function (x) { return x !== ob && (ob * dias) % x === 0; })) || ob * 2;
        return { cons: '<b>' + ob + ' obreros</b> tardan <b>' + dias + ' días</b> en hacer una obra. ¿Cuántos días tardan <b>' + ob2 + ' obreros</b> (al mismo ritmo)?', campos: [{ v: ob * dias / ob2, un: 'días' }], ayuda: 'Es inversa: más obreros, menos días. ' + ob + ' × ' + dias + ' = ' + ob * dias + ' días-obrero; dividí por ' + ob2 + '.', bien: '¡Bien! ' + ob + ' × ' + dias + ' ÷ ' + ob2 + ' = ' + ob * dias / ob2 + ' días.' }; }
      var a = R(2, 8), pr = R(3, 40) * 50, c = R(2, 15);
      return { cons: 'Si <b>' + a + ' kg</b> cuestan <b>$' + fmt(pr) + '</b>, ¿cuánto cuestan <b>' + c + ' kg</b>?', campos: [{ v: r2(pr * c / a), un: '$' }], ayuda: 'Es directa. Dato: ' + a + ' → ' + fmt(pr) + '. Pregunta: ' + c + ' → x. x = ' + c + ' × ' + fmt(pr) + ' ÷ ' + a + '.', bien: '¡Bien! $' + fmt(r2(pr * c / a)) + '.' }; });
  } };

  // ======================= FUNCIONES =======================
  function plano(r, extra) { var s = 14, c = 10 + r * s, g = ''; for (var k = -r; k <= r; k++) g += '<line class="grid' + (k ? '' : ' eje') + '" x1="' + (c + k * s) + '" y1="10" x2="' + (c + k * s) + '" y2="' + (2 * c - 10) + '"/><line class="grid' + (k ? '' : ' eje') + '" x1="10" y1="' + (c + k * s) + '" x2="' + (2 * c - 10) + '" y2="' + (c + k * s) + '"/>';
    return { s: s, c: c, svg: '<svg viewBox="0 0 ' + 2 * c + ' ' + 2 * c + '" class="lb2-svg lb2-plano">' + g + (extra || '') + '</svg>' }; }
  M.plano = { tipo: 'ejemplo', render: function (el) {
    var x = R(-5, 5), y = R(-5, 5);
    function pintar() { var P = plano(6), cx = P.c + x * P.s, cy = P.c - y * P.s, celdas = ''; for (var i = -6; i <= 6; i++) for (var j = -6; j <= 6; j++) celdas += '<circle class="hit" r="6" cx="' + (P.c + i * P.s) + '" cy="' + (P.c - j * P.s) + '" data-x="' + i + '" data-y="' + j + '"/>';
      el.innerHTML = '<p class="lb-ayuda">Tocá cualquier punto del plano.</p>' + P.svg.replace('</svg>', '<line class="diag" x1="' + cx + '" y1="' + cy + '" x2="' + cx + '" y2="' + P.c + '"/><line class="diag" x1="' + cx + '" y1="' + cy + '" x2="' + P.c + '" y2="' + cy + '"/><circle class="pt" r="6" cx="' + cx + '" cy="' + cy + '"/>' + celdas + '</svg>') +
        '<p class="lb-res">P = (' + x + ', ' + y + ')</p><p class="lb-nota">Primero se lee x (cuánto a la derecha o izquierda) y después y (cuánto arriba o abajo). ' + (x && y ? 'Está en el ' + (x > 0 ? (y > 0 ? 'primer' : 'cuarto') : (y > 0 ? 'segundo' : 'tercer')) + ' cuadrante.' : 'Está sobre un eje.') + '</p>'; }
    el.onclick = function (e) { var h = e.target.closest('[data-x]'); if (h) { x = +h.getAttribute('data-x'); y = +h.getAttribute('data-y'); pintar(); } }; pintar();
  } };
  M.funcion_lineal = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('a', 'Pendiente a', -3, 3, 1, 2) + ctrl('b', 'Ordenada b', -4, 4, 1, 1), function (o) { var P = plano(6), xs = [-2, -1, 0, 1, 2], f = function (x) { return o.a * x + o.b; };
      var lin = '<line class="graf" x1="' + (P.c - 6 * P.s) + '" y1="' + (P.c - f(-6) * P.s) + '" x2="' + (P.c + 6 * P.s) + '" y2="' + (P.c - f(6) * P.s) + '"/>' + xs.map(function (x) { return '<circle class="pt" r="4" cx="' + (P.c + x * P.s) + '" cy="' + (P.c - f(x) * P.s) + '"/>'; }).join('');
      return '<p class="lb-res">y = ' + (o.a === 1 ? '' : o.a === -1 ? '−' : o.a) + (o.a ? 'x' : '') + (o.b ? (o.b > 0 ? (o.a ? ' + ' : '') + o.b : ' − ' + -o.b) : (o.a ? '' : '0')) + '</p><table class="lb2-tab"><tr><th>x</th>' + xs.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr><th>y</th>' + xs.map(function (x) { return '<td>' + f(x) + '</td>'; }).join('') + '</tr></table>' +
        '<div style="max-width:260px;margin:auto">' + P.svg.replace('</svg>', '<g style="clip-path:inset(0)">' + lin + '</g></svg>') + '</div><p class="lb-nota">b es donde corta al eje y; a es cuánto sube (o baja) la recta por cada paso a la derecha. ' + (o.a > 0 ? 'Creciente.' : o.a < 0 ? 'Decreciente.' : 'Constante.') + '</p>'; });
  } };
  M.coordenadas = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var x = R(-5, 5), y = R(-5, 5), P = plano(6);
      return { cons: '¿Cuáles son las coordenadas del punto <b>A</b>?', html: '<div style="max-width:260px;margin:auto">' + P.svg.replace('</svg>', '<circle class="pt" r="6" cx="' + (P.c + x * P.s) + '" cy="' + (P.c - y * P.s) + '"/><text class="ptx" x="' + (P.c + x * P.s + 8) + '" y="' + (P.c - y * P.s - 8) + '">A</text></svg>') + '</div>', campos: [{ lab: 'x =', v: x }, { lab: 'y =', v: y }], ayuda: 'Primero contá cuánto se corre en x desde el 0 (a la derecha +, a la izquierda −) y después en y (arriba +, abajo −).', bien: '¡Bien! A = (' + x + ', ' + y + ').' }; });
  } };
  M.funcion_tabla = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = R(-3, 4) || 2, b = R(-5, 5), xs = mezclar([-2, -1, 0, 1, 2, 3]).slice(0, 3).sort(function (m, n) { return m - n; }), txt = 'y = ' + (a === 1 ? '' : a === -1 ? '−' : a) + 'x' + (b ? (b > 0 ? ' + ' + b : ' − ' + -b) : '');
      return { cons: 'Completá la tabla de <b>' + txt + '</b>.', campos: xs.map(function (x) { return { lab: 'x = ' + x + ' → y =', v: a * x + b }; }), ayuda: 'Reemplazá cada x en la fórmula: y = ' + a + ' · x ' + (b < 0 ? '− ' + -b : '+ ' + b) + '.', bien: '¡Tabla completa!' }; });
  } };

  // ======================= ESTADÍSTICA Y PROBABILIDAD =======================
  var CATS = [['Fútbol', 'Vóley', 'Básquet', 'Natación'], ['Perro', 'Gato', 'Pez', 'Ninguna'], ['Rojo', 'Azul', 'Verde', 'Amarillo'], ['Pizza', 'Empanadas', 'Milanesa', 'Pastas']];
  function datos() { var cs = pick(CATS), n = pick([10, 20, 20, 25]), L = []; for (var i = 0; i < n; i++) L.push(cs[Math.min(cs.length - 1, Math.floor(Math.pow(Math.random(), 1.4) * cs.length))]); return { cs: cs, L: L }; }
  M.frecuencias = { tipo: 'ejemplo', render: function (el) {
    var D = datos();
    function pintar() { var f = D.cs.map(function (c) { return D.L.filter(function (x) { return x === c; }).length; }), n = D.L.length, mx = Math.max.apply(null, f);
      el.innerHTML = '<p class="lb-nota">Datos (' + n + ' respuestas): ' + D.L.join(', ') + '.</p><table class="lb2-tab"><tr><th>Valor</th><th>Frecuencia</th><th>%</th><th></th></tr>' + D.cs.map(function (c, i) { return '<tr><td>' + c + '</td><td>' + f[i] + '</td><td>' + fmt(r2(f[i] / n * 100)) + ' %</td><td class="lb2-bar"><i style="width:' + (mx ? f[i] / mx * 100 : 0) + '%"></i></td></tr>'; }).join('') + '<tr><th>Total</th><th>' + n + '</th><th>100 %</th><th></th></tr></table>' +
        '<p class="lb-nota">La frecuencia es cuántas veces aparece cada valor; el porcentaje es la frecuencia ÷ total × 100. Las frecuencias suman el total.</p><div class="lb-pie"><button type="button" class="lb-btn suave" data-o="1">🔄 Otros datos</button></div>'; }
    el.onclick = function (e) { if (e.target.closest('[data-o]')) { D = datos(); pintar(); } }; pintar();
  } };
  M.tabla_frecuencias = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var D = datos(), f = D.cs.map(function (c) { return D.L.filter(function (x) { return x === c; }).length; });
      return { cons: 'Contá los datos y completá la frecuencia de cada valor.', html: '<p class="lb-nota">' + D.L.join(', ') + '.</p>', campos: D.cs.map(function (c, i) { return { lab: c + ':', v: f[i] }; }), ayuda: 'Contá cuántas veces aparece cada uno. Control: tienen que sumar ' + D.L.length + '.', bien: '¡Bien contado! Suman ' + D.L.length + '.' }; });
  } };
  function stats(L) { var s = L.slice().sort(function (a, b) { return a - b; }), n = s.length, media = L.reduce(function (a, b) { return a + b; }, 0) / n, med = n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2, c = {}, mx = 0;
    L.forEach(function (x) { c[x] = (c[x] || 0) + 1; mx = Math.max(mx, c[x]); }); var moda = Object.keys(c).filter(function (k) { return c[k] === mx; }).map(Number); return { media: media, med: med, moda: mx > 1 ? moda : [], s: s }; }
  M.medidas = { tipo: 'ejemplo', render: function (el) {
    var L = [6, 8, 7, 8, 9, 4];
    escena(el, L.map(function (x, i) { return ctrl('d' + i, 'Dato ' + (i + 1), 0, 10, 1, x); }).join(''), function (o) { var D = [0, 1, 2, 3, 4, 5].map(function (i) { return o['d' + i]; }), S = stats(D), pts = '', cnt = {};
      D.forEach(function (x) { cnt[x] = (cnt[x] || 0) + 1; pts += '<circle class="pt" r="6" cx="' + (15 + x * 22) + '" cy="' + (60 - (cnt[x] - 1) * 13) + '"/>'; });
      return '<svg viewBox="0 0 250 95" class="lb2-svg"><line class="rayo" x1="10" y1="70" x2="240" y2="70"/>' + [0, 2, 4, 6, 8, 10].map(function (k) { return '<text x="' + (15 + k * 22) + '" y="88">' + k + '</text>'; }).join('') + '<line class="graf" x1="' + (15 + S.media * 22) + '" y1="5" x2="' + (15 + S.media * 22) + '" y2="72"/>' + pts + '</svg>' +
        '<p class="lb-res">Media = ' + fmt(r2(S.media)) + ' · Mediana = ' + fmt(S.med) + ' · Moda = ' + (S.moda.length ? S.moda.join(' y ') : 'no hay') + '</p><p class="lb-nota">Media: suma ' + D.join(' + ') + ' = ' + D.reduce(function (a, b) { return a + b; }, 0) + ', dividido 6. Mediana: el del medio de los datos ordenados (' + S.s.join(', ') + '). Moda: el que más se repite. Probá llevar un dato a 0: la media se mueve mucho más que la mediana.</p>'; });
  } };
  M.media_moda_mediana = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var que = p.que || pick(['media', 'moda', 'mediana']), L, S, t = 0;
      do { L = []; var n = que === 'mediana' ? pick([5, 7]) : R(5, 7); for (var i = 0; i < n; i++) L.push(R(2, 10)); S = stats(L); } while (t++ < 200 && ((que === 'media' && S.media % 1) || (que === 'moda' && S.moda.length !== 1)));
      var v = que === 'media' ? S.media : que === 'moda' ? S.moda[0] : S.med;
      return { cons: 'Datos: <b>' + L.join(', ') + '</b>. ¿Cuál es la <b>' + que + '</b>?', campos: [{ v: v }], ayuda: que === 'media' ? 'Sumá todos los datos (' + L.reduce(function (a, b) { return a + b; }, 0) + ') y dividí por la cantidad (' + L.length + ').' : que === 'moda' ? 'Es el dato que más veces aparece.' : 'Ordená los datos (' + S.s.join(', ') + ') y tomá el del medio.', bien: '¡Bien! La ' + que + ' es ' + fmt(v) + '.' }; });
  } };
  M.barras_armar = { tipo: 'ejercicio', render: function (el, p, api) {
    H.ejercicio(el, api, 'Armá el <b>gráfico de barras</b> de la tabla: usá + y − para que cada barra llegue a su frecuencia.', function (c) {
      var D = datos(), f = D.cs.map(function (x) { return D.L.filter(function (y) { return y === x; }).length; }), h = D.cs.map(function () { return 0; }), mx = Math.max.apply(null, f) + 2;
      function pintar() { c.innerHTML = '<table class="lb2-tab"><tr>' + D.cs.map(function (x) { return '<th>' + x + '</th>'; }).join('') + '</tr><tr>' + f.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr></table><div class="lb2-graf">' +
        D.cs.map(function (x, i) { return '<div class="lb2-col"><div class="lb2-colb"><i style="height:' + h[i] / mx * 100 + '%"></i><span>' + h[i] + '</span></div><b>' + x + '</b><div><button type="button" class="lb-btn suave chico" data-m="' + i + '">−</button><button type="button" class="lb-btn chico" data-p="' + i + '">+</button></div></div>'; }).join('') + '</div>'; }
      c.addEventListener('click', function (e) { var a = e.target.closest('[data-p]'), b = e.target.closest('[data-m]'); if (a) { h[+a.getAttribute('data-p')] = Math.min(mx, h[+a.getAttribute('data-p')] + 1); pintar(); } if (b) { h[+b.getAttribute('data-m')] = Math.max(0, h[+b.getAttribute('data-m')] - 1); pintar(); } });
      pintar();
      return { comprobar: function () { var mal = D.cs.filter(function (x, i) { return h[i] !== f[i]; }); return mal.length ? { ok: false, msg: 'Revisá ' + mal.join(', ') + ': cada barra tiene que llegar justo a su frecuencia.' } : { ok: true, msg: '¡Gráfico bien armado!' }; },
        resolver: function () { f.forEach(function (x, i) { h[i] = x; }); pintar(); } };
    });
  } };
  M.urna = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('r', 'Bolitas rojas', 0, 8, 1, 3) + ctrl('a', 'Bolitas azules', 0, 8, 1, 2) + ctrl('v', 'Bolitas verdes', 0, 8, 1, 5), function (o) { var t = o.r + o.a + o.v; if (!t) return '<p class="lb-ayuda">Poné al menos una bolita.</p>';
      var bol = '', cols = [['r', '#253638', 'roja'], ['a', '#087E83', 'azul'], ['v', '#7FD3C4', 'verde']]; cols.forEach(function (q) { for (var i = 0; i < o[q[0]]; i++) bol += '<i style="background:' + q[1] + '"></i>'; });
      return '<div class="lb2-urna">' + bol + '</div><table class="lb2-tab"><tr><th>Sacar</th><th>Probabilidad</th><th>Decimal</th><th>%</th></tr>' + cols.map(function (q) { return '<tr><td>' + q[2] + '</td><td>' + o[q[0]] + '/' + t + (mcd(o[q[0]], t) > 1 && o[q[0]] ? ' = ' + frs(o[q[0]], t) : '') + '</td><td>' + fmt(r2(o[q[0]] / t)) + '</td><td>' + fmt(r2(o[q[0]] / t * 100)) + ' %</td></tr>'; }).join('') + '</table>' +
        '<p class="lb-nota">Probabilidad = casos favorables ÷ casos posibles (' + t + ' bolitas). Las tres suman 1.</p><div class="lb-pie"><button type="button" class="lb-btn suave" data-sim="1">Sacar 100 veces (con reposición)</button></div><div class="lb2-sim"></div>'; },
      '');
    el.addEventListener('click', function (e) { if (!e.target.closest('[data-sim]')) return; var g = function (k) { return num(el.querySelector('[data-k="' + k + '"]').value); }, r = g('r'), a = g('a'), v = g('v'), t = r + a + v, c = [0, 0, 0];
      for (var i = 0; i < 100; i++) { var x = Math.random() * t; c[x < r ? 0 : x < r + a ? 1 : 2]++; }
      el.querySelector('.lb2-sim').innerHTML = '<p class="lb-nota">Salieron: roja ' + c[0] + ', azul ' + c[1] + ', verde ' + c[2] + ' de 100. Con muchas repeticiones, la frecuencia se acerca a la probabilidad (' + fmt(r2(r / t * 100)) + ' %, ' + fmt(r2(a / t * 100)) + ' %, ' + fmt(r2(v / t * 100)) + ' %).</p>'; });
  } };
  M.probabilidad = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { if (Math.random() < .4) { var ev = pick([['un número par', 3], ['un número mayor que 4', 2], ['un múltiplo de 3', 2], ['un número menor que 3', 2], ['un 6', 1]]);
        return { cons: 'Tirás un dado. ¿Cuál es la probabilidad de sacar <b>' + ev[0] + '</b>? (Fracción.)', campos: [{ tipo: 'frac', v: ev[1] / 6, n: ev[1], d: 6 }], ayuda: 'Casos posibles: 6. Contá los favorables.', bien: '¡Bien! ' + ev[1] + '/6' + (mcd(ev[1], 6) > 1 ? ' = ' + frs(ev[1], 6) : '') + '.' }; }
      var r = R(1, 7), a = R(1, 7), v = R(1, 7), t = r + a + v, q = pick([['roja', r], ['azul', a], ['verde', v]]);
      return { cons: 'En una bolsa hay <b>' + r + ' rojas, ' + a + ' azules y ' + v + ' verdes</b>. Sacás una sin mirar. ¿Cuál es la probabilidad de que sea <b>' + q[0] + '</b>? (Fracción.)', campos: [{ tipo: 'frac', v: q[1] / t, n: q[1], d: t }], ayuda: 'Favorables: las ' + q[0] + 's (' + q[1] + '). Posibles: todas (' + t + ').', bien: '¡Bien! ' + q[1] + '/' + t + '.' }; });
  } };
  M.combinaciones_tabla = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('a', 'Remeras', 1, 5, 1, 3) + ctrl('b', 'Gorras', 1, 5, 1, 2), function (o) { var R1 = ['Roja', 'Azul', 'Verde', 'Negra', 'Blanca'], G = ['🧢A', '🧢B', '🧢C', '🧢D', '🧢E'];
      return '<table class="lb2-tab"><tr><th></th>' + G.slice(0, o.b).map(function (g) { return '<th>' + g + '</th>'; }).join('') + '</tr>' + R1.slice(0, o.a).map(function (r) { return '<tr><th>' + r + '</th>' + G.slice(0, o.b).map(function () { return '<td class="on">✔</td>'; }).join('') + '</tr>'; }).join('') + '</table><p class="lb-nota">Cada casilla es una combinación distinta: no se olvida ninguna.</p><p class="lb-res">' + o.a + ' × ' + o.b + ' = ' + o.a * o.b + ' combinaciones</p>'; });
  } };
  M.combinaciones = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = R(2, 6), b = R(2, 5), c = Math.random() < .4 ? R(2, 4) : 0;
      return { cons: 'Hay <b>' + a + ' entradas</b>, <b>' + b + ' platos principales</b>' + (c ? ' y <b>' + c + ' postres</b>' : '') + '. ¿Cuántos menús distintos se pueden armar eligiendo uno de cada uno?', campos: [{ v: a * b * (c || 1) }], ayuda: 'Por cada entrada hay ' + b + ' platos' + (c ? ', y por cada combinación ' + c + ' postres' : '') + ': se multiplica.', bien: '¡Bien! ' + a + ' × ' + b + (c ? ' × ' + c : '') + ' = ' + a * b * (c || 1) + '.' }; });
  } };

  // ======================= MÁS: problemas, razones, álgebra de 2.º año =======================
  M.mcd_mcm_problemas = { tipo: 'ejercicio', render: function (el, p, api) {
    var PB = [['Cortar cintas de 18 y 24 cm en trozos iguales lo más largos posible', 0], ['Armar bolsitas iguales con 30 caramelos y 45 chupetines sin que sobre nada', 0], ['Embaldosar un patio de 12 × 20 con baldosas cuadradas lo más grandes posible', 0], ['Repartir 16 lápices y 40 gomas en la mayor cantidad de cajas iguales', 0],
      ['Dos colectivos salen juntos, uno cada 12 minutos y otro cada 18: ¿cuándo vuelven a coincidir?', 1], ['Dos luces titilan cada 4 y cada 6 segundos: ¿cuándo prenden juntas otra vez?', 1], ['El menor número de alumnos que se pueden agrupar de a 3, de a 4 o de a 5 sin que sobre nadie', 1], ['Juan va al club cada 6 días y Sofía cada 8: ¿cuándo se encuentran de nuevo?', 1]];
    cajas(el, api, function () { var S = mezclar(PB).slice(0, 6); return { tit: '¿Se resuelve con el <b>MCD</b> o con el <b>MCM</b>? Pensá si la respuesta tiene que dividir a los datos (más chica) o ser múltiplo de ellos (más grande).', cajas: ['MCD (divide a los datos)', 'MCM (múltiplo de los datos)'], items: S.map(function (x, i) { return { v: 'p' + i, t: x[0], c: x[1] }; }) }; });
  } };
  M.fraccion_cantidad = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('t', 'Total', 12, 120, 12, 60) + ctrl('a', 'Primero uso', 1, 3, 1, 1) + ctrl('b', 'de', 2, 6, 1, 3) + ctrl('c', 'Después uso', 1, 3, 1, 1) + ctrl('d', 'del resto, de', 2, 6, 1, 4), function (o) {
      var a = Math.min(o.a, o.b - 1), c = Math.min(o.c, o.d - 1), u1 = o.t * a / o.b, resto = o.t - u1, u2 = resto * c / o.d, fin = resto - u2;
      return '<div class="lb2-barra3"><i style="width:' + (u1 / o.t * 100) + '%" class="x1"></i><i style="width:' + (u2 / o.t * 100) + '%" class="x2"></i><i style="width:' + (fin / o.t * 100) + '%" class="x3"></i></div>' +
        '<p class="lb-nota">Primero: ' + fr(a, o.b) + ' de ' + o.t + ' = ' + fmt(r2(u1)) + '. Queda ' + fmt(r2(resto)) + '. Después: ' + fr(c, o.d) + ' <b>del resto</b> = ' + fmt(r2(u2)) + '. Ojo: es del resto, no del total.</p><p class="lb-res">Queda ' + fmt(r2(fin)) + ' de ' + o.t + '</p>'; });
  } };
  M.fraccion_cantidad_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var b = pick([2, 3, 4, 5]), d = pick([2, 3, 4]), a = R(1, b - 1), c = R(1, d - 1), t = b * d * R(2, 10), u1 = t * a / b, rest = t - u1, u2 = rest * c / d;
      return { cons: 'De <b>' + t + '</b> se usa ' + fr(a, b) + ' el lunes y ' + fr(c, d) + ' <b>del resto</b> el martes. ¿Cuánto queda?', campos: [{ v: rest - u2 }], ayuda: 'Lunes: ' + fr(a, b) + ' de ' + t + ' = ' + u1 + '; queda ' + rest + '. Martes: ' + fr(c, d) + ' de ' + rest + ' = ' + u2 + '.', bien: '¡Bien! Quedan ' + (rest - u2) + '.' }; });
  } };
  M.escala = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('n', 'Escala 1 :', 1000, 100000, 1000, 50000) + ctrl('m', 'Medida en el mapa (cm)', 1, 20, 1, 6), function (o) { var real = o.n * o.m;
      return '<div class="lb2-mapa"><i style="width:' + o.m * 4.5 + '%"></i><span>' + o.m + ' cm</span></div><p class="lb-nota">1 cm en el mapa representa ' + fmt(o.n) + ' cm reales. Del mapa a la realidad se <b>multiplica</b> por la escala; de la realidad al mapa se <b>divide</b>.</p><p class="lb-res">' + o.m + ' cm × ' + fmt(o.n) + ' = ' + fmt(real) + ' cm = ' + fmt(real / 100) + ' m = ' + fmt(real / 100000) + ' km</p>'; });
  } };
  M.escala_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var n = pick([10000, 20000, 25000, 50000, 100000]), m = R(2, 15), km = n * m / 100000;
      if (Math.random() < .5) return { cons: 'En un mapa de escala <b>1 : ' + fmt(n) + '</b>, dos pueblos están a <b>' + m + ' cm</b>. ¿A cuántos <b>km</b> están en la realidad?', campos: [{ v: km, un: 'km' }], ayuda: m + ' × ' + fmt(n) + ' = ' + fmt(n * m) + ' cm; para pasar a km dividí por 100.000.', bien: '¡Bien! ' + fmt(km) + ' km.' };
      return { cons: 'Con escala <b>1 : ' + fmt(n) + '</b>, ¿cuántos <b>cm</b> mide en el mapa una distancia real de <b>' + fmt(km) + ' km</b>?', campos: [{ v: m, un: 'cm' }], ayuda: 'Pasá ' + fmt(km) + ' km a cm (× 100.000) y dividí por ' + fmt(n) + '.', bien: '¡Bien! ' + m + ' cm.' }; });
  } };
  M.velocidad = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('d', 'Distancia (km)', 10, 600, 10, 240) + ctrl('t', 'Tiempo (h)', 1, 10, 1, 3), function (o) { var v = o.d / o.t;
      return '<div class="lb2-ruta"><span style="left:' + Math.min(92, o.d / 6.5) + '%">🚗</span></div><p class="lb-nota">La velocidad es la razón distancia ÷ tiempo: cuántos km recorre en cada hora. Despejando: d = v · t y t = d ÷ v. Para pasar de km/h a m/s se divide por 3,6.</p><p class="lb-res">v = ' + o.d + ' ÷ ' + o.t + ' = ' + fmt(r2(v)) + ' km/h ≈ ' + fmt(r2(v / 3.6)) + ' m/s</p>'; });
  } };
  M.velocidad_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var v = R(4, 24) * 5, t = R(2, 8), d = v * t, q = pick(['v', 'd', 't']);
      if (q === 'v') return { cons: 'Un auto recorre <b>' + d + ' km</b> en <b>' + t + ' h</b>. ¿Cuál es su velocidad?', campos: [{ v: v, un: 'km/h' }], ayuda: 'v = d ÷ t.', bien: '¡Bien! ' + v + ' km/h.' };
      if (q === 'd') return { cons: 'Un tren va a <b>' + v + ' km/h</b> durante <b>' + t + ' h</b>. ¿Cuántos km recorre?', campos: [{ v: d, un: 'km' }], ayuda: 'd = v · t.', bien: '¡Bien! ' + d + ' km.' };
      return { cons: 'Un micro recorre <b>' + d + ' km</b> a <b>' + v + ' km/h</b>. ¿Cuántas horas tarda?', campos: [{ v: t, un: 'h' }], ayuda: 't = d ÷ v.', bien: '¡Bien! ' + t + ' h.' }; });
  } };
  M.regla_tres_compuesta = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var ob = R(2, 6), h = R(2, 8), m = ob * h * R(3, 12), ob2 = R(2, 9), h2 = R(2, 9), m2 = m / (ob * h) * ob2 * h2;
      return { cons: '<b>' + ob + ' pintores</b> trabajando <b>' + h + ' horas</b> pintan <b>' + m + ' m²</b>. ¿Cuántos m² pintan <b>' + ob2 + ' pintores</b> en <b>' + h2 + ' horas</b>?', html: '<table class="lb2-tab"><tr><th>Pintores</th><th>Horas</th><th>m²</th></tr><tr><td>' + ob + '</td><td>' + h + '</td><td>' + m + '</td></tr><tr><td>' + ob2 + '</td><td>' + h2 + '</td><td>x</td></tr></table>', campos: [{ v: m2, un: 'm²' }], ayuda: 'Las dos magnitudes son directas con los m²: x = ' + m + ' × ' + ob2 + '/' + ob + ' × ' + h2 + '/' + h + '.', bien: '¡Bien! ' + fmt(m2) + ' m².' }; });
  } };
  function monoTxt(k, e) { return (k === 1 && e ? '' : k === -1 && e ? '−' : String(k).replace('-', '−')) + (e ? 'x' + (e > 1 ? '<sup>' + e + '</sup>' : '') : ''); }
  M.monomio = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('k', 'Coeficiente', -9, 9, 1, 5) + ctrl('e', 'Exponente de x', 0, 5, 1, 2) + ctrl('f', 'Exponente de y', 0, 3, 1, 1), function (o) { var lit = (o.e ? 'x' + (o.e > 1 ? '<sup>' + o.e + '</sup>' : '') : '') + (o.f ? 'y' + (o.f > 1 ? '<sup>' + o.f + '</sup>' : '') : '');
      return '<p class="lb-res" style="font-size:1.6rem">' + String(o.k).replace('-', '−') + lit + '</p><table class="lb2-tab"><tr><th>Coeficiente</th><td>' + String(o.k).replace('-', '−') + '</td></tr><tr><th>Parte literal</th><td>' + (lit || '(no tiene)') + '</td></tr><tr><th>Grado</th><td>' + o.e + ' + ' + o.f + ' = ' + (o.e + o.f) + '</td></tr></table><p class="lb-nota">Dos monomios son semejantes si tienen la misma parte literal: ahí se pueden sumar sus coeficientes. Para multiplicar, se multiplican los coeficientes y se suman los exponentes.</p>'; });
  } };
  M.monomio_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = R(2, 7) * pick([1, -1]), b = R(2, 6), m = R(1, 4), n = R(1, 4);
      return { cons: 'Multiplicá: <b>(' + monoTxt(a, m) + ') · (' + monoTxt(b, n) + ')</b>. Escribí el coeficiente y el exponente del resultado.', campos: [{ lab: 'Coeficiente', v: a * b }, { lab: 'Exponente de x', v: m + n }], ayuda: 'Coeficientes: ' + a + ' · ' + b + '. Exponentes de igual base se suman: ' + m + ' + ' + n + '.', bien: '¡Bien! ' + (a * b) + 'x^' + (m + n) + '.' }; });
  } };
  function poli() { return [R(-6, 6), R(-9, 9), R(-9, 9)]; }
  function poliTxt(P) { var t = [[P[0], 2], [P[1], 1], [P[2], 0]].filter(function (q) { return q[0]; }); return t.map(function (q, i) { var k = q[0], a = Math.abs(k); return (k < 0 ? '− ' : i ? '+ ' : '') + (q[1] && a === 1 ? '' : a) + (q[1] === 2 ? 'x²' : q[1] === 1 ? 'x' : ''); }).join(' ') || '0'; }
  M.polinomio_operar = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var A = poli(), Bp = poli(), resta = p.op === 'resta' || (p.op !== 'suma' && Math.random() < .5); if (!A[0]) A[0] = 2; if (!Bp[0]) Bp[0] = -1;
      var S = A.map(function (x, i) { return resta ? x - Bp[i] : x + Bp[i]; });
      return { cons: 'Calculá: <b>(' + poliTxt(A) + ') ' + (resta ? '−' : '+') + ' (' + poliTxt(Bp) + ')</b>. Escribí el coeficiente de cada término.', campos: [{ lab: 'x²:', v: S[0] }, { lab: 'x:', v: S[1] }, { lab: 'número:', v: S[2] }], ayuda: (resta ? 'Al restar se cambia el signo de todos los términos del segundo polinomio; después ' : '') + 'se suman los términos semejantes.', bien: '¡Bien! ' + poliTxt(S) + '.' }; });
  } };
  M.distributiva = { tipo: 'ejemplo', render: function (el) {
    escena(el, ctrl('a', 'a', 1, 6, 1, 3) + ctrl('b', 'b', 1, 6, 1, 2), function (o) { var a = o.a, b = o.b, X = 70, s = 14;
      return '<svg viewBox="0 0 ' + (X + b * s + 40) + ' ' + (X + a * s + 40) + '" class="lb2-svg" style="max-width:240px"><rect x="20" y="20" width="' + X + '" height="' + X + '" class="c2"/><rect x="' + (20 + X) + '" y="20" width="' + b * s + '" height="' + X + '" class="c1"/><rect x="20" y="' + (20 + X) + '" width="' + X + '" height="' + a * s + '" class="c1"/><rect x="' + (20 + X) + '" y="' + (20 + X) + '" width="' + b * s + '" height="' + a * s + '" class="c0"/>' +
        '<text x="' + (20 + X / 2) + '" y="14">x</text><text x="' + (20 + X + b * s / 2) + '" y="14">' + b + '</text><text x="10" y="' + (24 + X / 2) + '">x</text><text x="10" y="' + (24 + X + a * s / 2) + '">' + a + '</text></svg>' +
        '<p class="lb-nota">El rectángulo de lados (x + ' + a + ') y (x + ' + b + ') se parte en cuatro: x², ' + b + 'x, ' + a + 'x y ' + a * b + '. Cada término de un paréntesis multiplica a cada término del otro.</p><p class="lb-res">(x + ' + a + ')(x + ' + b + ') = x² + ' + (a + b) + 'x + ' + a * b + '</p>'; });
  } };
  M.distributiva_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = R(-6, 7) || 2, b = R(-6, 7) || 3, sa = a < 0 ? '− ' + -a : '+ ' + a, sb = b < 0 ? '− ' + -b : '+ ' + b;
      return { cons: 'Aplicá la distributiva: <b>(x ' + sa + ')(x ' + sb + ')</b>. Escribí los coeficientes del resultado.', campos: [{ lab: 'x²:', v: 1 }, { lab: 'x:', v: a + b }, { lab: 'número:', v: a * b }], ayuda: 'x · x = x²; x · (' + b + ') + (' + a + ') · x = ' + (a + b) + 'x; (' + a + ') · (' + b + ') = ' + a * b + '.', bien: '¡Bien! x² ' + (a + b < 0 ? '− ' + -(a + b) : '+ ' + (a + b)) + 'x ' + (a * b < 0 ? '− ' + -(a * b) : '+ ' + a * b) + '.' }; });
  } };
  M.ecuacion_denominadores = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = pick([2, 3, 4, 5]), b = pick([2, 3, 4, 6].filter(function (x) { return x !== a; })), m = a * b / mcd(a, b), x = m * R(1, 4) * pick([1, -1]), c = x / a + x / b;
      return { cons: 'Resolvé: <b>x/' + a + ' + x/' + b + ' = ' + fmt(c) + '</b>', campos: [{ lab: 'x =', v: x }], ayuda: 'Multiplicá los dos miembros por el mcm de ' + a + ' y ' + b + ' (' + m + ') para sacar los denominadores: ' + m / a + 'x + ' + m / b + 'x = ' + fmt(c * m) + '.', bien: '¡Bien! x = ' + x + '.' }; });
  } };

  // ---------- estilos (prefijo lb2-, solo lección) ----------
  var css = document.createElement('style');
  css.textContent = [
    '.lb2-ctls{display:grid;gap:6px;margin-bottom:8px}.lb2-ctl{display:flex;flex-direction:column;gap:2px;font-size:.9rem;color:#4b6a6c}.lb2-ctl b{color:#253638}.lb2-ctl input[type=range]{width:100%;accent-color:#087E83}.lb-inp.largo{width:180px}',
    '.lb2-svg{display:block;width:100%;max-width:300px;margin:6px auto}.lb2-svg .rayo{stroke:#253638;stroke-width:3;stroke-linecap:round}.lb2-svg .arc{fill:rgba(8,126,131,.18);stroke:#087E83;stroke-width:2}.lb2-svg .recto{fill:none;stroke:#087E83;stroke-width:2}',
    '.lb2-svg .fig{fill:rgba(8,126,131,.2);stroke:#087E83;stroke-width:3;stroke-linejoin:round}.lb2-svg .diag{stroke:#9dbdb9;stroke-width:2;stroke-dasharray:5 4}.lb2-svg .grid{stroke:#E3ECEA;stroke-width:1}.lb2-svg .grid.eje{stroke:#253638;stroke-width:2}',
    '.lb2-svg .cT{fill:#7FD3C4;stroke:#253638}.lb2-svg .cL{fill:#087E83;stroke:#253638}.lb2-svg .cR{fill:#066A6E;stroke:#253638}.lb2-svg .fosf{stroke:#087E83;stroke-width:4;stroke-linecap:round}',
    '.lb2-svg .c0{fill:#fff;stroke:#9dbdb9}.lb2-svg .c1{fill:#D7F0E9;stroke:#9dbdb9}.lb2-svg .c2{fill:#087E83;stroke:#253638}.lb2-svg .pt{fill:#087E83}.lb2-svg .pt2{fill:none;stroke:#253638;stroke-width:2}.lb2-svg .graf{stroke:#087E83;stroke-width:3;fill:none}',
    '.lb2-svg text{font-size:12px;font-weight:800;fill:#253638;text-anchor:middle}.lb2-svg .ptx{font-size:13px;fill:#087E83;text-anchor:start}.lb2-svg .hit{fill:transparent;cursor:pointer}.lb2-svg .hit:hover{fill:rgba(8,126,131,.25)}.lb2-plano{max-width:260px}',
    '.lb2-tab{border-collapse:collapse;margin:8px auto;background:#fff}.lb2-tab th,.lb2-tab td{border:2px solid #E3ECEA;padding:5px 9px;text-align:center;font-weight:700}.lb2-tab th{background:#F3FBF7}.lb2-tab td.on{background:#087E83;color:#fff}',
    '.lb2-bar{min-width:90px}.lb2-bar i{display:block;height:12px;border-radius:6px;background:#087E83}',
    '.lb2-barra{position:relative;height:34px;border-radius:10px;background:#E3ECEA;overflow:hidden}.lb2-barra i{display:block;height:100%;background:#087E83}.lb2-barra span{position:absolute;left:10px;top:7px;font-weight:900;color:#fff;text-shadow:0 0 3px #253638}.lb2-esc{display:flex;justify-content:space-between;font-size:.8rem;font-weight:700;color:#4b6a6c}',
    '.lb2-term{padding:2px 8px;border-radius:8px;font-weight:800}.lb2-term.t0{background:#253638;color:#fff}.lb2-term.t1{background:#087E83;color:#fff}.lb2-term.t2{background:#D7F0E9;color:#253638}',
    '.lb2-pasos{margin:6px 0;padding-left:22px;font-weight:800;font-size:1.1rem;line-height:1.6;color:#066A6E}.lb2-per{text-decoration:overline;text-decoration-thickness:3px;color:#087E83}',
    '.lb2-fb{display:flex;gap:2px;margin:6px 0}.lb2-fb i{flex:1;height:28px;border:2px solid #253638;border-radius:4px;background:#fff}.lb2-fb i.p1{background:#087E83}.lb2-fb i.p2{background:#7FD3C4}.lb2-fb i.fuera{border-style:dashed}',
    '.lb2-lamps{display:flex;gap:4px;justify-content:center;flex-wrap:wrap}.lb2-lamp{display:flex;flex-direction:column;align-items:center;width:44px;padding:6px 0;border:2px solid #E3ECEA;border-radius:12px;background:#fff;cursor:pointer;font:inherit}.lb2-lamp.on{background:#D7F0E9;border-color:#087E83}.lb2-lamp i{font-style:normal;font-size:1.3rem}.lb2-lamp small{color:#4b6a6c;font-weight:700}',
    '.lb2-urna{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;max-width:260px;margin:8px auto;padding:12px;border:3px solid #253638;border-top:0;border-radius:0 0 40px 40px}.lb2-urna i{width:22px;height:22px;border-radius:50%}',
    '.lb2-graf{display:flex;gap:10px;justify-content:center;align-items:flex-end;margin-top:10px}.lb2-col{display:flex;flex-direction:column;align-items:center;gap:4px}.lb2-colb{position:relative;width:44px;height:150px;border-bottom:3px solid #253638;display:flex;align-items:flex-end}.lb2-colb i{display:block;width:100%;background:#087E83;border-radius:6px 6px 0 0}.lb2-colb span{position:absolute;top:-2px;width:100%;text-align:center;font-weight:900}',
    '.lb2-col .lb-btn{padding:4px 10px;margin:0 2px}.lb2-campos{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}.lb2-campo{display:flex;align-items:center;gap:6px;font-weight:700}.lb2-campo em{font-style:normal;font-weight:800;color:#4b6a6c}.lb-pares.uno{grid-template-columns:1fr}',
    '.lb2-barra3{display:flex;height:34px;border-radius:10px;overflow:hidden;border:2px solid #253638}.lb2-barra3 i{display:block;height:100%}.lb2-barra3 .x1{background:#253638}.lb2-barra3 .x2{background:#087E83}.lb2-barra3 .x3{background:#D7F0E9}',
    '.lb2-mapa{position:relative;height:60px;border-radius:12px;background:repeating-linear-gradient(45deg,#F3FBF7,#F3FBF7 8px,#E3ECEA 8px,#E3ECEA 16px)}.lb2-mapa i{position:absolute;left:4%;top:26px;height:6px;border-radius:3px;background:#087E83}.lb2-mapa span{position:absolute;left:4%;top:4px;font-weight:800}',
    '.lb2-ruta{position:relative;height:40px;border-bottom:4px dashed #253638;margin:6px 0}.lb2-ruta span{position:absolute;bottom:2px;font-size:26px}',
    '.lb-cajas.n2 .lb-chip{max-width:100%;border-radius:14px;text-align:left;font-size:.9rem}',
    '.lb-cajas.n4{grid-template-columns:1fr 1fr}@media (min-width:700px){.lb-cajas.n4{grid-template-columns:repeat(4,1fr)}}'
  ].join('');
  document.head.appendChild(css);
})();
