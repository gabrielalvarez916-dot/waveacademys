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
    todo = re.sub(r'(Revolución|Plaza|Avenida) de Mayo|\d+ de (diciembre|junio|marzo|septiembre)', '', ' '.join(textos(L['escenas'])))
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
from revisar_pasos import revisar as _rp
for _s in args:
    if os.path.exists(os.path.join(AQUI, 'lecciones', _s + '.json')): err.extend(_rp(_s))
# VARIEDAD DE RECURSOS (regla general, todos los años y niveles): las 4 clases de una misión no pueden ser el mismo molde
_BASICAS = {'pregunta', 'resumen', 'errores', 'definicion', 'reto', 'noticia', 'gancho', 'historia', 'chat', 'portada', 'tabla', 'clasificar', 'pasos', 'consejo', 'frase'}
_secs = {}
for _s in args:
    _lp = os.path.join(AQUI, 'lecciones', _s + '.json')
    if os.path.exists(_lp):
        _secs[_s] = [e.get('t') for e in json.load(open(_lp, encoding='utf-8'))['escenas']]
for _s, _ts in _secs.items():
    if len([t for t in _ts if t not in _BASICAS]) < 2: E(_s, 'poca variedad de recursos: usar al menos 2 plantillas del banco fuera de las básicas (comparar, antesdespues, causas, ciclo, flujo, linea, venn, balanza, matriz, partes, dato, dialogo, bloques, zoom, etc.)')
_grupos = {}
for _s, _ts in _secs.items(): _grupos.setdefault(re.sub(r'-n\d+(\.neutro)?$', '', _s), []).append((_s, _ts))
for _g, _l in _grupos.items():
    if len(_l) < 3: continue
    _cont = {}
    for _s, _ts in _l:
        for t in set(_ts):
            if t not in ('pregunta', 'resumen', 'errores', 'definicion'): _cont.setdefault(t, []).append(_s)
    for t, ss in _cont.items():
        if len(ss) > 3 and t not in ('reto', 'noticia', 'gancho', 'historia', 'chat', 'texto'): E(_g, f'plantilla «{t}» repetida en {len(ss)} clases de la misión (máximo 3 de 4): variar los recursos')
    if len({tuple(ts) for _, ts in _l}) < len(_l): E(_g, 'dos clases tienen exactamente la misma secuencia de escenas')
if mis:
    for n, c in mis['niveles'].items():
        s = f'mision {mis["tema"]} nivel {n}'
        tx = re.sub(r'(Revolución|Plaza|Avenida) de Mayo|\d+ de (diciembre|junio|marzo|septiembre)|Julio Verne', '', ' '.join(textos(c)))
        if re.search(MESES, tx, re.I): E(s, 'el PDF nombra meses')
        if 'en tu carpeta' in (c.get('ejemplo_solo') or {}).get('planteo', '') and any(q.get('t') == 'keywords' for q in mis['act'].get(n, [])): E(s, 'la producción se manda "a la carpeta": tiene que ir a la actividad del nivel')
    for n, acts in mis['act'].items():
        for q in acts:
            if q.get('t') == 'keywords' and isinstance(q.get('r'), dict): E(f'mision {mis["tema"]} act {n}', 'escritura con palabras clave: tiene que corregirla la IA (r como texto de referencia)')
# versión neutra: toda palabra que parezca voseo tiene que estar en el diccionario de tools/neutro.py
sys.path.insert(0, os.path.dirname(os.path.dirname(AQUI)) + '/tools')
from neutro import revisar as _rev_neutro, tiene_neutro
# etiqueta de cada misión (común / variante / alternativa): la parte para alumnos de otros países no se puede olvidar
_VER = json.load(open(os.path.join(os.path.dirname(AQUI), 'versiones.json'), encoding='utf-8'))['materias']
def _version(materia, n):
    return (_VER.get(materia) or {}).get('misiones', {}).get(str(n), 'comun')
_POR_ID = {v['id']: k for k, v in _VER.items()}
for slug in args:
    L = json.load(open(os.path.join(AQUI, 'lecciones', slug + '.json'), encoding='utf-8'))
    m = re.search(r'Misión (\d+)', L.get('sub', ''))
    v = _version(L.get('materia'), m.group(1)) if m else 'comun'
    if v == 'variante' and not tiene_neutro(L) and not L.get('sin_variante'):
        E(slug, 'la misión es VARIANTE: faltan las partes "neutro" para alumnos de otros países (o "sin_variante": true si esta clase es igual para todos)')
    if v == 'alternativa' and not L.get('alternativa_de'):
        alt = L.get('alternativa')
        if not alt or not os.path.exists(os.path.join(AQUI, 'lecciones', alt + '.json')):
            E(slug, 'la misión es ALTERNATIVA: falta la clase para alumnos de otros países ("alternativa": "<slug>" con su archivo en lecciones/)')
if mis:
    v = _version(_POR_ID.get(mis.get('subject_id')), mis.get('tema'))
    if v == 'variante' and not tiene_neutro({k: x for k, x in mis.items() if k != 'alternativa'}):
        E(f'mision {mis["tema"]}', 'la misión es VARIANTE: faltan las partes "neutro" (PDF, actividades o examen) para alumnos de otros países')
    if v == 'alternativa' and not isinstance(mis.get('alternativa'), dict):
        E(f'mision {mis["tema"]}', 'la misión es ALTERNATIVA: falta "alternativa" con la misión entera para alumnos de otros países')
for slug in args:
    r = _rev_neutro(json.load(open(os.path.join(AQUI, 'lecciones', slug + '.json'), encoding='utf-8')))
    if r: E(slug, 'voseo sin pasar al diccionario neutro (agregar a MAPA u OK en tools/neutro.py): ' + ' '.join(r))
if mis:
    r = _rev_neutro(mis)
    if r: E(f'mision {mis["tema"]}', 'voseo sin pasar al diccionario neutro (agregar a MAPA u OK en tools/neutro.py): ' + ' '.join(r))
for e in err: print(e)
print('contenido:', 'OK' if not err else f'{len(err)} problema(s)'); sys.exit(1 if err else 0)
