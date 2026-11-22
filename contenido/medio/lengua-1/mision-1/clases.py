# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 1 · Mi nombre y los nombres del grado: las 4 clases animadas.
Metáfora: el primer día de Sofi en primer grado. Regla de primeros años y regla de variedad del banco.
Genera tools/medio/clase/lecciones/medio-leng1-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '22b659ce-e46d-4587-99bc-b4fd7d19c384', 2: '32408f49-91d4-45ee-bd30-cff16db2e5e0', 3: 'b9e5507c-e7f9-401d-a573-a847df19dcff', 4: '925a339e-7f7b-42ed-990b-41a90d30b010'}
TIT = {1: 'Leer los nombres del grado', 2: 'Copiar mi nombre sin mirar', 3: 'Nombres que empiezan igual', 4: 'La lista de la clase'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🏫", "lineas": ["Es el primer día de clase.", "Cada mesa tiene un cartel.", "¿Dónde se sienta Sofi?"], "titulo": "LOS NOMBRES", "sub": "del grado",
  "voz": ["¡Es el *primer día* de clase!", "Cada mesa tiene un *cartel* con un nombre.", "¿Dónde se sienta Sofi?", "Hoy: *leer los nombres del grado*."]},
 {"t": "fichas", "fichas": ["S", "O", "F", "I"], "grande": "SOFI", "etiqueta": "¡ACÁ SE SIENTA SOFI!",
  "voz": ["Sofi busca su cartel: sss, o, fff, i.", "Las letras forman su nombre: *SOFI*.", "¡Encontró su lugar!"]},
 {"t": "bloques", "titulo": "LOS CARTELES DEL GRADO", "items": [{"cab": "TOMI", "txt": "empieza con T"}, {"cab": "ANA", "txt": "empieza con A"}, {"cab": "MATEO", "txt": "empieza con M"}],
  "voz": ["Mirá otros carteles del grado.", "Este dice *TOMI*.", "Este dice *ANA*.", "Y este dice *MATEO*."]},
 {"t": "comparar", "a": {"cab": "ANA", "texto": "3 letras", "emoji": "🐜"}, "b": {"cab": "MARTINA", "texto": "7 letras", "emoji": "🐍"}, "signo": "vs",
  "voz": ["*ANA* tiene 3 letras: es corto.", "*MARTINA* tiene 7 letras: es largo.", "¡Hay nombres *cortos* y *largos*!"]},
 {"t": "pregunta", "pregunta": "¿Cuántas letras tiene TOMI?", "opciones": ["3", "4", "5"], "correcta": 1,
  "voz": ["Ahora vos. Mirá el nombre TOMI.", "¿Cuántas letras tiene?", "¡*4*! Tomi tiene cuatro letras."]},
 {"t": "consejo", "titulo": "MIRÁ LA PRIMERA", "texto": "La primera letra te ayuda a encontrar el nombre", "emoji": "🔍",
  "voz": ["Truco: mirá la *primera letra* del cartel."]},
 {"t": "resumen", "items": [["CARTEL", "dice un nombre"], ["LETRAS", "forman el nombre"], ["LARGO", "tiene más letras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cada *cartel* dice un nombre.", "Las *letras* forman el nombre.", "Un nombre *largo* tiene más letras.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Podés escribir tu nombre sin mirar el cartel?", "segundos": 6, "respuesta": "¡SÍ!", "emoji": "🙈", "titulo": "SIN MIRAR", "sub": "copiar mi nombre",
  "voz": ["Desafío: ¿podés escribir tu nombre *sin mirar*?", "¡Claro que sí!", "Hoy: *copiar mi nombre sin mirar*."]},
 {"t": "fichas", "fichas": ["T", "O", "M", "I"], "grande": "TOMI", "etiqueta": "T · O · M · I",
  "voz": ["Tomi mira su cartel y dice las letras.", "to… mmm… i: *TOMI*.", "¡Las recuerda en *orden*!"]},
 {"t": "orden", "titulo": "LAS LETRAS DE MATEO", "items": [{"txt": "M", "emoji": "1️⃣"}, {"txt": "A", "emoji": "2️⃣"}, {"txt": "T", "emoji": "3️⃣"}, {"txt": "E", "emoji": "4️⃣"}, {"txt": "O", "emoji": "5️⃣"}], "relato": [2, 0, 4, 1, 3],
  "voz": ["¡Se mezclaron las letras de Mateo!", "Las ponemos en *orden*.", "mmm… a… te… o: *MATEO*."]},
 {"t": "antesdespues", "antes": {"cab": "PRIMERO", "emoji": "👀", "texto": "Miro el cartel y lo digo"}, "despues": {"cab": "DESPUÉS", "emoji": "✍️", "texto": "Lo tapo y lo escribo"},
  "voz": ["*Primero* miro el cartel y digo las letras.", "*Después* lo tapo y lo escribo."]},
 {"t": "pregunta", "pregunta": "¿Qué letra falta? MA_EO", "opciones": ["S", "T", "R"], "correcta": 1,
  "voz": ["Ahora vos. Falta una letra en Mateo.", "mmm… a… ¿qué sonido sigue?", "¡*te*! ma… te… o: MATEO."]},
 {"t": "errores", "items": [{"mal": "Cambiar el orden: TIMO", "bien": "Mismo orden: TOMI"}],
  "voz": ["Ojo con este error.", "Las letras van siempre en el *mismo orden*."]},
 {"t": "resumen", "items": [["MIRAR", "el cartel"], ["RECORDAR", "las letras en orden"], ["COMPARAR", "con el cartel"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero *miramos* el cartel.", "*Recordamos* las letras en orden.", "Y *comparamos* con el cartel.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Santi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¡Hola Sofi! Soy Santi"}, {"yo": True, "txt": "¡Empezamos igual!"}, {"yo": False, "txt": "¿Igual? ¿Cómo?"}], "titulo": "EMPIEZAN IGUAL", "sub": "los nombres",
  "voz": ["Santi le escribe a Sofi.", "¡Hola Sofi! Soy Santi.", "¡Nuestros nombres *empiezan igual*!", "Hoy: *nombres que empiezan igual*."]},
 {"t": "texto", "oracion": "SOFI Y SANTI SALTAN", "marcas": [{"desde": 0, "hasta": 0, "etiqueta": "S", "color": "sol"}, {"desde": 2, "hasta": 2, "etiqueta": "S", "color": "sol"}, {"desde": 3, "hasta": 3, "etiqueta": "S", "color": "sol"}],
  "voz": ["Leemos: Sofi y Santi saltan.", "*SOFI* empieza con sss.", "*SANTI* también empieza con sss.", "¡Y *SALTAN* también!"]},
 {"t": "matriz", "titulo": "NOMBRES QUE EMPIEZAN IGUAL", "celdas": [{"cab": "S", "txt": "SOFI · SANTI"}, {"cab": "M", "txt": "MATEO · MARTINA"}, {"cab": "L", "txt": "LUCÍA · LUCAS"}, {"cab": "A", "txt": "ANA · ALMA"}],
  "voz": ["Juntamos los que *empiezan igual*.", "Con *sss*: Sofi y Santi.", "Con *mmm*: Mateo y Martina.", "Con *lll*: Lucía y Lucas.", "Con *A*: Ana y Alma."]},
 {"t": "pregunta", "pregunta": "¿Qué nombre empieza igual que TOMI?", "opciones": ["BRUNO", "ANA", "TERE"], "correcta": 2,
  "voz": ["Ahora vos. Mirá la primera letra.", "¿Qué nombre empieza igual que Tomi?", "¡*TERE*! To-mi y te-re empiezan igual."]},
 {"t": "consejo", "titulo": "SOLO LA PRIMERA", "texto": "Para agrupar, mirá solo la primera letra", "emoji": "1️⃣",
  "voz": ["Truco: mirá solo la *primera letra*."]},
 {"t": "errores", "items": [{"mal": "Mirar la última letra", "bien": "Mirar la primera letra"}],
  "voz": ["Ojo con este error.", "Mirá la *primera* letra, no la última."]},
 {"t": "resumen", "items": [["PRIMERA", "la letra de adelante"], ["IGUAL", "SOFI y SANTI"], ["GRUPOS", "por la primera letra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Miramos la *primera letra*.", "Sofi y Santi *empiezan igual*.", "Armamos *grupos* por la primera letra.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "AVISO DE LA SEÑO", "titular": "¡HOY PASAMOS LISTA!", "bajada": "Cada uno dice presente", "emoji": "📋", "titulo": "LA LISTA", "sub": "de la clase",
  "voz": ["¡Aviso de la seño!", "Hoy pasamos *lista*.", "Hoy: *la lista de la clase*."]},
 {"t": "contar", "titulo": "LOS CHICOS DEL GRADO", "emoji": "🧒", "cantidad": 6, "etiqueta": "6 NOMBRES EN LA LISTA",
  "voz": ["Contamos a los chicos del grado.", "1, 2, 3, 4, 5, 6.", "¡Son *6*! La lista tiene 6 nombres."]},
 {"t": "linea", "titulo": "LA LISTA EN ORDEN", "eventos": [{"fecha": "1", "txt": "ANA", "emoji": "👧"}, {"fecha": "2", "txt": "BRUNO", "emoji": "👦"}, {"fecha": "3", "txt": "LUCÍA", "emoji": "👧"}, {"fecha": "4", "txt": "MATEO", "emoji": "👦"}, {"fecha": "5", "txt": "SOFI", "emoji": "👧"}],
  "voz": ["Número 1: *ANA*, con A.", "Número 2: *BRUNO*, bru-no.", "Número 3: *LUCÍA*, con lll.", "Número 4: *MATEO*, con mmm.", "Número 5: *SOFI*, con sss."]},
 {"t": "orden", "titulo": "¿CÓMO VAN EN LA LISTA?", "items": [{"txt": "ANA", "emoji": "🅰️"}, {"txt": "MATEO", "emoji": "Ⓜ️"}, {"txt": "SOFI", "emoji": "🔤"}], "relato": [2, 0, 1],
  "voz": ["Sofi, Ana y Mateo están mezclados.", "Los ordenamos por la *primera letra*.", "a… mmm… sss: ¡Ana, Mateo y Sofi!"]},
 {"t": "pregunta", "pregunta": "En la lista, ¿qué número tiene SOFI?", "opciones": ["1", "5", "6"], "correcta": 1,
  "voz": ["Ahora vos. Buscá a Sofi en la lista.", "¿Qué número tiene?", "¡El *5*!"]},
 {"t": "resumen", "items": [["LISTA", "uno abajo del otro"], ["NÚMERO", "dice el lugar"], ["BUSCAR", "por la primera letra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la *lista*, uno abajo del otro.", "El *número* dice el lugar.", "*Buscamos* por la primera letra.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m1-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
