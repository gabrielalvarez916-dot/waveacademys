// Genera la voz de una clase con ElevenLabs (con tiempos exactos por palabra para los subtítulos).
// Guarda un mp3 por escena y NO vuelve a pedir las que ya tiene (si el texto no cambió): la cuota gratis rinde mes a mes.
// Si se acaba la cuota, corta prolijo: lo generado queda y el resto de las escenas usa la voz del dispositivo.
// Uso: ELEVEN_KEY=xxx [ELEVEN_VOZ=id] node tools/clase/voz.mjs clase.json carpeta-audio/
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const [, , specPath, dirAudio] = process.argv;
const KEY = process.env.ELEVEN_KEY, VOZ = process.env.ELEVEN_VOZ || 'pNInz6obpgDQGcFmaJgB', MODELO = process.env.ELEVEN_MODELO || 'eleven_multilingual_v2';
if (!KEY || !specPath || !dirAudio) { console.error('Uso: ELEVEN_KEY=xxx node voz.mjs clase.json carpeta-audio/'); process.exit(1); }
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
fs.mkdirSync(dirAudio, { recursive: true });
const rel = path.relative(path.dirname(specPath), dirAudio).split(path.sep).join('/') || '.';

let gastados = 0;
for (const e of spec.escenas) {
  const texto = e.voz.join(' '), hash = crypto.createHash('md5').update(VOZ + texto).digest('hex').slice(0, 10);
  const mp3 = path.join(dirAudio, e.id + '-' + hash + '.mp3'), tiempos = mp3.replace(/\.mp3$/, '.json');
  let al;
  if (fs.existsSync(mp3) && fs.existsSync(tiempos)) al = JSON.parse(fs.readFileSync(tiempos, 'utf8'));
  else {
    const r = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${VOZ}/with-timestamps`, {
      method: 'POST', headers: { 'xi-api-key': KEY, 'content-type': 'application/json' },
      body: JSON.stringify({ text: texto, model_id: MODELO })
    });
    if (!r.ok) { console.error(`Corté en ${e.id}: ElevenLabs respondió ${r.status} ${(await r.text()).slice(0, 200)}`); break; }
    const j = await r.json();
    fs.writeFileSync(mp3, Buffer.from(j.audio_base64, 'base64'));
    al = j.alignment; fs.writeFileSync(tiempos, JSON.stringify(al));
    gastados += texto.length;
  }
  // tiempos de inicio/fin de cada frase y de cada palabra dentro de ella
  const ini = al.character_start_times_seconds, fin = al.character_end_times_seconds, n = ini.length;
  let pos = 0;
  const frases = e.voz.map((f) => {
    const a = Math.min(pos, n - 1), b = Math.min(pos + f.length - 1, n - 1), w = [];
    let c = a; for (const pal of f.split(' ')) { w.push(+ini[Math.min(c, n - 1)].toFixed(3)); c += pal.length + 1; }
    pos += f.length + 1;
    return { t0: +ini[a].toFixed(3), t1: +fin[b].toFixed(3), w };
  });
  e.audio = { src: rel + '/' + path.basename(mp3), frases };
}
fs.writeFileSync(specPath, JSON.stringify(spec, null, 1));
const conVoz = spec.escenas.filter((e) => e.audio).length;
console.log(`listo: ${conVoz}/${spec.escenas.length} escenas con voz ElevenLabs · ${gastados} caracteres gastados en esta vuelta`);
