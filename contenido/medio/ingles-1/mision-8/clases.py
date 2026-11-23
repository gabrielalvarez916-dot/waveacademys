# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 8 · Toys and Games: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: la caja de juguetes de Sofi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 8
TIT = {1: 'My toys: ball, doll and car', 2: 'I have a ball', 3: 'Big and small toys', 4: 'Yes or no: the toy game'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SOFI ABRE SU CAJA DE JUGUETES!", "bajada": "Y los nombra en inglés", "emoji": "🧸", "titulo": "MY TOYS", "sub": "mis juguetes",
  "voz": ["¡Último momento! Sofi abre su caja de *juguetes*.", "¡Y los nombra en inglés!", "Hoy: *mis juguetes en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "BALL", "emoji": "⚽", "trad": "pelota", "pron": "bol"}, {"palabra": "DOLL", "emoji": "🪆", "trad": "muñeca", "pron": "dol"}, {"palabra": "CAR", "emoji": "🚗", "trad": "auto", "pron": "car"}, {"palabra": "TEDDY", "emoji": "🧸", "trad": "osito", "pron": "tédi"}],
  "voz": ["Ball!", "Doll!", "Car!", "Teddy!"], "voz_en": [0, 1, 2, 3]},
 {"t": "partes", "emoji": "📦", "titulo": "MY TOY BOX", "partes": [{"txt": "BALL", "x": -0.6, "y": -0.5}, {"txt": "DOLL", "x": 0.6, "y": -0.5}, {"txt": "CAR", "x": -0.6, "y": 0.5}, {"txt": "TEDDY", "x": 0.6, "y": 0.5}],
  "voz": ["¿Qué hay en la caja de Sofi?", "A ball!", "A doll!", "A car!", "A teddy!"], "voz_en": [1, 2, 3, 4]},
 {"t": "pregunta", "pregunta": "¿Cómo se dice pelota?", "opciones": ["BALL", "DOLL", "CAR"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en una pelota.", "¿Cómo se dice en inglés?", "Ball!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "PARA TODOS", "texto": "Todos podemos jugar con todos los juguetes", "emoji": "🤝",
  "voz": ["Recordá: *todos* podemos jugar con todos los juguetes."]},
 {"t": "resumen", "items": [["BALL", "pelota"], ["DOLL", "muñeca"], ["CAR / TEDDY", "auto y osito"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Ball, doll, car, teddy!", "Los *juguetes* en inglés.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "gancho", "emoji": "🎁", "final": "❓", "titulo": "I HAVE A BALL", "sub": "lo que tengo",
  "voz": ["Tomi tiene un regalo nuevo.", "¿Qué juguete tendrá?", "Hoy: *decir lo que tengo en inglés*."]},
 {"t": "dialogo", "personas": [{"nombre": "TOMI", "emoji": "👦"}, {"nombre": "SOFI", "emoji": "👧"}], "lineas": [{"quien": 0, "txt": "I HAVE A CAR!", "trad": "¡tengo un auto!"}, {"quien": 1, "txt": "I HAVE A DOLL!", "trad": "¡tengo una muñeca!"}, {"quien": 0, "txt": "LET'S PLAY!", "trad": "¡juguemos!"}],
  "voz": ["I have a car!", "I have a doll!", "Let's play!"], "voz_en": [0, 1, 2]},
 {"t": "matriz", "titulo": "I HAVE A…", "celdas": [{"cab": "👦🚗", "txt": "I HAVE A CAR"}, {"cab": "👧🪆", "txt": "I HAVE A DOLL"}, {"cab": "🧒⚽", "txt": "I HAVE A BALL"}, {"cab": "👶🧸", "txt": "I HAVE A TEDDY"}],
  "voz": ["Cada chico dice lo que tiene.", "I have a car!", "I have a doll!", "I have a ball!", "I have a teddy!"], "voz_en": [1, 2, 3, 4]},
 {"t": "pregunta", "pregunta": "Tenés una pelota. ¿Qué decís?", "opciones": ["I HAVE A BALL", "I AM A BALL", "IT IS RED"], "correcta": 0,
  "voz": ["Ahora vos. Tenés una pelota.", "¿Qué decís en inglés?", "I have a ball!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "MOSTRÁ", "texto": "Mostrá el juguete al decir I HAVE A", "emoji": "🙌",
  "voz": ["Truco: *mostrá* el juguete al decirlo."]},
 {"t": "resumen", "items": [["I HAVE A…", "tengo un…"], ["HAVE", "tener"], ["LET'S PLAY", "¡juguemos!"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "I have a ball!", "Así decimos lo que *tenemos*.", CIERRE], "voz_en": [1]},
]
N3 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🛝", "lineas": ["Tomi lleva dos pelotas a la plaza.", "Una es enorme.", "¡La otra es chiquita!"], "titulo": "BIG AND SMALL", "sub": "grande y chico",
  "voz": ["Tomi lleva dos pelotas a la *plaza*.", "Una es *enorme*.", "¡La otra es *chiquita*!", "Hoy: *grande y chico en inglés*."]},
 {"t": "comparar", "a": {"cab": "BIG", "texto": "Grande", "emoji": "🐘"}, "b": {"cab": "SMALL", "texto": "Chico", "emoji": "🐭"}, "signo": "vs",
  "voz": ["Dos palabras opuestas.", "Big!", "Small!"], "voz_en": [1, 2]},
 {"t": "balanza", "izq": {"cab": "BIG", "items": ["A BIG TEDDY"]}, "der": {"cab": "SMALL", "items": ["A SMALL CAR"]}, "gana": "izq",
  "voz": ["Ponemos dos juguetes en la balanza.", "A big teddy!", "A small car!"], "voz_en": [1, 2]},
 {"t": "pregunta", "pregunta": "Un oso enorme es…", "opciones": ["BIG", "SMALL", "RED"], "correcta": 0,
  "voz": ["Ahora vos. Mirá el oso enorme.", "¿Es big o small?", "Big!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "CON LAS MANOS", "texto": "Grande: abrí los brazos. Chico: juntá los dedos", "emoji": "🙌",
  "voz": ["Truco: para grande, *abrí los brazos*."]},
 {"t": "resumen", "items": [["BIG", "grande"], ["SMALL", "chico"], ["A BIG BALL", "una pelota grande"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Big and small!", "Grande y *chico* en inglés.", CIERRE], "voz_en": [1]},
]
N4 = [
 {"t": "chat", "contacto": SOFI, "mensajes": [{"yo": False, "txt": "🙈 I HAVE A TOY. GUESS!"}, {"yo": True, "txt": "IS IT A BALL?"}, {"yo": False, "txt": "NO, IT ISN'T!"}], "titulo": "THE TOY GAME", "sub": "adivinar con YES y NO",
  "voz": ["Sofi le propone un juego a Tomi.", "Guess! ¡Adiviná!", "Tomi pregunta en inglés.", "Hoy: *el juego de los juguetes*."]},
 {"t": "ciclo", "titulo": "ASÍ SE JUEGA", "items": ["ESCONDO", "PREGUNTÁS", "YES O NO"],
  "voz": ["Así se juega.", "Uno *esconde* un juguete.", "El otro *pregunta* en inglés.", "Y contestamos *yes* o *no*."]},
 {"t": "corrige", "titulo": "¿ESTÁ BIEN?", "cambios": [{"antes": "🚗 IS IT A CAR? NO", "despues": "🚗 IS IT A CAR? YES!", "motivo": "es un auto"}, {"antes": "⚽ IS IT A DOLL? YES", "despues": "⚽ IS IT A DOLL? NO!", "motivo": "es una pelota"}],
  "voz": ["Tomi contestó mal. Lo arreglamos.", "Is it a car? Yes!", "Is it a doll? No!"], "voz_en": [1, 2]},
 {"t": "pregunta", "pregunta": "Es una pelota. IS IT A BALL?", "opciones": ["YES, IT IS", "NO, IT ISN'T", "I HAVE A CAR"], "correcta": 0,
  "voz": ["Ahora vos. Es una pelota.", "Is it a ball?", "Yes, it is!"], "voz_en": [1, 2]},
 {"t": "consejo", "titulo": "TURNOS", "texto": "Esperá tu turno para preguntar", "emoji": "⏳",
  "voz": ["Truco: *esperá* tu turno para preguntar."]},
 {"t": "resumen", "items": [["IS IT A…?", "¿es un…?"], ["YES", "sí"], ["NO", "no"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Is it a ball? Yes! No!", "¡A *jugar* en inglés!", CIERRE], "voz_en": [1]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
