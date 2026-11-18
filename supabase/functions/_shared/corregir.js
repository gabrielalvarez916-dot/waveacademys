// Corrección SIN IA de las preguntas cerradas. Se copia igual dentro de la función `corregir` (junto a wave-calc.js).
// Las respuestas correctas viven en question_rubrics.reference_answer (el alumno nunca las lee).
// Devuelve { ia: true } cuando la pregunta necesita a la IA (abiertas, resolver y completar, o sin clave cargada).
(function (root) {
  'use strict';
  var W = root.WaveCalc;

  function norm(s) {
    return String(s == null ? '' : s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9ñ%°\/ ]+/g, ' ').replace(/\s+/g, ' ').trim();
  }
  function esNum(s) { return /^-?[\d.,\s\/]+$/.test(String(s).trim()) && /\d/.test(s); }
  function eq(resp, acepta) {
    resp = String(resp == null ? '' : resp).trim();
    return [].concat(acepta == null ? [] : acepta).some(function (x) {
      x = String(x).trim();
      if (esNum(resp) && esNum(x)) { var a = W.parseNum(resp), b = W.parseNum(x); return !isNaN(a) && Math.abs(a - b) < 1e-9; }
      return norm(resp) === norm(x);
    });
  }
  function json(s) { try { var v = JSON.parse(s); return v && typeof v === 'object' ? v : null; } catch (e) { return null; } }
  function lineas(s) { return String(s || '').split('\n').map(function (x) { return x.trim(); }).filter(Boolean); }
  function frac(ok, total) { return total ? Math.round((ok / total) * 100) : 0; }
  function lcs(a, b) {
    var m = [], i, j;
    for (i = 0; i <= a.length; i++) { m[i] = []; for (j = 0; j <= b.length; j++) m[i][j] = 0; }
    for (i = 1; i <= a.length; i++) for (j = 1; j <= b.length; j++) m[i][j] = a[i - 1] === b[j - 1] ? m[i - 1][j - 1] + 1 : Math.max(m[i - 1][j], m[i][j - 1]);
    return m[a.length][b.length];
  }
  function fichasValidas(usadas, pool, todas) {
    var cuenta = {};
    pool.forEach(function (f) { f = String(f).trim(); cuenta[f] = (cuenta[f] || 0) + 1; });
    for (var i = 0; i < usadas.length; i++) { var f = String(usadas[i]).trim(); if (!cuenta[f]) return false; cuenta[f]--; }
    if (todas) return usadas.length === pool.length;
    return true;
  }
  function tieneAlgo(s) { return String(s == null ? '' : s).trim() !== ''; }

  // q: { question_type, options, prompt }, ref: reference_answer (jsonb), resp: texto que mandó la app, seed: semilla de los números al azar
  function corregir(q, ref, resp, seed) {
    var t = q.question_type, o = q.options, r = ref;
    var vacia = !tieneAlgo(resp);
    function fin(score, correcta) { return { ia: false, score: score, correcta: correcta || '' }; }
    if (r && typeof r === 'string' && t !== 'multiple_choice' && t !== 'true_false' && t !== 'odd_one_out') r = null;

    if (t === 'multiple_choice' || t === 'true_false' || t === 'odd_one_out') {
      var c = r && typeof r === 'object' ? r.correcta : r;
      if (!tieneAlgo(c)) return { ia: true };
      return fin(!vacia && eq(resp, c) ? 100 : 0, String(c));
    }
    if (t === 'short_answer') {
      if (!r || !r.acepta) return { ia: true };
      return fin(!vacia && eq(resp, r.acepta) ? 100 : 0, [].concat(r.acepta)[0]);
    }
    if (t === 'numeric') {
      if (!r) return { ia: true };
      var esperados = [], texto = r.modo === 'texto';
      if (r.formula) {
        var vars = W.instanciar(o, seed);
        if (!vars) return fin(0, '');
        var v0 = W.evaluar(r.formula, vars);
        if (isNaN(v0)) return fin(0, '');
        esperados = [v0];
      } else esperados = [].concat(r.acepta == null ? [] : r.acepta);
      if (!esperados.length) return { ia: true };
      var mostrar = typeof esperados[0] === 'number' ? W.fmtNum(esperados[0]) : String(esperados[0]);
      if (r.unidad) mostrar += ' ' + r.unidad;
      if (vacia) return fin(0, mostrar);
      var ok;
      if (texto) ok = eq(String(resp).replace(/\s+/g, ''), esperados.map(function (x) { return String(x).replace(/\s+/g, ''); }));
      else {
        var val = W.parseNum(resp), tol = r.tolerancia || 0;
        ok = !isNaN(val) && esperados.some(function (x) { var e = typeof x === 'number' ? x : W.parseNum(x); return !isNaN(e) && Math.abs(val - e) <= tol + 1e-9 * Math.max(1, Math.abs(e)); });
      }
      if (!ok) return fin(0, mostrar);
      if (r.unidad && !texto) { var u = W.unidadDe(resp); if (u && norm(u) !== norm(r.unidad).replace(/ /g, '')) return fin(50, mostrar); }
      return fin(100, mostrar);
    }
    if (t === 'fill_blank') {
      if (!r || !Array.isArray(r.huecos)) return { ia: true };
      var rs = vacia ? [] : String(resp).split(' | ').map(function (x) { return x.replace(/^\d+\)\s*/, ''); }), bien = 0;
      r.huecos.forEach(function (ac, i) { if (tieneAlgo(rs[i]) && eq(rs[i], ac)) bien++; });
      return fin(frac(bien, r.huecos.length), r.huecos.map(function (a) { return [].concat(a)[0]; }).join(' · '));
    }
    if (t === 'ordering') {
      if (!r || !Array.isArray(r.orden)) return { ia: true };
      var ro = vacia ? [] : String(resp).split(' → ');
      var b2 = 0; r.orden.forEach(function (x, i) { if (ro[i] != null && norm(ro[i]) === norm(x)) b2++; });
      return fin(frac(b2, r.orden.length), r.orden.join(' → '));
    }
    if (t === 'matching' || t === 'classify') {
      var mapa = t === 'matching' ? (r && r.pares) : (r && r.categorias);
      if (!mapa) return { ia: true };
      var sep = t === 'matching' ? ' = ' : ' → ', dados = {};
      lineas(resp).forEach(function (l) { var k = l.indexOf(sep); if (k > 0) dados[norm(l.slice(0, k))] = l.slice(k + sep.length); });
      var claves = Object.keys(mapa), b3 = 0;
      claves.forEach(function (k) { if (dados[norm(k)] != null && norm(dados[norm(k)]) === norm(mapa[k])) b3++; });
      return fin(frac(b3, claves.length), claves.map(function (k) { return k + sep + mapa[k]; }).join('; '));
    }
    if (t === 'table_fill') {
      if (!r || !r.celdas) return { ia: true };
      var cel = {};
      lineas(resp).forEach(function (l) { var m = /^Fila (\d+), columna (.*?): (.*)$/.exec(l); if (m) cel[m[1] + '|' + norm(m[2])] = m[3]; });
      var ks = Object.keys(r.celdas), b4 = 0;
      ks.forEach(function (k) { var p = k.split('|'), d = cel[p[0] + '|' + norm(p[1])]; if (d != null && eq(d, r.celdas[k])) b4++; });
      return fin(frac(b4, ks.length), ks.map(function (k) { return k.replace('|', ' / ') + ': ' + [].concat(r.celdas[k])[0]; }).join('; '));
    }
    if (t === 'multi_select') {
      if (!r || !Array.isArray(r.correctas)) return { ia: true };
      var mar = vacia ? [] : String(resp).split(' | ');
      var aciertos = mar.filter(function (x) { return r.correctas.some(function (c) { return norm(c) === norm(x); }); }).length;
      var errores = mar.length - aciertos;
      return fin(Math.max(0, frac(aciertos - errores, r.correctas.length)), r.correctas.join(' | '));
    }
    if (t === 'tap_text') {
      if (!r || !Array.isArray(r.tocar) && !r.categorias) return { ia: true };
      var d = json(resp) || {}, seg = (o && o.segmentos) || [];
      var esperado = r.categorias ? r.categorias : null, idxs = esperado ? Object.keys(esperado) : r.tocar.map(String);
      var elegidos = esperado ? Object.keys(d.cat || {}).filter(function (k) { return d.cat[k]; }) : (d.sel || []).map(String);
      var hits = 0;
      idxs.forEach(function (k) {
        if (elegidos.indexOf(k) < 0) return;
        if (esperado && norm(d.cat[k]) !== norm(esperado[k])) return;
        hits++;
      });
      var extras = elegidos.filter(function (k) { return idxs.indexOf(k) < 0; }).length, total = idxs.length;
      if (r.correccion) { total++; if (tieneAlgo(d.corr) && eq(d.corr, r.correccion)) hits++; }
      var mostrarT = idxs.map(function (k) { return '«' + (seg[+k] != null ? seg[+k] : k) + '»' + (esperado ? ' (' + esperado[k] + ')' : ''); }).join(', ') + (r.correccion ? ' → ' + [].concat(r.correccion)[0] : '');
      return fin(Math.max(0, Math.round(((hits - extras * 0.5) / total) * 100)), mostrarT);
    }
    if (t === 'tokens') {
      var dt = json(resp) || {}, fich = Array.isArray(dt.t) ? dt.t.map(String) : [];
      if (o && o.objetivo != null) {
        var esOp = function (x) { return /^[+\-−–×x·÷:*\/()^%]$/.test(String(x).trim()); };
        var pool = (o.fichas || []).map(String).filter(function (x) { return !esOp(x); });
        var permitidos = (o.operadores || ['+', '−', '×', '÷', '(', ')']).map(String);
        var numUsados = fich.filter(function (x) { return !esOp(x); }), opUsados = fich.filter(esOp);
        var ej = r && r.ejemplo ? r.ejemplo : '';
        if (!fich.length) return fin(0, ej);
        if (!fichasValidas(numUsados, pool, o.usar_todas !== false)) return fin(0, ej);
        if (opUsados.some(function (x) { return permitidos.indexOf(String(x).trim()) < 0; })) return fin(0, ej);
        var vv; try { vv = W.evaluarFichas(fich); } catch (e) { vv = NaN; }
        return fin(!isNaN(vv) && Math.abs(vv - o.objetivo) < 1e-9 ? 100 : 0, r && r.ejemplo ? r.ejemplo : '');
      }
      if (!r || !Array.isArray(r.soluciones)) return { ia: true };
      var mejor = 0, exacto = false;
      r.soluciones.forEach(function (s) {
        s = s.map(String);
        if (s.length === fich.length && s.every(function (x, i) { return norm(x) === norm(fich[i]); })) exacto = true;
        mejor = Math.max(mejor, s.length ? lcs(s.map(norm), fich.map(norm)) / s.length : 0);
      });
      return fin(exacto ? 100 : Math.round(mejor * 50), r.soluciones[0].join(' '));
    }
    if (t === 'keywords') {
      if (!r || !Array.isArray(r.grupos)) return { ia: true };
      var tx = ' ' + norm(resp) + ' ', presentes = 0, faltan = [];
      r.grupos.forEach(function (g) {
        var hay = [].concat(g).some(function (syn) {
          var s = norm(syn), pref = /\*$/.test(String(syn));
          s = s.replace(/\*$/, '').trim();
          if (!s) return false;
          return pref ? tx.indexOf(' ' + s) >= 0 : tx.indexOf(' ' + s + ' ') >= 0;
        });
        if (hay) presentes++; else faltan.push([].concat(g)[0]);
      });
      var min = r.minimo || r.grupos.length;
      return { ia: false, score: vacia ? 0 : Math.min(100, Math.round((presentes / min) * 100)), correcta: r.grupos.map(function (g) { return [].concat(g)[0]; }).join(', '), faltan: faltan };
    }
    if (t === 'label_image') {
      if (!r || !r.puntos) return { ia: true };
      var dl = json(resp) || {}, ids = Object.keys(r.puntos), b5 = 0;
      ids.forEach(function (k) { if (tieneAlgo(dl[k]) && norm(dl[k]) === norm(r.puntos[k])) b5++; });
      return fin(frac(b5, ids.length), ids.map(function (k) { return k + ': ' + r.puntos[k]; }).join('; '));
    }
    return { ia: true };
  }

  // Devolución para el alumno. mostrar = true en actividades (se muestra la respuesta correcta y la explicación); en el examen no.
  function devolucion(res, explicacion, mostrar) {
    var s = res.score, txt;
    if (s >= 100) txt = '¡Correcto!';
    else if (s > 0) txt = 'Vas bien, pero falta.';
    else txt = 'Esta no es.';
    if (res.faltan && res.faltan.length && s < 100 && mostrar) txt += ' Te faltó mencionar: ' + res.faltan.join(', ') + '.';
    else if (s < 100 && mostrar && res.correcta) txt += ' Respuesta: ' + res.correcta + '.';
    if (mostrar && explicacion) txt += ' ' + explicacion;
    return txt;
  }

  root.WaveCorregir = { corregir: corregir, devolucion: devolucion, norm: norm, eq: eq };
})(typeof globalThis !== 'undefined' ? globalThis : this);
