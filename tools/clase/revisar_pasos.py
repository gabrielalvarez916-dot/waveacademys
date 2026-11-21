# -*- coding: utf-8 -*-
"""Controla que cada escena tenga exactamente las frases de voz que su plantilla necesita (si no, la imagen y la voz se desfasan:
por ejemplo un círculo de 6 colores con frases para 4). Uso: python tools/clase/revisar_pasos.py [slug ...]  (sin argumentos: todas)"""
import json, glob, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
N = {'gancho': lambda d: 3, 'historia': lambda d: len(d['lineas']) + 1, 'chat': lambda d: len(d['mensajes']) + 1, 'noticia': lambda d: 3, 'reto': lambda d: 3,
     'portada': lambda d: 1, 'definicion': lambda d: 2, 'dato': lambda d: 2, 'frase': lambda d: 1, 'consejo': lambda d: 1, 'errores': lambda d: 1 + len(d['items']),
     'pregunta': lambda d: 3, 'resumen': lambda d: 2 + len(d['items']), 'comparar': lambda d: 4 if d.get('def') else 3, 'antesdespues': lambda d: 2,
     'clasificar': lambda d: 1 + len(d['cajas']), 'tabla': lambda d: 1 + len(d['filas']), 'venn': lambda d: 4, 'balanza': lambda d: 3, 'matriz': lambda d: 1 + len(d['celdas']),
     'pasos': lambda d: 1 + len(d['items']), 'ciclo': lambda d: 1 + len(d['items']), 'flujo': lambda d: len(d['items']), 'causas': lambda d: 1 + len(d['items']),
     'linea': lambda d: len(d['eventos']), 'barras': lambda d: 1 + len(d['items']), 'torta': lambda d: 1 + len(d['items']), 'zoom': lambda d: len(d['niveles']),
     'bloques': lambda d: 1 + len(d['items']), 'dialogo': lambda d: len(d['lineas']), 'vocab': lambda d: len(d['items']), 'texto': lambda d: 1 + len(d['marcas']),
     'partes': lambda d: 1 + len(d['partes']), 'orden': lambda d: 3, 'corrige': lambda d: 1 + len(d['cambios']), 'silabas': lambda d: 3}
def revisar(slug):
    p = os.path.join(AQUI, 'lecciones', slug + '.json'); out = []
    for k, e in enumerate(json.load(open(p, encoding='utf-8'))['escenas']):
        f = N.get(e.get('t'))
        if not f: continue
        try: n = f(e)
        except Exception: continue
        if len(e.get('voz') or []) != n: out.append(f'{slug}: escena {k} «{e["t"]}» necesita {n} frases de voz y tiene {len(e.get("voz") or [])}')
    return out
if __name__ == '__main__':
    slugs = sys.argv[1:] or [os.path.basename(f)[:-5] for f in sorted(glob.glob(os.path.join(AQUI, 'lecciones', '*.json')))]
    err = [x for s in slugs for x in revisar(s)]
    for x in err: print(x)
    print('pasos:', 'OK' if not err else f'{len(err)} escena(s) desfasada(s)'); sys.exit(1 if err else 0)
