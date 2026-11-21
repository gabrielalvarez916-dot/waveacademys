# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 2 · Los números hasta 20. Genera mision-2.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: el tren de los números de Tomi (igual que en las clases animadas, clases.py)."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
N = lambda p, r, e, **k: {"t": "numeric", "p": p, "o": {}, "r": {"acepta": [r]}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a contar, leer y ordenar los números del 1 al 10.",
"vas_a_ver": ["Los números del 1 al 10", "Contar con las dos manos", "El último número dice cuántos hay"],
"secciones": [
 S(1, "El tren del 1 al 10", [
  P("Tomi viaja en el tren de los números."),
  P("Cada vagón tiene su número: <b>1, 2, 3… hasta el 10</b>."),
  IMG("El tren de Tomi", "Diez vagones, del 1 al 10.", FG.tren(1, 10)),
 ]),
 S(1, "Contar hasta 10", [
  D("Dos manos", "En tus <b>dos manos</b> tenés <b>10 dedos</b>. Te ayudan a contar."),
  IMG("Las manzanas", "El último número es 7: hay 7 manzanas.", FG.contar_numerado("manzana", 7, "7 manzanas")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Grupos A, B y C", "Contá cada grupo con el dedo.", FG.grupos_letras([("A", "pelota", 4), ("B", "estrella", 8), ("C", "caramelo", 10)])),
 ]),
],
"ejemplo_completo": {"titulo": "Los vagones", "planteo": "Tomi cuenta los vagones del tren.", "pasos": ["Toca cada vagón y dice un número.", "1, 2, 3, 4, 5, 6.", "El último número es 6: hay 6 vagones."]},
"ejemplo_incompleto": {"titulo": "Los números en orden", "planteo": "Completá los números que faltan.", "pasos": ["1, 2, 3, ___ , 5.", "6, ___ , 8, 9, 10."]},
"ejemplo_solo": {"titulo": "Tus dedos", "planteo": "Contá los dedos de una mano. ¿Cuántos son?"},
"tip": {"titulo": "Usá tus manos", "texto": "Levantá un dedo por cada número que decís."},
"ojo": ["No te saltees ningún número.", "Decilos siempre en orden."],
"resumen": [{"titulo": "Del 1 al 10", "texto": "Siempre en orden."}, {"titulo": "Dos manos", "texto": "Diez dedos."}, {"titulo": "Cuántos hay", "texto": "Lo dice el último número."}],
"glosario": [{"palabra": "Número", "significado": "Lo que usamos para contar."}, {"palabra": "Orden", "significado": "Uno detrás de otro, sin saltear."}],
"carpeta": ["¿Cuántas pelotas hay en el grupo A?", "¿Cuántas estrellas hay en el grupo B?", "¿Cuántos caramelos hay en el grupo C?"],
"respuestas_carpeta": [["4"], ["8"], ["10"]],
"soluciones": {"incompleto": "4. 7.", "solo": "5 dedos.", "carpeta": ["4.", "8.", "10."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar del 11 al 20 con una caja de 10.",
"vas_a_ver": ["Diez y algo más", "Del 11 al 19", "El 20 es diez y diez"],
"secciones": [
 S(1, "Diez y algo más", [
  P("Esta caja tiene <b>10 caramelos</b>. Al lado hay 3 sueltos."),
  P("Contamos desde el 10: <b>11, 12, 13</b>."),
  IMG("Caramelos", "10 y 3 son 13.", FG.diez_y_mas("caramelo", 13, "10 y 3 son 13")),
 ]),
 S(1, "El tren hasta el 20", [
  D("Del 11 al 19", "Cada número es <b>diez y algo más</b>. El <b>20</b> es diez y diez."),
  IMG("El tren sigue", "Del 11 al 20.", FG.tren(11, 20)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cajas. Las vas a usar en la carpeta."),
  IMG("Caja A", "Una caja de 10 y sueltos.", FG.diez_y_mas("estrella", 12)),
  IMG("Caja B", "Una caja de 10 y sueltos.", FG.diez_y_mas("pelota", 16)),
 ]),
],
"ejemplo_completo": {"titulo": "Estrellas", "planteo": "Hay una caja de 10 estrellas y 4 sueltas.", "pasos": ["Empezamos en 10.", "Seguimos: 11, 12, 13, 14.", "10 y 4 son 14."]},
"ejemplo_incompleto": {"titulo": "Pelotas", "planteo": "Hay una caja de 10 pelotas y 6 sueltas.", "pasos": ["Empezamos en ___ .", "Seguimos: 11, 12, 13, 14, 15, ___ .", "10 y 6 son ___ ."]},
"ejemplo_solo": {"titulo": "Lápices", "planteo": "Tenés 10 lápices y te regalan 9. ¿Cuántos tenés?"},
"tip": {"titulo": "Empezá en 10", "texto": "No cuentes la caja de nuevo: arrancá en 10."},
"ojo": ["Diez y seis es 16, no 106.", "Después del 19 viene el 20."],
"resumen": [{"titulo": "Caja de 10", "texto": "Arrancamos a contar en 10."}, {"titulo": "11 al 19", "texto": "Diez y algo más."}, {"titulo": "20", "texto": "Diez y diez."}],
"glosario": [{"palabra": "Diez", "significado": "Un grupo de 10 cosas."}, {"palabra": "Veinte", "significado": "Dos grupos de 10."}],
"carpeta": ["¿Cuántas estrellas hay en la caja A en total?", "¿Cuántas pelotas hay en la caja B en total?", "¿Qué número viene después del 19?"],
"respuestas_carpeta": [["12"], ["16"], ["20"]],
"soluciones": {"incompleto": "10. 16. 16.", "solo": "19 lápices: 10 y 9.", "carpeta": ["12: 10 y 2.", "16: 10 y 6.", "20."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir los números con cifras y leerlos con palabras.",
"vas_a_ver": ["Escribir con cifras", "Leer con palabras", "Del 10 al 19 empiezan con 1"],
"secciones": [
 S(1, "Cifras y palabras", [
  P("Un número se puede <b>escribir con cifras</b> o <b>leer con palabras</b>."),
  P("12 se lee <b>doce</b>. 15 se lee <b>quince</b>."),
  IMG("Tarjetas", "Cada número con su nombre.", FG.tarjetas([(12, "doce"), (15, "quince"), (18, "dieciocho")])),
 ]),
 S(1, "Primero el 1", [
  D("Del 10 al 19", "Todos empiezan con <b>1</b>. Doce es un 1 y un 2: <b>12</b>."),
  IMG("Del 10 al 19", "Todos empiezan con 1.", FG.tarjetas([(10, "diez"), (11, "once"), (13, "trece"), (19, "diecinueve")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas para completar", "Escribí el nombre que falta.", FG.tarjetas([(14, "catorce"), (16, "dieciséis"), (20, "veinte")], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Trece", "planteo": "¿Cómo se escribe trece?", "pasos": ["Trece empieza con 1.", "Después va el 3.", "Se escribe 13."]},
"ejemplo_incompleto": {"titulo": "Diecisiete", "planteo": "Completá.", "pasos": ["Diecisiete empieza con ___ .", "Después va el 7.", "Se escribe ___ ."]},
"ejemplo_solo": {"titulo": "Tu edad", "planteo": "Escribí con cifras cuántos años tenés."},
"tip": {"titulo": "Mirá el primero", "texto": "Del 10 al 19, la primera cifra es 1."},
"ojo": ["Doce es 12, no 21.", "Mirá bien el orden de las cifras."],
"resumen": [{"titulo": "Escribir", "texto": "Con cifras: 12."}, {"titulo": "Leer", "texto": "Con palabras: doce."}, {"titulo": "Del 10 al 19", "texto": "Empiezan con 1."}],
"glosario": [{"palabra": "Cifra", "significado": "Cada símbolo: 0, 1, 2… 9."}, {"palabra": "Leer", "significado": "Decir el nombre del número."}],
"carpeta": ["Escribí con palabras el número 14.", "Escribí con palabras el número 20.", "Escribí con cifras: dieciséis."],
"respuestas_carpeta": [["catorce"], ["veinte"], ["16"]],
"soluciones": {"incompleto": "1. 17.", "solo": "Depende de tu edad: por ejemplo, 6 o 7.", "carpeta": ["Catorce.", "Veinte.", "16."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ordenar números hasta 20.",
"vas_a_ver": ["El anterior y el siguiente", "La recta numérica", "Mayor y menor"],
"secciones": [
 S(1, "Anterior y siguiente", [
  D("Anterior y siguiente", "El <b>anterior</b> va antes. El <b>siguiente</b> va después."),
  P("El anterior del 14 es el 13. El siguiente es el 15."),
  IMG("La recta del 10 al 20", "13 va antes del 14. 15 va después.", FG.recta_num(10, 20, [(13, "antes"), (14, ""), (15, "después")])),
 ]),
 S(1, "Mayor y menor", [
  P("En la recta, el número <b>mayor</b> está más lejos del 0."),
  P("18 es mayor que 12. 12 es menor que 18."),
  IMG("12 y 18 en la recta", "18 está más lejos del 0.", FG.recta_num(10, 20, [(12, "menor"), (18, "mayor")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("¿Qué vagones faltan?", "Completá los vagones con ?.", FG.tren(13, 20, (15, 19))),
 ]),
],
"ejemplo_completo": {"titulo": "El 9", "planteo": "¿Cuál es el anterior y el siguiente del 9?", "pasos": ["Antes del 9 va el 8.", "Después del 9 va el 10.", "8, 9, 10."]},
"ejemplo_incompleto": {"titulo": "El 17", "planteo": "Completá.", "pasos": ["Antes del 17 va el ___ .", "Después del 17 va el ___ ."]},
"ejemplo_solo": {"titulo": "Ordenar", "planteo": "Ordená de menor a mayor: 15, 11, 19."},
"tip": {"titulo": "Pensá en la recta", "texto": "Más a la derecha, más grande."},
"ojo": ["El anterior va antes, el siguiente después.", "Mayor es el que está más lejos del 0."],
"resumen": [{"titulo": "Anterior", "texto": "El que va antes."}, {"titulo": "Siguiente", "texto": "El que va después."}, {"titulo": "Mayor", "texto": "Más lejos del 0."}],
"glosario": [{"palabra": "Anterior", "significado": "El número que va antes."}, {"palabra": "Siguiente", "significado": "El número que va después."}],
"carpeta": ["¿Qué número falta en el primer vagón con ?", "¿Qué número falta en el segundo vagón con ?", "¿Cuál es mayor: 16 o 13?"],
"respuestas_carpeta": [["15"], ["19"], ["16"]],
"soluciones": {"incompleto": "16. 18.", "solo": "11, 15, 19.", "carpeta": ["15: va entre 14 y 16.", "19: va entre 18 y 20.", "16: está más lejos del 0."]},
}

ACT = {
"1": [N("¿CUÁNTOS PATITOS HAY? 🐤🐤🐤🐤🐤🐤🐤🐤", 8, "1, 2, 3, 4, 5, 6, 7, 8. HAY 8."),
      MC("¿QUÉ NÚMERO VA DESPUÉS DEL 9?", ["8", "10", "7"], "10", "DESPUÉS DEL 9 VIENE EL 10.")],
"2": [N("📦 10 Y 🍬🍬🍬🍬 ¿CUÁNTOS SON?", 14, "10 Y 4 SON 14."),
      MC("¿CUÁNTO ES 10 Y 6?", ["16", "60", "106"], "16", "DIEZ Y SEIS: 16.")],
"3": [MC("¿CÓMO SE ESCRIBE QUINCE?", ["51", "15", "5"], "15", "QUINCE ES UN 1 Y UN 5: 15."),
      MC("¿CÓMO SE LEE 19?", ["NUEVE", "DIECINUEVE", "NOVENTA"], "DIECINUEVE", "19 SE LEE DIECINUEVE.")],
"4": [N("¿QUÉ NÚMERO VA ANTES DEL 13?", 12, "ANTES DEL 13 VA EL 12."),
      MC("¿CUÁL ES MAYOR?", ["17", "14"], "17", "17 ESTÁ MÁS LEJOS DEL 0.")],
"5": [N("RELÁMPAGO. ¿QUÉ NÚMERO VA DESPUÉS DEL 19?", 20, "DESPUÉS DEL 19 VIENE EL 20.", tiempo=30),
      MC("RELÁMPAGO. ¿CÓMO SE ESCRIBE DOCE?", ["21", "12"], "12", "DOCE ES UN 1 Y UN 2.", tiempo=30),
      N("RELÁMPAGO. 📦 10 Y 🍬🍬🍬 ¿CUÁNTOS SON?", 13, "10 Y 3 SON 13.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES MENOR?", ["11", "18"], "11", "11 ESTÁ MÁS CERCA DEL 0.", tiempo=30)],
}
EXAMEN = [
 [1, N("¿CUÁNTOS SOLES HAY? ☀️☀️☀️☀️☀️☀️", 6, "1, 2, 3, 4, 5, 6.")],
 [1, MC("¿QUÉ NÚMERO FALTA? 1, 2, 3, ___, 5", ["4", "6", "3"], "4", "DESPUÉS DEL 3 VA EL 4.")],
 [1, N("¿CUÁNTOS DEDOS HAY EN DOS MANOS?", 10, "CINCO Y CINCO: 10.")],
 [2, N("📦 10 Y 🍬🍬 ¿CUÁNTOS SON?", 12, "10 Y 2 SON 12.")],
 [2, MC("¿CUÁNTO ES 10 Y 8?", ["18", "80", "108"], "18", "DIEZ Y OCHO: 18.")],
 [2, MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 19?", ["20", "10", "21"], "20", "DESPUÉS DEL 19 VIENE EL 20.")],
 [3, MC("¿CÓMO SE ESCRIBE TRECE?", ["31", "13", "3"], "13", "TRECE ES UN 1 Y UN 3.")],
 [3, MC("¿CÓMO SE LEE 16?", ["SEIS", "DIECISÉIS", "SESENTA"], "DIECISÉIS", "16 SE LEE DIECISÉIS.")],
 [3, MC("¿CÓMO SE ESCRIBE VEINTE?", ["20", "12", "2"], "20", "VEINTE SE ESCRIBE 20.")],
 [4, N("¿QUÉ NÚMERO VA ANTES DEL 15?", 14, "ANTES DEL 15 VA EL 14.")],
 [4, N("¿QUÉ NÚMERO VA DESPUÉS DEL 17?", 18, "DESPUÉS DEL 17 VA EL 18.")],
 [4, MC("¿CUÁL ES MAYOR?", ["13", "19"], "19", "19 ESTÁ MÁS LEJOS DEL 0.")],
 [4, MC("¿CUÁL ES MENOR?", ["16", "10"], "10", "10 ESTÁ MÁS CERCA DEL 0.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: los números hasta 20", "examen_titulo": "Nivel jefe: los números hasta 20",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
