/* BANCO DE LA LECCIÓN · NATURALES (parte 3): física (circuitos, movimiento, fuerzas, vectores, palancas, energía, ondas, luz, calor, fluidos, imanes)
   y Tierra y espacio (día y noche, estaciones, fases de la Luna, sistema solar). Usa H.nat de js/leccion-banco-nat.js. Todos PASO A PASO. */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h || !B._h.nat) return;
  var H = B._h, M = B.motores, R = H.R, pick = H.pick, mezclar = H.mezclar, fmt = H.fmt, N = H.nat;
  var escena = H.escena, ctrl = H.ctrl, respuesta = H.respuesta;
  var C = N.C, S = N.S, tx = N.tx, txw = N.txw, ln = N.ln, fl = N.fl, ci = N.ci, rc = N.rc, em = N.em, r1 = N.r1, sel = N.sel, otro = N.otro, rot = N.rot, nota = N.nota, elegir = N.elegir, ordenar = N.ordenar;
  var G = 10; // gravedad aproximada (m/s²) para cuentas escolares
  function r2(x) { return Math.round(x * 100) / 100; }
  function f2(x) { return fmt(r2(x)); }
  function formula(t, s2) { return S(470, s2 ? 78 : 54, tx(235, 34, t, { a: 'middle', s: 18, w: 900 }) + (s2 ? tx(235, 64, s2, { a: 'middle', s: 13, w: 800, c: C.teal }) : '')); }

  // 1) CIRCUITO: ley de Ohm, serie y paralelo, lámparas que brillan
  function lampara(x, y, P, on) { var gl = on ? Math.min(26, 6 + P * 2) : 0; return (gl ? ci(x, y, 12 + gl, 'rgba(245,211,59,.35)') : '') + ci(x, y, 13, on ? '#F5D33B' : '#eee', C.osc) + '<path d="M' + (x - 6) + ',' + (y + 4) + ' q6,-12 12,0" fill="none" stroke="' + C.osc + '" stroke-width="1.5"/>'; }
  function circuito(modo, V, R1, R2, fase, quitar) { var s = '', paralelo = modo === 'paralelo', Req = paralelo ? R1 * R2 / (R1 + R2) : R1 + R2, I = V / Req, I1 = paralelo ? V / R1 : I, I2 = paralelo ? V / R2 : I, V1 = paralelo ? V : I * R1, V2 = paralelo ? V : I * R2, on1 = !(quitar && !paralelo) , on2 = !quitar;
    s += rc(40, 90, 36, 60, '#fff', C.osc, 4) + ln(46, 100, 70, 100, C.osc, 4) + ln(52, 110, 64, 110, C.osc, 2) + tx(58, 170, f2(V) + ' V', { a: 'middle', s: 12, w: 900 }) + tx(58, 86, '+', { a: 'middle', s: 12, w: 900, c: C.coral });
    var cab = function (pts, act) { return '<polyline points="' + pts + '" fill="none" stroke="' + (act ? C.osc : '#ccc') + '" stroke-width="3"/>'; };
    if (!paralelo) { s += cab('58,90 58,40 420,40 420,200 58,200 58,150', !quitar) + lampara(180, 40, V1 * I1, on1 && !quitar) + (quitar ? rc(290, 30, 40, 20, '#fff') + tx(310, 30, 'quitada', { a: 'middle', s: 10, c: C.rosa }) : lampara(310, 40, V2 * I2, on2)); }
    else { s += cab('58,90 58,40 420,40 420,200 58,200 58,150', true) + cab('240,40 240,90', true) + cab('240,150 240,200', true) + cab('330,40 330,90', !quitar) + cab('330,150 330,200', !quitar) + ln(240, 90, 240, 150, C.osc, 3) + ln(330, 90, 330, 150, quitar ? '#ccc' : C.osc, 3) + lampara(240, 120, V1 * I1, true) + (quitar ? tx(330, 124, 'quitada', { a: 'middle', s: 10, c: C.rosa }) : lampara(330, 120, V2 * I2, true)); }
    if (fase >= 1) s += tx(paralelo ? 240 : 180, paralelo ? 162 : 75, 'R₁ = ' + R1 + ' Ω', { a: 'middle', s: 11, w: 800 }) + (quitar ? '' : tx(paralelo ? 330 : 310, paralelo ? 162 : 75, 'R₂ = ' + R2 + ' Ω', { a: 'middle', s: 11, w: 800 }));
    if (fase >= 2 && !quitar) s += fl(380, 200, 300, 200, C.coral, 3) + tx(340, 220, 'I = ' + f2(I) + ' A', { a: 'middle', s: 12, w: 900, c: C.coral });
    return { svg: S(470, 230, s), Req: Req, I: I, I1: I1, I2: I2, V1: V1, V2: V2 }; }
  M.circuito = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Conexión', [['serie', 'En serie'], ['paralelo', 'En paralelo']], p.modo || 'serie') + ctrl('v', 'Pila o fuente (V)', 1.5, 12, 1.5, 6) + ctrl('a', 'R₁ (Ω)', 1, 20, 1, 4) + ctrl('b', 'R₂ (Ω)', 1, 20, 1, 2), function (o) { var m = o.m || 'serie', V = o.v || 6, R1 = o.a || 4, R2 = o.b || 2, c = circuito(m, V, R1, R2, 1), P = [];
      P.push({ vis: circuito(m, V, R1, R2, 0).svg, txt: 'Un <b>circuito cerrado</b>: la pila empuja a los electrones por los cables y las lámparas se encienden. Están conectadas <b>' + (m === 'serie' ? 'en serie' : 'en paralelo') + '</b>.' });
      P.push({ vis: c.svg + formula(m === 'serie' ? 'R = R₁ + R₂ = ' + R1 + ' + ' + R2 + ' = ' + f2(c.Req) + ' Ω' : 'R = R₁·R₂ / (R₁ + R₂) = ' + f2(c.Req) + ' Ω'), txt: m === 'serie' ? 'En serie, las resistencias <b>se suman</b>.' : 'En paralelo, la resistencia total es <b>menor</b> que cada una.' });
      P.push({ vis: circuito(m, V, R1, R2, 2).svg + formula('I = V / R = ' + f2(V) + ' / ' + f2(c.Req) + ' = ' + f2(c.I) + ' A'), txt: '<b>Ley de Ohm</b>: la corriente es la tensión dividida por la resistencia.' });
      P.push({ vis: circuito(m, V, R1, R2, 2).svg + formula(m === 'serie' ? 'V₁ = ' + f2(c.V1) + ' V · V₂ = ' + f2(c.V2) + ' V' : 'I₁ = ' + f2(c.I1) + ' A · I₂ = ' + f2(c.I2) + ' A'), txt: m === 'serie' ? 'En serie pasa la <b>misma corriente</b> por las dos y la tensión se reparte.' : 'En paralelo cada lámpara recibe <b>toda la tensión</b> y la corriente se reparte.' });
      P.push({ vis: circuito(m, V, R1, R2, 1, true).svg, txt: m === 'serie' ? 'Si se quita una lámpara en serie, el circuito se abre y <b>se apagan todas</b>.' : 'En paralelo, si se quita una, <b>la otra sigue encendida</b>: así están conectados los enchufes de una casa.' });
      return P; });
  } };
  M.circuito_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var k = rot(3, u), V = pick([3, 6, 9, 12]), R1 = pick([1, 2, 3, 4, 6]), R2 = pick([2, 3, 6]);
      if (k === 0) return { cons: 'Una lámpara de <b>' + R1 + ' Ω</b> se conecta a una pila de <b>' + V + ' V</b>. ¿Qué corriente circula?', campos: [{ lab: 'I', v: r2(V / R1), un: 'A', tol: 0.01 }], ayuda: 'Ley de Ohm: I = V / R.', bien: '¡Bien! I = ' + V + ' / ' + R1 + ' = ' + f2(V / R1) + ' A.' };
      if (k === 1) return { cons: 'Dos resistencias de <b>' + R1 + ' Ω</b> y <b>' + R2 + ' Ω</b> en <b>serie</b>, con una pila de ' + V + ' V. ¿Cuál es la corriente?', html: circuito('serie', V, R1, R2, 1).svg, campos: [{ lab: 'I', v: r2(V / (R1 + R2)), un: 'A', tol: 0.01 }], ayuda: 'Primero sumá las resistencias; después, I = V / R.', bien: '¡Bien! R = ' + (R1 + R2) + ' Ω, I = ' + f2(V / (R1 + R2)) + ' A.' };
      var Rp = r2(R1 * R2 / (R1 + R2)); return { cons: 'Dos resistencias de <b>' + R1 + ' Ω</b> y <b>' + R2 + ' Ω</b> en <b>paralelo</b>. ¿Cuál es la resistencia total?', html: circuito('paralelo', V, R1, R2, 1).svg, campos: [{ lab: 'R', v: Rp, un: 'Ω', tol: 0.01 }], ayuda: 'R = R₁·R₂ / (R₁ + R₂).', bien: '¡Bien! R = ' + f2(Rp) + ' Ω.' }; });
  } };

  // 2) MOVIMIENTO: MRU, MRUV, caída libre y tiro vertical, con el móvil y los gráficos
  function mov(modo, v0, a) { if (modo === 'mru') a = 0; if (modo === 'caida') { v0 = 0; a = G; } if (modo === 'tiro') a = -G; return function (t) { return { x: v0 * t + a * t * t / 2, v: v0 + a * t }; }; }
  function pista(f, modo, hasta, T) { var xs = []; for (var t = 0; t <= T; t++) xs.push(f(t).x); var mn = Math.min(0, Math.min.apply(null, xs)), mx = Math.max.apply(null, xs) || 1, s = '';
    if (modo === 'caida' || modo === 'tiro') { var Y = function (x) { return 200 - (x - mn) / (mx - mn || 1) * 170; }; s += ln(60, 205, 60, 25, C.gris, 2); for (t = 0; t <= Math.min(hasta, T); t++) s += ci(60, Y(xs[t]), 9, t === Math.min(hasta, T) ? C.coral : '#fff', C.coral) + tx(78, Y(xs[t]) + 4, 't=' + t + ' s · ' + f2(xs[t]) + ' m', { s: 10.5 }); return s; }
    var X = function (x) { return 30 + (x - mn) / (mx - mn || 1) * 400; }; s += ln(20, 110, 450, 110, C.osc, 2);
    for (t = 0; t <= Math.min(hasta, T); t++) s += em(X(xs[t]), 94, '🚗', t === Math.min(hasta, T) ? 24 : 14) + ln(X(xs[t]), 106, X(xs[t]), 116, C.osc, 2) + tx(X(xs[t]), 132 + (t % 2) * 14, t + ' s', { a: 'middle', s: 10 });
    return s; }
  function graficoM(f, T, que) { var vals = []; for (var t = 0; t <= T; t++) vals.push(que === 'x' ? f(t).x : f(t).v); var mn = Math.min(0, Math.min.apply(null, vals)), mx = Math.max(0, Math.max.apply(null, vals)); if (mx === mn) mx = mn + 1;
    var x0 = 50, y0 = 185, W = 380, Hh = 150, Y = function (v) { return y0 - (v - mn) / (mx - mn) * Hh; }, s = ln(x0, Y(0), x0 + W, Y(0)) + ln(x0, y0 + 2, x0, y0 - Hh - 6) + tx(x0 + W, Y(0) + 16, 't (s)', { a: 'end', s: 11 }) + tx(x0 + 4, y0 - Hh - 10, que === 'x' ? 'posición (m)' : 'velocidad (m/s)', { s: 11 });
    s += '<polyline points="' + vals.map(function (v, t) { return r1(x0 + t / T * W) + ',' + r1(Y(v)); }).join(' ') + '" fill="none" stroke="' + (que === 'x' ? C.teal : C.coral) + '" stroke-width="3"/>';
    vals.forEach(function (v, t) { s += ci(x0 + t / T * W, Y(v), 3, C.osc) + tx(x0 + t / T * W, Y(0) + 14, t, { a: 'middle', s: 9.5 }); }); s += tx(x0 - 6, Y(mx) + 4, f2(mx), { a: 'end', s: 9.5 }) + (mn < 0 ? tx(x0 - 6, Y(mn) + 4, f2(mn), { a: 'end', s: 9.5 }) : '');
    return S(470, 218, s); }
  M.movimiento = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Movimiento', [['mru', 'MRU (velocidad constante)'], ['mruv', 'MRUV (acelera)'], ['caida', 'Caída libre'], ['tiro', 'Tiro vertical hacia arriba']], p.modo || 'mru') + ctrl('v', 'Velocidad inicial (m/s)', 0, 30, 1, 10) + ctrl('a', 'Aceleración (m/s²) en MRUV', -5, 5, 1, 2), function (o) { var m = o.m || 'mru', v0 = m === 'caida' ? 0 : o.v == null ? 10 : o.v, a = m === 'mru' ? 0 : m === 'caida' ? G : m === 'tiro' ? -G : o.a || 0, f = mov(m, v0, a), T = m === 'tiro' ? Math.max(2, Math.ceil(2 * v0 / G)) : 5, P = [];
      var desc = { mru: 'recorre distancias iguales en tiempos iguales', mruv: 'su velocidad cambia lo mismo cada segundo', caida: 'cae por la gravedad: acelera ' + G + ' m/s² (aproximado)', tiro: 'sube frenando ' + G + ' m/s cada segundo, se detiene y vuelve a caer' }[m];
      P.push({ vis: S(470, 70, tx(235, 30, 'v₀ = ' + f2(v0) + ' m/s · a = ' + f2(a) + ' m/s²', { a: 'middle', s: 17, w: 900 }) + tx(235, 56, 'el móvil ' + desc, { a: 'middle', s: 12, c: C.teal, w: 800 })), txt: 'Los datos del movimiento: velocidad inicial y aceleración.' });
      P.push({ vis: S(470, 215, pista(f, m, T, T)), txt: 'Posiciones segundo a segundo: ' + [0, 1, 2, 3].map(function (t) { return f2(f(t).x) + ' m'; }).join(', ') + '…' + (m === 'mru' ? ' Siempre la misma distancia por segundo.' : ' Las distancias cambian: hay aceleración.') });
      P.push({ vis: graficoM(f, T, 'x'), txt: 'Gráfico <b>posición-tiempo</b>: ' + (m === 'mru' ? 'una recta (la pendiente es la velocidad).' : 'una curva (parábola), porque la velocidad cambia.') });
      P.push({ vis: graficoM(f, T, 'v'), txt: 'Gráfico <b>velocidad-tiempo</b>: ' + (a === 0 ? 'una línea horizontal, la velocidad no cambia.' : 'una recta inclinada; su pendiente es la aceleración (' + f2(a) + ' m/s²).') });
      var t1 = m === 'tiro' ? r2(v0 / G) : 3; P.push({ vis: formula(a ? 'x = v₀·t + ½·a·t²' : 'x = v · t', a ? 'v = v₀ + a·t' : ''), txt: m === 'tiro' ? 'Llega a la altura máxima cuando v = 0: en t = ' + f2(t1) + ' s, a ' + f2(f(t1).x) + ' m.' : 'A los 3 s: x = ' + f2(f(3).x) + ' m y v = ' + f2(f(3).v) + ' m/s.' });
      return P; });
  } };
  M.movimiento_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var k = rot(4, u);
      if (k === 0) { var v = pick([5, 10, 15, 20]), t = pick([2, 3, 4, 6]); return { cons: 'Un ciclista va a velocidad constante de <b>' + v + ' m/s</b>. ¿Qué distancia recorre en <b>' + t + ' s</b>?', campos: [{ lab: 'Distancia', v: v * t, un: 'm' }], ayuda: 'MRU: distancia = velocidad × tiempo.', bien: '¡Bien! ' + v + ' × ' + t + ' = ' + v * t + ' m.' }; }
      if (k === 1) { var v0 = pick([0, 5, 10]), a = pick([2, 3, 4]), t2 = pick([2, 3, 5]); return { cons: 'Un auto parte con <b>' + v0 + ' m/s</b> y acelera <b>' + a + ' m/s²</b>. ¿Qué velocidad tiene a los <b>' + t2 + ' s</b>?', campos: [{ lab: 'v', v: v0 + a * t2, un: 'm/s' }], ayuda: 'MRUV: v = v₀ + a·t.', bien: '¡Bien! v = ' + v0 + ' + ' + a + '·' + t2 + ' = ' + (v0 + a * t2) + ' m/s.' }; }
      if (k === 2) { var t3 = pick([1, 2, 3, 4]); return { cons: 'Se suelta una piedra desde lo alto. Tomando g = 10 m/s², ¿cuántos metros cayó a los <b>' + t3 + ' s</b>?', campos: [{ lab: 'Caída', v: 5 * t3 * t3, un: 'm' }], ayuda: 'Caída libre: d = ½·g·t² = 5·t².', bien: '¡Bien! 5 · ' + t3 + '² = ' + 5 * t3 * t3 + ' m.' }; }
      var v1 = pick([10, 20, 30]); return { cons: 'Se lanza una pelota hacia arriba a <b>' + v1 + ' m/s</b> (g = 10 m/s²). ¿Cuánto tarda en llegar a la altura máxima?', campos: [{ lab: 't', v: v1 / 10, un: 's' }], ayuda: 'En la altura máxima v = 0: t = v₀ / g.', bien: '¡Bien! t = ' + v1 + ' / 10 = ' + v1 / 10 + ' s.' }; });
  } };

  // 3) FUERZAS: diagrama de cuerpo libre, fuerza neta y segunda ley de Newton (piso o plano inclinado)
  function dcl(modo, m, F, mu, ang, hasta) { var s = '', Pw = m * G, rad = ang * Math.PI / 180, Nn = modo === 'plano' ? Pw * Math.cos(rad) : Pw, Px = modo === 'plano' ? Pw * Math.sin(rad) : 0, Fr = mu * Nn, net = modo === 'plano' ? Px - Fr : F - Fr; if (net < 0 && (modo === 'plano' ? Px <= Fr : F <= Fr)) net = 0;
    var cx = 235, cy = 120, k = 1.4 / Math.max(1, Pw / 60);
    if (modo === 'plano') { var x1 = 60, y1 = 210, x2 = 410, y2 = 210 - Math.tan(rad) * 350; s += '<polygon points="' + x1 + ',' + y1 + ' ' + x2 + ',' + y1 + ' ' + x2 + ',' + r1(y2) + '" fill="#ECEFF1" stroke="' + C.osc + '" stroke-width="2"/>'; cx = 260; cy = 210 - Math.tan(rad) * 200 - 22; s += '<g transform="rotate(' + (-ang) + ' ' + cx + ' ' + cy + ')">' + rc(cx - 24, cy - 20, 48, 40, '#FFE0B2', C.osc, 4) + '</g>'; }
    else s += ln(30, 160, 440, 160, C.osc, 3) + rc(cx - 30, 100, 60, 60, '#FFE0B2', C.osc, 4) + tx(cx, 135, m + ' kg', { a: 'middle', s: 12, w: 900 });
    var F_ = function (dx, dy, L, col, lab, i) { if (i > hasta) return ''; var o0 = modo === 'plano' ? 0 : 30, x1 = cx + dx * o0, y1 = cy + dy * o0, Lc = Math.min(Math.max(L, 30), 62), x2 = x1 + dx * Lc, y2 = y1 + dy * Lc; return fl(x1, y1, x2, y2, col, 3.5) + tx(x2 + dx * 12, y2 + dy * 12 + 4, lab, { a: 'middle', s: 11.5, w: 900, c: col }); };
    s += F_(0, 1, Pw * k * 0.8, C.rosa, 'P = ' + f2(Pw) + ' N', 1);
    if (modo === 'plano') { s += F_(-Math.sin(rad), -Math.cos(rad), Nn * k * 0.8, C.azul, 'N = ' + f2(Nn) + ' N', 2) + (mu ? F_(Math.cos(rad), -Math.sin(rad), Fr * k * 0.8 + 6, C.sol, 'Fr = ' + f2(Fr) + ' N', 3) : ''); }
    else { s += F_(0, -1, Nn * k * 0.8, C.azul, 'N = ' + f2(Nn) + ' N', 2) + (F ? F_(1, 0, F * k * 0.8 + 6, C.verde, 'F = ' + f2(F) + ' N', 2) : '') + (mu ? F_(-1, 0, Fr * k * 0.8 + 6, C.sol, 'Fr = ' + f2(Fr) + ' N', 3) : ''); }
    return { svg: S(470, 250, s), P: Pw, N: Nn, Fr: Fr, Px: Px, net: net, a: net / m }; }
  M.fuerzas = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('mo', 'Situación', [['piso', 'Empujar una caja en el piso'], ['plano', 'Caja en un plano inclinado']], p.modo || 'piso') + ctrl('m', 'Masa (kg)', 1, 50, 1, 10) + ctrl('f', 'Fuerza aplicada (N), en el piso', 0, 200, 5, 60) + ctrl('mu', 'Coeficiente de rozamiento', 0, 0.8, 0.05, 0.2) + ctrl('g', 'Inclinación (°), en el plano', 5, 60, 5, 30), function (o) {
      var mo = o.mo || 'piso', m = o.m || 10, F = o.f == null ? 60 : o.f, mu = o.mu == null ? 0.2 : o.mu, ang = o.g || 30, d = dcl(mo, m, F, mu, ang, 9), P = [];
      P.push({ vis: dcl(mo, m, F, mu, ang, 1).svg, txt: 'El <b>peso</b> apunta hacia abajo: P = m · g = ' + m + ' · ' + G + ' = ' + f2(d.P) + ' N.' });
      P.push({ vis: dcl(mo, m, F, mu, ang, 2).svg, txt: 'La <b>normal</b> es la fuerza que hace la superficie, perpendicular a ella' + (mo === 'plano' ? ': N = P · cos ' + ang + '° = ' + f2(d.N) + ' N.' : ': aquí N = P = ' + f2(d.N) + ' N.') + (mo === 'piso' && F ? ' Y la fuerza que aplicamos: ' + f2(F) + ' N.' : '') });
      P.push({ vis: dcl(mo, m, F, mu, ang, 3).svg, txt: mu ? 'El <b>rozamiento</b> se opone al movimiento: Fr = μ · N = ' + f2(mu) + ' · ' + f2(d.N) + ' = ' + f2(d.Fr) + ' N.' : 'Sin rozamiento, nada se opone al deslizamiento.' });
      P.push({ vis: d.svg + formula('F neta = ' + (mo === 'plano' ? f2(d.Px) : f2(F)) + ' − ' + f2(d.Fr) + ' = ' + f2(d.net) + ' N', 'a = F neta / m = ' + f2(d.a) + ' m/s²'), txt: d.net > 0 ? '<b>Segunda ley de Newton</b>: la fuerza neta acelera la caja: a = F / m.' : 'La fuerza no alcanza a vencer el rozamiento: la fuerza neta es 0 y la caja <b>queda quieta</b> (primera ley: equilibrio).' });
      P.push({ vis: d.svg, txt: '<b>Tercera ley</b>: la caja también empuja al piso con una fuerza igual y opuesta a la normal; son un par acción-reacción.' });
      return P; });
  } };
  M.fuerzas_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var k = rot(3, u), m = pick([2, 4, 5, 10, 20]);
      if (k === 0) return { cons: '¿Cuánto pesa un objeto de <b>' + m + ' kg</b>? (g = 10 m/s²)', campos: [{ lab: 'P', v: m * G, un: 'N' }], ayuda: 'P = m · g.', bien: '¡Bien! P = ' + m * G + ' N.' };
      var F = m * pick([2, 3, 4, 5]); if (k === 1) return { cons: 'Sobre una caja de <b>' + m + ' kg</b>, sin rozamiento, se aplica una fuerza de <b>' + F + ' N</b>. ¿Qué aceleración adquiere?', campos: [{ lab: 'a', v: F / m, un: 'm/s²' }], ayuda: 'Segunda ley de Newton: a = F / m.', bien: '¡Bien! a = ' + F + ' / ' + m + ' = ' + F / m + ' m/s².' };
      var mu = pick([0.1, 0.2]), Fr = mu * m * G, a = (F - Fr) / m; return { cons: 'Se empuja una caja de <b>' + m + ' kg</b> con <b>' + F + ' N</b>. El coeficiente de rozamiento es <b>' + mu + '</b> (g = 10 m/s²). ¿Qué aceleración tiene?', campos: [{ lab: 'a', v: r2(a), un: 'm/s²', tol: 0.01 }], ayuda: 'Fr = μ·m·g; F neta = F − Fr; a = F neta / m.', bien: '¡Bien! Fr = ' + f2(Fr) + ' N, a = ' + f2(a) + ' m/s².' }; });
  } };

  // 4) VECTORES: suma gráfica (uno a continuación del otro) y componentes
  function vect(A, aA, Bm, aB, fase) { var k = 9, ox = 120, oy = 190, ra = aA * Math.PI / 180, rb = aB * Math.PI / 180, ax = A * Math.cos(ra), ay = A * Math.sin(ra), bx = Bm * Math.cos(rb), by = Bm * Math.sin(rb), rx = ax + bx, ry = ay + by, s = '';
    for (var i = -10; i <= 30; i++) { s += ln(ox + i * k, 10, ox + i * k, 220, '#f1f1f1', 1); } for (i = -3; i <= 20; i++) s += ln(10, oy - i * k, 460, oy - i * k, '#f1f1f1', 1);
    s += fl(ox, oy, ox + ax * k, oy - ay * k, C.teal, 3.5) + tx(ox + ax * k / 2 - 10, oy - ay * k / 2 - 8, 'A', { s: 13, w: 900, c: C.teal });
    if (fase >= 1) s += fl(ox + ax * k, oy - ay * k, ox + rx * k, oy - ry * k, C.azul, 3.5) + tx(ox + (ax + bx / 2) * k + 8, oy - (ay + by / 2) * k - 4, 'B', { s: 13, w: 900, c: C.azul });
    else s += fl(ox, oy, ox + bx * k, oy - by * k, C.azul, 3.5, ' stroke-dasharray="6 3"') + tx(ox + bx * k / 2 + 10, oy - by * k / 2, 'B', { s: 13, w: 900, c: C.azul });
    if (fase >= 2) s += fl(ox, oy, ox + rx * k, oy - ry * k, C.coral, 4) + tx(ox + rx * k / 2 + 12, oy - ry * k / 2 + 14, 'R', { s: 14, w: 900, c: C.coral });
    if (fase >= 3) s += ln(ox, oy, ox + rx * k, oy, C.sol, 2, ' stroke-dasharray="4 3"') + ln(ox + rx * k, oy, ox + rx * k, oy - ry * k, C.sol, 2, ' stroke-dasharray="4 3"') + tx(ox + rx * k / 2, oy + 16, 'Rx = ' + f2(rx), { a: 'middle', s: 11, w: 800, c: C.sol }) + tx(ox + rx * k + 6, oy - ry * k / 2, 'Ry = ' + f2(ry), { s: 11, w: 800, c: C.sol });
    return { svg: S(470, 230, s), rx: rx, ry: ry, R: Math.sqrt(rx * rx + ry * ry), ang: Math.atan2(ry, rx) * 180 / Math.PI }; }
  M.vectores = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('a', 'Módulo de A', 1, 20, 1, 12) + ctrl('aa', 'Ángulo de A (°)', 0, 90, 5, 0) + ctrl('b', 'Módulo de B', 1, 20, 1, 9) + ctrl('ab', 'Ángulo de B (°)', 0, 180, 5, 90), function (o) { var A = o.a || 12, aA = o.aa || 0, Bm = o.b || 9, aB = o.ab == null ? 90 : o.ab, v = vect(A, aA, Bm, aB, 3);
      return [{ vis: vect(A, aA, Bm, aB, 0).svg, txt: 'Dos <b>vectores</b>: cada uno tiene módulo (largo), dirección y sentido. A = ' + A + ' a ' + aA + '°; B = ' + Bm + ' a ' + aB + '°.' }, { vis: vect(A, aA, Bm, aB, 1).svg, txt: 'Para sumarlos, ponemos el origen de B en la punta de A (método del polígono).' },
        { vis: vect(A, aA, Bm, aB, 2).svg, txt: 'La <b>resultante</b> R va del origen de A a la punta de B.' }, { vis: v.svg + formula('R = √(Rx² + Ry²) = √(' + f2(v.rx) + '² + ' + f2(v.ry) + '²) ≈ ' + f2(v.R), 'ángulo ≈ ' + f2(v.ang) + '°'), txt: 'Con las <b>componentes</b> (cuánto avanza en x y en y) calculamos el módulo con Pitágoras.' }]; });
  } };
  M.vectores_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var k = rot(3, u), t = pick([[3, 4, 5], [6, 8, 10], [5, 12, 13], [8, 15, 17]]);
      if (k === 0) return { cons: 'Dos fuerzas de <b>' + t[0] + ' N</b> y <b>' + t[1] + ' N</b> actúan en la misma dirección y sentido. ¿Cuánto vale la resultante?', campos: [{ lab: 'R', v: t[0] + t[1], un: 'N' }], ayuda: 'Mismo sentido: se suman.', bien: '¡Bien! ' + (t[0] + t[1]) + ' N.' };
      if (k === 1) return { cons: 'Dos fuerzas de <b>' + t[1] + ' N</b> y <b>' + t[0] + ' N</b> actúan en la misma dirección pero en <b>sentidos opuestos</b>. ¿Cuánto vale la resultante?', campos: [{ lab: 'R', v: t[1] - t[0], un: 'N' }], ayuda: 'Sentidos opuestos: se restan.', bien: '¡Bien! ' + (t[1] - t[0]) + ' N.' };
      return { cons: 'Dos fuerzas <b>perpendiculares</b> de <b>' + t[0] + ' N</b> y <b>' + t[1] + ' N</b>. ¿Cuánto vale la resultante?', html: vect(t[0], 0, t[1], 90, 2).svg, campos: [{ lab: 'R', v: t[2], un: 'N' }], ayuda: 'Pitágoras: R = √(a² + b²).', bien: '¡Bien! √(' + t[0] + '² + ' + t[1] + '²) = ' + t[2] + ' N.' }; });
  } };

  // 5) PALANCA: equilibrio de momentos y los tres géneros
  function palanca(g, Rr, br, bp, Fp) { var s = '', y = 120, L = br + bp, k = 360 / L, x0 = 55, xa, xr, xp;
    if (g === 1) { xr = x0; xa = x0 + br * k; xp = x0 + L * k; } else if (g === 2) { xa = x0; xr = x0 + br * k; xp = x0 + L * k; } else { xa = x0; xp = x0 + bp * k; xr = x0 + L * k; }
    s += rc(Math.min(xa, xr, xp) - 6, y - 5, Math.max(xa, xr, xp) - Math.min(xa, xr, xp) + 12, 10, '#8D6E63', C.osc, 3) + '<polygon points="' + xa + ',' + (y + 5) + ' ' + (xa - 16) + ',' + (y + 34) + ' ' + (xa + 16) + ',' + (y + 34) + '" fill="' + C.osc + '"/>' + tx(xa, y + 50, 'apoyo', { a: 'middle', s: 10.5, w: 800 });
    s += rc(xr - 18, y - 42, 36, 36, '#BDBDBD', C.osc, 4) + fl(xr, y - 4, xr, y + 40, C.rosa, 3) + tx(xr, y + 62, 'R = ' + f2(Rr) + ' N', { a: 'middle', s: 11, w: 900, c: C.rosa });
    s += fl(xp, y - 60, xp, y - 8, C.verde, 3) + tx(xp, y - 66, 'P = ' + (Fp == null ? '?' : f2(Fp) + ' N'), { a: 'middle', s: 11, w: 900, c: C.verde });
    s += ln(xa, y + 76, xr, y + 76, C.rosa, 2) + tx((xa + xr) / 2, y + 92, 'br = ' + br + ' m', { a: 'middle', s: 10.5, c: C.rosa }) + ln(xa, y - 86, xp, y - 86, C.verde, 2) + tx((xa + xp) / 2, y - 92, 'bp = ' + bp + ' m', { a: 'middle', s: 10.5, c: C.verde });
    return S(470, 225, s); }
  M.palanca = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('g', 'Tipo de palanca', [[1, '1.º género (apoyo en el medio): sube y baja, tijera'], [2, '2.º género (carga en el medio): carretilla'], [3, '3.º género (fuerza en el medio): pinza, brazo']], p.genero || 1) + ctrl('r', 'Carga R (N)', 10, 500, 10, 200) + ctrl('br', 'Brazo de la carga (m)', 0.5, 4, 0.5, 1) + ctrl('bp', 'Brazo de la potencia (m)', 0.5, 4, 0.5, 2), function (o) {
      var g = +(o.g || 1), Rr = o.r || 200, br = o.br || 1, bp = o.bp || 2; if (g === 2 && bp <= br) bp = br + 1; if (g === 3 && bp >= br) br = bp + 1; var Fp = Rr * br / bp, P = [];
      P.push({ vis: palanca(g, Rr, br, bp), txt: 'Una <b>palanca</b>: una barra que gira sobre un <b>punto de apoyo</b>. Queremos levantar una carga de ' + f2(Rr) + ' N.' });
      P.push({ vis: palanca(g, Rr, br, bp), txt: 'Los <b>brazos</b> son las distancias al apoyo: el de la carga mide ' + br + ' m y el de la potencia, ' + bp + ' m.' });
      P.push({ vis: palanca(g, Rr, br, bp, Fp) + formula('P · bp = R · br', 'P = ' + f2(Rr) + ' · ' + br + ' / ' + bp + ' = ' + f2(Fp) + ' N'), txt: '<b>Ley de la palanca</b>: está en equilibrio cuando la potencia por su brazo es igual a la carga por el suyo.' });
      P.push({ vis: palanca(g, Rr, br, bp, Fp), txt: Fp < Rr ? 'Como el brazo de la potencia es más largo, alcanza con <b>menos fuerza</b> que la carga: la palanca nos ayuda.' : 'Aquí la potencia es <b>mayor</b> que la carga: no ahorra fuerza, pero gana velocidad y precisión (como la pinza o el brazo).' });
      return P; });
  } };
  M.palanca_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var Rr = pick([100, 200, 300, 600]), br = pick([0.5, 1, 1.5]), bp = pick([1.5, 2, 3]), F = r2(Rr * br / bp);
      return { cons: 'Con una palanca de 1.º género queremos levantar <b>' + Rr + ' N</b>. El brazo de la carga mide <b>' + fmt(br) + ' m</b> y el de la potencia, <b>' + fmt(bp) + ' m</b>. ¿Qué fuerza hay que hacer?', html: palanca(1, Rr, br, bp), campos: [{ lab: 'P', v: F, un: 'N', tol: 0.01 }], ayuda: 'P · bp = R · br → P = R · br / bp.', bien: '¡Bien! P = ' + f2(F) + ' N.' }; });
  } };

  // 6) ENERGÍA: montaña rusa o péndulo con barras de energía potencial, cinética y pérdidas
  function pistaE(esc, k, h) { var s = '', pts = esc === 'pendulo' ? [[110, 60], [235, 190], [360, 60]] : [[60, 40], [235, 200], [380, 110]];
    if (esc === 'pendulo') { s += ln(235, 20, pts[k][0], pts[k][1], C.osc, 2) + ci(235, 20, 4, C.osc) + '<path d="M110,60 Q235,250 360,60" fill="none" stroke="#ddd" stroke-dasharray="4 4"/>'; }
    else s += '<path d="M20,40 L60,40 Q160,40 235,200 Q300,110 380,110 L450,110" fill="none" stroke="' + C.osc + '" stroke-width="4"/>';
    s += ci(pts[k][0], pts[k][1] - (esc === 'pendulo' ? 0 : 12), 12, C.coral, C.osc) + ['A', 'B', 'C'].map(function (l, i) { return tx(pts[i][0], pts[i][1] + (esc === 'pendulo' ? -18 : 26) + (i === 1 && esc !== 'pendulo' ? 0 : 0), l, { a: 'middle', s: 12, w: 900, c: C.teal }); }).join('');
    return s; }
  function barrasE(Ep, Ec, Q, tot) { var s = '', L = [['Potencial', Ep, C.azul], ['Cinética', Ec, C.coral], ['Calor (rozamiento)', Q, C.gris]]; L.forEach(function (b, i) { var w = tot ? b[1] / tot * 220 : 0; s += tx(150, 20 + i * 26, b[0], { a: 'end', s: 11, w: 800 }) + rc(158, 8 + i * 26, 220, 16, '#f3f3f3', null, 4) + rc(158, 8 + i * 26, w, 16, b[2], null, 4) + tx(384, 21 + i * 26, f2(b[1]) + ' J', { s: 11, w: 800 }); }); return s; }
  M.energia = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('e', 'Escena', [['montana', 'Carrito en una montaña rusa'], ['pendulo', 'Péndulo']], p.escena || 'montana') + ctrl('m', 'Masa (kg)', 1, 100, 1, 50) + ctrl('h', 'Altura inicial (m)', 1, 40, 1, 20) + ctrl('r', 'Pérdida por rozamiento (%)', 0, 40, 5, 0), function (o) {
      var es = o.e || 'montana', m = o.m || 50, h = o.h || 20, perd = (o.r || 0) / 100, E0 = m * G * h, hB = 0, hC = es === 'pendulo' ? h : h * 0.45, P = [];
      var EB = E0 * (1 - perd / 2), EC = E0 * (1 - perd), EpC = Math.min(EC, m * G * hC), vB = Math.sqrt(2 * EB / m);
      var vis = function (k, Ep, Ec, Q) { return S(470, 238, pistaE(es, k, h)) + S(470, 86, barrasE(Ep, Ec, Q, E0)); };
      P.push({ vis: vis(0, E0, 0, 0), txt: 'En A, arriba y quieto: toda su energía es <b>potencial</b>. Ep = m · g · h = ' + m + ' · ' + G + ' · ' + h + ' = ' + f2(E0) + ' J.' });
      P.push({ vis: vis(1, 0, EB, E0 - EB), txt: 'En B, abajo: la potencial se transformó en <b>cinética</b>' + (perd ? ' (y un poco en calor)' : '') + '. Va a ' + f2(vB) + ' m/s.' });
      P.push({ vis: vis(2, EpC, Math.max(0, EC - EpC), E0 - EC), txt: es === 'pendulo' ? (perd ? 'En C no llega tan alto como en A: parte de la energía se perdió como calor.' : 'En C vuelve a la misma altura: sin rozamiento, la energía se conserva.') : 'En C tiene un poco de cada una: la suma sigue siendo ' + f2(EC) + ' J.' });
      P.push({ vis: vis(2, EpC, Math.max(0, EC - EpC), E0 - EC), txt: '<b>Conservación de la energía</b>: no se crea ni se destruye, se transforma. ' + (perd ? 'Lo que "falta" se fue como calor por el rozamiento.' : 'Sin rozamiento, la energía mecánica total no cambia.') });
      return P; });
  } };
  M.energia_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var k = rot(3, u), m = pick([2, 5, 10, 20, 50]), h = pick([5, 10, 20, 45]), v = pick([2, 4, 6, 10]);
      if (k === 0) return { cons: '¿Cuánta energía potencial tiene un objeto de <b>' + m + ' kg</b> a <b>' + h + ' m</b> de altura? (g = 10 m/s²)', campos: [{ lab: 'Ep', v: m * G * h, un: 'J' }], ayuda: 'Ep = m · g · h.', bien: '¡Bien! ' + m * G * h + ' J.' };
      if (k === 1) return { cons: '¿Cuánta energía cinética tiene un objeto de <b>' + m + ' kg</b> que va a <b>' + v + ' m/s</b>?', campos: [{ lab: 'Ec', v: m * v * v / 2, un: 'J' }], ayuda: 'Ec = ½ · m · v².', bien: '¡Bien! ½ · ' + m + ' · ' + v + '² = ' + m * v * v / 2 + ' J.' };
      return { cons: 'Un carrito parte del reposo desde <b>' + h + ' m</b> de altura, sin rozamiento. ¿A qué velocidad llega abajo? (g = 10 m/s²)', campos: [{ lab: 'v', v: Math.sqrt(2 * G * h), un: 'm/s', tol: 0.05 }], ayuda: 'm·g·h = ½·m·v² → v = √(2·g·h).', bien: '¡Bien! v = √(2·10·' + h + ') = ' + f2(Math.sqrt(2 * G * h)) + ' m/s.' }; });
  } };

  // 7) ONDAS: amplitud, longitud de onda, frecuencia y sonido
  function onda(A, lam, fase) { var s = ln(20, 110, 450, 110, '#ccc', 1), pts = []; for (var x = 0; x <= 430; x += 3) pts.push(r1(20 + x) + ',' + r1(110 - A * 8 * Math.sin(2 * Math.PI * x / (lam * 40)))); s += '<polyline points="' + pts.join(' ') + '" fill="none" stroke="' + C.teal + '" stroke-width="3"/>';
    if (fase >= 1) s += fl(20 + lam * 10, 110, 20 + lam * 10, 110 - A * 8, C.coral, 2.5) + tx(28 + lam * 10, 110 - A * 4, 'A', { s: 13, w: 900, c: C.coral });
    if (fase >= 2) s += fl(20 + lam * 10, 110 - A * 8 - 12, 20 + lam * 50, 110 - A * 8 - 12, C.azul, 2.5) + fl(20 + lam * 50, 110 - A * 8 - 12, 20 + lam * 10, 110 - A * 8 - 12, C.azul, 2.5) + tx(20 + lam * 30, 110 - A * 8 - 18, 'λ = ' + f2(lam) + ' m', { a: 'middle', s: 12, w: 900, c: C.azul });
    return S(470, 210, s); }
  M.onda = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('a', 'Amplitud', 1, 10, 1, 5) + ctrl('l', 'Longitud de onda λ (m)', 1, 5, 0.5, 2) + ctrl('f', 'Frecuencia (Hz)', 20, 2000, 20, 170), function (o) { var A = o.a || 5, lam = o.l || 2, f = o.f || 170, v = lam * f, P = [];
      P.push({ vis: onda(A, lam, 0), txt: 'Una <b>onda</b> transporta energía sin transportar materia: el medio vibra y la perturbación avanza.' });
      P.push({ vis: onda(A, lam, 1), txt: 'La <b>amplitud</b> es cuánto se aleja del equilibrio. En el sonido, más amplitud es un sonido <b>' + (A > 5 ? 'más fuerte' : 'más débil') + '</b>.' });
      P.push({ vis: onda(A, lam, 2), txt: 'La <b>longitud de onda</b> (λ) es la distancia entre dos crestas: ' + f2(lam) + ' m.' });
      P.push({ vis: onda(A, lam, 2) + formula('v = λ · f = ' + f2(lam) + ' · ' + f2(f) + ' = ' + f2(v) + ' m/s'), txt: 'La <b>frecuencia</b> es cuántas oscilaciones hay por segundo (' + f2(f) + ' Hz). La velocidad de la onda es λ por f.' });
      P.push({ vis: onda(A, lam, 2), txt: 'En el sonido, la frecuencia da la altura: ' + f2(f) + ' Hz es un sonido <b>' + (f < 300 ? 'grave' : f > 1000 ? 'agudo' : 'medio') + '</b>. Las personas oímos entre 20 y 20.000 Hz.' });
      return P; });
  } };
  M.onda_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var lam = pick([0.5, 1, 2, 4]), f = pick([10, 20, 50, 85, 170]);
      if (rot(2, u)) return { cons: 'Una onda tiene una longitud de onda de <b>' + fmt(lam) + ' m</b> y una frecuencia de <b>' + f + ' Hz</b>. ¿A qué velocidad se propaga?', html: onda(4, lam, 2), campos: [{ lab: 'v', v: lam * f, un: 'm/s' }], ayuda: 'v = λ · f.', bien: '¡Bien! ' + fmt(lam) + ' · ' + f + ' = ' + fmt(lam * f) + ' m/s.' };
      var v = 340; return { cons: 'El sonido viaja en el aire a <b>340 m/s</b>. ¿Cuál es la longitud de onda de un sonido de <b>' + f * 2 + ' Hz</b>?', campos: [{ lab: 'λ', v: r2(v / (f * 2)), un: 'm', tol: 0.01 }], ayuda: 'λ = v / f.', bien: '¡Bien! λ = 340 / ' + f * 2 + ' = ' + f2(v / (f * 2)) + ' m.' }; });
  } };

  // 8) LUZ: sombras, reflexión y refracción
  function luz(modo, a, d) { var s = '';
    if (modo === 'sombra') { var xl = 40, xo = 40 + d * 30, xp = 440, ho = 40, hs = ho * (xp - xl) / (xo - xl); s += em(xl, 120, '💡', 26) + rc(xo - 4, 120 - ho / 2, 8, ho, C.osc) + ln(xp, 10, xp, 230, C.osc, 3) + rc(xp - 3, 120 - Math.min(hs, 220) / 2, 6, Math.min(hs, 220), '#555') + ln(xl, 120, xp, 120 - hs / 2, '#F5D33B', 2) + ln(xl, 120, xp, 120 + hs / 2, '#F5D33B', 2) + tx(xo, 120 + ho / 2 + 18, 'objeto', { a: 'middle', s: 10.5 }) + tx(xp - 8, 236, 'pantalla', { a: 'end', s: 10.5 }); return { svg: S(470, 245, s), hs: hs / ho }; }
    var cx = 235, cy = 130, r = a * Math.PI / 180; s += ln(cx, 20, cx, 240, '#aaa', 1.5, ' stroke-dasharray="5 4"') + tx(cx + 4, 30, 'normal', { s: 10, c: '#888' });
    if (modo === 'reflexion') { s += rc(30, cy, 410, 10, '#B0BEC5', C.osc) + fl(cx - 110 * Math.sin(r), cy - 110 * Math.cos(r), cx, cy, C.coral, 3) + fl(cx, cy, cx + 110 * Math.sin(r), cy - 110 * Math.cos(r), C.coral, 3, ' stroke-dasharray="7 3"') + tx(cx - 30, cy - 70, a + '°', { a: 'middle', s: 12, w: 900, c: C.coral }) + tx(cx + 30, cy - 70, a + '°', { a: 'middle', s: 12, w: 900, c: C.coral }) + tx(235, cy + 32, 'espejo', { a: 'middle', s: 11 }); return { svg: S(470, 190, s) }; }
    var n1 = 1, n2 = 1.33, sr = n1 / n2 * Math.sin(r), r2a = Math.asin(sr), bb = r2a * 180 / Math.PI;
    s += rc(20, cy, 430, 110, '#D6EEF8') + tx(40, 50, 'aire (n = 1)', { s: 11, w: 800 }) + tx(40, 225, 'agua (n = 1,33)', { s: 11, w: 800 }) + fl(cx - 110 * Math.sin(r), cy - 110 * Math.cos(r), cx, cy, C.coral, 3) + fl(cx, cy, cx + 100 * Math.sin(r2a), cy + 100 * Math.cos(r2a), C.coral, 3) + tx(cx - 28, cy - 60, a + '°', { a: 'middle', s: 12, w: 900, c: C.coral }) + tx(cx + 26, cy + 70, f2(bb) + '°', { a: 'middle', s: 12, w: 900, c: C.coral });
    return { svg: S(470, 245, s), b: bb }; }
  M.luz = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Fenómeno', [['sombra', 'Sombras'], ['reflexion', 'Reflexión en un espejo'], ['refraccion', 'Refracción (aire → agua)']], p.modo || 'sombra') + ctrl('a', 'Ángulo de incidencia (°)', 5, 80, 5, 40) + ctrl('d', 'Distancia de la lámpara al objeto (para sombras)', 1, 12, 1, 4), function (o) { var m = o.m || 'sombra', a = o.a || 40, d = o.d || 4, L = luz(m, a, d);
      if (m === 'sombra') return [{ vis: L.svg, txt: 'La luz viaja en <b>línea recta</b>. Donde un objeto opaco la frena, se forma una <b>sombra</b>.' }, { vis: L.svg, txt: 'Con la lámpara a ' + d + ' unidades del objeto, la sombra es <b>' + f2(L.hs) + ' veces</b> más grande que el objeto.' }, { vis: luz(m, a, Math.min(12, d + 4)).svg, txt: 'Si alejamos la lámpara, la sombra se <b>achica</b>; si la acercamos, crece.' }];
      if (m === 'reflexion') return [{ vis: luz(m, a).svg.replace(/stroke-dasharray="7 3"[^>]*>/, '>'), txt: 'Un rayo de luz llega al espejo. La <b>normal</b> es la línea perpendicular al espejo.' }, { vis: L.svg, txt: '<b>Ley de la reflexión</b>: el ángulo de reflexión es igual al de incidencia (' + a + '°), medidos desde la normal.' }];
      return [{ vis: L.svg, txt: 'Al pasar del aire al agua, la luz cambia de velocidad y se <b>desvía</b>: es la refracción.' }, { vis: L.svg + formula('n₁ · sen α = n₂ · sen β', '1 · sen ' + a + '° = 1,33 · sen β → β ≈ ' + f2(L.b) + '°'), txt: 'Se acerca a la normal, porque en el agua la luz va más lenta (ley de Snell). Por eso una pajita parece quebrada en un vaso.' }]; });
  } };
  M.luz_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { if (rot(2, u)) { var a = pick([20, 30, 35, 45, 60]); return { cons: 'Un rayo llega a un espejo con un ángulo de incidencia de <b>' + a + '°</b> respecto de la normal. ¿Cuál es el ángulo de reflexión?', html: luz('reflexion', a).svg, campos: [{ lab: 'Ángulo', v: a, un: '°' }], ayuda: 'Ley de la reflexión: los dos ángulos son iguales.', bien: '¡Bien! ' + a + '°.' }; }
      var ho = pick([10, 20, 30]), dl = pick([1, 2, 4]), dp = dl * pick([2, 3, 4]); return { cons: 'Una lámpara está a <b>' + dl + ' m</b> de un objeto de <b>' + ho + ' cm</b> de alto, y la pared está a <b>' + dp + ' m</b> de la lámpara. ¿Cuánto mide la sombra?', campos: [{ lab: 'Sombra', v: ho * dp / dl, un: 'cm' }], ayuda: 'Triángulos semejantes: sombra = objeto · (distancia a la pared / distancia al objeto).', bien: '¡Bien! ' + ho + ' · ' + dp + ' / ' + dl + ' = ' + ho * dp / dl + ' cm.' }; });
  } };

  // 9) CALOR: dos cuerpos en contacto llegan al equilibrio térmico; Q = m · c · ΔT
  function termos(T1, T2, Tf, fase) { var s = '', col = function (t) { return t > 60 ? '#E53935' : t > 30 ? '#FB8C00' : t > 15 ? '#FDD835' : '#42A5F5'; };
    [[T1, 120, 'agua caliente'], [T2, 350, 'agua fría']].forEach(function (q, i) { var t = fase >= 2 ? Tf : q[0]; s += rc(q[1] - 60, 70, 120, 110, col(t), C.osc, 10) + tx(q[1], 132, fmt(Math.round(t * 10) / 10) + ' °C', { a: 'middle', s: 18, w: 900, c: '#fff' }) + tx(q[1], 200, q[2], { a: 'middle', s: 11, w: 800 }); });
    if (fase === 1) s += fl(190, 125, 280, 125, C.coral, 5) + tx(235, 110, 'calor', { a: 'middle', s: 12, w: 900, c: C.coral });
    if (fase >= 2) s += tx(235, 40, 'equilibrio térmico', { a: 'middle', s: 14, w: 900, c: C.teal });
    return S(470, 215, s); }
  M.calor = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('m1', 'Masa del agua caliente (g)', 50, 500, 50, 200) + ctrl('t1', 'Temperatura caliente (°C)', 40, 100, 5, 80) + ctrl('m2', 'Masa del agua fría (g)', 50, 500, 50, 300) + ctrl('t2', 'Temperatura fría (°C)', 0, 30, 5, 10), function (o) { var m1 = o.m1 || 200, T1 = o.t1 || 80, m2 = o.m2 || 300, T2 = o.t2 == null ? 10 : o.t2, Tf = (m1 * T1 + m2 * T2) / (m1 + m2), Q = m1 * (T1 - Tf);
      return [{ vis: termos(T1, T2, Tf, 0), txt: 'Ponemos en contacto ' + m1 + ' g de agua a ' + T1 + ' °C con ' + m2 + ' g a ' + T2 + ' °C. La <b>temperatura</b> mide qué tan rápido se mueven sus partículas.' },
        { vis: termos(T1, T2, Tf, 1), txt: 'El <b>calor</b> es energía que pasa siempre del cuerpo más caliente al más frío.' },
        { vis: termos(T1, T2, Tf, 2) + formula('Tf = (m₁·T₁ + m₂·T₂) / (m₁ + m₂) = ' + f2(Tf) + ' °C'), txt: 'Pasa calor hasta que los dos quedan a la misma temperatura: el <b>equilibrio térmico</b>. La más pesada «pesa» más en el resultado.' },
        { vis: termos(T1, T2, Tf, 2) + formula('Q = m · c · ΔT = ' + m1 + ' · 1 · ' + f2(T1 - Tf) + ' = ' + f2(Q) + ' cal'), txt: 'Calor que cedió el agua caliente (c del agua = 1 cal/g·°C). Es el mismo que ganó la fría.' }]; });
  } };
  M.calor_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { var m = pick([100, 200, 250, 500]), dT = pick([10, 20, 30, 40]);
      if (rot(2, u)) return { cons: '¿Cuántas calorías hacen falta para calentar <b>' + m + ' g</b> de agua de 20 °C a <b>' + (20 + dT) + ' °C</b>? (c = 1 cal/g·°C)', campos: [{ lab: 'Q', v: m * dT, un: 'cal' }], ayuda: 'Q = m · c · ΔT.', bien: '¡Bien! Q = ' + m + ' · 1 · ' + dT + ' = ' + m * dT + ' cal.' };
      var T1 = pick([60, 80, 90]), T2 = pick([10, 20]); return { cons: 'Se mezclan <b>' + m + ' g</b> de agua a <b>' + T1 + ' °C</b> con <b>' + m + ' g</b> a <b>' + T2 + ' °C</b>. ¿A qué temperatura quedan?', campos: [{ lab: 'Tf', v: (T1 + T2) / 2, un: '°C' }], ayuda: 'Con masas iguales, la temperatura final es el promedio.', bien: '¡Bien! (' + T1 + ' + ' + T2 + ') / 2 = ' + (T1 + T2) / 2 + ' °C.' }; });
  } };

  // 10) FLUIDOS: presión hidrostática y empuje (Arquímedes)
  M.fluidos = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Tema', [['presion', 'Presión en el agua'], ['empuje', 'Empuje (Arquímedes)']], p.modo || 'presion') + ctrl('h', 'Profundidad (m)', 1, 40, 1, 10) + ctrl('v', 'Volumen del objeto (L)', 1, 20, 1, 5) + ctrl('ms', 'Masa del objeto (kg)', 1, 30, 1, 3), function (o) { var md = o.m || 'presion', h = o.h || 10, V = o.v || 5, ms = o.ms == null ? 3 : o.ms, P = [];
      if (md === 'presion') { var Ph = 1000 * G * h, y = 30 + Math.min(h, 40) * 4.5, s = rc(40, 20, 390, 200, '#BBDEFB') + ln(40, 20, 430, 20, C.azul, 3) + em(235, y, '🤿', 26) + fl(235, 22, 235, y - 16, C.osc, 2) + tx(250, (22 + y) / 2, h + ' m', { s: 12, w: 900 });
        P.push({ vis: S(470, 230, s), txt: 'Un buzo baja ' + h + ' m. Sobre él está todo el peso del agua de arriba.' });
        P.push({ vis: S(470, 230, s) + formula('P = ρ · g · h = 1000 · ' + G + ' · ' + h + ' = ' + fmt(Ph) + ' Pa'), txt: 'La <b>presión hidrostática</b> depende de la densidad del líquido y de la profundidad, no de la forma del recipiente.' });
        P.push({ vis: S(470, 230, s), txt: 'Cada 10 m de agua la presión aumenta unos 100.000 Pa: casi <b>1 atmósfera</b> más. A ' + h + ' m, el buzo soporta ' + fmt(Math.round(Ph / 1013) / 100) + ' atm además del aire.' });
        return P; }
      var E = 1000 * V / 1000 * G, Pw = ms * G, flota = E > Pw, y2 = flota ? 90 : 165, kf = Math.min(2, 60 / Math.max(E, Pw)), s2 = rc(80, 50, 310, 170, '#BBDEFB') + rc(205, y2 - 25, 60, 50, '#FFE0B2', C.osc, 6) + fl(235, y2, 235, y2 + Pw * kf + 10, C.rosa, 3) + tx(250, y2 + Pw * kf + 10, 'P = ' + f2(Pw) + ' N', { s: 11, w: 900, c: C.rosa }) + fl(235, y2, 235, y2 - E * kf - 10, C.azul, 3) + tx(250, y2 - E * kf - 6, 'E = ' + f2(E) + ' N', { s: 11, w: 900, c: C.azul });
      P.push({ vis: S(470, 240, s2), txt: 'Un objeto de ' + V + ' L y ' + ms + ' kg en el agua. Su peso es ' + f2(Pw) + ' N.' });
      P.push({ vis: S(470, 240, s2) + formula('E = ρ · V · g = 1 kg/L · ' + V + ' L · ' + G + ' = ' + f2(E) + ' N'), txt: '<b>Principio de Arquímedes</b>: el agua empuja hacia arriba con una fuerza igual al peso del agua que el objeto desaloja.' });
      P.push({ vis: S(470, 240, s2), txt: flota ? 'El empuje es mayor que el peso: el objeto <b>flota</b> y queda en parte afuera del agua.' : 'El peso es mayor que el empuje: el objeto <b>se hunde</b>, aunque en el agua «pesa» menos (' + f2(Pw - E) + ' N).' });
      return P; });
  } };
  M.fluidos_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { if (rot(2, u)) { var h = pick([2, 5, 10, 20, 30]); return { cons: '¿Qué presión hace el agua a <b>' + h + ' m</b> de profundidad? (ρ = 1000 kg/m³, g = 10 m/s²)', campos: [{ lab: 'P', v: 10000 * h, un: 'Pa' }], ayuda: 'P = ρ · g · h.', bien: '¡Bien! 1000 · 10 · ' + h + ' = ' + fmt(10000 * h) + ' Pa.' }; }
      var V = pick([2, 3, 5, 8]); return { cons: 'Un objeto de <b>' + V + ' L</b> está totalmente sumergido en agua. ¿Qué empuje recibe? (1 L de agua pesa 10 N)', campos: [{ lab: 'E', v: V * 10, un: 'N' }], ayuda: 'El empuje es el peso del agua desalojada.', bien: '¡Bien! ' + V + ' L de agua pesan ' + V * 10 + ' N.' }; });
  } };

  // 11) IMANES: polos, líneas de campo y electroimán
  function iman(x, y, gir) { return '<g transform="rotate(' + (gir || 0) + ' ' + x + ' ' + y + ')">' + rc(x - 50, y - 15, 50, 30, '#E53935', C.osc, 3) + rc(x, y - 15, 50, 30, '#1E88E5', C.osc, 3) + tx(x - 25, y + 6, 'N', { a: 'middle', s: 15, w: 900, c: '#fff' }) + tx(x + 25, y + 6, 'S', { a: 'middle', s: 15, w: 900, c: '#fff' }) + '</g>'; }
  M.iman = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Tema', [['polos', 'Polos y campo magnético'], ['electro', 'Electroimán']], p.modo || 'polos') + ctrl('n', 'Vueltas del cable (electroimán)', 5, 50, 5, 20) + ctrl('i', 'Corriente (A)', 0, 3, 0.5, 1.5), function (o) { var md = o.m || 'polos', P = [];
      if (md === 'polos') { var lineas = ''; for (var k = 1; k <= 4; k++) lineas += '<path d="M185,115 C185,' + (115 - k * 26) + ' 285,' + (115 - k * 26) + ' 285,115" fill="none" stroke="' + C.gris + '" stroke-width="1.5" marker-end="url(#natfl)"/><path d="M185,115 C185,' + (115 + k * 26) + ' 285,' + (115 + k * 26) + ' 285,115" fill="none" stroke="' + C.gris + '" stroke-width="1.5" marker-end="url(#natfl)"/>';
        P.push({ vis: S(470, 230, iman(235, 115)), txt: 'Todo imán tiene dos <b>polos</b>: norte (N) y sur (S). Si se lo corta, cada pedazo vuelve a tener los dos.' });
        P.push({ vis: S(470, 230, lineas + iman(235, 115)), txt: 'Las <b>líneas de campo</b> salen del norte y entran por el sur. Las limaduras de hierro las dibujan solas.' });
        P.push({ vis: S(470, 120, iman(120, 40) + iman(330, 40) + tx(225, 46, '→ ← se atraen', { a: 'middle', s: 12, w: 900, c: C.verde }) + iman(120, 95) + iman(330, 95, 180) + tx(225, 101, '← → se repelen', { a: 'middle', s: 12, w: 900, c: C.rosa })), txt: 'Polos <b>distintos se atraen</b>; polos <b>iguales se repelen</b>.' });
        P.push({ vis: S(470, 150, ci(235, 75, 60, '#fff', C.osc) + '<polygon points="235,25 245,75 225,75" fill="#E53935"/><polygon points="235,125 245,75 225,75" fill="#1E88E5"/>' + tx(235, 14, 'N geográfico', { a: 'middle', s: 11, w: 800 })), txt: 'La Tierra es un gran imán: por eso la aguja de la <b>brújula</b> apunta siempre hacia el norte.' });
        return P; }
      var n = o.n || 20, I = o.i == null ? 1.5 : o.i, fuerza = n * I, clavos = Math.min(12, Math.round(fuerza / 5)), s = rc(150, 90, 170, 40, '#B0BEC5', C.osc, 4);
      for (var j = 0; j < Math.min(n, 30); j++) s += '<ellipse cx="' + r1(160 + j * 5) + '" cy="110" rx="3" ry="24" fill="none" stroke="#C2552E" stroke-width="2"/>';
      s += rc(40, 150, 40, 50, '#fff', C.osc, 4) + tx(60, 180, I + ' A', { a: 'middle', s: 11, w: 900 }) + '<polyline points="60,150 60,110 150,110" fill="none" stroke="#C2552E" stroke-width="2"/>';
      var cl = ''; for (j = 0; j < clavos; j++) cl += '<line x1="' + (330 + (j % 4) * 10) + '" y1="' + (95 + Math.floor(j / 4) * 14) + '" x2="' + (352 + (j % 4) * 10) + '" y2="' + (99 + Math.floor(j / 4) * 14) + '" stroke="#555" stroke-width="3"/>';
      P.push({ vis: S(470, 220, s), txt: 'Un <b>electroimán</b>: un clavo de hierro con un cable enrollado (' + n + ' vueltas).' });
      P.push({ vis: S(470, 220, s + (I ? cl : '')), txt: I ? 'Al pasar corriente (' + I + ' A), el clavo se <b>imanta</b> y atrae ' + clavos + ' clavitos. Sin corriente, los suelta.' : 'Sin corriente no hay imán: no atrae nada.' });
      P.push({ vis: S(470, 220, s + (I ? cl : '')), txt: 'Más vueltas o más corriente = un electroimán más fuerte. Se usan en grúas de chatarra, timbres y parlantes.' });
      return P; });
  } };
  M.iman_x = { tipo: 'ejercicio', render: function (el, p, api) {
    elegir(el, api, function () { var a = pick(['N', 'S']), b = pick(['N', 'S']), ok = a === b ? 'Se repelen' : 'Se atraen'; return { cons: 'Acercamos el polo <b>' + a + '</b> de un imán al polo <b>' + b + '</b> de otro. ¿Qué pasa?', ops: ['Se atraen', 'Se repelen', 'No pasa nada'], ok: ok, ayuda: 'Polos iguales se repelen; distintos se atraen.' }; });
  } };

  // 12) TIERRA Y LUNA: día y noche, estaciones y fases de la Luna
  var FASES = [['Luna nueva', 0], ['Cuarto creciente', 7], ['Luna llena', 15], ['Cuarto menguante', 22]];
  function faseNom(d) { d = d % 29.5; return d < 2 || d > 27.5 ? 'Luna nueva' : d < 6 ? 'creciente' : d < 9 ? 'Cuarto creciente' : d < 13 ? 'gibosa creciente' : d < 17 ? 'Luna llena' : d < 21 ? 'gibosa menguante' : d < 24 ? 'Cuarto menguante' : 'menguante'; }
  function lunaVista(cx, cy, r, d) { var f = (d % 29.5) / 29.5, ilum = (1 - Math.cos(2 * Math.PI * f)) / 2, x = r * (1 - 2 * ilum), lado = f < 0.5 ? 1 : 0;
    return ci(cx, cy, r, '#37474F') + '<path d="M' + cx + ',' + (cy - r) + ' A' + r + ',' + r + ' 0 0 ' + lado + ' ' + cx + ',' + (cy + r) + ' A' + r1(Math.abs(x)) + ',' + r + ' 0 0 ' + (x > 0 ? 1 - lado : lado) + ' ' + cx + ',' + (cy - r) + '" fill="#FFF8E1"/>'; }
  M.tierra_luna = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Tema', [['dia', 'Día y noche'], ['estaciones', 'Las estaciones'], ['fases', 'Fases de la Luna']], p.modo || 'fases') + ctrl('d', 'Día del ciclo lunar (fases)', 0, 29, 1, 7), function (o) { var md = o.m || 'fases', P = [];
      if (md === 'dia') { var tierra = function (giro) { return '<defs><clipPath id="nt"><circle cx="300" cy="115" r="70"/></clipPath></defs>' + ci(300, 115, 70, '#4FC3F7') + '<g clip-path="url(#nt)"><rect x="300" y="45" width="80" height="140" fill="rgba(0,0,40,.55)"/></g>' + em(70, 115, '☀️', 50) + [0, 1, 2, 3].map(function (i) { return fl(110, 80 + i * 24, 220, 80 + i * 24, '#F5D33B', 2); }).join('') + em(300 + 50 * Math.cos(giro), 115 + 50 * Math.sin(giro), '🏠', 18); };
        P.push({ vis: S(470, 235, tierra(Math.PI)), txt: 'El Sol ilumina siempre <b>la mitad</b> de la Tierra: de ese lado es de día.' });
        P.push({ vis: S(470, 235, tierra(-Math.PI / 2)), txt: 'La Tierra <b>rota</b> sobre su eje de oeste a este: da una vuelta completa cada 24 horas.' });
        P.push({ vis: S(470, 235, tierra(0)), txt: 'Al girar, nuestra casa pasa al lado oscuro: es de <b>noche</b>. Por eso el Sol parece salir por el este y ponerse por el oeste.' }); return P; }
      if (md === 'estaciones') { var orb = function (k) { var s = '<ellipse cx="235" cy="120" rx="180" ry="80" fill="none" stroke="#ccc" stroke-dasharray="5 4"/>' + em(235, 120, '☀️', 44), pos = [[415, 120], [235, 40], [55, 120], [235, 200]], nm = ['diciembre: verano en el sur', 'marzo: otoño en el sur', 'junio: invierno en el sur', 'septiembre: primavera en el sur'];
          pos.forEach(function (q, i) { s += '<g transform="rotate(23 ' + q[0] + ' ' + q[1] + ')">' + ci(q[0], q[1], i === k ? 18 : 12, i === k ? '#4FC3F7' : '#B3E5FC', C.osc) + ln(q[0], q[1] - 24, q[0], q[1] + 24, C.osc, 1.5) + '</g>'; }); return S(470, 240, s); };
        P.push({ vis: orb(-1), txt: 'La Tierra da una vuelta al Sol en un año (<b>traslación</b>), con su eje siempre inclinado unos 23°.' });
        P.push({ vis: orb(0), txt: 'Cuando el hemisferio sur se inclina hacia el Sol, los rayos llegan más directos y los días son más largos: <b>verano</b> en la Argentina.' });
        P.push({ vis: orb(2), txt: 'Del otro lado de la órbita, el sur queda inclinado hacia afuera: rayos oblicuos y días cortos, <b>invierno</b>. No es por estar más lejos del Sol.' });
        P.push({ vis: orb(1), txt: 'En los puntos intermedios los dos hemisferios reciben la luz parecida: <b>otoño</b> y <b>primavera</b>.' }); return P; }
      var d = o.d == null ? 7 : o.d, ang = d / 29.5 * 2 * Math.PI, orbita = function (dd) { var a = dd / 29.5 * 2 * Math.PI; return em(30, 120, '☀️', 34) + fl(55, 60, 90, 60, '#F5D33B', 2) + fl(55, 180, 90, 180, '#F5D33B', 2) + ci(235, 120, 26, '#4FC3F7', C.osc) + ci(235, 120, 85, 'none', '#ccc', ' stroke-dasharray="4 4"') + (function () { var x = 235 - 85 * Math.cos(a), y = 120 + 85 * Math.sin(a); return ci(x, y, 12, '#37474F') + '<path d="M' + r1(x) + ',' + r1(y - 12) + ' A12,12 0 0 0 ' + r1(x) + ',' + r1(y + 12) + ' Z" fill="#FFF8E1"/>'; })() + lunaVista(410, 120, 34, dd) + tx(410, 176, 'así se ve', { a: 'middle', s: 11, w: 800 }); };
      P.push({ vis: S(470, 240, orbita(0)), txt: 'La Luna no tiene luz propia: el Sol ilumina siempre su mitad. Tarda unos <b>29,5 días</b> en dar la vuelta a la Tierra.' });
      FASES.forEach(function (fz) { P.push({ vis: S(470, 240, orbita(fz[1])), txt: 'Día ' + fz[1] + ': <b>' + fz[0] + '</b>. ' + (fz[1] === 0 ? 'La Luna está entre la Tierra y el Sol: vemos su lado oscuro.' : fz[1] === 15 ? 'La Tierra está entre el Sol y la Luna: vemos toda la mitad iluminada.' : 'Vemos la mitad de la cara iluminada.') }); });
      P.push({ vis: S(470, 240, orbita(d)), txt: 'Día ' + d + ' del ciclo: fase <b>' + faseNom(d) + '</b>. En el hemisferio sur, la Luna creciente tiene forma de C (de «crece»… al revés que en el norte).' });
      return P; });
    function verD() { var m = el.querySelector('[data-k="m"]'), c = el.querySelector('[data-k="d"]'); if (m && c) c.closest('label').style.display = m.value === 'fases' ? '' : 'none'; }
    el.addEventListener('input', verD); verD();
  } };
  M.tierra_luna_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    elegir(el, api, function () { var k = rot(4, u), fz = FASES[k]; return { cons: '¿Qué fase de la Luna corresponde a este dibujo, visto desde la Tierra?', html: S(470, 110, lunaVista(235, 55, 45, fz[1])), ops: FASES.map(function (q) { return q[0]; }), ok: fz[0], ayuda: 'Toda oscura: nueva; toda iluminada: llena; la mitad: cuarto creciente o menguante.' }; });
  } };

  // 13) SISTEMA SOLAR A ESCALA
  var PLAN = [['Mercurio', 0.39, 0.38, '#9E9E9E'], ['Venus', 0.72, 0.95, '#F5D33B'], ['Tierra', 1, 1, '#4FC3F7'], ['Marte', 1.52, 0.53, '#E53935'], ['Júpiter', 5.2, 11.2, '#FFB74D'], ['Saturno', 9.5, 9.4, '#FFE082'], ['Urano', 19.2, 4, '#80DEEA'], ['Neptuno', 30, 3.9, '#5C6BC0']];
  function sistema(k, modo) { var s = '';
    if (modo === 'tam') { var x = 20; PLAN.forEach(function (q, i) { var r = Math.max(2, q[2] * 4.5); if (i <= k) s += ci(x + r, 120, r, q[3], C.osc) + tx(x + r, 120 + r + 16 + (i % 2) * 12, q[0], { a: 'middle', s: 10, w: 800 }); x += r * 2 + 6; }); return S(470, 210, s); }
    s += ci(14, 100, 12, '#FFB300') + ln(14, 100, 460, 100, '#ddd', 1); PLAN.forEach(function (q, i) { var x = 26 + q[1] / 30 * 430; if (i <= k) s += ci(x, 100, i === k ? 7 : 5, q[3], i === k ? C.coral : C.osc) + ln(x, 92, x, 86 - (i < 4 ? i : i % 2) * 16, '#bbb', 1) + tx(x + (i < 4 ? i * 6 : 0), 82 - (i < 4 ? i : i % 2) * 16, q[0], { a: i === 7 ? 'end' : i < 4 ? 'start' : 'middle', s: 10, w: i === k ? 900 : 700, c: i === k ? C.coral : C.osc }) + (i === k ? tx(x, 122, fmt(q[1]) + ' UA', { a: i === 7 ? 'end' : 'middle', s: 11, w: 900, c: C.coral }) : ''); });
    return S(470, 150, s + tx(235, 146, 'distancia al Sol en unidades astronómicas (1 UA = 150 millones de km)', { a: 'middle', s: 10 })); }
  M.sistema_solar = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Escala de', [['dist', 'distancias'], ['tam', 'tamaños']], p.modo || 'dist'), function (o) { var md = o.m || 'dist', P = [{ vis: sistema(-1, md), txt: md === 'dist' ? 'Ubicamos los planetas según su distancia al Sol, a escala.' : 'Comparamos el tamaño de los planetas, a escala (la Tierra mide 1).' }];
      PLAN.forEach(function (q, i) { P.push({ vis: sistema(i, md), txt: '<b>' + q[0] + '</b>: ' + (md === 'dist' ? fmt(q[1]) + ' UA del Sol.' : fmt(q[2]) + ' veces el diámetro de la Tierra.') + (i === 3 ? ' Los cuatro primeros son rocosos.' : i === 7 ? ' Los cuatro últimos son gigantes gaseosos (o helados).' : '') }); });
      P.push({ vis: sistema(7, md), txt: md === 'dist' ? 'Los planetas interiores están muy juntos y los exteriores, muy separados: el sistema solar es casi todo espacio vacío.' : 'El Sol no entra en el dibujo: mide unas 109 veces la Tierra, unas 10 veces Júpiter.' }); return P; });
  } };
  M.sistema_solar_x = { tipo: 'ejercicio', render: function (el, p, api) {
    ordenar(el, api, function () { var L = mezclar(PLAN.slice()).slice(0, 4).sort(function (a, b) { return a[1] - b[1]; }); return { cons: 'Ordená estos planetas del <b>más cercano</b> al más lejano del Sol.', items: L.map(function (q) { return q[0]; }), ayuda: 'Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno.', bien: '¡Bien! ' + L.map(function (q) { return q[0]; }).join(' → ') + '.' }; });
  } };
})();
