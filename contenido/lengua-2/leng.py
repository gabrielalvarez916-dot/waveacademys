# -*- coding: utf-8 -*-
"""Lengua y Literatura II (Avanzado, Año 2): constructores. Reusa los de Inglés I (ing.py) y agrega escenas de Lengua."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "ingles-1"))
from ing import *
AQUI = os.path.dirname(os.path.abspath(__file__))
SID = "a29bde14-2609-4d6f-b3c6-2562ea53f6bc"
RAIZ = os.path.join(AQUI, "..", "..", "tools", "clase", "lecciones")
CJ = lambda t, x, e, v: {"t": "consejo", "titulo": t, "texto": x, "emoji": e, "voz": v}
TX = lambda o, m, v: {"t": "texto", "oracion": o, "marcas": [{"desde": a, "hasta": b, "etiqueta": c, "color": d} for a, b, c, d in m], "voz": v}
COR = lambda t, cs, v: {"t": "corrige", "titulo": t, "cambios": [{"antes": a, "despues": b, "motivo": c} for a, b, c in cs], "voz": v}
VOF = lambda a, em, ok, ex, v: {"t": "vof", "afirmacion": a, "emoji": em, "verdadero": ok, "explicacion": ex, "voz": v}
def escribir(n, M, STEPS, TIT, CLS):
    d = os.path.join(AQUI, f"mision-{n}"); os.makedirs(d, exist_ok=True)
    json.dump(M, open(os.path.join(d, f"mision-{n}.json"), "w"), ensure_ascii=False)
    for k, es in CLS.items():
        json.dump({"slug": f"leng2-m{n}-n{k}", "step_id": STEPS[k], "materia": "Lengua y Literatura II", "titulo": TIT[k], "sub": f"Lengua y Literatura II · Misión {n} · Nivel {k}", "escenas": es}, open(os.path.join(RAIZ, f"leng2-m{n}-n{k}.json"), "w"), ensure_ascii=False)
    print("ok misión", n)
