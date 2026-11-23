# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 13 · El abecedario: las 4 clases animadas.
Vía fonológica: la VOZ no nombra letras; dice palabras ancla («la de dedo»). La pantalla muestra las letras.
Metáfora: el álbum completo de Sofi. Genera tools/medio/clase/lecciones/medio-leng1-m13-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '4b70b402-9944-4d69-baf7-b7f0b3cdcb8f', 2: '5826d7a9-3cc5-4068-b1ed-fe5807cea656', 3: 'a39b506d-f193-45cb-9ec3-88be842d8030', 4: '32d175fc-ee16-448e-86b5-746890cf1567'}
TIT = {1: 'Cantar el abecedario', 2: 'Letras mayúsculas y minúsculas', 3: 'Ordenar nombres por la primera letra', 4: 'Buscar palabras en un listado'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📒", "lineas": ["¡Sofi completó su álbum!", "Tiene las 27 letras.", "Ahora las pone en orden."], "titulo": "EL ABECEDARIO", "sub": "en orden",
  "voz": ["¡Sofi completó su *álbum*!", "Tiene las *27 letras*.", "Ahora las pone en orden.", "Hoy: *el abecedario*."]},
 {"t": "definicion", "palabra": "Abecedario", "texto": "Todas las letras, siempre en el mismo orden", "emoji": "🔤",
  "voz": ["El *abecedario* son todas las letras juntas.", "Van siempre en el *mismo orden*."]},
 {"t": "patron", "titulo": "¿QUÉ LETRA SIGUE?", "items": ["A", "B", "C", "D", "E"], "falta": 3, "regla": "Siempre el mismo orden",
  "voz": ["Mirá: la de *avión*, la de *barco*, la de *casa*…", "¿Cuál sigue?", "¡La de *dedo*!"]},
 {"t": "contrarreloj", "titulo": "¿CUÁL VA DESPUÉS?", "segundos": 20, "items": [{"p": "L, M, …", "r": "N"}, {"p": "N, …", "r": "Ñ"}, {"p": "X, Y, …", "r": "Z"}],
  "voz": ["¡Ronda rápida! ¿Cuál va después?", "Después de la de *mamá*: la de *nube*.", "Después de la de *nube*: la de *ñandú*.", "Y al final de todo: la de *zapato*."]},
 {"t": "consejo", "titulo": "DE A PEDACITOS", "texto": "Aprendelo por partes", "emoji": "🧩",
  "voz": ["Truco: aprendé el abecedario *de a pedacitos*."]},
 {"t": "resumen", "items": [["ABECEDARIO", "todas las letras"], ["27", "de la A a la Z"], ["ORDEN", "siempre el mismo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *abecedario* son todas las letras.", "Son *27*: de *avión* a *zapato*.", "Siempre en el *mismo orden*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ÁLBUM", "titular": "¡Cada letra tiene dos formas!", "bajada": "Una grande y una chica", "emoji": "🔠", "titulo": "MAYÚSCULAS", "sub": "y minúsculas",
  "voz": ["¡Noticia: cada letra tiene *dos formas*!", "Una *grande* y una *chica*.", "Hoy: *mayúsculas y minúsculas*."]},
 {"t": "comparar", "a": {"cab": "M", "texto": "mayúscula: la grande", "emoji": "🐘"}, "b": {"cab": "m", "texto": "minúscula: la chica", "emoji": "🐭"}, "signo": "=",
  "voz": ["Esta es la *mayúscula*: la grande.", "Esta es la *minúscula*: la chica.", "¡Son la *misma letra*!"]},
 {"t": "mazo", "titulo": "GRANDE Y CHICA", "items": [{"frente": "A", "dorso": "a", "emoji": "✈️"}, {"frente": "S", "dorso": "s", "emoji": "☀️"}, {"frente": "T", "dorso": "t", "emoji": "🍅"}],
  "voz": ["La de *avión*, grande y chica.", "La de *sol*, grande y chica.", "La de *tomate*, grande y chica."]},
 {"t": "pregunta", "pregunta": "¿Cómo empieza el nombre Sofi?", "opciones": ["Con mayúscula", "Con minúscula"], "correcta": 0,
  "voz": ["¿Cómo empieza el nombre Sofi?", "Pensá: es un nombre.", "¡Con *mayúscula*!"]},
 {"t": "consejo", "titulo": "NOMBRES CON GRANDE", "texto": "Tu nombre empieza con mayúscula", "emoji": "✍️",
  "voz": ["Truco: tu nombre empieza siempre con *mayúscula*."]},
 {"t": "resumen", "items": [["MAYÚSCULA", "la grande"], ["MINÚSCULA", "la chica"], ["NOMBRES", "con mayúscula"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *mayúscula* es la grande.", "La *minúscula* es la chica.", "Los *nombres* empiezan con mayúscula.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Seño Ana", "emoji": "👩‍🏫"}, "mensajes": [{"yo": False, "txt": "Sofi, ¿me ordenás la lista del grado? 📋"}, {"yo": True, "txt": "¡Sí! Por la primera letra"}], "titulo": "ORDENAR", "sub": "nombres",
  "voz": ["La seño le pide a Sofi: ¿me ordenás la lista?", "Sofi responde: ¡sí, por la primera letra!", "Hoy: *ordenar nombres*."]},
 {"t": "transforma", "titulo": "ORDENAMOS LA LISTA", "pasos": [{"txt": "TOMI · ANA · SOFI · BETO", "nota": "sin orden"}, {"txt": "ANA · BETO · …", "nota": "primero la de avión y la de barco"}, {"txt": "ANA · BETO · SOFI · TOMI", "nota": "¡en orden!"}],
  "voz": ["La lista está desordenada.", "Primero *Ana*, la de avión. Después *Beto*, la de barco.", "Después *Sofi* y *Tomi*. ¡En orden!"]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Desorden", "emoji": "🌀"}, "preguntas": [{"p": "CARLA o PEPE, ¿quién va primero?", "r": "CARLA"}, {"p": "LUZ o DANI, ¿quién va primero?", "r": "DANI"}],
  "voz": ["¡Apareció el *Monstruo Desorden*!", "Ordenamos sus listas.", "Carla o Pepe: ¡primero *Carla*!", "Luz o Dani: ¡primero *Dani*! ¡Ganamos!"]},
 {"t": "consejo", "titulo": "MIRÁ EL ABECEDARIO", "texto": "Si dudás, buscá las letras", "emoji": "🔤",
  "voz": ["Truco: si dudás, mirá el *abecedario*."]},
 {"t": "errores", "items": [{"mal": "MATEO antes que DANI", "bien": "DANI antes que MATEO"}],
  "voz": ["Cuidado con este error.", "La de *dedo* va antes: primero *Dani*."]},
 {"t": "resumen", "items": [["MIRAR", "la primera letra"], ["BUSCAR", "en el abecedario"], ["ORDENAR", "la que va antes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Miramos* la primera letra.", "La *buscamos* en el abecedario.", "*Ordenamos*: la que va antes, primero.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "¿Dónde busco ZORRO en una lista en orden?", "segundos": 8, "respuesta": "¡Abajo de todo!", "emoji": "🦊", "titulo": "BUSCAR", "sub": "en un listado",
  "voz": ["Desafío: ¿dónde busco *zorro* en una lista en orden?", "¡*Abajo de todo*! Es la última letra.", "Hoy: *buscar palabras en un listado*."]},
 {"t": "zoom", "niveles": [{"emoji": "📋", "txt": "LISTA DE FRUTAS"}, {"emoji": "🔎", "txt": "BUSCO PERA"}, {"emoji": "⬇️", "txt": "CASI AL FINAL"}, {"emoji": "🍐", "txt": "¡PERA!"}],
  "voz": ["Tenemos una *lista de frutas* en orden.", "Buscamos *pera*.", "Empieza como *pato*: casi al final.", "¡La encontramos!"]},
 {"t": "vof", "afirmacion": "ANA está arriba de todo en una lista en orden", "emoji": "📋", "verdadero": True, "explicacion": "Empieza como AVIÓN, la primera",
  "voz": ["¿Verdadero o falso? Ana está arriba de todo.", "Pensá en la primera letra.", "¡*Verdadero*! Empieza como avión, la primera."]},
 {"t": "pregunta", "pregunta": "GATO, LORO, OSO. ¿Qué va después de LORO?", "opciones": ["OSO", "GATO"], "correcta": 0,
  "voz": ["Lista: gato, loro, oso.", "¿Qué va después de loro?", "¡*Oso*!"]},
 {"t": "consejo", "titulo": "PRINCIPIO, MEDIO O FINAL", "texto": "Pensá dónde está la letra", "emoji": "🧭",
  "voz": ["Truco: ¿está al principio, al medio o al final?"]},
 {"t": "resumen", "items": [["LISTADO", "en orden"], ["BUSCAR", "por la primera letra"], ["RÁPIDO", "sin leer todo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Muchos *listados* están en orden.", "*Buscamos* por la primera letra.", "¡Así encontramos *rápido*!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m13-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 13 · Nivel {n}", "estilo": "primeros", **({"minusculas": True} if n == 2 else {}), "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
