# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 8 · La oración. Genera mision-8.json.
Regla de primeros años y vía fonológica. Solo palabras con letras ya vistas (vocales, M, P, S, L, T, N, D, C, F, B).
Metáfora: el tren de las palabras (cada palabra es un vagón; la mayúscula arranca el tren y el punto lo frena).
Niveles: 1 palabras que forman oraciones · 2 mayúscula y punto · 3 ordenar palabras · 4 escribir mis primeras oraciones."""
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
"objetivo": "Vas a ver que las palabras juntas forman oraciones.",
"vas_a_ver": ["El tren de las palabras", "Contar palabras", "Oración o no"],
"secciones": [
 S(1, "El tren de las palabras", [
  P("Cada palabra es un <b>vagón</b>. Juntas forman una <b>oración</b>."),
  IMG("Un tren de palabras", "Cuatro vagones, cuatro palabras.", FG.nombres(["EL", "OSO", "TOMA", "SOPA."], cols=4)),
 ]),
 S(1, "Una oración dice algo", [
  D("La oración", "Es un grupo de palabras que dice algo completo."),
  P("<b>EL SOL SALE.</b> Dice algo. <b>SOL EL</b> no dice nada."),
  IMG("Oración", "Se entiende.", FG.tiras(["EL SOL SALE.", "MAMÁ MIMA A SOFI."], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la oración. La vas a usar en la carpeta."),
  IMG("Contá los vagones", "Una palabra en cada cartel.", FG.nombres(["LA", "FOCA", "TOMA", "UN", "COCO."], cols=5)),
 ]),
],
"ejemplo_completo": {"titulo": "Contamos", "planteo": "EL OSO TOMA SOPA.", "pasos": ["EL: 1.", "OSO: 2. TOMA: 3.", "SOPA: 4. Son 4 palabras."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Contá las palabras.", "pasos": ["EL SOL SALE: ___ palabras."]},
"ejemplo_solo": {"titulo": "Con aplausos", "planteo": "Decí MAMÁ MIMA A SOFI. Dá un aplauso por palabra."},
"tip": {"titulo": "Un aplauso", "texto": "Un aplauso por cada palabra."},
"ojo": ["Las palabras chiquitas también cuentan: A, LA, UN.", "Entre palabra y palabra hay un espacio."],
"resumen": [{"titulo": "Vagón", "texto": "Cada palabra."}, {"titulo": "Tren", "texto": "La oración."}, {"titulo": "Dice algo", "texto": "Se entiende."}],
"glosario": [{"palabra": "Oración", "significado": "Palabras juntas que dicen algo."}, {"palabra": "Vagón", "significado": "Cada parte de un tren."}],
"carpeta": ["¿Cuántas palabras tiene la oración?", "¿Cuál es la primera palabra?", "¿Cuál es la última palabra?"],
"respuestas_carpeta": [["5", "cinco", "CINCO"], low("LA"), low("COCO")],
"soluciones": {"incompleto": "3.", "solo": "4 aplausos.", "carpeta": ["5.", "LA.", "COCO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver cómo empieza y cómo termina una oración.",
"vas_a_ver": ["La mayúscula", "El punto", "Revisar la oración"],
"secciones": [
 S(1, "Empieza con mayúscula", [
  P("La oración <b>arranca</b> con mayúscula: la primera letra, grande."),
  IMG("La primera letra", "Pintada en amarillo.", FG.letras("PAPÁ", resaltar=(0,))),
 ]),
 S(1, "Termina con punto", [
  D("El punto", "Es un puntito al final. Dice: la oración terminó."),
  P("Como el tren que <b>frena</b> en la estación."),
  IMG("El punto", "Al final, el punto.", FG.letras("SOL.", resaltar=(3,))),
 ]),
 S(2, "Para practicar", [
  P("Mirá la oración. La vas a usar en la carpeta."),
  IMG("Oración", "Mayúscula y punto.", FG.tiras(["LA NUBE ES LINDA."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Revisamos", "planteo": "EL PATO NADA.", "pasos": ["Empieza con mayúscula: E.", "Termina con punto.", "¡Está bien escrita!"]},
"ejemplo_incompleto": {"titulo": "Falta algo", "planteo": "Completá.", "pasos": ["LA FOCA TOMA SOPA___"]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá una oración en un cuento. Señalá el punto."},
"tip": {"titulo": "Arranca y frena", "texto": "Mayúscula: arranca. Punto: frena."},
"ojo": ["El punto va pegado a la última palabra.", "Sin punto, la oración no terminó."],
"resumen": [{"titulo": "Mayúscula", "texto": "Al principio."}, {"titulo": "Punto", "texto": "Al final."}, {"titulo": "Revisar", "texto": "Mirar las dos cosas."}],
"glosario": [{"palabra": "Mayúscula", "significado": "Letra grande del comienzo."}, {"palabra": "Punto", "significado": "Marca del final."}],
"carpeta": ["¿Con qué letra empieza la oración?", "¿Qué hay al final de la oración?", "¿Cuál es la última palabra?"],
"respuestas_carpeta": [low("L"), ["PUNTO", "punto", "Punto", "UN PUNTO", "un punto", "Un punto", "."], low("LINDA")],
"soluciones": {"incompleto": "Falta el punto: LA FOCA TOMA SOPA.", "solo": "El punto está al final.", "carpeta": ["L.", "UN PUNTO.", "LINDA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ordenar palabras para armar oraciones.",
"vas_a_ver": ["Palabras mezcladas", "Ordenar", "Leer para revisar"],
"secciones": [
 S(1, "Se mezclaron los vagones", [
  P("<b>SOPA TOMA OSO EL</b>. ¡No se entiende!"),
  IMG("Mezcladas", "Así no dice nada.", FG.nombres(["SOPA", "TOMA", "OSO", "EL"], cols=4)),
 ]),
 S(1, "Los ponemos en orden", [
  D("Ordenar", "Poner cada palabra en su lugar para que se entienda."),
  P("Primero: ¿quién? <b>EL OSO</b>. Después: ¿qué hace? <b>TOMA SOPA</b>."),
  IMG("En orden", "Ahora se entiende.", FG.nombres(["EL", "OSO", "TOMA", "SOPA."], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Ordená", "Están mezcladas.", FG.nombres(["SALE", "SOL", "EL"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenamos", "planteo": "MIMA SOFI MAMÁ A", "pasos": ["¿Quién? MAMÁ.", "¿Qué hace? MIMA A SOFI.", "MAMÁ MIMA A SOFI."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "NADA PATO EL", "pasos": ["EL ___ NADA."]},
"ejemplo_solo": {"titulo": "Leé", "planteo": "Ordená y leé en voz alta: BOTE EL FLOTA."},
"tip": {"titulo": "¿Quién y qué hace?", "texto": "Primero quién. Después qué hace."},
"ojo": ["Leé la oración para ver si se entiende.", "La palabra con punto va al final."],
"resumen": [{"titulo": "Mezcladas", "texto": "No se entiende."}, {"titulo": "Ordenar", "texto": "Quién y qué hace."}, {"titulo": "Revisar", "texto": "Leer otra vez."}],
"glosario": [{"palabra": "Ordenar", "significado": "Poner cada cosa en su lugar."}, {"palabra": "Mezclado", "significado": "Todo revuelto."}],
"carpeta": ["¿Qué palabra va primero?", "¿Qué palabra va al final?", "Escribí la oración ordenada."],
"respuestas_carpeta": [low("EL"), low("SALE"), ["EL SOL SALE.", "EL SOL SALE", "el sol sale.", "el sol sale", "El sol sale.", "El sol sale"]],
"soluciones": {"incompleto": "PATO.", "solo": "EL BOTE FLOTA.", "carpeta": ["EL.", "SALE.", "EL SOL SALE."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir tus primeras oraciones.",
"vas_a_ver": ["Pensar qué decir", "Escribir", "Revisar"],
"secciones": [
 S(1, "Pensar y decir", [
  P("Primero lo <b>decís</b> en voz alta: <b>MI PAPÁ TOMA MATE.</b>"),
  IMG("Pasos", "Pienso, digo, escribo.", FG.tiras(["1. PIENSO", "2. LO DIGO", "3. LO ESCRIBO", "4. LO LEO"], numeros=False, cols=2)),
 ]),
 S(1, "Escribir con espacios", [
  D("Espacio", "Lugar vacío entre palabra y palabra."),
  P("<b>ELSOLSALE</b> no se lee. <b>EL SOL SALE.</b> sí."),
  IMG("Con espacios", "Una palabra en cada cartel.", FG.nombres(["EL", "SOL", "SALE."], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la oración. La vas a usar en la carpeta."),
  IMG("Revisá", "¿Qué le falta?", FG.tiras(["mi mamá toma té"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Escribimos", "planteo": "Quiero contar algo de mi pato.", "pasos": ["Digo: MI PATO NADA.", "Escribo con espacios.", "Pongo mayúscula y punto."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Terminá la oración.", "pasos": ["EL OSO TOMA ___."]},
"ejemplo_solo": {"titulo": "Tu oración", "planteo": "Escribí una oración sobre tu mascota o tu familia. Leela para revisar."},
"tip": {"titulo": "Leela otra vez", "texto": "Al terminar, leé tu oración en voz alta."},
"ojo": ["Dejá espacio entre las palabras.", "No te olvides el punto."],
"resumen": [{"titulo": "Pensar", "texto": "Decir en voz alta."}, {"titulo": "Escribir", "texto": "Con espacios."}, {"titulo": "Revisar", "texto": "Mayúscula y punto."}],
"glosario": [{"palabra": "Espacio", "significado": "Lugar vacío entre palabras."}, {"palabra": "Revisar", "significado": "Mirar otra vez para arreglar."}],
"carpeta": ["¿Cuántas palabras tiene la oración?", "¿Qué le falta al final?", "Escribila bien."],
"respuestas_carpeta": [["4", "cuatro", "CUATRO"], ["PUNTO", "punto", "Punto", "EL PUNTO", "el punto", "El punto", "UN PUNTO", "un punto", "."], ["MI MAMÁ TOMA TÉ.", "MI MAMA TOMA TE.", "Mi mamá toma té.", "mi mamá toma té.", "MI MAMÁ TOMA TÉ", "Mi mamá toma té"]],
"soluciones": {"incompleto": "Por ejemplo: SOPA.", "solo": "Por ejemplo: MI PAPÁ TOMA MATE.", "carpeta": ["4.", "EL PUNTO.", "MI MAMÁ TOMA TÉ."]},
}

ACT = {
"1": [MC("¿CUÁL ES UNA ORACIÓN?", ["EL SOL SALE.", "SOL EL", "SALE SOL"], "EL SOL SALE.", "SE ENTIENDE."),
      SA("¿CUÁNTAS PALABRAS TIENE? EL OSO TOMA SOPA.", ["4", "cuatro", "CUATRO"], "EL, OSO, TOMA, SOPA.")],
"2": [MC("¿CÓMO TERMINA UNA ORACIÓN?", ["CON UN PUNTO", "CON UNA A", "CON UN ESPACIO"], "CON UN PUNTO", "EL PUNTO VA AL FINAL."),
      MC("TOMI ESCRIBIÓ: el pato nada. ¿QUÉ LE FALTA AL PRINCIPIO?", ["LA MAYÚSCULA", "EL PUNTO", "UN ESPACIO"], "LA MAYÚSCULA", "El pato nada.")],
"3": [ORD("ORDENÁ LA ORACIÓN.", ["SALE.", "EL", "SOL"], ["EL", "SOL", "SALE."], "EL SOL SALE."),
      MC("¿QUÉ PALABRA VA PRIMERO? PATO NADA EL", ["EL", "PATO", "NADA"], "EL", "EL PATO NADA.")],
"4": [SA("TERMINÁ LA ORACIÓN: EL OSO TOMA ___.", ["SOPA", "sopa", "Sopa", "LECHE", "leche", "Leche", "TÉ", "té", "TE", "te", "AGUA", "agua", "Agua", "MATE", "mate", "Mate", "JUGO", "jugo", "Jugo"], "POR EJEMPLO: SOPA."),
      MC("¿CUÁL TIENE ESPACIOS?", ["MI PAPÁ TOMA MATE.", "MIPAPÁTOMAMATE.", "MI PAPÁTOMA MATE."], "MI PAPÁ TOMA MATE.", "UN ESPACIO ENTRE PALABRAS.")],
"5": [MC("RELÁMPAGO. ¿CON QUÉ EMPIEZA UNA ORACIÓN?", ["CON MAYÚSCULA", "CON PUNTO", "CON ESPACIO"], "CON MAYÚSCULA", "ARRANCA CON MAYÚSCULA.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁNTAS PALABRAS? MAMÁ MIMA A SOFI.", ["4", "3", "5"], "4", "MAMÁ, MIMA, A, SOFI.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES UNA ORACIÓN?", ["LA FOCA NADA.", "FOCA LA", "NADA FOCA LA"], "LA FOCA NADA.", "SE ENTIENDE.", tiempo=30),
      SA("RELÁMPAGO. ¿QUÉ VA AL FINAL DE LA ORACIÓN?", ["PUNTO", "punto", "Punto", "EL PUNTO", "el punto", "UN PUNTO", "un punto", "."], "EL PUNTO.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿CUÁL ES UNA ORACIÓN?", ["MAMÁ MIMA A SOFI.", "MIMA SOFI", "A MAMÁ"], "MAMÁ MIMA A SOFI.", "DICE ALGO COMPLETO.")],
 [1, SA("¿CUÁNTAS PALABRAS TIENE? LA FOCA TOMA UN COCO.", ["5", "cinco", "CINCO"], "LA, FOCA, TOMA, UN, COCO.")],
 [1, MC("CADA VAGÓN DEL TREN ES…", ["UNA PALABRA", "UNA LETRA", "UN PUNTO"], "UNA PALABRA", "CADA PALABRA ES UN VAGÓN.")],
 [2, MC("¿QUÉ HAY AL FINAL DE UNA ORACIÓN?", ["UN PUNTO", "UNA MAYÚSCULA", "NADA"], "UN PUNTO", "EL PUNTO FRENA EL TREN.")],
 [2, MC("¿DÓNDE VA EL PUNTO?", ["AL FINAL", "AL PRINCIPIO", "EN EL MEDIO"], "AL FINAL", "EL PUNTO FRENA EL TREN.")],
 [2, MC("¿DÓNDE VA LA MAYÚSCULA?", ["AL PRINCIPIO", "AL FINAL", "EN EL MEDIO"], "AL PRINCIPIO", "ARRANCA CON MAYÚSCULA.")],
 [3, ORD("ORDENÁ LA ORACIÓN.", ["SOPA.", "OSO", "EL", "TOMA"], ["EL", "OSO", "TOMA", "SOPA."], "EL OSO TOMA SOPA.")],
 [3, MC("¿QUÉ PALABRA VA AL FINAL? NADA LA FOCA", ["NADA", "LA", "FOCA"], "NADA", "LA FOCA NADA.")],
 [3, ORD("ORDENÁ LA ORACIÓN.", ["SOFI.", "MIMA", "MAMÁ", "A"], ["MAMÁ", "MIMA", "A", "SOFI."], "MAMÁ MIMA A SOFI.")],
 [4, SA("TERMINÁ LA ORACIÓN: LA FOCA TOMA ___.", ["SOPA", "sopa", "Sopa", "AGUA", "agua", "Agua", "LECHE", "leche", "Leche", "TÉ", "té", "TE", "te", "UN COCO", "un coco", "COCO", "coco", "Coco"], "POR EJEMPLO: SOPA.")],
 [4, MC("¿QUÉ LE FALTA? mi papá toma mate", ["MAYÚSCULA Y PUNTO", "NADA", "MÁS PALABRAS"], "MAYÚSCULA Y PUNTO", "Mi papá toma mate.")],
 [4, MC("¿CUÁL TIENE ESPACIOS?", ["EL SOL SALE.", "ELSOLSALE.", "ELSOL SALE."], "EL SOL SALE.", "UN ESPACIO ENTRE PALABRAS.")],
 [4, SA("¿QUÉ VA ENTRE PALABRA Y PALABRA?", ["ESPACIO", "espacio", "Espacio", "UN ESPACIO", "un espacio", "Un espacio"], "UN ESPACIO.")],
]
for N, t in ((N1, ["aplicar", "recordar", "recordar"]), (N2, ["recordar", "recordar", "aplicar"]), (N3, ["aplicar", "aplicar", "aplicar"]), (N4, ["aplicar", "error", "error"])):
    N["carpeta_nivel"] = t
for k, t in {"1": ["analizar", "aplicar"], "2": ["recordar", "error"], "3": ["aplicar", "aplicar"], "4": ["aplicar", "analizar"], "5": ["recordar", "aplicar", "analizar", "recordar"]}.items():
    for q, n in zip(ACT[k], t): q["n"] = n
for it, n in zip(EXAMEN, ["analizar", "aplicar", "recordar", "recordar", "recordar", "recordar", "aplicar", "aplicar", "aplicar", "aplicar", "error", "analizar", "recordar"]):
    it[1]["n"] = n
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 8, "estilo": "primeros",
     "practica": "Práctica general: la oración", "examen_titulo": "Nivel jefe: la oración",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
