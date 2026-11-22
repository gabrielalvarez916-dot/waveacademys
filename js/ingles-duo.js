// Actividades de Inglés al estilo "app de idiomas". Se activan con marcas dentro del enunciado de la pregunta (la corrección no cambia):
//   [[audio:Where is the library?]]    · botones 🔊 Escuchar y 🐢 Despacio (voz del navegador en inglés). Sirve en cualquier tipo de pregunta
//                                        (escribí lo que escuchás = short_answer; escuchá y elegí = multiple_choice).
//   [[hablar:Where is the library?]]   · lo anterior + 🎤 Hablar: el navegador escucha al alumno y escribe lo que entendió en el campo de texto
//                                        (usar con short_answer). Si el navegador no puede, el alumno escribe la frase.
//   [[memorama]]                       · en una pregunta "matching": se juega con tarjetas que se dan vuelta. Pareja k de izquierda = k de derecha.
// Además: si todas las opciones de una pregunta son emojis, se muestran como fichas grandes ("elegí la imagen").
// No conoce las respuestas correctas: eso lo sigue corrigiendo el servidor.
(function () {
  'use strict';
  var RE = /\[\[(audio|hablar|memorama)(?::([\s\S]*?))?\]\]/;
  var EMO = /^[←-⯿\uD83C-􏰀-\uDFFF️‍\s]+$/;

  // ---------- Voz y micrófono ----------
  function vozIngles() {
    try {
      var vs = window.speechSynthesis.getVoices() || [], i;
      for (i = 0; i < vs.length; i++) if (/^en[-_]US/i.test(vs[i].lang)) return vs[i];
      for (i = 0; i < vs.length; i++) if (/^en/i.test(vs[i].lang)) return vs[i];
    } catch (e) {}
    return null;
  }
  function decir(texto, lento) {
    if (!window.speechSynthesis || !window.SpeechSynthesisUtterance) return false;
    try {
      window.speechSynthesis.cancel();
      var u = new SpeechSynthesisUtterance(texto), v = vozIngles();
      u.lang = v ? v.lang : 'en-US'; if (v) u.voice = v;
      u.rate = lento ? 0.6 : 0.92;
      window.speechSynthesis.speak(u);
      return true;
    } catch (e) { return false; }
  }
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;

  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
  function boton(txt, accion, texto) {
    var b = el('button', 'dd-b', txt); b.type = 'button'; b.setAttribute('data-dd', accion); b._t = texto; return b;
  }

  // ---------- Cambio de marcas por botones ----------
  function procesarTexto(nodo) {
    var m = RE.exec(nodo.nodeValue); if (!m) return;
    var antes = nodo.nodeValue.slice(0, m.index), desp = nodo.nodeValue.slice(m.index + m[0].length), padre = nodo.parentNode;
    if (!padre) return;
    var tipo = m[1], texto = (m[2] || '').trim();
    var marco = document.createDocumentFragment();
    if (antes) marco.appendChild(document.createTextNode(antes));
    var cont = el('span', 'dd-ing');
    if (tipo === 'audio' || tipo === 'hablar') {
      cont.appendChild(boton('🔊 Escuchar', 'oir', texto));
      cont.appendChild(boton('🐢 Despacio', 'oirlento', texto));
      if (tipo === 'hablar') { cont.appendChild(boton('🎤 Hablar', 'mic', texto)); cont.appendChild(el('small', 'dd-est')); }
      marco.appendChild(cont);
    } else if (tipo === 'memorama') {
      cont.setAttribute('data-memo', '1');
    }
    if (desp) marco.appendChild(document.createTextNode(desp));
    padre.replaceChild(marco, nodo);
    if (tipo === 'memorama') armarMemorama(padre);
  }

  function recorrer(raiz) {
    if (!raiz || raiz.nodeType === 8) return;
    var nodos = [];
    var w = document.createTreeWalker(raiz, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (n.nodeValue.indexOf('[[') < 0) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode && n.parentNode.nodeName;
        return /^(SCRIPT|STYLE|TEXTAREA|INPUT|OPTION)$/.test(p) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    while (w.nextNode()) nodos.push(w.currentNode);
    nodos.forEach(procesarTexto);
    // opciones que son todas emojis → fichas grandes
    var base = raiz.nodeType === 1 ? raiz : document;
    Array.prototype.forEach.call(base.querySelectorAll ? base.querySelectorAll('.mt-preg-c') : [], function (c) {
      if (c.getAttribute('data-dd-fichas')) return;
      var ops = c.querySelectorAll('.mt-op > span');
      if (ops.length < 2) return;
      var todos = Array.prototype.every.call(ops, function (s) { return EMO.test(s.textContent.trim()) && s.textContent.trim().length <= 12; });
      c.setAttribute('data-dd-fichas', '1');
      if (todos) c.classList.add('dd-fichas');
    });
  }

  // ---------- Memorama ----------
  function mezclar(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function armarMemorama(contexto) {
    var preg = contexto.closest ? contexto.closest('.mt-preg-c') : null;
    if (!preg || preg.querySelector('.dd-memo')) return;
    var pares = preg.querySelector('.mt-pares'); if (!pares) return;
    var filas = pares.querySelectorAll('.mt-par'), izq = [];
    Array.prototype.forEach.call(filas, function (f) { izq.push(f.querySelector('span').textContent); });
    // las opciones de cada lista están en el orden original (la pareja k de izquierda es la k de derecha)
    var ops0 = filas[0] && filas[0].querySelector('select') ? Array.prototype.slice.call(filas[0].querySelectorAll('option')).slice(1).map(function (o) { return o.value; }) : [];
    if (ops0.length !== izq.length) return;
    var cartas = [];
    izq.forEach(function (t, k) { cartas.push({ k: k, lado: 'i', t: t }); cartas.push({ k: k, lado: 'd', t: ops0[k] }); });
    mezclar(cartas);
    var juego = el('div', 'dd-memo');
    juego.appendChild(el('small', 'mt-ayuda', 'Dá vuelta dos tarjetas: si son pareja, quedan a la vista.'));
    var grilla = el('div', 'dd-grilla'), est = el('small', 'dd-est', 'Intentos: 0');
    var abiertas = [], hechas = 0, intentos = 0, bloqueo = false;
    cartas.forEach(function (c) {
      var b = el('button', 'dd-carta'); b.type = 'button'; b._c = c;
      var f = el('span', 'dd-frente', '❓'), r = el('span', 'dd-reverso', c.t);
      b.appendChild(f); b.appendChild(r); grilla.appendChild(b);
    });
    grilla.addEventListener('click', function (ev) {
      var b = ev.target.closest('.dd-carta'); if (!b || bloqueo || b.classList.contains('abierta') || b.classList.contains('lista')) return;
      b.classList.add('abierta'); abiertas.push(b);
      if (/^[A-Za-z]/.test(b._c.t) && b._c.lado === 'i') decir(b._c.t, false);
      if (abiertas.length < 2) return;
      intentos++; est.textContent = 'Intentos: ' + intentos;
      var a = abiertas[0], z = abiertas[1];
      if (a._c.k === z._c.k && a._c.lado !== z._c.lado) {
        a.classList.add('lista'); z.classList.add('lista'); abiertas = []; hechas++;
        var fila = pares.querySelectorAll('.mt-par')[a._c.k], sel = fila && fila.querySelector('select');
        if (sel) { sel.value = (a._c.lado === 'd' ? a : z)._c.t; sel.dispatchEvent(new Event('change', { bubbles: true })); }
        if (hechas === izq.length) est.textContent = '¡Completo! Intentos: ' + intentos;
      } else {
        bloqueo = true;
        setTimeout(function () { a.classList.remove('abierta'); z.classList.remove('abierta'); abiertas = []; bloqueo = false; }, 900);
      }
    });
    juego.appendChild(grilla); juego.appendChild(est);
    pares.style.display = 'none';
    pares.parentNode.insertBefore(juego, pares);
  }

  // ---------- Clicks ----------
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest && ev.target.closest('[data-dd]'); if (!b) return;
    var acc = b.getAttribute('data-dd'), texto = b._t || '';
    var est = b.parentNode && b.parentNode.querySelector('.dd-est');
    if (acc === 'oir' || acc === 'oirlento') {
      if (!decir(texto, acc === 'oirlento') && est) est.textContent = 'Este navegador no puede reproducir la voz.';
      return;
    }
    if (acc === 'mic') {
      if (!SR) { if (est) est.textContent = 'Este navegador no escucha la voz: escribí la frase.'; return; }
      var preg = b.closest('.mt-preg-c'), campo = preg && preg.querySelector('input.mt-txt, textarea.mt-txt');
      var r = new SR(); r.lang = 'en-US'; r.interimResults = false; r.maxAlternatives = 1;
      b.classList.add('grabando'); if (est) est.textContent = 'Escuchando…';
      r.onresult = function (e) {
        var t = e.results[0][0].transcript;
        if (campo) { campo.value = t; campo.dispatchEvent(new Event('input', { bubbles: true })); }
        if (est) est.textContent = 'Escuchamos: «' + t + '»';
      };
      r.onerror = function (e) {
        if (est) est.textContent = (e.error === 'not-allowed' || e.error === 'service-not-allowed') ? 'Falta permitir el micrófono en el navegador. Mientras tanto, escribí la frase.' : (e.error === 'no-speech' ? 'No te escuchamos. Probá de nuevo.' : 'No pudimos escuchar. Escribí la frase.');
      };
      r.onend = function () { b.classList.remove('grabando'); };
      try { r.start(); } catch (e2) { b.classList.remove('grabando'); if (est) est.textContent = 'No pudimos activar el micrófono. Escribí la frase.'; }
    }
  });

  // ---------- Estilos ----------
  var css = '.dd-ing{display:inline-flex;flex-wrap:wrap;gap:8px;align-items:center;margin:6px 0}' +
    '.dd-b{border:2px solid #2E8B57;background:#fff;color:#1d6b42;border-radius:12px;padding:8px 14px;font:inherit;font-weight:800;cursor:pointer}' +
    '.dd-b:hover{background:#eaf7ef}.dd-b.grabando{background:#ffe3e3;border-color:#d9534f;color:#a02622}' +
    '.dd-est{display:block;width:100%;color:#555}' +
    '.dd-grilla{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:10px;margin:10px 0}' +
    '.dd-carta{position:relative;min-height:72px;border:2px solid #7C5CE0;border-radius:14px;background:#f3eefe;font:inherit;font-weight:800;cursor:pointer;padding:6px}' +
    '.dd-carta .dd-reverso{display:none}.dd-carta.abierta .dd-frente,.dd-carta.lista .dd-frente{display:none}' +
    '.dd-carta.abierta .dd-reverso,.dd-carta.lista .dd-reverso{display:block}' +
    '.dd-carta.abierta{background:#fff7d6;border-color:#e0a800}.dd-carta.lista{background:#e3f6e8;border-color:#2E8B57}' +
    '.dd-fichas .mt-op{display:inline-flex;margin:6px}.dd-fichas .mt-op span{font-size:2.6rem;line-height:1;padding:10px 16px}' +
    '.dd-fichas .mt-op input{margin-right:6px}';
  var st = document.createElement('style'); st.textContent = css; (document.head || document.documentElement).appendChild(st);

  // ---------- Observador ----------
  var pendiente = false;
  function programar() { if (pendiente) return; pendiente = true; (window.requestAnimationFrame || setTimeout)(function () { pendiente = false; try { recorrer(document.body); } catch (e) {} }); }
  function iniciar() {
    if (window.speechSynthesis && window.speechSynthesis.getVoices) { try { window.speechSynthesis.getVoices(); } catch (e) {} }
    new MutationObserver(programar).observe(document.body, { childList: true, subtree: true, characterData: true });
    programar();
  }
  if (document.body) iniciar(); else document.addEventListener('DOMContentLoaded', iniciar);
  window.WaveIngles = { decir: decir, recorrer: recorrer };
})();
