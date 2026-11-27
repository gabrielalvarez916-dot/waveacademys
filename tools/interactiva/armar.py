# -*- coding: utf-8 -*-
"""Ayuda para ESCRIBIR EN SESIÓN la lección interactiva y las actividades de una misión.
No inventa contenido: solo da atajos para armar los bloques y, ANTES de guardar, corre los dos
controles reales (validar.js y control_calidad.py) sobre una copia. Si hay errores, los muestra
todos juntos y NO guarda: se corrige una vez y se vuelve a correr.

Uso desde un script de sesión:
    import sys; sys.path.insert(0, 'tools/interactiva'); from armar import *
    L = {'1': {'temas': [T(...), ...], 'recuerda': [R(...), ...]}, ...}
    guardar('contenido/matematica-1/mision-20/mision-20.json', L, acts={'1': [...]})
"""
import json, os, re, subprocess, sys, tempfile

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
Pp = lambda x: {"tipo": "parrafo", "texto": x}
Li = lambda *i: {"tipo": "lista", "items": list(i)}
m = lambda motor, **p: {"motor": motor, "p": p}
T = lambda ti, ej, ejer, d, pa, li: {"titulo": ti, "ejemplo": ej, "ejercicio": ejer, "explicacion": [D(*d), Pp(pa), Li(*li)]}
R = lambda c, d, e, **k: dict(concepto=c, definicion=d, ejemplo=e, **k)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _etiquetar(M):
    """Pone la etiqueta n que falte (actividades, examen y carpeta) con un criterio simple.
    El control después avisa si alguna quedó mal puesta."""
    for l in (M.get('act') or {}).values():
        for q in l:
            if 'n' not in q:
                q['n'] = 'recordar' if q['t'] == 'true_false' else ('error' if 'error' in q['p'].lower() else 'aplicar')
    for lv, q in M.get('examen') or []:
        p = q['p'].lower()
        q.setdefault('n', 'error' if ('error' in p or 'compañer' in p) else ('recordar' if q['t'] == 'true_false' else 'aplicar'))
    for N in (M.get('niveles') or {}).values():
        if N.get('carpeta') and not N.get('carpeta_nivel'):
            N['carpeta_nivel'] = ['error' if 'compañer' in (c if isinstance(c, str) else c.get('consigna', '')).lower() else 'aplicar' for c in N['carpeta']]


def controlar(ruta, M):
    """Corre los dos controles sobre una copia (en la misma carpeta, para que encuentren las clases). Devuelve la lista de problemas."""
    d = os.path.dirname(os.path.abspath(ruta))
    fd, tmp = tempfile.mkstemp(suffix='.json', dir=d)
    with os.fdopen(fd, 'w', encoding='utf-8') as f: json.dump(M, f, ensure_ascii=False, indent=1)
    try:
        v = subprocess.run(['node', os.path.join(RAIZ, 'tools/interactiva/validar.js'), tmp], capture_output=True, text=True).stdout
        # control_calidad decide si una misión es "existente" por su ruta: se lo corre sobre la ruta real con la copia en su lugar
        orig = open(ruta, encoding='utf-8').read() if os.path.exists(ruta) else None
        os.replace(tmp, ruta)
        try:
            c = subprocess.run([sys.executable, os.path.join(RAIZ, 'tools/control_calidad.py'), ruta], capture_output=True, text=True, cwd=RAIZ).stdout
        finally:
            if orig is None: os.remove(ruta)
            else: open(ruta, 'w', encoding='utf-8').write(orig)
    finally:
        if os.path.exists(tmp): os.remove(tmp)
    probs = [l.strip() for l in v.splitlines() if '✘' in l]
    probs += [l.strip() for l in c.splitlines() if l.strip().startswith('- ')]
    # Si un control se cae (falta un archivo, error de Python), no hay veredicto: eso NUNCA cuenta como aprobado
    if '✓' not in c and not probs: probs.append('control_calidad no dio veredicto (¿se cayó?): ' + (c.strip()[-200:] or 'sin salida'))
    if 'lección interactiva OK' not in v and not any('✘' in l for l in v.splitlines()): probs.append('validar.js no dio veredicto (¿se cayó?)')
    return probs


def guardar(ruta, L=None, acts=None, ajustes=None):
    """L: lecciones por nivel. acts: actividades a AGREGAR por nivel. ajustes(M): función opcional para cambios a mano.
    Guarda solo si pasan los dos controles; si no, imprime todos los problemas juntos y devuelve False."""
    M = json.load(open(ruta, encoding='utf-8'))
    for n, lec in (L or {}).items():
        M['niveles'].setdefault(n, {})['leccion'] = lec
    for n, v in (acts or {}).items():
        M['act'].setdefault(n, []).extend(v)
    if ajustes: ajustes(M)
    M['actualizar_preguntas'] = True
    _etiquetar(M)
    probs = controlar(ruta, M)
    if probs:
        print('✗ NO se guardó %s · %d problema(s):' % (ruta, len(probs)))
        for p in probs: print('   ', p)
        return False
    json.dump(M, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('✓ guardado %s (pasa los dos controles)' % ruta)
    return True
