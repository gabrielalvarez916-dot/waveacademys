/* MÚSICA DE FONDO: se compone en el momento con WebAudio (sin archivos). Cada clase tiene la suya:
   la semilla sale del título, y de ahí salen tonalidad, acordes, tempo, instrumento y ritmo.
   Va bajita y baja más mientras habla la voz (MUSICA.hablando lo dice el reproductor). */
var MUSICA = (function () {
  var semilla = 0, s = (window.CLASE && (CLASE.slug || CLASE.titulo)) || 'wave';
  for (var i = 0; i < s.length; i++) semilla = (semilla * 31 + s.charCodeAt(i)) >>> 0;
  function rnd() { semilla = (semilla * 1664525 + 1013904223) >>> 0; return semilla / 4294967296; }
  function elegir(a) { return a[Math.floor(rnd() * a.length)]; }

  var ACORDES = { I: [0, 4, 7, 11], ii: [2, 5, 9, 12], iii: [4, 7, 11, 14], IV: [5, 9, 12, 16], V: [7, 11, 14, 17], vi: [9, 12, 16, 19] };
  var PROG = [['I', 'V', 'vi', 'IV'], ['vi', 'IV', 'I', 'V'], ['I', 'vi', 'IV', 'V'], ['ii', 'V', 'I', 'vi'], ['I', 'iii', 'IV', 'V'], ['IV', 'I', 'V', 'vi'], ['I', 'IV', 'vi', 'V']];
  var est = {
    raiz: 45 + Math.floor(rnd() * 9), prog: elegir(PROG), bpm: 72 + Math.floor(rnd() * 22),
    pad: elegir(['sine', 'triangle', 'sawtooth']), arpa: elegir(['triangle', 'sine', 'square']),
    patron: elegir([[0, 1, 2, 1, 3, 2, 1, 2], [0, 2, 1, 3, 2, 1, 3, 2], [3, 2, 1, 0, 1, 2, 3, 2], [0, 1, 2, 3, 2, 1, 0, null]]),
    bateria: rnd() < .75, hats: rnd() < .6
  };
  if (/natural|biolog/i.test((window.CLASE && CLASE.materia) || '')) { est.bpm = 62 + Math.floor(rnd() * 14); est.pad = 'sine'; est.arpa = elegir(['sine', 'triangle']); est.bateria = false; est.hats = false; est.raiz += 5; } // Naturales: más calma, sin batería

  var ctx = null, maestro = null, sonando = false, silencio = false, prox = 0, paso = 0, timer = null, VOL = .12, VOL_VOZ = .045;
  function hz(m) { return 440 * Math.pow(2, (m - 69) / 12); }
  function nota(t, m, dur, tipo, vol, corte) {
    var o = ctx.createOscillator(), g = ctx.createGain(), f = ctx.createBiquadFilter();
    o.type = tipo; o.frequency.value = hz(m); f.type = 'lowpass'; f.frequency.value = corte || 1800;
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + Math.min(.4, dur * .25)); g.gain.exponentialRampToValueAtTime(.0001, t + dur);
    o.connect(f); f.connect(g); g.connect(maestro); o.start(t); o.stop(t + dur + .05);
  }
  function bombo(t) { var o = ctx.createOscillator(), g = ctx.createGain(); o.frequency.setValueAtTime(110, t); o.frequency.exponentialRampToValueAtTime(40, t + .18);
    g.gain.setValueAtTime(.5, t); g.gain.exponentialRampToValueAtTime(.001, t + .25); o.connect(g); g.connect(maestro); o.start(t); o.stop(t + .3); }
  var ruido = null;
  function hat(t, v) { if (!ruido) { ruido = ctx.createBuffer(1, ctx.sampleRate * .1, ctx.sampleRate); var d = ruido.getChannelData(0); for (var k = 0; k < d.length; k++) d[k] = Math.random() * 2 - 1; }
    var n = ctx.createBufferSource(), f = ctx.createBiquadFilter(), g = ctx.createGain(); n.buffer = ruido; f.type = 'highpass'; f.frequency.value = 7000;
    g.gain.setValueAtTime(v, t); g.gain.exponentialRampToValueAtTime(.001, t + .05); n.connect(f); f.connect(g); g.connect(maestro); n.start(t); n.stop(t + .06); }

  function programar() { // cada paso es una corchea; 8 corcheas por compás, un acorde cada 2 compases
    var c = 60 / est.bpm / 2;
    while (prox < ctx.currentTime + .3) {
      var ac = ACORDES[est.prog[Math.floor(paso / 16) % est.prog.length]], k = paso % 16, r = est.raiz;
      if (k === 0) { ac.forEach(function (x) { nota(prox, r + 12 + x, c * 16, est.pad, .05, est.pad === 'sawtooth' ? 900 : 1400); }); }
      if (k % 4 === 0) nota(prox, r + ac[0] - 12 + 12, c * 3.5, 'sine', .16, 400);
      var p = est.patron[k % 8]; if (p != null && k % 1 === 0) nota(prox, r + 24 + ac[p], c * 1.6, est.arpa, est.arpa === 'square' ? .018 : .04, 2400);
      if (est.bateria && k % 8 === 0) bombo(prox);
      if (est.bateria && k % 8 === 4) bombo(prox);
      if (est.hats && k % 2 === 1) hat(prox, .05);
      prox += c; paso++;
    }
  }
  function volumen() { if (!maestro) return; var obj = silencio || !sonando ? 0 : (M.hablando && M.hablando() ? VOL_VOZ : VOL); maestro.gain.setTargetAtTime(obj, ctx.currentTime, .25); }

  var M = {
    hablando: null,
    iniciar: function () {
      try { if (!ctx) { var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return; ctx = new AC(); maestro = ctx.createGain(); maestro.gain.value = 0; maestro.connect(ctx.destination); setInterval(volumen, 200); }
        if (ctx.state === 'suspended') ctx.resume(); } catch (_) { return; }
      M.seguir();
    },
    seguir: function () { if (!ctx || sonando) return; sonando = true; if (ctx.state === 'suspended') ctx.resume(); prox = ctx.currentTime + .1; timer = setInterval(programar, 100); volumen(); },
    pausa: function () { if (!ctx) return; sonando = false; clearInterval(timer); volumen(); },
    alternar: function () { silencio = !silencio; volumen(); return !silencio; }
  };
  return M;
})();
