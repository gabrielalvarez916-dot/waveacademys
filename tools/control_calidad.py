# -*- coding: utf-8 -*-
"""CONTROL DE CALIDAD de una misión (Avanzado y Medio), ANTES de cargarla. Si algo no cumple, frena la carga
y explica qué arreglar. Sin IA. Reglas: docs/reglas-fijas-pdf.md (sección "Calidad de carpeta, actividades y examen").

Uso: python tools/control_calidad.py contenido/<materia>/mision-N/mision-N.json [...]
     python tools/control_calidad.py --todas      (revisa todas, sin frenar: solo informa)

Etiqueta de nivel que pide cada consigna o pregunta (obligatoria en misiones nuevas):
- carpeta: en cada nivel, "carpeta_nivel": ["recordar", "aplicar", "analizar", "error"], paralela a "carpeta".
- actividades y examen: en cada pregunta, "n": "recordar" | "aplicar" | "analizar" | "error".
  aplicar = usar lo aprendido en un caso nuevo · analizar = comparar, explicar causas, justificar ·
  error = encontrar y corregir un error típico ("un compañero dice…"). Las tres cuentan como "pensadas".
Las misiones que ya estaban en el repo al poner esta regla (tools/calidad_existentes.txt) no se revisan."""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, 'medio'))
try:
    from primeros_anios import es_primeros
except Exception:
    def es_primeros(materia=None, subject_id=None, contenido=None): return False

NIVELES = {'recordar', 'aplicar', 'analizar', 'error'}
PENSADAS = {'aplicar', 'analizar', 'error'}
CON_IA = {'open', 'solve_complete'}
ELECCION = {'multiple_choice', 'true_false'}

# Mínimos por tipo de nivel. carpeta = pensadas por nivel (PDF); act = pensadas en las actividades de los niveles 1 a 4
# (el Relámpago no cuenta: es velocidad a propósito); examen = pensadas en el banco y tope de opción múltiple + V/F.
REGLAS = {
    'avanzado': {'carpeta': 2, 'act': 3, 'examen': 5, 'eleccion_max': 0.60, 'examen_no_eleccion_pensada': 1},
    'medio':    {'carpeta': 1, 'act': 2, 'examen': 4, 'eleccion_max': 0.70, 'examen_no_eleccion_pensada': 1},
    'primeros': {'carpeta': 1, 'act': 2, 'examen': 3, 'eleccion_max': 0.80, 'examen_no_eleccion_pensada': 0},
}

# Consignas que piden solo recordar: no pueden ir etiquetadas como pensadas.
MEMORIA = re.compile(r'^\W*(¿\s*)?(c[oó]mo se llama|c[oó]mo se llaman|qu[eé] (es|son|se llama)\b|cu[aá]l es el nombre|c[oó]mo se denomina)'
                     r'|respond[eé] (s[ií] o no|solo s[ií] o no)', re.I)
# Distractores de relleno: se descartan solos y regalan la respuesta.
RELLENO = re.compile(r'^\W*(todas las anteriores|ninguna de las anteriores|no s[eé]|cualquiera|agua sucia|son lindas?|no importa|nada que ver)\W*$', re.I)
ABSOLUTOS = re.compile(r'^\W*(nada|nunca|ninguno|ninguna|siempre|solo en .+|nadie)\W*$', re.I)

def norm(s): return re.sub(r'\s+', ' ', re.sub(r'[^\wñáéíóúü%° ]', ' ', str(s).lower())).strip()

def existentes():
    ruta = os.path.join(AQUI, 'calidad_existentes.txt')
    if not os.path.exists(ruta): return set()
    return {l.strip() for l in open(ruta, encoding='utf-8') if l.strip() and not l.startswith('#')}

def tipo_nivel(ruta, M):
    if '/medio/' in ruta.replace('\\', '/'):
        return 'primeros' if es_primeros(subject_id=M.get('subject_id'), contenido=M) or M.get('estilo') == 'primeros' else 'medio'
    return 'avanzado'

