# -*- coding: utf-8 -*-
"""Borrador para ElevenLabs (solo Lengua, nivel medio): reescribe SOLO el texto que se manda a la voz, nunca lo que ve el alumno.
Regla de Gaby: todo lo que se alarga se escribe con cada letra repetida 4 veces.
  sss, mmm, fff, lll...      -> ssss, mmmm, ffff, llll
  vocal suelta (a, o, i...)  -> aaaa, oooo, iiii
  palabra con guiones (To-mi, te-re) -> letra por letra: tttt oooo mmmm iiii
  sílaba antes de «…» o «:»  -> letra por letra:  to… -> tttt oooo…   ma… -> mmmm aaaa…   va: -> vvvv aaaa:
Solo actúa en frases de sonidos (las que tienen sss/mmm/… o puntos suspensivos). «la A» / «la E» (nombre de la letra) no se toca."""
import re
L = r'A-Za-zÁÉÍÓÚáéíóúñÑüÜ'
SOLO = lambda p: rf'(?<![{L}]){p}(?![{L}])'
RUN = re.compile(SOLO(r'([sSmMfFlLnNrRzZvV])\1{2,}'))
SIL = re.compile(rf'(?<![{L}])([bcdfgjklmnñpqrstvxyz])([aeiou])(?=\s?(?:…|\.\.\.|:))')
VOC = re.compile(rf'(?<![{L}])(?<!la )(?<!la\s)([aeiouAEIOU])(?![{L}])(?=\s?(?:…|\.\.\.|:|,|\.|\?|$))')

def es_de_sonidos(t):
    return bool(RUN.search(t)) or t.count('…') >= 2 or ('…' in t and re.search(rf'(?<![{L}])[aeiou](?![{L}])', t))

GUION = re.compile(rf'(?<![{L}])([{L}]+(?:-[{L}]+)+)(?![{L}])')

def silabeado(m):  # To-mi -> tttt oooo mmmm iiii   (como lo escribe Gaby)
    return ' '.join(c * 4 for c in m.group(1).replace('-', '') if c.isalpha()).lower()

# Un hueco (letra que falta) no se dice «hueco»: es un silencio.
HUECO = re.compile(r'(?<=[,:]\s)huecos?(?=\s?[,.?!])', re.I)

def para_eleven(t):
    t = HUECO.sub('… …', t)
    t = GUION.sub(silabeado, t)
    if not es_de_sonidos(t): return t
    t = RUN.sub(lambda m: m.group(1) * 4, t)
    t = SIL.sub(lambda m: m.group(1) * 4 + ' ' + m.group(2) * 4, t)
    return VOC.sub(lambda m: m.group(1) * 4, t)

if __name__ == '__main__':
    import glob, json, os, sys
    n = 0
    for p in sorted(glob.glob('tools/medio/clase/lecciones/medio-leng*.json')):
        for i, e in enumerate(json.load(open(p)).get('escenas', [])):
            for j, v in enumerate(e.get('voz', [])):
                v2 = v.replace('*', ''); w = para_eleven(v2)
                if w != v2: n += 1; print(f"{os.path.basename(p).replace('medio-leng1-','')}[{i}][{j}]  {v2}  ->  {w}")
    print(n, 'frases', file=sys.stderr)
