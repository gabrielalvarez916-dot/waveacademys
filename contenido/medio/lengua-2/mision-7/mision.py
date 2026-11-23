# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 7 · Textos informativos. Genera mision-7.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (hoy pega una lámina sobre el hornero).
Niveles: 1 títulos e imágenes · 2 leer un texto informativo · 3 subrayar datos importantes · 4 responder por escrito."""
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
TXT = ["ES UN PÁJARO DE ARGENTINA.", "HACE SU NIDO CON BARRO.", "EL NIDO PARECE UN HORNO.", "COME BICHITOS."]

N1 = {**ESTILO,
"objetivo": "Vas a mirar el título y la imagen de un texto.",
"vas_a_ver": ["El título", "La imagen", "El epígrafe"],
"secciones": [
 S(1, "Una lámina nueva", [
  P("Sofi pegó una <b>lámina</b> en su cuaderno viajero."),
  P("Es un <b>texto informativo</b>: cuenta cosas reales."),
  IMG("La lámina de Sofi", "Mirá el título arriba.", FG.lamina("El hornero", TXT, pie="El hornero", marcar_titulo=True)),
 ]),
 S(1, "Título e imagen", [
  D("Título", "Dice <b>de qué trata</b> el texto."),
  D("Imagen", "<b>Muestra</b> cómo es lo que se cuenta."),
  D("Epígrafe", "Es la frase <b>debajo</b> de la imagen."),
  IMG("El hornero y su nido", "La imagen ayuda a entender.", FG.objetos([("hornero", "EL HORNERO"), ("nido", "SU NIDO")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá estas imágenes. Las vas a usar en la carpeta."),
  IMG("Tres imágenes", "¿Qué título le pondrías?", FG.objetos([("flor", "?"), ("nido", "?"), ("raton", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "El título", "planteo": "Título: EL HORNERO. ¿De qué trata?", "pasos": ["Leo el título.", "Dice EL HORNERO.", "Trata sobre ese pájaro."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Mirá la lámina de Sofi.", "pasos": ["El título es ___ .", "La imagen muestra un ___ ."]},
"ejemplo_solo": {"titulo": "Tu lámina", "planteo": "Dibujá tu animal preferido. Ponele un título."},
"tip": {"titulo": "Mirá antes de leer", "texto": "El título y la imagen te ayudan."},
"ojo": ["El título va arriba.", "El epígrafe va debajo de la imagen."],
"resumen": [{"titulo": "Título", "texto": "De qué trata."}, {"titulo": "Imagen", "texto": "Muestra cómo es."}, {"titulo": "Epígrafe", "texto": "Debajo de la imagen."}],
"glosario": [{"palabra": "Lámina", "significado": "Hoja con texto e imagen."}, {"palabra": "Epígrafe", "significado": "Frase debajo de una imagen."}],
"carpeta": ["¿Qué título le pondrías a la primera imagen?", "¿Qué título le pondrías a la última imagen?", "Tomi dice que el título va abajo. ¿Dónde va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("LA FLOR") + low("FLOR") + low("LAS FLORES"), low("EL RATÓN") + low("RATÓN") + low("raton") + low("el raton"), low("ARRIBA") + ["Va arriba", "va arriba", "VA ARRIBA"]],
"soluciones": {"incompleto": "EL HORNERO. PÁJARO.", "solo": "Tu dibujo con su título.", "carpeta": ["LA FLOR.", "EL RATÓN.", "Arriba."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a leer un texto informativo.",
"vas_a_ver": ["Cuento o texto informativo", "Cosas reales", "Leer la lámina"],
"secciones": [
 S(1, "¿Cuento o informativo?", [
  D("Cuento", "Cuenta una <b>historia inventada</b>."),
  D("Texto informativo", "Da <b>datos reales</b> sobre algo."),
  IMG("Dos textos", "Uno inventa y otro informa.", FG.tiras(["CUENTO: HABÍA UNA VEZ UN HADA.", "INFORMATIVO: EL HORNERO COME BICHITOS."], numeros=False, cols=1)),
 ]),
 S(1, "Leer la lámina", [
  P("Leé el texto de Sofi despacio."),
  P("Cada oración da un <b>dato</b>."),
  IMG("El hornero", "Cuatro datos reales.", FG.lamina("El hornero", TXT, pie="El hornero")),
 ]),
 S(2, "Para practicar", [
  P("Leé estas oraciones. Las vas a usar en la carpeta."),
  IMG("¿Dato o invento?", "Pensá si es real.", FG.tiras(["EL HORNERO HABLA CON LOS GATOS.", "EL HORNERO TIENE PLUMAS."], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "¿Es real?", "planteo": "EL HORNERO HACE SU NIDO CON BARRO.", "pasos": ["Es algo que pasa de verdad.", "Es un dato real.", "Es de un texto informativo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Leé la lámina de Sofi.", "pasos": ["El hornero come ___ .", "El nido parece un ___ ."]},
"ejemplo_solo": {"titulo": "Tu dato", "planteo": "Escribí un dato real de tu mascota o de un animal."},
"tip": {"titulo": "¿Pasa de verdad?", "texto": "Si es real, es un dato."},
"ojo": ["Los animales no hablan: eso es de cuento.", "Leé todo el texto, no solo el título."],
"resumen": [{"titulo": "Cuento", "texto": "Historia inventada."}, {"titulo": "Informativo", "texto": "Datos reales."}, {"titulo": "Dato", "texto": "Algo que es verdad."}],
"glosario": [{"palabra": "Dato", "significado": "Algo real que se sabe."}, {"palabra": "Real", "significado": "Que es verdad."}],
"carpeta": ["¿Qué oración del dibujo es un dato real?", "¿Qué oración del dibujo es un invento?", "Tomi dice que un texto informativo inventa. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [["2", "LA 2", "la 2", "La 2", "EL HORNERO TIENE PLUMAS", "El hornero tiene plumas"], ["1", "LA 1", "la 1", "La 1", "EL HORNERO HABLA CON LOS GATOS", "El hornero habla con los gatos"], ["NO", "no", "No"]],
"soluciones": {"incompleto": "BICHITOS. HORNO.", "solo": "Un dato que sea verdad.", "carpeta": ["La 2: tiene plumas.", "La 1: no habla.", "No: da datos reales."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a subrayar los datos importantes.",
"vas_a_ver": ["Qué es importante", "Subrayar", "Leer lo subrayado"],
"secciones": [
 S(1, "Lo importante", [
  P("Sofi quiere recordar lo <b>más importante</b>."),
  D("Subrayar", "Marcar con color las <b>palabras clave</b>."),
  IMG("Lámina subrayada", "Las palabras clave, en amarillo.", FG.lamina("El hornero", TXT, pie="El hornero", subrayar=[(0, "pájaro"), (1, "barro"), (2, "horno"), (3, "bichitos")])),
 ]),
 S(1, "Leer lo subrayado", [
  P("Después leemos <b>solo</b> lo marcado."),
  P("PÁJARO, BARRO, HORNO, BICHITOS."),
  IMG("Las palabras clave", "Con ellas recordamos el texto.", FG.nombres(["PÁJARO", "BARRO", "HORNO", "BICHITOS"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Leé esta lámina. La vas a usar en la carpeta."),
  IMG("La paloma", "Buscá las palabras clave.", FG.lamina("La paloma", ["ES UN PÁJARO DE LA PLAZA.", "COME SEMILLAS.", "HACE SU NIDO EN LOS ÁRBOLES."], dibujo="paloma", pie="Una paloma")),
 ]),
],
"ejemplo_completo": {"titulo": "Subrayar", "planteo": "HACE SU NIDO CON BARRO.", "pasos": ["¿Qué es lo importante?", "Con qué hace el nido.", "Subrayo BARRO."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "COME BICHITOS.", "pasos": ["La palabra clave es ___ ."]},
"ejemplo_solo": {"titulo": "Tu lámina", "planteo": "Subrayá dos palabras clave en un texto de tu libro."},
"tip": {"titulo": "Poco y bien", "texto": "Subrayá pocas palabras, las más importantes."},
"ojo": ["Si subrayás todo, nada se destaca.", "EL, LA, UN no son palabras clave."],
"resumen": [{"titulo": "Subrayar", "texto": "Marcar lo importante."}, {"titulo": "Pocas", "texto": "Solo palabras clave."}, {"titulo": "Repasar", "texto": "Leer lo subrayado."}],
"glosario": [{"palabra": "Subrayar", "significado": "Marcar con una línea o color."}, {"palabra": "Clave", "significado": "Lo más importante."}],
"carpeta": ["En la lámina de la paloma, ¿qué come? Subrayá esa palabra.", "¿Dónde hace su nido la paloma?", "Tomi subrayó todo el texto. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("SEMILLAS"), low("EN LOS ÁRBOLES") + low("en los arboles") + low("ÁRBOLES") + low("arboles"), ["NO", "no", "No"]],
"soluciones": {"incompleto": "BICHITOS.", "solo": "Dos palabras importantes.", "carpeta": ["SEMILLAS.", "EN LOS ÁRBOLES.", "No: se subraya poco."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a responder preguntas por escrito.",
"vas_a_ver": ["Leer la pregunta", "Buscar en el texto", "Responder con oración"],
"secciones": [
 S(1, "Responder", [
  P("Tomi le pregunta a Sofi: ¿con qué hace el nido el hornero?"),
  P("Sofi busca en la lámina y <b>responde por escrito</b>."),
  IMG("La pregunta", "La respuesta está en el texto.", FG.ficha([("¿Con qué hace el nido?", "con barro")], titulo="Pregunta de Tomi")),
 ]),
 S(1, "Una oración completa", [
  P("Respondemos con una <b>oración</b>."),
  P("Empieza con <b>mayúscula</b> y termina con <b>punto</b>."),
  IMG("Bien respondido", "Con mayúscula y punto.", FG.tiras(["EL HORNERO HACE SU NIDO CON BARRO."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la ficha. La vas a usar en la carpeta."),
  IMG("Ficha del hornero", "Completá lo que falta.", FG.ficha([("¿Qué es?", "un pájaro"), ("¿Qué come?", ""), ("¿A qué se parece el nido?", "")], titulo="Ficha del hornero")),
 ]),
],
"ejemplo_completo": {"titulo": "Responder", "planteo": "¿Qué es el hornero?", "pasos": ["Busco en la lámina.", "Dice: es un pájaro.", "Escribo: El hornero es un pájaro."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿Dónde vive el hornero?", "pasos": ["Busco en la lámina.", "El hornero vive en ___ ."]},
"ejemplo_solo": {"titulo": "Tu pregunta", "planteo": "Inventá una pregunta sobre el hornero. Respondela."},
"tip": {"titulo": "Volvé al texto", "texto": "La respuesta está en la lámina."},
"ojo": ["Empezá con mayúscula.", "Terminá con punto."],
"resumen": [{"titulo": "Leer", "texto": "La pregunta."}, {"titulo": "Buscar", "texto": "En el texto."}, {"titulo": "Escribir", "texto": "Oración con mayúscula y punto."}],
"glosario": [{"palabra": "Pregunta", "significado": "Lo que queremos saber."}, {"palabra": "Respuesta", "significado": "Lo que contestamos."}],
"carpeta": ["¿Qué come el hornero?", "¿A qué se parece el nido del hornero?", "Tomi escribió: el hornero come bichitos. ¿Qué le falta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("BICHITOS") + low("COME BICHITOS") + low("EL HORNERO COME BICHITOS") + ["El hornero come bichitos."], low("A UN HORNO") + low("UN HORNO") + low("HORNO") + ["Parece un horno.", "PARECE UN HORNO", "parece un horno"], ["MAYÚSCULA Y PUNTO", "mayúscula y punto", "Mayúscula y punto", "mayuscula y punto", "La mayúscula y el punto", "la mayúscula y el punto"]],
"soluciones": {"incompleto": "ARGENTINA.", "solo": "Tu pregunta y su respuesta.", "carpeta": ["Come bichitos.", "A un horno.", "Mayúscula al principio y punto al final."]},
}

ACT = {
"1": [MC("¿PARA QUÉ SIRVE EL TÍTULO?", ["DICE DE QUÉ TRATA", "ES UN DIBUJO", "VA AL FINAL"], "DICE DE QUÉ TRATA", "EL TÍTULO DICE EL TEMA.", n="recordar"),
      UNI("UNÍ CADA PARTE CON LO QUE HACE.", [("TÍTULO", "DE QUÉ TRATA"), ("IMAGEN", "CÓMO ES"), ("EPÍGRAFE", "FRASE DEBAJO")], "CADA PARTE AYUDA.", n="analizar")],
"2": [TF("UN TEXTO INFORMATIVO DA DATOS REALES.", "VERDADERO", "INFORMA COSAS QUE SON VERDAD.", n="recordar"),
      MC("¿CUÁL ES UN DATO REAL?", ["EL HORNERO COME BICHITOS", "EL HORNERO HABLA", "EL HORNERO VUELA A LA LUNA"], "EL HORNERO COME BICHITOS", "ES VERDAD.", n="analizar")],
"3": [MC("HACE SU NIDO CON BARRO. ¿QUÉ PALABRA SUBRAYÁS?", ["BARRO", "SU", "CON"], "BARRO", "ES LA PALABRA CLAVE.", n="aplicar"),
      TF("HAY QUE SUBRAYAR TODO EL TEXTO.", "FALSO", "SE SUBRAYA SOLO LO IMPORTANTE.", n="error")],
"4": [SA("¿CON QUÉ HACE EL NIDO EL HORNERO?", low("BARRO") + low("CON BARRO") + low("HACE SU NIDO CON BARRO") + ["Con barro."], "CON BARRO.", n="aplicar"),
      MC("¿CUÁL RESPUESTA ESTÁ BIEN ESCRITA?", ["EL HORNERO ES UN PÁJARO CON PUNTO", "EL HORNERO ES UN PÁJARO SIN PUNTO"], "EL HORNERO ES UN PÁJARO CON PUNTO", "LA ORACIÓN TERMINA CON PUNTO.", n="analizar")],
"5": [MC("RELÁMPAGO. EL TÍTULO VA…", ["ARRIBA", "ABAJO"], "ARRIBA", "ARRIBA DEL TEXTO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. UN TEXTO INFORMATIVO…", ["DA DATOS", "INVENTA"], "DA DATOS", "DATOS REALES.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. SE SUBRAYA…", ["LO IMPORTANTE", "TODO"], "LO IMPORTANTE", "POCAS PALABRAS.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA RESPUESTA TERMINA CON…", ["PUNTO", "NADA"], "PUNTO", "CON PUNTO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿DÓNDE VA EL EPÍGRAFE?", ["DEBAJO DE LA IMAGEN", "ARRIBA DEL TÍTULO", "EN OTRA HOJA"], "DEBAJO DE LA IMAGEN", "ES LA FRASE DE LA IMAGEN.", n="recordar")],
 [1, SA("UN TEXTO HABLA DEL HORNERO. ESCRIBÍ UN TÍTULO.", low("EL HORNERO") + low("HORNERO"), "EL HORNERO.", n="aplicar")],
 [1, TF("LA IMAGEN MUESTRA CÓMO ES LO QUE SE CUENTA.", "VERDADERO", "AYUDA A ENTENDER.", n="recordar")],
 [2, MC("¿QUÉ TEXTO ES INFORMATIVO?", ["EL HORNERO TIENE PLUMAS", "HABÍA UNA VEZ UN HADA", "EL GATO HABLABA CON SU AMIGO"], "EL HORNERO TIENE PLUMAS", "DA UN DATO REAL.", n="analizar")],
 [2, TF("LOS CUENTOS DAN SOLO DATOS REALES.", "FALSO", "LOS CUENTOS INVENTAN.", n="error")],
 [2, SA("EL NIDO PARECE UN… ¿QUÉ?", low("HORNO") + low("UN HORNO"), "UN HORNO.", n="recordar")],
 [3, MC("COME BICHITOS. ¿QUÉ PALABRA SUBRAYÁS?", ["BICHITOS", "COME"], "BICHITOS", "ES LO QUE COME.", n="aplicar")],
 [3, UNI("UNÍ CADA ORACIÓN CON SU PALABRA CLAVE.", [("HACE SU NIDO CON BARRO", "BARRO"), ("ES UN PÁJARO DE ARGENTINA", "PÁJARO"), ("EL NIDO PARECE UN HORNO", "HORNO")], "LA PALABRA MÁS IMPORTANTE.", n="analizar")],
 [3, TF("TOMI SUBRAYÓ LA PALABRA EL. ESTÁ BIEN.", "FALSO", "EL NO ES PALABRA CLAVE.", n="error")],
 [4, SA("¿QUÉ COME EL HORNERO?", low("BICHITOS") + low("COME BICHITOS") + low("EL HORNERO COME BICHITOS") + ["El hornero come bichitos."], "BICHITOS.", n="aplicar")],
 [4, MC("¿CÓMO EMPIEZA UNA RESPUESTA ESCRITA?", ["CON MAYÚSCULA", "CON PUNTO", "CON MINÚSCULA"], "CON MAYÚSCULA", "Y TERMINA CON PUNTO.", n="recordar")],
 [4, TF("TOMI ESCRIBIÓ: el hornero es un pájaro. ESTÁ BIEN ESCRITO.", "FALSO", "LE FALTAN LA MAYÚSCULA Y EL PUNTO.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: textos informativos", "examen_titulo": "Nivel jefe: textos informativos",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
