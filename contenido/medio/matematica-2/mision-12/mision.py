# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 12 · Propiedades de la suma. Genera mision-12.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa.
Niveles: 1 cambiar el orden · 2 agrupar para calcular mejor · 3 usar sumas conocidas · 4 la suma y la resta se relacionan."""
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
"objetivo": "Vas a ver que en la suma el orden no importa.",
"vas_a_ver": ["Dar vuelta la suma", "Empezar por el grande", "En la resta no vale"],
"secciones": [
 S(1, "Dar vuelta la suma", [
  P("Rosa tiene 30 alfajores de dulce y 40 de chocolate."),
  D("Cambiar el orden", "En la suma, el orden no cambia el resultado: <b>30 + 40 = 40 + 30</b>."),
  IMG("Dos órdenes", "Las dos dan 70.", FG.cuentas([("30 + 40", 70), ("40 + 30", 70)])),
 ]),
 S(1, "Empezar por el grande", [
  P("2 + 98 es más fácil como <b>98 + 2</b> = 100."),
  P("Contamos desde el grande: 98, 99, 100."),
  IMG("Desde el grande", "98 + 2 = 100.", FG.recta_num(96, 100, marcas=[(98, "98"), (100, "100")], flechas=[(98, 99), (99, 100)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Sumas para dar vuelta", "Empezá por el grande.", FG.cuentas([("3 + 250", 253), ("5 + 195", 200), ("20 + 400", 420)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "4 + 120", "planteo": "Sumá empezando por el grande.", "pasos": ["Doy vuelta: 120 + 4.", "120, 121, 122, 123, 124.", "Da 124."]},
"ejemplo_incompleto": {"titulo": "Dar vuelta", "planteo": "Completá.", "pasos": ["50 + 300 = 300 + ___ .", "Las dos dan ___ ."]},
"ejemplo_solo": {"titulo": "Tu suma", "planteo": "¿Cuánto es 6 + 94?"},
"tip": {"titulo": "Grande primero", "texto": "Contar desde el grande es más rápido."},
"ojo": ["En la resta no se puede dar vuelta.", "30 + 40 y 40 + 30 dan lo mismo."],
"resumen": [{"titulo": "Orden", "texto": "No cambia la suma."}, {"titulo": "Truco", "texto": "Empezá por el grande."}, {"titulo": "Resta", "texto": "No se da vuelta."}],
"glosario": [{"palabra": "Orden", "significado": "Cuál va primero."}, {"palabra": "Propiedad", "significado": "Algo que siempre se cumple."}],
"carpeta": ["¿Cuánto es 3 + 250?", "¿Cuánto es 5 + 195?", "Tomi dice que 8 − 3 es igual a 3 − 8. ¿Tiene razón? Escribí sí o no."],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["253"], ["200"], ["no"]],
"soluciones": {"incompleto": "50. 350.", "solo": "100.", "carpeta": ["253.", "200.", "No: en la resta el orden importa."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a juntar los números que suman fácil.",
"vas_a_ver": ["Buscar parejas amigas", "Juntar primero esas", "Sumar lo que queda"],
"secciones": [
 S(1, "Parejas amigas", [
  P("Rosa suma 37 + 25 + 3."),
  D("Agrupar", "Juntamos primero los números que dan <b>redondo</b>: 37 + 3 = 40."),
  P("Después: 40 + 25 = <b>65</b>."),
  IMG("Juntar primero", "37 + 3 = 40. 40 + 25 = 65.", FG.cuentas([("37 + 3", 40), ("40 + 25", 65)])),
 ]),
 S(1, "Más parejas", [
  P("60 + 75 + 40: juntamos 60 + 40 = <b>100</b>."),
  P("100 + 75 = <b>175</b>."),
  IMG("Parejas de 100", "60 y 40 hacen 100.", FG.recta_decenas(saltos=[(0, 60), (60, 100)], marcas=[(60, "60"), (100, "100")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Buscá parejas", "Juntá primero las que dan redondo.", FG.cuentas([("8 + 45 + 2", 55), ("70 + 18 + 30", 118), ("200 + 64 + 300", 564)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "16 + 9 + 4", "planteo": "Agrupá para sumar.", "pasos": ["16 + 4 = 20.", "20 + 9 = 29.", "Da 29."]},
"ejemplo_incompleto": {"titulo": "50 + 23 + 50", "planteo": "Completá.", "pasos": ["50 + 50 = ___ .", "___ + 23 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu suma", "planteo": "¿Cuánto es 7 + 38 + 3?"},
"tip": {"titulo": "Buscá el redondo", "texto": "7 y 3, 6 y 4, 60 y 40 son amigos."},
"ojo": ["Juntar distinto no cambia el resultado.", "No te olvides del número que quedó."],
"resumen": [{"titulo": "Agrupar", "texto": "Juntar los amigos."}, {"titulo": "Redondo", "texto": "Más fácil de sumar."}, {"titulo": "Después", "texto": "Sumar lo que queda."}],
"glosario": [{"palabra": "Agrupar", "significado": "Juntar algunos números primero."}, {"palabra": "Número redondo", "significado": "Termina en 0."}],
"carpeta": ["¿Cuánto es 8 + 45 + 2?", "¿Cuánto es 70 + 18 + 30?", "Sofi hizo 37 + 25 + 3 y le dio 62. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["55"], ["118"], ["65"]],
"soluciones": {"incompleto": "100. 100 + 23 = 123.", "solo": "48.", "carpeta": ["55.", "118.", "65: se olvidó del 3."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a usar sumas que ya sabés para resolver otras.",
"vas_a_ver": ["Usar los dobles", "Uno más, uno menos", "Sumas parecidas"],
"secciones": [
 S(1, "Usar los dobles", [
  P("Rosa sabe que 25 + 25 = 50."),
  D("Sumas conocidas", "Si sé <b>25 + 25 = 50</b>, entonces <b>25 + 26 = 51</b>: uno más."),
  IMG("Del doble a otra", "Uno más, uno más en el resultado.", FG.cuentas([("25 + 25", 50), ("25 + 26", 51), ("25 + 24", 49)])),
 ]),
 S(1, "Sumas parecidas", [
  P("Si 40 + 40 = 80, entonces 40 + 50 = <b>90</b>."),
  P("Si 300 + 300 = 600, entonces 300 + 301 = <b>601</b>."),
  IMG("Parecidas", "Cambia un poco, cambia un poco.", FG.cuentas([("40 + 40", 80), ("40 + 50", 90), ("300 + 301", 601)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Usá lo que sabés", "Pensá en un doble.", FG.cuentas([("50 + 51", 101), ("100 + 99", 199), ("30 + 40", 70)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "15 + 16", "planteo": "Usá un doble.", "pasos": ["Sé que 15 + 15 = 30.", "16 es uno más que 15.", "15 + 16 = 31."]},
"ejemplo_incompleto": {"titulo": "200 + 199", "planteo": "Completá.", "pasos": ["200 + 200 = ___ .", "199 es uno menos: da ___ ."]},
"ejemplo_solo": {"titulo": "Tu suma", "planteo": "¿Cuánto es 60 + 61?"},
"tip": {"titulo": "Pensá en un doble", "texto": "Buscá la suma que ya sabés."},
"ojo": ["Si uno sube 1, el resultado sube 1.", "Si uno baja 1, el resultado baja 1."],
"resumen": [{"titulo": "Dobles", "texto": "Los ya sabés."}, {"titulo": "Uno más", "texto": "Resultado + 1."}, {"titulo": "Uno menos", "texto": "Resultado − 1."}],
"glosario": [{"palabra": "Doble", "significado": "Un número más él mismo."}, {"palabra": "Parecida", "significado": "Casi igual a otra."}],
"carpeta": ["¿Cuánto es 50 + 51?", "¿Cuánto es 100 + 99?", "Tomi sabe 30 + 30 = 60 y dice 30 + 40 = 61. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["101"], ["199"], ["70"]],
"soluciones": {"incompleto": "400. 399.", "solo": "121.", "carpeta": ["101.", "199.", "70: subió 10, no 1."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver que la suma y la resta van juntas.",
"vas_a_ver": ["Una familia de cuentas", "De la suma a la resta", "Usar una para la otra"],
"secciones": [
 S(1, "Una familia de cuentas", [
  P("Rosa tiene 25 alfajores de dulce y 15 de chocolate: 40."),
  D("Familia de cuentas", "Con <b>25, 15 y 40</b> armamos cuatro cuentas."),
  IMG("La familia", "25 + 15, 15 + 25, 40 − 15, 40 − 25.", FG.cuentas([("25 + 15", 40), ("15 + 25", 40), ("40 − 15", 25), ("40 − 25", 15)])),
 ]),
 S(1, "Usar una para la otra", [
  P("Si sé que 70 + 30 = 100, sé que <b>100 − 30 = 70</b>."),
  P("Si sé que 300 + 200 = 500, sé que <b>500 − 200 = 300</b>."),
  IMG("De la suma a la resta", "La resta deshace la suma.", FG.cuentas([("300 + 200", 500), ("500 − 200", 300)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Completá la familia", "Usá la suma.", FG.cuentas([("60 + 40", 100), ("100 − 40", 60), ("100 − 60", 40)], ocultar=(1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "La familia de 8, 5 y 13", "planteo": "Armá las cuatro cuentas.", "pasos": ["8 + 5 = 13.", "5 + 8 = 13.", "13 − 5 = 8.", "13 − 8 = 5."]},
"ejemplo_incompleto": {"titulo": "La familia de 200, 300 y 500", "planteo": "Completá.", "pasos": ["200 + 300 = ___ .", "500 − 300 = ___ .", "500 − 200 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "Si 45 + 55 = 100, ¿cuánto es 100 − 55?"},
"tip": {"titulo": "Usá la que sabés", "texto": "Una suma te da dos restas."},
"ojo": ["En la resta, el grande va primero.", "La familia usa siempre los mismos tres números."],
"resumen": [{"titulo": "Familia", "texto": "Tres números, cuatro cuentas."}, {"titulo": "Suma", "texto": "Junta."}, {"titulo": "Resta", "texto": "Deshace la suma."}],
"glosario": [{"palabra": "Familia de cuentas", "significado": "Sumas y restas con los mismos números."}, {"palabra": "Deshacer", "significado": "Volver a como estaba."}],
"carpeta": ["Si 60 + 40 = 100, ¿cuánto es 100 − 40?", "¿Cuánto es 100 − 60?", "Sofi dice que 40 − 100 = 60. ¿Cómo se escribe bien la resta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["60"], ["40"], ["100 − 40", "100 - 40", "100 menos 40"]],
"soluciones": {"incompleto": "500. 200. 300.", "solo": "45.", "carpeta": ["60.", "40.", "100 − 40 = 60: el grande va primero."]},
}

ACT = {
"1": [N("¿CUÁNTO ES 4 + 120? EMPEZÁ POR EL GRANDE.", 124, "120, 121, 122, 123, 124.", n="aplicar"),
      TF("30 + 40 DA LO MISMO QUE 40 + 30.", "VERDADERO", "EN LA SUMA EL ORDEN NO CAMBIA.", n="analizar")],
"2": [N("¿CUÁNTO ES 37 + 25 + 3?", 65, "37 + 3 = 40. 40 + 25 = 65.", n="aplicar"),
      MC("EN 60 + 75 + 40, ¿QUÉ CONVIENE JUNTAR PRIMERO?", ["60 Y 40", "60 Y 75", "75 Y 40"], "60 Y 40", "DAN 100.", n="analizar")],
"3": [N("SI 25 + 25 = 50, ¿CUÁNTO ES 25 + 26?", 51, "UNO MÁS.", n="aplicar"),
      UNI("UNÍ CADA SUMA CON SU RESULTADO.", [("40 + 40", "80"), ("40 + 41", "81"), ("40 + 39", "79")], "UNO MÁS, UNO MENOS.", n="analizar")],
"4": [N("SI 70 + 30 = 100, ¿CUÁNTO ES 100 − 30?", 70, "LA RESTA DESHACE LA SUMA.", n="aplicar"),
      MC("¿CUÁL ES DE LA FAMILIA DE 25, 15 Y 40?", ["40 MENOS 15", "40 MÁS 15", "25 MENOS 40"], "40 MENOS 15", "TRES NÚMEROS, CUATRO CUENTAS.", n="analizar")],
"5": [N("RELÁMPAGO. 2 + 98 = ___", 100, "98 + 2.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 6 + 17 + 4 = ___", 27, "6 + 4 = 10.", tiempo=40, n="aplicar"),
      N("RELÁMPAGO. 50 + 51 = ___", 101, "DOBLE + 1.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 500 − 200 = ___", 300, "300 + 200 = 500.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 7 + 300?", 307, "300 + 7.", n="aplicar")],
 [1, TF("EN LA RESTA TAMBIÉN SE PUEDE DAR VUELTA: 8 − 3 = 3 − 8.", "FALSO", "SOLO EN LA SUMA.", n="error")],
 [1, MC("¿CUÁL DA LO MISMO QUE 150 + 20?", ["20 + 150", "150 − 20", "15 + 20"], "20 + 150", "EL ORDEN NO CAMBIA LA SUMA.", n="analizar")],
 [2, N("¿CUÁNTO ES 16 + 9 + 4?", 29, "16 + 4 = 20.", n="aplicar")],
 [2, N("¿CUÁNTO ES 50 + 23 + 50?", 123, "50 + 50 = 100.", n="aplicar")],
 [2, MC("EN 8 + 45 + 2, ¿QUÉ JUNTO PRIMERO?", ["8 Y 2", "8 Y 45", "45 Y 2"], "8 Y 2", "DAN 10.", n="analizar")],
 [3, N("SI 15 + 15 = 30, ¿CUÁNTO ES 15 + 16?", 31, "UNO MÁS.", n="aplicar")],
 [3, N("SI 200 + 200 = 400, ¿CUÁNTO ES 200 + 199?", 399, "UNO MENOS.", n="aplicar")],
 [3, TF("SI 30 + 30 = 60, ENTONCES 30 + 40 = 61.", "FALSO", "SUBE 10: DA 70.", n="error")],
 [4, N("SI 45 + 55 = 100, ¿CUÁNTO ES 100 − 55?", 45, "LA RESTA DESHACE LA SUMA.", n="aplicar")],
 [4, UNI("UNÍ CADA RESTA CON LA SUMA QUE LA AYUDA.", [("100 − 30", "70 + 30"), ("500 − 200", "300 + 200"), ("13 − 5", "8 + 5")], "MISMA FAMILIA.", n="analizar")],
 [4, MC("CON 8, 5 Y 13, ¿CUÁNTAS CUENTAS ARMO?", ["4", "2", "3"], "4", "DOS SUMAS Y DOS RESTAS.", n="recordar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 12, "estilo": "primeros",
     "practica": "Práctica general: propiedades de la suma", "examen_titulo": "Nivel jefe: propiedades de la suma",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-12.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
