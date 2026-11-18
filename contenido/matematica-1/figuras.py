# -*- coding: utf-8 -*-
"""Figuras de las misiones 8, 11, 14 y 17 de Matemática I. Las dibuja y las agrega como bloques de imagen
(png_base64) en mision-N.json. Uso: python3 figuras.py"""
import io, json, base64, math, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from PIL import Image

V, O, C = "#0e7c7b", "#243b3f", "#d8f0ea"
AQUI = os.path.dirname(os.path.abspath(__file__))

def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=16)
    o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()

def lienzo(w, h):
    fig, ax = plt.subplots(figsize=(w, h)); ax.set_aspect("equal"); ax.axis("off"); return fig, ax

def recta(ax, a, b, marcas, etiquetas, y=0):
    ax.annotate("", xy=(b + 0.4, y), xytext=(a - 0.4, y), arrowprops=dict(arrowstyle="<->", color=O, lw=1.6))
    for x, t in zip(marcas, etiquetas):
        ax.plot([x, x], [y - 0.12, y + 0.12], color=O, lw=1.4)
        ax.text(x, y - 0.42, t, ha="center", fontsize=11, color=O)

def fig_recta_enteros():
    fig, ax = lienzo(7, 1.8); ax.set_xlim(-6, 6); ax.set_ylim(-1, 1.3)
    recta(ax, -5, 5, range(-5, 6), [str(i).replace("-", "−") for i in range(-5, 6)])
    for x in (-3, 4): ax.plot(x, 0, "o", color=V, ms=9)
    ax.annotate("", xy=(0, 0.55), xytext=(-3, 0.55), arrowprops=dict(arrowstyle="<->", color=V, lw=1.6))
    ax.annotate("", xy=(4, 0.55), xytext=(0, 0.55), arrowprops=dict(arrowstyle="<->", color=O, lw=1.6))
    ax.text(-1.5, 0.75, "3", ha="center", fontsize=12, color=V, weight="bold")
    ax.text(2, 0.75, "4", ha="center", fontsize=12, color=O, weight="bold")
    return png(fig)

def fig_recta_sextos():
    fig, ax = lienzo(7, 1.6); ax.set_xlim(-0.3, 6.6); ax.set_ylim(-1, 1.1)
    recta(ax, 0, 6, range(7), ["0", "1/6", "2/6", "3/6", "4/6", "5/6", "1"])
    for x, t in ((4, "2/3"), (5, "5/6")):
        ax.plot(x, 0, "o", color=V, ms=9); ax.text(x, 0.35, t, ha="center", fontsize=12, color=V, weight="bold")
    return png(fig)

def fig_grafico_directa():
    fig, ax = plt.subplots(figsize=(5, 3.4))
    xs, ys = [1, 2, 3, 5], [800, 1600, 2400, 4000]
    ax.plot([0, 5.5], [0, 4400], "--", color=V, lw=1.2); ax.plot(xs, ys, "o", color=O, ms=8)
    for x, y in zip(xs, ys): ax.text(x + 0.12, y - 330, f"({x}; {y:,})".replace(",", "."), fontsize=9, color=O)
    ax.plot(0, 0, "o", color=V, ms=7); ax.set_xlim(0, 6); ax.set_ylim(0, 4600)
    ax.set_xlabel("Kilos de pan", color=O); ax.set_ylabel("Precio ($)", color=O)
    ax.spines[["top", "right"]].set_visible(False); ax.grid(alpha=0.25)
    return png(fig)

def fig_angulos_cruzados():
    fig, ax = lienzo(5, 3.2); ax.set_xlim(-3.2, 3.2); ax.set_ylim(-2.2, 2.2)
    t = math.radians(65)
    ax.plot([-3, 3], [0, 0], color=O, lw=2); ax.plot([-2.2 * math.cos(t) * 1.1, 2.2 * math.cos(t) * 1.1], [-2.2 * math.sin(t) * 1.1, 2.2 * math.sin(t) * 1.1], color=O, lw=2)
    for a1, a2, txt, r, col in ((0, 65, "65°", 0.7, V), (65, 180, "115°", 0.55, O), (180, 245, "65°", 0.7, V), (245, 360, "115°", 0.55, O)):
        ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=a1, theta2=a2, color=col, lw=1.6))
        m = math.radians((a1 + a2) / 2); ax.text(1.15 * math.cos(m), 1.15 * math.sin(m), txt, ha="center", va="center", fontsize=12, color=col, weight="bold")
    return png(fig)

