# -*- coding: utf-8 -*-
"""Separa las misiones cambiadas: imprime las que cambiaron en algo MÁS que la práctica de la lección interactiva
(esas pasan por el control de calidad de siempre y la carga completa). Si en una misión ya cargada solo se agregaron
o cambiaron prácticas o la lección interactiva, no se la vuelve a revisar con las reglas generales: solo se validan y cargan las prácticas.
Uso: python tools/interactiva/solo_practicas.py <commit_base> archivo [...]"""
import json, subprocess, sys
def sin(o):
    if isinstance(o, dict): return {k: sin(v) for k, v in o.items() if k not in ('practica', 'leccion')}
    if isinstance(o, list): return [sin(x) for x in o]
    return o
base, out = sys.argv[1], []
for f in sys.argv[2:]:
    try: antes = json.loads(subprocess.run(['git', 'show', f'{base}:{f}'], capture_output=True, text=True, check=True).stdout)
    except Exception: out.append(f); continue  # misión nueva
    if sin(antes) != sin(json.load(open(f, encoding='utf-8'))): out.append(f)
print(' '.join(out))
