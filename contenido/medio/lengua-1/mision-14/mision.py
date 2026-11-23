# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 14 · Listas y carteles. Genera mision-14.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Metáfora: Sofi ayuda a ordenar el aula (lista de útiles, carteles, etiquetas y la agenda de la semana).
Niveles: 1 listas para la clase · 2 carteles para el aula · 3 etiquetas con nombres · 4 agenda de la semana."""
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
"objetivo": "Vas a leer y escribir listas.",
"vas_a_ver": ["Qué es una lista", "Una cosa por renglón", "Para qué sirve"],
"secciones": [
 S(1, "Una lista", [
  P("Sofi prepara la mochila con una <b>lista</b>."),
  D("Lista", "Palabras escritas <b>una abajo de la otra</b>."),
  IMG("La lista de Sofi", "Una cosa por renglón.", FG.lista(["LÁPIZ", "GOMA", "CUADERNO", "TIJERA"], titulo="MI MOCHILA")),
 ]),
 S(1, "Para qué sirve", [
  P("La lista sirve para <b>no olvidarnos</b> de nada."),
  P("Cuando guardamos algo, lo <b>marcamos</b>."),
  IMG("Lista marcada", "Lo que ya guardé.", FG.lista(["LÁPIZ", "GOMA", "CUADERNO", "TIJERA"], titulo="MI MOCHILA", marcar=(0, 1))),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("Lista del súper", "Para comprar.", FG.lista(["PAN", "LECHE", "QUESO"], titulo="PARA COMPRAR")),
 ]),
],
"ejemplo_completo": {"titulo": "Lista", "planteo": "¿Qué llevo a la plaza?", "pasos": ["PELOTA.", "AGUA.", "Una abajo de la otra."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Lista de la mochila.", "pasos": ["LÁPIZ.", "___ ."]},
"ejemplo_solo": {"titulo": "Tu lista", "planteo": "Escribí la lista de lo que llevás a la escuela."},
"tip": {"titulo": "Una por renglón", "texto": "Cada cosa va en su renglón."},
"ojo": ["En la lista no hace falta oración.", "Solo el nombre de cada cosa."],
"resumen": [{"titulo": "Lista", "texto": "Una abajo de la otra."}, {"titulo": "Sirve", "texto": "Para no olvidar."}, {"titulo": "Marcar", "texto": "Lo que ya está."}],
"glosario": [{"palabra": "Lista", "significado": "Palabras una abajo de la otra."}, {"palabra": "Útiles", "significado": "Cosas para la escuela."}],
"carpeta": ["En la lista para comprar, ¿qué va primero?", "¿Qué va último?", "Tomi escribió todo en un solo renglón. ¿Es una lista?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PAN"), low("QUESO"), NO],
"soluciones": {"incompleto": "Por ejemplo: GOMA.", "solo": "Tu lista de útiles.", "carpeta": ["PAN.", "QUESO.", "No: va una abajo de la otra."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a leer y hacer carteles para el aula.",
"vas_a_ver": ["Qué es un cartel", "Pocas palabras", "Letras grandes"],
"secciones": [
 S(1, "Carteles", [
  P("En la escuela hay muchos <b>carteles</b>."),
  D("Cartel", "Dice algo con <b>pocas palabras</b> y <b>letras grandes</b>."),
  IMG("Carteles de la escuela", "Se leen de lejos.", FG.nombres(["BAÑO", "BIBLIOTECA", "SALIDA"], cols=3)),
 ]),
 S(1, "Carteles que avisan", [
  P("Algunos carteles <b>avisan</b> qué hacer."),
  IMG("Avisos", "Cortos y claros.", FG.nombres(["NO CORRER", "SILENCIO", "LAVATE LAS MANOS"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los carteles. Los vas a usar en la carpeta."),
  IMG("¿Dónde va?", "Pensá en cada lugar.", FG.nombres(["COMEDOR", "PATIO", "DIRECCIÓN"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Cartel", "planteo": "La puerta del baño.", "pasos": ["¿Qué hay adentro? El baño.", "Pocas palabras.", "Cartel: BAÑO."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cartel para la biblioteca.", "pasos": ["Dice: ___ ."]},
"ejemplo_solo": {"titulo": "Tu cartel", "planteo": "Hacé un cartel para la puerta de tu cuarto."},
"tip": {"titulo": "Corto y grande", "texto": "Así se lee de lejos."},
"ojo": ["Un cartel no cuenta una historia.", "Dice lo justo."],
"resumen": [{"titulo": "Cartel", "texto": "Pocas palabras."}, {"titulo": "Letras", "texto": "Grandes."}, {"titulo": "Avisa", "texto": "Qué hay o qué hacer."}],
"glosario": [{"palabra": "Cartel", "significado": "Letrero con pocas palabras."}, {"palabra": "Aviso", "significado": "Algo que nos dice qué hacer."}],
"carpeta": ["¿Qué cartel va donde comemos?", "¿Qué cartel va donde jugamos en el recreo?", "Tomi hizo un cartel con un cuento largo. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("COMEDOR"), low("PATIO"), NO],
"soluciones": {"incompleto": "BIBLIOTECA.", "solo": "Tu cartel.", "carpeta": ["COMEDOR.", "PATIO.", "No: el cartel lleva pocas palabras."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir etiquetas con nombres.",
"vas_a_ver": ["Qué es una etiqueta", "Dónde van", "Escribir tu nombre"],
"secciones": [
 S(1, "Etiquetas", [
  D("Etiqueta", "Un papelito que dice <b>de quién es</b> o <b>qué hay adentro</b>."),
  P("Sofi pone etiquetas en las cajas del aula."),
  IMG("Las cajas del aula", "Cada caja con su etiqueta.", FG.nombres(["LÁPICES", "TIJERAS", "PLASTILINA"], cols=3)),
 ]),
 S(1, "Con tu nombre", [
  P("En la mochila y en el cuaderno va <b>tu nombre</b>."),
  IMG("La etiqueta de Sofi", "Su nombre en el cuaderno.", FG.letras("SOFI")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los dibujos. Los vas a usar en la carpeta."),
  IMG("¿Qué etiqueta va?", "Pensá qué hay adentro.", FG.dibujo_palabra([("pelota", "?"), ("caramelo", "?"), ("globo", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Etiqueta", "planteo": "Una caja con pelotas.", "pasos": ["¿Qué hay adentro?", "Pelotas.", "Etiqueta: PELOTAS."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Mi cuaderno.", "pasos": ["La etiqueta dice: ___ ."]},
"ejemplo_solo": {"titulo": "Tus etiquetas", "planteo": "Escribí tu nombre en tus útiles."},
"tip": {"titulo": "Clara y corta", "texto": "Una o dos palabras alcanzan."},
"ojo": ["Tu nombre empieza con mayúscula.", "Escribí con letra clara."],
"resumen": [{"titulo": "Etiqueta", "texto": "Dice qué es o de quién."}, {"titulo": "Corta", "texto": "Una o dos palabras."}, {"titulo": "Nombre", "texto": "En tus cosas."}],
"glosario": [{"palabra": "Etiqueta", "significado": "Papelito que dice qué es."}, {"palabra": "Plastilina", "significado": "Masa de colores para modelar."}],
"carpeta": ["¿Qué etiqueta va en la caja de la pelota?", "¿Qué etiqueta va en la caja de los globos?", "Tomi puso la etiqueta LÁPICES en la caja de tijeras. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PELOTA") + low("PELOTAS"), low("GLOBOS") + low("GLOBO"), NO],
"soluciones": {"incompleto": "Tu nombre.", "solo": "Tus útiles con tu nombre.", "carpeta": ["PELOTAS.", "GLOBOS.", "No: tiene que decir TIJERAS."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a leer la agenda de la semana.",
"vas_a_ver": ["Los días de la semana", "Qué hacemos cada día", "Leer la agenda"],
"secciones": [
 S(1, "La semana", [
  P("La semana de la escuela tiene <b>cinco días</b>."),
  IMG("Los días de la escuela", "De lunes a viernes.", FG.nombres(["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES"], cols=3)),
 ]),
 S(1, "La agenda", [
  D("Agenda", "Dice <b>qué hacemos</b> cada día."),
  IMG("La agenda del grado", "Un día por renglón.", FG.tiras(["LUNES: MÚSICA", "MARTES: EDUCACIÓN FÍSICA", "MIÉRCOLES: BIBLIOTECA", "JUEVES: PLÁSTICA", "VIERNES: JUEGOS"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la agenda. La vas a usar en la carpeta."),
  IMG("La agenda", "Buscá cada día.", FG.tiras(["LUNES: MÚSICA", "MIÉRCOLES: BIBLIOTECA", "VIERNES: JUEGOS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Leer la agenda", "planteo": "¿Qué hacemos el martes?", "pasos": ["Busco MARTES.", "Leo lo que dice.", "EDUCACIÓN FÍSICA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Después del lunes viene…", "pasos": ["El ___ ."]},
"ejemplo_solo": {"titulo": "Tu agenda", "planteo": "Escribí qué hacés vos cada día de la semana."},
"tip": {"titulo": "Buscá el día", "texto": "Primero buscá el día y después leé al lado."},
"ojo": ["Los días van en orden.", "El sábado y el domingo no hay escuela."],
"resumen": [{"titulo": "Semana", "texto": "Cinco días de escuela."}, {"titulo": "Agenda", "texto": "Qué hacemos cada día."}, {"titulo": "Leer", "texto": "Buscar el día."}],
"glosario": [{"palabra": "Agenda", "significado": "Lo que hacemos cada día."}, {"palabra": "Semana", "significado": "Siete días seguidos."}],
"carpeta": ["En la agenda, ¿qué hacemos el miércoles?", "¿Qué día hay juegos?", "Tomi dice que después del martes viene el viernes. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("BIBLIOTECA"), low("VIERNES") + low("EL VIERNES"), NO],
"soluciones": {"incompleto": "MARTES.", "solo": "Tu agenda.", "carpeta": ["BIBLIOTECA.", "El viernes.", "No: viene el miércoles."]},
}

ACT = {
"1": [MC("¿QUÉ ES UNA LISTA?", ["PALABRAS UNA ABAJO DE LA OTRA", "UN CUENTO LARGO"], "PALABRAS UNA ABAJO DE LA OTRA", "UNA POR RENGLÓN.", n="recordar"),
      SA("LISTA PARA COMPRAR: PAN, LECHE, QUESO. ¿QUÉ VA PRIMERO?", low("PAN"), "PAN.", n="aplicar")],
"2": [MC("¿CUÁL ES UN CARTEL?", ["BAÑO", "HABÍA UNA VEZ UN REY QUE VIVÍA LEJOS"], "BAÑO", "POCAS PALABRAS.", n="analizar"),
      TF("LOS CARTELES TIENEN LETRAS GRANDES.", "VERDADERO", "ASÍ SE LEEN DE LEJOS.", n="recordar")],
"3": [UNI("UNÍ CADA CAJA CON SU ETIQUETA.", [("✏️", "LÁPICES"), ("✂️", "TIJERAS"), ("⚽", "PELOTAS")], "LA ETIQUETA DICE QUÉ HAY.", n="analizar"),
      SA("¿QUÉ VA EN LA ETIQUETA DE TU CUADERNO?", ["MI NOMBRE", "mi nombre", "Mi nombre", "EL NOMBRE", "el nombre", "NOMBRE", "nombre", "Nombre"], "TU NOMBRE.", n="aplicar")],
"4": [ORD("ORDENÁ LOS DÍAS.", ["MIÉRCOLES", "LUNES", "MARTES"], ["LUNES", "MARTES", "MIÉRCOLES"], "LUNES, MARTES, MIÉRCOLES.", n="analizar"),
      MC("LUNES: MÚSICA. ¿QUÉ HACEMOS EL LUNES?", ["MÚSICA", "JUEGOS", "BIBLIOTECA"], "MÚSICA", "LO DICE LA AGENDA.", n="aplicar")],
"5": [MC("RELÁMPAGO. EN UNA LISTA, CADA COSA VA…", ["EN SU RENGLÓN", "TODO JUNTO"], "EN SU RENGLÓN", "UNA ABAJO DE LA OTRA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. UN CARTEL TIENE…", ["POCAS PALABRAS", "MUCHAS PÁGINAS"], "POCAS PALABRAS", "CORTO Y CLARO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. DESPUÉS DEL JUEVES VIENE…", ["VIERNES", "LUNES"], "VIERNES", "JUEVES, VIERNES.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA ETIQUETA DE TU MOCHILA DICE…", ["TU NOMBRE", "UN CUENTO"], "TU NOMBRE", "DE QUIÉN ES.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿PARA QUÉ SIRVE UNA LISTA?", ["PARA NO OLVIDARNOS", "PARA DORMIR"], "PARA NO OLVIDARNOS", "ANOTAMOS LO QUE HACE FALTA.", n="recordar")],
 [1, SA("LISTA: LÁPIZ, GOMA, CUADERNO. ¿QUÉ VA ÚLTIMO?", low("CUADERNO"), "CUADERNO.", n="aplicar")],
 [1, TF("UNA LISTA SE ESCRIBE EN UN SOLO RENGLÓN.", "FALSO", "UNA ABAJO DE LA OTRA.", n="error")],
 [2, MC("¿QUÉ CARTEL VA EN LA PUERTA DEL BAÑO?", ["BAÑO", "PATIO", "COMEDOR"], "BAÑO", "DICE QUÉ HAY ADENTRO.", n="aplicar")],
 [2, UNI("UNÍ CADA LUGAR CON SU CARTEL.", [("🍽️", "COMEDOR"), ("📚", "BIBLIOTECA"), ("🛝", "PATIO")], "EL CARTEL DICE EL LUGAR.", n="analizar")],
 [2, TF("UN CARTEL CUENTA UNA HISTORIA LARGA.", "FALSO", "LLEVA POCAS PALABRAS.", n="error")],
 [3, MC("¿QUÉ DICE UNA ETIQUETA?", ["QUÉ HAY O DE QUIÉN ES", "UN CHISTE"], "QUÉ HAY O DE QUIÉN ES", "ES CORTA Y CLARA.", n="recordar")],
 [3, SA("UNA CAJA TIENE GLOBOS. ¿QUÉ DICE LA ETIQUETA?", low("GLOBOS") + low("GLOBO"), "GLOBOS.", n="aplicar")],
 [3, TF("LA CAJA DE TIJERAS LLEVA LA ETIQUETA LÁPICES.", "FALSO", "LLEVA TIJERAS.", n="error")],
 [4, ORD("ORDENÁ LOS DÍAS.", ["VIERNES", "JUEVES", "MIÉRCOLES"], ["MIÉRCOLES", "JUEVES", "VIERNES"], "MIÉRCOLES, JUEVES, VIERNES.", n="analizar")],
 [4, SA("AGENDA: VIERNES: JUEGOS. ¿QUÉ HACEMOS EL VIERNES?", low("JUEGOS") + low("JUGAMOS") + low("JUGAR"), "JUEGOS.", n="aplicar")],
 [4, MC("¿CUÁNTOS DÍAS DE ESCUELA HAY EN LA SEMANA?", ["CINCO", "DOS", "DIEZ"], "CINCO", "DE LUNES A VIERNES.", n="recordar")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 14, "estilo": "primeros",
     "practica": "Práctica general: listas y carteles", "examen_titulo": "Nivel jefe: listas y carteles",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-14.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
