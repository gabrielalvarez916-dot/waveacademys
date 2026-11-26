# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 12 · Sumar y restar decenas enteras. Genera mision-12.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el kiosco de Sofi con bolsitas de 10 caramelos (como la misión 6).
Niveles: 1 sumar decenas · 2 restar decenas · 3 contar de a diez · 4 cálculos con decenas. Todo hasta 100."""
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
"objetivo": "Vas a sumar decenas enteras: 20 + 30.",
"vas_a_ver": ["Bolsitas de 10", "Juntar bolsitas", "Sumar decenas"],
"secciones": [
 S(1, "Juntar bolsitas", [
  P("Sofi tiene <b>2</b> bolsitas de 10. Le traen <b>3</b> bolsitas más."),
  IMG("2 y 3 bolsitas", "Son 5 bolsitas: 50 caramelos.", FG.juntar(("bolsita", 2), ("bolsita", 3), "50")),
 ]),
 S(1, "Sumar decenas", [
  D("Decena entera", "Un número que termina en <b>0</b>: 10, 20, 30… Son bolsitas sin sueltos."),
  P("2 bolsitas + 3 bolsitas = 5 bolsitas. <b>20 + 30 = 50</b>."),
  IMG("En la recta", "Saltamos de 10 en 10.", FG.recta_decenas([(20, 30), (30, 40), (40, 50)], [(20, ""), (50, "20 + 30 = 50")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bolsitas. Las vas a usar en la carpeta."),
  IMG("Bolsitas", "Contá cada grupo.", FG.juntar(("bolsita", 4), ("bolsita", 2), "?")),
 ]),
],
"ejemplo_completo": {"titulo": "40 + 10", "planteo": "4 bolsitas y 1 más.", "pasos": ["4 + 1 = 5 bolsitas.", "5 bolsitas son 50.", "40 + 10 = 50."]},
"ejemplo_incompleto": {"titulo": "30 + 30", "planteo": "Completá.", "pasos": ["3 + 3 = ___ bolsitas.", "30 + 30 = ___ ."]},
"ejemplo_solo": {"titulo": "Figuritas", "planteo": "Tenés 50 figuritas y te regalan 20. ¿Cuántas tenés?"},
"tip": {"titulo": "Sumá las bolsitas", "texto": "20 + 30 es como 2 + 3, ¡pero con bolsitas!"},
"ojo": ["20 + 30 es 50, no 23.", "El 0 queda al final."],
"resumen": [{"titulo": "Bolsita", "texto": "Vale 10."}, {"titulo": "Juntar", "texto": "2 + 3 bolsitas."}, {"titulo": "Suma", "texto": "20 + 30 = 50."}],
"glosario": [{"palabra": "Decena entera", "significado": "10, 20, 30…"}, {"palabra": "Bolsita", "significado": "10 caramelos."}],
"carpeta": ["¿Cuántas bolsitas hay en total?", "¿Cuántos caramelos son?", "¿Cuánto es 40 + 20?"],
"respuestas_carpeta": [["6"], ["60"], ["60"]],
"soluciones": {"incompleto": "6. 60.", "solo": "70 figuritas.", "carpeta": ["6.", "60.", "60."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a restar decenas enteras: 70 − 20.",
"vas_a_ver": ["Vender bolsitas", "Cuántas quedan", "Restar decenas"],
"secciones": [
 S(1, "Vender bolsitas", [
  P("Sofi tiene <b>7</b> bolsitas. Vende <b>2</b>."),
  IMG("Quedan 5 bolsitas", "70 − 20 = 50.", FG.sacar("bolsita", 7, 2, "70 − 20 = 50")),
 ]),
 S(1, "Restar decenas", [
  D("Restar decenas", "Sacar bolsitas enteras. Restamos como con números chicos."),
  P("7 − 2 = 5. Entonces <b>70 − 20 = 50</b>."),
  IMG("En la recta", "Saltamos para atrás de 10 en 10.", FG.recta_decenas([(70, 60), (60, 50)], [(70, ""), (50, "70 − 20 = 50")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bolsitas. Las vas a usar en la carpeta."),
  IMG("Bolsitas", "Las tachadas se venden.", FG.sacar("bolsita", 9, 3, "¿CUÁNTAS QUEDAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "80 − 30", "planteo": "8 bolsitas, vende 3.", "pasos": ["8 − 3 = 5 bolsitas.", "5 bolsitas son 50.", "80 − 30 = 50."]},
"ejemplo_incompleto": {"titulo": "60 − 40", "planteo": "Completá.", "pasos": ["6 − 4 = ___ bolsitas.", "60 − 40 = ___ ."]},
"ejemplo_solo": {"titulo": "Hojas", "planteo": "Tenés 90 hojas y usás 50. ¿Cuántas te quedan?"},
"tip": {"titulo": "Restá las bolsitas", "texto": "70 − 20 es como 7 − 2, ¡pero con bolsitas!"},
"ojo": ["Al restar quedan menos bolsitas.", "El 0 queda al final."],
"resumen": [{"titulo": "Vender", "texto": "Sacar bolsitas."}, {"titulo": "Restar", "texto": "7 − 2 bolsitas."}, {"titulo": "Resta", "texto": "70 − 20 = 50."}],
"glosario": [{"palabra": "Vender", "significado": "Dar algo y que te paguen."}, {"palabra": "Restar", "significado": "Sacar."}],
"carpeta": ["¿Cuántas bolsitas había?", "¿Cuántas bolsitas se venden?", "¿Cuánto es 90 − 30?"],
"respuestas_carpeta": [["9"], ["3"], ["60"]],
"soluciones": {"incompleto": "2. 20.", "solo": "40 hojas.", "carpeta": ["9.", "3.", "60."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a contar de 10 en 10, para adelante y para atrás.",
"vas_a_ver": ["Contar de 10 en 10", "Empezar en cualquier decena", "Contar para atrás"],
"secciones": [
 S(1, "De 10 en 10", [
  P("<b>10, 20, 30, 40, 50, 60, 70, 80, 90, 100</b>."),
  IMG("El tren de las decenas", "Cada vagón suma 10.", FG.tren_paso(10, 100, 10)),
 ]),
 S(1, "Para atrás", [
  D("Contar de 10 en 10", "Sumar o restar <b>una bolsita</b> cada vez."),
  P("Para atrás: <b>100, 90, 80, 70…</b>"),
  IMG("En la recta", "De 100 a 70.", FG.recta_decenas([(100, 90), (90, 80), (80, 70)], [(100, ""), (70, "")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Faltan vagones", "Completá de 10 en 10.", FG.tren_paso(10, 100, 10, faltan=(30, 60, 90))),
 ]),
],
"ejemplo_completo": {"titulo": "Desde 40", "planteo": "Contá 3 veces de 10 en 10 desde 40.", "pasos": ["40…", "50, 60, 70.", "Llegamos a 70."]},
"ejemplo_incompleto": {"titulo": "Para atrás", "planteo": "Completá.", "pasos": ["90, 80, ___ , 60, ___ ."]},
"ejemplo_solo": {"titulo": "Saltos", "planteo": "Empezá en 20 y saltá de 10 en 10 hasta 80."},
"tip": {"titulo": "Mirá el primer número", "texto": "De 10 en 10 cambia el primer número: 30, 40, 50."},
"ojo": ["De 10 en 10, el 0 no cambia.", "Para atrás, los números bajan."],
"resumen": [{"titulo": "Adelante", "texto": "10, 20, 30…"}, {"titulo": "Atrás", "texto": "100, 90, 80…"}, {"titulo": "Truco", "texto": "Cambia el primer número."}],
"glosario": [{"palabra": "De 10 en 10", "significado": "Sumando 10 cada vez."}, {"palabra": "Para atrás", "significado": "Restando."}],
"carpeta": ["¿Qué número falta después del 20?", "¿Qué número falta después del 50?", "¿Qué número falta después del 80?"],
"respuestas_carpeta": [["30"], ["60"], ["90"]],
"soluciones": {"incompleto": "70. 50.", "solo": "20, 30, 40, 50, 60, 70, 80.", "carpeta": ["30.", "60.", "90."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver cálculos y problemas con decenas.",
"vas_a_ver": ["Sumar y restar decenas", "Problemas del kiosco", "Llegar a 100"],
"secciones": [
 S(1, "Cálculos rápidos", [
  P("<b>50 + 40 = 90</b>. <b>80 − 50 = 30</b>."),
  IMG("Cuentas con decenas", "Pensá en bolsitas.", FG.cuentas([("50 + 40", 90), ("80 − 50", 30), ("60 + 40", 100)])),
 ]),
 S(1, "Problemas del kiosco", [
  D("Problema", "Una pregunta que se resuelve con una cuenta."),
  P("Sofi tiene 30 caramelos. Compra 40 más. <b>30 + 40 = 70</b>."),
  IMG("El problema", "3 + 4 bolsitas.", FG.juntar(("bolsita", 3), ("bolsita", 4), "70")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Completá", "Escribí el resultado.", FG.cuentas([("20 + 50", 70), ("90 − 60", 30), ("70 + 30", 100)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Problema", "planteo": "Hay 100 caramelos. Se venden 30.", "pasos": ["Es una resta: 100 − 30.", "10 − 3 = 7 bolsitas.", "Quedan 70 caramelos."]},
"ejemplo_incompleto": {"titulo": "Cálculos", "planteo": "Completá.", "pasos": ["40 + 40 = ___ .", "50 − 20 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Inventá un problema con 60 + 30."},
"tip": {"titulo": "¿Suma o resta?", "texto": "Si llegan más, sumá. Si se van, restá."},
"ojo": ["Leé bien: ¿llegan o se van?", "10 bolsitas son 100."],
"resumen": [{"titulo": "Sumar", "texto": "50 + 40 = 90."}, {"titulo": "Restar", "texto": "80 − 50 = 30."}, {"titulo": "Problemas", "texto": "¿Llegan o se van?"}],
"glosario": [{"palabra": "Problema", "significado": "Una pregunta con una cuenta."}, {"palabra": "Cien", "significado": "10 bolsitas de 10."}],
"carpeta": ["¿Cuánto es 20 + 50?", "¿Cuánto es 90 − 60?", "¿Cuánto es 70 + 30?"],
"respuestas_carpeta": [["70"], ["30"], ["100"]],
"soluciones": {"incompleto": "80. 30.", "solo": "Por ejemplo: tengo 60 figuritas y me regalan 30. Tengo 90.", "carpeta": ["70.", "30.", "100."]},
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
 T("JUNTAR BOLSITAS", [LD("SUMAR DECENAS", "PARA SUMAR <b>20 + 30</b>, SUMAMOS LAS BOLSITAS: 2 + 3 = 5."),
   LL("5 BOLSITAS DE 10 SON 50.", "20 + 30 = 50.")],
   {"modo": "decenas_op", "que": "sumar"}, {"modo": "decenas_op", "que": "sumar"}),
 T("PENSAR EN BOLSITAS", [LD("UN TRUCO", "SI PENSÁS EN <b>BOLSITAS</b>, SUMÁS NÚMEROS CHICOS Y AL FINAL PONÉS EL 0."),
   LL("40 + 10: 4 + 1 = 5, ES 50.", "NO ES 41 NI 14.")],
   {"modo": "decenas_op", "que": "sumar"}, {"modo": "decenas_op", "que": "sumar"}),
], "recuerda": [
 RC("SUMAR DECENAS", "SUMAMOS LAS BOLSITAS DE DIEZ Y DESPUÉS VEMOS CUÁNTO VALEN.", "20 + 30 = 50"),
 RC("EL TRUCO", "SUMAMOS COMO NÚMEROS CHICOS Y AGREGAMOS EL CERO.", "4 + 1 = 5, ENTONCES 40 + 10 = 50"),
]}

N2["leccion"] = {"temas": [
 T("VENDER BOLSITAS", [LD("RESTAR DECENAS", "PARA RESTAR <b>70 − 20</b>, SACAMOS BOLSITAS: 7 − 2 = 5."),
   LL("QUEDAN 5 BOLSITAS: 50.", "70 − 20 = 50.")],
   {"modo": "decenas_op", "que": "restar"}, {"modo": "decenas_op", "que": "restar"}),
 T("CUÁNTAS QUEDAN", [LD("LO QUE QUEDA", "DESPUÉS DE VENDER, CONTAMOS LAS BOLSITAS QUE <b>QUEDAN</b>."),
   LL("TENÍA 80 Y VENDO 30: QUEDAN 50.", "SI SE VAN, ES UNA RESTA.")],
   {"modo": "decenas_op", "que": "restar"}, {"modo": "decenas_op", "que": "restar"}),
], "recuerda": [
 RC("RESTAR DECENAS", "SACAMOS BOLSITAS DE DIEZ Y CONTAMOS LAS QUE QUEDAN.", "70 − 20 = 50"),
 RC("SI SE VAN", "HACEMOS UNA RESTA PARA SABER CUÁNTO QUEDA.", "80 − 30 = 50"),
]}

N3["leccion"] = {"temas": [
 T("DE 10 EN 10", [LD("PARA ADELANTE", "CONTAR <b>DE 10 EN 10</b> ES SUMAR UNA BOLSITA CADA VEZ."),
   LL("10, 20, 30, 40.", "LA PRIMERA CIFRA SUBE 1.")],
   {"modo": "saltos", "de": 10}, {"modo": "decenas_op", "que": "contar10"}),
 T("PARA ATRÁS", [LD("PARA ATRÁS", "CONTAR <b>PARA ATRÁS</b> DE 10 EN 10 ES SACAR UNA BOLSITA CADA VEZ."),
   LL("100, 90, 80, 70.", "LA PRIMERA CIFRA BAJA 1.")],
   {"modo": "decenas_op", "que": "atras10"}, {"modo": "decenas_op", "que": "atras10"}),
], "recuerda": [
 RC("PARA ADELANTE", "SUMAMOS DIEZ CADA VEZ Y LA PRIMERA CIFRA SUBE.", "50, 60, 70"),
 RC("PARA ATRÁS", "RESTAMOS DIEZ CADA VEZ Y LA PRIMERA CIFRA BAJA.", "60, 50, 40"),
]}

N4["leccion"] = {"temas": [
 T("¿SUMA O RESTA?", [LD("ELEGIR LA CUENTA", "SI <b>LLEGAN</b> MÁS, SUMAMOS. SI SE <b>VAN</b>, RESTAMOS."),
   LL("HAY 50 Y LLEGAN 20: 50 + 20.", "HAY 90 Y SE VENDEN 60: 90 − 60.")],
   {"modo": "decenas_op", "que": "sumar"}, {"modo": "decenas_op", "que": "restar"}),
 T("LLEGAR A 100", [LD("CIEN", "10 BOLSITAS DE 10 SON <b>100</b>."),
   LL("60 + 40 = 100.", "70 + 30 = 100.")],
   {"modo": "decenas_op", "que": "sumar"}, {"modo": "decenas_op", "que": "sumar"}),
], "recuerda": [
 RC("SUMA O RESTA", "SI LLEGAN SUMAMOS Y SI SE VAN RESTAMOS.", "50 + 20 Y 90 − 60"),
 RC("CIEN", "SON DIEZ BOLSITAS DE DIEZ.", "70 + 30 = 100"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("¿CUÁNTO ES 20 + 30?", 50, "2 + 3 = 5 BOLSITAS: 50.", **A),
      MC("¿CUÁNTO ES 40 + 10?", ["50", "41", "14"], "50", "4 + 1 = 5 BOLSITAS.", **A),
      MC("LEO DICE QUE 30 + 20 ES 3020. ¿CUÁNTO ES DE VERDAD?", ["50", "3020", "32"], "50", "3 + 2 = 5 BOLSITAS: 50.", **ER),
      UNIR("UNÍ CADA SUMA CON SU RESULTADO.", ["10 + 10", "30 + 30", "50 + 20"], ["70", "20", "60"], {"10 + 10": "20", "30 + 30": "60", "50 + 20": "70"}, "20, 60 Y 70.", **A)],
"2": [N("¿CUÁNTO ES 70 − 20?", 50, "7 − 2 = 5 BOLSITAS: 50.", **A),
      N("SOFI TIENE 80 CARAMELOS. VENDE 30. ¿CUÁNTOS LE QUEDAN?", 50, "8 − 3 = 5 BOLSITAS.", **A),
      FB("COMPLETÁ: 60 − 40 = ___", [["20"]], "6 − 4 = 2 BOLSITAS: 20.", **A),
      MC("TOMI HIZO 90 − 30 = 120. ¿QUÉ HIZO MAL?", ["SUMÓ EN VEZ DE RESTAR", "NADA, ESTÁ BIEN", "LE FALTA UN 0"], "SUMÓ EN VEZ DE RESTAR", "90 − 30 = 60.", **ER)],
"3": [N("10, 20, 30, ___ ¿QUÉ NÚMERO SIGUE?", 40, "SUMAMOS 10.", **A),
      N("100, 90, 80, ___ ¿QUÉ NÚMERO SIGUE?", 70, "RESTAMOS 10.", **A),
      ORD("ORDENÁ PARA CONTAR PARA ATRÁS DE 10 EN 10.", ["60", "90", "70", "80"], ["90", "80", "70", "60"], "90, 80, 70, 60.", **A),
      FB("COMPLETÁ: 30, 40, ___, 60, ___", [["50"], ["70"]], "DE 10 EN 10.", **A)],
"4": [N("¿CUÁNTO ES 60 + 40?", 100, "6 + 4 = 10 BOLSITAS: 100.", **A),
      MC("HAY 50 CARAMELOS. LLEGAN 20 MÁS. ¿QUÉ CUENTA HACEMOS?", ["50 + 20", "50 − 20", "20 − 50"], "50 + 20", "SI LLEGAN MÁS, SUMAMOS.", **AN),
      CLAS("¿SUMA O RESTA?", ["LLEGAN 30 MÁS", "SE VENDEN 20", "SE PIERDEN 10", "COMPRA 40 MÁS"], ["SUMA", "RESTA"],
           {"LLEGAN 30 MÁS": "SUMA", "SE VENDEN 20": "RESTA", "SE PIERDEN 10": "RESTA", "COMPRA 40 MÁS": "SUMA"}, "SI LLEGAN SUMAMOS; SI SE VAN RESTAMOS.", **AN),
      N("[[problema]] EL KIOSCO TENÍA 90 CHUPETINES Y VENDIÓ 50. ¿CUÁNTOS CHUPETINES LE QUEDAN?", 40, "9 − 5 = 4 BOLSITAS: 40.", **AN, **NEU("LA TIENDA TENÍA 90 PALETAS Y VENDIÓ 50. ¿CUÁNTAS PALETAS LE QUEDAN?"))],
"5": [N("RELÁMPAGO. ¿CUÁNTO ES 30 + 30?", 60, "3 + 3 = 6 BOLSITAS.", tiempo=30, **A),
      N("RELÁMPAGO. ¿CUÁNTO ES 90 − 40?", 50, "9 − 4 = 5 BOLSITAS.", tiempo=30, **A),
      N("RELÁMPAGO. 50, 60, 70, ___", 80, "DE 10 EN 10.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿CUÁNTAS BOLSITAS DE 10 SON 100?", ["10", "100", "1"], "10", "10 BOLSITAS DE 10.", tiempo=30, **RE)],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 10 + 20?", 30, "1 + 2 = 3 BOLSITAS.", **A)],
 [1, N("¿CUÁNTO ES 50 + 30?", 80, "5 + 3 = 8 BOLSITAS.", **A)],
 [1, MC("MICA DICE QUE 20 + 30 ES 23. ¿CUÁNTO ES DE VERDAD?", ["50", "23", "5"], "50", "5 BOLSITAS DE 10.", **ER)],
 [2, N("¿CUÁNTO ES 60 − 20?", 40, "6 − 2 = 4 BOLSITAS.", **A)],
 [2, FB("COMPLETÁ: 90 − 50 = ___", [["40"]], "9 − 5 = 4 BOLSITAS.", **A)],
 [2, N("[[problema]] TOMI TIENE 70 FIGURITAS. REGALA 40. ¿CUÁNTAS FIGURITAS LE QUEDAN?", 30, "7 − 4 = 3 BOLSITAS.", **AN, **NEU("TOMI TIENE 70 ESTAMPAS. REGALA 40. ¿CUÁNTAS ESTAMPAS LE QUEDAN?"))],
 [3, N("20, 30, 40, ___ ¿QUÉ NÚMERO SIGUE?", 50, "SUMAMOS 10.", **A)],
 [3, N("60, 50, 40, ___ ¿QUÉ NÚMERO SIGUE?", 30, "RESTAMOS 10.", **A)],
 [3, MC("¿CUÁL CUENTA DE 10 EN 10?", ["10, 20, 30", "10, 11, 12", "1, 2, 3"], "10, 20, 30", "SUMAMOS UNA BOLSITA CADA VEZ.", **RE)],
 [4, N("¿CUÁNTO ES 70 + 30?", 100, "7 + 3 = 10 BOLSITAS: 100.", **A)],
 [4, N("HAY 100 CARAMELOS. SE VENDEN 60. ¿CUÁNTOS QUEDAN?", 40, "10 − 6 = 4 BOLSITAS.", **A)],
 [4, MC("SI SE VAN CARAMELOS, HACEMOS UNA…", ["SUMA", "RESTA"], "RESTA", "SI SE VAN, RESTAMOS.", **RE)],
 [4, N("SOFI TIENE 40 CARAMELOS Y COMPRA 50. ¿CUÁNTOS TIENE?", 90, "4 + 5 = 9 BOLSITAS.", **A)],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 12, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: sumar y restar decenas", "examen_titulo": "Nivel jefe: sumar y restar decenas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-12.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
