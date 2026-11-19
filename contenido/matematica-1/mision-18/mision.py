# -*- coding: utf-8 -*-
"""Matemática I · Misión 18 · Triángulos y cuadriláteros: propiedades. Genera mision-18.json (se carga con cargar_mision).
Incluye las figuras (matplotlib, colores de Wave) como bloques de imagen con png_base64."""
import os, sys, io, math, base64, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon
from PIL import Image

V, O, C = "#0e7c7b", "#243b3f", "#d8f0ea"
def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=16)
    o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()
def IMG(t, pie, desc, b64): return {"tipo":"imagen","imagen_tipo":"diagrama","titulo":t,"texto":pie,"imagen_descripcion":desc,"imagen_fuente":"Dibujo propio (matplotlib).","png_base64":b64}
def poli(ax, pts, fill=C):
    ax.add_patch(Polygon(pts, closed=True, facecolor=fill, edgecolor=O, lw=2))
def marca(ax, p, q, n=1):  # marquitas de lados iguales
    mx, my = (p[0]+q[0])/2, (p[1]+q[1])/2; dx, dy = q[0]-p[0], q[1]-p[1]; L = math.hypot(dx, dy); nx, ny = -dy/L, dx/L; ux, uy = dx/L, dy/L
    for k in range(n):
        o = (k - (n-1)/2) * 0.12
        ax.plot([mx+ux*o-nx*0.13, mx+ux*o+nx*0.13], [my+uy*o-ny*0.13, my+uy*o+ny*0.13], color=V, lw=2)

def fig_tipos_lados():
    fig, axs = plt.subplots(1, 3, figsize=(8, 2.6))
    datos = [("Equilátero", [(0,0),(2,0),(1,1.73)], [(0,1,1),(1,2,1),(2,0,1)]), ("Isósceles", [(0,0),(2,0),(1,2.2)], [(1,2,2),(2,0,2)]), ("Escaleno", [(0,0),(2.4,0),(0.6,1.5)], [])]
    for ax, (tit, P, ms) in zip(axs, datos):
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-0.3, 2.7); ax.set_ylim(-0.3, 2.4); ax.set_title(tit, color=O, fontsize=12)
        poli(ax, P)
        for a, b, n in ms: marca(ax, P[a], P[b], n)
    return png(fig)

def fig_exterior():
    fig, ax = plt.subplots(figsize=(5.4, 3.4)); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-0.6, 7.2); ax.set_ylim(-0.7, 4.2)
    A, B = (0, 0), (4.5, 0); bb = 4.5 * math.sin(math.radians(70)) / math.sin(math.radians(60)); Cp = (bb * math.cos(math.radians(50)), bb * math.sin(math.radians(50)))
    poli(ax, [A, B, Cp]); ax.plot([4.5, 6.9], [0, 0], color=O, lw=2, ls="--")
    for P, a1, a2, txt, d in ((A, 0, 50, "50°", 0.95), (Cp, 230, 290, "60°", 0.8), (B, 110, 180, "70°", 0.8)):
        ax.add_patch(Arc(P, 0.9, 0.9, theta1=a1, theta2=a2, color=O, lw=1.4)); m = math.radians((a1+a2)/2); ax.text(P[0]+d*math.cos(m), P[1]+d*math.sin(m), txt, ha="center", va="center", fontsize=11, color=O)
    ax.add_patch(Arc(B, 1.3, 1.3, theta1=0, theta2=110, color=V, lw=2)); ax.text(B[0]+0.95, 0.85, "110°", fontsize=12, color=V, weight="bold")
    ax.text(5.0, -0.5, "exterior = 50° + 60°", fontsize=10, color=V)
    return png(fig)

def fig_paralelogramos():
    fig, axs = plt.subplots(1, 5, figsize=(9.5, 2.4))
    datos = [("Paralelogramo", [(0,0),(2,0),(2.6,1.2),(0.6,1.2)]), ("Rectángulo", [(0,0),(2.4,0),(2.4,1.3),(0,1.3)]), ("Rombo", [(1.2,0),(2.4,0.9),(1.2,1.8),(0,0.9)]),
             ("Cuadrado", [(0.3,0),(1.9,0),(1.9,1.6),(0.3,1.6)]), ("Trapecio", [(0,0),(2.6,0),(1.9,1.3),(0.6,1.3)])]
    for ax, (tit, P) in zip(axs, datos):
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-0.2, 2.8); ax.set_ylim(-0.2, 2.0); ax.set_title(tit, color=O, fontsize=10.5)
        poli(ax, P, C if tit != "Trapecio" else "#eef3f3")
    return png(fig)

