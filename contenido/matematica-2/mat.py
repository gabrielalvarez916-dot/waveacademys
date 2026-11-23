# -*- coding: utf-8 -*-
"""Matemática II (Avanzado, Año 2): constructores. Reusa los de Inglés I (ing.py) y agrega los de Matemática."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "ingles-1"))
from ing import *
AQUI = os.path.dirname(os.path.abspath(__file__))
SID = "0b36ea19-5877-4077-a8bd-c62313d37658"
RAIZ = os.path.join(AQUI, "..", "..", "tools", "clase", "lecciones")
FR = lambda num, den, forma, txt, v: {"t":"fraccion","num":num,"den":den,"forma":forma,"txt":txt,"voz":v}
RCT = lambda mn, mx, paso, marcas, v: {"t":"recta","min":mn,"max":mx,"paso":paso,"marcas":[{"v":a,"txt":b} for a,b in marcas],"voz":v}
EQ = lambda pasos, notas, v: {"t":"ecuacion","pasos":pasos,"notas":notas,"voz":v}
SAL = lambda t, mn, mx, cada, ini, sal, v: {"t":"saltos","titulo":t,"min":mn,"max":mx,"cada":cada,"inicio":ini,"saltos":[{"a":a,"txt":b} for a,b in sal],"voz":v}
UNI = lambda t, pares, v: {"t":"unir","titulo":t,"pares":[list(p) for p in pares],"mezclar":False,"voz":v}
PIZ = lambda lineas, v, t=None: {"t":"pizarra","lineas":[{"txt":a,**({"color":b} if b else {}),**({"marca":c} if c else {})} for a,b,c in lineas],"voz":v,**({"titulo":t} if t else {})}
QZ = lambda p, o, c, v: {"t":"quiz4","pregunta":p,"opciones":o,"correcta":c,"voz":v}
PAT = lambda t, it, falta, regla, v: {"t":"patron","titulo":t,"items":it,"falta":falta,"regla":regla,"voz":v}
BAL = lambda iz, de, gana, v: {"t":"balanza","izq":{"cab":iz[0],"items":iz[1]},"der":{"cab":de[0],"items":de[1]},"gana":gana,"voz":v}
PRED = lambda p, a, b, c, r, v: {"t":"prediccion","pregunta":p,"a":{"txt":a[0],"emoji":a[1]},"b":{"txt":b[0],"emoji":b[1]},"correcta":c,"resultado":r,"voz":v}
def escribir(n, M, STEPS, TIT, CLS):
    d = os.path.join(AQUI, f"mision-{n}"); os.makedirs(d, exist_ok=True)
    json.dump(M, open(os.path.join(d, f"mision-{n}.json"), "w"), ensure_ascii=False)
    for k, es in CLS.items():
        json.dump({"slug":f"mat2-m{n}-n{k}","step_id":STEPS[k],"materia":"Matemática II","titulo":TIT[k],"sub":f"Matemática II · Misión {n} · Nivel {k}","escenas":es},open(os.path.join(RAIZ,f"mat2-m{n}-n{k}.json"),"w"),ensure_ascii=False)
    print("ok misión", n)
