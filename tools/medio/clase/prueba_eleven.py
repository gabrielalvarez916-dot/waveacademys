# -*- coding: utf-8 -*-
"""PRUEBA de voz con ElevenLabs (NO toca la plataforma ni las clases): genera unos pocos mp3 para escucharlos.
Clave: secreto ELEVEN_KEY de GitHub. Guarda los mp3 en tools/medio/clase/prueba_eleven/."""
import base64, json, os, re, sys, urllib.request
KEY = os.environ['ELEVEN_KEY']
VOCES = ['3gPFGgE0k2MQEWPgTpZa', 'FXGrCtY3PEyfqczBAlqm']
MODELO = os.environ.get('ELEVEN_MODELO', 'eleven_multilingual_v2')
FRASES = [
    ('tere1', 'Ahora vos. Mirá la primera letra.'),
    ('tere2', '¿Qué nombre empieza igual que Tomi?'),
    ('tere3', '¡TERE! To-mi y te-re empiezan igual.'),
    ('sss_normal', 'Con sss: Sofi y Santi.'),
    ('sss_larga', 'Con ssssss: Sofi y Santi.'),
]
SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prueba_eleven')
os.makedirs(SALIDA, exist_ok=True)
gastados = 0
for v in VOCES:
    for nombre, texto in FRASES:
        req = urllib.request.Request(
            f'https://api.elevenlabs.io/v1/text-to-speech/{v}?output_format=mp3_44100_128',
            data=json.dumps({'text': texto, 'model_id': MODELO}).encode(),
            headers={'xi-api-key': KEY, 'content-type': 'application/json'})
        try:
            audio = urllib.request.urlopen(req, timeout=120).read()
        except Exception as e:
            print('Error', v, nombre, getattr(e, 'code', ''), getattr(e, 'read', lambda: b'')()[:200]); sys.exit(1)
        open(os.path.join(SALIDA, f'{v[:6]}_{nombre}.mp3'), 'wb').write(audio)
        gastados += len(texto); print('ok', v[:6], nombre, len(audio))
print('caracteres gastados:', gastados)
