# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 9 · Letras R, G y J. Genera mision-9.json.
Regla de primeros años y vía fonológica. La R fuerte al principio (RANA) y suave en el medio (PERA). La G solo con su sonido suave (GA, GO, GU).
Metáfora: la función del circo (MAGO, JIRAFA, RANA, GORRO…).
Niveles: 1 conocer la R · 2 conocer la G y la J · 3 leer palabras con R, G y J · 4 escribir palabras con R, G y J."""
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
"objetivo": "Vas a conocer la letra R.",
"vas_a_ver": ["La R de RANA", "Sílabas con R", "La R en el medio"],
"secciones": [
 S(1, "La R", [
  P("<b>R</b> de <b>RANA</b>. Al principio suena fuerte, como un motor: rrr."),
  IMG("Palabras con R", "La R en rojo.", FG.nombres(["RANA", "ROSA", "RATÓN"], True, 3)),
 ]),
 S(1, "Sílabas con R", [
  D("La R", "Con las vocales forma <b>RA, RE, RI, RO, RU</b>."),
  IMG("Sílabas", "RA, RE, RI, RO, RU.", FG.nombres(["RA", "RE", "RI", "RO", "RU"], cols=5)),
 ]),
 S(2, "Para practicar", [
  P("En el medio, la R suena suave: <b>PERA</b>, <b>LORO</b>."),
  IMG("Palabras", "¿Dónde está la R?", FG.nombres(["PERA", "LORO", "RUEDA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "RANA", "planteo": "Leemos RANA.", "pasos": ["RA.", "NA.", "Todo junto: RANA."]},
"ejemplo_incompleto": {"titulo": "ROSA", "planteo": "Completá.", "pasos": ["RO + ___ = ROSA."]},
"ejemplo_solo": {"titulo": "El motor", "planteo": "Hacé el ruido de un motor: rrr. ¿Qué palabra empieza así?"},
"tip": {"titulo": "Como un motor", "texto": "Al principio, la R suena fuerte: rrr."},
"ojo": ["En el medio suena suave: PERA.", "La R no es la L: RAMA no es LAMA."],
"resumen": [{"titulo": "R", "texto": "De RANA."}, {"titulo": "Sílabas", "texto": "RA, RE, RI, RO, RU."}, {"titulo": "Medio", "texto": "Suave: PERA."}],
"glosario": [{"palabra": "Rana", "significado": "Animal verde que salta."}, {"palabra": "Loro", "significado": "Pájaro que habla."}],
"carpeta": ["¿Con qué letra empieza RUEDA?", "¿Con qué sílaba termina PERA?", "¿Con qué sílaba termina LORO?"],
"respuestas_carpeta": [low("R"), low("RA"), low("RO")],
"carpeta_nivel": ["recordar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "SA.", "solo": "Por ejemplo: RATÓN.", "carpeta": ["R.", "RA.", "RO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer la letra G y la letra J.",
"vas_a_ver": ["La G de GATO", "La J de JIRAFA", "Sílabas con G y J"],
"secciones": [
 S(1, "La G", [
  P("<b>G</b> de <b>GATO</b>. Con A, O y U: <b>GA, GO, GU</b>."),
  IMG("Palabras con G", "La G en rojo.", FG.nombres(["GATO", "GOMA", "GOTA"], True, 3)),
 ]),
 S(1, "La J", [
  D("La J", "Suena como cuando tenés frío: jjj. <b>JA, JE, JI, JO, JU</b>."),
  IMG("Palabras con J", "La J en rojo.", FG.nombres(["JIRAFA", "JUGO", "JAMÓN"], True, 3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "¿G o J?", FG.nombres(["MAGO", "OJO", "LAGO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "GOMA", "planteo": "Leemos GOMA.", "pasos": ["GO.", "MA.", "Todo junto: GOMA."]},
"ejemplo_incompleto": {"titulo": "JUGO", "planteo": "Completá.", "pasos": ["JU + ___ = JUGO."]},
"ejemplo_solo": {"titulo": "Tu cara", "planteo": "Señalá tu OJO. ¿Escuchás jjj?"},
"tip": {"titulo": "Raspá", "texto": "Para la J, el aire raspa la garganta: jjj."},
"ojo": ["Por ahora, la G va con A, O y U.", "JUGO tiene las dos: J y G."],
"resumen": [{"titulo": "G", "texto": "GA, GO, GU."}, {"titulo": "J", "texto": "Suena jjj."}, {"titulo": "Palabras", "texto": "GATO, JUGO."}],
"glosario": [{"palabra": "Mago", "significado": "Hace trucos en el circo."}, {"palabra": "Lago", "significado": "Mucha agua quieta."}],
"carpeta": ["¿Con qué sílaba termina MAGO?", "¿Con qué sílaba termina OJO?", "¿Con qué sílaba empieza LAGO?"],
"respuestas_carpeta": [low("GO"), low("JO"), low("LA")],
"carpeta_nivel": ["aplicar", "aplicar", "recordar"],
"soluciones": {"incompleto": "GO.", "solo": "Sí: O-JO.", "carpeta": ["GO.", "JO.", "LA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a leer palabras y oraciones con R, G y J.",
"vas_a_ver": ["Palabras del circo", "Leer una oración", "Leer con ritmo"],
"secciones": [
 S(1, "Palabras del circo", [
  P("MA-GO: <b>MAGO</b>. JI-RA-FA: <b>JIRAFA</b>. RA-NA: <b>RANA</b>."),
  IMG("Palabras", "Sílaba por sílaba.", FG.nombres(["MAGO", "JIRAFA", "RANA"], cols=3)),
 ]),
 S(1, "Una oración", [
  D("Leer una oración", "Palabra por palabra, y después todo junto."),
  P("<b>EL MAGO TOMA JUGO.</b>"),
  IMG("Leemos", "Palabra por palabra.", FG.nombres(["EL", "MAGO", "TOMA", "JUGO."], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la oración. La vas a usar en la carpeta."),
  IMG("Oración", "Leela.", FG.nombres(["LA", "JIRAFA", "TIENE", "UNA", "ROSA."], cols=5)),
 ]),
],
"ejemplo_completo": {"titulo": "GORRO", "planteo": "Leemos GORRO.", "pasos": ["GO.", "RRO.", "Todo junto: GORRO."]},
"ejemplo_incompleto": {"titulo": "JIRAFA", "planteo": "Completá.", "pasos": ["JI + RA + ___ = JIRAFA."]},
"ejemplo_solo": {"titulo": "Leé", "planteo": "Leé en voz alta: LA RANA SALTA EN EL LAGO."},
"tip": {"titulo": "Leé dos veces", "texto": "Primero despacio, después más rápido."},
"ojo": ["No saltees las palabras chiquitas.", "Si no entendés, leé otra vez."],
"resumen": [{"titulo": "Sílabas", "texto": "JI-RA-FA."}, {"titulo": "Palabras", "texto": "MAGO, RANA."}, {"titulo": "Oración", "texto": "EL MAGO TOMA JUGO."}],
"glosario": [{"palabra": "Circo", "significado": "Lugar con payasos y magos."}, {"palabra": "Gorro", "significado": "Va en la cabeza."}],
"carpeta": ["¿Quién tiene una rosa?", "¿Qué tiene la jirafa?", "¿Cuántas palabras tiene la oración?"],
"respuestas_carpeta": [["LA JIRAFA", "JIRAFA", "la jirafa", "jirafa", "La jirafa"], ["UNA ROSA", "ROSA", "una rosa", "rosa", "Una rosa"], ["5", "cinco", "CINCO"]],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "FA.", "solo": "LA RANA SALTA EN EL LAGO.", "carpeta": ["LA JIRAFA.", "UNA ROSA.", "5."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con R, G y J.",
"vas_a_ver": ["Escuchar cada sonido", "R o L", "Revisar"],
"secciones": [
 S(1, "Escribir MAGO", [
  P("Decimos <b>MA-GO</b>. Escribimos MA y después GO."),
  IMG("MAGO", "M, A, G, O.", FG.letras("MAGO", numeros=True)),
 ]),
 S(1, "¿R o L?", [
  D("R o L", "Se parecen. Con la R la lengua tiembla; con la L, no."),
  P("<b>PERA</b> lleva R. <b>PALA</b> lleva L."),
  IMG("Falta una letra", "LO_O: falta la R.", FG.letras("LORO", ocultar=(2,), numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la palabra. La vas a usar en la carpeta."),
  IMG("Completá", "JUGO con huecos.", FG.letras("JUGO", ocultar=(0, 2), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "ROJO", "planteo": "Escribimos ROJO.", "pasos": ["Digo: RO-JO.", "Escribo RO.", "Escribo JO: ROJO."]},
"ejemplo_incompleto": {"titulo": "GATO", "planteo": "Completá.", "pasos": ["_ A T O."]},
"ejemplo_solo": {"titulo": "Tu palabra", "planteo": "Escribí una palabra con J. Leela para revisar."},
"tip": {"titulo": "Decilo despacio", "texto": "Decí la palabra despacio antes de escribir."},
"ojo": ["La R en el medio suena suave: PERA.", "Revisá leyendo despacio."],
"resumen": [{"titulo": "Escuchar", "texto": "MA-GO."}, {"titulo": "R o L", "texto": "La lengua tiembla."}, {"titulo": "Revisar", "texto": "Leer lo escrito."}],
"glosario": [{"palabra": "Lengua", "significado": "Está adentro de la boca."}, {"palabra": "Temblar", "significado": "Moverse rápido."}],
"carpeta": ["¿Qué letra va en el lugar 1?", "¿Qué letra va en el lugar 3?", "¿Qué palabra se forma?"],
"respuestas_carpeta": [low("J"), low("G"), low("JUGO")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "GATO.", "solo": "Por ejemplo: OJO.", "carpeta": ["J.", "G.", "JUGO."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA EMPIEZA CON R?", ["RANA", "LANA", "PALA"], "RANA", "RA-NA.", n="aplicar"),
      MC("¿CÓMO SE LEE R CON O?", ["RO", "OR", "LO"], "RO", "R Y O: RO.", n="recordar")],
"2": [MC("¿QUÉ PALABRA EMPIEZA CON J?", ["JUGO", "GATO", "ROSA"], "JUGO", "JU-GO.", n="aplicar"),
      SA("ESCRIBÍ G CON A.", low("GA"), "G Y A: GA.", n="recordar")],
"3": [MC("¿QUÉ PALABRA FORMAN MA Y GO?", ["MAGO", "GOMA", "LAGO"], "MAGO", "MA-GO.", n="aplicar"),
      MC("EN: EL MAGO TOMA JUGO, ¿QUÉ TOMA EL MAGO?", ["JUGO", "SOPA", "TÉ"], "JUGO", "LO DICE LA ORACIÓN.", n="analizar")],
"4": [SA("¿QUÉ LETRA FALTA? PE_A", low("R"), "PE-RA.", n="aplicar"),
      MC("TOMI ESCRIBIÓ PALO, PERO QUERÍA DECIR PARO. ¿QUÉ LETRA CAMBIA?", ["LA L POR LA R", "LA P POR LA B", "LA O POR LA A"], "LA L POR LA R", "PA-RO.", n="error")],
"5": [MC("RELÁMPAGO. ¿CUÁL SUENA COMO UN MOTOR?", ["R", "J", "G"], "R", "RRR.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ PALABRA ES? GO-TA", ["GOTA", "TAGO", "JOTA"], "GOTA", "GO-TA.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. ¿QUÉ LETRA FALTA? O_O", low("J"), "OJO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ES UNA SÍLABA CON J?", ["JU", "GU", "RU"], "JU", "J Y U.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿CON QUÉ LETRA EMPIEZA ROSA?", ["R", "L", "J"], "R", "RO-SA.", n="recordar")],
 [1, MC("¿QUÉ PALABRA TIENE R EN EL MEDIO?", ["PERA", "RANA", "ROSA"], "PERA", "PE-RA.", n="analizar")],
 [1, SA("ESCRIBÍ R CON A.", low("RA"), "R Y A: RA.", n="recordar")],
 [2, MC("¿CON QUÉ LETRA EMPIEZA GATO?", ["G", "J", "R"], "G", "GA-TO.", n="recordar")],
 [2, MC("¿CON QUÉ LETRA EMPIEZA JIRAFA?", ["J", "G", "R"], "J", "JI-RA-FA.", n="recordar")],
 [2, MC("¿QUÉ PALABRA TIENE J Y G?", ["JUGO", "GATO", "OJO"], "JUGO", "JU-GO.", n="analizar")],
 [3, MC("¿QUÉ PALABRA DICE LA-GO?", ["LAGO", "GOLA", "MAGO"], "LAGO", "LA-GO.", n="aplicar")],
 [3, ORD("ORDENÁ LAS SÍLABAS DE JIRAFA.", ["FA", "JI", "RA"], ["JI", "RA", "FA"], "JI-RA-FA.", n="aplicar")],
 [3, MC("EN: LA JIRAFA TIENE UNA ROSA, ¿QUÉ TIENE?", ["UNA ROSA", "UN GORRO", "UN JUGO"], "UNA ROSA", "LO DICE LA ORACIÓN.", n="aplicar")],
 [4, SA("¿QUÉ LETRA FALTA? MA_O", low("G"), "MAGO.", n="aplicar")],
 [4, SA("¿QUÉ LETRA FALTA? _ANA", low("R"), "RANA.", n="aplicar")],
 [4, ORD("ORDENÁ LAS SÍLABAS DE ROJO.", ["JO", "RO"], ["RO", "JO"], "RO-JO.", n="aplicar")],
 [4, MC("SOFI ESCRIBIÓ LANA, PERO QUERÍA DECIR RANA. ¿QUÉ ESTÁ MAL?", ["LA PRIMERA LETRA", "LA ÚLTIMA LETRA", "NADA"], "LA PRIMERA LETRA", "RA-NA.", n="error")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: letras R, G y J", "examen_titulo": "Nivel jefe: letras R, G y J",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
