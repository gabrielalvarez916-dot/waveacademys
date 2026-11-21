# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 1 · Contar y comparar colecciones. Genera mision-1.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: el cumple de Sofi (igual que en las clases animadas, clases.py)."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IM = lambda t, x: {"tipo": "importante", "titulo": t, "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
# actividades y examen: también en imprenta mayúscula, para que las lean los chicos
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
N = lambda p, r, e, **k: {"t": "numeric", "p": p, "o": {}, "r": {"acepta": [r]}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a contar objetos de a uno y decir cuántos hay.",
"vas_a_ver": ["Contar de a uno, en orden", "Tocar cada objeto con el dedo", "El último número dice cuántos hay"],
"secciones": [
 S(1, "Contamos de a uno", [
  P("Sofi cuenta los globos de su cumple."),
  P("Toca cada globo con el dedo y dice un número: <b>1, 2, 3, 4, 5</b>."),
  IMG("Los globos de Sofi", "Cada globo tiene su número.", FG.contar_numerado("globo", 5, "5 globos")),
 ]),
 S(1, "El último número", [
  D("Cuántos hay", "El <b>último número</b> que decís es la cantidad de objetos."),
  IMG("Las estrellas", "El último número es 7: hay 7 estrellas.", FG.contar_numerado("estrella", 7, "7 estrellas")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los tres grupos. Los vas a usar en la carpeta."),
  IMG("Grupos A, B y C", "Contá cada grupo con el dedo.", FG.grupos_letras([("A", "manzana", 3), ("B", "pelota", 6), ("C", "estrella", 9)])),
 ]),
],
"ejemplo_completo": {"titulo": "Los caramelos", "planteo": "Sofi tiene caramelos. ¿Cuántos hay?", "pasos": ["Toca el primero y dice 1.", "Sigue: 2, 3, 4.", "El último número es 4: hay 4 caramelos."]},
"ejemplo_incompleto": {"titulo": "Las pelotas", "planteo": "Completá lo que falta.", "pasos": ["Contamos: 1, 2, 3, ___ , 5.", "El último número es ___ .", "Hay ___ pelotas."]},
"ejemplo_solo": {"titulo": "Tus juguetes", "planteo": "Contá tus juguetes y decí cuántos hay."},
"tip": {"titulo": "Usá el dedo", "texto": "Tocá cada objeto una sola vez."},
"ojo": ["No cuentes dos veces el mismo.", "No te saltees ninguno."],
"resumen": [{"titulo": "Contar", "texto": "De a uno, en orden."}, {"titulo": "El dedo", "texto": "Toca cada objeto una vez."}, {"titulo": "Cuántos hay", "texto": "Lo dice el último número."}],
"glosario": [{"palabra": "Contar", "significado": "Decir los números en orden, uno por objeto."}, {"palabra": "Cantidad", "significado": "Cuántos objetos hay."}],
"carpeta": ["¿Cuántas manzanas hay en el grupo A?", "¿Cuántas pelotas hay en el grupo B?", "¿Cuántas estrellas hay en el grupo C?"],
"respuestas_carpeta": [["3"], ["6"], ["9"]],
"soluciones": {"incompleto": "4. 5. 5.", "solo": "Depende de tus juguetes. El último número dice cuántos hay.", "carpeta": ["3.", "6.", "9."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a decir qué grupo tiene más, menos o igual.",
"vas_a_ver": ["Más", "Menos", "Igual: la misma cantidad"],
"secciones": [
 S(1, "Más y menos", [
  P("Juan tiene 4 caramelos. Sofi tiene 2 caramelos."),
  P("4 es más que 2. Juan tiene <b>más</b>. Sofi tiene <b>menos</b>."),
  IMG("Los caramelos de Juan y de Sofi", "Juan tiene más. Sofi tiene menos.", FG.dos_grupos(("caramelo", 4), ("caramelo", 2), "más", "menos", ("Juan", "Sofi"))),
 ]),
 S(1, "Igual", [
  D("Igual", "Dos grupos son <b>iguales</b> si tienen la misma cantidad."),
  IMG("Las manzanas de Ana y de Leo", "Ana tiene 3. Leo tiene 3. Tienen igual.", FG.dos_grupos(("manzana", 3), ("manzana", 3), "igual", "igual", ("Ana", "Leo"))),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Grupos A, B y C", "Contá cada grupo.", FG.grupos_letras([("A", "pelota", 5), ("B", "pelota", 3), ("C", "estrella", 5)])),
 ]),
],
"ejemplo_completo": {"titulo": "Globos", "planteo": "Ana tiene 5 globos. Leo tiene 3 globos.", "pasos": ["Contamos los dos grupos: 5 y 3.", "5 es más que 3.", "Ana tiene más globos. Leo tiene menos."]},
"ejemplo_incompleto": {"titulo": "Autitos", "planteo": "Juan tiene 2 autitos. Sofi tiene 6 autitos.", "pasos": ["6 es más que ___ .", "Tiene más autitos ___ .", "Tiene menos autitos ___ ."]},
"ejemplo_solo": {"titulo": "Lápices", "planteo": "Tenés 4 lápices y tu amigo tiene 4. ¿Quién tiene más?"},
"tip": {"titulo": "Contá los dos grupos", "texto": "El número más grande es el grupo que tiene más."},
"ojo": ["Mirá cuántos hay, no qué tan grandes son.", "Si hay la misma cantidad, hay igual."],
"resumen": [{"titulo": "Más", "texto": "El grupo con más objetos."}, {"titulo": "Menos", "texto": "El grupo con menos objetos."}, {"titulo": "Igual", "texto": "La misma cantidad."}],
"glosario": [{"palabra": "Más", "significado": "Cuando un grupo tiene más objetos que otro."}, {"palabra": "Menos", "significado": "Cuando un grupo tiene menos objetos que otro."}, {"palabra": "Igual", "significado": "La misma cantidad."}],
"carpeta": ["¿Qué grupo tiene más: A o B?", "¿Qué grupo tiene menos: A o B?", "¿Qué grupo tiene igual que el A?"],
"respuestas_carpeta": [["a", "grupo a"], ["b", "grupo b"], ["c", "grupo c"]],
"soluciones": {"incompleto": "2. Sofi. Juan.", "solo": "Nadie: tienen igual, 4 y 4.", "carpeta": ["A: tiene 5 y B tiene 3.", "B: tiene 3.", "C: tiene 5, igual que A."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a comparar dos grupos sin contar, armando parejas.",
"vas_a_ver": ["Unir uno con uno", "Si sobran, ese grupo tiene más", "Si faltan, ese grupo tiene menos"],
"secciones": [
 S(1, "Uno con uno", [
  P("Sofi quiere saber si alcanzan los vasos para sus amigos."),
  D("Uno con uno", "Unimos cada chico con <b>un</b> vaso. Así armamos <b>parejas</b>."),
  IMG("Chicos y vasos", "Sobran 2 vasos: hay más vasos que chicos.", FG.parejas(("chico", 4), ("vaso", 6), "sobran vasos")),
 ]),
 S(1, "Sobran, faltan o igual", [
  P("Si <b>sobran</b> vasos, hay más vasos que chicos."),
  P("Si <b>faltan</b> vasos, hay menos vasos que chicos."),
  P("Si no sobra ni falta, hay <b>igual</b>."),
  IMG("Tres casos", "Sobran, faltan o igual.", FG.tres_casos()),
 ]),
 S(2, "Para practicar", [
  P("Mirá los chicos y las sillas. Lo vas a usar en la carpeta."),
  IMG("Chicos y sillas", "Uní cada chico con una silla.", FG.parejas(("chico", 5), ("silla", 3), "¿alcanzan las sillas?", sobra=False)),
 ]),
],
"ejemplo_completo": {"titulo": "Chicos y tortitas", "planteo": "Hay 3 chicos y 4 tortitas.", "pasos": ["Unimos cada chico con una tortita.", "Sobra 1 tortita.", "Hay más tortitas que chicos."]},
"ejemplo_incompleto": {"titulo": "Perros y huesos", "planteo": "Hay 4 perros y 2 huesos.", "pasos": ["Unimos cada perro con un hueso.", "Faltan ___ huesos.", "Hay ___ huesos que perros."]},
"ejemplo_solo": {"titulo": "Flores y macetas", "planteo": "Hay 5 flores y 5 macetas. ¿Sobra o falta alguna?"},
"tip": {"titulo": "Armá parejas", "texto": "Uní con una línea cada objeto con otro."},
"ojo": ["Cada objeto va con un solo compañero.", "No unas dos con el mismo."],
"resumen": [{"titulo": "Uno con uno", "texto": "Armar parejas."}, {"titulo": "Sobran", "texto": "Ese grupo tiene más."}, {"titulo": "Faltan", "texto": "Ese grupo tiene menos."}],
"glosario": [{"palabra": "Pareja", "significado": "Dos objetos unidos: uno de cada grupo."}, {"palabra": "Sobrar", "significado": "Quedar sin pareja."}],
"carpeta": ["¿Cuántos chicos quedan sin silla?", "¿Hay más chicos o más sillas?", "¿Cuántas sillas hay que traer para que alcancen?"],
"respuestas_carpeta": [["2"], ["chicos", "mas chicos", "más chicos", "hay más chicos", "hay mas chicos"], ["2"]],
"soluciones": {"incompleto": "2. Menos.", "solo": "No sobra ni falta: hay igual.", "carpeta": ["2: sobran 2 chicos.", "Más chicos.", "2 sillas."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a armar grupos iguales agregando o quitando objetos.",
"vas_a_ver": ["Agregar al grupo que tiene menos", "Quitar al grupo que tiene más", "Comprobar que hay igual"],
"secciones": [
 S(1, "Agregar", [
  P("Sofi arma bolsitas. Una tiene 5 caramelos y otra tiene 3."),
  P("<b>Agregamos</b> 2 caramelos a la que tiene menos."),
  IMG("Agregar caramelos", "Ahora las dos tienen 5.", FG.igualar("caramelo", 5, 3, "agregar")),
 ]),
 S(1, "Quitar", [
  P("Juan tiene 6 pelotas y Sofi tiene 4."),
  P("<b>Quitamos</b> 2 pelotas al grupo que tiene más."),
  IMG("Quitar pelotas", "Ahora los dos tienen 4.", FG.igualar("pelota", 6, 4, "quitar")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Grupos A y B", "Contá cada grupo.", FG.grupos_letras([("A", "estrella", 7), ("B", "estrella", 4)])),
 ]),
],
"ejemplo_completo": {"titulo": "Manzanas", "planteo": "Un plato tiene 4 manzanas. Otro tiene 2.", "pasos": ["El segundo plato tiene menos.", "Agregamos 2 manzanas: 3, 4.", "Ahora hay 4 y 4: igual."]},
"ejemplo_incompleto": {"titulo": "Globos", "planteo": "Ana tiene 5 globos. Leo tiene 3.", "pasos": ["Para igualar, a Leo le agregamos ___ globos.", "O a Ana le quitamos ___ globos."]},
"ejemplo_solo": {"titulo": "Lápices", "planteo": "Tenés 6 lápices y tu amigo tiene 3. ¿Cómo igualás?"},
"tip": {"titulo": "Contá al final", "texto": "Contá los dos grupos para ver si hay igual."},
"ojo": ["Agregá al grupo que tiene menos.", "Quitá al grupo que tiene más."],
"resumen": [{"titulo": "Igual", "texto": "La misma cantidad."}, {"titulo": "Agregar", "texto": "Al grupo que tiene menos."}, {"titulo": "Quitar", "texto": "Al grupo que tiene más."}],
"glosario": [{"palabra": "Agregar", "significado": "Poner más objetos en un grupo."}, {"palabra": "Quitar", "significado": "Sacar objetos de un grupo."}],
"carpeta": ["¿Cuántas estrellas tiene el grupo A? ¿Y el B?", "¿Cuántas estrellas agregás al B para igualar?", "¿Cuántas estrellas quitás al A para igualar?"],
"respuestas_carpeta": [["7 y 4", "7, 4", "7 4", "a 7 b 4"], ["3"], ["3"]],
"soluciones": {"incompleto": "2. 2.", "solo": "Agregás 3 lápices a tu amigo, o le quitás 3 a tu grupo.", "carpeta": ["A tiene 7. B tiene 4.", "3: 5, 6, 7.", "3: quedan 4 y 4."]},
}

ACT = {
"1": [N("¿CUÁNTAS MANZANAS HAY? 🍎🍎🍎🍎🍎", 5, "CONTAMOS: 1, 2, 3, 4, 5. HAY 5."),
      MC("¿EN QUÉ GRUPO HAY 3? ", ["⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐"], "⭐⭐⭐", "1, 2, 3: ESE GRUPO TIENE 3.")],
"2": [MC("¿QUIÉN TIENE MÁS? JUAN 🍬🍬🍬🍬🍬 · SOFI 🍬🍬", ["JUAN", "SOFI", "TIENEN IGUAL"], "JUAN", "JUAN TIENE 5 Y SOFI TIENE 2. 5 ES MÁS QUE 2."),
      MC("¿QUIÉN TIENE MENOS? ANA ⚽⚽⚽ · LEO ⚽⚽⚽⚽⚽⚽", ["ANA", "LEO", "TIENEN IGUAL"], "ANA", "ANA TIENE 3 Y LEO TIENE 6. 3 ES MENOS QUE 6.")],
"3": [MC("🧒🧒🧒🧒 · 🥤🥤🥤🥤🥤🥤 ¿ALCANZAN LOS VASOS?", ["SÍ, SOBRAN VASOS", "NO, FALTAN VASOS", "HAY IGUAL"], "SÍ, SOBRAN VASOS", "CADA CHICO TIENE SU VASO Y SOBRAN 2."),
      N("🐶🐶🐶🐶🐶 · 🦴🦴🦴 ¿CUÁNTOS HUESOS FALTAN?", 2, "3 PERROS TIENEN HUESO. FALTAN 2.")],
"4": [N("🍎🍎🍎🍎🍎🍎 · 🍎🍎🍎🍎 ¿CUÁNTAS AGREGO AL GRUPO CHICO PARA IGUALAR?", 2, "AGREGAMOS 2: 5, 6. QUEDAN 6 Y 6."),
      N("⭐⭐⭐⭐⭐ · ⭐⭐ ¿CUÁNTAS QUITO AL GRUPO GRANDE PARA IGUALAR?", 3, "QUITAMOS 3. QUEDAN 2 Y 2.")],
"5": [N("RELÁMPAGO. ¿CUÁNTOS GLOBOS HAY? 🎈🎈🎈🎈🎈🎈🎈", 7, "1, 2, 3, 4, 5, 6, 7.", tiempo=30),
      MC("RELÁMPAGO. ¿DÓNDE HAY MÁS?", ["🍬🍬🍬", "🍬🍬🍬🍬🍬"], "🍬🍬🍬🍬🍬", "5 ES MÁS QUE 3.", tiempo=30),
      MC("RELÁMPAGO. 🧒🧒🧒 · 🪑🪑🪑 ¿ALCANZAN LAS SILLAS?", ["SOBRAN", "FALTAN", "HAY IGUAL"], "HAY IGUAL", "CADA CHICO TIENE SU SILLA Y NO SOBRA NINGUNA.", tiempo=30),
      N("RELÁMPAGO. 🍭🍭🍭🍭 · 🍭 ¿CUÁNTOS AGREGO AL GRUPO CHICO?", 3, "AGREGAMOS 3: QUEDAN 4 Y 4.", tiempo=40)],
}
EXAMEN = [
 [1, N("¿CUÁNTOS PERROS HAY? 🐶🐶🐶🐶", 4, "1, 2, 3, 4.")],
 [1, N("¿CUÁNTAS ESTRELLAS HAY? ⭐⭐⭐⭐⭐⭐⭐⭐", 8, "CONTAMOS DE A UNA: HAY 8.")],
 [1, MC("PARA SABER CUÁNTOS HAY, ¿QUÉ NÚMERO MIRO?", ["EL PRIMERO", "EL ÚLTIMO"], "EL ÚLTIMO", "EL ÚLTIMO NÚMERO QUE DECÍS ES LA CANTIDAD.")],
 [2, MC("¿QUIÉN TIENE MÁS? SOFI 🎈🎈🎈 · JUAN 🎈🎈🎈🎈🎈🎈", ["SOFI", "JUAN", "TIENEN IGUAL"], "JUAN", "JUAN TIENE 6 Y SOFI TIENE 3.")],
 [2, MC("¿QUIÉN TIENE MENOS? ANA 🍎🍎🍎🍎 · LEO 🍎", ["ANA", "LEO", "TIENEN IGUAL"], "LEO", "LEO TIENE 1. 1 ES MENOS QUE 4.")],
 [2, MC("ANA 🌸🌸🌸🌸 · LEO 🌸🌸🌸🌸 ¿QUIÉN TIENE MÁS?", ["ANA", "LEO", "TIENEN IGUAL"], "TIENEN IGUAL", "4 Y 4 ES LA MISMA CANTIDAD.")],
 [3, MC("🧒🧒🧒🧒🧒 · 🧁🧁🧁 ¿ALCANZAN LAS TORTITAS?", ["SÍ, SOBRAN", "NO, FALTAN", "HAY IGUAL"], "NO, FALTAN", "3 CHICOS TIENEN TORTITA Y 2 NO.")],
 [3, N("🐱🐱🐱 · 🐟🐟🐟🐟🐟 ¿CUÁNTOS PESCADOS SOBRAN?", 2, "CADA GATO TIENE SU PESCADO Y SOBRAN 2.")],
 [3, MC("SI AL UNIR UNO CON UNO SOBRAN VASOS, ¿QUÉ HAY MÁS?", ["VASOS", "CHICOS"], "VASOS", "LO QUE SOBRA ES LO QUE HAY MÁS.")],
 [4, N("⚽⚽⚽⚽ · ⚽⚽ ¿CUÁNTAS AGREGO AL GRUPO CHICO PARA IGUALAR?", 2, "AGREGAMOS 2: QUEDAN 4 Y 4.")],
 [4, N("🍬🍬🍬🍬🍬🍬🍬 · 🍬🍬🍬🍬🍬 ¿CUÁNTOS QUITO AL GRUPO GRANDE PARA IGUALAR?", 2, "QUITAMOS 2: QUEDAN 5 Y 5.")],
 [4, MC("PARA IGUALAR, ¿A QUÉ GRUPO LE AGREGO?", ["AL QUE TIENE MÁS", "AL QUE TIENE MENOS"], "AL QUE TIENE MENOS", "SE AGREGA AL GRUPO MÁS CHICO.")],
 [4, MC("PARA IGUALAR, ¿A QUÉ GRUPO LE QUITO?", ["AL QUE TIENE MÁS", "AL QUE TIENE MENOS"], "AL QUE TIENE MÁS", "SE QUITA AL GRUPO MÁS GRANDE.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: contar y comparar colecciones", "examen_titulo": "Nivel jefe: contar y comparar colecciones",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
