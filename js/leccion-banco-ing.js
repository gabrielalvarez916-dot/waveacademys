/* BANCO DE LA LECCIÓN INTERACTIVA · INGLÉS (secundaria; con frases cortas también sirve en Medio).
   Mismo banco que js/leccion-banco*.js (SOLO lección). Explicación en castellano, ejemplos en inglés con audio 🔊 (voz del navegador).
   Cada ejemplo tiene un dibujo propio y es PASO A PASO; cada uno con su práctica (_x). */
(function () {
  'use strict';
  var B = window.WaveLeccionBanco; if (!B || !B._h || !B._h.nat) return;
  var H = B._h, M = B.motores, N = H.nat, R = H.R, pick = H.pick, mezclar = H.mezclar;
  var escena = H.escena, respuesta = H.respuesta, cajas = H.cajas, C = N.C, S = N.S, tx = N.tx, ln = N.ln, fl = N.fl, ci = N.ci, rc = N.rc, em = N.em, sel = N.sel, otro = N.otro, elegir = N.elegir, ordenar = N.ordenar, rot = N.rot, nota = N.nota;
  function say(t, lento) { try { var u = new SpeechSynthesisUtterance(t); u.lang = 'en-US'; u.rate = lento ? 0.7 : 0.95; var v = speechSynthesis.getVoices().filter(function (x) { return /^en/i.test(x.lang); })[0]; if (v) u.voice = v; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) {} }
  function oir(t) { return '<button type="button" class="ing-oir" data-say="' + String(t).replace(/"/g, '&quot;') + '" aria-label="Escuchar">🔊</button>'; }
  function conOir(el) { if (el._ing) return; el._ing = 1; el.addEventListener('click', function (e) { var b = e.target.closest('[data-say]'); if (b) say(b.getAttribute('data-say'), e.shiftKey); }); }
  function frase(t, extra) { return '<p class="ing-fr">' + t + ' ' + oir(String(t).replace(/<[^>]+>/g, '')) + '</p>' + (extra || ''); }
  function chips(L) { return '<div class="ing-chips">' + L.map(function (c) { return '<span class="' + (c[1] || '') + '">' + c[0] + (c[2] ? '<small>' + c[2] + '</small>' : '') + '</span>'; }).join('') + '</div>'; }
  function card(t, cls) { return '<p class="nat-card ' + (cls || '') + '">' + t + '</p>'; }
  H.ing = { say: say, oir: oir, conOir: conOir };

  // =====================================================================================
  // 1) TIEMPOS VERBALES en la línea del tiempo
  // =====================================================================================
  var TIE = [['Past simple', 'pasado', 'punto', 'I played football.', [['I', 'suj'], ['played', 'verb', 'verbo + -ed']], 'yesterday, last week, in 2019', 'Una acción terminada en el pasado.'],
    ['Past continuous', 'pasado', 'tramo', 'I was playing football.', [['I', 'suj'], ['was', 'aux', 'was / were'], ['playing', 'verb', 'verbo + -ing']], 'at 5 pm yesterday, while…', 'Una acción en desarrollo en un momento del pasado.'],
    ['Present perfect', 'puente', 'puente', 'I have played football.', [['I', 'suj'], ['have', 'aux', 'have / has'], ['played', 'verb', 'participio']], 'already, yet, ever, never, since, for', 'Algo del pasado conectado con el presente (experiencia o resultado).'],
    ['Present simple', 'presente', 'rutina', 'I play football.', [['I', 'suj'], ['play', 'verb', 'verbo (+ -s con he/she/it)']], 'every day, always, usually, on Mondays', 'Rutinas, hábitos y verdades generales.'],
    ['Present continuous', 'presente', 'ahora', 'I am playing football.', [['I', 'suj'], ['am', 'aux', 'am / is / are'], ['playing', 'verb', 'verbo + -ing']], 'now, right now, at the moment', 'Lo que está pasando ahora.'],
    ['Future (will)', 'futuro', 'punto', 'I will play football.', [['I', 'suj'], ['will', 'aux', 'will'], ['play', 'verb', 'verbo']], 'tomorrow, next week, in 2030', 'Decisiones y predicciones sobre el futuro.']];
  function linea(t, paso) { var s = ln(20, 80, 460, 80, C.osc, 3) + ln(240, 60, 240, 100, C.osc, 2) + tx(240, 116, 'NOW', { a: 'middle', s: 11, w: 900 }) + tx(80, 116, 'PAST', { a: 'middle', s: 11, w: 900, c: C.azul }) + tx(400, 116, 'FUTURE', { a: 'middle', s: 11, w: 900, c: C.verde }) + fl(440, 80, 465, 80, C.osc, 3);
    if (paso >= 1) { var k = t[2], c = C.coral; if (k === 'punto') { var x = t[1] === 'pasado' ? 110 : 380; s += ci(x, 80, 9, c) + em(x, 44, '⚽', 22); }
      else if (k === 'tramo') s += rc(80, 70, 90, 20, 'rgba(194,85,46,.4)', c, 8) + ln(130, 50, 130, 100, C.lila, 2, ' stroke-dasharray="4 3"') + tx(130, 44, '5 pm', { a: 'middle', s: 10, w: 800, c: C.lila });
      else if (k === 'puente') s += '<path d="M90,80 Q165,20 240,80" fill="none" stroke="' + c + '" stroke-width="4" marker-end="url(#natfl)"/>' + ci(90, 80, 7, c);
      else if (k === 'rutina') [60, 130, 200, 270, 340, 410].forEach(function (x) { s += ci(x, 80, 6, c); });
      else s += rc(220, 68, 40, 24, 'rgba(194,85,46,.4)', c, 8) + em(240, 44, '⚽', 22); }
    return S(480, 125, s); }
  M.tiempos_en = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('t', 'Tense', TIE.map(function (t, i) { return [i, t[0]]; }), 0), function (o) { var t = TIE[+(o.t || 0)] || TIE[0];
      return [{ vis: linea(t, 0), txt: 'La <b>línea del tiempo</b>: el pasado a la izquierda, el presente (NOW) en el medio y el futuro a la derecha.' },
        { vis: linea(t, 1), txt: '<b>' + t[0] + '</b>: ' + t[6] },
        { vis: linea(t, 1) + chips(t[4]), txt: 'Se arma así: ' + t[4].map(function (c) { return c[2] || 'sujeto'; }).join(' + ') + '.' },
        { vis: linea(t, 1) + frase(t[3]), txt: 'Ejemplo: <b>' + t[3] + '</b> Tocá 🔊 para escucharlo.' },
        { vis: linea(t, 1) + card('🕒 ' + t[5]), txt: 'Palabras que suelen acompañarlo: <i>' + t[5] + '</i>.' }]; });
  } };
  var TIE_X = [['She is reading a book right now.', 4], ['We visited Rome last year.', 0], ['He has never seen the sea.', 2], ['They will travel tomorrow.', 5], ['I get up at seven every day.', 3], ['I was sleeping at midnight.', 1], ['My brother plays the guitar on Fridays.', 3], ['Look! It is raining.', 4]];
  M.tiempos_en_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; conOir(el);
    elegir(el, api, function () { var q = TIE_X[rot(TIE_X.length, u)], t = TIE[q[1]]; return { cons: '¿Qué tiempo verbal es?', html: frase(q[0]), ops: mezclar([t[0]].concat(mezclar(TIE.filter(function (x) { return x !== t; })).slice(0, 2).map(function (x) { return x[0]; }))), ok: t[0], ayuda: 'Mirá el auxiliar, la forma del verbo y la palabra de tiempo.', bien: '¡Sí! ' + t[0] + ': ' + t[6].toLowerCase() }; });
  } };

  // =====================================================================================
  // 2) MÁQUINA DE CONJUGAR: present simple (afirmativa, 3.ª persona, negativa, pregunta)
  // =====================================================================================
  var VB = [['play', 'plays', 'jugar', 'agrega -s'], ['watch', 'watches', 'mirar', 'termina en -ch: agrega -es'], ['study', 'studies', 'estudiar', 'consonante + y: cambia a -ies'], ['go', 'goes', 'ir', 'termina en -o: agrega -es'], ['have', 'has', 'tener', 'irregular: has'], ['fix', 'fixes', 'arreglar', 'termina en -x: agrega -es']];
  var COMP = { play: 'football', watch: 'TV', study: 'English', go: 'to school', have: 'a dog', fix: 'bikes' };
  M.conjugar_en = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('v', 'Verb', VB.map(function (v, i) { return [i, v[0] + ' (' + v[2] + ')']; }), 0), function (o) { var v = VB[+(o.v || 0)] || VB[0], c = COMP[v[0]];
      return [{ vis: chips([['I', 'suj'], [v[0], 'verb'], [c, 'resto']]) + frase('I ' + v[0] + ' ' + c + '.'), txt: 'Con <b>I, you, we, they</b> el verbo va igual que en el diccionario: <b>' + v[0] + '</b>.' },
        { vis: chips([['She', 'suj'], [v[1], 'verb on'], [c, 'resto']]) + frase('She ' + v[1] + ' ' + c + '.'), txt: 'Con <b>he, she, it</b> cambia: <b>' + v[1] + '</b> (' + v[3] + ').' },
        { vis: chips([['She', 'suj'], ["doesn't", 'aux on', 'does + not'], [v[0], 'verb'], [c, 'resto']]) + frase("She doesn't " + v[0] + ' ' + c + '.'), txt: 'Para negar usamos <b>don\'t</b> (I, you, we, they) o <b>doesn\'t</b> (he, she, it). ¡Ojo! Con doesn\'t el verbo vuelve a la forma base: <b>' + v[0] + '</b>, sin -s.' },
        { vis: chips([['Does', 'aux on'], ['she', 'suj'], [v[0], 'verb'], [c + '?', 'resto']]) + frase('Does she ' + v[0] + ' ' + c + '?'), txt: 'Para preguntar, el auxiliar va <b>adelante</b>: Do / Does + sujeto + verbo base.' },
        { vis: frase('Yes, she does.') + frase("No, she doesn't."), txt: 'Respuestas cortas: se repite el auxiliar, no el verbo.' }]; });
  } };
  M.conjugar_en_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; conOir(el);
    respuesta(el, api, function () { var v = VB[rot(VB.length, u)], c = COMP[v[0]], m = p.modo || pick(['tercera', 'negativa']), sj = pick(['He', 'She', 'My cat', 'Tom']);
      if (m === 'negativa') return { cons: 'Pasá a negativa: <b>' + sj + ' ' + v[1] + ' ' + c + '.</b>', campos: [{ lab: sj, v: ["doesn't " + v[0], 'does not ' + v[0]], tipo: 'texto' }, { lab: '', v: [c, c + '.'], tipo: 'texto' }], ayuda: "doesn't + verbo base (sin -s): doesn't " + v[0] + '.', bien: '¡Bien! ' + sj + " doesn't " + v[0] + ' ' + c + '.' };
      return { cons: 'Completá con el verbo <b>' + v[0] + '</b>: ' + sj + ' ___ ' + c + ' every day.', campos: [{ lab: 'Verbo:', v: v[1], tipo: 'texto' }], ayuda: 'Con he / she / it: ' + v[3] + '.', bien: '¡Bien! ' + sj + ' ' + v[1] + ' ' + c + ' every day.' }; }); otro(el);
  } };

  // =====================================================================================
  // 3) VERBOS IRREGULARES: tarjetas por patrón
  // =====================================================================================
  var IRR = { 'A-A-A (no cambia)': [['cut', 'cut', 'cut', 'cortar'], ['put', 'put', 'put', 'poner'], ['let', 'let', 'let', 'dejar']], 'A-B-B (pasado = participio)': [['buy', 'bought', 'bought', 'comprar'], ['make', 'made', 'made', 'hacer'], ['find', 'found', 'found', 'encontrar'], ['sleep', 'slept', 'slept', 'dormir']], 'A-B-C (cambian las tres)': [['go', 'went', 'gone', 'ir'], ['see', 'saw', 'seen', 'ver'], ['eat', 'ate', 'eaten', 'comer'], ['write', 'wrote', 'written', 'escribir']], 'A-B-A (vuelve)': [['come', 'came', 'come', 'venir'], ['run', 'ran', 'run', 'correr'], ['become', 'became', 'become', 'convertirse']] };
  function tarj(v, n) { return '<div class="ing-tarjs">' + ['base', 'past', 'participle'].map(function (k, i) { return '<div class="' + (i < n ? 'on' : '') + '"><small>' + k + '</small><b>' + (i < n ? v[i] : '?') + '</b>' + (i < n ? oir(v[i]) : '') + '</div>'; }).join('') + '<em>' + v[3] + '</em></div>'; }
  M.irregulares = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el); var ks = Object.keys(IRR);
    escena(el, sel('g', 'Patrón', ks.map(function (k) { return [k, k]; }), ks[2]), function (o) { var L = IRR[o.g] || IRR[ks[2]], v = L[0];
      return [{ vis: tarj(v, 1), txt: 'Los verbos irregulares no forman el pasado con -ed: hay que aprenderlos. Partimos de la forma base: <b>' + v[0] + '</b> (' + v[3] + ').' },
        { vis: tarj(v, 2), txt: 'El <b>past simple</b>: <b>' + v[1] + '</b> (por ejemplo, <i>Yesterday I ' + v[1] + '…</i>).' },
        { vis: tarj(v, 3), txt: 'El <b>participio</b>: <b>' + v[2] + '</b> (para el present perfect: <i>I have ' + v[2] + '…</i>).' },
        { vis: L.map(function (x) { return tarj(x, 3); }).join(''), txt: 'Este grupo sigue el mismo patrón: <b>' + o.g + '</b>. Aprenderlos por patrones es más fácil que de a uno.' }]; });
  } };
  M.irregulares_x = { tipo: 'ejercicio', render: function (el, p, api) { var L = [], u = {}; Object.keys(IRR).forEach(function (k) { L = L.concat(IRR[k]); }); conOir(el);
    respuesta(el, api, function () { var v = L[rot(L.length, u)], k = p.modo === 'participio' ? 2 : 1; return { cons: '¿Cuál es el <b>' + (k === 1 ? 'past simple' : 'participio') + '</b> de <b>' + v[0] + '</b> (' + v[3] + ')?', campos: [{ lab: v[0] + ' →', v: v[k], tipo: 'texto' }], ayuda: v[0] + ' – ' + v[1] + ' – ' + v[2] + '.', bien: '¡Bien! ' + v[0] + ' – ' + v[1] + ' – ' + v[2] + '.' }; }); otro(el);
  } };

  // =====================================================================================
  // 4) COMPARATIVOS Y SUPERLATIVOS con barras
  // =====================================================================================
  var ADJ = [['tall', 'taller', 'the tallest', 'alto', 'corto: + -er / the + -est', ['Tom', 150], ['Ann', 165], ['Joe', 180], 'cm'], ['big', 'bigger', 'the biggest', 'grande', 'vocal + consonante: se duplica la consonante', ['Cat', 4], ['Dog', 20], ['Horse', 500], 'kg'],
    ['happy', 'happier', 'the happiest', 'feliz', 'termina en -y: cambia a -ier / -iest', ['Mon', 3], ['Wed', 6], ['Sat', 9], '/10'], ['expensive', 'more expensive', 'the most expensive', 'caro', 'largo: more / the most', ['Pen', 2], ['Book', 15], ['Phone', 300], 'USD'], ['good', 'better', 'the best', 'bueno', 'irregular', ['Team A', 4], ['Team B', 7], ['Team C', 9], 'points']];
  function barras(a, paso) { var mx = a[7][1], s = ''; [a[5], a[6], a[7]].forEach(function (q, i) { var h = 18 + q[1] / mx * 120, x = 60 + i * 130; s += rc(x, 160 - h, 70, h, paso >= 1 && i >= 1 ? (paso >= 2 && i === 2 ? C.coral : '#64B5F6') : '#B0BEC5', null, 6) + tx(x + 35, 178, q[0], { a: 'middle', s: 12, w: 900 }) + tx(x + 35, 152 - h, q[1] + ' ' + a[8], { a: 'middle', s: 10, w: 700 }); }); if (paso >= 3) s += em(320, 18 + 0, '🏆', 20); return S(470, 190, s); }
  M.comparar_en = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('a', 'Adjective', ADJ.map(function (a, i) { return [i, a[0] + ' (' + a[3] + ')']; }), 0), function (o) { var a = ADJ[+(o.a || 0)] || ADJ[0], f1 = a[6][0] + ' is ' + a[1] + ' than ' + a[5][0] + '.', f2 = a[7][0] + ' is ' + a[2] + '.';
      return [{ vis: barras(a, 0), txt: 'Tres cosas para comparar según el adjetivo <b>' + a[0] + '</b> (' + a[3] + ').' }, { vis: barras(a, 1) + frase(f1), txt: 'Para comparar <b>dos</b>: el <b>comparativo</b> + <b>than</b>: ' + a[1] + ' than.' }, { vis: barras(a, 2) + frase(f2), txt: 'Para decir cuál es el que más, entre <b>todos</b>: el <b>superlativo</b>, con <b>the</b>: ' + a[2] + '.' }, { vis: barras(a, 3) + card('📏 ' + a[0] + ' → ' + a[1] + ' → ' + a[2] + ' · regla: ' + a[4]), txt: 'La regla depende del adjetivo: ' + a[4] + '.' }]; });
  } };
  M.comparar_en_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, X = [['small', 'smaller', 'the smallest'], ['hot', 'hotter', 'the hottest'], ['easy', 'easier', 'the easiest'], ['beautiful', 'more beautiful', 'the most beautiful'], ['bad', 'worse', 'the worst'], ['fast', 'faster', 'the fastest'], ['interesting', 'more interesting', 'the most interesting'], ['big', 'bigger', 'the biggest']];
    respuesta(el, api, function () { var a = X[rot(X.length, u)], sup = p.modo === 'superlativo' || (p.modo !== 'comparativo' && R(0, 1)); return sup ? { cons: 'Completá con el superlativo de <b>' + a[0] + '</b>: It is ___ day of the year.', campos: [{ lab: 'It is', v: a[2], tipo: 'texto' }], ayuda: 'Superlativo: ' + a[2] + '.', bien: '¡Bien!' } : { cons: 'Completá con el comparativo de <b>' + a[0] + '</b>: This one is ___ than that one.', campos: [{ lab: 'This one is', v: a[1], tipo: 'texto' }], ayuda: 'Comparativo: ' + a[1] + '.', bien: '¡Bien!' }; }); otro(el);
  } };

  // =====================================================================================
  // 5) PREPOSICIONES DE LUGAR
  // =====================================================================================
  var PREP = [['in', 'adentro de', 120, 100], ['on', 'arriba de (apoyado)', 120, 52], ['under', 'debajo de', 120, 162], ['next to', 'al lado de', 210, 110], ['behind', 'detrás de', 140, 70], ['in front of', 'delante de', 120, 150], ['between', 'entre', 260, 110]];
  function escenaP(k) { var q = PREP[k], s = rc(0, 0, 360, 200, '#FFF8E1') + rc(0, 180, 360, 20, '#D7CCC8') + (k === 6 ? rc(190, 90, 40, 60, '#8D6E63', C.osc, 4) + rc(290, 90, 40, 60, '#8D6E63', C.osc, 4) : '') + (k === 4 ? em(140, 70, '🐱', 34) : '') + rc(70, 70, 100, 110, '#A1887F', C.osc, 6) + (k === 0 ? em(120, 112, '🐱', 34) + rc(70, 70, 100, 110, 'rgba(161,136,127,.55)', C.osc, 6) : '') + (k !== 0 && k !== 4 ? em(q[2], q[3], '🐱', 34) : ''); return S(360, 200, s); }
  M.preposiciones_en = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, '', function () { return PREP.map(function (q, k) { var f = 'The cat is ' + q[0] + ' the box' + (k === 6 ? 'es' : '') + '.'; return { vis: escenaP(k) + frase(f), txt: '<b>' + q[0] + '</b> = ' + q[1] + '.' + (k === 6 ? ' Between se usa con dos cosas.' : '') }; }); });
  } };
  M.preposiciones_en_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {};
    elegir(el, api, function () { var k = rot(PREP.length, u); return { cons: 'Where is the cat? The cat is ___ the box' + (k === 6 ? 'es' : '') + '.', html: escenaP(k), ops: mezclar([PREP[k][0]].concat(mezclar(PREP.filter(function (_, j) { return j !== k; })).slice(0, 2).map(function (q) { return q[0]; }))), ok: PREP[k][0], bien: '¡Sí! ' + PREP[k][0] + ' = ' + PREP[k][1] + '.' }; });
  } };

  // =====================================================================================
  // 6) THERE IS / THERE ARE (some, any, contables e incontables)
  // =====================================================================================
  var CUARTO = [['bed', '🛏️', 1, 'a bed'], ['chairs', '🪑', 2, 'two chairs'], ['books', '📚', 3, 'some books'], ['lamp', '💡', 1, 'a lamp'], ['TV', '📺', 0, 'a TV'], ['water', '🥛', -1, 'some water']];
  function cuarto(n) { var s = rc(0, 0, 400, 180, '#EDE7F6') + rc(0, 150, 400, 30, '#BCAAA4'); var pos = [[60, 120], [150, 125], [240, 90], [320, 70], [330, 130]]; CUARTO.slice(0, 4).concat([CUARTO[5]]).forEach(function (q, i) { var c = q[2] > 0 ? q[2] : 1; for (var j = 0; j < c; j++) s += em(pos[i][0] + j * 26, pos[i][1], q[1], 30); }); if (n >= 1) s += tx(200, 24, 'no TV 🚫', { a: 'middle', s: 12, w: 800, c: C.rosa }); return S(400, 180, s); }
  M.there_is = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, '', function () { return [{ vis: cuarto(0) + frase('There is a bed.'), txt: 'Para decir que algo <b>hay</b> (una sola cosa): <b>There is</b> + a / an.' }, { vis: cuarto(0) + frase('There are two chairs.'), txt: 'Si son varias: <b>There are</b> + plural.' }, { vis: cuarto(1) + frase("There isn't a TV."), txt: 'Negativa: <b>There isn\'t</b> / <b>There aren\'t</b>.' }, { vis: cuarto(1) + frase('There are some books.') + frase('Are there any books?'), txt: '<b>some</b> en afirmativas; <b>any</b> en negativas y preguntas.' }, { vis: cuarto(1) + frase('There is some water.'), txt: 'Lo que no se cuenta (water, milk, sugar) es <b>incontable</b>: va con <b>There is</b> y some, nunca con a ni con número.' }]; });
  } };
  M.there_is_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, L = [['___ a cat on the sofa.', 'There is'], ['___ three apples in the bag.', 'There are'], ["___ any milk in the fridge.", "There isn't"], ['___ some rice in the pot.', 'There is'], ["___ any students in the classroom.", "There aren't"], ['___ two windows in my room.', 'There are']];
    elegir(el, api, function () { var q = L[rot(L.length, u)]; return { cons: 'Completá: <b>' + q[0] + '</b>', ops: ['There is', 'There are', "There isn't", "There aren't"], ok: q[1], ayuda: '¿Es una o varias? ¿Contable o incontable? ¿Afirmativa o negativa (any)?', bien: '¡Bien! ' + q[0].replace('___', q[1]) }; });
  } };

  // =====================================================================================
  // 7) MODALES
  // =====================================================================================
  var MOD = [['can', '💪', 'capacidad o permiso', 'I can swim. / Can I go out?'], ['must', '⚠️', 'obligación fuerte (la decide quien habla)', 'I must study for the test.'], ["mustn't", '⛔', 'prohibición', "You mustn't run by the pool."], ['should', '💡', 'consejo', 'You should drink more water.'], ['have to', '📋', 'obligación que viene de afuera (reglas)', 'I have to wear a uniform at school.'], ["don't have to", '🆗', 'no es necesario (pero podés)', "You don't have to bring lunch."]];
  M.modales = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('m', 'Modal', MOD.map(function (m, i) { return [i, m[0]]; }), 0), function (o) { var m = MOD[+(o.m || 0)] || MOD[0], cartel = '<div class="ing-cartel"><i>' + m[1] + '</i><b>' + m[0] + '</b><small>' + m[2] + '</small></div>';
      return [{ vis: cartel, txt: '<b>' + m[0] + '</b> expresa ' + m[2] + '.' }, { vis: cartel + chips([['I / He / She', 'suj'], [m[0], 'aux on'], ['verbo base', 'verb']]), txt: 'Va seguido del verbo en forma base. ' + (m[0].indexOf('have') < 0 ? 'No lleva -s con he/she/it ni do/does: <i>She ' + m[0] + ' swim</i>.' : 'Ojo: have to sí cambia: <i>She has to…</i>, <i>She doesn\'t have to…</i>.') }, { vis: cartel + m[3].split(' / ').map(function (f) { return frase(f); }).join(''), txt: 'Ejemplo: <b>' + m[3] + '</b>' }, { vis: '<div class="ing-carteles">' + MOD.map(function (x) { return '<div class="ing-cartel chico' + (x === m ? ' on' : '') + '"><i>' + x[1] + '</i><b>' + x[0] + '</b></div>'; }).join('') + '</div>', txt: 'Cuidado con dos parecidos: <b>mustn\'t</b> (está prohibido) no es lo mismo que <b>don\'t have to</b> (no hace falta).' }]; });
  } };
  M.modales_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, L = [['Tenés fiebre. You ___ see a doctor.', 'should'], ['Es una regla del museo: you ___ touch the paintings.', "mustn't"], ['Mi hermana ___ play the piano very well.', 'can'], ['Mañana es feriado: you ___ go to school.', "don't have to"], ['En el colegio, students ___ wear a uniform.', 'have to']];
    elegir(el, api, function () { var q = L[rot(L.length, u)]; return { cons: q[0], ops: mezclar([q[1]].concat(mezclar(MOD.map(function (m) { return m[0]; }).filter(function (x) { return x !== q[1]; })).slice(0, 2))), ok: q[1], bien: '¡Sí! ' + q[1] + '.' }; });
  } };

  // =====================================================================================
  // 8) CONDICIONALES (0, 1 y 2)
  // =====================================================================================
  var COND = [['Zero', 'If you heat ice, it melts.', 'If + present', 'present', 'algo que siempre pasa (hechos, ciencia)', '🧊➜💧'], ['First', 'If it rains tomorrow, I will stay home.', 'If + present', 'will + verbo', 'algo posible en el futuro', '🌧️➜🏠'], ['Second', 'If I had a million dollars, I would travel the world.', 'If + past', 'would + verbo', 'algo imaginario o poco probable', '💰➜✈️']];
  function cadena(c, n) { var parts = c[1].split(', '); return '<div class="ing-cad"><div class="' + (n >= 1 ? 'on' : '') + '"><small>CONDICIÓN · ' + c[2] + '</small><b>' + parts[0] + '</b></div><em>➜</em><div class="' + (n >= 2 ? 'on' : '') + '"><small>RESULTADO · ' + c[3] + '</small><b>' + (n >= 2 ? parts[1] : '?') + '</b></div></div>'; }
  M.condicionales = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('c', 'Type', COND.map(function (c, i) { return [i, c[0] + ' conditional']; }), 0), function (o) { var c = COND[+(o.c || 0)] || COND[0];
      return [{ vis: '<p class="ing-emo">' + c[5] + '</p>' + cadena(c, 0), txt: 'Un condicional une una <b>condición</b> (if…) con un <b>resultado</b>.' }, { vis: cadena(c, 1), txt: 'La condición: <b>' + c[2] + '</b>.' }, { vis: cadena(c, 2), txt: 'El resultado: <b>' + c[3] + '</b>.' }, { vis: cadena(c, 2) + frase(c[1]), txt: '<b>' + c[0] + ' conditional</b>: ' + c[4] + '. Si el if va primero, lleva coma; si va segundo, no.' }]; });
  } };
  M.condicionales_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}, L = [['If you mix blue and yellow, you ___ (get) green.', 'get', 'Zero: present'], ['If she studies, she ___ (pass) the exam.', ['will pass', "'ll pass"], 'First: will + verbo'], ['If I were a bird, I ___ (fly) over the city.', ['would fly', "'d fly"], 'Second: would + verbo'], ['If it ___ (be) sunny tomorrow, we will go to the beach.', 'is', 'First: if + present'], ['If I ___ (have) a dog, I would walk it every day.', 'had', 'Second: if + past']];
    respuesta(el, api, function () { var q = L[rot(L.length, u)]; return { cons: 'Completá: <b>' + q[0] + '</b>', campos: [{ lab: 'Verbo:', v: q[1], tipo: 'texto' }], ayuda: q[2] + '.', bien: '¡Bien!' }; }); otro(el);
  } };

  // =====================================================================================
  // 9) VOZ PASIVA: los bloques cambian de lugar
  // =====================================================================================
  var PAS = [['The chef', 'cooks', 'the pasta', 'is cooked', 'present'], ['Shakespeare', 'wrote', 'Hamlet', 'was written', 'past'], ['The students', 'painted', 'the mural', 'was painted', 'past'], ['People', 'speak', 'English', 'is spoken', 'present']];
  function bloques(q, paso) { var a = '<div class="ing-fila"><span class="suj">' + q[0] + '</span><span class="verb">' + q[1] + '</span><span class="obj">' + q[2] + '</span></div>';
    if (paso === 0) return a; var b = '<div class="ing-fila"><span class="obj">' + (paso >= 1 ? q[2].charAt(0).toUpperCase() + q[2].slice(1) : '') + '</span><span class="verb">' + (paso >= 2 ? q[3] : '?') + '</span><span class="suj">' + (paso >= 3 ? 'by ' + q[0].charAt(0).toLowerCase() + q[0].slice(1) : '') + '</span></div>';
    return a + '<p class="ing-flecha">⬇️ pasiva</p>' + b; }
  M.pasiva = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('s', 'Sentence', PAS.map(function (q, i) { return [i, q.slice(0, 3).join(' ')]; }), 0), function (o) { var q = PAS[+(o.s || 0)] || PAS[0], pas = q[2].charAt(0).toUpperCase() + q[2].slice(1) + ' ' + q[3] + ' by ' + q[0].charAt(0).toLowerCase() + q[0].slice(1) + '.';
      return [{ vis: bloques(q, 0) + frase(q.slice(0, 3).join(' ') + '.'), txt: 'Voz <b>activa</b>: el sujeto (' + q[0] + ') hace la acción.' }, { vis: bloques(q, 1), txt: 'En la <b>pasiva</b>, el objeto (' + q[2] + ') pasa adelante: lo importante es lo que le pasa.' }, { vis: bloques(q, 2), txt: 'El verbo se arma con <b>be</b> (en el mismo tiempo: ' + (q[4] === 'present' ? 'is/are' : 'was/were') + ') + <b>participio</b>: ' + q[3] + '.' }, { vis: bloques(q, 3) + frase(pas), txt: 'Quien hace la acción, si importa, va al final con <b>by</b>. Muchas veces se omite.' }]; });
  } };
  M.pasiva_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; ordenar(el, api, function () { var q = PAS[rot(PAS.length, u)], w = (q[2].charAt(0).toUpperCase() + q[2].slice(1) + ' ' + q[3] + ' by ' + q[0].charAt(0).toLowerCase() + q[0].slice(1) + '.').split(' '); return { cons: 'Pasá a voz pasiva: <b>' + q.slice(0, 3).join(' ') + '.</b> Ordená las palabras.', items: w, ayuda: 'Objeto + be + participio + by + quien lo hace.', bien: '¡Bien!' }; }); } };

  // =====================================================================================
  // 10) REPORTED SPEECH: del globo al estilo indirecto
  // =====================================================================================
  var REP = [['Anna', 'I am tired.', 'Anna said (that) she was tired.', 'am → was, I → she'], ['Leo', 'I will call you.', 'Leo said (that) he would call me.', 'will → would, I → he, you → me'], ['My mum', 'I can help you today.', 'My mum said (that) she could help me that day.', 'can → could, today → that day'], ['Tom', 'I like pizza.', 'Tom said (that) he liked pizza.', 'present simple → past simple']];
  M.reported = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('r', 'Quote', REP.map(function (q, i) { return [i, q[0] + ': ' + q[1]]; }), 0), function (o) { var q = REP[+(o.r || 0)] || REP[0], glob = '<div class="soc2-chat"><p class="izq"><b>' + q[0] + ':</b> «' + q[1] + '»</p></div>';
      return [{ vis: glob + frase(q[1]), txt: 'Estilo <b>directo</b>: las palabras exactas, entre comillas.' }, { vis: glob + '<p class="ing-flecha">⬇️ reported speech</p>' + frase(q[2]), txt: 'Estilo <b>indirecto</b> (reported speech): contamos lo que dijo, con <b>said (that)</b>.' }, { vis: card('🔁 ' + q[3]), txt: 'El verbo da <b>un paso atrás</b> en el tiempo (am → was, will → would, can → could) y cambian los pronombres y las palabras de tiempo.' }]; });
  } };
  M.reported_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; elegir(el, api, function () { var q = REP[rot(REP.length, u)], mal1 = q[2].replace(/ (was|would|could|liked) /, function (m) { return { ' was ': ' is ', ' would ': ' will ', ' could ': ' can ', ' liked ': ' likes ' }[m]; }), mal2 = q[2].replace(/ (she|he) /, ' I '); return { cons: q[0] + ': «' + q[1] + '». ¿Cómo se cuenta en reported speech?', ops: mezclar([q[2], mal1, mal2].filter(function (x, i, a) { return a.indexOf(x) === i; })), ok: q[2], ayuda: 'El verbo da un paso atrás y el pronombre cambia.', bien: '¡Bien!' }; }); } };

  // =====================================================================================
  // 11) WH-QUESTIONS: de la respuesta a la pregunta
  // =====================================================================================
  var WH = [['She lives in <u>Madrid</u>.', 'Where', 'does', 'she', 'live', 'lugar'], ['The class starts at <u>nine</u>.', 'When', 'does', 'the class', 'start', 'momento'], ['They have <u>two</u> dogs.', 'How many', 'do', 'they', 'have', 'cantidad'], ['He is sad <u>because he lost his keys</u>.', 'Why', 'is', 'he', 'sad', 'razón'], ['I like <u>pizza</u>.', 'What', 'do', 'you', 'like', 'cosa']];
  M.wh_preguntas = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('w', 'Answer', WH.map(function (q, i) { return [i, q[0].replace(/<[^>]+>/g, '')]; }), 0), function (o) { var q = WH[+(o.w || 0)] || WH[0], pr = q[1] + ' ' + q[2] + ' ' + q[3] + ' ' + q[4] + '?';
      return [{ vis: frase(q[0]), txt: 'Queremos preguntar por la parte subrayada: es un/a <b>' + q[5] + '</b>.' }, { vis: chips([[q[1], 'wh on', q[5]]]), txt: 'Para ' + q[5] + ' usamos <b>' + q[1] + '</b>.' }, { vis: chips([[q[1], 'wh'], [q[2], 'aux on', 'auxiliar'], [q[3], 'suj']]), txt: 'Después el <b>auxiliar</b> (' + q[2] + ') y el sujeto. Si el verbo es <i>be</i>, el mismo verbo hace de auxiliar.' }, { vis: chips([[q[1], 'wh'], [q[2], 'aux'], [q[3], 'suj'], [q[4] + '?', 'verb on', q[2] === 'is' ? 'el resto' : 'verbo base']]) + frase(pr), txt: 'Orden: <b>Wh + auxiliar + sujeto + verbo</b>. ' + pr }]; });
  } };
  M.wh_preguntas_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; ordenar(el, api, function () { var q = WH[rot(WH.length, u)]; return { cons: 'Armá la pregunta para la parte subrayada: ' + q[0], items: (q[1] + ' ' + q[2] + ' ' + q[3] + ' ' + q[4] + '?').split(' '), ayuda: 'Wh + auxiliar + sujeto + verbo.', bien: '¡Bien!' }; }); } };

  // =====================================================================================
  // 12) PRONUNCIACIÓN: pares mínimos y terminaciones -ed
  // =====================================================================================
  var PARES = [['ship', 'sheep', '/ɪ/ corta', '/iː/ larga', '🚢', '🐑'], ['live', 'leave', '/ɪ/ corta', '/iː/ larga', '🏠', '🚪'], ['cap', 'cup', '/æ/ boca abierta', '/ʌ/ más cerrada', '🧢', '☕'], ['full', 'fool', '/ʊ/ corta', '/uː/ larga', '🍽️', '🤡'], ['three', 'tree', '/θ/ lengua entre los dientes', '/t/', '3️⃣', '🌳']];
  var ED = [['worked', '/t/'], ['watched', '/t/'], ['laughed', '/t/'], ['played', '/d/'], ['cleaned', '/d/'], ['opened', '/d/'], ['wanted', '/ɪd/'], ['needed', '/ɪd/'], ['visited', '/ɪd/']];
  M.pronunciacion = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    if (p.modo === 'ed') { escena(el, '', function () { var g = function (k) { return '<div class="ing-tarjs">' + ED.filter(function (e) { return e[1] === k; }).map(function (e) { return '<div class="on"><b>' + e[0] + '</b>' + oir(e[0]) + '<small>' + k + '</small></div>'; }).join('') + '</div>'; };
        return [{ vis: g('/t/'), txt: 'La terminación <b>-ed</b> del pasado suena de 3 formas. Suena <b>/t/</b> después de sonidos sordos (k, ch, f, p, s, sh): work<b>ed</b>.' }, { vis: g('/d/'), txt: 'Suena <b>/d/</b> después de vocales y sonidos sonoros (l, n, m, b, g, v, r): play<b>ed</b>.' }, { vis: g('/ɪd/'), txt: 'Suena <b>/ɪd/</b> (una sílaba más) solo después de <b>t</b> o <b>d</b>: want<b>ed</b>.' }]; }); return; }
    escena(el, sel('p', 'Pair', PARES.map(function (q, i) { return [i, q[0] + ' / ' + q[1]]; }), 0), function (o) { var q = PARES[+(o.p || 0)] || PARES[0], t = function (n) { return '<div class="ing-tarjs">' + [0, 1].slice(0, n).map(function (i) { return '<div class="on"><i>' + q[4 + i] + '</i><b>' + q[i] + '</b>' + oir(q[i]) + '<small>' + q[2 + i] + '</small></div>'; }).join('') + '</div>'; };
      return [{ vis: t(1), txt: '<b>' + q[0] + '</b>: sonido ' + q[2] + '. Escuchalo y repetilo.' }, { vis: t(2), txt: '<b>' + q[1] + '</b>: sonido ' + q[3] + '. Cambia un solo sonido… ¡y cambia el significado!' }, { vis: t(2), txt: 'Estos son <b>pares mínimos</b>. Escuchá los dos seguidos varias veces y probá decirlos vos.' }]; });
  } };
  M.pronunciacion_x = { tipo: 'ejercicio', render: function (el, p, api) {
    if (p.modo === 'ed') { cajas(el, api, function () { var it = mezclar(ED.slice()).slice(0, 6); return { tit: '¿Cómo suena la terminación -ed? Decilas en voz alta.', cajas: ['/t/', '/d/', '/ɪd/'], items: it.map(function (e, i) { return { v: 'e' + i, t: e[0], c: ['/t/', '/d/', '/ɪd/'].indexOf(e[1]) }; }) }; }); otro(el); return; }
    var u = {}; conOir(el); elegir(el, api, function () { var q = PARES[rot(PARES.length, u)], k = R(0, 1); setTimeout(function () { say(q[k]); }, 300); return { cons: 'Escuchá 🔊 y tocá la palabra que suena.', html: '<p class="ing-fr">' + oir(q[k]) + '</p>', ops: [q[4] + ' ' + q[0], q[5] + ' ' + q[1]], ok: q[4 + k] + ' ' + q[k], ayuda: 'Volvé a escuchar: ' + q[2 + k] + '.', bien: '¡Sí! ' + q[k] + '.' }; });
  } };

  // =====================================================================================
  // 13) LECTURA CON ESTRATEGIA: skimming, scanning y glosario
  // =====================================================================================
  var TXT = [['A day at the zoo', 'Last Saturday, Mia and her brother Sam went to the city zoo. They arrived at <s>10 o\'clock</s> and bought two tickets for <s>8 dollars</s>. First, they saw the <g>giraffes</g>, which were eating leaves from very tall trees. Then they watched the <g>penguins</g> swim. Sam\'s favourite animal was the <g>elephant</g>. They had lunch near the lake and went home at <s>4 o\'clock</s>, tired but happy.', 'Una visita al zoológico', [['What time did they arrive?', "10 o'clock"], ['How much were the tickets?', '8 dollars']]],
    ['Plastic in the ocean', 'Every year, millions of tons of <g>plastic</g> end up in the ocean. Sea turtles sometimes eat plastic bags because they look like <g>jellyfish</g>. Scientists say that by <s>2050</s> there could be more plastic than fish in the sea. You can help: use a <g>reusable</g> bottle, say no to straws and recycle. Small actions make a big difference.', 'El plástico en el océano', [['What do turtles confuse plastic bags with?', 'jellyfish'], ['Which year do scientists mention?', '2050']]]];
  var GLO = { giraffes: 'jirafas', penguins: 'pingüinos', elephant: 'elefante', plastic: 'plástico', jellyfish: 'medusas', reusable: 'reutilizable' };
  function lectura(t, paso) { var h = t[1]; if (paso >= 1) h = h.replace(/^([^.]*\.)/, '<mark class="ing-sk">$1</mark>'); h = h.replace(/<s>(.*?)<\/s>/g, paso >= 2 ? '<mark class="ing-sc">$1</mark>' : '$1').replace(/<g>(.*?)<\/g>/g, function (m, w) { return paso >= 3 ? '<span class="ing-glo">' + w + '<small>' + (GLO[w] || '') + '</small></span>' : w; }); return '<div class="ing-texto"><h4>' + t[0] + ' ' + oir(t[1].replace(/<[^>]+>/g, '')) + '</h4><p>' + h + '</p></div>'; }
  M.lectura_en = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('t', 'Text', TXT.map(function (t, i) { return [i, t[0]]; }), 0), function (o) { var t = TXT[+(o.t || 0)] || TXT[0];
      return [{ vis: lectura(t, 0), txt: 'No hace falta entender todas las palabras para entender un texto. Vamos con estrategias.' }, { vis: lectura(t, 1), txt: '<b>Skimming</b> (leer por arriba): el título y la primera oración dan la idea general: <i>' + t[2] + '</i>.' }, { vis: lectura(t, 2), txt: '<b>Scanning</b> (buscar un dato): pasamos la vista buscando solo números, nombres u horas, sin leer todo.' }, { vis: lectura(t, 3), txt: 'Para las palabras clave que no conocemos usamos el <b>glosario</b> (o el contexto).' }, { vis: lectura(t, 3) + card('❓ ' + t[3][0][0] + ' → <b>' + t[3][0][1] + '</b>'), txt: 'Con scanning respondemos rápido: ' + t[3][0][0] + ' <b>' + t[3][0][1] + '</b>.' }]; });
  } };
  M.lectura_en_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; respuesta(el, api, function () { var t = TXT[rot(TXT.length, u)], q = pick(t[3]); return { cons: 'Hacé scanning: <b>' + q[0] + '</b>', html: lectura(t, 0), campos: [{ lab: 'Answer:', v: [q[1], q[1].replace(" o'clock", ''), q[1].replace(' dollars', '')], tipo: 'texto' }], ayuda: 'Buscá solo el dato (un número, una hora, una palabra).', bien: '¡Bien! ' + q[1] + '.' }; }); otro(el); } };

  // =====================================================================================
  // 14) FALSOS AMIGOS
  // =====================================================================================
  var FAM = [['actually', 'actualmente', 'en realidad', 'currently'], ['embarrassed', 'embarazada', 'avergonzado/a', 'pregnant'], ['carpet', 'carpeta', 'alfombra', 'folder'], ['library', 'librería', 'biblioteca', 'bookshop'], ['exit', 'éxito', 'salida', 'success'], ['sensible', 'sensible', 'sensato/a', 'sensitive'], ['assist', 'asistir (ir a)', 'ayudar', 'attend']];
  function trampa(f, n) { return '<div class="ing-trampa"><div class="on"><b>' + f[0] + '</b>' + oir(f[0]) + '</div><em>' + (n >= 1 ? '≠' : '=?') + '</em><div class="' + (n >= 1 ? 'tachado' : '') + '"><b>' + f[1] + '</b></div>' + (n >= 2 ? '<em>✔</em><div class="ok"><b>' + f[2] + '</b></div>' : '') + '</div>'; }
  M.false_friends = { tipo: 'ejemplo', pasos: true, render: function (el, p) { conOir(el);
    escena(el, sel('f', 'Word', FAM.map(function (f, i) { return [i, f[0]]; }), 0), function (o) { var f = FAM[+(o.f || 0)] || FAM[0];
      return [{ vis: trampa(f, 0), txt: '<b>' + f[0] + '</b> se parece a «' + f[1] + '»… ¿significará lo mismo?' }, { vis: trampa(f, 1), txt: '¡No! Es un <b>falso amigo</b>: palabras que se parecen pero significan otra cosa.' }, { vis: trampa(f, 2), txt: '<b>' + f[0] + '</b> significa <b>' + f[2] + '</b>.' }, { vis: trampa(f, 2) + card('🔁 Y «' + f[1] + '» en inglés se dice <b>' + f[3] + '</b>.'), txt: 'Para decir «' + f[1] + '» en inglés: <b>' + f[3] + '</b>.' }]; });
  } };
  M.false_friends_x = { tipo: 'ejercicio', render: function (el, p, api) { var u = {}; elegir(el, api, function () { var f = FAM[rot(FAM.length, u)]; return { cons: '¿Qué significa <b>' + f[0] + '</b>?', ops: mezclar([f[2], f[1], pick(FAM.filter(function (x) { return x !== f; }))[2]]), ok: f[2], ayuda: '¡Cuidado! Se parece a «' + f[1] + '», pero es un falso amigo.', bien: '¡Sí! ' + f[0] + ' = ' + f[2] + '.' }; }); } };

  var css = document.createElement('style');
  css.textContent = ['.ing-oir{border:0;background:#D7F0E9;border-radius:50%;width:32px;height:32px;cursor:pointer;font-size:.95rem;vertical-align:middle}.ing-fr{text-align:center;font-size:1.25rem;font-weight:800;margin:8px 0}.ing-emo{text-align:center;font-size:2.4rem;margin:4px 0}',
    '.ing-chips{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:8px 0}.ing-chips span{display:flex;flex-direction:column;align-items:center;padding:8px 12px;border-radius:12px;font-weight:900;font-size:1.15rem;background:#ECEFF1}.ing-chips small{font-size:.65rem;font-weight:700;color:#4b6a6c}.ing-chips .suj,.ing-fila .suj{background:#B3E5FC}.ing-chips .verb,.ing-fila .verb{background:#FFCCBC}.ing-chips .aux{background:#E1BEE7}.ing-chips .resto,.ing-fila .obj{background:#DCEDC8}.ing-chips .wh{background:#FFE082}.ing-chips .on{outline:3px solid #C2552E}',
    '.ing-tarjs{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;align-items:center;margin:6px 0}.ing-tarjs>div{min-width:100px;padding:10px;border:2px dashed #9dbdb9;border-radius:14px;display:flex;flex-direction:column;align-items:center;gap:2px}.ing-tarjs>div.on{border-style:solid;border-color:#087E83;background:#F3FBF7}.ing-tarjs b{font-size:1.25rem}.ing-tarjs i{font-style:normal;font-size:2rem}.ing-tarjs small{font-size:.75rem;color:#4b6a6c}.ing-tarjs em{font-style:normal;color:#4b6a6c}',
    '.ing-cartel{max-width:260px;margin:0 auto;padding:12px;border:4px solid #253638;border-radius:14px;background:#FFF8E1;display:flex;flex-direction:column;align-items:center}.ing-cartel i{font-style:normal;font-size:2.4rem}.ing-cartel b{font-size:1.5rem}.ing-carteles{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.ing-cartel.chico{padding:6px;border-width:2px;opacity:.6}.ing-cartel.chico.on{opacity:1;border-color:#C2552E}.ing-cartel.chico i{font-size:1.4rem}.ing-cartel.chico b{font-size:1rem}',
    '.ing-cad{display:flex;gap:6px;align-items:center;justify-content:center;flex-wrap:wrap}.ing-cad>div{flex:1 1 160px;padding:10px;border:2px dashed #9dbdb9;border-radius:14px;text-align:center}.ing-cad>div.on{border-style:solid;border-color:#087E83;background:#F3FBF7}.ing-cad small{display:block;font-size:.7rem;font-weight:800;color:#4b6a6c}.ing-cad em{font-style:normal;font-size:1.5rem;color:#C2552E}',
    '.ing-fila{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin:4px 0}.ing-fila span{min-width:60px;min-height:24px;padding:8px 12px;border-radius:12px;font-weight:900;text-align:center}.ing-flecha{text-align:center;font-weight:800;color:#C2552E;margin:2px 0}',
    '.ing-texto{max-width:460px;margin:0 auto;padding:12px 14px;border-radius:14px;background:#fff;border:2px solid #E3ECEA;text-align:left;line-height:1.6}.ing-texto h4{margin:0 0 6px}.ing-sk{background:#FFF3C4}.ing-sc{background:#FFCCBC;font-weight:800}.ing-glo{border-bottom:2px dotted #087E83;font-weight:800}.ing-glo small{margin-left:3px;font-size:.75rem;color:#066A6E;font-weight:700}',
    '.ing-trampa{display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap}.ing-trampa>div{padding:10px 14px;border-radius:14px;border:2px solid #E3ECEA;font-size:1.2rem}.ing-trampa>div.on{border-color:#087E83}.ing-trampa>div.tachado{text-decoration:line-through;color:#c2416b;border-color:#c2416b}.ing-trampa>div.ok{border-color:#3c8d2f;background:#E8F5E9}.ing-trampa em{font-style:normal;font-size:1.4rem;font-weight:900}'].join('');
  document.head.appendChild(css);
})();
