/* ACTIVIDADES DE SOCIALES (banco de ACTIVIDADES; solo actividades de nivel y generales, nunca examen).
   Mismo mecanismo que js/actividades-plus.js y js/actividades-nat.js: una marca al principio del enunciado cambia la pantalla y lo que arma
   el alumno se escribe en el campo del tipo de siempre (la corrección no cambia). Los dibujos se reusan del banco de la lección (H.nat.soc).
     [[cronologia]]                      ordering (hechos con su año entre paréntesis: "Revolución de Mayo (1810)") · ubica los hechos en la línea
     [[coordenadas]]                     short_answer (nombre de la ciudad)            · toca la ciudad en la grilla de latitud y longitud
     [[escala:1000000:6]]                numeric                                        · mide con la regla en el mapa y calcula
     [[husos:-3:9:10]]                   numeric (hora de 0 a 23)                       · gira la aguja del reloj de la otra ciudad (UTC origen : UTC destino : hora)
     [[piramide:0]]                      multiple_choice                                · lee la pirámide (0 joven, 1 adulta, 2 envejecida)
     [[fuente]]                          matching (izquierda: Autor, Fecha, Intención, Tipo) · analiza el documento del enunciado con fichas
     [[arbol:Revolución de Mayo]]        classify (Causa / Consecuencia)                · arma el árbol del proceso
     [[dhondt:42000,31000,15000:5]]      fill_blank (un ___ por partido)                · marca los cocientes más grandes de la tabla
     [[ley]]                             ordering (etapas de la ley)                    · lleva el proyecto por el Congreso
     [[poderes]]                         classify (Ejecutivo / Legislativo / Judicial)  · ubica cada institución en su edificio
     [[sectores]]                        classify (Primario / Secundario / Terciario)   · ubica cada actividad en el campo, la fábrica o el comercio
     [[mercado:100,1:0,1]]               numeric                                        · mueve el precio hasta el equilibrio (Qd = a − b·p ; Qo = c + d·p)
     [[carrito]]                         numeric                                        · arma la canasta y compara precios (enunciado con "producto $viejo $nuevo; …")
     [[balanza]]                         classify (A favor / En contra)                 · los argumentos inclinan la balanza
     [[dilema]]                          open o keywords                                · elige postura y la justifica desde una mirada ética
     [[chequeo]]                         multi_select (señales de alerta)               · revisa la publicación con la lista de verificación
     [[sociedad:feudal]]                 ordering (grupos)                              · arma la pirámide social de arriba hacia abajo
     [[comparativa]]                     table_fill                                     · completa la tabla comparativa con encabezados ilustrados
     [[climograma:0]]                    numeric                                        · toca cada mes del climograma para leer temperatura y lluvia (0 Buenos Aires, 1 Ushuaia, 2 Manaos, 3 Mendoza)
     [[placas]]                          classify (Convergente / Divergente / Transformante) · ubica cada caso en el dibujo de su borde
     [[cuenca]]                          matching (izquierda: partes; opciones "1" a "7")  · toca la parte y después el número en el mapa del río
     [[argumento]]                       classify (Premisa / Conclusión)                · arma el esquema: premisas arriba, conclusión abajo
     [[falacia]]                         multiple_choice (nombres de falacias)          · el diálogo del enunciado como chat; la elegida queda como sello
     [[constitucion]]                    classify (ej. Derecho / Garantía, o Primera parte / Segunda parte) · ubica cada artículo en las páginas
     [[periodos:Colonia:Después de 1810]] classify (Cambio / Continuidad)               · puente entre los dos períodos
     [[bioma]]                           classify (nombres de biomas: Selva, Desierto, Pastizal, Bosque templado, Estepa, Tundra) · cada uno a su paisaje */
