# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 2 · Las vocales. Genera mision-2.json.
Regla de primeros años. Metáfora: las cinco vocales son cinco amigas que viven en todas las palabras.
Niveles: 1 las cinco vocales · 2 vocales en los nombres · 3 vocales en las palabras · 4 escribir palabras con vocales."""
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

N1 = {**ESTILO,
"objetivo": "Vas a conocer las cinco vocales.",
"vas_a_ver": ["Las cinco vocales", "Cómo suenan", "Palabras que empiezan con vocal"],
"secciones": [
 S(1, "Cinco amigas", [
  P("Las vocales son cinco: <b>A, E, I, O, U</b>."),
  IMG("Las vocales", "A, E, I, O, U.", FG.nombres(["A", "E", "I", "O", "U"], cols=5)),
 ]),
 S(1, "Cómo suenan", [
  D("Vocal", "Una letra que suena <b>sola</b>, con la boca abierta."),
  P("A de ANA. E de ESTRELLA. I de ISLA. O de OSO. U de UVA."),
  IMG("Palabras con vocal", "Empiezan con vocal.", FG.nombres(["ANA", "ESTRELLA", "ISLA", "OSO", "UVA"], True, 5)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas", "Mirá la primera letra.", FG.nombres(["OSO", "UVA", "ESTRELLA"], True, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "OSO", "planteo": "¿Con qué vocal empieza OSO?", "pasos": ["Digo: O-SO.", "Empieza con O.", "La O es una vocal."]},
"ejemplo_incompleto": {"titulo": "UVA", "planteo": "Completá.", "pasos": ["UVA empieza con la vocal ___ ."]},
"ejemplo_solo": {"titulo": "Tus vocales", "planteo": "Decí las cinco vocales en voz alta."},
"tip": {"titulo": "Abrí la boca", "texto": "Las vocales se dicen con la boca abierta."},
"ojo": ["Son cinco vocales, no más.", "La S, la M o la T no son vocales."],
"resumen": [{"titulo": "Cinco", "texto": "A, E, I, O, U."}, {"titulo": "Suenan", "texto": "Solas."}, {"titulo": "Palabras", "texto": "OSO, UVA."}],
"glosario": [{"palabra": "Vocal", "significado": "A, E, I, O, U."}, {"palabra": "Sonido", "significado": "Cómo se escucha."}],
"carpeta": ["¿Con qué vocal empieza OSO?", "¿Con qué vocal empieza UVA?", "¿Con qué vocal empieza ESTRELLA?"],
"respuestas_carpeta": [["O", "o"], ["U", "u"], ["E", "e"]],
"soluciones": {"incompleto": "U.", "solo": "A, E, I, O, U.", "carpeta": ["O.", "U.", "E."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a encontrar las vocales en los nombres.",
"vas_a_ver": ["Buscar vocales", "Contar vocales", "Vocales que se repiten"],
"secciones": [
 S(1, "Vocales en SOFI", [
  P("SOFI tiene dos vocales: la <b>O</b> y la <b>I</b>."),
  IMG("Las vocales de SOFI", "En amarillo: O, I.", FG.letras("SOFI", resaltar=(1, 3))),
 ]),
 S(1, "Contar vocales", [
  D("Buscar vocales", "Mirar letra por letra y marcar A, E, I, O, U."),
  P("ANA tiene la <b>A</b> dos veces. ¡Se puede repetir!"),
  IMG("Las vocales de ANA", "A y A.", FG.letras("ANA", resaltar=(0, 2))),
 ]),
 S(2, "Para practicar", [
  P("Mirá el nombre. Lo vas a usar en la carpeta."),
  IMG("Un nombre", "Buscá las vocales.", FG.letras("MATEO", numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "TOMI", "planteo": "¿Qué vocales tiene TOMI?", "pasos": ["T no es vocal.", "O sí. M no. I sí.", "TOMI tiene O e I."]},
"ejemplo_incompleto": {"titulo": "BRUNO", "planteo": "Completá.", "pasos": ["BRUNO tiene la ___ y la ___ ."]},
"ejemplo_solo": {"titulo": "Tu nombre", "planteo": "Escribí tu nombre y marcá sus vocales."},
"tip": {"titulo": "Letra por letra", "texto": "Mirá cada letra y preguntá: ¿es vocal?"},
"ojo": ["Una vocal se puede repetir.", "Todos los nombres tienen vocales."],
"resumen": [{"titulo": "Buscar", "texto": "Letra por letra."}, {"titulo": "Marcar", "texto": "A, E, I, O, U."}, {"titulo": "Repetir", "texto": "ANA: A y A."}],
"glosario": [{"palabra": "Marcar", "significado": "Pintar o rodear."}, {"palabra": "Repetir", "significado": "Estar otra vez."}],
"carpeta": ["¿Cuál es la primera vocal de MATEO?", "¿Cuántas vocales tiene MATEO?", "¿Cuál es la última vocal de MATEO?"],
"respuestas_carpeta": [["A", "a"], ["3"], ["O", "o"]],
"soluciones": {"incompleto": "U. O.", "solo": "Depende de tu nombre.", "carpeta": ["A.", "3.", "O."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a encontrar las vocales en las palabras.",
"vas_a_ver": ["Vocales en todas las palabras", "Palabras con A", "Palabras con O"],
"secciones": [
 S(1, "Todas tienen vocales", [
  P("Todas las palabras tienen <b>vocales</b>. ¡Buscalas!"),
  IMG("Palabras con A", "La A en rojo.", FG.dibujo_palabra([("pelota", "PELOTA"), ("manzana", "MANZANA"), ("vaso", "VASO")], "A")),
 ]),
 S(1, "Con O", [
  D("Vocales en las palabras", "Están al principio, en el medio o al final."),
  IMG("Palabras con O", "La O en rojo.", FG.dibujo_palabra([("globo", "GLOBO"), ("pelota", "PELOTA"), ("vaso", "VASO")], "O")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "Buscá la E.", FG.dibujo_palabra([("estrella", "ESTRELLA"), ("pelota", "PELOTA"), ("silla", "SILLA")])),
 ]),
],
"ejemplo_completo": {"titulo": "MESA", "planteo": "¿Qué vocales tiene MESA?", "pasos": ["M no. E sí.", "S no. A sí.", "MESA tiene E y A."]},
"ejemplo_incompleto": {"titulo": "LUNA", "planteo": "Completá.", "pasos": ["LUNA tiene la ___ y la ___ ."]},
"ejemplo_solo": {"titulo": "Tu casa", "planteo": "Pensá una cosa de tu casa. ¿Qué vocales tiene?"},
"tip": {"titulo": "Decila despacio", "texto": "Decí la palabra lento y escuchá las vocales."},
"ojo": ["Las vocales pueden estar en cualquier lugar.", "No hay palabras sin vocales."],
"resumen": [{"titulo": "Todas", "texto": "Tienen vocales."}, {"titulo": "Lugar", "texto": "Principio, medio o final."}, {"titulo": "Escuchar", "texto": "Decir lento."}],
"glosario": [{"palabra": "Palabra", "significado": "Letras que dicen algo."}, {"palabra": "Medio", "significado": "Entre el principio y el final."}],
"carpeta": ["¿Qué palabra tiene la E dos veces?", "¿Cuántas E tiene PELOTA?", "¿Con qué vocal termina SILLA?"],
"respuestas_carpeta": [["ESTRELLA", "estrella", "Estrella"], ["1"], ["A", "a"]],
"soluciones": {"incompleto": "U. A.", "solo": "Por ejemplo: CAMA tiene A y A.", "carpeta": ["ESTRELLA.", "1.", "A."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras completando las vocales.",
"vas_a_ver": ["Palabras con huecos", "Completar con vocales", "Leer la palabra"],
"secciones": [
 S(1, "Faltan vocales", [
  P("A esta palabra le falta una vocal: <b>O _ O</b>. ¡Es OSO!"),
  IMG("Completar", "Le falta la vocal U.", FG.letras("UVA", ocultar=(0,), numeros=True)),
 ]),
 S(1, "Completar", [
  D("Completar", "Poner la letra que falta para que la palabra se lea bien."),
  P("_VA: le falta la <b>U</b>. UVA."),
  IMG("UVA completa", "U, V, A.", FG.letras("UVA", resaltar=(0,), numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la palabra. La vas a usar en la carpeta."),
  IMG("Faltan vocales", "Completá PELOTA.", FG.letras("PELOTA", ocultar=(1, 3, 5), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "ISLA", "planteo": "_SLA", "pasos": ["Digo la palabra: ISLA.", "Empieza con I.", "Escribo: ISLA."]},
"ejemplo_incompleto": {"titulo": "MESA", "planteo": "Completá.", "pasos": ["M _ S _ ."]},
"ejemplo_solo": {"titulo": "Tu palabra", "planteo": "Escribí una palabra y tapale las vocales. ¿Alguien la adivina?"},
"tip": {"titulo": "Probá en voz alta", "texto": "Decí la palabra con cada vocal y elegí la que suena bien."},
"ojo": ["Solo faltan vocales: A, E, I, O, U.", "Leé la palabra completa al final."],
"resumen": [{"titulo": "Hueco", "texto": "Falta una letra."}, {"titulo": "Completar", "texto": "Con una vocal."}, {"titulo": "Leer", "texto": "La palabra entera."}],
"glosario": [{"palabra": "Hueco", "significado": "Lugar vacío."}, {"palabra": "Completar", "significado": "Poner lo que falta."}],
"carpeta": ["¿Qué vocal va en el lugar 2?", "¿Qué vocal va en el lugar 4?", "¿Qué vocal va en el lugar 6?"],
"respuestas_carpeta": [["E", "e"], ["O", "o"], ["A", "a"]],
"soluciones": {"incompleto": "MESA.", "solo": "Por ejemplo: C_S_ (CASA).", "carpeta": ["E.", "O.", "A."]},
}

ACT = {
"1": [MC("¿CUÁL ES UNA VOCAL?", ["A", "M", "S"], "A", "LAS VOCALES SON A, E, I, O, U."),
      MC("¿CON QUÉ VOCAL EMPIEZA OSO?", ["O", "U", "A"], "O", "O-SO.")],
"2": [MC("¿QUÉ VOCALES TIENE SOFI?", ["O Y I", "O Y A", "U Y A"], "O Y I", "S-O-F-I: LA O Y LA I."),
      SA("¿CUÁNTAS VOCALES TIENE ANA?", ["2", "dos", "DOS"], "A Y A: 2.")],
"3": [MC("¿QUÉ PALABRA TIENE LA U?", ["LUNA", "MESA", "PATO"], "LUNA", "L-U-N-A."),
      MC("¿CON QUÉ VOCAL TERMINA PELOTA?", ["A", "O", "E"], "A", "PE-LO-TA.")],
"4": [SA("¿QUÉ VOCAL FALTA? _VA", ["U", "u"], "UVA."),
      SA("¿QUÉ VOCAL FALTA? M_SA", ["E", "e"], "MESA.")],
"5": [MC("RELÁMPAGO. ¿CUÁNTAS VOCALES HAY?", ["3", "5", "10"], "5", "A, E, I, O, U.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL NO ES VOCAL?", ["T", "I", "O"], "T", "LA T NO ES VOCAL.", tiempo=30),
      SA("RELÁMPAGO. ¿QUÉ VOCAL FALTA? _SLA", ["I", "i"], "ISLA.", tiempo=30),
      MC("RELÁMPAGO. ¿CON QUÉ VOCAL EMPIEZA ESTRELLA?", ["E", "A", "I"], "E", "E-STRE-LLA.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿CUÁNTAS VOCALES HAY?", ["5", "4", "6"], "5", "A, E, I, O, U.")],
 [1, MC("¿CUÁL ES UNA VOCAL?", ["U", "P", "L"], "U", "LA U ES VOCAL.")],
 [1, MC("¿CON QUÉ VOCAL EMPIEZA ISLA?", ["I", "E", "A"], "I", "I-SLA.")],
 [2, MC("¿QUÉ VOCALES TIENE TOMI?", ["O Y I", "A Y E", "U"], "O Y I", "T-O-M-I.")],
 [2, SA("¿CUÁNTAS VOCALES TIENE MATEO?", ["3", "tres", "TRES"], "A, E, O.")],
 [2, MC("¿QUÉ VOCAL SE REPITE EN ANA?", ["A", "N", "E"], "A", "A-N-A.")],
 [3, MC("¿QUÉ PALABRA TIENE LA O?", ["GLOBO", "MESA", "LUNA"], "GLOBO", "G-L-O-B-O.")],
 [3, MC("¿CON QUÉ VOCAL TERMINA VASO?", ["O", "A", "E"], "O", "VA-SO.")],
 [3, MC("¿HAY PALABRAS SIN VOCALES?", ["NO", "SÍ"], "NO", "TODAS TIENEN VOCALES.")],
 [4, SA("¿QUÉ VOCAL FALTA? _SO", ["O", "o"], "OSO.")],
 [4, SA("¿QUÉ VOCAL FALTA? L_NA", ["U", "u"], "LUNA.")],
 [4, SA("¿QUÉ VOCAL FALTA? CAS_", ["A", "a"], "CASA.")],
 [4, ORD("ORDENÁ LAS LETRAS DE UVA.", ["A", "U", "V"], ["U", "V", "A"], "U-V-A.")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: las vocales", "examen_titulo": "Nivel jefe: las vocales",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