def fig_diagonales():
    fig, axs = plt.subplots(1, 3, figsize=(8, 2.8))
    datos = [("Rectángulo: iguales", [(0,0),(2.6,0),(2.6,1.6),(0,1.6)], False), ("Rombo: perpendiculares", [(1.3,0),(2.5,1),(1.3,2),(0.1,1)], True), ("Cuadrado: las dos cosas", [(0.3,0),(2.1,0),(2.1,1.8),(0.3,1.8)], True)]
    for ax, (tit, P, perp) in zip(axs, datos):
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-0.2, 2.8); ax.set_ylim(-0.2, 2.2); ax.set_title(tit, color=O, fontsize=11)
        poli(ax, P); ax.plot([P[0][0], P[2][0]], [P[0][1], P[2][1]], color=V, lw=2); ax.plot([P[1][0], P[3][0]], [P[1][1], P[3][1]], color=V, lw=2)
        cx, cy = (P[0][0]+P[2][0])/2, (P[0][1]+P[2][1])/2; ax.plot(cx, cy, "o", color=O, ms=5)
        if perp:
            a = math.atan2(P[2][1]-P[0][1], P[2][0]-P[0][0]); u = (math.cos(a)*0.2, math.sin(a)*0.2); w = (-u[1], u[0])
            ax.plot([cx+u[0], cx+u[0]+w[0], cx+w[0]], [cy+u[1], cy+u[1]+w[1], cy+w[1]], color=O, lw=1.2)
    return png(fig)

