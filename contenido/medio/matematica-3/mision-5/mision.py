# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 5 · Sumar con tres y cuatro cifras. Genera mision-5.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la colecta de botellas para reciclar de la escuela de Sofi.
Niveles: 1 sumar redondos · 2 sumar descomponiendo · 3 estimar · 4 sumas de memoria."""
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
"objetivo": "Vas a sumar miles y cientos.",
"vas_a_ver": ["Miles con miles", "Cientos con cientos", "Diez cientos, un mil"],
"secciones": [
 S(1, "Miles con miles", [
  P("Juntaron 2.400 botellas. Llegan 1.300 más."),
  P("Miles: 2 + 1 = 3. Cientos: 4 + 3 = 7. Son <b>3.700</b>."),
  IMG("2.400 + 1.300", "Miles y cientos por separado.", FG.cuentas([("2.000 + 1.000", "3.000"), ("400 + 300", 700)])),
 ]),
 S(1, "Se arma un mil", [
  D("Sumar redondos", "Sumamos <b>miles con miles</b> y <b>cientos con cientos</b>."),
  P("Si los cientos llegan a 10, se arma un mil."),
  IMG("600 + 500", "Once cientos: 1.100.", FG.cuentas([("600 + 500", "1.100"), ("3.600 + 1.500", "5.100")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sumas. Las vas a usar en la carpeta."),
  IMG("Sumas para resolver", "Miles y cientos.", FG.cuentas([("4.200 + 3.500", "7.700"), ("2.800 + 400", "3.200")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Sumar", "planteo": "5.100 + 2.600.", "pasos": ["Miles: 5 + 2 = 7.", "Cientos: 1 + 6 = 7. Da 7.700."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Sumá.", "pasos": ["3.000 + 4.000 = ___", "1.200 + 600 = ___"]},
"ejemplo_solo": {"titulo": "Sumá", "planteo": "¿Cuánto es 6.300 + 2.400?"},
"tip": {"titulo": "Por separado", "texto": "Primero los miles, después los cientos."},
"ojo": ["2.000 + 500 es 2.500, no 7.000.", "Diez cientos forman un mil."],
"resumen": [{"titulo": "Miles", "texto": "Con miles."}, {"titulo": "Cientos", "texto": "Con cientos."}, {"titulo": "10 cientos", "texto": "Un mil."}],
"glosario": [{"palabra": "Sumar", "significado": "Juntar cantidades."}, {"palabra": "Redondo", "significado": "Número que termina en ceros."}],
"carpeta": ["¿Cuánto es 4.200 + 3.500?", "¿Cuánto es 2.800 + 400?", "Tomi dice que 2.000 + 500 = 7.000. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["7700", "7.700"], ["3200", "3.200"], ["2500", "2.500"]],
"soluciones": {"incompleto": "7.000. 1.800.", "solo": "8.700.", "carpeta": ["7.700.", "3.200.", "2.500."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a sumar desarmando los números.",
"vas_a_ver": ["Desarmar los dos números", "Sumar lugar por lugar", "Juntar el resultado"],
"secciones": [
 S(1, "Desarmar", [
  P("Tercero juntó 2.345. Cuarto, 1.432."),
  P("2.345 = 2.000 + 300 + 40 + 5."),
  IMG("Desarmamos", "Cada cifra con su valor.", FG.cuentas([("2.345", "2.000 + 300 + 40 + 5"), ("1.432", "1.000 + 400 + 30 + 2")])),
 ]),
 S(1, "Lugar por lugar", [
  D("Sumar descomponiendo", "Sumamos <b>miles, centenas, decenas y unidades</b> por separado y juntamos."),
  P("3.000 + 700 + 70 + 7 = 3.777."),
  IMG("Lugar por lugar", "Juntamos los resultados.", FG.cuentas([("miles", "3.000"), ("centenas", 700), ("decenas", 70), ("unidades", 7)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sumas. Las vas a usar en la carpeta."),
  IMG("Sumas para resolver", "Desarmá y sumá.", FG.cuentas([("3.214 + 2.563", "5.777"), ("4.105 + 1.372", "5.477")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Sumar", "planteo": "1.623 + 2.154.", "pasos": ["3.000 + 700 + 70 + 7.", "Da 3.777."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "5.241 + 3.506.", "pasos": ["Miles: ___ . Centenas: ___ .", "Decenas: 40. Unidades: 7."]},
"ejemplo_solo": {"titulo": "Sumá", "planteo": "¿Cuánto es 2.031 + 6.425?"},
"tip": {"titulo": "Todos los lugares", "texto": "No te olvides de ningún lugar."},
"ojo": ["Sumá todos los lugares.", "El cero no suma nada."],
"resumen": [{"titulo": "Desarmar", "texto": "Los dos números."}, {"titulo": "Sumar", "texto": "Lugar por lugar."}, {"titulo": "Juntar", "texto": "El resultado."}],
"glosario": [{"palabra": "Descomponer", "significado": "Desarmar en partes."}, {"palabra": "Resultado", "significado": "Lo que da la cuenta."}],
"carpeta": ["¿Cuánto es 3.214 + 2.563?", "¿Cuánto es 4.105 + 1.372?", "Mía dice que 2.345 + 1.432 = 3.000. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["5777", "5.777"], ["5477", "5.477"], ["3777", "3.777"]],
"soluciones": {"incompleto": "8.000. 700.", "solo": "8.456.", "carpeta": ["5.777.", "5.477.", "3.777."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a calcular más o menos cuánto da una suma.",
"vas_a_ver": ["El mil más cercano", "Sumar redondos", "Controlar la cuenta"],
"secciones": [
 S(1, "El mil más cercano", [
  P("3.890 está cerca del <b>4.000</b>."),
  P("2.105 está cerca del <b>2.000</b>."),
  IMG("Cerca del 4.000", "En la recta.", FG.recta_miles([(3890, "3.890")])),
 ]),
 S(1, "Estimar", [
  D("Estimar", "Calcular <b>más o menos</b> cuánto da, con números redondos."),
  P("4.000 + 2.000 = 6.000. Da cerca de 6.000."),
  IMG("Estimamos", "Cerca de 6.000.", FG.cuentas([("3.890 + 2.105", "≈ 6.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sumas. Las vas a usar en la carpeta."),
  IMG("Sumas para estimar", "¿Más o menos cuánto da?", FG.cuentas([("5.120 + 2.940", "8.000"), ("1.980 + 3.050", "5.000")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Estimar", "planteo": "6.950 + 1.100.", "pasos": ["7.000 + 1.000.", "Da cerca de 8.000."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Redondeá al mil.", "pasos": ["4.120 está cerca de ___ .", "5.870 está cerca de ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿2.010 + 2.990 da cerca de 5.000 o de 9.000?"},
"tip": {"titulo": "Para controlar", "texto": "Si la cuenta da muy lejos, hay un error."},
"ojo": ["Estimar no es la cuenta exacta.", "Buscá el mil más cercano."],
"resumen": [{"titulo": "Estimar", "texto": "Más o menos."}, {"titulo": "Redondear", "texto": "Al mil cercano."}, {"titulo": "Sirve", "texto": "Para controlar."}],
"glosario": [{"palabra": "Estimar", "significado": "Calcular más o menos."}, {"palabra": "Cercano", "significado": "Que está a poca distancia."}],
"carpeta": ["¿5.120 + 2.940 da cerca de qué número?", "¿1.980 + 3.050 da cerca de qué número?", "Leo dice que 3.890 + 2.105 da cerca de 9.000. ¿Cerca de cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["8000", "8.000"], ["5000", "5.000"], ["6000", "6.000"]],
"soluciones": {"incompleto": "4.000. 6.000.", "solo": "5.000.", "carpeta": ["8.000.", "5.000.", "6.000."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a sumar miles de memoria.",
"vas_a_ver": ["Amigos del mil", "Dobles", "Miles como unidades"],
"secciones": [
 S(1, "Amigos del mil", [
  P("300 y 700 forman 1.000."),
  P("A 3.600 le faltan <b>400</b> para 4.000."),
  IMG("Amigos del mil", "Suman 1.000.", FG.cuentas([("300 + 700", "1.000"), ("600 + 400", "1.000"), ("800 + 200", "1.000")])),
 ]),
 S(1, "Dobles y miles", [
  D("De memoria", "Los miles se suman <b>como unidades</b>: 4.000 + 3.000 = 7.000."),
  P("El doble de 2.500 es 5.000."),
  IMG("Dobles", "El mismo número dos veces.", FG.cuentas([("2.500 + 2.500", "5.000"), ("1.500 + 1.500", "3.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sumas. Las vas a usar en la carpeta."),
  IMG("Sumas de memoria", "Sin papel.", FG.cuentas([("5.200 + ?", "6.000"), ("3.500 + 3.500", "7.000")], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Completar al mil", "planteo": "¿Cuánto le falta a 2.700 para 3.000?", "pasos": ["7 cientos y 3 cientos forman mil.", "Le faltan 300."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "De memoria.", "pasos": ["5.000 + 4.000 = ___", "4.500 + 4.500 = ___"]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto le falta a 8.100 para 9.000?"},
"tip": {"titulo": "Contá cientos", "texto": "Para llegar al mil, contá los cientos que faltan."},
"ojo": ["A 3.600 le faltan 400, no 600.", "Los miles se suman como unidades."],
"resumen": [{"titulo": "Amigos", "texto": "Suman 1.000."}, {"titulo": "Dobles", "texto": "Dos veces."}, {"titulo": "Miles", "texto": "Como unidades."}],
"glosario": [{"palabra": "Doble", "significado": "Dos veces lo mismo."}, {"palabra": "Memoria", "significado": "Calcular en la cabeza."}],
"carpeta": ["¿Cuánto le falta a 5.200 para 6.000?", "¿Cuánto es 3.500 + 3.500?", "Sofi dice que a 3.600 le faltan 600 para 4.000. ¿Cuánto le falta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["800"], ["7000", "7.000"], ["400"]],
"soluciones": {"incompleto": "9.000. 9.000.", "solo": "900.", "carpeta": ["800.", "7.000.", "400."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("MILES CON MILES", [LD("CADA LUGAR APARTE", "CADA LUGAR SE SUMA CON <b>SU MISMO LUGAR</b> DEL OTRO NÚMERO."),
   LL("EL MIL NO SE JUNTA CON EL CIEN.", "AL TERMINAR, ARMAMOS EL NÚMERO.")],
   {"modo": "sumar4", "que": "redondos"}, {"modo": "sumar4", "que": "redondos"}),
 T("SE ARMA UN MIL", [LD("DIEZ CIENTOS", "SI LOS CIENTOS LLEGAN A <b>10</b>, SE ARMA UN MIL MÁS."),
   LL("600 + 500 = 1.100.", "ONCE CIENTOS: UN MIL Y CIEN.")],
   {"modo": "sumar4", "que": "redondos"}, {"modo": "sumar4", "que": "redondos"}),
], "recuerda": [
 RC("SUMAR REDONDOS", "SUMAMOS CADA LUGAR POR SEPARADO Y DESPUÉS JUNTAMOS.", "5.100 + 2.600 = 7.700"),
 RC("DIEZ CIENTOS", "CUANDO LOS CIENTOS SUMAN DIEZ O MÁS, SE ARMA UN MIL.", "2.800 + 400 = 3.200"),
]}
N2["leccion"] = {"temas": [
 T("DESARMAR Y SUMAR", [LD("SUMAR DESCOMPONIENDO", "DESARMAMOS LOS DOS NÚMEROS Y SUMAMOS <b>LUGAR POR LUGAR</b>."),
   LL("MILES, CENTENAS, DECENAS Y UNIDADES.", "AL FINAL JUNTAMOS TODO.")],
   {"modo": "sumar4", "que": "descomp"}, {"modo": "sumar4", "que": "descomp"}),
 T("JUNTAR EL RESULTADO", [LD("JUNTAR", "SUMAMOS LOS RESULTADOS DE CADA LUGAR: <b>3.000 + 700 + 70 + 7</b>."),
   LL("SI UN LUGAR PASA DE 9, SE ARMA OTRO.", "CONTROLÁ QUE NO FALTE NINGUNO.")],
   {"modo": "sumar4", "que": "descomp"}, {"modo": "sumar4", "que": "descomp"}),
], "recuerda": [
 RC("DESCOMPONER", "PARTIMOS CADA NÚMERO SEGÚN EL VALOR DE SUS CIFRAS.", "1.623 = 1.000 + 600 + 20 + 3"),
 RC("LUGAR POR LUGAR", "SUMAMOS CADA LUGAR Y JUNTAMOS LOS RESULTADOS.", "1.623 + 2.154 = 3.777"),
]}
N3["leccion"] = {"temas": [
 T("EL MIL MÁS CERCANO", [LD("REDONDEAR", "CAMBIAMOS CADA NÚMERO POR EL <b>MIL MÁS CERCANO</b>."),
   LL("3.890 ESTÁ CERCA DEL 4.000.", "2.105 ESTÁ CERCA DEL 2.000.")],
   {"modo": "recta10000"}, {"modo": "recta10000", "que": "entre"}),
 T("ESTIMAR UNA SUMA", [LD("ESTIMAR", "SUMAMOS LOS REDONDOS PARA SABER <b>MÁS O MENOS</b> CUÁNTO DA."),
   LL("SIRVE PARA CONTROLAR LA CUENTA.", "NO ES EL RESULTADO EXACTO.")],
   {"modo": "sumar4", "que": "estimar"}, {"modo": "sumar4", "que": "estimar"}),
], "recuerda": [
 RC("REDONDEAR", "BUSCAMOS EL MIL QUE ESTÁ MÁS CERCA DEL NÚMERO.", "4.120 ESTÁ CERCA DEL 4.000"),
 RC("ESTIMAR", "SUMAMOS REDONDOS PARA SABER MÁS O MENOS CUÁNTO DA.", "6.950 + 1.100 DA CERCA DE 8.000"),
]}
N4["leccion"] = {"temas": [
 T("AMIGOS DEL MIL", [LD("COMPLETAR AL MIL", "BUSCAMOS LOS <b>CIENTOS QUE FALTAN</b> PARA LLEGAR AL MIL."),
   LL("300 Y 700 FORMAN 1.000.", "A 2.700 LE FALTAN 300.")],
   {"modo": "sumar4", "que": "falta1000"}, {"modo": "sumar4", "que": "falta1000"}),
 T("DOBLES CON MILES", [LD("DOBLE", "SUMAMOS EL MISMO NÚMERO <b>DOS VECES</b>: PRIMERO LOS MILES, DESPUÉS LOS CIENTOS."),
   LL("2.500 + 2.500 = 5.000.", "LOS MILES SE SUMAN COMO UNIDADES.")],
   {"modo": "sumar4", "que": "dobles"}, {"modo": "sumar4", "que": "dobles"}),
], "recuerda": [
 RC("AMIGOS DEL MIL", "DOS NÚMEROS QUE JUNTOS FORMAN 1.000.", "800 + 200 = 1.000"),
 RC("DOBLE", "ES SUMAR EL MISMO NÚMERO DOS VECES.", "1.500 + 1.500 = 3.000"),
]}

ACT = {
"1": [N("¿CUÁNTO ES 5.100 + 2.600?", 7700, "MILES Y CIENTOS.", n="aplicar"),
      N("¿CUÁNTO ES 3.600 + 1.500?", 5100, "11 CIENTOS: UN MIL MÁS.", n="analizar"),
      MC("TOMI DICE QUE 2.000 + 500 = 7.000. ¿CUÁNTO ES?", ["2.500", "7.000", "2.005"], "2.500", "MILES CON CIENTOS NO SE MEZCLAN.", n="error"),
      UNIR("UNÍ CADA SUMA CON SU RESULTADO.", ["4.000 + 300", "4.000 + 3.000", "400 + 300"], ["700", "4.300", "7.000"], {"4.000 + 300": "4.300", "4.000 + 3.000": "7.000", "400 + 300": "700"}, "MIRÁ QUÉ LUGARES SE SUMAN.", n="aplicar")],
"2": [N("¿CUÁNTO ES 1.623 + 2.154?", 3777, "3.000 + 700 + 70 + 7.", n="aplicar"),
      FB("COMPLETÁ: 5.241 + 3.506 = 8.000 + ___ + 40 + 7", [["700"]], "200 + 500.", n="aplicar"),
      MC("MÍA DICE QUE 2.345 + 1.432 = 3.000. ¿CUÁNTO ES?", ["3.777", "3.000", "3.700"], "3.777", "FALTAN LOS OTROS LUGARES.", n="error"),
      N("[[problema]] UN GRADO JUNTÓ 2.031 BOTELLAS Y OTRO 6.425. ¿CUÁNTAS JUNTARON?", 8456, "8.000 + 400 + 50 + 6.", n="analizar")],
"3": [MC("¿4.120 ESTÁ MÁS CERCA DE 4.000 O DE 5.000?", ["4.000", "5.000"], "4.000", "SOLO 120 DE DISTANCIA.", n="aplicar"),
      MC("6.950 + 1.100 DA MÁS O MENOS…", ["8.000", "6.000", "10.000"], "8.000", "7.000 + 1.000.", n="aplicar"),
      MC("LEO DICE QUE 3.890 + 2.105 DA CERCA DE 9.000. ¿CERCA DE CUÁNTO DA?", ["6.000", "9.000", "5.000"], "6.000", "4.000 + 2.000.", n="error"),
      CLAS("¿ESTÁ MÁS CERCA DE 3.000 O DE 4.000?", ["3.100", "3.900", "3.300", "3.800"], ["CERCA DE 3.000", "CERCA DE 4.000"], {"3.100": "CERCA DE 3.000", "3.900": "CERCA DE 4.000", "3.300": "CERCA DE 3.000", "3.800": "CERCA DE 4.000"}, "MIRÁ LOS CIENTOS.", n="analizar")],
"4": [N("¿CUÁNTO LE FALTA A 2.700 PARA LLEGAR A 3.000?", 300, "7 CIENTOS Y 3 CIENTOS.", n="aplicar"),
      N("¿CUÁNTO ES 4.500 + 4.500?", 9000, "8.000 + 1.000.", n="aplicar"),
      MC("SOFI DICE QUE A 3.600 LE FALTAN 600 PARA 4.000. ¿CUÁNTO LE FALTA?", ["400", "600", "1.400"], "400", "6 CIENTOS Y 4 CIENTOS.", n="error"),
      UNIR("UNÍ LOS AMIGOS DEL MIL.", ["300", "600", "800"], ["400", "200", "700"], {"300": "700", "600": "400", "800": "200"}, "JUNTOS SUMAN 1.000.", n="analizar")],
"5": [N("RELÁMPAGO. 3.000 + 4.000 = ___", 7000, "7.000.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 1.500 + 1.500 = ___", 3000, "3.000.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿CUÁNTO LE FALTA A 8.100 PARA 9.000?", 900, "900.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿5.120 + 2.940 DA CERCA DE…?", ["8.000", "6.000"], "8.000", "5.000 + 3.000.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 6.300 + 2.400?", 8700, "MILES Y CIENTOS.", n="aplicar")],
 [1, N("¿CUÁNTO ES 2.800 + 400?", 3200, "12 CIENTOS: UN MIL Y 200.", n="analizar")],
 [1, TF("2.000 + 500 = 7.000.", "FALSO", "ES 2.500.", n="error")],
 [2, N("¿CUÁNTO ES 3.214 + 2.563?", 5777, "LUGAR POR LUGAR.", n="aplicar")],
 [2, MC("¿QUÉ SUMA DA 4.105 + 1.372 DESARMADA?", ["5.000 + 400 + 70 + 7", "5.000 + 400 + 7", "4.000 + 1.000"], "5.000 + 400 + 70 + 7", "CADA LUGAR SUMADO.", n="analizar")],
 [2, N("[[problema]] HAY 1.240 BOTELLAS VERDES Y 2.350 BLANCAS. ¿CUÁNTAS HAY?", 3590, "3.000 + 500 + 90.", n="aplicar")],
 [3, MC("¿5.870 ESTÁ MÁS CERCA DE 5.000 O DE 6.000?", ["6.000", "5.000"], "6.000", "FALTAN SOLO 130.", n="aplicar")],
 [3, MC("¿2.010 + 2.990 DA CERCA DE…?", ["5.000", "9.000", "4.000"], "5.000", "2.000 + 3.000.", n="aplicar")],
 [3, MC("ESTIMAR ES…", ["CALCULAR MÁS O MENOS", "HACER LA CUENTA EXACTA", "RESTAR"], "CALCULAR MÁS O MENOS", "CON NÚMEROS REDONDOS.", n="recordar")],
 [4, N("¿CUÁNTO LE FALTA A 5.200 PARA 6.000?", 800, "2 CIENTOS Y 8 CIENTOS.", n="aplicar")],
 [4, N("¿CUÁNTO ES 3.500 + 3.500?", 7000, "6.000 + 1.000.", n="aplicar")],
 [4, MC("NICO DICE QUE 4.000 + 3.000 = 43.000. ¿CUÁNTO ES?", ["7.000", "43.000", "700"], "7.000", "4 MILES Y 3 MILES.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 5, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: sumar con tres y cuatro cifras", "examen_titulo": "Nivel jefe: sumar con tres y cuatro cifras",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
