# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 9 · Quitar y comparar. Genera mision-9.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el picnic de Sofi en la plaza (sigue de la misión 8).
Niveles: 1 sacar elementos · 2 perder y gastar · 3 comparar cantidades · 4 escribir la resta. Todo hasta 10."""
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
"objetivo": "Vas a sacar cosas de un grupo y contar cuántas quedan.",
"vas_a_ver": ["Un grupo de cosas", "Sacar algunas", "Contar las que quedan"],
"secciones": [
 S(1, "Sofi saca manzanas", [
  P("En la canasta hay <b>7</b> manzanas. Sofi saca <b>3</b>."),
  IMG("Sacamos 3", "Quedan 4 manzanas.", FG.sacar("manzana", 7, 3)),
 ]),
 S(1, "Sacar", [
  D("Sacar", "Quitar cosas de un grupo. El grupo se hace <b>más chico</b>."),
  IMG("Pelotas", "Había 5. Sacamos 2. Quedan 3.", FG.sacar("pelota", 5, 2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los vasos. Los vas a usar en la carpeta."),
  IMG("Vasos", "Los tachados se sacan.", FG.sacar("vaso", 8, 3, "¿CUÁNTOS QUEDAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "Estrellas", "planteo": "Hay 6 estrellas. Sacamos 1.", "pasos": ["Tachamos 1 estrella.", "Contamos las otras: 1, 2, 3, 4, 5.", "Quedan 5 estrellas."]},
"ejemplo_incompleto": {"titulo": "Globos", "planteo": "Completá.", "pasos": ["Hay 4 globos. Sacamos 2.", "Quedan ___ globos."]},
"ejemplo_solo": {"titulo": "Tus lápices", "planteo": "Tenés 9 lápices. Prestás 4. ¿Cuántos te quedan?"},
"tip": {"titulo": "Tachá primero", "texto": "Tachá las que sacás. Después contá las otras."},
"ojo": ["No cuentes las tachadas.", "Al sacar, quedan menos."],
"resumen": [{"titulo": "Grupo", "texto": "Lo que había."}, {"titulo": "Sacar", "texto": "Quitar algunas."}, {"titulo": "Quedan", "texto": "Contamos las otras."}],
"glosario": [{"palabra": "Sacar", "significado": "Quitar de un grupo."}, {"palabra": "Quedan", "significado": "Las que no sacamos."}],
"carpeta": ["¿Cuántos vasos había?", "¿Cuántos vasos se sacan?", "¿Cuántos vasos quedan en la mesa ahora?"],
"respuestas_carpeta": [["8"], ["3"], ["5"]],
"soluciones": {"incompleto": "2.", "solo": "5 lápices.", "carpeta": ["8.", "3.", "5."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a resolver problemas de perder y gastar.",
"vas_a_ver": ["Cosas que se pierden", "Cosas que se gastan", "Contar hacia atrás"],
"secciones": [
 S(1, "Se vuelan los globos", [
  P("Sofi tiene <b>6</b> globos. El viento se lleva <b>2</b>."),
  IMG("Se volaron 2", "Le quedan 4 globos.", FG.sacar("globo", 6, 2, "QUEDAN 4")),
 ]),
 S(1, "Gastar", [
  D("Perder y gastar", "Cuando perdemos o gastamos, nos quedan <b>menos</b>."),
  P("Tomi tiene <b>8</b> caramelos. Come <b>3</b>. Contamos para atrás: <b>7, 6, 5</b>."),
  IMG("Caramelos", "Le quedan 5.", FG.sacar("caramelo", 8, 3, "QUEDAN 5")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las estrellas. Las vas a usar en la carpeta."),
  IMG("Estrellas", "Sofi pierde las tachadas.", FG.sacar("estrella", 9, 4, "¿CUÁNTAS QUEDAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "Pelotas", "planteo": "Hay 5 pelotas. Se pierden 2.", "pasos": ["Empezamos en 5.", "Contamos para atrás: 4, 3.", "Quedan 3 pelotas."]},
"ejemplo_incompleto": {"titulo": "Caramelos", "planteo": "Completá.", "pasos": ["Tomi tiene 7. Come 2.", "Para atrás: 6, ___ .", "Le quedan ___ ."]},
"ejemplo_solo": {"titulo": "Figuritas", "planteo": "Tenés 10 figuritas. Regalás 3. ¿Cuántas te quedan?"},
"tip": {"titulo": "Para atrás", "texto": "Contá para atrás desde el número que tenés."},
"ojo": ["Perder y gastar es sacar.", "Al final hay menos que al principio."],
"resumen": [{"titulo": "Perder", "texto": "Se va algo."}, {"titulo": "Gastar", "texto": "Usamos algo."}, {"titulo": "Quedan", "texto": "Menos que antes."}],
"glosario": [{"palabra": "Perder", "significado": "Ya no tener algo."}, {"palabra": "Gastar", "significado": "Usar algo hasta que no está."}],
"carpeta": ["¿Cuántas estrellas tenía Sofi?", "¿Cuántas estrellas perdió?", "¿Cuántas estrellas le quedan a Sofi ahora?"],
"respuestas_carpeta": [["9"], ["4"], ["5"]],
"soluciones": {"incompleto": "5. 5.", "solo": "7 figuritas.", "carpeta": ["9.", "4.", "5."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a comparar dos grupos y ver cuántos más tiene uno.",
"vas_a_ver": ["Unir uno con uno", "Ver lo que sobra", "Cuántos más, cuántos menos"],
"secciones": [
 S(1, "Uno con uno", [
  P("Sofi tiene <b>6</b> pelotas. Tomi tiene <b>4</b> estrellas."),
  IMG("Unimos uno con uno", "Sobran 2 pelotas.", FG.parejas(("pelota", 6), ("estrella", 4), "HAY 2 PELOTAS MÁS")),
 ]),
 S(1, "Cuántos más", [
  D("Comparar", "Ver cuántos <b>más</b> tiene un grupo que el otro."),
  P("6 pelotas y 4 estrellas. Hay <b>2</b> pelotas más. Hay <b>2</b> estrellas menos."),
  IMG("Manzanas de Sofi y Tomi", "Sofi tiene 3 más.", FG.parejas(("manzana", 7), ("manzana", 4), "SOFI TIENE 3 MÁS")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Vasos y chicos", "Uní uno con uno.", FG.parejas(("chico", 5), ("vaso", 8), "¿CUÁNTOS SOBRAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "Manzanas", "planteo": "Sofi tiene 7. Tomi tiene 5.", "pasos": ["Unimos uno con uno.", "Sobran 2 de Sofi.", "Sofi tiene 2 más."]},
"ejemplo_incompleto": {"titulo": "Globos", "planteo": "Completá.", "pasos": ["Sofi tiene 3. Tomi tiene 6.", "Tomi tiene ___ más."]},
"ejemplo_solo": {"titulo": "Tus cosas", "planteo": "Tenés 4 lápices y 9 hojas. ¿Cuántas hojas más tenés?"},
"tip": {"titulo": "Mirá lo que sobra", "texto": "Lo que sobra dice cuántos más hay."},
"ojo": ["Uní de a uno, sin saltear.", "Contá solo lo que sobra."],
"resumen": [{"titulo": "Uno con uno", "texto": "Unimos los grupos."}, {"titulo": "Sobran", "texto": "Los que quedan solos."}, {"titulo": "Más", "texto": "Lo que sobra."}],
"glosario": [{"palabra": "Comparar", "significado": "Ver qué grupo tiene más."}, {"palabra": "Sobrar", "significado": "Quedar sin pareja."}],
"carpeta": ["¿Cuántos chicos hay?", "¿Cuántos vasos hay?", "Cada chico toma un vaso. ¿Cuántos vasos sobran?"],
"respuestas_carpeta": [["5"], ["8"], ["3"]],
"soluciones": {"incompleto": "3.", "solo": "5 hojas más.", "carpeta": ["5.", "8.", "3."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir la resta con números y signos.",
"vas_a_ver": ["El signo −", "Escribir la cuenta", "Leer la resta"],
"secciones": [
 S(1, "El signo menos", [
  D("El signo −", "Se lee <b>menos</b>. Sirve para sacar."),
  IMG("Los signos", "Menos e igual.", FG.tarjetas([("−", "menos"), ("=", "igual")])),
 ]),
 S(1, "Escribir la resta", [
  P("7 manzanas, sacamos 3. Se escribe <b>7 − 3 = 4</b>."),
  IMG("La resta", "7 − 3 = 4.", FG.sacar("manzana", 7, 3, "7 − 3 = 4")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pelotas. Las vas a usar en la carpeta."),
  IMG("Pelotas", "Escribí la resta.", FG.sacar("pelota", 9, 5, "9 − 5 = ?")),
 ]),
],
"ejemplo_completo": {"titulo": "8 y 2", "planteo": "Hay 8 vasos. Sacamos 2.", "pasos": ["Primero el 8.", "Después: − 2.", "8 − 2 = 6."]},
"ejemplo_incompleto": {"titulo": "6 y 4", "planteo": "Completá.", "pasos": ["6 − ___ = ___ ."]},
"ejemplo_solo": {"titulo": "Tu resta", "planteo": "Escribí la resta: 10 globos y se vuelan 3."},
"tip": {"titulo": "Se lee así", "texto": "7 − 3 = 4 se lee siete menos tres igual a cuatro."},
"ojo": ["Primero va lo que había.", "El número grande va primero."],
"resumen": [{"titulo": "−", "texto": "Se lee menos."}, {"titulo": "=", "texto": "Se lee igual."}, {"titulo": "Resta", "texto": "7 − 3 = 4."}],
"glosario": [{"palabra": "Menos (−)", "significado": "El signo de restar."}, {"palabra": "Resta", "significado": "La cuenta de sacar."}],
"carpeta": ["¿Cuántas pelotas había?", "¿Cuántas pelotas se sacan?", "¿Cuánto es 9 − 5?"],
"respuestas_carpeta": [["9"], ["5"], ["4"]],
"soluciones": {"incompleto": "6 − 4 = 2.", "solo": "10 − 3 = 7.", "carpeta": ["9.", "5.", "4."]},
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
 T("SACAR ALGUNAS", [LD("SACAR", "<b>SACAR</b> ES QUITAR COSAS DE UN GRUPO. EL GRUPO SE ACHICA."),
   LL("HABÍA 5 MANZANAS Y SACAMOS 2.", "AHORA HAY MENOS QUE ANTES.")],
   {"modo": "restar", "que": "sacar"}, {"modo": "restar", "que": "sacar"}),
 T("LAS QUE QUEDAN", [LD("QUEDAN", "DESPUÉS DE SACAR, CONTAMOS SOLO LAS COSAS QUE <b>QUEDAN</b>."),
   LL("NO CUENTES LAS QUE SACASTE.", "8 Y SACAMOS 3: QUEDAN 5.")],
   {"modo": "restar", "que": "sacar"}, {"modo": "restar", "que": "sacar"}),
], "recuerda": [
 RC("SACAR", "ES QUITAR COSAS Y EL GRUPO SE ACHICA.", "5 MANZANAS Y SACAMOS 2"),
 RC("QUEDAN", "SON LAS COSAS QUE SIGUEN EN EL GRUPO DESPUÉS DE SACAR.", "QUEDAN 3 MANZANAS"),
]}

N2["leccion"] = {"temas": [
 T("PERDER Y GASTAR", [LD("PERDER", "SI ALGO SE <b>PIERDE</b>, SE GASTA O SE VUELA, NOS QUEDAN MENOS."),
   LL("TENÍA 6 GLOBOS Y SE VOLARON 2.", "COMER CARAMELOS TAMBIÉN ES SACAR.")],
   {"modo": "restar", "que": "sacar"}, {"modo": "restar", "que": "sacar"}),
 T("CONTAR PARA ATRÁS", [LD("PARA ATRÁS", "PODEMOS <b>CONTAR PARA ATRÁS</b> DESDE LO QUE HABÍA, UNO POR CADA COSA QUE SE VA."),
   LL("HABÍA 8 Y SE VAN 3: 7, 6, 5.", "EL ÚLTIMO NÚMERO ES LO QUE QUEDA.")],
   {"modo": "restar", "que": "atras"}, {"modo": "restar", "que": "atras"}),
], "recuerda": [
 RC("PERDER O GASTAR", "SON FORMAS DE SACAR: NOS QUEDAN MENOS.", "9 FIGURITAS Y PIERDO 2"),
 RC("PARA ATRÁS", "CONTAMOS HACIA ATRÁS DESDE LO QUE HABÍA.", "9… 8, 7: QUEDAN 7"),
]}

N3["leccion"] = {"temas": [
 T("UNIR UNO CON UNO", [LD("PAREJAS", "PARA COMPARAR DOS GRUPOS, UNIMOS <b>UNO CON UNO</b>."),
   LL("CADA CHICO CON UN VASO.", "NO HACE FALTA CONTAR TODO.")],
   {"modo": "restar", "que": "comparar"}, {"modo": "restar", "que": "comparar"}),
 T("CUÁNTOS MÁS", [LD("LO QUE SOBRA", "LOS QUE QUEDAN <b>SIN PAREJA</b> DICEN CUÁNTOS MÁS TIENE UN GRUPO."),
   LL("7 PELOTAS Y 4 PELOTAS: SOBRAN 3.", "EL OTRO GRUPO TIENE 3 MENOS.")],
   {"modo": "restar", "que": "comparar"}, {"modo": "restar", "que": "comparar"}),
], "recuerda": [
 RC("UNO CON UNO", "ARMAMOS PAREJAS PARA COMPARAR DOS GRUPOS.", "4 CHICOS Y 6 VASOS"),
 RC("CUÁNTOS MÁS", "SON LOS QUE QUEDAN SIN PAREJA.", "SOBRAN 2 VASOS"),
]}

N4["leccion"] = {"temas": [
 T("EL SIGNO −", [LD("MENOS", "EL SIGNO <b>−</b> SE LEE MENOS Y QUIERE DECIR SACAR."),
   LL("7 − 2 SE LEE SIETE MENOS DOS.", "PRIMERO VA LO QUE HABÍA.")],
   {"modo": "restar", "que": "cuenta"}, {"modo": "restar", "que": "cuenta"}),
 T("ESCRIBIR LA RESTA", [LD("LA CUENTA", "LA RESTA SE ESCRIBE: LO QUE HABÍA, <b>−</b>, LO QUE SACAMOS, <b>=</b>, LO QUE QUEDA."),
   LL("9 − 4 = 5.", "SI SACAMOS TODO, QUEDA 0.")],
   {"modo": "restar", "que": "cuenta"}, {"modo": "restar", "que": "cuenta"}),
], "recuerda": [
 RC("EL SIGNO −", "SE LEE MENOS Y QUIERE DECIR SACAR.", "8 − 3"),
 RC("LA RESTA", "PRIMERO LO QUE HABÍA, DESPUÉS LO QUE SACAMOS Y EL RESULTADO.", "8 − 3 = 5"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("HAY 🍎🍎🍎🍎🍎. SACAMOS 2. ¿CUÁNTAS QUEDAN?", 3, "5 MENOS 2 SON 3.", **A),
      MC("SI SACAMOS COSAS DE UN GRUPO, EL GRUPO…", ["CRECE", "SE ACHICA", "QUEDA IGUAL"], "SE ACHICA", "AL SACAR QUEDAN MENOS.", **RE),
      MC("HABÍA 7 VASOS Y SACAMOS 2. LEO DICE QUE QUEDAN 9. ¿CUÁNTOS QUEDAN DE VERDAD?", ["5", "9", "7"], "5", "AL SACAR QUEDAN MENOS: 5.", **ER),
      UNIR("UNÍ CADA GRUPO CON LO QUE QUEDA.", ["6 Y SACO 1", "4 Y SACO 3", "9 Y SACO 6"], ["3", "5", "1"], {"6 Y SACO 1": "5", "4 Y SACO 3": "1", "9 Y SACO 6": "3"}, "QUEDAN 5, 1 Y 3.", **A)],
"2": [N("SOFI TIENE 6 GLOBOS. SE VUELAN 2. ¿CUÁNTOS LE QUEDAN?", 4, "6… 5, 4.", **A),
      N("TOMI TIENE 8 CARAMELOS. COME 3. ¿CUÁNTOS LE QUEDAN?", 5, "8… 7, 6, 5.", **A),
      FB("CONTÁ PARA ATRÁS DESDE EL 9: 9, 8, ___, 6, ___", [["7"], ["5"]], "9, 8, 7, 6, 5.", **A),
      MC("[[problema]] ANA TENÍA 10 FIGURITAS Y PERDIÓ 4. ¿LE QUEDAN MÁS O MENOS DE 10?", ["MENOS DE 10", "MÁS DE 10", "10"], "MENOS DE 10", "SI PIERDE, LE QUEDAN MENOS: 6.", **AN)],
"3": [N("SOFI TIENE 7 PELOTAS Y TOMI 4. ¿CUÁNTAS MÁS TIENE SOFI?", 3, "UNIMOS UNO CON UNO: SOBRAN 3.", **A),
      MC("⚽⚽⚽⚽⚽ Y ⭐⭐⭐ ¿QUÉ HAY MÁS?", ["PELOTAS", "ESTRELLAS", "HAY IGUAL"], "PELOTAS", "SOBRAN 2 PELOTAS.", **A),
      N("[[problema]] HAY 5 CHICOS Y 8 SILLAS. CADA CHICO SE SIENTA EN UNA. ¿CUÁNTAS SILLAS QUEDAN LIBRES?", 3, "UNA SILLA POR CHICO: SOBRAN 3.", **AN),
      CLAS("¿SOBRAN O FALTAN VASOS?", ["4 CHICOS Y 6 VASOS", "5 CHICOS Y 3 VASOS", "2 CHICOS Y 5 VASOS"], ["SOBRAN VASOS", "FALTAN VASOS"],
           {"4 CHICOS Y 6 VASOS": "SOBRAN VASOS", "5 CHICOS Y 3 VASOS": "FALTAN VASOS", "2 CHICOS Y 5 VASOS": "SOBRAN VASOS"}, "SI HAY MÁS VASOS QUE CHICOS, SOBRAN.", **AN)],
"4": [N("¿CUÁNTO ES 7 − 2?", 5, "7… 6, 5.", **A),
      MC("¿CÓMO SE ESCRIBE 9 VASOS Y SACAMOS 4?", ["9 − 4 = 5", "4 − 9 = 5", "9 + 4 = 5"], "9 − 4 = 5", "PRIMERO LO QUE HABÍA.", **A),
      MC("JUAN ESCRIBIÓ 3 − 8 = 5 PARA 8 GLOBOS QUE PIERDEN 3. ¿CÓMO SE ESCRIBE BIEN?", ["8 − 3 = 5", "3 − 8 = 5", "8 + 3 = 5"], "8 − 3 = 5", "PRIMERO VA LO QUE HABÍA: 8.", **ER),
      UNIR("UNÍ CADA RESTA CON SU RESULTADO.", ["6 − 2", "10 − 7", "5 − 5"], ["0", "4", "3"], {"6 − 2": "4", "10 − 7": "3", "5 − 5": "0"}, "6 − 2 = 4, 10 − 7 = 3 Y 5 − 5 = 0.", **A)],
"5": [N("RELÁMPAGO. ¿CUÁNTO ES 5 − 1?", 4, "5… 4.", tiempo=30, **A),
      N("RELÁMPAGO. HAY 10 GLOBOS. SE VUELAN 3. ¿CUÁNTOS QUEDAN?", 7, "10… 9, 8, 7.", tiempo=30, **A),
      N("RELÁMPAGO. SOFI TIENE 6 Y TOMI 4. ¿CUÁNTOS MÁS TIENE SOFI?", 2, "SOBRAN 2.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿QUÉ SIGNO SE LEE MENOS?", ["−", "+", "="], "−", "EL − ES EL SIGNO DE RESTAR.", tiempo=30, **RE)],
}
EXAMEN = [
 [1, N("HAY 6 MANZANAS. SACAMOS 2. ¿CUÁNTAS QUEDAN?", 4, "6 MENOS 2 SON 4.", **A)],
 [1, MC("SACAR ES…", ["QUITAR COSAS DE UN GRUPO", "PONER MÁS COSAS", "JUNTAR DOS GRUPOS"], "QUITAR COSAS DE UN GRUPO", "AL SACAR QUEDAN MENOS.", **RE)],
 [1, N("⭐⭐⭐⭐⭐⭐⭐⭐ SACAMOS 5. ¿CUÁNTAS QUEDAN?", 3, "8 MENOS 5 SON 3.", **A)],
 [2, N("SOFI TIENE 9 FIGURITAS. PIERDE 2. ¿CUÁNTAS LE QUEDAN?", 7, "9… 8, 7.", **A)],
 [2, N("TOMI TIENE 5 CARAMELOS. COME 4. ¿CUÁNTOS LE QUEDAN?", 1, "5… 4, 3, 2, 1.", **A)],
 [2, FB("CONTÁ PARA ATRÁS: 7, 6, ___, 4", [["5"]], "7, 6, 5, 4.", **A)],
 [3, N("SOFI TIENE 8 GLOBOS Y TOMI 5. ¿CUÁNTOS MÁS TIENE SOFI?", 3, "UNIMOS UNO CON UNO: SOBRAN 3.", **A)],
 [3, MC("🍎🍎🍎 Y 🍎🍎🍎🍎🍎 ¿QUÉ GRUPO TIENE MENOS?", ["EL DE 3", "EL DE 5", "HAY IGUAL"], "EL DE 3", "AL DE 3 LE FALTAN 2.", **A)],
 [3, N("[[problema]] HAY 4 CHICOS Y 6 VASOS. CADA UNO TOMA UN VASO. ¿CUÁNTOS VASOS SOBRAN?", 2, "UN VASO POR CHICO: SOBRAN 2.", **AN)],
 [4, N("¿CUÁNTO ES 8 − 3?", 5, "8… 7, 6, 5.", **A)],
 [4, MC("EL SIGNO − SE LEE…", ["MÁS", "MENOS", "IGUAL"], "MENOS", "ES EL SIGNO DE RESTAR.", **RE)],
 [4, MC("MICA ESCRIBIÓ 6 − 10 = 4 PARA 10 GLOBOS Y SE VUELAN 6. ¿CÓMO SE ESCRIBE BIEN?", ["10 − 6 = 4", "6 − 10 = 4", "10 + 6 = 4"], "10 − 6 = 4", "PRIMERO LO QUE HABÍA.", **ER)],
 [4, N("¿CUÁNTO ES 6 − 6?", 0, "SI SACAMOS TODO, QUEDAN 0.", **A)],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 9, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: quitar y comparar", "examen_titulo": "Nivel jefe: quitar y comparar",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
