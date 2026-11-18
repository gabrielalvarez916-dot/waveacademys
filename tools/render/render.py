# -*- coding: utf-8 -*-
"""Une los cortes y la intro de cada pedido de video final en UN solo MP4 (listo para internet) y lo carga en la lección.
Lo ejecuta GitHub Actions (.github/workflows/render-videos.yml). Variables: WAVE_GEN_TOKEN (secreto), WAVE_FN_URL (opcional)."""
import os, sys, json, subprocess, tempfile, urllib.request, urllib.error

URL = os.environ.get("WAVE_FN_URL", "https://ndglmonqpqpfgeoxatcb.supabase.co/functions/v1/render-videos")
TOKEN = os.environ["WAVE_GEN_TOKEN"].strip()
MAX_POR_VUELTA = 25

def llamar(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"content-type": "application/json", "x-gen-token": TOKEN})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read())
        except Exception: return e.code, {"error": str(e)}

def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)

def sonda(ruta):
    j = json.loads(sh(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", ruta]).stdout)
    v = next((s for s in j["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in j["streams"] if s["codec_type"] == "audio"), None)
    return {"alto": int(v["height"]) if v else 0, "audio": a is not None, "dur": float(j["format"].get("duration") or 0)}

FUNDIDO = 0.5  # segundos de fundido cruzado entre partes (imagen y sonido)

def unir_con_fundido(listado, final):
    """Une las partes con un fundido cruzado corto para que no se note el corte.
    Devuelve False si no se puede (una sola parte, partes muy cortas o error): entonces se pegan sin transición."""
    if len(listado) < 2: return False
    durs = [sonda(r)["dur"] for r in listado]
    if any(d < 2 * FUNDIDO + 0.3 for d in durs): return False
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for r in listado: cmd += ["-i", r]
    f, v, a, acum = [], "[0:v]", "[0:a]", durs[0]
    for k in range(1, len(listado)):
        off = acum - FUNDIDO * k
        f.append(f"{v}[{k}:v]xfade=transition=fade:duration={FUNDIDO}:offset={off:.3f}[v{k}]")
        f.append(f"{a}[{k}:a]acrossfade=d={FUNDIDO}:c1=tri:c2=tri[a{k}]")
        v, a, acum = f"[v{k}]", f"[a{k}]", acum + durs[k]
    cmd += ["-filter_complex", ";".join(f), "-map", v, "-map", a,
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart", final]
    print("  uniendo con fundidos…", flush=True)
    try:
        sh(cmd); return True
    except subprocess.CalledProcessError as e:
        print("  (no se pudo hacer el fundido, se unen sin transición)", (e.stderr or "")[-300:], flush=True)
        return False

def procesar(p, tmp):
    partes = []
    for k, parte in enumerate(p["plan"]):
        ruta = os.path.join(tmp, f"src{k}.bin")
        print(f"  bajando parte {k + 1} de {len(p['plan'])}…", flush=True)
        sh(["curl", "-fsSL", "--retry", "3", "-o", ruta, parte["url"]])
        partes.append({"ruta": ruta, "i": float(parte.get("i") or 0), "f": float(parte.get("f") or 0), **sonda(ruta)})
    alto = max(2, min(1080, max(x["alto"] for x in partes) or 720))
    alto -= alto % 2
    ancho = int(round(alto * 16 / 9)); ancho -= ancho % 2
    vf = (f"scale={ancho}:{alto}:force_original_aspect_ratio=decrease,pad={ancho}:{alto}:(ow-iw)/2:(oh-ih)/2:black,"
          "setsar=1,fps=30,format=yuv420p")
    listado = []
    for k, x in enumerate(partes):
        sal = os.path.join(tmp, f"p{k}.mp4")
        cmd = ["ffmpeg", "-y", "-v", "error"]
        if x["i"] > 0: cmd += ["-ss", str(x["i"])]
        cmd += ["-i", x["ruta"]]
        if not x["audio"]: cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        if x["f"] > x["i"]: cmd += ["-t", str(x["f"] - x["i"])]
        cmd += ["-map", "0:v:0", "-map", "0:a:0" if x["audio"] else "1:a:0", "-vf", vf,
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2"]
        if not x["audio"]: cmd += ["-shortest"]
        cmd += [sal]
        print(f"  procesando parte {k + 1} de {len(partes)}…", flush=True)
        sh(cmd)
        listado.append(sal)
    final = os.path.join(tmp, "final.mp4")
    if not unir_con_fundido(listado, final):
        lista = os.path.join(tmp, "lista.txt")
        with open(lista, "w") as fh:
            fh.write("".join(f"file '{r}'\n" for r in listado))
        sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", "-movflags", "+faststart", final])
    dur = sonda(final)["dur"]
    if dur < 1: raise RuntimeError("El video final salió vacío")
    print(f"  subiendo el video final ({os.path.getsize(final) // 1048576} MB, {int(dur)} s)…", flush=True)
    sh(["curl", "-fsS", "--retry", "3", "-X", "PUT", "-H", "content-type: video/mp4", "-T", final, p["put_url"]])

def main():
    hechos = fallos = 0
    for _ in range(MAX_POR_VUELTA):
        st, res = llamar({"action": "siguiente"})
        if st != 200:
            print("No se pudo pedir el siguiente:", st, res); sys.exit(1)
        p = res.get("pedido")
        if not p:
            if res.get("saltado"): print("Un pedido tenía partes de YouTube y se marcó con error."); continue
            break
        print(f"Pedido {p['id']}", flush=True)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                procesar(p, tmp)
            st, r2 = llamar({"action": "listo", "id": p["id"]})
            if st != 200: raise RuntimeError(f"No se pudo cerrar el pedido: {r2}")
            hechos += 1; print("  listo ✔")
        except subprocess.CalledProcessError as e:
            fallos += 1; msg = (e.stderr or str(e))[-400:]; print("  ERROR:", msg)
            llamar({"action": "error", "id": p["id"], "error": msg})
        except Exception as e:
            fallos += 1; print("  ERROR:", e); llamar({"action": "error", "id": p["id"], "error": str(e)})
    print(f"Videos finales generados: {hechos}. Con error: {fallos}.")
    if fallos and not hechos: sys.exit(1)

if __name__ == "__main__":
    main()
