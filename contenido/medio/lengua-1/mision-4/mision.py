# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 4 · Letras S y L. Genera mision-4.json.
Regla de primeros años. Metáfora: un día de sol en la laguna (SOL, SAPO, LUPA, PALA…). Solo palabras con letras ya vistas (vocales, M, P, S, L).
Niveles: 1 conocer la S y la L · 2 leer sílabas con S y L · 3 leer palabras con S y L · 4 escribir palabras con S y L."""
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

N1 = {**ESTILO,
"objetivo": "Vas a conocer la letra S y la letra L.",
"vas_a_ver": ["La S de SOL", "La L de LUPA", "Cómo suenan"],
"secciones": [
 S(1, "La S", [
  P("<b>S</b> de <b>SOL</b>. Suena como una víbora: sss."),
  IMG("Palabras con S", "La S en rojo.", FG.nombres(["SOL", "SAPO", "SOPA"], True, 3)),
 ]),
 S(1, "La L", [
  D("La S y la L", "Son <b>consonantes</b>. Suenan con una vocal."),
  P("<b>L</b> de <b>LUPA</b>. La lengua toca arriba: lll."),
  IMG("Palabras con L", "La L en rojo.", FG.nombres(["LUPA", "LOMA", "LILA"], True, 3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "¿Con qué letra empiezan?", FG.nombres(["SAL", "LUPA", "SUMA"], True, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "SAPO", "planteo": "¿Con qué letra empieza SAPO?", "pasos": ["Digo: sss-APO.", "Empieza con S.", "S de SAPO."]},
"ejemplo_incompleto": {"titulo": "LOMA", "planteo": "Completá.", "pasos": ["LOMA empieza con la letra ___ ."]},
"ejemplo_solo": {"titulo": "Tu casa", "planteo": "Pensá algo de tu casa que empiece con S."},
"tip": {"titulo": "Escuchá el sonido", "texto": "La S suena sss. La L suena lll."},
"ojo": ["La S no es una vocal.", "La L se escribe con un palito y una patita."],
"resumen": [{"titulo": "S", "texto": "De SOL."}, {"titulo": "L", "texto": "De LUPA."}, {"titulo": "Sonido", "texto": "sss y lll."}],
"glosario": [{"palabra": "Lupa", "significado": "Vidrio que agranda las cosas."}, {"palabra": "Loma", "significado": "Un pequeño cerro."}],
"carpeta": ["¿Con qué letra empieza SAL?", "¿Con qué letra empieza LUPA?", "¿Con qué letra empieza SUMA?"],
"respuestas_carpeta": [low("S"), low("L"), low("S")],
"soluciones": {"incompleto": "L.", "solo": "Por ejemplo: SILLA, SOFÁ.", "carpeta": ["S.", "L.", "S."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a leer sílabas con S y con L.",
"vas_a_ver": ["La S con las vocales", "La L con las vocales", "Sílabas al revés"],
"secciones": [
 S(1, "Con S", [
  P("<b>SA, SE, SI, SO, SU</b>."),
  IMG("Sílabas con S", "Leelas en voz alta.", FG.nombres(["SA", "SE", "SI", "SO", "SU"], cols=5)),
 ]),
 S(1, "Con L", [
  D("Sílaba", "Pedacito de palabra que se dice de un golpe."),
  P("<b>LA, LE, LI, LO, LU</b>. ¡Y también al revés: <b>AL, EL, SOL</b>!"),
  IMG("Sílabas con L", "LA, LE, LI, LO, LU.", FG.nombres(["LA", "LE", "LI", "LO", "LU"], cols=5)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sílabas. Las vas a usar en la carpeta."),
  IMG("Sílabas", "Leelas.", FG.nombres(["SO", "LI", "SE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "LU", "planteo": "¿Cómo se lee L con U?", "pasos": ["L: lll.", "U: u.", "Juntas: LU."]},
"ejemplo_incompleto": {"titulo": "SA", "planteo": "Completá.", "pasos": ["S con A dice ___ ."]},
"ejemplo_solo": {"titulo": "Tu sílaba", "planteo": "Juntá la L con tu vocal preferida. ¿Qué dice?"},
"tip": {"titulo": "Estirá el sonido", "texto": "Decí sss-A: así suena SA."},
"ojo": ["SA y AS no son iguales.", "Leé de izquierda a derecha."],
"resumen": [{"titulo": "Con S", "texto": "SA, SE, SI, SO, SU."}, {"titulo": "Con L", "texto": "LA, LE, LI, LO, LU."}, {"titulo": "Al revés", "texto": "AL, EL."}],
"glosario": [{"palabra": "Sílaba", "significado": "Pedacito de palabra."}, {"palabra": "Al revés", "significado": "Primero la vocal."}],
"carpeta": ["¿Qué vocal tiene SO?", "¿Con qué letra empieza LI?", "¿Cómo se escribe S con E?"],
"respuestas_carpeta": [low("O"), low("L"), low("SE")],
"soluciones": {"incompleto": "SA.", "solo": "Por ejemplo: LA.", "carpeta": ["O.", "L.", "SE."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a leer palabras con S y con L.",
"vas_a_ver": ["Juntar sílabas", "Palabras de la laguna", "Leer una oración"],
"secciones": [
 S(1, "Palabras", [
  P("SA-PO: <b>SAPO</b>. PA-LA: <b>PALA</b>. LU-PA: <b>LUPA</b>."),
  IMG("Palabras", "Sílaba por sílaba.", FG.nombres(["SAPO", "PALA", "LUPA"], cols=3)),
 ]),
 S(1, "Una oración", [
  D("Oración", "Palabras juntas que dicen algo completo."),
  P("Leemos: <b>EL SAPO ES MALO</b>. Son cuatro palabras."),
  IMG("Leemos", "Palabra por palabra.", FG.nombres(["EL", "SAPO", "ES", "MALO"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "Leelas.", FG.nombres(["SOPA", "MESA", "LOMA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "SOPA", "planteo": "Leemos SOPA.", "pasos": ["SO.", "PA.", "Todo junto: SOPA."]},
"ejemplo_incompleto": {"titulo": "MESA", "planteo": "Completá.", "pasos": ["ME + ___ = MESA."]},
"ejemplo_solo": {"titulo": "Leé", "planteo": "Leé en voz alta: LOLA SALE AL SOL."},
"tip": {"titulo": "Palabra por palabra", "texto": "En una oración, leé cada palabra y después todo."},
"ojo": ["Entre palabra y palabra hay un espacio.", "Leé despacio, sin saltear."],
"resumen": [{"titulo": "Sílabas", "texto": "SA + PO."}, {"titulo": "Palabras", "texto": "SAPO."}, {"titulo": "Oración", "texto": "Dice algo completo."}],
"glosario": [{"palabra": "Oración", "significado": "Palabras que dicen algo."}, {"palabra": "Espacio", "significado": "Lugar vacío entre palabras."}],
"carpeta": ["¿Qué palabra está primero?", "¿Con qué sílaba empieza MESA?", "¿Con qué sílaba termina LOMA?"],
"respuestas_carpeta": [low("SOPA"), low("ME"), low("MA")],
"soluciones": {"incompleto": "SA.", "solo": "LOLA SALE AL SOL.", "carpeta": ["SOPA.", "ME.", "MA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con S y con L.",
"vas_a_ver": ["Escuchar las sílabas", "Escribir", "Revisar"],
"secciones": [
 S(1, "Escribir SOL", [
  P("Decimos <b>SOL</b>. Escuchamos: sss-O-lll."),
  IMG("SOL", "S, O, L.", FG.letras("SOL", numeros=True)),
 ]),
 S(1, "Revisar", [
  D("Revisar", "Leer lo que escribí para ver si está bien."),
  P("LU_A: falta la <b>P</b>. ¡LUPA!"),
  IMG("Falta una letra", "LUPA con un hueco.", FG.letras("LUPA", ocultar=(2,), numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la palabra. La vas a usar en la carpeta."),
  IMG("Completá", "SALA con huecos.", FG.letras("SALA", ocultar=(0, 2), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "PALA", "planteo": "Escribimos PALA.", "pasos": ["Digo: PA-LA.", "Escribo PA.", "Escribo LA: PALA."]},
"ejemplo_incompleto": {"titulo": "SAPO", "planteo": "Completá.", "pasos": ["_ A P O."]},
"ejemplo_solo": {"titulo": "Tu palabra", "planteo": "Escribí una palabra con S o con L. Leela para revisar."},
"tip": {"titulo": "Estirá la palabra", "texto": "Decí la palabra lento para escuchar cada letra."},
"ojo": ["No te olvides la L al final de SOL.", "Revisá leyendo despacio."],
"resumen": [{"titulo": "Escuchar", "texto": "sss-O-lll."}, {"titulo": "Escribir", "texto": "Letra por letra."}, {"titulo": "Revisar", "texto": "Leer lo escrito."}],
"glosario": [{"palabra": "Sala", "significado": "Lugar de una casa."}, {"palabra": "Pala", "significado": "Herramienta para la arena."}],
"carpeta": ["¿Qué letra va en el lugar 1?", "¿Qué letra va en el lugar 3?", "¿Qué palabra se forma?"],
"respuestas_carpeta": [low("S"), low("L"), low("SALA")],
"soluciones": {"incompleto": "SAPO.", "solo": "Por ejemplo: SOPA.", "carpeta": ["S.", "L.", "SALA."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA EMPIEZA CON S?", ["SOL", "LUPA", "MESA"], "SOL", "S DE SOL."),
      MC("¿QUÉ PALABRA EMPIEZA CON L?", ["SAPO", "LOMA", "PALA"], "LOMA", "L DE LOMA.")],
"2": [MC("¿CÓMO SE LEE L CON A?", ["LA", "AL", "SA"], "LA", "L Y A: LA."),
      SA("ESCRIBÍ S CON U.", low("SU"), "S Y U: SU.")],
"3": [MC("¿QUÉ PALABRA FORMAN SA Y PO?", ["SAPO", "POSA", "PASO"], "SAPO", "SA-PO."),
      MC("¿CUÁNTAS PALABRAS TIENE: EL SAPO ES MALO?", ["4", "2", "3"], "4", "EL · SAPO · ES · MALO.")],
"4": [SA("¿QUÉ LETRA FALTA? SO_", low("L"), "SOL."),
      ORD("ORDENÁ LAS SÍLABAS DE PALA.", ["LA", "PA"], ["PA", "LA"], "PA-LA.")],
"5": [MC("RELÁMPAGO. ¿CÓMO SUENA LA S?", ["SSS", "LLL", "MMM"], "SSS", "COMO UNA VÍBORA.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ PALABRA ES? LU-PA", ["LUPA", "PALU", "LOMA"], "LUPA", "LU-PA.", tiempo=30),
      SA("RELÁMPAGO. ¿QUÉ LETRA FALTA? _APO", low("S"), "SAPO.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES UNA SÍLABA CON L?", ["LI", "SI", "MI"], "LI", "L E I.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿CON QUÉ LETRA EMPIEZA SOPA?", ["S", "L", "P"], "S", "S DE SOPA.")],
 [1, MC("¿CON QUÉ LETRA EMPIEZA LILA?", ["L", "S", "I"], "L", "L DE LILA.")],
 [1, MC("LA S Y LA L SON…", ["CONSONANTES", "VOCALES"], "CONSONANTES", "NECESITAN UNA VOCAL.")],
 [2, MC("¿CÓMO SE LEE S CON I?", ["SI", "IS", "LI"], "SI", "S Y I: SI.")],
 [2, SA("ESCRIBÍ L CON O.", low("LO"), "L Y O: LO.")],
 [2, MC("¿CUÁL ES UNA SÍLABA CON S?", ["SE", "LE", "ME"], "SE", "S Y E.")],
 [3, MC("¿QUÉ PALABRA FORMAN ME Y SA?", ["MESA", "SAME", "MASA"], "MESA", "ME-SA.")],
 [3, MC("¿QUÉ PALABRA DICE LO-MA?", ["LOMA", "MALO", "SOLA"], "LOMA", "LO-MA.")],
 [3, MC("UNA ORACIÓN ES…", ["PALABRAS QUE DICEN ALGO", "UNA SOLA LETRA", "UN NÚMERO"], "PALABRAS QUE DICEN ALGO", "DICE ALGO COMPLETO.")],
 [4, SA("¿QUÉ LETRA FALTA? PA_A", low("L"), "PALA.")],
 [4, SA("¿QUÉ LETRA FALTA? _ALA", low("S"), "SALA.")],
 [4, ORD("ORDENÁ LAS SÍLABAS DE SOPA.", ["PA", "SO"], ["SO", "PA"], "SO-PA.")],
 [4, ORD("ORDENÁ LAS LETRAS DE SOL.", ["L", "S", "O"], ["S", "O", "L"], "S-O-L.")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: letras S y L", "examen_titulo": "Nivel jefe: letras S y L",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
