# -*- coding: utf-8 -*-
"""MÁQUINA DEL NIVEL MEDIO · publica sola cada misión del Nivel Medio que quedó COMPLETA
(4 clases, 4 PDF, Relámpago y examen) con la función publicar_completas_medio. Nunca despublica.
Lo corren al final voz-clases-medio.yml y mision-medio.yml (lo que termine último la publica). Variable: MEDIO_TOKEN."""
import json, os, sys, urllib.request
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/publicar_completas_medio'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'  # clave pública (la misma de js/config.js)
req = urllib.request.Request(URL, data=json.dumps({'p_token': os.environ['MEDIO_TOKEN'].strip()}).encode(), method='POST',
                             headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
with urllib.request.urlopen(req, timeout=60) as r: print('Publicadas:', json.loads(r.read()))
