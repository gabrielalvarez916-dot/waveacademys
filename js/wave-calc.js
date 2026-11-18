// Cálculo compartido entre la app del alumno y el servidor (se copia igual a las funciones que corrigen).
// Sirve para: números al azar con semilla, evaluar fórmulas y reglas, leer números escritos en formato argentino
// y evaluar lo que el alumno arma con fichas. No usa eval: tiene su propio intérprete de expresiones.
(function (root) {
  'use strict';

  // ---------- Azar con semilla (misma semilla = mismos números, en el navegador y en el servidor) ----------
  function hash(s) {
    var h = 1779033703 ^ s.length;
    for (var i = 0; i < s.length; i++) { h = Math.imul(h ^ s.charCodeAt(i), 3432918353); h = (h << 13) | (h >>> 19); }
    h = Math.imul(h ^ (h >>> 16), 2246822507); h = Math.imul(h ^ (h >>> 13), 3266489909);
    return (h ^ (h >>> 16)) >>> 0;
  }
  function rng(seed) {
    var a = hash(String(seed));
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // ---------- Intérprete de expresiones ----------
  var CACHE = {};
  function tokenizar(s) {
    var out = [], i = 0, m;
    s = String(s);
    while (i < s.length) {
      var c = s[i];
      if (/\s/.test(c)) { i++; continue; }
      if ((m = /^(\d+(\.\d+)?|\.\d+)/.exec(s.slice(i)))) { out.push({ t: 'n', v: parseFloat(m[1]) }); i += m[1].length; continue; }
      if ((m = /^[A-Za-z_][A-Za-z_0-9]*/.exec(s.slice(i)))) { out.push({ t: 'i', v: m[0] }); i += m[0].length; continue; }
      var dos = s.substr(i, 2);
      if (['==', '!=', '<=', '>=', '&&', '||'].indexOf(dos) >= 0) { out.push({ t: 'o', v: dos }); i += 2; continue; }
      if ('+-*/%^()<>!,'.indexOf(c) >= 0) { out.push({ t: 'o', v: c }); i++; continue; }
      throw new Error('Carácter no válido en la expresión: ' + c);
    }
    return out;
  }
  function parsear(src) {
    if (CACHE[src]) return CACHE[src];
    var tk = tokenizar(src), p = 0;
    function ver() { return tk[p]; }
    function es(v) { return tk[p] && tk[p].t === 'o' && tk[p].v === v; }
    function comer(v) { if (!es(v)) throw new Error('Se esperaba ' + v); p++; }
    function o() { var a = y(); while (es('||')) { p++; a = { k: 'b', o: '||', a: a, b: y() }; } return a; }
    function y() { var a = cmp(); while (es('&&')) { p++; a = { k: 'b', o: '&&', a: a, b: cmp() }; } return a; }
    function cmp() {
      var a = suma(), v = ver();
      if (v && v.t === 'o' && ['==', '!=', '<=', '>=', '<', '>'].indexOf(v.v) >= 0) { p++; a = { k: 'b', o: v.v, a: a, b: suma() }; }
      return a;
    }
    function suma() { var a = prod(); while (es('+') || es('-')) { var op = tk[p++].v; a = { k: 'b', o: op, a: a, b: prod() }; } return a; }
    function prod() { var a = pot(); while (es('*') || es('/') || es('%')) { var op = tk[p++].v; a = { k: 'b', o: op, a: a, b: pot() }; } return a; }
    function pot() { var a = un(); if (es('^')) { p++; a = { k: 'b', o: '^', a: a, b: pot() }; } return a; }
    function un() {
      if (es('-')) { p++; return { k: 'u', o: '-', a: un() }; }
      if (es('!')) { p++; return { k: 'u', o: '!', a: un() }; }
      return prim();
    }
    function prim() {
      var v = ver();
      if (!v) throw new Error('Expresión incompleta');
      if (v.t === 'n') { p++; return { k: 'n', v: v.v }; }
      if (v.t === 'i') {
        p++;
        if (es('(')) {
          p++; var args = [];
          if (!es(')')) { args.push(o()); while (es(',')) { p++; args.push(o()); } }
          comer(')');
          return { k: 'f', n: v.v, a: args };
        }
        return { k: 'v', n: v.v };
      }
      if (es('(')) { p++; var e = o(); comer(')'); return e; }
      throw new Error('Expresión no válida');
    }
    var ast = o();
    if (p < tk.length) throw new Error('Sobra algo al final de la expresión');
    CACHE[src] = ast;
    return ast;
  }
  var FUN = {
    abs: Math.abs, min: Math.min, max: Math.max, floor: Math.floor, ceil: Math.ceil, round: Math.round, sqrt: Math.sqrt,
    mcd: function (a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = b; b = a % b; a = t; } return a; },
    digitos: function (n) { return String(Math.abs(Math.trunc(n))).length; }
  };
  function ev(n, vars) {
    switch (n.k) {
      case 'n': return n.v;
      case 'v': if (!(n.n in vars)) throw new Error('Falta la variable ' + n.n); return vars[n.n];
      case 'u': var x = ev(n.a, vars); return n.o === '-' ? -x : (x ? 0 : 1);
      case 'f': if (!FUN[n.n]) throw new Error('Función desconocida ' + n.n); return FUN[n.n].apply(null, n.a.map(function (a) { return ev(a, vars); }));
      case 'b':
        var a = ev(n.a, vars), b = ev(n.b, vars);
        switch (n.o) {
          case '+': return a + b; case '-': return a - b; case '*': return a * b;
          case '/': return b === 0 ? NaN : a / b;
          case '%': return b === 0 ? NaN : a % b;
          case '^': return (Math.abs(b) > 64) ? NaN : Math.pow(a, b);
          case '==': return Math.abs(a - b) < 1e-9 ? 1 : 0;
          case '!=': return Math.abs(a - b) < 1e-9 ? 0 : 1;
          case '<': return a < b ? 1 : 0; case '>': return a > b ? 1 : 0;
          case '<=': return a <= b + 1e-9 ? 1 : 0; case '>=': return a >= b - 1e-9 ? 1 : 0;
          case '&&': return a && b ? 1 : 0; case '||': return a || b ? 1 : 0;
        }
    }
    throw new Error('Expresión no válida');
  }
  function evaluar(src, vars) {
    var r = ev(parsear(src), vars || {});
    return typeof r === 'number' && isFinite(r) ? r : NaN;
  }

  // ---------- Números al azar con resultados válidos ----------
  // opciones: { vars: {a: {min, max, paso?} | {valores: [...]}}, calculadas: {c: "a*b"}, reglas: ["a % b == 0", "a > b"] }
  // Se repite el sorteo hasta que se cumplan todas las reglas; si no hay manera, devuelve null.
  function instanciar(op, seed) {
    op = op || {};
    var def = op.vars || {}, nombres = Object.keys(def), r = rng(seed);
    for (var t = 0; t < 800; t++) {
      var vars = {}, ok = true;
      nombres.forEach(function (n) {
        var d = def[n];
        if (Array.isArray(d.valores)) vars[n] = d.valores[Math.floor(r() * d.valores.length)];
        else { var paso = d.paso || 1, k = Math.floor((d.max - d.min) / paso) + 1; vars[n] = d.min + paso * Math.floor(r() * k); }
      });
      try {
        var calc = op.calculadas || {};
        Object.keys(calc).forEach(function (n) { var v = evaluar(calc[n], vars); if (isNaN(v)) throw new Error('x'); vars[n] = v; });
        (op.reglas || []).forEach(function (rg) { var v = evaluar(rg, vars); if (isNaN(v) || !v) ok = false; });
      } catch (e) { ok = false; }
      if (ok) return vars;
    }
    return null;
  }

  // ---------- Formato argentino ----------
  function fmtNum(n) {
    if (typeof n !== 'number' || !isFinite(n)) return String(n);
    var neg = n < 0, s = Math.abs(n).toString(), p = s.split('.');
    var ent = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, p[0].length >= 4 ? '.' : '');
    return (neg ? '-' : '') + ent + (p[1] ? ',' + p[1] : '');
  }
  function plantilla(texto, vars) {
    if (!vars) return String(texto);
    return String(texto).replace(/\{([A-Za-z_][A-Za-z_0-9]*)\}/g, function (m, n) { return n in vars ? fmtNum(vars[n]) : m; });
  }
  // Lee un número escrito como lo escribe un alumno argentino: 1.000 · 1000 · 1.000,5 · 3,5 · 3/4 · 6 000
  function parseNum(s) {
    s = String(s == null ? '' : s).trim().toLowerCase().replace(/\s+/g, '').replace(/−/g, '-');
    if (!s) return NaN;
    var m = /^(-?\d+(?:[.,]\d+)*)\/(\d+(?:[.,]\d+)*)$/.exec(s);
    if (m) { var a = parseNum(m[1]), b = parseNum(m[2]); return b ? a / b : NaN; }
    m = /^(-?\d[\d.,]*)/.exec(s);
    if (!m) return NaN;
    var x = m[1];
    if (/,/.test(x)) x = x.replace(/\./g, '').replace(',', '.');
    else if (/^-?\d{1,3}(\.\d{3})+$/.test(x)) x = x.replace(/\./g, '');
    var v = parseFloat(x);
    return isFinite(v) ? v : NaN;
  }
  // Lo que queda escrito después del número (la unidad): "45 min" -> "min"
  function unidadDe(s) {
    var m = /^\s*-?\d[\d.,\s\/]*(.*)$/.exec(String(s || '').toLowerCase());
    return m ? m[1].replace(/\s+/g, '').replace(/\./g, '') : '';
  }

  // ---------- Fichas: ["8", "÷", "(", "3", "−", "8", "÷", "3", ")"] ----------
  function evaluarFichas(fichas) {
    var partes = (fichas || []).map(function (f) {
      f = String(f).trim();
      if (f === '×' || f === 'x' || f === '·') return '*';
      if (f === '÷' || f === ':') return '/';
      if (f === '−' || f === '–') return '-';
      if (/^[+\-*\/()^%]$/.test(f)) return f;
      var n = parseNum(f);
      if (isNaN(n)) throw new Error('Ficha no válida');
      return '(' + n + ')';
    });
    return evaluar(partes.join(' '), {});
  }

  root.WaveCalc = { rng: rng, parsear: parsear, evaluar: evaluar, instanciar: instanciar, plantilla: plantilla, parseNum: parseNum, unidadDe: unidadDe, fmtNum: fmtNum, evaluarFichas: evaluarFichas };
})(typeof window !== 'undefined' ? window : globalThis);
