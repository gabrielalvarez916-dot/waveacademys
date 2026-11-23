# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 3 · Colours: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: el arcoíris de Sofi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 3
TIT = {1: 'Red, blue and yellow', 2: 'Green, orange and pink', 3: 'Black, white and brown', 4: 'What colour is it?'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SOFI PINTA UN ARCOÍRIS!", "bajada": "Y dice los colores en inglés", "emoji": "🌈", "titulo": "COLOURS", "sub": "rojo, azul y amarillo",
  "voz": ["¡Último momento! Sofi pinta un *arcoíris*.", "Y dice los colores en *inglés*.", "Hoy: *rojo, azul y amarillo en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "RED", "emoji": "🔴", "trad": "rojo", "pron": "red"}, {"palabra": "BLUE", "emoji": "🔵", "trad": "azul", "pron": "blú"}, {"palabra": "YELLOW", "emoji": "🟡", "trad": "amarillo", "pron": "iélou"}],
  "voz": ["Red!", "Blue!", "Yellow!"], "voz_en": [0, 1, 2]},
 {"t": "bloques", "titulo": "COSAS DE COLORES", "items": [{"cab": "🍓", "txt": "RED"}, {"cab": "🌊", "txt": "BLUE"}, {"cab": "🌞", "txt": "YELLOW"}],
  "voz": ["Miramos cosas de colores.", "La frutilla es roja: red!", "El mar es azul: blue!", "El sol es amarillo: yellow!"]},
 {"t": "pregunta", "pregunta": "El sol es…", "opciones": ["YELLOW", "BLUE", "RED"], "correcta": 0,
  "voz": ["Ahora vos. Mirá el sol.", "¿De qué color es en inglés?", "Yellow!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "SEÑALÁ", "texto": "Señalá el color al decirlo", "emoji": "👉",
  "voz": ["Truco: *señalá* el color al decirlo."]},
 {"t": "resumen", "items": [["RED", "rojo"], ["BLUE", "azul"], ["YELLOW", "amarillo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Red, blue, yellow!", "Rojo, azul y *amarillo*.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "gancho", "emoji": "🎨", "final": "🤔", "titulo": "MIX COLOURS", "sub": "verde, naranja y rosa",
  "voz": ["Sofi mezcla dos pinturas.", "¿Qué color va a salir?", "Hoy: *verde, naranja y rosa en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "GREEN", "emoji": "🟢", "trad": "verde", "pron": "grín"}, {"palabra": "ORANGE", "emoji": "🟠", "trad": "naranja", "pron": "órinch"}, {"palabra": "PINK", "emoji": "🌸", "trad": "rosa", "pron": "pink"}],
  "voz": ["Green!", "Orange!", "Pink!"], "voz_en": [0, 1, 2]},
 {"t": "matriz", "titulo": "MEZCLAMOS", "celdas": [{"cab": "🔵 + 🟡", "txt": "GREEN"}, {"cab": "🔴 + 🟡", "txt": "ORANGE"}, {"cab": "🔴 + ⚪", "txt": "PINK"}, {"cab": "🐸", "txt": "GREEN"}],
  "voz": ["Mezclamos colores.", "Azul y amarillo dan verde: green!", "Rojo y amarillo dan naranja: orange!", "Rojo y blanco dan rosa: pink!", "¡La rana es green!"]},
 {"t": "pregunta", "pregunta": "Azul y amarillo dan…", "opciones": ["GREEN", "PINK", "ORANGE"], "correcta": 0,
  "voz": ["Ahora vos. Mezclá azul y amarillo.", "¿Qué color sale en inglés?", "Green!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "LA FRUTA", "texto": "ORANGE es el color de la naranja", "emoji": "🍊",
  "voz": ["Truco: orange es el color de la *naranja*."]},
 {"t": "resumen", "items": [["GREEN", "verde"], ["ORANGE", "naranja"], ["PINK", "rosa"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Green, orange, pink!", "Verde, naranja y *rosa*.", CIERRE], "voz_en": [1]},
]
N3 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🏞️", "lineas": ["Tomi va al zoológico.", "Ve una cebra y un oso.", "¿De qué color son?"], "titulo": "BLACK AND WHITE", "sub": "negro, blanco y marrón",
  "voz": ["Tomi va al *zoológico*.", "Ve una cebra y un oso.", "¿De qué color son?", "Hoy: *negro, blanco y marrón en inglés*."]},
 {"t": "zoom", "niveles": [{"emoji": "🦓", "txt": "ZEBRA"}, {"emoji": "⬛", "txt": "BLACK"}, {"emoji": "⬜", "txt": "WHITE"}],
  "voz": ["Miramos la cebra de cerca.", "Black! Negro.", "White! Blanco."], "voz_en": []},
 {"t": "venn", "a": "BLACK", "b": "WHITE", "itemsA": ["NOCHE", "CUERVO"], "itemsB": ["NIEVE", "LECHE"], "ambos": ["CEBRA", "PANDA"],
  "voz": ["Separamos cosas por su color.", "La noche y el cuervo son negros.", "La nieve y la leche son blancas.", "¡La cebra y el panda tienen los dos!"]},
 {"t": "pregunta", "pregunta": "El chocolate es…", "opciones": ["BROWN", "WHITE", "PINK"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el chocolate.", "¿De qué color es en inglés?", "Brown!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "OPUESTOS", "texto": "BLACK es oscuro y WHITE es claro", "emoji": "🌗",
  "voz": ["Recordá: negro es *oscuro* y blanco es *claro*."]},
 {"t": "resumen", "items": [["BLACK", "negro"], ["WHITE", "blanco"], ["BROWN", "marrón"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Black, white, brown!", "Negro, blanco y *marrón*.", CIERRE], "voz_en": [1]},
]
N4 = [
 {"t": "chat", "contacto": SOFI, "mensajes": [{"yo": False, "txt": "WHAT COLOUR IS IT? 🎈"}, {"yo": True, "txt": "IT IS RED!"}, {"yo": False, "txt": "¡Muy bien!"}], "titulo": "WHAT COLOUR IS IT?", "sub": "¿de qué color es?",
  "voz": ["Sofi le manda una foto a Tomi.", "What colour is it?", "Quiere saber de qué *color* es.", "Hoy: *preguntar el color en inglés*."], "voz_en": [1]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "TOMI", "emoji": "👦"}], "lineas": [{"quien": 0, "txt": "WHAT COLOUR IS IT?", "trad": "¿de qué color es?"}, {"quien": 1, "txt": "IT IS GREEN.", "trad": "es verde"}, {"quien": 0, "txt": "YES! VERY GOOD!", "trad": "¡sí! ¡muy bien!"}],
  "voz": ["What colour is it?", "It is green.", "Yes! Very good!"], "voz_en": [0, 1, 2]},
 {"t": "corrige", "titulo": "¿ESTÁ BIEN?", "cambios": [{"antes": "🍓 IT IS BLUE", "despues": "🍓 IT IS RED", "motivo": "la frutilla es roja"}, {"antes": "🌞 IT IS BLACK", "despues": "🌞 IT IS YELLOW", "motivo": "el sol es amarillo"}],
  "voz": ["Tomi se equivocó. Lo arreglamos.", "La frutilla: it is red!", "El sol: it is yellow!"], "voz_en": []},
 {"t": "pregunta", "pregunta": "Una frutilla. WHAT COLOUR IS IT?", "opciones": ["IT IS RED", "IT IS BLUE", "IT IS GREEN"], "correcta": 0,
  "voz": ["Ahora vos. Mirá la frutilla.", "¿Qué contestás?", "It is red!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "SEÑALÁ", "texto": "Señalá la cosa al preguntar", "emoji": "👉",
  "voz": ["Truco: *señalá* la cosa al preguntar."]},
 {"t": "resumen", "items": [["WHAT COLOUR IS IT?", "¿de qué color es?"], ["IT IS…", "es…"], ["COLOUR", "color"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "What colour is it?", "Contestamos con el *color*.", "It is red!", CIERRE], "voz_en": [1, 3]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
