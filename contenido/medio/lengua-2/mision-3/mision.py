# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 3 · La Cenicienta. Genera mision-3.json.
Regla de primeros años y vía fonológica. Cuento tradicional (versión propia, contada con palabras simples).
Metáfora: el cuaderno viajero de Sofi (Sofi lee el cuento con la abuela y anota lo que descubre).
Niveles: 1 escuchar La Cenicienta · 2 los personajes y sus deseos · 3 lugares y objetos mágicos · 4 comparar con otros cuentos de hadas."""
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

N1 = {**ESTILO,
"objetivo": "Vas a conocer el cuento de La Cenicienta.",
"vas_a_ver": ["Cómo empieza", "Qué pasa en el baile", "Cómo termina"],
"secciones": [
 S(1, "El cuento", [
  P("Cenicienta vivía con su madrastra y sus dos hermanastras."),
  P("Ellas la trataban mal. Cenicienta limpiaba toda la casa."),
  P("Un día, el príncipe hizo un <b>baile</b> en el castillo."),
  P("Su <b>hada madrina</b> le dio un vestido y una carroza."),
  P("Tenía que volver antes de las <b>doce</b> de la noche."),
  P("Al salir corriendo, perdió un <b>zapatito de cristal</b>."),
  P("El príncipe la buscó. ¡El zapatito era de ella!"),
  IMG("Momentos del cuento", "Al principio, en el medio y al final.", FG.tiras(["CENICIENTA LIMPIA LA CASA.", "VA AL BAILE DEL CASTILLO.", "PIERDE UN ZAPATITO.", "EL PRÍNCIPE LA ENCUENTRA."], numeros=True)),
 ]),
 S(1, "Un cuento tradicional", [
  D("Cuento tradicional", "Es un cuento muy viejo que se cuenta hace muchos años."),
  P("Empieza con <b>«había una vez»</b>."),
  IMG("Objetos del cuento", "Cosas que aparecen.", FG.objetos([("castillo", "castillo"), ("zapato", "zapatito"), ("reloj", "reloj")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("Las tiras del cuento", "Están numeradas.", FG.tiras(["EL HADA LE DA UN VESTIDO.", "SUENAN LAS DOCE."], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "¿Qué pasó?", "planteo": "¿Qué perdió Cenicienta?", "pasos": ["Salió corriendo a las doce.", "Se le cayó algo en la escalera.", "Perdió un zapatito de cristal."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Completá con palabras del cuento.", "pasos": ["El príncipe hizo un ___ .", "Tenía que volver antes de las ___ ."]},
"ejemplo_solo": {"titulo": "Contalo", "planteo": "Contale el cuento a alguien de tu casa con tus palabras."},
"tip": {"titulo": "Principio, medio y final", "texto": "Pensá qué pasa en cada parte."},
"ojo": ["El hada madrina ayuda a Cenicienta.", "Las hermanastras no la ayudan."],
"resumen": [{"titulo": "Principio", "texto": "Cenicienta limpia."}, {"titulo": "Medio", "texto": "Va al baile."}, {"titulo": "Final", "texto": "El príncipe la encuentra."}],
"glosario": [{"palabra": "Madrastra", "significado": "La esposa del papá."}, {"palabra": "Baile", "significado": "Una fiesta para bailar."}],
"carpeta": ["¿Quién le da el vestido a Cenicienta?", "¿A qué hora tenía que volver?", "Tomi dice que Cenicienta perdió una corona. ¿Qué perdió?"],
"carpeta_nivel": ["recordar", "recordar", "error"],
"respuestas_carpeta": [low("EL HADA") + low("EL HADA MADRINA") + low("HADA MADRINA") + low("HADA"), ["12", "a las 12", "A LAS DOCE", "a las doce", "DOCE", "doce"], low("UN ZAPATITO") + low("ZAPATITO") + low("UN ZAPATITO DE CRISTAL")],
"soluciones": {"incompleto": "BAILE. DOCE.", "solo": "Lo contás con tus palabras.", "carpeta": ["El hada madrina.", "A las doce.", "Un zapatito de cristal."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer a los personajes y lo que quieren.",
"vas_a_ver": ["Quiénes son", "Cómo son", "Qué desean"],
"secciones": [
 S(1, "Los personajes", [
  D("Personaje", "Es quien aparece y hace cosas en el cuento."),
  P("Cenicienta es <b>buena</b> y trabajadora."),
  P("La madrastra y las hermanastras son <b>malas</b> con ella."),
  P("El hada madrina es <b>generosa</b>: la ayuda."),
  IMG("Los personajes", "Cada uno con su nombre.", FG.nombres(["CENICIENTA", "MADRASTRA", "HADA", "PRÍNCIPE"], cols=2)),
 ]),
 S(1, "Lo que desean", [
  D("Deseo", "Es lo que un personaje <b>quiere</b> que pase."),
  P("Cenicienta desea <b>ir al baile</b>."),
  P("El príncipe desea <b>encontrarla</b>."),
  IMG("Deseos", "Lo que quiere cada uno.", FG.tiras(["CENICIENTA: IR AL BAILE.", "PRÍNCIPE: ENCONTRARLA."], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los nombres. Los vas a usar en la carpeta."),
  IMG("Personajes para unir", "¿Cómo es cada uno?", FG.nombres(["HADA", "HERMANASTRAS"], cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "El hada", "planteo": "¿Cómo es el hada madrina?", "pasos": ["Le da un vestido.", "Le da una carroza.", "Es generosa: la ayuda."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cenicienta desea ir al ___ .", "pasos": ["Desea ir al ___ ."]},
"ejemplo_solo": {"titulo": "Tu deseo", "planteo": "Si tuvieras un hada madrina, ¿qué le pedirías?"},
"tip": {"titulo": "Mirá lo que hacen", "texto": "Lo que hace un personaje dice cómo es."},
"ojo": ["El hada no es mala: ayuda.", "Las hermanastras no ayudan a Cenicienta."],
"resumen": [{"titulo": "Personaje", "texto": "Quien hace cosas."}, {"titulo": "Cómo es", "texto": "Por lo que hace."}, {"titulo": "Deseo", "texto": "Lo que quiere."}],
"glosario": [{"palabra": "Generosa", "significado": "Que da y ayuda."}, {"palabra": "Deseo", "significado": "Lo que alguien quiere."}],
"carpeta": ["¿Cómo es el hada: buena o mala?", "¿Cómo son las hermanastras con Cenicienta?", "¿Qué desea Cenicienta?"],
"carpeta_nivel": ["analizar", "analizar", "recordar"],
"respuestas_carpeta": [low("BUENA") + low("GENEROSA"), low("MALAS") + low("MALOS"), low("IR AL BAILE") + low("EL BAILE")],
"soluciones": {"incompleto": "BAILE.", "solo": "Lo que vos quieras.", "carpeta": ["Buena.", "Malas.", "Ir al baile."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a encontrar los lugares y los objetos mágicos del cuento.",
"vas_a_ver": ["Dónde pasa", "La magia del hada", "A las doce todo cambia"],
"secciones": [
 S(1, "Los lugares", [
  P("El cuento pasa en la <b>casa</b> y en el <b>castillo</b>."),
  IMG("El castillo", "Donde es el baile.", FG.objetos([("castillo", "castillo")])),
 ]),
 S(1, "Objetos mágicos", [
  D("Objeto mágico", "Es una cosa que hace algo <b>imposible</b> en la vida real."),
  P("Con la <b>varita</b>, la calabaza se convierte en <b>carroza</b>."),
  P("Los ratones se convierten en <b>caballos</b>."),
  P("A las <b>doce</b>, la magia se termina."),
  IMG("La magia", "Lo que cambia con la varita.", FG.objetos([("varita", "varita"), ("calabaza", "calabaza"), ("raton", "ratón"), ("reloj", "reloj")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los objetos. Los vas a usar en la carpeta."),
  IMG("Objetos del cuento", "¿En qué se convierten?", FG.objetos([("calabaza", "calabaza"), ("raton", "ratón")])),
 ]),
],
"ejemplo_completo": {"titulo": "La calabaza", "planteo": "¿Qué pasa con la calabaza?", "pasos": ["El hada usa la varita.", "La calabaza se convierte en carroza.", "¡Es magia!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "A las doce…", "pasos": ["La carroza vuelve a ser ___ ."]},
"ejemplo_solo": {"titulo": "Tu objeto mágico", "planteo": "Inventá un objeto mágico. ¿Qué haría?"},
"tip": {"titulo": "¿Pasa de verdad?", "texto": "Si no puede pasar en la vida real, es magia."},
"ojo": ["El zapatito no desaparece a las doce.", "La magia dura hasta las doce."],
"resumen": [{"titulo": "Lugares", "texto": "La casa y el castillo."}, {"titulo": "Magia", "texto": "Varita, carroza, caballos."}, {"titulo": "Las doce", "texto": "Se termina la magia."}],
"glosario": [{"palabra": "Carroza", "significado": "Un carro lujoso tirado por caballos."}, {"palabra": "Varita", "significado": "Palito mágico del hada."}],
"carpeta": ["¿En qué se convierte la calabaza?", "¿En qué se convierten los ratones?", "Sofi dice que la magia dura toda la noche. ¿Hasta cuándo dura?"],
"carpeta_nivel": ["recordar", "recordar", "error"],
"respuestas_carpeta": [low("CARROZA") + low("EN CARROZA") + low("EN UNA CARROZA"), low("CABALLOS") + low("EN CABALLOS"), ["hasta las doce", "HASTA LAS DOCE", "las doce", "12", "hasta las 12", "Hasta las doce"]],
"soluciones": {"incompleto": "CALABAZA.", "solo": "Lo que vos imagines.", "carpeta": ["En carroza.", "En caballos.", "Hasta las doce."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a comparar La Cenicienta con otros cuentos de hadas.",
"vas_a_ver": ["Cuentos de hadas", "En qué se parecen", "En qué son distintos"],
"secciones": [
 S(1, "Cuentos de hadas", [
  D("Cuento de hadas", "Tiene <b>magia</b>, personajes buenos y malos, y un <b>final feliz</b>."),
  P("Blancanieves y Caperucita también son cuentos tradicionales."),
  IMG("Tres cuentos", "Cuentos que se cuentan hace mucho.", FG.nombres(["CENICIENTA", "BLANCANIEVES", "CAPERUCITA"], cols=3)),
 ]),
 S(1, "Se parecen y son distintos", [
  P("En Cenicienta y en Blancanieves hay una <b>madrastra mala</b>."),
  P("En Cenicienta hay un <b>hada</b>. En Caperucita hay un <b>lobo</b>."),
  IMG("Comparar", "Lo que tiene cada uno.", FG.tiras(["CENICIENTA: HADA Y ZAPATITO.", "BLANCANIEVES: MANZANA Y ENANITOS.", "CAPERUCITA: LOBO Y CANASTA."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("¿De qué cuento es?", "Pensá en cada cuento.", FG.tiras(["UNA MANZANA ENVENENADA.", "UN ZAPATITO DE CRISTAL."], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Comparar", "planteo": "¿En qué se parecen Cenicienta y Blancanieves?", "pasos": ["Las dos tienen madrastra mala.", "Las dos tienen un príncipe.", "Las dos terminan felices."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En Caperucita hay un ___ .", "pasos": ["En Caperucita hay un ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuento", "planteo": "¿Qué cuento de hadas te gusta más? ¿Por qué?"},
"tip": {"titulo": "Buscá lo igual", "texto": "Primero lo que se parece, después lo distinto."},
"ojo": ["No todos los cuentos tienen hada.", "No todos los cuentos tienen príncipe."],
"resumen": [{"titulo": "Cuento de hadas", "texto": "Magia y final feliz."}, {"titulo": "Se parecen", "texto": "Madrastra, príncipe."}, {"titulo": "Distintos", "texto": "Hada, lobo, manzana."}],
"glosario": [{"palabra": "Comparar", "significado": "Ver en qué se parecen y en qué no."}, {"palabra": "Final feliz", "significado": "Cuando todo termina bien."}],
"carpeta": ["¿De qué cuento es la manzana envenenada?", "¿De qué cuento es el zapatito de cristal?", "Tomi dice que en Cenicienta hay un lobo. ¿Qué personaje ayuda a Cenicienta?"],
"carpeta_nivel": ["recordar", "recordar", "error"],
"respuestas_carpeta": [low("BLANCANIEVES"), low("CENICIENTA"), low("EL HADA") + low("HADA") + low("EL HADA MADRINA") + low("HADA MADRINA")],
"soluciones": {"incompleto": "LOBO.", "solo": "El que vos elijas.", "carpeta": ["Blancanieves.", "Cenicienta.", "El hada madrina: el lobo es de Caperucita."]},
}

ACT = {
"1": [ORD("ORDENÁ LO QUE PASA EN EL CUENTO.", ["PIERDE UN ZAPATITO", "LIMPIA LA CASA", "VA AL BAILE"], ["LIMPIA LA CASA", "VA AL BAILE", "PIERDE UN ZAPATITO"], "PRINCIPIO, MEDIO Y FINAL.", n="analizar"),
      MC("¿QUÉ PERDIÓ CENICIENTA?", ["UN ZAPATITO", "UNA CORONA", "UN RELOJ"], "UN ZAPATITO", "UN ZAPATITO DE CRISTAL.", n="recordar")],
"2": [UNI("UNÍ CADA PERSONAJE CON CÓMO ES.", [("HADA MADRINA", "GENEROSA"), ("HERMANASTRAS", "MALAS"), ("CENICIENTA", "TRABAJADORA")], "POR LO QUE HACEN.", n="analizar"),
      MC("¿QUÉ DESEA CENICIENTA?", ["IR AL BAILE", "LIMPIAR MÁS", "SER HADA"], "IR AL BAILE", "ESO QUIERE.", n="recordar")],
"3": [MC("¿EN QUÉ SE CONVIERTE LA CALABAZA?", ["EN CARROZA", "EN CABALLO", "EN VESTIDO"], "EN CARROZA", "CON LA VARITA.", n="recordar"),
      TF("LA MAGIA DURA HASTA LAS DOCE.", "VERDADERO", "A LAS DOCE SE TERMINA.", n="recordar")],
"4": [MC("¿EN QUÉ CUENTO HAY UN LOBO?", ["CAPERUCITA", "CENICIENTA", "BLANCANIEVES"], "CAPERUCITA", "EL LOBO ES DE CAPERUCITA.", n="aplicar"),
      TF("CENICIENTA Y BLANCANIEVES TIENEN UNA MADRASTRA MALA.", "VERDADERO", "SE PARECEN EN ESO.", n="analizar")],
"5": [MC("RELÁMPAGO. ¿QUIÉN AYUDA A CENICIENTA?", ["EL HADA", "LA MADRASTRA"], "EL HADA", "EL HADA MADRINA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿DÓNDE ES EL BAILE?", ["EN EL CASTILLO", "EN EL BOSQUE"], "EN EL CASTILLO", "EN EL CASTILLO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿A QUÉ HORA TERMINA LA MAGIA?", ["A LAS DOCE", "A LAS TRES"], "A LAS DOCE", "A LAS DOCE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ TIENE UN CUENTO DE HADAS?", ["MAGIA", "NOTICIAS"], "MAGIA", "MAGIA Y FINAL FELIZ.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, ORD("ORDENÁ EL CUENTO.", ["EL PRÍNCIPE LA ENCUENTRA", "EL HADA LE DA UN VESTIDO", "SUENAN LAS DOCE"], ["EL HADA LE DA UN VESTIDO", "SUENAN LAS DOCE", "EL PRÍNCIPE LA ENCUENTRA"], "PRINCIPIO, MEDIO Y FINAL.", n="analizar")],
 [1, SA("¿QUIÉN HIZO EL BAILE?", low("EL PRÍNCIPE") + low("PRÍNCIPE") + low("principe"), "EL PRÍNCIPE.", n="recordar")],
 [1, TF("TOMI DICE QUE CENICIENTA PERDIÓ UNA CORONA.", "FALSO", "PERDIÓ UN ZAPATITO.", n="error")],
 [2, MC("¿CÓMO ES EL HADA MADRINA?", ["GENEROSA", "MALA", "ENOJADA"], "GENEROSA", "LA AYUDA.", n="analizar")],
 [2, MC("¿QUÉ DESEA EL PRÍNCIPE?", ["ENCONTRAR A CENICIENTA", "IR AL BOSQUE", "COMER"], "ENCONTRAR A CENICIENTA", "LA BUSCA CON EL ZAPATITO.", n="recordar")],
 [2, TF("LAS HERMANASTRAS AYUDAN A CENICIENTA.", "FALSO", "LA TRATAN MAL.", n="error")],
 [3, MC("¿EN QUÉ SE CONVIERTEN LOS RATONES?", ["EN CABALLOS", "EN PERROS", "EN PÁJAROS"], "EN CABALLOS", "POR LA MAGIA.", n="recordar")],
 [3, UNI("UNÍ CADA OBJETO CON LO QUE PASA.", [("VARITA", "HACE MAGIA"), ("CALABAZA", "SE HACE CARROZA"), ("ZAPATITO", "SE PIERDE")], "LOS OBJETOS DEL CUENTO.", n="analizar")],
 [3, MC("¿DÓNDE VIVE CENICIENTA AL PRINCIPIO?", ["CON SU MADRASTRA", "EN EL CASTILLO", "EN EL BOSQUE"], "CON SU MADRASTRA", "EN LA CASA DE LA MADRASTRA.", n="recordar")],
 [4, MC("¿DE QUÉ CUENTO ES LA MANZANA ENVENENADA?", ["BLANCANIEVES", "CENICIENTA", "CAPERUCITA"], "BLANCANIEVES", "BLANCANIEVES COME LA MANZANA.", n="aplicar")],
 [4, MC("¿QUÉ TIENEN LOS CUENTOS DE HADAS?", ["MAGIA Y FINAL FELIZ", "NÚMEROS Y CUENTAS", "RECETAS"], "MAGIA Y FINAL FELIZ", "ASÍ SON.", n="analizar")],
 [4, SA("¿EN QUÉ CUENTO HAY UN LOBO?", low("CAPERUCITA") + low("CAPERUCITA ROJA"), "EN CAPERUCITA.", n="aplicar")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: La Cenicienta", "examen_titulo": "Nivel jefe: La Cenicienta",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
