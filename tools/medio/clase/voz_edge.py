# -*- coding: utf-8 -*-
"""Genera la voz de una clase animada como AUDIO (voces neuronales de Microsoft vía edge-tts, gratis).
MÁQUINA DEL NIVEL MEDIO. Lee las frases de tools/medio/clase/lecciones/<slug>.json y guarda tools/medio/clase/voz/<leccion>.json con un mp3 por frase
y el momento de cada palabra (para los subtítulos). No repite frases que ya tienen audio con la misma voz.
Lo corre GitHub Actions (.github/workflows/voz-clases-medio.yml). Variables: VOZ (es-MX-JorgeNeural), RATE (+8%)."""
import variar, asyncio, base64, glob, hashlib, json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tools/medio
from neutro_medio import convertir, argentino
import edge_tts
import difflib, subprocess, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eleven_borrador import para_eleven

VOZ = os.environ.get('VOZ', 'es-MX-JorgeNeural')
RATE = os.environ.get('RATE', '+25%')
from primeros_anios import es_primeros, RATE as RATE_PRIMEROS, PITCH as PITCH_PRIMEROS, VOZ as VOZ_PRIMEROS, VOZ_NEUTRA as VOZ_NEUTRA_PRIMEROS  # 1.º a 3.º: voz pausada, cálida y expresiva
AQUI = os.path.dirname(os.path.abspath(__file__))


U = 'cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince dieciséis diecisiete dieciocho diecinueve veinte veintiuno veintidós veintitrés veinticuatro veinticinco veintiséis veintisiete veintiocho veintinueve'.split()
D = {3: 'treinta', 4: 'cuarenta', 5: 'cincuenta', 6: 'sesenta', 7: 'setenta', 8: 'ochenta', 9: 'noventa'}
C = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']


def _menos_de_mil(n):
    if n == 100: return 'cien'
    c, r = divmod(n, 100); out = [C[c]] if c else []
    if r:
        if r < 30: out.append(U[r])
        else:
            d, u = divmod(r, 10); out.append(D[d] + (' y ' + U[u] if u else ''))
    return ' '.join(out)


def en_letras(n):  # 4205 -> cuatro mil doscientos cinco
    if n < 1000: return U[n] if n < 30 else _menos_de_mil(n)
    if n < 1_000_000:
        m, r = divmod(n, 1000)
        pre = 'mil' if m == 1 else re.sub(r'uno$', 'ún', en_letras(m)).replace('veintiún', 'veintiún') + ' mil'
        return pre + (' ' + en_letras(r) if r else '')
    m, r = divmod(n, 1_000_000)
    pre = 'un millón' if m == 1 else re.sub(r'uno$', 'ún', en_letras(m)) + ' millones'
    return pre + (' ' + en_letras(r) if r else '')


LETRA = {'M': 'eme', 'D': 'de', 'C': 'ce', 'L': 'ele', 'X': 'equis', 'V': 've', 'I': 'i'}


def decir_numeros(s):
    s = re.sub(r'\b[MDCLXVI]{2,}\b', lambda m: ', '.join(LETRA[c] for c in m.group(0)), s)  # romanos: letra por letra
    def num(m):
        n = int(m.group(0).replace('.', ''))
        sig = s[m.end():m.end() + 3]
        w = en_letras(n)
        return 'un' if n == 1 and re.match(r' (?![yoeu]\b|[a-z]\b)[a-záéíóú]', sig) else w  # "1 grupo" -> "un grupo"
    return re.sub(r'\d{1,3}(?:\.\d{3})+(?!\d)|\d+', num, s)


ORD = {2: 'medio', 3: 'tercio', 4: 'cuarto', 5: 'quinto', 6: 'sexto', 7: 'séptimo', 8: 'octavo', 9: 'noveno', 10: 'décimo'}


