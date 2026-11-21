# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 4 · Comparar y ordenar hasta 1.000: las 4 clases animadas.
Metáfora: los pedidos y camiones de la fábrica de alfajores de la abuela Rosa. Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat2-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '98d3a50a-5e46-44a0-8f46-65d8b7f795ce', 2: 'cede3e3c-e778-4702-8aad-985e96b56c78', 3: '15046120-689c-4893-a781-86379424a6b8', 4: 'af2ffef0-cae3-46fd-9412-86a7c0bff3fb'}
TIT = {1: 'Mayor y menor hasta mil', 2: 'Ordenar números', 3: 'Números redondos', 4: 'La recta numérica hasta 1.000'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🚚", "lineas": ["Llegaron dos pedidos.", "Uno de 412 alfajores.", "Otro de 398."], "titulo": "MAYOR", "sub": "y menor",
  "voz": ["Llegaron *dos pedidos* a la fábrica de Rosa.", "Uno es de 412 alfajores.", "El otro es de 398.", "Hoy: *mayor y menor hasta mil*."]},
 {"t": "balanza", "izq": {"cab": "412", "items": ["4 cajas", "1 paquete", "2 sueltos"]}, "der": {"cab": "398", "items": ["3 cajas", "9 paquetes", "8 sueltos"]}, "gana": "izq",
  "voz": ["El pedido de 412 tiene *4 cajas*.", "El de 398 tiene *3 cajas*.", "¡Más cajas, más alfajores: *412 es mayor*!"]},
 {"t": "pasos", "titulo": "CÓMO COMPARAR", "items": [{"txt": "Mirá las centenas", "emoji": "📦"}, {"txt": "Si empatan, las decenas", "emoji": "🍫"}, {"txt": "Si empatan, las unidades", "emoji": "🍪"}],
  "voz": ["¿Cómo comparamos números grandes?", "Primero mirá las *centenas*.", "Si empatan, mirá las *decenas*.", "Si empatan otra vez, mirá las *unidades*."]},
 {"t": "balanza", "izq": {"cab": "356", "items": ["3 cajas", "5 paquetes", "6 sueltos"]}, "der": {"cab": "372", "items": ["3 cajas", "7 paquetes", "2 sueltos"]}, "gana": "der",
  "voz": ["Ahora comparamos 356 y 372.", "Los dos tienen *3 cajas*: empatan.", "Paquetes: 7 es más que 5. ¡*372 es mayor*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es mayor: 645 o 654?", "opciones": ["645", "654"], "correcta": 1,
  "voz": ["Ahora vos. Mirá bien estos dos números.", "¿Cuál es *mayor*: 645 o 654?", "¡*654*! Tiene más decenas."]},
 {"t": "errores", "items": [{"mal": "Mirar solo las unidades", "bien": "Empezar por las centenas"}],
  "voz": ["Ojo con este error.", "Siempre empezá por las *centenas*."]},
 {"t": "resumen", "items": [["MAYOR", "tiene más"], ["MENOR", "tiene menos"], ["COMPARAR", "primero las centenas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *mayor* tiene más.", "El *menor* tiene menos.", "Para comparar, primero las *centenas*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Ordená de menor a mayor: 530, 305, 350", "segundos": 8, "respuesta": "305, 350, 530", "emoji": "🚚", "titulo": "ORDENAR", "sub": "números hasta 1.000",
  "voz": ["Desafío: ordená de menor a mayor: 530, 305 y 350.", "¡305, 350 y 530!", "Hoy: *ordenar números*."]},
 {"t": "orden", "titulo": "LOS CAMIONES DE ROSA", "etq1": "DESORDENADOS", "etq2": "DE MENOR A MAYOR",
  "items": [{"txt": "215", "emoji": "🚚"}, {"txt": "270", "emoji": "🚚"}, {"txt": "540", "emoji": "🚚"}, {"txt": "812", "emoji": "🚚"}], "relato": [2, 0, 3, 1],
  "voz": ["Rosa tiene cuatro camiones con pedidos.", "Están desordenados: 540, 215, 812, 270.", "De menor a mayor: 215, 270, 540, 812."]},
 {"t": "consejo", "titulo": "MENOR A MAYOR", "texto": "Del más chico al más grande", "emoji": "📶",
  "voz": ["Menor a mayor: del *más chico* al *más grande*."]},
 {"t": "orden", "titulo": "AL REVÉS", "etq1": "DESORDENADOS", "etq2": "DE MAYOR A MENOR",
  "items": [{"txt": "950", "emoji": "🚚"}, {"txt": "905", "emoji": "🚚"}, {"txt": "590", "emoji": "🚚"}, {"txt": "509", "emoji": "🚚"}], "relato": [3, 1, 2, 0],
  "voz": ["Ahora al revés: *de mayor a menor*.", "Desordenados: 509, 905, 590, 950.", "Ordenados: 950, 905, 590, 509."]},
 {"t": "pregunta", "pregunta": "De menor a mayor, ¿cuál va primero?", "opciones": ["307", "370", "703"], "correcta": 0,
  "voz": ["Ahora vos. Ordenamos 703, 370 y 307.", "¿Cuál va *primero*, de menor a mayor?", "¡*307*! Es el más chico."]},
 {"t": "errores", "items": [{"mal": "Ordenar por la última cifra", "bien": "Mirar primero las centenas"}],
  "voz": ["Ojo con este error.", "Para ordenar, mirá primero las *centenas*."]},
 {"t": "resumen", "items": [["MENOR A MAYOR", "del chico al grande"], ["MAYOR A MENOR", "del grande al chico"], ["CENTENAS", "se miran primero"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Menor a mayor*: del chico al grande.", "*Mayor a menor*: del grande al chico.", "Las *centenas* se miran primero.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "⭕", "final": "💯", "titulo": "NÚMEROS", "sub": "redondos",
  "voz": ["Rosa ama los números *redondos*.", "¿Qué tienen de especial el 100, el 200, el 300?", "Hoy: *los números redondos*."]},
 {"t": "definicion", "palabra": "Número redondo", "texto": "Termina en 0: 40, 100, 350", "emoji": "⭕",
  "voz": ["Un número *redondo* termina en cero.", "Como 40, 100 o 350: ¡fáciles de contar!"]},
 {"t": "tren", "desde": 100, "hasta": 1000, "paso": 100, "titulo": "DE 100 EN 100",
  "voz": ["Los camiones de Rosa salen de 100 en 100.", "100, 200, 300, 400, 500, 600, 700, 800, 900, 1.000.", "¡Llegamos al *1.000*!"]},
 {"t": "tren", "desde": 410, "hasta": 500, "paso": 10, "titulo": "DE 10 EN 10",
  "voz": ["Ahora de 10 en 10, desde el 410.", "410, 420, 430, 440, 450, 460, 470, 480, 490, 500.", "¡Todos terminan en *cero*!"]},
 {"t": "recta", "min": 230, "max": 240, "paso": 1, "marcas": [{"v": 238, "txt": "238"}],
  "voz": ["¿Entre qué números redondos está el 238?", "Entre el *230* y el *240*. ¡Más cerca del 240!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es un número redondo?", "opciones": ["347", "560", "821"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cuál es un número *redondo*?", "Fijate en la última cifra.", "¡*560*! Termina en cero."]},
 {"t": "consejo", "titulo": "MIRÁ EL FINAL", "texto": "Si termina en 0, es redondo", "emoji": "👀",
  "voz": ["Truco: si termina en *cero*, es redondo."]},
 {"t": "resumen", "items": [["REDONDO", "termina en 0"], ["DE 10 EN 10", "10, 20, 30…"], ["DE 100 EN 100", "100, 200…"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un número *redondo* termina en cero.", "Contamos *de 10 en 10*.", "Y *de 100 en 100*.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🛣️", "lineas": ["Rosa reparte por una ruta larga.", "Hay un cartel cada 100 pasos.", "¿Dónde vive cada cliente?"], "titulo": "LA RECTA", "sub": "hasta 1.000",
  "voz": ["Rosa reparte alfajores por una *ruta* larga.", "Hay un cartel cada 100 pasos.", "¿Dónde vive cada cliente?", "Hoy: *la recta numérica hasta 1.000*."]},
 {"t": "recta", "min": 0, "max": 1000, "paso": 100, "marcas": [{"v": 300, "txt": "300"}, {"v": 650, "txt": "650"}, {"v": 900, "txt": "900"}],
  "voz": ["Esta es la recta del 0 al 1.000.", "El *300* está justo en un cartel.", "El *650* está entre el 600 y el 700.", "El *900* está cerca del final."]},
 {"t": "consejo", "titulo": "MÁS A LA DERECHA", "texto": "Más a la derecha, más grande", "emoji": "➡️",
  "voz": ["Truco: en la recta, *más a la derecha*, más grande."]},
 {"t": "saltos", "titulo": "SALTOS EN LA RECTA", "min": 500, "max": 600, "cada": 10, "inicio": 520, "saltos": [{"a": 30, "txt": "+30"}, {"a": -10, "txt": "−10"}],
  "voz": ["Empezamos en el 520.", "Saltamos 30 para adelante: llegamos al *550*.", "Volvemos 10: llegamos al *540*."]},
 {"t": "pregunta", "pregunta": "¿Entre qué cientos está el 470?", "opciones": ["400 y 500", "300 y 400", "500 y 600"], "correcta": 0,
  "voz": ["Ahora vos. Mirá el 470 en la recta.", "¿Entre qué cientos está?", "¡Entre el *400* y el *500*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál está más a la derecha?", "opciones": ["780", "870"], "correcta": 1,
  "voz": ["Otra más. Pensá en la recta.", "¿Cuál está *más a la derecha*: 780 u 870?", "¡*870*! Es el mayor."]},
 {"t": "resumen", "items": [["LA RECTA", "del 0 al 1.000"], ["DERECHA", "más grande"], ["ENTRE", "dos cientos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La recta va *del 0 al 1.000*.", "*Más a la derecha*, más grande.", "Cada número está *entre dos cientos*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m4-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 4 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
