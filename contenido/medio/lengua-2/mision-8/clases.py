# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 8 · Fichas informativas: las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Metáfora: el cuaderno viajero de Sofi y su ficha del yaguareté.
Genera tools/medio/clase/lecciones/medio-leng2-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '52559f1a-9d15-4bc3-8a2e-bc0d7eeda5bb', 2: 'cd39e8a1-aa50-4dff-afaa-e5c1336cad29', 3: 'f0ee9267-5926-41ac-8151-66ff53c8438d', 4: 'e3b5222f-1a48-4b30-aee0-a4fde4f734d1'}
TIT = {1: 'Elegir un tema', 2: 'Buscar datos', 3: 'Escribir la ficha', 4: 'Revisar y compartir la ficha'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📒", "lineas": ["Sofi leyó la lámina del hornero.", "Ahora quiere hacer su propia ficha.", "¿Sobre qué será?"], "titulo": "ELEGIR", "sub": "un tema",
  "voz": ["Sofi leyó la lámina del hornero.", "Ahora quiere hacer *su propia ficha*.", "¿Sobre qué será?", "Hoy: *elegir un tema*."]},
 {"t": "definicion", "palabra": "Tema", "texto": "De qué va a tratar la ficha", "emoji": "🎯",
  "voz": ["El *tema* es de qué va a tratar la ficha.", "Lo elegimos primero."]},
 {"t": "dilema", "situacion": "Sofi tiene que elegir un tema", "emoji": "🤔", "a": {"txt": "Todos los animales", "consecuencia": "¡Es demasiado para una hoja!", "emoji": "🌍"}, "b": {"txt": "El yaguareté", "consecuencia": "¡Uno solo, se cuenta bien!", "emoji": "🐆"},
  "voz": ["Sofi duda: ¿qué tema elige?", "Todos los animales: ¡es *demasiado* para una hoja!", "El *yaguareté*: uno solo, ¡se cuenta bien!"]},
 {"t": "quiz4", "pregunta": "¿Cuál es un buen tema?", "opciones": ["TODO EL MUNDO", "EL HORNERO", "TODAS LAS PLANTAS", "TODOS LOS PAÍSES"], "correcta": 1,
  "voz": ["¿Cuál es un buen tema para una ficha?", "Buscá el que sea *uno solo*.", "¡*El hornero*! Es un tema chico."]},
 {"t": "consejo", "titulo": "UNO SOLO", "texto": "Un tema chico se cuenta mejor", "emoji": "☝️",
  "voz": ["Truco: un tema *chico* se cuenta mejor."]},
 {"t": "resumen", "items": [["FICHA", "datos reales"], ["TEMA", "de qué trata"], ["UNO SOLO", "un tema chico"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *ficha* tiene datos reales.", "El *tema* dice de qué trata.", "Elegimos *uno solo*, un tema chico.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Qué sabés del yaguareté? 🐆"}, {"yo": True, "txt": "¡Poco! Voy a buscar datos"}], "titulo": "BUSCAR", "sub": "datos",
  "voz": ["Tomi pregunta: ¿qué sabés del yaguareté?", "Sofi responde: ¡poco! Voy a buscar datos.", "Hoy: *buscar datos*."]},
 {"t": "zoom", "niveles": [{"emoji": "📚", "txt": "EN LIBROS"}, {"emoji": "🖼️", "txt": "EN LÁMINAS"}, {"emoji": "👩‍🏫", "txt": "PREGUNTANDO A UN ADULTO"}, {"emoji": "💻", "txt": "INTERNET CON UN ADULTO"}],
  "voz": ["Buscamos datos en *libros*.", "También en *láminas*.", "Le preguntamos a un *adulto*.", "Y miramos *internet*, siempre con un adulto."]},
 {"t": "mazo", "titulo": "LAS PREGUNTAS DE SOFI", "items": [{"frente": "¿Dónde vive?", "dorso": "EN LA SELVA", "emoji": "🌳"}, {"frente": "¿Cómo es?", "dorso": "TIENE MANCHAS", "emoji": "🐆"}, {"frente": "¿Qué come?", "dorso": "OTROS ANIMALES", "emoji": "🍖"}],
  "voz": ["¿Dónde vive? En la *selva*.", "¿Cómo es? Tiene *manchas*.", "¿Qué come? *Otros animales*."]},
 {"t": "errores", "items": [{"mal": "Copiar el libro entero", "bien": "Anotar datos cortos"}],
  "voz": ["Cuidado con este error.", "No copiamos todo: anotamos *datos cortos*."]},
 {"t": "consejo", "titulo": "SOLO DATOS REALES", "texto": "Nada inventado", "emoji": "✅",
  "voz": ["Truco: en la ficha van solo datos *reales*."]},
 {"t": "resumen", "items": [["BUSCAR", "libros, láminas, adultos"], ["PREGUNTAR", "¿dónde vive? ¿qué come?"], ["ANOTAR", "datos cortos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Buscamos* en libros, láminas y con adultos.", "Nos hacemos *preguntas*.", "*Anotamos* datos cortos.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué va arriba en la ficha?", "segundos": 8, "respuesta": "¡El título!", "emoji": "📝", "titulo": "ESCRIBIR", "sub": "la ficha",
  "voz": ["Desafío: ¿qué va arriba en la ficha?", "¡El *título*!", "Hoy: *escribir la ficha*."]},
 {"t": "matriz", "titulo": "LA FICHA DEL YAGUARETÉ", "celdas": [{"cab": "¿QUÉ ES?", "txt": "Es un animal grande."}, {"cab": "¿DÓNDE VIVE?", "txt": "Vive en la selva."}, {"cab": "¿CÓMO ES?", "txt": "Tiene manchas."}, {"cab": "¿QUÉ COME?", "txt": "Come otros animales."}],
  "voz": ["Esta es la ficha de Sofi.", "Es un animal grande.", "Vive en la selva.", "Tiene manchas.", "Come otros animales."]},
 {"t": "completa", "antes": "Vive en la", "despues": ".", "opciones": ["SELVA", "LUNA"], "correcta": 0,
  "voz": ["Completá el dato: vive en la…", "¿Selva o luna?", "¡*Selva*! Es un dato real."]},
 {"t": "unir", "titulo": "DEL DATO A LA ORACIÓN", "pares": [["SELVA", "Vive en la selva."], ["MANCHAS", "Tiene manchas."], ["GRANDE", "Es un animal grande."]], "mezclar": True,
  "voz": ["Cada dato se vuelve una oración.", "Selva: vive en la selva.", "Manchas: tiene manchas.", "Grande: es un animal grande."]},
 {"t": "consejo", "titulo": "UN DATO, UN RENGLÓN", "texto": "Con mayúscula y punto", "emoji": "✏️",
  "voz": ["Truco: un dato por renglón, con *mayúscula* y *punto*."]},
 {"t": "resumen", "items": [["TÍTULO", "arriba"], ["DIBUJO", "cómo es"], ["DATOS", "uno por renglón"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *título* va arriba.", "El *dibujo* muestra cómo es.", "Los *datos* van uno por renglón.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Sofi va a leer su ficha al grado!", "bajada": "Pero antes la revisa", "emoji": "🎤", "titulo": "REVISAR", "sub": "y compartir",
  "voz": ["¡Último momento: Sofi va a leer su ficha!", "Pero antes la *revisa*.", "Hoy: *revisar y compartir la ficha*."]},
 {"t": "escape", "titulo": "LA PUERTA DEL AULA", "candados": [{"p": "¿Tiene título?", "r": "SÍ ✅"}, {"p": "¿Cada oración tiene punto?", "r": "SÍ ✅"}, {"p": "¿Los datos son reales?", "r": "SÍ ✅"}],
  "voz": ["¡Para salir a compartir, abrimos los candados!", "¿Tiene título? ¡Sí!", "¿Cada oración tiene punto? ¡Sí!", "¿Los datos son reales? ¡Sí!", "¡Lista para compartir!"]},
 {"t": "personaje", "personaje": SOFI, "lineas": [{"txt": "¡Hola! Mi ficha es del yaguareté.", "animo": "feliz"}, {"txt": "Vive en la selva y tiene manchas.", "animo": "ojo"}, {"txt": "¡Gracias por escuchar!", "animo": "feliz"}],
  "voz": ["¡Hola! Mi ficha es del yaguareté.", "Vive en la selva y tiene manchas.", "¡Gracias por escuchar!"]},
 {"t": "errores", "items": [{"mal": "Leer muy rápido", "bien": "Leer despacio y en voz alta"}],
  "voz": ["Cuidado con este error.", "No leemos rápido: leemos *despacio* y en voz alta."]},
 {"t": "consejo", "titulo": "MOSTRÁ EL DIBUJO", "texto": "Así todos ven de qué hablás", "emoji": "🖼️",
  "voz": ["Truco: mostrá el *dibujo* mientras leés."]},
 {"t": "resumen", "items": [["REVISAR", "título, mayúscula, punto"], ["CORREGIR", "arreglar errores"], ["COMPARTIR", "en voz alta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Revisamos* título, mayúsculas y puntos.", "*Corregimos* los errores.", "*Compartimos* en voz alta.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m8-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 8 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
