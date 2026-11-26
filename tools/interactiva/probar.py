# -*- coding: utf-8 -*-
"""PRUEBA EN EL NAVEGADOR de las lecciones interactivas, COMO LAS VE EL ALUMNO (con accesibilidad y dictado cargados).
Recorre cada nivel, cada pantalla, cada paso del ejemplo y abre la práctica. Falla si hay errores de JavaScript, textos con
NaN/undefined, ejemplos que se salen de su recuadro, pantallas sin ejemplo paso a paso o sin práctica. Guarda capturas en /tmp/probar/.
Uso: python3 tools/interactiva/probar.py contenido/<materia>/mision-N/mision-N.json [...]   (necesita playwright y Chrome)"""
import asyncio, json, os, sys, pathlib
from playwright.async_api import async_playwright
RAIZ = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = ['js/apoyos.js', 'js/wave-calc.js', 'js/leccion-banco.js', 'js/leccion-banco2.js', 'js/leccion-interactiva.js']
CSS = ['css/styles.css', 'css/apoyos.css']
async def probar(pg, ruta, M, out):
    malos = []
    for n, niv in sorted((M.get('niveles') or {}).items()):
        L = (niv or {}).get('leccion')
        if not L: continue
        html = out / f'n{n}.html'
        html.write_text('<!doctype html><html><head><meta charset="utf-8">' + ''.join(f'<link rel="stylesheet" href="{RAIZ / c}">' for c in CSS) + '</head><body>' +
                        ''.join(f'<script src="{RAIZ / s}"></script>' for s in SCRIPTS) +
                        f'<script>WaveLeccion.abrir({{titulo:"Nivel {n}",contenido:{json.dumps(niv, ensure_ascii=False)}}});</script></body></html>', encoding='utf-8')
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto(html.as_uri()); await pg.wait_for_timeout(400)
        for t in range(len(L['temas'])):
            d = f'{ruta} · nivel {n} · pantalla {t + 1}'
            if t: await pg.click(f'[data-ir="{t}"]'); await pg.wait_for_timeout(250)
            pasos = 0
            while True:
                txt = await pg.locator('.li2-lado').inner_text() if await pg.locator('.li2-lado').count() else ''
                if 'NaN' in txt or 'undefined' in txt: malos.append(f'{d}: el ejemplo muestra NaN/undefined')
                sale = await pg.evaluate("""() => { const c = document.querySelector('.li2-lado .li2-ejem'); if (!c) return 'sin ejemplo'; const r = c.getBoundingClientRect();
                  return [...c.querySelectorAll('*')].some(e => { const q = e.getBoundingClientRect(); return q.width && (q.right > r.right + 2 || q.left < r.left - 2); }) ? 'se sale' : ''; }""")
                if sale: malos.append(f'{d}: ejemplo {sale} (paso {pasos + 1})'); 
                sig = pg.locator('.li2-motor [data-pp="1"]')
                if not await sig.count(): malos.append(f'{d}: el ejemplo no es paso a paso'); break
                await pg.locator('.li2-lado').screenshot(path=str(out / f'n{n}-p{t + 1}-paso{pasos + 1}.png'))
                if await sig.is_disabled() or pasos > 25: break
                await sig.click(); pasos += 1; await pg.wait_for_timeout(60)
            if not await pg.locator('[data-li="practicar"]').count(): malos.append(f'{d}: sin práctica'); continue
            await pg.click('[data-li="practicar"]'); await pg.wait_for_timeout(300)
            for k in range(3):   # tres juegos de "Otros números"
                txt = await pg.locator('.li2-pv').inner_text() if await pg.locator('.li2-pv').count() else ''
                if 'NaN' in txt or 'undefined' in txt: malos.append(f'{d}: la práctica muestra NaN/undefined')
                if k == 0: await pg.screenshot(path=str(out / f'n{n}-p{t + 1}-practica.png'))
                b = pg.locator('.li2-pv [data-lb="nuevo"], .li2-pv .lb-nuevo')
                if await b.count(): await b.first.click(); await pg.wait_for_timeout(100)
            await pg.click('[data-pv="x"]'); await pg.wait_for_timeout(150)
        malos += [f'{ruta} · nivel {n}: error de JavaScript: {e}' for e in errs]
    return malos
async def main():
    out = pathlib.Path('/tmp/probar'); out.mkdir(exist_ok=True)
    todos = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None)
        pg = await b.new_page(viewport={'width': 1366, 'height': 768})
        for ruta in sys.argv[1:]:
            todos += await probar(pg, ruta, json.load(open(ruta, encoding='utf-8')), out)
        await b.close()
    for m in todos: print('  ✘', m)
    print(f'{len(todos)} problema(s). Capturas en {out}/ (mirá al menos una por pantalla).')
    sys.exit(1 if todos else 0)
asyncio.run(main())
