# -*- coding: utf-8 -*-
"""PRUEBA con el borrador real (eleven_borrador.para_eleven): la frase «to… mmm… i: TOMI.» con Carolina (argentina) y Jenny (latina)."""
import json, os, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eleven_borrador import para_eleven
H = {'xi-api-key': os.environ['ELEVEN_KEY'], 'content-type': 'application/json'}
D = 'tools/medio/clase/prueba_eleven'; os.makedirs(D, exist_ok=True)
txt = para_eleven('to… mmm… i: TOMI.'); print('texto enviado:', txt)
for nombre, vid in (('carolina', '0LdgqX7HWxqwl7GGMBS4'), ('jenny', '87bJkTOBRagtx7PAFZDB')):
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{vid}?output_format=mp3_44100_128',
        data=json.dumps({'text': txt, 'model_id': 'eleven_multilingual_v2'}).encode(), headers=H)
    open(f'{D}/{nombre}_tomi_borrador.mp3', 'wb').write(urllib.request.urlopen(req, timeout=120).read()); print('ok', nombre)
