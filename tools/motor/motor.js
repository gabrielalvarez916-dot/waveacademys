/* MOTOR DE JUEGOS INTERACTIVOS DE WAVE ACADEMY
   Toma un SPEC (historia + desafíos + pasos) y arma el juego completo. Cada paso tiene un "t" (tipo) del catálogo T.
   Cada paso vale 1 punto a la primera, 0,5 a la segunda y 0 si falla; al final avisa el porcentaje a la plataforma. */
(function () {
  var SPEC = window.SPEC, app = document.getElementById('app'), E = {};

  // ---------- utilidades ----------
  function S(t) { // texto de la IA: se escapa todo y se permiten solo unas pocas marcas
    return String(t == null ? '' : t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/&lt;(\/?)(b|i|sub|sup|br)&gt;/g, '<$1$2>');
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }
  function baraja(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function suma(a) { return a.reduce(function (x, y) { return x + y; }, 0); }
  function pad(n, len) { n = String(n); while (n.length < len) n = '0' + n; return n; }
  function on(sel, ev, fn) { [].forEach.call(app.querySelectorAll(sel), function (el) { el['on' + ev] = function () { fn(el); }; }); }
  function igualArr(a, b) { return a.length === b.length && a.every(function (x, i) { return x === b[i]; }); }
  var DES = SPEC.desafios, ND = DES.length;
  function nPasos(d) { return DES[d].pasos.length; }

  // ---------- pantalla base ----------
  function hud() {
    var h = '<div class="hud"><div class="pasos">';
    for (var d = 0; d < ND; d++) { var w = E.cred && E.cred[d] ? Math.round(E.cred[d].length / nPasos(d) * 100) : 0; h += '<i><b style="width:' + w + '%"></b></i>'; }
    return h + '</div><span class="chip">⭐ ' + (E.pts || 0) + '</span></div>';
  }
  function pintar(h, cls) { clearTimeout(E.tm); app.innerHTML = hud() + '<div class="escena ' + (cls || '') + '">' + h + '</div><div class="fb" id="fb"></div>'; }
  function fb(tipo, html, botones) {
    var f = document.getElementById('fb'); f.className = 'fb ver ' + tipo;
    f.innerHTML = '<div>' + html + '</div><span class="bt">' + botones.map(function (b, i) { return '<button class="btn" data-b="' + i + '">' + b[0] + '</button>'; }).join('') + '</span>';
    [].forEach.call(f.querySelectorAll('[data-b]'), function (el) { el.onclick = function () { botones[+el.dataset.b][1](); }; });
    var es = app.querySelector('.escena'); if (es) { es.classList.add('confb'); es.scrollTop = es.scrollHeight; }
  }
  function sinFb() { var f = document.getElementById('fb'); if (f) f.className = 'fb'; var es = app.querySelector('.escena'); if (es) es.classList.remove('confb'); }
  function cab() { var d = DES[E.d]; return '<div><div class="etq">' + S(d.ico || '⭐') + ' Desafío ' + (E.d + 1) + ' · ' + (E.a + 1) + ' de ' + nPasos(E.d) + '</div></div>'; }

  // ---------- veredicto común: 2 intentos (A.uno = un solo intento) ----------
  function veredicto(A, ok, h) {
    if (ok) {
      var c = E.int === 1 ? 1 : .5; h.bloquear();
      fb('bien', (c === 1 ? '¡Perfecto!' : '¡Bien, a la segunda!') + '<small>' + S(A.exp || '') + '</small>', [['Seguir ➜', function () { anotar(c); }]]); return;
    }
    if (E.int === 1 && !A.uno) {
      E.int = 2; h.marcar();
      fb('mal', 'Casi. Tenés otra oportunidad (vale medio punto).<small>' + S(A.pista || '') + '</small>', [['Probar de nuevo', function () { h.reintento(); sinFb(); }]]); return;
    }
    h.revelar();
    fb('mal', 'Esta vez no salió. Mirá cómo se resuelve:<small>' + S(A.exp || '') + '</small>', [['Seguir ➜', function () { anotar(0); }]]);
  }
  function anotar(c) { E.cred[E.d].push(c); E.pts += Math.round(c * 10); E.a++; if (E.a >= nPasos(E.d)) finDesafio(); else jugar(); }
  function botonComprobar(lock, habilitado) { return '<button class="btn" id="ok"' + (lock || !habilitado ? ' disabled' : '') + '>Comprobar</button>'; }

  var T = {};

  // ================= TIPOS GENÉRICOS (sirven para cualquier materia) =================
  // op: elegir una opción. {q, tarjeta?, ops[], ok, mezclar?, seg? (relámpago con tiempo, un solo intento)}
  T.op = function (A) {
    var opts = A.ops.map(function (t, i) { return { t: t, ok: i === A.ok }; }); if (A.mezclar !== false) opts = baraja(opts);
    var sel = -1, malas = [], lock = false, mostrarOk = false, rapido = !!A.seg; if (rapido) A.uno = true;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2>' + (A.tarjeta ? '<div class="tarjeta' + (String(A.tarjeta).length > 14 ? ' chica' : '') + '">' + S(A.tarjeta) + '</div>' : '') +
        (rapido && !lock ? '<div class="tiempo"><b id="tb"></b></div>' : '') +
        '<div class="ops' + (A.ops.length === 2 ? ' dos' : '') + '">' + opts.map(function (o, i) {
          var c = 'op' + (i === sel ? ' sel' : '') + (malas.indexOf(i) >= 0 ? ' mal' : '') + (mostrarOk && o.ok ? ' bien' : '') + (lock && !o.ok && malas.indexOf(i) < 0 ? ' gris' : '');
          return '<button class="' + c + '" data-o="' + i + '"' + (lock || malas.indexOf(i) >= 0 ? ' disabled' : '') + '>' + S(o.t) + '</button>';
        }).join('') + '</div>' + (rapido ? '' : botonComprobar(lock, sel >= 0));
      pintar(h);
      var hk = {
        bloquear: function () { lock = true; mostrarOk = true; dib(); },
        marcar: function () { malas.push(sel); sel = -1; dib(); }, reintento: function () { },
        revelar: function () { if (sel >= 0) malas.push(sel); lock = true; mostrarOk = true; sel = -1; dib(); }
      };
      if (rapido && !lock) {
        var tb = document.getElementById('tb'); tb.style.transition = 'width ' + A.seg + 's linear'; setTimeout(function () { tb.style.width = '0%'; }, 30);
        E.tm = setTimeout(function () { veredicto(A, false, hk); }, A.seg * 1000);
      }
      on('[data-o]', 'click', function (b) {
        sel = +b.dataset.o;
        if (rapido) { clearTimeout(E.tm); veredicto(A, opts[sel].ok, hk); } else dib();
      });
      var ok = document.getElementById('ok');
      if (ok) ok.onclick = function () { veredicto(A, opts[sel].ok, hk); };
    }
    dib();
  };

  // vf: verdadero o falso. {q, ok:true|false, uno?}
  T.vf = function (A) {
    var lock = false, sel = null, ver = null;
    function dib() {
      var h = cab() + '<h2>Verdadero o falso</h2><div class="tarjeta chica">' + S(A.q) + '</div><div class="vf">' + [true, false].map(function (v) {
        var c = 'op' + (lock && v === A.ok ? ' bien' : '') + (sel === v && ver === false ? ' mal' : '');
        return '<button class="' + c + '" data-v="' + v + '"' + (lock ? ' disabled' : '') + '>' + (v ? '✔ Verdadero' : '✘ Falso') + '</button>';
      }).join('') + '</div>';
      pintar(h);
      on('[data-v]', 'click', function (b) {
        sel = b.dataset.v === 'true'; ver = sel === A.ok;
        veredicto(A, ver, { bloquear: function () { lock = true; dib(); }, marcar: function () { dib(); sel = null; }, reintento: function () { dib(); }, revelar: function () { lock = true; dib(); } });
      });
    }
    dib();
  };

  // multi: marcar todas las correctas. {q, ops[], oks[indices]}
  T.multi = function (A) {
    var opts = baraja(A.ops.map(function (t, i) { return { t: t, ok: A.oks.indexOf(i) >= 0 }; })), sel = [], err = [], lock = false, rev = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><p style="text-align:center">Puede haber más de una correcta.</p><div class="ops">' + opts.map(function (o, i) {
        var c = 'op' + (sel.indexOf(i) >= 0 ? ' sel' : '') + (err.indexOf(i) >= 0 ? ' mal' : '') + (rev && o.ok ? ' bien' : '') + (lock && !rev && sel.indexOf(i) >= 0 ? ' bien' : '');
        return '<button class="' + c + '" data-o="' + i + '"' + (lock ? ' disabled' : '') + '>' + S(o.t) + '</button>';
      }).join('') + '</div>' + botonComprobar(lock, sel.length);
      pintar(h);
      on('[data-o]', 'click', function (b) { var i = +b.dataset.o, k = sel.indexOf(i); if (k >= 0) sel.splice(k, 1); else sel.push(i); err = []; dib(); });
      document.getElementById('ok').onclick = function () {
        var mal = []; opts.forEach(function (o, i) { if ((sel.indexOf(i) >= 0) !== o.ok) mal.push(i); });
        veredicto(A, !mal.length, { bloquear: function () { lock = true; dib(); }, marcar: function () { err = mal; dib(); }, reintento: function () { err = []; dib(); }, revelar: function () { lock = true; rev = true; err = []; dib(); } });
      };
    }
    dib();
  };

  // armar: armar una palabra, número o frase tocando piezas en orden. {q, piezas[], extra[]?, sol (texto unido), union?:'' (separador, '' para cifras/letras, ' ' para palabras)}
  T.armar = function (A) {
    var uni = A.union == null ? '' : A.union, base = baraja(A.piezas.concat(A.extra || [])).map(function (t, i) { return { t: t, i: i }; }), puestas = [], lock = false, ok = false, mal = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><div class="ranuras" style="' + (mal ? 'border-color:var(--coral)' : ok ? 'border-color:var(--aqua)' : '') + '">' + puestas.map(function (p) { return '<button class="pz" data-q="' + p.i + '"' + (lock ? ' disabled' : '') + '>' + S(p.t) + '</button>'; }).join('') + '</div>' +
        '<div class="piezas">' + base.map(function (p) { return '<button class="pz' + (puestas.indexOf(p) >= 0 ? ' usada' : '') + '" data-p="' + p.i + '"' + (lock ? ' disabled' : '') + '>' + S(p.t) + '</button>'; }).join('') + '</div>' + botonComprobar(lock, puestas.length);
      pintar(h);
      on('[data-p]', 'click', function (b) { var p = base.filter(function (x) { return x.i === +b.dataset.p; })[0]; puestas.push(p); mal = false; dib(); });
      on('[data-q]', 'click', function (b) { puestas = puestas.filter(function (x) { return x.i !== +b.dataset.q; }); mal = false; dib(); });
      document.getElementById('ok').onclick = function () {
        var v = puestas.map(function (p) { return p.t; }).join(uni) === String(A.sol);
        veredicto(A, v, { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { mal = true; dib(); }, reintento: function () { puestas = []; mal = false; dib(); }, revelar: function () { lock = true; mal = false; puestas = String(A.sol).split(uni).map(function (t) { return base.filter(function (x) { return x.t === t; })[0] || { t: t, i: -1 }; }); dib(); } });
      };
    }
    dib();
  };

  // ordenar: ordenar elementos tocándolos en el orden correcto. {q, items[] (en orden correcto)}
  T.ordenar = function (A) {
    var base = baraja(A.items.map(function (t, i) { return { t: t, k: i }; })), orden = [], err = false, lock = false, ok = false;
    if (base.every(function (x, i) { return x.k === i; }) && base.length > 1) base.reverse();
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><p style="text-align:center">Tocalos en el orden correcto. Tocá uno puesto para sacarlo.</p><div class="ops">' + base.map(function (x) {
        var pos = orden.indexOf(x), c = 'fila-ord' + (pos >= 0 ? ' puesta' : '') + (lock && ok ? ' bien' : '') + (err && pos >= 0 && orden[pos].k !== pos ? ' mal' : '');
        return '<button class="' + c + '" data-x="' + x.k + '"' + (lock ? ' disabled' : '') + '><i>' + (pos >= 0 ? pos + 1 : '·') + '</i>' + S(x.t) + '</button>';
      }).join('') + '</div>' + botonComprobar(lock, orden.length === base.length);
      pintar(h);
      on('[data-x]', 'click', function (b) { var x = base.filter(function (y) { return y.k === +b.dataset.x; })[0], p = orden.indexOf(x); if (p >= 0) orden.splice(p, 1); else orden.push(x); err = false; dib(); });
      document.getElementById('ok').onclick = function () {
        veredicto(A, orden.every(function (x, i) { return x.k === i; }), { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { err = true; dib(); }, reintento: function () { orden = []; err = false; dib(); }, revelar: function () { lock = true; err = false; orden = base.slice().sort(function (a, b) { return a.k - b.k; }); dib(); } });
      };
    }
    dib();
  };

  // unir: unir cada elemento de la izquierda con el de la derecha. {q, pares:[[izq,der],...]}
  T.unir = function (A) {
    var izq = A.pares.map(function (p, i) { return { t: p[0], k: i }; }), der = baraja(A.pares.map(function (p, i) { return { t: p[1], k: i }; })), un = {}, selI = -1, err = [], lock = false;
    function dib() {
      var claves = Object.keys(un);
      var cI = function (k) { var p = claves.indexOf(String(k)); return p >= 0 ? ' c' + (p % 6) : ''; };
      var cD = function (k) { var dueno = claves.filter(function (i) { return un[i] === k; })[0]; return dueno != null ? cI(dueno) : ''; };
      var filas = '';
      izq.forEach(function (x, n) {
        filas += '<button class="par' + (selI === x.k ? ' sel' : '') + cI(x.k) + (err.indexOf(x.k) >= 0 ? ' mal' : '') + '" data-i="' + x.k + '"' + (lock ? ' disabled' : '') + '>' + S(x.t) + '</button>' +
          '<button class="par' + cD(der[n].k) + '" data-d="' + der[n].k + '"' + (lock ? ' disabled' : '') + '>' + S(der[n].t) + '</button>';
      });
      var h = cab() + '<h2>' + S(A.q) + '</h2><p style="text-align:center">Tocá uno de la izquierda y después su pareja de la derecha.</p><div class="pares">' + filas + '</div>' + botonComprobar(lock, claves.length === izq.length);
      pintar(h);
      on('[data-i]', 'click', function (b) { var k = +b.dataset.i; if (un[k] != null && selI !== k) { delete un[k]; } selI = k; err = []; dib(); });
      on('[data-d]', 'click', function (b) { if (selI < 0) return; var k = +b.dataset.d; Object.keys(un).forEach(function (i) { if (un[i] === k) delete un[i]; }); un[selI] = k; selI = -1; err = []; dib(); });
      document.getElementById('ok').onclick = function () {
        var mal = izq.filter(function (x) { return un[x.k] !== x.k; }).map(function (x) { return x.k; });
        veredicto(A, !mal.length, { bloquear: function () { lock = true; dib(); }, marcar: function () { err = mal; dib(); }, reintento: function () { err = []; dib(); }, revelar: function () { lock = true; un = {}; izq.forEach(function (x) { un[x.k] = x.k; }); err = []; dib(); } });
      };
    }
    dib();
  };

  // clasificar: tocar un elemento y después la caja donde va. {q, cajas[], items:[{t, c (índice de caja)}]}
  T.clasificar = function (A) {
    var its = baraja(A.items.map(function (x, i) { return { t: x.t, c: x.c, k: i }; })), puesto = {}, sel = -1, err = [], lock = false;
    function chipi(x, cl) { return '<button class="chipi' + (sel === x.k ? ' sel' : '') + (cl || '') + '" data-c="' + x.k + '"' + (lock ? ' disabled' : '') + '>' + S(x.t) + '</button>'; }
    function dib() {
      var sueltos = its.filter(function (x) { return puesto[x.k] == null; });
      var h = cab() + '<h2>' + S(A.q) + '</h2><div class="suelto">' + (sueltos.length ? sueltos.map(function (x) { return chipi(x); }).join('') : '<p>¡Todo clasificado! Tocá Comprobar.</p>') + '</div><div class="cajas">' +
        A.cajas.map(function (nom, ci) {
          return '<div class="caja' + (sel >= 0 ? ' lista' : '') + '" data-box="' + ci + '"><h3>' + S(nom) + '</h3><div class="dentro">' + its.filter(function (x) { return puesto[x.k] === ci; }).map(function (x) { return chipi(x, err.indexOf(x.k) >= 0 ? ' mal' : lock ? ' bien' : ''); }).join('') + '</div></div>';
        }).join('') + '</div>' + botonComprobar(lock, !sueltos.length);
      pintar(h);
      on('[data-c]', 'click', function (b) { var k = +b.dataset.c; if (puesto[k] != null) { delete puesto[k]; sel = -1; } else sel = sel === k ? -1 : k; err = []; dib(); });
      on('[data-box]', 'click', function (b) { if (sel < 0) return; puesto[sel] = +b.dataset.box; sel = -1; err = []; dib(); });
      document.getElementById('ok').onclick = function () {
        var mal = its.filter(function (x) { return puesto[x.k] !== x.c; }).map(function (x) { return x.k; });
        veredicto(A, !mal.length, { bloquear: function () { lock = true; dib(); }, marcar: function () { err = mal; dib(); }, reintento: function () { mal.forEach(function (k) { delete puesto[k]; }); err = []; dib(); }, revelar: function () { lock = true; its.forEach(function (x) { puesto[x.k] = x.c; }); err = []; dib(); } });
      };
    }
    dib();
  };

  // completar: completar huecos (___) con palabras de un banco. {q, texto con ___, banco[], sol[]}
  T.completar = function (A) {
    var partes = String(A.texto).split('___'), n = partes.length - 1, ban = baraja(A.banco.map(function (t, i) { return { t: t, k: i }; })), val = [], act = 0, err = [], lock = false, ok = false;
    for (var i = 0; i < n; i++) val.push(null);
    function dib() {
      var frase = ''; partes.forEach(function (p, i) { frase += S(p); if (i < n) frase += '<span class="hueco' + (i === act && !lock ? ' act' : '') + (err.indexOf(i) >= 0 ? ' mal' : '') + (lock && ok ? ' bien' : '') + '" data-h="' + i + '">' + (val[i] ? S(val[i].t) : '&nbsp;&nbsp;&nbsp;&nbsp;') + '</span>'; });
      var h = cab() + '<h2>' + S(A.q) + '</h2><div class="tarjeta chica" style="font-weight:800"><div class="frase">' + frase + '</div></div><div class="suelto">' + ban.map(function (x) { return '<button class="chipi" data-w="' + x.k + '"' + (lock || val.indexOf(x) >= 0 ? ' style="visibility:hidden"' : '') + (lock ? ' disabled' : '') + '>' + S(x.t) + '</button>'; }).join('') + '</div>' + botonComprobar(lock, val.every(Boolean));
      pintar(h);
      on('[data-h]', 'click', function (b) { var i = +b.dataset.h; if (val[i]) val[i] = null; act = i; err = []; dib(); });
      on('[data-w]', 'click', function (b) { var x = ban.filter(function (y) { return y.k === +b.dataset.w; })[0], i = val[act] == null ? act : val.indexOf(null); if (i < 0) return; val[i] = x; act = val.indexOf(null) >= 0 ? val.indexOf(null) : i; err = []; dib(); });
      document.getElementById('ok').onclick = function () {
        var mal = []; val.forEach(function (x, i) { if (x.t !== A.sol[i]) mal.push(i); });
        veredicto(A, !mal.length, { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { err = mal; dib(); }, reintento: function () { mal.forEach(function (i) { val[i] = null; }); act = val.indexOf(null); err = []; dib(); }, revelar: function () { lock = true; err = []; val = A.sol.map(function (t) { return { t: t }; }); dib(); } });
      };
    }
    dib();
  };

  // numero: escribir una respuesta numérica con el teclado de la pantalla. {q, sol (texto), aceptadas?[], unidad?}
  T.numero = function (A) {
    var v = '', lock = false, ok = false, mal = false;
    var norm = function (s) { return String(s).replace(/[\s.]/g, '').replace(',', '.'); };
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><div class="vis-num' + (mal ? ' mal' : '') + (lock && ok ? ' bien' : '') + '">' + (v === '' ? '<small>Tu respuesta</small>' : S(v)) + (A.unidad && v !== '' ? '<small>' + S(A.unidad) + '</small>' : '') + '</div><div class="teclan">' +
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '0', '⌫'].map(function (d) { return '<button class="pz' + (d === '⌫' ? ' borrar' : '') + '" data-k="' + d + '"' + (lock ? ' disabled' : '') + '>' + d + '</button>'; }).join('') + '</div>' + botonComprobar(lock, v !== '');
      pintar(h);
      on('[data-k]', 'click', function (b) { var d = b.dataset.k; mal = false; if (d === '⌫') v = v.slice(0, -1); else if (v.length < 14) v += d; dib(); });
      document.getElementById('ok').onclick = function () {
        var aceptadas = [A.sol].concat(A.aceptadas || []).map(norm);
        veredicto(A, aceptadas.indexOf(norm(v)) >= 0, { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { mal = true; dib(); }, reintento: function () { v = ''; mal = false; dib(); }, revelar: function () { lock = true; mal = false; v = String(A.sol); dib(); } });
      };
    }
    dib();
  };

  // detective: encontrar el paso con el error en una resolución. {q, pasos[], error (índice)}
  T.detective = function (A) {
    var sel = -1, mal = [], lock = false, rev = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><p style="text-align:center">🔎 Hay un solo paso con un error. Tocalo.</p><div class="ops">' + A.pasos.map(function (p, i) {
        var c = 'linea-det' + (sel === i ? ' sel' : '') + (mal.indexOf(i) >= 0 ? ' mal' : '') + (rev && i === A.error ? ' bien' : '');
        return '<button class="' + c + '" data-l="' + i + '"' + (lock || mal.indexOf(i) >= 0 ? ' disabled' : '') + '><b>' + (i + 1) + '</b>' + S(p) + '</button>';
      }).join('') + '</div>' + botonComprobar(lock, sel >= 0);
      pintar(h);
      on('[data-l]', 'click', function (b) { sel = +b.dataset.l; dib(); });
      document.getElementById('ok').onclick = function () {
        veredicto(A, sel === A.error, { bloquear: function () { lock = true; rev = true; dib(); }, marcar: function () { mal.push(sel); sel = -1; dib(); }, reintento: function () { }, revelar: function () { lock = true; rev = true; if (sel >= 0) mal.push(sel); sel = -1; dib(); } });
      };
    }
    dib();
  };

  // recta: ubicar un valor en una recta numérica. {q, min, max, paso?, sol, tol?, unidad?}
  T.recta = function (A) {
    var paso = A.paso || 1, tol = A.tol == null ? 0 : A.tol, v = Math.round((A.min + A.max) / 2 / paso) * paso, lock = false, ok = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><div class="vis-num' + (lock ? (ok ? ' bien' : ' mal') : '') + '">' + fmt(v).replace('.', ',') + (A.unidad ? '<small>' + S(A.unidad) + '</small>' : '') + '</div><div class="recta"><input type="range" id="rg" min="' + A.min + '" max="' + A.max + '" step="' + paso + '" value="' + v + '"' + (lock ? ' disabled' : '') + '><div class="eje"><span>' + fmt(A.min) + '</span><span>' + fmt(A.max) + '</span></div></div>' + botonComprobar(lock, true);
      pintar(h);
      document.getElementById('rg').oninput = function (e) { v = +e.target.value; app.querySelector('.vis-num').firstChild.nodeValue = fmt(v).replace('.', ','); };
      document.getElementById('ok').onclick = function () {
        veredicto(A, Math.abs(v - A.sol) <= tol, { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { }, reintento: function () { }, revelar: function () { lock = true; v = A.sol; dib(); } });
      };
    }
    dib();
  };

  // comparar: elegir <, = o > entre dos expresiones. {q?, a, b, ok:'<'|'='|'>'}
  T.comparar = function (A) {
    var sel = null, malas = [], lock = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q || '¿Qué signo va entre los dos?') + '</h2><div class="cmp"><div class="tarjeta">' + S(A.a) + '</div><div class="sig">' + (lock ? A.ok : '?') + '</div><div class="tarjeta">' + S(A.b) + '</div></div><div class="simbolos">' +
        ['<', '=', '>'].map(function (s) { var c = 'op' + (sel === s ? ' sel' : '') + (malas.indexOf(s) >= 0 ? ' mal' : '') + (lock && s === A.ok ? ' bien' : ''); return '<button class="' + c + '" data-s="' + s + '"' + (lock || malas.indexOf(s) >= 0 ? ' disabled' : '') + '>' + (s === '<' ? '&lt;' : s === '>' ? '&gt;' : s) + '</button>'; }).join('') + '</div>' + botonComprobar(lock, sel != null);
      pintar(h);
      on('[data-s]', 'click', function (b) { sel = b.dataset.s; dib(); });
      document.getElementById('ok').onclick = function () {
        veredicto(A, sel === A.ok, { bloquear: function () { lock = true; dib(); }, marcar: function () { malas.push(sel); sel = null; dib(); }, reintento: function () { }, revelar: function () { if (sel) malas.push(sel); lock = true; dib(); } });
      };
    }
    dib();
  };

  // memoria: encontrar las parejas dadas vuelta. {q, pares:[[a,b],...]} (3 o 4 parejas). Un solo intento: se puntúa por errores.
  T.memoria = function (A) {
    var cartas = baraja([].concat.apply([], A.pares.map(function (p, i) { return [{ t: p[0], k: i, id: i * 2 }, { t: p[1], k: i, id: i * 2 + 1 }]; }))), arriba = [], hechas = [], fallos = 0, bloqueo = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><p style="text-align:center">Dadas vuelta, encontrá cada pareja. Errores: <b>' + fallos + '</b></p><div class="memo">' + cartas.map(function (c) {
        return '<button class="carta' + (hechas.indexOf(c.k) >= 0 ? ' ok' : arriba.indexOf(c) >= 0 ? ' arriba' : '') + '" data-m="' + c.id + '">' + S(c.t) + '</button>';
      }).join('') + '</div>';
      pintar(h);
      on('[data-m]', 'click', function (b) {
        if (bloqueo) return; var c = cartas.filter(function (x) { return x.id === +b.dataset.m; })[0]; if (arriba.indexOf(c) >= 0 || hechas.indexOf(c.k) >= 0) return;
        arriba.push(c); dib();
        if (arriba.length === 2) {
          bloqueo = true;
          if (arriba[0].k === arriba[1].k) { hechas.push(arriba[0].k); arriba = []; bloqueo = false; setTimeout(function () { dib(); fin(); }, 250); }
          else { fallos++; setTimeout(function () { arriba = []; bloqueo = false; dib(); }, 800); }
        }
      });
    }
    function fin() {
      if (hechas.length < A.pares.length) return;
      var cr = fallos <= 1 ? 1 : fallos <= 3 ? .5 : 0;
      fb(cr > 0 ? 'bien' : 'mal', (fallos === 0 ? '¡Memoria de elefante!' : '¡Las encontraste todas!') + ' (' + fallos + ' error' + (fallos === 1 ? '' : 'es') + ')<small>' + S(A.exp || '') + '</small>', [['Seguir ➜', function () { anotar(cr); }]]);
    }
    dib();
  };

  // ================= MÓDULOS DE NUMERACIÓN (Matemática: sistema decimal hasta los millones) =================
  var ABR = ['CMill', 'DMill', 'UMill', 'CM', 'DM', 'UM', 'C', 'D', 'U'];
  var VAL = ['100.000.000', '10.000.000', '1.000.000', '100.000', '10.000', '1.000', '100', '10', '1'];
  function esperado(num) { var p = pad(num, 9), n = String(num).length; return p.split('').map(function (c, i) { return i >= 9 - n ? c : ''; }); }
  function tablaHTML(sl, act, err, lock, ok, editable) {
    var h = '<div class="tabla">', nombres = ['Millones', 'Miles', 'Unidades'];
    for (var g = 0; g < 3; g++) {
      h += '<div class="clase"><div class="clase-t">' + nombres[g] + '</div><div class="slots">';
      for (var j = 0; j < 3; j++) {
        var i = g * 3 + j, c = 'slot' + (i === act && !lock && editable ? ' act' : '') + (err.indexOf(i) >= 0 ? ' mal' : '') + (lock && ok ? ' bien' : '');
        h += '<button class="slot ' + c + '" data-s="' + i + '"' + (editable && !lock ? '' : ' disabled') + '><small>' + ABR[i] + '</small>' + (sl[i] === '' ? '&nbsp;' : sl[i]) + '</button>';
      }
      h += '</div></div>';
    }
    return h + '</div>';
  }
  // tabla: escribir un número en la tabla de posiciones. {q, num}
  T.tabla = function (A) {
    var exp = esperado(A.num), sl = ['', '', '', '', '', '', '', '', ''], act = 0, err = [], lock = false, ok = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2>' + tablaHTML(sl, act, err, lock, ok, true) +
        '<div class="teclado">' + '0123456789'.split('').map(function (d) { return '<button class="pz" data-d="' + d + '"' + (lock ? ' disabled' : '') + '>' + d + '</button>'; }).join('') +
        '<button class="pz borrar" data-d="x"' + (lock ? ' disabled' : '') + '>⌫</button><button class="pz borrar" data-d="xx"' + (lock ? ' disabled' : '') + ' title="Borrar todo">🗑</button></div>' +
        botonComprobar(lock, sl.some(function (v) { return v !== ''; }));
      pintar(h);
      on('[data-s]', 'click', function (b) { act = +b.dataset.s; err = []; dib(); });
      on('[data-d]', 'click', function (b) { var d = b.dataset.d; err = []; if (d === 'xx') { sl = ['', '', '', '', '', '', '', '', '']; act = 0; } else if (d === 'x') { sl[act] = ''; } else { sl[act] = d; if (act < 8) act++; } dib(); });
      document.getElementById('ok').onclick = function () {
        var mal = []; sl.forEach(function (v, i) { if (v !== exp[i]) mal.push(i); });
        veredicto(A, !mal.length, { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { err = mal; dib(); }, reintento: function () { err = []; dib(); }, revelar: function () { sl = exp.slice(); lock = true; ok = false; err = []; dib(); } });
      };
    }
    dib();
  };
  // leer: leer un número mostrado en la tabla. {q, num, ops[], ok}
  T.leer = function (A) {
    var exp = esperado(A.num), opts = baraja(A.ops.map(function (t, i) { return { t: t, ok: i === A.ok }; })), sel = -1, malas = [], lock = false, mostrarOk = false;
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2>' + tablaHTML(exp, -1, [], false, false, false) + '<div class="ops">' + opts.map(function (o, i) {
        var c = 'op' + (i === sel ? ' sel' : '') + (malas.indexOf(i) >= 0 ? ' mal' : '') + (mostrarOk && o.ok ? ' bien' : '') + (lock && !o.ok && malas.indexOf(i) < 0 ? ' gris' : '');
        return '<button class="' + c + '" data-o="' + i + '"' + (lock || malas.indexOf(i) >= 0 ? ' disabled' : '') + '>' + S(o.t) + '</button>';
      }).join('') + '</div>' + botonComprobar(lock, sel >= 0);
      pintar(h);
      on('[data-o]', 'click', function (b) { sel = +b.dataset.o; dib(); });
      document.getElementById('ok').onclick = function () {
        veredicto(A, opts[sel].ok, { bloquear: function () { lock = true; mostrarOk = true; dib(); }, marcar: function () { malas.push(sel); sel = -1; dib(); }, reintento: function () { }, revelar: function () { malas.push(sel); lock = true; mostrarOk = true; sel = -1; dib(); } });
      };
    }
    dib();
  };
  // perillas: armar un número girando perillas ▲▼ (hasta 7 lugares). {q, num}
  T.perillas = function (A) {
    var exp = pad(A.num, 7).split('').map(Number), v = [0, 0, 0, 0, 0, 0, 0], err = [], lock = false, ok = false;
    function numero() { var s = v.join('').replace(/^0+/, ''); return s === '' ? '0' : fmt(s); }
    function dib() {
      var h = cab() + '<h2>' + S(A.q) + '</h2><div class="visor"><small>LA MÁQUINA ARMÓ</small>' + numero() + '</div><div class="perillas">';
      for (var i = 0; i < 7; i++) {
        var k = i + 2;
        h += '<div class="perilla"><small>' + ABR[k] + '</small><em>' + VAL[k] + '</em><button class="fl" data-u="' + i + '"' + (lock ? ' disabled' : '') + '>▲</button><div class="dig' + (err.indexOf(i) >= 0 ? ' mal' : '') + (lock && ok ? ' bien' : '') + '">' + v[i] + '</div><button class="fl" data-w="' + i + '"' + (lock ? ' disabled' : '') + '>▼</button></div>';
      }
      h += '</div>' + botonComprobar(lock, true);
      pintar(h);
      on('[data-u]', 'click', function (b) { var i = +b.dataset.u; v[i] = (v[i] + 1) % 10; err = []; dib(); });
      on('[data-w]', 'click', function (b) { var i = +b.dataset.w; v[i] = (v[i] + 9) % 10; err = []; dib(); });
      document.getElementById('ok').onclick = function () {
        var mal = []; v.forEach(function (x, i) { if (x !== exp[i]) mal.push(i); });
        veredicto(A, !mal.length, { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { err = mal; dib(); }, reintento: function () { err = []; dib(); }, revelar: function () { v = exp.slice(); lock = true; ok = false; err = []; dib(); } });
      };
    }
    dib();
  };
  // tachar: tachar cifras de la derecha para contar decenas, centenas, etc. {q, num, k (cuántas cifras se tachan), unidad}
  T.tachar = function (A) {
    var n = A.num.length, cut = n, lock = false, ok = false;
    function dib() {
      var rest = A.num.slice(0, cut);
      var h = cab() + '<div class="pedido">' + S(A.q) + '</div><div class="cifras">' + A.num.split('').map(function (c, i) {
        return '<button class="cifra' + (i >= cut ? ' tach' : '') + (lock && ok && i < cut ? ' bien' : '') + '" data-c="' + i + '"' + (lock ? ' disabled' : '') + '>' + c + '</button>';
      }).join('') + '</div><div class="visor"><small>CANTIDAD DE ' + S(String(A.unidad || '').toUpperCase()) + '</small>' + (cut > 0 && cut < n ? fmt(rest) : '—') + '</div><p style="text-align:center">Tocá la cifra desde donde querés tachar. Tocala de nuevo para deshacer.</p>' + botonComprobar(lock, cut !== n);
      pintar(h);
      on('[data-c]', 'click', function (b) { var i = +b.dataset.c; cut = (cut === i) ? n : i; dib(); });
      document.getElementById('ok').onclick = function () {
        veredicto(A, cut === n - A.k, { bloquear: function () { lock = true; ok = true; dib(); }, marcar: function () { dib(); }, reintento: function () { cut = n; dib(); }, revelar: function () { cut = n - A.k; lock = true; ok = false; dib(); } });
      };
    }
    dib();
  };

  // ================= flujo del juego =================
  function estrellas(p) { var n = p >= .9 ? 3 : p >= .6 ? 2 : p > 0 ? 1 : 0; return '★★★'.slice(0, n) + '<s>' + '★★★'.slice(n) + '</s>'; }
  function mapa() {
    var h = '<div class="mapa mini">';
    DES.forEach(function (d, i) {
      var hecho = !!(E.cred && E.cred[i] && E.cred[i].length >= nPasos(i)), act = !hecho && i === E.d;
      h += '<div class="nodo' + (hecho ? ' hecho' : act ? ' act' : '') + '"><i>' + (hecho ? '✓' : S(d.ico || '⭐')) + '</i><div>' + S(d.nom) + '<small>' + S(d.sub || '') + '</small></div>' + (hecho ? '<em class="estrellas" style="font-size:1rem">' + estrellas(suma(E.cred[i]) / nPasos(i)) + '</em>' : '') + '</div>';
    });
    return h + '</div>';
  }
  function jugar() { var A = DES[E.d].pasos[E.a]; E.int = 1; if (!T[A.t]) { anotar(1); return; } T[A.t](A); }
  function introDesafio() {
    var d = DES[E.d];
    pintar('<div class="etq">Desafío ' + (E.d + 1) + ' de ' + ND + '</div><h1>' + S(d.ico || '⭐') + ' ' + S(d.nom) + '</h1><div class="tip"><b>Cómo funciona.</b> ' + S(d.como || '') + '</div><p style="max-width:520px">Tenés 2 intentos por actividad: si acertás a la primera vale 1 punto; a la segunda, medio punto.</p><button class="btn" style="min-width:220px">Empezar ➜</button>', 'centro');
    app.querySelector('.escena .btn').onclick = function () { E.a = 0; jugar(); };
  }
  function finDesafio() {
    var c = suma(E.cred[E.d]) / nPasos(E.d), ult = E.d >= ND - 1, msgs = ['¡Desafío superado!', 'Muy buen trabajo.', 'Lo importante es que lo intentaste.'];
    var h = '<div class="etq">Desafío ' + (E.d + 1) + ' completo</div><div class="gran">' + Math.round(c * 100) + '%</div><div class="estrellas">' + estrellas(c) + '</div><h2>' + (c >= .9 ? msgs[0] : c >= .5 ? msgs[1] : msgs[2]) + '</h2>' + mapa() + '<button class="btn">' + (ult ? 'Ver resultado final' : 'Siguiente desafío ➜') + '</button>';
    pintar(h, 'centro');
    app.querySelector('.escena .btn').onclick = function () { if (ult) final(); else { E.d++; introDesafio(); } };
  }
  function final() {
    var total = 0, cant = 0; E.cred.forEach(function (c) { total += suma(c); cant += c.length; });
    var pct = Math.round(total / cant * 100), cie = SPEC.cierre || {};
    var msg = pct >= 90 ? (cie.alto || '¡Excelente trabajo!') : pct >= 60 ? (cie.medio || '¡Muy bien! Repasá lo que falló en el PDF.') : (cie.bajo || 'Buen intento. Volvé al PDF y jugá otra vez.');
    var h = '<div class="etq">' + S(SPEC.titulo) + ' · resultado</div><div class="gran">' + pct + '%</div><div class="estrellas">' + estrellas(pct / 100) + '</div><h2>' + S(msg) + '</h2><p>⭐ ' + E.pts + ' puntos</p>' + mapa() + '<button class="btn sec">Jugar de nuevo</button>';
    pintar(h, 'centro'); app.querySelector('.escena .btn').onclick = inicio;
    if (pct >= 60) { var c = document.createElement('div'); c.className = 'conf'; var col = ['#7FD3C4', '#F4B63F', '#ff7a66', '#fff', '#19a39f']; for (var i = 0; i < 70; i++) { var p = document.createElement('i'); p.style.left = Math.random() * 100 + '%'; p.style.background = col[i % 5]; p.style.animationDuration = (2 + Math.random() * 2.5) + 's'; p.style.animationDelay = Math.random() * 1.2 + 's'; c.appendChild(p); } app.appendChild(c); }
    try { window.parent.postMessage({ tipo: 'wave-resultado', puntaje: pct }, '*'); } catch (e) { }
  }
  function inicio() {
    E = { d: 0, a: 0, int: 1, pts: 0, cred: DES.map(function () { return []; }) };
    pintar('<div class="etq">' + S(SPEC.etiqueta || '') + '</div><h1>' + S(SPEC.titulo) + '</h1><p style="max-width:520px">' + S(SPEC.historia || '') + '</p>' + mapa() + '<button class="btn" style="min-width:220px">' + S(SPEC.boton || 'Empezar ➜') + '</button>', 'centro');
    app.querySelector('.escena .btn').onclick = introDesafio;
  }
  window.WaveMotor = { tipos: Object.keys(T), T: T, inicio: inicio };
  inicio();
})();
