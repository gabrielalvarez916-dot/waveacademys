# -*- coding: utf-8 -*-
"""Figura de la lección 2 (Misión 2): rectángulo de 12 × 17 partido en 12 × 10 y 12 × 7."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

VERDE, OSCURO, CLARO = "#0e7c7b", "#243b3f", "#d8f0ea"
fig, ax = plt.subplots(figsize=(6.4, 3.4), dpi=130)
ax.set_xlim(-2.2, 18.2); ax.set_ylim(-2.6, 13.6); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 10, 12, facecolor=CLARO, edgecolor=OSCURO, lw=1.6))
ax.add_patch(Rectangle((10, 0), 7, 12, facecolor="#b9e3d9", edgecolor=OSCURO, lw=1.6))
for x in range(1, 17):
    ax.plot([x, x], [0, 12], color="white", lw=0.5, zorder=1)
for y in range(1, 12):
    ax.plot([0, 17], [y, y], color="white", lw=0.5, zorder=1)
ax.add_patch(Rectangle((0, 0), 17, 12, fill=False, edgecolor=OSCURO, lw=2))
ax.plot([10, 10], [0, 12], color=VERDE, lw=2.4)
ax.text(5, 6, "12 × 10\n= 120", ha="center", va="center", fontsize=13, color=OSCURO, weight="bold")
ax.text(13.5, 6, "12 × 7\n= 84", ha="center", va="center", fontsize=13, color=OSCURO, weight="bold")
ax.text(5, -1.3, "10", ha="center", fontsize=12, color=VERDE, weight="bold")
ax.text(13.5, -1.3, "7", ha="center", fontsize=12, color=VERDE, weight="bold")
ax.text(8.5, 12.8, "17 = 10 + 7", ha="center", fontsize=12, color=OSCURO)
ax.text(-1.2, 6, "12", ha="center", va="center", fontsize=12, color=VERDE, weight="bold")
fig.savefig("distributiva.png", bbox_inches="tight", facecolor="white")
print("ok")