def fraccion(m):  # 3/4 -> tres cuartos · 1/2 -> un medio · 5/12 -> cinco doceavos
    a, b = int(m.group(1)), int(m.group(2))
    if b == 1 or ' ' in en_letras(b) and b not in (100, 1000):
        return en_letras(a) + ' sobre ' + en_letras(b)
    den = ORD.get(b) or {100: 'centésimo', 1000: 'milésimo'}.get(b) or (en_letras(b) + 'avo')
    return ('un ' + den) if a == 1 else (en_letras(a) + ' ' + den + 's')


# Nombres extranjeros: cómo se dicen en castellano (solo cambia la voz, no el subtítulo)
PRONUNCIA = {'Sherlock Holmes': 'Shérlok Jolms', 'Holmes': 'Jolms', 'Watson': 'Uátson', 'Conan Doyle': 'Conan Doil', 'Oscar Wilde': 'Óscar Uáild', 'Wilde': 'Uáild', 'Baker Street': 'Béiker Strit', 'Canterville': 'Cánterwil', 'Jabez Wilson': 'Yábez Uílson', 'Wilson': 'Uílson', 'John Clay': 'Yon Cléi', 'Clay': 'Cléi', 'Spaulding': 'Spólding', 'Edgar Allan Poe': 'Édgar Álan Pou', 'Poe': 'Pou', 'Dupin': 'Dipán', 'Agatha Christie': 'Ágata Cristi', 'Poirot': 'Puaró', 'Walsh': 'Uolsh', 'Morgue': 'Morg', 'Bioy': 'Bióy', 'Arthur': 'Ártur', 'Greenwich': 'Grínich', 'Ushuaia': 'Ushuáia'}
def pronuncia(s):
    for a, b in PRONUNCIA.items(): s = re.sub(r'\b' + re.escape(a) + r'\b', b, s)
    return s

def limpio(s):  # igual que en el reproductor: lo que se DICE
    s = pronuncia(s.replace('*', ''))
    s = re.sub(r'\b(\d+) (?=\d+/\d+)', r'\1 y ', s)  # 1 3/4 -> 1 y tres cuartos
    s = re.sub(r'\b(\d+)/(\d+)\b', fraccion, s)
    s = re.sub(r'(\d),(0*)(?=\d)', lambda m: m.group(1) + ' coma ' + 'cero ' * len(m.group(2)), s)  # 0,075 -> 0 coma cero 75
    s = re.sub(r'\s*−\s*', ' menos ', s)
    s = re.sub(r'\s*÷\s*', ' dividido ', s)
    s = re.sub(r'\s*%', ' por ciento', s)
    s = s.replace('°', ' grados').replace('′', ' minutos')
    s = re.sub(r'\s*=\s*', ' igual a ', s)
    s = re.sub(r'(\d)([a-zA-Z])\b', r'\1 \2', s)  # 3n -> 3 n
    s = re.sub(r'\s*\+\s*', ' más ', s)
    s = re.sub(r'\s*×\s*', ' por ', s)
    return decir_numeros(s.replace('\\u2026', '…')).strip()


def frases(L):
    return [[limpio(x) for x in e['voz']] for e in L['escenas']]


VOZ_NEUTRA = {'naturales': 'es-MX-DaliaNeural', 'lengua': 'es-CO-GonzaloNeural', 'sociales': 'es-US-AlonsoNeural', 'otra': 'es-MX-JorgeNeural'}  # versión neutra (alumnos de otros países)
VOZ_MATERIA = {'naturales': 'es-AR-ElenaNeural', 'lengua': 'es-AR-TomasNeural', 'sociales': 'es-UY-MateoNeural'}  # cada materia con su voz (Matemática: Jorge)


