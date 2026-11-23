# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 9 · Sumas con algoritmo. Genera mision-9.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (cajas de 100, paquetes de 10 y sueltos).
Niveles: 1 sumar en columnas · 2 sumas sin reagrupar · 3 sumas con reagrupamiento · 4 controlar el resultado."""
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
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a armar una suma en columnas.",
"vas_a_ver": ["Cada cifra en su columna", "Empezar por las unidades", "Escribir el resultado"],
"secciones": [
 S(1, "Cada cifra en su columna", [
  P("Rosa suma 234 + 52 en columnas."),
  D("Sumar en columnas", "Unidades debajo de unidades. Decenas debajo de decenas."),
  P("El 52 no tiene centenas: va corrido a la derecha."),
  IMG("La cuenta armada", "Cada cifra en su columna.", FG.columnas(234, 52, "+")),
 ]),
 S(1, "Empezar por las unidades", [
  P("Primero las unidades: 4 + 2 = <b>6</b>."),
  P("Después las decenas: 3 + 5 = <b>8</b>. Las centenas: <b>2</b>."),
  IMG("El resultado", "234 + 52 = 286.", FG.columnas(234, 52, "+", 286)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la cuenta. La vas a usar en la carpeta."),
  IMG("Cuenta para resolver", "Empezá por las unidades.", FG.columnas(413, 75, "+", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "321 + 46", "planteo": "Sumá en columnas.", "pasos": ["Unidades: 1 + 6 = 7.", "Decenas: 2 + 4 = 6.", "Centenas: 3.", "Resultado: 367."]},
"ejemplo_incompleto": {"titulo": "142 + 35", "planteo": "Completá.", "pasos": ["Unidades: 2 + 5 = ___ .", "Decenas: 4 + 3 = ___ .", "Resultado: ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "Armá y resolvé 503 + 64."},
"tip": {"titulo": "De derecha a izquierda", "texto": "Siempre empezá por las unidades."},
"ojo": ["El 52 va debajo del 34, no del 23.", "No empieces por la izquierda."],
"resumen": [{"titulo": "Columnas", "texto": "U con U, D con D, C con C."}, {"titulo": "Empezar", "texto": "Por las unidades."}, {"titulo": "Resultado", "texto": "Abajo de la raya."}],
"glosario": [{"palabra": "Columna", "significado": "Una fila de arriba hacia abajo."}, {"palabra": "Algoritmo", "significado": "Los pasos para hacer una cuenta."}],
"carpeta": ["En la cuenta, ¿cuánto dan las unidades: 3 + 5?", "¿Cuánto dan las decenas: 1 + 7?", "Tomi puso el 75 debajo del 41. ¿Cuánto es 413 + 75?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["8"], ["8"], ["488"]],
"soluciones": {"incompleto": "7. 7. 177.", "solo": "567.", "carpeta": ["8.", "8.", "488: el 75 va debajo del 13."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a resolver sumas en columnas con números de tres cifras.",
"vas_a_ver": ["Sumar columna por columna", "Cuando hay un cero", "Sumas de tres cifras"],
"secciones": [
 S(1, "Columna por columna", [
  P("Rosa junta dos pedidos: 342 + 125."),
  P("Unidades: 2 + 5 = 7. Decenas: 4 + 2 = 6. Centenas: 3 + 1 = 4."),
  IMG("342 + 125", "Resultado: 467.", FG.columnas(342, 125, "+", 467)),
 ]),
 S(1, "Cuando hay un cero", [
  D("El cero", "Sumar <b>0</b> no cambia nada: 0 + 8 = 8."),
  P("503 + 284: las decenas son 0 + 8 = <b>8</b>."),
  IMG("503 + 284", "Resultado: 787.", FG.columnas(503, 284, "+", 787)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la cuenta. La vas a usar en la carpeta."),
  IMG("Cuenta para resolver", "Columna por columna.", FG.columnas(621, 253, "+", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "430 + 216", "planteo": "Sumá en columnas.", "pasos": ["Unidades: 0 + 6 = 6.", "Decenas: 3 + 1 = 4.", "Centenas: 4 + 2 = 6.", "Resultado: 646."]},
"ejemplo_incompleto": {"titulo": "512 + 375", "planteo": "Completá.", "pasos": ["Unidades: 2 + 5 = ___ .", "Decenas: 1 + 7 = ___ .", "Centenas: 5 + 3 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "Resolvé 264 + 315."},
"tip": {"titulo": "Una columna por vez", "texto": "Terminá una columna antes de pasar a la otra."},
"ojo": ["Más cero no cambia el número.", "Escribí cada resultado debajo de su columna."],
"resumen": [{"titulo": "Unidades", "texto": "Primero."}, {"titulo": "Decenas", "texto": "Después."}, {"titulo": "Centenas", "texto": "Al final."}],
"glosario": [{"palabra": "Sumando", "significado": "Cada número que se suma."}, {"palabra": "Suma", "significado": "El resultado."}],
"carpeta": ["¿Cuánto dan las unidades: 1 + 3?", "¿Cuánto es 621 + 253?", "Sofi hizo 503 + 284 y le dio 7087. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["4"], ["874"], ["787"]],
"soluciones": {"incompleto": "7. 8. 8.", "solo": "579.", "carpeta": ["4.", "874.", "787: cada resultado va en su columna."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a sumar cuando una columna pasa de 10.",
"vas_a_ver": ["10 sueltos hacen 1 paquete", "Me llevo 1", "Sumar el 1 en la otra columna"],
"secciones": [
 S(1, "10 sueltos, 1 paquete", [
  P("Rosa suma 147 + 235. Unidades: 7 + 5 = <b>12</b>."),
  P("12 sueltos son 1 paquete y 2 sueltos."),
  D("Me llevo 1", "Escribo el <b>2</b> y paso el paquete de 10 a las decenas: <b>me llevo 1</b>."),
  IMG("12 sueltos", "1 paquete y 2 sueltos.", FG.bloques(0, 1, 2)),
 ]),
 S(1, "Sumar el 1", [
  P("Decenas: 4 + 3 + <b>1</b> = 8. Centenas: 1 + 2 = 3."),
  P("147 + 235 = <b>382</b>."),
  IMG("147 + 235", "El 1 que me llevé va arriba de las decenas.", FG.columnas(147, 235, "+", 382, marcas=[("D", "1")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la cuenta. La vas a usar en la carpeta."),
  IMG("Cuenta para resolver", "¿Te llevás 1?", FG.columnas(268, 125, "+", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "356 + 128", "planteo": "Sumá en columnas.", "pasos": ["Unidades: 6 + 8 = 14. Escribo 4, me llevo 1.", "Decenas: 5 + 2 + 1 = 8.", "Centenas: 3 + 1 = 4.", "Resultado: 484."]},
"ejemplo_incompleto": {"titulo": "239 + 145", "planteo": "Completá.", "pasos": ["Unidades: 9 + 5 = 14. Escribo ___ , me llevo 1.", "Decenas: 3 + 4 + 1 = ___ .", "Resultado: ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "Resolvé 427 + 316."},
"tip": {"titulo": "No te olvides del 1", "texto": "Anotalo arriba de la columna que sigue."},
"ojo": ["7 + 5 = 12: no escribas 12 abajo.", "Sumá el 1 que te llevaste."],
"resumen": [{"titulo": "Pasa de 10", "texto": "Me llevo 1."}, {"titulo": "Escribo", "texto": "Solo las unidades."}, {"titulo": "El 1", "texto": "Se suma en la otra columna."}],
"glosario": [{"palabra": "Reagrupar", "significado": "Juntar 10 sueltos en 1 paquete."}, {"palabra": "Me llevo", "significado": "Paso 1 a la columna que sigue."}],
"carpeta": ["En 268 + 125, ¿cuánto dan las unidades: 8 + 5?", "¿Cuánto es 268 + 125?", "Tomi hizo 147 + 235 y le dio 3712. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["13"], ["393"], ["382"]],
"soluciones": {"incompleto": "4. 8. 384.", "solo": "743.", "carpeta": ["13: escribo 3 y me llevo 1.", "393.", "382: escribió el 12 entero."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a controlar si el resultado de una suma tiene sentido.",
"vas_a_ver": ["Calcular más o menos", "Comparar con el resultado", "Encontrar errores"],
"secciones": [
 S(1, "Más o menos", [
  P("Rosa suma 298 + 405. ¿Cuánto da más o menos?"),
  D("Estimar", "Es calcular <b>más o menos</b> con números redondos: 300 + 400 = 700."),
  IMG("Números redondos", "298 es casi 300. 405 es casi 400.", FG.recta_cien([(298, "298"), (405, "405")])),
 ]),
 S(1, "Comparar", [
  P("La cuenta da <b>703</b>. Está cerca de 700: ¡tiene sentido!"),
  P("Si diera 1003, estaría muy lejos: hay un error."),
  IMG("298 + 405", "703 está cerca de 700.", FG.columnas(298, 405, "+", 703, marcas=[("D", "1"), ("C", "1")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("¿Tienen sentido?", "Estimá cada una.", FG.cuentas([("199 + 302", 501), ("410 + 290", 1100), ("505 + 195", 700)])),
 ]),
],
"ejemplo_completo": {"titulo": "Controlar 196 + 503", "planteo": "La cuenta dio 699. ¿Tiene sentido?", "pasos": ["196 es casi 200. 503 es casi 500.", "200 + 500 = 700.", "699 está cerca: tiene sentido."]},
"ejemplo_incompleto": {"titulo": "Estimar 402 + 297", "planteo": "Completá.", "pasos": ["402 es casi ___ .", "297 es casi ___ .", "Da más o menos ___ ."]},
"ejemplo_solo": {"titulo": "¿Tiene sentido?", "planteo": "Alguien dice que 301 + 299 = 900. ¿Tiene sentido?"},
"tip": {"titulo": "Redondeá", "texto": "Usá el número redondo más cercano."},
"ojo": ["Estimar no es el resultado exacto.", "Si el resultado está lejos, revisá la cuenta."],
"resumen": [{"titulo": "Estimar", "texto": "Calcular más o menos."}, {"titulo": "Comparar", "texto": "¿Está cerca?"}, {"titulo": "Revisar", "texto": "Si está lejos, hay error."}],
"glosario": [{"palabra": "Estimar", "significado": "Calcular más o menos."}, {"palabra": "Controlar", "significado": "Revisar si está bien."}],
"carpeta": ["199 + 302: ¿cuánto da más o menos?", "¿Cuál de las tres cuentas está mal?", "¿Cuánto da de verdad 410 + 290?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["500"], ["410 + 290", "la del medio", "la segunda"], ["700"]],
"soluciones": {"incompleto": "400. 300. 700.", "solo": "No: 300 + 300 = 600.", "carpeta": ["500.", "410 + 290: da 700, no 1100.", "700."]},
}

ACT = {
"1": [N("SUMÁ EN COLUMNAS: 231 + 45", 276, "U: 1 + 5 = 6. D: 3 + 4 = 7. C: 2.", n="aplicar"),
      MC("EN 234 + 52, ¿DEBAJO DE QUÉ VA EL 5?", ["DEL 3", "DEL 2", "DEL 4"], "DEL 3", "DECENAS DEBAJO DE DECENAS.", n="analizar")],
"2": [N("¿CUÁNTO ES 342 + 125?", 467, "COLUMNA POR COLUMNA.", n="aplicar"),
      N("¿CUÁNTO ES 503 + 284?", 787, "0 + 8 = 8.", n="aplicar")],
"3": [N("¿CUÁNTO ES 147 + 235?", 382, "7 + 5 = 12: ME LLEVO 1.", n="aplicar"),
      MC("EN 356 + 128, 6 + 8 = 14. ¿QUÉ ESCRIBO ABAJO?", ["4", "14", "1"], "4", "ESCRIBO 4 Y ME LLEVO 1.", n="analizar")],
"4": [MC("298 + 405 DA MÁS O MENOS…", ["700", "600", "900"], "700", "300 + 400 = 700.", n="aplicar"),
      MC("ALGUIEN DICE: 410 + 290 = 1100. ¿TIENE SENTIDO?", ["NO", "SÍ"], "NO", "400 + 300 = 700: ESTÁ MUY LEJOS.", n="error")],
"5": [N("RELÁMPAGO. 123 + 45 = ___", 168, "SIN LLEVARSE.", tiempo=40, n="aplicar"),
      N("RELÁMPAGO. 210 + 360 = ___", 570, "COLUMNA POR COLUMNA.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. 8 + 6 = 14. ¿ME LLEVO 1?", ["SÍ", "NO"], "SÍ", "PASA DE 10.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. 199 + 201 DA MÁS O MENOS…", ["400", "300"], "400", "200 + 200.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, N("SUMÁ EN COLUMNAS: 312 + 64", 376, "U: 2 + 4. D: 1 + 6. C: 3.", n="aplicar")],
 [1, MC("¿POR QUÉ COLUMNA SE EMPIEZA?", ["UNIDADES", "CENTENAS", "DECENAS"], "UNIDADES", "DE DERECHA A IZQUIERDA.", n="recordar")],
 [1, MC("TOMI PUSO EL 52 DEBAJO DEL 23 EN 234 + 52. ¿QUÉ PASÓ?", ["NO LO ALINEÓ", "ESTÁ BIEN", "LE FALTA UN 0"], "NO LO ALINEÓ", "EL 52 VA DEBAJO DEL 34.", n="error")],
 [2, N("¿CUÁNTO ES 421 + 356?", 777, "1 + 6, 2 + 5, 4 + 3.", n="aplicar")],
 [2, N("¿CUÁNTO ES 608 + 130?", 738, "8 + 0, 0 + 3, 6 + 1.", n="aplicar")],
 [2, N("¿CUÁNTO ES 250 + 340?", 590, "0 + 0, 5 + 4, 2 + 3.", n="aplicar")],
 [3, N("¿CUÁNTO ES 238 + 145?", 383, "8 + 5 = 13: ME LLEVO 1.", n="aplicar")],
 [3, N("¿CUÁNTO ES 459 + 236?", 695, "9 + 6 = 15: ME LLEVO 1.", n="aplicar")],
 [3, MC("SOFI HIZO 147 + 235 = 372. ¿QUÉ SE OLVIDÓ?", ["SUMAR EL 1 QUE SE LLEVÓ", "SUMAR LAS UNIDADES", "NADA"], "SUMAR EL 1 QUE SE LLEVÓ", "4 + 3 + 1 = 8: DA 382.", n="error")],
 [4, MC("302 + 497 DA MÁS O MENOS…", ["800", "700", "900"], "800", "300 + 500 = 800.", n="aplicar")],
 [4, MC("ALGUIEN DICE: 199 + 199 = 598. ¿TIENE SENTIDO?", ["NO", "SÍ"], "NO", "200 + 200 = 400.", n="analizar")],
 [4, N("¿CUÁNTO ES 298 + 405?", 703, "CERCA DE 700.", n="aplicar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: sumas con algoritmo", "examen_titulo": "Nivel jefe: sumas con algoritmo",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
