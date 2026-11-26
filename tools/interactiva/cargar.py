# -*- coding: utf-8 -*-
"""MÁQUINA · carga (o actualiza) la práctica de cada tema de la lección interactiva en los borradores de la misión.
Sirve para misiones nuevas y para las ya cargadas (no toca nada más del borrador). Lo corre .github/workflows/mision-avanzado.yml.
Uso: python tools/interactiva/cargar.py contenido/<materia>/mision-N/mision-N.json [...]"""
import json, os, sys, urllib.request, urllib.error
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_practicas'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'
TOKEN = os.environ['WAVE_GEN_TOKEN'].strip()
error = False
for ruta in sys.argv[1:]:
    M = json.load(open(ruta, encoding='utf-8'))
    # Los niveles marcados pdf_en_otra_mision no traen secciones: no se mandan, así no se borran sus prácticas.
    p = {'subject_id': M['subject_id'], 'tema': M['tema'], 'niveles': {k: v for k, v in (M.get('niveles') or {}).items() if not (isinstance(v, dict) and v.get('pdf_en_otra_mision'))}}
    if isinstance(M.get('alternativa'), dict) and M['alternativa'].get('niveles'): p['alternativa'] = {'niveles': M['alternativa']['niveles']}
    req = urllib.request.Request(URL, data=json.dumps({'p_token': TOKEN, 'p': p}).encode(), method='POST',
                                 headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: print(ruta, ':', r.read().decode())
    except urllib.error.HTTPError as e:
        error = True; print(ruta, ': ERROR', e.read().decode()[:400])
sys.exit(1 if error else 0)
