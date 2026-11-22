# -*- coding: utf-8 -*-
"""PRUEBA: 4 formas de escribir la «iiii» final para que NO la lea como la «y». Solo Carolina (argentina). ~100 caracteres."""
import json, os, urllib.request
H = {'xi-api-key': os.environ['ELEVEN_KEY'], 'content-type': 'application/json'}
D = 'tools/medio/clase/prueba_eleven'; os.makedirs(D, exist_ok=True)
V = {'a': 'tttt oooo… mmmm… iiii… TOMI.', 'b': 'tttt oooo… mmmm… iiiiii: TOMI.', 'c': 'tttt oooo… mmmm… iiii, TOMI.', 'd': 'tttt oooo… mmmm… iiii. TOMI.'}
for k, t in V.items():
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/0LdgqX7HWxqwl7GGMBS4?output_format=mp3_44100_128',
        data=json.dumps({'text': t, 'model_id': 'eleven_multilingual_v2'}).encode(), headers=H)
    open(f'{D}/carolina_var_{k}.mp3', 'wb').write(urllib.request.urlopen(req, timeout=120).read()); print('ok', k, t)
