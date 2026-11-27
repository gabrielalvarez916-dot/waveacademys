# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 10 · La tabla pitagórica: las 4 clases animadas.
Metáfora de toda la misión: el mapa del tesoro de Lucas (la tabla es un mapa: fila y columna marcan el lugar).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '0bebe3ef-3c89-4537-9e46-32f83f766a4d', 2: 'f02ee849-bb4d-4dc2-98a8-c6007cf48113', 3: 'e3a4f91b-b697-4045-ba2c-06c631a5b711', 4: 'a5af7d52-f1f6-4107-a4ba-2d3fc99e7121'}
TIT = {1: 'Armar la tabla pitagórica', 2: 'Regularidades en la tabla pitagórica', 3: 'Tablas del 3, 4 y 6', 4: 'Tablas del 7, 8 y 9'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LUCAS = {"nombre": "Lucas", "emoji": "🧭"}

N1 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Lucas encontró un mapa de números!", "bajada": "Todas las tablas en un solo cuadro", "emoji": "🗺️", "titulo": "LA TABLA", "sub": "pitagórica",
  "voz": ["¡Último momento: Lucas encontró un *mapa de números*!", "Tiene todas las tablas en un solo cuadro.", "Hoy: *armar la tabla pitagórica*."]},
 {"t": "grilla", "titulo": "EL MAPA DE LUCAS", "filas": 10, "cols": 10, "resaltar": [{"fila": 2, "col": 3, "txt": "6"}, {"fila": 4, "col": 7, "txt": "28"}],
  "voz": ["Este es el mapa: diez filas y diez columnas.", "Fila del 2, columna del 3: *6*.", "¡Fila del 4, columna del 7: *28*!"]},
 {"t": "definicion", "palabra": "Tabla pitagórica", "texto": "Un cuadro con todas las tablas: fila por columna.", "emoji": "🔢",
  "voz": ["La *tabla pitagórica* tiene todas las tablas juntas.", "Cada casillero es *fila por columna*."]},
 {"t": "escape", "titulo": "COFRES DEL MAPA", "candados": [{"p": "Fila 5, columna 6", "r": "30"}, {"p": "Fila 3, columna 9", "r": "27"}],
  "voz": ["¡Escape! Dos cofres con candado.", "Fila 5, columna 6: cinco por seis, *30*.", "Fila 3, columna 9: tres por nueve, *27*.", "¡Abrimos los cofres!"]},
 {"t": "errores", "items": [{"mal": "Fila 4, columna 7: 4 + 7 = 11", "bien": "Fila 4, columna 7: 4 × 7 = 28"}],
  "voz": ["Ojo con este error.", "En la tabla se *multiplica*, no se suma."]},
 {"t": "resumen", "items": [["FILA", "un número"], ["COLUMNA", "otro número"], ["CRUCE", "fila por columna"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Buscamos la *fila* de un número.", "Después la *columna* del otro.", "Donde se cruzan está el resultado: *fila por columna*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Lucas", "emoji": "🧭"}, "mensajes": [{"yo": False, "txt": "¡El mapa tiene secretos!"}, {"yo": True, "txt": "¿Qué secretos?"}, {"yo": False, "txt": "Hay filas que se repiten distinto"}], "titulo": "SECRETOS", "sub": "de la tabla",
  "voz": ["Lucas escribe: ¡el mapa tiene *secretos*!", "¿Qué secretos?", "Hay filas que se parecen mucho.", "Hoy: *regularidades en la tabla pitagórica*."]},
 {"t": "comparar", "a": {"cab": "FILA DEL 2", "texto": "2, 4, 6, 8", "emoji": "2️⃣"}, "b": {"cab": "FILA DEL 4", "texto": "4, 8, 12, 16", "emoji": "4️⃣"}, "signo": "y",
  "voz": ["La fila del 2: 2, 4, 6, 8.", "La fila del 4: 4, 8, 12, 16.", "¡La del 4 es el *doble*!"]},
 {"t": "datoloco", "texto": "¡La tabla es como un espejo! 3 × 5 da lo mismo que 5 × 3", "emoji": "🪞", "numero": "15",
  "voz": ["¿Sabías que la tabla es como un *espejo*?", "3 por 5 y 5 por 3: *15*."]},
 {"t": "memoria", "titulo": "LA FILA DEL 5", "items": ["5", "10", "15", "20", "25"], "falta": 3,
  "voz": ["Mirá la fila del 5: terminan en 0 o 5.", "Se tapan… ¿cuál desapareció?", "¡Faltaba el *20*!"]},
 {"t": "errores", "items": [{"mal": "4 × 6 y 6 × 4 dan distinto", "bien": "Dan lo mismo: 24"}],
  "voz": ["Ojo con este error.", "Si damos vuelta la cuenta, da *lo mismo*."]},
 {"t": "resumen", "items": [["DOBLE", "fila del 4 y del 2"], ["ESPEJO", "3 × 5 = 5 × 3"], ["FILA DEL 5", "termina en 0 o 5"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La fila del 4 es el *doble*.", "La tabla es un *espejo*: el orden no cambia.", "La fila del 5 termina en *0 o 5*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Lucas tiene 6 cofres con 4 monedas. ¿Cuántas monedas?", "segundos": 8, "respuesta": "¡24!", "emoji": "💰", "titulo": "TABLAS", "sub": "del 3, 4 y 6",
  "voz": ["Desafío: 6 cofres con 4 monedas.", "¿Cuántas monedas hay? ¡*24*!", "Hoy: *las tablas del 3, del 4 y del 6*."]},
 {"t": "escala", "titulo": "LA TABLA DEL 3", "items": [{"txt": "1 × 3 = 3", "emoji": "💰", "valor": 3}, {"txt": "2 × 3 = 6", "emoji": "💰", "valor": 6}, {"txt": "3 × 3 = 9", "emoji": "💰", "valor": 9}, {"txt": "4 × 3 = 12", "emoji": "💰", "valor": 12}],
  "voz": ["Uno por tres: *3*.", "Dos por tres: *6*.", "Tres por tres: *9*.", "¡Cuatro por tres: *12*!"]},
 {"t": "pizarra", "titulo": "TRUCO DEL DOBLE", "lineas": [{"txt": "6 × 2 = 12"}, {"txt": "6 × 4 = 24", "color": "verde", "marca": "subraya"}, {"txt": "7 × 3 = 21"}, {"txt": "7 × 6 = 42", "color": "verde", "marca": "subraya"}],
  "voz": ["6 por 2 es 12.", "El doble: 6 por 4, *24*.", "7 por 3 es 21.", "El doble: 7 por 6, *42*."]},
 {"t": "quiz4", "pregunta": "¿Cuánto es 8 × 4?", "opciones": ["32", "12", "36"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuánto es 8 por 4?", "8 por 2 es 16, y el doble…", "¡*32*!"]},
 {"t": "errores", "items": [{"mal": "6 × 4 = 22", "bien": "6 × 4 = 24: el doble de 12"}],
  "voz": ["Ojo con este error.", "Usá el truco del doble para *controlar*: 24."]},
 {"t": "resumen", "items": [["DEL 3", "de 3 en 3"], ["DEL 4", "doble del 2"], ["DEL 6", "doble del 3"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La tabla del 3 va *de 3 en 3*.", "La del 4 es el *doble* de la del 2.", "La del 6, *doble* de la del 3.", CIERRE]},
]
N4 = [
 {"t": "gancho", "emoji": "🏴‍☠️", "final": "🤔", "titulo": "TABLAS", "sub": "del 7, 8 y 9",
  "voz": ["Las tablas más difíciles guardan el *tesoro más grande*.", "¿Cómo las aprendemos sin perdernos?", "Hoy: *las tablas del 7, del 8 y del 9*."]},
 {"t": "mazo", "titulo": "TRUCO DEL 9", "items": [{"frente": "6 × 9", "dorso": "60 − 6 = 54"}, {"frente": "4 × 9", "dorso": "40 − 4 = 36"}, {"frente": "8 × 9", "dorso": "80 − 8 = 72"}],
  "voz": ["6 por 9: 60 menos 6, *54*.", "4 por 9: 40 menos 4, *36*.", "¡8 por 9: 80 menos 8, *72*!"]},
 {"t": "prediccion", "pregunta": "7 × 4 = 28. ¿Cuánto es 7 × 8?", "a": {"txt": "56", "emoji": "😎"}, "b": {"txt": "32", "emoji": "🤔"}, "correcta": "a", "resultado": "¡56! El doble de 28",
  "voz": ["7 por 4 es 28. ¿Y 7 por 8?", "El 8 es el doble del 4…", "¡*56*, el doble de 28!"]},
 {"t": "contrarreloj", "titulo": "RONDA DEL 7", "segundos": 20, "items": [{"p": "7 × 2", "r": "14"}, {"p": "7 × 5", "r": "35"}, {"p": "7 × 7", "r": "49"}],
  "voz": ["¡Ronda rápida de la tabla del 7!", "7 por 2 es *14*.", "7 por 5 es *35*.", "7 por 7 es *49*."]},
 {"t": "errores", "items": [{"mal": "6 × 9 = 60", "bien": "6 × 9 = 60 − 6 = 54"}],
  "voz": ["Ojo con este error.", "En el truco del 9, *sacamos* el número."]},
 {"t": "resumen", "items": [["DEL 7", "de 7 en 7"], ["DEL 8", "doble del 4"], ["DEL 9", "por 10 menos uno"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La tabla del 7 va *de 7 en 7*.", "La del 8 es el *doble* de la del 4.", "La del 9: por 10 y *sacamos una vez*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m10-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 10 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
