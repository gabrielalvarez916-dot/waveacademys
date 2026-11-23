# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 14 · Singular y plural. Genera mision-14.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (hoy cuenta cosas de la granja: un pato, tres patos).
Niveles: 1 uno y varios · 2 plural con S y con ES · 3 concordar sustantivo y adjetivo · 4 corregir oraciones."""
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
"objetivo": "Vas a distinguir singular y plural.",
"vas_a_ver": ["Uno solo", "Varios", "Cómo cambia la palabra"],
"secciones": [
 S(1, "Uno y varios", [
  D("Singular", "Nombra <b>uno solo</b>: EL PATO."),
  D("Plural", "Nombra <b>varios</b>: LOS PATOS."),
  IMG("Uno y varios", "PATO y PATOS.", FG.objetos([("pato", "UN PATO"), ("pato", "PATOS"), ("pato", "PATOS")])),
 ]),
 S(1, "Cambian también EL y LA", [
  P("EL PATO → <b>LOS</b> PATOS. LA RANA → <b>LAS</b> RANAS."),
  IMG("Singular y plural", "Cambian las dos palabras.", FG.tiras(["EL PATO → LOS PATOS", "LA RANA → LAS RANAS"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Uno o varios?", "Pensá cuántos nombra.", FG.nombres(["FLOR", "UVAS", "NIDO", "ROSAS"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Plural", "planteo": "LA FLOR.", "pasos": ["Es una sola: singular.", "Varias: LAS FLORES.", "Es plural."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Pasá a plural.", "pasos": ["EL GATO → LOS ___ ."]},
"ejemplo_solo": {"titulo": "Contá", "planteo": "Mirá tu mesa y escribí algo en singular y algo en plural."},
"tip": {"titulo": "¿Cuántos?", "texto": "Uno: singular. Varios: plural."},
"ojo": ["EL va con uno. LOS va con varios.", "LA va con una. LAS va con varias."],
"resumen": [{"titulo": "Singular", "texto": "Uno solo."}, {"titulo": "Plural", "texto": "Varios."}, {"titulo": "Cambian", "texto": "EL → LOS, LA → LAS."}],
"glosario": [{"palabra": "Singular", "significado": "Uno solo."}, {"palabra": "Plural", "significado": "Más de uno."}],
"carpeta": ["¿Qué palabras del dibujo están en plural?", "¿Qué palabras del dibujo están en singular?", "Tomi dice que LOS PATOS es singular. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("UVAS Y ROSAS") + low("UVAS, ROSAS") + low("ROSAS Y UVAS"), low("FLOR Y NIDO") + low("FLOR, NIDO") + low("NIDO Y FLOR"), NO],
"soluciones": {"incompleto": "GATOS.", "solo": "Por ejemplo: UN LÁPIZ, LOS LIBROS.", "carpeta": ["UVAS y ROSAS.", "FLOR y NIDO.", "No: es plural."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a formar el plural con S y con ES.",
"vas_a_ver": ["Agregar S", "Agregar ES", "Cuándo va cada una"],
"secciones": [
 S(1, "Con S", [
  P("Si la palabra termina en <b>vocal</b>, agregamos <b>S</b>."),
  IMG("Con S", "Termina en vocal.", FG.tiras(["CASA → CASAS", "PATO → PATOS", "NIDO → NIDOS"], numeros=False, cols=1)),
 ]),
 S(1, "Con ES", [
  P("Si termina en <b>consonante</b>, agregamos <b>ES</b>."),
  IMG("Con ES", "Termina en consonante.", FG.tiras(["FLOR → FLORES", "RATÓN → RATONES", "PAN → PANES"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Para pasar a plural", "¿S o ES?", FG.nombres(["MESA", "SOL", "LORO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Plural", "planteo": "ÁRBOL.", "pasos": ["Termina en L: consonante.", "Agregamos ES.", "ÁRBOLES."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Pasá a plural.", "pasos": ["MESA → ___ .", "SOL → ___ ."]},
"ejemplo_solo": {"titulo": "Tu lista", "planteo": "Escribí tres cosas de tu casa en plural."},
"tip": {"titulo": "Mirá el final", "texto": "Vocal: S. Consonante: ES."},
"ojo": ["FLORS está mal: es FLORES.", "CASAES está mal: es CASAS."],
"resumen": [{"titulo": "Vocal", "texto": "Agregar S."}, {"titulo": "Consonante", "texto": "Agregar ES."}, {"titulo": "Ejemplos", "texto": "CASAS, FLORES."}],
"glosario": [{"palabra": "Vocal", "significado": "A, E, I, O, U."}, {"palabra": "Consonante", "significado": "Las letras que no son vocales."}],
"carpeta": ["¿Cómo es el plural de MESA?", "¿Cómo es el plural de SOL?", "Tomi escribió LOROES. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MESAS") + low("LAS MESAS"), low("SOLES") + low("LOS SOLES"), low("LOROS")],
"soluciones": {"incompleto": "MESAS. SOLES.", "solo": "Tres palabras en plural.", "carpeta": ["MESAS.", "SOLES.", "LOROS: termina en vocal, va S."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a hacer que sustantivo y adjetivo vayan juntos.",
"vas_a_ver": ["Concordar", "Singular con singular", "Plural con plural"],
"secciones": [
 S(1, "Concordar", [
  D("Concordar", "Que el sustantivo y el adjetivo <b>vayan juntos</b>: los dos en singular o los dos en plural."),
  IMG("Juntos", "Los dos cambian.", FG.tiras(["EL PATO BLANCO", "LOS PATOS BLANCOS"], numeros=False, cols=1)),
 ]),
 S(1, "Más ejemplos", [
  P("LA FLOR ROJA → LAS FLORES <b>ROJAS</b>."),
  P("EL RATÓN GRIS → LOS RATONES <b>GRISES</b>."),
  IMG("Concuerdan", "Todo en plural.", FG.tiras(["LAS FLORES ROJAS", "LOS RATONES GRISES"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las frases. Las vas a usar en la carpeta."),
  IMG("¿Están bien?", "Revisá cada una.", FG.tiras(["1. LAS RANAS VERDE", "2. EL SOL AMARILLO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Concordar", "planteo": "LA CASA GRANDE → plural.", "pasos": ["CASA → CASAS.", "GRANDE → GRANDES.", "LAS CASAS GRANDES."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Pasá a plural.", "pasos": ["EL GATO NEGRO → LOS GATOS ___ ."]},
"ejemplo_solo": {"titulo": "Describí", "planteo": "Escribí dos animales con su adjetivo en plural."},
"tip": {"titulo": "Los dos juntos", "texto": "Si uno cambia, cambia el otro."},
"ojo": ["LAS RANAS VERDE está mal.", "Va LAS RANAS VERDES."],
"resumen": [{"titulo": "Concordar", "texto": "Ir juntos."}, {"titulo": "Singular", "texto": "EL PATO BLANCO."}, {"titulo": "Plural", "texto": "LOS PATOS BLANCOS."}],
"glosario": [{"palabra": "Concordar", "significado": "Que dos palabras vayan de acuerdo."}, {"palabra": "Adjetivo", "significado": "Dice cómo es algo."}],
"carpeta": ["¿Qué frase del dibujo está mal?", "Corregí la frase 1.", "Tomi escribió LOS PERROS GRANDE. ¿Está bien?"],
"carpeta_nivel": ["analizar", "error", "error"],
"respuestas_carpeta": [["1", "LA 1", "la 1", "La 1"] + low("LAS RANAS VERDE"), low("LAS RANAS VERDES"), NO],
"soluciones": {"incompleto": "NEGROS.", "solo": "Por ejemplo: LOS PATOS BLANCOS.", "carpeta": ["La 1.", "LAS RANAS VERDES.", "No: LOS PERROS GRANDES."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a corregir oraciones con singular y plural.",
"vas_a_ver": ["Buscar el error", "Corregir", "Revisar todo"],
"secciones": [
 S(1, "El cuaderno de Tomi", [
  P("Tomi escribió oraciones con errores. Sofi lo ayuda."),
  IMG("Antes y después", "Corregimos el plural.", FG.tiras(["LOS GATO DUERMEN. → LOS GATOS DUERMEN.", "LA FLORES ROJAS. → LAS FLORES ROJAS."], numeros=False, cols=1)),
 ]),
 S(1, "Cómo revisar", [
  P("1. ¿Es uno o varios? 2. ¿Todas las palabras dicen lo mismo?"),
  IMG("Bien escrito", "Todo de acuerdo.", FG.tiras(["LOS PÁJAROS CANTAN.", "EL PÁJARO CANTA."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Leé las oraciones. Las vas a usar en la carpeta."),
  IMG("Para corregir", "Buscá el error.", FG.tiras(["1. LAS NUBE BLANCAS.", "2. EL NIDOS ES DE BARRO."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Corregir", "planteo": "LOS LORO HABLAN.", "pasos": ["Son varios: plural.", "LORO tiene que ser LOROS.", "LOS LOROS HABLAN."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Corregí: LA RANAS SALTAN.", "pasos": ["___ RANAS SALTAN."]},
"ejemplo_solo": {"titulo": "Revisá", "planteo": "Revisá una página de tu cuaderno buscando plurales."},
"tip": {"titulo": "Todas de acuerdo", "texto": "Todas las palabras tienen que decir uno o varios."},
"ojo": ["LOS va con plural.", "Revisá también el adjetivo."],
"resumen": [{"titulo": "Buscar", "texto": "¿Uno o varios?"}, {"titulo": "Corregir", "texto": "Todas de acuerdo."}, {"titulo": "Revisar", "texto": "El adjetivo también."}],
"glosario": [{"palabra": "Corregir", "significado": "Arreglar un error."}, {"palabra": "Revisar", "significado": "Mirar de nuevo."}],
"carpeta": ["Corregí la oración 1.", "Corregí la oración 2 (es un solo nido).", "Tomi dice que LOS PÁJAROS CANTAN está mal. ¿Tiene razón?"],
"carpeta_nivel": ["error", "error", "analizar"],
"respuestas_carpeta": [low("LAS NUBES BLANCAS") + ["Las nubes blancas.", "LAS NUBES BLANCAS."], low("EL NIDO ES DE BARRO") + ["El nido es de barro.", "EL NIDO ES DE BARRO."], NO],
"soluciones": {"incompleto": "LAS.", "solo": "Los plurales que encuentres.", "carpeta": ["LAS NUBES BLANCAS.", "EL NIDO ES DE BARRO.", "No: está bien."]},
}

ACT = {
"1": [MC("¿CUÁL ESTÁ EN PLURAL?", ["LOS PATOS", "EL PATO"], "LOS PATOS", "NOMBRA VARIOS.", n="aplicar"),
      TF("LA RANA ES SINGULAR.", "VERDADERO", "ES UNA SOLA.", n="aplicar")],
"2": [UNI("UNÍ CADA PALABRA CON SU PLURAL.", [("CASA", "CASAS"), ("FLOR", "FLORES"), ("PAN", "PANES")], "S O ES.", n="analizar"),
      SA("ESCRIBÍ EL PLURAL DE RATÓN.", low("RATONES") + low("LOS RATONES"), "RATONES.", n="aplicar")],
"3": [MC("¿CUÁL ESTÁ BIEN?", ["LAS FLORES ROJAS", "LAS FLORES ROJA"], "LAS FLORES ROJAS", "LAS DOS EN PLURAL.", n="analizar"),
      SA("PASÁ A PLURAL: EL PATO BLANCO", low("LOS PATOS BLANCOS"), "LOS PATOS BLANCOS.", n="aplicar")],
"4": [SA("CORREGÍ: LOS GATO DUERMEN", low("LOS GATOS DUERMEN") + ["Los gatos duermen.", "LOS GATOS DUERMEN."], "LOS GATOS DUERMEN.", n="error"),
      TF("EL NIDOS ES DE BARRO ESTÁ BIEN ESCRITO.", "FALSO", "VA EL NIDO.", n="error")],
"5": [MC("RELÁMPAGO. VARIOS ES…", ["PLURAL", "SINGULAR"], "PLURAL", "MÁS DE UNO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. PLURAL DE SOL", ["SOLES", "SOLS"], "SOLES", "CONSONANTE: ES.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. PLURAL DE MESA", ["MESAS", "MESAES"], "MESAS", "VOCAL: S.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA VA CON…", ["UNA", "VARIAS"], "UNA", "LA ES SINGULAR.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿CUÁL ESTÁ EN SINGULAR?", ["EL NIDO", "LOS NIDOS"], "EL NIDO", "ES UNO SOLO.", n="aplicar")],
 [1, TF("LOS PATOS NOMBRA UNO SOLO.", "FALSO", "NOMBRA VARIOS.", n="error")],
 [1, SA("¿CÓMO SE DICE EL PLURAL DE EL GATO?", low("LOS GATOS"), "LOS GATOS.", n="aplicar")],
 [2, MC("PLURAL DE FLOR", ["FLORES", "FLORS"], "FLORES", "TERMINA EN CONSONANTE: ES.", n="aplicar")],
 [2, SA("ESCRIBÍ EL PLURAL DE CASA.", low("CASAS") + low("LAS CASAS"), "CASAS.", n="aplicar")],
 [2, UNI("UNÍ CADA PALABRA CON SU PLURAL.", [("LORO", "LOROS"), ("SOL", "SOLES"), ("NIDO", "NIDOS")], "S O ES.", n="analizar")],
 [3, MC("¿CUÁL CONCUERDA?", ["LOS RATONES GRISES", "LOS RATONES GRIS"], "LOS RATONES GRISES", "LAS DOS EN PLURAL.", n="analizar")],
 [3, SA("PASÁ A PLURAL: LA CASA GRANDE", low("LAS CASAS GRANDES"), "LAS CASAS GRANDES.", n="aplicar")],
 [3, TF("LAS RANAS VERDE ESTÁ BIEN ESCRITO.", "FALSO", "VA LAS RANAS VERDES.", n="error")],
 [4, SA("CORREGÍ: LA FLORES ROJAS", low("LAS FLORES ROJAS") + ["Las flores rojas.", "LAS FLORES ROJAS."], "LAS FLORES ROJAS.", n="error")],
 [4, MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["LOS PÁJAROS CANTAN", "LOS PÁJARO CANTAN", "EL PÁJAROS CANTA"], "LOS PÁJAROS CANTAN", "TODO EN PLURAL.", n="analizar")],
 [4, SA("CORREGÍ: LOS LORO HABLAN", low("LOS LOROS HABLAN") + ["Los loros hablan.", "LOS LOROS HABLAN."], "LOS LOROS HABLAN.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 14, "estilo": "primeros",
     "practica": "Práctica general: singular y plural", "examen_titulo": "Nivel jefe: singular y plural",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-14.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
