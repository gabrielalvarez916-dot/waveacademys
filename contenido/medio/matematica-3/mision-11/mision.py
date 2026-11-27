# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 11 · Multiplicar por 10, 100 y 1.000. Genera mision-11.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la imprenta de Valen (paquetes de 10, cajas de 100 y pallets de 1.000).
Niveles: 1 la regularidad · 2 por 100 y 1.000 · 3 por redondos · 4 problemas con redondos."""
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
"objetivo": "Vas a multiplicar por 10, 100 y 1.000.",
"vas_a_ver": ["Por 10: un cero", "Por 100: dos ceros", "Por 1.000: tres ceros"],
"secciones": [
 S(1, "Paquetes de 10", [
  P("Valen armó 23 paquetes de 10 hojas."),
  P("23 × 10 = <b>230</b>: las cifras se corren un lugar."),
  IMG("23 × 10", "Un cero al final.", FG.cuentas([("23 × 10", 230)])),
 ]),
 S(1, "La regla", [
  D("Por 10, 100 y 1.000", "Agregamos <b>uno, dos o tres ceros</b> al final."),
  P("7 × 10 = 70. 7 × 100 = 700. 7 × 1.000 = 7.000."),
  IMG("El 7", "Un cero, dos, tres.", FG.cuentas([("7 × 10", 70), ("7 × 100", 700), ("7 × 1.000", "7.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas", "Agregá ceros.", FG.cuentas([("45 × 10", 450), ("9 × 1.000", "9.000")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Por 10", "planteo": "58 × 10.", "pasos": ["Agregamos un cero.", "580."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Agregá ceros.", "pasos": ["6 × 100 = ___ .", "3 × 1.000 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 81 × 10?"},
"tip": {"titulo": "Contá ceros", "texto": "Tantos ceros como tiene el 10, el 100 o el 1.000."},
"ojo": ["Por 10 no es más 10.", "23 × 10 es 230, no 33."],
"resumen": [{"titulo": "× 10", "texto": "Un cero."}, {"titulo": "× 100", "texto": "Dos ceros."}, {"titulo": "× 1.000", "texto": "Tres ceros."}],
"glosario": [{"palabra": "Cero", "significado": "La cifra 0."}, {"palabra": "Regularidad", "significado": "Algo que siempre pasa igual."}],
"carpeta": ["¿Cuánto es 45 × 10?", "¿Cuánto es 9 × 1.000?", "Leo dice que 23 × 10 = 33. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["450"], ["9000", "9.000"], ["230"]],
"soluciones": {"incompleto": "600. 3.000.", "solo": "810.", "carpeta": ["450.", "9.000.", "230."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a multiplicar por 100 y por 1.000.",
"vas_a_ver": ["Cajas de 100", "Pallets de 1.000", "Las cifras se corren"],
"secciones": [
 S(1, "Pallets", [
  P("Llegaron 8 pallets de 1.000 hojas."),
  P("8 × 1.000 = <b>8.000</b>."),
  IMG("Pallets", "De mil en mil.", FG.tren_paso(1000, 8000, 1000)),
 ]),
 S(1, "Por 100", [
  D("Por 100", "Cada cifra se corre <b>dos lugares</b>: agregamos dos ceros."),
  P("36 × 100 = 3.600."),
  IMG("36 × 100", "Dos ceros.", FG.cuentas([("36 × 100", "3.600"), ("50 × 100", "5.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas", "Por 100 y por 1.000.", FG.cuentas([("72 × 100", "7.200"), ("6 × 1.000", "6.000")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Por 100", "planteo": "19 × 100.", "pasos": ["Dos ceros.", "1.900."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Por 100 y 1.000.", "pasos": ["41 × 100 = ___ .", "5 × 1.000 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 80 × 100?"},
"tip": {"titulo": "Lugares", "texto": "Por 100, dos lugares a la izquierda."},
"ojo": ["36 × 100 no es 3.610.", "Por 1.000 van tres ceros."],
"resumen": [{"titulo": "× 100", "texto": "Dos ceros."}, {"titulo": "× 1.000", "texto": "Tres ceros."}, {"titulo": "Cifras", "texto": "Se corren."}],
"glosario": [{"palabra": "Pallet", "significado": "Base grande para llevar cajas."}, {"palabra": "Correr", "significado": "Mover de lugar."}],
"carpeta": ["¿Cuánto es 72 × 100?", "¿Cuánto es 6 × 1.000?", "Mía dice que 36 × 100 = 3.610. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["7200", "7.200"], ["6000", "6.000"], ["3600", "3.600"]],
"soluciones": {"incompleto": "4.100. 5.000.", "solo": "8.000.", "carpeta": ["7.200.", "6.000.", "3.600."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a multiplicar por números redondos.",
"vas_a_ver": ["El redondo es por 10", "La cuenta chica", "El cero al final"],
"secciones": [
 S(1, "Sobres", [
  P("Valen necesita 4 cajas de 30 sobres."),
  P("4 × 3 = 12. Agregamos el cero: <b>120</b>."),
  IMG("4 × 30", "Cuenta chica y un cero.", FG.cuentas([("4 × 3", 12), ("4 × 30", 120)])),
 ]),
 S(1, "Redondos", [
  D("Número redondo", "El 30 es <b>3 × 10</b>: hacemos la cuenta chica y agregamos el cero."),
  P("5 × 40: 5 × 4 = 20, entonces 200."),
  IMG("Más redondos", "Cuenta chica y cero.", FG.cuentas([("6 × 20", 120), ("5 × 40", 200)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas", "Con redondos.", FG.cuentas([("7 × 30", 210), ("8 × 50", 400)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Redondo", "planteo": "3 × 60.", "pasos": ["3 × 6 = 18.", "180."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cuenta chica y cero.", "pasos": ["9 × 20: 9 × 2 = ___ .", "Entonces ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 6 × 70?"},
"tip": {"titulo": "Tapá el cero", "texto": "Tapá el cero, hacé la cuenta y después ponelo."},
"ojo": ["5 × 40 no es 20.", "No olvides el cero."],
"resumen": [{"titulo": "Redondo", "texto": "Por 10."}, {"titulo": "Cuenta chica", "texto": "Primero."}, {"titulo": "Cero", "texto": "Al final."}],
"glosario": [{"palabra": "Redondo", "significado": "Número que termina en 0."}, {"palabra": "Cuenta chica", "significado": "La de la tabla."}],
"carpeta": ["¿Cuánto es 7 × 30?", "¿Cuánto es 8 × 50?", "Juan dice que 5 × 40 = 20. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["210"], ["400"], ["200"]],
"soluciones": {"incompleto": "18. 180.", "solo": "420.", "carpeta": ["210.", "400.", "200."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas con números redondos.",
"vas_a_ver": ["Grupos iguales", "Cuenta chica y ceros", "Responder"],
"secciones": [
 S(1, "Cuadernos", [
  P("6 cajas con 40 cuadernos."),
  P("6 × 4 = 24. Con el cero: <b>240</b> cuadernos."),
  IMG("6 × 40", "Grupos iguales.", FG.cuentas([("6 × 4", 24), ("6 × 40", 240)])),
 ]),
 S(1, "Por hora", [
  D("Problema con redondos", "Si los grupos son iguales, <b>multiplicamos</b> y agregamos los ceros."),
  P("300 hojas por hora, 3 horas: 900."),
  IMG("3 × 300", "Dos ceros.", FG.cuentas([("3 × 3", 9), ("3 × 300", 900)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el problema. Lo vas a usar en la carpeta."),
  IMG("Paquetes", "8 paquetes de 50 hojas.", FG.cuentas([("8 × 50", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Problema", "planteo": "4 bolsas de 20 tapitas.", "pasos": ["4 × 2 = 8.", "Son 80 tapitas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "7 cajas de 100 clips.", "pasos": ["7 × 100 = ___ .", "Son ___ clips."]},
"ejemplo_solo": {"titulo": "Resolvé", "planteo": "9 filas de 30 sillas. ¿Cuántas sillas?"},
"tip": {"titulo": "Grupos", "texto": "Grupos iguales: multiplicá."},
"ojo": ["6 cajas de 40 no es 46.", "Respondé con una oración."],
"resumen": [{"titulo": "Grupos", "texto": "Multiplicar."}, {"titulo": "Ceros", "texto": "Al final."}, {"titulo": "Responder", "texto": "Con oración."}],
"glosario": [{"palabra": "Problema", "significado": "Pregunta con datos."}, {"palabra": "Respuesta", "significado": "Oración que contesta."}],
"carpeta": ["8 paquetes de 50 hojas. ¿Cuántas hojas hay?", "¿Y en 8 paquetes de 500 hojas?", "Leo sumó 6 + 40 para 6 cajas de 40. ¿Cuántos cuadernos hay?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["400"], ["4000", "4.000"], ["240"]],
"soluciones": {"incompleto": "700. 700.", "solo": "270.", "carpeta": ["400.", "4.000.", "240."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("POR 10", [LD("LUGAR NUEVO", "AL MULTIPLICAR <b>POR 10</b>, CADA CIFRA PASA AL LUGAR DE SU IZQUIERDA."),
   LL("LAS UNIDADES QUEDAN EN CERO.", "NO ES SUMAR 10.")],
   {"modo": "por10m", "de": 10}, {"modo": "por10m", "de": 10}),
], "recuerda": [
 RC("POR 10", "LAS CIFRAS SE CORREN UN LUGAR Y APARECE UN CERO.", "58 × 10 = 580"),
 RC("LA REGLA", "POR 10, 100 Y 1.000 AGREGAMOS UNO, DOS Y TRES CEROS.", "6 × 100 = 600"),
]}
N2["leccion"] = {"temas": [
 T("POR 100", [LD("DOS LUGARES", "AL MULTIPLICAR <b>POR 100</b>, CADA CIFRA AVANZA DOS LUGARES."),
   LL("APARECEN DOS CEROS AL FINAL.", "EL NÚMERO SE HACE CIEN VECES MÁS GRANDE.")],
   {"modo": "por10m", "de": 100}, {"modo": "por10m", "de": 100}),
 T("POR 1.000", [LD("TRES LUGARES", "AL MULTIPLICAR <b>POR 1.000</b>, CADA CIFRA AVANZA TRES LUGARES."),
   LL("UN NÚMERO DE UNA CIFRA PASA A LOS MILES.", "APARECEN TRES CEROS.")],
   {"modo": "por10m", "de": 1000}, {"modo": "por10m", "de": 1000}),
], "recuerda": [
 RC("POR 100", "LAS CIFRAS AVANZAN DOS LUGARES Y APARECEN DOS CEROS.", "19 × 100 = 1.900"),
 RC("POR 1.000", "LAS CIFRAS AVANZAN TRES LUGARES Y APARECEN TRES CEROS.", "5 × 1.000 = 5.000"),
]}
N3["leccion"] = {"temas": [
 T("POR UN NÚMERO REDONDO", [LD("TAPAR EL CERO", "UN REDONDO COMO 30 ES <b>3 VECES 10</b>: MULTIPLICAMOS POR 3 Y DESPUÉS POR 10."),
   LL("PRIMERO LA CUENTA DE LA TABLA.", "AL FINAL VUELVE EL CERO.")],
   {"modo": "por10m", "que": "redondos"}, {"modo": "por10m", "que": "redondos"}),
], "recuerda": [
 RC("REDONDOS", "HACEMOS LA CUENTA DE LA TABLA Y AGREGAMOS EL CERO.", "3 × 60: 3 × 6 = 18, ENTONCES 180"),
 RC("TAPAR EL CERO", "TAPAMOS EL CERO, CALCULAMOS Y LO DESTAPAMOS AL FINAL.", "9 × 20 = 180"),
]}
N4["leccion"] = {"temas": [
 T("PROBLEMAS CON REDONDOS", [LD("GRUPOS IGUALES", "SI CADA GRUPO TIENE UN <b>REDONDO</b>, MULTIPLICAMOS CON EL TRUCO DEL CERO."),
   LL("NO SE SUMAN GRUPOS Y CANTIDAD.", "CONTESTAMOS CON PALABRAS.")],
   {"modo": "por10m", "que": "problema"}, {"modo": "por10m", "que": "problema"}),
], "recuerda": [
 RC("PROBLEMA", "MULTIPLICAMOS LOS GRUPOS POR LO QUE TIENE CADA UNO.", "4 BOLSAS DE 20: 80 TAPITAS"),
 RC("RESPONDER", "ESCRIBIMOS UNA ORACIÓN CON EL NÚMERO Y LO QUE CUENTA.", "HAY 270 SILLAS"),
]}

ACT = {
"1": [N("¿CUÁNTO ES 58 × 10?", 580, "UN CERO.", n="aplicar"),
      FB("COMPLETÁ: 6 × 100 = ___", [["600"]], "DOS CEROS.", n="aplicar"),
      MC("LEO DICE QUE 23 × 10 = 33. ¿CUÁNTO ES?", ["230", "33", "2.300"], "230", "NO ES SUMAR 10.", n="error"),
      UNIR("UNÍ CADA CUENTA CON SU RESULTADO.", ["4 × 10", "4 × 100", "4 × 1.000"], ["4.000", "40", "400"], {"4 × 10": "40", "4 × 100": "400", "4 × 1.000": "4.000"}, "UNO, DOS O TRES CEROS.", n="aplicar")],
"2": [N("¿CUÁNTO ES 19 × 100?", 1900, "DOS CEROS.", n="aplicar"),
      MC("¿CUÁNTO ES 5 × 1.000?", ["5.000", "500", "50"], "5.000", "TRES CEROS.", n="aplicar"),
      MC("MÍA DICE QUE 36 × 100 = 3.610. ¿CUÁNTO ES?", ["3.600", "3.610", "360"], "3.600", "DOS CEROS.", n="error"),
      N("[[problema]] LLEGAN 8 PALLETS DE 1.000 HOJAS. ¿CUÁNTAS HOJAS?", 8000, "8 × 1.000.", n="analizar")],
"3": [N("¿CUÁNTO ES 3 × 60?", 180, "3 × 6 = 18.", n="aplicar"),
      FB("COMPLETÁ: 9 × 20 = ___", [["180"]], "9 × 2 = 18.", n="aplicar"),
      MC("JUAN DICE QUE 5 × 40 = 20. ¿CUÁNTO ES?", ["200", "20", "45"], "200", "FALTA EL CERO.", n="error"),
      ORD("ORDENÁ DE MENOR A MAYOR.", ["6 × 70", "2 × 30", "4 × 50"], ["2 × 30", "4 × 50", "6 × 70"], "60, 200 Y 420.", n="analizar")],
"4": [N("4 BOLSAS DE 20 TAPITAS. ¿CUÁNTAS TAPITAS?", 80, "4 × 2 = 8.", n="aplicar"),
      N("[[problema]] 9 FILAS DE 30 SILLAS. ¿CUÁNTAS SILLAS?", 270, "9 × 3 = 27.", n="aplicar"),
      MC("LEO SUMÓ 6 + 40 PARA 6 CAJAS DE 40. ¿CUÁNTOS HAY?", ["240", "46", "64"], "240", "SE MULTIPLICA.", n="error"),
      MC("¿QUÉ CUENTA RESUELVE «7 CAJAS DE 100 CLIPS»?", ["7 × 100", "7 + 100", "100 − 7"], "7 × 100", "GRUPOS IGUALES.", n="analizar")],
"5": [N("RELÁMPAGO. 81 × 10 = ___", 810, "810.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. 80 × 100 = ___", ["8.000", "800"], "8.000", "DOS CEROS.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 6 × 70 = ___", 420, "420.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. POR 1.000 SE AGREGAN…", ["TRES CEROS", "UN CERO"], "TRES CEROS", "1.000.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 45 × 10?", 450, "UN CERO.", n="aplicar")],
 [1, MC("¿CUÁNTO ES 3 × 1.000?", ["3.000", "300", "30"], "3.000", "TRES CEROS.", n="aplicar")],
 [1, TF("MULTIPLICAR POR 10 ES SUMAR 10.", "FALSO", "SE AGREGA UN CERO.", n="error")],
 [2, N("¿CUÁNTO ES 72 × 100?", 7200, "DOS CEROS.", n="aplicar")],
 [2, FB("COMPLETÁ: 41 × 100 = ___", [["4.100", "4100"]], "DOS CEROS.", n="aplicar")],
 [2, MC("AL MULTIPLICAR POR 100, LAS CIFRAS SE CORREN…", ["DOS LUGARES", "UN LUGAR", "NADA"], "DOS LUGARES", "DOS CEROS.", n="recordar")],
 [3, N("¿CUÁNTO ES 7 × 30?", 210, "7 × 3 = 21.", n="aplicar")],
 [3, MC("¿CUÁNTO ES 8 × 50?", ["400", "40", "58"], "400", "8 × 5 = 40.", n="aplicar")],
 [3, CLAS("¿DA MÁS O MENOS DE 200?", ["3 × 50", "5 × 60", "2 × 90", "4 × 70"], ["MENOS DE 200", "MÁS DE 200"], {"3 × 50": "MENOS DE 200", "5 × 60": "MÁS DE 200", "2 × 90": "MENOS DE 200", "4 × 70": "MÁS DE 200"}, "150, 300, 180 Y 280.", n="analizar")],
 [4, N("[[problema]] 8 PAQUETES DE 50 HOJAS. ¿CUÁNTAS HOJAS?", 400, "8 × 5 = 40.", n="aplicar")],
 [4, N("LA IMPRENTA HACE 300 HOJAS POR HORA. ¿CUÁNTAS EN 3 HORAS?", 900, "3 × 300.", n="analizar")],
 [4, MC("NICO DICE QUE 6 CAJAS DE 40 SON 46. ¿CUÁNTOS SON?", ["240", "46", "24"], "240", "6 × 40.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 11, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: multiplicar por 10, 100 y 1.000", "examen_titulo": "Nivel jefe: multiplicar por 10, 100 y 1.000",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-11.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
