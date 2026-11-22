# -*- coding: utf-8 -*-
"""PRUEBA (no toca la plataforma): busca en la cuenta las voces «Mia» (argentina) y «Jenny» (mexicana), guarda la lista en voces.txt
y genera UNA frase con cada una, con las letras alargadas escritas 4 veces."""
import json, os, urllib.request
KEY = os.environ['ELEVEN_KEY']; H = {'xi-api-key': KEY, 'content-type': 'application/json'}
D = 'tools/medio/clase/prueba_eleven'; os.makedirs(D, exist_ok=True)
v = json.load(urllib.request.urlopen(urllib.request.Request('https://api.elevenlabs.io/v2/voices?page_size=100', headers=H), timeout=60)).get('voices', [])
with open(D + '/voces.txt', 'w') as f:
    for x in v:
        l = x.get('labels') or {}
        f.write(f"{x['voice_id']} | {x.get('name')} | {x.get('category')} | {l.get('gender','')} {l.get('accent','')} {l.get('language','')}\n")
def buscar(*claves):
    for x in v:
        if any(c in (x.get('name') or '').lower() for c in claves): return x
mia, jenny = buscar('mia', 'mía'), buscar('jenny')
print(len(v), 'voces · mia:', mia and (mia['voice_id'], mia['name']), '· jenny:', jenny and (jenny['voice_id'], jenny['name']))
for nombre, x in (('mia', mia), ('jenny', jenny)):
    if not x: continue
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{x['voice_id']}?output_format=mp3_44100_128",
        data=json.dumps({'text': 'to… mmmm… iiii: TOMI.', 'model_id': 'eleven_multilingual_v2'}).encode(), headers=H)
    open(f'{D}/{nombre}_tomi.mp3', 'wb').write(urllib.request.urlopen(req, timeout=120).read()); print('ok', nombre)
