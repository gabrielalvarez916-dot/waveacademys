# MÁQUINA DEL NIVEL MEDIO. Control de contenido: reglas que Gabriel fue marcando. Uso: python3 tools/medio/clase/revisar_contenido.py slug1 slug2 ... [--mision contenido/.../mision-N.json]
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
    if re.search(MESES, todo, re.I) and 'Julio Verne' not in todo and not L.get('meses_ok'): E(slug, 'nombra meses: los alumnos entran en cualquier fecha')
    for k, e in enumerate(L['escenas']):
        t = e['t']
        if t == 'mundo' and (e.get('fondo', 'nada') != 'nada' or any(('zoom' in a or 'mueve' in a) for p in e['pasos'] for a in p['acc'])) and 'subject_id' not in L:
            E(slug, f'escena {k}: mundo con fondo/zoom/movimiento (formato simple: fondo "nada")')
        if t == 'clasificar':
            for f in e['fichas']:
                if len(f['txt']) > 19: E(slug, f'escena {k}: ficha larga (>19): «{f["txt"]}»')
        if t == 'pregunta' and len(e['opciones']) < 3 and set(e['opciones']) != {'Sí', 'No'} and 'I' in (L.get('materia') or ''): E(slug, f'escena {k}: pregunta con menos de 3 opciones (secundaria)')
        if t == 'dato' and re.fullmatch(r'1[0-9]{3}|20[0-9]{2}', str(e.get('numero', ''))): E(slug, f'escena {k}: un año en "dato" sale con punto de miles; usar frase')
        for j, v in enumerate(e.get('voz', [])):
            if j in (e.get('voz_en') or []): continue  # frase dicha con voz en inglés
            for w in EXTR.findall(v.replace('*', '')):
                if w not in PRON and not any(w in p for p in PRON) and w.lower() not in ('hay', 'muy', 'hoy', 'voy', 'soy', 'estoy', 'ley', 'rey', 'yo', 'ya', 'yerba', 'uruguay', 'paraguay'):
                    E(slug, f'escena {k}: nombre extranjero sin pronunciación cargada: «{w}» (agregar a PRONUNCIA en voz_edge.py)')
    if re.search(r'lengua|literatura', (L.get('materia') or ''), re.I) and re.match(PROD, tit) and not any(e.get('titulo') == 'TU TURNO' for e in L['escenas']):  # y en la misión: actividad de escritura (keywords/IA)
        E(slug, 'nivel de producción sin escena "TU TURNO" que diga la tarea concreta')
# VÍA FONOLÓGICA (primeros años): la voz dice el SONIDO de las consonantes, no su nombre (ver GUIA.md «Vía fonológica»)
sys.path.insert(0, os.path.dirname(AQUI)); from primeros_anios import es_primeros as _es_prim
_CONS = 'BCDFGHJKLMNÑPQRSTVWXZ'
_NOMBRE = [re.compile(r'(?<![A-Za-zÁÉÍÓÚÑáéíóúñ])\*?[' + _CONS + r']\*?(?:\s*,\s*\*?[A-ZÁÉÍÓÚÑ]\*?(?![A-Za-zÁÉÍÓÚÑáéíóúñ])){1,}'),  # deletreo: T, O, M, I
           re.compile(r'\b(?:la|las|una|con|de|dos|\d+)\s+\*?[' + _CONS + r']\*?(?![A-Za-zÁÉÍÓÚÑáéíóúñ])', re.I),  # la T · con S · dos M
           re.compile(r'(?:^|[¿¡\s])\*?[' + _CONS + r']\*?\s+(?:con|o|y)\s')]  # M con A · T o D
for slug in args:
    L = json.load(open(os.path.join(AQUI, 'lecciones', slug + '.json'), encoding='utf-8'))
    if not _es_prim(L.get('materia'), contenido=L): continue
    for k, e in enumerate(L['escenas']):
        for v in e.get('voz', []):
            if any(rx.search(v) for rx in _NOMBRE): E(slug, f'escena {k}: la voz nombra una letra («{v}»): decir su sonido (sss, mmm, lll) o la sílaba (ta, pa, de)')
