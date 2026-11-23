# -*- coding: utf-8 -*-
"""Arma el HTML final de cada clase: motor + plantillas + lección (lecciones/<slug>.json) + audio (voz/<slug>.json).
Salidas: actividades/clases/<slug>.html y tools/clase/dist/<slug>.html (la que se carga en la plataforma).
Uso: python tools/clase/armar.py [slug ...]   (sin argumentos arma todas)"""
import variar, glob, json, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
M = os.path.join(AQUI, 'motor')
GSAP = '<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.1/dist/gsap.min.js"></script>'
ORDEN = ['base.js', 't-narrativa.js', 't-procesos.js', 't-tecnologia.js', 't-ingles.js', 't-mate.js', 't-ciencias-lengua.js', 't-mundo.js', 't-plataformas.js', 't-extras.js', 'musica.js', 'reproductor.js']
MOTOR = '\n'.join(open(os.path.join(M, f), encoding='utf-8').read() for f in ORDEN[:-1])
REPRO = open(os.path.join(M, ORDEN[-1]), encoding='utf-8').read()
SHELL = open(os.path.join(M, 'shell.html'), encoding='utf-8').read()
MAPAS = json.load(open(os.path.join(M, 'mapas.json'), encoding='utf-8'))
J = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
esc = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# Estilo por materia: se reemplazan los colores del motor (fondo, tarjetas, acento). Matemática usa los originales.
TEMAS = {
    'naturales': {'#050f10': '#081208', '#17585a': '#2e6a35', '#0c292b': '#12301a', '#1d474a': '#25492b', '#132f31': '#17331d',
                  '#a7efe2': '#c9f2a6', '#5fc2b2': '#7dc95d', '#7FD3C4': '#9BE07A', '#9be8da': '#c3f0a0', '#3e9488': '#4f8f37',
                  '#06282a': '#14300c', '#d8fff7': '#efffdc', '#2c5a5e': '#3c6a3a', '#9dbdb9': '#b2c9a8', '#eaf7f4': '#f3fbe9', 'rgba(5,15,16': 'rgba(8,20,8'},
    'lengua': {'#050f10': '#0e0a1a', '#17585a': '#4a3480', '#0c292b': '#1d1433', '#1d474a': '#3a2a63', '#132f31': '#241a40',
               '#a7efe2': '#e0d2ff', '#5fc2b2': '#a98bff', '#7FD3C4': '#C3A8FF', '#9be8da': '#d6c4ff', '#3e9488': '#7458c4',
               '#06282a': '#1a1030', '#d8fff7': '#f1eaff', '#2c5a5e': '#4b3c74', '#9dbdb9': '#bdb2d6', '#eaf7f4': '#f5f1fc', '#14300c': '#241a40', 'rgba(5,15,16': 'rgba(14,10,26'},
}
TEMAS['sociales'] = {'#050f10': '#140c08', '#17585a': '#8a4a2a', '#0c292b': '#2a160c', '#1d474a': '#5a3220', '#132f31': '#3a2014',
                     '#a7efe2': '#ffd9b8', '#5fc2b2': '#e8955a', '#7FD3C4': '#F2A65A', '#9be8da': '#ffcf9f', '#3e9488': '#b8622f',
                     '#06282a': '#2a140a', '#d8fff7': '#fff1e4', '#2c5a5e': '#6a4030', '#9dbdb9': '#d6bba8', '#eaf7f4': '#fdf4ec', '#14300c': '#3a2014', 'rgba(5,15,16': 'rgba(20,12,8'}
def tema_de(materia):
    m = (materia or '').lower()
    if 'natural' in m or 'biolog' in m: return TEMAS['naturales']
    if 'lengua' in m or 'literatura' in m: return TEMAS['lengua']
    if 'social' in m or 'historia' in m or 'geograf' in m: return TEMAS['sociales']
    return None

sys.path.insert(0, os.path.dirname(AQUI))
from neutro import convertir, argentino

SOLO_CAMBIADAS = '--cambiadas' in sys.argv
def armar(L, slug, suf, outs):
    voz = os.path.join(AQUI, 'voz', slug + suf + '.json')
    audio = [[{'a': f['a'], 'w': f['w']} for f in e] for e in json.load(open(voz))] if os.path.exists(voz) else None
    zonas = sorted({e.get('zona', 'mundo') for e in L['escenas'] if e.get('t') == 'mapa'})
    datos = '<script>window.CLASE=' + J(L) + ';' + ('window.MAPAS=' + J({z: MAPAS[z] for z in zonas}) + ';' if zonas else '') + ('window.VOZ_AUDIO=' + J(audio) + ';' if audio else '') + '</script>'
    if SOLO_CAMBIADAS and os.path.exists(outs[-1]):  # --cambiadas: si el HTML ya tiene esta misma lección y esta misma voz, no se rearma (un cambio de motor no re-sube todo)
        dt = datos
        for a, b in (tema_de(L.get('materia')) or {}).items(): dt = dt.replace(a, b).replace(a.lower(), b)
        if dt in open(outs[-1], encoding='utf-8').read(): return
    html = SHELL.replace('{{TITULO}}', esc(L['titulo'])).replace('{{SUB}}', esc(L.get('sub', ''))).replace('{{SCRIPTS}}', GSAP + '\n' + datos + '\n<script>\n' + MOTOR + '\n' + REPRO + '\n</script>')
    for a, b in (tema_de(L.get('materia')) or {}).items():
        html = html.replace(a, b).replace(a.lower(), b)
    for out in outs:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w', encoding='utf-8').write(html)
    print(slug + suf, 'armada', 'con audio' if audio else 'SIN audio', round(len(html) / 1024), 'KB')

SOLO_CAMBIADAS = '--cambiadas' in sys.argv
pedidas = [a for a in sys.argv[1:] if a != '--cambiadas']
for path in sorted(glob.glob(os.path.join(AQUI, 'lecciones', '*.json'))) + (sorted(glob.glob(os.path.join(AQUI, 'pruebas', '*.json'))) if pedidas else []):
    crudo = json.load(open(path, encoding='utf-8'))
    slug = crudo.get('slug') or os.path.basename(path)[:-5]
    if pedidas and slug not in pedidas:
        continue
    L = argentino(crudo); variar.preparar(L)
    N = convertir(crudo); variar.preparar(N)  # versión en español neutro (alumnos de otros países), con sus partes "neutro"
    armar(L, slug, '', (os.path.join(RAIZ, 'actividades', 'clases', slug + '.html'), os.path.join(AQUI, 'dist', slug + '.html')))
    armar(N, slug, '.neutro', (os.path.join(AQUI, 'dist', slug + '.neutro.html'),))
