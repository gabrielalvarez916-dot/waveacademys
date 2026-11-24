// Pruebas del motor sin navegador: node probar.mjs archivo.html [...]  (necesita jsdom: npm i jsdom en una carpeta aparte y NODE_PATH)
import fs from 'node:fs';
import { createRequire } from 'node:module';
const require = createRequire(process.env.JSDOM_DIR ? process.env.JSDOM_DIR + '/' : import.meta.url);
const { JSDOM } = require('jsdom');
const esperar = (ms) => new Promise((r) => setTimeout(r, ms));
const limpio = (t) => String(t).replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();

async function correr(archivo, modo) {
  const errores = [];
  const dom = new JSDOM(fs.readFileSync(archivo, 'utf8'), { runScripts: 'dangerously', pretendToBeVisual: true, url: 'http://localhost/' });
  const w = dom.window; let resultado = null;
  w.addEventListener('error', (e) => errores.push(String(e.message)));
  w.addEventListener('message', (e) => { if (e.data && e.data.tipo === 'wave-resultado') resultado = e.data.puntaje; });
  const d = w.document, spec = w.SPEC;
  const btns = (sel) => [...d.querySelectorAll(sel)].filter((b) => !b.disabled);
  const click = (el) => { if (!el) throw new Error('no encontré el botón'); el.dispatchEvent(new w.MouseEvent('click', { bubbles: true })); };
  const porTexto = (sel, t) => btns(sel).find((b) => limpio(b.textContent) === limpio(t)) || btns(sel).find((b) => limpio(b.textContent).includes(limpio(t)));
  const seguir = () => { const f = d.querySelector('#fb.ver .btn'); if (f) click(f); };
  const grande = () => d.querySelector('.escena .btn');

  async function oraculo(A) {
    const t = A.t, comprobar = () => click(d.getElementById('ok'));
    if (t === 'op') { click(porTexto('.op', A.ops[A.ok])); if (!A.seg) comprobar(); }
    else if (t === 'vf') click(porTexto('.vf .op', A.ok ? 'Verdadero' : 'Falso'));
    else if (t === 'multi') { A.oks.forEach((i) => click(porTexto('.op', A.ops[i]))); comprobar(); }
    else if (t === 'armar') { const uni = A.union == null ? '' : A.union; String(A.sol).split(uni).forEach((p) => click(btns('.piezas .pz:not(.usada)').find((b) => limpio(b.textContent) === p))); comprobar(); }
    else if (t === 'ordenar') { A.items.forEach((x) => click(porTexto('.fila-ord', x))); comprobar(); }
    else if (t === 'unir') { for (const [a, b] of A.pares) { click(btns('[data-i]').find((x) => limpio(x.textContent) === limpio(a))); click(btns('[data-d]').find((x) => limpio(x.textContent) === limpio(b))); } comprobar(); }
    else if (t === 'arrastrar') { const L = ['centenas de mil', 'decenas de mil', 'unidades de mil', 'centenas', 'decenas', 'unidades']; const dd = L.length - 1 - L.indexOf(A.lugar); const z = A.num != null ? String(A.num).length - 1 - dd : L.indexOf(A.lugar); click(d.querySelector('[data-f]')); click(d.querySelector('[data-z="' + z + '"]')); }
    else if (t === 'clasificar') { for (const it of A.items) { click(btns('.suelto .chipi').find((x) => limpio(x.textContent) === limpio(it.t))); click(d.querySelector('[data-box="' + it.c + '"]')); } comprobar(); }
    else if (t === 'completar') { for (const s of A.sol) click(btns('.suelto .chipi').find((x) => limpio(x.textContent) === s && x.style.visibility !== 'hidden')); comprobar(); }
    else if (t === 'numero') { for (const ch of String(A.sol)) click(btns('.teclan .pz').find((b) => b.textContent === ch)); comprobar(); }
    else if (t === 'letras') { const inp = d.getElementById('pgin'); inp.value = w.WaveMotor.enLetras(parseInt(A.num, 10)); comprobar(); }
    else if (t === 'detective') { click(d.querySelector('[data-l="' + A.error + '"]')); comprobar(); }
    else if (t === 'recta') { const r = d.getElementById('rg'); r.value = A.sol; r.dispatchEvent(new w.Event('input', { bubbles: true })); comprobar(); }
    else if (t === 'comparar') { click(d.querySelector('[data-s="' + A.ok + '"]')); comprobar(); }
    else if (t === 'memoria') { for (const [a, b] of A.pares) { click(btns('[data-m]').find((x) => limpio(x.textContent) === limpio(a) && !x.classList.contains('ok'))); click(btns('[data-m]').find((x) => limpio(x.textContent) === limpio(b) && !x.classList.contains('ok'))); await esperar(320); } }
    else if (t === 'tachar') { click(d.querySelector('[data-c="' + (A.num.length - A.k) + '"]')); comprobar(); }
    else if (t === 'tabla') { String(A.num).padStart(9, '0').split('').forEach(() => 0); const n = String(A.num).length; for (let i = 9 - n; i < 9; i++) { click(d.querySelector('[data-s="' + i + '"]')); click(btns('.teclado .pz').find((b) => b.textContent === String(A.num)[i - (9 - n)])); } comprobar(); }
    else if (t === 'leer') { click(porTexto('.op', A.ops[A.ok])); comprobar(); }
    else if (t === 'perillas') { const dig = String(A.num).padStart(7, '0').split('').map(Number); dig.forEach((v, i) => { for (let k = 0; k < v; k++) click(d.querySelector('[data-u="' + i + '"]')); }); comprobar(); }
    else throw new Error('tipo sin prueba: ' + t);
    await esperar(5); seguir();
  }

  try {
    if (!d.querySelector('.tip')) click(grande()); // empezar (si ya está la placa del único desafío, no hace falta)
    if (modo === 'oraculo') {
      for (const ds of spec.desafios) { click(grande()); for (const A of ds.pasos) { await oraculo(A); await esperar(5); } if (!spec.continuo) click(grande()); }
    } else { // azar: toca botones cualquiera hasta terminar; solo busca errores de código
      for (let i = 0; i < 6000 && resultado == null; i++) {
        const f = d.querySelector('#fb.ver .btn'); if (f && Math.random() < .7) { click(f); continue; }
        const g = grande(); if (g && !g.disabled && d.querySelector('.etq') && !d.querySelector('[data-b]') && !d.querySelector('.ops,.pares,.cajas,.piezas,.teclan,.teclado,.recta,.memo,.perillas,.cifras,.hueco')) { click(g); continue; }
        const todos = btns('.escena button, .escena .hueco, .escena .caja').filter((b) => !(b.id === 'ok' && Math.random() < .2));
        if (!todos.length) break; click(todos[Math.floor(Math.random() * todos.length)]);
        if (d.querySelector('.memo')) await esperar(1);
        const r = d.getElementById('rg'); if (r) { r.value = String(Math.floor(Math.random() * 100)); r.dispatchEvent(new w.Event('input', { bubbles: true })); }
      }
    }
  } catch (e) { errores.push(e.message); }
  await esperar(50); w.close();
  return { resultado, errores };
}
let mal = 0;
for (const f of process.argv.slice(2)) {
  for (const modo of ['oraculo', 'azar']) {
    const r = await correr(f, modo);
    const ok = r.errores.length === 0 && (modo === 'azar' ? true : r.resultado === 100);
    if (!ok) mal++;
    console.log((ok ? 'OK  ' : 'MAL ') + f + ' [' + modo + '] resultado=' + r.resultado + (r.errores.length ? ' errores=' + JSON.stringify(r.errores.slice(0, 3)) : ''));
  }
}
process.exit(mal ? 1 : 0);
