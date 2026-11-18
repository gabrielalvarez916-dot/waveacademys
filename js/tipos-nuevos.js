// Preguntas de las piezas nuevas (se corrigen sin IA en la función `corregir`):
//   numeric     · respuesta numérica (sirve también para "cuentas con números al azar", ver wave-calc.js)
//   tap_text    · tocá el texto · subrayá y clasificá · detective del error
//   tokens      · armá con fichas · reto de armado
//   keywords    · respuesta escrita con palabras clave
//   label_image · rotulá el dibujo
// Este módulo dibuja el campo, lee lo que respondió el alumno y lo muestra en el resultado. No conoce las respuestas correctas.
window.WaveTipos = (function () {
  'use strict';
  var TIPOS = ['numeric', 'tap_text', 'tokens', 'keywords', 'label_image'];
  var C = function () { return window.WaveCalc; };

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function lista(x) { return Array.isArray(x) ? x : []; }
  function w(i) { return ' data-w="' + i + '"'; }
  function soporta(t) { return TIPOS.indexOf(t) >= 0; }

  // ---------- Dibujo del campo ----------
  function html(q, i, enunciado) {
    var o = q.options || {}, t = q.question_type, h = '<p>' + esc(enunciado) + '</p>';

    if (t === 'numeric') {
      return h + '<div class="nu-fila"><input type="text" inputmode="decimal" class="mt-txt nu-in"' + w(i) + ' data-k="num" maxlength="40" autocomplete="off" placeholder="' + esc(o.placeholder || 'Tu resultado') + '">' +
        (o.unidad ? '<span class="nu-un">' + esc(o.unidad) + '</span>' : '') + '</div>';
    }

    if (t === 'keywords') {
      return h + (o.ayuda ? '<small class="mt-ayuda">' + esc(o.ayuda) + '</small>' : '') +
        '<textarea class="mt-txt kw-in"' + w(i) + ' data-k="kw" rows="4" maxlength="1200" placeholder="Escribí tu respuesta con tus palabras"></textarea>';
    }

    if (t === 'tap_text') {
      var segs = lista(o.segmentos), cats = lista(o.categorias), modo = o.modo === 'lineas' ? 'lineas' : 'palabras';
      if (!segs.length) return null;
      h += '<small class="mt-ayuda">' + (cats.length ? 'Elegí una opción y tocá las partes del texto que correspondan. Tocá de nuevo para sacarla.' : 'Tocá las partes del texto que correspondan. Tocá de nuevo para sacarla.') + '</small>';
      if (cats.length) {
        h += '<div class="tp-cats"' + w(i) + '>' + cats.map(function (c, k) {
          return '<button type="button" class="tp-cat c' + (k % 5) + (k === 0 ? ' on' : '') + '" data-tp="cat" data-c="' + k + '">' + esc(c) + '</button>';
        }).join('') + '</div>';
      }
      h += '<div class="tp-texto ' + modo + '"' + w(i) + '>' + segs.map(function (s, k) {
        return '<span class="tp-seg" data-tp="seg" data-i="' + k + '" tabindex="0">' + esc(s) + '</span>';
      }).join(modo === 'lineas' ? '' : ' ') + '</div>';
      if (o.pide_correccion) h += '<label class="mt-lbl">' + esc(o.pide_correccion) + '</label><input type="text" class="mt-txt tp-corr"' + w(i) + ' data-k="corr" maxlength="120" autocomplete="off">';
      return h;
    }

    if (t === 'tokens') {
      var fichas = lista(o.fichas), reto = o.objetivo != null, ops = reto ? lista(o.operadores).length ? o.operadores : ['+', '−', '×', '÷', '(', ')'] : [];
      if (!fichas.length) return null;
      h += '<small class="mt-ayuda">' + (reto ? 'Tocá las fichas para armar la cuenta. Usá ' + (o.usar_todas === false ? 'los números que quieras' : 'todos los números') + ', cada uno una vez.' : 'Tocá las fichas en el orden correcto. Tocá una ficha armada para sacarla. Puede haber fichas que sobren.') + '</small>';
      if (reto) h += '<div class="tk-obj">Tiene que dar <b>' + esc(C().fmtNum(+o.objetivo)) + '</b></div>';
      h += '<div class="tk-arm"' + w(i) + ' data-tk="arm"></div>' + (reto ? '<div class="tk-val"' + w(i) + '></div>' : '');
      h += '<div class="tk-banco"' + w(i) + '>' + fichas.map(function (f, k) {
        return '<button type="button" class="tk-f" data-tk="banco" data-b="' + k + '" data-v="' + esc(f) + '">' + esc(f) + '</button>';
      }).join('') + '</div>';
      if (ops.length) h += '<div class="tk-ops">' + ops.map(function (x) { return '<button type="button" class="tk-f op" data-tk="op" data-v="' + esc(x) + '">' + esc(x) + '</button>'; }).join('') + '</div>';
      h += '<div class="tk-pie"><button type="button" class="mt-boton suave chico" data-tk="borrar">Borrar todo</button></div>';
      return h;
    }

    if (t === 'label_image') {
      var pts = lista(o.puntos), rot = lista(o.rotulos);
      if (!o.imagen || !pts.length || !rot.length) return null;
      h += '<small class="mt-ayuda">Mirá cada número del dibujo y elegí qué es.</small>';
      h += '<div class="li-wrap"><img class="li-img" src="' + esc(o.imagen) + '" alt="' + esc(o.alt || 'Dibujo para rotular') + '">' + pts.map(function (p) {
        return '<span class="li-pt" data-tp="pt" data-id="' + esc(p.id) + '" style="left:' + (+p.x) + '%;top:' + (+p.y) + '%">' + esc(p.id) + '</span>';
      }).join('') + '</div><div class="mt-pares">' + pts.map(function (p) {
        return '<div class="mt-par"><span><b class="li-n">' + esc(p.id) + '</b></span><select class="mt-sel"' + w(i) + ' data-k="' + esc(p.id) + '" data-pt="' + esc(p.id) + '"><option value="">Elegí…</option>' +
          rot.map(function (r) { return '<option value="' + esc(r) + '">' + esc(r) + '</option>'; }).join('') + '</select></div>';
      }).join('') + '</div>';
      return h;
    }
    return null;
  }

  // ---------- Lo que respondió el alumno (texto para el corrector) ----------
  function leer(q, i, root) {
    var t = q.question_type, o = q.options || {}, sel = '[data-w="' + i + '"]';
    if (t === 'numeric') { var n = root.querySelector('input' + sel); return n ? n.value.trim() : ''; }
    if (t === 'keywords') { var k = root.querySelector('textarea' + sel); return k ? k.value.trim() : ''; }
    if (t === 'tap_text') {
      var cats = lista(o.categorias), cont = root.querySelector('.tp-texto' + sel), out = { sel: [], cat: {} }, algo = false;
      if (cont) Array.prototype.forEach.call(cont.querySelectorAll('.tp-seg'), function (s) {
        var idx = +s.getAttribute('data-i');
        if (cats.length) { var c = s.getAttribute('data-cat'); if (c != null && c !== '') { out.cat[idx] = cats[+c]; algo = true; } }
        else if (s.classList.contains('on')) { out.sel.push(idx); algo = true; }
      });
      var cr = root.querySelector('input.tp-corr' + sel);
      if (cr && cr.value.trim()) { out.corr = cr.value.trim(); algo = true; }
      return algo ? JSON.stringify(out) : '';
    }
    if (t === 'tokens') {
      var arm = root.querySelector('.tk-arm' + sel);
      var v = arm ? Array.prototype.map.call(arm.querySelectorAll('.tk-f'), function (b) { return b.getAttribute('data-v'); }) : [];
      return v.length ? JSON.stringify({ t: v }) : '';
    }
    if (t === 'label_image') {
      var res = {}, alguno = false;
      Array.prototype.forEach.call(root.querySelectorAll('select' + sel), function (s) { if (s.value) { res[s.getAttribute('data-pt')] = s.value; alguno = true; } });
      return alguno ? JSON.stringify(res) : '';
    }
    return null;
  }

  // ---------- Respuesta del alumno en el resultado ----------
  function mostrar(q, ans) {
    if (!ans) return '';
    var o = q.options || {}, t = q.question_type, d;
    try { d = JSON.parse(ans); } catch (e) { return ans; }
    if (t === 'tap_text') {
      var segs = lista(o.segmentos), partes = [];
      Object.keys(d.cat || {}).forEach(function (k) { partes.push('«' + (segs[+k] != null ? segs[+k] : k) + '» (' + d.cat[k] + ')'); });
      (d.sel || []).forEach(function (k) { partes.push('«' + (segs[+k] != null ? segs[+k] : k) + '»'); });
      if (d.corr) partes.push('→ ' + d.corr);
      return partes.join(', ');
    }
    if (t === 'tokens') return (d.t || []).join(' ');
    if (t === 'label_image') return Object.keys(d).map(function (k) { return k + ': ' + d[k]; }).join(' · ');
    return ans;
  }

  // ---------- Interacción (se enlaza una sola vez por ventana de cuestionario) ----------
  function valor(scope) {
    var v = scope.querySelector('.tk-val'), arm = scope.querySelector('.tk-arm');
    if (!v || !arm) return;
    var fs = Array.prototype.map.call(arm.querySelectorAll('.tk-f'), function (b) { return b.getAttribute('data-v'); });
    var r = NaN;
    if (fs.length) { try { r = C().evaluarFichas(fs); } catch (e) { r = NaN; } }
    v.textContent = isNaN(r) ? '' : '= ' + C().fmtNum(Math.round(r * 1e6) / 1e6);
  }
  function enlazar(root) {
    if (root.__tipos) return;
    root.__tipos = true;
    function accion(ev) {
      var b = ev.target.closest('[data-tp],[data-tk]');
      if (!b || !root.contains(b)) return;
      var scope = b.closest('.mt-preg-c');
      if (!scope) return;
      var tp = b.getAttribute('data-tp');
      if (tp === 'cat') {
        Array.prototype.forEach.call(scope.querySelectorAll('.tp-cat'), function (x) { x.classList.remove('on'); });
        b.classList.add('on');
        return;
      }
      if (tp === 'seg') {
        var cat = scope.querySelector('.tp-cat.on');
        if (cat) {
          var k = cat.getAttribute('data-c');
          if (b.getAttribute('data-cat') === k) { b.removeAttribute('data-cat'); b.className = 'tp-seg'; }
          else { b.setAttribute('data-cat', k); b.className = 'tp-seg on c' + (+k % 5); }
        } else b.classList.toggle('on');
        return;
      }
      if (tp === 'pt') {
        var s = scope.querySelector('select[data-pt="' + b.getAttribute('data-id') + '"]');
        if (s) s.focus();
        return;
      }
      var tk = b.getAttribute('data-tk'), arm = scope.querySelector('.tk-arm');
      if (!arm) return;
      if (tk === 'banco' || tk === 'op') {
        if (b.disabled) return;
        var n = document.createElement('button');
        n.type = 'button'; n.className = 'tk-f en' + (tk === 'op' ? ' op' : ''); n.setAttribute('data-tk', 'quitar'); n.setAttribute('data-v', b.getAttribute('data-v')); n.textContent = b.textContent;
        if (tk === 'banco') { n.setAttribute('data-b', b.getAttribute('data-b')); b.disabled = true; }
        arm.appendChild(n); valor(scope);
      } else if (tk === 'quitar') {
        var bi = b.getAttribute('data-b');
        if (bi != null) { var o = scope.querySelector('.tk-banco [data-b="' + bi + '"]'); if (o) o.disabled = false; }
        b.remove(); valor(scope);
      } else if (tk === 'borrar') {
        arm.innerHTML = '';
        Array.prototype.forEach.call(scope.querySelectorAll('.tk-banco .tk-f'), function (x) { x.disabled = false; });
        valor(scope);
      }
    }
    root.addEventListener('click', accion);
    root.addEventListener('keydown', function (ev) {
      if ((ev.key === 'Enter' || ev.key === ' ') && ev.target.closest && ev.target.closest('.tp-seg')) { ev.preventDefault(); accion(ev); }
    });
  }

  return { tipos: TIPOS, soporta: soporta, html: html, leer: leer, mostrar: mostrar, enlazar: enlazar };
})();