# VARIEDAD DEL BANCO DE FORMATOS (regla del Nivel Medio, ver GUIA.md «Variedad»): las clases van rotando las plantillas del banco
_BASICAS = {'pregunta', 'resumen', 'errores', 'definicion', 'reto', 'noticia', 'gancho', 'historia', 'chat', 'portada', 'tabla', 'clasificar', 'pasos', 'consejo', 'frase'}
_GANCHOS = {'gancho', 'historia', 'chat', 'noticia', 'reto'}
def _escenas(s):
    p = os.path.join(AQUI, 'lecciones', s + '.json')
    return [e.get('t') for e in json.load(open(p, encoding='utf-8'))['escenas']] if os.path.exists(p) else None
_secs = {s: _escenas(s) for s in args if not s.endswith('.neutro')}
for _s, _ts in _secs.items():
    if _ts and len({t for t in _ts if t not in _BASICAS}) < 2: E(_s, 'poca variedad: usar al menos 2 formatos distintos del banco fuera de los básicos')
# PLANTILLAS ESTILO PLATAFORMAS (regla desde nov 2026, solo clases nuevas: las de plataformas_existentes.txt no se revisan):
# cada clase usa al menos 2, y en una misión ninguna se repite en más de 2 clases.
_PLAT = {'fichas', 'completa', 'personaje', 'logro', 'pizarra', 'pistas', 'deslizador', 'prediccion', 'patron', 'contrarreloj', 'memoria', 'unir', 'mazo', 'tipeo', 'documental', 'escala', 'dilema', 'quiz4', 'transforma'}
try: _VIEJAS = set(open(os.path.join(AQUI, 'plataformas_existentes.txt'), encoding='utf-8').read().split())
except Exception: _VIEJAS = set()
_cuenta_plat = {}
for _s, _ts in _secs.items():
    if _s in _VIEJAS or _s.endswith('.neutro'): continue
    _p = {t for t in _ts if t in _PLAT}
    if len(_p) < 2: E(_s, 'faltan plantillas estilo plataformas: usar al menos 2 (fichas, completa, personaje, logro, pizarra, pistas, deslizador, prediccion, patron, contrarreloj, memoria, unir, mazo, tipeo, documental, escala, dilema, quiz4, transforma)')
    for t in _p: _cuenta_plat.setdefault((re.sub(r'-n\d+$', '', _s), t), []).append(_s)
for (_g, t), _ss in _cuenta_plat.items():
    if len(_ss) > 2: E(_g, f'plantilla «{t}» en {len(_ss)} clases de la misión (máximo 2): rotar las de plataformas')
_grupos = {}
for _s, _ts in _secs.items():
    if _ts: _grupos.setdefault(re.sub(r'-n\d+$', '', _s), []).append((_s, _ts))
for _g, _l in _grupos.items():
    _l.sort()
    if len(_l) >= 3:
        _cont = {}
        for _s, _ts in _l:
            for t in set(_ts):
                if t not in _BASICAS: _cont.setdefault(t, []).append(_s)
        for t, ss in _cont.items():
            if len(ss) > 3: E(_g, f'formato «{t}» en {len(ss)} clases de la misión (máximo 3 de 4): variar con otros del banco')
        if len({tuple(ts) for _, ts in _l}) < len(_l): E(_g, 'dos clases tienen exactamente la misma secuencia de escenas')
    for (s1, t1), (s2, t2) in zip(_l, _l[1:]):
        if t1[0] in _GANCHOS and t1[0] == t2[0]: E(s2, f'el gancho «{t2[0]}» repite el de la clase anterior: rotar gancho, historia, chat, noticia y reto')
    # contra la misión anterior de la misma materia: la misión nueva tiene que sumar formatos y no copiar moldes
    _m = re.match(r'(.*-m)(\d+)$', _g)
    if _m and int(_m.group(2)) > 1:
        _prev = [(_escenas(f'{_m.group(1)}{int(_m.group(2)) - 1}-n{k}')) for k in range(1, 5)]
        if all(_prev):
            usados = {t for ts in _prev for t in ts if t not in _BASICAS}
            nuevos = {t for _, ts in _l for t in ts if t not in _BASICAS} - usados
            if not nuevos: E(_g, 'no suma ningún formato del banco que no estuviera en la misión anterior: incorporar al menos uno nuevo')
            for k, (_s, _ts) in enumerate(_l):
                if k < 4 and _ts == _prev[k]: E(_s, 'misma secuencia de escenas que el mismo nivel de la misión anterior')
