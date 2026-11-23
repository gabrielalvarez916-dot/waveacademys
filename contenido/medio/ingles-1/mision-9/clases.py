# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 9 · Food I Like: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: la merienda de Sofi y Tomi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 9
TIT = {1: 'Fruit: apple, banana and orange', 2: 'I like apples', 3: 'Milk, bread and water', 4: 'Yummy or yuck?'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "reto", "texto": "¿Cómo se dice manzana en inglés?", "segundos": 6, "respuesta": "¡APPLE!", "emoji": "🍎", "titulo": "FRUIT", "sub": "frutas en inglés",
  "voz": ["Desafío: ¿cómo se dice manzana en inglés?", "Apple!", "Hoy: *frutas en inglés*."], "voz_en": [1]},
 {"t": "vocab", "items": [{"palabra": "APPLE", "emoji": "🍎", "trad": "manzana", "pron": "ápel"}, {"palabra": "BANANA", "emoji": "🍌", "trad": "banana", "pron": "banána"}, {"palabra": "ORANGE", "emoji": "🍊", "trad": "naranja", "pron": "órinch"}],
  "voz": ["Apple!", "Banana!", "Orange!"], "voz_en": [0, 1, 2]},
 {"t": "bloques", "titulo": "FRUTAS DE COLORES", "items": [{"cab": "🍎", "txt": "RED APPLE"}, {"cab": "🍌", "txt": "YELLOW BANANA"}, {"cab": "🍊", "txt": "ORANGE ORANGE"}],
  "voz": ["Cada fruta tiene su color.", "A red apple!", "A yellow banana!", "An orange orange!"], "voz_en": [1, 2, 3]},
 {"t": "pregunta", "pregunta": "Es amarilla y larga. ¿Qué fruta es?", "opciones": ["BANANA", "APPLE", "ORANGE"], "correcta": 0,
  "voz": ["Ahora vos. Es amarilla y larga.", "¿Qué fruta es en inglés?", "Banana!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "CASI IGUAL", "texto": "BANANA se dice casi igual en castellano", "emoji": "🍌",
  "voz": ["Dato: banana se dice *casi igual* en inglés."]},
 {"t": "resumen", "items": [["APPLE", "manzana"], ["BANANA", "banana"], ["ORANGE", "naranja"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Apple, banana, orange!", "Las *frutas* en inglés.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡MERIENDA DE FRUTAS!", "bajada": "Cada uno elige la que le gusta", "emoji": "🧺", "titulo": "I LIKE APPLES", "sub": "lo que me gusta",
  "voz": ["¡Último momento! Hay *merienda* de frutas.", "Cada uno elige la que le *gusta*.", "Hoy: *decir lo que me gusta en inglés*."]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "TOMI", "emoji": "👦"}], "lineas": [{"quien": 0, "txt": "I LIKE APPLES!", "trad": "¡me gustan las manzanas!"}, {"quien": 1, "txt": "I LIKE ORANGES!", "trad": "¡me gustan las naranjas!"}, {"quien": 0, "txt": "I LIKE BANANAS TOO!", "trad": "¡también las bananas!"}],
  "voz": ["I like apples!", "I like oranges!", "I like bananas too!"], "voz_en": [0, 1, 2]},
 {"t": "venn", "a": "SOFI", "b": "TOMI", "itemsA": ["APPLES"], "itemsB": ["ORANGES"], "ambos": ["BANANAS"],
  "voz": ["¿Qué le gusta a cada uno?", "A Sofi le gustan las manzanas.", "A Tomi, las naranjas.", "¡Y a los dos les gustan las bananas!"]},
 {"t": "pregunta", "pregunta": "Te gustan las manzanas. ¿Qué decís?", "opciones": ["I LIKE APPLES", "I HAVE A CAR", "I AM SAD"], "correcta": 0,
  "voz": ["Ahora vos. Te gustan las manzanas.", "¿Qué decís en inglés?", "I like apples!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "GUSTOS DISTINTOS", "texto": "A cada uno le gusta algo distinto", "emoji": "🤝",
  "voz": ["Recordá: a cada uno le gusta algo *distinto*."]},
 {"t": "resumen", "items": [["I LIKE…", "me gusta…"], ["LIKE", "gustar"], ["DISTINTOS", "cada uno su gusto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "I like apples!", "Así decimos lo que nos *gusta*.", CIERRE], "voz_en": [1]},
]
N3 = [
 {"t": "gancho", "emoji": "🥣", "final": "❓", "titulo": "BREAKFAST", "sub": "el desayuno",
  "voz": ["Tomi se despierta con hambre.", "¿Qué va a desayunar?", "Hoy: *el desayuno en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "MILK", "emoji": "🥛", "trad": "leche", "pron": "milk"}, {"palabra": "BREAD", "emoji": "🍞", "trad": "pan", "pron": "bred"}, {"palabra": "WATER", "emoji": "💧", "trad": "agua", "pron": "uóter"}],
  "voz": ["Milk!", "Bread!", "Water!"], "voz_en": [0, 1, 2]},
 {"t": "flujo", "titulo": "MI DESAYUNO", "items": ["MILK 🥛", "BREAD 🍞", "APPLE 🍎", "WATER 💧"],
  "voz": ["Primero, un vaso de leche.", "Después, pan con manteca.", "Una fruta rica.", "¡Y agua para tomar!"]},
 {"t": "clasificar", "cajas": [{"cab": "COMEMOS", "emoji": "🍽️"}, {"cab": "TOMAMOS", "emoji": "🥤"}], "fichas": [{"txt": "BREAD", "caja": 0}, {"txt": "APPLE", "caja": 0}, {"txt": "MILK", "caja": 1}, {"txt": "WATER", "caja": 1}],
  "voz": ["¿Se come o se toma?", "Bread and apple: we eat!", "Milk and water: we drink!"], "voz_en": [1, 2]},
 {"t": "pregunta", "pregunta": "Un vaso blanco de leche. ¿Qué es?", "opciones": ["MILK", "WATER", "BREAD"], "correcta": 0,
  "voz": ["Ahora vos. Mirá el vaso blanco.", "¿Qué es en inglés?", "Milk!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "TOMAR AGUA", "texto": "El agua es lo más sano para tomar", "emoji": "💧",
  "voz": ["Recordá: el *agua* es lo más sano para tomar."]},
 {"t": "resumen", "items": [["MILK", "leche"], ["BREAD", "pan"], ["WATER", "agua"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Milk, bread, water!", "Un *desayuno* en inglés.", CIERRE], "voz_en": [1]},
]
N4 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍽️", "lineas": ["Sofi prueba comidas nuevas.", "Una le encanta.", "¡Otra no le gusta nada!"], "titulo": "YUMMY OR YUCK?", "sub": "rico o feo",
  "voz": ["Sofi prueba comidas *nuevas*.", "Una le *encanta*.", "¡Otra no le gusta nada!", "Hoy: *rico o feo en inglés*."]},
 {"t": "comparar", "a": {"cab": "YUMMY!", "texto": "¡Rico!", "emoji": "😋"}, "b": {"cab": "YUCK!", "texto": "¡Puaj!", "emoji": "🤢"}, "signo": "vs",
  "voz": ["Dos palabras para el sabor.", "Yummy!", "Yuck!"], "voz_en": [1, 2]},
 {"t": "barras", "titulo": "LA FRUTA PREFERIDA DEL GRADO", "unidad": "votos", "items": [{"txt": "APPLE", "valor": 6}, {"txt": "BANANA", "valor": 9}, {"txt": "ORANGE", "valor": 4}],
  "voz": ["Votamos la fruta más rica.", "Apple: six votes.", "Banana: nine votes!", "Orange: four votes."], "voz_en": [1, 2, 3]},
 {"t": "pregunta", "pregunta": "Te encanta la banana. ¿Qué decís?", "opciones": ["YUMMY!", "YUCK!", "BYE!"], "correcta": 0,
  "voz": ["Ahora vos. Probás una banana y te encanta.", "¿Qué decís en inglés?", "Yummy!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "CON RESPETO", "texto": "Decimos YUCK sin ofender a nadie", "emoji": "🤝",
  "voz": ["Recordá: a cada uno le gusta algo *distinto*."]},
 {"t": "resumen", "items": [["YUMMY", "¡rico!"], ["YUCK", "¡puaj!"], ["GUSTOS", "cada uno el suyo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Yummy! Yuck!", "¡Y la fruta preferida fue la *banana*!", CIERRE], "voz_en": [1]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
