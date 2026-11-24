# -*- coding: utf-8 -*-
"""PROFUNDIDAD Y NO REPETICIÓN (regla del 23/11/2026, Avanzado y Medio, solo misiones nuevas). La corre tools/control_calidad.py
ANTES de cargar; si algo no cumple, no se carga nada y el log dice qué arreglar. Sin IA. Texto de la regla: docs/reglas-fijas-pdf.md,
sección "Profundidad y no repetición".

1) LO YA VISTO NO SE VUELVE A EXPLICAR. Se arma la lista de lo ya visto (términos, definiciones, glosario y ejemplos) de TODAS las misiones
   anteriores de la misma familia de materias (misma materia en años previos, en el nivel Medio si existe, y misiones anteriores del mismo año).
   Un término ya definido no puede volver a definirse casi igual, y un ejemplo ya usado no puede volver a usarse.
   Etiqueta de la misión (mapa_curricular.relacion): Nuevo = nada de lo anterior; Retoma = se apoya en lo visto para explicar OTRA cosa;
   Profundiza = el mismo tema pero MÁS a fondo, nunca igual. Los repasos van en actividades y examen, no en el PDF ni en la clase.
2) PDF: mínimo de palabras por nivel, etapas con conceptos, ejemplo completo con pasos.
3) CLASES ANIMADAS: mínimo de escenas y de palabras de voz por clase.
4) PREGUNTAS: una pregunta "pensada" tiene que traer un caso o texto (mínimo de palabras); la máquina ya no cree la etiqueta sola.
   Tope de recordar, de respuestas de una palabra y de consignas de carpeta sin caso."""
import glob, json, os, re, sys, unicodedata, urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

# ---- umbrales (cambiar acá y en docs/reglas-fijas-pdf.md) ----
SIM_DEF = 0.50          # parecido de definiciones del mismo término (palabras de contenido)
SIM_DEF_NUEVO = 0.30    # misión "Nuevo": un término ya definido no puede volver ni con otra redacción parecida
SIM_EJ = 0.60           # parecido de ejemplos
PDF_PALABRAS = {'avanzado': 400, 'medio': 320, 'primeros': 200}   # por nivel, sin carpeta ni claves
PDF_ETAPAS = {'avanzado': 2, 'medio': 2, 'primeros': 1}            # secciones mínimas de etapa 1 y de etapa 2
CLASE = {'avanzado': (8, 220), 'medio': (8, 180), 'primeros': (6, 130)}   # (escenas, palabras de voz) por clase
PENSADA_MIN_PALABRAS = {'avanzado': 12, 'medio': 9, 'primeros': 6}   # palabras del caso o texto de una pregunta pensada
RECORDAR_MAX = {'avanzado': 0.25, 'medio': 0.30, 'primeros': 0.40}
UNA_PALABRA_MAX = {'avanzado': 0.25, 'medio': 0.30, 'primeros': 0.40}
CARPETA_CON_CASO = {'avanzado': 3, 'medio': 2, 'primeros': 1}      # de cada 4 consignas, al menos tantas con un caso (o una cuenta)
PENSADAS = {'aplicar', 'analizar', 'error'}

STOP = set('''para como pero porque cuando donde sobre entre desde hasta esta este esto estos estas ese esa eso esos esas una uno unos unas del los las
con por que sus muy mas son era fue ser hay han tiene tienen puede pueden cada todo toda todos todas otro otra otros otras algo nada alguien
tambien solo sino si no ya el la lo le les se su al en de y o a e u es un'''.split())

def norm(s):
    s = unicodedata.normalize('NFD', str(s).lower())
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', ''.join(c for c in s if unicodedata.category(c) != 'Mn'))).strip()

def palabras(s):
    return {w for w in norm(re.sub(r'<[^>]+>', ' ', str(s))).split() if len(w) > 2 and w not in STOP}

def sim(a, b):
    A, B = palabras(a), palabras(b)
    if not A or not B: return 0.0
    return len(A & B) / len(A | B)

def textos(x):
    if isinstance(x, str): yield x
    elif isinstance(x, dict):
        for k, v in x.items():
            if k in ('png_base64',): continue
            yield from textos(v)
    elif isinstance(x, list):
        for v in x: yield from textos(v)