(function () {
  'use strict';
  var RE = /\[\[(cronologia|coordenadas|escala|husos|piramide|fuente|arbol|dhondt|ley|poderes|sectores|mercado|carrito|balanza|dilema|chequeo|sociedad|comparativa|climograma|placas|cuenca|argumento|falacia|constitucion|periodos|bioma)(?::([^\]]*))?\]\]\s*/g;
  var NOMBRE = { cronologia: ['🕰️', 'Ubicá en la línea de tiempo'], coordenadas: ['🌐', 'Encontrá el lugar'], escala: ['📏', 'Medí con la escala'], husos: ['🕒', '¿Qué hora es allá?'], piramide: ['👥', 'Leé la pirámide de población'], fuente: ['🔎', 'Detective de fuentes'],
    arbol: ['🌳', 'Árbol de causas y consecuencias'], dhondt: ['🗳️', 'Repartí las bancas'], ley: ['🏛️', 'El camino de una ley'], poderes: ['⚖️', 'Los tres poderes'], sectores: ['🏭', 'Sectores de la economía'], mercado: ['📈', 'Encontrá el equilibrio'], carrito: ['🛒', 'El carrito de la inflación'],
    balanza: ['⚖️', 'Balanza de argumentos'], dilema: ['🤔', 'Dilema ético'], chequeo: ['📰', 'Chequeá la noticia'], sociedad: ['🔺', 'Armá la pirámide social'], comparativa: ['📊', 'Tabla comparativa'], climograma: ['🌦️', 'Leé el climograma'], placas: ['🌋', 'Bordes de placas'], cuenca: ['🏞️', 'Partes de la cuenca'], argumento: ['🧩', 'Armá el argumento'], falacia: ['🪤', 'Cazá la falacia'], constitucion: ['📜', 'La Constitución'], periodos: ['🔁', 'Cambios y continuidades'], bioma: ['🌍', 'Cada uno en su bioma'] };
  var A = {};
  function N() { return window.WaveLeccionBanco && WaveLeccionBanco._h && WaveLeccionBanco._h.nat; }
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
  function propio(blk) { [].forEach.call(blk.querySelectorAll('.ap2-uni,.ap2-pool2,.ap2-cajas,.ap2-banco'), function (x) { x.remove(); }); var m = mk('i', 'ap2-banco'); m.hidden = true; blk.appendChild(m); [].forEach.call(blk.querySelectorAll('.mt-pares'), ocultar); }
  function caja(ayuda) { return mk('div', 'an-caja', ayuda ? '<small class="mt-ayuda">' + ayuda + '</small>' : ''); }
  // Clasificar tocando: zonas = [{c: categoría, html}] ; pinta las fichas sin ubicar y las ubicadas dentro de su zona
  function clasificar(blk, w, zonasHtml, alPintar) { var S = sels(blk), cats = valores(S[0]), pool = mk('div', 'an-fichas'), zon = mk('div', 'soa-zonas'), elegido = null;
    function pintar() { zon.innerHTML = cats.map(function (c, k) { return '<div class="soa-zona" data-dest="' + esc(c) + '">' + (zonasHtml ? zonasHtml(c, k) : '<b>' + esc(c) + '</b>') + '<div class="soa-dentro">' + S.filter(function (s) { return s.value === c; }).map(function (s) { return '<span data-quitar="' + esc(filaDe(s)) + '">' + esc(filaDe(s)) + '</span>'; }).join('') + '</div></div>'; }).join('');
      pool.innerHTML = S.filter(function (s) { return !s.value; }).map(function (s) { var t = filaDe(s); return '<button type="button" class="an-ficha' + (elegido === t ? ' on' : '') + '" data-sp="' + esc(t) + '">' + esc(t) + '</button>'; }).join('') || '<em>Todo ubicado. Tocá una ficha ubicada para devolverla.</em>'; if (alPintar) alPintar(S, cats); }
    pool.addEventListener('click', function (e) { var f = e.target.closest('[data-sp]'); if (f) { elegido = f.getAttribute('data-sp'); pintar(); } });
    zon.addEventListener('click', function (e) { var q = e.target.closest('[data-quitar]'); if (q && !elegido) { var s0 = selDe(blk, q.getAttribute('data-quitar')); if (s0) setVal(s0, ''); pintar(); return; } var z = e.target.closest('[data-dest]'); if (!z || !elegido) return; var s = selDe(blk, elegido); if (s) setVal(s, z.getAttribute('data-dest')); elegido = null; sonar('bien'); pintar(); });
    w.appendChild(pool); w.appendChild(zon); pintar(); return pintar; }
  // Ordenar tocando sobre un dibujo: posiciones = función(k) → [x, y]; dibujo(ordenTocado) devuelve el svg con [data-dest=k]
  function ordenarDib(blk, w, dibujo) { var ol = blk.querySelector('ol.mt-orden'); if (!ol) return; var lis = [].slice.call(ol.children), orden = []; ocultar(ol); var ay = blk.querySelector('.mt-ayuda'); if (ay) ocultar(ay);
    var vis = mk('div'), bt = mk('button', 'an-btn', '↺ Volver a empezar'); bt.type = 'button';
    function pintar() { vis.innerHTML = dibujo(lis.map(function (li) { return li.getAttribute('data-v'); }), orden); orden.map(function (k) { return lis[k]; }).concat(lis.filter(function (_, k) { return orden.indexOf(k) < 0; })).forEach(function (li) { ol.appendChild(li); }); fire(ol); }
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-dest]'); if (!t) return; var k = +t.getAttribute('data-dest'); if (orden.indexOf(k) >= 0) return; orden.push(k); sonar('bien'); pintar(); });
    bt.addEventListener('click', function () { orden = []; pintar(); }); w.appendChild(vis); w.appendChild(bt); pintar(); }

  // 1) CRONOLOGÍA ----------------------------------------------------------------------------------------
  A.cronologia = function (blk) { var n = N(); if (!n) return; var w = caja('Tocá los hechos del más antiguo al más reciente: cada uno se ubica en la línea en su año.');
    ordenarDib(blk, w, function (L, orden) { var anios = L.map(function (t) { var m = /\((-?\d+)(\s*a\.?\s*C\.?)?\)/.exec(t); return m ? (m[2] ? -Math.abs(+m[1]) : +m[1]) : null; }), val = anios.filter(function (a) { return a != null; }), mn = Math.min.apply(null, val.concat([0])), mx = Math.max.apply(null, val.concat([1]));
      if (val.length) { mn = Math.min.apply(null, val); mx = Math.max.apply(null, val); } var pad = (mx - mn) * 0.1 + 5; mn -= pad; mx += pad; var X = function (a) { return 30 + (a - mn) / (mx - mn || 1) * 410; };
      var s = n.ln(20, 150, 450, 150, n.C.osc, 3); orden.forEach(function (k, i) { var a = anios[k], x = a != null ? X(a) : 30 + i * 60, y = 130 - (i % 3) * 34; s += n.ln(x, y + 6, x, 150, n.C.teal, 1.5) + n.ci(x, 150, 5, n.C.coral) + n.tx(x, y, (i + 1) + '. ' + L[k].replace(/\s*\(.*\)\s*$/, '').slice(0, 26), { a: x > 350 ? 'end' : x < 120 ? 'start' : 'middle', s: 10, w: 800 }) + (a != null ? n.tx(x, 168, a < 0 ? -a + ' a. C.' : a, { a: 'middle', s: 9.5, c: n.C.coral, w: 800 }) : ''); });
      var chips = L.map(function (t, k) { return orden.indexOf(k) >= 0 ? '' : '<g data-dest="' + k + '" class="nat-tap">' + n.rc(10 + (k % 3) * 153, 180 + Math.floor(k / 3) * 34, 147, 28, '#fff', n.C.teal, 10) + n.tx(83 + (k % 3) * 153, 198 + Math.floor(k / 3) * 34, t.length > 26 ? t.slice(0, 25) + '…' : t, { a: 'middle', s: 9.5, w: 800 }) + '</g>'; }).join('');
      return n.S(470, 190 + Math.ceil(L.length / 3) * 34, s + chips); }); despues(blk, w); };

  // 2) COORDENADAS ---------------------------------------------------------------------------------------
  A.coordenadas = function (blk) { var n = N(); var inp = campoTxt(blk); if (!n || !n.soc || !inp) return; ocultar(inp); var w = caja('Tocá el punto de la ciudad en la grilla.'), vis = mk('div', '', n.soc.grilla(2, null, true)), lab = mk('div', 'an-val', '—');
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-t]'); if (!t) return; var c = n.soc.CIU[+t.getAttribute('data-t')]; [].forEach.call(vis.querySelectorAll('[data-t]'), function (x) { x.classList.toggle('nat-sel', x === t); }); lab.textContent = c[0]; setVal(inp, c[0]); sonar('bien'); });
    w.appendChild(vis); w.appendChild(lab); despues(blk, w); };

  // 3) ESCALA --------------------------------------------------------------------------------------------
  A.escala = function (blk, arg) { var n = N(); if (!n || !n.soc) return; var a = String(arg || '1000000:6').split(':'), e = +a[0] || 1000000, cm = Math.min(10, Math.max(1, +a[1] || 6)), w = caja('Usá la regla: tocá «Poner la regla» y leé cuántos cm hay entre A y B. Después calculá.'), vis = mk('div'), b = mk('button', 'an-btn', '📏 Poner la regla'), con = false; b.type = 'button';
    function pintar() { vis.innerHTML = n.soc.mapaEsc(cm, e, con ? 1 : 0); } b.onclick = function () { con = !con; b.textContent = con ? '📏 Sacar la regla' : '📏 Poner la regla'; pintar(); }; w.appendChild(b); w.appendChild(vis); pintar(); despues(blk, w); };

  // 4) HUSOS ---------------------------------------------------------------------------------------------
  A.husos = function (blk, arg) { var n = N(); var inp = campoNum(blk); if (!n || !n.soc || !inp) return; var a = String(arg || '-3:9:10').split(':'), u1 = +a[0], u2 = +a[1], h1 = +a[2] || 0, h = 12, w = caja('Mové la aguja del reloj de la derecha hasta la hora que corresponde (diferencia de husos: ' + (u2 - u1 >= 0 ? '+' : '') + (u2 - u1) + ' h).'), vis = mk('div'), bot = mk('div', 'an-fichas', '<button type="button" class="an-btn" data-d="-1">− 1 h</button><button type="button" class="an-btn" data-d="1">+ 1 h</button>'); ocultar(inp.closest('.nu-fila') || inp);
    function pintar() { vis.innerHTML = n.S(470, 140, n.soc.reloj(130, 50, h1, 'UTC ' + (u1 >= 0 ? '+' : '') + u1) + n.soc.reloj(340, 50, h, 'UTC ' + (u2 >= 0 ? '+' : '') + u2)); setVal(inp, String(h)); }
    bot.addEventListener('click', function (e) { var b = e.target.closest('[data-d]'); if (!b) return; h = (h + +b.getAttribute('data-d') + 24) % 24; sonar('bien'); pintar(); }); w.appendChild(vis); w.appendChild(bot); pintar(); despues(blk, w); };

  // 5) PIRÁMIDE ------------------------------------------------------------------------------------------
  A.piramide = function (blk, arg) { var n = N(); if (!n || !n.soc) return; var P = n.soc.PIR[+arg || 0] || n.soc.PIR[0], w = caja('Mirá la base, el centro y la cima. Tocá cada franja para ver su porcentaje.'), vis = mk('div', '', n.soc.piramide(P, 6)), lab = mk('div', 'an-val', '—'), EDAD = ['0-14', '15-29', '30-44', '45-59', '60-74', '75+'];
    vis.addEventListener('click', function (e) { var r = vis.querySelector('svg').getBoundingClientRect(), y = (e.clientY - r.top) / r.height * 222, i = Math.floor((196 - y) / 30); if (i < 0 || i > 5) return; var g = P[1][i]; lab.textContent = EDAD[i] + ' años: ' + g[0] + ' % varones y ' + g[1] + ' % mujeres'; });
    w.appendChild(vis); w.appendChild(lab); despues(blk, w); };

  // 6) FUENTE --------------------------------------------------------------------------------------------
  A.fuente = function (blk) { var S = sels(blk); if (!S.length) return; propio(blk); var p = enun(blk), txt = p ? p.innerHTML : '', w = caja('Leé el documento. Tocá una ficha y después el casillero de la ficha de análisis.'), doc = mk('div', 'soc-doc viejo', txt), ficha = mk('div', 'soa-ficha'), elegido = null, opts = valores(S[0]);
    if (p) p.innerHTML = '<b>Analizá esta fuente:</b>';
    var pool = mk('div', 'an-fichas'); function pintar() { pool.innerHTML = opts.map(function (o) { var usada = S.some(function (s) { return s.value === o; }); return '<button type="button" class="an-ficha' + (elegido === o ? ' on' : '') + (usada ? ' usada' : '') + '" data-o="' + esc(o) + '">' + esc(o) + '</button>'; }).join('');
      ficha.innerHTML = '<b>🔎 Ficha de análisis</b>' + S.map(function (s, k) { return '<div class="soa-campo" data-k="' + k + '"><span>' + esc(filaDe(s)) + ':</span><em>' + (s.value ? esc(s.value) : '…') + '</em></div>'; }).join(''); }
    pool.addEventListener('click', function (e) { var f = e.target.closest('[data-o]'); if (f) { elegido = f.getAttribute('data-o'); pintar(); } });
    ficha.addEventListener('click', function (e) { var c = e.target.closest('[data-k]'); if (!c || !elegido) return; setVal(S[+c.getAttribute('data-k')], elegido); elegido = null; sonar('bien'); pintar(); });
    w.appendChild(doc); w.appendChild(pool); w.appendChild(ficha); pintar(); despues(blk, w); };

  // 7) CAUSAS --------------------------------------------------------------------------------------------
  A.arbol = function (blk, arg) { if (!sels(blk).length) return; propio(blk); var w = caja('Tocá cada tarjeta y ubicala arriba (causas) o abajo (consecuencias) del proceso.');
    w.appendChild(mk('div', 'soa-proceso', esc(arg || 'El proceso')));
    clasificar(blk, w, function (c) { return '<b>' + (/cons/i.test(c) ? '⬇️ ' : '⬆️ ') + esc(c) + '</b>'; }); var z = w.querySelector('.soa-zonas'); if (z) { z.classList.add('arbol'); w.insertBefore(z, w.querySelector('.soa-proceso')); } despues(blk, w); };

  // 8) D'HONDT -------------------------------------------------------------------------------------------
  A.dhondt = function (blk, arg) { var hs = [].slice.call(blk.querySelectorAll('.mt-hueco')), a = String(arg || '').split(':'), V = (a[0] || '').split(',').map(Number).filter(function (x) { return x > 0; }), nb = +a[1] || 5; if (!V.length || hs.length !== V.length) return; hs.forEach(function (h) { h.readOnly = true; });
    var marc = {}, w = caja('Marcá en la tabla los ' + nb + ' cocientes más grandes: cada uno es una banca.'), tab = mk('div', 'an-tab'), lab = mk('div', 'an-val'), col = ['#c2416b', '#2a7ab8', '#3c8d2f', '#C29A1E', '#7a3fa0'];
    function pintar() { var h = '<table class="soa-dh"><tr><th></th>' + Array.apply(null, Array(nb)).map(function (_, d) { return '<th>÷' + (d + 1) + '</th>'; }).join('') + '</tr>';
      V.forEach(function (v, i) { h += '<tr><th style="color:' + col[i % 5] + '">' + String.fromCharCode(65 + i) + '</th>' + Array.apply(null, Array(nb)).map(function (_, d) { var k = i + '-' + d; return '<td data-k="' + k + '" class="' + (marc[k] ? 'on' : '') + '" style="--c:' + col[i % 5] + '">' + Math.round(v / (d + 1)).toLocaleString('es-AR') + '</td>'; }).join('') + '</tr>'; });
      tab.innerHTML = h + '</table>'; var n = Object.keys(marc).length; lab.textContent = n + ' de ' + nb + ' bancas marcadas'; V.forEach(function (_, i) { setVal(hs[i], String(Object.keys(marc).filter(function (k) { return +k.split('-')[0] === i; }).length)); }); }
    tab.addEventListener('click', function (e) { var c = e.target.closest('[data-k]'); if (!c) return; var k = c.getAttribute('data-k'); if (marc[k]) delete marc[k]; else if (Object.keys(marc).length < nb) marc[k] = 1; sonar('bien'); pintar(); });
    w.appendChild(tab); w.appendChild(lab); pintar(); despues(blk, w); };

  // 9) LEY -----------------------------------------------------------------------------------------------
  A.ley = function (blk) { var n = N(); if (!n || !n.soc) return; var w = caja('Tocá las etapas en orden: el proyecto avanza por el Congreso.'), P = n.soc.LEY;
    ordenarDib(blk, w, function (L, orden) { var s = n.rc(150, 20, 170, 76, '#F3FBF7', n.C.gris, 14) + n.tx(235, 36, 'Congreso de la Nación', { a: 'middle', s: 10, w: 900, c: n.C.teal });
      L.forEach(function (t, k) { var q = P[k] || [t, '', '📍', 60 + k * 70, 120], i = orden.indexOf(k), x = P[k] ? P[k][3] : q[3], y = P[k] ? P[k][4] : q[4]; s += '<g data-dest="' + k + '" class="nat-tap">' + n.ci(x, y, 24, i >= 0 ? n.C.claro : '#fff', i >= 0 ? n.C.teal : n.C.gris) + n.em(x, y, P[k] ? P[k][2] : '📍', 18) + '</g>' + n.txw(x, y + 40, t, { a: 'middle', s: 9.5, w: 800 }, 16) + (i >= 0 ? n.tx(x + 20, y - 18, i + 1, { s: 13, w: 900, c: n.C.coral }) : ''); });
      for (var j = 1; j < orden.length; j++) { var a2 = P[orden[j - 1]], b2 = P[orden[j]]; if (a2 && b2) s += n.fl(a2[3], a2[4], b2[3] - (b2[3] - a2[3]) * 0.25, b2[4] - (b2[4] - a2[4]) * 0.25, n.C.coral, 2.5); }
      return n.S(470, 250, s); });
    // las estaciones se dibujan en el lugar del orden correcto de la lección solo si los nombres coinciden; si no, en fila
    despues(blk, w); };

  // 10) PODERES y 11) SECTORES ---------------------------------------------------------------------------
  var EDI = { Ejecutivo: ['🏛️', 'administra y ejecuta'], Legislativo: ['📜', 'hace las leyes'], Judicial: ['⚖️', 'juzga y resuelve conflictos'] };
  A.poderes = function (blk) { if (!sels(blk).length) return; propio(blk); var w = caja('Tocá cada institución y llevala al edificio de su poder.'); clasificar(blk, w, function (c) { var e = EDI[c] || ['🏢', '']; return '<div class="soa-edif">' + e[0] + '</div><b>Poder ' + esc(c) + '</b><small>' + e[1] + '</small>'; }); despues(blk, w); };
  var SECZ = { primario: ['🌾', 'obtiene recursos de la naturaleza'], secundario: ['🏭', 'transforma en productos'], terciario: ['🛒', 'brinda servicios'] };
  A.sectores = function (blk) { if (!sels(blk).length) return; propio(blk); var w = caja('Tocá cada actividad y llevala a su sector: el campo, la fábrica o el comercio y los servicios.'); clasificar(blk, w, function (c) { var e = SECZ[norm(c).split(' ')[0]] || ['🏢', '']; return '<div class="soa-edif">' + e[0] + '</div><b>' + esc(c) + '</b><small>' + e[1] + '</small>'; }); despues(blk, w); };

  // 12) MERCADO ------------------------------------------------------------------------------------------
  A.mercado = function (blk, arg) { var n = N(); var inp = campoNum(blk); if (!n || !inp) return; var a = String(arg || '100,1:0,1').split(':'), d = a[0].split(',').map(Number), o = (a[1] || '0,1').split(',').map(Number), pmax = d[0] / d[1], pr = Math.round(pmax * 0.8);
    var w = caja('Mové el precio. Cuando lo que se demanda sea igual a lo que se ofrece, encontraste el equilibrio.'), rg = mk('input'), vis = mk('div'); rg.type = 'range'; rg.min = 0; rg.max = Math.round(pmax); rg.step = 1; rg.value = pr; rg.className = 'soa-rango'; ocultar(inp.closest('.nu-fila') || inp);
    function pintar() { pr = +rg.value; var qd = Math.max(0, d[0] - d[1] * pr), qo = Math.max(0, o[0] + o[1] * pr), mx = Math.max(d[0], o[0] + o[1] * pmax), s = '';
      s += n.tx(20, 30, 'Precio: $' + pr, { s: 16, w: 900, c: n.C.coral }) + n.tx(20, 62, 'Demandan', { s: 11, w: 800, c: n.C.azul }) + n.rc(100, 50, qd / mx * 330, 18, n.C.azul, null, 4) + n.tx(106 + qd / mx * 330, 64, Math.round(qd), { s: 11, w: 900 }) + n.tx(20, 92, 'Ofrecen', { s: 11, w: 800, c: n.C.coral }) + n.rc(100, 80, qo / mx * 330, 18, n.C.coral, null, 4) + n.tx(106 + qo / mx * 330, 94, Math.round(qo), { s: 11, w: 900 });
      s += n.tx(235, 126, Math.abs(qd - qo) < 1e-9 ? '⚖️ ¡Equilibrio!' : qd > qo ? 'Falta producto: escasez' : 'Sobra producto: exceso de oferta', { a: 'middle', s: 13, w: 900, c: Math.abs(qd - qo) < 1e-9 ? n.C.verde : n.C.sol });
      vis.innerHTML = n.S(470, 136, s); setVal(inp, String(pr)); }
    rg.addEventListener('input', pintar); w.appendChild(rg); w.appendChild(vis); pintar(); despues(blk, w); };

  // 13) CARRITO ------------------------------------------------------------------------------------------
  A.carrito = function (blk) { var p = enun(blk); if (!p) return; var m, L = [], re = /([^;$]+?)\s*\$\s*([\d.]+)\s*\$\s*([\d.]+)/g, t = p.textContent; while ((m = re.exec(t))) L.push([m[1].replace(/^[\s:.,]+/, '').trim(), +m[2].replace(/\./g, ''), +m[3].replace(/\./g, '')]); if (!L.length) return;
    var en = {}, w = caja('Tocá los productos para cargarlos al carrito y compará el total de antes y de ahora.'), g = mk('div', 'soa-gondola'), tot = mk('div', 'soa-tot');
    function pintar() { g.innerHTML = L.map(function (q, i) { return '<button type="button" class="soa-prod' + (en[i] ? ' on' : '') + '" data-i="' + i + '"><b>' + esc(q[0]) + '</b><span>antes $' + q[1].toLocaleString('es-AR') + '</span><span>ahora $' + q[2].toLocaleString('es-AR') + '</span></button>'; }).join('');
      var a1 = 0, a2 = 0; L.forEach(function (q, i) { if (en[i]) { a1 += q[1]; a2 += q[2]; } }); tot.innerHTML = '🛒 Antes: <b>$' + a1.toLocaleString('es-AR') + '</b> · Ahora: <b>$' + a2.toLocaleString('es-AR') + '</b>' + (a1 ? ' · Diferencia: <b>$' + (a2 - a1).toLocaleString('es-AR') + '</b>' : ''); }
    g.addEventListener('click', function (e) { var b = e.target.closest('[data-i]'); if (!b) return; var i = +b.getAttribute('data-i'); en[i] = !en[i]; sonar('bien'); pintar(); }); w.appendChild(g); w.appendChild(tot); pintar(); despues(blk, w); };

  // 14) BALANZA ------------------------------------------------------------------------------------------
  A.balanza = function (blk) { var n = N(); if (!n || !sels(blk).length) return; propio(blk); var w = caja('Tocá cada argumento y ponelo del lado que corresponde: la balanza se inclina.'), vis = mk('div');
    var pintar = clasificar(blk, w, null, function (S, cats) { var f = S.filter(function (s) { return s.value === cats[0]; }).length, c = S.filter(function (s) { return s.value === cats[1]; }).length, ang = Math.max(-14, Math.min(14, (c - f) * 5)), r = ang * Math.PI / 180;
      vis.innerHTML = n.S(470, 120, '<polygon points="235,40 215,115 255,115" fill="#B0BEC5"/>' + n.ln(235 - 150 * Math.cos(r), 40 - 150 * Math.sin(r), 235 + 150 * Math.cos(r), 40 + 150 * Math.sin(r), n.C.osc, 5) + n.tx(235 - 150 * Math.cos(r), 30 - 150 * Math.sin(r), (cats[0] || '') + ' (' + f + ')', { a: 'middle', s: 11, w: 900, c: n.C.verde }) + n.tx(235 + 150 * Math.cos(r), 30 + 150 * Math.sin(r), (cats[1] || '') + ' (' + c + ')', { a: 'middle', s: 11, w: 900, c: n.C.rosa })); });
    w.insertBefore(vis, w.querySelector('.soa-zonas')); pintar(); despues(blk, w); };

  // 15) DILEMA -------------------------------------------------------------------------------------------
  A.dilema = function (blk) { var ta = campoTxt(blk); if (!ta) return; ocultar(ta); var pos = '', mir = '', w = caja('Elegí tu postura y desde qué mirada la defendés. Después escribí tus razones.');
    var MIR = [['⚖️ Consecuencias', 'pienso en qué resultado trae más bienestar'], ['📏 Deber', 'pienso en la regla que tendría que valer para todos'], ['🌱 Virtud', 'pienso en qué haría una buena persona']];
    w.innerHTML += '<div class="an-fichas" data-g="p"><button type="button" class="an-ficha" data-v="Estoy a favor">👍 Estoy a favor</button><button type="button" class="an-ficha" data-v="Estoy en contra">👎 Estoy en contra</button></div><div class="soa-miradas">' + MIR.map(function (m) { return '<button type="button" class="soa-mir" data-v="' + esc(m[0].slice(3)) + '"><b>' + m[0] + '</b><small>' + m[1] + '</small></button>'; }).join('') + '</div><textarea class="soa-razon" rows="4" placeholder="Mis razones son…"></textarea>';
    function act() { setVal(ta, (pos ? pos + '. ' : '') + (mir ? 'Lo pienso desde la ética de la ' + mir.toLowerCase().replace('consecuencias', 'consecuencias') + '. ' : '') + w.querySelector('.soa-razon').value.trim()); }
    w.addEventListener('click', function (e) { var b = e.target.closest('[data-v]'); if (!b) return; if (b.classList.contains('soa-mir')) { mir = b.getAttribute('data-v'); [].forEach.call(w.querySelectorAll('.soa-mir'), function (x) { x.classList.toggle('on', x === b); }); } else { pos = b.getAttribute('data-v'); [].forEach.call(w.querySelectorAll('[data-g="p"] .an-ficha'), function (x) { x.classList.toggle('on', x === b); }); } act(); });
    w.addEventListener('input', act); despues(blk, w); };

  // 16) CHEQUEO ------------------------------------------------------------------------------------------
  A.chequeo = function (blk) { var cb = [].slice.call(blk.querySelectorAll('.mt-op input[type=checkbox]')); if (!cb.length) return; var p = enun(blk), txt = p ? p.innerHTML : '', w = caja('Leé la publicación y marcá en la lista las señales de alerta que encontrás.'), post = mk('div', 'soa-post', '<div class="soa-post-h">👤 <b>CadenaViral24</b> · hace 5 min</div><div>' + txt + '</div><div class="soa-sellos"></div>');
    if (p) p.innerHTML = '<b>Chequeá esta publicación:</b>';
    function pintar() { post.querySelector('.soa-sellos').innerHTML = cb.filter(function (c) { return c.checked; }).map(function (c) { return '<span>🚩 ' + esc(c.value) + '</span>'; }).join(''); }
    blk.addEventListener('change', function (e) { if (e.target.type === 'checkbox') pintar(); }); w.appendChild(post); despues(blk, w); pintar(); };

  // 17) SOCIEDAD -----------------------------------------------------------------------------------------
  A.sociedad = function (blk) { var n = N(); if (!n) return; var w = caja('Tocá los grupos desde el de más privilegios hasta el de menos: la pirámide se arma de arriba hacia abajo.');
    ordenarDib(blk, w, function (L, orden) { var s = '', nL = L.length; orden.forEach(function (k, i) { var y = 15 + i * (200 / nL), wd = 90 + i * (330 / nL), hh = 200 / nL - 4; s += '<path d="M' + (235 - wd / 2) + ',' + (y + hh) + ' L' + (235 - wd / 2 + 14) + ',' + y + ' L' + (235 + wd / 2 - 14) + ',' + y + ' L' + (235 + wd / 2) + ',' + (y + hh) + ' Z" fill="' + ['#B39DDB', '#9FA8DA', '#90CAF9', '#A5D6A7', '#FFE082', '#FFCC80'][i % 6] + '" stroke="#fff" stroke-width="2"/>' + n.tx(235, y + hh / 2 + 4, L[k], { a: 'middle', s: 10.5, w: 900 }); });
      var chips = L.map(function (t, k) { return orden.indexOf(k) >= 0 ? '' : '<g data-dest="' + k + '" class="nat-tap">' + n.rc(10 + (k % 3) * 153, 225 + Math.floor(k / 3) * 34, 147, 28, '#fff', n.C.teal, 10) + n.tx(83 + (k % 3) * 153, 243 + Math.floor(k / 3) * 34, t, { a: 'middle', s: 9.5, w: 800 }) + '</g>'; }).join('');
      return n.S(470, 235 + Math.ceil(L.length / 3) * 34, s + chips); }); despues(blk, w); };

  // 18) COMPARATIVA --------------------------------------------------------------------------------------
  A.comparativa = function (blk) { var t = blk.querySelector('table.mt-tabla'); if (!t) return; t.classList.add('soa-comp'); despues(blk, caja('Completá cada casillero comparando las dos columnas: mismo aspecto, fila por fila.')); var ths = t.querySelectorAll('thead th'), ic = ['🏷️', '🏛️', '🗺️', '⚔️', '💰', '🙏', '📜']; [].forEach.call(ths, function (th, i) { if (i) th.innerHTML = '<span class="soa-ic">' + ic[i % ic.length] + '</span>' + th.innerHTML; }); };


  // ---------- SOCIALES (parte 2): geografía física, filosofía y Constitución ----------
  function S2() { var n = N(); return n && n.soc2; }
  A.climograma = function (blk, arg) { var n = N(), d = S2(), inp = campoNum(blk); if (!d || !inp) return; var c = d.CLI[+arg || 0] || d.CLI[0], w = caja('Tocá cada mes para leer su temperatura y su lluvia. Después respondé.'), vis = mk('div', '', d.climo(c, 2)), lab = mk('div', 'an-val', 'Tocá una barra');
    vis.addEventListener('click', function (e) { var r = vis.querySelector('svg').getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 460, i = Math.floor((x - 50) / 30.5); if (i < 0 || i > 11) return; lab.innerHTML = 'Mes ' + (i + 1) + ': <b>' + String(c[1][i]).replace('.', ',') + ' °C</b> y <b>' + c[2][i] + ' mm</b>'; });
    w.appendChild(mk('b', '', '📍 ' + c[0])); w.appendChild(vis); w.appendChild(lab); despues(blk, w); };
  A.placas = function (blk) { var d = S2(); if (!d || !sels(blk).length) return; propio(blk); var w = caja('Tocá cada caso y llevalo al dibujo del borde que corresponde.'), K = { convergente: 'convergente', divergente: 'divergente', transformante: 'transformante' };
    clasificar(blk, w, function (c) { var k = K[norm(c).split(' ')[0]]; return '<b>' + esc(c) + '</b>' + (k ? '<div class="soa-mini">' + d.placas(k, 2) + '</div>' : ''); }); despues(blk, w); };
  A.cuenca = function (blk) { var d = S2(), S = sels(blk); if (!d || !S.length) return; propio(blk); var w = caja('Tocá el nombre de una parte y después su número en el mapa.'), vis = mk('div', '', d.cuenca(null, true)), pool = mk('div', 'an-fichas'), elegido = null;
    function pintar() { pool.innerHTML = S.map(function (s) { var t = filaDe(s); return '<button type="button" class="an-ficha' + (elegido === t ? ' on' : '') + (s.value ? ' usada' : '') + '" data-sp="' + esc(t) + '">' + esc(t) + (s.value ? ' → ' + esc(s.options[s.selectedIndex].text) : '') + '</button>'; }).join(''); }
    pool.addEventListener('click', function (e) { var f = e.target.closest('[data-sp]'); if (f) { elegido = f.getAttribute('data-sp'); pintar(); } });
    vis.addEventListener('click', function (e) { var t = e.target.closest('[data-t]'); if (!t || !elegido) return; var num = t.textContent.trim(), s = selDe(blk, elegido), op = s && [].filter.call(s.options, function (o) { return o.value && (o.text.trim() === num || o.value === num || new RegExp('\\b' + num + '\\b').test(o.text)); })[0]; if (op) { setVal(s, op.value); sonar('bien'); } elegido = null; pintar(); });
    w.appendChild(pool); w.appendChild(vis); pintar(); despues(blk, w); };
  A.argumento = function (blk) { if (!sels(blk).length) return; propio(blk); var w = caja('Armá el esquema del argumento: las premisas arriba y la conclusión abajo.');
    clasificar(blk, w, function (c) { return '<b>' + (/conc/i.test(c) ? '🎯 ' : '🧱 ') + esc(c) + '</b>'; }); var z = w.querySelector('.soa-zonas'); if (z) { z.classList.add('arbol', 'argu'); } despues(blk, w); };
  A.falacia = function (blk) { var rs = [].slice.call(blk.querySelectorAll('.mt-op input[type=radio]')), p = enun(blk), d = S2(); if (!rs.length || !p) return; var txt = p.textContent, w = caja('Leé el diálogo y elegí la trampa que tiene.'), ch = mk('div', 'soc2-chat');
    ch.innerHTML = txt.split(/\s*—\s*/).filter(Boolean).map(function (t, i) { return '<p class="' + (i % 2 ? 'der' : 'izq') + '">' + esc(t) + '</p>'; }).join('') + '<span class="soc2-sello" hidden></span>'; p.innerHTML = '<b>¿Qué falacia hay en este diálogo?</b>';
    var ICO = {}; if (d) d.FAL.forEach(function (f) { ICO[norm(f[0]).split(' ')[0]] = f[1]; });
    rs.forEach(function (r) { var op = r.closest('.mt-op'); if (op) ocultar(op); });
    var cards = mk('div', 'soa-miradas', rs.map(function (r, i) { var t = (r.closest('.mt-op') || r.parentNode).textContent.trim(); return '<button type="button" class="soa-mir" data-i="' + i + '"><b>' + (ICO[norm(t).split(' ')[0]] || '🪤') + ' ' + esc(t) + '</b></button>'; }).join(''));
    cards.addEventListener('click', function (e) { var b = e.target.closest('[data-i]'); if (!b) return; var r = rs[+b.getAttribute('data-i')]; r.checked = true; fire(r); [].forEach.call(cards.children, function (x) { x.classList.toggle('on', x === b); }); var sl = ch.querySelector('.soc2-sello'); sl.hidden = false; sl.textContent = b.textContent; sonar('bien'); });
    w.appendChild(ch); w.appendChild(cards); despues(blk, w); };
  A.constitucion = function (blk) { if (!sels(blk).length) return; propio(blk); var w = caja('Tocá cada caso y ubicalo en la página que corresponde de la Constitución.');
    clasificar(blk, w, function (c, k) { return '<b>' + (/garant/i.test(c) ? '🛡️ ' : /derech/i.test(c) ? '🧑‍🤝‍🧑 ' : '📜 ') + esc(c) + '</b>'; }); var z = w.querySelector('.soa-zonas'); if (z) z.classList.add('libro'); despues(blk, w); };
  A.periodos = function (blk, arg) { if (!sels(blk).length) return; propio(blk); var a = String(arg || '').split(':'), w = caja('Tocá cada aspecto y decidí: ¿cambió de un período al otro o continuó?');
    w.appendChild(mk('div', 'soa-puente', '<b>' + esc(a[0] || 'Antes') + '</b><span>⟶</span><b>' + esc(a[1] || 'Después') + '</b>'));
    clasificar(blk, w, function (c) { return '<b>' + (/contin/i.test(c) ? '= ' : '≠ ') + esc(c) + '</b>'; }); despues(blk, w); };
  A.bioma = function (blk) { var d = S2(); if (!d || !sels(blk).length) return; propio(blk); var w = caja('Tocá cada planta o animal y llevalo a su bioma.');
    clasificar(blk, w, function (c) { var b = d.BIO.filter(function (x) { return norm(x[0]) === norm(c); })[0]; return (b ? '<div class="soa-mini">' + d.paisaje(b, 1) + '</div>' : '') + '<b>' + esc(c) + '</b>'; }); despues(blk, w); };

  // ---------- Recorrido de la página ----------
  function quitar(root) { var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), nn, L = []; while ((nn = tw.nextNode())) if (nn.nodeValue.indexOf('[[') >= 0) L.push(nn); L.forEach(function (x) { RE.lastIndex = 0; x.nodeValue = x.nodeValue.replace(RE, ''); }); RE.lastIndex = 0; }
  function recorrer() {
    [].forEach.call(document.querySelectorAll('.wvp.act .mt-preg:not([data-asoc])'), function (blk) { var tx = blk.textContent || '', m = new RegExp(RE.source).exec(tx); if (!m) return; blk.setAttribute('data-asoc', '1');
      quitar(blk); var tp = blk.querySelector('.mt-tipo'), nm = NOMBRE[m[1]]; if (tp && nm) tp.innerHTML = '<span aria-hidden="true">' + nm[0] + '</span> ' + esc(nm[1]);
      try { A[m[1]](blk, m[2]); } catch (e) { if (window.console) console.warn('Actividad de Sociales', m[1], e); } });
    [].forEach.call(document.querySelectorAll('.wvp'), function (v) { if ((v.textContent || '').indexOf('[[') >= 0) quitar(v); });
  }
  var css = document.createElement('style');
  css.textContent = ['.soa-zonas{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px;margin-top:6px}.soa-zonas.arbol{grid-template-columns:1fr}.soa-zona{min-height:76px;padding:8px;border:2px dashed #9dbdb9;border-radius:14px;cursor:pointer;background:#fff}.soa-zona:hover{border-color:#087E83}.soa-zona small{display:block;color:#4b6a6c}',
    '.soa-dentro{display:flex;flex-wrap:wrap;gap:4px;justify-content:center;margin-top:6px}.soa-dentro span{padding:4px 8px;border-radius:8px;background:#D7F0E9;font-weight:700;font-size:.85rem}.soa-edif{font-size:2rem}',
    '.soa-proceso{margin:8px auto;padding:10px;border-radius:12px;background:#C2552E;color:#fff;font-weight:900;max-width:320px}',
    '.soa-ficha{margin-top:8px;padding:10px;border:2px solid #E3ECEA;border-radius:14px;text-align:left}.soa-campo{display:flex;gap:8px;margin:6px 0;padding:8px;border:2px dashed #9dbdb9;border-radius:10px;cursor:pointer}.soa-campo em{font-style:normal;font-weight:800;color:#066A6E}.an-ficha.usada{opacity:.5}',
    '.soa-dh{margin:6px auto;border-collapse:separate;border-spacing:4px}.soa-dh th{padding:4px 8px}.soa-dh td{padding:8px 10px;border:2px solid #E3ECEA;border-radius:8px;cursor:pointer;font-weight:800}.soa-dh td.on{background:var(--c);border-color:var(--c);color:#fff}',
    '.soa-rango{width:100%;accent-color:#087E83}.soa-gondola{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px}.soa-prod{padding:10px;border:2px solid #E3ECEA;border-bottom-width:4px;border-radius:14px;background:#fff;font:inherit;cursor:pointer;display:flex;flex-direction:column;gap:2px}.soa-prod.on{border-color:#087E83;background:#D7F0E9}.soa-prod span{font-size:.85rem}.soa-tot{margin-top:10px;font-size:1.05rem}',
    '.soa-miradas{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin:8px 0}.soa-mir{padding:10px;border:2px solid #E3ECEA;border-radius:14px;background:#fff;font:inherit;cursor:pointer;text-align:left}.soa-mir small{display:block;color:#4b6a6c}.soa-mir.on{border-color:#087E83;background:#D7F0E9}.soa-razon{width:100%;box-sizing:border-box;padding:10px 12px;border:2px solid #E3ECEA;border-radius:14px;font:inherit}',
    '.soa-post{margin:6px auto;max-width:440px;padding:12px;border:1px solid #ddd;border-radius:14px;background:#fff;text-align:left;box-shadow:0 2px 6px rgba(0,0,0,.08)}.soa-post-h{color:#555;margin-bottom:6px}.soa-sellos{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}.soa-sellos span{padding:3px 8px;border-radius:8px;background:#FCE4EC;color:#c2416b;font-weight:800;font-size:.85rem}',
    '.soa-mini svg{max-height:70px;width:100%}.soa-zonas.argu .soa-zona:last-child{border-color:#C2552E;background:#FFF8F0}.soa-zonas.argu{grid-template-columns:1fr}.soa-zonas.libro{background:#FFFDF5;border-left:8px solid #8D6E63;padding:8px;border-radius:6px 14px 14px 6px}.soa-puente{display:flex;justify-content:center;gap:10px;align-items:center;margin:6px 0}.soa-puente b{padding:6px 12px;border-radius:10px;background:#087E83;color:#fff}.soa-puente span{font-size:1.6rem;color:#C2552E}',
    '.soa-comp thead th{background:#087E83;color:#fff}.soa-ic{display:block;font-size:1.4rem}'].join('');
  document.head.appendChild(css);
  var pend = false;
  function prog() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; try { recorrer(); } catch (e) {} }); }
  function iniciar() { new MutationObserver(prog).observe(document.body, { childList: true, subtree: true }); prog(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
