# -*- coding: utf-8 -*-
"""Dibujos para los PDF de Matemática 1 (Nivel Medio, primeros años): objetos simples para contar y comparar.
Cada función devuelve un PNG en base64 listo para un bloque {"tipo": "imagen", "png_base64": ...}.
Todo el texto de los dibujos va en IMPRENTA MAYÚSCULA (regla de tools/primeros_anios.py)."""
import io, base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon, FancyBboxPatch, Rectangle, RegularPolygon
from PIL import Image

TEAL, OSC, MENTA, AMBAR, CORAL, ROJO, VERDE, AZUL, LILA = "#0e7c7b", "#243b3f", "#d8f0ea", "#F4B63F", "#ff7a66", "#e2453c", "#4caf50", "#4a90d9", "#9b7fe0"
F = dict(fontfamily="DejaVu Sans", fontweight="bold")


def _ajustar_textos(fig):
    """REGLA: ninguna letra puede quedar afuera de su recuadro. Si un texto se sale del recuadro que lo contiene,
    primero se parte en dos renglones (si es una frase y entra de alto) y, si todavía no entra, se achica hasta que entre."""
    from matplotlib.patches import FancyBboxPatch as _FB, Rectangle as _R
    r = fig.canvas.get_renderer()
    for ax in fig.axes:
        cajas = [p for p in ax.patches if isinstance(p, (_FB, _R)) and p.get_gid() != 'resalte']
        for t in ax.texts:
            if not t.get_text().strip(): continue
            bb = t.get_window_extent(r); cx, cy = (bb.x0 + bb.x1) / 2, (bb.y0 + bb.y1) / 2
            dentro = [c.get_window_extent(r) for c in cajas]
            dentro = [c for c in dentro if c.x0 <= cx <= c.x1 and c.y0 <= cy <= c.y1 and c.height >= bb.height * .8]
            if not dentro: continue
            c = min(dentro, key=lambda c: c.width * c.height); m = max(12, .07 * c.width)
            otros = [o for o in ax.texts if o is not t and o.get_text().strip()]
            def entra(bb):
                if not (bb.x0 >= c.x0 + m and bb.x1 <= c.x1 - m and bb.y0 >= c.y0 + 3 and bb.y1 <= c.y1 - 3): return False
                for o in otros:  # tampoco puede pisar otro texto del mismo recuadro (por ejemplo, el número de la tira)
                    ob = o.get_window_extent(r)
                    if c.x0 <= ob.x0 and ob.x1 <= c.x1 and c.y0 <= ob.y0 and ob.y1 <= c.y1 and ob.x0 < bb.x1 and bb.x0 < ob.x1 and ob.y0 < bb.y1 and bb.y0 < ob.y1: return False
                return True
            if entra(t.get_window_extent(r)): continue
            _AVISOS.append(t.get_text())
            txt = t.get_text(); pal = txt.split(' ')
            if '\n' not in txt and len(pal) >= 3:
                for nl in (2, 3):  # probar en 2 y en 3 renglones, si entran de alto
                    if len(pal) < nl or c.height < bb.height * (nl * 1.1 + .2): break
                    obj = len(txt) / nl; cortes = []; acc = 0
                    for i, w in enumerate(pal[:-1]):
                        acc += len(w) + 1
                        if acc >= obj * (len(cortes) + 1) and len(cortes) < nl - 1: cortes.append(i + 1)
                    trozos = []; ini = 0
                    for k in cortes + [len(pal)]: trozos.append(' '.join(pal[ini:k])); ini = k
                    t.set_text('\n'.join(trozos)); t.set_linespacing(1.15)
                    if entra(t.get_window_extent(r)): break
            while t.get_fontsize() > 6 and not entra(t.get_window_extent(r)):
                t.set_fontsize(t.get_fontsize() - .5)
            if not entra(t.get_window_extent(r)):  # último recurso: centrar en el recuadro
                t.set_horizontalalignment('center'); inv = ax.transData.inverted(); t.set_x(inv.transform(((c.x0 + c.x1) / 2, 0))[0])


_AVISOS = []


def png(fig):
    _ajustar_textos(fig)
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=120, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=32)
    o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()


def lienzo(w, h, x1, y1, x0=0, y0=0):
    fig, ax = plt.subplots(figsize=(w, h)); ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect("equal"); ax.axis("off"); return fig, ax


# ---------------- objetos (centro x, y; tamaño ~1) ----------------
def globo(ax, x, y, c=CORAL):
    ax.add_patch(Ellipse((x, y + .12), .62, .78, color=c, ec=OSC, lw=1.4))
    ax.add_patch(Polygon([[x - .07, y - .3], [x + .07, y - .3], [x, y - .22]], color=c, ec=OSC, lw=1))
    ax.plot([x, x + .06, x - .04, x], [y - .3, y - .45, y - .6, y - .75], color=OSC, lw=1.2)
    ax.add_patch(Ellipse((x - .12, y + .3), .1, .18, color="white", alpha=.7))


def manzana(ax, x, y, c=ROJO):
    ax.add_patch(Circle((x - .12, y), .3, color=c, ec=OSC, lw=1.4)); ax.add_patch(Circle((x + .12, y), .3, color=c, ec=OSC, lw=1.4))
    ax.add_patch(Circle((x - .12, y), .28, color=c)); ax.add_patch(Circle((x + .12, y), .28, color=c))
    ax.plot([x, x + .04], [y + .22, y + .42], color="#6b4226", lw=2.2)
    ax.add_patch(Ellipse((x + .17, y + .38), .22, .1, angle=25, color=VERDE, ec=OSC, lw=.8))


def estrella(ax, x, y, c=AMBAR):
    import math
    P = [[x + (.4 if k % 2 == 0 else .17) * math.cos(math.pi / 2 + k * math.pi / 5), y + (.4 if k % 2 == 0 else .17) * math.sin(math.pi / 2 + k * math.pi / 5)] for k in range(10)]
    ax.add_patch(Polygon(P, color=c, ec=OSC, lw=1.4))


