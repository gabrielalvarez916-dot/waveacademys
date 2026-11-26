# -*- coding: utf-8 -*-
"""MÁQUINA DEL NIVEL MEDIO · carga la lección interactiva (niveles.N.leccion, escrita en sesión) de cada misión (función cargar_leccion_medio).
Uso: python tools/medio/cargar_leccion.py contenido/medio/<materia>/mision-N/mision-N.json ...   Variable: MEDIO_TOKEN."""
import json, os, sys, urllib.request, urllib.error
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_leccion_medio'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'
TOKEN = os.environ['MEDIO_TOKEN'].strip()
def lecciones(M):
    return {n: v['leccion'] for n, v in (M.get('niveles') or {}).items() if isinstance(v, dict) and v.get('leccion')}
error = False
for ruta in sys.argv[1:]:
    M = json.load(open(ruta, encoding='utf-8'))
    p = {'subject_id': M['subject_id'], 'tema': M['tema'], 'niveles': lecciones(M)}
    if isinstance(M.get('alternativa'), dict) and lecciones(M['alternativa']): p['alternativa'] = {'niveles': lecciones(M['alternativa'])}
    if not p['niveles']: print(ruta, ': sin lección interactiva todavía (queda el PDF)'); continue
    req = urllib.request.Request(URL, data=json.dumps({'p_token': TOKEN, 'p': p}).encode(), method='POST',
                                 headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: print(ruta, ':', r.read().decode())
    except urllib.error.HTTPError as e:
        error = True; print(ruta, ': ERROR', e.read().decode()[:300])
sys.exit(1 if error else 0)
