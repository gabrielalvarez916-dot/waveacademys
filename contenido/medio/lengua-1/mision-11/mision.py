# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 11 · Letras V, Ñ y LL. Genera mision-11.json.
Regla de primeros años y vía fonológica (la VOZ de las clases dice sonidos y palabras ancla, nunca nombres de letras; el PDF muestra las letras).
V (VACA: suena igual que la B), Ñ (ÑANDÚ, NIÑO), LL (LLAVE, LLUVIA, POLLO).
Metáfora: un día de lluvia en la granja de la abuela (VACA, POLLITO, LLUVIA, NIÑA…).
Niveles: 1 conocer la V · 2 conocer la Ñ y la LL · 3 leer palabras con V, Ñ y LL · 4 escribir palabras con V, Ñ y LL."""
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

N1 = {**ESTILO,
"objetivo": "Vas a conocer la letra V.",
"vas_a_ver": ["La V de VACA", "Sílabas con V", "Palabras con V"],
"secciones": [
 S(1, "La V", [
  P("Sofi visita la granja de la abuela. ¡Hay una <b>VACA</b>!"),
  P("<b>V</b> de <b>VACA</b>: <b>VA, VE, VI, VO, VU</b>."),
  IMG("Sílabas con V", "VA, VE, VI, VO, VU.", FG.nombres(["VA", "VE", "VI", "VO", "VU"], cols=5)),
 ]),
 S(1, "Palabras con V", [
  D("La V", "Suena igual que la B de BOTE. Hay que mirar cómo se escribe."),
  IMG("Palabras con V", "La V en rojo.", FG.nombres(["VACA", "VASO", "UVA"], True, 3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "Leelas despacio.", FG.nombres(["VELA", "AVIÓN", "NUEVE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "VACA", "planteo": "Leemos VACA.", "pasos": ["VA.", "CA.", "Todo junto: VACA."]},
"ejemplo_incompleto": {"titulo": "VELA", "planteo": "Completá.", "pasos": ["VE + ___ = VELA."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá en tu casa algo que empiece con V."},
"tip": {"titulo": "Mirá la palabra", "texto": "La V y la B suenan igual. Fijate cómo se escribe."},
"ojo": ["VACA va con V.", "BOTE va con B."],
"resumen": [{"titulo": "V", "texto": "VA, VE, VI, VO, VU."}, {"titulo": "Suena", "texto": "Igual que la B."}, {"titulo": "Palabras", "texto": "VACA, VASO, UVA."}],
"glosario": [{"palabra": "Granja", "significado": "Lugar del campo con animales."}, {"palabra": "Vela", "significado": "Da luz cuando se prende."}],
"carpeta": ["¿Con qué letra empieza VELA?", "¿Con qué sílaba empieza VELA?", "Tomi escribió BACA para el animal. ¿Con qué letra empieza?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("V"), low("VE"), low("V") + low("VACA")],
"soluciones": {"incompleto": "LA.", "solo": "Por ejemplo: VENTANA.", "carpeta": ["V.", "VE.", "Con V: VACA."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer la letra Ñ y la LL.",
"vas_a_ver": ["La Ñ de ÑANDÚ", "La LL de LLUVIA", "Palabras con Ñ y LL"],
"secciones": [
 S(1, "La Ñ", [
  P("<b>Ñ</b> de <b>ÑANDÚ</b> y de <b>NIÑO</b>: <b>ÑA, ÑE, ÑI, ÑO, ÑU</b>."),
  D("La Ñ", "Es la N con un <b>sombrerito</b>. Suena distinto."),
  IMG("Palabras con Ñ", "La Ñ está en el medio.", FG.nombres(["NIÑO", "MOÑO", "PIÑA"], cols=3)),
 ]),
 S(1, "La LL", [
  P("Empieza a llover. <b>LL</b> de <b>LLUVIA</b> y de <b>LLAVE</b>."),
  D("La LL", "Son <b>dos L juntas</b> que hacen un solo sonido."),
  IMG("Palabras con LL", "Dos L juntas.", FG.nombres(["LLAVE", "LLUVIA", "POLLO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Ñ o LL?", "¿Qué falta?", FG.nombres(["NI_O", "PO_ITO", "_AVE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "NIÑO", "planteo": "Leemos NIÑO.", "pasos": ["NI.", "ÑO.", "Todo junto: NIÑO."]},
"ejemplo_incompleto": {"titulo": "LLAVE", "planteo": "Completá.", "pasos": ["LLA + ___ = LLAVE."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá una LLAVE en tu casa y decí su nombre."},
"tip": {"titulo": "Mirá el sombrerito", "texto": "Sin sombrerito es N. Con sombrerito es Ñ."},
"ojo": ["NIÑO no es NINO.", "La LL son dos L juntas."],
"resumen": [{"titulo": "Ñ", "texto": "ÑANDÚ, NIÑO."}, {"titulo": "LL", "texto": "LLAVE, LLUVIA."}, {"titulo": "Mirá", "texto": "El sombrerito de la Ñ."}],
"glosario": [{"palabra": "Ñandú", "significado": "Ave grande que corre rápido."}, {"palabra": "Moño", "significado": "Lazo para el pelo o un regalo."}],
"carpeta": ["¿Qué falta en NI_O?", "¿Qué falta en PO_ITO?", "Tomi escribió NINO. ¿Cómo se escribe?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("Ñ"), low("LL"), low("NIÑO")],
"soluciones": {"incompleto": "VE.", "solo": "LLAVE.", "carpeta": ["Ñ.", "LL.", "NIÑO, con Ñ."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a leer palabras con V, Ñ y LL.",
"vas_a_ver": ["Juntar sílabas", "Leer palabras", "Leer una oración"],
"secciones": [
 S(1, "Juntar sílabas", [
  P("Leemos de a una sílaba y después todo junto."),
  IMG("Sílabas", "Juntalas.", FG.tiras(["VA + SO = VASO", "PI + ÑA = PIÑA", "PO + LLO = POLLO"], numeros=False, cols=1)),
 ]),
 S(1, "Una oración", [
  P("Sofi leyó en la granja:"),
  IMG("La oración de Sofi", "Leela despacio.", FG.tiras(["EL POLLITO VE LA LLUVIA."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Leé las palabras. Las vas a usar en la carpeta."),
  IMG("Para leer", "Leelas en voz alta.", FG.nombres(["UÑA", "SILLA", "VACA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "PIÑA", "planteo": "Leemos PIÑA.", "pasos": ["PI.", "ÑA.", "Todo junto: PIÑA."]},
"ejemplo_incompleto": {"titulo": "SILLA", "planteo": "Completá.", "pasos": ["SI + ___ = SILLA."]},
"ejemplo_solo": {"titulo": "Leé", "planteo": "Leé la oración de Sofi a alguien de tu casa."},
"tip": {"titulo": "De a una", "texto": "Leé sílaba por sílaba y después juntá."},
"ojo": ["En POLLO, LLO es una sola sílaba.", "En PIÑA, ÑA es una sola sílaba."],
"resumen": [{"titulo": "Sílabas", "texto": "De a una."}, {"titulo": "Juntar", "texto": "Todo junto."}, {"titulo": "Oración", "texto": "Leer despacio."}],
"glosario": [{"palabra": "Pollito", "significado": "Pollo bebé."}, {"palabra": "Piña", "significado": "Fruta, también se llama ananá."}],
"carpeta": ["¿Qué palabra del dibujo tiene Ñ?", "¿Qué palabra del dibujo tiene LL?", "Tomi leyó SI-LA. ¿Cómo se lee bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("UÑA"), low("SILLA"), low("SILLA") + low("SI-LLA")],
"soluciones": {"incompleto": "LLA.", "solo": "EL POLLITO VE LA LLUVIA.", "carpeta": ["UÑA.", "SILLA.", "SI-LLA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con V, Ñ y LL.",
"vas_a_ver": ["Escuchar", "Elegir la letra", "Escribir"],
"secciones": [
 S(1, "Escribir", [
  P("Decimos la palabra despacio y escribimos cada sílaba."),
  IMG("Palabras para escribir", "Mirá cómo se escriben.", FG.dibujo_palabra([("vaso", "VASO"), ("estrella", "ESTRELLA"), ("silla", "SILLA")])),
 ]),
 S(1, "Elegir la letra", [
  P("¿Tiene sombrerito? Es <b>Ñ</b>. ¿Dos L juntas? Es <b>LL</b>."),
  IMG("Palabras con huecos", "¿Qué va?", FG.nombres(["_ASO", "ESTRE_A", "MO_O"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los dibujos. Los vas a usar en la carpeta."),
  IMG("Para escribir", "Escribí sus nombres.", FG.dibujo_palabra([("vaso", "?"), ("silla", "?"), ("estrella", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "LLAVE", "planteo": "Escribimos LLAVE.", "pasos": ["LLA: dos L y A.", "VE: V y E.", "LLAVE."]},
"ejemplo_incompleto": {"titulo": "MOÑO", "planteo": "Completá.", "pasos": ["MO + ___ = MOÑO."]},
"ejemplo_solo": {"titulo": "Tu lista", "planteo": "Escribí tres palabras: una con V, una con Ñ y una con LL."},
"tip": {"titulo": "Decilo despacio", "texto": "Escuchá cada sílaba antes de escribir."},
"ojo": ["ESTRELLA lleva LL.", "MOÑO lleva Ñ."],
"resumen": [{"titulo": "V", "texto": "VASO."}, {"titulo": "Ñ", "texto": "MOÑO."}, {"titulo": "LL", "texto": "ESTRELLA."}],
"glosario": [{"palabra": "Estrella", "significado": "Brilla en el cielo de noche."}, {"palabra": "Escribir", "significado": "Poner letras en el papel."}],
"carpeta": ["Escribí el nombre del primer dibujo.", "Escribí el nombre del segundo dibujo.", "Tomi escribió ESTRELA. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("VASO"), low("SILLA"), low("ESTRELLA")],
"soluciones": {"incompleto": "ÑO.", "solo": "Por ejemplo: VACA, NIÑO, LLAVE.", "carpeta": ["VASO.", "SILLA.", "ESTRELLA, con LL."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA EMPIEZA CON V?", ["VACA", "BOCA", "PATO"], "VACA", "VA-CA.", n="aplicar"),
      SA("COMPLETÁ: VA + SO = ___", low("VASO"), "VASO.", n="aplicar")],
"2": [MC("¿QUÉ PALABRA TIENE Ñ?", ["NIÑO", "NUBE", "LUNA"], "NIÑO", "NI-ÑO.", n="aplicar"),
      TF("LA LL SON DOS L JUNTAS.", "VERDADERO", "COMO EN LLAVE.", n="recordar")],
"3": [ORD("ORDENÁ LAS SÍLABAS: POLLO.", ["LLO", "PO"], ["PO", "LLO"], "PO-LLO.", n="analizar"),
      UNI("UNÍ CADA PALABRA CON SU LETRA.", [("VACA", "V"), ("PIÑA", "Ñ"), ("SILLA", "LL")], "MIRÁ LAS LETRAS.", n="analizar")],
"4": [SA("ESCRIBÍ BIEN: ESTRE_A", low("ESTRELLA"), "ESTRELLA, CON LL.", n="aplicar"),
      MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["MOÑO", "MONO DE REGALO", "MOLLO"], "MOÑO", "MOÑO VA CON Ñ.", n="error")],
"5": [MC("RELÁMPAGO. ¿QUÉ LETRA TIENE SOMBRERITO?", ["Ñ", "N"], "Ñ", "LA Ñ.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CON QUÉ EMPIEZA LLUVIA?", ["LL", "Y"], "LL", "LLU-VIA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CON QUÉ EMPIEZA VASO?", ["V", "B"], "V", "VA-SO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ESTÁ BIEN?", ["NIÑO", "NINO"], "NIÑO", "CON Ñ.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿CON QUÉ LETRA EMPIEZA VELA?", ["V", "B", "P"], "V", "VE-LA.", n="aplicar")],
 [1, SA("COMPLETÁ: U + VA = ___", low("UVA"), "UVA.", n="aplicar")],
 [1, TF("BACA ESTÁ BIEN ESCRITO PARA EL ANIMAL.", "FALSO", "SE ESCRIBE VACA.", n="error")],
 [2, MC("¿QUÉ PALABRA TIENE LL?", ["LLAVE", "LUNA", "LORO"], "LLAVE", "LLA-VE.", n="aplicar")],
 [2, SA("COMPLETÁ: PI + ÑA = ___", low("PIÑA") + low("pina"), "PIÑA.", n="aplicar")],
 [2, UNI("UNÍ CADA PALABRA CON SU LETRA.", [("MOÑO", "Ñ"), ("POLLO", "LL"), ("VASO", "V")], "MIRÁ LAS LETRAS.", n="analizar")],
 [3, ORD("ORDENÁ LAS SÍLABAS: SILLA.", ["LLA", "SI"], ["SI", "LLA"], "SI-LLA.", n="analizar")],
 [3, MC("¿QUÉ DICE? PO + LLI + TO", ["POLLITO", "PALITO", "PELOTA"], "POLLITO", "PO-LLI-TO.", n="aplicar")],
 [3, TF("EN NIÑO, ÑO ES UNA SÍLABA.", "VERDADERO", "NI-ÑO.", n="recordar")],
 [4, SA("ESCRIBÍ BIEN: _ASO", low("VASO"), "VASO, CON V.", n="aplicar")],
 [4, SA("ESCRIBÍ BIEN: MO_O (PARA EL PELO)", low("MOÑO") + low("mono"), "MOÑO, CON Ñ.", n="aplicar")],
 [4, MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["ESTRELLA", "ESTRELA"], "ESTRELLA", "CON LL.", n="error")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 11, "estilo": "primeros",
     "practica": "Práctica general: letras V, Ñ y LL", "examen_titulo": "Nivel jefe: letras V, Ñ y LL",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-11.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
