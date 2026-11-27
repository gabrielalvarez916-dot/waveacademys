/* ACTIVIDADES DE NATURALES (banco de ACTIVIDADES; solo actividades de nivel y generales, nunca examen).
   Igual que js/actividades-plus.js: una marca al principio del enunciado cambia la pantalla; lo que arma el alumno se escribe en el campo
   del tipo de pregunta de siempre, así que la corrección es la de siempre. Los dibujos se reusan del banco de la lección (H.nat.d).
   Marcas (ver docs/tipos-de-pregunta.md, sección "Actividades de Naturales"):
     [[rotular:celula_animal]]      matching (izquierda "1","2"…; derecha nombres)     · rotula el dibujo tocando nombre y lugar
     [[red:pastizal]]               classify (elementos = especies; categorías = niveles)· ubica cada especie en su nivel; se dibujan las flechas y la energía
     [[recorrido:digestion]]        ordering (estaciones)                               · lleva la ficha estación por estación
     [[clave:vertebrados]]          multiple_choice (grupos)                            · recorre la clave respondiendo sí / no
     [[punnett:Aa,Aa]]              cualquiera (casi siempre numeric)                   · completa el cuadro de Punnett y ve las proporciones
     [[adn:TACGGA]] [[arn:TACGGA]]  short_answer                                        · arma la cadena complementaria o el ARN con fichas de bases
     [[osmosis:0:animal]]           multiple_choice                                     · mira el medio y la célula antes de predecir
     [[mezclas]]                    matching (izquierda mezclas; derecha métodos)       · elige el aparato para cada mezcla
     [[densidad:120:30]]            numeric                                             · pesa en la balanza y sumerge en la probeta; calcula d
     [[instrumento:termometro:46]]  numeric                                             · lee el instrumento (con lupa)
     [[atomo]]                      cualquiera                                          · arma el átomo con protones, neutrones y electrones
     [[tabla]]                      short_answer                                        · toca el elemento en la tabla periódica (se escribe el símbolo)
     [[balancear:H2+O2>H2O]]        fill_blank (un ___ por coeficiente)                 · balancea con botones + y − y contadores de átomos
     [[ph]]                         classify (categorías ácida, neutra, básica)         · ubica cada sustancia en la escala de colores
     [[ohm:serie:6:4:2]]            cualquiera                                          · banco de circuitos con amperímetro y voltímetro
     [[pista:mruv:0:2]]             cualquiera                                          · el auto avanza segundo a segundo; anota posiciones
     [[dcl]]                        multi_select (fuerzas con "hacia arriba/abajo/…")    · dibuja las fuerzas sobre la caja
     [[graficar:0,10;2,20|t (s)|x (m)]] cualquiera                                       · ubica los puntos de la tabla en el gráfico
     [[experimento]]                classify (Cambia / Se mide / Queda igual)            · arma los dos montajes del experimento
     [[luna]]                       matching (izquierda "1".."4"; derecha fases)        · ubica cada fase en la órbita
     [[plato]]                      classify (categorías = grupos de alimentos)         · arma el plato ubicando cada alimento en su sector */
