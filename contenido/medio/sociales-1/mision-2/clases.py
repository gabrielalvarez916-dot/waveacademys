# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 2 · Mi escuela es una institución: las 4 clases animadas.
Metáfora: un día en la escuela. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 2
TIT = {1: 'Para qué sirve una escuela', 2: 'Los trabajos que hay en la escuela', 3: 'Normas que nos cuidan en el aula', 4: 'Los espacios de la escuela y para qué sirven'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Para qué vamos a la escuela?"}, {"yo": True, "txt": "¡PARA APRENDER Y JUGAR!"}, {"yo": False, "txt": "¡Y para ver amigos!"}], "titulo": "MI ESCUELA", "sub": "es una institución",
  "voz": ["Tomi le escribe a Sofi.", "¿Para qué vamos a la escuela?", "Para *aprender* y jugar.", "Hoy: *para qué sirve la escuela*."]},
 {"t": "causas", "causa": {"txt": "LA ESCUELA SIRVE PARA", "emoji": "🏫"}, "items": ["APRENDER", "JUGAR", "HACER AMIGOS"],
  "voz": ["¿Para qué sirve la *escuela*?", "Para *aprender* a leer y contar.", "Para *jugar* en el recreo.", "Y para hacer *amigos*."]},
 {"t": "zoom", "niveles": [{"emoji": "🏘️", "txt": "EL BARRIO"}, {"emoji": "🏫", "txt": "LA ESCUELA"}, {"emoji": "🧑‍🏫", "txt": "MI AULA"}],
  "voz": ["Miramos el *barrio*.", "Ahí está la *escuela*.", "¡Y adentro, *mi aula*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál también es una institución?", "opciones": ["UNA PELOTA", "EL HOSPITAL", "UN ÁRBOL"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en lugares que ayudan.", "¿Cuál es una institución?", "¡El *hospital*! Cuida la salud de todos."]},
 {"t": "consejo", "titulo": "ES DE TODOS", "texto": "Todos los chicos pueden ir a la escuela", "emoji": "🎒",
  "voz": ["Recordá: la escuela es para *todos* los chicos."]},
 {"t": "resumen", "items": [["INSTITUCIÓN", "tarea para todos"], ["APRENDER", "leer, escribir, contar"], ["COMPARTIR", "jugar y hacer amigos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La escuela es una *institución*.", "Sirve para *aprender*.", "Y para *compartir* con amigos.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🏫", "lineas": ["Sofi llega temprano a la escuela.", "El portero abre la puerta.", "¡Y la cocinera ya prepara el almuerzo!"], "titulo": "LOS TRABAJOS", "sub": "de la escuela",
  "voz": ["Sofi llega *temprano* a la escuela.", "El portero abre la puerta.", "¡La cocinera ya prepara el almuerzo!", "Hoy: *los trabajos de la escuela*."]},
 {"t": "bloques", "titulo": "QUIÉN HACE QUÉ", "items": [{"cab": "🧑‍🏫 MAESTRA", "txt": "ENSEÑA"}, {"cab": "👩‍💼 DIRECTORA", "txt": "ORGANIZA"}, {"cab": "🧹 PORTERO", "txt": "LIMPIA Y CUIDA"}, {"cab": "👩‍🍳 COCINERA", "txt": "COCINA"}],
  "voz": ["En la escuela trabajan muchas personas.", "La maestra *enseña*.", "La directora *organiza*.", "El portero *limpia* y cuida.", "La cocinera *cocina*."]},
 {"t": "antesdespues", "antes": {"cab": "SIN EL PORTERO", "emoji": "🗑️", "texto": "Todo sucio"}, "despues": {"cab": "CON EL PORTERO", "emoji": "✨", "texto": "¡Todo limpio!"},
  "voz": ["Sin el portero, la escuela estaría *sucia*.", "Gracias a su trabajo, está *limpia*."]},
 {"t": "pregunta", "pregunta": "¿Quién enseña a leer?", "opciones": ["COCINERA", "MAESTRA", "PORTERO"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el aula.", "¿Quién enseña a leer?", "¡La *maestra*!"]},
 {"t": "consejo", "titulo": "SALUDÁ A TODOS", "texto": "Todos los trabajos son importantes", "emoji": "👋",
  "voz": ["Recordá: *todos* los trabajos son importantes."]},
 {"t": "resumen", "items": [["MAESTRA", "enseña"], ["PORTERO", "limpia y cuida"], ["TODOS", "son importantes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La maestra *enseña*.", "El portero *limpia* y cuida.", "*Todos* los trabajos importan.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué hacés para hablar en clase?", "segundos": 6, "respuesta": "¡LEVANTO LA MANO!", "emoji": "✋", "titulo": "LAS NORMAS", "sub": "que nos cuidan",
  "voz": ["Desafío: ¿qué hacés para hablar en clase?", "¡*Levanto la mano*!", "Hoy: *normas que nos cuidan*."]},
 {"t": "corrige", "titulo": "ASÍ NO, ASÍ SÍ", "cambios": [{"antes": "GRITO PARA HABLAR", "despues": "LEVANTO LA MANO", "motivo": "así me escuchan"}, {"antes": "CORRO EN EL AULA", "despues": "CAMINO DESPACIO", "motivo": "para no golpearnos"}],
  "voz": ["Arreglamos lo que está mal.", "En vez de gritar, *levanto la mano*.", "En vez de correr, *camino despacio*."]},
 {"t": "causas", "causa": {"txt": "SIN NORMAS", "emoji": "😵"}, "items": ["TODOS GRITAN", "NADIE ESCUCHA", "SE ROMPEN COSAS"],
  "voz": ["¿Qué pasa *sin normas*?", "Todos *gritan*.", "*Nadie* escucha.", "Y se *rompen* cosas."]},
 {"t": "pregunta", "pregunta": "¿Cuál es una norma del aula?", "opciones": ["GRITAR", "ESPERAR MI TURNO", "TIRAR PAPELES"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en tu aula.", "¿Cuál es una norma?", "¡*Esperar mi turno*!"]},
 {"t": "consejo", "titulo": "ENTRE TODOS", "texto": "Las normas se arman entre todos", "emoji": "🤝",
  "voz": ["Truco: las normas se pueden armar *entre todos*."]},
 {"t": "resumen", "items": [["NORMA", "regla que nos cuida"], ["AULA", "levantar la mano"], ["PARA QUÉ", "estar bien todos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *norma* es una regla que cuida.", "En el aula *levantamos la mano*.", "Así estamos *bien todos*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡RECORREMOS LA ESCUELA!", "bajada": "Cada lugar tiene su uso", "emoji": "🗺️", "titulo": "LOS ESPACIOS", "sub": "de la escuela",
  "voz": ["¡Último momento! Vamos a *recorrer* la escuela.", "Cada lugar tiene su uso.", "Hoy: *los espacios de la escuela*."]},
 {"t": "partes", "emoji": "🏫", "titulo": "MI ESCUELA", "partes": [{"txt": "AULA", "x": -0.6, "y": -0.4}, {"txt": "PATIO", "x": 0.5, "y": 0.6}, {"txt": "BIBLIOTECA", "x": 0.6, "y": -0.4}, {"txt": "COMEDOR", "x": -0.5, "y": 0.6}],
  "voz": ["Miramos la *escuela* por dentro.", "Acá está el *aula*.", "Allá, el *patio*.", "Acá, la *biblioteca*.", "Y allá, el *comedor*."]},
 {"t": "matriz", "titulo": "¿PARA QUÉ SIRVE?", "celdas": [{"cab": "🧑‍🏫 AULA", "txt": "APRENDER"}, {"cab": "⚽ PATIO", "txt": "JUGAR"}, {"cab": "📚 BIBLIOTECA", "txt": "LEER"}, {"cab": "🍽️ COMEDOR", "txt": "COMER"}],
  "voz": ["Cada espacio sirve para algo.", "En el aula, *aprendemos*.", "En el patio, *jugamos*.", "En la biblioteca, *leemos*.", "En el comedor, *comemos*."]},
 {"t": "pregunta", "pregunta": "¿Dónde buscás un cuento?", "opciones": ["PATIO", "BIBLIOTECA", "BAÑO"], "correcta": 1,
  "voz": ["Ahora vos. Querés leer un cuento.", "¿Adónde vas?", "¡A la *biblioteca*!"]},
 {"t": "consejo", "titulo": "BAJITO", "texto": "En la biblioteca se habla bajito", "emoji": "🤫",
  "voz": ["Truco: en la biblioteca, hablá *bajito*."]},
 {"t": "resumen", "items": [["ESPACIOS", "aula, patio, biblioteca"], ["USO", "cada uno sirve para algo"], ["CUIDAR", "dejarlos limpios"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La escuela tiene muchos *espacios*.", "Cada uno tiene su *uso*.", "Y los *cuidamos* entre todos.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
