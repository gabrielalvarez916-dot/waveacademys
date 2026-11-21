# -*- coding: utf-8 -*-
"""MÁQUINA DEL NIVEL MEDIO · carga una misión en la plataforma con la función propia cargar_mision_medio
(actividades de cada nivel, Relámpago en la lección 5 y examen "Nivel jefe", todo SIN publicar).
Si la misión ya estaba cargada, no pisa nada y sigue. Solo acepta materias del Nivel Medio (la función rechaza el resto).
Lo corre .github/workflows/mision-medio.yml. Variable: MEDIO_TOKEN (secreto).
Uso: python tools/medio/cargar_mision.py contenido/medio/<materia>/mision-N/mision-N.json [...]"""
import json, os, sys, urllib.request, urllib.error

URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_mision_medio'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'  # clave pública (la misma de js/config.js)
TOKEN = os.environ['MEDIO_TOKEN'].strip()
YA = ('ya tiene actividades', 'ya tiene examen')

error = False
for ruta in sys.argv[1:]:
    M = json.load(open(ruta, encoding='utf-8'))
    p = {k: v for k, v in M.items() if k != 'niveles'}  # el contenido del PDF no va a la base: lo sube pdf-medio
    req = urllib.request.Request(URL, data=json.dumps({'p_token': TOKEN, 'p': p}).encode(), method='POST',
                                 headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: print(ruta, ':', r.read().decode())
    except urllib.error.HTTPError as e:
        msg = e.read().decode()[:400]
        if any(y in msg for y in YA): print(ruta, ': ya estaba cargada, no se pisa nada')
        else: error = True; print(ruta, ': ERROR', msg)
sys.exit(1 if error else 0)
