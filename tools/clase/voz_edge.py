# -*- coding: utf-8 -*-
"""Genera la voz de una clase animada como AUDIO (voces neuronales de Microsoft vía edge-tts, gratis).
Lee las frases de tools/clase/lecciones/<slug>.json y guarda tools/clase/voz/<leccion>.json con un mp3 por frase
y el momento de cada palabra (para los subtítulos). No repite frases que ya tienen audio con la misma voz.
Lo corre GitHub Actions (.github/workflows/voz-clases.yml). Variables: VOZ (es-MX-JorgeNeural), RATE (+8%)."""
import asyncio, base64, glob, hashlib, json, os, re, sys
import edge_tts

VOZ = os.environ.get('VOZ', 'es-MX-JorgeNeural')
RATE = os.environ.get('RATE', '+25%')
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


def limpio(s):  # igual que en el reproductor: lo que se DICE
    s = s.replace('*', '')
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


async def tts(texto):
    try:
        c = edge_tts.Communicate(texto, VOZ, rate=RATE, boundary='WordBoundary')
    except TypeError:
        c = edge_tts.Communicate(texto, VOZ, rate=RATE)
    audio, w = b'', []
    async for ch in c.stream():
        if ch['type'] == 'audio':
            audio += ch['data']
        elif ch['type'] == 'WordBoundary':
            w.append(round(ch['offset'] / 10000))  # en milisegundos
    if not audio:
        raise RuntimeError('sin audio para: ' + texto)
    return {'a': base64.b64encode(audio).decode(), 'w': w}


async def una(src_path):
    L = json.load(open(src_path, encoding='utf-8'))
    nombre = L.get('slug') or os.path.basename(src_path)[:-5]
    destino = os.path.join(AQUI, 'voz', nombre + '.json')
    viejo = json.load(open(destino)) if os.path.exists(destino) else []
    cache = {f.get('h'): f for esc in viejo for f in esc if isinstance(f, dict)}
    F = frases(L)
    res, nuevas = [], 0
    for esc in F:
        fila = []
        for t in esc:
            h = hashlib.md5((VOZ + RATE + t).encode()).hexdigest()[:12]
            if h in cache:
                fila.append(cache[h])
            else:
                for intento in range(6):
                    try:
                        r = await tts(t); break
                    except Exception as e:
                        if intento == 5: raise
                        await asyncio.sleep(5 * (intento + 1))  # Microsoft a veces corta por muchos pedidos seguidos
                r['h'] = h; fila.append(r); nuevas += 1
        res.append(fila)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    json.dump(res, open(destino, 'w'), separators=(',', ':'))
    print(nombre, ':', sum(len(e) for e in F), 'frases,', nuevas, 'nuevas, voz', VOZ, RATE)


async def main():
    for p in (sys.argv[1:] or sorted(glob.glob(os.path.join(AQUI, 'lecciones', '*.json')))):
        try:
            await una(p)
        except Exception as e:  # una clase que falla no frena a las demás: queda sin voz y se graba en la próxima corrida
            print('ERROR', os.path.basename(p), ':', e)

asyncio.run(main())
