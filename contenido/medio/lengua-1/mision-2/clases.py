# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 2 · Las vocales: las 4 clases animadas.
Metáfora: las cinco vocales son cinco amigas que viven en todas las palabras. Regla de primeros años y de variedad del banco.
Genera tools/medio/clase/lecciones/medio-leng1-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'f12fc1cc-11d2-4418-a706-1e8aa1c56299', 2: 'e6634674-36eb-412a-b3fd-7ddd5efa9934', 3: '4fdf4428-b752-4001-a3db-3295e1ce0e2f', 4: '6d0ecca3-e1fa-4f50-826b-aeeb148a27ab'}
TIT = {1: 'Las cinco vocales', 2: 'Vocales en los nombres', 3: 'Vocales en las palabras', 4: 'Escribir palabras con vocales'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📖", "lineas": ["Sofi abre un libro.", "Ve cinco letras que se repiten.", "¡Están en todas las palabras!"], "titulo": "LAS VOCALES", "sub": "cinco amigas",
  "voz": ["Sofi abre un libro de cuentos.", "Ve cinco letras que aparecen mucho.", "¡Están en *todas* las palabras!", "Hoy: *las cinco vocales*."]},
 {"t": "fichas", "fichas": ["A", "E", "I", "O", "U"], "grande": "A E I O U", "etiqueta": "LAS 5 VOCALES",
  "voz": ["Estas son las *vocales*: A, E, I, O, U.", "Son cinco amigas.", "¡Las vas a encontrar en todos lados!"]},
 {"t": "tabla", "titulo": "CADA VOCAL Y SU PALABRA", "columnas": ["VOCAL", "PALABRA"], "filas": [["A", "ANA"], ["E", "ESTRELLA"], ["I", "ISLA"], ["O", "OSO"], ["U", "UVA"]],
  "voz": ["Cada vocal tiene su palabra.", "*A* de Ana.", "*E* de estrella.", "*I* de isla.", "*O* de oso.", "*U* de uva."]},
 {"t": "contar", "titulo": "¿CUÁNTAS VOCALES HAY?", "emoji": "🔤", "cantidad": 5, "etiqueta": "5 VOCALES",
  "voz": ["Contamos las vocales.", "1, 2, 3, 4, 5.", "¡Son *5* vocales!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es una vocal?", "opciones": ["M", "O", "S"], "correcta": 1,
  "voz": ["Ahora vos. Mirá las tres letras.", "¿Cuál es una vocal?", "¡La *O*!"]},
 {"t": "consejo", "titulo": "ABRÍ LA BOCA", "texto": "Las vocales se dicen con la boca abierta", "emoji": "😮",
  "voz": ["Truco: las vocales se dicen con la *boca abierta*."]},
 {"t": "resumen", "items": [["CINCO", "A, E, I, O, U"], ["SUENAN", "solas"], ["PALABRAS", "oso, uva"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Hay *cinco* vocales.", "Suenan *solas*.", "Y están en *todas* las palabras.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué vocales tiene el nombre SOFI?", "segundos": 6, "respuesta": "¡O e I!", "emoji": "🔎", "titulo": "VOCALES", "sub": "en los nombres",
  "voz": ["Desafío: ¿qué vocales tiene SOFI?", "¡La *O* y la *I*!", "Hoy: *vocales en los nombres*."]},
 {"t": "zoom", "niveles": [{"emoji": "👧", "txt": "SOFI"}, {"emoji": "🔍", "txt": "S · O · F · I"}, {"emoji": "🔤", "txt": "VOCALES: O · I"}],
  "voz": ["Esta es *SOFI*.", "Miramos su nombre letra por letra.", "¡Encontramos las vocales: *O* e *I*!"]},
 {"t": "matriz", "titulo": "LAS VOCALES DE CADA NOMBRE", "celdas": [{"cab": "ANA", "txt": "A · A"}, {"cab": "TOMI", "txt": "O · I"}, {"cab": "MATEO", "txt": "A · E · O"}, {"cab": "LUCÍA", "txt": "U · I · A"}],
  "voz": ["Buscamos vocales en otros nombres.", "*ANA*: A y A.", "*TOMI*: O e I.", "*MATEO*: A, E y O.", "*LUCÍA*: U, I y A."]},
 {"t": "pregunta", "pregunta": "¿Cuántas vocales tiene ANA?", "opciones": ["1", "2", "3"], "correcta": 1,
  "voz": ["Ahora vos. Mirá el nombre ANA.", "¿Cuántas vocales tiene?", "¡*2*! A y A."]},
 {"t": "consejo", "titulo": "LETRA POR LETRA", "texto": "Preguntá: ¿es vocal?", "emoji": "👆",
  "voz": ["Truco: mirá *letra por letra* y preguntá."]},
 {"t": "errores", "items": [{"mal": "Contar la A de ANA una vez", "bien": "Las vocales se pueden repetir"}],
  "voz": ["Ojo con este error.", "Una vocal se puede *repetir*."]},
 {"t": "resumen", "items": [["BUSCAR", "letra por letra"], ["MARCAR", "A, E, I, O, U"], ["REPETIR", "ANA: A y A"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Buscamos* letra por letra.", "*Marcamos* las vocales.", "Y algunas se *repiten*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Hay palabras sin vocales?"}, {"yo": True, "txt": "¡Busquemos una!"}, {"yo": False, "txt": "No encuentro ninguna"}], "titulo": "VOCALES", "sub": "en las palabras",
  "voz": ["Tomi le escribe a Sofi.", "¿Hay palabras *sin* vocales?", "¡Busquemos una!", "Hoy: *vocales en las palabras*."]},
 {"t": "venn", "a": "CON A", "b": "CON O", "itemsA": ["MESA", "CASA"], "itemsB": ["OSO", "GLOBO"], "ambos": ["PELOTA", "VASO"],
  "voz": ["Separamos palabras por sus vocales.", "*MESA* y *CASA* tienen A.", "*OSO* y *GLOBO* tienen O.", "¡*PELOTA* y *VASO* tienen las dos!"]},
 {"t": "comparar", "a": {"cab": "VOCALES", "texto": "A, E, I, O, U", "emoji": "😮"}, "b": {"cab": "OTRAS LETRAS", "texto": "M, P, S, T…", "emoji": "🤐"}, "signo": "y",
  "voz": ["Las *vocales* suenan solas.", "Las *otras letras* necesitan una vocal.", "¡Juntas forman las palabras!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra tiene la U?", "opciones": ["MESA", "LUNA", "PATO"], "correcta": 1,
  "voz": ["Ahora vos. Decí cada palabra despacio.", "¿Cuál tiene la *U*?", "¡*LUNA*! L, U, N, A."]},
 {"t": "consejo", "titulo": "DECILA DESPACIO", "texto": "Así escuchás cada vocal", "emoji": "🐢",
  "voz": ["Truco: decí la palabra *despacio*."]},
 {"t": "resumen", "items": [["TODAS", "tienen vocales"], ["LUGAR", "principio, medio o final"], ["ESCUCHAR", "decir lento"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Todas* las palabras tienen vocales.", "Están en *cualquier lugar*.", "Las *escuchamos* diciendo lento.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "¡ATENCIÓN!", "titular": "¡SE ESCAPARON LAS VOCALES!", "bajada": "Hay palabras con huecos", "emoji": "🚨", "titulo": "ESCRIBIR", "sub": "palabras con vocales",
  "voz": ["¡Atención! ¡Se escaparon las *vocales*!", "Hay palabras con *huecos*.", "Hoy: *escribir palabras con vocales*."]},
 {"t": "antesdespues", "antes": {"cab": "CON HUECOS", "emoji": "🕳️", "texto": "O _ O"}, "despues": {"cab": "COMPLETA", "emoji": "🐻", "texto": "OSO"},
  "voz": ["*Antes*: O, hueco, O. No se lee.", "¡Ponemos la S y dice *OSO*!"]},
 {"t": "orden", "titulo": "ARMAMOS UVA", "items": [{"txt": "U", "emoji": "1️⃣"}, {"txt": "V", "emoji": "2️⃣"}, {"txt": "A", "emoji": "3️⃣"}], "relato": [2, 0, 1],
  "voz": ["Las letras de UVA están mezcladas.", "Las ponemos en *orden*.", "U, V, A: ¡*UVA*!"]},
 {"t": "fichas", "fichas": ["M", "E", "S", "A"], "grande": "MESA", "etiqueta": "FALTABAN LA E Y LA A",
  "voz": ["M, hueco, S, hueco. ¿Qué es?", "Ponemos la E y la A: *MESA*.", "¡Volvieron las vocales!"]},
 {"t": "pregunta", "pregunta": "¿Qué vocal falta? L_NA", "opciones": ["A", "U", "E"], "correcta": 1,
  "voz": ["Ahora vos. L, hueco, N, A.", "¿Qué vocal falta?", "¡La *U*! LUNA."]},
 {"t": "resumen", "items": [["HUECO", "falta una letra"], ["COMPLETAR", "con una vocal"], ["LEER", "la palabra entera"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *hueco* es una letra que falta.", "Lo *completamos* con una vocal.", "Y *leemos* la palabra entera.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m2-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 2 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
