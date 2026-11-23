# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 13 · La multiplicación como suma repetida: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (bandejas con la misma cantidad).
Usa la plantilla nueva «grupos» (grupos iguales). Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat2-m13-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '2f08bdc0-efb3-4fcd-865a-5892ed9c90e8', 2: '6e981182-175c-4799-bd86-9b81959bdfc4', 3: '497584c2-0941-4bcd-9a1f-46829e842d5e', 4: 'dcffea70-13ef-4030-8c1b-5b0051f9c9e2'}
TIT = {1: 'Sumar muchas veces lo mismo', 2: 'Series de números', 3: 'Escribir con multiplicación', 4: 'Problemas de grupos iguales'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa llena bandejas.", "Pone 4 alfajores en cada una.", "¿Cuántos usa?"], "titulo": "SUMAR", "sub": "muchas veces lo mismo",
  "voz": ["Rosa llena *bandejas* de alfajores.", "En cada bandeja pone *4*.", "¿Cuántos alfajores usa en total?", "Hoy: *sumar muchas veces lo mismo*."]},
 {"t": "grupos", "emoji": "🍫", "grupos": 3, "cada": 4, "texto": "4 + 4 + 4 = 12", "titulo": "TRES BANDEJAS",
  "voz": ["Mirá: tres bandejas con 4 alfajores.", "Contamos de a 4: 4, 8, 12.", "¡Son *12* alfajores!"]},
 {"t": "comparar", "a": {"cab": "IGUALES", "texto": "4, 4 y 4", "emoji": "✅"}, "b": {"cab": "DISTINTOS", "texto": "4, 2 y 5", "emoji": "❌"}, "signo": "≠",
  "voz": ["Estos grupos son *iguales*: todos tienen 4.", "Estos son *distintos*: 4, 2 y 5.", "¡Hoy trabajamos con grupos *iguales*!"]},
 {"t": "grupos", "emoji": "⭐", "grupos": 5, "cada": 2, "texto": "2 + 2 + 2 + 2 + 2 = 10", "titulo": "CINCO DE 2",
  "voz": ["Ahora cinco grupos de 2.", "2, 4, 6, 8, 10.", "¡Son *10* estrellas!"]},
 {"t": "pregunta", "pregunta": "4 bandejas con 3 caramelos. ¿Cuántos son?", "opciones": ["12", "7", "43"], "correcta": 0,
  "voz": ["Ahora vos: 4 bandejas de 3.", "Contá de a 3: 3, 6, 9…", "¡*12*! 3 más 3 más 3 más 3."]},
 {"t": "resumen", "items": [["GRUPOS IGUALES", "misma cantidad"], ["SUMAR", "lo mismo varias veces"], ["MIRAR", "grupos y cuántos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *grupos iguales* tienen la misma cantidad.", "Sumamos *lo mismo* varias veces.", "Miramos cuántos grupos y cuántos en cada uno.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Contá de 5 en 5 hasta 30", "segundos": 8, "respuesta": "5, 10, 15, 20, 25, 30", "emoji": "🖐️", "titulo": "SERIES", "sub": "de números",
  "voz": ["Desafío: contá de 5 en 5 hasta 30.", "¡5, 10, 15, 20, 25, 30!", "Hoy: *series de números*."]},
 {"t": "saltos", "titulo": "DE 2 EN 2", "min": 0, "max": 10, "cada": 2, "inicio": 0, "saltos": [{"a": 2, "txt": "+2"}, {"a": 2, "txt": "+2"}, {"a": 2, "txt": "+2"}, {"a": 2, "txt": "+2"}, {"a": 2, "txt": "+2"}],
  "voz": ["Los alfajores vienen de a dos.", "Saltamos: *2*.", "*4*.", "*6*.", "*8*.", "¡*10*!"]},
 {"t": "tren", "desde": 5, "hasta": 40, "paso": 5, "faltan": [20, 35], "titulo": "DE 5 EN 5",
  "voz": ["El tren cuenta de 5 en 5.", "5, 10, 15, 25, 30, 40.", "¡Faltaban el *20* y el *35*!"]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["10", "20", "30"], "falta": "40", "regla": "Saltamos de 10 en 10",
  "voz": ["Mirá: 10, 20, 30…", "¿Qué sigue?", "¡*40*! De 10 en 10."]},
 {"t": "vof", "afirmacion": "De 5 en 5: 5, 10, 15, 21", "emoji": "🤔", "verdadero": False, "explicacion": "Después del 15 viene el 20",
  "voz": ["¿Verdadero o falso? 5, 10, 15, 21.", "Pensá: ¿cuánto salta?", "¡*Falso*! Después del 15 viene el *20*."]},
 {"t": "resumen", "items": [["DE 2 EN 2", "2, 4, 6, 8"], ["DE 5 EN 5", "5, 10, 15, 20"], ["DE 10 EN 10", "10, 20, 30"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "De 2 en 2: 2, 4, 6, 8.", "De 5 en 5: 5, 10, 15, 20.", "De 10 en 10: 10, 20, 30.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, 4 + 4 + 4 es largo 😩"}, {"yo": True, "txt": "¡Escribilo con ×!"}, {"yo": False, "txt": "¿Con qué?"}], "titulo": "ESCRIBIR", "sub": "con multiplicación",
  "voz": ["Tomi le escribe a Rosa.", "4 más 4 más 4 es muy largo.", "Rosa le dice: ¡escribilo con el *por*!", "Hoy: *escribir con multiplicación*."]},
 {"t": "transforma", "titulo": "MÁS CORTO", "pasos": [{"txt": "4 + 4 + 4"}, {"txt": "3 veces 4", "nota": "contamos las veces"}, {"txt": "3 × 4 = 12", "nota": "se lee 3 por 4"}],
  "voz": ["Tenemos 4 más 4 más 4.", "Es sumar *3 veces 4*.", "Se escribe 3 *por* 4. ¡Da *12*!"], "sticker": {"txt": "✨", "paso": 2}},
 {"t": "grupos", "emoji": "🍪", "grupos": 2, "cada": 5, "texto": "2 × 5 = 10", "titulo": "2 VECES 5",
  "voz": ["Dos bandejas de 5 galletitas.", "5, 10.", "¡2 por 5 es *10*!"]},
 {"t": "unir", "titulo": "SUMA Y MULTIPLICACIÓN", "pares": [["2 + 2 + 2", "3 × 2"], ["5 + 5", "2 × 5"], ["10 + 10 + 10", "3 × 10"]],
  "voz": ["Uní cada suma con su multiplicación.", "2 más 2 más 2: *3 por 2*.", "5 más 5: *2 por 5*.", "10 más 10 más 10: *3 por 10*."]},
 {"t": "errores", "items": [{"mal": "3 × 4 = 3 + 4 = 7", "bien": "3 × 4 = 4 + 4 + 4 = 12"}],
  "voz": ["Ojo con este error.", "3 por 4 no es 3 más 4: es *12*."]},
 {"t": "resumen", "items": [["VECES", "cuántos grupos"], ["×", "se lee por"], ["3 × 4", "4 + 4 + 4 = 12"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *veces* son cuántos grupos.", "El signo × se lee *por*.", "3 por 4 es 4 más 4 más 4: *12*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Pedido de cajitas!", "bajada": "La escuela quiere 5 cajitas de 2", "emoji": "🎁", "titulo": "PROBLEMAS", "sub": "de grupos iguales",
  "voz": ["¡Último momento: la escuela pide cajitas!", "Quieren 5 cajitas con 2 alfajores.", "Hoy: *problemas de grupos iguales*."]},
 {"t": "pasos", "titulo": "CÓMO LO RESUELVO", "items": [{"txt": "¿Cuántos grupos?", "emoji": "📦"}, {"txt": "¿Cuántos en cada uno?", "emoji": "🍫"}, {"txt": "Multiplico", "emoji": "✖️"}],
  "voz": ["¿Cómo resolvemos estos problemas?", "Primero: ¿cuántos *grupos* hay?", "Después: ¿cuántos hay en *cada uno*?", "¡Y multiplicamos!"]},
 {"t": "grupos", "emoji": "🍫", "grupos": 5, "cada": 2, "texto": "5 × 2 = 10", "titulo": "CINCO CAJITAS",
  "voz": ["5 cajitas con 2 alfajores.", "2, 4, 6, 8, 10.", "¡5 por 2 es *10*! Rosa usa 10 alfajores."]},
 {"t": "pistas", "problema": "Hay 3 mesas con 4 sillas cada una. ¿Cuántas sillas hay?", "pistas": ["Hay 3 grupos", "Cada grupo tiene 4", "3 × 4"], "respuesta": "12 sillas",
  "voz": ["Ahora vos: 3 mesas con 4 sillas.", "Pista uno: hay *3 grupos*.", "Pista dos: cada grupo tiene *4*.", "Pista tres: 3 por 4.", "¡Hay *12* sillas!"]},
 {"t": "jefe", "jefe": {"nombre": "Señor Grupos", "emoji": "🐲"}, "preguntas": [{"p": "2 autos con 4 ruedas", "r": "8"}, {"p": "4 bolsas de 10", "r": "40"}],
  "voz": ["¡Apareció el *Señor Grupos*!", "Resolvemos sus problemas.", "2 autos de 4 ruedas: *8*.", "¡4 bolsas de 10: *40*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["GRUPOS", "¿cuántos hay?"], ["CADA UNO", "¿cuántos tiene?"], ["×", "grupos por cantidad"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Buscamos cuántos *grupos* hay.", "Y cuántos hay en *cada uno*.", "Después *multiplicamos*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m13-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 13 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
