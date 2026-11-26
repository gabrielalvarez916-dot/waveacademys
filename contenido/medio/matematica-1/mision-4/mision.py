# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 4 · Los números hasta 100. Genera mision-4.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el álbum nuevo de Tomi, de 100 figuritas (igual que clases.py)."""
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

N1 = {**ESTILO,
"objetivo": "Vas a contar del 1 al 100.",
"vas_a_ver": ["Los números redondos hasta 100", "Contar los del sesenta y los del noventa", "Después de un 9 viene un redondo"],
"secciones": [
 S(1, "Los redondos", [
  P("El álbum nuevo de Tomi tiene <b>100 figuritas</b>."),
  P("Los números redondos son: <b>10, 20, 30… 100</b>."),
  IMG("Los redondos", "Del 10 al 100, de 10 en 10.", FG.tren_paso(10, 100, 10)),
 ]),
 S(1, "Después del 9", [
  D("Después de un 9", "Después de un número que termina en 9 viene un <b>redondo</b>: 69, 70."),
  IMG("Los del sesenta", "Del 61 al 70.", FG.tren(61, 70)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("El último tramo", "Del 91 al 100.", FG.tren(91, 100, (93, 99))),
 ]),
],
"ejemplo_completo": {"titulo": "Contar desde el 77", "planteo": "Tomi cuenta desde el 77.", "pasos": ["77, 78, 79.", "Después del 79 viene el 80.", "80, 81, 82."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí los que faltan.", "pasos": ["58, ___ , 60, 61.", "98, 99, ___ ."]},
"ejemplo_solo": {"titulo": "Los redondos", "planteo": "Decí en voz alta los redondos del 10 al 100."},
"tip": {"titulo": "Mirá el 9", "texto": "Después de un 9 viene un redondo."},
"ojo": ["Después del 79 viene el 80, no el 70.", "Después del 99 viene el 100."],
"resumen": [{"titulo": "Hasta 100", "texto": "En orden."}, {"titulo": "Redondos", "texto": "10, 20, 30…"}, {"titulo": "Después del 9", "texto": "Viene un redondo."}],
"glosario": [{"palabra": "Cien", "significado": "El número 100."}, {"palabra": "Redondo", "significado": "Número que termina en 0."}],
"carpeta": ["¿Qué número falta en el primer vagón vacío?", "¿Qué número falta en el segundo vagón vacío?", "¿Qué número viene después del 79?"],
"respuestas_carpeta": [["93"], ["99"], ["80"]],
"soluciones": {"incompleto": "59. 100.", "solo": "10, 20, 30, 40, 50, 60, 70, 80, 90, 100.", "carpeta": ["93.", "99.", "80."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer la tabla de cien y encontrar números en ella.",
"vas_a_ver": ["La tabla de cien", "Filas y columnas", "La primera cifra te dice la fila"],
"secciones": [
 S(1, "La tabla de cien", [
  P("Tomi pegó todas sus figuritas. Quedó una <b>tabla de cien</b>."),
  IMG("La tabla de cien", "Diez filas de diez números.", FG.cuadro(99, desde=0)),
 ]),
 S(1, "Filas y columnas", [
  D("Fila y columna", "Una <b>fila</b> va de costado. Una <b>columna</b> va para abajo."),
  P("El 57 está en la fila del cincuenta."),
  IMG("El 57", "Fila del cincuenta.", FG.cuadro(99, resaltar=(57,), desde=0)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla. La vas a usar en la carpeta."),
  IMG("La fila del 80", "Pintada en amarillo.", FG.cuadro(99, resaltar=range(80, 90), desde=0)),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar el 34", "planteo": "¿Dónde está el 34?", "pasos": ["Empieza con 3.", "Está en la fila del treinta.", "Es el cuarto de esa fila."]},
"ejemplo_incompleto": {"titulo": "Buscar el 72", "planteo": "Completá.", "pasos": ["Empieza con ___ .", "Está en la fila del ___ ."]},
"ejemplo_solo": {"titulo": "El 90", "planteo": "¿En qué fila está el 90?"},
"tip": {"titulo": "Mirá la primera cifra", "texto": "Te dice en qué fila buscar."},
"ojo": ["El 90 empieza la fila del noventa.", "Fila es de costado; columna, para abajo."],
"resumen": [{"titulo": "Tabla", "texto": "100 números."}, {"titulo": "Fila", "texto": "De costado."}, {"titulo": "Columna", "texto": "Para abajo."}],
"glosario": [{"palabra": "Tabla de cien", "significado": "Los números del 0 al 99 en filas de 10."}, {"palabra": "Fila", "significado": "Números de costado."}],
"carpeta": ["¿Con qué número empieza la fila pintada?", "¿Con qué número termina la fila pintada?", "¿En qué fila está el 34: la del 30 o la del 40?"],
"respuestas_carpeta": [["80"], ["89"], ["30", "la del 30", "del 30", "treinta"]],
"soluciones": {"incompleto": "7. Setenta.", "solo": "En la fila del noventa.", "carpeta": ["80.", "89.", "La del 30."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a descubrir los secretos de la tabla de cien.",
"vas_a_ver": ["Las columnas terminan igual", "Las filas empiezan igual", "Bajar una fila es sumar 10"],
"secciones": [
 S(1, "Columnas y filas", [
  D("Columnas", "En una columna, todos <b>terminan igual</b>: 3, 13, 23…"),
  IMG("La columna del 3", "Todos terminan en 3.", FG.cuadro(99, resaltar=range(3, 100, 10), desde=0)),
  D("Filas", "En una fila, todos <b>empiezan igual</b>: 41, 42, 43…"),
 ]),
 S(1, "Abajo suma 10", [
  P("Debajo del 45 está el <b>55</b>. Bajar una fila es <b>sumar 10</b>."),
  IMG("45 y 55", "Uno arriba del otro.", FG.cuadro(99, resaltar=(45, 55), desde=0)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla. La vas a usar en la carpeta."),
  IMG("Figuritas perdidas", "Completá los que faltan.", FG.cuadro(99, faltan=(36, 64, 88), desde=0)),
 ]),
],
"ejemplo_completo": {"titulo": "Debajo del 62", "planteo": "¿Qué número va debajo del 62?", "pasos": ["Bajar una fila es sumar 10.", "62 + 10 = 72.", "Debajo del 62 va el 72."]},
"ejemplo_incompleto": {"titulo": "La columna del 8", "planteo": "Completá.", "pasos": ["8, 18, 28, ___ , 48.", "Todos terminan en ___ ."]},
"ejemplo_solo": {"titulo": "Arriba del 50", "planteo": "¿Qué número va arriba del 50?"},
"tip": {"titulo": "Usá los secretos", "texto": "Fila y columna te dicen dónde va cada número."},
"ojo": ["Debajo del 45 no va el 46: va el 55.", "En una columna todos terminan igual."],
"resumen": [{"titulo": "Filas", "texto": "Empiezan igual."}, {"titulo": "Columnas", "texto": "Terminan igual."}, {"titulo": "Abajo", "texto": "Suma 10."}],
"glosario": [{"palabra": "Regularidad", "significado": "Algo que se repite siempre igual."}, {"palabra": "Columna", "significado": "Números para abajo."}],
"carpeta": ["¿Qué número falta en la fila del 30?", "¿Qué número falta en la fila del 60?", "¿Qué número falta en la fila del 80?"],
"respuestas_carpeta": [["36"], ["64"], ["88"]],
"soluciones": {"incompleto": "38. 8.", "solo": "El 40.", "carpeta": ["36.", "64.", "88."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a contar de a 2, 5 y 10.",
"vas_a_ver": ["Contar de a 2", "Contar de a 5", "Contar de a 10"],
"secciones": [
 S(1, "De a 2", [
  P("Tomi cuenta medias de a pares: <b>2, 4, 6, 8…</b>"),
  IMG("De a 2", "Del 2 al 20.", FG.tren_paso(2, 20, 2)),
 ]),
 S(1, "De a 5 y de a 10", [
  D("De a 5", "5, 10, 15, 20… Terminan en <b>5</b> o en <b>0</b>."),
  IMG("De a 5", "Del 5 al 50.", FG.tren_paso(5, 50, 5)),
  D("De a 10", "10, 20, 30… ¡El más rápido!"),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("¿Qué vagones faltan?", "Contá de a 5.", FG.tren_paso(5, 50, 5, (25, 40))),
 ]),
],
"ejemplo_completo": {"titulo": "Medias", "planteo": "Hay 6 pares de medias. ¿Cuántas medias son?", "pasos": ["Contamos de a 2.", "2, 4, 6, 8, 10, 12.", "Son 12 medias."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí el que sigue.", "pasos": ["2, 4, 6, ___ .", "10, 20, 30, ___ ."]},
"ejemplo_solo": {"titulo": "Manos", "planteo": "¿Cuántos dedos hay en 3 manos? Contá de a 5."},
"tip": {"titulo": "Elegí el salto", "texto": "De a 10 es el más rápido."},
"ojo": ["De a 2 no se dice 3: 2, 4, 6.", "De a 5 terminan en 5 o en 0."],
"resumen": [{"titulo": "De a 2", "texto": "2, 4, 6…"}, {"titulo": "De a 5", "texto": "5, 10, 15…"}, {"titulo": "De a 10", "texto": "10, 20, 30…"}],
"glosario": [{"palabra": "Par", "significado": "Dos cosas juntas."}, {"palabra": "Saltar", "significado": "Contar sin decir todos los números."}],
"carpeta": ["¿Qué número falta en el primer vagón vacío?", "¿Qué número falta en el segundo vagón vacío?", "¿Qué sigue? 10, 20, 30, ___"],
"respuestas_carpeta": [["25"], ["40"], ["40"]],
"soluciones": {"incompleto": "8. 40.", "solo": "15: 5, 10, 15.", "carpeta": ["25.", "40.", "40."]},
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
 T("LOS NÚMEROS REDONDOS", [LD("REDONDOS", "LOS NÚMEROS <b>REDONDOS</b> TERMINAN EN 0: 10, 20, 30… HASTA EL 100."),
   LL("60 SE LEE SESENTA.", "90 SE LEE NOVENTA.")],
   {"modo": "cuadro", "que": "contar", "hasta": 100}, {"modo": "redondos"}),
 T("DESPUÉS DE UN 9", [LD("EL 9 Y EL REDONDO", "CUANDO UN NÚMERO TERMINA EN 9, EL QUE SIGUE ES <b>REDONDO</b>."),
   LL("69 Y LUEGO 70.", "99 Y LUEGO 100: CIEN.")],
   {"modo": "tren", "desde": 57, "hasta": 71}, {"modo": "redondo", "max": 100}),
], "recuerda": [
 RC("REDONDOS", "SON LOS NÚMEROS QUE TERMINAN EN 0.", "50, 60, 70, 80, 90"),
 RC("DESPUÉS DE UN 9", "SIEMPRE VIENE UN NÚMERO REDONDO.", "89 Y DESPUÉS 90"),
]}

N2["leccion"] = {"temas": [
 T("LA TABLA DE CIEN", [LD("LA TABLA", "LA <b>TABLA DE CIEN</b> TIENE LOS NÚMEROS DEL 0 AL 100, DE A 10 POR FILA."),
   LL("LOS REDONDOS QUEDAN A LA IZQUIERDA.", "EL 100 QUEDA SOLO, ABAJO.")],
   {"modo": "cuadro", "que": "contar", "hasta": 100}, {"modo": "cuadro", "que": "falta", "hasta": 100}),
 T("LA PRIMERA CIFRA", [LD("LA FILA", "LA <b>PRIMERA CIFRA</b> DE UN NÚMERO TE DICE EN QUÉ FILA ESTÁ."),
   LL("EL 34 ESTÁ EN LA FILA DEL 30.", "EL 72 ESTÁ EN LA FILA DEL 70.")],
   {"modo": "cuadro", "que": "fila", "hasta": 100}, {"modo": "cuadro", "que": "fila", "hasta": 100}),
], "recuerda": [
 RC("LA TABLA DE CIEN", "TIENE LOS NÚMEROS DEL 0 AL 100 EN FILAS DE 10.", "LA FILA DEL 50: 50, 51… 59"),
 RC("LA PRIMERA CIFRA", "TE DICE EN QUÉ FILA BUSCAR EL NÚMERO.", "EL 86 ESTÁ EN LA FILA DEL 80"),
]}

N3["leccion"] = {"temas": [
 T("LAS COLUMNAS", [LD("UNA COLUMNA", "EN UNA <b>COLUMNA</b> DE LA TABLA, TODOS LOS NÚMEROS TERMINAN IGUAL."),
   LL("LA COLUMNA VA PARA ABAJO.", "3, 13, 23, 33 TERMINAN EN 3.")],
   {"modo": "cuadro", "que": "columna", "hasta": 100}, {"modo": "cuadro", "que": "columna", "hasta": 100}),
 T("BAJAR UNA FILA", [LD("ABAJO", "EL NÚMERO DE <b>ABAJO</b> ES 10 MÁS QUE EL DE ARRIBA."),
   LL("DEBAJO DEL 45 ESTÁ EL 55.", "LA PRIMERA CIFRA CRECE 1 Y LA ÚLTIMA QUEDA IGUAL.")],
   {"modo": "cuadro", "que": "bajar", "hasta": 100}, {"modo": "cuadro", "que": "bajar", "hasta": 100}),
], "recuerda": [
 RC("LA COLUMNA", "VA PARA ABAJO Y SUS NÚMEROS TERMINAN IGUAL.", "8, 18, 28, 38 TERMINAN EN 8"),
 RC("BAJAR UNA FILA", "ES SUMAR 10 AL NÚMERO DE ARRIBA.", "DEBAJO DEL 62 ESTÁ EL 72"),
]}

N4["leccion"] = {"temas": [
 T("CONTAR DE A 2", [LD("SALTOS DE 2", "CONTAR <b>DE A 2</b> ES SALTAR UN NÚMERO CADA VEZ."),
   LL("0, 2, 4, 6, 8, 10.", "NO DECIMOS EL DE EN MEDIO.")],
   {"modo": "saltos", "de": 2}, {"modo": "saltos", "de": 2}),
 T("CONTAR DE A 5", [LD("SALTOS DE 5", "CONTAR <b>DE A 5</b> ES COMO CONTAR LOS DEDOS DE CADA MANO."),
   LL("5, 10, 15, 20, 25.", "TERMINAN EN 5 O EN 0.")],
   {"modo": "saltos", "de": 5}, {"modo": "saltos", "de": 5}),
 T("CONTAR DE A 10", [LD("SALTOS DE 10", "CONTAR <b>DE A 10</b> ES BAJAR POR LA COLUMNA DE LOS REDONDOS."),
   LL("10, 20, 30, 40, 50.", "ASÍ LLEGAMOS RÁPIDO AL 100.")],
   {"modo": "saltos", "de": 10}, {"modo": "saltos", "de": 10}),
], "recuerda": [
 RC("DE A 2", "SALTAMOS DE DOS EN DOS SIN DECIR EL DE EN MEDIO.", "2, 4, 6, 8, 10"),
 RC("DE A 5", "SALTAMOS DE CINCO EN CINCO, COMO LOS DEDOS.", "5, 10, 15, 20"),
 RC("DE A 10", "SALTAMOS DE DIEZ EN DIEZ POR LOS REDONDOS.", "10, 20, 30, 40"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 79?", 80, "DESPUÉS DE UN 9 VIENE UN REDONDO.", **A),
      UNIR("UNÍ CADA NÚMERO REDONDO CON SU NOMBRE.", ["60", "70", "90"], ["NOVENTA", "SESENTA", "SETENTA"], {"60": "SESENTA", "70": "SETENTA", "90": "NOVENTA"}, "60 ES SESENTA, 70 ES SETENTA Y 90 ES NOVENTA.", **RE),
      MC("LEO CONTÓ: 97, 98, 99, 910. ¿QUÉ NÚMERO VA DESPUÉS DEL 99?", ["100", "910", "90"], "100", "DESPUÉS DEL 99 VIENE EL 100: CIEN.", **ER),
      FB("COMPLETÁ: 58, 59, ___, 61", [["60"]], "DESPUÉS DEL 59 VIENE EL 60.", **A)],
"2": [CLAS("¿EN QUÉ FILA DE LA TABLA VA CADA NÚMERO?", ["72", "65", "78", "61"], ["FILA DEL 60", "FILA DEL 70"],
           {"72": "FILA DEL 70", "65": "FILA DEL 60", "78": "FILA DEL 70", "61": "FILA DEL 60"}, "65 Y 61 EMPIEZAN CON 6; 72 Y 78 CON 7.", **A),
      MC("¿CUÁNTOS NÚMEROS HAY EN CADA FILA DE LA TABLA DE CIEN?", ["10", "100", "9"], "10", "CADA FILA TIENE 10 NÚMEROS.", **RE),
      MC("SOFI BUSCA EL 56 EN LA TABLA. ¿EN QUÉ FILA LO TIENE QUE BUSCAR?", ["LA DEL 50", "LA DEL 60", "LA DEL 6"], "LA DEL 50", "56 EMPIEZA CON 5: FILA DEL 50.", **AN),
      N("¿QUÉ NÚMERO REDONDO EMPIEZA LA FILA DONDE ESTÁ EL 84?", 80, "84 EMPIEZA CON 8: SU FILA EMPIEZA EN EL 80.", **A)],
"3": [N("¿QUÉ NÚMERO VA DEBAJO DEL 45 EN LA TABLA?", 55, "BAJAR UNA FILA ES SUMAR 10.", **A),
      MC("MIRÁ LA COLUMNA: 3, 13, 23, 33… ¿QUÉ SIGUE?", ["34", "43", "44"], "43", "TODOS TERMINAN EN 3.", **A),
      MC("JUAN DICE QUE DEBAJO DEL 27 ESTÁ EL 28. ¿QUÉ NÚMERO ESTÁ DE VERDAD?", ["37", "28", "26"], "37", "EL 28 ESTÁ AL COSTADO; ABAJO ESTÁ EL 37.", **ER),
      ORD("ORDENÁ LA COLUMNA DE ARRIBA ABAJO.", ["46", "16", "36", "26"], ["16", "26", "36", "46"], "CADA VEZ QUE BAJÁS, SUMÁS 10.", **A)],
"4": [FB("CONTÁ DE A 2: 2, 4, ___, 8, ___", [["6"], ["10"]], "2, 4, 6, 8, 10.", **A),
      N("5, 10, 15… ¿QUÉ SIGUE?", 20, "DE A 5: 15 Y 5 MÁS SON 20.", **A),
      MC("[[problema]] CADA MANO TIENE 5 DEDOS. ¿CUÁNTOS DEDOS HAY EN 4 MANOS? CONTÁ DE A 5.", ["20", "9", "40"], "20", "5, 10, 15, 20.", **AN),
      CLAS("¿DE A CUÁNTO SALTA CADA SERIE?", ["10, 20, 30", "5, 10, 15", "2, 4, 6"], ["DE A 2", "DE A 5", "DE A 10"],
           {"10, 20, 30": "DE A 10", "5, 10, 15": "DE A 5", "2, 4, 6": "DE A 2"}, "MIRÁ CUÁNTO CRECE DE UN NÚMERO AL OTRO.", **AN)],
"5": [N("RELÁMPAGO. ¿QUÉ SIGUE DESPUÉS DEL 69?", 70, "69, 70.", tiempo=30, **A),
      N("RELÁMPAGO. 10, 20, 30… ¿QUÉ SIGUE?", 40, "DE A 10.", tiempo=30, **A),
      N("RELÁMPAGO. ¿QUÉ VA DEBAJO DEL 23?", 33, "SUMA 10.", tiempo=30, **A),
      N("RELÁMPAGO. 2, 4, 6… ¿QUÉ SIGUE?", 8, "DE A 2.", tiempo=30, **A)],
}
EXAMEN = [
 [1, N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 59?", 60, "59, 60.", **A)],
 [1, FB("COMPLETÁ: 86, 87, ___, 89", [["88"]], "87, 88, 89.", **A)],
 [1, MC("¿CUÁL ES UN NÚMERO REDONDO?", ["70", "73", "77"], "70", "TERMINA EN 0.", **RE)],
 [2, MC("¿EN QUÉ FILA DE LA TABLA ESTÁ EL 72?", ["LA DEL 70", "LA DEL 20", "LA DEL 80"], "LA DEL 70", "EMPIEZA CON 7.", **A)],
 [2, MC("UNA COLUMNA DE LA TABLA VA…", ["PARA ABAJO", "DE COSTADO"], "PARA ABAJO", "LA FILA VA DE COSTADO.", **RE)],
 [2, CLAS("¿EN QUÉ FILA VA CADA NÚMERO?", ["43", "38", "47", "31"], ["FILA DEL 30", "FILA DEL 40"],
          {"43": "FILA DEL 40", "38": "FILA DEL 30", "47": "FILA DEL 40", "31": "FILA DEL 30"}, "38 Y 31 EMPIEZAN CON 3; 43 Y 47 CON 4.", **A)],
 [3, N("¿QUÉ NÚMERO VA DEBAJO DEL 62?", 72, "62 Y 10 MÁS SON 72.", **A)],
 [3, MC("8, 18, 28, 38… ¿QUÉ SIGUE?", ["39", "48", "40"], "48", "TODOS TERMINAN EN 8.", **A)],
 [3, MC("MICA DICE QUE DEBAJO DEL 50 ESTÁ EL 51. ¿QUÉ NÚMERO ESTÁ DE VERDAD?", ["60", "51", "40"], "60", "ABAJO ES 10 MÁS: 60.", **ER)],
 [4, N("2, 4, 6, 8, 10… ¿QUÉ SIGUE?", 12, "DE A 2.", **A)],
 [4, FB("CONTÁ DE A 5: 5, 10, 15, ___, 25", [["20"]], "15 Y 5 MÁS SON 20.", **A)],
 [4, N("10, 20, 30, 40… ¿QUÉ SIGUE?", 50, "DE A 10.", **A)],
 [4, MC("[[problema]] HAY 3 MANOS LEVANTADAS. ¿CUÁNTOS DEDOS SON? CONTÁ DE A 5.", ["15", "8", "30"], "15", "5, 10, 15.", **AN)],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 4, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: los números hasta 100", "examen_titulo": "Nivel jefe: los números hasta 100",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
