# -*- coding: utf-8 -*-
"""Rearma los moldes repetidos de las clases de una materia: cambia escenas básicas por plantillas del banco
sin tocar el contenido (tabla -> matriz/bloques, clasificar -> bloques, dos definiciones seguidas -> comparar).
Respeta la regla de variedad (al menos 2 plantillas no básicas por clase, ninguna en más de 3 de las 4 clases de la misión).
Uso: python tools/clase/variar_escenas.py ciud1-m1 ciud1-m2 ...   (prefijo de la misión)"""
import json, os, sys, collections
AQUI = os.path.dirname(os.path.abspath(__file__)); LEC = os.path.join(AQUI, 'lecciones')
BAS = {'pregunta', 'resumen', 'errores', 'definicion', 'reto', 'noticia', 'gancho', 'historia', 'chat', 'portada', 'tabla', 'clasificar', 'pasos', 'consejo', 'frase'}
LIM = {'tabla': 3, 'clasificar': 3, 'pasos': 3}

def candidatos(es):
    """lista de (indice, nuevo_tipo, escena_nueva) que se pueden aplicar sin cambiar la cantidad de frases de voz"""
    out = []
    for k, e in enumerate(es):
        t = e.get('t'); v = e.get('voz') or []
        if t == 'tabla' and len(e['columnas']) == 2:
            f = e['filas']
            if len(f) == 4 and len(v) == 5: out.append((k, 'matriz', {'t': 'matriz', 'titulo': e['titulo'], 'celdas': [{'cab': str(a).upper(), 'txt': b} for a, b in f], 'voz': v}))
            if 2 <= len(f) <= 5 and len(v) == len(f) + 1: out.append((k, 'bloques', {'t': 'bloques', 'titulo': e['titulo'], 'items': [{'cab': str(a).upper(), 'txt': b} for a, b in f], 'voz': v}))
        if t == 'clasificar' and 2 <= len(e['cajas']) <= 4 and len(v) == len(e['cajas']) + 1:
            its = [{'cab': c['cab'], 'txt': ', '.join(f['txt'] for f in e['fichas'] if e['cajas'][f['caja']]['cab'] == c['cab'])} for c in e['cajas']]
            if all(i['txt'] for i in its): out.append((k, 'bloques', {'t': 'bloques', 'titulo': 'CÓMO SE CLASIFICA', 'items': its, 'voz': v}))
        if t == 'pasos' and 2 <= len(e['items']) <= 6 and len(v) == len(e['items']) + 1:
            out.append((k, 'linea', {'t': 'linea', 'titulo': e['titulo'], 'eventos': [{'fecha': str(i + 1), 'txt': x['txt'] if isinstance(x, dict) else x, 'emoji': (x.get('emoji') if isinstance(x, dict) else None) or '🔹'} for i, x in enumerate(e['items'])], 'voz': v}))
        if t == 'clasificar' and len(e['cajas']) == 2 and len(v) == 3:
            its = [', '.join(f['txt'] for f in e['fichas'] if f['caja'] == i) for i in (0, 1)]
            if all(its): out.append((k, 'antesdespues', {'t': 'antesdespues', 'antes': {'cab': e['cajas'][0]['cab'], 'emoji': e['cajas'][0].get('emoji', '🔷'), 'texto': its[0]}, 'despues': {'cab': e['cajas'][1]['cab'], 'emoji': e['cajas'][1].get('emoji', '🔶'), 'texto': its[1]}, 'voz': v}))
        if t == 'definicion' and k + 1 < len(es) and es[k + 1].get('t') == 'definicion':
            a, b = e, es[k + 1]; va, vb = a.get('voz') or [], b.get('voz') or []
            if len(va) == 2 and len(vb) == 2:
                out.append((k, 'comparar', {'t': 'comparar', 'a': {'cab': a['palabra'].upper(), 'texto': a['texto'], 'emoji': a.get('emoji', '🔷')}, 'b': {'cab': b['palabra'].upper(), 'texto': b['texto'], 'emoji': b.get('emoji', '🔶')}, 'signo': 'vs', 'voz': ['Dos ideas que se relacionan.', va[0], vb[0]], '_borra': k + 1}))
    return out

def main(pref):
    clases = {}
    for n in range(1, 5):
        p = os.path.join(LEC, f'{pref}-n{n}.json')
        if os.path.exists(p): clases[n] = json.load(open(p, encoding='utf-8'))
    uso = collections.defaultdict(set)   # plantilla -> clases de la misión que la usan
    for n, L in clases.items():
        for e in L['escenas']: uso[e['t']].add(n)
    for n, L in clases.items():
        es = L['escenas']
        for _ in range(4):
            esp = [e for e in es if e['t'] not in BAS]
            sobra = [t for t in LIM if len(uso[t]) > LIM[t] and any(e['t'] == t for e in es)]
            if len(esp) >= 2 and not sobra: break
            cand = [c for c in candidatos(es) if len(uso[c[1]] - {n}) < 3 and (c[1] not in LIM)]
            if not cand: break
            # primero las que sacan plantillas que sobran
            cand.sort(key=lambda c: 0 if es[c[0]]['t'] in sobra else 1)
            k, t, nuevo = cand[0]; viejo = es[k]['t']
            borra = nuevo.pop('_borra', None)
            es[k] = nuevo
            if borra is not None: es.pop(borra)
            uso[t].add(n)
            if not any(e['t'] == viejo for e in es): uso[viejo].discard(n)
        json.dump(L, open(os.path.join(LEC, f'{pref}-n{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{pref}-n{n}:', [e['t'] for e in es])

if __name__ == '__main__':
    for p in sys.argv[1:]: main(p)
