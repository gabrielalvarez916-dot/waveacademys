# -*- coding: utf-8 -*-
"""Borrador para ElevenLabs (solo Lengua, nivel medio): reescribe SOLO el texto que se manda a la voz, nunca lo que ve el alumno.
Regla de Gaby: todo lo que se alarga se escribe con la letra repetida 4 veces (ssss, mmmm, aaaa, oooo, iiii).
  1) sss / mmm / fff / lll / nnn / rrr / zzz / vvv  ->  4 letras
  2) vocal suelta seguida de «…» o «:»  (a… , o: , i:)  ->  4 letras ( aaaa… , oooo: , iiii: )"""
import re
RUN = re.compile(r'(?<![A-Za-zÁÉÍÓÚáéíóúñÑ])([sSmMfFlLnNrRzZvV])\1{2,}(?![A-Za-zÁÉÍÓÚáéíóúñÑ])')
VOC = re.compile(r'(?<![A-Za-zÁÉÍÓÚáéíóúñÑ])([aeiouAEIOU])(?=\s?(?:…|\.\.\.|:))')

def para_eleven(t):
    t = RUN.sub(lambda m: m.group(1) * 4, t)
    return VOC.sub(lambda m: m.group(1) * 4, t)

def lleva_alargado(t):
    return para_eleven(t) != t

if __name__ == '__main__':
    import glob, json, sys
    n = 0
    for p in sorted(glob.glob('tools/medio/clase/lecciones/medio-leng*.json')):
        for i, e in enumerate(json.load(open(p)).get('escenas', [])):
            for j, v in enumerate(e.get('voz', [])):
                v2 = re.sub(r'\*', '', v)
                if lleva_alargado(v2):
                    n += 1; print(f"{os.path.basename(p) if (os:=__import__('os')) else ''}[{i}][{j}]  {v2}  ->  {para_eleven(v2)}")
    print(n, 'frases', file=sys.stderr)
