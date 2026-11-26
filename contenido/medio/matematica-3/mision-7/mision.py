# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 7 · Problemas de suma y resta. Genera mision-7.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la biblioteca del barrio de Martín.
Niveles: 1 distancia · 2 cantidad inicial desconocida · 3 varios pasos · 4 inventar problemas."""
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
ORD = lambda p, o, orden, e, **k: {"t": "ordering", "p": p, "o": o, "r": {"orden": orden}, "e": e, **k}
UNIR = lambda p, iz, de, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": iz, "derecha": de}, "r": {"pares": pares}, "e": e, **k}
CLAS = lambda p, el, cats, r, e, **k: {"t": "classify", "p": p, "o": {"elementos": el, "categorias": cats}, "r": {"categorias": r}, "e": e, **k}
FB = lambda p, huecos, e, **k: {"t": "fill_blank", "p": p, "o": {}, "r": {"huecos": huecos}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a calcular la distancia entre dos números.",
"vas_a_ver": ["Contar para adelante", "Restar", "Cuánto falta"],
"secciones": [
 S(1, "Cuánto falta", [
  P("La biblioteca tiene 3.750 libros. Quiere llegar a 6.000."),
  P("Del 3.750 al 4.000 hay 250. Del 4.000 al 6.000, 2.000. Faltan <b>2.250</b>."),
  IMG("Dos saltos", "250 y 2.000.", FG.cuentas([("3.750 → 4.000", 250), ("4.000 → 6.000", "2.000")])),
 ]),
 S(1, "Con una resta", [
  D("Distancia", "Es cuánto hay de un número a otro. Se cuenta para adelante o se <b>resta</b>."),
  P("6.000 − 3.750 = 2.250."),
  IMG("En la recta", "Del 3.750 al 6.000.", FG.recta_miles([(3750, "3.750"), (6000, "6.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las distancias. Las vas a usar en la carpeta."),
  IMG("Distancias", "¿Cuánto falta?", FG.cuentas([("4.800 → 5.000", 200), ("2.500 → 7.000", "4.500")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Distancia", "planteo": "Del 1.600 al 3.000.", "pasos": ["1.600 → 2.000: 400. 2.000 → 3.000: 1.000.", "Hay 1.400."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Del 5.300 al 8.000.", "pasos": ["5.300 → 6.000: ___ .", "6.000 → 8.000: 2.000. Total: ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto hay del 7.900 al 9.000?"},
"tip": {"titulo": "Al mil", "texto": "Primero saltá hasta el mil."},
"ojo": ["La distancia no es una suma.", "Restá el grande menos el chico."],
"resumen": [{"titulo": "Distancia", "texto": "Cuánto falta."}, {"titulo": "Contar", "texto": "Para adelante."}, {"titulo": "Restar", "texto": "Grande menos chico."}],
"glosario": [{"palabra": "Distancia", "significado": "Lo que hay entre dos números."}, {"palabra": "Faltar", "significado": "No llegar todavía."}],
"carpeta": ["¿Cuánto hay del 4.800 al 5.000?", "¿Cuánto hay del 2.500 al 7.000?", "Leo sumó 3.750 + 6.000 para saber cuánto falta. ¿Cuánto falta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["200"], ["4500", "4.500"], ["2250", "2.250"]],
"soluciones": {"incompleto": "700. 2.700.", "solo": "1.100.", "carpeta": ["200.", "4.500.", "2.250."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a averiguar cuánto había al principio.",
"vas_a_ver": ["La historia al revés", "Si llegaron, restamos", "Si se fueron, sumamos"],
"secciones": [
 S(1, "Al revés", [
  P("Martín no sabe cuántos libros tenía. Le regalaron 1.250. Ahora tiene 4.600."),
  P("4.600 − 1.250 = <b>3.350</b>."),
  IMG("Al revés", "Sacamos lo que llegó.", FG.cuentas([("? + 1.250", "4.600"), ("4.600 − 1.250", "3.350")])),
 ]),
 S(1, "Si se fueron", [
  D("Volver al principio", "Si llegaron, <b>restamos</b>. Si se fueron, <b>sumamos</b>."),
  P("Prestó 800 y le quedan 2.500: tenía 3.300."),
  IMG("Sumamos", "Devolvemos lo que se fue.", FG.cuentas([("? − 800", "2.500"), ("2.500 + 800", "3.300")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("¿Cuánto tenía?", "Pensá al revés.", FG.cuentas([("? + 2.000", "5.400"), ("? − 1.500", "3.000")], ocultar=())),
 ]),
],
"ejemplo_completo": {"titulo": "Al revés", "planteo": "Llegaron 900. Ahora hay 6.100.", "pasos": ["Llegaron: restamos.", "6.100 − 900 = 5.200."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Se fueron 1.300. Quedan 2.200.", "pasos": ["Se fueron: ___ .", "2.200 + 1.300 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "Le dieron 2.500 y ahora tiene 7.500. ¿Cuánto tenía?"},
"tip": {"titulo": "Al revés", "texto": "Hacé la cuenta contraria."},
"ojo": ["Si llegaron, no sumes: restá.", "Si se fueron, sumá."],
"resumen": [{"titulo": "Al revés", "texto": "Volvemos atrás."}, {"titulo": "Llegaron", "texto": "Restamos."}, {"titulo": "Se fueron", "texto": "Sumamos."}],
"glosario": [{"palabra": "Principio", "significado": "Lo que había antes."}, {"palabra": "Desconocido", "significado": "Lo que no sabemos."}],
"carpeta": ["Le llegaron 2.000 y ahora tiene 5.400. ¿Cuánto tenía?", "Se fueron 1.500 y quedan 3.000. ¿Cuánto tenía?", "Sofi sumó 4.600 + 1.250 para saber cuánto tenía Martín. ¿Cuánto tenía?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3400", "3.400"], ["4500", "4.500"], ["3350", "3.350"]],
"soluciones": {"incompleto": "Sumamos. 3.500.", "solo": "5.000.", "carpeta": ["3.400.", "4.500.", "3.350."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a resolver problemas de varios pasos.",
"vas_a_ver": ["Leer todo", "Una cuenta por vez", "Responder"],
"secciones": [
 S(1, "Paso a paso", [
  P("Tenía 3.400. Compra 1.200. Presta 800."),
  P("3.400 + 1.200 = 4.600. 4.600 − 800 = <b>3.800</b>."),
  IMG("Dos pasos", "Una suma y una resta.", FG.cuentas([("3.400 + 1.200", "4.600"), ("4.600 − 800", "3.800")])),
 ]),
 S(1, "Una cuenta por vez", [
  D("Varios pasos", "Hacemos <b>una cuenta por vez</b>, en orden."),
  P("Respondemos con una oración."),
  IMG("Otro problema", "Presta y le devuelven.", FG.cuentas([("5.000 − 1.500", "3.500"), ("3.500 + 700", "4.200")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el problema. Lo vas a usar en la carpeta."),
  IMG("Problema", "Tenía 6.000, presta 2.000, compra 500.", FG.cuentas([("6.000 − 2.000", "4.000"), ("4.000 + 500", "4.500")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Dos pasos", "planteo": "Tenía 2.000. Compra 1.500. Presta 300.", "pasos": ["2.000 + 1.500 = 3.500.", "3.500 − 300 = 3.200."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Tenía 4.000. Presta 1.000. Le devuelven 600.", "pasos": ["4.000 − 1.000 = ___ .", "___ + 600 = ___ ."]},
"ejemplo_solo": {"titulo": "Resolvé", "planteo": "Tenía 7.000. Presta 2.500. Compra 1.000. ¿Cuántos hay?"},
"tip": {"titulo": "Subrayá", "texto": "Marcá cada cosa que pasa."},
"ojo": ["No hagas solo la primera cuenta.", "Respondé con una oración."],
"resumen": [{"titulo": "Leer", "texto": "Todo."}, {"titulo": "Pasos", "texto": "Uno por vez."}, {"titulo": "Responder", "texto": "Con oración."}],
"glosario": [{"palabra": "Paso", "significado": "Cada cuenta del problema."}, {"palabra": "Respuesta", "significado": "Oración que contesta."}],
"carpeta": ["Tenía 6.000. Presta 2.000. ¿Cuántos quedan?", "Después compra 500. ¿Cuántos hay ahora?", "Juan hizo solo 6.000 − 2.000 y respondió 4.000. ¿Cuántos hay al final?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["4000", "4.000"], ["4500", "4.500"], ["4500", "4.500"]],
"soluciones": {"incompleto": "3.000. 3.000 + 600 = 3.600.", "solo": "5.500.", "carpeta": ["4.000.", "4.500.", "4.500."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a inventar problemas.",
"vas_a_ver": ["Datos", "Qué pasa", "La pregunta"],
"secciones": [
 S(1, "Las partes", [
  P("Un problema tiene datos, una historia y una pregunta."),
  P("Para 2.500 + 1.300: <b>tenía 2.500 y llegan 1.300. ¿Cuántos hay?</b>"),
  IMG("Las partes", "Datos, historia y pregunta.", FG.cuentas([("datos", "2.500 · 1.300"), ("pregunta", "¿cuántos?")])),
 ]),
 S(1, "Suma o resta", [
  D("Inventar", "Elegimos una historia que <b>vaya con la cuenta</b>: llegar para sumar, irse para restar."),
  P("3.000 − 500: prestó 500."),
  IMG("Palabras", "Suma y resta.", FG.cuentas([("suma", "llegan"), ("resta", "se van")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas", "Inventá un problema.", FG.cuentas([("4.200 + 800", "?"), ("5.000 − 1.200", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Inventar", "planteo": "Cuenta: 1.800 + 700.", "pasos": ["Tenía 1.800 estampas y le dan 700.", "¿Cuántas tiene? 2.500."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cuenta: 6.000 − 2.000.", "pasos": ["Tenía 6.000 y ___ 2.000.", "¿Cuántos ___ ?"]},
"ejemplo_solo": {"titulo": "Inventá", "planteo": "Inventá un problema para 3.500 + 1.500."},
"tip": {"titulo": "Pregunta", "texto": "Terminá siempre con una pregunta."},
"ojo": ["Sin pregunta no es un problema.", "La historia tiene que ir con la cuenta."],
"resumen": [{"titulo": "Datos", "texto": "Los números."}, {"titulo": "Historia", "texto": "Suma o resta."}, {"titulo": "Pregunta", "texto": "Al final."}],
"glosario": [{"palabra": "Inventar", "significado": "Crear algo nuevo."}, {"palabra": "Datos", "significado": "Números que ya sabemos."}],
"carpeta": ["Inventá un problema para 4.200 + 800. ¿Cuál es la respuesta?", "Inventá un problema para 5.000 − 1.200. ¿Cuál es la respuesta?", "Mía inventó un problema para 5.000 − 1.200 con la palabra «llegan». ¿Qué palabra va mejor?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["5000", "5.000"], ["3800", "3.800"], ["prestan", "se van", "regala", "presta", "se fueron"]],
"soluciones": {"incompleto": "presta. quedan.", "solo": "Por ejemplo: tenía 3.500 y le dan 1.500. ¿Cuántos tiene? 5.000.", "carpeta": ["5.000.", "3.800.", "Una palabra de irse: se van, presta."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("CUÁNTO FALTA", [LD("SALTOS", "DEL CHICO SALTAMOS AL <b>MIL</b>, Y DE AHÍ AL GRANDE."),
   LL("JUNTAMOS LOS SALTOS: ESO FALTA.", "TAMBIÉN SALE CON UNA <b>RESTA</b>: GRANDE MENOS CHICO.", "NO SE SUMAN LOS DOS.")],
   {"modo": "problema4", "tipo": "distancia"}, {"modo": "problema4", "tipo": "distancia"}),
], "recuerda": [
 RC("DISTANCIA", "ES LO QUE HAY ENTRE DOS NÚMEROS.", "DEL 1.600 AL 3.000 HAY 1.400"),
 RC("RESTAR", "PARA LA DISTANCIA RESTAMOS EL GRANDE MENOS EL CHICO.", "6.000 − 3.750 = 2.250"),
]}
N2["leccion"] = {"temas": [
 T("SI LLEGARON", [LD("RESTAMOS", "SI LLEGARON, PARA VOLVER AL PRINCIPIO <b>SACAMOS</b> LO QUE LLEGÓ."),
   LL("LA HISTORIA SE PIENSA AL REVÉS.", "LA CUENTA ES CONTRARIA.")],
   {"modo": "problema4", "tipo": "inicio"}, {"modo": "problema4", "tipo": "inicio"}),
 T("SI SE FUERON", [LD("SUMAMOS", "SI SE FUERON, PARA VOLVER AL PRINCIPIO <b>DEVOLVEMOS</b> LO QUE SE FUE."),
   LL("PRESTÓ 800 Y QUEDAN 2.500.", "TENÍA 2.500 + 800.")],
   {"modo": "problema4", "tipo": "inicio", "dir": "quitar"}, {"modo": "problema4", "tipo": "inicio", "dir": "mezcla"}),
], "recuerda": [
 RC("SI LLEGARON", "RESTAMOS LO QUE LLEGÓ PARA SABER CUÁNTO HABÍA.", "LLEGARON 900 Y HAY 6.100: HABÍA 5.200"),
 RC("SI SE FUERON", "SUMAMOS LO QUE SE FUE PARA SABER CUÁNTO HABÍA.", "SE FUERON 1.300 Y QUEDAN 2.200: HABÍA 3.500"),
]}
N3["leccion"] = {"temas": [
 T("DOS PASOS", [LD("UNA CUENTA POR VEZ", "SEGUIMOS EL <b>ORDEN</b> DE LO QUE PASA: PRIMERO UNA CUENTA, DESPUÉS LA OTRA."),
   LL("EL RESULTADO DE UNA SIRVE PARA LA OTRA.", "NO TE SALTES NINGUNA.", "AL FINAL, UNA <b>ORACIÓN</b>: QUEDAN 3.800 LIBROS.")],
   {"modo": "problema4", "tipo": "pasos"}, {"modo": "problema4", "tipo": "pasos"}),
], "recuerda": [
 RC("VARIOS PASOS", "HACEMOS LAS CUENTAS UNA POR VEZ, EN ORDEN.", "2.000 + 1.500 = 3.500 Y 3.500 − 300 = 3.200"),
 RC("RESPONDER", "AL TERMINAR, CONTESTAMOS LA PREGUNTA CON UNA ORACIÓN COMPLETA.", "HAY 3.200 LIBROS"),
]}
N4["leccion"] = {"temas": [
 T("INVENTAR UN PROBLEMA", [LD("PARTES", "UN PROBLEMA TIENE <b>DATOS</b>, UNA HISTORIA Y UNA PREGUNTA."),
   LL("PARA SUMAR, ALGO <b>LLEGA</b>: LE DAN, COMPRA, JUNTA.", "PARA RESTAR, ALGO <b>SE VA</b>: PRESTA, REGALA.", "LA PREGUNTA VA AL FINAL.")],
   {"modo": "problema4"}, {"modo": "problema4"}),
], "recuerda": [
 RC("PARTES", "DATOS, UNA HISTORIA Y UNA PREGUNTA.", "TENÍA 2.500 Y LLEGAN 1.300. ¿CUÁNTOS HAY?"),
 RC("ELEGIR", "LA HISTORIA TIENE QUE IR CON LA CUENTA.", "3.000 − 500: PRESTÓ 500"),
]}

ACT = {
"1": [N("¿CUÁNTO HAY DEL 1.600 AL 3.000?", 1400, "400 + 1.000.", n="aplicar"),
      N("[[problema]] LA BIBLIOTECA TIENE 5.300 LIBROS. QUIERE 8.000. ¿CUÁNTOS LE FALTAN?", 2700, "700 + 2.000.", n="analizar"),
      MC("LEO SUMÓ 3.750 + 6.000 PARA SABER CUÁNTO FALTA. ¿CUÁNTO FALTA?", ["2.250", "9.750", "3.250"], "2.250", "SE RESTA.", n="error"),
      FB("COMPLETÁ: DEL 7.900 AL 9.000 HAY ___", [["1.100", "1100"]], "100 + 1.000.", n="aplicar")],
"2": [N("LLEGARON 900 Y AHORA HAY 6.100. ¿CUÁNTOS HABÍA?", 5200, "RESTAMOS.", n="aplicar"),
      N("SE FUERON 1.300 Y QUEDAN 2.200. ¿CUÁNTOS HABÍA?", 3500, "SUMAMOS.", n="aplicar"),
      MC("SOFI SUMÓ 4.600 + 1.250. LLEGARON 1.250 Y HAY 4.600. ¿CUÁNTO HABÍA?", ["3.350", "5.850", "1.250"], "3.350", "SI LLEGARON, RESTAMOS.", n="error"),
      CLAS("PARA SABER CUÁNTO HABÍA, ¿SUMO O RESTO?", ["LLEGARON 500", "SE FUERON 500", "PRESTÓ 500", "LE DIERON 500"], ["SUMO", "RESTO"],
           {"LLEGARON 500": "RESTO", "SE FUERON 500": "SUMO", "PRESTÓ 500": "SUMO", "LE DIERON 500": "RESTO"}, "AL REVÉS DE LO QUE PASÓ.", n="analizar")],
"3": [N("TENÍA 2.000. COMPRA 1.500. PRESTA 300. ¿CUÁNTOS HAY?", 3200, "3.500 − 300.", n="aplicar"),
      N("[[problema]] TENÍA 7.000. PRESTA 2.500. COMPRA 1.000. ¿CUÁNTOS HAY?", 5500, "4.500 + 1.000.", n="analizar"),
      MC("JUAN HIZO SOLO 6.000 − 2.000. FALTABA SUMAR 500. ¿CUÁNTOS HAY?", ["4.500", "4.000", "8.500"], "4.500", "HAY QUE HACER TODOS LOS PASOS.", n="error"),
      ORD("ORDENÁ LOS PASOS PARA RESOLVER.", ["HAGO LA CUENTA", "LEO TODO", "RESPONDO"], ["LEO TODO", "HAGO LA CUENTA", "RESPONDO"], "PRIMERO LEER.", n="recordar")],
"4": [MC("¿QUÉ HISTORIA VA CON 3.000 − 500?", ["PRESTÓ 500", "LE REGALAN 500", "COMPRA 500"], "PRESTÓ 500", "EN LA RESTA ALGO SE VA.", n="aplicar"),
      MC("¿QUÉ LE FALTA A «TENÍA 2.500 Y LLEGAN 1.300»?", ["LA PREGUNTA", "LOS DATOS", "NADA"], "LA PREGUNTA", "SIN PREGUNTA NO ES PROBLEMA.", n="analizar"),
      MC("MÍA USÓ «LLEGAN» PARA 5.000 − 1.200. ¿QUÉ PALABRA VA MEJOR?", ["PRESTA", "LLEGAN", "JUNTA"], "PRESTA", "RESTA: ALGO SE VA.", n="error"),
      UNIR("UNÍ CADA HISTORIA CON SU CUENTA.", ["LE DAN 800", "REGALA 800", "JUNTA 800 MÁS"], ["4.200 − 800", "4.200 + 800 ", "4.200 + 800"], {"LE DAN 800": "4.200 + 800", "REGALA 800": "4.200 − 800", "JUNTA 800 MÁS": "4.200 + 800 "}, "LLEGAR SUMA, IRSE RESTA.", n="aplicar")],
"5": [N("RELÁMPAGO. ¿CUÁNTO HAY DEL 4.800 AL 5.000?", 200, "200.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. SE FUERON 1.000 Y QUEDAN 3.000. ¿HABÍA?", 4000, "4.000.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 5.000 − 1.000 + 500 = ___", 4500, "4.500.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. «PRESTA» VA CON…", ["RESTA", "SUMA"], "RESTA", "ALGO SE VA.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO HAY DEL 2.500 AL 7.000?", 4500, "500 + 4.000.", n="aplicar")],
 [1, N("¿CUÁNTO HAY DEL 3.200 AL 4.000?", 800, "8 SALTOS DE 100.", n="aplicar")],
 [1, TF("PARA SABER CUÁNTO FALTA, SE SUMAN LOS DOS NÚMEROS.", "FALSO", "SE RESTA O SE CUENTA PARA ADELANTE.", n="error")],
 [2, N("LE DIERON 2.500 Y AHORA TIENE 7.500. ¿CUÁNTO TENÍA?", 5000, "7.500 − 2.500.", n="aplicar")],
 [2, N("PRESTÓ 800 Y LE QUEDAN 2.500. ¿CUÁNTO TENÍA?", 3300, "2.500 + 800.", n="aplicar")],
 [2, MC("SI SE FUERON LIBROS, PARA SABER CUÁNTOS HABÍA…", ["SUMAMOS", "RESTAMOS"], "SUMAMOS", "DEVOLVEMOS LO QUE SE FUE.", n="analizar")],
 [3, N("TENÍA 4.000. PRESTA 1.000. LE DEVUELVEN 600. ¿CUÁNTOS HAY?", 3600, "3.000 + 600.", n="aplicar")],
 [3, N("[[problema]] TENÍA 5.000. PRESTA 1.500. LE DEVUELVEN 700. ¿CUÁNTOS HAY?", 4200, "3.500 + 700.", n="analizar")],
 [3, MC("¿CUÁNTAS CUENTAS HACEN FALTA SI COMPRA Y DESPUÉS PRESTA?", ["DOS", "UNA", "NINGUNA"], "DOS", "UNA POR CADA COSA QUE PASA.", n="analizar")],
 [4, MC("¿QUÉ PROBLEMA VA CON 1.800 + 700?", ["TENÍA 1.800 Y LE DAN 700", "TENÍA 1.800 Y REGALA 700", "TIENE 700"], "TENÍA 1.800 Y LE DAN 700", "SUMA: ALGO LLEGA.", n="aplicar")],
 [4, MC("UN PROBLEMA SIEMPRE LLEVA…", ["UNA PREGUNTA", "UN DIBUJO", "UNA RESTA"], "UNA PREGUNTA", "SIN PREGUNTA NO HAY PROBLEMA.", n="recordar")],
 [4, MC("NICO INVENTÓ «TENÍA 6.000 Y COMPRA 2.000» PARA 6.000 − 2.000. ¿ESTÁ BIEN?", ["NO: DEBE IRSE ALGO", "SÍ"], "NO: DEBE IRSE ALGO", "LA RESTA NECESITA QUE ALGO SE VAYA.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 7, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: problemas de suma y resta", "examen_titulo": "Nivel jefe: problemas de suma y resta",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
