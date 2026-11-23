# -*- coding: utf-8 -*-
"""Dibujos para los PDF de Lengua 2 (Nivel Medio, primeros años). Reusa los de Lengua 1 (tiras, nombres, letras…)
y suma objetos de cuentos dibujados a mano (calabaza, zapato, reloj, castillo, varita, hada, ratón)."""
import os, importlib.util
from matplotlib.patches import Circle, Ellipse, Rectangle, Polygon, FancyBboxPatch
_s = importlib.util.spec_from_file_location('figuras_leng1', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lengua-1', 'figuras.py'))
_L = importlib.util.module_from_spec(_s); _s.loader.exec_module(_L)
nombres, letras, lista, tiras, dibujo_palabra = _L.nombres, _L.letras, _L.lista, _L.tiras, _L.dibujo_palabra
png, lienzo, F = _L.png, _L.lienzo, _L.F
TEAL, OSC, MENTA, AMBAR, CORAL, VERDE, AZUL, LILA = _L.TEAL, _L.OSC, _L.MENTA, _L.AMBAR, _L.CORAL, _L.VERDE, _L.AZUL, _L.LILA


def _calabaza(ax, x, y):
    for dx in (-.28, 0, .28): ax.add_patch(Ellipse((x + dx, y), .5, .62, color="#f08a24", ec=OSC, lw=1.2))
    ax.add_patch(Rectangle((x - .05, y + .28), .1, .16, color=VERDE))


def _zapato(ax, x, y):
    ax.add_patch(Polygon([(x - .45, y - .15), (x + .45, y - .15), (x + .45, y + .02), (x + .05, y + .05), (x - .25, y + .3), (x - .45, y + .3)], closed=True, color="#bfe6f5", ec=AZUL, lw=1.6))
    ax.add_patch(Rectangle((x + .3, y - .4), .08, .27, color="#bfe6f5", ec=AZUL, lw=1.2))


def _reloj(ax, x, y):
    ax.add_patch(Circle((x, y), .4, color="white", ec=OSC, lw=2))
    ax.plot([x, x], [y, y + .3], color=OSC, lw=2.5); ax.plot([x, x], [y, y + .22], color=CORAL, lw=3)
    ax.text(x, y + .3, "12", ha="center", va="center", fontsize=7, color=OSC, **F)


def _castillo(ax, x, y):
    ax.add_patch(Rectangle((x - .4, y - .4), .8, .55, color="#e8d9f5", ec=LILA, lw=1.4))
    for dx in (-.4, .25):
        ax.add_patch(Rectangle((x + dx, y - .4), .15, .8, color="#e8d9f5", ec=LILA, lw=1.4))
        ax.add_patch(Polygon([(x + dx - .03, y + .4), (x + dx + .18, y + .4), (x + dx + .075, y + .65)], closed=True, color=CORAL))
    ax.add_patch(Rectangle((x - .08, y - .4), .16, .25, color=LILA))


def _varita(ax, x, y):
    ax.plot([x - .35, x + .2], [y - .35, y + .2], color=OSC, lw=3)
    pts = [(x + .25 + .22 * __import__('math').cos(a), y + .25 + .22 * __import__('math').sin(a)) for a in [__import__('math').pi / 2 + k * 2 * __import__('math').pi / 5 * 2 for k in range(5)]]
    ax.add_patch(Polygon(pts, closed=True, color=AMBAR, ec=OSC, lw=1))


def _raton(ax, x, y):
    ax.add_patch(Ellipse((x, y - .05), .55, .35, color="#b9b9b9", ec=OSC, lw=1.2))
    ax.add_patch(Circle((x + .22, y + .12), .1, color="#b9b9b9", ec=OSC, lw=1))
    ax.plot([x - .27, x - .45], [y - .05, y + .1], color=OSC, lw=1.5)


def _vestido(ax, x, y):
    ax.add_patch(Polygon([(x - .12, y + .35), (x + .12, y + .35), (x + .4, y - .4), (x - .4, y - .4)], closed=True, color="#f7b6d2", ec=CORAL, lw=1.4))


OBJ2 = {"calabaza": _calabaza, "zapato": _zapato, "reloj": _reloj, "castillo": _castillo, "varita": _varita, "raton": _raton, "vestido": _vestido}


def objetos(pares, titulo=None):
    """Objetos de cuento con su nombre debajo: [("zapato", "ZAPATITO DE CRISTAL"), ...]."""
    n = len(pares); fig, ax = lienzo(min(7.2, 2.4 * n), 2.6, 2.4 * n, 2.6, 0, 0)
    for i, (obj, txt) in enumerate(pares):
        x = 2.4 * i + 1.2; OBJ2[obj](ax, x, 1.6)
        ax.text(x, .45, txt.upper(), ha="center", va="center", fontsize=10 if len(txt) > 9 else 12, color=OSC, **F)
    return png(fig)
