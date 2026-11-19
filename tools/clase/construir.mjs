// Arma el HTML de una clase animada (un solo archivo) a partir del guion: node tools/clase/construir.mjs clase.json salida.html
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const dir = path.dirname(fileURLToPath(import.meta.url));
export function construir(clase) {
  const json = JSON.stringify(clase).replace(/</g, '\\u003c').split('\u2028').join('\\u2028').split('\u2029').join('\\u2029');
  const titulo = String(clase.titulo || 'Clase').replace(/[<>&"]/g, '');
  return `<!doctype html>\n<html lang="es"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>${titulo}</title>\n<style>\n${fs.readFileSync(path.join(dir, 'clase.css'), 'utf8')}</style>\n</head><body><div id="app"></div>\n<script>window.CLASE=${json};</script>\n<script>\n${fs.readFileSync(path.join(dir, 'clase.js'), 'utf8')}</script></body></html>\n`;
}
if (process.argv[1]?.endsWith('construir.mjs') && process.argv[2]) {
  fs.writeFileSync(process.argv[3], construir(JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))));
  console.log('listo', process.argv[3]);
}