def pelota(ax, x, y, c=AZUL):
    ax.add_patch(Circle((x, y), .34, color=c, ec=OSC, lw=1.4))
    ax.plot([x - .34, x + .34], [y, y], color="white", lw=2.5); ax.plot([x, x], [y - .34, y + .34], color="white", lw=2.5)
    ax.add_patch(Circle((x, y), .34, fill=False, ec=OSC, lw=1.4))


def caramelo(ax, x, y, c=LILA):
    ax.add_patch(Polygon([[x - .2, y], [x - .45, y + .17], [x - .45, y - .17]], color=c, ec=OSC, lw=1.2))
    ax.add_patch(Polygon([[x + .2, y], [x + .45, y + .17], [x + .45, y - .17]], color=c, ec=OSC, lw=1.2))
    ax.add_patch(Ellipse((x, y), .46, .34, color=c, ec=OSC, lw=1.4))
    ax.plot([x - .08, x + .08], [y - .1, y + .1], color="white", lw=2)


def vaso(ax, x, y, c=MENTA):
    ax.add_patch(Polygon([[x - .26, y + .32], [x + .26, y + .32], [x + .19, y - .34], [x - .19, y - .34]], color=c, ec=OSC, lw=1.4))
    ax.add_patch(Polygon([[x - .23, y + .1], [x + .23, y + .1], [x + .19, y - .34], [x - .19, y - .34]], color=CORAL, alpha=.55))
    ax.plot([x + .08, x + .2, x + .32], [y + .2, y + .55, y + .6], color=AZUL, lw=2.5)


def chico(ax, x, y, c=TEAL):
    ax.add_patch(Circle((x, y + .26), .19, color="#f6c99c", ec=OSC, lw=1.4))
    ax.add_patch(Ellipse((x, y + .37), .4, .16, color="#6b4226"))
    ax.add_patch(Circle((x - .06, y + .26), .025, color=OSC)); ax.add_patch(Circle((x + .06, y + .26), .025, color=OSC))
    ax.add_patch(FancyBboxPatch((x - .2, y - .42), .4, .48, boxstyle="round,pad=0.02,rounding_size=0.12", color=c, ec=OSC, lw=1.4))


def silla(ax, x, y, c="#b5835a"):
    ax.add_patch(Rectangle((x - .25, y - .02), .5, .1, color=c, ec=OSC, lw=1.2))
    ax.add_patch(Rectangle((x - .25, y + .08), .08, .4, color=c, ec=OSC, lw=1.2))
    for dx in (-.22, .17): ax.add_patch(Rectangle((x + dx, y - .4), .06, .38, color=c, ec=OSC, lw=1))


OBJ = {"globo": globo, "manzana": manzana, "estrella": estrella, "pelota": pelota, "caramelo": caramelo, "vaso": vaso, "chico": chico, "silla": silla}


def numero(ax, x, y, n, r=.2, c=AMBAR):
    ax.add_patch(Circle((x, y), r, color=c, ec=OSC, lw=1.2)); ax.text(x, y - .01, str(n), ha="center", va="center", fontsize=12, color=OSC, **F)


def cartel(ax, x, y, s, c=TEAL, fs=14, tc="white"):
    ax.text(x, y, s.upper(), ha="center", va="center", fontsize=fs, color=tc, bbox=dict(boxstyle="round,pad=0.4", fc=c, ec=OSC, lw=1.2), **F)


def fila(ax, obj, n, y, x0=0.6, paso=1.0, **k):
    xs = [x0 + i * paso for i in range(n)]
    for x in xs: OBJ[obj](ax, x, y, **k)
    return xs


# ---------------- dibujos de la misión 1 ----------------
def contar_numerado(obj, n, total_txt):
    """Objetos en fila (hasta 5 por fila) con su número debajo y el total."""
    cols = min(5, n); filas = (n + cols - 1) // cols
    baja = .98 if obj == "globo" else .62; H = 1.45 + (baja - .62)  # el globo tiene hilo: el número va más abajo
    fig, ax = lienzo(1.25 * cols + 2.6, H * filas + .3, cols + 2.6, H * filas + .2, 0, -.2)
    k = 0
    for f in range(filas):
        y = H * (filas - f) - .45
        for c in range(cols):
            if k >= n: break
            x = .6 + c; OBJ[obj](ax, x, y); numero(ax, x, y - baja, k + 1); k += 1
    cartel(ax, cols + 1.25, H * filas / 2, total_txt, fs=13)
    ax.annotate("", xy=(cols + .3, H * filas / 2), xytext=(cols - .2, H * filas / 2), arrowprops=dict(arrowstyle="-|>", color=OSC, lw=1.6))
    return png(fig)


def grupos_letras(grupos):
    """Varios grupos para practicar: [('A', 'manzana', 3), ('B', 'pelota', 6)...] uno debajo del otro."""
    n = len(grupos); m = max(g[2] for g in grupos)
    fig, ax = lienzo(1.05 * m + 1.8, 1.15 * n, m + 1.6, 1.15 * n, 0, 0)
    for i, (letra, obj, cant) in enumerate(grupos):
        y = 1.15 * (n - i) - .55
        cartel(ax, .35, y, letra, c=AMBAR, tc=OSC, fs=13)
        for j in range(cant): OBJ[obj](ax, 1.3 + j, y)
        ax.add_patch(FancyBboxPatch((.9, y - .5), m + .55, 1.0, boxstyle="round,pad=0.02,rounding_size=0.2", fill=False, ec=TEAL, lw=1.2, ls="--"))
    return png(fig)


def dos_grupos(a, b, txt_a, txt_b, nombres=("", ""), objb=None):
    """Dos filas para comparar, cada una con su cartel (MÁS / MENOS / IGUAL)."""
    obj, na = a; objb, nb = b
    m = max(na, nb); fig, ax = lienzo(1.05 * m + 3.4, 2.7, m + 3.2, 2.6, 0, 0)
    for y, (o, n, t, nom) in ((1.9, (obj, na, txt_a, nombres[0])), (.65, (objb, nb, txt_b, nombres[1]))):
        if nom: ax.text(.55, y, nom.upper(), ha="center", va="center", fontsize=12, color=OSC, **F)
        for j in range(n): OBJ[o](ax, 1.6 + j, y)
        cartel(ax, m + 2.35, y, t, c=TEAL if t.upper() != "MENOS" else CORAL, fs=12)
    return png(fig)


