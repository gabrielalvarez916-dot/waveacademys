# -*- coding: utf-8 -*-
"""Matemática I · Misión 19 · Perímetro, área y volumen. Las unidades van dentro de cada nivel (1 longitud, 2 superficie, 3 volumen y capacidad).
El nivel 4 (cuadrados y cubos perfectos) ya existía con PDF y actividades: acá solo entra en el examen. El nivel 5 es la práctica general.
Genera mision-19.json (se carga con cargar_mision)."""
import os, sys, io, base64, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
V, O, C = "#0e7c7b", "#243b3f", "#d8f0ea"
def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=16); o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()
def IMG(t, pie, desc, b64): return {"tipo":"imagen","imagen_tipo":"diagrama","titulo":t,"texto":pie,"imagen_descripcion":desc,"imagen_fuente":"Dibujo propio (matplotlib).","png_base64":b64}
def lienzo(w, h): fig, ax = plt.subplots(figsize=(w, h)); ax.set_aspect("equal"); ax.axis("off"); return fig, ax

def fig_L():
    fig, ax = lienzo(5, 3.2); P = [(0,0),(10,0),(10,3),(6,3),(6,6),(0,6)]
    ax.add_patch(Polygon(P, closed=True, facecolor=C, edgecolor=O, lw=2.2)); ax.set_xlim(-1.5, 11.5); ax.set_ylim(-1.2, 7)
    for (x, y, t) in ((5,-0.7,"10 cm"),(10.7,1.5,"3 cm"),(8,3.4,"4 cm"),(6.6,4.5,"3 cm"),(3,6.4,"6 cm"),(-1.0,3,"6 cm")): ax.text(x, y, t, ha="center", va="center", fontsize=11, color=V, weight="bold")
    return png(fig)
def fig_triangulo():
    fig, ax = lienzo(5, 2.8); ax.set_xlim(-0.5, 8.8); ax.set_ylim(-1, 5.6)
    ax.add_patch(Polygon([(0,0),(8,0),(8,5),(0,5)], closed=True, facecolor="white", edgecolor=O, lw=1.6, ls="--"))
    ax.add_patch(Polygon([(0,0),(8,0),(3,5)], closed=True, facecolor=C, edgecolor=O, lw=2.2)); ax.plot([3,3],[0,5], color=V, lw=1.8, ls=":")
    ax.text(4, -0.6, "base 8 cm", ha="center", fontsize=11, color=O); ax.text(3.15, 2.5, "altura 5 cm", fontsize=11, color=V)
    return png(fig)
def fig_prisma():
    fig, ax = lienzo(5, 3.4); dx, dy = 0.5, 0.35; a, b, c = 4, 3, 2
    def cara(P, f): ax.add_patch(Polygon(P, closed=True, facecolor=f, edgecolor=O, lw=1.1))
    for k in range(c):
        for i in range(a): cara([(i, k), (i+1, k), (i+1, k+1), (i, k+1)], C)
    for j in range(b):
        for i in range(a): cara([(i+j*dx, c+j*dy), (i+1+j*dx, c+j*dy), (i+1+(j+1)*dx, c+(j+1)*dy), (i+(j+1)*dx, c+(j+1)*dy)], "#b9e3d9")
    for j in range(b):
        for k in range(c): cara([(a+j*dx, k+j*dy), (a+(j+1)*dx, k+(j+1)*dy), (a+(j+1)*dx, k+1+(j+1)*dy), (a+j*dx, k+1+j*dy)], "#eef7f5")
    ax.set_xlim(-0.6, a + b*dx + 0.6); ax.set_ylim(-0.8, c + b*dy + 0.4)
    ax.text(a/2, -0.5, "4 cm", ha="center", fontsize=11, color=V, weight="bold"); ax.text(a + b*dx + 0.25, c/2 + b*dy/2, "2 cm", fontsize=11, color=V, weight="bold"); ax.text(a + b*dx/2 + 0.1, c + b*dy/2 - 0.35, "3 cm", fontsize=11, color=V, weight="bold")
    return png(fig)