# ---- ubicación de la misión: familia de materia y orden (nivel, año, misión) ----
def ubicar(ruta):
    r = os.path.relpath(os.path.abspath(ruta), RAIZ).replace('\\', '/')
    m = re.match(r'contenido/(medio/)?([a-z]+)-(\d+)/mision-(\d+)/', r)
    if not m: return None
    medio, fam, anio, mis = bool(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4))
    return {'ruta': r, 'familia': fam, 'orden': (1 if not medio else 0, anio, mis), 'medio': medio, 'anio': anio, 'mision': mis}

def _items(M):
    """(términos, ejemplos): términos = lista de (termino, texto, donde); ejemplos = lista de (texto, donde)."""
    ter, eje = [], []
    for k, N in (M.get('niveles') or {}).items():
        for g in N.get('glosario') or []:
            ter.append((norm(g.get('palabra', '')), g.get('significado', ''), f'glosario del nivel {k}'))
        for s in N.get('secciones') or []:
            for b in s.get('bloques') or []:
                if b.get('tipo') == 'definicion': ter.append((norm(b.get('titulo', '')), b.get('texto', ''), f'definición del nivel {k}'))
                if b.get('tipo') == 'ejemplo': eje.append((' '.join([str(b.get('texto', ''))] + [str(i) for i in b.get('items') or []]), f'ejemplo del nivel {k}'))
        for c in ('ejemplo_completo', 'ejemplo_incompleto', 'ejemplo_solo'):
            e = N.get(c)
            if e: eje.append((' '.join(textos(e)), f'{c.replace("_", " ")} del nivel {k}'))
    return ter, eje

def _lo_ya_visto(me):
    previas = []
    for p in glob.glob(os.path.join(RAIZ, 'contenido', '**', 'mision-*.json'), recursive=True):
        u = ubicar(p)
        if not u or u['familia'] != me['familia'] or u['ruta'] == me['ruta'] or u['orden'] >= me['orden']: continue
        try: M = json.load(open(p, encoding='utf-8'))
        except Exception: continue
        previas.append((u, M))
    return previas

