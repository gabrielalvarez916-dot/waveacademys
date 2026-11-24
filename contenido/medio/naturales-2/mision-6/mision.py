# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 6 · Empujar y tirar. Genera mision-6.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (hoy en el patio y la plaza).
Niveles: 1 empujar, tirar y mover · 2 rápido y despacio · 3 el rozamiento · 4 los imanes atraen."""
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
"objetivo": "Vas a ver cómo movemos las cosas.",
"vas_a_ver": ["Empujar", "Tirar", "La fuerza"],
"secciones": [
 S(1, "Empujar y tirar", [
  P("Tomi <b>empuja</b> un carrito: lo aleja de él."),
  P("Después <b>tira</b> de una soga: la acerca a él."),
  D("Fuerza", "Empujar o tirar. Con una fuerza, las cosas se <b>mueven</b>."),
  IMG("Empujar y tirar", "Dos formas de mover.", FG.tiras(["EMPUJAR: ALEJA", "TIRAR: ACERCA"], numeros=False, cols=1)),
 ]),
 S(1, "Ejemplos", [
  P("Empujamos una puerta, una hamaca, un changuito."),
  P("Tiramos de un cajón, de una soga, de un perro con correa."),
  IMG("¿Empujar o tirar?", "Ejemplos de todos los días.", FG.nombres(["PUERTA", "CAJÓN", "HAMACA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Qué hacés?", "Pensá en cada una.", FG.tiras(["1. ABRIR UN CAJÓN", "2. MOVER UNA HAMACA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La hamaca", "planteo": "¿Cómo muevo la hamaca?", "pasos": ["Me pongo atrás.", "La empujo.", "¡Se mueve!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para abrir un cajón…", "pasos": ["…lo ___ hacia mí."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá algo que se empuja y algo que se tira."},
"tip": {"titulo": "¿Se aleja o se acerca?", "texto": "Si se aleja, empujás. Si se acerca, tirás."},
"ojo": ["Sin fuerza, las cosas no se mueven solas.", "Empujar y tirar son fuerzas."],
"resumen": [{"titulo": "Empujar", "texto": "Aleja."}, {"titulo": "Tirar", "texto": "Acerca."}, {"titulo": "Fuerza", "texto": "Hace mover."}],
"glosario": [{"palabra": "Fuerza", "significado": "Empujar o tirar."}, {"palabra": "Changuito", "significado": "Carrito de compras."}],
"carpeta": ["En la tarjeta 1, ¿empujás o tirás?", "En la tarjeta 2, ¿empujás o tirás?", "Tomi dice que una pelota se mueve sola, sin fuerza. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("TIRO") + low("TIRAR") + low("TIRÁS") + low("tiras"), low("EMPUJO") + low("EMPUJAR") + low("EMPUJÁS") + low("empujas"), NO],
"soluciones": {"incompleto": "TIRO.", "solo": "Algo para empujar y algo para tirar.", "carpeta": ["Tiro.", "Empujo.", "No: necesita una fuerza."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver qué pasa con más o menos fuerza.",
"vas_a_ver": ["Fuerza suave", "Fuerza fuerte", "Rápido y despacio"],
"secciones": [
 S(1, "Suave y fuerte", [
  P("Tomi patea la pelota <b>suave</b>: va <b>despacio</b> y cerca."),
  P("La patea <b>fuerte</b>: va <b>rápido</b> y lejos."),
  IMG("Más fuerza, más lejos", "Comparamos.", FG.tiras(["PATADA SUAVE: DESPACIO Y CERCA", "PATADA FUERTE: RÁPIDO Y LEJOS"], numeros=False, cols=1)),
 ]),
 S(1, "Frenar", [
  P("Para <b>frenar</b> algo que se mueve, también hace falta fuerza."),
  P("El arquero frena la pelota con las manos."),
  IMG("Mover y frenar", "La fuerza hace las dos cosas.", FG.nombres(["MOVER", "FRENAR", "CAMBIAR DE LADO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Lejos o cerca?", "Pensá en la fuerza.", FG.tiras(["1. EMPUJO LA HAMACA FUERTE", "2. EMPUJO LA HAMACA SUAVE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La bolita", "planteo": "Empujo una bolita fuerte.", "pasos": ["Recibe mucha fuerza.", "Va rápido.", "Llega lejos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Con fuerza suave…", "pasos": ["…la pelota va ___ ."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "En el patio, tirá una pelota suave y fuerte. ¿Hasta dónde llega?"},
"tip": {"titulo": "Comparar", "texto": "Más fuerza: más rápido y más lejos."},
"ojo": ["Frenar también necesita fuerza.", "Jugá con cuidado, sin golpear a nadie."],
"resumen": [{"titulo": "Suave", "texto": "Despacio y cerca."}, {"titulo": "Fuerte", "texto": "Rápido y lejos."}, {"titulo": "Frenar", "texto": "También es fuerza."}],
"glosario": [{"palabra": "Rápido", "significado": "En poco tiempo."}, {"palabra": "Frenar", "significado": "Hacer que algo pare."}],
"carpeta": ["¿Con qué tarjeta la hamaca va más alto?", "¿Con cuál va más bajito?", "Tomi dice que con una patada suave la pelota llega más lejos. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [["1", "LA 1", "la 1", "La 1"] + low("FUERTE") + low("CON LA 1"), ["2", "LA 2", "la 2", "La 2"] + low("SUAVE") + low("CON LA 2"), NO],
"soluciones": {"incompleto": "DESPACIO.", "solo": "Hasta dónde llegó.", "carpeta": ["La 1.", "La 2.", "No: llega más lejos con fuerza."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer el rozamiento.",
"vas_a_ver": ["Qué es el rozamiento", "Superficies lisas y ásperas", "Resbalar y frenar"],
"secciones": [
 S(1, "El rozamiento", [
  D("Rozamiento", "Cuando algo se arrastra, el piso lo <b>frena</b> un poco."),
  P("Una pelota que rueda, al final <b>para</b>: el rozamiento la frena."),
  IMG("Lisa y áspera", "Comparamos superficies.", FG.tiras(["PISO LISO: SE DESLIZA MÁS", "PASTO O ALFOMBRA: FRENA MÁS"], numeros=False, cols=1)),
 ]),
 S(1, "Resbalar", [
  P("En el <b>hielo</b> o en un piso mojado, hay poco rozamiento: ¡resbalamos!"),
  P("Las zapatillas tienen <b>dibujitos</b> abajo para no resbalar."),
  IMG("Para no resbalar", "Más rozamiento, más agarre.", FG.nombres(["SUELA CON DIBUJOS", "PISO SECO", "ARENA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las superficies. Las vas a usar en la carpeta."),
  IMG("¿Dónde frena más?", "Pensá en cada una.", FG.nombres(["PISO DE CERÁMICA", "ALFOMBRA", "HIELO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El autito", "planteo": "¿Dónde llega más lejos el autito?", "pasos": ["En el piso liso.", "Hay poco rozamiento.", "Frena menos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el hielo…", "pasos": ["…hay poco rozamiento y ___ ."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Hacé rodar un autito en la alfombra y en el piso. ¿Dónde llega más lejos?"},
"tip": {"titulo": "Liso o áspero", "texto": "Lo áspero frena más que lo liso."},
"ojo": ["Cuidado con los pisos mojados.", "El rozamiento siempre frena."],
"resumen": [{"titulo": "Rozamiento", "texto": "Frena lo que se arrastra."}, {"titulo": "Liso", "texto": "Frena menos."}, {"titulo": "Áspero", "texto": "Frena más."}],
"glosario": [{"palabra": "Áspero", "significado": "Que no es liso."}, {"palabra": "Resbalar", "significado": "Deslizarse sin querer."}],
"carpeta": ["¿Dónde frena MÁS el autito: cerámica, alfombra o hielo?", "¿Dónde frena MENOS?", "Tomi dice que en el hielo no se resbala. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("ALFOMBRA") + low("EN LA ALFOMBRA") + low("LA ALFOMBRA"), low("HIELO") + low("EN EL HIELO") + low("EL HIELO"), NO],
"soluciones": {"incompleto": "RESBALAMOS.", "solo": "Dónde llegó más lejos.", "carpeta": ["En la alfombra.", "En el hielo.", "No: en el hielo se resbala."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver qué atraen los imanes.",
"vas_a_ver": ["Qué es un imán", "Qué atrae", "Qué no atrae"],
"secciones": [
 S(1, "Los imanes", [
  D("Imán", "Atrae algunos objetos de <b>metal</b>, ¡sin tocarlos!"),
  P("Tomi acerca un imán a unos clips y ¡se pegan!"),
  IMG("El imán atrae", "Clips, tornillos y clavos.", FG.nombres(["CLIP", "TORNILLO", "CLAVO"], cols=3)),
 ]),
 S(1, "No atrae", [
  P("El imán <b>no atrae</b> papel, madera, plástico ni vidrio."),
  IMG("Atrae o no atrae", "Probamos.", FG.tiras(["ATRAE: CLIP, CLAVO", "NO ATRAE: GOMA, LÁPIZ, PAPEL"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los objetos. Los vas a usar en la carpeta."),
  IMG("¿Lo atrae?", "Pensá de qué está hecho.", FG.nombres(["TAPITA DE METAL", "HOJA", "CUCHARA DE MADERA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El clip", "planteo": "¿El imán atrae un clip?", "pasos": ["El clip es de metal.", "Acerco el imán.", "¡Se pega!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El imán no atrae…", "pasos": ["…el ___ ni la madera."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Con un imán de la heladera, probá qué cosas atrae."},
"tip": {"titulo": "Probá y anotá", "texto": "Hacé dos listas: atrae y no atrae."},
"ojo": ["No todos los metales se pegan al imán.", "El imán no atrae plástico."],
"resumen": [{"titulo": "Imán", "texto": "Atrae sin tocar."}, {"titulo": "Atrae", "texto": "Clips, clavos."}, {"titulo": "No atrae", "texto": "Papel, madera, plástico."}],
"glosario": [{"palabra": "Imán", "significado": "Objeto que atrae algunos metales."}, {"palabra": "Atraer", "significado": "Acercar hacia sí."}],
"carpeta": ["¿Qué objeto del dibujo atrae el imán?", "¿Atrae la CUCHARA DE MADERA?", "Tomi dice que el imán atrae el papel. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("TAPITA DE METAL") + low("LA TAPITA") + low("TAPITA"), NO, NO],
"soluciones": {"incompleto": "PAPEL (o plástico).", "solo": "Tus dos listas.", "carpeta": ["La tapita de metal.", "No.", "No: el papel no se pega."]},
}

ACT = {
"1": [MC("PARA ABRIR UN CAJÓN…", ["TIRO", "EMPUJO"], "TIRO", "LO ACERCO A MÍ.", n="aplicar"),
      TF("EMPUJAR Y TIRAR SON FUERZAS.", "VERDADERO", "HACEN MOVER LAS COSAS.", n="recordar")],
"2": [MC("¿CÓMO VA LA PELOTA CON UNA PATADA FUERTE?", ["RÁPIDO Y LEJOS", "DESPACIO Y CERCA"], "RÁPIDO Y LEJOS", "MÁS FUERZA, MÁS LEJOS.", n="aplicar"),
      TF("PARA FRENAR TAMBIÉN HACE FALTA FUERZA.", "VERDADERO", "COMO EL ARQUERO.", n="analizar")],
"3": [MC("¿DÓNDE RESBALAMOS MÁS?", ["EN EL HIELO", "EN EL PASTO"], "EN EL HIELO", "HAY POCO ROZAMIENTO.", n="aplicar"),
      UNI("UNÍ CADA SUPERFICIE CON LO QUE PASA.", [("HIELO", "RESBALA"), ("ALFOMBRA", "FRENA MUCHO"), ("PISO LISO", "SE DESLIZA")], "LISO FRENA MENOS.", n="analizar")],
"4": [MC("¿QUÉ ATRAE EL IMÁN?", ["UN CLIP", "UNA GOMA", "UN PAPEL"], "UN CLIP", "ES DE METAL.", n="aplicar"),
      TF("EL IMÁN ATRAE LA MADERA.", "FALSO", "NO ATRAE MADERA.", n="error")],
"5": [MC("RELÁMPAGO. EMPUJAR…", ["ALEJA", "ACERCA"], "ALEJA", "LO MANDO LEJOS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. MÁS FUERZA…", ["MÁS LEJOS", "MÁS CERCA"], "MÁS LEJOS", "Y MÁS RÁPIDO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA ALFOMBRA…", ["FRENA MÁS", "FRENA MENOS"], "FRENA MÁS", "ES ÁSPERA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL IMÁN ATRAE…", ["UN CLAVO", "UN LÁPIZ"], "UN CLAVO", "ES DE METAL.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES TIRAR?", ["ACERCAR ALGO", "ALEJAR ALGO"], "ACERCAR ALGO", "COMO UNA SOGA.", n="recordar")],
 [1, UNI("UNÍ CADA ACCIÓN.", [("PUERTA QUE SE ABRE HACIA AFUERA", "EMPUJAR"), ("SOGA", "TIRAR")], "¿SE ALEJA O SE ACERCA?", n="analizar")],
 [1, TF("UNA PELOTA QUIETA SE MUEVE SOLA.", "FALSO", "NECESITA UNA FUERZA.", n="error")],
 [2, MC("¿CON QUÉ PATADA LA PELOTA VA MÁS LEJOS?", ["FUERTE", "SUAVE"], "FUERTE", "MÁS FUERZA, MÁS LEJOS.", n="aplicar")],
 [2, SA("¿QUÉ HACE EL ARQUERO CON LA PELOTA?", low("LA FRENA") + low("FRENA") + low("LA ATAJA") + low("ATAJA") + low("LA PARA"), "LA FRENA.", n="aplicar")],
 [2, TF("CON POCA FUERZA, ALGO SE MUEVE DESPACIO.", "VERDADERO", "Y LLEGA CERCA.", n="recordar")],
 [3, MC("¿QUÉ ES EL ROZAMIENTO?", ["LO QUE FRENA AL ARRASTRAR", "UN IMÁN"], "LO QUE FRENA AL ARRASTRAR", "EL PISO FRENA UN POCO.", n="recordar")],
 [3, SA("¿POR QUÉ LAS ZAPATILLAS TIENEN DIBUJOS ABAJO?", low("PARA NO RESBALAR") + low("NO RESBALAR") + low("PARA NO RESBALARSE") + low("PARA AGARRAR"), "PARA NO RESBALAR.", n="aplicar")],
 [3, TF("EN EL HIELO HAY MUCHO ROZAMIENTO.", "FALSO", "HAY POCO: POR ESO RESBALAMOS.", n="error")],
 [4, UNI("UNÍ CADA OBJETO.", [("CLIP", "ATRAE"), ("PAPEL", "NO ATRAE")], "PROBÁ CON UN IMÁN.", n="analizar")],
 [4, SA("ESCRIBÍ ALGO QUE EL IMÁN ATRAE.", low("CLIP") + low("CLAVO") + low("TORNILLO") + low("TAPITA") + low("ALFILER") + low("TUERCA") + low("LLAVE") + low("UN CLIP") + low("UN CLAVO"), "POR EJEMPLO: UN CLIP.", n="aplicar")],
 [4, MC("EL IMÁN ATRAE…", ["SIN TOCAR", "SOLO SI LO TOCA"], "SIN TOCAR", "LOS CLIPS SALTAN HACIA EL IMÁN.", n="recordar")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: empujar y tirar", "examen_titulo": "Nivel jefe: empujar y tirar",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
