# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 1 · Mi nombre y los nombres del grado. Genera mision-1.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el primer día de Sofi en primer grado (los carteles con los nombres).
Niveles: 1 leer los nombres del grado · 2 copiar mi nombre sin mirar · 3 nombres que empiezan igual · 4 la lista de la clase."""
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
GRADO = ["ANA", "BRUNO", "LUCÍA", "MATEO", "SOFI", "TOMI"]

N1 = {**ESTILO,
"objetivo": "Vas a leer los nombres de tus compañeros.",
"vas_a_ver": ["Los carteles del grado", "Nombres largos y cortos", "Encontrar tu nombre"],
"secciones": [
 S(1, "Los carteles", [
  P("Es el primer día de clase. Cada chico tiene su <b>cartel</b> con su nombre."),
  IMG("Los nombres del grado", "Cada nombre en su cartel.", FG.nombres(["SOFI", "TOMI", "ANA", "MATEO", "LUCÍA", "BRUNO"])),
 ]),
 S(1, "Largos y cortos", [
  D("Nombre", "La palabra que dice <b>quién sos</b>. Se escribe con letras."),
  P("ANA tiene <b>3</b> letras. MARTINA tiene <b>7</b>. ¡Es más largo!"),
  IMG("Contamos letras", "ANA: 3 letras.", FG.letras("ANA", numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el nombre. Lo vas a usar en la carpeta."),
  IMG("Un nombre", "Contá sus letras.", FG.letras("TOMI", numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "SOFI", "planteo": "¿Cuántas letras tiene SOFI?", "pasos": ["S, O, F, I.", "Contamos: 1, 2, 3, 4.", "SOFI tiene 4 letras."]},
"ejemplo_incompleto": {"titulo": "BRUNO", "planteo": "Completá.", "pasos": ["B, R, U, N, O.", "BRUNO tiene ___ letras."]},
"ejemplo_solo": {"titulo": "Tu nombre", "planteo": "Escribí tu nombre. ¿Cuántas letras tiene?"},
"tip": {"titulo": "Mirá la primera", "texto": "La primera letra te ayuda a encontrar un nombre."},
"ojo": ["Los nombres empiezan con mayúscula.", "Cada nombre tiene sus letras en orden."],
"resumen": [{"titulo": "Cartel", "texto": "Dice un nombre."}, {"titulo": "Letras", "texto": "Forman el nombre."}, {"titulo": "Largo", "texto": "Más letras."}],
"glosario": [{"palabra": "Nombre", "significado": "Dice quién sos."}, {"palabra": "Letra", "significado": "Forma las palabras."}],
"carpeta": ["¿Qué nombre dice el cartel?", "¿Cuántas letras tiene?", "¿Con qué letra empieza?"],
"respuestas_carpeta": [["TOMI", "tomi", "Tomi"], ["4"], ["T", "t"]],
"soluciones": {"incompleto": "5.", "solo": "Depende de tu nombre.", "carpeta": ["TOMI.", "4.", "T."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a escribir tu nombre sin mirar el cartel.",
"vas_a_ver": ["Mirar el cartel", "Recordar las letras en orden", "Escribir sin mirar"],
"secciones": [
 S(1, "Mirar y recordar", [
  P("Tomi mira su cartel: <b>T, O, M, I</b>. Lo dice en voz alta."),
  IMG("El cartel de Tomi", "Cada letra en su lugar.", FG.letras("TOMI", numeros=True)),
 ]),
 S(1, "Escribir sin mirar", [
  D("El orden", "Las letras van siempre en el <b>mismo orden</b>."),
  P("Tomi tapa el cartel y escribe. ¡Después lo compara!"),
  IMG("¿Qué letra falta?", "MATEO: falta la T.", FG.letras("MATEO", ocultar=(2,), numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el nombre. Lo vas a usar en la carpeta."),
  IMG("Faltan letras", "Completá SOFI.", FG.letras("SOFI", ocultar=(1, 3), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "ANA", "planteo": "Ana escribe su nombre sin mirar.", "pasos": ["Dice: A, N, A.", "Escribe ANA.", "Compara con el cartel: ¡está bien!"]},
"ejemplo_incompleto": {"titulo": "BRUNO", "planteo": "Completá las letras.", "pasos": ["B, R, ___ , N, O."]},
"ejemplo_solo": {"titulo": "Tu nombre", "planteo": "Mirá tu nombre, tapalo y escribilo sin mirar."},
"tip": {"titulo": "Decilo en voz alta", "texto": "Decí cada letra mientras la escribís."},
"ojo": ["No cambies el orden de las letras.", "Compará siempre con el cartel."],
"resumen": [{"titulo": "Mirar", "texto": "El cartel."}, {"titulo": "Recordar", "texto": "Las letras en orden."}, {"titulo": "Comparar", "texto": "Con el cartel."}],
"glosario": [{"palabra": "Copiar", "significado": "Escribir lo que ves."}, {"palabra": "Comparar", "significado": "Ver si es igual."}],
"carpeta": ["¿Qué letra va en el lugar 2?", "¿Qué letra va en el lugar 4?", "¿Qué nombre se forma?"],
"respuestas_carpeta": [["O", "o"], ["I", "i"], ["SOFI", "sofi", "Sofi"]],
"soluciones": {"incompleto": "U.", "solo": "Tu nombre igual al cartel.", "carpeta": ["O.", "I.", "SOFI."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a encontrar nombres que empiezan con la misma letra.",
"vas_a_ver": ["La primera letra", "Nombres que empiezan igual", "Agrupar nombres"],
"secciones": [
 S(1, "La primera letra", [
  P("SOFI y SANTI empiezan con <b>S</b>. MATEO y MARTINA empiezan con <b>M</b>."),
  IMG("Empiezan igual", "La primera letra en rojo.", FG.nombres(["SOFI", "SANTI", "MATEO", "MARTINA"], True, 2)),
 ]),
 S(1, "Agrupar", [
  D("Empiezan igual", "Tienen la <b>misma primera letra</b>."),
  P("LUCÍA y LUCAS van juntos. ANA y ALMA, también."),
  IMG("Más grupos", "L con L, A con A.", FG.nombres(["LUCÍA", "LUCAS", "ANA", "ALMA"], True, 2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los carteles. Los vas a usar en la carpeta."),
  IMG("Carteles", "Mirá la primera letra.", FG.nombres(["TOMI", "BRUNO", "TERE", "BELÉN"], True, 2)),
 ]),
],
"ejemplo_completo": {"titulo": "Con P", "planteo": "PAULA y PEDRO.", "pasos": ["PAULA empieza con P.", "PEDRO empieza con P.", "¡Empiezan igual!"]},
"ejemplo_incompleto": {"titulo": "Con M", "planteo": "Completá.", "pasos": ["MATEO empieza con ___ .", "Otro nombre con M: ___ ."]},
"ejemplo_solo": {"titulo": "Tu letra", "planteo": "¿Con qué letra empieza tu nombre? Pensá otro nombre igual."},
"tip": {"titulo": "Mirá solo la primera", "texto": "Para agrupar, fijate solo en la primera letra."},
"ojo": ["SOFI y TOMI no empiezan igual.", "Mirá la primera letra, no la última."],
"resumen": [{"titulo": "Primera", "texto": "La letra de adelante."}, {"titulo": "Igual", "texto": "SOFI y SANTI."}, {"titulo": "Grupos", "texto": "Por la primera letra."}],
"glosario": [{"palabra": "Primera letra", "significado": "La de adelante."}, {"palabra": "Agrupar", "significado": "Juntar los que se parecen."}],
"carpeta": ["¿Con qué letra empieza TOMI?", "¿Qué nombre empieza igual que TOMI?", "¿Qué nombre empieza igual que BRUNO?"],
"respuestas_carpeta": [["T", "t"], ["TERE", "tere", "Tere"], ["BELÉN", "BELEN", "belén", "belen", "Belén"]],
"soluciones": {"incompleto": "M. Por ejemplo, MARTINA.", "solo": "Depende de tu nombre.", "carpeta": ["T.", "TERE.", "BELÉN."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a leer y usar la lista de la clase.",
"vas_a_ver": ["Qué es una lista", "Los nombres en orden", "Buscar un nombre"],
"secciones": [
 S(1, "La lista del grado", [
  P("La seño tiene una <b>lista</b> con todos los nombres. Uno abajo del otro."),
  IMG("La lista", "Seis nombres con su número.", FG.lista(GRADO)),
 ]),
 S(1, "En orden", [
  D("Lista", "Nombres escritos <b>uno abajo del otro</b>. Cada uno tiene su número."),
  P("Están ordenados por la primera letra: <b>A, B, L, M, S, T</b>."),
  IMG("¿Dónde está SOFI?", "SOFI es el número 5.", FG.lista(GRADO, marcar=(4,))),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("Buscá en la lista", "Un nombre marcado.", FG.lista(GRADO, marcar=(1,))),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar a TOMI", "planteo": "¿Qué número tiene TOMI?", "pasos": ["Busco la T.", "Está al final.", "TOMI es el número 6."]},
"ejemplo_incompleto": {"titulo": "Buscar a ANA", "planteo": "Completá.", "pasos": ["ANA empieza con ___ .", "Es el número ___ ."]},
"ejemplo_solo": {"titulo": "Tu lista", "planteo": "Escribí la lista de tu familia, un nombre abajo del otro."},
"tip": {"titulo": "Buscá la primera letra", "texto": "En la lista, buscá primero la letra del nombre."},
"ojo": ["En la lista, un nombre por renglón.", "El número dice el lugar."],
"resumen": [{"titulo": "Lista", "texto": "Uno abajo del otro."}, {"titulo": "Número", "texto": "El lugar."}, {"titulo": "Buscar", "texto": "Por la primera letra."}],
"glosario": [{"palabra": "Lista", "significado": "Nombres uno abajo del otro."}, {"palabra": "Renglón", "significado": "Una línea de la hoja."}],
"carpeta": ["¿Qué nombre está marcado?", "¿Qué número tiene?", "¿Qué nombre es el número 1?"],
"respuestas_carpeta": [["BRUNO", "bruno", "Bruno"], ["2"], ["ANA", "ana", "Ana"]],
"soluciones": {"incompleto": "A. 1.", "solo": "Por ejemplo: MAMÁ, PAPÁ, LUCAS.", "carpeta": ["BRUNO.", "2.", "ANA."]},
}

ACT = {
"1": [MC("¿QUÉ NOMBRE ES MÁS LARGO?", ["ANA", "MARTINA", "TOMI"], "MARTINA", "MARTINA TIENE 7 LETRAS."),
      MC("¿CUÁNTAS LETRAS TIENE SOFI?", ["3", "4", "5"], "4", "S, O, F, I.")],
"2": [ORD("ORDENÁ LAS LETRAS DE TOMI.", ["M", "T", "I", "O"], ["T", "O", "M", "I"], "T, O, M, I."),
      MC("¿QUÉ LETRA FALTA? MA_EO", ["T", "S", "R"], "T", "M, A, T, E, O.")],
"3": [MC("¿QUÉ NOMBRE EMPIEZA IGUAL QUE SOFI?", ["SANTI", "TOMI", "ANA"], "SANTI", "LOS DOS EMPIEZAN CON S."),
      SA("¿CON QUÉ LETRA EMPIEZA MATEO?", ["M", "m"], "MATEO EMPIEZA CON M.")],
"4": [MC("EN UNA LISTA, LOS NOMBRES VAN…", ["UNO ABAJO DEL OTRO", "TODOS JUNTOS", "AL REVÉS"], "UNO ABAJO DEL OTRO", "UN NOMBRE POR RENGLÓN."),
      ORD("ORDENÁ COMO EN LA LISTA: SOFI, ANA, MATEO.", ["SOFI", "ANA", "MATEO"], ["ANA", "MATEO", "SOFI"], "A, M, S.")],
"5": [MC("RELÁMPAGO. ¿CON QUÉ LETRA EMPIEZA ANA?", ["A", "N", "M"], "A", "ANA EMPIEZA CON A.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL EMPIEZA CON L?", ["LUCÍA", "BRUNO", "TOMI"], "LUCÍA", "L DE LUCÍA.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁNTAS LETRAS TIENE ANA?", ["2", "3", "4"], "3", "A, N, A.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ LETRA FALTA? TO_I", ["M", "S", "A"], "M", "T, O, M, I.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿QUÉ NOMBRE ES MÁS CORTO?", ["ANA", "MATEO", "MARTINA"], "ANA", "ANA TIENE 3 LETRAS.")],
 [1, MC("¿CUÁNTAS LETRAS TIENE BRUNO?", ["4", "5", "6"], "5", "B, R, U, N, O.")],
 [1, MC("LOS NOMBRES EMPIEZAN CON…", ["MAYÚSCULA", "UN NÚMERO", "UN PUNTO"], "MAYÚSCULA", "LA PRIMERA LETRA ES MAYÚSCULA.")],
 [2, ORD("ORDENÁ LAS LETRAS DE ANA.", ["N", "A", "A"], ["A", "N", "A"], "A, N, A.")],
 [2, MC("¿QUÉ LETRA FALTA? S_FI", ["O", "A", "U"], "O", "S, O, F, I.")],
 [2, MC("DESPUÉS DE ESCRIBIR SIN MIRAR, HAY QUE…", ["COMPARAR CON EL CARTEL", "BORRAR TODO", "NADA"], "COMPARAR CON EL CARTEL", "ASÍ VEMOS SI ESTÁ BIEN.")],
 [3, MC("¿QUÉ NOMBRE EMPIEZA IGUAL QUE MATEO?", ["MARTINA", "TOMI", "SOFI"], "MARTINA", "LOS DOS EMPIEZAN CON M.")],
 [3, SA("¿CON QUÉ LETRA EMPIEZA LUCÍA?", ["L", "l"], "LUCÍA EMPIEZA CON L.")],
 [3, MC("¿QUÉ NOMBRES EMPIEZAN IGUAL?", ["ANA Y ALMA", "ANA Y TOMI", "SOFI Y BRUNO"], "ANA Y ALMA", "LOS DOS EMPIEZAN CON A.")],
 [4, MC("EN LA LISTA, ¿QUÉ NOMBRE VA PRIMERO?", ["ANA", "TOMI", "SOFI"], "ANA", "LA A VA PRIMERO.")],
 [4, MC("¿PARA QUÉ SIRVE EL NÚMERO DE LA LISTA?", ["DICE EL LUGAR", "DICE LA EDAD", "PARA SUMAR"], "DICE EL LUGAR", "CADA NOMBRE TIENE SU LUGAR.")],
 [4, ORD("ORDENÁ COMO EN LA LISTA: TOMI, BRUNO, LUCÍA.", ["TOMI", "BRUNO", "LUCÍA"], ["BRUNO", "LUCÍA", "TOMI"], "B, L, T.")],
 [4, MC("¿CUÁNTOS NOMBRES VAN EN CADA RENGLÓN?", ["UNO", "DOS", "TODOS"], "UNO", "UNO ABAJO DEL OTRO.")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: mi nombre y los nombres del grado", "examen_titulo": "Nivel jefe: mi nombre y los nombres del grado",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
