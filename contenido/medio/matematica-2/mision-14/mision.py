# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 14 · Organizaciones rectangulares. Genera mision-14.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (alfajores ordenados en filas en las bandejas grandes).
Niveles: 1 contar filas y columnas · 2 arreglos rectangulares · 3 multiplicar para contar · 4 problemas con filas y columnas."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), "matematica-1"))  # dibujos compartidos del Medio
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
N = lambda p, r, e, **k: {"t": "numeric", "p": p, "o": {}, "r": {"acepta": [r]}, "e": e, **k}
TF = lambda p, ok, e, **k: {"t": "true_false", "p": p, "o": ["VERDADERO", "FALSO"], "r": {"correcta": ok}, "e": e, **k}
UNI = lambda p, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": [a for a, _ in pares], "derecha": [b for _, b in pares]}, "r": {"pares": dict(pares)}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a contar filas y columnas.",
"vas_a_ver": ["Qué es una fila", "Qué es una columna", "Contar las dos"],
"secciones": [
 S(1, "Filas y columnas", [
  P("Rosa ordena los alfajores en la bandeja grande."),
  D("Fila y columna", "La <b>fila</b> va acostada, de lado a lado. La <b>columna</b> va parada, de arriba abajo."),
  IMG("La bandeja", "3 filas y 4 columnas.", FG.arreglo("manzana", 3, 4, contar=False)),
 ]),
 S(1, "Contar las dos", [
  P("Contamos las filas: <b>1, 2, 3</b>."),
  P("Contamos las columnas: <b>1, 2, 3, 4</b>."),
  IMG("Otra bandeja", "2 filas y 5 columnas.", FG.arreglo("estrella", 2, 5, contar=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la bandeja. La vas a usar en la carpeta."),
  IMG("Bandeja para contar", "Contá filas y columnas.", FG.arreglo("caramelo", 4, 3, contar=False)),
 ]),
],
"ejemplo_completo": {"titulo": "Las sillas", "planteo": "En el aula hay sillas en 4 filas de 5.", "pasos": ["Filas: 4, acostadas.", "Columnas: 5, paradas.", "4 filas y 5 columnas."]},
"ejemplo_incompleto": {"titulo": "La caja de huevos", "planteo": "Una caja tiene 2 filas de 6. Completá.", "pasos": ["Tiene ___ filas.", "Tiene ___ columnas."]},
"ejemplo_solo": {"titulo": "Tu bandeja", "planteo": "Dibujá 3 filas de 2 círculos."},
"tip": {"titulo": "Acostada o parada", "texto": "Fila acostada, columna parada."},
"ojo": ["No confundas fila con columna.", "Todas las filas tienen la misma cantidad."],
"resumen": [{"titulo": "Fila", "texto": "De lado a lado."}, {"titulo": "Columna", "texto": "De arriba abajo."}, {"titulo": "Contar", "texto": "Las dos."}],
"glosario": [{"palabra": "Fila", "significado": "Cosas una al lado de la otra."}, {"palabra": "Columna", "significado": "Cosas una arriba de la otra."}],
"carpeta": ["¿Cuántas filas tiene la bandeja?", "¿Cuántas columnas tiene?", "Tomi dice que tiene 4 columnas. ¿Cuántas tiene?"],
"carpeta_nivel": ["recordar", "recordar", "error"],
"respuestas_carpeta": [["4"], ["3"], ["3"]],
"soluciones": {"incompleto": "2. 6.", "solo": "Dibujo con 3 filas de 2.", "carpeta": ["4.", "3.", "3: Tomi contó las filas."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a armar y reconocer arreglos rectangulares.",
"vas_a_ver": ["Qué es un arreglo", "Todas las filas iguales", "Armar arreglos"],
"secciones": [
 S(1, "Un arreglo", [
  D("Arreglo rectangular", "Objetos ordenados en <b>filas iguales</b>. Forman un rectángulo."),
  P("3 filas de 5 alfajores: <b>5, 10, 15</b>."),
  IMG("3 filas de 5", "5, 10, 15.", FG.arreglo("manzana", 3, 5, "3 filas de 5")),
 ]),
 S(1, "Filas iguales", [
  P("Si una fila tiene menos, <b>no</b> es un arreglo."),
  P("12 alfajores entran en 2 filas de 6."),
  P("También entran en 3 filas de 4."),
  IMG("2 filas de 6", "6, 12.", FG.arreglo("estrella", 2, 6, "2 filas de 6")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el arreglo. Lo vas a usar en la carpeta."),
  IMG("Arreglo de Rosa", "Contá de fila en fila.", FG.arreglo("pelota", 4, 5, contar=False)),
 ]),
],
"ejemplo_completo": {"titulo": "Los botones", "planteo": "Ordeno 10 botones en 2 filas iguales.", "pasos": ["10 en 2 filas.", "Cada fila tiene 5.", "Es un arreglo de 2 filas de 5."]},
"ejemplo_incompleto": {"titulo": "Arreglo de 8", "planteo": "8 figuritas en 2 filas. Completá.", "pasos": ["Cada fila tiene ___ .", "4, ___ ."]},
"ejemplo_solo": {"titulo": "Tu arreglo", "planteo": "Dibujá 6 estrellas en 2 filas iguales."},
"tip": {"titulo": "Contá de fila en fila", "texto": "Sumá lo que tiene cada fila."},
"ojo": ["Las filas tienen que ser iguales.", "Un mismo número se ordena de varias formas."],
"resumen": [{"titulo": "Arreglo", "texto": "Filas iguales."}, {"titulo": "Rectángulo", "texto": "La forma que tiene."}, {"titulo": "Contar", "texto": "De fila en fila."}],
"glosario": [{"palabra": "Arreglo", "significado": "Objetos en filas y columnas iguales."}, {"palabra": "Rectángulo", "significado": "Figura de cuatro lados con esquinas rectas."}],
"carpeta": ["¿Cuántas filas tiene el arreglo?", "¿Cuántas pelotas hay en total?", "Sofi dice que son 9 pelotas. ¿Cuántas hay?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["4"], ["20"], ["20"]],
"soluciones": {"incompleto": "4. 8.", "solo": "2 filas de 3.", "carpeta": ["4.", "20: 5, 10, 15, 20.", "20: Sofi sumó 4 + 5."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a multiplicar para contar un arreglo.",
"vas_a_ver": ["Filas por columnas", "Más rápido que contar", "Dar vuelta el arreglo"],
"secciones": [
 S(1, "Filas por columnas", [
  P("Una bandeja tiene 3 filas de 4 alfajores."),
  D("Multiplicar para contar", "Multiplicamos <b>filas × columnas</b>: 3 × 4 = <b>12</b>."),
  IMG("3 filas de 4", "3 × 4 = 12.", FG.arreglo("manzana", 3, 4, "3 × 4 = 12")),
 ]),
 S(1, "Dar vuelta", [
  P("Si giramos la bandeja, quedan 4 filas de 3."),
  P("4 × 3 = <b>12</b>. ¡Da lo mismo!"),
  IMG("4 filas de 3", "4 × 3 = 12.", FG.arreglo("manzana", 4, 3, "4 × 3 = 12")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el arreglo. Lo vas a usar en la carpeta."),
  IMG("Arreglo para multiplicar", "Filas × columnas.", FG.arreglo("estrella", 2, 5, contar=False)),
 ]),
],
"ejemplo_completo": {"titulo": "5 filas de 2", "planteo": "¿Cuántos hay en 5 filas de 2?", "pasos": ["Filas: 5. Columnas: 2.", "5 × 2 = 10.", "Hay 10."]},
"ejemplo_incompleto": {"titulo": "3 filas de 10", "planteo": "Completá.", "pasos": ["3 × 10 = ___ .", "10 × 3 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "¿Cuántos hay en 4 filas de 5?"},
"tip": {"titulo": "Filas × columnas", "texto": "Multiplicar es más rápido que contar uno por uno."},
"ojo": ["3 × 4 no es 3 + 4.", "Girar el arreglo no cambia el total."],
"resumen": [{"titulo": "Filas × columnas", "texto": "Da el total."}, {"titulo": "Rápido", "texto": "No contamos de a uno."}, {"titulo": "Girar", "texto": "Da lo mismo."}],
"glosario": [{"palabra": "Total", "significado": "Todos juntos."}, {"palabra": "Girar", "significado": "Dar vuelta."}],
"carpeta": ["¿Qué cuenta sirve para el arreglo? Escribí filas × columnas.", "¿Cuántas estrellas hay?", "Tomi dice 2 × 5 = 7. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["2 × 5", "2 x 5", "2 por 5"], ["10"], ["10"]],
"soluciones": {"incompleto": "30. 30.", "solo": "20.", "carpeta": ["2 × 5.", "10.", "10: Tomi sumó."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas con filas y columnas.",
"vas_a_ver": ["Encontrar el arreglo", "Multiplicar", "Responder"],
"secciones": [
 S(1, "Encontrar el arreglo", [
  P("En el acto, las sillas están en 4 filas de 10. ¿Cuántas sillas hay?"),
  D("Problema de arreglo", "Buscamos <b>las filas</b> y <b>cuántos hay en cada fila</b>."),
  P("4 × 10 = <b>40</b>. Hay 40 sillas."),
  IMG("Las filas de 10", "10, 20, 30, 40.", FG.tren_paso(10, 40, 10)),
 ]),
 S(1, "Otro problema", [
  P("Una caja de huevos tiene 2 filas de 6. 2 × 6 = <b>12</b>."),
  IMG("La caja de huevos", "2 × 6 = 12.", FG.arreglo("pelota", 2, 6, "2 × 6 = 12")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el arreglo. Lo vas a usar en la carpeta."),
  IMG("El jardín de Rosa", "Filas de flores.", FG.arreglo("estrella", 3, 5, contar=False)),
 ]),
],
"ejemplo_completo": {"titulo": "El chocolate", "planteo": "Una barra tiene 3 filas de 5 cuadraditos.", "pasos": ["3 filas, 5 en cada una.", "3 × 5 = 15.", "Tiene 15 cuadraditos."]},
"ejemplo_incompleto": {"titulo": "Las baldosas", "planteo": "Un patio tiene 5 filas de 4 baldosas. Completá.", "pasos": ["Son ___ filas de ___ .", "5 × 4 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "En un estante hay 2 filas de 10 libros. ¿Cuántos libros hay?"},
"tip": {"titulo": "Dibujá si hace falta", "texto": "Un dibujo de filas ayuda a pensar."},
"ojo": ["Multiplicá filas por columnas.", "Escribí la respuesta con palabras."],
"resumen": [{"titulo": "Buscar", "texto": "Filas y columnas."}, {"titulo": "Multiplicar", "texto": "Filas × columnas."}, {"titulo": "Responder", "texto": "Con palabras."}],
"glosario": [{"palabra": "Problema", "significado": "Una pregunta que se resuelve con cuentas."}, {"palabra": "Respuesta", "significado": "Lo que contesta la pregunta."}],
"carpeta": ["¿Cuántas filas de flores hay?", "¿Cuántas flores hay en total?", "Sofi contestó 8. ¿Qué hizo mal?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["3"], ["15"], ["sumó", "sumó 3 + 5", "sumo"]],
"soluciones": {"incompleto": "5 filas de 4. 20.", "solo": "20 libros.", "carpeta": ["3.", "15: 3 × 5.", "Sumó 3 + 5 en vez de multiplicar."]},
}

ACT = {
"1": [N("UNA BANDEJA TIENE 3 FILAS Y 4 COLUMNAS. ¿CUÁNTAS FILAS?", 3, "LA FILA VA ACOSTADA.", n="recordar"),
      TF("LA COLUMNA VA DE ARRIBA ABAJO.", "VERDADERO", "LA COLUMNA VA PARADA.", n="recordar"),
      UNI("UNÍ CADA PALABRA CON SU FORMA.", [("FILA", "ACOSTADA"), ("COLUMNA", "PARADA")], "FILA ACOSTADA, COLUMNA PARADA.", n="analizar")],
"2": [N("3 FILAS DE 5 ALFAJORES. ¿CUÁNTOS SON?", 15, "5, 10, 15.", n="aplicar"),
      TF("2 FILAS: UNA DE 6 Y OTRA DE 4. ES UN ARREGLO.", "FALSO", "LAS FILAS TIENEN QUE SER IGUALES.", n="analizar")],
"3": [N("¿CUÁNTOS HAY EN 4 FILAS DE 3?", 12, "4 × 3 = 12.", n="aplicar"),
      MC("SI GIRO 3 FILAS DE 4, ¿QUÉ PASA CON EL TOTAL?", ["QUEDA IGUAL", "AUMENTA", "BAJA"], "QUEDA IGUAL", "4 × 3 = 3 × 4 = 12.", n="analizar")],
"4": [N("HAY 4 FILAS DE 10 SILLAS. ¿CUÁNTAS SILLAS?", 40, "4 × 10 = 40.", n="aplicar"),
      N("UNA CAJA TIENE 2 FILAS DE 6 HUEVOS. ¿CUÁNTOS HUEVOS?", 12, "2 × 6 = 12.", n="aplicar")],
"5": [N("RELÁMPAGO. 2 FILAS DE 5 = ___", 10, "2 × 5.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 3 FILAS DE 10 = ___", 30, "3 × 10.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA FILA VA…", ["ACOSTADA", "PARADA"], "ACOSTADA", "DE LADO A LADO.", tiempo=30, n="recordar"),
      N("RELÁMPAGO. 5 FILAS DE 2 = ___", 10, "5 × 2.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, N("UN ARREGLO TIENE 2 FILAS Y 5 COLUMNAS. ¿CUÁNTAS COLUMNAS?", 5, "LA COLUMNA VA PARADA.", n="recordar")],
 [1, TF("TOMI DICE QUE LA FILA VA DE ARRIBA ABAJO.", "FALSO", "LA FILA VA ACOSTADA.", n="error")],
 [2, N("4 FILAS DE 5. ¿CUÁNTOS HAY?", 20, "5, 10, 15, 20.", n="aplicar")],
 [2, MC("12 ALFAJORES EN FILAS IGUALES. ¿CUÁL SIRVE?", ["3 FILAS DE 4", "3 FILAS DE 5", "2 FILAS DE 5"], "3 FILAS DE 4", "3 × 4 = 12.", n="analizar")],
 [2, TF("UNA FILA DE 5 Y OTRA DE 3 FORMAN UN ARREGLO.", "FALSO", "LAS FILAS TIENEN QUE SER IGUALES.", n="analizar")],
 [3, N("¿CUÁNTOS HAY EN 3 FILAS DE 5?", 15, "3 × 5 = 15.", n="aplicar")],
 [3, N("¿CUÁNTOS HAY EN 5 FILAS DE 10?", 50, "5 × 10 = 50.", n="aplicar")],
 [3, MC("SOFI DICE 2 × 5 = 7. ¿QUÉ HIZO?", ["SUMÓ 2 + 5", "MULTIPLICÓ BIEN", "RESTÓ"], "SUMÓ 2 + 5", "2 × 5 = 10.", n="error")],
 [4, N("UN PATIO TIENE 5 FILAS DE 4 BALDOSAS. ¿CUÁNTAS BALDOSAS?", 20, "5 × 4 = 20.", n="aplicar")],
 [4, N("UNA BARRA TIENE 3 FILAS DE 5 CUADRADITOS. ¿CUÁNTOS?", 15, "3 × 5 = 15.", n="aplicar")],
 [4, UNI("UNÍ CADA PROBLEMA CON SU CUENTA.", [("2 FILAS DE 6 HUEVOS", "2 × 6"), ("4 FILAS DE 10 SILLAS", "4 × 10"), ("3 FILAS DE 5 FLORES", "3 × 5")], "FILAS POR COLUMNAS.", n="analizar")],
 [4, N("HAY 2 FILAS DE 10 LIBROS. ¿CUÁNTOS LIBROS?", 20, "2 × 10 = 20.", n="aplicar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 14, "estilo": "primeros",
     "practica": "Práctica general: organizaciones rectangulares", "examen_titulo": "Nivel jefe: organizaciones rectangulares",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-14.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
