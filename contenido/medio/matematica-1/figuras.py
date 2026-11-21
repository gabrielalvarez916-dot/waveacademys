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


def png(fig):
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