def fig_posiciones():
    fig, axs = plt.subplots(1, 3, figsize=(8, 2.6))
    for ax, tit in zip(axs, ("Paralelas", "Perpendiculares", "Secantes")):
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-2, 2); ax.set_ylim(-1.6, 1.6); ax.set_title(tit, color=O, fontsize=12)
    axs[0].plot([-1.8, 1.8], [0.6, 0.6], color=O, lw=2); axs[0].plot([-1.8, 1.8], [-0.6, -0.6], color=O, lw=2)
    axs[0].annotate("", xy=(0, 0.6), xytext=(0, -0.6), arrowprops=dict(arrowstyle="<->", color=V, lw=1.4)); axs[0].text(0.15, 0, "distancia", color=V, fontsize=9, va="center")
    axs[1].plot([-1.8, 1.8], [0, 0], color=O, lw=2); axs[1].plot([0, 0], [-1.5, 1.5], color=O, lw=2)
    axs[1].plot([0, 0.3, 0.3], [0.3, 0.3, 0], color=V, lw=1.6); axs[1].text(0.4, 0.45, "90°", color=V, fontsize=11)
    axs[2].plot([-1.8, 1.8], [-0.4, 0.4], color=O, lw=2); axs[2].plot([-1.2, 1.2], [1.4, -1.4], color=O, lw=2)
    return png(fig)

