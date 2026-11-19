# -*- coding: utf-8 -*-
"""Matemática I · Misión 20 · Estadística y probabilidad introductorias. Genera mision-20.json (se carga con cargar_mision)."""
import os, sys, io, base64, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
V, O, C = "#0e7c7b", "#243b3f", "#d8f0ea"
def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=16); o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()
def IMG(t, pie, desc, b64): return {"tipo":"imagen","imagen_tipo":"diagrama","titulo":t,"texto":pie,"imagen_descripcion":desc,"imagen_fuente":"Dibujo propio (matplotlib).","png_base64":b64}
def fig_barras():
    fig, axs = plt.subplots(1, 2, figsize=(8, 2.9)); cat = ["Fútbol", "Vóley", "Básquet", "Natación"]; f = [10, 6, 5, 4]
    axs[0].bar(cat, f, color=[V, "#5fb3a8", "#9fd2c9", C], edgecolor=O); axs[0].set_ylabel("Cantidad de alumnos", color=O); axs[0].set_title("Gráfico de barras", color=O, fontsize=11)
    for s in ("top", "right"): axs[0].spines[s].set_visible(False)
    axs[1].pie(f, labels=[f"{c}\n{x * 4}%" for c, x in zip(cat, f)], colors=[V, "#5fb3a8", "#9fd2c9", C], wedgeprops=dict(edgecolor="white"), textprops=dict(color=O, fontsize=9)); axs[1].set_title("Gráfico circular", color=O, fontsize=11)
    return png(fig)
def fig_media():
    fig, ax = plt.subplots(figsize=(6, 2.6)); n = ["Ana", "Beto", "Caro", "Dani", "Eli"]; v = [6, 8, 7, 9, 10]
    ax.bar(n, v, color=C, edgecolor=O); ax.axhline(8, color=V, lw=2.2, ls="--"); ax.text(4.45, 8.2, "media 8", color=V, fontsize=11, ha="right", weight="bold")
    ax.set_ylim(0, 11); ax.set_ylabel("Nota", color=O)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    return png(fig)

