# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 8 · Cálculo mental de restas. Genera mision-8.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (cajas de 100, paquetes de 10 y sueltos que se venden).
Niveles: 1 restar decenas y unidades de memoria · 2 restar contando hacia adelante · 3 restar descomponiendo · 4 restas de memoria."""
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
"objetivo": "Vas a restar decenas, centenas y unidades en la cabeza.",
"vas_a_ver": ["Restar cajas y paquetes", "Restar sueltos", "Usar la cuenta chica"],
"secciones": [
 S(1, "Restar cajas y paquetes", [
  P("Rosa tenía 5 cajas. Vendió 2."),
  P("5 − 2 = 3. Entonces <b>500 − 200 = 300</b>."),
  D("Truco", "Si sabés <b>8 − 3</b>, sabés <b>80 − 30</b> y <b>800 − 300</b>."),
  IMG("La misma resta", "Con ceros o sin ceros.", FG.cuentas([("8 − 3", 5), ("80 − 30", 50), ("800 − 300", 500)])),
 ]),
 S(1, "Restar sueltos", [
  P("47 − 5: solo cambian los sueltos. 7 − 5 = 2."),
  P("47 − 5 = <b>42</b>."),
  IMG("47 alfajores", "4 paquetes y 7 sueltos.", FG.bloques(0, 4, 7)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Restas para completar", "Pensá la cuenta chica primero.", FG.cuentas([("700 − 400", 300), ("90 − 60", 30), ("58 − 6", 52)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "600 − 200", "planteo": "¿Cuánto es 600 − 200?", "pasos": ["Pienso 6 − 2 = 4.", "Son 4 cajas.", "600 − 200 = 400."]},
"ejemplo_incompleto": {"titulo": "70 − 40", "planteo": "Completá.", "pasos": ["7 − 4 = ___ .", "70 − 40 = ___ ."]},
"ejemplo_solo": {"titulo": "Sueltos", "planteo": "¿Cuánto es 39 − 4?"},
"tip": {"titulo": "Tapá los ceros", "texto": "Restá los números sin ceros y después agregalos."},
"ojo": ["500 − 200 es 300, no 3.", "En 47 − 5, las decenas no cambian."],
"resumen": [{"titulo": "Cajas", "texto": "500 − 200 = 300."}, {"titulo": "Paquetes", "texto": "80 − 30 = 50."}, {"titulo": "Sueltos", "texto": "47 − 5 = 42."}],
"glosario": [{"palabra": "Restar", "significado": "Sacar, quitar."}, {"palabra": "Cuenta chica", "significado": "La misma resta sin ceros."}],
"carpeta": ["¿Cuánto es 700 − 400?", "¿Cuánto es 90 − 60?", "Tomi dice que 58 − 6 es 2. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["300"], ["30"], ["52"]],
"soluciones": {"incompleto": "3. 30.", "solo": "35.", "carpeta": ["300.", "30.", "52: el 5 de las decenas queda igual."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a restar contando desde el número chico hasta el grande.",
"vas_a_ver": ["Contar para adelante", "Saltos de 10", "Saltos de 100"],
"secciones": [
 S(1, "Contar para adelante", [
  P("Rosa tenía 100 alfajores. Le quedan 70. ¿Cuántos vendió?"),
  D("Restar contando", "Contamos <b>desde el chico</b> hasta el grande y sumamos los saltos."),
  P("70, 80, 90, 100: <b>3 saltos de 10</b>. 100 − 70 = <b>30</b>."),
  IMG("Del 70 al 100", "Tres saltos de 10.", FG.recta_decenas(saltos=[(70, 80), (80, 90), (90, 100)], marcas=[(70, "70"), (100, "100")])),
 ]),
 S(1, "Saltos de 100", [
  P("500 − 300: desde 300 contamos 400, 500."),
  P("<b>2 saltos de 100</b>. 500 − 300 = <b>200</b>."),
  IMG("Del 300 al 500", "Dos camiones de 100.", FG.tren_paso(300, 500, 100)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la recta. La vas a usar en la carpeta."),
  IMG("Del 40 al 100", "Contá los saltos.", FG.recta_decenas(marcas=[(40, "40"), (100, "100")])),
 ]),
],
"ejemplo_completo": {"titulo": "90 − 60", "planteo": "Restá contando para adelante.", "pasos": ["Desde 60: 70, 80, 90.", "Son 3 saltos de 10.", "90 − 60 = 30."]},
"ejemplo_incompleto": {"titulo": "800 − 500", "planteo": "Completá.", "pasos": ["Desde 500: 600, ___ , 800.", "Son ___ saltos de 100.", "800 − 500 = ___ ."]},
"ejemplo_solo": {"titulo": "Contá vos", "planteo": "¿Cuánto es 100 − 80?"},
"tip": {"titulo": "Empezá por el chico", "texto": "Contá los saltos hasta llegar al grande."},
"ojo": ["Contá los saltos, no los números.", "Empezá en el número chico."],
"resumen": [{"titulo": "Contar", "texto": "Del chico al grande."}, {"titulo": "Saltos de 10", "texto": "100 − 70 = 30."}, {"titulo": "Saltos de 100", "texto": "500 − 300 = 200."}],
"glosario": [{"palabra": "Salto", "significado": "Lo que sumamos cada vez."}, {"palabra": "Diferencia", "significado": "Lo que hay entre dos números."}],
"carpeta": ["En la recta, ¿cuánto es 100 − 40?", "¿Cuánto es 600 − 400?", "Sofi contó 70, 80, 90, 100 y dijo que 100 − 70 = 4. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["60"], ["200"], ["30"]],
"soluciones": {"incompleto": "700. 3. 300.", "solo": "20.", "carpeta": ["60.", "200.", "30: contó los números en vez de los saltos."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a restar desarmando los números.",
"vas_a_ver": ["Desarmar el número que restamos", "Restar cada parte", "Juntar al final"],
"secciones": [
 S(1, "Desarmar para restar", [
  P("Rosa tiene 365 alfajores. Vende 42."),
  P("Desarma el 42: <b>40 + 2</b>."),
  IMG("365 alfajores", "3 cajas, 6 paquetes y 5 sueltos.", FG.bloques(3, 6, 5)),
 ]),
 S(1, "Restar cada parte", [
  D("Restar descomponiendo", "Restamos paquetes de paquetes y sueltos de sueltos."),
  P("Cajas: 300. 60 − 40 = 20. 5 − 2 = 3. Queda <b>323</b>."),
  IMG("Parte por parte", "300 + 20 + 3 = 323.", FG.cuentas([("300", 300), ("60 − 40", 20), ("5 − 2", 3)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Restas para desarmar", "Desarmá y restá.", FG.cuentas([("178 − 35", 143), ("496 − 52", 444), ("259 − 27", 232)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "486 − 53", "planteo": "Restá desarmando.", "pasos": ["Cajas: 400.", "Paquetes: 80 − 50 = 30.", "Sueltos: 6 − 3 = 3.", "Queda 433."]},
"ejemplo_incompleto": {"titulo": "275 − 31", "planteo": "Completá.", "pasos": ["Cajas: 200.", "Paquetes: 70 − 30 = ___ .", "Sueltos: 5 − 1 = ___ .", "Queda ___ ."]},
"ejemplo_solo": {"titulo": "Tu resta", "planteo": "¿Cuánto es 147 − 23?"},
"tip": {"titulo": "Cada uno con su igual", "texto": "Paquetes de paquetes, sueltos de sueltos."},
"ojo": ["No restes una decena de una unidad.", "Las cajas que no tocás quedan igual."],
"resumen": [{"titulo": "Desarmar", "texto": "40 + 2."}, {"titulo": "Restar", "texto": "Cada parte de su igual."}, {"titulo": "Juntar", "texto": "Lo que queda."}],
"glosario": [{"palabra": "Quedar", "significado": "Lo que sobra después de restar."}, {"palabra": "Descomponer", "significado": "Desarmar un número en partes."}],
"carpeta": ["¿Cuánto es 178 − 35?", "¿Cuánto es 496 − 52?", "Tomi hizo 259 − 27 y le dio 259. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["143"], ["444"], ["232"]],
"soluciones": {"incompleto": "40. 4. 244.", "solo": "124.", "carpeta": ["143.", "444.", "232: Tomi no restó."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a restar rápido con trucos que ya sabés.",
"vas_a_ver": ["Restar 10 y restar 100", "Restar desde 100", "Elegir el truco"],
"secciones": [
 S(1, "Restar 10 y 100", [
  P("Restar 10 cambia la cifra de las decenas: 364 − 10 = <b>354</b>."),
  P("Restar 100 cambia la cifra de las centenas: 364 − 100 = <b>264</b>."),
  IMG("Menos 10, menos 100", "Cambia una sola cifra.", FG.cuentas([("364 − 10", 354), ("364 − 100", 264)])),
 ]),
 S(1, "Restar desde 100", [
  D("Pareja de 100", "Si 70 + 30 = 100, entonces <b>100 − 70 = 30</b>."),
  P("100 − 60 = <b>40</b>. 100 − 90 = <b>10</b>."),
  IMG("Restas desde 100", "Usá las parejas de 100.", FG.cuentas([("100 − 60", 40), ("100 − 90", 10), ("100 − 50", 50)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Restas rápidas", "Elegí el truco.", FG.cuentas([("572 − 10", 562), ("800 − 100", 700), ("100 − 20", 80)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Elegir el truco", "planteo": "¿Cuánto es 100 − 30?", "pasos": ["Sé que 70 + 30 = 100.", "Entonces 100 − 30 = 70."]},
"ejemplo_incompleto": {"titulo": "Menos 100", "planteo": "Completá.", "pasos": ["645 − 100 = ___ .", "Cambió la cifra de las ___ ."]},
"ejemplo_solo": {"titulo": "Menos 10", "planteo": "¿Cuánto es 283 − 10?"},
"tip": {"titulo": "Mirá antes de restar", "texto": "¿Resta 10? ¿Resta 100? ¿Empieza en 100?"},
"ojo": ["364 − 10 es 354, no 264.", "100 − 70 es 30, no 3."],
"resumen": [{"titulo": "− 10", "texto": "Cambian las decenas."}, {"titulo": "− 100", "texto": "Cambian las centenas."}, {"titulo": "Desde 100", "texto": "Usá las parejas."}],
"glosario": [{"palabra": "De memoria", "significado": "Sin escribir la cuenta."}, {"palabra": "Truco", "significado": "Una forma rápida de calcular."}],
"carpeta": ["¿Cuánto es 572 − 10?", "¿Cuánto es 800 − 100?", "¿Cuánto es 100 − 20?"],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"respuestas_carpeta": [["562"], ["700"], ["80"]],
"soluciones": {"incompleto": "545. Centenas.", "solo": "273.", "carpeta": ["562.", "700.", "80: pareja de 100."]},
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
 T("RESTAR CAJAS Y PAQUETES", [LD("CUENTA CHICA", "PARA RESTAR <b>CENTENAS</b> O <b>DECENAS</b>, PENSAMOS LA CUENTA CHICA."),
   LL("800 − 300: 8 − 3 = 5, SON 500.", "90 − 60: 9 − 6 = 3, SON 30.")],
   {"modo": "mental", "que": "chica", "esc": 100, "op": "resta"}, {"modo": "mental", "que": "chica", "op": "resta"}),
 T("RESTAR SUELTOS", [LD("SOLO LAS UNIDADES", "SI RESTAMOS <b>SUELTOS</b>, CAMBIAN SOLO LAS UNIDADES."),
   LL("47 − 5 = 42.", "58 − 6 = 52, NO 2.")],
   {"modo": "mental", "que": "desarmar", "op": "resta"}, {"modo": "mental", "que": "chica", "esc": 10, "op": "resta"}),
], "recuerda": [
 RC("CUENTA CHICA", "PENSAMOS SIN LOS CEROS Y DESPUÉS LOS PONEMOS.", "700 − 400 = 300"),
 RC("SUELTOS", "AL RESTAR SUELTOS CAMBIAN SOLO LAS UNIDADES.", "47 − 5 = 42"),
]}

N2["leccion"] = {"temas": [
 T("CONTAR PARA ADELANTE", [LD("DESDE EL CHICO", "PARA RESTAR, PODEMOS CONTAR <b>DESDE EL CHICO</b> HASTA EL GRANDE."),
   LL("100 − 70: 80, 90, 100.", "SON 3 SALTOS DE 10: 30.")],
   {"modo": "mental", "que": "falta100", "op": "resta"}, {"modo": "mental", "que": "falta100", "op": "resta"}),
 T("SALTOS DE 100", [LD("SALTOS GRANDES", "CON CENTENAS CONTAMOS <b>DE 100 EN 100</b>."),
   LL("500 − 300: 400, 500.", "SON 2 SALTOS DE 100: 200.")],
   {"modo": "mental", "que": "chica", "esc": 100, "op": "resta"}, {"modo": "mental", "que": "chica", "esc": 100, "op": "resta"}),
], "recuerda": [
 RC("CONTAR PARA ADELANTE", "CONTAMOS DESDE EL CHICO HASTA EL GRANDE.", "100 − 40: 60 SALTANDO DE 10"),
 RC("SALTOS DE 100", "CONTAMOS LAS CAJAS QUE HAY ENTRE LOS DOS.", "600 − 400 = 200"),
]}

N3["leccion"] = {"temas": [
 T("RESTAR CADA PARTE", [LD("DESARMAR", "DESARMAMOS EL NÚMERO QUE RESTAMOS Y <b>RESTAMOS CADA PARTE</b> DE SU PARTE."),
   LL("365 − 42: 60 − 40 Y 5 − 2.", "LAS CENTENAS QUEDAN IGUAL.")],
   {"modo": "mental", "que": "desarmar", "op": "resta"}, {"modo": "mental", "que": "desarmar", "op": "resta"}),
 T("JUNTAR AL FINAL", [LD("JUNTAR", "AL FINAL <b>JUNTAMOS</b> LO QUE QUEDÓ DE CADA PARTE."),
   LL("300 + 20 + 3 = 323.", "SI DA IGUAL QUE ANTES, ALGO SALIÓ MAL.")],
   {"modo": "mental", "que": "desarmar", "op": "resta"}, {"modo": "mental", "que": "desarmar", "op": "resta"}),
], "recuerda": [
 RC("CADA PARTE", "RESTAMOS DECENAS DE DECENAS Y UNIDADES DE UNIDADES.", "70 − 30 = 40 Y 8 − 5 = 3"),
 RC("JUNTAR", "AL FINAL UNIMOS LO QUE QUEDÓ.", "178 − 35 = 143"),
]}

N4["leccion"] = {"temas": [
 T("RESTAR 10 Y RESTAR 100", [LD("UNA CIFRA", "AL RESTAR <b>10</b> O <b>100</b> CAMBIA UNA SOLA CIFRA."),
   LL("572 − 10 = 562.", "483 − 100 = 383.")],
   {"modo": "mental", "que": "truco", "op": "resta"}, {"modo": "mental", "que": "truco", "op": "resta"}),
 T("RESTAR DESDE 100", [LD("DESDE 100", "PARA RESTAR <b>DESDE 100</b>, PENSAMOS QUÉ LE FALTA AL OTRO NÚMERO."),
   LL("100 − 40 = 60, PORQUE 40 + 60 = 100.", "ELEGÍ EL TRUCO QUE TE SIRVA.")],
   {"modo": "mental", "que": "falta100", "op": "resta"}, {"modo": "mental", "que": "falta100", "op": "resta"}),
], "recuerda": [
 RC("RESTAR 10 O 100", "CAMBIA SOLO UNA CIFRA DEL NÚMERO.", "800 − 100 = 700"),
 RC("DESDE 100", "PENSAMOS LO QUE LE FALTA AL OTRO PARA LLEGAR A 100.", "100 − 20 = 80"),
]}

ACT = {
"1": [N("¿CUÁNTO ES 800 − 300?", 500, "8 − 3 = 5: QUEDAN 5 CAJAS.", n="aplicar"),
      MC("¿CUÁNTO ES 47 − 5?", ["42", "2", "37"], "42", "SOLO CAMBIAN LOS SUELTOS.", n="analizar"),
      UNIR("UNÍ CADA RESTA CON SU RESULTADO.", ["900 − 200", "90 − 20", "9 − 2"], ["70", "7", "700"], {"900 − 200": "700", "90 − 20": "70", "9 − 2": "7"}, "LA MISMA CUENTA CHICA: 700, 70 Y 7.", n="analizar"),
      MC("TOMI DICE QUE 58 − 6 ES 2. ¿CUÁNTO ES?", ["52", "2", "12"], "52", "EL 6 SE RESTA DE LOS SUELTOS: 8 − 6 = 2. QUEDAN 52.", n="error")],
"2": [N("100 − 70 = ___", 30, "70, 80, 90, 100: 3 SALTOS DE 10.", n="aplicar"),
      MC("PARA HACER 500 − 300 CONTANDO, ¿DESDE DÓNDE EMPEZÁS?", ["DESDE 300", "DESDE 500", "DESDE 0"], "DESDE 300", "DESDE EL CHICO HASTA EL GRANDE.", n="analizar", **NEU("PARA HACER 500 − 300 CONTANDO, ¿DESDE DÓNDE EMPIEZAS?")),
      FB("COMPLETÁ: 600 − 400 = ___", [["200"]], "500, 600: 2 SALTOS DE 100.", n="aplicar"),
      N("[[problema]] TENÍAS 100 FIGURITAS Y REGALASTE 30. ¿CUÁNTAS TE QUEDAN?", 70, "100 − 30 = 70.", n="analizar", **NEU("TENÍAS 100 ESTAMPAS Y REGALASTE 30. ¿CUÁNTAS TE QUEDAN?"))],
"3": [N("¿CUÁNTO ES 365 − 42?", 323, "300; 60 − 40 = 20; 5 − 2 = 3.", n="aplicar"),
      MC("PARA RESTAR 365 − 42, ¿DE QUÉ RESTAMOS EL 40?", ["DEL 60", "DEL 5", "DEL 300"], "DEL 60", "PAQUETES DE PAQUETES.", n="analizar"),
      FB("COMPLETÁ: 178 − 35 = 100 + 40 + ___ = ___", [["3"], ["143"]], "70 − 30 = 40 Y 8 − 5 = 3.", n="aplicar"),
      MC("JUAN HIZO 259 − 27 Y LE DIO 259. ¿CUÁNTO DA?", ["232", "259", "286"], "232", "50 − 20 = 30 Y 9 − 7 = 2: 232.", n="error")],
"4": [N("¿CUÁNTO ES 483 − 100?", 383, "CAMBIAN LAS CENTENAS.", n="aplicar"),
      N("¿CUÁNTO ES 100 − 40?", 60, "60 + 40 = 100.", n="aplicar"),
      CLAS("¿QUÉ TRUCO CONVIENE?", ["572 − 10", "100 − 20", "800 − 100", "100 − 60"], ["RESTAR 10 O 100", "PENSAR CUÁNTO FALTA PARA 100"],
           {"572 − 10": "RESTAR 10 O 100", "100 − 20": "PENSAR CUÁNTO FALTA PARA 100", "800 − 100": "RESTAR 10 O 100", "100 − 60": "PENSAR CUÁNTO FALTA PARA 100"}, "SI RESTÁS 10 O 100 CAMBIA UNA CIFRA; DESDE 100 PENSÁS LO QUE FALTA.", n="analizar"),
      FB("COMPLETÁ: 572 − 10 = ___", [["562"]], "CAMBIAN LAS DECENAS.", n="aplicar")],
"5": [N("RELÁMPAGO. 900 − 400 = ___", 500, "9 − 4 = 5.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 100 − 90 = ___", 10, "90 + 10 = 100.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 256 − 10 = ___", 246, "CAMBIAN LAS DECENAS.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 68 − 5 = ___", 63, "8 − 5 = 3.", tiempo=40, n="aplicar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 700 − 200?", 500, "7 − 2 = 5.", n="aplicar")],
 [1, N("¿CUÁNTO ES 90 − 50?", 40, "9 − 5 = 4.", n="aplicar")],
 [1, MC("TOMI DICE: 600 − 400 = 2. ¿CUÁNTO ES?", ["200", "2", "20"], "200", "QUEDAN 2 CAJAS DE 100.", n="error")],
 [2, N("100 − 80 = ___", 20, "80, 90, 100: 2 SALTOS DE 10.", n="aplicar")],
 [2, N("¿CUÁNTO ES 400 − 100?", 300, "DESDE 100: 200, 300, 400. 3 SALTOS.", n="aplicar")],
 [2, MC("¿CUÁNTOS SALTOS DE 10 HAY DEL 60 AL 100?", ["4", "40", "6"], "4", "70, 80, 90, 100.", n="analizar")],
 [3, N("¿CUÁNTO ES 287 − 45?", 242, "200; 80 − 40 = 40; 7 − 5 = 2.", n="aplicar")],
 [3, N("¿CUÁNTO ES 659 − 34?", 625, "600; 50 − 30 = 20; 9 − 4 = 5.", n="aplicar")],
 [3, MC("¿CÓMO SE DESARMA 42 PARA RESTAR?", ["40 + 2", "4 + 2", "400 + 2"], "40 + 2", "UN PAQUETE ES 10.", n="aplicar")],
 [4, N("¿CUÁNTO ES 538 − 10?", 528, "CAMBIAN LAS DECENAS.", n="aplicar")],
 [4, N("¿CUÁNTO ES 100 − 30?", 70, "70 + 30 = 100.", n="aplicar")],
 [4, MC("SOFI DICE: 364 − 10 = 264. ¿CUÁNTO ES?", ["354", "264", "363"], "354", "MENOS 10 CAMBIA LAS DECENAS.", n="error")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 8, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: cálculo mental de restas", "examen_titulo": "Nivel jefe: cálculo mental de restas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
