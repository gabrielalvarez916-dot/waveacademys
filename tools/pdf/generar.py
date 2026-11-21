# -*- coding: utf-8 -*-
"""Arma el PDF de cada borrador de lección que ya está listo y lo carga en la lección (sin publicar).
Lo ejecuta GitHub Actions (.github/workflows/pdfs-lecciones.yml). Variables: WAVE_GEN_TOKEN (secreto), WAVE_FN_URL (opcional)."""
import os, sys, json, base64, tempfile, time, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_leccion import render
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from neutro import convertir, argentino

URL = os.environ.get("WAVE_FN_URL", "https://ndglmonqpqpfgeoxatcb.supabase.co/functions/v1/fabrica-pdf")
TOKEN = os.environ["WAVE_GEN_TOKEN"].strip()

def llamar(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"content-type": "application/json", "x-gen-token": TOKEN})
    ultimo = None
    for intento in range(4):  # si el servidor tarda o corta, se reintenta antes de rendirse
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            try: return e.code, json.loads(e.read())
            except Exception: return e.code, {"error": str(e)}
        except Exception as e:
            ultimo = e; print("  (reintento", intento + 1, "de la llamada", body.get("action"), ":", repr(e), ")")
            time.sleep(5 * (intento + 1))
    return 599, {"error": repr(ultimo)}

def armar_pdf(m, contenido, imagenes, tmp):
    entrada = os.path.join(tmp, "e.json"); salida = os.path.join(tmp, "s.pdf")
    for k, im in enumerate(imagenes or []):  # imágenes cargadas desde el admin
        try:
            blk = contenido["secciones"][im["sec"]]["bloques"][im["bloque"]]
            ext = ".jpg" if "jpeg" in (im.get("mime") or "") else ".png"
            ruta = os.path.join(tmp, f"img{k}{ext}")
            open(ruta, "wb").write(base64.b64decode(im["b64"]))
            blk["archivo"] = ruta
        except Exception as e:
            print("  (imagen no usada:", repr(e), ")")
    json.dump({"meta": m, "contenido": contenido}, open(entrada, "w", encoding="utf8"))
    render(entrada, salida)
    return open(salida, "rb").read()

def neutros():
    """Segundo PDF de cada lección, en español neutro (alumnos de otros países). También para lecciones ya publicadas."""
    hechos, fallos = [], 0
    while True:
        st, res = llamar({"action": "pendientes_neutro", "limite": 5, "excluir": hechos})
        pend = res.get("pendientes", []) if st == 200 else []
        if st != 200: print("No se pudo pedir los pendientes neutros:", st, res); return 1
        if not pend: break
        for p in pend:
            hechos.append(p["draft_id"])
            m = dict(p["meta"]); m["neutro"] = True; nombre = f"{m['materia']} · Lección {m['leccion_num']} · {m['titulo']} (neutro)"
            try:
                c = convertir(p["contenido"])
                with tempfile.TemporaryDirectory() as tmp:
                    pdf = armar_pdf(m, c, p.get("imagenes"), tmp)
                car = [str(x if isinstance(x, str) else (x or {}).get("consigna", "")) for x in (c.get("carpeta") or [])]
                st, r = llamar({"action": "subir_neutro", "draft_id": p["draft_id"], "pdf_base64": base64.b64encode(pdf).decode(), "carpeta": car})
                if st == 200 and r.get("ok"): print("OK  ", nombre, f"({len(pdf)//1024} KB)")
                else: fallos += 1; print("FALLO", nombre, st, r)
            except Exception as e:
                fallos += 1; print("FALLO", nombre, repr(e))
    return fallos

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
                contenido = argentino(p["contenido"])
                # imágenes cargadas desde el admin: se guardan como archivo y se enganchan al bloque de imagen que corresponde
                for k, im in enumerate(p.get("imagenes") or []):
                    try:
                        blk = contenido["secciones"][im["sec"]]["bloques"][im["bloque"]]
                        ext = ".jpg" if "jpeg" in (im.get("mime") or "") else ".png"
                        ruta = os.path.join(tmp, f"img{k}{ext}")
                        open(ruta, "wb").write(base64.b64decode(im["b64"]))
                        blk["archivo"] = ruta
                    except Exception as e:
                        print("  (imagen no usada:", repr(e), ")")
                json.dump({"meta": m, "contenido": contenido}, open(entrada, "w", encoding="utf8"))
                render(entrada, salida)
                pdf = open(salida, "rb").read()
            st, r = llamar({"action": "subir", "draft_id": p["draft_id"], "pdf_base64": base64.b64encode(pdf).decode()})
            if st == 200 and r.get("ok"): print("OK  ", nombre, f"({len(pdf)//1024} KB)")
            else: fallos += 1; print("FALLO", nombre, st, r)
        except Exception as e:
            fallos += 1; print("FALLO", nombre, repr(e))
    fallos += neutros()
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
