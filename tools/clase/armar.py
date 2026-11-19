# -*- coding: utf-8 -*-
"""Arma el HTML final de cada clase: el código + su audio (tools/clase/voz/<leccion>.json) en un solo archivo.
Salidas: actividades/clases/<leccion>.html y tools/clase/dist/<leccion>.html (la que se carga en la plataforma)."""
import glob, json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
GSAP = '<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.1/dist/gsap.min.js"></script>'

for src in sorted(glob.glob(os.path.join(AQUI, '*.src.html'))):
    nombre = os.path.basename(src).replace('.src.html', '')
    if nombre.startswith('demo-'):
        continue
    voz = os.path.join(AQUI, 'voz', nombre + '.json')
    audio = json.load(open(voz)) if os.path.exists(voz) else None
    s = open(src, encoding='utf-8').read().replace('<script>/*GSAP*/</script>', GSAP)
    if audio:
        audio = [[{'a': f['a'], 'w': f['w']} for f in esc] for esc in audio]
        s = s.replace('<script>\n(function () {', '<script>window.VOZ_AUDIO=' + json.dumps(audio, separators=(',', ':')) + ';</script>\n<script>\n(function () {', 1)
    for out in (os.path.join(RAIZ, 'actividades', 'clases', nombre + '.html'), os.path.join(AQUI, 'dist', nombre + '.html')):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w', encoding='utf-8').write(s)
    print(nombre, 'armada', 'con audio' if audio else 'SIN audio', round(len(s) / 1024), 'KB')
