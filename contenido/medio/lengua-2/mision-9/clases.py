# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 9 · Poemas de Rafael Pombo («El renacuajo paseador», dominio público): las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Metáfora: el cuaderno viajero de Sofi con un poema.
Genera tools/medio/clase/lecciones/medio-leng2-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'a335ea10-574f-4101-8307-0c4fcbb0a90a', 2: '5d10b497-5392-4e31-95a4-26da3bff7d95', 3: '0d91c36c-882b-4b6e-9e3e-8c67d3eb6fc8', 4: '34347eb5-5c72-4931-b59f-34f91875c175'}
TIT = {1: 'Escuchar El renacuajo paseador', 2: 'Leer en voz alta con ritmo', 3: 'Imaginar y dibujar los personajes', 4: 'Inventar una estrofa'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."

N1 = [
 {"t": "historieta", "titulo": "EL RENACUAJO PASEADOR", "vinetas": [{"emojis": ["🐸", "🎩"], "txt": "Rinrín sale muy elegante", "quien": "Narrador"}, {"emojis": ["🐸", "🗣️"], "txt": "¡Muchacho, no salgas!", "quien": "Mamá"}, {"emojis": ["🐭", "🐱"], "txt": "Visita a doña Ratona y llegan los gatos"}, {"emojis": ["🦆", "😮"], "txt": "Al final, un pato se lo traga"}],
  "voz": ["Rinrín Renacuajo sale de paseo muy elegante.", "Su mamá le grita: ¡Muchacho, no salgas!", "Visita a doña Ratona… ¡y llegan los gatos!", "Un pato se lo traga. Hoy: *el renacuajo paseador*."]},
 {"t": "definicion", "palabra": "Poema", "texto": "Texto escrito en versos, con música", "emoji": "🎵",
  "voz": ["Esta historia es un *poema*.", "La escribió *Rafael Pombo*, un poeta de Colombia."]},
 {"t": "memoria", "titulo": "LOS PERSONAJES", "items": ["RINRÍN", "MAMÁ RANA", "EL RATÓN", "DOÑA RATONA", "EL PATO"], "falta": 3,
  "voz": ["Mirá los personajes del poema.", "Se tapan… ¡y uno desapareció!", "¡Faltaba *doña Ratona*!"]},
 {"t": "vof", "afirmacion": "Rinrín hizo caso a su mamá", "emoji": "🐸", "verdadero": False, "explicacion": "Salió igual de paseo",
  "voz": ["¿Verdadero o falso? Rinrín hizo caso a su mamá.", "Acordate del poema…", "¡*Falso*! Salió igual de paseo."]},
 {"t": "consejo", "titulo": "ESCUCHÁ LA MÚSICA", "texto": "Los poemas suenan como una canción", "emoji": "🎶",
  "voz": ["Truco: escuchá la *música* del poema."]},
 {"t": "resumen", "items": [["AUTOR", "Rafael Pombo"], ["POEMA", "texto en versos"], ["RINRÍN", "no hizo caso"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El autor es *Rafael Pombo*.", "Un *poema* es un texto en versos.", "*Rinrín* no hizo caso a su mamá.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué palabra rima con MODA?", "segundos": 8, "respuesta": "¡BODA!", "emoji": "🎵", "titulo": "LEER", "sub": "con ritmo",
  "voz": ["Desafío: ¿qué palabra rima con moda?", "¡*Boda*! Terminan igual.", "Hoy: *leer en voz alta con ritmo*."]},
 {"t": "pizarra", "titulo": "LA PRIMERA ESTROFA", "lineas": [{"txt": "El hijo de Rana, Rinrín Renacuajo,", "marca": "subraya"}, {"txt": "salió esta mañana muy tieso y muy majo,", "marca": "subraya", "color": "coral"}, {"txt": "con pantalón corto, corbata a la moda,", "marca": "subraya", "color": "verde"}, {"txt": "sombrero encintado y chupa de boda.", "marca": "subraya", "color": "azul"}],
  "voz": ["El hijo de Rana, Rinrín Renacuajo,", "salió esta mañana muy tieso y muy majo,", "con pantalón corto, corbata a la moda,", "sombrero encintado y chupa de boda."]},
 {"t": "definicion", "palabra": "Rima", "texto": "Palabras que terminan igual", "emoji": "🔔",
  "voz": ["*Renacuajo* y *majo* terminan igual: riman.", "*Moda* y *boda* también riman."]},
 {"t": "contrarreloj", "titulo": "¿RIMAN?", "segundos": 20, "items": [{"p": "GATO · PATO", "r": "SÍ"}, {"p": "SOL · LUNA", "r": "NO"}, {"p": "RATÓN · BOTÓN", "r": "SÍ"}],
  "voz": ["¡Ronda rápida! ¿Riman o no?", "Gato y pato: ¡*sí*!", "Sol y luna: *no*.", "Ratón y botón: ¡*sí*!"]},
 {"t": "consejo", "titulo": "PAUSA AL FINAL", "texto": "Hacé una pausa en cada verso", "emoji": "⏸️",
  "voz": ["Truco: hacé una *pausa* al final de cada verso."]},
 {"t": "resumen", "items": [["VERSO", "cada renglón"], ["ESTROFA", "grupo de versos"], ["RIMA", "finales iguales"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cada renglón es un *verso*.", "Un grupo de versos es una *estrofa*.", "La *rima*: finales que suenan igual.", CIERRE]},
]
N3 = [
 {"t": "historia", "personaje": {"nombre": "Sofi", "emoji": "👧"}, "lugar": "🖍️", "lineas": ["Sofi lee el poema otra vez.", "Quiere dibujar a Rinrín.", "¿Cómo será?"], "titulo": "IMAGINAR", "sub": "y dibujar",
  "voz": ["Sofi lee el poema otra vez.", "Quiere *dibujar* a Rinrín.", "¿Cómo será?", "Hoy: *imaginar y dibujar los personajes*."]},
 {"t": "pistas", "problema": "¿Cómo se viste Rinrín?", "pistas": ["Pantalón corto", "Corbata a la moda", "Sombrero con cinta"], "respuesta": "¡Muy elegante! 🎩",
  "voz": ["¿Cómo se viste Rinrín? Busquemos en el poema.", "Lleva *pantalón corto*.", "Una *corbata* a la moda.", "Un *sombrero* con cinta.", "¡Muy elegante!"]},
 {"t": "definicion", "palabra": "Chupa", "texto": "Una chaqueta elegante", "emoji": "🧥",
  "voz": ["El poema dice *chupa de boda*.", "Una chupa es una *chaqueta* elegante."]},
 {"t": "vof", "afirmacion": "Rinrín lleva pantalón largo", "emoji": "👖", "verdadero": False, "explicacion": "El poema dice pantalón corto",
  "voz": ["¿Verdadero o falso? Rinrín lleva pantalón largo.", "Volvé al poema…", "¡*Falso*! Dice pantalón *corto*."]},
 {"t": "consejo", "titulo": "VOLVÉ AL POEMA", "texto": "Los detalles están en los versos", "emoji": "🔎",
  "voz": ["Truco: los detalles para dibujar están en los *versos*."]},
 {"t": "resumen", "items": [["LEER", "cómo es"], ["IMAGINAR", "al personaje"], ["DIBUJAR", "con los detalles"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Leemos* cómo es cada personaje.", "Lo *imaginamos*.", "Lo *dibujamos* con los detalles.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Podemos inventar un poema? 🐱"}, {"yo": True, "txt": "¡Sí! Como el de Rinrín"}], "titulo": "INVENTAR", "sub": "una estrofa",
  "voz": ["Tomi pregunta: ¿podemos inventar un poema?", "Sofi responde: ¡sí, como el de Rinrín!", "Hoy: *inventar una estrofa*."]},
 {"t": "pasos", "titulo": "CÓMO INVENTO", "items": [{"txt": "Elijo un personaje", "emoji": "🐱"}, {"txt": "Busco dos palabras que rimen", "emoji": "🔔"}, {"txt": "Escribo los versos", "emoji": "✏️"}],
  "voz": ["¿Cómo inventamos una estrofa?", "Elegimos un *personaje*.", "Buscamos dos palabras que *rimen*.", "Escribimos los *versos*."]},
 {"t": "fichas", "consigna": "Armá el verso de Sofi", "fichas": ["La", "hija", "de", "Gata,", "Mimí", "Gatita"], "desorden": [4, 0, 5, 2, 1, 3], "traduccion": "Como «El hijo de Rana, Rinrín Renacuajo»",
  "voz": ["Armamos el verso de Sofi con las fichas.", "La hija de Gata, *Mimí Gatita*.", "¡Igual que el comienzo de Rinrín!"]},
 {"t": "tipeo", "titulo": "BUSCÁ LA RIMA", "items": [{"p": "Mimí Gatita salió muy…", "r": "BONITA"}, {"p": "El perro Pancho salió a pasear, con su corbata se fue a…", "r": "JUGAR"}],
  "voz": ["Mimí Gatita salió muy… ¡*bonita*!", "El perro Pancho salió a pasear… ¡se fue a *jugar*!"]},
 {"t": "consejo", "titulo": "PRIMERO LA RIMA", "texto": "Elegí antes las dos palabras que riman", "emoji": "💡",
  "voz": ["Truco: elegí primero las dos palabras que *riman*."]},
 {"t": "resumen", "items": [["FORMA", "como el poema"], ["PERSONAJE", "uno nuevo"], ["RIMA", "finales iguales"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Copiamos la *forma* del poema.", "Inventamos un *personaje* nuevo.", "Buscamos la *rima*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m9-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 9 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
