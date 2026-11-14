// Arma el HTML completo de un juego a partir de un spec JSON: node construir.mjs specs/xxx.json salida.html
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const dir = path.dirname(fileURLToPath(import.meta.url));
export function motorCss() { return fs.readFileSync(path.join(dir, 'base.css'), 'utf8') + '\n' + fs.readFileSync(path.join(dir, 'extra.css'), 'utf8'); }
export function motorJs() { return fs.readFileSync(path.join(dir, 'motor.js'), 'utf8'); }
export function construir(spec) {
  const json = JSON.stringify(spec).replace(/</g, '\\u003c').split(String.fromCharCode(0x2028)).join('\\u2028').split(String.fromCharCode(0x2029)).join('\\u2029');
  const titulo = String(spec.titulo || 'Actividad').replace(/[<>&"]/g, '');
  return `<!doctype html>\n<html lang="es"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>${titulo}</title>\n<style>\n${motorCss()}</style>\n</head><body><div id="app"></div>\n<script>window.SPEC=${json};</script>\n<script>\n${motorJs()}</script></body></html>\n`;
}
if (process.argv[1] && process.argv[1].endsWith('construir.mjs') && process.argv[2]) {
  const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  fs.writeFileSync(process.argv[3], construir(spec));
  console.log('listo', process.argv[3], fs.statSync(process.argv[3]).size, 'bytes');
}
