# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 10 · Restas con algoritmo. Genera mision-10.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (cajas de 100, paquetes de 10 y sueltos que se venden).
Niveles: 1 restar en columnas · 2 restas sin canje · 3 restas con canje · 4 controlar una resta con la suma."""
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
UNI = lambda p, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": [a for a, _ in pares], "derecha": [b for _, b in pares]}, "r": {"pares": dict(pares)}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a armar una resta en columnas.",
"vas_a_ver": ["El número grande arriba", "Cada cifra en su columna", "Empezar por las unidades"],
"secciones": [
 S(1, "El grande arriba", [
  P("Rosa tenía 576 alfajores. Vendió 234."),
  D("Restar en columnas", "El número <b>más grande</b> va arriba. Cada cifra en su columna."),
  IMG("La resta armada", "576 arriba, 234 abajo.", FG.columnas(576, 234, "−")),
 ]),
 S(1, "Empezar por las unidades", [
  P("Unidades: 6 − 4 = <b>2</b>. Decenas: 7 − 3 = <b>4</b>."),
  P("Centenas: 5 − 2 = <b>3</b>. Quedan <b>342</b>."),
  IMG("El resultado", "576 − 234 = 342.", FG.columnas(576, 234, "−", 342)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la resta. La vas a usar en la carpeta."),
  IMG("Resta para resolver", "Empezá por las unidades.", FG.columnas(487, 53, "−", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "368 − 45", "planteo": "Restá en columnas.", "pasos": ["Unidades: 8 − 5 = 3.", "Decenas: 6 − 4 = 2.", "Centenas: 3.", "Resultado: 323."]},
"ejemplo_incompleto": {"titulo": "259 − 34", "planteo": "Completá.", "pasos": ["Unidades: 9 − 4 = ___ .", "Decenas: 5 − 3 = ___ .", "Resultado: ___ ."]},
"ejemplo_solo": {"titulo": "Tu resta", "planteo": "Armá y resolvé 675 − 52."},
"tip": {"titulo": "Arriba el grande", "texto": "Siempre restamos el de abajo al de arriba."},
"ojo": ["El 53 va debajo del 87, no del 48.", "En la resta no se suma: se saca."],
"resumen": [{"titulo": "Arriba", "texto": "El número grande."}, {"titulo": "Columnas", "texto": "U con U, D con D."}, {"titulo": "Empezar", "texto": "Por las unidades."}],
"glosario": [{"palabra": "Resta", "significado": "Sacar una cantidad de otra."}, {"palabra": "Diferencia", "significado": "El resultado de la resta."}],
"carpeta": ["En la resta, ¿cuánto dan las unidades: 7 − 3?", "¿Cuánto dan las decenas: 8 − 5?", "¿Cuánto es 487 − 53?"],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"respuestas_carpeta": [["4"], ["3"], ["434"]],
"soluciones": {"incompleto": "5. 2. 225.", "solo": "623.", "carpeta": ["4.", "3.", "434."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a resolver restas en columnas de tres cifras.",
"vas_a_ver": ["Restar columna por columna", "Cuando da cero", "Restas de tres cifras"],
"secciones": [
 S(1, "Columna por columna", [
  P("Rosa tenía 865 alfajores. Vendió 432."),
  P("Unidades: 5 − 2 = 3. Decenas: 6 − 3 = 3. Centenas: 8 − 4 = 4."),
  IMG("865 − 432", "Resultado: 433.", FG.columnas(865, 432, "−", 433)),
 ]),
 S(1, "Cuando da cero", [
  D("El cero", "Si los dos números son iguales, queda <b>0</b>: 7 − 7 = 0."),
  P("579 − 274: decenas 7 − 7 = <b>0</b>. Quedan <b>305</b>."),
  IMG("579 − 274", "El 0 guarda el lugar de las decenas.", FG.columnas(579, 274, "−", 305)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la resta. La vas a usar en la carpeta."),
  IMG("Resta para resolver", "Columna por columna.", FG.columnas(796, 352, "−", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "684 − 251", "planteo": "Restá en columnas.", "pasos": ["Unidades: 4 − 1 = 3.", "Decenas: 8 − 5 = 3.", "Centenas: 6 − 2 = 4.", "Resultado: 433."]},
"ejemplo_incompleto": {"titulo": "958 − 316", "planteo": "Completá.", "pasos": ["Unidades: 8 − 6 = ___ .", "Decenas: 5 − 1 = ___ .", "Centenas: 9 − 3 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu resta", "planteo": "Resolvé 747 − 325."},
"tip": {"titulo": "Una columna por vez", "texto": "Terminá una antes de pasar a la otra."},
"ojo": ["7 − 7 es 0, no 7.", "No restes el de arriba al de abajo."],
"resumen": [{"titulo": "Unidades", "texto": "Primero."}, {"titulo": "Decenas", "texto": "Después."}, {"titulo": "Centenas", "texto": "Al final."}],
"glosario": [{"palabra": "Minuendo", "significado": "El número de arriba."}, {"palabra": "Sustraendo", "significado": "El número que restamos."}],
"carpeta": ["En 796 − 352, ¿cuánto dan las unidades?", "¿Cuánto es 796 − 352?", "Sofi hizo 579 − 274 y le dio 35. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["4"], ["444"], ["305"]],
"soluciones": {"incompleto": "2. 4. 6.", "solo": "422.", "carpeta": ["4.", "444.", "305: se olvidó el 0 de las decenas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a restar cuando arriba hay menos que abajo.",
"vas_a_ver": ["Cuando no alcanza", "Abrir un paquete", "El canje"],
"secciones": [
 S(1, "Cuando no alcanza", [
  P("Rosa tiene 352 alfajores. Vende 128."),
  P("Unidades: 2 − 8. ¡No alcanza! Tiene 2 sueltos y necesita 8."),
  IMG("352 alfajores", "3 cajas, 5 paquetes y 2 sueltos.", FG.bloques(3, 5, 2)),
 ]),
 S(1, "El canje", [
  D("Canje", "Abro <b>un paquete</b>: quedan 4 paquetes y <b>12 sueltos</b>."),
  P("12 − 8 = 4. Decenas: 4 − 2 = 2. Centenas: 3 − 1 = 2. Quedan <b>224</b>."),
  IMG("352 − 128", "El 5 pasa a 4 y el 2 pasa a 12.", FG.columnas(352, 128, "−", 224, marcas=[("U", "12")], tachar=[("D", "4")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la resta. La vas a usar en la carpeta."),
  IMG("Resta para resolver", "¿Alcanza en las unidades?", FG.columnas(463, 247, "−", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "541 − 316", "planteo": "Restá en columnas.", "pasos": ["1 − 6 no alcanza: abro un paquete.", "El 4 pasa a 3. El 1 pasa a 11.", "11 − 6 = 5. 3 − 1 = 2. 5 − 3 = 2.", "Resultado: 225."]},
"ejemplo_incompleto": {"titulo": "372 − 145", "planteo": "Completá.", "pasos": ["2 − 5 no alcanza: el 7 pasa a ___ .", "El 2 pasa a ___ . 12 − 5 = ___ .", "Resultado: ___ ."]},
"ejemplo_solo": {"titulo": "Tu resta", "planteo": "Resolvé 650 − 234."},
"tip": {"titulo": "Mirá antes de restar", "texto": "Si arriba hay menos, abrí un paquete."},
"ojo": ["No des vuelta: 2 − 8 no es 8 − 2.", "Si abriste un paquete, hay uno menos."],
"resumen": [{"titulo": "No alcanza", "texto": "Arriba hay menos."}, {"titulo": "Canje", "texto": "Abro un paquete: 10 sueltos."}, {"titulo": "Después", "texto": "Hay un paquete menos."}],
"glosario": [{"palabra": "Canje", "significado": "Cambiar 1 paquete por 10 sueltos."}, {"palabra": "Desagrupar", "significado": "Abrir un paquete."}],
"carpeta": ["En 463 − 247, ¿alcanza 3 para restar 7?", "Después del canje, ¿cuánto es 13 − 7?", "Tomi hizo 352 − 128 y le dio 236. ¿Cuánto da?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [["no"], ["6"], ["224"]],
"soluciones": {"incompleto": "6. 12. 7. 227.", "solo": "416.", "carpeta": ["No: hay que abrir un paquete.", "6. Resultado: 216.", "224: Tomi dio vuelta 2 − 8."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a controlar una resta con una suma.",
"vas_a_ver": ["La suma deshace la resta", "Sumar para controlar", "Encontrar errores"],
"secciones": [
 S(1, "La suma deshace la resta", [
  P("Rosa tenía 352. Vendió 128. Le quedan 224."),
  D("Controlar", "Si sumo lo que quedó y lo que vendí, vuelvo al <b>principio</b>."),
  P("224 + 128 = <b>352</b>. ¡La resta está bien!"),
  IMG("Para controlar", "224 + 128 = 352.", FG.columnas(224, 128, "+", 352, marcas=[("D", "1")])),
 ]),
 S(1, "Encontrar un error", [
  P("Tomi hizo 463 − 247 = 226."),
  P("Controla: 226 + 247 = 473. ¡No da 463! Hay un error."),
  IMG("El control", "La suma no vuelve al principio.", FG.cuentas([("463 − 247", 226), ("226 + 247", 473)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las restas. Las vas a usar en la carpeta."),
  IMG("¿Están bien?", "Controlá con una suma.", FG.cuentas([("685 − 243", 442), ("530 − 210", 310), ("472 − 158", 314)])),
 ]),
],
"ejemplo_completo": {"titulo": "Controlar 576 − 234", "planteo": "La resta dio 342.", "pasos": ["Sumo 342 + 234.", "Da 576.", "¡Es el número de arriba: está bien!"]},
"ejemplo_incompleto": {"titulo": "Controlar 865 − 432", "planteo": "Dio 433. Completá.", "pasos": ["433 + 432 = ___ .", "¿Volvió al 865? ___ ."]},
"ejemplo_solo": {"titulo": "¿Está bien?", "planteo": "Alguien hizo 700 − 300 = 300. Controlá con una suma."},
"tip": {"titulo": "Volver al principio", "texto": "Resultado + lo que restaste = el de arriba."},
"ojo": ["Se suma el resultado con el de abajo.", "Si no vuelve al principio, hay un error."],
"resumen": [{"titulo": "Controlar", "texto": "Con una suma."}, {"titulo": "Sumar", "texto": "Resultado + lo que restaste."}, {"titulo": "Comparar", "texto": "Con el de arriba."}],
"glosario": [{"palabra": "Controlar", "significado": "Revisar si está bien."}, {"palabra": "Deshacer", "significado": "Volver a como estaba."}],
"carpeta": ["Controlá 685 − 243 = 442. ¿Cuánto es 442 + 243?", "¿Cuál de las restas está mal?", "¿Cuánto es de verdad 530 − 210?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["685"], ["530 − 210", "530 - 210", "la del medio", "la segunda"], ["320"]],
"soluciones": {"incompleto": "865. Sí.", "solo": "Está mal: 300 + 300 = 600. Da 400.", "carpeta": ["685: está bien.", "530 − 210: 310 + 210 = 520.", "320."]},
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
 T("EL GRANDE ARRIBA", [LD("ARMAR LA RESTA", "EN LA RESTA PONEMOS <b>ARRIBA EL MÁS GRANDE</b> Y ABAJO LO QUE SACAMOS."),
   LL("UNIDADES DEBAJO DE UNIDADES.", "576 − 234: EL 576 VA ARRIBA.")],
   {"modo": "columna", "op": "resta"}, {"modo": "columna", "op": "resta"}),
 T("EMPEZAR POR LAS UNIDADES", [LD("DE DERECHA A IZQUIERDA", "RESTAMOS PRIMERO LAS <b>UNIDADES</b>, DESPUÉS DECENAS Y CENTENAS."),
   LL("487 − 53: 7 − 3, 8 − 5, 4.", "DA 434.")],
   {"modo": "columna", "op": "resta"}, {"modo": "columna", "op": "resta"}),
], "recuerda": [
 RC("ARRIBA EL GRANDE", "DEL NÚMERO DE ARRIBA SACAMOS EL DE ABAJO.", "576 − 234"),
 RC("EL ORDEN", "RESTAMOS DE DERECHA A IZQUIERDA.", "576 − 234 = 342"),
]}

N2["leccion"] = {"temas": [
 T("COLUMNA POR COLUMNA", [LD("TRES CIFRAS", "CON TRES CIFRAS RESTAMOS <b>TRES COLUMNAS</b>, CADA UNA POR SEPARADO."),
   LL("796 − 352 = 444.", "865 − 432 = 433.")],
   {"modo": "columna", "op": "resta"}, {"modo": "columna", "op": "resta"}),
 T("CUANDO DA CERO", [LD("EL CERO", "SI UNA COLUMNA <b>DA 0</b>, ESCRIBIMOS EL 0 PARA GUARDAR EL LUGAR."),
   LL("579 − 274 = 305.", "NO ES 35.")],
   {"modo": "columna", "op": "resta"}, {"modo": "columna", "op": "resta"}),
], "recuerda": [
 RC("COLUMNA POR COLUMNA", "RESTAMOS UNIDADES, DECENAS Y CENTENAS POR SEPARADO.", "796 − 352 = 444"),
 RC("EL CERO", "SI UNA COLUMNA DA CERO, LO ESCRIBIMOS.", "579 − 274 = 305"),
]}

N3["leccion"] = {"temas": [
 T("CUANDO NO ALCANZA", [LD("NO ALCANZA", "SI ARRIBA HAY <b>MENOS</b> QUE ABAJO, NO PODEMOS RESTAR TODAVÍA."),
   LL("EN 352 − 128: 2 − 8 NO ALCANZA.", "NO SE HACE 8 − 2.")],
   {"modo": "columna", "op": "resta", "lleva": True}, {"modo": "columna", "op": "resta", "lleva": True}),
 T("ABRIR UN PAQUETE", [LD("EL CANJE", "<b>ABRIMOS UN PAQUETE</b> DE AL LADO: SON 10 SUELTOS MÁS, Y AL PAQUETE LE QUEDA UNO MENOS."),
   LL("12 − 8 = 4.", "352 − 128 = 224.")],
   {"modo": "columna", "op": "resta", "lleva": True}, {"modo": "columna", "op": "resta", "lleva": True}),
], "recuerda": [
 RC("NO ALCANZA", "SI ARRIBA HAY MENOS, NO RESTAMOS AL REVÉS.", "2 − 8 NO ALCANZA"),
 RC("EL CANJE", "UN PAQUETE SE CAMBIA POR 10 SUELTOS.", "463 − 247 = 216"),
]}

N4["leccion"] = {"temas": [
 T("LA SUMA DESHACE LA RESTA", [LD("CONTROLAR", "PARA <b>CONTROLAR</b> UNA RESTA, SUMAMOS EL RESULTADO Y LO QUE RESTAMOS."),
   LL("685 − 243 = 442.", "442 + 243 = 685: ¡ESTÁ BIEN!")],
   {"modo": "columna", "lleva": False}, {"modo": "columna", "op": "resta", "que": "control"}),
 T("ENCONTRAR ERRORES", [LD("ERRORES", "SI LA SUMA <b>NO DA</b> EL NÚMERO DE ARRIBA, LA RESTA ESTÁ MAL."),
   LL("463 − 247 = 226: 226 + 247 = 473.", "NO DA 463: HAY UN ERROR.")],
   {"modo": "columna", "op": "resta", "lleva": True}, {"modo": "columna", "op": "resta", "que": "control"}),
], "recuerda": [
 RC("CONTROLAR", "SUMAMOS EL RESULTADO Y LO QUE RESTAMOS.", "224 + 128 = 352"),
 RC("ERRORES", "SI LA SUMA NO DA EL NÚMERO DE ARRIBA, HAY UN ERROR.", "226 + 247 ≠ 463"),
]}

ACT = {
"1": [N("RESTÁ EN COLUMNAS: 576 − 234", 342, "U: 6 − 4. D: 7 − 3. C: 5 − 2.", n="aplicar"),
      MC("EN UNA RESTA, ¿QUÉ NÚMERO VA ARRIBA?", ["EL MÁS GRANDE", "EL MÁS CHICO", "EL QUE SE VENDIÓ"], "EL MÁS GRANDE", "DE ÉL SACAMOS.", n="analizar"),
      FB("COMPLETÁ: 487 − 53 = ___", [["434"]], "7 − 3 = 4, 8 − 5 = 3, 4.", n="aplicar"),
      MC("LEO PUSO EL 53 DEBAJO DEL 48 EN 487 − 53. ¿QUÉ HIZO MAL?", ["NO ALINEÓ LAS UNIDADES", "NADA, ESTÁ BIEN", "PUSO EL GRANDE ARRIBA"], "NO ALINEÓ LAS UNIDADES", "EL 3 VA DEBAJO DEL 7.", n="error")],
"2": [N("¿CUÁNTO ES 865 − 432?", 433, "COLUMNA POR COLUMNA.", n="aplicar"),
      UNIR("UNÍ CADA RESTA CON SU RESULTADO.", ["865 − 432", "579 − 274", "796 − 352"], ["444", "433", "305"], {"865 − 432": "433", "579 − 274": "305", "796 − 352": "444"}, "COLUMNA POR COLUMNA.", n="aplicar"),
      MC("SOFI HIZO 579 − 274 Y LE DIO 35. ¿CUÁNTO DA?", ["305", "35", "350"], "305", "LAS DECENAS DAN 0: SE ESCRIBE.", n="error"),
      N("[[problema]] EN UN COLEGIO HABÍA 685 LIBROS Y SE PRESTARON 243. ¿CUÁNTOS LIBROS QUEDAN?", 442, "685 − 243 = 442.", n="analizar", **NEU("EN UNA ESCUELA HABÍA 685 LIBROS Y SE PRESTARON 243. ¿CUÁNTOS LIBROS QUEDAN?"))],
"3": [N("¿CUÁNTO ES 352 − 128?", 224, "ABRO UN PAQUETE: 12 − 8 = 4.", n="aplicar"),
      MC("EN 352 − 128, 2 − 8 NO ALCANZA. ¿QUÉ HAGO?", ["ABRO UN PAQUETE", "HAGO 8 − 2", "PONGO 0"], "ABRO UN PAQUETE", "CANJE: 1 PAQUETE POR 10 SUELTOS.", n="analizar"),
      FB("COMPLETÁ: 463 − 247 = ___", [["216"]], "13 − 7 = 6, 5 − 4 = 1, 4 − 2 = 2.", n="aplicar"),
      MC("TOMI HIZO 352 − 128 Y LE DIO 236. ¿CUÁNTO DA?", ["224", "236", "230"], "224", "NO SE HACE 8 − 2: SE ABRE UN PAQUETE.", n="error")],
"4": [N("224 + 128 = ___", 352, "VUELVE AL NÚMERO DE ARRIBA.", n="aplicar"),
      TF("TOMI HIZO 463 − 247 = 226. ESTÁ BIEN.", "FALSO", "226 + 247 = 473, NO 463.", n="error"),
      CLAS("CONTROLÁ CON UNA SUMA. ¿ESTÁ BIEN O MAL?", ["685 − 243 = 442", "530 − 210 = 310", "796 − 352 = 444", "463 − 247 = 226"], ["BIEN", "MAL"],
           {"685 − 243 = 442": "BIEN", "530 − 210 = 310": "MAL", "796 − 352 = 444": "BIEN", "463 − 247 = 226": "MAL"}, "SUMÁ EL RESULTADO Y LO QUE RESTÁS.", n="analizar"),
      N("¿CUÁNTO ES DE VERDAD 530 − 210?", 320, "320 + 210 = 530.", n="aplicar")],
"5": [N("RELÁMPAGO. 759 − 314 = ___", 445, "SIN CANJE.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. 5 − 9: ¿ALCANZA?", ["NO", "SÍ"], "NO", "HAY QUE ABRIR UN PAQUETE.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 15 − 9 = ___", 6, "DESPUÉS DEL CANJE.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 300 + 200 = ___ (CONTROL DE 500 − 200)", 500, "VUELVE AL PRINCIPIO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, N("RESTÁ EN COLUMNAS: 498 − 65", 433, "U: 8 − 5. D: 9 − 6. C: 4.", n="aplicar")],
 [1, MC("¿POR QUÉ COLUMNA SE EMPIEZA A RESTAR?", ["UNIDADES", "CENTENAS", "DECENAS"], "UNIDADES", "DE DERECHA A IZQUIERDA.", n="recordar")],
 [1, TF("SOFI PUSO 234 ARRIBA Y 576 ABAJO. ESTÁ BIEN.", "FALSO", "EL MÁS GRANDE VA ARRIBA.", n="error")],
 [2, N("¿CUÁNTO ES 967 − 523?", 444, "7 − 3, 6 − 2, 9 − 5.", n="aplicar")],
 [2, N("¿CUÁNTO ES 688 − 380?", 308, "8 − 0, 8 − 8, 6 − 3.", n="aplicar")],
 [2, N("¿CUÁNTO ES 745 − 132?", 613, "COLUMNA POR COLUMNA.", n="aplicar")],
 [3, N("¿CUÁNTO ES 463 − 247?", 216, "13 − 7 = 6. 5 − 4 = 1. 4 − 2 = 2.", n="aplicar")],
 [3, N("¿CUÁNTO ES 541 − 316?", 225, "11 − 6 = 5. 3 − 1 = 2. 5 − 3 = 2.", n="aplicar")],
 [3, MC("TOMI HIZO 352 − 128 = 236. ¿QUÉ HIZO MAL?", ["DIO VUELTA 2 − 8", "NADA", "SUMÓ"], "DIO VUELTA 2 − 8", "HAY QUE ABRIR UN PAQUETE.", n="error")],
 [4, N("CONTROLÁ 576 − 234 = 342. ¿CUÁNTO ES 342 + 234?", 576, "VUELVE AL NÚMERO DE ARRIBA.", n="aplicar")],
 [4, TF("530 − 210 = 310 ESTÁ BIEN.", "FALSO", "310 + 210 = 520: DA 320.", n="analizar")],
 [4, MC("PARA CONTROLAR UNA RESTA, ¿QUÉ SUMO?", ["RESULTADO + LO QUE RESTÉ", "LOS DOS DE ARRIBA", "NADA"], "RESULTADO + LO QUE RESTÉ", "ASÍ VUELVO AL PRINCIPIO.", n="analizar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 10, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: restas con algoritmo", "examen_titulo": "Nivel jefe: restas con algoritmo",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
