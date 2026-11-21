# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 4 · Los números hasta 100. Genera mision-4.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el álbum nuevo de Tomi, de 100 figuritas (igual que clases.py)."""
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
"objetivo": "Vas a contar del 1 al 100.",
"vas_a_ver": ["Los números redondos hasta 100", "Contar los del sesenta y los del noventa", "Después de un 9 viene un redondo"],
"secciones": [
 S(1, "Los redondos", [
  P("El álbum nuevo de Tomi tiene <b>100 figuritas</b>."),
  P("Los números redondos son: <b>10, 20, 30… 100</b>."),
  IMG("Los redondos", "Del 10 al 100, de 10 en 10.", FG.tren_paso(10, 100, 10)),
 ]),
 S(1, "Después del 9", [
  D("Después de un 9", "Después de un número que termina en 9 viene un <b>redondo</b>: 69, 70."),
  IMG("Los del sesenta", "Del 61 al 70.", FG.tren(61, 70)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("El último tramo", "Del 91 al 100.", FG.tren(91, 100, (93, 99))),
 ]),
],
"ejemplo_completo": {"titulo": "Contar desde el 77", "planteo": "Tomi cuenta desde el 77.", "pasos": ["77, 78, 79.", "Después del 79 viene el 80.", "80, 81, 82."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí los que faltan.", "pasos": ["58, ___ , 60, 61.", "98, 99, ___ ."]},
"ejemplo_solo": {"titulo": "Los redondos", "planteo": "Decí en voz alta los redondos del 10 al 100."},
"tip": {"titulo": "Mirá el 9", "texto": "Después de un 9 viene un redondo."},
"ojo": ["Después del 79 viene el 80, no el 70.", "Después del 99 viene el 100."],
"resumen": [{"titulo": "Hasta 100", "texto": "En orden."}, {"titulo": "Redondos", "texto": "10, 20, 30…"}, {"titulo": "Después del 9", "texto": "Viene un redondo."}],
"glosario": [{"palabra": "Cien", "significado": "El número 100."}, {"palabra": "Redondo", "significado": "Número que termina en 0."}],
"carpeta": ["¿Qué número falta en el primer vagón con ?", "¿Qué número falta en el segundo vagón con ?", "¿Qué número viene después del 79?"],
"respuestas_carpeta": [["93"], ["99"], ["80"]],
"soluciones": {"incompleto": "59. 100.", "solo": "10, 20, 30, 40, 50, 60, 70, 80, 90, 100.", "carpeta": ["93.", "99.", "80."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer la tabla de cien y encontrar números en ella.",
"vas_a_ver": ["La tabla de cien", "Filas y columnas", "La primera cifra te dice la fila"],
"secciones": [
 S(1, "La tabla de cien", [
  P("Tomi pegó todas sus figuritas. Quedó una <b>tabla de cien</b>."),
  IMG("La tabla de cien", "Diez filas de diez números.", FG.cuadro(100)),
 ]),
 S(1, "Filas y columnas", [
  D("Fila y columna", "Una <b>fila</b> va de costado. Una <b>columna</b> va para abajo."),
  P("El 57 está en la fila del cincuenta."),
  IMG("El 57", "Fila del cincuenta.", FG.cuadro(100, resaltar=(57,))),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla. La vas a usar en la carpeta."),
  IMG("La fila del 80", "Pintada en amarillo.", FG.cuadro(100, resaltar=range(81, 91))),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar el 34", "planteo": "¿Dónde está el 34?", "pasos": ["Empieza con 3.", "Está en la fila del treinta.", "Es el cuarto de esa fila."]},
"ejemplo_incompleto": {"titulo": "Buscar el 72", "planteo": "Completá.", "pasos": ["Empieza con ___ .", "Está en la fila del ___ ."]},
"ejemplo_solo": {"titulo": "El 90", "planteo": "¿En qué fila está el 90?"},
"tip": {"titulo": "Mirá la primera cifra", "texto": "Te dice en qué fila buscar."},
"ojo": ["El 90 está al final de la fila del ochenta.", "Fila es de costado; columna, para abajo."],
"resumen": [{"titulo": "Tabla", "texto": "100 números."}, {"titulo": "Fila", "texto": "De costado."}, {"titulo": "Columna", "texto": "Para abajo."}],
"glosario": [{"palabra": "Tabla de cien", "significado": "Los números del 1 al 100 en filas de 10."}, {"palabra": "Fila", "significado": "Números de costado."}],
"carpeta": ["¿Con qué número empieza la fila pintada?", "¿Con qué número termina la fila pintada?", "¿En qué fila está el 34: la del 30 o la del 40?"],
"respuestas_carpeta": [["81"], ["90"], ["30", "la del 30", "del 30", "treinta"]],
"soluciones": {"incompleto": "7. Setenta.", "solo": "Al final de la fila del ochenta.", "carpeta": ["81.", "90.", "La del 30."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a descubrir los secretos de la tabla de cien.",
"vas_a_ver": ["Las columnas terminan igual", "Las filas empiezan igual", "Bajar una fila es sumar 10"],
"secciones": [
 S(1, "Columnas y filas", [
  D("Columnas", "En una columna, todos <b>terminan igual</b>: 3, 13, 23…"),
  IMG("La columna del 3", "Todos terminan en 3.", FG.cuadro(100, resaltar=range(3, 101, 10))),
  D("Filas", "En una fila, todos <b>empiezan igual</b>: 41, 42, 43…"),
 ]),
 S(1, "Abajo suma 10", [
  P("Debajo del 45 está el <b>55</b>. Bajar una fila es <b>sumar 10</b>."),
  IMG("45 y 55", "Uno arriba del otro.", FG.cuadro(100, resaltar=(45, 55))),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla. La vas a usar en la carpeta."),
  IMG("Figuritas perdidas", "Completá los que faltan.", FG.cuadro(100, faltan=(36, 64, 88))),
 ]),
],
"ejemplo_completo": {"titulo": "Debajo del 62", "planteo": "¿Qué número va debajo del 62?", "pasos": ["Bajar una fila es sumar 10.", "62 + 10 = 72.", "Debajo del 62 va el 72."]},
"ejemplo_incompleto": {"titulo": "La columna del 8", "planteo": "Completá.", "pasos": ["8, 18, 28, ___ , 48.", "Todos terminan en ___ ."]},
"ejemplo_solo": {"titulo": "Arriba del 50", "planteo": "¿Qué número va arriba del 50?"},
"tip": {"titulo": "Usá los secretos", "texto": "Fila y columna te dicen dónde va cada número."},
"ojo": ["Debajo del 45 no va el 46: va el 55.", "En una columna todos terminan igual."],
"resumen": [{"titulo": "Filas", "texto": "Empiezan igual."}, {"titulo": "Columnas", "texto": "Terminan igual."}, {"titulo": "Abajo", "texto": "Suma 10."}],
"glosario": [{"palabra": "Regularidad", "significado": "Algo que se repite siempre igual."}, {"palabra": "Columna", "significado": "Números para abajo."}],
"carpeta": ["¿Qué número falta en la fila del 30?", "¿Qué número falta en la fila del 60?", "¿Qué número falta en la fila del 80?"],
"respuestas_carpeta": [["36"], ["64"], ["88"]],
"soluciones": {"incompleto": "38. 8.", "solo": "El 40.", "carpeta": ["36.", "64.", "88."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a contar de a 2, 5 y 10.",
"vas_a_ver": ["Contar de a 2", "Contar de a 5", "Contar de a 10"],
"secciones": [
 S(1, "De a 2", [
  P("Tomi cuenta medias de a pares: <b>2, 4, 6, 8…</b>"),
  IMG("De a 2", "Del 2 al 20.", FG.tren_paso(2, 20, 2)),
 ]),
 S(1, "De a 5 y de a 10", [
  D("De a 5", "5, 10, 15, 20… Terminan en <b>5</b> o en <b>0</b>."),
  IMG("De a 5", "Del 5 al 50.", FG.tren_paso(5, 50, 5)),
  D("De a 10", "10, 20, 30… ¡El más rápido!"),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("¿Qué vagones faltan?", "Contá de a 5.", FG.tren_paso(5, 50, 5, (25, 40))),
 ]),
],
"ejemplo_completo": {"titulo": "Medias", "planteo": "Hay 6 pares de medias. ¿Cuántas medias son?", "pasos": ["Contamos de a 2.", "2, 4, 6, 8, 10, 12.", "Son 12 medias."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí el que sigue.", "pasos": ["2, 4, 6, ___ .", "10, 20, 30, ___ ."]},
"ejemplo_solo": {"titulo": "Manos", "planteo": "¿Cuántos dedos hay en 3 manos? Contá de a 5."},
"tip": {"titulo": "Elegí el salto", "texto": "De a 10 es el más rápido."},
"ojo": ["De a 2 no se dice 3: 2, 4, 6.", "De a 5 terminan en 5 o en 0."],
"resumen": [{"titulo": "De a 2", "texto": "2, 4, 6…"}, {"titulo": "De a 5", "texto": "5, 10, 15…"}, {"titulo": "De a 10", "texto": "10, 20, 30…"}],
"glosario": [{"palabra": "Par", "significado": "Dos cosas juntas."}, {"palabra": "Saltar", "significado": "Contar sin decir todos los números."}],
"carpeta": ["¿Qué número falta en el primer vagón con ?", "¿Qué número falta en el segundo vagón con ?", "¿Qué sigue? 10, 20, 30, ___"],
"respuestas_carpeta": [["25"], ["40"], ["40"]],
"soluciones": {"incompleto": "8. 40.", "solo": "15: 5, 10, 15.", "carpeta": ["25.", "40.", "40."]},
}

ACT = {
"1": [N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 79?", 80, "DESPUÉS DE UN 9 VIENE UN REDONDO."),
      N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 99?", 100, "99, 100.")],
"2": [MC("¿EN QUÉ FILA ESTÁ EL 34?", ["LA DEL 30", "LA DEL 40", "LA DEL 20"], "LA DEL 30", "EMPIEZA CON 3."),
      MC("¿CUÁNTOS NÚMEROS TIENE LA TABLA DE CIEN?", ["10", "50", "100"], "100", "DIEZ FILAS DE DIEZ.")],
"3": [N("¿QUÉ NÚMERO VA DEBAJO DEL 45?", 55, "BAJAR UNA FILA ES SUMAR 10."),
      MC("3, 13, 23, 33… ¿QUÉ SIGUE?", ["34", "43", "44"], "43", "TODOS TERMINAN EN 3.")],
"4": [N("2, 4, 6, 8… ¿QUÉ SIGUE?", 10, "DE A 2."),
      N("5, 10, 15… ¿QUÉ SIGUE?", 20, "DE A 5.")],
"5": [N("RELÁMPAGO. ¿QUÉ SIGUE DESPUÉS DEL 69?", 70, "69, 70.", tiempo=30),
      N("RELÁMPAGO. 10, 20, 30… ¿QUÉ SIGUE?", 40, "DE A 10.", tiempo=30),
      N("RELÁMPAGO. ¿QUÉ VA DEBAJO DEL 23?", 33, "SUMA 10.", tiempo=30),
      N("RELÁMPAGO. 2, 4, 6… ¿QUÉ SIGUE?", 8, "DE A 2.", tiempo=30)],
}
EXAMEN = [
 [1, N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 59?", 60, "59, 60.")],
 [1, N("¿QUÉ NÚMERO FALTA? 86, 87, ___, 89", 88, "87, 88, 89.")],
 [1, MC("¿CUÁL ES UN NÚMERO REDONDO?", ["70", "73", "77"], "70", "TERMINA EN 0.")],
 [2, MC("¿EN QUÉ FILA ESTÁ EL 72?", ["LA DEL 70", "LA DEL 20", "LA DEL 80"], "LA DEL 70", "EMPIEZA CON 7.")],
 [2, MC("UNA COLUMNA VA…", ["PARA ABAJO", "DE COSTADO"], "PARA ABAJO", "LA FILA VA DE COSTADO.")],
 [2, N("¿CON QUÉ NÚMERO TERMINA LA FILA DEL 40?", 50, "41, 42… 50.")],
 [3, N("¿QUÉ NÚMERO VA DEBAJO DEL 62?", 72, "62 + 10 = 72.")],
 [3, MC("8, 18, 28, 38… ¿QUÉ SIGUE?", ["39", "48", "40"], "48", "TODOS TERMINAN EN 8.")],
 [3, N("¿QUÉ NÚMERO VA ARRIBA DEL 50?", 40, "ARRIBA RESTA 10.")],
 [4, N("2, 4, 6, 8, 10… ¿QUÉ SIGUE?", 12, "DE A 2.")],
 [4, N("5, 10, 15, 20… ¿QUÉ SIGUE?", 25, "DE A 5.")],
 [4, N("10, 20, 30, 40… ¿QUÉ SIGUE?", 50, "DE A 10.")],
 [4, N("¿CUÁNTOS DEDOS HAY EN 3 MANOS?", 15, "5, 10, 15.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: los números hasta 100", "examen_titulo": "Nivel jefe: los números hasta 100",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
