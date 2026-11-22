# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 4 · Letras S y L: las 4 clases animadas.
Metáfora: un día de sol en la laguna. Regla de primeros años y de variedad del banco.
Genera tools/medio/clase/lecciones/medio-leng1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '4bd75bb0-105d-4023-b668-ff3596f34893', 2: '8979d6de-4115-406c-badc-dcc9c7f4295f', 3: '15a22426-bba2-4f42-85c4-1e638d31a22d', 4: '0edd03d1-3361-439b-80a5-9dcbd6b14b60'}
TIT = {1: 'Conocer la S y la L', 2: 'Leer sílabas con S y L', 3: 'Leer palabras con S y L', 4: 'Escribir palabras con S y L'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "☀️", "lineas": ["Hace sol en la laguna.", "Sofi lleva una lupa.", "¡Encuentra un sapo!"], "titulo": "LA S Y LA L", "sub": "en la laguna",
  "voz": ["Hace *sol* en la laguna.", "Sofi lleva una *lupa*.", "¡Y encuentra un *sapo*!", "Hoy: *los sonidos sss y lll*."]},
 {"t": "zoom", "niveles": [{"emoji": "☀️", "txt": "SOL"}, {"emoji": "🐍", "txt": "S suena sss"}, {"emoji": "🔍", "txt": "L de LUPA"}],
  "voz": ["Esta palabra es *SOL*.", "Suena como una víbora: *sss*.", "Y en *lupa* escuchamos lll."]},
 {"t": "comparar", "a": {"cab": "S", "texto": "SOL · SAPO · SOPA", "emoji": "🐸"}, "b": {"cab": "L", "texto": "LUPA · LOMA · LILA", "emoji": "🔍"}, "signo": "y",
  "voz": ["Con *sss*: sol, sapo y sopa.", "Con *lll*: lupa, loma y lila.", "¡Dos letras nuevas para leer!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza con L?", "opciones": ["SAPO", "LOMA", "PALA"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá cada palabra.", "¿Cuál empieza con *lll*?", "¡*LOMA*! lll… o… ma."]},
 {"t": "consejo", "titulo": "ESCUCHÁ EL SONIDO", "texto": "S suena sss · L suena lll", "emoji": "👂",
  "voz": ["Truco: *escuchá* el sonido de cada letra."]},
 {"t": "resumen", "items": [["S", "de SOL"], ["L", "de LUPA"], ["SONIDO", "sss y lll"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*sss* de sol.", "*lll* de lupa.", "Suenan *sss* y *lll*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cómo suenan juntas la S y la A?", "segundos": 6, "respuesta": "¡SA!", "emoji": "🐸", "titulo": "SÍLABAS", "sub": "con S y L",
  "voz": ["Desafío: ¿cómo suenan juntos sss y a?", "¡*SA*!", "Hoy: *sílabas con sss y lll*."]},
 {"t": "silabas", "palabra": "SAPO", "silabas": ["SA", "PO"], "tonica": 0, "tipo": "2 SÍLABAS",
  "voz": ["Esta palabra es *SAPO*.", "La cortamos: SA, PO.", "¡Tiene *2 sílabas*!"]},
 {"t": "tabla", "titulo": "LA S Y LA L CON LAS VOCALES", "columnas": ["CON S", "CON L"], "filas": [["SA", "LA"], ["SE", "LE"], ["SI", "LI"], ["SO", "LO"], ["SU", "LU"]],
  "voz": ["Las juntamos con cada vocal.", "*SA* y *LA*.", "*SE* y *LE*.", "*SI* y *LI*.", "*SO* y *LO*.", "*SU* y *LU*."]},
 {"t": "antesdespues", "antes": {"cab": "ASÍ", "emoji": "➡️", "texto": "LA"}, "despues": {"cab": "AL REVÉS", "emoji": "↩️", "texto": "AL"},
  "voz": ["Si lll va primero, dice *LA*.", "Si la a va primero, dice *AL*."]},
 {"t": "pregunta", "pregunta": "¿Cómo se lee S con O?", "opciones": ["OS", "SO", "LO"], "correcta": 1,
  "voz": ["Ahora vos. Juntá sss y o.", "¿Cómo se lee?", "¡*SO*!"]},
 {"t": "resumen", "items": [["CON S", "SA, SE, SI, SO, SU"], ["CON L", "LA, LE, LI, LO, LU"], ["AL REVÉS", "AL, EL"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*SA, SE, SI, SO, SU*.", "*LA, LE, LI, LO, LU*.", "Y al revés: *AL, EL*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Qué viste en la laguna?"}, {"yo": True, "txt": "EL SAPO ES MALO"}, {"yo": False, "txt": "¡Ja! ¡Lo leí solo!"}], "titulo": "LEER", "sub": "palabras con S y L",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué viste en la laguna?", "Sofi contesta con una oración.", "Hoy: *leer palabras con sss y lll*."]},
 {"t": "texto", "oracion": "EL SAPO ES MALO", "marcas": [{"desde": 1, "hasta": 1, "etiqueta": "SA-PO", "color": "sol"}, {"desde": 3, "hasta": 3, "etiqueta": "MA-LO", "color": "sol"}],
  "voz": ["Leemos: el sapo es malo.", "*SAPO*: SA, PO.", "*MALO*: MA, LO."]},
 {"t": "venn", "a": "CON S", "b": "CON L", "itemsA": ["SOPA", "MESA"], "itemsB": ["LUPA", "LOMA"], "ambos": ["SAL", "SOL"],
  "voz": ["Separamos palabras.", "*SOPA* y *MESA* tienen sss.", "*LUPA* y *LOMA* tienen lll.", "¡*SAL* y *SOL* tienen las dos!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra forman PA y LA?", "opciones": ["LAPA", "PALA", "PAPA"], "correcta": 1,
  "voz": ["Ahora vos. Juntá PA y LA.", "¿Qué palabra se forma?", "¡*PALA*!"]},
 {"t": "consejo", "titulo": "PALABRA POR PALABRA", "texto": "Leé cada palabra y después todo junto", "emoji": "📖",
  "voz": ["Truco: leé *palabra por palabra*."]},
 {"t": "resumen", "items": [["SÍLABAS", "SA + PO"], ["PALABRAS", "SAPO"], ["ORACIÓN", "dice algo completo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Juntamos *sílabas*.", "Leemos *palabras*.", "Y leemos una *oración*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "LAGUNA", "titular": "¡SOFI HACE UN CARTEL!", "bajada": "Escribe con S y L", "emoji": "🪧", "titulo": "ESCRIBIR", "sub": "palabras con S y L",
  "voz": ["¡Sofi hace un *cartel* para la laguna!", "Escribe palabras con sss y lll.", "Hoy: *escribir con sss y lll*."]},
 {"t": "fichas", "fichas": ["S", "O", "L"], "grande": "SOL", "etiqueta": "S · O · L",
  "voz": ["Sofi dice despacio: sss, o, lll.", "Escribe sss, o, lll: *SOL*.", "¡No se olvidó el lll del final!"]},
 {"t": "orden", "titulo": "ARMAMOS LUPA", "items": [{"txt": "L", "emoji": "1️⃣"}, {"txt": "U", "emoji": "2️⃣"}, {"txt": "P", "emoji": "3️⃣"}, {"txt": "A", "emoji": "4️⃣"}], "relato": [3, 0, 2, 1],
  "voz": ["Las letras de LUPA se mezclaron.", "Las ponemos en *orden*.", "lll… u… pa: ¡*LUPA*!"]},
 {"t": "matriz", "titulo": "EL CARTEL DE SOFI", "celdas": [{"cab": "SOL", "txt": "S · O · L"}, {"cab": "SAPO", "txt": "SA · PO"}, {"cab": "PALA", "txt": "PA · LA"}, {"cab": "LUPA", "txt": "LU · PA"}],
  "voz": ["Sofi escribe cuatro palabras.", "*SOL*.", "*SAPO*.", "*PALA*.", "Y *LUPA*. ¡Qué lindo cartel!"]},
 {"t": "pregunta", "pregunta": "¿Qué letra falta? SO_", "opciones": ["L", "P", "M"], "correcta": 0,
  "voz": ["Ahora vos. sss, o, hueco.", "¿Qué letra falta?", "¡Falta *lll*! SOL."]},
 {"t": "resumen", "items": [["ESCUCHAR", "sss-O-lll"], ["ESCRIBIR", "letra por letra"], ["REVISAR", "leer lo escrito"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Escuchamos* cada sonido.", "*Escribimos* letra por letra.", "Y *revisamos* leyendo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m4-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 4 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
