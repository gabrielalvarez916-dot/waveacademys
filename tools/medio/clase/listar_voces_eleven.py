# -*- coding: utf-8 -*-
"""Lista las voces de la cuenta de ElevenLabs (no gasta créditos). Guarda tools/medio/clase/prueba_eleven/voces.txt."""
import json, os, urllib.request
req = urllib.request.Request('https://api.elevenlabs.io/v2/voices?page_size=100', headers={'xi-api-key': os.environ['ELEVEN_KEY']})
v = json.load(urllib.request.urlopen(req, timeout=60)).get('voices', [])
os.makedirs('tools/medio/clase/prueba_eleven', exist_ok=True)
with open('tools/medio/clase/prueba_eleven/voces.txt', 'w') as f:
    for x in v:
        l = x.get('labels') or {}
        f.write(f"{x['voice_id']} | {x.get('name')} | {x.get('category')} | {l.get('gender','')} {l.get('accent','')} {l.get('language','')} | {(x.get('description') or '')[:60]}\n")
print(len(v), 'voces')
