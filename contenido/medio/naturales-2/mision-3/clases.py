# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 3 · De la flor al fruto: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador con su lupa (en la huerta de la escuela).
Genera tools/medio/clase/lecciones/medio-nat2-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '12904dff-a67e-4de5-9173-e2af7efb6d6a', 2: '261c94f2-418c-427c-b9fe-7f2872632bae', 3: '59d877ec-419f-4504-b809-c13457098ba2', 4: 'd206ac25-0e8b-47b4-a6d8-ae5e4dc8eb32'}
TIT = {1: 'Flores y frutos', 2: 'Cómo viajan las semillas', 3: 'Plantas que nacen sin semillas', 4: 'Armo mi semillero'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🌼", "lineas": ["Tomi mira la huerta de la escuela.", "La planta de tomate tiene flores.", "Días después… ¡hay tomates!"], "titulo": "DE LA FLOR", "sub": "al fruto",
  "voz": ["Tomi mira la *huerta* de la escuela.", "La planta de tomate tiene *flores* amarillas.", "Días después… ¡hay *tomates*!", "Hoy: *de la flor al fruto*."]},
 {"t": "ciclo", "titulo": "EL CICLO DE LA PLANTA", "items": ["SEMILLA 🌰", "PLANTA 🌱", "FLOR 🌼", "FRUTO 🍅"],
  "voz": ["Las plantas tienen un *ciclo*.", "Todo empieza con una *semilla*.", "Crece una *planta*.", "La planta da *flores*.", "¡Y la flor se convierte en *fruto*, con semillas adentro!"]},
 {"t": "definicion", "palabra": "Fruto", "texto": "Sale de la flor y guarda las semillas", "emoji": "🍎",
  "voz": ["El *fruto* sale de la flor.", "Adentro guarda las *semillas*."]},
 {"t": "quiz4", "pregunta": "¿Cuál es un fruto?", "opciones": ["LA HOJA", "EL TOMATE", "LA RAÍZ", "EL TALLO"], "correcta": 1,
  "voz": ["¿Cuál de estos es un *fruto*?", "Pensá: ¿cuál tiene semillas adentro?", "¡El *tomate*!"]},
 {"t": "consejo", "titulo": "MIRÁ ADENTRO", "texto": "Si tiene semillas adentro, es un fruto", "emoji": "🔍",
  "voz": ["Truco: si tiene *semillas* adentro, es un fruto."]},
 {"t": "resumen", "items": [["FLOR", "primero"], ["FRUTO", "sale de la flor"], ["SEMILLAS", "adentro del fruto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero está la *flor*.", "La flor se convierte en *fruto*.", "Adentro del fruto hay *semillas*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "HUERTA", "titular": "¡Las semillas se van de viaje!", "bajada": "¿Cómo viajan?", "emoji": "🌬️", "titulo": "SEMILLAS", "sub": "viajeras",
  "voz": ["¡Noticia en la huerta: las semillas se van de *viaje*!", "¿Cómo viajan?", "Hoy: *cómo viajan las semillas*."]},
 {"t": "matriz", "titulo": "CÓMO VIAJAN", "celdas": [{"cab": "VIENTO 🌬️", "txt": "El panadero vuela"}, {"cab": "ANIMALES 🐦", "txt": "Comen frutos y las llevan"}, {"cab": "PELO 🐕", "txt": "Se pegan con pinches"}, {"cab": "AGUA 🌊", "txt": "El coco flota"}],
  "voz": ["Las semillas viajan de muchas formas.", "Con el *viento*: el panadero vuela.", "Con los *animales*: comen frutos y las llevan.", "Pegadas al *pelo*, con pinches.", "Y por el *agua*: ¡el coco flota!"]},
 {"t": "mazo", "titulo": "SEMILLAS VIAJERAS", "items": [{"frente": "🌬️ PANADERO", "dorso": "VIENTO", "emoji": "🌬️"}, {"frente": "🦔 CON PINCHES", "dorso": "ANIMALES", "emoji": "🐕"}, {"frente": "🥥 COCO", "dorso": "AGUA", "emoji": "🌊"}],
  "voz": ["El *panadero* viaja con el viento.", "La semilla con *pinches* viaja en los animales.", "El *coco* viaja por el agua."]},
 {"t": "pregunta", "pregunta": "¿Cómo viaja el panadero?", "opciones": ["CON EL VIENTO", "CON EL AGUA"], "correcta": 0,
  "voz": ["Ahora vos: ¿cómo viaja el panadero?", "Pensá: es muy liviano.", "¡Con el *viento*!"]},
 {"t": "consejo", "titulo": "MIRÁ LA FORMA", "texto": "La forma te dice cómo viaja", "emoji": "🔎",
  "voz": ["Truco: la *forma* de la semilla te dice cómo viaja."]},
 {"t": "resumen", "items": [["VIENTO", "semillas livianas"], ["ANIMALES", "comen o se pegan"], ["AGUA", "semillas que flotan"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Con el *viento* viajan las livianas.", "Los *animales* las comen o las llevan pegadas.", "Por el *agua* viajan las que flotan.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Puede nacer una planta sin semilla?", "segundos": 8, "respuesta": "¡Sí! De un gajo o una papa", "emoji": "🥔", "titulo": "SIN SEMILLAS", "sub": "plantas que nacen distinto",
  "voz": ["Desafío: ¿puede nacer una planta *sin semilla*?", "¡Sí! De un *gajo* o de una *papa*.", "Hoy: *plantas que nacen sin semillas*."]},
 {"t": "experimento", "titulo": "UN GAJO EN AGUA", "variable": "EL AGUA", "a": {"cab": "GAJO SECO", "emojis": ["🌿", "🏜️"], "txt": "Sin agua", "res": "SE SECA"}, "b": {"cab": "GAJO EN AGUA", "emojis": ["🌿", "💧"], "txt": "En un vaso con agua", "res": "¡LE SALEN RAÍCES!"},
  "voz": ["Probamos con dos gajos.", "El gajo *sin agua* se seca.", "El gajo *en agua*: ¡le salen raíces!"]},
 {"t": "definicion", "palabra": "Gajo", "texto": "Pedacito de tallo que echa raíces", "emoji": "🌿",
  "voz": ["Un *gajo* es un pedacito de tallo.", "Con agua, echa *raíces* y nace una planta nueva."]},
 {"t": "vof", "afirmacion": "Todas las plantas nacen de semillas", "emoji": "🌱", "verdadero": False, "explicacion": "Algunas nacen de gajos o de papas",
  "voz": ["¿Verdadero o falso? Todas las plantas nacen de semillas.", "Acordate del gajo…", "¡*Falso*! Algunas nacen de gajos o papas."]},
 {"t": "consejo", "titulo": "PACIENCIA", "texto": "Las raíces tardan varios días", "emoji": "⏳",
  "voz": ["Truco: *paciencia*, las raíces tardan varios días."]},
 {"t": "resumen", "items": [["GAJO", "pedacito de tallo"], ["RAÍCES", "le salen en agua"], ["PAPA", "echa brotes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *gajo* es un pedacito de tallo.", "En agua le salen *raíces*.", "La *papa* vieja echa brotes.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Seño Ana", "emoji": "👩‍🏫"}, "mensajes": [{"yo": False, "txt": "Mañana armamos un semillero 🌱"}, {"yo": True, "txt": "¡Traigo porotos y un vaso!"}], "titulo": "MI SEMILLERO", "sub": "armo y observo",
  "voz": ["La seño escribe: mañana armamos un *semillero*.", "Tomi responde: ¡traigo porotos y un vaso!", "Hoy: *armo mi semillero*."]},
 {"t": "pasos", "titulo": "CÓMO LO ARMO", "items": [{"txt": "Pongo tierra en el vaso", "emoji": "🪴"}, {"txt": "Pongo las semillas", "emoji": "🌰"}, {"txt": "Riego un poco", "emoji": "💧"}, {"txt": "Lo dejo con luz", "emoji": "☀️"}],
  "voz": ["¿Cómo armamos el semillero?", "Ponemos *tierra* en un vaso.", "Ponemos las *semillas*.", "Regamos *un poco*.", "Y lo dejamos con *luz*."]},
 {"t": "linea", "titulo": "LO QUE ANOTÓ TOMI", "eventos": [{"fecha": "DÍA 1", "txt": "Siembro", "emoji": "🌰"}, {"fecha": "DÍA 5", "txt": "Sale un brote", "emoji": "🌱"}, {"fecha": "DÍA 10", "txt": "Tiene hojitas", "emoji": "🌿"}],
  "voz": ["Tomi anota. *Día uno*: siembra.", "*Día cinco*: sale un brote.", "*Día diez*: ¡tiene hojitas!"]},
 {"t": "memoria", "titulo": "LO QUE NECESITA", "items": ["TIERRA", "AGUA", "LUZ", "SEMILLA"], "falta": 2,
  "voz": ["Mirá lo que necesita la planta.", "Se tapan… ¡y una desapareció!", "¡Faltaba la *luz*!"]},
 {"t": "consejo", "titulo": "ANOTÁ TODO", "texto": "Un científico anota lo que observa", "emoji": "📝",
  "voz": ["Truco: un científico *anota* lo que observa cada día."]},
 {"t": "resumen", "items": [["MATERIALES", "vaso, tierra, semillas"], ["PASOS", "tierra, semilla, agua, luz"], ["ANOTAR", "cada día"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *materiales*: vaso, tierra y semillas.", "Los *pasos*: tierra, semilla, agua y luz.", "Y *anotamos* lo que pasa cada día.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m3-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 3 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
