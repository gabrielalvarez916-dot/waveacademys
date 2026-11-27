# -*- coding: utf-8 -*-
"""Carga la carpeta de cada nivel (consignas que ve el alumno + clave de corrección) directo desde el archivo de la misión.
Desde el 26/11/2026 el PDF ya no se arma, así que la carpeta no puede depender de él. Lo corren mision-avanzado.yml y mision-medio.yml.
Uso: python tools/cargar_carpeta.py contenido/.../mision-N.json [...]   (token: WAVE_GEN_TOKEN o MEDIO_TOKEN)"""
import json, os, subprocess, sys, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from neutro import convertir
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_carpetas'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'
TOKEN = (os.environ.get('WAVE_GEN_TOKEN') or os.environ.get('MEDIO_TOKEN') or '').strip()
AQUI = os.path.dirname(os.path.abspath(__file__))


def errores_carpeta(ruta):
    """Solo las reglas de carpeta de control_calidad: si la carpeta no cumple, no se carga (el resto de la misión se controla aparte)."""
    out = subprocess.run([sys.executable, os.path.join(AQUI, 'control_calidad.py'), ruta], capture_output=True, text=True).stdout
    return [l.strip() for l in out.splitlines() if l.strip().startswith('- ') and 'carpeta' in l]


error = False
for ruta in sys.argv[1:]:
    M = json.load(open(ruta, encoding='utf-8'))
    malos = errores_carpeta(ruta)
    if malos:
        error = True; print(ruta, ': la carpeta NO se carga:'); [print('   ', m) for m in malos]; continue
    niv = {}
    for k, N in (M.get('niveles') or {}).items():
        cons = [str(c if isinstance(c, str) else (c or {}).get('consigna', '')) for c in (N.get('carpeta') or [])]
        if not cons: continue
        niv[k] = {'carpeta': cons, 'carpeta_neutro': [str(x) for x in convertir(cons)], 'respuestas_carpeta': N.get('respuestas_carpeta') or [],
                  'soluciones': {'carpeta': (N.get('soluciones') or {}).get('carpeta') or []}}
    if not niv: continue
    p = {'subject_id': M.get('subject_id'), 'tema': M.get('tema'), 'niveles': niv}
    if 'libro' in M: p['libro'] = M['libro']
    req = urllib.request.Request(URL, data=json.dumps({'p_token': TOKEN, 'p': p}).encode(), method='POST',
                                 headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: print(ruta, ':', r.read().decode())
    except urllib.error.HTTPError as e:
        error = True; print(ruta, ': ERROR', e.read().decode()[:300])
sys.exit(1 if error else 0)
