# -*- coding: utf-8 -*-
"""Transcribe los videos de cada misión (sin IA paga) y guarda el texto en video_transcripciones.
Archivos propios: faster-whisper (modelo small, CPU). YouTube: subtítulos con yt-dlp.
Si el paso tiene video final, se transcribe ese; si no, cada video con sus cortes.
Lo ejecuta GitHub Actions (.github/workflows/transcribir.yml). Variable: WAVE_GEN_TOKEN."""
import os, sys, re, json, glob, subprocess, tempfile, urllib.request, urllib.error

URL = os.environ.get("WAVE_FN_URL", "https://ndglmonqpqpfgeoxatcb.supabase.co/functions/v1/optimizar-videos")
TOKEN = os.environ["WAVE_GEN_TOKEN"].strip()
_modelo = None

def llamar(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"content-type": "application/json", "x-gen-token": TOKEN})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read())
        except Exception: return e.code, {"error": str(e)}

def sh(cmd): return subprocess.run(cmd, check=True, capture_output=True, text=True)

def modelo():
    global _modelo
    if _modelo is None:
        from faster_whisper import WhisperModel
        _modelo = WhisperModel("small", device="cpu", compute_type="int8")
    return _modelo

def whisper(wav):
    segs, _ = modelo().transcribe(wav, language="es", beam_size=1, vad_filter=True)
    return " ".join(s.text.strip() for s in segs)

def tramos_de(t):
    return [(float(x.get("i") or 0), float(x.get("f") or 0)) for x in (t or [])] or [(0.0, 0.0)]

def de_archivo(parte, tmp, k):
    src = os.path.join(tmp, f"v{k}.bin")
    sh(["curl", "-fsSL", "--retry", "3", "-o", src, parte["url"]])
    textos = []
    for j, (i, f) in enumerate(tramos_de(parte.get("tramos"))):
        wav = os.path.join(tmp, f"a{k}_{j}.wav")
        cmd = ["ffmpeg", "-y", "-v", "error"] + (["-ss", str(i)] if i > 0 else []) + ["-i", src]
        if f > i: cmd += ["-t", str(f - i)]
        sh(cmd + ["-vn", "-ac", "1", "-ar", "16000", wav])
        textos.append(whisper(wav))
    return " ".join(textos)

def de_youtube(parte, tmp, k):
    base = os.path.join(tmp, f"yt{k}")
    sh(["yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs", "--sub-langs", "es.*,es", "--sub-format", "vtt",
        "-o", base, f"https://www.youtube.com/watch?v={parte['yt']}"])
    vtts = glob.glob(base + "*.vtt")
    if not vtts: raise RuntimeError("YouTube no dio subtítulos en español para este video")
    lineas, previa = [], ""
    for l in open(vtts[0], encoding="utf8"):
        l = re.sub(r"<[^>]+>", "", l).strip()
        if not l or "-->" in l or l.startswith(("WEBVTT", "Kind:", "Language:")) or l == previa: continue
        lineas.append(l); previa = l
    return " ".join(lineas)

def main():
    hechos = fallos = 0
    for _ in range(40):
        st, res = llamar({"action": "trans_lote"})
        if st != 200: print("No se pudo pedir el lote:", st, res); sys.exit(1)
        lote = res.get("lote") or []
        if not lote: break
        for t in lote:
            print("Paso", t["step_id"], flush=True)
            try:
                with tempfile.TemporaryDirectory() as tmp:
                    textos = [de_youtube(p, tmp, k) if p.get("yt") else de_archivo(p, tmp, k) for k, p in enumerate(t["partes"])]
                texto = "\n\n".join(x for x in textos if x.strip())
                llamar({"action": "trans_listo", "step_id": t["step_id"], "lesson_id": t["lesson_id"], "firma": t["firma"], "estado": "ok", "texto": texto,
                        "nota": f"{len(texto.split())} palabras"})
                hechos += 1; print("  listo ✔", len(texto.split()), "palabras", flush=True)
            except Exception as e:
                fallos += 1; msg = getattr(e, "stderr", None) or str(e)
                print("  ERROR:", msg[-300:], flush=True)
                llamar({"action": "trans_listo", "step_id": t["step_id"], "lesson_id": t["lesson_id"], "firma": t["firma"], "estado": "error", "texto": "", "nota": msg[-400:]})
    print(f"Transcripciones: {hechos} listas, {fallos} con error.")

if __name__ == "__main__":
    main()
