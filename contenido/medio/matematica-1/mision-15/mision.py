# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 15 · Sumar y restar con calculadora. Genera mision-15.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: la calculadora del kiosco de Sofi.
Niveles: 1 conocer la calculadora · 2 sumar y restar con teclas · 3 controlar resultados · 4 descubrir regularidades."""
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
"objetivo": "Vas a conocer las partes de la calculadora.",
"vas_a_ver": ["La pantalla", "Las teclas de números", "Las teclas de signos"],
"secciones": [
 S(1, "La calculadora del kiosco", [
  P("Sofi usa una <b>calculadora</b> para hacer cuentas rápido."),
  IMG("La calculadora", "Pantalla arriba, teclas abajo.", FG.calculadora("0")),
 ]),
 S(1, "Sus partes", [
  D("Pantalla", "Donde se ven los números y el resultado."),
  D("Teclas", "Los botones. Hay números y signos: <b>+</b>, <b>−</b> e <b>=</b>."),
  IMG("Teclas de signos", "+, − e = están marcadas.", FG.calculadora("0", ("+", "−", "="))),
 ]),
 S(2, "Para practicar", [
  P("Mirá la calculadora. La vas a usar en la carpeta."),
  IMG("Una tecla marcada", "¿Qué tecla es?", FG.calculadora("8", ("8",))),
 ]),
],
"ejemplo_completo": {"titulo": "Escribir 25", "planteo": "¿Cómo escribo 25?", "pasos": ["Aprieto el 2.", "Después aprieto el 5.", "En la pantalla dice 25."]},
"ejemplo_incompleto": {"titulo": "Escribir 31", "planteo": "Completá.", "pasos": ["Aprieto el ___ .", "Después el ___ ."]},
"ejemplo_solo": {"titulo": "Borrar", "planteo": "¿Qué tecla usás para borrar todo?"},
"tip": {"titulo": "La C borra", "texto": "Si te equivocás, apretá la C y empezá de nuevo."},
"ojo": ["Apretá las teclas de a una.", "Mirá la pantalla después de cada tecla."],
"resumen": [{"titulo": "Pantalla", "texto": "Muestra los números."}, {"titulo": "Números", "texto": "Del 0 al 9."}, {"titulo": "Signos", "texto": "+, − e =."}],
"glosario": [{"palabra": "Calculadora", "significado": "Aparato para hacer cuentas."}, {"palabra": "Tecla", "significado": "Botón que se aprieta."}],
"carpeta": ["¿Qué número dice la pantalla?", "¿Cuántas teclas de signos tiene: +, − e =?", "¿Qué tecla borra?"],
"respuestas_carpeta": [["8"], ["3"], ["C"]],
"soluciones": {"incompleto": "3. 1.", "solo": "La C.", "carpeta": ["8.", "3.", "C."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a sumar y restar con la calculadora.",
"vas_a_ver": ["El orden de las teclas", "Sumar", "Restar"],
"secciones": [
 S(1, "Sumar con teclas", [
  P("Para <b>7 + 5</b>: aprieto <b>7</b>, <b>+</b>, <b>5</b> y <b>=</b>."),
  IMG("7 + 5", "La pantalla dice 12.", FG.calculadora("12", ("7", "+", "5", "="), "7 + 5 = 12")),
 ]),
 S(1, "Restar con teclas", [
  D("El orden", "Número, signo, número y al final <b>=</b>."),
  P("Para <b>15 − 4</b>: aprieto <b>1</b>, <b>5</b>, <b>−</b>, <b>4</b> y <b>=</b>."),
  IMG("15 − 4", "La pantalla dice 11.", FG.calculadora("11", ("1", "5", "−", "4", "="), "15 − 4 = 11")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las teclas marcadas. Las vas a usar en la carpeta."),
  IMG("Una cuenta", "¿Qué cuenta es?", FG.calculadora("9 + 6", ("9", "+", "6"))),
 ]),
],
"ejemplo_completo": {"titulo": "20 + 30", "planteo": "Con la calculadora.", "pasos": ["Aprieto 2, 0.", "Aprieto +, después 3, 0.", "Aprieto = y sale 50."]},
"ejemplo_incompleto": {"titulo": "18 − 8", "planteo": "Completá.", "pasos": ["Aprieto 1, 8, ___ , 8 y = .", "Sale ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "Hacé 13 + 4 con la calculadora. ¿Qué sale?"},
"tip": {"titulo": "No te olvides del =", "texto": "Sin el = no sale el resultado."},
"ojo": ["Apretá el signo entre los números.", "Al final siempre va el =."],
"resumen": [{"titulo": "Orden", "texto": "Número, signo, número, =."}, {"titulo": "Sumar", "texto": "Con la tecla +."}, {"titulo": "Restar", "texto": "Con la tecla −."}],
"glosario": [{"palabra": "Apretar", "significado": "Tocar una tecla."}, {"palabra": "Resultado", "significado": "Lo que sale después del =."}],
"carpeta": ["¿Qué número se apretó primero?", "¿Qué signo se apretó?", "¿Cuánto es 9 + 6?"],
"respuestas_carpeta": [["9"], ["+"], ["15"]],
"soluciones": {"incompleto": "−. 10.", "solo": "17.", "carpeta": ["9.", "+.", "15."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a controlar si un resultado está bien.",
"vas_a_ver": ["Pensar antes de apretar", "Comprobar con la calculadora", "Encontrar errores"],
"secciones": [
 S(1, "Pensar primero", [
  P("Tomi hizo <b>20 + 3</b> y le salió <b>50</b>. ¿Está bien?"),
  P("Pensamos: 20 y 3 más es <b>23</b>. ¡Tomi apretó mal!"),
  IMG("Lo que apretó Tomi", "Apretó 20 + 30.", FG.calculadora("50", ("2", "0", "+", "3"), "MAL: 20 + 3 = 23")),
 ]),
 S(1, "Comprobar", [
  D("Controlar", "Pensar el resultado y mirar si la calculadora dice lo mismo."),
  IMG("Bien hecho", "20 + 3 = 23.", FG.calculadora("23", ("2", "0", "+", "3", "="), "BIEN: 20 + 3 = 23")),
 ]),
 S(2, "Para practicar", [
  P("Mirá la calculadora. La vas a usar en la carpeta."),
  IMG("¿Está bien?", "Sofi hizo 10 − 4.", FG.calculadora("14", ("1", "0", "−", "4", "="), "10 − 4 = 14 ¿BIEN?")),
 ]),
],
"ejemplo_completo": {"titulo": "8 + 2", "planteo": "La calculadora dice 10. ¿Está bien?", "pasos": ["Pienso: 8 y 2 son 10.", "Dice 10.", "¡Está bien!"]},
"ejemplo_incompleto": {"titulo": "30 − 10", "planteo": "Completá.", "pasos": ["Pienso: 3 − 1 = 2 bolsitas.", "Tiene que dar ___ ."]},
"ejemplo_solo": {"titulo": "¿Está bien?", "planteo": "La calculadora dice que 5 + 5 = 55. ¿Qué pasó?"},
"tip": {"titulo": "Pensá primero", "texto": "Si el resultado es muy raro, volvé a apretar."},
"ojo": ["La calculadora hace lo que apretás.", "Si apretás mal, sale mal."],
"resumen": [{"titulo": "Pensar", "texto": "Antes de apretar."}, {"titulo": "Mirar", "texto": "La pantalla."}, {"titulo": "Comparar", "texto": "¿Dice lo mismo?"}],
"glosario": [{"palabra": "Controlar", "significado": "Revisar si está bien."}, {"palabra": "Error", "significado": "Algo que salió mal."}],
"carpeta": ["¿Qué número dice la pantalla?", "¿Cuánto es de verdad 10 − 4?", "¿Está bien? Escribí SÍ o NO."],
"respuestas_carpeta": [["14"], ["6"], ["NO", "no"]],
"soluciones": {"incompleto": "20.", "solo": "Apretó 5 + 50 o se olvidó el +.", "carpeta": ["14.", "6.", "NO."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a descubrir qué pasa al sumar y restar 1 y 10.",
"vas_a_ver": ["Sumar 1", "Sumar 10", "Restar 10"],
"secciones": [
 S(1, "Sumar 1 muchas veces", [
  P("Sofi aprieta <b>+ 1 =</b> una y otra vez: <b>5, 6, 7, 8…</b>"),
  P("¡Va de uno en uno!"),
  IMG("Sumar 1", "Cambia el último número.", FG.tren(5, 12)),
 ]),
 S(1, "Sumar 10", [
  D("Regularidad", "Algo que se repite siempre igual."),
  P("Desde 3, sumando 10: <b>3, 13, 23, 33, 43</b>. ¡El 3 no cambia!"),
  IMG("Sumar 10", "Cambia el primer número.", FG.cuentas([("3 + 10", 13), ("13 + 10", 23), ("23 + 10", 33)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Restar 10", "Completá.", FG.cuentas([("47 − 10", 37), ("37 − 10", 27), ("27 − 10", 17)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Desde 6", "planteo": "Sumamos 10 tres veces.", "pasos": ["6 + 10 = 16.", "16 + 10 = 26.", "26 + 10 = 36."]},
"ejemplo_incompleto": {"titulo": "Desde 54", "planteo": "Completá restando 10.", "pasos": ["54, 44, ___ , ___ ."]},
"ejemplo_solo": {"titulo": "Descubrí", "planteo": "¿Qué número no cambia si sumás 10 al 8?"},
"tip": {"titulo": "Mirá los números", "texto": "Sumar 10 cambia el primero. Sumar 1 cambia el último."},
"ojo": ["Sumar 10 no es sumar 1.", "Restar 10 baja una decena."],
"resumen": [{"titulo": "+ 1", "texto": "Cambia el último."}, {"titulo": "+ 10", "texto": "Cambia el primero."}, {"titulo": "− 10", "texto": "Baja una decena."}],
"glosario": [{"palabra": "Regularidad", "significado": "Algo que se repite."}, {"palabra": "Descubrir", "significado": "Darse cuenta."}],
"carpeta": ["¿Cuánto es 47 − 10?", "¿Cuánto es 37 − 10?", "¿Cuánto es 27 − 10?"],
"respuestas_carpeta": [["37"], ["27"], ["17"]],
"soluciones": {"incompleto": "34. 24.", "solo": "El 8.", "carpeta": ["37.", "27.", "17."]},
}

ACT = {
"1": [MC("¿DÓNDE SE VE EL RESULTADO?", ["EN LA PANTALLA", "EN LAS TECLAS", "EN LA C"], "EN LA PANTALLA", "LA PANTALLA MUESTRA LOS NÚMEROS."),
      MC("¿QUÉ TECLA BORRA TODO?", ["C", "=", "+"], "C", "LA C BORRA.")],
"2": [N("APRETÁS 7, +, 5 Y =. ¿QUÉ SALE?", 12, "7 + 5 = 12."),
      N("APRETÁS 1, 5, −, 4 Y =. ¿QUÉ SALE?", 11, "15 − 4 = 11.")],
"3": [MC("TOMI HIZO 20 + 3 Y LE SALIÓ 50. ¿ESTÁ BIEN?", ["NO", "SÍ"], "NO", "20 + 3 = 23."),
      N("¿CUÁNTO TIENE QUE DAR 10 − 4?", 6, "10 − 4 = 6.")],
"4": [N("3, 13, 23, ___ ¿QUÉ SIGUE?", 33, "SUMAMOS 10."),
      N("¿CUÁNTO ES 47 − 10?", 37, "BAJA UNA DECENA.")],
"5": [N("RELÁMPAGO. APRETÁS 9, +, 9 Y =. ¿QUÉ SALE?", 18, "9 + 9 = 18.", tiempo=30),
      N("RELÁMPAGO. ¿CUÁNTO ES 25 + 10?", 35, "CAMBIA EL PRIMER NÚMERO.", tiempo=30),
      N("RELÁMPAGO. ¿CUÁNTO ES 8 + 1?", 9, "UNO MÁS.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ TECLA DA EL RESULTADO?", ["=", "+", "C"], "=", "SIN EL = NO SALE.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿CÓMO SE LLAMAN LOS BOTONES DE LA CALCULADORA?", ["TECLAS", "PANTALLAS", "NÚMEROS"], "TECLAS", "SE APRIETAN.")],
 [1, MC("¿QUÉ TECLA SIRVE PARA SUMAR?", ["+", "−", "C"], "+", "EL + ES EL SIGNO DE SUMAR.")],
 [1, MC("PARA ESCRIBIR 25 APRETAMOS…", ["2 Y 5", "5 Y 2", "25 VECES"], "2 Y 5", "PRIMERO EL 2.")],
 [2, N("APRETÁS 8, +, 6 Y =. ¿QUÉ SALE?", 14, "8 + 6 = 14.")],
 [2, N("APRETÁS 2, 0, −, 5 Y =. ¿QUÉ SALE?", 15, "20 − 5 = 15.")],
 [2, MC("¿QUÉ TECLA VA AL FINAL?", ["=", "+", "−"], "=", "EL = DA EL RESULTADO.")],
 [3, MC("LA CALCULADORA DICE 6 + 2 = 62. ¿ESTÁ BIEN?", ["NO", "SÍ"], "NO", "6 + 2 = 8.")],
 [3, N("¿CUÁNTO TIENE QUE DAR 30 + 10?", 40, "3 + 1 = 4 BOLSITAS.")],
 [3, MC("SI APRETAMOS MAL, EL RESULTADO…", ["SALE MAL", "SALE BIEN IGUAL"], "SALE MAL", "LA CALCULADORA HACE LO QUE APRETAMOS.")],
 [4, N("5, 15, 25, ___ ¿QUÉ SIGUE?", 35, "SUMAMOS 10.")],
 [4, N("¿CUÁNTO ES 62 − 10?", 52, "BAJA UNA DECENA.")],
 [4, N("¿CUÁNTO ES 39 + 1?", 40, "UNO MÁS.")],
 [4, MC("AL SUMAR 10, ¿QUÉ NÚMERO CAMBIA?", ["EL PRIMERO", "EL ÚLTIMO", "NINGUNO"], "EL PRIMERO", "CAMBIAN LAS DECENAS.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 15, "estilo": "primeros",
     "practica": "Práctica general: calculadora", "examen_titulo": "Nivel jefe: sumar y restar con calculadora",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-15.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
