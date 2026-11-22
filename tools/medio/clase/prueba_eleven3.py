# -*- coding: utf-8 -*-
"""PRUEBA (no toca la plataforma): una voz argentina femenina (no la clonada) y «Jenny» de México; una frase con cada una."""
import json, os, urllib.parse, urllib.request
KEY = os.environ['ELEVEN_KEY']; H = {'xi-api-key': KEY, 'content-type': 'application/json'}
D = 'tools/medio/clase/prueba_eleven'; os.makedirs(D, exist_ok=True)
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request('https://api.elevenlabs.io' + u, headers=H), timeout=60))
def post(u, d): return json.load(urllib.request.urlopen(urllib.request.Request('https://api.elevenlabs.io' + u, data=json.dumps(d).encode(), headers=H), timeout=60))
cuenta = get('/v2/voices?page_size=100').get('voices', [])
def de_cuenta(f):
    for x in cuenta:
        if f(x): return x['voice_id'], x['name']
def lab(x, k): return ((x.get('labels') or {}).get(k) or '').lower()
def biblioteca(q):
    r = get('/v1/shared-voices?page_size=15&' + urllib.parse.urlencode(q)).get('voices', [])
    for x in r[:15]: print('  cand', x.get('name'), x.get('accent'), x.get('gender'), x.get('voice_id'))
    return r
def agregar(x):
    try: post(f"/v1/voices/add/{x['public_owner_id']}/{x['voice_id']}", {'new_name': x['name']}); return x['voice_id'], x['name']
    except Exception as e: print('no pude agregar', x['name'], e)
arg = de_cuenta(lambda x: 'argentin' in lab(x, 'accent') and lab(x, 'gender') == 'female' and 'mia' not in x['name'].lower() and x.get('category') != 'cloned')
if not arg:
    r = biblioteca({'language': 'es', 'accent': 'argentine', 'gender': 'female'}); arg = r and agregar(r[0])
jen = de_cuenta(lambda x: 'jenny' in x['name'].lower())
if not jen:
    r = biblioteca({'search': 'jenny', 'language': 'es'}) or biblioteca({'language': 'es', 'accent': 'mexican', 'gender': 'female'}); jen = r and agregar(r[0])
print('arg:', arg, '· jenny:', jen)
for nombre, x in (('arg', arg), ('jenny', jen)):
    if not x: continue
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{x[0]}?output_format=mp3_44100_128",
        data=json.dumps({'text': 'to… mmmm… iiii: TOMI.', 'model_id': 'eleven_multilingual_v2'}).encode(), headers=H)
    open(f'{D}/{nombre}_tomi.mp3', 'wb').write(urllib.request.urlopen(req, timeout=120).read()); print('ok', nombre, x)
