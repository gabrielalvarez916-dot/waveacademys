# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 2 · Los números hasta 500. Genera mision-2.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (igual que en las clases animadas, clases.py).
Niveles: 1 del 200 al 300 · 2 hasta 400 · 3 hasta 500 · 4 leer y escribir números grandes."""
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
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a contar números del 200 al 300.",
"vas_a_ver": ["Dos cajas y más", "Contar del 200 al 300", "Del 299 al 300"],
"secciones": [
 S(1, "Dos cajas y más", [
  P("Rosa ya llenó <b>2 cajas</b> de 100: son 200."),
  P("Después suma paquetes y sueltos."),
  P("2 cajas, 4 paquetes y 6 sueltos son <b>246</b>."),
  IMG("El pedido de 246", "2 cajas, 4 paquetes y 6 sueltos.", FG.bloques(2, 4, 6)),
 ]),
 S(1, "Hasta el 300", [
  D("Trescientos", "Tres cajas de 100 son <b>300</b> alfajores."),
  P("Después del 299 viene el <b>300</b>."),
  IMG("El tren pasa el 300", "297, 298, 299, 300, 301…", FG.tren(296, 303)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("Otro pedido", "Contá cajas, paquetes y sueltos.", FG.bloques(2, 7, 1)),
 ]),
],
"ejemplo_completo": {"titulo": "Un pedido", "planteo": "Hay 2 cajas, 3 paquetes y 4 sueltos.", "pasos": ["Las cajas: 100, 200.", "Los paquetes: 210, 220, 230.", "Los sueltos: 231, 232, 233, 234.", "Son 234 alfajores."]},
"ejemplo_incompleto": {"titulo": "Cerca del 300", "planteo": "Completá.", "pasos": ["297, 298, ___ , 300.", "299, ___ , 301."]},
"ejemplo_solo": {"titulo": "Después del 259", "planteo": "¿Qué número viene después del 259?"},
"tip": {"titulo": "Empezá por las cajas", "texto": "Dos cajas ya son 200."},
"ojo": ["Después del 299 viene el 300.", "Doscientos cinco es 205, no 2005."],
"resumen": [{"titulo": "200", "texto": "Dos cajas de 100."}, {"titulo": "Contar", "texto": "Cajas, paquetes y sueltos."}, {"titulo": "300", "texto": "Tres cajas de 100."}],
"glosario": [{"palabra": "Doscientos", "significado": "Dos centenas: 200."}, {"palabra": "Trescientos", "significado": "Tres centenas: 300."}],
"carpeta": ["¿Cuántas cajas de 100 hay en el pedido?", "¿Cuántos alfajores hay en total en el pedido?", "Tomi dice que después del 299 viene el 2100. ¿Qué número viene?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["2", "dos"], ["271"], ["300", "trescientos"]],
"soluciones": {"incompleto": "299. 300.", "solo": "260.", "carpeta": ["2 cajas.", "271: 200, 270 y 1 suelto.", "300. Tomi se equivocó."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar números hasta el 400.",
"vas_a_ver": ["Contar de 100 en 100", "Tres cajas y más", "Del 399 al 400"],
"secciones": [
 S(1, "De 100 en 100", [
  P("Cada caja suma <b>100</b> alfajores."),
  P("Contamos las cajas: 100, 200, 300, <b>400</b>."),
  IMG("El tren de las cajas", "De 100 en 100 hasta el 400.", FG.tren_paso(100, 400, 100)),
 ]),
 S(1, "Tres cajas y más", [
  P("3 cajas, 7 paquetes y 2 sueltos son <b>372</b>."),
  D("Cuatrocientos", "Después del 399 viene el <b>400</b>: cuatro cajas."),
  IMG("El pedido de 372", "3 cajas, 7 paquetes y 2 sueltos.", FG.bloques(3, 7, 2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Vagones vacíos", "De 10 en 10. Faltan dos números.", FG.tren_paso(310, 400, 10, faltan=(340, 370))),
 ]),
],
"ejemplo_completo": {"titulo": "Contar cajas", "planteo": "Rosa tiene 4 cajas de 100.", "pasos": ["Contamos: 100, 200, 300, 400.", "Hay 400 alfajores.", "4 centenas son 400."]},
"ejemplo_incompleto": {"titulo": "Cerca del 400", "planteo": "Completá.", "pasos": ["396, 397, ___ , 399.", "380, 390, ___ ."]},
"ejemplo_solo": {"titulo": "Un pedido", "planteo": "¿Cuánto es 3 cajas, 1 paquete y 5 sueltos?"},
"tip": {"titulo": "Contá las cajas", "texto": "Cada caja suma 100."},
"ojo": ["Después del 399 viene el 400.", "390 y 10 más es 400, no 3100."],
"resumen": [{"titulo": "De 100 en 100", "texto": "Contar cajas."}, {"titulo": "Pedido", "texto": "Cajas, paquetes y sueltos."}, {"titulo": "400", "texto": "Cuatro cajas de 100."}],
"glosario": [{"palabra": "Cuatrocientos", "significado": "Cuatro centenas: 400."}, {"palabra": "De 100 en 100", "significado": "Sumar 100 cada vez."}],
"carpeta": ["En el tren, ¿qué número falta después del 330?", "¿Qué número falta después del 360?", "¿Cuánto es 3 cajas, 2 paquetes y 8 sueltos?"],
"carpeta_nivel": ["recordar", "recordar", "aplicar"],
"respuestas_carpeta": [["340"], ["370"], ["328"]],
"soluciones": {"incompleto": "398. 400.", "solo": "315.", "carpeta": ["340.", "370.", "328."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a contar números hasta el 500.",
"vas_a_ver": ["Cinco cajas de 100", "De 10 en 10 hasta el 500", "Del 499 al 500"],
"secciones": [
 S(1, "Cinco cajas", [
  P("Rosa llenó <b>5 cajas</b> de 100."),
  D("Quinientos", "Cinco cajas de 100 son <b>500</b> alfajores."),
  IMG("Cinco cajas", "5 cajas, 0 paquetes y 0 sueltos: 500.", FG.bloques(5, 0, 0)),
 ]),
 S(1, "De 10 en 10 hasta el 500", [
  P("De 10 en 10 sumamos un paquete."),
  P("410, 420, 430… hasta el <b>500</b>."),
  IMG("El tren de los paquetes", "Después del 490 viene el 500.", FG.tren_paso(410, 500, 10)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Vagones vacíos", "Faltan dos números.", FG.tren(494, 501, faltan=(497, 500))),
 ]),
],
"ejemplo_completo": {"titulo": "Desde el 460", "planteo": "Contá de 10 en 10 desde el 460.", "pasos": ["470.", "480.", "490.", "¡500! Cinco cajas."]},
"ejemplo_incompleto": {"titulo": "Cerca del 500", "planteo": "Completá.", "pasos": ["470, 480, ___ , 500.", "497, 498, ___ , 500."]},
"ejemplo_solo": {"titulo": "Antes del 500", "planteo": "¿Qué número viene antes del 500?"},
"tip": {"titulo": "Mirá el final", "texto": "Del 499 se salta al 500."},
"ojo": ["Después del 499 viene el 500.", "Quinientos es 500, no 5100."],
"resumen": [{"titulo": "500", "texto": "Cinco cajas de 100."}, {"titulo": "De 10 en 10", "texto": "Sumar un paquete."}, {"titulo": "499", "texto": "Viene antes del 500."}],
"glosario": [{"palabra": "Quinientos", "significado": "Cinco centenas: 500."}, {"palabra": "Antes", "significado": "El número que va atrás."}],
"carpeta": ["En el tren, ¿qué número falta después del 496?", "¿Qué número falta después del 499?", "Contá de 10 en 10 desde el 465. ¿Qué número sigue?"],
"carpeta_nivel": ["recordar", "recordar", "aplicar"],
"respuestas_carpeta": [["497"], ["500", "quinientos"], ["475"]],
"soluciones": {"incompleto": "490. 499.", "solo": "499.", "carpeta": ["497.", "500.", "475."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a leer y escribir números hasta el 500.",
"vas_a_ver": ["Escribir con cifras", "Leer con palabras", "El cero guarda el lugar"],
"secciones": [
 S(1, "Escribir con cifras", [
  P("Cada número tiene <b>tres cifras</b>."),
  P("258 se lee <b>doscientos cincuenta y ocho</b>."),
  IMG("Tablero", "Cada cifra en su lugar.", FG.tablero([258, 307, 450])),
 ]),
 S(1, "Leer con palabras", [
  D("Los nombres", "300 es trescientos. 400 es cuatrocientos. 500 es quinientos."),
  P("307 no tiene decenas: va un <b>0</b> en el medio."),
  IMG("Tarjetas", "Número y nombre.", FG.tarjetas([(300, "trescientos"), (400, "cuatrocientos"), (500, "quinientos")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tablero. Lo vas a usar en la carpeta."),
  IMG("Tablero para completar", "Escribí cada cifra en su lugar.", FG.tablero([346, 205, 480], vacios=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Cuatrocientos doce", "planteo": "¿Cómo se escribe cuatrocientos doce?", "pasos": ["Cuatrocientos: 4 centenas.", "Doce: 1 decena y 2 unidades.", "Se escribe 412."]},
"ejemplo_incompleto": {"titulo": "Doscientos nueve", "planteo": "Completá.", "pasos": ["Doscientos: ___ centenas.", "No hay decenas: va un ___ .", "Se escribe ___ ."]},
"ejemplo_solo": {"titulo": "Leer", "planteo": "Escribí con palabras el número 360."},
"tip": {"titulo": "Mirá el cero", "texto": "Si falta un lugar, va un 0."},
"ojo": ["Trescientos siete es 307, no 3007.", "Quinientos se escribe con q."],
"resumen": [{"titulo": "Escribir", "texto": "Con cifras: 258."}, {"titulo": "Leer", "texto": "Con palabras."}, {"titulo": "El cero", "texto": "Guarda el lugar."}],
"glosario": [{"palabra": "Cifra", "significado": "Cada símbolo de un número."}, {"palabra": "Tres cifras", "significado": "Centenas, decenas y unidades."}],
"carpeta": ["Escribí con cifras: doscientos cinco.", "Escribí con cifras: cuatrocientos ochenta.", "Sofi escribió 3006 para trescientos seis. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["205"], ["480"], ["306"]],
"soluciones": {"incompleto": "2. 0. 209.", "solo": "Trescientos sesenta.", "carpeta": ["205.", "480.", "306: tres cifras, el 0 en el medio."]},
}

ACT = {
"1": [N("2 CAJAS, 5 PAQUETES Y 1 SUELTO. ¿CUÁNTOS SON?", 251, "200 + 50 + 1 = 251.", n="aplicar"),
      MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 299?", ["300", "2.100", "290"], "300", "DESPUÉS DEL 299 VIENE EL 300.", n="recordar")],
"2": [MC("DE 100 EN 100: 100, 200, 300, ___", ["400", "310", "3.100"], "400", "SUMAMOS UNA CAJA.", n="aplicar"),
      N("3 CAJAS, 6 PAQUETES Y 4 SUELTOS. ¿CUÁNTOS SON?", 364, "300 + 60 + 4 = 364.", n="aplicar")],
"3": [N("¿CUÁNTO ES 5 CAJAS DE 100?", 500, "100, 200, 300, 400, 500.", n="recordar"),
      MC("DE 10 EN 10: 470, 480, 490, ___", ["500", "491", "4.100"], "500", "490 Y UN PAQUETE SON 500.", n="aplicar")],
"4": [MC("¿CÓMO SE ESCRIBE TRESCIENTOS SIETE?", ["37", "307", "3.007"], "307", "EL 0 GUARDA EL LUGAR DE LAS DECENAS.", n="aplicar"),
      ORD("ORDENÁ LAS CIFRAS PARA ESCRIBIR DOSCIENTOS CINCUENTA Y OCHO.", ["8", "2", "5"], ["2", "5", "8"], "2 CENTENAS, 5 DECENAS Y 8 UNIDADES.", n="analizar")],
"5": [N("RELÁMPAGO. ¿QUÉ VIENE DESPUÉS DEL 399?", 400, "399, 400.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁNTO ES 3 CAJAS DE 100?", ["300", "30"], "300", "100, 200, 300.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CÓMO SE ESCRIBE CUATROCIENTOS CINCO?", ["405", "4.005"], "405", "NO HAY DECENAS: VA UN 0.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 2 CAJAS, 2 PAQUETES Y 2 SUELTOS. ¿CUÁNTOS?", 222, "200 + 20 + 2.", tiempo=40, n="aplicar")],
}
EXAMEN = [
 [1, N("2 CAJAS, 8 PAQUETES Y 3 SUELTOS. ¿CUÁNTOS SON?", 283, "200 + 80 + 3 = 283.", n="aplicar")],
 [1, MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 249?", ["250", "2.410", "240"], "250", "249, 250.", n="recordar")],
 [1, MC("LUCÍA DICE: DESPUÉS DEL 299 VIENE EL 2100. ¿QUÉ VIENE?", ["300", "2100", "290"], "300", "LUCÍA SE EQUIVOCÓ: VIENE EL 300.", n="error")],
 [2, N("¿CUÁNTO ES 4 CAJAS DE 100?", 400, "100, 200, 300, 400.", n="recordar")],
 [2, N("3 CAJAS, 1 PAQUETE Y 9 SUELTOS. ¿CUÁNTOS SON?", 319, "300 + 10 + 9 = 319.", n="aplicar")],
 [2, MC("DE 10 EN 10: 370, 380, 390, ___", ["400", "391", "3.100"], "400", "390 Y UN PAQUETE SON 400.", n="aplicar")],
 [3, MC("¿QUÉ NÚMERO VIENE ANTES DEL 500?", ["499", "501", "400"], "499", "499, 500.", n="recordar")],
 [3, N("DE 10 EN 10 DESDE EL 455: 455, 465, ___", 475, "LA ÚLTIMA CIFRA SIGUE SIENDO 5.", n="aplicar")],
 [3, MC("¿CUÁNTAS CAJAS DE 100 HAY EN 500?", ["5", "50", "500"], "5", "5 CENTENAS SON 500.", n="analizar")],
 [4, MC("¿CÓMO SE LEE 258?", ["DOSCIENTOS CINCUENTA Y OCHO", "VEINTICINCO", "DOS CINCO OCHO"], "DOSCIENTOS CINCUENTA Y OCHO", "2 CENTENAS, 5 DECENAS Y 8 UNIDADES.", n="recordar")],
 [4, MC("¿CÓMO SE ESCRIBE CUATROCIENTOS DOCE?", ["412", "4.012", "40.012"], "412", "4 CENTENAS, 1 DECENA Y 2 UNIDADES.", n="aplicar")],
 [4, MC("SOFI ESCRIBIÓ 3006 PARA TRESCIENTOS SEIS. ¿CÓMO VA?", ["306", "3006", "36"], "306", "TRES CIFRAS: EL 0 VA EN EL MEDIO.", n="error")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: los números hasta 500", "examen_titulo": "Nivel jefe: los números hasta 500",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