def revisar_pregunta(q, donde, nivel, err, avi):
    t = q.get('t'); p = str(q.get('p') or ''); o = q.get('o'); r = q.get('r') or {}
    n = str(q.get('n') or '').lower().strip()
    if n not in NIVELES: err.append(f'{donde}: falta "n" (recordar, aplicar, analizar o error)')
    if t in CON_IA: err.append(f'{donde}: tipo "{t}" llama a la IA; usá keywords, short_answer o numeric (sin IA)')
    if n in PENSADAS and MEMORIA.search(p): err.append(f'{donde}: está como "{n}" pero pide recordar un nombre o un sí/no: «{p[:70]}»')
    if t in ('multiple_choice', 'multi_select', 'odd_one_out') and isinstance(o, list):
        ops = [str(x) for x in o]
        if len({(norm(x) or str(x).strip()) for x in ops}) < len(ops): err.append(f'{donde}: opciones repetidas')
        if nivel != 'primeros' and t == 'multiple_choice' and len(ops) < 3 and {norm(x) for x in ops} != {'sí', 'no'}:
            err.append(f'{donde}: menos de 3 opciones')
        corr = r.get('correcta') if isinstance(r, dict) else r
        correctas = [corr] if t != 'multi_select' else list((r or {}).get('correctas') or [])
        if t == 'multiple_choice' and corr is not None and corr not in ops: err.append(f'{donde}: la correcta no está entre las opciones')
        distr = [x for x in ops if x not in correctas]
        for x in distr:
            if RELLENO.match(x): err.append(f'{donde}: distractor de relleno «{x}»: usá un error típico (lo de "ojo" del PDF)')
            elif ABSOLUTOS.match(x) and nivel != 'primeros': avi.append(f'{donde}: distractor absoluto «{x}»: suele descartarse solo')
        if t == 'multiple_choice' and corr and distr:
            largo, mayor = len(str(corr)), max(len(x) for x in distr)
            if largo > 25 and largo > 2 * mayor: err.append(f'{donde}: la correcta es mucho más larga que las demás y se delata: igualá el largo')
    return n

# ======================================================================================================================
# PROFUNDIDAD Y NO REPETICIÓN (regla del 23/11/2026; hace parte del MISMO control, no es otro aparte).
# 1) Lo ya visto no se vuelve a explicar (según la etiqueta Nuevo/Retoma/Profundiza de mapa_curricular). 2) PDF: mínimo de palabras por nivel.
# 3) Clases animadas: mínimo de escenas y de voz. 4) Preguntas: pensada = etiqueta + caso o texto; topes de recordar y de una palabra.
# Texto de la regla: docs/reglas-fijas-pdf.md, sección "Profundidad y no repetición".
# ======================================================================================================================
import glob, unicodedata, urllib.request
RAIZ = os.path.dirname(AQUI)
# ---- umbrales (cambiar acá y en docs/reglas-fijas-pdf.md) ----
SIM_DEF = 0.80          # misma explicación casi igual (Retoma/Profundiza pueden volver a usar el término; lo que no vale es repetir la explicación)
SIM_DEF_NUEVO = 0.50    # misión "Nuevo": un término ya definido no puede volver con una explicación parecida
SIM_EJ = 0.60           # parecido de ejemplos
PDF_ETAPAS = {'avanzado': 2, 'medio': 2, 'primeros': 1}            # secciones mínimas de etapa 1 y de etapa 2
ENSEÑAN = {'definicion', 'pasos', 'errores', 'resumen', 'tabla', 'comparar', 'linea', 'flujo', 'causas', 'texto', 'corrige', 'matriz', 'escala', 'noticia'}
DISTINTAS_AV, ENSEÑAN_AV = 8, 5   # 80-85% del modelo: las 4 clases de Lengua II M1 (10 escenas, 10 plantillas distintas, 6-8 que enseñan, 282-295 palabras)
DISTINTAS_ME, ENSEÑAN_ME = 5, 2   # 85% de las primeras 60 clases de Medio (21/11): 7,2 escenas, 6,3 plantillas distintas, 2,2 que enseñan, 123 palabras
CLASE = {'avanzado': (10, 280), 'medio': (6, 105), 'primeros': (6, 105)}   # (escenas, palabras de voz): 85% de las primeras clases medidas — Avanzado 11 esc/329 pal (18-19/11), Medio/primeros 7 esc/124 pal (21/11)
PROCEDIMENTALES = {'matematica', 'fisica', 'quimica'}   # repetir el tema es válido si suben las cifras: solo se compara el ejemplo con los mismos números  
PENSADA_MIN_PALABRAS = {'avanzado': 12, 'medio': 9, 'primeros': 6}   # palabras del caso o texto de una pregunta pensada
RECORDAR_MAX = {'avanzado': 0.25, 'medio': 0.30, 'primeros': 0.40}
UNA_PALABRA_MAX = {'avanzado': 0.25, 'medio': 0.30, 'primeros': 0.40}
CARPETA_CON_CASO = {'avanzado': 3, 'medio': 2, 'primeros': 1}      # de cada 4 consignas, al menos tantas con un caso (o una cuenta)

