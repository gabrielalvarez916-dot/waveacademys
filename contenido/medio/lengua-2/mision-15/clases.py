# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 15 · Ortografía: GUE, GUI, QUE y QUI: las 4 clases animadas.
Vía fonológica: la VOZ dice sonidos (que, qui, gue, gui, güe) y «la letra escondida que no suena», «los dos puntitos»; nunca nombres de letras.
Metáfora: Sofi, detective de palabras. Genera tools/medio/clase/lecciones/medio-leng2-m15-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'ac7db775-71fd-4384-8569-12b1e449df60', 2: '1f5f5372-784e-4d55-88a9-0d91636f4650', 3: '2551f6eb-2fa7-40f7-9319-de70aac18aad', 4: 'abd8b08c-0d9c-4966-ac7a-c14a61051565'}
TIT = {1: 'Palabras con QUE y QUI', 2: 'Palabras con GUE y GUI', 3: 'Palabras con GÜE y GÜI', 4: 'Dictado con las cuatro reglas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "🕵️‍♀️"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🧀", "lineas": ["La detective mira la palabra QUESO.", "¡Hay una letra escondida!", "Se ve, pero no suena."], "titulo": "QUE", "sub": "y QUI",
  "voz": ["La detective mira la palabra *queso*.", "¡Hay una *letra escondida*!", "Se ve, pero *no suena*.", "Hoy: *que y qui*."]},
 {"t": "silabas", "palabra": "QUESO", "silabas": ["QUE", "SO"], "tonica": 0, "tipo": "grave",
  "voz": ["Escuchá: que… so.", "En *que* hay tres letras, pero suenan dos.", "¡La del medio está escondida!"]},
 {"t": "memoria", "titulo": "CON QUE Y QUI", "items": ["QUESO", "QUINCE", "PAQUETE", "MOSQUITO"], "falta": 2,
  "voz": ["Mirá estas palabras con que y qui.", "Se tapan… ¡y una desapareció!", "¡Faltaba *paquete*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál está bien escrita?", "opciones": ["QUESO", "QESO"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuál está bien?", "Buscá la letra escondida.", "¡*Queso*, con su letra escondida!"]},
 {"t": "consejo", "titulo": "LA ESCONDIDA", "texto": "QUE y QUI siempre llevan U", "emoji": "🔎",
  "voz": ["Truco: *que* y *qui* siempre llevan la letra escondida."]},
 {"t": "resumen", "items": [["QUE · QUI", "con letra escondida"], ["EJEMPLOS", "QUESO, QUINCE"], ["OJO", "nunca QE ni QI"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Que* y *qui* llevan una letra que no suena.", "Como en *queso* y *quince*.", "¡Nunca se olvida!", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "CASO NUEVO", "titular": "¡Otra letra escondida!", "bajada": "Ahora en GUITARRA", "emoji": "🎸", "titulo": "GUE", "sub": "y GUI",
  "voz": ["¡Caso nuevo: otra letra escondida!", "Ahora en *guitarra*.", "Hoy: *gue y gui*."]},
 {"t": "pistas", "problema": "¿Qué palabra es?", "pistas": ["Es un instrumento", "Tiene cuerdas", "Empieza con GUI"], "respuesta": "GUITARRA 🎸",
  "voz": ["Adivinanza: ¿qué palabra es?", "Pista uno: es un instrumento.", "Pista dos: tiene cuerdas.", "Pista tres: empieza con *gui*.", "¡La *guitarra*!"]},
 {"t": "vof", "afirmacion": "En GUISO, la letra del medio suena", "emoji": "🍲", "verdadero": False, "explicacion": "Está escondida: no suena",
  "voz": ["¿Verdadero o falso? En guiso, la letra del medio suena.", "Escuchá: gui… so.", "¡*Falso*! Está escondida."]},
 {"t": "clasificar", "cajas": [{"cab": "GA · GO · GU", "emoji": "🐱"}, {"cab": "GUE · GUI", "emoji": "🎸"}], "fichas": [{"txt": "GATO", "caja": 0}, {"txt": "GUSANO", "caja": 0}, {"txt": "GUISO", "caja": 1}, {"txt": "JUGUETE", "caja": 1}],
  "voz": ["Separamos las palabras.", "Gato y gusano: sin letra escondida.", "Guiso y juguete: ¡con letra escondida!"]},
 {"t": "consejo", "titulo": "CON GUE Y GUI", "texto": "Llevan una U que no suena", "emoji": "🤫",
  "voz": ["Truco: *gue* y *gui* también llevan la letra escondida."]},
 {"t": "resumen", "items": [["GA · GO · GU", "sin escondida"], ["GUE · GUI", "con escondida"], ["EJEMPLOS", "GUITARRA, JUGUETE"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Ga*, *go*, *gu*: sin letra escondida.", "*Gue* y *gui*: con letra escondida.", "Como en *guitarra* y *juguete*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Decí despacio: PINGÜINO", "segundos": 8, "respuesta": "pin · güi · no: ¡se escucha!", "emoji": "🐧", "titulo": "GÜE", "sub": "y GÜI",
  "voz": ["Desafío: decí despacio *pingüino*.", "Pin… güi… no. ¡Ahora la letra *sí se escucha*!", "Hoy: *güe y güi*."]},
 {"t": "comparar", "a": {"cab": "GUISO", "texto": "no suena", "emoji": "🍲"}, "b": {"cab": "PINGÜINO", "texto": "sí suena: Ü", "emoji": "🐧"}, "signo": "≠", "def": {"cab": "LOS DOS PUNTITOS", "texto": "avisan: ¡esta suena!"},
  "voz": ["En *guiso*, la letra del medio no suena.", "En *pingüino*, ¡sí suena!", "Por eso lleva *dos puntitos* arriba.", "Los puntitos avisan: ¡esta suena!"]},
 {"t": "mazo", "titulo": "CON PUNTITOS", "items": [{"frente": "🐧", "dorso": "PINGÜINO", "emoji": "🐧"}, {"frente": "🦩", "dorso": "CIGÜEÑA", "emoji": "🦩"}, {"frente": "💧", "dorso": "AGÜITA", "emoji": "💧"}],
  "voz": ["*Pingüino*: con dos puntitos.", "*Cigüeña*: con dos puntitos.", "*Agüita*: ¡también!"]},
 {"t": "pregunta", "pregunta": "¿Cuál lleva los dos puntitos?", "opciones": ["CIGÜEÑA", "GUISO"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuál lleva los dos puntitos?", "Decilas en voz alta.", "¡*Cigüeña*! Ahí suena."]},
 {"t": "consejo", "titulo": "¿SUENA?", "texto": "Si suena, lleva los dos puntitos", "emoji": "👂",
  "voz": ["Truco: si la escuchás, lleva los *dos puntitos*."]},
 {"t": "resumen", "items": [["GUE · GUI", "no suena"], ["GÜE · GÜI", "sí suena"], ["DIÉRESIS", "los dos puntitos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En *gue* y *gui*, no suena.", "En *güe* y *güi*, ¡sí suena!", "Los dos puntitos se llaman *diéresis*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Me dictás palabras difíciles? 📝"}, {"yo": True, "txt": "¡Sí! Con las cuatro reglas"}], "titulo": "DICTADO", "sub": "las cuatro reglas",
  "voz": ["Tomi le pide: ¿me dictás palabras difíciles?", "Sofi responde: ¡sí, con las cuatro reglas!", "Hoy: *dictado*."]},
 {"t": "pizarra", "titulo": "LAS CUATRO REGLAS", "lineas": [{"txt": "QUE · QUI → QUESO", "color": "sol"}, {"txt": "GUE · GUI → GUISO", "color": "coral"}, {"txt": "GÜE · GÜI → PINGÜINO", "color": "verde", "marca": "circulo"}, {"txt": "GA · GO · GU → GATO", "color": "azul"}],
  "voz": ["*Que*, *qui*: con letra escondida, como *queso*.", "*Gue*, *gui*: con letra escondida, como *guiso*.", "*Güe*, *güi*: con dos puntitos, como *pingüino*.", "*Ga*, *go*, *gu*: sin nada extra, como *gato*."]},
 {"t": "tipeo", "titulo": "DICTADO", "items": [{"p": "El ave del hielo", "r": "PINGÜINO"}, {"p": "Instrumento con cuerdas", "r": "GUITARRA"}, {"p": "Insecto que pica", "r": "MOSQUITO"}],
  "voz": ["Primera palabra: *pingüino*.", "Segunda palabra: *guitarra*.", "Tercera palabra: *mosquito*."]},
 {"t": "errores", "items": [{"mal": "MAQINA", "bien": "MÁQUINA"}, {"mal": "PINGUINO", "bien": "PINGÜINO"}],
  "voz": ["Cuidado con estos errores.", "Máquina lleva la letra *escondida*.", "Pingüino lleva los *dos puntitos*."]},
 {"t": "consejo", "titulo": "REVISÁ AL FINAL", "texto": "Buscá cada QU, GU y GÜ", "emoji": "🔍",
  "voz": ["Truco: al final, *revisá* cada palabra difícil."]},
 {"t": "resumen", "items": [["QUE · QUI", "con U"], ["GUE · GUI", "con U muda"], ["GÜE · GÜI", "con Ü"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Que* y *qui*: con letra escondida.", "*Gue* y *gui*: con letra escondida.", "*Güe* y *güi*: con dos puntitos.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m15-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 15 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
