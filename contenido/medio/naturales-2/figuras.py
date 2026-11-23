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
