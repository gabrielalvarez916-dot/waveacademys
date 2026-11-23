# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 3 · Colours. Genera mision-3.json.
Regla de primeros años. Metáfora: el arcoíris de Sofi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 red, blue, yellow · 2 green, orange, pink · 3 black, white, brown · 4 what colour is it."""
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
def acepta(*ws):
    out = []
    for w in ws: out += [w, w.lower(), w.capitalize()]
    return out


N1 = {**ESTILO,
"objetivo": "Vas a decir rojo, azul y amarillo en inglés.",
"vas_a_ver": ["RED: rojo", "BLUE: azul", "YELLOW: amarillo"],
"secciones": [
 S(1, "Tres colores", [
  D("Color", "Cómo se ven las cosas: rojo, azul…"),
  P("En inglés, rojo es <b>RED</b>, azul es <b>BLUE</b> y amarillo es <b>YELLOW</b>."),
  IMG("Tres colores", "Cada color en inglés.", FG.tiras(["ROJO = RED", "AZUL = BLUE", "AMARILLO = YELLOW"], numeros=False, cols=1)),
 ]),
 S(1, "Cosas de colores", [
  P("Una frutilla es <b>RED</b>. El mar es <b>BLUE</b>. El sol es <b>YELLOW</b>."),
  IMG("Cosas", "Así se ven.", FG.tiras(["FRUTILLA: RED", "MAR: BLUE", "SOL: YELLOW"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cosas de Sofi. Las vas a usar en la carpeta."),
  IMG("Las cosas de Sofi", "¿De qué color son?", FG.tiras(["UN TOMATE", "EL CIELO", "UN POLLITO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi pinta", "planteo": "Sofi pinta un sol.", "pasos": ["Elige el amarillo.", "Pinta el sol.", "Dice: YELLOW!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La frutilla es ___.", "pasos": ["La frutilla es ___."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "Buscá algo azul y decí: BLUE!"},
"tip": {"titulo": "Señalá", "texto": "Señalá el color al decirlo."},
"ojo": ["RED es rojo.", "YELLOW es amarillo."],
"resumen": [{"titulo": "RED", "texto": "Rojo."}, {"titulo": "BLUE", "texto": "Azul."}, {"titulo": "YELLOW", "texto": "Amarillo."}],
"glosario": [{"palabra": "RED", "significado": "Rojo."}, {"palabra": "BLUE", "significado": "Azul."}],
"carpeta": ["El tomate es…", "El cielo es…", "Sofi dice que el pollito es BLUE. ¿De qué color es?"],
"respuestas_carpeta": [acepta("RED"), acepta("BLUE"), acepta("YELLOW", "ES YELLOW")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "RED.", "solo": "BLUE!", "carpeta": ["RED.", "BLUE.", "YELLOW."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a decir verde, naranja y rosa en inglés.",
"vas_a_ver": ["GREEN: verde", "ORANGE: naranja", "PINK: rosa"],
"secciones": [
 S(1, "Tres colores más", [
  D("Mezclar", "Juntar dos colores para hacer otro."),
  P("Verde es <b>GREEN</b>, naranja es <b>ORANGE</b> y rosa es <b>PINK</b>."),
  IMG("Tres colores", "Cada color en inglés.", FG.tiras(["VERDE = GREEN", "NARANJA = ORANGE", "ROSA = PINK"], numeros=False, cols=1)),
 ]),
 S(1, "Mezclamos", [
  P("Si mezclamos <b>BLUE</b> y <b>YELLOW</b>, sale <b>GREEN</b>."),
  IMG("Mezclas", "Dos colores hacen otro.", FG.tiras(["BLUE + YELLOW = GREEN", "RED + YELLOW = ORANGE", "RED + WHITE = PINK"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el jardín de Sofi. Lo vas a usar en la carpeta."),
  IMG("El jardín", "¿De qué color son?", FG.tiras(["EL PASTO", "UNA NARANJA", "UN CERDITO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi mezcla", "planteo": "Sofi tiene azul y amarillo.", "pasos": ["Los mezcla.", "Sale verde.", "Dice: GREEN!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El pasto es ___.", "pasos": ["El pasto es ___."]},
"ejemplo_solo": {"titulo": "A mezclar", "planteo": "Mezclá rojo y amarillo. ¿Qué color sale?"},
"tip": {"titulo": "Mirá la fruta", "texto": "ORANGE es el color de la naranja."},
"ojo": ["GREEN es verde.", "PINK es rosa."],
"resumen": [{"titulo": "GREEN", "texto": "Verde."}, {"titulo": "ORANGE", "texto": "Naranja."}, {"titulo": "PINK", "texto": "Rosa."}],
"glosario": [{"palabra": "GREEN", "significado": "Verde."}, {"palabra": "PINK", "significado": "Rosa."}],
"carpeta": ["El pasto es…", "La naranja es…", "Tomi dice: BLUE y YELLOW dan PINK. ¿Qué sale?"],
"respuestas_carpeta": [acepta("GREEN"), acepta("ORANGE"), acepta("GREEN", "SALE GREEN")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "GREEN.", "solo": "ORANGE.", "carpeta": ["GREEN.", "ORANGE.", "SALE GREEN."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a decir negro, blanco y marrón en inglés.",
"vas_a_ver": ["BLACK: negro", "WHITE: blanco", "BROWN: marrón"],
"secciones": [
 S(1, "Tres colores", [
  D("Oscuro y claro", "El negro es oscuro. El blanco es claro."),
  P("Negro es <b>BLACK</b>, blanco es <b>WHITE</b> y marrón es <b>BROWN</b>."),
  IMG("Tres colores", "Cada color en inglés.", FG.tiras(["NEGRO = BLACK", "BLANCO = WHITE", "MARRÓN = BROWN"], numeros=False, cols=1)),
 ]),
 S(1, "Animales", [
  P("La cebra es <b>BLACK</b> y <b>WHITE</b>. El oso es <b>BROWN</b>."),
  IMG("Animales", "Sus colores.", FG.tiras(["CEBRA: BLACK AND WHITE", "OSO: BROWN"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá estas cosas. Las vas a usar en la carpeta."),
  IMG("Cosas", "¿De qué color son?", FG.tiras(["LA NIEVE", "EL CHOCOLATE", "LA NOCHE"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El perro de Tomi", "planteo": "Tomi tiene un perro.", "pasos": ["Es marrón.", "Tomi lo mira.", "Dice: BROWN!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La leche es ___.", "pasos": ["La leche es ___."]},
"ejemplo_solo": {"titulo": "Tu ropa", "planteo": "Mirá tu ropa. ¿Hay algo BLACK o WHITE?"},
"tip": {"titulo": "BLACK y WHITE", "texto": "Son opuestos: oscuro y claro."},
"ojo": ["BLACK es negro.", "BROWN es marrón."],
"resumen": [{"titulo": "BLACK", "texto": "Negro."}, {"titulo": "WHITE", "texto": "Blanco."}, {"titulo": "BROWN", "texto": "Marrón."}],
"glosario": [{"palabra": "BLACK", "significado": "Negro."}, {"palabra": "WHITE", "significado": "Blanco."}],
"carpeta": ["La nieve es…", "El chocolate es…", "Tomi dice que la noche es WHITE. ¿De qué color es?"],
"respuestas_carpeta": [acepta("WHITE"), acepta("BROWN"), acepta("BLACK", "ES BLACK")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "WHITE.", "solo": "Tu ropa.", "carpeta": ["WHITE.", "BROWN.", "BLACK."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a preguntar y decir de qué color es algo.",
"vas_a_ver": ["La pregunta", "IT IS RED", "Jugar con colores"],
"secciones": [
 S(1, "¿De qué color es?", [
  D("Pregunta", "Lo que decimos para saber algo."),
  P("Preguntamos: <b>WHAT COLOUR IS IT?</b> Quiere decir: ¿de qué color es?"),
  IMG("La pregunta", "Para saber el color.", FG.tiras(["WHAT COLOUR IS IT?"], numeros=False, cols=1)),
 ]),
 S(1, "La respuesta", [
  P("Contestamos: <b>IT IS</b> y el color."),
  IMG("La respuesta", "Quiere decir: es…", FG.tiras(["IT IS RED = ES ROJO", "IT IS GREEN = ES VERDE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los juguetes de Tomi. Los vas a usar en la carpeta."),
  IMG("Los juguetes", "¿De qué color son?", FG.tiras(["PELOTA ROJA", "AUTO AZUL", "OSITO MARRÓN"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi pregunta", "planteo": "Sofi ve una flor rosa.", "pasos": ["Sofi: WHAT COLOUR IS IT?", "Tomi: IT IS PINK!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "IT ___ BLUE.", "pasos": ["IT ___ BLUE."]},
"ejemplo_solo": {"titulo": "A jugar", "planteo": "Preguntale a tu familia WHAT COLOUR IS IT?"},
"tip": {"titulo": "Señalá", "texto": "Señalá la cosa al preguntar."},
"ojo": ["IT IS es: es.", "COLOUR es color."],
"resumen": [{"titulo": "Pregunta", "texto": "WHAT COLOUR IS IT?"}, {"titulo": "Respuesta", "texto": "IT IS RED."}, {"titulo": "COLOUR", "texto": "Color."}],
"glosario": [{"palabra": "COLOUR", "significado": "Color."}, {"palabra": "IT IS", "significado": "Es."}],
"carpeta": ["La pelota es roja. ¿Qué decís?", "El auto es azul. ¿Qué decís?", "El osito es marrón. Tomi dice IT IS PINK. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("IT IS RED", "RED", "IT'S RED"), acepta("IT IS BLUE", "BLUE", "IT'S BLUE"), acepta("IT IS BROWN", "BROWN", "IT'S BROWN")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "IS.", "solo": "Tu juego.", "carpeta": ["IT IS RED.", "IT IS BLUE.", "IT IS BROWN."]},
}

ACT = {
"1": [MC("ROJO EN INGLÉS ES…", ["RED", "BLUE", "YELLOW"], "RED", "RED ES ROJO.", n="recordar"),
      MC("EL SOL ES…", ["YELLOW", "BLUE", "RED"], "YELLOW", "EL SOL ES YELLOW.", n="aplicar"),
      MC("EL MAR ES…", ["BLUE", "RED", "YELLOW"], "BLUE", "EL MAR ES BLUE.", n="aplicar")],
"2": [MC("EL PASTO ES…", ["GREEN", "PINK", "ORANGE"], "GREEN", "EL PASTO ES GREEN.", n="aplicar"),
      MC("BLUE + YELLOW = …", ["GREEN", "PINK", "ORANGE"], "GREEN", "SALE GREEN.", n="analizar")],
"3": [MC("LA NIEVE ES…", ["WHITE", "BLACK", "BROWN"], "WHITE", "LA NIEVE ES WHITE.", n="aplicar"),
      MC("TOMI DICE QUE EL CHOCOLATE ES WHITE. ¿QUÉ ESTÁ MAL?", ["ES BROWN", "ESTÁ BIEN", "ES PINK"], "ES BROWN", "EL CHOCOLATE ES BROWN.", n="error")],
"4": [MC("UNA FRUTILLA. WHAT COLOUR IS IT?", ["IT IS RED", "IT IS BLUE", "IT IS GREEN"], "IT IS RED", "ES RED.", n="aplicar"),
      ORD("ORDENÁ LA PREGUNTA.", ["IS", "WHAT", "IT", "COLOUR"], ["WHAT", "COLOUR", "IS", "IT"], "WHAT COLOUR IS IT?", n="aplicar")],
"5": [MC("RELÁMPAGO. AZUL EN INGLÉS ES…", ["BLUE", "RED", "PINK"], "BLUE", "BLUE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. VERDE EN INGLÉS ES…", ["GREEN", "BLACK", "WHITE"], "GREEN", "GREEN.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA NOCHE ES…", ["BLACK", "YELLOW", "PINK"], "BLACK", "BLACK.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. UNA NARANJA ES…", ["ORANGE", "BLUE", "WHITE"], "ORANGE", "ORANGE.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("AMARILLO EN INGLÉS ES…", ["YELLOW", "RED", "BLUE"], "YELLOW", "YELLOW ES AMARILLO.", n="recordar")],
 [1, SA("EL TOMATE ES ROJO. ESCRIBÍ EL COLOR EN INGLÉS.", acepta("RED"), "RED.", n="aplicar")],
 [1, MC("SOFI DICE QUE EL CIELO ES RED. ¿QUÉ ESTÁ MAL?", ["ES BLUE", "ESTÁ BIEN", "ES BLACK"], "ES BLUE", "EL CIELO ES BLUE.", n="error")],
 [2, MC("ROSA EN INGLÉS ES…", ["PINK", "GREEN", "ORANGE"], "PINK", "PINK ES ROSA.", n="recordar")],
 [2, SA("EL PASTO ES VERDE. ESCRIBÍ EL COLOR EN INGLÉS.", acepta("GREEN"), "GREEN.", n="aplicar")],
 [2, MC("RED + YELLOW = …", ["ORANGE", "GREEN", "BLUE"], "ORANGE", "SALE ORANGE.", n="analizar")],
 [3, MC("NEGRO EN INGLÉS ES…", ["BLACK", "WHITE", "BROWN"], "BLACK", "BLACK ES NEGRO.", n="recordar")],
 [3, SA("EL OSO ES MARRÓN. ESCRIBÍ EL COLOR EN INGLÉS.", acepta("BROWN"), "BROWN.", n="aplicar")],
 [3, MC("LA CEBRA ES…", ["BLACK AND WHITE", "RED AND BLUE", "GREEN"], "BLACK AND WHITE", "NEGRO Y BLANCO.", n="aplicar")],
 [4, MC("WHAT COLOUR IS IT QUIERE DECIR…", ["¿DE QUÉ COLOR ES?", "¿CÓMO TE LLAMÁS?", "¿CUÁNTOS AÑOS TENÉS?"], "¿DE QUÉ COLOR ES?", "COLOUR ES COLOR.", n="recordar")],
 [4, MC("UN POLLITO. WHAT COLOUR IS IT?", ["IT IS YELLOW", "IT IS BLACK", "IT IS GREEN"], "IT IS YELLOW", "ES YELLOW.", n="aplicar")],
 [4, MC("UNA HOJA VERDE. TOMI DICE IT IS PINK. ¿QUÉ DEBERÍA DECIR?", ["IT IS GREEN", "IT IS RED", "ESTÁ BIEN"], "IT IS GREEN", "LA HOJA ES GREEN.", n="error")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: Colours", "examen_titulo": "Nivel jefe: Colours",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
