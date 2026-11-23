# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 12 · Las letras que faltan. Genera mision-12.json.
Regla de primeros años y vía fonológica (la VOZ de las clases dice sonidos, nunca nombres de letras; el PDF muestra las letras).
Y (YOYO, YEMA), Z (ZAPATO; en Argentina suena como sss), H (no suena: HUEVO), Q (siempre con U muda: QUESO), K (KIWI), X (TAXI: ks).
Metáfora: Sofi completa su abecedario (le faltan seis figuritas).
Niveles: 1 la Y y la Z · 2 la H y la Q · 3 la K y la X · 4 leer y escribir con todas las letras."""
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
"objetivo": "Vas a conocer la letra Y y la letra Z.",
"vas_a_ver": ["El álbum de Sofi", "La Y de YOYO", "La Z de ZAPATO"],
"secciones": [
 S(1, "Las letras que faltan", [
  P("Sofi tiene un álbum del <b>abecedario</b>. ¡Le faltan seis letras!"),
  IMG("El álbum de Sofi", "Las que faltan, en rojo.", FG.abecedario(resaltar="YZHQKX")),
 ]),
 S(1, "La Y y la Z", [
  P("<b>Y</b> de <b>YOYO</b> y de <b>YEMA</b>: YA, YE, YO."),
  P("<b>Z</b> de <b>ZAPATO</b>: ZA, ZO, ZU. Suena como sss."),
  IMG("Palabras con Y y Z", "La primera letra en rojo.", FG.nombres(["YOYO", "YEMA", "ZAPATO", "ZORRO"], True, 2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Y o Z?", "Mirá la primera letra.", FG.nombres(["YATE", "ZOO", "YUYO"], True, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "ZAPATO", "planteo": "Leemos ZAPATO.", "pasos": ["ZA.", "PA.", "TO. Todo junto: ZAPATO."]},
"ejemplo_incompleto": {"titulo": "YOYO", "planteo": "Completá.", "pasos": ["YO + ___ = YOYO."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá en tu casa algo que empiece con Z."},
"tip": {"titulo": "Mirá la letra", "texto": "La Z y la S suenan parecido. Mirá bien cómo se escribe."},
"ojo": ["ZAPATO va con Z.", "YOYO va con Y."],
"resumen": [{"titulo": "Y", "texto": "YA, YE, YO."}, {"titulo": "Z", "texto": "ZA, ZO, ZU."}, {"titulo": "Palabras", "texto": "YOYO, ZAPATO."}],
"glosario": [{"palabra": "Yema", "significado": "La parte amarilla del huevo."}, {"palabra": "Zorro", "significado": "Animal de cola larga."}],
"carpeta": ["¿Con qué letra empieza YATE?", "¿Con qué letra empieza ZOO?", "Tomi escribió SAPATO. ¿Con qué letra empieza?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("Y"), low("Z"), low("Z") + low("ZAPATO")],
"soluciones": {"incompleto": "YO.", "solo": "Por ejemplo: ZAPATILLA.", "carpeta": ["Y.", "Z.", "Con Z: ZAPATO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer la letra H y la letra Q.",
"vas_a_ver": ["La H no suena", "La Q va con U", "Palabras con H y Q"],
"secciones": [
 S(1, "La H", [
  D("La H", "Es la letra que <b>no suena</b>. Se escribe, pero no se escucha."),
  P("<b>HUEVO</b>, <b>HADA</b>, <b>HOJA</b>, <b>HELADO</b>."),
  IMG("Palabras con H", "La H en rojo: no suena.", FG.nombres(["HUEVO", "HADA", "HOJA"], True, 3)),
 ]),
 S(1, "La Q", [
  D("La Q", "Siempre va con <b>U</b>: <b>QUE</b>, <b>QUI</b>. La U no suena."),
  P("<b>QUESO</b>, <b>QUINCE</b>, <b>PAQUETE</b>."),
  IMG("Palabras con Q", "QUE y QUI.", FG.nombres(["QUESO", "QUINCE", "PAQUETE"], True, 3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Qué letra falta?", "Pensá en la H y la Q.", FG.nombres(["_ELADO", "_UESO", "_OJA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "HUEVO", "planteo": "Leemos HUEVO.", "pasos": ["La H no suena.", "UE. VO.", "Todo junto: HUEVO."]},
"ejemplo_incompleto": {"titulo": "QUESO", "planteo": "Completá.", "pasos": ["Q + U + E = ___ ."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Mirá en la heladera: ¿hay algo con Q o con H?"},
"tip": {"titulo": "La H es callada", "texto": "No la escuchás, pero hay que escribirla."},
"ojo": ["HUEVO lleva H aunque no suene.", "La Q siempre lleva U."],
"resumen": [{"titulo": "H", "texto": "No suena."}, {"titulo": "Q", "texto": "QUE, QUI."}, {"titulo": "Palabras", "texto": "HUEVO, QUESO."}],
"glosario": [{"palabra": "Hada", "significado": "Personaje mágico de los cuentos."}, {"palabra": "Paquete", "significado": "Algo envuelto para regalar o mandar."}],
"carpeta": ["¿Qué letra falta en _ELADO?", "¿Qué letra falta en _UESO?", "Tomi escribió UEVO. ¿Qué letra falta al principio?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("H"), low("Q"), low("H")],
"soluciones": {"incompleto": "QUE.", "solo": "Por ejemplo: QUESO, HUEVOS.", "carpeta": ["H.", "Q.", "H: HUEVO."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer la letra K y la letra X.",
"vas_a_ver": ["La K de KIWI", "La X de TAXI", "Pocas palabras"],
"secciones": [
 S(1, "La K", [
  P("<b>K</b> de <b>KIWI</b> y de <b>KOALA</b>. Suena como en CASA."),
  IMG("Palabras con K", "Hay muy pocas.", FG.nombres(["KIWI", "KOALA", "KILO"], True, 3)),
 ]),
 S(1, "La X", [
  P("<b>X</b> de <b>TAXI</b>. Suena como dos sonidos juntos: ks."),
  P("También en <b>EXAMEN</b> y <b>BOXEO</b>."),
  IMG("Palabras con X", "La X está en el medio.", FG.nombres(["TAXI", "EXAMEN", "BOXEO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿K o X?", "Pensá cómo suena.", FG.nombres(["_OALA", "TA_I", "_ILO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "KIWI", "planteo": "Leemos KIWI.", "pasos": ["KI.", "WI.", "Todo junto: KIWI."]},
"ejemplo_incompleto": {"titulo": "TAXI", "planteo": "Completá.", "pasos": ["TA + ___ = TAXI."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá un cartel de TAXI en la calle."},
"tip": {"titulo": "Pocas palabras", "texto": "Con K y con X hay muy pocas palabras."},
"ojo": ["KILO va con K.", "TAXI va con X."],
"resumen": [{"titulo": "K", "texto": "KIWI, KOALA."}, {"titulo": "X", "texto": "Suena ks: TAXI."}, {"titulo": "Pocas", "texto": "Hay pocas palabras."}],
"glosario": [{"palabra": "Koala", "significado": "Animal que vive en los árboles."}, {"palabra": "Kiwi", "significado": "Fruta verde por dentro."}],
"carpeta": ["¿Qué letra falta en _OALA?", "¿Qué letra falta en TA_I?", "Tomi escribió TACSI. ¿Cómo se escribe?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("K"), low("X"), low("TAXI")],
"soluciones": {"incompleto": "XI.", "solo": "TAXI.", "carpeta": ["K.", "X.", "TAXI."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a leer y escribir palabras con todas las letras.",
"vas_a_ver": ["El álbum completo", "Leer palabras", "Escribir palabras"],
"secciones": [
 S(1, "¡Álbum completo!", [
  P("Sofi pegó las seis letras que faltaban. ¡Ya tiene <b>todas</b>!"),
  IMG("El abecedario completo", "Las 27 letras.", FG.abecedario()),
 ]),
 S(1, "Leer y escribir", [
  P("Ahora leemos palabras con las letras nuevas."),
  IMG("Palabras para leer", "Leelas despacio.", FG.nombres(["HELADO", "ZORRO", "QUESO", "YATE", "TAXI", "KIWI"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras con huecos", "¿Qué letra falta?", FG.nombres(["_APATO", "_ADA", "_IWI"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "HELADO", "planteo": "Leemos HELADO.", "pasos": ["La H no suena: E.", "LA. DO.", "Todo junto: HELADO."]},
"ejemplo_incompleto": {"titulo": "QUINCE", "planteo": "Completá.", "pasos": ["Q + U + I = ___ ."]},
"ejemplo_solo": {"titulo": "Tu lista", "planteo": "Escribí una palabra con H y otra con Z."},
"tip": {"titulo": "Leé despacio", "texto": "Juntá las sílabas de a una."},
"ojo": ["La H no suena, pero se escribe.", "La Q siempre va con U."],
"resumen": [{"titulo": "Y · Z", "texto": "YOYO, ZAPATO."}, {"titulo": "H · Q", "texto": "HUEVO, QUESO."}, {"titulo": "K · X", "texto": "KIWI, TAXI."}],
"glosario": [{"palabra": "Abecedario", "significado": "Todas las letras en orden."}, {"palabra": "Álbum", "significado": "Libro para pegar figuritas."}],
"carpeta": ["¿Qué letra falta en _APATO?", "¿Qué letra falta en _ADA?", "Tomi escribió QESO. ¿Qué letra le falta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("Z"), low("H"), low("U")],
"soluciones": {"incompleto": "QUI.", "solo": "Por ejemplo: HOJA y ZORRO.", "carpeta": ["Z.", "H.", "U: QUESO."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA EMPIEZA CON Z?", ["ZAPATO", "YOYO", "SOPA"], "ZAPATO", "ZA-PA-TO.", n="aplicar"),
      SA("COMPLETÁ: YO + YO = ___", low("YOYO"), "YOYO.", n="aplicar")],
"2": [TF("LA H NO SUENA.", "VERDADERO", "SE ESCRIBE PERO NO SE ESCUCHA.", n="recordar"),
      MC("¿QUÉ PALABRA EMPIEZA CON H?", ["HUEVO", "QUESO", "ZORRO"], "HUEVO", "HUE-VO.", n="aplicar")],
"3": [UNI("UNÍ CADA PALABRA CON SU LETRA.", [("KIWI", "K"), ("TAXI", "X"), ("YOYO", "Y")], "MIRÁ LAS LETRAS.", n="analizar"),
      MC("¿QUÉ PALABRA TIENE X?", ["TAXI", "KILO", "QUESO"], "TAXI", "TA-XI.", n="aplicar")],
"4": [SA("ESCRIBÍ BIEN: _ELADO", low("HELADO"), "HELADO, CON H.", n="aplicar"),
      TF("QESO ESTÁ BIEN ESCRITO.", "FALSO", "SE ESCRIBE QUESO.", n="error")],
"5": [MC("RELÁMPAGO. ¿QUÉ LETRA NO SUENA?", ["H", "Z"], "H", "LA H ES CALLADA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA Q VA CON…", ["U", "A"], "U", "QUE, QUI.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CON QUÉ EMPIEZA KIWI?", ["K", "Q"], "K", "KI-WI.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CON QUÉ EMPIEZA YATE?", ["Y", "Z"], "Y", "YA-TE.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿CON QUÉ LETRA EMPIEZA ZORRO?", ["Z", "S", "Y"], "Z", "ZO-RRO.", n="aplicar")],
 [1, SA("COMPLETÁ: YE + MA = ___", low("YEMA"), "YEMA.", n="aplicar")],
 [1, TF("SAPATO ESTÁ BIEN ESCRITO.", "FALSO", "SE ESCRIBE ZAPATO.", n="error")],
 [2, MC("¿QUÉ LETRA SE ESCRIBE PERO NO SUENA?", ["H", "Q", "Y"], "H", "COMO EN HUEVO.", n="recordar")],
 [2, SA("COMPLETÁ: _OJA", low("HOJA"), "HOJA, CON H.", n="aplicar")],
 [2, UNI("UNÍ CADA PALABRA CON SU LETRA.", [("HADA", "H"), ("QUESO", "Q"), ("ZORRO", "Z")], "MIRÁ LA PRIMERA LETRA.", n="analizar")],
 [3, MC("¿QUÉ PALABRA EMPIEZA CON K?", ["KOALA", "COCO", "QUESO"], "KOALA", "KO-A-LA.", n="aplicar")],
 [3, SA("COMPLETÁ: TA + XI = ___", low("TAXI"), "TAXI.", n="aplicar")],
 [3, TF("CON K HAY MUCHÍSIMAS PALABRAS.", "FALSO", "HAY MUY POCAS.", n="error")],
 [4, ORD("ORDENÁ LAS SÍLABAS: HELADO.", ["DO", "HE", "LA"], ["HE", "LA", "DO"], "HE-LA-DO.", n="analizar")],
 [4, SA("ESCRIBÍ BIEN: _IWI", low("KIWI"), "KIWI, CON K.", n="aplicar")],
 [4, MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["QUESO", "QESO", "KESO"], "QUESO", "Q CON U.", n="error")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 12, "estilo": "primeros",
     "practica": "Práctica general: las letras que faltan", "examen_titulo": "Nivel jefe: las letras que faltan",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-12.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