def voz_de(L, neutra=False):
    m = (L.get('materia') or '').lower()
    if es_primeros(L.get('materia'), contenido=L) and not L.get('voz'):
        return VOZ_NEUTRA_PRIMEROS if neutra else VOZ_PRIMEROS
    if neutra:
        if L.get('voz_neutra'): return L['voz_neutra']
        if 'natural' in m or 'biolog' in m: return VOZ_NEUTRA['naturales']
        if 'lengua' in m or 'literatura' in m: return VOZ_NEUTRA['lengua']
        if 'social' in m or 'historia' in m or 'geograf' in m: return VOZ_NEUTRA['sociales']
        return VOZ_NEUTRA['otra']
    if L.get('voz'): return L['voz']
    if 'natural' in m or 'biolog' in m: return VOZ_MATERIA['naturales']
    if 'lengua' in m or 'literatura' in m: return VOZ_MATERIA['lengua']
    if 'social' in m or 'historia' in m or 'geograf' in m: return VOZ_MATERIA['sociales']
    return VOZ


async def tts(texto, voz=None, rate=None, pitch=None):
    rate = rate or RATE; extra = {'pitch': pitch} if pitch else {}
    try:
        c = edge_tts.Communicate(texto, voz or VOZ, rate=rate, boundary='WordBoundary', **extra)
    except TypeError:
        c = edge_tts.Communicate(texto, voz or VOZ, rate=rate, **extra)
    audio, w = b'', []
    async for ch in c.stream():
        if ch['type'] == 'audio':
            audio += ch['data']
        elif ch['type'] == 'WordBoundary':
            w.append(round(ch['offset'] / 10000))  # en milisegundos
    if not audio:
        raise RuntimeError('sin audio para: ' + texto)
    return {'a': base64.b64encode(audio).decode(), 'w': w}


# ───────── ElevenLabs (SOLO Lengua 1.º y 2.º año, nivel medio) ─────────
# Apagado por defecto: solo se enciende desde el flujo "Voz ElevenLabs Lengua" (ELEVEN_TOPE > 0). Modelo v3, estabilidad 0.5, similitud 0.75.
ELEVEN_KEY = os.environ.get('ELEVEN_KEY', '')
ELEVEN_TOPE = int(os.environ.get('ELEVEN_TOPE', '0') or 0)          # tope de caracteres por corrida (0 = no usar ElevenLabs)
ELEVEN_VERSIONES = os.environ.get('ELEVEN_VERSIONES', 'arg').split(',')  # arg, neutro
ELEVEN_VOCES = {'arg': os.environ.get('ELEVEN_VOZ_ARG', '0LdgqX7HWxqwl7GGMBS4'), 'neutro': os.environ.get('ELEVEN_VOZ_NEUTRO') or '87bJkTOBRagtx7PAFZDB'}
ELEVEN_MODELO = 'eleven_v3'
GASTADOS = [0]
import shutil
if ELEVEN_KEY and ELEVEN_TOPE > 0 and not (shutil.which('ffmpeg') and shutil.which('ffprobe')):
    sys.exit('Falta ffmpeg en la máquina: no se gastó nada de ElevenLabs')
ELEVEN_PARALELO = int(os.environ.get('ELEVEN_PARALELO', '2'))  # ElevenLabs limita los pedidos a la vez (con 4 respondía 429)
MANUALES = {}  # frases grabadas a mano por Gaby (no se pisan): {slug: [[escena, linea], ...]}
_mp = os.path.join(AQUI, 'voz', 'manuales.json')
if os.path.exists(_mp): MANUALES = json.load(open(_mp))


def eleven_activo(L, suf):
    if not (ELEVEN_KEY and ELEVEN_TOPE > 0): return False
    if not re.match(r'^\s*Lengua\s*[12]\b', L.get('materia') or '', re.I): return False
    v = 'neutro' if suf else 'arg'
    return v in ELEVEN_VERSIONES and bool(ELEVEN_VOCES[v])


def eleven_hash(vid, t):
    return hashlib.md5(('eleven-v3-s50-sim75|' + vid + '|' + para_eleven(t)).encode()).hexdigest()[:12]


def _ffmpeg(args, datos):
    return subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-loglevel', 'info', '-i', 'pipe:0'] + args, input=datos, capture_output=True)


