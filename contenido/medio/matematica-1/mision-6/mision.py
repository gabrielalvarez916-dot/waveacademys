# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 6 · Decenas y unidades. Genera mision-6.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el kiosco de la escuela de Sofi (igual que clases.py)."""
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
"objetivo": "Vas a agrupar de a diez para contar más rápido.",
"vas_a_ver": ["Una bolsita tiene 10", "Unidad y decena", "Una decena y algunos sueltos"],
"secciones": [
 S(1, "Una bolsita de 10", [
  P("Sofi guarda los caramelos en bolsitas de <b>10</b>."),
  IMG("Diez caramelos", "Llenan una bolsita.", FG.contar_numerado("caramelo", 10, "1 bolsita")),
 ]),
 S(1, "Unidad y decena", [
  D("Decena", "Un grupo de <b>10</b> es una <b>decena</b>. Un suelto es una <b>unidad</b>."),
  IMG("1 decena y 4 unidades", "10 y 4 son 14.", FG.diez_y_mas("caramelo", 14, "14")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bolsitas. Las vas a usar en la carpeta."),
  IMG("Bolsitas y sueltos", "Contá bolsitas y sueltos.", FG.bolsitas(2, 5)),
 ]),
],
"ejemplo_completo": {"titulo": "16 caramelos", "planteo": "Sofi tiene 16 caramelos.", "pasos": ["Llena 1 bolsita con 10.", "Le sobran 6 sueltos.", "16 = 1 decena y 6 unidades."]},
"ejemplo_incompleto": {"titulo": "20 caramelos", "planteo": "Completá.", "pasos": ["Con 20 llena ___ bolsitas.", "Le sobran ___ sueltos."]},
"ejemplo_solo": {"titulo": "Tus lápices", "planteo": "Si tenés 12 lápices, ¿cuántos grupos de 10 armás?"},
"tip": {"titulo": "Agrupá de a 10", "texto": "Así contás más rápido."},
"ojo": ["Una bolsita tiene 10, no 5.", "Los sueltos son menos de 10."],
"resumen": [{"titulo": "Unidad", "texto": "Un suelto."}, {"titulo": "Decena", "texto": "Un grupo de 10."}, {"titulo": "Agrupar", "texto": "De a 10."}],
"glosario": [{"palabra": "Decena", "significado": "Un grupo de 10."}, {"palabra": "Unidad", "significado": "Uno solo."}],
"carpeta": ["¿Cuántas bolsitas de 10 hay?", "¿Cuántos caramelos sueltos hay?", "¿Cuántos caramelos hay en total?"],
"respuestas_carpeta": [["2"], ["5"], ["25"]],
"soluciones": {"incompleto": "2. 0.", "solo": "1 grupo de 10 y sobran 2.", "carpeta": ["2.", "5.", "25."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar decenas y unidades sueltas.",
"vas_a_ver": ["Contar las bolsitas de 10 en 10", "Contar los sueltos", "Decenas y unidades forman el número"],
"secciones": [
 S(1, "Bolsitas y sueltos", [
  P("Primero contamos las bolsitas: <b>10, 20, 30</b>."),
  P("Después los sueltos: <b>31, 32, 33, 34, 35</b>."),
  IMG("35 caramelos", "3 decenas y 5 unidades.", FG.bolsitas(3, 5)),
 ]),
 S(1, "Decenas y unidades", [
  D("Decenas y unidades", "52 tiene <b>5 decenas</b> y <b>2 unidades</b>."),
  IMG("52 caramelos", "5 bolsitas y 2 sueltos.", FG.bolsitas(5, 2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("Un pedido", "Contá bolsitas y sueltos.", FG.bolsitas(4, 7)),
 ]),
],
"ejemplo_completo": {"titulo": "6 bolsitas y 1 suelto", "planteo": "¿Cuántos caramelos son?", "pasos": ["Bolsitas: 10, 20, 30, 40, 50, 60.", "Suelto: 61.", "Son 61 caramelos."]},
"ejemplo_incompleto": {"titulo": "2 bolsitas y 8 sueltos", "planteo": "Completá.", "pasos": ["Bolsitas: 10, ___ .", "Sueltos: 21, 22… ___ .", "Son ___ caramelos."]},
"ejemplo_solo": {"titulo": "El 90", "planteo": "¿Cuántas decenas tiene el 90?"},
"tip": {"titulo": "Bolsitas primero", "texto": "Contá de 10 en 10 y después de a 1."},
"ojo": ["Una bolsita vale 10, no 1.", "Los sueltos se cuentan de a 1."],
"resumen": [{"titulo": "Decenas", "texto": "Bolsitas de 10."}, {"titulo": "Unidades", "texto": "Sueltos."}, {"titulo": "Juntas", "texto": "Forman el número."}],
"glosario": [{"palabra": "Decenas", "significado": "Grupos de 10."}, {"palabra": "Unidades", "significado": "Los sueltos."}],
"carpeta": ["¿Cuántas decenas tiene el pedido?", "¿Cuántas unidades sueltas tiene?", "¿Qué número forma?"],
"respuestas_carpeta": [["4"], ["7"], ["47"]],
"soluciones": {"incompleto": "20. 28. 28.", "solo": "9 decenas.", "carpeta": ["4.", "7.", "47."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir números con decenas y unidades.",
"vas_a_ver": ["Decenas a la izquierda", "Unidades a la derecha", "Leer el número"],
"secciones": [
 S(1, "Cada cifra en su lugar", [
  P("6 bolsitas y 3 sueltos se escribe <b>63</b>."),
  D("El lugar", "Las <b>decenas</b> van a la izquierda. Las <b>unidades</b>, a la derecha."),
  IMG("Tablero", "Decenas y unidades.", FG.tablero_du([63, 48, 25])),
 ]),
 S(1, "Leer el número", [
  P("63 se lee <b>sesenta y tres</b>."),
  IMG("Tarjetas", "Cada número con su nombre.", FG.tarjetas([(63, "sesenta y tres"), (48, "cuarenta y ocho")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tablero. Lo vas a usar en la carpeta."),
  IMG("Tablero para completar", "Escribí decenas y unidades.", FG.tablero_du([72, 39, 50], vacios=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Escribir 4 y 8", "planteo": "4 bolsitas y 8 sueltos.", "pasos": ["Decenas: 4.", "Unidades: 8.", "Se escribe 48."]},
"ejemplo_incompleto": {"titulo": "Escribir 9 y 1", "planteo": "Completá.", "pasos": ["Decenas: ___ .", "Unidades: ___ .", "Se escribe ___ ."]},
"ejemplo_solo": {"titulo": "Leer", "planteo": "Escribí con palabras el número 25."},
"tip": {"titulo": "Primero las bolsitas", "texto": "Las decenas se escriben primero."},
"ojo": ["Sesenta y tres es 63, no 36.", "Las decenas van a la izquierda."],
"resumen": [{"titulo": "Decenas", "texto": "A la izquierda."}, {"titulo": "Unidades", "texto": "A la derecha."}, {"titulo": "Leer", "texto": "Sesenta y tres."}],
"glosario": [{"palabra": "Izquierda", "significado": "Donde van las decenas."}, {"palabra": "Derecha", "significado": "Donde van las unidades."}],
"carpeta": ["¿Cuántas decenas tiene el 72?", "¿Cuántas unidades tiene el 39?", "¿Cuántas unidades tiene el 50?"],
"respuestas_carpeta": [["7"], ["9"], ["0"]],
"soluciones": {"incompleto": "9. 1. 91.", "solo": "Veinticinco.", "carpeta": ["7.", "9.", "0."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a armar y desarmar números con sumas.",
"vas_a_ver": ["Armar con bolsitas y sueltos", "Desarmar en una suma", "Cada decena vale 10"],
"secciones": [
 S(1, "Armar el 47", [
  P("Para 47, Sofi arma <b>4 bolsitas y 7 sueltos</b>."),
  IMG("El pedido de 47", "4 decenas y 7 unidades.", FG.bolsitas(4, 7)),
 ]),
 S(1, "Desarmar en una suma", [
  D("Desarmar", "Escribir el número como una suma: <b>47 = 40 + 7</b>."),
  IMG("Tablero", "Cada cifra con su valor.", FG.tablero_du([47, 85, 52])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("Otro pedido", "Contá bolsitas y sueltos.", FG.bolsitas(6, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "Desarmar 85", "planteo": "¿Cómo se desarma el 85?", "pasos": ["El 8 vale 80.", "El 5 vale 5.", "85 = 80 + 5."]},
"ejemplo_incompleto": {"titulo": "Desarmar 29", "planteo": "Completá.", "pasos": ["El 2 vale ___ .", "29 = 20 + ___ ."]},
"ejemplo_solo": {"titulo": "Armar", "planteo": "¿Qué número es 70 + 4?"},
"tip": {"titulo": "Cada bolsita vale 10", "texto": "4 bolsitas valen 40."},
"ojo": ["47 no es 4 + 7.", "47 es 40 + 7."],
"resumen": [{"titulo": "Armar", "texto": "40 + 7 = 47."}, {"titulo": "Desarmar", "texto": "47 = 40 + 7."}, {"titulo": "Decenas", "texto": "Valen 10 cada una."}],
"glosario": [{"palabra": "Armar", "significado": "Juntar las partes."}, {"palabra": "Desarmar", "significado": "Separar en una suma."}],
"carpeta": ["¿Qué número forma el pedido?", "¿Cuánto valen las bolsitas de ese pedido?", "¿Qué número es 30 + 6?"],
"respuestas_carpeta": [["63"], ["60"], ["36"]],
"soluciones": {"incompleto": "20. 9.", "solo": "74.", "carpeta": ["63.", "60.", "36."]},
}

ACT = {
"1": [MC("¿CUÁNTOS CARAMELOS VAN EN UNA BOLSITA?", ["5", "10", "100"], "10", "UNA DECENA SON 10."),
      N("🛍️ UNA BOLSITA DE 10 Y 🍬🍬🍬 ¿CUÁNTOS SON?", 13, "10 Y 3 SON 13.")],
"2": [N("3 BOLSITAS DE 10 Y 5 SUELTOS. ¿CUÁNTOS SON?", 35, "10, 20, 30… 35."),
      MC("¿CUÁNTAS DECENAS TIENE EL 47?", ["4", "7", "47"], "4", "4 BOLSITAS DE 10.")],
"3": [MC("6 BOLSITAS Y 3 SUELTOS, ¿QUÉ NÚMERO ES?", ["63", "36", "9"], "63", "PRIMERO LAS DECENAS."),
      MC("¿CÓMO SE LEE 48?", ["CUARENTA Y OCHO", "OCHENTA Y CUATRO", "CUATRO OCHO"], "CUARENTA Y OCHO", "4 DECENAS Y 8 UNIDADES.")],
"4": [N("¿QUÉ NÚMERO ES 30 + 6?", 36, "3 DECENAS Y 6 UNIDADES."),
      MC("¿CÓMO SE DESARMA EL 52?", ["50 + 2", "5 + 2", "20 + 5"], "50 + 2", "EL 5 VALE 50.")],
"5": [N("RELÁMPAGO. 2 BOLSITAS DE 10. ¿CUÁNTOS SON?", 20, "10, 20.", tiempo=30),
      N("RELÁMPAGO. ¿CUÁNTAS UNIDADES TIENE EL 74?", 4, "EL 4 ESTÁ EN LAS UNIDADES.", tiempo=30),
      N("RELÁMPAGO. ¿QUÉ NÚMERO ES 80 + 1?", 81, "8 DECENAS Y 1 UNIDAD.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES 9 DECENAS?", ["9", "90", "19"], "90", "9 BOLSITAS DE 10.", tiempo=30)],
}
EXAMEN = [
 [1, MC("UNA DECENA ES UN GRUPO DE…", ["5", "10", "2"], "10", "DECENA = 10.")],
 [1, N("🛍️ UNA BOLSITA DE 10 Y 🍬🍬🍬🍬🍬🍬 ¿CUÁNTOS SON?", 16, "10 Y 6 SON 16.")],
 [1, N("¿CUÁNTOS SUELTOS HAY EN 1 DECENA Y 2 UNIDADES?", 2, "LAS UNIDADES SON LOS SUELTOS.")],
 [2, N("5 BOLSITAS DE 10 Y 2 SUELTOS. ¿CUÁNTOS SON?", 52, "10, 20, 30, 40, 50… 52.")],
 [2, N("¿CUÁNTAS DECENAS TIENE EL 90?", 9, "9 BOLSITAS DE 10.")],
 [2, MC("UNA BOLSITA DE 10 VALE…", ["1", "10"], "10", "NO SE CUENTA COMO 1.")],
 [3, MC("4 DECENAS Y 8 UNIDADES, ¿QUÉ NÚMERO ES?", ["48", "84", "12"], "48", "PRIMERO LAS DECENAS.")],
 [3, MC("¿CÓMO SE ESCRIBE SESENTA Y TRES?", ["36", "63", "603"], "63", "6 DECENAS Y 3 UNIDADES.")],
 [3, N("¿CUÁNTAS DECENAS TIENE EL 72?", 7, "EL 7 ESTÁ EN LAS DECENAS.")],
 [4, N("¿QUÉ NÚMERO ES 40 + 7?", 47, "4 DECENAS Y 7 UNIDADES.")],
 [4, MC("¿CÓMO SE DESARMA EL 85?", ["80 + 5", "8 + 5", "50 + 8"], "80 + 5", "EL 8 VALE 80.")],
 [4, N("¿QUÉ NÚMERO ES 70 + 4?", 74, "7 DECENAS Y 4 UNIDADES.")],
 [4, MC("EN EL 29, ¿CUÁNTO VALE EL 2?", ["2", "20", "200"], "20", "ESTÁ EN LAS DECENAS.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: decenas y unidades", "examen_titulo": "Nivel jefe: decenas y unidades",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
