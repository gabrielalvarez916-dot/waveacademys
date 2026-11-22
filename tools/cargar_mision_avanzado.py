# -*- coding: utf-8 -*-
"""MÁQUINA DEL AVANZADO · carga una misión (borradores de PDF, actividades, Relámpago y examen, todo SIN publicar)
con cargar_mision_avanzado. Si ya estaba cargada no pisa nada. Lo corre .github/workflows/mision-avanzado.yml. Variable: WAVE_GEN_TOKEN.
Uso: python tools/cargar_mision_avanzado.py contenido/<materia>/mision-N/mision-N.json [...]"""
import json, os, sys, urllib.request, urllib.error
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_mision_avanzado'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'
TOKEN = os.environ['WAVE_GEN_TOKEN'].strip()
error = False
import re
def _limpiar(x):
    """Saca el prefijo "Relámpago." de los enunciados (el modo ya se ve por el cronómetro, no va en el texto)."""
    if isinstance(x, dict):
        return {k: (re.sub(r'^\s*Rel[aá]mpago[\.:!]?\s+', '', v) if k == 'p' and isinstance(v, str) else _limpiar(v)) for k, v in x.items()}
    if isinstance(x, list): return [_limpiar(i) for i in x]
    return x

for ruta in sys.argv[1:]:
    M = _limpiar(json.load(open(ruta, encoding='utf-8')))
    req = urllib.request.Request(URL, data=json.dumps({'p_token': TOKEN, 'p': M}).encode(), method='POST',
                                 headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: print(ruta, ':', r.read().decode())
    except urllib.error.HTTPError as e:
        error = True; print(ruta, ': ERROR', e.read().decode()[:400])
sys.exit(1 if error else 0)
