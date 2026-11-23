# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 14 · Listas y carteles: las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Metáfora: Sofi ayuda a ordenar el aula.
Genera tools/medio/clase/lecciones/medio-leng1-m14-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '0bba5bf4-a717-4d45-90ff-5984e6a3310a', 2: '3da1c157-b343-41d4-8db3-055558c3dd88', 3: '027c9df3-8493-4d8f-958b-da5fbd855234', 4: '7d737bc9-2f2f-4945-b6a7-5d774d399f7d'}
TIT = {1: 'Listas para la clase', 2: 'Carteles para el aula', 3: 'Etiquetas con nombres', 4: 'Agenda de la semana'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎒", "lineas": ["Sofi prepara la mochila.", "¡No se quiere olvidar nada!", "Hace una lista."], "titulo": "LISTAS", "sub": "para la clase",
  "voz": ["Sofi prepara la *mochila*.", "¡No se quiere olvidar nada!", "Escribe una *lista*.", "Hoy: *listas para la clase*."]},
 {"t": "definicion", "palabra": "Lista", "texto": "Palabras una abajo de la otra", "emoji": "📝",
  "voz": ["Una *lista* son palabras una abajo de la otra.", "Cada cosa en su renglón."]},
 {"t": "memoria", "titulo": "LA LISTA DE SOFI", "items": ["LÁPIZ", "GOMA", "CUADERNO", "TIJERA"], "falta": 1,
  "voz": ["Mirá la lista de Sofi.", "Se tapan… ¡y una desapareció!", "¡Faltaba la *goma*!"]},
 {"t": "quiz4", "pregunta": "¿Cuál es una lista?", "opciones": ["PAN / LECHE / QUESO", "HABÍA UNA VEZ…", "¡HOLA!", "NO CORRER"], "correcta": 0,
  "voz": ["¿Cuál de estas es una *lista*?", "Buscá palabras una abajo de la otra.", "¡Pan, leche, queso!"]},
 {"t": "consejo", "titulo": "UNA POR RENGLÓN", "texto": "Cada cosa en su renglón", "emoji": "📏",
  "voz": ["Truco: cada cosa va en *su renglón*."]},
 {"t": "resumen", "items": [["LISTA", "una abajo de la otra"], ["SIRVE", "para no olvidar"], ["MARCAR", "lo que ya está"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *lista*: una palabra abajo de la otra.", "Sirve para *no olvidarnos*.", "*Marcamos* lo que ya guardamos.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ESCUELA", "titular": "¡Faltan carteles en el aula!", "bajada": "Sofi los va a hacer", "emoji": "🪧", "titulo": "CARTELES", "sub": "para el aula",
  "voz": ["¡Noticia: faltan *carteles* en la escuela!", "Sofi los va a hacer.", "Hoy: *carteles para el aula*."]},
 {"t": "pistas", "problema": "¿Qué cartel es?", "pistas": ["Va en una puerta", "Ahí hay muchos libros", "Hay que hablar bajito"], "respuesta": "BIBLIOTECA 📚",
  "voz": ["Adivinanza: ¿qué cartel es?", "Pista uno: va en una puerta.", "Pista dos: ahí hay muchos libros.", "Pista tres: hay que hablar bajito.", "¡*Biblioteca*!"]},
 {"t": "unir", "titulo": "CADA CARTEL EN SU LUGAR", "pares": [["🍽️", "COMEDOR"], ["🛝", "PATIO"], ["🚽", "BAÑO"]],
  "voz": ["Ponemos cada cartel en su lugar.", "Donde comemos: *comedor*.", "Donde jugamos: *patio*.", "Y la puerta del *baño*."]},
 {"t": "consejo", "titulo": "CORTO Y GRANDE", "texto": "Así se lee de lejos", "emoji": "🔭",
  "voz": ["Truco: el cartel es *corto* y con letras *grandes*."]},
 {"t": "errores", "items": [{"mal": "Un cartel con un cuento largo", "bien": "Un cartel con pocas palabras"}],
  "voz": ["Cuidado con este error.", "El cartel no cuenta historias: dice *lo justo*."]},
 {"t": "resumen", "items": [["CARTEL", "pocas palabras"], ["LETRAS", "grandes"], ["AVISA", "qué hay o qué hacer"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *cartel* tiene pocas palabras.", "Con letras *grandes*.", "*Avisa* qué hay o qué hacer.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué etiqueta va en una caja con pelotas?", "segundos": 8, "respuesta": "¡PELOTAS!", "emoji": "⚽", "titulo": "ETIQUETAS", "sub": "con nombres",
  "voz": ["Desafío: ¿qué etiqueta va en una caja con pelotas?", "¡*Pelotas*!", "Hoy: *etiquetas con nombres*."]},
 {"t": "definicion", "palabra": "Etiqueta", "texto": "Dice qué hay adentro o de quién es", "emoji": "🏷️",
  "voz": ["Una *etiqueta* es un papelito.", "Dice qué hay adentro o *de quién es*."]},
 {"t": "completa", "antes": "Caja de", "despues": "", "opciones": ["TIJERAS ✂️", "PERRO 🐶"], "correcta": 0,
  "voz": ["Esta caja tiene tijeras. La etiqueta dice: caja de…", "¿Tijeras o perro?", "¡*Tijeras*!"]},
 {"t": "escape", "titulo": "EL ARMARIO DEL AULA", "candados": [{"p": "Caja con ✏️", "r": "LÁPICES"}, {"p": "Caja con 🟣🟢", "r": "PLASTILINA"}, {"p": "El cuaderno de Sofi", "r": "SOFI"}],
  "voz": ["¡Para abrir el armario, ponemos las etiquetas!", "La caja de *lápices*.", "La caja de *plastilina*.", "Y el cuaderno con el nombre: *Sofi*.", "¡Abrimos el armario!"]},
 {"t": "consejo", "titulo": "CLARA Y CORTA", "texto": "Una o dos palabras alcanzan", "emoji": "✍️",
  "voz": ["Truco: en la etiqueta, *una o dos palabras* alcanzan."]},
 {"t": "resumen", "items": [["ETIQUETA", "qué es o de quién"], ["CORTA", "una o dos palabras"], ["NOMBRE", "en tus cosas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *etiqueta* dice qué es o de quién.", "Es *corta*.", "Tu *nombre* va en tus cosas.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Qué día tenemos música? 🎵"}, {"yo": True, "txt": "¡Miro la agenda!"}], "titulo": "LA AGENDA", "sub": "de la semana",
  "voz": ["Tomi pregunta: ¿qué día tenemos música?", "Sofi responde: ¡miro la agenda!", "Hoy: *la agenda de la semana*."]},
 {"t": "linea", "titulo": "LA AGENDA DEL GRADO", "eventos": [{"fecha": "LUNES", "txt": "Música", "emoji": "🎵"}, {"fecha": "MARTES", "txt": "Educación física", "emoji": "🏃"}, {"fecha": "MIÉRCOLES", "txt": "Biblioteca", "emoji": "📚"}, {"fecha": "JUEVES", "txt": "Plástica", "emoji": "🎨"}, {"fecha": "VIERNES", "txt": "Juegos", "emoji": "🎲"}],
  "voz": ["El *lunes*: música.", "El *martes*: educación física.", "El *miércoles*: biblioteca.", "El *jueves*: plástica.", "Y el *viernes*: ¡juegos!"]},
 {"t": "tipeo", "titulo": "¿QUÉ DÍA SIGUE?", "items": [{"p": "LUNES, …", "r": "MARTES"}, {"p": "JUEVES, …", "r": "VIERNES"}],
  "voz": ["Después del lunes: *martes*.", "Después del jueves: *viernes*."]},
 {"t": "pregunta", "pregunta": "¿Qué día hay música?", "opciones": ["LUNES", "VIERNES"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué día hay música?", "Buscá en la agenda.", "¡El *lunes*!"]},
 {"t": "consejo", "titulo": "BUSCÁ EL DÍA", "texto": "Primero el día, después leé al lado", "emoji": "🔎",
  "voz": ["Truco: primero buscá *el día*, después leé al lado."]},
 {"t": "resumen", "items": [["SEMANA", "cinco días de escuela"], ["AGENDA", "qué hacemos"], ["LEER", "buscar el día"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La semana tiene *cinco días* de escuela.", "La *agenda* dice qué hacemos.", "*Buscamos* el día y leemos.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m14-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 14 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