N1={
"objetivo":"Vas a poder organizar datos en una tabla de frecuencias y leer y armar gráficos de barras, circulares y de líneas.",
"vas_a_ver":["Variables y datos","Tabla de frecuencias","Gráfico de barras","Gráfico circular","Gráfico de líneas"],
"secciones":[
 S(1,"Variables y datos",[
  D("Variable y dato","Una <b>variable</b> es lo que se pregunta o se mide (el deporte favorito, la altura). Cada respuesta es un <b>dato</b>. La <b>frecuencia</b> es cuántas veces aparece cada valor."),
  P("Se preguntó a 25 alumnos su deporte favorito. La variable es \"deporte favorito\"; \"fútbol\" es un valor; si 10 alumnos dijeron fútbol, la frecuencia de fútbol es 10."),
 ]),
 S(1,"Tabla de frecuencias",[
  D("Tabla de frecuencias","Ordena cada <b>valor</b> con su <b>frecuencia</b>. La suma de las frecuencias da el <b>total de datos</b>."),
  T("Deporte favorito (25 alumnos)",["Deporte","Frecuencia","Porcentaje"],[["Fútbol","10","40%"],["Vóley","6","24%"],["Básquet","5","20%"],["Natación","4","16%"]],"10 + 6 + 5 + 4 = 25. El porcentaje es la frecuencia sobre el total: 10/25 = 40/100 = 40%."),
 ]),
 S(2,"Barras y circular",[
  P("En el <b>gráfico de barras</b>, cada barra mide la frecuencia; la escala del eje tiene que ir de a saltos iguales y los ejes van rotulados. En el <b>circular</b>, cada porción es el porcentaje del total: todo el círculo es el 100%."),
  IMG("Dos gráficos de los mismos datos","Las barras comparan cantidades; el círculo muestra qué parte del total es cada deporte.","Gráfico de barras y gráfico circular del deporte favorito de 25 alumnos.",fig_barras()),
 ]),
 S(2,"Gráfico de líneas",[
  P("Sirve para ver cómo <b>cambia</b> algo con el tiempo. Se marcan los puntos y se unen: si la línea sube, aumenta; si baja, disminuye."),
  E("Temperaturas de una mañana","Se lee punto por punto.",["8 h: 12 °C; 10 h: 15 °C; 12 h: 19 °C.","La línea sube todo el tiempo: la temperatura aumentó.","Entre las 10 y las 12 subió más: 4 grados."]),
 ]),
],
"ejemplo_completo":{"titulo":"las mascotas","planteo":"En un curso de 20 alumnos: 8 tienen perro, 5 gato, 2 pájaro y 5 ninguna. Armá la tabla con porcentajes.","pasos":["Total: 8 + 5 + 2 + 5 = 20.","Perro: 8/20 = 40/100 = 40%.","Gato: 5/20 = 25%. Pájaro: 2/20 = 10%. Ninguna: 25%.","Control: 40 + 25 + 10 + 25 = 100%."]},
"ejemplo_incompleto":{"titulo":"frutas","planteo":"En 10 alumnos, 4 prefieren manzana y el resto banana. Completá los espacios.","pasos":["Banana: 10 − 4 = ___ alumnos.","Manzana: 4/10 = ___ %."]},
"ejemplo_solo":{"titulo":"colores","planteo":"De 50 alumnos, 15 prefieren el azul. ¿Qué porcentaje es?"},
"tip":{"titulo":"Controlá el total","texto":"Las frecuencias tienen que sumar el total de datos, y los porcentajes, 100%."},
"ojo":["Confundir la frecuencia con el valor: \"fútbol\" es el valor y 10 es su frecuencia.","Dibujar barras con una escala desigual o sin rotular los ejes."],
"resumen":[{"titulo":"Variable","texto":"Lo que se pregunta o se mide."},{"titulo":"Frecuencia","texto":"Cuántas veces aparece cada valor."},{"titulo":"Barras","texto":"Comparan cantidades."},{"titulo":"Circular","texto":"Partes del total (100%)."},{"titulo":"Líneas","texto":"Cambios en el tiempo."}],
"glosario":[{"palabra":"Variable","significado":"Lo que se estudia en cada persona o cosa."},{"palabra":"Dato","significado":"Cada respuesta obtenida."},{"palabra":"Frecuencia","significado":"Cantidad de veces que aparece un valor."},{"palabra":"Escala","significado":"Cómo se numera un eje del gráfico."},{"palabra":"Porcentaje","significado":"Cuántos de cada 100."}],
"carpeta":["En una encuesta, 12 alumnos eligieron rojo, 8 azul y 5 verde. ¿Cuántos alumnos respondieron?","De 20 alumnos, 5 eligieron natación. ¿Qué porcentaje es?","En un gráfico circular, ¿cuánto suman todos los porcentajes?","Un compañero dice que en \"rojo: 12\", el dato más repetido es 12. ¿Cuál es el valor más elegido, el color o el número?"],
"respuestas_carpeta":[["25"],["25","25%"],["100","100%"],["color","el color","rojo"]],
"soluciones":{"incompleto":"6. 40%.","solo":"15/50 = 30/100 = 30%.","carpeta":["25: 12 + 8 + 5.","25%: 5/20 = 25/100.","100%: el círculo completo.","El color, rojo: 12 es su frecuencia."]}
}
N2={
"objetivo":"Vas a poder calcular la media y la moda de un conjunto de datos y decidir qué dice cada una.",
"vas_a_ver":["La media aritmética","La moda","Qué dice cada medida","Valores extremos","Media con tablas de frecuencias"],
"secciones":[
 S(1,"La media",[
  D("Media aritmética","La <b>media</b> (o promedio) se calcula <b>sumando todos los datos</b> y <b>dividiendo por la cantidad de datos</b>."),
  IMG("Notas de cinco amigos","La media es la altura que tendrían todas las barras si se emparejaran.","Gráfico de barras con las notas 6, 8, 7, 9 y 10 y una línea en la media 8.",fig_media()),
  E("Notas 6, 8, 7, 9 y 10","Sumamos y dividimos.",["6 + 8 + 7 + 9 + 10 = 40.","Son 5 datos: 40 ÷ 5 = 8.","La media es 8."]),
 ]),
 S(1,"La moda",[
  D("Moda","La <b>moda</b> es el <b>valor que más se repite</b>. Puede haber más de una moda, o ninguna si todos aparecen igual."),
  E("Talles de zapatillas","38, 39, 38, 40, 38, 39.",["El 38 aparece 3 veces, el 39 dos y el 40 una.","La moda es 38."]),
 ]),
 S(2,"Qué dice cada una",[
  P("La <b>media</b> reparte el total en partes iguales: sirve para comparar rendimientos. La <b>moda</b> dice qué es lo más común: sirve para decidir qué talle comprar más o qué sabor gusta más. La moda también sirve con datos que no son números (colores, deportes); la media, no."),
 ]),
 S(2,"Valores extremos",[
  P("Un valor muy distinto de los demás <b>arrastra la media</b>. Sueldos de 300, 320, 310 y 2.070 mil pesos: la media da 750 mil, aunque tres de los cuatro cobran cerca de 300 mil."),
  E("Con tabla de frecuencias","Goles por partido: 0 goles en 2 partidos, 1 gol en 5, 2 goles en 3.",["Total de goles: 0 × 2 + 1 × 5 + 2 × 3 = 11.","Total de partidos: 2 + 5 + 3 = 10.","Media: 11 ÷ 10 = 1,1 goles por partido. Moda: 1 gol."]),
 ]),
],
"ejemplo_completo":{"titulo":"las alturas","planteo":"Alturas de 6 plantas en cm: 12, 15, 12, 18, 14 y 13. Calculá la media y la moda.","pasos":["Suma: 12 + 15 + 12 + 18 + 14 + 13 = 84.","Media: 84 ÷ 6 = 14 cm.","El 12 aparece dos veces y los demás una: la moda es 12 cm."]},
"ejemplo_incompleto":{"titulo":"cuatro notas","planteo":"Notas 7, 9, 8 y 8. Completá los espacios.","pasos":["7 + 9 + 8 + 8 = ___ .","32 ÷ 4 = ___ . La moda es ___ ."]},
"ejemplo_solo":{"titulo":"los minutos","planteo":"Minutos de lectura en 5 días: 20, 30, 25, 30 y 45. ¿Cuál es la media?"},
"tip":{"titulo":"Contá los datos","texto":"Antes de dividir, contá cuántos datos hay, incluidos los repetidos y los ceros."},
"ojo":["Dividir por una cantidad equivocada: hay que contar todos los datos.","Confundir media con moda: la moda es la que más se repite, no el promedio."],
"resumen":[{"titulo":"Media","texto":"Suma ÷ cantidad de datos."},{"titulo":"Moda","texto":"El valor más repetido."},{"titulo":"Para qué","texto":"Media compara; moda dice lo más común."},{"titulo":"Extremos","texto":"Arrastran la media."}],
"glosario":[{"palabra":"Media","significado":"Promedio: suma dividida por la cantidad de datos."},{"palabra":"Moda","significado":"Valor que más se repite."},{"palabra":"Valor extremo","significado":"Dato muy distinto de los demás."},{"palabra":"Promedio","significado":"Otro nombre de la media."}],
"carpeta":["¿Cuál es la media de 4, 6, 8 y 10?","¿Cuál es la moda de 3, 5, 5, 7, 5, 9?","Las notas de Lu son 7, 8 y 9. ¿Qué nota necesita en una cuarta prueba para que la media sea 8?","Un compañero dice que la media de 2, 2, 2 y 10 es 2 porque el 2 se repite. ¿Cuál es la media?"],
"respuestas_carpeta":[["7"],["5"],["8"],["4"]],
"soluciones":{"incompleto":"32. 8. 8.","solo":"150 ÷ 5 = 30 minutos.","carpeta":["7: 28 ÷ 4.","5: aparece tres veces.","8: la suma tiene que dar 32, y 7 + 8 + 9 = 24.","4: 16 ÷ 4. El 2 es la moda, no la media."]}
}
N3={
"objetivo":"Vas a poder distinguir experimentos al azar, escribir todos los resultados posibles y clasificar sucesos en seguros, imposibles y posibles.",
"vas_a_ver":["Experimento aleatorio o determinista","Espacio muestral","Sucesos seguros, imposibles y posibles","Contar casos con tablas","El azar no tiene memoria"],
"secciones":[
 S(1,"Azar o no",[
  D("Aleatorio y determinista","Un experimento es <b>aleatorio</b> si no se puede saber el resultado antes de hacerlo (tirar un dado). Es <b>determinista</b> si el resultado se sabe (soltar una piedra: cae)."),
  E("¿Cuál es cuál?","Preguntamos si se sabe el resultado.",["Tirar una moneda: aleatorio.","Calentar agua a 100 °C a nivel del mar: hierve, determinista.","Sacar una carta de un mazo mezclado: aleatorio."]),
 ]),
 S(1,"Espacio muestral",[
  D("Espacio muestral","Es el <b>conjunto de todos los resultados posibles</b> de un experimento aleatorio."),
  T("Algunos espacios muestrales",["Experimento","Resultados posibles","Cantidad"],[["Tirar una moneda","cara, ceca","2"],["Tirar un dado","1, 2, 3, 4, 5, 6","6"],["Girar una ruleta de 4 colores","rojo, azul, verde, amarillo","4"]]),
 ]),
 S(2,"Sucesos",[
  P("Un <b>suceso</b> es algo que puede pasar al hacer el experimento. Es <b>seguro</b> si pasa siempre, <b>imposible</b> si no pasa nunca y <b>posible</b> si a veces sí y a veces no."),
  E("Con un dado","Miramos los resultados 1 a 6.",["Sacar un número menor que 7: seguro.","Sacar un 8: imposible.","Sacar un número par: posible (2, 4 o 6)."]),
 ]),
 S(2,"Contar casos con una tabla",[
  P("Con dos monedas conviene una tabla para no olvidar casos: cara-cara, cara-ceca, ceca-cara y ceca-ceca. Son <b>4 resultados</b>, no 3: \"una cara y una ceca\" puede salir de dos maneras. El azar <b>no tiene memoria</b>: después de 5 caras, la próxima puede ser cara o ceca igual que siempre."),
 ]),
],
"ejemplo_completo":{"titulo":"dos monedas","planteo":"Se tiran dos monedas. Escribí el espacio muestral y clasificá el suceso \"salen dos cecas\".","pasos":["Primera moneda: cara o ceca. Segunda: cara o ceca.","Resultados: cara-cara, cara-ceca, ceca-cara, ceca-ceca.","Son 4 resultados posibles.","\"Dos cecas\" sale en uno de ellos: es un suceso posible."]},
"ejemplo_incompleto":{"titulo":"la ruleta","planteo":"Una ruleta tiene los números 1 a 8. Completá los espacios.","pasos":["El espacio muestral tiene ___ resultados.","\"Sacar un número mayor que 10\" es un suceso ___ ."]},
"ejemplo_solo":{"titulo":"dado y moneda","planteo":"Se tira un dado y una moneda. ¿Cuántos resultados posibles hay?"},
"tip":{"titulo":"Hacé una tabla","texto":"Cuando hay dos cosas al azar, armá una tabla con una en las filas y la otra en las columnas: así no se escapa ningún caso."},
"ojo":["Olvidar casos: con dos monedas son 4 resultados, no 3.","Pensar que el azar sigue un patrón: después de muchas caras, la ceca no está \"debida\"."],
"resumen":[{"titulo":"Aleatorio","texto":"No se sabe el resultado antes."},{"titulo":"Espacio muestral","texto":"Todos los resultados posibles."},{"titulo":"Sucesos","texto":"Seguro, imposible o posible."},{"titulo":"Contar","texto":"Con tablas, sin olvidar casos."}],
"glosario":[{"palabra":"Aleatorio","significado":"Que depende del azar."},{"palabra":"Determinista","significado":"Que tiene un resultado que se sabe de antemano."},{"palabra":"Espacio muestral","significado":"Lista de todos los resultados posibles."},{"palabra":"Suceso","significado":"Algo que puede pasar en un experimento."},{"palabra":"Resultado","significado":"Lo que sale cada vez que se hace el experimento."}],
"carpeta":["¿Cuántos resultados posibles tiene tirar un dado de 6 caras?","Con un dado, \"sacar un 9\" es un suceso seguro, imposible o posible?","¿Cuántos resultados posibles hay al tirar dos monedas?","Un compañero dice que después de 4 caras seguidas, la próxima tiene que ser ceca. En la próxima tirada, ¿cuántos resultados posibles hay?"],
"respuestas_carpeta":[["6"],["imposible"],["4"],["2"]],
"soluciones":{"incompleto":"8. Imposible.","solo":"6 × 2 = 12 resultados.","carpeta":["6: del 1 al 6.","Imposible: el dado llega al 6.","4: cara-cara, cara-ceca, ceca-cara, ceca-ceca.","2: cara o ceca, igual que siempre. El azar no tiene memoria."]}
}
N4={
"objetivo":"Vas a poder calcular la probabilidad de un suceso simple, escribirla como fracción, decimal y porcentaje, y comparar probabilidades.",
"vas_a_ver":["Casos favorables y posibles","La probabilidad como fracción","Decimal y porcentaje","Entre 0 y 1","Comparar y experimentar"],
"secciones":[
 S(1,"Favorables y posibles",[
  D("Probabilidad","Si todos los resultados tienen la misma chance, la <b>probabilidad</b> de un suceso es <b>casos favorables ÷ casos posibles</b>."),
  E("Sacar un número par en un dado","Contamos.",["Posibles: 1, 2, 3, 4, 5, 6. Son 6.","Favorables: 2, 4 y 6. Son 3.","Probabilidad: 3/6 = 1/2."]),
 ]),
 S(1,"Fracción, decimal y porcentaje",[
  D("Tres formas","La misma probabilidad se puede escribir como <b>fracción</b>, <b>decimal</b> o <b>porcentaje</b>: 1/2 = 0,5 = 50%."),
  T("Una bolsa con 3 rojas, 1 azul y 4 verdes (8 bolitas)",["Sacar","Fracción","Decimal","Porcentaje"],[["Roja","3/8","0,375","37,5%"],["Azul","1/8","0,125","12,5%"],["Verde","4/8 = 1/2","0,5","50%"]]),
 ]),
 S(2,"Siempre entre 0 y 1",[
  P("La probabilidad va de <b>0</b> (suceso imposible) a <b>1</b> (suceso seguro). Nunca da más que 1 ni menos que 0, porque los favorables no pueden ser más que los posibles."),
 ]),
 S(2,"Comparar y experimentar",[
  P("Para comparar, se pasan a la misma forma: en la bolsa, verde (50%) es más probable que roja (37,5%). Si se repite un experimento muchas veces, la <b>frecuencia</b> de un resultado se acerca a su probabilidad: tirando 600 veces un dado, el 6 sale cerca de 100 veces."),
 ]),
],
"ejemplo_completo":{"titulo":"la caja de caramelos","planteo":"Una caja tiene 5 caramelos de menta, 3 de frutilla y 2 de limón. Se saca uno sin mirar. ¿Qué probabilidad hay de que sea de menta? Escribila de las tres formas.","pasos":["Posibles: 5 + 3 + 2 = 10.","Favorables (menta): 5.","Probabilidad: 5/10 = 1/2.","Decimal: 0,5. Porcentaje: 50%."]},
"ejemplo_incompleto":{"titulo":"la ruleta","planteo":"Una ruleta tiene 4 partes iguales: 1 roja y 3 azules. Completá los espacios.","pasos":["Probabilidad de roja: ___ /4.","En porcentaje: ___ %."]},
"ejemplo_solo":{"titulo":"el dado","planteo":"¿Cuál es la probabilidad de sacar un número mayor que 4 al tirar un dado? Escribila como fracción irreducible."},
"tip":{"titulo":"Contá dos veces","texto":"Primero contá todos los resultados posibles; después, solo los que te sirven. La probabilidad es el segundo número sobre el primero."},
"ojo":["Poner favorables sobre desfavorables: con 3 rojas y 5 que no, es 3/8, no 3/5.","Creer que un resultado está \"debido\": cada tirada es nueva."],
"resumen":[{"titulo":"Probabilidad","texto":"Favorables ÷ posibles."},{"titulo":"Formas","texto":"1/2 = 0,5 = 50%."},{"titulo":"Rango","texto":"De 0 (imposible) a 1 (seguro)."},{"titulo":"Muchas veces","texto":"La frecuencia se acerca a la probabilidad."}],
"glosario":[{"palabra":"Probabilidad","significado":"Número que mide qué tan posible es un suceso."},{"palabra":"Casos favorables","significado":"Los resultados que cumplen lo que se pide."},{"palabra":"Casos posibles","significado":"Todos los resultados que pueden salir."},{"palabra":"Equiprobables","significado":"Que tienen la misma chance de salir."}],
"carpeta":["¿Cuál es la probabilidad de sacar un 3 al tirar un dado? Escribila como fracción.","Una bolsa tiene 2 bolitas rojas y 8 blancas. ¿Qué porcentaje de probabilidad hay de sacar roja?","¿Cuál es la probabilidad de un suceso imposible?","Un compañero dice que con 3 bolitas rojas y 5 blancas, la probabilidad de roja es 3/5. ¿Cuántos casos posibles hay en realidad?"],
"respuestas_carpeta":[["1/6"],["20","20%"],["0"],["8"]],
"soluciones":{"incompleto":"1/4. 25%.","solo":"Favorables: 5 y 6. 2/6 = 1/3.","carpeta":["1/6: un caso favorable de 6.","20%: 2/10 = 20/100.","0.","8: 3 + 5. La probabilidad es 3/8."]}
}
ACT={
"1":[N("En una encuesta, {a} alumnos eligieron fútbol, {b} vóley y {c} básquet. ¿Cuántos respondieron?",{"formula":"a+b+c"},"Se suman todas las frecuencias.",{"vars":{"a":{"min":5,"max":20},"b":{"min":3,"max":15},"c":{"min":2,"max":12}}}),
     MC("De 20 alumnos, 4 eligieron natación. ¿Qué porcentaje es?",["4%","20%","40%","80%"],"20%","4/20 = 20/100.")],
"2":[N("¿Cuál es la media de 5, 7, 9 y 11?",{"acepta":[8]},"32 ÷ 4 = 8."),
     MC("¿Cuál es la moda de 2, 4, 4, 6, 4, 8?",["4","6","4,67","8"],"4","El 4 aparece tres veces.")],
"3":[{"t":"classify","p":"Al tirar un dado, clasificá cada suceso.","o":{"elementos":["Sacar un 7","Sacar menos de 7","Sacar un 5","Sacar un número impar"],"categorias":["Seguro","Imposible","Posible"]},"r":{"categorias":{"Sacar un 7":"Imposible","Sacar menos de 7":"Seguro","Sacar un 5":"Posible","Sacar un número impar":"Posible"}},"e":"El dado va del 1 al 6."},
     N("¿Cuántos resultados posibles hay al tirar un dado y una moneda?",{"acepta":[12]},"6 × 2 = 12.")],
"4":[MC("¿Cuál es la probabilidad de sacar un número par al tirar un dado?",["1/6","1/3","1/2","2/3"],"1/2","3 favorables de 6 posibles."),
     N("Una bolsa tiene {r} bolitas rojas y {b} azules. ¿Qué porcentaje de probabilidad hay de sacar roja?",{"formula":"r*100/(r+b)"},"Favorables ÷ posibles, llevado a 100.",{"vars":{"r":{"min":1,"max":9},"b":{"min":1,"max":19}},"reglas":["(r*100)%(r+b)==0"]})],
"5":[N("Relámpago. Media de 2, 4 y 6.",{"acepta":[4]},"12 ÷ 3.",tiempo=20),
     MC("Relámpago. Sacar un 8 con un dado es…",["Seguro","Imposible","Posible"],"Imposible","El dado llega al 6.",tiempo=15),
     MC("Relámpago. Probabilidad de cara al tirar una moneda.",["1/4","1/2","1"],"1/2","1 de 2.",tiempo=15),
     N("Relámpago. Volumen de un prisma de 2 × 3 × 4 cm (en cm³).",{"acepta":[24]},"Repaso de la misión 19.",tiempo=30)],
}
EXAMEN=[
 [1,N("Respondieron 8 alumnos rojo, 7 azul y 5 verde. ¿Cuántos respondieron en total?",{"acepta":[20]},"8 + 7 + 5.")],
 [1,N("De 25 alumnos, 10 prefieren fútbol. ¿Qué porcentaje es?",{"acepta":[40]},"10/25 = 40/100.")],
 [1,MC("¿Qué gráfico conviene para ver cómo cambia la temperatura durante el día?",["Barras","Circular","Líneas","Ninguno"],"Líneas","Muestra cambios en el tiempo.")],
 [2,N("¿Cuál es la media de 3, 5, 7, 9 y 11?",{"acepta":[7]},"35 ÷ 5.")],
 [2,N("¿Cuál es la moda de 6, 7, 7, 8, 9, 7, 10?",{"acepta":[7]},"Aparece tres veces.")],
 [2,VF("La media de 1, 1, 1 y 9 es 1.","Falso","12 ÷ 4 = 3. El 1 es la moda.")],
 [3,MC("¿Cuál de estos experimentos es aleatorio?",["Soltar una piedra","Tirar un dado","Hervir agua a 100 °C","Sumar 2 + 2"],"Tirar un dado","No se sabe el resultado antes.")],
 [3,N("¿Cuántos resultados posibles hay al tirar dos monedas?",{"acepta":[4]},"Cara-cara, cara-ceca, ceca-cara, ceca-ceca.")],
 [3,MC("Con un dado, \"sacar un número menor que 7\" es un suceso…",["Seguro","Imposible","Posible"],"Seguro","Pasa siempre.")],
 [4,MC("Una bolsa tiene 3 bolitas rojas y 5 azules. ¿Cuál es la probabilidad de sacar roja?",["3/5","3/8","5/8","1/3"],"3/8","3 favorables de 8 posibles.")],
 [4,N("Una ruleta tiene 4 partes iguales y una sola es amarilla. ¿Qué porcentaje de probabilidad hay de que salga amarillo?",{"acepta":[25]},"1/4 = 25%.")],
 [4,VF("Una probabilidad puede valer 1,5.","Falso","Va de 0 a 1.")],
 [4,N("¿Cuál es la probabilidad de un suceso seguro?",{"acepta":[1]},"Siempre pasa: vale 1.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":20,"practica":"Práctica general: estadística y probabilidad","examen_titulo":"Nivel jefe: estadística y probabilidad",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-20.json"),"w"),ensure_ascii=False)
print("ok")
