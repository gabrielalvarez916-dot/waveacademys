// Avatares de Wave Academy's: se dibujan como SVG en el navegador, no hay imágenes para subir.
// Inicial y primaria: animalitos. Secundaria: personas (estilo más adulto, personalizable).
// En la base se guarda solo una configuración chica, por ejemplo:
//   {"t":"animal","a":"zorro","f":"#CDEBE3"}
//   {"t":"persona","piel":2,"estilo":1,"pelo":3,"ropa":0,"f":"#D9DDF7"}
window.Wave = window.Wave || {};
Wave.avatar = (function () {
  var FONDOS = ['#CDEBE3', '#BFE3F2', '#F6D9C6', '#E6D8F3', '#F7E3A6', '#F5C6D0', '#C9D8C5', '#D6DCE4'];
  var PIELES = ['#FADCC2', '#F1C27D', '#D9A066', '#B9774B', '#8D5524', '#5C3A21'];
  var PELOS = ['#1F1A17', '#4A2F1D', '#8B5A2B', '#C9A24B', '#B5472F', '#8A8F98'];
  var ROPAS = ['#087E83', '#253638', '#6366F1', '#C2410C', '#BE185D', '#4D7C0F'];
  var ESTILOS = ['Corto', 'Largo', 'Rulos', 'Rodete', 'Rapado', 'Ondas'];

  var ANIMALES = [
    ['gato', 'Gato'], ['perro', 'Perro'], ['zorro', 'Zorro'], ['panda', 'Panda'], ['conejo', 'Conejo'],
    ['oso', 'Oso'], ['buho', 'Búho'], ['rana', 'Rana'], ['pinguino', 'Pingüino'], ['leon', 'León']
  ];

  function C(cx, cy, r, fill, extra) { return '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="' + fill + '"' + (extra || '') + '/>'; }
  function E(cx, cy, rx, ry, fill, extra) { return '<ellipse cx="' + cx + '" cy="' + cy + '" rx="' + rx + '" ry="' + ry + '" fill="' + fill + '"' + (extra || '') + '/>'; }
  function Pg(pts, fill) { return '<polygon points="' + pts + '" fill="' + fill + '"/>'; }
  function Pa(d, fill, extra) { return '<path d="' + d + '" fill="' + fill + '"' + (extra || '') + '/>'; }
  function trazo(d, color, w) { return '<path d="' + d + '" fill="none" stroke="' + color + '" stroke-width="' + (w || 2) + '" stroke-linecap="round" stroke-linejoin="round"/>'; }

  function ojos(y, dx, r) {
    r = r || 3.6;
    return C(50 - dx, y, r, '#2B2B2B') + C(50 + dx, y, r, '#2B2B2B') +
      C(50 - dx + 1.2, y - 1.2, 1.1, '#fff') + C(50 + dx + 1.2, y - 1.2, 1.1, '#fff');
  }

  var DIBUJO = {
    gato: function () {
      return Pg('25,44 29,16 47,32', '#E89A3C') + Pg('75,44 71,16 53,32', '#E89A3C') +
        Pg('30,38 32,24 42,32', '#F6B8C0') + Pg('70,38 68,24 58,32', '#F6B8C0') +
        C(50, 58, 28, '#F4A950') +
        trazo('M50 32v8M43 34l1 6M57 34l-1 6', '#C9772A', 2.2) +
        ojos(56, 11) + Pg('46.5,63 53.5,63 50,67.5', '#E36C7E') +
        trazo('M50 67.5v3M50 70.5q-4 3-8 0M50 70.5q4 3 8 0', '#8A4B1E', 1.6) +
        trazo('M20 62l14 2M20 70l14-2M80 62l-14 2M80 70l-14-2', '#fff', 1.6);
    },
    perro: function () {
      return E(24, 52, 9, 19, '#7A4A2C', ' transform="rotate(14 24 52)"') + E(76, 52, 9, 19, '#7A4A2C', ' transform="rotate(-14 76 52)"') +
        C(50, 55, 28, '#DDAA72') + E(50, 67, 15, 12, '#F6E3C5') + ojos(52, 11) +
        E(50, 62, 6.5, 4.8, '#2B2B2B') + C(48.5, 60.6, 1.3, '#fff') +
        trazo('M50 67v4M50 71q-5 4-9 0M50 71q5 4 9 0', '#6B3E22', 1.7) + Pa('M46 73q4 9 8 0z', '#EF7A8A');
    },
    zorro: function () {
      return Pg('24,46 26,14 46,32', '#EE7B30') + Pg('76,46 74,14 54,32', '#EE7B30') +
        Pg('27,38 28,22 39,31', '#3A2A22') + Pg('73,38 72,22 61,31', '#3A2A22') +
        C(50, 56, 28, '#EE7B30') +
        Pa('M24 58Q50 76 76 58Q72 84 50 91Q28 84 24 58Z', '#FFF4E6') +
        ojos(54, 11) + C(50, 84, 4, '#2B2B2B') + trazo('M50 88v2', '#2B2B2B', 1.6);
    },
    panda: function () {
      return C(27, 32, 11, '#26292E') + C(73, 32, 11, '#26292E') + C(50, 58, 29, '#FFFFFF') +
        E(38, 56, 7.5, 9.5, '#26292E', ' transform="rotate(20 38 56)"') + E(62, 56, 7.5, 9.5, '#26292E', ' transform="rotate(-20 62 56)"') +
        C(38.5, 56, 2.6, '#fff') + C(61.5, 56, 2.6, '#fff') + C(39, 56, 1.4, '#26292E') + C(61, 56, 1.4, '#26292E') +
        E(50, 68, 4.8, 3.4, '#26292E') + trazo('M50 71.5q-5 4-9 0M50 71.5q5 4 9 0', '#26292E', 1.6);
    },
    conejo: function () {
      return E(37, 24, 8.5, 21, '#F7F1EA') + E(63, 24, 8.5, 21, '#F7F1EA') +
        E(37, 25, 4, 15, '#F6B8C0') + E(63, 25, 4, 15, '#F6B8C0') +
        C(50, 63, 27, '#F7F1EA') + C(36, 69, 5, '#F6B8C0', ' opacity=".6"') + C(64, 69, 5, '#F6B8C0', ' opacity=".6"') +
        ojos(60, 11) + Pg('46.5,66 53.5,66 50,70', '#E36C7E') +
        trazo('M50 70v2M50 72q-4 3-7 0M50 72q4 3 7 0', '#9A7B6B', 1.5) +
        '<rect x="47" y="73" width="6" height="6" rx="1.5" fill="#fff" stroke="#E3D8CC" stroke-width="1"/>';
    },
    oso: function () {
      return C(28, 34, 10, '#7A4E2D') + C(72, 34, 10, '#7A4E2D') + C(28, 34, 5, '#C89B72') + C(72, 34, 5, '#C89B72') +
        C(50, 58, 29, '#8B5E3C') + E(50, 67, 14, 11, '#D9B68C') + ojos(53, 12) +
        E(50, 62, 6, 4.5, '#2B2B2B') + C(48.5, 60.7, 1.3, '#fff') + trazo('M50 66.5v3M50 69.5q-4 3-8 0M50 69.5q4 3 8 0', '#4A2F1D', 1.6);
    },
    buho: function () {
      return Pg('26,42 24,18 44,32', '#8A6A49') + Pg('74,42 76,18 56,32', '#8A6A49') +
        E(50, 56, 30, 29, '#A67F5B') + Pa('M34 80q16 12 32 0q-4 12-16 12q-12 0-16-12z', '#D8BE9B') +
        C(37, 52, 13, '#F5E9D4') + C(63, 52, 13, '#F5E9D4') +
        C(37, 52, 7, '#F2B632') + C(63, 52, 7, '#F2B632') + C(37, 52, 3.6, '#2B2B2B') + C(63, 52, 3.6, '#2B2B2B') +
        C(38.3, 50.7, 1.1, '#fff') + C(64.3, 50.7, 1.1, '#fff') + Pg('46,60 54,60 50,70', '#F08A24');
    },
    rana: function () {
      return E(50, 62, 31, 25, '#6DBF4B') + C(33, 38, 12, '#6DBF4B') + C(67, 38, 12, '#6DBF4B') +
        C(33, 38, 8, '#fff') + C(67, 38, 8, '#fff') + C(34, 39, 4, '#2B2B2B') + C(66, 39, 4, '#2B2B2B') +
        C(35, 37.5, 1.2, '#fff') + C(67, 37.5, 1.2, '#fff') +
        C(26, 66, 5, '#F59AA8', ' opacity=".6"') + C(74, 66, 5, '#F59AA8', ' opacity=".6"') +
        C(46, 56, 1.1, '#3F7F2A') + C(54, 56, 1.1, '#3F7F2A') +
        trazo('M30 66q20 16 40 0', '#2F5F1F', 2.2);
    },
    pinguino: function () {
      return C(50, 58, 29, '#2B3A4A') + C(40, 57, 13.5, '#fff') + C(60, 57, 13.5, '#fff') +
        ojos(54, 10, 3.4) + E(50, 65, 7, 4.5, '#F08A24') + trazo('M43 65h14', '#C96A12', 1.2) +
        C(30, 66, 4.5, '#F59AA8', ' opacity=".55"') + C(70, 66, 4.5, '#F59AA8', ' opacity=".55"');
    },
    leon: function () {
      return C(50, 56, 40, '#C8782A') + C(28, 30, 9, '#F5C26B') + C(72, 30, 9, '#F5C26B') +
        C(28, 30, 4.5, '#E8A8A0') + C(72, 30, 4.5, '#E8A8A0') +
        C(50, 58, 27, '#F5C26B') + E(50, 67, 13, 10, '#FBE3B0') + ojos(54, 11) +
        Pg('45.5,61 54.5,61 50,67', '#8A4B1E') + trazo('M50 67v4M50 71q-5 3-9 0M50 71q5 3 9 0', '#8A4B1E', 1.6) +
        C(41, 70, 1, '#C8782A') + C(59, 70, 1, '#C8782A');
    }
  };

  var PELO_ATRAS = {
    0: function () { return ''; },
    1: function (c) { return Pa('M30 48Q28 22 50 22Q72 22 70 48L74 88L26 88Z', c); },
    2: function (c) { return C(33, 32, 10, c) + C(50, 25, 11, c) + C(67, 32, 10, c) + C(28, 46, 8, c) + C(72, 46, 8, c); },
    3: function (c) { return C(50, 15, 8.5, c); },
    4: function () { return ''; },
    5: function (c) { return Pa('M30 46Q28 22 50 22Q72 22 70 46Q74 62 70 70Q60 62 50 66Q40 62 30 70Q26 62 30 46Z', c); }
  };

  var PELO_FRENTE = {
    0: function (c) { return Pa('M32 46Q30 24 50 24Q70 24 68 46Q62 34 50 34Q38 34 32 46Z', c); },
    1: function (c) { return Pa('M32 46Q30 24 50 24Q70 24 68 46Q64 33 54 32Q42 36 32 46Z', c); },
    2: function (c) { return C(40, 31, 8, c) + C(54, 28, 9, c) + C(62, 35, 7, c); },
    3: function (c) { return Pa('M32 46Q30 24 50 24Q70 24 68 46Q62 34 50 34Q38 34 32 46Z', c); },
    4: function (c) { return Pa('M33 44Q33 28 50 28Q67 28 67 44Q60 36 50 36Q40 36 33 44Z', c, ' opacity=".55"'); },
    5: function (c) { return Pa('M32 48Q30 24 50 24Q70 24 68 48Q66 34 54 31Q40 40 32 48Z', c); }
  };

  function persona(cfg) {
    var piel = PIELES[cfg.piel], pelo = PELOS[cfg.pelo], ropa = ROPAS[cfg.ropa], e = cfg.estilo;
    return PELO_ATRAS[e](pelo) +
      Pa('M14 100Q16 74 50 72Q84 74 86 100Z', ropa) +
      '<rect x="43" y="58" width="14" height="16" rx="6" fill="' + piel + '"/>' +
      Pa('M42 72Q50 80 58 72', 'none', ' stroke="rgba(255,255,255,.55)" stroke-width="2" stroke-linecap="round"') +
      E(50, 45, 17, 20, piel) + E(33.5, 47, 3, 4.2, piel) + E(66.5, 47, 3, 4.2, piel) +
      PELO_FRENTE[e](pelo) +
      C(43, 47, 2.1, '#2B2B2B') + C(57, 47, 2.1, '#2B2B2B') +
      trazo('M39.5 41.5q3.5-2 7 0M53.5 41.5q3.5-2 7 0', pelo, 1.6) +
      trazo('M44.5 55q5.5 4 11 0', '#7A3E32', 1.7);
  }

  function esHex(c) { return typeof c === 'string' && /^#[0-9a-fA-F]{6}$/.test(c); }
  function idx(v, lista) { v = Number(v); return v >= 0 && v < lista.length && v % 1 === 0 ? v : 0; }

  // Deja la configuración siempre válida (nunca se dibuja nada que no esté en las listas)
  function limpiar(cfg, nivel) {
    cfg = cfg && typeof cfg === 'object' ? cfg : {};
    var fondo = esHex(cfg.f) ? cfg.f : FONDOS[0];
    if (cfg.t === 'persona' && nivel === 'avanzado') {
      return { t: 'persona', piel: idx(cfg.piel, PIELES), estilo: idx(cfg.estilo, ESTILOS),
               pelo: idx(cfg.pelo, PELOS), ropa: idx(cfg.ropa, ROPAS), f: fondo };
    }
    if (cfg.t === 'animal' && DIBUJO[cfg.a] && nivel !== 'avanzado') {
      return { t: 'animal', a: cfg.a, f: fondo };
    }
    return porDefecto(nivel);
  }

  function porDefecto(nivel) {
    return nivel === 'avanzado'
      ? { t: 'persona', piel: 1, estilo: 0, pelo: 1, ropa: 0, f: FONDOS[0] }
      : { t: 'animal', a: 'gato', f: FONDOS[0] };
  }

  function svg(cfg, nivel, tam) {
    var c = limpiar(cfg, nivel);
    var cuerpo = c.t === 'persona' ? persona(c) : DIBUJO[c.a]();
    return '<svg class="avatar-svg" viewBox="0 0 100 100" width="' + (tam || 96) + '" height="' + (tam || 96) +
      '" role="img" aria-label="Avatar" style="border-radius:50%;display:block">' +
      '<rect width="100" height="100" fill="' + c.f + '"/>' + cuerpo + '</svg>';
  }

  return {
    svg: svg, limpiar: limpiar, porDefecto: porDefecto,
    FONDOS: FONDOS, PIELES: PIELES, PELOS: PELOS, ROPAS: ROPAS, ESTILOS: ESTILOS, ANIMALES: ANIMALES
  };
})();
