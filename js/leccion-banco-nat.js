/* BANCO DE LA LECCIÓN INTERACTIVA · NATURALES (parte 1): seres vivos, cuerpo humano, genética, evolución y ecología.
   Mismo banco que js/leccion-banco.js y js/leccion-banco2.js (SOLO lección, separado del de actividades).
   Regla del área: cada ejemplo tiene un formato visual propio (dibujos con rótulos, recorridos, ruedas, redes, cuadros, simulaciones);
   no se repite el mismo molde. Todos los ejemplos son PASO A PASO (pasos: true). Sirve para secundaria y para Nivel Medio. */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h || !B._h.escena) return;
  var H = B._h, M = B.motores, R = H.R, pick = H.pick, mezclar = H.mezclar, fmt = H.fmt, num = H.num, chip = H.chip;
  var escena = H.escena, ctrl = H.ctrl, respuesta = H.respuesta, cajas = H.cajas;
  var C = { teal: '#087E83', osc: '#253638', claro: '#D7F0E9', coral: '#C2552E', sol: '#C29A1E', lila: '#7a3fa0', azul: '#2a7ab8', verde: '#3c8d2f', rosa: '#c2416b', gris: '#9dbdb9' };

  // ---------- herramientas comunes (las usan también js/leccion-banco-nat2.js y nat3) ----------
  function S(w, h, b) { return '<svg viewBox="0 0 ' + w + ' ' + h + '" class="nat-svg" role="img">' + FL + b + '</svg>'; }
  var FL = '<defs><marker id="natfl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs>';
  function tx(x, y, t, o) { o = o || {}; return '<text x="' + r1(x) + '" y="' + r1(y) + '"' + (o.c === '#fff' || o.sh ? ' class="sh"' : '') + (o.a ? ' text-anchor="' + o.a + '"' : '') + (o.c ? ' fill="' + o.c + '"' : '') + (o.s ? ' font-size="' + o.s + '"' : '') + (o.w ? ' font-weight="' + o.w + '"' : '') + '>' + t + '</text>'; }
  function ln(x1, y1, x2, y2, c, w, x) { return '<line x1="' + r1(x1) + '" y1="' + r1(y1) + '" x2="' + r1(x2) + '" y2="' + r1(y2) + '" stroke="' + (c || C.osc) + '" stroke-width="' + (w || 2) + '"' + (x || '') + '/>'; }
  function fl(x1, y1, x2, y2, c, w, x) { return ln(x1, y1, x2, y2, c || C.osc, w || 2, ' marker-end="url(#natfl)"' + (x || '')); }
  function ci(x, y, r, f, s, x2) { return '<circle cx="' + r1(x) + '" cy="' + r1(y) + '" r="' + r + '" fill="' + (f || 'none') + '"' + (s ? ' stroke="' + s + '" stroke-width="2"' : '') + (x2 || '') + '/>'; }
  function rc(x, y, w, h, f, s, rr, x2) { return '<rect x="' + r1(x) + '" y="' + r1(y) + '" width="' + r1(w) + '" height="' + r1(h) + '" rx="' + (rr || 0) + '" fill="' + (f || 'none') + '"' + (s ? ' stroke="' + s + '" stroke-width="2"' : '') + (x2 || '') + '/>'; }
  function em(x, y, e, s) { return '<text x="' + r1(x) + '" y="' + r1(y) + '" font-size="' + (s || 24) + '" text-anchor="middle" dominant-baseline="central">' + e + '</text>'; }
  function r1(x) { return Math.round(x * 10) / 10; }
  function txw(x, y, t, o, max) { max = max || 15; if (t.length <= max) return tx(x, y, t, o); var w = t.split(' '), a = '', b2 = ''; w.forEach(function (q) { if ((a + ' ' + q).trim().length <= Math.max(max, Math.ceil(t.length / 2)) && !b2) a = (a + ' ' + q).trim(); else b2 = (b2 + ' ' + q).trim(); });
    o = o || {}; return '<text x="' + r1(x) + '" y="' + r1(y - 7) + '"' + (o.a ? ' text-anchor="' + o.a + '"' : '') + (o.c ? ' fill="' + o.c + '"' : '') + (o.s ? ' font-size="' + o.s + '"' : '') + (o.w ? ' font-weight="' + o.w + '"' : '') + '><tspan x="' + r1(x) + '">' + a + '</tspan><tspan x="' + r1(x) + '" dy="1.15em">' + b2 + '</tspan></text>'; }
  function sel(k, lab, ops, v) { return '<div class="lb-fila"><label>' + lab + '</label><select data-k="' + k + '">' + ops.map(function (o) { var val = Array.isArray(o) ? o[0] : o, t = Array.isArray(o) ? o[1] : o; return '<option value="' + val + '"' + (String(val) === String(v) ? ' selected' : '') + '>' + t + '</option>'; }).join('') + '</select></div>'; }
  function otro(el) { var b = el.querySelector('[data-lb="otro"]'); if (b) b.textContent = '🔄 Otro caso'; }
  function rot(n, u) { var k; do { k = R(0, n - 1); } while (n > 1 && k === u.v); u.v = k; return k; }
  function nota(t) { return '<p class="nat-nota">' + t + '</p>'; }
  function pct(x) { return fmt(Math.round(x * 10) / 10) + ' %'; }
  // Ejercicio de elegir una opción (fichas). D = {cons, html, ops:[texto], ok: texto correcto, ayuda, bien}
  function elegir(el, api, datos) {
    H.ejercicio(el, api, '', function (c) {
      var D = datos(); el.querySelector('.lb-cons').innerHTML = D.cons;
      c.innerHTML = (D.html || '') + '<div class="lb-banco">' + mezclar(D.ops.slice()).map(function (o) { return '<button type="button" class="lb-chip" data-ok="' + (o === D.ok ? 1 : 0) + '">' + o + '</button>'; }).join('') + '</div>';
      c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (!b) return; [].forEach.call(c.querySelectorAll('.lb-chip'), function (x) { x.classList.toggle('sel', x === b); x.classList.remove('bien', 'mal'); }); };
      return { comprobar: function () { var s = c.querySelector('.lb-chip.sel'); if (!s) return { ok: false, msg: 'Tocá una ficha y después comprobá.' }; var ok = s.getAttribute('data-ok') === '1'; s.classList.add(ok ? 'bien' : 'mal'); return ok ? { ok: true, msg: D.bien || '¡Bien!' } : { ok: false, msg: D.ayuda || 'Revisalo.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-chip'), function (x) { x.classList.toggle('sel', x.getAttribute('data-ok') === '1'); }); } };
    }); otro(el);
  }
  // Ejercicio de ordenar tocando: D = {cons, html, items: [en el orden correcto], ayuda, bien}
  function ordenar(el, api, datos) {
    H.ejercicio(el, api, '', function (c) {
      var D = datos(), n = D.items.length; el.querySelector('.lb-cons').innerHTML = D.cons;
      c.innerHTML = (D.html || '') + '<ol class="nat-ord">' + D.items.map(function () { return '<li class="nat-hueco"></li>'; }).join('') + '</ol><div class="lb-banco">' + mezclar(D.items.map(function (t, i) { return { t: t, i: i }; })).map(function (o) { return '<button type="button" class="lb-chip" data-i="' + o.i + '">' + o.t + '</button>'; }).join('') + '</div><p class="lb-ayuda">Tocá las fichas en orden. Para sacar una, tocala de nuevo.</p>';
      var ol = c.querySelector('.nat-ord'), banco = c.querySelector('.lb-banco');
      c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (!b) return; b.classList.remove('bien', 'mal');
        if (b.parentNode === banco) { var h = [].filter.call(ol.children, function (li) { return !li.firstChild; })[0]; if (h) h.appendChild(b); } else banco.appendChild(b); };
      return { comprobar: function () { var L = [].map.call(ol.children, function (li) { return li.firstChild; }); if (L.some(function (x) { return !x; })) return { ok: false, msg: 'Te faltan ubicar ' + L.filter(function (x) { return !x; }).length + '.' };
          var mal = 0; L.forEach(function (b, k) { var ok = +b.getAttribute('data-i') === k; b.classList.toggle('bien', ok); b.classList.toggle('mal', !ok); if (!ok) mal++; });
          return mal ? { ok: false, msg: D.ayuda || 'Hay ' + mal + ' fuera de lugar (marcadas).' } : { ok: true, msg: D.bien || '¡Orden correcto!' }; },
        resolver: function () { var bs = [].slice.call(c.querySelectorAll('.lb-chip')); bs.forEach(function (b) { ol.children[+b.getAttribute('data-i')].appendChild(b); }); } };
    }); otro(el);
  }
  // Ejercicio de tocar en el dibujo: D = {cons, svg (con elementos data-t="valor"), ok: valor correcto, ayuda, bien}
  function tocar(el, api, datos) {
    H.ejercicio(el, api, '', function (c) {
      var D = datos(); el.querySelector('.lb-cons').innerHTML = D.cons; c.innerHTML = D.svg + (D.pie || '');
      c.onclick = function (e) { var t = e.target.closest('[data-t]'); if (!t) return; [].forEach.call(c.querySelectorAll('[data-t]'), function (x) { x.classList.toggle('nat-sel', x === t); x.classList.remove('nat-bien', 'nat-mal'); }); };
      return { comprobar: function () { var s = c.querySelector('.nat-sel'); if (!s) return { ok: false, msg: 'Tocá una ficha y después comprobá.' }; var ok = s.getAttribute('data-t') === String(D.ok); s.classList.add(ok ? 'nat-bien' : 'nat-mal'); return ok ? { ok: true, msg: D.bien || '¡Bien!' } : { ok: false, msg: D.ayuda || 'Revisalo.' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('[data-t]'), function (x) { x.classList.toggle('nat-sel', x.getAttribute('data-t') === String(D.ok)); }); } };
    }); otro(el);
  }
  H.nat = { C: C, S: S, tx: tx, txw: txw, ln: ln, fl: fl, ci: ci, rc: rc, em: em, r1: r1, sel: sel, otro: otro, rot: rot, nota: nota, pct: pct, elegir: elegir, ordenar: ordenar, tocar: tocar };

  // =====================================================================================
  // 1) PARTES: dibujo con rótulos que aparecen de a uno (célula, flor, planta, ojo, corazón, Tierra, neurona, bacteria, virus, suelo)
  // =====================================================================================
  var FIG = {
    celula_animal: { nombre: 'Célula animal', dib: '<ellipse cx="100" cy="105" rx="92" ry="86" fill="#FCE4EC" stroke="#c2416b" stroke-width="4"/>' +
        '<path d="M48,62 q12,-8 24,0 M46,70 q14,-8 28,0 M48,78 q12,-8 24,0" stroke="#C29A1E" stroke-width="3" fill="none"/>' +
        '<path d="M136,78 q8,-10 16,0 t16,0 M136,92 q8,-10 16,0 t16,0 M136,106 q8,-10 16,0 t16,0" stroke="#2a7ab8" stroke-width="2.5" fill="none"/>' +
        '<g fill="#253638"><circle cx="140" cy="118" r="2.5"/><circle cx="150" cy="122" r="2.5"/><circle cx="160" cy="117" r="2.5"/><circle cx="146" cy="128" r="2.5"/><circle cx="156" cy="130" r="2.5"/></g>' +
        '<circle cx="100" cy="100" r="30" fill="#E1D5F5" stroke="#7a3fa0" stroke-width="3"/><circle cx="108" cy="94" r="9" fill="#7a3fa0"/>' +
        '<g><ellipse cx="52" cy="150" rx="20" ry="10" fill="#F6C28B" stroke="#C2552E" stroke-width="2"/><polyline points="36,150 42,145 48,155 54,145 60,155 66,150" fill="none" stroke="#C2552E" stroke-width="1.5"/></g>' +
        '<g transform="rotate(-30 120 168)"><ellipse cx="120" cy="168" rx="16" ry="8" fill="#F6C28B" stroke="#C2552E" stroke-width="2"/><polyline points="107,168 112,164 117,172 122,164 127,172 132,168" fill="none" stroke="#C2552E" stroke-width="1.5"/></g>' +
        '<circle cx="158" cy="155" r="8" fill="#E8C95A" stroke="#C29A1E" stroke-width="2"/>',
      partes: [['Membrana plasmática', 100, 19, 'envuelve la célula y regula lo que entra y sale'], ['Citoplasma', 84, 178, 'líquido donde están los orgánulos'], ['Núcleo', 85, 112, 'guarda el ADN y dirige la célula'],
        ['Mitocondria', 52, 150, 'obtiene energía de los nutrientes (respiración celular)'], ['Retículo endoplasmático', 160, 92, 'red de membranas que fabrica y transporta sustancias'], ['Ribosomas', 152, 124, 'fabrican las proteínas'],
        ['Aparato de Golgi', 60, 70, 'empaqueta y distribuye lo que fabrica la célula'], ['Lisosoma', 158, 155, 'digiere restos y sustancias que ya no sirven']] },
    celula_vegetal: { nombre: 'Célula vegetal', dib: '<rect x="8" y="8" width="184" height="194" rx="16" fill="#E8F5E9" stroke="#3c8d2f" stroke-width="8"/><rect x="16" y="16" width="168" height="178" rx="12" fill="none" stroke="#8BC34A" stroke-width="2"/>' +
        '<rect x="66" y="48" width="104" height="110" rx="40" fill="#D6EEF8" stroke="#2a7ab8" stroke-width="3"/>' +
        '<circle cx="42" cy="52" r="20" fill="#E1D5F5" stroke="#7a3fa0" stroke-width="3"/><circle cx="47" cy="48" r="6" fill="#7a3fa0"/>' +
        '<g fill="#5BAA3C" stroke="#2E6B1F" stroke-width="1.5"><ellipse cx="34" cy="108" rx="13" ry="7"/><ellipse cx="170" cy="176" rx="12" ry="7"/><ellipse cx="104" cy="178" rx="13" ry="7"/><ellipse cx="160" cy="32" rx="12" ry="6"/><ellipse cx="34" cy="140" rx="12" ry="6"/></g>' +
        '<ellipse cx="44" cy="176" rx="14" ry="7" fill="#F6C28B" stroke="#C2552E" stroke-width="2"/>',
      partes: [['Pared celular', 100, 8, 'capa rígida de celulosa que da forma y sostén'], ['Membrana plasmática', 184, 120, 'por dentro de la pared, regula lo que entra y sale'], ['Vacuola', 118, 104, 'gran bolsa de agua y sustancias de reserva'],
        ['Cloroplasto', 34, 108, 'hace la fotosíntesis: tiene clorofila'], ['Núcleo', 42, 52, 'guarda el ADN'], ['Citoplasma', 140, 186, 'líquido donde están los orgánulos'], ['Mitocondria', 44, 176, 'obtiene energía de los nutrientes']] },
    flor: { nombre: 'Flor', dib: '<line x1="100" y1="215" x2="100" y2="150" stroke="#3c8d2f" stroke-width="7"/>' +
        '<g fill="#F7A8C4" stroke="#c2416b" stroke-width="2"><ellipse cx="60" cy="95" rx="34" ry="20" transform="rotate(-20 60 95)"/><ellipse cx="140" cy="95" rx="34" ry="20" transform="rotate(20 140 95)"/><ellipse cx="72" cy="56" rx="30" ry="18" transform="rotate(35 72 56)"/><ellipse cx="128" cy="56" rx="30" ry="18" transform="rotate(-35 128 56)"/></g>' +
        '<path d="M76,146 L60,124 L92,138 Z M124,146 L140,124 L108,138 Z" fill="#5BAA3C" stroke="#2E6B1F" stroke-width="2"/><ellipse cx="100" cy="148" rx="20" ry="8" fill="#8BC34A" stroke="#2E6B1F" stroke-width="2"/>' +
        '<g stroke="#C29A1E" stroke-width="2.5"><line x1="96" y1="130" x2="74" y2="86"/><line x1="104" y1="130" x2="126" y2="86"/></g><g fill="#F5D33B" stroke="#C29A1E" stroke-width="1.5"><ellipse cx="73" cy="83" rx="7" ry="4"/><ellipse cx="127" cy="83" rx="7" ry="4"/></g>' +
        '<ellipse cx="100" cy="130" rx="11" ry="13" fill="#9CCC65" stroke="#2E6B1F" stroke-width="2"/><line x1="100" y1="118" x2="100" y2="80" stroke="#7CB342" stroke-width="4"/><circle cx="100" cy="77" r="6" fill="#7CB342" stroke="#2E6B1F" stroke-width="1.5"/>',
      partes: [['Pétalo', 42, 100, 'atrae a los polinizadores con su color'], ['Antera (estambre)', 127, 83, 'parte masculina: produce el polen'], ['Estigma', 100, 76, 'recibe el polen: es la parte de arriba del pistilo'],
        ['Estilo', 100, 100, 'tubo que une el estigma con el ovario'], ['Ovario', 100, 131, 'guarda los óvulos; después se convierte en fruto'], ['Sépalo', 66, 128, 'hoja verde que protege la flor en el pimpollo'], ['Pedúnculo', 100, 195, 'une la flor con el tallo']] },
    planta: { nombre: 'Planta', dib: '<rect x="0" y="160" width="200" height="55" fill="#D7B98E"/><g stroke="#8D6E63" stroke-width="3" fill="none"><path d="M100,160 L100,205 M100,175 L78,198 M100,182 L124,204 M100,170 L120,188 M86,190 L74,210"/></g>' +
        '<line x1="100" y1="160" x2="100" y2="48" stroke="#3c8d2f" stroke-width="7"/><g fill="#5BAA3C" stroke="#2E6B1F" stroke-width="2"><ellipse cx="72" cy="118" rx="26" ry="11" transform="rotate(25 72 118)"/><ellipse cx="128" cy="96" rx="26" ry="11" transform="rotate(-25 128 96)"/><ellipse cx="76" cy="78" rx="20" ry="9" transform="rotate(30 76 78)"/></g>' +
        '<g fill="#F5D33B" stroke="#C29A1E" stroke-width="1.5"><circle cx="100" cy="24" r="10"/><circle cx="114" cy="34" r="10"/><circle cx="86" cy="34" r="10"/><circle cx="108" cy="48" r="10"/><circle cx="92" cy="48" r="10"/></g><circle cx="100" cy="37" r="8" fill="#8D6E63"/>',
      partes: [['Flor', 100, 30, 'órgano de la reproducción'], ['Hoja', 128, 96, 'hace la fotosíntesis y la transpiración'], ['Tallo', 100, 140, 'sostiene la planta y transporta la savia'], ['Raíz', 100, 196, 'fija la planta al suelo y absorbe agua y sales']] },
    ojo: { nombre: 'Ojo', dib: '<circle cx="110" cy="105" r="82" fill="#fff" stroke="#253638" stroke-width="3"/><path d="M118,26 A82,82 0 0 1 118,184" fill="none" stroke="#c2416b" stroke-width="6"/>' +
        '<path d="M44,58 Q8,105 44,152" fill="#D6EEF8" stroke="#2a7ab8" stroke-width="3"/><g stroke="#3B7A57" stroke-width="7"><line x1="40" y1="70" x2="40" y2="92"/><line x1="40" y1="118" x2="40" y2="140"/></g>' +
        '<ellipse cx="54" cy="105" rx="9" ry="26" fill="#FFF3C4" stroke="#C29A1E" stroke-width="2"/><path d="M190,98 L215,92 L215,120 L190,114 Z" fill="#F6C28B" stroke="#C2552E" stroke-width="2"/>',
      partes: [['Córnea', 22, 105, 'capa transparente del frente: deja pasar la luz'], ['Iris', 40, 80, 'parte de color: regula cuánta luz entra'], ['Pupila', 40, 105, 'agujero del iris por donde entra la luz'],
        ['Cristalino', 54, 118, 'lente que enfoca la imagen'], ['Humor vítreo', 120, 70, 'gel transparente que llena el ojo'], ['Retina', 188, 60, 'capa con células sensibles a la luz: forma la imagen'], ['Nervio óptico', 206, 106, 'lleva la información al cerebro']] },
    corazon: { nombre: 'Corazón (esquema)', dib: '<rect x="34" y="60" width="64" height="52" rx="14" fill="#BBD7F0" stroke="#2a7ab8" stroke-width="3"/><rect x="102" y="60" width="64" height="52" rx="14" fill="#F6C3C3" stroke="#c2416b" stroke-width="3"/>' +
        '<rect x="34" y="116" width="64" height="86" rx="20" fill="#8FB8E3" stroke="#2a7ab8" stroke-width="3"/><rect x="102" y="116" width="64" height="86" rx="20" fill="#EE9A9A" stroke="#c2416b" stroke-width="3"/><rect x="97" y="60" width="10" height="142" fill="#C9A9A6"/>' +
        '<path d="M50,60 L50,14" stroke="#2a7ab8" stroke-width="12"/><path d="M120,116 C120,40 160,20 186,40" stroke="#c2416b" stroke-width="12" fill="none"/><path d="M82,116 C82,60 70,40 40,30" stroke="#5B8FC7" stroke-width="9" fill="none"/>',
      partes: [['Aurícula derecha', 66, 86, 'recibe la sangre pobre en oxígeno del cuerpo'], ['Ventrículo derecho', 66, 160, 'la impulsa hacia los pulmones'], ['Aurícula izquierda', 134, 86, 'recibe la sangre rica en oxígeno de los pulmones'],
        ['Ventrículo izquierdo', 134, 160, 'la impulsa a todo el cuerpo: tiene la pared más gruesa'], ['Tabique', 102, 190, 'separa los dos lados: la sangre no se mezcla'], ['Aorta', 180, 38, 'la arteria más grande: sale del ventrículo izquierdo'], ['Venas cavas', 50, 20, 'traen la sangre del cuerpo a la aurícula derecha']] },
    tierra: { nombre: 'Capas de la Tierra', dib: '<circle cx="100" cy="105" r="98" fill="#8D6E63"/><circle cx="100" cy="105" r="90" fill="#E07A2F"/><circle cx="100" cy="105" r="52" fill="#F2A541"/><circle cx="100" cy="105" r="26" fill="#F5D33B"/>',
      partes: [['Corteza', 100, 10, 'capa sólida y delgada donde vivimos'], ['Manto', 100, 34, 'roca muy caliente que se mueve lentamente'], ['Núcleo externo', 100, 66, 'hierro y níquel en estado líquido'], ['Núcleo interno', 100, 105, 'hierro y níquel sólidos, a enorme presión']] },
    neurona: { nombre: 'Neurona', dib: '<g stroke="#7a3fa0" stroke-width="3" fill="none"><path d="M40,90 L14,62 M30,80 L22,52 M38,112 L10,128 M26,122 L18,146 M48,82 L44,50 M52,122 L50,152"/></g><circle cx="50" cy="102" r="22" fill="#E1D5F5" stroke="#7a3fa0" stroke-width="3"/><circle cx="50" cy="102" r="8" fill="#7a3fa0"/>' +
        '<line x1="72" y1="102" x2="182" y2="102" stroke="#7a3fa0" stroke-width="4"/><g fill="#F6C28B" stroke="#C2552E" stroke-width="2"><rect x="88" y="94" width="24" height="16" rx="8"/><rect x="118" y="94" width="24" height="16" rx="8"/><rect x="148" y="94" width="24" height="16" rx="8"/></g>' +
        '<g stroke="#7a3fa0" stroke-width="3"><line x1="182" y1="102" x2="198" y2="84"/><line x1="182" y1="102" x2="200" y2="102"/><line x1="182" y1="102" x2="198" y2="120"/></g><g fill="#7a3fa0"><circle cx="198" cy="84" r="4"/><circle cx="200" cy="102" r="4"/><circle cx="198" cy="120" r="4"/></g>',
      partes: [['Dendritas', 18, 62, 'reciben los mensajes de otras neuronas'], ['Cuerpo celular', 50, 122, 'tiene el núcleo y mantiene viva la neurona'], ['Axón', 80, 102, 'prolongación larga que conduce el impulso'], ['Vaina de mielina', 130, 102, 'envuelve el axón y acelera el impulso'], ['Terminales del axón', 198, 120, 'pasan el mensaje a la célula siguiente']] },
    bacteria: { nombre: 'Bacteria', dib: '<rect x="22" y="58" width="150" height="94" rx="47" fill="#FFF3C4" stroke="#C29A1E" stroke-width="5"/><rect x="30" y="66" width="134" height="78" rx="39" fill="#F3FBF7" stroke="#3c8d2f" stroke-width="3"/>' +
        '<path d="M60,100 q10,-20 20,0 t20,0 t20,0 q-10,20 -30,10 t-25,-5" fill="none" stroke="#7a3fa0" stroke-width="3"/><circle cx="138" cy="86" r="8" fill="none" stroke="#c2416b" stroke-width="3"/>' +
        '<g fill="#253638"><circle cx="62" cy="128" r="2.5"/><circle cx="72" cy="132" r="2.5"/><circle cx="130" cy="124" r="2.5"/><circle cx="142" cy="120" r="2.5"/><circle cx="118" cy="130" r="2.5"/></g><path d="M172,105 q10,-12 18,0 t18,0" fill="none" stroke="#253638" stroke-width="3"/>',
      partes: [['Cápsula', 96, 56, 'capa externa que la protege'], ['Pared celular', 96, 146, 'le da forma y resistencia'], ['ADN circular', 90, 100, 'material genético libre en el citoplasma: no hay núcleo'], ['Plásmido', 138, 86, 'pequeño anillo de ADN extra'], ['Ribosomas', 66, 128, 'fabrican proteínas'], ['Flagelo', 196, 104, 'le permite moverse']] },
    virus: { nombre: 'Virus', dib: '<g stroke="#C2552E" stroke-width="3">' + [0, 45, 90, 135, 180, 225, 270, 315].map(function (a) { var r = a * Math.PI / 180; return '<line x1="' + r1(100 + 62 * Math.cos(r)) + '" y1="' + r1(105 + 62 * Math.sin(r)) + '" x2="' + r1(100 + 82 * Math.cos(r)) + '" y2="' + r1(105 + 82 * Math.sin(r)) + '"/>'; }).join('') + '</g>' +
        [0, 45, 90, 135, 180, 225, 270, 315].map(function (a) { var r = a * Math.PI / 180; return '<circle cx="' + r1(100 + 84 * Math.cos(r)) + '" cy="' + r1(105 + 84 * Math.sin(r)) + '" r="7" fill="#E07A2F"/>'; }).join('') +
        '<circle cx="100" cy="105" r="62" fill="#FCE4EC" stroke="#c2416b" stroke-width="4"/><polygon points="100,62 137,83 137,127 100,148 63,127 63,83" fill="#D6EEF8" stroke="#2a7ab8" stroke-width="3"/><path d="M80,95 q10,-14 20,0 t20,0 M80,115 q10,-14 20,0 t20,0" fill="none" stroke="#7a3fa0" stroke-width="3"/>',
      partes: [['Espículas', 100, 23, 'proteínas que se enganchan a la célula que van a infectar'], ['Envoltura', 160, 120, 'membrana externa (no todos los virus la tienen)'], ['Cápside', 70, 125, 'cubierta de proteínas que protege el material genético'], ['Material genético', 100, 101, 'ADN o ARN con las instrucciones para hacer más virus']] },
    suelo: { nombre: 'Capas del suelo', dib: '<rect x="0" y="18" width="200" height="34" fill="#4E342E"/><rect x="0" y="52" width="200" height="50" fill="#8D6E63"/><rect x="0" y="102" width="200" height="50" fill="#BCAAA4"/><rect x="0" y="152" width="200" height="60" fill="#9E9E9E"/>' +
        '<g fill="#757575"><circle cx="40" cy="125" r="7"/><circle cx="120" cy="135" r="9"/><circle cx="170" cy="118" r="6"/></g><path d="M20,170 L60,190 M110,165 L150,200 M150,160 L180,175" stroke="#616161" stroke-width="3"/>' +
        '<g stroke="#3c8d2f" stroke-width="4"><line x1="50" y1="18" x2="50" y2="0"/><line x1="140" y1="18" x2="140" y2="2"/></g><g stroke="#A1887F" stroke-width="2" fill="none"><path d="M50,18 L46,60 M50,18 L58,70 M140,18 L136,74 M140,18 L150,64"/></g>',
      partes: [['Humus (capa orgánica)', 100, 34, 'restos de seres vivos descompuestos: muy fértil'], ['Suelo superficial', 100, 76, 'mezcla de minerales y humus donde crecen las raíces'], ['Subsuelo', 100, 126, 'más claro, con piedras y poca materia orgánica'], ['Roca madre', 100, 182, 'roca que, al desgastarse, forma el suelo']] }
  };
  function figura(p, i) { if (p.items && p.items.length) { var it = p.items[i] || p.items[0]; return { nombre: it.nombre, dib: em(100, 105, it.emoji || '🔬', 150), partes: it.partes.map(function (q) { return [q[0], q[1] * 200, q[2] * 210, q[3] || '']; }) }; }
    var L = p.figuras || [p.figura || 'celula_animal']; return FIG[L[i] || L[0]] || FIG.celula_animal; }
  function listaFig(p) { return p.items && p.items.length ? p.items.map(function (x) { return x.nombre; }) : (p.figuras || [p.figura || 'celula_animal']).map(function (k) { return (FIG[k] || FIG.celula_animal).nombre; }); }
  function dibPartes(F, hasta, marca) { // hasta: cuántos rótulos se muestran
    var W = 470, ox = 135, oy = 8, izq = [], der = [];
    F.partes.forEach(function (q, j) { (q[1] < 100 ? izq : der).push(j); });
    function ys(L) { L.sort(function (a, b) { return F.partes[a][2] - F.partes[b][2]; }); var n = L.length, o = {}; L.forEach(function (j, k) { o[j] = n === 1 ? F.partes[j][2] + oy : 20 + k * (210 / Math.max(1, n - 1)); }); return o; }
    var yi = ys(izq), yd = ys(der), b = '<g transform="translate(' + ox + ',' + oy + ')">' + F.dib + '</g>';
    F.partes.forEach(function (q, j) { if (j >= hasta) return; var px = ox + q[1], py = oy + q[2], L = q[1] < 100, ly = (L ? yi : yd)[j], lx = L ? 128 : 342, act = j === hasta - 1 && marca;
      b += ln(lx + (L ? 2 : -2), ly - 4, px, py, act ? C.coral : C.osc, act ? 2.5 : 1.5) + ci(px, py, 4, act ? C.coral : C.osc) + txw(L ? lx - 2 : lx + 2, ly, q[0], { a: L ? 'end' : 'start', c: act ? C.coral : C.osc, s: 12, w: 800 }, 16); });
    return S(W, 245, b);
  }
  M.partes = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = listaFig(p);
    escena(el, L.length > 1 ? sel('i', 'Dibujo', L.map(function (t, i) { return [i, t]; }), 0) : '', function (o) { var F = figura(p, +(o.i || 0)), P = [{ vis: dibPartes(F, 0), txt: 'Observá el dibujo: <b>' + F.nombre.toLowerCase() + '</b>. Vamos a nombrar cada parte.' }];
      F.partes.forEach(function (q, j) { P.push({ vis: dibPartes(F, j + 1, true), txt: '<b>' + q[0] + '</b>' + (q[3] ? ': ' + q[3] + '.' : '.') }); }); return P; });
  } };
  M.partes_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = listaFig(p), u = { v: -1 }, uf = { v: -1 };
    tocar(el, api, function () { var F = figura(p, rot(L.length, uf)), k = rot(F.partes.length, u), ox = 135, oy = 8;
      var b = '<g transform="translate(' + ox + ',' + oy + ')">' + F.dib + '</g>' + F.partes.map(function (q, j) { return '<g data-t="' + j + '" class="nat-tap">' + ci(ox + q[1], oy + q[2], 11, '#fff', C.osc) + tx(ox + q[1], oy + q[2] + 4.5, j + 1, { a: 'middle', s: 12, w: 900 }) + '</g>'; }).join('');
      return { cons: F.nombre + ': tocá el número que señala <b>' + F.partes[k][0].toLowerCase() + '</b>.', svg: S(470, 245, b), ok: k, ayuda: 'Pista: ' + F.partes[k][3] + '.', bien: '¡Bien! Es ' + F.partes[k][0].toLowerCase() + ': ' + F.partes[k][3] + '.' }; });
  } };

  // =====================================================================================
  // 2) RECORRIDO: una ficha viaja por estaciones y se transforma (digestión, circulación, respiración, savia, arco reflejo, orina)
  // =====================================================================================
  var REC = {
    digestion: { nombre: 'Digestión de un sándwich', ficha: '🥪', est: [['Boca', '👄', 'los dientes trituran y la saliva empieza a digerir el almidón', 'bolo alimenticio'], ['Esófago', '⬇️', 'los movimientos peristálticos empujan el bolo hacia el estómago', 'bolo alimenticio'],
      ['Estómago', '🫃', 'el jugo gástrico, muy ácido, digiere las proteínas', 'quimo'], ['Intestino delgado', '〰️', 'la bilis y los jugos terminan la digestión; los nutrientes pasan a la sangre', 'quilo'], ['Intestino grueso', '🔁', 'se absorbe el agua y se forma la materia fecal', 'materia fecal'], ['Ano', '🚽', 'se elimina lo que no se digirió: egestión', 'eliminado']] },
    sangre: { nombre: 'La sangre en la circulación doble', ficha: '🩸', est: [['Ventrículo derecho', '❤️', 'impulsa la sangre pobre en oxígeno', 'pobre en O₂'], ['Arteria pulmonar', '➡️', 'la lleva a los pulmones', 'pobre en O₂'], ['Pulmones', '🫁', 'deja dióxido de carbono y toma oxígeno', 'rica en O₂'], ['Venas pulmonares', '⬅️', 'la devuelven al corazón', 'rica en O₂'],
      ['Ventrículo izquierdo', '❤️', 'pasa por la aurícula izquierda y el ventrículo la impulsa con fuerza', 'rica en O₂'], ['Aorta', '➡️', 'la reparte a todo el cuerpo', 'rica en O₂'], ['Órganos y tejidos', '🧍', 'entrega oxígeno y nutrientes; recoge dióxido de carbono', 'pobre en O₂'], ['Venas cavas', '⬅️', 'la traen de vuelta a la aurícula derecha', 'pobre en O₂']] },
    aire: { nombre: 'El aire hasta los alvéolos', ficha: '💨', est: [['Fosas nasales', '👃', 'el aire se filtra, se humedece y se calienta', 'aire filtrado'], ['Faringe', '⬇️', 'conducto que comparten el aire y el alimento', 'aire'], ['Laringe', '🗣️', 'tiene las cuerdas vocales; la epiglotis evita que entre comida', 'aire'],
      ['Tráquea', '🫁', 'tubo con anillos de cartílago que no se cierra', 'aire'], ['Bronquios y bronquiolos', '🌿', 'se ramifican dentro de cada pulmón', 'aire'], ['Alvéolos', '🫧', 'el oxígeno pasa a la sangre y el dióxido de carbono sale', 'intercambio de gases']] },
    savia: { nombre: 'El agua dentro de la planta', ficha: '💧', est: [['Raíz', '🌱', 'los pelos absorbentes toman agua y sales minerales', 'savia bruta'], ['Tallo (xilema)', '⬆️', 'los vasos llevan la savia bruta hacia arriba', 'savia bruta'], ['Hoja', '🍃', 'con luz, CO₂ y agua hace la fotosíntesis', 'savia elaborada'], ['Floema', '⬇️', 'reparte la savia elaborada (con azúcares) a toda la planta', 'savia elaborada'], ['Toda la planta', '🌳', 'las células usan los azúcares para crecer y vivir', 'energía y materia']] },
    reflejo: { nombre: 'Arco reflejo: sacar la mano del fuego', ficha: '⚡', est: [['Receptor', '🔥', 'la piel detecta el calor', 'estímulo'], ['Neurona sensitiva', '➡️', 'lleva el impulso nervioso hacia la médula', 'impulso nervioso'], ['Médula espinal', '🦴', 'una interneurona responde sin esperar al cerebro', 'respuesta'], ['Neurona motora', '➡️', 'lleva la orden al músculo', 'impulso nervioso'], ['Músculo', '💪', 'se contrae y retira la mano', 'movimiento']] },
    orina: { nombre: 'Formación de la orina', ficha: '🩸', est: [['Arteria renal', '➡️', 'llega la sangre con desechos', 'sangre con urea'], ['Riñón (nefronas)', '🫘', 'filtra la sangre y forma la orina', 'orina'], ['Uréteres', '⬇️', 'llevan la orina a la vejiga', 'orina'], ['Vejiga', '🫙', 'la almacena', 'orina'], ['Uretra', '🚽', 'la elimina al exterior', 'eliminada']] }
  };
  function recLista(p) { return p.items && p.items.length ? p.items : (p.recorridos || [p.recorrido || 'digestion']).map(function (k) { return REC[k] || REC.digestion; }); }
  function dibRec(r, k) { var n = r.est.length, por = n > 6 ? 4 : 3, W = 470, filas = Math.ceil(n / por), H2 = 20 + filas * 96, pos = [], b = '';
    for (var j = 0; j < n; j++) { var f = Math.floor(j / por), c = j % por; if (f % 2) c = por - 1 - c; pos.push([60 + c * ((W - 120) / (por - 1)), 50 + f * 96]); }
    for (j = 0; j < n - 1; j++) b += fl(pos[j][0] + (pos[j + 1][1] === pos[j][1] ? (pos[j + 1][0] > pos[j][0] ? 30 : -30) : 0), pos[j][1] + (pos[j + 1][1] === pos[j][1] ? 0 : 30), pos[j + 1][0] + (pos[j + 1][1] === pos[j][1] ? (pos[j + 1][0] > pos[j][0] ? -30 : 30) : 0), pos[j + 1][1] - (pos[j + 1][1] === pos[j][1] ? 0 : 30), j < k ? C.teal : '#cfdedb', 3);
    r.est.forEach(function (s, j) { var on = j === k, ya = j < k; b += ci(pos[j][0], pos[j][1], 27, on ? '#FFF3C4' : ya ? C.claro : '#fff', on ? C.coral : ya ? C.teal : '#cfdedb', on ? ' stroke-width="4"' : '') + em(pos[j][0], pos[j][1], s[1], 24) + tx(pos[j][0], pos[j][1] + 44, s[0], { a: 'middle', s: 12, w: 800, c: on ? C.coral : C.osc }); });
    if (k >= 0) b += rc(105, H2 - 6, 260, 30, C.coral, null, 15) + tx(235, H2 + 14, r.ficha + ' ahora es: ' + r.est[k][3], { a: 'middle', c: '#fff', s: 13, w: 800 });
    else b += rc(105, H2 - 6, 260, 30, '#F3FBF7', C.gris, 15) + tx(235, H2 + 14, r.ficha + ' entra al recorrido', { a: 'middle', s: 13, w: 800 });
    return S(W, H2 + 30, b); }
  M.recorrido = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = recLista(p);
    escena(el, L.length > 1 ? sel('i', 'Recorrido', L.map(function (r, i) { return [i, r.nombre]; }), 0) : '', function (o) { var r = L[+(o.i || 0)] || L[0], P = [{ vis: dibRec(r, -1), txt: '<b>' + r.nombre + '</b>: seguí la ficha ' + r.ficha + ' estación por estación.' }];
      r.est.forEach(function (s, j) { P.push({ vis: dibRec(r, j), txt: '<b>' + s[0] + '</b>: ' + s[2] + '.' }); }); return P; });
  } };
  M.recorrido_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = recLista(p), u = { v: -1 };
    ordenar(el, api, function () { var r = L[rot(L.length, u)]; return { cons: '<b>' + r.nombre + '</b>: ordená las estaciones del recorrido, de la primera a la última.', items: r.est.map(function (s) { return s[1] + ' ' + s[0]; }), ayuda: 'Pensá por dónde entra y qué le pasa en cada lugar.', bien: '¡Bien! ' + r.est.map(function (s) { return s[0]; }).join(' → ') + '.' }; });
  } };

  // =====================================================================================
  // 3) CICLO: rueda de etapas que se ilumina de a una (agua, carbono, nitrógeno, metamorfosis, celular, rocas, vida de una planta)
  // =====================================================================================
  var CIC = {
    agua: { nombre: 'Ciclo del agua', et: [['Evaporación', '☀️', 'el calor del Sol convierte el agua de mares, ríos y lagos en vapor'], ['Condensación', '☁️', 'el vapor sube, se enfría y forma gotitas: las nubes'], ['Precipitación', '🌧️', 'el agua cae como lluvia, nieve o granizo'], ['Escurrimiento e infiltración', '🏞️', 'corre por la superficie o se filtra en el suelo'], ['Acumulación', '🌊', 'llega a mares, lagos y napas, y vuelve a evaporarse']] },
    carbono: { nombre: 'Ciclo del carbono', et: [['Fotosíntesis', '🌿', 'las plantas toman CO₂ del aire y forman azúcares'], ['Alimentación', '🐄', 'los animales comen y el carbono pasa a su cuerpo'], ['Respiración', '💨', 'plantas y animales devuelven CO₂ al aire'], ['Descomposición', '🍄', 'hongos y bacterias degradan los restos y liberan CO₂'], ['Combustión', '🏭', 'quemar combustibles fósiles libera el carbono guardado durante millones de años']] },
    nitrogeno: { nombre: 'Ciclo del nitrógeno', et: [['Fijación', '🦠', 'bacterias del suelo transforman el nitrógeno del aire en compuestos útiles'], ['Absorción', '🌱', 'las plantas toman los nitratos por la raíz'], ['Consumo', '🐑', 'los animales lo incorporan al comer plantas'], ['Descomposición', '🍄', 'los restos se transforman en amonio'], ['Desnitrificación', '💨', 'otras bacterias devuelven el nitrógeno al aire']] },
    rana: { nombre: 'Metamorfosis de la rana', et: [['Huevos', '🫧', 'la hembra pone los huevos en el agua'], ['Renacuajo', '🐟', 'respira por branquias y tiene cola'], ['Renacuajo con patas', '🦵', 'le crecen las patas y se forman los pulmones'], ['Rana joven', '🐸', 'pierde la cola y sale del agua'], ['Rana adulta', '🐸', 'se reproduce y el ciclo vuelve a empezar']] },
    mariposa: { nombre: 'Metamorfosis de la mariposa', et: [['Huevo', '⚪', 'la mariposa pone los huevos sobre una hoja'], ['Oruga (larva)', '🐛', 'come muchísimo y crece'], ['Crisálida (pupa)', '🫘', 'adentro, el cuerpo se transforma por completo'], ['Mariposa adulta', '🦋', 'sale, vuela y se reproduce']] },
    celular: { nombre: 'Ciclo celular', et: [['G1', '🌱', 'la célula crece y fabrica proteínas'], ['S', '🧬', 'duplica su ADN'], ['G2', '🔧', 'revisa el ADN y se prepara para dividirse'], ['Mitosis', '✂️', 'divide el núcleo en dos núcleos iguales'], ['Citocinesis', '⚪⚪', 'divide el citoplasma: quedan dos células hijas']] },
    rocas: { nombre: 'Ciclo de las rocas', et: [['Magma', '🌋', 'roca fundida en el interior de la Tierra'], ['Roca ígnea', '🪨', 'el magma se enfría y se solidifica'], ['Meteorización y erosión', '🌬️', 'el agua, el viento y el hielo la desgastan en sedimentos'], ['Roca sedimentaria', '🧱', 'los sedimentos se compactan en capas'], ['Roca metamórfica', '🔥', 'el calor y la presión la transforman; si se funde, vuelve a ser magma']] },
    planta: { nombre: 'Ciclo de vida de una planta', et: [['Semilla', '🌰', 'guarda el embrión y su reserva de alimento'], ['Germinación', '🌱', 'con agua y temperatura adecuada, sale la raíz y el tallito'], ['Planta adulta', '🌿', 'crece y fabrica su alimento'], ['Flor', '🌸', 'se poliniza y se forman las semillas'], ['Fruto', '🍎', 'protege las semillas y ayuda a dispersarlas']] }
  };
  function cicLista(p) { return p.items && p.items.length ? p.items : (p.ciclos || [p.ciclo || 'agua']).map(function (k) { return CIC[k] || CIC.agua; }); }
  function dibCic(c, k, oculto) { var n = c.et.length, cx = 235, cy = 142, rr = 86, b = ci(cx, cy, rr, 'none', '#E3ECEA', ' stroke-width="14"'), pos = c.et.map(function (_, j) { var a = -Math.PI / 2 + j * 2 * Math.PI / n; return [cx + rr * Math.cos(a), cy + rr * Math.sin(a), a]; });
    pos.forEach(function (q, j) { var a1 = q[2] + 0.36, a2 = q[2] + 2 * Math.PI / n - 0.36, act = k >= n || j < k; b += '<path d="M' + r1(cx + rr * Math.cos(a1)) + ',' + r1(cy + rr * Math.sin(a1)) + ' A' + rr + ',' + rr + ' 0 0 1 ' + r1(cx + rr * Math.cos(a2)) + ',' + r1(cy + rr * Math.sin(a2)) + '" fill="none" stroke="' + (act ? C.teal : '#cfdedb') + '" stroke-width="3" marker-end="url(#natfl)"/>'; });
    pos.forEach(function (q, j) { var on = j === k, x = q[0], y = q[1], lab = j === oculto ? '?' : c.et[j][0], lx = x + (Math.cos(q[2]) > 0.3 ? 32 : Math.cos(q[2]) < -0.3 ? -32 : 0), ly = y + (Math.abs(Math.cos(q[2])) <= 0.3 ? (Math.sin(q[2]) < 0 ? -34 : 42) : 5), an = Math.cos(q[2]) > 0.3 ? 'start' : Math.cos(q[2]) < -0.3 ? 'end' : 'middle';
      b += ci(x, y, 24, on ? '#FFF3C4' : '#fff', on ? C.coral : C.teal, on ? ' stroke-width="4"' : '') + (j === oculto ? tx(x, y + 7, '?', { a: 'middle', s: 22, w: 900, c: C.coral }) : em(x, y, c.et[j][1], 22)) + txw(lx, ly, lab, { a: an, s: 12, w: 800, c: on ? C.coral : C.osc }, an === 'middle' ? 22 : 15); });
    b += tx(cx, cy - 4, c.nombre.replace(/^(Ciclo|Metamorfosis) de(l| la)? /, ''), { a: 'middle', s: 13, w: 900, c: C.teal }) + tx(cx, cy + 14, '↻', { a: 'middle', s: 22, c: C.teal });
    return S(470, 284, b); }
  M.ciclo = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = cicLista(p);
    escena(el, L.length > 1 ? sel('i', 'Ciclo', L.map(function (c, i) { return [i, c.nombre]; }), 0) : '', function (o) { var c = L[+(o.i || 0)] || L[0], P = [{ vis: dibCic(c, -1), txt: '<b>' + c.nombre + '</b>: ' + c.et.length + ' etapas que se repiten una y otra vez.' }];
      c.et.forEach(function (s, j) { P.push({ vis: dibCic(c, j), txt: '<b>' + s[0] + '</b>: ' + s[2] + '.' }); }); P.push({ vis: dibCic(c, c.et.length), txt: 'Y vuelve a empezar: por eso es un <b>ciclo</b>, no tiene principio ni fin.' }); return P; });
  } };
  M.ciclo_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = cicLista(p), u = { v: -1 }, uk = { v: -1 };
    elegir(el, api, function () { var c = L[rot(L.length, u)], k = rot(c.et.length, uk), otros = [];
      Object.keys(CIC).forEach(function (q) { CIC[q].et.forEach(function (s) { if (c.et.every(function (z) { return z[0] !== s[0]; })) otros.push(s[0]); }); });
      c.et.forEach(function (s, j) { if (j !== k) otros.push(s[0]); });
      var ops = [c.et[k][0]].concat(mezclar(otros).filter(function (x, i, a) { return a.indexOf(x) === i; }).slice(0, 3));
      return { cons: '<b>' + c.nombre + '</b>: ¿qué etapa falta en el lugar del signo de pregunta?', html: dibCic(c, -1, k), ops: ops, ok: c.et[k][0], ayuda: 'Mirá la etapa anterior y la siguiente: ¿qué tiene que pasar entre las dos?', bien: '¡Bien! ' + c.et[k][0] + ': ' + c.et[k][2] + '.' }; });
  } };

  // =====================================================================================
  // 4) RED TRÓFICA: niveles, flechas de energía, regla del 10 % y qué pasa si desaparece una especie
  // =====================================================================================
  var REDES = {
    pastizal: { nombre: 'Pastizal pampeano', el: 'el pastizal pampeano', sp: [['Pasto', '🌾', 1, []], ['Cardo', '🌿', 1, []], ['Langosta', '🦗', 2, [0]], ['Liebre', '🐇', 2, [0, 1]], ['Ratón', '🐁', 2, [0, 1]], ['Sapo', '🐸', 3, [2]], ['Lechuza', '🦉', 3, [4]], ['Zorro', '🦊', 3, [3, 4]], ['Puma', '🐆', 4, [3, 7]]] },
    laguna: { nombre: 'Laguna', el: 'la laguna', sp: [['Algas', '🟢', 1, []], ['Juncos', '🌿', 1, []], ['Caracol', '🐌', 2, [0]], ['Mojarra', '🐟', 2, [0]], ['Coipo', '🦫', 2, [1]], ['Tararira', '🐠', 3, [3]], ['Garza', '🪿', 3, [2, 3]], ['Yacaré', '🐊', 4, [4, 5, 6]]] },
    monte: { nombre: 'Monte chaqueño', el: 'el monte chaqueño', sp: [['Algarrobo', '🌳', 1, []], ['Cactus', '🌵', 1, []], ['Oruga', '🐛', 2, [0]], ['Vizcacha', '🐀', 2, [0, 1]], ['Corzuela', '🦌', 2, [0]], ['Hornero', '🐦', 3, [2]], ['Boa', '🐍', 3, [3, 5]], ['Yaguareté', '🐆', 4, [3, 4, 6]]] }
  };
  var NIV = ['', 'Productores', 'Consumidores primarios', 'Consumidores secundarios', 'Consumidores terciarios'];
  function redPos(r) { var por = {}, pos = []; r.sp.forEach(function (s, j) { (por[s[2]] = por[s[2]] || []).push(j); });
    Object.keys(por).forEach(function (nv) { var L = por[nv]; L.forEach(function (j, k) { pos[j] = [118 + (k + 0.5) * (290 / L.length), 236 - (nv - 1) * 58]; }); }); return pos; }
  function dibRed(r, hasta, opt) { opt = opt || {}; var pos = redPos(r), b = '', fuera = opt.fuera;
    for (var nv = 1; nv <= 4; nv++) if (nv <= hasta && r.sp.some(function (s) { return s[2] === nv; })) b += txw(4, 240 - (nv - 1) * 58, NIV[nv], { s: 10, c: C.teal, w: 800 }, 13);
    if (hasta >= 1) b += em(432, 30, '☀️', 26) + tx(432, 56, 'energía del Sol', { a: 'middle', s: 9.5 });
    r.sp.forEach(function (s, j) { if (s[2] > hasta) return; s[3].forEach(function (q) { var a = pos[q], c = pos[j], dx = c[0] - a[0], dy = c[1] - a[1], d = Math.sqrt(dx * dx + dy * dy); var gris = fuera != null && (q === fuera || j === fuera);
      b += fl(a[0] + dx / d * 18, a[1] + dy / d * 18, c[0] - dx / d * 20, c[1] - dy / d * 20, gris ? '#d9d9d9' : C.teal, 2, gris ? ' stroke-dasharray="4 3"' : ''); }); });
    r.sp.forEach(function (s, j) { if (s[2] > hasta) return; var q = pos[j], st = opt.est && opt.est[j], f = j === fuera ? '#eee' : st === 'baja' ? '#FCE4EC' : st === 'sube' ? '#E8F5E9' : '#fff', bord = j === fuera ? '#bbb' : st === 'baja' ? C.rosa : st === 'sube' ? C.verde : C.teal;
      b += ci(q[0], q[1], 18, f, bord) + em(q[0], q[1], s[1], 20) + tx(q[0], q[1] + 31, s[0], { a: 'middle', s: 10.5, w: 800, c: j === fuera ? '#aaa' : C.osc }) + (j === fuera ? ln(q[0] - 14, q[1] - 14, q[0] + 14, q[1] + 14, C.rosa, 3) : '') + (st === 'baja' ? tx(q[0] + 20, q[1] - 12, '▼', { s: 12, c: C.rosa }) : st === 'sube' ? tx(q[0] + 20, q[1] - 12, '▲', { s: 12, c: C.verde }) : ''); });
    if (opt.desc) b += em(440, 196, '🍄', 22) + tx(440, 222, 'Descompo-', { a: 'middle', s: 9.5, w: 800 }) + tx(440, 233, 'nedores', { a: 'middle', s: 9.5, w: 800 }) + fl(420, 140, 436, 180, '#8D6E63', 2, ' stroke-dasharray="4 3"');
    return S(470, 280, b); }
  function efectos(r, x) { var est = {}; r.sp.forEach(function (s, j) { if (s[3].indexOf(x) >= 0) est[j] = s[3].length === 1 ? 'baja' : 'baja'; });
    r.sp[x][3].forEach(function (q) { est[q] = 'sube'; }); return est; }
  M.red_trofica = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var r = REDES[p.red] || p.red_propia || REDES.pastizal, maxN = Math.max.apply(null, r.sp.map(function (s) { return s[2]; }));
    escena(el, ctrl('e', 'Energía que captan los productores (kcal)', 1000, 100000, 1000, 10000) + sel('x', 'Si desaparece…', [[-1, '(ninguna)']].concat(r.sp.map(function (s, j) { return [j, s[0]]; })), -1), function (o) { var E = o.e || 10000, x = +o.x, P = [];
      P.push({ vis: dibRed(r, 1), txt: '<b>Productores</b>: fabrican su alimento con la energía del Sol (' + r.sp.filter(function (s) { return s[2] === 1; }).map(function (s) { return s[0].toLowerCase(); }).join(', ') + ').' });
      for (var nv = 2; nv <= maxN; nv++) P.push({ vis: dibRed(r, nv), txt: '<b>' + NIV[nv] + '</b>: ' + r.sp.filter(function (s) { return s[2] === nv; }).map(function (s) { return s[0].toLowerCase(); }).join(', ') + '. Las flechas van del que es comido al que come: muestran el camino de la energía.' });
      P.push({ vis: dibRed(r, maxN, { desc: true }), txt: 'Los <b>descomponedores</b> (hongos y bacterias) transforman los restos de todos y devuelven la materia al suelo.' });
      var ener = [E]; for (nv = 2; nv <= maxN; nv++) ener.push(ener[nv - 2] / 10);
      var pir = ener.map(function (v, i) { var w = 380 - i * 80; return rc(235 - w / 2, 200 - i * 46, w, 38, ['#5BAA3C', '#9CCC65', '#F5D33B', '#E07A2F'][i], C.osc, 6) + tx(235, 224 - i * 46, NIV[i + 1].replace('Consumidores', 'Cons.') + ': ' + fmt(Math.round(v * 100) / 100) + ' kcal', { a: 'middle', s: 12, w: 800 }); }).join('');
      P.push({ vis: S(470, 248, pir), txt: '<b>Regla del 10 %</b>: a cada nivel pasa solo una décima parte de la energía; el resto se pierde como calor y en la actividad de los seres vivos.' });
      if (x >= 0) { var est = efectos(r, x), sube = [], baja = []; Object.keys(est).forEach(function (j) { (est[j] === 'sube' ? sube : baja).push(r.sp[j][0].toLowerCase()); });
        P.push({ vis: dibRed(r, maxN, { fuera: x, est: est }), txt: 'Si desaparece <b>' + r.sp[x][0].toLowerCase() + '</b>: ' + (baja.length ? 'bajan sus predadores (' + baja.join(', ') + ')' : 'ningún animal se queda sin una de sus presas') + (sube.length ? '; aumentan lo que comía (' + sube.join(', ') + ')' : '') + '.' }); }
      return P; });
  } };
  M.red_trofica_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = (p.redes || [p.red || 'pastizal']).map(function (k) { return REDES[k] || REDES.pastizal; }), u = { v: -1 }, ut = { v: -1 };
    var tipos = p.que ? [].concat(p.que) : ['rol', 'energia', 'quitar'];
    H.ejercicio(el, api, '', function (c) { var r = L[rot(L.length, u)], t = tipos[rot(tipos.length, ut)], D;
      if (t === 'energia') { var E = pick([1000, 5000, 10000, 20000, 50000]), nv = R(2, 3), v = E / Math.pow(10, nv - 1);
        el.querySelector('.lb-cons').innerHTML = 'Los productores de ' + r.el + ' captan <b>' + fmt(E) + ' kcal</b>. Según la regla del 10 %, ¿cuántas kcal llegan a los <b>' + NIV[nv].toLowerCase() + '</b>?';
        c.innerHTML = dibRed(r, 4) + '<div class="lb2-campos"><label class="lb2-campo"><input class="lb-inp" inputmode="decimal" data-i="0"><em>kcal</em></label></div>';
        return { comprobar: function () { var x = num(c.querySelector('input').value); if (!isFinite(x)) return { ok: false, msg: 'Completá todos los casilleros.' }; return Math.abs(x - v) < 1e-6 ? { ok: true, msg: '¡Bien! ' + fmt(E) + (nv === 3 ? ' → ' + fmt(E / 10) : '') + ' → ' + fmt(v) + ' kcal.' } : { ok: false, msg: 'Dividí por 10 en cada salto de nivel.' }; }, resolver: function () { c.querySelector('input').value = String(v).replace('.', ','); } }; }
      var j = R(0, r.sp.length - 1), ops, ok, cons;
      if (t === 'rol') { ok = NIV[r.sp[j][2]]; ops = NIV.slice(1, 5).concat('Descomponedores'); cons = 'En ' + r.el + ', ¿qué papel cumple <b>' + r.sp[j][0].toLowerCase() + '</b> ' + r.sp[j][1] + '?'; }
      else { do { j = R(0, r.sp.length - 1); } while (!r.sp.some(function (s) { return s[3].indexOf(j) >= 0; }) && !r.sp[j][3].length);
        var est = efectos(r, j), ks = Object.keys(est), q = +pick(ks); ok = est[q] === 'sube' ? 'Aumenta' : 'Disminuye'; ops = ['Aumenta', 'Disminuye', 'No cambia'];
        cons = 'En ' + r.el + ', si desaparece <b>' + r.sp[j][0].toLowerCase() + '</b>, ¿qué le pasa a la población de <b>' + r.sp[q][0].toLowerCase() + '</b>?'; }
      el.querySelector('.lb-cons').innerHTML = cons;
      c.innerHTML = dibRed(r, 4) + '<div class="lb-banco">' + mezclar(ops).map(function (o) { return '<button type="button" class="lb-chip" data-ok="' + (o === ok ? 1 : 0) + '">' + o + '</button>'; }).join('') + '</div>';
      c.onclick = function (e) { var b = e.target.closest('.lb-chip'); if (!b) return; [].forEach.call(c.querySelectorAll('.lb-chip'), function (x) { x.classList.toggle('sel', x === b); x.classList.remove('bien', 'mal'); }); };
      return { comprobar: function () { var s = c.querySelector('.lb-chip.sel'); if (!s) return { ok: false, msg: 'Tocá una ficha y después comprobá.' }; var b2 = s.getAttribute('data-ok') === '1'; s.classList.add(b2 ? 'bien' : 'mal'); return b2 ? { ok: true, msg: '¡Bien!' } : { ok: false, msg: t === 'rol' ? 'Mirá en qué fila está y de qué se alimenta.' : 'Seguí las flechas: ¿lo come o es comido por él?' }; },
        resolver: function () { [].forEach.call(c.querySelectorAll('.lb-chip'), function (x) { x.classList.toggle('sel', x.getAttribute('data-ok') === '1'); }); } };
    }); otro(el);
  } };

  // =====================================================================================
  // 5) CLAVE DICOTÓMICA: escalera de preguntas sí / no que se recorre con un organismo
  // =====================================================================================
  var CLAVES = {
    vertebrados: { nombre: 'Vertebrados', q: [['¿Tiene plumas?', 'Aves', '🐦'], ['¿Tiene pelos y toma leche al nacer?', 'Mamíferos', '🐄'], ['¿Tiene aletas y respira por branquias?', 'Peces', '🐟'], ['¿Tiene piel húmeda y sin escamas?', 'Anfibios', '🐸']], resto: ['Reptiles', '🦎'],
      org: [['Hornero', '🐦', 0, 'tiene plumas y pico'], ['Ñandú', '🐦', 0, 'no vuela, pero tiene plumas'], ['Carpincho', '🦫', 1, 'tiene pelos y las crías toman leche'], ['Ballena franca', '🐋', 1, 'vive en el mar, respira con pulmones y amamanta'], ['Dorado', '🐟', 2, 'tiene aletas y branquias'], ['Tiburón', '🦈', 2, 'tiene aletas y branquias'], ['Sapo', '🐸', 3, 'tiene piel húmeda, sin escamas'], ['Salamandra', '🦎', 3, 'tiene piel húmeda y cola'], ['Yacaré', '🐊', 4, 'tiene escamas duras y pone huevos en tierra'], ['Tortuga', '🐢', 4, 'tiene caparazón y escamas']] },
    invertebrados: { nombre: 'Invertebrados', q: [['¿Tiene 6 patas articuladas?', 'Insectos', '🐜'], ['¿Tiene 8 patas articuladas?', 'Arácnidos', '🕷️'], ['¿Tiene 2 pares de antenas y caparazón?', 'Crustáceos', '🦀'], ['¿Tiene muchísimos pares de patas?', 'Miriápodos', '🐛'], ['¿Tiene cuerpo blando con concha o pie musculoso?', 'Moluscos', '🐌'], ['¿Tiene el cuerpo formado por anillos?', 'Anélidos', '🪱']], resto: ['Cnidarios y otros', '🪼'],
      org: [['Hormiga', '🐜', 0, 'tiene 6 patas y antenas'], ['Mariposa', '🦋', 0, 'tiene 6 patas y alas'], ['Araña', '🕷️', 1, 'tiene 8 patas y no tiene antenas'], ['Escorpión', '🦂', 1, 'tiene 8 patas y una cola con aguijón'], ['Cangrejo', '🦀', 2, 'tiene caparazón y dos pares de antenas'], ['Langostino', '🦐', 2, 'tiene caparazón y vive en el agua'], ['Ciempiés', '🐛', 3, 'tiene muchísimos pares de patas'], ['Caracol', '🐌', 4, 'tiene cuerpo blando y concha'], ['Pulpo', '🐙', 4, 'tiene cuerpo blando y tentáculos con ventosas'], ['Lombriz', '🪱', 5, 'tiene el cuerpo en anillos y sin patas'], ['Medusa', '🪼', 6, 'tiene tentáculos urticantes y cuerpo gelatinoso']] },
    plantas: { nombre: 'Plantas', q: [['¿No tiene vasos conductores?', 'Briófitas (musgos)', '🌿'], ['¿Se reproduce por esporas, sin semillas?', 'Pteridófitas (helechos)', '🌱'], ['¿Tiene semillas desnudas, sin fruto?', 'Gimnospermas', '🌲']], resto: ['Angiospermas (con flores y frutos)', '🌸'],
      org: [['Musgo', '🌿', 0, 'no tiene vasos conductores'], ['Helecho', '🌱', 1, 'tiene esporas debajo de las hojas'], ['Pino', '🌲', 2, 'tiene semillas en piñas, sin fruto'], ['Araucaria', '🌲', 2, 'tiene semillas (piñones) en piñas'], ['Ceibo', '🌺', 3, 'tiene flores rojas y frutos'], ['Girasol', '🌻', 3, 'tiene flores y frutos con semillas'], ['Trigo', '🌾', 3, 'tiene flores pequeñas y granos que son frutos']] },
    reinos: { nombre: 'Reinos', q: [['¿Sus células no tienen núcleo?', 'Moneras (bacterias)', '🦠'], ['¿Es unicelular o sin tejidos, con núcleo?', 'Protistas', '🧫'], ['¿Hace fotosíntesis?', 'Plantas', '🌳'], ['¿Se alimenta absorbiendo, con pared de quitina?', 'Hongos', '🍄']], resto: ['Animales', '🐈'],
      org: [['Bacteria del yogur', '🦠', 0, 'células sin núcleo'], ['Paramecio', '🧫', 1, 'una sola célula con núcleo'], ['Ameba', '🧫', 1, 'una sola célula con núcleo que cambia de forma'], ['Ceibo', '🌺', 2, 'muchas células, hace fotosíntesis'], ['Champiñón', '🍄', 3, 'absorbe alimento y tiene quitina'], ['Gato', '🐈', 4, 'muchas células, come otros seres vivos'], ['Lombriz', '🪱', 4, 'muchas células, come restos del suelo']] }
  };
  function clLista(p) { return (p.claves || [p.clave || 'vertebrados']).map(function (k) { return CLAVES[k] || CLAVES.vertebrados; }); }
  function dibClave(K, org, hasta) { var n = K.q.length, b = '', fin = org ? org[2] : -1, H2 = 30 + n * 40 + 40;
    K.q.forEach(function (q, j) { var y = 28 + j * 40, pas = org && j < hasta && j <= fin, si = pas && j === fin, no = pas && j < fin;
      b += rc(8, y - 16, 300, 30, pas ? (si ? '#FFF3C4' : C.claro) : '#fff', pas ? (si ? C.coral : C.teal) : '#cfdedb', 8) + tx(16, y + 4, q[0], { s: 11.5, w: 700 });
      b += fl(308, y - 1, 350, y - 1, si ? C.coral : '#cfdedb', 2) + tx(330, y - 6, 'sí', { a: 'middle', s: 10, c: si ? C.coral : '#9aa' }) + em(366, y - 1, q[2], 18) + txw(380, y + 4, q[1], { s: 11, w: 800, c: si ? C.coral : C.osc }, 13);
      if (j < n - 1) b += fl(40, y + 14, 40, y + 24, no ? C.teal : '#cfdedb', 2) + tx(52, y + 23, 'no', { s: 9.5, c: no ? C.teal : '#9aa' }); });
    var yR = 28 + n * 40, enR = org && fin === n && hasta >= n; b += fl(40, yR - 26, 40, yR - 14, enR ? C.coral : '#cfdedb', 2) + tx(52, yR - 15, 'no', { s: 9.5, c: '#9aa' }) + rc(8, yR - 12, 230, 30, enR ? '#FFF3C4' : '#fff', enR ? C.coral : '#cfdedb', 8) + em(28, yR + 3, K.resto[1], 18) + tx(44, yR + 8, K.resto[0], { s: 11.5, w: 800, c: enR ? C.coral : C.osc });
    return S(470, H2, b); }
  M.clave = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = clLista(p), K0 = L[0];
    escena(el, (L.length > 1 ? sel('k', 'Clave', L.map(function (k, i) { return [i, k.nombre]; }), 0) : '') + sel('o', 'Organismo', K0.org.map(function (o, i) { return [i, o[1] + ' ' + o[0]]; }), 0), function (o) { var K = L[+(o.k || 0)] || K0, org = K.org[+(o.o || 0)] || K.org[0], fin = org[2], P = [];
      P.push({ vis: '<p class="nat-card">' + org[1] + ' <b>' + org[0] + '</b>: ' + org[3] + '.</p>' + dibClave(K, null, 0), txt: 'Vamos a clasificar <b>' + org[0].toLowerCase() + '</b> con la clave: se lee de arriba hacia abajo.' });
      for (var j = 0; j <= Math.min(fin, K.q.length - 1); j++) P.push({ vis: '<p class="nat-card">' + org[1] + ' <b>' + org[0] + '</b>: ' + org[3] + '.</p>' + dibClave(K, org, j + 1), txt: K.q[j][0] + ' <b>' + (j === fin ? 'Sí' : 'No') + '</b>' + (j === fin ? ': es del grupo <b>' + K.q[j][1] + '</b>.' : ': bajamos a la pregunta siguiente.') });
      if (fin >= K.q.length) P.push({ vis: '<p class="nat-card">' + org[1] + ' <b>' + org[0] + '</b>: ' + org[3] + '.</p>' + dibClave(K, org, K.q.length), txt: 'Respondió que no a todas: es del grupo <b>' + K.resto[0] + '</b>.' });
      return P; });
    if (L.length > 1) el.addEventListener('change', function (e) { if (e.target.getAttribute('data-k') !== 'k') return; var K = L[+e.target.value]; el.querySelector('[data-k="o"]').innerHTML = K.org.map(function (o, i) { return '<option value="' + i + '">' + o[1] + ' ' + o[0] + '</option>'; }).join(''); el._pintar(); });
  } };
  M.clave_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = clLista(p), u = { v: -1 }, uo = { v: -1 };
    elegir(el, api, function () { var K = L[rot(L.length, u)], org = K.org[rot(K.org.length, uo)], grupos = K.q.map(function (q) { return q[1]; }).concat(K.resto[0]), ok = grupos[org[2]];
      return { cons: 'Usá la clave para clasificar a <b>' + org[0].toLowerCase() + '</b> ' + org[1] + ': ' + org[3] + '.', html: dibClave(K, null, 0), ops: mezclar(grupos.filter(function (g) { return g !== ok; })).slice(0, 3).concat(ok), ok: ok, ayuda: 'Leé las preguntas de arriba hacia abajo y frená en el primer «sí».', bien: '¡Bien! ' + org[0] + ' es del grupo ' + ok + '.' }; });
  } };

  // =====================================================================================
  // 6) PLATO: el plato recomendado (Guías Alimentarias para la Población Argentina) contra una comida real
  // =====================================================================================
  var GRU = [['Verduras y frutas', '#5BAA3C', 50], ['Legumbres, cereales, papa, pan y pastas', '#F2A541', 25], ['Leche, yogur y quesos', '#8FB8E3', 8], ['Carnes y huevos', '#c2416b', 12], ['Aceites, frutas secas y semillas', '#C29A1E', 5], ['Opcionales (dulces, gaseosas, frituras)', '#9E9E9E', 0]];
  var COMIDAS = [['Guiso de lentejas con verduras y una naranja', [40, 35, 0, 15, 10, 0], 'Muy completo: tiene legumbres, verduras, fruta y algo de carne.'], ['Milanesa con papas fritas y gaseosa', [0, 40, 0, 30, 10, 20], 'Faltan verduras y frutas, y sobran frituras y azúcar: agregar una ensalada y tomar agua.'],
    ['Fideos con manteca', [0, 85, 10, 0, 5, 0], 'Casi todo es un solo grupo: sumar verduras y una porción de carne, huevo o legumbres.'], ['Ensalada completa con pollo y pan integral', [50, 20, 0, 25, 5, 0], 'Muy equilibrada: se parece mucho al plato recomendado.'], ['Pancho con papas fritas y alfajor', [0, 35, 0, 20, 15, 30], 'Muchos ultraprocesados y opcionales: es para alguna vez, no para todos los días.']];
  function torta(cx, cy, rr, vals) { var tot = vals.reduce(function (a, b) { return a + b; }, 0), a0 = -Math.PI / 2, s = '';
    vals.forEach(function (v, i) { if (!v) return; var a1 = a0 + v / tot * 2 * Math.PI, big = a1 - a0 > Math.PI ? 1 : 0; s += v === tot ? ci(cx, cy, rr, GRU[i][1], '#fff') : '<path d="M' + cx + ',' + cy + ' L' + r1(cx + rr * Math.cos(a0)) + ',' + r1(cy + rr * Math.sin(a0)) + ' A' + rr + ',' + rr + ' 0 ' + big + ' 1 ' + r1(cx + rr * Math.cos(a1)) + ',' + r1(cy + rr * Math.sin(a1)) + ' Z" fill="' + GRU[i][1] + '" stroke="#fff" stroke-width="2"/>'; a0 = a1; });
    return ci(cx, cy, rr + 8, '#fff', '#cfdedb') + s; }
  function leyenda(vals, x, y) { return vals.map(function (v, i) { return v ? rc(x, y + i * 18 - 10, 12, 12, GRU[i][1], null, 3) + tx(x + 18, y + i * 18, GRU[i][0] + ' (' + v + ' %)', { s: 10.5, w: 700 }) : ''; }).join(''); }
  M.plato = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = p.items && p.items.length ? p.items : COMIDAS;
    escena(el, sel('i', 'Comida', L.map(function (c, i) { return [i, c[0]]; }), 0), function (o) { var cm = L[+(o.i || 0)] || L[0], rec = GRU.map(function (g) { return g[2]; }), P = [];
      P.push({ vis: S(470, 200, torta(95, 100, 80, rec) + leyenda(rec, 200, 40)), txt: 'El <b>plato recomendado</b>: la mitad, verduras y frutas; un cuarto, cereales y legumbres; el resto, proteínas, lácteos y un poco de aceite.' });
      P.push({ vis: S(470, 200, torta(95, 100, 80, cm[1]) + leyenda(cm[1], 200, 40)), txt: 'El plato de <b>' + cm[0].toLowerCase() + '</b>, repartido por grupos de alimentos.' });
      var barras = GRU.map(function (g, i) { var y = 22 + i * 30, a = rec[i] * 3, bb = cm[1][i] * 3; return tx(150, y + 8, g[0].replace(/,.*$/, '').replace(/ \(.*$/, ''), { a: 'end', s: 10.5, w: 700 }) + rc(158, y - 4, a, 9, '#cfdedb', null, 3) + rc(158, y + 6, bb, 9, g[1], null, 3) + tx(166 + Math.max(a, bb), y + 9, (cm[1][i] - rec[i] > 0 ? '+' : '') + (cm[1][i] - rec[i]), { s: 10, c: cm[1][i] < rec[i] ? C.rosa : C.osc, w: 800 }); }).join('');
      P.push({ vis: S(470, 200, barras + tx(158, 196, '▬ gris: recomendado · ▬ color: este plato', { s: 10 })), txt: 'Comparamos grupo por grupo: los números en rojo muestran lo que <b>falta</b>.' });
      P.push({ vis: '<p class="nat-card">🍽️ ' + cm[2] + '</p>', txt: 'Conclusión: ' + cm[2] });
      return P; });
  } };
  var ALIM = [['manzana', 0], ['zanahoria', 0], ['acelga', 0], ['banana', 0], ['tomate', 0], ['lentejas', 1], ['arroz', 1], ['pan', 1], ['fideos', 1], ['papa', 1], ['leche', 2], ['yogur', 2], ['queso', 2], ['pollo', 3], ['huevo', 3], ['carne vacuna', 3], ['pescado', 3], ['aceite de girasol', 4], ['nueces', 4], ['semillas de chía', 4], ['gaseosa', 5], ['caramelos', 5], ['papas fritas de paquete', 5]];
  M.plato_x = { tipo: 'ejercicio', render: function (el, p, api) { var cuantos = p.cuantos || 6;
    cajas(el, api, function () { var g = mezclar([0, 1, 2, 3, 4, 5]).slice(0, 3).sort(), it = mezclar(ALIM.filter(function (a) { return g.indexOf(a[1]) >= 0; })).slice(0, cuantos);
      return { tit: 'Ubicá cada alimento en su grupo.', cajas: g.map(function (k) { return GRU[k][0]; }), items: it.map(function (a, i) { return { v: 'a' + i, t: a[0], c: g.indexOf(a[1]) }; }) }; }); otro(el);
  } };

  // =====================================================================================
  // 7) ÓSMOSIS: membrana con partículas y la célula que se hincha o se arruga
  // =====================================================================================
  var MEDIOS = [['Agua destilada', 0, 'hipotónico'], ['Suero fisiológico', 9, 'isotónico'], ['Agua muy salada', 30, 'hipertónico']];
  function puntos(x, y, w, h, n, seed, col) { var s = ''; for (var i = 0; i < n; i++) { var a = (i * 97 + seed * 31) % 100 / 100, bb = (i * 53 + seed * 17) % 100 / 100; s += ci(x + 6 + a * (w - 12), y + 6 + bb * (h - 12), 3.2, col || C.coral); } return s; }
  function celulaOs(cx, cy, tipo, estado) { var esc = estado === 'hinchada' ? 1.25 : estado === 'arrugada' ? 0.7 : 1;
    if (tipo === 'vegetal') { var w = 70, h = 70; return rc(cx - 40, cy - 40, 80, 80, '#E8F5E9', C.verde, 10, ' stroke-width="6"') + (estado === 'arrugada' ? '<path d="M' + (cx - 22) + ',' + (cy - 20) + ' q22,-14 44,0 q12,22 0,40 q-22,12 -44,0 q-10,-20 0,-40" fill="#D6EEF8" stroke="#2a7ab8" stroke-width="2"/>' : rc(cx - 34 * (estado === 'hinchada' ? 1 : .95), cy - 34 * (estado === 'hinchada' ? 1 : .95), 68 * (estado === 'hinchada' ? 1 : .95), 68 * (estado === 'hinchada' ? 1 : .95), '#D6EEF8', '#2a7ab8', 12)); }
    return estado === 'arrugada' ? '<path d="M' + (cx - 30) + ',' + cy + ' q8,-22 18,-8 q8,-20 18,-4 q12,-10 14,8 q14,10 0,16 q4,18 -16,12 q-10,14 -20,0 q-20,4 -14,-24" fill="#FCE4EC" stroke="#c2416b" stroke-width="3"/>' : '<ellipse cx="' + cx + '" cy="' + cy + '" rx="' + r1(36 * esc) + '" ry="' + r1(30 * esc) + '" fill="#FCE4EC" stroke="#c2416b" stroke-width="3"' + (estado === 'hinchada' ? ' stroke-dasharray="6 3"' : '') + '/>'; }
  function resOs(medio, tipo) { return medio === 0 ? (tipo === 'vegetal' ? ['hinchada', 'turgente: la pared resiste y la célula queda firme'] : ['hinchada', 'se hincha y puede romperse (lisis)']) : medio === 2 ? (tipo === 'vegetal' ? ['arrugada', 'plasmólisis: la membrana se separa de la pared'] : ['arrugada', 'se arruga y se achica (crenación)']) : ['normal', 'queda igual: entra y sale la misma cantidad de agua']; }
  M.osmosis = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Medio', MEDIOS.map(function (m, i) { return [i, m[0]]; }), 0) + sel('t', 'Célula', [['animal', 'Animal (glóbulo rojo)'], ['vegetal', 'Vegetal']], p.celula || 'animal'), function (o) { var m = +(o.m || 0), t = o.t || 'animal', md = MEDIOS[m], adentro = 9, res = resOs(m, t), P = [];
      var tubo = function (fl2) { return rc(20, 30, 200, 120, '#EAF6FB', C.azul, 8) + rc(250, 30, 200, 120, '#EAF6FB', C.azul, 8) + '<line x1="235" y1="24" x2="235" y2="156" stroke="#7a3fa0" stroke-width="5" stroke-dasharray="10 5"/>' + puntos(20, 30, 200, 120, Math.round(md[1] * 1.4), 1) + puntos(250, 30, 200, 120, Math.round(adentro * 1.4), 2) + tx(120, 172, 'Afuera: ' + md[0].toLowerCase(), { a: 'middle', s: 11.5, w: 800 }) + tx(350, 172, 'Adentro de la célula', { a: 'middle', s: 11.5, w: 800 }) + tx(235, 18, 'membrana', { a: 'middle', s: 10, c: C.lila, w: 800 }) + (fl2 || ''); };
      P.push({ vis: S(470, 180, tubo()), txt: 'Contamos las partículas de sal (puntos): afuera hay ' + (md[1] < adentro ? 'menos' : md[1] > adentro ? 'más' : 'la misma cantidad') + ' que adentro. El medio es <b>' + md[2] + '</b>.' });
      var dir = md[1] < adentro ? fl(160, 90, 310, 90, C.azul, 5) + tx(235, 80, 'agua →', { a: 'middle', s: 12, c: C.azul, w: 900 }) : md[1] > adentro ? fl(310, 90, 160, 90, C.azul, 5) + tx(235, 80, '← agua', { a: 'middle', s: 12, c: C.azul, w: 900 }) : fl(170, 80, 300, 80, C.azul, 3) + fl(300, 100, 170, 100, C.azul, 3);
      P.push({ vis: S(470, 180, tubo(dir)), txt: 'La sal no atraviesa la membrana, pero el <b>agua sí</b>: pasa hacia donde hay más partículas disueltas. Eso es la <b>ósmosis</b>.' });
      P.push({ vis: S(470, 180, celulaOs(120, 90, t, 'normal') + tx(120, 172, 'antes', { a: 'middle', s: 12, w: 800 }) + fl(200, 90, 270, 90, C.osc, 3) + celulaOs(350, 90, t, res[0]) + tx(350, 172, 'después', { a: 'middle', s: 12, w: 800 })), txt: 'Resultado en la célula ' + t + ': ' + res[1] + '.' });
      return P; });
  } };
  M.osmosis_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    elegir(el, api, function () { var k = rot(6, u), m = k % 3, t = k < 3 ? 'animal' : 'vegetal', res = resOs(m, t), opsA = ['Se hincha y puede romperse', 'Se arruga y se achica', 'Queda igual'], opsV = ['Queda turgente', 'Sufre plasmólisis', 'Queda igual'], ops = t === 'animal' ? opsA : opsV, ok = ops[m === 0 ? 0 : m === 2 ? 1 : 2];
      return { cons: 'Una célula <b>' + t + '</b> se coloca en <b>' + MEDIOS[m][0].toLowerCase() + '</b> (medio ' + MEDIOS[m][2] + '). ¿Qué le pasa?', html: S(470, 120, celulaOs(110, 60, t, 'normal') + rc(240, 10, 200, 100, '#EAF6FB', C.azul, 8) + puntos(240, 10, 200, 100, Math.round(MEDIOS[m][1] * 1.4), 3) + tx(340, 118, MEDIOS[m][0], { a: 'middle', s: 11, w: 800 })), ops: ops, ok: ok, ayuda: 'El agua pasa hacia donde hay más partículas disueltas.', bien: '¡Bien! ' + res[1][0].toUpperCase() + res[1].slice(1) + '.' }; });
  } };

  // =====================================================================================
  // 8) ENZIMA: llave y cerradura, y actividad según la temperatura (o el pH)
  // =====================================================================================
  var ENZ = [['Amilasa de la saliva', 37, 'T', 'almidón'], ['Pepsina del estómago', 2, 'pH', 'proteínas'], ['Enzima de una bacteria de aguas termales', 75, 'T', 'grasas']];
  function actividad(x, opt, tipo) { var a = tipo === 'pH' ? Math.exp(-Math.pow((x - opt) / 1.6, 2)) : (x <= opt ? Math.exp(-Math.pow((x - opt) / (opt * 0.55 + 6), 2)) : Math.max(0, 1 - Math.pow((x - opt) / 12, 2))); return Math.max(0, Math.round(a * 100)); }
  function enzDib(fase, deformada) { var e = deformada ? '<path d="M120,60 q30,-26 70,-4 q34,20 10,52 q-30,24 -66,8 q-30,-20 -14,-56" fill="#B39DDB" stroke="#7a3fa0" stroke-width="3"/>' : '<path d="M110,50 L230,50 L230,120 L110,120 L110,95 L140,95 L150,85 L160,95 L190,95 L190,50" fill="#B39DDB" stroke="#7a3fa0" stroke-width="3" transform="translate(0,0)"/>';
    var sus = '<path d="M140,95 L150,85 L160,95 L190,95 L190,82 L140,82 Z" fill="#F5D33B" stroke="#C29A1E" stroke-width="2"/>';
    var s = rc(0, 0, 0, 0) + e;
    if (fase === 0) s += '<g transform="translate(120,-60)">' + sus + '</g>' + tx(285, 32, 'sustrato', { s: 11, w: 800 });
    if (fase === 1) s += '<g transform="translate(0,-2)">' + sus + '</g>' + tx(165, 140, 'complejo enzima-sustrato', { a: 'middle', s: 11, w: 800 });
    if (fase === 2) s += '<g transform="translate(110,-62)"><path d="M140,95 L150,85 L160,95 L163,95 L163,82 L140,82 Z" fill="#F5D33B" stroke="#C29A1E" stroke-width="2"/></g><g transform="translate(150,-40)"><path d="M167,95 L190,95 L190,82 L167,82 Z" fill="#F5D33B" stroke="#C29A1E" stroke-width="2"/></g>' + tx(320, 64, 'productos', { s: 11, w: 800 });
    return s + tx(170, 135 + (fase === 1 ? 20 : 0), deformada ? 'enzima desnaturalizada: ya no encaja' : 'enzima', { a: 'middle', s: 11, w: 800, c: C.lila }); }
  M.enzima = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = p.items || ENZ;
    escena(el, sel('i', 'Enzima', L.map(function (z, i) { return [i, z[0]]; }), 0) + ctrl('x', 'Temperatura (°C)', 0, 100, 1, 37) + ctrl('ph', 'pH (para la pepsina)', 0, 14, 0.5, 2), function (o) { var z = L[+(o.i || 0)] || L[0], tipo = z[2], x = tipo === 'pH' ? (o.ph == null ? 2 : o.ph) : o.x, a = actividad(x, z[1], tipo), P = [], u = tipo === 'pH' ? '' : ' °C', nom = tipo === 'pH' ? 'pH ' + fmt(x) : fmt(x) + u;
      P.push({ vis: S(470, 160, enzDib(0)), txt: 'La <b>enzima</b> tiene un <b>sitio activo</b> con una forma justa, donde encaja su sustrato (' + z[3] + '): como una llave en su cerradura.' });
      P.push({ vis: S(470, 165, enzDib(1)), txt: 'El sustrato encaja y se forma el <b>complejo enzima-sustrato</b>.' });
      P.push({ vis: S(470, 160, enzDib(2)), txt: 'La reacción ocurre mucho más rápido y salen los <b>productos</b>. La enzima queda libre y se vuelve a usar.' });
      var g = '', W = 380, x0 = 60, y0 = 170, maxX = tipo === 'pH' ? 14 : 100; g += ln(x0, y0, x0 + W, y0) + ln(x0, y0, x0, 20) + tx(x0 + W, y0 + 18, tipo === 'pH' ? 'pH' : 'temperatura (°C)', { a: 'end', s: 11 }) + tx(x0 - 6, 24, 'actividad', { a: 'end', s: 11 });
      var pts = []; for (var t = 0; t <= maxX; t += maxX / 60) pts.push(r1(x0 + t / maxX * W) + ',' + r1(y0 - actividad(t, z[1], tipo) * 1.4)); g += '<polyline points="' + pts.join(' ') + '" fill="none" stroke="' + C.teal + '" stroke-width="3"/>';
      g += ln(x0 + z[1] / maxX * W, y0, x0 + z[1] / maxX * W, y0 - 140, C.sol, 1.5, ' stroke-dasharray="4 3"') + tx(x0 + z[1] / maxX * W, y0 - 146, 'óptimo: ' + (tipo === 'pH' ? 'pH ' + z[1] : z[1] + ' °C'), { a: 'middle', s: 10.5, c: C.sol, w: 800 }) + ci(x0 + x / maxX * W, y0 - a * 1.4, 6, C.coral);
      P.push({ vis: S(470, 200, g), txt: 'Cada enzima trabaja mejor en su <b>óptimo</b>. Con ' + nom + ', la actividad es del <b>' + a + ' %</b>.' });
      var desn = tipo === 'T' ? x > z[1] + 10 : Math.abs(x - z[1]) > 3;
      P.push({ vis: S(470, 160, enzDib(desn ? 3 : 1, desn)), txt: desn ? 'Lejos del óptimo, la enzima se <b>desnaturaliza</b>: cambia de forma, el sustrato ya no encaja y deja de funcionar.' : (tipo === 'T' && x < z[1] - 10 ? 'Con frío, las moléculas se mueven poco: la enzima sigue sana, pero trabaja lento.' : 'Cerca del óptimo, la enzima conserva su forma y trabaja bien.') });
      return P; });
  } };
  M.enzima_x = { tipo: 'ejercicio', render: function (el, p, api) {
    elegir(el, api, function () { var z = pick(ENZ), tipo = z[2], x = tipo === 'pH' ? pick([1, 2, 3, 7, 9, 12]) : pick([5, 20, z[1], z[1] + 3, z[1] + 25, 95].filter(function (v) { return v <= 100; })), a = actividad(x, z[1], tipo), desn = tipo === 'T' ? x > z[1] + 10 : Math.abs(x - z[1]) > 3,
        ok = desn ? 'Casi nula: se desnaturalizó' : a >= 70 ? 'Alta: está cerca de su óptimo' : 'Baja, pero la enzima no se dañó';
      return { cons: 'La <b>' + z[0].toLowerCase() + '</b> tiene su óptimo en ' + (tipo === 'pH' ? 'pH ' + z[1] : z[1] + ' °C') + '. ¿Cómo es su actividad con ' + (tipo === 'pH' ? 'pH ' + x : x + ' °C') + '?', ops: ['Alta: está cerca de su óptimo', 'Baja, pero la enzima no se dañó', 'Casi nula: se desnaturalizó'], ok: ok, ayuda: 'Por encima del óptimo (o con un pH muy distinto) la enzima cambia de forma; con frío solo se vuelve lenta.' }; });
  } };

  // =====================================================================================
  // 9) PUNNETT: cruzamientos con gametos, cuadro y proporciones (dominancia completa, incompleta, grupos sanguíneos, ligado al X)
  // =====================================================================================
  var RASGOS = {
    arveja: { nombre: 'Color de la semilla de arveja (Mendel)', gen: ['AA', 'Aa', 'aa'], fen: function (g) { return /A/.test(g) ? 'amarilla' : 'verde'; }, expl: 'A (amarilla) domina sobre a (verde).' },
    flor: { nombre: 'Color de la flor de boca de dragón', gen: ['RR', 'RB', 'BB'], fen: function (g) { return g === 'RR' ? 'roja' : g === 'BB' ? 'blanca' : 'rosada'; }, expl: 'Dominancia incompleta: R (roja) y B (blanca) juntas dan rosada.' },
    grupo: { nombre: 'Grupo sanguíneo (ABO)', gen: ['AA', 'AO', 'BB', 'BO', 'AB', 'OO'], fen: function (g) { return g === 'AB' ? 'grupo AB' : /A/.test(g) ? 'grupo A' : /B/.test(g) ? 'grupo B' : 'grupo 0'; }, expl: 'A y B son codominantes; los dos dominan sobre O.' },
    daltonismo: { nombre: 'Daltonismo (ligado al cromosoma X)', gen: ['XᴰXᴰ', 'XᴰXᵈ', 'XᵈXᵈ'], gen2: ['XᴰY', 'XᵈY'], fen: function (g) { var muj = !/Y/.test(g); return (muj ? 'mujer ' : 'varón ') + (muj ? (/ᴰ/.test(g) ? (/ᵈ/.test(g) ? 'portadora' : 'visión normal') : 'daltónica') : (/ᴰ/.test(g) ? 'visión normal' : 'daltónico')); }, expl: 'El gen está en el X: los varones tienen un solo X.' }
  };
  function alelos(g) { return /X/.test(g) ? g.match(/X[ᴰᵈ]|Y/g) : g.split(''); }
  function unir(a, b, rasgo) { var L = [a, b]; if (rasgo === 'daltonismo') L.sort(function (x, y) { return x === 'Y' ? 1 : y === 'Y' ? -1 : (x < y ? -1 : 1); }); else if (rasgo === 'grupo') L.sort(function (x, y) { return 'ABO'.indexOf(x) - 'ABO'.indexOf(y); }); else if (rasgo === 'flor') L.sort(function (x, y) { return 'RB'.indexOf(x) - 'RB'.indexOf(y); }); else L.sort(function (x, y) { return x.toLowerCase() === y.toLowerCase() ? (x < y ? -1 : 1) : 0; }); return L.join(''); }
  function cuadro(ga, gb, celdas, hasta) { var b = '', x0 = 150, y0 = 40, s = 70;
    ga.forEach(function (g, i) { b += ci(x0 + s * i + s / 2, y0 - 18, 15, '#E1D5F5', C.lila) + tx(x0 + s * i + s / 2, y0 - 13, g, { a: 'middle', s: 13, w: 900 }); });
    gb.forEach(function (g, j) { b += ci(x0 - 22, y0 + s * j + s / 2, 15, '#FFF3C4', C.sol) + tx(x0 - 22, y0 + s * j + s / 2 + 5, g, { a: 'middle', s: 13, w: 900 }); });
    for (var j = 0; j < gb.length; j++) for (var i = 0; i < ga.length; i++) { var k = j * ga.length + i; b += rc(x0 + s * i, y0 + s * j, s, s, k < hasta ? C.claro : '#fff', C.teal, 4) + (k < hasta ? tx(x0 + s * i + s / 2, y0 + s * j + s / 2 + 5, celdas[k], { a: 'middle', s: 15, w: 900 }) : ''); }
    return b; }
  M.punnett = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var key = RASGOS[p.rasgo] ? p.rasgo : 'arveja', Rg = RASGOS[key], g2 = Rg.gen2 || Rg.gen;
    escena(el, sel('a', key === 'daltonismo' ? 'Madre' : 'Progenitor 1', Rg.gen.map(function (g) { return [g, g + ' · ' + Rg.fen(g)]; }), Rg.gen[1]) + sel('b', key === 'daltonismo' ? 'Padre' : 'Progenitor 2', g2.map(function (g) { return [g, g + ' · ' + Rg.fen(g)]; }), g2[key === 'daltonismo' ? 0 : 1]), function (o) {
      var A = o.a || Rg.gen[1], Bq = o.b || g2[0], ga = alelos(A), gb = alelos(Bq), cel = [], P = [];
      gb.forEach(function (y) { ga.forEach(function (x) { cel.push(unir(x, y, key)); }); });
      P.push({ vis: '<p class="nat-card">' + Rg.expl + '</p>' + S(470, 60, tx(120, 30, A, { a: 'middle', s: 22, w: 900 }) + tx(120, 50, Rg.fen(A), { a: 'middle', s: 11 }) + tx(235, 34, '×', { a: 'middle', s: 22 }) + tx(350, 30, Bq, { a: 'middle', s: 22, w: 900 }) + tx(350, 50, Rg.fen(Bq), { a: 'middle', s: 11 })), txt: 'Cruzamos <b>' + A + '</b> con <b>' + Bq + '</b>. Cada letra es un <b>alelo</b>: uno viene de cada progenitor.' });
      P.push({ vis: S(470, 200, cuadro(ga, gb, cel, 0)), txt: 'Cada progenitor forma <b>gametos</b> con un solo alelo: ' + ga.join(' y ') + ' de un lado; ' + gb.join(' y ') + ' del otro.' });
      P.push({ vis: S(470, 200, cuadro(ga, gb, cel, 4)), txt: 'Combinamos cada gameto con cada gameto: el <b>cuadro de Punnett</b> muestra los 4 hijos posibles, igual de probables.' });
      var cuenta = {}; cel.forEach(function (g) { cuenta[g] = (cuenta[g] || 0) + 1; });
      P.push({ vis: S(470, 200, cuadro(ga, gb, cel, 4)), txt: '<b>Genotipos</b>: ' + Object.keys(cuenta).map(function (g) { return g + ' ' + cuenta[g] * 25 + ' %'; }).join(' · ') + '.' });
      var cf = {}; cel.forEach(function (g) { var f = Rg.fen(g); cf[f] = (cf[f] || 0) + 1; });
      var nf = Object.keys(cf).length, wf = Math.min(140, 440 / nf - 8), x0f = 235 - nf * (wf + 8) / 2;
      P.push({ vis: S(470, 80, Object.keys(cf).map(function (f, i) { var x = x0f + i * (wf + 8); return rc(x, 10, wf, 58, C.claro, C.teal, 10) + tx(x + wf / 2, 34, cf[f] * 25 + ' %', { a: 'middle', s: 16, w: 900 }) + txw(x + wf / 2, 58, f, { a: 'middle', s: 10.5, w: 700 }, 12); }).join('')), txt: '<b>Fenotipos</b> (lo que se ve): ' + Object.keys(cf).map(function (f) { return cf[f] * 25 + ' % ' + f; }).join(', ') + '.' });
      return P; });
  } };
  M.punnett_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = (p.rasgos || [p.rasgo || 'arveja']).filter(function (k) { return RASGOS[k]; });
    respuesta(el, api, function () { var key = pick(L.length ? L : ['arveja']), Rg = RASGOS[key], A = pick(Rg.gen), Bq = pick(Rg.gen2 || Rg.gen), cel = []; alelos(Bq).forEach(function (y) { alelos(A).forEach(function (x) { cel.push(unir(x, y, key)); }); });
      var f = Rg.fen(pick(cel)), v = cel.filter(function (g) { return Rg.fen(g) === f; }).length * 25;
      return { cons: Rg.nombre + '. ' + Rg.expl + ' Se cruzan <b>' + A + '</b> × <b>' + Bq + '</b>. ¿Qué porcentaje de los hijos será <b>' + f + '</b>?', campos: [{ lab: 'Porcentaje', v: v, un: '%' }], ayuda: 'Armá el cuadro de Punnett: cada casillero vale 25 %.', bien: '¡Bien! ' + v + ' % de los hijos: ' + f + '.' }; });
  } };

  // =====================================================================================
  // 10) ADN: cadena complementaria, ARN mensajero, codones, aminoácidos y mutaciones
  // =====================================================================================
  var COD = (function () { var b = 'UCAG', aa = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG', o = {}, k = 0; for (var i = 0; i < 4; i++) for (var j = 0; j < 4; j++) for (var l = 0; l < 4; l++) o[b[i] + b[j] + b[l]] = aa[k++]; return o; })();
  var AAN = { F: 'Fen', L: 'Leu', S: 'Ser', Y: 'Tir', '*': 'STOP', C: 'Cis', W: 'Trp', P: 'Pro', H: 'His', Q: 'Gln', R: 'Arg', I: 'Ile', M: 'Met', T: 'Tre', N: 'Asn', K: 'Lis', V: 'Val', A: 'Ala', D: 'Asp', E: 'Glu', G: 'Gli' };
  var COMP = { A: 'T', T: 'A', C: 'G', G: 'C' }, ARN = { A: 'U', T: 'A', C: 'G', G: 'C' };
  var BCOL = { A: '#E07A2F', T: '#2a7ab8', U: '#7a3fa0', C: '#3c8d2f', G: '#c2416b' };
  function base(x, y, l, on) { return rc(x - 13, y - 13, 26, 26, on === false ? '#eee' : BCOL[l], null, 6) + tx(x, y + 5, l, { a: 'middle', s: 14, w: 900, c: '#fff' }); }
  function hebra(s, y, x0, hasta, marcaIdx) { return s.split('').map(function (l, i) { return i < hasta ? base(x0 + i * 32, y, l) + (i === marcaIdx ? ci(x0 + i * 32, y, 18, 'none', C.osc, ' stroke-width="3"') : '') : ''; }).join(''); }
  M.adn = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var modos = [['replicacion', 'Replicación (copia del ADN)'], ['transcripcion', 'Transcripción y traducción'], ['mutacion', 'Mutación puntual']];
    escena(el, '<div class="lb-fila"><label>ADN molde (A, T, C, G)</label><input type="text" data-k="s" class="lb-inp largo" value="' + (p.secuencia || 'TACGGATTC') + '" maxlength="12" style="text-transform:uppercase"></div>' + sel('m', 'Qué hacemos', p.modo ? modos.filter(function (q) { return q[0] === p.modo; }) : modos, p.modo || 'transcripcion') + ctrl('pos', 'Posición de la mutación', 1, 12, 1, 5), function (o) {
      var s = String(o.s || '').toUpperCase().replace(/[^ATCG]/g, ''); if (s.length < 3) s = 'TACGGATTC'; s = s.slice(0, Math.floor(Math.min(12, s.length) / 3) * 3); var n = s.length, x0 = 235 - (n - 1) * 16, P = [], m = o.m || 'transcripcion';
      if (m === 'replicacion') { var c = s.split('').map(function (l) { return COMP[l]; }).join('');
        P.push({ vis: S(470, 120, hebra(s, 30, x0, n) + tx(x0 - 22, 35, 'molde', { a: 'end', s: 10 })), txt: 'Una cadena de ADN es una secuencia de bases: <b>A, T, C y G</b>.' });
        P.push({ vis: S(470, 120, hebra(s, 30, x0, n) + hebra(c, 86, x0, Math.ceil(n / 2)) + s.split('').map(function (l, i) { return i < Math.ceil(n / 2) ? ln(x0 + i * 32, 44, x0 + i * 32, 72, '#bbb', 2) : ''; }).join('')), txt: 'La cadena nueva se arma con bases <b>complementarias</b>: A con T, C con G.' });
        P.push({ vis: S(470, 120, hebra(s, 30, x0, n) + hebra(c, 86, x0, n) + s.split('').map(function (l, i) { return ln(x0 + i * 32, 44, x0 + i * 32, 72, '#bbb', 2); }).join('')), txt: 'Cadena complementaria: <b>' + c + '</b>. Así cada célula hija recibe una copia exacta del ADN.' });
        return P; }
      var ar = s.split('').map(function (l) { return ARN[l]; }).join(''), cods = ar.match(/.../g), aas = cods.map(function (q) { return AAN[COD[q]]; });
      if (m === 'mutacion') { var k = Math.min(n, o.pos || 5) - 1, nueva = { A: 'G', G: 'A', T: 'C', C: 'T' }[s[k]], s2 = s.slice(0, k) + nueva + s.slice(k + 1), ar2 = s2.split('').map(function (l) { return ARN[l]; }).join(''), cods2 = ar2.match(/.../g), aas2 = cods2.map(function (q) { return AAN[COD[q]]; }), ci3 = Math.floor(k / 3);
        var cmp = function (A1, A2) { return A1.map(function (a, i) { return rc(x0 - 16 + i * 96, 0, 92, 26, A1 === A2 || a === A2[i] ? C.claro : '#FFF3C4', C.teal, 8) + tx(x0 + 30 + i * 96, 18, a, { a: 'middle', s: 12, w: 900 }); }).join(''); };
        P.push({ vis: S(470, 90, hebra(s, 24, x0, n) + '<g transform="translate(0,52)">' + cmp(aas, aas) + '</g>'), txt: 'ADN original y su proteína: <b>' + aas.join(' – ') + '</b>.' });
        P.push({ vis: S(470, 90, hebra(s2, 24, x0, n, k) + '<g transform="translate(0,52)">' + cmp(aas, aas) + '</g>'), txt: 'Una <b>mutación puntual</b> cambia una sola base: en la posición ' + (k + 1) + ', ' + s[k] + ' pasa a ' + nueva + '.' });
        var tipoM = aas2[ci3] === aas[ci3] ? 'silenciosa: el aminoácido no cambia, porque varios codones dan el mismo' : aas2[ci3] === 'STOP' ? 'sin sentido: aparece un STOP y la proteína queda cortada' : 'de cambio de sentido: cambia un aminoácido (' + aas[ci3] + ' → ' + aas2[ci3] + ')';
        P.push({ vis: S(470, 90, hebra(s2, 24, x0, n, k) + '<g transform="translate(0,52)">' + cmp(aas2, aas) + '</g>'), txt: 'Proteína nueva: <b>' + aas2.join(' – ') + '</b>. La mutación es ' + tipoM + '.' });
        return P; }
      P.push({ vis: S(470, 130, hebra(s, 30, x0, n) + tx(x0 - 22, 35, 'ADN', { a: 'end', s: 10 })), txt: 'Partimos de la cadena molde de ADN, dentro del núcleo.' });
      P.push({ vis: S(470, 130, hebra(s, 30, x0, n) + hebra(ar, 86, x0, n) + tx(x0 - 22, 91, 'ARNm', { a: 'end', s: 10 })), txt: '<b>Transcripción</b>: se copia en ARN mensajero. Es complementario, pero en el ARN la <b>U</b> reemplaza a la T.' });
      P.push({ vis: S(470, 130, hebra(ar, 40, x0, n) + cods.map(function (q, i) { return rc(x0 - 15 + i * 96, 22, 94, 36, 'none', C.osc, 10, ' stroke-dasharray="5 3"'); }).join('')), txt: 'El ARNm sale al citoplasma. El ribosoma lo lee de a tres bases: cada trío es un <b>codón</b> (' + cods.join(', ') + ').' });
      P.push({ vis: S(470, 130, hebra(ar, 40, x0, n) + cods.map(function (q, i) { return rc(x0 - 15 + i * 96, 22, 94, 36, 'none', C.osc, 10, ' stroke-dasharray="5 3"') + ci(x0 + 32 + i * 96, 98, 20, aas[i] === 'STOP' ? '#ddd' : '#FFF3C4', C.sol) + tx(x0 + 32 + i * 96, 103, aas[i], { a: 'middle', s: 12, w: 900 }) + (i ? ln(x0 - 44 + i * 96 + 32, 98, x0 + 12 + i * 96, 98, C.sol, 3) : ''); }).join('')), txt: '<b>Traducción</b>: cada codón corresponde a un aminoácido. Proteína: <b>' + aas.join(' – ') + '</b>.' });
      return P; });
    function verPos() { var m = el.querySelector('[data-k="m"]'), c = el.querySelector('[data-k="pos"]'); if (m && c) c.closest('label').style.display = m.value === 'mutacion' ? '' : 'none'; }
    el.addEventListener('input', verPos); verPos();
  } };
  M.adn_x = { tipo: 'ejercicio', render: function (el, p, api) { var tipos = p.que ? [].concat(p.que) : ['complementaria', 'arn', 'aminoacido'], u = { v: -1 };
    respuesta(el, api, function () { var t = tipos[rot(tipos.length, u)], s = ''; for (var i = 0; i < 6; i++) s += pick('ATCG'.split(''));
      if (t === 'complementaria') { var c = s.split('').map(function (l) { return COMP[l]; }).join(''); return { cons: 'Escribí la cadena de ADN complementaria de <b>' + s + '</b>.', campos: [{ tipo: 'texto', lab: 'Cadena nueva', v: [c] }], ayuda: 'A se une con T y C con G.', bien: '¡Bien! ' + s + ' → ' + c + '.' }; }
      if (t === 'arn') { var a = s.split('').map(function (l) { return ARN[l]; }).join(''); return { cons: 'Transcribí a ARN mensajero el ADN molde <b>' + s + '</b>.', campos: [{ tipo: 'texto', lab: 'ARNm', v: [a] }], ayuda: 'Es complementario, pero frente a una A va U (no T).', bien: '¡Bien! ' + s + ' → ' + a + '.' }; }
      var q; do { q = ''; for (i = 0; i < 3; i++) q += pick('UCAG'.split('')); } while (COD[q] === '*'); var nm = AAN[COD[q]], tabla = Object.keys(COD).filter(function (k) { return COD[k] === COD[q] || Math.random() < 0.08; }).slice(0, 8);
      if (tabla.indexOf(q) < 0) tabla.push(q);
      return { cons: 'Con esta parte del código genético, ¿qué aminoácido corresponde al codón <b>' + q + '</b>? Escribí su abreviatura.', html: '<p class="nat-card">' + mezclar(tabla).map(function (k) { return k + ' → ' + AAN[COD[k]]; }).join(' · ') + '</p>', campos: [{ tipo: 'texto', lab: 'Aminoácido', v: [nm] }], ayuda: 'Buscá el codón exacto en la tabla.', bien: '¡Bien! ' + q + ' → ' + nm + '.' }; });
  } };

  // =====================================================================================
  // 11) MITOSIS Y MEIOSIS: los cromosomas dibujados fase por fase
  // =====================================================================================
  var CCOL = [['#c2416b', '#2a7ab8'], ['#E07A2F', '#3c8d2f'], ['#7a3fa0', '#C29A1E']];
  function crom(x, y, l, col, doble, cruz) { var s = ''; if (doble) { s += rc(x - 6, y - l / 2, 5, l, col, null, 2.5) + rc(x + 1, y - l / 2, 5, l, cruz || col, null, 2.5) + ci(x, y, 3.5, C.osc); } else s += rc(x - 2.5, y - l / 2, 5, l, col, null, 2.5) + ci(x, y, 3, C.osc); return s; }
  function celM(cx, cy, rr, cont, huso) { var h = ''; if (huso) { h = ln(cx, cy - rr + 6, cx, cy + rr - 6, '#bbb', 1.5, ' stroke-dasharray="4 4"') + ci(cx - rr + 10, cy, 4, C.osc) + ci(cx + rr - 10, cy, 4, C.osc); for (var k = -2; k <= 2; k++) h += ln(cx - rr + 10, cy, cx, cy + k * 26, '#ddd', 1) + ln(cx + rr - 10, cy, cx, cy + k * 26, '#ddd', 1); } return ci(cx, cy, rr, '#F3FBF7', C.teal, ' stroke-width="3"') + h + cont; }
  function fasesMit(pares) { var F = [], cx = 235, cy = 95, ls = [44, 30, 22];
    var todos = function (fn) { var s = ''; for (var i = 0; i < pares; i++) for (var h = 0; h < 2; h++) s += fn(i, h); return s; };
    F.push(['Interfase', celM(cx, cy, 80, '<path d="M190,80 q20,-30 40,0 t40,0 M200,110 q20,-25 40,0 t30,0" stroke="#7a3fa0" stroke-width="3" fill="none"/>'), 'El ADN se <b>duplica</b>, pero todavía no se ve en forma de cromosomas.']);
    F.push(['Profase', celM(cx, cy, 80, todos(function (i, h) { return crom(cx - 50 + (i * 2 + h) * (100 / (pares * 2)) , cy - 20 + (h ? 25 : 0), ls[i], CCOL[i][h], true); })), 'Los cromosomas se <b>condensan</b>: cada uno tiene dos cromátidas hermanas unidas.']);
    F.push(['Metafase', celM(cx, cy, 80, todos(function (i, h) { var j = i * 2 + h, y = cy - 52 + j * (104 / (pares * 2 - 1 || 1)); return '<g transform="rotate(90 ' + cx + ' ' + y + ')">' + crom(cx, y, ls[i], CCOL[i][h], true) + '</g>'; }), true), 'Se ubican en fila en el <b>ecuador</b> de la célula, enganchados al huso.']);
    F.push(['Anafase', celM(cx, cy, 80, todos(function (i, h) { var j = i * 2 + h, y = cy - 52 + j * (104 / (pares * 2 - 1 || 1)); return '<g transform="rotate(90 ' + (cx - 36) + ' ' + y + ')">' + crom(cx - 36, y, ls[i], CCOL[i][h]) + '</g><g transform="rotate(90 ' + (cx + 36) + ' ' + y + ')">' + crom(cx + 36, y, ls[i], CCOL[i][h]) + '</g>'; }), true), 'Las <b>cromátidas hermanas se separan</b> y van a polos opuestos.']);
    var hija = function (ox) { return celM(ox, cy, 62, todos(function (i, h) { return crom(ox - 28 + (i * 2 + h) * (56 / (pares * 2 - 1 || 1)), cy, ls[i], CCOL[i][h]); })); };
    F.push(['Telofase y citocinesis', hija(150) + hija(320), 'Se forman dos núcleos y se divide el citoplasma: <b>2 células hijas</b> con ' + pares * 2 + ' cromosomas cada una, iguales a la madre (2n = ' + pares * 2 + ').']);
    return F; }
  function fasesMei(pares) { var F = [], cx = 235, cy = 95, ls = [44, 30, 22];
    F.push(['Profase I', celM(cx, cy, 80, (function () { var s = ''; for (var i = 0; i < pares; i++) { var x = cx - 40 + i * 40; s += crom(x - 8, cy, ls[i], CCOL[i][0], true, CCOL[i][1]) + crom(x + 8, cy, ls[i], CCOL[i][1], true, CCOL[i][0]); } return s; })()), 'Los cromosomas <b>homólogos</b> se aparean e intercambian pedazos: es el <b>entrecruzamiento</b> (mirá los colores mezclados).']);
    F.push(['Metafase I', celM(cx, cy, 80, (function () { var s = ''; for (var i = 0; i < pares; i++) { var y = cy - 40 + i * (80 / Math.max(1, pares - 1 || 1)); if (pares === 1) y = cy; s += '<g transform="rotate(90 ' + cx + ' ' + y + ')">' + crom(cx, y - 9, ls[i], CCOL[i][0], true, CCOL[i][1]) + crom(cx, y + 9, ls[i], CCOL[i][1], true, CCOL[i][0]) + '</g>'; } return s; })(), true), 'Los <b>pares de homólogos</b> se ubican juntos en el ecuador.']);
    var mitad = function (ox, h, rr) { var s = ''; for (var i = 0; i < pares; i++) s += crom(ox - 20 + i * (40 / Math.max(1, pares - 1)) * (pares > 1 ? 1 : 0), cy, ls[i], CCOL[i][h], true, CCOL[i][1 - h]); return celM(ox, cy, rr || 60, s); };
    F.push(['Anafase y telofase I', mitad(150, 0) + mitad(320, 1), 'Se separan los homólogos: quedan <b>2 células con n = ' + pares + '</b> cromosomas (la mitad), todavía dobles.']);
    var cuatro = ''; [0, 1].forEach(function (h) { [0, 1].forEach(function (q) { var ox = 70 + (h * 2 + q) * 110, s = ''; for (var i = 0; i < pares; i++) s += crom(ox - 16 + i * (32 / Math.max(1, pares - 1)) * (pares > 1 ? 1 : 0), cy, ls[i], q ? CCOL[i][1 - h] : CCOL[i][h]); cuatro += celM(ox, cy, 48, s); }); });
    F.push(['Meiosis II', cuatro, 'Una segunda división separa las cromátidas: resultan <b>4 células</b> con n = ' + pares + ' cromosomas simples, todas distintas. Son las gametas.']);
    return F; }
  M.mitosis = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'División', [['mitosis', 'Mitosis'], ['meiosis', 'Meiosis']], p.modo || 'mitosis') + ctrl('n', 'Pares de cromosomas (2n = el doble)', 1, 3, 1, 2), function (o) { var pares = o.n || 2, F = (o.m || 'mitosis') === 'meiosis' ? fasesMei(pares) : fasesMit(pares);
      return [{ vis: S(470, 190, celM(235, 95, 80, (function () { var s = ''; for (var i = 0; i < pares; i++) for (var h = 0; h < 2; h++) s += crom(195 + (i * 2 + h) * (80 / (pares * 2)), 95, [44, 30, 22][i], CCOL[i][h]); return s; })())), txt: 'Célula madre con <b>2n = ' + pares * 2 + '</b>: ' + pares + ' par' + (pares > 1 ? 'es' : '') + ' de cromosomas homólogos (cada par, un color de la madre y uno del padre).' }]
        .concat(F.map(function (f) { return { vis: S(470, 190, f[1]) + '<p class="nat-et">' + f[0] + '</p>', txt: '<b>' + f[0] + '</b>: ' + f[2] }; })); });
  } };
  M.mitosis_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 }, tipos = p.que ? [].concat(p.que) : ['orden', 'cuenta'];
    var t0 = { v: -1 };
    var t = function () { return tipos[rot(tipos.length, t0)]; };
    function armar() { if (t() === 'orden') ordenar(el, api, function () { var m = pick(['mitosis', 'meiosis']); return m === 'mitosis' ? { cons: 'Ordená las fases de la <b>mitosis</b>.', items: ['Profase', 'Metafase', 'Anafase', 'Telofase y citocinesis'], ayuda: 'Primero se condensan, después se alinean, se separan y se dividen.' } : { cons: 'Ordená las etapas de la <b>meiosis</b>.', items: ['Profase I (entrecruzamiento)', 'Metafase I', 'Anafase y telofase I', 'Meiosis II'], ayuda: 'Primero se separan los homólogos y después las cromátidas.' }; });
      else respuesta(el, api, function () { var n2 = pick([4, 6, 8, 12, 14, 46]), m = pick(['mitosis', 'meiosis']), v = m === 'mitosis' ? n2 : n2 / 2; return { cons: 'Una célula con <b>2n = ' + n2 + '</b> cromosomas hace <b>' + m + '</b>. ¿Cuántos cromosomas tiene cada célula hija?', campos: [{ lab: 'Cromosomas', v: v }], ayuda: m === 'mitosis' ? 'La mitosis da células iguales a la madre.' : 'La meiosis reduce el número a la mitad.', bien: '¡Bien! ' + (m === 'mitosis' ? '2 células con ' + v : '4 células con ' + v) + ' cromosomas.' }; });
      otro(el); var bt = el.querySelector('[data-lb="otro"]'); if (bt) bt.onclick = function (e) { e.stopPropagation(); armar(); }; }
    armar();
  } };

  // =====================================================================================
  // 12) TIEMPO GEOLÓGICO: la historia de la Tierra comprimida en un día de 24 horas (o en una cancha de 100 m)
  // =====================================================================================
  var EVT = [['Se forma la Tierra', 4600, '🌍'], ['Primeros seres vivos (bacterias)', 3800, '🦠'], ['Bacterias que hacen fotosíntesis llenan el aire de oxígeno', 2400, '🫧'], ['Primeras células con núcleo', 1800, '🧫'], ['Primeros animales con muchas células', 600, '🪼'], ['Las plantas conquistan la tierra firme', 470, '🌿'], ['Aparecen los dinosaurios', 230, '🦖'], ['Se extinguen los dinosaurios', 66, '☄️'], ['Primeros homínidos', 7, '🦍'], ['Homo sapiens', 0.3, '🧍']];
  function hora(ma) { var s = Math.round((1 - ma / 4600) * 86400), h = Math.floor(s / 3600), mi = Math.floor(s % 3600 / 60), se = s % 60; return (h < 10 ? '0' : '') + h + ':' + (mi < 10 ? '0' : '') + mi + (ma < 10 ? ':' + (se < 10 ? '0' : '') + se : ''); }
  function reloj(L, k) { var cx = 150, cy = 125, rr = 95, b = ci(cx, cy, rr, '#fff', C.osc, ' stroke-width="3"');
    for (var h = 0; h < 24; h++) { var a = -Math.PI / 2 + h / 24 * 2 * Math.PI; b += ln(cx + (rr - 6) * Math.cos(a), cy + (rr - 6) * Math.sin(a), cx + rr * Math.cos(a), cy + rr * Math.sin(a), C.osc, h % 6 ? 1 : 3); if (h % 6 === 0) b += tx(cx + (rr - 18) * Math.cos(a), cy + (rr - 18) * Math.sin(a) + 4, h, { a: 'middle', s: 11, w: 900 }); }
    L.forEach(function (e, j) { if (j > k) return; var a = -Math.PI / 2 + (1 - e[1] / 4600) * 2 * Math.PI, on = j === k; b += ln(cx, cy, cx + (rr - 14) * Math.cos(a), cy + (rr - 14) * Math.sin(a), on ? C.coral : '#cfdedb', on ? 3 : 1.5) + ci(cx + rr * Math.cos(a), cy + rr * Math.sin(a), on ? 6 : 4, on ? C.coral : C.teal); });
    if (k >= 0) { var e = L[k]; b += em(370, 70, e[2], 40) + tx(370, 120, hora(e[1]), { a: 'middle', s: 24, w: 900, c: C.coral }) + tx(370, 142, 'hace ' + fmt(e[1]) + ' millones de años', { a: 'middle', s: 11 }); }
    return S(470, 250, b); }
  function cancha(L, k) { var x0 = 20, W = 430, b = rc(x0, 60, W, 70, '#5BAA3C', '#fff', 6) + ln(x0 + W / 2, 60, x0 + W / 2, 130, '#fff', 2) + ci(x0 + W / 2, 95, 18, 'none', '#fff');
    [0, 25, 50, 75, 100].forEach(function (m) { b += tx(x0 + m / 100 * W, 148, m + ' m', { a: 'middle', s: 10 }); });
    L.forEach(function (e, j) { if (j > k) return; var x = x0 + (1 - e[1] / 4600) * W, on = j === k; b += ln(x, 56, x, 134, on ? C.coral : '#fff', on ? 3 : 1.5) + (on ? em(x, 36, e[2], 26) : ''); });
    if (k >= 0) b += tx(235, 180, 'a ' + fmt(Math.round((1 - L[k][1] / 4600) * 1000) / 10) + ' m del inicio' + (L[k][1] < 10 ? ' (¡a ' + fmt(Math.round(L[k][1] / 4600 * 100000) / 1000) + ' m del final!)' : ''), { a: 'middle', s: 13, w: 900, c: C.coral });
    return S(470, 195, b); }
  M.tiempo_geo = { tipo: 'ejemplo', pasos: true, render: function (el, p) { var L = p.items ? p.items.map(function (e) { return [e.t, e.ma, e.e || '📍']; }) : EVT;
    escena(el, sel('m', 'Comparar con', [['reloj', 'Un día de 24 horas'], ['cancha', 'Una cancha de 100 metros']], p.modo || 'reloj'), function (o) { var f = o.m === 'cancha' ? cancha : reloj, P = [{ vis: f(L, -1), txt: 'La Tierra tiene unos <b>4.600 millones de años</b>. Para imaginarlo, comprimimos toda esa historia en ' + (o.m === 'cancha' ? 'una cancha de 100 metros.' : 'un solo día.') }];
      L.forEach(function (e, j) { P.push({ vis: f(L, j), txt: '<b>' + e[0] + '</b>: hace ' + fmt(e[1]) + ' millones de años → ' + (o.m === 'cancha' ? 'a los ' + fmt(Math.round((1 - e[1] / 4600) * 1000) / 10) + ' m.' : 'a las ' + hora(e[1]) + '.') }); });
      P.push({ vis: f(L, L.length - 1), txt: 'Los seres humanos aparecemos en los <b>últimos segundos</b>: casi toda la historia de la vida ocurrió sin nosotros.' }); return P; });
  } };
  M.tiempo_geo_x = { tipo: 'ejercicio', render: function (el, p, api) {
    ordenar(el, api, function () { var L = mezclar(EVT.slice()).slice(0, 4).sort(function (a, b) { return b[1] - a[1]; }); return { cons: 'Ordená estos hechos de la historia de la Tierra, del <b>más antiguo</b> al más reciente.', items: L.map(function (e) { return e[2] + ' ' + e[0]; }), ayuda: 'Pensá qué tuvo que existir antes para que apareciera lo siguiente.', bien: '¡Bien! ' + L.map(function (e) { return e[0] + ' (' + fmt(e[1]) + ' Ma)'; }).join(' → ') + '.' }; });
  } };

  // =====================================================================================
  // 13) POBLACIÓN: crecimiento exponencial (J) y logístico (S) con natalidad, mortalidad y capacidad de carga
  // =====================================================================================
  function serie(N0, r, K, modelo, anios) { var L = [N0]; for (var t = 1; t <= anios; t++) { var N = L[t - 1]; N = modelo === 'logistico' ? N + r * N * (1 - N / K) : N + r * N; L.push(Math.max(0, Math.round(N))); } return L; }
  function grafPob(L, K, hasta, modelo) { var x0 = 50, y0 = 200, W = 400, Hh = 170, mx = Math.max(modelo === 'logistico' ? K * 1.1 : 0, Math.max.apply(null, L)) || 1, n = L.length - 1, b = ln(x0, y0, x0 + W, y0) + ln(x0, y0, x0, y0 - Hh - 5) + tx(x0 + W, y0 + 28, 'años', { a: 'end', s: 11 }) + tx(x0 + 4, y0 - Hh - 10, 'individuos', { s: 11 });
    if (modelo === 'logistico') b += ln(x0, y0 - K / mx * Hh, x0 + W, y0 - K / mx * Hh, C.coral, 2, ' stroke-dasharray="6 4"') + tx(x0 + W, y0 - K / mx * Hh - 6, 'K = ' + fmt(K), { a: 'end', s: 11, c: C.coral, w: 800 });
    var pts = []; for (var t = 0; t <= Math.min(hasta, n); t++) pts.push(r1(x0 + t / n * W) + ',' + r1(y0 - L[t] / mx * Hh));
    b += '<polyline points="' + pts.join(' ') + '" fill="none" stroke="' + C.teal + '" stroke-width="3"/>' + pts.map(function (q) { var c = q.split(','); return ci(+c[0], +c[1], 3, C.teal); }).join('');
    [0, Math.round(n / 2), n].forEach(function (t) { b += tx(x0 + t / n * W, y0 + 14, t, { a: 'middle', s: 10 }); }); b += tx(x0 - 4, y0 - Hh + 4, fmt(Math.round(mx)), { a: 'end', s: 10 });
    return S(470, 235, b); }
  M.poblacion = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, sel('m', 'Modelo', [['exponencial', 'Sin límites (exponencial)'], ['logistico', 'Con recursos limitados (logístico)']], p.modelo || 'logistico') + ctrl('n0', 'Población inicial', 10, 500, 10, 100) + ctrl('b', 'Natalidad (%)', 0, 80, 1, 40) + ctrl('d', 'Mortalidad (%)', 0, 80, 1, 10) + ctrl('k', 'Capacidad de carga K', 200, 5000, 100, 1500), function (o) {
      var N0 = o.n0 || 100, r = ((o.b || 0) - (o.d || 0)) / 100, K = o.k || 1500, mo = o.m || 'logistico', L = serie(N0, r, K, mo, 20), N1 = L[1], P = [];
      P.push({ vis: S(470, 70, tx(235, 30, 'r = natalidad − mortalidad = ' + (o.b || 0) + ' % − ' + (o.d || 0) + ' % = ' + Math.round(r * 100) + ' %', { a: 'middle', s: 15, w: 900 }) + tx(235, 55, r > 0 ? 'nacen más de los que mueren: crece' : r < 0 ? 'mueren más de los que nacen: disminuye' : 'nacen tantos como mueren: se mantiene', { a: 'middle', s: 12, c: C.teal, w: 800 })), txt: 'La <b>tasa de crecimiento</b> es la diferencia entre natalidad y mortalidad.' });
      P.push({ vis: S(470, 70, tx(235, 38, fmt(N0) + (mo === 'logistico' ? ' + ' + Math.round(r * 100) + ' % × ' + fmt(N0) + ' × (1 − ' + fmt(N0) + '/' + fmt(K) + ')' : ' + ' + Math.round(r * 100) + ' % × ' + fmt(N0)) + ' ≈ ' + fmt(N1), { a: 'middle', s: 14, w: 900 })), txt: 'Al cabo del primer año: <b>' + fmt(N1) + '</b> individuos.' + (mo === 'logistico' ? ' El factor (1 − N/K) frena el crecimiento cuando la población se acerca a K.' : '') });
      P.push({ vis: grafPob(L, K, 5, mo), txt: 'Los primeros 5 años: ' + L.slice(0, 6).map(fmt).join(' → ') + '.' });
      P.push({ vis: grafPob(L, K, 20, mo), txt: mo === 'logistico' ? (r > 0 ? 'Curva en <b>S</b>: crece rápido y se estabiliza cerca de la <b>capacidad de carga</b>, el máximo que el ambiente puede sostener.' : 'Con r negativo, la población baja aunque haya recursos.') : (r > 0 ? 'Curva en <b>J</b>: sin límites, crece cada vez más rápido. En la naturaleza esto no dura: se acaban los recursos.' : 'Con r negativo, la población disminuye año tras año.') });
      return P; });
  } };
  M.poblacion_x = { tipo: 'ejercicio', render: function (el, p, api) {
    respuesta(el, api, function () { var N0 = pick([100, 200, 400, 500, 800, 1000]), b = pick([20, 25, 30, 40]), d = pick([5, 10, 15]), v = Math.round(N0 * (1 + (b - d) / 100));
      return { cons: 'Una población de <b>' + fmt(N0) + '</b> carpinchos tiene una natalidad del <b>' + b + ' %</b> y una mortalidad del <b>' + d + ' %</b> por año. Sin límites de recursos, ¿cuántos habrá al año siguiente?', campos: [{ lab: 'Individuos', v: v }], ayuda: 'Calculá r = natalidad − mortalidad y sumale a la población ese porcentaje.', bien: '¡Bien! r = ' + (b - d) + ' %: ' + fmt(N0) + ' + ' + fmt(v - N0) + ' = ' + fmt(v) + '.' }; });
  } };

  // =====================================================================================
  // 14) EPIDEMIA: cadena de contagios con R₀ y vacunación; umbral de inmunidad de rebaño
  // =====================================================================================
  M.epidemia = { tipo: 'ejemplo', pasos: true, render: function (el, p) {
    escena(el, ctrl('r', 'R₀ (a cuántos contagia cada enfermo)', 1, 5, 0.5, 3) + ctrl('v', 'Población vacunada (%)', 0, 95, 5, 0), function (o) { var R0 = o.r || 3, v = (o.v || 0) / 100, Re = Math.round(R0 * (1 - v) * 100) / 100, gens = 4, casos = [1], P = [];
      for (var g = 1; g <= gens; g++) casos.push(casos[g - 1] * Re);
      var dib = function (hasta) { var b = ''; for (var g = 0; g <= hasta; g++) { var n = Math.round(casos[g]), y = 30 + g * 46, mostrar = Math.min(n, 30); b += tx(30, y + 5, 'G' + g, { a: 'middle', s: 11, w: 900, c: C.teal });
          for (var i = 0; i < mostrar; i++) b += em(60 + i * 10.5, y, '🤒', 11); b += tx(60 + mostrar * 10.5 + 8, y + 5, n > 30 ? '… ' + fmt(n) + ' casos' : fmt(n) + (n === 1 ? ' caso' : ' casos'), { s: 11, w: 800 }); } return S(470, 30 + (hasta + 1) * 46, b); };
      P.push({ vis: dib(0), txt: 'Empieza con <b>1 persona enferma</b>. Cada una contagia, en promedio, a <b>R₀ = ' + fmt(R0) + '</b> personas si nadie está protegido.' });
      if (v) P.push({ vis: dib(0), txt: 'Con un ' + Math.round(v * 100) + ' % de vacunados, cada enfermo contagia en realidad a R = ' + fmt(R0) + ' × ' + fmt(Math.round((1 - v) * 100) / 100) + ' = <b>' + fmt(Re) + '</b>.' });
      for (g = 1; g <= gens; g++) P.push({ vis: dib(g), txt: 'Generación ' + g + ': ' + fmt(Math.round(casos[g - 1])) + ' × ' + fmt(Re) + ' ≈ <b>' + fmt(Math.round(casos[g])) + '</b> casos.' });
      var umb = Math.round((1 - 1 / R0) * 100);
      P.push({ vis: dib(gens) + nota('Umbral de inmunidad: 1 − 1/R₀ = ' + umb + ' %'), txt: Re > 1 ? 'Si cada enfermo contagia a más de una persona, los casos <b>crecen</b>. Para frenarlo hay que vacunar al menos al <b>' + umb + ' %</b>.' : 'Con R menor o igual a 1, la epidemia <b>se apaga</b>: la vacunación protege también a quienes no pueden vacunarse.' });
      return P; });
  } };
  M.epidemia_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = { v: -1 };
    respuesta(el, api, function () { if (rot(2, u)) { var R0 = pick([2, 3, 4]), g = pick([2, 3, 4]), v = Math.pow(R0, g); return { cons: 'Una enfermedad tiene <b>R₀ = ' + R0 + '</b> y nadie está vacunado. Si empieza con 1 caso, ¿cuántos casos nuevos habrá en la generación <b>' + g + '</b>?', campos: [{ lab: 'Casos', v: v }], ayuda: 'En cada generación se multiplica por ' + R0 + '.', bien: '¡Bien! ' + R0 + (g > 1 ? '^' + g : '') + ' = ' + v + '.' }; }
      var R1 = pick([2, 4, 5, 10]), w = Math.round((1 - 1 / R1) * 100); return { cons: 'Una enfermedad tiene <b>R₀ = ' + R1 + '</b>. ¿Qué porcentaje de la población hay que vacunar como mínimo para frenarla? (umbral = 1 − 1/R₀)', campos: [{ lab: 'Umbral', v: w, un: '%' }], ayuda: 'Calculá 1 − 1/' + R1 + ' y pasalo a porcentaje.', bien: '¡Bien! 1 − 1/' + R1 + ' = ' + w + ' %.' }; });
  } };

  // ---------- estilos del banco de Naturales ----------
  var css = document.createElement('style');
  css.textContent = [
    '.nat-svg{display:block;width:100%;max-width:470px;height:auto;margin:6px auto;font-family:inherit}.nat-svg text{font-family:inherit;paint-order:stroke;stroke:#fff;stroke-width:3px;stroke-linejoin:round}.nat-svg text.sh{stroke:none}',
    '.nat-svg .nat-tap{cursor:pointer}.nat-svg .nat-tap:hover circle{fill:#D7F0E9}.nat-svg .nat-sel circle,.nat-svg .nat-sel rect{fill:#FFF3C4;stroke:#C2552E;stroke-width:3}.nat-svg .nat-bien circle,.nat-svg .nat-bien rect{fill:#D7F0E9;stroke:#087E83}.nat-svg .nat-mal circle,.nat-svg .nat-mal rect{fill:#FCE4EC;stroke:#c2416b}',
    '.nat-card{margin:6px 0;padding:8px 12px;border-radius:12px;background:#F3FBF7;border:2px solid #D7F0E9;font-size:.98rem;line-height:1.45}.nat-nota{margin:4px 0;text-align:center;font-weight:800;color:#066A6E}.nat-et{margin:0;text-align:center;font-weight:900;color:#C2552E;letter-spacing:.03em}',
    '.nat-ord{margin:6px 0 8px;padding-left:28px;display:flex;flex-direction:column;gap:6px}.nat-ord li{min-height:40px;border:2px dashed #9dbdb9;border-radius:12px;display:flex;align-items:center;padding:2px 4px}.nat-ord li::marker{font-weight:900;color:#087E83}'
  ].join('');
  document.head.appendChild(css);
})();
