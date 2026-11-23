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


# ---------------- letra cursiva (misión 2): letra escolar Playwrite Argentina (licencia OFL, en fuentes/) ----------------
from matplotlib.font_manager import FontProperties
_FP = FontProperties(fname=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fuentes', 'PlaywriteAR-Regular.ttf'))


def cursiva(renglones, imprenta=None, repasar=False):
    """Renglones de cuaderno con texto en cursiva escolar. renglones: lista de textos (uno por renglón, en minúscula como se escribe).
    imprenta: lista paralela con la misma palabra en imprenta (a la izquierda). repasar=True: la cursiva sale en gris claro para repasar con el lápiz."""
    n = len(renglones); H = 1.25 * n + .2
    fig, ax = lienzo(6.8, min(5.5, .95 * n + .3), 10.0, H, 0, 0)
    for i, txt in enumerate(renglones):
        y = H - .5 - i * 1.25
        for dy, c, ls, lw in ((-.32, "#9fb8e6", "-", 1.2), (.05, "#c7d7f2", "--", .9), (.42, "#9fb8e6", "-", 1.2)):
            ax.plot([.1, 9.9], [y + dy, y + dy], color=c, ls=ls, lw=lw)
        x0 = .3
        if imprenta:
            ax.text(.3, y, imprenta[i].upper(), ha="left", va="center", fontsize=15, color=TEAL, **F); x0 = 3.3
        ax.text(x0, y - .3, txt, ha="left", va="baseline", fontsize=30, color="#b9c2d8" if repasar else "#1d2a5a", fontproperties=_FP)
    return png(fig)


# ---------------- textos informativos (misión 7): el hornero y su nido ----------------
def _hornero(ax, x, y, s=1.0, c="#c98a4b", panza="#f3d7b0", cola="#a8703a"):
    ax.add_patch(Ellipse((x, y), .9 * s, .55 * s, color=c, ec=OSC, lw=1.4))
    ax.add_patch(Ellipse((x, y - .08 * s), .55 * s, .3 * s, color=panza))
    ax.add_patch(Circle((x + .45 * s, y + .22 * s), .2 * s, color=c, ec=OSC, lw=1.2))
    ax.add_patch(Circle((x + .5 * s, y + .27 * s), .04 * s, color=OSC))
    ax.add_patch(Polygon([(x + .62 * s, y + .25 * s), (x + .85 * s, y + .2 * s), (x + .62 * s, y + .16 * s)], closed=True, color=AMBAR, ec=OSC, lw=1))
    ax.add_patch(Polygon([(x - .4 * s, y + .05 * s), (x - .8 * s, y + .2 * s), (x - .75 * s, y - .05 * s)], closed=True, color=cola, ec=OSC, lw=1))
    for dx in (-.08, .1): ax.plot([x + dx * s, x + dx * s], [y - .27 * s, y - .5 * s], color=OSC, lw=2)


def _nido(ax, x, y, s=1.0):
    ax.add_patch(Ellipse((x, y), 1.3 * s, 1.0 * s, color="#b07a46", ec=OSC, lw=1.6))
    ax.add_patch(Ellipse((x + .2 * s, y - .05 * s), .32 * s, .42 * s, color="#4a2f1a"))
    ax.add_patch(Rectangle((x - .9 * s, y - .58 * s), 1.8 * s, .1 * s, color="#7a5a3a"))


def _flor(ax, x, y, s=1.0):
    import math
    for k in range(5):
        a = k * 2 * math.pi / 5; ax.add_patch(Circle((x + .2 * s * math.cos(a), y + .2 * s * math.sin(a)), .14 * s, color="#f7b6d2", ec=CORAL, lw=1))
    ax.add_patch(Circle((x, y), .12 * s, color=AMBAR)); ax.plot([x, x], [y - .15 * s, y - .7 * s], color=VERDE, lw=2.5)


OBJ2.update({"paloma": lambda ax, x, y, s=1.0: _hornero(ax, x, y, s, "#9aa3b5", "#c9d0dc", "#7d8698"), "hornero": _hornero, "nido": _nido, "flor": _flor})


def _ancho(fig, ax, txt, fs=11):
    """Ancho en unidades del dibujo de un texto en negrita tamaño 11 (para resaltar palabras exactas)."""
    if not txt: return 0
    t = ax.text(0, 0, txt.replace(" ", "\u00a0"), fontsize=fs, **F); r = fig.canvas.get_renderer(); bb = t.get_window_extent(r); t.remove()
    inv = ax.transData.inverted(); return inv.transform((bb.x1, 0))[0] - inv.transform((bb.x0, 0))[0]


def lamina(titulo, lineas, dibujo="hornero", subrayar=(), pie=None, marcar_titulo=False):
    """Página de un texto informativo: título arriba, dibujo con su pie a la izquierda y renglones de texto a la derecha.
    subrayar: [(renglón, palabra)] se resalta esa palabra en amarillo. marcar_titulo: recuadro rojo en el título."""
    W = 10.0; H = max(3.6, 1.7 + .62 * len(lineas))
    fig, ax = lienzo(6.8, H * .68, W, H, 0, 0)
    ax.add_patch(FancyBboxPatch((.15, .15), W - .3, H - .3, boxstyle="round,pad=0.05", fc="white", ec=OSC, lw=1.6))
    ax.text(W / 2, H - .55, titulo.upper(), ha="center", va="center", fontsize=17, color=TEAL, zorder=3, **F)
    if marcar_titulo: ax.add_patch(FancyBboxPatch((2.0, H - .95), W - 4, .8, boxstyle="round,pad=0.05", fc="none", ec=CORAL, lw=2.5, zorder=3))
    OBJ2[dibujo](ax, 1.5, H - 2.0, 1.0)
    if pie: ax.text(1.5, H - 2.85, pie.upper(), ha="center", va="center", fontsize=8, color=OSC, style="italic", zorder=3, **F)
    for i, ln in enumerate(lineas):
        y = H - 1.4 - i * .62; x = 3.2
        ax.text(x, y, ln.upper(), ha="left", va="center", fontsize=11, color=OSC, zorder=3, **F)
        for (r, pal) in subrayar:
            if r == i and pal.upper() in ln.upper():
                k = ln.upper().index(pal.upper()); x1 = x + _ancho(fig, ax, ln.upper()[:k]); x2 = x + _ancho(fig, ax, ln.upper()[:k + len(pal)])
                ax.add_patch(Rectangle((x1 - .04, y - .2), x2 - x1 + .08, .4, color="#ffe36b", zorder=2))
    return png(fig)


def ficha(campos, titulo="FICHA"):
    """Ficha para responder por escrito: [("¿QUÉ ES?", "UN PÁJARO"), ("¿DÓNDE VIVE?", "")]. Vacío = renglón para completar."""
    n = len(campos); H = 1.0 + .9 * n
    fig, ax = lienzo(6.8, H * .7, 10, H, 0, 0)
    ax.add_patch(FancyBboxPatch((.15, .15), 9.7, H - .3, boxstyle="round,pad=0.05", fc="#f6fbfb", ec=TEAL, lw=1.8))
    ax.text(5, H - .45, titulo.upper(), ha="center", va="center", fontsize=15, color=TEAL, **F)
    for i, (p, r) in enumerate(campos):
        y = H - 1.2 - i * .9
        ax.text(.5, y, p.upper(), ha="left", va="center", fontsize=11, color=CORAL, **F)
        ax.plot([5.4, 9.5], [y - .22, y - .22], color="#9aa", lw=1.2)
        if r: ax.text(5.5, y, r.upper(), ha="left", va="center", fontsize=11, color=OSC, **F)
    return png(fig)


# ---------------- misión 8 (ficha del yaguareté) y misión 9 (El renacuajo paseador) ----------------
def _yaguarete(ax, x, y, s=1.0):
    ax.add_patch(Ellipse((x - .1 * s, y), 1.1 * s, .5 * s, color="#f2b544", ec=OSC, lw=1.4))
    ax.add_patch(Circle((x + .5 * s, y + .2 * s), .25 * s, color="#f2b544", ec=OSC, lw=1.3))
    for dx in (.36, .62): ax.add_patch(Circle((x + dx * s, y + .42 * s), .07 * s, color="#f2b544", ec=OSC, lw=1))
    ax.add_patch(Circle((x + .58 * s, y + .24 * s), .035 * s, color=OSC))
    for (dx, dy) in ((-.4, .05), (-.15, .12), (.1, -.02), (-.3, -.12), (.0, .15), (.2, .1)):
        ax.add_patch(Circle((x + dx * s, y + dy * s), .055 * s, color="none", ec=OSC, lw=1.4))
    for dx in (-.45, -.25, .1, .3): ax.plot([x + dx * s, x + dx * s], [y - .2 * s, y - .5 * s], color="#d99a2b", lw=4)
    ax.plot([x - .65 * s, x - .9 * s], [y + .05 * s, y + .3 * s], color="#d99a2b", lw=3)


def _rana(ax, x, y, s=1.0):
    ax.add_patch(Ellipse((x, y - .05 * s), .9 * s, .6 * s, color="#7cc576", ec=OSC, lw=1.4))
    for dx in (-.2, .2):
        ax.add_patch(Circle((x + dx * s, y + .28 * s), .13 * s, color="white", ec=OSC, lw=1.2)); ax.add_patch(Circle((x + dx * s, y + .28 * s), .05 * s, color=OSC))
    ax.plot([x - .2 * s, x + .2 * s], [y - .05 * s, y - .05 * s], color=OSC, lw=1.5)


def _renacuajo(ax, x, y, s=1.0):
    ax.add_patch(Circle((x, y), .28 * s, color="#5a8f4e", ec=OSC, lw=1.4))
    ax.plot([x - .25 * s, x - .5 * s, x - .7 * s], [y - .05 * s, y + .08 * s, y - .08 * s], color="#5a8f4e", lw=4)
    ax.add_patch(Circle((x + .1 * s, y + .08 * s), .05 * s, color="white", ec=OSC, lw=1))
    ax.add_patch(Polygon([(x - .2 * s, y + .24 * s), (x + .2 * s, y + .24 * s), (x + .12 * s, y + .45 * s), (x - .12 * s, y + .45 * s)], closed=True, color=OSC))
    ax.add_patch(Rectangle((x - .28 * s, y + .22 * s), .56 * s, .05 * s, color=CORAL))
    ax.add_patch(Polygon([(x + .05 * s, y - .2 * s), (x + .15 * s, y - .2 * s), (x + .1 * s, y - .42 * s)], closed=True, color=CORAL))


def _pato(ax, x, y, s=1.0):
    ax.add_patch(Ellipse((x, y - .05 * s), .8 * s, .5 * s, color="white", ec=OSC, lw=1.4))
    ax.add_patch(Circle((x + .3 * s, y + .2 * s), .18 * s, color="white", ec=OSC, lw=1.2))
    ax.add_patch(Polygon([(x + .5 * s, y + .27 * s), (x + .72 * s, y + .22 * s), (x + .5 * s, y + .17 * s)], closed=True, color=AMBAR, ec=OSC, lw=1))
    ax.add_patch(Circle((x + .38 * s, y + .3 * s), .03 * s, color=OSC))


OBJ2.update({"yaguarete": _yaguarete, "rana": _rana, "renacuajo": _renacuajo, "pato": _pato})


def estrofa(versos, rimas=(), titulo=None):
    """Una estrofa de poema, verso por verso. rimas: [(verso, terminación)] se pinta esa terminación en coral."""
    n = len(versos); H = .8 * n + (1.0 if titulo else .4)
    fig, ax = lienzo(6.8, H * .7, 10, H, 0, 0)
    ax.add_patch(FancyBboxPatch((.15, .15), 9.7, H - .3, boxstyle="round,pad=0.05", fc="#fffaf0", ec=AMBAR, lw=1.8))
    if titulo: ax.text(5, H - .45, titulo.upper(), ha="center", va="center", fontsize=14, color=TEAL, **F)
    for i, v in enumerate(versos):
        y = H - (1.15 if titulo else .55) - i * .8; v = v.upper(); x = .5
        ter = next((t.upper() for (r, t) in rimas if r == i and v.rstrip(".,;!").endswith(t.upper())), None)
        if ter:
            k = v.rstrip(".,;!").rindex(ter); x1 = x + _ancho(fig, ax, v[:k], 12)
            ax.text(x, y, v[:k], ha="left", va="center", fontsize=12, color=OSC, zorder=3, **F)
            ax.text(x1, y, v[k:], ha="left", va="center", fontsize=12, color=CORAL, zorder=3, **F)
        else:
            ax.text(x, y, v, ha="left", va="center", fontsize=12, color=OSC, zorder=3, **F)
    return png(fig)
