# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 4 · Cuerpos para cada ambiente: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador con su lupa (viaja por la Argentina).
Genera tools/medio/clase/lecciones/medio-nat2-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '42c624c5-fcec-44ca-b91a-8baecfdd5dd7', 2: '2bb7e82e-1810-47c4-bd4e-4c89650b5561', 3: 'c5c0ac10-cb47-4050-92bf-9a37bf3444d4', 4: 'df572644-4cfd-4d3b-8329-b6c873052c06'}
TIT = {1: 'Patas, picos y pelajes', 2: 'Plantas de ambientes secos y húmedos', 3: 'Cuerpos para moverse', 4: 'Comparo ambientes argentinos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🔍", "lineas": ["Tomi mira un pato con su lupa.", "¡Sus patas son raras!", "¿Para qué le sirven?"], "titulo": "CUERPOS", "sub": "patas, picos y pelajes",
  "voz": ["Tomi mira un *pato* con su lupa.", "¡Sus patas son raras!", "¿Para qué le sirven?", "Hoy: *patas, picos y pelajes*."]},
 {"t": "zoom", "niveles": [{"emoji": "🦆", "txt": "UN PATO"}, {"emoji": "🦶", "txt": "SUS PATAS"}, {"emoji": "🏊", "txt": "¡PIEL PARA NADAR!"}],
  "voz": ["Miramos de cerca un *pato*.", "Más cerca: sus *patas*.", "¡Tienen piel entre los dedos para *nadar*!"]},
 {"t": "unir", "titulo": "¿PARA QUÉ SIRVE?", "pares": [["PATAS DEL PATO", "nadar"], ["PICO DEL HORNERO", "comer bichitos"], ["LANA DEL GUANACO", "abrigar"]], "mezclar": True,
  "voz": ["Unimos cada parte con lo que hace.", "Patas del pato: para *nadar*.", "Pico del hornero: para *comer bichitos*.", "Lana del guanaco: para *abrigar*."]},
 {"t": "pregunta", "pregunta": "¿Para qué sirve la lana del guanaco?", "opciones": ["PARA EL FRÍO", "PARA NADAR"], "correcta": 0,
  "voz": ["Ahora vos: ¿para qué sirve la lana?", "Pensá dónde vive el guanaco.", "¡Para el *frío*!"]},
 {"t": "consejo", "titulo": "PREGUNTÁ ¿PARA QUÉ?", "texto": "Cada parte del cuerpo sirve para algo", "emoji": "❓",
  "voz": ["Truco: cada parte del cuerpo *sirve para algo*."]},
 {"t": "resumen", "items": [["PATAS", "nadar o correr"], ["PICOS", "comer"], ["PELAJE", "abrigar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *patas* sirven para nadar o correr.", "Los *picos*, para comer.", "El *pelaje*, para abrigar.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "VIAJE", "titular": "¡Una planta con espinas en el desierto!", "bajada": "Y otra que flota en el río", "emoji": "🌵", "titulo": "PLANTAS", "sub": "secas y húmedas",
  "voz": ["¡Noticia: una planta con *espinas* en el desierto!", "Y otra que *flota* en el río.", "Hoy: *plantas de lugares secos y húmedos*."]},
 {"t": "versus", "titulo": "SECO CONTRA HÚMEDO", "a": {"txt": "CACTUS", "emoji": "🌵", "datos": ["tallo grueso", "espinas"]}, "b": {"txt": "HOJAS DE SELVA", "emoji": "🌿", "datos": ["hojas grandes", "mucha agua"]}, "gana": "empate", "veredicto": "¡Cada una sirve para su lugar!",
  "voz": ["Comparamos dos plantas.", "El *cactus*: tallo grueso y espinas, para el desierto.", "Las plantas de *selva*: hojas grandes, con mucha agua.", "¡Cada una sirve para su lugar!"]},
 {"t": "pistas", "problema": "¿Qué planta es?", "pistas": ["Vive en el río", "Tiene hojas verdes", "Flota en el agua"], "respuesta": "EL CAMALOTE",
  "voz": ["Adivinanza: ¿qué planta es?", "Pista uno: vive en el río.", "Pista dos: tiene hojas verdes.", "Pista tres: *flota* en el agua.", "¡El *camalote*!"]},
 {"t": "pregunta", "pregunta": "¿Qué planta guarda agua en su tallo?", "opciones": ["EL CACTUS", "EL CAMALOTE"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué planta guarda agua?", "Pensá en el desierto.", "¡El *cactus*!"]},
 {"t": "consejo", "titulo": "MIRÁ EL LUGAR", "texto": "Cada planta es como el lugar donde vive", "emoji": "🗺️",
  "voz": ["Truco: cada planta se parece al *lugar* donde vive."]},
 {"t": "resumen", "items": [["SECO", "cactus: guarda agua"], ["HÚMEDO", "hojas grandes"], ["RÍO", "camalote: flota"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En lo *seco*: el cactus guarda agua.", "En lo *húmedo*: hojas grandes.", "En el *río*: el camalote flota.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Cómo se mueve un animal sin patas?", "segundos": 8, "respuesta": "¡Repta, como la víbora!", "emoji": "🐍", "titulo": "MOVERSE", "sub": "cada uno a su manera",
  "voz": ["Desafío: ¿cómo se mueve un animal *sin patas*?", "¡*Repta*, como la víbora!", "Hoy: *cuerpos para moverse*."]},
 {"t": "personaje", "personaje": {"nombre": "Rana Rita", "emoji": "🐸"}, "lineas": [{"txt": "¡Hola! Yo salto muy lejos.", "animo": "feliz"}, {"txt": "Mis patas de atrás son largas y fuertes.", "animo": "ojo"}, {"txt": "¡Por eso salto tan bien!", "animo": "feliz"}],
  "voz": ["¡Hola! Yo *salto* muy lejos.", "Mis patas de atrás son *largas* y fuertes.", "¡Por eso salto tan bien!"]},
 {"t": "escape", "titulo": "LA PUERTA DEL ZOOLÓGICO", "candados": [{"p": "El pez se mueve…", "r": "NADANDO"}, {"p": "El pájaro se mueve…", "r": "VOLANDO"}, {"p": "La víbora se mueve…", "r": "REPTANDO"}],
  "voz": ["¡Para salir del zoológico, abrimos los candados!", "El pez: *nadando*.", "El pájaro: *volando*.", "La víbora: *reptando*.", "¡Escapamos!"]},
 {"t": "clasificar", "cajas": [{"cab": "AGUA", "emoji": "🌊"}, {"cab": "AIRE", "emoji": "☁️"}, {"cab": "TIERRA", "emoji": "🌍"}], "fichas": [{"txt": "PEZ", "caja": 0}, {"txt": "PÁJARO", "caja": 1}, {"txt": "ÑANDÚ", "caja": 2}, {"txt": "VÍBORA", "caja": 2}],
  "voz": ["Separamos según dónde se mueven.", "El pez, en el *agua*.", "El pájaro, en el *aire*.", "El ñandú y la víbora, en la *tierra*."]},
 {"t": "consejo", "titulo": "MIRÁ EL CUERPO", "texto": "Las partes del cuerpo dicen cómo se mueve", "emoji": "🔍",
  "voz": ["Truco: las partes del cuerpo dicen *cómo se mueve*."]},
 {"t": "resumen", "items": [["NADAR", "aletas"], ["VOLAR", "alas"], ["CORRER Y SALTAR", "patas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Para *nadar*: aletas.", "Para *volar*: alas.", "Para *correr y saltar*: patas.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Sofi", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "¿Adónde viajás, Tomi? 🗺️"}, {"yo": True, "txt": "¡Por toda la Argentina!"}], "titulo": "AMBIENTES", "sub": "de la Argentina",
  "voz": ["Sofi pregunta: ¿adónde viajás, Tomi?", "Tomi responde: ¡por toda la Argentina!", "Hoy: *ambientes argentinos*."]},
 {"t": "documental", "emojis": ["🌳", "🌊", "🏔️"], "lugar": "🇦🇷", "rotulos": [{"txt": "SELVA", "sub": "yaguareté y tucán"}, {"txt": "MAR", "sub": "pingüino y lobo marino"}, {"txt": "MONTAÑA", "sub": "guanaco y cóndor"}],
  "voz": ["En la *selva* viven el yaguareté y el tucán.", "En el *mar*, el pingüino y el lobo marino.", "En la *montaña*, el guanaco y el cóndor."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Perdido", "emoji": "🧭"}, "preguntas": [{"p": "¿Dónde vive el pingüino?", "r": "EN EL MAR"}, {"p": "¿Dónde vive el tucán?", "r": "EN LA SELVA"}],
  "voz": ["¡Apareció el *Monstruo Perdido*! No sabe dónde vive cada animal.", "Lo ayudamos.", "El pingüino: en el *mar*.", "¡El tucán: en la *selva*! ¡Ganamos!"]},
 {"t": "pregunta", "pregunta": "¿Dónde hace más frío?", "opciones": ["EN LA MONTAÑA", "EN LA SELVA"], "correcta": 0,
  "voz": ["Ahora vos: ¿dónde hace más frío?", "Pensá en la lana del guanaco.", "¡En la *montaña*!"]},
 {"t": "consejo", "titulo": "CALOR O FRÍO", "texto": "Pensá cómo es el clima de cada lugar", "emoji": "🌡️",
  "voz": ["Truco: ¿el lugar es de *calor* o de *frío*?"]},
 {"t": "resumen", "items": [["SELVA", "calor y lluvia"], ["MAR", "agua salada"], ["MONTAÑA", "frío"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *selva*: calor y lluvia.", "El *mar*: agua salada.", "La *montaña*: frío.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m4-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 4 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
