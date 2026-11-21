# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 13 · Problemas de suma: las 4 clases animadas.
Metáfora: la feria de juegos de la escuela de Sofi. Regla de primeros años y regla de variedad del banco.
Genera tools/medio/clase/lecciones/medio-mat1-m13-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '9904c8c2-be39-45e6-a2ac-d312e6d729a7', 2: 'af7b880e-ad69-4b8a-990c-845f08fa3826', 3: 'd1ee40a7-b555-43cf-ad87-a6f9fb15c58b', 4: '3b20ae9f-8118-4b03-819c-48d843e50955'}
TIT = {1: 'Juntar y agregar', 2: 'Avanzar y ganar', 3: 'Completar cantidades', 4: 'Armar problemas de suma'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎪", "lineas": ["Hay feria de juegos en la escuela.", "Sofi y Tomi ganan premios.", "¿Cuántos ganaron?"], "titulo": "PROBLEMAS", "sub": "de juntar y agregar",
  "voz": ["¡Hay *feria de juegos* en la escuela!", "Sofi y Tomi ganan premios.", "¿Cuántos premios ganaron?", "Hoy: *problemas de juntar y agregar*."]},
 {"t": "flujo", "titulo": "CÓMO RESOLVER", "items": [{"txt": "Leo", "emoji": "👀"}, {"txt": "Pienso la cuenta", "emoji": "🤔"}, {"txt": "Respondo", "emoji": "✅"}],
  "voz": ["Primero *leo* el problema.", "Después *pienso* la cuenta.", "Al final, *respondo* la pregunta."]},
 {"t": "juntar", "a": {"emoji": "⚽", "n": 5}, "b": {"emoji": "⚽", "n": 3}, "texto": "5 + 3 = 8",
  "voz": ["Sofi gana *5* pelotas. Tomi gana *3*.", "¿Cuántas ganaron? Las juntamos.", "¡Ganaron *8* pelotas entre los dos!"]},
 {"t": "agregar", "emoji": "🎈", "n": 6, "mas": 4, "texto": "6 + 4 = 10",
  "voz": ["En el puesto hay *6* globos.", "Llegan 4 más: 7, 8, 9, 10.", "¡Ahora hay *10* globos!"]},
 {"t": "pregunta", "pregunta": "Sofi tiene 4 caramelos. Le dan 5. ¿Cuántos tiene?", "opciones": ["1", "9", "45"], "correcta": 1,
  "voz": ["Ahora vos. Sofi tiene 4 y le dan 5.", "¿Cuántos caramelos tiene?", "¡*9*! 4 más 5."]},
 {"t": "resumen", "items": [["LEER", "la historia"], ["SUMAR", "juntar o agregar"], ["RESPONDER", "con una oración"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Leemos* la historia.", "*Sumamos*: juntamos o agregamos.", "Y *respondemos* la pregunta.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Estás en el casillero 4 y avanzás 3. ¿Dónde quedás?", "segundos": 6, "respuesta": "¡EN EL 7!", "emoji": "🎲", "titulo": "AVANZAR", "sub": "y ganar",
  "voz": ["Desafío: estás en el 4 y avanzás 3.", "¡Quedás en el *7*!", "Hoy: *avanzar y ganar*."]},
 {"t": "saltos", "titulo": "EL JUEGO DE LA OCA", "min": 0, "max": 12, "cada": 1, "inicio": 4, "saltos": [{"a": 1, "txt": "+1"}, {"a": 1, "txt": "+1"}, {"a": 1, "txt": "+1"}],
  "voz": ["Sofi está en el *4* y saca 3.", "Un salto: ¡5!", "Otro salto: ¡6!", "Y otro más: ¡queda en el *7*!"]},
 {"t": "cuenta", "filas": ["8", "5"], "op": "+", "resultado": "13",
  "voz": ["Tomi tiene 8 puntos y gana 5.", "8 más 5: ¡tiene *13* puntos!"]},
 {"t": "agregar", "emoji": "⭐", "n": 7, "mas": 2, "texto": "7 + 2 = 9",
  "voz": ["Sofi tiene *7* estrellas del juego.", "Gana 2 más: 8, 9.", "¡Ahora tiene *9* estrellas!"]},
 {"t": "consejo", "titulo": "DESDE DONDE ESTÁS", "texto": "No cuentes tu casillero", "emoji": "📍",
  "voz": ["Truco: empezá a contar *después* de tu casillero."]},
 {"t": "pregunta", "pregunta": "Tomi está en el 9. Avanza 2. ¿Dónde queda?", "opciones": ["7", "11", "92"], "correcta": 1,
  "voz": ["Ahora vos. Tomi está en el 9.", "Avanza 2. ¿Dónde queda?", "¡En el *11*! Diez, once."]},
 {"t": "resumen", "items": [["AVANZAR", "sumamos saltos"], ["GANAR", "sumamos puntos"], ["CONTAR", "desde donde estoy"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Avanzar* es sumar saltos.", "*Ganar* es sumar puntos.", "Contamos *desde donde estamos*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Cuántas pelotas tenés?"}, {"yo": True, "txt": "Tengo 6 y quiero 9"}, {"yo": False, "txt": "¿Cuántas te faltan?"}], "titulo": "COMPLETAR", "sub": "cantidades",
  "voz": ["Tomi le escribe a Sofi.", "Sofi tiene 6 pelotas y quiere 9.", "¿Cuántas le faltan?", "Hoy: *completar cantidades*."]},
 {"t": "igualar", "a": {"emoji": "⚽", "n": 6}, "b": {"emoji": "⚽", "n": 9}, "accion": "agregar", "texto": "¡FALTAN 3!",
  "voz": ["Sofi tiene *6*. Quiere tener *9*.", "Agregamos: 7, 8, 9.", "¡Le faltan *3* pelotas!"]},
 {"t": "balanza", "izq": {"cab": "TENGO", "items": ["🍎🍎🍎🍎🍎🍎🍎"]}, "der": {"cab": "QUIERO", "items": ["🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎"]}, "gana": "der",
  "voz": ["De un lado, lo que *tengo*: 7.", "Del otro, lo que *quiero*: 10.", "¡Faltan *3* para que quede pareja!"]},
 {"t": "cuenta", "filas": ["7", "?"], "op": "+", "resultado": "10",
  "voz": ["7 más algo es igual a 10.", "Contamos 8, 9, 10: ¡el algo es *3*!"]},
 {"t": "pregunta", "pregunta": "Tomi tiene 5. Quiere 8. ¿Cuántos le faltan?", "opciones": ["8", "3", "13"], "correcta": 1,
  "voz": ["Ahora vos. Tiene 5 y quiere 8.", "¿Cuántos le faltan?", "¡*3*! Seis, siete, ocho."]},
 {"t": "errores", "items": [{"mal": "Responder el número grande", "bien": "Responder lo que falta"}],
  "voz": ["Ojo con este error.", "La respuesta es *lo que falta*, no el grande."]},
 {"t": "resumen", "items": [["TENGO", "el número chico"], ["QUIERO", "el número grande"], ["FALTA", "contamos el camino"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Miramos lo que *tengo*.", "Miramos lo que *quiero*.", "Contamos lo que *falta*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "CONCURSO", "titular": "¡INVENTÁ TU PROBLEMA!", "bajada": "Premio para el mejor problema", "emoji": "🏆", "titulo": "ARMAR", "sub": "problemas de suma",
  "voz": ["¡Concurso en la feria de la escuela!", "Gana quien *invente* el mejor problema.", "Hoy: *armar problemas de suma*."]},
 {"t": "matriz", "titulo": "LAS PARTES DEL PROBLEMA", "celdas": [{"cab": "QUIÉN", "txt": "Sofi"}, {"cab": "TIENE", "txt": "3 manzanas"}, {"cab": "PASA", "txt": "le dan 4"}, {"cab": "PREGUNTA", "txt": "¿cuántas tiene?"}],
  "voz": ["Todo problema tiene *cuatro partes*.", "*Quién*: Sofi.", "Qué *tiene*: 3 manzanas.", "Qué *pasa*: le dan 4 más.", "Y la *pregunta*: ¿cuántas tiene?"]},
 {"t": "juntar", "a": {"emoji": "🍎", "n": 3}, "b": {"emoji": "🍎", "n": 4}, "texto": "3 + 4 = 7",
  "voz": ["Resolvemos el problema de Sofi.", "Juntamos sus 3 manzanas y las 4.", "¡Tiene *7* manzanas!"]},
 {"t": "bloques", "titulo": "INVENTÁ CON 5 + 5", "items": [{"cab": "QUIÉN", "txt": "Tomi"}, {"cab": "QUÉ PASA", "txt": "Tiene 5 autitos y le regalan 5"}, {"cab": "PREGUNTA", "txt": "¿Cuántos autitos tiene?"}],
  "voz": ["Inventamos otro con 5 más 5.", "Elegimos *quién*: Tomi.", "Decimos *qué pasa*: le regalan 5.", "Y hacemos la *pregunta*."]},
 {"t": "pregunta", "pregunta": "¿Qué le falta? «Sofi tiene 3 globos y le dan 2.»", "opciones": ["La pregunta", "Los números", "Un nombre"], "correcta": 0,
  "voz": ["Ahora vos. Escuchá este problema.", "Sofi tiene 3 globos y le dan 2. ¿Qué falta?", "¡La *pregunta*!"]},
 {"t": "resumen", "items": [["QUIÉN", "Sofi, Tomi…"], ["QUÉ PASA", "gana, le dan…"], ["PREGUNTA", "¿cuántos tiene?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Elegimos *quién*.", "Contamos *qué pasa*.", "Y terminamos con una *pregunta*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m13-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 13 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