def a_mp3_nivelado(crudo, objetivo=-20.0):
    m = _ffmpeg(['-af', 'loudnorm=print_format=summary', '-f', 'null', '-'], crudo).stderr.decode(errors='ignore')
    g = re.search(r'Input Integrated:\s+(-?[\d.]+)', m)
    db = (objetivo - float(g.group(1))) if g else 0
    r = _ffmpeg(['-af', f'volume={db:.2f}dB,alimiter=limit=0.9', '-ar', '24000', '-ac', '1', '-c:a', 'libmp3lame', '-b:a', '48k', '-write_xing', '0', '-f', 'mp3', 'pipe:1'], crudo)
    if not r.stdout: raise RuntimeError('ffmpeg sin salida')
    return r.stdout


def tiempos_palabras(texto, enviado, inicios):  # inicio (ms) de cada palabra del subtítulo, dentro del audio de lo enviado
    pos, p = [], 0
    for tok in texto.split():
        p = texto.index(tok, p); pos.append(p); p += len(tok)
    ops = difflib.SequenceMatcher(None, texto, enviado, autojunk=False).get_opcodes()
    out = []
    for x in pos:
        q = 0
        for tag, i1, i2, j1, j2 in ops:
            if i1 <= x < i2 or (x == i2 == len(texto)):
                q = j1 + (x - i1) if tag == 'equal' else j1 + int((x - i1) * (j2 - j1) / max(1, i2 - i1)); break
        out.append(round(inicios[min(q, len(inicios) - 1)] * 1000))
    return out