def fig_bisectriz():
    fig, ax = lienzo(5, 3.4); ax.set_xlim(-0.3, 4.6); ax.set_ylim(-0.4, 4)
    a = math.radians(70); u = (math.cos(a), math.sin(a)); b = math.radians(35)
    ax.plot([0, 4.4], [0, 0], color=O, lw=2); ax.plot([0, 4.2 * u[0]], [0, 4.2 * u[1]], color=O, lw=2)
    r1 = 2.0; P1 = (r1, 0); P2 = (r1 * u[0], r1 * u[1]); r2 = 1.8
    ax.add_patch(Arc((0, 0), 2 * r1, 2 * r1, theta1=-5, theta2=75, color=V, lw=1.2, ls="--"))
    half = math.dist(P1, P2) / 2; mid = ((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2)
    d = math.hypot(*mid) + math.sqrt(r2 ** 2 - half ** 2); Q = (d * math.cos(b), d * math.sin(b))
    for P in (P1, P2):
        ang = math.degrees(math.atan2(Q[1] - P[1], Q[0] - P[0])); ax.add_patch(Arc(P, 2 * r2, 2 * r2, theta1=ang - 15, theta2=ang + 15, color=V, lw=1.2, ls="--"))
        ax.plot(*P, "o", color=V, ms=5)
    ax.plot([0, 4.2 * math.cos(b)], [0, 4.2 * math.sin(b)], color=V, lw=2.4); ax.plot(*Q, "o", color=O, ms=6)
    ax.text(-0.25, -0.3, "O", fontsize=12, color=O); ax.text(4.2 * math.cos(b) + 0.05, 4.2 * math.sin(b), "bisectriz", color=V, fontsize=11)
    return png(fig)

def fig_mediatriz():
    fig, ax = lienzo(5, 3.6); ax.set_xlim(-1, 7); ax.set_ylim(-3.6, 3.6)
    ax.plot([0, 6], [0, 0], color=O, lw=2.2); ax.plot([0, 6], [0, 0], "o", color=O, ms=6)
    ax.text(-0.5, -0.45, "A", fontsize=12, color=O); ax.text(6.2, -0.45, "B", fontsize=12, color=O)
    y = math.sqrt(16 - 9)
    for cx, s in ((0, 1), (6, -1)):
        for sy in (1, -1):
            ang = math.degrees(math.atan2(sy * y, 3 - cx)); ax.add_patch(Arc((cx, 0), 8, 8, theta1=ang - 14, theta2=ang + 14, color=V, lw=1.2, ls="--"))
    ax.plot([3, 3], [-3.4, 3.4], color=V, lw=2.4); ax.plot([3, 3], [y, -y], "o", color=O, ms=5)
    ax.plot([3, 3.3, 3.3], [0.3, 0.3, 0], color=O, lw=1.2); ax.text(3.15, 3.0, "mediatriz", color=V, fontsize=11)
    ax.text(1.3, -0.5, "3 cm", fontsize=10, color=O); ax.text(4.3, -0.5, "3 cm", fontsize=10, color=O)
    return png(fig)

def fig_triangulo():
    fig, ax = lienzo(5.2, 3.6); ax.set_xlim(-0.8, 6.8); ax.set_ylim(-0.8, 4.4)
    A, B = (0, 0), (6, 0); cx = 45 / 12; Cp = (cx, math.sqrt(25 - cx ** 2))
    for P, r in ((A, 5), (B, 4)):
        ang = math.degrees(math.atan2(Cp[1] - P[1], Cp[0] - P[0])); ax.add_patch(Arc(P, 2 * r, 2 * r, theta1=ang - 18, theta2=ang + 18, color=V, lw=1.3, ls="--"))
    ax.plot([A[0], B[0], Cp[0], A[0]], [A[1], B[1], Cp[1], A[1]], color=O, lw=2.2)
    for P, t, dx, dy in ((A, "A", -0.45, -0.4), (B, "B", 0.15, -0.4), (Cp, "C", 0.0, 0.2)):
        ax.plot(*P, "o", color=O, ms=5); ax.text(P[0] + dx, P[1] + dy, t, fontsize=12, color=O)
    ax.text(3, -0.55, "6 cm", ha="center", fontsize=11, color=O)
    ax.text(1.4, 1.95, "5 cm", fontsize=11, color=V, weight="bold"); ax.text(5.05, 1.7, "4 cm", fontsize=11, color=V, weight="bold")
    return png(fig)

def img(titulo, pie, desc, b64):
    return {"tipo": "imagen", "imagen_tipo": "diagrama", "titulo": titulo, "texto": pie, "imagen_descripcion": desc, "imagen_fuente": "Dibujo propio (matplotlib).", "png_base64": b64}

# (misión, nivel, sección, bloque) -> se agrega al final de la sección
AGREGAR = [
 (8, "3", 0, img("Sextos en la recta", "Con la unidad dividida en 6, 2/3 = 4/6 queda un sexto antes que 5/6.", "Recta de 0 a 1 dividida en sextos, con 2/3 (4/6) y 5/6 marcados.", fig_recta_sextos())),
 (11, "2", 2, img("De −3 a 4", "Se cuentan 3 unidades hasta el 0 y 4 más: la distancia es 7.", "Recta entera de −5 a 5 con −3 y 4 marcados y las distancias 3 y 4 hasta el cero.", fig_recta_enteros())),
 (14, "2", 1, img("Kilos de pan y precio", "Los puntos están alineados y la recta pasa por el origen: es proporcionalidad directa.", "Gráfico con los puntos (1; 800), (2; 1.600), (3; 2.400) y (5; 4.000) sobre una recta que pasa por (0; 0).", fig_grafico_directa())),
 (17, "1", 2, img("Dos rectas que se cortan", "Los opuestos por el vértice son iguales (65° y 65°; 115° y 115°) y los vecinos suman 180°.", "Dos rectas que se cortan formando ángulos de 65°, 115°, 65° y 115°.", fig_angulos_cruzados())),
 (17, "2", 0, img("Posiciones de dos rectas", "Las paralelas no se cortan; las perpendiculares forman 90°; las secantes se cortan en un punto.", "Tres dibujos: dos rectas paralelas con su distancia, dos perpendiculares con el ángulo recto marcado y dos secantes.", fig_posiciones())),
 (17, "3", 0, img("Construcción de la bisectriz", "Arco desde el vértice, dos arcos iguales desde los cortes y se une O con el cruce.", "Ángulo de 70° con vértice O, los arcos de la construcción y la bisectriz que lo divide en dos de 35°.", fig_bisectriz())),
 (17, "3", 1, img("Construcción de la mediatriz", "Arcos de igual abertura desde A y desde B; la recta que une los cruces es perpendicular en el punto medio.", "Segmento AB de 6 cm, arcos desde A y B y la mediatriz perpendicular que pasa por el punto medio.", fig_mediatriz())),
 (17, "4", 1, img("Triángulo de 6, 5 y 4 cm", "Sobre AB de 6 cm, arco de 5 cm desde A y de 4 cm desde B: se cortan en C.", "Triángulo ABC con AB = 6 cm, AC = 5 cm y BC = 4 cm, con los arcos de la construcción.", fig_triangulo())),
]
for m, n, s, b in AGREGAR:
    ruta = os.path.join(AQUI, f"mision-{m}", f"mision-{m}.json")
    M = json.load(open(ruta)); sec = M["niveles"][n]["secciones"][s]
    sec["bloques"] = [x for x in sec["bloques"] if not (x.get("tipo") == "imagen" and x.get("titulo") == b["titulo"])] + [b]
    json.dump(M, open(ruta, "w"), ensure_ascii=False)
print("ok", len(AGREGAR), "figuras")
