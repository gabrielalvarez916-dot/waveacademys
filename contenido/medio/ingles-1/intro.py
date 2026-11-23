# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Clase de introducción de la materia.
Regla de primeros años. Explicación en castellano; las frases en inglés van en "voz_en".
Se carga en la introducción de la materia (subject_id). Genera tools/medio/clase/lecciones/medio-intro-ing1.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
SOFI = {"nombre": "Sofi", "emoji": "👧"}
E = [
 {"t": "historia", "personaje": SOFI, "lugar": "🌎", "lineas": ["Sofi conoce a una nena de otro país.", "La nena le dice: HELLO!", "¡Sofi quiere aprender a contestarle!"], "titulo": "WELCOME!", "sub": "a Inglés 1",
  "voz": ["Sofi conoce a una nena de otro *país*.", "Hello!", "¡Sofi quiere aprender a contestarle!", "¡Bienvenidos a *Inglés 1*!"], "voz_en": [1]},
 {"t": "matriz", "titulo": "ESTE AÑO VAMOS A APRENDER", "celdas": [{"cab": "👋", "txt": "SALUDAR"}, {"cab": "🔢", "txt": "LOS NÚMEROS"}, {"cab": "🎨", "txt": "LOS COLORES"}, {"cab": "👨‍👩‍👧", "txt": "MI FAMILIA"}, {"cab": "🐶", "txt": "LOS ANIMALES"}, {"cab": "🍎", "txt": "LA COMIDA"}],
  "voz": ["Este año vamos a aprender muchas *palabras*.", "Hello!", "One, two, three!", "Red, blue, yellow!", "Mi familia y los *animales*.", "¡Y la comida que nos gusta!"], "voz_en": [1, 2, 3]},
 {"t": "flujo", "titulo": "ASÍ APRENDEMOS", "items": ["ESCUCHO 👂", "REPITO 🗣️", "JUEGO 🎲", "CANTO 🎵"],
  "voz": ["Aprendemos inglés *jugando*.", "Primero *escucho* cómo suena.", "Después lo *repito* en voz alta.", "*Juego* con las palabras.", "¡Y *canto* canciones!"]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "AMY", "emoji": "👱‍♀️"}], "lineas": [{"quien": 1, "txt": "HELLO! I AM AMY.", "trad": "¡hola! soy Amy"}, {"quien": 0, "txt": "HELLO! I AM SOFI.", "trad": "¡hola! soy Sofi"}, {"quien": 1, "txt": "LET'S PLAY!", "trad": "¡juguemos!"}],
  "voz": ["Hello! I am Amy.", "Hello! I am Sofi.", "Let's play!"], "voz_en": [0, 1, 2]},
 {"t": "pregunta", "pregunta": "¿Cómo se saluda en inglés?", "opciones": ["HELLO", "CHAU", "GRACIAS"], "correcta": 0,
  "voz": ["Ahora vos. Una nena te saluda.", "¿Cómo se dice hola en inglés?", "Hello!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "SIN MIEDO", "texto": "Equivocarse es parte de aprender", "emoji": "💪",
  "voz": ["Importante: *equivocarse* es parte de aprender."]},
 {"t": "frase", "texto": "LET'S LEARN ENGLISH!", "emoji": "🌈", "color": "sol",
  "voz": ["Let's learn English!", "¡A aprender inglés *juntos*!"], "voz_en": [0]},
]
L = {"slug": "medio-intro-ing1", "subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "materia": "Inglés 1", "titulo": "Bienvenidos a Inglés 1", "sub": "Introducción · Nivel medio", "estilo": "primeros", "escenas": E}
json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', 'medio-intro-ing1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('medio-intro-ing1', len(E), 'escenas')
