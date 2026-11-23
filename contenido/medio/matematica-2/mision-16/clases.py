# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 16 · Tablas del 2, 5 y 10: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (cajitas de 2, bandejas de 5 y paquetes de 10).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat2-m16-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '1934c2b0-4f3d-428d-9bbc-ee7518ca420c', 2: '2243128c-57d1-42da-8f12-f8fc307c704f', 3: '932b914f-691b-456f-9a60-d7ba9f8085c7', 4: 'e4742e0d-fe8d-4e90-9f44-524fc68ae7e8'}
TIT = {1: 'La tabla del 2', 2: 'La tabla del 5', 3: 'La tabla del 10', 4: 'Usar las tablas para calcular'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa arma cajitas.", "Cada una lleva 2 alfajores.", "¿Cuántos usa?"], "titulo": "LA TABLA", "sub": "del 2",
  "voz": ["Rosa arma *cajitas de regalo*.", "Cada cajita lleva *2 alfajores*.", "¿Cuántos usa en muchas cajitas?", "Hoy: *la tabla del 2*."]},
 {"t": "grupos", "emoji": "🍫", "grupos": 3, "cada": 2, "texto": "3 × 2 = 6", "titulo": "TRES CAJITAS",
  "voz": ["Tres cajitas de 2.", "Contamos: 2, 4, 6.", "¡3 por 2 es *6*!"]},
 {"t": "saltos", "titulo": "DE 2 EN 2", "min": 0, "max": 12, "cada": 2, "inicio": 0, "saltos": [{"a": 2, "txt": "1 × 2"}, {"a": 2, "txt": "2 × 2"}, {"a": 2, "txt": "3 × 2"}, {"a": 2, "txt": "4 × 2"}, {"a": 2, "txt": "5 × 2"}],
  "voz": ["La tabla del 2 salta de 2 en 2.", "1 por 2: *2*.", "2 por 2: *4*.", "3 por 2: *6*.", "4 por 2: *8*.", "¡5 por 2: *10*!"]},
 {"t": "consejo", "titulo": "ES EL DOBLE", "texto": "× 2 es hacer el doble", "emoji": "👯",
  "voz": ["Truco: por 2 es hacer el *doble*."]},
 {"t": "quiz4", "pregunta": "¿Cuánto es 6 × 2?", "opciones": ["12", "8", "62"], "correcta": 0,
  "voz": ["Ahora vos: 6 por 2.", "Pensá en el doble de 6.", "¡*12*!"]},
 {"t": "resumen", "items": [["TABLA DEL 2", "de 2 en 2"], ["DOBLE", "× 2"], ["PARES", "2, 4, 6, 8"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La tabla del 2 salta *de 2 en 2*.", "Por 2 es el *doble*.", "Todos los resultados son *pares*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cuántos dedos hay en 4 manos?", "segundos": 6, "respuesta": "¡20!", "emoji": "🖐️", "titulo": "LA TABLA", "sub": "del 5",
  "voz": ["Desafío: ¿cuántos dedos hay en 4 manos?", "¡*20*! 5, 10, 15, 20.", "Hoy: *la tabla del 5*."]},
 {"t": "arreglo", "emoji": "🍪", "filas": 4, "cols": 5, "texto": "4 × 5 = 20", "titulo": "BANDEJAS DE 5",
  "voz": ["Rosa pone 5 galletitas por fila.", "5, 10, 15, 20.", "¡4 por 5 es *20*!"]},
 {"t": "tren", "desde": 5, "hasta": 50, "paso": 5, "faltan": [25, 40], "titulo": "LA TABLA DEL 5",
  "voz": ["El tren de la tabla del 5.", "5, 10, 15, 20, 30, 35, 45, 50.", "¡Faltaban el *25* y el *40*!"]},
 {"t": "vof", "afirmacion": "9 × 5 = 44", "emoji": "🤔", "verdadero": False, "explicacion": "Termina en 5 o en 0: es 45",
  "voz": ["¿Verdadero o falso? 9 por 5 es 44.", "Mirá cómo termina…", "¡*Falso*! Tiene que terminar en 5 o 0: *45*."]},
 {"t": "memoria", "titulo": "LA TABLA DEL 5", "items": ["5", "10", "15", "20", "25", "30"], "falta": 3,
  "voz": ["Mirá la tabla del 5.", "Se tapan… ¡y uno desapareció!", "¡Faltaba el *20*!"]},
 {"t": "resumen", "items": [["TABLA DEL 5", "de 5 en 5"], ["TERMINA", "en 5 o en 0"], ["MANOS", "5 dedos cada una"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La tabla del 5 salta *de 5 en 5*.", "Los resultados terminan en *5 o en 0*.", "Como los dedos de las *manos*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿cuánto es 7 × 10?"}, {"yo": True, "txt": "¡Fácil! Agregá un 0"}, {"yo": False, "txt": "¿¡70!?"}], "titulo": "LA TABLA", "sub": "del 10",
  "voz": ["Tomi le pregunta a Rosa: 7 por 10.", "Rosa le dice: ¡agregá un cero!", "¡70! ¡Qué fácil!", "Hoy: *la tabla del 10*."]},
 {"t": "agrupar", "niveles": [{"nombre": "1 PAQUETE", "valor": "10", "icono": "pack"}, {"nombre": "10 PAQUETES", "valor": "100", "icono": "caja"}], "salto": "×10",
  "voz": ["Un paquete tiene *10* alfajores.", "10 paquetes llenan una caja.", "¡10 por 10 es *100*!"]},
 {"t": "transforma", "titulo": "UN 0 AL FINAL", "pasos": [{"txt": "4 × 10"}, {"txt": "4 → 40", "nota": "agregamos un 0"}, {"txt": "4 × 10 = 40"}],
  "voz": ["Mirá: 4 por 10.", "Al 4 le agregamos un *cero*.", "¡4 por 10 es *40*!"], "sticker": {"txt": "0️⃣", "paso": 1}},
 {"t": "unir", "titulo": "UNÍ", "pares": [["3 × 10", "30"], ["5 × 10", "50"], ["9 × 10", "90"]],
  "voz": ["Uní cada cuenta con su resultado.", "3 por 10: *30*.", "5 por 10: *50*.", "9 por 10: *90*."]},
 {"t": "errores", "items": [{"mal": "7 × 10 = 17", "bien": "7 × 10 = 70"}],
  "voz": ["Ojo con este error.", "7 por 10 es *70*: el cero va al final."]},
 {"t": "resumen", "items": [["TABLA DEL 10", "de 10 en 10"], ["EL 0", "va al final"], ["10 × 10", "es 100"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La tabla del 10 salta *de 10 en 10*.", "El *cero* va al final.", "10 por 10 es *100*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Llegan pedidos de todo tipo!", "bajada": "De a 2, de a 5 y de a 10", "emoji": "📦", "titulo": "USAR", "sub": "las tablas",
  "voz": ["¡Último momento: llegan pedidos de todo tipo!", "Cajitas de 2, bandejas de 5, paquetes de 10.", "Hoy: *usar las tablas para calcular*."]},
 {"t": "grilla", "titulo": "LA TABLA DE ROSA", "filas": 5, "cols": 10, "resaltar": [{"fila": 2, "col": 4, "txt": "8"}, {"fila": 5, "col": 4, "txt": "20"}],
  "voz": ["Esta es una tabla para buscar resultados.", "Fila del 2, columna del 4: *8*.", "Fila del 5, columna del 4: *20*."]},
 {"t": "escala", "titulo": "4 × 2, 4 × 5, 4 × 10", "items": [{"txt": "8", "emoji": "🍫", "valor": 8}, {"txt": "20", "emoji": "📦", "valor": 20}, {"txt": "40", "emoji": "🚚", "valor": 40}],
  "voz": ["4 cajitas de 2: *8*.", "4 bandejas de 5: *20*.", "¡4 paquetes de 10: *40*!"]},
 {"t": "pistas", "problema": "Hay 7 pares de medias. ¿Cuántas medias hay?", "pistas": ["Un par tiene 2", "Uso la tabla del 2", "7 × 2"], "respuesta": "14 medias",
  "voz": ["Ahora vos: 7 pares de medias.", "Pista uno: un par tiene *2*.", "Pista dos: uso la *tabla del 2*.", "Pista tres: 7 por 2.", "¡*14* medias!"]},
 {"t": "jefe", "jefe": {"nombre": "Dragón Tablas", "emoji": "🐉"}, "preguntas": [{"p": "8 × 2", "r": "16"}, {"p": "6 × 5", "r": "30"}, {"p": "9 × 10", "r": "90"}],
  "voz": ["¡Apareció el *Dragón Tablas*!", "Lo vencemos con las tablas.", "8 por 2: *16*.", "6 por 5: *30*.", "¡9 por 10: *90*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["ELEGIR", "¿de a cuánto vienen?"], ["BUSCAR", "en la tabla"], ["RESPONDER", "con palabras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Miramos *de a cuánto* vienen.", "Buscamos en la *tabla*.", "Respondemos *con palabras*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m16-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 16 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
