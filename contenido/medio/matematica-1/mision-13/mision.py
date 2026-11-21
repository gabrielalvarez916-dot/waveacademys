# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 13 · Problemas de suma. Genera mision-13.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: la feria de juegos de la escuela de Sofi.
Niveles: 1 juntar y agregar · 2 avanzar y ganar · 3 completar cantidades · 4 armar problemas de suma. Resultados hasta 20."""
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
"objetivo": "Vas a resolver problemas de juntar y agregar.",
"vas_a_ver": ["Leer el problema", "Juntar o agregar", "Responder la pregunta"],
"secciones": [
 S(1, "Un problema de juntar", [
  P("Sofi gana <b>5</b> pelotas. Tomi gana <b>3</b>. ¿Cuántas ganaron entre los dos?"),
  IMG("Juntamos", "5 + 3 = 8.", FG.juntar(("pelota", 5), ("pelota", 3), "8")),
 ]),
 S(1, "Un problema de agregar", [
  D("Problema", "Una historia con una <b>pregunta</b>. La respondemos con una cuenta."),
  P("Hay <b>6</b> globos. Llegan <b>4</b> más. ¿Cuántos hay ahora?"),
  IMG("Agregamos", "6 + 4 = 10.", FG.agregar("globo", 6, 4, "6 + 4 = 10")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Estrellas", "Sofi gana 7. Tomi gana 2.", FG.juntar(("estrella", 7), ("estrella", 2), "?")),
 ]),
],
"ejemplo_completo": {"titulo": "Caramelos", "planteo": "Sofi tiene 4 caramelos. Le dan 5 más. ¿Cuántos tiene?", "pasos": ["Le dan más: es una suma.", "4 + 5 = 9.", "Tiene 9 caramelos."]},
"ejemplo_incompleto": {"titulo": "Pelotas", "planteo": "Completá.", "pasos": ["Hay 3 pelotas rojas y 6 azules.", "3 + 6 = ___ .", "Hay ___ pelotas."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Tenés 8 figuritas y te regalan 2. ¿Cuántas tenés?"},
"tip": {"titulo": "Leé dos veces", "texto": "Primero leé todo. Después buscá la pregunta."},
"ojo": ["Respondé con una oración: Hay 9 caramelos.", "Usá los dos números del problema."],
"resumen": [{"titulo": "Leer", "texto": "La historia."}, {"titulo": "Sumar", "texto": "Juntar o agregar."}, {"titulo": "Responder", "texto": "Con una oración."}],
"glosario": [{"palabra": "Problema", "significado": "Historia con pregunta."}, {"palabra": "Respuesta", "significado": "Lo que contestamos."}],
"carpeta": ["¿Cuántas estrellas ganó Sofi?", "¿Cuántas estrellas ganó Tomi?", "¿Cuántas ganaron entre los dos?"],
"respuestas_carpeta": [["7"], ["2"], ["9"]],
"soluciones": {"incompleto": "9. 9.", "solo": "10 figuritas.", "carpeta": ["7.", "2.", "9."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a resolver problemas de avanzar y ganar.",
"vas_a_ver": ["Avanzar en un juego", "Ganar puntos", "Seguir contando"],
"secciones": [
 S(1, "Avanzar casilleros", [
  P("Sofi está en el casillero <b>4</b>. Avanza <b>3</b>. ¿Dónde queda?"),
  IMG("En el camino", "4 + 3 = 7.", FG.recta_num(0, 12, [(4, ""), (7, "4 + 3 = 7")], [(4, 5), (5, 6), (6, 7)])),
 ]),
 S(1, "Ganar puntos", [
  D("Avanzar y ganar", "Cuando avanzamos o ganamos, el número <b>crece</b>: sumamos."),
  P("Tomi tiene <b>8</b> puntos. Gana <b>5</b>. 8… <b>9, 10, 11, 12, 13</b>."),
  IMG("Puntos", "8 + 5 = 13.", FG.cuentas([("8 + 5", 13)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el camino. Lo vas a usar en la carpeta."),
  IMG("Otro juego", "Contá los saltos.", FG.recta_num(0, 12, [(6, "")], [(6, 7), (7, 8), (8, 9), (9, 10)])),
 ]),
],
"ejemplo_completo": {"titulo": "La oca", "planteo": "Tomi está en el 9. Avanza 2.", "pasos": ["Avanza: sumamos.", "9… 10, 11.", "Queda en el 11."]},
"ejemplo_incompleto": {"titulo": "Puntos", "planteo": "Completá.", "pasos": ["Sofi tiene 10 puntos. Gana 4.", "10 + 4 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu juego", "planteo": "Estás en el 5 y sacás 6 en el dado. ¿Dónde quedás?"},
"tip": {"titulo": "Seguí contando", "texto": "Empezá en tu casillero y contá los saltos."},
"ojo": ["No cuentes el casillero donde estás.", "Avanzar y ganar es sumar."],
"resumen": [{"titulo": "Avanzar", "texto": "Sumamos saltos."}, {"titulo": "Ganar", "texto": "Sumamos puntos."}, {"titulo": "Contar", "texto": "Desde donde estoy."}],
"glosario": [{"palabra": "Avanzar", "significado": "Ir para adelante."}, {"palabra": "Casillero", "significado": "Cada lugar del juego."}],
"carpeta": ["¿En qué número empieza?", "¿Cuántos saltos da?", "¿En qué número queda?"],
"respuestas_carpeta": [["6"], ["4"], ["10"]],
"soluciones": {"incompleto": "14.", "solo": "Quedás en el 11.", "carpeta": ["6.", "4.", "10."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a saber cuánto falta para completar una cantidad.",
"vas_a_ver": ["Tengo y quiero", "Cuánto falta", "Completar con una suma"],
"secciones": [
 S(1, "Tengo y quiero", [
  P("Sofi tiene <b>6</b> pelotas. Quiere tener <b>9</b>. ¿Cuántas le faltan?"),
  IMG("Completamos", "Faltan 3.", FG.igualar("pelota", 6, 9, "agregar")),
 ]),
 S(1, "Completar", [
  D("Completar", "Agregar lo que falta para llegar a un número."),
  P("<b>6 + ___ = 9</b>. Contamos desde 6: <b>7, 8, 9</b>. ¡Faltan 3!"),
  IMG("Cuadro de 10", "7 y faltan 3.", FG.marco10(7, "manzana", texto="7 + 3 = 10")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro de 10", "Contá los vacíos.", FG.marco10(4, "estrella", texto="¿CUÁNTOS FALTAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "Figuritas", "planteo": "Tomi tiene 5. Quiere 8. ¿Cuántas le faltan?", "pasos": ["Contamos desde 5: 6, 7, 8.", "Contamos 3 números.", "Le faltan 3."]},
"ejemplo_incompleto": {"titulo": "Vasos", "planteo": "Completá.", "pasos": ["Hay 7 vasos. Se necesitan 10.", "7 + ___ = 10."]},
"ejemplo_solo": {"titulo": "Tus lápices", "planteo": "Tenés 2 lápices. Querés 6. ¿Cuántos te faltan?"},
"tip": {"titulo": "Contá con los dedos", "texto": "Desde lo que tenés hasta lo que querés."},
"ojo": ["La respuesta es lo que falta.", "No es el número grande."],
"resumen": [{"titulo": "Tengo", "texto": "El número chico."}, {"titulo": "Quiero", "texto": "El número grande."}, {"titulo": "Falta", "texto": "Contamos el camino."}],
"glosario": [{"palabra": "Completar", "significado": "Poner lo que falta."}, {"palabra": "Faltar", "significado": "No estar todavía."}],
"carpeta": ["¿Cuántas estrellas hay?", "¿Cuántos lugares tiene el cuadro?", "¿Cuántas estrellas faltan para 10?"],
"respuestas_carpeta": [["4"], ["10"], ["6"]],
"soluciones": {"incompleto": "3.", "solo": "4 lápices.", "carpeta": ["4.", "10.", "6."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a inventar tus propios problemas de suma.",
"vas_a_ver": ["Las partes de un problema", "Inventar una historia", "Hacer la pregunta"],
"secciones": [
 S(1, "Las partes", [
  P("Un problema tiene: <b>quién</b>, <b>qué tiene</b>, <b>qué pasa</b> y una <b>pregunta</b>."),
  IMG("Un problema", "Sofi tiene 3. Le dan 4.", FG.agregar("manzana", 3, 4, "3 + 4 = 7")),
 ]),
 S(1, "Inventar", [
  D("Inventar un problema", "Pensar una historia con números y una pregunta."),
  P("Tomi tiene <b>5</b> autitos. Le regalan <b>5</b>. ¿Cuántos tiene?"),
  IMG("La cuenta", "5 + 5 = 10.", FG.juntar(("pelota", 5), ("pelota", 5), "10")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el dibujo. Lo vas a usar en la carpeta."),
  IMG("Globos", "Inventá la historia.", FG.agregar("globo", 2, 6, "2 + 6 = ?")),
 ]),
],
"ejemplo_completo": {"titulo": "Mi problema", "planteo": "Con 4 y 2.", "pasos": ["Sofi tiene 4 globos.", "Le dan 2 más.", "¿Cuántos globos tiene? 4 + 2 = 6."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí la pregunta.", "pasos": ["Tomi tiene 3 peces. Compra 3 más.", "¿___ ?"]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Inventá un problema con la cuenta 7 + 2."},
"tip": {"titulo": "Termina con ?", "texto": "Todo problema termina con una pregunta."},
"ojo": ["Sin pregunta no es un problema.", "Los números tienen que ser cosas."],
"resumen": [{"titulo": "Quién", "texto": "Sofi, Tomi…"}, {"titulo": "Qué pasa", "texto": "Gana, le dan…"}, {"titulo": "Pregunta", "texto": "¿Cuántos tiene?"}],
"glosario": [{"palabra": "Inventar", "significado": "Crear algo nuevo."}, {"palabra": "Pregunta", "significado": "Termina con ?."}],
"carpeta": ["¿Cuántos globos había al principio?", "¿Cuántos globos llegaron?", "¿Cuánto es 2 + 6?"],
"respuestas_carpeta": [["2"], ["6"], ["8"]],
"soluciones": {"incompleto": "¿Cuántos peces tiene?", "solo": "Por ejemplo: tengo 7 lápices y me dan 2. ¿Cuántos tengo? 9.", "carpeta": ["2.", "6.", "8."]},
}

ACT = {
"1": [N("SOFI TIENE 4 FIGURITAS Y TOMI 5. ¿CUÁNTAS TIENEN ENTRE LOS DOS?", 9, "4 + 5 = 9."),
      N("HAY 7 GLOBOS. LLEGAN 3 MÁS. ¿CUÁNTOS HAY AHORA?", 10, "7 + 3 = 10.")],
"2": [N("SOFI ESTÁ EN EL CASILLERO 5. AVANZA 4. ¿DÓNDE QUEDA?", 9, "5… 6, 7, 8, 9."),
      N("TOMI TIENE 10 PUNTOS. GANA 6. ¿CUÁNTOS TIENE?", 16, "10 + 6 = 16.")],
"3": [N("SOFI TIENE 5 PELOTAS. QUIERE 8. ¿CUÁNTAS LE FALTAN?", 3, "5… 6, 7, 8: FALTAN 3."),
      N("7 + ___ = 10", 3, "7 Y 3 SON 10.")],
"4": [MC("¿QUÉ LE FALTA A ESTE PROBLEMA? SOFI TIENE 3 GLOBOS Y LE DAN 2.", ["LA PREGUNTA", "LOS NÚMEROS", "UN NOMBRE"], "LA PREGUNTA", "TODO PROBLEMA TIENE PREGUNTA."),
      MC("¿QUÉ PROBLEMA SE RESUELVE CON 6 + 2?", ["TENGO 6 Y ME DAN 2", "TENGO 6 Y PIERDO 2", "TENGO 2"], "TENGO 6 Y ME DAN 2", "ME DAN MÁS: SUMO.")],
"5": [N("RELÁMPAGO. HAY 8 PECES. COMPRAN 2. ¿CUÁNTOS HAY?", 10, "8 + 2 = 10.", tiempo=30),
      N("RELÁMPAGO. ESTÁS EN EL 9. AVANZÁS 3. ¿DÓNDE QUEDÁS?", 12, "9… 10, 11, 12.", tiempo=30),
      N("RELÁMPAGO. TENÉS 6. QUERÉS 10. ¿CUÁNTOS FALTAN?", 4, "6 + 4 = 10.", tiempo=30),
      MC("RELÁMPAGO. ¿CON QUÉ TERMINA UN PROBLEMA?", ["CON UNA PREGUNTA", "CON UN DIBUJO", "CON UN NÚMERO"], "CON UNA PREGUNTA", "SIEMPRE HAY UNA PREGUNTA.", tiempo=30)],
}
EXAMEN = [
 [1, N("SOFI GANA 3 OSITOS Y TOMI GANA 6. ¿CUÁNTOS GANARON?", 9, "3 + 6 = 9.")],
 [1, N("HAY 5 VASOS. TRAEN 5 MÁS. ¿CUÁNTOS HAY?", 10, "5 + 5 = 10.")],
 [1, MC("SI NOS DAN MÁS COSAS, HACEMOS UNA…", ["SUMA", "RESTA"], "SUMA", "AGREGAR ES SUMAR.")],
 [2, N("TOMI ESTÁ EN EL CASILLERO 7. AVANZA 5. ¿DÓNDE QUEDA?", 12, "7… 8, 9, 10, 11, 12.")],
 [2, N("SOFI TIENE 9 PUNTOS. GANA 4. ¿CUÁNTOS TIENE?", 13, "9… 10, 11, 12, 13.")],
 [2, MC("AL AVANZAR EN UN JUEGO, EL NÚMERO…", ["CRECE", "BAJA", "NO CAMBIA"], "CRECE", "AVANZAR ES SUMAR.")],
 [3, N("TOMI TIENE 4 AUTITOS. QUIERE 7. ¿CUÁNTOS LE FALTAN?", 3, "4… 5, 6, 7: FALTAN 3.")],
 [3, N("8 + ___ = 10", 2, "8 Y 2 SON 10.")],
 [3, N("HAY 3 CHICOS. SE NECESITAN 9. ¿CUÁNTOS FALTAN?", 6, "3 + 6 = 9.")],
 [4, MC("¿QUÉ ES UN PROBLEMA?", ["UNA HISTORIA CON PREGUNTA", "UNA CUENTA SOLA", "UN DIBUJO"], "UNA HISTORIA CON PREGUNTA", "SE RESPONDE CON UNA CUENTA.")],
 [4, MC("¿QUÉ PROBLEMA SE RESUELVE CON 4 + 4?", ["TENGO 4 Y ME DAN 4", "TENGO 4 Y PIERDO 4", "TENGO 8"], "TENGO 4 Y ME DAN 4", "ME DAN MÁS: SUMO.")],
 [4, N("SOFI TIENE 6 FLORES Y JUNTA 3 MÁS. ¿CUÁNTAS TIENE?", 9, "6 + 3 = 9.")],
 [4, N("TOMI TIENE 11 FIGURITAS Y LE DAN 2. ¿CUÁNTAS TIENE?", 13, "11… 12, 13.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 13, "estilo": "primeros",
     "practica": "Práctica general: problemas de suma", "examen_titulo": "Nivel jefe: problemas de suma",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-13.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
