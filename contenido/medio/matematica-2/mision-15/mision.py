# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 15 · Multiplicar por 10 y por 100. Genera mision-15.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (paquetes de 10 y cajas de 100).
Niveles: 1 multiplicar por 10 · 2 multiplicar por 100 · 3 qué pasa con las cifras · 4 problemas con 10 y 100."""
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
ESTILO = {"estilo": "primeros"}
NEU = lambda p: {"neutro": {"p": p}}

N1 = {**ESTILO,
"objetivo": "Vas a multiplicar por 10.",
"vas_a_ver": ["Paquetes de 10", "Contar de 10 en 10", "Agregar un cero"],
"secciones": [
 S(1, "Paquetes de 10", [
  P("Rosa guarda los alfajores en paquetes de <b>10</b>."),
  P("4 paquetes: 10, 20, 30, 40. Son <b>4 × 10 = 40</b>."),
  IMG("Cuatro paquetes de 10", "4 × 10 = 40.", FG.bloques(0, 4, 0, "4 × 10 = 40")),
 ]),
 S(1, "Agregar un cero", [
  D("Por 10", "Para multiplicar por 10, al número le agregamos <b>un 0</b> al final."),
  P("6 × 10 = 60. 9 × 10 = 90."),
  IMG("Por 10", "Un cero al final.", FG.cuentas([("3 × 10", 30), ("6 × 10", 60), ("9 × 10", 90)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Por 10 para completar", "Agregá un cero.", FG.cuentas([("5 × 10", 50), ("7 × 10", 70), ("2 × 10", 20)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "7 × 10", "planteo": "¿Cuánto es 7 × 10?", "pasos": ["Son 7 paquetes de 10.", "Al 7 le agrego un 0.", "7 × 10 = 70."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Agregá el cero.", "pasos": ["5 × 10 = ___ .", "8 × 10 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "¿Cuánto es 3 × 10?"},
"tip": {"titulo": "Un cero", "texto": "Por 10: un cero al final."},
"ojo": ["7 × 10 es 70, no 17.", "El cero va al final."],
"resumen": [{"titulo": "Paquete", "texto": "Tiene 10."}, {"titulo": "Por 10", "texto": "Un 0 al final."}, {"titulo": "Ejemplo", "texto": "4 × 10 = 40."}],
"glosario": [{"palabra": "Multiplicar", "significado": "Sumar varias veces lo mismo."}, {"palabra": "Paquete", "significado": "Un grupo de 10."}],
"carpeta": ["¿Cuánto es 5 × 10?", "¿Cuánto es 7 × 10?", "Tomi dice que 2 × 10 = 12. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["50"], ["70"], ["20"]],
"soluciones": {"incompleto": "50. 80.", "solo": "30.", "carpeta": ["50.", "70.", "20: Tomi sumó 2 + 10."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a multiplicar por 100.",
"vas_a_ver": ["Cajas de 100", "Contar de 100 en 100", "Agregar dos ceros"],
"secciones": [
 S(1, "Cajas de 100", [
  P("En cada caja entran <b>100</b> alfajores."),
  P("3 cajas: 100, 200, 300. Son <b>3 × 100 = 300</b>."),
  IMG("Tres cajas de 100", "3 × 100 = 300.", FG.bloques(3, 0, 0, "3 × 100 = 300")),
 ]),
 S(1, "Agregar dos ceros", [
  D("Por 100", "Para multiplicar por 100, agregamos <b>dos ceros</b> al final."),
  P("5 × 100 = 500. 8 × 100 = 800."),
  IMG("De 100 en 100", "100, 200, 300…", FG.tren_paso(100, 600, 100)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Por 100 para completar", "Agregá dos ceros.", FG.cuentas([("4 × 100", 400), ("6 × 100", 600), ("9 × 100", 900)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "6 × 100", "planteo": "¿Cuánto es 6 × 100?", "pasos": ["Son 6 cajas de 100.", "Al 6 le agrego dos ceros.", "6 × 100 = 600."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Agregá los ceros.", "pasos": ["2 × 100 = ___ .", "7 × 100 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "¿Cuánto es 5 × 100?"},
"tip": {"titulo": "Dos ceros", "texto": "Por 100: dos ceros al final."},
"ojo": ["4 × 100 es 400, no 40.", "Por 100 van dos ceros."],
"resumen": [{"titulo": "Caja", "texto": "Tiene 100."}, {"titulo": "Por 100", "texto": "Dos ceros al final."}, {"titulo": "Ejemplo", "texto": "3 × 100 = 300."}],
"glosario": [{"palabra": "Caja", "significado": "Un grupo de 100."}, {"palabra": "Centena", "significado": "Cien unidades."}],
"carpeta": ["¿Cuánto es 4 × 100?", "¿Cuánto es 9 × 100?", "Sofi dice que 6 × 100 = 60. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["400"], ["900"], ["600"]],
"soluciones": {"incompleto": "200. 700.", "solo": "500.", "carpeta": ["400.", "900.", "600: Sofi puso un solo cero."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver cómo se mueven las cifras.",
"vas_a_ver": ["Las cifras se corren", "Por 10, un lugar", "Por 100, dos lugares"],
"secciones": [
 S(1, "Las cifras se corren", [
  P("24 × 10 = 240."),
  P("El 2 y el 4 se corren <b>un lugar</b> a la izquierda."),
  IMG("24 y 240", "Las cifras cambian de lugar.", FG.tablero([24, 240])),
 ]),
 S(1, "Por 100, dos lugares", [
  D("Por 100", "Por 100, cada cifra se corre <b>dos lugares</b>. Atrás van dos ceros."),
  P("3 × 100 = 300. El 3 pasa a las centenas."),
  IMG("3 y 300", "El 3 pasa a las centenas.", FG.tablero([3, 300])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tablero. Lo vas a usar en la carpeta."),
  IMG("Tablero para completar", "Completá las cifras.", FG.tablero([31, 310, 5, 500], vacios=(1, 3))),
 ]),
],
"ejemplo_completo": {"titulo": "35 × 10", "planteo": "¿Cuánto es 35 × 10?", "pasos": ["El 3 y el 5 se corren un lugar.", "Atrás va un 0.", "35 × 10 = 350."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Corré las cifras.", "pasos": ["12 × 10 = ___ .", "4 × 100 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuenta", "planteo": "¿Cuánto es 41 × 10?"},
"tip": {"titulo": "Mirá el lugar", "texto": "Por 10 se corre un lugar."},
"ojo": ["24 × 10 es 240, no 2410.", "Por 100 son dos ceros."],
"resumen": [{"titulo": "Por 10", "texto": "Un lugar y un 0."}, {"titulo": "Por 100", "texto": "Dos lugares y dos 0."}, {"titulo": "Ejemplo", "texto": "24 × 10 = 240."}],
"glosario": [{"palabra": "Cifra", "significado": "Cada número de 0 a 9 que forma otro."}, {"palabra": "Lugar", "significado": "Unidades, decenas o centenas."}],
"carpeta": ["¿Cuánto es 31 × 10?", "¿Cuánto es 5 × 100?", "Tomi dice que 24 × 10 = 2410. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["310"], ["500"], ["240"]],
"soluciones": {"incompleto": "120. 400.", "solo": "410.", "carpeta": ["310.", "500.", "240: el cero va al final, no el 10."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas con 10 y con 100.",
"vas_a_ver": ["Leer el problema", "¿Por 10 o por 100?", "Responder"],
"secciones": [
 S(1, "¿Por 10 o por 100?", [
  P("Rosa vende 6 paquetes de 10."),
  P("Son <b>6 × 10 = 60</b> alfajores."),
  IMG("Seis paquetes", "6 × 10 = 60.", FG.bloques(0, 6, 0, "6 × 10 = 60")),
 ]),
 S(1, "Cajas grandes", [
  D("Problema", "Si cada caja tiene <b>100</b>, multiplicamos por 100."),
  P("4 cajas de 100 son <b>400</b>."),
  IMG("Cuatro cajas", "4 × 100 = 400.", FG.bloques(4, 0, 0, "4 × 100 = 400")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuentas para completar", "Por 10 o por 100.", FG.cuentas([("8 × 10", 80), ("2 × 100", 200), ("5 × 10", 50)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "Paquetes", "planteo": "Rosa tiene 8 paquetes de 10. ¿Cuántos alfajores?", "pasos": ["Cada paquete tiene 10.", "8 × 10 = 80.", "Tiene 80 alfajores."]},
"ejemplo_incompleto": {"titulo": "Cajas", "planteo": "El camión lleva 7 cajas de 100.", "pasos": ["7 × 100 = ___ .", "Lleva ___ alfajores."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Hay 5 paquetes de 10. ¿Cuántos hay?"},
"tip": {"titulo": "Mirá el grupo", "texto": "¿Paquete de 10 o caja de 100?"},
"ojo": ["No sumes: multiplicá.", "Respondé con palabras."],
"resumen": [{"titulo": "Paquetes", "texto": "Por 10."}, {"titulo": "Cajas", "texto": "Por 100."}, {"titulo": "Respuesta", "texto": "Con palabras."}],
"glosario": [{"palabra": "Problema", "significado": "Una historia con pregunta."}, {"palabra": "Respuesta", "significado": "Lo que contestamos."}],
"carpeta": ["Rosa tiene 8 paquetes de 10. ¿Cuántos alfajores hay?", "Hay 2 cajas de 100. ¿Cuántos alfajores hay?", "Sofi tiene 5 paquetes de 10 y dice que son 15. ¿Cuántos son?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["80"], ["200"], ["50"]],
"soluciones": {"incompleto": "700. 700.", "solo": "50.", "carpeta": ["80.", "200.", "50: Sofi sumó en vez de multiplicar."]},
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

N1["leccion"] = {"temas": [
 T("PAQUETES DE 10", [LD("POR 10", "MULTIPLICAR <b>POR 10</b> ES JUNTAR PAQUETES DE 10."),
   LL("4 PAQUETES: 10, 20, 30, 40.", "4 × 10 = 40.")],
   {"modo": "por10", "de": 10}, {"modo": "por10", "de": 10}),
 T("AGREGAR UN CERO", [LD("EL TRUCO", "PARA MULTIPLICAR POR 10, AGREGAMOS <b>UN 0</b> AL FINAL DEL NÚMERO."),
   LL("7 × 10 = 70.", "NO ES 17: NO SE SUMA.")],
   {"modo": "por10", "de": 10}, {"modo": "por10", "de": 10}),
], "recuerda": [
 RC("POR 10", "ES JUNTAR PAQUETES DE DIEZ.", "4 × 10 = 40"),
 RC("EL TRUCO", "AGREGAMOS UN CERO AL FINAL DEL NÚMERO.", "9 × 10 = 90"),
]}

N2["leccion"] = {"temas": [
 T("CAJAS DE 100", [LD("POR 100", "MULTIPLICAR <b>POR 100</b> ES JUNTAR CAJAS DE 100."),
   LL("3 CAJAS: 100, 200, 300.", "3 × 100 = 300.")],
   {"modo": "por10", "de": 100}, {"modo": "por10", "de": 100}),
 T("AGREGAR DOS CEROS", [LD("DOS CEROS", "EL 100 TIENE DOS CEROS: ESOS <b>DOS CEROS</b> SE PEGAN DETRÁS DEL NÚMERO."),
   LL("6 × 100 = 600.", "NO ES 60: VAN DOS CEROS.")],
   {"modo": "por10", "de": 100}, {"modo": "por10", "que": "cuantos0"}),
], "recuerda": [
 RC("POR 100", "ES JUNTAR CAJAS DE CIEN.", "3 × 100 = 300"),
 RC("DOS CEROS", "AGREGAMOS DOS CEROS AL FINAL DEL NÚMERO.", "8 × 100 = 800"),
]}

N3["leccion"] = {"temas": [
 T("LAS CIFRAS SE CORREN", [LD("UN LUGAR", "POR 10, CADA CIFRA SE CORRE <b>UN LUGAR</b>. ATRÁS VA UN 0."),
   LL("24 × 10 = 240.", "EL 2 PASA A LAS CENTENAS.")],
   {"modo": "por10", "que": "cifras", "de": 10}, {"modo": "por10", "que": "cifras", "de": 10}),
 T("POR 100, DOS LUGARES", [LD("DOS LUGARES", "CON EL 100, LAS CIFRAS SALTAN <b>DOS LUGARES</b> HACIA LA IZQUIERDA."),
   LL("3 × 100 = 300.", "24 × 10 NO ES 2410.")],
   {"modo": "por10", "que": "cifras", "de": 100}, {"modo": "por10", "que": "cifras", "de": 100}),
], "recuerda": [
 RC("POR 10", "LAS CIFRAS SE CORREN UN LUGAR Y VA UN CERO.", "35 × 10 = 350"),
 RC("POR 100", "LAS CIFRAS SE CORREN DOS LUGARES Y VAN DOS CEROS.", "4 × 100 = 400"),
]}

N4["leccion"] = {"temas": [
 T("¿POR 10 O POR 100?", [LD("MIRAR EL GRUPO", "MIRAMOS SI HAY <b>PAQUETES DE 10</b> O <b>CAJAS DE 100</b>."),
   LL("6 PAQUETES DE 10: 6 × 10.", "4 CAJAS DE 100: 4 × 100.")],
   {"modo": "por10", "de": 10}, {"modo": "por10", "que": "problema"}),
 T("RESPONDER", [LD("LA RESPUESTA", "DESPUÉS DE MULTIPLICAR, <b>RESPONDEMOS</b> CON UNA ORACIÓN."),
   LL("8 × 10 = 80: HAY 80 ALFAJORES.", "NO SE SUMA 8 + 10.")],
   {"modo": "por10", "de": 100}, {"modo": "por10", "que": "problema"}),
], "recuerda": [
 RC("MIRAR EL GRUPO", "VEMOS SI LOS GRUPOS SON DE DIEZ O DE CIEN.", "6 PAQUETES DE 10 = 60"),
 RC("RESPONDER", "CONTESTAMOS CON UNA ORACIÓN COMPLETA.", "HAY 400 ALFAJORES"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("📦 4 PAQUETES DE 10. ¿CUÁNTOS ALFAJORES SON?", 40, "10, 20, 30, 40: 4 × 10 = 40.", n="aplicar", **NEU("📦 4 PAQUETES DE 10. ¿CUÁNTAS GALLETAS SON?")),
      FB("COMPLETÁ: 7 × 10 = ___", [["70"]], "AL 7 LE AGREGAMOS UN CERO.", n="aplicar"),
      UNIR("UNÍ CADA CUENTA CON SU RESULTADO.", ["3 × 10", "8 × 10", "5 × 10"], ["50", "30", "80"], {"3 × 10": "30", "8 × 10": "80", "5 × 10": "50"}, "UN CERO AL FINAL.", n="aplicar"),
      MC("TOMI DICE QUE 2 × 10 = 12. ¿CUÁNTO ES?", ["20", "12", "210"], "20", "NO SE SUMA: SE AGREGA UN CERO.", n="error")],
"2": [N("🗃️ 3 CAJAS DE 100. ¿CUÁNTOS ALFAJORES SON?", 300, "100, 200, 300.", n="aplicar", **NEU("🗃️ 3 CAJAS DE 100. ¿CUÁNTAS GALLETAS SON?")),
      FB("COMPLETÁ: 6 × 100 = ___", [["600"]], "AL 6 LE AGREGAMOS DOS CEROS.", n="aplicar"),
      MC("PARA HACER × 100, ¿CUÁNTOS CEROS AGREGÁS?", ["DOS", "UNO", "TRES"], "DOS", "100 TIENE DOS CEROS.", n="recordar", **NEU("PARA HACER × 100, ¿CUÁNTOS CEROS AGREGAS?")),
      MC("SOFI DICE QUE 6 × 100 = 60. ¿CUÁNTO ES?", ["600", "60", "106"], "600", "POR 100 VAN DOS CEROS.", n="error")],
"3": [N("¿CUÁNTO ES 24 × 10?", 240, "LAS CIFRAS SE CORREN UN LUGAR: 240.", n="aplicar"),
      CLAS("¿SE MULTIPLICÓ POR 10 O POR 100?", ["3 → 300", "3 → 30", "12 → 120", "7 → 700"], ["POR 10", "POR 100"],
           {"3 → 300": "POR 100", "3 → 30": "POR 10", "12 → 120": "POR 10", "7 → 700": "POR 100"}, "CONTÁ LOS CEROS QUE SE AGREGARON.", n="analizar"),
      FB("COMPLETÁ: 35 × 10 = ___", [["350"]], "EL 3 Y EL 5 SE CORREN: 350.", n="aplicar"),
      MC("TOMI DICE QUE 24 × 10 = 2410. ¿CUÁNTO ES?", ["240", "2410", "34"], "240", "SE AGREGA UN CERO, NO UN 10.", n="error")],
"4": [N("[[problema]] ROSA TIENE 8 PAQUETES DE 10 ALFAJORES. ¿CUÁNTOS ALFAJORES TIENE?", 80, "8 × 10 = 80.", n="aplicar", **NEU("ROSA TIENE 8 PAQUETES DE 10 GALLETAS. ¿CUÁNTAS GALLETAS TIENE?")),
      N("[[problema]] UN CAMIÓN LLEVA 5 CAJAS Y CADA CAJA TIENE 100 ALFAJORES. ¿CUÁNTOS LLEVA?", 500, "5 × 100 = 500.", n="analizar", **NEU("UN CAMIÓN LLEVA 5 CAJAS Y CADA CAJA TIENE 100 GALLETAS. ¿CUÁNTAS LLEVA?")),
      CLAS("¿QUÉ CUENTA HACÉS?", ["6 PAQUETES DE 10", "4 CAJAS DE 100", "9 PAQUETES DE 10", "2 CAJAS DE 100"], ["POR 10", "POR 100"],
           {"6 PAQUETES DE 10": "POR 10", "4 CAJAS DE 100": "POR 100", "9 PAQUETES DE 10": "POR 10", "2 CAJAS DE 100": "POR 100"}, "PAQUETES DE 10, CAJAS DE 100.", n="analizar", **NEU("¿QUÉ CUENTA HACES?")),
      MC("SOFI TIENE 5 PAQUETES DE 10 Y DICE QUE SON 15. ¿QUÉ HIZO MAL?", ["SUMÓ EN VEZ DE MULTIPLICAR", "NADA, ESTÁ BIEN", "PUSO DOS CEROS"], "SUMÓ EN VEZ DE MULTIPLICAR", "5 × 10 = 50.", n="error")],
"5": [N("RELÁMPAGO. ¿CUÁNTO ES 9 × 10?", 90, "UN CERO AL FINAL.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿CUÁNTO ES 4 × 100?", 400, "DOS CEROS AL FINAL.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿CUÁNTO ES 12 × 10?", 120, "LAS CIFRAS SE CORREN UN LUGAR.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁNTOS CEROS VAN EN × 10?", ["UNO", "DOS"], "UNO", "10 TIENE UN CERO.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 6 × 10?", 60, "UN CERO AL FINAL.", n="aplicar")],
 [1, N("¿CUÁNTO ES 9 × 10?", 90, "UN CERO AL FINAL.", n="aplicar")],
 [1, MC("LEO DICE QUE 7 × 10 = 17. ¿CUÁNTO ES?", ["70", "17", "710"], "70", "SE AGREGA UN CERO, NO SE SUMA.", n="error")],
 [2, N("¿CUÁNTO ES 5 × 100?", 500, "DOS CEROS AL FINAL.", n="aplicar")],
 [2, MC("PARA MULTIPLICAR POR 100 AGREGAMOS…", ["DOS CEROS", "UN CERO", "UN 100"], "DOS CEROS", "100 TIENE DOS CEROS.", n="recordar")],
 [2, N("¿CUÁNTO ES 8 × 100?", 800, "DOS CEROS AL FINAL.", n="aplicar")],
 [3, N("¿CUÁNTO ES 41 × 10?", 410, "LAS CIFRAS SE CORREN UN LUGAR.", n="aplicar")],
 [3, TF("AL MULTIPLICAR POR 10, LAS CIFRAS SE CORREN UN LUGAR.", "VERDADERO", "Y ATRÁS VA UN CERO.", n="recordar")],
 [3, MC("MICA DICE QUE 3 × 100 = 30. ¿CUÁNTO ES?", ["300", "30", "103"], "300", "POR 100 SON DOS CEROS.", n="error")],
 [4, N("[[problema]] HAY 7 PAQUETES Y CADA UNO TIENE 10 CARAMELOS. ¿CUÁNTOS CARAMELOS HAY?", 70, "7 × 10 = 70.", n="analizar")],
 [4, N("[[problema]] HAY 2 CAJAS Y CADA UNA TIENE 100 LÁPICES. ¿CUÁNTOS LÁPICES HAY?", 200, "2 × 100 = 200.", n="analizar")],
 [4, MC("6 CAJAS DE 100. ¿QUÉ CUENTA SIRVE?", ["6 × 100", "6 + 100", "6 × 10"], "6 × 100", "SON CAJAS DE 100.", n="aplicar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 15, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: multiplicar por 10 y por 100", "examen_titulo": "Nivel jefe: multiplicar por 10 y por 100",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-15.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
