# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 5 · Calentar y enfriar: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (en la cocina, siempre con un adulto).
Genera tools/medio/clase/lecciones/medio-nat2-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '7639ad94-e71f-4057-83a5-fd142218f507', 2: '3381a430-db9e-451e-90f5-db8c8d08f368', 3: '1d61c4c2-4295-45c8-aaed-80610bf68e6c', 4: '6e8e091d-0e8a-4ff2-80a0-89b547187486'}
TIT = {1: 'Qué pasa al calentar', 2: 'Derretir y solidificar', 3: 'Evaporar y condensar', 4: 'Qué cambia al cocinar'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "☀️", "lineas": ["Tomi dejó un chocolate al sol.", "¡Se puso blandito!", "¿Qué pasó?"], "titulo": "CALENTAR", "sub": "qué pasa con el calor",
  "voz": ["Tomi dejó un *chocolate* al sol.", "¡Se puso *blandito*!", "¿Qué pasó?", "Hoy: *qué pasa al calentar*."]},
 {"t": "experimento", "titulo": "DOS CHOCOLATES", "variable": "EL CALOR", "a": {"cab": "A LA SOMBRA", "emojis": ["🍫", "🌳"], "txt": "Sin calor", "res": "QUEDA DURO"}, "b": {"cab": "AL SOL", "emojis": ["🍫", "☀️"], "txt": "Con calor", "res": "¡SE ABLANDA!"},
  "voz": ["Probamos con dos chocolates.", "A la *sombra*: queda duro.", "Al *sol*: ¡se ablanda!"]},
 {"t": "medidor", "titulo": "EL TERMÓMETRO", "tipo": "termometro", "min": 0, "max": 50, "valor": 35, "unidad": "°C", "nota": "Día de mucho calor",
  "voz": ["Esto es un *termómetro*.", "Mide si algo está frío o caliente.", "¡Hoy marca mucho calor!"]},
 {"t": "pregunta", "pregunta": "¿Qué le pasa a la manteca en la sartén caliente?", "opciones": ["SE DERRITE", "SE CONGELA"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué le pasa a la manteca?", "Pensá en el calor.", "¡Se *derrite*!"]},
 {"t": "consejo", "titulo": "CON UN ADULTO", "texto": "Las cosas calientes queman", "emoji": "⚠️",
  "voz": ["Truco: con cosas calientes, siempre con un *adulto*."]},
 {"t": "resumen", "items": [["CALENTAR", "dar calor"], ["CAMBIA", "se ablanda, se derrite"], ["TERMÓMETRO", "mide frío y calor"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Calentar* es dar calor.", "Con calor, las cosas *cambian*.", "El *termómetro* mide frío y calor.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué pasa con el helado en el verano?", "segundos": 8, "respuesta": "¡Se derrite!", "emoji": "🍦", "titulo": "DERRETIR", "sub": "y solidificar",
  "voz": ["Desafío: ¿qué pasa con el helado en verano?", "¡Se *derrite*!", "Hoy: *derretir y solidificar*."]},
 {"t": "ciclo", "titulo": "IDA Y VUELTA", "items": ["HIELO 🧊", "+ CALOR 🔥", "AGUA 💧", "+ FRÍO ❄️"],
  "voz": ["El agua va y vuelve.", "Empezamos con *hielo*.", "Con *calor*, se derrite.", "Se hace *agua*.", "Con *frío*, ¡vuelve a ser hielo!"]},
 {"t": "quiz4", "pregunta": "¿Qué hace que el agua se haga hielo?", "opciones": ["EL SOL", "EL FRÍO", "EL VIENTO", "LA LUZ"], "correcta": 1,
  "voz": ["¿Qué hace que el agua se haga *hielo*?", "Pensá en el congelador.", "¡El *frío*!"]},
 {"t": "definicion", "palabra": "Sólido y líquido", "texto": "Sólido: tiene forma. Líquido: se derrama", "emoji": "🧊",
  "voz": ["El hielo es *sólido*: tiene forma.", "El agua es *líquido*: se derrama."]},
 {"t": "consejo", "titulo": "CALOR O FRÍO", "texto": "Calor derrite. Frío solidifica", "emoji": "🌡️",
  "voz": ["Truco: el *calor* derrite y el *frío* solidifica."]},
 {"t": "resumen", "items": [["DERRETIR", "sólido a líquido"], ["SOLIDIFICAR", "líquido a sólido"], ["IDA Y VUELTA", "se puede repetir"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Derretir*: de sólido a líquido.", "*Solidificar*: de líquido a sólido.", "¡Es *ida y vuelta*!", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "COCINA", "titular": "¡Gotitas misteriosas en la tapa!", "bajada": "Tomi investiga la olla", "emoji": "🫕", "titulo": "EVAPORAR", "sub": "y condensar",
  "voz": ["¡Noticia: gotitas *misteriosas* en la tapa de la olla!", "Tomi investiga.", "Hoy: *evaporar y condensar*."]},
 {"t": "transforma", "titulo": "EL VIAJE DEL AGUA", "pasos": [{"txt": "AGUA EN LA OLLA 💧", "nota": "líquido"}, {"txt": "VAPOR QUE SUBE ♨️", "nota": "con calor: se evapora"}, {"txt": "GOTITAS EN LA TAPA 💦", "nota": "con frío: se condensa"}],
  "voz": ["El agua está en la olla.", "Con calor, se *evapora*: sube el vapor.", "En la tapa fría, se *condensa*: ¡gotitas!"]},
 {"t": "vof", "afirmacion": "El agua del charco desaparece para siempre", "emoji": "☀️", "verdadero": False, "explicacion": "Se hace vapor y sube",
  "voz": ["¿Verdadero o falso? El charco desaparece para siempre.", "Pensá en el vapor…", "¡*Falso*! Se hace vapor y sube."]},
 {"t": "pregunta", "pregunta": "¿Por qué se empaña el espejo del baño?", "opciones": ["EL VAPOR SE CONDENSA", "SE ENSUCIA"], "correcta": 0,
  "voz": ["Ahora vos: ¿por qué se empaña el espejo?", "Pensá en la ducha caliente.", "¡El vapor se *condensa*!"]},
 {"t": "consejo", "titulo": "CUIDADO", "texto": "El vapor también quema", "emoji": "⚠️",
  "voz": ["Truco: el *vapor* también quema. ¡De lejos!"]},
 {"t": "resumen", "items": [["EVAPORAR", "agua a vapor"], ["CONDENSAR", "vapor a gotitas"], ["VAPOR", "agua que no vemos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Evaporar*: el agua se hace vapor.", "*Condensar*: el vapor se hace gotitas.", "El *vapor* es agua que no vemos.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Abuela", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "¿Me ayudás a cocinar? 🍳"}, {"yo": True, "txt": "¡Sí! Y miro qué cambia"}], "titulo": "COCINAR", "sub": "qué cambia",
  "voz": ["La abuela pregunta: ¿me ayudás a cocinar?", "Tomi responde: ¡sí, y miro qué cambia!", "Hoy: *qué cambia al cocinar*."]},
 {"t": "antesdespues", "antes": {"cab": "CRUDO", "emoji": "🥚", "texto": "Huevo líquido"}, "despues": {"cab": "COCIDO", "emoji": "🍳", "texto": "Huevo duro"},
  "voz": ["*Antes*: el huevo crudo es líquido.", "*Después* de cocinarlo: ¡se pone duro y no vuelve atrás!"]},
 {"t": "mazo", "titulo": "ANTES Y DESPUÉS", "items": [{"frente": "🍞 PAN", "dorso": "TOSTADA", "emoji": "🍞"}, {"frente": "🥔 PAPA DURA", "dorso": "PAPA BLANDA", "emoji": "🥔"}, {"frente": "🧊 HIELO", "dorso": "AGUA (¡VUELVE!)", "emoji": "🧊"}],
  "voz": ["El *pan* se hace tostada.", "La *papa* dura se pone blanda.", "El *hielo* se hace agua… ¡y ese sí vuelve!"]},
 {"t": "pregunta", "pregunta": "¿Qué cambio NO vuelve atrás?", "opciones": ["COCINAR UN HUEVO", "DERRETIR HIELO"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué cambio no vuelve atrás?", "Pensá en el huevo duro.", "¡*Cocinar un huevo*!"]},
 {"t": "consejo", "titulo": "COMPARÁ", "texto": "Mirá el alimento antes y después", "emoji": "👀",
  "voz": ["Truco: mirá el alimento *antes* y *después*."]},
 {"t": "resumen", "items": [["CRUDO", "antes de cocinar"], ["COCIDO", "después del calor"], ["NO VUELVE", "huevo, tostada"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Crudo*: antes de cocinar.", "*Cocido*: después del calor.", "Algunos cambios *no vuelven*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m5-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 5 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
