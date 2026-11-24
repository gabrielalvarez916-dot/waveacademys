# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 4 · Cuerpos para cada ambiente. Genera mision-4.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador con su lupa (hoy viaja por la Argentina).
Niveles: 1 patas, picos y pelajes · 2 plantas de ambientes secos y húmedos · 3 cuerpos para moverse · 4 comparo ambientes argentinos."""
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
"objetivo": "Vas a ver cómo el cuerpo ayuda a cada animal.",
"vas_a_ver": ["Patas", "Picos", "Pelajes"],
"secciones": [
 S(1, "Patas y picos", [
  P("El <b>pato</b> tiene patas con <b>piel entre los dedos</b>: le sirven para nadar."),
  P("El <b>hornero</b> tiene un pico fino para comer <b>bichitos</b>."),
  IMG("Cuerpos que sirven", "Cada parte tiene una función.", FG.objetos([("pato", "PATAS PARA NADAR"), ("hornero", "PICO FINO")])),
 ]),
 S(1, "Pelajes", [
  D("Pelaje", "El <b>pelo</b> que cubre a un animal. Lo protege del frío."),
  P("El <b>guanaco</b> vive en lugares fríos y tiene <b>lana gruesa</b>."),
  IMG("Para cada lugar", "El cuerpo ayuda a vivir.", FG.tiras(["PATO: PATAS PARA NADAR", "HORNERO: PICO PARA BICHITOS", "GUANACO: LANA PARA EL FRÍO"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las partes. Las vas a usar en la carpeta."),
  IMG("¿Para qué sirve?", "Pensá en cada una.", FG.nombres(["LANA GRUESA", "PATAS PARA NADAR", "PICO FUERTE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El pato", "planteo": "¿Por qué el pato nada bien?", "pasos": ["Mira sus patas.", "Tienen piel entre los dedos.", "Le sirven como remos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El guanaco vive en el frío.", "pasos": ["Tiene ___ gruesa."]},
"ejemplo_solo": {"titulo": "Observá", "planteo": "Mirá un pájaro de tu barrio. ¿Cómo es su pico?"},
"tip": {"titulo": "Preguntá ¿para qué?", "texto": "Cada parte del cuerpo sirve para algo."},
"ojo": ["El pato no nada con las alas.", "El pelaje grueso abriga."],
"resumen": [{"titulo": "Patas", "texto": "Para nadar o correr."}, {"titulo": "Picos", "texto": "Para comer."}, {"titulo": "Pelaje", "texto": "Para el frío."}],
"glosario": [{"palabra": "Pelaje", "significado": "Pelo que cubre a un animal."}, {"palabra": "Guanaco", "significado": "Animal de lugares fríos, con lana."}],
"carpeta": ["¿Para qué sirve la LANA GRUESA?", "¿Para qué sirven las PATAS del pato?", "Tomi dice que el pato nada con las alas. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PARA EL FRÍO") + low("para el frio") + low("ABRIGAR") + low("PARA ABRIGAR") + low("PARA NO TENER FRÍO") + low("para no tener frio"), low("PARA NADAR") + low("NADAR"), NO],
"soluciones": {"incompleto": "LANA.", "solo": "Cómo es el pico.", "carpeta": ["Para el frío.", "Para nadar.", "No: nada con las patas."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer plantas de lugares secos y húmedos.",
"vas_a_ver": ["Plantas del desierto", "Plantas del agua", "Cómo se cuidan"],
"secciones": [
 S(1, "Lugares secos", [
  P("En el <b>desierto</b> casi no llueve."),
  P("El <b>cactus</b> guarda agua en su tallo grueso y tiene <b>espinas</b>."),
  IMG("El cactus", "Guarda agua adentro.", FG.tiras(["TALLO GRUESO: GUARDA AGUA", "ESPINAS: NO PIERDE AGUA"], numeros=False, cols=1)),
 ]),
 S(1, "Lugares húmedos", [
  P("En la <b>selva</b> llueve mucho. Las plantas tienen <b>hojas grandes</b>."),
  P("El <b>camalote</b> vive en el río y <b>flota</b>."),
  IMG("Plantas de cada lugar", "Seco o húmedo.", FG.nombres(["CACTUS", "HELECHO", "CAMALOTE"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Seco o húmedo?", "Pensá en cada planta.", FG.tiras(["1. TIENE ESPINAS Y TALLO GRUESO", "2. FLOTA EN EL RÍO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El cactus", "planteo": "¿Cómo vive sin lluvia?", "pasos": ["Guarda agua en el tallo.", "Tiene espinas.", "Aguanta mucho tiempo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El camalote…", "pasos": ["El camalote ___ en el río."]},
"ejemplo_solo": {"titulo": "Observá", "planteo": "Mirá una planta de tu casa. ¿Necesita mucha agua o poca?"},
"tip": {"titulo": "Mirá el lugar", "texto": "Cada planta es como el lugar donde vive."},
"ojo": ["El cactus no necesita mucha agua.", "Las espinas son hojas especiales."],
"resumen": [{"titulo": "Seco", "texto": "Cactus: guarda agua."}, {"titulo": "Húmedo", "texto": "Hojas grandes."}, {"titulo": "Agua", "texto": "Camalote: flota."}],
"glosario": [{"palabra": "Desierto", "significado": "Lugar donde casi no llueve."}, {"palabra": "Camalote", "significado": "Planta que flota en los ríos."}],
"carpeta": ["¿Qué planta es la tarjeta 1?", "¿Qué planta es la tarjeta 2?", "Tomi dice que el cactus necesita mucha agua. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("CACTUS") + low("EL CACTUS"), low("CAMALOTE") + low("EL CAMALOTE"), NO],
"soluciones": {"incompleto": "FLOTA.", "solo": "Lo que necesita tu planta.", "carpeta": ["El cactus.", "El camalote.", "No: guarda agua y necesita poca."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver cómo se mueven los animales.",
"vas_a_ver": ["Nadar, volar y correr", "Saltar y reptar", "Partes del cuerpo"],
"secciones": [
 S(1, "Cómo se mueven", [
  P("Los peces <b>nadan</b> con aletas. Los pájaros <b>vuelan</b> con alas."),
  P("El ñandú <b>corre</b> con patas largas. La rana <b>salta</b>. La víbora <b>repta</b>."),
  IMG("Cómo se mueven", "Cada uno con su cuerpo.", FG.tiras(["PEZ: NADA CON ALETAS", "PÁJARO: VUELA CON ALAS", "ÑANDÚ: CORRE CON PATAS", "VÍBORA: REPTA SIN PATAS"], numeros=False)),
 ]),
 S(1, "La rana", [
  P("La rana tiene patas de atrás <b>largas y fuertes</b>: ¡salta lejos!"),
  IMG("La rana", "Patas para saltar.", FG.objetos([("rana", "SALTA")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("¿Cómo se mueve?", "Pensá en su cuerpo.", FG.nombres(["PEZ", "VÍBORA", "CANGURO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El pez", "planteo": "¿Cómo se mueve el pez?", "pasos": ["Vive en el agua.", "Tiene aletas.", "Nada."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La víbora no tiene patas.", "pasos": ["La víbora ___ ."]},
"ejemplo_solo": {"titulo": "Imitá", "planteo": "Imitá cómo se mueven tres animales."},
"tip": {"titulo": "Mirá el cuerpo", "texto": "Las partes del cuerpo dicen cómo se mueve."},
"ojo": ["El ñandú es un ave, pero no vuela: corre.", "La víbora no tiene patas."],
"resumen": [{"titulo": "Nadar", "texto": "Aletas."}, {"titulo": "Volar", "texto": "Alas."}, {"titulo": "Correr y saltar", "texto": "Patas."}],
"glosario": [{"palabra": "Reptar", "significado": "Moverse arrastrando el cuerpo."}, {"palabra": "Aleta", "significado": "Parte del pez para nadar."}],
"carpeta": ["¿Cómo se mueve el PEZ?", "¿Cómo se mueve la VÍBORA?", "Tomi dice que el ñandú vuela. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("NADA") + low("NADANDO"), low("REPTA") + low("REPTANDO") + low("SE ARRASTRA") + low("ARRASTRÁNDOSE") + low("arrastrandose"), NO],
"soluciones": {"incompleto": "REPTA.", "solo": "Tus imitaciones.", "carpeta": ["Nada.", "Repta.", "No: corre."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a comparar ambientes de la Argentina.",
"vas_a_ver": ["La selva", "El mar", "La montaña"],
"secciones": [
 S(1, "Ambientes", [
  D("Ambiente", "El <b>lugar</b> donde viven plantas y animales."),
  P("La Argentina tiene muchos ambientes distintos."),
  IMG("Ambientes argentinos", "Cada uno con sus seres vivos.", FG.tiras(["SELVA: YAGUARETÉ, TUCÁN", "MAR: PINGÜINO, LOBO MARINO", "MONTAÑA: GUANACO, CÓNDOR", "LAGUNA: PATO, RANA"], numeros=False)),
 ]),
 S(1, "Comparar", [
  P("En la <b>selva</b> hace calor y llueve mucho. En la <b>montaña</b> hace frío."),
  IMG("El yaguareté", "Vive en la selva.", FG.objetos([("yaguarete", "SELVA")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("¿Dónde vive?", "Pensá en su ambiente.", FG.nombres(["PINGÜINO", "TUCÁN", "CÓNDOR"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El pingüino", "planteo": "¿Dónde vive?", "pasos": ["Nada muy bien.", "Come peces.", "Vive en el mar."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El guanaco…", "pasos": ["El guanaco vive en la ___ ."]},
"ejemplo_solo": {"titulo": "Tu ambiente", "planteo": "¿Cómo es el lugar donde vivís? Dibujá un animal de ahí."},
"tip": {"titulo": "Calor o frío", "texto": "Pensá cómo es el clima de cada lugar."},
"ojo": ["El pingüino no vive en la selva.", "El yaguareté no vive en el mar."],
"resumen": [{"titulo": "Selva", "texto": "Calor y lluvia."}, {"titulo": "Mar", "texto": "Agua salada."}, {"titulo": "Montaña", "texto": "Frío."}],
"glosario": [{"palabra": "Ambiente", "significado": "Lugar donde viven los seres vivos."}, {"palabra": "Cóndor", "significado": "Ave grande de la montaña."}],
"carpeta": ["¿Dónde vive el PINGÜINO?", "¿Dónde vive el TUCÁN?", "Tomi dice que el cóndor vive en el mar. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("EN EL MAR") + low("MAR") + low("EL MAR"), low("EN LA SELVA") + low("SELVA") + low("LA SELVA"), NO],
"soluciones": {"incompleto": "MONTAÑA.", "solo": "Tu dibujo.", "carpeta": ["En el mar.", "En la selva.", "No: vive en la montaña."]},
}

ACT = {
"1": [UNI("UNÍ CADA PARTE CON PARA QUÉ SIRVE.", [("PATAS DEL PATO", "NADAR"), ("LANA DEL GUANACO", "ABRIGAR"), ("PICO DEL HORNERO", "COMER BICHITOS")], "CADA PARTE SIRVE PARA ALGO.", n="analizar"),
      TF("EL PELAJE GRUESO PROTEGE DEL FRÍO.", "VERDADERO", "COMO LA LANA DEL GUANACO.", n="recordar")],
"2": [MC("¿QUÉ PLANTA GUARDA AGUA EN SU TALLO?", ["EL CACTUS", "EL CAMALOTE"], "EL CACTUS", "VIVE DONDE CASI NO LLUEVE.", n="aplicar"),
      SA("¿QUÉ PLANTA FLOTA EN EL RÍO?", low("CAMALOTE") + low("EL CAMALOTE"), "EL CAMALOTE.", n="recordar")],
"3": [UNI("UNÍ CADA ANIMAL CON CÓMO SE MUEVE.", [("PEZ", "NADA"), ("PÁJARO", "VUELA"), ("VÍBORA", "REPTA")], "MIRÁ SU CUERPO.", n="analizar"),
      MC("¿CÓMO SE MUEVE EL ÑANDÚ?", ["CORRE", "VUELA", "NADA"], "CORRE", "TIENE PATAS LARGAS.", n="aplicar")],
"4": [UNI("UNÍ CADA ANIMAL CON SU AMBIENTE.", [("PINGÜINO", "MAR"), ("YAGUARETÉ", "SELVA"), ("GUANACO", "MONTAÑA")], "CADA UNO EN SU LUGAR.", n="analizar"),
      TF("EN LA SELVA HACE MUCHO FRÍO.", "FALSO", "HACE CALOR Y LLUEVE MUCHO.", n="error")],
"5": [MC("RELÁMPAGO. EL PEZ NADA CON…", ["ALETAS", "ALAS"], "ALETAS", "ALETAS PARA NADAR.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL CACTUS VIVE EN…", ["LUGARES SECOS", "EL RÍO"], "LUGARES SECOS", "GUARDA AGUA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL PINGÜINO VIVE EN…", ["EL MAR", "LA SELVA"], "EL MAR", "COME PECES.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA VÍBORA…", ["REPTA", "SALTA"], "REPTA", "NO TIENE PATAS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿PARA QUÉ LE SIRVEN AL PATO SUS PATAS?", ["PARA NADAR", "PARA VOLAR"], "PARA NADAR", "TIENEN PIEL ENTRE LOS DEDOS.", n="aplicar")],
 [1, SA("¿QUÉ ANIMAL TIENE LANA GRUESA PARA EL FRÍO?", low("GUANACO") + low("EL GUANACO") + low("OVEJA") + low("LA OVEJA") + low("LLAMA") + low("VICUÑA"), "EL GUANACO.", n="recordar")],
 [1, TF("CADA PARTE DEL CUERPO DE UN ANIMAL SIRVE PARA ALGO.", "VERDADERO", "PATAS, PICOS, PELAJE…", n="recordar")],
 [2, MC("¿POR QUÉ EL CACTUS AGUANTA SIN LLUVIA?", ["GUARDA AGUA EN EL TALLO", "TIENE HOJAS GRANDES"], "GUARDA AGUA EN EL TALLO", "Y TIENE ESPINAS.", n="analizar")],
 [2, TF("EL CACTUS NECESITA MUCHA AGUA.", "FALSO", "NECESITA POCA.", n="error")],
 [2, MC("¿CÓMO SON LAS HOJAS EN LA SELVA?", ["GRANDES", "ESPINAS"], "GRANDES", "LLUEVE MUCHO.", n="aplicar")],
 [3, UNI("UNÍ CADA ANIMAL CON CÓMO SE MUEVE.", [("RANA", "SALTA"), ("ÑANDÚ", "CORRE"), ("PEZ", "NADA")], "MIRÁ SU CUERPO.", n="analizar")],
 [3, SA("¿CON QUÉ VUELAN LOS PÁJAROS?", low("ALAS") + low("CON LAS ALAS") + low("LAS ALAS") + low("CON ALAS"), "CON LAS ALAS.", n="recordar")],
 [3, TF("EL ÑANDÚ VUELA MUY ALTO.", "FALSO", "EL ÑANDÚ CORRE.", n="error")],
 [4, MC("¿DÓNDE VIVE EL CÓNDOR?", ["EN LA MONTAÑA", "EN EL MAR", "EN LA SELVA"], "EN LA MONTAÑA", "VUELA ENTRE LAS MONTAÑAS.", n="aplicar")],
 [4, SA("ESCRIBÍ UN ANIMAL DE LA SELVA.", low("YAGUARETÉ") + low("yaguarete") + low("TUCÁN") + low("tucan") + low("MONO") + low("LORO") + low("TAPIR") + low("COATÍ") + low("coati"), "POR EJEMPLO: TUCÁN.", n="aplicar")],
 [4, TF("UN AMBIENTE ES EL LUGAR DONDE VIVEN PLANTAS Y ANIMALES.", "VERDADERO", "COMO LA SELVA O EL MAR.", n="recordar")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: cuerpos para cada ambiente", "examen_titulo": "Nivel jefe: cuerpos para cada ambiente",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
