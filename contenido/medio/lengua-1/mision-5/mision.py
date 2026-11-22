# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 5 · Letras T, N y D. Genera mision-5.json.
Regla de primeros años. Metáfora: la huerta de la abuela de Sofi (TOMATE, NIDO, DEDO, DADO…). Solo letras ya vistas (vocales, M, P, S, L, T, N, D).
Niveles: 1 conocer la T · 2 conocer la N y la D · 3 leer palabras con T, N y D · 4 escribir palabras con T, N y D."""
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
"objetivo": "Vas a conocer la letra T.",
"vas_a_ver": ["La T de TOMATE", "Sílabas con T", "Palabras con T"],
"secciones": [
 S(1, "La T", [
  P("<b>T</b> de <b>TOMATE</b>. Suena como un reloj: t, t, t."),
  IMG("Palabras con T", "La T en rojo.", FG.nombres(["TOMATE", "TAPA", "TELA"], True, 3)),
 ]),
 S(1, "Sílabas con T", [
  D("La T", "Es una consonante. Con las vocales dice <b>TA, TE, TI, TO, TU</b>."),
  IMG("Sílabas con T", "TA, TE, TI, TO, TU.", FG.nombres(["TA", "TE", "TI", "TO", "TU"], cols=5)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "¿Dónde está la T?", FG.nombres(["PATO", "MOTO", "TINA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "TAPA", "planteo": "Leemos TAPA.", "pasos": ["TA.", "PA.", "Todo junto: TAPA."]},
"ejemplo_incompleto": {"titulo": "TELA", "planteo": "Completá.", "pasos": ["TE + ___ = TELA."]},
"ejemplo_solo": {"titulo": "Tu huerta", "planteo": "Pensá una verdura que empiece con T."},
"tip": {"titulo": "Como un reloj", "texto": "La T suena corta: t, t, t."},
"ojo": ["La T puede estar en el medio: PATO.", "No confundas la T con la D."],
"resumen": [{"titulo": "T", "texto": "De TOMATE."}, {"titulo": "Sílabas", "texto": "TA, TE, TI, TO, TU."}, {"titulo": "Lugar", "texto": "Principio o medio."}],
"glosario": [{"palabra": "Tela", "significado": "Con ella se hace la ropa."}, {"palabra": "Tina", "significado": "Bañera."}],
"carpeta": ["¿Con qué sílaba empieza TINA?", "¿Con qué sílaba termina PATO?", "¿Con qué sílaba termina MOTO?"],
"respuestas_carpeta": [low("TI"), low("TO"), low("TO")],
"soluciones": {"incompleto": "LA.", "solo": "Por ejemplo: TOMATE.", "carpeta": ["TI.", "TO.", "TO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer la letra N y la letra D.",
"vas_a_ver": ["La N de NIDO", "La D de DEDO", "Sílabas con N y D"],
"secciones": [
 S(1, "La N", [
  P("<b>N</b> de <b>NIDO</b>. Suena por la nariz: nnn."),
  IMG("Palabras con N", "La N en rojo.", FG.nombres(["NIDO", "NENE", "NUDO"], True, 3)),
 ]),
 S(1, "La D", [
  D("La N y la D", "Son consonantes. <b>NA, NE, NI, NO, NU</b>. <b>DA, DE, DI, DO, DU</b>."),
  P("<b>D</b> de <b>DEDO</b>. La lengua toca los dientes: d."),
  IMG("Palabras con D", "La D en rojo.", FG.nombres(["DEDO", "DADO", "DAMA"], True, 3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "¿N o D?", FG.nombres(["NADA", "DUENDE", "MANO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "NUDO", "planteo": "Leemos NUDO.", "pasos": ["NU.", "DO.", "Todo junto: NUDO."]},
"ejemplo_incompleto": {"titulo": "DADO", "planteo": "Completá.", "pasos": ["DA + ___ = DADO."]},
"ejemplo_solo": {"titulo": "Tu cuerpo", "planteo": "Mostrá tu DEDO y tu MANO. ¿Qué letras tienen?"},
"tip": {"titulo": "Tocá tu nariz", "texto": "Al decir la N, sentís cosquillas en la nariz."},
"ojo": ["DEDO tiene dos D.", "NENE tiene dos N."],
"resumen": [{"titulo": "N", "texto": "De NIDO."}, {"titulo": "D", "texto": "De DEDO."}, {"titulo": "Sílabas", "texto": "NA… DA…"}],
"glosario": [{"palabra": "Nido", "significado": "Casita de los pájaros."}, {"palabra": "Nudo", "significado": "Lazo apretado."}],
"carpeta": ["¿Con qué letra empieza NADA?", "¿Con qué letra empieza DUENDE?", "¿Con qué sílaba termina MANO?"],
"respuestas_carpeta": [low("N"), low("D"), low("NO")],
"soluciones": {"incompleto": "DO.", "solo": "DEDO: D, E, D, O. MANO: M, A, N, O.", "carpeta": ["N.", "D.", "NO."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a leer palabras y oraciones con T, N y D.",
"vas_a_ver": ["Palabras de la huerta", "Leer una oración", "Leer con ritmo"],
"secciones": [
 S(1, "En la huerta", [
  P("TO-MA-TE: <b>TOMATE</b>. LU-NA: <b>LUNA</b>. PA-TO: <b>PATO</b>."),
  IMG("Palabras", "Sílaba por sílaba.", FG.nombres(["TOMATE", "LUNA", "PATO"], cols=3)),
 ]),
 S(1, "Una oración", [
  D("Leer una oración", "Leer cada palabra y después <b>todo junto</b>, sin parar."),
  P("<b>EL PATO TOMA SOPA</b>."),
  IMG("Leemos", "Palabra por palabra.", FG.nombres(["EL", "PATO", "TOMA", "SOPA"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Oración", "Leela.", FG.nombres(["DANI", "TIENE", "UN", "DADO"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "NIDO", "planteo": "Leemos NIDO.", "pasos": ["NI.", "DO.", "Todo junto: NIDO."]},
"ejemplo_incompleto": {"titulo": "MONO", "planteo": "Completá.", "pasos": ["MO + ___ = MONO."]},
"ejemplo_solo": {"titulo": "Leé", "planteo": "Leé en voz alta: EL NENE TOMA LA TAPA."},
"tip": {"titulo": "Leé dos veces", "texto": "La primera vez despacio. La segunda, más rápido."},
"ojo": ["No saltees palabras chiquitas: EL, UN.", "Volvé a leer si no entendiste."],
"resumen": [{"titulo": "Sílabas", "texto": "TO-MA-TE."}, {"titulo": "Palabras", "texto": "TOMATE."}, {"titulo": "Oración", "texto": "EL PATO TOMA SOPA."}],
"glosario": [{"palabra": "Huerta", "significado": "Lugar donde crecen verduras."}, {"palabra": "Ritmo", "significado": "Leer parejo, sin parar."}],
"carpeta": ["¿Cuál es la primera palabra?", "¿Cuántas palabras tiene la oración?", "¿Qué tiene DANI?"],
"respuestas_carpeta": [low("DANI"), ["4"], ["UN DADO", "un dado", "DADO", "dado", "Un dado"]],
"soluciones": {"incompleto": "NO.", "solo": "EL NENE TOMA LA TAPA.", "carpeta": ["DANI.", "4.", "UN DADO."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con T, N y D.",
"vas_a_ver": ["Escuchar cada sonido", "T o D", "Revisar"],
"secciones": [
 S(1, "Escribir PATO", [
  P("Decimos <b>PA-TO</b>. Escribimos PA y después TO."),
  IMG("PATO", "P, A, T, O.", FG.letras("PATO", numeros=True)),
 ]),
 S(1, "¿T o D?", [
  D("T o D", "Suenan parecido. Decí la palabra lento y escuchá."),
  P("DADO lleva <b>D</b>. TAPA lleva <b>T</b>."),
  IMG("Falta una letra", "DE_O: falta la D.", FG.letras("DEDO", ocultar=(2,), numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la palabra. La vas a usar en la carpeta."),
  IMG("Completá", "TOMATE con huecos.", FG.letras("TOMATE", ocultar=(0, 4), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "NIDO", "planteo": "Escribimos NIDO.", "pasos": ["Digo: NI-DO.", "Escribo NI.", "Escribo DO: NIDO."]},
"ejemplo_incompleto": {"titulo": "MANO", "planteo": "Completá.", "pasos": ["M A _ O."]},
"ejemplo_solo": {"titulo": "Tu palabra", "planteo": "Escribí una palabra con T, N o D. Leela para revisar."},
"tip": {"titulo": "Mirá tu boca", "texto": "En la T sale aire. En la D, la voz vibra."},
"ojo": ["TOMATE tiene dos T.", "Revisá leyendo despacio."],
"resumen": [{"titulo": "Escuchar", "texto": "PA-TO."}, {"titulo": "T o D", "texto": "Decir lento."}, {"titulo": "Revisar", "texto": "Leer lo escrito."}],
"glosario": [{"palabra": "Vibrar", "significado": "Temblar un poquito."}, {"palabra": "Pato", "significado": "Ave que nada."}],
"carpeta": ["¿Qué letra va en el lugar 1?", "¿Qué letra va en el lugar 5?", "¿Qué palabra se forma?"],
"respuestas_carpeta": [low("T"), low("T"), low("TOMATE")],
"soluciones": {"incompleto": "MANO.", "solo": "Por ejemplo: DADO.", "carpeta": ["T.", "T.", "TOMATE."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA EMPIEZA CON T?", ["TAPA", "DADO", "NIDO"], "TAPA", "T DE TAPA."),
      MC("¿CÓMO SE LEE T CON O?", ["TO", "OT", "DO"], "TO", "T Y O: TO.")],
"2": [MC("¿QUÉ PALABRA EMPIEZA CON N?", ["NUDO", "DEDO", "TELA"], "NUDO", "N DE NUDO."),
      MC("¿QUÉ PALABRA EMPIEZA CON D?", ["MANO", "DAMA", "LUNA"], "DAMA", "D DE DAMA.")],
"3": [MC("¿QUÉ PALABRA FORMAN LU Y NA?", ["LUNA", "NALU", "LANA"], "LUNA", "LU-NA."),
      MC("¿CUÁNTAS PALABRAS TIENE: EL PATO TOMA SOPA?", ["4", "3", "5"], "4", "EL · PATO · TOMA · SOPA.")],
"4": [SA("¿QUÉ LETRA FALTA? DE_O", low("D"), "DEDO."),
      ORD("ORDENÁ LAS SÍLABAS DE TOMATE.", ["TE", "TO", "MA"], ["TO", "MA", "TE"], "TO-MA-TE.")],
"5": [MC("RELÁMPAGO. ¿CUÁL ES LA N?", ["N", "M", "D"], "N", "N DE NIDO.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ PALABRA ES? DA-DO", ["DADO", "TODO", "NADA"], "DADO", "DA-DO.", tiempo=30),
      SA("RELÁMPAGO. ¿QUÉ LETRA FALTA? PA_O", low("T"), "PATO.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES UNA SÍLABA CON D?", ["DI", "TI", "NI"], "DI", "D E I.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿CON QUÉ LETRA EMPIEZA TELA?", ["T", "D", "N"], "T", "T DE TELA.")],
 [1, MC("¿CUÁNTAS T TIENE TOMATE?", ["2", "1", "3"], "2", "TO-MA-TE.")],
 [1, MC("¿CÓMO SE LEE T CON U?", ["TU", "UT", "DU"], "TU", "T Y U: TU.")],
 [2, MC("¿CON QUÉ LETRA EMPIEZA NENE?", ["N", "M", "D"], "N", "N DE NENE.")],
 [2, MC("¿CON QUÉ LETRA EMPIEZA DEDO?", ["D", "T", "N"], "D", "D DE DEDO.")],
 [2, SA("ESCRIBÍ D CON A.", low("DA"), "D Y A: DA.")],
 [3, MC("¿QUÉ PALABRA DICE NI-DO?", ["NIDO", "DINO", "NUDO"], "NIDO", "NI-DO.")],
 [3, MC("¿QUÉ PALABRA FORMAN MO Y TO?", ["MOTO", "TOMO", "MONO"], "MOTO", "MO-TO.")],
 [3, MC("EN: EL PATO TOMA SOPA, ¿QUÉ TOMA EL PATO?", ["SOPA", "TÉ", "AGUA"], "SOPA", "LO DICE LA ORACIÓN.")],
 [4, SA("¿QUÉ LETRA FALTA? MA_O", low("N"), "MANO.")],
 [4, SA("¿QUÉ LETRA FALTA? _APA", low("T"), "TAPA.")],
 [4, ORD("ORDENÁ LAS SÍLABAS DE DADO.", ["DO", "DA"], ["DA", "DO"], "DA-DO.")],
 [4, MC("¿CÓMO SE ESCRIBE BIEN?", ["NIDO", "NITO", "MIDO"], "NIDO", "NI-DO.")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: letras T, N y D", "examen_titulo": "Nivel jefe: letras T, N y D",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
