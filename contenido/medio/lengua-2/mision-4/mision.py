# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 4 · Qué pasó primero y qué pasó después. Genera mision-4.json.
Regla de primeros años y vía fonológica. Cuento de trabajo: Los tres chanchitos (tradicional, contado con palabras simples).
Metáfora: el cuaderno viajero de Sofi (pega las escenas del cuento en orden).
Niveles: 1 ordenar las escenas · 2 palabras que ordenan · 3 resumir en tres oraciones · 4 contar el cuento ordenado."""
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
ESC = ["LOS CHANCHITOS HACEN SUS CASAS.", "EL LOBO SOPLA LA CASA DE PAJA.", "EL LOBO SOPLA LA CASA DE MADERA.", "LA CASA DE LADRILLOS NO SE CAE."]

N1 = {**ESTILO,
"objetivo": "Vas a ordenar las escenas de un cuento.",
"vas_a_ver": ["El cuento de los tres chanchitos", "Qué pasó primero", "Qué pasó después"],
"secciones": [
 S(1, "Los tres chanchitos", [
  P("Tres chanchitos hicieron sus casas."),
  P("Uno de paja, otro de madera y otro de ladrillos."),
  P("El lobo sopló y tiró la de paja. Después, la de madera."),
  P("La casa de ladrillos <b>no se cayó</b>. ¡Los chanchitos se salvaron!"),
  IMG("Las escenas", "En orden, del 1 al 4.", FG.tiras(ESC, numeros=True)),
 ]),
 S(1, "Ordenar escenas", [
  D("Escena", "Es una parte del cuento. Las escenas van <b>en orden</b>."),
  P("Si cambiamos el orden, el cuento <b>no se entiende</b>."),
  IMG("Mezcladas", "Así no se entiende.", FG.tiras([ESC[3], ESC[0], ESC[2], ESC[1]], numeros=True, ocultar_num=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("Para ordenar", "¿Cuál va primero?", FG.tiras([ESC[2], ESC[1], ESC[0]], numeros=True, ocultar_num=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenamos", "planteo": "¿Qué pasa primero?", "pasos": ["Primero hacen las casas.", "Después sopla el lobo.", "Al final, se salvan."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿Qué casa sopla primero el lobo?", "pasos": ["Primero sopla la casa de ___ ."]},
"ejemplo_solo": {"titulo": "Tu orden", "planteo": "Dibujá en tu carpeta tres escenas del cuento, en orden."},
"tip": {"titulo": "Pensá en el cuento", "texto": "¿Qué tiene que pasar antes?"},
"ojo": ["El final no va primero.", "Cada escena va en su lugar."],
"resumen": [{"titulo": "Escena", "texto": "Una parte del cuento."}, {"titulo": "Orden", "texto": "Primero, después, al final."}, {"titulo": "Mezclado", "texto": "No se entiende."}],
"glosario": [{"palabra": "Escena", "significado": "Una parte del cuento."}, {"palabra": "Orden", "significado": "Cuál va primero y cuál después."}],
"carpeta": ["¿Qué tira va primero?", "¿Qué casa sopla el lobo después de la de paja?", "Tomi puso primero que el lobo sopla. ¿Qué pasa antes?"],
"carpeta_nivel": ["analizar", "recordar", "error"],
"respuestas_carpeta": [low("LOS CHANCHITOS HACEN SUS CASAS") + low("HACEN SUS CASAS") + low("LA 3") + ["3", "tres"], low("LA DE MADERA") + low("MADERA"), low("HACEN SUS CASAS") + low("LOS CHANCHITOS HACEN SUS CASAS")],
"soluciones": {"incompleto": "PAJA.", "solo": "Tres dibujos en orden.", "carpeta": ["Los chanchitos hacen sus casas.", "La de madera.", "Los chanchitos hacen sus casas."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a usar palabras que ordenan: primero, luego, al final.",
"vas_a_ver": ["Primero", "Luego", "Al final"],
"secciones": [
 S(1, "Palabras que ordenan", [
  D("Palabras que ordenan", "<b>Primero</b>, <b>luego</b> y <b>al final</b> dicen en qué orden pasan las cosas."),
  P("<b>Primero</b>, los chanchitos hacen sus casas."),
  P("<b>Luego</b>, el lobo sopla."),
  P("<b>Al final</b>, se salvan en la casa de ladrillos."),
  IMG("Con palabras que ordenan", "Primero, luego, al final.", FG.tiras(["PRIMERO, HACEN SUS CASAS.", "LUEGO, EL LOBO SOPLA.", "AL FINAL, SE SALVAN."], numeros=True)),
 ]),
 S(1, "Otras palabras", [
  P("También sirven: <b>después</b>, <b>entonces</b>, <b>por último</b>."),
  IMG("Palabras para ordenar", "Van al principio de la oración.", FG.nombres(["PRIMERO", "LUEGO", "DESPUÉS", "AL FINAL"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("¿Qué palabra va?", "Completá con primero, luego o al final.", FG.tiras(["___ , ME LEVANTO.", "___ , DESAYUNO.", "___ , VOY A LA ESCUELA."], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi mañana", "planteo": "Ordená con palabras.", "pasos": ["Primero, me despierto.", "Luego, me visto.", "Al final, desayuno."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí la palabra que falta.", "pasos": ["___ , el lobo sopla la casa de paja."]},
"ejemplo_solo": {"titulo": "Tu tarde", "planteo": "Contá tu tarde con primero, luego y al final."},
"tip": {"titulo": "Al principio", "texto": "Las palabras que ordenan van al principio de la oración."},
"ojo": ["Al final no va al principio del cuento.", "Después de la palabra va una coma."],
"resumen": [{"titulo": "Primero", "texto": "Lo que pasa antes."}, {"titulo": "Luego", "texto": "Lo que sigue."}, {"titulo": "Al final", "texto": "Lo último."}],
"glosario": [{"palabra": "Luego", "significado": "Después."}, {"palabra": "Al final", "significado": "Lo último que pasa."}],
"carpeta": ["¿Qué palabra va en la tira 1?", "¿Qué palabra va en la tira 2?", "Sofi escribió AL FINAL, ME LEVANTO. ¿Qué palabra va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PRIMERO"), low("LUEGO") + low("DESPUÉS") + low("despues"), low("PRIMERO")],
"soluciones": {"incompleto": "Luego.", "solo": "Por ejemplo: Primero, almuerzo. Luego, juego. Al final, me baño.", "carpeta": ["Primero.", "Luego.", "Primero: levantarse es lo primero."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a contar el cuento en tres oraciones.",
"vas_a_ver": ["Qué es resumir", "Principio, medio y final", "Tres oraciones"],
"secciones": [
 S(1, "Resumir", [
  D("Resumir", "Es contar el cuento <b>corto</b>, con lo más importante."),
  P("Una oración para el <b>principio</b> y otra para el <b>medio</b>."),
  P("Y una oración más para el <b>final</b>."),
  IMG("Tres partes", "Principio, medio y final.", FG.nombres(["PRINCIPIO", "MEDIO", "FINAL"], cols=3)),
 ]),
 S(1, "El resumen de los chanchitos", [
  P("1. Tres chanchitos hacen casas."),
  P("2. El lobo sopla dos casas."),
  P("3. Se salvan en la de ladrillos."),
  IMG("El resumen", "Tres oraciones.", FG.tiras(["TRES CHANCHITOS HACEN CASAS.", "EL LOBO SOPLA DOS CASAS.", "SE SALVAN EN LA DE LADRILLOS."], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("¿Va en el resumen?", "Solo lo importante.", FG.tiras(["EL LOBO SOPLA DOS CASAS.", "EL LOBO TENÍA BIGOTES."], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Cenicienta", "planteo": "Contá Cenicienta en tres oraciones.", "pasos": ["Cenicienta va al baile con magia.", "Pierde un zapatito a las doce.", "El príncipe la encuentra."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Completá el final del resumen.", "pasos": ["Al final, los chanchitos se ___ ."]},
"ejemplo_solo": {"titulo": "Tu resumen", "planteo": "Escribí en tres oraciones un cuento que te guste."},
"tip": {"titulo": "Solo lo importante", "texto": "Si se puede sacar, no va en el resumen."},
"ojo": ["El resumen no cuenta todo.", "No te olvides del final."],
"resumen": [{"titulo": "Resumir", "texto": "Contar corto."}, {"titulo": "Tres oraciones", "texto": "Principio, medio y final."}, {"titulo": "Importante", "texto": "Lo que no se puede sacar."}],
"glosario": [{"palabra": "Resumen", "significado": "El cuento contado corto."}, {"palabra": "Importante", "significado": "Lo que no se puede sacar."}],
"carpeta": ["¿Cuál tira va en el resumen?", "¿En qué casa se salvan los chanchitos?", "Tomi resumió solo el principio. ¿Qué parte le falta además del medio?"],
"carpeta_nivel": ["analizar", "recordar", "error"],
"respuestas_carpeta": [["1", "la 1", "LA 1", "uno"] + low("EL LOBO SOPLA DOS CASAS"), low("EN LA DE LADRILLOS") + low("LADRILLOS") + low("LA DE LADRILLOS"), low("EL FINAL") + low("FINAL")],
"soluciones": {"incompleto": "SALVAN.", "solo": "Tu resumen en tres oraciones.", "carpeta": ["La 1: es importante.", "En la de ladrillos.", "El final."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a contar el cuento entero y en orden.",
"vas_a_ver": ["Contar en voz alta", "Usar palabras que ordenan", "Revisar el orden"],
"secciones": [
 S(1, "Contar en orden", [
  P("Sofi le cuenta el cuento a su hermanito."),
  P("<b>Primero</b>, los chanchitos hacen sus casas. <b>Luego</b>, viene el lobo."),
  P("<b>Después</b>, sopla dos casas. <b>Al final</b>, se salvan."),
  IMG("Sofi cuenta", "Con palabras que ordenan.", FG.tiras(["PRIMERO, HACEN SUS CASAS.", "LUEGO, VIENE EL LOBO.", "DESPUÉS, SOPLA DOS CASAS.", "AL FINAL, SE SALVAN."], numeros=True)),
 ]),
 S(1, "Revisar", [
  D("Revisar", "Leemos lo que contamos y vemos si <b>está en orden</b>."),
  P("Si algo está fuera de lugar, lo cambiamos."),
  IMG("Las escenas", "¿Están en orden?", FG.tiras(ESC, numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("Para revisar", "¿Algo está fuera de lugar?", FG.tiras(["PRIMERO, SE SALVAN.", "LUEGO, VIENE EL LOBO.", "AL FINAL, HACEN SUS CASAS."], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Contar Cenicienta", "planteo": "Contá Cenicienta en orden.", "pasos": ["Primero, Cenicienta limpia.", "Luego, va al baile.", "Al final, el príncipe la encuentra."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Completá con palabras que ordenan.", "pasos": ["___ , viene el lobo.", "___ , se salvan."]},
"ejemplo_solo": {"titulo": "Tu cuento", "planteo": "Contale a alguien de tu casa el cuento de los tres chanchitos."},
"tip": {"titulo": "Contá con calma", "texto": "Usá primero, luego y al final."},
"ojo": ["No empieces por el final.", "Revisá el orden antes de terminar."],
"resumen": [{"titulo": "Contar", "texto": "En voz alta."}, {"titulo": "Ordenar", "texto": "Con primero, luego, al final."}, {"titulo": "Revisar", "texto": "Que esté en orden."}],
"glosario": [{"palabra": "Contar", "significado": "Decir lo que pasa en un cuento."}, {"palabra": "Revisar", "significado": "Mirar de nuevo para mejorar."}],
"carpeta": ["¿Qué tira está mal en el primer lugar?", "¿Qué pasa primero de verdad?", "¿Qué pasa al final de verdad?"],
"carpeta_nivel": ["error", "aplicar", "aplicar"],
"respuestas_carpeta": [["1", "la 1", "LA 1", "uno"] + low("PRIMERO, SE SALVAN"), low("HACEN SUS CASAS") + low("LOS CHANCHITOS HACEN SUS CASAS"), low("SE SALVAN") + low("LOS CHANCHITOS SE SALVAN")],
"soluciones": {"incompleto": "Luego. Al final.", "solo": "Lo contás en orden.", "carpeta": ["La 1: salvarse es el final.", "Hacen sus casas.", "Se salvan."]},
}

ACT = {
"1": [ORD("ORDENÁ LAS ESCENAS.", [ESC[2], ESC[0], ESC[1]], [ESC[0], ESC[1], ESC[2]], "PRIMERO LAS CASAS, DESPUÉS EL LOBO.", n="analizar"),
      MC("¿QUÉ PASA AL FINAL?", ["LA CASA DE LADRILLOS NO SE CAE", "EL LOBO SOPLA LA PAJA", "HACEN SUS CASAS"], "LA CASA DE LADRILLOS NO SE CAE", "ES EL FINAL.", n="recordar")],
"2": [MC("___ , ME LEVANTO. ¿QUÉ PALABRA VA?", ["PRIMERO", "AL FINAL"], "PRIMERO", "ES LO PRIMERO DEL DÍA.", n="aplicar"),
      UNI("UNÍ CADA PALABRA CON SU MOMENTO.", [("PRIMERO", "LO QUE PASA ANTES"), ("LUEGO", "LO QUE SIGUE"), ("AL FINAL", "LO ÚLTIMO")], "PALABRAS QUE ORDENAN.", n="recordar")],
"3": [TF("EL RESUMEN CUENTA TODO, CON TODOS LOS DETALLES.", "FALSO", "SOLO LO IMPORTANTE.", n="analizar"),
      MC("¿QUÉ VA EN EL RESUMEN?", ["EL LOBO SOPLA DOS CASAS", "EL LOBO TENÍA BIGOTES", "LA PAJA ERA AMARILLA"], "EL LOBO SOPLA DOS CASAS", "ES LO IMPORTANTE.", n="analizar")],
"4": [ORD("ORDENÁ EL CUENTO CON SUS PALABRAS.", ["AL FINAL, SE SALVAN", "PRIMERO, HACEN SUS CASAS", "LUEGO, VIENE EL LOBO"], ["PRIMERO, HACEN SUS CASAS", "LUEGO, VIENE EL LOBO", "AL FINAL, SE SALVAN"], "PRIMERO, LUEGO, AL FINAL.", n="aplicar"),
      SA("COMPLETÁ: ___ , VIENE EL LOBO.", low("LUEGO") + low("DESPUÉS") + low("despues"), "LUEGO, VIENE EL LOBO.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿QUÉ VA PRIMERO?", ["HACEN SUS CASAS", "SE SALVAN"], "HACEN SUS CASAS", "ES EL PRINCIPIO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿QUÉ PALABRA VA AL ÚLTIMO?", ["AL FINAL", "PRIMERO"], "AL FINAL", "LO ÚLTIMO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁNTAS ORACIONES TIENE EL RESUMEN?", ["3", "10"], "3", "PRINCIPIO, MEDIO Y FINAL.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ CASA NO SE CAE?", ["LA DE LADRILLOS", "LA DE PAJA"], "LA DE LADRILLOS", "ES LA MÁS FUERTE.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, ORD("ORDENÁ LAS ESCENAS.", [ESC[3], ESC[1], ESC[0]], [ESC[0], ESC[1], ESC[3]], "PRINCIPIO, MEDIO Y FINAL.", n="analizar")],
 [1, MC("¿QUÉ CASA SOPLA PRIMERO EL LOBO?", ["LA DE PAJA", "LA DE LADRILLOS", "LA DE MADERA"], "LA DE PAJA", "LA PRIMERA QUE SOPLA.", n="recordar")],
 [1, TF("TOMI DICE QUE EL CUENTO EMPIEZA CUANDO SE SALVAN.", "FALSO", "ESO ES EL FINAL.", n="error")],
 [2, MC("___ , EL LOBO SOPLA. ¿QUÉ PALABRA VA EN EL MEDIO DEL CUENTO?", ["LUEGO", "PRIMERO", "AL FINAL"], "LUEGO", "LO QUE SIGUE.", n="aplicar")],
 [2, SA("COMPLETÁ: ___ , SE SALVAN.", low("AL FINAL") + low("POR ÚLTIMO") + low("por ultimo"), "ES LO ÚLTIMO.", n="aplicar")],
 [2, TF("PRIMERO Y AL FINAL SON PALABRAS QUE ORDENAN.", "VERDADERO", "DICEN EL ORDEN.", n="recordar")],
 [3, MC("¿QUÉ ES RESUMIR?", ["CONTAR LO IMPORTANTE", "CONTAR TODO JUNTO", "DIBUJAR EL CUENTO"], "CONTAR LO IMPORTANTE", "SOLO LO IMPORTANTE.", n="recordar")],
 [3, MC("¿QUÉ NO VA EN EL RESUMEN?", ["EL LOBO TENÍA BIGOTES", "EL LOBO SOPLA DOS CASAS", "SE SALVAN"], "EL LOBO TENÍA BIGOTES", "NO ES IMPORTANTE.", n="analizar")],
 [3, UNI("UNÍ CADA PARTE CON SU ORACIÓN.", [("PRINCIPIO", "HACEN CASAS"), ("MEDIO", "EL LOBO SOPLA"), ("FINAL", "SE SALVAN")], "TRES PARTES.", n="analizar")],
 [4, ORD("ORDENÁ CENICIENTA.", ["AL FINAL, LA ENCUENTRA EL PRÍNCIPE", "PRIMERO, LIMPIA LA CASA", "LUEGO, VA AL BAILE"], ["PRIMERO, LIMPIA LA CASA", "LUEGO, VA AL BAILE", "AL FINAL, LA ENCUENTRA EL PRÍNCIPE"], "CON PALABRAS QUE ORDENAN.", n="aplicar")],
 [4, TF("PRIMERO, SE SALVAN ESTÁ BIEN PARA EMPEZAR.", "FALSO", "SALVARSE ES EL FINAL.", n="error")],
 [4, MC("ANTES DE TERMINAR DE CONTAR, ¿QUÉ HACÉS?", ["REVISO EL ORDEN", "BORRO TODO", "NADA"], "REVISO EL ORDEN", "PARA QUE SE ENTIENDA.", n="aplicar")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: qué pasó primero y qué pasó después", "examen_titulo": "Nivel jefe: qué pasó primero y qué pasó después",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
