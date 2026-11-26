# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 5 · Valor posicional con centenas. Genera mision-5.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (cajas de 100, paquetes de 10 y sueltos).
Niveles: 1 el valor de cada cifra · 2 descomponer · 3 armar números con sus partes · 4 cambiar una cifra."""
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
"objetivo": "Vas a saber cuánto vale cada cifra según su lugar.",
"vas_a_ver": ["El lugar de cada cifra", "La misma cifra vale distinto", "Centenas, decenas y unidades"],
"secciones": [
 S(1, "Tres treses", [
  P("Rosa escribió el número <b>333</b>."),
  P("Tiene tres cifras iguales. ¡Pero no valen lo mismo!"),
  D("Valor de la cifra", "Cada cifra vale según su <b>lugar</b>."),
  IMG("El 333", "3 cajas, 3 paquetes y 3 sueltos.", FG.bloques(3, 3, 3)),
 ]),
 S(1, "Cuánto vale cada 3", [
  P("El primer 3 vale <b>300</b>. Está en las centenas."),
  P("El segundo vale <b>30</b>. El último vale <b>3</b>."),
  IMG("Tablero", "Cada cifra en su lugar.", FG.tablero([333, 452, 718])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tablero. Lo vas a usar en la carpeta."),
  IMG("Tablero de práctica", "Mirá dónde está cada cifra.", FG.tablero([574, 245, 457])),
 ]),
],
"ejemplo_completo": {"titulo": "El 5 en 452", "planteo": "¿Cuánto vale el 5 en 452?", "pasos": ["El 5 está en las decenas.", "Una decena es un paquete de 10.", "El 5 vale 50."]},
"ejemplo_incompleto": {"titulo": "El 7 en 718", "planteo": "Completá.", "pasos": ["El 7 está en las ___ .", "El 7 vale ___ ."]},
"ejemplo_solo": {"titulo": "El 4", "planteo": "¿Cuánto vale el 4 en 245?"},
"tip": {"titulo": "Mirá el lugar", "texto": "La misma cifra vale distinto en otro lugar."},
"ojo": ["En 452, el 5 vale 50, no 5.", "Contá los lugares desde la derecha."],
"resumen": [{"titulo": "Centenas", "texto": "Valen cientos."}, {"titulo": "Decenas", "texto": "Valen dieces."}, {"titulo": "Unidades", "texto": "Valen unos."}],
"glosario": [{"palabra": "Lugar", "significado": "Centenas, decenas o unidades."}, {"palabra": "Valor", "significado": "Cuánto vale una cifra en su lugar."}],
"carpeta": ["En 574, ¿cuánto vale el 5?", "En 245, ¿cuánto vale el 4?", "En 457, ¿cuánto vale el 7?"],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"respuestas_carpeta": [["500"], ["40"], ["7"]],
"soluciones": {"incompleto": "Centenas. 700.", "solo": "40.", "carpeta": ["500.", "40.", "7."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a desarmar números en centenas, decenas y unidades.",
"vas_a_ver": ["Desarmar en cajas, paquetes y sueltos", "Escribir la suma", "Cuando hay un cero"],
"secciones": [
 S(1, "Desarmar el 465", [
  P("Rosa arma un pedido de <b>465</b> alfajores."),
  P("Son 4 cajas, 6 paquetes y 5 sueltos."),
  IMG("El pedido de 465", "4 centenas, 6 decenas y 5 unidades.", FG.bloques(4, 6, 5)),
 ]),
 S(1, "La suma", [
  D("Descomponer", "Escribir el número como una suma: <b>465 = 400 + 60 + 5</b>."),
  P("Si hay un 0, esa parte no se suma: <b>708 = 700 + 8</b>."),
  IMG("El 708", "7 cajas y 8 sueltos. No hay paquetes.", FG.bloques(7, 0, 8)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("Pedido para desarmar", "Contá cajas, paquetes y sueltos.", FG.bloques(6, 3, 9)),
 ]),
],
"ejemplo_completo": {"titulo": "Desarmar 738", "planteo": "Desarmá el 738.", "pasos": ["7 centenas: 700.", "3 decenas: 30.", "8 unidades: 8.", "738 = 700 + 30 + 8."]},
"ejemplo_incompleto": {"titulo": "Desarmar 529", "planteo": "Completá.", "pasos": ["529 = 500 + ___ + 9.", "La cifra 2 vale ___ ."]},
"ejemplo_solo": {"titulo": "Desarmar 806", "planteo": "Desarmá el 806 en una suma."},
"tip": {"titulo": "Una parte por cifra", "texto": "Cada cifra da una parte de la suma."},
"ojo": ["465 no es 4 + 6 + 5.", "Si hay un 0, esa parte no está."],
"resumen": [{"titulo": "Desarmar", "texto": "Escribir una suma."}, {"titulo": "Partes", "texto": "Centenas, decenas y unidades."}, {"titulo": "El cero", "texto": "Esa parte no está."}],
"glosario": [{"palabra": "Descomponer", "significado": "Desarmar un número en partes."}, {"palabra": "Parte", "significado": "Lo que vale cada cifra."}],
"carpeta": ["¿Qué número forma el pedido del dibujo?", "En ese número, ¿cuánto vale la cifra de las decenas?", "Tomi dice que 465 es 4 + 6 + 5. ¿Cuánto vale el 4?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["639"], ["30"], ["400"]],
"soluciones": {"incompleto": "20. 20.", "solo": "806 = 800 + 6.", "carpeta": ["639.", "30.", "400: el 4 está en las centenas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a armar números juntando sus partes.",
"vas_a_ver": ["Juntar centenas, decenas y unidades", "Partes desordenadas", "Cuando falta una parte"],
"secciones": [
 S(1, "Juntar las partes", [
  P("Rosa tiene <b>500 + 20 + 7</b> alfajores."),
  P("5 cajas, 2 paquetes y 7 sueltos: <b>527</b>."),
  IMG("El 527", "500 + 20 + 7 = 527.", FG.bloques(5, 2, 7)),
 ]),
 S(1, "Cuando falta una parte", [
  D("Armar", "Juntamos las partes y cada cifra va a <b>su lugar</b>."),
  P("600 + 8 no tiene decenas: va un <b>0</b>. Es <b>608</b>."),
  IMG("Tablero", "Cada parte en su lugar.", FG.tablero([527, 608, 390])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tablero. Lo vas a usar en la carpeta."),
  IMG("Tablero para completar", "Armá cada número.", FG.tablero([243, 806, 570], vacios=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Partes desordenadas", "planteo": "¿Qué número es 4 + 30 + 200?", "pasos": ["Buscamos las centenas: 200.", "Las decenas: 30.", "Las unidades: 4.", "Es 234."]},
"ejemplo_incompleto": {"titulo": "Armar", "planteo": "Completá.", "pasos": ["300 + 50 + 1 = ___ .", "900 + 9 = ___ ."]},
"ejemplo_solo": {"titulo": "Otro número", "planteo": "¿Qué número es 700 + 40?"},
"tip": {"titulo": "Ordená primero", "texto": "Centenas, decenas y unidades, en ese orden."},
"ojo": ["600 + 8 es 608, no 68.", "El orden de la suma no cambia el número."],
"resumen": [{"titulo": "Armar", "texto": "Juntar las partes."}, {"titulo": "Cada cifra", "texto": "Va a su lugar."}, {"titulo": "Si falta", "texto": "Va un 0."}],
"glosario": [{"palabra": "Componer", "significado": "Armar un número con sus partes."}, {"palabra": "Lugar vacío", "significado": "Se escribe con un 0."}],
"carpeta": ["¿Qué número es 200 + 40 + 3?", "¿Qué número es 800 + 6?", "Sofi armó 500 + 70 y escribió 57. ¿Qué número es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["243"], ["806"], ["570"]],
"soluciones": {"incompleto": "351. 909.", "solo": "740.", "carpeta": ["243.", "806.", "570: no hay unidades, va un 0."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver qué pasa cuando cambia una cifra.",
"vas_a_ver": ["Cambiar las unidades", "Cambiar las decenas", "Cambiar las centenas"],
"secciones": [
 S(1, "Una cifra cambia", [
  P("Rosa tenía <b>352</b> alfajores."),
  P("Llegó una caja más de 100: ahora tiene <b>452</b>."),
  P("Solo cambió la cifra de las <b>centenas</b>."),
  IMG("Antes y después", "352 y 452: cambia el 3 por el 4.", FG.tablero([352, 452])),
 ]),
 S(1, "Sumar 10 o sumar 1", [
  D("Cambiar una cifra", "Sumar 100 cambia las centenas. Sumar 10, las decenas. Sumar 1, las unidades."),
  P("352 + 10 = <b>362</b>. 352 + 1 = <b>353</b>."),
  IMG("Tres cambios", "Cambia una sola cifra cada vez.", FG.tablero([352, 362, 353])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("El pedido de 241", "2 cajas, 4 paquetes y 1 suelto.", FG.bloques(2, 4, 1)),
 ]),
],
"ejemplo_completo": {"titulo": "Una caja más", "planteo": "Rosa tiene 518. Llega una caja de 100.", "pasos": ["Cambian las centenas.", "El 5 pasa a 6.", "Ahora tiene 618."]},
"ejemplo_incompleto": {"titulo": "Un paquete más", "planteo": "Completá.", "pasos": ["426 + 10 = ___ .", "Cambió la cifra de las ___ ."]},
"ejemplo_solo": {"titulo": "Un suelto más", "planteo": "¿Cuánto es 739 + 1?"},
"tip": {"titulo": "Mirá qué se suma", "texto": "100, 10 o 1: cambia una sola cifra."},
"ojo": ["352 + 100 es 452, no 353.", "Las otras cifras quedan iguales."],
"resumen": [{"titulo": "+ 100", "texto": "Cambian las centenas."}, {"titulo": "+ 10", "texto": "Cambian las decenas."}, {"titulo": "+ 1", "texto": "Cambian las unidades."}],
"glosario": [{"palabra": "Cambiar", "significado": "Una cifra pasa a otra."}, {"palabra": "Quedar igual", "significado": "La cifra no cambia."}],
"carpeta": ["¿Qué número forma el pedido del dibujo?", "Si llega una caja más de 100, ¿qué número queda?", "Si en cambio llega un paquete de 10, ¿qué número queda?"],
"carpeta_nivel": ["recordar", "aplicar", "aplicar"],
"respuestas_carpeta": [["241"], ["341"], ["251"]],
"soluciones": {"incompleto": "436. Decenas.", "solo": "740.", "carpeta": ["241.", "341.", "251."]},
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
NEU = lambda p: {"neutro": {"p": p}}
N1["leccion"] = {"temas": [
 T("EL LUGAR DE CADA CIFRA", [LD("EL LUGAR", "CADA CIFRA VALE SEGÚN SU <b>LUGAR</b>: CENTENAS, DECENAS O UNIDADES."),
   LL("EN 574, EL 5 VALE 500.", "EN 457, EL 5 VALE 50.")],
   {"modo": "valor"}, {"modo": "valor"}),
 T("LA MISMA CIFRA VALE DISTINTO", [LD("DISTINTO", "EN <b>444</b> HAY TRES 4, PERO CADA UNO VALE DISTINTO."),
   LL("400, 40 Y 4.", "LO QUE CAMBIA ES EL LUGAR.")],
   {"modo": "valor"}, {"modo": "valor"}),
], "recuerda": [
 RC("EL LUGAR", "LA CIFRA VALE SEGÚN DÓNDE ESTÁ EN EL NÚMERO.", "EN 245 EL 4 VALE 40"),
 RC("LA MISMA CIFRA", "PUEDE VALER CIEN, DIEZ O UNO SEGÚN SU LUGAR.", "444 = 400 + 40 + 4"),
]}

N2["leccion"] = {"temas": [
 T("DESARMAR EN UNA SUMA", [LD("DESARMAR", "DESARMAR ES ESCRIBIR EL NÚMERO COMO <b>SUMA</b> DE LO QUE VALE CADA CIFRA."),
   LL("465 = 400 + 60 + 5.", "NO ES 4 + 6 + 5.")],
   {"modo": "valor"}, {"modo": "valor"}),
 T("CUANDO HAY UN CERO", [LD("EL CERO", "SI UNA CIFRA ES <b>0</b>, ESA PARTE NO SE SUMA."),
   LL("708 = 700 + 8.", "905 = 900 + 5.")],
   {"modo": "centenas", "que": "escribir", "max": 9}, {"modo": "valor", "que": "desarmar"}),
], "recuerda": [
 RC("DESARMAR", "ESCRIBIMOS LA SUMA DE LO QUE VALE CADA CIFRA.", "382 = 300 + 80 + 2"),
 RC("EL CERO", "CUANDO HAY UN CERO, ESA PARTE NO SE ESCRIBE.", "708 = 700 + 8"),
]}

N3["leccion"] = {"temas": [
 T("JUNTAR LAS PARTES", [LD("ARMAR", "PARA <b>ARMAR</b> UN NÚMERO, JUNTAMOS CENTENAS, DECENAS Y UNIDADES."),
   LL("200 + 40 + 3 = 243.", "CADA PARTE VA EN SU LUGAR.")],
   {"modo": "valor"}, {"modo": "valor", "que": "desarmar"}),
 T("PARTES DESORDENADAS", [LD("EN DESORDEN", "SI LAS PARTES VIENEN <b>DESORDENADAS</b>, PRIMERO LAS ORDENAMOS."),
   LL("5 + 60 + 200 = 265.", "500 + 70 = 570, NO 57.")],
   {"modo": "valor"}, {"modo": "valor", "que": "desarmar"}),
], "recuerda": [
 RC("ARMAR", "JUNTAMOS LAS PARTES Y CADA UNA VA EN SU LUGAR.", "700 + 40 + 6 = 746"),
 RC("DESORDENADAS", "PRIMERO LAS CENTENAS, DESPUÉS DECENAS Y UNIDADES.", "6 + 800 = 806"),
]}

N4["leccion"] = {"temas": [
 T("SUMAR 100 O 10", [LD("UNA CIFRA CAMBIA", "AL SUMAR <b>100</b> CAMBIAN LAS CENTENAS; AL SUMAR <b>10</b>, LAS DECENAS."),
   LL("352 + 100 = 452.", "426 + 10 = 436.")],
   {"modo": "cambia", "op": 100}, {"modo": "cambia"}),
 T("SUMAR 1", [LD("UN SUELTO", "AL SUMAR <b>1</b> CAMBIAN LAS UNIDADES: SALE EL SIGUIENTE."),
   LL("739 + 1 = 740.", "SI HAY UN 9, CAMBIA TAMBIÉN LA DE AL LADO.")],
   {"modo": "cambia", "op": 1}, {"modo": "cambia"}),
], "recuerda": [
 RC("SUMAR 100", "CAMBIA LA CIFRA DE LAS CENTENAS.", "619 + 100 = 719"),
 RC("SUMAR 10 O 1", "CAMBIAN LAS DECENAS O LAS UNIDADES.", "245 + 10 = 255"),
]}

ACT = {
"1": [MC("¿CUÁNTO VALE EL 5 EN 452?", ["5", "50", "500"], "50", "ESTÁ EN LAS DECENAS.", n="aplicar"),
      MC("¿EN CUÁL NÚMERO EL 7 VALE 700?", ["718", "171", "257"], "718", "EN 718 EL 7 ESTÁ EN LAS CENTENAS.", n="analizar"),
      UNIR("EN EL 333, UNÍ CADA 3 CON LO QUE VALE.", ["EL PRIMER 3", "EL SEGUNDO 3", "EL TERCER 3"], ["3", "300", "30"], {"EL PRIMER 3": "300", "EL SEGUNDO 3": "30", "EL TERCER 3": "3"}, "300, 30 Y 3.", n="analizar"),
      MC("LEO DICE QUE EN 628 EL 2 VALE 2. ¿CUÁNTO VALE DE VERDAD?", ["20", "2", "200"], "20", "ESTÁ EN LAS DECENAS: VALE 20.", n="error")],
"2": [MC("¿CÓMO SE DESARMA 465?", ["400 + 60 + 5", "4 + 6 + 5", "40 + 60 + 50"], "400 + 60 + 5", "CADA CIFRA VALE SEGÚN SU LUGAR.", n="aplicar"),
      FB("COMPLETÁ: 708 = 700 + ___", [["8"]], "NO HAY DECENAS.", n="aplicar"),
      FB("COMPLETÁ: 539 = ___ + 30 + 9", [["500"]], "EL 5 VALE 500.", n="aplicar"),
      CLAS("¿ESTÁ BIEN DESARMADO?", ["275 = 200 + 70 + 5", "381 = 3 + 8 + 1", "604 = 600 + 4", "916 = 90 + 10 + 6"], ["BIEN", "MAL"],
           {"275 = 200 + 70 + 5": "BIEN", "381 = 3 + 8 + 1": "MAL", "604 = 600 + 4": "BIEN", "916 = 90 + 10 + 6": "MAL"}, "CADA CIFRA VALE SEGÚN SU LUGAR.", n="analizar")],
"3": [N("¿QUÉ NÚMERO ES 300 + 50 + 1?", 351, "3 CENTENAS, 5 DECENAS Y 1 UNIDAD.", n="aplicar"),
      MC("SOFI DICE QUE 600 + 8 ES 68. ¿QUÉ NÚMERO ES?", ["608", "68", "6.008"], "608", "NO HAY DECENAS: VA UN 0.", n="error"),
      N("[[problema]] ROSA ARMÓ UN PEDIDO CON 4 + 90 + 700 ALFAJORES. ¿QUÉ NÚMERO FORMA?", 794, "ORDENAMOS: 700 + 90 + 4 = 794.", n="analizar", **NEU("ROSA ARMÓ UN PEDIDO CON 4 + 90 + 700 GALLETAS. ¿QUÉ NÚMERO FORMA?")),
      UNIR("UNÍ CADA SUMA CON SU NÚMERO.", ["200 + 5", "200 + 50", "20 + 5"], ["250", "25", "205"], {"200 + 5": "205", "200 + 50": "250", "20 + 5": "25"}, "205, 250 Y 25.", n="analizar")],
"4": [N("ROSA TIENE 352. LLEGA UNA CAJA DE 100. ¿CUÁNTO TIENE?", 452, "CAMBIAN LAS CENTENAS.", n="aplicar"),
      MC("426 + 10. ¿QUÉ CIFRA CAMBIA?", ["LA DE LAS DECENAS", "LA DE LAS UNIDADES", "LA DE LAS CENTENAS"], "LA DE LAS DECENAS", "426 + 10 = 436.", n="analizar"),
      FB("COMPLETÁ: 518 + 100 = ___", [["618"]], "CAMBIAN LAS CENTENAS.", n="aplicar"),
      MC("JUAN HIZO 245 + 10 Y LE DIO 246. ¿CUÁNTO DA DE VERDAD?", ["255", "246", "345"], "255", "SUMAR 10 CAMBIA LAS DECENAS.", n="error")],
"5": [MC("RELÁMPAGO. ¿CUÁNTO VALE EL 9 EN 290?", ["90", "9"], "90", "ESTÁ EN LAS DECENAS.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿QUÉ NÚMERO ES 400 + 20 + 1?", 421, "4 CENTENAS, 2 DECENAS Y 1 UNIDAD.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 518 + 100 = ___", 618, "CAMBIAN LAS CENTENAS.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 739 + 1 = ___", 740, "739, 740.", tiempo=40, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿CUÁNTO VALE EL 3 EN 538?", ["3", "30", "300"], "30", "ESTÁ EN LAS DECENAS.", n="aplicar")],
 [1, MC("¿CUÁNTO VALE EL 6 EN 614?", ["6", "60", "600"], "600", "ESTÁ EN LAS CENTENAS.", n="aplicar")],
 [1, MC("EN 444, ¿VALEN LO MISMO LOS TRES 4?", ["SÍ", "NO"], "NO", "VALEN 400, 40 Y 4.", n="analizar")],
 [2, MC("¿CÓMO SE DESARMA 382?", ["300 + 80 + 2", "3 + 8 + 2", "30 + 80 + 2"], "300 + 80 + 2", "UNA PARTE POR CIFRA.", n="aplicar")],
 [2, N("905 = 900 + ___", 5, "NO HAY DECENAS.", n="aplicar")],
 [2, MC("TOMI DICE: 253 ES 2 + 5 + 3. ¿CÓMO ES?", ["200 + 50 + 3", "2 + 5 + 3", "20 + 5 + 3"], "200 + 50 + 3", "TOMI SE EQUIVOCÓ: CADA CIFRA VALE SEGÚN SU LUGAR.", n="error")],
 [3, N("¿QUÉ NÚMERO ES 700 + 40 + 6?", 746, "7 CENTENAS, 4 DECENAS Y 6 UNIDADES.", n="aplicar")],
 [3, N("¿QUÉ NÚMERO ES 5 + 60 + 200?", 265, "ORDENAMOS: 200 + 60 + 5.", n="analizar")],
 [3, MC("¿QUÉ NÚMERO ES 400 + 3?", ["43", "403", "4.003"], "403", "NO HAY DECENAS: VA UN 0.", n="aplicar")],
 [4, N("619 + 100 = ___", 719, "CAMBIAN LAS CENTENAS.", n="aplicar")],
 [4, N("245 + 10 = ___", 255, "CAMBIAN LAS DECENAS.", n="aplicar")],
 [4, MC("ROSA TENÍA 352 Y AHORA 362. ¿QUÉ LLEGÓ?", ["UN PAQUETE DE 10", "UNA CAJA DE 100", "UN SUELTO"], "UN PAQUETE DE 10", "CAMBIARON LAS DECENAS.", n="analizar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 5, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: valor posicional con centenas", "examen_titulo": "Nivel jefe: valor posicional con centenas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
