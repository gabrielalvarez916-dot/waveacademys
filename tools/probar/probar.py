# -*- coding: utf-8 -*-
"""PRUEBA (no toca la plataforma ni sube nada): ¿se puede bajar un video de YouTube desde GitHub, transcribirlo gratis
y detectar en CUALQUIER parte las frases que sobran (suscribite, like, campanita, patrocinadores…)?
Imprime un informe en el log y en el resumen de la ejecución."""
import os, re, sys, json, time, subprocess

VID = sys.argv[1]
OUT = "/tmp/prueba"; os.makedirs(OUT, exist_ok=True)
resumen = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); resumen.append(s)

def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

# 1) bajar el video (baja calidad: es solo una prueba)
t0 = time.time()
r = sh(["yt-dlp", "-f", "worstvideo[height>=360]+bestaudio/best[height<=480]/best", "--merge-output-format", "mp4",
        "-o", f"{OUT}/v.%(ext)s", "--no-playlist", f"https://www.youtube.com/watch?v={VID}"])
archivos = [f for f in os.listdir(OUT) if f.startswith("v.")]
if r.returncode != 0 or not archivos:
    p("## 1) DESCARGA: FALLÓ")
    p((r.stderr or r.stdout)[-600:])
    descarga_ok = False
else:
    descarga_ok = True
    p(f"## 1) DESCARGA: OK ({archivos[0]}, {os.path.getsize(os.path.join(OUT, archivos[0])) // 1048576} MB, {time.time() - t0:.0f} s)")

# 2) subtítulos de YouTube (alternativa rápida)
r2 = sh(["yt-dlp", "--skip-download", "--write-auto-subs", "--sub-langs", "es.*", "--sub-format", "json3", "-o", f"{OUT}/s", f"https://www.youtube.com/watch?v={VID}"])
subs = [f for f in os.listdir(OUT) if f.startswith("s.") and f.endswith(".json3")]
p("## 2) SUBTÍTULOS DE YOUTUBE:", "disponibles " + ",".join(subs) if subs else "no se pudieron bajar")

if not descarga_ok:
    open(os.environ.get("GITHUB_STEP_SUMMARY", "/dev/null"), "a").write("\n".join(resumen)); sys.exit(0)

# 3) transcribir con Whisper (gratis, corre acá)
from faster_whisper import WhisperModel
t1 = time.time()
audio = os.path.join(OUT, archivos[0])
modelo = WhisperModel("base", device="cpu", compute_type="int8")
segs, info = modelo.transcribe(audio, language="es", word_timestamps=True, vad_filter=True)
segs = list(segs)
dur = info.duration
p(f"## 3) TRANSCRIPCIÓN: OK (video de {dur:.0f} s, transcripción en {time.time() - t1:.0f} s con el modelo 'base')")

# 4) frases que sobran (en cualquier parte del video)
PAT = re.compile(r"suscrib|suscríb|subscrib|campanita|campana\b|dale (un )?like|deja(le)? (tu )?(like|me gusta)|me gusta\b.*(video|canal)|"
                 r"(en|a) (mi|el) canal|tu comentario|d[eé]jame (un )?comentario|comparte (el )?video|compártelo|"
                 r"link (en|de) la descripci[oó]n|enlace (en|de) la descripci[oó]n|patreon|instagram|facebook|tiktok|s[ií]gueme|"
                 r"patrocin|auspici|hasta (el )?pr[oó]ximo video|nos vemos en (el )?pr[oó]ximo", re.I)
def mm(s): return f"{int(s // 60)}:{int(s % 60):02d}"
cortes = []
for s in segs:
    if PAT.search(s.text):
        cortes.append((s.start, s.end, s.text.strip()))
p(f"## 4) FRASES QUE SOBRAN DETECTADAS: {len(cortes)}")
for a, b, t in cortes:
    p(f"- {mm(a)} a {mm(b)} ({b - a:.0f} s): «{t}»")
tot = sum(b - a for a, b, _ in cortes)
p(f"Total a cortar: {tot:.0f} s de {dur:.0f} s ({100 * tot / dur:.1f}%)")
p("\n## TRANSCRIPCIÓN COMPLETA (para comparar a ojo)")
for s in segs:
    p(f"[{mm(s.start)}] {s.text.strip()}")
open(os.environ.get("GITHUB_STEP_SUMMARY", "/dev/null"), "a").write("\n".join(resumen))