(function () {
  'use strict';
  var RE = /\[\[(rotular|red|recorrido|clave|punnett|adn|arn|osmosis|mezclas|densidad|instrumento|atomo|tabla|balancear|ph|ohm|pista|dcl|graficar|experimento|luna|plato)(?::([^\]]*))?\]\]\s*/g;
  var NOMBRE = { rotular: ['🏷️', 'Rotulá el dibujo'], red: ['🕸️', 'Armá la red trófica'], recorrido: ['🧭', 'Hacé el recorrido'], clave: ['🔑', 'Usá la clave dicotómica'], punnett: ['🧬', 'Cuadro de Punnett'], adn: ['🧬', 'Armá la cadena de ADN'], arn: ['🧬', 'Armá el ARN mensajero'],
    osmosis: ['💧', 'Ósmosis'], mezclas: ['⚗️', 'Laboratorio de mezclas'], densidad: ['⚖️', 'Medí la densidad'], instrumento: ['🌡️', 'Leé el instrumento'], atomo: ['⚛️', 'Armá el átomo'], tabla: ['🧪', 'Tabla periódica'], balancear: ['⚖️', 'Balanceá la ecuación'],
    ph: ['🌈', 'Escala de pH'], ohm: ['🔌', 'Banco de circuitos'], pista: ['🚗', 'Pista de movimiento'], dcl: ['➡️', 'Dibujá las fuerzas'], graficar: ['📈', 'Graficá los datos'], experimento: ['🔬', 'Diseñá el experimento'], luna: ['🌙', 'Fases de la Luna'], plato: ['🍽️', 'Armá el plato'] };
  var A = {};
  function d() { return window.WaveLeccionBanco && WaveLeccionBanco._h && WaveLeccionBanco._h.nat; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fire(el) { el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }
  function setVal(el, v) { if (!el) return; el.value = v; fire(el); }
  function sonar(n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }
  function mk(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function norm(s) { return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9ñ]+/g, ' ').trim(); }
  function enun(blk) { return blk.querySelector('.mt-preg-c > p, .mt-preg-c > .mt-hueco-p'); }
  function despues(blk, el) { var p = enun(blk); if (p && p.parentNode) p.parentNode.insertBefore(el, p.nextSibling); else blk.querySelector('.mt-preg-c').appendChild(el); }
  function ocultar(el) { if (el) el.classList.add('an-oculto'); }
  function campoNum(blk) { return blk.querySelector('input.nu-in') || blk.querySelector('input.mt-txt'); }
  function campoTxt(blk) { return blk.querySelector('input.mt-txt') || blk.querySelector('textarea.mt-txt'); }
  function sels(blk) { return [].slice.call(blk.querySelectorAll('select.mt-sel')); }
  function filaDe(s) { var p = s.closest('.mt-par'), sp = p && p.querySelector('span'); return sp ? sp.textContent.trim() : ''; }
  function valores(s) { return [].map.call(s.options, function (o) { return o.value; }).filter(Boolean); }
  function selDe(blk, fila) { return sels(blk).filter(function (s) { return norm(filaDe(s)) === norm(fila); })[0]; }
  // Saca la versión «tocando» que arma actividades-plus para unir/clasificar y oculta los desplegables (quedan como respaldo)
  function propio(blk) { [].forEach.call(blk.querySelectorAll('.ap2-uni,.ap2-pool2,.ap2-cajas,.ap2-banco'), function (x) { x.remove(); }); var m = mk('i', 'ap2-banco'); m.hidden = true; blk.appendChild(m); var ps = blk.querySelector('.mt-pares'); ocultar(ps); [].forEach.call(blk.querySelectorAll('.mt-pares'), ocultar); }
  // Fichas para tocar: devuelve la caja con las fichas; on(valor) se llama al tocar un destino [data-dest]
  function fichas(w, vals, alColocar) { var sel = null, b = mk('div', 'an-fichas', vals.map(function (v) { return '<button type="button" class="an-ficha" data-v="' + esc(v) + '">' + esc(v) + '</button>'; }).join(''));
    b.addEventListener('click', function (e) { var f = e.target.closest('.an-ficha'); if (!f) return; sel = f.getAttribute('data-v'); [].forEach.call(b.children, function (x) { x.classList.toggle('on', x === f); }); });
    w.addEventListener('click', function (e) { var t = e.target.closest('[data-dest]'); if (!t || sel == null) return; alColocar(t.getAttribute('data-dest'), sel); sel = null; [].forEach.call(b.children, function (x) { x.classList.remove('on'); }); sonar('bien'); });
    return b; }
  function caja(ayuda) { return mk('div', 'an-caja', ayuda ? '<small class="mt-ayuda">' + ayuda + '</small>' : ''); }

  // 1) ROTULAR -------------------------------------------------------------------------------------------
  A.rotular = function (blk, arg) { var N = d(); if (!N || !N.d) return; var F = N.d.FIG[(arg || 'celula_animal').trim()]; if (!F) return; var S = sels(blk); if (!S.length) return; propio(blk);
    var ox = 135, oy = 8, w = caja('Tocá un nombre y después el número del dibujo donde va.'), vis = mk('div');
    function pintar() { var b = '<g transform="translate(' + ox + ',' + oy + ')">' + F.dib + '</g>', izq = 0, der = 0;
      F.partes.forEach(function (q, j) { var s = selDe(blk, String(j + 1)), v = s ? s.value : '', x = ox + q[1], y = oy + q[2], L = q[1] < 100;
        if (v) { var ly = 28 + (L ? izq++ : der++) * 28; b += N.ln(L ? 128 : 342, ly - 4, x, y, N.C.teal, 1.5) + N.txw(L ? 126 : 344, ly, v, { a: L ? 'end' : 'start', s: 12, w: 800, c: N.C.teal }, 16); }
        b += '<g data-dest="' + j + '" class="nat-tap">' + N.ci(x, y, 11, v ? N.C.claro : '#fff', N.C.osc) + N.tx(x, y + 4.5, j + 1, { a: 'middle', s: 12, w: 900 }) + '</g>'; });
      vis.innerHTML = N.S(470, 245, b); }
    w.appendChild(vis); w.appendChild(fichas(w, valores(S[0]), function (k, v) { var s = selDe(blk, String(+k + 1)); if (s) { setVal(s, v); pintar(); } })); pintar(); despues(blk, w);
  };

  // 2) RED TRÓFICA ---------------------------------------------------------------------------------------
  A.red = function (blk, arg) { var N = d(); if (!N || !N.d) return; var r = N.d.REDES[(arg || 'pastizal').trim()]; var S = sels(blk); if (!r || !S.length) return; propio(blk);
    var cats = valores(S[0]), w = caja('Tocá una especie y después la fila del nivel donde va. Se dibujan las flechas de quién come a quién.'), vis = mk('div'), pool = mk('div', 'an-fichas');
    var spp = S.map(function (s) { var nm = filaDe(s), sp = r.sp.filter(function (q) { return norm(q[0]) === norm(nm); })[0]; return { s: s, nm: nm, sp: sp }; });
    var elegido = null;
    function pintar() { var filas = {}, pos = {}, b = '', nf = cats.length, alto = 60;
      cats.forEach(function (c, k) { var y = 20 + (nf - 1 - k) * alto; b += '<g data-dest="' + k + '" class="nat-tap">' + N.rc(110, y, 350, alto - 8, k % 2 ? '#F3FBF7' : '#fff', N.C.gris, 10) + '</g>' + N.txw(8, y + 28, c, { s: 10.5, w: 800, c: N.C.teal }, 14); filas[c] = []; });
      spp.forEach(function (e) { if (e.s.value && filas[e.s.value]) filas[e.s.value].push(e); });
      cats.forEach(function (c, k) { var y = 20 + (nf - 1 - k) * alto + 24; filas[c].forEach(function (e, i) { pos[e.nm] = [110 + (i + 0.5) * 350 / filas[c].length, y]; }); });
      spp.forEach(function (e) { if (!e.sp || !pos[e.nm]) return; e.sp[3].forEach(function (q) { var presa = r.sp[q][0], a = pos[presa], c = pos[e.nm]; if (!a) { spp.forEach(function (o) { if (norm(o.nm) === norm(presa)) a = pos[o.nm]; }); } if (!a) return; var dx = c[0] - a[0], dy = c[1] - a[1], L = Math.sqrt(dx * dx + dy * dy) || 1; b += N.fl(a[0] + dx / L * 18, a[1] + dy / L * 18, c[0] - dx / L * 20, c[1] - dy / L * 20, N.C.teal, 2); }); });
      spp.forEach(function (e) { var q = pos[e.nm]; if (!q) return; b += N.ci(q[0], q[1], 17, '#fff', N.C.teal) + N.em(q[0], q[1], e.sp ? e.sp[1] : '•', 18) + N.tx(q[0], q[1] + 28, e.nm, { a: 'middle', s: 10, w: 800 }); });
      var listo = spp.every(function (e) { return e.s.value; }); if (listo) { var E = 10000; cats.forEach(function (c, k) { b += N.tx(456, 20 + (nf - 1 - k) * alto + 14, '≈ ' + Math.round(E / Math.pow(10, k)) + ' kcal', { a: 'end', s: 9.5, c: N.C.sol, w: 800 }); }); }
      vis.innerHTML = N.S(470, 24 + nf * alto, b);
      pool.innerHTML = spp.filter(function (e) { return !e.s.value; }).map(function (e) { return '<button type="button" class="an-ficha' + (elegido === e.nm ? ' on' : '') + '" data-sp="' + esc(e.nm) + '">' + (e.sp ? e.sp[1] + ' ' : '') + esc(e.nm) + '</button>'; }).join('') || '<em>Todas ubicadas. Tocá una fila con una especie elegida para moverla.</em>'; }
    pool.addEventListener('click', function (e) { var f = e.target.closest('[data-sp]'); if (!f) return; elegido = f.getAttribute('data-sp'); pintar(); });
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-dest]'); if (!t) { var c = e.target.closest('text'); return; } if (!elegido) return; var en = spp.filter(function (x) { return x.nm === elegido; })[0]; if (en) setVal(en.s, cats[+t.getAttribute('data-dest')]); elegido = null; sonar('bien'); pintar(); });
    w.appendChild(pool); w.appendChild(vis); pintar(); despues(blk, w);
  };

  // 3) RECORRIDO -----------------------------------------------------------------------------------------
  A.recorrido = function (blk, arg) { var N = d(); var ol = blk.querySelector('ol.mt-orden'); if (!N || !N.d || !ol) return; var rc0 = N.d.REC[(arg || '').trim()], lis = [].slice.call(ol.children); ocultar(ol); var ay = blk.querySelector('.mt-ayuda'); if (ay) ocultar(ay);
    var orden = [], n = lis.length, w = caja('Tocá las estaciones en el orden en que pasa la ficha. «Volver a empezar» borra el camino.'), vis = mk('div'), bt = mk('button', 'an-btn', '↺ Volver a empezar'); bt.type = 'button';
    var pos = lis.map(function (_, k) { var por = n > 6 ? 4 : 3; return [60 + (k % por) * (350 / (por - 1)), 50 + Math.floor(k / por) * 90]; });
    function info(nm) { if (!rc0) return null; return rc0.est.filter(function (e) { return norm(e[0]) === norm(nm); })[0]; }
    function pintar() { var b = '', H2 = 40 + Math.ceil(n / (n > 6 ? 4 : 3)) * 90;
      for (var k = 1; k < orden.length; k++) { var a = pos[orden[k - 1]], c = pos[orden[k]]; b += N.fl(a[0], a[1], c[0] - (c[0] - a[0]) * 0.2, c[1] - (c[1] - a[1]) * 0.2, N.C.teal, 3); }
      lis.forEach(function (li, k) { var nm = li.getAttribute('data-v'), e = info(nm), i = orden.indexOf(k); b += '<g data-dest="' + k + '" class="nat-tap">' + N.ci(pos[k][0], pos[k][1], 26, i >= 0 ? N.C.claro : '#fff', i >= 0 ? N.C.teal : N.C.gris) + N.em(pos[k][0], pos[k][1], e ? e[1] : '📍', 22) + '</g>' + N.tx(pos[k][0], pos[k][1] + 42, nm, { a: 'middle', s: 11.5, w: 800 }) + (i >= 0 ? N.tx(pos[k][0] + 22, pos[k][1] - 18, i + 1, { s: 13, w: 900, c: N.C.coral }) : ''); });
      var ult = orden.length ? info(lis[orden[orden.length - 1]].getAttribute('data-v')) : null;
      b += N.rc(105, H2 - 8, 260, 30, orden.length ? N.C.coral : '#F3FBF7', N.C.gris, 15) + N.tx(235, H2 + 12, orden.length ? (rc0 ? rc0.ficha + ' ' : '') + (ult ? 'ahora es: ' + ult[3] : 'en ' + lis[orden[orden.length - 1]].getAttribute('data-v')) : (rc0 ? rc0.ficha + ' ' : '') + 'esperando el primer paso', { a: 'middle', s: 12.5, w: 800, c: orden.length ? '#fff' : N.C.osc });
      vis.innerHTML = N.S(470, H2 + 30, b);
      var L2 = orden.map(function (k) { return lis[k]; }).concat(lis.filter(function (_, k) { return orden.indexOf(k) < 0; })); L2.forEach(function (li) { ol.appendChild(li); }); fire(ol); }
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-dest]'); if (!t) return; var k = +t.getAttribute('data-dest'); if (orden.indexOf(k) >= 0) return; orden.push(k); sonar('bien'); pintar(); });
    bt.addEventListener('click', function () { orden = []; pintar(); });
    w.appendChild(vis); w.appendChild(bt); pintar(); despues(blk, w);
  };

  // 4) CLAVE DICOTÓMICA ----------------------------------------------------------------------------------
  A.clave = function (blk, arg) { var N = d(); if (!N || !N.d) return; var K = N.d.CLAVES[(arg || 'vertebrados').trim()]; if (!K) return; var radios = [].slice.call(blk.querySelectorAll('.mt-op input[type=radio]'));
    var w = caja('Respondé cada pregunta de la clave pensando en el organismo. Al llegar a un grupo, se marca la respuesta.'), cur = 0, cam = [], box = mk('div', 'an-clave');
    function pintar() { var h = cam.map(function (c) { return '<div class="an-cl-paso">' + esc(c[0]) + ' <b>' + c[1] + '</b></div>'; }).join('');
      if (cur < K.q.length && (cam.length === 0 || cam[cam.length - 1][1] === 'No')) h += '<div class="an-cl-q">' + esc(K.q[cur][0]) + '<div><button type="button" class="an-btn" data-r="si">Sí</button> <button type="button" class="an-btn" data-r="no">No</button></div></div>';
      else { var g = cam.length && cam[cam.length - 1][1] === 'Sí' ? K.q[cur][1] : K.resto[0], e = cam.length && cam[cam.length - 1][1] === 'Sí' ? K.q[cur][2] : K.resto[1]; h += '<div class="an-cl-fin">' + e + ' Llegaste a: <b>' + esc(g) + '</b></div><button type="button" class="an-btn" data-r="reset">↺ Recorrer de nuevo</button>';
        radios.forEach(function (r) { if (norm(r.value) === norm(g)) { r.checked = true; fire(r); } }); }
      box.innerHTML = h; }
    box.addEventListener('click', function (e) { var b = e.target.closest('[data-r]'); if (!b) return; var r = b.getAttribute('data-r'); if (r === 'reset') { cur = 0; cam = []; } else if (r === 'si') cam.push([K.q[cur][0], 'Sí']); else { cam.push([K.q[cur][0], 'No']); cur++; } sonar('bien'); pintar(); });
    w.appendChild(box); pintar(); despues(blk, w);
  };

  // 5) PUNNETT -------------------------------------------------------------------------------------------
  A.punnett = function (blk, arg) { var p = String(arg || 'Aa,Aa').split(','), g1 = (p[0] || 'Aa').trim().match(/X[ᴰᵈ]|Y|./g), g2 = (p[1] || 'Aa').trim().match(/X[ᴰᵈ]|Y|./g); if (!g1 || !g2) return;
    var w = caja('Completá cada casillero con los dos alelos (uno de arriba y uno de la izquierda). Abajo se cuentan los genotipos.'), t = '<table class="an-pun"><tr><th></th>' + g1.map(function (a) { return '<th>' + esc(a) + '</th>'; }).join('') + '</tr>';
    g2.forEach(function (b, j) { t += '<tr><th>' + esc(b) + '</th>' + g1.map(function (_, i) { return '<td><input class="an-pun-in" maxlength="6" data-c="' + (j * 2 + i) + '" autocomplete="off"></td>'; }).join('') + '</tr>'; });
    w.innerHTML += t + '</table><div class="an-val">—</div>'; var out = w.querySelector('.an-val');
    w.addEventListener('input', function () { var c = {}, n = 0; [].forEach.call(w.querySelectorAll('.an-pun-in'), function (i) { var v = i.value.trim(); if (!v) return; var k = v.split('').sort(function (a, b) { return a.toLowerCase() === b.toLowerCase() ? (a < b ? -1 : 1) : a.localeCompare(b); }).join(''); c[k] = (c[k] || 0) + 1; n++; }); out.textContent = n ? Object.keys(c).map(function (k) { return k + ': ' + c[k] + ' de 4 (' + c[k] * 25 + ' %)'; }).join(' · ') : '—'; });
    despues(blk, w);
  };

  // 6) ADN / ARN -----------------------------------------------------------------------------------------
  function cadena(blk, arg, arn) { var inp = campoTxt(blk); if (!inp) return; var m = String(arg || 'TACGGA').toUpperCase().replace(/[^ATCG]/g, '').slice(0, 12); if (!m) return; ocultar(inp);
    var bases = arn ? ['A', 'U', 'C', 'G'] : ['A', 'T', 'C', 'G'], col = { A: '#E07A2F', T: '#2a7ab8', U: '#7a3fa0', C: '#3c8d2f', G: '#c2416b' }, arm = [], w = caja('Tocá las bases en orden para armar la cadena ' + (arn ? 'de ARN' : 'complementaria') + ' frente al molde.');
    var vis = mk('div', 'an-adn'), bot = mk('div', 'an-fichas', bases.map(function (b) { return '<button type="button" class="an-base" style="--c:' + col[b] + '" data-b="' + b + '">' + b + '</button>'; }).join('') + '<button type="button" class="an-btn" data-b="x">⌫</button>');
    function pintar() { vis.innerHTML = '<div class="an-fila"><small>molde</small>' + m.split('').map(function (b) { return '<span class="an-b" style="--c:' + col[b] + '">' + b + '</span>'; }).join('') + '</div><div class="an-fila"><small>' + (arn ? 'ARN' : 'nueva') + '</small>' + m.split('').map(function (_, i) { var b = arm[i]; return '<span class="an-b' + (b ? '' : ' vacio') + '" style="--c:' + (b ? col[b] : '#ccc') + '">' + (b || '') + '</span>'; }).join('') + '</div>'; setVal(inp, arm.join('')); }
    bot.addEventListener('click', function (e) { var b = e.target.closest('[data-b]'); if (!b) return; var v = b.getAttribute('data-b'); if (v === 'x') arm.pop(); else if (arm.length < m.length) arm.push(v); sonar('bien'); pintar(); });
    w.appendChild(vis); w.appendChild(bot); pintar(); despues(blk, w); }
  A.adn = function (blk, arg) { cadena(blk, arg, false); }; A.arn = function (blk, arg) { cadena(blk, arg, true); };

  // 7) ÓSMOSIS -------------------------------------------------------------------------------------------
  A.osmosis = function (blk, arg) { var N = d(); if (!N || !N.d) return; var a = String(arg || '0:animal').split(':'), md = N.d.MEDIOS[+a[0] || 0], t = a[1] || 'animal';
    var w = caja('Contá las partículas de sal afuera y adentro de la célula antes de responder.');
    w.innerHTML += N.S(470, 190, N.rc(10, 20, 450, 150, '#EAF6FB', N.C.azul, 12) + N.d.puntos(10, 20, 450, 150, Math.round(md[1] * 2.2), 4) + '<g>' + N.d.celulaOs(235, 95, t, 'normal') + '</g>' + N.d.puntos(205, 70, 60, 50, 6, 5) + N.tx(235, 186, 'Célula ' + t + ' en ' + md[0].toLowerCase(), { a: 'middle', s: 12, w: 800 }));
    despues(blk, w); };

  // 8) MEZCLAS -------------------------------------------------------------------------------------------
  var MET = { filtracion: 'filtro', evaporacion: 'evapora', imantacion: 'iman', decantacion: 'decanta', tamizacion: 'tamiz' };
  A.mezclas = function (blk) { var N = d(); var S = sels(blk); if (!N || !N.d || !N.d.aparato || !S.length) return; propio(blk);
    var w = caja('Tocá un método y después la mezcla. Vas a ver el aparato armado.'), g = mk('div', 'an-cards');
    function pintar() { g.innerHTML = S.map(function (s, k) { var v = s.value, ap = v && MET[norm(v)]; return '<div class="an-card" data-dest="' + k + '"><b>' + esc(filaDe(s)) + '</b>' + (ap ? N.d.aparato(ap, false).replace(/<text[^>]*>[^<]*<\/text>(?=<\/svg>)/, '') : '<div class="an-vacio">¿qué método?</div>') + '<em>' + esc(v || '') + '</em></div>'; }).join(''); }
    w.appendChild(fichas(w, valores(S[0]), function (k, v) { setVal(S[+k], v); pintar(); })); w.appendChild(g); pintar(); despues(blk, w);
  };

  // 9) DENSIDAD ------------------------------------------------------------------------------------------
  A.densidad = function (blk, arg) { var N = d(); if (!N || !N.d) return; var a = String(arg || '120:30').split(':'), m = +a[0] || 120, V = Math.min(40, +a[1] || 30);
    var w = caja('Hacé las dos mediciones y después calculá la densidad.'), vis = mk('div'), fase = 0, b1 = mk('button', 'an-btn', '⚖️ Pesar en la balanza'), b2 = mk('button', 'an-btn', '🧪 Sumergir en la probeta'); b1.type = b2.type = 'button';
    function pintar() { var h = ''; if (fase >= 1) h += '<div class="an-med"><b>Balanza</b>' + N.d.instrumento('balanza', Math.round(m / 50) * 50 === m ? m : m, 1) + '</div>';
      h += '<div class="an-med"><b>Probeta ' + (fase >= 2 ? 'con el objeto' : 'con 40 mL de agua') + '</b>' + N.d.instrumento('probeta', fase >= 2 ? 40 + V : 40, 1) + '</div>'; vis.innerHTML = h; }
    b1.onclick = function () { fase = Math.max(fase, 1); sonar('bien'); pintar(); }; b2.onclick = function () { fase = 2; sonar('bien'); pintar(); };
    w.appendChild(b1); w.appendChild(b2); w.appendChild(vis); pintar(); despues(blk, w); };

  // 10) INSTRUMENTO --------------------------------------------------------------------------------------
  A.instrumento = function (blk, arg) { var N = d(); if (!N || !N.d) return; var a = String(arg || 'termometro:46').split(':'), t = a[0] || 'termometro', v = +a[1] || 0; if (!N.d.INS[t]) return;
    var w = caja('Mirá cuánto vale cada rayita. Con la lupa se agranda.'), box = mk('div', 'an-lupa', N.d.instrumento(t, v, 1)), b = mk('button', 'an-btn', '🔍 Lupa'); b.type = 'button';
    b.onclick = function () { box.classList.toggle('on'); }; w.appendChild(b); w.appendChild(box); despues(blk, w); };

  // 11) ÁTOMO --------------------------------------------------------------------------------------------
  A.atomo = function (blk) { var N = d(); if (!N || !N.d) return; var c = { p: 1, n: 0, e: 1 }, w = caja('Agregá o sacá partículas. El número de protones decide qué elemento es.'), vis = mk('div'), ctl = mk('div', 'an-atctl');
    ctl.innerHTML = [['p', 'Protones'], ['n', 'Neutrones'], ['e', 'Electrones']].map(function (q) { return '<div><b>' + q[1] + '</b><button type="button" class="an-btn" data-k="' + q[0] + '" data-d="-1">−</button><span data-v="' + q[0] + '"></span><button type="button" class="an-btn" data-k="' + q[0] + '" data-d="1">+</button></div>'; }).join('');
    function pintar() { [].forEach.call(ctl.querySelectorAll('[data-v]'), function (s) { s.textContent = c[s.getAttribute('data-v')]; }); var el = N.d.EL[c.p - 1], q = c.p - c.e;
      vis.innerHTML = N.S(470, 245, N.d.bohr(c.p, c.p + c.n, c.e, 9) + N.rc(320, 40, 130, 110, '#fff', N.C.teal, 12) + N.tx(385, 90, el ? el[0] + (q ? (Math.abs(q) > 1 ? Math.abs(q) : '') + (q > 0 ? '+' : '−') : '') : '?', { a: 'middle', s: 34, w: 900 }) + N.tx(385, 118, el ? el[1] : '', { a: 'middle', s: 12, w: 800 }) + N.tx(385, 138, 'A = ' + (c.p + c.n) + (q ? ' · ion' : ' · neutro'), { a: 'middle', s: 11 })); }
    ctl.addEventListener('click', function (e) { var b = e.target.closest('[data-k]'); if (!b) return; var k = b.getAttribute('data-k'); c[k] = Math.max(k === 'p' ? 1 : 0, Math.min(k === 'p' ? 20 : 28, c[k] + +b.getAttribute('data-d'))); sonar('bien'); pintar(); });
    w.appendChild(ctl); w.appendChild(vis); pintar(); despues(blk, w); };

  // 12) TABLA PERIÓDICA ----------------------------------------------------------------------------------
  A.tabla = function (blk) { var N = d(); var inp = campoTxt(blk); if (!N || !N.d || !inp) return; ocultar(inp); var w = caja('Tocá el elemento en la tabla.'), vis = mk('div', '', N.d.tabla(0, null, true)), lab = mk('div', 'an-val', '—');
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-t]'); if (!t) return; var z = +t.getAttribute('data-t'), el = N.d.EL[z - 1]; [].forEach.call(vis.querySelectorAll('[data-t]'), function (x) { x.classList.toggle('nat-sel', x === t); }); lab.textContent = el[0] + ' · ' + el[1]; setVal(inp, el[0]); sonar('bien'); });
    w.appendChild(vis); w.appendChild(lab); despues(blk, w); };

  // 13) BALANCEAR ----------------------------------------------------------------------------------------
  function atomos(f) { var c = {}, re = /([A-Z][a-z]?)(\d*)/g, m; while ((m = re.exec(f))) c[m[1]] = (c[m[1]] || 0) + (+m[2] || 1); return c; }
  function bonita(f) { return f.replace(/\d/g, function (x) { return '₀₁₂₃₄₅₆₇₈₉'[x]; }); }
  A.balancear = function (blk, arg) { var hs = [].slice.call(blk.querySelectorAll('.mt-hueco')), sp = String(arg || '').split('>'); if (sp.length !== 2) return; var re = sp[0].split('+').map(function (x) { return x.trim(); }), pr = sp[1].split('+').map(function (x) { return x.trim(); }), F = re.concat(pr); if (hs.length !== F.length) return;
    var co = F.map(function () { return 1; }), w = caja('Usá + y − en cada coeficiente hasta que los átomos de cada elemento sean iguales a los dos lados.'), ec = mk('div', 'an-ec'), bar = mk('div');
    var p = enun(blk); if (p) ocultar(p);
    function pintar() { ec.innerHTML = F.map(function (f, i) { return (i === re.length ? '<b class="an-flecha">→</b>' : i ? '<b>+</b>' : '') + '<span class="an-co"><button type="button" class="an-btn" data-i="' + i + '" data-d="1">+</button><b>' + co[i] + '</b><button type="button" class="an-btn" data-i="' + i + '" data-d="-1">−</button></span><span class="an-f">' + bonita(f) + '</span>'; }).join('');
      var A1 = {}, A2 = {}; F.forEach(function (f, i) { var a = atomos(f), T = i < re.length ? A1 : A2; Object.keys(a).forEach(function (k) { T[k] = (T[k] || 0) + a[k] * co[i]; }); });
      bar.innerHTML = Object.keys(A1).map(function (k) { var ok = A1[k] === A2[k]; return '<div class="an-at ' + (ok ? 'ok' : '') + '"><b>' + k + '</b><span>' + A1[k] + '</span><i>' + (ok ? '=' : '≠') + '</i><span>' + (A2[k] || 0) + '</span></div>'; }).join('');
      hs.forEach(function (h, i) { setVal(h, String(co[i])); }); }
    ec.addEventListener('click', function (e) { var b = e.target.closest('[data-i]'); if (!b) return; var i = +b.getAttribute('data-i'); co[i] = Math.max(1, Math.min(12, co[i] + +b.getAttribute('data-d'))); sonar('bien'); pintar(); });
    w.appendChild(ec); w.appendChild(bar); pintar(); despues(blk, w); };

  // 14) pH -----------------------------------------------------------------------------------------------
  A.ph = function (blk) { var N = d(); var S = sels(blk); if (!N || !N.d || !S.length) return; propio(blk); var cats = valores(S[0]);
    function zona(c) { var n = norm(c); return /acid/.test(n) ? 0 : /neutr/.test(n) ? 1 : 2; }
    var w = caja('Tocá una sustancia y después la zona de la escala donde va.'), vis = mk('div'), pool = mk('div', 'an-fichas'), elegido = null;
    function pintar() { var b = ''; for (var i = 0; i <= 14; i++) b += N.rc(20 + i * 29, 10, 29, 30, N.d.PCOL[i]) + N.tx(34.5 + i * 29, 56, i, { a: 'middle', s: 10, w: 800 });
      var zs = [[20, 140, 'ÁCIDA (0 a 6)'], [165, 140, 'NEUTRA (7)'], [310, 140, 'BÁSICA (8 a 14)']];
      zs.forEach(function (z, k) { var c = cats.filter(function (x) { return zona(x) === k; })[0]; b += '<g data-dest="' + k + '" class="nat-tap">' + N.rc(z[0], 66, z[1], 130, k === 1 ? '#fafafa' : '#fff', N.C.gris, 8) + '</g>' + N.tx(z[0] + z[1] / 2, 84, z[2], { a: 'middle', s: 11, w: 900 });
        S.filter(function (s) { return s.value === c; }).forEach(function (s, j) { b += N.txw(z[0] + z[1] / 2, 104 + j * 24, filaDe(s), { a: 'middle', s: 10.5, w: 800, c: N.C.teal }, 20); }); });
      vis.innerHTML = N.S(470, 205, b); pool.innerHTML = S.filter(function (s) { return !s.value; }).map(function (s) { var t = filaDe(s); return '<button type="button" class="an-ficha' + (elegido === t ? ' on' : '') + '" data-sp="' + esc(t) + '">' + esc(t) + '</button>'; }).join('') || '<em>Todas ubicadas.</em>'; }
    pool.addEventListener('click', function (e) { var f = e.target.closest('[data-sp]'); if (f) { elegido = f.getAttribute('data-sp'); pintar(); } });
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-dest]'); if (!t || !elegido) return; var k = +t.getAttribute('data-dest'), c = cats.filter(function (x) { return zona(x) === k; })[0], s = selDe(blk, elegido); if (s && c) setVal(s, c); elegido = null; sonar('bien'); pintar(); });
    w.appendChild(pool); w.appendChild(vis); pintar(); despues(blk, w); };

  // 15) OHM ----------------------------------------------------------------------------------------------
  A.ohm = function (blk, arg) { var N = d(); if (!N || !N.d || !N.d.circuito) return; var a = String(arg || 'serie:6:4:2').split(':'), md = a[0] === 'paralelo' ? 'paralelo' : 'serie', v = { V: +a[1] || 6, R1: +a[2] || 4, R2: +a[3] || 2 };
    var w = caja('Mové las perillas y mirá qué marcan el amperímetro y el voltímetro.'), ctl = mk('div', 'an-sim'), vis = mk('div'), med = mk('div', 'an-medidas');
    ctl.innerHTML = [['V', 'Pila (V)', 1.5, 12, 1.5], ['R1', 'R₁ (Ω)', 1, 20, 1], ['R2', 'R₂ (Ω)', 1, 20, 1]].map(function (q) { return '<label><b>' + q[1] + ': <span data-v="' + q[0] + '"></span></b><input type="range" data-k="' + q[0] + '" min="' + q[2] + '" max="' + q[3] + '" step="' + q[4] + '" value="' + v[q[0]] + '"></label>'; }).join('');
    function f2(x) { return String(Math.round(x * 100) / 100).replace('.', ','); }
    function pintar() { [].forEach.call(ctl.querySelectorAll('[data-v]'), function (s) { s.textContent = f2(v[s.getAttribute('data-v')]); }); var c = N.d.circuito(md, v.V, v.R1, v.R2, 1); vis.innerHTML = c.svg;
      med.innerHTML = '<span>🅰️ Amperímetro: <b>' + f2(c.I) + ' A</b></span><span>🆅 Voltímetro en R₁: <b>' + f2(c.V1) + ' V</b></span><span>🆅 Voltímetro en R₂: <b>' + f2(c.V2) + ' V</b></span>'; }
    ctl.addEventListener('input', function (e) { var k = e.target.getAttribute('data-k'); if (!k) return; v[k] = parseFloat(e.target.value); pintar(); });
    w.appendChild(ctl); w.appendChild(vis); w.appendChild(med); pintar(); despues(blk, w); };

  // 16) PISTA --------------------------------------------------------------------------------------------
  A.pista = function (blk, arg) { var N = d(); if (!N) return; var a = String(arg || 'mru:5:0').split(':'), v0 = +a[1] || 0, ac = a[0] === 'mru' ? 0 : +a[2] || 0, t = 0, T = 6, xs = []; for (var k = 0; k <= T; k++) xs.push(v0 * k + ac * k * k / 2);
    var mx0 = Math.max.apply(null, xs) || 1, mx = Math.ceil(mx0 / 10) * 10, w = caja('Tocá ▶ para que pase un segundo. Anotá la posición que marca la cinta.'), vis = mk('div'), b = mk('button', 'an-btn', '▶ Pasar 1 segundo'), r = mk('button', 'an-btn', '↺'), tb = mk('div', 'an-tab'); b.type = r.type = 'button';
    function X(x) { return 30 + x / mx * 400; }
    function pintar() { var s = N.ln(20, 110, 450, 110, N.C.osc, 2); for (var m = 0; m <= 10; m++) { var xx = 30 + m * 40; s += N.ln(xx, 112, xx, 124, N.C.osc, 1.5) + N.tx(xx, 138, String(Math.round(mx / 10 * m * 10) / 10).replace('.', ','), { a: 'middle', s: 9.5 }); }
      for (var k = 0; k <= t; k++) s += N.em(X(xs[k]), 92, '🚗', k === t ? 24 : 12) + (k < t ? N.ci(X(xs[k]), 110, 3, N.C.coral) : '');
      s += N.tx(235, 30, '⏱ ' + t + ' s', { a: 'middle', s: 16, w: 900, c: N.C.coral }) + N.tx(440, 152, 'metros', { a: 'end', s: 10 }); vis.innerHTML = N.S(470, 160, s);
      tb.innerHTML = '<table class="mt-tabla"><tr><th>t (s)</th>' + xs.slice(0, t + 1).map(function (_, k) { return '<td>' + k + '</td>'; }).join('') + '</tr><tr><th>x (m)</th>' + xs.slice(0, t + 1).map(function (x) { return '<td>' + String(Math.round(x * 10) / 10).replace('.', ',') + '</td>'; }).join('') + '</tr></table>'; }
    b.onclick = function () { if (t < T) { t++; sonar('bien'); pintar(); } }; r.onclick = function () { t = 0; pintar(); };
    w.appendChild(vis); w.appendChild(b); w.appendChild(r); w.appendChild(tb); pintar(); despues(blk, w); };

  // 17) DIAGRAMA DE CUERPO LIBRE -------------------------------------------------------------------------
  A.dcl = function (blk) { var N = d(); var cb = [].slice.call(blk.querySelectorAll('.mt-op input[type=checkbox]')); if (!N || !cb.length) return; var w = caja('Marcá las fuerzas que actúan: se dibujan sobre la caja.'), vis = mk('div');
    function dir(t) { var n = norm(t); return /abajo/.test(n) ? [0, 1] : /arriba/.test(n) ? [0, -1] : /izquierda/.test(n) ? [-1, 0] : /derecha/.test(n) ? [1, 0] : null; }
    var cols = ['#c2416b', '#2a7ab8', '#3c8d2f', '#C29A1E', '#7a3fa0', '#E07A2F'];
    function pintar() { var s = N.ln(40, 160, 430, 160, N.C.osc, 3) + N.rc(205, 100, 60, 60, '#FFE0B2', N.C.osc, 4), cx = 235, cy = 130;
      cb.forEach(function (c, k) { if (!c.checked) return; var dd = dir(c.value); if (!dd) return; var x1 = cx + dd[0] * 30, y1 = cy + dd[1] * 30, x2 = x1 + dd[0] * 60, y2 = y1 + dd[1] * 45; s += N.fl(x1, y1, x2, y2, cols[k % 6], 4) + N.tx(x2 + dd[0] * 10, y2 + dd[1] * 14 + 4, c.value.split(' ')[0], { a: dd[0] < 0 ? 'end' : dd[0] > 0 ? 'start' : 'middle', s: 11, w: 900, c: cols[k % 6] }); });
      vis.innerHTML = N.S(470, 240, s); }
    blk.addEventListener('change', function (e) { if (e.target.type === 'checkbox') pintar(); }); w.appendChild(vis); pintar(); despues(blk, w); };

  // 18) GRAFICAR -----------------------------------------------------------------------------------------
  A.graficar = function (blk, arg) { var N = d(); if (!N) return; var p = String(arg || '').split('|'), pts = (p[0] || '').split(';').map(function (q) { var x = q.split(','); return [parseFloat(x[0]), parseFloat(x[1])]; }).filter(function (q) { return isFinite(q[0]) && isFinite(q[1]); }); if (pts.length < 2) return;
    var xl = p[1] || 'x', yl = p[2] || 'y', ys = pts.map(function (q) { return q[1]; }), ymn = Math.min(0, Math.min.apply(null, ys)), ymx = Math.max.apply(null, ys), paso = Math.pow(10, Math.floor(Math.log10((ymx - ymn) / 5 || 1))) * (((ymx - ymn) / Math.pow(10, Math.floor(Math.log10((ymx - ymn) / 5 || 1)))) > 25 ? 5 : 2) || 1;
    ymn = Math.floor(ymn / paso) * paso; ymx = Math.ceil(ymx / paso) * paso; var nY = Math.round((ymx - ymn) / paso), puestos = {}, x0 = 60, y0 = 200, W = 380, Hh = 170;
    var w = caja('Para cada valor de ' + esc(xl) + ', tocá la altura que corresponde según la tabla. Se va trazando la línea.'), vis = mk('div'), lab = mk('div', 'an-val', '');
    function Y(v) { return y0 - (v - ymn) / (ymx - ymn) * Hh; } function Xp(i) { return x0 + (i + 0.5) * W / pts.length; }
    function pintar() { var s = N.ln(x0, y0, x0 + W, y0) + N.ln(x0, y0, x0, y0 - Hh - 6) + N.tx(x0 + W, y0 + 30, xl, { a: 'end', s: 11 }) + N.tx(x0 + 4, y0 - Hh - 10, yl, { s: 11 });
      for (var j = 0; j <= nY; j++) { var v = ymn + j * paso; s += N.ln(x0, Y(v), x0 + W, Y(v), '#eee', 1) + N.tx(x0 - 6, Y(v) + 4, String(Math.round(v * 100) / 100).replace('.', ','), { a: 'end', s: 9.5 }); }
      pts.forEach(function (q, i) { s += N.tx(Xp(i), y0 + 14, String(q[0]).replace('.', ','), { a: 'middle', s: 10 }); for (var j = 0; j <= nY; j++) s += '<circle cx="' + N.r1(Xp(i)) + '" cy="' + N.r1(Y(ymn + j * paso)) + '" r="7" class="an-g-p" data-dest="' + i + ':' + j + '"/>'; });
      var L = pts.map(function (_, i) { return puestos[i] != null ? N.r1(Xp(i)) + ',' + N.r1(Y(ymn + puestos[i] * paso)) : null; }).filter(Boolean); if (L.length > 1) s += '<polyline points="' + L.join(' ') + '" fill="none" stroke="' + N.C.teal + '" stroke-width="3"/>';
      pts.forEach(function (q, i) { if (puestos[i] == null) return; var ok = Math.abs(ymn + puestos[i] * paso - q[1]) < paso / 2; s += N.ci(Xp(i), Y(ymn + puestos[i] * paso), 6, ok ? N.C.teal : N.C.coral); });
      vis.innerHTML = N.S(470, 240, s); var bien = pts.filter(function (q, i) { return puestos[i] != null && Math.abs(ymn + puestos[i] * paso - q[1]) < paso / 2; }).length; lab.textContent = Object.keys(puestos).length ? bien + ' de ' + pts.length + ' puntos coinciden con la tabla' : ''; }
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-dest]'); if (!t) return; var q = t.getAttribute('data-dest').split(':'); puestos[+q[0]] = +q[1]; sonar('bien'); pintar(); });
    w.appendChild(vis); w.appendChild(lab); pintar(); despues(blk, w); };

  // 19) EXPERIMENTO --------------------------------------------------------------------------------------
  A.experimento = function (blk) { var S = sels(blk); if (!S.length) return; propio(blk); var cats = valores(S[0]), w = caja('Tocá cada condición y después dónde va: lo que cambia, lo que se mide o lo que queda igual.'), pool = mk('div', 'an-fichas'), mesa = mk('div', 'an-mesa'), elegido = null;
    function tipo(c) { var n = norm(c); return /camb|indep/.test(n) ? 0 : /mide|depen/.test(n) ? 1 : 2; }
    function pintar() { var g = [[], [], []]; S.forEach(function (s) { if (s.value) g[tipo(s.value)].push(filaDe(s)); });
      mesa.innerHTML = cats.map(function (c) { var k = tipo(c); return '<div class="an-zona z' + k + '" data-dest="' + esc(c) + '"><b>' + (k === 0 ? '🔀 ' : k === 1 ? '📏 ' : '🟰 ') + esc(c) + '</b>' + g[k].map(function (t) { return '<span>' + esc(t) + '</span>'; }).join('') + '</div>'; }).join('') +
        '<div class="an-montajes"><div><b>Montaje A</b>' + g[2].map(function (t) { return '<span>🟰 ' + esc(t) + '</span>'; }).join('') + g[0].map(function (t) { return '<span class="cambia">🔀 ' + esc(t) + ': versión A</span>'; }).join('') + g[1].map(function (t) { return '<span>📏 medimos ' + esc(t) + '</span>'; }).join('') + '</div><div><b>Montaje B (control)</b>' + g[2].map(function (t) { return '<span>🟰 ' + esc(t) + '</span>'; }).join('') + g[0].map(function (t) { return '<span class="cambia">🔀 ' + esc(t) + ': versión B</span>'; }).join('') + g[1].map(function (t) { return '<span>📏 medimos ' + esc(t) + '</span>'; }).join('') + '</div></div>';
      pool.innerHTML = S.filter(function (s) { return !s.value; }).map(function (s) { var t = filaDe(s); return '<button type="button" class="an-ficha' + (elegido === t ? ' on' : '') + '" data-sp="' + esc(t) + '">' + esc(t) + '</button>'; }).join('') || '<em>Todo ubicado.</em>'; }
    pool.addEventListener('click', function (e) { var f = e.target.closest('[data-sp]'); if (f) { elegido = f.getAttribute('data-sp'); pintar(); } });
    mesa.addEventListener('click', function (e) { var z = e.target.closest('[data-dest]'); if (!z) return; if (!elegido) { var sp = e.target.closest('span'); if (sp && z.contains(sp)) { var s0 = selDe(blk, sp.textContent); if (s0) setVal(s0, ''); pintar(); } return; } var s = selDe(blk, elegido); if (s) setVal(s, z.getAttribute('data-dest')); elegido = null; sonar('bien'); pintar(); });
    w.appendChild(pool); w.appendChild(mesa); pintar(); despues(blk, w); };

  // 20) LUNA ---------------------------------------------------------------------------------------------
  A.luna = function (blk) { var N = d(); var S = sels(blk); if (!N || !S.length) return; propio(blk); var w = caja('Tocá una fase y después la posición de la Luna en la órbita (el Sol está a la izquierda).'), vis = mk('div');
    var pos = [[150, 120], [235, 205], [320, 120], [235, 35]];
    function pintar() { var s = N.em(28, 120, '☀️', 34) + N.fl(52, 70, 90, 70, '#F5D33B', 2) + N.fl(52, 170, 90, 170, '#F5D33B', 2) + N.ci(235, 120, 85, 'none', '#ccc', ' stroke-dasharray="4 4"') + N.ci(235, 120, 24, '#4FC3F7', N.C.osc) + N.tx(235, 124, 'Tierra', { a: 'middle', s: 9, w: 800 });
      S.forEach(function (sl, k) { var q = pos[(+filaDe(sl) || k + 1) - 1] || pos[k % 4]; s += '<g data-dest="' + k + '" class="nat-tap">' + N.ci(q[0], q[1], 14, '#37474F', N.C.osc) + '<path d="M' + q[0] + ',' + (q[1] - 14) + ' A14,14 0 0 0 ' + q[0] + ',' + (q[1] + 14) + ' Z" fill="#FFF8E1"/>' + N.ci(q[0] + 16, q[1] - 16, 9, '#fff', N.C.osc) + N.tx(q[0] + 16, q[1] - 12, filaDe(sl), { a: 'middle', s: 10, w: 900 }) + '</g>' + (sl.value ? N.txw(q[0] + (q[0] > 300 ? 22 : q[0] < 170 ? -22 : 0), q[1] + (q[1] > 150 ? 30 : q[1] < 60 ? -20 : 0), sl.value, { a: q[0] > 300 ? 'start' : q[0] < 170 ? 'end' : 'middle', s: 11, w: 800, c: N.C.teal }, 12) : ''); });
      vis.innerHTML = N.S(470, 245, s); }
    w.appendChild(fichas(w, valores(S[0]), function (k, v) { setVal(S[+k], v); pintar(); })); w.appendChild(vis); pintar(); despues(blk, w); };

  // 21) PLATO --------------------------------------------------------------------------------------------
  A.plato = function (blk) { var N = d(); var S = sels(blk); if (!N || !S.length) return; propio(blk); var cats = valores(S[0]), cols = ['#5BAA3C', '#F2A541', '#8FB8E3', '#c2416b', '#C29A1E', '#9E9E9E'], w = caja('Tocá un alimento y después el sector del plato donde va.'), pool = mk('div', 'an-fichas'), vis = mk('div'), elegido = null;
    function pintar() { var n = cats.length, s = N.ci(235, 135, 120, '#fff', N.C.gris), a0 = -Math.PI / 2;
      cats.forEach(function (c, k) { var a1 = a0 + 2 * Math.PI / n, am = (a0 + a1) / 2, big = 0; s += '<g data-dest="' + k + '" class="nat-tap"><path d="M235,135 L' + N.r1(235 + 112 * Math.cos(a0)) + ',' + N.r1(135 + 112 * Math.sin(a0)) + ' A112,112 0 ' + big + ' 1 ' + N.r1(235 + 112 * Math.cos(a1)) + ',' + N.r1(135 + 112 * Math.sin(a1)) + ' Z" fill="' + cols[k % 6] + '" fill-opacity=".28" stroke="#fff" stroke-width="3"/></g>';
        var lx = 235 + 70 * Math.cos(am), ly = 135 + 70 * Math.sin(am); s += N.txw(lx, ly - 8, c.replace(/,.*$/, ''), { a: 'middle', s: 9.5, w: 900, c: N.C.osc }, 14);
        S.filter(function (sl) { return sl.value === c; }).forEach(function (sl, j) { s += N.tx(lx, ly + 14 + j * 12, filaDe(sl), { a: 'middle', s: 9.5, c: N.C.teal, w: 800 }); }); a0 = a1; });
      vis.innerHTML = N.S(470, 270, s); pool.innerHTML = S.filter(function (sl) { return !sl.value; }).map(function (sl) { var t = filaDe(sl); return '<button type="button" class="an-ficha' + (elegido === t ? ' on' : '') + '" data-sp="' + esc(t) + '">' + esc(t) + '</button>'; }).join('') || '<em>Plato completo.</em>'; }
    pool.addEventListener('click', function (e) { var f = e.target.closest('[data-sp]'); if (f) { elegido = f.getAttribute('data-sp'); pintar(); } });
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-dest]'); if (!t || !elegido) return; var sl = selDe(blk, elegido); if (sl) setVal(sl, cats[+t.getAttribute('data-dest')]); elegido = null; sonar('bien'); pintar(); });
    w.appendChild(pool); w.appendChild(vis); pintar(); despues(blk, w); };

  // ---------- Recorrido de la página ----------
  function quitar(root) { var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), n, L = []; while ((n = tw.nextNode())) if (n.nodeValue.indexOf('[[') >= 0) L.push(n); L.forEach(function (x) { RE.lastIndex = 0; x.nodeValue = x.nodeValue.replace(RE, ''); }); RE.lastIndex = 0; }
  function recorrer() {
    [].forEach.call(document.querySelectorAll('.wvp.act .mt-preg:not([data-anat])'), function (blk) {
      var tx = blk.textContent || '', re = new RegExp(RE.source, 'g'), m = re.exec(tx); if (!m) return; blk.setAttribute('data-anat', '1');
      quitar(blk); var tp = blk.querySelector('.mt-tipo'), nm = NOMBRE[m[1]]; if (tp && nm) tp.innerHTML = '<span aria-hidden="true">' + nm[0] + '</span> ' + esc(nm[1]);
      try { A[m[1]](blk, m[2]); } catch (e) { if (window.console) console.warn('Actividad de Naturales', m[1], e); }
    });
    [].forEach.call(document.querySelectorAll('.wvp'), function (v) { if ((v.textContent || '').indexOf('[[') >= 0) quitar(v); });
  }
  var css = document.createElement('style');
  css.textContent = [
    '.an-oculto{position:absolute!important;width:1px!important;height:1px!important;opacity:0!important;pointer-events:none!important;overflow:hidden!important}',
    '.an-caja{margin:8px 0 6px;padding:12px;border:2px solid #E3ECEA;border-radius:18px;background:#fff;text-align:center}.an-caja .mt-ayuda{display:block;text-align:left;margin-bottom:6px}',
    '.an-fichas{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:8px 0}.an-fichas em{color:#066A6E;font-weight:700}',
    '.an-ficha,.an-btn{padding:8px 14px;border:2px solid #E3ECEA;border-bottom-width:4px;border-radius:14px;background:#fff;font:inherit;font-weight:800;cursor:pointer;color:#253638}.an-ficha.on{border-color:#087E83;background:#D7F0E9}.an-btn{margin:4px}',
    '.an-val{margin-top:8px;font-weight:800;font-size:1.05rem;color:#066A6E}',
    '.an-cl-paso{margin:4px 0;padding:6px 10px;border-radius:10px;background:#F3FBF7;text-align:left}.an-cl-q{margin:8px 0;padding:12px;border:2px solid #087E83;border-radius:14px;font-weight:800}.an-cl-fin{margin:10px 0;padding:12px;border-radius:14px;background:#FFF3C4;font-size:1.05rem}',
    '.an-pun{margin:6px auto;border-collapse:collapse}.an-pun th{padding:6px 12px;font-size:1.1rem;color:#7a3fa0}.an-pun td{border:2px solid #087E83;padding:4px}.an-pun-in{width:70px;padding:10px;font:inherit;font-weight:900;font-size:1.1rem;text-align:center;border:0}',
    '.an-adn .an-fila{display:flex;gap:6px;justify-content:center;align-items:center;margin:6px 0}.an-adn small{width:44px;font-weight:800;color:#066A6E}.an-b{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:8px;background:var(--c);color:#fff;font-weight:900}.an-b.vacio{background:#fff;border:2px dashed #ccc}',
    '.an-base{width:52px;height:52px;border-radius:12px;border:0;background:var(--c);color:#fff;font:inherit;font-weight:900;font-size:1.3rem;cursor:pointer}',
    '.an-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}.an-card{padding:8px;border:2px solid #E3ECEA;border-radius:14px;cursor:pointer}.an-card:hover{border-color:#087E83}.an-card em{display:block;font-weight:800;color:#066A6E}.an-card svg{max-width:180px}.an-vacio{padding:30px 0;color:#9aa}',
    '.an-med{display:block;max-width:420px;margin:6px auto}.an-lupa{overflow:auto;max-height:360px}.an-lupa.on svg{max-width:none;width:940px}',
    '.an-atctl{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}.an-atctl div{display:flex;align-items:center;gap:4px}.an-atctl span{min-width:26px;font-weight:900;font-size:1.1rem}',
    '.an-ec{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;align-items:center;font-size:1.25rem}.an-co{display:inline-flex;flex-direction:column;align-items:center}.an-co .an-btn{padding:0 10px;margin:1px}.an-f{font-weight:900}.an-flecha{color:#087E83}',
    '.an-at{display:inline-flex;gap:8px;align-items:center;margin:4px;padding:6px 12px;border-radius:12px;background:#FCE4EC;font-weight:800}.an-at.ok{background:#D7F0E9}',
    '.an-sim{text-align:left}.an-sim label{display:block}.an-sim input{width:100%;accent-color:#087E83}.an-medidas{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;font-weight:700}.an-medidas b{color:#C2552E}',
    '.an-tab{overflow-x:auto}.an-g-p{fill:#e7f1ef;cursor:pointer}.an-g-p:hover{fill:rgba(8,126,131,.35)}',
    '.an-mesa{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px}.an-zona{min-height:80px;padding:8px;border:2px dashed #9dbdb9;border-radius:14px;cursor:pointer}.an-zona span,.an-montajes span{display:block;margin:4px 0;padding:4px 8px;border-radius:8px;background:#F3FBF7;font-weight:700}',
    '.an-montajes{grid-column:1/-1;display:grid;grid-template-columns:1fr 1fr;gap:8px;text-align:left}.an-montajes>div{padding:8px;border:2px solid #E3ECEA;border-radius:14px}.an-montajes .cambia{background:#FFF3C4}'
  ].join('');
  document.head.appendChild(css);
  var pend = false;
  function prog() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; try { recorrer(); } catch (e) {} }); }
  function iniciar() { new MutationObserver(prog).observe(document.body, { childList: true, subtree: true }); prog(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
