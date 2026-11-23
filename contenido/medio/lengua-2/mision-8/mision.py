# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 8 · Fichas informativas. Genera mision-8.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (hoy arma su propia ficha sobre el yaguareté).
Niveles: 1 elegir un tema · 2 buscar datos · 3 escribir la ficha · 4 revisar y compartir la ficha."""
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
FICHA = [("¿Qué es?", "un animal"), ("¿Dónde vive?", "en la selva"), ("¿Cómo es?", "tiene manchas"), ("¿Qué come?", "otros animales")]

N1 = {**ESTILO,
"objetivo": "Vas a elegir el tema de tu ficha.",
"vas_a_ver": ["Qué es una ficha", "Qué es un tema", "Elegir uno solo"],
"secciones": [
 S(1, "La ficha de Sofi", [
  P("Sofi quiere hacer su <b>propia ficha</b> informativa."),
  D("Ficha informativa", "Hoja corta con <b>datos reales</b> sobre algo."),
  IMG("Una ficha", "Tiene título, dibujo y datos.", FG.ficha(FICHA[:2], titulo="El yaguareté")),
 ]),
 S(1, "Elegir el tema", [
  D("Tema", "Es <b>de qué</b> va a tratar la ficha."),
  P("Sofi elige <b>uno solo</b>: el yaguareté."),
  P("Todos los animales es <b>demasiado</b> para una ficha."),
  IMG("El tema de Sofi", "Un animal de Argentina.", FG.objetos([("yaguarete", "EL YAGUARETÉ")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los temas. Los vas a usar en la carpeta."),
  IMG("¿Cuál sirve?", "Pensá si es uno solo.", FG.tiras(["1. TODOS LOS ANIMALES", "2. EL HORNERO", "3. TODO EL MUNDO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Elegir", "planteo": "¿Las plantas o el girasol?", "pasos": ["Las plantas son muchísimas.", "El girasol es uno solo.", "Elijo el girasol."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Sofi elige su tema.", "pasos": ["El tema de Sofi es el ___ ."]},
"ejemplo_solo": {"titulo": "Tu tema", "planteo": "Elegí un animal para tu ficha. Escribí su nombre."},
"tip": {"titulo": "Uno solo", "texto": "Un tema chico se cuenta mejor."},
"ojo": ["Elegí algo que te guste.", "Elegí algo real, no inventado."],
"resumen": [{"titulo": "Ficha", "texto": "Datos reales en una hoja."}, {"titulo": "Tema", "texto": "De qué trata."}, {"titulo": "Uno solo", "texto": "Un tema chico."}],
"glosario": [{"palabra": "Tema", "significado": "De qué trata algo."}, {"palabra": "Yaguareté", "significado": "Animal grande con manchas."}],
"carpeta": ["¿Qué tema del dibujo sirve para una ficha?", "¿Cuál es el tema de la ficha de Sofi?", "Tomi eligió TODO EL MUNDO. ¿Sirve para una ficha?"],
"carpeta_nivel": ["analizar", "recordar", "error"],
"respuestas_carpeta": [low("EL HORNERO") + low("HORNERO") + ["2", "EL 2", "el 2"], low("EL YAGUARETÉ") + low("YAGUARETÉ") + low("yaguarete") + low("el yaguarete"), NO],
"soluciones": {"incompleto": "YAGUARETÉ.", "solo": "El nombre de tu animal.", "carpeta": ["EL HORNERO.", "EL YAGUARETÉ.", "No: es demasiado grande."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a buscar datos para tu ficha.",
"vas_a_ver": ["Dónde buscar", "Hacer preguntas", "Anotar datos cortos"],
"secciones": [
 S(1, "Dónde buscar", [
  P("Sofi busca datos del yaguareté."),
  P("Busca en <b>libros</b> y <b>láminas</b>."),
  P("Pregunta a un <b>adulto</b> y mira <b>internet</b> con un adulto."),
  IMG("Lugares para buscar", "Siempre datos reales.", FG.tiras(["LIBROS", "LÁMINAS", "UN ADULTO", "INTERNET CON UN ADULTO"], numeros=False)),
 ]),
 S(1, "Preguntas guía", [
  P("Sofi se hace <b>preguntas</b> y busca las respuestas."),
  IMG("Las preguntas de Sofi", "Cada respuesta es un dato.", FG.ficha([("¿Qué es?", ""), ("¿Dónde vive?", ""), ("¿Cómo es?", ""), ("¿Qué come?", "")], titulo="Preguntas")),
 ]),
 S(2, "Para practicar", [
  P("Leé los datos de Sofi. Los vas a usar en la carpeta."),
  IMG("Datos del yaguareté", "Datos cortos y reales.", FG.lamina("El yaguareté", ["ES UN ANIMAL GRANDE.", "VIVE EN LA SELVA.", "TIENE MANCHAS.", "COME OTROS ANIMALES."], dibujo="yaguarete", pie="El yaguareté")),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar", "planteo": "¿Dónde vive el yaguareté?", "pasos": ["Busco en un libro.", "Dice: vive en la selva.", "Anoto: VIVE EN LA SELVA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Mirá los datos de Sofi.", "pasos": ["El yaguareté tiene ___ ."]},
"ejemplo_solo": {"titulo": "Tus datos", "planteo": "Buscá dos datos de tu animal con un adulto."},
"tip": {"titulo": "Datos cortos", "texto": "Anotá pocas palabras, no copies todo."},
"ojo": ["En internet, siempre con un adulto.", "Solo datos reales, nada inventado."],
"resumen": [{"titulo": "Buscar", "texto": "Libros, láminas, adultos."}, {"titulo": "Preguntar", "texto": "¿Qué es? ¿Dónde vive?"}, {"titulo": "Anotar", "texto": "Datos cortos."}],
"glosario": [{"palabra": "Selva", "significado": "Lugar con muchos árboles y plantas."}, {"palabra": "Anotar", "significado": "Escribir para no olvidar."}],
"carpeta": ["¿Dónde vive el yaguareté?", "¿Qué come el yaguareté?", "Tomi copió el libro entero. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("EN LA SELVA") + low("LA SELVA") + low("SELVA") + ["Vive en la selva.", "VIVE EN LA SELVA"], low("OTROS ANIMALES") + low("ANIMALES") + ["Come otros animales.", "COME OTROS ANIMALES"], NO],
"soluciones": {"incompleto": "MANCHAS.", "solo": "Dos datos reales.", "carpeta": ["En la selva.", "Otros animales.", "No: se anotan datos cortos."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir tu ficha.",
"vas_a_ver": ["Las partes de la ficha", "Un dato por renglón", "Oraciones cortas"],
"secciones": [
 S(1, "Las partes", [
  P("La ficha tiene <b>título</b> arriba y un <b>dibujo</b>."),
  P("Después van los <b>datos</b>, uno por renglón."),
  IMG("La ficha de Sofi", "Con todas sus partes.", FG.lamina("El yaguareté", ["ES UN ANIMAL GRANDE.", "VIVE EN LA SELVA.", "TIENE MANCHAS.", "COME OTROS ANIMALES."], dibujo="yaguarete", pie="El yaguareté", marcar_titulo=True)),
 ]),
 S(1, "Oraciones cortas", [
  P("Cada dato es una <b>oración corta</b>."),
  P("Empieza con <b>mayúscula</b> y termina con <b>punto</b>."),
  IMG("Del dato a la oración", "SELVA → VIVE EN LA SELVA.", FG.tiras(["SELVA → VIVE EN LA SELVA.", "MANCHAS → TIENE MANCHAS."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la ficha. La vas a usar en la carpeta."),
  IMG("Ficha para completar", "Faltan dos datos.", FG.ficha([("¿Qué es?", "un pájaro"), ("¿Con qué hace el nido?", ""), ("¿Qué come?", "")], titulo="El hornero")),
 ]),
],
"ejemplo_completo": {"titulo": "Escribir", "planteo": "Dato: MANCHAS.", "pasos": ["Armo una oración.", "Tiene manchas.", "Con mayúscula y punto."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Dato: SELVA.", "pasos": ["Vive en la ___ ."]},
"ejemplo_solo": {"titulo": "Tu ficha", "planteo": "Escribí la ficha de tu animal con título, dibujo y dos datos."},
"tip": {"titulo": "Un dato, un renglón", "texto": "Así la ficha se lee fácil."},
"ojo": ["No te olvides del título.", "Cada oración con mayúscula y punto."],
"resumen": [{"titulo": "Título", "texto": "Arriba."}, {"titulo": "Dibujo", "texto": "Muestra cómo es."}, {"titulo": "Datos", "texto": "Uno por renglón."}],
"glosario": [{"palabra": "Renglón", "significado": "Línea donde se escribe."}, {"palabra": "Oración", "significado": "Palabras que dicen algo completo."}],
"carpeta": ["En la ficha del hornero, ¿con qué hace el nido?", "¿Qué come el hornero?", "Tomi hizo una ficha sin título. ¿Qué le falta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("CON BARRO") + low("BARRO"), low("BICHITOS") + low("COME BICHITOS"), low("EL TÍTULO") + low("TÍTULO") + low("titulo") + low("el titulo")],
"soluciones": {"incompleto": "SELVA.", "solo": "Tu ficha completa.", "carpeta": ["Con barro.", "Bichitos.", "El título."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a revisar y compartir tu ficha.",
"vas_a_ver": ["Revisar la ficha", "Corregir errores", "Leerla al grado"],
"secciones": [
 S(1, "Revisar", [
  P("Antes de compartir, Sofi <b>revisa</b> su ficha."),
  P("¿Tiene título? ¿Mayúsculas? ¿Puntos?"),
  IMG("Lista para revisar", "Una marca por cada cosa.", FG.lista(["TÍTULO", "DIBUJO", "MAYÚSCULAS", "PUNTOS"], titulo="REVISO MI FICHA", marcar=(0, 1, 2, 3))),
 ]),
 S(1, "Compartir", [
  P("Sofi lee su ficha <b>en voz alta</b> al grado."),
  P("Lee <b>despacio</b> y muestra el dibujo."),
  IMG("Sofi comparte", "Sus compañeros escuchan.", FG.objetos([("yaguarete", "SU TEMA"), ("castillo", "LA ESCUELA")])),
 ]),
 S(2, "Para practicar", [
  P("Leé la ficha de Tomi. La vas a usar en la carpeta."),
  IMG("La ficha de Tomi", "Tiene errores.", FG.tiras(["EL PATO VIVE EN LA LAGUNA", "TIENE PLUMAS."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Revisar", "planteo": "TIENE MANCHAS", "pasos": ["Leo la oración.", "Falta el punto al final.", "TIENE MANCHAS."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "VIVE EN LA SELVA", "pasos": ["Al final le falta el ___ ."]},
"ejemplo_solo": {"titulo": "Compartí", "planteo": "Leé tu ficha en voz alta a tu familia."},
"tip": {"titulo": "Revisá dos veces", "texto": "Una para el contenido y otra para la escritura."},
"ojo": ["Leé despacio para que entiendan.", "Mostrá el dibujo."],
"resumen": [{"titulo": "Revisar", "texto": "Título, mayúscula, punto."}, {"titulo": "Corregir", "texto": "Arreglar los errores."}, {"titulo": "Compartir", "texto": "Leer en voz alta."}],
"glosario": [{"palabra": "Compartir", "significado": "Mostrar a otros lo que hiciste."}, {"palabra": "En voz alta", "significado": "Que todos escuchen."}],
"carpeta": ["En la ficha de Tomi, ¿dónde vive el pato?", "¿Qué le falta a la primera oración de Tomi?", "Tomi lee su ficha muy rápido. ¿Cómo tiene que leer?"],
"carpeta_nivel": ["aplicar", "error", "error"],
"respuestas_carpeta": [low("EN LA LAGUNA") + low("LA LAGUNA") + low("LAGUNA"), low("EL PUNTO") + low("PUNTO") + low("UN PUNTO"), low("DESPACIO") + ["Más despacio", "más despacio", "MÁS DESPACIO", "mas despacio"]],
"soluciones": {"incompleto": "PUNTO.", "solo": "Tu ficha leída en voz alta.", "carpeta": ["En la laguna.", "El punto al final.", "Despacio."]},
}

ACT = {
"1": [MC("¿CUÁL ES UN BUEN TEMA PARA UNA FICHA?", ["EL YAGUARETÉ", "TODOS LOS ANIMALES", "TODO EL MUNDO"], "EL YAGUARETÉ", "ES UNO SOLO.", n="analizar"),
      TF("EL TEMA DICE DE QUÉ TRATA LA FICHA.", "VERDADERO", "ES DE QUÉ VA A HABLAR.", n="recordar")],
"2": [MC("¿DÓNDE BUSCO DATOS REALES?", ["EN UN LIBRO", "EN UN CUENTO DE HADAS", "LOS INVENTO"], "EN UN LIBRO", "LOS LIBROS DAN DATOS.", n="aplicar"),
      SA("¿DÓNDE VIVE EL YAGUARETÉ?", low("EN LA SELVA") + low("LA SELVA") + low("SELVA"), "EN LA SELVA.", n="recordar")],
"3": [UNI("UNÍ CADA PREGUNTA CON SU DATO.", [("¿DÓNDE VIVE?", "EN LA SELVA"), ("¿CÓMO ES?", "TIENE MANCHAS"), ("¿QUÉ COME?", "OTROS ANIMALES")], "CADA PREGUNTA TIENE SU DATO.", n="analizar"),
      MC("¿QUÉ VA ARRIBA EN LA FICHA?", ["EL TÍTULO", "EL PUNTO", "UN DATO"], "EL TÍTULO", "EL TÍTULO VA ARRIBA.", n="recordar")],
"4": [TF("ANTES DE COMPARTIR, HAY QUE REVISAR LA FICHA.", "VERDADERO", "ASÍ ARREGLAMOS LOS ERRORES.", n="recordar"),
      TF("TOMI ESCRIBIÓ UNA ORACIÓN SIN PUNTO. ESTÁ BIEN.", "FALSO", "TODA ORACIÓN TERMINA CON PUNTO.", n="error")],
"5": [MC("RELÁMPAGO. UNA FICHA TIENE DATOS…", ["REALES", "INVENTADOS"], "REALES", "DATOS DE VERDAD.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁNTOS TEMAS TIENE UNA FICHA?", ["UNO", "MUCHOS"], "UNO", "UN TEMA SOLO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. CADA DATO VA EN…", ["UN RENGLÓN", "TODO JUNTO"], "UN RENGLÓN", "UNO POR RENGLÓN.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA FICHA SE LEE…", ["DESPACIO", "MUY RÁPIDO"], "DESPACIO", "ASÍ SE ENTIENDE.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UNA FICHA INFORMATIVA?", ["UNA HOJA CON DATOS REALES", "UN CUENTO INVENTADO", "UN DIBUJO SOLO"], "UNA HOJA CON DATOS REALES", "INFORMA COSAS REALES.", n="recordar")],
 [1, TF("TODOS LOS ANIMALES ES UN BUEN TEMA PARA UNA FICHA.", "FALSO", "ES DEMASIADO GRANDE.", n="error")],
 [1, SA("SOFI HIZO SU FICHA SOBRE UN ANIMAL CON MANCHAS. ¿CUÁL?", low("YAGUARETÉ") + low("yaguarete") + low("EL YAGUARETÉ") + low("el yaguarete"), "EL YAGUARETÉ.", n="recordar")],
 [2, MC("¿CON QUIÉN SE BUSCA EN INTERNET?", ["CON UN ADULTO", "SOLO", "CON UN GATO"], "CON UN ADULTO", "SIEMPRE CON UN ADULTO.", n="recordar")],
 [2, UNI("UNÍ CADA PREGUNTA CON SU DATO.", [("¿QUÉ ES?", "UN ANIMAL GRANDE"), ("¿DÓNDE VIVE?", "EN LA SELVA"), ("¿QUÉ COME?", "OTROS ANIMALES")], "CADA RESPUESTA ES UN DATO.", n="analizar")],
 [2, TF("PARA LA FICHA HAY QUE COPIAR EL LIBRO ENTERO.", "FALSO", "SE ANOTAN DATOS CORTOS.", n="error")],
 [3, MC("¿CÓMO TERMINA CADA ORACIÓN DE LA FICHA?", ["CON PUNTO", "CON UN DIBUJO", "SIN NADA"], "CON PUNTO", "CADA ORACIÓN TERMINA CON PUNTO.", n="analizar")],
 [3, SA("DATO: SELVA. COMPLETÁ: VIVE EN LA ___", low("SELVA"), "VIVE EN LA SELVA.", n="aplicar")],
 [3, TF("EN LA FICHA VA UN DATO POR RENGLÓN.", "VERDADERO", "ASÍ SE LEE FÁCIL.", n="recordar")],
 [4, MC("TOMI HIZO SU FICHA SIN TÍTULO. ¿QUÉ LE FALTA?", ["EL TÍTULO", "UN PERRO", "NADA"], "EL TÍTULO", "EL TÍTULO VA ARRIBA.", n="error")],
 [4, SA("TOMI ESCRIBIÓ: EL PATO NADA (SIN PUNTO). ¿QUÉ LE FALTA?", low("EL PUNTO") + low("PUNTO") + low("UN PUNTO"), "EL PUNTO AL FINAL.", n="error")],
 [4, MC("¿CÓMO SE LEE LA FICHA AL GRADO?", ["EN VOZ ALTA Y DESPACIO", "EN SECRETO", "MUY RÁPIDO"], "EN VOZ ALTA Y DESPACIO", "ASÍ TODOS ENTIENDEN.", n="aplicar")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 8, "estilo": "primeros",
     "practica": "Práctica general: fichas informativas", "examen_titulo": "Nivel jefe: fichas informativas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
