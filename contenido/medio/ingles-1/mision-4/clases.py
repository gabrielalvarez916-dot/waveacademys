# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 4 · My Things: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: la mochila de Tomi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 4
TIT = {1: 'Pencil, book and bag', 2: 'Listen and do: simple commands', 3: 'Is it a pen? Yes, it is', 4: 'In and on: where is it?'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "reto", "texto": "¿Sabés cómo se dice libro en inglés?", "segundos": 6, "respuesta": "¡BOOK!", "emoji": "📘", "titulo": "MY THINGS", "sub": "mis útiles",
  "voz": ["Desafío: ¿cómo se dice libro en inglés?", "Book!", "Hoy: *mis útiles en inglés*."], "voz_en": [1]},
 {"t": "vocab", "items": [{"palabra": "PENCIL", "emoji": "✏️", "trad": "lápiz", "pron": "pénsil"}, {"palabra": "BOOK", "emoji": "📘", "trad": "libro", "pron": "buk"}, {"palabra": "BAG", "emoji": "🎒", "trad": "mochila", "pron": "bag"}, {"palabra": "PEN", "emoji": "🖊️", "trad": "lapicera", "pron": "pen"}],
  "voz": ["Pencil!", "Book!", "Bag!", "Pen!"], "voz_en": [0, 1, 2, 3]},
 {"t": "partes", "emoji": "🎒", "titulo": "MY BAG", "partes": [{"txt": "PENCIL", "x": -0.6, "y": -0.5}, {"txt": "BOOK", "x": 0.6, "y": -0.5}, {"txt": "PEN", "x": -0.6, "y": 0.5}, {"txt": "RUBBER", "x": 0.6, "y": 0.5}],
  "voz": ["Abrimos la mochila de Tomi.", "Pencil!", "Book!", "Pen!", "Rubber!"], "voz_en": [1, 2, 3, 4]},
 {"t": "pregunta", "pregunta": "¿Cómo se dice mochila?", "opciones": ["BAG", "BOOK", "PEN"], "correcta": 0,
  "voz": ["Ahora vos. Mirá la mochila.", "¿Cómo se dice en inglés?", "Bag!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "TOCÁ Y DECÍ", "texto": "Tocá cada útil al nombrarlo", "emoji": "✋",
  "voz": ["Truco: *tocá* cada útil al nombrarlo."]},
 {"t": "resumen", "items": [["PENCIL", "lápiz"], ["BOOK", "libro"], ["BAG", "mochila"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Pencil, book, bag!", "Lápiz, libro y *mochila*.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡LA MAESTRA HABLA EN INGLÉS!", "bajada": "Y los chicos la entienden", "emoji": "👩‍🏫", "titulo": "LISTEN AND DO", "sub": "escuchar y hacer",
  "voz": ["¡Último momento! La maestra habla en *inglés*.", "¡Y los chicos la entienden!", "Hoy: *escuchar y hacer*."]},
 {"t": "flujo", "titulo": "ESCUCHÁ Y HACÉ", "items": ["STAND UP!", "SIT DOWN!", "OPEN YOUR BOOK!", "CLOSE YOUR BOOK!"],
  "voz": ["Stand up!", "Sit down!", "Open your book!", "Close your book!"], "voz_en": [0, 1, 2, 3]},
 {"t": "comparar", "a": {"cab": "OPEN", "texto": "Abrir el libro", "emoji": "📖"}, "b": {"cab": "CLOSE", "texto": "Cerrar el libro", "emoji": "📕"}, "signo": "vs",
  "voz": ["Abrir y cerrar son opuestos.", "Open es *abrir*.", "Close es *cerrar*."]},
 {"t": "pregunta", "pregunta": "La maestra dice SIT DOWN. ¿Qué hacés?", "opciones": ["ME SIENTO", "ME PARO", "ABRO EL LIBRO"], "correcta": 0,
  "voz": ["Ahora vos. La maestra dice algo.", "Sit down! ¿Qué hacés?", "¡Te *sentás*!"]},
 {"t": "consejo", "titulo": "ESCUCHÁ BIEN", "texto": "Primero escuchá, después hacé", "emoji": "👂",
  "voz": ["Truco: primero *escuchá*, después hacé."]},
 {"t": "resumen", "items": [["STAND UP", "pararse"], ["SIT DOWN", "sentarse"], ["OPEN / CLOSE", "abrir y cerrar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Stand up! Sit down!", "Open and close!", CIERRE], "voz_en": [1, 2]},
]
N3 = [
 {"t": "gancho", "emoji": "🙈", "final": "❓", "titulo": "IS IT A PEN?", "sub": "adivinar en inglés",
  "voz": ["Sofi esconde algo en la mano.", "¿Qué será? ¡A adivinar!", "Hoy: *adivinar en inglés*."]},
 {"t": "dialogo", "personas": [{"nombre": "TOMI", "emoji": "👦"}, {"nombre": "SOFI", "emoji": "👧"}], "lineas": [{"quien": 0, "txt": "IS IT A PEN?", "trad": "¿es una lapicera?"}, {"quien": 1, "txt": "NO, IT ISN'T.", "trad": "no, no es"}, {"quien": 0, "txt": "IS IT A PENCIL?", "trad": "¿es un lápiz?"}, {"quien": 1, "txt": "YES, IT IS!", "trad": "¡sí, es!"}],
  "voz": ["Is it a pen?", "No, it isn't.", "Is it a pencil?", "Yes, it is!"], "voz_en": [0, 1, 2, 3]},
 {"t": "balanza", "izq": {"cab": "SÍ ✅", "items": ["YES, IT IS"]}, "der": {"cab": "NO ❌", "items": ["NO, IT ISN'T"]}, "gana": "izq",
  "voz": ["Hay dos respuestas: sí o no.", "Yes, it is!", "No, it isn't!"], "voz_en": [1, 2]},
 {"t": "pregunta", "pregunta": "Es un libro. IS IT A BOOK?", "opciones": ["YES, IT IS", "NO, IT ISN'T", "HELLO"], "correcta": 0,
  "voz": ["Ahora vos. Mirá: es un libro.", "Is it a book?", "Yes, it is!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "CON LA CABEZA", "texto": "Mové la cabeza al decir YES o NO", "emoji": "🙂",
  "voz": ["Truco: mové la *cabeza* al decir sí o no."]},
 {"t": "resumen", "items": [["IS IT A…?", "¿es un…?"], ["YES, IT IS", "sí, es"], ["NO, IT ISN'T", "no, no es"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Is it a pen?", "Yes, it is! No, it isn't!", CIERRE], "voz_en": [1, 2]},
]
N4 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🏠", "lineas": ["Sofi busca su lápiz.", "¿Dónde está?", "¡Está en la mochila!"], "titulo": "WHERE IS IT?", "sub": "in y on",
  "voz": ["Sofi busca su *lápiz*.", "Where is it?", "¡Está en la mochila!", "Hoy: *in y on, dónde están las cosas*."], "voz_en": [1]},
 {"t": "antesdespues", "antes": {"cab": "IN", "emoji": "🎒", "texto": "Adentro de la mochila"}, "despues": {"cab": "ON", "emoji": "📘", "texto": "Arriba de la mesa"},
  "voz": ["The pencil is in the bag.", "The book is on the table."], "voz_en": [0, 1]},
 {"t": "matriz", "titulo": "¿DÓNDE ESTÁ?", "celdas": [{"cab": "✏️🎒", "txt": "IN THE BAG"}, {"cab": "📘🪑", "txt": "ON THE TABLE"}, {"cab": "🧸📦", "txt": "IN THE BOX"}, {"cab": "🐱🛏️", "txt": "ON THE BED"}],
  "voz": ["Buscamos las cosas de Tomi.", "In the bag!", "On the table!", "In the box!", "On the bed!"], "voz_en": [1, 2, 3, 4]},
 {"t": "pregunta", "pregunta": "El lápiz está adentro de la mochila. ¿IN u ON?", "opciones": ["IN", "ON", "UP"], "correcta": 0,
  "voz": ["Ahora vos. El lápiz está adentro.", "¿Es in u on?", "In the bag!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "CON LAS MANOS", "texto": "IN: mano adentro. ON: mano arriba", "emoji": "🙌",
  "voz": ["Truco: *adentro* es in, *arriba* es on."]},
 {"t": "resumen", "items": [["IN", "adentro"], ["ON", "arriba"], ["WHERE IS IT?", "¿dónde está?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Where is it?", "In the bag! On the table!", CIERRE], "voz_en": [1, 2]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