def parejas(a, b, txt, sobra=True):
    """Uno con uno: fila de arriba unida con la de abajo; lo que sobra queda marcado."""
    (oa, na), (ob, nb) = a, b
    m = max(na, nb); fig, ax = lienzo(1.1 * m + .4, 3.3, m + .2, 3.2, 0, -.5)
    for j in range(na): OBJ[oa](ax, .6 + j, 2.3)
    for j in range(nb): OBJ[ob](ax, .6 + j, .5)
    for j in range(min(na, nb)): ax.plot([.6 + j, .6 + j], [1.75, 1.05], color=TEAL, lw=2.2)
    for j in range(min(na, nb), max(na, nb)):
        y = 2.3 if na > nb else .5
        ax.add_patch(Circle((.6 + j, y), .48, fill=False, ec=CORAL, lw=2.2, ls="--"))
    cartel(ax, m / 2 + .1, -.25, txt, c=AMBAR, tc=OSC, fs=12)
    return png(fig)


def tres_casos():
    """Sobran, faltan e igual, uno al lado del otro (chicos y vasos)."""
    fig, ax = lienzo(9, 3.0, 13.4, 3.1, 0, -.6)
    for x0, nv, txt in ((0, 4, "SOBRAN VASOS"), (4.7, 2, "FALTAN VASOS"), (9.4, 3, "IGUAL")):
        for j in range(3): chico(ax, x0 + .6 + j, 2.2)
        for j in range(nv): vaso(ax, x0 + .6 + j, .45)
        for j in range(min(3, nv)): ax.plot([x0 + .6 + j] * 2, [1.72, 1.0], color=TEAL, lw=2)
        cartel(ax, x0 + 2.0, -.35, txt, c=TEAL if txt == "IGUAL" else AMBAR, tc="white" if txt == "IGUAL" else OSC, fs=11)
    return png(fig)


def igualar(obj, na, nb, accion):
    """Dos grupos: se agregan (punteados) al más chico o se tachan del más grande hasta que haya igual."""
    m = max(na, nb); fig, ax = lienzo(1.05 * m + 2.6, 2.8, m + 2.4, 2.7, 0, 0)
    meta = max(na, nb) if accion == "agregar" else min(na, nb)
    for y, n in ((1.95, na), (.7, nb)):
        for j in range(n): OBJ[obj](ax, .6 + j, y)
        if accion == "agregar":
            for j in range(n, meta):
                ax.add_patch(Circle((.6 + j, y), .42, fill=False, ec=VERDE, lw=2.2, ls="--")); ax.text(.6 + j, y, "+", ha="center", va="center", fontsize=20, color=VERDE, **F)
        else:
            for j in range(meta, n):
                ax.plot([.25 + j, .95 + j], [y - .35, y + .35], color=CORAL, lw=3); ax.plot([.25 + j, .95 + j], [y + .35, y - .35], color=CORAL, lw=3)
        cartel(ax, m + 1.5, y, str(meta), c=TEAL, fs=14)
    return png(fig)


# ---------------- dibujos de la misión 2 (números hasta 20) ----------------
def tren(desde, hasta, faltan=(), titulo=None):
    """Tren con un vagón por número; los que faltan quedan en blanco con un '?'."""
    N = list(range(desde, hasta + 1)); n = len(N)
    fig, ax = lienzo(1.0 * n + 2.2, 2.1, n + 1.9, 2.0, 0, -0.1)
    # locomotora
    ax.add_patch(FancyBboxPatch((0.15, .45), 1.1, .9, boxstyle="round,pad=0.02,rounding_size=0.15", color=CORAL, ec=OSC, lw=1.4))
    ax.add_patch(Rectangle((0.3, 1.35), .3, .35, color=OSC)); ax.add_patch(Rectangle((0.75, .85), .38, .35, color="white", ec=OSC, lw=1))
    for x in (0.45, 1.0): ax.add_patch(Circle((x, .35), .16, color=OSC))
    for j, v in enumerate(N):
        x = 1.45 + j
        falta = v in faltan
        ax.add_patch(FancyBboxPatch((x, .45), .85, .8, boxstyle="round,pad=0.02,rounding_size=0.12", fill=not falta, color=[TEAL, AMBAR, AZUL, LILA, VERDE][j % 5], ec=CORAL if falta else OSC, lw=2 if falta else 1.4, ls="--" if falta else "-"))
        if falta: ax.add_patch(FancyBboxPatch((x, .45), .85, .8, boxstyle="round,pad=0.02,rounding_size=0.12", color="white", ec=CORAL, lw=2, ls="--"))
        ax.text(x + .425, .85, "?" if falta else str(v), ha="center", va="center", fontsize=16, color=CORAL if falta else "white", **F)
        for dx in (.2, .65): ax.add_patch(Circle((x + dx, .35), .12, color=OSC))
        if j: ax.plot([x - .15, x], [.6, .6], color=OSC, lw=2)
    ax.plot([0, n + 1.6], [.2, .2], color=OSC, lw=2)
    return png(fig)


