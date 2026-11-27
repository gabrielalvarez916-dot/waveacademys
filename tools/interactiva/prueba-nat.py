# -*- coding: utf-8 -*-
"""PRUEBA EN EL NAVEGADOR del banco de Naturales de la lección (js/leccion-banco-nat*.js), como lo ve el alumno.
- Ejemplos: recorre cada opción de cada selector y todos los pasos; falla si hay errores de JavaScript, NaN/undefined
  o algo que se sale del recuadro. Guarda una captura por paso en /tmp/prueba-nat/.
- Ejercicios: 6 rondas de «resolver → comprobar» (la respuesta correcta tiene que dar bien) y «Otro caso».
Uso: python3 tools/interactiva/prueba-nat.py [motor ...]   (sin argumentos prueba todos los de tools/interactiva/casos-nat.json)"""
import asyncio, json, pathlib, sys
from playwright.async_api import async_playwright
RAIZ = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = ['js/apoyos.js', 'js/leccion-banco.js', 'js/leccion-banco2.js', 'js/leccion-banco-nat.js', 'js/leccion-banco-nat2.js', 'js/leccion-banco-nat3.js', 'js/leccion-banco-soc.js', 'js/leccion-banco-soc2.js', 'js/leccion-banco-medio.js']
CSS = ['css/styles.css', 'css/apoyos.css']
OUT = pathlib.Path('/tmp/prueba-nat'); OUT.mkdir(exist_ok=True)

async def main():
    casos = json.loads((RAIZ / 'tools/interactiva/casos-nat.json').read_text(encoding='utf-8'))
    pedidos = set(sys.argv[1:])
    if pedidos: casos = [c for c in casos if c['motor'] in pedidos or c['motor'].replace('_x', '') in pedidos]
    html = OUT / 'p.html'
    html.write_text('<!doctype html><html><head><meta charset="utf-8">' + ''.join(f'<link rel="stylesheet" href="{RAIZ / c}">' for c in CSS) +
                    '<style>body{margin:0;padding:10px;background:#fff}#c{width:480px;border:1px solid #ddd;padding:8px;box-sizing:border-box}</style></head><body><div id="c"></div>' +
                    ''.join(f'<script src="{RAIZ / s}"></script>' for s in SCRIPTS if (RAIZ / s).exists()) + '</body></html>', encoding='utf-8')
    malos = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width': 520, 'height': 900})
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto(html.as_uri())
        for c in casos:
            m, prm = c['motor'], c.get('p', {})
            nombre = c.get('nombre', m)
            errs.clear()
            ok = await pg.evaluate("([m, p]) => { const v = document.getElementById('c'), el = document.createElement('div'); el.id = 'c'; v.replaceWith(el); return WaveLeccionBanco.render(el, {motor: m, p: p}, {sonar(){}, confeti(){}}); }", [m, prm])
            if not ok: malos.append(f'{nombre}: el motor no existe'); continue
            tipo = await pg.evaluate("m => WaveLeccionBanco.motores[m].tipo", m)
            if tipo == 'ejemplo':
                sels = await pg.evaluate("() => [...document.querySelectorAll('#c select[data-k]')].map(s => [s.getAttribute('data-k'), [...s.options].map(o => o.value)])")
                combos = [None]
                if sels:
                    k, vals = sels[0]; combos = [(k, v) for v in vals]
                    if len(sels) > 1: combos += [(sels[1][0], v) for v in sels[1][1][1:]]
                for ci, cb in enumerate(combos):
                    if cb:
                        await pg.evaluate("([k, v]) => { const s = document.querySelector('#c select[data-k=\"' + k + '\"]'); s.value = v; s.dispatchEvent(new Event('input', {bubbles: true})); s.dispatchEvent(new Event('change', {bubbles: true})); }", list(cb))
                    paso = 0
                    while True:
                        paso += 1
                        d = f'{nombre} [{cb[0] + "=" + cb[1] if cb else "-"}] paso {paso}'
                        txt = await pg.inner_text('#c')
                        if 'NaN' in txt or 'undefined' in txt: malos.append(f'{d}: muestra NaN/undefined')
                        sale = await pg.evaluate("""() => { const c = document.getElementById('c').getBoundingClientRect(); const fuera = [];
                            document.querySelectorAll('#c *').forEach(e => { const q = e.getBoundingClientRect(); if (q.width && (q.right > c.right + 2 || q.left < c.left - 2)) fuera.push(e.tagName + ':' + (e.textContent || '').slice(0, 30)); });
                            document.querySelectorAll('#c svg text').forEach(t => { const s = t.closest('svg').getBoundingClientRect(), q = t.getBoundingClientRect(); if (q.width && (q.right > s.right + 1 || q.left < s.left - 1 || q.top < s.top - 1 || q.bottom > s.bottom + 1)) fuera.push('texto fuera del dibujo: ' + t.textContent.slice(0, 30)); });
                            return fuera.slice(0, 3); }""")
                        if sale: malos.append(f'{d}: se sale → {sale}')
                        if ci < 2: await (await pg.query_selector('#c')).screenshot(path=str(OUT / f'{nombre}-{ci}-{paso}.png'))
                        sig = await pg.query_selector('#c .lb-pp-b.sig:not([disabled])')
                        if not sig or paso > 20: break
                        await sig.click()
                    if paso < 2: malos.append(f'{nombre}: el ejemplo no es paso a paso')
            else:
                for ronda in range(6):
                    r = await pg.evaluate("() => { const el = document.getElementById('c'); el._lb.resolver(); return el._lb.comprobar(); }")
                    if ronda == 0: await (await pg.query_selector('#c')).screenshot(path=str(OUT / f'{nombre}-ej.png'))
                    txt = await pg.inner_text('#c')
                    if 'NaN' in txt or 'undefined' in txt: malos.append(f'{nombre} ronda {ronda}: muestra NaN/undefined')
                    if not r or not r.get('ok'): malos.append(f'{nombre} ronda {ronda}: la respuesta correcta no pasa → {r}')
                    await pg.click('#c [data-lb="otro"]')
            for e in errs: malos.append(f'{nombre}: error de JavaScript → {e}')
        await b.close()
    for x in malos: print('  ✘', x)
    print(f'{len(malos)} problema(s) en {len(casos)} casos. Capturas en {OUT}/')
    sys.exit(1 if malos else 0)

asyncio.run(main())
