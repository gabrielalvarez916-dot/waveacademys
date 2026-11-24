# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 8 · Distintas costumbres, mismos derechos. Genera mision-8.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy entrevista a familias de distintos lugares).
Niveles: 1 crianza, comidas y ropa · 2 historias y cuentos que se heredan · 3 prejuicios y discriminación · 4 carnaval y otras fiestas."""
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
"objetivo": "Vas a conocer costumbres de distintas culturas.",
"vas_a_ver": ["Cómo se cuida a los bebés", "Qué se come", "Cómo se visten"],
"secciones": [
 S(1, "Distintas culturas", [
  D("Cultura", "La forma de vivir de un grupo: sus comidas, su ropa, sus fiestas y su idioma."),
  P("En el barrio de Lola viven familias que vinieron de <b>distintos lugares</b>."),
  P("Cada familia tiene sus costumbres. ¡Y todas tienen los <b>mismos derechos</b>!"),
  IMG("Cómo llevan a los bebés", "Distintas formas de cuidar.", FG.tiras(["EN UN AGUAYO, A LA ESPALDA", "EN UN COCHECITO", "EN UNA MOCHILA DE TELA"], numeros=False, cols=1)),
 ]),
 S(1, "Comidas y ropa", [
  P("En una casa se comen <b>empanadas</b>. En otra, <b>arepas</b>. En otra, <b>tortillas</b> o arroz."),
  P("La ropa también cambia. Hay ponchos, vestidos bordados y pañuelos de colores."),
  P("Ninguna costumbre es mejor que otra: son <b>distintas</b>."),
  IMG("Comidas de muchos lugares", "Todas ricas.", FG.nombres(["EMPANADAS", "AREPAS", "TORTILLAS"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Qué es?", "Pensá en cada una.", FG.tiras(["1. TELA PARA LLEVAR AL BEBÉ A LA ESPALDA", "2. ABRIGO DE LANA CON UN AGUJERO PARA LA CABEZA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La familia de Yanina", "planteo": "¿Qué costumbres tiene?", "pasos": ["Lleva a su hermanito en aguayo.", "Comen sopa de maní.", "Usan ponchos de colores."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La forma de vivir de un grupo es su…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "¿Qué comida especial se hace en tu casa?"},
"tip": {"titulo": "Distinto no es peor", "texto": "Cada costumbre es valiosa."},
"ojo": ["Todas las culturas merecen respeto.", "Las familias pueden venir de lugares distintos."],
"resumen": [{"titulo": "Cultura", "texto": "Forma de vivir."}, {"titulo": "Costumbres", "texto": "Comida, ropa, crianza."}, {"titulo": "Derechos", "texto": "Los mismos para todos."}],
"glosario": [{"palabra": "Aguayo", "significado": "Tela de colores para cargar cosas o bebés."}, {"palabra": "Poncho", "significado": "Abrigo de lana con un agujero para la cabeza."}],
"carpeta": ["Leé la tarjeta 1: ¿es un aguayo o un poncho?", "Leé la tarjeta 2: ¿es un aguayo o un poncho?", "Lola dice que una comida es mejor que todas las otras. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("AGUAYO") + low("UN AGUAYO") + low("ES UN AGUAYO"), low("PONCHO") + low("UN PONCHO") + low("ES UN PONCHO"), NO],
"soluciones": {"incompleto": "CULTURA.", "solo": "Tu comida especial.", "carpeta": ["Un aguayo.", "Un poncho.", "No: son distintas, no mejores."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer historias que pasan de abuelos a nietos.",
"vas_a_ver": ["Historias de vida", "Cuentos heredados", "Contar y escuchar"],
"secciones": [
 S(1, "Historias de vida", [
  D("Historia de vida", "Lo que le pasó a una persona con los años."),
  P("Lola entrevista a Doña Rosa. Le cuenta que llegó en tren desde otra provincia."),
  P("Trabajó de costurera y crió a sus hijos en el barrio."),
  IMG("La vida de Doña Rosa", "Paso a paso.", FG.tiras(["1. NACIÓ EN EL CAMPO", "2. VIAJÓ EN TREN", "3. TRABAJÓ DE COSTURERA", "4. HOY ES ABUELA"], numeros=False)),
 ]),
 S(1, "Cuentos que se heredan", [
  D("Heredar", "Recibir algo de los mayores, como un cuento o una receta."),
  P("La abuela le contó un cuento a la mamá. La mamá se lo cuenta a Lola."),
  P("Así, los cuentos y las canciones <b>pasan</b> de abuelos a nietos."),
  IMG("El cuento viaja", "De abuela a nieta.", FG.nombres(["ABUELA", "MAMÁ", "LOLA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Qué pasó primero?", FG.tiras(["TRABAJÓ DE COSTURERA", "NACIÓ EN EL CAMPO", "HOY ES ABUELA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Entrevistar", "planteo": "¿Cómo armo una historia de vida?", "pasos": ["Pregunto dónde nació.", "Pregunto en qué trabajó.", "Ordeno lo que me contó."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Recibir algo de los que vinieron antes es…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Entrevista", "planteo": "Preguntale a un abuelo un cuento que le contaban de chico."},
"tip": {"titulo": "Escuchá con atención", "texto": "Las historias de los mayores enseñan mucho."},
"ojo": ["Cada familia tiene su historia.", "Contar y escuchar mantiene vivos los recuerdos."],
"resumen": [{"titulo": "Historia de vida", "texto": "Lo que le pasó a alguien."}, {"titulo": "Heredar", "texto": "Recibir de los mayores."}, {"titulo": "Cuentos", "texto": "Pasan de abuelos a nietos."}],
"glosario": [{"palabra": "Costurera", "significado": "Persona que cose ropa."}, {"palabra": "Nieta", "significado": "Hija del hijo o de la hija."}],
"carpeta": ["De las tarjetas, ¿qué pasó primero en la vida de Doña Rosa?", "¿Qué pasó al final?", "Lola dice que los cuentos de la abuela no sirven para nada. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("NACIÓ EN EL CAMPO") + low("nacio en el campo"), low("HOY ES ABUELA") + low("ES ABUELA"), NO],
"soluciones": {"incompleto": "HEREDAR.", "solo": "El cuento del abuelo.", "carpeta": ["Nació en el campo.", "Hoy es abuela.", "No: enseñan y se heredan."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a aprender qué son los prejuicios.",
"vas_a_ver": ["Prejuicio", "Discriminar", "Cómo cuidarnos"],
"secciones": [
 S(1, "El prejuicio", [
  D("Prejuicio", "Pensar algo de una persona <b>sin conocerla</b>."),
  P("Llega un chico nuevo que habla otro idioma. Alguien dice: «No va a saber jugar»."),
  P("¡Eso es un prejuicio! No lo conoce todavía."),
  IMG("Prejuicio o conocer", "Comparamos.", FG.tiras(["PREJUICIO: OPINO SIN CONOCER", "CONOCER: PREGUNTO Y JUEGO"], numeros=False, cols=1)),
 ]),
 S(1, "Discriminar", [
  D("Discriminar", "Tratar mal o dejar afuera a alguien por ser <b>distinto</b>."),
  P("Nadie puede ser discriminado por su color, idioma o religión."),
  P("Si vemos que discriminan a alguien, <b>avisamos</b> a un adulto."),
  IMG("Para no discriminar", "Lo que sí hacemos.", FG.nombres(["INVITAR", "PREGUNTAR", "RESPETAR"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Está bien?", "Pensá en cada una.", FG.tiras(["1. NO DEJAN JUGAR A UNA NENA PORQUE ES NUEVA", "2. INVITAN AL CHICO NUEVO A JUGAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El chico nuevo", "planteo": "Llega Kenji al grado.", "pasos": ["Habla poco castellano.", "Lola lo invita a jugar.", "¡Descubren que les gusta lo mismo!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Pensar algo de alguien sin conocerlo es un…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Qué harías si un compañero queda solo en el recreo?"},
"tip": {"titulo": "Primero conocé", "texto": "Antes de opinar, preguntá y escuchá."},
"ojo": ["Discriminar está mal y lastima.", "Si pasa, avisale a un adulto."],
"resumen": [{"titulo": "Prejuicio", "texto": "Opinar sin conocer."}, {"titulo": "Discriminar", "texto": "Dejar afuera."}, {"titulo": "Respetar", "texto": "Invitar y conocer."}],
"glosario": [{"palabra": "Prejuicio", "significado": "Opinión sin conocer."}, {"palabra": "Discriminar", "significado": "Tratar mal por ser distinto."}],
"carpeta": ["¿La tarjeta 1 está bien o mal?", "¿La tarjeta 2 está bien o mal?", "Lola dice: «Dejemos afuera al que habla otro idioma». ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("MAL") + low("ESTÁ MAL") + low("esta mal"), low("BIEN") + low("ESTÁ BIEN") + low("esta bien"), NO],
"soluciones": {"incompleto": "PREJUICIO.", "solo": "Lo que harías.", "carpeta": ["Mal: es discriminar.", "Bien.", "No: es discriminar."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer el carnaval y otras fiestas.",
"vas_a_ver": ["El carnaval", "Murgas y comparsas", "Otras fiestas"],
"secciones": [
 S(1, "El carnaval", [
  P("El <b>carnaval</b> es una fiesta con música, baile y disfraces."),
  P("Se festeja en muchos lugares de América, cada uno a su manera."),
  D("Murga", "Grupo que canta y baila por la calle, con bombos."),
  IMG("En el carnaval", "Mucha alegría.", FG.tiras(["MURGAS QUE BAILAN", "COMPARSAS CON PLUMAS", "DISFRACES Y MÁSCARAS", "AGUA Y ESPUMA"], numeros=False)),
 ]),
 S(1, "Otras fiestas", [
  P("Cada cultura tiene sus fiestas. Algunas familias festejan el <b>Año Nuevo chino</b> con dragones."),
  P("Otras agradecen a la <b>Pachamama</b>, la madre tierra, con comida y música."),
  P("Compartir las fiestas nos ayuda a conocernos."),
  IMG("Fiestas de muchas culturas", "Todas valen.", FG.nombres(["CARNAVAL", "AÑO NUEVO CHINO", "PACHAMAMA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué fiesta es?", "Pensá en cada pista.", FG.tiras(["1. HAY MURGAS, DISFRACES Y ESPUMA", "2. SE AGRADECE A LA MADRE TIERRA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La murga del barrio", "planteo": "¿Cómo prepara su traje Lola?", "pasos": ["Elige los colores.", "Le cose lentejuelas.", "¡Sale a bailar con la murga!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El grupo que canta y baila con bombos es la…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu fiesta", "planteo": "¿Qué fiesta te gusta más? Dibujala."},
"tip": {"titulo": "Compartí", "texto": "Invitá a tus amigos a conocer tus fiestas."},
"ojo": ["Cada fiesta tiene su historia.", "Todas las fiestas merecen respeto."],
"resumen": [{"titulo": "Carnaval", "texto": "Música y disfraces."}, {"titulo": "Murga", "texto": "Canta y baila."}, {"titulo": "Otras fiestas", "texto": "Cada cultura, la suya."}],
"glosario": [{"palabra": "Comparsa", "significado": "Grupo que desfila disfrazado."}, {"palabra": "Pachamama", "significado": "La madre tierra para los pueblos andinos."}],
"carpeta": ["¿Qué fiesta es la pista 1?", "¿Qué fiesta es la pista 2?", "Lola dice que solo vale la fiesta de su familia. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("CARNAVAL") + low("EL CARNAVAL"), low("PACHAMAMA") + low("LA PACHAMAMA") + low("FIESTA DE LA PACHAMAMA"), NO],
"soluciones": {"incompleto": "MURGA.", "solo": "Tu dibujo.", "carpeta": ["El carnaval.", "La Pachamama.", "No: todas valen."]},
}

ACT = {
"1": [MC("YANINA LLEVA A SU HERMANITO EN UNA TELA A LA ESPALDA. ¿CÓMO SE LLAMA?", ["AGUAYO", "PONCHO"], "AGUAYO", "ES UNA TELA DE COLORES.", n="aplicar"),
      TF("MATEO DICE QUE UNA CULTURA ES MEJOR QUE OTRA.", "FALSO", "SON DISTINTAS.", n="error")],
"2": [ORD("ORDENÁ LA VIDA DE DOÑA ROSA.", ["HOY ES ABUELA", "NACIÓ EN EL CAMPO", "VIAJÓ EN TREN"], ["NACIÓ EN EL CAMPO", "VIAJÓ EN TREN", "HOY ES ABUELA"], "PRIMERO NACIÓ.", n="analizar"),
      MC("LA ABUELA CONTÓ UN CUENTO. HOY LOLA LO SABE. ¿QUÉ PASÓ CON EL CUENTO?", ["SE HEREDÓ", "SE PERDIÓ"], "SE HEREDÓ", "PASÓ DE UNA A OTRA.", n="analizar")],
"3": [MC("LLEGA UNA NENA NUEVA Y ALGUIEN DICE «NO SABE JUGAR». ¿QUÉ ES ESO?", ["UN PREJUICIO", "UN ACUERDO"], "UN PREJUICIO", "NO LA CONOCE.", n="aplicar"),
      UNI("UNÍ: ¿ESTÁ BIEN O MAL?", [("INVITAR A JUGAR", "BIEN"), ("DEJAR AFUERA", "MAL")], "PENSÁ EN EL OTRO.", n="analizar")],
"4": [UNI("UNÍ CADA FIESTA.", [("CARNAVAL", "MURGAS"), ("AÑO NUEVO CHINO", "DRAGONES"), ("PACHAMAMA", "MADRE TIERRA")], "CADA CULTURA, SU FIESTA.", n="analizar"),
      TF("JULIA DICE QUE SOLO VALE LA FIESTA DE SU FAMILIA.", "FALSO", "TODAS VALEN.", n="error")],
"5": [MC("RELÁMPAGO. LA FORMA DE VIVIR ES LA…", ["CULTURA", "PLAZA"], "CULTURA", "COMIDA, ROPA, FIESTAS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. RECIBIR DE LOS MAYORES ES…", ["HEREDAR", "PERDER"], "HEREDAR", "COMO UN CUENTO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. OPINAR SIN CONOCER ES…", ["PREJUICIO", "RESPETO"], "PREJUICIO", "PRIMERO CONOCÉ.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. CANTA Y BAILA EN CARNAVAL…", ["LA MURGA", "EL TREN"], "LA MURGA", "CON BOMBOS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES LA CULTURA?", ["LA FORMA DE VIVIR DE UN GRUPO", "UN JUEGO DEL RECREO"], "LA FORMA DE VIVIR DE UN GRUPO", "COMIDAS, ROPA, FIESTAS.", n="recordar")],
 [1, MC("EN UNA CASA COMEN AREPAS Y EN OTRA EMPANADAS. ¿CUÁL ES MEJOR?", ["NINGUNA: SON DISTINTAS", "SOLO LAS EMPANADAS"], "NINGUNA: SON DISTINTAS", "CADA COSTUMBRE VALE.", n="analizar")],
 [1, SA("HACE FRÍO. DON JUAN SE PONE UN ABRIGO DE LANA. ¿QUÉ ES?", low("PONCHO") + low("UN PONCHO") + low("EL PONCHO"), "UN PONCHO.", n="aplicar")],
 [2, MC("¿QUÉ ES UNA HISTORIA DE VIDA?", ["LO QUE LE PASÓ A ALGUIEN", "UN CUENTO DE MAGIA"], "LO QUE LE PASÓ A ALGUIEN", "A LO LARGO DE LOS AÑOS.", n="recordar")],
 [2, ORD("ORDENÁ: CÓMO ARMO UNA HISTORIA DE VIDA.", ["ORDENO LO QUE ME CONTÓ", "PREGUNTO DÓNDE NACIÓ", "PREGUNTO EN QUÉ TRABAJÓ"], ["PREGUNTO DÓNDE NACIÓ", "PREGUNTO EN QUÉ TRABAJÓ", "ORDENO LO QUE ME CONTÓ"], "PRIMERO PREGUNTO.", n="analizar")],
 [2, TF("LUCAS DICE QUE LOS CUENTOS DE LOS ABUELOS NO SIRVEN.", "FALSO", "ENSEÑAN Y SE HEREDAN.", n="error")],
 [3, MC("¿QUÉ ES DISCRIMINAR?", ["DEJAR AFUERA POR SER DISTINTO", "INVITAR A JUGAR"], "DEJAR AFUERA POR SER DISTINTO", "ESTÁ MAL.", n="recordar")],
 [3, MC("VES QUE NO DEJAN JUGAR A UN COMPAÑERO POR SU IDIOMA. ¿QUÉ HACÉS?", ["AVISO A UN ADULTO", "ME RÍO"], "AVISO A UN ADULTO", "Y LO INVITO A JUGAR.", n="aplicar")],
 [3, TF("TOMÁS DICE QUE SE PUEDE DEJAR AFUERA A ALGUIEN POR SU COLOR.", "FALSO", "ES DISCRIMINAR.", n="error")],
 [4, SA("EN EL CARNAVAL, UN GRUPO CANTA Y BAILA CON BOMBOS. ¿CÓMO SE LLAMA?", low("MURGA") + low("LA MURGA") + low("UNA MURGA"), "LA MURGA.", n="aplicar")],
 [4, MC("UNA FAMILIA FESTEJA CON DRAGONES DE COLORES. ¿QUÉ FIESTA ES?", ["AÑO NUEVO CHINO", "PACHAMAMA"], "AÑO NUEVO CHINO", "CON DRAGONES.", n="aplicar")],
 [4, TF("COMPARTIR FIESTAS NOS AYUDA A CONOCERNOS.", "VERDADERO", "Y A RESPETARNOS.", n="recordar")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 8, "estilo": "primeros",
     "practica": "Práctica general: distintas costumbres, mismos derechos", "examen_titulo": "Nivel jefe: distintas costumbres, mismos derechos",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
