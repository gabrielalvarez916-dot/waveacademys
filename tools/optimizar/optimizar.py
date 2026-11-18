# -*- coding: utf-8 -*-
"""Optimiza para internet los videos MP4 cargados en la plataforma: mueve el índice del archivo al principio
(ffmpeg -c copy -movflags +faststart). NO recodifica, así que no pierde calidad y tarda segundos por video.
Lo ejecuta GitHub Actions (.github/workflows/optimizar-videos.yml) cuando el admin toca "Optimizar videos".
Variables: WAVE_GEN_TOKEN (secreto), WAVE_FN_URL (opcional)."""
import os, sys, json, struct, subprocess, tempfile, urllib.request, urllib.error

URL = os.environ.get("WAVE_FN_URL", "https://ndglmonqpqpfgeoxatcb.supabase.co/functions/v1/optimizar-videos")
TOKEN = os.environ["WAVE_GEN_TOKEN"].strip()
VUELTAS = 20  # hasta 10 videos por vuelta
EXT_OK = (".mp4", ".m4v", ".mov")

def llamar(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"content-type": "application/json", "x-gen-token": TOKEN})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read())
        except Exception: return e.code, {"error": str(e)}

def sh(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)

def indice_al_principio(url):
    """True si el 'moov' está antes que el 'mdat' (ya está optimizado). Lee solo el principio del archivo con pedidos por rango."""
    pos = 0
    for _ in range(40):
        r = subprocess.run(["curl", "-fsS", "-r", f"{pos}-{pos + 15}", url], capture_output=True)
        if r.returncode != 0 or len(r.stdout) < 8:
            return None
        tam = struct.unpack(">I", r.stdout[:4])[0]; tipo = r.stdout[4:8].decode("latin1")
        if tam == 1:
            if len(r.stdout) < 16: return None
            tam = struct.unpack(">Q", r.stdout[8:16])[0]
        if tipo == "moov": return True
        if tipo == "mdat": return False
        if tam < 8: return None
        pos += tam
    return None

def dur(ruta):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", ruta]).stdout.strip() or 0)

def procesar(v, tmp):
    key = v["key"]
    if not key.lower().endswith(EXT_OK):
        return "omitido", "Formato que no necesita este paso"
    ya = indice_al_principio(v["get_url"])
    if ya:
        return "ok", "Ya estaba optimizado"
    orig = os.path.join(tmp, "orig.mp4"); sal = os.path.join(tmp, "web.mp4")
    print("  bajando…", flush=True)
    sh(["curl", "-fsSL", "--retry", "3", "-o", orig, v["get_url"]])
    sh(["ffmpeg", "-y", "-v", "error", "-i", orig, "-c", "copy", "-movflags", "+faststart", sal])
    d0, d1 = dur(orig), dur(sal)
    if d1 < 1 or abs(d0 - d1) > 1.0:
        raise RuntimeError(f"El resultado no coincide (duración {d0:.1f}s -> {d1:.1f}s); no se reemplazó")
    if indice_al_principio_local(sal) is not True:
        raise RuntimeError("El resultado quedó sin optimizar; no se reemplazó")
    print(f"  subiendo ({os.path.getsize(sal) // 1048576} MB)…", flush=True)
    sh(["curl", "-fsS", "--retry", "3", "-X", "PUT", "-H", "content-type: video/mp4", "-T", sal, v["put_url"]])
    return "optimizado", f"{int(d1)} s"

def indice_al_principio_local(ruta):
    with open(ruta, "rb") as f:
        pos = 0
        for _ in range(40):
            f.seek(pos); h = f.read(16)
            if len(h) < 8: return None
            tam = struct.unpack(">I", h[:4])[0]; tipo = h[4:8].decode("latin1")
            if tam == 1: tam = struct.unpack(">Q", h[8:16])[0]
            if tipo == "moov": return True
            if tipo == "mdat": return False
            if tam < 8: return None
            pos += tam
    return None

def main():
    opt = ok = err = 0
    for _ in range(VUELTAS):
        st, res = llamar({"action": "lote"})
        if st != 200:
            print("No se pudo pedir el lote:", st, res); sys.exit(1)
        lote = res.get("lote") or []
        if not lote: break
        for v in lote:
            print(f"Video {v['key']}", flush=True)
            try:
                with tempfile.TemporaryDirectory() as tmp:
                    estado, nota = procesar(v, tmp)
                llamar({"action": "listo", "key": v["key"], "estado": estado, "nota": nota})
                if estado == "optimizado": opt += 1
                else: ok += 1
                print(f"  {estado}: {nota}")
            except Exception as e:
                err += 1; msg = (getattr(e, "stderr", None) or str(e))[-300:]
                print("  ERROR:", msg)
                llamar({"action": "listo", "key": v["key"], "estado": "error", "nota": msg})
    print(f"Optimizados: {opt}. Ya estaban bien u omitidos: {ok}. Con error: {err}.")
    if err and not (opt or ok): sys.exit(1)

if __name__ == "__main__":
    main()
