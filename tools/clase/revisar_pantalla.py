# Control de pantalla: abre cada clase armada (tools/clase/dist/<slug>.html), recorre todas las escenas
# y avisa si un texto se sale de la pantalla o si dos textos se pisan. Uso: python3 tools/clase/revisar_pantalla.py slug1 slug2 ...
import asyncio, sys, os, json
from playwright.async_api import async_playwright
AQUI = os.path.dirname(os.path.abspath(__file__))
JS = r"""() => {
  const svg = document.querySelector('svg'); const vb = svg.viewBox.baseVal; const r0 = svg.getBoundingClientRect(); const k = r0.width / vb.width;
  const op = (el) => { let o = 1; for (let e = el; e && e !== svg; e = e.parentNode) { const s = getComputedStyle(e); o *= parseFloat(s.opacity || 1); if (s.display === 'none' || s.visibility === 'hidden') return 0; } return o; };
  const cur = (document.getElementById('escena') || svg).lastElementChild || svg;
  const T = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim() && op(t) > 0.2 && !t.closest('#subs') && cur.contains(t)).map(t => { const r = t.getBoundingClientRect();
    return { s: t.textContent.trim().slice(0, 40), x0: (r.left - r0.left) / k, y0: (r.top - r0.top) / k, x1: (r.right - r0.left) / k, y1: (r.bottom - r0.top) / k }; }).filter(b => b.x1 - b.x0 > 4);
  const out = [];
  T.forEach(b => { if (b.x0 < -2 || b.x1 > vb.width + 2 || b.y0 < -2 || b.y1 > vb.height + 2) out.push('se sale de la pantalla: «' + b.s + '»'); else if (b.y1 > vb.height - 125) out.push('queda bajo los controles del reproductor: «' + b.s + '»'); });
  for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const a = T[i], b = T[j];
    const w = Math.min(a.x1, b.x1) - Math.max(a.x0, b.x0), h = Math.min(a.y1, b.y1) - Math.max(a.y0, b.y0);
    if (!/[a-zA-Z0-9áéíóúñ]/i.test(a.s) && !/[a-zA-Z0-9áéíóúñ]/i.test(b.s)) continue; // dos emojis juntos (cubito sobre el vaso): a propósito
    if (w > 6 && h > 6) { const m = Math.min((a.x1 - a.x0) * (a.y1 - a.y0), (b.x1 - b.x0) * (b.y1 - b.y0)); if (w * h > .15 * m) out.push('se pisan: «' + a.s + '» y «' + b.s + '»'); } }
  // texto que se sale de su recuadro: el rect más chico (de la escena actual) que contiene el centro del texto
  const R = [...cur.querySelectorAll('rect')].filter(r => op(r) > 0.2).map(r => { const q = r.getBoundingClientRect(); return { x0: (q.left - r0.left) / k, y0: (q.top - r0.top) / k, x1: (q.right - r0.left) / k, y1: (q.bottom - r0.top) / k }; }).filter(q => (q.x1 - q.x0) > 40 && (q.y1 - q.y0) > 20 && (q.x1 - q.x0) < vb.width * 0.95);
  T.forEach(b => { const cx = (b.x0 + b.x1) / 2, cy = (b.y0 + b.y1) / 2; const dentro = R.filter(q => cx > q.x0 && cx < q.x1 && cy > q.y0 && cy < q.y1);
    if (!dentro.length || !/[a-zA-Z0-9áéíóúñ]/i.test(b.s) || /^(VERDADERO|FALSO)$/.test(b.s)) return; /* el sello de V o F cae encima a propósito */ const q = dentro.sort((a, c) => (a.x1 - a.x0) * (a.y1 - a.y0) - (c.x1 - c.x0) * (c.y1 - c.y0))[0];
    if (b.x0 < q.x0 - 3 || b.x1 > q.x1 + 3) out.push('se sale de su recuadro: «' + b.s + '»'); });
  return out; }"""
async def main(slugs):
    total = 0
    gsap = os.path.join(AQUI, '..', '..', 'node_modules', 'gsap', 'dist', 'gsap.min.js')
    if not os.path.exists(gsap): gsap = '/home/claude/chk/node_modules/gsap/dist/gsap.min.js'
    G = open(gsap).read() if os.path.exists(gsap) else None
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get('CHROME', '/usr/bin/google-chrome'), args=['--no-sandbox'])
        for slug in slugs:
            pg = await b.new_page(viewport={'width': 960, 'height': 540})
            if G: await pg.route('**/gsap.min.js', lambda r: r.fulfill(body=G, content_type='application/javascript'))
            await pg.goto('file://' + os.path.join(AQUI, 'dist', slug + '.html')); await pg.wait_for_timeout(300)
            n = await pg.evaluate("(document.getElementById('ui')||{remove(){}}).remove(); CLASE.escenas.length")
            for k in range(n):
                await pg.evaluate("LECCION.irA(%d)" % k); await pg.wait_for_timeout(450)
                await pg.evaluate("LECCION.tl().progress(1), 0"); await pg.wait_for_timeout(150)
                for m in await pg.evaluate(JS): print(f'{slug} escena {k}: {m}'); total += 1
            await pg.close()
        await b.close()
    print('pantalla:', 'OK' if not total else f'{total} problema(s)'); sys.exit(1 if total else 0)
asyncio.run(main(sys.argv[1:]))