async def tts_eleven(texto, vid):
    env = para_eleven(texto)
    cuerpo = json.dumps({'text': env, 'model_id': ELEVEN_MODELO, 'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75}}).encode()
    def pedir():
        rq = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128', data=cuerpo,
                                    headers={'xi-api-key': ELEVEN_KEY, 'content-type': 'application/json'})
        return json.load(urllib.request.urlopen(rq, timeout=180))
    j = await asyncio.get_event_loop().run_in_executor(None, pedir)
    crudo = base64.b64decode(j['audio_base64'])
    al = j.get('alignment') or j.get('normalized_alignment') or {}
    ini = al.get('character_start_times_seconds') or []
    if len(ini) < len(env):  # sin tiempos por letra: se reparte proporcional a lo largo del audio
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', '-'], input=crudo, capture_output=True).stdout or 3)
        ini = [dur * i / max(1, len(env)) for i in range(len(env))]
    return {'a': base64.b64encode(a_mp3_nivelado(crudo)).decode(), 'w': tiempos_palabras(texto, env, ini)}


PARALELO = int(os.environ.get('VOZ_PARALELO', '4'))  # frases que se graban a la vez
INICIO = time.time(); MINUTOS = float(os.environ.get('VOZ_MINUTOS', '0') or 0)  # tope de tiempo por corrida (0 = sin tope)
PENDIENTES = []


async def grabar(L, nombre, suf, vz):
    destino = os.path.join(AQUI, 'voz', nombre + suf + '.json')
    cache = {}
    for v in {nombre + '.json', nombre + '.neutro.json'}:  # se reusan frases iguales entre las dos versiones (misma voz)
        pv = os.path.join(AQUI, 'voz', v)
        if os.path.exists(pv): cache.update({f.get('h'): f for esc in json.load(open(pv)) for f in esc if isinstance(f, dict)})
    F = frases(L)
    prim = es_primeros(L.get('materia'), contenido=L)
    rate = RATE_PRIMEROS if prim else RATE
    pitch = PITCH_PRIMEROS if prim else None
    res, nuevas = [], 0
    l12 = bool(re.match(r'^\s*Lengua\s*[12]\b', L.get('materia') or '', re.I)); textos = {}
    el = eleven_activo(L, suf); vid = ELEVEN_VOCES['neutro' if suf else 'arg'] if el else ''
    viejo = json.load(open(destino)) if os.path.exists(destino) else []
    prot = {tuple(x) for x in MANUALES.get(nombre, [])} if el else set()
    if el:  # la lección se hace entera o no se hace (cada lección completa cuesta lo mismo que sus frases nuevas)
        costo = sum(len(para_eleven(t)) for i, esc in enumerate(F) for j, t in enumerate(esc) if (i, j) not in prot and eleven_hash(vid, t) not in cache)
        if costo and GASTADOS[0] + costo > ELEVEN_TOPE:
            PENDIENTES.append(nombre + suf); print('SALTEADA por tope de gasto:', nombre + suf, costo, 'caracteres'); return
        GASTADOS[0] += costo
    # se graban EN PARALELO (de a PARALELO frases a la vez): mismo audio, mismo orden, mucho más rápido
    sem = asyncio.Semaphore(ELEVEN_PARALELO if el else PARALELO)
    async def grabar_una(t):
        async with sem:
            for intento in range(6):
                try:
                    if el: return await tts_eleven(t, vid)
                    return await tts(t, vz, rate, pitch)
                except Exception as e:
                    if intento == 5: raise
                    await asyncio.sleep(5 * (intento + 1))  # Microsoft a veces corta por muchos pedidos seguidos
    pedidos = {}  # hash -> tarea (una frase repetida se graba una sola vez)
    for ie, esc in enumerate(F):
        fila = []
        for il, t in enumerate(esc):
            if el and (ie, il) in prot and ie < len(viejo) and il < len(viejo[ie]): fila.append(viejo[ie][il]); continue  # grabada a mano: se respeta
            if not el and l12 and ie < len(viejo) and il < len(viejo[ie]) and viejo[ie][il].get('e') and viejo[ie][il].get('th') == hashlib.md5(t.encode()).hexdigest()[:12]:
                fila.append(viejo[ie][il]); continue  # ya tiene voz de ElevenLabs: una corrida común NO la pisa
            h = eleven_hash(vid, t) if el else hashlib.md5((vz + rate + (pitch or '') + t).encode()).hexdigest()[:12]
            if h in cache:
                fila.append(cache[h])
            else:
                if MINUTOS and time.time() - INICIO > MINUTOS * 60:
                    PENDIENTES.append(nombre + suf); return
                if h not in pedidos: pedidos[h] = asyncio.ensure_future(grabar_una(t)); textos[h] = t
                fila.append(h)
        res.append(fila)
    hechos = dict(zip(pedidos, await asyncio.gather(*pedidos.values())))
    for h, r in hechos.items():
        r['h'] = h
        if el: r['e'] = 1; r['th'] = hashlib.md5(textos[h].encode()).hexdigest()[:12]
    nuevas = len(hechos)
    res = [[hechos[f] if isinstance(f, str) else f for f in fila] for fila in res]
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    json.dump(res, open(destino, 'w'), separators=(',', ':'))
    print(nombre + suf, ':', sum(len(e) for e in F), 'frases,', nuevas, 'nuevas, voz', ('ElevenLabs ' + vid) if el else vz, rate)


async def una(src_path):
    crudo = json.load(open(src_path, encoding='utf-8'))
    nombre = crudo.get('slug') or os.path.basename(src_path)[:-5]
    L = argentino(crudo); variar.preparar(L)
    N = convertir(crudo); variar.preparar(N)  # versión en español neutro, con sus partes "neutro"
    await grabar(L, nombre, '', voz_de(L))
    await grabar(N, nombre, '.neutro', voz_de(L, True))


async def main():
    for p in (sys.argv[1:] or sorted(glob.glob(os.path.join(AQUI, 'lecciones', '*.json')))):
        try:
            await una(p)
        except Exception as e:  # una clase que falla no frena a las demás: queda sin voz y se graba en la próxima corrida
            print('ERROR', os.path.basename(p), ':', e)
    marca = os.path.join(AQUI, 'voz', '.pendiente')
    if PENDIENTES:
        open(marca, 'w').write('\n'.join(PENDIENTES)); print('Quedan para la próxima corrida:', len(PENDIENTES))
    elif os.path.exists(marca): os.remove(marca)

asyncio.run(main())
