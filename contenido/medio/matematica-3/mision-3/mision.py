# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 3 · Valor posicional con miles. Genera mision-3.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la tienda de bloques de Mía (cubitos, barras de 10, placas de 100 y cubos de 1.000).
Niveles: 1 los cuatro lugares · 2 descomponer con sumas · 3 armar con tarjetas · 4 cambiar una cifra."""
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
"objetivo": "Vas a saber cuánto vale cada cifra.",
"vas_a_ver": ["Cubitos, barras, placas y cubos", "Los cuatro lugares", "Cuánto vale cada cifra"],
"secciones": [
 S(1, "Los bloques de Mía", [
  P("Un cubito vale 1. Una barra, 10."),
  P("Una placa vale 100. Un cubo, <b>1.000</b>."),
  IMG("Los bloques", "Cada uno vale diez veces más.", FG.tarjetas([("1", "cubito"), ("10", "barra"), ("100", "placa"), ("1.000", "cubo")])),
 ]),
 S(1, "Cada cifra en su lugar", [
  D("Valor de la cifra", "Cada cifra vale según su <b>lugar</b>: miles, centenas, decenas o unidades."),
  P("En 2.476, el 2 vale 2.000."),
  IMG("El 2.476", "2.000, 400, 70 y 6.", FG.cuentas([("miles", "2.000"), ("centenas", 400), ("decenas", 70), ("unidades", 6)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Cuánto vale?", "Mirá el lugar de cada cifra.", FG.tarjetas([("5.381", "el 5"), ("3.814", "el 8")], ocultar=())),
 ]),
],
"ejemplo_completo": {"titulo": "¿Cuánto vale?", "planteo": "En 6.452, ¿cuánto vale el 4?", "pasos": ["El 4 está en las centenas.", "Vale 400."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En 7.169:", "pasos": ["El 7 vale ___ .", "El 6 vale ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "En 9.235, ¿cuánto vale el 9?"},
"tip": {"titulo": "Contá lugares", "texto": "Desde la derecha: U, D, C, M."},
"ojo": ["El mismo número vale distinto en otro lugar.", "En 3.814 el 8 vale 800."],
"resumen": [{"titulo": "Cubito", "texto": "1."}, {"titulo": "Placa", "texto": "100."}, {"titulo": "Cubo", "texto": "1.000."}],
"glosario": [{"palabra": "Cifra", "significado": "Cada número del 0 al 9."}, {"palabra": "Lugar", "significado": "Dónde está la cifra."}],
"carpeta": ["En la tarjeta 5.381, ¿cuánto vale el 5?", "En la tarjeta 3.814, ¿cuánto vale el 8?", "Leo dice que en 3.814 el 1 vale 1. ¿Cuánto vale?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["5000", "5.000"], ["800"], ["10"]],
"soluciones": {"incompleto": "7.000. 100.", "solo": "9.000.", "carpeta": ["5.000.", "800.", "10: está en las decenas."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a descomponer números con sumas.",
"vas_a_ver": ["Desarmar un número", "Armar desde la suma", "El cero guarda el lugar"],
"secciones": [
 S(1, "Desarmar", [
  P("3.608 = 3.000 + 600 + 8."),
  P("No hay decenas: el cero guarda el lugar."),
  IMG("Desarmamos el 3.608", "Cada cifra con su valor.", FG.cuentas([("miles", "3.000"), ("centenas", 600), ("unidades", 8)])),
 ]),
 S(1, "Armar desde la suma", [
  D("Descomponer", "Escribir el número como <b>suma</b> del valor de cada cifra."),
  P("7.000 + 30 = 7.030."),
  IMG("Armar", "De la suma al número.", FG.cuentas([("5.000 + 241", "5.241"), ("7.000 + 30", "7.030")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sumas. Las vas a usar en la carpeta."),
  IMG("Sumas para armar", "Escribí el número.", FG.cuentas([("4.000 + 50", "4.050"), ("8.000 + 900", "8.900")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Desarmar", "planteo": "Descomponé 2.719.", "pasos": ["2.000 + 700 + 10 + 9.", "Suma 2.719."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí lo que falta.", "pasos": ["6.305 = 6.000 + ___ + 5", "1.090 = 1.000 + ___"]},
"ejemplo_solo": {"titulo": "Armá", "planteo": "¿Qué número es 9.000 + 400 + 6?"},
"tip": {"titulo": "Contá ceros", "texto": "Miles tienen tres ceros."},
"ojo": ["7.000 + 30 no es 730.", "Si falta un lugar, va un 0."],
"resumen": [{"titulo": "Descomponer", "texto": "Una suma."}, {"titulo": "Cada cifra", "texto": "Su valor."}, {"titulo": "El cero", "texto": "Guarda lugar."}],
"glosario": [{"palabra": "Descomponer", "significado": "Separar en partes."}, {"palabra": "Suma", "significado": "Juntar partes."}],
"carpeta": ["¿Qué número es 4.000 + 50?", "¿Qué número es 8.000 + 900?", "Mía escribió 49 para 4.000 + 9. ¿Qué número es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["4050", "4.050"], ["8900", "8.900"], ["4009", "4.009"]],
"soluciones": {"incompleto": "300. 90.", "solo": "9.406.", "carpeta": ["4.050.", "8.900.", "4.009."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a armar números con tarjetas.",
"vas_a_ver": ["El número más grande", "El número más chico", "Los miles deciden"],
"secciones": [
 S(1, "El más grande", [
  P("Mía tiene 3, 8, 1 y 6."),
  P("La cifra mayor va adelante: <b>8.631</b>."),
  IMG("Tarjetas de Mía", "3, 8, 1 y 6.", FG.tarjetas([("3", ""), ("8", ""), ("1", ""), ("6", "")])),
 ]),
 S(1, "El más chico", [
  D("Más chico", "La cifra <b>menor</b> va en los miles: 1.368."),
  P("Después, de menor a mayor."),
  IMG("Grande y chico", "Con las mismas tarjetas.", FG.tarjetas([("8.631", "más grande"), ("1.368", "más chico")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas para armar", "4, 9, 2 y 5.", FG.tarjetas([("4", ""), ("9", ""), ("2", ""), ("5", "")])),
 ]),
],
"ejemplo_completo": {"titulo": "Armar", "planteo": "Con 7, 2, 5 y 4, el más grande.", "pasos": ["Ordenamos de mayor a menor.", "Queda 7.542."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Con 6, 1, 8 y 3:", "pasos": ["El más grande: ___ .", "El más chico: ___ ."]},
"ejemplo_solo": {"titulo": "Armá", "planteo": "Con 5, 2, 7 y 9, el más chico."},
"tip": {"titulo": "Adelante", "texto": "La cifra de adelante pesa más."},
"ojo": ["El más chico empieza con la menor.", "Usá cada tarjeta una vez."],
"resumen": [{"titulo": "Grande", "texto": "Mayor adelante."}, {"titulo": "Chico", "texto": "Menor adelante."}, {"titulo": "Miles", "texto": "Deciden."}],
"glosario": [{"palabra": "Tarjeta", "significado": "Cartón con una cifra."}, {"palabra": "Armar", "significado": "Juntar cifras en un número."}],
"carpeta": ["Con 4, 9, 2 y 5, armá el más grande.", "Con esas tarjetas, armá el número más chico.", "Leo armó 2.459 como el más grande. ¿Cuál es el más grande?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["9542", "9.542"], ["2459", "2.459"], ["9542", "9.542"]],
"soluciones": {"incompleto": "8.631. 1.368.", "solo": "2.579.", "carpeta": ["9.542.", "2.459.", "9.542."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver qué pasa al cambiar una cifra.",
"vas_a_ver": ["Sumar 1, 10, 100 o 1.000", "Cambia un solo lugar", "Cuando se llena un lugar"],
"secciones": [
 S(1, "Cambia una cifra", [
  P("3.452 + 100 = <b>3.552</b>."),
  P("Solo cambian las centenas."),
  IMG("Sumar 100", "Cambia una sola cifra.", FG.cuentas([("3.452 + 100", "3.552"), ("3.452 + 1.000", "4.452")])),
 ]),
 S(1, "Se llena un lugar", [
  D("Cambio", "Si un lugar llega a 10, <b>pasa al de al lado</b>."),
  P("2.950 + 100 = 3.050."),
  IMG("Se llena", "9 centenas y 1 más.", FG.cuentas([("2.950 + 100", "3.050")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas para completar", "Escribí el resultado.", FG.cuentas([("6.218 + 10", "6.228"), ("6.218 + 1.000", "7.218")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Sumar 10", "planteo": "5.134 + 10.", "pasos": ["Cambian las decenas: 3 y 1 más.", "Queda 5.144."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí el resultado.", "pasos": ["1.807 + 100 = ___", "8.090 + 10 = ___"]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 4.999 + 1?"},
"tip": {"titulo": "Un solo lugar", "texto": "Mirá qué lugar suma."},
"ojo": ["+ 10 cambia las decenas, no los miles.", "4.271 + 10 es 4.281."],
"resumen": [{"titulo": "+ 1, 10, 100", "texto": "Un lugar."}, {"titulo": "+ 1.000", "texto": "Los miles."}, {"titulo": "Llega a 10", "texto": "Pasa al lado."}],
"glosario": [{"palabra": "Cambiar", "significado": "Poner otra cifra."}, {"palabra": "Lugar", "significado": "Miles, centenas, decenas o unidades."}],
"carpeta": ["¿Cuánto es 6.218 + 10?", "¿Cuánto es 6.218 + 1.000?", "Mía dice que 4.271 + 10 = 5.271. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["6228", "6.228"], ["7218", "7.218"], ["4281", "4.281"]],
"soluciones": {"incompleto": "1.907. 8.100.", "solo": "5.000.", "carpeta": ["6.228.", "7.218.", "4.281."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("LOS CUATRO LUGARES", [LD("LUGARES", "<b>MILES, CENTENAS, DECENAS Y UNIDADES</b>: CADA CIFRA TIENE SU LUGAR."),
   LL("UN CUBO VALE 1.000.", "UNA PLACA VALE 100.")],
   {"modo": "valor4"}, {"modo": "valor4"}),
 T("CUÁNTO VALE CADA CIFRA", [LD("VALOR", "LA MISMA CIFRA VALE <b>DISTINTO</b> SEGÚN EL LUGAR."),
   LL("EN 5.381, EL 5 VALE 5.000.", "EN 3.814, EL 8 VALE 800.")],
   {"modo": "valor4"}, {"modo": "valor4"}),
], "recuerda": [
 RC("LUGARES", "CADA CIFRA VA EN MILES, CENTENAS, DECENAS O UNIDADES.", "EN 2.476 HAY 2 MILES"),
 RC("VALOR", "LO QUE VALE UNA CIFRA DEPENDE DE SU LUGAR.", "EN 6.452 EL 4 VALE 400"),
]}
N2["leccion"] = {"temas": [
 T("DESARMAR CON SUMAS", [LD("DESCOMPONER", "ESCRIBIMOS EL NÚMERO COMO <b>SUMA</b> DE LO QUE VALE CADA CIFRA."),
   LL("2.719 = 2.000 + 700 + 10 + 9.", "EL CERO NO SE SUMA.")],
   {"modo": "valor4"}, {"modo": "valor4", "que": "desarmar"}),
 T("ARMAR DESDE LA SUMA", [LD("ARMAR", "PONEMOS CADA PARTE EN SU <b>LUGAR</b>. SI FALTA UNO, VA UN 0."),
   LL("7.000 + 30 = 7.030.", "SIEMPRE SON CUATRO CIFRAS.")],
   {"modo": "valor4"}, {"modo": "valor4", "que": "juntar"}),
], "recuerda": [
 RC("DESCOMPONER", "SEPARAMOS EL NÚMERO EN LO QUE VALE CADA CIFRA.", "3.608 = 3.000 + 600 + 8"),
 RC("ARMAR", "JUNTAMOS LAS PARTES Y EL CERO GUARDA EL LUGAR VACÍO.", "4.000 + 9 = 4.009"),
]}
N3["leccion"] = {"temas": [
 T("EL MÁS GRANDE", [LD("MÁS GRANDE", "PONEMOS LA CIFRA <b>MAYOR</b> EN LOS MILES Y SEGUIMOS BAJANDO."),
   LL("LA CIFRA DE ADELANTE PESA MÁS.", "CADA TARJETA, UNA VEZ.")],
   {"modo": "armar4"}, {"modo": "armar4"}),
 T("EL MÁS CHICO", [LD("MÁS CHICO", "PONEMOS LA CIFRA <b>MENOR</b> EN LOS MILES Y SEGUIMOS SUBIENDO."),
   LL("ES EL ORDEN AL REVÉS.", "LOS MILES DECIDEN.")],
   {"modo": "armar4", "que": "menor"}, {"modo": "armar4", "que": "mezcla"}),
], "recuerda": [
 RC("MÁS GRANDE", "LA CIFRA MAYOR VA ADELANTE, EN LOS MILES.", "CON 7, 2, 5 Y 4: 7.542"),
 RC("MÁS CHICO", "LA CIFRA MENOR VA ADELANTE, EN LOS MILES.", "CON 5, 2, 7 Y 9: 2.579"),
]}
N4["leccion"] = {"temas": [
 T("SUMAR 1.000 O 100", [LD("UN LUGAR", "SUMAR <b>1.000</b> CAMBIA LOS MILES; SUMAR 100, LAS CENTENAS."),
   LL("LAS DEMÁS CIFRAS QUEDAN IGUAL.", "3.452 + 1.000 = 4.452.")],
   {"modo": "cambia4", "op": 1000}, {"modo": "cambia4", "op": 1000}),
 T("SUMAR 10 O 1", [LD("DECENAS Y UNIDADES", "SUMAR <b>10</b> CAMBIA LAS DECENAS; SUMAR 1, LAS UNIDADES."),
   LL("SI LLEGA A 10, PASA AL LADO.", "4.999 + 1 = 5.000.")],
   {"modo": "cambia4", "op": 10}, {"modo": "cambia4"}),
], "recuerda": [
 RC("SUMAR 1.000", "CAMBIA SOLO LA CIFRA DE LOS MILES.", "6.218 + 1.000 = 7.218"),
 RC("SUMAR 10", "CAMBIA LA CIFRA DE LAS DECENAS.", "5.134 + 10 = 5.144"),
]}

ACT = {
"1": [MC("EN 6.452, ¿CUÁNTO VALE EL 4?", ["400", "4", "40"], "400", "ESTÁ EN LAS CENTENAS.", n="aplicar"),
      MC("LEO DICE QUE EN 3.814 EL 1 VALE 1. ¿CUÁNTO VALE?", ["10", "1", "100"], "10", "ESTÁ EN LAS DECENAS.", n="error"),
      UNIR("UNÍ CADA BLOQUE CON LO QUE VALE.", ["CUBO", "PLACA", "BARRA"], ["100", "10", "1.000"], {"CUBO": "1.000", "PLACA": "100", "BARRA": "10"}, "DIEZ VECES MÁS CADA UNO.", n="recordar"),
      N("[[problema]] MÍA TIENE 2 CUBOS, 4 PLACAS, 7 BARRAS Y 6 CUBITOS. ¿QUÉ NÚMERO ES?", 2476, "2.000 + 400 + 70 + 6.", n="analizar")],
"2": [N("¿QUÉ NÚMERO ES 9.000 + 400 + 6?", 9406, "NO HAY DECENAS: VA UN 0.", n="aplicar"),
      FB("COMPLETÁ: 6.305 = 6.000 + ___ + 5", [["300"]], "EL 3 ESTÁ EN LAS CENTENAS.", n="aplicar"),
      MC("MÍA ESCRIBIÓ 49 PARA 4.000 + 9. ¿QUÉ NÚMERO ES?", ["4.009", "49", "4.090"], "4.009", "EL CERO GUARDA EL LUGAR.", n="error"),
      UNIR("UNÍ CADA SUMA CON SU NÚMERO.", ["2.000 + 700 + 9", "2.000 + 70 + 9", "2.000 + 7"], ["2.007", "2.709", "2.079"], {"2.000 + 700 + 9": "2.709", "2.000 + 70 + 9": "2.079", "2.000 + 7": "2.007"}, "MIRÁ DÓNDE VA EL CERO.", n="analizar")],
"3": [N("CON 7, 2, 5 Y 4, ARMÁ EL NÚMERO MÁS GRANDE.", 7542, "LA MAYOR ADELANTE.", n="aplicar"),
      N("CON 5, 2, 7 Y 9, ARMÁ EL NÚMERO MÁS CHICO.", 2579, "LA MENOR ADELANTE.", n="aplicar"),
      MC("CON 4, 9, 2 Y 5, LEO ARMÓ 2.459. ¿CUÁL ES EL MÁS GRANDE?", ["9.542", "2.459", "5.942"], "9.542", "LA MAYOR VA EN LOS MILES.", n="error"),
      ORD("ORDENÁ LAS CIFRAS PARA ARMAR EL MÁS GRANDE.", ["1", "6", "8", "3"], ["8", "6", "3", "1"], "DE MAYOR A MENOR.", n="analizar")],
"4": [N("¿CUÁNTO ES 1.807 + 100?", 1907, "CAMBIAN LAS CENTENAS.", n="aplicar"),
      N("¿CUÁNTO ES 8.090 + 10?", 8100, "9 DECENAS Y 1 MÁS: SE LLENA UNA CENTENA.", n="analizar"),
      MC("MÍA DICE QUE 4.271 + 10 = 5.271. ¿CUÁNTO ES?", ["4.281", "5.271", "4.272"], "4.281", "+ 10 CAMBIA LAS DECENAS.", n="error"),
      CLAS("¿QUÉ LUGAR CAMBIA EN 3.452?", ["+ 1.000", "+ 100", "+ 10", "+ 1"], ["MILES O CENTENAS", "DECENAS O UNIDADES"],
           {"+ 1.000": "MILES O CENTENAS", "+ 100": "MILES O CENTENAS", "+ 10": "DECENAS O UNIDADES", "+ 1": "DECENAS O UNIDADES"}, "CADA SUMA CAMBIA SU LUGAR.", n="aplicar")],
"5": [MC("RELÁMPAGO. EN 7.169, ¿CUÁNTO VALE EL 7?", ["7.000", "700"], "7.000", "MILES.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 5.000 + 30 = ___", 5030, "5.030.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿CUÁNTO ES 4.999 + 1?", 5000, "5.000.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁNTO VALE UNA PLACA?", ["100", "10"], "100", "DIEZ BARRAS.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("EN 9.235, ¿CUÁNTO VALE EL 9?", ["9.000", "900", "9"], "9.000", "ESTÁ EN LOS MILES.", n="aplicar")],
 [1, TF("EN 1.111 TODOS LOS UNOS VALEN LO MISMO.", "FALSO", "CADA UNO VALE SEGÚN SU LUGAR.", n="analizar")],
 [1, N("¿CUÁNTOS CUBITOS HAY EN UN CUBO?", 1000, "DIEZ PLACAS DE 100.", n="recordar")],
 [2, N("¿QUÉ NÚMERO ES 3.000 + 200 + 50 + 4?", 3254, "CADA PARTE EN SU LUGAR.", n="aplicar")],
 [2, FB("COMPLETÁ: 1.090 = 1.000 + ___", [["90"]], "9 DECENAS.", n="aplicar")],
 [2, MC("LEO DICE QUE 6.000 + 8 = 68. ¿QUÉ NÚMERO ES?", ["6.008", "68", "6.080"], "6.008", "SON CUATRO CIFRAS.", n="error")],
 [3, N("CON 3, 9, 6 Y 1, ARMÁ EL NÚMERO MÁS GRANDE.", 9631, "LA MAYOR ADELANTE.", n="aplicar")],
 [3, N("CON 8, 4, 2 Y 7, ARMÁ EL NÚMERO MÁS CHICO.", 2478, "LA MENOR ADELANTE.", n="aplicar")],
 [3, MC("CON 5, 3, 8 Y 6: ¿QUÉ CIFRA VA ADELANTE EN EL MÁS CHICO?", ["3", "8", "5"], "3", "LA MÁS CHICA.", n="analizar")],
 [4, N("¿CUÁNTO ES 2.416 + 1.000?", 3416, "CAMBIAN LOS MILES.", n="aplicar")],
 [4, N("¿CUÁNTO ES 5.960 + 100?", 6060, "9 CENTENAS Y 1 MÁS: SE LLENA UN MIL.", n="analizar")],
 [4, MC("SOFI DICE QUE 7.340 + 100 = 8.340. ¿CUÁNTO ES?", ["7.440", "8.340", "7.350"], "7.440", "+ 100 CAMBIA LAS CENTENAS.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 3, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: valor posicional con miles", "examen_titulo": "Nivel jefe: valor posicional con miles",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
