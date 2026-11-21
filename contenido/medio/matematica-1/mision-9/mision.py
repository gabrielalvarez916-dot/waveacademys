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
"carpeta": ["¿Cuántos vasos había?", "¿Cuántos vasos se sacan?", "¿Cuántos vasos quedan?"],
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
"carpeta": ["¿Cuántas estrellas tenía Sofi?", "¿Cuántas estrellas perdió?", "¿Cuántas estrellas le quedan?"],
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
"ejemplo_solo": {"titulo": "Tus cosas", "planteo": "Tenés 4 lápices y 9 hojas. ¿Cuántas hojas más que lápices?"},
"tip": {"titulo": "Mirá lo que sobra", "texto": "Lo que sobra dice cuántos más hay."},
"ojo": ["Uní de a uno, sin saltear.", "Contá solo lo que sobra."],
"resumen": [{"titulo": "Uno con uno", "texto": "Unimos los grupos."}, {"titulo": "Sobran", "texto": "Los que quedan solos."}, {"titulo": "Más", "texto": "Lo que sobra."}],
"glosario": [{"palabra": "Comparar", "significado": "Ver qué grupo tiene más."}, {"palabra": "Sobrar", "significado": "Quedar sin pareja."}],
"carpeta": ["¿Cuántos chicos hay?", "¿Cuántos vasos hay?", "¿Cuántos vasos más que chicos hay?"],
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

ACT = {
"1": [N("HAY 🍎🍎🍎🍎🍎. SACAMOS 2. ¿CUÁNTAS QUEDAN?", 3, "5 MENOS 2 SON 3."),
      MC("SI SACAMOS COSAS DE UN GRUPO, EL GRUPO…", ["CRECE", "SE ACHICA", "QUEDA IGUAL"], "SE ACHICA", "AL SACAR QUEDAN MENOS.")],
"2": [N("SOFI TIENE 6 GLOBOS. SE VUELAN 2. ¿CUÁNTOS LE QUEDAN?", 4, "6… 5, 4."),
      N("TOMI TIENE 8 CARAMELOS. COME 3. ¿CUÁNTOS LE QUEDAN?", 5, "8… 7, 6, 5.")],
"3": [N("SOFI TIENE 7 PELOTAS Y TOMI 4. ¿CUÁNTAS MÁS TIENE SOFI?", 3, "UNIMOS UNO CON UNO: SOBRAN 3."),
      MC("⚽⚽⚽⚽⚽ Y ⭐⭐⭐ ¿QUÉ HAY MÁS?", ["PELOTAS", "ESTRELLAS", "HAY IGUAL"], "PELOTAS", "SOBRAN 2 PELOTAS.")],
"4": [N("¿CUÁNTO ES 7 − 2?", 5, "7… 6, 5."),
      MC("¿CÓMO SE ESCRIBE 9 VASOS Y SACAMOS 4?", ["9 − 4 = 5", "4 − 9 = 5", "9 + 4 = 5"], "9 − 4 = 5", "PRIMERO LO QUE HABÍA.")],
"5": [N("RELÁMPAGO. ¿CUÁNTO ES 5 − 1?", 4, "5… 4.", tiempo=30),
      N("RELÁMPAGO. HAY 10 GLOBOS. SE VUELAN 3. ¿CUÁNTOS QUEDAN?", 7, "10… 9, 8, 7.", tiempo=30),
      N("RELÁMPAGO. SOFI TIENE 6 Y TOMI 4. ¿CUÁNTOS MÁS TIENE SOFI?", 2, "SOBRAN 2.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ SIGNO SE LEE MENOS?", ["−", "+", "="], "−", "EL − ES EL SIGNO DE RESTAR.", tiempo=30)],
}
EXAMEN = [
 [1, N("HAY 6 MANZANAS. SACAMOS 2. ¿CUÁNTAS QUEDAN?", 4, "6 MENOS 2 SON 4.")],
 [1, MC("SACAR ES…", ["QUITAR COSAS DE UN GRUPO", "PONER MÁS COSAS", "JUNTAR DOS GRUPOS"], "QUITAR COSAS DE UN GRUPO", "AL SACAR QUEDAN MENOS.")],
 [1, N("⭐⭐⭐⭐⭐⭐⭐⭐ SACAMOS 5. ¿CUÁNTAS QUEDAN?", 3, "8 MENOS 5 SON 3.")],
 [2, N("SOFI TIENE 9 FIGURITAS. PIERDE 2. ¿CUÁNTAS LE QUEDAN?", 7, "9… 8, 7.")],
 [2, N("TOMI TIENE 5 CARAMELOS. COME 4. ¿CUÁNTOS LE QUEDAN?", 1, "5… 4, 3, 2, 1.")],
 [2, MC("SI PERDEMOS ALGO, NOS QUEDAN…", ["MÁS", "MENOS", "IGUAL"], "MENOS", "PERDER ES SACAR.")],
 [3, N("SOFI TIENE 8 GLOBOS Y TOMI 5. ¿CUÁNTOS MÁS TIENE SOFI?", 3, "UNIMOS UNO CON UNO: SOBRAN 3.")],
 [3, MC("🍎🍎🍎 Y 🍎🍎🍎🍎🍎 ¿QUÉ GRUPO TIENE MENOS?", ["EL DE 3", "EL DE 5", "HAY IGUAL"], "EL DE 3", "AL DE 3 LE FALTAN 2.")],
 [3, N("HAY 4 CHICOS Y 6 VASOS. ¿CUÁNTOS VASOS SOBRAN?", 2, "UN VASO POR CHICO: SOBRAN 2.")],
 [4, N("¿CUÁNTO ES 8 − 3?", 5, "8… 7, 6, 5.")],
 [4, MC("EL SIGNO − SE LEE…", ["MÁS", "MENOS", "IGUAL"], "MENOS", "ES EL SIGNO DE RESTAR.")],
 [4, MC("¿CÓMO SE ESCRIBE 10 GLOBOS Y SE VUELAN 6?", ["10 − 6 = 4", "6 − 10 = 4", "10 + 6 = 4"], "10 − 6 = 4", "PRIMERO LO QUE HABÍA.")],
 [4, N("¿CUÁNTO ES 6 − 6?", 0, "SI SACAMOS TODO, QUEDAN 0.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: quitar y comparar", "examen_titulo": "Nivel jefe: quitar y comparar",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
