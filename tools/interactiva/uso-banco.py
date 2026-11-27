# -*- coding: utf-8 -*-
"""REPORTE DE VARIEDAD: qué herramientas del banco de la lección se usan en cada materia y cuáles todavía no se usaron nunca.
Uso: python3 tools/interactiva/uso-banco.py            (todas las misiones de contenido/)
     python3 tools/interactiva/uso-banco.py lengua-1   (solo las carpetas que contengan ese texto)
Antes de elegir el ejemplo y la práctica de una pantalla, mirá la lista «sin usar» del área: si alguna corresponde al tema, va primero."""
import json, re, sys, glob, pathlib, collections
RAIZ = pathlib.Path(__file__).resolve().parents[2]
filtro = sys.argv[1:] 
banco = collections.OrderedDict()
for f in sorted(RAIZ.glob('js/leccion-banco*.js')):
    banco[f.name] = sorted(set(m for m in re.findall(r"\bM\.([a-z0-9_]+)\s*=\s*\{\s*tipo", f.read_text(encoding='utf-8'))))
usos = collections.defaultdict(collections.Counter)
for f in sorted(glob.glob(str(RAIZ / 'contenido/**/mision-*.json'), recursive=True)):
    mat = re.sub(r'^.*contenido/', '', f).split('/mision-')[0]
    if filtro and not any(x in mat for x in filtro): continue
    try: M = json.load(open(f, encoding='utf-8'))
    except Exception: continue
    for n, nv in (M.get('niveles') or {}).items():
        for t in ((nv or {}).get('leccion') or {}).get('temas') or []:
            for k in ('ejemplo', 'ejercicio'):
                if isinstance(t.get(k), dict) and t[k].get('motor'): usos[mat][t[k]['motor']] += 1
total = collections.Counter()
for mat, c in sorted(usos.items()):
    total.update(c); s = sum(c.values())
    print(f'\n== {mat}: {s} usos, {len(c)} herramientas distintas')
    for m, n in c.most_common(): print(f'   {n:4d}  {m}' + ('   ⚠ demasiado repetida' if n > max(4, s / 8) else ''))
print('\n== SIN USAR NUNCA (por archivo del banco)')
for f, ms in banco.items():
    libres = [m for m in ms if not total[m]]
    print(f'  {f}: {len(libres)} de {len(ms)} sin usar')
    print('     ' + ', '.join(libres))
