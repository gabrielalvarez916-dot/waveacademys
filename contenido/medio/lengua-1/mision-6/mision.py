# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 6 · Cuentos que ya conocemos. Genera mision-6.json.
Regla de primeros años. Cuentos tradicionales de dominio público (Caperucita Roja, Los tres chanchitos, El patito feo).
Metáfora: la ronda de cuentos en la biblioteca de la escuela de Sofi.
Niveles: 1 leer títulos de cuentos conocidos · 2 ordenar las escenas del cuento · 3 escribir los nombres de los personajes · 4 leer una frase del cuento."""
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
ESCENAS = ["SALE DE SU CASA", "SE ENCUENTRA AL LOBO", "EL LOBO CORRE", "EL CAZADOR LAS SALVA"]

N1 = {**ESTILO,
"objetivo": "Vas a leer los títulos de cuentos que conocés.",
"vas_a_ver": ["Qué es un título", "Títulos de cuentos", "Encontrar un cuento"],
"secciones": [
 S(1, "Los títulos", [
  P("En la biblioteca hay muchos cuentos. Cada uno tiene su <b>título</b>."),
  IMG("Títulos de cuentos", "Tres cuentos conocidos.", FG.nombres(["CAPERUCITA ROJA", "LOS TRES CHANCHITOS", "EL PATITO FEO"], cols=1)),
 ]),
 S(1, "Qué es el título", [
  D("Título", "El <b>nombre del cuento</b>. Está en la tapa, con letras grandes."),
  P("El título nos dice de qué se trata."),
  IMG("Una tapa", "El título en la tapa.", FG.nombres(["CAPERUCITA ROJA"], cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los títulos. Los vas a usar en la carpeta."),
  IMG("Títulos", "Leelos.", FG.nombres(["LOS TRES CHANCHITOS", "EL PATITO FEO"], cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar un cuento", "planteo": "Buscamos el cuento del lobo y la nena.", "pasos": ["Miro los títulos.", "Leo: CAPERUCITA ROJA.", "¡Es ese!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El patito.", "pasos": ["EL PATITO ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuento", "planteo": "¿Cuál es tu cuento preferido? Escribí su título."},
"tip": {"titulo": "Mirá la tapa", "texto": "El título siempre está en la tapa, bien grande."},
"ojo": ["El título no es todo el cuento.", "Leé el título antes de empezar."],
"resumen": [{"titulo": "Título", "texto": "El nombre del cuento."}, {"titulo": "Tapa", "texto": "Ahí está el título."}, {"titulo": "Buscar", "texto": "Leyendo títulos."}],
"glosario": [{"palabra": "Título", "significado": "Nombre del cuento."}, {"palabra": "Tapa", "significado": "La parte de adelante del libro."}],
"carpeta": ["¿Cuántos chanchitos dice el título?", "¿Cómo es el patito?", "¿Qué palabra se repite en los dos títulos?"],
"respuestas_carpeta": [["TRES", "tres", "Tres", "3"], low("FEO"), ["EL", "el", "LOS", "los"]],
"soluciones": {"incompleto": "FEO.", "solo": "Depende de tu cuento.", "carpeta": ["TRES.", "FEO.", "EL (o LOS)."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ordenar lo que pasa en el cuento.",
"vas_a_ver": ["Principio, medio y final", "Qué pasa primero", "Contar el cuento en orden"],
"secciones": [
 S(1, "En orden", [
  P("En <b>Caperucita Roja</b> pasan cosas en orden."),
  IMG("Las escenas", "Del 1 al 4.", FG.tiras(ESCENAS)),
 ]),
 S(1, "Principio, medio y final", [
  D("Orden del cuento", "Todo cuento tiene <b>principio</b>, <b>medio</b> y <b>final</b>."),
  P("Principio: sale de su casa. Medio: el lobo. Final: el cazador las salva."),
  IMG("Principio, medio y final", "Las tres partes.", FG.tiras(["PRINCIPIO: SALE", "MEDIO: EL LOBO", "FINAL: LAS SALVAN"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las escenas. Las vas a usar en la carpeta."),
  IMG("Sin números", "¿Cuál va primero?", FG.tiras(["EL CAZADOR LAS SALVA", "SALE DE SU CASA", "SE ENCUENTRA AL LOBO"], ocultar_num=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Los chanchitos", "planteo": "Ordenamos.", "pasos": ["1. Hacen sus casas.", "2. Viene el lobo y sopla.", "3. Se salvan en la casa de ladrillos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿Qué pasa al final?", "pasos": ["Al final, el cazador ___ ."]},
"ejemplo_solo": {"titulo": "Contalo", "planteo": "Contale a alguien el cuento de Caperucita en orden."},
"tip": {"titulo": "Preguntá", "texto": "¿Qué pasó primero? ¿Y después? ¿Cómo terminó?"},
"ojo": ["El final va al final.", "Si cambiás el orden, el cuento no se entiende."],
"resumen": [{"titulo": "Principio", "texto": "Cómo empieza."}, {"titulo": "Medio", "texto": "El problema."}, {"titulo": "Final", "texto": "Cómo termina."}],
"glosario": [{"palabra": "Escena", "significado": "Un momento del cuento."}, {"palabra": "Final", "significado": "Cómo termina."}],
"carpeta": ["¿Qué escena va primero?", "¿Qué escena va segunda?", "¿Qué escena va al final?"],
"respuestas_carpeta": [["SALE DE SU CASA", "sale de su casa", "Sale de su casa"], ["SE ENCUENTRA AL LOBO", "se encuentra al lobo", "Se encuentra al lobo"], ["EL CAZADOR LAS SALVA", "el cazador las salva", "El cazador las salva"]],
"soluciones": {"incompleto": "LAS SALVA.", "solo": "Sale de su casa, se encuentra al lobo, el lobo corre, el cazador las salva.", "carpeta": ["SALE DE SU CASA.", "SE ENCUENTRA AL LOBO.", "EL CAZADOR LAS SALVA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir los nombres de los personajes.",
"vas_a_ver": ["Qué es un personaje", "Los personajes de Caperucita", "Escribir sus nombres"],
"secciones": [
 S(1, "Los personajes", [
  D("Personaje", "Quien <b>hace cosas</b> en el cuento: una nena, un lobo, una abuela…"),
  IMG("Personajes", "Los de Caperucita Roja.", FG.nombres(["CAPERUCITA", "LOBO", "ABUELA", "CAZADOR"], cols=2)),
 ]),
 S(1, "Escribir nombres", [
  P("<b>LOBO</b>: LO-BO. Cuatro letras."),
  IMG("LOBO", "L, O, B, O.", FG.letras("LOBO", numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el nombre. Lo vas a usar en la carpeta."),
  IMG("Completá", "ABUELA con huecos.", FG.letras("ABUELA", ocultar=(1, 4), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "MAMÁ", "planteo": "Escribimos el personaje MAMÁ.", "pasos": ["Digo: MA-MÁ.", "Escribo MA y MÁ.", "MAMÁ."]},
"ejemplo_incompleto": {"titulo": "LOBO", "planteo": "Completá.", "pasos": ["L _ B _ ."]},
"ejemplo_solo": {"titulo": "Tu personaje", "planteo": "Escribí el nombre de un personaje que te guste."},
"tip": {"titulo": "Decilo lento", "texto": "Decí el nombre despacio y escribí cada sonido."},
"ojo": ["Los nombres de personajes también llevan sus letras en orden.", "CAPERUCITA es largo: escribilo por sílabas."],
"resumen": [{"titulo": "Personaje", "texto": "Hace cosas en el cuento."}, {"titulo": "Nombres", "texto": "LOBO, ABUELA."}, {"titulo": "Escribir", "texto": "Sílaba por sílaba."}],
"glosario": [{"palabra": "Personaje", "significado": "Quien está en el cuento."}, {"palabra": "Cazador", "significado": "Persona que caza."}],
"carpeta": ["¿Qué letra va en el lugar 2?", "¿Qué letra va en el lugar 5?", "¿Qué personaje es?"],
"respuestas_carpeta": [low("B"), low("L"), low("ABUELA")],
"soluciones": {"incompleto": "LOBO.", "solo": "Por ejemplo: CAPERUCITA.", "carpeta": ["B.", "L.", "ABUELA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a leer una frase famosa del cuento.",
"vas_a_ver": ["Lo que dicen los personajes", "Leer la frase", "Leer con emoción"],
"secciones": [
 S(1, "Lo que dicen", [
  P("Caperucita le dice al lobo: <b>¡QUÉ OJOS TAN GRANDES!</b>"),
  IMG("La frase", "Palabra por palabra.", FG.nombres(["¡QUÉ", "OJOS", "TAN", "GRANDES!"], cols=4)),
 ]),
 S(1, "Leer con emoción", [
  D("Signos de exclamación", "<b>¡ !</b> Avisan que la frase se dice con <b>emoción</b>."),
  P("El lobo contesta: <b>¡PARA VERTE MEJOR!</b>"),
  IMG("La respuesta", "Con emoción.", FG.nombres(["¡PARA", "VERTE", "MEJOR!"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la frase. La vas a usar en la carpeta."),
  IMG("Otra frase", "Leela con emoción.", FG.nombres(["¡QUÉ", "BOCA", "TAN", "GRANDE!"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Las orejas", "planteo": "¡QUÉ OREJAS TAN GRANDES!", "pasos": ["Leo palabra por palabra.", "Veo los signos ¡ !", "La digo con emoción."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La respuesta del lobo.", "pasos": ["¡PARA VERTE ___ !"]},
"ejemplo_solo": {"titulo": "Actuala", "planteo": "Leé la frase de Caperucita con voz de sorpresa."},
"tip": {"titulo": "Mirá los signos", "texto": "Si ves ¡ !, leé con emoción."},
"ojo": ["El signo ¡ va al principio y el ! al final.", "Leé toda la frase sin parar."],
"resumen": [{"titulo": "Frase", "texto": "Lo que dice un personaje."}, {"titulo": "¡ !", "texto": "Con emoción."}, {"titulo": "Leer", "texto": "Palabra por palabra."}],
"glosario": [{"palabra": "Frase", "significado": "Palabras que dice alguien."}, {"palabra": "Emoción", "significado": "Sorpresa, alegría, miedo…"}],
"carpeta": ["¿Qué parte de la cara dice la frase?", "¿Cómo es la boca?", "¿Cuántas palabras tiene la frase?"],
"respuestas_carpeta": [low("BOCA"), low("GRANDE"), ["4"]],
"soluciones": {"incompleto": "MEJOR.", "solo": "¡QUÉ OJOS TAN GRANDES!", "carpeta": ["BOCA.", "GRANDE.", "4."]},
}

ACT = {
"1": [MC("¿DÓNDE ESTÁ EL TÍTULO DE UN CUENTO?", ["EN LA TAPA", "AL FINAL", "EN NINGÚN LADO"], "EN LA TAPA", "CON LETRAS GRANDES."),
      MC("¿QUÉ TÍTULO TIENE UN LOBO Y UNA NENA?", ["CAPERUCITA ROJA", "EL PATITO FEO", "LOS TRES CHANCHITOS"], "CAPERUCITA ROJA", "CAPERUCITA SE ENCUENTRA AL LOBO.")],
"2": [ORD("ORDENÁ EL CUENTO.", ["EL CAZADOR LAS SALVA", "SALE DE SU CASA", "SE ENCUENTRA AL LOBO"], ["SALE DE SU CASA", "SE ENCUENTRA AL LOBO", "EL CAZADOR LAS SALVA"], "PRINCIPIO, MEDIO Y FINAL."),
      MC("¿QUÉ PASA AL FINAL DE CAPERUCITA?", ["EL CAZADOR LAS SALVA", "SALE DE SU CASA"], "EL CAZADOR LAS SALVA", "ASÍ TERMINA.")],
"3": [MC("¿QUIÉN ES UN PERSONAJE DE CAPERUCITA?", ["EL LOBO", "EL PATITO", "EL CHANCHITO"], "EL LOBO", "EL LOBO ESTÁ EN EL CUENTO."),
      SA("¿QUÉ LETRA FALTA? LO_O", low("B"), "LO-BO.")],
"4": [MC("¿QUÉ DICE CAPERUCITA?", ["¡QUÉ OJOS TAN GRANDES!", "¡HOLA, PATITO!", "¡A COMER!"], "¡QUÉ OJOS TAN GRANDES!", "ES LA FRASE DEL CUENTO."),
      MC("LOS SIGNOS ¡ ! NOS DICEN QUE LEAMOS…", ["CON EMOCIÓN", "EN SILENCIO", "AL REVÉS"], "CON EMOCIÓN", "ES UNA EXCLAMACIÓN.")],
"5": [MC("RELÁMPAGO. ¿CUÁNTOS CHANCHITOS HAY?", ["3", "2", "5"], "3", "LOS TRES CHANCHITOS.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ VA PRIMERO?", ["EL PRINCIPIO", "EL FINAL"], "EL PRINCIPIO", "PRINCIPIO, MEDIO Y FINAL.", tiempo=30),
      SA("RELÁMPAGO. ¿QUÉ LETRA FALTA? _OBO", low("L"), "LOBO.", tiempo=30),
      MC("RELÁMPAGO. ¿PARA QUÉ TIENE OJOS GRANDES EL LOBO?", ["PARA VERTE MEJOR", "PARA COMER", "PARA DORMIR"], "PARA VERTE MEJOR", "ASÍ CONTESTA EL LOBO.", tiempo=30)],
}
EXAMEN = [
 [1, MC("EL TÍTULO ES…", ["EL NOMBRE DEL CUENTO", "UN PERSONAJE", "EL FINAL"], "EL NOMBRE DEL CUENTO", "ESTÁ EN LA TAPA.")],
 [1, MC("¿CÓMO ES EL PATITO DEL TÍTULO?", ["FEO", "ROJO", "GRANDE"], "FEO", "EL PATITO FEO.")],
 [1, MC("¿QUÉ COLOR DICE EL TÍTULO DE CAPERUCITA?", ["ROJA", "AZUL", "VERDE"], "ROJA", "CAPERUCITA ROJA.")],
 [2, ORD("ORDENÁ.", ["EL LOBO CORRE", "SALE DE SU CASA", "EL CAZADOR LAS SALVA"], ["SALE DE SU CASA", "EL LOBO CORRE", "EL CAZADOR LAS SALVA"], "PRINCIPIO, MEDIO Y FINAL.")],
 [2, MC("¿CÓMO EMPIEZA CAPERUCITA?", ["SALE DE SU CASA", "EL CAZADOR LAS SALVA"], "SALE DE SU CASA", "ES EL PRINCIPIO.")],
 [2, MC("TODO CUENTO TIENE PRINCIPIO, MEDIO Y…", ["FINAL", "TAPA", "TÍTULO"], "FINAL", "CÓMO TERMINA.")],
 [3, MC("UN PERSONAJE ES…", ["QUIEN HACE COSAS EN EL CUENTO", "EL TÍTULO", "LA TAPA"], "QUIEN HACE COSAS EN EL CUENTO", "COMO EL LOBO.")],
 [3, SA("¿QUÉ LETRA FALTA? A_UELA", low("B"), "A-BUE-LA.")],
 [3, MC("¿QUIÉN SALVA A CAPERUCITA?", ["EL CAZADOR", "EL LOBO", "EL PATITO"], "EL CAZADOR", "AL FINAL.")],
 [4, MC("¿QUIÉN DICE ¡PARA VERTE MEJOR!?", ["EL LOBO", "LA ABUELA", "CAPERUCITA"], "EL LOBO", "LE CONTESTA A CAPERUCITA.")],
 [4, MC("¿DÓNDE VA EL SIGNO ¡?", ["AL PRINCIPIO", "AL FINAL"], "AL PRINCIPIO", "¡ AL PRINCIPIO Y ! AL FINAL.")],
 [4, MC("¿CUÁNTAS PALABRAS TIENE: ¡QUÉ OJOS TAN GRANDES!?", ["4", "3", "5"], "4", "QUÉ · OJOS · TAN · GRANDES.")],
 [4, MC("UNA FRASE CON ¡ ! SE LEE…", ["CON EMOCIÓN", "MUY BAJITO"], "CON EMOCIÓN", "ES UNA EXCLAMACIÓN.")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: cuentos que ya conocemos", "examen_titulo": "Nivel jefe: cuentos que ya conocemos",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
