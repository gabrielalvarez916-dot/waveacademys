# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 15 · Una fábula para leer («El león y el ratón», Esopo, dominio público): las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Genera tools/medio/clase/lecciones/medio-leng1-m15-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'f0c1525f-d053-4a44-af17-4be43a0934c6', 2: 'a15b4922-df5c-4a4e-9f72-b2357fb74b94', 3: '78a5824d-73e1-4c68-8006-03900aa0573a', 4: 'ef072f6f-7d09-4bf8-8743-a1e423f9f912'}
TIT = {1: 'Escuchar la fábula', 2: 'Quiénes son los animales de la fábula', 3: 'Qué enseña la fábula', 4: 'Contar la fábula con mis palabras'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LEON = {"nombre": "León", "emoji": "🦁"}

N1 = [
 {"t": "historieta", "titulo": "EL LEÓN Y EL RATÓN", "vinetas": [{"emojis": ["🦁", "💤"], "txt": "Un león dormía"}, {"emojis": ["🐭", "😳"], "txt": "Un ratón lo despertó"}, {"emojis": ["🦁", "🕸️"], "txt": "El león cayó en una red"}, {"emojis": ["🐭", "✂️"], "txt": "¡El ratón mordió la red!"}],
  "voz": ["Un león dormía. Un ratón lo despertó.", "El león lo dejó ir.", "Un día, el león cayó en una red.", "¡El ratón lo salvó! Hoy: *una fábula*."]},
 {"t": "definicion", "palabra": "Fábula", "texto": "Cuento corto con animales que enseña algo", "emoji": "📖",
  "voz": ["Esta historia es una *fábula*: tiene animales y enseña algo.", "La contó *Esopo*, hace muchísimo."]},
 {"t": "escala", "titulo": "¿QUIÉN ES MÁS GRANDE?", "items": [{"txt": "RATÓN", "emoji": "🐭", "valor": 1}, {"txt": "LEÓN", "emoji": "🦁", "valor": 10}],
  "voz": ["El ratón es *chiquito*.", "¡El león es *enorme*!"]},
 {"t": "pregunta", "pregunta": "¿Quién mordió la red?", "opciones": ["EL RATÓN", "EL LEÓN"], "correcta": 0,
  "voz": ["Ahora vos: ¿quién mordió la red?", "Acordate de la fábula.", "¡El *ratón*!"]},
 {"t": "consejo", "titulo": "ESCUCHÁ", "texto": "Mirá lo que hace cada animal", "emoji": "👂",
  "voz": ["Truco: prestá atención a lo que *hace* cada animal."]},
 {"t": "resumen", "items": [["FÁBULA", "cuento con animales"], ["PRINCIPIO", "el ratón despierta al león"], ["FINAL", "el ratón lo salva"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *fábula* es un cuento con animales.", "Al *principio*, el ratón despierta al león.", "Al *final*, el ratón lo salva.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Quién es más fuerte: el león o el ratón?", "segundos": 8, "respuesta": "¡El león!", "emoji": "💪", "titulo": "LOS ANIMALES", "sub": "de la fábula",
  "voz": ["Desafío: ¿quién es más fuerte?", "¡El *león*!", "Hoy: *los animales de la fábula*."]},
 {"t": "versus", "titulo": "¿CÓMO SON?", "a": {"txt": "LEÓN", "emoji": "🦁", "datos": ["grande", "fuerte"]}, "b": {"txt": "RATÓN", "emoji": "🐭", "datos": ["chiquito", "valiente"]}, "gana": "empate", "veredicto": "¡Los dos se ayudaron!",
  "voz": ["Comparamos a los dos animales.", "El león es *grande* y *fuerte*.", "El ratón es *chiquito* y *valiente*.", "¡Al final, los dos se ayudaron!"]},
 {"t": "personaje", "personaje": LEON, "lineas": [{"txt": "¡Grrr! Yo soy el rey de la selva.", "animo": "feliz"}, {"txt": "¡Caí en una red y no podía salir!", "animo": "triste"}, {"txt": "¡Gracias, ratoncito!", "animo": "sorpresa"}],
  "voz": ["¡Grrr! Yo soy el rey de la selva.", "¡Caí en una red y no podía salir!", "¡Gracias, ratoncito!"]},
 {"t": "consejo", "titulo": "POR LO QUE HACEN", "texto": "Lo que hace cada animal muestra cómo es", "emoji": "🔎",
  "voz": ["Truco: lo que *hace* cada animal muestra cómo es."]},
 {"t": "errores", "items": [{"mal": "Chiquito no puede ayudar", "bien": "Todos podemos ayudar"}],
  "voz": ["Cuidado con este error.", "Ser chiquito *no* quiere decir que no podés ayudar."]},
 {"t": "resumen", "items": [["LEÓN", "grande y fuerte"], ["RATÓN", "chiquito y valiente"], ["LOS DOS", "se ayudaron"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *león* es grande y fuerte.", "El *ratón* es chiquito y valiente.", "*Los dos* se ayudaron.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "FÁBULAS", "titular": "¡Un ratón salvó al rey de la selva!", "bajada": "¿Qué nos enseña?", "emoji": "🐭", "titulo": "LA ENSEÑANZA", "sub": "de la fábula",
  "voz": ["¡Noticia: un ratón salvó al rey de la selva!", "¿Qué nos *enseña*?", "Hoy: *qué enseña la fábula*."]},
 {"t": "definicion", "palabra": "Moraleja", "texto": "Todos podemos ayudar, aunque seamos chiquitos", "emoji": "💡",
  "voz": ["Lo que enseña la fábula se llama *moraleja*.", "Todos podemos ayudar, aunque seamos *chiquitos*."]},
 {"t": "dilema", "situacion": "Tomi ve que a un compañero se le cayeron los lápices", "emoji": "✏️", "a": {"txt": "Lo ayuda a juntarlos", "consecuencia": "¡Como el ratón! Su amigo se pone contento", "emoji": "🤝"}, "b": {"txt": "Sigue de largo", "consecuencia": "Su amigo queda solo juntando todo", "emoji": "🚶"},
  "voz": ["A un compañero de Tomi se le cayeron los lápices.", "Si lo *ayuda*, ¡como el ratón! Su amigo, contento.", "Si sigue de largo, su amigo queda solo."]},
 {"t": "vof", "afirmacion": "La moraleja es: el león dormía", "emoji": "🦁", "verdadero": False, "explicacion": "Eso cuenta lo que pasó",
  "voz": ["¿Verdadero o falso? La moraleja es: el león dormía.", "Pensá: ¿eso enseña algo?", "¡*Falso*! Eso cuenta lo que pasó."]},
 {"t": "consejo", "titulo": "PREGUNTÁ", "texto": "¿Qué aprendí? Esa es la moraleja", "emoji": "❓",
  "voz": ["Truco: preguntá *¿qué aprendí?* Esa es la moraleja."]},
 {"t": "resumen", "items": [["MORALEJA", "lo que enseña"], ["ESTA FÁBULA", "todos podemos ayudar"], ["EN LA ESCUELA", "también ayudamos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *moraleja* es lo que enseña.", "Esta fábula: *todos podemos ayudar*.", "En la escuela, ¡también *ayudamos*!", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¡Contame la fábula del león! 🦁"}, {"yo": True, "txt": "¡Te la cuento con mis palabras!"}], "titulo": "CONTAR", "sub": "con mis palabras",
  "voz": ["Tomi le pide a Sofi: ¡contame la fábula!", "Sofi responde: ¡te la cuento con mis palabras!", "Hoy: *contar la fábula*."]},
 {"t": "bloques", "titulo": "LAS TRES PARTES", "items": [{"cab": "PRINCIPIO", "txt": "El ratón despierta al león"}, {"cab": "PROBLEMA", "txt": "El león cae en una red"}, {"cab": "FINAL", "txt": "El ratón lo salva"}],
  "voz": ["Para contar, pensamos en tres partes.", "*Principio*: el ratón despierta al león.", "*Problema*: el león cae en una red.", "*Final*: el ratón lo salva."]},
 {"t": "prediccion", "pregunta": "¿Qué palabra usamos para empezar a contar?", "a": {"txt": "PRIMERO", "emoji": "1️⃣"}, "b": {"txt": "AL FINAL", "emoji": "🏁"}, "correcta": "a", "resultado": "PRIMERO, DESPUÉS y AL FINAL",
  "voz": ["¿Qué palabra usamos para empezar?", "Pensá…", "¡*Primero*! Después viene *después* y *al final*."]},
 {"t": "pregunta", "pregunta": "¿Qué pasa en el problema?", "opciones": ["EL LEÓN CAE EN UNA RED", "EL RATÓN COME QUESO"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué pasa en el problema?", "Acordate de la red.", "¡El león cae en una *red*!"]},
 {"t": "consejo", "titulo": "EN ORDEN", "texto": "No te saltees el problema", "emoji": "🧭",
  "voz": ["Truco: contá *en orden* y no te saltees el problema."]},
 {"t": "resumen", "items": [["PRINCIPIO", "lo primero"], ["PROBLEMA", "la red"], ["FINAL", "el ratón lo salva"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *principio*: lo primero que pasa.", "El *problema*: la red.", "El *final*: el ratón lo salva.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m15-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 15 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
