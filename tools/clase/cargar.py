# -*- coding: utf-8 -*-
"""Carga en la plataforma las clases armadas (tools/clase/dist/<slug>.html): en el paso de video del nivel (step_id)
o en la introducción de la materia (subject_id). Lo corre GitHub Actions después de grabar la voz.
Uso: python tools/clase/cargar.py slug1 slug2 ...   (sin argumentos: las que cambiaron en dist según git)"""
import json, os, subprocess, sys, urllib.request

URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/rest/v1/rpc/cargar_clase'
KEY = 'sb_publishable_POUL2SrzhGe2x-sqoGawYw_UrAk7As-'  # clave pública (la misma de js/config.js)
TOKEN = os.environ.get('CLASES_TOKEN') or 'wROjyAHXj1ixep8Qex5rLFXhsU0fcQ4C73x-ZcLyrJo'  # solo sirve para cargar clases
AQUI = os.path.dirname(os.path.abspath(__file__))

slugs = sys.argv[1:]
if not slugs:
    out = subprocess.run(['git', 'status', '--porcelain', '--', os.path.join(AQUI, 'dist')], capture_output=True, text=True).stdout
    slugs = [os.path.basename(l.split()[-1])[:-5] for l in out.splitlines() if l.strip().endswith('.html')]
error = False
for nombre in slugs:
    neutro = nombre.endswith('.neutro'); slug = nombre[:-7] if neutro else nombre
    lp = os.path.join(AQUI, 'lecciones', slug + '.json')
    if not os.path.exists(lp):
        continue
    L = json.load(open(lp, encoding='utf-8'))
    if not (L.get('step_id') or L.get('subject_id')):
        print(slug, ': sin step_id ni subject_id, no se carga'); continue
    html = open(os.path.join(AQUI, 'dist', nombre + '.html'), encoding='utf-8').read()
    if 'window.VOZ_AUDIO=' not in html:
        print(nombre, ': todavía sin voz, no se carga'); continue
    body = json.dumps({'p_token': TOKEN, 'p_html': html, 'p_step_id': L.get('step_id'), 'p_subject_id': L.get('subject_id'), 'p_neutro': neutro}).encode()
    req = urllib.request.Request(URL, data=body, method='POST', headers={'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    import time
    for intento in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                print(nombre, ':', r.read().decode())
            break
        except Exception as e:
            msg = getattr(e, 'read', lambda: b'')().decode()[:300] or str(e)
            if intento == 3:
                error = True; print(nombre, ': ERROR', msg)
            else:
                print(nombre, ': reintento', intento + 1, msg[:80]); time.sleep(8 * (intento + 1))
sys.exit(1 if error else 0)