NO=["no"]; SI=["si","sí"]
N1={
"objetivo":"Vas a poder clasificar triángulos según sus lados y según sus ángulos, y decidir si tres medidas forman un triángulo.",
"vas_a_ver":["Triángulos según sus lados","Triángulos según sus ángulos","Un triángulo, dos nombres","La desigualdad triangular","Construir según los datos"],
"secciones":[
 S(1,"Según sus lados",[
  D("Clasificación por lados","Un triángulo es <b>equilátero</b> si tiene los <b>tres lados iguales</b>, <b>isósceles</b> si tiene <b>dos lados iguales</b> y <b>escaleno</b> si tiene los <b>tres lados distintos</b>."),
  T("Mirando las medidas",["Lados","Iguales","Es"],[["5, 5 y 5 cm","los tres","Equilátero"],["5, 5 y 3 cm","dos","Isósceles"],["4, 5 y 6 cm","ninguno","Escaleno"]],"Se cuenta cuántos lados miden lo mismo."),
  IMG("Triángulos según sus lados","Las marquitas indican los lados iguales.","Un triángulo equilátero, uno isósceles y uno escaleno, con marcas en los lados iguales.",fig_tipos_lados()),
 ]),
 S(1,"Según sus ángulos",[
  D("Clasificación por ángulos","Un triángulo es <b>acutángulo</b> si sus <b>tres ángulos son agudos</b>, <b>rectángulo</b> si tiene <b>un ángulo recto</b> y <b>obtusángulo</b> si tiene <b>un ángulo obtuso</b>."),
  E("Tres triángulos","Miramos el ángulo más grande.",["60°, 60° y 60°: todos agudos, es acutángulo.","90°, 45° y 45°: tiene uno recto, es rectángulo.","120°, 30° y 30°: tiene uno obtuso, es obtusángulo."]),
 ]),
 S(2,"Un triángulo, dos nombres",[
  P("Todo triángulo tiene <b>un nombre por sus lados y otro por sus ángulos</b>, al mismo tiempo. El de 90°, 45° y 45° tiene dos lados iguales: es <b>rectángulo isósceles</b>. Uno con ángulos de 100°, 50° y 30° y los tres lados distintos es <b>obtusángulo escaleno</b>."),
  E("Nombre completo","Lados 6, 6 y 6 cm.",["Por sus lados: los tres iguales, equilátero.","Por sus ángulos: cada uno mide 60°, todos agudos, acutángulo.","Nombre completo: equilátero acutángulo."]),
 ]),
 S(2,"La desigualdad triangular",[
  P("No con cualquier medida se arma un triángulo. <b>Cada lado tiene que ser menor que la suma de los otros dos</b>. Alcanza con mirar el lado más largo: si es menor que la suma de los otros dos, se puede."),
  E("¿Se puede?","Probamos el lado más largo.",["3, 4 y 8 cm: 3 + 4 = 7, menor que 8. No se puede.","5, 6 y 9 cm: 5 + 6 = 11, mayor que 9. Se puede.","2, 3 y 5 cm: 2 + 3 = 5, igual a 5. No se puede: los lados quedan acostados."]),
 ]),
],
"ejemplo_completo":{"titulo":"lados de 5, 5 y 8 cm","planteo":"¿Se puede construir un triángulo con lados de 5, 5 y 8 cm? Si se puede, clasificalo por sus lados y por sus ángulos (su ángulo mayor mide unos 106°).","pasos":["Lado más largo: 8. Suma de los otros: 5 + 5 = 10.","8 es menor que 10: se puede construir.","Tiene dos lados iguales: es isósceles.","Su ángulo mayor, de unos 106°, es obtuso: es obtusángulo.","Nombre completo: isósceles obtusángulo."]},
"ejemplo_incompleto":{"titulo":"lados de 7, 7 y 7 cm","planteo":"Completá los espacios.","pasos":["7 es menor que 7 + 7 = ___ : se puede.","Los tres lados son iguales: es ___ .","Cada ángulo mide 60°: es ___ ."]},
"ejemplo_solo":{"titulo":"4, 6 y 11 cm","planteo":"¿Se puede construir un triángulo con lados de 4, 6 y 11 cm? Justificá."},
"tip":{"titulo":"Empezá por el más largo","texto":"Para la desigualdad triangular no hace falta probar los tres lados: si el más largo es menor que la suma de los otros dos, ya está."},
"ojo":["Creer que un triángulo tiene un solo nombre: siempre tiene uno por lados y otro por ángulos.","Aceptar tres medidas sin probar: con 3, 4 y 8 cm no hay triángulo."],
"resumen":[{"titulo":"Por lados","texto":"Equilátero, isósceles, escaleno."},{"titulo":"Por ángulos","texto":"Acutángulo, rectángulo, obtusángulo."},{"titulo":"Dos nombres","texto":"90°, 45°, 45°: rectángulo isósceles."},{"titulo":"Desigualdad","texto":"El lado mayor, menor que la suma de los otros."}],
"glosario":[{"palabra":"Equilátero","significado":"Con los tres lados iguales."},{"palabra":"Isósceles","significado":"Con dos lados iguales."},{"palabra":"Escaleno","significado":"Con los tres lados distintos."},{"palabra":"Acutángulo","significado":"Con los tres ángulos agudos."},{"palabra":"Obtusángulo","significado":"Con un ángulo obtuso."},{"palabra":"Desigualdad triangular","significado":"Regla que dice si tres medidas forman un triángulo."}],
"carpeta":["Un triángulo tiene lados de 8, 8 y 5 cm. ¿Cómo se clasifica según sus lados?","Un triángulo tiene ángulos de 90°, 35° y 55°. ¿Cómo se clasifica según sus ángulos?","¿Se puede construir un triángulo con lados de 3, 5 y 9 cm? Respondé sí o no.","Un compañero dice que un triángulo equilátero no puede ser acutángulo. ¿Cuántos grados mide cada ángulo de un equilátero?"],
"respuestas_carpeta":[["isosceles","isósceles"],["rectangulo","rectángulo"],NO,["60","60°"]],
"soluciones":{"incompleto":"14. Equilátero. Acutángulo.","solo":"No: 4 + 6 = 10, que es menor que 11.","carpeta":["Isósceles: tiene dos lados iguales.","Rectángulo: tiene un ángulo de 90°.","No: 3 + 5 = 8, menor que 9.","60°: los tres ángulos son agudos, así que el equilátero siempre es acutángulo."]}
}
N2={
"objetivo":"Vas a poder usar que los ángulos interiores de un triángulo suman 180° y la propiedad del ángulo exterior para calcular ángulos que faltan.",
"vas_a_ver":["Los ángulos interiores suman 180°","Calcular el ángulo que falta","El ángulo exterior","Isósceles y equiláteros","Ángulos con ecuaciones"],
"secciones":[
 S(1,"La suma es 180°",[
  D("Suma de los ángulos interiores","En <b>todo triángulo</b>, los tres ángulos interiores <b>suman 180°</b>."),
  P("Si recortás las tres puntas de un triángulo de papel y las juntás por el vértice, forman un ángulo llano: 180°. Ejemplo: 50° + 60° + 70° = 180°."),
 ]),
 S(1,"El ángulo que falta",[
  D("Calcular un ángulo","Si conocés dos ángulos, el tercero es <b>180° menos la suma de los otros dos</b>."),
  E("Ángulos de 45° y 75°","Sumamos y restamos de 180°.",["45° + 75° = 120°.","180° − 120° = 60°.","El tercer ángulo mide 60°."]),
 ]),
 S(2,"El ángulo exterior",[
  P("Si se prolonga un lado, se forma un <b>ángulo exterior</b>: es el adyacente a un ángulo interior, así que suman 180°. Además, el exterior es igual a la <b>suma de los dos interiores que no están pegados a él</b>."),
  IMG("Ángulo exterior","Junto al 70° se forma un exterior de 110°, que es 50° + 60°.","Triángulo con ángulos de 50°, 60° y 70° y el ángulo exterior de 110° marcado al prolongar un lado.",fig_exterior()),
  E("Interiores de 50°, 60° y 70°","Exterior junto al de 70°.",["Por adyacente: 180° − 70° = 110°.","Por la propiedad: 50° + 60° = 110°.","Las dos cuentas dan lo mismo."]),
 ]),
 S(2,"Isósceles y equiláteros",[
  P("En el <b>equilátero</b> los tres ángulos son iguales: 180° ÷ 3 = 60°. En el <b>isósceles</b>, los dos ángulos que están frente a los lados iguales son iguales."),
  E("Isósceles con un ángulo desigual de 40°","Lo que queda se reparte entre los dos iguales.",["180° − 40° = 140°.","140° ÷ 2 = 70°.","Los ángulos miden 40°, 70° y 70°."]),
 ]),
 S(2,"Con ecuaciones",[
  P("Si los ángulos se dan con letras, se plantea que suman 180°. Con x, 2x y 3x: x + 2x + 3x = 180, o sea 6x = 180 y x = 30. Los ángulos miden 30°, 60° y 90°."),
 ]),
],
"ejemplo_completo":{"titulo":"el isósceles de 36°","planteo":"En un triángulo isósceles, el ángulo desigual mide 36°. ¿Cuánto miden los otros dos?","pasos":["Los otros dos ángulos son iguales.","Entre los dos suman 180° − 36° = 144°.","Cada uno mide 144° ÷ 2 = 72°.","Verificación: 36° + 72° + 72° = 180°."]},
"ejemplo_incompleto":{"titulo":"ángulos de 48° y 67°","planteo":"Completá los espacios para hallar el tercer ángulo.","pasos":["48° + 67° = ___ .","180° − 115° = ___ ."]},
"ejemplo_solo":{"titulo":"x, x + 20 y 2x","planteo":"Los ángulos de un triángulo miden x, x + 20° y 2x. ¿Cuánto vale x?"},
"tip":{"titulo":"Verificá sumando","texto":"Cuando termines, sumá los tres ángulos: si no da 180°, hay un error de cuenta."},
"ojo":["Confundir ángulo interior con exterior: el exterior está afuera, pegado a un lado prolongado.","Olvidar que la suma es 180° y restar de 360°."],
"resumen":[{"titulo":"Suma","texto":"Los interiores suman 180°."},{"titulo":"El que falta","texto":"180° − la suma de los otros dos."},{"titulo":"Exterior","texto":"Suma de los dos interiores no pegados."},{"titulo":"Equilátero","texto":"60°, 60° y 60°."}],
"glosario":[{"palabra":"Ángulo interior","significado":"Ángulo de adentro del triángulo."},{"palabra":"Ángulo exterior","significado":"El que se forma al prolongar un lado."},{"palabra":"Prolongar","significado":"Alargar un lado con una línea."},{"palabra":"Adyacente","significado":"Ángulo pegado que suma 180° con otro."},{"palabra":"Desigual","significado":"El ángulo distinto en un isósceles."}],
"carpeta":["Dos ángulos de un triángulo miden 35° y 85°. ¿Cuánto mide el tercero?","¿Cuánto mide el ángulo exterior adyacente a un ángulo interior de 72°?","Los dos ángulos interiores no adyacentes a un ángulo exterior miden 40° y 75°. ¿Cuánto mide ese ángulo exterior?","Un compañero dice que un triángulo puede tener dos ángulos rectos. ¿Cuántos grados sumarían esos dos ángulos solos?"],
"respuestas_carpeta":[["60","60°"],["108","108°"],["115","115°"],["180","180°"]],
"soluciones":{"incompleto":"115°. 65°.","solo":"x + x + 20 + 2x = 180, 4x = 160, x = 40. Los ángulos miden 40°, 60° y 80°.","carpeta":["60°: 180° − (35° + 85°).","108°: 180° − 72°.","115°: 40° + 75°.","180°: ya sumarían todo, y el tercer ángulo mediría 0°. Es imposible."]}
}
N3={
"objetivo":"Vas a poder reconocer y clasificar cuadriláteros, y usar las propiedades de los lados y los ángulos de los paralelogramos.",
"vas_a_ver":["Qué es un cuadrilátero","Paralelogramos, trapecios y trapezoides","Rectángulo, rombo y cuadrado","Uno dentro de otro","Lados y ángulos del paralelogramo"],
"secciones":[
 S(1,"Cuadriláteros",[
  D("Cuadrilátero","Un <b>cuadrilátero</b> es un polígono de <b>4 lados</b>, con 4 vértices y 4 ángulos. Se clasifican según cuántos pares de <b>lados paralelos</b> tienen."),
  T("Según los lados paralelos",["Pares de lados paralelos","Se llama"],[["Dos pares","Paralelogramo"],["Un par","Trapecio"],["Ninguno","Trapezoide"]],"Se miran los lados opuestos: los que no se tocan."),
 ]),
 S(1,"La familia de los paralelogramos",[
  D("Paralelogramos especiales","El <b>rectángulo</b> es un paralelogramo con <b>4 ángulos rectos</b>. El <b>rombo</b> es un paralelogramo con <b>4 lados iguales</b>. El <b>cuadrado</b> tiene las dos cosas: 4 ángulos rectos y 4 lados iguales."),
  IMG("Cuadriláteros","Los cuatro primeros tienen dos pares de lados paralelos; el trapecio, uno solo.","Un paralelogramo, un rectángulo, un rombo, un cuadrado y un trapecio.",fig_paralelogramos()),
 ]),
 S(2,"Uno dentro de otro",[
  P("Las familias se incluyen: todo cuadrado <b>es</b> un rectángulo (tiene 4 ángulos rectos) y también <b>es</b> un rombo (tiene 4 lados iguales). Y todo rectángulo y todo rombo son paralelogramos. Al revés no: no todo rectángulo es cuadrado."),
  E("¿Es o no es?","Se controlan las propiedades, no la apariencia.",["¿Un cuadrado es un rectángulo? Sí: tiene 4 ángulos rectos.","¿Un rombo es un cuadrado? Solo si además tiene ángulos rectos.","¿Un rectángulo es un paralelogramo? Sí: tiene dos pares de lados paralelos."]),
 ]),
 S(2,"Lados y ángulos del paralelogramo",[
  P("En todo paralelogramo, los <b>lados opuestos son iguales</b> y los <b>ángulos opuestos son iguales</b>. Además, dos ángulos <b>consecutivos suman 180°</b>."),
  E("Un ángulo de 70°","Usamos opuestos y consecutivos.",["Su opuesto mide 70°.","Su consecutivo mide 180° − 70° = 110°.","Los cuatro ángulos: 70°, 110°, 70° y 110°."]),
 ]),
],
"ejemplo_completo":{"titulo":"¿qué cuadrilátero es?","planteo":"Un cuadrilátero tiene dos pares de lados paralelos, sus 4 lados miden 5 cm y sus ángulos miden 60°, 120°, 60° y 120°. ¿Qué cuadrilátero es?","pasos":["Dos pares de lados paralelos: es un paralelogramo.","Los 4 lados iguales: es un rombo.","No tiene ángulos rectos: no es cuadrado.","Es un rombo."]},
"ejemplo_incompleto":{"titulo":"un ángulo de 65°","planteo":"En un paralelogramo un ángulo mide 65°. Completá los espacios.","pasos":["Su ángulo opuesto mide ___ .","Su ángulo consecutivo mide 180° − 65° = ___ ."]},
"ejemplo_solo":{"titulo":"un ángulo recto","planteo":"Un paralelogramo de lados 6 cm y 4 cm tiene un ángulo de 90°. ¿Cuánto miden los otros tres ángulos y qué paralelogramo es?"},
"tip":{"titulo":"Propiedades, no apariencia","texto":"Un cuadrado dibujado inclinado sigue siendo un cuadrado. Clasificá mirando lados y ángulos, no cómo está girado."},
"ojo":["Creer que el cuadrado no es un rectángulo: tiene 4 ángulos rectos, así que sí lo es.","Confundir rombo con cuadrado: el rombo no necesita ángulos rectos."],
"resumen":[{"titulo":"Paralelogramo","texto":"Dos pares de lados paralelos."},{"titulo":"Trapecio","texto":"Un solo par de lados paralelos."},{"titulo":"Rectángulo y rombo","texto":"4 ángulos rectos; 4 lados iguales."},{"titulo":"Cuadrado","texto":"Es rectángulo y rombo a la vez."},{"titulo":"Ángulos","texto":"Opuestos iguales, consecutivos suman 180°."}],
"glosario":[{"palabra":"Cuadrilátero","significado":"Figura de 4 lados."},{"palabra":"Paralelogramo","significado":"Cuadrilátero con dos pares de lados paralelos."},{"palabra":"Trapecio","significado":"Cuadrilátero con un solo par de lados paralelos."},{"palabra":"Trapezoide","significado":"Cuadrilátero sin lados paralelos."},{"palabra":"Rombo","significado":"Paralelogramo con 4 lados iguales."},{"palabra":"Lados opuestos","significado":"Los que no se tocan."}],
"carpeta":["¿Cómo se llama el cuadrilátero que tiene un solo par de lados paralelos?","En un paralelogramo un ángulo mide 80°. ¿Cuánto mide su ángulo consecutivo?","¿Cuántos lados iguales tiene un rombo?","Un compañero dice que el cuadrado no es un rectángulo. ¿Cuántos ángulos rectos tiene un cuadrado?"],
"respuestas_carpeta":[["trapecio"],["100","100°"],["4","cuatro"],["4","cuatro"]],
"soluciones":{"incompleto":"65°. 115°.","solo":"Los cuatro miden 90° (opuesto 90° y consecutivos 180° − 90° = 90°). Como sus lados no son todos iguales, es un rectángulo.","carpeta":["Trapecio.","100°: los consecutivos suman 180°.","4: todos sus lados son iguales.","4: por eso el cuadrado también es un rectángulo."]}
}
N4={
"objetivo":"Vas a poder usar las propiedades de las diagonales de los paralelogramos y que los ángulos de un cuadrilátero suman 360°.",
"vas_a_ver":["Qué es una diagonal","Diagonales del paralelogramo","Rectángulo, rombo y cuadrado","Los ángulos suman 360°","Construir con diagonales"],
"secciones":[
 S(1,"Diagonales",[
  D("Diagonal","Una <b>diagonal</b> es el segmento que une <b>dos vértices que no son consecutivos</b>. Todo cuadrilátero tiene <b>2 diagonales</b>."),
  P("En el cuadrilátero ABCD, las diagonales son AC y BD. AB no es diagonal: es un lado, porque A y B son consecutivos."),
 ]),
 S(1,"Diagonales del paralelogramo",[
  D("Se cortan en su punto medio","En todo paralelogramo, las diagonales <b>se cortan en su punto medio</b>: cada diagonal queda partida en dos partes iguales."),
  E("Una diagonal de 10 cm","El punto de corte la divide en dos.",["10 ÷ 2 = 5.","Cada mitad mide 5 cm."]),
 ]),
 S(2,"Rectángulo, rombo y cuadrado",[
  T("Sus diagonales",["Cuadrilátero","Iguales","Perpendiculares"],[["Paralelogramo común","No","No"],["Rectángulo","Sí","No"],["Rombo","No","Sí"],["Cuadrado","Sí","Sí"]],"En los cuatro, además, se cortan en su punto medio."),
  IMG("Diagonales","En el rectángulo son iguales; en el rombo, perpendiculares; en el cuadrado, las dos cosas.","Un rectángulo, un rombo y un cuadrado con sus diagonales y el ángulo recto marcado donde corresponde.",fig_diagonales()),
 ]),
 S(2,"Los ángulos suman 360°",[
  P("Una diagonal divide al cuadrilátero en <b>dos triángulos</b>. Cada uno suma 180°, así que los ángulos de un cuadrilátero suman <b>2 × 180° = 360°</b>."),
  E("Ángulos de 80°, 95° y 110°","Falta el cuarto.",["80° + 95° + 110° = 285°.","360° − 285° = 75°.","El cuarto ángulo mide 75°."]),
 ]),
 S(2,"Construir con diagonales",[
  P("Un rombo de diagonales 6 cm y 4 cm: se trazan dos segmentos perpendiculares de 6 y 4 cm que se cortan en sus puntos medios (a 3 cm y a 2 cm de cada punta) y se unen los cuatro extremos."),
 ]),
],
"ejemplo_completo":{"titulo":"diagonales de 8 cm","planteo":"Las diagonales de un cuadrilátero miden 8 cm las dos, se cortan en su punto medio y son perpendiculares. ¿Qué cuadrilátero es? ¿Cuánto mide cada mitad de diagonal?","pasos":["Se cortan en su punto medio: es un paralelogramo.","Son iguales: es un rectángulo.","Son perpendiculares: es un rombo.","Las dos cosas: es un cuadrado.","Cada mitad mide 8 ÷ 2 = 4 cm."]},
"ejemplo_incompleto":{"titulo":"ángulos de 100°, 70° y 110°","planteo":"Completá los espacios para hallar el cuarto ángulo.","pasos":["100° + 70° + 110° = ___ .","360° − 280° = ___ ."]},
"ejemplo_solo":{"titulo":"el rombo","planteo":"Un rombo tiene diagonales de 10 cm y 6 cm. ¿A cuántos cm del centro está cada extremo de la diagonal más corta?"},
"tip":{"titulo":"Pensá en dos triángulos","texto":"Si te olvidás cuánto suman los ángulos de un cuadrilátero, trazá una diagonal: son dos triángulos, 180° + 180°."},
"ojo":["Pensar que las diagonales siempre son perpendiculares: en el rectángulo común no lo son.","Olvidar que los ángulos del cuadrilátero suman 360°, no 180°."],
"resumen":[{"titulo":"Diagonal","texto":"Une vértices no consecutivos."},{"titulo":"Paralelogramo","texto":"Se cortan en su punto medio."},{"titulo":"Rectángulo y rombo","texto":"Iguales; perpendiculares."},{"titulo":"Cuadrado","texto":"Iguales y perpendiculares."},{"titulo":"Ángulos","texto":"Suman 360°."}],
"glosario":[{"palabra":"Diagonal","significado":"Segmento entre dos vértices no consecutivos."},{"palabra":"Punto medio","significado":"El que parte un segmento en dos partes iguales."},{"palabra":"Perpendiculares","significado":"Que se cortan formando ángulos rectos."},{"palabra":"Consecutivos","significado":"Vértices que están uno al lado del otro."},{"palabra":"Extremo","significado":"Cada punta de un segmento."}],
"carpeta":["¿Cuánto suman los ángulos interiores de un cuadrilátero?","Tres ángulos de un cuadrilátero miden 90°, 90° y 120°. ¿Cuánto mide el cuarto?","Una diagonal de un rectángulo mide 14 cm. ¿Cuánto mide la otra?","Un compañero dice que las diagonales de un rectángulo siempre son perpendiculares. ¿En cuál de estos sí lo son siempre: rectángulo o rombo?"],
"respuestas_carpeta":[["360","360°"],["60","60°"],["14","14cm","14 cm"],["rombo"]],
"soluciones":{"incompleto":"280°. 80°.","solo":"A 3 cm: la diagonal corta mide 6 cm y se corta en su punto medio.","carpeta":["360°: dos triángulos de 180°.","60°: 360° − 300°.","14 cm: en el rectángulo las diagonales son iguales.","Rombo: en el rectángulo común las diagonales no son perpendiculares."]}
}
ACT={
"1":[{"t":"classify","p":"Clasificá cada triángulo según sus lados.","o":{"elementos":["5, 5 y 5 cm","6, 6 y 4 cm","3, 4 y 5 cm","7, 7 y 2 cm"],"categorias":["Equilátero","Isósceles","Escaleno"]},"r":{"categorias":{"5, 5 y 5 cm":"Equilátero","6, 6 y 4 cm":"Isósceles","3, 4 y 5 cm":"Escaleno","7, 7 y 2 cm":"Isósceles"}},"e":"Se cuenta cuántos lados son iguales: tres, dos o ninguno."},
     MC("¿Con cuál de estas medidas se puede construir un triángulo?",["2, 3 y 7 cm","4, 4 y 9 cm","5, 7 y 10 cm","1, 2 y 3 cm"],"5, 7 y 10 cm","El lado mayor tiene que ser menor que la suma de los otros dos: 10 < 5 + 7 = 12.")],
"2":[N("Dos ángulos de un triángulo miden {a}° y {b}°. ¿Cuánto mide el tercero?",{"formula":"180-a-b"},"Los tres suman 180°: se resta la suma de los dos.",{"vars":{"a":{"min":25,"max":80},"b":{"min":25,"max":80}}}),
     N("¿Cuánto mide el ángulo exterior adyacente a un ángulo interior de {a}°?",{"formula":"180-a"},"El exterior y su interior adyacente suman 180°.",{"vars":{"a":{"min":30,"max":150}}})],
"3":[{"t":"multi_select","p":"¿Cuáles de estas frases son verdaderas?","o":["Todo cuadrado es un rectángulo","Todo rombo es un cuadrado","Todo rectángulo es un paralelogramo","Un trapecio tiene dos pares de lados paralelos"],"r":{"correctas":["Todo cuadrado es un rectángulo","Todo rectángulo es un paralelogramo"]},"e":"El cuadrado tiene 4 ángulos rectos; el rombo no siempre; el trapecio tiene un solo par de lados paralelos."},
     N("En un paralelogramo un ángulo mide {a}°. ¿Cuánto mide su ángulo consecutivo?",{"formula":"180-a"},"Los ángulos consecutivos de un paralelogramo suman 180°.",{"vars":{"a":{"min":40,"max":140}},"reglas":["a!=90"]})],
"4":[N("Tres ángulos de un cuadrilátero miden {a}°, {b}° y {c}°. ¿Cuánto mide el cuarto?",{"formula":"360-a-b-c"},"Los ángulos de un cuadrilátero suman 360°.",{"vars":{"a":{"min":60,"max":120},"b":{"min":60,"max":120},"c":{"min":60,"max":120}},"reglas":["a+b+c<330"]}),
     {"t":"matching","p":"Uní cada cuadrilátero con la propiedad de sus diagonales.","o":{"izquierda":["Rectángulo","Rombo","Cuadrado"],"derecha":["Iguales","Perpendiculares","Iguales y perpendiculares"]},"r":{"pares":{"Rectángulo":"Iguales","Rombo":"Perpendiculares","Cuadrado":"Iguales y perpendiculares"}},"e":"El cuadrado es rectángulo y rombo a la vez, así que tiene las dos propiedades."}],
"5":[MC("Relámpago. Un triángulo con ángulos de 90°, 60° y 30° es…",["Acutángulo","Rectángulo","Obtusángulo"],"Rectángulo","Tiene un ángulo de 90°.",tiempo=20),
     N("Relámpago. Dos ángulos de un triángulo miden 50° y 70°. ¿Cuánto mide el tercero?",{"acepta":[60]},"180° − 120° = 60°.",tiempo=25),
     N("Relámpago. ¿Cuánto mide el adyacente de un ángulo de 40°?",{"acepta":[140]},"Repaso de la misión 17: los adyacentes suman 180°.",tiempo=20),
     N("Relámpago. Resolvé 3x − 6 = 24.",{"acepta":[10]},"Repaso de la misión 16: 3x = 30, x = 10.",tiempo=30)],
}
EXAMEN=[
 [1,{"t":"classify","p":"Clasificá cada triángulo según sus ángulos.","o":{"elementos":["60°, 60° y 60°","90°, 50° y 40°","110°, 40° y 30°","80°, 55° y 45°"],"categorias":["Acutángulo","Rectángulo","Obtusángulo"]},"r":{"categorias":{"60°, 60° y 60°":"Acutángulo","90°, 50° y 40°":"Rectángulo","110°, 40° y 30°":"Obtusángulo","80°, 55° y 45°":"Acutángulo"}},"e":"Se mira el ángulo mayor: agudo, recto u obtuso."}],
 [1,VF("Con lados de 4, 5 y 10 cm se puede construir un triángulo.","Falso","4 + 5 = 9, menor que 10.")],
 [1,MC("Un triángulo tiene ángulos de 90°, 45° y 45°. ¿Cuál es su nombre completo?",["Rectángulo isósceles","Rectángulo escaleno","Acutángulo isósceles","Obtusángulo isósceles"],"Rectángulo isósceles","Tiene un ángulo recto y dos ángulos iguales, frente a dos lados iguales.")],
 [2,N("Dos ángulos de un triángulo miden 47° y 68°. ¿Cuánto mide el tercero?",{"acepta":[65]},"180° − 115° = 65°.")],
 [2,N("En un triángulo isósceles el ángulo desigual mide 50°. ¿Cuánto mide cada uno de los otros dos?",{"acepta":[65]},"(180° − 50°) ÷ 2 = 65°.")],
 [2,N("Los dos ángulos interiores no adyacentes a un ángulo exterior miden 35° y 80°. ¿Cuánto mide el exterior?",{"acepta":[115]},"El exterior es la suma de los dos interiores no adyacentes.")],
 [2,N("Los ángulos de un triángulo miden x, 2x y 3x. ¿Cuánto vale x?",{"acepta":[30]},"6x = 180, x = 30.")],
 [3,MC("¿Cómo se llama un cuadrilátero sin lados paralelos?",["Trapecio","Trapezoide","Paralelogramo","Rombo"],"Trapezoide","El trapecio tiene un par; el trapezoide, ninguno.")],
 [3,VF("Todo cuadrado es también un rombo.","Verdadero","Tiene 4 lados iguales.")],
 [3,N("En un paralelogramo un ángulo mide 55°. ¿Cuánto mide su ángulo opuesto?",{"acepta":[55]},"Los ángulos opuestos son iguales.")],
 [4,N("Tres ángulos de un cuadrilátero miden 85°, 95° y 100°. ¿Cuánto mide el cuarto?",{"acepta":[80]},"360° − 280° = 80°.")],
 [4,MC("¿En qué cuadrilátero las diagonales son iguales pero no perpendiculares?",["Rombo","Cuadrado","Rectángulo","Trapezoide"],"Rectángulo","En el rectángulo son iguales; en el cuadrado, además, perpendiculares.")],
 [4,N("Una diagonal de un paralelogramo mide 18 cm. ¿Cuánto mide cada mitad?",{"acepta":[9]},"Las diagonales se cortan en su punto medio.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":18,"practica":"Práctica general: triángulos y cuadriláteros","examen_titulo":"Nivel jefe: triángulos y cuadriláteros",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-18.json"),"w"),ensure_ascii=False)
print("ok")
