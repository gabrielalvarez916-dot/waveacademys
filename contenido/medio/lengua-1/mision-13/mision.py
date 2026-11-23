# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 13 · El abecedario. Genera mision-13.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras: dice palabras ancla —«la de avión»—; el PDF muestra las letras).
Metáfora: el álbum completo de Sofi (ya tiene las 27 letras y ahora las ordena).
Niveles: 1 el abecedario en orden · 2 mayúsculas y minúsculas · 3 ordenar nombres por la primera letra · 4 buscar palabras en un listado."""
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
TF = lambda p, ok, e, **k: {"t": "true_false", "p": p, "o": ["VERDADERO", "FALSO"], "r": {"correcta": ok}, "e": e, **k}
UNI = lambda p, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": [a for a, _ in pares], "derecha": [b for _, b in pares]}, "r": {"pares": dict(pares)}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
low = lambda w: [w, w.lower(), w.capitalize()]
NO = ["NO", "no", "No"]

N1 = {**ESTILO,
"objetivo": "Vas a conocer el abecedario en orden.",
"vas_a_ver": ["Qué es el abecedario", "Las 27 letras", "Siempre en el mismo orden"],
"secciones": [
 S(1, "El abecedario", [
  D("Abecedario", "Son <b>todas las letras</b>, siempre en el <b>mismo orden</b>."),
  P("En castellano son <b>27 letras</b>. Empieza con la <b>A</b> y termina con la <b>Z</b>."),
  IMG("El abecedario", "De la A a la Z.", FG.abecedario()),
 ]),
 S(1, "Antes y después", [
  P("Cada letra tiene una que va <b>antes</b> y otra que va <b>después</b>."),
  P("Después de la <b>A</b> va la <b>B</b>. Después de la <b>N</b> va la <b>Ñ</b>."),
  IMG("Vecinas", "Tres letras seguidas.", FG.abecedario(letras_="MNÑ", resaltar="N")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las letras. Las vas a usar en la carpeta."),
  IMG("¿Qué letra falta?", "Pensá en el orden.", FG.nombres(["A _ C", "D _ F", "Ñ _ P"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Después", "planteo": "¿Qué letra va después de la D?", "pasos": ["Digo el abecedario.", "A, B, C, D…", "Después va la E."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí la letra que falta.", "pasos": ["L, ___ , N."]},
"ejemplo_solo": {"titulo": "Cantalo", "planteo": "Decí el abecedario en voz alta con alguien de tu casa."},
"tip": {"titulo": "Por partes", "texto": "Aprendelo de a pedacitos: A a la G, H a la N…"},
"ojo": ["La Ñ va después de la N.", "Son 27 letras, no 26."],
"resumen": [{"titulo": "Abecedario", "texto": "Todas las letras en orden."}, {"titulo": "27", "texto": "De la A a la Z."}, {"titulo": "Orden", "texto": "Siempre el mismo."}],
"glosario": [{"palabra": "Abecedario", "significado": "Todas las letras en orden."}, {"palabra": "Orden", "significado": "Quién va primero y quién después."}],
"carpeta": ["¿Qué letra falta en A _ C?", "¿Qué letra falta en Ñ _ P?", "Tomi dice que después de la N va la O. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("B"), low("O"), NO],
"soluciones": {"incompleto": "M.", "solo": "El abecedario completo.", "carpeta": ["B.", "O.", "No: va la Ñ."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer las mayúsculas y las minúsculas.",
"vas_a_ver": ["Letra grande y letra chica", "Las dos formas", "Cuándo va la mayúscula"],
"secciones": [
 S(1, "Dos formas", [
  D("Mayúscula y minúscula", "Cada letra tiene una forma <b>grande</b> y una <b>chica</b>. Es la misma letra."),
  IMG("El abecedario con sus dos formas", "Arriba la grande, abajo la chica.", FG.abecedario(minusculas=True)),
 ]),
 S(1, "Cuándo va la grande", [
  P("La <b>mayúscula</b> va al principio de los <b>nombres</b>: Sofi, Tomi, Ana."),
  P("También al <b>principio</b> de una oración."),
  IMG("Nombres", "Empiezan con mayúscula.", FG.letras("Sofi", resaltar=(0,), tal_cual=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las letras. Las vas a usar en la carpeta."),
  IMG("Parejas", "Grande y chica.", FG.abecedario(minusculas=True, letras_="MST")),
 ]),
],
"ejemplo_completo": {"titulo": "Dos formas", "planteo": "¿Cómo es la M chica?", "pasos": ["La grande: M.", "La chica: m.", "Es la misma letra."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La grande y la chica.", "pasos": ["A y ___ .", "B y ___ ."]},
"ejemplo_solo": {"titulo": "Tu nombre", "planteo": "Escribí tu nombre con la primera letra grande y las demás chicas."},
"tip": {"titulo": "Nombres con grande", "texto": "Tu nombre empieza siempre con mayúscula."},
"ojo": ["La grande y la chica son la misma letra.", "Algunas cambian mucho: A y a."],
"resumen": [{"titulo": "Mayúscula", "texto": "La grande."}, {"titulo": "Minúscula", "texto": "La chica."}, {"titulo": "Nombres", "texto": "Empiezan con mayúscula."}],
"glosario": [{"palabra": "Mayúscula", "significado": "La letra grande."}, {"palabra": "Minúscula", "significado": "La letra chica."}],
"carpeta": ["¿Cuál es la chica de la S?", "¿Con qué letra empieza el nombre SOFI: grande o chica?", "Tomi dice que la A y la a son letras distintas. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["s", "S", "la s"], low("GRANDE") + low("MAYÚSCULA") + low("mayuscula") + low("con mayúscula"), NO],
"soluciones": {"incompleto": "a. b.", "solo": "Tu nombre bien escrito.", "carpeta": ["s.", "Grande: mayúscula.", "No: es la misma letra."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ordenar nombres por la primera letra.",
"vas_a_ver": ["Mirar la primera letra", "Buscarla en el abecedario", "Ordenar"],
"secciones": [
 S(1, "La lista del grado", [
  P("La maestra quiere la lista <b>en orden</b>."),
  P("Miramos la <b>primera letra</b> de cada nombre."),
  IMG("Nombres sin orden", "¿Quién va primero?", FG.nombres(["TOMI", "ANA", "SOFI", "BETO"], True, 4)),
 ]),
 S(1, "Ordenar", [
  P("ANA empieza con <b>A</b>: va primero. Después <b>B</b>, de BETO."),
  P("Después <b>S</b>, de SOFI, y <b>T</b>, de TOMI."),
  IMG("La lista ordenada", "Como en el abecedario.", FG.lista(["ANA", "BETO", "SOFI", "TOMI"], titulo="LISTA DEL GRADO")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los nombres. Los vas a usar en la carpeta."),
  IMG("Para ordenar", "Mirá la primera letra.", FG.nombres(["LUZ", "DANI", "MATEO"], True, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenar", "planteo": "PEPE y CARLA, ¿quién va primero?", "pasos": ["PEPE empieza con P.", "CARLA empieza con C.", "La C va antes: CARLA primero."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Ordená: EMA, BRUNO.", "pasos": ["Primero ___ , después ___ ."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "Escribí los nombres de tu familia en orden."},
"tip": {"titulo": "Mirá el abecedario", "texto": "Si dudás, buscá las letras en el abecedario."},
"ojo": ["Miramos solo la primera letra.", "No importa si el nombre es largo o corto."],
"resumen": [{"titulo": "Mirar", "texto": "La primera letra."}, {"titulo": "Buscar", "texto": "En el abecedario."}, {"titulo": "Ordenar", "texto": "La que va antes, primero."}],
"glosario": [{"palabra": "Lista", "significado": "Nombres uno abajo del otro."}, {"palabra": "Ordenar", "significado": "Poner cada cosa en su lugar."}],
"carpeta": ["De los nombres del dibujo, ¿cuál va primero?", "¿Cuál va último?", "Tomi puso MATEO antes que DANI. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("DANI"), low("MATEO"), NO],
"soluciones": {"incompleto": "BRUNO. EMA.", "solo": "Los nombres de tu familia en orden.", "carpeta": ["DANI.", "MATEO.", "No: la D va antes que la M."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a buscar palabras en un listado.",
"vas_a_ver": ["Listados en orden", "Buscar por la primera letra", "Encontrar rápido"],
"secciones": [
 S(1, "Listados", [
  P("Muchos listados están en orden de <b>abecedario</b>."),
  P("Así es más fácil <b>encontrar</b> una palabra."),
  IMG("Lista de frutas", "En orden.", FG.lista(["BANANA", "KIWI", "MANZANA", "PERA", "UVA"], titulo="FRUTAS")),
 ]),
 S(1, "Buscar", [
  P("¿Dónde está <b>PERA</b>? Empieza con <b>P</b>."),
  P("La P está casi al final del abecedario. ¡Busco abajo!"),
  IMG("¡La encontré!", "PERA, en el lugar de la P.", FG.lista(["BANANA", "KIWI", "MANZANA", "PERA", "UVA"], titulo="FRUTAS", marcar=(3,))),
 ]),
 S(2, "Para practicar", [
  P("Mirá el listado. Lo vas a usar en la carpeta."),
  IMG("Animales", "Un listado en orden.", FG.lista(["GATO", "LORO", "OSO", "RANA", "ZORRO"], titulo="ANIMALES")),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar", "planteo": "¿Dónde está KIWI?", "pasos": ["Empieza con K.", "La K está en el medio.", "Está después de BANANA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En la lista de frutas…", "pasos": ["La primera es ___ .", "La última es ___ ."]},
"ejemplo_solo": {"titulo": "Tu listado", "planteo": "Escribí cinco animales en orden de abecedario."},
"tip": {"titulo": "Primera letra", "texto": "Pensá dónde está la letra: al principio, en el medio o al final."},
"ojo": ["La A está arriba de todo.", "La Z está abajo de todo."],
"resumen": [{"titulo": "Listado", "texto": "En orden de abecedario."}, {"titulo": "Buscar", "texto": "Por la primera letra."}, {"titulo": "Rápido", "texto": "Sin leer todo."}],
"glosario": [{"palabra": "Listado", "significado": "Lista de palabras."}, {"palabra": "Encontrar", "significado": "Dar con lo que buscás."}],
"carpeta": ["En la lista de animales, ¿cuál es el primero?", "¿Qué animal está después de OSO?", "Tomi buscó ZORRO arriba de todo. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("GATO"), low("RANA"), NO],
"soluciones": {"incompleto": "BANANA. UVA.", "solo": "Cinco animales en orden.", "carpeta": ["GATO.", "RANA.", "No: la Z está abajo de todo."]},
}

ACT = {
"1": [MC("¿QUÉ LETRA VA DESPUÉS DE LA N?", ["Ñ", "O", "M"], "Ñ", "N, Ñ, O.", n="recordar"),
      SA("COMPLETÁ: D, E, ___", low("F"), "D, E, F.", n="aplicar")],
"2": [UNI("UNÍ CADA GRANDE CON SU CHICA.", [("A", "a"), ("M", "m"), ("T", "t")], "ES LA MISMA LETRA.", n="analizar"),
      TF("LOS NOMBRES EMPIEZAN CON MAYÚSCULA.", "VERDADERO", "COMO SOFI Y TOMI.", n="recordar")],
"3": [ORD("ORDENÁ LOS NOMBRES.", ["TOMI", "ANA", "SOFI"], ["ANA", "SOFI", "TOMI"], "A, S, T.", n="analizar"),
      MC("¿QUIÉN VA PRIMERO?", ["CARLA", "PEPE"], "CARLA", "LA C VA ANTES QUE LA P.", n="aplicar")],
"4": [MC("EN UN LISTADO, ¿DÓNDE BUSCO ZORRO?", ["ABAJO DE TODO", "ARRIBA DE TODO"], "ABAJO DE TODO", "LA Z ES LA ÚLTIMA.", n="aplicar"),
      SA("EN LA LISTA DE ANIMALES, ¿QUÉ ANIMAL VA PRIMERO?", low("GATO"), "GATO.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿CUÁNTAS LETRAS TIENE EL ABECEDARIO?", ["27", "10"], "27", "DE LA A A LA Z.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ES LA PRIMERA?", ["A", "Z"], "A", "EMPIEZA CON A.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUIÉN VA ANTES?", ["BETO", "LUZ"], "BETO", "LA B VA ANTES.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ES LA ÚLTIMA LETRA?", ["Z", "Y"], "Z", "TERMINA CON Z.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ LETRA VA DESPUÉS DE LA A?", ["B", "C", "Z"], "B", "A, B, C.", n="recordar")],
 [1, SA("COMPLETÁ: L, ___, N", low("M"), "L, M, N.", n="aplicar")],
 [1, TF("EL ABECEDARIO TIENE 27 LETRAS.", "VERDADERO", "CONTANDO LA Ñ.", n="recordar")],
 [2, UNI("UNÍ CADA GRANDE CON SU CHICA.", [("B", "b"), ("S", "s"), ("E", "e")], "ES LA MISMA LETRA.", n="analizar")],
 [2, MC("¿CÓMO EMPIEZA TU NOMBRE?", ["CON MAYÚSCULA", "CON MINÚSCULA"], "CON MAYÚSCULA", "LOS NOMBRES EMPIEZAN CON GRANDE.", n="aplicar")],
 [2, TF("LA M Y LA m SON LETRAS DISTINTAS.", "FALSO", "ES LA MISMA LETRA: GRANDE Y CHICA.", n="error")],
 [3, ORD("ORDENÁ LOS NOMBRES.", ["MATEO", "DANI", "LUZ"], ["DANI", "LUZ", "MATEO"], "D, L, M.", n="analizar")],
 [3, MC("¿QUIÉN VA ÚLTIMO EN LA LISTA?", ["TOMI", "ANA", "BETO"], "TOMI", "LA T VA DESPUÉS.", n="aplicar")],
 [3, TF("PARA ORDENAR NOMBRES MIRAMOS LA ÚLTIMA LETRA.", "FALSO", "MIRAMOS LA PRIMERA.", n="error")],
 [4, MC("EN UNA LISTA EN ORDEN, ¿DÓNDE ESTÁ ANA?", ["ARRIBA", "ABAJO"], "ARRIBA", "LA A ES LA PRIMERA.", n="aplicar")],
 [4, SA("LISTA: GATO, LORO, OSO. ¿QUÉ ANIMAL VA DESPUÉS DE LORO?", low("OSO"), "OSO.", n="aplicar")],
 [4, MC("¿CUÁL LISTA ESTÁ EN ORDEN?", ["ANA, BETO, SOFI", "SOFI, ANA, BETO"], "ANA, BETO, SOFI", "A, B, S.", n="analizar")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 13, "estilo": "primeros",
     "practica": "Práctica general: el abecedario", "examen_titulo": "Nivel jefe: el abecedario",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-13.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
