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
NEU = lambda p: {"neutro": {"p": p}}

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
"carpeta": ["¿Cuántas estrellas ganó Sofi?", "¿Cuántas estrellas ganó Tomi?", "¿Cuántas estrellas ganaron entre los dos juntos?"],
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
"carpeta": ["¿En qué número empieza?", "¿Cuántos saltos da?", "¿En qué número queda después de saltar?"],
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

# ---------- LECCIÓN INTERACTIVA (escrita en sesión, docs/reglas-leccion-interactiva.md, primer ciclo: poco texto, todo visual) ----------
LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LP = lambda x: {"tipo": "parrafo", "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}
ORD = lambda p, o, orden, e, **k: {"t": "ordering", "p": p, "o": o, "r": {"orden": orden}, "e": e, **k}
UNIR = lambda p, iz, de, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": iz, "derecha": de}, "r": {"pares": pares}, "e": e, **k}
CLAS = lambda p, el, cats, r, e, **k: {"t": "classify", "p": p, "o": {"elementos": el, "categorias": cats}, "r": {"categorias": r}, "e": e, **k}
FB = lambda p, huecos, e, **k: {"t": "fill_blank", "p": p, "o": {}, "r": {"huecos": huecos}, "e": e, **k}
A, AN, RE, ER = {"n": "aplicar"}, {"n": "analizar"}, {"n": "recordar"}, {"n": "error"}
for _N in (N1, N2, N3, N4): _N["carpeta_nivel"] = ["aplicar", "aplicar", "aplicar"]

N1["leccion"] = {"temas": [
 T("LEER EL PROBLEMA", [LD("UN PROBLEMA", "UN <b>PROBLEMA</b> ES UNA HISTORIA CON NÚMEROS Y UNA PREGUNTA."),
   LL("LOS NÚMEROS SON LOS DATOS.", "LA PREGUNTA DICE QUÉ BUSCAMOS.")],
   {"modo": "problema", "tipo": "juntar"}, {"modo": "problema", "tipo": "juntar"}),
 T("JUNTAR O AGREGAR", [LD("SUMAR", "SI SE <b>JUNTAN</b> DOS GRUPOS O <b>LLEGAN</b> MÁS, HACEMOS UNA SUMA."),
   LL("HAY 7 Y LLEGAN 3: 7 + 3.", "AL FINAL RESPONDEMOS LA PREGUNTA.")],
   {"modo": "problema", "tipo": "agregar"}, {"modo": "problema", "tipo": "agregar"}),
], "recuerda": [
 RC("EL PROBLEMA", "TIENE DATOS, UNA PREGUNTA Y SE RESUELVE CON UNA CUENTA.", "SOFI TIENE 4 Y TOMI 5"),
 RC("JUNTAR O AGREGAR", "CUANDO SE JUNTAN O LLEGAN MÁS, SUMAMOS.", "4 + 5 = 9"),
]}

N2["leccion"] = {"temas": [
 T("AVANZAR EN UN JUEGO", [LD("AVANZAR", "SI <b>AVANZÁS</b> EN UN JUEGO, EL NÚMERO DEL CASILLERO CRECE."),
   LL("ESTÁS EN EL 5 Y AVANZÁS 4: 9.", "SEGUÍ CONTANDO DESDE DONDE ESTÁS.")],
   {"modo": "problema", "tipo": "avanzar"}, {"modo": "problema", "tipo": "avanzar"}),
 T("GANAR PUNTOS", [LD("GANAR", "SI <b>GANÁS</b> PUNTOS, TENÉS MÁS: ES UNA SUMA."),
   LL("TENÍA 10 Y GANO 6: 16.", "NO EMPECES DE NUEVO DESDE EL 1.")],
   {"modo": "problema", "tipo": "agregar"}, {"modo": "problema", "tipo": "avanzar"}),
], "recuerda": [
 RC("AVANZAR", "EL NÚMERO CRECE Y SEGUIMOS CONTANDO DESDE DONDE ESTAMOS.", "DEL 7 AVANZO 5: 12"),
 RC("GANAR", "SI GANAMOS, TENEMOS MÁS Y SUMAMOS.", "9 + 4 = 13"),
]}

N3["leccion"] = {"temas": [
 T("TENGO Y QUIERO", [LD("CUÁNTO FALTA", "SI TENÉS MENOS DE LO QUE QUERÉS, CONTÁ <b>CUÁNTO FALTA</b> HASTA LLEGAR."),
   LL("TENGO 5 Y QUIERO 8: 6, 7, 8.", "FALTAN 3.")],
   {"modo": "problema", "tipo": "completar"}, {"modo": "problema", "tipo": "completar"}),
 T("COMPLETAR CON UNA SUMA", [LD("LA SUMA QUE FALTA", "LO QUE FALTA SE ESCRIBE COMO UNA <b>SUMA CON UN HUECO</b>."),
   LL("5 + ___ = 8.", "EL HUECO ES 3.")],
   {"modo": "problema", "tipo": "completar"}, {"modo": "diez", "que": "cuadro"}),
], "recuerda": [
 RC("CUÁNTO FALTA", "CONTAMOS DESDE LO QUE TENEMOS HASTA LO QUE QUEREMOS.", "DE 4 A 7 FALTAN 3"),
 RC("SUMA CON HUECO", "EL HUECO ES LO QUE FALTA PARA COMPLETAR.", "7 + ___ = 10: ES 3"),
]}

N4["leccion"] = {"temas": [
 T("LAS PARTES DEL PROBLEMA", [LD("LAS PARTES", "TODO PROBLEMA TIENE UNA <b>HISTORIA</b>, LOS <b>DATOS</b> Y UNA <b>PREGUNTA</b>."),
   LL("SIN PREGUNTA NO SE PUEDE RESOLVER.", "LA CUENTA VA DESPUÉS.")],
   {"modo": "problema", "tipo": "juntar"}, {"modo": "problema", "tipo": "mezcla"}),
 T("INVENTAR UNA HISTORIA", [LD("INVENTAR", "PARA <b>INVENTAR</b> UN PROBLEMA DE SUMA, CONTÁ ALGO QUE SE JUNTA O QUE LLEGA."),
   LL("2 + 6: HABÍA 2 GLOBOS Y LLEGARON 6.", "TERMINÁ CON UNA PREGUNTA.")],
   {"modo": "problema", "tipo": "agregar"}, {"modo": "problema", "tipo": "operacion"}),
], "recuerda": [
 RC("LAS PARTES", "UNA HISTORIA, LOS DATOS Y LA PREGUNTA.", "HAY 3 GLOBOS, LLEGAN 2, ¿CUÁNTOS HAY?"),
 RC("INVENTAR", "CONTAMOS ALGO QUE SE JUNTA O LLEGA Y HACEMOS UNA PREGUNTA.", "6 + 2: TENGO 6 Y ME DAN 2"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("[[problema]] SOFI TIENE 4 FIGURITAS Y TOMI 5. ¿CUÁNTAS TIENEN ENTRE LOS DOS?", 9, "4 + 5 = 9.", **A, **NEU("SOFI TIENE 4 ESTAMPAS Y TOMI 5. ¿CUÁNTAS TIENEN ENTRE LOS DOS?")),
      N("[[problema]] HAY 7 GLOBOS. LLEGAN 3 MÁS. ¿CUÁNTOS HAY AHORA?", 10, "7 + 3 = 10.", **A),
      MC("EN EL PROBLEMA «HAY 5 PATITOS Y LLEGAN 2. ¿CUÁNTOS HAY?», ¿CUÁL ES LA PREGUNTA?", ["¿CUÁNTOS HAY?", "HAY 5 PATITOS", "LLEGAN 2"], "¿CUÁNTOS HAY?", "LA PREGUNTA DICE QUÉ BUSCAMOS.", **AN),
      MC("LEO RESPONDIÓ «8» PERO NO DIJO DE QUÉ. ¿CÓMO SE RESPONDE MEJOR?", ["HAY 8 GLOBOS", "8", "OCHO"], "HAY 8 GLOBOS", "RESPONDEMOS CON UNA ORACIÓN.", **ER)],
"2": [N("[[problema]] SOFI ESTÁ EN EL CASILLERO 5 Y AVANZA 4. ¿EN QUÉ CASILLERO QUEDA?", 9, "5… 6, 7, 8, 9.", **A),
      N("[[problema]] TOMI TIENE 10 PUNTOS Y GANA 6 MÁS. ¿CUÁNTOS PUNTOS TIENE?", 16, "10 + 6 = 16.", **A),
      MC("ANA ESTÁ EN EL 6, AVANZA 3 Y CUENTA 6, 7, 8. ¿EN QUÉ CASILLERO QUEDA DE VERDAD?", ["9", "8", "3"], "9", "EL 6 NO SE CUENTA: 7, 8, 9.", **ER),
      FB("COMPLETÁ: ESTOY EN EL 8 Y AVANZO 2. QUEDO EN EL ___", [["10"]], "8… 9, 10.", **A)],
"3": [N("[[problema]] SOFI TIENE 5 PELOTAS Y QUIERE TENER 8. ¿CUÁNTAS LE FALTAN?", 3, "5… 6, 7, 8: FALTAN 3.", **A),
      FB("COMPLETÁ: 7 + ___ = 10", [["3"]], "7 Y 3 SON 10.", **A),
      UNIR("UNÍ CADA SUMA CON EL NÚMERO QUE FALTA.", ["4 + ___ = 6", "2 + ___ = 9", "5 + ___ = 10"], ["5", "2", "7"], {"4 + ___ = 6": "2", "2 + ___ = 9": "7", "5 + ___ = 10": "5"}, "FALTAN 2, 7 Y 5.", **A),
      MC("JUAN TIENE 4 Y QUIERE 7. DICE QUE LE FALTAN 11. ¿CUÁNTOS LE FALTAN DE VERDAD?", ["3", "11", "7"], "3", "CONTAMOS DE 4 A 7: 5, 6, 7.", **ER)],
"4": [MC("¿QUÉ LE FALTA A ESTE PROBLEMA? SOFI TIENE 3 GLOBOS Y LE DAN 2.", ["LA PREGUNTA", "LOS NÚMEROS", "UN NOMBRE"], "LA PREGUNTA", "TODO PROBLEMA TIENE PREGUNTA.", **AN),
      MC("¿QUÉ PROBLEMA SE RESUELVE CON 6 + 2?", ["TENGO 6 Y ME DAN 2", "TENGO 6 Y PIERDO 2", "TENGO 2"], "TENGO 6 Y ME DAN 2", "ME DAN MÁS: SUMO.", **AN),
      ORD("ORDENÁ LAS PARTES DEL PROBLEMA.", ["¿CUÁNTOS HAY?", "HAY 3 PATITOS.", "LLEGAN 4 MÁS."], ["HAY 3 PATITOS.", "LLEGAN 4 MÁS.", "¿CUÁNTOS HAY?"], "PRIMERO LA HISTORIA, AL FINAL LA PREGUNTA.", **A),
      N("[[problema]] SOFI TIENE 6 FLORES Y JUNTA 3 MÁS. ¿CUÁNTAS FLORES TIENE?", 9, "6 + 3 = 9.", **A)],
"5": [N("RELÁMPAGO. HAY 8 PECES. COMPRAN 2. ¿CUÁNTOS HAY?", 10, "8 + 2 = 10.", tiempo=30, **A),
      N("RELÁMPAGO. ESTÁS EN EL 9. AVANZÁS 3. ¿DÓNDE QUEDÁS?", 12, "9… 10, 11, 12.", tiempo=30, **A),
      N("RELÁMPAGO. TENÉS 6. QUERÉS 10. ¿CUÁNTOS FALTAN?", 4, "6 + 4 = 10.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿CON QUÉ TERMINA UN PROBLEMA?", ["CON UNA PREGUNTA", "CON UN DIBUJO", "CON UN NÚMERO"], "CON UNA PREGUNTA", "SIEMPRE HAY UNA PREGUNTA.", tiempo=30, **RE)],
}
EXAMEN = [
 [1, N("[[problema]] SOFI GANA 3 OSITOS Y TOMI GANA 6. ¿CUÁNTOS OSITOS GANARON?", 9, "3 + 6 = 9.", **A)],
 [1, N("HAY 5 VASOS. TRAEN 5 MÁS. ¿CUÁNTOS HAY?", 10, "5 + 5 = 10.", **A)],
 [1, MC("SI NOS DAN MÁS COSAS, HACEMOS UNA…", ["SUMA", "RESTA"], "SUMA", "AGREGAR ES SUMAR.", **RE)],
 [2, N("TOMI ESTÁ EN EL CASILLERO 7. AVANZA 5. ¿DÓNDE QUEDA?", 12, "7… 8, 9, 10, 11, 12.", **A)],
 [2, N("SOFI TIENE 9 PUNTOS. GANA 4. ¿CUÁNTOS TIENE?", 13, "9… 10, 11, 12, 13.", **A)],
 [2, MC("AL AVANZAR EN UN JUEGO, EL NÚMERO…", ["CRECE", "BAJA", "NO CAMBIA"], "CRECE", "AVANZAR ES SUMAR.", **RE)],
 [3, N("[[problema]] TOMI TIENE 4 AUTITOS Y QUIERE 7. ¿CUÁNTOS AUTITOS LE FALTAN?", 3, "4… 5, 6, 7: FALTAN 3.", **AN, **NEU("TOMI TIENE 4 CARRITOS Y QUIERE 7. ¿CUÁNTOS CARRITOS LE FALTAN?"))],
 [3, FB("COMPLETÁ: 8 + ___ = 10", [["2"]], "8 Y 2 SON 10.", **A)],
 [3, N("HAY 3 CHICOS. SE NECESITAN 9. ¿CUÁNTOS FALTAN?", 6, "3 + 6 = 9.", **A)],
 [4, MC("¿QUÉ ES UN PROBLEMA?", ["UNA HISTORIA CON PREGUNTA", "UNA CUENTA SOLA", "UN DIBUJO"], "UNA HISTORIA CON PREGUNTA", "SE RESPONDE CON UNA CUENTA.", **RE)],
 [4, MC("MICA DICE QUE «TENGO 4 Y PIERDO 4» SE RESUELVE CON 4 + 4. ¿QUÉ PROBLEMA VA CON 4 + 4?", ["TENGO 4 Y ME DAN 4", "TENGO 4 Y PIERDO 4"], "TENGO 4 Y ME DAN 4", "SI ME DAN, SUMO; SI PIERDO, RESTO.", **ER)],
 [4, N("SOFI TIENE 6 FLORES Y JUNTA 3 MÁS. ¿CUÁNTAS TIENE?", 9, "6 + 3 = 9.", **A)],
 [4, N("TOMI TIENE 11 FIGURITAS Y LE DAN 2. ¿CUÁNTAS TIENE?", 13, "11… 12, 13.", **A, **NEU("TOMI TIENE 11 ESTAMPAS Y LE DAN 2. ¿CUÁNTAS TIENE?"))],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 13, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: problemas de suma", "examen_titulo": "Nivel jefe: problemas de suma",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-13.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
