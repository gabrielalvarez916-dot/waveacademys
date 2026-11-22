# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 5 · Letras T, N y D: las 4 clases animadas.
Metáfora: la huerta de la abuela de Sofi. Regla de primeros años y de variedad del banco.
Genera tools/medio/clase/lecciones/medio-leng1-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'd0d6b4e9-3265-493a-8fa6-445ff872ce42', 2: '7cab90e7-83ec-4710-b711-9e8faecdc727', 3: '601aa16a-7ab3-4c88-b3ac-ea2231667c90', 4: '54a91e6e-0a67-4484-80ae-55454bc76c41'}
TIT = {1: 'Conocer la T', 2: 'Conocer la N y la D', 3: 'Leer palabras con T, N y D', 4: 'Escribir palabras con T, N y D'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍅", "lineas": ["Sofi visita a su abuela.", "La abuela tiene una huerta.", "¡Hay tomates rojos!"], "titulo": "LA T", "sub": "de tomate",
  "voz": ["Sofi visita a su *abuela*.", "La abuela tiene una *huerta*.", "¡Hay tomates bien rojos!", "Hoy: *conocer la T*."]},
 {"t": "silabas", "palabra": "TOMATE", "silabas": ["TO", "MA", "TE"], "tonica": 1, "tipo": "3 SÍLABAS",
  "voz": ["Esta palabra es *TOMATE*.", "La cortamos: TO, MA, TE.", "¡Tiene *2 T* y 3 sílabas!"]},
 {"t": "linea", "titulo": "LA T CON LAS VOCALES", "eventos": [{"fecha": "TA", "txt": "TAPA", "emoji": "🫙"}, {"fecha": "TE", "txt": "TELA", "emoji": "🧵"}, {"fecha": "TI", "txt": "TINA", "emoji": "🛁"}, {"fecha": "TO", "txt": "TOMATE", "emoji": "🍅"}, {"fecha": "TU", "txt": "TUNA", "emoji": "🌵"}],
  "voz": ["*TA* de tapa.", "*TE* de tela.", "*TI* de tina.", "*TO* de tomate.", "*TU* de tuna."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza con T?", "opciones": ["DADO", "TAPA", "NIDO"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá cada palabra.", "¿Cuál empieza con *T*?", "¡*TAPA*!"]},
 {"t": "consejo", "titulo": "COMO UN RELOJ", "texto": "La T suena corta: t, t, t", "emoji": "⏰",
  "voz": ["Truco: la T suena como un *reloj*: t, t, t."]},
 {"t": "resumen", "items": [["T", "de TOMATE"], ["SÍLABAS", "TA, TE, TI, TO, TU"], ["LUGAR", "principio o medio"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *T* de tomate.", "*TA, TE, TI, TO, TU*.", "Puede estar al *principio* o en el *medio*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué hay en el árbol de la abuela?", "segundos": 6, "respuesta": "¡UN NIDO!", "emoji": "🪺", "titulo": "LA N Y LA D", "sub": "letras nuevas",
  "voz": ["Desafío: ¿qué hay en el árbol?", "¡Un *NIDO*!", "Hoy: *conocer la N y la D*."]},
 {"t": "comparar", "a": {"cab": "N", "texto": "de NIDO · nnn", "emoji": "🪺"}, "b": {"cab": "D", "texto": "de DEDO · d", "emoji": "☝️"}, "signo": "y",
  "voz": ["La *N* de nido suena por la nariz.", "La *D* de dedo: la lengua toca los dientes.", "¡Dos letras nuevas!"]},
 {"t": "parejas", "a": {"emoji": "🪺", "n": 3}, "b": {"emoji": "🐣", "n": 3}, "texto": "¡UN NIDO PARA CADA POLLITO!",
  "voz": ["Hay nidos y pollitos.", "Unimos cada *pollito* con su *nido*.", "¡Un nido para cada uno!"]},
 {"t": "tabla", "titulo": "LA N Y LA D CON LAS VOCALES", "columnas": ["CON N", "CON D"], "filas": [["NA", "DA"], ["NE", "DE"], ["NI", "DI"], ["NO", "DO"], ["NU", "DU"]],
  "voz": ["Las juntamos con cada vocal.", "*NA* y *DA*.", "*NE* y *DE*.", "*NI* y *DI*.", "*NO* y *DO*.", "*NU* y *DU*."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza con D?", "opciones": ["MANO", "DAMA", "LUNA"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá cada palabra.", "¿Cuál empieza con *D*?", "¡*DAMA*!"]},
 {"t": "resumen", "items": [["N", "de NIDO"], ["D", "de DEDO"], ["SÍLABAS", "NA… DA…"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *N* de nido.", "La *D* de dedo.", "*NA, NE, NI*… *DA, DE, DI*…", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Abuela", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "EL PATO TOMA SOPA"}, {"yo": True, "txt": "¡Lo leí, abuela!"}, {"yo": False, "txt": "¡Qué bien lees, Sofi!"}], "titulo": "LEER", "sub": "palabras con T, N y D",
  "voz": ["La abuela le escribe a Sofi.", "Le manda una oración.", "¡Y Sofi la lee sola!", "Hoy: *leer palabras con T, N y D*."]},
 {"t": "texto", "oracion": "EL PATO TOMA SOPA", "marcas": [{"desde": 1, "hasta": 1, "etiqueta": "PA-TO", "color": "sol"}, {"desde": 2, "hasta": 2, "etiqueta": "TO-MA", "color": "sol"}, {"desde": 3, "hasta": 3, "etiqueta": "SO-PA", "color": "sol"}],
  "voz": ["Leemos: el pato toma sopa.", "*PATO*: PA, TO.", "*TOMA*: TO, MA.", "*SOPA*: SO, PA."]},
 {"t": "bloques", "titulo": "PALABRAS DE LA HUERTA", "items": [{"cab": "LUNA", "txt": "LU + NA"}, {"cab": "NIDO", "txt": "NI + DO"}, {"cab": "MONO", "txt": "MO + NO"}],
  "voz": ["Leemos más palabras.", "LU y NA: *LUNA*.", "NI y DO: *NIDO*.", "MO y NO: *MONO*."]},
 {"t": "antesdespues", "antes": {"cab": "PRIMERA VEZ", "emoji": "🐢", "texto": "Leo despacio"}, "despues": {"cab": "SEGUNDA VEZ", "emoji": "🐇", "texto": "Leo más rápido"},
  "voz": ["La *primera vez* leemos despacio.", "La *segunda vez*, más rápido."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra forman LU y NA?", "opciones": ["NALU", "LUNA", "LANA"], "correcta": 1,
  "voz": ["Ahora vos. Juntá LU y NA.", "¿Qué palabra se forma?", "¡*LUNA*!"]},
 {"t": "resumen", "items": [["SÍLABAS", "TO-MA-TE"], ["PALABRAS", "TOMATE"], ["ORACIÓN", "EL PATO TOMA SOPA"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos *sílabas*.", "Formamos *palabras*.", "Y leemos *oraciones*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "HUERTA DE LA ABUELA", "titular": "¡HAY QUE PONER CARTELES!", "bajada": "Sofi escribe los nombres", "emoji": "🪧", "titulo": "ESCRIBIR", "sub": "palabras con T, N y D",
  "voz": ["¡La huerta necesita *carteles*!", "Sofi escribe los nombres.", "Hoy: *escribir palabras con T, N y D*."]},
 {"t": "fichas", "fichas": ["P", "A", "T", "O"], "grande": "PATO", "etiqueta": "PA · TO",
  "voz": ["Sofi dice despacio: PA, TO.", "Escribe P, A, T, O: *PATO*.", "¡El cartel del pato está listo!"]},
 {"t": "venn", "a": "CON T", "b": "CON D", "itemsA": ["TAPA", "PATO"], "itemsB": ["DADO", "NIDO"], "ambos": ["TODO", "DATO"],
  "voz": ["¿T o D? Separamos palabras.", "*TAPA* y *PATO* llevan T.", "*DADO* y *NIDO* llevan D.", "¡*TODO* y *DATO* llevan las dos!"]},
 {"t": "orden", "titulo": "ARMAMOS MANO", "items": [{"txt": "M", "emoji": "1️⃣"}, {"txt": "A", "emoji": "2️⃣"}, {"txt": "N", "emoji": "3️⃣"}, {"txt": "O", "emoji": "4️⃣"}], "relato": [2, 0, 3, 1],
  "voz": ["Las letras de MANO se mezclaron.", "Las ponemos en *orden*.", "M, A, N, O: ¡*MANO*!"]},
 {"t": "pregunta", "pregunta": "¿Qué letra falta? DE_O", "opciones": ["T", "D", "N"], "correcta": 1,
  "voz": ["Ahora vos. D, E, hueco, O.", "¿Qué letra falta?", "¡La *D*! DEDO."]},
 {"t": "resumen", "items": [["ESCUCHAR", "PA-TO"], ["T O D", "decir lento"], ["REVISAR", "leer lo escrito"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Escuchamos* cada sílaba.", "Para *T o D*, decimos lento.", "Y *revisamos* leyendo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m5-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 5 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
