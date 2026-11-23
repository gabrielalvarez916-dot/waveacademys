# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 7 · Animals: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: la granja y el zoológico de Tomi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 7
TIT = {1: 'Pets: dog, cat and fish', 2: 'Farm animals', 3: 'Wild animals', 4: 'Animal sounds: guessing game'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "gancho", "emoji": "🐾", "final": "❓", "titulo": "PETS", "sub": "mascotas en inglés",
  "voz": ["Tomi ve huellas en el patio.", "¿De qué animal serán?", "Hoy: *mascotas en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "DOG", "emoji": "🐶", "trad": "perro", "pron": "dog"}, {"palabra": "CAT", "emoji": "🐱", "trad": "gato", "pron": "cat"}, {"palabra": "FISH", "emoji": "🐠", "trad": "pez", "pron": "fish"}],
  "voz": ["Dog!", "Cat!", "Fish!"], "voz_en": [0, 1, 2]},
 {"t": "bloques", "titulo": "CUIDAMOS A LAS MASCOTAS", "items": [{"cab": "🍖", "txt": "COMIDA"}, {"cab": "💧", "txt": "AGUA"}, {"cab": "💛", "txt": "CARIÑO"}],
  "voz": ["Las mascotas necesitan cuidados.", "Necesitan *comida*.", "Necesitan *agua*.", "¡Y mucho *cariño*!"]},
 {"t": "pregunta", "pregunta": "¿Qué mascota nada?", "opciones": ["FISH", "DOG", "CAT"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en una mascota que nada.", "¿Cuál es en inglés?", "Fish!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "SONIDOS", "texto": "Pensá en cómo suena cada animal", "emoji": "🔊",
  "voz": ["Truco: pensá en cómo *suena* cada animal."]},
 {"t": "resumen", "items": [["DOG", "perro"], ["CAT", "gato"], ["FISH", "pez"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Dog, cat, fish!", "Perro, gato y *pez*.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🏡", "lineas": ["Tomi visita la granja del abuelo.", "Hay muchos animales.", "¡Escucha mugidos y relinchos!"], "titulo": "FARM ANIMALS", "sub": "animales de granja",
  "voz": ["Tomi visita la *granja* del abuelo.", "Hay muchos animales.", "¡Escucha mugidos y relinchos!", "Hoy: *animales de granja en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "COW", "emoji": "🐄", "trad": "vaca", "pron": "cáu"}, {"palabra": "PIG", "emoji": "🐷", "trad": "chancho", "pron": "pig"}, {"palabra": "HORSE", "emoji": "🐴", "trad": "caballo", "pron": "jors"}, {"palabra": "SHEEP", "emoji": "🐑", "trad": "oveja", "pron": "ship"}],
  "voz": ["Cow!", "Pig!", "Horse!", "Sheep!"], "voz_en": [0, 1, 2, 3]},
 {"t": "matriz", "titulo": "¿QUÉ NOS DAN?", "celdas": [{"cab": "🐄 COW", "txt": "LECHE"}, {"cab": "🐑 SHEEP", "txt": "LANA"}, {"cab": "🐔 HEN", "txt": "HUEVOS"}, {"cab": "🐴 HORSE", "txt": "AYUDA EN EL CAMPO"}],
  "voz": ["Los animales de granja nos ayudan.", "La vaca nos da *leche*.", "La oveja nos da *lana*.", "La gallina nos da *huevos*.", "El caballo *ayuda* en el campo."]},
 {"t": "pregunta", "pregunta": "¿Qué animal da leche?", "opciones": ["COW", "PIG", "HORSE"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en la leche.", "¿Qué animal la da?", "Cow!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "LO QUE DAN", "texto": "La vaca da leche y la oveja, lana", "emoji": "🥛",
  "voz": ["Truco: pensá en lo que *da* cada animal."]},
 {"t": "resumen", "items": [["COW / PIG", "vaca y chancho"], ["HORSE", "caballo"], ["SHEEP", "oveja"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cow, pig, horse, sheep!", "Los animales de la *granja*.", CIERRE], "voz_en": [1]},
]
N3 = [
 {"t": "chat", "contacto": SOFI, "mensajes": [{"yo": False, "txt": "🦁 I AM AT THE ZOO!"}, {"yo": True, "txt": "¡Qué lindo!"}, {"yo": False, "txt": "A LION! A MONKEY!"}], "titulo": "WILD ANIMALS", "sub": "animales salvajes",
  "voz": ["Sofi le escribe desde el zoológico.", "I am at the zoo!", "Ve animales *salvajes*.", "Hoy: *animales salvajes en inglés*."], "voz_en": [1]},
 {"t": "vocab", "items": [{"palabra": "LION", "emoji": "🦁", "trad": "león", "pron": "láion"}, {"palabra": "ELEPHANT", "emoji": "🐘", "trad": "elefante", "pron": "élefant"}, {"palabra": "MONKEY", "emoji": "🐒", "trad": "mono", "pron": "mánki"}, {"palabra": "GIRAFFE", "emoji": "🦒", "trad": "jirafa", "pron": "yiráf"}],
  "voz": ["Lion!", "Elephant!", "Monkey!", "Giraffe!"], "voz_en": [0, 1, 2, 3]},
 {"t": "comparar", "a": {"cab": "GRANJA", "texto": "COW, PIG, SHEEP", "emoji": "🏡"}, "b": {"cab": "SELVA", "texto": "LION, MONKEY", "emoji": "🌴"}, "signo": "vs",
  "voz": ["Los animales viven en lugares distintos.", "Unos viven en la *granja*.", "Otros viven libres en la *selva*."]},
 {"t": "clasificar", "cajas": [{"cab": "GRANJA", "emoji": "🏡"}, {"cab": "SELVA", "emoji": "🌴"}], "fichas": [{"txt": "COW", "caja": 0}, {"txt": "PIG", "caja": 0}, {"txt": "LION", "caja": 1}, {"txt": "GIRAFFE", "caja": 1}],
  "voz": ["¿Dónde vive cada uno?", "Cow and pig: farm!", "Lion and giraffe: jungle!"], "voz_en": [1, 2]},
 {"t": "pregunta", "pregunta": "Tiene el cuello muy largo. ¿Cuál es?", "opciones": ["GIRAFFE", "LION", "MONKEY"], "correcta": 0,
  "voz": ["Ahora vos. Tiene el cuello muy largo.", "¿Qué animal es?", "Giraffe!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "PISTAS", "texto": "Mirá cómo es el animal para adivinar", "emoji": "🔎",
  "voz": ["Truco: mirá cómo es el animal para *adivinar*."]},
 {"t": "resumen", "items": [["LION / ELEPHANT", "león y elefante"], ["MONKEY", "mono"], ["GIRAFFE", "jirafa"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Lion, elephant, monkey, giraffe!", "Los animales *salvajes*.", CIERRE], "voz_en": [1]},
]
N4 = [
 {"t": "reto", "texto": "¿Qué animal hace MOO?", "segundos": 6, "respuesta": "¡LA VACA: COW!", "emoji": "🐄", "titulo": "ANIMAL SOUNDS", "sub": "adivinar por el sonido",
  "voz": ["Desafío: ¿qué animal hace así?", "Moo!", "¡La vaca! Hoy: *sonidos de animales*."], "voz_en": [1]},
 {"t": "bloques", "titulo": "¿CÓMO SUENAN?", "items": [{"cab": "🐶", "txt": "WOOF!"}, {"cab": "🐱", "txt": "MEOW!"}, {"cab": "🐄", "txt": "MOO!"}, {"cab": "🦆", "txt": "QUACK!"}],
  "voz": ["En inglés, los animales suenan así.", "Woof!", "Meow!", "Moo!", "Quack!"], "voz_en": [1, 2, 3, 4]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "TOMI", "emoji": "👦"}], "lineas": [{"quien": 0, "txt": "WOOF! WOOF!", "trad": "¡guau, guau!"}, {"quien": 1, "txt": "WHAT IS IT?", "trad": "¿qué es?"}, {"quien": 1, "txt": "IT IS A DOG!", "trad": "¡es un perro!"}],
  "voz": ["Woof! Woof!", "What is it?", "It is a dog!"], "voz_en": [0, 1, 2]},
 {"t": "pregunta", "pregunta": "Escuchás MEOW. ¿Qué es?", "opciones": ["IT IS A CAT", "IT IS A DOG", "IT IS A COW"], "correcta": 0,
  "voz": ["Ahora vos. Escuchá el sonido.", "Meow!", "It is a cat!"], "voz_en": [1, 2]},
 {"t": "consejo", "titulo": "DISTINTOS", "texto": "En inglés los animales suenan distinto", "emoji": "🔊",
  "voz": ["Dato: en inglés los animales *suenan distinto*."]},
 {"t": "resumen", "items": [["WOOF / MEOW", "perro y gato"], ["MOO / QUACK", "vaca y pato"], ["WHAT IS IT?", "¿qué es?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Woof, meow, moo, quack!", "What is it?", CIERRE], "voz_en": [1, 2]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
