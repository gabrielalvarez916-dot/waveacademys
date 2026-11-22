# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Clase de introducción de la materia.
Regla de primeros años. Se carga en la introducción de la materia (subject_id).
Genera tools/medio/clase/lecciones/medio-intro-nat1.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
SOFI = {"nombre": "Sofi", "emoji": "👧"}
E = [
 {"t": "historia", "personaje": SOFI, "lugar": "🔍", "lineas": ["Sofi encuentra una hormiga.", "La mira con una lupa.", "¡Quiere saber todo de ella!"], "titulo": "¡BIENVENIDOS!", "sub": "a Ciencias Naturales 1",
  "voz": ["¡Hola! Ella es *Sofi*.", "Sofi mira una hormiga con una *lupa*.", "¡Quiere saber todo de ella!", "¡Bienvenidos a *Ciencias Naturales 1*!"]},
 {"t": "matriz", "titulo": "ESTE AÑO VAMOS A CONOCER", "celdas": [{"cab": "🧍", "txt": "MI CUERPO"}, {"cab": "🐾", "txt": "LOS ANIMALES"}, {"cab": "🌱", "txt": "LAS PLANTAS"}, {"cab": "🌙", "txt": "EL CIELO"}],
  "voz": ["Este año vamos a *descubrir* un montón.", "Vamos a conocer tu *cuerpo*.", "Vamos a mirar los *animales*.", "Vamos a explorar las *plantas*.", "¡Y vamos a observar el *cielo*!"]},
 {"t": "flujo", "titulo": "ASÍ TRABAJA UN CIENTÍFICO", "items": ["OBSERVO", "PREGUNTO", "PRUEBO", "ANOTO"],
  "voz": ["Vamos a trabajar como *científicos*.", "Primero, *observo* con atención.", "Después, me hago una *pregunta*.", "Hago una *prueba*.", "Y *anoto* lo que pasó."]},
 {"t": "bloques", "titulo": "MIS HERRAMIENTAS", "items": [{"cab": "👀", "txt": "MIS SENTIDOS"}, {"cab": "🔍", "txt": "UNA LUPA"}, {"cab": "📓", "txt": "MI CUADERNO"}],
  "voz": ["Un científico usa *herramientas*.", "Usa sus *sentidos*.", "Usa una *lupa*.", "Y su *cuaderno* para anotar."]},
 {"t": "pregunta", "pregunta": "¿Qué hace primero un científico?", "opciones": ["ANOTA", "OBSERVA", "SE VA"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en Sofi y la hormiga.", "¿Qué hace primero un científico?", "¡*Observa* con atención!"]},
 {"t": "consejo", "titulo": "CON CUIDADO", "texto": "Las pruebas, siempre con un adulto", "emoji": "🧑‍🔬",
  "voz": ["Importante: las pruebas, siempre *con un adulto*."]},
 {"t": "frase", "texto": "¡A DESCUBRIR EL MUNDO!", "emoji": "🌍", "color": "sol",
  "voz": ["¡Vamos a *descubrir el mundo* juntos!"]},
]
L = {"slug": "medio-intro-nat1", "subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "materia": "Ciencias Naturales 1", "titulo": "Bienvenidos a Ciencias Naturales 1", "sub": "Introducción · Nivel medio", "estilo": "primeros", "escenas": E}
json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', 'medio-intro-nat1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('medio-intro-nat1', len(E), 'escenas')
