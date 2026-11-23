# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 1 · La serie numérica hasta 200: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (sueltos, paquetes de 10 y cajas de 100).
Regla de primeros años (tools/medio/primeros_anios.py). Genera tools/medio/clase/lecciones/medio-mat2-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'ea008220-181d-4188-9a4a-56e1ecc0a9cf', 2: 'ed3381db-ac71-45f3-a7a3-1d4d27bf613b', 3: 'd5735aa5-13a9-41bc-9874-b8c5cd2af2af', 4: '14d43acc-8ba8-43ac-8f96-560f5cad6171'}
TIT = {1: 'Contar hasta 100 y más', 2: 'Hasta 200', 3: 'Escalas de 10 en 10', 4: 'Series que suben y bajan'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["La abuela Rosa hace alfajores.", "Hoy hizo muchísimos.", "¿Pasará del 100?"], "titulo": "CONTAR", "sub": "hasta 100 y más",
  "voz": ["La abuela Rosa tiene una *fábrica de alfajores*.", "Hoy hizo muchísimos alfajores.", "¿Puede contar más de 100?", "Hoy: *contar hasta 100 y más*."]},
 {"t": "cuadro", "hasta": 100, "desde": 0, "faltan": [100], "titulo": "DEL 0 AL 100",
  "voz": ["Mirá el cuadro de los números.", "Los redondos: 10, 20, 30, 40, 50.", "¡Y el último es el *100*!"]},
 {"t": "agrupar", "niveles": [{"nombre": "UNIDAD", "valor": "1", "icono": "alf"}, {"nombre": "DECENA", "valor": "10", "icono": "pack"}, {"nombre": "CIEN", "valor": "100", "icono": "caja"}], "salto": "×10",
  "voz": ["Un alfajor suelto es una *unidad*.", "10 alfajores llenan un paquete: una *decena*.", "10 paquetes llenan una caja.", "¡Una caja tiene *100 alfajores*!"]},
 {"t": "tren", "desde": 98, "hasta": 105, "faltan": [101], "titulo": "DESPUÉS DEL 100",
  "voz": ["El tren no se frena en el 100.", "98, 99, 100… 102, 103, 104, 105.", "¡Faltaba el *101*! Ciento uno."]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["107", "108", "109"], "falta": "110", "regla": "Sumamos 1 cada vez",
  "voz": ["Mirá: 107, 108, 109…", "¿Qué número sigue?", "¡El *110*! Ciento diez."]},
 {"t": "quiz4", "pregunta": "¿Qué número viene después del 100?", "opciones": ["101", "200", "1001"], "correcta": 0,
  "voz": ["Ahora vos. Rosa cuenta: 99, 100…", "¿Qué número viene después?", "¡El *101*! Seguimos de a uno."]},
 {"t": "errores", "items": [{"mal": "Después del 100, el 200", "bien": "Después del 100, el 101"}],
  "voz": ["Ojo con este error.", "Después del 100 viene el *101*."]},
 {"t": "resumen", "items": [["DECENA", "paquete de 10"], ["CIEN", "10 paquetes"], ["DESPUÉS", "101, 102, 103"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *decena* es un paquete de 10.", "*10 paquetes* son 100.", "Después del 100 seguimos: *101, 102*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué número viene después del 199?", "segundos": 5, "respuesta": "¡El 200!", "emoji": "📦", "titulo": "HASTA", "sub": "el 200",
  "voz": ["Desafío: ¿qué viene después del 199?", "¡El *200*! Doscientos.", "Hoy: *los números hasta 200*."]},
 {"t": "cdu", "c": 1, "d": 4, "u": 3, "texto": "¡Son 143 alfajores!",
  "voz": ["Mirá el pedido de Rosa.", "La caja: 100.", "Los paquetes: 110, 120, 130, 140.", "Los sueltos: 141, 142, 143.", "¡Son *143 alfajores*!"]},
 {"t": "consejo", "titulo": "EN ORDEN", "texto": "Caja, paquetes, sueltos", "emoji": "📦",
  "voz": ["Truco: primero la caja, después paquetes y sueltos."]},
 {"t": "deslizador", "titulo": "DEL 100 AL 200", "min": 100, "max": 200, "emoji": "🍫", "paradas": [{"v": 100, "txt": "una caja"}, {"v": 150, "txt": "en el medio"}, {"v": 200, "txt": "dos cajas"}],
  "voz": ["Empezamos en el *100*: una caja.", "Movemos hasta el *150*: justo en el medio.", "¡Y llegamos al *200*: dos cajas!"]},
 {"t": "tren", "desde": 193, "hasta": 200, "faltan": [200], "titulo": "LLEGAMOS AL 200",
  "voz": ["Contemos los últimos vagones.", "193, 194, 195, 196, 197, 198, 199.", "¡Y el último es el *200*!"]},
 {"t": "pistas", "problema": "Rosa tiene 1 caja, 6 paquetes y 2 sueltos. ¿Cuántos son?", "pistas": ["La caja: 100", "6 paquetes: 60", "2 sueltos: 2"], "respuesta": "162 alfajores",
  "voz": ["Ahora vos. Una caja, seis paquetes, dos sueltos.", "Pista uno: la caja tiene *100*.", "Pista dos: seis paquetes son *60*.", "Pista tres: y dos sueltos.", "¡Son *162* alfajores!"]},
 {"t": "resumen", "items": [["CAJA", "100 alfajores"], ["CONTAR", "caja, paquetes, sueltos"], ["200", "dos cajas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *caja* tiene 100 alfajores.", "Contamos caja, paquetes y sueltos.", "Dos cajas son *200*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿contás de a uno?"}, {"yo": True, "txt": "¡No! De 10 en 10 🍫"}], "titulo": "DE 10", "sub": "en 10",
  "voz": ["Tomi, el nieto, le escribe a Rosa.", "¿Contás los alfajores de a uno?", "¡No! Rosa cuenta *de 10 en 10*."]},
 {"t": "saltos", "titulo": "UN PAQUETE MÁS", "min": 100, "max": 160, "cada": 10, "inicio": 120, "saltos": [{"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}],
  "voz": ["Empezamos en el 120.", "Un paquete más: *130*.", "Otro paquete: *140*.", "Otro más: *150*."]},
 {"t": "tren", "desde": 110, "hasta": 200, "paso": 10, "faltan": [150, 180], "titulo": "DE 10 EN 10",
  "voz": ["El tren cuenta de 10 en 10.", "110, 120, 130, 140, 160, 170, 190, 200.", "¡Faltaban el *150* y el *180*!"]},
 {"t": "pizarra", "titulo": "LA CIFRA DEL MEDIO", "lineas": [{"txt": "113"}, {"txt": "123", "color": "sol", "marca": "circulo"}, {"txt": "133", "color": "verde", "marca": "subraya"}],
  "voz": ["Rosa escribe en la pizarra: 113.", "Un paquete más: 123. ¡Cambió la del medio!", "Otro más: 133. El 3 del final no cambia."]},
 {"t": "pregunta", "pregunta": "De 10 en 10: 113, 123, ¿qué sigue?", "opciones": ["133", "124", "223"], "correcta": 0,
  "voz": ["Ahora vos. 113, 123…", "¿Qué número sigue de 10 en 10?", "¡*133*! El 3 del final no cambia."]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "140 y 10 más", "r": "150"}, {"p": "170 y 10 más", "r": "180"}, {"p": "190 y 10 más", "r": "200"}],
  "voz": ["¡Ronda rápida de 10 en 10!", "140 y 10 más: *150*.", "170 y 10 más: *180*.", "190 y 10 más: ¡*200*!"]},
 {"t": "errores", "items": [{"mal": "190 y después 1100", "bien": "190 y después 200"}],
  "voz": ["Ojo con este error.", "Después del 190 viene el *200*."]},
 {"t": "resumen", "items": [["DE 10 EN 10", "un paquete más"], ["CAMBIA", "las decenas"], ["NO CAMBIA", "las unidades"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "De 10 en 10 sumamos *un paquete*.", "Cambia la cifra de las *decenas*.", "Las *unidades* quedan igual.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡El camión va para atrás!", "bajada": "Reparte de 10 en 10", "emoji": "🚚", "titulo": "SUBEN", "sub": "y bajan",
  "voz": ["¡Último momento en la fábrica de Rosa!", "El camión reparte y quedan menos alfajores.", "Hoy: *series que suben y bajan*."]},
 {"t": "comparar", "a": {"cab": "SUBE", "texto": "150, 151, 152", "emoji": "⬆️"}, "b": {"cab": "BAJA", "texto": "200, 190, 180", "emoji": "⬇️"}, "signo": "≠",
  "voz": ["Esta serie *sube*: suma uno cada vez.", "Esta serie *baja*: resta diez cada vez.", "¡Mirá si los números crecen o achican!"]},
 {"t": "saltos", "titulo": "PARA ATRÁS", "min": 140, "max": 200, "cada": 10, "inicio": 200, "saltos": [{"a": -10, "txt": "−10"}, {"a": -10, "txt": "−10"}, {"a": -10, "txt": "−10"}],
  "voz": ["El camión sale del 200.", "Reparte un paquete: *190*.", "Otro paquete: *180*.", "Otro más: *170*."]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["200", "190", "180"], "falta": "170", "regla": "Restamos 10 cada vez",
  "voz": ["Mirá esta serie: 200, 190, 180…", "¿Qué número sigue?", "¡El *170*! La serie baja de 10 en 10."]},
 {"t": "quiz4", "pregunta": "La serie 160, 150, 140, ¿sube o baja?", "opciones": ["Sube", "Baja"], "correcta": 1,
  "voz": ["Ahora vos. Mirá: 160, 150, 140.", "¿La serie sube o baja?", "¡*Baja*! Resta 10 cada vez."]},
 {"t": "pregunta", "pregunta": "Seguí: 125, 124, 123, ¿qué sigue?", "opciones": ["122", "124", "133"], "correcta": 0,
  "voz": ["Otra más. 125, 124, 123…", "¿Qué número sigue?", "¡*122*! Baja de a uno."]},
 {"t": "consejo", "titulo": "MIRÁ DOS NÚMEROS", "texto": "Crece: sube. Achica: baja", "emoji": "🔍",
  "voz": ["Truco: si crece, sube. Si achica, *baja*."]},
 {"t": "resumen", "items": [["SUBE", "sumamos"], ["BAJA", "restamos"], ["EL SALTO", "siempre igual"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una serie que *sube* suma.", "Una serie que *baja* resta.", "El salto es *siempre igual*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m1-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
