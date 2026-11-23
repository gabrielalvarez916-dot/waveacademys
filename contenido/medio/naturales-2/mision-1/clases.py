# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 1 · Cómo crecemos y cambiamos: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador con su lupa.
Genera tools/medio/clase/lecciones/medio-nat2-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '1db8ac06-84e8-4450-93d8-bec72adac062', 2: '94d553cc-6480-4814-894a-6dd8764b6435', 3: 'e0521561-747e-481e-9b67-a825b4b340cf', 4: '1d576a2f-c7c6-4364-9430-715d77e52381'}
TIT = {1: 'Antes y ahora: cómo cambié', 2: 'Lo que necesita cada edad', 3: 'Alimentos para crecer', 4: 'Las vacunas y la salud'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "📸", "lineas": ["Tomi encontró una foto vieja.", "¡Es él, de bebé!", "¿Cuánto cambió?"], "titulo": "ANTES", "sub": "y ahora",
  "voz": ["Tomi, el científico, encontró una *foto vieja*.", "¡Es él, de bebé!", "¿Cuánto cambió?", "Hoy: *antes y ahora*."]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "👶", "texto": "Gateaba y tomaba mamadera"}, "despues": {"cab": "AHORA", "emoji": "🧒", "texto": "Corre, lee y come de todo"},
  "voz": ["*Antes*, Tomi gateaba y tomaba mamadera.", "*Ahora* corre, lee y come de todo. ¡Creció!"]},
 {"t": "linea", "titulo": "LA VIDA DE TOMI", "eventos": [{"fecha": "0", "txt": "Nació", "emoji": "👶"}, {"fecha": "1", "txt": "Caminó", "emoji": "🚶"}, {"fecha": "3", "txt": "Fue al jardín", "emoji": "🧸"}, {"fecha": "7", "txt": "Segundo grado", "emoji": "🎒"}],
  "voz": ["Cuando *nació*, era chiquito.", "Al año, empezó a *caminar*.", "A los tres, fue al *jardín*.", "¡Y ahora está en *segundo grado*!"]},
 {"t": "pregunta", "pregunta": "¿Qué hacía Tomi de bebé?", "opciones": ["GATEABA", "LEÍA"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué hacía Tomi de bebé?", "Pensá en un bebé.", "¡*Gateaba*!"]},
 {"t": "consejo", "titulo": "CADA UNO A SU RITMO", "texto": "Todos crecemos, pero no igual", "emoji": "🌱",
  "voz": ["Truco: todos crecemos, cada uno *a su ritmo*."]},
 {"t": "resumen", "items": [["CRECER", "es cambiar"], ["ANTES", "bebé"], ["AHORA", "más alto y fuerte"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Crecer* es cambiar.", "*Antes* éramos bebés.", "*Ahora* somos más altos y fuertes.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué necesita un bebé para vivir?", "segundos": 8, "respuesta": "¡Que lo cuiden!", "emoji": "👶", "titulo": "CADA EDAD", "sub": "lo que necesita",
  "voz": ["Desafío: ¿qué necesita un bebé?", "¡Que lo *cuiden*, lo alimenten y lo quieran!", "Hoy: *lo que necesita cada edad*."]},
 {"t": "ciclo", "titulo": "LAS ETAPAS DE LA VIDA", "items": ["BEBÉ 👶", "NIÑO 🧒", "ADOLESCENTE 🧑", "ADULTO 🧔"],
  "voz": ["La vida tiene *etapas*.", "Primero somos *bebés*.", "Después, *niños*.", "Después, *adolescentes*.", "Y después, *adultos*."]},
 {"t": "matriz", "titulo": "LO QUE NECESITAMOS", "celdas": [{"cab": "BEBÉ", "txt": "Que lo cuiden"}, {"cab": "NIÑO", "txt": "Jugar y aprender"}, {"cab": "ADOLESCENTE", "txt": "Aprender y tener amigos"}, {"cab": "TODOS", "txt": "Comer, dormir y amor"}],
  "voz": ["Cada edad necesita algo.", "El *bebé*: que lo cuiden.", "El *niño*: jugar y aprender.", "El *adolescente*: aprender y tener amigos.", "*Todos*: comer, dormir y amor."]},
 {"t": "pregunta", "pregunta": "¿Quién usa pañales?", "opciones": ["EL BEBÉ", "EL ADULTO"], "correcta": 0,
  "voz": ["Ahora vos: ¿quién usa pañales?", "Pensá en las etapas.", "¡El *bebé*!"]},
 {"t": "consejo", "titulo": "CUIDARNOS", "texto": "En cada edad necesitamos cuidados", "emoji": "🤗",
  "voz": ["Truco: en *todas* las edades necesitamos cuidados."]},
 {"t": "resumen", "items": [["ETAPAS", "bebé, niño, adolescente, adulto"], ["BEBÉ", "que lo cuiden"], ["TODOS", "comer, dormir, jugar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *etapas*: bebé, niño, adolescente, adulto.", "El *bebé* necesita que lo cuiden.", "*Todos* necesitamos comer, dormir y jugar.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "LABORATORIO", "titular": "¿Qué comida nos ayuda a crecer?", "bajada": "Tomi investiga", "emoji": "🔬", "titulo": "ALIMENTOS", "sub": "para crecer",
  "voz": ["¡Pregunta de laboratorio: qué comida nos ayuda a crecer?", "Tomi *investiga*.", "Hoy: *alimentos para crecer*."]},
 {"t": "experimento", "titulo": "¿QUÉ PLATO AYUDA MÁS?", "variable": "LO QUE COMEMOS", "a": {"cab": "SOLO GOLOSINAS", "emojis": ["🍬", "🍭"], "txt": "Todos los días", "res": "POCA ENERGÍA"}, "b": {"cab": "PLATO VARIADO", "emojis": ["🥕", "🍗", "🥛"], "txt": "De todo un poco", "res": "¡CRECEMOS SANOS!"},
  "voz": ["Comparamos dos formas de comer.", "Solo golosinas: nos da *poca energía*.", "Un plato *variado*: ¡crecemos sanos!"]},
 {"t": "clasificar", "cajas": [{"cab": "FRUTAS Y VERDURAS", "emoji": "🥕"}, {"cab": "LECHE Y QUESOS", "emoji": "🥛"}, {"cab": "CARNES Y HUEVOS", "emoji": "🍗"}], "fichas": [{"txt": "MANZANA", "caja": 0}, {"txt": "ZANAHORIA", "caja": 0}, {"txt": "YOGUR", "caja": 1}, {"txt": "HUEVO", "caja": 2}],
  "voz": ["Separamos los alimentos en grupos.", "Manzana y zanahoria: *frutas y verduras*.", "Yogur: *leche y quesos*.", "Huevo: *carnes y huevos*."]},
 {"t": "quiz4", "pregunta": "¿Cuál es la mejor bebida?", "opciones": ["GASEOSA", "AGUA", "JUGO EN POLVO", "BEBIDA DULCE"], "correcta": 1,
  "voz": ["¿Cuál es la mejor bebida?", "Pensá en lo más sano.", "¡El *agua*!"]},
 {"t": "consejo", "titulo": "COLORES EN EL PLATO", "texto": "Un plato con colores tiene de todo", "emoji": "🌈",
  "voz": ["Truco: un plato con *muchos colores* tiene de todo."]},
 {"t": "resumen", "items": [["VARIADO", "de todo un poco"], ["GRUPOS", "frutas, leche, carnes"], ["AGUA", "la mejor bebida"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Comemos *variado*.", "Hay *grupos* de alimentos.", "El *agua* es la mejor bebida.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Mamá", "emoji": "👩"}, "mensajes": [{"yo": False, "txt": "Mañana vamos al centro de salud 🏥"}, {"yo": True, "txt": "¿Para qué, mamá?"}, {"yo": False, "txt": "¡Te toca una vacuna! 💉"}], "titulo": "LA SALUD", "sub": "y las vacunas",
  "voz": ["Mamá le escribe a Tomi.", "Mañana vamos al centro de salud.", "¿Para qué, mamá?", "¡Te toca una *vacuna*! Hoy: *la salud*."]},
 {"t": "definicion", "palabra": "Vacuna", "texto": "Ayuda al cuerpo a defenderse de algunas enfermedades", "emoji": "💉",
  "voz": ["La *vacuna* ayuda al cuerpo a *defenderse*.", "Se anota en la *libreta de vacunas*."]},
 {"t": "mazo", "titulo": "HÁBITOS SANOS", "items": [{"frente": "🧼", "dorso": "LAVARSE LAS MANOS", "emoji": "🧼"}, {"frente": "😴", "dorso": "DORMIR BIEN", "emoji": "😴"}, {"frente": "⚽", "dorso": "JUGAR Y MOVERSE", "emoji": "⚽"}],
  "voz": ["*Lavarse las manos*: saca los microbios.", "*Dormir bien*: el cuerpo descansa.", "*Jugar y moverse*: el cuerpo se pone fuerte."]},
 {"t": "vof", "afirmacion": "Lavarse las manos no sirve para nada", "emoji": "🧼", "verdadero": False, "explicacion": "Nos protege de los microbios",
  "voz": ["¿Verdadero o falso? Lavarse las manos no sirve.", "Pensá en los microbios…", "¡*Falso*! Nos protege."]},
 {"t": "consejo", "titulo": "TODOS LOS DÍAS", "texto": "Cuidar la salud es de todos los días", "emoji": "📅",
  "voz": ["Truco: cuidar la salud es cosa de *todos los días*."]},
 {"t": "resumen", "items": [["VACUNAS", "ayudan a defenderse"], ["LIBRETA", "ahí se anotan"], ["HÁBITOS", "manos, dormir, jugar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *vacunas* ayudan a defenderse.", "Se anotan en la *libreta*.", "Y tenemos *hábitos sanos*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m1-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
