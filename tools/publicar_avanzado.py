# -*- coding: utf-8 -*-
"""Máquina del AVANZADO · publica sola cada misión del Nivel Avanzado que quedó COMPLETA
(4 lecciones con clase o video y PDF, práctica y examen) con la función publicar_completas_avanzado. Nunca despublica.
Lo corren al final voz-clases.yml y pdfs-lecciones.yml. Variable: WAVE_GEN_TOKEN (secreto que ya usan los PDF)."""
import json, os, sys, urllib.request
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/publicar_completas_avanzado'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'  # clave pública (la misma de js/config.js)
req = urllib.request.Request(URL, data=json.dumps({'p_token': os.environ['WAVE_GEN_TOKEN'].strip()}).encode(), method='POST',
                             headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
with urllib.request.urlopen(req, timeout=60) as r: print('Publicadas:', json.loads(r.read()))
