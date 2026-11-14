# -*- coding: utf-8 -*-
"""Arma el PDF de cada borrador de lección que ya está listo y lo carga en la lección (sin publicar).
Lo ejecuta GitHub Actions (.github/workflows/pdfs-lecciones.yml). Variables: WAVE_GEN_TOKEN (secreto), WAVE_FN_URL (opcional)."""
import os, sys, json, base64, tempfile, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_leccion import render

URL = os.environ.get("WAVE_FN_URL", "https://ndglmonqpqpfgeoxatcb.supabase.co/functions/v1/fabrica-pdf")
TOKEN = os.environ["WAVE_GEN_TOKEN"].strip()

def llamar(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"content-type": "application/json", "x-gen-token": TOKEN})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read())
        except Exception: return e.code, {"error": str(e)}

def main():
    st, res = llamar({"action": "pendientes"})
    if st != 200:
        print("No se pudo pedir los pendientes:", st, res); sys.exit(1)
    pend = res.get("pendientes", [])
    print(f"{len(pend)} borrador(es) sin PDF")
    fallos = 0
    for p in pend:
        m = p["meta"]; nombre = f"{m['materia']} · Lección {m['leccion_num']} · {m['titulo']}"
        try:
            with tempfile.TemporaryDirectory() as tmp:
                entrada = os.path.join(tmp, "e.json"); salida = os.path.join(tmp, "s.pdf")
                json.dump({"meta": m, "contenido": p["contenido"]}, open(entrada, "w", encoding="utf8"))
                render(entrada, salida)
                pdf = open(salida, "rb").read()
            st, r = llamar({"action": "subir", "draft_id": p["draft_id"], "pdf_base64": base64.b64encode(pdf).decode()})
            if st == 200 and r.get("ok"): print("OK  ", nombre, f"({len(pdf)//1024} KB)")
            else: fallos += 1; print("FALLO", nombre, st, r)
        except Exception as e:
            fallos += 1; print("FALLO", nombre, repr(e))
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
