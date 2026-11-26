/* LECCIÓN INTERACTIVA (reemplaza al PDF dentro del nivel; el PDF queda en Recursos).
   Se arma sola desde el borrador de la lección (lesson_drafts.contenido): cada sección es un tema con
   explicación (bloques) + ejemplo paso a paso con números que cambian + botón de práctica de ese tema; al final, el resumen.
   La "practica" de cada sección (la escribe la máquina de misiones, ver docs/leccion-interactiva.md):
     { vars, calculadas, reglas,            // números al azar (wave-calc.js), opcional
       enunciado, pasos:[..], respuesta: {formula} | {acepta:[..]} | {opciones:[..], correcta},
       unidad, variantes:[{enunciado, pasos, respuesta}] }   // sin números al azar: ejemplos que se van rotando
   La práctica es formativa: se comprueba en el momento y no se guarda nota. */
window.WaveLeccion = (function () {
  'use strict';
  var C = function () { return window.WaveCalc; };
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  // el borrador trae <b>, <i>, <br>, <sup>, <sub>: se respetan solo esas etiquetas
  function rico(s) { return esc(s).replace(/&lt;(\/?)(b|i|em|strong|br|sup|sub)\s*\/?&gt;/gi, '<$1$2>'); }
  function sonar(n) { try { if (window.WaveJuego) WaveJuego.sonar(n); } catch (_) {} }
  var NO_TOCAR = { png_base64: 1, vars: 1, calculadas: 1, reglas: 1, formula: 1 };
  function neutral(o, k) {
    if (typeof o === 'string') return NO_TOCAR[k] || !window.WaveNeutro ? o : WaveNeutro.neutro(o);
    if (Array.isArray(o)) return o.map(function (x) { return neutral(x, k); });
    if (o && typeof o === 'object') {
      var r = {}; Object.keys(o).forEach(function (kk) { if (kk !== 'neutro') r[kk] = NO_TOCAR[kk] ? o[kk] : neutral(o[kk], kk); });
      if (o.neutro && typeof o.neutro === 'object') Object.keys(o.neutro).forEach(function (kk) { r[kk] = neutral(o.neutro[kk], kk); });
      return r;
    }
    return o;
  }
  function argentino(o) {
    if (Array.isArray(o)) return o.map(argentino);
    if (o && typeof o === 'object') { var r = {}; Object.keys(o).forEach(function (k) { if (k !== 'neutro') r[k] = argentino(o[k]); }); return r; }
    return o;
  }

  // ---------- Explicación: bloques del borrador ----------
  function lista(x) { return Array.isArray(x) ? x : []; }
  function txt(b) { return b.texto || ''; }
  function bloque(b) {
    var t = b.tipo, ti = b.titulo ? String(b.titulo).replace(/^\s*(importante|tip|ojo( con esto)?)\s*[:·-]\s*/i, '') : '';
    if (t === 'parrafo') return '<p>' + rico(txt(b)) + '</p>';
    if (t === 'definicion') return '<div class="li2-def"><small>' + esc(ti || 'Definición') + '</small><div>' + rico(txt(b)) + '</div></div>';
    if (t === 'importante' || t === 'tip' || t === 'ojo') {
      var ic = { importante: '✦', tip: '💡', ojo: '⚠️' }[t], rot = { importante: 'Importante', tip: 'Tip', ojo: 'Ojo con esto' }[t];
      return '<div class="li2-nota ' + t + '"><b>' + ic + ' ' + rot + (ti ? ': ' + esc(ti) : '') + '</b><div>' + rico(txt(b)) + '</div></div>';
    }
    if (t === 'lista') return (ti ? '<h4>' + esc(ti) + '</h4>' : '') + '<ul>' + lista(b.items).map(function (x) { return '<li>' + rico(x) + '</li>'; }).join('') + '</ul>' + (txt(b) ? '<p>' + rico(txt(b)) + '</p>' : '');
    if (t === 'pasos') return (ti ? '<h4>' + esc(ti) + '</h4>' : '') + '<ol class="li2-pasos">' + lista(b.items).map(function (x) { return '<li>' + rico(x) + '</li>'; }).join('') + '</ol>';
    if (t === 'ejemplo') return '<div class="li2-ej"><small>Ejemplo' + (ti ? '' : '') + '</small>' + (ti ? '<b>' + rico(ti) + '</b>' : '') + (txt(b) ? '<p>' + rico(txt(b)) + '</p>' : '') +
      (lista(b.items).length ? '<ul>' + lista(b.items).map(function (x) { return '<li>' + rico(x) + '</li>'; }).join('') + '</ul>' : '') + '</div>';
    if (t === 'error') return '<div class="li2-nota error"><b>✘ Error típico' + (ti ? ': ' + esc(ti) : '') + '</b><div>' + rico(txt(b)) + '</div></div>';
    if (t === 'tabla') return (ti ? '<h4>' + esc(ti) + '</h4>' : '') + '<div class="li2-tabla-w"><table class="li2-tabla"><thead><tr>' + lista(b.columnas).map(function (c) { return '<th>' + rico(c) + '</th>'; }).join('') +
      '</tr></thead><tbody>' + lista(b.filas).map(function (f) { return '<tr>' + lista(f).map(function (c) { return '<td>' + rico(c) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
    if (t === 'imagen') return b.png_base64 ? '<figure class="li2-fig"><img src="data:image/png;base64,' + esc(b.png_base64) + '" alt="' + esc(ti || b.descripcion || 'Imagen') + '">' + (ti ? '<figcaption>' + esc(ti) + '</figcaption>' : '') + '</figure>' : '';
    return txt(b) ? '<p>' + rico(txt(b)) + '</p>' : '';
  }

  // ---------- Ejemplos y prácticas desde la plantilla ----------
  function semilla() { return Math.random().toString(36).slice(2, 10); }
  // Devuelve { enunciado, pasos[], respuesta:{valor?, textos?, opciones?, correcta?}, unidad } listo para mostrar
  function instancia(pr, n) {
    if (!pr) return null;
    var vs = lista(pr.variantes);
    if (vs.length) { var v = vs[((n % vs.length) + vs.length) % vs.length]; return armar(v, null, pr.unidad); }
    var seed = typeof n === 'string' ? n : semilla(), vars = null;
    if (pr.vars && C()) { vars = C().instanciar(pr, seed); if (!vars) return null; }
    return armar(pr, vars, pr.unidad);
  }
  function armar(src, vars, unidad) {
    function p(s) { return vars && C() ? C().plantilla(s, vars) : String(s == null ? '' : s); }
    var r = src.respuesta || {}, out = { enunciado: p(src.enunciado), pasos: lista(src.pasos).map(p), unidad: src.unidad || unidad || '', respuesta: {} };
    if (r.formula != null && C()) { try { out.respuesta.valor = C().evaluar(String(r.formula), vars || {}); out.respuesta.tol = +r.tolerancia || 1e-9; out.respuesta.mostrar = C().fmtNum(out.respuesta.valor); } catch (_) { return null; } }
    if (lista(r.acepta).length) { out.respuesta.textos = r.acepta.map(function (x) { return p(x); }); out.respuesta.mostrar = out.respuesta.mostrar || out.respuesta.textos[0]; }
    if (lista(r.opciones).length) { out.respuesta.opciones = r.opciones.map(p); out.respuesta.correcta = p(r.correcta); out.respuesta.mostrar = out.respuesta.correcta; }
    return out;
  }
  function norm(s) { return String(s == null ? '' : s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[\s.¿?¡!]+/g, ' ').trim(); }
  function correcto(inst, a) {
    var r = inst.respuesta;
    if (r.opciones) return a === r.correcta;
    if (r.valor != null && C()) { var x = C().parseNum(a); if (isFinite(x) && Math.abs(x - r.valor) <= Math.max(r.tol, Math.abs(r.valor) * 1e-9)) return true; }
    if (r.textos) return r.textos.some(function (t) { return norm(t) === norm(a); });
    return false;
  }
  function mezclar(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  // ---------- Pantalla ----------
  function abrir(op) {
    var c = op.neutro ? neutral(op.contenido) : argentino(op.contenido);
    var B = window.WaveLeccionBanco, todas = lista(c.secciones), secs;
    if (c.leccion && lista(c.leccion.temas).length) { // armada por la máquina: temas (pueden juntar secciones) con motor del banco de la lección
      secs = c.leccion.temas.map(function (t) {
        var ss = lista(t.secs).map(function (i) { return todas[i]; }).filter(Boolean), pr = null;
        ss.forEach(function (x) { if (!pr && x.practica) pr = x.practica; });
        return { titulo: t.titulo, bloques: lista(t.explicacion).length ? t.explicacion : [].concat.apply([], ss.map(function (x) { return lista(x.bloques); })), practica: pr,
          ejemplo: t.ejemplo && B && B.tiene(t.ejemplo.motor) ? t.ejemplo : null, ejercicio: t.ejercicio && B && B.tiene(t.ejercicio.motor) ? t.ejercicio : null };
      }).filter(function (t) { return t.bloques.length; });
    } else { // borrador con prácticas: lo de concepto se acopla al tema práctico siguiente (o al anterior, si es lo último); cada pantalla tiene su ejemplo
      var vale = todas.filter(function (s) { return s && (lista(s.bloques).length || s.practica); }), pend = [];
      secs = [];
      if (!vale.some(function (s) { return s.practica; })) secs = vale;
      else {
        vale.forEach(function (s) {
          if (!s.practica) { pend = pend.concat(lista(s.bloques)); return; }
          secs.push({ titulo: s.titulo, bloques: pend.concat(lista(s.bloques)), practica: s.practica }); pend = [];
        });
        if (pend.length) secs[secs.length - 1].bloques = secs[secs.length - 1].bloques.concat(pend);
      }
    }
    if (!secs.length) throw new Error('Esta lección todavía no está lista.');
    var hayResumen = lista(c.resumen).length > 0;
    var total = secs.length + (hayResumen ? 1 : 0), cur = 0, ejN = {}, ejPaso = {};
    var el = document.createElement('div'); el.className = 'li2';
    el.innerHTML = '<div class="li2-caja" role="dialog" aria-label="Lección interactiva"><div class="li2-barra"><b class="li2-t">' + esc(op.titulo) + '</b>' +
      '<button type="button" class="li2-x" data-li="cerrar" aria-label="Cerrar">✕</button></div><div class="li2-cuerpo"><nav class="li2-idx" aria-label="Temas de la lección"></nav><main class="li2-main"></main></div></div>';
    document.body.appendChild(el); document.body.classList.add('wvp-abierto');
    var idx = el.querySelector('.li2-idx'), main = el.querySelector('.li2-main');
    function cerrar() { document.body.classList.remove('wvp-abierto'); el.remove(); if (op.alCerrar) op.alCerrar(); }

    function pintarIdx() {
      idx.innerHTML = '<small>Temas</small>' + secs.map(function (s, k) { return '<button type="button" data-ir="' + k + '" class="' + (k === cur ? 'on' : '') + '"><i>' + (k + 1) + '</i><span>' + esc(s.titulo || 'Tema ' + (k + 1)) + '</span></button>'; }).join('') +
        (hayResumen ? '<button type="button" data-ir="' + secs.length + '" class="' + (cur === secs.length ? 'on' : '') + '"><i>★</i><span>Resumen</span></button>' : '');
    }
    function ejemploHtml(k) {
      var s = secs[k], pr = s.practica; if (!pr) return '';
      if (ejN[k] == null) ejN[k] = pr.variantes ? 0 : 'ej' + k;
      var inst = instancia(pr, ejN[k]); if (!inst) return '';
      var vis = ejPaso[k] || 0, todos = vis >= inst.pasos.length;
      return '<section class="li2-ejem" aria-live="polite"><div class="li2-ejem-h"><small>Ejemplo paso a paso</small><button type="button" class="li2-mini" data-li="otro">🔄 Otro ejemplo</button></div>' +
        '<p class="li2-enun">' + rico(inst.enunciado) + '</p><ol class="li2-ejpasos">' + inst.pasos.map(function (p, j) { return '<li class="' + (j < vis ? 'ver' : '') + '">' + (j < vis ? rico(p) : '') + '</li>'; }).join('') + '</ol>' +
        (todos ? (inst.respuesta.mostrar != null ? '<div class="li2-res">Resultado: <b>' + rico(inst.respuesta.mostrar) + (inst.unidad ? ' ' + esc(inst.unidad) : '') + '</b></div>' : '')
          : '<div class="li2-ejpie"><button type="button" class="li2-btn suave" data-li="paso">Siguiente paso ›</button><button type="button" class="li2-link" data-li="todos">Ver todos</button></div>') + '</section>';
    }
    function tema(k) {
      var s = secs[k], primero = k === 0 && c.objetivo;
      return '<div class="li2-kick">Tema ' + (k + 1) + ' de ' + secs.length + '</div><h2>' + esc(s.titulo || 'Tema ' + (k + 1)) + '</h2>' +
        (primero ? '<p class="li2-obj">🎯 ' + rico(c.objetivo) + '</p>' : '') +
        '<div class="li2-cols' + (s.ejemplo || s.practica ? '' : ' una') + '"><div class="li2-exp">' + lista(s.bloques).map(bloque).join('') + '</div>' +
        (s.ejemplo ? '<div class="li2-lado"><section class="li2-ejem"><div class="li2-ejem-h"><small>Ejemplo interactivo</small></div><div class="li2-motor"></div></section></div>'
          : s.practica ? '<div class="li2-lado">' + ejemploHtml(k) + '</div>' : '') + '</div>';
    }
    function resumen() {
      var h = '<div class="li2-kick">Para cerrar</div><h2>Recordá lo más importante</h2><div class="li2-resu">' + lista(c.resumen).map(function (r) {
        return '<div class="li2-rc"><b>' + rico(r.titulo || '') + '</b><span>' + rico(r.texto || (typeof r === 'string' ? r : '')) + '</span></div>'; }).join('') + '</div>';
      return h;
    }
    function pintar() {
      pintarIdx();
      var esRes = cur === secs.length, s = secs[cur];
      main.innerHTML = '<div class="li2-hoja">' + (esRes ? resumen() : tema(cur)) + '</div><div class="li2-nav">' +
        '<button type="button" class="li2-btn suave" data-li="ant"' + (cur ? '' : ' style="visibility:hidden"') + ' aria-label="Anterior">‹<span class="li2-lg"> Anterior</span></button>' +
        (!esRes && (s.ejercicio || s.practica) ? '<button type="button" class="li2-btn prac" data-li="practicar">✏️ Practicá<span class="li2-lg"> este tema</span></button>' : '<span></span>') +
        (cur < total - 1 ? '<button type="button" class="li2-btn" data-li="sig" aria-label="Siguiente"><span class="li2-lg">Siguiente </span>›</button>' : '<button type="button" class="li2-btn" data-li="fin">Terminar la lección ✓</button>') + '</div>';
      main.scrollTop = 0;
      var mt = main.querySelector('.li2-motor'); if (mt && s && s.ejemplo) B.render(mt, s.ejemplo);
    }

    // ---------- Práctica de un tema ----------
    function practicar(k) {
      if (secs[k].ejercicio) { // ejercicio del banco de la lección
        var pe = document.createElement('div'); pe.className = 'li2-pv';
        pe.innerHTML = '<div class="li2-pv-c" role="dialog" aria-label="Ejercicio del tema"><div class="li2-pv-h"><b>✏️ ' + esc(secs[k].titulo || 'Ejercicio') + '</b><span class="li2-cont"></span><button type="button" class="li2-x" data-pv="x" aria-label="Cerrar">✕</button></div><div class="li2-pv-b"></div></div>';
        el.appendChild(pe); var bien = 0, hechos = 0;
        B.render(pe.querySelector('.li2-pv-b'), secs[k].ejercicio, { alResultado: function (ok) { hechos++; if (ok) bien++; pe.querySelector('.li2-cont').textContent = bien + ' de ' + hechos + ' bien'; } });
        pe.addEventListener('click', function (e) { if (e.target === pe || e.target.closest('[data-pv="x"]')) pe.remove(); });
        return;
      }
      var pr = secs[k].practica, vN = pr.variantes ? (ejN[k] || 0) + 1 : null, bien = 0, hechas = 0, inst = null;
      var pv = document.createElement('div'); pv.className = 'li2-pv';
      pv.innerHTML = '<div class="li2-pv-c" role="dialog" aria-label="Práctica del tema"><div class="li2-pv-h"><b>✏️ Practicá: ' + esc(secs[k].titulo || '') + '</b><span class="li2-cont"></span><button type="button" class="li2-x" data-pv="x" aria-label="Cerrar">✕</button></div><div class="li2-pv-b"></div></div>';
      el.appendChild(pv);
      var cuerpo = pv.querySelector('.li2-pv-b');
      function nuevo() {
        for (var t = 0; t < 30 && !inst; t++) inst = instancia(pr, vN != null ? vN++ : semilla());
        if (!inst) { cuerpo.innerHTML = '<p>No pudimos armar el ejercicio.</p>'; return; }
        var r = inst.respuesta;
        cuerpo.innerHTML = '<p class="li2-enun">' + rico(inst.enunciado) + '</p>' +
          (r.opciones ? '<div class="li2-ops">' + mezclar(r.opciones).map(function (o) { return '<button type="button" class="li2-op" data-op="' + esc(o) + '">' + rico(o) + '</button>'; }).join('') + '</div>'
            : '<div class="li2-in"><input type="text" class="li2-inp" autocomplete="off" inputmode="' + (r.valor != null ? 'decimal' : 'text') + '" placeholder="Tu respuesta" aria-label="Tu respuesta">' + (inst.unidad ? '<span>' + esc(inst.unidad) + '</span>' : '') + '</div>') +
          '<div class="li2-fb" aria-live="polite"></div><div class="li2-pv-pie">' + (r.opciones ? '' : '<button type="button" class="li2-btn" data-pv="comp">Comprobar</button>') + '<button type="button" class="li2-btn suave" data-pv="otro">🔄 Otro ejercicio</button></div>';
        var i = cuerpo.querySelector('.li2-inp'); if (i) { i.focus(); i.addEventListener('keydown', function (e) { if (e.key === 'Enter') comprobar(i.value); }); }
        pv.querySelector('.li2-cont').textContent = hechas ? bien + ' de ' + hechas + ' bien' : '';
      }
      function comprobar(a) {
        if (!inst || !String(a).trim()) { cuerpo.querySelector('.li2-fb').innerHTML = '<span class="li2-av">Primero escribí o elegí tu respuesta.</span>'; return; }
        var ok = correcto(inst, String(a).trim()); hechas++; if (ok) bien++; sonar(ok ? 'bien' : 'mal');
        if (ok && window.WaveJuego) try { WaveJuego.confeti(cuerpo); } catch (_) {}
        cuerpo.querySelector('.li2-fb').innerHTML = (ok ? '<div class="li2-ok">✔ ¡Bien! Es correcto.</div>' : '<div class="li2-no">✘ Todavía no. La respuesta es <b>' + rico(inst.respuesta.mostrar) + (inst.unidad ? ' ' + esc(inst.unidad) : '') + '</b>.</div>') +
          (inst.pasos.length ? '<details class="li2-sol"' + (ok ? '' : ' open') + '><summary>Ver cómo se resuelve</summary><ol>' + inst.pasos.map(function (p) { return '<li>' + rico(p) + '</li>'; }).join('') + '</ol></details>' : '');
        [].forEach.call(cuerpo.querySelectorAll('.li2-op'), function (b) { b.disabled = true; var v = b.getAttribute('data-op'); if (v === inst.respuesta.correcta) b.classList.add('ok'); else if (v === a) b.classList.add('no'); });
        var cb = cuerpo.querySelector('[data-pv="comp"]'); if (cb) cb.remove(); var ii = cuerpo.querySelector('.li2-inp'); if (ii) ii.readOnly = true;
        pv.querySelector('.li2-cont').textContent = bien + ' de ' + hechas + ' bien';
      }
      pv.addEventListener('click', function (e) {
        var b = e.target.closest('[data-pv]'), o = e.target.closest('.li2-op');
        if (e.target === pv || (b && b.getAttribute('data-pv') === 'x')) { pv.remove(); return; }
        if (o && !o.disabled) return comprobar(o.getAttribute('data-op'));
        if (!b) return; var a = b.getAttribute('data-pv');
        if (a === 'comp') comprobar(cuerpo.querySelector('.li2-inp').value);
        if (a === 'otro') { inst = null; nuevo(); }
      });
      nuevo();
    }

    el.addEventListener('click', function (e) {
      if (e.target.closest('.li2-pv')) return;
      var ir = e.target.closest('[data-ir]'); if (ir) { cur = +ir.getAttribute('data-ir'); return pintar(); }
      var b = e.target.closest('[data-li]'); if (!b) return;
      var a = b.getAttribute('data-li');
      if (a === 'cerrar') return cerrar();
      if (a === 'ant' && cur > 0) { cur--; return pintar(); }
      if (a === 'sig' && cur < total - 1) { cur++; return pintar(); }
      if (a === 'paso') { ejPaso[cur] = (ejPaso[cur] || 0) + 1; sonar('bien'); return pintar(); }
      if (a === 'todos') { ejPaso[cur] = 99; return pintar(); }
      if (a === 'otro') { var pr = secs[cur].practica; ejN[cur] = pr.variantes ? (ejN[cur] || 0) + 1 : semilla(); ejPaso[cur] = 0; return pintar(); }
      if (a === 'practicar') return practicar(cur);
      if (a === 'fin') { if (op.alTerminar) op.alTerminar(); sonar('fanfarria'); return cerrar(); }
    });
    el.addEventListener('keydown', function (e) { if (e.key === 'Escape') { var pv = el.querySelector('.li2-pv'); if (pv) pv.remove(); else cerrar(); } });
    pintar();
  }

  var css = document.createElement('style');
  css.textContent = [
    '.li2{position:fixed;inset:0;z-index:9000;background:rgba(37,54,56,.55);display:flex;align-items:stretch;justify-content:center;padding:14px}',
    '.li2-caja{display:flex;flex-direction:column;width:100%;max-width:1180px;background:#F3FBF7;border-radius:24px;overflow:hidden;color:#253638}',
    '.li2-barra{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 18px;background:#253638;color:#fff}.li2-t{font-size:1.02rem}',
    '.li2-x{width:38px;height:38px;border:0;border-radius:12px;background:rgba(255,255,255,.12);color:inherit;font-size:1.1rem;cursor:pointer}',
    '.li2-cuerpo{flex:1;min-height:0;display:grid;grid-template-columns:230px 1fr}',
    '.li2-idx{display:flex;flex-direction:column;gap:6px;padding:16px 12px;background:#fff;border-right:2px solid #E3ECEA;overflow-y:auto}.li2-idx small{font-weight:800;color:#4b6a6c;padding:0 8px 4px;text-transform:uppercase;font-size:.72rem;letter-spacing:.06em}',
    '.li2-idx button{display:flex;align-items:center;gap:10px;padding:9px 10px;border:0;border-radius:14px;background:none;font:inherit;font-weight:700;color:#4b6a6c;text-align:left;cursor:pointer}.li2-idx button:hover{background:#F3FBF7}',
    '.li2-idx i{flex:none;display:grid;place-items:center;width:28px;height:28px;border-radius:50%;border:2px solid #9dbdb9;font-style:normal;font-weight:800;font-size:.85rem}.li2-idx button.on{background:#D7F0E9;color:#253638}.li2-idx button.on i{background:#087E83;border-color:#087E83;color:#fff}',
    '.li2-main{display:flex;flex-direction:column;min-height:0;overflow-y:auto}.li2-hoja{flex:1;padding:22px 26px}',
    '.li2-kick{font-weight:800;font-size:.78rem;color:#087E83;text-transform:uppercase;letter-spacing:.06em}.li2-hoja h2{margin:4px 0 14px;font-size:1.5rem;color:#253638}',
    '.li2-obj{margin:-4px 0 14px;padding:10px 14px;border-radius:14px;background:#fff;border:2px solid #D7F0E9;font-weight:700}',
    '.li2-cols{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:20px;align-items:start}.li2-cols.una{grid-template-columns:1fr}',
    '.li2-exp{line-height:1.6}.li2-exp p{margin:0 0 12px}.li2-exp h4{margin:14px 0 6px;color:#066A6E}.li2-exp ul,.li2-exp ol{margin:0 0 12px;padding-left:22px}',
    '.li2-def{margin:0 0 14px;padding:14px 16px;border-radius:16px;background:#253638;color:#fff}.li2-def small{display:block;font-weight:800;color:#7FD3C4;text-transform:uppercase;font-size:.75rem;letter-spacing:.05em;margin-bottom:4px}',
    '.li2-nota{margin:0 0 14px;padding:12px 16px;border-radius:16px;background:#fff;border:2px solid #D7F0E9}.li2-nota>b{display:block;margin-bottom:4px;color:#066A6E}.li2-nota.importante{border-color:#087E83}.li2-nota.ojo,.li2-nota.error{border-color:#253638}.li2-nota.error>b{color:#253638}.li2-nota.ojo>b{color:#253638}',
    '.li2-ej{margin:0 0 14px;padding:12px 16px;border-radius:16px;background:#D7F0E9}.li2-ej small{font-weight:800;color:#066A6E;text-transform:uppercase;font-size:.72rem}.li2-ej b{display:block}.li2-ej ul{margin:6px 0 0}',
    '.li2-tabla-w{overflow-x:auto;margin:0 0 14px}.li2-tabla{border-collapse:collapse;width:100%;background:#fff;border-radius:12px;overflow:hidden}.li2-tabla th{background:#087E83;color:#fff;text-align:left}.li2-tabla th,.li2-tabla td{padding:8px 10px;border:1px solid #E3ECEA}',
    '.li2-fig{margin:0 0 14px;text-align:center}.li2-fig img{max-width:100%;border-radius:14px;background:#fff;border:2px solid #E3ECEA}.li2-fig figcaption{font-size:.85rem;color:#4b6a6c;margin-top:4px}',
    '.li2-lado{position:sticky;top:0}.li2-ejem{padding:16px;border-radius:20px;background:#fff;border:2px solid #087E83}.li2-ejem-h{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:8px}.li2-ejem-h small{font-weight:800;color:#087E83;text-transform:uppercase;font-size:.75rem;letter-spacing:.05em}',
    '.li2-mini{border:2px solid #D7F0E9;background:#F3FBF7;border-radius:99px;padding:5px 12px;font:inherit;font-weight:800;font-size:.82rem;color:#066A6E;cursor:pointer}',
    '.li2-enun{font-weight:800;font-size:1.06rem;margin:0 0 10px;line-height:1.5}.li2-ejpasos{margin:0;padding:0;list-style:none;counter-reset:ej}.li2-ejpasos li{counter-increment:ej;position:relative;min-height:34px;margin:6px 0;padding:7px 10px 7px 40px;border-radius:12px;background:#F3FBF7;border:2px dashed #D7F0E9}',
    '.li2-ejpasos li::before{content:counter(ej);position:absolute;left:8px;top:6px;display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:#9dbdb9;color:#fff;font-weight:800;font-size:.78rem}.li2-ejpasos li.ver{border-style:solid;border-color:#D7F0E9;background:#fff;animation:li2in .3s ease-out}.li2-ejpasos li.ver::before{background:#087E83}',
    '@keyframes li2in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}.ap-sin-anim .li2-ejpasos li.ver{animation:none}',
    '.li2-ejpie{display:flex;align-items:center;gap:12px;margin-top:10px}.li2-link{border:0;background:none;font:inherit;font-weight:700;color:#4b6a6c;text-decoration:underline;cursor:pointer}',
    '.li2-res{margin-top:10px;padding:10px 12px;border-radius:12px;background:#087E83;color:#fff;font-weight:700}',
    '.li2-nav{position:sticky;bottom:0;display:flex;justify-content:space-between;align-items:center;gap:10px;padding:12px 26px;background:#fff;border-top:2px solid #E3ECEA}',
    '.li2-btn{padding:12px 22px;border:0;border-radius:16px;background:#087E83;color:#fff;font:inherit;font-weight:800;cursor:pointer;box-shadow:0 4px 0 #066A6E}.li2-btn:active{transform:translateY(2px);box-shadow:0 2px 0 #066A6E}',
    '.li2-btn.suave{background:#fff;color:#066A6E;border:2px solid #087E83;box-shadow:none}.li2-btn.prac{background:#253638;box-shadow:0 4px 0 #111c1d}',
    '.li2-resu{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:14px}.li2-rc{padding:14px;border-radius:16px;background:#fff;border:2px solid #D7F0E9}.li2-rc b{display:block;color:#087E83;margin-bottom:4px}',
    '.li2-glos{margin-top:8px;padding:12px 16px;border-radius:16px;background:#fff;border:2px solid #E3ECEA}.li2-glos summary{font-weight:800;cursor:pointer}.li2-glos dt{font-weight:800;margin-top:8px}.li2-glos dd{margin:0}',
    '.li2-pv{position:absolute;inset:0;z-index:2;display:grid;place-items:center;padding:16px;background:rgba(37,54,56,.45)}.li2-pv-c{width:100%;max-width:640px;max-height:100%;overflow-y:auto;border-radius:22px;background:#fff}',
    '.li2-pv-h{display:flex;align-items:center;gap:10px;padding:12px 16px;background:#087E83;color:#fff}.li2-pv-h b{flex:1}.li2-cont{font-weight:700;font-size:.85rem}.li2-pv-b{padding:18px}',
    '.li2-in{display:flex;align-items:center;gap:10px}.li2-inp{flex:1;min-width:0;padding:14px 16px;border:2px solid #E3ECEA;border-radius:16px;font:inherit;font-size:1.15rem;font-weight:700}.li2-inp:focus{outline:none;border-color:#087E83;box-shadow:0 0 0 3px #D7F0E9}.li2-in span{font-weight:800;color:#4b6a6c}',
    '.li2-ops{display:grid;gap:8px}.li2-op{padding:12px 14px;border:2px solid #E3ECEA;border-radius:14px;background:#fff;font:inherit;font-weight:700;text-align:left;cursor:pointer}.li2-op:hover{border-color:#9dbdb9}.li2-op.ok{border-color:#087E83;background:#D7F0E9}.li2-op.no{border-color:#253638;background:#E3ECEA}',
    '.li2-fb{margin-top:12px}.li2-ok,.li2-no{padding:10px 12px;border-radius:12px;font-weight:700}.li2-ok{background:#D7F0E9;color:#253638}.li2-no{background:#E3ECEA;color:#253638}.li2-av{color:#4b6a6c;font-weight:700}',
    '.li2-sol{margin-top:10px}.li2-sol summary{font-weight:800;color:#066A6E;cursor:pointer}.li2-sol ol{margin:8px 0 0;padding-left:22px;line-height:1.6}.li2-pv-pie{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}',
    '@media (max-width:820px){.li2{padding:0}.li2-caja{border-radius:0}.li2-cuerpo{grid-template-columns:1fr;grid-template-rows:auto 1fr}.li2-idx{flex-direction:row;overflow-x:auto;border-right:0;border-bottom:2px solid #E3ECEA;padding:8px}.li2-idx small{display:none}.li2-idx button{flex:none}.li2-idx button span{max-width:150px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.li2-cols{grid-template-columns:1fr}.li2-lado{position:static}.li2-hoja{padding:16px}.li2-nav{padding:10px 12px}.li2-btn{padding:11px 16px;font-size:.95rem;white-space:nowrap}.li2-lg{display:none}}'
  ].join('');
  document.head.appendChild(css);
  return { abrir: abrir, instancia: instancia, correcto: correcto };
})();
