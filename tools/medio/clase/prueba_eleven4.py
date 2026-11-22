# -*- coding: utf-8 -*-
"""PRUEBA: usa directo (sin agregarlas a la cuenta) dos voces de la biblioteca: Carolina (rioplatense) y Jenny (latina). Una frase cada una."""
import json, os, urllib.request
H = {'xi-api-key': os.environ['ELEVEN_KEY'], 'content-type': 'application/json'}
D = 'tools/medio/clase/prueba_eleven'; os.makedirs(D, exist_ok=True)
for nombre, vid in (('carolina', '0LdgqX7HWxqwl7GGMBS4'), ('cande', 'yFykvY9iSJewrANOC0cU'), ('jenny', '87bJkTOBRagtx7PAFZDB')):
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{vid}?output_format=mp3_44100_128',
        data=json.dumps({'text': 'to… mmmm… iiii: TOMI.', 'model_id': 'eleven_multilingual_v2'}).encode(), headers=H)
    try:
        open(f'{D}/{nombre}_tomi.mp3', 'wb').write(urllib.request.urlopen(req, timeout=120).read()); print('ok', nombre)
    except Exception as e:
        print('ERROR', nombre, getattr(e, 'code', ''), getattr(e, 'read', lambda: b'')()[:300])
