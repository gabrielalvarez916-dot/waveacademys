# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 16 · Tablas del 2, 5 y 10. Genera mision-16.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (cajitas de 2, bandejas de 5 y paquetes de 10).
Niveles: 1 la tabla del 2 · 2 la tabla del 5 · 3 la tabla del 10 · 4 usar las tablas para calcular."""
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
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
tabla = lambda n, hasta=10: [(f"{k} × {n}", k * n) for k in range(1, hasta + 1)]

N1 = {**ESTILO,
"objetivo": "Vas a aprender la tabla del 2.",
"vas_a_ver": ["Cajitas de 2", "Contar de 2 en 2", "La tabla del 2"],
"secciones": [
 S(1, "Cajitas de 2", [
  P("Rosa vende alfajores en cajitas de 2."),
  P("3 cajitas: 2, 4, 6. Son <b>3 × 2 = 6</b>."),
  IMG("Tres cajitas de 2", "3 × 2 = 6.", FG.grupos("caramelo", 3, 2, "3 × 2 = 6")),
 ]),
 S(1, "La tabla del 2", [
  D("Tabla del 2", "Son los resultados de contar de 2 en 2: <b>2, 4, 6, 8, 10…</b>"),
  P("Todos los resultados son <b>pares</b>."),
  IMG("La tabla del 2", "Del 1 × 2 al 5 × 2.", FG.cuentas(tabla(2, 5)[:3])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Tabla del 2 para completar", "Contá de 2 en 2.", FG.cuentas([("4 × 2", 8), ("6 × 2", 12), ("10 × 2", 20)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "5 × 2", "planteo": "¿Cuánto es 5 × 2?", "pasos": ["Cuento de 2 en 2, 5 veces.", "2, 4, 6, 8, 10.", "5 × 2 = 10."]},
"ejemplo_incompleto": {"titulo": "La tabla", "planteo": "Completá.", "pasos": ["6 × 2 = ___ .", "7 × 2 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "¿Cuánto es 8 × 2?"},
"tip": {"titulo": "Es el doble", "texto": "Multiplicar por 2 es hacer el doble."},
"ojo": ["4 × 2 no es 6.", "Los resultados de la tabla del 2 son pares."],
"resumen": [{"titulo": "Tabla del 2", "texto": "De 2 en 2."}, {"titulo": "Doble", "texto": "× 2 es el doble."}, {"titulo": "Pares", "texto": "2, 4, 6, 8…"}],
"glosario": [{"palabra": "Tabla", "significado": "Los resultados de multiplicar un número."}, {"palabra": "Doble", "significado": "Dos veces lo mismo."}],
"carpeta": ["¿Cuánto es 4 × 2?", "¿Cuánto es 6 × 2?", "Tomi dice 10 × 2 = 12. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["8"], ["12"], ["20"]],
"soluciones": {"incompleto": "12. 14.", "solo": "16.", "carpeta": ["8.", "12.", "20: Tomi sumó 10 + 2."]},
}
N1["secciones"][1]["bloques"][2] = IMG("La tabla del 2", "1 × 2, 2 × 2, 3 × 2.", FG.cuentas(tabla(2, 3)))

N2 = {**ESTILO,
"objetivo": "Vas a aprender la tabla del 5.",
"vas_a_ver": ["Bandejas de 5", "Contar de 5 en 5", "La tabla del 5"],
"secciones": [
 S(1, "Bandejas de 5", [
  P("Rosa pone 5 alfajores en cada bandeja."),
  P("4 bandejas: 5, 10, 15, 20. Son <b>4 × 5 = 20</b>."),
  IMG("Cuatro bandejas de 5", "4 × 5 = 20.", FG.grupos("manzana", 4, 5, "4 × 5 = 20")),
 ]),
 S(1, "La tabla del 5", [
  D("Tabla del 5", "Contamos de 5 en 5: <b>5, 10, 15, 20, 25…</b>"),
  P("Los resultados terminan en <b>5</b> o en <b>0</b>."),
  IMG("De 5 en 5", "Como los dedos de la mano.", FG.tren_paso(5, 50, 5)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Tabla del 5 para completar", "Contá de 5 en 5.", FG.cuentas([("3 × 5", 15), ("6 × 5", 30), ("9 × 5", 45)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "7 × 5", "planteo": "¿Cuánto es 7 × 5?", "pasos": ["Cuento de 5 en 5, 7 veces.", "5, 10, 15, 20, 25, 30, 35.", "7 × 5 = 35."]},
"ejemplo_incompleto": {"titulo": "La tabla", "planteo": "Completá.", "pasos": ["4 × 5 = ___ .", "8 × 5 = ___ ."]},
"ejemplo_solo": {"titulo": "Tus manos", "planteo": "¿Cuántos dedos hay en 6 manos?"},
"tip": {"titulo": "Termina en 5 o en 0", "texto": "Si no termina así, revisá la cuenta."},
"ojo": ["6 × 5 es 30, no 11.", "La tabla del 5 salta de 5 en 5."],
"resumen": [{"titulo": "Tabla del 5", "texto": "De 5 en 5."}, {"titulo": "Termina", "texto": "En 5 o en 0."}, {"titulo": "Manos", "texto": "5 dedos cada una."}],
"glosario": [{"palabra": "Multiplicar", "significado": "Sumar varias veces lo mismo."}, {"palabra": "Resultado", "significado": "Lo que da la cuenta."}],
"carpeta": ["¿Cuánto es 3 × 5?", "¿Cuánto es 6 × 5?", "Sofi dice 9 × 5 = 44. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["15"], ["30"], ["45"]],
"soluciones": {"incompleto": "20. 40.", "solo": "30: 6 × 5.", "carpeta": ["15.", "30.", "45: tiene que terminar en 5 o en 0."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a aprender la tabla del 10.",
"vas_a_ver": ["Paquetes de 10", "Contar de 10 en 10", "El cero al final"],
"secciones": [
 S(1, "Paquetes de 10", [
  P("Cada paquete de Rosa tiene 10 alfajores."),
  P("3 paquetes: 10, 20, 30. Son <b>3 × 10 = 30</b>."),
  IMG("Tres paquetes", "3 × 10 = 30.", FG.bloques(0, 3, 0)),
 ]),
 S(1, "El cero al final", [
  D("Tabla del 10", "Multiplicar por 10 es poner un <b>0</b> al final: 4 × 10 = <b>40</b>."),
  IMG("De 10 en 10", "10, 20, 30… hasta 100.", FG.tren_paso(10, 100, 10)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Tabla del 10 para completar", "Agregá un 0.", FG.cuentas([("5 × 10", 50), ("7 × 10", 70), ("10 × 10", 100)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "6 × 10", "planteo": "¿Cuánto es 6 × 10?", "pasos": ["6 paquetes de 10.", "Agrego un 0 al 6.", "6 × 10 = 60."]},
"ejemplo_incompleto": {"titulo": "La tabla", "planteo": "Completá.", "pasos": ["8 × 10 = ___ .", "9 × 10 = ___ ."]},
"ejemplo_solo": {"titulo": "Tus paquetes", "planteo": "¿Cuántos alfajores hay en 4 paquetes de 10?"},
"tip": {"titulo": "Un 0 al final", "texto": "× 10 agrega un cero."},
"ojo": ["7 × 10 es 70, no 17.", "10 × 10 es 100."],
"resumen": [{"titulo": "Tabla del 10", "texto": "De 10 en 10."}, {"titulo": "El 0", "texto": "Va al final."}, {"titulo": "10 × 10", "texto": "Es 100."}],
"glosario": [{"palabra": "Decena", "significado": "Un grupo de 10."}, {"palabra": "Cero", "significado": "El número 0."}],
"carpeta": ["¿Cuánto es 5 × 10?", "¿Cuánto es 7 × 10?", "Tomi dice 10 × 10 = 20. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["50"], ["70"], ["100"]],
"soluciones": {"incompleto": "80. 90.", "solo": "40.", "carpeta": ["50.", "70.", "100: Tomi sumó 10 + 10."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a usar las tablas para resolver cuentas y problemas.",
"vas_a_ver": ["Elegir la tabla", "Problemas con tablas", "Comparar tablas"],
"secciones": [
 S(1, "Elegir la tabla", [
  P("Rosa arma 4 bandejas de 5. Busca en la <b>tabla del 5</b>: 4 × 5 = <b>20</b>."),
  D("Usar la tabla", "Buscamos <b>cuántos grupos</b> y <b>cuántos en cada uno</b>. Así sabemos qué tabla usar."),
  IMG("Las tres tablas", "4 × 2, 4 × 5 y 4 × 10.", FG.cuentas([("4 × 2", 8), ("4 × 5", 20), ("4 × 10", 40)])),
 ]),
 S(1, "Comparar", [
  P("4 × 10 es el <b>doble</b> de 4 × 5: 40 y 20."),
  P("Si sabés la del 5, encontrás la del 10."),
  IMG("Doble", "20 y 40.", FG.arreglo("estrella", 4, 5, "4 × 5 = 20")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bandejas. Las vas a usar en la carpeta."),
  IMG("Las bandejas de Rosa", "¿Qué tabla usás?", FG.grupos("pelota", 3, 5)),
 ]),
],
"ejemplo_completo": {"titulo": "Las medias", "planteo": "Hay 7 pares de medias. ¿Cuántas medias?", "pasos": ["Cada par tiene 2.", "Uso la tabla del 2.", "7 × 2 = 14 medias."]},
"ejemplo_incompleto": {"titulo": "Las monedas", "planteo": "Tengo 6 monedas de 10. Completá.", "pasos": ["Uso la tabla del ___ .", "6 × 10 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Hay 8 manos. ¿Cuántos dedos hay?"},
"tip": {"titulo": "¿De a cuánto?", "texto": "Eso te dice qué tabla usar."},
"ojo": ["Mirá de a cuánto vienen.", "Escribí la respuesta con palabras."],
"resumen": [{"titulo": "Elegir", "texto": "¿De a cuánto vienen?"}, {"titulo": "Buscar", "texto": "En la tabla."}, {"titulo": "Responder", "texto": "Con palabras."}],
"glosario": [{"palabra": "Par", "significado": "Dos cosas iguales juntas."}, {"palabra": "Tabla", "significado": "Los resultados de multiplicar un número."}],
"carpeta": ["¿Qué tabla usás para las bandejas del dibujo?", "¿Cuántas pelotas hay?", "Sofi dice que son 8. ¿Cuántas son?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [["5", "la del 5", "tabla del 5"], ["15"], ["15"]],
"soluciones": {"incompleto": "10. 60.", "solo": "40 dedos.", "carpeta": ["La del 5.", "15: 3 × 5.", "15: Sofi sumó 3 + 5."]},
}

ACT = {
"1": [N("¿CUÁNTO ES 6 × 2?", 12, "2, 4, 6, 8, 10, 12.", n="aplicar"),
      TF("TODOS LOS RESULTADOS DE LA TABLA DEL 2 SON PARES.", "VERDADERO", "2, 4, 6, 8, 10…", n="analizar")],
"2": [N("¿CUÁNTO ES 7 × 5?", 35, "5, 10, 15, 20, 25, 30, 35.", n="aplicar"),
      MC("¿CUÁL ES DE LA TABLA DEL 5?", ["25", "23", "12"], "25", "TERMINA EN 5 O EN 0.", n="analizar")],
"3": [N("¿CUÁNTO ES 8 × 10?", 80, "UN 0 AL FINAL.", n="aplicar"),
      UNI("UNÍ CADA CUENTA CON SU RESULTADO.", [("3 × 10", "30"), ("5 × 10", "50"), ("9 × 10", "90")], "UN 0 AL FINAL.", n="aplicar")],
"4": [N("ROSA ARMA 4 BANDEJAS DE 5. ¿CUÁNTOS ALFAJORES?", 20, "4 × 5 = 20.", n="aplicar"),
      ORD("ORDENÁ DE MENOR A MAYOR.", ["4 × 10", "4 × 2", "4 × 5"], ["4 × 2", "4 × 5", "4 × 10"], "8, 20, 40.", n="analizar")],
"5": [N("RELÁMPAGO. 5 × 2 = ___", 10, "TABLA DEL 2.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 3 × 5 = ___", 15, "TABLA DEL 5.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 6 × 10 = ___", 60, "TABLA DEL 10.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 9 × 2 = ___", 18, "TABLA DEL 2.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 4 × 2?", 8, "2, 4, 6, 8.", n="aplicar")],
 [1, N("¿CUÁNTO ES 9 × 2?", 18, "EL DOBLE DE 9.", n="aplicar")],
 [1, TF("TOMI DICE 10 × 2 = 12.", "FALSO", "10 × 2 = 20.", n="error")],
 [2, N("¿CUÁNTO ES 6 × 5?", 30, "5, 10, 15, 20, 25, 30.", n="aplicar")],
 [2, N("¿CUÁNTOS DEDOS HAY EN 8 MANOS?", 40, "8 × 5 = 40.", n="aplicar")],
 [2, MC("SOFI DICE 9 × 5 = 44. ¿POR QUÉ ESTÁ MAL?", ["NO TERMINA EN 5 NI EN 0", "ES MUY CHICO", "ESTÁ BIEN"], "NO TERMINA EN 5 NI EN 0", "9 × 5 = 45.", n="error")],
 [3, N("¿CUÁNTO ES 7 × 10?", 70, "UN 0 AL FINAL.", n="aplicar")],
 [3, N("¿CUÁNTO ES 10 × 10?", 100, "10 PAQUETES DE 10.", n="aplicar")],
 [3, TF("MULTIPLICAR POR 10 ES AGREGAR UN 0 AL FINAL.", "VERDADERO", "4 × 10 = 40.", n="recordar")],
 [4, N("HAY 7 PARES DE MEDIAS. ¿CUÁNTAS MEDIAS?", 14, "7 × 2 = 14.", n="aplicar")],
 [4, MC("6 MONEDAS DE 10. ¿QUÉ TABLA USO?", ["LA DEL 10", "LA DEL 2", "LA DEL 5"], "LA DEL 10", "VIENEN DE A 10.", n="analizar")],
 [4, UNI("UNÍ CADA PROBLEMA CON SU CUENTA.", [("3 BANDEJAS DE 5", "3 × 5"), ("4 PARES DE MEDIAS", "4 × 2"), ("2 PAQUETES DE 10", "2 × 10")], "¿DE A CUÁNTO VIENEN?", n="analizar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 16, "estilo": "primeros",
     "practica": "Práctica general: tablas del 2, 5 y 10", "examen_titulo": "Nivel jefe: tablas del 2, 5 y 10",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-16.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
