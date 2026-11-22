# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 10 · Rimas y poemas para leer. Genera mision-10.json.
Regla de primeros años. Poemas originales (escritos para la misión) y una rima tradicional ("Sana, sana").
Metáfora: la caja de música (las palabras que riman suenan igual al final, como una canción).
Niveles: 1 leer rimas conocidas · 2 encontrar palabras que riman · 3 leer un poema en voz alta · 4 copiar mi verso preferido."""
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
SAPO = ["EL SAPO PEPE", "SALTA Y SALTA,", "SE PONE UN GORRO", "¡Y NADA LE FALTA!"]
LUNA = ["LA LUNA DE NOCHE", "SALE A PASEAR,", "LA MIRA LA FOCA", "DESDE EL MAR."]

N1 = {**ESTILO,
"objetivo": "Vas a leer rimas que ya conocés.",
"vas_a_ver": ["Una rima conocida", "Leer con ritmo", "Decirla de memoria"],
"secciones": [
 S(1, "Una rima conocida", [
  P("Esta rima la dicen las familias cuando te duele algo."),
  IMG("Sana, sana", "Una rima de siempre.", FG.tiras(["SANA, SANA,", "COLITA DE RANA."], numeros=False, cols=1)),
 ]),
 S(1, "¿Qué es una rima?", [
  D("Rima", "Palabras que suenan igual al final: SANA y RANA."),
  IMG("Suenan igual", "SANA · RANA.", FG.nombres(["SANA", "RANA"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el poema. Lo vas a usar en la carpeta."),
  IMG("El sapo Pepe", "Cuatro renglones.", FG.tiras(SAPO, numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Leemos", "planteo": "SANA, SANA, COLITA DE RANA.", "pasos": ["SANA, SANA.", "COLITA DE RANA.", "SANA y RANA suenan igual."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Terminá la rima.", "pasos": ["SANA, SANA, COLITA DE ___."]},
"ejemplo_solo": {"titulo": "En familia", "planteo": "Preguntá en tu casa una rima que sepan. Decila en voz alta."},
"tip": {"titulo": "Con palmas", "texto": "Leé la rima marcando el ritmo con palmas."},
"ojo": ["Leé despacio, renglón por renglón.", "Las rimas se dicen con alegría."],
"resumen": [{"titulo": "Rima", "texto": "Suena igual al final."}, {"titulo": "Ritmo", "texto": "Con palmas."}, {"titulo": "Conocidas", "texto": "Las sabe tu familia."}],
"glosario": [{"palabra": "Rima", "significado": "Palabras que terminan con el mismo sonido."}, {"palabra": "Ritmo", "significado": "Manera de decir con golpes parejos."}],
"carpeta": ["¿Cómo se llama el sapo?", "¿Qué se pone el sapo?", "¿Qué palabra rima con SALTA?"],
"respuestas_carpeta": [low("PEPE"), ["UN GORRO", "GORRO", "un gorro", "gorro", "Un gorro"], low("FALTA")],
"carpeta_nivel": ["recordar", "aplicar", "analizar"],
"soluciones": {"incompleto": "RANA.", "solo": "Por ejemplo: SANA, SANA.", "carpeta": ["PEPE.", "UN GORRO.", "FALTA."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a encontrar palabras que riman.",
"vas_a_ver": ["Escuchar el final", "Parejas que riman", "Inventar rimas"],
"secciones": [
 S(1, "Escuchar el final", [
  P("<b>GATO</b> y <b>PATO</b> terminan igual: <b>-ATO</b>."),
  IMG("Riman", "El final en rojo.", FG.tiras(["GATO · PATO", "LUNA · CUNA"], numeros=False, cols=2)),
 ]),
 S(1, "Parejas que riman", [
  D("Riman", "Dos palabras riman si el final suena igual."),
  P("<b>FOCA</b> rima con <b>BOCA</b>. <b>FOCA</b> no rima con <b>SOL</b>."),
  IMG("Parejas", "Cada una con su pareja.", FG.tiras(["FOCA · BOCA", "MESA · FRESA", "SOL · CARACOL"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Riman?", "Escuchá el final.", FG.nombres(["RANA", "LANA", "MESA", "PATO"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "¿Riman?", "planteo": "LUNA y CUNA.", "pasos": ["LUNA termina en -UNA.", "CUNA termina en -UNA.", "¡Riman!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Buscá la pareja.", "pasos": ["GATO rima con P___."]},
"ejemplo_solo": {"titulo": "Inventá", "planteo": "Buscá una palabra que rime con TOMATE."},
"tip": {"titulo": "Escuchá el final", "texto": "Decí la palabra despacio y escuchá cómo termina."},
"ojo": ["No alcanza con empezar igual: GATO y GOMA no riman.", "Mirá el final, no el principio."],
"resumen": [{"titulo": "Final", "texto": "Suena igual."}, {"titulo": "Parejas", "texto": "GATO · PATO."}, {"titulo": "Inventar", "texto": "Buscar otra igual."}],
"glosario": [{"palabra": "Pareja", "significado": "Dos que van juntos."}, {"palabra": "Final", "significado": "La última parte."}],
"carpeta": ["¿Qué palabra rima con RANA?", "¿Qué palabra rima con GATO?", "¿Cuál no rima con ninguna?"],
"respuestas_carpeta": [low("LANA"), low("PATO"), low("MESA")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "PATO.", "solo": "Por ejemplo: CHOCOLATE.", "carpeta": ["LANA.", "PATO.", "MESA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a leer un poema en voz alta.",
"vas_a_ver": ["Los versos", "Leer con ritmo", "Leer para otros"],
"secciones": [
 S(1, "Un poema", [
  P("Un poema se escribe en renglones cortos."),
  IMG("La luna", "Un poema.", FG.tiras(LUNA, numeros=True, cols=1)),
 ]),
 S(1, "Los versos", [
  D("Verso", "Cada renglón del poema."),
  P("El poema de la luna tiene <b>4 versos</b>. <b>PASEAR</b> rima con <b>MAR</b>."),
  IMG("Riman", "Al final de los versos.", FG.nombres(["PASEAR", "MAR"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el poema. Lo vas a usar en la carpeta."),
  IMG("El sapo Pepe", "Leelo en voz alta.", FG.tiras(SAPO, numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Leemos", "planteo": "LA LUNA DE NOCHE.", "pasos": ["Leo el verso 1.", "Hago una pausa.", "Sigo con el verso 2."]},
"ejemplo_incompleto": {"titulo": "Contá", "planteo": "Contá los versos.", "pasos": ["El poema de la luna tiene ___ versos."]},
"ejemplo_solo": {"titulo": "Para tu familia", "planteo": "Leé el poema del sapo en voz alta en tu casa."},
"tip": {"titulo": "Pausa", "texto": "Al final de cada verso, una pausa cortita."},
"ojo": ["Leé fuerte y claro.", "No corras: cada verso con su pausa."],
"resumen": [{"titulo": "Poema", "texto": "Renglones cortos."}, {"titulo": "Verso", "texto": "Cada renglón."}, {"titulo": "Leer", "texto": "Con pausas."}],
"glosario": [{"palabra": "Poema", "significado": "Texto con versos y rimas."}, {"palabra": "Pausa", "significado": "Parar un ratito."}],
"carpeta": ["¿Cuántos versos tiene el poema?", "¿Qué palabra rima con FALTA?", "¿Qué dice el verso 3?"],
"respuestas_carpeta": [["4", "cuatro", "CUATRO"], low("SALTA"), ["SE PONE UN GORRO", "se pone un gorro", "Se pone un gorro"]],
"carpeta_nivel": ["aplicar", "analizar", "aplicar"],
"soluciones": {"incompleto": "4.", "solo": "Lo leíste con pausas.", "carpeta": ["4.", "SALTA.", "SE PONE UN GORRO."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a copiar tu verso preferido.",
"vas_a_ver": ["Elegir un verso", "Copiar bien", "Revisar"],
"secciones": [
 S(1, "Elegir", [
  P("Leé los poemas y elegí el verso que <b>más te gusta</b>."),
  IMG("Versos", "¿Cuál te gusta más?", FG.tiras(["EL SAPO PEPE", "SE PONE UN GORRO", "LA LUNA DE NOCHE", "DESDE EL MAR."], numeros=False, cols=2)),
 ]),
 S(1, "Copiar bien", [
  D("Copiar", "Escribir igual a lo que está escrito."),
  P("Mirás una palabra, la escribís, y mirás otra vez."),
  IMG("Palabra por palabra", "Con espacios.", FG.nombres(["SE", "PONE", "UN", "GORRO"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la copia. La vas a usar en la carpeta."),
  IMG("¿Está bien copiado?", "Compará con el poema.", FG.tiras(["LA LUNA DE NOCE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Copiamos", "planteo": "EL SAPO PEPE.", "pasos": ["Miro EL y lo escribo.", "Miro SAPO y lo escribo.", "Miro PEPE y lo escribo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Terminá de copiar.", "pasos": ["SALTA Y ___."]},
"ejemplo_solo": {"titulo": "Tu verso", "planteo": "Copiá tu verso preferido y hacé un dibujo al lado."},
"tip": {"titulo": "Con el dedo", "texto": "Seguí cada palabra con el dedo."},
"ojo": ["Dejá espacio entre palabras.", "Compará letra por letra al final."],
"resumen": [{"titulo": "Elegir", "texto": "El que más te gusta."}, {"titulo": "Copiar", "texto": "Palabra por palabra."}, {"titulo": "Revisar", "texto": "Comparar."}],
"glosario": [{"palabra": "Copiar", "significado": "Escribir igual."}, {"palabra": "Preferido", "significado": "El que más te gusta."}],
"carpeta": ["¿Qué palabra está mal copiada?", "¿Qué letra falta?", "Escribí la palabra bien."],
"respuestas_carpeta": [low("NOCE"), low("H"), low("NOCHE")],
"carpeta_nivel": ["error", "error", "error"],
"soluciones": {"incompleto": "SALTA.", "solo": "Por ejemplo: EL SAPO PEPE.", "carpeta": ["NOCE.", "H.", "NOCHE."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA RIMA CON SANA?", ["RANA", "SOPA", "SOL"], "RANA", "SANA · RANA.", n="aplicar"),
      SA("COMPLETÁ: SANA, SANA, COLITA DE ___", low("RANA"), "SANA, SANA, COLITA DE RANA.", n="recordar")],
"2": [MC("¿QUÉ PALABRA RIMA CON FOCA?", ["BOCA", "FOTO", "FIDEO"], "BOCA", "FOCA · BOCA.", n="aplicar"),
      MC("TOMI DICE QUE GATO Y GOMA RIMAN. ¿TIENE RAZÓN?", ["NO: EL FINAL ES DISTINTO", "SÍ: EMPIEZAN IGUAL", "SÍ: SON ANIMALES"], "NO: EL FINAL ES DISTINTO", "RIMAN SI EL FINAL SUENA IGUAL.", n="error")],
"3": [SA("¿CUÁNTOS VERSOS TIENE EL POEMA DE LA LUNA?", ["4", "cuatro", "CUATRO"], "4 RENGLONES.", n="aplicar"),
      MC("EN EL POEMA, ¿QUIÉN MIRA A LA LUNA?", ["LA FOCA", "EL SAPO", "EL GATO"], "LA FOCA", "LA MIRA LA FOCA.", n="analizar")],
"4": [ORD("ORDENÁ EL VERSO.", ["GORRO", "SE", "UN", "PONE"], ["SE", "PONE", "UN", "GORRO"], "SE PONE UN GORRO.", n="aplicar"),
      MC("¿CUÁL ESTÁ BIEN COPIADO? EL SAPO PEPE", ["EL SAPO PEPE", "EL SAPOPEPE", "EL SAPO PEPA"], "EL SAPO PEPE", "IGUAL AL POEMA.", n="error")],
"5": [MC("RELÁMPAGO. ¿QUÉ RIMA CON LUNA?", ["CUNA", "LANA", "LUPA"], "CUNA", "LUNA · CUNA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. CADA RENGLÓN DEL POEMA ES UN…", ["VERSO", "PUNTO", "CUENTO"], "VERSO", "VERSO.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿QUÉ RIMA CON PATO?", ["GATO", "gato", "Gato", "RATO", "rato", "Rato", "PLATO", "plato", "Plato", "ZAPATO", "zapato", "Zapato"], "POR EJEMPLO: GATO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿QUÉ RIMA CON MESA?", ["FRESA", "MASA", "MANO"], "FRESA", "MESA · FRESA.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UNA RIMA?", ["PALABRAS QUE TERMINAN IGUAL", "PALABRAS LARGAS", "PALABRAS CON PUNTO"], "PALABRAS QUE TERMINAN IGUAL", "SANA · RANA.", n="recordar")],
 [1, SA("COMPLETÁ LA RIMA: SANA, SANA, COLITA DE ___", low("RANA"), "RANA.", n="recordar")],
 [1, MC("EN EL POEMA, ¿QUÉ SE PONE EL SAPO PEPE?", ["UN GORRO", "UNA BOTA", "UN MOÑO"], "UN GORRO", "SE PONE UN GORRO.", n="aplicar")],
 [2, MC("¿QUÉ PALABRA RIMA CON LUNA?", ["CUNA", "LOMA", "LUPA"], "CUNA", "LUNA · CUNA.", n="aplicar")],
 [2, MC("¿QUÉ PAREJA RIMA?", ["MESA · FRESA", "MESA · MANO", "MESA · SOL"], "MESA · FRESA", "TERMINAN EN -ESA.", n="analizar")],
 [2, SA("ESCRIBÍ UNA PALABRA QUE RIME CON GATO.", ["PATO", "pato", "Pato", "RATO", "rato", "Rato", "PLATO", "plato", "Plato", "ZAPATO", "zapato", "Zapato", "DATO", "dato", "Dato"], "POR EJEMPLO: PATO.", n="aplicar")],
 [2, MC("SOFI DICE QUE SOL Y SOPA RIMAN. ¿POR QUÉ NO?", ["EL FINAL ES DISTINTO", "SON CORTAS", "EMPIEZAN IGUAL"], "EL FINAL ES DISTINTO", "RIMAN POR EL FINAL.", n="error")],
 [3, MC("CADA RENGLÓN DE UN POEMA SE LLAMA…", ["VERSO", "PUNTO", "TÍTULO"], "VERSO", "VERSO.", n="recordar")],
 [3, MC("EN EL POEMA DE LA LUNA, ¿QUÉ RIMA CON PASEAR?", ["MAR", "NOCHE", "FOCA"], "MAR", "PASEAR · MAR.", n="analizar")],
 [3, SA("¿CUÁNTOS VERSOS TIENE EL POEMA DEL SAPO?", ["4", "cuatro", "CUATRO"], "4.", n="aplicar")],
 [4, ORD("ORDENÁ EL VERSO.", ["NOCHE", "LA", "DE", "LUNA"], ["LA", "LUNA", "DE", "NOCHE"], "LA LUNA DE NOCHE.", n="aplicar")],
 [4, MC("TOMI COPIÓ: SALTA Y SALT. ¿QUÉ FALTA?", ["LA A AL FINAL", "UN PUNTO", "NADA"], "LA A AL FINAL", "SALTA Y SALTA.", n="error")],
 [4, MC("¿CUÁL ESTÁ BIEN COPIADO? DESDE EL MAR", ["DESDE EL MAR", "DESDEEL MAR", "DESDE EL MAL"], "DESDE EL MAR", "IGUAL AL POEMA.", n="aplicar")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 10, "estilo": "primeros",
     "practica": "Práctica general: rimas y poemas", "examen_titulo": "Nivel jefe: rimas y poemas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
