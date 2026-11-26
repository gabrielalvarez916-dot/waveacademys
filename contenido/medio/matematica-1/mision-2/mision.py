# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 2 · Los números hasta 20. Genera mision-2.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: el tren de los números de Tomi (igual que en las clases animadas, clases.py)."""
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
"objetivo": "Vas a contar, leer y ordenar los números del 1 al 10.",
"vas_a_ver": ["Los números del 1 al 10", "Contar con las dos manos", "El último número dice cuántos hay"],
"secciones": [
 S(1, "El tren del 1 al 10", [
  P("Tomi viaja en el tren de los números."),
  P("Cada vagón tiene su número: <b>1, 2, 3… hasta el 10</b>."),
  IMG("El tren de Tomi", "Diez vagones, del 1 al 10.", FG.tren(1, 10)),
 ]),
 S(1, "Contar hasta 10", [
  D("Dos manos", "En tus <b>dos manos</b> tenés <b>10 dedos</b>. Te ayudan a contar."),
  IMG("Las manzanas", "El último número es 7: hay 7 manzanas.", FG.contar_numerado("manzana", 7, "7 manzanas")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Grupos A, B y C", "Contá cada grupo con el dedo.", FG.grupos_letras([("A", "pelota", 4), ("B", "estrella", 8), ("C", "caramelo", 10)])),
 ]),
],
"ejemplo_completo": {"titulo": "Los vagones", "planteo": "Tomi cuenta los vagones del tren.", "pasos": ["Toca cada vagón y dice un número.", "1, 2, 3, 4, 5, 6.", "El último número es 6: hay 6 vagones."]},
"ejemplo_incompleto": {"titulo": "Los números en orden", "planteo": "Completá los números que faltan.", "pasos": ["1, 2, 3, ___ , 5.", "6, ___ , 8, 9, 10."]},
"ejemplo_solo": {"titulo": "Tus dedos", "planteo": "Contá los dedos de una mano. ¿Cuántos son?"},
"tip": {"titulo": "Usá tus manos", "texto": "Levantá un dedo por cada número que decís."},
"ojo": ["No te saltees ningún número.", "Decilos siempre en orden."],
"resumen": [{"titulo": "Del 1 al 10", "texto": "Siempre en orden."}, {"titulo": "Dos manos", "texto": "Diez dedos."}, {"titulo": "Cuántos hay", "texto": "Lo dice el último número."}],
"glosario": [{"palabra": "Número", "significado": "Lo que usamos para contar."}, {"palabra": "Orden", "significado": "Uno detrás de otro, sin saltear."}],
"carpeta": ["¿Cuántas pelotas hay en el grupo A?", "¿Cuántas estrellas hay en el grupo B?", "¿Cuántos caramelos hay en el grupo C?"],
"respuestas_carpeta": [["4"], ["8"], ["10"]],
"soluciones": {"incompleto": "4. 7.", "solo": "5 dedos.", "carpeta": ["4.", "8.", "10."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar del 11 al 20 con una caja de 10.",
"vas_a_ver": ["Diez y algo más", "Del 11 al 19", "El 20 es diez y diez"],
"secciones": [
 S(1, "Diez y algo más", [
  P("Esta caja tiene <b>10 caramelos</b>. Al lado hay 3 sueltos."),
  P("Contamos desde el 10: <b>11, 12, 13</b>."),
  IMG("Caramelos", "10 y 3 son 13.", FG.diez_y_mas("caramelo", 13, "10 y 3 son 13")),
 ]),
 S(1, "El tren hasta el 20", [
  D("Del 11 al 19", "Cada número es <b>diez y algo más</b>. El <b>20</b> es diez y diez."),
  IMG("El tren sigue", "Del 11 al 20.", FG.tren(11, 20)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cajas. Las vas a usar en la carpeta."),
  IMG("Caja A", "Una caja de 10 y sueltos.", FG.diez_y_mas("estrella", 12)),
  IMG("Caja B", "Una caja de 10 y sueltos.", FG.diez_y_mas("pelota", 16)),
 ]),
],
"ejemplo_completo": {"titulo": "Estrellas", "planteo": "Hay una caja de 10 estrellas y 4 sueltas.", "pasos": ["Empezamos en 10.", "Seguimos: 11, 12, 13, 14.", "10 y 4 son 14."]},
"ejemplo_incompleto": {"titulo": "Pelotas", "planteo": "Hay una caja de 10 pelotas y 6 sueltas.", "pasos": ["Empezamos en ___ .", "Seguimos: 11, 12, 13, 14, 15, ___ .", "10 y 6 son ___ ."]},
"ejemplo_solo": {"titulo": "Lápices", "planteo": "Tenés 10 lápices y te regalan 9. ¿Cuántos tenés?"},
"tip": {"titulo": "Empezá en 10", "texto": "No cuentes la caja de nuevo: arrancá en 10."},
"ojo": ["Diez y seis es 16, no 106.", "Después del 19 viene el 20."],
"resumen": [{"titulo": "Caja de 10", "texto": "Arrancamos a contar en 10."}, {"titulo": "11 al 19", "texto": "Diez y algo más."}, {"titulo": "20", "texto": "Diez y diez."}],
"glosario": [{"palabra": "Diez", "significado": "Un grupo de 10 cosas."}, {"palabra": "Veinte", "significado": "Dos grupos de 10."}],
"carpeta": ["¿Cuántas estrellas hay en la caja A en total?", "¿Cuántas pelotas hay en la caja B en total?", "¿Qué número viene después del 19?"],
"respuestas_carpeta": [["12"], ["16"], ["20"]],
"soluciones": {"incompleto": "10. 16. 16.", "solo": "19 lápices: 10 y 9.", "carpeta": ["12: 10 y 2.", "16: 10 y 6.", "20."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir los números con cifras y leerlos con palabras.",
"vas_a_ver": ["Escribir con cifras", "Leer con palabras", "Del 10 al 19 empiezan con 1"],
"secciones": [
 S(1, "Cifras y palabras", [
  P("Un número se puede <b>escribir con cifras</b> o <b>leer con palabras</b>."),
  P("12 se lee <b>doce</b>. 15 se lee <b>quince</b>."),
  IMG("Tarjetas", "Cada número con su nombre.", FG.tarjetas([(12, "doce"), (15, "quince"), (18, "dieciocho")])),
 ]),
 S(1, "Primero el 1", [
  D("Del 10 al 19", "Todos empiezan con <b>1</b>. Doce es un 1 y un 2: <b>12</b>."),
  IMG("Del 10 al 19", "Todos empiezan con 1.", FG.tarjetas([(10, "diez"), (11, "once"), (13, "trece"), (19, "diecinueve")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas para completar", "Escribí el nombre que falta.", FG.tarjetas([(14, "catorce"), (16, "dieciséis"), (20, "veinte")], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Trece", "planteo": "¿Cómo se escribe trece?", "pasos": ["Trece empieza con 1.", "Después va el 3.", "Se escribe 13."]},
"ejemplo_incompleto": {"titulo": "Diecisiete", "planteo": "Completá.", "pasos": ["Diecisiete empieza con ___ .", "Después va el 7.", "Se escribe ___ ."]},
"ejemplo_solo": {"titulo": "Tu edad", "planteo": "Escribí con cifras cuántos años tenés."},
"tip": {"titulo": "Mirá el primero", "texto": "Del 10 al 19, la primera cifra es 1."},
"ojo": ["Doce es 12, no 21.", "Mirá bien el orden de las cifras."],
"resumen": [{"titulo": "Escribir", "texto": "Con cifras: 12."}, {"titulo": "Leer", "texto": "Con palabras: doce."}, {"titulo": "Del 10 al 19", "texto": "Empiezan con 1."}],
"glosario": [{"palabra": "Cifra", "significado": "Cada símbolo: 0, 1, 2… 9."}, {"palabra": "Leer", "significado": "Decir el nombre del número."}],
"carpeta": ["Escribí con palabras el número 14.", "Escribí con palabras el número 20.", "Escribí con cifras: dieciséis."],
"respuestas_carpeta": [["catorce"], ["veinte"], ["16"]],
"soluciones": {"incompleto": "1. 17.", "solo": "Depende de tu edad: por ejemplo, 6 o 7.", "carpeta": ["Catorce.", "Veinte.", "16."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ordenar números hasta 20.",
"vas_a_ver": ["El anterior y el siguiente", "La recta numérica", "Mayor y menor"],
"secciones": [
 S(1, "Anterior y siguiente", [
  D("Anterior y siguiente", "El <b>anterior</b> va antes. El <b>siguiente</b> va después."),
  P("El anterior del 14 es el 13. El siguiente es el 15."),
  IMG("La recta del 10 al 20", "13 va antes del 14. 15 va después.", FG.recta_num(10, 20, [(13, "antes"), (14, ""), (15, "después")])),
 ]),
 S(1, "Mayor y menor", [
  P("En la recta, el número <b>mayor</b> está más lejos del 0."),
  P("18 es mayor que 12. 12 es menor que 18."),
  IMG("12 y 18 en la recta", "18 está más lejos del 0.", FG.recta_num(10, 20, [(12, "menor"), (18, "mayor")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("¿Qué vagones faltan?", "Completá los vagones con ?.", FG.tren(13, 20, (15, 19))),
 ]),
],
"ejemplo_completo": {"titulo": "El 9", "planteo": "¿Cuál es el anterior y el siguiente del 9?", "pasos": ["Antes del 9 va el 8.", "Después del 9 va el 10.", "8, 9, 10."]},
"ejemplo_incompleto": {"titulo": "El 17", "planteo": "Completá.", "pasos": ["Antes del 17 va el ___ .", "Después del 17 va el ___ ."]},
"ejemplo_solo": {"titulo": "Ordenar", "planteo": "Ordená de menor a mayor: 15, 11, 19."},
"tip": {"titulo": "Pensá en la recta", "texto": "Más a la derecha, más grande."},
"ojo": ["El anterior va antes, el siguiente después.", "Mayor es el que está más lejos del 0."],
"resumen": [{"titulo": "Anterior", "texto": "El que va antes."}, {"titulo": "Siguiente", "texto": "El que va después."}, {"titulo": "Mayor", "texto": "Más lejos del 0."}],
"glosario": [{"palabra": "Anterior", "significado": "El número que va antes."}, {"palabra": "Siguiente", "significado": "El número que va después."}],
"carpeta": ["¿Qué número falta en el primer vagón vacío?", "¿Qué número falta en el segundo vagón vacío?", "¿Cuál es mayor: 16 o 13?"],
"respuestas_carpeta": [["15"], ["19"], ["16"]],
"soluciones": {"incompleto": "16. 18.", "solo": "11, 15, 19.", "carpeta": ["15: va entre 14 y 16.", "19: va entre 18 y 20.", "16: está más lejos del 0."]},
}

# ---------- LECCIÓN INTERACTIVA (escrita en sesión, docs/reglas-leccion-interactiva.md, primer ciclo: poco texto, todo visual) ----------
LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LP = lambda x: {"tipo": "parrafo", "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["carpeta_nivel"] = ["aplicar", "aplicar", "aplicar"]
N1["leccion"] = {"temas": [
 T("LOS NÚMEROS EN ORDEN", [LD("EN ORDEN", "LOS NÚMEROS VAN <b>EN ORDEN</b>: CADA UNO VIENE DESPUÉS DEL OTRO."),
   LL("1, 2, 3, 4, 5, 6, 7, 8, 9, 10.", "NO SE SALTEA NINGUNO.")],
   {"modo": "tren", "desde": 1, "hasta": 10}, {"modo": "falta", "desde": 1, "hasta": 10}),
 T("CONTAR HASTA 10", [LD("CON LOS DEDOS", "PODÉS CONTAR CON LOS DEDOS: CADA DEDO ES UN NÚMERO Y DOS MANOS LLEGAN AL 10."),
   LP("CUANDO TERMINÁS, EL ÚLTIMO NÚMERO TE DICE CUÁNTOS HAY.")],
   {"modo": "contar", "max": 10}, {"modo": "contar", "min": 5, "max": 10}),
], "recuerda": [
 RC("EN ORDEN", "CADA NÚMERO VIENE DESPUÉS DEL ANTERIOR, SIN SALTEAR.", "5, 6, 7, 8, 9, 10"),
 RC("DOS MANOS", "TIENEN DIEZ DEDOS QUE TE AYUDAN A CONTAR HASTA 10.", "🖐️ 5 Y 🖐️ 5 SON 10"),
]}

N2["carpeta_nivel"] = ["aplicar", "aplicar", "recordar"]
N2["leccion"] = {"temas": [
 T("DIEZ Y ALGO MÁS", [LD("LA CAJA DE 10", "UNA CAJA DE 10 Y ALGUNOS SUELTOS FORMAN LOS NÚMEROS DEL 11 AL 19."),
   LP("YA SABEMOS QUE LA CAJA TIENE 10: SEGUIMOS CONTANDO LOS SUELTOS DESDE AHÍ.")],
   {"modo": "decena", "ini": 3}, {"modo": "decena"}),
 T("LLEGAMOS AL 20", [LD("VEINTE", "EL <b>20</b> SON DOS GRUPOS DE 10. SE LEE VEINTE."),
   LL("DESPUÉS DEL 19 VIENE EL 20.", "DIEZ Y SEIS ES 16, NO 106.")],
   {"modo": "tren", "desde": 10, "hasta": 20}, {"modo": "falta", "desde": 10, "hasta": 20}),
], "recuerda": [
 RC("DEL 11 AL 19", "SON UNA CAJA DE 10 Y ALGUNOS SUELTOS MÁS.", "📦 10 Y 4 SUELTOS SON 14"),
 RC("VEINTE", "ES EL NÚMERO QUE FORMAN DOS GRUPOS DE 10.", "📦 10 Y 📦 10 SON 20"),
]}

N3["carpeta_nivel"] = ["aplicar", "aplicar", "aplicar"]
N3["leccion"] = {"temas": [
 T("CIFRAS Y PALABRAS", [LD("ESCRIBIR Y LEER", "UN NÚMERO SE ESCRIBE CON <b>CIFRAS</b> Y SE LEE CON <b>PALABRAS</b>."),
   LL("15 SE LEE QUINCE.", "LAS CIFRAS SON 0, 1, 2, 3, 4, 5, 6, 7, 8 Y 9.")],
   {"modo": "leer"}, {"modo": "leer"}),
 T("PRIMERO EL 1", [LD("DEL 10 AL 19", "DEL 10 AL 19, LA <b>PRIMERA CIFRA</b> SIEMPRE ES UN 1."),
   LP("TRECE ES 13, NO 31: SI CAMBIÁS EL ORDEN DE LAS CIFRAS, CAMBIA EL NÚMERO.")],
   {"modo": "leer", "forma": "escribir"}, {"modo": "escribir"}),
], "recuerda": [
 RC("CIFRAS", "CON CIFRAS ESCRIBIMOS LOS NÚMEROS, COMO EL 17.", "DIECISIETE SE ESCRIBE 17"),
 RC("PALABRAS", "CON PALABRAS DECIMOS EL NOMBRE DEL NÚMERO.", "18 SE LEE DIECIOCHO"),
 RC("PRIMERO EL 1", "DEL 10 AL 19 LA PRIMERA CIFRA ES UN 1.", "ONCE ES 11 Y CATORCE ES 14"),
]}

N4["carpeta_nivel"] = ["aplicar", "aplicar", "analizar"]
N4["leccion"] = {"temas": [
 T("ANTERIOR Y SIGUIENTE", [LD("ANTERIOR Y SIGUIENTE", "EL <b>ANTERIOR</b> VA JUSTO ANTES Y EL <b>SIGUIENTE</b> VA JUSTO DESPUÉS."),
   LL("ANTES DEL 16 VA EL 15.", "DESPUÉS DEL 16 VA EL 17.")],
   {"modo": "anterior_siguiente"}, {"modo": "anterior_siguiente"}),
 T("MAYOR Y MENOR", [LD("MAYOR", "EL <b>MAYOR</b> ES EL QUE ESTÁ MÁS LEJOS DEL 0 EN LA RECTA."),
   LP("Y EL <b>MENOR</b> ES EL QUE QUEDA MÁS CERCA DEL 0.")],
   {"modo": "mayor_menor"}, {"modo": "mayor_menor"}),
], "recuerda": [
 RC("ANTERIOR", "ES EL NÚMERO QUE VA JUSTO ANTES.", "EL ANTERIOR DEL 12 ES 11"),
 RC("SIGUIENTE", "ES EL NÚMERO QUE VA JUSTO DESPUÉS.", "EL SIGUIENTE DEL 12 ES 13"),
 RC("MAYOR Y MENOR", "EL MAYOR ESTÁ MÁS LEJOS DEL 0 Y EL MENOR MÁS CERCA.", "19 ES MAYOR QUE 11"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ORD = lambda p, o, orden, e, **k: {"t": "ordering", "p": p, "o": o, "r": {"orden": orden}, "e": e, **k}
UNIR = lambda p, iz, de, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": iz, "derecha": de}, "r": {"pares": pares}, "e": e, **k}
CLAS = lambda p, el, cats, r, e, **k: {"t": "classify", "p": p, "o": {"elementos": el, "categorias": cats}, "r": {"categorias": r}, "e": e, **k}
FB = lambda p, huecos, e, **k: {"t": "fill_blank", "p": p, "o": {}, "r": {"huecos": huecos}, "e": e, **k}
A, AN, RE, ER = {"n": "aplicar"}, {"n": "analizar"}, {"n": "recordar"}, {"n": "error"}

ACT = {
"1": [N("¿CUÁNTOS PATITOS HAY? CONTÁ CON EL DEDO. 🐤🐤🐤🐤🐤🐤🐤🐤", 8, "1, 2, 3, 4, 5, 6, 7, 8. HAY 8.", **A),
      MC("EN EL TREN VAN EL 7, EL 8 Y EL 9. ¿QUÉ VAGÓN SIGUE?", ["8", "10", "7"], "10", "DESPUÉS DEL 9 VIENE EL 10.", **A),
      FB("COMPLETÁ LOS VAGONES QUE FALTAN: 1, 2, 3, ___, 5, 6, ___, 8, 9, 10", [["4"], ["7"]], "DESPUÉS DEL 3 VA EL 4 Y DESPUÉS DEL 6 VA EL 7.", **A),
      ORD("ORDENÁ LOS VAGONES DEL TREN, DEL MÁS CHICO AL MÁS GRANDE.", ["6", "3", "9", "1", "10"], ["1", "3", "6", "9", "10"], "1, 3, 6, 9 Y 10: EN ORDEN.", **A)],
"2": [N("📦 10 Y 🍬🍬🍬🍬 ¿CUÁNTOS CARAMELOS SON EN TOTAL?", 14, "10 Y 4 SON 14.", **A),
      MC("JUAN DICE QUE DIEZ Y SEIS SE ESCRIBE 106. ¿QUÉ NÚMERO ES DE VERDAD?", ["16", "106", "60"], "16", "DIEZ Y SEIS ES 16: UN 1 Y UN 6.", **ER),
      UNIR("UNÍ CADA CAJA CON SU NÚMERO.", ["📦 10 Y ⭐⭐", "📦 10 Y ⭐⭐⭐⭐⭐", "📦 10 Y 📦 10"], ["20", "12", "15"],
           {"📦 10 Y ⭐⭐": "12", "📦 10 Y ⭐⭐⭐⭐⭐": "15", "📦 10 Y 📦 10": "20"}, "10 Y 2 SON 12, 10 Y 5 SON 15, 10 Y 10 SON 20.", **A),
      N("[[problema]] TENÉS 10 FIGURITAS Y TE REGALAN 7. ¿CUÁNTAS FIGURITAS TENÉS AHORA?", 17, "ARRANCAMOS EN 10 Y SEGUIMOS: 11, 12, 13, 14, 15, 16, 17.", **A)],
"3": [MC("¿CÓMO SE ESCRIBE QUINCE?", ["51", "15", "5"], "15", "QUINCE ES UN 1 Y UN 5: 15.", **RE),
      MC("¿CÓMO SE LEE 19?", ["NUEVE", "DIECINUEVE", "NOVENTA"], "DIECINUEVE", "19 SE LEE DIECINUEVE.", **RE),
      UNIR("UNÍ CADA NÚMERO CON SU NOMBRE.", ["13", "17", "20"], ["VEINTE", "TRECE", "DIECISIETE"], {"13": "TRECE", "17": "DIECISIETE", "20": "VEINTE"}, "13 ES TRECE, 17 ES DIECISIETE Y 20 ES VEINTE.", **A),
      MC("LUCÍA ESCRIBIÓ 21 PARA DECIR DOCE. ¿CÓMO SE ESCRIBE BIEN?", ["12", "21", "2"], "12", "DOCE EMPIEZA CON 1: SE ESCRIBE 12.", **ER)],
"4": [N("EN EL TREN, ¿QUÉ NÚMERO VA JUSTO ANTES DEL 13?", 12, "ANTES DEL 13 VA EL 12.", **A),
      MC("¿CUÁL ES MAYOR, 17 O 14? PENSÁ EN LA RECTA.", ["17", "14"], "17", "17 ESTÁ MÁS LEJOS DEL 0.", **A),
      ORD("ORDENÁ DE MENOR A MAYOR.", ["18", "11", "15", "13"], ["11", "13", "15", "18"], "11, 13, 15 Y 18: DE MENOR A MAYOR.", **A),
      CLAS("¿VA ANTES O DESPUÉS DEL 15? UBICÁ CADA NÚMERO.", ["12", "19", "14", "17"], ["ANTES DEL 15", "DESPUÉS DEL 15"],
           {"12": "ANTES DEL 15", "19": "DESPUÉS DEL 15", "14": "ANTES DEL 15", "17": "DESPUÉS DEL 15"}, "12 Y 14 SON MENORES QUE 15; 17 Y 19 SON MAYORES.", **AN)],
"5": [N("RELÁMPAGO. ¿QUÉ NÚMERO VA DESPUÉS DEL 19?", 20, "DESPUÉS DEL 19 VIENE EL 20.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿CÓMO SE ESCRIBE DOCE?", ["21", "12"], "12", "DOCE ES UN 1 Y UN 2.", tiempo=30, **RE),
      N("RELÁMPAGO. 📦 10 Y 🍬🍬🍬 ¿CUÁNTOS SON?", 13, "10 Y 3 SON 13.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿CUÁL ES MENOR?", ["11", "18"], "11", "11 ESTÁ MÁS CERCA DEL 0.", tiempo=30, **A)],
}
EXAMEN = [
 [1, N("¿CUÁNTOS SOLES HAY? CONTÁ CON EL DEDO. ☀️☀️☀️☀️☀️☀️", 6, "1, 2, 3, 4, 5, 6.", **A)],
 [1, MC("¿QUÉ NÚMERO FALTA EN EL TREN? 1, 2, 3, ___, 5", ["4", "6", "3"], "4", "DESPUÉS DEL 3 VA EL 4.", **A)],
 [1, N("¿CUÁNTOS DEDOS HAY EN DOS MANOS?", 10, "CINCO Y CINCO: 10.", **RE)],
 [2, N("📦 10 Y 🍬🍬 ¿CUÁNTOS CARAMELOS SON EN TOTAL?", 12, "10 Y 2 SON 12.", **A)],
 [2, MC("UNA CAJA DE 10 Y 8 SUELTOS. ¿CUÁNTOS SON?", ["18", "80", "108"], "18", "DIEZ Y OCHO: 18.", **A)],
 [2, MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 19?", ["20", "10", "21"], "20", "DESPUÉS DEL 19 VIENE EL 20.", **RE)],
 [3, MC("¿CÓMO SE ESCRIBE TRECE?", ["31", "13", "3"], "13", "TRECE ES UN 1 Y UN 3.", **RE)],
 [3, MC("¿CÓMO SE LEE 16?", ["SEIS", "DIECISÉIS", "SESENTA"], "DIECISÉIS", "16 SE LEE DIECISÉIS.", **RE)],
 [3, MC("TOMI ESCRIBIÓ 41 PARA DECIR CATORCE. ¿CÓMO SE ESCRIBE BIEN?", ["14", "41", "4"], "14", "CATORCE EMPIEZA CON 1: SE ESCRIBE 14.", **ER)],
 [4, N("EN EL TREN, ¿QUÉ NÚMERO VA JUSTO ANTES DEL 15?", 14, "ANTES DEL 15 VA EL 14.", **A)],
 [4, N("EN EL TREN, ¿QUÉ NÚMERO VA JUSTO DESPUÉS DEL 17?", 18, "DESPUÉS DEL 17 VA EL 18.", **A)],
 [4, ORD("ORDENÁ DE MENOR A MAYOR.", ["19", "12", "16"], ["12", "16", "19"], "12, 16 Y 19.", **A)],
 [4, MC("¿CUÁL ES MENOR, 16 O 10? PENSÁ EN LA RECTA.", ["16", "10"], "10", "10 ESTÁ MÁS CERCA DEL 0.", **A)],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 2, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: los números hasta 20", "examen_titulo": "Nivel jefe: los números hasta 20",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
