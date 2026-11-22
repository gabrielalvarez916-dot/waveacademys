# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Clase de introducción de la materia.
Regla de primeros años. Se carga en la introducción de la materia (subject_id).
Genera tools/medio/clase/lecciones/medio-intro-soc1.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
TOMI = {"nombre": "Tomi", "emoji": "👦"}
E = [
 {"t": "historia", "personaje": TOMI, "lugar": "🏘️", "lineas": ["Tomi sale de su casa.", "Saluda a sus vecinos.", "¡Quiere conocer cómo vive la gente!"], "titulo": "¡BIENVENIDOS!", "sub": "a Ciencias Sociales 1",
  "voz": ["¡Hola! Él es *Tomi*.", "Tomi sale y saluda a sus *vecinos*.", "¡Quiere saber cómo vive la gente!", "¡Bienvenidos a *Ciencias Sociales 1*!"]},
 {"t": "matriz", "titulo": "ESTE AÑO VAMOS A CONOCER", "celdas": [{"cab": "👨‍👩‍👧", "txt": "LAS FAMILIAS"}, {"cab": "🏫", "txt": "LA ESCUELA"}, {"cab": "🏘️", "txt": "EL BARRIO"}, {"cab": "🌾", "txt": "EL CAMPO Y LA CIUDAD"}, {"cab": "⏳", "txt": "EL PASADO"}, {"cab": "🎉", "txt": "FIESTAS Y DERECHOS"}],
  "voz": ["Este año vamos a conocer a las *personas*.", "Las *familias* y la escuela.", "El *barrio* donde vivimos.", "El *campo* y la ciudad.", "Cómo vivían *antes*.", "¡Y las fiestas y los *derechos*!"]},
 {"t": "flujo", "titulo": "ASÍ INVESTIGAMOS", "items": ["MIRO", "PREGUNTO", "COMPARO", "CUENTO"],
  "voz": ["Vamos a investigar como *exploradores*.", "Primero, *miro* a mi alrededor.", "Después, *pregunto* a los grandes.", "*Comparo* antes y ahora.", "Y *cuento* lo que aprendí."]},
 {"t": "comparar", "a": {"cab": "ANTES", "texto": "Cartas en papel", "emoji": "✉️"}, "b": {"cab": "AHORA", "texto": "Mensajes en el celular", "emoji": "📱"}, "signo": "vs",
  "voz": ["Las cosas *cambian* con el tiempo.", "*Antes* mandaban cartas.", "*Ahora* mandamos mensajes.", "¡Vamos a descubrir esos cambios!"]},
 {"t": "pregunta", "pregunta": "¿A quién le pregunto cómo era antes?", "opciones": ["A MI ABUELA", "A MI PERRO", "A LA TELE"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el pasado.", "¿A quién le preguntás cómo era antes?", "¡A tu *abuela* o tu abuelo!"]},
 {"t": "consejo", "titulo": "CONVIVIR", "texto": "Respetamos a todas las personas", "emoji": "🤝",
  "voz": ["Importante: *respetamos* a todas las personas."]},
 {"t": "frase", "texto": "¡A CONOCER NUESTRO MUNDO!", "emoji": "🌎", "color": "sol",
  "voz": ["¡Vamos a *conocer nuestro mundo* juntos!"]},
]
L = {"slug": "medio-intro-soc1", "subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "materia": "Ciencias Sociales 1", "titulo": "Bienvenidos a Ciencias Sociales 1", "sub": "Introducción · Nivel medio", "estilo": "primeros", "escenas": E}
json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', 'medio-intro-soc1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('medio-intro-soc1', len(E), 'escenas')
