# -*- coding: utf-8 -*-
"""MÁQUINA · carga en los borradores la lección interactiva que armó tools/interactiva/armar.js (función cargar_leccion).
Uso: python tools/interactiva/cargar_leccion.py /tmp/lecciones.json"""
import json, os, sys, urllib.request, urllib.error
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_leccion'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'
TOKEN = os.environ['WAVE_GEN_TOKEN'].strip()
error = False
def escritas(rutas):
    """Arma la carga con las lecciones ESCRITAS EN SESIÓN (niveles.N.leccion) de cada misión. La máquina no inventa lecciones."""
    out = []
    for ruta in rutas:
        M = json.load(open(ruta, encoding='utf-8'))
        nv = lambda X: {n: v['leccion'] for n, v in (X.get('niveles') or {}).items() if isinstance(v, dict) and v.get('leccion')}
        p = {'subject_id': M['subject_id'], 'tema': M['tema'], 'niveles': nv(M)}
        if isinstance(M.get('alternativa'), dict) and nv(M['alternativa']): p['alternativa'] = {'niveles': nv(M['alternativa'])}
        if p['niveles']: out.append(p)
        else: print(ruta, ': sin lección escrita (queda el PDF)')
    return out
carga = escritas(sys.argv[1:]) if sys.argv[1].endswith('.json') and '/mision-' in sys.argv[1].replace('\\', '/') else json.load(open(sys.argv[1], encoding='utf-8'))
for p in carga:
    req = urllib.request.Request(URL, data=json.dumps({'p_token': TOKEN, 'p': p}).encode(), method='POST',
                                 headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: print('Misión', p['tema'], ':', r.read().decode())
    except urllib.error.HTTPError as e:
        error = True; print('Misión', p['tema'], ': ERROR', e.read().decode()[:300])
sys.exit(1 if error else 0)
