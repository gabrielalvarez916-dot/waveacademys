# -*- coding: utf-8 -*-
"""MÁQUINA DEL NIVEL MEDIO. Carga en la plataforma las clases armadas (tools/medio/clase/dist/<slug>.html): en el paso de video del nivel (step_id)
o en la introducción de la materia (subject_id). Lo corre GitHub Actions después de grabar la voz.
Uso: python tools/medio/clase/cargar.py slug1 slug2 ...   (sin argumentos: las que cambiaron en dist según git)"""
import json, os, subprocess, sys, urllib.request

URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_clase_medio'  # función propia del Medio (solo acepta pasos del Nivel Medio)
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'  # clave pública (la misma de js/config.js)
TOKEN = os.environ['MEDIO_TOKEN'].strip()  # clave propia de la máquina del Medio (secreto de GitHub)
AQUI = os.path.dirname(os.path.abspath(__file__))

slugs = sys.argv[1:]
if not slugs:
    out = subprocess.run(['git', 'status', '--porcelain', '--', os.path.join(AQUI, 'dist')], capture_output=True, text=True).stdout
    slugs = [os.path.basename(l.split()[-1])[:-5] for l in out.splitlines() if l.strip().endswith('.html')]
def paso_video(d):
    body = json.dumps({'p_token': TOKEN, 'p_subject': d['subject_id'], 'p_tema': d['tema'], 'p_nivel': d['nivel'], 'p_internacional': bool(d.get('internacional'))}).encode()
    req = urllib.request.Request(URL.replace('cargar_clase_medio', 'paso_video_medio'), data=body, method='POST', headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())

error = False
for nombre in slugs:
    neutro = nombre.endswith('.neutro'); slug = nombre[:-7] if neutro else nombre
    lp = os.path.join(AQUI, 'lecciones', slug + '.json')
    if not os.path.exists(lp):
        continue
    L = json.load(open(lp, encoding='utf-8'))
    if L.get('destino') and not L.get('step_id'):  # {"subject_id", "tema", "nivel", "internacional"}: se busca el paso de video en la base
        L['step_id'] = paso_video(L['destino'])
        if not L['step_id']:
            print(nombre, ': AVISO todavía no existe la lección de destino (se carga en la próxima corrida)'); continue
    if not (L.get('step_id') or L.get('subject_id')):
        print(slug, ': sin step_id ni subject_id, no se carga'); continue
    html = open(os.path.join(AQUI, 'dist', nombre + '.html'), encoding='utf-8').read()
    if 'window.VOZ_AUDIO=' not in html:
        print(nombre, ': todavía sin voz, no se carga'); continue
    body = json.dumps({'p_token': TOKEN, 'p_html': html, 'p_step_id': L.get('step_id'), 'p_subject_id': L.get('subject_id'), 'p_neutro': neutro}).encode()
    req = urllib.request.Request(URL, data=body, method='POST', headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            print(nombre, ':', r.read().decode())
    except Exception as e:
        error = True; print(nombre, ': ERROR', getattr(e, 'read', lambda: b'')().decode()[:300] or e)
sys.exit(1 if error else 0)
