# -*- coding: utf-8 -*-
"""Genera la voz de una clase animada como AUDIO (voces neuronales de Microsoft vía edge-tts, gratis).
Lee las frases de tools/clase/<leccion>.src.html y guarda tools/clase/voz/<leccion>.json con un mp3 por frase
y el momento de cada palabra (para los subtítulos). No repite frases que ya tienen audio con la misma voz.
Lo corre GitHub Actions (.github/workflows/voz-clases.yml). Variables: VOZ (es-MX-JorgeNeural), RATE (+8%)."""
import asyncio, base64, glob, hashlib, json, os, re, sys
import edge_tts

VOZ = os.environ.get('VOZ', 'es-MX-JorgeNeural')
RATE = os.environ.get('RATE', '+8%')
AQUI = os.path.dirname(os.path.abspath(__file__))


def limpio(s):  # igual que en el reproductor: lo que se DICE
    s = s.replace('*', '')
    s = re.sub(r'\s*\+\s*', ' más ', s)
    s = re.sub(r'\s*×\s*', ' por ', s)
    return s.replace('\\u2026', '…').strip()


def frases(src):
    out = []
    for m in re.finditer(r"voz: \[(.*?)\],\s*\n\s*armar", src, re.S):
        out.append([limpio(x) for x in re.findall(r"'((?:[^'\\]|\\.)*)'", m.group(1))])
    return out


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
    nombre = os.path.basename(src_path).replace('.src.html', '')
    destino = os.path.join(AQUI, 'voz', nombre + '.json')
    viejo = json.load(open(destino)) if os.path.exists(destino) else []
    cache = {f.get('h'): f for esc in viejo for f in esc if isinstance(f, dict)}
    F = frases(open(src_path, encoding='utf-8').read())
    res, nuevas = [], 0
    for esc in F:
        fila = []
        for t in esc:
            h = hashlib.md5((VOZ + RATE + t).encode()).hexdigest()[:12]
            if h in cache:
                fila.append(cache[h])
            else:
                for intento in range(3):
                    try:
                        r = await tts(t); break
                    except Exception as e:
                        if intento == 2: raise
                        await asyncio.sleep(3)
                r['h'] = h; fila.append(r); nuevas += 1
        res.append(fila)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    json.dump(res, open(destino, 'w'), separators=(',', ':'))
    print(nombre, ':', sum(len(e) for e in F), 'frases,', nuevas, 'nuevas, voz', VOZ, RATE)


async def main():
    for p in (sys.argv[1:] or sorted(glob.glob(os.path.join(AQUI, '*.src.html')))):
        if 'demo-' in os.path.basename(p):
            continue
        await una(p)

asyncio.run(main())