STOP = set('''para como pero porque cuando donde sobre entre desde hasta esta este esto estos estas ese esa eso esos esas una uno unos unas del los las
con por que sus muy mas son era fue ser hay han tiene tienen puede pueden cada todo toda todos todas otro otra otros otras algo nada alguien
tambien solo sino si no ya el la lo le les se su al en de y o a e u es un'''.split())

def norm_t(s):
    s = unicodedata.normalize('NFD', str(s).lower())
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', ''.join(c for c in s if unicodedata.category(c) != 'Mn'))).strip()

def palabras(s):
    return {w for w in norm_t(re.sub(r'<[^>]+>', ' ', str(s))).split() if len(w) > 2 and w not in STOP}

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
            ter.append((norm_t(g.get('palabra', '')), g.get('significado', ''), f'glosario del nivel {k}'))
        for s in N.get('secciones') or []:
            for b in s.get('bloques') or []:
                if b.get('tipo') == 'definicion': ter.append((norm_t(b.get('titulo', '')), b.get('texto', ''), f'definición del nivel {k}'))
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
    for t, x, donde in ([] if me['familia'] in PROCEDIMENTALES else ter):
        for u, P in previas:
            for t2, x2, d2 in _items(P)[0]:
                if t and t == t2 and sim(x, x2) >= umbral and (t, u['ruta']) not in vistos:
                    vistos.add((t, u['ruta']))
                    err.append(f'ya visto: «{t}» ({donde}) ya se explicó casi igual en {u["ruta"]} ({d2}). Ahora: «{str(x)[:90]}» / Antes: «{str(x2)[:90]}». No se vuelve a explicar'
                               + (' (misión Nuevo: nada de lo anterior)' if etiqueta == 'Nuevo' else ' — Retoma: usalo para explicar OTRA cosa; Profundiza: más a fondo, no igual'))
    for x, donde in eje:
        for u, P in previas:
            for x2, d2 in _items(P)[1]:
                if sim(x, x2) >= SIM_EJ and set(re.findall(r'\d+', x)) == set(re.findall(r'\d+', x2)) and (x[:40], u['ruta']) not in vistos:
                    vistos.add((x[:40], u['ruta']))
                    err.append(f'ya visto: el {donde} repite el {d2} de {u["ruta"]}: «{x[:60]}…». Usá un caso nuevo')

def revisar_pdf(M, nivel, err):
    for k, N in (M.get('niveles') or {}).items():
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
        for k, e in enumerate(L.get('escenas') or []):
            if e.get('t') == 'dato' and (L.get('materia', '').lower().startswith('lengua') or not re.search(r'\d|mill|mil', str(e.get('numero', '')).lower())):
                err.append(f'clase {L.get("slug")}: la escena {k + 1} usa «dato», que es para cifras y muestra un número grande: en Lengua o sin cifra real usá otra plantilla (consejo, definición…)')
    for p, L in cl:
        e = L.get('escenas') or []
        voz = sum(len(' '.join(x.get('voz', [])).split()) for x in e if isinstance(x.get('voz'), list))
        ts = [x.get('t') for x in e]
        ens = sum(t in ENSEÑAN for t in ts)
        dmin, emin, modelo = (DISTINTAS_AV, ENSEÑAN_AV, 'Lengua II, Misión 1') if nivel == 'avanzado' else (DISTINTAS_ME, ENSEÑAN_ME, 'primeras clases de Medio, 21/11')
        if len(set(ts)) < dmin: err.append(f'clase {L.get("slug")}: usa {len(set(ts))} plantillas distintas; el mínimo es {dmin} (modelo: {modelo}). Variá los recursos')
        if ens < emin: err.append(f'clase {L.get("slug")}: {ens} escenas que enseñan (definición, pasos, errores, resumen, tabla, comparar, línea, flujo, causas, texto, corrige, matriz, escala o noticia); el mínimo es {emin} (modelo: {modelo})')
        if len(e) < esc_min or voz < voz_min:
            err.append(f'clase {L.get("slug")}: {len(e)} escenas y {voz} palabras de voz (≈{voz / 2.7 / 60:.1f} min); el mínimo es {esc_min} escenas y {voz_min} palabras (línea base de las primeras clases). Explicá más, con un ejemplo resuelto paso a paso')


