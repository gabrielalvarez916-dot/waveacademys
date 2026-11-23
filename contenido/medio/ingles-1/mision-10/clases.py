# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 10 · Project: My Little Book of English: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: el librito de inglés de Sofi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 10
TIT = {1: 'Choose my favourite words', 2: 'Draw and label my pictures', 3: 'Record my voice', 4: 'Share my little book'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": SOFI, "mensajes": [{"yo": False, "txt": "¡Vamos a hacer un librito!"}, {"yo": True, "txt": "¿De qué?"}, {"yo": False, "txt": "MY LITTLE BOOK OF ENGLISH! 📒"}], "titulo": "MY LITTLE BOOK", "sub": "elegir mis palabras",
  "voz": ["Sofi le escribe a Tomi.", "¡Vamos a hacer un *librito*!", "My little book of English!", "Hoy: *elegimos nuestras palabras*."], "voz_en": [2]},
 {"t": "matriz", "titulo": "LO QUE APRENDIMOS", "celdas": [{"cab": "👋", "txt": "HELLO"}, {"cab": "🔢", "txt": "ONE, TWO"}, {"cab": "🎨", "txt": "RED, BLUE"}, {"cab": "🐶", "txt": "DOG, CAT"}, {"cab": "🍎", "txt": "APPLE"}, {"cab": "🧸", "txt": "BALL, DOLL"}],
  "voz": ["¡Aprendimos un montón este año!", "Hello!", "One, two!", "Red, blue!", "Dog, cat!", "Apple!", "Ball, doll!"], "voz_en": [1, 2, 3, 4, 5, 6]},
 {"t": "partes", "emoji": "📒", "titulo": "LAS PÁGINAS DE SOFI", "partes": [{"txt": "1: HELLO", "x": -0.6, "y": -0.5}, {"txt": "2: RED", "x": 0.6, "y": -0.5}, {"txt": "3: CAT", "x": -0.6, "y": 0.5}, {"txt": "4: APPLE", "x": 0.6, "y": 0.5}],
  "voz": ["Sofi elige una palabra por página.", "Página uno: hello.", "Página dos: red.", "Página tres: cat.", "Página cuatro: apple."]},
 {"t": "pregunta", "pregunta": "Querés un animal para tu librito. ¿Cuál elegís?", "opciones": ["CAT", "RED", "ONE"], "correcta": 0,
  "voz": ["Ahora vos. Querés un animal.", "¿Cuál es un animal en inglés?", "Cat!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "LAS QUE MÁS TE GUSTAN", "texto": "Elegí palabras que te hagan sonreír", "emoji": "😊",
  "voz": ["Truco: elegí las palabras que *más te gustan*."]},
 {"t": "resumen", "items": [["PROYECTO", "mi librito"], ["ELEGIR", "mis palabras"], ["PÁGINAS", "una palabra en cada una"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Armamos un *librito* de inglés.", "Elegimos una palabra por *página*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué va al lado del dibujo de un gato?", "segundos": 6, "respuesta": "¡CAT!", "emoji": "🐱", "titulo": "DRAW AND LABEL", "sub": "dibujar y nombrar",
  "voz": ["Desafío: ¿qué escribimos al lado del gato?", "Cat!", "Hoy: *dibujar y nombrar en inglés*."], "voz_en": [1]},
 {"t": "flujo", "titulo": "PASO A PASO", "items": ["DIBUJO ✏️", "ESCRIBO EL NOMBRE 🔤", "PINTO 🖍️"],
  "voz": ["Primero, *dibujo* lo que elegí.", "Después, *escribo* su nombre en inglés.", "Al final, lo *pinto*."]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "🐶", "texto": "Un dibujo sin nombre"}, "despues": {"cab": "DESPUÉS", "emoji": "🐶", "texto": "El dibujo con DOG"},
  "voz": ["*Antes*, el dibujo no tiene nombre.", "*Después*, le escribimos el nombre: dog!"]},
 {"t": "pregunta", "pregunta": "Dibujaste una pelota. ¿Qué escribís?", "opciones": ["BALL", "DOLL", "CAR"], "correcta": 0,
  "voz": ["Ahora vos. Dibujaste una pelota.", "¿Qué nombre le escribís?", "Ball!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "LETRA CLARA", "texto": "Escribí en imprenta mayúscula grande", "emoji": "🔠",
  "voz": ["Truco: escribí con letra *grande* y clara."]},
 {"t": "resumen", "items": [["DIBUJAR", "lo que elegí"], ["ROTULAR", "escribir el nombre"], ["PINTAR", "con colores"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Dibujamos* cada página.", "Le escribimos el *nombre* en inglés.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡LOS CHICOS GRABAN SU VOZ!", "bajada": "Dicen sus palabras en inglés", "emoji": "🎙️", "titulo": "RECORD MY VOICE", "sub": "grabar mi voz",
  "voz": ["¡Último momento! Los chicos *graban* su voz.", "¡Dicen sus palabras en inglés!", "Hoy: *grabar mi voz*."]},
 {"t": "ciclo", "titulo": "ASÍ GRABAMOS", "items": ["ESCUCHO 👂", "REPITO 🗣️", "GRABO 🎙️"],
  "voz": ["Así grabamos cada palabra.", "Primero *escucho* cómo suena.", "Después la *repito*.", "¡Y la *grabo*!"]},
 {"t": "comparar", "a": {"cab": "ASÍ NO", "texto": "Bajito y rápido", "emoji": "🙊"}, "b": {"cab": "ASÍ SÍ", "texto": "Despacio y fuerte", "emoji": "🗣️"}, "signo": "vs",
  "voz": ["¿Cómo hablamos al grabar?", "Bajito y rápido no se *entiende*.", "Despacio y fuerte, ¡sí!"]},
 {"t": "pregunta", "pregunta": "Grabás la página del gato. ¿Qué decís?", "opciones": ["CAT", "DOG", "RED"], "correcta": 0,
  "voz": ["Ahora vos. Grabás la página del gato.", "¿Qué decís?", "Cat!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "PRACTICÁ", "texto": "Decí la palabra tres veces antes de grabar", "emoji": "🔁",
  "voz": ["Truco: *practicá* tres veces antes de grabar."]},
 {"t": "resumen", "items": [["ESCUCHAR", "cómo suena"], ["REPETIR", "practicar"], ["GRABAR", "guardar mi voz"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Escuchamos, *repetimos* y grabamos.", "Hablamos *despacio* y fuerte.", CIERRE]},
]
N4 = [
 {"t": "gancho", "emoji": "📒", "final": "🎉", "titulo": "SHARE MY BOOK", "sub": "compartir mi librito",
  "voz": ["¡El librito de Sofi está *listo*!", "¿A quién se lo va a mostrar?", "Hoy: *compartir mi librito*."]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "TOMI", "emoji": "👦"}], "lineas": [{"quien": 0, "txt": "HELLO! THIS IS MY BOOK!", "trad": "¡hola! ¡este es mi libro!"}, {"quien": 1, "txt": "I LIKE YOUR BOOK!", "trad": "¡me gusta tu libro!"}, {"quien": 0, "txt": "THANK YOU! GOODBYE!", "trad": "¡gracias! ¡chau!"}],
  "voz": ["Hello! This is my book!", "I like your book!", "Thank you! Goodbye!"], "voz_en": [0, 1, 2]},
 {"t": "orden", "titulo": "MI PRESENTACIÓN", "items": [{"txt": "HELLO!", "emoji": "1️⃣"}, {"txt": "THIS IS MY BOOK!", "emoji": "2️⃣"}, {"txt": "MIS PÁGINAS", "emoji": "3️⃣"}, {"txt": "GOODBYE!", "emoji": "4️⃣"}], "relato": [2, 0, 3, 1],
  "voz": ["¡Se mezclaron los pasos de Sofi!", "Los ponemos en *orden*.", "Saludo, muestro, cuento y me *despido*."]},
 {"t": "pregunta", "pregunta": "Te gustó el librito de tu amigo. ¿Qué decís?", "opciones": ["I LIKE YOUR BOOK!", "YUCK!", "I AM SIX!"], "correcta": 0,
  "voz": ["Ahora vos. Te gustó el librito de tu amigo.", "¿Qué le decís?", "I like your book!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "CON ORGULLO", "texto": "¡Mostrá tu librito con orgullo!", "emoji": "🌟",
  "voz": ["¡Mostrá tu librito con *orgullo*!"]},
 {"t": "resumen", "items": [["THIS IS MY BOOK", "este es mi libro"], ["I LIKE YOUR BOOK", "me gusta tu libro"], ["COMPARTIR", "mostrar y escuchar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "This is my book!", "¡Terminamos el año en *inglés*!", CIERRE], "voz_en": [1]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
