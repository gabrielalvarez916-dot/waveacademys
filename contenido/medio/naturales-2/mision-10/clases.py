# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 10 · Museo de ciencias: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (arma el museo del grado).
Genera tools/medio/clase/lecciones/medio-nat2-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '2cdf29c4-e6ab-4886-b7d7-e926bd6112fc', 2: '494d576e-e8a7-4247-b937-8b2e4095adef', 3: '8da11841-4b38-40b3-a50e-c5bc423635b6', 4: '8ebef30b-de45-4ef6-a530-a1cf157fd1bb'}
TIT = {1: 'Elijo un tema para mostrar', 2: 'Armo mi puesto del museo', 3: 'Explico con dibujos y datos', 4: 'Visitamos el museo'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🏛️", "lineas": ["El grado arma un museo.", "Cada uno muestra un tema.", "¿Cuál elige Tomi?"], "titulo": "MUSEO", "sub": "de ciencias",
  "voz": ["El grado arma un *museo*.", "Cada uno muestra un *tema*.", "¿Cuál elegirá Tomi?", "Hoy: *elijo un tema*."]},
 {"t": "memoria", "titulo": "TEMAS DEL AÑO", "items": ["CRECEMOS", "LAS CRÍAS", "EL AGUA", "LOS IMANES"], "falta": 3,
  "voz": ["Mirá los temas que aprendimos.", "Se tapan… ¡y uno desapareció!", "¡Faltaban *los imanes*!"]},
 {"t": "quiz4", "pregunta": "¿Qué tema elige Tomi?", "opciones": ["LOS IMANES", "LOS PLANETAS", "LOS AUTOS", "LA MÚSICA"], "correcta": 0,
  "voz": ["¿Qué tema elige Tomi?", "Le encantan los clips que saltan.", "¡*Los imanes*!"]},
 {"t": "pregunta", "pregunta": "¿Para qué sirve un museo?", "opciones": ["PARA APRENDER", "PARA DORMIR"], "correcta": 0,
  "voz": ["Ahora vos: ¿para qué sirve un museo?", "Pensá en lo que se muestra.", "¡Para *aprender*!"]},
 {"t": "consejo", "titulo": "ELEGÍ CON GANAS", "texto": "El tema que más te guste", "emoji": "💡",
  "voz": ["Truco: elegí el tema que más te *guste*."]},
 {"t": "resumen", "items": [["MUSEO", "mostrar y aprender"], ["TEMAS", "los del año"], ["ELEGIR", "el que más te gusta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *museo* es para mostrar y aprender.", "Los *temas* son los del año.", "*Elegimos* el que más nos gusta.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué necesita un buen puesto del museo?", "segundos": 8, "respuesta": "¡Título, dibujo y algo para probar!", "emoji": "🖼️", "titulo": "ARMO", "sub": "mi puesto",
  "voz": ["Desafío: ¿qué necesita un buen puesto?", "¡Título, dibujo y algo para *probar*!", "Hoy: *armo mi puesto*."]},
 {"t": "partes", "emoji": "🖼️", "titulo": "EL PUESTO DE TOMI", "partes": [{"txt": "TÍTULO", "x": 0, "y": -0.8}, {"txt": "DIBUJO", "x": -0.7, "y": 0}, {"txt": "OBJETOS", "x": 0.7, "y": 0}, {"txt": "PARA PROBAR", "x": 0, "y": 0.8}],
  "voz": ["Este es el puesto de Tomi.", "Arriba, el *título*.", "Un *dibujo* del imán.", "Los *objetos*: clips y clavos.", "Y algo *para probar*."]},
 {"t": "unir", "titulo": "¿PARA QUÉ SIRVE?", "pares": [["TÍTULO", "dice el tema"], ["DIBUJO", "muestra"], ["OBJETOS", "se tocan"]], "mezclar": True,
  "voz": ["Unimos cada parte con lo que hace.", "El *título* dice el tema.", "El *dibujo* muestra.", "Los *objetos* se tocan."]},
 {"t": "pregunta", "pregunta": "¿Cómo tiene que ser la letra del cartel?", "opciones": ["GRANDE Y CLARA", "CHIQUITA"], "correcta": 0,
  "voz": ["Ahora vos: ¿cómo es la letra del cartel?", "Pensá en leer de lejos.", "¡*Grande* y clara!"]},
 {"t": "consejo", "titulo": "POCAS PALABRAS", "texto": "Se leen mejor", "emoji": "✏️",
  "voz": ["Truco: en el cartel, *pocas* palabras."]},
 {"t": "resumen", "items": [["TÍTULO", "arriba y grande"], ["DIBUJO", "muestra el tema"], ["PARA PROBAR", "algo para tocar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *título* va arriba y grande.", "El *dibujo* muestra el tema.", "Y algo *para probar*.", CIERRE]},
]
N3 = [
 {"t": "dialogo", "personas": [{"nombre": "TOMI", "emoji": "🧑‍🔬"}, {"nombre": "VISITANTE", "emoji": "👦"}], "lineas": [{"quien": 0, "txt": "¡Hola! Bienvenido a mi puesto."}, {"quien": 1, "txt": "¿De qué se trata?"}, {"quien": 0, "txt": "Mirá: el imán atrae clips."}],
  "voz": ["¡Hola! Bienvenido a mi puesto.", "¿De qué se trata?", "Mirá: el imán atrae *clips*."]},
 {"t": "comparar", "a": {"cab": "SIN DIBUJO", "texto": "CUESTA ENTENDER", "emoji": "😕"}, "b": {"cab": "CON DIBUJO", "texto": "¡SE ENTIENDE!", "emoji": "😃"}, "signo": "→",
  "voz": ["Comparamos dos formas de explicar.", "*Sin dibujo*: cuesta entender.", "*Con dibujo*: ¡se entiende mejor!"]},
 {"t": "prediccion", "pregunta": "¿Qué hacemos primero al explicar?", "a": {"txt": "SALUDO", "emoji": "👋"}, "b": {"txt": "ME VOY", "emoji": "🚶"}, "correcta": "a", "resultado": "Saludo, señalo el dibujo y digo un dato",
  "voz": ["¿Qué hacemos *primero* al explicar?", "Pensá…", "¡*Saludo*! Después, el dibujo y un dato."]},
 {"t": "pregunta", "pregunta": "¿Cómo hablo para explicar?", "opciones": ["DESPACIO Y FUERTE", "RAPIDÍSIMO"], "correcta": 0,
  "voz": ["Ahora vos: ¿cómo hablo para explicar?", "Pensá en el que escucha.", "¡*Despacio* y fuerte!"]},
 {"t": "consejo", "titulo": "ENSAYÁ", "texto": "Practicá en casa antes del museo", "emoji": "🎤",
  "voz": ["Truco: *ensayá* en casa antes del museo."]},
 {"t": "resumen", "items": [["SALUDO", "bienvenida"], ["DIBUJO", "lo señalo"], ["DATO", "algo verdadero"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero, *saludo*.", "Después, señalo el *dibujo*.", "Y digo un *dato* verdadero.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Seño Ana", "emoji": "👩‍🏫"}, "mensajes": [{"yo": False, "txt": "¡Hoy abrimos el museo! 🏛️"}, {"yo": True, "txt": "¡Voy a visitar todos los puestos!"}], "titulo": "VISITAMOS", "sub": "el museo",
  "voz": ["La seño escribe: ¡hoy abrimos el museo!", "Tomi responde: ¡voy a *visitar* todo!", "Hoy: *visitamos el museo*."]},
 {"t": "escape", "titulo": "LA PUERTA DEL MUSEO", "candados": [{"p": "¿Cómo hablamos en el museo?", "r": "BAJITO"}, {"p": "¿Qué hacemos antes de tocar?", "r": "PREGUNTAR"}],
  "voz": ["¡Para entrar al museo, abrimos los candados!", "En el museo hablamos *bajito*.", "Antes de tocar, *preguntamos*.", "¡Entramos!"]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Gritón", "emoji": "👹"}, "preguntas": [{"p": "¿Esperamos el turno para hablar?", "r": "SÍ"}, {"p": "¿Qué decimos al irnos?", "r": "¡QUÉ BUEN PUESTO!"}],
  "voz": ["¡Apareció el *Monstruo Gritón*!", "No sabe visitar un museo.", "¿Esperamos el turno? ¡*Sí*!", "Al irnos: ¡qué buen puesto! ¡Ganamos!"]},
 {"t": "pregunta", "pregunta": "¿Qué hace un buen visitante?", "opciones": ["ESCUCHA Y PREGUNTA", "GRITA Y CORRE"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué hace un buen visitante?", "Pensá en el museo.", "¡*Escucha* y pregunta!"]},
 {"t": "consejo", "titulo": "FELICITÁ", "texto": "Decí algo lindo de cada puesto", "emoji": "👏",
  "voz": ["Truco: *felicitá* a tus compañeros."]},
 {"t": "resumen", "items": [["MIRO", "con cuidado"], ["PREGUNTO", "para aprender"], ["FELICITO", "al irme"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Miro* con cuidado.", "*Pregunto* para aprender.", "*Felicito* al irme. ¡Fuiste un gran científico!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m10-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 10 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
