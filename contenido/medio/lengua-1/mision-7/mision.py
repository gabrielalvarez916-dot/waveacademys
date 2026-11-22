# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 7 · Letras C, F y B. Genera mision-7.json.
Regla de primeros años y vía fonológica. La C solo con su sonido fuerte (CA, CO, CU). Metáfora: un paseo por el mar (FOCA, BOTE, COCO, NUBE…).
Niveles: 1 conocer la C y la F · 2 conocer la B · 3 leer palabras con C, F y B · 4 escribir palabras con C, F y B."""
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
"objetivo": "Vas a conocer la letra C y la letra F.",
"vas_a_ver": ["La C de CASA", "La F de FOCA", "Sílabas con C y F"],
"secciones": [
 S(1, "La C", [
  P("<b>C</b> de <b>CASA</b>. Con A, O y U suena fuerte: <b>CA, CO, CU</b>."),
  IMG("Palabras con C", "La C en rojo.", FG.nombres(["CASA", "COCO", "CUNA"], True, 3)),
 ]),
 S(1, "La F", [
  D("La F", "Suena como cuando soplás: fff. <b>FA, FE, FI, FO, FU</b>."),
  IMG("Palabras con F", "La F en rojo.", FG.nombres(["FOCA", "FOTO", "FIDEO"], True, 3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "¿C o F?", FG.nombres(["CAMA", "FOCA", "CUBO"], True, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "COCO", "planteo": "Leemos COCO.", "pasos": ["CO.", "CO.", "Todo junto: COCO."]},
"ejemplo_incompleto": {"titulo": "FOTO", "planteo": "Completá.", "pasos": ["FO + ___ = FOTO."]},
"ejemplo_solo": {"titulo": "Soplá", "planteo": "Poné la mano frente a tu boca y decí FOCA. ¿Sentís el aire?"},
"tip": {"titulo": "Soplá", "texto": "Para la F, los dientes tocan el labio y sale aire."},
"ojo": ["Por ahora, la C va con A, O y U.", "La F no es la P."],
"resumen": [{"titulo": "C", "texto": "CA, CO, CU."}, {"titulo": "F", "texto": "Suena fff."}, {"titulo": "Palabras", "texto": "CASA, FOCA."}],
"glosario": [{"palabra": "Foca", "significado": "Animal que vive en el mar."}, {"palabra": "Cuna", "significado": "Camita de bebé."}],
"carpeta": ["¿Con qué letra empieza CAMA?", "¿Con qué letra empieza FOCA?", "¿Con qué sílaba empieza CUBO?"],
"respuestas_carpeta": [low("C"), low("F"), low("CU")],
"soluciones": {"incompleto": "TO.", "solo": "Sí: sale aire.", "carpeta": ["C.", "F.", "CU."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer la letra B.",
"vas_a_ver": ["La B de BOTE", "Sílabas con B", "Palabras con B"],
"secciones": [
 S(1, "La B", [
  P("<b>B</b> de <b>BOTE</b>. Los labios se juntan y se abren: <b>BA, BE, BI, BO, BU</b>."),
  IMG("Sílabas con B", "BA, BE, BI, BO, BU.", FG.nombres(["BA", "BE", "BI", "BO", "BU"], cols=5)),
 ]),
 S(1, "Palabras con B", [
  D("La B", "Es una consonante. Con las vocales forma sílabas."),
  IMG("Palabras con B", "La B en rojo.", FG.nombres(["BOTE", "BEBÉ", "BOCA"], True, 3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "¿Dónde está la B?", FG.nombres(["NUBE", "LOBO", "BOTA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "BOTA", "planteo": "Leemos BOTA.", "pasos": ["BO.", "TA.", "Todo junto: BOTA."]},
"ejemplo_incompleto": {"titulo": "NUBE", "planteo": "Completá.", "pasos": ["NU + ___ = NUBE."]},
"ejemplo_solo": {"titulo": "Tu cuerpo", "planteo": "Señalá tu BOCA. ¿Con qué sílaba empieza?"},
"tip": {"titulo": "Labios juntos", "texto": "Para la B, juntá los labios y abrilos."},
"ojo": ["La B y la P se parecen: BOTA no es POTA.", "La B puede estar en el medio: NUBE."],
"resumen": [{"titulo": "B", "texto": "De BOTE."}, {"titulo": "Sílabas", "texto": "BA, BE, BI, BO, BU."}, {"titulo": "Lugar", "texto": "Principio o medio."}],
"glosario": [{"palabra": "Bote", "significado": "Barco chiquito."}, {"palabra": "Nube", "significado": "Está en el cielo."}],
"carpeta": ["¿Con qué sílaba termina NUBE?", "¿Con qué sílaba termina LOBO?", "¿Con qué sílaba empieza BOTA?"],
"respuestas_carpeta": [low("BE"), low("BO"), low("BO")],
"soluciones": {"incompleto": "BE.", "solo": "BO.", "carpeta": ["BE.", "BO.", "BO."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a leer palabras y oraciones con C, F y B.",
"vas_a_ver": ["Palabras del mar", "Leer una oración", "Leer con ritmo"],
"secciones": [
 S(1, "Palabras del mar", [
  P("FO-CA: <b>FOCA</b>. BO-TE: <b>BOTE</b>. CO-CO: <b>COCO</b>."),
  IMG("Palabras", "Sílaba por sílaba.", FG.nombres(["FOCA", "BOTE", "COCO"], cols=3)),
 ]),
 S(1, "Una oración", [
  D("Leer una oración", "Leer palabra por palabra y después todo junto."),
  P("<b>LA FOCA TOMA UN COCO</b>."),
  IMG("Leemos", "Palabra por palabra.", FG.nombres(["LA", "FOCA", "TOMA", "UN", "COCO"], cols=5)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la oración. La vas a usar en la carpeta."),
  IMG("Oración", "Leela.", FG.nombres(["EL", "BEBÉ", "TIENE", "UNA", "BOTA"], cols=5)),
 ]),
],
"ejemplo_completo": {"titulo": "CUBO", "planteo": "Leemos CUBO.", "pasos": ["CU.", "BO.", "Todo junto: CUBO."]},
"ejemplo_incompleto": {"titulo": "FIDEO", "planteo": "Completá.", "pasos": ["FI + DE + ___ = FIDEO."]},
"ejemplo_solo": {"titulo": "Leé", "planteo": "Leé en voz alta: EL BOTE ESTÁ EN EL MAR."},
"tip": {"titulo": "Leé dos veces", "texto": "Primero despacio, después más rápido."},
"ojo": ["No saltees palabras chiquitas: LA, UN.", "Volvé a leer si no entendiste."],
"resumen": [{"titulo": "Sílabas", "texto": "FO-CA."}, {"titulo": "Palabras", "texto": "FOCA, BOTE."}, {"titulo": "Oración", "texto": "LA FOCA TOMA UN COCO."}],
"glosario": [{"palabra": "Coco", "significado": "Fruta dura con agua adentro."}, {"palabra": "Cubo", "significado": "Balde para la arena."}],
"carpeta": ["¿Quién tiene una bota?", "¿Qué tiene el bebé?", "¿Cuántas palabras tiene la oración?"],
"respuestas_carpeta": [["EL BEBÉ", "BEBÉ", "BEBE", "el bebé", "bebé", "bebe", "El bebé"], ["UNA BOTA", "BOTA", "una bota", "bota", "Una bota"], ["5"]],
"soluciones": {"incompleto": "O.", "solo": "EL BOTE ESTÁ EN EL MAR.", "carpeta": ["EL BEBÉ.", "UNA BOTA.", "5."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con C, F y B.",
"vas_a_ver": ["Escuchar cada sonido", "B o P", "Revisar"],
"secciones": [
 S(1, "Escribir FOCA", [
  P("Decimos <b>FO-CA</b>. Escribimos FO y después CA."),
  IMG("FOCA", "F, O, C, A.", FG.letras("FOCA", numeros=True)),
 ]),
 S(1, "¿B o P?", [
  D("B o P", "Se parecen. En la P sale aire; en la B, la voz vibra."),
  P("BOTA lleva <b>B</b>. PATO lleva <b>P</b>."),
  IMG("Falta una letra", "NU_E: falta la B.", FG.letras("NUBE", ocultar=(2,), numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la palabra. La vas a usar en la carpeta."),
  IMG("Completá", "CUBO con huecos.", FG.letras("CUBO", ocultar=(0, 2), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "BOCA", "planteo": "Escribimos BOCA.", "pasos": ["Digo: BO-CA.", "Escribo BO.", "Escribo CA: BOCA."]},
"ejemplo_incompleto": {"titulo": "FOTO", "planteo": "Completá.", "pasos": ["_ O T O."]},
"ejemplo_solo": {"titulo": "Tu palabra", "planteo": "Escribí una palabra con F. Leela para revisar."},
"tip": {"titulo": "Mano en la garganta", "texto": "Con la B sentís que vibra. Con la P, no."},
"ojo": ["COCO tiene dos C.", "Revisá leyendo despacio."],
"resumen": [{"titulo": "Escuchar", "texto": "FO-CA."}, {"titulo": "B o P", "texto": "Sentir la voz."}, {"titulo": "Revisar", "texto": "Leer lo escrito."}],
"glosario": [{"palabra": "Garganta", "significado": "Parte del cuello por donde sale la voz."}, {"palabra": "Vibrar", "significado": "Temblar un poquito."}],
"carpeta": ["¿Qué letra va en el lugar 1?", "¿Qué letra va en el lugar 3?", "¿Qué palabra se forma?"],
"respuestas_carpeta": [low("C"), low("B"), low("CUBO")],
"soluciones": {"incompleto": "FOTO.", "solo": "Por ejemplo: FOCA.", "carpeta": ["C.", "B.", "CUBO."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA EMPIEZA CON F?", ["FOCA", "CASA", "BOTA"], "FOCA", "FO-CA."),
      MC("¿CÓMO SE LEE C CON A?", ["CA", "AC", "FA"], "CA", "C Y A: CA.")],
"2": [MC("¿QUÉ PALABRA EMPIEZA CON B?", ["BOTE", "FOTO", "COCO"], "BOTE", "BO-TE."),
      SA("ESCRIBÍ B CON U.", low("BU"), "B Y U: BU.")],
"3": [MC("¿QUÉ PALABRA FORMAN CU Y NA?", ["CUNA", "NACU", "CUBA"], "CUNA", "CU-NA."),
      MC("EN: LA FOCA TOMA UN COCO, ¿QUÉ TOMA LA FOCA?", ["UN COCO", "UNA SOPA", "UN BOTE"], "UN COCO", "LO DICE LA ORACIÓN.")],
"4": [SA("¿QUÉ LETRA FALTA? NU_E", low("B"), "NU-BE."),
      ORD("ORDENÁ LAS SÍLABAS DE FOCA.", ["CA", "FO"], ["FO", "CA"], "FO-CA.")],
"5": [MC("RELÁMPAGO. ¿CUÁL SUENA COMO UN SOPLIDO?", ["F", "B", "C"], "F", "FFF.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ PALABRA ES? BO-CA", ["BOCA", "CABO", "COBA"], "BOCA", "BO-CA.", tiempo=30),
      SA("RELÁMPAGO. ¿QUÉ LETRA FALTA? _ASA", low("C"), "CASA.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES UNA SÍLABA CON B?", ["BI", "PI", "FI"], "BI", "B E I.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿CON QUÉ LETRA EMPIEZA CAMA?", ["C", "F", "B"], "C", "CA-MA.")],
 [1, MC("¿CON QUÉ LETRA EMPIEZA FIDEO?", ["F", "P", "B"], "F", "FI-DE-O.")],
 [1, MC("¿CÓMO SE LEE C CON O?", ["CO", "OC", "FO"], "CO", "C Y O: CO.")],
 [2, MC("¿CON QUÉ LETRA EMPIEZA BEBÉ?", ["B", "P", "D"], "B", "BE-BÉ.")],
 [2, SA("ESCRIBÍ B CON A.", low("BA"), "B Y A: BA.")],
 [2, MC("¿QUÉ PALABRA TIENE B EN EL MEDIO?", ["NUBE", "BOTA", "FOCA"], "NUBE", "NU-BE.")],
 [3, MC("¿QUÉ PALABRA DICE FO-TO?", ["FOTO", "TOFO", "COCO"], "FOTO", "FO-TO.")],
 [3, MC("¿QUÉ PALABRA FORMAN CU Y BO?", ["CUBO", "BOCU", "CUNA"], "CUBO", "CU-BO.")],
 [3, MC("EN: EL BEBÉ TIENE UNA BOTA, ¿QUÉ TIENE EL BEBÉ?", ["UNA BOTA", "UN COCO", "UNA FOCA"], "UNA BOTA", "LO DICE LA ORACIÓN.")],
 [4, SA("¿QUÉ LETRA FALTA? _OTO", low("F"), "FOTO.")],
 [4, SA("¿QUÉ LETRA FALTA? LO_O", low("B"), "LOBO.")],
 [4, ORD("ORDENÁ LAS SÍLABAS DE BOTE.", ["TE", "BO"], ["BO", "TE"], "BO-TE.")],
 [4, MC("¿CÓMO SE ESCRIBE BIEN?", ["BOTA", "POTA", "DOTA"], "BOTA", "BO-TA.")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: letras C, F y B", "examen_titulo": "Nivel jefe: letras C, F y B",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
