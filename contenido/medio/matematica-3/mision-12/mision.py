# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 12 · Multiplicación por una cifra. Genera mision-12.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la huerta de Nina.
Niveles: 1 descomponiendo · 2 en columnas · 3 con reagrupamiento · 4 controlar estimando."""
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
"objetivo": "Vas a multiplicar desarmando el número.",
"vas_a_ver": ["Desarmar en decenas y unidades", "Multiplicar cada parte", "Sumar las partes"],
"secciones": [
 S(1, "Cajones de plantines", [
  P("Nina tiene 4 cajones con 23 plantines."),
  P("23 = 20 + 3. 4 × 20 = 80 y 4 × 3 = 12. Son <b>92</b>."),
  IMG("4 × 23", "Dos partes.", FG.cuentas([("4 × 20", 80), ("4 × 3", 12), ("80 + 12", 92)])),
 ]),
 S(1, "Descomponer", [
  D("Multiplicar descomponiendo", "Desarmamos el número, <b>multiplicamos cada parte</b> y sumamos."),
  P("3 × 14 = 30 + 12 = 42."),
  IMG("3 × 14", "Dos partes.", FG.cuentas([("3 × 10", 30), ("3 × 4", 12)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas", "Desarmá y multiplicá.", FG.cuentas([("5 × 21", 105), ("6 × 13", 78)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Descomponer", "planteo": "2 × 34.", "pasos": ["2 × 30 = 60. 2 × 4 = 8.", "60 + 8 = 68."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "3 × 25.", "pasos": ["3 × 20 = ___ . 3 × 5 = ___ .", "Total: ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 4 × 16?"},
"tip": {"titulo": "Dos partes", "texto": "No te olvides de ninguna parte."},
"ojo": ["4 × 23 no es solo 4 × 20.", "Sumá las dos partes."],
"resumen": [{"titulo": "Desarmar", "texto": "Decenas y unidades."}, {"titulo": "Multiplicar", "texto": "Cada parte."}, {"titulo": "Sumar", "texto": "Las partes."}],
"glosario": [{"palabra": "Descomponer", "significado": "Desarmar en partes."}, {"palabra": "Parte", "significado": "Un pedazo del número."}],
"carpeta": ["¿Cuánto es 5 × 21?", "¿Cuánto es 6 × 13?", "Leo hizo 4 × 23 = 80. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["105"], ["78"], ["92"]],
"soluciones": {"incompleto": "60. 15. 75.", "solo": "64.", "carpeta": ["105.", "78.", "92."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a multiplicar en columnas.",
"vas_a_ver": ["El número chico abajo", "Empezar por las unidades", "Todas las cifras"],
"secciones": [
 S(1, "Canteros de lechuga", [
  P("3 canteros de 32 lechugas."),
  P("3 × 2 = 6 y 3 × 3 = 9. Son <b>96</b>."),
  IMG("32 × 3", "En columnas.", FG.cuentas([("unidades: 3 × 2", 6), ("decenas: 3 × 3", 9)])),
 ]),
 S(1, "En columnas", [
  D("Multiplicar en columnas", "El número de abajo multiplica a <b>cada cifra</b> de arriba."),
  P("Empezamos por las unidades."),
  IMG("21 × 4", "Cada cifra.", FG.cuentas([("4 × 1", 4), ("4 × 2", 8), ("21 × 4", 84)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas", "En columnas.", FG.cuentas([("13 × 3", 39), ("42 × 2", 84)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Columnas", "planteo": "34 × 2.", "pasos": ["Unidades: 8. Decenas: 6.", "Da 68."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "22 × 3.", "pasos": ["Unidades: ___ .", "Decenas: ___ . Da 66."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 11 × 7?"},
"tip": {"titulo": "Derecha", "texto": "Empezá siempre por la derecha."},
"ojo": ["Multiplicá todas las cifras.", "El chico va abajo."],
"resumen": [{"titulo": "Abajo", "texto": "El chico."}, {"titulo": "Empezar", "texto": "Unidades."}, {"titulo": "Todas", "texto": "Las cifras."}],
"glosario": [{"palabra": "Cifra", "significado": "Cada número del 0 al 9."}, {"palabra": "Columna", "significado": "Fila hacia abajo."}],
"carpeta": ["¿Cuánto es 13 × 3?", "¿Cuánto es 42 × 2?", "Mía multiplicó solo las unidades de 32 × 3 y le dio 36. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["39"], ["84"], ["96"]],
"soluciones": {"incompleto": "6. 6.", "solo": "77.", "carpeta": ["39.", "84.", "96."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a multiplicar llevándote.",
"vas_a_ver": ["Cuando pasa de 9", "Anotar lo que me llevo", "Sumar después"],
"secciones": [
 S(1, "Bandejas de semillas", [
  P("4 bandejas de 47 semillas."),
  P("7 × 4 = 28: escribo 8 y me llevo 2. 4 × 4 = 16, más 2: 18. Son <b>188</b>."),
  IMG("47 × 4", "Me llevo 2.", FG.cuentas([("7 × 4", 28), ("4 × 4 + 2", 18), ("47 × 4", 188)])),
 ]),
 S(1, "Reagrupar", [
  D("Me llevo", "Si da <b>10 o más</b>, escribimos las unidades y llevamos las decenas."),
  P("Lo que llevamos se suma después de multiplicar."),
  IMG("25 × 3", "Me llevo 1.", FG.cuentas([("5 × 3", 15), ("2 × 3 + 1", 7), ("25 × 3", 75)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas", "Con reagrupamiento.", FG.cuentas([("36 × 2", 72), ("18 × 5", 90)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Me llevo", "planteo": "16 × 4.", "pasos": ["6 × 4 = 24: escribo 4, me llevo 2.", "1 × 4 + 2 = 6. Da 64."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "29 × 3.", "pasos": ["9 × 3 = 27: escribo ___ , me llevo 2.", "2 × 3 + 2 = ___ . Da 87."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 58 × 2?"},
"tip": {"titulo": "Anotá", "texto": "Escribí chiquito lo que te llevás."},
"ojo": ["Sumá lo que te llevás.", "47 × 4 no es 168."],
"resumen": [{"titulo": "Pasa de 9", "texto": "Me llevo."}, {"titulo": "Anoto", "texto": "Arriba."}, {"titulo": "Sumo", "texto": "Después."}],
"glosario": [{"palabra": "Reagrupar", "significado": "Juntar diez en uno."}, {"palabra": "Llevarse", "significado": "Pasar al lugar de al lado."}],
"carpeta": ["¿Cuánto es 36 × 2?", "¿Cuánto es 18 × 5?", "Juan hizo 47 × 4 = 168. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["72"], ["90"], ["188"]],
"soluciones": {"incompleto": "7. 8.", "solo": "116.", "carpeta": ["72.", "90.", "188."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a controlar multiplicaciones estimando.",
"vas_a_ver": ["Redondear a la decena", "Estimar", "Comparar"],
"secciones": [
 S(1, "¿Puede ser?", [
  P("Nina calculó 38 × 6 = 2.280."),
  P("40 × 6 = 240: tiene que dar <b>cerca de 240</b>."),
  IMG("Estimar", "38 está cerca de 40.", FG.cuentas([("40 × 6", 240), ("exacto", 228)])),
 ]),
 S(1, "Controlar", [
  D("Estimar", "Redondeamos a la <b>decena</b> y multiplicamos de memoria."),
  P("Si da muy lejos, hay un error."),
  IMG("Más estimaciones", "Cerca.", FG.cuentas([("19 × 5", "≈ 100"), ("31 × 4", "≈ 120")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("¿Puede ser?", "Estimá.", FG.cuentas([("52 × 3", "?"), ("29 × 4", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Estimar", "planteo": "21 × 6.", "pasos": ["20 × 6 = 120.", "Cerca de 120."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Redondeá.", "pasos": ["49 × 2: 50 × 2 = ___ .", "Cerca de ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿67 × 3 da cerca de 210 o de 2.100?"},
"tip": {"titulo": "Redondo", "texto": "Usá la decena más cercana."},
"ojo": ["38 × 6 no puede dar 2.280.", "Estimar no es la cuenta exacta."],
"resumen": [{"titulo": "Redondear", "texto": "A la decena."}, {"titulo": "Estimar", "texto": "Antes."}, {"titulo": "Comparar", "texto": "Después."}],
"glosario": [{"palabra": "Estimar", "significado": "Calcular más o menos."}, {"palabra": "Decena", "significado": "Grupo de diez."}],
"carpeta": ["¿52 × 3 da cerca de qué número?", "¿29 × 4 da cerca de qué número?", "Sofi dice que 38 × 6 = 2.280. ¿Cerca de cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["150"], ["120"], ["240"]],
"soluciones": {"incompleto": "100. 100.", "solo": "210.", "carpeta": ["150.", "120.", "240."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("MULTIPLICAR POR PARTES", [LD("PARTIR", "SEPARAMOS EL NÚMERO EN <b>DECENAS Y UNIDADES</b>; CADA PARTE SE MULTIPLICA."),
   LL("AL FINAL JUNTAMOS LOS DOS RESULTADOS.", "NINGUNA PARTE SE PUEDE OLVIDAR.")],
   {"modo": "mult1"}, {"modo": "mult1"}),
], "recuerda": [
 RC("DESCOMPONER", "PARTIMOS EL NÚMERO Y MULTIPLICAMOS CADA PARTE.", "2 × 34 = 60 + 8 = 68"),
 RC("SUMAR LAS PARTES", "JUNTAMOS LOS RESULTADOS DE CADA PARTE.", "3 × 25 = 60 + 15 = 75"),
]}
N2["leccion"] = {"temas": [
 T("EN COLUMNAS", [LD("UNA POR UNA", "EL MULTIPLICADOR CHICO <b>RECORRE</b> LAS CIFRAS DEL NÚMERO GRANDE."),
   LL("PRIMERO LA CIFRA DE LA DERECHA.", "CADA RESULTADO QUEDA DEBAJO DE SU CIFRA.")],
   {"modo": "mult1", "que": "columna"}, {"modo": "mult1", "que": "columna"}),
], "recuerda": [
 RC("EN COLUMNAS", "MULTIPLICAMOS CADA CIFRA EMPEZANDO POR LAS UNIDADES.", "34 × 2 = 68"),
 RC("ABAJO", "EL NÚMERO DE UNA CIFRA VA DEBAJO DE LAS UNIDADES.", "22 × 3: EL 3 DEBAJO DEL 2 DE LA DERECHA"),
]}
N3["leccion"] = {"temas": [
 T("ME LLEVO AL MULTIPLICAR", [LD("REAGRUPAR", "SI UNA COLUMNA DA <b>10 O MÁS</b>, LAS DECENAS PASAN AL LADO."),
   LL("LAS ANOTAMOS ARRIBA, CHIQUITO.", "SE SUMAN DESPUÉS DE MULTIPLICAR.")],
   {"modo": "mult1", "que": "lleva"}, {"modo": "mult1", "que": "lleva"}),
], "recuerda": [
 RC("ME LLEVO", "ESCRIBIMOS LAS UNIDADES Y PASAMOS LAS DECENAS AL LADO.", "16 × 4: 24, ESCRIBO 4 Y ME LLEVO 2"),
 RC("SUMAR DESPUÉS", "LO QUE NOS LLEVAMOS SE SUMA DESPUÉS DE MULTIPLICAR.", "1 × 4 + 2 = 6: DA 64"),
]}
N4["leccion"] = {"temas": [
 T("¿TIENE SENTIDO?", [LD("CONTROLAR", "CAMBIAMOS EL NÚMERO POR SU <b>DECENA CERCANA</b> Y MULTIPLICAMOS DE MEMORIA."),
   LL("LA CUENTA EXACTA TIENE QUE QUEDAR CERCA.", "SI QUEDA MUY LEJOS, LA REVISAMOS.")],
   {"modo": "mult1", "que": "estimar"}, {"modo": "mult1", "que": "estimar"}),
], "recuerda": [
 RC("ESTIMAR", "REDONDEAMOS A LA DECENA Y MULTIPLICAMOS DE MEMORIA.", "21 × 6: 20 × 6 = 120"),
 RC("CONTROLAR", "SI LA CUENTA DA MUY LEJOS DE LO ESTIMADO, HAY UN ERROR.", "47 × 5 NO PUEDE DAR 2.350"),
]}

ACT = {
"1": [N("¿CUÁNTO ES 2 × 34?", 68, "60 + 8.", n="aplicar"),
      FB("COMPLETÁ: 3 × 25 = 60 + ___", [["15"]], "3 × 5.", n="aplicar"),
      MC("LEO HIZO 4 × 23 = 80. ¿CUÁNTO ES?", ["92", "80", "27"], "92", "FALTA 4 × 3.", n="error"),
      UNIR("UNÍ CADA CUENTA CON SUS PARTES.", ["4 × 16", "5 × 12", "2 × 47"], ["80 + 14", "40 + 24", "50 + 10"], {"4 × 16": "40 + 24", "5 × 12": "50 + 10", "2 × 47": "80 + 14"}, "DECENAS Y UNIDADES.", n="analizar")],
"2": [N("¿CUÁNTO ES 34 × 2?", 68, "8 Y 6.", n="aplicar"),
      N("¿CUÁNTO ES 11 × 7?", 77, "7 Y 7.", n="aplicar"),
      MC("MÍA MULTIPLICÓ SOLO LAS UNIDADES DE 32 × 3 Y LE DIO 36. ¿CUÁNTO ES?", ["96", "36", "35"], "96", "TODAS LAS CIFRAS.", n="error"),
      ORD("ORDENÁ LOS PASOS DE 22 × 3.", ["3 × 2 DECENAS = 6", "3 × 2 UNIDADES = 6", "DA 66"], ["3 × 2 UNIDADES = 6", "3 × 2 DECENAS = 6", "DA 66"], "PRIMERO LAS UNIDADES.", n="analizar")],
"3": [N("¿CUÁNTO ES 16 × 4?", 64, "ME LLEVO 2.", n="aplicar"),
      N("¿CUÁNTO ES 58 × 2?", 116, "ME LLEVO 1.", n="aplicar"),
      MC("JUAN HIZO 47 × 4 = 168. ¿CUÁNTO ES?", ["188", "168", "1.628"], "188", "SUMÁ EL 2 QUE TE LLEVÁS.", n="error"),
      MC("EN 25 × 3, ¿QUÉ PASA EN LAS UNIDADES?", ["ESCRIBO 5 Y ME LLEVO 1", "ESCRIBO 15 Y NO LLEVO", "ESCRIBO 1 Y ME LLEVO 5"], "ESCRIBO 5 Y ME LLEVO 1", "PASA DE 9.", n="analizar")],
"4": [MC("21 × 6 DA CERCA DE…", ["120", "1.200", "27"], "120", "20 × 6.", n="aplicar"),
      MC("¿67 × 3 DA CERCA DE 210 O DE 2.100?", ["210", "2.100"], "210", "70 × 3.", n="aplicar"),
      MC("SOFI DICE QUE 38 × 6 = 2.280. ¿PUEDE SER?", ["NO: DA CERCA DE 240", "SÍ"], "NO: DA CERCA DE 240", "40 × 6 = 240.", n="error"),
      CLAS("¿PUEDE SER EL RESULTADO?", ["19 × 5 = 95", "31 × 4 = 1.240", "52 × 3 = 156", "29 × 4 = 16"], ["PUEDE SER", "NO PUEDE SER"],
           {"19 × 5 = 95": "PUEDE SER", "31 × 4 = 1.240": "NO PUEDE SER", "52 × 3 = 156": "PUEDE SER", "29 × 4 = 16": "NO PUEDE SER"}, "ESTIMÁ CADA UNA.", n="analizar")],
"5": [N("RELÁMPAGO. 3 × 14 = ___", 42, "30 + 12.", tiempo=40, n="aplicar"),
      N("RELÁMPAGO. 21 × 4 = ___", 84, "84.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 25 × 3 = ___", 75, "75.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. ¿EMPEZAMOS POR…?", ["LAS UNIDADES", "LAS DECENAS"], "LAS UNIDADES", "DE DERECHA A IZQUIERDA.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 5 × 21?", 105, "100 + 5.", n="aplicar")],
 [1, FB("COMPLETÁ: 6 × 13 = 60 + ___", [["18"]], "6 × 3.", n="aplicar")],
 [1, TF("PARA 4 × 23 ALCANZA CON 4 × 20.", "FALSO", "FALTA 4 × 3.", n="error")],
 [2, N("¿CUÁNTO ES 13 × 3?", 39, "9 Y 3.", n="aplicar")],
 [2, N("¿CUÁNTO ES 42 × 2?", 84, "4 Y 8.", n="aplicar")],
 [2, MC("EN COLUMNAS, ¿DÓNDE VA EL NÚMERO DE UNA CIFRA?", ["DEBAJO DE LAS UNIDADES", "ARRIBA", "AL COSTADO"], "DEBAJO DE LAS UNIDADES", "ABAJO A LA DERECHA.", n="recordar")],
 [3, N("¿CUÁNTO ES 36 × 2?", 72, "ME LLEVO 1.", n="aplicar")],
 [3, N("[[problema]] NINA TIENE 5 BANDEJAS DE 18 SEMILLAS. ¿CUÁNTAS SEMILLAS?", 90, "18 × 5.", n="analizar")],
 [3, MC("29 × 3: 9 × 3 = 27. ¿QUÉ ESCRIBO?", ["7 Y ME LLEVO 2", "27", "2 Y ME LLEVO 7"], "7 Y ME LLEVO 2", "LAS DECENAS PASAN AL LADO.", n="analizar")],
 [4, MC("49 × 2 DA CERCA DE…", ["100", "1.000", "51"], "100", "50 × 2.", n="aplicar")],
 [4, MC("52 × 3 DA CERCA DE…", ["150", "1.500", "55"], "150", "50 × 3.", n="aplicar")],
 [4, MC("NICO DICE QUE 31 × 4 = 1.240. ¿PUEDE SER?", ["NO: DA CERCA DE 120", "SÍ"], "NO: DA CERCA DE 120", "30 × 4 = 120.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 12, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: multiplicación por una cifra", "examen_titulo": "Nivel jefe: multiplicación por una cifra",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-12.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
