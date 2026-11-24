# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 4 · Los servicios de la ciudad: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (recorre la ciudad).
Genera tools/medio/clase/lecciones/medio-soc2-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'c343cc66-d180-4e2e-84b0-cc0a1bfcfb8b', 2: '0bc29532-3875-4b61-8f54-af582e6d6af1', 3: '39634c6a-fb5c-4464-b89e-6c793834f0b9', 4: '78501488-789e-4012-9239-9bf318813390'}
TIT = {1: 'Qué servicios tiene una ciudad', 2: 'Trabajadores y técnicas de cada servicio', 3: 'Normas que organizan los servicios', 4: 'Servicios en un pueblo y en el campo'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LOLA = {"nombre": "Lola", "emoji": "👧🎤"}

N1 = [
 {"t": "historia", "personaje": LOLA, "lugar": "🏙️", "lineas": ["Lola abre la canilla.", "Prende la luz.", "¿De dónde viene todo?"], "titulo": "LOS SERVICIOS", "sub": "de la ciudad",
  "voz": ["Lola abre la *canilla*.", "Prende la *luz*.", "¿De dónde viene todo eso?", "Hoy: *los servicios de la ciudad*."]},
 {"t": "matriz", "titulo": "SERVICIOS", "celdas": [{"cab": "AGUA 🚰", "txt": "sale de la canilla"}, {"cab": "LUZ 💡", "txt": "llega por cables"}, {"cab": "BASURA 🚛", "txt": "la juntan"}, {"cab": "HOSPITAL 🏥", "txt": "cuida la salud"}],
  "voz": ["La ciudad tiene muchos *servicios*.", "El *agua* sale de la canilla.", "La *luz* llega por cables.", "La *basura* la junta un camión.", "El *hospital* cuida la salud."]},
 {"t": "memoria", "titulo": "SERVICIOS", "items": ["AGUA", "LUZ", "GAS", "ESCUELA"], "falta": 2,
  "voz": ["Mirá los servicios.", "Se tapan… ¡y uno desapareció!", "¡Faltaba el *gas*!"]},
 {"t": "pregunta", "pregunta": "¿La escuela es un servicio?", "opciones": ["SÍ", "NO"], "correcta": 0,
  "voz": ["Ahora vos: ¿la escuela es un servicio?", "Pensá: ¿es para todos?", "¡*Sí*! Es para todos."]},
 {"t": "pasos", "titulo": "LA MAÑANA DE LOLA", "items": [{"txt": "Se lava: agua", "emoji": "🚰"}, {"txt": "Prende la luz", "emoji": "💡"}, {"txt": "Toma el colectivo", "emoji": "🚌"}, {"txt": "Llega a la escuela", "emoji": "🏫"}],
  "voz": ["¿Cuántos servicios usa Lola en una mañana?", "Se lava la cara: usa el *agua*.", "Prende la *luz* para vestirse.", "Toma el *colectivo* para viajar.", "Y llega a la *escuela*. ¡Cuatro servicios!"]},
 {"t": "consejo", "titulo": "CUIDALOS", "texto": "Apagá la luz y cerrá la canilla", "emoji": "💡",
  "voz": ["Truco: apagá la *luz* y cerrá la canilla."]},
 {"t": "resumen", "items": [["SERVICIO", "para vivir mejor"], ["EN CASA", "agua, luz, gas"], ["PARA TODOS", "hospital y escuela"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *servicio* nos ayuda a vivir mejor.", "En casa: agua, luz y *gas*.", "Para todos: hospital y *escuela*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Abuela Rosa", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "¡Se cortó la luz! 😮"}, {"yo": True, "txt": "¡Ya viene el electricista!"}], "titulo": "TRABAJADORES", "sub": "de los servicios",
  "voz": ["La abuela escribe: ¡se cortó la luz!", "Lola responde: ¡ya viene el *electricista*!", "Hoy: *trabajadores de los servicios*."]},
 {"t": "mazo", "titulo": "TRABAJOS DE LA CIUDAD", "items": [{"frente": "🚛", "dorso": "RECOLECTOR: BASURA", "emoji": "🚛"}, {"frente": "🔌", "dorso": "ELECTRICISTA: CABLES", "emoji": "🔌"}, {"frente": "🚌", "dorso": "CHOFER: COLECTIVO", "emoji": "🚌"}, {"frente": "🌡️", "dorso": "ENFERMERA: TERMÓMETRO", "emoji": "🌡️"}],
  "voz": ["El *recolector* junta la basura.", "El *electricista* arregla los cables.", "El *chofer* maneja el colectivo.", "La *enfermera* usa el termómetro."]},
 {"t": "pistas", "problema": "¿Quién trabaja de noche?", "pistas": ["Pasa con un camión", "Junta bolsas", "Deja la calle limpia"], "respuesta": "¡EL RECOLECTOR! 🚛",
  "voz": ["Adivinanza: ¿quién trabaja de *noche*?", "Pista uno: pasa con un camión.", "Pista dos: junta bolsas.", "Pista tres: deja la calle limpia.", "¡El *recolector*!"]},
 {"t": "pregunta", "pregunta": "¿Quién arregla la luz?", "opciones": ["EL ELECTRICISTA", "LA ENFERMERA"], "correcta": 0,
  "voz": ["Ahora vos: ¿quién arregla la luz?", "Pensá en los cables.", "¡El *electricista*!"]},
 {"t": "datoloco", "texto": "Muchos recolectores trabajan de noche para que la calle esté limpia", "emoji": "🌙",
  "voz": ["¿Sabías qué?", "Muchos recolectores trabajan de *noche*. ¡Calle limpia!"]},
 {"t": "consejo", "titulo": "AGRADECÉ", "texto": "Decí gracias a quien trabaja para todos", "emoji": "🙏",
  "voz": ["Truco: decí *gracias* a quien trabaja para todos."]},
 {"t": "resumen", "items": [["RECOLECTOR", "junta la basura"], ["ELECTRICISTA", "arregla la luz"], ["ENFERMERA", "cuida la salud"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *recolector* junta la basura.", "El *electricista* arregla la luz.", "La *enfermera* cuida la salud.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué pasa si todos sacan la basura a cualquier hora?", "segundos": 8, "respuesta": "¡La calle se ensucia!", "emoji": "🗑️", "titulo": "NORMAS", "sub": "de los servicios",
  "voz": ["Desafío: ¿y si sacan la basura a cualquier hora?", "¡La calle se *ensucia*!", "Hoy: *normas de los servicios*."]},
 {"t": "datoloco", "texto": "El semáforo tiene tres colores: rojo, amarillo y verde", "emoji": "🚦",
  "voz": ["¿Sabías qué?", "El *semáforo* nos dice cuándo cruzar."]},
 {"t": "versus", "titulo": "ROJO O VERDE", "a": {"txt": "ROJO", "emoji": "🔴", "datos": ["espero", "quieto"]}, "b": {"txt": "VERDE", "emoji": "🟢", "datos": ["cruzo", "con cuidado"]}, "gana": "empate", "veredicto": "¡Los dos nos cuidan!",
  "voz": ["Comparamos dos colores.", "*Rojo*: espero, quieto.", "*Verde*: cruzo, con cuidado.", "¡Los dos nos *cuidan*!"]},
 {"t": "quiz4", "pregunta": "¿Dónde esperamos el colectivo?", "opciones": ["EN LA PARADA", "EN LA PLAZA", "EN EL MEDIO DE LA CALLE", "EN CASA"], "correcta": 0,
  "voz": ["¿Dónde esperamos el *colectivo*?", "Pensá en el cartel.", "¡En la *parada*!"]},
 {"t": "pasos", "titulo": "CRUZAR LA CALLE", "items": [{"txt": "Voy con un adulto", "emoji": "🧑‍🧒"}, {"txt": "Busco la senda", "emoji": "🚸"}, {"txt": "Miro el semáforo", "emoji": "🚦"}, {"txt": "Cruzo con verde", "emoji": "🟢"}],
  "voz": ["Cruzamos la calle con Lola, paso a paso.", "Primero, de la mano de un *adulto*.", "Buscamos la *senda* peatonal: las rayas blancas.", "Miramos el *semáforo*.", "Con *verde*, cruzamos mirando a los dos lados."]},
 {"t": "consejo", "titulo": "POR LA SENDA", "texto": "Cruzá por las rayas blancas", "emoji": "🚸",
  "voz": ["Truco: cruzá por la *senda* peatonal, con un adulto."]},
 {"t": "resumen", "items": [["BASURA", "en su horario"], ["COLECTIVO", "en la parada"], ["SEMÁFORO", "verde: cruzo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *basura*, en su horario.", "El *colectivo*, en la parada.", "Con el *semáforo* en verde, cruzo.", CIERRE]},
]
N4 = [
 {"t": "historieta", "titulo": "LOLA VA AL CAMPO", "vinetas": [{"emojis": ["🏙️", "🚌"], "txt": "Sale de la ciudad"}, {"emojis": ["🌾", "🏡"], "txt": "Las casas están lejos"}, {"emojis": ["☀️", "🔋"], "txt": "¡Luz de panel solar!"}],
  "voz": ["Lola sale de la *ciudad*.", "En el *campo*, las casas están lejos.", "¡Hay luz de *panel solar*! Hoy: *ciudad y campo*."]},
 {"t": "comparar", "a": {"cab": "CIUDAD", "texto": "HOSPITAL CERCA", "emoji": "🏙️"}, "b": {"cab": "CAMPO", "texto": "HOSPITAL LEJOS", "emoji": "🌾"}, "signo": "↔", "def": "En el campo los servicios quedan lejos",
  "voz": ["Comparamos la ciudad y el campo.", "En la *ciudad*, el hospital queda cerca.", "En el *campo*, queda lejos.", "Allá buscan otras formas."]},
 {"t": "unir", "titulo": "EN EL CAMPO", "pares": [["AGUA", "pozo"], ["LUZ", "panel solar"], ["ESCUELA", "rural"]], "mezclar": True,
  "voz": ["Unimos cada servicio del campo.", "El *agua*: de un pozo.", "La *luz*: de un panel solar.", "La *escuela*: rural."]},
 {"t": "pregunta", "pregunta": "¿Todos tienen derecho a los servicios?", "opciones": ["SÍ", "NO"], "correcta": 0,
  "voz": ["Ahora vos: ¿todos tienen derecho a los servicios?", "Pensá en el campo.", "¡*Sí*! En la ciudad y en el campo."]},
 {"t": "datoloco", "texto": "En el campo, muchas casas usan paneles solares para tener luz", "emoji": "☀️",
  "voz": ["¿Sabías qué?", "En el campo, muchas casas tienen luz gracias al *sol*."]},
 {"t": "consejo", "titulo": "COMPARÁ", "texto": "¿Está cerca o lejos?", "emoji": "📍",
  "voz": ["Truco: para comparar, preguntá: ¿cerca o *lejos*?"]},
 {"t": "resumen", "items": [["CIUDAD", "servicios cerca"], ["CAMPO", "servicios lejos"], ["SOLUCIONES", "pozo y panel solar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la *ciudad*, los servicios están cerca.", "En el *campo*, lejos.", "Allá usan *pozos* y paneles solares.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m4-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 4 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
