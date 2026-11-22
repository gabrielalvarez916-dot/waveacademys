# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 7 · Letras C, F y B: las 4 clases animadas.
Metáfora: un paseo por el mar. Regla de primeros años, vía fonológica (la voz dice ca, fff, ba; nunca el nombre de la letra) y variedad del banco.
Genera tools/medio/clase/lecciones/medio-leng1-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '488886cb-6f0d-4c3b-a8ac-f67a7783dd67', 2: '19128ec8-46c6-4906-aae0-754bdf6ff5ad', 3: '719a22c2-1860-49b1-8be3-30030c033e6b', 4: 'fd7928cc-d488-4bf8-8814-80125c0e0b79'}
TIT = {1: 'Conocer la C y la F', 2: 'Conocer la B', 3: 'Leer palabras con C, F y B', 4: 'Escribir palabras con C, F y B'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🌊", "lineas": ["Sofi pasea por el mar.", "Ve una foca en una roca.", "¡Y una casa en la playa!"], "titulo": "LA C Y LA F", "sub": "en el mar",
  "voz": ["Sofi pasea por el *mar*.", "Ve una *foca* en una roca.", "¡Y una *casa* en la playa!", "Hoy: *los sonidos de casa y foca*."]},
 {"t": "comparar", "a": {"cab": "C", "texto": "CASA · COCO · CUNA", "emoji": "🏠"}, "b": {"cab": "F", "texto": "FOCA · FOTO · FIDEO", "emoji": "🦭"}, "signo": "y",
  "voz": ["En *casa*, *coco* y *cuna*: ca, co, cu.", "En *foca*, *foto* y *fideo*: fff.", "¡Dos sonidos nuevos!"]},
 {"t": "silabas", "palabra": "FOCA", "silabas": ["FO", "CA"], "tonica": 0, "tipo": "2 SÍLABAS",
  "voz": ["Esta palabra es *FOCA*.", "La cortamos: fo, ca.", "¡Tiene *2 sílabas*!"]},
 {"t": "consejo", "titulo": "SOPLÁ", "texto": "Para decir fff, los dientes tocan el labio", "emoji": "🌬️",
  "voz": ["Truco: para decir *fff*, soplá suavecito."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza como FOCA?", "opciones": ["CASA", "FOTO", "BOTA"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá: fff… oca.", "¿Qué palabra empieza igual?", "¡*FOTO*! fff… oto."]},
 {"t": "resumen", "items": [["CASA", "ca, co, cu"], ["FOCA", "fff"], ["SÍLABAS", "FO-CA"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En casa: *ca, co, cu*.", "En foca: *fff*.", "Y leemos *fo-ca*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué flota en el mar y lleva gente?", "segundos": 6, "respuesta": "¡UN BOTE!", "emoji": "⛵", "titulo": "UN SONIDO", "sub": "nuevo",
  "voz": ["Desafío: ¿qué flota en el mar y lleva gente?", "¡Un *BOTE*!", "Hoy: *el sonido de bote*."]},
 {"t": "silabas", "palabra": "BOTE", "silabas": ["BO", "TE"], "tonica": 0, "tipo": "2 SÍLABAS",
  "voz": ["Esta palabra es *BOTE*.", "La cortamos: bo, te.", "¡Empieza con *bo*!"]},
 {"t": "tabla", "titulo": "CON LAS VOCALES", "columnas": ["SÍLABA", "PALABRA"], "filas": [["BA", "BALDE"], ["BE", "BEBÉ"], ["BI", "BICI"], ["BO", "BOTE"], ["BU", "BÚHO"]],
  "voz": ["Juntamos el sonido con cada vocal.", "*ba*.", "*be*.", "*bi*.", "*bo*.", "*bu*."]},
 {"t": "antesdespues", "antes": {"cab": "LABIOS JUNTOS", "emoji": "😶", "texto": "Cierro la boca"}, "despues": {"cab": "SE ABREN", "emoji": "😮", "texto": "¡BA!"},
  "voz": ["Primero juntamos los *labios*.", "Los abrimos con la voz: ¡*ba*!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra empieza como BOTE?", "opciones": ["FOCA", "BOCA", "CASA"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá: bo… te.", "¿Qué palabra empieza igual?", "¡*BOCA*! bo… ca."]},
 {"t": "resumen", "items": [["BOTE", "empieza con bo"], ["SÍLABAS", "ba, be, bi, bo, bu"], ["LABIOS", "se juntan y se abren"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Bote* empieza con bo.", "*ba, be, bi, bo, bu*.", "Los *labios* se juntan y se abren.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Qué viste en el mar?"}, {"yo": True, "txt": "LA FOCA TOMA UN COCO"}, {"yo": False, "txt": "¡Ja! ¡Lo leí!"}], "titulo": "LEER", "sub": "palabras del mar",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué viste en el mar?", "Sofi contesta con una oración.", "Hoy: *leer palabras del mar*."]},
 {"t": "texto", "oracion": "LA FOCA TOMA UN COCO", "marcas": [{"desde": 1, "hasta": 1, "etiqueta": "FO-CA", "color": "sol"}, {"desde": 2, "hasta": 2, "etiqueta": "TO-MA", "color": "sol"}, {"desde": 4, "hasta": 4, "etiqueta": "CO-CO", "color": "sol"}],
  "voz": ["Leemos: la foca toma un coco.", "*FOCA*: fo, ca.", "*TOMA*: to, ma.", "*COCO*: co, co."]},
 {"t": "venn", "a": "CON F", "b": "CON B", "itemsA": ["FOTO", "FIDEO"], "itemsB": ["BOTE", "NUBE"], "ambos": ["FÚTBOL", "FIEBRE"],
  "voz": ["Separamos palabras por su sonido.", "*FOTO* y *FIDEO* suenan con fff.", "*BOTE* y *NUBE* suenan con ba, be.", "¡*FÚTBOL* tiene los dos!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra forman CU y NA?", "opciones": ["NACU", "CUNA", "CUBA"], "correcta": 1,
  "voz": ["Ahora vos. Juntá cu y na.", "¿Qué palabra se forma?", "¡*CUNA*!"]},
 {"t": "consejo", "titulo": "LEÉ DOS VECES", "texto": "Primero despacio, después más rápido", "emoji": "🔁",
  "voz": ["Truco: leé *dos veces*, la segunda más rápido."]},
 {"t": "resumen", "items": [["SÍLABAS", "FO-CA"], ["PALABRAS", "FOCA, BOTE"], ["ORACIÓN", "LA FOCA TOMA UN COCO"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos *sílabas*.", "Formamos *palabras*.", "Y leemos *oraciones*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "DIARIO DEL MAR", "titular": "¡SOFI ESCRIBE UNA POSTAL!", "bajada": "Con palabras del mar", "emoji": "💌", "titulo": "ESCRIBIR", "sub": "palabras del mar",
  "voz": ["¡Sofi escribe una *postal* desde el mar!", "Usa palabras con sonidos nuevos.", "Hoy: *escribir palabras del mar*."]},
 {"t": "fichas", "fichas": ["F", "O", "C", "A"], "grande": "FOCA", "etiqueta": "FO · CA",
  "voz": ["Sofi dice despacio: fff… o… ca.", "Escribe y se forma *FOCA*.", "¡La primera palabra de la postal!"]},
 {"t": "orden", "titulo": "ARMAMOS BOTA", "items": [{"txt": "B", "emoji": "1️⃣"}, {"txt": "O", "emoji": "2️⃣"}, {"txt": "T", "emoji": "3️⃣"}, {"txt": "A", "emoji": "4️⃣"}], "relato": [2, 3, 0, 1],
  "voz": ["Las letras de BOTA se mezclaron.", "Las ponemos en *orden*.", "bo… ta: ¡*BOTA*!"]},
 {"t": "comparar", "a": {"cab": "BOTA", "texto": "la voz vibra", "emoji": "👢"}, "b": {"cab": "PATO", "texto": "sale aire", "emoji": "🦆"}, "signo": "vs",
  "voz": ["En *bota*, la garganta vibra.", "En *pato*, sale aire.", "¡Tocá tu garganta y probá!"]},
 {"t": "pregunta", "pregunta": "¿Qué letra falta? NU_E", "opciones": ["P", "B", "F"], "correcta": 1,
  "voz": ["Ahora vos. nnn… u… hueco… e.", "¿Qué falta para decir NUBE?", "¡Falta *be*! NU-BE."]},
 {"t": "resumen", "items": [["ESCUCHAR", "FO-CA"], ["BOTA O PATO", "sentir la voz"], ["REVISAR", "leer lo escrito"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Escuchamos* cada sonido.", "Sentimos la *voz* en la garganta.", "Y *revisamos* leyendo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m7-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 7 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
