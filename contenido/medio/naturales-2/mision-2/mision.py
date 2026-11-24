# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 2 · Las crías de los animales. Genera mision-2.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador con su lupa (hoy visita una granja y un parque).
Niveles: 1 nacen de huevos o de la panza · 2 crías que se parecen (o no) a sus padres · 3 quién cuida a las crías · 4 animales que viven en grupo."""
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
"objetivo": "Vas a saber cómo nacen los animales.",
"vas_a_ver": ["De un huevo", "De la panza de la mamá", "Ejemplos"],
"secciones": [
 S(1, "De un huevo", [
  P("Tomi visita la granja. La gallina puso <b>huevos</b>."),
  D("Nacen de huevos", "La cría crece <b>adentro de un huevo</b> y después sale."),
  IMG("Nacen de huevos", "Gallina, pato y tortuga.", FG.objetos([("huevo", "HUEVO"), ("pato", "PATO"), ("tortuga", "TORTUGA")])),
 ]),
 S(1, "De la panza", [
  D("Nacen de la panza", "La cría crece <b>adentro de la mamá</b> y después nace."),
  P("Así nacen el perro, el gato, la vaca y las personas."),
  IMG("Nacen de la panza", "Crecen adentro de la mamá.", FG.nombres(["PERRO", "GATO", "VACA", "CABALLO"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("¿Huevo o panza?", "Pensá en cada uno.", FG.nombres(["GALLINA", "OVEJA", "TORTUGA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "¿Cómo nace?", "planteo": "¿Cómo nace un pollito?", "pasos": ["La gallina pone un huevo.", "El pollito crece adentro.", "Rompe el huevo y sale."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El gatito…", "pasos": ["El gatito nace de la ___ de la mamá."]},
"ejemplo_solo": {"titulo": "Investigá", "planteo": "Elegí un animal y averiguá con un adulto cómo nace."},
"tip": {"titulo": "Dos formas", "texto": "Huevo o panza: así nacen los animales."},
"ojo": ["Los peces y las aves nacen de huevos.", "El perro nace de la panza."],
"resumen": [{"titulo": "Huevo", "texto": "Gallina, pato, tortuga."}, {"titulo": "Panza", "texto": "Perro, gato, vaca."}, {"titulo": "Cría", "texto": "El animal bebé."}],
"glosario": [{"palabra": "Cría", "significado": "Animal recién nacido."}, {"palabra": "Granja", "significado": "Lugar del campo con animales."}],
"carpeta": ["¿Cómo nace la GALLINA: de huevo o de la panza?", "¿Cómo nace la OVEJA?", "Tomi dice que la tortuga nace de la panza. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("DE HUEVO") + low("HUEVO") + low("DE UN HUEVO"), low("DE LA PANZA") + low("PANZA") + low("DE LA PANZA DE LA MAMÁ"), NO],
"soluciones": {"incompleto": "PANZA.", "solo": "Cómo nace tu animal.", "carpeta": ["De huevo.", "De la panza.", "No: nace de un huevo."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver si las crías se parecen a sus padres.",
"vas_a_ver": ["Crías parecidas", "Crías que cambian", "La rana y la mariposa"],
"secciones": [
 S(1, "Parecidas", [
  P("El <b>perrito</b> se parece al perro. El <b>potrillo</b> se parece al caballo."),
  IMG("Crías parecidas", "Son como sus padres, pero chiquitas.", FG.tiras(["PERRITO → PERRO", "POTRILLO → CABALLO", "TERNERO → VACA"], numeros=False, cols=1)),
 ]),
 S(1, "Crías que cambian", [
  P("El <b>renacuajo</b> no se parece a la rana. ¡Va <b>cambiando</b>!"),
  P("La <b>oruga</b> se convierte en <b>mariposa</b>."),
  IMG("Del renacuajo a la rana", "Cambia mucho.", FG.objetos([("renacuajo", "RENACUAJO"), ("rana", "RANA")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las crías. Las vas a usar en la carpeta."),
  IMG("¿Se parece?", "Pensá en sus padres.", FG.nombres(["GATITO", "ORUGA", "PATITO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Cambiar", "planteo": "¿Cómo cambia el renacuajo?", "pasos": ["Primero tiene cola.", "Le salen patas.", "Se convierte en rana."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La oruga…", "pasos": ["La oruga se convierte en ___ ."]},
"ejemplo_solo": {"titulo": "Dibujá", "planteo": "Dibujá un animal y su cría."},
"tip": {"titulo": "Mirá bien", "texto": "Algunas crías cambian mucho al crecer."},
"ojo": ["El renacuajo no es un pez.", "La oruga no es un gusano."],
"resumen": [{"titulo": "Parecidas", "texto": "Perrito, potrillo."}, {"titulo": "Cambian", "texto": "Renacuajo, oruga."}, {"titulo": "Crecen", "texto": "Y se hacen adultos."}],
"glosario": [{"palabra": "Potrillo", "significado": "Cría del caballo."}, {"palabra": "Oruga", "significado": "Cría de la mariposa."}],
"carpeta": ["¿Qué cría del dibujo NO se parece a su mamá?", "¿En qué se convierte la oruga?", "Tomi dice que el renacuajo es un pez. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "recordar", "error"],
"respuestas_carpeta": [low("ORUGA") + low("LA ORUGA"), low("MARIPOSA") + low("EN MARIPOSA") + low("EN UNA MARIPOSA"), NO],
"soluciones": {"incompleto": "MARIPOSA.", "solo": "Tu dibujo.", "carpeta": ["La oruga.", "En mariposa.", "No: es la cría de la rana."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a saber quién cuida a las crías.",
"vas_a_ver": ["Mamás y papás que cuidan", "Crías que se arreglan solas", "Cómo las cuidan"],
"secciones": [
 S(1, "Las cuidan", [
  P("La <b>vaca</b> le da leche al ternero. La <b>gallina</b> abriga a sus pollitos."),
  P("El hornero <b>papá y mamá</b> llevan comida al nido."),
  IMG("Cuidan a sus crías", "Las alimentan y abrigan.", FG.objetos([("hornero", "HORNERO"), ("nido", "SU NIDO")])),
 ]),
 S(1, "Se arreglan solas", [
  P("La <b>tortuga</b> deja sus huevos en la arena y se va."),
  P("Las tortuguitas <b>se arreglan solas</b> desde que nacen."),
  IMG("Solas desde chiquitas", "Nadie las cuida.", FG.objetos([("tortuga", "TORTUGUITA")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Cómo cuidan?", "Pensá en cada mamá.", FG.tiras(["VACA: DA LECHE", "GALLINA: ABRIGA", "TORTUGA: SE VA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Cuidar", "planteo": "¿Cómo cuida la vaca al ternero?", "pasos": ["Le da leche.", "Lo lame.", "Lo acompaña."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La gallina…", "pasos": ["La gallina ___ a sus pollitos."]},
"ejemplo_solo": {"titulo": "Observá", "planteo": "Mirá una mascota o un pájaro con crías. ¿Cómo las cuida?"},
"tip": {"titulo": "Cada animal", "texto": "Cada animal cuida distinto a sus crías."},
"ojo": ["No todas las crías tienen quien las cuide.", "Algunos papás también cuidan."],
"resumen": [{"titulo": "Cuidan", "texto": "Vaca, gallina, hornero."}, {"titulo": "Solas", "texto": "Tortuga."}, {"titulo": "Cómo", "texto": "Dar comida, abrigar."}],
"glosario": [{"palabra": "Abrigar", "significado": "Dar calor."}, {"palabra": "Ternero", "significado": "Cría de la vaca."}],
"carpeta": ["¿Qué hace la vaca por su cría?", "¿Qué mamá del dibujo se va y no cuida?", "Tomi dice que todas las crías tienen quien las cuide. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("DA LECHE") + low("LE DA LECHE"), low("TORTUGA") + low("LA TORTUGA"), NO],
"soluciones": {"incompleto": "ABRIGA.", "solo": "Lo que observaste.", "carpeta": ["Le da leche.", "La tortuga.", "No: la tortuga no cuida."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer animales que viven en grupo.",
"vas_a_ver": ["Vivir en grupo", "Ejemplos", "Para qué sirve"],
"secciones": [
 S(1, "En grupo", [
  P("Algunos animales viven <b>juntos</b>: se ayudan y se cuidan."),
  IMG("Grupos de animales", "Cada grupo tiene su nombre.", FG.tiras(["HORMIGAS: HORMIGUERO", "ABEJAS: COLMENA", "OVEJAS: REBAÑO", "PECES: CARDUMEN"], numeros=False)),
 ]),
 S(1, "Para qué sirve", [
  P("En grupo se <b>defienden</b> mejor y <b>buscan comida</b> juntos."),
  P("Las hormigas llevan comida al hormiguero entre todas."),
  IMG("Las hormigas", "Trabajan en equipo.", FG.tiras(["BUSCAN COMIDA", "LA LLEVAN JUNTAS", "LA GUARDAN"], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los nombres. Los vas a usar en la carpeta."),
  IMG("¿Qué animales?", "Pensá en cada grupo.", FG.nombres(["COLMENA", "REBAÑO", "CARDUMEN"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Grupo", "planteo": "¿Dónde viven las abejas?", "pasos": ["Viven juntas.", "En una colmena.", "Hacen miel."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las ovejas…", "pasos": ["Las ovejas viven en un ___ ."]},
"ejemplo_solo": {"titulo": "Observá", "planteo": "Mirá un hormiguero con un adulto. ¿Qué hacen las hormigas?"},
"tip": {"titulo": "Juntos es mejor", "texto": "En grupo se cuidan y se ayudan."},
"ojo": ["Mirá las hormigas, pero no las molestes.", "Las abejas pueden picar: de lejos."],
"resumen": [{"titulo": "Grupo", "texto": "Viven juntos."}, {"titulo": "Ejemplos", "texto": "Hormigas, abejas, ovejas."}, {"titulo": "Sirve", "texto": "Para cuidarse y comer."}],
"glosario": [{"palabra": "Colmena", "significado": "Casa de las abejas."}, {"palabra": "Cardumen", "significado": "Grupo de peces."}],
"carpeta": ["¿Qué animales viven en una COLMENA?", "¿Qué animales andan en CARDUMEN?", "Tomi dice que vivir en grupo no sirve para nada. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ABEJAS") + low("LAS ABEJAS"), low("PECES") + low("LOS PECES"), NO],
"soluciones": {"incompleto": "REBAÑO.", "solo": "Lo que hacen las hormigas.", "carpeta": ["Las abejas.", "Los peces.", "No: se cuidan y buscan comida juntos."]},
}

ACT = {
"1": [UNI("UNÍ CADA ANIMAL CON CÓMO NACE.", [("GALLINA", "DE HUEVO"), ("PERRO", "DE LA PANZA"), ("TORTUGA", "DE UN HUEVITO")], "HUEVO O PANZA.", n="analizar"),
      MC("¿QUÉ ANIMAL NACE DE UN HUEVO?", ["EL PATO", "EL GATO", "LA VACA"], "EL PATO", "LOS PATOS NACEN DE HUEVOS.", n="aplicar")],
"2": [MC("¿QUÉ CRÍA CAMBIA MUCHO AL CRECER?", ["EL RENACUAJO", "EL PERRITO"], "EL RENACUAJO", "SE CONVIERTE EN RANA.", n="analizar"),
      SA("LA ORUGA SE CONVIERTE EN…", low("MARIPOSA") + low("UNA MARIPOSA"), "MARIPOSA.", n="recordar")],
"3": [TF("LA TORTUGA CUIDA A SUS CRÍAS.", "FALSO", "DEJA LOS HUEVOS Y SE VA.", n="aplicar"),
      MC("¿QUÉ HACE LA VACA POR SU TERNERO?", ["LE DA LECHE", "LO DEJA SOLO"], "LE DA LECHE", "LO ALIMENTA.", n="aplicar")],
"4": [UNI("UNÍ CADA ANIMAL CON SU GRUPO.", [("ABEJAS", "COLMENA"), ("OVEJAS", "REBAÑO"), ("PECES", "CARDUMEN")], "CADA GRUPO TIENE NOMBRE.", n="analizar"),
      MC("¿PARA QUÉ VIVEN EN GRUPO?", ["PARA CUIDARSE Y COMER", "PARA PELEAR"], "PARA CUIDARSE Y COMER", "SE AYUDAN.", n="recordar")],
"5": [MC("RELÁMPAGO. EL POLLITO NACE DE…", ["UN HUEVO", "LA PANZA"], "UN HUEVO", "LA GALLINA PONE HUEVOS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA CRÍA DEL CABALLO ES…", ["EL POTRILLO", "EL TERNERO"], "EL POTRILLO", "POTRILLO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL RENACUAJO SE CONVIERTE EN…", ["RANA", "PEZ"], "RANA", "CAMBIA MUCHO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LAS ABEJAS VIVEN EN…", ["COLMENA", "NIDO"], "COLMENA", "TODAS JUNTAS.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿CÓMO NACE EL GATO?", ["DE LA PANZA DE LA MAMÁ", "DE UN HUEVO"], "DE LA PANZA DE LA MAMÁ", "CRECE ADENTRO DE LA MAMÁ.", n="aplicar")],
 [1, TF("LAS AVES NACEN DE HUEVOS.", "VERDADERO", "COMO EL POLLITO.", n="recordar")],
 [1, SA("ESCRIBÍ UN ANIMAL QUE NACE DE UN HUEVO.", low("GALLINA") + low("POLLITO") + low("PATO") + low("TORTUGA") + low("PEZ") + low("HORNERO") + low("PÁJARO") + low("pajaro") + low("COCODRILO") + low("SERPIENTE") + low("RANA"), "POR EJEMPLO: PATO.", n="aplicar")],
 [2, MC("¿QUÉ CRÍA SE PARECE A SUS PADRES?", ["EL PERRITO", "LA ORUGA", "EL RENACUAJO"], "EL PERRITO", "ES COMO UN PERRO CHIQUITO.", n="analizar")],
 [2, TF("EL RENACUAJO ES UN PEZ.", "FALSO", "ES LA CRÍA DE LA RANA.", n="error")],
 [2, SA("¿CÓMO SE LLAMA LA CRÍA DE LA VACA?", low("TERNERO") + low("EL TERNERO") + low("TERNERITO"), "TERNERO.", n="recordar")],
 [3, MC("¿QUÉ HACE LA GALLINA CON SUS POLLITOS?", ["LOS ABRIGA", "SE VA"], "LOS ABRIGA", "LES DA CALOR.", n="aplicar")],
 [3, TF("TODAS LAS CRÍAS TIENEN QUIEN LAS CUIDE.", "FALSO", "LAS TORTUGUITAS SE ARREGLAN SOLAS.", n="error")],
 [3, SA("¿QUIÉN LLEVA COMIDA AL NIDO DEL HORNERO?", low("PAPÁ Y MAMÁ") + low("papa y mama") + low("LOS PADRES") + low("EL PAPÁ Y LA MAMÁ") + low("la mamá y el papá") + low("MAMÁ Y PAPÁ") + low("mama y papa"), "PAPÁ Y MAMÁ.", n="recordar")],
 [4, UNI("UNÍ CADA GRUPO CON SUS ANIMALES.", [("HORMIGUERO", "HORMIGAS"), ("REBAÑO", "OVEJAS"), ("CARDUMEN", "PECES")], "CADA GRUPO TIENE NOMBRE.", n="analizar")],
 [4, MC("¿QUÉ HACEN LAS HORMIGAS JUNTAS?", ["LLEVAN COMIDA", "DUERMEN TODO EL DÍA"], "LLEVAN COMIDA", "TRABAJAN EN EQUIPO.", n="aplicar")],
 [4, TF("VIVIR EN GRUPO AYUDA A DEFENDERSE.", "VERDADERO", "JUNTOS SE CUIDAN.", n="recordar")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: las crías de los animales", "examen_titulo": "Nivel jefe: las crías de los animales",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
