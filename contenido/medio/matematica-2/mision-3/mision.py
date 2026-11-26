# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 3 · Los números hasta 1.000. Genera mision-3.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (igual que en las clases animadas, clases.py)."""
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
"objetivo": "Vas a conocer las centenas: grupos de 100.",
"vas_a_ver": ["Unidad, decena y centena", "10 decenas forman 1 centena", "Contar de 100 en 100"],
"secciones": [
 S(1, "Sueltos, paquetes y cajas", [
  P("La abuela Rosa hace alfajores."),
  P("Un alfajor es una <b>unidad</b>. Un paquete de 10 es una <b>decena</b>."),
  D("Centena", "Una caja de <b>100</b> alfajores es una <b>centena</b>. Tiene 10 paquetes de 10."),
  IMG("Cajas, paquetes y sueltos", "1 caja, 3 paquetes y 4 sueltos.", FG.bloques(1, 3, 4)),
 ]),
 S(1, "De 100 en 100", [
  P("Contamos las cajas de 100 en 100: <b>100, 200, 300…</b>"),
  IMG("La recta de 100 en 100", "Del 0 al 1.000.", FG.recta_cien([(300, "300"), (800, "800")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cajas. Las vas a usar en la carpeta."),
  IMG("Las cajas de Rosa", "Contá las cajas de 100.", FG.bloques(6, 0, 0)),
 ]),
],
"ejemplo_completo": {"titulo": "Tres cajas", "planteo": "Rosa tiene 3 cajas de 100.", "pasos": ["Contamos: 100, 200, 300.", "Hay 300 alfajores.", "3 centenas son 300."]},
"ejemplo_incompleto": {"titulo": "Cinco cajas", "planteo": "Completá.", "pasos": ["100, 200, 300, ___ , 500.", "5 centenas son ___ ."]},
"ejemplo_solo": {"titulo": "Paquetes", "planteo": "¿Cuántos paquetes de 10 entran en una caja de 100?"},
"tip": {"titulo": "Contá las cajas", "texto": "Cada caja suma 100."},
"ojo": ["Una caja de 100 no es 10.", "10 paquetes de 10 son 100."],
"resumen": [{"titulo": "Unidad", "texto": "Un suelto."}, {"titulo": "Decena", "texto": "Un paquete de 10."}, {"titulo": "Centena", "texto": "Una caja de 100."}],
"glosario": [{"palabra": "Decena", "significado": "Un grupo de 10."}, {"palabra": "Centena", "significado": "Un grupo de 100."}],
"carpeta": ["¿Cuántas cajas de 100 hay en el dibujo?", "¿Cuántos alfajores hay en esas cajas?", "¿Cuánto es 10 decenas?"],
"respuestas_carpeta": [["6"], ["600"], ["100", "1 centena", "una centena"]],
"soluciones": {"incompleto": "400. 500.", "solo": "10 paquetes.", "carpeta": ["6 cajas.", "600 alfajores.", "100: una centena."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar números hasta el 1.000.",
"vas_a_ver": ["Contar cajas, paquetes y sueltos", "Contar de 10 en 10", "10 centenas son 1.000"],
"secciones": [
 S(1, "Cajas, paquetes y sueltos", [
  P("Primero contamos las cajas, después los paquetes y al final los sueltos."),
  P("100, 200. Después 210, 220, 230. Después 231, 232… <b>235</b>."),
  IMG("El pedido de hoy", "2 cajas, 3 paquetes y 5 sueltos: 235.", FG.bloques(2, 3, 5)),
 ]),
 S(1, "Hasta el 1.000", [
  D("Mil", "Diez cajas de 100 llenan un camión: <b>1.000</b> alfajores."),
  IMG("La recta hasta 1.000", "Después del 999 viene el 1.000.", FG.recta_cien([(1000, "1.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("Otro pedido", "Contá cajas, paquetes y sueltos.", FG.bloques(3, 2, 6)),
 ]),
],
"ejemplo_completo": {"titulo": "Un pedido", "planteo": "Hay 1 caja, 2 paquetes y 4 sueltos.", "pasos": ["La caja: 100.", "Los paquetes: 110, 120.", "Los sueltos: 121, 122, 123, 124.", "Son 124 alfajores."]},
"ejemplo_incompleto": {"titulo": "De 10 en 10", "planteo": "Completá.", "pasos": ["340, 350, 360, ___ , 380.", "990, ___ , 1.000."]},
"ejemplo_solo": {"titulo": "Después del 599", "planteo": "¿Qué número viene después del 599?"},
"tip": {"titulo": "Contá en orden", "texto": "Primero las cajas, después los paquetes, al final los sueltos."},
"ojo": ["Después del 999 viene el 1.000.", "De 10 en 10 cambia el número de las decenas."],
"resumen": [{"titulo": "De 10 en 10", "texto": "Contar paquetes."}, {"titulo": "De 100 en 100", "texto": "Contar cajas."}, {"titulo": "1.000", "texto": "Diez centenas."}],
"glosario": [{"palabra": "Mil", "significado": "Diez centenas: 1.000."}, {"palabra": "Contar de 10 en 10", "significado": "Sumar 10 cada vez."}],
"carpeta": ["¿Cuántas cajas de 100 hay en el pedido?", "¿Cuántos alfajores hay en total en el pedido?", "¿Qué número viene después del 999?"],
"respuestas_carpeta": [["3"], ["326"], ["1000", "1.000", "mil"]],
"soluciones": {"incompleto": "370. 1.000 no: 990, 1.000 tiene salto de 10.", "solo": "600.", "carpeta": ["3 cajas.", "326: 300, 320 y 6 sueltos.", "1.000."]},
}
N2["ejemplo_incompleto"]["pasos"] = ["340, 350, 360, ___ , 380.", "970, 980, 990, ___ ."]
N2["soluciones"]["incompleto"] = "370. 1.000."

N3 = {**ESTILO,
"objetivo": "Vas a leer y escribir números hasta el 1.000.",
"vas_a_ver": ["Escribir con tres cifras", "Leer con palabras", "El cero guarda el lugar"],
"secciones": [
 S(1, "Tres cifras", [
  P("Los números de las cajas tienen <b>tres cifras</b>."),
  P("345 se lee <b>trescientos cuarenta y cinco</b>."),
  IMG("Tablero", "Cada cifra en su lugar.", FG.tablero([345, 708, 910])),
 ]),
 S(1, "El cero", [
  D("El cero", "El <b>0</b> guarda un lugar vacío. 708 no tiene decenas."),
  IMG("708", "7 cajas, 0 paquetes y 8 sueltos.", FG.bloques(7, 0, 8)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tablero. Lo vas a usar en la carpeta."),
  IMG("Tablero para completar", "Escribí cada cifra en su lugar.", FG.tablero([506, 830, 999], vacios=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Seiscientos veinte", "planteo": "¿Cómo se escribe seiscientos veinte?", "pasos": ["Seiscientos: 6 centenas.", "Veinte: 2 decenas.", "No hay unidades: va un 0.", "Se escribe 620."]},
"ejemplo_incompleto": {"titulo": "Cuatrocientos cinco", "planteo": "Completá.", "pasos": ["Cuatrocientos: ___ centenas.", "No hay decenas: va un ___ .", "Se escribe ___ ."]},
"ejemplo_solo": {"titulo": "Leer", "planteo": "Escribí con palabras el número 312."},
"tip": {"titulo": "Mirá el cero", "texto": "Si falta un lugar, va un 0."},
"ojo": ["Setecientos ocho es 708, no 7008.", "Leé de izquierda a derecha."],
"resumen": [{"titulo": "Escribir", "texto": "Con cifras: 345."}, {"titulo": "Leer", "texto": "Con palabras."}, {"titulo": "El cero", "texto": "Guarda el lugar."}],
"glosario": [{"palabra": "Cifra", "significado": "Cada símbolo de un número."}, {"palabra": "Lugar", "significado": "Centenas, decenas o unidades."}],
"carpeta": ["Escribí con cifras: quinientos seis.", "Escribí con cifras: ochocientos treinta.", "¿Cuántas centenas tiene el 999?"],
"respuestas_carpeta": [["506"], ["830"], ["9"]],
"soluciones": {"incompleto": "4. 0. 405.", "solo": "Trescientos doce.", "carpeta": ["506.", "830.", "9 centenas."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a saber cuánto vale cada cifra de un número.",
"vas_a_ver": ["Centenas, decenas y unidades", "El valor de cada cifra", "Desarmar un número en una suma"],
"secciones": [
 S(1, "Cada cifra en su lugar", [
  P("Mirá el 243. El 2 está en las <b>centenas</b>."),
  P("El 4 está en las <b>decenas</b>. El 3, en las <b>unidades</b>."),
  IMG("El pedido de 243", "2 cajas, 4 paquetes y 3 sueltos.", FG.bloques(2, 4, 3)),
 ]),
 S(1, "Desarmar el número", [
  D("Cuánto vale", "El 2 vale <b>200</b>. El 4 vale <b>40</b>. El 3 vale <b>3</b>."),
  P("243 = 200 + 40 + 3."),
  IMG("Tablero", "Cada cifra vale según su lugar.", FG.tablero([243, 365, 407])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("Pedido para desarmar", "Contá cajas, paquetes y sueltos.", FG.bloques(5, 1, 7)),
 ]),
],
"ejemplo_completo": {"titulo": "Desarmar 365", "planteo": "¿Cuánto vale cada cifra de 365?", "pasos": ["El 3 vale 300.", "El 6 vale 60.", "El 5 vale 5.", "365 = 300 + 60 + 5."]},
"ejemplo_incompleto": {"titulo": "Desarmar 482", "planteo": "Completá.", "pasos": ["El 4 vale ___ .", "El 8 vale ___ .", "482 = 400 + 80 + ___ ."]},
"ejemplo_solo": {"titulo": "Armar", "planteo": "¿Qué número es 600 + 30 + 9?"},
"tip": {"titulo": "Contá los lugares", "texto": "Desde la derecha: unidades, decenas, centenas."},
"ojo": ["En 365, el 6 vale 60, no 6.", "Si falta un lugar, va un 0."],
"resumen": [{"titulo": "Centenas", "texto": "Cajas de 100."}, {"titulo": "Decenas", "texto": "Paquetes de 10."}, {"titulo": "Unidades", "texto": "Sueltos."}],
"glosario": [{"palabra": "Valor", "significado": "Cuánto vale una cifra según su lugar."}, {"palabra": "Desarmar", "significado": "Escribir el número como una suma."}],
"carpeta": ["¿Qué número forma el pedido del dibujo?", "En ese número, ¿cuánto vale la cifra de las centenas?", "¿Qué número es 300 + 40 + 2?"],
"respuestas_carpeta": [["517"], ["500"], ["342"]],
"soluciones": {"incompleto": "400. 80. 2.", "solo": "639.", "carpeta": ["517.", "500.", "342."]},
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
N1["carpeta_nivel"] = ["recordar", "aplicar", "aplicar"]
N2["carpeta_nivel"] = ["recordar", "aplicar", "recordar"]
N3["carpeta_nivel"] = ["aplicar", "aplicar", "aplicar"]
N4["carpeta_nivel"] = ["aplicar", "aplicar", "aplicar"]

N1["leccion"] = {"temas": [
 T("UNIDAD, DECENA Y CENTENA", [LD("LA CENTENA", "UNA <b>CENTENA</b> ES UN GRUPO DE 100: DIEZ DECENAS."),
   LL("1 SUELTO ES UNA UNIDAD.", "10 UNIDADES SON 1 DECENA; 10 DECENAS, 1 CENTENA.")],
   {"modo": "centenas", "max": 3}, {"modo": "centenas", "max": 3}),
 T("DE 100 EN 100", [LD("CONTAR CENTENAS", "CONTAMOS LAS CENTENAS <b>DE 100 EN 100</b>: 100, 200, 300…"),
   LL("7 CAJAS DE 100 SON 700.", "CAMBIA LA PRIMERA CIFRA.")],
   {"modo": "serie", "de": 100, "desde": 100, "hasta": 500}, {"modo": "serie", "de": 100, "desde": 100, "hasta": 900}),
], "recuerda": [
 RC("LA CENTENA", "ES UN GRUPO DE CIEN, IGUAL A DIEZ DECENAS.", "10 PAQUETES DE 10 = 100"),
 RC("DE 100 EN 100", "SUMAMOS UNA CENTENA CADA VEZ.", "300, 400, 500"),
]}

N2["leccion"] = {"temas": [
 T("CONTAR HASTA 1.000", [LD("TODO JUNTO", "CONTAMOS <b>CAJAS</b>, DESPUÉS <b>PAQUETES</b> Y AL FINAL <b>SUELTOS</b>, HASTA EL 999."),
   LL("2 CAJAS, 3 PAQUETES Y 5: 235.", "200 + 30 + 5 = 235.")],
   {"modo": "centenas", "max": 9}, {"modo": "centenas", "max": 9}),
 T("10 CENTENAS SON 1.000", [LD("MIL", "DESPUÉS DEL <b>999</b> VIENE EL <b>1.000</b>: DIEZ CENTENAS."),
   LL("990, 991… 999, 1.000.", "1.000 SE LEE MIL.")],
   {"modo": "serie", "de": 1, "desde": 990, "hasta": 996}, {"modo": "serie", "de": 10, "desde": 900, "hasta": 1000}),
], "recuerda": [
 RC("CONTAR TODO", "PRIMERO LAS CENTENAS, DESPUÉS DECENAS Y UNIDADES.", "1 CAJA, 4 PAQUETES Y 2 = 142"),
 RC("MIL", "DIEZ CENTENAS JUNTAS FORMAN EL MIL.", "DESPUÉS DEL 999 VIENE EL 1.000"),
]}

N3["leccion"] = {"temas": [
 T("ESCRIBIR CON TRES CIFRAS", [LD("TRES CIFRAS", "ESCRIBIMOS <b>CENTENAS, DECENAS Y UNIDADES</b>, EN ESE ORDEN."),
   LL("OCHOCIENTOS TREINTA: 830.", "SETECIENTOS OCHO: 708.")],
   {"modo": "centenas", "que": "escribir", "max": 9}, {"modo": "centenas", "que": "escribir", "max": 9}),
 T("LEER CON PALABRAS", [LD("LEER", "PARA LEER, DECIMOS PRIMERO LAS <b>CENTENAS</b> Y DESPUÉS EL RESTO."),
   LL("345: TRESCIENTOS CUARENTA Y CINCO.", "620: SEISCIENTOS VEINTE.")],
   {"modo": "centenas", "que": "escribir", "max": 9}, {"modo": "centenas", "que": "leer", "max": 9}),
], "recuerda": [
 RC("ESCRIBIR", "CENTENAS, DECENAS Y UNIDADES; EL CERO GUARDA EL LUGAR.", "QUINIENTOS SEIS ES 506"),
 RC("LEER", "PARA LEER EMPEZAMOS POR LAS CENTENAS.", "620 ES SEISCIENTOS VEINTE"),
]}

N4["leccion"] = {"temas": [
 T("EL VALOR DE CADA CIFRA", [LD("EL LUGAR", "CADA CIFRA VALE SEGÚN SU <b>LUGAR</b>: CENTENAS, DECENAS O UNIDADES."),
   LL("EN 365, EL 6 VALE 60.", "EN 950, EL 9 VALE 900.")],
   {"modo": "valor"}, {"modo": "valor"}),
 T("DESARMAR EN UNA SUMA", [LD("DESARMAR", "PODEMOS <b>DESARMAR</b> UN NÚMERO EN LO QUE VALE CADA CIFRA."),
   LL("427 = 400 + 20 + 7.", "351 = 300 + 50 + 1.")],
   {"modo": "valor"}, {"modo": "valor", "que": "desarmar"}),
], "recuerda": [
 RC("EL LUGAR", "LA MISMA CIFRA VALE DISTINTO SEGÚN DÓNDE ESTÁ.", "EN 243 EL 4 VALE 40"),
 RC("DESARMAR", "SUMAMOS LO QUE VALE CADA CIFRA.", "407 = 400 + 7"),
]}

ACT = {
"1": [N("📦📦📦 TRES CAJAS DE 100. ¿CUÁNTOS ALFAJORES SON?", 300, "100, 200, 300.", n="aplicar", **NEU("📦📦📦 TRES CAJAS DE 100. ¿CUÁNTAS GALLETAS SON?")),
      MC("¿CUÁNTAS DECENAS FORMAN 1 CENTENA?", ["10", "100", "1"], "10", "10 PAQUETES DE 10 SON 100.", n="recordar"),
      UNIR("UNÍ CADA CANTIDAD CON SU NÚMERO.", ["10 DECENAS", "10 UNIDADES", "4 CENTENAS"], ["10", "400", "100"], {"10 DECENAS": "100", "10 UNIDADES": "10", "4 CENTENAS": "400"}, "10 DECENAS = 100, 10 UNIDADES = 10, 4 CENTENAS = 400.", n="analizar"),
      MC("LEO DICE QUE 6 CAJAS DE 100 SON 60. ¿CUÁNTO ES DE VERDAD?", ["600", "60", "106"], "600", "CADA CAJA TIENE 100: 600.", n="error")],
"2": [N("2 CAJAS, 3 PAQUETES Y 5 SUELTOS. ¿CUÁNTOS SON?", 235, "200 + 30 + 5 = 235.", n="aplicar"),
      MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 999?", ["1.000", "990", "9.991"], "1.000", "DESPUÉS DEL 999 VIENE EL 1.000.", n="recordar"),
      FB("COMPLETÁ DE 10 EN 10: 760, 770, ___, 790", [["780"]], "770 Y 10 MÁS SON 780.", n="aplicar"),
      N("[[problema]] UN CAMIÓN LLEVA 6 CAJAS DE 100, 4 PAQUETES DE 10 Y 8 SUELTOS. ¿CUÁNTOS LLEVA?", 648, "600 + 40 + 8 = 648.", n="aplicar")],
"3": [MC("¿CÓMO SE ESCRIBE SETECIENTOS OCHO?", ["78", "708", "7.008"], "708", "EL 0 GUARDA EL LUGAR DE LAS DECENAS.", n="aplicar"),
      MC("¿CÓMO SE LEE 345?", ["TREINTA Y CUATRO", "TRESCIENTOS CUARENTA Y CINCO", "TRES CUATRO CINCO"], "TRESCIENTOS CUARENTA Y CINCO", "3 CENTENAS, 4 DECENAS Y 5 UNIDADES.", n="recordar"),
      UNIR("UNÍ CADA NÚMERO CON SU NOMBRE.", ["905", "950", "590"], ["QUINIENTOS NOVENTA", "NOVECIENTOS CINCO", "NOVECIENTOS CINCUENTA"], {"905": "NOVECIENTOS CINCO", "950": "NOVECIENTOS CINCUENTA", "590": "QUINIENTOS NOVENTA"}, "MIRÁ DÓNDE ESTÁ EL CERO.", n="analizar"),
      MC("SOFI ESCRIBIÓ 6004 PARA SEISCIENTOS CUATRO. ¿CÓMO VA?", ["604", "6004", "64"], "604", "TRES CIFRAS: EL 0 VA EN LAS DECENAS.", n="error")],
"4": [MC("¿CUÁNTO VALE EL 6 EN 365?", ["6", "60", "600"], "60", "ESTÁ EN LAS DECENAS.", n="aplicar"),
      N("¿QUÉ NÚMERO ES 400 + 20 + 7?", 427, "4 CENTENAS, 2 DECENAS Y 7 UNIDADES.", n="aplicar"),
      FB("COMPLETÁ: 538 = ___ + 30 + 8", [["500"]], "EL 5 ESTÁ EN LAS CENTENAS: VALE 500.", n="aplicar"),
      CLAS("EN EL 274, ¿QUÉ LUGAR OCUPA CADA CIFRA?", ["EL 2", "EL 7", "EL 4"], ["CENTENAS", "DECENAS", "UNIDADES"], {"EL 2": "CENTENAS", "EL 7": "DECENAS", "EL 4": "UNIDADES"}, "2 CENTENAS, 7 DECENAS Y 4 UNIDADES.", n="analizar")],
"5": [N("RELÁMPAGO. ¿CUÁNTO ES 5 CENTENAS?", 500, "5 CAJAS DE 100.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿QUÉ VIENE DESPUÉS DEL 499?", ["500", "400"], "500", "499, 500.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CÓMO SE ESCRIBE NOVECIENTOS DIEZ?", ["910", "9.010"], "910", "9 CENTENAS Y 1 DECENA.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿CUÁNTO VALE EL 8 EN 182?", 80, "ESTÁ EN LAS DECENAS.", tiempo=40, n="aplicar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 1 CENTENA?", 100, "UNA CAJA DE 100.", n="recordar")],
 [1, MC("¿CUÁNTOS PAQUETES DE 10 HAY EN UNA CAJA DE 100?", ["10", "100", "5"], "10", "10 X 10 = 100.", n="recordar")],
 [1, N("7 CAJAS DE 100. ¿CUÁNTOS ALFAJORES SON?", 700, "100, 200… 700.", n="aplicar", **NEU("7 CAJAS DE 100. ¿CUÁNTAS GALLETAS SON?"))],
 [2, N("1 CAJA, 4 PAQUETES Y 2 SUELTOS. ¿CUÁNTOS SON?", 142, "100 + 40 + 2.", n="aplicar")],
 [2, FB("COMPLETÁ: 330, 340, 350, ___", [["360"]], "DE 10 EN 10.", n="aplicar")],
 [2, MC("JUAN DICE QUE DESPUÉS DEL 999 VIENE EL 9.100. ¿QUÉ NÚMERO VIENE?", ["1.000", "9.100", "990"], "1.000", "10 CENTENAS SON 1.000.", n="error")],
 [3, MC("¿CÓMO SE ESCRIBE QUINIENTOS SEIS?", ["56", "506", "5.006"], "506", "NO HAY DECENAS: VA UN 0.", n="aplicar")],
 [3, MC("¿CÓMO SE LEE 620?", ["SEISCIENTOS VEINTE", "SESENTA Y DOS", "SEIS DOS CERO"], "SEISCIENTOS VEINTE", "6 CENTENAS Y 2 DECENAS.", n="recordar")],
 [3, MC("¿CÓMO SE ESCRIBE OCHOCIENTOS TREINTA?", ["830", "8.030", "83"], "830", "8 CENTENAS Y 3 DECENAS.", n="aplicar")],
 [4, MC("¿CUÁNTO VALE EL 4 EN 243?", ["4", "40", "400"], "40", "ESTÁ EN LAS DECENAS.", n="aplicar")],
 [4, N("¿QUÉ NÚMERO ES 300 + 50 + 1?", 351, "3 CENTENAS, 5 DECENAS Y 1 UNIDAD.", n="aplicar")],
 [4, MC("[[problema]] UN NÚMERO TIENE 4 CENTENAS, NINGUNA DECENA Y 7 UNIDADES. ¿CUÁL ES?", ["407", "47", "470"], "407", "NO HAY DECENAS: VA UN 0.", n="analizar")],
 [4, MC("¿CUÁNTO VALE EL 9 EN 950?", ["9", "90", "900"], "900", "ESTÁ EN LAS CENTENAS.", n="aplicar")],
]

M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 3, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: los números hasta 1.000", "examen_titulo": "Nivel jefe: los números hasta 1.000",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
