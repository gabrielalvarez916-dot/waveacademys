# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 10 · Museo de ciencias (proyecto final). Genera mision-10.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (hoy arma el museo del grado).
Niveles: 1 elijo un tema · 2 armo mi puesto · 3 explico con dibujos y datos · 4 visitamos el museo."""
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
"objetivo": "Vas a elegir un tema para el museo.",
"vas_a_ver": ["Qué es un museo", "Los temas del año", "Elegir uno"],
"secciones": [
 S(1, "El museo del grado", [
  D("Museo", "Un lugar donde se <b>muestran</b> cosas para aprender."),
  P("Tomi y sus compañeros arman un <b>museo de ciencias</b> en el aula."),
  IMG("Nuestro museo", "Cada uno muestra un tema.", FG.nombres(["MUSEO", "PUESTOS", "VISITAS"], cols=3)),
 ]),
 S(1, "Los temas del año", [
  P("Este año aprendimos muchas cosas. ¡Elegí la que más te gustó!"),
  IMG("Temas para elegir", "Todos los vimos este año.", FG.tiras(["CÓMO CRECEMOS", "LAS CRÍAS", "DE LA FLOR AL FRUTO", "EL CICLO DEL AGUA", "LOS IMANES", "EL SUELO"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué tema es?", "Pensá en cada pista.", FG.tiras(["1. LLUEVE, SUBE EL VAPOR, SE FORMAN NUBES", "2. ATRAEN CLIPS Y CLAVOS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El tema de Tomi", "planteo": "¿Qué tema elige Tomi?", "pasos": ["Piensa qué le gustó más.", "Le encantaron los imanes.", "¡Elige los imanes!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Un museo es un lugar para…", "pasos": ["…___ y aprender."]},
"ejemplo_solo": {"titulo": "Tu tema", "planteo": "¿Qué tema del año te gustó más? Escribilo."},
"tip": {"titulo": "Elegí con ganas", "texto": "Elegí el tema que más te guste explicar."},
"ojo": ["Cada uno elige un tema.", "Podés mirar tu carpeta para recordar."],
"resumen": [{"titulo": "Museo", "texto": "Mostrar para aprender."}, {"titulo": "Temas", "texto": "Lo que vimos este año."}, {"titulo": "Elegir", "texto": "El que más te gusta."}],
"glosario": [{"palabra": "Museo", "significado": "Lugar para mostrar y aprender."}, {"palabra": "Tema", "significado": "De qué se trata algo."}],
"carpeta": ["¿Qué tema es la pista 1?", "¿Qué tema es la pista 2?", "Tomi dice que en un museo no se aprende nada. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("EL CICLO DEL AGUA") + low("CICLO DEL AGUA") + low("EL AGUA"), low("LOS IMANES") + low("IMANES") + low("EL IMÁN") + low("IMÁN"), NO],
"soluciones": {"incompleto": "MOSTRAR.", "solo": "Tu tema favorito.", "carpeta": ["El ciclo del agua.", "Los imanes.", "No: es para aprender."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a armar tu puesto del museo.",
"vas_a_ver": ["El cartel", "Los objetos", "El experimento"],
"secciones": [
 S(1, "Las partes del puesto", [
  P("Un buen puesto tiene <b>título</b>, <b>dibujo</b>, <b>objetos</b> y algo para <b>probar</b>."),
  IMG("El puesto de Tomi", "Tema: los imanes.", FG.tiras(["TÍTULO: LOS IMANES", "DIBUJO: UN IMÁN CON CLIPS", "OBJETOS: CLIPS Y CLAVOS", "PARA PROBAR: ¿QUÉ ATRAE?"], numeros=False)),
 ]),
 S(1, "El cartel", [
  P("El <b>título</b> va arriba, grande y claro."),
  P("Abajo, un <b>dibujo</b> y pocas palabras."),
  IMG("Un buen cartel", "Se lee de lejos.", FG.nombres(["TÍTULO GRANDE", "DIBUJO", "POCAS PALABRAS"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Qué parte es?", "Pensá en el puesto.", FG.tiras(["1. VA ARRIBA, GRANDE Y CLARO", "2. LOS VISITANTES LO PUEDEN TOCAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi puesto", "planteo": "¿Qué necesita el puesto del agua?", "pasos": ["Título: el ciclo del agua.", "Un dibujo con flechas.", "Un frasco para mirar."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El título va…", "pasos": ["…___ y grande."]},
"ejemplo_solo": {"titulo": "Tu cartel", "planteo": "Dibujá el cartel de tu puesto en la carpeta."},
"tip": {"titulo": "De lejos", "texto": "Si se lee de lejos, el cartel está bien."},
"ojo": ["Usá letra grande y clara.", "Pocas palabras se leen mejor."],
"resumen": [{"titulo": "Título", "texto": "Arriba y grande."}, {"titulo": "Dibujo", "texto": "Muestra el tema."}, {"titulo": "Para probar", "texto": "Algo para tocar."}],
"glosario": [{"palabra": "Puesto", "significado": "Lugar donde mostrás tu tema."}, {"palabra": "Cartel", "significado": "Hoja grande con título y dibujo."}],
"carpeta": ["¿Qué parte del puesto es la tarjeta 1?", "¿Qué parte es la tarjeta 2?", "Tomi dice que el cartel tiene que tener muchas palabras. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("TÍTULO") + low("titulo") + low("EL TÍTULO") + low("el titulo"), low("OBJETOS") + low("LOS OBJETOS") + low("PARA PROBAR") + low("EL EXPERIMENTO") + low("EXPERIMENTO"), NO],
"soluciones": {"incompleto": "ARRIBA.", "solo": "Tu cartel.", "carpeta": ["El título.", "Los objetos para probar.", "No: pocas palabras se leen mejor."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a explicar tu tema.",
"vas_a_ver": ["Explicar con dibujos", "Dar datos", "Hablar claro"],
"secciones": [
 S(1, "Explicar", [
  P("Cuando llega un visitante, Tomi <b>señala el dibujo</b> y explica."),
  P("Dice un <b>dato</b>: «El imán atrae clips sin tocarlos»."),
  IMG("Para explicar bien", "Tres pasos.", FG.tiras(["1. SALUDO", "2. SEÑALO EL DIBUJO", "3. DIGO UN DATO"], numeros=False, cols=1)),
 ]),
 S(1, "Hablar claro", [
  P("Hablá <b>despacio</b> y fuerte, mirando a quien escucha."),
  IMG("Un buen explicador", "Así se explica.", FG.nombres(["DESPACIO", "FUERTE", "MIRANDO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Qué va primero?", FG.tiras(["DIGO UN DATO", "SALUDO", "SEÑALO EL DIBUJO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi explica", "planteo": "¿Qué dice Tomi?", "pasos": ["«¡Hola! Bienvenidos.»", "«Miren este dibujo.»", "«El imán atrae clips.»"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para explicar, hablo…", "pasos": ["…___ y fuerte."]},
"ejemplo_solo": {"titulo": "Tu dato", "planteo": "Escribí un dato de tu tema para contar."},
"tip": {"titulo": "Practicá", "texto": "Ensayá en tu casa antes del museo."},
"ojo": ["Un dato tiene que ser verdadero.", "Si no sabés algo, decí «no sé»."],
"resumen": [{"titulo": "Saludo", "texto": "Doy la bienvenida."}, {"titulo": "Dibujo", "texto": "Lo señalo."}, {"titulo": "Dato", "texto": "Algo verdadero."}],
"glosario": [{"palabra": "Dato", "significado": "Algo verdadero que sabemos."}, {"palabra": "Visitante", "significado": "Quien viene a mirar."}],
"carpeta": ["De las tarjetas, ¿qué va primero?", "¿Qué va al final?", "Tomi dice que hay que hablar rapidísimo. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("SALUDO") + low("EL SALUDO") + low("SALUDAR"), low("DIGO UN DATO") + low("UN DATO") + low("EL DATO"), NO],
"soluciones": {"incompleto": "DESPACIO.", "solo": "Tu dato.", "carpeta": ["Saludo.", "Digo un dato.", "No: despacio y claro."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a visitar el museo.",
"vas_a_ver": ["Mirar con respeto", "Hacer preguntas", "Felicitar"],
"secciones": [
 S(1, "De visita", [
  P("Ahora Tomi es <b>visitante</b>: recorre los puestos de sus compañeros."),
  P("Mira, <b>escucha</b> y espera su <b>turno</b> para hablar."),
  IMG("Buen visitante", "Así visitamos.", FG.tiras(["MIRO CON CUIDADO", "ESCUCHO", "ESPERO MI TURNO"], numeros=False, cols=1)),
 ]),
 S(1, "Preguntar y felicitar", [
  P("Hace una <b>pregunta</b>: «¿Cómo lo descubriste?»."),
  P("Al irse, <b>felicita</b>: «¡Qué buen puesto!»."),
  IMG("Palabras amables", "Para cada puesto.", FG.nombres(["GRACIAS", "¡QUÉ LINDO!", "¿CÓMO LO HICISTE?"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Está bien?", "Pensá en cada una.", FG.tiras(["1. TOCAR TODO SIN PREGUNTAR", "2. ESPERAR MI TURNO PARA HABLAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La visita", "planteo": "¿Qué hace un buen visitante?", "pasos": ["Mira con cuidado.", "Hace una pregunta.", "Felicita al irse."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para hablar, espero mi…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu pregunta", "planteo": "Escribí una pregunta para hacer en el museo."},
"tip": {"titulo": "Felicitá", "texto": "Decir algo lindo alegra a tus compañeros."},
"ojo": ["Preguntá antes de tocar.", "Hablá bajito en el museo."],
"resumen": [{"titulo": "Miro", "texto": "Con cuidado."}, {"titulo": "Pregunto", "texto": "Para aprender."}, {"titulo": "Felicito", "texto": "Al irme."}],
"glosario": [{"palabra": "Turno", "significado": "El momento de cada uno."}, {"palabra": "Felicitar", "significado": "Decir algo lindo por lo que hizo otro."}],
"carpeta": ["¿La tarjeta 1 está bien o mal?", "¿La tarjeta 2 está bien o mal?", "Tomi dice que en el museo se grita. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MAL") + low("ESTÁ MAL") + low("esta mal"), low("BIEN") + low("ESTÁ BIEN") + low("esta bien"), NO],
"soluciones": {"incompleto": "TURNO.", "solo": "Tu pregunta.", "carpeta": ["Mal.", "Bien.", "No: se habla bajito."]},
}

ACT = {
"1": [MC("¿PARA QUÉ SIRVE UN MUSEO?", ["PARA APRENDER", "PARA DORMIR"], "PARA APRENDER", "MOSTRAMOS LO QUE SABEMOS.", n="recordar"),
      UNI("UNÍ CADA PISTA CON SU TEMA.", [("ATRAE CLIPS", "IMANES"), ("SUBE EL VAPOR", "CICLO DEL AGUA"), ("LOMBRICES", "EL SUELO")], "PENSÁ EN LO QUE VIMOS.", n="analizar")],
"2": [ORD("ORDENÁ EL CARTEL, DE ARRIBA ABAJO.", ["DIBUJO", "TÍTULO", "POCAS PALABRAS"], ["TÍTULO", "DIBUJO", "POCAS PALABRAS"], "EL TÍTULO VA ARRIBA.", n="analizar"),
      TF("EL CARTEL TIENE QUE TENER MUCHAS PALABRAS.", "FALSO", "POCAS SE LEEN MEJOR.", n="error")],
"3": [ORD("ORDENÁ: CÓMO EXPLICO.", ["DIGO UN DATO", "SALUDO", "SEÑALO EL DIBUJO"], ["SALUDO", "SEÑALO EL DIBUJO", "DIGO UN DATO"], "PRIMERO SALUDO.", n="analizar"),
      MC("¿CÓMO HABLO PARA EXPLICAR?", ["DESPACIO Y FUERTE", "RAPIDÍSIMO"], "DESPACIO Y FUERTE", "ASÍ ME ENTIENDEN.", n="aplicar")],
"4": [MC("¿QUÉ HACE UN BUEN VISITANTE?", ["ESPERA SU TURNO", "GRITA"], "ESPERA SU TURNO", "Y ESCUCHA.", n="aplicar"),
      TF("ANTES DE TOCAR, HAY QUE PREGUNTAR.", "VERDADERO", "ES DE BUEN VISITANTE.", n="recordar")],
"5": [MC("RELÁMPAGO. EL TÍTULO VA…", ["ARRIBA", "ABAJO"], "ARRIBA", "GRANDE Y CLARO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. PRIMERO…", ["SALUDO", "ME VOY"], "SALUDO", "DOY LA BIENVENIDA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. UN DATO ES…", ["VERDADERO", "INVENTADO"], "VERDADERO", "ALGO QUE SABEMOS.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. AL IRME…", ["FELICITO", "ME QUEJO"], "FELICITO", "¡QUÉ BUEN PUESTO!", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UN MUSEO?", ["UN LUGAR PARA APRENDER", "UN LUGAR PARA DORMIR"], "UN LUGAR PARA APRENDER", "COMO EL DEL GRADO.", n="recordar")],
 [1, SA("¿QUÉ TEMA ELIGIÓ TOMI?", low("IMANES") + low("LOS IMANES") + low("EL IMÁN") + low("IMÁN"), "LOS IMANES.", n="recordar")],
 [1, TF("CADA UNO ELIGE UN TEMA DEL AÑO.", "VERDADERO", "EL QUE MÁS LE GUSTA.", n="recordar")],
 [2, UNI("UNÍ CADA PARTE DEL PUESTO.", [("TÍTULO", "ARRIBA Y GRANDE"), ("OBJETOS", "PARA PROBAR")], "PENSÁ EN EL CARTEL.", n="analizar")],
 [2, SA("¿DÓNDE VA EL TÍTULO DEL CARTEL?", low("ARRIBA") + low("EN LA PARTE DE ARRIBA"), "ARRIBA.", n="aplicar")],
 [2, MC("¿CÓMO TIENE QUE SER LA LETRA DEL CARTEL?", ["GRANDE Y CLARA", "CHIQUITA"], "GRANDE Y CLARA", "SE LEE DE LEJOS.", n="aplicar")],
 [3, MC("¿QUÉ ES UN DATO?", ["ALGO VERDADERO", "ALGO INVENTADO"], "ALGO VERDADERO", "COMO: EL IMÁN ATRAE CLIPS.", n="recordar")],
 [3, SA("SI NO SABÉS ALGO, ¿QUÉ DECÍS?", low("NO SÉ") + low("no se") + low("NO LO SÉ") + low("no lo se"), "«NO SÉ».", n="aplicar")],
 [3, TF("PARA EXPLICAR HAY QUE HABLAR RAPIDÍSIMO.", "FALSO", "DESPACIO Y CLARO.", n="error")],
 [4, MC("¿QUÉ SE DICE AL IRSE DE UN PUESTO?", ["¡QUÉ BUEN PUESTO!", "¡QUÉ ABURRIDO!"], "¡QUÉ BUEN PUESTO!", "FELICITAMOS.", n="aplicar")],
 [4, UNI("UNÍ: ¿ESTÁ BIEN O MAL?", [("ESPERAR MI TURNO", "BIEN"), ("GRITAR EN EL MUSEO", "MAL")], "PENSÁ EN LOS DEMÁS.", n="analizar")],
 [4, TF("EN EL MUSEO SE HABLA BAJITO.", "VERDADERO", "ASÍ TODOS ESCUCHAN.", n="recordar")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 10, "estilo": "primeros",
     "practica": "Práctica general: museo de ciencias", "examen_titulo": "Nivel jefe: museo de ciencias",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
