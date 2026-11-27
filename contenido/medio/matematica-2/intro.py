# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Introducción de la materia (clase animada de bienvenida).
Mismo molde que la introducción de Matemática 1, con la metáfora de todo el año: la fábrica de alfajores de la abuela Rosa.
Regla de primeros años. Se carga en la introducción de la materia (subject_id).
Genera tools/medio/clase/lecciones/medio-intro-mat2.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
ROSA = {"nombre": "Rosa", "emoji": "👵"}
E = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["La abuela Rosa tiene una fábrica.", "Hace miles de alfajores.", "¡Y necesita tu ayuda!"], "titulo": "¡BIENVENIDOS!", "sub": "a Matemática 2",
  "voz": ["¡Hola! Ella es la abuela *Rosa*.", "Tiene una *fábrica de alfajores*.", "¡Y este año necesita tu ayuda!", "¡Bienvenidos a *Matemática 2*!"]},
 {"t": "agrupar", "niveles": [{"nombre": "SUELTO", "valor": "1", "icono": "alf"}, {"nombre": "PAQUETE", "valor": "10", "icono": "pack"}, {"nombre": "CAJA", "valor": "100", "icono": "caja"}, {"nombre": "CAMIÓN", "valor": "1.000", "icono": "camion"}], "salto": "×10",
  "voz": ["En la fábrica hay alfajores *sueltos*.", "10 sueltos llenan un *paquete*.", "10 paquetes llenan una *caja*: 100.", "¡Y 10 cajas llenan un *camión*: 1.000!", "¡Este año vamos a contar hasta *1.000*!"]},
 {"t": "quiz4", "pregunta": "¿Cuántos alfajores hay en una caja?", "opciones": ["10", "100", "1.000"], "correcta": 1,
  "voz": ["Probemos. Una caja de Rosa…", "¿Cuántos alfajores tiene?", "¡*100*! ¡Ya sabés un montón!"]},
 {"t": "linea", "titulo": "TU VIAJE: 30 MISIONES", "eventos": [
   {"fecha": "1", "txt": "Los números hasta 1.000", "emoji": "🔢"},
   {"fecha": "2", "txt": "Sumar y restar", "emoji": "➕"},
   {"fecha": "3", "txt": "Multiplicar y repartir", "emoji": "✖️"},
   {"fecha": "4", "txt": "Figuras y planos", "emoji": "🔺"},
   {"fecha": "5", "txt": "Medir, la hora y los datos", "emoji": "⏰"}],
  "voz": ["Tu viaje tiene *30 misiones*. Primero, los números hasta *1.000*.", "Después vas a *sumar* y *restar*.", "Vas a *multiplicar* y repartir.", "Vas a conocer *figuras* y planos.", "¡Y a *medir*, leer la hora y usar datos!"]},
 {"t": "pasos", "titulo": "¿CÓMO SE JUEGA?", "items": [{"txt": "Mirás la clase", "emoji": "🎬"}, {"txt": "Hacés la lección", "emoji": "🧠"}, {"txt": "Hacés las actividades", "emoji": "✏️"}],
  "voz": ["Cada misión tiene *niveles*.", "Primero mirás una *clase*, como esta.", "Después hacés la *lección*: mirás ejemplos y practicás.", "Y hacés las *actividades*."]},
 {"t": "frase", "texto": "Al final de cada misión: ¡el NIVEL JEFE!", "emoji": "🏆",
  "voz": ["Al final te espera el *nivel jefe*."]},
 {"t": "consejo", "titulo": "UN CONSEJO", "texto": "Tené una hoja y tus lápices a mano", "emoji": "🎒",
  "voz": ["Tené una *hoja* y tus lápices a mano."]},
 {"t": "frase", "texto": "Tu primera misión: los números hasta 200. ¡Vamos!", "emoji": "🚀",
  "voz": ["¿Listos? Primera misión: *los números hasta 200*. ¡Vamos!"]},
]
L = {"slug": "medio-intro-mat2", "subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "materia": "Matemática 2", "titulo": "Bienvenidos a Matemática 2",
     "sub": "Introducción · Nivel medio", "estilo": "primeros", "escenas": E}
json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', 'medio-intro-mat2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('medio-intro-mat2', len(E), 'escenas')
