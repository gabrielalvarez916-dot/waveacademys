# -*- coding: utf-8 -*-
"""PRUEBA: el texto de Gaby (3 frases de la clase 3) con la voz Carolina, ajustes estabilidad 0.5 / similitud 0.75, y lista de modelos.
Compara la duración con su audio hecho a mano (15,3 s). ~120 caracteres por modelo probado."""
import json, os, urllib.request
H = {'xi-api-key': os.environ['ELEVEN_KEY'], 'content-type': 'application/json'}
D = 'tools/medio/clase/prueba_eleven'; os.makedirs(D, exist_ok=True)
cand = ['eleven_v4', 'eleven_v3', 'eleven_multilingual_v2']  # la clave no puede listar modelos: se prueban por nombre
txt = 'Ahora vos. Mirá la primera letra.\n¿Qué nombre empieza igual que Tomi?\n¡TERE! tttt oooo mmmm iiii y tttt eeee rrrr eeee empiezan igual'
for mid in cand:
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/0LdgqX7HWxqwl7GGMBS4?output_format=mp3_44100_128',
        data=json.dumps({'text': txt, 'model_id': mid, 'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75}}).encode(), headers=H)
    try:
        open(f'{D}/gaby_{mid}.mp3', 'wb').write(urllib.request.urlopen(req, timeout=120).read()); print('ok', mid)
    except Exception as e:
        print('ERROR', mid, getattr(e, 'code', ''), getattr(e, 'read', lambda: b'')()[:200])
