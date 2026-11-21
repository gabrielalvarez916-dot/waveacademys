# -*- coding: utf-8 -*-
"""MÁQUINA DEL NIVEL MEDIO · arma los PDF de una misión desde el repo (contenido/medio/.../mision-N.json) y los sube
a sus lecciones con la función pdf-medio (separada de fabrica-pdf, que es del Avanzado). Nunca publica.
Lo ejecuta .github/workflows/mision-medio.yml. Variables: MEDIO_TOKEN (secreto).
Uso: python tools/medio/pdf/generar.py contenido/medio/matematica-1/mision-1/mision-1.json [...]"""
import os, sys, json, base64, tempfile, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_leccion import render
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tools/medio
from neutro_medio import convertir, argentino
from primeros_anios import es_medio

URL = os.environ.get("MEDIO_FN_URL", "https://ndglmonqpqpfgeoxatcb.supabase.co/functions/v1/pdf-medio")
TOKEN = os.environ["MEDIO_TOKEN"].strip()

def llamar(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST", headers={"content-type": "application/json", "x-medio-token": TOKEN})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read())
        except Exception: return e.code, {"error": str(e)}

def pdf_de(meta, contenido):
    with tempfile.TemporaryDirectory() as tmp:
        e, s = os.path.join(tmp, "e.json"), os.path.join(tmp, "s.pdf")
        json.dump({"meta": meta, "contenido": contenido}, open(e, "w", encoding="utf8")); render(e, s)
        return open(s, "rb").read()

def mision(ruta):
    M = json.load(open(ruta, encoding="utf-8")); fallos = subir(M, M["niveles"], False)
    if isinstance(M.get("alternativa"), dict):  # ALTERNATIVA: la misión par para alumnos de otros países (todo en neutro)
        fallos += subir(M, M["alternativa"].get("niveles") or {}, True)
    return fallos

def subir(M, niveles, internacional):
    fallos = 0
    st, res = llamar({"action": "lecciones", "subject_id": M["subject_id"], "tema": M["tema"], "internacional": internacional})
    if st != 200: print("No se pudieron pedir las lecciones" + (" (par internacional)" if internacional else "") + ":", st, res); return 1
    for L in res["lecciones"]:
        n = str(L["nivel"]); c = niveles.get(n)
        if not c: continue
        if not es_medio(L["materia"]): print("SALTEO (no es del Nivel Medio):", L["materia"]); continue
        if L["publicada"]: print("SALTEO (publicada):", L["titulo"]); continue
        meta = {k: L[k] for k in ("materia", "anio", "tema_num", "tema", "leccion_num", "titulo")}
        for neutro in (False, True):
            cont = convertir(c) if (neutro or internacional) else argentino(c)
            nombre = f"{L['materia']} · Lección {L['leccion_num']} · {L['titulo']}" + (" (neutro)" if neutro else "") + (" [internacional]" if internacional else "")
            try:
                pdf = pdf_de({**meta, **({"neutro": True} if (neutro or internacional) else {})}, cont)
                st, r = llamar({"action": "subir", "lesson_id": L["lesson_id"], "pdf_base64": base64.b64encode(pdf).decode(), "contenido": cont, "neutro": neutro})
                if st == 200 and r.get("ok"): print("OK  ", nombre, f"({len(pdf)//1024} KB)", r.get("carpeta", ""))
                else: fallos += 1; print("FALLO", nombre, st, r)
            except Exception as e:
                fallos += 1; print("FALLO", nombre, repr(e))
    return fallos

if __name__ == "__main__":
    sys.exit(1 if sum(mision(r) for r in sys.argv[1:]) else 0)
