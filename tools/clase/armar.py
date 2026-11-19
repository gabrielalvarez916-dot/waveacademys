# -*- coding: utf-8 -*-
"""Arma el HTML final de cada clase: motor + plantillas + lección (lecciones/<slug>.json) + audio (voz/<slug>.json).
Salidas: actividades/clases/<slug>.html y tools/clase/dist/<slug>.html (la que se carga en la plataforma).
Uso: python tools/clase/armar.py [slug ...]   (sin argumentos arma todas)"""
import glob, json, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
M = os.path.join(AQUI, 'motor')
GSAP = '<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.1/dist/gsap.min.js"></script>'
ORDEN = ['base.js', 't-narrativa.js', 't-procesos.js', 't-mate.js', 't-ciencias-lengua.js', 'reproductor.js']
MOTOR = '\n'.join(open(os.path.join(M, f), encoding='utf-8').read() for f in ORDEN[:-1])
REPRO = open(os.path.join(M, ORDEN[-1]), encoding='utf-8').read()
SHELL = open(os.path.join(M, 'shell.html'), encoding='utf-8').read()
MAPAS = json.load(open(os.path.join(M, 'mapas.json'), encoding='utf-8'))
J = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
esc = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

pedidas = sys.argv[1:]
for path in sorted(glob.glob(os.path.join(AQUI, 'lecciones', '*.json'))) + (sorted(glob.glob(os.path.join(AQUI, 'pruebas', '*.json'))) if pedidas else []):
    L = json.load(open(path, encoding='utf-8'))
    slug = L.get('slug') or os.path.basename(path)[:-5]
    if pedidas and slug not in pedidas:
        continue
    voz = os.path.join(AQUI, 'voz', slug + '.json')
    audio = [[{'a': f['a'], 'w': f['w']} for f in e] for e in json.load(open(voz))] if os.path.exists(voz) else None
    zonas = sorted({e.get('zona', 'mundo') for e in L['escenas'] if e.get('t') == 'mapa'})
    datos = '<script>window.CLASE=' + J(L) + ';' + ('window.MAPAS=' + J({z: MAPAS[z] for z in zonas}) + ';' if zonas else '') + ('window.VOZ_AUDIO=' + J(audio) + ';' if audio else '') + '</script>'
    html = SHELL.replace('{{TITULO}}', esc(L['titulo'])).replace('{{SUB}}', esc(L.get('sub', ''))).replace('{{SCRIPTS}}', GSAP + '\n' + datos + '\n<script>\n' + MOTOR + '\n' + REPRO + '\n</script>')
    for out in (os.path.join(RAIZ, 'actividades', 'clases', slug + '.html'), os.path.join(AQUI, 'dist', slug + '.html')):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w', encoding='utf-8').write(html)
    print(slug, 'armada', 'con audio' if audio else 'SIN audio', round(len(html) / 1024), 'KB')