def revisar_profundidad(ruta, M, nivel, err, avi, forzar=False, etiqueta=None):
    n = len(err)
    revisar_repeticion(ruta, M, err, avi, etiqueta)
    revisar_pdf(M, nivel, err)
    revisar_preguntas(M, nivel, err)
    revisar_clases(ruta, M, nivel, err, avi)
    return len(err) - n



def revisar(ruta, forzar=False):
    M = json.load(open(ruta, encoding='utf-8'))
    nivel = tipo_nivel(ruta, M); R = REGLAS[nivel]
    err, avi = [], []
    # Carpeta de cada nivel (PDF)
    for k, N in sorted((M.get('niveles') or {}).items(), key=lambda x: int(x[0]) if str(x[0]).isdigit() else 0):
        cons = N.get('carpeta') or []; tags = [str(x).lower().strip() for x in (N.get('carpeta_nivel') or [])]
        resp = N.get('respuestas_carpeta') or []
        d = f'nivel {k} · carpeta'
        if len(tags) != len(cons): err.append(f'{d}: "carpeta_nivel" tiene que tener una etiqueta por consigna ({len(cons)})'); continue
        if any(x not in NIVELES for x in tags): err.append(f'{d}: etiqueta inválida (vale recordar, aplicar, analizar o error)')
        for i, (c, tg) in enumerate(zip(cons, tags)):
            texto = c if isinstance(c, str) else (c or {}).get('consigna', '')
            if tg in PENSADAS and MEMORIA.search(texto): err.append(f'{d} {i + 1}: está como "{tg}" pero pide recordar un nombre o un sí/no')
            acepta = resp[i] if i < len(resp) else []
            acepta = acepta if isinstance(acepta, list) else [acepta]
            if not [a for a in acepta if str(a).strip()]: err.append(f'{d} {i + 1}: sin respuesta válida en respuestas_carpeta')
            elif any(len(str(a).split()) > 6 for a in acepta): err.append(f'{d} {i + 1}: respuesta válida de más de 6 palabras: la app la compara letra por letra; reformulá para que la respuesta sea corta')
        p = sum(t in PENSADAS for t in tags)
        if p < R['carpeta']: err.append(f'{d}: {p} consigna(s) pensada(s); el mínimo es {R["carpeta"]} (caso nuevo, causa y consecuencia, comparar o error típico, con respuesta corta)')
        if nivel != 'primeros' and 'error' not in tags: avi.append(f'{d}: ninguna consigna apunta a un error típico (regla del PDF)')
    # Actividades (niveles 1 a 4; el 5 es Relámpago)
    pens = 0
    for k, lista in (M.get('act') or {}).items():
        for j, q in enumerate(lista or []):
            n = revisar_pregunta(q, f'actividad {k}.{j + 1}', nivel, err, avi)
            if str(k) != '5' and n in PENSADAS: pens += 1
    # Cantidad fija (regla acordada): 4 actividades después de cada lección (niveles 1 a 4) y 4 generales (nivel 5)
    A = M.get('act') or {}
    for k in ['1', '2', '3', '4', '5']:
        cant = len(A.get(k) or A.get(int(k)) or [])
        if cant != 4: err.append(f'actividades del nivel {k}: hay {cant}; tienen que ser 4' + (' (las generales)' if k == '5' else ' (las que van después de la lección)'))
    if M.get('act') and pens < R['act']: err.append(f'actividades: {pens} pensada(s) en los niveles 1 a 4; el mínimo es {R["act"]}')
    # Examen (banco del nivel jefe)
    ex = M.get('examen') or []
    if ex:
        pens = elec = no_elec_pens = 0
        for j, it in enumerate(ex):
            q = it[1] if isinstance(it, list) and len(it) > 1 else it
            n = revisar_pregunta(q, f'examen {j + 1}', nivel, err, avi)
            pens += n in PENSADAS; elec += q.get('t') in ELECCION
            no_elec_pens += (n in PENSADAS and q.get('t') not in ELECCION)
        if pens < R['examen']: err.append(f'examen: {pens} pregunta(s) pensada(s) de {len(ex)}; el mínimo es {R["examen"]}')
        if elec > R['eleccion_max'] * len(ex): err.append(f'examen: {elec} de {len(ex)} son opción múltiple o V/F; el tope es {int(R["eleccion_max"] * 100)} %')
        if no_elec_pens < R['examen_no_eleccion_pensada']: err.append('examen: falta al menos 1 pregunta pensada que no sea de elegir (keywords, numeric, short_answer, classify, ordering…)')
    # VARIEDAD DE TIPOS (regla del 23/11/2026, solo misiones nuevas): actividades (niveles 1 a 4) + examen.
    # Ningún tipo de pregunta puede pasar del tope, y tiene que haber un mínimo de tipos distintos.
    if forzar or os.path.relpath(os.path.abspath(ruta), os.path.dirname(AQUI)).replace('\\', '/') not in existentes():
        V = {'avanzado': (.40, 5), 'medio': (.50, 4), 'primeros': (.60, 3)}[nivel]
        ts = [q.get('t') for k, l in (M.get('act') or {}).items() if str(k) != '5' for q in (l or [])]
        ts += [(it[1] if isinstance(it, list) and len(it) > 1 else it).get('t') for it in (M.get('examen') or [])]
        if ts:
            c = {}
            for t in ts: c[t] = c.get(t, 0) + 1
            top = max(c, key=c.get)
            if c[top] > V[0] * len(ts): err.append(f'variedad: «{top}» es {c[top]} de {len(ts)} preguntas (más del {int(V[0] * 100)} %); usá otros tipos (ordenar, unir, clasificar, completar, tocá el texto, fichas, numérica, palabras clave, crucigrama, sopa…)')
            if len(c) < V[1]: err.append(f'variedad: solo {len(c)} tipos de pregunta distintos; el mínimo es {V[1]}')
    # PROFUNDIDAD Y NO REPETICIÓN (mismo control, solo misiones nuevas)
    if forzar or os.path.relpath(os.path.abspath(ruta), os.path.dirname(AQUI)).replace('\\', '/') not in existentes():
        try: revisar_profundidad(ruta, M, nivel, err, avi, forzar=True)
        except Exception as ex: avi.append(f'profundidad: no se pudo revisar ({ex})')
    return nivel, err, avi

def main():
    args = sys.argv[1:]
    informe = '--todas' in args
    if informe:
        base = os.path.join(os.path.dirname(AQUI), 'contenido')
        args = sorted(os.path.relpath(os.path.join(r, f), os.path.dirname(AQUI)) for r, _, fs in os.walk(base) for f in fs if re.fullmatch(r'mision-\d+\.json', f))
    viejas = set() if informe else existentes()
    frenar = False
    for ruta in args:
        rel = ruta.replace('\\', '/')
        if rel in viejas: print(f'{rel}: misión anterior a la regla, no se revisa'); continue
        nivel, err, avi = revisar(ruta, forzar=informe)
        if err:
            frenar = True
            print(f'\n✗ {rel} ({nivel}): {len(err)} problema(s) — NO se carga')
            for e in err: print('   -', e)
        else:
            print(f'✓ {rel} ({nivel}): cumple la regla de calidad')
        for a in avi: print('   (aviso)', a)
    sys.exit(1 if frenar and not informe else 0)

if __name__ == '__main__':
    main()
