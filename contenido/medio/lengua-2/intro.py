# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Introducción de la materia (clase animada de bienvenida).
Mismo molde que las otras introducciones del Medio. Regla de primeros años y vía fonológica (la voz no nombra letras).
Metáfora del año: el cuaderno viajero de Sofi (lo que lee y escribe en segundo grado).
Se carga en la introducción de la materia (subject_id). Genera tools/medio/clase/lecciones/medio-intro-leng2.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
SOFI = {"nombre": "Sofi", "emoji": "👧"}
E = [
 {"t": "historia", "personaje": SOFI, "lugar": "🏫", "lineas": ["Sofi empieza segundo grado.", "Ya lee y escribe.", "¡Tiene un cuaderno viajero!"], "titulo": "¡BIENVENIDOS!", "sub": "a Lengua 2",
  "voz": ["¡Hola! Ella es *Sofi*.", "Ya empezó *segundo grado*: ¡lee y escribe!", "Este año tiene un *cuaderno viajero*.", "¡Bienvenidos a *Lengua 2*!"]},
 {"t": "causas", "causa": {"txt": "Leer y escribir sirve para…", "emoji": "📖"}, "items": [{"txt": "Disfrutar cuentos", "emoji": "🧚"}, {"txt": "Mandar mensajes", "emoji": "✉️"}, {"txt": "Aprender cosas nuevas", "emoji": "🔍"}],
  "voz": ["¿Para qué sirve leer y escribir?", "Para disfrutar *cuentos* y poemas.", "Para mandar *mensajes* y cartas.", "¡Y para *aprender* cosas nuevas!"]},
 {"t": "fichas", "consigna": "Armá la oración", "fichas": ["Sofi", "lee", "un", "cuento."], "desorden": [2, 0, 3, 1], "traduccion": "¡Ya sabés armar oraciones!",
  "voz": ["Probemos. Estas palabras están mezcladas.", "Las ordenamos: Sofi lee un cuento.", "¡Ya sabés armar *oraciones*!"]},
 {"t": "linea", "titulo": "TU VIAJE: 30 MISIONES", "eventos": [
   {"fecha": "1", "txt": "Oraciones y letra cursiva", "emoji": "✍️"},
   {"fecha": "2", "txt": "Cuentos, poemas y fábulas", "emoji": "📚"},
   {"fecha": "3", "txt": "Ortografía y palabras", "emoji": "🔤"},
   {"fecha": "4", "txt": "Cartas, recetas y noticias", "emoji": "📰"},
   {"fecha": "5", "txt": "Escribir un cuento", "emoji": "🖍️"}],
  "voz": ["Tu viaje tiene *30 misiones*. Primero, *oraciones*.", "Vas a leer *cuentos*, poemas y fábulas.", "Vas a escribir *sin errores*.", "Vas a conocer cartas, recetas y *noticias*.", "¡Y al final vas a *escribir un cuento*!"]},
 {"t": "pasos", "titulo": "¿CÓMO SE JUEGA?", "items": [{"txt": "Mirás la clase", "emoji": "🎬"}, {"txt": "Leés el PDF", "emoji": "📄"}, {"txt": "Hacés las actividades", "emoji": "✏️"}],
  "voz": ["Cada misión tiene *niveles*.", "Primero mirás una *clase*, como esta.", "Después leés el *PDF* con tu carpeta.", "Y hacés las *actividades*."]},
 {"t": "frase", "texto": "Al final de cada misión: ¡el NIVEL JEFE!", "emoji": "🏆",
  "voz": ["Al final te espera el *nivel jefe*."]},
 {"t": "consejo", "titulo": "UN CONSEJO", "texto": "Leé un ratito todos los días", "emoji": "📖",
  "voz": ["Un consejo: *leé un ratito* todos los días."]},
 {"t": "frase", "texto": "Tu primera misión: palabras y oraciones. ¡Vamos!", "emoji": "🚀",
  "voz": ["¿Listos? Primera misión: *palabras y oraciones*. ¡Vamos!"]},
]
L = {"slug": "medio-intro-leng2", "subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "materia": "Lengua 2", "titulo": "Bienvenidos a Lengua 2",
     "sub": "Introducción · Nivel medio", "estilo": "primeros", "escenas": E}
json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', 'medio-intro-leng2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('medio-intro-leng2', len(E), 'escenas')
