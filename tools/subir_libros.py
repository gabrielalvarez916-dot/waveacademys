# -*- coding: utf-8 -*-
"""Sube el PDF del libro de cada misión al nivel «Libro: …» (función subir-libro). 27/11/2026.
La misión lo declara en "libro": {"titulo": ..., "pdf": "libros/<archivo>.pdf", "act": [...]}.
Uso: python tools/subir_libros.py [libros/x.pdf ...]   (sin argumentos: todos los libros declarados). Token: WAVE_GEN_TOKEN."""
import base64, glob, json, os, sys, urllib.request, urllib.error
URL = 'https://ndglmonqpqpfgeoxatcb.supabase.co/functions/v1/subir-libro'
TOKEN = (os.environ.get('WAVE_GEN_TOKEN') or '').strip()
pedidos = set(sys.argv[1:])
error = False
for f in sorted(glob.glob('contenido/*/mision-*/mision-*.json')):
    M = json.load(open(f, encoding='utf-8'))
    pdf = (M.get('libro') or {}).get('pdf')
    if not pdf or (pedidos and pdf not in pedidos): continue
    if not os.path.exists(pdf): error = True; print(f, ': falta el archivo', pdf); continue
    body = json.dumps({'subject_id': M['subject_id'], 'tema': M['tema'], 'pdf_base64': base64.b64encode(open(pdf, 'rb').read()).decode()}).encode()
    req = urllib.request.Request(URL, data=body, method='POST', headers={'x-gen-token': TOKEN, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=180) as r: print(f, ':', r.read().decode())
    except urllib.error.HTTPError as e:
        error = True; print(f, ': ERROR', e.code, e.read().decode()[:300])
sys.exit(1 if error else 0)
