# -*- coding: utf-8 -*-
"""Arma preguntas-juego para actividades (se corrigen igual que tipos que ya existen, sin IA):
  crucigrama([(respuesta, pista), ...], consigna)  -> fill_blank con [[crucigrama:...]] (cada palabra es un hueco)
  sopa([palabras], consigna)                       -> multi_select con [[sopa]] (todas las opciones son palabras a encontrar)
  escape(pregunta)                                 -> marca la actividad como escape room (un candado por pregunta)
Uso en los .py de contenido:  sys.path.insert(0, 'tools'); from juegos_actividad import crucigrama, sopa, escape"""
import unicodedata

def _n(s):
    s = unicodedata.normalize('NFD', str(s).upper()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn' or c == '̃')
    return unicodedata.normalize('NFC', s).replace(' ', '')

def _layout(pals):
    """ubica las palabras cruzándolas por letras en común. Devuelve [(fila, col, dir, largo)] en el mismo orden."""
    G = {}; pos = [None] * len(pals)
    def puede(w, f, c, d):
        for j, ch in enumerate(w):
            ff, cc = (f, c + j) if d == 'h' else (f + j, c)
            if (ff, cc) in G and G[(ff, cc)] != ch: return False
            if (ff, cc) not in G:  # que no quede pegada de costado a otra palabra
                vec = [(ff - 1, cc), (ff + 1, cc)] if d == 'h' else [(ff, cc - 1), (ff, cc + 1)]
                if any(v in G for v in vec): return False
        a = (f, c - 1) if d == 'h' else (f - 1, c); b = (f, c + len(w)) if d == 'h' else (f + len(w), c)
        return a not in G and b not in G
    def poner(w, f, c, d):
        for j, ch in enumerate(w): G[(f, c + j) if d == 'h' else (f + j, c)] = ch
    orden = sorted(range(len(pals)), key=lambda i: -len(pals[i]))
    for n, i in enumerate(orden):
        w = pals[i]
        if n == 0: poner(w, 0, 0, 'h'); pos[i] = (0, 0, 'h'); continue
        hecho = False
        for k in orden[:n]:
            if pos[k] is None: continue
            f0, c0, d0 = pos[k]; wk = pals[k]
            for a, ch in enumerate(wk):
                for b, ch2 in enumerate(w):
                    if ch != ch2: continue
                    d = 'v' if d0 == 'h' else 'h'
                    f, c = (f0 - b, c0 + a) if d == 'v' else (f0 + a, c0 - b)
                    if puede(w, f, c, d): poner(w, f, c, d); pos[i] = (f, c, d); hecho = True; break
                if hecho: break
            if hecho: break
        if not hecho:  # sin cruce: abajo de todo
            f = max(ff for ff, _ in G) + 2; c = min(cc for _, cc in G); poner(w, f, c, 'h'); pos[i] = (f, c, 'h')
    fm = min(p[0] for p in pos); cm = min(p[1] for p in pos)
    return [(p[0] - fm, p[1] - cm, p[2], len(pals[i])) for i, p in enumerate(pos)]

def crucigrama(pares, consigna='Completá el crucigrama.', e='', n='aplicar'):
    pals = [_n(r) for r, _ in pares]
    lay = _layout(pals)
    spec = ';'.join(f'{f},{c},{d},{l}' for f, c, d, l in lay)
    pistas = ' '.join(f'{i + 1}) {p} ___' for i, (_, p) in enumerate(pares))
    return {"t": "fill_blank", "p": f"[[crucigrama:{spec}]] {consigna} {pistas}", "o": [], "r": {"huecos": [[r, _n(r).lower()] for r, _ in pares]}, "e": e, "n": n}

def sopa(palabras, consigna='Encontrá las palabras en la sopa de letras.', e='', n='recordar'):
    return {"t": "multi_select", "p": f"[[sopa]] {consigna}", "o": list(palabras), "r": {"correctas": list(palabras)}, "e": e, "n": n}

def escape(q):
    q = dict(q); q['p'] = '[[escape]] ' + q['p']; return q
