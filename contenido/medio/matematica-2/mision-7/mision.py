# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 7 · Cálculo mental de sumas. Genera mision-7.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (cajas de 100, paquetes de 10 y sueltos).
Niveles: 1 sumar decenas y centenas · 2 complementos a 100 · 3 sumar descomponiendo · 4 sumas de memoria."""
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
"objetivo": "Vas a sumar decenas y centenas sin hacer la cuenta escrita.",
"vas_a_ver": ["Sumar cajas de 100", "Sumar paquetes de 10", "Usar lo que ya sabés"],
"secciones": [
 S(1, "Sumar cajas", [
  P("Rosa tiene 3 cajas. Le traen 2 cajas más."),
  P("3 + 2 = 5. Entonces <b>300 + 200 = 500</b>."),
  IMG("Cajas de 100", "3 cajas y 2 cajas son 5 cajas.", FG.bloques(5, 0, 0)),
 ]),
 S(1, "Sumar paquetes", [
  D("Truco", "Si sabés <b>4 + 3</b>, sabés <b>40 + 30</b> y <b>400 + 300</b>."),
  P("40 + 30 = <b>70</b>. 400 + 300 = <b>700</b>."),
  IMG("Cuentas amigas", "La misma cuenta, con ceros.", FG.cuentas([("4 + 3", 7), ("40 + 30", 70), ("400 + 300", 700)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas para completar", "Pensá la cuenta chica primero.", FG.cuentas([("200 + 600", 800), ("50 + 40", 90), ("250 + 100", 350)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "500 + 300", "planteo": "¿Cuánto es 500 + 300?", "pasos": ["Pienso 5 + 3 = 8.", "Son 8 cajas.", "500 + 300 = 800."]},
"ejemplo_incompleto": {"titulo": "60 + 20", "planteo": "Completá.", "pasos": ["6 + 2 = ___ .", "60 + 20 = ___ ."]},
"ejemplo_solo": {"titulo": "Cajas", "planteo": "¿Cuánto es 400 + 400?"},
"tip": {"titulo": "Tapá los ceros", "texto": "Sumá los números sin ceros y después agregalos."},
"ojo": ["300 + 200 es 500, no 50.", "40 + 30 es 70, no 700."],
"resumen": [{"titulo": "Cajas", "texto": "300 + 200 = 500."}, {"titulo": "Paquetes", "texto": "40 + 30 = 70."}, {"titulo": "Truco", "texto": "Usá la cuenta chica."}],
"glosario": [{"palabra": "Cálculo mental", "significado": "Hacer la cuenta en la cabeza."}, {"palabra": "Cuenta amiga", "significado": "Una cuenta fácil que ya sabés."}],
"carpeta": ["¿Cuánto es 200 + 600?", "¿Cuánto es 50 + 40?", "¿Cuánto es 250 + 100?"],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"respuestas_carpeta": [["800"], ["90"], ["350"]],
"soluciones": {"incompleto": "8. 80.", "solo": "800.", "carpeta": ["800.", "90.", "350: sumamos una caja."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a encontrar cuánto falta para llegar a 100.",
"vas_a_ver": ["Parejas que suman 10", "Parejas que suman 100", "Cuánto falta para 100"],
"secciones": [
 S(1, "Parejas que suman 10", [
  P("7 + 3 = 10. 6 + 4 = 10."),
  P("Con paquetes: <b>70 + 30 = 100</b>. <b>60 + 40 = 100</b>."),
  IMG("Una caja de 100", "70 y 30 llenan la caja.", FG.recta_decenas(saltos=[(0, 70), (70, 100)], marcas=[(70, "70")])),
 ]),
 S(1, "Cuánto falta", [
  D("Complemento a 100", "Es lo que le <b>falta</b> a un número para llegar a <b>100</b>."),
  P("A 80 le faltan <b>20</b>. A 45 le faltan <b>55</b>."),
  IMG("Parejas de 100", "Cada pareja suma 100.", FG.cuentas([("80 + ___", 20), ("90 + ___", 10), ("45 + ___", 55)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la recta. La vas a usar en la carpeta."),
  IMG("¿Cuánto falta?", "Desde el 60 hasta el 100.", FG.recta_decenas(marcas=[(60, "60"), (100, "100")])),
 ]),
],
"ejemplo_completo": {"titulo": "Desde 40", "planteo": "¿Cuánto le falta a 40 para 100?", "pasos": ["4 + 6 = 10.", "40 + 60 = 100.", "Le faltan 60."]},
"ejemplo_incompleto": {"titulo": "Desde 30", "planteo": "Completá.", "pasos": ["3 + ___ = 10.", "30 + ___ = 100."]},
"ejemplo_solo": {"titulo": "Desde 90", "planteo": "¿Cuánto le falta a 90 para 100?"},
"tip": {"titulo": "Pensá en 10", "texto": "Si 7 + 3 = 10, entonces 70 + 30 = 100."},
"ojo": ["A 70 le faltan 30, no 3.", "80 + 20 = 100, no 1000."],
"resumen": [{"titulo": "Parejas de 10", "texto": "7 + 3, 6 + 4."}, {"titulo": "Parejas de 100", "texto": "70 + 30, 60 + 40."}, {"titulo": "Complemento", "texto": "Lo que falta para 100."}],
"glosario": [{"palabra": "Complemento", "significado": "Lo que falta para completar."}, {"palabra": "Pareja", "significado": "Dos números que suman 100."}],
"carpeta": ["En la recta, ¿cuánto le falta a 60 para 100?", "¿Cuánto le falta a 90 para 100?", "Tomi dice que a 70 le faltan 3 para 100. ¿Cuánto le falta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["40"], ["10"], ["30"]],
"soluciones": {"incompleto": "7. 70.", "solo": "10.", "carpeta": ["40.", "10.", "30: 70 + 30 = 100."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a sumar desarmando los números.",
"vas_a_ver": ["Desarmar en cajas, paquetes y sueltos", "Sumar cada parte", "Juntar al final"],
"secciones": [
 S(1, "Desarmar para sumar", [
  P("Rosa suma 245 + 32."),
  P("Desarma: 245 = 200 + 40 + 5. 32 = 30 + 2."),
  IMG("Los dos pedidos", "245 y 32.", FG.bloques(2, 7, 7)),
 ]),
 S(1, "Sumar cada parte", [
  D("Sumar descomponiendo", "Sumamos las cajas, los paquetes y los sueltos <b>por separado</b>."),
  P("200. 40 + 30 = 70. 5 + 2 = 7. Total: <b>277</b>."),
  IMG("Parte por parte", "200 + 70 + 7 = 277.", FG.cuentas([("200", 200), ("40 + 30", 70), ("5 + 2", 7)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Sumas para desarmar", "Desarmá y sumá.", FG.cuentas([("123 + 45", 168), ("310 + 26", 336), ("452 + 34", 486)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "134 + 52", "planteo": "Sumá desarmando.", "pasos": ["Cajas: 100.", "Paquetes: 30 + 50 = 80.", "Sueltos: 4 + 2 = 6.", "Total: 186."]},
"ejemplo_incompleto": {"titulo": "321 + 46", "planteo": "Completá.", "pasos": ["Cajas: 300.", "Paquetes: 20 + 40 = ___ .", "Sueltos: 1 + 6 = ___ .", "Total: ___ ."]},
"ejemplo_solo": {"titulo": "Tu suma", "planteo": "¿Cuánto es 213 + 24?"},
"tip": {"titulo": "Cada uno con su igual", "texto": "Paquetes con paquetes, sueltos con sueltos."},
"ojo": ["No sumes una decena con una unidad.", "Al final, juntá todas las partes."],
"resumen": [{"titulo": "Desarmar", "texto": "Cajas, paquetes y sueltos."}, {"titulo": "Sumar", "texto": "Cada parte con su igual."}, {"titulo": "Juntar", "texto": "Al final, todo junto."}],
"glosario": [{"palabra": "Descomponer", "significado": "Desarmar un número en partes."}, {"palabra": "Total", "significado": "El resultado de la suma."}],
"carpeta": ["¿Cuánto es 123 + 45?", "¿Cuánto es 310 + 26?", "Sofi hizo 452 + 34 y le dio 792. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["168"], ["336"], ["486"]],
"soluciones": {"incompleto": "60. 7. 367.", "solo": "237.", "carpeta": ["168.", "336.", "486: sumó 3 decenas como centenas."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a sumar rápido con trucos que ya sabés.",
"vas_a_ver": ["Sumar 10 y sumar 100", "Los dobles", "Elegir el truco"],
"secciones": [
 S(1, "Sumar 10 y 100", [
  P("Sumar 10 cambia la cifra de las decenas: 254 + 10 = <b>264</b>."),
  P("Sumar 100 cambia la cifra de las centenas: 254 + 100 = <b>354</b>."),
  IMG("Más 10, más 100", "Cambia una sola cifra.", FG.cuentas([("254 + 10", 264), ("254 + 100", 354)])),
 ]),
 S(1, "Los dobles", [
  D("Doble", "El <b>doble</b> es sumar un número con él mismo."),
  P("20 + 20 = <b>40</b>. 200 + 200 = <b>400</b>. 50 + 50 = <b>100</b>."),
  IMG("Dobles", "Un número sumado con él mismo.", FG.cuentas([("20 + 20", 40), ("50 + 50", 100), ("300 + 300", 600)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Sumas rápidas", "Elegí el truco.", FG.cuentas([("365 + 10", 375), ("400 + 400", 800), ("75 + 25", 100)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Elegir el truco", "planteo": "¿Cuánto es 60 + 40?", "pasos": ["6 + 4 = 10.", "Es una pareja de 100.", "60 + 40 = 100."]},
"ejemplo_incompleto": {"titulo": "Más 100", "planteo": "Completá.", "pasos": ["518 + 100 = ___ .", "Cambió la cifra de las ___ ."]},
"ejemplo_solo": {"titulo": "Un doble", "planteo": "¿Cuánto es 250 + 250?"},
"tip": {"titulo": "Mirá antes de sumar", "texto": "¿Es un doble? ¿Suma 10? ¿Llega a 100?"},
"ojo": ["365 + 10 es 375, no 465.", "El doble de 50 es 100."],
"resumen": [{"titulo": "+ 10", "texto": "Cambian las decenas."}, {"titulo": "+ 100", "texto": "Cambian las centenas."}, {"titulo": "Dobles", "texto": "Un número más él mismo."}],
"glosario": [{"palabra": "Doble", "significado": "Un número más él mismo."}, {"palabra": "Truco", "significado": "Una forma rápida de calcular."}],
"carpeta": ["¿Cuánto es 365 + 10?", "¿Cuánto es 400 + 400?", "¿Cuánto es 75 + 25?"],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"respuestas_carpeta": [["375"], ["800"], ["100"]],
"soluciones": {"incompleto": "618. Centenas.", "solo": "500.", "carpeta": ["375.", "800: doble de 400.", "100: pareja de 100."]},
}

ACT = {
"1": [N("¿CUÁNTO ES 300 + 400?", 700, "3 + 4 = 7: SON 7 CAJAS.", n="aplicar"),
      MC("SI 5 + 2 = 7, ¿CUÁNTO ES 50 + 20?", ["70", "7", "700"], "70", "SON 7 PAQUETES DE 10.", n="analizar")],
"2": [N("70 + ___ = 100", 30, "7 + 3 = 10.", n="aplicar"),
      MC("¿QUÉ PAREJA SUMA 100?", ["60 + 40", "60 + 30", "50 + 40"], "60 + 40", "6 + 4 = 10.", n="aplicar")],
"3": [N("¿CUÁNTO ES 234 + 52?", 286, "200; 30 + 50 = 80; 4 + 2 = 6.", n="aplicar"),
      MC("PARA SUMAR 245 + 32, ¿QUÉ JUNTAMOS CON EL 40?", ["EL 30", "EL 2", "EL 200"], "EL 30", "PAQUETES CON PAQUETES.", n="analizar")],
"4": [N("¿CUÁNTO ES 472 + 100?", 572, "CAMBIAN LAS CENTENAS.", n="aplicar"),
      N("¿CUÁNTO ES 300 + 300?", 600, "EL DOBLE DE 300.", n="aplicar")],
"5": [N("RELÁMPAGO. 200 + 500 = ___", 700, "2 + 5 = 7.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 80 + ___ = 100", 20, "8 + 2 = 10.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 125 + 10 = ___", 135, "CAMBIAN LAS DECENAS.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 50 + 50 = ___", 100, "DOBLE DE 50.", tiempo=40, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 600 + 300?", 900, "6 + 3 = 9.", n="aplicar")],
 [1, N("¿CUÁNTO ES 30 + 50?", 80, "3 + 5 = 8.", n="aplicar")],
 [1, MC("TOMI DICE: 200 + 300 = 50. ¿CUÁNTO ES?", ["500", "50", "5.000"], "500", "SON 5 CAJAS DE 100.", n="error")],
 [2, N("40 + ___ = 100", 60, "4 + 6 = 10.", n="aplicar")],
 [2, MC("¿CUÁNTO LE FALTA A 85 PARA 100?", ["15", "25", "5"], "15", "85 + 15 = 100.", n="analizar")],
 [2, MC("¿CUÁL NO SUMA 100?", ["70 + 20", "70 + 30", "90 + 10"], "70 + 20", "70 + 20 = 90.", n="analizar")],
 [3, N("¿CUÁNTO ES 143 + 25?", 168, "100; 40 + 20 = 60; 3 + 5 = 8.", n="aplicar")],
 [3, N("¿CUÁNTO ES 512 + 47?", 559, "500; 10 + 40 = 50; 2 + 7 = 9.", n="aplicar")],
 [3, MC("¿CÓMO SE DESARMA 245 PARA SUMAR?", ["200 + 40 + 5", "2 + 4 + 5", "24 + 5"], "200 + 40 + 5", "CAJAS, PAQUETES Y SUELTOS.", n="aplicar")],
 [4, N("¿CUÁNTO ES 386 + 10?", 396, "CAMBIAN LAS DECENAS.", n="aplicar")],
 [4, N("¿CUÁNTO ES EL DOBLE DE 200?", 400, "200 + 200 = 400.", n="aplicar")],
 [4, MC("SOFI DICE: 365 + 10 = 465. ¿CUÁNTO ES?", ["375", "465", "366"], "375", "MÁS 10 CAMBIA LAS DECENAS.", n="error")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: cálculo mental de sumas", "examen_titulo": "Nivel jefe: cálculo mental de sumas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
