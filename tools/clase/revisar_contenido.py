# Control de contenido: reglas que Gabriel fue marcando. Uso: python3 tools/clase/revisar_contenido.py slug1 slug2 ... [--mision contenido/.../mision-N.json]
import json, sys, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
MESES = r'\b(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)\b'
PROD = r'^(escribo mi|escribo un|corrijo mi)\b'  # solo producción escrita de Lengua
src = open(os.path.join(AQUI, 'voz_edge.py'), encoding='utf-8').read()
PRON = set(re.findall(r"'([^']+)':", src[src.index('PRONUNCIA'):src.index('def pronuncia')]))
EXTR = re.compile(r"\b[A-Z][a-zA-Z]*(?:w|W|sh|th|ck|y\b)[a-zA-Z]*\b")
args = sys.argv[1:]; mis = None
if '--mision' in args: i = args.index('--mision'); mis = json.load(open(args[i + 1], encoding='utf-8')); args = args[:i] + args[i + 2:]
err = []
def E(s, m): err.append(f'{s}: {m}')
def textos(x):
    if isinstance(x, str): yield x
    elif isinstance(x, dict):
        for v in x.values(): yield from textos(v)
    elif isinstance(x, list):
        for v in x: yield from textos(v)
for slug in args:
    L = json.load(open(os.path.join(AQUI, 'lecciones', slug + '.json'), encoding='utf-8'))
    tit = (L.get('titulo') or '').lower()
    todo = ' '.join(textos(L['escenas']))
    if re.search(MESES, todo, re.I) and 'Julio Verne' not in todo: E(slug, 'nombra meses: los alumnos entran en cualquier fecha')
    for k, e in enumerate(L['escenas']):
        t = e['t']
        if t == 'mundo' and (e.get('fondo', 'nada') != 'nada' or any(('zoom' in a or 'mueve' in a) for p in e['pasos'] for a in p['acc'])) and 'subject_id' not in L:
            E(slug, f'escena {k}: mundo con fondo/zoom/movimiento (formato simple: fondo "nada")')
        if t == 'clasificar':
            for f in e['fichas']:
                if len(f['txt']) > 19: E(slug, f'escena {k}: ficha larga (>19): «{f["txt"]}»')
        if t == 'pregunta' and len(e['opciones']) < 3 and set(e['opciones']) != {'Sí', 'No'} and 'I' in (L.get('materia') or ''): E(slug, f'escena {k}: pregunta con menos de 3 opciones (secundaria)')
        if t == 'dato' and re.fullmatch(r'1[0-9]{3}|20[0-9]{2}', str(e.get('numero', ''))): E(slug, f'escena {k}: un año en "dato" sale con punto de miles; usar frase')
        for v in e.get('voz', []):
            for w in EXTR.findall(v.replace('*', '')):
                if w not in PRON and not any(w in p for p in PRON) and w.lower() not in ('hay', 'muy', 'hoy', 'voy', 'soy', 'estoy', 'ley', 'rey', 'yo', 'ya', 'yerba', 'uruguay', 'paraguay'):
                    E(slug, f'escena {k}: nombre extranjero sin pronunciación cargada: «{w}» (agregar a PRONUNCIA en voz_edge.py)')
    if re.search(r'lengua|literatura', (L.get('materia') or ''), re.I) and re.match(PROD, tit) and not any(e.get('titulo') == 'TU TURNO' for e in L['escenas']):  # y en la misión: actividad de escritura (keywords/IA)
        E(slug, 'nivel de producción sin escena "TU TURNO" que diga la tarea concreta')
if mis:
    for n, c in mis['niveles'].items():
        s = f'mision {mis["tema"]} nivel {n}'
        if re.search(MESES, ' '.join(textos(c)), re.I) and 'Julio Verne' not in ' '.join(textos(c)): E(s, 'el PDF nombra meses')
        if 'en tu carpeta' in (c.get('ejemplo_solo') or {}).get('planteo', '') and any(q.get('t') == 'keywords' for q in mis['act'].get(n, [])): E(s, 'la producción se manda "a la carpeta": tiene que ir a la actividad del nivel')
    for n, acts in mis['act'].items():
        for q in acts:
            if q.get('t') == 'keywords' and isinstance(q.get('r'), dict): E(f'mision {mis["tema"]} act {n}', 'escritura con palabras clave: tiene que corregirla la IA (r como texto de referencia)')
for e in err: print(e)
print('contenido:', 'OK' if not err else f'{len(err)} problema(s)'); sys.exit(1 if err else 0)
