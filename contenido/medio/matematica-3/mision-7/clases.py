# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 7 · Problemas de suma y resta: las 4 clases animadas.
Metáfora de toda la misión: la biblioteca del barrio de Martín.
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'ce9a3a6c-8e4a-454c-8f4c-95a8866d4b45', 2: 'd9858edc-839c-4cea-8edd-f2d618859f3b', 3: 'e56c2ab1-a003-4577-9c4b-bee3ca6e154b', 4: '6c42c1b2-3553-425a-8ebf-d9cbf4f7626d'}
TIT = {1: 'Distancia entre números', 2: 'Cantidad inicial desconocida', 3: 'Problemas de varios pasos', 4: 'Inventar problemas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
MARTIN = {"nombre": "Martín", "emoji": "👨‍🏫"}

N1 = [
 {"t": "gancho", "emoji": "📚", "final": "🤔", "titulo": "DISTANCIA", "sub": "entre números",
  "voz": ["La biblioteca tiene *3.750* libros.", "Quiere llegar a *6.000*. ¿Cuántos le faltan?", "Hoy: *la distancia entre números*."]},
 {"t": "saltos", "titulo": "CONTAMOS PARA ADELANTE", "min": 3000, "max": 6000, "cada": 1000, "inicio": 3750, "saltos": [{"a": 4000, "txt": "+ 250"}, {"a": 6000, "txt": "+ 2.000"}],
  "voz": ["Empezamos en el 3.750.", "Saltamos hasta el 4.000: *250*.", "Y del 4.000 al 6.000: *2.000*."]},
 {"t": "definicion", "palabra": "Distancia", "texto": "Cuánto hay de un número a otro. Se cuenta para adelante o se resta.", "emoji": "📏",
  "voz": ["La *distancia* es cuánto hay de un número a otro.", "Contamos para adelante, o *restamos*."]},
 {"t": "transforma", "titulo": "CON UNA RESTA", "pasos": [{"txt": "6.000 − 3.750"}, {"txt": "250 + 2.000", "nota": "saltos"}, {"txt": "= 2.250"}],
  "voz": ["También podemos *restar*: 6.000 menos 3.750.", "Los saltos eran 250 y 2.000.", "¡Le faltan *2.250* libros!"]},
 {"t": "quiz4", "pregunta": "¿Cuánto hay del 4.800 al 5.000?", "opciones": ["200", "800", "1.200"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuánto hay del 4.800 al 5.000?", "Contá de 100 en 100…", "¡*200*!"]},
 {"t": "errores", "items": [{"mal": "Sumar los dos números para la distancia", "bien": "Restar o contar para adelante"}],
  "voz": ["Ojo con este error.", "Para la distancia *no se suman* los dos números."]},
 {"t": "resumen", "items": [["DISTANCIA", "cuánto falta"], ["CONTAR", "para adelante"], ["RESTAR", "grande menos chico"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La distancia dice *cuánto falta*.", "Podemos *contar para adelante*.", "O *restar*: el grande menos el chico.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": MARTIN, "lugar": "📚", "lineas": ["Martín no sabe cuántos libros tenía.", "Le regalaron 1.250.", "Ahora tiene 4.600."], "titulo": "EL PRINCIPIO", "sub": "desconocido",
  "voz": ["Martín es el bibliotecario del barrio.", "No sabe cuántos libros *tenía*.", "Le regalaron 1.250 y ahora tiene *4.600*.", "Hoy: *la cantidad inicial desconocida*."]},
 {"t": "orden", "titulo": "LA HISTORIA AL REVÉS", "items": [{"txt": "Tenía ?", "emoji": "❓"}, {"txt": "Llegan 1.250", "emoji": "🎁"}, {"txt": "Tiene 4.600", "emoji": "📚"}], "relato": [2, 1, 0],
  "voz": ["Contamos la historia *al revés*.", "Ahora tiene 4.600. Antes llegaron 1.250.", "Si sacamos lo que llegó, ¡volvemos al *principio*!"]},
 {"t": "platillos", "titulo": "? + 1.250 = 4.600", "estados": [{"izq": ["?", "1.250"], "der": ["4.600"], "txt": "Algo más 1.250"}, {"izq": ["?"], "der": ["4.600 − 1.250"], "txt": "Sacamos 1.250"}, {"izq": ["?"], "der": ["3.350"], "txt": "¡Tenía 3.350!"}],
  "voz": ["Algo más 1.250 es igual a 4.600.", "Sacamos 1.250 de los dos lados.", "¡Tenía *3.350* libros!"]},
 {"t": "prediccion", "pregunta": "Prestó 800 y le quedan 2.500. ¿Tenía…?", "a": {"txt": "3.300", "emoji": "😎"}, "b": {"txt": "1.700", "emoji": "🤔"}, "correcta": "a", "resultado": "¡3.300! Sumamos",
  "voz": ["Martín prestó 800 y le quedan 2.500.", "Si se fueron, para volver *sumamos*…", "¡Tenía *3.300*!"]},
 {"t": "errores", "items": [{"mal": "Si llegaron, para el principio sumo", "bien": "Si llegaron, para el principio resto"}],
  "voz": ["Ojo con este error.", "Si llegaron libros, para volver al principio *restamos*."]},
 {"t": "resumen", "items": [["AL REVÉS", "volvemos atrás"], ["SI LLEGARON", "restamos"], ["SI SE FUERON", "sumamos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos la historia *al revés*.", "Si llegaron, *restamos*.", "Si se fueron, *sumamos*.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Mucho movimiento en la biblioteca!", "bajada": "Compran libros y prestan otros", "emoji": "📚", "titulo": "VARIOS PASOS", "sub": "en un problema",
  "voz": ["¡Último momento: mucho movimiento en la biblioteca!", "Compran libros y *prestan* otros.", "Hoy: *problemas de varios pasos*."]},
 {"t": "flujo", "titulo": "PASO A PASO", "items": [{"txt": "Tenía 3.400", "emoji": "📚"}, {"txt": "+ 1.200 = 4.600", "emoji": "🛒"}, {"txt": "− 800 = 3.800", "emoji": "📤"}],
  "voz": ["La biblioteca tenía *3.400* libros.", "Compra 1.200: ahora tiene *4.600*.", "Presta 800: le quedan *3.800*."]},
 {"t": "pistas", "problema": "Tiene 5.000. Presta 1.500 y le devuelven 700. ¿Cuántos hay?", "pistas": ["Primero: 5.000 − 1.500", "Después: + 700"], "respuesta": "4.200",
  "voz": ["Tiene 5.000. Presta 1.500 y le devuelven 700.", "Pista: primero, 5.000 menos 1.500: *3.500*.", "Pista: después, más 700.", "¡Hay *4.200* libros!"]},
 {"t": "quiz4", "pregunta": "¿Cuántas cuentas hacen falta?", "opciones": ["Una", "Dos", "Ninguna"], "correcta": 1,
  "voz": ["La biblioteca tenía, compró y después prestó.", "¿Cuántas cuentas hacen falta?", "¡*Dos*: una suma y una resta!"]},
 {"t": "errores", "items": [{"mal": "Hacer solo la primera cuenta", "bien": "Hacer todos los pasos"}],
  "voz": ["Ojo con este error.", "Hay que hacer *todos* los pasos, no solo el primero."]},
 {"t": "resumen", "items": [["LEER", "todo el problema"], ["PASO A PASO", "una cuenta por vez"], ["RESPONDER", "con una oración"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos *todo* el problema.", "Hacemos *una cuenta por vez*.", "Respondemos *con una oración*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Martín", "emoji": "👨‍🏫"}, "mensajes": [{"yo": False, "txt": "Te paso una cuenta: 2.500 + 1.300"}, {"yo": True, "txt": "¿Y qué hago?"}, {"yo": False, "txt": "¡Inventá un problema!"}], "titulo": "INVENTAR", "sub": "problemas",
  "voz": ["Martín manda una cuenta: 2.500 más 1.300.", "Pide algo distinto.", "¡Que inventemos un *problema*!", "Hoy: *inventar problemas*."]},
 {"t": "bloques", "titulo": "UN PROBLEMA TIENE", "items": [{"cab": "DATOS", "txt": "2.500 y 1.300"}, {"cab": "QUÉ PASA", "txt": "llegan más"}, {"cab": "PREGUNTA", "txt": "¿cuántos hay?"}],
  "voz": ["Un problema tiene partes.", "Los *datos*: 2.500 y 1.300.", "*Qué pasa*: llegan más libros.", "Y la *pregunta*: ¿cuántos hay?"]},
 {"t": "comparar", "a": {"cab": "SUMA", "texto": "llegan, juntan, ganan", "emoji": "➕"}, "b": {"cab": "RESTA", "texto": "se van, prestan, faltan", "emoji": "➖"}, "signo": "y",
  "voz": ["Para una *suma*: algo llega, se junta o se gana.", "Para una *resta*: algo se va, se presta o falta.", "¡Elegimos la historia según la cuenta!"]},
 {"t": "quiz4", "pregunta": "¿Qué historia va con 3.000 − 500?", "opciones": ["Prestó 500", "Le regalan 500", "Compra 500"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué historia va con una resta?", "Algo tiene que irse…", "¡*Prestó* 500!"]},
 {"t": "errores", "items": [{"mal": "Un problema sin pregunta", "bien": "Siempre lleva pregunta"}],
  "voz": ["Ojo con este error.", "Un problema siempre lleva *pregunta*."]},
 {"t": "resumen", "items": [["DATOS", "los números"], ["HISTORIA", "suma o resta"], ["PREGUNTA", "al final"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Ponemos los *datos*.", "Inventamos una *historia* que vaya con la cuenta.", "Y al final, la *pregunta*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m7-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 7 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
