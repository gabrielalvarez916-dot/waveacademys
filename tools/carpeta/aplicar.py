# -*- coding: utf-8 -*-
"""Aplica reescrituras de carpeta: NUEVAS[(mision, nivel, i)] = consigna nueva (las respuestas no cambian salvo RESP)."""
import json, os, sys, importlib
mod, base = sys.argv[1], sys.argv[2]          # p. ej.: medio_mat1 contenido/medio/matematica-1
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
m = importlib.import_module(mod); NUEVAS = m.NUEVAS; RESP = getattr(m, 'RESP', {})
tocadas = {}
for (k, n, i), txt in list(NUEVAS.items()) + [((k, n, i), None) for (k, n, i) in RESP if (k, n, i) not in NUEVAS]:
    f = f'{base}/mision-{k}/mision-{k}.json'
    M = tocadas.get(f) or json.load(open(f, encoding='utf-8')); tocadas[f] = M
    N = M['niveles'][n]
    if txt is not None:
        c = N['carpeta'][i]
        if isinstance(c, dict): c['consigna'] = txt
        else: N['carpeta'][i] = txt
    if (k, n, i) in RESP: N['respuestas_carpeta'][i] = RESP[(k, n, i)]
for f, M in tocadas.items(): json.dump(M, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(NUEVAS), 'consignas reescritas en', len(tocadas), 'misiones')
