# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 4 · Comparar y ordenar hasta 1.000. Genera mision-4.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: los pedidos y camiones de la abuela Rosa (igual que clases.py)."""
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
"objetivo": "Vas a comparar números hasta 1.000.",
"vas_a_ver": ["Mayor y menor", "Primero las centenas", "Si empatan, las decenas"],
"secciones": [
 S(1, "¿Cuál pedido es mayor?", [
  P("Rosa recibió dos pedidos: <b>412</b> y <b>398</b>."),
  P("412 tiene 4 cajas. 398 tiene 3 cajas. <b>412 es mayor</b>."),
  IMG("Pedido de 412", "4 cajas, 1 paquete y 2 sueltos.", FG.bloques(4, 1, 2)),
  IMG("Pedido de 398", "3 cajas, 9 paquetes y 8 sueltos.", FG.bloques(3, 9, 8)),
 ]),
 S(1, "Cómo comparar", [
  D("Comparar", "Primero mirá las <b>centenas</b>. Si empatan, las <b>decenas</b>. Si empatan, las <b>unidades</b>."),
  IMG("356 y 372", "Empatan en centenas. 7 decenas es más que 5.", FG.tablero([356, 372])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tablero. Lo vas a usar en la carpeta."),
  IMG("Números para comparar", "Compará de a dos.", FG.tablero([645, 654, 820, 802])),
 ]),
],
"ejemplo_completo": {"titulo": "518 y 581", "planteo": "¿Cuál es mayor?", "pasos": ["Centenas: 5 y 5. Empatan.", "Decenas: 1 y 8. 8 es más.", "581 es mayor."]},
"ejemplo_incompleto": {"titulo": "730 y 703", "planteo": "Completá.", "pasos": ["Centenas: 7 y 7. ___ .", "Decenas: 3 y 0. Gana el ___ .", "El mayor es ___ ."]},
"ejemplo_solo": {"titulo": "299 y 300", "planteo": "¿Cuál es mayor? Explicá por qué."},
"tip": {"titulo": "Mirá las cajas", "texto": "Más cajas de 100, número más grande."},
"ojo": ["No mires solo las unidades.", "Empezá siempre por las centenas."],
"resumen": [{"titulo": "Mayor", "texto": "Tiene más."}, {"titulo": "Menor", "texto": "Tiene menos."}, {"titulo": "Comparar", "texto": "Primero las centenas."}],
"glosario": [{"palabra": "Mayor", "significado": "El número más grande."}, {"palabra": "Menor", "significado": "El número más chico."}],
"carpeta": ["¿Cuál es mayor: 645 o 654?", "¿Cuál es mayor: 820 o 802?", "¿Cuál es menor: 299 o 300?"],
"respuestas_carpeta": [["654"], ["820"], ["299"]],
"soluciones": {"incompleto": "Empatan. 730. 730.", "solo": "300: tiene 3 centenas y 299 tiene 2.", "carpeta": ["654: tiene más decenas.", "820: tiene más decenas.", "299."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ordenar números hasta 1.000.",
"vas_a_ver": ["De menor a mayor", "De mayor a menor", "Mirar primero las centenas"],
"secciones": [
 S(1, "De menor a mayor", [
  P("Rosa tiene camiones desordenados."),
  P("De <b>menor a mayor</b> es del más chico al más grande."),
  IMG("Desordenados", "540, 215, 812 y 270.", FG.camiones([540, 215, 812, 270])),
  IMG("Ordenados", "215, 270, 540 y 812.", FG.camiones([215, 270, 540, 812])),
 ]),
 S(1, "De mayor a menor", [
  D("Mayor a menor", "Es al revés: del <b>más grande</b> al <b>más chico</b>."),
  IMG("De mayor a menor", "950, 905, 590 y 509.", FG.camiones([950, 905, 590, 509])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los camiones. Los vas a usar en la carpeta."),
  IMG("Camiones para ordenar", "Ordenalos en tu carpeta.", FG.camiones([703, 370, 307])),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenar 460, 406, 640", "planteo": "De menor a mayor.", "pasos": ["Centenas: 4, 4 y 6. El 640 va último.", "460 y 406: decenas 6 y 0.", "406, 460, 640."]},
"ejemplo_incompleto": {"titulo": "Ordenar 128, 821, 281", "planteo": "De menor a mayor.", "pasos": ["Primero va el ___ .", "Después el ___ .", "Último el ___ ."]},
"ejemplo_solo": {"titulo": "Al revés", "planteo": "Ordená de mayor a menor: 315, 531, 153."},
"tip": {"titulo": "Buscá el más chico", "texto": "Encontrá el más chico y ponelo primero."},
"ojo": ["No ordenes por la última cifra.", "Mirá primero las centenas."],
"resumen": [{"titulo": "Menor a mayor", "texto": "Del chico al grande."}, {"titulo": "Mayor a menor", "texto": "Del grande al chico."}, {"titulo": "Centenas", "texto": "Se miran primero."}],
"glosario": [{"palabra": "Ordenar", "significado": "Poner uno detrás de otro."}, {"palabra": "Creciente", "significado": "De menor a mayor."}],
"carpeta": ["De menor a mayor, ¿qué camión va primero?", "De menor a mayor, ¿qué camión va último?", "De mayor a menor, ¿qué número va primero: 315, 531 o 153?"],
"respuestas_carpeta": [["307"], ["703"], ["531"]],
"soluciones": {"incompleto": "128. 281. 821.", "solo": "531, 315, 153.", "carpeta": ["307.", "703.", "531."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a reconocer y usar números redondos.",
"vas_a_ver": ["Qué es un número redondo", "Contar de 10 en 10", "Contar de 100 en 100"],
"secciones": [
 S(1, "Números redondos", [
  D("Número redondo", "Es un número que <b>termina en 0</b>: 40, 100, 350."),
  IMG("De 100 en 100", "Todos terminan en 0.", FG.tren_paso(100, 1000, 100)),
 ]),
 S(1, "De 10 en 10", [
  P("Contamos de 10 en 10: <b>410, 420, 430…</b>"),
  IMG("De 10 en 10", "Del 410 al 500.", FG.tren_paso(410, 500, 10)),
  P("El 238 está entre el <b>230</b> y el <b>240</b>."),
  IMG("El 238 en la recta", "Entre dos números redondos.", FG.recta_num(230, 240, [(238, "238")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("¿Qué vagones faltan?", "Contá de 100 en 100.", FG.tren_paso(100, 1000, 100, (400, 800))),
 ]),
],
"ejemplo_completo": {"titulo": "Contar de 10 en 10", "planteo": "Desde el 670.", "pasos": ["670, 680, 690.", "Después del 690 viene el 700.", "¡Todos terminan en 0!"]},
"ejemplo_incompleto": {"titulo": "De 100 en 100", "planteo": "Completá.", "pasos": ["300, 400, ___ , 600.", "700, 800, ___ , 1.000."]},
"ejemplo_solo": {"titulo": "Entre redondos", "planteo": "¿Entre qué números redondos está el 154?"},
"tip": {"titulo": "Mirá el final", "texto": "Si termina en 0, es redondo."},
"ojo": ["347 no es redondo: termina en 7.", "Después del 990 viene el 1.000."],
"resumen": [{"titulo": "Redondo", "texto": "Termina en 0."}, {"titulo": "De 10 en 10", "texto": "410, 420, 430."}, {"titulo": "De 100 en 100", "texto": "100, 200, 300."}],
"glosario": [{"palabra": "Redondo", "significado": "Número que termina en 0."}, {"palabra": "Entre", "significado": "En el medio de dos números."}],
"carpeta": ["¿Qué número falta en el primer vagón vacío?", "¿Qué número falta en el segundo vagón vacío?", "¿Cuál es redondo: 347, 560 o 821?"],
"respuestas_carpeta": [["400"], ["800"], ["560"]],
"soluciones": {"incompleto": "500. 900.", "solo": "Entre el 150 y el 160.", "carpeta": ["400.", "800.", "560."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ubicar números en la recta hasta 1.000.",
"vas_a_ver": ["La recta del 0 al 1.000", "Más a la derecha, más grande", "Entre qué cientos está un número"],
"secciones": [
 S(1, "La ruta de Rosa", [
  P("La recta es como una ruta con un cartel cada 100."),
  IMG("La recta del 0 al 1.000", "300, 650 y 900.", FG.recta_cien([(300, "300"), (650, "650"), (900, "900")])),
 ]),
 S(1, "Entre dos cientos", [
  D("Entre", "El 650 está <b>entre el 600 y el 700</b>."),
  P("En la recta, <b>más a la derecha</b> es más grande."),
  IMG("Saltos en la recta", "Del 520 saltamos 30: llegamos al 550.", FG.recta_num(510, 560, [(520, "520"), (550, "550")], [(520, 550)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la recta. La vas a usar en la carpeta."),
  IMG("¿Dónde está cada número?", "Mirá las marcas.", FG.recta_cien([(200, "A"), (470, "B"), (870, "C")])),
 ]),
],
"ejemplo_completo": {"titulo": "El 470", "planteo": "¿Entre qué cientos está el 470?", "pasos": ["Tiene 4 centenas.", "Está después del 400.", "Está antes del 500.", "Entre el 400 y el 500."]},
"ejemplo_incompleto": {"titulo": "El 830", "planteo": "Completá.", "pasos": ["Está después del ___ .", "Está antes del ___ ."]},
"ejemplo_solo": {"titulo": "Más a la derecha", "planteo": "¿Cuál está más a la derecha: 780 u 870?"},
"tip": {"titulo": "Mirá las centenas", "texto": "Te dicen entre qué cientos está."},
"ojo": ["Más a la derecha es más grande.", "El 1.000 está al final."],
"resumen": [{"titulo": "La recta", "texto": "Del 0 al 1.000."}, {"titulo": "Derecha", "texto": "Más grande."}, {"titulo": "Entre", "texto": "Dos cientos."}],
"glosario": [{"palabra": "Recta numérica", "significado": "Una línea con los números en orden."}, {"palabra": "Derecha", "significado": "Hacia donde los números crecen."}],
"carpeta": ["¿Qué número está en la marca B?", "¿Entre qué cientos está la marca C?", "¿Cuál está más a la derecha: A o C?"],
"respuestas_carpeta": [["470"], ["800 y 900", "entre 800 y 900", "800 900"], ["c"]],
"soluciones": {"incompleto": "800. 900.", "solo": "870: es el mayor.", "carpeta": ["470.", "Entre el 800 y el 900.", "C."]},
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
for _N in (N1, N2, N3, N4): _N["carpeta_nivel"] = ["aplicar", "aplicar", "aplicar"]

N1["leccion"] = {"temas": [
 T("PRIMERO LAS CENTENAS", [LD("COMPARAR", "PARA COMPARAR, MIRÁ PRIMERO LAS <b>CENTENAS</b>: GANA EL QUE TIENE MÁS."),
   LL("412 ES MAYOR QUE 398.", "4 CENTENAS SON MÁS QUE 3.")],
   {"modo": "comparar3"}, {"modo": "comparar3"}),
 T("SI EMPATAN", [LD("EMPATE", "SI LAS CENTENAS SON IGUALES, MIRÁ LAS <b>DECENAS</b>; SI TAMBIÉN EMPATAN, LAS UNIDADES."),
   LL("654 ES MAYOR QUE 645.", "802 ES MENOR QUE 820.")],
   {"modo": "comparar3"}, {"modo": "comparar3"}),
], "recuerda": [
 RC("PRIMERO LAS CENTENAS", "EL QUE TIENE MÁS CENTENAS ES EL MAYOR.", "700 ES MAYOR QUE 699"),
 RC("SI EMPATAN", "MIRAMOS LAS DECENAS Y DESPUÉS LAS UNIDADES.", "372 ES MAYOR QUE 356"),
]}

N2["leccion"] = {"temas": [
 T("DE MENOR A MAYOR", [LD("ORDENAR", "PARA ORDENAR <b>DE MENOR A MAYOR</b>, BUSCÁ EL MÁS CHICO Y SEGUÍ."),
   LL("406, 460, 640.", "MIRÁ PRIMERO LAS CENTENAS.")],
   {"modo": "orden3"}, {"modo": "orden3"}),
 T("DE MAYOR A MENOR", [LD("AL REVÉS", "<b>DE MAYOR A MENOR</b> EMPEZAMOS POR EL MÁS GRANDE."),
   LL("531, 315, 153.", "ES LA LISTA DADA VUELTA.")],
   {"modo": "orden3", "orden": "desc"}, {"modo": "orden3", "orden": "desc"}),
], "recuerda": [
 RC("DE MENOR A MAYOR", "DEL MÁS CHICO AL MÁS GRANDE.", "128, 281, 821"),
 RC("DE MAYOR A MENOR", "DEL MÁS GRANDE AL MÁS CHICO.", "821, 281, 128"),
]}

N3["leccion"] = {"temas": [
 T("NÚMEROS REDONDOS", [LD("REDONDOS", "UN NÚMERO <b>REDONDO</b> TERMINA EN 0: 240, 560, 700."),
   LL("347 NO ES REDONDO.", "SON FÁCILES PARA CONTAR Y CALCULAR.")],
   {"modo": "serie", "de": 10, "desde": 400, "hasta": 450}, {"modo": "redondos3"}),
 T("DE 10 Y DE 100", [LD("SALTOS REDONDOS", "CONTANDO <b>DE 10 EN 10</b> O <b>DE 100 EN 100</b> PASAMOS POR NÚMEROS REDONDOS."),
   LL("670, 680, 690, 700.", "700, 800, 900, 1.000.")],
   {"modo": "serie", "de": 100, "desde": 100, "hasta": 500}, {"modo": "serie", "de": 10, "desde": 400, "hasta": 1000}),
], "recuerda": [
 RC("REDONDOS", "SON LOS NÚMEROS QUE TERMINAN EN CERO.", "480 ES REDONDO; 485 NO"),
 RC("SALTOS", "DE 10 EN 10 O DE 100 EN 100 LLEGAMOS A REDONDOS.", "300, 400, 500, 600"),
]}

N4["leccion"] = {"temas": [
 T("LA RECTA DEL 0 AL 1.000", [LD("UBICAR", "PARA UBICAR UN NÚMERO, BUSCÁ SUS <b>CENTENAS</b> EN LA RECTA."),
   LL("EL 470 ESTÁ ENTRE 400 Y 500.", "MÁS A LA DERECHA, MÁS GRANDE.")],
   {"modo": "recta1000"}, {"modo": "recta1000"}),
 T("ENTRE QUÉ CIENTOS", [LD("ENTRE DOS", "CADA NÚMERO ESTÁ <b>ENTRE</b> DOS CIENTOS SEGUIDOS."),
   LL("650 ESTÁ ENTRE 600 Y 700.", "LO DICE LA CIFRA DE LAS CENTENAS.")],
   {"modo": "recta1000"}, {"modo": "recta1000", "que": "entre"}),
], "recuerda": [
 RC("UBICAR", "BUSCAMOS LAS CENTENAS Y AVANZAMOS.", "780 ESTÁ ANTES QUE 870"),
 RC("ENTRE QUÉ CIENTOS", "LA CIFRA DE LAS CENTENAS DICE DESDE DÓNDE.", "650: ENTRE 600 Y 700"),
]}

ACT = {
"1": [MC("¿CUÁL ES MAYOR?", ["518", "581"], "581", "EMPATAN EN CENTENAS. 8 DECENAS ES MÁS QUE 1.", n="aplicar"),
      FB("COMPLETÁ CON EL MENOR DE 700 Y 699: ___", [["699"]], "699 TIENE 6 CENTENAS.", n="aplicar"),
      MC("LEO DICE QUE 398 ES MAYOR QUE 412 PORQUE TIENE UN 9. ¿CUÁL ES MAYOR?", ["412", "398"], "412", "PRIMERO LAS CENTENAS: 4 ES MÁS QUE 3.", n="error"),
      CLAS("¿ES MAYOR O MENOR QUE 500?", ["499", "512", "350", "905"], ["MENOR QUE 500", "MAYOR QUE 500"],
           {"499": "MENOR QUE 500", "512": "MAYOR QUE 500", "350": "MENOR QUE 500", "905": "MAYOR QUE 500"}, "MIRÁ LAS CENTENAS.", n="analizar")],
"2": [MC("DE MENOR A MAYOR, ¿CUÁL VA PRIMERO?", ["460", "406", "640"], "406", "4 CENTENAS Y 0 DECENAS.", n="aplicar"),
      N("DE MAYOR A MENOR: 315, 531, 153. ¿QUÉ NÚMERO VA PRIMERO?", 531, "TIENE 5 CENTENAS.", n="aplicar"),
      ORD("ORDENÁ LOS CAMIONES DE MENOR A MAYOR.", ["734", "347", "473", "374"], ["347", "374", "473", "734"], "MIRÁ CENTENAS Y DESPUÉS DECENAS.", n="aplicar"),
      N("[[problema]] TRES CAMIONES LLEVAN 250, 520 Y 205 CAJAS. ¿CUÁNTAS LLEVA EL QUE MÁS LLEVA?", 520, "520 TIENE 5 CENTENAS.", n="analizar")],
"3": [MC("¿CUÁL ES UN NÚMERO REDONDO?", ["347", "560", "821"], "560", "TERMINA EN 0.", n="recordar"),
      N("¿QUÉ SIGUE? 670, 680, 690, ___", 700, "DE 10 EN 10: 700.", n="aplicar"),
      FB("COMPLETÁ DE 100 EN 100: 300, ___, 500, ___", [["400"], ["600"]], "SUMAMOS UNA CENTENA.", n="aplicar"),
      MC("SOFI CONTÓ DE 10 EN 10: 880, 890, 8100. ¿QUÉ NÚMERO TENÍA QUE ESCRIBIR?", ["900", "8100", "891"], "900", "890 Y 10 MÁS SON 900.", n="error")],
"4": [MC("¿ENTRE QUÉ CIENTOS ESTÁ EL 470?", ["400 Y 500", "300 Y 400", "500 Y 600"], "400 Y 500", "TIENE 4 CENTENAS.", n="aplicar"),
      N("ESTOY EN EL 520 Y SALTO 30 PARA ADELANTE. ¿A QUÉ NÚMERO LLEGO?", 550, "520 + 30 = 550.", n="aplicar"),
      ORD("ORDENÁ COMO ESTÁN EN LA RECTA, DE IZQUIERDA A DERECHA.", ["870", "250", "520"], ["250", "520", "870"], "MÁS A LA DERECHA, MÁS GRANDE.", n="aplicar"),
      MC("JUAN UBICÓ EL 380 ENTRE EL 800 Y EL 900. ¿ENTRE QUÉ CIENTOS VA?", ["300 Y 400", "800 Y 900", "30 Y 40"], "300 Y 400", "380 TIENE 3 CENTENAS.", n="error")],
"5": [MC("RELÁMPAGO. ¿CUÁL ES MAYOR?", ["909", "990"], "990", "9 DECENAS ES MÁS QUE 0.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ES REDONDO?", ["480", "485"], "480", "TERMINA EN 0.", tiempo=30, n="recordar"),
      N("RELÁMPAGO. ¿QUÉ SIGUE? 300, 400, 500, ___", 600, "DE 100 EN 100.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿CUÁL ESTÁ MÁS A LA DERECHA EN LA RECTA: 250 O 520?", 520, "ES EL MAYOR.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿CUÁL ES MAYOR?", ["412", "398"], "412", "TIENE MÁS CENTENAS.", n="aplicar")],
 [1, MC("¿CUÁL ES MAYOR?", ["356", "372"], "372", "EMPATAN EN CENTENAS; 7 DECENAS ES MÁS.", n="aplicar")],
 [1, MC("MICA DICE QUE 810 ES MENOR QUE 801. ¿CUÁL ES MENOR DE VERDAD?", ["801", "810"], "801", "0 DECENAS ES MENOS QUE 1.", n="error")],
 [2, N("DE MENOR A MAYOR: 215, 812, 540. ¿QUÉ NÚMERO VA ÚLTIMO?", 812, "ES EL MÁS GRANDE.", n="aplicar")],
 [2, ORD("ORDENÁ DE MENOR A MAYOR.", ["703", "370", "307"], ["307", "370", "703"], "DEL MÁS CHICO AL MÁS GRANDE.", n="aplicar")],
 [2, MC("¿CUÁL ESTÁ ORDENADO DE MENOR A MAYOR?", ["128, 281, 821", "821, 281, 128", "281, 128, 821"], "128, 281, 821", "DEL MÁS CHICO AL MÁS GRANDE.", n="aplicar")],
 [3, MC("¿CUÁL ES UN NÚMERO REDONDO?", ["204", "240", "241"], "240", "TERMINA EN 0.", n="recordar")],
 [3, N("¿QUÉ SIGUE? 410, 420, 430, ___", 440, "DE 10 EN 10.", n="aplicar")],
 [3, N("¿QUÉ SIGUE? 700, 800, 900, ___", 1000, "DESPUÉS DEL 900 VIENE EL 1.000.", n="aplicar")],
 [4, MC("¿ENTRE QUÉ CIENTOS ESTÁ EL 650?", ["600 Y 700", "500 Y 600", "700 Y 800"], "600 Y 700", "TIENE 6 CENTENAS.", n="aplicar")],
 [4, N("¿CUÁL ESTÁ MÁS A LA DERECHA EN LA RECTA: 780 O 870?", 870, "ES EL MAYOR.", n="aplicar")],
 [4, N("[[problema]] ESTOY EN EL 550 DE LA RECTA Y VUELVO 10 PARA ATRÁS. ¿A QUÉ NÚMERO LLEGO?", 540, "550 − 10 = 540.", n="analizar")],
 [4, MC("EN LA RECTA, ¿CUÁL ESTÁ MÁS CERCA DEL 0?", ["300", "900"], "300", "ES EL MENOR.", n="aplicar")],
]

M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 4, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: comparar y ordenar hasta 1.000", "examen_titulo": "Nivel jefe: comparar y ordenar hasta 1.000",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
