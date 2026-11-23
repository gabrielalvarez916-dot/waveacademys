# -*- coding: utf-8 -*-
"""Dibujos para los PDF de Lengua 1 (Nivel Medio, primeros años): carteles de nombres, letras y listas.
Todo en IMPRENTA MAYÚSCULA. Usa la base de dibujo de Matemática 1 (png, lienzo, colores)."""
import os, importlib.util
_s = importlib.util.spec_from_file_location('figuras_mat1', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'matematica-1', 'figuras.py'))
_B = importlib.util.module_from_spec(_s); _s.loader.exec_module(_B)
png, lienzo, cartel, FancyBboxPatch, F = _B.png, _B.lienzo, _B.cartel, _B.FancyBboxPatch, _B.F
TEAL, OSC, MENTA, AMBAR, CORAL, VERDE, AZUL, LILA = _B.TEAL, _B.OSC, _B.MENTA, _B.AMBAR, _B.CORAL, _B.VERDE, _B.AZUL, _B.LILA
OBJ, juntar, parejas = _B.OBJ, _B.juntar, _B.parejas

COLS = [TEAL, CORAL, AZUL, LILA, VERDE, AMBAR]


def nombres(lista, resaltar_inicial=False, cols=3):
    """Carteles de nombres (como los del aula). resaltar_inicial: la primera letra en otro color.
    El cartel se ensancha solo si hay palabras largas, para que ninguna quede afuera del recuadro."""
    W = max(2.6, .29 * max(len(str(x)) for x in lista) + .7); P = W + .3
    if W > 2.6: cols = min(cols, max(2, int(8.8 // P)))  # si los carteles son anchos, van menos por fila (así no se achica todo el dibujo)
    n = len(lista); filas = (n + cols - 1) // cols; c = min(n, cols)
    fig, ax = lienzo(P * c, 1.35 * filas, P * c, 1.35 * filas, 0, 0)
    for i, nom in enumerate(lista):
        x, y = P * (i % cols) + .15, 1.35 * (filas - 1 - i // cols) + .15
        ax.add_patch(FancyBboxPatch((x, y), W, 1.05, boxstyle="round,pad=0.02,rounding_size=0.15", color="white", ec=COLS[i % len(COLS)], lw=2.4))
        if resaltar_inicial:
            t0 = nom.upper(); w = .22 * len(t0); x0 = x + W / 2 - w / 2
            ax.text(x0, y + .52, t0[0], ha="left", va="center", fontsize=20, color=CORAL, **F)
            ax.text(x0 + .26, y + .52, t0[1:], ha="left", va="center", fontsize=20, color=OSC, **F)
        else:
            ax.text(x + W / 2, y + .52, nom.upper(), ha="center", va="center", fontsize=20, color=OSC, **F)
    return png(fig)


def letras(palabra, ocultar=(), numeros=False, resaltar=()):
    """Una palabra con cada letra en su casillero. ocultar: posiciones en blanco. numeros: número de orden debajo. resaltar: posiciones en amarillo."""
    p = palabra.upper(); n = len(p)
    fig, ax = lienzo(1.15 * n + .3, 1.9 if numeros else 1.4, 1.15 * n + .3, 1.9 if numeros else 1.4, 0, -.5 if numeros else 0)
    for i, ch in enumerate(p):
        x = .15 + 1.15 * i
        ax.add_patch(FancyBboxPatch((x, .15), 1.0, 1.1, boxstyle="round,pad=0.02,rounding_size=0.12", color="#ffe39a" if i in resaltar else MENTA, ec=AMBAR if i in resaltar else TEAL, lw=2))
        ax.text(x + .5, .7, "" if i in ocultar else ch, ha="center", va="center", fontsize=28, color=OSC, **F)
        if numeros: ax.text(x + .5, -.2, str(i + 1), ha="center", va="center", fontsize=12, color=TEAL, **F)
    return png(fig)


def lista(nombres_, titulo="LISTA DEL GRADO", marcar=()):
    """Lista numerada de nombres; marcar: posiciones resaltadas."""
    n = len(nombres_)
    fig, ax = lienzo(4.2, .62 * n + 1.1, 4.2, .62 * n + 1.1, 0, 0)
    ax.add_patch(FancyBboxPatch((.1, .1), 4.0, .62 * n + .9, boxstyle="round,pad=0.02,rounding_size=0.12", color="#fffdf2", ec=OSC, lw=1.6))
    ax.text(2.1, .62 * n + .62, titulo.upper(), ha="center", va="center", fontsize=14, color=TEAL, **F)
    for i, nom in enumerate(nombres_):
        y = .62 * (n - i) - .15
        if i in marcar: ax.add_patch(FancyBboxPatch((.35, y - .24), 3.5, .48, boxstyle="round,pad=0.02,rounding_size=0.1", color="#fff0c2", ec=AMBAR, lw=1.4))
        ax.text(.6, y, f"{i + 1}.", ha="left", va="center", fontsize=14, color=OSC, **F)
        ax.text(1.2, y, nom.upper(), ha="left", va="center", fontsize=15, color=OSC, **F)
    return png(fig)


def dibujo_palabra(pares, resaltar=None):
    """Dibujos con su palabra debajo: [("pelota", "PELOTA"), ...]. resaltar: letra que se pinta en rojo en cada palabra (ej. "P")."""
    n = len(pares); fig, ax = lienzo(2.4 * n, 2.6, 2.4 * n, 2.6, 0, 0)
    for i, (obj, pal) in enumerate(pares):
        x = 2.4 * i + 1.2
        OBJ[obj](ax, x, 1.75)
        pal = pal.upper(); w = .2 * len(pal); x0 = x - w / 2 * 1.0
        if resaltar:
            for j, ch in enumerate(pal):
                ax.text(x - .2 * (len(pal) - 1) / 2 * 1.0 + .2 * j * 1.0, .45, ch, ha="center", va="center", fontsize=16, color=CORAL if ch == resaltar else OSC, **F)
        else:
            ax.text(x, .45, pal, ha="center", va="center", fontsize=16, color=OSC, **F)
    return png(fig)


def tiras(textos, numeros=True, ocultar_num=False, cols=2):
    """Tiras de un cuento: cuadros con una frase corta y su número (1, 2, 3…). ocultar_num: el número en blanco (para ordenar)."""
    n = len(textos); filas = (n + cols - 1) // cols; c = min(n, cols)
    fig, ax = lienzo(4.4 * c, 1.7 * filas, 4.4 * c, 1.7 * filas, 0, 0)
    for i, t in enumerate(textos):
        x, y = 4.4 * (i % cols) + .15, 1.7 * (filas - 1 - i // cols) + .15
        ax.add_patch(FancyBboxPatch((x, y), 4.1, 1.4, boxstyle="round,pad=0.02,rounding_size=0.15", color="#fffdf2", ec=COLS[i % len(COLS)], lw=2.2))
        if numeros: ax.text(x + .35, y + 1.05, "_" if ocultar_num else str(i + 1), ha="center", va="center", fontsize=15, color=CORAL, **F)
        ax.text(x + 2.05, y + .62, t.upper(), ha="center", va="center", fontsize=13, color=OSC, **F)
    return png(fig)
