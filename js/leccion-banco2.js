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
    // dibujar puede devolver un html (vista fija) o una lista de pasos [{vis, txt}] (ejemplo PASO A PASO)
    function pintar() { var r = dibujar(val()); if (Array.isArray(r)) pasoAPaso(v, r); else { v.onclick = null; v.innerHTML = r; } }
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
          var ok = D.campos.every(function (f, i) { var x = leer(i); if (typeof f.acepta === 'function') return f.acepta(x); if (f.tipo === 'texto') return [].concat(f.v).some(function (v) { return H.norm(v) === x; }); return Math.abs(x - f.v) <= (f.tol || 1e-9) + Math.abs(f.v) * 1e-9; });
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
  M.transportador = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('g', 'Abertura', 0, 360, 5, R(4, 30) * 5, '°'), function (o) { var g = o.g, d = svgAng(g, 260, 160);
      var cmp = g < 90 ? 'Es <b>menor que 90°</b> (menos que un recto).' : g === 90 ? 'Mide <b>justo 90°</b>.' : g < 180 ? 'Está <b>entre 90° y 180°</b>.' : g === 180 ? 'Mide <b>180°</b>: los lados forman una recta.' : 'Es <b>más de 180°</b>.';
      return [{ vis: d, txt: 'El ángulo abre <b>' + g + '°</b>.' }, { vis: d, txt: 'Lo comparamos con el recto (90°) y el llano (180°). ' + cmp }, { vis: d + '<p class="lb-cn-res">' + g + '° · ángulo ' + tipoAng(g) + '</p>', txt: 'Por eso es un ángulo <b>' + tipoAng(g) + '</b>.' }]; });
  } };
  M.triangulo = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'Lado a', 1, 12, 1, 5, ' cm') + ctrl('b', 'Lado b', 1, 12, 1, 5, ' cm') + ctrl('c', 'Lado c', 1, 12, 1, 6, ' cm'), function (o) {
      var a = o.a, b = o.b, c = o.c, mx = Math.max(a, b, c), resto = a + b + c - mx, P0 = { vis: '<p class="lb-cn-res">' + a + ' cm · ' + b + ' cm · ' + c + ' cm</p>', txt: 'Tenemos tres lados.' };
      if (!(mx < resto)) return [P0, { vis: '<p class="lb-cn-res">' + mx + ' no es menor que ' + resto + '</p>', txt: 'El lado más largo tiene que ser <b>menor</b> que la suma de los otros dos. No se cumple: <b>no se puede armar</b>.' }];
      var A = Math.acos((b * b + c * c - a * a) / (2 * b * c)), Bg = Math.acos((a * a + c * c - b * b) / (2 * a * c)), Cg = Math.PI - A - Bg, deg = function (x) { return Math.round(x * 180 / Math.PI); };
      var sc = 200 / mx, Pt = [[20, 150], [20 + c * sc, 150], [20 + b * sc * Math.cos(A), 150 - b * sc * Math.sin(A)]];
      var svg = '<svg viewBox="0 0 250 165" class="lb2-svg"><polygon class="fig" points="' + Pt.map(function (q) { return q[0].toFixed(1) + ',' + q[1].toFixed(1); }).join(' ') + '"/></svg>';
      var lados = a === b && b === c ? 'equilátero' : (a === b || b === c || a === c) ? 'isósceles' : 'escaleno', mg = Math.max(deg(A), deg(Bg), deg(Cg)), ang = Math.abs(mx * mx - (a * a + b * b + c * c - mx * mx)) < 1e-9 ? 'rectángulo' : mg > 90 ? 'obtusángulo' : 'acutángulo';
      return [P0, { vis: svg, txt: 'El lado más largo (' + mx + ') es menor que la suma de los otros dos (' + resto + '): <b>se puede armar</b>.' },
        { vis: svg, txt: 'Por sus lados es <b>' + lados + '</b>' + (lados === 'equilátero' ? ': los tres iguales.' : lados === 'isósceles' ? ': dos iguales.' : ': los tres distintos.') },
        { vis: svg + '<p class="lb-nota">' + deg(A) + '° + ' + deg(Bg) + '° + ' + deg(Cg) + '° = 180°</p>', txt: 'Sus ángulos suman 180°. El mayor mide <b>' + mg + '°</b>: es <b>' + ang + '</b>.' },
        { vis: svg + '<p class="lb-cn-res">Triángulo ' + lados + ' y ' + ang + '</p>', txt: 'Lo clasificamos por sus lados y por sus ángulos.' }];
    });
  } };
  M.poligono_angulos = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('n', 'Cantidad de lados', 3, 10, 1, 4), function (o) {
      var n = o.n, P = [], cx = 120, cy = 95, r = 80; for (var i = 0; i < n; i++) { var t = -Math.PI / 2 + 2 * Math.PI * i / n; P.push([cx + r * Math.cos(t), cy + r * Math.sin(t)]); }
      var diag = ''; for (var j = 2; j < n - 1; j++) diag += '<line class="diag" x1="' + P[0][0].toFixed(1) + '" y1="' + P[0][1].toFixed(1) + '" x2="' + P[j][0].toFixed(1) + '" y2="' + P[j][1].toFixed(1) + '"/>';
      var pol = '<polygon class="fig" points="' + P.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' ') + '"/>', sv = function (x) { return '<svg viewBox="0 0 240 190" class="lb2-svg">' + pol + x + '</svg>'; };
      return [{ vis: sv(''), txt: 'Un polígono de <b>' + n + ' lados</b>.' },
        { vis: sv(diag), txt: n === 3 ? 'Es un triángulo: no hace falta trazar diagonales.' : 'Desde un vértice trazamos <b>' + (n - 3) + ' diagonal' + (n - 3 === 1 ? '' : 'es') + '</b>.' },
        { vis: sv(diag), txt: 'Quedan <b>' + (n - 2) + ' triángulos</b> (siempre 2 menos que los lados).' },
        { vis: sv(diag) + '<p class="lb-cn-res">' + (n - 2) + ' × 180° = ' + fmt((n - 2) * 180) + '°</p>', txt: 'Cada triángulo suma 180°: multiplicamos.' }];
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
  M.area_figura = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var f = FIG[p.figura] ? p.figura : 'rectangulo';
    escena(el, ctrl('b', f === 'rombo' ? 'Diagonal mayor D' : f === 'trapecio' ? 'Base mayor B' : 'Base', 2, 10, 1, 6, ' cm') + (f === 'trapecio' ? ctrl('c', 'Base menor b', 1, 9, 1, 3, ' cm') : '') + ctrl('h', f === 'rombo' ? 'Diagonal menor d' : 'Altura', 1, 6, 1, 4, ' cm'), function (o) {
      var b2 = f === 'trapecio' ? Math.min(o.c, o.b - 1) : 0, A = areaFig(f, o.b, o.h, b2), d = dibFig(f, o.b, o.h, b2);
      var cuenta = f === 'trapecio' ? '(' + o.b + ' + ' + b2 + ') × ' + o.h + ' ÷ 2' : f === 'triangulo' || f === 'rombo' ? o.b + ' × ' + o.h + ' ÷ 2' : o.b + ' × ' + o.h;
      return [{ vis: d, txt: 'Un ' + FIG[f][0].toLowerCase() + '. Cada cuadradito es <b>1 cm²</b>.' },
        { vis: d + '<p class="lb-nota">Área = ' + FIG[f][1] + '</p>', txt: 'La fórmula del ' + FIG[f][0].toLowerCase() + '.' },
        { vis: d + '<p class="lb-nota">A = ' + cuenta + '</p>', txt: 'Reemplazamos por las medidas.' },
        { vis: d + '<p class="lb-cn-res">A = ' + cuenta + ' = ' + fmt(A) + ' cm²</p>', txt: 'Hacemos la cuenta.' }];
    });
  } };
  M.volumen_cubitos = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'Largo', 1, 6, 1, 4) + ctrl('b', 'Ancho', 1, 5, 1, 3) + ctrl('c', 'Alto', 1, 5, 1, 2), function (o) {
      var s = 16, ox = 30, oy = 170;
      function cubo(x, y, z) { var px = ox + (x - y) * s * .87 + o.b * s * .87, py = oy - (x + y) * s * .5 - z * s, P = function (L) { return L.map(function (q) { return q.join(','); }).join(' '); };
        return '<polygon class="cT" points="' + P([[px, py - s], [px + s * .87, py - s * 1.5], [px, py - s * 2], [px - s * .87, py - s * 1.5]]) + '"/><polygon class="cL" points="' + P([[px - s * .87, py - s * 1.5], [px, py - s], [px, py], [px - s * .87, py - s * .5]]) + '"/><polygon class="cR" points="' + P([[px, py - s], [px + s * .87, py - s * 1.5], [px + s * .87, py - s * .5], [px, py]]) + '"/>'; }
      function sv(capas) { var c = ''; for (var z = 0; z < capas; z++) for (var y = o.b - 1; y >= 0; y--) for (var x = o.a - 1; x >= 0; x--) c += cubo(x, y, z); return '<svg viewBox="0 0 260 190" class="lb2-svg">' + c + '</svg>'; }
      return [{ vis: sv(1), txt: 'Armamos la primera capa: <b>' + o.a + ' × ' + o.b + ' = ' + o.a * o.b + '</b> cubitos.' },
        { vis: sv(o.c), txt: 'Apilamos <b>' + o.c + ' capa' + (o.c > 1 ? 's' : '') + '</b> iguales.' },
        { vis: sv(o.c) + '<p class="lb-cn-res">V = ' + o.a + ' × ' + o.b + ' × ' + o.c + ' = ' + o.a * o.b * o.c + ' cm³</p>', txt: 'Cubitos por capa × capas: ese es el volumen.' }];
    });
  } };
  M.circulo = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('r', 'Radio', 1, 10, 1, 4, ' cm'), function (o) {
      var c = '<circle class="fig" cx="120" cy="115" r="' + o.r * 10 + '"/>', rad = '<line class="rayo" x1="120" y1="115" x2="' + (120 + o.r * 10) + '" y2="115"/>', dia = '<line class="rayo" x1="' + (120 - o.r * 10) + '" y1="115" x2="' + (120 + o.r * 10) + '" y2="115"/>', sv = function (x) { return '<svg viewBox="0 0 240 230" class="lb2-svg">' + c + x + '</svg>'; };
      return [{ vis: sv(rad), txt: 'El radio mide <b>' + o.r + ' cm</b>: va del centro al borde.' },
        { vis: sv(dia), txt: 'El diámetro es el doble: <b>2 × ' + o.r + ' = ' + 2 * o.r + ' cm</b>.' },
        { vis: sv(rad) + '<p class="lb-nota">Longitud = 2 × π × r = 2 × 3,14 × ' + o.r + ' = ' + fmt(r2(2 * PI * o.r)) + ' cm</p>', txt: 'El borde (circunferencia) mide 2 × π × r. Usamos π ≈ 3,14.' },
        { vis: sv(rad) + '<p class="lb-cn-res">Área = π × r² = 3,14 × ' + o.r + ' × ' + o.r + ' = ' + fmt(r2(PI * o.r * o.r)) + ' cm²</p>', txt: 'La superficie del círculo es π × r × r.' }];
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
  M.valor_numerico = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var e = pick(EXPR);
    escena(el, ctrl('x', 'x', -5, 10, 1, 2), function (o) { var x = o.x, xs = x < 0 ? '(' + sig(x) + ')' : String(x), v = sig(e[1](x)).replace('+', '');
      var tab = '<table class="lb2-tab"><tr><th>x</th>' + [-2, -1, 0, 1, 2, 3].map(function (k) { return '<td' + (k === x ? ' class="on"' : '') + '>' + k + '</td>'; }).join('') + '</tr><tr><th>valor</th>' + [-2, -1, 0, 1, 2, 3].map(function (k) { return '<td' + (k === x ? ' class="on"' : '') + '>' + e[1](k) + '</td>'; }).join('') + '</tr></table>';
      return [{ vis: '<p class="lb-pt-g">' + e[0] + '</p>', txt: 'Esta es la expresión. Queremos su valor para <b>x = ' + x + '</b>.' },
        { vis: '<p class="lb-pt-g">' + e[0].replace(/x/g, '<span class="lb2-on">' + xs + '</span>') + '</p>', txt: 'Reemplazamos cada x por ' + xs + '.' },
        { vis: '<p class="lb-pt-g">' + e[0].replace(/x/g, xs) + ' = ' + v + '</p>', txt: 'Resolvemos: primero potencias, después multiplicaciones y al final sumas y restas.' },
        { vis: '<p class="lb-pt-g">' + e[0].replace(/x/g, xs) + ' = ' + v + '</p>' + tab, txt: 'Con cada valor de x la expresión da otro número.' }]; },
      '<div class="lb-pie"><button type="button" class="lb-btn suave" data-otra="1">🔄 Otra expresión</button></div>');
    el.addEventListener('click', function (ev) { if (ev.target.closest('[data-otra]')) { e = pick(EXPR); el._pintar(); } });
  } };
  function terminos() { var L = [], g = { x2: 0, x: 0, c: 0 }; for (var i = 0; i < 6; i++) { var t = pick(['x2', 'x', 'x', 'c']), k = R(1, 9) * pick([1, -1]); g[t] += k; L.push([t, k]); } return { L: L, g: g }; }
  function termTxt(t, k, primero) { var a = Math.abs(k), s = k < 0 ? '− ' : primero ? '' : '+ ', lit = t === 'x2' ? 'x²' : t === 'x' ? 'x' : ''; return s + (lit && a === 1 ? '' : a) + lit; }
  M.terminos_semejantes = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var T = terminos();
    el.innerHTML = '<div class="lb-vista"></div><div class="lb-pie"><button type="button" class="lb-btn suave" data-otra="1">🔄 Otra expresión</button></div>';
    var v = el.querySelector('.lb-vista');
    function armar() { var orden = ['x2', 'x', 'c'], col = { x2: 't0', x: 't1', c: 't2' }, nom = { x2: 'x²', x: 'x', c: 'números' };
      var expr = '<p class="lb-res">' + T.L.map(function (q, i) { return '<span class="lb2-term ' + col[q[0]] + '">' + termTxt(q[0], q[1], !i) + '</span>'; }).join(' ') + '</p>', P = [{ vis: expr, txt: 'Mismo color = misma parte literal: son <b>semejantes</b>.' }], hechos = '';
      orden.forEach(function (t) { var ks = T.L.filter(function (q) { return q[0] === t; }); if (!ks.length) return;
        hechos += '<p class="lb-nota"><span class="lb2-term ' + col[t] + '">' + nom[t] + '</span>: ' + ks.map(function (q) { return sig(q[1]); }).join(' ') + ' = <b>' + sig(T.g[t]) + '</b></p>';
        P.push({ vis: expr + hechos, txt: 'Juntamos los términos con <b>' + nom[t] + '</b>: sumamos sus coeficientes con su signo.' }); });
      P.push({ vis: expr + hechos + '<p class="lb-cn-res">= ' + (orden.filter(function (t) { return T.g[t]; }).map(function (t, i) { return termTxt(t, T.g[t], !i); }).join(' ') || '0') + '</p>', txt: 'Escribimos lo que quedó de cada parte.' });
      pasoAPaso(v, P); }
    el.addEventListener('click', function (e) { if (e.target.closest('[data-otra]')) { T = terminos(); armar(); } }); armar();
  } };
  M.patron_figuras = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('n', 'Figura número', 1, 8, 1, 3), function (o) { var n = o.n, s = 22, lin = '';
      for (var i = 0; i <= n; i++) lin += '<line class="fosf" x1="' + (10 + i * s) + '" y1="10" x2="' + (10 + i * s) + '" y2="' + (10 + s) + '"/>';
      for (var j = 0; j < n; j++) lin += '<line class="fosf" x1="' + (10 + j * s) + '" y1="10" x2="' + (10 + (j + 1) * s) + '" y2="10"/><line class="fosf" x1="' + (10 + j * s) + '" y1="' + (10 + s) + '" x2="' + (10 + (j + 1) * s) + '" y2="' + (10 + s) + '"/>';
      var fig = '<svg viewBox="0 0 ' + (20 + n * s) + ' 45" class="lb2-svg" style="max-height:90px">' + lin + '</svg>';
      var tab = '<table class="lb2-tab"><tr><th>Figura</th>' + [1, 2, 3, 4, 5].map(function (k) { return '<td' + (k === n ? ' class="on"' : '') + '>' + k + '</td>'; }).join('') + '</tr><tr><th>Fósforos</th>' + [1, 2, 3, 4, 5].map(function (k) { return '<td' + (k === n ? ' class="on"' : '') + '>' + (3 * k + 1) + '</td>'; }).join('') + '</tr></table>';
      return [{ vis: fig, txt: 'La figura <b>' + n + '</b> tiene ' + n + ' cuadradito' + (n > 1 ? 's' : '') + ' hechos con fósforos.' },
        { vis: fig + tab, txt: 'Contamos los fósforos de las primeras figuras: 4, 7, 10, 13…' },
        { vis: fig + tab, txt: 'Cada figura tiene <b>3 más</b> que la anterior: hay 1 fósforo inicial y 3 por cada cuadradito.' },
        { vis: fig + tab + '<p class="lb-cn-res">Figura ' + n + ': 3 × ' + n + ' + 1 = ' + (3 * n + 1) + '</p>', txt: 'La fórmula es <b>3n + 1</b>: sirve para cualquier figura.' }]; });
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
  M.porcentaje_barra = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var modo = p.modo || 'parte';
    escena(el, ctrl('p', 'Porcentaje', 5, 95, 5, 25, ' %') + ctrl('t', 'Cantidad', 100, 5000, 100, 2400), function (o) { var parte = o.t * o.p / 100;
      var barra = function (w) { return '<div class="lb2-barra"><i style="width:' + w + '%"></i><span>' + (w ? o.p + ' %' : '') + '</span></div><div class="lb2-esc"><span>0</span><span>' + fmt(o.t) + ' = 100 %</span></div>'; };
      var P = [{ vis: barra(0), txt: 'La barra entera es el total: <b>' + fmt(o.t) + ' = 100 %</b>.' },
        { vis: barra(o.p), txt: 'Pintamos el <b>' + o.p + ' %</b>: ' + o.p + ' de cada 100 partes.' },
        { vis: barra(o.p) + '<p class="lb-cn-res">' + fmt(o.t) + ' × ' + o.p + ' ÷ 100 = ' + fmt(parte) + '</p>', txt: 'Para calcularlo: multiplicamos por ' + o.p + ' y dividimos por 100.' }];
      if (modo === 'aumento' || modo === 'descuento') { var fin = modo === 'aumento' ? o.t + parte : o.t - parte;
        P.push({ vis: barra(o.p) + '<p class="lb-cn-res">' + fmt(o.t) + (modo === 'aumento' ? ' + ' : ' − ') + fmt(parte) + ' = $' + fmt(fin) + '</p>', txt: (modo === 'aumento' ? 'Es un aumento: lo sumamos' : 'Es un descuento: lo restamos') + ' al precio.' }); }
      return P; });
  } };
  M.porcentaje = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var m = p.modo || pick(['parte', 'que', 'descuento', 'aumento']), pc = pick([5, 10, 15, 20, 25, 30, 40, 50, 75]), t = R(2, 60) * 100, parte = t * pc / 100;
      if (m === 'que') return { cons: '¿Qué porcentaje es <b>' + fmt(parte) + '</b> de <b>' + fmt(t) + '</b>?', campos: [{ v: pc, un: '%' }], ayuda: 'Dividí la parte por el total y multiplicá por 100.', bien: '¡Bien! ' + fmt(parte) + ' ÷ ' + fmt(t) + ' × 100 = ' + pc + ' %.' };
      if (m === 'descuento' || m === 'aumento') return { cons: 'Un producto de <b>$' + fmt(t) + '</b> tiene un <b>' + (m === 'aumento' ? 'aumento' : 'descuento') + ' del ' + pc + ' %</b>. ¿Cuál es el precio final?', campos: [{ v: m === 'aumento' ? t + parte : t - parte, un: '$' }], ayuda: 'Calculá el ' + pc + ' % de ' + fmt(t) + ' y ' + (m === 'aumento' ? 'sumalo' : 'restalo') + '.', bien: '¡Bien! Precio final: $' + fmt(m === 'aumento' ? t + parte : t - parte) + '.' };
      return { cons: 'Calculá el <b>' + pc + ' %</b> de <b>' + fmt(t) + '</b>.', campos: [{ v: parte }], ayuda: 'Multiplicá ' + fmt(t) + ' × ' + pc + ' y dividí por 100.', bien: '¡Bien! ' + fmt(parte) + '.' }; });
  } };
  // operaciones combinadas: genera expresión con jerarquía y la resuelve paso a paso
  // Cuentas combinadas por modo (Matemática I · Misión 4): cada paso con su explicación. Solo naturales y divisiones exactas.
  function expr2(modo) {
    var a = R(2, 9), b = R(2, 9), c = R(2, 9), d = R(2, 6), q;
    if (modo === 'izq') { if (Math.random() < .5) { var x = R(20, 60), y = R(2, 15), z = R(2, 15); return { e: x + ' − ' + y + ' + ' + z, P: [[(x - y) + ' + ' + z, 'Suma y resta están al mismo nivel: de izquierda a derecha. Primero ' + x + ' − ' + y + '.'], [String(x - y + z), 'Después la suma.']], v: x - y + z }; }
      q = a * b; return { e: q * c + ' ÷ ' + a + ' × ' + d, P: [[q * c / a + ' × ' + d, '× y ÷ están al mismo nivel: de izquierda a derecha. Primero la división.'], [String(q * c / a * d), 'Después la multiplicación.']], v: q * c / a * d }; }
    if (modo === 'terminos') { q = c * d; var e2 = R(1, 9); return { e: a + ' × ' + b + ' + ' + q + ' ÷ ' + d + ' − ' + e2, P: [[a * b + ' + ' + c + ' − ' + e2, 'Separamos en términos con los + y −: cada término se resuelve por separado.'], [(a * b + c) + ' − ' + e2, 'Ahora sumas y restas, de izquierda a derecha.'], [String(a * b + c - e2), 'Resultado.']], v: a * b + c - e2 }; }
    if (modo === 'parentesis') { if (Math.random() < .5) return { e: '(' + a + ' + ' + b + ') × ' + c, P: [[(a + b) + ' × ' + c, 'Primero lo que está entre paréntesis.'], [String((a + b) * c), 'Después la multiplicación.']], v: (a + b) * c };
      var m = R(b + 1, 15); return { e: a + ' × (' + m + ' − ' + b + ') + ' + c, P: [[a + ' × ' + (m - b) + ' + ' + c, 'Primero el paréntesis.'], [a * (m - b) + ' + ' + c, 'Después la multiplicación.'], [String(a * (m - b) + c), 'Al final la suma.']], v: a * (m - b) + c }; }
    if (modo === 'corchetes') { var m2 = R(c + 1, 12), ins = a + b * (m2 - c); return { e: '[' + a + ' + ' + b + ' × (' + m2 + ' − ' + c + ')] × ' + d, P: [['[' + a + ' + ' + b + ' × ' + (m2 - c) + '] × ' + d, 'De adentro hacia afuera: primero el paréntesis.'], ['[' + a + ' + ' + b * (m2 - c) + '] × ' + d, 'Dentro del corchete, la multiplicación antes que la suma.'], [ins + ' × ' + d, 'Terminamos el corchete.'], [String(ins * d), 'Y la multiplicación de afuera.']], v: ins * d }; }
    if (modo === 'potencias') { if (Math.random() < .5) return { e: a + '² + ' + b + ' × ' + c, P: [[a * a + ' + ' + b + ' × ' + c, 'Primero la potencia.'], [a * a + ' + ' + b * c, 'Después la multiplicación.'], [String(a * a + b * c), 'Al final la suma.']], v: a * a + b * c };
      var p2 = R(1, 4), k = R(2, 3); return { e: '(' + p2 + ' + ' + k + ')² − ' + b + ' × ' + 2, P: [[(p2 + k) + '² − ' + b + ' × 2', 'Primero el paréntesis.'], [(p2 + k) * (p2 + k) + ' − ' + b * 2, 'Después la potencia y la multiplicación (cada término).'], [String((p2 + k) * (p2 + k) - 2 * b), 'Al final la resta.']], v: (p2 + k) * (p2 + k) - 2 * b }; }
    if (modo === 'raiz') { var pr = pick([[9, 16, 5], [36, 64, 10], [25, 144, 13], [64, 36, 10], [81, 144, 15]]); return { e: '√(' + pr[0] + ' + ' + pr[1] + ') × ' + d, P: [['√' + (pr[0] + pr[1]) + ' × ' + d, 'La raíz agrupa como un paréntesis: primero lo de adentro.'], [pr[2] + ' × ' + d, 'Después la raíz.'], [String(pr[2] * d), 'Al final la multiplicación.']], v: pr[2] * d }; }
    if (modo === 'enunciado') { return { e: 'Al doble de ' + a + ' sumale el triple de ' + b, P: [['2 × ' + a + ' + 3 × ' + b, 'Traducimos: «el doble de» es 2 ×, «el triple de» es 3 ×.'], [2 * a + ' + ' + 3 * b, 'Multiplicaciones primero.'], [String(2 * a + 3 * b), 'Al final la suma.']], v: 2 * a + 3 * b }; }
    q = b * c; var t = R(0, 1);
    return t ? { e: a + ' + ' + b + ' × ' + c, P: [[a + ' + ' + b * c, 'La multiplicación va antes que la suma.'], [String(a + b * c), 'Después la suma.']], v: a + b * c } : { e: a * d + ' − ' + q + ' ÷ ' + c, P: [[a * d + ' − ' + b, 'La división va antes que la resta.'], [String(a * d - b), 'Después la resta.']], v: a * d - b };
  }
  function expresion() {
    var a = R(2, 9), b = R(2, 9), c = R(2, 9), d = R(1, 9), t = R(0, 3);
    if (t === 0) return { e: a + ' + ' + b + ' × ' + c, pasos: [a + ' + ' + (b * c), String(a + b * c)], v: a + b * c };
    if (t === 1) return { e: '(' + a + ' + ' + b + ') × ' + c + ' − ' + d, pasos: [(a + b) + ' × ' + c + ' − ' + d, (a + b) * c + ' − ' + d, String((a + b) * c - d)], v: (a + b) * c - d };
    if (t === 2) { var q = b * c; return { e: a * d + ' − ' + q + ' ÷ ' + c + ' + ' + b, pasos: [a * d + ' − ' + b + ' + ' + b, String(a * d - b + b)], v: a * d }; }
    return { e: a + '² − ' + b + ' × ' + (c > 1 ? '(' + c + ' − 1)' : c), pasos: [a * a + ' − ' + b + ' × ' + (c - 1), a * a + ' − ' + b * (c - 1), String(a * a - b * (c - 1))], v: a * a - b * (c - 1) };
  }
  M.jerarquia = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var gen = function () { return p && p.modo ? expr2(p.modo) : expresion(); }, X = gen();
    el.innerHTML = '<div class="lb-vista"></div><div class="lb-pie"><button type="button" class="lb-btn suave" data-o="1">🔄 Otra cuenta</button></div>'; var v = el.querySelector('.lb-vista');
    function armar() { var P = [{ vis: '<p class="lb-pt-g">' + X.e + '</p>', txt: 'Orden: 1) paréntesis, 2) potencias y raíces, 3) × y ÷, 4) + y − (de izquierda a derecha).' }];
      var PS = X.P ? X.P.map(function (q) { return q[0]; }) : X.pasos;
      PS.forEach(function (st, i) { P.push({ vis: '<p class="lb-res">' + X.e + '</p><ol class="lb2-pasos">' + PS.slice(0, i + 1).map(function (q, j) { return '<li' + (j === i ? ' class="on"' : '') + '>= ' + q + '</li>'; }).join('') + '</ol>', txt: X.P ? X.P[i][1] : (i === PS.length - 1 ? 'Último paso: ese es el resultado.' : 'Resolvemos lo que va primero según el orden.') }); });
      pasoAPaso(v, P); }
    el.addEventListener('click', function (e) { if (e.target.closest('[data-o]')) { X = gen(); armar(); } }); armar();
  } };
  M.combinadas = { tipo: 'ejercicio', render: function (el, p, api) { respuesta(el, api, function () { var X = p.modo ? expr2(p.modo) : expresion(); if (X.P) X.pasos = X.P.map(function (q) { return q[0]; }); return { cons: 'Resolvé respetando la jerarquía: <b>' + X.e + '</b>', campos: [{ v: X.v }], ayuda: 'Paso a paso: ' + X.pasos.join(' = ') + '.', bien: '¡Bien! ' + X.e + ' = ' + X.v + '.' }; }); } };
  function periodo(a, b) { var ent = Math.floor(a / b), r = a % b, vistos = {}, dig = '', pos = 0; while (r && vistos[r] == null && pos < 40) { vistos[r] = pos++; r *= 10; dig += Math.floor(r / b); r %= b; } return { ent: ent, dig: dig, ini: r ? vistos[r] : -1 }; }
  M.periodo = { tipo: 'ejemplo', pasos: true, render: function (el) {
    el.innerHTML = '<div class="lb2-ctls"><label class="lb2-ctl">Fracción: <input class="lb-inp chico" data-k="a" inputmode="numeric" value="' + pick([1, 2, 5, 7]) + '"> / <input class="lb-inp chico" data-k="b" inputmode="numeric" value="' + pick([3, 6, 7, 9, 11, 12]) + '"></label></div><div class="lb-vista"></div>';
    var v = el.querySelector('.lb-vista');
    function armar() { var a = Math.floor(num(el.querySelector('[data-k="a"]').value)), b = Math.floor(num(el.querySelector('[data-k="b"]').value));
      if (!(a >= 0 && b >= 1 && b <= 99 && a <= 999)) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Probá con números chicos (denominador hasta 99).</p>'; return; }
      var Q = periodo(a, b), d = Q.dig, plano = Q.ent + (d ? ',' + d : ''), marc = Q.ini < 0 ? plano : Q.ent + ',' + d.slice(0, Q.ini) + '<span class="lb2-per">' + d.slice(Q.ini) + '</span>…';
      var P = [{ vis: '<p class="lb-pt-g">' + a + '/' + b + '</p>', txt: 'Una fracción es una división: <b>' + a + ' ÷ ' + b + '</b>.' },
        { vis: '<p class="lb-pt-g">' + a + ' ÷ ' + b + ' = ' + plano + (Q.ini < 0 ? '' : '…') + '</p>', txt: 'Hacemos la división y miramos las cifras decimales.' }];
      if (Q.ini < 0) P.push({ vis: '<p class="lb-cn-res">' + a + '/' + b + ' = ' + plano + '</p>', txt: 'La división <b>termina</b> (da resto 0): es un <b>decimal exacto</b>.' });
      else { P.push({ vis: '<p class="lb-pt-g">' + marc + '</p>', txt: 'Un resto se repite y desde ahí se repiten las cifras: el <b>período</b> es ' + d.slice(Q.ini) + '.' });
        P.push({ vis: '<p class="lb-cn-res">' + a + '/' + b + ' = ' + marc + '</p>', txt: Q.ini === 0 ? 'El período empieza enseguida: <b>periódico puro</b>.' : 'Antes hay cifras que no se repiten: <b>periódico mixto</b>.' }); }
      pasoAPaso(v, P); }
    el.addEventListener('input', armar); armar();
  } };
  M.decimal_tipo = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = [], vis = {}, tope = 0;
      while (it.length < 9 && tope++ < 2000) { var b = R(2, 30), a = R(1, b * 2), P = periodo(a, b), t = P.ini < 0 ? 0 : P.ini === 0 ? 1 : 2, k = a + '/' + b; if (vis[k] || it.filter(function (x) { return x.c === t; }).length >= 3 || mcd(a, b) !== 1) continue; vis[k] = 1; it.push({ v: k, t: fr(a, b), c: t }); }
      return { tit: 'Ubicá cada fracción según el decimal que da.', cajas: ['Exacto', 'Periódico puro', 'Periódico mixto'], items: it }; });
  } };
  function cientif(x) { var e = Math.floor(Math.log10(Math.abs(x))), m = Math.round(x / Math.pow(10, e) * 1000) / 1000; if (m >= 10) { m /= 10; e++; } return { m: m, e: e }; }
  M.notacion_cientifica = { tipo: 'ejemplo', pasos: true, render: function (el) {
    el.innerHTML = '<div class="lb2-ctls"><label class="lb2-ctl">Número: <input class="lb-inp largo" data-k="n" inputmode="decimal" value="' + pick(['3.450.000', '0,00072', '58.000.000', '0,0305']) + '"></label></div><div class="lb-vista"></div>';
    var v = el.querySelector('.lb-vista');
    function armar() { var x = num(el.querySelector('[data-k="n"]').value); if (!isFinite(x) || !x) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Escribí un número distinto de 0.</p>'; return; }
      var C = cientif(x), L = Math.abs(C.e);
      pasoAPaso(v, [{ vis: '<p class="lb-pt-g">' + fmt(x) + '</p>', txt: 'Queremos escribirlo como un número entre 1 y 10 por una potencia de 10.' },
        { vis: '<p class="lb-pt-g">' + fmt(C.m) + '</p>', txt: 'Movemos la coma hasta dejar <b>una sola cifra distinta de 0</b> antes de ella.' },
        { vis: '<p class="lb-pt-g">' + fmt(C.m) + ' × 10<sup>' + C.e + '</sup></p>', txt: 'La coma se movió <b>' + L + ' lugar' + (L === 1 ? '' : 'es') + '</b> hacia la ' + (C.e >= 0 ? 'izquierda: el exponente es <b>positivo</b>.' : 'derecha: el exponente es <b>negativo</b>.') },
        { vis: '<p class="lb-cn-res">' + fmt(x) + ' = ' + fmt(C.m) + ' × 10<sup>' + C.e + '</sup></p>', txt: 'Ese es el número en notación científica.' }]); }
    el.addEventListener('input', armar); armar();
  } };
  M.notacion = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var m = R(11, 99) / 10, e = pick([R(3, 8), -R(2, 6)]), x = Math.round(m * Math.pow(10, e) * 1e8) / 1e8;
      return { cons: 'Escribí <b>' + fmt(x) + '</b> en notación científica: mantisa × 10 elevado al exponente.', campos: [{ lab: 'Mantisa', v: m }, { lab: '× 10 elevado a', v: e }], ayuda: 'La mantisa tiene una sola cifra antes de la coma; el exponente es cuántos lugares corriste la coma (negativo si el número es menor que 1).', bien: '¡Bien! ' + fmt(m) + ' × 10^' + e + '.' }; });
  } };
  M.fraccion_barras = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var resta = p.op === 'resta';
    escena(el, ctrl('a', 'Numerador 1', 1, 5, 1, 1) + ctrl('b', 'Denominador 1', 2, 6, 1, 2) + ctrl('c', 'Numerador 2', 1, 5, 1, 1) + ctrl('d', 'Denominador 2', 2, 6, 1, 3), function (o) {
      var den = o.b * o.d / mcd(o.b, o.d), n1 = o.a * den / o.b, n2 = o.c * den / o.d, res = resta ? n1 - n2 : n1 + n2;
      function barra(n, partes, cls) { var s = ''; for (var i = 0; i < Math.max(partes, n); i++) s += '<i class="' + (i < n ? cls : '') + (i >= partes ? ' fuera' : '') + '"></i>'; return '<div class="lb2-fb">' + s + '</div>'; }
      var op = resta ? ' − ' : ' + ';
      return [{ vis: barra(o.a, o.b, 'p1') + barra(o.c, o.d, 'p2'), txt: fr(o.a, o.b) + op + fr(o.c, o.d) + ': las partes son de distinto tamaño, no se pueden juntar así.' },
        { vis: barra(n1, den, 'p1') + barra(n2, den, 'p2'), txt: 'Partimos las dos barras en <b>' + den + '</b> partes iguales (denominador común): ' + fr(o.a, o.b) + ' = ' + fr(n1, den) + ' y ' + fr(o.c, o.d) + ' = ' + fr(n2, den) + '.' },
        { vis: barra(n1, den, 'p1') + barra(n2, den, 'p2') + '<p class="lb-cn-res">' + fr(n1, den) + op + fr(n2, den) + ' = ' + fr(res, den) + (mcd(Math.abs(res), den) > 1 && res ? ' = ' + frHtml(res, den) : '') + '</p>', txt: 'Ahora las partes son iguales: ' + (resta ? 'restamos' : 'sumamos') + ' los numeradores.' }]; });
  } };
  M.fraccion_area = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'Tomo', 1, 5, 1, 2) + ctrl('b', 'de', 2, 6, 1, 3) + ctrl('c', 'partes de', 1, 5, 1, 3) + ctrl('d', 'de', 2, 6, 1, 4), function (o) {
      var a = Math.min(o.a, o.b), c = Math.min(o.c, o.d), s = 26;
      function sv(k) { var g = ''; for (var i = 0; i < o.d; i++) for (var j = 0; j < o.b; j++) g += '<rect x="' + (5 + i * s) + '" y="' + (5 + j * s) + '" width="' + s + '" height="' + s + '" class="' + (k >= 2 && i < c && j < a ? 'c2' : k >= 1 && i < c ? 'c1' : 'c0') + '"/>'; return '<svg viewBox="0 0 ' + (10 + o.d * s) + ' ' + (10 + o.b * s) + '" class="lb2-svg" style="max-height:170px">' + g + '</svg>'; }
      return [{ vis: sv(0), txt: 'El cuadrado es el entero, partido en ' + o.d + ' columnas y ' + o.b + ' filas.' },
        { vis: sv(1), txt: 'Pintamos ' + fr(c, o.d) + ': ' + c + ' de las ' + o.d + ' columnas.' },
        { vis: sv(2), txt: 'De lo pintado tomamos ' + fr(a, o.b) + ': ' + a + ' de las ' + o.b + ' filas (lo más oscuro).' },
        { vis: sv(2) + '<p class="lb-cn-res">' + fr(a, o.b) + ' de ' + fr(c, o.d) + ' = ' + fr(a * c, o.b * o.d) + '</p>', txt: 'Quedan <b>' + a * c + '</b> cuadraditos oscuros de <b>' + o.b * o.d + '</b>.' }]; });
  } };
  M.fraccion_operar = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var op = p.op || pick(['suma', 'resta', 'producto', 'division']), a, b, c, d, n, dd, s, tt = 0;
      do { a = R(1, 7); b = R(2, 9); c = R(1, 7); d = R(2, 9); } while (op === 'resta' && a * d === c * b && tt++ < 200);
      if (op === 'suma') { n = a * d + c * b; dd = b * d; s = '+'; } else if (op === 'resta') { if (a * d < c * b) { var t = a; a = c; c = t; t = b; b = d; d = t; } n = a * d - c * b; dd = b * d; s = '−'; } else if (op === 'producto') { n = a * c; dd = b * d; s = '×'; } else { n = a * d; dd = b * c; s = '÷'; }
      return { cons: 'Resolvé: <b>' + fr(a, b) + ' ' + s + ' ' + fr(c, d) + '</b> (podés simplificar o no).', campos: [{ tipo: 'frac', v: n / dd, n: n, d: dd }], ayuda: op === 'suma' || op === 'resta' ? 'Buscá un denominador común y ' + (op === 'suma' ? 'sumá' : 'restá') + ' los numeradores.' : op === 'producto' ? 'Multiplicá numerador por numerador y denominador por denominador.' : 'Multiplicá por la inversa de la segunda fracción.', bien: '¡Bien! = ' + frs(n, dd) + '.' }; });
  } };
  var POSD = [['unidades', 1], ['décimos', .1], ['centésimos', .01]];
  M.redondeo = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('x', 'Número', 0, 20, .01, 7.36) + '<label class="lb2-ctl"><span>Redondear a</span><select class="lb-inp largo" data-k="p">' + POSD.map(function (q, i) { return '<option value="' + i + '"' + (i === 1 ? ' selected' : '') + '>' + q[0] + '</option>'; }).join('') + '</select></label>', function (o) {
      var u = POSD[+o.p][1], lo = Math.floor(o.x / u + 1e-9) * u, hi = lo + u, r = (o.x - lo) < u / 2 - 1e-9 ? lo : hi, W = 260, X = function (v) { return 20 + (v - lo) / u * (W - 40); };
      var sv = '<svg viewBox="0 0 ' + W + ' 70" class="lb2-svg"><line class="rayo" x1="10" y1="35" x2="' + (W - 10) + '" y2="35"/><line class="rayo" x1="' + X(lo) + '" y1="27" x2="' + X(lo) + '" y2="43"/><line class="rayo" x1="' + X(hi) + '" y1="27" x2="' + X(hi) + '" y2="43"/><line class="diag" x1="' + X(lo + u / 2) + '" y1="25" x2="' + X(lo + u / 2) + '" y2="45"/><circle cx="' + X(o.x).toFixed(1) + '" cy="35" r="6" class="pt"/><text x="' + X(lo) + '" y="62">' + fmt(r2(lo)) + '</text><text x="' + X(hi) + '" y="62">' + fmt(r2(hi)) + '</text></svg>';
      return [{ vis: sv, txt: 'El número <b>' + fmt(o.x) + '</b> está entre <b>' + fmt(r2(lo)) + '</b> y <b>' + fmt(r2(hi)) + '</b>.' }, { vis: sv, txt: 'La rayita del medio es <b>' + fmt(r2(lo + u / 2)) + '</b>: si el número llega o la pasa, se redondea para arriba.' }, { vis: sv + '<p class="lb-cn-res">' + fmt(o.x) + ' ≈ ' + fmt(r2(r)) + '</p>', txt: 'Queda más cerca de <b>' + fmt(r2(r)) + '</b>.' }]; });
  } };
  M.redondear = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var i = R(0, 2), u = POSD[i][1], x = R(100, 99999) / 1000, r = Math.round(x / u) * u;
      return { cons: 'Redondeá <b>' + fmt(x) + '</b> a los <b>' + POSD[i][0] + '</b>.', campos: [{ v: r2(r) }], ayuda: 'Mirá la cifra que sigue a los ' + POSD[i][0] + ': si es 5 o más, sube; si es menos de 5, queda igual.', bien: '¡Bien! ' + fmt(x) + ' ≈ ' + fmt(r2(r)) + '.' }; });
  } };
  M.sexagesimal_conv = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'ambos';
    respuesta(el, api, function () { if (md === 'convertir') { var cv = R(0, 2);
        if (cv === 0) { var hh = R(1, 9); return { cons: '¿Cuántos minutos son <b>' + hh + ' horas</b>?', campos: [{ v: hh * 60, un: 'min' }], ayuda: 'Cada hora tiene 60 minutos: multiplicá por 60.', bien: '¡Bien! ' + hh + ' h = ' + hh * 60 + ' min.' }; }
        if (cv === 1) { var mm = R(61, 400); return { cons: 'Pasá <b>' + mm + ' minutos</b> a horas y minutos.', campos: [{ lab: 'h', v: Math.floor(mm / 60) }, { lab: 'min', v: mm % 60 }], ayuda: 'Dividí por 60: el cociente son las horas y el resto, los minutos que sobran.', bien: '¡Bien! ' + mm + ' min = ' + Math.floor(mm / 60) + ' h ' + mm % 60 + ' min.' }; }
      }
      if (md === 'convertir' || (md === 'ambos' && Math.random() < .5)) { var t = R(3700, 30000), h = Math.floor(t / 3600), m = Math.floor(t % 3600 / 60), s = t % 60;
        return { cons: 'Pasá <b>' + fmt(t) + ' segundos</b> a horas, minutos y segundos.', campos: [{ lab: 'h', v: h }, { lab: 'min', v: m }, { lab: 's', v: s }], ayuda: 'Dividí por 60 para pasar a minutos (lo que sobra son segundos) y otra vez por 60 para pasar a horas.', bien: '¡Bien! ' + h + ' h ' + m + ' min ' + s + ' s.' }; }
      var h1 = R(0, 3), m1 = R(10, 59), s1 = R(10, 59), h2 = R(0, 3), m2 = R(10, 59), s2 = R(10, 59), T = (h1 + h2) * 3600 + (m1 + m2) * 60 + s1 + s2;
      return { cons: 'Sumá: <b>' + h1 + ' h ' + m1 + ' min ' + s1 + ' s</b> + <b>' + h2 + ' h ' + m2 + ' min ' + s2 + ' s</b>.', campos: [{ lab: 'h', v: Math.floor(T / 3600) }, { lab: 'min', v: Math.floor(T % 3600 / 60) }, { lab: 's', v: T % 60 }], ayuda: 'Sumá cada columna; si los segundos o minutos pasan de 60, cambiá 60 por 1 de la columna de al lado.', bien: '¡Bien sumado!' }; });
  } };
  // Valor posicional: escribí un número y se ve cada cifra en su lugar, lo que vale y cómo se lee (modo 'valor' | 'leer')
  function leerN(x) { var m = Math.floor(x / 1e6), r = x % 1e6, o = []; if (m) o.push(m === 1 ? 'un millón' : H.letras(m).replace(/veintiuno$/, 'veintiún').replace(/(^| )uno$/, '$1un') + ' millones'); if (r || !m) o.push(H.letras(r)); return o.join(' '); }

  // Comparar naturales: dos números; cuenta cifras y, si empatan, marca la primera cifra distinta

  // Operar en sexagesimal: suma o resta de tiempos (h, min, s) o de ángulos (°, ′, ″), con los canjes de a 60 a la vista

  // Descomponer (ejemplo visual): cada cifra se convierte en un bloque con su valor; modo 'aditiva' o 'potencias'
  var SUP = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'];
  function partesDe(s) { var n = s.length, o = []; for (var k = n - 1; k >= 0; k--) { var d = s[n - 1 - k]; if (d !== '0') o.push({ d: d, k: k }); } return o; }
  // Descomponer (ejercicio): completar el valor de cada cifra (aditiva) o el exponente de cada potencia
  M.descomponer_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var pot = p.modo === 'potencias';
    respuesta(el, api, function () {
      var n; do { n = R(1000, 999999); } while (partesDe(String(n)).length < 3);
      var P = partesDe(String(n));
      if (pot) return { cons: 'Descomponé <b>' + fmt(n) + '</b> con potencias de 10: completá cada exponente.', campos: P.map(function (x) { return { lab: x.d + ' × 10 elevado a', v: x.k }; }), ayuda: 'Contá los lugares desde la derecha empezando en 0: las unidades tienen exponente 0.', bien: '¡Bien! ' + fmt(n) + ' = ' + P.map(function (x) { return x.d + ' × 10' + SUP[x.k]; }).join(' + ') };
      return { cons: 'Descomponé <b>' + fmt(n) + '</b>: escribí lo que vale cada cifra que no es 0, de izquierda a derecha.', campos: P.map(function (x, i) { return { lab: i ? '+' : fmt(n) + ' =', v: Number(x.d) * Math.pow(10, x.k) }; }), ayuda: 'Cada cifra vale la cifra por lo que vale su lugar: no te olvides de los ceros.', bien: '¡Bien! ' + fmt(n) + ' = ' + P.map(function (x) { return fmt(Number(x.d) * Math.pow(10, x.k)); }).join(' + ') };
    });
  } };
  // Pasar entre decimal y binario (ejemplo visual): 'a_binario' muestra la escalera de divisiones; 'a_decimal', el valor de cada lugar

  // Operar en sexagesimal (ejercicio): sumar o restar dos tiempos o dos ángulos y escribir el resultado
  M.sexa_operar_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var ang = p.modo === 'angulo', U = ang ? ['°', '′', '″'] : ['h', 'min', 's'];
    respuesta(el, api, function () {
      var a = [R(1, ang ? 90 : 5), R(10, 59), R(0, 59)], b = [R(1, ang ? 60 : 4), R(10, 59), R(0, 59)], suma = Math.random() < .5;
      var A = a[0] * 3600 + a[1] * 60 + a[2], B = b[0] * 3600 + b[1] * 60 + b[2];
      if (!suma && A < B) { var t = a; a = b; b = t; t = A; A = B; B = t; }
      var T = suma ? A + B : A - B, r = [Math.floor(T / 3600), Math.floor(T / 60) % 60, T % 60];
      var f = function (v) { return v[0] + ' ' + U[0] + ' ' + v[1] + ' ' + U[1] + ' ' + v[2] + ' ' + U[2]; };
      return { cons: (suma ? 'Sumá' : 'Restá') + ': <b>' + f(a) + (suma ? ' + ' : ' − ') + f(b) + '</b>', campos: [{ v: r[0], un: U[0] }, { v: r[1], un: U[1] }, { v: r[2], un: U[2] }],
        ayuda: suma ? 'Sumá cada columna y canjeá cada 60 por 1 de la columna de la izquierda.' : 'Si una columna no alcanza, pedí 1 a la izquierda: suma 60, no 100.', bien: '¡Bien! Da ' + f(r) + '.' };
    });
  } };

  // Potencias de 10 (ejercicio): solo base 10 y exponentes naturales; también multiplicar y dividir por 10, 100 y 1.000
  M.potencias10_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () {
      var k = R(0, 3), e = R(1, 6), a = R(2, 99), q = pick([10, 100, 1000]);
      if (k === 0) return { cons: '¿Cuánto es <b>10' + SUP[e] + '</b>?', campos: [{ v: Math.pow(10, e) }], ayuda: 'El exponente dice cuántos ceros lleva: 10' + SUP[e] + ' tiene ' + e + ' ceros.', bien: '¡Bien! 10' + SUP[e] + ' = ' + fmt(Math.pow(10, e)) + '.' };
      if (k === 1) return { cons: 'Escribí <b>' + fmt(Math.pow(10, e)) + '</b> como potencia de 10: ¿cuál es el exponente?', campos: [{ lab: '10 elevado a', v: e }], ayuda: 'Contá los ceros: esa es la cantidad de veces que se multiplica el 10.', bien: '¡Bien! ' + fmt(Math.pow(10, e)) + ' = 10' + SUP[e] + '.' };
      if (k === 2) return { cons: '¿Cuánto es <b>' + a + ' × ' + fmt(q) + '</b>?', campos: [{ v: a * q }], ayuda: 'Multiplicar por ' + fmt(q) + ' agrega ' + (String(q).length - 1) + ' ceros.', bien: '¡Bien! ' + a + ' × ' + fmt(q) + ' = ' + fmt(a * q) + '.' };
      return { cons: '¿Cuánto es <b>' + fmt(a * q) + ' ÷ ' + fmt(q) + '</b>?', campos: [{ v: a }], ayuda: 'Dividir por ' + fmt(q) + ' saca ' + (String(q).length - 1) + ' ceros.', bien: '¡Bien! ' + fmt(a * q) + ' ÷ ' + fmt(q) + ' = ' + a + '.' };
    });
  } };
  // Sistema binario, primera pantalla (ejercicio): valores de los lugares y qué números pueden ser binarios (todavía sin pasar de un sistema a otro)
  M.binario_lugares_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () {
      if (Math.random() < .5) { var L = R(4, 7), vals = []; for (var i = 0; i < L; i++) vals.push(Math.pow(2, i)); var h = R(2, L - 1);
        return { cons: 'En binario, cada lugar vale el doble que el de su derecha. Completá el valor que falta: <b>' + vals.map(function (v, i) { return i === h ? '__' : v; }).join(', ') + '</b>', campos: [{ v: vals[h] }], ayuda: 'Duplicá el valor del lugar anterior: ' + vals[h - 1] + ' × 2.', bien: '¡Bien! Va ' + vals[h] + '.' }; }
      var cand = [], es; do { var largo = R(3, 6), x = '1'; for (var j = 1; j < largo; j++) x += String(R(0, Math.random() < .3 ? 2 : 1)); cand = x; es = !/2/.test(x); } while (false);
      return { cons: '¿El número <b>' + cand + '</b> puede estar escrito en el sistema binario? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: es ? ['si', 'sí'] : ['no'] }], ayuda: 'En binario solo existen las cifras 0 y 1.', bien: es ? '¡Bien! Solo tiene ceros y unos.' : '¡Bien! Tiene un 2: en binario no existe.' };
    });
  } };

  // ======= EJEMPLOS PASO A PASO (modelo CIDEAD): el dibujo se arma de a un paso con "Siguiente paso", una línea corta por paso =======
  // P = [{ vis: html del dibujo en ese paso, txt: una línea corta }]. Al cambiar los datos vuelve al paso 1.
  function pasoAPaso(v, P) {
    var k = 0;
    function show() {
      v.innerHTML = '<div class="lb-pp-vis">' + P[k].vis + '</div><p class="lb-pp-txt">' + P[k].txt + '</p><div class="lb-pp-nav"><button type="button" class="lb-pp-b" data-pp="-1"' + (k ? '' : ' disabled') + '>◀ Anterior</button><span>Paso ' + (k + 1) + ' de ' + P.length + '</span><button type="button" class="lb-pp-b sig" data-pp="1"' + (k < P.length - 1 ? '' : ' disabled') + '>Siguiente paso ▶</button></div>';
    }
    v.onclick = function (e) { var b = e.target.closest('[data-pp]'); if (!b || b.disabled) return; k = Math.max(0, Math.min(P.length - 1, k + Number(b.getAttribute('data-pp')))); show(); };
    show();
  }
  H.pasoAPaso = pasoAPaso;   // también lo usan los ejemplos de js/leccion-banco.js
  function entrada(el, lab, val, max, w) { el.innerHTML = '<div class="lb-in-f"><label>' + lab + '</label><input type="text" inputmode="numeric" class="lb-inp lb-vp-in" value="' + val + '" maxlength="' + max + '"' + (w ? ' style="width:' + w + 'ch!important"' : '') + '></div><div class="lb-vista"></div>'; return [el.querySelector('input'), el.querySelector('.lb-vista')]; }
  function soloNum(x) { return String(x).replace(/\D/g, '').replace(/^0+(?=\d)/, ''); }
  function unLetras(x) { return H.letras(x).replace(/veintiuno$/, 'veintiún').replace(/(^| )uno$/, '$1un'); }

  // Valor posicional: 'valor' = cifra por cifra, cuánto vale cada una; 'leer' = separar en períodos y leer grupo por grupo
  var LUG = ['U', 'D', 'C', 'UM', 'DM', 'CM', 'UMi', 'DMi', 'CMi', 'UMM', 'DMM', 'CMM'];
  var NOM = ['unidades', 'decenas', 'centenas', 'unidades de mil', 'decenas de mil', 'centenas de mil', 'unidades de millón', 'decenas de millón', 'centenas de millón', 'unidades de mil millones', 'decenas de mil millones', 'centenas de mil millones'];
  var PER = ['Unidades', 'Miles', 'Millones', 'Miles de millones'];
  function tablaVP(s, hl) {
    var n = s.length, nper = Math.ceil(n / 3), cab = '', sub = '', fil = '';
    for (var g = nper - 1; g >= 0; g--) { var cols = []; for (var j = 2; j >= 0; j--) { var pos = g * 3 + j; if (pos < n) cols.push(pos); }
      cab += '<th colspan="' + cols.length + '" class="lb-vp-per">' + PER[g] + '</th>';
      cols.forEach(function (pos) { var c = s[n - 1 - pos]; sub += '<th>' + LUG[pos] + '</th>'; fil += '<td><span class="lb-vp-c' + (pos === hl ? ' on' : '') + (c === '0' ? ' cero' : '') + '">' + c + '</span></td>'; }); }
    return '<div class="lb-vp-w"><table class="lb-vp' + (n > 7 ? ' vplargo' : '') + '"><thead><tr>' + cab + '</tr><tr>' + sub + '</tr></thead><tbody><tr>' + fil + '</tr></tbody></table></div>';
  }
  function gruposDe(s) { var n = s.length, nper = Math.ceil(n / 3), o = []; for (var g = nper - 1; g >= 0; g--) o.push({ g: g, t: s.slice(Math.max(0, n - (g + 1) * 3), n - g * 3) }); return o; }
  function leerGrupo(G, gs) { var v = Number(G.t); if (!v) return '';
    if (G.g === 0) return H.letras(v);
    if (G.g === 1 || G.g === 3) return v === 1 ? 'mil' : unLetras(v) + ' mil';
    var hayMM = gs.some(function (x) { return x.g === 3 && Number(x.t); }); return (v === 1 && !hayMM) ? 'un millón' : (v === 1 ? 'un' : unLetras(v)) + ' millones'; }
  M.valor_posicional = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var leer = p.modo === 'leer', io = entrada(el, 'Escribí un número', leer ? pick(['3040506000', '12007450', '905300210']) : pick(['57209', '403718', '2060935']), leer ? 12 : 9), inp = io[0], v = io[1];
    function armar() {
      var s = soloNum(inp.value); if (!s) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Escribí un número.</p>'; return; }
      var n = s.length, P = [];
      if (!leer) {
        P.push({ vis: tablaVP(s, -1), txt: 'Ubicamos cada cifra en su lugar, contando desde la derecha.' });
        var partes = [];
        for (var k = n - 1; k >= 0; k--) { var d = s[n - 1 - k]; if (d === '0') continue; var val = fmt(Number(d) * Math.pow(10, k)); partes.push(val);
          P.push({ vis: tablaVP(s, k) + '<p class="lb-cn-res">' + partes.join(' + ') + '</p>', txt: 'El <b>' + d + '</b> está en las <b>' + NOM[k] + '</b>: vale ' + d + ' × ' + fmt(Math.pow(10, k)) + ' = <b>' + val + '</b>.' }); }
        P.push({ vis: tablaVP(s, -1) + '<p class="lb-cn-res">' + partes.join(' + ') + ' = ' + fmt(Number(s)) + '</p>', txt: 'Sumando lo que vale cada cifra volvemos al número.' });
      } else {
        var gs = gruposDe(s), tro = function (hl, leidos) { return '<div class="lb-vp-trozos">' + gs.map(function (G, i) { return '<span class="lb-vp-tr' + (/^0+$/.test(G.t) ? ' cero' : '') + (i === hl ? ' on' : '') + '"><b>' + G.t + '</b><small>' + PER[G.g].toLowerCase() + '</small>' + (leidos && i <= leidos.i && leerGrupo(G, gs) ? '<em>' + leerGrupo(G, gs) + '</em>' : '') + '</span>'; }).join('') + '</div>'; };
        P.push({ vis: '<p class="lb-vp-num">' + s + '</p>', txt: 'Para leerlo, primero hay que separarlo.' });
        P.push({ vis: tro(-1), txt: 'Separamos las cifras de a tres, <b>desde la derecha</b>.' });
        gs.forEach(function (G, i) { var l = leerGrupo(G, gs); P.push({ vis: tro(i, { i: i }), txt: l ? 'El grupo <b>' + G.t + '</b> se lee «<b>' + l + '</b>».' : 'El grupo <b>' + G.t + '</b> tiene solo ceros: no se nombra.' }); });
        var todo = gs.map(function (G) { return leerGrupo(G, gs); }).filter(Boolean).join(' ') || 'cero';
        P.push({ vis: tro(-1, { i: 99 }) + '<p class="lb-vp-big">Se lee: <b>' + esc(todo) + '</b></p>', txt: 'Juntamos los grupos en orden.' });
      }
      pasoAPaso(v, P);
    }
    inp.addEventListener('input', armar); armar();
  } };

  // Descomponer: bloque por bloque
  M.descomponer = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var pot = p.modo === 'potencias', io = entrada(el, 'Escribí un número', pick(['60427', '305081', '7208']), 9), inp = io[0], v = io[1];
    function armar() {
      var s = soloNum(inp.value); if (!s) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Escribí un número.</p>'; return; }
      var Pt = partesDe(s), col = function (i) { return 'c' + (i % 5); }, P = [];
      var cif = function (hasta) { return '<div class="lb-dc-cif">' + s.split('').map(function (d, i) { var k = s.length - 1 - i, j = -1; Pt.forEach(function (x, q) { if (x.k === k) j = q; }); return '<span class="lb-dc-d ' + (j < 0 ? 'cero' : (j <= hasta ? col(j) : 'pend')) + '">' + d + '</span>'; }).join('') + '</div>'; };
      var bl = function (hasta) { return '<div class="lb-dc-bs">' + Pt.slice(0, hasta + 1).map(function (x, i) { var val = fmt(Number(x.d) * Math.pow(10, x.k)); return '<span class="lb-dc-b ' + col(i) + '"><b>' + (pot ? x.d + ' × 10' + SUP[x.k] : val) + '</b><small>' + (pot ? val : x.d + ' × ' + fmt(Math.pow(10, x.k))) + '</small></span>'; }).join('<i class="lb-dc-mas">+</i>') + '</div>'; };
      P.push({ vis: cif(-1), txt: 'Miramos las cifras. Los ceros no suman nada: los salteamos.' });
      Pt.forEach(function (x, i) { P.push({ vis: cif(i) + bl(i), txt: 'El <b>' + x.d + '</b> vale <b>' + (pot ? x.d + ' × 10' + SUP[x.k] : fmt(Number(x.d) * Math.pow(10, x.k))) + '</b>' + (pot ? ' (su lugar es el ' + x.k + ' contando desde 0).' : '.') }); });
      P.push({ vis: cif(99) + bl(99) + '<p class="lb-cn-res">= ' + fmt(Number(s)) + '</p>', txt: 'Sumando todos los bloques volvemos al número.' });
      pasoAPaso(v, P);
    }
    inp.addEventListener('input', armar); armar();
  } };

  // Comparar dos naturales
  M.comparar_naturales = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var p0 = pick([['405000', '98990'], ['405100', '405000'], ['1203400', '1230400'], ['56789', '56798']]);
    el.innerHTML = '<div class="lb-in-f dos"><label>Un número</label><input type="text" inputmode="numeric" class="lb-inp lb-cn-in" value="' + p0[0] + '" maxlength="10"><label>Otro número</label><input type="text" inputmode="numeric" class="lb-inp lb-cn-in" value="' + p0[1] + '" maxlength="10"></div><div class="lb-vista"></div>';
    var ins = el.querySelectorAll('input'), v = el.querySelector('.lb-vista');
    function armar() {
      var a = soloNum(ins[0].value), b = soloNum(ins[1].value);
      if (!a || !b) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Escribí dos números.</p>'; return; }
      var L = Math.max(a.length, b.length), dif = -1, P = [];
      function fila(x, d) { var pad = L - x.length, h = ''; for (var k = 0; k < L; k++) { var c = k < pad ? '' : x[k - pad]; h += '<span class="lb-cn-c' + (c === '' ? ' vac' : '') + (d >= 0 && k === d ? ' on' : (d > 0 && k < d ? ' eq' : '')) + '">' + c + '</span>'; } return '<div class="lb-cn-f">' + h + '</div>'; }
      var dos = function (d) { return '<div class="lb-cn">' + fila(a, d) + fila(b, d) + '</div>'; };
      P.push({ vis: dos(-1), txt: 'Ponemos un número debajo del otro, alineados a la derecha.' });
      var sg;
      if (a.length !== b.length) { sg = a.length > b.length ? '>' : '<'; P.push({ vis: dos(-1), txt: 'Contamos las cifras: <b>' + a.length + '</b> y <b>' + b.length + '</b>. El que tiene más cifras es mayor.' }); }
      else { for (var i = 0; i < L; i++) if (a[i] !== b[i]) { dif = i; break; }
        P.push({ vis: dos(-1), txt: 'Los dos tienen <b>' + L + '</b> cifras: hay que comparar cifra por cifra, desde la izquierda.' });
        if (dif < 0) sg = '=';
        else { sg = a[dif] > b[dif] ? '>' : '<'; P.push({ vis: dos(dif), txt: (dif ? 'Las primeras cifras son iguales. ' : '') + 'La primera distinta: <b>' + a[dif] + '</b> contra <b>' + b[dif] + '</b>.' }); } }
      P.push({ vis: dos(dif) + '<p class="lb-cn-res">' + fmt(Number(a)) + ' <b>' + sg + '</b> ' + fmt(Number(b)) + '</p>', txt: sg === '=' ? 'Son el mismo número.' : 'Ya sabemos cuál es mayor.' });
      pasoAPaso(v, P);
    }
    [].forEach.call(ins, function (i) { i.addEventListener('input', armar); }); armar();
  } };

  // Pasar entre decimal y binario
  M.binario_pasar = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var aBin = p.modo !== 'a_decimal', io = entrada(el, aBin ? 'Número decimal (hasta 255)' : 'Número binario (solo 0 y 1)', aBin ? pick(['19', '45', '100']) : pick(['101101', '11001', '1110']), aBin ? 3 : 8), inp = io[0], v = io[1];
    function armar() {
      var s = String(inp.value).trim(), P = [];
      if (aBin) {
        var n = parseInt(soloNum(s), 10);
        if (!(n >= 1 && n <= 255)) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Escribí un número del 1 al 255.</p>'; return; }
        var rows = [], x = n; while (x > 0) { rows.push({ x: x, q: Math.floor(x / 2), r: x % 2 }); x = Math.floor(x / 2); }
        var tab = function (h, fin) { return '<div class="lb-bp-w"><table class="lb-bp"><thead><tr><th></th><th>cociente</th><th>resto</th></tr></thead><tbody>' + rows.slice(0, h).map(function (r) { return '<tr><td>' + r.x + ' ÷ 2</td><td>= ' + r.q + '</td><td class="lb-bp-r' + (fin ? '' : ' tenue') + '">' + r.r + '</td></tr>'; }).join('') + '</tbody></table>' + (fin ? '<div class="lb-bp-fl">↑<small>de abajo<br>hacia arriba</small></div>' : '') + '</div>'; };
        rows.forEach(function (r, i) { P.push({ vis: tab(i + 1), txt: '<b>' + r.x + ' ÷ 2 = ' + r.q + '</b> y sobra <b>' + r.r + '</b>.' + (r.q === 0 ? ' El cociente dio 0: terminamos.' : '') }); });
        P.push({ vis: tab(rows.length, true) + '<p class="lb-cn-res">' + n + ' = ' + rows.map(function (r) { return r.r; }).reverse().join('') + '₂</p>', txt: 'Leemos los restos <b>de abajo hacia arriba</b>.' });
      } else {
        if (!/^[01]+$/.test(s)) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Un número binario solo tiene ceros y unos.</p>'; return; }
        var Ln = s.length, fila = function (vals, marcar) { return '<div class="lb-bp-row">' + s.split('').map(function (d, i) { var val = Math.pow(2, Ln - 1 - i); return '<div class="lb-bp-c' + (marcar && d === '1' ? ' on' : '') + '"><small>' + (vals ? val : '&nbsp;') + '</small><b>' + d + '</b></div>'; }).join('') + '</div>'; };
        var sum = []; s.split('').forEach(function (d, i) { if (d === '1') sum.push(Math.pow(2, Ln - 1 - i)); });
        P.push({ vis: fila(false, false), txt: 'Este es el número en binario.' });
        P.push({ vis: fila(true, false), txt: 'Arriba de cada cifra, el valor de su lugar: <b>1</b> a la derecha y el doble en cada lugar hacia la izquierda.' });
        P.push({ vis: fila(true, true), txt: 'Nos quedamos con los lugares que tienen <b>1</b>.' });
        P.push({ vis: fila(true, true) + '<p class="lb-cn-res">' + s + '₂ = ' + (sum.length ? sum.join(' + ') + ' = ' + sum.reduce(function (a, b) { return a + b; }, 0) : '0') + '</p>', txt: 'Sumamos esos valores.' });
      }
      pasoAPaso(v, P);
    }
    inp.addEventListener('input', armar); armar();
  } };

  // Operar en sexagesimal: tiempos (h, min, s) o ángulos (°, ′, ″), columna por columna
  M.sexa_operar = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var ang = p.modo === 'angulo', U = ang ? ['°', '′', '″'] : ['h', 'min', 's'], X = ang ? [[48, 35, 20], [27, 50, 45]] : [[2, 50, 35], [1, 25, 40]];
    function caja(i, j) { return '<input type="text" inputmode="numeric" class="lb-inp lb-sx-in" data-i="' + i + '" data-j="' + j + '" value="' + X[i][j] + '" maxlength="3"><em>' + U[j] + '</em>'; }
    el.innerHTML = '<div class="lb-sx-op"><button type="button" class="lb-chip on" data-op="+">Sumar</button><button type="button" class="lb-chip" data-op="-">Restar</button></div>' +
      '<div class="lb-sx-dat">' + [0, 1].map(function (i) { return '<div class="lb-sx-row">' + caja(i, 0) + caja(i, 1) + caja(i, 2) + '</div>'; }).join('') + '</div><div class="lb-vista"></div>';
    var op = '+', v = el.querySelector('.lb-vista');
    function val(i, j) { var x = Math.floor(num(el.querySelector('[data-i="' + i + '"][data-j="' + j + '"]').value)); return isNaN(x) || x < 0 ? 0 : x; }
    function tabla(a, b, r, hl) { var c = function (v3, cls) { return '<tr class="' + (cls || '') + '"><td>' + (cls === 'res' ? '' : (cls === 'b' ? (op === '+' ? '+' : '−') : '')) + '</td>' + [0, 1, 2].map(function (j) { return '<td class="' + (hl === j ? 'on' : '') + '">' + (v3 ? v3[j] + ' ' + U[j] : '') + '</td>'; }).join('') + '</tr>'; };
      return '<table class="lb-sx-t">' + c(a) + c(b, 'b') + c(r, 'res') + '</table>'; }
    function armar() {
      var a = [val(0, 0), val(0, 1), val(0, 2)], b = [val(1, 0), val(1, 1), val(1, 2)], P = [];
      if (a[1] > 59 || a[2] > 59 || b[1] > 59 || b[2] > 59) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Los ' + U[1] + ' y los ' + U[2] + ' van de 0 a 59.</p>'; return; }
      P.push({ vis: tabla(a, b, null), txt: 'Ponemos las medidas en columnas: ' + U[0] + ' con ' + U[0] + ', ' + U[1] + ' con ' + U[1] + ' y ' + U[2] + ' con ' + U[2] + '.' });
      if (op === '+') {
        var r = [a[0] + b[0], a[1] + b[1], a[2] + b[2]];
        P.push({ vis: tabla(a, b, r.slice()), txt: 'Sumamos cada columna.' });
        if (r[2] >= 60) { r[2] -= 60; r[1] += 1; P.push({ vis: tabla(a, b, r.slice(), 2), txt: 'Los ' + U[2] + ' pasan de 60: canjeamos 60 ' + U[2] + ' por <b>1 ' + U[1] + '</b>.' }); }
        if (r[1] >= 60) { r[1] -= 60; r[0] += 1; P.push({ vis: tabla(a, b, r.slice(), 1), txt: 'Los ' + U[1] + ' pasan de 60: canjeamos 60 ' + U[1] + ' por <b>1 ' + U[0] + '</b>.' }); }
        P.push({ vis: tabla(a, b, r) + '<p class="lb-cn-res">= ' + r[0] + ' ' + U[0] + ' ' + r[1] + ' ' + U[1] + ' ' + r[2] + ' ' + U[2] + '</p>', txt: 'Ninguna columna llega a 60: ese es el resultado.' });
      } else {
        if (a[0] * 3600 + a[1] * 60 + a[2] < b[0] * 3600 + b[1] * 60 + b[2]) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Para restar, la primera medida tiene que ser mayor.</p>'; return; }
        var t = a.slice();
        if (t[2] < b[2]) { t[2] += 60; t[1] -= 1; P.push({ vis: tabla(t.slice(), b, null, 2), txt: 'No alcanzan los ' + U[2] + ': pedimos 1 ' + U[1] + ' y lo cambiamos por <b>60 ' + U[2] + '</b>.' }); }
        if (t[1] < b[1]) { t[1] += 60; t[0] -= 1; P.push({ vis: tabla(t.slice(), b, null, 1), txt: 'No alcanzan los ' + U[1] + ': pedimos 1 ' + U[0] + ' y lo cambiamos por <b>60 ' + U[1] + '</b>.' }); }
        var rr = [t[0] - b[0], t[1] - b[1], t[2] - b[2]];
        P.push({ vis: tabla(t, b, rr) + '<p class="lb-cn-res">= ' + rr[0] + ' ' + U[0] + ' ' + rr[1] + ' ' + U[1] + ' ' + rr[2] + ' ' + U[2] + '</p>', txt: 'Ahora restamos cada columna.' });
      }
      pasoAPaso(v, P);
    }
    el.addEventListener('input', armar);
    el.addEventListener('click', function (e) { var bt = e.target.closest('[data-op]'); if (!bt) return; op = bt.getAttribute('data-op'); [].forEach.call(el.querySelectorAll('[data-op]'), function (x) { x.classList.toggle('on', x === bt); });
      if (op === '-') { var d = ang ? [[90, 0, 0], [37, 25, 10]] : [[5, 10, 0], [2, 45, 30]]; [].forEach.call(el.querySelectorAll('.lb-sx-in'), function (x) { x.value = d[+x.getAttribute('data-i')][+x.getAttribute('data-j')]; }); } armar(); });
    armar();
  } };

  // Agrupar de a 60: segundos a horas, minutos y segundos
  M.sexagesimal = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var io = entrada(el, 'Segundos', pick(['7384', '4000', '9125']), 6), inp = io[0], v = io[1];
    function caj(h, m, s) { return '<div class="lb-sg">' + (h != null ? '<span><b>' + h + '</b><small>h</small></span>' : '') + (m != null ? '<span><b>' + m + '</b><small>min</small></span>' : '') + '<span><b>' + s + '</b><small>s</small></span></div>'; }
    function armar() {
      var t = parseInt(soloNum(inp.value), 10); if (!(t >= 1)) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Escribí una cantidad de segundos.</p>'; return; }
      var m = Math.floor(t / 60), s = t % 60, h = Math.floor(m / 60), mm = m % 60, P = [];
      P.push({ vis: caj(null, null, fmt(t)), txt: 'Tenemos <b>' + fmt(t) + ' segundos</b>.' });
      P.push({ vis: caj(null, m, s), txt: 'Cada 60 s forman 1 min: <b>' + fmt(t) + ' ÷ 60 = ' + m + '</b> min y sobran <b>' + s + '</b> s.' });
      if (m >= 60) P.push({ vis: caj(h, mm, s), txt: 'Cada 60 min forman 1 h: <b>' + m + ' ÷ 60 = ' + h + '</b> h y sobran <b>' + mm + '</b> min.' });
      P.push({ vis: caj(m >= 60 ? h : null, m >= 60 ? mm : m, s) + '<p class="lb-cn-res">' + fmt(t) + ' s = ' + (m >= 60 ? h + ' h ' + mm + ' min ' : m + ' min ') + s + ' s</p>', txt: 'Ya no queda ningún grupo de 60.' });
      pasoAPaso(v, P);
    }
    inp.addEventListener('input', armar); armar();
  } };

  // Sistema binario: los lugares valen 1, 2, 4, 8…; al final se prenden y apagan las lámparas
  M.binario_lamparas = { tipo: 'ejemplo', pasos: true, render: function (el) {
    el.innerHTML = '<div class="lb-vista"></div>'; var v = el.querySelector('.lb-vista'), on = [0, 0, 1, 0, 1, 1, 0, 1];
    function lamps(ver, toca) { return '<div class="lb2-lamps">' + on.map(function (b, i) { var val = Math.pow(2, 7 - i), vis = 7 - i < ver; return '<button type="button" class="lb2-lamp' + (b && toca ? ' on' : '') + '"' + (toca ? ' data-l="' + i + '"' : ' disabled') + '><i>' + (b && toca ? '💡' : '○') + '</i><b>' + (toca ? b : '') + '</b><small>' + (vis ? val : '?') + '</small></button>'; }).join('') + '</div>'; }
    var P = [{ vis: lamps(0), txt: 'Cada lámpara es un lugar. Puede estar apagada (0) o prendida (1).' },
      { vis: lamps(1), txt: 'El lugar de la derecha vale <b>1</b>.' }, { vis: lamps(2), txt: 'El siguiente vale el doble: <b>2</b>.' },
      { vis: lamps(3), txt: 'El doble de 2: <b>4</b>.' }, { vis: lamps(4), txt: 'El doble de 4: <b>8</b>.' }, { vis: lamps(8), txt: 'Y así sigue: 16, 32, 64, 128.' }];
    function fin() { var sum = []; on.forEach(function (b, i) { if (b) sum.push(Math.pow(2, 7 - i)); }); return lamps(8, true) + '<p class="lb-cn-res">' + on.join('') + '₂ = ' + (sum.join(' + ') || '0') + ' = ' + sum.reduce(function (a, b) { return a + b; }, 0) + '</p>'; }
    P.push({ vis: fin(), txt: 'Tocá las lámparas: el número vale la suma de los lugares prendidos.' });
    pasoAPaso(v, P);
    el.addEventListener('click', function (e) { var b = e.target.closest('[data-l]'); if (!b) return; var i = +b.getAttribute('data-l'); on[i] = on[i] ? 0 : 1; P[P.length - 1].vis = fin(); v.querySelector('.lb-pp-vis').innerHTML = P[P.length - 1].vis; });
  } };

  // Potencias de 10: el 10 se multiplica por sí mismo, un factor por paso; cada factor agrega un cero
  M.potencias10 = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var io = entrada(el, 'Exponente (de 0 a 7)', pick(['3', '5', '4']), 1, 4), inp = io[0], v = io[1];
    function armar() {
      var e = parseInt(soloNum(inp.value), 10); if (!(e >= 0 && e <= 7)) { v.onclick = null; v.innerHTML = '<p class="lb-ayuda">Probá con un exponente del 0 al 7.</p>'; return; }
      var P = [{ vis: '<p class="lb-pt-g">10' + SUP[e] + '</p>', txt: 'El exponente <b>' + e + '</b> dice cuántas veces se multiplica el 10.' }];
      if (e === 0) P.push({ vis: '<p class="lb-pt-g">10⁰ = 1</p>', txt: 'Con exponente 0 no se multiplica ninguna vez: da <b>1</b>.' });
      for (var i = 1; i <= e; i++) P.push({ vis: '<p class="lb-pt-f">' + Array(i + 1).join('10 × ').slice(0, -3) + '</p><p class="lb-pt-g">= ' + fmt(Math.pow(10, i)) + '</p>', txt: i === 1 ? 'Un 10.' : 'Otro × 10: se agrega un cero. Ya van <b>' + i + '</b> ceros.' });
      if (e > 0) P.push({ vis: '<p class="lb-pt-g">10' + SUP[e] + ' = ' + fmt(Math.pow(10, e)) + '</p>', txt: 'Un 1 seguido de <b>' + e + '</b> ceros: tantos como el exponente.' });
      pasoAPaso(v, P);
    }
    inp.addEventListener('input', armar); armar();
  } };

  // ======= NÚMEROS NATURALES (Matemática I · Misión 2): un ejemplo paso a paso y una práctica, con un modo por tema =======
  function puntos(f, c, rotar) { var s = 22, F = rotar ? c : f, C = rotar ? f : c, g = ''; for (var i = 0; i < F; i++) for (var j = 0; j < C; j++) g += '<circle cx="' + (14 + j * s) + '" cy="' + (14 + i * s) + '" r="8" class="pt"/>'; return '<svg viewBox="0 0 ' + (8 + C * s) + ' ' + (8 + F * s) + '" class="lb2-svg" style="max-height:200px">' + g + '</svg>'; }
  var LUGR = [['decenas', 10], ['centenas', 100], ['unidades de mil', 1000]];
  M.naturales = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'asociativa', C = {
      asociativa: ctrl('a', 'Primer número', 1, 99, 1, 36) + ctrl('b', 'Segundo número', 1, 99, 1, 47) + ctrl('c', 'Tercer número', 1, 99, 1, 64),
      inversa: ctrl('a', 'Un número', 1, 500, 1, 45) + ctrl('b', 'Otro número', 1, 500, 1, 30),
      descomposicion: ctrl('a', 'Primer número', 10, 99, 1, 47) + ctrl('b', 'Segundo número', 10, 99, 1, 36),
      compensacion: ctrl('a', 'Primer número', 10, 300, 1, 146) + ctrl('b', 'Número cerca de uno redondo', 11, 99, 1, 39),
      multiplicar: ctrl('f', 'Filas', 1, 9, 1, 4) + ctrl('c', 'Columnas', 1, 9, 1, 6),
      distributiva: ctrl('a', 'Multiplicador', 2, 9, 1, 6) + ctrl('b', 'Decenas', 10, 90, 10, 40) + ctrl('c', 'Unidades', 1, 9, 1, 3),
      mental: ctrl('a', 'Multiplicador', 2, 9, 1, 7) + ctrl('b', 'Número cerca de 100', 95, 105, 1, 98),
      division: ctrl('D', 'Dividendo', 10, 200, 1, 47) + ctrl('d', 'Divisor', 2, 12, 1, 6),
      relacion: ctrl('D', 'Dividendo', 10, 500, 1, 157) + ctrl('d', 'Divisor', 2, 15, 1, 6),
      falta: ctrl('d', 'Divisor', 2, 15, 1, 8) + ctrl('q', 'Cociente', 1, 50, 1, 23) + ctrl('r', 'Resto', 0, 14, 1, 5),
      redondear: ctrl('x', 'Número', 10, 99999, 1, 46382) + ctrl('k', 'A las (1 decenas · 2 centenas · 3 unidades de mil)', 1, 3, 1, 2),
      estimar: ctrl('a', 'Primer número', 100, 999, 1, 489) + ctrl('b', 'Segundo número', 100, 999, 1, 312),
      pasos: ctrl('n', 'Cuadernos', 2, 9, 1, 4) + ctrl('pr', 'Precio de cada uno ($)', 100, 900, 50, 350) + ctrl('pa', 'Pago con ($)', 1000, 10000, 500, 2000) }[md];
    escena(el, C, function (o) {
      var R1 = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; };
      if (md === 'asociativa') { var n = [o.a, o.b, o.c], par = null; [[0, 1], [0, 2], [1, 2]].forEach(function (q) { if (!par && (n[q[0]] + n[q[1]]) % 10 === 0) par = q; });
        var t = fmt(o.a + o.b + o.c), P = [{ vis: R1(o.a + ' + ' + o.b + ' + ' + o.c), txt: 'Tenemos que sumar tres números.' }];
        if (par) { var otro = [0, 1, 2].filter(function (k) { return par.indexOf(k) < 0; })[0], rd = n[par[0]] + n[par[1]];
          P.push({ vis: R1('(' + n[par[0]] + ' + ' + n[par[1]] + ') + ' + n[otro]), txt: 'Cambiamos el orden y agrupamos <b>' + n[par[0]] + ' + ' + n[par[1]] + '</b>: dan un número redondo.' });
          P.push({ vis: R1(rd + ' + ' + n[otro]), txt: n[par[0]] + ' + ' + n[par[1]] + ' = <b>' + rd + '</b>. Ahora la cuenta es fácil.' });
          P.push({ vis: RS(o.a + ' + ' + o.b + ' + ' + o.c + ' = ' + t), txt: 'El resultado es el mismo que sumando en orden: el orden y la forma de agrupar no lo cambian.' }); }
        else { P.push({ vis: R1('(' + o.a + ' + ' + o.b + ') + ' + o.c + ' = ' + (o.a + o.b) + ' + ' + o.c), txt: 'Ningún par da un número redondo: sumamos de a dos.' }); P.push({ vis: RS(o.a + ' + ' + o.b + ' + ' + o.c + ' = ' + t), txt: 'Probá cambiar un número para que dos de ellos sumen 10, 20, 30…' }); }
        return P; }
      if (md === 'inversa') { var c = o.a + o.b; return [{ vis: R1(o.a + ' + ' + o.b + ' = ' + c), txt: 'Una suma.' }, { vis: R1(o.a + ' + ' + o.b + ' = ' + c) + R1(c + ' − ' + o.b + ' = ' + o.a), txt: 'Si al total le restamos <b>' + o.b + '</b>, volvemos a ' + o.a + ': la resta deshace la suma.' }, { vis: R1(o.a + ' + ' + o.b + ' = ' + c) + R1(c + ' − ' + o.b + ' = ' + o.a) + R1(c + ' − ' + o.a + ' = ' + o.b), txt: 'Y si le restamos <b>' + o.a + '</b>, nos queda ' + o.b + '.' }, { vis: RS('1 suma → 2 restas'), txt: 'Con una suma ya sabés el resultado de dos restas: por eso la resta sirve para controlar una suma.' }]; }
      if (md === 'descomposicion') { var dec = o.b - o.b % 10, un = o.b % 10; return [{ vis: R1(o.a + ' + ' + o.b), txt: 'Queremos sumar mentalmente.' }, { vis: R1(o.a + ' + ' + dec + ' + ' + un), txt: 'Partimos el ' + o.b + ' en <b>' + dec + '</b> y <b>' + un + '</b>.' }, { vis: R1((o.a + dec) + ' + ' + un), txt: 'Primero sumamos las decenas: ' + o.a + ' + ' + dec + ' = <b>' + (o.a + dec) + '</b>.' }, { vis: RS(o.a + ' + ' + o.b + ' = ' + (o.a + o.b)), txt: 'Después las unidades: ' + (o.a + dec) + ' + ' + un + ' = ' + (o.a + o.b) + '.' }]; }
      if (md === 'compensacion') { var k = (10 - o.b % 10) % 10, rd2 = o.b + k;
        if (!k) return [{ vis: R1(o.a + ' + ' + o.b), txt: o.b + ' ya es redondo.' }, { vis: RS(o.a + ' + ' + o.b + ' = ' + (o.a + o.b)), txt: 'Probá con un número que esté cerca de uno redondo, como 39 o 98.' }];
        return [{ vis: R1(o.a + ' + ' + o.b), txt: o.b + ' está cerca de <b>' + rd2 + '</b>.' }, { vis: R1(o.a + ' + ' + rd2), txt: 'Sumamos el redondo: le agregamos <b>' + k + '</b> de más.' }, { vis: R1(o.a + ' + ' + rd2 + ' = ' + (o.a + rd2)), txt: 'Esta cuenta es fácil.' }, { vis: RS((o.a + rd2) + ' − ' + k + ' = ' + (o.a + o.b)), txt: 'Le sacamos los <b>' + k + '</b> que habíamos agregado: compensamos.' }]; }
      if (md === 'multiplicar') { var rep = Array(o.f + 1).join(o.c + ' + ').slice(0, -3); return [{ vis: puntos(o.f, o.c), txt: '<b>' + o.f + '</b> filas de <b>' + o.c + '</b> puntos.' }, { vis: puntos(o.f, o.c) + R1(rep), txt: 'Podemos sumar fila por fila: ' + o.f + ' veces ' + o.c + '.' }, { vis: puntos(o.f, o.c) + RS(o.f + ' × ' + o.c + ' = ' + o.f * o.c), txt: 'Multiplicar es una suma repetida, más corta.' }, { vis: puntos(o.f, o.c, true) + RS(o.c + ' × ' + o.f + ' = ' + o.f * o.c), txt: 'Girando el dibujo quedan ' + o.c + ' filas de ' + o.f + ': el orden de los factores no cambia el producto.' }]; }
      if (md === 'distributiva') { var resta = p.op === 'resta', b = o.b, c2 = o.c, tot = resta ? b - c2 : b + c2, sg = resta ? ' − ' : ' + ';
        return [{ vis: R1(o.a + ' × ' + tot), txt: 'Queremos calcular ' + o.a + ' × ' + tot + '.' }, { vis: R1(o.a + ' × (' + b + sg + c2 + ')'), txt: 'Escribimos ' + tot + ' como <b>' + b + sg + c2 + '</b>.' }, { vis: R1(o.a + ' × ' + b + sg + o.a + ' × ' + c2), txt: 'El ' + o.a + ' multiplica a <b>cada</b> término del paréntesis.' }, { vis: R1(o.a * b + sg + o.a * c2), txt: o.a + ' × ' + b + ' = ' + o.a * b + ' y ' + o.a + ' × ' + c2 + ' = ' + o.a * c2 + '.' }, { vis: RS(o.a + ' × ' + tot + ' = ' + o.a * tot), txt: (resta ? 'Restamos' : 'Sumamos') + ' los dos productos.' }]; }
      if (md === 'mental') { var dif = o.b - 100, sg2 = dif < 0 ? ' − ' : ' + ', ad = Math.abs(dif);
        if (!dif) return [{ vis: RS(o.a + ' × 100 = ' + o.a * 100), txt: 'Por 100 se agregan dos ceros. Probá con 98 o 103.' }];
        return [{ vis: R1(o.a + ' × ' + o.b), txt: o.b + ' está cerca de <b>100</b>.' }, { vis: R1(o.a + ' × (100' + sg2 + ad + ')'), txt: 'Escribimos ' + o.b + ' = 100' + sg2 + ad + '.' }, { vis: R1(o.a + ' × 100' + sg2 + o.a + ' × ' + ad), txt: 'Distributiva: ' + o.a + ' × 100 = ' + o.a * 100 + ' y ' + o.a + ' × ' + ad + ' = ' + o.a * ad + '.' }, { vis: RS(o.a * 100 + sg2 + o.a * ad + ' = ' + o.a * o.b), txt: 'Dos cuentas fáciles en lugar de una difícil.' }]; }
      if (md === 'division' || md === 'relacion') { var q = Math.floor(o.D / o.d), r = o.D % o.d, cuenta = '<table class="lb2-tab"><tr><th>Dividendo</th><th>Divisor</th><th>Cociente</th><th>Resto</th></tr><tr><td>' + o.D + '</td><td>' + o.d + '</td><td>' + q + '</td><td>' + r + '</td></tr></table>';
        if (md === 'division') return [{ vis: R1(o.D + ' ÷ ' + o.d), txt: 'Repartimos <b>' + o.D + '</b> (dividendo) en grupos de <b>' + o.d + '</b> (divisor).' }, { vis: R1(o.d + ' × ' + q + ' = ' + o.d * q), txt: 'Entran <b>' + q + '</b> grupos (cociente): ' + o.d + ' × ' + q + ' = ' + o.d * q + '.' }, { vis: R1(o.D + ' − ' + o.d * q + ' = ' + r), txt: 'Sobran <b>' + r + '</b> (resto). El resto siempre es menor que el divisor.' }, { vis: cuenta, txt: r ? 'Como sobra algo, la división no es exacta.' : 'Resto 0: la división es <b>exacta</b>.' }];
        return [{ vis: cuenta, txt: 'Las cuatro partes de la división.' }, { vis: cuenta + R1(o.d + ' × ' + q + ' + ' + r), txt: 'Divisor por cociente, más el resto…' }, { vis: cuenta + RS(o.d + ' × ' + q + ' + ' + r + ' = ' + o.D), txt: '…da el dividendo: <b>D = d × c + r</b>, con el resto menor que el divisor.' }, { vis: cuenta + RS(o.D + ' − ' + r + ' = ' + (o.D - r) + ' → ' + (o.D - r) + ' ÷ ' + o.d + ' = ' + q), txt: 'Así se comprueba una división, y si falta un dato se puede despejar.' }]; }
      if (md === 'falta') { var rr = Math.min(o.r, o.d - 1), DD = o.d * o.q + rr;
        return [{ vis: '<table class="lb2-tab"><tr><th>Dividendo</th><th>Divisor</th><th>Cociente</th><th>Resto</th></tr><tr><td>?</td><td>' + o.d + '</td><td>' + o.q + '</td><td>' + rr + '</td></tr></table>', txt: 'Falta el <b>dividendo</b>. Sabemos el divisor, el cociente y el resto' + (rr !== o.r ? ' (el resto tiene que ser menor que ' + o.d + ')' : '') + '.' }, { vis: R1('D = d × c + r'), txt: 'Usamos la relación fundamental.' }, { vis: R1('D = ' + o.d + ' × ' + o.q + ' + ' + rr), txt: 'Reemplazamos los datos.' }, { vis: RS('D = ' + (o.d * o.q) + ' + ' + rr + ' = ' + DD), txt: 'Control: ' + DD + ' ÷ ' + o.d + ' da ' + o.q + ' y sobran ' + rr + '.' }]; }
      if (md === 'redondear') { var L = LUGR[o.k - 1], u = L[1], x = Math.round(o.x), lo = Math.floor(x / u) * u, hi = lo + u, sigc = Math.floor(x % u / (u / 10)), r3 = sigc >= 5 ? hi : lo;
        return [{ vis: R1(fmt(x)), txt: 'Lo redondeamos a las <b>' + L[0] + '</b>.' }, { vis: R1(fmt(lo) + ' ← ' + fmt(x) + ' → ' + fmt(hi)), txt: 'Está entre <b>' + fmt(lo) + '</b> y <b>' + fmt(hi) + '</b>.' }, { vis: R1(fmt(x)), txt: 'Miramos la cifra siguiente al lugar: es <b>' + sigc + '</b>. ' + (sigc >= 5 ? 'Es 5 o más: sube.' : 'Es menor que 5: queda igual.') }, { vis: RS(fmt(x) + ' ≈ ' + fmt(r3)), txt: 'Ese es el redondeo.' }]; }
      if (md === 'estimar') { var ra = Math.round(o.a / 100) * 100, rb = Math.round(o.b / 100) * 100;
        return [{ vis: R1(o.a + ' + ' + o.b), txt: 'Antes de calcular, estimamos.' }, { vis: R1(o.a + ' ≈ ' + ra + ' · ' + o.b + ' ≈ ' + rb), txt: 'Redondeamos cada número a las centenas.' }, { vis: R1(ra + ' + ' + rb + ' = ' + (ra + rb)), txt: 'Hacemos la cuenta con los redondeados: es fácil y da un resultado <b>aproximado</b>.' }, { vis: RS(o.a + ' + ' + o.b + ' = ' + (o.a + o.b)), txt: 'La cuenta exacta da cerca de ' + (ra + rb) + ': el resultado es <b>razonable</b>.' }]; }
      if (md === 'pasos') { var g = o.n * o.pr, vu = o.pa - g;
        return [{ vis: R1(o.n + ' cuadernos de $' + fmt(o.pr) + ' · pago con $' + fmt(o.pa)), txt: '¿Cuánto me dan de vuelto? Primero, los datos.' }, { vis: R1(o.n + ' × ' + fmt(o.pr) + ' = ' + fmt(g)), txt: 'Paso 1: cuánto gasto en total.' },
          vu >= 0 ? { vis: RS(fmt(o.pa) + ' − ' + fmt(g) + ' = $' + fmt(vu)), txt: 'Paso 2: al pago le resto el gasto. Ese es el vuelto.' } : { vis: RS('Faltan $' + fmt(-vu)), txt: 'Paso 2: el gasto es mayor que lo que pago: no alcanza.' },
          { vis: RS('≈ ' + o.n + ' × ' + fmt(Math.round(o.pr / 100) * 100) + ' = ' + fmt(o.n * Math.round(o.pr / 100) * 100)), txt: 'Control: estimando, el gasto da cerca de lo calculado. Es razonable.' }]; }
      return [];
    });
  } };
  M.naturales_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'asociativa';
    respuesta(el, api, function () {
      if (md === 'asociativa') { var a = R(11, 89), c = R(12, 88), b = (10 - a % 10) % 10 + R(1, 6) * 10; return { cons: 'Calculá agrupando lo que da redondo: <b>' + a + ' + ' + c + ' + ' + b + '</b>', campos: [{ v: a + b + c }], ayuda: 'Fijate qué dos números juntos dan un número terminado en 0: ' + a + ' + ' + b + '.', bien: '¡Bien! ' + a + ' + ' + b + ' = ' + (a + b) + ' y + ' + c + ' = ' + (a + b + c) + '.' }; }
      if (md === 'inversa') { var x = R(20, 400), y = R(10, 300), z = x + y, cual = Math.random() < .5; return { cons: 'Sabiendo que <b>' + x + ' + ' + y + ' = ' + z + '</b>, ¿cuánto es <b>' + z + ' − ' + (cual ? y : x) + '</b>? (sin hacer la cuenta)', campos: [{ v: cual ? x : y }], ayuda: 'La resta deshace la suma: si al total le sacás uno de los sumandos, queda el otro.', bien: '¡Bien! Queda el otro sumando.' }; }
      if (md === 'descomposicion' || md === 'compensacion') { var a2 = R(20, 199), b2 = md === 'compensacion' ? R(1, 9) * 10 + pick([8, 9]) : R(12, 89); return { cons: 'Calculá mentalmente: <b>' + a2 + ' + ' + b2 + '</b>', campos: [{ v: a2 + b2 }], ayuda: md === 'compensacion' ? 'Sumá ' + (b2 + (10 - b2 % 10)) + ' y después sacá los ' + (10 - b2 % 10) + ' de más.' : 'Sumá primero ' + (b2 - b2 % 10) + ' y después ' + b2 % 10 + '.', bien: '¡Bien! Da ' + (a2 + b2) + '.' }; }
      if (md === 'multiplicar') { var f = R(3, 9), c3 = R(2, 9); return { cons: '<b>' + Array(f + 1).join(c3 + ' + ').slice(0, -3) + '</b> es lo mismo que una multiplicación. Completá: ___ × ' + c3 + ' = ___', campos: [{ lab: 'veces', v: f }, { lab: 'resultado', v: f * c3 }], ayuda: 'Contá cuántas veces se suma el ' + c3 + '.', bien: '¡Bien! ' + f + ' × ' + c3 + ' = ' + f * c3 + '.' }; }
      if (md === 'distributiva') { var m = R(3, 9), d = R(2, 9) * 10, u = R(1, 9), rs = p.op === 'resta', t = rs ? d - u : d + u, s2 = rs ? ' − ' : ' + ';
        return { cons: 'Completá: <b>' + m + ' × ' + t + ' = ' + m + ' × (' + d + s2 + u + ') = ' + m + ' × ' + d + s2 + m + ' × ' + u + ' = ___' + s2 + '___ = ___</b>', campos: [{ v: m * d }, { v: m * u }, { v: m * t }], ayuda: 'Multiplicá el ' + m + ' por cada término y después ' + (rs ? 'restá.' : 'sumá.'), bien: '¡Bien! ' + m * d + s2 + m * u + ' = ' + m * t + '.' }; }
      if (md === 'mental') { var m2 = R(3, 9), n = 100 + pick([-3, -2, -1, 1, 2, 3]); return { cons: 'Calculá con la distributiva: <b>' + m2 + ' × ' + n + '</b>', campos: [{ v: m2 * n }], ayuda: 'Pensá ' + n + ' como 100 ' + (n < 100 ? '− ' + (100 - n) : '+ ' + (n - 100)) + ': ' + m2 + ' × 100 ' + (n < 100 ? '−' : '+') + ' ' + m2 + ' × ' + Math.abs(n - 100) + '.', bien: '¡Bien! Da ' + m2 * n + '.' }; }
      if (md === 'division') { var D = R(20, 300), dv = R(3, 12); return { cons: 'Hacé la división <b>' + D + ' ÷ ' + dv + '</b>.', campos: [{ lab: 'cociente', v: Math.floor(D / dv) }, { lab: 'resto', v: D % dv }], ayuda: 'Buscá cuántas veces entra ' + dv + ' en ' + D + '; lo que sobra es el resto (menor que ' + dv + ').', bien: '¡Bien! ' + dv + ' × ' + Math.floor(D / dv) + ' + ' + D % dv + ' = ' + D + '.' }; }
      if (md === 'relacion') { var dv2 = R(3, 15), q = R(5, 40), r = R(0, dv2 - 1), D2 = dv2 * q + r, falta = pick(['D', 'r']);
        if (falta === 'D') return { cons: 'En una división el divisor es <b>' + dv2 + '</b>, el cociente <b>' + q + '</b> y el resto <b>' + r + '</b>. ¿Cuál es el dividendo?', campos: [{ v: D2 }], ayuda: 'D = d × c + r = ' + dv2 + ' × ' + q + ' + ' + r + '.', bien: '¡Bien! ' + D2 + '.' };
        return { cons: 'En una división el dividendo es <b>' + D2 + '</b>, el divisor <b>' + dv2 + '</b> y el cociente <b>' + q + '</b>. ¿Cuál es el resto?', campos: [{ v: r }], ayuda: 'r = D − d × c = ' + D2 + ' − ' + dv2 * q + '.', bien: '¡Bien! El resto es ' + r + '.' }; }
      if (md === 'redondear') { var L = pick(LUGR), x2 = R(1000, 99999), rr = Math.round(x2 / L[1]) * L[1]; return { cons: 'Redondeá <b>' + fmt(x2) + '</b> a las <b>' + L[0] + '</b>.', campos: [{ v: rr }], ayuda: 'Mirá la cifra que sigue a las ' + L[0] + ': si es 5 o más, sube; si no, queda igual.', bien: '¡Bien! ≈ ' + fmt(rr) + '.' }; }
      if (md === 'estimar') { var e1 = R(110, 890), e2 = R(110, 890); return { cons: 'Estimá <b>' + e1 + ' + ' + e2 + '</b> redondeando cada número a las centenas.', campos: [{ v: Math.round(e1 / 100) * 100 + Math.round(e2 / 100) * 100 }], ayuda: e1 + ' ≈ ' + Math.round(e1 / 100) * 100 + ' y ' + e2 + ' ≈ ' + Math.round(e2 / 100) * 100 + '.', bien: '¡Bien! Es una estimación: la cuenta exacta da ' + (e1 + e2) + '.' }; }
      var n3 = R(2, 6), pr = R(2, 9) * 100 + pick([0, 50]), pa = Math.ceil(n3 * pr / 1000) * 1000 + pick([0, 1000]);
      return { cons: 'Compro <b>' + n3 + '</b> entradas de <b>$' + fmt(pr) + '</b> y pago con <b>$' + fmt(pa) + '</b>. ¿Cuánto me dan de vuelto?', campos: [{ v: pa - n3 * pr, un: '$' }], ayuda: 'Paso 1: gasto total = ' + n3 + ' × ' + fmt(pr) + '. Paso 2: pago − gasto.', bien: '¡Bien! $' + fmt(pa - n3 * pr) + '.' };
    });
  } };

  // ======= POTENCIAS Y RAÍCES CON NATURALES (Matemática I · Misión 3) =======
  function sup(n) { return String(n).split('').map(function (d) { return SUP[+d]; }).join(''); }
  function fac(b, n) { return n ? Array(n + 1).join(b + ' · ').slice(0, -3) : '1'; }
  function cuadr(n, s) { s = s || Math.min(22, 180 / n); var g = ''; for (var i = 0; i < n; i++) for (var j = 0; j < n; j++) g += '<rect x="' + (4 + j * s) + '" y="' + (4 + i * s) + '" width="' + (s - 2) + '" height="' + (s - 2) + '" class="c1"/>'; return '<svg viewBox="0 0 ' + (8 + n * s) + ' ' + (8 + n * s) + '" class="lb2-svg" style="max-height:170px">' + g + '</svg>'; }
  M.potencias_n = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'potencia', C = {
      potencia: ctrl('b', 'Base', 1, 10, 1, 3) + ctrl('e', 'Exponente', 0, 6, 1, 4),
      cuadrado_cubo: ctrl('n', 'Número', 1, 6, 1, 3),
      crecen: ctrl('n', 'Hasta', 3, 8, 1, 6),
      producto: ctrl('b', 'Base', 2, 5, 1, 2) + ctrl('m', 'Primer exponente', 1, 4, 1, 3) + ctrl('n', 'Segundo exponente', 1, 4, 1, 2),
      cociente: ctrl('b', 'Base', 2, 5, 1, 3) + ctrl('m', 'Exponente de arriba', 2, 6, 1, 5) + ctrl('n', 'Exponente de abajo', 1, 5, 1, 2),
      potencia_potencia: ctrl('b', 'Base', 2, 5, 1, 2) + ctrl('m', 'Exponente de adentro', 1, 4, 1, 3) + ctrl('n', 'Exponente de afuera', 1, 3, 1, 2),
      distributiva: ctrl('a', 'Primer factor', 2, 6, 1, 2) + ctrl('b', 'Segundo factor', 2, 6, 1, 5) + ctrl('n', 'Exponente', 2, 3, 1, 2),
      no_suma: ctrl('a', 'Primer número', 1, 9, 1, 3) + ctrl('b', 'Segundo número', 1, 9, 1, 4),
      raiz_cubica: ctrl('n', 'Número', 1, 1000, 1, 216),
      raiz_grande: ctrl('k', 'Raíz chica', 1, 12, 1, 6) + ctrl('c', 'Ceros (pares)', 2, 4, 2, 2),
      lado_area: ctrl('l', 'Lado (cm)', 1, 12, 1, 5),
      arista_volumen: ctrl('a', 'Arista (cm)', 1, 6, 1, 3),
      perfectos: ctrl('n', 'Número', 1, 1000, 1, 64) }[md];
    escena(el, C, function (o) {
      var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
      if (md === 'potencia') { var b = o.b, e = o.e, P = [{ vis: G(b + sup(e)), txt: 'La <b>base</b> es ' + b + ' (el número que se multiplica) y el <b>exponente</b> es ' + e + ' (cuántas veces).' }];
        if (e === 0) P.push({ vis: RS(b + '⁰ = 1'), txt: 'Con exponente 0 la potencia vale <b>1</b> (con cualquier base distinta de 0).' });
        else if (e === 1) P.push({ vis: RS(b + '¹ = ' + b), txt: 'Con exponente 1 queda la misma base.' });
        else { for (var i = 2; i <= e; i++) P.push({ vis: F(fac(b, i)) + G('= ' + fmt(Math.pow(b, i))), txt: i === 2 ? 'Multiplicamos la base por sí misma.' : 'Otra vez por ' + b + '.' }); P.push({ vis: RS(b + sup(e) + ' = ' + fac(b, e) + ' = ' + fmt(Math.pow(b, e))), txt: 'No es ' + b + ' × ' + e + ' = ' + b * e + ': el exponente no multiplica a la base.' }); }
        return P; }
      if (md === 'cuadrado_cubo') { var n = o.n; return [{ vis: cuadr(n), txt: 'Un cuadrado de <b>' + n + '</b> por <b>' + n + '</b>.' }, { vis: cuadr(n) + RS(n + '² = ' + n + ' · ' + n + ' = ' + n * n), txt: 'Tiene ' + n * n + ' cuadraditos: por eso n² se lee «' + n + ' al cuadrado».' }, { vis: F(n + ' capas de ' + n * n) + G(n + '³'), txt: 'Si apilamos <b>' + n + '</b> capas iguales, armamos un cubo.' }, { vis: RS(n + '³ = ' + n + ' · ' + n + ' · ' + n + ' = ' + n * n * n), txt: 'Tiene ' + n * n * n + ' cubitos: por eso n³ se lee «' + n + ' al cubo».' }]; }
      if (md === 'crecen') { var N = o.n, filas = function (k) { var h = '<table class="lb2-tab"><tr><th>n</th><th>n²</th><th>2ⁿ</th></tr>'; for (var i = 1; i <= N; i++) h += '<tr><td>' + i + '</td><td>' + (k >= 1 ? i * i : '') + '</td><td>' + (k >= 2 ? Math.pow(2, i) : '') + '</td></tr>'; return h + '</table>'; };
        return [{ vis: filas(0), txt: 'Comparamos dos formas de crecer.' }, { vis: filas(1), txt: '<b>n²</b>: el número por sí mismo.' }, { vis: filas(2), txt: '<b>2ⁿ</b>: el 2 multiplicado n veces. Al principio es más chico…' }, { vis: filas(2), txt: '…pero cuando el exponente crece, la potencia crece muy rápido: cada paso <b>duplica</b>.' }]; }
      if (md === 'producto') { var b2 = o.b, m = o.m, n2 = o.n; return [{ vis: G(b2 + sup(m) + ' · ' + b2 + sup(n2)), txt: 'Un producto de potencias con la <b>misma base</b>.' }, { vis: F('(' + fac(b2, m) + ') · (' + fac(b2, n2) + ')'), txt: 'Escribimos los factores: ' + m + ' y ' + n2 + '.' }, { vis: F(fac(b2, m + n2)), txt: 'En total hay <b>' + (m + n2) + '</b> factores ' + b2 + '.' }, { vis: RS(b2 + sup(m) + ' · ' + b2 + sup(n2) + ' = ' + b2 + sup(m + n2) + ' = ' + fmt(Math.pow(b2, m + n2))), txt: 'Se deja la base y se <b>suman</b> los exponentes.' }]; }
      if (md === 'cociente') { var b3 = o.b, m3 = o.m, n3 = Math.min(o.n, o.m - 1), arr = Array(m3 + 1).join(b3 + ' · ').slice(0, -3).split(' · ').map(function (x, i) { return i < n3 ? '<s>' + x + '</s>' : x; }).join(' · '), abj = Array(n3 + 1).join('<s>' + b3 + '</s> · ').slice(0, -3);
        return [{ vis: G(b3 + sup(m3) + ' : ' + b3 + sup(n3)), txt: 'Un cociente de potencias con la misma base.' }, { vis: F(fac(b3, m3) + '<br>÷<br>' + fac(b3, n3)), txt: 'Arriba hay ' + m3 + ' factores y abajo ' + n3 + '.' }, { vis: F(arr + '<br>÷<br>' + abj), txt: 'Cada factor de abajo se simplifica con uno de arriba.' }, { vis: RS(b3 + sup(m3) + ' : ' + b3 + sup(n3) + ' = ' + b3 + sup(m3 - n3) + ' = ' + fmt(Math.pow(b3, m3 - n3))), txt: 'Quedan ' + (m3 - n3) + ': se deja la base y se <b>restan</b> los exponentes.' }]; }
      if (md === 'potencia_potencia') { var b4 = o.b, m4 = o.m, n4 = o.n, grupos = Array(n4 + 1).join('(' + fac(b4, m4) + ') · ').slice(0, -3);
        return [{ vis: G('(' + b4 + sup(m4) + ')' + sup(n4)), txt: 'Una potencia elevada a otra potencia.' }, { vis: F(Array(n4 + 1).join(b4 + sup(m4) + ' · ').slice(0, -3)), txt: 'Es ' + b4 + sup(m4) + ' multiplicado ' + n4 + ' veces.' }, { vis: F(grupos), txt: n4 + ' grupos de ' + m4 + ' factores: <b>' + m4 * n4 + '</b> factores en total.' }, { vis: RS('(' + b4 + sup(m4) + ')' + sup(n4) + ' = ' + b4 + sup(m4 * n4) + ' = ' + fmt(Math.pow(b4, m4 * n4))), txt: 'Se deja la base y se <b>multiplican</b> los exponentes.' }]; }
      if (md === 'distributiva') { var a5 = o.a, b5 = o.b, n5 = o.n; return [{ vis: G('(' + a5 + ' · ' + b5 + ')' + sup(n5)), txt: 'Una potencia de un producto.' }, { vis: F(Array(n5 + 1).join('(' + a5 + ' · ' + b5 + ') · ').slice(0, -3)), txt: 'Escribimos los ' + n5 + ' factores.' }, { vis: F(a5 + sup(n5) + ' · ' + b5 + sup(n5) + ' = ' + Math.pow(a5, n5) + ' · ' + Math.pow(b5, n5)), txt: 'Juntamos los ' + a5 + ' y los ' + b5 + ': la potencia se <b>distribuye</b> en cada factor.' }, { vis: RS('(' + a5 * b5 + ')' + sup(n5) + ' = ' + fmt(Math.pow(a5 * b5, n5))), txt: 'Da lo mismo que multiplicar primero. También vale con la división exacta.' }]; }
      if (md === 'no_suma') { var a6 = o.a, b6 = o.b; return [{ vis: G('(' + a6 + ' + ' + b6 + ')²'), txt: '¿La potencia se distribuye en una <b>suma</b>?' }, { vis: G('(' + a6 + ' + ' + b6 + ')² = ' + (a6 + b6) + '² = ' + (a6 + b6) * (a6 + b6)), txt: 'Primero el paréntesis: ' + a6 + ' + ' + b6 + ' = ' + (a6 + b6) + '.' }, { vis: G(a6 + '² + ' + b6 + '² = ' + a6 * a6 + ' + ' + b6 * b6 + ' = ' + (a6 * a6 + b6 * b6)), txt: 'Si la repartiéramos daría otra cosa.' }, { vis: RS((a6 + b6) * (a6 + b6) + ' ≠ ' + (a6 * a6 + b6 * b6)), txt: 'Con la <b>suma y la resta NO</b> se puede distribuir.' }]; }
      if (md === 'raiz_cubica') { var n7 = o.n, k7 = 1; while ((k7 + 1) * (k7 + 1) * (k7 + 1) <= n7) k7++; var ex = k7 * k7 * k7 === n7, lista = []; for (var c = 1; c <= Math.min(k7 + 1, 10); c++) lista.push(c + '³ = ' + c * c * c);
        return [{ vis: G('∛' + n7), txt: 'Buscamos un número que multiplicado <b>tres veces</b> por sí mismo dé ' + n7 + '.' }, { vis: F(lista.join(' · ')), txt: 'Probamos con los cubos: 1, 8, 27, 64…' }, { vis: RS(ex ? '∛' + n7 + ' = ' + k7 + ' porque ' + k7 + '³ = ' + n7 : '∛' + n7 + ' está entre ' + k7 + ' y ' + (k7 + 1)), txt: ex ? n7 + ' es un <b>cubo perfecto</b>.' : 'No es un cubo perfecto: la raíz no es exacta.' }]; }
      if (md === 'raiz_grande') { var k8 = o.k, z = Math.pow(10, o.c), N8 = k8 * k8 * z, rz = k8 * Math.pow(10, o.c / 2);
        return [{ vis: G('√' + fmt(N8)), txt: 'Un número grande terminado en ceros.' }, { vis: G('√(' + k8 * k8 + ' · ' + fmt(z) + ')'), txt: 'Lo separamos en un número conocido por 1 seguido de ceros (una cantidad par).' }, { vis: G('√' + k8 * k8 + ' · √' + fmt(z) + ' = ' + k8 + ' · ' + fmt(Math.pow(10, o.c / 2))), txt: 'Calculamos cada raíz: la de ' + fmt(z) + ' tiene la mitad de ceros.' }, { vis: RS('√' + fmt(N8) + ' = ' + fmt(rz)), txt: 'Control: ' + fmt(rz) + ' · ' + fmt(rz) + ' = ' + fmt(N8) + '.' }]; }
      if (md === 'lado_area') { var l = o.l; return [{ vis: cuadr(l), txt: 'Un cuadrado de lado <b>' + l + ' cm</b>.' }, { vis: cuadr(l) + RS('A = ' + l + '² = ' + l * l + ' cm²'), txt: 'Su área es el lado al cuadrado.' }, { vis: cuadr(l) + RS('l = √' + l * l + ' = ' + l + ' cm'), txt: 'Al revés: si sabés el área, el lado es la <b>raíz cuadrada</b>.' }]; }
      if (md === 'arista_volumen') { var a9 = o.a; return [{ vis: F(a9 + ' × ' + a9 + ' × ' + a9) + G('cubo de arista ' + a9 + ' cm'), txt: 'Un cubo: todas sus aristas miden <b>' + a9 + ' cm</b>.' }, { vis: RS('V = ' + a9 + '³ = ' + a9 * a9 * a9 + ' cm³'), txt: 'Su volumen es la arista al cubo: ' + a9 * a9 + ' cubitos por capa y ' + a9 + ' capas.' }, { vis: RS('a = ∛' + a9 * a9 * a9 + ' = ' + a9 + ' cm'), txt: 'Al revés: si sabés el volumen, la arista es la <b>raíz cúbica</b>.' }]; }
      var n0 = o.n, q = Math.round(Math.sqrt(n0)), cb = Math.round(Math.cbrt(n0)), esC = q * q === n0, esK = cb * cb * cb === n0;
      return [{ vis: G(String(n0)), txt: '¿Es un cuadrado perfecto? ¿Y un cubo perfecto?' }, { vis: F(esC ? q + '² = ' + n0 : Math.floor(Math.sqrt(n0)) + '² = ' + Math.pow(Math.floor(Math.sqrt(n0)), 2) + ' y ' + (Math.floor(Math.sqrt(n0)) + 1) + '² = ' + Math.pow(Math.floor(Math.sqrt(n0)) + 1, 2)), txt: esC ? 'Es <b>cuadrado perfecto</b>: ' + q + ' × ' + q + '.' : 'No es cuadrado perfecto: queda entre dos cuadrados.' }, { vis: F(esK ? cb + '³ = ' + n0 : 'ningún natural al cubo da ' + n0), txt: esK ? 'Es <b>cubo perfecto</b>: ' + cb + ' × ' + cb + ' × ' + cb + '.' : 'No es cubo perfecto.' }];
    });
  } };
  M.potencias_n_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'potencia';
    respuesta(el, api, function () {
      if (md === 'potencia') { var b = R(2, 10), e = pick([0, 1, 2, 2, 3, 3, 4]); if (b > 5 && e > 3) e = 3; return { cons: '¿Cuánto es <b>' + b + sup(e) + '</b>?', campos: [{ v: Math.pow(b, e) }], ayuda: e === 0 ? 'Con exponente 0 la potencia vale 1.' : 'Multiplicá ' + b + ' por sí mismo ' + e + ' veces: ' + fac(b, e) + '.', bien: '¡Bien! ' + b + sup(e) + ' = ' + Math.pow(b, e) + '.' }; }
      if (md === 'base_exp') { var b1 = R(2, 9), e1 = R(2, 6); return { cons: 'Escribí como potencia: <b>' + fac(b1, e1) + '</b>', campos: [{ lab: 'base', v: b1 }, { lab: 'exponente', v: e1 }], ayuda: 'La base es el número que se repite; el exponente, cuántas veces.', bien: '¡Bien! ' + b1 + sup(e1) + '.' }; }
      if (md === 'cuadrado_cubo') { var n = R(2, 12), cu = Math.random() < .4 && n <= 9; return { cons: '¿Cuánto es <b>' + n + (cu ? '³' : '²') + '</b>?', campos: [{ v: cu ? n * n * n : n * n }], ayuda: cu ? n + ' · ' + n + ' · ' + n + '.' : n + ' · ' + n + '.', bien: '¡Bien!' }; }
      if (md === 'producto' || md === 'cociente' || md === 'potencia_potencia') { var b2 = R(2, 9), m = R(2, 7), n2 = R(1, md === 'cociente' ? m - 1 : 5), ex2 = md === 'producto' ? m + n2 : md === 'cociente' ? m - n2 : m * n2, txt = md === 'producto' ? b2 + sup(m) + ' · ' + b2 + sup(n2) : md === 'cociente' ? b2 + sup(m) + ' : ' + b2 + sup(n2) : '(' + b2 + sup(m) + ')' + sup(n2);
        return { cons: 'Escribí como una sola potencia: <b>' + txt + ' = ' + b2 + '</b> elevado a ___', campos: [{ lab: 'exponente', v: ex2 }], ayuda: md === 'producto' ? 'Misma base que se multiplica: se suman los exponentes.' : md === 'cociente' ? 'Misma base que se divide: se restan los exponentes.' : 'Potencia de potencia: se multiplican los exponentes.', bien: '¡Bien! ' + b2 + sup(ex2) + '.' }; }
      if (md === 'distributiva') { var a = R(2, 5), c = R(2, 5), n3 = R(2, 3); return { cons: 'Calculá distribuyendo la potencia: <b>(' + a + ' · ' + c + ')' + sup(n3) + '</b>', campos: [{ lab: a + sup(n3), v: Math.pow(a, n3) }, { lab: c + sup(n3), v: Math.pow(c, n3) }, { lab: 'resultado', v: Math.pow(a * c, n3) }], ayuda: '(' + a + ' · ' + c + ')' + sup(n3) + ' = ' + a + sup(n3) + ' · ' + c + sup(n3) + '.', bien: '¡Bien!' }; }
      if (md === 'no_suma') { var x = R(1, 7), y = R(1, 7); return { cons: 'Calculá <b>(' + x + ' + ' + y + ')²</b>. Ojo: con la suma no se distribuye.', campos: [{ v: (x + y) * (x + y) }], ayuda: 'Primero el paréntesis: ' + x + ' + ' + y + ' = ' + (x + y) + '; después al cuadrado.', bien: '¡Bien! ' + (x + y) + '² = ' + (x + y) * (x + y) + '.' }; }
      if (md === 'raiz_cuadrada' || md === 'raiz_cubica') { var k = md === 'raiz_cubica' ? R(1, 10) : R(1, 20), N = md === 'raiz_cubica' ? k * k * k : k * k; return { cons: 'Calculá <b>' + (md === 'raiz_cubica' ? '∛' : '√') + N + '</b>', campos: [{ v: k }], ayuda: 'Buscá un número que ' + (md === 'raiz_cubica' ? 'multiplicado tres veces' : 'multiplicado por sí mismo') + ' dé ' + N + '.', bien: '¡Bien! ' + (md === 'raiz_cubica' ? k + '³' : k + '²') + ' = ' + N + '.' }; }
      if (md === 'raiz_grande') { var k2 = R(2, 12), z = pick([100, 10000]); return { cons: 'Calculá <b>√' + fmt(k2 * k2 * z) + '</b>', campos: [{ v: k2 * Math.sqrt(z) }], ayuda: 'Separá: √' + k2 * k2 + ' · √' + fmt(z) + '.', bien: '¡Bien! ' + fmt(k2 * Math.sqrt(z)) + '.' }; }
      if (md === 'estimar_raiz') { var n4; do { n4 = R(5, 150); } while (Math.sqrt(n4) % 1 === 0); var f4 = Math.floor(Math.sqrt(n4)); return { cons: '<b>√' + n4 + '</b> no es exacta. ¿Entre qué dos números naturales está?', campos: [{ lab: 'entre', v: f4 }, { lab: 'y', v: f4 + 1 }], ayuda: 'Buscá los cuadrados que lo rodean: ' + f4 + '² = ' + f4 * f4 + ' y ' + (f4 + 1) + '² = ' + (f4 + 1) * (f4 + 1) + '.', bien: '¡Bien!' }; }
      if (md === 'lado_area') { var l = R(2, 15), inv = Math.random() < .5; return inv ? { cons: 'Un cuadrado tiene <b>' + l * l + ' cm²</b> de área. ¿Cuánto mide su lado?', campos: [{ v: l, un: 'cm' }], ayuda: 'El lado es la raíz cuadrada del área: √' + l * l + '.', bien: '¡Bien! ' + l + ' cm.' } : { cons: 'Un cuadrado tiene <b>' + l + ' cm</b> de lado. ¿Cuál es su área?', campos: [{ v: l * l, un: 'cm²' }], ayuda: 'Área = lado² = ' + l + ' · ' + l + '.', bien: '¡Bien! ' + l * l + ' cm².' }; }
      if (md === 'arista_volumen') { var a2 = R(2, 10), inv2 = Math.random() < .5; return inv2 ? { cons: 'Una caja cúbica tiene <b>' + a2 * a2 * a2 + ' cm³</b> de volumen. ¿Cuánto mide su arista?', campos: [{ v: a2, un: 'cm' }], ayuda: 'La arista es la raíz cúbica del volumen.', bien: '¡Bien! ' + a2 + ' cm.' } : { cons: 'Un cubo tiene <b>' + a2 + ' cm</b> de arista. ¿Cuál es su volumen?', campos: [{ v: a2 * a2 * a2, un: 'cm³' }], ayuda: 'Volumen = arista³.', bien: '¡Bien! ' + a2 * a2 * a2 + ' cm³.' }; }
      var n5 = pick([R(2, 15) * R(2, 15), R(10, 200)]), r5 = Math.round(Math.sqrt(n5)), es5 = r5 * r5 === n5;
      return { cons: '¿<b>' + n5 + '</b> es un cuadrado perfecto? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: es5 ? ['si', 'sí'] : ['no'] }], ayuda: 'Buscá un número que multiplicado por sí mismo dé ' + n5 + '.', bien: es5 ? '¡Bien! ' + r5 + '² = ' + n5 + '.' : '¡Bien! No hay ninguno.' };
    });
  } };

  // Calculadora (Matemática I · Misión 4, nivel 4)
  M.calculadora = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'comun';
    el.innerHTML = '<div class="lb-vista"></div><div class="lb-pie"><button type="button" class="lb-btn suave" data-o="1">🔄 Otra cuenta</button></div>'; var v = el.querySelector('.lb-vista');
    var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, pant = function (x) { return '<div class="lb2-calc">' + x + '</div>'; };
    function armar() { var a = R(2, 9), b = R(2, 9), c = R(2, 9), P;
      if (md === 'comun') P = [{ vis: G(a + ' + ' + b + ' × ' + c), txt: 'Tipeamos la cuenta tal cual, tecla por tecla.' }, { vis: G(a + ' + ' + b + ' × ' + c) + pant((a + b) * c), txt: 'Una calculadora <b>común</b> resuelve a medida que tipeás: hizo ' + a + ' + ' + b + ' = ' + (a + b) + ' y después × ' + c + '.' }, { vis: G(a + ' + ' + b + ' × ' + c) + pant(a + b * c), txt: 'Una calculadora <b>científica</b> respeta la jerarquía: primero ' + b + ' × ' + c + '.' }, { vis: RS(a + ' + ' + b + ' × ' + c + ' = ' + (a + b * c)), txt: 'El resultado correcto es el de la científica. Con una común, hay que hacer primero la multiplicación.' }];
      else if (md === 'estimar') { var x = R(31, 89) * 10 + R(1, 9), y = R(21, 79), ex = x * y, rx = Math.round(x / 100) * 100, ry = Math.round(y / 10) * 10;
        P = [{ vis: G(fmt(x) + ' × ' + y), txt: 'Antes de usar la calculadora, estimamos.' }, { vis: G(fmt(rx) + ' × ' + ry + ' = ' + fmt(rx * ry)), txt: 'Redondeamos y hacemos la cuenta de cabeza: da cerca de <b>' + fmt(rx * ry) + '</b>.' }, { vis: G(fmt(x) + ' × ' + y) + pant(fmt(ex)), txt: 'Ahora sí, la calculadora.' }, { vis: RS(fmt(ex) + ' ≈ ' + fmt(rx * ry)), txt: 'El resultado está cerca de la estimación: es razonable.' }]; }
      else { var x2 = R(21, 89), y2 = R(11, 49), bien = x2 * y2, mal = x2 * 10 * y2;
        P = [{ vis: G(x2 + ' × ' + y2), txt: 'Queremos calcular esta cuenta con la calculadora.' }, { vis: G(x2 + '0 × ' + y2) + pant(fmt(mal)), txt: 'Sin darnos cuenta tipeamos un 0 de más.' }, { vis: G('≈ ' + Math.round(x2 / 10) * 10 + ' × ' + Math.round(y2 / 10) * 10 + ' = ' + fmt(Math.round(x2 / 10) * 10 * Math.round(y2 / 10) * 10)), txt: 'La estimación da mucho menos: <b>algo está mal</b>.' }, { vis: pant(fmt(bien)) + RS(x2 + ' × ' + y2 + ' = ' + fmt(bien)), txt: 'Volvemos a tipear con cuidado. Estimar sirve para detectar errores de tipeo.' }]; }
      pasoAPaso(v, P); }
    el.addEventListener('click', function (e) { if (e.target.closest('[data-o]')) armar(); }); armar();
  } };
  M.calculadora_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'comun';
    respuesta(el, api, function () { var a = R(2, 9), b = R(2, 9), c = R(2, 9);
      if (md === 'comun') return { cons: 'Una calculadora <b>común</b> muestra <b>' + (a + b) * c + '</b> para <b>' + a + ' + ' + b + ' × ' + c + '</b>. ¿Cuál es el resultado correcto?', campos: [{ v: a + b * c }], ayuda: 'La común sumó primero. Respetá la jerarquía: primero ' + b + ' × ' + c + '.', bien: '¡Bien! ' + a + ' + ' + b * c + ' = ' + (a + b * c) + '.' };
      var x = R(21, 89) * 10, y = R(21, 79), rx = Math.round(x / 100) * 100, ry = Math.round(y / 10) * 10;
      if (md === 'estimar') return { cons: 'Estimá <b>' + fmt(x) + ' × ' + y + '</b> redondeando a ' + fmt(rx) + ' y ' + ry + '.', campos: [{ v: rx * ry }], ayuda: fmt(rx) + ' × ' + ry + '.', bien: '¡Bien! La cuenta exacta da ' + fmt(x * y) + ', cerca de tu estimación.' };
      var mal = Math.random() < .5, mostrado = mal ? x * y * 10 : x * y;
      return { cons: 'Para <b>' + fmt(x) + ' × ' + y + '</b> la calculadora mostró <b>' + fmt(mostrado) + '</b>. Estimá: ¿es razonable? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: mal ? ['no'] : ['si', 'sí'] }], ayuda: 'Estimá: ' + fmt(rx) + ' × ' + ry + ' = ' + fmt(rx * ry) + '. ¿El resultado está cerca?', bien: mal ? '¡Bien! Tiene un cero de más.' : '¡Bien! Está cerca de la estimación.' }; });
  } };

  // ======= DIVISIBILIDAD (Matemática I · Misión 5) =======
  function divs(n) { var o = []; for (var i = 1; i <= n; i++) if (n % i === 0) o.push(i); return o; }
  M.divis = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'patron', C = {
      patron: ctrl('a', 'Una luz titila cada (s)', 2, 9, 1, 4) + ctrl('b', 'Otra cada (s)', 2, 9, 1, 6),
      suma: ctrl('d', 'Divisor', 2, 9, 1, 7) + ctrl('x', 'Primer múltiplo (veces)', 1, 9, 1, 3) + ctrl('y', 'Segundo múltiplo (veces)', 1, 9, 1, 5),
      multiplo: ctrl('d', 'Divisor', 2, 9, 1, 4) + ctrl('a', 'Número que divide (veces el divisor)', 1, 9, 1, 3) + ctrl('k', 'Lo multiplicamos por', 2, 9, 1, 5),
      contraejemplo: ctrl('d', '«Todo número divisible por…', 2, 6, 1, 3) + ctrl('e', '…también es divisible por…»', 2, 12, 1, 6),
      reparto: ctrl('n', 'Cantidad para repartir', 6, 60, 1, 24),
      cual: ctrl('a', 'Primer dato', 4, 30, 1, 12) + ctrl('b', 'Segundo dato', 4, 30, 1, 18),
      pistas: ctrl('m', 'Es múltiplo de', 2, 9, 1, 3) + ctrl('v', 'Es divisor de', 12, 100, 1, 60) + ctrl('g', 'Es mayor que', 1, 30, 1, 10) }[md];
    escena(el, C, function (o) {
      var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
      if (md === 'patron') { var tope = Math.min(60, o.a * o.b), m = o.a * o.b / mcd(o.a, o.b);
        var tira = function (k) { var h = '<div class="lb2-tira">'; for (var i = 1; i <= Math.min(tope, 36); i++) { var A = i % o.a === 0, B = i % o.b === 0; h += '<span class="' + (k >= 1 && A ? 'a' : '') + (k >= 2 && B ? ' b' : '') + (k >= 3 && A && B ? ' ab' : '') + '">' + i + '</span>'; } return h + '</div>'; };
        return [{ vis: tira(0), txt: 'Los segundos, uno por uno.' }, { vis: tira(1), txt: 'Una luz titila en los <b>múltiplos de ' + o.a + '</b>.' }, { vis: tira(2), txt: 'La otra, en los <b>múltiplos de ' + o.b + '</b>.' }, { vis: tira(3) + RS('Coinciden cada ' + m + ' s'), txt: 'Titilan juntas en los <b>múltiplos comunes</b>: el primero es ' + m + ', y después se repite.' }]; }
      if (md === 'suma') { var a = o.d * o.x, b = o.d * o.y, gr = function (n, cls) { var h = ''; for (var i = 0; i < n / o.d; i++) h += '<i class="' + cls + '">' + o.d + '</i>'; return h; };
        return [{ vis: G(a + ' y ' + b), txt: o.d + ' divide a ' + a + ' y a ' + b + ': se arman grupos justos de ' + o.d + '.' }, { vis: '<div class="lb2-grupos">' + gr(a, 'g1') + '</div><div class="lb2-grupos">' + gr(b, 'g2') + '</div>', txt: a + ' son ' + o.x + ' grupos de ' + o.d + ', y ' + b + ' son ' + o.y + ' grupos.' }, { vis: '<div class="lb2-grupos">' + gr(a, 'g1') + gr(b, 'g2') + '</div>', txt: 'Si juntamos todo, siguen siendo grupos justos: ' + (o.x + o.y) + ' grupos.' }, { vis: RS(o.d + ' divide a ' + a + ' + ' + b + ' = ' + (a + b)), txt: 'Si un número divide a dos números, divide a su suma (y a su resta).' }]; }
      if (md === 'multiplo') { var n = o.d * o.a; return [{ vis: G(o.d + ' divide a ' + n), txt: n + ' = ' + o.d + ' × ' + o.a + '.' }, { vis: G(n + ' × ' + o.k + ' = ' + n * o.k), txt: 'Multiplicamos ' + n + ' por ' + o.k + '.' }, { vis: G(n * o.k + ' = ' + o.d + ' × ' + o.a * o.k), txt: 'El ' + o.d + ' sigue estando como factor.' }, { vis: RS(o.d + ' divide a ' + n * o.k), txt: 'Si un número divide a otro, divide a todos sus múltiplos.' }]; }
      if (md === 'contraejemplo') { var d = o.d, e = o.e, hall = null; for (var i = d; i <= d * 30 && hall === null; i += d) if (i % e) hall = i; var pr = []; for (var j = d; j <= (hall || d * 6) && pr.length < 6; j += d) pr.push(j + (j % e ? ' ✘' : ' ✔'));
        return [{ vis: G('¿Todo múltiplo de ' + d + ' es múltiplo de ' + e + '?'), txt: 'Una afirmación sobre <b>todos</b> los números.' }, { vis: F(pr.join(' · ')), txt: 'Probamos con múltiplos de ' + d + ' y miramos si ' + e + ' los divide.' }, hall ? { vis: RS(hall + ' es múltiplo de ' + d + ' pero no de ' + e), txt: 'Encontramos un <b>contraejemplo</b>: alcanza uno solo para saber que la afirmación es falsa.' } : { vis: RS('Siempre se cumple'), txt: 'No aparece ningún contraejemplo: acá la afirmación es verdadera (' + e + ' divide a ' + d + '), y se justifica con un razonamiento, no solo con ejemplos.' }]; }
      if (md === 'reparto') { var n2 = o.n, D = divs(n2); return [{ vis: G(n2 + ' caramelos'), txt: '¿En cuántas bolsitas iguales se pueden repartir sin que sobre ninguno?' }, { vis: F(n2 + ' ÷ 5 = ' + Math.floor(n2 / 5) + ', resto ' + n2 % 5), txt: n2 % 5 ? 'En 5 bolsitas sobran ' + n2 % 5 + ': no sirve.' : 'En 5 bolsitas no sobra nada: sirve.' }, { vis: F(D.join(' · ')), txt: 'Sirven justo los <b>divisores de ' + n2 + '</b>.' }, { vis: RS(D.length + ' formas de repartir'), txt: 'Repartir sin sobrantes es buscar divisores.' }]; }
      if (md === 'cual') { var mc = o.a * o.b / mcd(o.a, o.b), md2 = mcd(o.a, o.b);
        return [{ vis: G(o.a + ' y ' + o.b), txt: 'Con estos dos datos pueden aparecer dos tipos de problema.' }, { vis: F('Cortar cintas de ' + o.a + ' y ' + o.b + ' cm en trozos iguales, sin que sobre'), txt: 'El trozo tiene que <b>entrar justo</b> en los dos: es un <b>divisor común</b> (más chico que los datos).' }, { vis: F('Dos colectivos salen cada ' + o.a + ' y ' + o.b + ' min. ¿Cuándo coinciden?'), txt: 'El momento tiene que ser <b>múltiplo</b> de los dos: es un <b>múltiplo común</b> (más grande que los datos).' }, { vis: RS('Trozo más largo: ' + md2 + ' cm · Coinciden a los ' + mc + ' min'), txt: 'Preguntate: ¿la respuesta divide a los datos o es múltiplo de ellos?' }]; }
      var cand = [], todos = divs(o.v); var mul = todos.filter(function (x) { return x % o.m === 0; }), fin = mul.filter(function (x) { return x > o.g; });
      return [{ vis: F('Divisores de ' + o.v + ': ' + todos.join(', ')), txt: 'Pista 1: es divisor de ' + o.v + '. Escribimos todos.' }, { vis: F('Múltiplos de ' + o.m + ': ' + (mul.join(', ') || 'ninguno')), txt: 'Pista 2: de esos, nos quedamos con los múltiplos de ' + o.m + '.' }, { vis: RS(fin.length ? 'Puede ser: ' + fin.join(', ') : 'Ningún número cumple todo'), txt: 'Pista 3: mayor que ' + o.g + '. Cada pista achica la lista.' }];
    });
  } };
  M.divis_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'multiplo_n';
    respuesta(el, api, function () {
      if (md === 'multiplo_n') { var n = R(3, 15), k = R(4, 12); return { cons: 'Si el primer múltiplo de <b>' + n + '</b> (sin contar el 0) es ' + n + ', ¿cuál es el múltiplo número <b>' + k + '</b>?', campos: [{ v: n * k }], ayuda: 'El múltiplo número ' + k + ' es ' + n + ' × ' + k + '.', bien: '¡Bien! ' + n * k + '.' }; }
      if (md === 'repite') { var a = pick([2, 3, 4, 5, 6]), b = pick([4, 6, 8, 9, 10]); while (a === b) b = pick([4, 6, 8, 9, 10]); var m = a * b / mcd(a, b); return { cons: 'Una luz titila cada <b>' + a + ' segundos</b> y otra cada <b>' + b + '</b>. Si titilan juntas ahora, ¿dentro de cuántos segundos vuelven a titilar juntas?', campos: [{ v: m, un: 's' }], ayuda: 'Buscá el primer múltiplo común de ' + a + ' y ' + b + ' (sin contar el 0).', bien: '¡Bien! A los ' + m + ' segundos.' }; }
      if (md === 'cuantos_div') { var n2 = pick([12, 16, 18, 20, 24, 28, 30, 36, 40, 45, 48]); return { cons: '¿Cuántos divisores tiene <b>' + n2 + '</b>?', campos: [{ v: divs(n2).length }], ayuda: 'Buscalos por parejas: 1 × ' + n2 + ', 2 × …', bien: '¡Bien! ' + divs(n2).join(', ') + '.' }; }
      if (md === 'suma' || md === 'multiplo') { var d = R(3, 9), x = R(2, 9), y = R(2, 9), A = d * x, B = d * y, k = R(2, 9);
        return md === 'suma' ? { cons: '<b>' + d + '</b> divide a <b>' + A + '</b> y a <b>' + B + '</b>. Sin hacer la cuenta, ¿cuántas veces entra ' + d + ' en ' + A + ' + ' + B + '?', campos: [{ v: x + y }], ayuda: A + ' son ' + x + ' grupos de ' + d + ' y ' + B + ' son ' + y + ' grupos.', bien: '¡Bien! ' + (x + y) + ' grupos: ' + d + ' divide a la suma.' } : { cons: '<b>' + d + '</b> divide a <b>' + A + '</b>. ¿Cuántas veces entra ' + d + ' en ' + A + ' × ' + k + '?', campos: [{ v: x * k }], ayuda: A + ' = ' + d + ' × ' + x + ', así que ' + A + ' × ' + k + ' = ' + d + ' × ' + x * k + '.', bien: '¡Bien! Divide también a sus múltiplos.' }; }
      if (md === 'contraejemplo') { var pr = pick([[2, 4], [3, 6], [2, 6], [3, 9], [5, 10], [4, 8]]); return { cons: 'Encontrá un contraejemplo: «Todo número divisible por <b>' + pr[0] + '</b> también es divisible por <b>' + pr[1] + '</b>». Escribí un múltiplo de ' + pr[0] + ' que NO sea múltiplo de ' + pr[1] + ' (menor que 50).', campos: [{ v: pr[0], acepta: function (x) { return x > 0 && x < 50 && x % pr[0] === 0 && x % pr[1] !== 0; } }], ayuda: 'Probá con los múltiplos de ' + pr[0] + ': ' + pr[0] + ', ' + 2 * pr[0] + ', ' + 3 * pr[0] + '…', bien: '¡Bien! Con un solo contraejemplo alcanza.' }; }
      if (md === 'reparto') { var n3 = pick([12, 18, 20, 24, 30, 36, 40]), g = pick(divs(n3).filter(function (x) { return x > 1 && x < n3; })); return { cons: 'Hay <b>' + n3 + '</b> figuritas para repartir en <b>' + g + '</b> sobres iguales, sin que sobre ninguna. ¿Cuántas van en cada sobre?', campos: [{ v: n3 / g }], ayuda: n3 + ' ÷ ' + g + '.', bien: '¡Bien! ' + g + ' divide a ' + n3 + '.' }; }
      if (md === 'cual') { var a2 = pick([8, 12, 15, 18]), b2 = pick([20, 24, 30, 36]); var tipo = Math.random() < .5; return tipo ? { cons: 'Se cortan cintas de <b>' + a2 + '</b> y <b>' + b2 + ' cm</b> en trozos iguales, lo más largos posible, sin que sobre nada. ¿Cuánto mide cada trozo?', campos: [{ v: mcd(a2, b2), un: 'cm' }], ayuda: 'El trozo tiene que dividir a los dos: buscá el mayor divisor común.', bien: '¡Bien! ' + mcd(a2, b2) + ' cm.' } : { cons: 'Dos colectivos salen juntos, uno cada <b>' + a2 + '</b> y otro cada <b>' + b2 + '</b> minutos. ¿A los cuántos minutos vuelven a salir juntos?', campos: [{ v: a2 * b2 / mcd(a2, b2), un: 'min' }], ayuda: 'Tiene que ser múltiplo de los dos: buscá el menor múltiplo común.', bien: '¡Bien! A los ' + a2 * b2 / mcd(a2, b2) + ' minutos.' }; }
      var m3 = pick([3, 4, 5, 6]), v3 = pick([24, 36, 48, 60, 72]), g3 = R(5, 20), ok = divs(v3).filter(function (x) { return x % m3 === 0 && x > g3; }); if (!ok.length) { g3 = 1; ok = divs(v3).filter(function (x) { return x % m3 === 0; }); }
      return { cons: 'Pensé un número: es <b>múltiplo de ' + m3 + '</b>, es <b>divisor de ' + v3 + '</b> y es <b>mayor que ' + g3 + '</b>. Escribí uno que cumpla todo.', campos: [{ v: ok[0], acepta: function (x) { return ok.indexOf(x) >= 0; } }], ayuda: 'Escribí los divisores de ' + v3 + ', quedate con los múltiplos de ' + m3 + ' y después con los mayores que ' + g3 + '.', bien: '¡Bien! Podían ser: ' + ok.join(', ') + '.' };
    });
  } };

  // ======= CRITERIOS Y FACTORIZACIÓN (Matemática I · Misiones 6 y 7) =======
  function primo(n) { if (n < 2) return false; for (var i = 2; i * i <= n; i++) if (n % i === 0) return false; return true; }
  function fact(n) { var o = {}, f = 2; while (n > 1) { while (n % f === 0) { o[f] = (o[f] || 0) + 1; n /= f; } f++; } return o; }
  function factTxt(F) { return Object.keys(F).map(function (k) { return k + (F[k] > 1 ? sup(F[k]) : ''); }).join(' · ') || '1'; }
  M.criterios = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || '2_5_10';
    escena(el, ctrl('n', 'Número', 10, 99999, 1, pick([4572, 2310, 7128, 1386])), function (o) {
      var n = Math.round(o.n), s = String(n), u = +s.slice(-1), G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, si = function (b) { return b ? '✔ sí' : '✘ no'; };
      var sum = s.split('').reduce(function (a, b) { return a + +b; }, 0), d2 = +s.slice(-2), d3 = +s.slice(-3);
      if (md === '2_5_10') return [{ vis: G(fmt(n)), txt: 'Para 2, 5 y 10 alcanza con mirar la <b>última cifra</b>: ' + u + '.' }, { vis: G('… ' + u) + RS('por 2: ' + si(u % 2 === 0)), txt: 'Por 2: termina en cifra par (0, 2, 4, 6, 8).' }, { vis: G('… ' + u) + RS('por 5: ' + si(u % 5 === 0)), txt: 'Por 5: termina en 0 o en 5.' }, { vis: G('… ' + u) + RS('por 10: ' + si(u === 0)), txt: 'Por 10: termina en 0.' }];
      if (md === '3_9') return [{ vis: G(fmt(n)), txt: 'Para 3 y 9 sumamos <b>todas las cifras</b>.' }, { vis: G(s.split('').join(' + ') + ' = ' + sum), txt: 'La suma de las cifras es ' + sum + '.' }, { vis: RS('por 3: ' + si(sum % 3 === 0)), txt: 'Es divisible por 3 si la suma es múltiplo de 3.' }, { vis: RS('por 9: ' + si(sum % 9 === 0)), txt: 'Es divisible por 9 si la suma es múltiplo de 9.' }];
      if (md === '4_8') return [{ vis: G(fmt(n)), txt: 'Para 4 miramos las dos últimas cifras; para 8, las tres últimas.' }, { vis: G('… ' + (s.length > 1 ? s.slice(-2) : s)) + RS('por 4: ' + si(d2 % 4 === 0)), txt: s.slice(-2) + (d2 % 4 === 0 ? ' es' : ' no es') + ' múltiplo de 4.' }, { vis: G('… ' + (s.length > 2 ? s.slice(-3) : s)) + RS('por 8: ' + si(d3 % 8 === 0)), txt: s.slice(-3) + (d3 % 8 === 0 ? ' es' : ' no es') + ' múltiplo de 8.' }];
      if (md === '6') return [{ vis: G(fmt(n)), txt: '6 = 2 × 3: hay que mirar los dos criterios.' }, { vis: RS('por 2: ' + si(u % 2 === 0)), txt: 'Por 2: ¿termina en cifra par?' }, { vis: RS('por 3: ' + si(sum % 3 === 0)), txt: 'Por 3: la suma de las cifras es ' + sum + '.' }, { vis: RS('por 6: ' + si(n % 6 === 0)), txt: 'Es divisible por 6 solo si cumple <b>los dos</b>.' }];
      var imp = 0, par = 0; s.split('').reverse().forEach(function (d, i) { if (i % 2) par += +d; else imp += +d; });
      if (md === '11') return [{ vis: G(fmt(n)), txt: 'Para 11 sumamos las cifras de lugares alternados, desde la derecha.' }, { vis: G('lugares impares: ' + imp + ' · lugares pares: ' + par), txt: 'Una suma con las cifras 1.ª, 3.ª, 5.ª… y otra con 2.ª, 4.ª…' }, { vis: G('Diferencia: ' + Math.abs(imp - par)), txt: 'Restamos las dos sumas.' }, { vis: RS('por 11: ' + si(Math.abs(imp - par) % 11 === 0)), txt: 'Es divisible por 11 si la diferencia es 0 o múltiplo de 11.' }];
      var tab = '<table class="lb2-tab"><tr>' + [2, 3, 4, 5, 6, 9, 10].map(function (k) { return '<th>' + k + '</th>'; }).join('') + '</tr><tr>' + [2, 3, 4, 5, 6, 9, 10].map(function (k) { return '<td class="' + (n % k ? '' : 'on') + '">' + (n % k ? '✘' : '✔') + '</td>'; }).join('') + '</tr></table>';
      return [{ vis: G(fmt(n)), txt: 'Aplicamos varios criterios al mismo número.' }, { vis: G('última cifra ' + u + ' · suma de cifras ' + sum), txt: 'Dos datos alcanzan para casi todo: la última cifra y la suma de las cifras.' }, { vis: tab, txt: 'Marcamos por cuáles es divisible.' }];
    });
  } };
  M.criterios_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || '2_5_10', K = { '2_5_10': [2, 5, 10], '3_9': [3, 9], '4_8': [4, 8], '6': [6], '11': [11], combinar: [2, 3, 4, 5, 6, 9] }[md] || [2];
    respuesta(el, api, function () { var k = pick(K), n = Math.random() < .5 ? k * R(50, 2000) : R(100, 20000), es = n % k === 0;
      return { cons: '¿<b>' + fmt(n) + '</b> es divisible por <b>' + k + '</b>? Usá el criterio y escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: es ? ['si', 'sí'] : ['no'] }], ayuda: { 2: 'Mirá si termina en cifra par.', 5: 'Mirá si termina en 0 o 5.', 10: 'Mirá si termina en 0.', 3: 'Sumá las cifras: ¿es múltiplo de 3?', 9: 'Sumá las cifras: ¿es múltiplo de 9?', 4: 'Mirá las dos últimas cifras.', 8: 'Mirá las tres últimas cifras.', 6: 'Tiene que ser divisible por 2 y por 3.', 11: 'Restá las sumas de cifras alternadas.' }[k], bien: es ? '¡Bien! Sí es divisible.' : '¡Bien! No es divisible.' }; });
  } };
  M.factores = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'criba', C = { criba: ctrl('n', 'Hasta', 20, 60, 10, 50), esprimo: ctrl('n', 'Número', 2, 400, 1, 91), divisores: ctrl('a', 'Exponente del 2', 0, 4, 1, 2) + ctrl('b', 'Exponente del 3', 0, 3, 1, 1) + ctrl('c', 'Exponente del 5', 0, 2, 1, 1),
      mcd_desc: ctrl('a', 'Un número', 4, 200, 1, 60) + ctrl('b', 'Otro número', 4, 200, 1, 84), mcm_desc: ctrl('a', 'Un número', 4, 100, 1, 12) + ctrl('b', 'Otro número', 4, 100, 1, 18), producto: ctrl('a', 'Un número', 2, 60, 1, 12) + ctrl('b', 'Otro número', 2, 60, 1, 18),
      tres: ctrl('a', 'Primero', 2, 60, 1, 12) + ctrl('b', 'Segundo', 2, 60, 1, 18) + ctrl('c', 'Tercero', 2, 60, 1, 30) }[md];
    escena(el, C, function (o) {
      var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
      if (md === 'criba') { var N = o.n, tira = function (hasta) { var h = '<div class="lb2-tira">'; for (var i = 2; i <= N; i++) { var tach = false; for (var q = 2; q <= hasta; q++) if (primo(q) && i !== q && i % q === 0) tach = true; h += '<span class="' + (tach ? 'b' : (hasta > 7 && primo(i) ? 'ab' : '')) + '" style="' + (tach ? 'text-decoration:line-through;opacity:.45' : '') + '">' + i + '</span>'; } return h + '</div>'; };
        return [{ vis: tira(1), txt: 'Escribimos los números del 2 al ' + N + '.' }, { vis: tira(2), txt: 'El 2 es primo: tachamos sus múltiplos.' }, { vis: tira(3), txt: 'El 3 es primo: tachamos sus múltiplos.' }, { vis: tira(5), txt: 'Lo mismo con el 5.' }, { vis: tira(N), txt: 'Y con el 7. Los que quedan sin tachar son los <b>primos</b>.' }]; }
      if (md === 'esprimo') { var n = o.n, raiz = Math.floor(Math.sqrt(n)), d = null, pr = []; for (var k = 2; k <= raiz; k++) { if (primo(k)) pr.push(k); if (d === null && n % k === 0) d = k; }
        return [{ vis: G(String(n)), txt: '¿Es primo? Probamos dividirlo por los primos.' }, { vis: F('√' + n + ' ≈ ' + raiz + ' → probamos: ' + (pr.join(', ') || 'ninguno')), txt: 'Alcanza con probar hasta la raíz cuadrada del número.' }, d ? { vis: RS(n + ' = ' + d + ' × ' + n / d + ' → compuesto'), txt: 'Lo divide el ' + d + ': no es primo.' } : { vis: RS(n + ' es primo'), txt: 'Ninguno lo divide: es <b>primo</b>.' }]; }
      if (md === 'divisores') { var a = o.a, b = o.b, c = o.c, N2 = Math.pow(2, a) * Math.pow(3, b) * Math.pow(5, c), F2 = '2' + sup(a) + ' · 3' + sup(b) + ' · 5' + sup(c);
        return [{ vis: G(fmt(N2) + ' = ' + F2), txt: 'El número ya está descompuesto en factores primos.' }, { vis: F('el 2 puede aparecer 0 a ' + a + ' veces → ' + (a + 1) + ' opciones'), txt: 'Cada divisor elige cuántas veces usa cada primo.' }, { vis: F((a + 1) + ' × ' + (b + 1) + ' × ' + (c + 1)), txt: 'Sumamos 1 a cada exponente y multiplicamos.' }, { vis: RS(fmt(N2) + ' tiene ' + (a + 1) * (b + 1) * (c + 1) + ' divisores'), txt: 'Así se cuentan sin escribirlos todos.' }]; }
      if (md === 'mcd_desc' || md === 'mcm_desc' || md === 'producto') { var A = o.a, B = o.b, FA = fact(A), FB = fact(B), K = {}, M2 = {}; Object.keys(FA).concat(Object.keys(FB)).forEach(function (k) { if (FA[k] && FB[k]) K[k] = Math.min(FA[k], FB[k]); M2[k] = Math.max(FA[k] || 0, FB[k] || 0); });
        var g = mcd(A, B), l = A * B / g, P = [{ vis: F(A + ' = ' + factTxt(FA)) + F(B + ' = ' + factTxt(FB)), txt: 'Descomponemos los dos números en factores primos.' }];
        if (md === 'mcd_desc') return P.concat([{ vis: F('comunes: ' + (factTxt(K) === '1' ? 'ninguno' : factTxt(K))), txt: 'MCD: los factores <b>comunes</b>, con el <b>menor</b> exponente.' }, { vis: RS('MCD(' + A + ', ' + B + ') = ' + g), txt: g === 1 ? 'Da 1: los números son <b>coprimos</b>.' : 'Multiplicamos esos factores.' }]);
        if (md === 'mcm_desc') return P.concat([{ vis: F('todos: ' + factTxt(M2)), txt: 'MCM: <b>todos</b> los factores, comunes y no comunes, con el <b>mayor</b> exponente.' }, { vis: RS('MCM(' + A + ', ' + B + ') = ' + l), txt: 'Multiplicamos esos factores.' }]);
        return [{ vis: G(A + ' y ' + B), txt: 'Dos números.' }, { vis: F('MCD = ' + g + ' · MCM = ' + l), txt: 'Calculamos su MCD y su MCM.' }, { vis: F(g + ' × ' + l + ' = ' + g * l + ' · ' + A + ' × ' + B + ' = ' + A * B), txt: 'Multiplicamos MCD por MCM, y los números entre sí.' }, { vis: RS('MCD × MCM = a × b'), txt: 'Siempre da lo mismo: si sabés tres datos, calculás el cuarto.' }]; }
      var a3 = o.a, b3 = o.b, c3 = o.c, g3 = mcd(mcd(a3, b3), c3), l1 = a3 * b3 / mcd(a3, b3), l3 = l1 * c3 / mcd(l1, c3);
      return [{ vis: G(a3 + ', ' + b3 + ' y ' + c3), txt: 'Con tres números se trabaja de a dos.' }, { vis: F('MCD(' + a3 + ', ' + b3 + ') = ' + mcd(a3, b3) + ' → MCD(' + mcd(a3, b3) + ', ' + c3 + ') = ' + g3), txt: 'MCD: el de los dos primeros, y después con el tercero.' }, { vis: F('MCM(' + a3 + ', ' + b3 + ') = ' + l1 + ' → MCM(' + l1 + ', ' + c3 + ') = ' + l3), txt: 'MCM: lo mismo.' }, { vis: RS('MCD = ' + g3 + ' · MCM = ' + l3), txt: 'También se puede con la descomposición de los tres.' }];
    });
  } };
  M.factores_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'esprimo';
    respuesta(el, api, function () {
      if (md === 'esprimo') { var n = pick([R(20, 150), pick([23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])]), es = primo(n); return { cons: '¿<b>' + n + '</b> es primo? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: es ? ['si', 'sí'] : ['no'] }], ayuda: 'Probá dividirlo por 2, 3, 5, 7… hasta √' + n + '.', bien: es ? '¡Bien! Es primo.' : '¡Bien! Es compuesto.' }; }
      if (md === 'desc') { var a = R(1, 4), b = R(0, 2), c = R(0, 1), N = Math.pow(2, a) * Math.pow(3, b) * Math.pow(5, c); return { cons: 'Descomponé <b>' + N + '</b> = 2 elevado a ___ · 3 elevado a ___ · 5 elevado a ___', campos: [{ lab: '2', v: a }, { lab: '3', v: b }, { lab: '5', v: c }], ayuda: 'Dividí por 2 todas las veces que se pueda, después por 3 y por 5. Si un primo no está, su exponente es 0.', bien: '¡Bien! ' + N + ' = ' + factTxt(fact(N)) + '.' }; }
      if (md === 'cuantos') { var a2 = R(1, 4), b2 = R(1, 2), c2 = R(0, 1), N2 = Math.pow(2, a2) * Math.pow(3, b2) * Math.pow(5, c2); return { cons: '<b>' + fmt(N2) + ' = ' + factTxt(fact(N2)) + '</b>. ¿Cuántos divisores tiene?', campos: [{ v: (a2 + 1) * (b2 + 1) * (c2 + 1) }], ayuda: 'Sumá 1 a cada exponente y multiplicá.', bien: '¡Bien!' }; }
      var A = pick([12, 18, 20, 24, 30, 36, 40, 42, 45, 48, 60]), B = pick([8, 15, 16, 27, 28, 32, 35, 54, 56, 72, 90]); if (A === B) B = 50;
      var g = mcd(A, B), l = A * B / g;
      if (md === 'mcd') return { cons: 'Calculá el <b>MCD(' + A + ', ' + B + ')</b>.', campos: [{ v: g }], ayuda: 'Factores comunes con el menor exponente.', bien: '¡Bien! ' + g + '.' };
      if (md === 'mcm') return { cons: 'Calculá el <b>MCM(' + A + ', ' + B + ')</b>.', campos: [{ v: l }], ayuda: 'Todos los factores con el mayor exponente.', bien: '¡Bien! ' + l + '.' };
      if (md === 'coprimos') { var x = pick([8, 9, 14, 15, 21, 25, 16, 27]), y = pick([9, 10, 12, 14, 20, 35, 22, 49]); return { cons: '¿<b>' + x + '</b> y <b>' + y + '</b> son coprimos? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: mcd(x, y) === 1 ? ['si', 'sí'] : ['no'] }], ayuda: 'Son coprimos si su único divisor común es 1.', bien: '¡Bien! MCD = ' + mcd(x, y) + '.' }; }
      if (md === 'producto') return { cons: 'Dos números multiplicados dan <b>' + A * B + '</b> y su MCD es <b>' + g + '</b>. ¿Cuál es su MCM?', campos: [{ v: l }], ayuda: 'MCD × MCM = a × b, así que MCM = ' + A * B + ' ÷ ' + g + '.', bien: '¡Bien! ' + l + '.' };
      var C2 = pick([6, 10, 15, 20, 30]), g3 = mcd(mcd(A, B), C2), l1 = l * C2 / mcd(l, C2), mcm3 = Math.random() < .5;
      return { cons: 'Calculá el <b>' + (mcm3 ? 'MCM' : 'MCD') + '(' + A + ', ' + B + ', ' + C2 + ')</b>.', campos: [{ v: mcm3 ? l1 : g3 }], ayuda: 'Hacelo de a dos: primero con ' + A + ' y ' + B + ', y el resultado con ' + C2 + '.', bien: '¡Bien!' };
    });
  } };

  // ======= FRACCIONES (Matemática I · Misiones 8 y 9) =======
  function fb(n, d, cls) { var h = ''; for (var i = 0; i < Math.max(d, n); i++) h += '<i class="' + (i < n ? (cls || 'p1') : '') + (i >= d ? ' fuera' : '') + '"></i>'; return '<div class="lb2-fb">' + h + '</div>'; }
  function simp(a, b) { var g = mcd(a, b) || 1; return [a / g, b / g]; }
  M.fracciones = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'parte', C = {
      parte: ctrl('a', 'Partes pintadas', 0, 12, 1, 3) + ctrl('b', 'Partes iguales en total', 2, 12, 1, 8),
      cociente: ctrl('a', 'Chocolates', 1, 9, 1, 3) + ctrl('b', 'Chicos', 2, 8, 1, 4),
      tipos: ctrl('a', 'Numerador', 1, 30, 1, 11) + ctrl('b', 'Denominador', 2, 9, 1, 4),
      equivalentes: ctrl('a', 'Numerador', 1, 5, 1, 2) + ctrl('b', 'Denominador', 2, 6, 1, 3) + ctrl('k', 'Multiplicar por', 2, 4, 1, 2),
      irreducible: ctrl('a', 'Numerador', 2, 60, 1, 18) + ctrl('b', 'Denominador', 2, 90, 1, 24),
      cruzados: ctrl('a', 'a', 1, 9, 1, 2) + ctrl('b', 'b', 2, 12, 1, 3) + ctrl('c', 'c', 1, 12, 1, 4) + ctrl('d', 'd', 2, 18, 1, 6),
      recta: ctrl('a', 'Numerador', 1, 20, 1, 7) + ctrl('b', 'Denominador', 2, 8, 1, 4),
      entre: ctrl('a', 'Numerador de la primera', 1, 5, 1, 1) + ctrl('c', 'Numerador de la segunda', 2, 6, 1, 2) + ctrl('b', 'Denominador (de las dos)', 2, 8, 1, 4),
      comparar: ctrl('a', 'a', 1, 9, 1, 3) + ctrl('b', 'b', 2, 9, 1, 4) + ctrl('c', 'c', 1, 9, 1, 5) + ctrl('d', 'd', 2, 9, 1, 6),
      referentes: ctrl('a', 'Numerador', 1, 12, 1, 5) + ctrl('b', 'Denominador', 2, 12, 1, 8),
      mixtos: ctrl('e', 'Entero 1', 1, 4, 1, 2) + ctrl('a', 'Numerador 1', 1, 3, 1, 1) + ctrl('b', 'Denominador 1', 2, 4, 1, 3) + ctrl('f', 'Entero 2', 1, 4, 1, 1) + ctrl('c', 'Numerador 2', 1, 3, 1, 1) + ctrl('d', 'Denominador 2', 2, 4, 1, 2),
      inverso: ctrl('a', 'Numerador', 1, 9, 1, 3) + ctrl('b', 'Denominador', 1, 9, 1, 5),
      division: ctrl('t', 'Litros', 1, 6, 1, 3) + ctrl('d', 'Botellas de 1/…', 2, 5, 1, 4),
      combinadas: ctrl('b', 'Denominador', 2, 6, 1, 3),
      potencia: ctrl('a', 'Numerador', 1, 5, 1, 2) + ctrl('b', 'Denominador', 2, 6, 1, 3) + ctrl('n', 'Exponente', 2, 3, 1, 2) }[md];
    escena(el, C, function (o) {
      var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
      if (md === 'parte') { var a = Math.min(o.a, o.b); return [{ vis: fb(0, o.b), txt: 'Un entero partido en <b>' + o.b + '</b> partes <b>iguales</b>: el denominador.' }, { vis: fb(a, o.b), txt: 'Pintamos <b>' + a + '</b>: el numerador.' }, { vis: fb(a, o.b) + RS(fr(a, o.b)), txt: 'Se lee «' + a + ' ' + (o.b === 2 ? 'medios' : o.b === 3 ? 'tercios' : o.b === 4 ? 'cuartos' : o.b + (o.b === 10 ? ' décimos' : 'avos')) + '». Las partes tienen que ser iguales.' }]; }
      if (md === 'cociente') { var q = Math.floor(o.a / o.b), r = o.a % o.b; return [{ vis: G(o.a + ' chocolates ÷ ' + o.b + ' chicos'), txt: 'Repartimos en partes iguales.' }, { vis: F('Partimos cada chocolate en ' + o.b + ' partes'), txt: 'Cada chico recibe una parte de cada chocolate: ' + o.a + ' partes de ' + o.b + '.' }, { vis: RS(o.a + ' ÷ ' + o.b + ' = ' + fr(o.a, o.b)), txt: 'Una fracción es también una división: numerador ÷ denominador.' }]; }
      if (md === 'tipos') { var a2 = o.a, b2 = o.b, e = Math.floor(a2 / b2), r2 = a2 % b2;
        return [{ vis: G(fr(a2, b2)), txt: a2 < b2 ? 'El numerador es menor que el denominador: es una fracción <b>propia</b> (menor que 1).' : 'El numerador es mayor o igual que el denominador: es <b>impropia</b> (1 o más).' },
          a2 < b2 ? { vis: fb(a2, b2), txt: 'No llega a completar un entero.' } : { vis: F(a2 + ' ÷ ' + b2 + ' = ' + e + ', resto ' + r2), txt: 'Dividimos: entran <b>' + e + '</b> enteros y sobran <b>' + r2 + '</b> partes.' },
          { vis: RS(a2 < b2 ? fr(a2, b2) + ' < 1' : fr(a2, b2) + ' = ' + e + (r2 ? ' ' + fr(r2, b2) : '')), txt: a2 < b2 ? 'Las propias no se pasan a número mixto.' : 'Ese es el <b>número mixto</b>: entero y fracción.' }]; }
      if (md === 'equivalentes') { var A = o.a, B = Math.max(o.b, o.a + 1), k = o.k; return [{ vis: fb(A, B) + G(fr(A, B)), txt: 'Una fracción.' }, { vis: fb(A * k, B * k) + G(fr(A * k, B * k)), txt: 'Partimos cada parte en ' + k + ': multiplicamos numerador y denominador por <b>' + k + '</b>.' }, { vis: fb(A, B) + fb(A * k, B * k), txt: 'Lo pintado es lo mismo: son <b>equivalentes</b> (amplificar).' }, { vis: RS(fr(A * k, B * k) + ' = ' + fr(A, B)), txt: 'Al revés, dividir los dos por el mismo número es <b>simplificar</b>.' }]; }
      if (md === 'irreducible') { var g = mcd(o.a, o.b), S = simp(o.a, o.b); return [{ vis: G(fr(o.a, o.b)), txt: 'Queremos la fracción más simple equivalente.' }, { vis: F('MCD(' + o.a + ', ' + o.b + ') = ' + g), txt: 'Buscamos el máximo común divisor.' }, { vis: G(fr(o.a, o.b) + ' = ' + fr(o.a + ' ÷ ' + g, o.b + ' ÷ ' + g)), txt: 'Dividimos numerador y denominador por el MCD.' }, { vis: RS(fr(o.a, o.b) + ' = ' + fr(S[0], S[1])), txt: S[0] === o.a ? 'Ya era irreducible.' : 'Es <b>irreducible</b>: no se puede simplificar más.' }]; }
      if (md === 'cruzados') { var x = o.a * o.d, y = o.b * o.c; return [{ vis: G(fr(o.a, o.b) + ' ¿ = ? ' + fr(o.c, o.d)), txt: '¿Son equivalentes?' }, { vis: F(o.a + ' × ' + o.d + ' = ' + x), txt: 'Multiplicamos en cruz: numerador de una por denominador de la otra.' }, { vis: F(o.a + ' × ' + o.d + ' = ' + x + ' · ' + o.b + ' × ' + o.c + ' = ' + y), txt: 'Y al revés.' }, { vis: RS(x === y ? 'Iguales → equivalentes' : 'Distintos → no son equivalentes'), txt: 'Si los productos cruzados son iguales, las fracciones son equivalentes.' }]; }
      if (md === 'recta') { var a3 = o.a, b3 = o.b, ent = Math.ceil(a3 / b3) + 1, W = 280, X = function (v) { return 14 + v / ent * (W - 28); }, t = '';
        for (var k2 = 0; k2 <= ent * b3; k2++) t += '<line class="rayo" x1="' + X(k2 / b3) + '" y1="' + (k2 % b3 ? 30 : 24) + '" x2="' + X(k2 / b3) + '" y2="' + (k2 % b3 ? 40 : 46) + '"/>' + (k2 % b3 ? '' : '<text x="' + X(k2 / b3) + '" y="62">' + k2 / b3 + '</text>');
        var sv = function (pt) { return '<svg viewBox="0 0 ' + W + ' 70" class="lb2-svg"><line class="rayo" x1="8" y1="35" x2="' + (W - 8) + '" y2="35"/>' + t + (pt ? '<circle cx="' + X(a3 / b3) + '" cy="35" r="6" class="pt"/>' : '') + '</svg>'; };
        return [{ vis: sv(0), txt: 'Cada entero, partido en <b>' + b3 + '</b> partes iguales (el denominador).' }, { vis: sv(1), txt: 'Contamos <b>' + a3 + '</b> partes desde el 0 (el numerador).' }, { vis: sv(1) + RS(fr(a3, b3) + ' está entre ' + Math.floor(a3 / b3) + ' y ' + (Math.floor(a3 / b3) + 1)), txt: a3 > b3 ? 'Es impropia: pasa del 1.' : 'Es propia: está antes del 1.' }]; }
      if (md === 'entre') { var a4 = o.a, c4 = Math.max(o.c, o.a + 1), b4 = o.b; return [{ vis: G(fr(a4, b4) + ' y ' + fr(c4, b4)), txt: '¿Hay fracciones entre estas dos?' }, { vis: G(fr(2 * a4, 2 * b4) + ' y ' + fr(2 * c4, 2 * b4)), txt: 'Amplificamos las dos por 2: las partes quedan más chicas.' }, { vis: RS(fr(2 * a4 + 1, 2 * b4) + ' está entre ellas'), txt: 'Ahora aparece una en el medio. Siempre se puede seguir: entre dos fracciones hay infinitas.' }]; }
      if (md === 'comparar') { var a5 = o.a, b5 = o.b, c5 = o.c, d5 = o.d, m5 = b5 * d5 / mcd(b5, d5), A5 = a5 * m5 / b5, C5 = c5 * m5 / d5, sg = A5 > C5 ? '>' : A5 < C5 ? '<' : '=';
        if (b5 === d5) return [{ vis: G(fr(a5, b5) + ' ? ' + fr(c5, d5)), txt: 'Mismo denominador: las partes son del mismo tamaño.' }, { vis: RS(fr(a5, b5) + ' ' + sg + ' ' + fr(c5, d5)), txt: 'Es mayor la que tiene más partes (mayor numerador).' }];
        if (a5 === c5) return [{ vis: G(fr(a5, b5) + ' ? ' + fr(c5, d5)), txt: 'Mismo numerador: la misma cantidad de partes.' }, { vis: RS(fr(a5, b5) + ' ' + sg + ' ' + fr(c5, d5)), txt: 'Es mayor la que tiene partes más grandes (menor denominador).' }];
        return [{ vis: G(fr(a5, b5) + ' ? ' + fr(c5, d5)), txt: 'Distinto numerador y denominador.' }, { vis: F('MCM(' + b5 + ', ' + d5 + ') = ' + m5), txt: 'Buscamos un denominador común.' }, { vis: G(fr(A5, m5) + ' ? ' + fr(C5, m5)), txt: 'Las escribimos con ese denominador.' }, { vis: RS(fr(a5, b5) + ' ' + sg + ' ' + fr(c5, d5)), txt: 'Ahora comparamos los numeradores.' }]; }
      if (md === 'referentes') { var a6 = o.a, b6 = o.b, v6 = a6 / b6; return [{ vis: G(fr(a6, b6)), txt: 'La comparamos con dos referentes: 1/2 y 1.' }, { vis: F(a6 + ' frente a la mitad de ' + b6 + ' (' + fmt(b6 / 2) + ')'), txt: v6 > .5 ? 'El numerador es más de la mitad del denominador: es <b>mayor que 1/2</b>.' : v6 < .5 ? 'Es menos de la mitad: <b>menor que 1/2</b>.' : 'Es justo la mitad: <b>igual a 1/2</b>.' }, { vis: RS(v6 < 1 ? fr(a6, b6) + ' < 1' : v6 > 1 ? fr(a6, b6) + ' > 1' : fr(a6, b6) + ' = 1'), txt: 'Con el 1: ¿el numerador es menor, igual o mayor que el denominador?' }]; }
      if (md === 'mixtos') { var b7 = o.b, d7 = o.d, A7 = o.e * b7 + o.a, C7 = o.f * d7 + o.c, m7 = b7 * d7 / mcd(b7, d7), n7 = A7 * m7 / b7 + C7 * m7 / d7, S7 = simp(n7, m7), E7 = Math.floor(S7[0] / S7[1]), R7 = S7[0] % S7[1];
        return [{ vis: G(o.e + ' ' + fr(o.a, b7) + ' + ' + o.f + ' ' + fr(o.c, d7)), txt: 'Sumamos dos números mixtos.' }, { vis: G(fr(A7, b7) + ' + ' + fr(C7, d7)), txt: 'Los pasamos a fracción: entero × denominador + numerador.' }, { vis: G(fr(A7 * m7 / b7, m7) + ' + ' + fr(C7 * m7 / d7, m7) + ' = ' + fr(n7, m7)), txt: 'Denominador común y sumamos.' }, { vis: RS('= ' + E7 + (R7 ? ' ' + fr(R7, S7[1]) : '')), txt: 'Lo volvemos a escribir como número mixto.' }]; }
      if (md === 'inverso') { var a8 = Math.max(o.a, 1), b8 = Math.max(o.b, 1); return [{ vis: G(fr(a8, b8)), txt: 'Buscamos su <b>inverso</b>.' }, { vis: G(fr(b8, a8)), txt: 'Se dan vuelta numerador y denominador.' }, { vis: RS(fr(a8, b8) + ' × ' + fr(b8, a8) + ' = ' + fr(a8 * b8, a8 * b8) + ' = 1'), txt: 'Una fracción por su inverso da <b>1</b>.' }]; }
      if (md === 'division') { var t9 = o.t, d9 = o.d; return [{ vis: G(t9 + ' ÷ ' + fr(1, d9)), txt: '¿Cuántas botellas de ' + fr(1, d9) + ' litro se llenan con ' + t9 + ' litros?' }, { vis: fb(t9 * d9, t9 * d9), txt: 'Cada litro alcanza para <b>' + d9 + '</b> botellas.' }, { vis: G(t9 + ' × ' + d9 + ' = ' + t9 * d9), txt: 'Dividir por ' + fr(1, d9) + ' es multiplicar por su inverso, ' + d9 + '.' }, { vis: RS(t9 + ' ÷ ' + fr(1, d9) + ' = ' + t9 * d9), txt: 'Para dividir fracciones: se multiplica la primera por el inverso de la segunda.' }]; }
      if (md === 'combinadas') { var b10 = o.b; return [{ vis: G(fr(1, b10) + ' + ' + fr(2, b10) + ' × ' + fr(1, 2)), txt: 'La jerarquía es la misma que con naturales.' }, { vis: G(fr(1, b10) + ' + ' + fr(2, 2 * b10)), txt: 'Primero la multiplicación: ' + fr(2, b10) + ' × ' + fr(1, 2) + ' = ' + fr(2, 2 * b10) + '.' }, { vis: G(fr(1, b10) + ' + ' + fr(1, b10)), txt: 'Simplificamos: ' + fr(2, 2 * b10) + ' = ' + fr(1, b10) + '.' }, { vis: RS('= ' + fr(2, b10)), txt: 'Al final la suma.' }]; }
      var a11 = o.a, b11 = o.b, n11 = o.n; return [{ vis: G('(' + fr(a11, b11) + ')' + sup(n11)), txt: 'Una fracción elevada a una potencia.' }, { vis: G(Array(n11 + 1).join(fr(a11, b11) + ' × ').slice(0, -3)), txt: 'Se multiplica ' + n11 + ' veces por sí misma.' }, { vis: RS(fr(Math.pow(a11, n11), Math.pow(b11, n11))), txt: 'Se elevan el numerador y el denominador.' }];
    });
  } };
  M.fracciones_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'parte';
    respuesta(el, api, function () { var b = R(3, 10), a = R(1, b - 1), F = function (n, d) { return { tipo: 'frac', v: n / d, n: n, d: d }; };
      if (md === 'parte') return { cons: 'Un entero se partió en <b>' + b + '</b> partes iguales y se pintaron <b>' + a + '</b>. ¿Qué fracción está pintada?', html: fb(a, b), campos: [F(a, b)], ayuda: 'Numerador: partes pintadas. Denominador: partes en total.', bien: '¡Bien! ' + a + '/' + b + '.' };
      if (md === 'cociente') { var c = R(1, 9), k = R(2, 8); return { cons: 'Se reparten <b>' + c + '</b> pizzas en partes iguales entre <b>' + k + '</b> chicos. ¿Qué fracción de pizza le toca a cada uno?', campos: [F(c, k)], ayuda: 'Es ' + c + ' ÷ ' + k + '.', bien: '¡Bien! ' + c + '/' + k + '.' }; }
      if (md === 'tipos') { var d = R(2, 9), n = d * R(1, 4) + R(1, d - 1); return { cons: 'Escribí <b>' + n + '/' + d + '</b> como número mixto.', campos: [{ lab: 'enteros', v: Math.floor(n / d) }, { lab: 'resto (numerador)', v: n % d }], ayuda: n + ' ÷ ' + d + ': el cociente son los enteros y el resto es el numerador.', bien: '¡Bien! ' + Math.floor(n / d) + ' ' + n % d + '/' + d + '.' }; }
      if (md === 'equivalentes') { var k2 = R(2, 6); return { cons: 'Completá para que sean equivalentes: <b>' + a + '/' + b + ' = ___/' + b * k2 + '</b>', campos: [{ v: a * k2 }], ayuda: 'El denominador se multiplicó por ' + k2 + ': hacé lo mismo con el numerador.', bien: '¡Bien!' }; }
      if (md === 'irreducible') { var g = R(2, 8), S = simp(a, b); return { cons: 'Simplificá hasta la fracción irreducible: <b>' + S[0] * g + '/' + S[1] * g + '</b>', campos: [{ lab: 'numerador', v: S[0] }, { lab: 'denominador', v: S[1] }], ayuda: 'Dividí numerador y denominador por su MCD.', bien: '¡Bien! ' + S[0] + '/' + S[1] + '.' }; }
      if (md === 'cruzados') { var k3 = R(2, 4), eq = Math.random() < .5, c3 = eq ? a * k3 : a * k3 + 1, d3 = b * k3; return { cons: '¿<b>' + a + '/' + b + '</b> y <b>' + c3 + '/' + d3 + '</b> son equivalentes? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: eq ? ['si', 'sí'] : ['no'] }], ayuda: 'Productos cruzados: ' + a + ' × ' + d3 + ' y ' + b + ' × ' + c3 + '.', bien: eq ? '¡Bien! Son iguales.' : '¡Bien! Son distintos.' }; }
      if (md === 'recta') { var n4 = R(b + 1, 4 * b); if (n4 % b === 0) n4++; return { cons: '¿Entre qué dos números naturales está <b>' + n4 + '/' + b + '</b> en la recta?', campos: [{ lab: 'entre', v: Math.floor(n4 / b) }, { lab: 'y', v: Math.floor(n4 / b) + 1 }], ayuda: 'Dividí ' + n4 + ' ÷ ' + b + '.', bien: '¡Bien!' }; }
      if (md === 'entre') { var x = R(1, 4), y = x + 1, dd = R(3, 7); return { cons: 'Escribí una fracción que esté entre <b>' + x + '/' + dd + '</b> y <b>' + y + '/' + dd + '</b>.', campos: [{ tipo: 'frac', v: (2 * x + 1) / (2 * dd), n: 2 * x + 1, d: 2 * dd, acepta: function (v) { return v > x / dd && v < y / dd; } }], ayuda: 'Amplificá las dos por 2: ' + 2 * x + '/' + 2 * dd + ' y ' + 2 * y + '/' + 2 * dd + '.', bien: '¡Bien! Hay infinitas.' }; }
      if (md === 'comparar' || md === 'referentes') { var a2 = R(1, 8), b2 = R(2, 9), c2 = R(1, 8), d2 = R(2, 9); while (a2 * d2 === b2 * c2) c2 = R(1, 8); var may = a2 / b2 > c2 / d2;
        return { cons: '¿Cuál es mayor: <b>' + a2 + '/' + b2 + '</b> o <b>' + c2 + '/' + d2 + '</b>? Escribí la mayor.', campos: [F(may ? a2 : c2, may ? b2 : d2)], ayuda: md === 'referentes' ? 'Comparalas con 1/2 y con 1.' : 'Llevalas a un denominador común.', bien: '¡Bien!' }; }
      if (md === 'inverso') return { cons: '¿Cuál es el inverso de <b>' + a + '/' + b + '</b>?', campos: [F(b, a)], ayuda: 'Se dan vuelta numerador y denominador.', bien: '¡Bien! ' + a + '/' + b + ' × ' + b + '/' + a + ' = 1.' };
      if (md === 'division') { var t = R(2, 6), dv = R(2, 5); return { cons: '¿Cuántas botellas de <b>1/' + dv + '</b> litro se llenan con <b>' + t + '</b> litros?', campos: [{ v: t * dv }], ayuda: t + ' ÷ 1/' + dv + ' = ' + t + ' × ' + dv + '.', bien: '¡Bien! ' + t * dv + ' botellas.' }; }
      if (md === 'combinadas') { var q = R(2, 6); return { cons: 'Resolvé: <b>1/' + q + ' + 2/' + q + ' × 1/2</b>', campos: [F(2, q)], ayuda: 'Primero la multiplicación: 2/' + q + ' × 1/2 = 1/' + q + '.', bien: '¡Bien! 2/' + q + '.' }; }
      if (md === 'potencia') { var n5 = R(2, 3), a5 = R(1, 4), b5 = R(a5 + 1, 6); return { cons: 'Calculá <b>(' + a5 + '/' + b5 + ')' + sup(n5) + '</b>', campos: [F(Math.pow(a5, n5), Math.pow(b5, n5))], ayuda: 'Elevá el numerador y el denominador.', bien: '¡Bien!' }; }
      var e1 = R(1, 3), e2 = R(1, 3), dd2 = pick([2, 3, 4, 5]), n1 = R(1, dd2 - 1), n2 = R(1, dd2 - 1), tot = (e1 + e2) * dd2 + n1 + n2;
      return { cons: 'Sumá: <b>' + e1 + ' ' + n1 + '/' + dd2 + ' + ' + e2 + ' ' + n2 + '/' + dd2 + '</b> (como fracción)', campos: [F(tot, dd2)], ayuda: 'Pasá los mixtos a fracción o sumá enteros con enteros y fracciones con fracciones.', bien: '¡Bien! ' + tot + '/' + dd2 + '.' };
    });
  } };

  // ======= DECIMALES (Matemática I · Misión 10) =======
  function r4(x) { return Math.round(x * 1e4) / 1e4; }
  function ndec(x) { var t = String(r4(x)); return t.indexOf('.') < 0 ? 0 : t.split('.')[1].length; }
  function solo25(b) { while (b % 2 === 0) b /= 2; while (b % 5 === 0) b /= 5; return b === 1; }
  function factoriza(n) { var f = [], p = 2; while (n > 1) { while (n % p === 0) { f.push(p); n /= p; } p++; } return f; }
  function perS(ent, d) { return ent + ',<span class="lb2-per">' + d + '</span>'; }
  M.decimales = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'frac_dec', C = {
      frac_dec: ctrl('a', 'Numerador', 1, 999, 1, 37) + ctrl('p', 'Ceros del denominador', 1, 3, 1, 2),
      dec_frac: ctrl('a', 'Cifras sin coma', 1, 999, 1, 45) + ctrl('p', 'Cifras decimales', 1, 3, 1, 2),
      comparar: ctrl('x', 'Primer número', 0, 9, .01, 2.7) + ctrl('y', 'Segundo número', 0, 9, .01, 2.65),
      cual: ctrl('a', 'Numerador', 1, 20, 1, 7) + ctrl('b', 'Denominador', 2, 40, 1, 12),
      puro_frac: ctrl('q', 'Período', 1, 98, 1, 36),
      suma: ctrl('x', 'Primer número', 0, 50, .1, 12.5) + ctrl('y', 'Segundo número', 0, 9, .01, 3.47),
      resta: ctrl('x', 'Primer número', 0, 50, .1, 12.5) + ctrl('y', 'Segundo número', 0, 9, .01, 3.47),
      producto: ctrl('x', 'Primer factor', 0, 20, .1, 2.4) + ctrl('y', 'Segundo factor', 0, 9, .01, 1.35),
      division: ctrl('x', 'Dividendo', 1, 99, .1, 7.5) + ctrl('y', 'Divisor', .1, 9, .1, 2.5),
      estimar: ctrl('x', 'Precio por kilo', 1, 20, .1, 4.9) + ctrl('y', 'Kilos', 1, 9, .1, 6.1) }[md];
    escena(el, C, function (o) {
      var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
      if (md === 'frac_dec') { var den = Math.pow(10, o.p), v = o.a / den; return [{ vis: G(fr(o.a, den)), txt: 'Una <b>fracción decimal</b>: el denominador es 10, 100 o 1.000.' }, { vis: F(o.p + ' cero' + (o.p > 1 ? 's' : '') + ' → ' + o.p + ' cifra' + (o.p > 1 ? 's' : '') + ' después de la coma'), txt: 'Cada cero del denominador es una cifra decimal.' }, { vis: RS(fr(o.a, den) + ' = ' + fmt(v)), txt: 'Escribimos el numerador y corremos la coma ' + o.p + ' lugar' + (o.p > 1 ? 'es' : '') + ' a la izquierda.' }]; }
      if (md === 'dec_frac') { var den2 = Math.pow(10, o.p), v2 = o.a / den2, g = mcd(o.a, den2); return [{ vis: G(fmt(v2)), txt: 'Contamos las cifras después de la coma: <b>' + o.p + '</b>.' }, { vis: G(fmt(v2) + ' = ' + fr(o.a, den2)), txt: 'El número sin coma va arriba; abajo, un 1 con ' + o.p + ' cero' + (o.p > 1 ? 's' : '') + '.' }, { vis: RS(fmt(v2) + ' = ' + fr(o.a / g, den2 / g)), txt: g > 1 ? 'Simplificamos dividiendo por ' + g + '.' : 'Ya es irreducible.' }]; }
      if (md === 'comparar') { var x = r4(o.x), y = r4(o.y), n = Math.max(ndec(x), ndec(y), 1), sx = x.toFixed(n).replace('.', ','), sy = y.toFixed(n).replace('.', ','), sg = x > y ? '>' : x < y ? '<' : '=';
        return [{ vis: G(fmt(x) + ' ? ' + fmt(y)), txt: 'Primero la parte entera: ' + Math.floor(x) + ' y ' + Math.floor(y) + '.' + (Math.floor(x) !== Math.floor(y) ? ' Ya alcanza: gana la mayor.' : ' Es igual, seguimos.') }, { vis: G(sx + ' ? ' + sy), txt: 'Completamos con ceros para tener la misma cantidad de decimales.' }, { vis: RS(fmt(x) + ' ' + sg + ' ' + fmt(y)), txt: 'Comparamos cifra por cifra, de izquierda a derecha. Más cifras no quiere decir más grande.' }]; }
      if (md === 'cual') { var g3 = mcd(o.a, o.b), a3 = o.a / g3, b3 = o.b / g3, fa = factoriza(b3), ex = solo25(b3), Q = periodo(a3, b3);
        return [{ vis: G(fr(o.a, o.b) + (g3 > 1 ? ' = ' + fr(a3, b3) : '')), txt: g3 > 1 ? 'Primero la dejamos irreducible.' : 'Ya es irreducible.' }, { vis: F(b3 + ' = ' + (fa.join(' × ') || '1')), txt: 'Descomponemos el denominador en factores primos.' }, { vis: F(ex ? 'Solo 2 y 5' : 'Aparece otro primo además de 2 y 5'), txt: ex ? 'Solo tiene 2 y 5: se puede llevar a 10, 100, 1.000…' : 'Tiene otro primo: nunca llega a 10, 100, 1.000…' }, { vis: RS(fr(a3, b3) + ' = ' + (Q.ini < 0 ? Q.ent + (Q.dig ? ',' + Q.dig : '') : Q.ent + ',' + Q.dig.slice(0, Q.ini) + '<span class="lb2-per">' + Q.dig.slice(Q.ini) + '</span>')), txt: ex ? 'Es un <b>decimal exacto</b>.' : 'Es un <b>decimal periódico</b>.' }]; }
      if (md === 'puro_frac') { var q = o.q, L = q < 10 ? 1 : 2, nueves = L === 1 ? 9 : 99, g4 = mcd(q, nueves), qs = L === 2 && q < 10 ? '0' + q : String(q);
        return [{ vis: G('x = ' + perS(0, qs)), txt: 'Un periódico puro: el período es <b>' + qs + '</b>, de ' + L + ' cifra' + (L > 1 ? 's' : '') + '.' }, { vis: G((L === 1 ? '10' : '100') + 'x = ' + q + ',<span class="lb2-per">' + qs + '</span>'), txt: 'Multiplicamos por ' + (L === 1 ? '10' : '100') + ': la coma salta un período.' }, { vis: G(nueves + 'x = ' + q), txt: 'Restamos x: la parte que se repite desaparece.' }, { vis: RS(perS(0, qs) + ' = ' + fr(q, nueves) + (g4 > 1 ? ' = ' + fr(q / g4, nueves / g4) : '')), txt: 'Arriba el período, abajo tantos 9 como cifras tiene.' }]; }
      if (md === 'suma' || md === 'resta') { var x5 = r4(o.x), y5 = r4(o.y); if (md === 'resta' && y5 > x5) { var t5 = x5; x5 = y5; y5 = t5; } var n5 = Math.max(ndec(x5), ndec(y5), 1), res = r4(md === 'suma' ? x5 + y5 : x5 - y5), col = '<pre class="lb2-col">  ' + x5.toFixed(n5).replace('.', ',').padStart(8) + '\n' + (md === 'suma' ? '+ ' : '− ') + y5.toFixed(n5).replace('.', ',').padStart(8) + '</pre>';
        return [{ vis: col, txt: 'Encolumnamos con <b>coma debajo de coma</b>.' }, { vis: col, txt: 'Completamos con ceros: ' + x5.toFixed(n5).replace('.', ',') + ' y ' + y5.toFixed(n5).replace('.', ',') + '.' }, { vis: col + RS('= ' + fmt(res)), txt: (md === 'suma' ? 'Sumamos' : 'Restamos') + ' como con naturales y bajamos la coma.' }]; }
      if (md === 'producto') { var x6 = r4(o.x), y6 = r4(o.y), d6 = ndec(x6) + ndec(y6), sinc = Math.round(x6 * Math.pow(10, ndec(x6))) * Math.round(y6 * Math.pow(10, ndec(y6)));
        return [{ vis: G(fmt(x6) + ' × ' + fmt(y6)), txt: 'Multiplicamos como si no hubiera comas.' }, { vis: F(Math.round(x6 * Math.pow(10, ndec(x6))) + ' × ' + Math.round(y6 * Math.pow(10, ndec(y6))) + ' = ' + sinc), txt: 'El producto sin comas.' }, { vis: F(ndec(x6) + ' + ' + ndec(y6) + ' = ' + d6 + ' cifras decimales'), txt: 'Contamos las cifras decimales de los dos factores.' }, { vis: RS('= ' + fmt(r4(x6 * y6))), txt: 'Ponemos la coma dejando ' + d6 + ' cifras a la derecha.' }]; }
      if (md === 'division') { var x7 = r4(o.x), y7 = r4(o.y), k7 = Math.pow(10, ndec(y7)), X7 = r4(x7 * k7), Y7 = r4(y7 * k7);
        return [{ vis: G(fmt(x7) + ' ÷ ' + fmt(y7)), txt: 'Queremos que el divisor no tenga coma.' }, { vis: G(fmt(X7) + ' ÷ ' + fmt(Y7)), txt: k7 > 1 ? 'Multiplicamos los dos por ' + k7 + ': el cociente no cambia.' : 'El divisor ya es entero.' }, { vis: RS('= ' + fmt(r4(x7 / y7))), txt: 'Dividimos como siempre; si sigue, se agregan ceros después de la coma.' }]; }
      var e1 = Math.round(o.x), e2 = Math.round(o.y);
      return [{ vis: G(fmt(o.x) + ' × ' + fmt(o.y)), txt: 'Antes de calcular, estimamos.' }, { vis: G(e1 + ' × ' + e2 + ' = ' + e1 * e2), txt: 'Redondeamos a enteros: ' + fmt(o.x) + ' ≈ ' + e1 + ' y ' + fmt(o.y) + ' ≈ ' + e2 + '.' }, { vis: RS(fmt(r4(o.x * o.y)) + ' ≈ ' + e1 * e2), txt: 'La cuenta exacta tiene que dar cerca. Si da 300, la coma está mal puesta.' }];
    });
  } };
  M.decimales_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'frac_dec';
    respuesta(el, api, function () {
      if (md === 'frac_dec') { var pp = R(1, 3), den = Math.pow(10, pp), a = R(1, den * 3); if (a % 10 === 0) a++; return { cons: 'Escribí <b>' + a + '/' + den + '</b> como número decimal.', campos: [{ v: r4(a / den) }], ayuda: den + ' tiene ' + pp + ' cero(s): ' + pp + ' cifra(s) después de la coma.', bien: '¡Bien! ' + fmt(r4(a / den)) + '.' }; }
      if (md === 'dec_frac') { var b = pick([10, 100, 1000]), a2 = R(2, b - 1), g = mcd(a2, b); return { cons: 'Escribí <b>' + fmt(a2 / b) + '</b> como fracción irreducible.', campos: [{ lab: 'numerador', v: a2 / g }, { lab: 'denominador', v: b / g }], ayuda: 'Primero ' + a2 + '/' + b + ', después simplificá.', bien: '¡Bien! ' + a2 / g + '/' + b / g + '.' }; }
      if (md === 'comparar') { var e = R(0, 9), x = r4(e + R(1, 9) / 10), y = r4(e + R(10, 99) / 100); if (x === y) y = r4(y + .01); return { cons: '¿Cuál es mayor: <b>' + fmt(x) + '</b> o <b>' + fmt(y) + '</b>? Escribí el mayor.', campos: [{ v: Math.max(x, y) }], ayuda: 'Completá con ceros: ' + x.toFixed(2).replace('.', ',') + ' y ' + y.toFixed(2).replace('.', ',') + '.', bien: '¡Bien!' }; }
      if (md === 'cual') { var bb = pick([3, 4, 6, 7, 8, 9, 12, 15, 16, 20, 25, 40]), aa = R(1, bb - 1); while (mcd(aa, bb) > 1) aa = R(1, bb - 1); var ex = solo25(bb); return { cons: '<b>' + aa + '/' + bb + '</b>, ¿da un decimal exacto o periódico? Escribí <b>exacto</b> o <b>periódico</b>.', campos: [{ tipo: 'texto', v: ex ? ['exacto'] : ['periodico', 'periódico'] }], ayuda: 'Descomponé ' + bb + ': ¿tiene solo 2 y 5?', bien: '¡Bien! Es ' + (ex ? 'exacto' : 'periódico') + '.' }; }
      if (md === 'puro_frac') { var L = pick([1, 2]), q = L === 1 ? R(1, 8) : R(10, 98), nv = L === 1 ? 9 : 99, g2 = mcd(q, nv); return { cons: 'Pasá <b>' + perS(0, String(q)) + '</b> a fracción irreducible.', campos: [{ lab: 'numerador', v: q / g2 }, { lab: 'denominador', v: nv / g2 }], ayuda: 'Arriba el período, abajo ' + nv + '; después simplificá.', bien: '¡Bien!' }; }
      if (md === 'suma' || md === 'resta') { var x2 = R(10, 300) / 10, y2 = R(10, 900) / 100; if (md === 'resta' && y2 > x2) { var t = x2; x2 = y2; y2 = t; } return { cons: 'Calculá <b>' + fmt(x2) + (md === 'suma' ? ' + ' : ' − ') + fmt(y2) + '</b>', campos: [{ v: r4(md === 'suma' ? x2 + y2 : x2 - y2) }], ayuda: 'Coma debajo de coma y completá con ceros.', bien: '¡Bien!' }; }
      if (md === 'producto') { var x3 = R(11, 99) / 10, y3 = R(2, 9) + (Math.random() < .5 ? R(1, 9) / 10 : 0); return { cons: 'Calculá <b>' + fmt(x3) + ' × ' + fmt(y3) + '</b>', campos: [{ v: r4(x3 * y3) }], ayuda: 'Multiplicá sin comas y después contá las cifras decimales de los dos factores.', bien: '¡Bien!' }; }
      if (md === 'division') { var y4 = pick([.2, .5, .4, 2.5, 1.5, .25]), c4 = R(2, 30), x4 = r4(y4 * c4); return { cons: 'Calculá <b>' + fmt(x4) + ' ÷ ' + fmt(y4) + '</b>', campos: [{ v: c4 }], ayuda: 'Multiplicá los dos por 10 o por 100 hasta que el divisor no tenga coma.', bien: '¡Bien! ' + c4 + '.' }; }
      var p5 = R(15, 99) / 10, k5 = R(2, 9) + (Math.random() < .5 ? .1 : -.1); return { cons: 'Un kilo cuesta $<b>' + fmt(p5) + '</b> y se compran <b>' + fmt(r4(k5)) + '</b> kilos. Estimá el total redondeando los dos números a enteros.', campos: [{ v: Math.round(p5) * Math.round(k5) }], ayuda: Math.round(p5) + ' × ' + Math.round(k5) + '.', bien: '¡Bien! Es una estimación.' };
    });
  } };
  // ======= ENTEROS (Matemática I · Misión 11) =======
  function rectaZ(marcas, extra) { var X = function (v) { return 130 + v * 11; }, t = '';
    for (var k = -10; k <= 10; k++) t += '<line class="rayo" x1="' + X(k) + '" y1="' + (k ? 32 : 26) + '" x2="' + X(k) + '" y2="' + (k ? 40 : 46) + '"/>' + (k % 5 === 0 ? '<text x="' + X(k) + '" y="62">' + sig(k) + '</text>' : '');
    (extra || []).forEach(function (s) { t += '<line class="diag" x1="' + X(s[0]) + '" y1="36" x2="' + X(s[1]) + '" y2="36" style="stroke-width:4"/>'; });
    (marcas || []).forEach(function (m) { t += '<circle cx="' + X(m[0]) + '" cy="36" r="6" class="pt"/><text x="' + X(m[0]) + '" y="20" class="pt">' + (m[1] || sig(m[0])) + '</text>'; });
    return '<svg viewBox="0 0 260 70" class="lb2-svg"><line class="rayo" x1="5" y1="36" x2="255" y2="36"/>' + t + '</svg>'; }
  M.enteros = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'situacion', C = {
      situacion: ctrl('x', 'Temperatura', -10, 10, 1, -3, ' °C'), opuesto: ctrl('x', 'Número', -10, 10, 1, -4),
      distancia: ctrl('a', 'Primer número', -10, 10, 1, -3) + ctrl('b', 'Segundo número', -10, 10, 1, 5),
      comparar: ctrl('a', 'Primer número', -10, 10, 1, -7) + ctrl('b', 'Segundo número', -10, 10, 1, -2),
      intervalo: ctrl('a', 'Desde', -10, 9, 1, -4) + ctrl('b', 'Hasta', -9, 10, 1, 3),
      absoluto: ctrl('x', 'Número', -10, 10, 1, -6),
      suma: ctrl('a', 'Primer sumando', -10, 10, 1, -7) + ctrl('b', 'Segundo sumando', -10, 10, 1, 4),
      resta: ctrl('a', 'Minuendo', -10, 10, 1, 3) + ctrl('b', 'Sustraendo', -10, 10, 1, -5),
      suprimir: ctrl('a', 'Número de afuera', -9, 9, 1, 8) + ctrl('b', 'Primer número del paréntesis', -9, 9, 1, 3) + ctrl('c', 'Segundo número del paréntesis', -9, 9, 1, -5),
      division: ctrl('q', 'Cociente', -9, 9, 1, -4) + ctrl('b', 'Divisor', -9, 9, 1, 3),
      combinadas: ctrl('a', 'a', -9, 9, 1, 10) + ctrl('b', 'b', -9, 9, 1, -2) + ctrl('c', 'c', -9, 9, 1, -6),
      cuadrado: ctrl('x', 'Número', 1, 9, 1, 3),
      raiz: ctrl('x', 'Número', -5, 5, 1, -2) }[md];
    escena(el, C, function (o) { var RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; };
      if (md === 'situacion') { var x = o.x; return [{ vis: rectaZ([[0, '0']]), txt: 'El <b>0</b> es la referencia: ni positivo ni negativo.' }, { vis: rectaZ([[x]]), txt: x < 0 ? 'Bajo cero: está a la <b>izquierda</b> del 0.' : x > 0 ? 'Sobre cero: a la <b>derecha</b> del 0.' : 'Justo en el 0.' }, { vis: rectaZ([[x]]) + RS(x < 0 ? x + ' °C → ' + sig(x) : x + ' °C → ' + sig(x)), txt: x < 0 ? 'Se escribe con signo <b>−</b>: es un número <b>negativo</b>.' : x > 0 ? 'Es <b>positivo</b>; el signo + se puede omitir.' : 'El 0 no lleva signo.' }]; }
      if (md === 'opuesto') { var y = o.x; return [{ vis: rectaZ([[y]]), txt: 'Ubicamos el <b>' + sig(y) + '</b>: está a ' + Math.abs(y) + ' del 0.' }, { vis: rectaZ([[y], [-y]], [[y, -y]]), txt: 'Del otro lado del 0, a la misma distancia: son <b>simétricos</b> respecto del 0.' }, { vis: rectaZ([[y], [-y]]) + RS('El opuesto de ' + sig(y) + ' es ' + sig(-y)), txt: 'El opuesto tiene el mismo número con el signo cambiado.' }]; }
      if (md === 'distancia') { var a = o.a, b = o.b; return [{ vis: rectaZ([[a], [b]]), txt: 'Ubicamos los dos números.' }, { vis: rectaZ([[a], [b]], [[a, b]]), txt: 'Contamos los saltos de uno en uno entre ellos.' }, { vis: rectaZ([[a], [b]], [[a, b]]) + RS('Distancia = ' + Math.abs(a - b)), txt: (a < 0) !== (b < 0) && a && b ? 'Si están a distinto lado del 0, se suman las distancias al 0: ' + Math.abs(a) + ' + ' + Math.abs(b) + '.' : 'Si están del mismo lado, se restan las distancias al 0.' }]; }
      if (md === 'comparar') { var c = o.a, d = o.b, sg = c > d ? '>' : c < d ? '<' : '='; return [{ vis: rectaZ([[c], [d]]), txt: 'Ubicamos los dos en la recta.' }, { vis: rectaZ([[c], [d]]), txt: 'Es mayor el que está más a la <b>derecha</b>.' }, { vis: rectaZ([[c], [d]]) + RS(sig(c) + ' ' + sg + ' ' + sig(d)), txt: c < 0 && d < 0 ? 'Entre negativos, es mayor el que está más cerca del 0.' : 'Cualquier positivo es mayor que cualquier negativo.' }]; }
      if (md === 'intervalo') { var lo = Math.min(o.a, o.b), hi = Math.max(o.a, o.b), L = []; for (var k = lo + 1; k < hi; k++) L.push(k); return [{ vis: rectaZ([[lo], [hi]]), txt: 'Marcamos los extremos: ' + sig(lo) + ' y ' + sig(hi) + '.' }, { vis: rectaZ([[lo], [hi]].concat(L.map(function (v) { return [v, ' ']; }))), txt: 'Marcamos los enteros que están <b>entre</b> ellos, sin contar los extremos.' }, { vis: RS(L.length ? L.map(sig).join(', ') : 'Ninguno') , txt: 'Hay <b>' + L.length + '</b>. Se cuentan de a uno, pasando por el 0.' }]; }
      var P = function (v) { return v < 0 ? '(' + sig(v) + ')' : String(v); }, G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
      if (md === 'suma') { var a1 = o.a, b1 = o.b, s1 = a1 + b1; return [{ vis: rectaZ([[a1]]), txt: 'Partimos del <b>' + sig(a1) + '</b>.' }, { vis: rectaZ([[a1], [s1]], [[a1, s1]]), txt: b1 >= 0 ? 'Sumar ' + b1 + ': avanzamos ' + b1 + ' a la <b>derecha</b>.' : 'Sumar ' + sig(b1) + ': retrocedemos ' + Math.abs(b1) + ' a la <b>izquierda</b>.' }, { vis: rectaZ([[s1]]) + RS(P(a1) + ' + ' + P(b1) + ' = ' + sig(s1)), txt: (a1 < 0) === (b1 < 0) ? 'Mismo signo: se suman las distancias al 0 y se deja el signo.' : 'Distinto signo: se restan las distancias y queda el signo del que está más lejos del 0.' }]; }
      if (md === 'resta') { var a2 = o.a, b2 = o.b; return [{ vis: G(P(a2) + ' − ' + P(b2)), txt: 'Una resta de enteros.' }, { vis: G(P(a2) + ' + ' + P(-b2)), txt: 'Restar es <b>sumar el opuesto</b>: el opuesto de ' + sig(b2) + ' es ' + sig(-b2) + '.' }, { vis: rectaZ([[a2], [a2 - b2]], [[a2, a2 - b2]]) + RS('= ' + sig(a2 - b2)), txt: b2 < 0 ? 'Restar un negativo hace avanzar: el resultado es mayor.' : 'Ahora es una suma común en la recta.' }]; }
      if (md === 'suprimir') { var a3 = o.a, b3 = o.b, c3 = o.c, ins = sig(b3) + (c3 < 0 ? ' − ' + -c3 : ' + ' + c3), cam = sig(-b3) + (c3 < 0 ? ' + ' + -c3 : ' − ' + c3); return [{ vis: G(a3 + ' − (' + ins + ')'), txt: 'Hay un signo <b>menos</b> delante del paréntesis.' }, { vis: G(a3 + ' ' + (cam.charAt(0) === '-' || cam.charAt(0) === '−' ? '− ' + cam.slice(1) : '+ ' + cam)), txt: 'Al sacar el paréntesis, <b>cambian todos los signos</b> de adentro.' }, { vis: RS('= ' + sig(a3 - b3 - c3)), txt: 'Sumamos de izquierda a derecha. Con un + delante, los signos quedan igual.' }]; }
      if (md === 'division') { var q4 = o.q || 1, b4 = o.b || 1, d4 = q4 * b4; return [{ vis: G(P(d4) + ' ÷ ' + P(b4)), txt: 'Primero los signos: ' + (d4 < 0 ? '−' : '+') + ' y ' + (b4 < 0 ? '−' : '+') + '.' }, { vis: F((d4 < 0) === (b4 < 0) ? 'Signos iguales → +' : 'Signos distintos → −'), txt: 'La misma regla que en la multiplicación.' }, { vis: RS(P(d4) + ' ÷ ' + P(b4) + ' = ' + sig(q4)), txt: 'Dividimos sin signo: ' + Math.abs(d4) + ' ÷ ' + Math.abs(b4) + ' = ' + Math.abs(q4) + '. Comprobación: ' + P(q4) + ' × ' + P(b4) + ' = ' + sig(d4) + '.' }]; }
      if (md === 'combinadas') { var a5 = o.a, b5 = o.b, c5 = o.c, m5 = b5 * c5; return [{ vis: G(a5 + ' + ' + P(b5) + ' × ' + P(c5)), txt: 'La jerarquía es la de siempre: primero × y ÷.' }, { vis: G(a5 + ' + ' + P(m5)), txt: P(b5) + ' × ' + P(c5) + ' = ' + sig(m5) + ', con la regla de los signos.' }, { vis: RS('= ' + sig(a5 + m5)), txt: 'Al final la suma de enteros.' }]; }
      if (md === 'cuadrado') { var x6 = o.x; return [{ vis: G('(−' + x6 + ')<sup>2</sup>'), txt: 'Con paréntesis, la base es <b>−' + x6 + '</b>.' }, { vis: G('(−' + x6 + ') × (−' + x6 + ') = ' + x6 * x6), txt: 'Menos por menos: da positivo.' }, { vis: G('−' + x6 + '<sup>2</sup> = −(' + x6 + ' × ' + x6 + ')'), txt: 'Sin paréntesis, el exponente afecta solo al ' + x6 + '; el menos queda afuera.' }, { vis: RS('(−' + x6 + ')<sup>2</sup> = ' + x6 * x6 + ' · −' + x6 + '<sup>2</sup> = −' + x6 * x6), txt: 'Son distintos: los paréntesis importan.' }]; }
      if (md === 'raiz') { var x7 = o.x, c7 = x7 * x7 * x7; return [{ vis: G('∛' + P(c7)), txt: 'Buscamos un número que, elevado al cubo, dé ' + sig(c7) + '.' }, { vis: G(P(x7) + '<sup>3</sup> = ' + sig(c7)), txt: 'Con exponente impar, el signo se conserva.' }, { vis: RS('∛' + P(c7) + ' = ' + sig(x7)), txt: 'La raíz cúbica de un negativo es negativa. La raíz cuadrada de un negativo, en cambio, no existe en los enteros.' }]; }
      var z = o.x; return [{ vis: rectaZ([[z]]), txt: 'Ubicamos el <b>' + sig(z) + '</b>.' }, { vis: rectaZ([[z]], [[0, z]]), txt: 'Medimos la distancia al 0: <b>' + Math.abs(z) + '</b>.' }, { vis: rectaZ([[z]], [[0, z]]) + RS('|' + sig(z) + '| = ' + Math.abs(z)), txt: 'Esa distancia es el <b>valor absoluto</b>. Nunca es negativo. No es lo mismo que el opuesto: el opuesto de ' + sig(z) + ' es ' + sig(-z) + '.' }];
    });
  } };
  M.enteros_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'situacion';
    respuesta(el, api, function () { var n = R(1, 12), s = pick([-1, 1]), x = s * n;
      if (md === 'situacion') { var S = pick([['Hacen ' + n + ' grados bajo cero.', -n], ['El auto está estacionado en el subsuelo ' + n + '.', -n], ['Un buzo está a ' + n + ' metros bajo el nivel del mar.', -n], ['El ascensor está en el piso ' + n + '.', n], ['Hacen ' + n + ' grados sobre cero.', n]]); return { cons: S[0] + ' Escribilo como número entero.', campos: [{ v: S[1] }], ayuda: 'Debajo del 0 (del nivel de referencia) es negativo: lleva signo −.', bien: '¡Bien! ' + sig(S[1]) + '.' }; }
      if (md === 'opuesto') return { cons: '¿Cuál es el opuesto de <b>' + sig(x) + '</b>?', campos: [{ v: -x }], ayuda: 'Mismo número, signo cambiado.', bien: '¡Bien! ' + sig(-x) + '.' };
      if (md === 'distancia') { var a = R(-10, 10), b = R(-10, 10); while (b === a) b = R(-10, 10); return { cons: '¿A cuántas unidades de distancia están <b>' + sig(a) + '</b> y <b>' + sig(b) + '</b> en la recta?', campos: [{ v: Math.abs(a - b) }], ayuda: 'Contá los saltos de uno en uno, pasando por el 0 si hace falta.', bien: '¡Bien!' }; }
      if (md === 'comparar') { var c = R(-15, 10), d = R(-15, 10); while (d === c) d = R(-15, 10); return { cons: '¿Cuál es mayor: <b>' + sig(c) + '</b> o <b>' + sig(d) + '</b>? Escribí el mayor.', campos: [{ v: Math.max(c, d) }], ayuda: 'En la recta, el mayor está más a la derecha.', bien: '¡Bien!' }; }
      if (md === 'intervalo') { var lo = R(-9, 0), hi = R(1, 8); return { cons: '¿Cuántos números enteros hay <b>entre</b> ' + sig(lo) + ' y ' + sig(hi) + ' (sin contar ' + sig(lo) + ' ni ' + sig(hi) + ')?', campos: [{ v: hi - lo - 1 }], ayuda: 'Escribilos todos, incluido el 0, y contalos.', bien: '¡Bien!' }; }
      var Pq = function (v) { return v < 0 ? '(' + sig(v) + ')' : String(v); };
      if (md === 'suma') { var a1 = R(-15, 15), b1 = R(-15, 15); return { cons: 'Calculá <b>' + Pq(a1) + ' + ' + Pq(b1) + '</b>', campos: [{ v: a1 + b1 }], ayuda: 'Mismo signo: sumá y dejá el signo. Distinto: restá y queda el signo del más lejano al 0.', bien: '¡Bien!' }; }
      if (md === 'resta') { var a2 = R(-12, 12), b2 = R(-12, 12); return { cons: 'Calculá <b>' + Pq(a2) + ' − ' + Pq(b2) + '</b>', campos: [{ v: a2 - b2 }], ayuda: 'Sumá el opuesto: ' + Pq(a2) + ' + ' + Pq(-b2) + '.', bien: '¡Bien!' }; }
      if (md === 'suprimir') { var a3 = R(2, 15), b3 = R(1, 9), c3 = R(1, 9); return { cons: 'Calculá <b>' + a3 + ' − (' + b3 + ' − ' + c3 + ')</b> suprimiendo el paréntesis.', campos: [{ v: a3 - b3 + c3 }], ayuda: 'Con un menos adelante cambian los signos: ' + a3 + ' − ' + b3 + ' + ' + c3 + '.', bien: '¡Bien!' }; }
      if (md === 'producto') { var a4 = R(-9, 9) || 2, b4 = R(-9, 9) || -3; return { cons: 'Calculá <b>' + Pq(a4) + ' × ' + Pq(b4) + '</b>', campos: [{ v: a4 * b4 }], ayuda: 'Signos iguales: +. Distintos: −.', bien: '¡Bien!' }; }
      if (md === 'division') { var q5 = R(-9, 9) || 4, b5 = pick([-7, -5, -3, -2, 2, 3, 4, 6]); return { cons: 'Calculá <b>' + Pq(q5 * b5) + ' ÷ ' + Pq(b5) + '</b>', campos: [{ v: q5 }], ayuda: 'Misma regla de signos que la multiplicación.', bien: '¡Bien!' }; }
      if (md === 'combinadas') { var a6 = R(-10, 10), b6 = R(-6, 6) || 2, c6 = R(-6, 6) || -3; return { cons: 'Calculá <b>' + a6 + ' + ' + Pq(b6) + ' × ' + Pq(c6) + '</b>', campos: [{ v: a6 + b6 * c6 }], ayuda: 'Primero la multiplicación, con la regla de los signos.', bien: '¡Bien!' }; }
      if (md === 'cuadrado') { var x7 = R(2, 9), con = Math.random() < .5; return { cons: 'Calculá <b>' + (con ? '(−' + x7 + ')' : '−' + x7) + '<sup>2</sup></b>', campos: [{ v: con ? x7 * x7 : -x7 * x7 }], ayuda: con ? 'Con paréntesis, la base es negativa: menos por menos.' : 'Sin paréntesis, el exponente afecta solo al ' + x7 + '.', bien: '¡Bien!' }; }
      if (md === 'potencia') { var b8 = -R(1, 5), e8 = R(2, 4); return { cons: 'Calculá <b>(' + b8 + ')<sup>' + e8 + '</sup></b>', campos: [{ v: Math.pow(b8, e8) }], ayuda: 'Base negativa: exponente par da +, impar da −.', bien: '¡Bien!' }; }
      if (md === 'raiz') { var x9 = -R(1, 5); return { cons: 'Calculá <b>∛(' + x9 * x9 * x9 + ')</b>', campos: [{ v: x9 }], ayuda: '¿Qué número negativo, elevado al cubo, da ' + x9 * x9 * x9 + '?', bien: '¡Bien!' }; }
      if (md === 'absoluto') return { cons: '¿Cuánto vale <b>|' + sig(x) + '|</b>?', campos: [{ v: n }], ayuda: 'Es la distancia al 0.', bien: '¡Bien! ' + n + '.' };
      return { cons: 'Para el número <b>' + sig(x) + '</b>, escribí su opuesto y su valor absoluto.', campos: [{ lab: 'opuesto', v: -x }, { lab: 'valor absoluto', v: n }], ayuda: 'El opuesto cambia el signo; el valor absoluto es la distancia al 0.', bien: '¡Bien!' };
    });
  } };

  // ======= RAZONES Y PROPORCIONES (Matemática I · Misión 14) =======
  M.razones = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'razon', C = {
      razon: ctrl('a', 'Varones', 1, 30, 1, 12) + ctrl('b', 'Mujeres', 1, 30, 1, 18),
      proporcion: ctrl('a', 'a', 1, 12, 1, 2) + ctrl('b', 'b', 1, 12, 1, 3) + ctrl('k', 'Multiplicar por', 2, 5, 1, 4),
      fundamental: ctrl('a', 'a', 1, 12, 1, 3) + ctrl('b', 'b', 1, 12, 1, 4) + ctrl('k', 'Multiplicar por', 2, 5, 1, 3),
      desconocido: ctrl('a', 'a', 1, 9, 1, 3) + ctrl('b', 'b', 1, 9, 1, 5) + ctrl('k', 'Multiplicar por', 2, 6, 1, 4) }[md];
    escena(el, C, function (o) { var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
      if (md === 'razon') { var g = mcd(o.a, o.b); return [{ vis: G(o.a + ' varones y ' + o.b + ' mujeres'), txt: 'Queremos comparar las dos cantidades dividiendo.' }, { vis: G(fr(o.a, o.b)), txt: 'La <b>razón</b> entre varones y mujeres es ' + o.a + ' : ' + o.b + ', que se escribe como fracción.' }, { vis: RS(fr(o.a, o.b) + ' = ' + fr(o.a / g, o.b / g)), txt: 'Simplificada: por cada <b>' + o.a / g + '</b> varones hay <b>' + o.b / g + '</b> mujeres.' }]; }
      var a = o.a, b = o.b, k = o.k, c = a * k, d = b * k;
      if (md === 'proporcion') return [{ vis: G(fr(a, b) + ' ¿ = ? ' + fr(c, d)), txt: 'Dos razones.' }, { vis: F(a + ' ÷ ' + b + ' = ' + fmt(r2(a / b)) + ' · ' + c + ' ÷ ' + d + ' = ' + fmt(r2(c / d))), txt: 'Calculamos los dos cocientes.' }, { vis: RS(fr(a, b) + ' = ' + fr(c, d)), txt: 'Dan lo mismo: forman una <b>proporción</b>.' }];
      if (md === 'fundamental') return [{ vis: G(fr(a, b) + ' = ' + fr(c, d)), txt: 'Una proporción: ' + a + ' y ' + d + ' son los <b>extremos</b>; ' + b + ' y ' + c + ', los <b>medios</b>.' }, { vis: F(a + ' × ' + d + ' = ' + a * d), txt: 'Multiplicamos los extremos.' }, { vis: F(b + ' × ' + c + ' = ' + b * c), txt: 'Multiplicamos los medios.' }, { vis: RS(a * d + ' = ' + b * c), txt: 'En toda proporción, extremos por extremos = medios por medios.' }];
      return [{ vis: G(fr(a, b) + ' = ' + fr(c, 'x')), txt: 'Falta un término de la proporción.' }, { vis: G(a + ' · x = ' + b + ' · ' + c), txt: 'Usamos la propiedad fundamental: productos cruzados.' }, { vis: G('x = ' + b * c + ' ÷ ' + a), txt: 'Despejamos: dividimos por ' + a + '.' }, { vis: RS('x = ' + d), txt: 'Control: ' + a + '/' + b + ' = ' + c + '/' + d + '.' }];
    });
  } };
  M.razones_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'razon';
    respuesta(el, api, function () { var a = R(1, 9), b = R(2, 9), k = R(2, 6);
      if (md === 'razon') { var A = a * k, B = b * k, g = mcd(A, B); return { cons: 'En una caja hay <b>' + A + '</b> lápices rojos y <b>' + B + '</b> azules. Escribí la razón entre rojos y azules, simplificada.', campos: [{ lab: 'rojos', v: A / g }, { lab: 'azules', v: B / g }], ayuda: 'Dividí los dos por ' + g + '.', bien: '¡Bien! Por cada ' + A / g + ' rojos hay ' + B / g + ' azules.' }; }
      if (md === 'proporcion') { var eq = Math.random() < .5, c = a * k, d = eq ? b * k : b * k + 1; return { cons: '¿<b>' + a + '/' + b + '</b> y <b>' + c + '/' + d + '</b> forman una proporción? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: eq ? ['si', 'sí'] : ['no'] }], ayuda: 'Comparalos: ' + a + ' × ' + d + ' y ' + b + ' × ' + c + '.', bien: '¡Bien!' }; }
      return { cons: 'Encontrá x: <b>' + a + '/' + b + ' = ' + a * k + '/x</b>', campos: [{ v: b * k }], ayuda: 'Productos cruzados: ' + a + ' · x = ' + b + ' · ' + a * k + '.', bien: '¡Bien! x = ' + b * k + '.' };
    });
  } };
  // ======= EXPRESIONES ALGEBRAICAS (Matemática I · Misión 15) =======
  M.algebra = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'equivalentes', C = {
      equivalentes: ctrl('k', 'Número de afuera', 2, 6, 1, 2) + ctrl('a', 'Número de adentro', 1, 9, 1, 4),
      un_valor: ctrl('x', 'Probar con x =', 0, 6, 1, 2),
      recursiva: ctrl('a', 'Primer término', 1, 10, 1, 4) + ctrl('d', 'Se suma siempre', 2, 6, 1, 3) + ctrl('n', 'Posición buscada', 5, 50, 1, 20) }[md];
    escena(el, C, function (o) { var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; };
      var tab = function (h, f1, f2, xs) { return '<table class="lb2-tab"><tr><th>m</th><th>' + h[0] + '</th><th>' + h[1] + '</th></tr>' + xs.map(function (x) { return '<tr><td>' + x + '</td><td>' + f1(x) + '</td><td>' + f2(x) + '</td></tr>'; }).join('') + '</table>'; };
      if (md === 'equivalentes') { var k = o.k, a = o.a, f1 = function (m) { return k * (m + a); }, f2 = function (m) { return k * m + k * a; };
        return [{ vis: G(k + '(m + ' + a + ')'), txt: 'Una expresión con paréntesis.' }, { vis: G(k + '(m + ' + a + ') = ' + k + 'm + ' + k * a), txt: 'Aplicamos la distributiva: el ' + k + ' multiplica a los dos términos.' }, { vis: tab([k + '(m + ' + a + ')', k + 'm + ' + k * a], f1, f2, [1, 2, 3, 10]), txt: 'Probamos con varios valores de m: dan siempre lo mismo.' }, { vis: RS(k + '(m + ' + a + ') ≡ ' + k + 'm + ' + k * a), txt: 'Son <b>equivalentes</b>: dan igual para <b>todos</b> los valores.' }]; }
      if (md === 'un_valor') { var x = o.x; return [{ vis: G('x + x  y  x · x'), txt: '¿Son equivalentes? Probemos.' }, { vis: G('x = ' + x + ': ' + (x + x) + ' y ' + x * x), txt: x + x === x * x ? 'Con ' + x + ' dan igual…' : 'Con ' + x + ' ya dan distinto.' }, { vis: G('x = 3: 6 y 9'), txt: 'Con 3 dan distinto.' }, { vis: RS('No son equivalentes'), txt: 'Que coincidan para un valor no alcanza: con un solo valor que dé distinto, no son equivalentes.' }]; }
      var a2 = o.a, d = o.d, n = o.n, c = a2 - d; return [{ vis: G(a2 + ', ' + (a2 + d) + ', ' + (a2 + 2 * d) + ', ' + (a2 + 3 * d) + ', …'), txt: 'Cada término es el anterior <b>+ ' + d + '</b>: esa es la regla <b>recursiva</b>.' }, { vis: G(d + 'n ' + (c >= 0 ? '+ ' + c : '− ' + -c)), txt: 'Como se suma ' + d + ' cada vez, la fórmula tiene ' + d + 'n; ajustamos para que el primero dé ' + a2 + '.' }, { vis: G(d + ' · ' + n + (c >= 0 ? ' + ' + c : ' − ' + -c)), txt: 'La fórmula <b>explícita</b> permite ir directo a la posición ' + n + '.' }, { vis: RS('Término ' + n + ' = ' + (d * n + c)), txt: 'Sin escribir todos los anteriores.' }];
    });
  } };
  M.algebra_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'equivalentes';
    respuesta(el, api, function () { var k = R(2, 7), a = R(1, 9);
      if (md === 'equivalentes') return { cons: 'Completá para que sean equivalentes: <b>' + k + '(m + ' + a + ') = ' + k + 'm + ___</b>', campos: [{ v: k * a }], ayuda: 'El ' + k + ' multiplica también al ' + a + '.', bien: '¡Bien!' };
      if (md === 'un_valor') { var P = pick([['2x', 'x + 2', false], ['3x + 3x', '6x', true], ['x · x', '2x', false], ['4(x − 1)', '4x − 4', true], ['x + 5', '5x', false]]); return { cons: '¿<b>' + P[0] + '</b> y <b>' + P[1] + '</b> son equivalentes? Probá con varios valores. Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: P[2] ? ['si', 'sí'] : ['no'] }], ayuda: 'Probá con x = 1, x = 2 y x = 3.', bien: '¡Bien!' }; }
      var a2 = R(1, 9), d = R(2, 6), n = R(10, 40); return { cons: 'La secuencia empieza en <b>' + a2 + '</b> y cada término es el anterior <b>+ ' + d + '</b>. ¿Cuál es el término número <b>' + n + '</b>?', campos: [{ v: a2 + (n - 1) * d }], ayuda: 'Fórmula: ' + d + 'n ' + (a2 - d >= 0 ? '+ ' + (a2 - d) : '− ' + (d - a2)) + '.', bien: '¡Bien!' };
    });
  } };

  // ======= ECUACIONES (Matemática I · Misión 16) =======
  function ecS(a, b) { return (a === 1 ? '' : a === -1 ? '−' : a) + 'x' + (b ? (b < 0 ? ' − ' + -b : ' + ' + b) : ''); }
  M.ecuaciones = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'inversa', C = {
      verificar: ctrl('a', 'Coeficiente', 2, 6, 1, 4) + ctrl('b', 'Número sumado', -9, 9, 1, -2) + ctrl('x', 'Probar con x =', -3, 8, 1, 3),
      inversa: ctrl('a', 'Coeficiente', 2, 9, 1, 3) + ctrl('b', 'Número sumado', -15, 15, 1, 4) + ctrl('x', 'Solución', -6, 10, 1, 5),
      dos_miembros: ctrl('a', 'x del primer miembro', 2, 9, 1, 7) + ctrl('c', 'x del segundo miembro', 1, 8, 1, 3) + ctrl('b', 'Número del primero', -9, 9, 1, -4) + ctrl('x', 'Solución', -5, 8, 1, 4),
      problema: ctrl('x', 'Número pensado', 2, 30, 1, 12) + ctrl('a', 'Multiplicar por', 2, 5, 1, 2) + ctrl('b', 'Sumar', 1, 20, 1, 7) }[md];
    escena(el, C, function (o) { var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, P = function (v) { return v < 0 ? '(' + sig(v) + ')' : v; };
      if (md === 'verificar') { var c = o.a * 3 + o.b, val = o.a * o.x + o.b; return [{ vis: G(ecS(o.a, o.b) + ' = ' + c), txt: 'Una <b>ecuación</b>: una igualdad con un valor desconocido, la incógnita x.' }, { vis: G(o.a + ' · ' + P(o.x) + (o.b < 0 ? ' − ' + -o.b : ' + ' + o.b) + ' = ' + val), txt: 'Reemplazamos x por ' + o.x + ' en el primer miembro.' }, { vis: RS(val === c ? val + ' = ' + c + ' ✓' : val + ' ≠ ' + c), txt: val === c ? 'La igualdad se cumple: x = ' + o.x + ' es la <b>solución</b>.' : 'No se cumple: ' + o.x + ' no es solución. Probá con 3.' }]; }
      if (md === 'inversa') { var a = o.a, b = o.b, x = o.x, c2 = a * x + b; return [{ vis: G(ecS(a, b) + ' = ' + c2), txt: 'A x la multiplicaron por ' + a + ' y le ' + (b < 0 ? 'restaron ' + -b : 'sumaron ' + b) + '.' }, { vis: G(a + 'x = ' + c2 + (b < 0 ? ' + ' + -b : ' − ' + b) + ' = ' + (c2 - b)), txt: 'Deshacemos al revés: primero ' + (b < 0 ? 'sumamos ' + -b : 'restamos ' + b) + ' en los <b>dos miembros</b>.' }, { vis: G('x = ' + (c2 - b) + ' ÷ ' + a), txt: 'Después dividimos los dos miembros por ' + a + '.' }, { vis: RS('x = ' + x), txt: 'Verificamos: ' + a + ' · ' + P(x) + (b < 0 ? ' − ' + -b : ' + ' + b) + ' = ' + c2 + ' ✓' }]; }
      if (md === 'dos_miembros') { var a3 = o.a, c3 = Math.min(o.c, o.a - 1), b3 = o.b, x3 = o.x, d3 = a3 * x3 + b3 - c3 * x3; return [{ vis: G(ecS(a3, b3) + ' = ' + ecS(c3, d3)), txt: 'Hay x en los <b>dos miembros</b>.' }, { vis: G(ecS(a3 - c3, b3) + ' = ' + d3), txt: 'Restamos ' + ecS(c3, 0) + ' en los dos miembros: las x quedan de un solo lado.' }, { vis: G((a3 - c3) + 'x = ' + (d3 - b3)), txt: (b3 < 0 ? 'Sumamos ' + -b3 : 'Restamos ' + b3) + ' en los dos miembros.' }, { vis: RS('x = ' + x3), txt: 'Dividimos por ' + (a3 - c3) + '. Verificamos: los dos miembros dan ' + (a3 * x3 + b3) + '.' }]; }
      var x4 = o.x, a4 = o.a, b4 = o.b, r4 = a4 * x4 + b4, nom = a4 === 2 ? 'El doble' : a4 === 3 ? 'El triple' : a4 + ' veces'; return [{ vis: G('«' + nom + ' de un número más ' + b4 + ' es ' + r4 + '»'), txt: 'Llamamos x al número desconocido.' }, { vis: G(a4 + 'x + ' + b4 + ' = ' + r4), txt: 'Traducimos el enunciado a una ecuación.' }, { vis: G(a4 + 'x = ' + (r4 - b4) + ' → x = ' + x4), txt: 'Resolvemos con las operaciones inversas.' }, { vis: RS('El número es ' + x4), txt: 'Verificamos en el enunciado y respondemos con una oración.' }];
    });
  } };
  M.ecuaciones_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'verificar';
    respuesta(el, api, function () { var a = R(2, 6), x = R(-4, 9), b = R(-9, 12), c = a * x + b;
      if (md === 'verificar') { var pr = Math.random() < .5 ? x : x + R(1, 3); return { cons: '¿<b>x = ' + pr + '</b> es solución de <b>' + ecS(a, b) + ' = ' + c + '</b>? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: pr === x ? ['si', 'sí'] : ['no'] }], ayuda: 'Reemplazá x por ' + pr + ' y fijate si da ' + c + '.', bien: '¡Bien!' }; }
      var xn = R(3, 25), an = R(2, 4), bn = R(2, 15), nom = an === 2 ? 'el doble' : an === 3 ? 'el triple' : 'el cuádruple';
      return { cons: 'Si a ' + nom + ' de un número le sumás <b>' + bn + '</b>, da <b>' + (an * xn + bn) + '</b>. ¿Cuál es el número?', campos: [{ v: xn }], ayuda: 'Planteá ' + an + 'x + ' + bn + ' = ' + (an * xn + bn) + '.', bien: '¡Bien! ' + xn + '.' };
    });
  } };
  // ======= ÁNGULOS Y CONSTRUCCIONES (Matemática I · Misión 17) =======
  function svgSec(g, marcas) { var cx = 120, cy = 75, L = 95, a = g * Math.PI / 180, dx = Math.cos(a) * L, dy = Math.sin(a) * L, t = '<line class="rayo" x1="25" y1="75" x2="215" y2="75"/><line class="rayo" x1="' + (cx - dx).toFixed(1) + '" y1="' + (cy + dy).toFixed(1) + '" x2="' + (cx + dx).toFixed(1) + '" y2="' + (cy - dy).toFixed(1) + '"/>';
    var arco = function (a0, a1, cls) { var r = 22, p0 = [cx + r * Math.cos(a0), cy - r * Math.sin(a0)], p1 = [cx + r * Math.cos(a1), cy - r * Math.sin(a1)]; return '<path class="' + cls + '" d="M' + p0[0].toFixed(1) + ' ' + p0[1].toFixed(1) + ' A' + r + ' ' + r + ' 0 0 0 ' + p1[0].toFixed(1) + ' ' + p1[1].toFixed(1) + '"/>'; };
    if (marcas.indexOf('a') >= 0) t += arco(0, a, 'arc'); if (marcas.indexOf('b') >= 0) t += arco(a, Math.PI, 'arc arc2'); if (marcas.indexOf('c') >= 0) t += arco(Math.PI, Math.PI + a, 'arc');
    return '<svg viewBox="0 0 240 150" class="lb2-svg">' + t + '</svg>'; }
  M.geometria = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'relaciones', C = {
      relaciones: ctrl('g', 'Ángulo', 20, 160, 5, 60, '°'), rectas: ctrl('g', 'Ángulo entre las rectas', 0, 90, 15, 90, '°'),
      bisectriz: ctrl('g', 'Ángulo', 30, 170, 10, 80, '°'), mediatriz: ctrl('s', 'Largo del segmento', 4, 20, 1, 10, ' cm'), copiar: ctrl('s', 'Largo del segmento', 3, 12, 1, 6, ' cm') }[md];
    escena(el, C, function (o) { var RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; };
      if (md === 'relaciones') { var g = o.g; return [{ vis: svgSec(g, 'a'), txt: 'Dos rectas secantes forman un ángulo de <b>' + g + '°</b>.' }, { vis: svgSec(g, 'ab'), txt: 'Su vecino sobre la misma recta es el <b>adyacente</b>: juntos forman un llano, 180°. Mide ' + (180 - g) + '°.' }, { vis: svgSec(g, 'ac'), txt: 'El de enfrente es el <b>opuesto por el vértice</b>: mide igual, ' + g + '°.' }, { vis: svgSec(g, 'abc') + RS(g + '° + ' + (180 - g) + '° = 180°'), txt: 'Con un solo ángulo se conocen los cuatro.' }]; }
      if (md === 'rectas') { var g2 = o.g, sv = function (extra) { var a = g2 * Math.PI / 180, t = '<line class="rayo" x1="20" y1="95" x2="220" y2="95"/>'; t += g2 === 0 ? '<line class="rayo" x1="20" y1="55" x2="220" y2="55"/>' : '<line class="rayo" x1="' + (120 - 70 * Math.cos(a)).toFixed(1) + '" y1="' + (95 + 70 * Math.sin(a)).toFixed(1) + '" x2="' + (120 + 70 * Math.cos(a)).toFixed(1) + '" y2="' + (95 - 70 * Math.sin(a)).toFixed(1) + '"/>'; return '<svg viewBox="0 0 240 160" class="lb2-svg">' + t + (extra || '') + '</svg>'; };
        var tipo = g2 === 0 ? 'paralelas' : g2 === 90 ? 'perpendiculares' : 'secantes oblicuas';
        return [{ vis: sv(), txt: 'Dos rectas en el plano.' }, { vis: sv(g2 === 90 ? '<rect x="120" y="83" width="12" height="12" class="arc"/>' : ''), txt: g2 === 0 ? 'No se cortan nunca y están siempre a la misma distancia.' : 'Se cortan en un punto' + (g2 === 90 ? ' formando cuatro ángulos rectos.' : ', con ángulos que no son rectos.') }, { vis: sv() + RS('Son ' + tipo), txt: g2 === 0 ? 'Se trazan con regla y escuadra, deslizando la escuadra.' : g2 === 90 ? 'Las perpendiculares también son secantes. Se trazan con la escuadra.' : 'Las secantes que no son perpendiculares se llaman oblicuas.' }]; }
      if (md === 'bisectriz') { var g3 = o.g, cx = 120, cy = 128, rad = function (d) { return d * Math.PI / 180; }, pt = function (d, r) { return [(cx + r * Math.cos(rad(d))).toFixed(1), (cy - r * Math.sin(rad(d))).toFixed(1)]; }, base = '<line class="rayo" x1="' + cx + '" y1="' + cy + '" x2="' + pt(0, 105)[0] + '" y2="' + cy + '"/><line class="rayo" x1="' + cx + '" y1="' + cy + '" x2="' + pt(g3, 105)[0] + '" y2="' + pt(g3, 105)[1] + '"/>', A = pt(0, 55), B = pt(g3, 55), M2 = pt(g3 / 2, 92);
        var arc = '<path class="arc" d="M' + A[0] + ' ' + A[1] + ' A55 55 0 0 0 ' + B[0] + ' ' + B[1] + '"/>', cruces = '<circle class="pt" cx="' + M2[0] + '" cy="' + M2[1] + '" r="4"/>', bis = '<line class="diag" x1="' + cx + '" y1="' + cy + '" x2="' + pt(g3 / 2, 115)[0] + '" y2="' + pt(g3 / 2, 115)[1] + '"/>', sv = function (x) { return '<svg viewBox="0 0 240 140" class="lb2-svg">' + base + x + '</svg>'; };
        return [{ vis: sv(''), txt: 'Un ángulo de <b>' + g3 + '°</b>.' }, { vis: sv(arc), txt: 'Con el compás pinchado en el vértice, un arco que corte los dos lados.' }, { vis: sv(arc + cruces), txt: 'Desde cada corte, dos arcos iguales que se crucen adentro del ángulo.' }, { vis: sv(arc + cruces + bis) + RS(g3 + '° ÷ 2 = ' + fmt(g3 / 2) + '°'), txt: 'La recta del vértice al cruce es la <b>bisectriz</b>: divide el ángulo en dos iguales.' }]; }
      if (md === 'mediatriz') { var s5 = o.s, L = s5 * 9, x0 = 120 - L / 2, x1 = 120 + L / 2, base5 = '<line class="rayo" x1="' + x0 + '" y1="75" x2="' + x1 + '" y2="75"/><circle class="pt" cx="' + x0 + '" cy="75" r="3"/><circle class="pt" cx="' + x1 + '" cy="75" r="3"/>', r5 = L * .7, h = Math.sqrt(r5 * r5 - L * L / 4).toFixed(1);
        var arcs = '<circle class="arc" cx="' + x0 + '" cy="75" r="' + r5.toFixed(1) + '" style="fill:none;opacity:.5"/><circle class="arc" cx="' + x1 + '" cy="75" r="' + r5.toFixed(1) + '" style="fill:none;opacity:.5"/>', med = '<line class="diag" x1="120" y1="' + (75 - h) + '" x2="120" y2="' + (75 + +h) + '"/>', sv = function (x) { return '<svg viewBox="0 0 240 150" class="lb2-svg">' + base5 + x + '</svg>'; };
        return [{ vis: sv(''), txt: 'Un segmento de <b>' + s5 + ' cm</b>.' }, { vis: sv(arcs), txt: 'Con la misma abertura del compás (más de la mitad), un arco desde cada extremo.' }, { vis: sv(arcs + med), txt: 'Unimos los dos cruces: es la <b>mediatriz</b>, perpendicular al segmento.' }, { vis: sv(med) + RS('Lo corta a ' + fmt(s5 / 2) + ' cm de cada extremo'), txt: 'Pasa por el punto medio. Cada punto de la mediatriz está a igual distancia de los dos extremos.' }]; }
      var s6 = o.s, L6 = s6 * 14, sv6 = function (x) { return '<svg viewBox="0 0 240 120" class="lb2-svg"><line class="rayo" x1="30" y1="35" x2="' + (30 + L6) + '" y2="35"/><text x="' + (30 + L6 / 2) + '" y="25">' + s6 + ' cm</text>' + x + '</svg>'; };
      return [{ vis: sv6(''), txt: 'Queremos copiar este segmento sin medir con regla.' }, { vis: sv6('<path class="arc" d="M30 45 A' + L6 + ' ' + L6 + ' 0 0 0 ' + (30 + L6) + ' 45" style="fill:none"/>'), txt: 'Abrimos el compás de un extremo al otro: la abertura es igual al segmento.' }, { vis: sv6('<line class="rayo" x1="30" y1="90" x2="220" y2="90"/><circle class="pt" cx="30" cy="90" r="3"/>'), txt: 'En otra recta, marcamos un punto de inicio.' }, { vis: sv6('<line class="rayo" x1="30" y1="90" x2="220" y2="90"/><line class="diag" x1="30" y1="90" x2="' + (30 + L6) + '" y2="90"/><circle class="pt" cx="' + (30 + L6) + '" cy="90" r="4"/>') + RS('Copia de ' + s6 + ' cm'), txt: 'Sin cambiar la abertura, pinchamos en el punto y marcamos: el segmento quedó copiado.' }];
    });
  } };
  M.geometria_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'relaciones';
    respuesta(el, api, function () { var g = R(4, 34) * 5;
      if (md === 'relaciones') { var op = Math.random() < .5; return { cons: 'Dos rectas secantes forman un ángulo de <b>' + g + '°</b>. ¿Cuánto mide su ángulo ' + (op ? '<b>opuesto por el vértice</b>' : '<b>adyacente</b>') + '?', html: svgSec(g, 'a'), campos: [{ v: op ? g : 180 - g, un: '°' }], ayuda: op ? 'Los opuestos por el vértice son iguales.' : 'Los adyacentes suman 180°.', bien: '¡Bien!' }; }
      if (md === 'rectas') { var S = pick([['Las vías de un tren', 'paralelas'], ['Las líneas de un cuaderno', 'paralelas'], ['El borde de arriba y el costado de una hoja', 'perpendiculares'], ['Las calles de una esquina en cruz', 'perpendiculares'], ['Las dos agujas del reloj a las 2', 'secantes']]); return { cons: S[0] + ', ¿son <b>paralelas</b>, <b>perpendiculares</b> o <b>secantes</b> (oblicuas)?', campos: [{ tipo: 'texto', v: [S[1]] }], ayuda: 'Paralelas no se cortan; perpendiculares se cortan con ángulos rectos.', bien: '¡Bien!' }; }
      if (md === 'bisectriz') { var b = R(3, 34) * 5; return { cons: 'Trazás la bisectriz de un ángulo de <b>' + b + '°</b>. ¿Cuánto mide cada ángulo que queda?', campos: [{ v: b / 2, un: '°' }], ayuda: 'La bisectriz lo divide en dos ángulos iguales.', bien: '¡Bien!' }; }
      if (md === 'mediatriz') { var s = R(4, 30); return { cons: 'Un segmento mide <b>' + s + ' cm</b>. ¿A cuántos centímetros de cada extremo lo corta su mediatriz?', campos: [{ v: s / 2, un: 'cm' }], ayuda: 'Pasa por el punto medio.', bien: '¡Bien!' }; }
      var l = [R(2, 9), R(2, 9), R(2, 12)].sort(function (x, y) { return x - y; }), ok = l[2] < l[0] + l[1]; return { cons: '¿Se puede construir un triángulo con lados de <b>' + l.join(', ') + ' cm</b>? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: ok ? ['si', 'sí'] : ['no'] }], ayuda: '¿El lado más largo es menor que la suma de los otros dos? ' + l[0] + ' + ' + l[1] + ' = ' + (l[0] + l[1]) + '.', bien: '¡Bien!' };
    });
  } };

  // ======= TRIÁNGULOS Y CUADRILÁTEROS (Matemática I · Misión 18) =======
  function svgTri(A, B, C, extra) { var pts = [[30, 130], [210, 130], [30 + (C || 110), 30]]; return '<svg viewBox="0 0 240 150" class="lb2-svg"><polygon class="fig" points="' + pts.map(function (q) { return q.join(','); }).join(' ') + '" style="fill:none"/>' + (extra || '') + '</svg>'; }
  function svgCuad(tipo, diag) { var P = { cuadrado: [[70, 25], [170, 25], [170, 125], [70, 125]], rectangulo: [[40, 40], [200, 40], [200, 115], [40, 115]], rombo: [[120, 15], [195, 75], [120, 135], [45, 75]], paralelogramo: [[70, 35], [215, 35], [170, 120], [25, 120]], trapecio: [[80, 35], [160, 35], [215, 120], [25, 120]], trapezoide: [[60, 30], [190, 50], [210, 125], [30, 110]] }[tipo];
    var t = '<polygon class="fig" points="' + P.map(function (q) { return q.join(','); }).join(' ') + '" style="fill:none"/>'; if (diag) t += '<line class="diag" x1="' + P[0][0] + '" y1="' + P[0][1] + '" x2="' + P[2][0] + '" y2="' + P[2][1] + '"/><line class="diag" x1="' + P[1][0] + '" y1="' + P[1][1] + '" x2="' + P[3][0] + '" y2="' + P[3][1] + '"/>';
    return '<svg viewBox="0 0 240 150" class="lb2-svg">' + t + '</svg>'; }
  var CUAD = { trapezoide: ['ningún par de lados paralelos', 'no son iguales ni perpendiculares'], trapecio: ['un solo par de lados paralelos', 'no se cortan en su punto medio'], paralelogramo: ['dos pares de lados paralelos', 'se cortan en su punto medio'], rectangulo: ['paralelogramo con 4 ángulos rectos', 'son iguales y se cortan en su punto medio'], rombo: ['paralelogramo con 4 lados iguales', 'son perpendiculares y se cortan en su punto medio'], cuadrado: ['rectángulo y rombo a la vez', 'son iguales, perpendiculares y se cortan en su punto medio'] };
  M.figuras = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'exterior', C = {
      exterior: ctrl('a', 'Ángulo A', 20, 100, 5, 50, '°') + ctrl('b', 'Ángulo B', 20, 100, 5, 70, '°'),
      isosceles: ctrl('a', 'Ángulo desigual', 20, 140, 10, 40, '°'),
      ecuacion: ctrl('a', 'Veces x del 1.º', 1, 3, 1, 1) + ctrl('b', 'Veces x del 2.º', 1, 4, 1, 2) + ctrl('c', 'Veces x del 3.º', 1, 5, 1, 3),
      paralelogramo: ctrl('a', 'Un ángulo', 30, 150, 5, 65, '°'),
      cuadrilateros: '<div class="lb-fila"><label>Figura</label><select data-k="f"><option value="trapezoide">Trapezoide</option><option value="trapecio">Trapecio</option><option value="paralelogramo">Paralelogramo</option><option value="rectangulo">Rectángulo</option><option value="rombo" selected>Rombo</option><option value="cuadrado">Cuadrado</option></select></div>',
      suma360: ctrl('a', 'Ángulo 1', 50, 130, 5, 80, '°') + ctrl('b', 'Ángulo 2', 50, 130, 5, 100, '°') + ctrl('c', 'Ángulo 3', 50, 130, 5, 95, '°') }[md];
    if (md === 'diagonales') C = C || '<div class="lb-fila"><label>Figura</label><select data-k="f"><option value="paralelogramo">Paralelogramo</option><option value="rectangulo" selected>Rectángulo</option><option value="rombo">Rombo</option><option value="cuadrado">Cuadrado</option><option value="trapecio">Trapecio</option></select></div>';
    escena(el, C, function (o) { var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; };
      if (md === 'exterior') { var a = o.a, b = o.b, c = 180 - a - b; if (c <= 0) { b = 180 - a - 10; c = 10; } return [{ vis: svgTri() + G('A = ' + a + '° · B = ' + b + '°'), txt: 'Dos ángulos interiores del triángulo.' }, { vis: svgTri() + G('C = 180° − ' + a + '° − ' + b + '° = ' + c + '°'), txt: 'Los tres interiores suman <b>180°</b>.' }, { vis: svgTri() + G('Exterior de C = 180° − ' + c + '° = ' + (180 - c) + '°'), txt: 'El <b>ángulo exterior</b> es el adyacente a un interior: juntos suman 180°.' }, { vis: RS((180 - c) + '° = ' + a + '° + ' + b + '°'), txt: 'Mide lo mismo que la suma de los dos interiores <b>no adyacentes</b>.' }]; }
      if (md === 'isosceles') { var d = o.a, ig = (180 - d) / 2; return [{ vis: svgTri(0, 0, 90), txt: 'Un triángulo <b>isósceles</b> tiene dos lados iguales, y los ángulos de la base también son iguales.' }, { vis: G('180° − ' + d + '° = ' + (180 - d) + '°'), txt: 'Al total le restamos el ángulo desigual, ' + d + '°.' }, { vis: RS((180 - d) + '° ÷ 2 = ' + fmt(ig) + '°'), txt: 'Lo que queda se reparte entre los dos ángulos iguales. En el <b>equilátero</b>, los tres miden 60°.' }]; }
      if (md === 'ecuacion') { var k = o.a + o.b + o.c, x = 180 / k, nm = function (n) { return (n === 1 ? '' : n) + 'x'; }; return [{ vis: G(nm(o.a) + ', ' + nm(o.b) + ' y ' + nm(o.c)), txt: 'Los ángulos de un triángulo escritos con una incógnita.' }, { vis: G(nm(o.a) + ' + ' + nm(o.b) + ' + ' + nm(o.c) + ' = 180°'), txt: 'Como suman 180°, planteamos la ecuación.' }, { vis: G(k + 'x = 180° → x = ' + fmt(r2(x)) + '°'), txt: 'Juntamos términos semejantes y despejamos.' }, { vis: RS(fmt(r2(o.a * x)) + '°, ' + fmt(r2(o.b * x)) + '° y ' + fmt(r2(o.c * x)) + '°'), txt: 'Reemplazamos para obtener cada ángulo y verificamos que sumen 180°.' }]; }
      if (md === 'paralelogramo') { var a2 = o.a; return [{ vis: svgCuad('paralelogramo') + G('Un ángulo: ' + a2 + '°'), txt: 'Un paralelogramo tiene dos pares de lados paralelos.' }, { vis: svgCuad('paralelogramo') + G('Opuesto: ' + a2 + '°'), txt: 'Los ángulos <b>opuestos</b> son iguales.' }, { vis: svgCuad('paralelogramo') + G('Consecutivo: 180° − ' + a2 + '° = ' + (180 - a2) + '°'), txt: 'Los ángulos <b>consecutivos</b> suman 180°.' }, { vis: RS(a2 + '° + ' + (180 - a2) + '° + ' + a2 + '° + ' + (180 - a2) + '° = 360°'), txt: 'Con un solo ángulo se conocen los cuatro. Sus lados opuestos también son iguales.' }]; }
      if (md === 'cuadrilateros') { var f = o.f || 'rombo'; return [{ vis: svgCuad(f), txt: 'Un cuadrilátero tiene 4 lados. Se clasifica por sus lados paralelos.' }, { vis: svgCuad(f) + G(CUAD[f][0]), txt: f === 'trapezoide' ? 'Sin lados paralelos: <b>trapezoide</b>.' : f === 'trapecio' ? 'Un solo par: <b>trapecio</b>.' : 'Dos pares: es un <b>paralelogramo</b>.' }, { vis: svgCuad(f) + RS(f === 'cuadrado' ? 'Cuadrado ⊂ rectángulo y rombo ⊂ paralelogramo' : f === 'rectangulo' || f === 'rombo' ? (f === 'rombo' ? 'Rombo' : 'Rectángulo') + ' ⊂ paralelogramo' : f.charAt(0).toUpperCase() + f.slice(1)), txt: f === 'cuadrado' ? 'El cuadrado es a la vez rectángulo y rombo.' : f === 'rectangulo' || f === 'rombo' ? 'Es un paralelogramo especial.' : 'Los paralelogramos especiales son el rectángulo, el rombo y el cuadrado.' }]; }
      if (md === 'diagonales') { var f2 = o.f || 'rectangulo'; return [{ vis: svgCuad(f2), txt: 'Un ' + f2 + '.' }, { vis: svgCuad(f2, 1), txt: 'Las <b>diagonales</b> unen vértices opuestos: todo cuadrilátero tiene 2.' }, { vis: svgCuad(f2, 1) + RS('Diagonales: ' + CUAD[f2][1]), txt: f2 === 'trapecio' ? 'En el trapecio no se cortan en el punto medio.' : 'En todo paralelogramo se cortan en su punto medio; en los especiales, además, tienen otras propiedades.' }]; }
      var s3 = o.a + o.b + o.c, d4 = 360 - s3; return [{ vis: svgCuad('trapezoide'), txt: 'Un cuadrilátero cualquiera.' }, { vis: svgCuad('trapezoide', 0) + G('2 triángulos × 180° = 360°'), txt: 'Una diagonal lo parte en dos triángulos: sus ángulos suman <b>360°</b>.' }, { vis: G('360° − ' + o.a + '° − ' + o.b + '° − ' + o.c + '°'), txt: 'Si conocemos tres ángulos, restamos.' }, { vis: RS('Cuarto ángulo = ' + d4 + '°'), txt: d4 > 0 ? 'Verificamos que los cuatro sumen 360°.' : 'Da negativo: esos tres ángulos no pueden ser de un cuadrilátero.' }];
    });
  } };
  M.figuras_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'exterior';
    respuesta(el, api, function () {
      if (md === 'clasificar') { var T = pick([[[5, 5, 5], 'equilatero', 'equilátero'], [[6, 6, 4], 'isosceles', 'isósceles'], [[3, 4, 5], 'escaleno', 'escaleno'], [[7, 7, 3], 'isosceles', 'isósceles'], [[4, 6, 8], 'escaleno', 'escaleno']]); return { cons: 'Un triángulo tiene lados de <b>' + T[0].join(', ') + ' cm</b>. ¿Es equilátero, isósceles o escaleno?', campos: [{ tipo: 'texto', v: [T[1], T[2]] }], ayuda: 'Fijate cuántos lados son iguales.', bien: '¡Bien! Es ' + T[2] + '.' }; }
      if (md === 'exterior') { var a = R(5, 16) * 5, b = R(5, 16) * 5; return { cons: 'Dos ángulos interiores de un triángulo miden <b>' + a + '°</b> y <b>' + b + '°</b>. ¿Cuánto mide el ángulo exterior adyacente al tercero?', campos: [{ v: a + b, un: '°' }], ayuda: 'El exterior es igual a la suma de los dos interiores no adyacentes.', bien: '¡Bien!' }; }
      if (md === 'isosceles') { var d = R(2, 14) * 10; return { cons: 'En un triángulo isósceles el ángulo desigual mide <b>' + d + '°</b>. ¿Cuánto mide cada uno de los otros dos?', campos: [{ v: (180 - d) / 2, un: '°' }], ayuda: '(180° − ' + d + '°) ÷ 2.', bien: '¡Bien!' }; }
      if (md === 'ecuacion') { var k = pick([[1, 2, 3], [1, 1, 2], [2, 3, 4], [1, 2, 2], [1, 3, 5]]), s = k[0] + k[1] + k[2], nm = function (n) { return (n === 1 ? '' : n) + 'x'; }; return { cons: 'Los ángulos de un triángulo miden <b>' + nm(k[0]) + ', ' + nm(k[1]) + ' y ' + nm(k[2]) + '</b>. ¿Cuánto vale x?', campos: [{ v: r2(180 / s), un: '°' }], ayuda: s + 'x = 180°.', bien: '¡Bien!' }; }
      if (md === 'paralelogramo') { var g = R(6, 30) * 5, op = Math.random() < .5; return { cons: 'En un paralelogramo un ángulo mide <b>' + g + '°</b>. ¿Cuánto mide su ángulo ' + (op ? '<b>opuesto</b>' : '<b>consecutivo</b>') + '?', campos: [{ v: op ? g : 180 - g, un: '°' }], ayuda: op ? 'Los opuestos son iguales.' : 'Los consecutivos suman 180°.', bien: '¡Bien!' }; }
      if (md === 'diagonales') { var Q = pick([['las diagonales son iguales pero no perpendiculares', 'rectangulo', 'rectángulo'], ['las diagonales son perpendiculares pero no iguales', 'rombo', 'rombo'], ['las diagonales son iguales y perpendiculares', 'cuadrado', 'cuadrado']]); return { cons: '¿Qué paralelogramo tiene ' + Q[0] + '?', campos: [{ tipo: 'texto', v: [Q[1], Q[2]] }], ayuda: 'Rectángulo: iguales. Rombo: perpendiculares. Cuadrado: las dos cosas.', bien: '¡Bien!' }; }
      var x = R(14, 22) * 5, y = R(14, 22) * 5, z = R(14, 22) * 5; return { cons: 'Tres ángulos de un cuadrilátero miden <b>' + x + '°, ' + y + '° y ' + z + '°</b>. ¿Cuánto mide el cuarto?', campos: [{ v: 360 - x - y - z, un: '°' }], ayuda: 'Los cuatro suman 360°.', bien: '¡Bien!' };
    });
  } };
  // ======= PERÍMETRO, ÁREA Y VOLUMEN (Matemática I · Misión 19) =======
  M.medida = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'perimetro', C = {
      perimetro: ctrl('a', 'Largo', 2, 12, 1, 8, ' cm') + ctrl('b', 'Ancho', 1, 8, 1, 3, ' cm'),
      misma_unidad: ctrl('a', 'Largo', 1, 5, 1, 2, ' m') + ctrl('b', 'Ancho', 10, 90, 10, 50, ' cm'),
      circulo: ctrl('d', 'Diámetro', 2, 40, 1, 10, ' cm'),
      compuesta: ctrl('a', 'Largo', 6, 12, 1, 10, ' cm') + ctrl('b', 'Ancho', 4, 8, 1, 6, ' cm') + ctrl('c', 'Lado del recorte', 1, 3, 1, 2, ' cm'),
      capacidad: ctrl('a', 'Largo', 10, 60, 5, 40, ' cm') + ctrl('b', 'Ancho', 10, 40, 5, 25, ' cm') + ctrl('c', 'Alto', 10, 40, 5, 30, ' cm') }[md];
    escena(el, C, function (o) { var G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; };
      var rect = function (a, b, rec) { var k = Math.min(180 / a, 100 / b), w = a * k, h = b * k; return '<svg viewBox="0 0 240 130" class="lb2-svg"><rect class="fig" x="' + (120 - w / 2) + '" y="' + (65 - h / 2) + '" width="' + w + '" height="' + h + '" style="fill-opacity:.25"/>' + (rec ? '<rect x="' + (120 + w / 2 - rec * k) + '" y="' + (65 - h / 2) + '" width="' + rec * k + '" height="' + rec * k + '" style="fill:#fff;stroke:#e11;stroke-dasharray:4"/>' : '') + '</svg>'; };
      if (md === 'perimetro') { var a = o.a, b = o.b; return [{ vis: rect(a, b), txt: 'El <b>perímetro</b> es el largo del borde: la vuelta completa.' }, { vis: rect(a, b) + G(a + ' + ' + b + ' + ' + a + ' + ' + b), txt: 'Sumamos los cuatro lados.' }, { vis: RS('P = 2 × ' + a + ' + 2 × ' + b + ' = ' + (2 * a + 2 * b) + ' cm'), txt: 'Se mide en unidades de <b>longitud</b>: cm, m…' }]; }
      if (md === 'misma_unidad') { var a1 = o.a, b1 = o.b; return [{ vis: G(a1 + ' m y ' + b1 + ' cm'), txt: 'Las medidas están en unidades distintas.' }, { vis: G(a1 + ' m = ' + a1 * 100 + ' cm'), txt: 'Antes de operar, pasamos todo a la misma unidad.' }, { vis: RS('P = 2 × ' + a1 * 100 + ' + 2 × ' + b1 + ' = ' + (2 * a1 * 100 + 2 * b1) + ' cm'), txt: 'Ahora sí calculamos. Sumar 2 m + 50 cm como 52 sería un error.' }]; }
      if (md === 'circulo') { var d = o.d, c = r2(3.14 * d); return [{ vis: '<svg viewBox="0 0 240 130" class="lb2-svg"><circle class="fig" cx="120" cy="65" r="50" style="fill-opacity:.2"/><line class="diag" x1="70" y1="65" x2="170" y2="65"/></svg>', txt: 'Un círculo de <b>' + d + ' cm</b> de diámetro.' }, { vis: G('La vuelta ≈ 3,14 × diámetro'), txt: 'La longitud de la circunferencia es un poco más de 3 veces el diámetro: ese número es <b>π ≈ 3,14</b>.' }, { vis: RS('3,14 × ' + d + ' = ' + fmt(c) + ' cm'), txt: 'Es el perímetro del círculo (aproximado).' }]; }
      if (md === 'compuesta') { var a3 = o.a, b3 = o.b, c3 = o.c; return [{ vis: rect(a3, b3, c3), txt: 'Un rectángulo al que le recortaron un cuadrado de ' + c3 + ' cm.' }, { vis: rect(a3, b3) + G(a3 + ' × ' + b3 + ' = ' + a3 * b3 + ' cm²'), txt: 'Calculamos el área del rectángulo entero.' }, { vis: rect(a3, b3, c3) + G(c3 + ' × ' + c3 + ' = ' + c3 * c3 + ' cm²'), txt: 'El área del recorte.' }, { vis: RS(a3 * b3 + ' − ' + c3 * c3 + ' = ' + (a3 * b3 - c3 * c3) + ' cm²'), txt: 'Restamos. Las figuras compuestas se parten o se completan en figuras conocidas.' }]; }
      var V = o.a * o.b * o.c; return [{ vis: G(o.a + ' cm × ' + o.b + ' cm × ' + o.c + ' cm'), txt: 'Una pecera con forma de prisma.' }, { vis: G('V = ' + fmt(V) + ' cm³'), txt: 'El volumen es largo × ancho × alto.' }, { vis: G(fmt(V) + ' cm³ = ' + fmt(V / 1000) + ' dm³'), txt: '1 dm³ = 1.000 cm³: dividimos por 1.000.' }, { vis: RS(fmt(V / 1000) + ' litros'), txt: '<b>1 dm³ = 1 litro</b>: el volumen se vuelve capacidad.' }];
    });
  } };
  M.medida_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'perimetro';
    respuesta(el, api, function () {
      if (md === 'perimetro') { var a = R(3, 30), b = R(2, 20); return { cons: 'Una huerta rectangular mide <b>' + a + ' m</b> por <b>' + b + ' m</b>. ¿Cuántos metros de alambre hacen falta para darle una vuelta?', campos: [{ v: 2 * a + 2 * b, un: 'm' }], ayuda: 'Es el perímetro: 2 × ' + a + ' + 2 × ' + b + '.', bien: '¡Bien!' }; }
      if (md === 'misma_unidad') { var m = R(1, 4), c = R(1, 9) * 10; return { cons: 'Un rectángulo mide <b>' + m + ' m</b> de largo y <b>' + c + ' cm</b> de ancho. ¿Cuál es su perímetro en cm?', campos: [{ v: 2 * m * 100 + 2 * c, un: 'cm' }], ayuda: 'Primero ' + m + ' m = ' + m * 100 + ' cm.', bien: '¡Bien!' }; }
      if (md === 'circulo') { var d = R(2, 30); return { cons: 'Una rueda tiene <b>' + d + ' cm</b> de diámetro. Usando 3,14, ¿cuánto avanza en una vuelta?', campos: [{ v: r2(3.14 * d), un: 'cm' }], ayuda: '3,14 × ' + d + '.', bien: '¡Bien!' }; }
      if (md === 'compuesta') { var a3 = R(6, 15), b3 = R(4, 10), c3 = R(1, 3); return { cons: 'A un rectángulo de <b>' + a3 + ' cm × ' + b3 + ' cm</b> se le recorta un cuadrado de <b>' + c3 + ' cm</b> de lado. ¿Qué área queda?', campos: [{ v: a3 * b3 - c3 * c3, un: 'cm²' }], ayuda: a3 * b3 + ' − ' + c3 * c3 + '.', bien: '¡Bien!' }; }
      var x = R(2, 6) * 10, y = R(2, 5) * 10, z = R(2, 5) * 10; return { cons: '¿Cuántos litros entran en una pecera de <b>' + x + ' cm × ' + y + ' cm × ' + z + ' cm</b>?', campos: [{ v: x * y * z / 1000, un: 'l' }], ayuda: 'V en cm³ ÷ 1.000 = litros (1 dm³ = 1 litro).', bien: '¡Bien!' };
    });
  } };

  // ======= BANCO MATEMÁTICA I M20 + MATEMÁTICA II =======
  var _G = function (x) { return '<p class="lb-pt-g">' + x + '</p>'; }, _RS = function (x) { return '<p class="lb-cn-res">' + x + '</p>'; }, _F = function (x) { return '<p class="lb-pt-f">' + x + '</p>'; };
  function _fr(a, b) { if (b < 0) { a = -a; b = -b; } return (a < 0 ? '−' : '') + fr(Math.abs(a), b); }
  // ---- datos: gráficos, media/moda, azar
  M.datos = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'circular', C = {
      circular: ctrl('a', 'Fútbol', 1, 20, 1, 10) + ctrl('b', 'Vóley', 1, 20, 1, 6) + ctrl('c', 'Tenis', 1, 20, 1, 4),
      lineas: ctrl('a', 'Lunes', 0, 30, 1, 12) + ctrl('b', 'Martes', 0, 30, 1, 18) + ctrl('c', 'Miércoles', 0, 30, 1, 15) + ctrl('d', 'Jueves', 0, 30, 1, 22),
      media_moda: ctrl('a', 'Dato 1', 1, 10, 1, 7) + ctrl('b', 'Dato 2', 1, 10, 1, 9) + ctrl('c', 'Dato 3', 1, 10, 1, 7) + ctrl('d', 'Dato 4', 1, 10, 1, 5),
      muestral: ctrl('n', 'Caras del dado', 4, 8, 2, 6) }[md];
    if (md === 'azar') C = '';
    escena(el, C, function (o) {
      if (md === 'circular') { var t = o.a + o.b + o.c, v = [o.a, o.b, o.c], nom = ['Fútbol', 'Vóley', 'Tenis'], cols = ['#0e7c7b', '#f2a541', '#5b8def'], ang = 0, sec = '';
        v.forEach(function (x, i) { var a0 = ang, a1 = ang + x / t * 2 * Math.PI; ang = a1; sec += '<path d="M120 70 L' + (120 + 55 * Math.cos(a0)).toFixed(1) + ' ' + (70 + 55 * Math.sin(a0)).toFixed(1) + ' A55 55 0 ' + (a1 - a0 > Math.PI ? 1 : 0) + ' 1 ' + (120 + 55 * Math.cos(a1)).toFixed(1) + ' ' + (70 + 55 * Math.sin(a1)).toFixed(1) + ' Z" fill="' + cols[i] + '"/>'; });
        var sv = '<svg viewBox="0 0 240 140" class="lb2-svg">' + sec + '</svg>';
        return [{ vis: _G(nom.map(function (n, i) { return n + ': ' + v[i]; }).join(' · ') + ' · Total: ' + t), txt: 'Los datos y el total.' }, { vis: _G(nom.map(function (n, i) { return n + ': ' + v[i] + '/' + t + ' = ' + fmt(r2(v[i] / t * 100)) + ' %'; }).join('<br>')), txt: 'Cada parte del total, como fracción y porcentaje.' }, { vis: sv + _F(nom.map(function (n, i) { return n + ': ' + fmt(r2(v[i] / t * 360)) + '°'; }).join(' · ')), txt: 'Cada porción del círculo es esa parte de <b>360°</b>.' }, { vis: sv + _RS('Muestra partes de un total'), txt: 'El <b>gráfico circular</b> sirve para comparar cada parte con el todo.' }]; }
      if (md === 'lineas') { var d = [o.a, o.b, o.c, o.d], mx = Math.max.apply(null, d) || 1, pts = d.map(function (y, i) { return (30 + i * 60) + ',' + (120 - y / mx * 95).toFixed(1); }), sv2 = function (k) { return '<svg viewBox="0 0 240 140" class="lb2-svg"><line class="rayo" x1="20" y1="122" x2="230" y2="122"/>' + (k > 1 ? '<polyline class="diag" fill="none" points="' + pts.join(' ') + '"/>' : '') + pts.map(function (q) { var c = q.split(','); return '<circle class="pt" cx="' + c[0] + '" cy="' + c[1] + '" r="4"/>'; }).join('') + '</svg>'; };
        var sube = d[3] > d[0]; return [{ vis: sv2(1), txt: 'Un punto por día: la altura es el dato.' }, { vis: sv2(2), txt: 'Unimos los puntos en orden.' }, { vis: sv2(2) + _RS(sube ? 'En total, sube' : 'En total, baja'), txt: 'El <b>gráfico de líneas</b> muestra cómo cambia algo en el tiempo: dónde sube y dónde baja.' }]; }
      if (md === 'media_moda') { var x = [o.a, o.b, o.c, o.d], s2 = x.reduce(function (a, b) { return a + b; }, 0), cuenta = {}; x.forEach(function (v) { cuenta[v] = (cuenta[v] || 0) + 1; }); var mxc = Math.max.apply(null, Object.keys(cuenta).map(function (k) { return cuenta[k]; })), modas = Object.keys(cuenta).filter(function (k) { return cuenta[k] === mxc; });
        return [{ vis: _G(x.join(', ')), txt: 'Cuatro datos.' }, { vis: _G('(' + x.join(' + ') + ') ÷ 4 = ' + fmt(r2(s2 / 4))), txt: 'La <b>media</b> (promedio): sumamos todos y dividimos por la cantidad.' }, { vis: _RS(mxc > 1 ? 'Moda: ' + modas.join(' y ') : 'No hay moda'), txt: mxc > 1 ? 'La <b>moda</b> es el dato que más se repite.' : 'Ningún dato se repite: no hay moda.' }]; }
      if (md === 'muestral') { var n = o.n, L = []; for (var i = 1; i <= n; i++) L.push(i); var pares = L.filter(function (v) { return v % 2 === 0; }); return [{ vis: _G('Dado de ' + n + ' caras'), txt: 'Un experimento de azar: no se sabe qué va a salir.' }, { vis: _G('E = {' + L.join(', ') + '}'), txt: 'El <b>espacio muestral</b> es la lista de todos los resultados posibles.' }, { vis: _G('«Sale par» = {' + pares.join(', ') + '}'), txt: 'Un <b>suceso</b> es una parte del espacio muestral.' }, { vis: _RS(pares.length + ' de ' + n + ' resultados'), txt: 'Contar casos así prepara el cálculo de probabilidades.' }]; }
      return [{ vis: _G('Tirar una moneda · Sumar 2 + 3'), txt: '¿Se puede saber el resultado antes?' }, { vis: _F('2 + 3 siempre da 5'), txt: 'Si siempre da lo mismo, <b>no es de azar</b> (es determinista).' }, { vis: _RS('La moneda es azar'), txt: 'Si se conocen los resultados posibles pero no cuál va a salir, el experimento es <b>de azar</b>.' }];
    });
  } };
  M.datos_x = { tipo: 'ejercicio', render: function (el, p, api) { var md = p.modo || 'circular';
    respuesta(el, api, function () {
      if (md === 'circular') { var t = pick([20, 40, 60, 90, 120]), a = t * pick([1, 1, 3]) / 4; return { cons: 'En una encuesta a <b>' + t + '</b> personas, <b>' + a + '</b> eligieron fútbol. ¿Cuántos grados mide la porción de fútbol en un gráfico circular?', campos: [{ v: a / t * 360, un: '°' }], ayuda: a + '/' + t + ' de 360°.', bien: '¡Bien!' }; }
      if (md === 'lineas') { var d = [R(5, 20), R(5, 20), R(5, 20), R(5, 20)], i = R(0, 2), sube = d[i + 1] > d[i]; if (d[i + 1] === d[i]) d[i + 1]++; return { cons: 'Un gráfico de líneas marca la temperatura: <b>' + d.join(' °C, ') + ' °C</b> (de lunes a jueves). Del día ' + (i + 1) + ' al ' + (i + 2) + ', ¿la línea <b>sube</b> o <b>baja</b>?', campos: [{ tipo: 'texto', v: [d[i + 1] > d[i] ? 'sube' : 'baja'] }], ayuda: 'Compará ' + d[i] + ' y ' + d[i + 1] + '.', bien: '¡Bien!' }; }
      if (md === 'media_moda') { var x = [R(2, 10), R(2, 10), R(2, 10)]; x.push(x[0]); var s2 = x.reduce(function (a, b) { return a + b; }, 0); if (s2 % 4) { x[1] += 4 - s2 % 4; s2 = x.reduce(function (a, b) { return a + b; }, 0); } return { cons: 'Las notas de Luz fueron <b>' + x.join(', ') + '</b>. ¿Cuál es la media?', campos: [{ v: s2 / 4 }], ayuda: 'Sumá todas y dividí por 4.', bien: '¡Bien!' }; }
      if (md === 'muestral') { var n = pick([4, 6, 8, 10]); return { cons: 'Se gira una ruleta con los números del <b>1 al ' + n + '</b>. ¿Cuántos resultados tiene el espacio muestral del suceso «sale un número par»?', campos: [{ v: n / 2 }], ayuda: 'Escribí los pares del 1 al ' + n + '.', bien: '¡Bien!' }; }
      var S = pick([['Sacar una bolita de una bolsa sin mirar', 'azar'], ['Calcular el doble de 8', 'no'], ['Tirar un dado', 'azar'], ['Soltar una piedra y ver si cae', 'no'], ['Sortear quién empieza', 'azar']]); return { cons: '«' + S[0] + '»: ¿es un experimento de azar? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: S[1] === 'azar' ? ['si', 'sí'] : ['no'] }], ayuda: '¿Se puede saber el resultado antes?', bien: '¡Bien!' };
    }); } };
  // ---- racionales (Matemática II M1-M3)
  M.racionales = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'recta_neg', C = {
      recta_neg: ctrl('a', 'Numerador', -11, 11, 1, -3) + ctrl('b', 'Denominador', 2, 4, 1, 4),
      punto_medio: ctrl('a', 'Primer número', -6, 6, .5, -1) + ctrl('b', 'Segundo número', -6, 6, .5, 2),
      mixto: ctrl('a', 'Cifra que no se repite', 1, 9, 1, 1) + ctrl('b', 'Período', 1, 9, 1, 6),
      mezcla: ctrl('a', 'Decimal (décimos)', 1, 9, 1, 5) + ctrl('b', 'Denominador de la fracción', 2, 6, 1, 3),
      pot_neg: ctrl('a', 'Numerador', 1, 4, 1, 2) + ctrl('b', 'Denominador', 2, 5, 1, 3) + ctrl('n', 'Exponente', 2, 3, 1, 3),
      exp_neg: ctrl('a', 'Base: numerador', 1, 5, 1, 2) + ctrl('b', 'Base: denominador', 1, 5, 1, 3) + ctrl('n', 'Exponente negativo', 1, 3, 1, 2),
      raiz_frac: ctrl('a', 'Raíz del numerador', 1, 9, 1, 3) + ctrl('b', 'Raíz del denominador', 2, 10, 1, 5) }[md];
    escena(el, C, function (o) {
      if (md === 'recta_neg') { var a = o.a || -1, b = o.b, X = function (v) { return 120 + v * 30; }, t = ''; for (var k = -3 * b; k <= 3 * b; k++) t += '<line class="rayo" x1="' + X(k / b) + '" y1="' + (k % b ? 32 : 26) + '" x2="' + X(k / b) + '" y2="' + (k % b ? 40 : 46) + '"/>' + (k % b ? '' : '<text x="' + X(k / b) + '" y="62">' + sig(k / b) + '</text>');
        var sv = function (pt) { return '<svg viewBox="0 0 240 70" class="lb2-svg"><line class="rayo" x1="20" y1="36" x2="220" y2="36"/>' + t + (pt ? '<circle class="pt" cx="' + X(a / b) + '" cy="36" r="6"/>' : '') + '</svg>'; };
        return [{ vis: sv(0), txt: 'Cada entero partido en <b>' + b + '</b> partes, también del lado negativo.' }, { vis: sv(1), txt: 'Contamos ' + Math.abs(a) + ' partes desde el 0 hacia la ' + (a < 0 ? '<b>izquierda</b>' : '<b>derecha</b>') + '.' }, { vis: sv(1) + _RS(_fr(a, b) + ' está entre ' + sig(Math.floor(a / b)) + ' y ' + sig(Math.floor(a / b) + 1)), txt: 'Los racionales negativos se ubican igual que los positivos, del otro lado del 0.' }]; }
      if (md === 'punto_medio') { var x = o.a, y = o.b; return [{ vis: _G(fmt(x) + ' y ' + fmt(y)), txt: 'Buscamos el número que está justo en el medio.' }, { vis: _G('(' + fmt(x) + ' + ' + fmt(y) + ') ÷ 2'), txt: 'Sumamos los dos y dividimos por 2.' }, { vis: _RS('Punto medio = ' + fmt(r2((x + y) / 2))), txt: 'Está a la misma distancia de los dos. Repitiéndolo, siempre aparece otro en el medio: hay <b>infinitos</b>.' }]; }
      if (md === 'mixto') { var a3 = o.a, b3 = o.b, num = a3 * 10 + b3 - a3, g = mcd(num, 90); return [{ vis: _G('0,' + a3 + '<span class="lb2-per">' + b3 + '</span>'), txt: 'Un periódico <b>mixto</b>: el ' + a3 + ' no se repite y el ' + b3 + ' sí.' }, { vis: _G('Numerador: ' + a3 + b3 + ' − ' + a3 + ' = ' + num), txt: 'Arriba: el número completo sin coma menos la parte que no se repite.' }, { vis: _G('Denominador: 90'), txt: 'Abajo: un 9 por cada cifra del período y un 0 por cada cifra que no se repite.' }, { vis: _RS('0,' + a3 + '<span class="lb2-per">' + b3 + '</span> = ' + fr(num, 90) + (g > 1 ? ' = ' + fr(num / g, 90 / g) : '')), txt: 'Simplificamos al final.' }]; }
      if (md === 'mezcla') { var d = o.a / 10, b4 = o.b, g4 = mcd(o.a, 10); return [{ vis: _G(fmt(d) + ' + ' + fr(1, b4)), txt: 'Un decimal y una fracción: hay que llevarlos al <b>mismo formato</b>.' }, { vis: _G(fmt(d) + ' = ' + fr(o.a / g4, 10 / g4)), txt: 'Pasamos el decimal a fracción (si la fracción diera periódico, conviene todo a fracción).' }, { vis: _G(fr(o.a / g4, 10 / g4) + ' + ' + fr(1, b4) + ' = ' + fr(o.a / g4 * b4 + 10 / g4, 10 / g4 * b4)), txt: 'Sumamos con denominador común.' }, { vis: _RS('= ' + (function () { var n = o.a / g4 * b4 + 10 / g4, dd = 10 / g4 * b4, g = mcd(n, dd); return fr(n / g, dd / g); })()), txt: 'Simplificamos.' }]; }
      if (md === 'pot_neg') { var a5 = o.a, b5 = o.b, n5 = o.n, sg = n5 % 2 ? '−' : ''; return [{ vis: _G('(−' + fr(a5, b5) + ')<sup>' + n5 + '</sup>'), txt: 'Una fracción negativa elevada a ' + n5 + '.' }, { vis: _F('Exponente ' + (n5 % 2 ? 'impar → negativo' : 'par → positivo')), txt: 'El signo sigue la regla de los enteros.' }, { vis: _RS(sg + fr(Math.pow(a5, n5), Math.pow(b5, n5))), txt: 'Se elevan numerador y denominador.' }]; }
      if (md === 'exp_neg') { var a6 = o.a, b6 = o.b, n6 = o.n; return [{ vis: _G('(' + fr(a6, b6) + ')<sup>−' + n6 + '</sup>'), txt: 'Un exponente <b>negativo</b>.' }, { vis: _G('(' + fr(b6, a6) + ')<sup>' + n6 + '</sup>'), txt: 'Se invierte la base y el exponente pasa a positivo.' }, { vis: _RS('= ' + fr(Math.pow(b6, n6), Math.pow(a6, n6))), txt: 'No da un número negativo: el signo del exponente indica <b>inverso</b>.' }]; }
      var a7 = o.a, b7 = o.b; return [{ vis: _G('√' + fr(a7 * a7, b7 * b7)), txt: 'La raíz de una fracción.' }, { vis: _G(fr('√' + a7 * a7, '√' + b7 * b7)), txt: 'Se calcula la raíz del numerador y la del denominador.' }, { vis: _RS('= ' + fr(a7, b7)), txt: 'Control: (' + fr(a7, b7) + ')² = ' + fr(a7 * a7, b7 * b7) + '. Ojo: la raíz no se distribuye en la suma.' }];
    });
  } };
  M.racionales_x = { tipo: 'ejercicio', render: function (el, p, api) { var md = p.modo || 'recta_neg';
    respuesta(el, api, function () { var F = function (n, d) { return { tipo: 'frac', v: n / d, n: n, d: d }; };
      if (md === 'recta_neg') { var b = R(2, 5), a = -R(b + 1, 3 * b); if (a % b === 0) a--; return { cons: '¿Entre qué dos enteros está <b>' + _fr(a, b) + '</b> en la recta?', campos: [{ lab: 'entre', v: Math.floor(a / b) }, { lab: 'y', v: Math.floor(a / b) + 1 }], ayuda: 'Es negativo: queda a la izquierda del 0. ' + Math.abs(a) + ' ÷ ' + b + '.', bien: '¡Bien!' }; }
      if (md === 'punto_medio') { var x = R(-8, 4), y = x + 2 * R(1, 5) + (Math.random() < .5 ? 1 : 0); return { cons: '¿Cuál es el punto medio entre <b>' + sig(x) + '</b> y <b>' + sig(y) + '</b>?', campos: [{ v: (x + y) / 2 }], ayuda: '(' + x + ' + ' + y + ') ÷ 2.', bien: '¡Bien!' }; }
      if (md === 'mixto') { var a3 = R(1, 8), b3 = R(1, 9); if (b3 === a3) b3 = a3 + 1 > 9 ? 1 : a3 + 1; var num = a3 * 10 + b3 - a3, g = mcd(num, 90); return { cons: 'Pasá <b>0,' + a3 + '<span class="lb2-per">' + b3 + '</span></b> a fracción irreducible.', campos: [{ lab: 'numerador', v: num / g }, { lab: 'denominador', v: 90 / g }], ayuda: '(' + a3 + b3 + ' − ' + a3 + ') / 90, y simplificá.', bien: '¡Bien!' }; }
      if (md === 'mezcla') { var d = R(1, 9), b4 = pick([2, 4, 5]), n4 = d * b4 + 10, dd = 10 * b4, g4 = mcd(n4, dd); return { cons: 'Calculá <b>' + fmt(d / 10) + ' + 1/' + b4 + '</b> y escribí el resultado como fracción irreducible.', campos: [{ lab: 'numerador', v: n4 / g4 }, { lab: 'denominador', v: dd / g4 }], ayuda: fmt(d / 10) + ' = ' + d + '/10. Denominador común.', bien: '¡Bien!' }; }
      if (md === 'pot_neg') { var a5 = R(1, 3), b5 = R(a5 + 1, 5), n5 = R(2, 3); return { cons: 'Calculá <b>(−' + a5 + '/' + b5 + ')<sup>' + n5 + '</sup></b>', campos: [F((n5 % 2 ? -1 : 1) * Math.pow(a5, n5), Math.pow(b5, n5))], ayuda: 'Exponente ' + (n5 % 2 ? 'impar: queda negativo.' : 'par: queda positivo.'), bien: '¡Bien!' }; }
      if (md === 'exp_neg') { var a6 = R(1, 4), b6 = R(2, 5), n6 = R(1, 2); return { cons: 'Calculá <b>(' + a6 + '/' + b6 + ')<sup>−' + n6 + '</sup></b>', campos: [F(Math.pow(b6, n6), Math.pow(a6, n6))], ayuda: 'Invertí la base: (' + b6 + '/' + a6 + ')' + (n6 > 1 ? '²' : '') + '.', bien: '¡Bien!' }; }
      var a7 = R(1, 9), b7 = R(2, 10); return { cons: 'Calculá <b>√(' + a7 * a7 + '/' + b7 * b7 + ')</b>', campos: [F(a7, b7)], ayuda: 'Raíz del numerador y del denominador.', bien: '¡Bien!' };
    }); } };
  // ---- porcentajes y regla de tres compuesta (Matemática II M4-M5)
  M.porcentajes = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'factor', C = {
      factor: ctrl('t', 'Precio', 100, 5000, 100, 2000, ' $') + ctrl('p', 'Porcentaje', 5, 50, 5, 20, ' %'),
      sucesivos: ctrl('t', 'Precio', 1000, 10000, 500, 1000, ' $') + ctrl('p', 'Aumento', 5, 50, 5, 10, ' %') + ctrl('q', 'Descuento', 5, 50, 5, 10, ' %'),
      interes: ctrl('c', 'Capital', 1000, 50000, 1000, 10000, ' $') + ctrl('r', 'Tasa anual', 1, 20, 1, 5, ' %') + ctrl('t', 'Años', 1, 6, 1, 3),
      variacion: ctrl('a', 'Valor inicial', 100, 2000, 100, 800) + ctrl('b', 'Valor final', 100, 2000, 100, 1000),
      compuesta: ctrl('a', 'Obreros', 2, 8, 1, 4) + ctrl('d', 'Días', 2, 10, 1, 6) + ctrl('m', 'Metros', 10, 60, 10, 30) + ctrl('a2', 'Obreros nuevos', 2, 12, 1, 8) + ctrl('m2', 'Metros nuevos', 10, 120, 10, 60) }[md];
    escena(el, C, function (o) {
      if (md === 'factor') { var t = o.t, pc = o.p; return [{ vis: _G('$' + fmt(t) + ' con un aumento del ' + pc + ' %'), txt: 'En vez de calcular el porcentaje y sumarlo, usamos un <b>factor</b>.' }, { vis: _G('100 % + ' + pc + ' % = ' + (100 + pc) + ' % → × ' + fmt((100 + pc) / 100)), txt: 'Aumento: se paga el ' + (100 + pc) + ' %. Descuento: el ' + (100 - pc) + ' % (× ' + fmt((100 - pc) / 100) + ').' }, { vis: _RS('Aumento: $' + fmt(r2(t * (100 + pc) / 100)) + ' · Descuento: $' + fmt(r2(t * (100 - pc) / 100))), txt: 'Una sola multiplicación da el precio final.' }]; }
      if (md === 'sucesivos') { var t2 = o.t, a = o.p, q = o.q, f1 = t2 * (100 + a) / 100, f2 = f1 * (100 - q) / 100; return [{ vis: _G('$' + fmt(t2) + ' · +' + a + ' % y después −' + q + ' %'), txt: 'Dos cambios uno después del otro.' }, { vis: _G('$' + fmt(t2) + ' × ' + fmt((100 + a) / 100) + ' = $' + fmt(r2(f1))), txt: 'El primero, sobre el precio original.' }, { vis: _G('$' + fmt(r2(f1)) + ' × ' + fmt((100 - q) / 100) + ' = $' + fmt(r2(f2))), txt: 'El segundo se calcula sobre el <b>nuevo</b> precio.' }, { vis: _RS('$' + fmt(r2(f2)) + (a === q ? ' ≠ $' + fmt(t2) : '')), txt: 'Los porcentajes sucesivos <b>no se suman</b>: se multiplican los factores.' }]; }
      if (md === 'interes') { var c = o.c, r = o.r, t3 = o.t, I = c * r / 100 * t3; return [{ vis: _G('Capital $' + fmt(c) + ' · ' + r + ' % anual · ' + t3 + ' años'), txt: 'Los datos del interés simple.' }, { vis: _G('Interés de un año: ' + fmt(c) + ' × ' + r + ' ÷ 100 = $' + fmt(c * r / 100)), txt: 'Cada año se gana el mismo interés, calculado sobre el capital inicial.' }, { vis: _G('I = $' + fmt(c * r / 100) + ' × ' + t3 + ' = $' + fmt(I)), txt: 'Multiplicamos por la cantidad de años: I = C × r × t ÷ 100.' }, { vis: _RS('Monto = $' + fmt(c) + ' + $' + fmt(I) + ' = $' + fmt(c + I)), txt: 'El <b>monto</b> es capital más interés.' }]; }
      if (md === 'variacion') { var a4 = o.a, b4 = o.b, v = (b4 - a4) / a4 * 100; return [{ vis: _G('De ' + fmt(a4) + ' a ' + fmt(b4)), txt: 'Queremos saber en qué porcentaje cambió.' }, { vis: _G('Cambio: ' + fmt(b4) + ' − ' + fmt(a4) + ' = ' + sig(b4 - a4)), txt: 'Calculamos cuánto cambió.' }, { vis: _G(sig(b4 - a4) + ' ÷ ' + fmt(a4) + ' × 100'), txt: 'Lo comparamos con el valor <b>inicial</b>.' }, { vis: _RS((v >= 0 ? 'Aumentó ' : 'Disminuyó ') + fmt(r2(Math.abs(v))) + ' %'), txt: 'Siempre se divide por el valor de antes, no por el de después.' }]; }
      var a5 = o.a, d5 = o.d, m5 = o.m, a6 = o.a2, m6 = o.m2, x = r2(d5 * (a5 / a6) * (m6 / m5)); return [{ vis: _G(a5 + ' obreros · ' + m5 + ' m · ' + d5 + ' días'), txt: 'Tres magnitudes: buscamos los días.' }, { vis: _F('Más obreros → menos días: inversa'), txt: 'Comparamos cada magnitud con los días, una por vez.' }, { vis: _F('Más metros → más días: directa'), txt: 'La otra relación.' }, { vis: _G('x = ' + d5 + ' × ' + fr(a5, a6) + ' × ' + fr(m6, m5)), txt: 'La inversa va dada vuelta; la directa, igual.' }, { vis: _RS('x = ' + fmt(x) + ' días'), txt: 'Verificamos que tenga sentido.' }];
    });
  } };
  M.porcentajes_x = { tipo: 'ejercicio', render: function (el, p, api) { var md = p.modo || 'factor';
    respuesta(el, api, function () {
      if (md === 'factor') { var t = R(2, 50) * 100, pc = pick([10, 15, 20, 25, 30]), au = Math.random() < .5; return { cons: 'Un precio de <b>$' + fmt(t) + '</b> tiene un ' + (au ? 'aumento' : 'descuento') + ' del <b>' + pc + ' %</b>. ¿Por qué número hay que multiplicarlo para obtener el precio final?', campos: [{ v: (au ? 100 + pc : 100 - pc) / 100 }], ayuda: (au ? '100 % + ' : '100 % − ') + pc + ' %, dividido 100.', bien: '¡Bien!' }; }
      if (md === 'sucesivos') { var t2 = R(1, 9) * 1000, a = pick([10, 20, 25]), q = pick([10, 20]); return { cons: 'Un precio de <b>$' + fmt(t2) + '</b> aumenta un <b>' + a + ' %</b> y después baja un <b>' + q + ' %</b>. ¿Cuál es el precio final?', campos: [{ v: r2(t2 * (100 + a) / 100 * (100 - q) / 100), un: '$' }], ayuda: t2 + ' × ' + fmt((100 + a) / 100) + ' × ' + fmt((100 - q) / 100) + '.', bien: '¡Bien!' }; }
      if (md === 'interes') { var c = R(1, 20) * 1000, r = R(2, 12), t3 = R(1, 4); return { cons: 'Se depositan <b>$' + fmt(c) + '</b> al <b>' + r + ' %</b> anual de interés simple durante <b>' + t3 + '</b> años. ¿Cuánto interés se gana?', campos: [{ v: c * r / 100 * t3, un: '$' }], ayuda: 'I = ' + c + ' × ' + r + ' × ' + t3 + ' ÷ 100.', bien: '¡Bien!' }; }
      if (md === 'variacion') { var a4 = R(2, 20) * 100, v = pick([-25, -20, -10, 10, 20, 25, 50]); return { cons: 'Un valor pasó de <b>' + fmt(a4) + '</b> a <b>' + fmt(a4 * (100 + v) / 100) + '</b>. ¿Cuál fue la variación porcentual? (Si bajó, escribila con signo menos.)', campos: [{ v: v, un: '%' }], ayuda: '(final − inicial) ÷ inicial × 100.', bien: '¡Bien!' }; }
      var a5 = R(2, 6), d5 = R(2, 8) * 2, m5 = R(1, 4) * 10, k = pick([2, 3]), a6 = a5 * k, m6 = m5 * pick([1, 2, 3]); return { cons: '<b>' + a5 + '</b> obreros hacen <b>' + m5 + ' m</b> de pared en <b>' + d5 + '</b> días. ¿Cuántos días tardan <b>' + a6 + '</b> obreros en hacer <b>' + m6 + ' m</b>?', campos: [{ v: r2(d5 * a5 / a6 * m6 / m5) }], ayuda: 'Obreros y días: inversa. Metros y días: directa. x = ' + d5 + ' × ' + a5 + '/' + a6 + ' × ' + m6 + '/' + m5 + '.', bien: '¡Bien!' };
    }); } };
  // ---- ecuaciones II (Matemática II M6, M8, M9)
  M.ecuaciones2 = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'parentesis', C = {
      parentesis: ctrl('k', 'Número de afuera', 2, 5, 1, 3) + ctrl('b', 'Dentro del paréntesis', -6, 6, 1, -2) + ctrl('x', 'Solución', -5, 8, 1, 4),
      denominadores: ctrl('a', 'Denominador 1', 2, 4, 1, 2) + ctrl('b', 'Denominador 2', 3, 6, 1, 3) + ctrl('x', 'Solución (múltiplo de los dos)', 6, 24, 6, 12),
      casos: '<div class="lb-fila"><label>Ecuación</label><select data-k="c"><option value="1">2x + 3 = x + 7</option><option value="2">2x + 3 = 2x + 7</option><option value="3">2(x + 3) = 2x + 6</option></select></div>',
      despejar: '<div class="lb-fila"><label>Fórmula</label><select data-k="f"><option value="r">A = b · h (despejar h)</option><option value="t">A = b · h / 2 (despejar b)</option><option value="v">d = v · t (despejar t)</option><option value="d">ρ = m / V (despejar m)</option></select></div>' }[md];
    escena(el, C, function (o) { var ec = function (a, b) { return (a === 1 ? '' : a) + 'x' + (b ? (b < 0 ? ' − ' + -b : ' + ' + b) : ''); };
      if (md === 'parentesis') { var k = o.k, b = o.b, x = o.x, c = k * (x + b); return [{ vis: _G(k + '(' + ec(1, b) + ') = ' + c), txt: 'Una ecuación con paréntesis.' }, { vis: _G(ec(k, k * b) + ' = ' + c), txt: 'Aplicamos la <b>distributiva</b>: el ' + k + ' multiplica a los dos términos.' }, { vis: _G(k + 'x = ' + (c - k * b)), txt: (k * b < 0 ? 'Sumamos ' + -k * b : 'Restamos ' + k * b) + ' en los dos miembros.' }, { vis: _RS('x = ' + x), txt: 'Dividimos por ' + k + ' y verificamos.' }]; }
      if (md === 'denominadores') { var a = o.a, b2 = Math.max(o.b, a + 1), mc = a * b2 / mcd(a, b2), x2 = mc * Math.max(1, Math.round(o.x / mc)), r = x2 / a + x2 / b2; return [{ vis: _G(fr('x', a) + ' + ' + fr('x', b2) + ' = ' + r), txt: 'Una ecuación con denominadores.' }, { vis: _G('MCM(' + a + ', ' + b2 + ') = ' + mc), txt: 'Buscamos el mínimo común múltiplo de los denominadores.' }, { vis: _G(mc / a + 'x + ' + mc / b2 + 'x = ' + r * mc), txt: 'Multiplicamos <b>todos</b> los términos por ' + mc + ': desaparecen los denominadores.' }, { vis: _RS((mc / a + mc / b2) + 'x = ' + r * mc + ' → x = ' + x2), txt: 'Resolvemos como siempre y verificamos.' }]; }
      if (md === 'casos') { var c2 = o.c || '1'; if (c2 === '1') return [{ vis: _G('2x + 3 = x + 7'), txt: 'Juntamos las x de un lado.' }, { vis: _G('x = 4'), txt: 'Queda un único valor.' }, { vis: _RS('Una solución'), txt: 'Es <b>compatible determinada</b>: tiene una sola solución.' }];
        if (c2 === '2') return [{ vis: _G('2x + 3 = 2x + 7'), txt: 'Restamos 2x en los dos miembros.' }, { vis: _G('3 = 7'), txt: 'Desaparecen las x y queda una igualdad <b>falsa</b>.' }, { vis: _RS('Sin solución'), txt: 'Ningún número la cumple: es <b>incompatible</b>.' }];
        return [{ vis: _G('2(x + 3) = 2x + 6'), txt: 'Aplicamos la distributiva.' }, { vis: _G('2x + 6 = 2x + 6 → 6 = 6'), txt: 'Queda una igualdad siempre <b>verdadera</b>.' }, { vis: _RS('Infinitas soluciones'), txt: 'Cualquier número la cumple: es una <b>identidad</b>.' }]; }
      var F = { r: ['A = b · h', 'h', 'Dividimos los dos miembros por b.', 'h = A ÷ b'], t: ['A = b · h / 2', 'b', 'Multiplicamos por 2 y dividimos por h.', 'b = 2A ÷ h'], v: ['d = v · t', 't', 'Dividimos los dos miembros por v.', 't = d ÷ v'], d: ['ρ = m / V', 'm', 'Multiplicamos los dos miembros por V.', 'm = ρ · V'] }[o.f || 'r'];
      return [{ vis: _G(F[0]), txt: 'Una fórmula: queremos dejar sola a <b>' + F[1] + '</b>.' }, { vis: _F(F[2]), txt: 'Despejar es lo mismo que resolver una ecuación: operaciones inversas en los dos miembros.' }, { vis: _RS(F[3]), txt: 'La fórmula nueva sirve para calcular ' + F[1] + ' con cualquier dato.' }];
    });
  } };
  M.ecuaciones2_x = { tipo: 'ejercicio', render: function (el, p, api) { var md = p.modo || 'parentesis';
    respuesta(el, api, function () {
      if (md === 'parentesis') { var k = R(2, 5), b = R(-6, 6) || 2, x = R(-4, 9); return { cons: 'Resolvé: <b>' + k + '(x ' + (b < 0 ? '− ' + -b : '+ ' + b) + ') = ' + k * (x + b) + '</b>', campos: [{ lab: 'x =', v: x }], ayuda: 'Distributiva: ' + k + 'x ' + (k * b < 0 ? '− ' + -k * b : '+ ' + k * b) + '.', bien: '¡Bien!' }; }
      if (md === 'denominadores') { var a = pick([2, 3, 4]), b = pick([3, 5, 6]); if (b === a) b = 5; var mc = a * b / mcd(a, b), x = mc * R(1, 4), r = x / a + x / b; return { cons: 'Resolvé: <b>x/' + a + ' + x/' + b + ' = ' + r + '</b>', campos: [{ lab: 'x =', v: x }], ayuda: 'Multiplicá todo por ' + mc + '.', bien: '¡Bien!' }; }
      if (md === 'casos') { var S = pick([['3x + 2 = 3x + 5', 'ninguna'], ['4(x − 1) = 4x − 4', 'infinitas'], ['5x − 1 = 2x + 8', 'una'], ['x + x = 2x + 1', 'ninguna'], ['3(x + 2) = 3x + 6', 'infinitas']]); return { cons: '<b>' + S[0] + '</b>: ¿tiene <b>una</b> solución, <b>ninguna</b> o <b>infinitas</b>?', campos: [{ tipo: 'texto', v: [S[1]] }], ayuda: 'Juntá las x: si desaparecen, mirá si queda algo verdadero o falso.', bien: '¡Bien!' }; }
      if (md === 'densidad') { var r = pick([2, 3, 5, 8]), v = R(2, 20); return { cons: 'Un material tiene una densidad de <b>' + r + ' g/cm³</b>. ¿Qué masa tienen <b>' + v + ' cm³</b>?', campos: [{ v: r * v, un: 'g' }], ayuda: 'm = ρ · V.', bien: '¡Bien!' }; }
      var Q = pick([['El área de un rectángulo es <b>A = b · h</b>. Si A = ', 'cm² y b = ', 'cm, ¿cuánto mide h?', function (A, b) { return A / b; }], ['Con <b>d = v · t</b>, si d = ', 'km y v = ', 'km/h, ¿cuántas horas tarda?', function (A, b) { return A / b; }]]), b2 = R(2, 9), res = R(2, 12); return { cons: Q[0] + b2 * res + ' ' + Q[1] + b2 + ' ' + Q[2], campos: [{ v: res }], ayuda: 'Despejá: dividí por ' + b2 + '.', bien: '¡Bien!' };
    }); } };
  // ---- funciones (Matemática II M10-M11)
  M.funciones = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'es_funcion', C = { es_funcion: '<div class="lb-fila"><label>Relación</label><select data-k="c"><option value="1">Cada alumno → su edad</option><option value="2">Cada edad → los alumnos que la tienen</option></select></div>', grafico: ctrl('m', 'Pendiente', -3, 3, 1, 2) + ctrl('b', 'Ordenada al origen', -4, 4, 1, 1) }[md];
    escena(el, C, function (o) {
      if (md === 'es_funcion') { var uno = (o.c || '1') === '1'; return [{ vis: _G(uno ? 'Ana → 12 · Beto → 13 · Caro → 12' : '12 → Ana y Caro · 13 → Beto'), txt: 'Una relación entre dos conjuntos.' }, { vis: _F(uno ? 'Cada alumno tiene UNA edad' : 'El 12 va a DOS alumnos'), txt: 'Miramos si a cada elemento de salida le toca <b>un solo</b> valor.' }, { vis: _RS(uno ? 'Es función' : 'No es función'), txt: 'Una <b>función</b> asigna a cada x un único y. Que dos x den el mismo y está permitido.' }]; }
      var m = o.m, b = o.b, X = function (x) { return 120 + x * 18; }, Y = function (y) { return 75 - y * 9; }, ln = '<line class="diag" x1="' + X(-5) + '" y1="' + Y(m * -5 + b) + '" x2="' + X(5) + '" y2="' + Y(m * 5 + b) + '"/>', ej = '<line class="rayo" x1="20" y1="75" x2="220" y2="75"/><line class="rayo" x1="120" y1="5" x2="120" y2="145"/>', sv = function (x) { return '<svg viewBox="0 0 240 150" class="lb2-svg">' + ej + x + '</svg>'; };
      return [{ vis: sv(ln), txt: 'El gráfico de y = ' + (m === 0 ? '' : (m === 1 ? '' : m === -1 ? '−' : m) + 'x') + (b ? (b < 0 ? ' − ' + -b : (m ? ' + ' : '') + b) : (m ? '' : '0')) + '.' }, { vis: sv(ln + '<circle class="pt" cx="120" cy="' + Y(b) + '" r="5"/>'), txt: 'Donde corta al eje y está la <b>ordenada al origen</b>: ' + b + '.' }, { vis: sv(ln) + _RS(m > 0 ? 'Creciente' : m < 0 ? 'Decreciente' : 'Constante'), txt: m > 0 ? 'De izquierda a derecha sube: es <b>creciente</b>.' : m < 0 ? 'De izquierda a derecha baja: es <b>decreciente</b>.' : 'No sube ni baja: es <b>constante</b>.' }];
    });
  } };
  M.funciones_x = { tipo: 'ejercicio', render: function (el, p, api) { var md = p.modo || 'es_funcion';
    respuesta(el, api, function () {
      if (md === 'es_funcion') { var S = pick([['Cada persona → su DNI', 'si'], ['Cada número → su doble', 'si'], ['Cada mamá → sus hijos (Ana tiene dos)', 'no'], ['Cada día → la temperatura máxima', 'si'], ['Cada número positivo → los números que al cuadrado lo dan (4 → 2 y −2)', 'no']]); return { cons: '«' + S[0] + '»: ¿es una función? Escribí <b>sí</b> o <b>no</b>.', campos: [{ tipo: 'texto', v: S[1] === 'si' ? ['si', 'sí'] : ['no'] }], ayuda: '¿A cada uno le corresponde un solo valor?', bien: '¡Bien!' }; }
      var m = pick([-3, -2, -1, 1, 2, 3]), b = R(-5, 5), ord = Math.random() < .5; return { cons: 'En el gráfico de <b>y = ' + m + 'x ' + (b < 0 ? '− ' + -b : '+ ' + b) + '</b>, ' + (ord ? '¿cuál es la <b>ordenada al origen</b>?' : '¿la función es <b>creciente</b> o <b>decreciente</b>?'), campos: [ord ? { v: b } : { tipo: 'texto', v: [m > 0 ? 'creciente' : 'decreciente'] }], ayuda: ord ? 'Es el valor de y cuando x = 0.' : 'Mirá el signo de lo que multiplica a x.', bien: '¡Bien!' };
    }); } };
  // ---- geometría II (Matemática II M12-M17)
  M.geometria2 = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'paralelas', C = { paralelas: ctrl('g', 'Ángulo', 30, 150, 5, 60, '°'), pitagoras: ctrl('a', 'Cateto a', 3, 12, 1, 6) + ctrl('b', 'Cateto b', 3, 12, 1, 8), congruencia: '<div class="lb-fila"><label>Criterio</label><select data-k="c"><option value="LLL">LLL</option><option value="LAL">LAL</option><option value="ALA">ALA</option></select></div>', cuerpos: '<div class="lb-fila"><label>Cuerpo</label><select data-k="c"><option value="cubo">Cubo</option><option value="prisma3">Prisma triangular</option><option value="piramide4">Pirámide cuadrangular</option></select></div>' }[md];
    escena(el, C, function (o) {
      if (md === 'paralelas') { var g = o.g, a = g * Math.PI / 180, dx = 60 * Math.cos(a), dy = 60 * Math.sin(a), sv = '<svg viewBox="0 0 240 150" class="lb2-svg"><line class="rayo" x1="15" y1="50" x2="225" y2="50"/><line class="rayo" x1="15" y1="110" x2="225" y2="110"/><line class="diag" x1="' + (120 - dx * 1.6).toFixed(1) + '" y1="' + (80 + dy * 1.6).toFixed(1) + '" x2="' + (120 + dx * 1.6).toFixed(1) + '" y2="' + (80 - dy * 1.6).toFixed(1) + '"/></svg>';
        return [{ vis: sv, txt: 'Dos rectas paralelas cortadas por una <b>transversal</b> forman 8 ángulos.' }, { vis: sv + _G('Correspondientes: ' + g + '° y ' + g + '°'), txt: 'Los <b>correspondientes</b> (misma posición en cada cruce) son iguales.' }, { vis: sv + _G('Alternos internos: ' + g + '° y ' + g + '°'), txt: 'Los <b>alternos internos</b> (entre las paralelas, de lados opuestos) también son iguales.' }, { vis: sv + _RS('Conjugados internos: ' + g + '° + ' + (180 - g) + '° = 180°'), txt: 'Los <b>conjugados</b> (entre las paralelas, del mismo lado) suman 180°.' }]; }
      if (md === 'pitagoras') { var a2 = o.a, b2 = o.b, c2 = Math.sqrt(a2 * a2 + b2 * b2); return [{ vis: _G('Catetos: ' + a2 + ' y ' + b2), txt: 'Un triángulo <b>rectángulo</b>: los lados del ángulo recto son los catetos.' }, { vis: _G(a2 + '² + ' + b2 + '² = ' + a2 * a2 + ' + ' + b2 * b2 + ' = ' + (a2 * a2 + b2 * b2)), txt: 'Teorema de Pitágoras: la suma de los cuadrados de los catetos…' }, { vis: _G('h² = ' + (a2 * a2 + b2 * b2)), txt: '…es igual al cuadrado de la hipotenusa.' }, { vis: _RS('h = √' + (a2 * a2 + b2 * b2) + ' ≈ ' + fmt(r2(c2))), txt: 'Sacamos la raíz. Solo vale en triángulos rectángulos.' }]; }
      if (md === 'congruencia') { var c3 = o.c || 'LLL', D = { LLL: ['Los tres lados', 'Si los tres lados son iguales, los triángulos son congruentes.'], LAL: ['Dos lados y el ángulo entre ellos', 'El ángulo tiene que ser el comprendido entre esos dos lados.'], ALA: ['Un lado y los dos ángulos de sus extremos', 'Los ángulos tienen que estar apoyados sobre ese lado.'] }[c3]; return [{ vis: svgTri() + svgTri(), txt: 'Dos triángulos son <b>congruentes</b> si son iguales: se pueden superponer.' }, { vis: _G(c3 + ': ' + D[0]), txt: 'No hace falta comparar todo: alcanza con un criterio.' }, { vis: _RS('Criterio ' + c3), txt: D[1] + ' Con tres ángulos iguales no alcanza: pueden ser de distinto tamaño.' }]; }
      var Q = { cubo: [6, 12, 8, 'Cubo'], prisma3: [5, 9, 6, 'Prisma triangular'], piramide4: [5, 8, 5, 'Pirámide cuadrangular'] }[o.c || 'cubo']; return [{ vis: _G(Q[3]), txt: 'Un cuerpo geométrico.' }, { vis: _G('Caras: ' + Q[0] + ' · Aristas: ' + Q[1] + ' · Vértices: ' + Q[2]), txt: 'Las <b>caras</b> son las superficies, las <b>aristas</b> los bordes y los <b>vértices</b> las puntas.' }, { vis: _RS(Q[0] + ' + ' + Q[2] + ' − ' + Q[1] + ' = 2'), txt: 'En todo poliedro convexo: caras + vértices − aristas = 2 (fórmula de Euler).' }];
    });
  } };
  M.geometria2_x = { tipo: 'ejercicio', render: function (el, p, api) { var md = p.modo || 'paralelas';
    respuesta(el, api, function () {
      if (md === 'paralelas') { var g = R(6, 30) * 5, t = pick([['correspondiente', g], ['alterno interno', g], ['conjugado interno', 180 - g]]); return { cons: 'Dos paralelas cortadas por una transversal forman un ángulo de <b>' + g + '°</b>. ¿Cuánto mide su ángulo <b>' + t[0] + '</b>?', campos: [{ v: t[1], un: '°' }], ayuda: 'Correspondientes y alternos: iguales. Conjugados: suman 180°.', bien: '¡Bien!' }; }
      if (md === 'pitagoras') { var T = pick([[3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 12, 15], [8, 15, 17]]), hip = Math.random() < .6; return hip ? { cons: 'Un triángulo rectángulo tiene catetos de <b>' + T[0] + '</b> y <b>' + T[1] + ' cm</b>. ¿Cuánto mide la hipotenusa?', campos: [{ v: T[2], un: 'cm' }], ayuda: '√(' + T[0] + '² + ' + T[1] + '²).', bien: '¡Bien!' } : { cons: 'Un triángulo rectángulo tiene hipotenusa de <b>' + T[2] + ' cm</b> y un cateto de <b>' + T[0] + ' cm</b>. ¿Cuánto mide el otro cateto?', campos: [{ v: T[1], un: 'cm' }], ayuda: '√(' + T[2] + '² − ' + T[0] + '²).', bien: '¡Bien!' }; }
      if (md === 'congruencia') { var S = pick([['Los tres lados son iguales', 'LLL'], ['Dos lados y el ángulo comprendido son iguales', 'LAL'], ['Un lado y los dos ángulos apoyados en él son iguales', 'ALA']]); return { cons: '«' + S[0] + '». ¿Qué criterio de congruencia es? Escribí LLL, LAL o ALA.', campos: [{ tipo: 'texto', v: [S[1].toLowerCase(), S[1]] }], ayuda: 'L = lado, A = ángulo, en el orden en que aparecen.', bien: '¡Bien!' }; }
      var Q = pick([['un cubo', 6, 12, 8], ['un prisma triangular', 5, 9, 6], ['una pirámide cuadrangular', 5, 8, 5], ['un prisma pentagonal', 7, 15, 10]]); return { cons: '¿Cuántas <b>aristas</b> tiene ' + Q[0] + ', si tiene ' + Q[1] + ' caras y ' + Q[3] + ' vértices?', campos: [{ v: Q[2] }], ayuda: 'Euler: caras + vértices − aristas = 2.', bien: '¡Bien!' };
    }); } };

  // ======= LENGUA (datos escritos en sesión; el motor solo los muestra paso a paso) =======
  // Marcas en el texto: {{frase|explicación del paso}}. Cada marca es un paso, en orden.
  var MK = 'background:#d8f0ea;border-bottom:3px solid #0e7c7b;border-radius:4px;padding:0 2px';
  function marcas(t) { var L = [], re = /\{\{([^|}]+)\|([^}]+)\}\}/g, m; while ((m = re.exec(t))) L.push({ f: m[1], e: m[2] }); return L; }
  function pintar(t, hasta, actual) { var k = 0; return t.replace(/\{\{([^|}]+)\|([^}]+)\}\}/g, function (_, f) { k++; return k <= hasta ? '<mark style="' + MK + (k === actual ? ';outline:2px solid #0e7c7b' : '') + '">' + f + '</mark>' : f; }); }
  function selItems(items, rot) { return items.length > 1 ? '<div class="lb-fila"><label>' + (rot || 'Ejemplo') + '</label><select data-k="i">' + items.map(function (it, i) { return '<option value="' + i + '">' + (it.nombre || (i + 1)) + '</option>'; }).join('') + '</select></div>' : ''; }
  function caja(x) { return '<div class="lb2-texto" style="font-size:1.08em;line-height:1.7;text-align:left;padding:10px 12px;background:#fff;border-radius:10px">' + x + '</div>'; }
  function otroEj(el) { var b = el.querySelector('[data-lb="otro"]'); if (b) b.textContent = '🔄 Otro ejemplo'; }
  M.marcar = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [{ texto: p.texto || '', cierre: p.cierre }];
    escena(el, selItems(items, p.rotulo), function (o) { var it = items[+(o.i || 0)] || items[0], L = marcas(it.texto), P = [{ vis: caja(pintar(it.texto, 0)), txt: it.inicio || p.inicio || 'Leemos el texto.' }];
      L.forEach(function (x, k) { P.push({ vis: caja(pintar(it.texto, k + 1, k + 1)), txt: x.e }); });
      if (it.cierre) P.push({ vis: caja(pintar(it.texto, L.length)) + '<p class="lb-cn-res">' + it.cierre + '</p>', txt: it.cierre_txt || 'En resumen.' });
      return P; });
  } };
  M.transformar = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items, p.rotulo), function (o) { var it = items[+(o.i || 0)] || items[0], P = [{ vis: caja(it.antes), txt: it.inicio || 'La primera versión.' }];
      (it.pasos || []).forEach(function (x) { P.push({ vis: caja(x.v.replace(/\{\{([^}]+)\}\}/g, '<mark style="' + MK + '">$1</mark>')), txt: x.txt }); });
      if (it.cierre) P.push({ vis: caja((it.pasos && it.pasos.length ? it.pasos[it.pasos.length - 1].v : it.antes).replace(/\{\{([^}]+)\}\}/g, '$1')) + '<p class="lb-cn-res">' + it.cierre + '</p>', txt: 'Comparada con la primera, se entiende mejor.' });
      return P; });
  } };
  M.palabra = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.s.join('') }; }), 'Palabra'), function (o) { var it = items[+(o.i || 0)] || items[0], s = it.s, t = it.t, n = s.length, pos = n - t, cl = pos === 1 ? 'aguda' : pos === 2 ? 'grave' : 'esdrújula', w = s.join(''), fin = w.slice(-1).normalize('NFD').replace(/[̀-ͯ]/g, ''), lleva = /[áéíóú]/.test(w), sil = function (hl) { return '<p class="lb-pt-g">' + s.map(function (x, i) { return i === hl ? '<b style="color:#0e7c7b;text-decoration:underline">' + x + '</b>' : x; }).join(' - ') + '</p>'; };
      var regla = cl === 'aguda' ? 'Las agudas llevan tilde si terminan en n, s o vocal.' : cl === 'grave' ? 'Las graves llevan tilde si NO terminan en n, s o vocal.' : 'Las esdrújulas llevan tilde siempre.';
      return [{ vis: sil(-1), txt: 'Separamos en sílabas: <b>' + n + '</b>.' }, { vis: sil(t), txt: 'La sílaba que suena más fuerte es la <b>tónica</b>: «' + s[t] + '».' }, { vis: sil(t) + '<p class="lb-pt-f">' + (pos === 1 ? 'Última' : pos === 2 ? 'Penúltima' : 'Antepenúltima') + ' sílaba → ' + cl + '</p>', txt: 'Contamos desde el final.' }, { vis: sil(t) + '<p class="lb-cn-res">' + w + ': ' + cl + ', ' + (lleva ? 'con tilde' : 'sin tilde') + '</p>', txt: regla + (cl !== 'esdrújula' ? ' Termina en «' + fin + '».' : '') }]; });
  } };
  M.marcar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], ult = -1;
    H.ejercicio(el, api, p.consigna || 'Tocá lo que corresponde.', function (c) {
      var k = items.length > 1 ? (function () { var x; do { x = R(0, items.length - 1); } while (x === ult); return x; })() : 0; ult = k; var it = items[k], n = 0;
      var html = it.texto.replace(/\[\[([^|\]]+)\|([01])\]\]/g, function (_, f, ok) { n++; return '<button type="button" class="lb-chip" data-ok="' + ok + '" style="margin:2px">' + f + '</button>'; });
      c.innerHTML = (it.cons ? '<p class="lb-ayuda">' + it.cons + '</p>' : '') + caja(html);
      c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (b) b.classList.toggle('sel'); };
      return { comprobar: function () { var B = [].slice.call(c.querySelectorAll('.lb-chip')), sel = B.filter(function (b) { return b.classList.contains('sel'); });
          if (!sel.length) return { ok: false, msg: 'Tocá una ficha y después comprobá.' };
          B.forEach(function (b) { b.classList.remove('bien', 'mal'); if (b.classList.contains('sel')) b.classList.add(b.getAttribute('data-ok') === '1' ? 'bien' : 'mal'); });
          var ok = B.every(function (b) { return b.classList.contains('sel') === (b.getAttribute('data-ok') === '1'); });
          return ok ? { ok: true, msg: it.bien || '¡Bien!' } : { ok: false, msg: it.ayuda || 'Revisalo: hay fichas de más o de menos.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-chip'), function (b) { b.classList.toggle('sel', b.getAttribute('data-ok') === '1'); }); } };
    }); otroEj(el);
  } };
  M.clasificar_x = { tipo: 'ejercicio', render: function (el, p, api) {
    cajas(el, api, function () { var it = mezclar(p.items || []).slice(0, p.cuantos || 5); return { tit: p.consigna || 'Ubicá cada ficha en su caja.', cajas: p.cajas, items: it.map(function (x, i) { return { v: 'i' + i, t: x[0], c: x[1] }; }) }; }); otroEj(el);
  } };
  M.elegir_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], ult = -1;
    H.ejercicio(el, api, p.consigna || 'Elegí la opción correcta.', function (c) {
      var k = items.length > 1 ? (function () { var x; do { x = R(0, items.length - 1); } while (x === ult); return x; })() : 0; ult = k; var it = items[k], ops = mezclar(it.ops.map(function (o, i) { return { t: o, ok: i === 0 }; }));
      c.innerHTML = '<p class="lb-pt-g" style="font-weight:normal">' + it.cons + '</p><div class="lb-banco">' + ops.map(function (o) { return '<button type="button" class="lb-chip" data-ok="' + (o.ok ? 1 : 0) + '">' + o.t + '</button>'; }).join('') + '</div>';
      c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (!b) return; [].forEach.call(c.querySelectorAll('.lb-chip'), function (x) { x.classList.toggle('sel', x === b); }); };
      return { comprobar: function () { var s = c.querySelector('.lb-chip.sel'); if (!s) return { ok: false, msg: 'Tocá una ficha y después comprobá.' }; var ok = s.getAttribute('data-ok') === '1'; s.classList.add(ok ? 'bien' : 'mal'); return ok ? { ok: true, msg: it.bien || '¡Bien!' } : { ok: false, msg: it.ayuda || 'Revisalo.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-chip'), function (x) { x.classList.toggle('sel', x.getAttribute('data-ok') === '1'); }); } };
    }); otroEj(el);
  } };

  // ---- LENGUA: ejemplos (paso a paso) ----
  var CL = ['#0e7c7b', '#e07a2f', '#5b5fc7', '#c2416b', '#3c8d2f', '#8a6d1d', '#2a7ab8', '#7a3fa0'];
  function bloq(t, lab, col, sub) { return '<span style="display:inline-flex;flex-direction:column;align-items:center;margin:4px 3px;vertical-align:top"><span style="padding:4px 7px;border:2px solid ' + (col || '#bbb') + ';border-radius:8px;background:#fff">' + t + '</span>' + (lab ? '<small style="color:' + (col || '#666') + ';font-weight:700;margin-top:2px">' + lab + '</small>' : '') + (sub || '') + '</span>'; }
  M.versiones = { tipo: 'ejemplo', pasos: true, render: function (el, p) { M.marcar.render(el, { items: p.items, rotulo: p.rotulo || 'Versión', inicio: p.inicio }); } };
  M.oracion = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.nombre || x.partes.map(function (q) { return q[0]; }).join(' ').slice(0, 30) + '…' }; }), 'Oración'), function (o) { var it = items[+(o.i || 0)] || items[0], P = it.partes, plano = P.map(function (q) { return q[0]; }).join(' '), pasos = [{ vis: caja(plano), txt: it.inicio || 'Leemos la oración completa.' }];
      var hecho = [];
      P.forEach(function (q, k) { hecho.push(k); pasos.push({ vis: caja(P.map(function (r, j) { return hecho.indexOf(j) >= 0 ? bloq(r[0], r[1], CL[j % CL.length]) : r[0]; }).join(' ')), txt: q[2] || ('<b>' + q[1] + '</b>: «' + q[0] + '».') }); });
      var sub = [];
      P.forEach(function (q, k) { (q[3] || []).forEach(function (sq) { sub.push([k, sq]); }); });
      var hechos2 = [];
      sub.forEach(function (z, n) { hechos2.push(n); pasos.push({ vis: caja(P.map(function (r, j) { var hijos = sub.map(function (w, m) { return w[0] === j && hechos2.indexOf(m) >= 0 ? bloq(w[1][0], w[1][1], CL[(j + 3) % CL.length]) : null; }).filter(Boolean); return bloq(hijos.length ? hijos.join(' ') : r[0], r[1], CL[j % CL.length]); }).join(' ')), txt: z[1][2] || ('<b>' + z[1][1] + '</b>: «' + z[1][0] + '».') }); });
      if (it.cierre) pasos.push({ vis: pasos[pasos.length - 1].vis + '<p class="lb-cn-res">' + it.cierre + '</p>', txt: 'Así queda el análisis completo.' });
      return pasos; });
  } };
  var VB = { ar: { presente: ['o', 'ás', 'a', 'amos', 'an', 'an'], 'pretérito perfecto simple': ['é', 'aste', 'ó', 'amos', 'aron', 'aron'], 'pretérito imperfecto': ['aba', 'abas', 'aba', 'ábamos', 'aban', 'aban'], futuro: ['aré', 'arás', 'ará', 'aremos', 'arán', 'arán'] }, er: { presente: ['o', 'és', 'e', 'emos', 'en', 'en'], 'pretérito perfecto simple': ['í', 'iste', 'ió', 'imos', 'ieron', 'ieron'], 'pretérito imperfecto': ['ía', 'ías', 'ía', 'íamos', 'ían', 'ían'], futuro: ['eré', 'erás', 'erá', 'eremos', 'erán', 'erán'] }, ir: { presente: ['o', 'ís', 'e', 'imos', 'en', 'en'], 'pretérito perfecto simple': ['í', 'iste', 'ió', 'imos', 'ieron', 'ieron'], 'pretérito imperfecto': ['ía', 'ías', 'ía', 'íamos', 'ían', 'ían'], futuro: ['iré', 'irás', 'irá', 'iremos', 'irán', 'irán'] } };
  var PERS = ['yo', 'vos', 'él / ella', 'nosotros', 'ustedes', 'ellos / ellas'], VREG = ['cantar', 'caminar', 'mirar', 'saltar', 'comer', 'correr', 'aprender', 'temer', 'vivir', 'escribir', 'partir', 'subir'];
  function conj(v, t, k) { var r = v.slice(0, -2), e = v.slice(-2); return [r, VB[e][t][k]]; }
  M.conjugador = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var vs = p.verbos || VREG, ts = p.tiempos || ['presente', 'pretérito perfecto simple', 'pretérito imperfecto', 'futuro'];
    var C = '<div class="lb-fila"><label>Verbo</label><select data-k="v">' + vs.map(function (v) { return '<option>' + v + '</option>'; }).join('') + '</select></div><div class="lb-fila"><label>Tiempo</label><select data-k="t">' + ts.map(function (v) { return '<option>' + v + '</option>'; }).join('') + '</select></div>' + ctrl('k', 'Persona (1 a 6)', 1, 6, 1, 1);
    escena(el, C, function (o) { var v = o.v || vs[0], t = o.t || ts[0], k = (o.k || 1) - 1, c = conj(v, t, k), e = v.slice(-2), lin = '';
      if (/pretérito/.test(t)) lin = '<svg viewBox="0 0 240 60" class="lb2-svg"><line class="rayo" x1="10" y1="30" x2="230" y2="30"/><text x="205" y="52">hoy</text><circle class="pt" cx="215" cy="30" r="4"/>' + (/perfecto/.test(t) ? '<circle class="pt" cx="90" cy="30" r="7"/><text x="55" y="52">una acción terminada</text>' : '<line class="diag" x1="40" y1="30" x2="150" y2="30" style="stroke-width:7"/><text x="45" y="52">algo que duraba</text>') + '</svg>';
      return [{ vis: _G(v), txt: 'El <b>infinitivo</b>: termina en -' + e + ' (' + (e === 'ar' ? '1.ª' : e === 'er' ? '2.ª' : '3.ª') + ' conjugación).' }, { vis: _G('<b style="color:#0e7c7b">' + c[0] + '</b> + -' + e), txt: 'Separamos la <b>raíz</b> (' + c[0] + '-), que no cambia.' }, { vis: _G(PERS[k] + ' · ' + t), txt: 'Elegimos persona y tiempo: la <b>desinencia</b> los indica.' }, { vis: _G('<b style="color:#0e7c7b">' + c[0] + '</b><b style="color:#e07a2f">' + c[1] + '</b>') + lin, txt: PERS[k] + ' ' + c[0] + c[1] + '. ' + (/perfecto/.test(t) ? 'El perfecto simple cuenta acciones <b>terminadas</b>, que hacen avanzar la historia.' : /imperfecto/.test(t) ? 'El imperfecto describe lo que <b>duraba</b> o se repetía: el fondo de la historia.' : 'Cambiá la persona y mirá qué parte se mueve.') }]; });
  } };
  M.clases = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [], orden = p.clases || [];
    escena(el, selItems(items), function (o) { var it = items[+(o.i || 0)] || items[0], cls = orden.length ? orden : [], re = /\{\{([^|}]+)\|([^}]+)\}\}/g, m;
      if (!cls.length) while ((m = re.exec(it.texto))) if (cls.indexOf(m[2]) < 0) cls.push(m[2]);
      var vis = function (h) { return caja(it.texto.replace(/\{\{([^|}]+)\|([^}]+)\}\}/g, function (_, w, c) { var j = cls.indexOf(c); return j < h ? '<span style="color:' + CL[j % CL.length] + ';font-weight:700;border-bottom:3px solid ' + CL[j % CL.length] + '">' + w + '</span>' : w; })) + '<p class="lb-ayuda">' + cls.slice(0, h).map(function (c, j) { return '<b style="color:' + CL[j % CL.length] + '">■ ' + c + '</b>'; }).join(' · ') + '</p>'; };
      var P = [{ vis: vis(0), txt: 'Leemos la oración.' }]; cls.forEach(function (c, j) { P.push({ vis: vis(j + 1), txt: (it.expl && it.expl[c]) || ('Marcamos los <b>' + c + '</b>.') }); }); return P; });
  } };
  M.formacion = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.palabra }; }), 'Palabra'), function (o) { var it = items[+(o.i || 0)] || items[0], P = [], acc = [];
      it.partes.forEach(function (q, k) { acc.push(q); P.push({ vis: '<p class="lb-pt-g">' + acc.map(function (r, j) { return bloq(r[0], r[1], CL[j % CL.length]); }).join('<b style="margin:0 2px">+</b>') + '</p>', txt: '<b>' + q[1] + '</b> «' + q[0] + '»' + (q[2] ? ': ' + q[2] + '.' : '.') }); });
      P.push({ vis: P[P.length - 1].vis + '<p class="lb-cn-res">' + it.palabra + (it.significado ? ': ' + it.significado : '') + '</p>', txt: it.cierre || 'Las partes juntas forman la palabra nueva.' }); return P; });
  } };
  M.vocales = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.s.join('') }; }), 'Palabra'), function (o) { var it = items[+(o.i || 0)] || items[0], w = it.s.join(''), pint = function (x) { return x.replace(/[aeoáéíóú]/gi, function (v) { return '<b style="color:#e07a2f">' + v + '</b>'; }).replace(/(^|[^>])([iuü])/g, '$1<b style="color:#2a7ab8">$2</b>'); };
      return [{ vis: _G(pint(w)) + '<p class="lb-ayuda"><b style="color:#e07a2f">■ abiertas</b> (a, e, o, í, ú) · <b style="color:#2a7ab8">■ cerradas</b> (i, u)</p>', txt: 'Miramos las vocales que están juntas: «' + it.g + '».' }, { vis: _G(it.s.join(' - ')), txt: it.tipo === 'diptongo' ? 'Quedan en la <b>misma sílaba</b>: es un <b>diptongo</b>.' : 'Quedan en <b>sílabas distintas</b>: es un <b>hiato</b>.' }, { vis: '<p class="lb-cn-res">' + w + ': ' + it.tipo + '</p>', txt: it.regla || (it.tipo === 'diptongo' ? 'Abierta + cerrada sin tilde, o dos cerradas: diptongo.' : 'Dos abiertas, o una cerrada con tilde (í, ú) junto a una abierta: hiato.') }]; });
  } };
  M.capas = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items), function (o) { var it = items[+(o.i || 0)] || items[0], cats = [], re = /\{\{([^|}]+)\|([^|}]+)(?:\|([^}]+))?\}\}/g, m, ex = {};
      while ((m = re.exec(it.texto))) { if (cats.indexOf(m[2]) < 0) cats.push(m[2]); if (m[3]) ex[m[2]] = m[3]; }
      var borrar = it.borrado, vis = function (h, tach) { return caja(it.texto.replace(/\{\{([^|}]+)\|([^|}]+)(?:\|[^}]+)?\}\}/g, function (_, f, c) { var j = cats.indexOf(c); if (tach && c !== borrar) return '<s style="opacity:.45">' + f + '</s>'; return j < h ? '<mark style="background:' + CL[j % CL.length] + '22;border-bottom:3px solid ' + CL[j % CL.length] + '">' + f + '</mark>' : f; })) + '<p class="lb-ayuda">' + cats.slice(0, h).map(function (c, j) { return '<b style="color:' + CL[j % CL.length] + '">■ ' + c + '</b>'; }).join(' · ') + '</p>'; };
      var P = [{ vis: vis(0), txt: it.inicio || 'Leemos el texto completo.' }]; cats.forEach(function (c, j) { P.push({ vis: vis(j + 1), txt: ex[c] || ('Marcamos: <b>' + c + '</b>.') }); });
      if (borrar) P.push({ vis: vis(cats.length, 1), txt: 'La <b>prueba del borrado</b>: tachamos lo demás y lo que queda se sigue entendiendo.' });
      if (it.cierre) P.push({ vis: vis(cats.length, !!borrar) + '<p class="lb-cn-res">' + it.cierre + '</p>', txt: 'En resumen.' }); return P; });
  } };
  M.esquema = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.nombre || x.raiz || 'Cuadro' }; })), function (o) { var it = items[+(o.i || 0)] || items[0], P = [];
      if (it.cols) { var F = it.filas, tab = function (h) { var n = 0; return '<table class="lb2-tab"><tr>' + it.cols.map(function (c) { return '<th>' + c + '</th>'; }).join('') + '</tr>' + F.map(function (f) { return '<tr>' + f.map(function (c, j) { n++; return j === 0 || n <= h ? '<td>' + (j === 0 ? '<b>' + c + '</b>' : c) + '</td>' : '<td style="color:#bbb">…</td>'; }).join('') + '</tr>'; }).join('') + '</table>'; }, tot = F.length * it.cols.length, celdas = [];
        P.push({ vis: tab(0), txt: it.inicio || 'Armamos el cuadro: arriba los criterios, a la izquierda lo que comparamos.' });
        F.forEach(function (f, i) { P.push({ vis: tab((i + 1) * it.cols.length), txt: 'Completamos la fila de <b>' + f[0] + '</b>.' }); });
        if (it.cierre) P.push({ vis: tab(tot) + '<p class="lb-cn-res">' + it.cierre + '</p>', txt: 'Con el cuadro se ven parecidos y diferencias de un vistazo.' }); return P; }
      var R0 = it.raiz, ram = it.ramas, dib = function (h) { var k = 0; return '<div style="display:flex;align-items:center;gap:8px;text-align:left"><div style="padding:8px;border:2px solid #0e7c7b;border-radius:10px;font-weight:700">' + R0 + '</div><div style="font-size:2.4em;line-height:1;color:#0e7c7b">{</div><div>' + ram.map(function (r, j) { k++; var vis1 = k <= h; return vis1 ? '<div style="margin:4px 0"><b style="color:' + CL[j % CL.length] + '">' + r[0] + '</b>' + (r[1] && r[1].length ? ': ' + r[1].join(', ') : '') + '</div>' : '<div style="margin:4px 0;color:#bbb">…</div>'; }).join('') + '</div></div>'; };
      P.push({ vis: dib(0), txt: 'En el centro va el <b>tema</b>: «' + R0 + '».' }); ram.forEach(function (r, j) { P.push({ vis: dib(j + 1), txt: r[2] || ('Agregamos <b>' + r[0] + '</b>.') }); });
      if (it.cierre) P.push({ vis: dib(ram.length) + '<p class="lb-cn-res">' + it.cierre + '</p>', txt: 'El esquema muestra la jerarquía de las ideas.' }); return P; });
  } };
  M.linea_tiempo = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items), function (o) { var it = items[+(o.i || 0)] || items[0], H2 = it.hechos, tarj = function (lst, marca) { return '<div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center">' + lst.map(function (h, k) { return '<div style="padding:6px 8px;border:2px solid ' + (marca && h.flash ? '#e07a2f' : '#0e7c7b') + ';border-radius:8px;background:#fff;max-width:140px;font-size:.92em"><b>' + (k + 1) + '.</b> ' + h.t + '</div>'; }).join('<span style="align-self:center">→</span>') + '</div>'; };
      var rel = H2.slice(), cro = H2.slice().sort(function (a, b) { return a.c - b.c; });
      return [{ vis: tarj(rel), txt: 'Así aparecen los hechos en el relato: el <b>orden del relato</b>.' }, { vis: tarj(rel, 1), txt: it.marca || 'Marcamos el hecho que pasó antes pero se cuenta después.' }, { vis: tarj(cro), txt: 'Los acomodamos según cuándo ocurrieron: el <b>orden cronológico</b>.' }, { vis: tarj(cro) + '<p class="lb-cn-res">' + (it.cierre || 'El autor elige el orden para crear suspenso.') + '</p>', txt: it.cierre_txt || 'Comparar los dos órdenes muestra cómo está armada la historia.' }]; });
  } };
  M.recursos = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.recurso + ': ' + x.frase.slice(0, 22) + '…' }; })), function (o) { var it = items[+(o.i || 0)] || items[0];
      return [{ vis: caja('«' + it.frase + '»'), txt: 'Leemos la frase: no dice las cosas de forma literal.' }, { vis: caja('«' + it.frase + '»') + _F('¿De qué se habla? <b>' + it.a + '</b>'), txt: 'Buscamos de qué se habla realmente.' }, { vis: caja('«' + it.frase + '»') + _F('¿Con qué se lo relaciona? <b>' + it.b + '</b>'), txt: 'Y con qué se lo relaciona.' }, { vis: _F('Lo que tienen en común: <b>' + it.rasgo + '</b>'), txt: 'El rasgo compartido es lo que se quiere destacar.' }, { vis: '<p class="lb-cn-res">' + it.recurso + '</p>' + _F('Dicho literal: «' + it.literal + '»'), txt: it.porque || 'Así se llama el recurso.' }]; });
  } };
  M.verso = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items), function (o) { var it = items[+(o.i || 0)] || items[0], V = it.versos, Rm = it.rima || [], cortes = it.estrofas || [V.length], fin = function (v) { return v.replace(/[.,;:!?¡¿»«"]+$/, ''); }, txtV = function (op) { var k = 0, html = ''; cortes.forEach(function (n, e) { for (var j = 0; j < n; j++, k++) { var v = V[k], l = Rm[k], col = l && l !== '-' ? CL[(l.charCodeAt(0) - 65) % CL.length] : '#999', w = fin(v).split(' '), ult = w.pop(); html += '<div>' + (op.num ? '<small style="color:#999">' + (k + 1) + '</small> ' : '') + w.join(' ') + ' ' + (op.rima ? '<b style="color:' + col + '">' + ult + '</b> <small style="color:' + col + '">' + (l || '') + '</small>' : ult) + v.slice(fin(v).length) + '</div>'; } if (e < cortes.length - 1) html += '<div style="height:10px"></div>'; }); return caja(html); };
      return [{ vis: txtV({}), txt: 'Un poema: cada renglón es un <b>verso</b>.' }, { vis: txtV({ num: 1 }), txt: 'Contamos los versos: ' + V.length + '. Los grupos separados por un espacio son <b>estrofas</b>: ' + cortes.length + '.' }, { vis: txtV({ num: 1, rima: 1 }), txt: 'Miramos el final de cada verso: los que suenan igual llevan la misma letra.' }, { vis: txtV({ num: 1, rima: 1 }) + '<p class="lb-cn-res">' + (it.tipo || 'Verso libre') + '</p>', txt: it.expl || 'Si coinciden vocales y consonantes, la rima es consonante; si solo las vocales, asonante.' }]; });
  } };
  M.personaje = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.nombre }; }), 'Personaje'), function (o) { var it = items[+(o.i || 0)] || items[0], ficha = function (t, d, col) { return '<div style="flex:1;min-width:120px;padding:8px;border:2px solid ' + col + ';border-radius:10px;text-align:left"><b style="color:' + col + '">' + t + '</b><div style="font-size:.92em">Físicos: ' + d.f.join(', ') + '<br>Psicológicos: ' + d.p.join(', ') + '</div></div>'; };
      var P = [{ vis: _G(it.nombre), txt: it.inicio || 'Un personaje del relato.' }, { vis: ficha('Al principio', it.antes, '#0e7c7b'), txt: 'Rasgos <b>físicos</b> (cómo es por fuera) y <b>psicológicos</b> (cómo es y cómo actúa).' }];
      if (it.despues) P.push({ vis: '<div style="display:flex;gap:8px;flex-wrap:wrap">' + ficha('Al principio', it.antes, '#0e7c7b') + ficha('Al final', it.despues, '#e07a2f') + '</div>', txt: 'Comparamos con el final del relato.' });
      P.push({ vis: P[P.length - 1].vis + '<p class="lb-cn-res">' + (it.cierre || (it.despues ? 'Es un personaje dinámico: cambia.' : 'Es un personaje estático.')) + '</p>', txt: it.porque || 'Lo que lo hace cambiar es clave para entender la historia.' }); return P; });
  } };
  M.conectores = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.relacion }; }), 'Relación'), function (o) { var it = items[+(o.i || 0)] || items[0], unir = function (c, col) { return caja(it.a + ' <b style="color:' + col + '">' + c + '</b> ' + it.b); };
      return [{ vis: caja(it.a + ' <span style="color:#bbb">▢</span> ' + it.b), txt: 'Dos ideas que hay que unir.' }, { vis: caja(it.a + ' <span style="color:#bbb">▢</span> ' + it.b) + _F('Relación: <b>' + it.relacion + '</b>'), txt: '¿Qué relación hay entre ellas?' }, { vis: unir(it.ok[0], '#0e7c7b'), txt: 'Con un conector de ' + it.relacion + ' («' + it.ok.join('», «') + '») el sentido funciona.' }, { vis: unir(it.mal[0], '#c2416b') + _F('✘ ' + (it.porque_mal || 'Cambia el sentido.')), txt: 'Con «' + it.mal[0] + '» la relación cambia y el texto no tiene sentido.' }]; });
  } };
  M.formato = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.tipo }; }), 'Texto'), function (o) { var it = items[+(o.i || 0)] || items[0], pl = function (h) { return '<div style="text-align:left;border:2px dashed #0e7c7b;border-radius:10px;padding:8px;background:#fff">' + it.partes.map(function (q, j) { return j < h ? '<div style="margin:5px 0"><small style="color:' + CL[j % CL.length] + ';font-weight:700">' + q[0] + '</small><div style="' + (q[2] || '') + '">' + q[1] + '</div></div>' : '<div style="margin:5px 0;color:#bbb">' + q[0] + ': …</div>'; }).join('') + '</div>'; };
      var P = [{ vis: pl(0), txt: 'La estructura de ' + it.tipo + ': cada parte tiene su lugar.' }]; it.partes.forEach(function (q, j) { P.push({ vis: pl(j + 1), txt: q[3] || ('Completamos: <b>' + q[0] + '</b>.') }); }); return P; });
  } };
  M.revision = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items), function (o) { var it = items[+(o.i || 0)] || items[0], lst = function (h) { return caja(it.borrador) + '<div style="text-align:left">' + it.criterios.map(function (c, j) { return j < h ? '<div>' + (c[1] ? '✅' : '❌') + ' ' + c[0] + (c[2] ? ' <small style="color:#666">— ' + c[2] + '</small>' : '') + '</div>' : '<div style="color:#bbb">☐ ' + c[0] + '</div>'; }).join('') + '</div>'; };
      var P = [{ vis: lst(0), txt: 'Un borrador y la lista de revisión.' }]; it.criterios.forEach(function (c, j) { P.push({ vis: lst(j + 1), txt: c[1] ? 'Esto está bien.' : 'Hay que corregirlo.' }); });
      if (it.final) P.push({ vis: caja(it.final) + '<p class="lb-cn-res">Versión corregida</p>', txt: 'Se reescribe arreglando cada punto marcado.' }); return P; });
  } };
  M.citar = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var items = p.items || [];
    escena(el, selItems(items.map(function (x) { return { nombre: x.f.autor }; }), 'Fuente'), function (o) { var it = items[+(o.i || 0)] || items[0], f = it.f, ref = [f.autor, '(' + f.anio + ').', '<i>' + f.titulo + '</i>.', f.editorial + '.'];
      return [{ vis: caja(it.original), txt: 'El texto original de la fuente.' }, { vis: caja('«' + it.cita + '» (' + f.autor.split(',')[0] + ', ' + f.anio + ')'), txt: 'La <b>cita textual</b> copia las palabras exactas, entre comillas y con el autor.' }, { vis: caja(it.parafrasis + ' (' + f.autor.split(',')[0] + ', ' + f.anio + ')'), txt: 'La <b>paráfrasis</b> dice la idea con palabras propias, y también nombra al autor.' }, { vis: '<p class="lb-pt-g">' + ref.map(function (r, j) { return bloq(r, ['autor', 'año', 'título', 'editorial'][j], CL[j]); }).join(' ') + '</p>', txt: 'La <b>referencia bibliográfica</b>: autor, año, título y editorial, en ese orden.' }]; });
  } };
  // ---- LENGUA: ejercicios ----
  function rot(items, ult) { if (items.length < 2) return 0; var x; do { x = R(0, items.length - 1); } while (x === ult.v); ult.v = x; return x; }
  M.etiquetar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Tocá una etiqueta y después el fragmento que le corresponde.', function (c) { var it = items[rot(items, u)], labs = p.etiquetas || [], k = 0, act = null;
      if (!labs.length) it.texto.replace(/\[\[[^|\]]+\|([^\]]+)\]\]/g, function (_, l) { if (labs.indexOf(l) < 0) labs.push(l); });
      c.innerHTML = '<div class="lb-banco">' + labs.map(function (l, j) { return '<button type="button" class="lb-chip" data-lab="' + j + '" style="border-color:' + CL[j % CL.length] + '">' + l + '</button>'; }).join('') + '</div>' + caja(it.texto.replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, function (_, f, l) { return '<button type="button" class="lb-frag" data-ok="' + labs.indexOf(l) + '" style="border:2px dashed #999;border-radius:6px;background:#fff;padding:1px 4px;margin:1px;cursor:pointer">' + f + '</button>'; }));
      c.onclick = function (e) { var l = e.target.closest('[data-lab]'), fg = e.target.closest('.lb-frag'); if (l) { act = +l.getAttribute('data-lab'); [].forEach.call(c.querySelectorAll('[data-lab]'), function (x) { x.classList.toggle('sel', x === l); }); }
        if (fg && act !== null) { fg.setAttribute('data-puesto', act); fg.style.border = '2px solid ' + CL[act % CL.length]; fg.style.background = CL[act % CL.length] + '22'; fg.title = labs[act]; } };
      return { comprobar: function () { var F2 = [].slice.call(c.querySelectorAll('.lb-frag')), falt = F2.filter(function (x) { return !x.hasAttribute('data-puesto'); }).length; if (falt) return { ok: false, msg: 'Te faltan ' + falt + ' fragmento(s) por etiquetar.' };
          var mal = F2.filter(function (x) { return x.getAttribute('data-puesto') !== x.getAttribute('data-ok'); }); F2.forEach(function (x) { x.style.outline = mal.indexOf(x) >= 0 ? '3px solid #c2416b' : 'none'; });
          return mal.length ? { ok: false, msg: 'Hay ' + mal.length + ' mal (con borde rojo). ' + (it.ayuda || '') } : { ok: true, msg: it.bien || '¡Todo bien etiquetado!' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-frag'), function (x) { var a = +x.getAttribute('data-ok'); x.setAttribute('data-puesto', a); x.style.border = '2px solid ' + CL[a % CL.length]; x.style.background = CL[a % CL.length] + '22'; }); } };
    }); otroEj(el);
  } };
  M.analizar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Analizá la oración: llevá cada etiqueta debajo de su parte.', function (c) { var it = items[rot(items, u)], B = it.bloques, labs = mezclar(B.map(function (b) { return b[1]; }).concat(it.extra || []));
      c.innerHTML = '<div class="lb-cajas" style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center">' + B.map(function (b, j) { return '<div class="lb-caja" data-dest="' + j + '" data-esp="' + esc(b[1]) + '" style="min-width:90px"><b>' + b[0] + '</b><div class="lb-dest-c"></div></div>'; }).join('') + '</div><div class="lb-banco">' + labs.map(function (l, j) { return chip('e' + j, l, ' data-c="' + esc(l) + '"'); }).join('') + '</div><p class="lb-ayuda">Tocá una etiqueta y después la parte de la oración.</p>';
      H.tocarYUbicar(c);
      return { comprobar: function () { var mal = 0, vac = 0; [].forEach.call(c.querySelectorAll('.lb-caja'), function (d) { var ch = d.querySelectorAll('.lb-chip'); if (!ch.length) { vac++; return; } [].forEach.call(ch, function (x) { var ok = x.getAttribute('data-c') === d.getAttribute('data-esp'); x.classList.toggle('bien', ok); x.classList.toggle('mal', !ok); if (!ok) mal++; }); });
          if (vac) return { ok: false, msg: 'Te faltan ubicar etiquetas en ' + vac + ' parte(s).' }; return mal ? { ok: false, msg: 'Hay ' + mal + ' etiqueta(s) mal ubicadas. ' + (it.ayuda || 'Empezá por el verbo y preguntale «¿quién?».') } : { ok: true, msg: it.bien || '¡Análisis correcto!' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-caja'), function (d) { var ch = [].filter.call(c.querySelectorAll('.lb-chip'), function (x) { return x.getAttribute('data-c') === d.getAttribute('data-esp') && !x.closest('.lb-caja'); })[0]; if (ch) d.querySelector('.lb-dest-c').appendChild(ch); }); } };
    }); otroEj(el);
  } };
  M.completar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Elegí en cada hueco la opción correcta.', function (c) { var it = items[rot(items, u)];
      c.innerHTML = caja(it.texto.replace(/\[\[([^\]]+)\]\]/g, function (_, o) { var ops = o.split('/'); return '<select class="lb-inp" data-ok="' + esc(ops[0]) + '" style="width:auto;display:inline-block;margin:2px"><option value="">…</option>' + mezclar(ops).map(function (x) { return '<option>' + x + '</option>'; }).join('') + '</select>'; }));
      return { comprobar: function () { var S = [].slice.call(c.querySelectorAll('select')); if (S.some(function (x) { return !x.value; })) return { ok: false, msg: 'Completá todos los huecos.' }; var mal = S.filter(function (x) { return x.value !== x.getAttribute('data-ok'); }); S.forEach(function (x) { x.style.borderColor = mal.indexOf(x) >= 0 ? '#c2416b' : '#0e7c7b'; });
          return mal.length ? { ok: false, msg: 'Hay ' + mal.length + ' hueco(s) mal. ' + (it.ayuda || '') } : { ok: true, msg: it.bien || '¡Bien!' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('select'), function (x) { x.value = x.getAttribute('data-ok'); }); } };
    }); otroEj(el);
  } };
  M.completar_banco_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Llevá cada ficha a su hueco.', function (c) { var it = items[rot(items, u)], fichas = [];
      var html = it.texto.replace(/\[\[([^\]]+)\]\]/g, function (_, w) { fichas.push(w); return '<span class="lb-caja" data-dest="' + (fichas.length - 1) + '" data-esp="' + esc(w) + '" style="display:inline-block;min-width:70px;min-height:30px;vertical-align:middle;padding:2px"><span class="lb-dest-c"></span></span>'; });
      c.innerHTML = caja(html) + '<div class="lb-banco">' + mezclar(fichas.concat(it.extra || [])).map(function (w, j) { return chip('f' + j, w, ' data-c="' + esc(w) + '"'); }).join('') + '</div><p class="lb-ayuda">Tocá una ficha y después el hueco.</p>';
      H.tocarYUbicar(c);
      return { comprobar: function () { var D2 = [].slice.call(c.querySelectorAll('.lb-caja')), vac = D2.filter(function (d) { return !d.querySelector('.lb-chip'); }).length; if (vac) return { ok: false, msg: 'Te faltan ' + vac + ' hueco(s).' };
          var mal = 0; D2.forEach(function (d) { [].forEach.call(d.querySelectorAll('.lb-chip'), function (x) { var ok = x.getAttribute('data-c') === d.getAttribute('data-esp'); x.classList.toggle('bien', ok); x.classList.toggle('mal', !ok); if (!ok) mal++; }); });
          return mal ? { ok: false, msg: 'Hay ' + mal + ' ficha(s) en un hueco equivocado. ' + (it.ayuda || '') } : { ok: true, msg: it.bien || '¡Bien!' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-caja'), function (d) { var ch = [].filter.call(c.querySelectorAll('.lb-banco .lb-chip'), function (x) { return x.getAttribute('data-c') === d.getAttribute('data-esp'); })[0]; if (ch && !d.querySelector('.lb-chip')) d.querySelector('.lb-dest-c').appendChild(ch); }); } };
    }); otroEj(el);
  } };
  M.conjugar_x = { tipo: 'ejercicio', render: function (el, p, api) { var vs = p.verbos || VREG, ts = p.tiempos || ['presente', 'pretérito perfecto simple', 'pretérito imperfecto', 'futuro'];
    respuesta(el, api, function () { var v = pick(vs), t = pick(ts), k = R(0, 5), c = conj(v, t, k), w = c[0] + c[1]; return { cons: 'Conjugá <b>' + v + '</b> en <b>' + t + '</b>, persona: <b>' + PERS[k] + '</b>.', campos: [{ tipo: 'texto', lab: PERS[k], v: [w] }], ayuda: 'Raíz ' + c[0] + '- + la desinencia de ' + t + '. Cuidá la tilde.', bien: '¡Bien! ' + PERS[k] + ' ' + w + '.' }; }); otroEj(el);
  } };
  M.tilde_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Tocá la sílaba que lleva tilde, o «No lleva tilde».', function (c) { var it = items[rot(items, u)], sin = function (x) { return x.normalize('NFD').replace(/[́]/g, '').normalize('NFC'); }, con = it.s.map(function (x) { return /[áéíóú]/.test(x); }), idx = con.indexOf(true);
      c.innerHTML = '<p class="lb-pt-g">' + it.s.map(function (x, j) { return '<button type="button" class="lb-chip" data-j="' + j + '">' + sin(x) + '</button>'; }).join(' - ') + '</p><div class="lb-banco"><button type="button" class="lb-chip" data-j="-1">No lleva tilde</button></div>';
      c.onclick = function (e) { var b = e.target.closest('[data-j]'); if (!b) return; [].forEach.call(c.querySelectorAll('[data-j]'), function (x) { x.classList.toggle('sel', x === b); }); };
      return { comprobar: function () { var s2 = c.querySelector('[data-j].sel'); if (!s2) return { ok: false, msg: 'Tocá una ficha y después comprobá.' }; var ok = +s2.getAttribute('data-j') === idx; s2.classList.add(ok ? 'bien' : 'mal'); return ok ? { ok: true, msg: '¡Bien! Se escribe «' + it.s.join('') + '».' } : { ok: false, msg: it.ayuda || 'Buscá la sílaba tónica, clasificá la palabra y aplicá la regla.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('[data-j]'), function (x) { x.classList.toggle('sel', +x.getAttribute('data-j') === idx); }); } };
    }); otroEj(el);
  } };
  M.silabas_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Tocá entre las letras para separar en sílabas.', function (c) { var it = items[rot(items, u)], partes = it.split('-'), w = partes.join(''), cortes = [], acc = 0; partes.slice(0, -1).forEach(function (q) { acc += q.length; cortes.push(acc); });
      c.innerHTML = '<p class="lb-pt-g" style="letter-spacing:2px">' + w.split('').map(function (ch, j) { return ch + (j < w.length - 1 ? '<button type="button" data-c="' + (j + 1) + '" style="border:none;background:none;color:#ccc;cursor:pointer;padding:0 2px;font-weight:700">·</button>' : ''); }).join('') + '</p>';
      c.onclick = function (e) { var b = e.target.closest('[data-c]'); if (!b) return; var on = b.textContent === '·'; b.textContent = on ? '-' : '·'; b.style.color = on ? '#0e7c7b' : '#ccc'; };
      var mios = function () { return [].filter.call(c.querySelectorAll('[data-c]'), function (b) { return b.textContent === '-'; }).map(function (b) { return +b.getAttribute('data-c'); }); };
      return { comprobar: function () { var m2 = mios(); if (!m2.length && cortes.length) return { ok: false, msg: 'Tocá entre las letras para marcar los cortes.' }; var ok = m2.join() === cortes.join(); return ok ? { ok: true, msg: '¡Bien! ' + it + '.' } : { ok: false, msg: 'Revisalo. Decila en voz alta, golpe por golpe.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('[data-c]'), function (b) { var on = cortes.indexOf(+b.getAttribute('data-c')) >= 0; b.textContent = on ? '-' : '·'; b.style.color = on ? '#0e7c7b' : '#ccc'; }); } };
    }); otroEj(el);
  } };
  M.puntuar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 }, SG = p.signos || ['', ',', '.', ';', ':'];
    H.ejercicio(el, api, p.consigna || 'Tocá entre las palabras para poner el signo que falta (cada toque cambia el signo).', function (c) { var it = items[rot(items, u)], tok = it.texto.split(/\s+/), esp = [], pal = [];
      tok.forEach(function (t) { var m = t.match(/^(.*?)(\[\[([^\]]+)\]\])?$/); pal.push(m[1]); esp.push(m[3] || ''); });
      c.innerHTML = caja(pal.map(function (w, j) { return w + '<button type="button" data-g="' + j + '" data-ok="' + esc(esp[j]) + '" style="min-width:16px;border:1px dashed #bbb;border-radius:4px;background:#fff;margin:0 3px;padding:0 3px;color:#0e7c7b;font-weight:800;cursor:pointer">' + '&nbsp;' + '</button>'; }).join(''));
      c.onclick = function (e) { var b = e.target.closest('[data-g]'); if (!b) return; var i = (SG.indexOf(b.getAttribute('data-v') || '') + 1) % SG.length; b.setAttribute('data-v', SG[i]); b.innerHTML = SG[i] || '&nbsp;'; };
      return { comprobar: function () { var G = [].slice.call(c.querySelectorAll('[data-g]')), mal = G.filter(function (b) { return (b.getAttribute('data-v') || '') !== b.getAttribute('data-ok'); }); G.forEach(function (b) { b.style.borderColor = mal.indexOf(b) >= 0 ? '#c2416b' : '#bbb'; });
          return mal.length ? { ok: false, msg: 'Hay ' + mal.length + ' lugar(es) para revisar (marcados). ' + (it.ayuda || '') } : { ok: true, msg: it.bien || '¡Bien puntuado!' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('[data-g]'), function (b) { b.setAttribute('data-v', b.getAttribute('data-ok')); b.innerHTML = b.getAttribute('data-ok') || '&nbsp;'; }); } };
    }); otroEj(el);
  } };
  M.ordenar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Ordená las tarjetas: tocalas en el orden correcto.', function (c) { var it = items[rot(items, u)], L = it.lista || it, orden = [];
      c.innerHTML = '<div class="lb-dest" style="min-height:44px;border:2px dashed #0e7c7b;border-radius:10px;padding:6px;text-align:left"></div><div class="lb-banco">' + mezclar(L.map(function (t, j) { return [t, j]; })).map(function (x) { return '<button type="button" class="lb-chip" data-j="' + x[1] + '">' + x[0] + '</button>'; }).join('') + '</div><p class="lb-ayuda">Tocá una tarjeta puesta para devolverla.</p>';
      var dest = c.querySelector('.lb-dest'), banco = c.querySelector('.lb-banco');
      c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (!b) return; (b.parentNode === banco ? dest : banco).appendChild(b); b.classList.remove('bien', 'mal'); };
      return { comprobar: function () { var D2 = [].slice.call(dest.querySelectorAll('.lb-chip')); if (D2.length < L.length) return { ok: false, msg: 'Te faltan ubicar ' + (L.length - D2.length) + ' tarjeta(s).' }; var mal = 0; D2.forEach(function (b, k) { var ok = +b.getAttribute('data-j') === k; b.classList.toggle('bien', ok); b.classList.toggle('mal', !ok); if (!ok) mal++; });
          return mal ? { ok: false, msg: 'Hay ' + mal + ' fuera de lugar. ' + (it.ayuda || '') } : { ok: true, msg: it.bien || '¡Orden correcto!' }; },
        resolver: function () { var all = [].slice.call(c.querySelectorAll('.lb-chip')).sort(function (a, b) { return a.getAttribute('data-j') - b.getAttribute('data-j'); }); all.forEach(function (b) { dest.appendChild(b); }); } };
    }); otroEj(el);
  } };
  M.unir_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Uní cada elemento de la izquierda con su pareja: tocá uno y después el otro.', function (c) { var it = items[rot(items, u)], pares = it.pares || it, izq = null, n = 0;
      c.innerHTML = '<div style="display:flex;gap:12px;justify-content:center"><div>' + pares.map(function (q, j) { return '<button type="button" class="lb-chip" data-i="' + j + '" style="display:block;width:100%;margin:4px 0">' + q[0] + '</button>'; }).join('') + '</div><div>' + mezclar(pares.map(function (q, j) { return [q[1], j]; })).map(function (q) { return '<button type="button" class="lb-chip" data-d="' + q[1] + '" style="display:block;width:100%;margin:4px 0">' + q[0] + '</button>'; }).join('') + '</div></div>';
      c.onclick = function (e) { var a = e.target.closest('[data-i]'), b = e.target.closest('[data-d]'); if (a) { izq = a; [].forEach.call(c.querySelectorAll('[data-i]'), function (x) { x.classList.toggle('sel', x === a); }); }
        if (b && izq) { var col = CL[n++ % CL.length]; [].forEach.call(c.querySelectorAll('[data-par="' + izq.getAttribute('data-i') + '"]'), function (x) { x.removeAttribute('data-par'); x.style.borderColor = ''; }); izq.setAttribute('data-par', izq.getAttribute('data-i')); b.setAttribute('data-par', izq.getAttribute('data-i')); izq.style.borderColor = b.style.borderColor = col; izq.classList.remove('sel'); izq = null; } };
      return { comprobar: function () { var D2 = [].slice.call(c.querySelectorAll('[data-d]')), falt = D2.filter(function (x) { return !x.hasAttribute('data-par'); }).length; if (falt) return { ok: false, msg: 'Te faltan ' + falt + ' pareja(s).' }; var mal = D2.filter(function (x) { return x.getAttribute('data-par') !== x.getAttribute('data-d'); }); D2.forEach(function (x) { x.classList.toggle('mal', mal.indexOf(x) >= 0); x.classList.toggle('bien', mal.indexOf(x) < 0); });
          return mal.length ? { ok: false, msg: 'Hay ' + mal.length + ' pareja(s) mal.' } : { ok: true, msg: it.bien || '¡Todas bien!' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('[data-d],[data-i]'), function (x) { x.setAttribute('data-par', x.getAttribute('data-d') || x.getAttribute('data-i')); x.style.borderColor = CL[+(x.getAttribute('data-d') || x.getAttribute('data-i')) % CL.length]; }); } };
    }); otroEj(el);
  } };
  M.armar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Armá la respuesta tocando las piezas en orden.', function (c) { var it = items[rot(items, u)], piezas = it.piezas, junta = it.junto ? '' : ' ';
      c.innerHTML = (it.cons ? '<p class="lb-ayuda">' + it.cons + '</p>' : '') + '<div class="lb-dest" style="min-height:44px;border:2px dashed #0e7c7b;border-radius:10px;padding:6px"></div><div class="lb-banco">' + mezclar(piezas.concat(it.extra || [])).map(function (w) { return '<button type="button" class="lb-chip" data-w="' + esc(w) + '">' + w + '</button>'; }).join('') + '</div>';
      var dest = c.querySelector('.lb-dest'), banco = c.querySelector('.lb-banco'); c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (b) (b.parentNode === banco ? dest : banco).appendChild(b); };
      return { comprobar: function () { var w = [].map.call(dest.querySelectorAll('.lb-chip'), function (b) { return b.getAttribute('data-w'); }); if (!w.length) return { ok: false, msg: 'Tocá las piezas para armar.' }; var ok = w.join(junta) === piezas.join(junta); dest.style.borderColor = ok ? '#0e7c7b' : '#c2416b'; return ok ? { ok: true, msg: it.bien || '¡Bien armado!' } : { ok: false, msg: it.ayuda || 'Revisá el orden o sobra alguna pieza.' }; },
        resolver: function () { [].forEach.call(dest.querySelectorAll('.lb-chip'), function (b) { banco.appendChild(b); }); piezas.forEach(function (w) { var b = [].filter.call(banco.querySelectorAll('.lb-chip'), function (x) { return x.getAttribute('data-w') === w; })[0]; if (b) dest.appendChild(b); }); } };
    }); otroEj(el);
  } };
  M.borrar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Prueba del borrado: tachá las oraciones que se pueden sacar sin perder la idea principal.', function (c) { var it = items[rot(items, u)];
      c.innerHTML = caja(it.oraciones.map(function (o2, j) { return '<span data-o="' + j + '" data-es="' + (o2[1] ? 1 : 0) + '" style="cursor:pointer;border-radius:4px;padding:0 2px">' + o2[0] + '</span>'; }).join(' '));
      c.onclick = function (e) { var s3 = e.target.closest('[data-o]'); if (!s3) return; var t = s3.getAttribute('data-t') === '1'; s3.setAttribute('data-t', t ? '0' : '1'); s3.style.textDecoration = t ? 'none' : 'line-through'; s3.style.opacity = t ? 1 : .45; };
      return { comprobar: function () { var S = [].slice.call(c.querySelectorAll('[data-o]')); if (!S.some(function (x) { return x.getAttribute('data-t') === '1'; })) return { ok: false, msg: 'Tocá las oraciones para tacharlas.' }; var mal = S.filter(function (x) { return (x.getAttribute('data-t') === '1') === (x.getAttribute('data-es') === '1'); }); S.forEach(function (x) { x.style.background = mal.indexOf(x) >= 0 ? '#c2416b22' : 'transparent'; });
          return mal.length ? { ok: false, msg: 'Revisá las marcadas: o tachaste algo importante o dejaste algo que se puede sacar.' } : { ok: true, msg: it.bien || '¡Bien! Lo que quedó es la idea principal.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('[data-o]'), function (x) { var t = x.getAttribute('data-es') !== '1'; x.setAttribute('data-t', t ? '1' : '0'); x.style.textDecoration = t ? 'line-through' : 'none'; x.style.opacity = t ? .45 : 1; }); } };
    }); otroEj(el);
  } };
  function tieneTodo(txt, lst) { var t = H.norm(txt); return (lst || []).filter(function (w) { return [].concat(w).every(function (x) { return x.split('|').some(function (y) { return t.indexOf(H.norm(y)) >= 0; }); }); }).length === (lst || []).length; }
  M.transformar_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Reescribí el texto como se pide.', function (c) { var it = items[rot(items, u)];
      c.innerHTML = '<p class="lb-ayuda">' + it.cons + '</p>' + caja(it.texto) + '<textarea class="lb-inp" rows="3" style="width:100%;margin-top:8px" placeholder="Escribí acá tu versión">' + '</textarea>';
      var ta = c.querySelector('textarea');
      return { comprobar: function () { var v = ta.value.trim(); if (v.length < 5) return { ok: false, msg: 'Escribí tu versión.' }; var faltan = (it.pide || []).filter(function (w) { return !tieneTodo(v, [w]); }), sobran = (it.prohibe || []).filter(function (w) { return tieneTodo(v, [w]); });
          if (!faltan.length && !sobran.length) return { ok: true, msg: (it.bien || '¡Bien!') + (it.modelo ? ' Una versión posible: «' + it.modelo + '».' : '') };
          return { ok: false, msg: (sobran.length ? 'Todavía aparece: «' + sobran.map(function (x) { return [].concat(x)[0].split('|')[0]; }).join('», «') + '». ' : '') + (faltan.length ? (it.ayuda || 'Te falta algo de lo pedido.') : '') }; },
        resolver: function () { ta.value = it.modelo || ''; } };
    }); otroEj(el);
  } };
  M.escribir_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Escribí siguiendo la lista: se va marcando mientras escribís.', function (c) { var it = items[rot(items, u)], K = it.criterios;
      c.innerHTML = '<p class="lb-ayuda">' + it.cons + '</p><textarea class="lb-inp" rows="4" style="width:100%"></textarea><div class="lb-chk" style="text-align:left;margin-top:6px"></div>';
      var ta = c.querySelector('textarea'), ck = c.querySelector('.lb-chk'), cumple = function (k) { var v = ta.value; if (k.min) return v.split(/\s+/).filter(Boolean).length >= k.min; if (k.re) return new RegExp(k.re, 'i').test(v); return tieneTodo(v, [k.alguna]); };
      var pint = function () { ck.innerHTML = K.map(function (k) { return '<div>' + (cumple(k) ? '✅' : '☐') + ' ' + k.txt + '</div>'; }).join(''); }; ta.oninput = pint; pint();
      return { comprobar: function () { var f = K.filter(function (k) { return !cumple(k); }); pint(); return f.length ? { ok: false, msg: 'Te falta: ' + f.map(function (k) { return k.txt; }).join('; ') + '.' } : { ok: true, msg: it.bien || '¡Cumple todo! Releelo una vez más antes de seguir.' }; },
        resolver: function () { ta.value = it.modelo || ''; pint(); } };
    }); otroEj(el);
  } };
  M.relacion_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 }, RL = p.relaciones || ['causa', 'consecuencia', 'oposición', 'adición', 'tiempo'];
    H.ejercicio(el, api, p.consigna || 'Primero elegí la relación entre las ideas y después el conector.', function (c) { var it = items[rot(items, u)];
      c.innerHTML = caja(it.a + ' <b class="lb-hueco" style="color:#0e7c7b">▢</b> ' + it.b) + '<p class="lb-ayuda">1. Relación</p><div class="lb-banco" data-g="r">' + RL.map(function (r) { return '<button type="button" class="lb-chip" data-v="' + r + '">' + r + '</button>'; }).join('') + '</div><p class="lb-ayuda">2. Conector</p><div class="lb-banco" data-g="c">' + mezclar(it.ok.slice(0, 1).concat(it.mal)).map(function (r) { return '<button type="button" class="lb-chip" data-v="' + esc(r) + '">' + r + '</button>'; }).join('') + '</div>';
      c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (!b) return; var g = b.parentNode; [].forEach.call(g.querySelectorAll('.lb-chip'), function (x) { x.classList.toggle('sel', x === b); }); if (g.getAttribute('data-g') === 'c') c.querySelector('.lb-hueco').textContent = b.getAttribute('data-v'); };
      var val = function (g) { var s3 = c.querySelector('[data-g="' + g + '"] .sel'); return s3 && s3.getAttribute('data-v'); };
      return { comprobar: function () { if (!val('r') || !val('c')) return { ok: false, msg: 'Tocá una ficha en cada paso.' }; var okr = val('r') === it.relacion, okc = it.ok.indexOf(val('c')) >= 0; return okr && okc ? { ok: true, msg: it.bien || '¡Bien! La relación es de ' + it.relacion + '.' } : { ok: false, msg: !okr ? 'Revisá la relación: ¿una idea es causa, consecuencia o se opone a la otra?' : 'La relación está bien, pero ese conector no la expresa.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('[data-g="r"] .lb-chip'), function (x) { x.classList.toggle('sel', x.getAttribute('data-v') === it.relacion); }); [].forEach.call(c.querySelectorAll('[data-g="c"] .lb-chip'), function (x) { x.classList.toggle('sel', x.getAttribute('data-v') === it.ok[0]); }); c.querySelector('.lb-hueco').textContent = it.ok[0]; } };
    }); otroEj(el);
  } };
  M.dictado_x = { tipo: 'ejercicio', render: function (el, p, api) { var items = p.items || [], u = { v: -1 };
    H.ejercicio(el, api, p.consigna || 'Escuchá la oración y escribila.', function (c) { var it = items[rot(items, u)], frase = it.texto || it;
      c.innerHTML = '<button type="button" class="lb-btn suave" data-hablar="1">🔊 Escuchar</button> <button type="button" class="lb-btn suave" data-hablar="2">🐢 Más lento</button><textarea class="lb-inp" rows="2" style="width:100%;margin-top:8px"></textarea><div class="lb-dif" style="text-align:left"></div>';
      c.onclick = function (e) { var b = e.target.closest('[data-hablar]'); if (!b || !window.speechSynthesis) return; var us = new SpeechSynthesisUtterance(frase.replace(/[«»]/g, '')); us.lang = 'es-AR'; us.rate = b.getAttribute('data-hablar') === '2' ? .6 : .9; speechSynthesis.cancel(); speechSynthesis.speak(us); };
      var ta = c.querySelector('textarea'), pal = function (x) { return x.toLowerCase().replace(/[.,;:¡!¿?«»"]/g, '').split(/\s+/).filter(Boolean); };
      return { comprobar: function () { var a = pal(ta.value), b2 = pal(frase); if (!a.length) return { ok: false, msg: 'Escribí lo que escuchaste.' }; var mal = b2.filter(function (w, i) { return a[i] !== w; });
          c.querySelector('.lb-dif').innerHTML = b2.map(function (w, i) { return a[i] === w ? w : '<b style="color:#c2416b;text-decoration:underline">' + (a[i] || '___') + '</b>'; }).join(' ');
          return mal.length ? { ok: false, msg: 'Hay ' + mal.length + ' palabra(s) para revisar (en rojo). Fijate tildes y letras.' } : { ok: true, msg: '¡Perfecto!' }; },
        resolver: function () { ta.value = frase; } };
    }); otroEj(el);
  } };

  M.binario_conv = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'ambos';
    respuesta(el, api, function () { var n = R(5, 200), b = n.toString(2);
      if (md === 'a_decimal' || (md === 'ambos' && Math.random() < .5)) return { cons: 'Pasá a decimal el número binario <b>' + b + '</b>.', campos: [{ v: n }], ayuda: 'Cada lugar desde la derecha vale 1, 2, 4, 8, 16…: sumá los que tienen 1.', bien: '¡Bien! ' + b + ' = ' + n + '.' };
      return { cons: 'Pasá a binario el número <b>' + n + '</b>.', campos: [{ tipo: 'texto', v: b }], ayuda: 'Dividí por 2 una y otra vez y leé los restos de abajo hacia arriba. Es ' + b + '.', bien: '¡Bien! ' + n + ' = ' + b + '.' }; });
  } };
  M.recta_explorar = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('x', 'Número', -10, 10, 1, -4), function (o) { var X = function (v) { return 130 + v * 11; }, t = '';
      for (var k = -10; k <= 10; k++) t += '<line class="rayo" x1="' + X(k) + '" y1="' + (k ? 32 : 26) + '" x2="' + X(k) + '" y2="' + (k ? 40 : 46) + '"/>';
      var sv = function (op, dist) { return '<svg viewBox="0 0 260 70" class="lb2-svg"><line class="rayo" x1="5" y1="36" x2="255" y2="36"/>' + t + '<text x="130" y="62">0</text>' + (dist ? '<line class="diag" x1="130" y1="36" x2="' + X(o.x) + '" y2="36" style="stroke-width:4"/>' : '') + '<circle cx="' + X(o.x) + '" cy="36" r="6" class="pt"/>' + (op ? '<circle cx="' + X(-o.x) + '" cy="36" r="5" class="pt2"/>' : '') + '</svg>'; };
      return [{ vis: sv(0, 0), txt: 'Ubicamos el <b>' + sig(o.x) + '</b> en la recta: ' + (o.x < 0 ? 'a la izquierda del 0.' : o.x > 0 ? 'a la derecha del 0.' : 'es el 0.') },
        { vis: sv(1, 0), txt: 'Su <b>opuesto</b> está a la misma distancia, del otro lado del 0: <b>' + sig(-o.x) + '</b>.' },
        { vis: sv(1, 1) + '<p class="lb-cn-res">|' + sig(o.x) + '| = ' + Math.abs(o.x) + '</p>', txt: 'El <b>valor absoluto</b> es la distancia al 0: siempre positiva.' }]; });
  } };
  M.signos = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'Primer factor', -9, 9, 1, -3) + ctrl('b', 'Segundo factor', -9, 9, 1, 4), function (o) { var a = o.a, b = o.b, sm = a * b;
      var tab = function (on) { var c = function (x, y, t) { return '<td class="' + (on && (a > 0) === x && (b > 0) === y ? 'on' : '') + '">' + t + '</td>'; }; return '<table class="lb2-tab"><tr><th>×</th><th>+</th><th>−</th></tr><tr><th>+</th>' + c(true, true, '+') + c(true, false, '−') + '</tr><tr><th>−</th>' + c(false, true, '−') + c(false, false, '+') + '</tr></table>'; };
      if (!a || !b) return [{ vis: '<p class="lb-cn-res">(' + sig(a) + ') × (' + sig(b) + ') = 0</p>', txt: 'Si un factor es 0, el producto es 0.' }];
      return [{ vis: tab(false) + '<p class="lb-pt-f">(' + sig(a) + ') × (' + sig(b) + ')</p>', txt: 'Primero miramos los <b>signos</b>: ' + (a > 0 ? '+' : '−') + ' y ' + (b > 0 ? '+' : '−') + '.' },
        { vis: tab(true) + '<p class="lb-pt-f">(' + sig(a) + ') × (' + sig(b) + ')</p>', txt: (a > 0) === (b > 0) ? 'Signos <b>iguales</b>: el resultado es <b>+</b>.' : 'Signos <b>distintos</b>: el resultado es <b>−</b>.' },
        { vis: tab(true) + '<p class="lb-cn-res">(' + sig(a) + ') × (' + sig(b) + ') = ' + sig(sm) + '</p>', txt: 'Después multiplicamos los números sin signo: ' + Math.abs(a) + ' × ' + Math.abs(b) + ' = ' + Math.abs(sm) + '. Para dividir vale la misma regla.' }]; });
  } };
  M.potencias_explorar = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('b', 'Base', -6, 10, 1, -2) + ctrl('e', 'Exponente', 0, 6, 1, 3), function (o) { var b = o.b, e = o.e, bs = b < 0 ? '(' + sig(b) + ')' : String(b), P = [{ vis: '<p class="lb-pt-g">' + bs + '<sup>' + e + '</sup></p>', txt: 'La base es <b>' + bs + '</b> y el exponente <b>' + e + '</b>: se multiplica la base ' + e + ' veces.' }];
      if (e === 0) P.push({ vis: '<p class="lb-cn-res">' + bs + '<sup>0</sup> = 1</p>', txt: 'Todo número (distinto de 0) elevado a 0 da 1.' });
      for (var i = 1; i <= e; i++) P.push({ vis: '<p class="lb-pt-f">' + Array(i + 1).join(bs + ' · ').slice(0, -3) + '</p><p class="lb-pt-g">= ' + fmt(Math.pow(b, i)) + '</p>', txt: i === 1 ? 'Un factor: la misma base.' : 'Multiplicamos otra vez por ' + bs + '.' + (b < 0 ? ' El signo cambia en cada factor negativo.' : '') });
      if (e > 0) P.push({ vis: '<p class="lb-cn-res">' + bs + '<sup>' + e + '</sup> = ' + fmt(Math.pow(b, e)) + '</p>', txt: b < 0 ? 'Base negativa: con exponente par da positivo, con impar, negativo.' : 'Ese es el resultado.' });
      return P; });
  } };
  M.raiz_explorar = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('n', 'Número', 1, 200, 1, 49), function (o) { var n = o.n, k = Math.floor(Math.sqrt(n)), exacta = k * k === n, s = Math.min(10, 140 / Math.max(k, 1));
      var sv = function (lado) { var g = ''; for (var i = 0; i < lado; i++) for (var j = 0; j < lado; j++) g += '<rect x="' + (5 + i * s) + '" y="' + (5 + j * s) + '" width="' + s + '" height="' + s + '" class="c1"/>'; return '<svg viewBox="0 0 ' + (10 + k * s) + ' ' + (10 + k * s) + '" class="lb2-svg" style="max-height:150px">' + g + '</svg>'; };
      return [{ vis: '<p class="lb-pt-g">√' + n + '</p>', txt: 'Buscamos un número que multiplicado por sí mismo dé <b>' + n + '</b>.' },
        { vis: sv(k), txt: 'Con ' + n + ' cuadraditos armamos el cuadrado más grande posible: de lado <b>' + k + '</b> (' + k + ' × ' + k + ' = ' + k * k + ').' },
        { vis: sv(k) + '<p class="lb-cn-res">' + (exacta ? '√' + n + ' = ' + k : '√' + n + ' está entre ' + k + ' y ' + (k + 1)) + '</p>', txt: exacta ? 'No sobra ninguno: ' + n + ' es un <b>cuadrado perfecto</b>.' : 'Sobran cuadraditos: ' + k * k + ' < ' + n + ' < ' + (k + 1) * (k + 1) + ', la raíz no es exacta.' }]; });
  } };
  M.proporcionalidad = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var inv = p.modo === 'inversa';
    escena(el, ctrl('k', inv ? 'Producto constante' : 'Constante k', inv ? 12 : 1, inv ? 60 : 8, inv ? 12 : 1, inv ? 24 : 3), function (o) { var xs = [1, 2, 3, 4, 6], k = o.k, ys = xs.map(function (x) { return inv ? r2(k / x) : k * x; }), W = 230, Hh = 140, my = Math.max.apply(null, ys);
      var pts = xs.map(function (x, i) { return (20 + x * 32) + ',' + (Hh - 10 - ys[i] / my * (Hh - 30)).toFixed(1); });
      var tab = '<table class="lb2-tab"><tr><th>x</th>' + xs.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr><th>y</th>' + ys.map(function (y) { return '<td>' + fmt(y) + '</td>'; }).join('') + '</tr></table>';
      var graf = 
        '<svg viewBox="0 0 ' + W + ' ' + Hh + '" class="lb2-svg"><line class="rayo" x1="20" y1="' + (Hh - 10) + '" x2="' + (W - 5) + '" y2="' + (Hh - 10) + '"/><line class="rayo" x1="20" y1="5" x2="20" y2="' + (Hh - 10) + '"/><polyline class="graf" points="' + (inv ? '' : '20,' + (Hh - 10) + ' ') + pts.join(' ') + '"/>' + pts.map(function (q) { return '<circle r="4" class="pt" cx="' + q.split(',')[0] + '" cy="' + q.split(',')[1] + '"/>'; }).join('') + '</svg>' ;
      return [{ vis: tab, txt: 'Armamos la tabla con algunos valores de x.' }, { vis: tab, txt: '' + (inv ? 'Inversa: si x se duplica, y se reduce a la mitad. Siempre x · y = ' + k + '.' : 'Directa: si x se duplica, y también. Siempre y ÷ x = ' + k + ' (la constante): y = ' + k + 'x.') + '' }, { vis: tab + graf, txt: inv ? 'En el gráfico queda una curva que baja.' : 'En el gráfico los puntos quedan en una recta que pasa por el 0.' }]; });
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
  M.plano = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var x = R(-5, 5), y = R(-5, 5);
    el.innerHTML = '<p class="lb-ayuda">Tocá cualquier punto del plano para cambiarlo.</p><div class="lb-vista"></div>'; var v = el.querySelector('.lb-vista');
    function armar() { var Pl = plano(6), cx = Pl.c + x * Pl.s, cy = Pl.c - y * Pl.s, celdas = ''; for (var i = -6; i <= 6; i++) for (var j = -6; j <= 6; j++) celdas += '<circle class="hit" r="6" cx="' + (Pl.c + i * Pl.s) + '" cy="' + (Pl.c - j * Pl.s) + '" data-x="' + i + '" data-y="' + j + '"/>';
      var sv = function (lx, ly) { return '<div style="max-width:280px;margin:auto">' + Pl.svg.replace('</svg>', (lx ? '<line class="diag" x1="' + cx + '" y1="' + cy + '" x2="' + cx + '" y2="' + Pl.c + '"/>' : '') + (ly ? '<line class="diag" x1="' + cx + '" y1="' + cy + '" x2="' + Pl.c + '" y2="' + cy + '"/>' : '') + '<circle class="pt" r="6" cx="' + cx + '" cy="' + cy + '"/>' + celdas + '</svg>') + '</div>'; };
      var cuad = x && y ? 'Está en el <b>' + (x > 0 ? (y > 0 ? 'primer' : 'cuarto') : (y > 0 ? 'segundo' : 'tercer')) + ' cuadrante</b>.' : 'Está sobre un eje.';
      pasoAPaso(v, [{ vis: sv(0, 0), txt: 'Queremos saber dónde está este punto.' },
        { vis: sv(1, 0), txt: 'Primero <b>x</b>: bajamos al eje horizontal. Está en <b>' + x + '</b> (' + (x > 0 ? 'a la derecha' : x < 0 ? 'a la izquierda' : 'en el centro') + ').' },
        { vis: sv(1, 1), txt: 'Después <b>y</b>: vamos al eje vertical. Está en <b>' + y + '</b> (' + (y > 0 ? 'arriba' : y < 0 ? 'abajo' : 'en el centro') + ').' },
        { vis: sv(1, 1) + '<p class="lb-cn-res">P = (' + x + ', ' + y + ')</p>', txt: 'Se escribe (x, y), siempre en ese orden. ' + cuad }]); }
    el.addEventListener('click', function (e) { var h = e.target.closest('[data-x]'); if (h) { x = +h.getAttribute('data-x'); y = +h.getAttribute('data-y'); armar(); } }); armar();
  } };
  M.funcion_lineal = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'Pendiente a', -3, 3, 1, 2) + ctrl('b', 'Ordenada b', -4, 4, 1, 1), function (o) { var Pl = plano(6), xs = [-2, -1, 0, 1, 2], f = function (x) { return o.a * x + o.b; };
      var form = 'y = ' + (o.a === 1 ? '' : o.a === -1 ? '−' : o.a) + (o.a ? 'x' : '') + (o.b ? (o.b > 0 ? (o.a ? ' + ' : '') + o.b : ' − ' + -o.b) : (o.a ? '' : '0'));
      var tab = '<table class="lb2-tab"><tr><th>x</th>' + xs.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr><th>y</th>' + xs.map(function (x) { return '<td>' + f(x) + '</td>'; }).join('') + '</tr></table>';
      var pts = xs.map(function (x) { return '<circle class="pt" r="4" cx="' + (Pl.c + x * Pl.s) + '" cy="' + (Pl.c - f(x) * Pl.s) + '"/>'; }).join(''), lin = '<line class="graf" x1="' + (Pl.c - 6 * Pl.s) + '" y1="' + (Pl.c - f(-6) * Pl.s) + '" x2="' + (Pl.c + 6 * Pl.s) + '" y2="' + (Pl.c - f(6) * Pl.s) + '"/>';
      var gr = function (conLinea) { return '<div style="max-width:220px;margin:auto">' + Pl.svg.replace('</svg>', '<g style="clip-path:inset(0)">' + (conLinea ? lin : '') + pts + '</g></svg>') + '</div>'; };
      return [{ vis: '<p class="lb-pt-g">' + form + '</p>', txt: 'La fórmula dice cómo se calcula y a partir de x.' },
        { vis: '<p class="lb-res">' + form + '</p>' + tab, txt: 'Armamos una tabla: elegimos valores de x y calculamos y.' },
        { vis: tab + gr(false), txt: 'Ubicamos cada par (x, y) en el plano.' },
        { vis: gr(true), txt: 'Los puntos quedan alineados: los unimos con una recta.' },
        { vis: gr(true) + '<p class="lb-nota">b = ' + o.b + ': corta al eje y en ' + o.b + '. a = ' + o.a + ': por cada paso a la derecha ' + (o.a > 0 ? 'sube ' + o.a : o.a < 0 ? 'baja ' + -o.a : 'no cambia') + '.</p>', txt: o.a > 0 ? 'Es <b>creciente</b>.' : o.a < 0 ? 'Es <b>decreciente</b>.' : 'Es <b>constante</b>.' }]; });
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
  M.frecuencias = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var D = datos();
    el.innerHTML = '<div class="lb-vista"></div><div class="lb-pie"><button type="button" class="lb-btn suave" data-o="1">🔄 Otros datos</button></div>'; var v = el.querySelector('.lb-vista');
    function armar() { var f = D.cs.map(function (c) { return D.L.filter(function (x) { return x === c; }).length; }), n = D.L.length, mx = Math.max.apply(null, f);
      var tab = function (filas, pct) { return '<table class="lb2-tab"><tr><th>Valor</th><th>Frecuencia</th>' + (pct ? '<th>%</th>' : '') + '<th></th></tr>' + D.cs.map(function (c, i) { return '<tr><td>' + c + '</td><td>' + (i < filas ? f[i] : '') + '</td>' + (pct ? '<td>' + fmt(r2(f[i] / n * 100)) + ' %</td>' : '') + '<td class="lb2-bar"><i style="width:' + (i < filas && mx ? f[i] / mx * 100 : 0) + '%"></i></td></tr>'; }).join('') + (filas >= D.cs.length ? '<tr><th>Total</th><th>' + n + '</th>' + (pct ? '<th>100 %</th>' : '') + '<th></th></tr>' : '') + '</table>'; };
      var dat = '<p class="lb-nota">Datos: ' + D.L.join(', ') + '.</p>', P = [{ vis: dat + tab(0), txt: 'Tenemos <b>' + n + '</b> respuestas. Hacemos una fila por cada valor distinto.' }];
      D.cs.forEach(function (c, i) { P.push({ vis: dat + tab(i + 1), txt: 'Contamos cuántas veces aparece <b>' + c + '</b>: ' + f[i] + '.' }); });
      P.push({ vis: tab(99, true), txt: 'Las frecuencias suman el total (' + n + '). El % es la frecuencia ÷ ' + n + ' × 100.' });
      pasoAPaso(v, P); }
    el.addEventListener('click', function (e) { if (e.target.closest('[data-o]')) { D = datos(); armar(); } }); armar();
  } };
  M.tabla_frecuencias = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var D = datos(), f = D.cs.map(function (c) { return D.L.filter(function (x) { return x === c; }).length; });
      return { cons: 'Contá los datos y completá la frecuencia de cada valor.', html: '<p class="lb-nota">' + D.L.join(', ') + '.</p>', campos: D.cs.map(function (c, i) { return { lab: c + ':', v: f[i] }; }), ayuda: 'Contá cuántas veces aparece cada uno. Control: tienen que sumar ' + D.L.length + '.', bien: '¡Bien contado! Suman ' + D.L.length + '.' }; });
  } };
  function stats(L) { var s = L.slice().sort(function (a, b) { return a - b; }), n = s.length, media = L.reduce(function (a, b) { return a + b; }, 0) / n, med = n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2, c = {}, mx = 0;
    L.forEach(function (x) { c[x] = (c[x] || 0) + 1; mx = Math.max(mx, c[x]); }); var moda = Object.keys(c).filter(function (k) { return c[k] === mx; }).map(Number); return { media: media, med: med, moda: mx > 1 ? moda : [], s: s }; }
  M.medidas = { tipo: 'ejemplo', pasos: true, render: function (el) {
    var L = [6, 8, 7, 8, 9, 4];
    escena(el, L.map(function (x, i) { return ctrl('d' + i, 'Dato ' + (i + 1), 0, 10, 1, x); }).join(''), function (o) { var D = [0, 1, 2, 3, 4, 5].map(function (i) { return o['d' + i]; }), S = stats(D), cnt = {}, pts = '', suma = D.reduce(function (a, b) { return a + b; }, 0);
      D.forEach(function (x) { cnt[x] = (cnt[x] || 0) + 1; pts += '<circle class="pt" r="6" cx="' + (15 + x * 22) + '" cy="' + (60 - (cnt[x] - 1) * 13) + '"/>'; });
      var sv = function (med) { return '<svg viewBox="0 0 250 95" class="lb2-svg"><line class="rayo" x1="10" y1="70" x2="240" y2="70"/>' + [0, 2, 4, 6, 8, 10].map(function (k) { return '<text x="' + (15 + k * 22) + '" y="88">' + k + '</text>'; }).join('') + (med ? '<line class="graf" x1="' + (15 + S.media * 22) + '" y1="5" x2="' + (15 + S.media * 22) + '" y2="72"/>' : '') + pts + '</svg>'; };
      return [{ vis: sv(0), txt: 'Los 6 datos sobre la recta. Ordenados: ' + S.s.join(', ') + '.' },
        { vis: sv(1) + '<p class="lb-nota">Media = ' + suma + ' ÷ 6 = ' + fmt(r2(S.media)) + '</p>', txt: '<b>Media</b>: sumamos todos y dividimos por la cantidad.' },
        { vis: sv(1) + '<p class="lb-nota">Mediana = ' + fmt(S.med) + '</p>', txt: '<b>Mediana</b>: el valor del medio de los datos ordenados (con 6 datos, el promedio de los dos del medio).' },
        { vis: sv(1) + '<p class="lb-cn-res">Media ' + fmt(r2(S.media)) + ' · Mediana ' + fmt(S.med) + ' · Moda ' + (S.moda.length ? S.moda.join(' y ') : 'no hay') + '</p>', txt: '<b>Moda</b>: el que más se repite. Probá llevar un dato a 0: la media se mueve mucho más que la mediana.' }]; });
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
  M.urna = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('r', 'Bolitas rojas', 0, 8, 1, 3) + ctrl('a', 'Bolitas azules', 0, 8, 1, 2) + ctrl('v', 'Bolitas verdes', 0, 8, 1, 5), function (o) { var t = o.r + o.a + o.v; if (!t) return '<p class="lb-ayuda">Poné al menos una bolita.</p>';
      var bol = '', cols = [['r', '#253638', 'roja'], ['a', '#087E83', 'azul'], ['v', '#7FD3C4', 'verde']]; cols.forEach(function (q) { for (var i = 0; i < o[q[0]]; i++) bol += '<i style="background:' + q[1] + '"></i>'; });
      var urna = '<div class="lb2-urna">' + bol + '</div>', P = [{ vis: urna, txt: 'En la urna hay <b>' + t + '</b> bolitas: esos son los <b>casos posibles</b>.' }];
      cols.forEach(function (q) { var k = o[q[0]]; P.push({ vis: urna + '<p class="lb-cn-res">P(' + q[2] + ') = ' + k + '/' + t + (mcd(k, t) > 1 && k ? ' = ' + frs(k, t) : '') + ' = ' + fmt(r2(k / t * 100)) + ' %</p>', txt: 'Hay <b>' + k + '</b> ' + q[2] + (k === 1 ? '' : 's') + ': casos favorables ÷ casos posibles.' }); });
      P.push({ vis: urna + '<p class="lb-nota">' + o.r + '/' + t + ' + ' + o.a + '/' + t + ' + ' + o.v + '/' + t + ' = 1</p>', txt: 'Las tres probabilidades suman 1 (el 100 %).' });
      return P; },
      '<div class="lb-pie"><button type="button" class="lb-btn suave" data-sim="1">Sacar 100 veces (con reposición)</button></div><div class="lb2-sim"></div>');
    el.addEventListener('click', function (e) { if (!e.target.closest('[data-sim]')) return; var g = function (k) { return num(el.querySelector('[data-k="' + k + '"]').value); }, r = g('r'), a = g('a'), v = g('v'), t = r + a + v, c = [0, 0, 0]; if (!t) return;
      for (var i = 0; i < 100; i++) { var x = Math.random() * t; c[x < r ? 0 : x < r + a ? 1 : 2]++; }
      el.querySelector('.lb2-sim').innerHTML = '<p class="lb-nota">Salieron: roja ' + c[0] + ', azul ' + c[1] + ', verde ' + c[2] + ' de 100. Con muchas repeticiones, la frecuencia se acerca a la probabilidad.</p>'; });
  } };
  M.probabilidad = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { if (Math.random() < .4) { var ev = pick([['un número par', 3], ['un número mayor que 4', 2], ['un múltiplo de 3', 2], ['un número menor que 3', 2], ['un 6', 1]]);
        return { cons: 'Tirás un dado. ¿Cuál es la probabilidad de sacar <b>' + ev[0] + '</b>? (Fracción.)', campos: [{ tipo: 'frac', v: ev[1] / 6, n: ev[1], d: 6 }], ayuda: 'Casos posibles: 6. Contá los favorables.', bien: '¡Bien! ' + ev[1] + '/6' + (mcd(ev[1], 6) > 1 ? ' = ' + frs(ev[1], 6) : '') + '.' }; }
      var r = R(1, 7), a = R(1, 7), v = R(1, 7), t = r + a + v, q = pick([['roja', r], ['azul', a], ['verde', v]]);
      return { cons: 'En una bolsa hay <b>' + r + ' rojas, ' + a + ' azules y ' + v + ' verdes</b>. Sacás una sin mirar. ¿Cuál es la probabilidad de que sea <b>' + q[0] + '</b>? (Fracción.)', campos: [{ tipo: 'frac', v: q[1] / t, n: q[1], d: t }], ayuda: 'Favorables: las ' + q[0] + 's (' + q[1] + '). Posibles: todas (' + t + ').', bien: '¡Bien! ' + q[1] + '/' + t + '.' }; });
  } };
  M.combinaciones_tabla = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'Remeras', 1, 5, 1, 3) + ctrl('b', 'Gorras', 1, 5, 1, 2), function (o) { var R1 = ['Roja', 'Azul', 'Verde', 'Negra', 'Blanca'], G = ['🧢A', '🧢B', '🧢C', '🧢D', '🧢E'];
      var tab = function (filas) { return '<table class="lb2-tab"><tr><th></th>' + G.slice(0, o.b).map(function (g) { return '<th>' + g + '</th>'; }).join('') + '</tr>' + R1.slice(0, o.a).map(function (r, i) { return '<tr><th>' + r + '</th>' + G.slice(0, o.b).map(function () { return '<td class="' + (i < filas ? 'on' : '') + '">' + (i < filas ? '✔' : '') + '</td>'; }).join('') + '</tr>'; }).join('') + '</table>'; };
      var P = [{ vis: tab(0), txt: 'Una tabla: las remeras en las filas y las gorras en las columnas.' }];
      for (var i = 0; i < o.a; i++) P.push({ vis: tab(i + 1), txt: 'La remera ' + R1[i].toLowerCase() + ' va con cada gorra: <b>' + o.b + '</b> combinaciones.' });
      P.push({ vis: tab(o.a) + '<p class="lb-cn-res">' + o.a + ' × ' + o.b + ' = ' + o.a * o.b + ' combinaciones</p>', txt: 'Cada casilla es una combinación: filas × columnas.' });
      return P; });
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
  M.fraccion_cantidad = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('t', 'Total', 12, 120, 12, 60) + ctrl('a', 'Primero uso', 1, 3, 1, 1) + ctrl('b', 'de', 2, 6, 1, 3) + ctrl('c', 'Después uso', 1, 3, 1, 1) + ctrl('d', 'del resto, de', 2, 6, 1, 4), function (o) {
      var a = Math.min(o.a, o.b - 1), c = Math.min(o.c, o.d - 1), u1 = o.t * a / o.b, resto = o.t - u1, u2 = resto * c / o.d, fin = resto - u2;
      var barra = function (k) { return '<div class="lb2-barra3"><i style="width:' + (k >= 1 ? u1 / o.t * 100 : 0) + '%" class="x1"></i><i style="width:' + (k >= 2 ? u2 / o.t * 100 : 0) + '%" class="x2"></i><i style="width:' + (k >= 2 ? fin / o.t * 100 : (k >= 1 ? resto / o.t * 100 : 100)) + '%" class="x3"></i></div>'; };
      return [{ vis: barra(0), txt: 'El total es <b>' + o.t + '</b>.' },
        { vis: barra(1), txt: 'Primero uso ' + fr(a, o.b) + ' del total: ' + o.t + ' × ' + a + ' ÷ ' + o.b + ' = <b>' + fmt(r2(u1)) + '</b>. Queda <b>' + fmt(r2(resto)) + '</b>.' },
        { vis: barra(2), txt: 'Después uso ' + fr(c, o.d) + ' <b>del resto</b> (no del total): ' + fmt(r2(resto)) + ' × ' + c + ' ÷ ' + o.d + ' = <b>' + fmt(r2(u2)) + '</b>.' },
        { vis: barra(2) + '<p class="lb-cn-res">Queda ' + fmt(r2(fin)) + ' de ' + o.t + '</p>', txt: 'Restamos lo usado: ' + fmt(r2(resto)) + ' − ' + fmt(r2(u2)) + '.' }]; });
  } };
  M.fraccion_cantidad_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var b = pick([2, 3, 4, 5]), d = pick([2, 3, 4]), a = R(1, b - 1), c = R(1, d - 1), t = b * d * R(2, 10), u1 = t * a / b, rest = t - u1, u2 = rest * c / d;
      return { cons: 'De <b>' + t + '</b> se usa ' + fr(a, b) + ' el lunes y ' + fr(c, d) + ' <b>del resto</b> el martes. ¿Cuánto queda?', campos: [{ v: rest - u2 }], ayuda: 'Lunes: ' + fr(a, b) + ' de ' + t + ' = ' + u1 + '; queda ' + rest + '. Martes: ' + fr(c, d) + ' de ' + rest + ' = ' + u2 + '.', bien: '¡Bien! Quedan ' + (rest - u2) + '.' }; });
  } };
  M.escala = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('n', 'Escala 1 :', 1000, 100000, 1000, 50000) + ctrl('m', 'Medida en el mapa (cm)', 1, 20, 1, 6), function (o) { var real = o.n * o.m, mapa = '<div class="lb2-mapa"><i style="width:' + o.m * 4.5 + '%"></i><span>' + o.m + ' cm</span></div>';
      return [{ vis: mapa, txt: 'En el mapa mide <b>' + o.m + ' cm</b>.' },
        { vis: mapa, txt: 'Escala 1 : ' + fmt(o.n) + ': cada 1 cm del mapa son <b>' + fmt(o.n) + ' cm</b> reales.' },
        { vis: mapa + '<p class="lb-nota">' + o.m + ' × ' + fmt(o.n) + ' = ' + fmt(real) + ' cm</p>', txt: 'Del mapa a la realidad se <b>multiplica</b> por la escala.' },
        { vis: mapa + '<p class="lb-cn-res">' + fmt(real) + ' cm = ' + fmt(real / 100) + ' m = ' + fmt(real / 100000) + ' km</p>', txt: 'Pasamos a metros (÷ 100) y a kilómetros (÷ 100.000).' }]; });
  } };
  M.escala_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var n = pick([10000, 20000, 25000, 50000, 100000]), m = R(2, 15), km = n * m / 100000;
      if (Math.random() < .5) return { cons: 'En un mapa de escala <b>1 : ' + fmt(n) + '</b>, dos pueblos están a <b>' + m + ' cm</b>. ¿A cuántos <b>km</b> están en la realidad?', campos: [{ v: km, un: 'km' }], ayuda: m + ' × ' + fmt(n) + ' = ' + fmt(n * m) + ' cm; para pasar a km dividí por 100.000.', bien: '¡Bien! ' + fmt(km) + ' km.' };
      return { cons: 'Con escala <b>1 : ' + fmt(n) + '</b>, ¿cuántos <b>cm</b> mide en el mapa una distancia real de <b>' + fmt(km) + ' km</b>?', campos: [{ v: m, un: 'cm' }], ayuda: 'Pasá ' + fmt(km) + ' km a cm (× 100.000) y dividí por ' + fmt(n) + '.', bien: '¡Bien! ' + m + ' cm.' }; });
  } };
  M.velocidad = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('d', 'Distancia (km)', 10, 600, 10, 240) + ctrl('t', 'Tiempo (h)', 1, 10, 1, 3), function (o) { var v = o.d / o.t, ruta = '<div class="lb2-ruta"><span style="left:' + Math.min(92, o.d / 6.5) + '%">🚗</span></div>';
      return [{ vis: ruta, txt: 'Recorre <b>' + o.d + ' km</b> en <b>' + o.t + ' h</b>.' },
        { vis: ruta + '<p class="lb-nota">v = distancia ÷ tiempo</p>', txt: 'La velocidad dice cuántos km recorre en cada hora.' },
        { vis: ruta + '<p class="lb-cn-res">v = ' + o.d + ' ÷ ' + o.t + ' = ' + fmt(r2(v)) + ' km/h</p>', txt: 'Dividimos.' },
        { vis: ruta + '<p class="lb-cn-res">' + fmt(r2(v)) + ' km/h ≈ ' + fmt(r2(v / 3.6)) + ' m/s</p>', txt: 'Para pasar de km/h a m/s se divide por 3,6. Despejando: d = v · t y t = d ÷ v.' }]; });
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
  M.monomio = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('k', 'Coeficiente', -9, 9, 1, 5) + ctrl('e', 'Exponente de x', 0, 5, 1, 2) + ctrl('f', 'Exponente de y', 0, 3, 1, 1), function (o) { var lit = (o.e ? 'x' + (o.e > 1 ? '<sup>' + o.e + '</sup>' : '') : '') + (o.f ? 'y' + (o.f > 1 ? '<sup>' + o.f + '</sup>' : '') : ''), k = String(o.k).replace('-', '−');
      var m = function (hk, hl) { return '<p class="lb-res" style="font-size:1.8rem"><span class="' + (hk ? 'lb2-on' : '') + '">' + k + '</span><span class="' + (hl ? 'lb2-on' : '') + '">' + lit + '</span></p>'; };
      return [{ vis: m(0, 0), txt: 'Un monomio: un número multiplicado por letras.' },
        { vis: m(1, 0), txt: 'El <b>coeficiente</b> es el número: <b>' + k + '</b>.' },
        { vis: m(0, 1), txt: 'La <b>parte literal</b> son las letras con sus exponentes: ' + (lit || '(no tiene)') + '.' },
        { vis: m(0, 1) + '<p class="lb-cn-res">Grado = ' + o.e + ' + ' + o.f + ' = ' + (o.e + o.f) + '</p>', txt: 'El <b>grado</b> es la suma de los exponentes de las letras.' }]; });
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
  M.distributiva = { tipo: 'ejemplo', pasos: true, render: function (el) {
    escena(el, ctrl('a', 'a', 1, 6, 1, 3) + ctrl('b', 'b', 1, 6, 1, 2), function (o) { var a = o.a, b = o.b, X = 70, s = 14;
      var sv = function (k) { var rect = function (x, y, w, h, c, show) { return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" class="' + (show ? c : 'c0') + '" style="' + (show ? '' : 'opacity:.25') + '"/>'; };
        return '<svg viewBox="0 0 ' + (X + b * s + 40) + ' ' + (X + a * s + 40) + '" class="lb2-svg" style="max-width:240px">' + rect(20, 20, X, X, 'c2', k >= 2) + rect(20 + X, 20, b * s, X, 'c1', k >= 3) + rect(20, 20 + X, X, a * s, 'c1', k >= 4) + rect(20 + X, 20 + X, b * s, a * s, 'c2', k >= 5) +
        '<text x="' + (20 + X / 2) + '" y="14">x</text><text x="' + (20 + X + b * s / 2) + '" y="14">' + b + '</text><text x="10" y="' + (24 + X / 2) + '">x</text><text x="10" y="' + (24 + X + a * s / 2) + '">' + a + '</text></svg>'; };
      return [{ vis: sv(1), txt: 'Un rectángulo de lados <b>(x + ' + a + ')</b> y <b>(x + ' + b + ')</b>: su área es (x + ' + a + ')(x + ' + b + ').' },
        { vis: sv(2), txt: 'Lo partimos en 4. El primero: x · x = <b>x²</b>.' },
        { vis: sv(3), txt: 'x · ' + b + ' = <b>' + b + 'x</b>.' },
        { vis: sv(4), txt: a + ' · x = <b>' + a + 'x</b>.' },
        { vis: sv(5), txt: a + ' · ' + b + ' = <b>' + a * b + '</b>.' },
        { vis: sv(5) + '<p class="lb-cn-res">(x + ' + a + ')(x + ' + b + ') = x² + ' + (a + b) + 'x + ' + a * b + '</p>', txt: 'Sumamos las 4 partes y juntamos las x: cada término de un paréntesis multiplica a cada término del otro.' }]; });
  } };
  M.distributiva_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = R(-6, 7) || 2, b = R(-6, 7) || 3, sa = a < 0 ? '− ' + -a : '+ ' + a, sb = b < 0 ? '− ' + -b : '+ ' + b;
      return { cons: 'Aplicá la distributiva: <b>(x ' + sa + ')(x ' + sb + ')</b>. Escribí los coeficientes del resultado.', campos: [{ lab: 'x²:', v: 1 }, { lab: 'x:', v: a + b }, { lab: 'número:', v: a * b }], ayuda: 'x · x = x²; x · (' + b + ') + (' + a + ') · x = ' + (a + b) + 'x; (' + a + ') · (' + b + ') = ' + a * b + '.', bien: '¡Bien! x² ' + (a + b < 0 ? '− ' + -(a + b) : '+ ' + (a + b)) + 'x ' + (a * b < 0 ? '− ' + -(a * b) : '+ ' + a * b) + '.' }; });
  } };
  M.ecuacion_denominadores = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var a = pick([2, 3, 4, 5]), b = pick([2, 3, 4, 6].filter(function (x) { return x !== a; })), m = a * b / mcd(a, b), x = m * R(1, 4) * pick([1, -1]), c = x / a + x / b;
      return { cons: 'Resolvé: <b>x/' + a + ' + x/' + b + ' = ' + fmt(c) + '</b>', campos: [{ lab: 'x =', v: x }], ayuda: 'Multiplicá los dos miembros por el mcm de ' + a + ' y ' + b + ' (' + m + ') para sacar los denominadores: ' + m / a + 'x + ' + m / b + 'x = ' + fmt(c * m) + '.', bien: '¡Bien! x = ' + x + '.' }; });
  } };

  // ======= PRIMER GRADO (Nivel Medio · Matemática 1, Misiones 1 y 2): contar, comparar, uno con uno, igualar, números hasta 20 =======
  // Todo en IMPRENTA MAYÚSCULA, con dibujos (emojis) grandes y números chicos. Un ejemplo paso a paso (primeros) y una práctica (primeros_x), con un modo por tema.
  var P1E = { manzana: '🍎', globo: '🎈', estrella: '⭐', caramelo: '🍬', pelota: '⚽', flor: '🌸', patito: '🐤', chico: '🧒', vaso: '🥤', perro: '🐶', hueso: '🦴', gato: '🐱', pescado: '🐟', silla: '🪑', tortita: '🧁', palito: '<i class="lb-p1-pal"></i>' };
  var P1PL = { manzana: 'MANZANAS', globo: 'GLOBOS', estrella: 'ESTRELLAS', caramelo: 'CARAMELOS', pelota: 'PELOTAS', flor: 'FLORES', patito: 'PATITOS', chico: 'CHICOS', vaso: 'VASOS', perro: 'PERROS', hueso: 'HUESOS', gato: 'GATOS', pescado: 'PESCADOS', silla: 'SILLAS', tortita: 'TORTITAS', palito: 'PALITOS' };
  var P1PARES = [['chico', 'vaso'], ['perro', 'hueso'], ['gato', 'pescado'], ['chico', 'silla'], ['chico', 'tortita']];
  var P1NOM = [['ANA', 'LEO'], ['SOFI', 'JUAN'], ['MICA', 'TOMI']];
  var P1M = { caramelo: 1, globo: 1, patito: 1, perro: 1, hueso: 1, gato: 1, pescado: 1, vaso: 1, chico: 1, palito: 1 };
  function g(o, fem, masc) { return P1M[o] ? masc : fem; }
  function p1Obj() { return pick(['manzana', 'globo', 'estrella', 'caramelo', 'pelota', 'flor', 'patito']); }
  function p1Up(n) { return H.letras(n).toUpperCase(); }
  // una fila de objetos: hasta = cuántos llevan número; marca = posición resaltada; tenue = desde qué posición se ven apagados
  function p1Fila(n, o, op) {
    op = op || {}; var h = '';
    for (var i = 0; i < n; i++) {
      var cls = 'lb-p1-o' + (op.marca === i + 1 ? ' on' : '') + (op.tenue != null && i >= op.tenue ? ' tenue' : '') + (op.nuevo != null && i >= op.nuevo ? ' nuevo' : '');
      h += '<span class="' + cls + '">' + P1E[o] + (op.hasta && i < op.hasta ? '<small>' + (i + 1) + '</small>' : '') + '</span>';
    }
    return '<div class="lb-p1-fila">' + (h || '<span class="lb-p1-vac">—</span>') + '</div>';
  }
  function p1Grupo(nom, n, o, op) { return '<div class="lb-p1-g"><b>' + nom + '</b>' + p1Fila(n, o, op) + '</div>'; }
  function p1Big(t) { return '<p class="lb-p1-big">' + t + '</p>'; }
  // parejas uno con uno: columnas con un objeto arriba y uno abajo; unidas = cuántas columnas ya están unidas
  function p1Parejas(a, oa, b, ob, unidas, marcarSobra) {
    var m = Math.max(a, b), h = '';
    for (var i = 0; i < m; i++) {
      var par = i < Math.min(a, b) && i < unidas, sobra = marcarSobra && i >= Math.min(a, b);
      h += '<div class="lb-p1-col' + (par ? ' par' : '') + (sobra ? ' sobra' : '') + '"><span>' + (i < a ? P1E[oa] : '') + '</span><i>' + (par ? '|' : '') + '</i><span>' + (i < b ? P1E[ob] : '') + '</span></div>';
    }
    return '<div class="lb-p1-pares">' + h + '</div>';
  }
  // tren de vagones con números
  function p1Tren(desde, hasta, op) {
    op = op || {}; var h = '';
    for (var k = desde; k <= hasta; k++) {
      var c = op[k] || '';
      h += '<span class="lb-p1-vag ' + c + '">' + (c === 'oculto' ? '?' : k) + '</span>';
    }
    return '<div class="lb-p1-tren"><span class="lb-p1-loco">🚂</span>' + h + '</div>';
  }
  // recta del 0 al 20 con marcas
  function p1Recta(marcas) {
    var h = '';
    for (var k = 0; k <= 20; k++) { var m = marcas[k]; h += '<span class="lb-p1-rc' + (m ? ' ' + m.c : '') + '"><i></i><b>' + k + '</b>' + (m && m.t ? '<em>' + m.t + '</em>' : '') + '</span>'; }
    return '<div class="lb-p1-rw"><div class="lb-p1-recta">' + h + '</div></div>';
  }
  // caja de 10 llena + sueltos
  function p1Caja(o, sueltos, op) {
    op = op || {}; var c = ''; for (var i = 0; i < 10; i++) c += '<span>' + P1E[o] + '</span>';
    var s = ''; for (var j = 0; j < sueltos; j++) s += '<span class="lb-p1-o' + (op.cuenta && j < op.cuenta ? ' on' : '') + '">' + P1E[o] + (op.cuenta && j < op.cuenta ? '<small>' + (11 + j) + '</small>' : '') + '</span>';
    return '<div class="lb-p1-dz"><div class="lb-p1-caja' + (op.caja ? ' on' : '') + '">' + c + '<small>10</small></div><div class="lb-p1-fila">' + s + '</div></div>';
  }
  // cuadro de números desde el 0, de a 10 por fila (los redondos quedan en el margen izquierdo). cls = {número: clase}; ver = hasta qué número se ve
  function p1Cuadro(hasta, cls, ver) {
    cls = cls || {}; var h = '', tope = ver == null ? hasta : ver;
    for (var k = 0; k <= hasta; k++) { var c = k > tope ? 'vac' : (cls[k] || ''); h += '<span class="' + c + '">' + (c === 'vac' ? '' : c.indexOf('oculto') >= 0 ? '?' : k) + '</span>'; }
    return '<div class="lb-p1-cua">' + h + '</div>';
  }
  function p1Marca(lista, c, o) { o = o || {}; lista.forEach(function (k) { o[k] = c; }); return o; }
  function p1Fil(n) { var a = Math.floor(n / 10) * 10, r = []; for (var k = a; k <= a + 9; k++) r.push(k); return r; }
  function p1Col(n, hasta) { var r = []; for (var k = n % 10; k <= hasta; k += 10) r.push(k); return r; }
  // bolsitas de 10 (decenas) y sueltos (unidades); op.bc = bolsitas contadas, op.sc = sueltos contados
  function p1Bolsas(n, op) {
    op = op || {}; var d = Math.floor(n / 10), u = n % 10, h = '', i;
    for (i = 0; i < d; i++) h += '<span class="lb-p1-o' + (op.bc > i ? ' on' : '') + '">🛍️' + (op.bc > i ? '<small>' + (10 * (i + 1)) + '</small>' : '<small>10</small>') + '</span>';
    var t = ''; for (i = 0; i < u; i++) t += '<span class="lb-p1-o' + (op.sc > i ? ' on' : '') + '">🍬' + (op.sc > i ? '<small>' + (10 * d + i + 1) + '</small>' : '') + '</span>';
    return '<div class="lb-p1-dz"><div class="lb-p1-fila">' + (h || '<span class="lb-p1-vac">—</span>') + '</div><div class="lb-p1-fila">' + (t || '<span class="lb-p1-vac">SIN SUELTOS</span>') + '</div></div>';
  }
  function p1DU(n, hl) { var d = Math.floor(n / 10), u = n % 10; return '<div class="lb-p1-du"><span class="' + (hl === 'd' || hl === 'du' ? 'on' : '') + '"><small>DECENAS</small><b>' + d + '</b></span><span class="' + (hl === 'u' || hl === 'du' ? 'on' : '') + '"><small>UNIDADES</small><b>' + u + '</b></span></div>'; }
  // recta del 0 al 100 con los redondos; marcas = [[número, clase, texto]]
  function p1R100(marcas) {
    var h = '', k; for (k = 0; k <= 100; k += 10) h += '<span class="lb-p1-t" style="left:' + k + '%"><i></i><b>' + k + '</b></span>';
    (marcas || []).forEach(function (m) { h += '<span class="lb-p1-m ' + (m[1] || '') + '" style="left:' + m[0] + '%">' + (m[2] != null ? m[2] : m[0]) + '</span>'; });
    return '<div class="lb-p1-r100w"><div class="lb-p1-r100">' + h + '</div></div>';
  }
  // dinero: lista de valores (billetes de 10 o 20, monedas de 1 o 5); hasta = cuántos ya contados (con el total que va)
  function p1Plata(vals, hasta) {
    var t = 0; return '<div class="lb-p1-fila">' + vals.map(function (v, i) { t += v; var c = i < (hasta || 0);
      return '<span class="lb-p1-pl ' + (v >= 10 ? 'bi' : 'mo') + (c ? ' on' : '') + '">' + (v >= 10 ? '💵' : '🪙') + '<b>$' + v + '</b>' + (c ? '<small>' + t + '</small>' : '') + '</span>'; }).join('') + '</div>';
  }
  function p1Desarmar(n) { var r = []; while (n >= 10) { r.push(10); n -= 10; } if (n >= 5) { r.push(5); n -= 5; } while (n > 0) { r.push(1); n--; } return r; }
  // cuadro de 10 (dos filas de 5): a casilleros de un color, b de otro, el resto vacíos; nb = cuántos de b ya se ven
  function p1Diez(a, b, nb) { var h = ''; nb = nb == null ? b : nb; for (var i = 0; i < 10; i++) h += '<span class="' + (i < a ? 'c1' : i < a + nb ? 'c2' : '') + '">' + (i < a ? '🔴' : i < a + nb ? '🔵' : '') + '</span>'; return '<div class="lb-p1-diez">' + h + '</div>'; }
  var P1DADO = ['', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];
  // fila de bolsitas de 10: n bolsitas; desde 'tenue' en adelante se ven apagadas; 'nuevo' desde dónde son nuevas
  function p1BolsasN(n, op) { op = op || {}; var h = ''; for (var i = 0; i < n; i++) h += '<span class="lb-p1-o' + (op.tenue != null && i >= op.tenue ? ' tenue' : '') + (op.nuevo != null && i >= op.nuevo ? ' nuevo' : '') + '">🛍️<small>10</small></span>'; return '<div class="lb-p1-fila">' + (h || '<span class="lb-p1-vac">—</span>') + '</div>'; }
  // problemas: arma la historia, la pregunta, la cuenta y el dibujo según el tipo
  function p1Hist(t, a, b, nm, o, esc) {
    if (esc > 1) { a *= esc; b *= esc; }
    if (t === 'dospasos') { var c = Math.max(esc || 1, Math.round((a + b) * 0.6 / (esc || 1)) * (esc || 1)), Pl = P1PL[o]; return { h: 'HABÍA <b>' + a + '</b> ' + Pl + '. LLEGARON <b>' + b + '</b> MÁS Y DESPUÉS SE VENDIERON <b>' + c + '</b>.', q: '¿' + g(o, 'CUÁNTAS', 'CUÁNTOS') + ' QUEDAN?', op: '+', w: 'DOS PASOS: PRIMERO SUMAMOS Y DESPUÉS RESTAMOS', r: a + b - c, c: a + ' + ' + b + ' = ' + (a + b) + ' · ' + (a + b) + ' − ' + c + ' = ' + (a + b - c), v: p1Big('1) ' + a + ' + ' + b + ' = ' + (a + b)) + p1Big('2) ' + (a + b) + ' − ' + c + ' = ' + (a + b - c)) }; }
    var P = P1PL[o], H = {}, CU = g(o, 'CUÁNTAS', 'CUÁNTOS');
    if (t === 'completar' || t === 'falta_resta' || t === 'quitar' || t === 'comparar') { if (b > a && t !== 'completar') { var x = a; a = b; b = x; } if (t === 'completar' && b <= a) b = a + 2; if (a === b) a = b + 1; }
    if (t === 'juntar') H = { h: nm[0] + ' TIENE <b>' + a + '</b> ' + P + ' Y ' + nm[1] + ' TIENE <b>' + b + '</b>.', q: '¿' + CU + ' TIENEN ENTRE LOS DOS?', op: '+', w: 'SE JUNTAN', r: a + b, c: a + ' + ' + b + ' = ' + (a + b), v: p1Grupo(nm[0], a, o) + p1Grupo(nm[1], b, o) };
    else if (t === 'agregar') H = { h: 'HAY <b>' + a + '</b> ' + P + '. LLEGAN <b>' + b + '</b> MÁS.', q: '¿' + CU + ' HAY AHORA?', op: '+', w: 'LLEGAN MÁS', r: a + b, c: a + ' + ' + b + ' = ' + (a + b), v: p1Fila(a + b, o, { nuevo: a }) };
    else if (t === 'avanzar') { var op1 = {}; op1[a] = 'on'; op1[a + b] = 'sig'; H = { h: nm[0] + ' ESTÁ EN EL CASILLERO <b>' + a + '</b> Y AVANZA <b>' + b + '</b>.', q: '¿EN QUÉ CASILLERO QUEDA?', op: '+', w: 'AVANZA', r: a + b, c: a + ' + ' + b + ' = ' + (a + b), v: p1Tren(a, a + b, op1) }; }
    else if (t === 'completar') H = { h: nm[0] + ' TIENE <b>' + a + '</b> ' + P + ' Y QUIERE TENER <b>' + b + '</b>.', q: '¿' + CU + ' LE FALTAN?', op: '+', w: 'COMPLETA', r: b - a, c: a + ' + ' + (b - a) + ' = ' + b, v: p1Fila(b, o, { tenue: a }) };
    else if (t === 'quitar') H = { h: 'HAY <b>' + a + '</b> ' + P + '. SE PIERDEN <b>' + b + '</b>.', q: '¿' + CU + ' QUEDAN?', op: '−', w: 'SE VAN', r: a - b, c: a + ' − ' + b + ' = ' + (a - b), v: p1Fila(a, o, { tenue: a - b }) };
    else if (t === 'comparar') H = { h: nm[0] + ' TIENE <b>' + a + '</b> ' + P + ' Y ' + nm[1] + ' TIENE <b>' + b + '</b>.', q: '¿' + CU + ' MÁS TIENE ' + nm[0] + '?', op: '−', w: 'COMPARAMOS', r: a - b, c: a + ' − ' + b + ' = ' + (a - b), v: p1Grupo(nm[0], a, o) + p1Grupo(nm[1], b, o) };
    else H = { h: 'SE NECESITAN <b>' + a + '</b> ' + P + '. HAY <b>' + b + '</b>.', q: '¿' + CU + ' FALTAN?', op: '−', w: 'NECESITO MÁS DE LO QUE HAY', r: a - b, c: a + ' − ' + b + ' = ' + (a - b), v: p1Fila(a, o, { tenue: b }) };
    if (esc > 1) H.v = '<div class="lb-p1-dos"><div class="lb-p1-pre">' + P1E[o] + '<b>' + a + '</b></div><div class="lb-p1-pre">' + P1E[o] + '<b>' + b + '</b></div></div>';
    return H;
  }
  // arreglo rectangular: f filas y c columnas; hl = 'f' + número de fila o 'c' + número de columna marcada, o 'todo'; hasta = cuántas filas ya contadas
  function p1Arr(f, c, o, op) {
    op = op || {}; var h = '', i, j;
    for (i = 0; i < f; i++) { h += '<div class="lb-p1-arf' + (op.fila === i ? ' on' : '') + '">'; for (j = 0; j < c; j++) h += '<span class="' + (op.col === j ? 'on' : '') + (op.hasta != null && i < op.hasta ? ' ya' : '') + '">' + P1E[o] + '</span>'; h += (op.hasta != null && i < op.hasta ? '<small>' + c * (i + 1) + '</small>' : '') + '</div>'; }
    return '<div class="lb-p1-arr">' + h + '</div>';
  }
  // calculadora: pantalla + teclas; hl = tecla o lista de teclas marcadas ('pan' marca la pantalla)
  function p1Calc(pan, hl) { hl = [].concat(hl || []); var K = ['7', '8', '9', 'C', '4', '5', '6', '+', '1', '2', '3', '−', '0', '=']; return '<div class="lb-p1-calc"><div class="lb-p1-pan' + (hl.indexOf('pan') >= 0 ? ' on' : '') + '">' + pan + '</div><div class="lb-p1-tec">' + K.map(function (k) { return '<span class="' + (hl.indexOf(k) >= 0 ? 'on' : '') + ('+−=C'.indexOf(k) >= 0 ? ' sg' : '') + (k === '0' ? ' cero' : '') + '">' + k + '</span>'; }).join('') + '</div></div>'; }
  // cajas de 100, paquetes de 10 y sueltos; op.c/op.d/op.u = cuántos de cada uno ya se contaron (con el total que va)
  function p1CDU(n, op) {
    op = op || {}; var mi = Math.floor(n / 1000), c = Math.floor(n / 100) % 10, d = Math.floor(n / 10) % 10, u = n % 10, h = '', i, t = 0;
    var it = function (e, val, k, lab) { var on = op[k] != null && op[k] > 0; if (on) { op[k]--; t += val; } return '<span class="lb-p1-o' + (on ? ' on' : '') + '">' + e + (on || lab ? '<small>' + (on ? t : lab) + '</small>' : '') + '</span>'; };
    var fm = '', fc = '', fd = '', fu = '';
    for (i = 0; i < mi; i++) fm += it('🚚', 1000, 'm', '1.000');
    for (i = 0; i < c; i++) fc += it('🗃️', 100, 'c', '100'); for (i = 0; i < d; i++) fd += it('📦', 10, 'd', '10'); for (i = 0; i < u; i++) fu += it('🍪', 1, 'u', '');
    return '<div class="lb-p1-dz lb-p1-cdu">' + (fm ? '<div class="lb-p1-fila">' + fm + '</div>' : '') + (fc ? '<div class="lb-p1-fila">' + fc + '</div>' : '') + (fd ? '<div class="lb-p1-fila">' + fd + '</div>' : '') + (fu ? '<div class="lb-p1-fila">' + fu + '</div>' : '') + '</div>';
  }
  function p1CDUt(n, hl) { var s = String(n), L = ['MILES', 'CENTENAS', 'DECENAS', 'UNIDADES'].slice(4 - s.length); return '<div class="lb-p1-du">' + s.split('').map(function (d, i) { return '<span class="' + (hl === 9 || hl === i ? 'on' : '') + '"><small>' + L[i] + '</small><b>' + d + '</b></span>'; }).join('') + '</div>'; }
  // recta del 0 al 1.000 de 100 en 100; marcas = [[número, clase, texto]]
  function p1R1000(marcas) {
    var h = '', k; for (k = 0; k <= 1000; k += 100) h += '<span class="lb-p1-t" style="left:' + k / 10 + '%"><i></i><b>' + (k === 1000 ? '1.000' : k) + '</b></span>';
    (marcas || []).forEach(function (m) { h += '<span class="lb-p1-m ' + (m[1] || '') + '" style="left:' + m[0] / 10 + '%">' + (m[2] != null ? m[2] : m[0]) + '</span>'; });
    return '<div class="lb-p1-r100w"><div class="lb-p1-r100">' + h + '</div></div>';
  }
  // recta del 0 al 10.000 de 1.000 en 1.000; marcas = [[número, clase, texto]]
  function p1R10000(marcas) {
    var h = '', k; for (k = 0; k <= 10000; k += 1000) h += '<span class="lb-p1-t" style="left:' + k / 100 + '%"><i></i><b>' + (k ? k / 1000 + 'M' : 0) + '</b></span>';
    (marcas || []).forEach(function (m) { h += '<span class="lb-p1-m ' + (m[1] || '') + '" style="left:' + m[0] / 100 + '%">' + (m[2] != null ? m[2] : fmt(m[0])) + '</span>'; });
    return '<div class="lb-p1-r100w"><div class="lb-p1-r100">' + h + '</div></div><p class="lb-nota">1M = 1.000</p>';
  }
  // cálculo mental: arma la cuenta según el tipo; devuelve {a, b, r, sg}
  function p1Ment(q, op, a, b, esc) {
    var res = op === 'resta', sg = res ? '−' : '+';
    if (q === 'chica') { if (res && b > a) { var t = a; a = b; b = t; } if (res && a === b) a = Math.min(9, a + 1); if (!res && a + b > 9) b = 9 - a || 1; return { a: a * esc, b: b * esc, r: res ? (a - b) * esc : (a + b) * esc, sg: sg, ca: a, cb: b }; }
    if (q === 'falta100') return { a: res ? 100 : a, b: res ? a : 100 - a, r: 100 - a, sg: sg };
    if (q === 'desarmar') { var ac = Math.floor(a / 100), ad = Math.floor(a / 10) % 10, au = a % 10, bd = Math.floor(b / 10) % 10, bu = b % 10;
      if (res) { bd = Math.min(bd, ad); bu = Math.min(bu, au); } else { bd = Math.min(bd, 9 - ad); bu = Math.min(bu, 9 - au); }
      var B = bd * 10 + bu; return { a: a, b: B, r: res ? a - B : a + B, sg: sg, p: [[ac * 100, 0], [ad * 10, bd * 10], [au, bu]] }; }
    return { a: a, b: b, r: res ? a - b : a + b, sg: sg };
  }
  // cuenta en columnas (3 cifras): arriba, abajo, resultado parcial (desde la derecha), marcas de "me llevo"/canje; col = columna marcada (0 C, 1 D, 2 U)
  function p1Col3(a, b, sg, res, col, llevo) {
    var A = ('   ' + a).slice(-3).split(''), B = ('   ' + b).slice(-3).split(''), Rr = ('   ' + (res || '')).slice(-3).split(''), Lv = llevo || ['', '', ''];
    var fila = function (arr, cl) { return '<tr' + (cl ? ' class="' + cl + '"' : '') + '><td class="sg">' + (cl === 'ab' ? sg : '') + '</td>' + arr.map(function (x, i) { return '<td class="' + (i === col ? 'on' : '') + '">' + (x === ' ' ? '' : x) + '</td>'; }).join('') + '</tr>'; };
    return '<table class="lb-p1-colc"><tr class="lv"><td></td>' + Lv.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr class="hd"><td></td><td>C</td><td>D</td><td>U</td></tr>' + fila(A) + fila(B, 'ab') + fila(Rr, 'rs') + '</table>';
  }
  function p1Cifras(n, hl) { return '<div class="lb-p1-cif">' + String(n).split('').map(function (d, i) { return '<span class="' + (hl === i || hl === 9 ? 'on' : '') + '">' + d + '</span>'; }).join('') + '</div>'; }

  M.primeros = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    var md = p.modo || 'contar', o = p1Obj(), pr = pick(P1PARES), nm = pick(P1NOM), C = {
      contar: ctrl('n', 'CANTIDAD', 1, p.max || 8, 1, R(4, Math.min(7, p.max || 8))),
      cantidad: ctrl('n', 'CANTIDAD', 2, p.max || 8, 1, R(4, Math.min(7, p.max || 8))),
      mas_menos: ctrl('a', nm[0], 1, 9, 1, p.igual ? 4 : 5) + ctrl('b', nm[1], 1, 9, 1, p.igual ? 4 : 2),
      uno_a_uno: ctrl('a', P1PL[pr[0]], 1, 8, 1, 4) + ctrl('b', P1PL[pr[1]], 1, 8, 1, p.igual ? 4 : 6),
      igualar: ctrl('a', 'GRUPO 1', 1, 9, 1, p.op === 'quitar' ? 7 : 5) + ctrl('b', 'GRUPO 2', 1, 9, 1, p.op === 'quitar' ? 4 : 2),
      tren: ctrl('n', 'HASTA EL', (p.desde || 1) + 1, p.hasta || 10, 1, p.hasta || 10),
      decena: ctrl('s', 'SUELTOS', 1, 10, 1, p.ini || 3),
      leer: ctrl('n', 'NÚMERO', 10, 20, 1, pick([12, 15, 17])),
      anterior_siguiente: ctrl('n', 'NÚMERO', p.min || 2, p.max || 19, 1, p.max ? R(p.min || 2, p.max) : pick([9, 14, 17])),
      cuadro: p.que === 'contar' ? ctrl('n', 'HASTA EL', 10, p.hasta || 30, 10, p.hasta || 30) : p.que === 'bajar' ? ctrl('n', 'NÚMERO', 0, (p.hasta || 100) - 10, 1, R(11, 38)) :
        ctrl('n', 'NÚMERO', p.que === 'columna' ? 0 : 10, Math.min(p.hasta || 100, 99), 1, R(12, Math.min(p.hasta || 100, 99) - 2)),
      comparar2: ctrl('a', 'UN NÚMERO', 10, 99, 1, 56) + ctrl('b', 'OTRO NÚMERO', 10, 99, 1, 65),
      ordenar3: ctrl('a', 'PRIMERO', 10, 99, 1, 47) + ctrl('b', 'SEGUNDO', 10, 99, 1, 74) + ctrl('c', 'TERCERO', 10, 99, 1, 40),
      recta100: p.que === 'saltar' ? ctrl('a', 'ESTÁS EN EL', p.dir === 'atras' ? 6 : 0, p.dir === 'atras' ? 20 : 14, 1, p.dir === 'atras' ? 12 : 4) + ctrl('s', 'SALTÁS', 1, 6, 1, 3) : ctrl('n', 'NÚMERO', 1, 99, 1, 46),
      decenas: ctrl('d', 'BOLSITAS DE 10', p.que === 'contar' ? 1 : 1, 9, 1, 3) + ctrl('u', 'SUELTOS', 0, 9, 1, 5),
      dinero: p.que === 'pagar' ? ctrl('n', 'PRECIO', 6, 39, 1, 17) : p.que === 'falta' ? ctrl('n', 'PRECIO', 6, 20, 1, 12) + ctrl('d', 'DAS', 1, 19, 1, 10) : p.que === 'caro' ? ctrl('a', 'PRECIO 1', 1, 50, 1, 20) + ctrl('b', 'PRECIO 2', 1, 50, 1, 8) :
        ctrl('d', 'BILLETES DE $10', 0, 3, 1, 2) + ctrl('c', 'MONEDAS DE $5', 0, 1, 1, 1) + ctrl('u', 'MONEDAS DE $1', 0, 4, 1, 2),
      sumar: ctrl('a', 'PRIMER GRUPO', 1, 7, 1, 4) + ctrl('b', 'SEGUNDO GRUPO', 1, 5, 1, 3),
      restar: ctrl('a', p.que === 'comparar' ? 'CHICOS' : 'HABÍA', 3, 10, 1, 8) + ctrl('b', p.que === 'comparar' ? 'VASOS' : 'SACAMOS', 1, p.que === 'comparar' ? 10 : 9, 1, 3),
      diez: p.que === 'dados' ? ctrl('a', 'UN DADO', 1, 6, 1, 2) + ctrl('b', 'OTRO DADO', 1, 6, 1, 5) : ctrl('a', 'ROJOS', 1, 9, 1, 7),
      dobles: p.que === 'iguales' ? ctrl('a', 'EN CADA GRUPO', 1, 5, 1, 3) + ctrl('k', 'GRUPOS', 2, 3, 1, 3) : ctrl('a', 'NÚMERO', 1, p.que === 'casi' ? 9 : 10, 1, 4),
      decenas_op: p.que === 'atras10' ? ctrl('a', 'DESDE EL', 30, 100, 10, 100) : ctrl('a', 'BOLSITAS', p.que === 'restar' ? 2 : 1, 9, 1, p.que === 'restar' ? 7 : 2) + ctrl('b', p.que === 'restar' ? 'SE VENDEN' : 'LLEGAN', 1, p.que === 'restar' ? 8 : 8, 1, 3),
      problema: ctrl('a', 'PRIMER NÚMERO', 2 * (p.esc || 1), 9 * (p.esc || 1), p.esc || 1, 6 * (p.esc || 1)) + ctrl('b', 'SEGUNDO NÚMERO', p.esc || 1, 9 * (p.esc || 1), p.esc || 1, 3 * (p.esc || 1)),
      calcu: p.que === 'uno_diez' ? ctrl('n', 'NÚMERO', 10, 89, 1, 47) : p.que === 'partes' ? ctrl('n', 'EN LA PANTALLA', 0, 99, 1, 8) : ctrl('a', 'PRIMER NÚMERO', 2, 30, 1, p.que === 'controlar' ? 20 : 9) + ctrl('b', 'SEGUNDO NÚMERO', 1, 9, 1, p.que === 'controlar' ? 3 : 6),
      centenas: ctrl('c', 'CAJAS DE 100', p.min || 1, p.max || 4, 1, 1) + ctrl('d', 'PAQUETES DE 10', 0, 9, 1, 5) + ctrl('u', 'SUELTOS', 0, 9, 1, 3),
      serie: ctrl('a', 'EMPIEZA EN', p.desde || 100, p.hasta || 190, 1, p.desde ? p.desde + 5 : 130),
      valor: ctrl('c', 'CENTENAS', 1, 9, 1, 3) + ctrl('d', 'DECENAS', 0, 9, 1, 6) + ctrl('u', 'UNIDADES', 0, 9, 1, 5),
      comparar3: ctrl('a', 'UN NÚMERO', 100, 999, 1, 645) + ctrl('b', 'OTRO NÚMERO', 100, 999, 1, 654),
      orden3: ctrl('a', 'PRIMERO', 100, 999, 1, 460) + ctrl('b', 'SEGUNDO', 100, 999, 1, 406) + ctrl('c', 'TERCERO', 100, 999, 1, 640),
      recta1000: ctrl('n', 'NÚMERO', 10, 990, 10, 470),
      cambia: ctrl('n', 'NÚMERO', 100, 899, 1, 352),
      dinero2: p.que === 'vuelto' ? ctrl('n', 'PRECIO', 10, 490, 10, 80) : p.que === 'sumar' ? ctrl('a', 'PRECIO 1', 50, 500, 50, 300) + ctrl('b', 'PRECIO 2', 50, 450, 50, 250) : p.que === 'caro' ? ctrl('a', 'PRECIO 1', 100, 990, 10, 540) + ctrl('b', 'PRECIO 2', 100, 990, 10, 450) :
        ctrl('q', 'BILLETES DE $500', 0, 1, 1, 1) + ctrl('d', 'BILLETES DE $200', 0, 2, 1, 1) + ctrl('c', 'BILLETES DE $100', 0, 3, 1, 1) + ctrl('m', 'BILLETES DE $50', 0, 1, 1, 1),
      mental: p.que === 'falta100' ? ctrl('a', 'NÚMERO', 10, 90, 10, 70) : p.que === 'desarmar' ? ctrl('a', 'PRIMER NÚMERO', 110, 489, 1, p.op === 'resta' ? 365 : 234) + ctrl('b', 'SEGUNDO NÚMERO', 11, 59, 1, p.op === 'resta' ? 42 : 52) :
        p.que === 'truco' ? ctrl('a', 'NÚMERO', 110, 889, 1, 472) + ctrl('b', 'SUMO O RESTO', 10, 100, 90, 100) : ctrl('a', 'PRIMER NÚMERO', 1, 9, 1, p.op === 'resta' ? 8 : 3) + ctrl('b', 'SEGUNDO NÚMERO', 1, 9, 1, p.op === 'resta' ? 3 : 4),
      columna: ctrl('a', 'ARRIBA', 100, 899, 1, p.op === 'resta' ? (p.lleva ? 352 : 576) : (p.lleva ? 268 : 231)) + ctrl('b', 'ABAJO', 10, 399, 1, p.op === 'resta' ? (p.lleva ? 128 : 234) : (p.lleva ? 125 : 45)),
      prop: p.que === 'familia' ? ctrl('a', 'PRIMER NÚMERO', 10, 60, 10, 60) + ctrl('b', 'SEGUNDO NÚMERO', 10, 40, 10, 40) : p.que === 'amigos' ? ctrl('a', 'PRIMER NÚMERO', 11, 89, 1, 37) + ctrl('b', 'SEGUNDO NÚMERO', 11, 89, 1, 25) : p.que === 'dobles' ? ctrl('a', 'NÚMERO', 10, 60, 5, 25) : ctrl('a', 'NÚMERO CHICO', 1, 9, 1, 4) + ctrl('b', 'NÚMERO GRANDE', 100, 300, 1, 120),
      mult: p.que === 'arreglo' || p.que === 'girar' ? ctrl('f', 'FILAS', 2, 5, 1, 3) + ctrl('c', 'COLUMNAS', 2, 6, 1, 4) : ctrl('g', 'GRUPOS', 2, 5, 1, 3) + ctrl('n', 'EN CADA GRUPO', 2, 6, 1, 4),
      por10: ctrl('n', 'NÚMERO', 1, p.de === 100 ? 9 : (p.que === 'cifras' ? 45 : 9), 1, p.de === 100 ? 3 : (p.que === 'cifras' ? 24 : 4)),
      comparar4: ctrl('a', 'UN NÚMERO', 1000, 9999, 1, 4735) + ctrl('b', 'OTRO NÚMERO', 1000, 9999, 1, 4753),
      orden4: ctrl('a', 'PRIMERO', 1000, 9999, 1, 5280) + ctrl('b', 'SEGUNDO', 1000, 9999, 1, 2850) + ctrl('c', 'TERCERO', 1000, 9999, 1, 5208),
      vecinos4: ctrl('n', 'NÚMERO', 1001, 9998, 1, 3999),
      recta10000: ctrl('n', 'NÚMERO', 100, 9900, 100, 6400),
      valor4: ctrl('m', 'MILES', 1, 9, 1, 4) + ctrl('c', 'CENTENAS', 0, 9, 1, 2) + ctrl('d', 'DECENAS', 0, 9, 1, 7) + ctrl('u', 'UNIDADES', 0, 9, 1, 6),
      armar4: ctrl('a', 'TARJETA 1', 1, 9, 1, 3) + ctrl('b', 'TARJETA 2', 1, 9, 1, 8) + ctrl('c', 'TARJETA 3', 1, 9, 1, 1) + ctrl('d', 'TARJETA 4', 1, 9, 1, 6),
      cambia4: ctrl('n', 'NÚMERO', 1000, 8899, 1, 3452),
      miles: ctrl('m', 'CAMIONES DE 1.000', p.min || 1, p.max || 9, 1, p.min || 2) + ctrl('c', 'CAJAS DE 100', 0, 9, 1, 3) + ctrl('d', 'PAQUETES DE 10', 0, 9, 1, 0) + ctrl('u', 'SUELTOS', 0, 9, 1, 5),
      saltos: ctrl('n', 'HASTA EL', (p.de || 2) * 3, (p.de || 2) * 10, p.de || 2, (p.de || 2) * 10),
      mayor_menor: ctrl('a', 'UN NÚMERO', 0, 20, 1, 12) + ctrl('b', 'OTRO NÚMERO', 0, 20, 1, 18) }[md];
    escena(el, C, function (v) {
      var P = [], i;
      if (md === 'contar') {
        P.push({ vis: p1Fila(v.n, o), txt: 'MIRÁ ' + g(o, 'LAS ', 'LOS ') + P1PL[o] + '. ' + g(o, 'LAS', 'LOS') + ' VAMOS A CONTAR DE A ' + g(o, 'UNA', 'UNO') + '.' });
        for (i = 1; i <= v.n; i++) P.push({ vis: p1Fila(v.n, o, { hasta: i, marca: i }), txt: (i === 1 ? 'TOCAMOS ' + g(o, 'LA PRIMERA', 'EL PRIMERO') + ' Y DECIMOS ' : 'TOCAMOS ' + g(o, 'OTRA', 'OTRO') + ' Y DECIMOS ') + '<b>' + i + '</b>.' });
        P.push({ vis: p1Fila(v.n, o, { hasta: v.n }) + p1Big('HAY ' + v.n), txt: 'YA TOCAMOS ' + g(o, 'TODAS', 'TODOS') + '. HAY <b>' + v.n + '</b> ' + P1PL[o] + '.' });
        return P;
      }
      if (md === 'cantidad') {
        P.push({ vis: p1Fila(v.n, o, { hasta: v.n }), txt: 'CONTAMOS ' + g(o, 'LAS ', 'LOS ') + P1PL[o] + ' DE A ' + g(o, 'UNA', 'UNO') + '.' });
        P.push({ vis: p1Fila(v.n, o, { hasta: v.n, marca: v.n }), txt: 'EL ÚLTIMO NÚMERO QUE DIJIMOS ES EL <b>' + v.n + '</b>.' });
        P.push({ vis: p1Fila(v.n, o, { hasta: v.n, marca: v.n }) + p1Big('HAY ' + v.n), txt: 'ESE NÚMERO DICE ' + g(o, 'CUÁNTAS', 'CUÁNTOS') + ' HAY: <b>' + v.n + '</b>.' });
        P.push({ vis: '<div class="lb-p1-mezcla">' + p1Fila(Math.ceil(v.n / 2), o) + p1Fila(Math.floor(v.n / 2), o) + '</div>' + p1Big('SIGUE HABIENDO ' + v.n), txt: 'SI ' + g(o, 'LAS', 'LOS') + ' CAMBIAMOS DE LUGAR, SIGUE HABIENDO <b>' + v.n + '</b>.' });
        return P;
      }
      if (md === 'mas_menos') {
        var G = function (ha, hb) { return p1Grupo(nm[0], v.a, o, { hasta: ha }) + p1Grupo(nm[1], v.b, o, { hasta: hb }); };
        P.push({ vis: G(0, 0), txt: nm[0] + ' Y ' + nm[1] + ' TIENEN ' + P1PL[o] + '. ¿QUIÉN TIENE MÁS?' });
        P.push({ vis: G(v.a, 0), txt: 'CONTAMOS ' + g(o, 'LAS', 'LOS') + ' DE ' + nm[0] + ': <b>' + v.a + '</b>.' });
        P.push({ vis: G(v.a, v.b), txt: 'CONTAMOS ' + g(o, 'LAS', 'LOS') + ' DE ' + nm[1] + ': <b>' + v.b + '</b>.' });
        if (v.a === v.b) P.push({ vis: G(v.a, v.b) + p1Big(v.a + ' Y ' + v.b + ': IGUAL'), txt: 'LOS DOS TIENEN <b>' + v.a + '</b>: TIENEN <b>IGUAL</b>.' });
        else { var ma = v.a > v.b ? nm[0] : nm[1], me = v.a > v.b ? nm[1] : nm[0], x = Math.max(v.a, v.b), y = Math.min(v.a, v.b);
          P.push({ vis: G(v.a, v.b) + p1Big(x + ' ES MÁS QUE ' + y), txt: '<b>' + ma + '</b> TIENE MÁS. <b>' + me + '</b> TIENE MENOS.' }); }
        return P;
      }
      if (md === 'uno_a_uno') {
        var A = pr[0], Bo = pr[1], mn = Math.min(v.a, v.b), d = Math.abs(v.a - v.b);
        P.push({ vis: p1Parejas(v.a, A, v.b, Bo, 0), txt: '¿ALCANZAN ' + g(Bo, 'LAS ', 'LOS ') + P1PL[Bo] + ' PARA ' + g(A, 'LAS ', 'LOS ') + P1PL[A] + '? NO HACE FALTA CONTAR.' });
        P.push({ vis: p1Parejas(v.a, A, v.b, Bo, 1), txt: 'UNIMOS UNO CON UNO: FORMAMOS UNA <b>PAREJA</b>.' });
        P.push({ vis: p1Parejas(v.a, A, v.b, Bo, mn), txt: 'SEGUIMOS UNIENDO HASTA QUE NO SE PUEDE MÁS.' });
        if (!d) P.push({ vis: p1Parejas(v.a, A, v.b, Bo, mn) + p1Big('HAY IGUAL'), txt: 'NO SOBRA NI FALTA NINGUNO: HAY <b>IGUAL</b>.' });
        else { var sob = v.b > v.a;
          P.push({ vis: p1Parejas(v.a, A, v.b, Bo, mn, true), txt: sob ? 'SOBRAN <b>' + d + '</b> ' + P1PL[Bo] + ' SIN PAREJA.' : 'FALTAN <b>' + d + '</b> ' + P1PL[Bo] + ': HAY ' + P1PL[A] + ' SIN PAREJA.' });
          P.push({ vis: p1Parejas(v.a, A, v.b, Bo, mn, true) + p1Big(sob ? 'MÁS ' + P1PL[Bo] : 'MENOS ' + P1PL[Bo]), txt: sob ? 'SI SOBRAN, HAY <b>MÁS</b> ' + P1PL[Bo] + ' QUE ' + P1PL[A] + '.' : 'SI FALTAN, HAY <b>MENOS</b> ' + P1PL[Bo] + ' QUE ' + P1PL[A] + '.' }); }
        return P;
      }
      if (md === 'igualar') {
        var quitar = p.op === 'quitar', g1 = v.a, g2 = v.b, dd = Math.abs(g1 - g2), may = g1 > g2 ? 1 : 2;
        var D = function (x1, x2, op1, op2) { return p1Grupo('GRUPO 1', x1, o, op1) + p1Grupo('GRUPO 2', x2, o, op2); };
        P.push({ vis: D(g1, g2, { hasta: g1 }, { hasta: g2 }), txt: 'EL GRUPO 1 TIENE <b>' + g1 + '</b> Y EL GRUPO 2 TIENE <b>' + g2 + '</b>.' });
        if (!dd) { P.push({ vis: D(g1, g2) + p1Big('YA HAY IGUAL'), txt: 'YA TIENEN LA MISMA CANTIDAD. PROBÁ CON OTROS NÚMEROS.' }); return P; }
        if (!quitar) {
          var chico = may === 1 ? 2 : 1, base = Math.min(g1, g2);
          P.push({ vis: D(g1, g2), txt: 'EL GRUPO ' + chico + ' TIENE MENOS: A ESE LE <b>AGREGAMOS</b>.' });
          for (i = 1; i <= dd; i++) { var t = base + i; P.push({ vis: chico === 2 ? D(g1, t, null, { nuevo: base, hasta: t }) : D(t, g2, { nuevo: base, hasta: t }, null), txt: 'AGREGAMOS ' + g(o, 'UNA', 'UNO') + ': AHORA TIENE <b>' + t + '</b>.' }); }
          P.push({ vis: (chico === 2 ? D(g1, g1) : D(g2, g2)) + p1Big(Math.max(g1, g2) + ' Y ' + Math.max(g1, g2) + ': IGUAL'), txt: 'AGREGAMOS <b>' + dd + '</b>. AHORA LOS DOS TIENEN IGUAL.' });
        } else {
          var gr = may, alto = Math.max(g1, g2), bajo = Math.min(g1, g2);
          P.push({ vis: D(g1, g2), txt: 'EL GRUPO ' + gr + ' TIENE MÁS: A ESE LE <b>QUITAMOS</b>.' });
          for (i = 1; i <= dd; i++) { var q = alto - i; P.push({ vis: gr === 1 ? D(g1, g2, { tenue: q }) : D(g1, g2, null, { tenue: q }), txt: 'QUITAMOS ' + g(o, 'UNA', 'UNO') + ': AHORA TIENE <b>' + q + '</b>.' }); }
          P.push({ vis: D(bajo, bajo) + p1Big(bajo + ' Y ' + bajo + ': IGUAL'), txt: 'QUITAMOS <b>' + dd + '</b>. AHORA LOS DOS TIENEN IGUAL.' });
        }
        return P;
      }
      if (md === 'tren') {
        var de = p.desde || 1;
        P.push({ vis: p1Tren(de, de), txt: 'EL PRIMER VAGÓN TIENE EL <b>' + de + '</b>.' });
        for (i = de + 1; i <= v.n; i++) { var op = {}; op[i] = 'on'; P.push({ vis: p1Tren(de, i, op), txt: 'DESPUÉS DEL ' + (i - 1) + ' VIENE EL <b>' + i + '</b>.' }); }
        P.push({ vis: p1Tren(de, v.n), txt: 'LOS NÚMEROS VAN EN ORDEN, SIN SALTEAR NINGUNO.' });
        return P;
      }
      if (md === 'decena') {
        var ob = pick(['caramelo', 'estrella', 'pelota']), tot = 10 + v.s;
        P.push({ vis: p1Caja(ob, v.s, { caja: true }), txt: 'LA CAJA ESTÁ LLENA: TIENE <b>10</b>. NO LA CONTAMOS DE NUEVO.' });
        for (i = 1; i <= v.s; i++) P.push({ vis: p1Caja(ob, v.s, { cuenta: i }), txt: 'SEGUIMOS DESDE EL 10: <b>' + (10 + i) + '</b>.' });
        P.push({ vis: p1Caja(ob, v.s, { cuenta: v.s }) + p1Big('10 Y ' + v.s + ' SON ' + tot), txt: tot === 20 ? 'DOS GRUPOS DE 10 SON <b>20</b>: VEINTE.' : '10 Y ' + v.s + ' SON <b>' + tot + '</b>: ' + p1Up(tot) + '.' });
        return P;
      }
      if (md === 'leer') {
        var s = String(v.n), u = v.n % 10, esc_ = p.forma === 'escribir';
        if (!esc_) {
          P.push({ vis: p1Cifras(v.n), txt: 'ESTE NÚMERO TIENE <b>DOS CIFRAS</b>: ' + s[0] + ' Y ' + s[1] + '.' });
          P.push({ vis: p1Cifras(v.n, 0), txt: v.n === 20 ? 'EMPIEZA CON <b>2</b>: SON DOS DIECES.' : 'EMPIEZA CON <b>1</b>: ES DIEZ Y ALGO MÁS.' });
          P.push({ vis: p1Cifras(v.n, 1), txt: v.n === 20 ? 'DESPUÉS VA EL 0: NO HAY SUELTOS.' : 'DESPUÉS VA EL <b>' + u + '</b>: DIEZ Y ' + u + '.' });
          P.push({ vis: p1Cifras(v.n, 9) + p1Big('SE LEE: ' + p1Up(v.n)), txt: 'CON PALABRAS SE LEE <b>' + p1Up(v.n) + '</b>.' });
        } else {
          P.push({ vis: p1Big(p1Up(v.n)), txt: 'QUEREMOS ESCRIBIR <b>' + p1Up(v.n) + '</b> CON CIFRAS.' });
          P.push({ vis: p1Big(p1Up(v.n)) + '<div class="lb-p1-cif"><span class="on">' + s[0] + '</span><span class="vac">?</span></div>', txt: v.n === 20 ? 'SON DOS DIECES: PRIMERO VA EL <b>2</b>.' : 'ES DIEZ Y ALGO MÁS: PRIMERO VA EL <b>1</b>.' });
          P.push({ vis: p1Big(p1Up(v.n)) + p1Cifras(v.n, 1), txt: 'DESPUÉS VA EL <b>' + s[1] + '</b>.' });
          P.push({ vis: p1Cifras(v.n, 9) + p1Big('SE ESCRIBE ' + v.n), txt: 'SE ESCRIBE <b>' + v.n + '</b>. EL ORDEN DE LAS CIFRAS IMPORTA.' });
        }
        return P;
      }
      if (md === 'anterior_siguiente') {
        var lo = Math.max(1, v.n - 3), hi = Math.min((p.max || 19) + 1, v.n + 3), m1 = {}, m2 = {}, m3 = {};
        m1[v.n] = 'on'; m2[v.n] = 'on'; m2[v.n - 1] = 'ant'; m3[v.n] = 'on'; m3[v.n - 1] = 'ant'; m3[v.n + 1] = 'sig';
        P.push({ vis: p1Tren(lo, hi, m1), txt: 'BUSCAMOS EL <b>' + v.n + '</b> EN EL TREN.' });
        P.push({ vis: p1Tren(lo, hi, m2), txt: 'ANTES DEL ' + v.n + ' VA EL <b>' + (v.n - 1) + '</b>: ES EL <b>ANTERIOR</b>.' });
        P.push({ vis: p1Tren(lo, hi, m3), txt: 'DESPUÉS DEL ' + v.n + ' VA EL <b>' + (v.n + 1) + '</b>: ES EL <b>SIGUIENTE</b>.' });
        P.push({ vis: p1Tren(lo, hi, m3) + p1Big((v.n - 1) + ' · ' + v.n + ' · ' + (v.n + 1)), txt: 'EL ANTERIOR VA ANTES Y EL SIGUIENTE VA DESPUÉS.' });
        return P;
      }
      if (md === 'mayor_menor') {
        var mk = function (lista) { var o2 = {}; lista.forEach(function (x) { o2[x[0]] = { c: x[1], t: x[2] }; }); return o2; };
        P.push({ vis: p1Recta(mk([[0, 'cero', '']])), txt: 'LA RECTA EMPIEZA EN EL <b>0</b>. LOS NÚMEROS VAN CRECIENDO.' });
        P.push({ vis: p1Recta(mk([[0, 'cero', ''], [v.a, 'pa', '']])), txt: 'MARCAMOS EL <b>' + v.a + '</b>.' });
        P.push({ vis: p1Recta(mk([[0, 'cero', ''], [v.a, 'pa', ''], [v.b, 'pb', '']])), txt: 'MARCAMOS EL <b>' + v.b + '</b>.' });
        if (v.a === v.b) P.push({ vis: p1Recta(mk([[v.a, 'pa', '']])) + p1Big('SON IGUALES'), txt: 'ES EL MISMO NÚMERO: NINGUNO ES MAYOR.' });
        else { var Mx = Math.max(v.a, v.b), Mn = Math.min(v.a, v.b);
          P.push({ vis: p1Recta(mk([[0, 'cero', ''], [Mn, 'pa', 'MENOR'], [Mx, 'pb', 'MAYOR']])), txt: 'EL <b>' + Mx + '</b> ESTÁ MÁS LEJOS DEL 0: ES EL <b>MAYOR</b>.' });
          P.push({ vis: p1Recta(mk([[0, 'cero', ''], [Mn, 'pa', 'MENOR'], [Mx, 'pb', 'MAYOR']])) + p1Big(Mx + ' ES MAYOR QUE ' + Mn), txt: 'Y EL <b>' + Mn + '</b> ES EL <b>MENOR</b>: ESTÁ MÁS CERCA DEL 0.' }); }
        return P;
      }
      if (md === 'cuadro') {
        var hc = p.hasta || 100, q = p.que || 'fila';
        if (q === 'contar') {
          P.push({ vis: p1Cuadro(v.n, null, 9), txt: 'LA PRIMERA FILA EMPIEZA EN EL <b>0</b> Y LLEGA AL <b>9</b>.' });
          for (i = 10; i <= v.n; i += 10) P.push({ vis: p1Cuadro(v.n, p1Marca([i], 'on'), Math.min(v.n, i + 9)), txt: 'DESPUÉS DEL <b>' + (i - 1) + '</b> VIENE EL <b>' + i + '</b>: ' + p1Up(i) + '.' });
          P.push({ vis: p1Cuadro(v.n, p1Marca(p1Col(0, v.n), 'on')), txt: 'LOS <b>REDONDOS</b> QUEDAN A LA IZQUIERDA: 10, 20, 30…' });
          return P;
        }
        if (q === 'bajar') {
          var ab = v.n + 10;
          P.push({ vis: p1Cuadro(hc, p1Marca([v.n], 'on')), txt: 'BUSCAMOS EL <b>' + v.n + '</b> EN EL CUADRO.' });
          P.push({ vis: p1Cuadro(hc, p1Marca([ab], 'sig', p1Marca([v.n], 'on'))), txt: 'BAJAMOS UNA FILA: JUSTO ABAJO ESTÁ EL <b>' + ab + '</b>.' });
          P.push({ vis: p1Cuadro(hc, p1Marca([ab], 'sig', p1Marca([v.n], 'on'))) + p1Big(v.n + ' Y 10 MÁS SON ' + ab), txt: 'BAJAR UNA FILA ES <b>SUMAR 10</b>.' });
          return P;
        }
        if (q === 'columna') {
          var u2 = v.n % 10, col = p1Col(v.n, hc);
          P.push({ vis: p1Cuadro(hc, p1Marca([v.n], 'on')), txt: 'BUSCAMOS EL <b>' + v.n + '</b> EN EL CUADRO.' });
          P.push({ vis: p1Cuadro(hc, p1Marca([v.n], 'on', p1Marca(col, 'fila'))), txt: 'MIRAMOS SU COLUMNA, DE ARRIBA ABAJO.' });
          P.push({ vis: p1Cuadro(hc, p1Marca([v.n], 'on', p1Marca(col, 'fila'))) + p1Big('TERMINAN EN ' + u2), txt: 'TODOS LOS DE ESA COLUMNA <b>TERMINAN EN ' + u2 + '</b>.' });
          return P;
        }
        var fi = p1Fil(v.n).filter(function (k) { return k <= hc; }), d1 = Math.floor(v.n / 10);
        P.push({ vis: p1Cuadro(hc, p1Marca([v.n], 'on')), txt: 'BUSCAMOS EL <b>' + v.n + '</b> EN EL CUADRO.' });
        P.push({ vis: p1Cuadro(hc, p1Marca([v.n], 'on', p1Marca(fi, 'fila'))), txt: 'MIRAMOS SU FILA, DE IZQUIERDA A DERECHA.' });
        P.push({ vis: p1Cuadro(hc, p1Marca([v.n], 'on', p1Marca(fi, 'fila'))) + p1Big('EMPIEZAN CON ' + d1), txt: 'TODOS LOS DE ESA FILA <b>EMPIEZAN CON ' + d1 + '</b>: SON LOS DEL ' + p1Up(d1 * 10) + '.' });
        return P;
      }
      if (md === 'comparar2') {
        var da = Math.floor(v.a / 10), db = Math.floor(v.b / 10), Gc = function (h) { return '<div class="lb-p1-dos">' + p1DU(v.a, h) + p1DU(v.b, h) + '</div>'; };
        P.push({ vis: Gc(''), txt: 'QUEREMOS SABER CUÁL ES MAYOR: <b>' + v.a + '</b> O <b>' + v.b + '</b>.' });
        P.push({ vis: Gc('d'), txt: 'PRIMERO MIRAMOS LAS <b>DECENAS</b>: ' + da + ' Y ' + db + '.' });
        if (v.a === v.b) { P.push({ vis: Gc('du') + p1Big('SON IGUALES'), txt: 'ES EL MISMO NÚMERO.' }); return P; }
        if (da === db) P.push({ vis: Gc('u'), txt: 'EMPATAN EN DECENAS: MIRAMOS LAS <b>UNIDADES</b>.' });
        var Mx2 = Math.max(v.a, v.b), Mn2 = Math.min(v.a, v.b);
        P.push({ vis: Gc(da === db ? 'u' : 'd') + p1Big(Mx2 + ' ES MAYOR QUE ' + Mn2), txt: '<b>' + Mx2 + '</b> ES EL MAYOR Y <b>' + Mn2 + '</b> ES EL MENOR.' });
        return P;
      }
      if (md === 'ordenar3') {
        var desc = p.orden === 'desc', L0 = [v.a, v.b, v.c], L1 = L0.slice().sort(function (x, y) { return desc ? y - x : x - y; });
        var Fi = function (lst, hl) { return '<div class="lb-p1-tren">' + lst.map(function (x, i) { return '<span class="lb-p1-vag' + (hl && hl.indexOf(i) >= 0 ? ' on' : '') + '">' + x + '</span>'; }).join('') + '</div>'; };
        P.push({ vis: Fi(L0), txt: 'VAMOS A ORDENAR DE <b>' + (desc ? 'MAYOR A MENOR' : 'MENOR A MAYOR') + '</b>.' });
        P.push({ vis: Fi(L0, [L0.indexOf(L1[0])]), txt: 'BUSCAMOS EL MÁS ' + (desc ? 'GRANDE' : 'CHICO') + ': <b>' + L1[0] + '</b>. VA PRIMERO.' });
        P.push({ vis: Fi(L1.slice(0, 2), [0, 1]), txt: 'DE LOS QUE QUEDAN, EL MÁS ' + (desc ? 'GRANDE' : 'CHICO') + ' ES <b>' + L1[1] + '</b>.' });
        P.push({ vis: Fi(L1, [0, 1, 2]) + p1Big(L1.join(desc ? ' > ' : ' < ')), txt: 'EL ÚLTIMO ES <b>' + L1[2] + '</b>. ¡LISTO!' });
        return P;
      }
      if (md === 'recta100') {
        if (p.que === 'saltar') {
          var at = p.dir === 'atras', pos = v.a, mk2 = function (lst) { var o2 = {}; lst.forEach(function (x) { o2[x[0]] = { c: x[1], t: x[2] }; }); return o2; };
          P.push({ vis: p1Recta(mk2([[pos, 'pa', 'ESTÁS']])), txt: 'ESTÁS EN EL <b>' + pos + '</b>. SALTÁS ' + v.s + ' PARA ' + (at ? 'ATRÁS' : 'ADELANTE') + '.' });
          for (i = 1; i <= v.s; i++) { var q2 = at ? pos - i : pos + i; P.push({ vis: p1Recta(mk2([[pos, 'pa', ''], [q2, 'pb', String(i)]])), txt: 'SALTO ' + i + ': CAEMOS EN EL <b>' + q2 + '</b>.' }); }
          var fin = at ? pos - v.s : pos + v.s;
          P.push({ vis: p1Recta(mk2([[pos, 'pa', ''], [fin, 'pb', 'LLEGÁS']])) + p1Big('LLEGÁS AL ' + fin), txt: at ? 'PARA ATRÁS LOS NÚMEROS SE ACHICAN.' : 'PARA ADELANTE LOS NÚMEROS CRECEN.' });
          return P;
        }
        var dd2 = Math.floor(v.n / 10) * 10;
        P.push({ vis: p1R100([]), txt: 'LA RECTA VA DEL <b>0</b> AL <b>100</b>, DE 10 EN 10.' });
        P.push({ vis: p1R100([[dd2, 'pa', dd2]]), txt: 'BUSCAMOS EL REDONDO DE ANTES: EL <b>' + dd2 + '</b>.' });
        P.push({ vis: p1R100([[dd2, 'pa', dd2], [v.n, 'pb', v.n]]), txt: v.n === dd2 ? 'EL ' + v.n + ' ESTÁ JUSTO EN LA MARCA.' : 'AVANZAMOS ' + (v.n - dd2) + ' MÁS: AHÍ ESTÁ EL <b>' + v.n + '</b>.' });
        P.push({ vis: p1R100([[v.n, 'pb', v.n]]) + p1Big('MÁS A LA DERECHA, MÁS GRANDE'), txt: 'LOS DE LA DERECHA SON MAYORES QUE EL ' + v.n + '.' });
        return P;
      }
      if (md === 'decenas') {
        var nn = v.d * 10 + v.u, q3 = p.que || 'contar';
        if (q3 === 'contar') {
          P.push({ vis: p1Bolsas(nn), txt: 'CADA BOLSITA TIENE <b>10</b>. ES UNA <b>DECENA</b>.' });
          P.push({ vis: p1Bolsas(nn, { bc: v.d }), txt: 'CONTAMOS LAS BOLSITAS DE 10 EN 10: <b>' + v.d * 10 + '</b>.' });
          if (v.u) P.push({ vis: p1Bolsas(nn, { bc: v.d, sc: v.u }), txt: 'SEGUIMOS CON LOS SUELTOS DE A UNO: <b>' + nn + '</b>.' });
          P.push({ vis: p1Bolsas(nn, { bc: v.d, sc: v.u }) + p1Big('HAY ' + nn), txt: v.d + ' DECENAS Y ' + v.u + ' UNIDADES SON <b>' + nn + '</b>.' });
          return P;
        }
        if (q3 === 'escribir') {
          P.push({ vis: p1Bolsas(nn), txt: 'TENEMOS <b>' + v.d + '</b> BOLSITAS Y <b>' + v.u + '</b> SUELTOS.' });
          P.push({ vis: p1DU(nn, 'd'), txt: 'LAS DECENAS VAN A LA <b>IZQUIERDA</b>: ' + v.d + '.' });
          P.push({ vis: p1DU(nn, 'du'), txt: 'LAS UNIDADES VAN A LA <b>DERECHA</b>: ' + v.u + '.' });
          P.push({ vis: p1DU(nn, 'du') + p1Big('SE ESCRIBE ' + nn), txt: 'SE ESCRIBE <b>' + nn + '</b> Y SE LEE <b>' + p1Up(nn) + '</b>.' });
          return P;
        }
        P.push({ vis: p1DU(nn), txt: 'VAMOS A DESARMAR EL <b>' + nn + '</b>.' });
        P.push({ vis: p1DU(nn, 'd') + p1Big(v.d + ' DECENAS VALEN ' + v.d * 10), txt: 'EL ' + v.d + ' ESTÁ EN LAS DECENAS: VALE <b>' + v.d * 10 + '</b>.' });
        P.push({ vis: p1DU(nn, 'u') + p1Big(v.u + ' UNIDADES VALEN ' + v.u), txt: 'EL ' + v.u + ' ESTÁ EN LAS UNIDADES: VALE <b>' + v.u + '</b>.' });
        P.push({ vis: p1DU(nn, 'du') + p1Big(nn + ' = ' + v.d * 10 + ' + ' + v.u), txt: 'ENTONCES <b>' + nn + ' = ' + v.d * 10 + ' + ' + v.u + '</b>.' });
        return P;
      }
      if (md === 'dinero') {
        var qd = p.que || 'contar';
        if (qd === 'contar') {
          var vs = []; for (i = 0; i < v.d; i++) vs.push(10); for (i = 0; i < v.c; i++) vs.push(5); for (i = 0; i < v.u; i++) vs.push(1);
          if (!vs.length) { P.push({ vis: p1Big('NO HAY DINERO'), txt: 'SUBÍ ALGÚN BILLETE O MONEDA.' }); return P; }
          P.push({ vis: p1Plata(vs), txt: 'EL NÚMERO DE CADA BILLETE Y MONEDA DICE <b>CUÁNTO VALE</b>.' });
          for (i = 1; i <= vs.length; i++) P.push({ vis: p1Plata(vs, i), txt: (i === 1 ? 'EMPEZAMOS POR LO QUE MÁS VALE: <b>' : 'SUMAMOS $' + vs[i - 1] + ': <b>') + vs.slice(0, i).reduce(function (x, y) { return x + y; }, 0) + '</b>.' });
          var tt = vs.reduce(function (x, y) { return x + y; }, 0);
          P.push({ vis: p1Plata(vs, vs.length) + p1Big('EN TOTAL $' + tt), txt: 'EN TOTAL HAY <b>$' + tt + '</b>.' });
          return P;
        }
        if (qd === 'pagar') {
          var ds = p1Desarmar(v.n);
          P.push({ vis: p1Big('CUESTA $' + v.n), txt: 'QUEREMOS PAGAR <b>JUSTO</b>: NI MÁS NI MENOS.' });
          for (i = 1; i <= ds.length; i++) P.push({ vis: p1Big('CUESTA $' + v.n) + p1Plata(ds.slice(0, i), i), txt: 'PONEMOS $' + ds[i - 1] + ': YA VAMOS <b>' + ds.slice(0, i).reduce(function (x, y) { return x + y; }, 0) + '</b>.' });
          P.push({ vis: p1Plata(ds, ds.length) + p1Big('$' + v.n + ' ¡JUSTO!'), txt: 'LLEGAMOS AL PRECIO: PAGAMOS <b>JUSTO</b>.' });
          return P;
        }
        if (qd === 'falta') {
          var da2 = Math.min(v.d, v.n - 1), ft = v.n - da2, op3 = {};
          P.push({ vis: p1Big('CUESTA $' + v.n + ' · DAS $' + da2), txt: 'CON $' + da2 + ' <b>NO ALCANZA</b> PARA PAGAR $' + v.n + '.' });
          for (i = 1; i <= ft; i++) { op3[da2 + i] = 'on'; P.push({ vis: p1Tren(da2, v.n, op3), txt: 'CONTAMOS DESDE ' + da2 + ': <b>' + (da2 + i) + '</b>.' }); }
          P.push({ vis: p1Tren(da2, v.n, op3) + p1Big('FALTAN $' + ft), txt: 'CONTAMOS ' + ft + ' VECES: FALTAN <b>$' + ft + '</b>.' });
          return P;
        }
        var ia = '🧃', ib = '🎈', mx = Math.max(v.a, v.b), mn = Math.min(v.a, v.b), Gp = function (h) { return '<div class="lb-p1-dos"><div class="lb-p1-pre' + (h && v.a === h ? ' on' : '') + '">' + ia + '<b>$' + v.a + '</b></div><div class="lb-p1-pre' + (h && v.b === h ? ' on' : '') + '">' + ib + '<b>$' + v.b + '</b></div></div>'; };
        P.push({ vis: Gp(), txt: 'EL JUGO CUESTA <b>$' + v.a + '</b> Y EL GLOBO <b>$' + v.b + '</b>.' });
        if (v.a === v.b) { P.push({ vis: Gp() + p1Big('CUESTAN IGUAL'), txt: 'TIENEN EL MISMO PRECIO.' }); return P; }
        P.push({ vis: Gp(mx), txt: 'EL PRECIO MÁS GRANDE ES <b>$' + mx + '</b>: ES EL MÁS <b>CARO</b>.' });
        P.push({ vis: Gp(mn) + p1Big('$' + mn + ' ES MÁS BARATO'), txt: 'EL PRECIO MÁS CHICO ES <b>$' + mn + '</b>: ES EL MÁS <b>BARATO</b>.' });
        return P;
      }
      if (md === 'sumar') {
        var qs = p.que || 'juntar', os = qs === 'palitos' ? 'palito' : o, tot2 = v.a + v.b;
        if (qs === 'juntar' || qs === 'palitos') {
          P.push({ vis: p1Grupo('', v.a, os) + p1Grupo('', v.b, os), txt: qs === 'palitos' ? 'DIBUJAMOS UN PALITO POR CADA COSA: <b>' + v.a + '</b> Y <b>' + v.b + '</b>.' : 'HAY DOS GRUPOS: UNO DE <b>' + v.a + '</b> Y OTRO DE <b>' + v.b + '</b>.' });
          P.push({ vis: p1Fila(tot2, os, { tenue: null }), txt: 'LOS <b>JUNTAMOS</b> EN UN SOLO GRUPO.' });
          for (i = 1; i <= tot2; i++) P.push({ vis: p1Fila(tot2, os, { hasta: i, marca: i }), txt: 'CONTAMOS: <b>' + i + '</b>.' });
          P.push({ vis: p1Fila(tot2, os, { hasta: tot2 }) + p1Big(v.a + ' Y ' + v.b + ' SON ' + tot2), txt: 'EN TOTAL HAY <b>' + tot2 + '</b>.' });
          return P;
        }
        if (qs === 'agregar') {
          P.push({ vis: p1Fila(v.a, o, { hasta: v.a }), txt: 'HABÍA <b>' + v.a + '</b> ' + P1PL[o] + '.' });
          P.push({ vis: p1Fila(tot2, o, { hasta: v.a, nuevo: v.a }), txt: 'LLEGAN <b>' + v.b + '</b> MÁS. NO EMPEZAMOS DE NUEVO.' });
          for (i = v.a + 1; i <= tot2; i++) P.push({ vis: p1Fila(tot2, o, { hasta: i, nuevo: v.a, marca: i }), txt: 'SEGUIMOS DESDE EL ' + v.a + ': <b>' + i + '</b>.' });
          P.push({ vis: p1Fila(tot2, o, { hasta: tot2, nuevo: v.a }) + p1Big('AHORA HAY ' + tot2), txt: 'EL GRUPO CRECIÓ: AHORA HAY <b>' + tot2 + '</b>.' });
          return P;
        }
        P.push({ vis: p1Grupo(String(v.a), v.a, o) + p1Grupo(String(v.b), v.b, o), txt: 'TENEMOS <b>' + v.a + '</b> Y <b>' + v.b + '</b>.' });
        P.push({ vis: p1Big(v.a + ' + ' + v.b), txt: 'EL SIGNO <b>+</b> SE LEE MÁS: QUIERE DECIR JUNTAR.' });
        P.push({ vis: p1Fila(tot2, o, { hasta: tot2 }) + p1Big(v.a + ' + ' + v.b + ' = ?'), txt: 'EL SIGNO <b>=</b> SE LEE IGUAL: DESPUÉS VA EL RESULTADO.' });
        P.push({ vis: p1Big(v.a + ' + ' + v.b + ' = ' + tot2), txt: 'CONTAMOS TODO Y ESCRIBIMOS <b>' + tot2 + '</b>.' });
        return P;
      }
      if (md === 'restar') {
        var qr = p.que || 'sacar', ha = v.a, sb = Math.min(v.b, v.a), qd2 = ha - sb;
        if (qr === 'comparar') {
          var A2 = 'chico', B2 = 'vaso', mn3 = Math.min(v.a, v.b), df = Math.abs(v.a - v.b);
          P.push({ vis: p1Parejas(v.a, A2, v.b, B2, 0), txt: 'HAY <b>' + v.a + '</b> CHICOS Y <b>' + v.b + '</b> VASOS.' });
          P.push({ vis: p1Parejas(v.a, A2, v.b, B2, mn3), txt: 'UNIMOS <b>UNO CON UNO</b>: CADA CHICO CON UN VASO.' });
          if (!df) { P.push({ vis: p1Parejas(v.a, A2, v.b, B2, mn3) + p1Big('HAY IGUAL'), txt: 'NO SOBRA NINGUNO: HAY IGUAL.' }); return P; }
          P.push({ vis: p1Parejas(v.a, A2, v.b, B2, mn3, true), txt: 'SOBRAN <b>' + df + '</b> ' + (v.b > v.a ? 'VASOS' : 'CHICOS') + ' SIN PAREJA.' });
          P.push({ vis: p1Parejas(v.a, A2, v.b, B2, mn3, true) + p1Big(Math.max(v.a, v.b) + ' − ' + mn3 + ' = ' + df), txt: 'HAY <b>' + df + ' MÁS</b> ' + (v.b > v.a ? 'VASOS QUE CHICOS' : 'CHICOS QUE VASOS') + '.' });
          return P;
        }
        if (qr === 'atras') {
          var opA = {}; opA[ha] = 'on';
          P.push({ vis: p1Tren(qd2, ha, opA), txt: 'HABÍA <b>' + ha + '</b>. SE VAN ' + sb + ': CONTAMOS PARA ATRÁS.' });
          for (i = 1; i <= sb; i++) { var opB = {}; opB[ha] = 'on'; for (var j = 1; j <= i; j++) opB[ha - j] = 'ant'; P.push({ vis: p1Tren(qd2, ha, opB), txt: 'SE VA ' + g(o, 'UNA', 'UNO') + ': <b>' + (ha - i) + '</b>.' }); }
          P.push({ vis: p1Big('QUEDAN ' + qd2), txt: 'CONTAMOS ' + sb + ' PARA ATRÁS: QUEDAN <b>' + qd2 + '</b>.' });
          return P;
        }
        P.push({ vis: p1Fila(ha, o, { hasta: ha }), txt: 'HABÍA <b>' + ha + '</b> ' + P1PL[o] + '.' });
        if (qr === 'cuenta') {
          P.push({ vis: p1Fila(ha, o, { tenue: qd2 }) + p1Big(ha + ' − ' + sb), txt: 'SACAMOS <b>' + sb + '</b>. EL SIGNO <b>−</b> SE LEE MENOS.' });
          P.push({ vis: p1Fila(ha, o, { tenue: qd2, hasta: qd2 }) + p1Big(ha + ' − ' + sb + ' = ' + qd2), txt: 'CONTAMOS LOS QUE QUEDAN: <b>' + ha + ' − ' + sb + ' = ' + qd2 + '</b>.' });
          return P;
        }
        for (i = 1; i <= sb; i++) P.push({ vis: p1Fila(ha, o, { tenue: ha - i }), txt: 'SACAMOS ' + g(o, 'UNA', 'UNO') + '. QUEDAN <b>' + (ha - i) + '</b>.' });
        P.push({ vis: p1Fila(ha, o, { tenue: qd2, hasta: qd2 }) + p1Big('QUEDAN ' + qd2), txt: 'AL SACAR, EL GRUPO SE <b>ACHICA</b>: QUEDAN ' + qd2 + '.' });
        return P;
      }
      if (md === 'diez') {
        var qz = p.que || 'cuadro';
        if (qz === 'dados') {
          var gr2 = Math.max(v.a, v.b), ch2 = Math.min(v.a, v.b), Dd = '<p class="lb-p1-big lb-p1-dado">' + P1DADO[v.a] + ' ' + P1DADO[v.b] + '</p>';
          P.push({ vis: Dd, txt: 'SALE <b>' + v.a + '</b> EN UN DADO Y <b>' + v.b + '</b> EN EL OTRO.' });
          P.push({ vis: Dd + p1Big('EMPEZAMOS EN ' + gr2), txt: 'EMPEZAMOS POR EL <b>MÁS GRANDE</b>: ' + gr2 + '.' });
          for (i = 1; i <= ch2; i++) P.push({ vis: Dd + p1Big(String(gr2 + i)), txt: 'SEGUIMOS CONTANDO: <b>' + (gr2 + i) + '</b>.' });
          P.push({ vis: Dd + p1Big(v.a + ' + ' + v.b + ' = ' + (v.a + v.b)), txt: 'EN TOTAL: <b>' + (v.a + v.b) + '</b>.' });
          return P;
        }
        var am = 10 - v.a;
        P.push({ vis: p1Diez(v.a, 0), txt: 'EL CUADRO TIENE <b>10</b> LUGARES. HAY <b>' + v.a + '</b> ROJOS.' });
        if (qz === 'falta') {
          P.push({ vis: p1Diez(v.a, 0), txt: 'CONTAMOS LOS LUGARES <b>VACÍOS</b>.' });
          P.push({ vis: p1Diez(v.a, am), txt: 'HAY <b>' + am + '</b> VACÍOS: AL ' + v.a + ' LE FALTAN ' + am + '.' });
          P.push({ vis: p1Diez(v.a, am) + p1Big(v.a + ' + ' + am + ' = 10'), txt: 'EL <b>' + am + '</b> ES EL AMIGO DEL ' + v.a + ' PARA LLEGAR A 10.' });
          return P;
        }
        for (i = 1; i <= am; i++) P.push({ vis: p1Diez(v.a, am, i), txt: 'PONEMOS UN AZUL: <b>' + (v.a + i) + '</b>.' });
        P.push({ vis: p1Diez(v.a, am) + p1Big(v.a + ' + ' + am + ' = 10'), txt: 'EL CUADRO SE LLENÓ: <b>' + v.a + ' + ' + am + ' = 10</b>.' });
        if (qz === 'parejas') P.push({ vis: p1Diez(am, v.a) + p1Big(am + ' + ' + v.a + ' = 10'), txt: 'SI LO DAMOS VUELTA, <b>' + am + ' + ' + v.a + '</b> TAMBIÉN ES 10.' });
        return P;
      }
      if (md === 'dobles') {
        var qb = p.que || 'espejo', ob = pick(['estrella', 'manzana', 'flor', 'globo']);
        if (qb === 'iguales') {
          var Gq = function (k2) { var h2 = ''; for (var j2 = 0; j2 < v.k; j2++) h2 += p1Grupo('', v.a, ob, j2 < k2 ? { hasta: v.a } : null); return h2; }, sum = [];
          P.push({ vis: Gq(0), txt: 'HAY <b>' + v.k + '</b> GRUPOS Y CADA UNO TIENE <b>' + v.a + '</b>.' });
          for (i = 1; i <= v.k; i++) { sum.push(v.a); P.push({ vis: Gq(i) + p1Big(sum.join(' + ')), txt: 'SUMAMOS OTRO ' + v.a + ': <b>' + v.a * i + '</b>.' }); }
          P.push({ vis: Gq(v.k) + p1Big(sum.join(' + ') + ' = ' + v.a * v.k), txt: 'SUMAMOS EL MISMO NÚMERO ' + v.k + ' VECES: <b>' + v.a * v.k + '</b>.' });
          return P;
        }
        if (qb === 'casi') {
          var dob = 2 * v.a;
          P.push({ vis: p1Grupo(String(v.a), v.a, ob) + p1Grupo(String(v.a + 1), v.a + 1, ob), txt: 'QUEREMOS SUMAR <b>' + v.a + ' + ' + (v.a + 1) + '</b>.' });
          P.push({ vis: p1Grupo(String(v.a), v.a, ob, { hasta: v.a }) + p1Grupo(String(v.a + 1), v.a + 1, ob, { hasta: v.a, tenue: v.a }), txt: 'MIRAMOS EL DOBLE: <b>' + v.a + ' + ' + v.a + ' = ' + dob + '</b>.' });
          P.push({ vis: p1Grupo(String(v.a), v.a, ob) + p1Grupo(String(v.a + 1), v.a + 1, ob, { marca: v.a + 1 }), txt: 'SOBRA <b>UNO</b> MÁS.' });
          P.push({ vis: p1Big(v.a + ' + ' + (v.a + 1) + ' = ' + (dob + 1)), txt: 'EL DOBLE Y UNO MÁS: <b>' + dob + ' + 1 = ' + (dob + 1) + '</b>.' });
          return P;
        }
        if (qb === 'tabla') {
          var lin = [];
          for (i = 1; i <= v.a; i++) { lin.push(i + ' + ' + i + ' = ' + 2 * i); P.push({ vis: '<div class="lb-p1-tab">' + lin.map(function (x, k) { return '<span' + (k === lin.length - 1 ? ' class="on"' : '') + '>' + x + '</span>'; }).join('') + '</div>', txt: 'EL DOBLE DE ' + i + ' ES <b>' + 2 * i + '</b>.' }); }
          P.push({ vis: '<div class="lb-p1-tab">' + lin.map(function (x) { return '<span>' + x + '</span>'; }).join('') + '</div>', txt: 'LOS DOBLES VAN <b>DE 2 EN 2</b>: 2, 4, 6, 8…' });
          return P;
        }
        P.push({ vis: p1Fila(v.a, ob, { hasta: v.a }), txt: 'TENEMOS <b>' + v.a + '</b>.' });
        P.push({ vis: '<div class="lb-p1-esp">' + p1Fila(v.a, ob) + '<i>🪞</i>' + p1Fila(v.a, ob) + '</div>', txt: 'EL ESPEJO MUESTRA <b>OTROS ' + v.a + '</b> IGUALES.' });
        P.push({ vis: '<div class="lb-p1-esp">' + p1Fila(v.a, ob) + '<i>🪞</i>' + p1Fila(v.a, ob) + '</div>' + p1Big(v.a + ' + ' + v.a + ' = ' + 2 * v.a), txt: 'DOS VECES LO MISMO ES EL <b>DOBLE</b>: ' + 2 * v.a + '.' });
        return P;
      }
      if (md === 'decenas_op') {
        var qo = p.que || 'sumar';
        if (qo === 'atras10') { var lst = []; for (i = v.a; i >= Math.max(0, v.a - 50); i -= 10) lst.push(i);
          for (i = 1; i <= lst.length; i++) P.push({ vis: '<div class="lb-p1-tren">' + lst.map(function (x, k) { return '<span class="lb-p1-vag' + (k < i ? (k === i - 1 ? ' on' : ' ant') : '') + '">' + (k < i ? x : '') + '</span>'; }).join('') + '</div>', txt: i === 1 ? 'EMPEZAMOS EN EL <b>' + lst[0] + '</b>.' : 'RESTAMOS 10: <b>' + lst[i - 1] + '</b>.' });
          P.push({ vis: p1Big(lst.join(', ')), txt: 'PARA ATRÁS DE 10 EN 10, LA PRIMERA CIFRA <b>BAJA 1</b>.' });
          return P; }
        if (qo === 'restar') { var bb = Math.min(v.b, v.a - 1), rr = v.a - bb;
          P.push({ vis: p1BolsasN(v.a), txt: 'HAY <b>' + v.a + '</b> BOLSITAS DE 10: SON <b>' + v.a * 10 + '</b>.' });
          P.push({ vis: p1BolsasN(v.a, { tenue: rr }), txt: 'SE VENDEN <b>' + bb + '</b> BOLSITAS: ' + bb * 10 + '.' });
          P.push({ vis: p1BolsasN(v.a, { tenue: rr }) + p1Big(v.a + ' − ' + bb + ' = ' + rr + ' BOLSITAS'), txt: 'RESTAMOS LAS BOLSITAS: QUEDAN <b>' + rr + '</b>.' });
          P.push({ vis: p1BolsasN(v.a, { tenue: rr }) + p1Big(v.a * 10 + ' − ' + bb * 10 + ' = ' + rr * 10), txt: rr + ' BOLSITAS DE 10 SON <b>' + rr * 10 + '</b>.' });
          return P; }
        var b2 = Math.min(v.b, 10 - v.a), tt2 = v.a + b2;
        P.push({ vis: p1BolsasN(v.a), txt: 'HAY <b>' + v.a + '</b> BOLSITAS DE 10: SON <b>' + v.a * 10 + '</b>.' });
        P.push({ vis: p1BolsasN(tt2, { nuevo: v.a }), txt: 'LLEGAN <b>' + b2 + '</b> BOLSITAS MÁS: ' + b2 * 10 + '.' });
        P.push({ vis: p1BolsasN(tt2, { nuevo: v.a }) + p1Big(v.a + ' + ' + b2 + ' = ' + tt2 + ' BOLSITAS'), txt: 'SUMAMOS LAS BOLSITAS: <b>' + tt2 + '</b>.' });
        P.push({ vis: p1BolsasN(tt2, { nuevo: v.a }) + p1Big(v.a * 10 + ' + ' + b2 * 10 + ' = ' + tt2 * 10), txt: tt2 + ' BOLSITAS DE 10 SON <b>' + tt2 * 10 + '</b>.' });
        return P;
      }
      if (md === 'problema') {
        var Hh = p1Hist(p.tipo || 'juntar', v.a / (p.esc || 1), v.b / (p.esc || 1), nm, o, p.esc || 1), Bx = function (x) { return '<div class="lb-p1-hist">' + x + '</div>'; };
        P.push({ vis: Bx(Hh.h + '<br>' + Hh.q), txt: 'LEEMOS EL PROBLEMA CON ATENCIÓN.' });
        P.push({ vis: Bx(Hh.h), txt: 'LOS <b>DATOS</b> SON LOS NÚMEROS QUE YA SABEMOS.' });
        P.push({ vis: Bx('<b>' + Hh.q + '</b>'), txt: 'LA <b>PREGUNTA</b> DICE QUÉ TENEMOS QUE AVERIGUAR.' });
        P.push({ vis: Hh.v, txt: p.tipo === 'dospasos' ? Hh.w + '.' : Hh.w + ': HACEMOS UNA <b>' + (Hh.op === '+' ? 'SUMA' : 'RESTA') + '</b>.' });
        P.push({ vis: Hh.v + p1Big(Hh.c), txt: 'LA CUENTA ES <b>' + Hh.c + '</b>.' });
        P.push({ vis: p1Big('RESPUESTA: ' + Hh.r), txt: 'RESPONDEMOS LA PREGUNTA CON UNA ORACIÓN: SON <b>' + Hh.r + '</b>.' });
        return P;
      }
      if (md === 'calcu') {
        var qc = p.que || 'teclas', opc = p.op === 'resta' ? '−' : '+';
        if (qc === 'partes') {
          P.push({ vis: p1Calc(v.n, 'pan'), txt: 'ARRIBA ESTÁ LA <b>PANTALLA</b>: MUESTRA LOS NÚMEROS.' });
          P.push({ vis: p1Calc(v.n, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']), txt: 'ESTAS SON LAS <b>TECLAS DE NÚMEROS</b>, DEL 0 AL 9.' });
          P.push({ vis: p1Calc(v.n, ['+', '−']), txt: 'EL <b>+</b> SUMA Y EL <b>−</b> RESTA.' });
          P.push({ vis: p1Calc(v.n, '='), txt: 'EL <b>=</b> MUESTRA EL RESULTADO.' });
          P.push({ vis: p1Calc('0', 'C'), txt: 'LA <b>C</b> BORRA TODO Y LA PANTALLA VUELVE A 0.' });
          return P;
        }
        if (qc === 'uno_diez') {
          var opu = p.op || 'mas10', dl = opu === 'mas1' ? 1 : opu === 'menos10' ? -10 : 10, rs = v.n + dl, sg = dl > 0 ? '+' : '−';
          P.push({ vis: p1Calc(v.n, 'pan'), txt: 'EN LA PANTALLA ESTÁ EL <b>' + v.n + '</b>.' });
          P.push({ vis: p1Calc(v.n + ' ' + sg + ' ' + Math.abs(dl), [sg]), txt: 'APRETAMOS <b>' + sg + ' ' + Math.abs(dl) + '</b>.' });
          P.push({ vis: p1Calc(rs, ['=', 'pan']), txt: 'APRETAMOS <b>=</b>: SALE <b>' + rs + '</b>.' });
          P.push({ vis: p1Cifras(v.n) + p1Cifras(rs, opu === 'mas1' ? 1 : 0), txt: opu === 'mas1' ? 'CAMBIA LA <b>ÚLTIMA</b> CIFRA: UNO MÁS.' : 'CAMBIA LA <b>PRIMERA</b> CIFRA: UNA DECENA ' + (dl > 0 ? 'MÁS' : 'MENOS') + '.' });
          return P;
        }
        var A3 = qc === 'teclas' && opc === '−' ? Math.max(v.a, v.b + 1) : v.a, res = opc === '+' ? A3 + v.b : A3 - v.b, ds2 = String(A3).split(''), pan = '';
        if (qc === 'controlar') {
          var malo = Number(String(A3) + String(v.b));
          P.push({ vis: p1Calc(A3 + ' + ' + v.b + ' = ' + malo, 'pan'), txt: 'LA PANTALLA DICE <b>' + A3 + ' + ' + v.b + ' = ' + malo + '</b>. ¿ESTARÁ BIEN?' });
          P.push({ vis: p1Big('¿' + malo + '?'), txt: 'PENSAMOS ANTES: SUMAR ' + v.b + ' AL ' + A3 + ' NO PUEDE DAR TANTO.' });
          P.push({ vis: p1Calc(A3 + ' + ' + v.b + ' = ' + res, ['=', 'pan']), txt: 'LO HACEMOS DE NUEVO CON CUIDADO: SALE <b>' + res + '</b>.' });
          P.push({ vis: p1Big('ESTABA MAL'), txt: 'SE APRETÓ MAL: LA CALCULADORA HACE <b>LO QUE APRETAMOS</b>.' });
          return P;
        }
        ds2.forEach(function (d) { pan += d; P.push({ vis: p1Calc(pan, d), txt: 'APRETAMOS EL <b>' + d + '</b>.' }); });
        P.push({ vis: p1Calc(A3 + ' ' + opc, opc), txt: 'APRETAMOS EL <b>' + opc + '</b>.' });
        P.push({ vis: p1Calc(A3 + ' ' + opc + ' ' + v.b, String(v.b)), txt: 'APRETAMOS EL <b>' + v.b + '</b>.' });
        P.push({ vis: p1Calc(res, ['=', 'pan']), txt: 'APRETAMOS EL <b>=</b>: SALE <b>' + res + '</b>.' });
        return P;
      }
      if (md === 'centenas') {
        var nC = v.c * 100 + v.d * 10 + v.u, qC = p.que || 'contar';
        if (qC === 'contar') {
          P.push({ vis: p1CDU(nC), txt: 'UNA CAJA TIENE <b>100</b>, UN PAQUETE <b>10</b> Y CADA SUELTO <b>1</b>.' });
          P.push({ vis: p1CDU(nC, { c: v.c }), txt: 'CONTAMOS LAS CAJAS DE 100 EN 100: <b>' + v.c * 100 + '</b>.' });
          if (v.d) P.push({ vis: p1CDU(nC, { c: v.c, d: v.d }), txt: 'SEGUIMOS CON LOS PAQUETES DE 10 EN 10: <b>' + (v.c * 100 + v.d * 10) + '</b>.' });
          if (v.u) P.push({ vis: p1CDU(nC, { c: v.c, d: v.d, u: v.u }), txt: 'Y LOS SUELTOS DE 1 EN 1: <b>' + nC + '</b>.' });
          P.push({ vis: p1CDU(nC, { c: v.c, d: v.d, u: v.u }) + p1Big('HAY ' + nC), txt: 'EN TOTAL HAY <b>' + nC + '</b>.' });
          return P;
        }
        P.push({ vis: p1CDU(nC), txt: 'TENEMOS <b>' + v.c + '</b> CAJAS, <b>' + v.d + '</b> PAQUETES Y <b>' + v.u + '</b> SUELTOS.' });
        P.push({ vis: p1CDUt(nC, 0), txt: 'LAS CAJAS SON <b>CENTENAS</b>: VAN PRIMERO.' });
        P.push({ vis: p1CDUt(nC, 1), txt: v.d ? 'LOS PAQUETES SON <b>DECENAS</b>: VAN EN EL MEDIO.' : 'NO HAY PAQUETES: EL <b>0</b> GUARDA SU LUGAR.' });
        P.push({ vis: p1CDUt(nC, 2), txt: 'LOS SUELTOS SON <b>UNIDADES</b>: VAN AL FINAL.' });
        P.push({ vis: p1CDUt(nC, 9) + p1Big(String(nC)), txt: 'SE ESCRIBE <b>' + nC + '</b> Y SE LEE <b>' + p1Up(nC) + '</b>.' });
        return P;
      }
      if (md === 'serie') {
        var pa = p.de || 10, baja = p.dir === 'baja', L5 = [];
        for (i = 0; i < 5; i++) L5.push(v.a + (baja ? -pa : pa) * i);
        for (i = 1; i <= 5; i++) P.push({ vis: '<div class="lb-p1-tren">' + L5.map(function (x, k) { return '<span class="lb-p1-vag' + (k < i ? (k === i - 1 ? ' on' : '') : ' oculto') + '">' + (k < i ? fmt(x) : '?') + '</span>'; }).join('') + '</div>', txt: i === 1 ? 'EMPEZAMOS EN EL <b>' + fmt(L5[0]) + '</b>.' : (baja ? 'RESTAMOS ' : 'SUMAMOS ') + fmt(pa) + ': <b>' + fmt(L5[i - 1]) + '</b>.' });
        P.push({ vis: p1Big(L5.map(fmt).join(', ')), txt: 'LA SERIE <b>' + (baja ? 'BAJA' : 'SUBE') + '</b> DE ' + pa + ' EN ' + pa + (pa === 10 ? ': CAMBIA LA CIFRA DE LAS DECENAS.' : pa === 100 ? ': CAMBIA LA CIFRA DE LAS CENTENAS.' : pa === 1000 ? ': CAMBIA LA CIFRA DE LOS MILES.' : '.') });
        return P;
      }
      if (md === 'valor') {
        var nV = v.c * 100 + v.d * 10 + v.u;
        P.push({ vis: p1CDUt(nV), txt: 'EL <b>' + nV + '</b> TIENE TRES CIFRAS.' });
        P.push({ vis: p1CDUt(nV, 0) + p1Big(v.c + ' CENTENAS = ' + v.c * 100), txt: 'EL <b>' + v.c + '</b> ESTÁ EN LAS CENTENAS: VALE <b>' + v.c * 100 + '</b>.' });
        P.push({ vis: p1CDUt(nV, 1) + p1Big(v.d + ' DECENAS = ' + v.d * 10), txt: 'EL <b>' + v.d + '</b> ESTÁ EN LAS DECENAS: VALE <b>' + v.d * 10 + '</b>.' });
        P.push({ vis: p1CDUt(nV, 2) + p1Big(v.u + ' UNIDADES = ' + v.u), txt: 'EL <b>' + v.u + '</b> ESTÁ EN LAS UNIDADES: VALE <b>' + v.u + '</b>.' });
        P.push({ vis: p1CDUt(nV, 9) + p1Big(nV + ' = ' + v.c * 100 + ' + ' + v.d * 10 + ' + ' + v.u), txt: 'CADA CIFRA VALE SEGÚN SU <b>LUGAR</b>.' });
        return P;
      }
      if (md === 'comparar3') {
        var sa = String(v.a), sb2 = String(v.b), Gk = function (h) { return '<div class="lb-p1-dos">' + p1CDUt(v.a, h) + p1CDUt(v.b, h) + '</div>'; }, NOM = ['CENTENAS', 'DECENAS', 'UNIDADES'];
        P.push({ vis: Gk(), txt: '¿CUÁL ES MAYOR: <b>' + v.a + '</b> O <b>' + v.b + '</b>?' });
        if (v.a === v.b) { P.push({ vis: Gk(9) + p1Big('SON IGUALES'), txt: 'ES EL MISMO NÚMERO.' }); return P; }
        for (i = 0; i < 3; i++) { P.push({ vis: Gk(i), txt: 'MIRAMOS LAS <b>' + NOM[i] + '</b>: ' + sa[i] + ' Y ' + sb2[i] + (sa[i] === sb2[i] ? '. EMPATAN.' : '.') }); if (sa[i] !== sb2[i]) break; }
        P.push({ vis: Gk(i) + p1Big(Math.max(v.a, v.b) + ' ES MAYOR QUE ' + Math.min(v.a, v.b)), txt: '<b>' + Math.max(v.a, v.b) + '</b> ES EL MAYOR.' });
        return P;
      }
      if (md === 'orden3') {
        var dsc = p.orden === 'desc', O0 = [v.a, v.b, v.c], O1 = O0.slice().sort(function (x, y) { return dsc ? y - x : x - y; });
        var Fo = function (lst, hl) { return '<div class="lb-p1-tren">' + lst.map(function (x, i) { return '<span class="lb-p1-vag' + (hl && hl.indexOf(i) >= 0 ? ' on' : '') + '">' + x + '</span>'; }).join('') + '</div>'; };
        P.push({ vis: Fo(O0), txt: 'VAMOS A ORDENAR DE <b>' + (dsc ? 'MAYOR A MENOR' : 'MENOR A MAYOR') + '</b>. MIRAMOS PRIMERO LAS CENTENAS.' });
        P.push({ vis: Fo(O0, [O0.indexOf(O1[0])]), txt: 'EL MÁS ' + (dsc ? 'GRANDE' : 'CHICO') + ' ES <b>' + O1[0] + '</b>.' });
        P.push({ vis: Fo(O1.slice(0, 2), [0, 1]), txt: 'DESPUÉS VA <b>' + O1[1] + '</b>.' });
        P.push({ vis: Fo(O1, [0, 1, 2]) + p1Big(O1.join(dsc ? ' > ' : ' < ')), txt: 'Y AL FINAL <b>' + O1[2] + '</b>.' });
        return P;
      }
      if (md === 'recta1000') {
        var c0 = Math.floor(v.n / 100) * 100;
        P.push({ vis: p1R1000([]), txt: 'LA RECTA VA DEL <b>0</b> AL <b>1.000</b>, DE 100 EN 100.' });
        P.push({ vis: p1R1000([[c0, 'pa', c0]]), txt: 'EL ' + v.n + ' TIENE ' + (c0 / 100) + ' CENTENAS: EMPEZAMOS EN EL <b>' + c0 + '</b>.' });
        P.push({ vis: p1R1000([[c0, 'pa', c0], [v.n, 'pb', v.n]]), txt: v.n === c0 ? 'ESTÁ JUSTO EN LA MARCA.' : 'ESTÁ ENTRE EL <b>' + c0 + '</b> Y EL <b>' + (c0 + 100) + '</b>.' });
        P.push({ vis: p1R1000([[v.n, 'pb', v.n]]) + p1Big('MÁS A LA DERECHA, MÁS GRANDE'), txt: 'LOS DE LA DERECHA SON MAYORES QUE EL ' + v.n + '.' });
        return P;
      }
      if (md === 'cambia') {
        var ad = p.op || 100, nn2 = v.n + ad, pos = ad === 100 ? 0 : ad === 10 ? 1 : 2, NM = ['UNA CAJA DE 100', 'UN PAQUETE DE 10', 'UN SUELTO'];
        P.push({ vis: p1CDUt(v.n), txt: 'TENEMOS EL <b>' + v.n + '</b>.' });
        P.push({ vis: p1CDUt(v.n, pos), txt: 'LLEGA <b>' + NM[pos] + '</b>: SUMAMOS ' + ad + '.' });
        P.push({ vis: p1CDUt(nn2, pos) + p1Big(v.n + ' + ' + ad + ' = ' + nn2), txt: 'CAMBIA SOLO LA CIFRA DE LAS <b>' + ['CENTENAS', 'DECENAS', 'UNIDADES'][pos] + '</b>' + (String(nn2).length > 3 || String(nn2)[pos] === '0' ? ' (Y PUEDE ARRASTRAR A LA DE AL LADO).' : '.') });
        return P;
      }
      if (md === 'comparar4') {
        var sa4 = String(v.a), sb4 = String(v.b), G4 = function (h) { return '<div class="lb-p1-dos">' + p1CDUt(v.a, h) + p1CDUt(v.b, h) + '</div>'; }, NOM4 = ['MILES', 'CENTENAS', 'DECENAS', 'UNIDADES'];
        P.push({ vis: G4(), txt: '¿CUÁL ES MAYOR: <b>' + fmt(v.a) + '</b> O <b>' + fmt(v.b) + '</b>?' });
        if (v.a === v.b) { P.push({ vis: G4(9) + p1Big('SON IGUALES'), txt: 'ES EL MISMO NÚMERO.' }); return P; }
        for (i = 0; i < 4; i++) { P.push({ vis: G4(i), txt: 'MIRAMOS ' + (i ? 'LAS ' : 'LOS ') + '<b>' + NOM4[i] + '</b>: ' + sa4[i] + ' Y ' + sb4[i] + (sa4[i] === sb4[i] ? '. EMPATAN.' : '.') }); if (sa4[i] !== sb4[i]) break; }
        P.push({ vis: G4(i) + p1Big(fmt(Math.max(v.a, v.b)) + ' > ' + fmt(Math.min(v.a, v.b))), txt: '<b>' + fmt(Math.max(v.a, v.b)) + '</b> ES MAYOR QUE ' + fmt(Math.min(v.a, v.b)) + '.' });
        return P;
      }
      if (md === 'orden4') {
        var ds4 = p.orden === 'desc', Q0 = [v.a, v.b, v.c], Q1 = Q0.slice().sort(function (x, y) { return ds4 ? y - x : x - y; });
        var Fq = function (lst, hl) { return '<div class="lb-p1-tren">' + lst.map(function (x, i) { return '<span class="lb-p1-vag' + (hl && hl.indexOf(i) >= 0 ? ' on' : '') + '">' + fmt(x) + '</span>'; }).join('') + '</div>'; };
        P.push({ vis: Fq(Q0), txt: 'ORDENAMOS DE <b>' + (ds4 ? 'MAYOR A MENOR' : 'MENOR A MAYOR') + '</b>. PRIMERO MIRAMOS LOS MILES.' });
        P.push({ vis: Fq(Q0, [Q0.indexOf(Q1[0])]), txt: 'EL MÁS ' + (ds4 ? 'GRANDE' : 'CHICO') + ' ES <b>' + fmt(Q1[0]) + '</b>.' });
        P.push({ vis: Fq(Q1.slice(0, 2), [0, 1]), txt: 'DESPUÉS VA <b>' + fmt(Q1[1]) + '</b>.' });
        P.push({ vis: Fq(Q1, [0, 1, 2]) + p1Big(Q1.map(fmt).join(ds4 ? ' > ' : ' < ')), txt: 'Y AL FINAL <b>' + fmt(Q1[2]) + '</b>.' });
        return P;
      }
      if (md === 'vecinos4') {
        var Tv = function (k) { return '<div class="lb-p1-tren">' + [v.n - 1, v.n, v.n + 1].map(function (x, i) { return '<span class="lb-p1-vag' + (i === 1 ? ' on' : '') + (k < 2 && i === 0 || k < 3 && i === 2 ? ' oculto">?' : '">' + fmt(x)) + '</span>'; }).join('') + '</div>'; };
        P.push({ vis: Tv(1), txt: 'TENEMOS EL <b>' + fmt(v.n) + '</b>.' });
        P.push({ vis: Tv(2), txt: 'EL <b>ANTERIOR</b> ES UNO MENOS: <b>' + fmt(v.n - 1) + '</b>.' });
        P.push({ vis: Tv(3), txt: 'EL <b>SIGUIENTE</b> ES UNO MÁS: <b>' + fmt(v.n + 1) + '</b>.' });
        P.push({ vis: Tv(3) + p1Big(fmt(v.n - 1) + ' · ' + fmt(v.n) + ' · ' + fmt(v.n + 1)), txt: (v.n + 1) % 1000 === 0 ? 'OJO: DESPUÉS DEL ' + fmt(v.n) + ' SE LLENA UN MIL.' : (v.n + 1) % 100 === 0 ? 'OJO: DESPUÉS DEL ' + fmt(v.n) + ' CAMBIAN LAS CENTENAS.' : v.n % 1000 === 0 ? 'OJO: ANTES DEL ' + fmt(v.n) + ' VA UN 999.' : 'EL ANTERIOR VA A LA IZQUIERDA Y EL SIGUIENTE A LA DERECHA.' });
        return P;
      }
      if (md === 'recta10000') {
        var m0 = Math.floor(v.n / 1000) * 1000;
        P.push({ vis: p1R10000([]), txt: 'LA RECTA VA DEL <b>0</b> AL <b>10.000</b>, DE 1.000 EN 1.000.' });
        P.push({ vis: p1R10000([[m0, 'pa', fmt(m0)]]), txt: 'EL ' + fmt(v.n) + ' TIENE ' + m0 / 1000 + ' MILES: EMPEZAMOS EN EL <b>' + fmt(m0) + '</b>.' });
        P.push({ vis: p1R10000([[m0, 'pa', fmt(m0)], [v.n, 'pb']]), txt: v.n === m0 ? 'ESTÁ JUSTO EN LA MARCA.' : 'ESTÁ ENTRE EL <b>' + fmt(m0) + '</b> Y EL <b>' + fmt(m0 + 1000) + '</b>.' });
        P.push({ vis: p1R10000([[v.n, 'pb']]) + p1Big('MÁS A LA DERECHA, MÁS GRANDE'), txt: 'LOS DE LA DERECHA SON MAYORES QUE EL ' + fmt(v.n) + '.' });
        return P;
      }
      if (md === 'valor4') {
        var n4 = v.m * 1000 + v.c * 100 + v.d * 10 + v.u, VL = [v.m * 1000, v.c * 100, v.d * 10, v.u], NL = ['MILES', 'CENTENAS', 'DECENAS', 'UNIDADES'], CF = [v.m, v.c, v.d, v.u];
        P.push({ vis: p1CDUt(n4), txt: 'EL <b>' + fmt(n4) + '</b> TIENE CUATRO CIFRAS.' });
        for (i = 0; i < 4; i++) P.push({ vis: p1CDUt(n4, i) + p1Big(CF[i] + ' ' + NL[i] + ' = ' + fmt(VL[i])), txt: 'EL <b>' + CF[i] + '</b> ESTÁ EN ' + (i ? 'LAS ' : 'LOS ') + NL[i] + ': VALE <b>' + fmt(VL[i]) + '</b>.' });
        P.push({ vis: p1CDUt(n4, 9) + p1Big(fmt(n4) + ' = ' + VL.map(fmt).join(' + ')), txt: 'LO ARMAMOS CON UNA <b>SUMA</b>: CADA CIFRA VALE SEGÚN SU LUGAR.' });
        return P;
      }
      if (md === 'armar4') {
        var TJ = [v.a, v.b, v.c, v.d], TA = TJ.slice().sort(function (x, y) { return y - x; }), TB = TA.slice().reverse(), menor = p.que === 'menor', TF = menor ? TB : TA;
        var Tt = function (L, k) { return '<div class="lb-p1-tren">' + L.map(function (x, i) { return '<span class="lb-p1-vag' + (i < k ? ' on' : '') + '">' + x + '</span>'; }).join('') + '</div>'; };
        P.push({ vis: Tt(TJ, 0), txt: 'TENEMOS CUATRO TARJETAS. QUEREMOS EL NÚMERO MÁS <b>' + (menor ? 'CHICO' : 'GRANDE') + '</b>.' });
        P.push({ vis: Tt(TF.slice(0, 1), 1), txt: 'EN LOS MILES VA LA CIFRA MÁS <b>' + (menor ? 'CHICA' : 'GRANDE') + '</b>: EL ' + TF[0] + '.' });
        P.push({ vis: Tt(TF.slice(0, 2), 2), txt: 'EN LAS CENTENAS, LA QUE SIGUE: EL ' + TF[1] + '.' });
        P.push({ vis: Tt(TF, 4) + p1Big(fmt(Number(TF.join('')))), txt: 'COMPLETAMOS: <b>' + fmt(Number(TF.join(''))) + '</b>.' });
        return P;
      }
      if (md === 'cambia4') {
        var a4 = p.op || 1000, r4 = v.n + a4, ps4 = [1000, 100, 10, 1].indexOf(a4), NM4 = ['UN MIL', 'UNA CENTENA', 'UNA DECENA', 'UNA UNIDAD'];
        P.push({ vis: p1CDUt(v.n), txt: 'TENEMOS EL <b>' + fmt(v.n) + '</b>.' });
        P.push({ vis: p1CDUt(v.n, ps4), txt: 'SUMAMOS <b>' + NM4[ps4] + '</b>: + ' + fmt(a4) + '.' });
        P.push({ vis: p1CDUt(r4, ps4) + p1Big(fmt(v.n) + ' + ' + fmt(a4) + ' = ' + fmt(r4)), txt: 'CAMBIA LA CIFRA DE ' + ['LOS MILES', 'LAS CENTENAS', 'LAS DECENAS', 'LAS UNIDADES'][ps4] + (String(r4)[ps4] === '0' ? ' (Y SE PASA A LA DE AL LADO).' : '. LAS DEMÁS QUEDAN IGUAL.') });
        return P;
      }
      if (md === 'dinero2') {
        var qd3 = p.que || 'contar';
        if (qd3 === 'contar') {
          var vs3 = [], k3; for (k3 = 0; k3 < v.q; k3++) vs3.push(500); for (k3 = 0; k3 < v.d; k3++) vs3.push(200); for (k3 = 0; k3 < v.c; k3++) vs3.push(100); for (k3 = 0; k3 < v.m; k3++) vs3.push(50);
          if (!vs3.length) { P.push({ vis: p1Big('NO HAY DINERO'), txt: 'SUBÍ ALGÚN BILLETE.' }); return P; }
          P.push({ vis: p1Plata(vs3), txt: 'EL NÚMERO DE CADA BILLETE DICE <b>CUÁNTO VALE</b>.' });
          for (i = 1; i <= vs3.length; i++) P.push({ vis: p1Plata(vs3, i), txt: (i === 1 ? 'EMPEZAMOS POR EL QUE MÁS VALE: <b>' : 'SUMAMOS $' + vs3[i - 1] + ': <b>') + vs3.slice(0, i).reduce(function (x, y) { return x + y; }, 0) + '</b>.' });
          var t3 = vs3.reduce(function (x, y) { return x + y; }, 0);
          P.push({ vis: p1Plata(vs3, vs3.length) + p1Big('EN TOTAL $' + t3), txt: 'EN TOTAL HAY <b>$' + t3 + '</b>.' });
          return P;
        }
        if (qd3 === 'vuelto') {
          var pg = v.n <= 100 ? 100 : v.n <= 200 ? 200 : 500, sal = [], x3 = v.n; while (x3 < pg) { var st = (x3 % 100) ? (x3 % 50 ? 10 : 50) : 100; if (x3 + st > pg) st = 10; x3 += st; sal.push(x3); }
          P.push({ vis: p1Big('CUESTA $' + v.n + ' · PAGÁS $' + pg), txt: 'PAGAMOS CON MÁS: NOS <b>DEVUELVEN</b> DINERO.' });
          P.push({ vis: p1Big('$' + v.n + ' → ' + sal.map(function (x) { return '$' + x; }).join(' → ')), txt: 'CONTAMOS <b>PARA ADELANTE</b> DESDE EL PRECIO HASTA LO QUE PAGAMOS.' });
          P.push({ vis: p1Big('TE DEVUELVEN $' + (pg - v.n)), txt: 'DE ' + v.n + ' A ' + pg + ' HAY <b>' + (pg - v.n) + '</b>: ES LO QUE TE DEVUELVEN.' });
          return P;
        }
        if (qd3 === 'sumar') {
          P.push({ vis: '<div class="lb-p1-dos"><div class="lb-p1-pre">🧃<b>$' + v.a + '</b></div><div class="lb-p1-pre">⚽<b>$' + v.b + '</b></div></div>', txt: 'QUEREMOS COMPRAR LAS <b>DOS</b> COSAS.' });
          P.push({ vis: p1Big('$' + v.a + ' + $' + v.b), txt: 'SUMAMOS LOS PRECIOS.' });
          P.push({ vis: p1Big('$' + v.a + ' + $' + v.b + ' = $' + (v.a + v.b)), txt: 'JUNTAS CUESTAN <b>$' + (v.a + v.b) + '</b>.' });
          return P;
        }
        var Gc3 = function (h) { return '<div class="lb-p1-dos"><div class="lb-p1-pre' + (h === v.a ? ' on' : '') + '">🧃<b>$' + v.a + '</b></div><div class="lb-p1-pre' + (h === v.b ? ' on' : '') + '">⚽<b>$' + v.b + '</b></div></div>'; };
        P.push({ vis: Gc3(), txt: 'COMPARAMOS LOS PRECIOS COMO NÚMEROS: PRIMERO LAS CENTENAS.' });
        if (v.a === v.b) { P.push({ vis: Gc3() + p1Big('CUESTAN IGUAL'), txt: 'TIENEN EL MISMO PRECIO.' }); return P; }
        P.push({ vis: Gc3(Math.max(v.a, v.b)), txt: '<b>$' + Math.max(v.a, v.b) + '</b> ES EL MÁS <b>CARO</b>.' });
        P.push({ vis: Gc3(Math.min(v.a, v.b)) + p1Big('$' + Math.min(v.a, v.b) + ' ES MÁS BARATO'), txt: '<b>$' + Math.min(v.a, v.b) + '</b> ES EL MÁS <b>BARATO</b>.' });
        return P;
      }
      if (md === 'mental') {
        var qm = p.que || 'chica', esc = p.esc || 100, Mm = p1Ment(qm, p.op, v.a, v.b, esc), cu = Mm.a + ' ' + Mm.sg + ' ' + Mm.b;
        P.push({ vis: p1Big(cu + ' = ?'), txt: 'LO HACEMOS <b>EN LA CABEZA</b>, SIN CUENTA ESCRITA.' });
        if (qm === 'chica') {
          P.push({ vis: p1Big(Mm.ca + ' ' + Mm.sg + ' ' + Mm.cb + ' = ' + (Mm.r / esc)), txt: 'PENSAMOS LA <b>CUENTA CHICA</b>: ' + Mm.ca + ' ' + Mm.sg + ' ' + Mm.cb + ' = ' + (Mm.r / esc) + '.' });
          P.push({ vis: p1Big(cu + ' = ' + Mm.r), txt: 'SON ' + (Mm.r / esc) + ' ' + (esc === 100 ? 'CAJAS DE 100' : 'PAQUETES DE 10') + ': <b>' + Mm.r + '</b>.' });
          return P;
        }
        if (qm === 'falta100') { var base = p.op === 'resta' ? Mm.b : Mm.a, Lf = []; for (i = base; i <= 100; i += 10) Lf.push(i);
          P.push({ vis: '<div class="lb-p1-tren">' + Lf.map(function (x, k) { return '<span class="lb-p1-vag' + (k ? ' sig' : ' on') + '">' + x + '</span>'; }).join('') + '</div>', txt: 'CONTAMOS DE 10 EN 10 DESDE EL <b>' + base + '</b> HASTA EL 100.' });
          P.push({ vis: p1Big(cu + ' = ' + Mm.r), txt: 'SON ' + (Lf.length - 1) + ' SALTOS DE 10: <b>' + Mm.r + '</b>. ' + (Mm.r / 10) + ' + ' + (base / 10) + ' = 10.' });
          return P; }
        if (qm === 'desarmar') {
          var NP = ['CENTENAS', 'DECENAS', 'UNIDADES'], acc = [];
          Mm.p.forEach(function (pp, k) { var rr = p.op === 'resta' ? pp[0] - pp[1] : pp[0] + pp[1]; acc.push(rr); P.push({ vis: p1Big(pp[1] ? pp[0] + ' ' + Mm.sg + ' ' + pp[1] + ' = ' + rr : pp[0]), txt: (k ? 'AHORA LAS <b>' : 'PRIMERO LAS <b>') + NP[k] + '</b>' + (pp[1] ? ': ' + pp[0] + ' ' + Mm.sg + ' ' + pp[1] + ' = ' + rr + '.' : ': QUEDAN ' + pp[0] + '.') }); });
          P.push({ vis: p1Big(acc.join(' + ') + ' = ' + Mm.r), txt: 'JUNTAMOS LAS PARTES: <b>' + cu + ' = ' + Mm.r + '</b>.' });
          return P; }
        var sb3 = p.op === 'resta' ? -v.b : v.b, nn3 = v.a + sb3;
        P.push({ vis: p1CDUt(v.a, v.b === 100 ? 0 : 1), txt: (sb3 > 0 ? 'SUMAR ' : 'RESTAR ') + v.b + ' CAMBIA LA CIFRA DE LAS <b>' + (v.b === 100 ? 'CENTENAS' : 'DECENAS') + '</b>.' });
        P.push({ vis: p1CDUt(nn3, v.b === 100 ? 0 : 1) + p1Big(v.a + (sb3 > 0 ? ' + ' : ' − ') + v.b + ' = ' + nn3), txt: 'LAS OTRAS CIFRAS QUEDAN IGUAL: <b>' + nn3 + '</b>.' });
        return P;
      }
      if (md === 'columna') {
        var rsC = p.op === 'resta', aC = v.a, bC = v.b, sgC = rsC ? '−' : '+';
        if (rsC && bC > aC) { var tC = aC; aC = bC; bC = tC; } if (!rsC && aC + bC > 999) bC = 999 - aC; if (rsC && aC === bC) bC = Math.max(10, bC - 11);
        var dA = String(aC).padStart(3, '0').split('').map(Number), dB = String(bC).padStart(3, '0').split('').map(Number), out = ['', '', ''], lv = ['', '', ''], car = 0, NMc = ['CENTENAS', 'DECENAS', 'UNIDADES'], resN = rsC ? aC - bC : aC + bC;
        P.push({ vis: p1Col3(aC, bC, sgC, '', -1), txt: 'PONEMOS ' + (rsC ? 'EL MÁS GRANDE ARRIBA Y ' : '') + 'CADA CIFRA EN SU <b>COLUMNA</b>: UNIDADES DEBAJO DE UNIDADES.' });
        for (var cI = 2; cI >= 0; cI--) {
          var x1 = dA[cI], x2 = dB[cI], txC;
          if (!rsC) { var sm = x1 + x2 + car; txC = (car ? x1 + ' + ' + x2 + ' + 1 (QUE ME LLEVÉ) = ' : x1 + ' + ' + x2 + ' = ') + sm; car = sm > 9 && cI > 0 ? 1 : 0; out[cI] = cI === 0 ? String(sm) : String(sm % 10); if (car) { lv[cI - 1] = '1'; txC += ': ESCRIBO ' + (sm % 10) + ' Y <b>ME LLEVO 1</b>.'; } else txC += '.'; }
          else { var top = x1 - car, cj = top < x2; if (cj) { top += 10; lv[cI] = String(top); if (cI > 0) lv[cI - 1] = '−1'; } txC = (cj ? 'NO ALCANZA: ABRO UN PAQUETE Y TENGO ' + top + '. ' : '') + top + ' − ' + x2 + ' = ' + (top - x2) + '.'; out[cI] = String(top - x2); car = cj ? 1 : 0; }
          var parc = out.join(''); P.push({ vis: p1Col3(aC, bC, sgC, parc, cI, lv.slice()), txt: 'LAS <b>' + NMc[cI] + '</b>: ' + txC });
        }
        P.push({ vis: p1Col3(aC, bC, sgC, resN, -1, lv) + p1Big(aC + ' ' + sgC + ' ' + bC + ' = ' + resN), txt: 'EL RESULTADO ES <b>' + resN + '</b>.' });
        return P;
      }
      if (md === 'prop') {
        var qp = p.que || 'conmuta';
        if (qp === 'conmuta') {
          P.push({ vis: p1Big(v.a + ' + ' + v.b), txt: 'QUEREMOS SUMAR <b>' + v.a + ' + ' + v.b + '</b>.' });
          P.push({ vis: p1Big(v.b + ' + ' + v.a), txt: 'EN LA SUMA EL <b>ORDEN NO IMPORTA</b>: LA DAMOS VUELTA.' });
          var Lc = []; for (i = 1; i <= v.a; i++) Lc.push(v.b + i);
          P.push({ vis: p1Big(v.b + '… ' + Lc.join(', ')), txt: 'EMPEZAMOS POR EL <b>GRANDE</b> Y CONTAMOS ' + v.a + ' MÁS.' });
          P.push({ vis: p1Big(v.a + ' + ' + v.b + ' = ' + v.b + ' + ' + v.a + ' = ' + (v.a + v.b)), txt: 'DA LO MISMO: <b>' + (v.a + v.b) + '</b>. EN LA RESTA, EN CAMBIO, NO SE PUEDE DAR VUELTA.' });
          return P;
        }
        if (qp === 'amigos') {
          var cA = (10 - v.a % 10) % 10 || 10, rd = v.a + cA;
          P.push({ vis: p1Big(v.a + ' + ' + v.b + ' + ' + cA), txt: 'TENEMOS QUE SUMAR <b>TRES</b> NÚMEROS.' });
          P.push({ vis: p1Big('(' + v.a + ' + ' + cA + ') + ' + v.b), txt: 'BUSCAMOS <b>AMIGOS</b>: ' + v.a + ' Y ' + cA + ' FORMAN UN REDONDO.' });
          P.push({ vis: p1Big(rd + ' + ' + v.b), txt: v.a + ' + ' + cA + ' = <b>' + rd + '</b>.' });
          P.push({ vis: p1Big(rd + ' + ' + v.b + ' = ' + (rd + v.b)), txt: 'SUMAMOS LO QUE QUEDA: <b>' + (rd + v.b) + '</b>.' });
          return P;
        }
        if (qp === 'dobles') {
          P.push({ vis: p1Big(v.a + ' + ' + v.a + ' = ' + 2 * v.a), txt: 'EMPEZAMOS CON UN DOBLE QUE SABEMOS: <b>' + 2 * v.a + '</b>.' });
          P.push({ vis: p1Big(v.a + ' + ' + (v.a + 1) + ' = ' + (2 * v.a + 1)), txt: 'SI UNO TIENE <b>UNO MÁS</b>, EL RESULTADO TIENE UNO MÁS.' });
          P.push({ vis: p1Big(v.a + ' + ' + (v.a - 1) + ' = ' + (2 * v.a - 1)), txt: 'SI TIENE <b>UNO MENOS</b>, EL RESULTADO TIENE UNO MENOS.' });
          P.push({ vis: p1Big(v.a + ' + ' + (v.a + 10) + ' = ' + (2 * v.a + 10)), txt: 'Y SI TIENE <b>DIEZ MÁS</b>, DA DIEZ MÁS.' });
          return P;
        }
        var cF = v.a + v.b, Fm = [v.a + ' + ' + v.b + ' = ' + cF, v.b + ' + ' + v.a + ' = ' + cF, cF + ' − ' + v.b + ' = ' + v.a, cF + ' − ' + v.a + ' = ' + v.b];
        P.push({ vis: p1Big(v.a + ', ' + v.b + ' Y ' + cF), txt: 'ESTOS TRES NÚMEROS FORMAN UNA <b>FAMILIA</b> DE CUENTAS.' });
        for (i = 1; i <= 4; i++) P.push({ vis: '<div class="lb-p1-tab">' + Fm.slice(0, i).map(function (x, k) { return '<span' + (k === i - 1 ? ' class="on"' : '') + '>' + x + '</span>'; }).join('') + '</div>', txt: i <= 2 ? 'DOS <b>SUMAS</b>: EL ORDEN NO IMPORTA.' : 'DOS <b>RESTAS</b>: LA RESTA DESHACE LA SUMA.' });
        return P;
      }
      if (md === 'mult') {
        var qx = p.que || 'grupos', ox = pick(['caramelo', 'pelota', 'estrella', 'manzana']);
        if (qx === 'grupos' || qx === 'signo') {
          var Gx = function (k) { var h2 = ''; for (var j2 = 0; j2 < v.g; j2++) h2 += p1Grupo('', v.n, ox, j2 < k ? { hasta: v.n } : null); return h2; }, sm = [];
          P.push({ vis: Gx(0), txt: 'HAY <b>' + v.g + '</b> GRUPOS IGUALES Y CADA UNO TIENE <b>' + v.n + '</b>.' });
          for (i = 1; i <= v.g; i++) { sm.push(v.n); P.push({ vis: Gx(i) + p1Big(sm.join(' + ')), txt: 'SUMAMOS OTRO ' + v.n + ': <b>' + v.n * i + '</b>.' }); }
          if (qx === 'signo') P.push({ vis: p1Big(sm.join(' + ') + ' = ' + v.g + ' × ' + v.n), txt: 'SUMAR ' + v.g + ' VECES EL ' + v.n + ' SE ESCRIBE <b>' + v.g + ' × ' + v.n + '</b>: SE LEE ' + v.g + ' POR ' + v.n + '.' });
          P.push({ vis: p1Big((qx === 'signo' ? v.g + ' × ' + v.n : sm.join(' + ')) + ' = ' + v.g * v.n), txt: 'EN TOTAL HAY <b>' + v.g * v.n + '</b>.' });
          return P;
        }
        P.push({ vis: p1Arr(v.f, v.c, ox), txt: 'UN <b>ARREGLO</b>: TODAS LAS FILAS TIENEN LO MISMO.' });
        P.push({ vis: p1Arr(v.f, v.c, ox, { fila: 0 }), txt: 'UNA <b>FILA</b> VA ACOSTADA: TIENE <b>' + v.c + '</b>.' });
        P.push({ vis: p1Arr(v.f, v.c, ox, { col: 0 }), txt: 'UNA <b>COLUMNA</b> VA PARADA: HAY <b>' + v.f + '</b> FILAS.' });
        for (i = 1; i <= v.f; i++) P.push({ vis: p1Arr(v.f, v.c, ox, { hasta: i }), txt: 'CONTAMOS FILA POR FILA: <b>' + v.c * i + '</b>.' });
        P.push({ vis: p1Arr(v.f, v.c, ox, { hasta: v.f }) + p1Big(v.f + ' × ' + v.c + ' = ' + v.f * v.c), txt: '<b>FILAS × COLUMNAS</b>: ' + v.f + ' × ' + v.c + ' = ' + v.f * v.c + '.' });
        if (qx === 'girar') P.push({ vis: p1Arr(v.c, v.f, ox) + p1Big(v.c + ' × ' + v.f + ' = ' + v.f * v.c), txt: 'SI LO <b>GIRAMOS</b>, CAMBIAN FILAS Y COLUMNAS PERO EL TOTAL ES EL MISMO.' });
        return P;
      }
      if (md === 'por10') {
        var de10 = p.de || 10, rz = v.n * de10, ceros = de10 === 100 ? '00' : '0';
        if (p.que === 'cifras') {
          P.push({ vis: p1CDUt(v.n), txt: 'EL <b>' + v.n + '</b> TIENE ESTAS CIFRAS.' });
          P.push({ vis: p1CDUt(rz, 9), txt: 'POR ' + de10 + ': CADA CIFRA SE CORRE ' + (de10 === 100 ? 'DOS LUGARES' : 'UN LUGAR') + ' A LA IZQUIERDA.' });
          P.push({ vis: p1CDUt(rz, 9) + p1Big(v.n + ' × ' + de10 + ' = ' + rz), txt: 'Y EN EL LUGAR QUE QUEDA VACÍO VA <b>' + (de10 === 100 ? 'DOS CEROS' : 'UN CERO') + '</b>.' });
          return P;
        }
        P.push({ vis: de10 === 100 ? p1CDU(v.n * 100) : p1BolsasN(v.n), txt: 'TENEMOS <b>' + v.n + '</b> ' + (de10 === 100 ? 'CAJAS DE 100' : 'PAQUETES DE 10') + '.' });
        P.push({ vis: (de10 === 100 ? p1CDU(v.n * 100, { c: v.n }) : p1BolsasN(v.n)) + p1Big(v.n + ' × ' + de10), txt: 'ES <b>' + v.n + ' VECES ' + de10 + '</b>: ' + v.n + ' × ' + de10 + '.' });
        P.push({ vis: p1Big(v.n + ' → ' + v.n + '<span style="color:#C2552E">' + ceros + '</span>'), txt: 'TRUCO: AL ' + v.n + ' LE AGREGAMOS <b>' + (de10 === 100 ? 'DOS CEROS' : 'UN CERO') + '</b>.' });
        P.push({ vis: p1Big(v.n + ' × ' + de10 + ' = ' + rz), txt: v.n + ' × ' + de10 + ' = <b>' + rz + '</b>.' });
        return P;
      }
      if (md === 'miles') {
        var nM = v.m * 1000 + v.c * 100 + v.d * 10 + v.u, fM = function (x) { return H.fmt ? H.fmt(x) : String(x); }, qM = p.que || 'contar';
        if (qM === 'contar') {
          P.push({ vis: p1CDU(nM), txt: 'UN CAMIÓN TIENE <b>1.000</b>: SON 10 CAJAS DE 100.' });
          P.push({ vis: p1CDU(nM, { m: v.m }), txt: 'CONTAMOS LOS CAMIONES DE 1.000 EN 1.000: <b>' + fM(v.m * 1000) + '</b>.' });
          if (v.c) P.push({ vis: p1CDU(nM, { m: v.m, c: v.c }), txt: 'SEGUIMOS CON LAS CAJAS DE 100 EN 100: <b>' + fM(v.m * 1000 + v.c * 100) + '</b>.' });
          if (v.d || v.u) P.push({ vis: p1CDU(nM, { m: v.m, c: v.c, d: v.d, u: v.u }), txt: 'Y LOS PAQUETES Y SUELTOS: <b>' + fM(nM) + '</b>.' });
          P.push({ vis: p1CDU(nM, { m: v.m, c: v.c, d: v.d, u: v.u }) + p1Big('HAY ' + fM(nM)), txt: 'EN TOTAL HAY <b>' + fM(nM) + '</b>.' });
          return P;
        }
        P.push({ vis: p1CDUt(nM, 0), txt: 'LOS CAMIONES SON <b>MILES</b>: VAN PRIMERO.' });
        P.push({ vis: p1CDUt(nM, 1), txt: 'DESPUÉS LAS <b>CENTENAS</b>.' });
        P.push({ vis: p1CDUt(nM, 2), txt: v.d ? 'DESPUÉS LAS <b>DECENAS</b>.' : 'NO HAY DECENAS: EL <b>0</b> GUARDA SU LUGAR.' });
        P.push({ vis: p1CDUt(nM, 3), txt: 'AL FINAL LAS <b>UNIDADES</b>.' });
        P.push({ vis: p1CDUt(nM, 9) + p1Big(fM(nM)), txt: 'SE ESCRIBE <b>' + fM(nM) + '</b> Y SE LEE <b>' + p1Up(nM) + '</b>.' });
        return P;
      }
      if (md === 'saltos') {
        var de2 = p.de || 2, hs = Math.ceil(v.n / 10) * 10, ya = [0];
        P.push({ vis: p1Cuadro(hs, p1Marca([0], 'on')), txt: 'EMPEZAMOS EN EL <b>0</b>. VAMOS A SALTAR DE A <b>' + de2 + '</b>.' });
        for (i = de2; i <= v.n; i += de2) { ya.push(i); P.push({ vis: p1Cuadro(hs, p1Marca(ya.slice(0, -1), 'fila', p1Marca([i], 'on'))), txt: 'SALTAMOS ' + de2 + ' Y CAEMOS EN EL <b>' + i + '</b>.' }); }
        P.push({ vis: p1Cuadro(hs, p1Marca(ya, 'on')) + p1Big(ya.slice(1, 6).join(', ') + '…'), txt: 'CONTAMOS DE A <b>' + de2 + '</b>: NO DECIMOS LOS DE EN MEDIO.' });
        return P;
      }
      return [{ vis: '', txt: '' }];
    });
  } };

  // Práctica de primer grado: elegir una opción tocándola (fichas grandes) o escribir un número
  function p1Elegir(el, api, datos) {
    H.ejercicio(el, api, '', function (c) {
      var D = datos(), sel = null; el.querySelector('.lb-cons').innerHTML = D.cons;
      c.innerHTML = (D.html || '') + '<div class="lb-p1-ops">' + D.ops.map(function (x, i) { return '<button type="button" class="lb-p1-op" data-op="' + i + '">' + x + '</button>'; }).join('') + '</div>';
      c.addEventListener('click', function (e) { var b = e.target.closest('[data-op]'); if (!b) return; [].forEach.call(c.querySelectorAll('[data-op]'), function (x) { x.classList.remove('on'); }); b.classList.add('on'); sel = Number(b.getAttribute('data-op')); });
      return {
        comprobar: function () { if (sel === null) return { ok: false, msg: 'Tocá una opción.' }; return D.ops[sel] === D.ok ? { ok: true, msg: D.bien || '¡MUY BIEN!' } : { ok: false, msg: D.ayuda || 'MIRÁ DE NUEVO.' }; },
        resolver: function () { var k = D.ops.indexOf(D.ok); [].forEach.call(c.querySelectorAll('[data-op]'), function (x) { x.classList.toggle('on', Number(x.getAttribute('data-op')) === k); }); sel = k; }
      };
    });
  }
  M.primeros_x = { tipo: 'ejercicio', render: function (el, p, api) {
    var md = p.modo || 'contar';
    if (md === 'contar') return respuesta(el, api, function () { var o = p1Obj(), n = R(p.min || 3, p.max || 8);
      return { cons: '¿' + g(o, 'CUÁNTAS ', 'CUÁNTOS ') + P1PL[o] + ' HAY? CONTÁ CON EL DEDO.', html: p1Fila(n, o), campos: [{ v: n }], ayuda: 'TOCÁ CADA ' + g(o, 'UNA', 'UNO') + ' UNA SOLA VEZ Y DECÍ UN NÚMERO.', bien: '¡MUY BIEN! HAY ' + n + '.' }; });
    if (md === 'grupo') return p1Elegir(el, api, function () { var o = p1Obj(), ns = mezclar([2, 3, 4, 5, 6, 7, 8]).slice(0, 3), n = pick(ns), op = ns.map(function (k) { return Array(k + 1).join(P1E[o]); });
      return { cons: '¿EN QUÉ GRUPO HAY <b>' + n + '</b>?', ops: op, ok: Array(n + 1).join(P1E[o]), ayuda: 'CONTÁ CADA GRUPO: EL ÚLTIMO NÚMERO DICE CUÁNTOS HAY.', bien: '¡MUY BIEN! ESE GRUPO TIENE ' + n + '.' }; });
    if (md === 'mas_menos' || md === 'igual') return p1Elegir(el, api, function () {
      var o = p1Obj(), nm = pick(P1NOM), a = R(1, 8), b = md === 'igual' && Math.random() < 0.4 ? a : R(1, 8); if (md === 'mas_menos') while (b === a) b = R(1, 8);
      var mas = Math.random() < 0.5, ok = a === b ? 'TIENEN IGUAL' : ((a > b) === mas ? nm[0] : nm[1]), ops = md === 'igual' ? [nm[0], nm[1], 'TIENEN IGUAL'] : [nm[0], nm[1]];
      return { cons: '¿QUIÉN TIENE <b>' + (mas ? 'MÁS' : 'MENOS') + '</b>?', html: p1Grupo(nm[0], a, o) + p1Grupo(nm[1], b, o), ops: ops, ok: ok, ayuda: 'CONTÁ LOS DOS GRUPOS Y COMPARÁ LOS NÚMEROS.', bien: a === b ? '¡MUY BIEN! LOS DOS TIENEN ' + a + '.' : '¡MUY BIEN! ' + nm[0] + ' TIENE ' + a + ' Y ' + nm[1] + ' TIENE ' + b + '.' }; });
    if (md === 'parejas') return respuesta(el, api, function () { var pr = pick(P1PARES), a = R(2, 7), b = R(2, 7); while (b === a) b = R(2, 7); var sob = b > a;
      return { cons: 'UNÍ CADA UNO CON SU PAREJA. ¿' + g(pr[1], 'CUÁNTAS ', 'CUÁNTOS ') + P1PL[pr[1]] + ' <b>' + (sob ? 'SOBRAN' : 'FALTAN') + '</b>?', html: p1Parejas(a, pr[0], b, pr[1], 0), campos: [{ v: Math.abs(a - b) }], ayuda: 'ARMÁ LAS PAREJAS CON EL DEDO Y MIRÁ CUÁNTOS QUEDAN SIN PAREJA.', bien: '¡MUY BIEN! ' + (sob ? 'SOBRAN ' : 'FALTAN ') + Math.abs(a - b) + '.' }; });
    if (md === 'alcanza') return p1Elegir(el, api, function () { var pr = pick(P1PARES), a = R(2, 7), r = Math.random(), b = r < 0.33 ? a : r < 0.66 ? Math.min(8, a + R(1, 2)) : Math.max(1, a - R(1, 2)), pl = P1PL[pr[1]];
      var ok = a === b ? 'HAY IGUAL' : b > a ? 'SOBRAN ' + pl : 'FALTAN ' + pl;
      return { cons: '¿ALCANZAN ' + g(pr[1], 'LAS ', 'LOS ') + pl + ' PARA ' + g(pr[0], 'LAS ', 'LOS ') + P1PL[pr[0]] + '?', html: p1Parejas(a, pr[0], b, pr[1], 0), ops: ['SOBRAN ' + pl, 'FALTAN ' + pl, 'HAY IGUAL'], ok: ok, ayuda: 'UNÍ UNO CON UNO: ¿QUEDA ALGUNO SIN PAREJA?', bien: '¡MUY BIEN!' }; });
    if (md === 'agregar' || md === 'quitar') return respuesta(el, api, function () { var o = p1Obj(), a = R(3, 9), b = R(1, 8); while (b >= a) { a = R(3, 9); b = R(1, 8); } var ag = md === 'agregar';
      return { cons: ag ? '¿' + g(o, 'CUÁNTAS ', 'CUÁNTOS ') + P1PL[o] + ' LE <b>AGREGÁS</b> AL GRUPO 2 PARA QUE HAYA IGUAL?' : '¿' + g(o, 'CUÁNTAS ', 'CUÁNTOS ') + P1PL[o] + ' LE <b>QUITÁS</b> AL GRUPO 1 PARA QUE HAYA IGUAL?', html: p1Grupo('GRUPO 1', a, o) + p1Grupo('GRUPO 2', b, o), campos: [{ v: a - b }], ayuda: ag ? 'AGREGÁ DE A ' + g(o, 'UNA', 'UNO') + ' AL GRUPO 2 HASTA LLEGAR A ' + a + '.' : 'QUITÁ DE A ' + g(o, 'UNA', 'UNO') + ' AL GRUPO 1 HASTA LLEGAR A ' + b + '.', bien: '¡MUY BIEN! ' + (ag ? 'AGREGANDO ' : 'QUITANDO ') + (a - b) + ' QUEDAN ' + (ag ? a + ' Y ' + a : b + ' Y ' + b) + '.' }; });
    if (md === 'falta') return respuesta(el, api, function () { var de = p.desde || 1, ha = p.hasta || 10, ini = R(de, ha - 4), f = ini + R(1, 3), op = {}; op[f] = 'oculto';
      return { cons: '¿QUÉ NÚMERO FALTA EN EL TREN?', html: p1Tren(ini, ini + 4, op), campos: [{ v: f }], ayuda: 'MIRÁ EL VAGÓN DE ANTES: EL QUE FALTA VIENE DESPUÉS.', bien: '¡MUY BIEN! DESPUÉS DEL ' + (f - 1) + ' VIENE EL ' + f + '.' }; });
    if (md === 'decena') return respuesta(el, api, function () { var o = pick(['caramelo', 'estrella', 'pelota']), s = R(1, 10);
      return { cons: 'UNA CAJA DE 10 Y ALGUNOS SUELTOS. ¿CUÁNTOS SON EN TOTAL?', html: p1Caja(o, s), campos: [{ v: 10 + s }], ayuda: 'NO CUENTES LA CAJA: ARRANCÁ EN 10 Y SEGUÍ CON LOS SUELTOS.', bien: '¡MUY BIEN! 10 Y ' + s + ' SON ' + (10 + s) + '.' }; });
    if (md === 'leer') return p1Elegir(el, api, function () { var n = R(11, 20), u = n % 10, ops = mezclar([p1Up(n), p1Up(u || 2), p1Up(u ? u * 10 : 12)]);
      return { cons: '¿CÓMO SE LEE ESTE NÚMERO?', html: p1Cifras(n), ops: ops, ok: p1Up(n), ayuda: 'MIRÁ LAS DOS CIFRAS: EMPIEZA CON ' + String(n)[0] + '.', bien: '¡MUY BIEN! ' + n + ' SE LEE ' + p1Up(n) + '.' }; });
    if (md === 'escribir') return p1Elegir(el, api, function () { var n = R(12, 19), s = String(n), ops = mezclar([s, s[1] + s[0], s[1]]);
      return { cons: '¿CÓMO SE ESCRIBE <b>' + p1Up(n) + '</b>?', ops: ops, ok: s, ayuda: 'ES DIEZ Y ALGO MÁS: PRIMERO VA EL 1.', bien: '¡MUY BIEN! SE ESCRIBE ' + n + '.' }; });
    if (md === 'anterior_siguiente') return respuesta(el, api, function () { var n = R(p.min || 2, p.max || 19), ant = Math.random() < 0.5;
      return { cons: '¿QUÉ NÚMERO VA <b>' + (ant ? 'ANTES' : 'DESPUÉS') + '</b> DEL ' + n + '?', html: p1Big(n), campos: [{ v: ant ? n - 1 : n + 1 }], ayuda: 'PENSÁ EN EL TREN DE LOS NÚMEROS.', bien: '¡MUY BIEN! ' + (ant ? 'EL ANTERIOR DEL ' + n + ' ES EL ' + (n - 1) : 'EL SIGUIENTE DEL ' + n + ' ES EL ' + (n + 1)) + '.' }; });
    if (md === 'mayor_menor') return p1Elegir(el, api, function () { var a = R(0, 20), b = R(0, 20); while (b === a) b = R(0, 20); var may = Math.random() < 0.5;
      return { cons: '¿CUÁL ES <b>' + (may ? 'MAYOR' : 'MENOR') + '</b>?', ops: [String(a), String(b)], ok: String(may ? Math.max(a, b) : Math.min(a, b)), ayuda: may ? 'EL MAYOR ESTÁ MÁS LEJOS DEL 0.' : 'EL MENOR ESTÁ MÁS CERCA DEL 0.', bien: '¡MUY BIEN!' }; });
    if (md === 'cuadro') { var hc = p.hasta || 100, q = p.que || 'falta';
      if (q === 'fila' || q === 'columna') return p1Elegir(el, api, function () { var n = R(10, Math.min(hc, 99)), fil = q === 'fila', ok = fil ? Math.floor(n / 10) : n % 10, lst = fil ? p1Fil(n) : p1Col(n, hc), ops = [ok]; while (ops.length < 3) { var x = R(0, fil ? Math.floor(Math.min(hc, 99) / 10) : 9); if (ops.indexOf(x) < 0) ops.push(x); }
        return { cons: fil ? '¿CON QUÉ CIFRA <b>EMPIEZAN</b> LOS NÚMEROS DE LA FILA MARCADA?' : '¿EN QUÉ CIFRA <b>TERMINAN</b> LOS NÚMEROS DE LA COLUMNA MARCADA?', html: p1Cuadro(hc, p1Marca(lst, 'fila')), ops: mezclar(ops.map(String)), ok: String(ok), ayuda: fil ? 'MIRÁ LA PRIMERA CIFRA DE CADA NÚMERO DE LA FILA.' : 'MIRÁ LA ÚLTIMA CIFRA DE CADA NÚMERO DE LA COLUMNA.', bien: '¡MUY BIEN! ' + (fil ? 'EMPIEZAN CON ' : 'TERMINAN EN ') + ok + '.' }; });
      return respuesta(el, api, function () { var baj = q === 'bajar', n = baj ? R(1, hc - 11) : R(11, hc - 1), f = baj ? n + 10 : n, cl = p1Marca([f], 'oculto'); if (baj) cl[n] = 'on';
        return { cons: baj ? '¿QUÉ NÚMERO VA JUSTO <b>ABAJO</b> DEL ' + n + '?' : '¿QUÉ NÚMERO FALTA EN EL CUADRO?', html: p1Cuadro(hc, cl), campos: [{ v: f }], ayuda: baj ? 'BAJAR UNA FILA ES SUMAR 10.' : 'MIRÁ EL DE ANTES: EL QUE FALTA VIENE DESPUÉS.', bien: '¡MUY BIEN! ES EL ' + f + '.' }; }); }
    if (md === 'saltos') return respuesta(el, api, function () { var de = p.de || pick([2, 5, 10]), ini = de * R(0, 4), s = [], k; for (k = 0; k < 5; k++) s.push(ini + de * k); var f = R(2, 4), op = s.map(function (x, i) { return '<span class="lb-p1-vag' + (i === f ? ' oculto">?' : '">' + x) + '</span>'; }).join('');
      return { cons: 'CONTAMOS DE A <b>' + de + '</b>. ¿QUÉ NÚMERO FALTA?', html: '<div class="lb-p1-tren"><span class="lb-p1-loco">🐸</span>' + op + '</div>', campos: [{ v: s[f] }], ayuda: 'SALTÁ ' + de + ' DESDE EL NÚMERO DE ANTES.', bien: '¡MUY BIEN! ' + s[f - 1] + ' Y ' + de + ' MÁS SON ' + s[f] + '.' }; });
    if (md === 'comparar2') return p1Elegir(el, api, function () { var a = R(10, 99), b = Math.random() < 0.4 ? Math.floor(a / 10) * 10 + R(0, 9) : R(10, 99); while (b === a) b = R(10, 99); var may = Math.random() < 0.5;
      return { cons: '¿CUÁL ES <b>' + (may ? 'MAYOR' : 'MENOR') + '</b>?', ops: [String(a), String(b)], ok: String(may ? Math.max(a, b) : Math.min(a, b)), ayuda: 'MIRÁ PRIMERO LAS DECENAS; SI EMPATAN, LAS UNIDADES.', bien: '¡MUY BIEN!' }; });
    if (md === 'ordenar3') return p1Elegir(el, api, function () { var L = []; while (L.length < 3) { var x = R(10, 99); if (L.indexOf(x) < 0) L.push(x); } var desc = p.orden === 'desc', S = L.slice().sort(function (x, y) { return desc ? y - x : x - y; }), pr = Math.random() < 0.6;
      return { cons: 'DE <b>' + (desc ? 'MAYOR A MENOR' : 'MENOR A MAYOR') + '</b>, ¿CUÁL VA <b>' + (pr ? 'PRIMERO' : 'ÚLTIMO') + '</b>?', ops: L.map(String), ok: String(pr ? S[0] : S[2]), ayuda: (pr ? 'BUSCÁ EL MÁS ' : 'EL ÚLTIMO ES EL MÁS ') + ((pr !== desc) ? 'CHICO.' : 'GRANDE.'), bien: '¡MUY BIEN! ' + S.join(desc ? ', ' : ', ') + '.' }; });
    if (md === 'recta100') { if (p.que === 'saltar') return respuesta(el, api, function () { var at = p.dir === 'atras', a = at ? R(6, 20) : R(0, 14), s2 = R(2, 6), f = at ? a - s2 : a + s2;
        return { cons: 'ESTÁS EN EL <b>' + a + '</b> Y SALTÁS <b>' + s2 + '</b> PARA ' + (at ? 'ATRÁS' : 'ADELANTE') + '. ¿A QUÉ NÚMERO LLEGÁS?', html: p1Recta((function () { var o2 = {}; o2[a] = { c: 'pa', t: 'ESTÁS' }; return o2; })()), campos: [{ v: f }], ayuda: 'CONTÁ LOS SALTOS DE A UNO EN LA RECTA.', bien: '¡MUY BIEN! LLEGÁS AL ' + f + '.' }; });
      return respuesta(el, api, function () { var n = 10 * R(1, 9) + pick([0, 5]);
        return { cons: '¿QUÉ NÚMERO VA EN EL LUGAR DEL <b>?</b>', html: p1R100([[n, 'pb', '?']]), campos: [{ v: n }], ayuda: 'MIRÁ EL REDONDO DE ANTES Y EL DE DESPUÉS.', bien: '¡MUY BIEN! ES EL ' + n + '.' }; }); }
    if (md === 'decenas') { var q4 = p.que || 'contar';
      if (q4 === 'cuantas') return respuesta(el, api, function () { var n = R(11, 99), dec = Math.random() < 0.5;
        return { cons: '¿CUÁNTAS <b>' + (dec ? 'DECENAS' : 'UNIDADES') + '</b> TIENE EL ' + n + '?', html: p1Cifras(n), campos: [{ v: dec ? Math.floor(n / 10) : n % 10 }], ayuda: dec ? 'LAS DECENAS SON LA CIFRA DE LA IZQUIERDA.' : 'LAS UNIDADES SON LA CIFRA DE LA DERECHA.', bien: '¡MUY BIEN!' }; });
      if (q4 === 'desarmar') return respuesta(el, api, function () { var d = R(2, 9), u = R(1, 9), n = d * 10 + u;
        return { cons: 'DESARMÁ EL <b>' + n + '</b>: ' + n + ' = ___ + ___', html: p1DU(n), campos: [{ v: d * 10, lab: n + ' =' }, { v: u, lab: '+' }], ayuda: 'LAS DECENAS VALEN ' + d + ' VECES 10.', bien: '¡MUY BIEN! ' + n + ' = ' + d * 10 + ' + ' + u + '.' }; });
      if (q4 === 'armar') return respuesta(el, api, function () { var d = R(2, 9), u = R(0, 9);
        return { cons: '¿QUÉ NÚMERO ES <b>' + d * 10 + ' + ' + u + '</b>?', campos: [{ v: d * 10 + u }], ayuda: d + ' DECENAS Y ' + u + ' UNIDADES.', bien: '¡MUY BIEN! ES EL ' + (d * 10 + u) + '.' }; });
      return respuesta(el, api, function () { var d = R(1, p.max ? Math.floor(p.max / 10) : 9), u = R(0, 9), n = d * 10 + u;
        return { cons: 'CADA BOLSITA TIENE 10. ¿CUÁNTOS CARAMELOS HAY EN TOTAL?', html: p1Bolsas(n), campos: [{ v: n }], ayuda: 'CONTÁ LAS BOLSITAS DE 10 EN 10 Y DESPUÉS LOS SUELTOS.', bien: '¡MUY BIEN! HAY ' + n + '.' }; }); }
    if (md === 'dinero') { var qd = p.que || 'contar';
      if (qd === 'contar') return respuesta(el, api, function () { var vs = [], k, d = R(0, 3), c = R(0, 1), u = R(0, 4); if (!d && !c && !u) d = 1; for (k = 0; k < d; k++) vs.push(10); for (k = 0; k < c; k++) vs.push(5); for (k = 0; k < u; k++) vs.push(1); vs = mezclar(vs); var t = 10 * d + 5 * c + u;
        return { cons: '¿CUÁNTO DINERO HAY EN TOTAL?', html: p1Plata(vs), campos: [{ v: t, lab: '$' }], ayuda: 'EMPEZÁ POR LO QUE MÁS VALE Y SEGUÍ SUMANDO.', bien: '¡MUY BIEN! HAY $' + t + '.' }; });
      if (qd === 'falta') return respuesta(el, api, function () { var n = R(6, 20), d = R(Math.max(1, n - 6), n - 1);
        return { cons: 'ALGO CUESTA <b>$' + n + '</b>. DAS <b>$' + d + '</b>. ¿CUÁNTO FALTA?', html: p1Tren(d, n), campos: [{ v: n - d, lab: '$' }], ayuda: 'CONTÁ DESDE ' + d + ' HASTA ' + n + '.', bien: '¡MUY BIEN! FALTAN $' + (n - d) + '.' }; });
      if (qd === 'caro') return p1Elegir(el, api, function () { var it = mezclar([['🧃', 'JUGO'], ['🎈', 'GLOBO'], ['⚽', 'PELOTA'], ['🍎', 'MANZANA']]).slice(0, 3), pr = []; while (pr.length < 3) { var x = R(2, 50); if (pr.indexOf(x) < 0) pr.push(x); } var car = Math.random() < 0.5, k = pr.indexOf(car ? Math.max.apply(null, pr) : Math.min.apply(null, pr)), ops = it.map(function (q, i) { return q[0] + ' $' + pr[i]; });
        return { cons: '¿QUÉ ES MÁS <b>' + (car ? 'CARO' : 'BARATO') + '</b>?', ops: ops, ok: ops[k], ayuda: car ? 'BUSCÁ EL PRECIO MÁS GRANDE.' : 'BUSCÁ EL PRECIO MÁS CHICO.', bien: '¡MUY BIEN!' }; });
      return p1Elegir(el, api, function () { var n = R(6, 39), ok = p1Desarmar(n), m1 = p1Desarmar(n + R(1, 5)), m2 = p1Desarmar(Math.max(1, n - R(1, 5))), f = function (l) { return l.map(function (x) { return '$' + x; }).join(' + '); };
        return { cons: 'ALGO CUESTA <b>$' + n + '</b>. ¿CON QUÉ PAGÁS <b>JUSTO</b>?', ops: mezclar([f(ok), f(m1), f(m2)]), ok: f(ok), ayuda: 'SUMÁ CADA OPCIÓN: TIENE QUE DAR ' + n + '.', bien: '¡MUY BIEN! DA JUSTO $' + n + '.' }; }); }
    if (md === 'sumar') { var qs = p.que || 'juntar';
      return respuesta(el, api, function () { var o = p1Obj(), a = R(1, 6), b = R(1, 4), t = a + b, h, c;
        if (qs === 'agregar') { c = 'HABÍA <b>' + a + '</b> ' + P1PL[o] + '. LLEGAN <b>' + b + '</b> MÁS. ¿CUÁNTOS HAY AHORA?'; h = p1Fila(t, o, { nuevo: a }); }
        else if (qs === 'palitos') { c = 'CONTÁ TODOS LOS PALITOS. ¿CUÁNTOS HAY?'; h = p1Grupo('', a, 'palito') + p1Grupo('', b, 'palito'); }
        else if (qs === 'cuenta') { c = '¿CUÁNTO ES <b>' + a + ' + ' + b + '</b>?'; h = p1Big(a + ' + ' + b + ' = ?'); }
        else { c = 'JUNTÁ LOS DOS GRUPOS. ¿CUÁNTOS HAY EN TOTAL?'; h = p1Grupo('', a, o) + p1Grupo('', b, o); }
        return { cons: c, html: h, campos: [{ v: t }], ayuda: qs === 'agregar' ? 'NO EMPIECES DE NUEVO: SEGUÍ CONTANDO DESDE ' + a + '.' : 'CONTÁ TODO JUNTO, DE A UNO.', bien: '¡MUY BIEN! ' + a + ' + ' + b + ' = ' + t + '.' }; }); }
    if (md === 'restar') { var qr = p.que || 'sacar';
      return respuesta(el, api, function () { var o = p1Obj(), a = R(4, 10), b = R(1, a - 1), c, h, r = a - b;
        if (qr === 'comparar') { b = R(2, 9); while (b === a) b = R(2, 9); c = 'HAY <b>' + a + '</b> CHICOS Y <b>' + b + '</b> VASOS. ¿CUÁNTOS ' + (b > a ? 'VASOS' : 'CHICOS') + ' <b>SOBRAN</b>?'; h = p1Parejas(a, 'chico', b, 'vaso', 0); r = Math.abs(a - b); }
        else if (qr === 'atras') { c = 'HABÍA <b>' + a + '</b> ' + P1PL[o] + '. SE VAN <b>' + b + '</b>. CONTÁ PARA ATRÁS: ¿CUÁNTOS QUEDAN?'; h = p1Tren(1, a); }
        else if (qr === 'cuenta') { c = '¿CUÁNTO ES <b>' + a + ' − ' + b + '</b>?'; h = p1Big(a + ' − ' + b + ' = ?'); }
        else { c = 'HAY ' + a + ' ' + P1PL[o] + '. SACAMOS <b>' + b + '</b>. ¿CUÁNTOS QUEDAN?'; h = p1Fila(a, o, { tenue: a - b }); }
        return { cons: c, html: h, campos: [{ v: r }], ayuda: qr === 'comparar' ? 'UNÍ UNO CON UNO Y CONTÁ LOS QUE NO TIENEN PAREJA.' : 'CONTÁ LOS QUE QUEDAN O CONTÁ PARA ATRÁS DESDE ' + a + '.', bien: '¡MUY BIEN! ES ' + r + '.' }; }); }
    if (md === 'diez') { var qz = p.que || 'cuadro';
      if (qz === 'parejas') return p1Elegir(el, api, function () { var a = R(1, 9), ok = a + ' + ' + (10 - a), ops = [ok]; while (ops.length < 3) { var x = R(1, 8), y = R(1, 8); if (x + y !== 10 && ops.indexOf(x + ' + ' + y) < 0) ops.push(x + ' + ' + y); }
        return { cons: '¿QUÉ SUMA DA <b>10</b>?', ops: mezclar(ops), ok: ok, ayuda: 'PENSÁ EN EL CUADRO DE 10: ¿SE LLENA?', bien: '¡MUY BIEN! ' + ok + ' = 10.' }; });
      return respuesta(el, api, function () { var a, b, c, h, r;
        if (qz === 'dados') { a = R(1, 6); b = R(1, 6); r = a + b; c = 'SALE <b>' + a + '</b> Y <b>' + b + '</b>. ¿CUÁNTO ES EN TOTAL?'; h = '<p class="lb-p1-big lb-p1-dado">' + P1DADO[a] + ' ' + P1DADO[b] + '</p>'; }
        else { a = R(1, 9); r = 10 - a; c = qz === 'falta' ? '¿CUÁNTO LE FALTA AL <b>' + a + '</b> PARA LLEGAR A 10?' : '<b>' + a + ' + ___ = 10</b>'; h = p1Diez(a, 0); }
        return { cons: c, html: h, campos: [{ v: r }], ayuda: qz === 'dados' ? 'EMPEZÁ POR EL MÁS GRANDE Y SEGUÍ CONTANDO.' : 'CONTÁ LOS LUGARES VACÍOS DEL CUADRO.', bien: '¡MUY BIEN! ES ' + r + '.' }; }); }
    if (md === 'dobles') { var qb = p.que || 'espejo';
      return respuesta(el, api, function () { var a, c, r, h = '';
        if (qb === 'iguales') { a = R(1, 5); var k = R(2, 3); r = a * k; c = '¿CUÁNTO ES <b>' + Array(k + 1).join(a + ' + ').slice(0, -3) + '</b>?'; for (var j = 0; j < k; j++) h += p1Grupo('', a, 'estrella'); }
        else if (qb === 'casi') { a = R(1, 9); r = 2 * a + 1; c = 'SI <b>' + a + ' + ' + a + ' = ' + 2 * a + '</b>, ¿CUÁNTO ES <b>' + a + ' + ' + (a + 1) + '</b>?'; }
        else { a = R(1, qb === 'tabla' ? 10 : 6); r = 2 * a; c = qb === 'tabla' ? '¿CUÁNTO ES <b>' + a + ' + ' + a + '</b>?' : '¿CUÁL ES EL <b>DOBLE</b> DE ' + a + '?'; if (qb !== 'tabla') h = p1Fila(a, 'manzana'); }
        return { cons: c, html: h, campos: [{ v: r }], ayuda: qb === 'casi' ? 'ES EL DOBLE Y UNO MÁS.' : qb === 'iguales' ? 'SUMÁ EL MISMO NÚMERO VARIAS VECES.' : 'EL DOBLE ES DOS VECES LO MISMO.', bien: '¡MUY BIEN! ES ' + r + '.' }; }); }
    if (md === 'decenas_op') { var qo = p.que || 'sumar';
      return respuesta(el, api, function () { var a, b, c, r, h = '';
        if (qo === 'atras10' || qo === 'contar10') { var at = qo === 'atras10', ini = 10 * R(at ? 5 : 1, at ? 10 : 6), s4 = [], k; for (k = 0; k < 4; k++) s4.push(ini + (at ? -10 : 10) * k); r = s4[3]; c = 'CONTÁ DE 10 EN 10 PARA ' + (at ? 'ATRÁS' : 'ADELANTE') + '. ¿QUÉ NÚMERO SIGUE?'; h = '<div class="lb-p1-tren">' + s4.slice(0, 3).map(function (x) { return '<span class="lb-p1-vag">' + x + '</span>'; }).join('') + '<span class="lb-p1-vag oculto">?</span></div>'; }
        else if (qo === 'restar') { a = R(3, 9); b = R(1, a - 1); r = 10 * (a - b); c = '¿CUÁNTO ES <b>' + a * 10 + ' − ' + b * 10 + '</b>?'; h = p1BolsasN(a, { tenue: a - b }); }
        else { a = R(1, 8); b = R(1, 10 - a); r = 10 * (a + b); c = '¿CUÁNTO ES <b>' + a * 10 + ' + ' + b * 10 + '</b>?'; h = p1BolsasN(a + b, { nuevo: a }); }
        return { cons: c, html: h, campos: [{ v: r }], ayuda: qo.indexOf('10') > 0 ? 'SUMÁ O RESTÁ UNA BOLSITA DE 10.' : 'CONTÁ LAS BOLSITAS Y DESPUÉS PENSÁ CUÁNTO VALEN.', bien: '¡MUY BIEN! ES ' + r + '.' }; }); }
    if (md === 'problema') { var tp = p.tipo || 'juntar';
      if (tp === 'operacion') return p1Elegir(el, api, function () { var t = pick(['juntar', 'agregar', 'quitar', 'comparar', 'falta_resta'].concat(p.esc ? [] : ['avanzar'])), H = p1Hist(t, R(4, 9), R(1, 4), pick(P1NOM), p1Obj(), p.esc || 1);
        return { cons: H.h + ' ' + H.q + '<br><b>¿SE RESUELVE CON UNA SUMA O CON UNA RESTA?</b>', ops: ['SUMA', 'RESTA'], ok: H.op === '+' ? 'SUMA' : 'RESTA', ayuda: 'SI SE JUNTA O LLEGA MÁS, SUMÁS; SI SE VA O COMPARÁS, RESTÁS.', bien: '¡MUY BIEN! ' + H.c + '.' }; });
      return respuesta(el, api, function () { var t = tp === 'mezcla' ? pick(['juntar', 'agregar', 'quitar', 'comparar']) : tp, H = p1Hist(t, R(3, 9), R(1, 6), pick(P1NOM), p1Obj(), p.esc || 1);
        return { cons: H.h + ' ' + H.q, html: H.v, campos: [{ v: H.r }], ayuda: H.w + ': HACÉ UNA ' + (H.op === '+' ? 'SUMA' : 'RESTA') + '.', bien: '¡MUY BIEN! ' + H.c + '.' }; }); }
    if (md === 'calcu') { var qc = p.que || 'teclas';
      if (qc === 'partes') return p1Elegir(el, api, function () { var q = pick([['¿QUÉ TECLA <b>BORRA</b> TODO?', 'C'], ['¿QUÉ TECLA MUESTRA EL <b>RESULTADO</b>?', '='], ['¿QUÉ TECLA SIRVE PARA <b>SUMAR</b>?', '+'], ['¿QUÉ TECLA SIRVE PARA <b>RESTAR</b>?', '−']]);
        return { cons: q[0], html: p1Calc(R(0, 99)), ops: mezclar(['C', '=', '+', '−']), ok: q[1], ayuda: 'MIRÁ LAS TECLAS DE SIGNOS DE LA DERECHA.', bien: '¡MUY BIEN!' }; });
      if (qc === 'controlar') return p1Elegir(el, api, function () { var a = 10 * R(1, 5), b = R(1, 9), bien = Math.random() < 0.4, mostr = bien ? a + b : Number(String(a) + String(b)) === a + b ? a + b + 10 : (Math.random() < 0.5 ? Number(String(a) + String(b)) : a + b + 10);
        return { cons: 'LA CALCULADORA DICE <b>' + a + ' + ' + b + ' = ' + mostr + '</b>. ¿ESTÁ BIEN?', ops: ['SÍ', 'NO'], ok: mostr === a + b ? 'SÍ' : 'NO', ayuda: 'PENSÁ: ' + a + ' + ' + b + ' ES ' + a + ' Y ' + b + ' MÁS.', bien: '¡MUY BIEN! ' + a + ' + ' + b + ' = ' + (a + b) + '.' }; });
      return respuesta(el, api, function () { var c, r;
        if (qc === 'uno_diez') { var n = R(11, 88), d = pick([1, 10, -10]); r = n + d; c = '¿CUÁNTO ES <b>' + n + (d > 0 ? ' + ' : ' − ') + Math.abs(d) + '</b>?'; }
        else { var a = R(5, 20), b = R(1, 9), rs2 = Math.random() < 0.5 && a > b; r = rs2 ? a - b : a + b; c = 'APRETÁS <b>' + String(a).split('').join(', ') + ', ' + (rs2 ? '−' : '+') + ', ' + b + '</b> Y <b>=</b>. ¿QUÉ SALE EN LA PANTALLA?'; }
        return { cons: c, html: p1Calc('?'), campos: [{ v: r }], ayuda: qc === 'uno_diez' ? 'SUMAR O RESTAR 10 CAMBIA LA PRIMERA CIFRA; SUMAR 1, LA ÚLTIMA.' : 'HACÉ LA CUENTA QUE ARMASTE CON LAS TECLAS.', bien: '¡MUY BIEN! SALE ' + r + '.' }; }); }
    if (md === 'centenas') { var qC = p.que || 'contar', mx = p.max || 4;
      if (qC === 'escribir' || qC === 'leer') return p1Elegir(el, api, function () { var c = R(1, mx), d = pick([0, R(1, 9)]), u = R(0, 9), n = c * 100 + d * 10 + u, ok = String(n), ops;
        if (qC === 'escribir') { ops = [ok, String(c * 1000 + d * 10 + u)]; var sw = String(c * 100 + u * 10 + d); ops.push(sw !== ok ? sw : String(n + 100));
          return { cons: '¿CÓMO SE ESCRIBE <b>' + p1Up(n) + '</b>?', ops: mezclar(ops), ok: ok, ayuda: 'SON ' + c + ' CENTENAS, ' + d + ' DECENAS Y ' + u + ' UNIDADES: TRES CIFRAS.', bien: '¡MUY BIEN! SE ESCRIBE ' + n + '.' }; }
        var otros = [n], k; while (otros.length < 3) { k = n + pick([-100, 100, 10, -10, 1, 9]); if (k > 100 && k < 1000 && otros.indexOf(k) < 0) otros.push(k); }
        return { cons: '¿CÓMO SE LEE ESTE NÚMERO?', html: p1CDUt(n), ops: mezclar(otros.map(p1Up)), ok: p1Up(n), ayuda: 'EMPEZÁ POR LAS CENTENAS.', bien: '¡MUY BIEN! ' + n + ' SE LEE ' + p1Up(n) + '.' }; });
      return respuesta(el, api, function () { var c = R(1, mx), d = R(0, 9), u = R(0, 9), n = c * 100 + d * 10 + u;
        return { cons: 'CADA CAJA TIENE 100 Y CADA PAQUETE 10. ¿CUÁNTOS HAY EN TOTAL?', html: p1CDU(n), campos: [{ v: n }], ayuda: 'CONTÁ LAS CAJAS DE 100 EN 100, LOS PAQUETES DE 10 EN 10 Y DESPUÉS LOS SUELTOS.', bien: '¡MUY BIEN! HAY ' + n + '.' }; }); }
    if (md === 'serie') return respuesta(el, api, function () { var pa = p.de || pick([1, 10, 100].filter(function (x) { return x <= (p.max || 500) / 5; })), baja = p.dir === 'baja' || (p.dir === 'mezcla' && Math.random() < 0.5), lo = (p.desde || 100) + (baja ? pa * 4 : 0), hi = (p.hasta || 190) - (baja ? 0 : pa * 4), a = R(Math.min(lo, hi), Math.max(lo, hi)), L = [], f = R(2, 4), k; for (k = 0; k < 5; k++) L.push(a + (baja ? -pa : pa) * k);
      return { cons: 'LA SERIE ' + (baja ? 'BAJA' : 'SUBE') + ' DE ' + pa + ' EN ' + pa + '. ¿QUÉ NÚMERO FALTA?', html: '<div class="lb-p1-tren">' + L.map(function (x, i) { return '<span class="lb-p1-vag' + (i === f ? ' oculto">?' : '">' + fmt(x)) + '</span>'; }).join('') + '</div>', campos: [{ v: L[f] }], ayuda: (baja ? 'RESTÁ ' : 'SUMÁ ') + pa + ' AL NÚMERO DE ANTES.', bien: '¡MUY BIEN! ES EL ' + L[f] + '.' }; });
    if (md === 'valor') { if (p.que === 'desarmar') return respuesta(el, api, function () { var c = R(1, 9), d = R(0, 9), u = R(0, 9);
        return { cons: '¿QUÉ NÚMERO ES <b>' + c * 100 + ' + ' + d * 10 + ' + ' + u + '</b>?', campos: [{ v: c * 100 + d * 10 + u }], ayuda: c + ' CENTENAS, ' + d + ' DECENAS Y ' + u + ' UNIDADES.', bien: '¡MUY BIEN! ES ' + (c * 100 + d * 10 + u) + '.' }; });
      return p1Elegir(el, api, function () { var c = R(1, 9), d = R(1, 9), u = R(1, 9); while (d === c) d = R(1, 9); while (u === c || u === d) u = R(1, 9); var n = c * 100 + d * 10 + u, k = R(0, 2), dig = String(n)[k], val = [c * 100, d * 10, u][k];
        return { cons: '¿CUÁNTO VALE EL <b>' + dig + '</b> EN EL ' + n + '?', html: p1CDUt(n), ops: [dig, dig + '0', dig + '00'], ok: String(val), ayuda: 'MIRÁ EN QUÉ LUGAR ESTÁ: CENTENAS, DECENAS O UNIDADES.', bien: '¡MUY BIEN! VALE ' + val + '.' }; }); }
    if (md === 'comparar3') return p1Elegir(el, api, function () { var a = R(100, 999), b = Math.random() < 0.5 ? Math.floor(a / 100) * 100 + R(0, 99) : R(100, 999); while (b === a) b = R(100, 999); var may = Math.random() < 0.5;
      return { cons: '¿CUÁL ES <b>' + (may ? 'MAYOR' : 'MENOR') + '</b>?', ops: [String(a), String(b)], ok: String(may ? Math.max(a, b) : Math.min(a, b)), ayuda: 'MIRÁ PRIMERO LAS CENTENAS; SI EMPATAN, LAS DECENAS.', bien: '¡MUY BIEN!' }; });
    if (md === 'orden3') return p1Elegir(el, api, function () { var L = [], x; while (L.length < 3) { x = R(100, 999); if (L.indexOf(x) < 0) L.push(x); } var dsc = p.orden === 'desc', S = L.slice().sort(function (a, b) { return dsc ? b - a : a - b; }), pr = Math.random() < 0.6;
      return { cons: 'DE <b>' + (dsc ? 'MAYOR A MENOR' : 'MENOR A MAYOR') + '</b>, ¿CUÁL VA <b>' + (pr ? 'PRIMERO' : 'ÚLTIMO') + '</b>?', ops: L.map(String), ok: String(pr ? S[0] : S[2]), ayuda: 'MIRÁ PRIMERO LAS CENTENAS.', bien: '¡MUY BIEN! ' + S.join(', ') + '.' }; });
    if (md === 'recta1000') { if (p.que === 'entre') return p1Elegir(el, api, function () { var n = R(11, 98) * 10, c = Math.floor(n / 100) * 100; if (n === c) n += 50; var ops = [c + ' Y ' + (c + 100), (c + 100) + ' Y ' + (c + 200), Math.max(0, c - 100) + ' Y ' + Math.max(100, c)]; ops = ops.filter(function (x, i) { return ops.indexOf(x) === i; });
        return { cons: '¿ENTRE QUÉ CIENTOS ESTÁ EL <b>' + n + '</b>?', ops: mezclar(ops), ok: c + ' Y ' + (c + 100), ayuda: 'MIRÁ LAS CENTENAS: TIENE ' + c / 100 + '.', bien: '¡MUY BIEN!' }; });
      return respuesta(el, api, function () { var n = 100 * R(1, 9) + pick([0, 50]);
        return { cons: '¿QUÉ NÚMERO VA EN EL LUGAR DEL <b>?</b>', html: p1R1000([[n, 'pb', '?']]), campos: [{ v: n }], ayuda: 'MIRÁ LAS MARCAS DE 100 EN 100.', bien: '¡MUY BIEN! ES EL ' + n + '.' }; }); }
    if (md === 'redondos3') return p1Elegir(el, api, function () { var r = 10 * R(11, 99), a = r + R(1, 9), b = r - 10 * R(1, 5) + R(1, 9);
      return { cons: '¿CUÁL ES UN NÚMERO <b>REDONDO</b>?', ops: mezclar([String(r), String(a), String(b)]), ok: String(r), ayuda: 'UN NÚMERO REDONDO TERMINA EN 0.', bien: '¡MUY BIEN! ' + r + ' TERMINA EN 0.' }; });
    if (md === 'cambia') return respuesta(el, api, function () { var n = R(100, 889), ad = pick([1, 10, 100]);
      return { cons: '¿CUÁNTO ES <b>' + n + ' + ' + ad + '</b>?', html: p1CDUt(n), campos: [{ v: n + ad }], ayuda: 'SUMAR ' + ad + ' CAMBIA LA CIFRA DE LAS ' + (ad === 100 ? 'CENTENAS' : ad === 10 ? 'DECENAS' : 'UNIDADES') + '.', bien: '¡MUY BIEN! ES ' + (n + ad) + '.' }; });
    if (md === 'comparar4') return p1Elegir(el, api, function () { var a = R(1000, 9999), b = Math.random() < 0.6 ? Math.floor(a / 1000) * 1000 + R(0, 999) : R(1000, 9999); while (b === a) b = R(1000, 9999); var may = Math.random() < 0.5;
      return { cons: '¿CUÁL ES <b>' + (may ? 'MAYOR' : 'MENOR') + '</b>?', ops: [fmt(a), fmt(b)], ok: fmt(may ? Math.max(a, b) : Math.min(a, b)), ayuda: 'MIRÁ PRIMERO LOS MILES; SI EMPATAN, LAS CENTENAS.', bien: '¡MUY BIEN!' }; });
    if (md === 'orden4') return p1Elegir(el, api, function () { var m = R(1, 9), L = [], x; while (L.length < 3) { x = Math.random() < 0.5 ? m * 1000 + R(0, 999) : R(1000, 9999); if (L.indexOf(x) < 0) L.push(x); } var dsc = p.orden === 'desc', S = L.slice().sort(function (a, b) { return dsc ? b - a : a - b; }), pr = Math.random() < 0.6;
      return { cons: 'DE <b>' + (dsc ? 'MAYOR A MENOR' : 'MENOR A MAYOR') + '</b>, ¿CUÁL VA <b>' + (pr ? 'PRIMERO' : 'ÚLTIMO') + '</b>?', ops: L.map(fmt), ok: fmt(pr ? S[0] : S[2]), ayuda: 'MIRÁ PRIMERO LOS MILES.', bien: '¡MUY BIEN! ' + S.map(fmt).join(', ') + '.' }; });
    if (md === 'vecinos4') return respuesta(el, api, function () { var n = pick([R(1001, 9998), 1000 * R(2, 9), 1000 * R(1, 8) + 999, 100 * R(11, 98) + 99]);
      return { cons: 'ESCRIBÍ EL <b>ANTERIOR</b> Y EL <b>SIGUIENTE</b> DEL <b>' + fmt(n) + '</b>.', campos: [{ lab: 'ANTERIOR', v: n - 1 }, { lab: 'SIGUIENTE', v: n + 1 }], ayuda: 'EL ANTERIOR ES UNO MENOS Y EL SIGUIENTE, UNO MÁS.', bien: '¡MUY BIEN! ' + fmt(n - 1) + ' Y ' + fmt(n + 1) + '.' }; });
    if (md === 'recta10000') { if (p.que === 'entre') return p1Elegir(el, api, function () { var n = R(11, 98) * 100, c = Math.floor(n / 1000) * 1000; if (n === c) n += 500; var ops = [fmt(c) + ' Y ' + fmt(c + 1000), fmt(c + 1000) + ' Y ' + fmt(c + 2000), fmt(Math.max(0, c - 1000)) + ' Y ' + fmt(Math.max(1000, c))]; ops = ops.filter(function (x, i) { return ops.indexOf(x) === i; });
        return { cons: '¿ENTRE QUÉ MILES ESTÁ EL <b>' + fmt(n) + '</b>?', ops: mezclar(ops), ok: fmt(c) + ' Y ' + fmt(c + 1000), ayuda: 'MIRÁ LOS MILES: TIENE ' + c / 1000 + '.', bien: '¡MUY BIEN!' }; });
      return respuesta(el, api, function () { var n = 1000 * R(1, 9) + pick([0, 500]);
        return { cons: '¿QUÉ NÚMERO VA EN EL LUGAR DEL <b>?</b>', html: p1R10000([[n, 'pb', '?']]), campos: [{ v: n }], ayuda: 'MIRÁ LAS MARCAS DE 1.000 EN 1.000.', bien: '¡MUY BIEN! ES EL ' + fmt(n) + '.' }; }); }
    if (md === 'valor4') { if (p.que === 'desarmar') return respuesta(el, api, function () { var m = R(1, 9), c = R(0, 9), d = R(0, 9), u = R(0, 9), n = m * 1000 + c * 100 + d * 10 + u;
        return { cons: 'ESCRIBÍ CUÁNTO VALE CADA CIFRA DEL <b>' + fmt(n) + '</b>.', html: p1CDUt(n), campos: [{ lab: 'MILES', v: m * 1000 }, { lab: 'CENTENAS', v: c * 100 }, { lab: 'DECENAS', v: d * 10 }, { lab: 'UNIDADES', v: u }], ayuda: 'EL ' + m + ' DE LOS MILES VALE ' + fmt(m * 1000) + '.', bien: '¡MUY BIEN! ' + fmt(n) + ' = ' + [m * 1000, c * 100, d * 10, u].map(fmt).join(' + ') + '.' }; });
      if (p.que === 'juntar') return respuesta(el, api, function () { var m = R(1, 9), c = R(0, 9), d = R(0, 9), u = R(0, 9), T = [[m * 1000, 0], [c * 100, 1], [d * 10, 2], [u, 3]].filter(function (x) { return x[0]; }); if (Math.random() < 0.5) T = mezclar(T);
        return { cons: '¿QUÉ NÚMERO ES <b>' + T.map(function (x) { return fmt(x[0]); }).join(' + ') + '</b>?', campos: [{ v: m * 1000 + c * 100 + d * 10 + u }], ayuda: 'PONÉ CADA CIFRA EN SU LUGAR. SI FALTA UN LUGAR, VA UN 0.', bien: '¡MUY BIEN! ES ' + fmt(m * 1000 + c * 100 + d * 10 + u) + '.' }; });
      return p1Elegir(el, api, function () { var D4 = mezclar([1, 2, 3, 4, 5, 6, 7, 8, 9]).slice(0, 4), n = Number(D4.join('')), k = R(0, 3), dig = String(D4[k]), val = D4[k] * [1000, 100, 10, 1][k];
        return { cons: '¿CUÁNTO VALE EL <b>' + dig + '</b> EN EL ' + fmt(n) + '?', html: p1CDUt(n), ops: [dig, dig + '0', dig + '00', fmt(Number(dig + '000'))], ok: fmt(val), ayuda: 'MIRÁ EN QUÉ LUGAR ESTÁ: MILES, CENTENAS, DECENAS O UNIDADES.', bien: '¡MUY BIEN! VALE ' + fmt(val) + '.' }; }); }
    if (md === 'armar4') return respuesta(el, api, function () { var D4 = mezclar([1, 2, 3, 4, 5, 6, 7, 8, 9]).slice(0, 4), menor = p.que === 'menor' || (p.que === 'mezcla' && Math.random() < 0.5), S = D4.slice().sort(function (a, b) { return menor ? a - b : b - a; });
      return { cons: 'CON ESTAS TARJETAS, ARMÁ EL NÚMERO MÁS <b>' + (menor ? 'CHICO' : 'GRANDE') + '</b>.', html: '<div class="lb-p1-tren">' + D4.map(function (x) { return '<span class="lb-p1-vag">' + x + '</span>'; }).join('') + '</div>', campos: [{ v: Number(S.join('')) }], ayuda: 'EN LOS MILES VA LA CIFRA MÁS ' + (menor ? 'CHICA' : 'GRANDE') + '.', bien: '¡MUY BIEN! ' + fmt(Number(S.join(''))) + '.' }; });
    if (md === 'cambia4') return respuesta(el, api, function () { var n = R(1000, 8899), ad = p.op || pick([1, 10, 100, 1000]);
      return { cons: '¿CUÁNTO ES <b>' + fmt(n) + ' + ' + fmt(ad) + '</b>?', html: p1CDUt(n), campos: [{ v: n + ad }], ayuda: 'SUMAR ' + fmt(ad) + ' CAMBIA LA CIFRA DE ' + (ad === 1000 ? 'LOS MILES' : ad === 100 ? 'LAS CENTENAS' : ad === 10 ? 'LAS DECENAS' : 'LAS UNIDADES') + '.', bien: '¡MUY BIEN! ES ' + fmt(n + ad) + '.' }; });
    if (md === 'dinero2') { var qd3 = p.que || 'contar';
      if (qd3 === 'caro') return p1Elegir(el, api, function () { var a = 10 * R(10, 99), b = 10 * R(10, 99); while (b === a) b = 10 * R(10, 99); var car = Math.random() < 0.5;
        return { cons: '¿CUÁL ES MÁS <b>' + (car ? 'CARO' : 'BARATO') + '</b>?', ops: ['$' + a, '$' + b], ok: '$' + (car ? Math.max(a, b) : Math.min(a, b)), ayuda: 'COMPARÁ COMO NÚMEROS: PRIMERO LAS CENTENAS.', bien: '¡MUY BIEN!' }; });
      return respuesta(el, api, function () { var c, r, h = '';
        if (qd3 === 'vuelto') { var pg = pick([100, 200, 500]), pr = 10 * R(pg / 20, pg / 10 - 1); r = pg - pr; c = 'ALGO CUESTA <b>$' + pr + '</b> Y PAGÁS CON <b>$' + pg + '</b>. ¿CUÁNTO TE DEVUELVEN?'; }
        else if (qd3 === 'sumar') { var a = 50 * R(1, 9), b = 50 * R(1, 9); r = a + b; c = 'ALGO DE <b>$' + a + '</b> Y ALGO DE <b>$' + b + '</b>. ¿CUÁNTO CUESTAN JUNTOS?'; }
        else { var vs = [], k; for (k = R(0, 1); k > 0; k--) vs.push(500); for (k = R(0, 2); k > 0; k--) vs.push(200); for (k = R(1, 3); k > 0; k--) vs.push(100); for (k = R(0, 1); k > 0; k--) vs.push(50); vs = mezclar(vs); r = vs.reduce(function (x, y) { return x + y; }, 0); c = '¿CUÁNTO DINERO HAY EN TOTAL?'; h = p1Plata(vs); }
        return { cons: c, html: h, campos: [{ v: r, lab: '$' }], ayuda: qd3 === 'vuelto' ? 'CONTÁ PARA ADELANTE DESDE EL PRECIO HASTA LO QUE PAGÁS.' : 'EMPEZÁ POR LO QUE MÁS VALE Y SEGUÍ SUMANDO.', bien: '¡MUY BIEN! $' + r + '.' }; }); }
    if (md === 'mental') return respuesta(el, api, function () { var qm = p.que || 'chica', M2, a, b;
      if (qm === 'falta100') M2 = p1Ment(qm, p.op, 10 * R(1, 9), 0);
      else if (qm === 'desarmar') M2 = p1Ment(qm, p.op, R(110, 489), R(11, 59));
      else if (qm === 'truco') { a = R(110, 889); b = pick([10, 100]); M2 = { a: a, b: b, sg: p.op === 'resta' ? '−' : '+', r: p.op === 'resta' ? a - b : a + b }; }
      else M2 = p1Ment('chica', p.op, R(1, 9), R(1, 9), p.esc || pick([10, 100]));
      return { cons: '¿CUÁNTO ES <b>' + M2.a + ' ' + M2.sg + ' ' + M2.b + '</b>? HACELO EN LA CABEZA.', campos: [{ v: M2.r }], ayuda: qm === 'chica' ? 'PENSÁ LA CUENTA CHICA SIN LOS CEROS.' : qm === 'falta100' ? 'CONTÁ DE 10 EN 10 HASTA EL 100.' : qm === 'desarmar' ? 'HACÉ CENTENAS, DECENAS Y UNIDADES POR SEPARADO.' : 'CAMBIA UNA SOLA CIFRA.', bien: '¡MUY BIEN! ' + M2.a + ' ' + M2.sg + ' ' + M2.b + ' = ' + M2.r + '.' }; });
    if (md === 'columna') { var rsC = p.op === 'resta', qq = p.que || 'cuenta';
      var gen = function () { var a, b, ok = false, t = 0; while (!ok && t++ < 200) { a = R(120, 899); b = R(11, rsC ? a - 1 : 999 - a); var A = String(a).padStart(3, '0'), B = String(b).padStart(3, '0'), lleva = rsC ? (+A[2] < +B[2] || +A[1] < +B[1]) : (+A[2] + +B[2] > 9 || +A[1] + +B[1] > 9); ok = b > 10 && (p.lleva ? lleva : !lleva) && (rsC || a + b < 1000); } return [a, b]; };
      if (qq === 'estimar') return p1Elegir(el, api, function () { var ab = gen(), r = rsC ? ab[0] - ab[1] : ab[0] + ab[1], cerca = Math.round(r / 100) * 100, ops = [cerca, cerca + 200, Math.max(100, cerca - 300)];
        return { cons: '<b>' + ab[0] + ' ' + (rsC ? '−' : '+') + ' ' + ab[1] + '</b> DA MÁS O MENOS…', ops: mezclar(ops.map(String)), ok: String(cerca), ayuda: 'REDONDEÁ CADA NÚMERO A LOS CIENES Y HACÉ LA CUENTA CHICA.', bien: '¡MUY BIEN! DA ' + r + ', CERCA DE ' + cerca + '.' }; });
      if (qq === 'control') return p1Elegir(el, api, function () { var ab = gen(), r = rsC ? ab[0] - ab[1] : ab[0] + ab[1], bien = Math.random() < 0.5, mos = bien ? r : r + pick([10, 100, -10, 90]);
        return { cons: rsC ? '¿ESTÁ BIEN <b>' + ab[0] + ' − ' + ab[1] + ' = ' + mos + '</b>? CONTROLÁ CON UNA SUMA.' : '¿ESTÁ BIEN <b>' + ab[0] + ' + ' + ab[1] + ' = ' + mos + '</b>?', ops: ['SÍ', 'NO'], ok: mos === r ? 'SÍ' : 'NO', ayuda: rsC ? 'SUMÁ ' + mos + ' + ' + ab[1] + ': TIENE QUE DAR ' + ab[0] + '.' : 'HACÉ LA CUENTA COLUMNA POR COLUMNA.', bien: '¡MUY BIEN! DA ' + r + '.' }; });
      return respuesta(el, api, function () { var ab = gen(), r = rsC ? ab[0] - ab[1] : ab[0] + ab[1];
        return { cons: 'RESOLVÉ EN COLUMNAS: <b>' + ab[0] + ' ' + (rsC ? '−' : '+') + ' ' + ab[1] + '</b>', html: p1Col3(ab[0], ab[1], rsC ? '−' : '+', '', -1), campos: [{ v: r }], ayuda: 'EMPEZÁ POR LAS UNIDADES' + (p.lleva ? (rsC ? '; SI NO ALCANZA, ABRÍ UN PAQUETE.' : '; SI PASA DE 9, TE LLEVÁS 1.') : '.'), bien: '¡MUY BIEN! ES ' + r + '.' }; }); }
    if (md === 'prop') return respuesta(el, api, function () { var qp = p.que || 'conmuta', c, r;
      if (qp === 'amigos') { var a = R(11, 89), b = R(11, 89), k = (10 - a % 10) % 10 || 10; r = a + b + k; c = '¿CUÁNTO ES <b>' + a + ' + ' + b + ' + ' + k + '</b>? BUSCÁ AMIGOS.'; }
      else if (qp === 'dobles') { var d = 5 * R(2, 12), dd = pick([1, -1]); r = 2 * d + dd; c = 'SI <b>' + d + ' + ' + d + ' = ' + 2 * d + '</b>, ¿CUÁNTO ES <b>' + d + ' + ' + (d + dd) + '</b>?'; }
      else if (qp === 'familia') { var x = 10 * R(1, 6), y = 10 * R(1, 4), z = x + y, rs = Math.random() < 0.5; r = rs ? x : y; c = 'SI <b>' + x + ' + ' + y + ' = ' + z + '</b>, ¿CUÁNTO ES <b>' + z + ' − ' + (rs ? y : x) + '</b>?'; }
      else { var s1 = R(1, 9), g1 = R(100, 300); r = s1 + g1; c = '¿CUÁNTO ES <b>' + s1 + ' + ' + g1 + '</b>? EMPEZÁ POR EL GRANDE.'; }
      return { cons: c, campos: [{ v: r }], ayuda: qp === 'amigos' ? 'JUNTÁ PRIMERO LOS QUE FORMAN UN REDONDO.' : qp === 'dobles' ? 'ES EL DOBLE CON UNO MÁS O UNO MENOS.' : qp === 'familia' ? 'LA RESTA DESHACE LA SUMA.' : 'DALA VUELTA: EL ORDEN NO IMPORTA EN LA SUMA.', bien: '¡MUY BIEN! ES ' + r + '.' }; });
    if (md === 'mult') { var qx = p.que || 'grupos';
      if (qx === 'signo') return p1Elegir(el, api, function () { var g2 = R(2, 5), n = R(2, 9), ok = g2 + ' × ' + n, ops = [ok, g2 + ' + ' + n, n + ' − ' + g2];
        return { cons: '¿CÓMO SE ESCRIBE <b>' + Array(g2 + 1).join(n + ' + ').slice(0, -3) + '</b>?', ops: mezclar(ops), ok: ok, ayuda: 'CONTÁ CUÁNTAS VECES SE SUMA EL ' + n + '.', bien: '¡MUY BIEN! ' + ok + ' = ' + g2 * n + '.' }; });
      return respuesta(el, api, function () { var o = pick(['caramelo', 'pelota', 'estrella', 'flor']), a, b, c, h = '', r;
        if (qx === 'arreglo' || qx === 'filas') { a = R(2, 5); b = R(2, 6); h = p1Arr(a, b, o); if (qx === 'filas') { var fl = Math.random() < 0.5; r = fl ? a : b; c = '¿CUÁNTAS <b>' + (fl ? 'FILAS' : 'COLUMNAS') + '</b> TIENE EL ARREGLO?'; } else { r = a * b; c = '¿CUÁNTOS HAY EN TOTAL? PENSÁ FILAS × COLUMNAS.'; } }
        else { a = R(2, 5); b = R(2, 6); for (var k = 0; k < a; k++) h += p1Grupo('', b, o); r = a * b; c = 'HAY ' + a + ' GRUPOS DE ' + b + '. ¿CUÁNTOS HAY EN TOTAL?'; }
        return { cons: c, html: h, campos: [{ v: r }], ayuda: qx === 'filas' ? 'LA FILA VA ACOSTADA Y LA COLUMNA PARADA.' : 'SUMÁ EL MISMO NÚMERO TANTAS VECES COMO GRUPOS O FILAS HAYA.', bien: '¡MUY BIEN! ES ' + r + '.' }; }); }
    if (md === 'por10') { var q10 = p.que || 'cuenta';
      if (q10 === 'cuantos0') return p1Elegir(el, api, function () { var d = pick([10, 100]);
        return { cons: 'PARA HACER <b>× ' + d + '</b>, ¿CUÁNTOS CEROS AGREGÁS AL FINAL?', ops: ['UN CERO', 'DOS CEROS', 'NINGUNO'], ok: d === 100 ? 'DOS CEROS' : 'UN CERO', ayuda: 'CONTÁ LOS CEROS DEL ' + d + '.', bien: '¡MUY BIEN!' }; });
      return respuesta(el, api, function () { var d = p.de || pick([10, 100]), n = d === 100 ? R(1, 9) : R(1, q10 === 'cifras' ? 45 : 9), c, h = '';
        if (q10 === 'problema') { var o = pick(['caramelo', 'pelota', 'estrella']); c = 'HAY <b>' + n + '</b> ' + (d === 100 ? 'CAJAS' : 'PAQUETES') + ' Y CADA UNO TIENE <b>' + d + '</b> ' + P1PL[o] + '. ¿' + g(o, 'CUÁNTAS', 'CUÁNTOS') + ' HAY?'; }
        else c = '¿CUÁNTO ES <b>' + n + ' × ' + d + '</b>?';
        if (d === 10 && q10 !== 'cifras') h = p1BolsasN(n);
        return { cons: c, html: h, campos: [{ v: n * d }], ayuda: 'AGREGÁ ' + (d === 100 ? 'DOS CEROS' : 'UN CERO') + ' AL ' + n + '.', bien: '¡MUY BIEN! ' + n + ' × ' + d + ' = ' + n * d + '.' }; }); }
    if (md === 'miles') { var qM = p.que || 'contar', fM = function (x) { return H.fmt ? H.fmt(x) : String(x); }, mxM = p.max || 9;
      var nG = function () { var m = R(1, mxM), c = R(0, 9), d = pick([0, R(1, 9)]), u = R(0, 9); return { m: m, c: c, d: d, u: u, n: m * 1000 + c * 100 + d * 10 + u }; };
      if (qM === 'escribir') return p1Elegir(el, api, function () { var x = nG(), ok = fM(x.n), w1 = fM(x.m * 10000 + x.c * 100 + x.d * 10 + x.u), w2 = fM(x.m * 100 + x.c * 10 + x.u);
        return { cons: '¿CÓMO SE ESCRIBE <b>' + p1Up(x.n) + '</b>?', ops: mezclar([ok, w1, w2 === ok ? fM(x.n + 1000) : w2]), ok: ok, ayuda: 'SON CUATRO CIFRAS: MILES, CENTENAS, DECENAS Y UNIDADES.', bien: '¡MUY BIEN! SE ESCRIBE ' + ok + '.' }; });
      if (qM === 'leer') return p1Elegir(el, api, function () { var x = nG(), o2 = [x.n], k; while (o2.length < 3) { k = x.n + pick([1000, -1000, 100, -100, 10]); if (k > 999 && k < 10000 && o2.indexOf(k) < 0) o2.push(k); }
        return { cons: '¿CÓMO SE LEE ESTE NÚMERO?', html: p1CDUt(x.n), ops: mezclar(o2.map(p1Up)), ok: p1Up(x.n), ayuda: 'EMPEZÁ POR LOS MILES.', bien: '¡MUY BIEN!' }; });
      return respuesta(el, api, function () { var x = nG();
        return { cons: 'CADA CAMIÓN TIENE 1.000, CADA CAJA 100 Y CADA PAQUETE 10. ¿CUÁNTOS HAY?', html: p1CDU(x.n), campos: [{ v: x.n }], ayuda: 'CONTÁ CAMIONES, CAJAS, PAQUETES Y SUELTOS, EN ESE ORDEN.', bien: '¡MUY BIEN! HAY ' + fM(x.n) + '.' }; }); }
    if (md === 'redondo') return respuesta(el, api, function () { var n = 10 * R(1, Math.floor((p.max || 100) / 10) - 1) - 1;
      return { cons: '¿QUÉ NÚMERO VIENE <b>DESPUÉS</b> DEL ' + n + '?', html: p1Big(n), campos: [{ v: n + 1 }], ayuda: 'DESPUÉS DE UN 9 VIENE UN NÚMERO REDONDO.', bien: '¡MUY BIEN! DESPUÉS DEL ' + n + ' VIENE EL ' + (n + 1) + '.' }; });
    if (md === 'redondos') return p1Elegir(el, api, function () { var n = 10 * R(2, 9), ops = [n]; while (ops.length < 3) { var x = 10 * R(2, 9); if (ops.indexOf(x) < 0) ops.push(x); }
      return { cons: '¿CÓMO SE LEE ESTE NÚMERO REDONDO?', html: p1Cifras(n), ops: mezclar(ops.map(p1Up)), ok: p1Up(n), ayuda: 'MIRÁ LA PRIMERA CIFRA: ES UN ' + String(n)[0] + '.', bien: '¡MUY BIEN! ' + n + ' SE LEE ' + p1Up(n) + '.' }; });
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
    '.lb-cajas.n4{grid-template-columns:1fr 1fr}@media (min-width:700px){.lb-cajas.n4{grid-template-columns:repeat(4,1fr)}}',
    '.lb-cn{display:flex;flex-direction:column;align-items:center;gap:6px;margin:8px 0}.lb-cn-f{display:flex;gap:4px}.lb-cn-c{width:36px;height:46px;display:grid;place-items:center;border:2px solid #087E83;border-radius:10px;background:#fff;font-weight:800;font-size:1.4rem}.lb-cn-c.vac{border-style:dashed;border-color:#D7F0E9}.lb-cn-c.eq{background:#F3FBF7;color:#9dbdb9}.lb-cn-c.on{background:#087E83;color:#fff}',
    '.lb-cn-res{font-size:1.5rem;font-weight:800;text-align:center;margin:10px 0 0;color:#066A6E}.lb-cn-in{width:12ch!important;font-size:1.15rem}',
    '.lb-sx-op{display:flex;gap:8px;margin-bottom:10px}.lb-sx-dat{display:flex;flex-direction:column;gap:8px}.lb-sx-row{display:flex;align-items:center;gap:6px;flex-wrap:wrap}.lb-sx-row em{font-style:normal;font-weight:800;color:#066A6E;margin-right:8px}.lb-sx-in{width:4ch!important;text-align:center;font-size:1.2rem}',
    '.lb-sx-pasos{margin:12px 0 0;padding-left:22px;line-height:1.55}.lb-sx-pasos li{margin:4px 0}',
    '.lb-dc-cif{display:flex;justify-content:center;gap:4px;margin:6px 0}.lb-dc-d{width:40px;height:50px;display:grid;place-items:center;border-radius:10px;font-weight:800;font-size:1.6rem;border:2px solid currentColor}.lb-dc-d.cero{color:#9dbdb9}.lb-dc-fl{text-align:center;font-size:1.4rem;color:#087E83}',
    '.lb-dc-bs{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:6px}.lb-dc-b{display:flex;flex-direction:column;align-items:center;padding:8px 12px;border-radius:12px;color:#fff}.lb-dc-b b{font-size:1.3rem}.lb-dc-b small{opacity:.9;font-weight:700}.lb-dc-mas{font-style:normal;font-weight:800;font-size:1.4rem;color:#253638}',
    '.lb-dc-d.c0{color:#087E83}.lb-dc-d.c1{color:#253638}.lb-dc-d.c2{color:#3BA99C}.lb-dc-d.c3{color:#066A6E}.lb-dc-d.c4{color:#5C8D89}.lb-dc-b.c0{background:#087E83}.lb-dc-b.c1{background:#253638}.lb-dc-b.c2{background:#3BA99C}.lb-dc-b.c3{background:#066A6E}.lb-dc-b.c4{background:#5C8D89}',
    '.lb-bp-w{display:flex;justify-content:center;align-items:center;gap:14px}.lb-bp{border-collapse:collapse;font-size:1.15rem}.lb-bp td,.lb-bp th{padding:4px 10px;text-align:left}.lb-bp th{font-size:.75rem;color:#4b6a6c}.lb-bp-r{font-weight:800;color:#fff;background:#087E83;text-align:center!important;border-radius:8px;border:3px solid #fff}',
    '.lb-bp-fl{font-size:2.2rem;color:#087E83;text-align:center;line-height:1}.lb-bp-fl small{display:block;font-size:.7rem;font-weight:700}.lb-bp-row{display:flex;justify-content:center;gap:6px;flex-wrap:wrap}.lb-bp-c{display:flex;flex-direction:column;align-items:center;gap:4px}.lb-bp-c small{font-weight:800;color:#4b6a6c}.lb-bp-c b{width:42px;height:50px;display:grid;place-items:center;border:2px solid #9dbdb9;border-radius:10px;font-size:1.5rem;color:#9dbdb9}.lb-bp-c.on b{background:#087E83;border-color:#087E83;color:#fff}.lb-bp-c.on small{color:#087E83}',
    '.lb-pp-vis{min-height:180px;display:flex;flex-direction:column;justify-content:center}.lb-pp-txt{font-size:1.1rem;line-height:1.45;margin:12px 0 10px;padding:10px 14px;background:#D7F0E9;border-radius:12px;color:#253638;min-height:2.9em}',
    '.lb-pp-nav{display:flex;align-items:center;justify-content:space-between;gap:8px}.lb-pp-nav span{font-weight:800;color:#4b6a6c;font-size:.9rem}.lb-pp-b{border:2px solid #087E83;background:#fff;color:#066A6E;font-weight:800;border-radius:999px;padding:8px 14px;cursor:pointer;font-family:inherit}.lb-pp-b.sig{background:#087E83;color:#fff}.lb-pp-b:disabled{opacity:.35;cursor:default}',
    '.lb-vp-c{display:inline-grid;place-items:center}.lb-vp-num{font-size:2rem;font-weight:800;letter-spacing:.12em;text-align:center;color:#066A6E;margin:0}.lb-vp-tr.on{background:#087E83}.lb-vp-tr.on b,.lb-vp-tr.on small{color:#fff}.lb-vp-tr em{font-style:normal;font-weight:700;font-size:.85rem;color:#066A6E;margin-top:4px;max-width:130px;text-align:center}.lb-vp-tr.on em{color:#fff}',
    '.lb-dc-d.pend{color:#253638;border-color:#9dbdb9}.lb-bp-r.tenue{background:#5C8D89}',
    '.lb-sx-t{border-collapse:collapse;margin:0 auto;font-size:1.2rem}.lb-sx-t td{padding:6px 12px;text-align:right;font-weight:700}.lb-sx-t td.on{background:#087E83;color:#fff;border-radius:8px}.lb-sx-t tr.res td{border-top:3px solid #253638;color:#066A6E;font-weight:800}',
    '.lb-sg{display:flex;justify-content:center;gap:10px}.lb-sg span{display:flex;flex-direction:column;align-items:center;padding:10px 18px;border-radius:14px;background:#087E83;color:#fff}.lb-sg b{font-size:1.8rem}.lb-sg small{font-weight:700}',
    '.lb-pt-g{font-size:2.2rem;font-weight:800;text-align:center;color:#066A6E;margin:4px 0}.lb-pt-f{font-size:1.2rem;text-align:center;margin:0;color:#253638}',
    '.lb2-calc{margin:8px auto;max-width:220px;padding:10px 14px;border-radius:12px;background:#253638;color:#D7F0E9;font:700 1.6rem/1.2 monospace;text-align:right}',
    '.lb2-tira{display:flex;flex-wrap:wrap;gap:4px;justify-content:center}.lb2-tira span{width:30px;height:30px;display:grid;place-items:center;border-radius:8px;background:#F3FBF7;font-weight:700;font-size:.8rem}.lb2-tira span.a{background:#7FD3C4}.lb2-tira span.b{background:#9dbdb9}.lb2-tira span.ab{background:#087E83;color:#fff}',
    '.lb2-grupos{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:6px 0}.lb2-grupos i{font-style:normal;padding:8px 12px;border-radius:10px;font-weight:800;color:#fff}.lb2-grupos i.g1{background:#087E83}.lb2-grupos i.g2{background:#253638}',
    '.lb-vp-w{overflow-x:auto}.lb-vp{border-collapse:separate;border-spacing:4px;margin:4px auto}.lb-vp th{font-size:.72rem;color:#4b6a6c;font-weight:800;text-align:center;padding:2px 4px}.lb-vp th.lb-vp-per{background:#D7F0E9;color:#066A6E;border-radius:8px;font-size:.78rem;padding:4px 6px}',
    '.lb-vp-c{width:44px;height:52px;border:2px solid #087E83;border-radius:12px;background:#fff;font-family:inherit;font-weight:800;font-size:1.6rem;line-height:1;color:#253638;cursor:pointer}.lb-vp.vplargo .lb-vp-c{width:32px;height:44px;font-size:1.25rem;border-radius:10px}.lb-vp.vplargo{border-spacing:2px}.lb-vp-in{width:14ch!important;font-size:1.2rem}.lb-vp-c.cero{color:#9dbdb9}.lb-vp-c.on{background:#087E83;color:#fff}',
    '.lb-vp-big{font-size:1.15rem;line-height:1.5;margin:12px 0 4px}.lb-vp-trozos{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:10px 0}.lb-vp-tr{display:flex;flex-direction:column;align-items:center;padding:8px 14px;border-radius:14px;background:#D7F0E9}.lb-vp-tr b{font-size:1.5rem;letter-spacing:.08em;color:#066A6E}.lb-vp-tr.cero{opacity:.5}.lb-vp-tr small{font-weight:700;color:#4b6a6c}',
    '.lb-p1-fila{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:6px 0}.lb-p1-o{position:relative;font-size:2.1rem;line-height:1;padding:4px;border-radius:12px;transition:opacity .2s}.lb-p1-o small{position:absolute;right:-4px;top:-6px;min-width:20px;height:20px;border-radius:10px;background:#087E83;color:#fff;font-size:.8rem;font-weight:800;display:grid;place-items:center;padding:0 4px}',
    '.lb-p1-o.on{background:#D7F0E9;outline:3px solid #087E83}.lb-p1-o.tenue{opacity:.18}.lb-p1-o.nuevo{background:#FFF3C4}.lb-p1-vac{font-size:1.4rem;color:#9dbdb9}.lb-p1-g{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:6px 10px;margin:6px 0;border-radius:14px;background:#F3FBF7}.lb-p1-g>b{min-width:5.5em;font-size:1rem;color:#066A6E}',
    '.lb-p1-big{font-size:1.7rem;font-weight:800;text-align:center;color:#066A6E;margin:10px 0 0;letter-spacing:.02em}.lb-p1-mezcla .lb-p1-fila:last-child{margin-left:30px}',
    '.lb-p1-pares{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin:6px 0}.lb-p1-col{display:flex;flex-direction:column;align-items:center;min-width:42px;padding:4px 2px;border-radius:14px;font-size:2rem;line-height:1.1}.lb-p1-col span{min-height:1.15em}.lb-p1-col i{font-style:normal;font-weight:800;color:#087E83;height:1em;font-size:1.3rem}.lb-p1-col.par{background:#D7F0E9}.lb-p1-col.sobra{background:#FFE1D6;outline:2px dashed #C2552E}',
    '.lb-p1-tren{display:flex;flex-wrap:wrap;gap:4px;justify-content:center;align-items:center;margin:8px 0}.lb-p1-loco{font-size:2rem}.lb-p1-vag{min-width:42px;height:44px;border:2px solid #087E83;border-radius:10px;display:grid;place-items:center;font-weight:800;font-size:1.3rem;background:#fff;color:#253638}.lb-p1-vag.on{background:#087E83;color:#fff}.lb-p1-vag.ant{background:#FFF3C4;border-color:#C29A1E}.lb-p1-vag.sig{background:#FFE1D6;border-color:#C2552E}.lb-p1-vag.oculto{background:#F3FBF7;border-style:dashed;color:#C2552E}',
    '.lb-p1-rw{padding:30px 0 4px}.lb-p1-recta{display:flex;width:100%;border-top:3px solid #253638}.lb-p1-rc{position:relative;flex:1;min-width:0;display:flex;flex-direction:column;align-items:center}.lb-p1-rc i{width:2px;height:8px;background:#253638}.lb-p1-rc b{font-size:.7rem;color:#4b6a6c}.lb-p1-rc em{position:absolute;top:-30px;font-style:normal;font-size:.62rem;font-weight:800;color:#066A6E;white-space:nowrap}',
    '.lb-p1-rc.pa b,.lb-p1-rc.pb b,.lb-p1-rc.cero b{width:19px;height:19px;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:.66rem;flex:none}.lb-p1-rc.pa b{background:#C29A1E}.lb-p1-rc.pb b{background:#087E83}.lb-p1-rc.cero b{background:#253638}',
    '.lb-p1-dz{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap}.lb-p1-caja{position:relative;display:grid;grid-template-columns:repeat(5,1fr);gap:2px;padding:6px;border:3px solid #087E83;border-radius:12px;font-size:1.4rem;line-height:1.1;background:#fff}.lb-p1-caja.on{background:#D7F0E9}.lb-p1-caja small{position:absolute;right:-10px;top:-12px;background:#087E83;color:#fff;font-weight:800;border-radius:10px;padding:0 6px;font-size:.85rem}',
    '.lb-p1-cif{display:flex;justify-content:center;gap:8px;margin:8px 0}.lb-p1-cif span{width:58px;height:70px;display:grid;place-items:center;border:3px solid #087E83;border-radius:14px;background:#fff;font-weight:800;font-size:2.4rem;color:#253638}.lb-p1-cif span.on{background:#087E83;color:#fff}.lb-p1-cif span.vac{border-style:dashed;color:#9dbdb9}',
    '.lb-p1-cua{display:grid;grid-template-columns:repeat(10,minmax(0,1fr));gap:3px;width:100%;max-width:360px;margin:6px auto}.lb-p1-cua span{height:28px;display:grid;place-items:center;border:2px solid #9dbdb9;border-radius:6px;background:#fff;font-weight:800;font-size:.8rem;color:#253638;overflow:hidden}.lb-p1-cua span.vac{border:0;background:none}.lb-p1-cua span.fila{background:#D7F0E9;border-color:#087E83}.lb-p1-cua span.on{background:#087E83;border-color:#087E83;color:#fff}.lb-p1-cua span.sig{background:#FFE1D6;border-color:#C2552E}.lb-p1-cua span.oculto{border-style:dashed;border-color:#C2552E;color:#C2552E;background:#FFF3C4}',
    '.lb-p1-du{display:flex;justify-content:center;gap:8px;margin:8px 0}.lb-p1-du span{display:flex;flex-direction:column;align-items:center;min-width:86px;padding:6px 8px;border:3px solid #9dbdb9;border-radius:14px;background:#fff}.lb-p1-du small{font-weight:800;font-size:.7rem;color:#4b6a6c}.lb-p1-du b{font-size:2rem;color:#253638}.lb-p1-du span.on{border-color:#087E83;background:#D7F0E9}.lb-p1-dos{display:flex;flex-wrap:wrap;justify-content:center;gap:16px}.lb-p1-dos .lb-p1-du{padding:6px;border:2px dashed #9dbdb9;border-radius:16px;margin:4px 0}',
    '.lb-p1-r100w{padding:64px 18px 8px}.lb-p1-r100{position:relative;height:30px;border-top:3px solid #253638}.lb-p1-t{position:absolute;top:-3px;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center}.lb-p1-t i{width:2px;height:10px;background:#253638}.lb-p1-t b{font-size:.62rem;color:#4b6a6c}.lb-p1-m{position:absolute;top:-32px;transform:translateX(-50%);min-width:24px;padding:2px 4px;border-radius:10px;background:#087E83;color:#fff;font-weight:800;font-size:.75rem;text-align:center}.lb-p1-m.pa{background:#C29A1E;top:-60px}.lb-p1-m.pa:after{content:"";position:absolute;left:50%;top:100%;width:2px;height:28px;background:#C29A1E}',
    '.lb-p1-pal{display:inline-block;width:6px;height:34px;background:#253638;border-radius:3px;margin:0 4px}.lb-p1-pl{position:relative;display:flex;flex-direction:column;align-items:center;padding:4px 6px;border-radius:10px;font-size:1.6rem;line-height:1.1}.lb-p1-pl b{font-size:.85rem;color:#253638}.lb-p1-pl.bi{background:#E8F5E1}.lb-p1-pl.mo{background:#FFF3C4}.lb-p1-pl.on{outline:3px solid #087E83}.lb-p1-pl small{position:absolute;right:-6px;top:-8px;background:#087E83;color:#fff;font-weight:800;border-radius:10px;padding:0 5px;font-size:.75rem}',
    '.lb-p1-pre{display:flex;flex-direction:column;align-items:center;padding:8px 16px;border:3px solid #9dbdb9;border-radius:16px;font-size:2.2rem;background:#fff}.lb-p1-pre b{font-size:1.2rem;color:#253638}.lb-p1-pre.on{border-color:#087E83;background:#D7F0E9}',
    '.lb-p1-diez{display:grid;grid-template-columns:repeat(5,46px);gap:4px;justify-content:center;margin:8px auto}.lb-p1-diez span{height:46px;display:grid;place-items:center;border:3px solid #253638;border-radius:8px;background:#fff;font-size:1.5rem}.lb-p1-diez span.c1{background:#FFE1D6}.lb-p1-diez span.c2{background:#D7E8FF}.lb-p1-dado{font-size:3.4rem;line-height:1}',
    '.lb-p1-esp{display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap}.lb-p1-esp>i{font-style:normal;font-size:2rem}.lb-p1-tab{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px;max-width:300px;margin:6px auto}.lb-p1-tab span{padding:4px 8px;border:2px solid #9dbdb9;border-radius:10px;background:#fff;font-weight:800;text-align:center}.lb-p1-tab span.on{background:#087E83;color:#fff;border-color:#087E83}',
    '.lb-p1-hist{margin:8px 0;padding:12px 14px;border:3px dashed #087E83;border-radius:16px;background:#fff;font-size:1.1rem;line-height:1.5;font-weight:700;color:#253638}',
    '.lb-p1-calc{width:200px;margin:6px auto;padding:10px;border-radius:18px;background:#253638}.lb-p1-pan{min-height:40px;padding:6px 10px;border-radius:8px;background:#D7F0E9;color:#253638;font:800 1.3rem/1.4 monospace;text-align:right;overflow:hidden;white-space:nowrap}.lb-p1-pan.on{outline:4px solid #FFC94D}.lb-p1-tec{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:8px}.lb-p1-tec span{height:32px;display:grid;place-items:center;border-radius:8px;background:#fff;font-weight:800;color:#253638}.lb-p1-tec span.sg{background:#9dbdb9}.lb-p1-tec span.cero{grid-column:span 2}.lb-p1-tec span.on{background:#FFC94D}',
    '.lb-p1-colc{border-collapse:collapse;margin:6px auto;font-weight:800;font-size:1.6rem;color:#253638}.lb-p1-colc td{width:40px;height:40px;text-align:center}.lb-p1-colc tr.hd td{font-size:.75rem;color:#4b6a6c;height:18px}.lb-p1-colc tr.lv td{font-size:.85rem;color:#C2552E;height:18px}.lb-p1-colc td.sg{width:28px}.lb-p1-colc tr.ab td{border-bottom:3px solid #253638}.lb-p1-colc tr.rs td{color:#066A6E}.lb-p1-colc td.on{background:#D7F0E9;border-radius:8px}',
    '.lb-p1-arr{display:flex;flex-direction:column;align-items:center;gap:4px;margin:8px 0}.lb-p1-arf{position:relative;display:flex;gap:4px;padding:2px 4px;border-radius:10px}.lb-p1-arf.on{background:#D7F0E9;outline:2px solid #087E83}.lb-p1-arf span{font-size:1.6rem;line-height:1.2;border-radius:8px;padding:0 2px}.lb-p1-arf span.on{background:#FFE1D6}.lb-p1-arf span.ya{opacity:.6}.lb-p1-arf small{position:absolute;right:-30px;top:6px;background:#087E83;color:#fff;font-weight:800;border-radius:10px;padding:0 6px;font-size:.8rem}',
    '.lb-p1-ops{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:12px}.lb-p1-op{min-width:90px;padding:12px 16px;border:3px solid #087E83;border-radius:16px;background:#fff;font:inherit;font-weight:800;font-size:1.2rem;color:#253638;cursor:pointer;word-break:break-word}.lb-p1-op.on{background:#087E83;color:#fff}'
  ].join('');
  document.head.appendChild(css);
})();
