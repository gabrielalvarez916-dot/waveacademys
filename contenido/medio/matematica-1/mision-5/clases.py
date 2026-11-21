# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 5 · Comparar y ordenar números: las 4 clases animadas.
Metáfora: las bolitas de Sofi y Tomi y la carrera de la escuela. Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat1-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '70ce9267-77da-470e-8099-42de1f6c27e0', 2: 'c39b492e-8ae9-456c-aa2c-aaf5a0ae2bca', 3: '9386a6b9-fbdf-4f49-a16c-e3838e0e7ab3', 4: '27ce7479-66d1-42d4-afae-c3a77c150de3'}
TIT = {1: 'Mayor y menor', 2: 'Ordenar de menor a mayor', 3: 'Ordenar de mayor a menor', 4: 'La recta numérica'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
BOL = {"cabD": "BOLSITAS DE 10", "cabU": "SUELTAS"}

N1 = [
 {"t": "historia", "personaje": {"nombre": "Sofi", "emoji": "👧"}, "lugar": "🔵", "lineas": ["Sofi y Tomi juegan a las bolitas.", "Sofi tiene 34.", "Tomi tiene 43."], "titulo": "MAYOR", "sub": "y menor",
  "voz": ["Sofi y Tomi juegan a las *bolitas*.", "Sofi tiene 34 bolitas.", "Tomi tiene 43. ¿Quién tiene más?", "Hoy: *mayor y menor*."]},
 {"t": "cdu", "d": 3, "u": 4, "texto": "Sofi: 34 bolitas", **BOL,
  "voz": ["Sofi guarda sus bolitas en bolsitas de 10.", "Bolsitas: 10, 20, 30.", "Sueltas: 31, 32, 33, 34.", "¡Sofi tiene *34*!"]},
 {"t": "cdu", "d": 4, "u": 3, "texto": "Tomi: 43 bolitas", **BOL,
  "voz": ["Ahora, las bolitas de Tomi.", "Bolsitas: 10, 20, 30, 40.", "Sueltas: 41, 42, 43.", "¡Tomi tiene *43*!"]},
 {"t": "balanza", "izq": {"cab": "34", "items": ["3 bolsitas", "4 sueltas"]}, "der": {"cab": "43", "items": ["4 bolsitas", "3 sueltas"]}, "gana": "der",
  "voz": ["Sofi tiene *3 bolsitas*.", "Tomi tiene *4 bolsitas*.", "¡Más bolsitas, más bolitas: *43 es mayor*!"]},
 {"t": "consejo", "titulo": "MIRÁ LAS DECENAS", "texto": "Primero mirá la primera cifra", "emoji": "👀",
  "voz": ["Truco: para comparar, mirá primero las *decenas*."]},
 {"t": "pregunta", "pregunta": "¿Cuál es mayor: 56 o 65?", "opciones": ["56", "65"], "correcta": 1,
  "voz": ["Ahora vos. Mirá bien estos números.", "¿Cuál es *mayor*: 56 o 65?", "¡*65*! Tiene 6 decenas."]},
 {"t": "resumen", "items": [["MAYOR", "tiene más"], ["MENOR", "tiene menos"], ["DECENAS", "se miran primero"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *mayor* tiene más.", "El *menor* tiene menos.", "Primero mirá las *decenas*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Ordená de menor a mayor: 25, 52, 12", "segundos": 8, "respuesta": "12, 25, 52", "emoji": "🏃", "titulo": "DE MENOR", "sub": "a mayor",
  "voz": ["Desafío: ordená de menor a mayor: 25, 52 y 12.", "¡12, 25 y 52!", "Hoy: *ordenar de menor a mayor*."]},
 {"t": "orden", "titulo": "LA CARRERA DE LA ESCUELA", "etq1": "DESORDENADOS", "etq2": "DE MENOR A MAYOR",
  "items": [{"txt": "18", "emoji": "👧"}, {"txt": "36", "emoji": "👦"}, {"txt": "59", "emoji": "🧒"}, {"txt": "71", "emoji": "👧"}], "relato": [2, 0, 3, 1],
  "voz": ["Los corredores tienen su número.", "Están desordenados: 59, 18, 71, 36.", "De menor a mayor: 18, 36, 59, 71."]},
 {"t": "consejo", "titulo": "EMPEZÁ POR EL MÁS CHICO", "texto": "Buscá el menor y ponelo primero", "emoji": "🔍",
  "voz": ["Truco: buscá el *más chico* y ponelo primero."]},
 {"t": "recta", "min": 0, "max": 100, "paso": 10, "marcas": [{"v": 18, "txt": "18"}, {"v": 36, "txt": "36"}, {"v": 59, "txt": "59"}, {"v": 71, "txt": "71"}],
  "voz": ["En la recta se ve el orden.", "El *18*.", "El *36*.", "El *59*.", "¡Y el *71*, el más grande!"]},
 {"t": "pregunta", "pregunta": "De menor a mayor, ¿cuál va primero?", "opciones": ["47", "74", "40"], "correcta": 2,
  "voz": ["Ahora vos. Ordenamos 47, 74 y 40.", "¿Cuál va *primero*, de menor a mayor?", "¡El *40*! Es el más chico."]},
 {"t": "errores", "items": [{"mal": "Mirar solo la última cifra", "bien": "Mirar primero las decenas"}],
  "voz": ["Ojo con este error.", "Para ordenar, mirá primero las *decenas*."]},
 {"t": "resumen", "items": [["MENOR A MAYOR", "del chico al grande"], ["PRIMERO", "el más chico"], ["DECENAS", "se miran primero"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Menor a mayor*: del chico al grande.", "Primero va el *más chico*.", "Mirá primero las *decenas*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "🏆", "final": "🥇", "titulo": "DE MAYOR", "sub": "a menor",
  "voz": ["¡Terminó la carrera de la escuela!", "¿Quién hizo más puntos? Los ordenamos.", "Hoy: *ordenar de mayor a menor*."]},
 {"t": "orden", "titulo": "LOS PUNTOS", "etq1": "DESORDENADOS", "etq2": "DE MAYOR A MENOR",
  "items": [{"txt": "92", "emoji": "🥇"}, {"txt": "75", "emoji": "🥈"}, {"txt": "48", "emoji": "🥉"}, {"txt": "30", "emoji": "🏅"}], "relato": [2, 0, 3, 1],
  "voz": ["Mirá los puntos de cada equipo.", "Desordenados: 48, 92, 30, 75.", "De mayor a menor: 92, 75, 48, 30."]},
 {"t": "comparar", "a": {"cab": "MENOR A MAYOR", "texto": "12, 25, 52", "emoji": "📈"}, "b": {"cab": "MAYOR A MENOR", "texto": "52, 25, 12", "emoji": "📉"}, "signo": "o",
  "voz": ["De menor a mayor, empezamos por el *más chico*.", "De mayor a menor, empezamos por el *más grande*.", "¡Es al revés!"]},
 {"t": "orden", "titulo": "UNO DIFÍCIL", "etq1": "DESORDENADOS", "etq2": "DE MAYOR A MENOR",
  "items": [{"txt": "99", "emoji": "⭐"}, {"txt": "90", "emoji": "⭐"}, {"txt": "19", "emoji": "⭐"}, {"txt": "9", "emoji": "⭐"}], "relato": [3, 1, 2, 0],
  "voz": ["¡Ahora, uno difícil!", "Desordenados: 9, 90, 19 y 99.", "De mayor a menor: 99, 90, 19, 9."]},
 {"t": "pregunta", "pregunta": "De mayor a menor, ¿cuál va primero?", "opciones": ["38", "83", "80"], "correcta": 1,
  "voz": ["Ahora vos. Ordenamos 38, 83 y 80.", "¿Cuál va *primero*, de mayor a menor?", "¡El *83*! Es el más grande."]},
 {"t": "consejo", "titulo": "EMPEZÁ POR EL MÁS GRANDE", "texto": "Buscá el mayor y ponelo primero", "emoji": "🏆",
  "voz": ["Truco: buscá el *más grande* y ponelo primero."]},
 {"t": "resumen", "items": [["MAYOR A MENOR", "del grande al chico"], ["PRIMERO", "el más grande"], ["AL REVÉS", "de menor a mayor"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Mayor a menor*: del grande al chico.", "Primero va el *más grande*.", "Es al revés que de menor a mayor.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": {"nombre": "Tomi", "emoji": "👦"}, "lugar": "🟨", "lineas": ["Tomi juega a la rayuela gigante.", "Cada casillero tiene un número.", "¡Es una recta numérica!"], "titulo": "LA RECTA", "sub": "numérica",
  "voz": ["Tomi juega en una *rayuela gigante*.", "Cada casillero tiene su número.", "¡Es una *recta numérica*!", "Hoy: *la recta numérica*."]},
 {"t": "recta", "min": 0, "max": 100, "paso": 10, "marcas": [{"v": 30, "txt": "30"}, {"v": 70, "txt": "70"}],
  "voz": ["La recta va del 0 al 100.", "Acá está el *30*.", "Y acá el *70*: más a la derecha, más grande."]},
 {"t": "consejo", "titulo": "A LA DERECHA", "texto": "Más a la derecha, más grande", "emoji": "➡️",
  "voz": ["Truco: *más a la derecha*, más grande."]},
 {"t": "saltos", "titulo": "SALTOS DE TOMI", "min": 0, "max": 20, "inicio": 4, "saltos": [{"a": 3, "txt": "+3"}, {"a": 5, "txt": "+5"}, {"a": -2, "txt": "−2"}],
  "voz": ["Tomi empieza en el 4.", "Salta 3: llega al *7*.", "Salta 5 más: llega al *12*.", "Vuelve 2: llega al *10*."]},
 {"t": "recta", "min": 40, "max": 50, "paso": 1, "marcas": [{"v": 46, "txt": "46"}],
  "voz": ["¿Dónde está el 46?", "Entre el 40 y el 50, más cerca del *50*."]},
 {"t": "pregunta", "pregunta": "¿Cuál está más a la derecha?", "opciones": ["29", "92"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la recta.", "¿Cuál está *más a la derecha*: 29 o 92?", "¡El *92*! Es el mayor."]},
 {"t": "resumen", "items": [["LA RECTA", "números en orden"], ["DERECHA", "más grande"], ["SALTOS", "para adelante o atrás"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la recta, los números van *en orden*.", "*Más a la derecha*, más grande.", "Podemos *saltar* para adelante o para atrás.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m5-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 5 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
