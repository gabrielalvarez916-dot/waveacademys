# -*- coding: utf-8 -*-
"""Dibujos para los PDF de Ciencias Naturales 2 (Nivel Medio, primeros años).
Reusa los de Lengua 2 (carteles, tiras, objetos dibujados, láminas) y suma dibujos propios de Naturales."""
import os, importlib.util
_s = importlib.util.spec_from_file_location('figuras_leng2', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lengua-2', 'figuras.py'))
_L = importlib.util.module_from_spec(_s); _s.loader.exec_module(_L)
nombres, tiras, letras, lista, objetos, ficha, lamina, dibujo_palabra = _L.nombres, _L.tiras, _L.letras, _L.lista, _L.objetos, _L.ficha, _L.lamina, _L.dibujo_palabra
png, lienzo, F = _L.png, _L.lienzo, _L.F
TEAL, OSC, MENTA, AMBAR, CORAL, VERDE, AZUL, LILA = _L.TEAL, _L.OSC, _L.MENTA, _L.AMBAR, _L.CORAL, _L.VERDE, _L.AZUL, _L.LILA
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch


def _persona(ax, x, base, alto, color):
    """Persona simple: cabeza y cuerpo, de la altura pedida (base = el piso)."""
    r = alto * .13
    ax.add_patch(Circle((x, base + alto - r), r, color="#f6d2b0", ec=OSC, lw=1.4))
    ax.add_patch(FancyBboxPatch((x - alto * .14, base + alto * .38), alto * .28, alto * .34, boxstyle="round,pad=0.01,rounding_size=0.05", color=color, ec=OSC, lw=1.2))
    for dx in (-.06, .06): ax.plot([x + dx * alto, x + dx * alto], [base, base + alto * .38], color=OSC, lw=2.5)


def crecimiento(etapas, titulo=None):
    """Personas de distinta altura una al lado de la otra: [("BEBÉ", .5), ("NIÑO", 1.0), ("ADULTO", 1.7)]. Con su nombre abajo."""
    n = len(etapas); W = 2.2 * n; H = 3.0
    fig, ax = lienzo(min(7.0, 1.9 * n), 2.7, W, H, 0, 0)
    ax.plot([0, W], [.55, .55], color="#b8c4c4", lw=2)
    cols = [CORAL, TEAL, AZUL, LILA, VERDE]
    for i, (txt, alto) in enumerate(etapas):
        x = 2.2 * i + 1.1; _persona(ax, x, .55, alto * 1.3, cols[i % len(cols)])
        ax.text(x, .22, txt.upper(), ha="center", va="center", fontsize=11, color=OSC, **F)
    return png(fig)


from matplotlib.patches import Ellipse, Polygon


def _huevo(ax, x, y, s=1.0):
    ax.add_patch(Ellipse((x, y), .45 * s, .6 * s, color="#fbf3e4", ec=OSC, lw=1.4))


def _semilla(ax, x, y, s=1.0):
    ax.add_patch(Ellipse((x, y), .35 * s, .22 * s, angle=30, color="#a07a4a", ec=OSC, lw=1.2))
    ax.plot([x - .1 * s, x + .1 * s], [y - .05 * s, y + .05 * s], color="#7a5a35", lw=1)


def _maceta(ax, x, y, s=1.0):
    ax.add_patch(Polygon([(x - .35 * s, y), (x + .35 * s, y), (x + .25 * s, y - .5 * s), (x - .25 * s, y - .5 * s)], closed=True, color="#d9774b", ec=OSC, lw=1.4))
    ax.plot([x, x], [y, y + .4 * s], color=VERDE, lw=2.5)
    for d in (-1, 1): ax.add_patch(Ellipse((x + d * .12 * s, y + .35 * s), .22 * s, .1 * s, angle=d * 25, color=VERDE))


def _fruto(ax, x, y, s=1.0):
    ax.add_patch(Circle((x, y), .3 * s, color="#e2493c", ec=OSC, lw=1.4))
    for (dx, dy) in ((-.08, .02), (.08, -.04), (0, -.12)): ax.add_patch(Ellipse((x + dx * s, y + dy * s), .06 * s, .1 * s, color="#f6e3b4"))
    ax.plot([x, x + .05 * s], [y + .28 * s, y + .42 * s], color="#6b4a2a", lw=2)


_L.OBJ2.update({"huevo": _huevo, "semilla": _semilla, "maceta": _maceta, "fruto": _fruto})
