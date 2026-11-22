# Prueba: cómo dice la voz de primeros años cada forma de escribir un sonido (sss, mmm…). Mide duración, parte con voz (vocales) y transcribe.
import asyncio, edge_tts, subprocess, numpy as np, json, sys
from faster_whisper import WhisperModel
CAND = sys.argv[1:] or ["sss", "ssss", "ssssss", "Sss.", "¡Sss!", "Shhh", "Sssh", "Psss", "s", "mmm", "Mmm", "¡Mmm!", "Mmmm.", "lll", "Lll.", "nnn", "Nnn.", "fff", "Fff.", "Ffff"]
V, R, P = 'es-AR-ElenaNeural', '-8%', '+6Hz'
async def gen(t, f):
    await edge_tts.Communicate(t, V, rate=R, pitch=P).save(f)
def analiza(f):
    raw = subprocess.run(['ffmpeg', '-v', 'quiet', '-i', f, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    fr = 400; n = len(x) // fr; act = 0; voz = 0
    for i in range(n):
        s = x[i*fr:(i+1)*fr]; e = (s**2).mean()
        if e < 1e-4: continue
        act += 1; s = s - s.mean(); ac = np.correlate(s, s, 'full')[fr-1:]; ac /= ac[0] + 1e-9
        if ac[40:320].max() > .5: voz += 1   # periodicidad = voz (vocal o m/n/l); un siseo no es periódico
    return round(act * fr / 16000, 2), round(voz / max(act, 1), 2)
async def main():
    m = WhisperModel('small', compute_type='int8')
    for i, t in enumerate(CAND):
        f = f'/tmp/c{i}.mp3'; await gen(t, f); d, vr = analiza(f)
        seg, _ = m.transcribe(f, language='es'); tx = ' '.join(s.text for s in seg).strip()
        print(json.dumps({'texto': t, 'seg_con_sonido': d, 'parte_con_voz': vr, 'whisper': tx}, ensure_ascii=False))
asyncio.run(main())
