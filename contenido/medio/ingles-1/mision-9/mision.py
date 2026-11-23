# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 9 · Food I Like. Genera mision-9.json.
Regla de primeros años. Metáfora: la merienda de Sofi y Tomi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 frutas: apple, banana, orange · 2 I like apples · 3 milk, bread, water · 4 yummy or yuck."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
SA = lambda p, acepta, e, **k: {"t": "short_answer", "p": p, "o": {}, "r": {"acepta": acepta}, "e": e, **k}
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
low = lambda w: [w, w.lower(), w.capitalize()]
def acepta(*ws):
    out = []
    for w in ws: out += [w, w.lower(), w.capitalize()]
    return out


N1 = {**ESTILO,
"objetivo": "Vas a nombrar frutas en inglés.",
"vas_a_ver": ["APPLE: manzana", "BANANA: banana", "ORANGE: naranja"],
"secciones": [
 S(1, "Frutas", [
  D("Fruta", "Alimento dulce que crece en las plantas."),
  P("Manzana es <b>APPLE</b>, banana es <b>BANANA</b> y naranja es <b>ORANGE</b>."),
  IMG("Frutas", "En inglés.", FG.tiras(["MANZANA = APPLE", "BANANA = BANANA", "NARANJA = ORANGE"], numeros=False, cols=1)),
 ]),
 S(1, "Colores de las frutas", [
  P("La <b>APPLE</b> es roja. La <b>BANANA</b> es amarilla."),
  IMG("Colores", "Fruta y color.", FG.tiras(["RED APPLE", "YELLOW BANANA", "ORANGE ORANGE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la frutera de Sofi. La vas a usar en la carpeta."),
  IMG("La frutera", "¿Qué fruta es?", FG.tiras(["ES ROJA Y REDONDA", "ES AMARILLA Y LARGA", "ES NARANJA Y JUGOSA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La merienda", "planteo": "Sofi come una manzana.", "pasos": ["La muerde.", "Dice: APPLE!", "¡Muy rica!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Naranja en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu fruta", "planteo": "Dibujá tu fruta preferida y escribí su nombre en inglés."},
"tip": {"titulo": "Casi igual", "texto": "BANANA se dice casi igual en castellano."},
"ojo": ["APPLE es manzana.", "ORANGE es naranja."],
"resumen": [{"titulo": "APPLE", "texto": "Manzana."}, {"titulo": "BANANA", "texto": "Banana."}, {"titulo": "ORANGE", "texto": "Naranja."}],
"glosario": [{"palabra": "APPLE", "significado": "Manzana."}, {"palabra": "ORANGE", "significado": "Naranja."}],
"carpeta": ["Es roja y redonda. ¿Qué fruta es?", "Es amarilla y larga. ¿Qué fruta es?", "Sofi come una naranja y dice APPLE. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("APPLE", "AN APPLE"), acepta("BANANA", "A BANANA"), acepta("ORANGE", "AN ORANGE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "ORANGE.", "solo": "Tu fruta.", "carpeta": ["APPLE.", "BANANA.", "ORANGE."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a decir qué comida te gusta en inglés.",
"vas_a_ver": ["I LIKE…", "Lo que me gusta", "A cada uno le gusta algo"],
"secciones": [
 S(1, "Me gusta", [
  D("Gustar", "Algo nos parece rico o lindo."),
  P("Para decir que algo nos gusta decimos <b>I LIKE</b>."),
  IMG("Me gusta", "Quiere decir: me gustan…", FG.tiras(["I LIKE APPLES.", "I LIKE BANANAS."], numeros=False, cols=1)),
 ]),
 S(1, "A cada uno", [
  P("A cada persona le gustan cosas distintas. ¡Está <b>bien</b>!"),
  IMG("Los chicos", "Lo que les gusta.", FG.tiras(["SOFI: I LIKE APPLES.", "TOMI: I LIKE ORANGES."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que comen los chicos. Lo vas a usar en la carpeta."),
  IMG("¿Qué les gusta?", "Sus frutas.", FG.tiras(["A LEO LE GUSTAN LAS BANANAS", "A ANA LE GUSTAN LAS MANZANAS"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi cuenta", "planteo": "Tomi come naranjas.", "pasos": ["Le encantan.", "Dice: I LIKE ORANGES!", "¡Qué rico!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "I ___ BANANAS.", "pasos": ["I ___ BANANAS."]},
"ejemplo_solo": {"titulo": "Lo que te gusta", "planteo": "Decí en voz alta: I LIKE y tu fruta preferida."},
"tip": {"titulo": "Sonreí", "texto": "Sonreí cuando decís I LIKE."},
"ojo": ["LIKE es gustar.", "I es yo."],
"resumen": [{"titulo": "I LIKE…", "texto": "Me gusta…"}, {"titulo": "LIKE", "texto": "Gustar."}, {"titulo": "Distintos", "texto": "A cada uno, algo."}],
"glosario": [{"palabra": "LIKE", "significado": "Gustar."}, {"palabra": "APPLES", "significado": "Manzanas."}],
"carpeta": ["A Leo le gustan las bananas. Completá: I LIKE ___.", "A Ana le gustan las manzanas. Completá: I LIKE ___.", "A Tomi le gustan las naranjas y dice I LIKE BANANAS. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("BANANAS", "BANANA"), acepta("APPLES", "APPLE"), acepta("I LIKE ORANGES", "ORANGES", "I LIKE ORANGE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "LIKE.", "solo": "Tu fruta.", "carpeta": ["BANANAS.", "APPLES.", "I LIKE ORANGES."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a nombrar comidas y bebidas del desayuno en inglés.",
"vas_a_ver": ["MILK: leche", "BREAD: pan", "WATER: agua"],
"secciones": [
 S(1, "El desayuno", [
  D("Desayuno", "La primera comida del día."),
  P("Leche es <b>MILK</b>, pan es <b>BREAD</b> y agua es <b>WATER</b>."),
  IMG("El desayuno", "En inglés.", FG.tiras(["LECHE = MILK", "PAN = BREAD", "AGUA = WATER"], numeros=False, cols=1)),
 ]),
 S(1, "Comer o tomar", [
  P("El <b>BREAD</b> se come. La <b>MILK</b> y el <b>WATER</b> se toman."),
  IMG("Comer o tomar", "Dos grupos.", FG.tiras(["COMEMOS: BREAD, APPLE", "TOMAMOS: MILK, WATER"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el desayuno de Tomi. Lo vas a usar en la carpeta."),
  IMG("El desayuno de Tomi", "¿Qué es?", FG.tiras(["UN VASO BLANCO", "UNA TOSTADA", "UN VASO TRANSPARENTE"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi desayuna", "planteo": "Tomi toma un vaso de leche.", "pasos": ["Es blanca.", "Dice: MILK!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Pan en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu desayuno", "planteo": "Mañana en el desayuno nombrá lo que comés en inglés."},
"tip": {"titulo": "Tomar agua", "texto": "WATER es lo más sano para tomar."},
"ojo": ["MILK es leche.", "WATER es agua."],
"resumen": [{"titulo": "MILK", "texto": "Leche."}, {"titulo": "BREAD", "texto": "Pan."}, {"titulo": "WATER", "texto": "Agua."}],
"glosario": [{"palabra": "MILK", "significado": "Leche."}, {"palabra": "BREAD", "significado": "Pan."}],
"carpeta": ["Un vaso de leche blanca. ¿Qué es?", "Una tostada. ¿Qué es?", "Tomi toma agua y dice MILK. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("MILK"), acepta("BREAD", "TOAST"), acepta("WATER")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "BREAD.", "solo": "Tu desayuno.", "carpeta": ["MILK.", "BREAD.", "WATER."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a decir si una comida es rica o fea en inglés.",
"vas_a_ver": ["YUMMY: ¡rico!", "YUCK: ¡puaj!", "Votar la fruta preferida"],
"secciones": [
 S(1, "Rico o feo", [
  D("Sabor", "Cómo sentimos la comida en la boca."),
  P("Si algo es rico decimos <b>YUMMY!</b> Si no nos gusta decimos <b>YUCK!</b>"),
  IMG("Rico o feo", "Dos palabras.", FG.tiras(["YUMMY! = ¡RICO!", "YUCK! = ¡PUAJ!"], numeros=False, cols=1)),
 ]),
 S(1, "Con respeto", [
  P("A cada uno le gusta algo distinto. Decimos <b>YUCK</b> sin ofender."),
  IMG("Respeto", "Gustos distintos.", FG.tiras(["SOFI: APPLES, YUMMY!", "TOMI: APPLES, YUCK!"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las caras de los chicos. Las vas a usar en la carpeta."),
  IMG("Las caras", "¿Les gusta?", FG.tiras(["SOFI SONRÍE CON LA BANANA", "TOMI PONE CARA FEA CON LA LECHE"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi prueba", "planteo": "Sofi prueba una frutilla.", "pasos": ["Le encanta.", "Dice: YUMMY!", "¡Qué rica!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "No me gusta: ___!", "pasos": ["___!"]},
"ejemplo_solo": {"titulo": "A probar", "planteo": "Probá una fruta y decí YUMMY o YUCK."},
"tip": {"titulo": "Con la cara", "texto": "YUMMY con sonrisa, YUCK con cara fea."},
"ojo": ["YUMMY es rico.", "YUCK es feo."],
"resumen": [{"titulo": "YUMMY", "texto": "¡Rico!"}, {"titulo": "YUCK", "texto": "¡Puaj!"}, {"titulo": "Gustos", "texto": "Cada uno el suyo."}],
"glosario": [{"palabra": "YUMMY", "significado": "¡Rico!"}, {"palabra": "YUCK", "significado": "¡Puaj!"}],
"carpeta": ["Sofi sonríe con la banana. ¿Qué dice?", "Tomi pone cara fea con la leche. ¿Qué dice?", "Leo sonríe con la manzana y dice YUCK. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("YUMMY", "YUMMY!"), acepta("YUCK", "YUCK!"), acepta("YUMMY", "YUMMY!")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "YUCK.", "solo": "Tu prueba.", "carpeta": ["YUMMY!", "YUCK!", "YUMMY!"]},
}

ACT = {
"1": [MC("MANZANA EN INGLÉS ES…", ["APPLE", "BANANA", "ORANGE"], "APPLE", "APPLE ES MANZANA.", n="recordar"),
      MC("ES AMARILLA Y LARGA. ¿QUÉ FRUTA ES?", ["BANANA", "APPLE", "ORANGE"], "BANANA", "LA BANANA ES AMARILLA.", n="aplicar"),
      MC("SOFI COME UNA NARANJA. ¿QUÉ DICE?", ["ORANGE", "APPLE", "BANANA"], "ORANGE", "NARANJA ES ORANGE.", n="aplicar")],
"2": [MC("A TOMI LE GUSTAN LAS MANZANAS. ¿QUÉ DICE?", ["I LIKE APPLES", "I HAVE A CAR", "I AM SIX"], "I LIKE APPLES", "LIKE ES GUSTAR.", n="aplicar"),
      ORD("ORDENÁ LA FRASE.", ["BANANAS", "I", "LIKE"], ["I", "LIKE", "BANANAS"], "I LIKE BANANAS.", n="aplicar")],
"3": [MC("TOMI TOMA UN VASO DE LECHE. ¿QUÉ ES?", ["MILK", "WATER", "BREAD"], "MILK", "LECHE ES MILK.", n="aplicar"),
      MC("¿CUÁL SE COME?", ["BREAD", "MILK", "WATER"], "BREAD", "EL PAN SE COME.", n="analizar")],
"4": [MC("TE ENCANTA LA BANANA. ¿QUÉ DECÍS?", ["YUMMY!", "YUCK!", "GOODBYE!"], "YUMMY!", "YUMMY ES RICO.", n="aplicar"),
      MC("TOMI PONE CARA FEA Y DICE YUMMY. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR YUCK", "ESTÁ BIEN", "DEBE DECIR HELLO"], "DEBE DECIR YUCK", "CARA FEA: YUCK.", n="error")],
"5": [MC("RELÁMPAGO. BANANA EN INGLÉS ES…", ["BANANA", "APPLE", "MILK"], "BANANA", "BANANA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. AGUA EN INGLÉS ES…", ["WATER", "MILK", "BREAD"], "WATER", "WATER.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. TE GUSTAN LAS NARANJAS. DECÍS I LIKE…", ["ORANGES", "MILK", "CARS"], "ORANGES", "ORANGES.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ALGO MUY RICO ES…", ["YUMMY", "YUCK", "SAD"], "YUMMY", "YUMMY.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("NARANJA EN INGLÉS ES…", ["ORANGE", "APPLE", "BANANA"], "ORANGE", "ORANGE ES NARANJA.", n="recordar")],
 [1, SA("ES ROJA Y REDONDA. ESCRIBÍ SU NOMBRE EN INGLÉS.", acepta("APPLE", "AN APPLE"), "APPLE.", n="aplicar")],
 [1, MC("SOFI COME UNA BANANA Y DICE ORANGE. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR BANANA", "ESTÁ BIEN", "DEBE DECIR APPLE"], "DEBE DECIR BANANA", "ES UNA BANANA.", n="error")],
 [2, MC("I LIKE APPLES QUIERE DECIR…", ["ME GUSTAN LAS MANZANAS", "TENGO MANZANAS", "NO ME GUSTAN"], "ME GUSTAN LAS MANZANAS", "LIKE ES GUSTAR.", n="recordar")],
 [2, SA("A LEO LE GUSTAN LAS BANANAS. COMPLETÁ: I LIKE…", acepta("BANANAS", "BANANA"), "BANANAS.", n="aplicar")],
 [2, MC("A ANA LE GUSTAN LAS NARANJAS. ¿QUÉ DICE?", ["I LIKE ORANGES", "I LIKE APPLES", "I HAVE ORANGES"], "I LIKE ORANGES", "LE GUSTAN LAS NARANJAS.", n="aplicar")],
 [3, MC("PAN EN INGLÉS ES…", ["BREAD", "MILK", "WATER"], "BREAD", "BREAD ES PAN.", n="recordar")],
 [3, SA("UN VASO DE AGUA. ESCRIBÍ AGUA EN INGLÉS.", acepta("WATER"), "WATER.", n="aplicar")],
 [3, MC("TOMI DICE QUE LA MILK SE COME CON TENEDOR. ¿QUÉ ESTÁ MAL?", ["LA LECHE SE TOMA", "ESTÁ BIEN", "LA LECHE ES PAN"], "LA LECHE SE TOMA", "LA MILK SE TOMA.", n="error")],
 [4, MC("YUCK QUIERE DECIR…", ["¡PUAJ!", "¡RICO!", "¡HOLA!"], "¡PUAJ!", "YUCK ES CUANDO NO NOS GUSTA.", n="recordar")],
 [4, MC("SOFI PRUEBA ALGO MUY RICO. ¿QUÉ DICE?", ["YUMMY!", "YUCK!", "BYE!"], "YUMMY!", "RICO ES YUMMY.", n="aplicar")],
 [4, MC("A TOMI NO LE GUSTA EL TOMATE. ¿QUÉ DICE?", ["YUCK!", "YUMMY!", "HELLO!"], "YUCK!", "NO LE GUSTA: YUCK.", n="aplicar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: Food I Like", "examen_titulo": "Nivel jefe: Food I Like",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
