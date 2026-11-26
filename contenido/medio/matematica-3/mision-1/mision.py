# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 1 · Los números hasta 10.000. Genera mision-1.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de lápices de Lola (cajas de 10, cajones de 100 y camiones de 1.000).
Niveles: 1 los miles · 2 hasta 5.000 · 3 hasta 10.000 · 4 leer y escribir números de cuatro cifras."""
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
"objetivo": "Vas a conocer el mil.",
"vas_a_ver": ["Diez cientos", "El mil", "De mil en mil"],
"secciones": [
 S(1, "Diez cientos", [
  P("Lola guarda 100 lápices en cada cajón."),
  P("Diez cajones forman <b>1.000</b>: un camión lleno."),
  IMG("Diez cajones", "10 cajones de 100 = 1.000.", FG.bloques(10, 0, 0, "1.000")),
 ]),
 S(1, "De mil en mil", [
  D("Mil", "Diez cientos forman <b>mil</b>. Se escribe 1.000."),
  P("Contamos: 1.000, 2.000, 3.000…"),
  IMG("De mil en mil", "Cada vagón suma mil.", FG.tren_paso(1000, 5000, 1000)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Tren para completar", "Faltan dos vagones.", FG.tren_paso(1000, 6000, 1000, faltan=(3000, 5000))),
 ]),
],
"ejemplo_completo": {"titulo": "Tres camiones", "planteo": "Hay 3 camiones de 1.000.", "pasos": ["1.000, 2.000, 3.000.", "Son 3.000 lápices."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "De mil en mil.", "pasos": ["4.000, ___ , 6.000.", "7.000, 8.000, ___ ."]},
"ejemplo_solo": {"titulo": "Contá", "planteo": "¿Cuánto son 2 camiones de 1.000?"},
"tip": {"titulo": "Tres ceros", "texto": "Mil tiene tres ceros."},
"ojo": ["1.000 no es 100.", "Diez cientos son mil."],
"resumen": [{"titulo": "Mil", "texto": "Diez cientos."}, {"titulo": "1.000", "texto": "Un camión."}, {"titulo": "Contar", "texto": "De mil en mil."}],
"glosario": [{"palabra": "Mil", "significado": "Diez grupos de cien."}, {"palabra": "Cajón", "significado": "Un grupo de 100."}],
"carpeta": ["En el tren, ¿qué número falta después del 2.000?", "¿Qué número falta después del 4.000?", "Tomi dice que diez cajones de 100 son 100. ¿Cuántos son?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3000", "3.000"], ["5000", "5.000"], ["1000", "1.000"]],
"soluciones": {"incompleto": "5.000. 9.000.", "solo": "2.000.", "carpeta": ["3.000.", "5.000.", "1.000: diez cientos son mil."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar números hasta el 5.000.",
"vas_a_ver": ["Camiones, cajones y cajas", "El cero guarda el lugar", "Del 4.999 al 5.000"],
"secciones": [
 S(1, "Camiones y cajones", [
  P("2 camiones, 3 cajones y 5 lápices."),
  P("2.000 + 300 + 5 = <b>2.305</b>."),
  IMG("2.305", "Dos mil trescientos cinco.", FG.tarjetas([("2.305", "dos mil trescientos cinco")])),
 ]),
 S(1, "Del 4.999 al 5.000", [
  D("Cinco mil", "Después del <b>4.999</b> viene el <b>5.000</b>."),
  P("Se llena otro camión."),
  IMG("Hasta 5.000", "De mil en mil hasta 5.000.", FG.tren_paso(1000, 5000, 1000)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas para completar", "Escribí cómo se lee.", FG.tarjetas([("3.120", "tres mil ciento veinte"), ("4.006", "cuatro mil seis")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Contar el pedido", "planteo": "3 camiones, 4 cajones y 2 lápices.", "pasos": ["3.000 + 400 + 2.", "Son 3.402 lápices."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Contá el pedido.", "pasos": ["4 camiones y 1 cajón: ___ .", "1 camión y 7 lápices: ___ ."]},
"ejemplo_solo": {"titulo": "Tu pedido", "planteo": "2 camiones y 6 cajones. ¿Cuántos lápices?"},
"tip": {"titulo": "Primero los miles", "texto": "Contá primero los camiones."},
"ojo": ["1 camión y 7 lápices es 1.007.", "Después del 4.999 va el 5.000."],
"resumen": [{"titulo": "Miles", "texto": "Van primero."}, {"titulo": "El cero", "texto": "Guarda el lugar."}, {"titulo": "5.000", "texto": "Después del 4.999."}],
"glosario": [{"palabra": "Camión", "significado": "Un grupo de 1.000."}, {"palabra": "Cifra", "significado": "Cada número del 0 al 9."}],
"carpeta": ["¿Cuánto son 3 camiones de 1.000 y 1 cajón de 100?", "¿Cuánto son 4 camiones y 6 lápices sueltos?", "Sofi dice que después del 4.999 viene el 41.000. ¿Qué número viene?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3100", "3.100"], ["4006", "4.006"], ["5000", "5.000"]],
"soluciones": {"incompleto": "4.100. 1.007.", "solo": "2.600.", "carpeta": ["3.100.", "4.006.", "5.000."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a contar hasta el 10.000.",
"vas_a_ver": ["De mil en mil hasta 10.000", "Diez mil tiene cinco cifras", "Del 9.999 al 10.000"],
"secciones": [
 S(1, "Hasta 10.000", [
  P("Diez camiones de 1.000 forman <b>10.000</b>."),
  P("Se lee <b>diez mil</b>."),
  IMG("De mil en mil", "Hasta diez mil.", FG.tren_paso(6000, 10000, 1000)),
 ]),
 S(1, "Cinco cifras", [
  D("Diez mil", "<b>10.000</b> tiene cinco cifras: un 1 y cuatro ceros."),
  P("Después del 9.999 viene el 10.000."),
  IMG("Diez mil", "Diez mil.", FG.tarjetas([("10.000", "diez mil")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Tren para completar", "Faltan dos vagones.", FG.tren_paso(5000, 10000, 1000, faltan=(7000, 10000))),
 ]),
],
"ejemplo_completo": {"titulo": "De mil en mil", "planteo": "Contá desde 7.000.", "pasos": ["7.000, 8.000, 9.000.", "Y después 10.000."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Seguí la serie.", "pasos": ["9.997, 9.998, ___ .", "9.999, ___ ."]},
"ejemplo_solo": {"titulo": "Contá", "planteo": "¿Cuántos camiones de 1.000 hay en 10.000?"},
"tip": {"titulo": "Cinco cifras", "texto": "10.000 tiene cinco cifras."},
"ojo": ["10.000 no tiene cuatro cifras.", "Después del 9.999 va el 10.000."],
"resumen": [{"titulo": "10.000", "texto": "Diez camiones."}, {"titulo": "Cifras", "texto": "Cinco."}, {"titulo": "Antes", "texto": "Va el 9.999."}],
"glosario": [{"palabra": "Diez mil", "significado": "Diez grupos de mil."}, {"palabra": "Serie", "significado": "Números en orden."}],
"carpeta": ["En el tren, ¿qué número falta después del 6.000?", "¿Qué número falta después del 9.000?", "Juan dice que después del 9.999 viene el 9.1000. ¿Qué número viene?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["7000", "7.000"], ["10000", "10.000"], ["10000", "10.000"]],
"soluciones": {"incompleto": "9.999. 10.000.", "solo": "10.", "carpeta": ["7.000.", "10.000.", "10.000."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a leer y escribir números de cuatro cifras.",
"vas_a_ver": ["Miles, cientos, dieces y unidades", "Escribir con cifras", "El cero guarda el lugar"],
"secciones": [
 S(1, "Escribir con cifras", [
  P("Tres mil cuarenta: 3 miles, 0 cientos, 4 dieces y 0."),
  P("Se escribe <b>3.040</b>."),
  IMG("3.040", "Tres mil cuarenta.", FG.tarjetas([("3.040", "tres mil cuarenta")])),
 ]),
 S(1, "El cero guarda el lugar", [
  D("El cero", "Si falta un lugar, va un <b>0</b>: seis mil ocho es 6.008."),
  P("Siempre son cuatro cifras."),
  IMG("Con ceros", "Los ceros guardan el lugar.", FG.tarjetas([("6.008", "seis mil ocho"), ("2.150", "dos mil ciento cincuenta")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas para completar", "Escribí cómo se lee.", FG.tarjetas([("7.205", "siete mil doscientos cinco"), ("5.030", "cinco mil treinta")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Escribir", "planteo": "Escribí cuatro mil quince.", "pasos": ["4 miles, 0 cientos, 1 diez y 5.", "Se escribe 4.015."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí con cifras.", "pasos": ["Dos mil seis: ___ .", "Ocho mil cien: ___ ."]},
"ejemplo_solo": {"titulo": "Leer", "planteo": "¿Cómo se lee 9.090?"},
"tip": {"titulo": "Cuatro cifras", "texto": "Del 1.000 al 9.999 son cuatro cifras."},
"ojo": ["Tres mil cinco es 3.005, no 30005.", "Leé primero los miles."],
"resumen": [{"titulo": "Cuatro cifras", "texto": "M, C, D, U."}, {"titulo": "El cero", "texto": "Guarda el lugar."}, {"titulo": "Leer", "texto": "Primero los miles."}],
"glosario": [{"palabra": "Leer", "significado": "Decir el número con palabras."}, {"palabra": "Escribir", "significado": "Poner el número con cifras."}],
"carpeta": ["Escribí con cifras: siete mil doscientos cinco.", "Escribí con cifras: cinco mil treinta.", "Tomi escribió 30005 para tres mil cinco. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["7205", "7.205"], ["5030", "5.030"], ["3005", "3.005"]],
"soluciones": {"incompleto": "2.006. 8.100.", "solo": "Nueve mil noventa.", "carpeta": ["7.205.", "5.030.", "3.005."]},
}

# ---------- LECCIÓN INTERACTIVA (escrita en sesión, docs/reglas-leccion-interactiva.md, primer ciclo: poco texto, todo visual) ----------
LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("DIEZ CIENTOS", [LD("EL MIL", "<b>DIEZ CAJONES</b> DE 100 FORMAN UN MIL: UN CAMIÓN LLENO."),
   LL("1.000 TIENE TRES CEROS.", "NO ES LO MISMO QUE 100.")],
   {"modo": "miles", "max": 1}, {"modo": "miles", "max": 1}),
 T("DE MIL EN MIL", [LD("CONTAR MILES", "CONTAMOS LOS CAMIONES <b>DE MIL EN MIL</b>: 1.000, 2.000, 3.000."),
   LL("CAMBIA LA CIFRA DE LOS MILES.", "LAS OTRAS QUEDAN EN CERO.")],
   {"modo": "serie", "de": 1000, "desde": 1000, "hasta": 1000}, {"modo": "serie", "de": 1000, "desde": 1000, "hasta": 9000}),
], "recuerda": [
 RC("EL MIL", "DIEZ GRUPOS DE CIEN FORMAN EL MIL.", "10 CAJONES DE 100 = 1.000"),
 RC("DE MIL EN MIL", "SUMAMOS UN CAMIÓN CADA VEZ.", "3.000, 4.000, 5.000"),
]}

N2["leccion"] = {"temas": [
 T("CAMIONES Y CAJONES", [LD("CONTAR TODO", "PRIMERO LOS <b>CAMIONES</b>, DESPUÉS CAJONES, CAJAS Y LÁPICES SUELTOS."),
   LL("2 CAMIONES, 3 CAJONES Y 5: 2.305.", "2.000 + 300 + 5.")],
   {"modo": "miles", "max": 4}, {"modo": "miles", "max": 4}),
 T("DEL 4.999 AL 5.000", [LD("CINCO MIL", "DESPUÉS DEL <b>4.999</b> VIENE EL <b>5.000</b>: OTRO CAMIÓN LLENO."),
   LL("NO ES 41.000.", "SE LEE CINCO MIL.")],
   {"modo": "serie", "de": 1, "desde": 4990, "hasta": 4996}, {"modo": "serie", "de": 1, "desde": 4950, "hasta": 5000}),
], "recuerda": [
 RC("CONTAR TODO", "EMPEZAMOS POR LOS MILES Y SEGUIMOS CON EL RESTO.", "3.000 + 400 + 2 = 3.402"),
 RC("CINCO MIL", "DESPUÉS DEL 4.999 VIENE EL 5.000.", "4.998, 4.999, 5.000"),
]}

N3["leccion"] = {"temas": [
 T("HASTA 10.000", [LD("DIEZ MIL", "<b>DIEZ CAMIONES</b> DE 1.000 FORMAN DIEZ MIL: 10.000."),
   LL("TIENE CINCO CIFRAS.", "UN 1 Y CUATRO CEROS.")],
   {"modo": "serie", "de": 1000, "desde": 6000, "hasta": 6000}, {"modo": "serie", "de": 1000, "desde": 5000, "hasta": 10000}),
 T("DEL 9.999 AL 10.000", [LD("DESPUÉS DEL 9.999", "DESPUÉS DEL <b>9.999</b> VIENE EL <b>10.000</b>."),
   LL("NO ES 9.1000.", "SE LLENA EL DÉCIMO CAMIÓN.")],
   {"modo": "serie", "de": 1, "desde": 9990, "hasta": 9996}, {"modo": "serie", "de": 1, "desde": 9950, "hasta": 10000}),
], "recuerda": [
 RC("DIEZ MIL", "DIEZ GRUPOS DE MIL FORMAN EL 10.000.", "9.000 Y 1.000 MÁS"),
 RC("CINCO CIFRAS", "EL 10.000 TIENE UN 1 Y CUATRO CEROS.", "DESPUÉS DEL 9.999 VIENE EL 10.000"),
]}

N4["leccion"] = {"temas": [
 T("ESCRIBIR CON CIFRAS", [LD("CUATRO CIFRAS", "ESCRIBIMOS <b>MILES, CIENTOS, DIECES Y UNIDADES</b>, EN ESE ORDEN."),
   LL("TRES MIL CUARENTA: 3.040.", "CADA LUGAR LLEVA UNA CIFRA.")],
   {"modo": "miles", "que": "escribir"}, {"modo": "miles", "que": "escribir"}),
 T("LEER CON PALABRAS", [LD("LEER", "PARA LEER, DECIMOS PRIMERO LOS <b>MILES</b> Y DESPUÉS EL RESTO."),
   LL("2.150: DOS MIL CIENTO CINCUENTA.", "6.008: SEIS MIL OCHO.")],
   {"modo": "miles", "que": "escribir"}, {"modo": "miles", "que": "leer"}),
], "recuerda": [
 RC("ESCRIBIR", "MILES, CIENTOS, DIECES Y UNIDADES; EL CERO GUARDA EL LUGAR.", "SEIS MIL OCHO ES 6.008"),
 RC("LEER", "PARA LEER EMPEZAMOS POR LOS MILES.", "2.015 ES DOS MIL QUINCE"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("🚚 ¿CUÁNTOS LÁPICES HAY EN 10 CAJONES DE 100?", 1000, "100, 200… 1.000.", n="aplicar"),
      FB("COMPLETÁ DE MIL EN MIL: 2.000, 3.000, ___, 5.000", [["4.000", "4000"]], "SUMAMOS MIL.", n="aplicar"),
      MC("TOMI DICE QUE DIEZ CAJONES DE 100 SON 100. ¿CUÁNTOS SON?", ["1.000", "100", "110"], "1.000", "DIEZ CIENTOS SON MIL.", n="error"),
      UNIR("UNÍ CADA CANTIDAD DE CAMIONES CON SU NÚMERO.", ["2 CAMIONES", "5 CAMIONES", "8 CAMIONES"], ["8.000", "2.000", "5.000"], {"2 CAMIONES": "2.000", "5 CAMIONES": "5.000", "8 CAMIONES": "8.000"}, "CADA CAMIÓN TIENE 1.000.", n="aplicar")],
"2": [N("2 CAMIONES, 3 CAJONES Y 5 LÁPICES. ¿CUÁNTOS SON?", 2305, "2.000 + 300 + 5 = 2.305.", n="aplicar"),
      MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 4.999?", ["5.000", "41.000", "4.990"], "5.000", "SE LLENA OTRO CAMIÓN.", n="recordar"),
      N("[[problema]] LOLA MANDA 1 CAMIÓN DE 1.000 Y 7 LÁPICES SUELTOS. ¿CUÁNTOS LÁPICES MANDA?", 1007, "1.000 + 7 = 1.007.", n="analizar"),
      ORD("ORDENÁ DE MENOR A MAYOR.", ["4.300", "3.400", "4.030"], ["3.400", "4.030", "4.300"], "PRIMERO LOS MILES, DESPUÉS LOS CIENTOS.", n="aplicar")],
"3": [N("¿CUÁNTOS CAMIONES DE 1.000 HAY EN 10.000?", 10, "1.000, 2.000… 10.000: SON 10.", n="aplicar"),
      FB("COMPLETÁ: 9.997, 9.998, ___, 10.000", [["9.999", "9999"]], "9.998 Y 1 MÁS.", n="aplicar"),
      MC("JUAN DICE QUE DESPUÉS DEL 9.999 VIENE EL 9.1000. ¿QUÉ NÚMERO VIENE?", ["10.000", "9.1000", "9.990"], "10.000", "SE LLENA EL DÉCIMO CAMIÓN.", n="error"),
      CLAS("¿CUÁNTAS CIFRAS TIENE?", ["10.000", "9.999", "1.000", "100"], ["MENOS DE 5", "5 CIFRAS"],
           {"10.000": "5 CIFRAS", "9.999": "MENOS DE 5", "1.000": "MENOS DE 5", "100": "MENOS DE 5"}, "SOLO 10.000 TIENE CINCO CIFRAS.", n="analizar")],
"4": [MC("¿CÓMO SE ESCRIBE TRES MIL CUARENTA?", ["3.040", "3.400", "30.040"], "3.040", "3 MILES, 0 CIENTOS, 4 DIECES Y 0.", n="aplicar"),
      UNIR("UNÍ CADA NÚMERO CON SU NOMBRE.", ["2.015", "2.150", "2.501"], ["DOS MIL QUINIENTOS UNO", "DOS MIL QUINCE", "DOS MIL CIENTO CINCUENTA"], {"2.015": "DOS MIL QUINCE", "2.150": "DOS MIL CIENTO CINCUENTA", "2.501": "DOS MIL QUINIENTOS UNO"}, "MIRÁ DÓNDE ESTÁN LOS CEROS.", n="analizar"),
      FB("ESCRIBÍ CON CIFRAS: SEIS MIL OCHO = ___", [["6.008", "6008"]], "EL CERO GUARDA EL LUGAR.", n="aplicar"),
      MC("TOMI ESCRIBIÓ 30005 PARA TRES MIL CINCO. ¿CÓMO VA?", ["3.005", "30005", "305"], "3.005", "SON CUATRO CIFRAS.", n="error")],
"5": [N("RELÁMPAGO. ¿CUÁNTO SON 4 CAMIONES DE 1.000?", 4000, "4.000.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿QUÉ VIENE DESPUÉS DEL 9.999?", ["10.000", "9.990"], "10.000", "DIEZ MIL.", tiempo=30, n="recordar"),
      N("RELÁMPAGO. 3.000 + 200 + 7 = ___", 3207, "3.207.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. ¿CÓMO SE ESCRIBE CINCO MIL DIEZ?", ["5.010", "5.100"], "5.010", "0 CIENTOS Y 1 DIEZ.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, N("¿CUÁNTOS LÁPICES SON 10 CAJONES DE 100?", 1000, "DIEZ CIENTOS SON MIL.", n="aplicar")],
 [1, FB("COMPLETÁ DE MIL EN MIL: 5.000, 6.000, ___", [["7.000", "7000"]], "SUMAMOS MIL.", n="aplicar")],
 [1, TF("1.000 Y 100 SON EL MISMO NÚMERO.", "FALSO", "1.000 TIENE TRES CEROS.", n="recordar")],
 [2, N("3 CAMIONES, 4 CAJONES Y 2 LÁPICES. ¿CUÁNTOS SON?", 3402, "3.000 + 400 + 2.", n="aplicar")],
 [2, MC("SOFI DICE QUE DESPUÉS DEL 4.999 VIENE EL 41.000. ¿QUÉ VIENE?", ["5.000", "41.000", "4.100"], "5.000", "SE LLENA OTRO CAMIÓN.", n="error")],
 [2, N("[[problema]] UN CAMIÓN LLEVA 2.000 LÁPICES. LE SUMAN 6 CAJONES DE 100. ¿CUÁNTOS LLEVA?", 2600, "2.000 + 600 = 2.600.", n="analizar")],
 [3, N("¿QUÉ SIGUE? 7.000, 8.000, 9.000, ___", 10000, "DIEZ MIL.", n="aplicar")],
 [3, MC("¿CUÁNTAS CIFRAS TIENE 10.000?", ["5", "4", "10"], "5", "UN 1 Y CUATRO CEROS.", n="recordar")],
 [3, N("¿QUÉ NÚMERO VA ANTES DEL 10.000?", 9999, "9.999, 10.000.", n="aplicar")],
 [4, MC("¿CÓMO SE ESCRIBE CUATRO MIL QUINCE?", ["4.015", "4.150", "40.015"], "4.015", "0 CIENTOS, 1 DIEZ Y 5.", n="aplicar")],
 [4, MC("¿CÓMO SE LEE 2.150?", ["DOS MIL CIENTO CINCUENTA", "DOS MIL QUINCE", "VEINTIÚN MIL CINCUENTA"], "DOS MIL CIENTO CINCUENTA", "PRIMERO LOS MILES.", n="recordar")],
 [4, MC("MICA ESCRIBIÓ 7.25 PARA SIETE MIL VEINTICINCO. ¿CÓMO VA?", ["7.025", "7.250", "725"], "7.025", "EL CERO GUARDA EL LUGAR DE LOS CIENTOS.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 1, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: los números hasta 10.000", "examen_titulo": "Nivel jefe: los números hasta 10.000",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