if mis:
    for n, c in mis['niveles'].items():
        s = f'mision {mis["tema"]} nivel {n}'
        tx =re.sub(r'(Revolución|Plaza|Avenida) de Mayo|\d+ de (diciembre|junio|marzo|septiembre)|Julio Verne', '', ' '.join(textos(c)))
        if re.search(MESES, tx, re.I) and not c.get('meses_ok'): E(s, 'el PDF nombra meses')  # "meses_ok": true solo cuando el tema son los meses o las fechas (calendario, fechas patrias)
        if 'en tu carpeta' in (c.get('ejemplo_solo') or {}).get('planteo', '') and any(q.get('t') == 'keywords' for q in mis['act'].get(n, [])): E(s, 'la producción se manda "a la carpeta": tiene que ir a la actividad del nivel')
    for n, acts in mis['act'].items():
        for q in acts:
            if q.get('t') == 'keywords' and isinstance(q.get('r'), dict): E(f'mision {mis["tema"]} act {n}', 'escritura con palabras clave: tiene que corregirla la IA (r como texto de referencia)')
# versión neutra: toda palabra que parezca voseo tiene que estar en el diccionario de tools/neutro.py
sys.path.insert(0, os.path.dirname(AQUI))  # tools/medio
from neutro_medio import revisar as _rev_neutro, tiene_neutro
# etiqueta de cada misión (común / variante / alternativa): la parte para alumnos de otros países no se puede olvidar
_VER = json.load(open(os.path.join(os.path.dirname(AQUI), 'versiones.json'), encoding='utf-8'))['materias']  # tools/medio/versiones.json (propia)
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
# primeros años (1.º a 3.º del Nivel Medio): frases cortas, clase corta, PDF con un dibujo por sección (regla en tools/primeros_anios.py)
from primeros_anios import es_primeros, oraciones, palabras, MAX_PALABRAS_VOZ, MAX_PALABRAS_PDF, MAX_ESCENAS
for slug in args:
    L = json.load(open(os.path.join(AQUI, 'lecciones', slug + '.json'), encoding='utf-8'))
    if not es_primeros(L.get('materia'), contenido=L): continue
    if len(L['escenas']) > MAX_ESCENAS: E(slug, f'primeros años: {len(L["escenas"])} escenas (máximo {MAX_ESCENAS}, clase de 3 a 4 minutos)')
    for k, e in enumerate(L['escenas']):
        for v in e.get('voz', []):
            if palabras(v.replace('*', '')) > MAX_PALABRAS_VOZ: E(slug, f'escena {k}: frase larga para primeros años (máx {MAX_PALABRAS_VOZ} palabras): «{v}»')
if mis and es_primeros(subject_id=mis.get('subject_id'), contenido=mis):
    def _largas(x, donde):
        for t in textos(x):
            for o in oraciones(t):
                if palabras(o) > MAX_PALABRAS_PDF: E(donde, f'oración larga para primeros años (máx {MAX_PALABRAS_PDF} palabras): «{o[:90]}»')
    for n, c in mis['niveles'].items():
        s = f'mision {mis["tema"]} nivel {n}'
        _largas({k: v for k, v in c.items() if k not in ('respuestas_carpeta', 'soluciones', 'estilo', 'secciones')}, s)
        _largas([[{k: v for k, v in b.items() if k not in ('png_base64', 'archivo', 'url', 'tipo', 'imagen_tipo')} for b in sec.get('bloques', [])] + [sec.get('titulo')] for sec in c.get('secciones', [])], s)
        for i, sec in enumerate(c.get('secciones', []), 1):
            if not any(b.get('tipo') == 'imagen' and (b.get('png_base64') or b.get('archivo') or b.get('url')) for b in sec.get('bloques', [])):
                E(s, f'sección {i} «{sec.get("titulo")}» sin dibujo (primeros años: un dibujo por sección)')
    for n, acts in mis['act'].items(): _largas([q.get('p') for q in acts], f'mision {mis["tema"]} act {n}')
    _largas([q[1].get('p') for q in mis['examen']], f'mision {mis["tema"]} examen')
for e in err: print(e)
print('contenido:', 'OK' if not err else f'{len(err)} problema(s)'); sys.exit(1 if err else 0)