def _etiqueta(M):
    """Etiqueta de la misión en mapa_curricular (Nuevo / Retoma / Profundiza), vía la función mision_relacion. Si no se puede leer, None."""
    tok = os.environ.get('WAVE_GEN_TOKEN') or os.environ.get('MEDIO_TOKEN') or os.environ.get('WAVE_MEDIO_TOKEN')
    if not tok or not M.get('subject_id') or not M.get('tema'): return None
    try:
        req = urllib.request.Request('https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/mision_relacion',
            data=json.dumps({'p_token': tok.strip(), 'p_subject': M['subject_id'], 'p_tema': int(M['tema'])}).encode(), method='POST',
            headers={'apikey': 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-', 'Authorization': 'Bearer sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-', 'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=20) as r: return json.loads(r.read().decode()) or None
    except Exception: return None

def revisar_repeticion(ruta, M, err, avi, etiqueta=None):
    me = ubicar(ruta)
    if not me: return
    etiqueta = etiqueta or _etiqueta(M)
    ter, eje = _items(M)
    previas = _lo_ya_visto(me)
    umbral = SIM_DEF_NUEVO if etiqueta == 'Nuevo' else SIM_DEF
    vistos = set()
    for t, x, donde in ter:
        for u, P in previas:
            for t2, x2, d2 in _items(P)[0]:
                if t and t == t2 and sim(x, x2) >= umbral and (t, u['ruta']) not in vistos:
                    vistos.add((t, u['ruta']))
                    err.append(f'ya visto: «{t}» ({donde}) ya se definió en {u["ruta"]} ({d2}). No se vuelve a explicar'
                               + (' (misión Nuevo: nada de lo anterior)' if etiqueta == 'Nuevo' else ' — Retoma: usalo para explicar OTRA cosa; Profundiza: más a fondo, no igual'))
    for x, donde in eje:
        for u, P in previas:
            for x2, d2 in _items(P)[1]:
                if sim(x, x2) >= SIM_EJ and (x[:40], u['ruta']) not in vistos:
                    vistos.add((x[:40], u['ruta']))
                    err.append(f'ya visto: el {donde} repite el {d2} de {u["ruta"]}: «{x[:60]}…». Usá un caso nuevo')

def revisar_pdf(M, nivel, err):
    for k, N in (M.get('niveles') or {}).items():
        base = {a: b for a, b in N.items() if a not in ('carpeta', 'carpeta_nivel', 'respuestas_carpeta', 'soluciones')}
        n = len(' '.join(textos(base)).split())
        if n < PDF_PALABRAS[nivel]: err.append(f'nivel {k} · PDF: {n} palabras; el mínimo es {PDF_PALABRAS[nivel]} (sin contar carpeta). Explicá más y con más ejemplos')
        secs = N.get('secciones') or []
        for et in (1, 2):
            c = sum(1 for s in secs if s.get('etapa') == et)
            if c < PDF_ETAPAS[nivel]: err.append(f'nivel {k} · PDF: {c} sección(es) de etapa {et}; el mínimo es {PDF_ETAPAS[nivel]}')
        ec = N.get('ejemplo_completo') or {}
        if len(ec.get('pasos') or []) < 3 and nivel != 'primeros': err.append(f'nivel {k} · PDF: el ejemplo completo tiene menos de 3 pasos')

ESTRUCTURADOS = {'numeric', 'ordering', 'matching', 'classify', 'tap_text', 'tokens', 'table_fill', 'multi_select', 'keywords', 'odd_one_out', 'label_image'}
def _es_pensada_real(q, nivel='avanzado'):
    # Los tipos que ya exigen armar o resolver algo (ordenar, unir, clasificar, tocar, fichas, cuentas…) valen por sí solos;
    # opción múltiple, V/F, respuesta corta y completar necesitan además un caso o texto de PENSADA_MIN_PALABRAS palabras.
    p = re.sub(r'\[\[[^\]]*\]\]', ' ', str(q.get('p') or ''))
    if str(q.get('n') or '').lower().strip() not in PENSADAS: return False
    return q.get('t') in ESTRUCTURADOS or len(p.split()) >= PENSADA_MIN_PALABRAS[nivel]

def _una_palabra(q):
    if q.get('t') != 'short_answer': return False
    p = str(q.get('p') or '').lower()
    ac = (q.get('r') or {}).get('acepta') if isinstance(q.get('r'), dict) else None
    return bool(re.search(r'una (sola )?palabra|solo la palabra', p)) or bool(ac and all(len(str(a).split()) <= 1 for a in ac))

def revisar_preguntas(M, nivel, err):
    qs = []
    for k, l in (M.get('act') or {}).items():
        if str(k) == '5': continue            # el Relámpago es velocidad a propósito
        qs += [q for q in (l or []) if isinstance(q, dict)]
    for it in (M.get('examen') or []):
        q = it[1] if isinstance(it, list) and len(it) > 1 else it
        if isinstance(q, dict): qs.append(q)
    car = [c for N in (M.get('niveles') or {}).values() for c in (N.get('carpeta') or [])]
    if qs:
        pens = sum(_es_pensada_real(q, nivel) for q in qs)
        rec = len(qs) - pens
        if rec > RECORDAR_MAX[nivel] * len(qs):
            err.append(f'preguntas: {rec} de {len(qs)} son de recordar ({int(100 * rec / len(qs))} %); el tope es {int(RECORDAR_MAX[nivel] * 100)} %. '
                       f'Una pregunta cuenta como pensada solo si lleva etiqueta aplicar/analizar/error Y un caso o texto de {PENSADA_MIN_PALABRAS[nivel]} palabras o más (salvo ordenar, unir, clasificar, tocar, fichas, cuentas)')
        una = sum(_una_palabra(q) for q in qs)
        tot = len(qs) + len(car)
        una += sum(bool(re.search(r'una (sola )?palabra|solo la palabra', str(c if isinstance(c, str) else (c or {}).get('consigna', '')), re.I)) for c in car)
        if una > UNA_PALABRA_MAX[nivel] * tot: err.append(f'preguntas: {una} de {tot} piden una sola palabra o un número suelto ({int(100 * una / tot)} %); el tope es {int(UNA_PALABRA_MAX[nivel] * 100)} %')
    for k, N in (M.get('niveles') or {}).items():
        cs = [c if isinstance(c, str) else (c or {}).get('consigna', '') for c in (N.get('carpeta') or [])]
        con = sum(len(re.sub(r'\[\[[^\]]*\]\]', ' ', c).split()) >= PENSADA_MIN_PALABRAS[nivel] or bool(re.search(r'\d', c)) for c in cs)
        if cs and con < min(CARPETA_CON_CASO[nivel], len(cs)): err.append(f'nivel {k} · carpeta: {con} consigna(s) con un caso (≥{PENSADA_MIN_PALABRAS[nivel]} palabras o una cuenta); el mínimo es {CARPETA_CON_CASO[nivel]}')

def _clases_de(ruta, M):
    """Clases animadas de la misión: se busca por materia y número de misión (docstring de mision-N.py / mision.py)."""
    d = os.path.dirname(os.path.abspath(ruta)); n = (ubicar(ruta) or {}).get('mision')
    fuente = [f for f in glob.glob(os.path.join(d, '*.py')) + glob.glob(os.path.join(os.path.dirname(d), f'mision-{n}.py'))]
    materia = None
    for f in fuente:
        m = re.search(r'"""\s*(?:[^"]*?·\s*)?([^·"(\n]+?)\s*(?:\([^)]*\))?\s*·\s*Misi[oó]n\s*(\d+)', open(f, encoding='utf-8').read(800))
        if m and int(m.group(2)) == n: materia = m.group(1).strip(); break
    out = []
    for dirc in (os.path.join(RAIZ, 'tools', 'clase', 'lecciones'), os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones')):
        for p in glob.glob(os.path.join(dirc, '*.json')):
            if p.endswith('.neutro.json'): continue
            try: L = json.load(open(p, encoding='utf-8'))
            except Exception: continue
            if materia and L.get('materia') == materia and re.search(rf'Misi[oó]n {n}\b', L.get('sub', '')): out.append((p, L))
    return materia, out

def revisar_clases(ruta, M, nivel, err, avi):
    materia, cl = _clases_de(ruta, M)
    if not cl:
        avi.append('clases: no encontré las clases animadas de esta misión para medir su duración (se revisan cuando se suban)'); return
    esc_min, voz_min = CLASE[nivel]
    for p, L in cl:
        e = L.get('escenas') or []
        voz = sum(len(' '.join(x.get('voz', [])).split()) for x in e if isinstance(x.get('voz'), list))
        if len(e) < esc_min or voz < voz_min:
            err.append(f'clase {L.get("slug")}: {len(e)} escenas y {voz} palabras de voz; el mínimo es {esc_min} escenas y {voz_min} palabras. Explicá más, con un ejemplo resuelto paso a paso')

def existentes():
    ruta = os.path.join(AQUI, 'profundidad_existentes.txt')
    if not os.path.exists(ruta): return set()
    return {l.strip() for l in open(ruta, encoding='utf-8') if l.strip() and not l.startswith('#')}

def revisar(ruta, M, nivel, err, avi, forzar=False, etiqueta=None):
    rel = os.path.relpath(os.path.abspath(ruta), RAIZ).replace('\\', '/')
    if not forzar and rel in existentes(): return
    n = len(err)
    revisar_repeticion(ruta, M, err, avi, etiqueta)
    revisar_pdf(M, nivel, err)
    revisar_preguntas(M, nivel, err)
    revisar_clases(ruta, M, nivel, err, avi)
    return len(err) - n

if __name__ == '__main__':
    # Uso de prueba: python tools/profundidad.py [--todas] ruta.json ...   (informa sin frenar)
    sys.path.insert(0, AQUI)
    import control_calidad as cc
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--todas' in sys.argv:
        args = sorted(os.path.relpath(p, RAIZ) for p in glob.glob(os.path.join(RAIZ, 'contenido', '**', 'mision-*.json'), recursive=True))
    for r in args:
        M = json.load(open(r, encoding='utf-8')); err, avi = [], []
        revisar(r, M, cc.tipo_nivel(r, M), err, avi, forzar=True, etiqueta='-')
        print(('✗' if err else '✓'), r, f'({len(err)})')
        for e in err[:int(os.environ.get('MAX', '6'))]: print('   -', e[:230])
