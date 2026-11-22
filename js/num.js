/* Trayecto Número: herramientas para ver el número y práctica diaria de cálculo.
   Todo se arma con código: no hay lecciones nuevas ni IA. */
(function () {
  'use strict';
  var sb = window.Wave && Wave.sb;

  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function hoy() { return new Date().toLocaleDateString('en-CA', { timeZone: 'America/Argentina/Buenos_Aires' }); }
  function azar(a, b) { return a + Math.floor(Math.random() * (b - a + 1)); }

  // ---------- Ventana ----------
  var abierta = null;
  function cerrar() {
    if (abierta) { abierta.remove(); abierta = null; document.removeEventListener('keydown', alTeclado); }
  }
  function alTeclado(e) { if (e.key === 'Escape') cerrar(); }
  function ventana(titulo, ancho) {
    cerrar();
    var ov = document.createElement('div');
    ov.className = 'num-ov';
    ov.innerHTML = '<div class="num-box" role="dialog" aria-modal="true" aria-label="' + esc(titulo) + '"' + (ancho ? ' style="max-width:' + ancho + 'px"' : '') + '>' +
      '<div class="num-cab"><h2>' + esc(titulo) + '</h2><button type="button" class="num-x" aria-label="Cerrar">×</button></div><div class="num-cuerpo"></div></div>';
    ov.addEventListener('click', function (e) { if (e.target === ov || e.target.closest('.num-x')) cerrar(); });
    document.body.appendChild(ov);
    document.addEventListener('keydown', alTeclado);
    abierta = ov;
    return ov.querySelector('.num-cuerpo');
  }

  // =====================================================================
  //  HERRAMIENTAS
  // =====================================================================
  // ----- Recta numérica -----
  function rectaNumerica(c) {
    var R = { max: 20, pos: null, saltos: [] };
    function paso() { return R.max <= 20 ? 1 : R.max <= 100 ? 10 : 100; }
    function salto() { return R.max <= 20 ? [1, 5, 10] : R.max <= 100 ? [1, 10, 50] : [10, 100, 500]; }
    function x(v) { return 30 + (v / R.max) * 540; }
    function dibuja() {
      var p = paso(), t = '', i;
      for (i = 0; i <= R.max; i += p) {
        t += '<line x1="' + x(i) + '" y1="78" x2="' + x(i) + '" y2="' + (i % (p * (R.max <= 20 ? 5 : 1)) === 0 ? 94 : 88) + '" stroke="currentColor" stroke-width="2"/>' +
          '<text x="' + x(i) + '" y="112" text-anchor="middle" font-size="' + (R.max <= 20 ? 11 : 12) + '" fill="currentColor">' + i + '</text>';
      }
      var arcos = R.saltos.map(function (s) {
        var a = x(s.de), b = x(s.a), m = (a + b) / 2, h = 62 - Math.min(40, Math.abs(b - a) / 6);
        return '<path d="M' + a + ' 78 Q' + m + ' ' + h + ' ' + b + ' 78" fill="none" stroke="#E4572E" stroke-width="3"/>' +
          '<text x="' + m + '" y="' + (h - 4) + '" text-anchor="middle" font-size="12" font-weight="700" fill="#E4572E">' + (s.a > s.de ? '+' : '−') + Math.abs(s.a - s.de) + '</text>';
      }).join('');
      var punto = R.pos == null ? '' : '<circle cx="' + x(R.pos) + '" cy="78" r="8" fill="#087E83"/>';
      c.querySelector('.rn-svg').innerHTML = '<line x1="30" y1="78" x2="570" y2="78" stroke="currentColor" stroke-width="3"/>' + t + arcos + punto;
      var cuenta = R.saltos.length ? R.saltos[0].de + R.saltos.map(function (s) { return ' ' + (s.a > s.de ? '+' : '−') + ' ' + Math.abs(s.a - s.de); }).join('') + ' = ' + R.pos : '';
      var sl = salto(), bs = '';
      sl.slice().reverse().forEach(function (n) { bs += '<button type="button" class="num-b num-b2" data-j="-' + n + '">−' + n + '</button>'; });
      sl.forEach(function (n) { bs += '<button type="button" class="num-b num-b2" data-j="' + n + '">+' + n + '</button>'; });
      c.querySelector('.rn-saltos').innerHTML = bs;
      c.querySelector('.rn-info').textContent = R.pos == null ? 'Tocá la recta para elegir dónde empezar.' : (cuenta || 'Estás en el ' + R.pos + '. Usá los botones para saltar.');
    }
    c.innerHTML = '<div class="num-fila"><b>Hasta:</b>' + [10, 20, 100, 1000].map(function (m) { return '<button type="button" class="num-b" data-max="' + m + '">' + m + '</button>'; }).join('') + '</div>' +
      '<svg class="rn-svg" viewBox="0 0 600 130" role="img" aria-label="Recta numérica" style="width:100%;color:#17323a;touch-action:manipulation"></svg>' +
      '<p class="rn-info num-info"></p>' +
      '<div class="num-fila rn-saltos"></div><div class="num-fila"><button type="button" class="num-b num-limpia" data-limpia="1">Empezar de nuevo</button></div>';
    c.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (b && b.dataset.max) { R.max = +b.dataset.max; R.pos = null; R.saltos = []; dibuja(); return; }
      if (b && b.dataset.j != null) {
        if (R.pos == null) { R.pos = 0; }
        var n = +b.dataset.j;
        var nuevo = Math.max(0, Math.min(R.max, R.pos + n));
        if (nuevo !== R.pos) { R.saltos.push({ de: R.pos, a: nuevo }); R.pos = nuevo; }
        dibuja(); return;
      }
      if (b && b.dataset.limpia) { R.pos = null; R.saltos = []; dibuja(); return; }
    });
    c.querySelector('.rn-svg').addEventListener('click', function (e) {
      var svg = e.currentTarget, r = svg.getBoundingClientRect(), px = (e.clientX - r.left) / r.width * 600;
      var snap = R.max <= 100 ? 1 : 10, v = Math.round(((px - 30) / 540) * R.max / snap) * snap;
      R.pos = Math.max(0, Math.min(R.max, v)); R.saltos = []; dibuja();
    });
    dibuja();
  }

  // ----- Bloques de base 10 -----
  function bloquesBase10(c) {
    var B = { m: 0, c: 0, d: 0, u: 0 };
    var NOM = { m: 'Miles', c: 'Centenas', d: 'Decenas', u: 'Unidades' }, VAL = { m: 1000, c: 100, d: 10, u: 1 };
    function pieza(k) {
      var s = '';
      for (var i = 0; i < B[k]; i++) {
        s += k === 'u' ? '<i class="b10-u"></i>' : k === 'd' ? '<i class="b10-d"></i>' : k === 'c' ? '<i class="b10-c"></i>' : '<i class="b10-m"></i>';
      }
      return s;
    }
    function pinta() {
      var total = B.m * 1000 + B.c * 100 + B.d * 10 + B.u;
      var hay = ['u', 'd', 'c'].some(function (k) { return B[k] >= 10; });
      c.innerHTML = '<div class="b10-num">' + total + '</div>' +
        '<div class="b10-cols">' + ['m', 'c', 'd', 'u'].map(function (k) {
          return '<div class="b10-col"><b>' + NOM[k] + '</b><div class="b10-pz">' + pieza(k) + '</div><div class="num-fila">' +
            '<button type="button" class="num-b" data-k="' + k + '" data-n="-1" aria-label="Sacar uno de ' + NOM[k] + '">−</button><span class="b10-cuenta">' + B[k] + '</span>' +
            '<button type="button" class="num-b" data-k="' + k + '" data-n="1" aria-label="Agregar uno de ' + NOM[k] + '">+</button></div></div>';
        }).join('') + '</div>' +
        (hay ? '<p class="num-info">¡Hay 10 piezas iguales! Se pueden cambiar por 1 pieza de la columna de al lado.</p>' : '') +
        '<div class="num-fila"><button type="button" class="num-b num-b2" data-agrupar="1"' + (hay ? '' : ' disabled') + '>Agrupar de a 10</button><button type="button" class="num-b num-limpia" data-limpia="1">Empezar de nuevo</button></div>';
    }
    c.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.dataset.k) { B[b.dataset.k] = Math.max(0, Math.min(b.dataset.k === 'm' ? 9 : 19, B[b.dataset.k] + (+b.dataset.n))); pinta(); }
      else if (b.dataset.agrupar) {
        if (B.u >= 10) { B.u -= 10; B.d++; } if (B.d >= 10) { B.d -= 10; B.c++; } if (B.c >= 10) { B.c -= 10; B.m = Math.min(9, B.m + 1); } pinta();
      } else if (b.dataset.limpia) { B = { m: 0, c: 0, d: 0, u: 0 }; pinta(); }
    });
    pinta();
  }

  // ----- Barras de fracciones -----
  function barrasFracciones(c) {
    var F = [{ den: 4, sel: 1 }, { den: 4, sel: 2 }];
    function barra(i) {
      var f = F[i], s = '';
      for (var k = 0; k < f.den; k++) s += '<button type="button" class="fr-seg' + (k < f.sel ? ' on' : '') + '" data-i="' + i + '" data-k="' + k + '" aria-label="Parte ' + (k + 1) + ' de ' + f.den + '"></button>';
      var opts = ''; for (var d = 1; d <= 12; d++) opts += '<option value="' + d + '"' + (d === f.den ? ' selected' : '') + '>' + d + '</option>';
      return '<div class="fr-bloque"><div class="fr-cab"><label>Partes iguales: <select data-den="' + i + '">' + opts + '</select></label><b class="fr-val">' + f.sel + '/' + f.den + '</b></div><div class="fr-barra">' + s + '</div></div>';
    }
    function pinta() {
      var a = F[0].sel * F[1].den, b = F[1].sel * F[0].den;
      var rel = a === b ? 'son iguales' : a < b ? 'la de arriba es menor' : 'la de arriba es mayor';
      c.innerHTML = barra(0) + barra(1) + '<p class="num-info">' + F[0].sel + '/' + F[0].den + ' y ' + F[1].sel + '/' + F[1].den + ': ' + rel + '.</p><p class="num-info">Tocá las partes para pintarlas.</p>';
    }
    c.addEventListener('click', function (e) {
      var b = e.target.closest('.fr-seg'); if (!b) return;
      var f = F[+b.dataset.i], k = +b.dataset.k + 1; f.sel = f.sel === k ? k - 1 : k; pinta();
    });
    c.addEventListener('change', function (e) {
      var s = e.target.closest('select[data-den]'); if (!s) return;
      var f = F[+s.dataset.den]; f.den = +s.value; f.sel = Math.min(f.sel, f.den); pinta();
    });
    pinta();
  }

  // ----- Valor posicional -----
  function valorPosicional(c) {
    c.innerHTML = '<label class="num-info">Escribí un número: <input type="text" class="vp-in" inputmode="decimal" maxlength="14" value="4352" aria-label="Número"></label><div class="vp-out"></div>';
    var inp = c.querySelector('.vp-in'), out = c.querySelector('.vp-out');
    var ENT = ['CM', 'DM', 'UM', 'C', 'D', 'U'], GR = ['Millones', 'Miles', 'Unidades'], DEC = ['d', 'c', 'm'];
    function pinta() {
      var t = inp.value.replace(',', '.').replace(/[^0-9.]/g, ''), partes = t.split('.');
      var e = (partes[0] || '0').replace(/^0+(?=\d)/, '').slice(-9), dd = (partes[1] || '').slice(0, 3);
      var enteros = ('000000000' + e).slice(-9).split(''), decs = (dd + '000').slice(0, 3).split('');
      var nombres = ['Centenas de millón', 'Decenas de millón', 'Unidades de millón', 'Centenas de mil', 'Decenas de mil', 'Unidades de mil', 'Centenas', 'Decenas', 'Unidades'];
      var head = '', fila = '', i;
      var first = enteros.findIndex(function (x) { return x !== '0'; }); if (first < 0) first = 8;
      for (i = first; i < 9; i++) {
        head += '<th>' + ['CM', 'DM', 'UM', 'C', 'D', 'U', 'C', 'D', 'U'][i] + '</th>';
        fila += '<td title="' + nombres[i] + '">' + enteros[i] + '</td>';
      }
      var hayDec = dd.length > 0;
      if (hayDec) { head += '<th class="vp-coma">,</th>'; fila += '<td class="vp-coma">,</td>'; DEC.forEach(function (n, j) { if (j < dd.length) { head += '<th>' + n + '</th>'; fila += '<td>' + decs[j] + '</td>'; } }); }
      var desc = [], pot = [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1];
      for (i = first; i < 9; i++) if (enteros[i] !== '0') desc.push(enteros[i] + ' × ' + pot[i].toLocaleString('es-AR'));
      var potd = ['0,1', '0,01', '0,001'];
      for (i = 0; i < dd.length; i++) if (decs[i] !== '0') desc.push(decs[i] + ' × ' + potd[i]);
      out.innerHTML = '<table class="vp-tab"><thead><tr>' + head + '</tr></thead><tbody><tr>' + fila + '</tr></tbody></table>' +
        '<p class="num-info"><b>Se descompone así:</b><br>' + (desc.length ? desc.join(' + ') : '0') + '</p>' +
        '<p class="num-info vp-ayuda">C = centenas, D = decenas, U = unidades, M = miles' + (hayDec ? ', d = décimos, c = centésimos, m = milésimos' : '') + '.</p>';
    }
    inp.addEventListener('input', pinta); pinta();
  }

  var TABS = [['recta', 'Recta numérica', rectaNumerica], ['bloques', 'Bloques de 10', bloquesBase10], ['fracc', 'Fracciones', barrasFracciones], ['valor', 'Valor posicional', valorPosicional]];
  var ultimaTab = 'recta';
  function herramientas(ini) {
    var cuerpo = ventana('Herramientas para ver el número', 640);
    cuerpo.innerHTML = '<div class="num-tabs" role="tablist">' + TABS.map(function (t) { return '<button type="button" role="tab" class="num-tab" data-t="' + t[0] + '">' + t[1] + '</button>'; }).join('') + '</div><div class="num-panel"></div>';
    function ir(id) {
      ultimaTab = id;
      cuerpo.querySelectorAll('.num-tab').forEach(function (b) { b.setAttribute('aria-selected', b.dataset.t === id ? 'true' : 'false'); });
      var p = cuerpo.querySelector('.num-panel'), nuevo = p.cloneNode(false); p.replaceWith(nuevo);
      TABS.filter(function (t) { return t[0] === id; })[0][2](nuevo);
    }
    cuerpo.querySelector('.num-tabs').addEventListener('click', function (e) { var b = e.target.closest('.num-tab'); if (b) ir(b.dataset.t); });
    ir(ini || ultimaTab);
  }

  // Botón flotante dentro de la materia
  function botonHerramientas(mostrar) {
    var b = document.getElementById('num-flota');
    if (!mostrar) { if (b) b.remove(); return; }
    if (b) return;
    b = document.createElement('button');
    b.id = 'num-flota'; b.type = 'button'; b.className = 'num-flota'; b.setAttribute('aria-label', 'Abrir herramientas para ver el número');
    b.innerHTML = '<span aria-hidden="true">📏</span> Herramientas';
    b.addEventListener('click', function () { herramientas(); });
    document.body.appendChild(b);
  }

  // =====================================================================
  //  PRÁCTICA DIARIA DE CÁLCULO
  // =====================================================================
  var NIVELES = [
    function () { var a = azar(1, 9), b = azar(1, 10 - a); return { q: a + ' + ' + b, a: a + b }; },
    function () { var a = azar(1, 20); if (Math.random() < .5) { var b = azar(0, 20 - a); return { q: a + ' + ' + b, a: a + b }; } var c = azar(0, a); return { q: a + ' − ' + c, a: a - c }; },
    function () { var a = azar(10, 99), b = azar(5, 90); return Math.random() < .5 ? { q: a + ' + ' + b, a: a + b } : (a >= b ? { q: a + ' − ' + b, a: a - b } : { q: b + ' − ' + a, a: b - a }); },
    function () { var a = azar(2, 5), b = azar(1, 10); return { q: a + ' × ' + b, a: a * b }; },
    function () { var a = azar(2, 10), b = azar(1, 10); return { q: a + ' × ' + b, a: a * b }; },
    function () { var a = azar(2, 10), b = azar(1, 10); return { q: (a * b) + ' ÷ ' + a, a: b }; },
    function () { var a = azar(100, 999), b = azar(100, 999); return Math.random() < .5 ? { q: a + ' + ' + b, a: a + b } : (a >= b ? { q: a + ' − ' + b, a: a - b } : { q: b + ' − ' + a, a: b - a }); },
    function () { var a = azar(11, 99), b = azar(2, 9); return { q: a + ' × ' + b, a: a * b }; }
  ];
  function generar(nivel) {
    return NIVELES[Math.max(0, Math.min(NIVELES.length - 1, nivel - 1))]();
  }

  async function estadoHoy(sid) {
    var r = await sb.from('practica_calculo').select('dia, nivel, correctas, total, errores').eq('student_id', sid).order('dia', { ascending: false }).limit(2);
    var filas = r.data || [], h = hoy();
    return { hoy: filas.filter(function (f) { return f.dia === h; })[0] || null, ultima: filas[0] || null };
  }

  async function practica(sid) {
    var cuerpo = ventana('Práctica de cálculo de hoy', 520);
    cuerpo.innerHTML = '<p class="num-info">Cargando…</p>';
    var st = { hoy: null, ultima: null };
    try { st = await estadoHoy(sid); } catch (e) { /* sin datos previos: empieza en el nivel 1 */ }
    if (!abierta) return;
    var TOTAL = 20, nivel = st.ultima ? Math.max(1, st.ultima.nivel) : 1;
    var previos = ((st.ultima && st.ultima.errores) || []).slice(0, 4);
    var S = { i: 0, ok: 0, racha: 0, fallas: 0, cola: previos.slice(), nuevosErrores: [], actual: null, nivelMax: nivel };

    function siguiente() {
      if (S.i >= TOTAL) return fin();
      var g;
      if (S.cola.length && (S.i % 4 === 3 || S.cola.length + S.i >= TOTAL)) g = S.cola.shift(); else g = generar(nivel);
      S.actual = g; S.i++;
      cuerpo.innerHTML = '<div class="pc-barra" role="progressbar" aria-valuemin="0" aria-valuemax="' + TOTAL + '" aria-valuenow="' + (S.i - 1) + '"><span style="width:' + Math.round(((S.i - 1) / TOTAL) * 100) + '%"></span></div>' +
        '<p class="pc-prog">Cuenta ' + S.i + ' de ' + TOTAL + '</p><div class="pc-q">' + esc(g.q) + ' = ?</div>' +
        '<form class="pc-form"><input class="pc-in" type="text" inputmode="numeric" autocomplete="off" maxlength="7" aria-label="Tu respuesta"><button type="submit" class="num-b num-b2">Comprobar</button></form><div class="pc-fb" aria-live="polite"></div>';
      var inp = cuerpo.querySelector('.pc-in'); inp.focus();
      cuerpo.querySelector('.pc-form').addEventListener('submit', function (e) { e.preventDefault(); responde(inp.value); });
    }
    function responde(v) {
      v = String(v).trim(); if (v === '') return;
      var ok = Number(v) === S.actual.a, fb = cuerpo.querySelector('.pc-fb');
      cuerpo.querySelector('.pc-form').remove();
      if (ok) { S.ok++; S.racha++; S.fallas = 0; if (S.racha >= 3 && nivel < NIVELES.length) { nivel++; S.racha = 0; S.nivelMax = Math.max(S.nivelMax, nivel); } }
      else { S.racha = 0; S.fallas++; S.nuevosErrores.push(S.actual); if (S.cola.length < 3 && !S.actual.rep) S.cola.push({ q: S.actual.q, a: S.actual.a, rep: true }); if (S.fallas >= 2 && nivel > 1) { nivel--; S.fallas = 0; } }
      fb.innerHTML = '<div class="pc-res ' + (ok ? 'ok' : 'mal') + '">' + (ok ? '¡Bien!' : 'No es ' + esc(v) + '. La respuesta es <b>' + S.actual.a + '</b>.') + '</div><button type="button" class="num-b num-b2 pc-sig">' + (S.i >= TOTAL ? 'Terminar' : 'Siguiente') + '</button>';
      var b = fb.querySelector('.pc-sig'); b.focus(); b.addEventListener('click', siguiente);
    }
    async function fin() {
      cuerpo.innerHTML = '<div class="pc-fin"><div class="pc-trofeo" aria-hidden="true">🏆</div><h3>¡Listo por hoy!</h3><p>Acertaste <b>' + S.ok + '</b> de ' + TOTAL + ' cuentas.</p><p class="num-info">Las que se te complicaron vuelven a aparecer mañana, para que te queden.</p><button type="button" class="num-b num-b2" data-cerrar="1">Cerrar</button></div>';
      cuerpo.querySelector('[data-cerrar]').addEventListener('click', function () { cerrar(); document.dispatchEvent(new CustomEvent('wave-num-practica')); });
      try {
        var prev = st.hoy, errores = S.nuevosErrores.slice(0, 6).map(function (e) { return { q: e.q, a: e.a }; });
        await sb.from('practica_calculo').upsert({
          student_id: sid, dia: hoy(), nivel: S.nivelMax,
          correctas: (prev ? prev.correctas : 0) + S.ok, total: (prev ? prev.total : 0) + TOTAL, errores: errores, updated_at: new Date().toISOString()
        }, { onConflict: 'student_id,dia' });
      } catch (e) { /* si no se guarda, igual terminó */ }
    }
    siguiente();
  }

  // Tarjeta para "Mis cursos"
  async function tarjetaPractica(sid) {
    var st = { hoy: null };
    try { st = await estadoHoy(sid); } catch (e) { /* se muestra sin estado */ }
    var h = st.hoy;
    return '<section class="num-card"><div><h2>Práctica de cálculo de hoy</h2><p>' + (h ? 'Hecha hoy ✓ Acertaste ' + h.correctas + ' de ' + h.total + '.' : '20 cuentas, unos 10 minutos. Van subiendo de dificultad a tu ritmo.') + '</p></div>' +
      '<button type="button" class="num-b num-b2" data-num-practica="1" data-sid="' + esc(sid) + '">' + (h ? 'Hacer otra vez' : 'Empezar') + '</button></section>';
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-num-practica]');
    if (!b) return;
    var sid = b.getAttribute('data-sid');
    if (sid) practica(sid);
  });

  window.WaveNum = { herramientas: herramientas, botonHerramientas: botonHerramientas, practica: practica, tarjetaPractica: tarjetaPractica };
})();
