# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Introducción de la materia (clase animada de bienvenida).
Mismo molde que las otras introducciones del Medio. Regla de primeros años.
Metáfora del año: Lola, reportera del barrio con su micrófono (pregunta, mira, escucha y cuenta).
Se carga en la introducción de la materia (subject_id). Genera tools/medio/clase/lecciones/medio-intro-soc2.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
LOLA = {"nombre": "Lola", "emoji": "👧🎤"}
E = [
 {"t": "historia", "personaje": LOLA, "lugar": "🏘️", "lineas": ["Lola empieza segundo grado.", "Tiene un micrófono nuevo.", "¡Quiere saber cómo vive la gente!"], "titulo": "¡BIENVENIDOS!", "sub": "a Ciencias Sociales 2",
  "voz": ["¡Hola! Ella es *Lola*. Hay *10 misiones*.", "Empieza *segundo grado* con un *micrófono* nuevo.", "¡Quiere saber cómo vive la gente!", "¡Bienvenidos a *Ciencias Sociales 2*!"]},
 {"t": "pasos", "titulo": "¿QUÉ HACE UNA REPORTERA?", "items": [{"txt": "Pregunta", "emoji": "🎤"}, {"txt": "Mira", "emoji": "👀"}, {"txt": "Escucha", "emoji": "👂"}, {"txt": "Cuenta", "emoji": "📰"}],
  "voz": ["¿Qué hace una *reportera*?", "*Pregunta* a la gente.", "*Mira* con atención.", "*Escucha* las respuestas.", "Y *cuenta* lo que descubrió."]},
 {"t": "linea", "titulo": "TU VIAJE: 10 MISIONES", "eventos": [
   {"fecha": "1", "txt": "Cómo se hacen las cosas", "emoji": "🏭"},
   {"fecha": "2", "txt": "Trabajos y normas", "emoji": "👷"},
   {"fecha": "3", "txt": "La ciudad y el campo", "emoji": "🚌"},
   {"fecha": "4", "txt": "La vida de antes", "emoji": "🕯️"},
   {"fecha": "5", "txt": "Derechos para todos", "emoji": "🤝"}],
  "voz": ["Primero: cómo se *hacen* las cosas.", "Vas a conocer *trabajos* y normas.", "Vas a recorrer la *ciudad* y el *campo*.", "Vas a viajar a la vida de *antes*.", "¡Y vas a aprender que todos tenemos *derechos*!"]},
 {"t": "transforma", "titulo": "UNA NOTA DE PRUEBA", "pasos": [{"txt": "TRIGO 🌾", "nota": "en el campo"}, {"txt": "HARINA 🥣", "nota": "en el molino"}, {"txt": "PAN 🍞", "nota": "¡en la panadería!"}],
  "voz": ["Primera nota de Lola: del *trigo*…", "…a la *harina*…", "…¡al *pan*! Muchas personas trabajaron."]},
 {"t": "pasos", "titulo": "¿CÓMO SE JUEGA?", "items": [{"txt": "Mirás la clase", "emoji": "🎬"}, {"txt": "Leés el PDF", "emoji": "📄"}, {"txt": "Hacés las actividades", "emoji": "✏️"}],
  "voz": ["Cada misión tiene *niveles*.", "Primero mirás una *clase*, como esta.", "Después leés el *PDF* con tu carpeta.", "Y hacés las *actividades*."]},
 {"t": "frase", "texto": "Al final de cada misión: ¡el NIVEL JEFE!", "emoji": "🏆",
  "voz": ["Al final te espera el *nivel jefe*."]},
 {"t": "consejo", "titulo": "UN CONSEJO", "texto": "Preguntá siempre, como una reportera", "emoji": "🎤",
  "voz": ["Un consejo: *preguntá* siempre, como Lola."]},
 {"t": "frase", "texto": "Tu primera misión: de la materia prima al producto. ¡Vamos!", "emoji": "🚀",
  "voz": ["¿Listos? Primera misión: *cómo se hacen las cosas*. ¡Vamos!"]},
]
L = {"slug": "medio-intro-soc2", "subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "materia": "Ciencias Sociales 2", "titulo": "Bienvenidos a Ciencias Sociales 2",
     "sub": "Introducción · Nivel medio", "estilo": "primeros", "escenas": E}
json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', 'medio-intro-soc2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('medio-intro-soc2', len(E), 'escenas')
