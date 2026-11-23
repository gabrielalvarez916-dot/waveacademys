# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 15 · Una fábula para leer. Genera mision-15.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Fábula de trabajo: «El león y el ratón» (Esopo, dominio público), contada con palabras simples.
Niveles: 1 escuchar la fábula · 2 quiénes son los animales · 3 qué enseña · 4 contarla con mis palabras."""
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
import importlib.util
_s2 = importlib.util.spec_from_file_location('figuras_leng2', os.path.join(os.path.dirname(AQUI), '..', 'lengua-2', 'figuras.py'))
FG2 = importlib.util.module_from_spec(_s2); _s2.loader.exec_module(FG2)
low = lambda w: [w, w.lower(), w.capitalize()]
NO = ["NO", "no", "No"]
CUENTO = ["UN LEÓN DORMÍA.", "UN RATÓN LO DESPERTÓ.", "EL LEÓN LO DEJÓ IR.", "EL LEÓN CAYÓ EN UNA RED.", "EL RATÓN MORDIÓ LA RED.", "¡EL LEÓN QUEDÓ LIBRE!"]

N1 = {**ESTILO,
"objetivo": "Vas a escuchar la fábula El león y el ratón.",
"vas_a_ver": ["Qué es una fábula", "Lo que pasa", "Cómo termina"],
"secciones": [
 S(1, "Una fábula", [
  D("Fábula", "Cuento corto con <b>animales</b> que nos <b>enseña algo</b>."),
  P("Hoy: <b>EL LEÓN Y EL RATÓN</b>. La contó <b>Esopo</b>, hace muchísimo."),
  IMG("Los animales", "Uno grande y uno chiquito.", FG2.objetos([("leon", "EL LEÓN"), ("raton", "EL RATÓN")])),
 ]),
 S(1, "Lo que pasa", [
  IMG("La fábula", "Leela con alguien.", FG.tiras(CUENTO[:4], numeros=True)),
  IMG("El final", "¡El ratón ayudó!", FG.tiras(CUENTO[4:], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("Tiras", "¿Qué pasó primero?", FG.tiras(["EL RATÓN MORDIÓ LA RED.", "UN LEÓN DORMÍA."], numeros=False)),
 ]),
],
"ejemplo_completo": {"titulo": "El principio", "planteo": "¿Cómo empieza la fábula?", "pasos": ["Un león dormía.", "Un ratón lo despertó.", "Así empieza."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El león cayó en una…", "pasos": ["El león cayó en una ___ ."]},
"ejemplo_solo": {"titulo": "Contala", "planteo": "Contale la fábula a alguien de tu casa."},
"tip": {"titulo": "Escuchá", "texto": "Prestá atención a lo que hace cada animal."},
"ojo": ["El ratón es chiquito, pero ayuda.", "En las fábulas los animales hablan."],
"resumen": [{"titulo": "Fábula", "texto": "Cuento con animales."}, {"titulo": "Principio", "texto": "El ratón despierta al león."}, {"titulo": "Final", "texto": "El ratón lo salva."}],
"glosario": [{"palabra": "Red", "significado": "Trampa hecha con sogas."}, {"palabra": "Morder", "significado": "Apretar con los dientes."}],
"carpeta": ["De las tiras del dibujo, ¿cuál pasó primero?", "¿Quién mordió la red?", "Tomi dice que el león salvó al ratón. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [low("UN LEÓN DORMÍA") + low("un leon dormia") + ["UN LEÓN DORMÍA.", "Un león dormía."], low("EL RATÓN") + low("RATÓN") + low("raton") + low("el raton"), NO],
"soluciones": {"incompleto": "RED.", "solo": "La fábula con tus palabras.", "carpeta": ["Un león dormía.", "El ratón.", "No: el ratón salvó al león."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer a los animales de la fábula.",
"vas_a_ver": ["El león", "El ratón", "Grande y chiquito"],
"secciones": [
 S(1, "El león", [
  P("El <b>león</b> es <b>grande</b> y <b>fuerte</b>. Es el rey de la selva."),
  IMG("El león", "Grande y fuerte.", FG2.objetos([("leon", "GRANDE Y FUERTE")])),
 ]),
 S(1, "El ratón", [
  P("El <b>ratón</b> es <b>chiquito</b>, pero muy <b>valiente</b>."),
  IMG("El ratón", "Chiquito y valiente.", FG2.objetos([("raton", "CHIQUITO Y VALIENTE")])),
 ]),
 S(2, "Para practicar", [
  P("Leé las palabras. Las vas a usar en la carpeta."),
  IMG("¿Cómo es?", "¿León o ratón?", FG.nombres(["GRANDE", "CHIQUITO", "FUERTE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El ratón", "planteo": "¿Cómo es el ratón?", "pasos": ["Es chiquito.", "Es valiente.", "Ayudó al león."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El león es…", "pasos": ["El león es ___ ."]},
"ejemplo_solo": {"titulo": "Dibujalos", "planteo": "Dibujá al león y al ratón."},
"tip": {"titulo": "Por lo que hacen", "texto": "Lo que hace cada animal muestra cómo es."},
"ojo": ["Ser chiquito no es ser débil.", "El ratón fue valiente."],
"resumen": [{"titulo": "León", "texto": "Grande y fuerte."}, {"titulo": "Ratón", "texto": "Chiquito y valiente."}, {"titulo": "Los dos", "texto": "Se ayudaron."}],
"glosario": [{"palabra": "Valiente", "significado": "Que se anima aunque dé miedo."}, {"palabra": "Fuerte", "significado": "Que tiene mucha fuerza."}],
"carpeta": ["¿Quién es CHIQUITO: el león o el ratón?", "¿Quién es FUERTE?", "Tomi dice que el ratón no ayudó porque es chiquito. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("EL RATÓN") + low("RATÓN") + low("raton") + low("el raton"), low("EL LEÓN") + low("LEÓN") + low("leon") + low("el leon"), NO],
"soluciones": {"incompleto": "GRANDE (o FUERTE).", "solo": "Tu dibujo.", "carpeta": ["El ratón.", "El león.", "No: el ratón lo ayudó."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a descubrir qué enseña la fábula.",
"vas_a_ver": ["La enseñanza", "Todos podemos ayudar", "Ayudar a otros"],
"secciones": [
 S(1, "La enseñanza", [
  D("Moraleja", "Es lo que nos <b>enseña</b> la fábula."),
  P("Esta fábula enseña: <b>todos podemos ayudar, aunque seamos chiquitos</b>."),
  IMG("El ratón ayuda", "Chiquito, pero muy útil.", FG2.objetos([("raton", "EL RATÓN"), ("red", "LA RED"), ("leon", "EL LEÓN")])),
 ]),
 S(1, "En la escuela", [
  P("También pasa en la escuela: <b>todos</b> podemos ayudar."),
  IMG("Ayudar", "Cosas que podemos hacer.", FG.tiras(["PRESTAR UN LÁPIZ", "LEVANTAR A UN AMIGO", "ORDENAR EL AULA"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Leé las frases. Las vas a usar en la carpeta."),
  IMG("¿Ayuda o no?", "Pensá en cada una.", FG.tiras(["1. LE PRESTO MI GOMA A TOMI.", "2. ME RÍO DE UN COMPAÑERO."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Moraleja", "planteo": "¿Qué aprendemos del ratón?", "pasos": ["Era chiquito.", "Igual ayudó.", "Todos podemos ayudar."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La moraleja.", "pasos": ["Todos podemos ___ ."]},
"ejemplo_solo": {"titulo": "Ayudá", "planteo": "Hoy ayudá a alguien en tu casa. Contá qué hiciste."},
"tip": {"titulo": "Preguntá", "texto": "¿Qué aprendí? Esa es la moraleja."},
"ojo": ["La moraleja no cuenta lo que pasó.", "Dice lo que aprendemos."],
"resumen": [{"titulo": "Moraleja", "texto": "Lo que enseña."}, {"titulo": "Esta fábula", "texto": "Todos podemos ayudar."}, {"titulo": "En la escuela", "texto": "También ayudamos."}],
"glosario": [{"palabra": "Moraleja", "significado": "Lo que enseña una fábula."}, {"palabra": "Ayudar", "significado": "Hacer algo bueno por otro."}],
"carpeta": ["¿Qué frase del dibujo es ayudar?", "Completá la moraleja: todos podemos…", "Tomi dice que la moraleja es: el león dormía. ¿Es una enseñanza?"],
"carpeta_nivel": ["analizar", "recordar", "error"],
"respuestas_carpeta": [["1", "LA 1", "la 1", "La 1"] + low("LE PRESTO MI GOMA A TOMI"), low("AYUDAR"), NO],
"soluciones": {"incompleto": "AYUDAR.", "solo": "Lo que hiciste.", "carpeta": ["La 1.", "Ayudar.", "No: eso cuenta lo que pasó."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a contar la fábula con tus palabras.",
"vas_a_ver": ["Principio", "Problema", "Final"],
"secciones": [
 S(1, "Tres partes", [
  P("Para contar, pensamos en <b>tres partes</b>."),
  IMG("Las tres partes", "Principio, problema y final.", FG.tiras(["PRINCIPIO: EL RATÓN DESPIERTA AL LEÓN.", "PROBLEMA: EL LEÓN CAE EN UNA RED.", "FINAL: EL RATÓN LO SALVA."], numeros=True, cols=1)),
 ]),
 S(1, "Con mis palabras", [
  P("No hace falta decir lo mismo. Contamos <b>con nuestras palabras</b>."),
  P("Usamos: <b>PRIMERO</b>, <b>DESPUÉS</b>, <b>AL FINAL</b>."),
  IMG("Palabras para contar", "Ordenan lo que pasa.", FG.nombres(["PRIMERO", "DESPUÉS", "AL FINAL"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las partes. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Cuál va primero?", FG.tiras(["EL RATÓN LO SALVA.", "EL RATÓN DESPIERTA AL LEÓN.", "EL LEÓN CAE EN UNA RED."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Contar", "planteo": "Cuento el principio.", "pasos": ["PRIMERO, un ratón despertó a un león.", "El león lo dejó ir.", "Así empieza."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cuento el final.", "pasos": ["AL FINAL, el ratón ___ al león."]},
"ejemplo_solo": {"titulo": "Contala", "planteo": "Contá la fábula a tu familia con PRIMERO, DESPUÉS y AL FINAL."},
"tip": {"titulo": "Palabras que ordenan", "texto": "PRIMERO, DESPUÉS y AL FINAL ayudan a contar."},
"ojo": ["No te saltees el problema.", "Contá en orden."],
"resumen": [{"titulo": "Principio", "texto": "Lo primero que pasa."}, {"titulo": "Problema", "texto": "La red."}, {"titulo": "Final", "texto": "El ratón lo salva."}],
"glosario": [{"palabra": "Principio", "significado": "Cómo empieza."}, {"palabra": "Problema", "significado": "Lo que sale mal."}],
"carpeta": ["De las partes del dibujo, ¿cuál va primero?", "¿Cuál va al final?", "Tomi contó el final antes que el principio. ¿Está bien?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("EL RATÓN DESPIERTA AL LEÓN") + low("el raton despierta al leon") + ["El ratón despierta al león."], low("EL RATÓN LO SALVA") + low("el raton lo salva") + ["El ratón lo salva."], NO],
"soluciones": {"incompleto": "SALVA.", "solo": "La fábula contada en orden.", "carpeta": ["El ratón despierta al león.", "El ratón lo salva.", "No: hay que contar en orden."]},
}

ACT = {
"1": [MC("¿QUIÉN DESPERTÓ AL LEÓN?", ["EL RATÓN", "UN PERRO", "UN PÁJARO"], "EL RATÓN", "EL RATÓN LO DESPERTÓ.", n="recordar"),
      ORD("ORDENÁ LA FÁBULA.", ["EL RATÓN MORDIÓ LA RED", "UN LEÓN DORMÍA", "EL LEÓN CAYÓ EN UNA RED"], ["UN LEÓN DORMÍA", "EL LEÓN CAYÓ EN UNA RED", "EL RATÓN MORDIÓ LA RED"], "PRIMERO DORMÍA.", n="analizar")],
"2": [UNI("UNÍ CADA ANIMAL CON CÓMO ES.", [("LEÓN", "GRANDE Y FUERTE"), ("RATÓN", "CHIQUITO Y VALIENTE")], "POR LO QUE HACEN.", n="analizar"),
      TF("EL RATÓN ES MÁS GRANDE QUE EL LEÓN.", "FALSO", "EL RATÓN ES CHIQUITO.", n="aplicar")],
"3": [MC("¿QUÉ ENSEÑA LA FÁBULA?", ["TODOS PODEMOS AYUDAR", "HAY QUE DORMIR MUCHO"], "TODOS PODEMOS AYUDAR", "AUNQUE SEAMOS CHIQUITOS.", n="aplicar"),
      SA("COMPLETÁ LA MORALEJA: TODOS PODEMOS ___", low("AYUDAR"), "AYUDAR.", n="recordar")],
"4": [ORD("ORDENÁ LAS PALABRAS PARA CONTAR.", ["AL FINAL", "PRIMERO", "DESPUÉS"], ["PRIMERO", "DESPUÉS", "AL FINAL"], "PRIMERO, DESPUÉS, AL FINAL.", n="analizar"),
      MC("¿CUÁL ES EL PROBLEMA DE LA FÁBULA?", ["EL LEÓN CAE EN UNA RED", "EL RATÓN COME QUESO"], "EL LEÓN CAE EN UNA RED", "ESO SALE MAL.", n="aplicar")],
"5": [MC("RELÁMPAGO. LA FÁBULA TIENE…", ["ANIMALES", "ROBOTS"], "ANIMALES", "UN LEÓN Y UN RATÓN.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUIÉN MORDIÓ LA RED?", ["EL RATÓN", "EL LEÓN"], "EL RATÓN", "CON SUS DIENTES.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL RATÓN ES…", ["VALIENTE", "MALO"], "VALIENTE", "SE ANIMÓ A AYUDAR.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿QUÉ PALABRA VA AL FINAL?", ["AL FINAL", "PRIMERO"], "AL FINAL", "CIERRA EL CUENTO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ HACÍA EL LEÓN AL PRINCIPIO?", ["DORMÍA", "CORRÍA", "COMÍA"], "DORMÍA", "UN LEÓN DORMÍA.", n="recordar")],
 [1, SA("EL LEÓN CAYÓ EN UNA ___", low("RED"), "RED.", n="recordar")],
 [1, TF("EL LEÓN SALVÓ AL RATÓN DE LA RED.", "FALSO", "EL RATÓN SALVÓ AL LEÓN.", n="error")],
 [2, MC("¿CÓMO ES EL LEÓN?", ["GRANDE Y FUERTE", "CHIQUITO Y GRIS"], "GRANDE Y FUERTE", "ES EL REY DE LA SELVA.", n="aplicar")],
 [2, SA("¿QUIÉN ES CHIQUITO Y VALIENTE?", low("EL RATÓN") + low("RATÓN") + low("raton") + low("el raton"), "EL RATÓN.", n="aplicar")],
 [2, TF("SER CHIQUITO QUIERE DECIR QUE NO PODÉS AYUDAR.", "FALSO", "EL RATÓN AYUDÓ.", n="error")],
 [3, MC("¿QUÉ ES LA MORALEJA?", ["LO QUE ENSEÑA LA FÁBULA", "EL NOMBRE DEL LEÓN"], "LO QUE ENSEÑA LA FÁBULA", "LO QUE APRENDEMOS.", n="recordar")],
 [3, MC("A SOFI SE LE ROMPIÓ EL LÁPIZ. ¿QUÉ HACÉS PARA AYUDAR?", ["LE PRESTO EL MÍO", "ME RÍO DE ELLA"], "LE PRESTO EL MÍO", "AYUDAR ES HACER ALGO BUENO.", n="aplicar")],
 [3, TF("LA MORALEJA ES: EL LEÓN DORMÍA.", "FALSO", "ESO CUENTA LO QUE PASÓ.", n="error")],
 [4, ORD("ORDENÁ LAS PARTES.", ["EL RATÓN LO SALVA", "EL RATÓN DESPIERTA AL LEÓN", "EL LEÓN CAE EN UNA RED"], ["EL RATÓN DESPIERTA AL LEÓN", "EL LEÓN CAE EN UNA RED", "EL RATÓN LO SALVA"], "PRINCIPIO, PROBLEMA, FINAL.", n="analizar")],
 [4, SA("COMPLETÁ: AL FINAL, EL RATÓN ___ AL LEÓN", low("SALVA") + low("SALVÓ") + low("salvo") + low("AYUDA") + low("AYUDÓ") + low("ayudo"), "LO SALVA.", n="aplicar")],
 [4, MC("¿QUÉ PALABRA USAMOS PARA EMPEZAR A CONTAR?", ["PRIMERO", "AL FINAL"], "PRIMERO", "PRIMERO, DESPUÉS, AL FINAL.", n="recordar")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 15, "estilo": "primeros",
     "practica": "Práctica general: una fábula para leer", "examen_titulo": "Nivel jefe: una fábula para leer",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-15.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
