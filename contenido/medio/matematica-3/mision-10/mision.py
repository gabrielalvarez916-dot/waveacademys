# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 10 · La tabla pitagórica. Genera mision-10.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: el mapa del tesoro de Lucas.
Niveles: 1 armar la tabla · 2 regularidades · 3 tablas del 3, 4 y 6 · 4 tablas del 7, 8 y 9."""
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
"objetivo": "Vas a usar la tabla pitagórica.",
"vas_a_ver": ["Filas y columnas", "Dónde se cruzan", "Fila por columna"],
"secciones": [
 S(1, "El mapa de números", [
  P("Arriba y al costado van los números del 1 al 10."),
  P("Cada casillero es <b>fila por columna</b>."),
  IMG("Fila del 3", "3, 6, 9, 12…", FG.tren_paso(3, 30, 3)),
 ]),
 S(1, "Donde se cruzan", [
  D("Tabla pitagórica", "Un cuadro con <b>todas las tablas</b>: fila por columna."),
  P("Fila 4, columna 7: 4 × 7 = 28."),
  IMG("El cruce", "Fila 4 y columna 7.", FG.cuentas([("fila 4 · col 7", 28), ("fila 6 · col 5", 30)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los cruces. Los vas a usar en la carpeta."),
  IMG("Cruces", "¿Qué número va?", FG.cuentas([("fila 3 · col 8", 24), ("fila 9 · col 2", 18)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar", "planteo": "Fila 5, columna 6.", "pasos": ["5 × 6.", "Va 30."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Fila 2, columna 9.", "pasos": ["2 × 9 = ___ .", "Va ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Qué va en fila 7, columna 3?"},
"tip": {"titulo": "Con el dedo", "texto": "Seguí la fila y la columna con el dedo."},
"ojo": ["Se multiplica, no se suma.", "Fila y columna se cruzan en un solo lugar."],
"resumen": [{"titulo": "Fila", "texto": "Un número."}, {"titulo": "Columna", "texto": "Otro número."}, {"titulo": "Cruce", "texto": "Fila × columna."}],
"glosario": [{"palabra": "Fila", "significado": "Renglón que va acostado."}, {"palabra": "Columna", "significado": "Renglón que va parado."}],
"carpeta": ["¿Qué número va en fila 3, columna 8?", "¿Qué número va en fila 9, columna 2?", "Leo puso 11 en fila 4, columna 7. ¿Qué número va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["24"], ["18"], ["28"]],
"soluciones": {"incompleto": "18. 18.", "solo": "21.", "carpeta": ["24.", "18.", "28."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a descubrir secretos de la tabla.",
"vas_a_ver": ["Filas dobles", "El espejo", "La fila del 5"],
"secciones": [
 S(1, "Filas dobles", [
  P("Fila del 2: 2, 4, 6, 8. Fila del 4: 4, 8, 12, 16."),
  P("La fila del 4 es el <b>doble</b> de la del 2."),
  IMG("Del 2 y del 4", "Doble.", FG.cuentas([("2 × 3", 6), ("4 × 3", 12)])),
 ]),
 S(1, "El espejo", [
  D("Orden", "Dar vuelta la multiplicación <b>no cambia</b> el resultado."),
  P("3 × 5 = 5 × 3 = 15."),
  IMG("Espejo", "Mismo resultado.", FG.cuentas([("3 × 5", 15), ("5 × 3", 15)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Secretos", "Usá los secretos.", FG.cuentas([("3 × 7", 21), ("6 × 7", 42)], ocultar=(1,))),
 ]),
],
"ejemplo_completo": {"titulo": "Doble", "planteo": "2 × 6 = 12.", "pasos": ["4 × 6 es el doble.", "24."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Usá el espejo.", "pasos": ["8 × 3 = 24, entonces 3 × 8 = ___ .", "9 × 2 = 18, entonces 2 × 9 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cómo terminan los números de la fila del 5?"},
"tip": {"titulo": "Mitad del trabajo", "texto": "Con el espejo, sabés la mitad de la tabla."},
"ojo": ["4 × 6 y 6 × 4 dan igual.", "La fila del 10 termina en 0."],
"resumen": [{"titulo": "Doble", "texto": "Fila del 4 y del 2."}, {"titulo": "Espejo", "texto": "El orden no cambia."}, {"titulo": "Fila del 5", "texto": "0 o 5."}],
"glosario": [{"palabra": "Regularidad", "significado": "Algo que se repite."}, {"palabra": "Doble", "significado": "Dos veces lo mismo."}],
"carpeta": ["Si 3 × 7 = 21, ¿cuánto es 6 × 7?", "Si 3 × 7 = 21, ¿cuánto es 7 × 3?", "Sofi dice que 4 × 6 y 6 × 4 dan distinto. ¿Cuánto dan?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["42"], ["21"], ["24"]],
"soluciones": {"incompleto": "24. 18.", "solo": "En 5 o en 0.", "carpeta": ["42.", "21.", "24 las dos."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a aprender las tablas del 3, 4 y 6.",
"vas_a_ver": ["Tabla del 3", "Tabla del 4: doble del 2", "Tabla del 6: doble del 3"],
"secciones": [
 S(1, "Tabla del 3", [
  P("Va de 3 en 3: 3, 6, 9, 12, 15…"),
  P("Hasta 10 × 3 = <b>30</b>."),
  IMG("Tabla del 3", "De 3 en 3.", FG.tren_paso(3, 30, 3)),
 ]),
 S(1, "Dobles", [
  D("Truco del doble", "El doble de la del 2 es la <b>del 4</b>."),
  P("7 × 3 = 21, entonces 7 × 6 = 42."),
  IMG("Tabla del 6", "De 6 en 6.", FG.tren_paso(6, 60, 6)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Tablas", "Del 3, 4 y 6.", FG.cuentas([("8 × 4", 32), ("9 × 6", 54)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Truco", "planteo": "5 × 4.", "pasos": ["5 × 2 = 10.", "El doble: 20."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Usá el doble.", "pasos": ["4 × 3 = 12, entonces 4 × 6 = ___ .", "8 × 2 = 16, entonces 8 × 4 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 6 × 6?"},
"tip": {"titulo": "Doble", "texto": "Con la del 2 sale la del 4."},
"ojo": ["6 × 4 es 24, no 22.", "Controlá con el doble."],
"resumen": [{"titulo": "Del 3", "texto": "De 3 en 3."}, {"titulo": "Del 4", "texto": "Doble del 2."}, {"titulo": "Del 6", "texto": "Doble del 3."}],
"glosario": [{"palabra": "Tabla", "significado": "Resultados de multiplicar un número."}, {"palabra": "Truco", "significado": "Forma rápida de pensar."}],
"carpeta": ["¿Cuánto es 8 × 4?", "¿Cuánto es 9 × 6?", "Juan dice que 6 × 4 = 22. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["32"], ["54"], ["24"]],
"soluciones": {"incompleto": "24. 32.", "solo": "36.", "carpeta": ["32.", "54.", "24."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a aprender las tablas del 7, 8 y 9.",
"vas_a_ver": ["Tabla del 7", "Tabla del 8: doble del 4", "Tabla del 9: por 10 menos uno"],
"secciones": [
 S(1, "Tabla del 7", [
  P("Va de 7 en 7: 7, 14, 21, 28, 35…"),
  P("Hasta 10 × 7 = <b>70</b>."),
  IMG("Tabla del 7", "De 7 en 7.", FG.tren_paso(7, 70, 7)),
 ]),
 S(1, "Trucos", [
  D("Truco del 9", "Multiplicamos <b>por 10</b> y sacamos una vez el número."),
  P("6 × 9 = 60 − 6 = 54. Y la del 8 es el doble de la del 4."),
  IMG("Del 9", "Por 10 menos uno.", FG.cuentas([("6 × 10 − 6", 54), ("7 × 4 + 7 × 4", 56)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Tablas", "Del 7, 8 y 9.", FG.cuentas([("7 × 6", 42), ("8 × 8", 64), ("9 × 4", 36)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Truco del 9", "planteo": "3 × 9.", "pasos": ["3 × 10 = 30.", "30 − 3 = 27."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Usá los trucos.", "pasos": ["5 × 9 = 50 − 5 = ___ .", "6 × 8 = 24 + 24 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 7 × 7?"},
"tip": {"titulo": "Truco del 9", "texto": "Por 10 y le sacás el número."},
"ojo": ["6 × 9 no es 60.", "Si dudás, contá desde uno que sepas."],
"resumen": [{"titulo": "Del 7", "texto": "De 7 en 7."}, {"titulo": "Del 8", "texto": "Doble del 4."}, {"titulo": "Del 9", "texto": "×10 menos uno."}],
"glosario": [{"palabra": "Multiplicar", "significado": "Sumar grupos iguales."}, {"palabra": "Resultado", "significado": "Lo que da la cuenta."}],
"carpeta": ["¿Cuánto es 7 × 6?", "¿Cuánto es 8 × 8?", "Mía dice que 9 × 4 = 40. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["42"], ["64"], ["36"]],
"soluciones": {"incompleto": "45. 48.", "solo": "49.", "carpeta": ["42.", "64.", "36: 40 − 4."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("FILA POR COLUMNA", [LD("EL CRUCE", "CADA CASILLERO GUARDA SU <b>FILA</b> POR SU <b>COLUMNA</b>."),
   LL("SEGUIMOS LA FILA CON UN DEDO.", "Y LA COLUMNA CON OTRO.")],
   {"modo": "pitagorica"}, {"modo": "pitagorica"}),
], "recuerda": [
 RC("TABLA PITAGÓRICA", "UN CUADRO QUE TIENE TODAS LAS TABLAS JUNTAS.", "LA FILA DEL 3 ES 3, 6, 9, 12…"),
 RC("EL CRUCE", "DONDE SE CRUZAN FILA Y COLUMNA ESTÁ SU MULTIPLICACIÓN.", "FILA 5 Y COLUMNA 6: 30"),
]}
N2["leccion"] = {"temas": [
 T("SECRETOS DE LA TABLA", [LD("REGULARIDADES", "ALGUNAS FILAS SON EL <b>DOBLE</b> DE OTRAS."),
   LL("FILA Y COLUMNA DE UN NÚMERO SON IGUALES.", "DAR VUELTA LA CUENTA NO CAMBIA NADA.")],
   {"modo": "pitagorica", "que": "regular"}, {"modo": "pitagorica", "que": "regular"}),
], "recuerda": [
 RC("DOBLE", "LA FILA DEL 4 ES EL DOBLE DE LA FILA DEL 2.", "2 × 6 = 12 Y 4 × 6 = 24"),
 RC("ESPEJO", "EL ORDEN DE LOS NÚMEROS NO CAMBIA EL RESULTADO.", "8 × 3 = 3 × 8 = 24"),
]}
N3["leccion"] = {"temas": [
 T("TABLAS DEL 3, DEL 4 Y DEL 6", [LD("USAR EL DOBLE", "LA DEL 4 SALE <b>DUPLICANDO</b> LA DEL 2."),
   LL("LA DEL 6 SALE DUPLICANDO LA DEL 3.", "LA DEL 3 SUBE DE A TRES.")],
   {"modo": "pitagorica", "que": "tabla", "min": 3, "max": 6}, {"modo": "pitagorica", "que": "tabla", "solo": [3, 4, 6]}),
], "recuerda": [
 RC("DEL 4", "SE CALCULA HACIENDO EL DOBLE DE LA TABLA DEL 2.", "5 × 2 = 10, ENTONCES 5 × 4 = 20"),
 RC("DEL 6", "SE CALCULA HACIENDO EL DOBLE DE LA TABLA DEL 3.", "4 × 3 = 12, ENTONCES 4 × 6 = 24"),
]}
N4["leccion"] = {"temas": [
 T("TABLAS DEL 7, DEL 8 Y DEL 9", [LD("ATAJOS", "PARA EL 8 USAMOS UN <b>DOBLE</b>; PARA EL 9, UNA DECENA ENTERA."),
   LL("OCHO VECES ES DUPLICAR CUATRO VECES.", "NUEVE VECES ES DIEZ VECES, QUITANDO UNA.", "EL SIETE SE CUENTA DESDE UNO CONOCIDO.")],
   {"modo": "pitagorica", "que": "tabla", "min": 7, "max": 9}, {"modo": "pitagorica", "que": "tabla", "solo": [7, 8, 9]}),
], "recuerda": [
 RC("DEL 9", "MULTIPLICAMOS POR 10 Y DESPUÉS LE SACAMOS EL NÚMERO.", "3 × 9 = 30 − 3 = 27"),
 RC("DEL 8", "SE CALCULA HACIENDO EL DOBLE DE LA TABLA DEL 4.", "6 × 4 = 24, ENTONCES 6 × 8 = 48"),
]}

ACT = {
"1": [N("¿QUÉ VA EN FILA 5, COLUMNA 6?", 30, "5 × 6.", n="aplicar"),
      FB("FILA 7, COLUMNA 3: 7 × 3 = ___", [["21"]], "7 × 3.", n="aplicar"),
      MC("LEO PUSO 11 EN FILA 4, COLUMNA 7. ¿QUÉ VA?", ["28", "11", "47"], "28", "SE MULTIPLICA.", n="error"),
      UNIR("UNÍ CADA CRUCE CON SU NÚMERO.", ["FILA 2 · COL 9", "FILA 3 · COL 6", "FILA 4 · COL 5"], ["20", "18 ", "18"], {"FILA 2 · COL 9": "18", "FILA 3 · COL 6": "18 ", "FILA 4 · COL 5": "20"}, "FILA POR COLUMNA.", n="analizar")],
"2": [N("SI 2 × 6 = 12, ¿CUÁNTO ES 4 × 6?", 24, "EL DOBLE.", n="aplicar"),
      ORD("ORDENÁ DE MENOR A MAYOR.", ["3 × 8", "2 × 5", "6 × 6"], ["2 × 5", "3 × 8", "6 × 6"], "10, 24 Y 36.", n="aplicar"),
      MC("SOFI DICE QUE 4 × 6 Y 6 × 4 DAN DISTINTO. ¿QUÉ PASA?", ["DAN IGUAL: 24", "DAN DISTINTO"], "DAN IGUAL: 24", "LA TABLA ES UN ESPEJO.", n="error"),
      CLAS("¿ESTÁ EN LA FILA DEL 5?", ["15", "22", "40", "33"], ["SÍ", "NO"], {"15": "SÍ", "22": "NO", "40": "SÍ", "33": "NO"}, "TERMINAN EN 0 O 5.", n="analizar")],
"3": [FB("8 × 2 = 16, ENTONCES 8 × 4 = ___", [["32"]], "EL DOBLE DE 16.", n="aplicar"),
      N("¿CUÁNTO ES 9 × 6?", 54, "EL DOBLE DE 27.", n="aplicar"),
      MC("JUAN DICE QUE 6 × 4 = 22. ¿CUÁNTO ES?", ["24", "22", "10"], "24", "EL DOBLE DE 12.", n="error"),
      N("[[problema]] HAY 6 COFRES CON 4 MONEDAS. ¿CUÁNTAS MONEDAS?", 24, "6 × 4.", n="analizar")],
"4": [N("¿CUÁNTO ES 7 × 6?", 42, "DE 7 EN 7.", n="aplicar"),
      MC("¿CUÁNTO ES 5 × 9?", ["45", "50", "59"], "45", "50 − 5.", n="aplicar"),
      MC("MÍA DICE QUE 9 × 4 = 40. ¿CUÁNTO ES?", ["36", "40", "13"], "36", "40 − 4.", n="error"),
      UNIR("UNÍ CADA CUENTA CON SU TRUCO.", ["6 × 9", "6 × 8", "6 × 7"], ["DE 7 EN 7", "60 − 6", "24 + 24"], {"6 × 9": "60 − 6", "6 × 8": "24 + 24", "6 × 7": "DE 7 EN 7"}, "CADA TABLA TIENE SU TRUCO.", n="analizar")],
"5": [N("RELÁMPAGO. 4 × 7 = ___", 28, "28.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 9 × 9 = ___", 81, "90 − 9.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. 6 × 3 = ___", ["18", "9"], "18", "18.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. 3 × 8 ES IGUAL A…", ["8 × 3", "3 + 8"], "8 × 3", "ESPEJO.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿QUÉ VA EN FILA 3, COLUMNA 8?", 24, "3 × 8.", n="aplicar")],
 [1, N("¿QUÉ VA EN FILA 9, COLUMNA 2?", 18, "9 × 2.", n="aplicar")],
 [1, TF("EN LA TABLA PITAGÓRICA SE SUMA FILA MÁS COLUMNA.", "FALSO", "SE MULTIPLICA.", n="error")],
 [2, N("SI 3 × 7 = 21, ¿CUÁNTO ES 6 × 7?", 42, "EL DOBLE.", n="analizar")],
 [2, MC("¿CÓMO TERMINAN LOS NÚMEROS DE LA FILA DEL 5?", ["EN 0 O EN 5", "EN 1", "EN 3"], "EN 0 O EN 5", "5, 10, 15, 20…", n="recordar")],
 [2, N("SI 9 × 2 = 18, ¿CUÁNTO ES 2 × 9?", 18, "EL ORDEN NO CAMBIA.", n="aplicar")],
 [3, N("¿CUÁNTO ES 6 × 6?", 36, "EL DOBLE DE 18.", n="aplicar")],
 [3, FB("7 × 2 = 14, ENTONCES 7 × 4 = ___", [["28"]], "EL DOBLE DE 14.", n="aplicar")],
 [3, MC("¿QUÉ TABLA ES EL DOBLE DE LA DEL 3?", ["LA DEL 6", "LA DEL 5", "LA DEL 9"], "LA DEL 6", "3 × 2 = 6.", n="analizar")],
 [4, N("¿CUÁNTO ES 8 × 7?", 56, "28 + 28.", n="aplicar")],
 [4, MC("¿CUÁNTO ES 7 × 9?", ["63", "70", "79"], "63", "70 − 7.", n="aplicar")],
 [4, MC("NICO DICE QUE 6 × 9 = 60. ¿CUÁNTO ES?", ["54", "60", "15"], "54", "60 − 6.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 10, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: la tabla pitagórica", "examen_titulo": "Nivel jefe: la tabla pitagórica",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
