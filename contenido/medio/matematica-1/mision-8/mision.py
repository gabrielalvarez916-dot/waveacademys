# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 8 · Juntar y agregar. Genera mision-8.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el picnic de Sofi en la plaza (igual que clases.py).
Niveles: 1 juntar colecciones · 2 agregar elementos · 3 sumar con dibujos · 4 escribir la suma. Todo hasta 10."""
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
NEU = lambda p: {"neutro": {"p": p}}

N1 = {**ESTILO,
"objetivo": "Vas a juntar dos grupos y contar cuántos hay.",
"vas_a_ver": ["Dos grupos de cosas", "Juntar los grupos", "Contar todo junto"],
"secciones": [
 S(1, "Dos canastas", [
  P("Sofi trae <b>3</b> manzanas. Tomi trae <b>2</b> manzanas."),
  IMG("Juntamos las manzanas", "3 y 2 son 5.", FG.juntar(("manzana", 3), ("manzana", 2), "5")),
 ]),
 S(1, "Juntar", [
  D("Juntar", "Poner dos grupos en uno solo. Después contamos <b>todo</b>."),
  IMG("Pelotas y estrellas", "4 y 3 son 7.", FG.juntar(("pelota", 4), ("estrella", 3), "7")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los dos grupos. Los vas a usar en la carpeta."),
  IMG("Dos grupos", "Contá cada grupo y después todo.", FG.juntar(("vaso", 5), ("vaso", 3), "?")),
 ]),
],
"ejemplo_completo": {"titulo": "Globos", "planteo": "Sofi tiene 2 globos. Tomi tiene 4.", "pasos": ["Juntamos los globos.", "Contamos: 1, 2, 3, 4, 5, 6.", "Hay 6 globos."]},
"ejemplo_incompleto": {"titulo": "Vasos", "planteo": "Completá.", "pasos": ["Hay 3 vasos y 3 vasos.", "Juntos hay ___ vasos."]},
"ejemplo_solo": {"titulo": "Tus juguetes", "planteo": "Tenés 2 autitos y 5 pelotas. ¿Cuántos juguetes son?"},
"tip": {"titulo": "Contá todo", "texto": "Después de juntar, contá todo desde 1."},
"ojo": ["Contá cada cosa una sola vez.", "No te olvides de ningún grupo."],
"resumen": [{"titulo": "Dos grupos", "texto": "Los contamos."}, {"titulo": "Juntar", "texto": "Un solo grupo."}, {"titulo": "Total", "texto": "Contamos todo."}],
"glosario": [{"palabra": "Juntar", "significado": "Poner todo en un grupo."}, {"palabra": "Total", "significado": "Cuántos hay en todo."}],
"carpeta": ["¿Cuántos vasos hay en el primer grupo?", "¿Cuántos vasos hay en el segundo grupo?", "¿Cuántos vasos hay en total?"],
"respuestas_carpeta": [["5"], ["3"], ["8"]],
"soluciones": {"incompleto": "6.", "solo": "7 juguetes.", "carpeta": ["5.", "3.", "8."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a agregar cosas a un grupo y contar cuántas quedan.",
"vas_a_ver": ["Un grupo que crece", "Seguir contando", "Cuántos hay ahora"],
"secciones": [
 S(1, "Llegan más", [
  P("En la manta hay <b>4</b> manzanas. Sofi agrega <b>3</b> más."),
  IMG("Agregamos manzanas", "4 y 3 más son 7.", FG.agregar("manzana", 4, 3, "AHORA HAY 7")),
 ]),
 S(1, "Seguir contando", [
  D("Agregar", "Sumar cosas a un grupo. El grupo se hace <b>más grande</b>."),
  P("Empezamos en <b>5</b> y seguimos: <b>6, 7, 8</b>."),
  IMG("Pelotas", "5 y 3 más son 8.", FG.agregar("pelota", 5, 3, "AHORA HAY 8")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las estrellas. Las vas a usar en la carpeta."),
  IMG("Estrellas", "Las del círculo son nuevas.", FG.agregar("estrella", 6, 2, "¿CUÁNTAS HAY?")),
 ]),
],
"ejemplo_completo": {"titulo": "Vasos", "planteo": "Hay 6 vasos. Tomi trae 2 más.", "pasos": ["Empezamos en 6.", "Seguimos: 7, 8.", "Ahora hay 8 vasos."]},
"ejemplo_incompleto": {"titulo": "Globos", "planteo": "Completá.", "pasos": ["Hay 7 globos. Llegan 2 más.", "Seguimos: 8, ___ .", "Ahora hay ___ globos."]},
"ejemplo_solo": {"titulo": "Figuritas", "planteo": "Tenés 5 figuritas. Te regalan 1. ¿Cuántas tenés?"},
"tip": {"titulo": "Seguí contando", "texto": "No empieces de nuevo. Seguí desde el número que tenés."},
"ojo": ["Al agregar, el grupo crece.", "Contá solo una vez lo que ya había."],
"resumen": [{"titulo": "Grupo", "texto": "Lo que había."}, {"titulo": "Agregar", "texto": "Llegan más."}, {"titulo": "Ahora", "texto": "Hay más que antes."}],
"glosario": [{"palabra": "Agregar", "significado": "Poner más cosas."}, {"palabra": "Seguir contando", "significado": "Contar desde donde estaba."}],
"carpeta": ["¿Cuántas estrellas había antes?", "¿Cuántas estrellas llegaron?", "¿Cuántas estrellas hay ahora todas juntas?"],
"respuestas_carpeta": [["6"], ["2"], ["8"]],
"soluciones": {"incompleto": "9. 9.", "solo": "6 figuritas.", "carpeta": ["6.", "2.", "8."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a sumar dibujando palitos o puntos.",
"vas_a_ver": ["Dibujar cada cosa", "Juntar los dibujos", "Contar los dibujos"],
"secciones": [
 S(1, "Dibujar para sumar", [
  P("Sofi no tiene las manzanas. ¡Las <b>dibuja</b>!"),
  P("3 manzanas: <b>I I I</b>. 4 manzanas: <b>I I I I</b>."),
  IMG("Contamos los dibujos", "3 y 4 son 7.", FG.juntar(("manzana", 3), ("manzana", 4), "7")),
 ]),
 S(1, "Sumar", [
  D("Sumar", "Juntar o agregar y contar cuántos hay. Se dice <b>más</b>."),
  P("3 <b>más</b> 4 es igual a 7."),
  IMG("Estrellas", "3 más 4 es 7.", FG.juntar(("estrella", 3), ("estrella", 4), "7")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Globos", "Dibujá un palito por globo.", FG.juntar(("globo", 2), ("globo", 5), "?")),
 ]),
],
"ejemplo_completo": {"titulo": "5 más 2", "planteo": "Sumamos 5 más 2 con palitos.", "pasos": ["Dibujamos 5 palitos: I I I I I.", "Dibujamos 2 más: I I.", "Contamos: son 7."]},
"ejemplo_incompleto": {"titulo": "4 más 4", "planteo": "Dibujá y completá.", "pasos": ["4 palitos: I I I I.", "4 palitos más: ___ .", "4 más 4 es ___ ."]},
"ejemplo_solo": {"titulo": "Con puntos", "planteo": "Dibujá puntos para sumar 6 más 3."},
"tip": {"titulo": "Un dibujo por cosa", "texto": "Un palito por cada cosa. Así es más fácil."},
"ojo": ["Dibujá un palito por cada cosa.", "Contá los palitos de los dos grupos."],
"resumen": [{"titulo": "Dibujar", "texto": "Un palito por cosa."}, {"titulo": "Sumar", "texto": "Juntar y contar."}, {"titulo": "Más", "texto": "Así se dice."}],
"glosario": [{"palabra": "Sumar", "significado": "Juntar y contar todo."}, {"palabra": "Palito", "significado": "Un dibujo por cada cosa."}],
"carpeta": ["¿Cuántos globos hay en el primer grupo?", "¿Cuántos globos hay en el segundo grupo?", "¿Cuántos globos hay en total?"],
"respuestas_carpeta": [["2"], ["5"], ["7"]],
"soluciones": {"incompleto": "I I I I. 8.", "solo": "9.", "carpeta": ["2.", "5.", "7."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir la suma con números y signos.",
"vas_a_ver": ["El signo +", "El signo =", "Escribir la cuenta"],
"secciones": [
 S(1, "Los signos", [
  D("El signo +", "Se lee <b>más</b>. Junta dos números."),
  D("El signo =", "Se lee <b>igual</b>. Después va el resultado."),
  IMG("Los signos", "Más e igual.", FG.tarjetas([("+", "más"), ("=", "igual")])),
 ]),
 S(1, "Escribir la suma", [
  P("3 manzanas y 2 manzanas se escribe <b>3 + 2 = 5</b>."),
  IMG("La suma", "3 + 2 = 5.", FG.juntar(("manzana", 3), ("manzana", 2), "3 + 2 = 5")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pelotas. Las vas a usar en la carpeta."),
  IMG("Pelotas", "Escribí la suma.", FG.agregar("pelota", 6, 3, "6 + 3 = ?")),
 ]),
],
"ejemplo_completo": {"titulo": "4 y 5", "planteo": "4 vasos y 5 vasos.", "pasos": ["Primero el 4.", "Después: + 5.", "4 + 5 = 9."]},
"ejemplo_incompleto": {"titulo": "2 y 6", "planteo": "Completá.", "pasos": ["2 + ___ = ___ ."]},
"ejemplo_solo": {"titulo": "Tu suma", "planteo": "Escribí la suma de 1 pelota y 7 pelotas."},
"tip": {"titulo": "Se lee así", "texto": "3 + 2 = 5 se lee tres más dos igual a cinco."},
"ojo": ["El + va entre los dos números.", "El resultado va después del =."],
"resumen": [{"titulo": "+", "texto": "Se lee más."}, {"titulo": "=", "texto": "Se lee igual."}, {"titulo": "Suma", "texto": "3 + 2 = 5."}],
"glosario": [{"palabra": "Más (+)", "significado": "El signo de sumar."}, {"palabra": "Igual (=)", "significado": "Antes del resultado."}],
"carpeta": ["¿Cuántas pelotas había al principio?", "¿Cuántas pelotas se agregaron?", "¿Cuánto es 6 + 3?"],
"respuestas_carpeta": [["6"], ["3"], ["9"]],
"soluciones": {"incompleto": "2 + 6 = 8.", "solo": "1 + 7 = 8.", "carpeta": ["6.", "3.", "9."]},
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
 T("DOS GRUPOS", [LD("JUNTAR", "<b>JUNTAR</b> ES PONER DOS GRUPOS EN UNO SOLO."),
   LL("3 MANZANAS Y 2 MANZANAS.", "AHORA ES UN SOLO GRUPO.")],
   {"modo": "sumar", "que": "juntar"}, {"modo": "sumar", "que": "juntar"}),
 T("CONTAR TODO JUNTO", [LD("EL TOTAL", "DESPUÉS DE JUNTAR, CONTAMOS <b>TODO</b> PARA SABER CUÁNTOS HAY."),
   LL("TOCÁ CADA UNO UNA SOLA VEZ.", "EL ÚLTIMO NÚMERO ES EL TOTAL.")],
   {"modo": "sumar", "que": "juntar"}, {"modo": "sumar", "que": "juntar"}),
], "recuerda": [
 RC("JUNTAR", "ES PONER DOS GRUPOS EN UNO SOLO.", "4 PELOTAS Y 4 PELOTAS"),
 RC("EL TOTAL", "ES CUÁNTOS HAY CUANDO CONTAMOS TODO JUNTO.", "4 Y 4 SON 8"),
]}

N2["leccion"] = {"temas": [
 T("UN GRUPO QUE CRECE", [LD("AGREGAR", "SI <b>AGREGAMOS</b> COSAS A UN GRUPO, EL GRUPO CRECE."),
   LL("HABÍA 5 GLOBOS Y LLEGAN 2.", "AHORA HAY MÁS QUE ANTES.")],
   {"modo": "sumar", "que": "agregar"}, {"modo": "sumar", "que": "agregar"}),
 T("SEGUIR CONTANDO", [LD("SEGUIR", "NO EMPEZAMOS DE NUEVO: <b>SEGUIMOS CONTANDO</b> DESDE LO QUE HABÍA."),
   LL("HABÍA 6: 7, 8, 9.", "CONTÁ SOLO LOS QUE LLEGAN.")],
   {"modo": "sumar", "que": "agregar"}, {"modo": "sumar", "que": "agregar"}),
], "recuerda": [
 RC("AGREGAR", "ES SUMAR COSAS A UN GRUPO QUE YA HABÍA.", "5 GLOBOS Y LLEGAN 2"),
 RC("SEGUIR CONTANDO", "ARRANCAMOS DESDE LO QUE HABÍA, NO DESDE EL 1.", "6… 7, 8, 9"),
]}

N3["leccion"] = {"temas": [
 T("UN PALITO POR CADA COSA", [LD("DIBUJAR", "PARA SUMAR, PODEMOS DIBUJAR <b>UN PALITO</b> POR CADA COSA."),
   LL("4 GLOBOS SON 4 PALITOS.", "NO HACE FALTA DIBUJAR LOS GLOBOS.")],
   {"modo": "sumar", "que": "palitos"}, {"modo": "sumar", "que": "palitos"}),
 T("CONTAR LOS DIBUJOS", [LD("CONTAR", "DESPUÉS CONTAMOS <b>TODOS</b> LOS PALITOS JUNTOS."),
   LP("LOS PALITOS NOS AYUDAN A NO PERDERNOS CUANDO LAS COSAS NO ESTÁN.")],
   {"modo": "sumar", "que": "palitos"}, {"modo": "sumar", "que": "palitos"}),
], "recuerda": [
 RC("PALITOS", "DIBUJAMOS UNO POR CADA COSA QUE QUEREMOS CONTAR.", "3 VASOS: I I I"),
 RC("CONTAR TODO", "CONTAMOS TODOS LOS PALITOS JUNTOS.", "I I Y I I I SON 5"),
]}

N4["leccion"] = {"temas": [
 T("EL SIGNO +", [LD("MÁS", "EL SIGNO <b>+</b> SE LEE MÁS Y QUIERE DECIR JUNTAR O AGREGAR."),
   LL("4 + 3 SE LEE CUATRO MÁS TRES.", "VA ENTRE LOS DOS NÚMEROS.")],
   {"modo": "sumar", "que": "cuenta"}, {"modo": "sumar", "que": "cuenta"}),
 T("EL SIGNO =", [LD("IGUAL", "EL SIGNO <b>=</b> SE LEE IGUAL. DESPUÉS VA EL RESULTADO."),
   LL("5 + 1 = 6.", "PRIMERO LA SUMA, DESPUÉS EL RESULTADO.")],
   {"modo": "sumar", "que": "cuenta"}, {"modo": "sumar", "que": "cuenta"}),
], "recuerda": [
 RC("EL SIGNO +", "SE LEE MÁS Y QUIERE DECIR JUNTAR.", "2 + 7"),
 RC("EL SIGNO =", "SE LEE IGUAL Y DESPUÉS VA EL RESULTADO.", "2 + 7 = 9"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("🍎🍎🍎 Y 🍎🍎 ¿CUÁNTAS MANZANAS HAY EN TOTAL?", 5, "3 Y 2 SON 5.", **A),
      MC("SI JUNTAMOS 4 PELOTAS Y 4 PELOTAS, ¿CUÁNTAS HAY?", ["4", "8", "6"], "8", "CONTAMOS TODO: 8.", **A),
      MC("LEO JUNTÓ 3 AUTOS Y 2 AUTOS Y DICE QUE HAY 3. ¿CUÁNTOS HAY DE VERDAD?", ["5", "3", "2"], "5", "HAY QUE CONTAR LOS DOS GRUPOS: 5.", **ER),
      UNIR("UNÍ CADA PAR DE GRUPOS CON SU TOTAL.", ["⭐⭐ Y ⭐", "⭐⭐⭐ Y ⭐⭐⭐", "⭐⭐⭐⭐ Y ⭐"], ["6", "3", "5"], {"⭐⭐ Y ⭐": "3", "⭐⭐⭐ Y ⭐⭐⭐": "6", "⭐⭐⭐⭐ Y ⭐": "5"}, "2 Y 1 SON 3, 3 Y 3 SON 6, 4 Y 1 SON 5.", **A)],
"2": [N("HAY 5 GLOBOS. LLEGAN 2 MÁS. ¿CUÁNTOS HAY AHORA?", 7, "5… 6, 7.", **A),
      MC("SI AGREGAMOS COSAS A UN GRUPO, EL GRUPO…", ["CRECE", "SE ACHICA", "QUEDA IGUAL"], "CRECE", "AL AGREGAR HAY MÁS.", **RE),
      N("[[problema]] EN EL COLECTIVO VAN 6 CHICOS. SUBEN 3 MÁS. ¿CUÁNTOS CHICOS VAN AHORA?", 9, "6… 7, 8, 9.", **AN, **NEU("EN EL AUTOBÚS VAN 6 NIÑOS. SUBEN 3 MÁS. ¿CUÁNTOS NIÑOS VAN AHORA?")),
      MC("HABÍA 7 FLORES Y TRAEN 2. SOFI CUENTA DESDE EL 1. ¿DESDE QUÉ NÚMERO CONVIENE SEGUIR?", ["DESDE EL 7", "DESDE EL 1", "DESDE EL 2"], "DESDE EL 7", "SEGUIMOS DESDE LO QUE HABÍA: 8, 9.", **ER)],
"3": [N("I I I I Y I I I ¿CUÁNTOS PALITOS HAY?", 7, "4 Y 3 SON 7.", **A),
      MC("¿CUÁNTO ES 2 MÁS 6?", ["8", "4", "9"], "8", "2 PALITOS Y 6 PALITOS SON 8.", **A),
      FB("DIBUJÁ CON PALITOS Y COMPLETÁ: 3 Y 4 SON ___", [["7"]], "I I I Y I I I I SON 7.", **A),
      MC("PARA SUMAR 5 PERROS Y 2 PERROS, JUAN DIBUJÓ UN SOLO PALITO POR GRUPO. ¿QUÉ HIZO MAL?", ["VA UN PALITO POR CADA PERRO", "NADA, ESTÁ BIEN", "TENÍA QUE DIBUJAR PERROS"], "VA UN PALITO POR CADA PERRO", "UN PALITO POR CADA COSA: 7 PALITOS.", **ER)],
"4": [N("¿CUÁNTO ES 4 + 3?", 7, "4… 5, 6, 7.", **A),
      MC("¿CÓMO SE ESCRIBE 5 MANZANAS Y 1 MANZANA?", ["5 + 1 = 6", "5 = 1 + 6", "5 + 6 = 1"], "5 + 1 = 6", "PRIMERO LA SUMA, DESPUÉS EL RESULTADO.", **A),
      UNIR("UNÍ CADA CUENTA CON SU RESULTADO.", ["2 + 2", "3 + 4", "6 + 3"], ["9", "4", "7"], {"2 + 2": "4", "3 + 4": "7", "6 + 3": "9"}, "2 + 2 = 4, 3 + 4 = 7, 6 + 3 = 9.", **A),
      ORD("ARMÁ LA CUENTA EN ORDEN.", ["=", "5", "+", "2", "7"], ["5", "+", "2", "=", "7"], "5 + 2 = 7.", **AN)],
"5": [N("RELÁMPAGO. ¿CUÁNTO ES 2 + 2?", 4, "2… 3, 4.", tiempo=30, **A),
      N("RELÁMPAGO. HAY 6 VASOS. LLEGAN 3. ¿CUÁNTOS HAY?", 9, "6… 7, 8, 9.", tiempo=30, **A),
      N("RELÁMPAGO. 🍎🍎🍎🍎🍎 Y 🍎 ¿CUÁNTAS SON?", 6, "5 Y 1 SON 6.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿QUÉ SIGNO SE LEE MÁS?", ["+", "=", "-"], "+", "EL + ES EL SIGNO DE SUMAR.", tiempo=30, **RE)],
}
EXAMEN = [
 [1, N("⚽⚽ Y ⚽⚽⚽ ¿CUÁNTAS PELOTAS HAY EN TOTAL?", 5, "2 Y 3 SON 5.", **A)],
 [1, MC("JUNTAR ES…", ["PONER DOS GRUPOS EN UNO", "SACAR COSAS", "CONTAR SOLO UN GRUPO"], "PONER DOS GRUPOS EN UNO", "DESPUÉS CONTAMOS TODO.", **RE)],
 [1, N("[[problema]] SOFI TIENE 4 GLOBOS Y TOMI TIENE 2. SI LOS JUNTAN, ¿CUÁNTOS SON?", 6, "4 Y 2 SON 6.", **AN)],
 [2, N("HAY 7 MANZANAS. SOFI AGREGA 1. ¿CUÁNTAS HAY?", 8, "7… 8.", **A)],
 [2, N("HAY 3 VASOS. LLEGAN 4 MÁS. ¿CUÁNTOS HAY AHORA?", 7, "3… 4, 5, 6, 7.", **A)],
 [2, MC("HAY 5 PELOTAS Y AGREGAMOS 2. SEGUIMOS CONTANDO DESDE…", ["1", "5", "2"], "5", "NO EMPEZAMOS DE NUEVO.", **A)],
 [3, N("I I I I I Y I I I ¿CUÁNTOS PALITOS HAY?", 8, "5 Y 3 SON 8.", **A)],
 [3, MC("PARA SUMAR CON DIBUJOS, HACEMOS…", ["UN PALITO POR CADA COSA", "UN PALITO PARA TODO", "NINGÚN PALITO"], "UN PALITO POR CADA COSA", "ASÍ NO NOS PERDEMOS.", **RE)],
 [3, FB("COMPLETÁ: 6 PALITOS Y 4 PALITOS SON ___", [["10"]], "6 Y 4 SON 10.", **A)],
 [4, N("¿CUÁNTO ES 3 + 5?", 8, "3… 4, 5, 6, 7, 8.", **A)],
 [4, MC("EL SIGNO = SE LEE…", ["MÁS", "IGUAL", "MENOS"], "IGUAL", "DESPUÉS DEL = VA EL RESULTADO.", **RE)],
 [4, MC("MICA ESCRIBIÓ 2 = 7 + 9 PARA 2 VASOS Y 7 VASOS. ¿CÓMO SE ESCRIBE BIEN?", ["2 + 7 = 9", "2 = 7 + 9", "9 + 2 = 7"], "2 + 7 = 9", "PRIMERO LA SUMA Y DESPUÉS EL RESULTADO.", **ER)],
 [4, UNIR("UNÍ CADA CUENTA CON SU RESULTADO.", ["1 + 8", "4 + 4"], ["8", "9"], {"1 + 8": "9", "4 + 4": "8"}, "1 + 8 = 9 Y 4 + 4 = 8.", **A)],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 8, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: juntar y agregar", "examen_titulo": "Nivel jefe: juntar y agregar",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
