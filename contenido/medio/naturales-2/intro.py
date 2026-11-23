# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Introducción de la materia (clase animada de bienvenida).
Mismo molde que las otras introducciones del Medio. Regla de primeros años.
Metáfora del año: Tomi, científico explorador con su lupa (observa, pregunta, prueba y anota).
Se carga en la introducción de la materia (subject_id). Genera tools/medio/clase/lecciones/medio-intro-nat2.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}
E = [
 {"t": "historia", "personaje": TOMI, "lugar": "🔍", "lineas": ["Tomi empieza segundo grado.", "Tiene una lupa nueva.", "¡Quiere investigar todo!"], "titulo": "¡BIENVENIDOS!", "sub": "a Ciencias Naturales 2",
  "voz": ["¡Hola! Él es *Tomi*.", "Empieza *segundo grado* y tiene una *lupa* nueva.", "¡Quiere investigar todo!", "¡Bienvenidos a *Ciencias Naturales 2*!"]},
 {"t": "pasos", "titulo": "¿QUÉ HACE UN CIENTÍFICO?", "items": [{"txt": "Observa", "emoji": "👀"}, {"txt": "Se pregunta", "emoji": "❓"}, {"txt": "Prueba", "emoji": "🧪"}, {"txt": "Anota", "emoji": "📝"}],
  "voz": ["¿Qué hace un científico?", "*Observa* con atención.", "Se hace *preguntas*.", "*Prueba* con experimentos.", "Y *anota* lo que descubre."]},
 {"t": "linea", "titulo": "TU VIAJE: 10 MISIONES", "eventos": [
   {"fecha": "1", "txt": "Cómo crecemos", "emoji": "🧒"},
   {"fecha": "2", "txt": "Animales y plantas", "emoji": "🐣"},
   {"fecha": "3", "txt": "Calor, frío y fuerzas", "emoji": "🔥"},
   {"fecha": "4", "txt": "El agua y el cielo", "emoji": "🌧️"},
   {"fecha": "5", "txt": "Rocas y museo", "emoji": "🪨"}],
  "voz": ["Tu viaje tiene *10 misiones*. Primero: cómo *crecemos*.", "Vas a conocer *animales* y *plantas*.", "Vas a investigar el *calor*, el *frío* y las fuerzas.", "Vas a seguir el viaje del *agua*.", "¡Y al final, *rocas* y un museo de ciencias!"]},
 {"t": "experimento", "titulo": "UN EXPERIMENTO DE PRUEBA", "variable": "EL SOL", "a": {"cab": "A LA SOMBRA", "emojis": ["🧊", "🌳"], "txt": "Un hielo", "res": "TARDA EN DERRETIRSE"}, "b": {"cab": "AL SOL", "emojis": ["🧊", "☀️"], "txt": "Otro hielo", "res": "¡SE DERRITE RÁPIDO!"},
  "voz": ["Probemos un experimento: dos hielos.", "Uno a la sombra, otro al *sol*.", "¡El del sol se derrite más rápido!"]},
 {"t": "pasos", "titulo": "¿CÓMO SE JUEGA?", "items": [{"txt": "Mirás la clase", "emoji": "🎬"}, {"txt": "Leés el PDF", "emoji": "📄"}, {"txt": "Hacés las actividades", "emoji": "✏️"}],
  "voz": ["Cada misión tiene *niveles*.", "Primero mirás una *clase*, como esta.", "Después leés el *PDF* con tu carpeta.", "Y hacés las *actividades*."]},
 {"t": "frase", "texto": "Al final de cada misión: ¡el NIVEL JEFE!", "emoji": "🏆",
  "voz": ["Al final te espera el *nivel jefe*."]},
 {"t": "consejo", "titulo": "UN CONSEJO", "texto": "Mirá todo con ojos de científico", "emoji": "🔍",
  "voz": ["Un consejo: mirá todo con *ojos de científico*."]},
 {"t": "frase", "texto": "Tu primera misión: cómo crecemos y cambiamos. ¡Vamos!", "emoji": "🚀",
  "voz": ["¿Listos? Primera misión: *cómo crecemos*. ¡Vamos!"]},
]
L = {"slug": "medio-intro-nat2", "subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "materia": "Ciencias Naturales 2", "titulo": "Bienvenidos a Ciencias Naturales 2",
     "sub": "Introducción · Nivel medio", "estilo": "primeros", "escenas": E}
json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', 'medio-intro-nat2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('medio-intro-nat2', len(E), 'escenas')