def diez_y_mas(obj, n, texto=None):
    """Una caja de 10 (dos filas de 5) y los sueltos al lado: 10 y n-10."""
    sueltos = n - 10
    fig, ax = lienzo(5.6 + 1.0 * min(5, sueltos) + 1.5, 3.0, 6.6 + min(5, sueltos) + 1.2, 2.9, 0, -0.5)
    ax.add_patch(FancyBboxPatch((0.1, 0.1), 5.3, 2.4, boxstyle="round,pad=0.02,rounding_size=0.25", color="#fff4d6", ec=AMBAR, lw=2.2))
    for k in range(10): OBJ[obj](ax, 0.75 + (k % 5), 1.85 - (k // 5) * 1.05)
    cartel(ax, 2.75, -0.25, "10", c=AMBAR, tc=OSC, fs=13)
    ax.text(5.95, 1.3, "+", ha="center", va="center", fontsize=30, color=OSC, **F)
    for k in range(sueltos): OBJ[obj](ax, 6.8 + (k % 5), 1.85 - (k // 5) * 1.05)
    if texto: cartel(ax, 6.8 + (min(5, sueltos) - 1) / 2, -0.25, texto, c=TEAL, fs=13)
    return png(fig)


def tarjetas(pares, ocultar=()):
    """Tarjetas número / palabra. ocultar: índices de tarjetas con la palabra en blanco (para completar)."""
    n = len(pares); fig, ax = lienzo(2.6 * n, 2.4, 2.6 * n, 2.4, 0, 0)
    for i, (num, pal) in enumerate(pares):
        x = 2.6 * i + .15
        ax.add_patch(FancyBboxPatch((x, .15), 2.3, 2.1, boxstyle="round,pad=0.02,rounding_size=0.2", color=MENTA, ec=TEAL, lw=1.8))
        ax.text(x + 1.15, 1.45, str(num), ha="center", va="center", fontsize=34, color=OSC, **F)
        ax.text(x + 1.15, .55, "_______" if i in ocultar else pal.upper(), ha="center", va="center", fontsize=13, color=TEAL, **F)
    return png(fig)


def recta_num(desde, hasta, marcas=(), flechas=()):
    """Recta numérica. marcas: [(valor, etiqueta)]; flechas: [(desde, hasta)] arcos de salto."""
    n = hasta - desde
    fig, ax = lienzo(0.62 * n + 1.4, 2.4, n + 1.2, 2.4, -0.6, -0.9)
    ax.annotate("", xy=(n + .5, 0), xytext=(-.5, 0), arrowprops=dict(arrowstyle="-|>", color=OSC, lw=1.8))
    for v in range(desde, hasta + 1):
        x = v - desde; ax.plot([x, x], [-.12, .12], color=OSC, lw=1.4); ax.text(x, -.45, str(v), ha="center", va="center", fontsize=11, color=OSC, **F)
    for v, et in marcas:
        x = v - desde; ax.add_patch(Circle((x, 0), .2, color=AMBAR, ec=OSC, lw=1.2, zorder=3))
        if et: cartel(ax, x, .95, et, c=TEAL, fs=10)
    for a, b in flechas:
        from matplotlib.patches import FancyArrowPatch
        ax.add_patch(FancyArrowPatch((a - desde, .25), (b - desde, .25), connectionstyle="arc3,rad=-.6", arrowstyle="-|>", mutation_scale=16, color=CORAL, lw=2))
    return png(fig)


# ---------------- dibujos de números hasta 1.000 (Matemática 2) ----------------
def _caja100(ax, x, y):
    ax.add_patch(FancyBboxPatch((x - .42, y - .32), .84, .64, boxstyle="round,pad=0.02,rounding_size=0.08", color="#dcaa62", ec=OSC, lw=1.3))
    ax.text(x, y - .05, "100", ha="center", va="center", fontsize=11, color="white", **F)


def _paq10(ax, x, y):
    ax.add_patch(FancyBboxPatch((x - .38, y - .17), .76, .34, boxstyle="round,pad=0.02,rounding_size=0.08", color=CORAL, ec=OSC, lw=1.2))
    ax.text(x, y - .01, "10", ha="center", va="center", fontsize=10, color="white", **F)


def _uno(ax, x, y):
    ax.add_patch(Circle((x, y), .2, color="#8a5634", ec=OSC, lw=1.1))


def bloques(c, d, u, texto=None):
    """Cajas de 100, paquetes de 10 y sueltos, en tres columnas con su cartel."""
    import math
    filas = max(1, math.ceil(max(c, d, u, 1) / 3)); fondo = 2.0 - (filas - 1) * .75 - .85
    fig, ax = lienzo(9.6, 3.6 - (2.0 - fondo) * .0 + 0, 9.6, 3.2, 0, fondo - .4)
    for j, (n, cab, dib, dx, dy) in enumerate(((c, "CENTENAS", _caja100, .95, .75), (d, "DECENAS", _paq10, .85, .42), (u, "UNIDADES", _uno, .5, .5))):
        x0 = .5 + j * 3.2
        cartel(ax, x0 + 1.1, 2.75, cab, c=TEAL, fs=10)
        for k in range(n): dib(ax, x0 + .2 + (k % 3) * dx, 2.0 - (k // 3) * dy)
        cartel(ax, x0 + 1.1, fondo, str(n), c=AMBAR, tc=OSC, fs=13)
    if texto: ax.text(4.8, -.35, "", ha="center")
    return png(fig)


def recta_cien(marcas=()):
    """Recta del 0 al 1.000, de 100 en 100. marcas: [(valor, etiqueta)]."""
    fig, ax = lienzo(9.5, 2.2, 10.9, 2.2, -0.5, -0.9)
    ax.annotate("", xy=(10.4, 0), xytext=(-.3, 0), arrowprops=dict(arrowstyle="-|>", color=OSC, lw=1.8))
    for k in range(11):
        ax.plot([k, k], [-.12, .12], color=OSC, lw=1.4); ax.text(k, -.45, f"{k*100:,}".replace(",", "."), ha="center", va="center", fontsize=9, color=OSC, **F)
    for v, et in marcas:
        ax.add_patch(Circle((v / 100, 0), .16, color=AMBAR, ec=OSC, lw=1.2, zorder=3))
        if et: cartel(ax, v / 100, .85, et, c=TEAL, fs=9)
    return png(fig)


def tablero(numeros, vacios=()):
    """Tablero de valor posicional: C | D | U para cada número. vacios: índices de filas en blanco (para completar)."""
    n = len(numeros); fig, ax = lienzo(6.4, .75 * (n + 1) + .2, 6.4, .75 * (n + 1) + .2, 0, 0)
    H = .75 * (n + 1)
    for j, (cab, col) in enumerate((("NÚMERO", OSC), ("C", "#dcaa62"), ("D", CORAL), ("U", "#8a5634"))):
        x = .1 + j * 1.55
        ax.add_patch(Rectangle((x, H - .7), 1.5, .62, color=col)); ax.text(x + .75, H - .39, cab, ha="center", va="center", fontsize=12, color="white", **F)
        for i, num in enumerate(numeros):
            y = H - .7 - (i + 1) * .75
            ax.add_patch(Rectangle((x, y), 1.5, .68, fill=False, ec=TEAL, lw=1.2))
            s = str(num).rjust(3, "0")
            v = str(num) if j == 0 else ("" if i in vacios else s[j - 1])
            ax.text(x + .75, y + .34, v, ha="center", va="center", fontsize=14, color=OSC, **F)
    return png(fig)


def camiones(nums, titulo=None):
    """Camiones con su número, en el orden dado (para ordenar de menor a mayor o al revés)."""
    n = len(nums); fig, ax = lienzo(2.3 * n, 1.9, 2.3 * n, 1.8, 0, 0)
    for i, v in enumerate(nums):
        x = 2.3 * i + .15
        ax.add_patch(FancyBboxPatch((x, .55), 1.35, .95, boxstyle="round,pad=0.02,rounding_size=0.12", color=TEAL, ec=OSC, lw=1.4))
        ax.add_patch(FancyBboxPatch((x + 1.4, .55), .6, .7, boxstyle="round,pad=0.02,rounding_size=0.1", color=MENTA, ec=OSC, lw=1.4))
        for dx in (.35, 1.65): ax.add_patch(Circle((x + dx, .45), .2, color=OSC))
        ax.text(x + .68, 1.02, f"{v:,}".replace(",", "."), ha="center", va="center", fontsize=17, color="white", **F)
    return png(fig)


def tren_paso(desde, hasta, paso, faltan=()):
    """Tren que cuenta de 10 en 10 o de 100 en 100."""
    N = list(range(desde, hasta + 1, paso)); n = len(N)
    fig, ax = lienzo(1.15 * n + 2.2, 2.1, 1.15 * n + 1.9, 2.0, 0, -0.1)
    ax.add_patch(FancyBboxPatch((0.15, .45), 1.1, .9, boxstyle="round,pad=0.02,rounding_size=0.15", color=CORAL, ec=OSC, lw=1.4))
    ax.add_patch(Rectangle((0.3, 1.35), .3, .35, color=OSC)); ax.add_patch(Rectangle((0.75, .85), .38, .35, color="white", ec=OSC, lw=1))
    for x in (0.45, 1.0): ax.add_patch(Circle((x, .35), .16, color=OSC))
    for j, v in enumerate(N):
        x = 1.45 + j * 1.15; falta = v in faltan
        ax.add_patch(FancyBboxPatch((x, .45), 1.0, .8, boxstyle="round,pad=0.02,rounding_size=0.12", color="white" if falta else [TEAL, AMBAR, AZUL, LILA, VERDE][j % 5], ec=CORAL if falta else OSC, lw=2 if falta else 1.4, ls="--" if falta else "-"))
        ax.text(x + .5, .85, "?" if falta else f"{v:,}".replace(",", "."), ha="center", va="center", fontsize=12 if v >= 1000 else 14, color=CORAL if falta else "white", **F)
        for dx in (.22, .78): ax.add_patch(Circle((x + dx, .35), .12, color=OSC))
    ax.plot([0, 1.15 * n + 1.6], [.2, .2], color=OSC, lw=2)
    return png(fig)


def cuadro(hasta, faltan=(), resaltar=(), desde=0):
    """Cuadro de números de a 10 por fila. faltan: casillas vacías (para completar). resaltar: casillas pintadas.
    REGLA FIJA: empieza SIEMPRE en 0, así los redondos (10, 20, 30…) quedan en el margen izquierdo de cada fila."""
    desde = 0
    filas = (hasta - desde + 10) // 10; fig, ax = lienzo(7.4, .74 * filas + .2, 10.2, filas + .2, 0, 0)
    for v in range(desde, hasta + 1):
        k = v - desde; x = .1 + (k % 10); y = filas - 1 - k // 10 + .1
        falta, res = v in faltan, v in resaltar
        ax.add_patch(FancyBboxPatch((x + .04, y + .04), .92, .84, boxstyle="round,pad=0.01,rounding_size=0.12",
                                    color="white" if falta else (AMBAR if res else MENTA), ec=CORAL if falta else TEAL, lw=1.6 if falta else 1.0, ls="--" if falta else "-"))
        if not falta: ax.text(x + .5, y + .46, str(v), ha="center", va="center", fontsize=13, color=OSC, **F)
    return png(fig)


def bolsitas(d, u, texto=None):
    """Bolsitas de 10 y sueltas (decenas y unidades), en dos columnas con su cartel."""
    import math
    filas = max(1, math.ceil(max(d, u, 1) / 3)); fondo = 2.0 - (filas - 1) * .5 - .75
    fig, ax = lienzo(6.6, 3.0, 6.6, 3.2, 0, fondo - .4)
    for j, (n, cab, dib, dx, dy) in enumerate(((d, "BOLSITAS DE 10", _paq10, .85, .5), (u, "SUELTAS", _uno, .5, .5))):
        x0 = .4 + j * 3.3
        cartel(ax, x0 + 1.0, 2.75, cab, c=TEAL, fs=10)
        for k in range(n): dib(ax, x0 + .2 + (k % 3) * dx, 2.0 - (k // 3) * dy)
        cartel(ax, x0 + 1.0, fondo, str(n), c=AMBAR, tc=OSC, fs=13)
    if texto: cartel(ax, 3.3, fondo, texto, c=VERDE, fs=12)
    return png(fig)


def chicos_numero(nums):
    """Chicos con su número en la remera (para ordenar), en el orden dado."""
    n = len(nums); fig, ax = lienzo(1.5 * n, 2.0, 1.5 * n, 2.0, 0, 0)
    for i, v in enumerate(nums):
        x = 1.5 * i + .75
        ax.add_patch(Circle((x, 1.55), .26, color="#f6c99c", ec=OSC, lw=1.4)); ax.add_patch(Ellipse((x, 1.7), .54, .2, color="#6b4226"))
        ax.add_patch(FancyBboxPatch((x - .42, .2), .84, .95, boxstyle="round,pad=0.02,rounding_size=0.15", color=[TEAL, CORAL, AZUL, LILA, VERDE][i % 5], ec=OSC, lw=1.4))
        ax.text(x, .66, str(v), ha="center", va="center", fontsize=17, color="white", **F)
    return png(fig)


def tablero_du(numeros, vacios=()):
    """Tablero de decenas y unidades: NÚMERO | D | U. vacios: filas con D y U en blanco (para completar)."""
    n = len(numeros); H = .75 * (n + 1); fig, ax = lienzo(4.8, H + .2, 4.8, H + .2, 0, 0)
    for j, (cab, col) in enumerate((("NÚMERO", OSC), ("D", CORAL), ("U", "#8a5634"))):
        x = .1 + j * 1.55
        ax.add_patch(Rectangle((x, H - .7), 1.5, .62, color=col)); ax.text(x + .75, H - .39, cab, ha="center", va="center", fontsize=12, color="white", **F)
        for i, num in enumerate(numeros):
            y = H - .7 - (i + 1) * .75
            ax.add_patch(Rectangle((x, y), 1.5, .68, fill=False, ec=TEAL, lw=1.2))
            s = str(num).rjust(2, "0")
            v = str(num) if j == 0 else ("" if i in vacios else s[j - 1])
            ax.text(x + .75, y + .34, v, ha="center", va="center", fontsize=14, color=OSC, **F)
    return png(fig)


def _plata(ax, x, y, v, sim="$"):
    if v >= 20:
        ax.add_patch(FancyBboxPatch((x - .5, y - .28), 1.0, .56, boxstyle="round,pad=0.03", fc="#2f8f5b", ec="#1d5e3b", lw=1.5))
        ax.text(x, y, f"{sim}{v}", ha="center", va="center", fontsize=12, color="white", **F)
    else:
        ax.add_patch(Circle((x, y), .3, fc=AMBAR if v >= 5 else "#c9ccd3", ec=OSC, lw=1.2))
        ax.text(x, y, f"{sim}{v}", ha="center", va="center", fontsize=10, color=OSC, **F)


def dinero(valores, texto=None, sim="$"):
    """Monedas (hasta 10) y billetes (20 o más) en fila, con el total abajo si se pide."""
    n = len(valores); paso = 1.2; W = n * paso + .4
    fig, ax = lienzo(min(6.8, W * .9 + .3), 1.9, W, 1.9, 0, 0)
    for k, v in enumerate(valores): _plata(ax, .8 + k * paso, 1.35, v, sim)
    if texto: cartel(ax, W / 2, .45, texto, c=VERDE, fs=13)
    return png(fig)


def precios(items, sim="$"):
    """Cosas del kiosco con su cartel de precio: items = [(objeto de OBJ, precio)]."""
    n = len(items); W = n * 1.8 + .2
    fig, ax = lienzo(min(6.8, W * .95), 2.0, W, 2.0, 0, 0)
    for k, (obj, p) in enumerate(items):
        x = 1.0 + k * 1.8; OBJ[obj](ax, x, 1.3)
        cartel(ax, x, .4, f"{sim}{p}", c=AMBAR, tc=OSC, fs=13)
    return png(fig)


# ---------------- dibujos de la misión 8 (juntar y agregar) ----------------
def juntar(a, b, texto=None):
    """Dos grupos (cada uno con su número), un + y, a la derecha, todo junto con el total. a, b = (objeto, cantidad)."""
    (oa, na), (ob, nb) = a, b; tot = na + nb
    ca, cb = min(na, 5), min(nb, 5); ct = min(tot, 5); fa, fb, ft = (na + 4) // 5, (nb + 4) // 5, (tot + 4) // 5
    H = 1.15 * max(fa, fb, ft) + 1.4; xa = 0.15; xb = xa + ca + 1.3; xt = xb + cb + 1.3; W = xt + ct + .3
    fig, ax = lienzo(min(9.5, .85 * W + .5), .85 * H + .3, W, H, 0, -1.0)
    def grupo(x0, obj, n, c, txt, col):
        filas = (n + 4) // 5
        ax.add_patch(FancyBboxPatch((x0, H - 1.0 - 1.15 * filas - .05), c, 1.15 * filas, boxstyle="round,pad=0.05,rounding_size=0.2", fill=False, ec=col, lw=1.8, ls="--"))
        for k in range(n): OBJ[obj](ax, x0 + .5 + (k % 5), H - 1.6 - (k // 5) * 1.15)
        cartel(ax, x0 + c / 2, -.55, txt, c=col if col != AMBAR else AMBAR, tc="white" if col != AMBAR else OSC, fs=14)
    grupo(xa, oa, na, ca, str(na), TEAL); grupo(xb, ob, nb, cb, str(nb), TEAL)
    ax.text(xb - .65, H - 1.6, "+", ha="center", va="center", fontsize=30, color=OSC, **F)
    ax.text(xt - .65, H - 1.6, "=", ha="center", va="center", fontsize=30, color=OSC, **F)
    for k in range(tot): OBJ[oa if k < na else ob](ax, xt + .5 + (k % 5), H - 1.6 - (k // 5) * 1.15)
    ax.add_patch(FancyBboxPatch((xt, H - 1.0 - 1.15 * ft - .05), ct, 1.15 * ft, boxstyle="round,pad=0.05,rounding_size=0.2", fill=False, ec=AMBAR, lw=2.2))
    cartel(ax, xt + ct / 2, -.55, texto or str(tot), c=AMBAR, tc=OSC, fs=14)
    return png(fig)


def agregar(obj, n, mas, texto=None):
    """Un grupo de n y los que llegan (marcados con +, en verde). Abajo, el total."""
    tot = n + mas; cols = min(tot, 5); filas = (tot + 4) // 5
    fig, ax = lienzo(1.1 * cols + 1.0, 1.15 * filas + 1.2, cols + .8, 1.15 * filas + .5, 0, -.9)
    for k in range(tot):
        x, y = .9 + (k % 5), 1.15 * filas - .3 - (k // 5) * 1.15
        OBJ[obj](ax, x, y)
        if k >= n:
            ax.add_patch(Circle((x, y), .5, fill=False, ec=VERDE, lw=2.4, ls="--"))
            ax.text(x + .4, y + .42, "+", ha="center", va="center", fontsize=16, color=VERDE, **F)
    cartel(ax, cols / 2 + .4, -.5, texto or f"{n} + {mas} = {tot}", c=AMBAR, tc=OSC, fs=14)
    return png(fig)


# ---------------- dibujos de la misión 9 (quitar y comparar) ----------------
def sacar(obj, n, menos, texto=None):
    """Un grupo de n con los últimos `menos` tachados (los que se sacan). Abajo, lo que queda."""
    q = n - menos; cols = min(n, 5); filas = (n + 4) // 5
    fig, ax = lienzo(1.1 * cols + 1.0, 1.15 * filas + 1.2, cols + .8, 1.15 * filas + .5, 0, -.9)
    for k in range(n):
        x, y = .9 + (k % 5), 1.15 * filas - .3 - (k // 5) * 1.15
        OBJ[obj](ax, x, y)
        if k >= q:
            ax.plot([x - .38, x + .38], [y - .38, y + .38], color=OSC, lw=3.6); ax.plot([x - .38, x + .38], [y + .38, y - .38], color=OSC, lw=3.6)
    cartel(ax, cols / 2 + .4, -.5, texto or f"QUEDAN {q}", c=AMBAR, tc=OSC, fs=14)
    return png(fig)


# ---------------- dibujos de la misión 10 (sumas y complementos a 10) ----------------
def marco10(n, obj="pelota", obj2=None, n2=0, texto=None):
    """Cuadro de 10 (2 filas de 5): n objetos, después n2 de otro tipo (obj2) y el resto vacío. Abajo, el texto."""
    fig, ax = lienzo(5.6, 3.2, 5.4, 3.0, 0, -.9)
    ax.add_patch(FancyBboxPatch((.15, .05), 5.1, 2.2, boxstyle="round,pad=0.02,rounding_size=0.15", color="#fff4d6", ec=AMBAR, lw=2.2))
    for k in range(10):
        x, y = .7 + (k % 5), 1.7 - (k // 5) * 1.1
        ax.add_patch(Rectangle((x - .45, y - .48), .9, .96, fill=False, ec=OSC, lw=1.2))
        if k < n: OBJ[obj](ax, x, y)
        elif k < n + n2: OBJ[obj2 or obj](ax, x, y)
    if texto: cartel(ax, 2.7, -.55, texto, c=TEAL, fs=14)
    return png(fig)


# ---------------- dibujos de la misión 12 (decenas enteras) ----------------
def recta_decenas(saltos=(), marcas=(), hasta=100):
    """Recta del 0 al 100 de 10 en 10, con saltos (arcos) de una decena a otra. saltos: [(desde, hasta)]; marcas: [(valor, etiqueta)]."""
    from matplotlib.patches import FancyArrowPatch
    n = hasta // 10
    fig, ax = lienzo(.85 * n + 1.2, 2.4, n + .8, 2.4, -0.5, -0.9)
    ax.annotate("", xy=(n + .5, 0), xytext=(-.3, 0), arrowprops=dict(arrowstyle="-|>", color=OSC, lw=1.8))
    for k in range(n + 1):
        ax.plot([k, k], [-.12, .12], color=OSC, lw=1.4); ax.text(k, -.45, str(k * 10), ha="center", va="center", fontsize=12, color=OSC, **F)
    for a, b in saltos:
        ax.add_patch(FancyArrowPatch((a / 10, .2), (b / 10, .2), connectionstyle="arc3,rad=%s" % (-.7 if b > a else .7), arrowstyle="-|>", mutation_scale=16, color=CORAL, lw=2))
    for v, et in marcas:
        ax.add_patch(Circle((v / 10, 0), .17, color=AMBAR, ec=OSC, lw=1.2, zorder=3))
        if et: cartel(ax, v / 10, 1.15, et, c=TEAL, fs=11)
    return png(fig)


# ---------------- dibujos de la misión 11 (dobles) ----------------
def cuentas(pares, ocultar=()):
    """Tarjetas con una cuenta arriba y su resultado grande abajo: [("6 + 6", 12)...]. ocultar: índices con el resultado en blanco."""
    n = len(pares); fig, ax = lienzo(2.6 * n, 2.4, 2.6 * n, 2.4, 0, 0)
    for i, (cta, res) in enumerate(pares):
        x = 2.6 * i + .15
        ax.add_patch(FancyBboxPatch((x, .15), 2.3, 2.1, boxstyle="round,pad=0.02,rounding_size=0.2", color=MENTA, ec=TEAL, lw=1.8))
        ax.text(x + 1.15, 1.75, cta, ha="center", va="center", fontsize=17, color=TEAL, **F)
        ax.text(x + 1.15, .85, "___" if i in ocultar else str(res), ha="center", va="center", fontsize=32, color=OSC, **F)
    return png(fig)


OBJ["bolsita"] = _paq10  # bolsita de 10 (misión 12): sirve en juntar, agregar y sacar


# ---------------- dibujos de la misión 15 (calculadora) ----------------
def calculadora(pantalla="0", resaltar=(), texto=None):
    """Calculadora simple con su pantalla; resaltar: teclas marcadas en amarillo (las que se aprietan)."""
    F_ = [['7', '8', '9', '−'], ['4', '5', '6', '+'], ['1', '2', '3', '='], ['0', 'C']]
    fig, ax = lienzo(3.4, 4.6, 5.0, 6.6, 0, -.9)
    ax.add_patch(FancyBboxPatch((.3, .2), 4.4, 5.9, boxstyle="round,pad=0.05,rounding_size=0.35", color="#24343a", ec=OSC, lw=1.6))
    ax.add_patch(FancyBboxPatch((.6, 4.75), 3.8, 1.0, boxstyle="round,pad=0.02,rounding_size=0.12", color="#cfe8c9", ec="#7fa77a", lw=1.4))
    ax.text(4.25, 5.25, pantalla, ha="right", va="center", fontsize=22, color="#1f3a1c", family="DejaVu Sans Mono", fontweight="bold")
    for r, fila in enumerate(F_):
        for c, k in enumerate(fila):
            x, y = .95 + c * 1.03, 4.05 - r * .95
            col = AMBAR if k in resaltar else ("#3c5158" if k.isdigit() else "#4f6f63")
            ax.add_patch(FancyBboxPatch((x - .4, y - .35), .8, .7, boxstyle="round,pad=0.02,rounding_size=0.12", color=col, ec=OSC, lw=1.1))
            ax.text(x, y, k, ha="center", va="center", fontsize=15, color=OSC if k in resaltar else "white", **F)
    if texto: cartel(ax, 2.5, -.5, texto, c=TEAL, fs=13)
    return png(fig)


# ---------------- cuenta en columnas (Matemática 2 · misiones 9 y 10: algoritmo de la suma y la resta) ----------------
def columnas(a, b, op="+", resultado=None, marcas=(), tachar=(), vacio=False):
    """Cuenta en columnas con C, D y U arriba. marcas: [(col, txt)] arriba de la columna ('U', 'D', 'C'): el «me llevo 1» o el 1 del canje.
    tachar: [(col, nuevo)] tacha la cifra de arriba y escribe el número nuevo (canje en la resta). vacio=True: el resultado queda en blanco (para completar)."""
    a, b = str(a), str(b); r = "" if resultado is None else str(resultado)
    nc = max(len(a), len(b), len(r), 2); IDX = {"U": 0, "D": 1, "C": 2}
    fig, ax = lienzo(1.15 * nc + 1.6, 4.0, 1.15 * nc + 1.6, 4.4, 0, 0)
    X = lambda k: 1.2 + (nc - 1 - k) * 1.15 + .5
    for k in range(nc):
        ax.add_patch(FancyBboxPatch((X(k) - .4, 3.75), .8, .45, boxstyle="round,pad=0.02,rounding_size=0.1", color=TEAL))
        ax.text(X(k), 3.97, ["U", "D", "C", "UM"][k], ha="center", va="center", fontsize=13, color="white", **F)
    def fila(s, y, c=OSC):
        for j, ch in enumerate(reversed(s)): ax.text(X(j), y, ch, ha="center", va="center", fontsize=26, color=c, **F)
    fila(a, 2.75); fila(b, 1.85)
    ax.text(X(nc - 1) - .9, 1.85, op, ha="center", va="center", fontsize=26, color=CORAL, **F)
    ax.plot([X(nc - 1) - 1.2, X(0) + .5], [1.35, 1.35], color=OSC, lw=2.5)
    if vacio:
        for k in range(nc): ax.add_patch(FancyBboxPatch((X(k) - .35, .45), .7, .7, boxstyle="round,pad=0.02,rounding_size=0.1", fill=False, ec=CORAL, lw=1.6, ls="--"))
    elif r: fila(r, .8, c=VERDE)
    for col, txt in marcas:
        k = IDX[col]; ax.add_patch(Circle((X(k), 3.35), .22, color="#fff4d6", ec=AMBAR, lw=1.6)); ax.text(X(k), 3.35, str(txt), ha="center", va="center", fontsize=12 if len(str(txt)) > 1 else 14, color=OSC, **F)
    for col, nuevo in tachar:
        k = IDX[col]; ax.plot([X(k) - .3, X(k) + .3], [2.45, 3.05], color=CORAL, lw=3)
        ax.text(X(k) + .45, 3.3, str(nuevo), ha="center", va="center", fontsize=15, color=CORAL, **F)
    return png(fig)


# ---------------- multiplicación (Matemática 2 · misiones 13 y 14) ----------------
def grupos(obj, n, cada, texto=None):
    """n bandejas iguales con 'cada' objetos (OBJ) adentro y su subtotal abajo (suma repetida)."""
    import math
    cols = cada if cada <= 3 else math.ceil(cada / 2); rows = math.ceil(cada / cols); w_, h_ = cols * .9 + .5, rows * .9 + .5
    W = n * (w_ + .4) + .2; fig, ax = lienzo(min(7.2, W * .9), 2.9, W, h_ + 1.6, 0, -1.0)
    for k in range(n):
        x = .3 + k * (w_ + .4)
        ax.add_patch(FancyBboxPatch((x, 0), w_, h_, boxstyle="round,pad=0.02,rounding_size=0.2", color="#fff4d6", ec=[TEAL, CORAL, AZUL, LILA, VERDE, AMBAR][k % 6], lw=2))
        for j in range(cada): OBJ[obj](ax, x + .7 + (j % cols) * .9, h_ - .7 - (j // cols) * .9)
        cartel(ax, x + w_ / 2, -.5, str((k + 1) * cada), c=AMBAR, tc=OSC, fs=12)
    if texto: ax.text(W / 2, h_ + .35, texto, ha="center", va="center", fontsize=14, color=OSC, **F)
    return png(fig)


def arreglo(obj, filas, cols, texto=None, contar=True):
    """Organización rectangular: filas × cols objetos (OBJ), con la cuenta de cada fila al costado si contar=True."""
    W, H = cols + 1.6, filas + (1.0 if texto else .4)
    fig, ax = lienzo(min(6.5, W * .75), min(5.2, H * .75), W, H, 0, 0)
    for r in range(filas):
        for c in range(cols): OBJ[obj](ax, .6 + c, filas - .4 - r)
        if contar: cartel(ax, cols + .7, filas - .4 - r, str((r + 1) * cols), c=AMBAR, tc=OSC, fs=11)
    if texto: ax.text(cols / 2 + .1, filas + .45, texto, ha="center", va="center", fontsize=14, color=OSC, **F)
    return png(fig)