N1={
"objetivo":"Vas a poder calcular el perímetro de polígonos y figuras compuestas, y pasar de una unidad de longitud a otra.",
"vas_a_ver":["Qué es el perímetro","Unidades de longitud","Perímetro de figuras compuestas","Sumar con la misma unidad","La vuelta a un círculo (idea)"],
"secciones":[
 S(1,"Perímetro",[
  D("Perímetro","El <b>perímetro</b> es la <b>longitud del borde</b> de una figura: la suma de las medidas de todos sus lados."),
  E("Rectángulo y cuadrado","Sumamos todos los lados.",["Rectángulo de 8 cm por 5 cm: 8 + 5 + 8 + 5 = 26 cm.","Cuadrado de 6 cm de lado: 6 + 6 + 6 + 6 = 4 × 6 = 24 cm."]),
 ]),
 S(1,"Unidades de longitud",[
  D("Unidades de longitud","Se mide en <b>km, hm, dam, m, dm, cm y mm</b>. Cada unidad es <b>10 veces</b> la que sigue: para pasar a una más chica se multiplica, y a una más grande se divide."),
  T("Equivalencias que más se usan",["Unidad","Equivale a"],[["1 km","1.000 m"],["1 m","100 cm"],["1 cm","10 mm"]],"Ejemplos: 3,5 m = 3,5 × 100 = 350 cm. 2.400 m = 2.400 ÷ 1.000 = 2,4 km."),
 ]),
 S(2,"Figuras compuestas",[
  P("En una figura armada con varias partes se suman <b>solo los lados del borde</b>. Si falta alguna medida, se calcula con las que hay."),
  IMG("Una figura en forma de L","Se suman los seis lados del borde: 10 + 3 + 4 + 3 + 6 + 6 = 32 cm.","Figura en forma de L con lados de 10, 3, 4, 3, 6 y 6 cm.",fig_L()),
  E("La L de la figura","El lado de 4 cm sale de 10 − 6.",["Lados: 10, 3, 4, 3, 6 y 6 cm.","10 + 3 + 4 + 3 + 6 + 6 = 32.","El perímetro es 32 cm."]),
 ]),
 S(2,"Todo en la misma unidad",[
  P("Antes de sumar, todas las medidas tienen que estar en la <b>misma unidad</b>. Un rectángulo de 2 m por 45 cm: 2 m = 200 cm, y el perímetro es 200 + 45 + 200 + 45 = 490 cm."),
 ]),
 S(2,"La vuelta a un círculo",[
  P("El borde de un círculo, la <b>circunferencia</b>, mide un poco más de <b>3 veces su diámetro</b>. Con un diámetro de 10 cm, la vuelta mide algo más de 30 cm. La cuenta exacta se ve en 2.º año."),
 ]),
],
"ejemplo_completo":{"titulo":"el cerco","planteo":"Un terreno rectangular mide 25 m por 12 m. Se quiere cercar con alambre, dejando un portón de 3 m. ¿Cuántos metros de alambre hacen falta?","pasos":["Perímetro: 25 + 12 + 25 + 12 = 74 m.","El portón no lleva alambre: 74 − 3 = 71 m.","Hacen falta 71 m de alambre."]},
"ejemplo_incompleto":{"titulo":"cuadrado de 1,5 m","planteo":"Calculá en cm el perímetro de un cuadrado de 1,5 m de lado. Completá los espacios.","pasos":["1,5 m = ___ cm.","4 × 150 = ___ cm."]},
"ejemplo_solo":{"titulo":"el equilátero","planteo":"Un triángulo equilátero tiene lados de 35 cm. ¿Cuál es su perímetro en metros?"},
"tip":{"titulo":"Recorré el borde","texto":"Marcá con el dedo un punto de partida y recorré el borde contando cada lado una sola vez hasta volver."},
"ojo":["Sumar medidas en unidades distintas: 3 m + 50 cm no es 53.","En figuras compuestas, sumar lados de adentro que no son borde."],
"resumen":[{"titulo":"Perímetro","texto":"Suma de los lados del borde."},{"titulo":"Cuadrado","texto":"4 × lado."},{"titulo":"Unidades","texto":"De a 10: 1 m = 100 cm."},{"titulo":"Antes de sumar","texto":"Todo en la misma unidad."}],
"glosario":[{"palabra":"Perímetro","significado":"Largo total del borde de una figura."},{"palabra":"Figura compuesta","significado":"Figura armada con varias partes."},{"palabra":"Equivalencia","significado":"Dos medidas que valen lo mismo."},{"palabra":"Circunferencia","significado":"El borde de un círculo."},{"palabra":"Diámetro","significado":"Segmento que cruza el círculo por el centro."}],
"carpeta":["¿Cuál es el perímetro, en cm, de un rectángulo de 12 cm por 7 cm?","¿Cuántos cm son 4,2 m?","¿Cuál es el perímetro, en cm, de un cuadrado de 9 cm de lado?","Un compañero sumó 3 m + 50 cm y le dio 53. ¿Cuántos cm son en total?"],
"respuestas_carpeta":[["38","38cm","38 cm"],["420","420cm","420 cm"],["36","36cm","36 cm"],["350","350cm","350 cm"]],
"soluciones":{"incompleto":"150 cm. 600 cm.","solo":"3 × 35 = 105 cm = 1,05 m.","carpeta":["38 cm: 12 + 7 + 12 + 7.","420 cm: 4,2 × 100.","36 cm: 4 × 9.","350 cm: 3 m = 300 cm, y 300 + 50 = 350."]}
}
N2={
"objetivo":"Vas a poder calcular el área de rectángulos, triángulos, paralelogramos, rombos, trapecios y figuras compuestas, y pasar de una unidad de superficie a otra.",
"vas_a_ver":["Qué es el área","Rectángulo y cuadrado","Triángulo y paralelogramo","Rombo y trapecio","Unidades de superficie"],
"secciones":[
 S(1,"Qué es el área",[
  D("Área","El <b>área</b> es la <b>superficie</b> que ocupa una figura. Se mide contando cuadraditos de 1 cm de lado: cada uno es <b>1 cm²</b>. En un rectángulo, el área es <b>base × altura</b>."),
  E("Rectángulo y cuadrado","Contamos filas por columnas.",["Rectángulo de 6 cm por 4 cm: 6 × 4 = 24 cm².","Cuadrado de 5 cm de lado: 5 × 5 = 25 cm²."]),
 ]),
 S(1,"Triángulo y paralelogramo",[
  D("Fórmulas","<b>Paralelogramo:</b> base × altura (si se recorta un triángulo de un costado y se pasa al otro, queda un rectángulo). <b>Triángulo:</b> base × altura ÷ 2, porque es la mitad de un rectángulo."),
  IMG("El triángulo es la mitad","El triángulo ocupa justo la mitad del rectángulo de 8 por 5.","Triángulo de base 8 cm y altura 5 cm dentro de un rectángulo de 8 por 5 cm.",fig_triangulo()),
  E("Triángulo de base 8 cm y altura 5 cm","La mitad del rectángulo.",["8 × 5 = 40.","40 ÷ 2 = 20.","El área es 20 cm²."]),
 ]),
 S(2,"Rombo y trapecio",[
  P("<b>Rombo:</b> diagonal mayor × diagonal menor ÷ 2. <b>Trapecio:</b> (base mayor + base menor) × altura ÷ 2."),
  E("Dos áreas","Usamos las fórmulas.",["Rombo de diagonales 6 y 4 cm: 6 × 4 ÷ 2 = 12 cm².","Trapecio de bases 10 y 6 cm y altura 4 cm: (10 + 6) × 4 ÷ 2 = 32 cm²."]),
 ]),
 S(2,"Unidades de superficie",[
  P("Como un cuadrado de 1 m de lado mide 100 cm por 100 cm, <b>1 m² = 10.000 cm²</b>. Entre unidades vecinas de superficie se salta de a <b>100</b>: 1 cm² = 100 mm²."),
  E("Pasar de unidad","Multiplicamos o dividimos.",["3 m² = 3 × 10.000 = 30.000 cm².","500 mm² = 500 ÷ 100 = 5 cm²."]),
 ]),
 S(2,"Figuras compuestas",[
  P("Se parte la figura en rectángulos y triángulos, o se calcula el rectángulo entero y se resta lo que falta. La L de 10 por 6 cm sin un rectángulo de 4 por 3: 60 − 12 = 48 cm²."),
 ]),
],
"ejemplo_completo":{"titulo":"la pared","planteo":"Hay que pintar una pared de 4 m por 2,5 m que tiene una ventana de 1,2 m por 1 m. ¿Cuántos m² se pintan?","pasos":["Pared: 4 × 2,5 = 10 m².","Ventana: 1,2 × 1 = 1,2 m².","Se pinta: 10 − 1,2 = 8,8 m²."]},
"ejemplo_incompleto":{"titulo":"un triángulo","planteo":"Área de un triángulo de base 12 cm y altura 7 cm. Completá los espacios.","pasos":["12 × 7 = ___ .","84 ÷ 2 = ___ cm²."]},
"ejemplo_solo":{"titulo":"el rombo","planteo":"Un rombo tiene diagonales de 10 cm y 7 cm. ¿Cuál es su área?"},
"tip":{"titulo":"Perímetro o área","texto":"Si la pregunta habla de bordes, cercos o marcos, es perímetro (cm). Si habla de cubrir, pintar o alfombrar, es área (cm²)."},
"ojo":["Olvidar dividir por 2 en el triángulo.","Creer que 1 m² son 100 cm²: son 10.000."],
"resumen":[{"titulo":"Rectángulo","texto":"base × altura."},{"titulo":"Triángulo","texto":"base × altura ÷ 2."},{"titulo":"Rombo","texto":"D × d ÷ 2."},{"titulo":"Trapecio","texto":"(B + b) × h ÷ 2."},{"titulo":"Unidades","texto":"De a 100: 1 m² = 10.000 cm²."}],
"glosario":[{"palabra":"Área","significado":"Superficie que ocupa una figura."},{"palabra":"cm²","significado":"Un cuadradito de 1 cm de lado."},{"palabra":"Altura","significado":"Distancia perpendicular de la base al lado opuesto."},{"palabra":"Diagonal","significado":"Segmento entre dos vértices no consecutivos."},{"palabra":"Superficie","significado":"Lo que cubre una figura."}],
"carpeta":["¿Cuál es el área, en cm², de un rectángulo de 9 cm por 6 cm?","¿Cuál es el área, en cm², de un triángulo de base 10 cm y altura 6 cm?","¿Cuántos cm² son 2 m²?","Un compañero dice que 1 m² son 100 cm². ¿Cuántos cm² son en realidad?"],
"respuestas_carpeta":[["54","54cm²","54 cm²"],["30","30cm²","30 cm²"],["20000","20.000"],["10000","10.000"]],
"soluciones":{"incompleto":"84. 42 cm².","solo":"10 × 7 ÷ 2 = 35 cm².","carpeta":["54 cm²: 9 × 6.","30 cm²: 10 × 6 ÷ 2.","20.000 cm²: 2 × 10.000.","10.000 cm²: 100 cm × 100 cm."]}
}
N3={
"objetivo":"Vas a poder calcular el volumen de cubos y prismas, y relacionar unidades de volumen con litros.",
"vas_a_ver":["Qué es el volumen","El cubo unidad","Volumen del prisma y del cubo","Unidades de volumen","Volumen y capacidad: litros"],
"secciones":[
 S(1,"Volumen y cubo unidad",[
  D("Volumen","El <b>volumen</b> es el <b>espacio</b> que ocupa un cuerpo. Se mide contando cubitos de 1 cm de arista: cada uno es <b>1 cm³</b>."),
  IMG("Una caja de cubitos","4 por 3 cubitos en cada piso, y 2 pisos: 24 cubitos.","Prisma de 4 por 3 por 2 cm armado con cubitos de 1 cm.",fig_prisma()),
  E("Caja de 4 × 3 × 2 cm","Contamos por pisos.",["Cada piso: 4 × 3 = 12 cubitos.","Hay 2 pisos: 12 × 2 = 24.","El volumen es 24 cm³."]),
 ]),
 S(1,"Prisma y cubo",[
  D("Fórmulas","<b>Prisma:</b> largo × ancho × alto (o área de la base × altura). <b>Cubo:</b> arista × arista × arista = arista³."),
  E("Dos volúmenes","Multiplicamos las tres medidas.",["Cubo de 5 cm de arista: 5 × 5 × 5 = 125 cm³.","Prisma con base de 12 cm² y altura 10 cm: 12 × 10 = 120 cm³."]),
 ]),
 S(2,"Unidades de volumen",[
  P("Un cubo de 1 dm de arista mide 10 × 10 × 10 cm, así que <b>1 dm³ = 1.000 cm³</b>. Entre unidades vecinas de volumen se salta de a <b>1.000</b>: 1 m³ = 1.000 dm³."),
 ]),
 S(2,"Volumen y capacidad",[
  P("La <b>capacidad</b> es lo que entra en un recipiente, y se mide en litros. <b>1 dm³ = 1 litro</b>, <b>1 cm³ = 1 ml</b> y <b>1 m³ = 1.000 litros</b>."),
  E("La pecera","Pecera de 50 × 30 × 40 cm.",["50 × 30 × 40 = 60.000 cm³.","60.000 cm³ = 60 dm³.","Entran 60 litros."]),
 ]),
],
"ejemplo_completo":{"titulo":"la pileta","planteo":"Una pileta mide 8 m de largo, 4 m de ancho y 1,5 m de profundidad. ¿Cuántos litros de agua entran?","pasos":["Volumen: 8 × 4 × 1,5 = 48 m³.","1 m³ = 1.000 litros.","48 × 1.000 = 48.000 litros."]},
"ejemplo_incompleto":{"titulo":"caja de 10 cm","planteo":"Una caja cúbica de 10 cm de arista. Completá los espacios.","pasos":["10 × 10 × 10 = ___ cm³.","1.000 cm³ = ___ dm³, o sea 1 litro."]},
"ejemplo_solo":{"titulo":"un cubito","planteo":"¿Cuál es el volumen de un cubo de 3 cm de arista?"},
"tip":{"titulo":"Fijate la unidad","texto":"Perímetro en cm, área en cm², volumen en cm³. El número chiquito te dice cuántas medidas se multiplicaron."},
"ojo":["Sumar las medidas en vez de multiplicarlas.","Creer que 1 litro son 100 cm³: son 1.000."],
"resumen":[{"titulo":"Volumen","texto":"Espacio que ocupa, en cm³."},{"titulo":"Prisma","texto":"largo × ancho × alto."},{"titulo":"Cubo","texto":"arista³."},{"titulo":"Litros","texto":"1 dm³ = 1 L; 1 m³ = 1.000 L."}],
"glosario":[{"palabra":"Volumen","significado":"Espacio que ocupa un cuerpo."},{"palabra":"Prisma","significado":"Cuerpo con dos bases iguales y caras rectangulares."},{"palabra":"Arista","significado":"Borde donde se juntan dos caras."},{"palabra":"Capacidad","significado":"Lo que entra en un recipiente."},{"palabra":"cm³","significado":"Un cubito de 1 cm de arista."}],
"carpeta":["¿Cuál es el volumen, en cm³, de un prisma de 5 cm por 4 cm por 3 cm?","¿Cuál es el volumen, en cm³, de un cubo de 4 cm de arista?","¿Cuántos litros entran en un recipiente de 5 dm³?","Un compañero dice que 1 litro son 100 cm³. ¿Cuántos cm³ son en realidad?"],
"respuestas_carpeta":[["60","60cm³","60 cm³"],["64","64cm³","64 cm³"],["5"],["1000","1.000"]],
"soluciones":{"incompleto":"1.000 cm³. 1 dm³.","solo":"3 × 3 × 3 = 27 cm³.","carpeta":["60 cm³: 5 × 4 × 3.","64 cm³: 4 × 4 × 4.","5 litros: 1 dm³ = 1 litro.","1.000 cm³: 1 litro = 1 dm³ = 1.000 cm³."]}
}
ACT={
"1":[N("¿Cuál es el perímetro de un rectángulo de {a} cm por {b} cm?",{"formula":"2*a+2*b"},"Se suman los cuatro lados: 2 veces el largo más 2 veces el ancho.",{"vars":{"a":{"min":6,"max":30},"b":{"min":3,"max":15}}}),
     MC("¿Cuántos cm son 2,5 m?",["25","250","2.500","0,25"],"250","1 m = 100 cm: 2,5 × 100 = 250.")],
"2":[N("¿Cuál es el área de un triángulo de base {b} cm y altura {h} cm?",{"formula":"b*k"},"Base × altura ÷ 2.",{"vars":{"b":{"min":4,"max":20},"k":{"min":2,"max":9}},"calculadas":{"h":"2*k"}}),
     MC("¿Cuántos cm² tiene 1 m²?",["100","1.000","10.000","1.000.000"],"10.000","100 cm × 100 cm = 10.000 cm².")],
"3":[N("¿Cuál es el volumen de un prisma de {a} cm por {b} cm por {c} cm?",{"formula":"a*b*c"},"Largo × ancho × alto.",{"vars":{"a":{"min":2,"max":12},"b":{"min":2,"max":10},"c":{"min":2,"max":8}}}),
     MC("¿Cuántos litros hay en 1 dm³?",["1","10","100","1.000"],"1","1 dm³ = 1 litro.")],
"5":[N("Relámpago. Perímetro de un cuadrado de 7 cm de lado (en cm).",{"acepta":[28]},"4 × 7.",tiempo=20),
     N("Relámpago. Área de un rectángulo de 8 cm por 3 cm (en cm²).",{"acepta":[24]},"8 × 3.",tiempo=20),
     MC("Relámpago. Volumen de un cubo de 2 cm de arista.",["6 cm³","8 cm³","12 cm³"],"8 cm³","2 × 2 × 2.",tiempo=20),
     N("Relámpago. Tres ángulos de un cuadrilátero miden 90°, 90° y 100°. ¿Cuánto mide el cuarto?",{"acepta":[80]},"Repaso de la misión 18: suman 360°.",tiempo=30)],
}
EXAMEN=[
 [1,N("¿Cuál es el perímetro de un rectángulo de 15 cm por 8 cm?",{"acepta":[46]},"15 + 8 + 15 + 8.")],
 [1,MC("¿Cuántos km son 3.200 m?",["32","3,2","0,32","320"],"3,2","Se divide por 1.000.")],
 [1,N("¿Cuál es el perímetro de un triángulo de lados 12, 9 y 7 cm?",{"acepta":[28]},"12 + 9 + 7.")],
 [2,N("¿Cuál es el área de un paralelogramo de base 9 cm y altura 4 cm?",{"acepta":[36]},"Base × altura.")],
 [2,N("¿Cuál es el área de un trapecio de bases 12 y 8 cm y altura 5 cm?",{"acepta":[50]},"(12 + 8) × 5 ÷ 2.")],
 [2,VF("1 m² equivale a 100 cm².","Falso","Son 10.000 cm².")],
 [2,N("A un rectángulo de 10 cm por 6 cm se le recorta un cuadrado de 2 cm de lado. ¿Cuál es el área que queda, en cm²?",{"acepta":[56]},"60 − 4.")],
 [3,N("¿Cuál es el volumen de un prisma de 6 cm por 5 cm por 2 cm?",{"acepta":[60]},"6 × 5 × 2.")],
 [3,N("¿Cuántos litros entran en una pecera de 40 cm por 25 cm por 30 cm?",{"acepta":[30]},"30.000 cm³ = 30 dm³ = 30 litros.")],
 [3,MC("1 m³ equivale a…",["10 litros","100 litros","1.000 litros","10.000 litros"],"1.000 litros","1 m³ = 1.000 dm³ y cada dm³ es un litro.")],
 [4,N("Un cuadrado tiene 81 cm² de área. ¿Cuánto mide su lado, en cm?",{"acepta":[9]},"√81 = 9.")],
 [4,N("Un cubo tiene 64 cm³ de volumen. ¿Cuánto mide su arista, en cm?",{"acepta":[4]},"∛64 = 4.")],
 [4,MC("¿Cuál de estos números es un cubo perfecto?",["36","49","100","125"],"125","125 = 5 × 5 × 5.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":19,"practica":"Práctica general: perímetro, área y volumen","examen_titulo":"Nivel jefe: perímetro, área y volumen",
   "niveles":{"1":N1,"2":N2,"3":N3},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-19.json"),"w"),ensure_ascii=False)
print("ok")
