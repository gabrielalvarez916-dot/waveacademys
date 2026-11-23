# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 2 · Los números hasta 500: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (sueltos, paquetes de 10 y cajas de 100).
Regla de primeros años (tools/medio/primeros_anios.py). Genera tools/medio/clase/lecciones/medio-mat2-m2-n<N>.json.
Formatos nuevos contra la misión 1: fichas y calculadora."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'c10404aa-bbc6-4429-a4e8-3818661217c7', 2: '82be64b8-3357-4c49-84c3-28b5a05d8f77', 3: '1e6dc920-8612-4a01-82d9-79cb0459bc05', 4: '2d0ee16c-321a-444b-af4a-155b4a3fc16b'}
TIT = {1: 'Del 200 al 300', 2: 'Hasta 400', 3: 'Hasta 500', 4: 'Leer y escribir números grandes'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Llegó un pedido grande.", "Ya hay 2 cajas llenas.", "¿Cuántos alfajores son?"], "titulo": "DEL 200", "sub": "al 300",
  "voz": ["Llegó un *pedido grande* a la fábrica de Rosa.", "Ya hay dos cajas llenas.", "¿Cuántos alfajores son en total?", "Hoy: *del 200 al 300*."]},
 {"t": "cdu", "c": 2, "d": 4, "u": 6, "texto": "¡Son 246 alfajores!",
  "voz": ["Contemos el pedido de Rosa.", "Las cajas: 100, 200.", "Los paquetes: 210, 220, 230, 240.", "Los sueltos: 241, 242, 243, 244, 245, 246.", "¡Son *246 alfajores*!"]},
 {"t": "recta", "min": 200, "max": 300, "paso": 10, "marcas": [{"v": 250, "txt": "250"}, {"v": 300, "txt": "300"}],
  "voz": ["En la recta vamos del 200 al 300.", "En el medio está el *250*.", "Y al final, el *300*: tres cajas."]},
 {"t": "tren", "desde": 296, "hasta": 303, "faltan": [300], "titulo": "PASAMOS EL 300",
  "voz": ["Contemos estos vagones.", "296, 297, 298, 299… 301, 302, 303.", "¡Faltaba el *300*! Trescientos."]},
 {"t": "pregunta", "pregunta": "2 cajas, 7 paquetes y 1 suelto. ¿Cuántos son?", "opciones": ["271", "217", "721"], "correcta": 0,
  "voz": ["Ahora vos. Dos cajas, siete paquetes, un suelto.", "¿Cuántos alfajores son?", "¡*271*! Doscientos setenta y uno."]},
 {"t": "errores", "items": [{"mal": "Doscientos cinco: 2005", "bien": "Doscientos cinco: 205"}],
  "voz": ["Ojo con este error.", "Doscientos cinco se escribe *205*: tres cifras."]},
 {"t": "resumen", "items": [["200", "dos cajas"], ["CONTAR", "cajas, paquetes, sueltos"], ["300", "tres cajas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Dos cajas son *200*.", "Contamos cajas, paquetes y sueltos.", "Tres cajas son *300*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué número viene después del 399?", "segundos": 5, "respuesta": "¡El 400!", "emoji": "📦", "titulo": "HASTA", "sub": "el 400",
  "voz": ["Desafío: ¿qué viene después del 399?", "¡El *400*! Cuatrocientos.", "Hoy: *los números hasta 400*."]},
 {"t": "saltos", "titulo": "CAJA POR CAJA", "min": 0, "max": 400, "cada": 100, "inicio": 0, "saltos": [{"a": 100, "txt": "+100"}, {"a": 100, "txt": "+100"}, {"a": 100, "txt": "+100"}, {"a": 100, "txt": "+100"}],
  "voz": ["Contamos las cajas *de 100 en 100*.", "Una caja: *100*.", "Dos cajas: *200*.", "Tres cajas: *300*.", "¡Cuatro cajas: *400*!"]},
 {"t": "cdu", "c": 3, "d": 7, "u": 2, "texto": "¡Son 372 alfajores!",
  "voz": ["Mirá este pedido.", "Las cajas: 100, 200, 300.", "Los paquetes: 310, 320, 330, 340, 350, 360, 370.", "Los sueltos: 371, 372.", "¡Son *372 alfajores*!"]},
 {"t": "calculadora", "teclas": ["3", "9", "9", "+", "1"], "resultado": "400", "texto": "399 + 1 = 400", "titulo": "UNO MÁS",
  "voz": ["Tomi prueba con la calculadora.", "Aprieta 399, más 1.", "¡Sale *400*! Cuatro cajas justas."]},
 {"t": "pregunta", "pregunta": "De 100 en 100: 100, 200, 300, ¿qué sigue?", "opciones": ["400", "310", "3100"], "correcta": 0,
  "voz": ["Ahora vos. 100, 200, 300…", "¿Qué número sigue?", "¡*400*! Una caja más."]},
 {"t": "consejo", "titulo": "CONTÁ LAS CAJAS", "texto": "Cada caja suma 100", "emoji": "📦",
  "voz": ["Truco: cada *caja* suma 100 alfajores."]},
 {"t": "resumen", "items": [["DE 100 EN 100", "contar cajas"], ["PEDIDO", "cajas, paquetes, sueltos"], ["400", "cuatro cajas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las cajas se cuentan *de 100 en 100*.", "Un pedido tiene cajas, paquetes y sueltos.", "Cuatro cajas son *400*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, la escuela pide 500 🍫"}, {"yo": True, "txt": "¡Son 5 cajas!"}, {"yo": False, "txt": "¿Cómo sabés?"}], "titulo": "HASTA", "sub": "el 500",
  "voz": ["Tomi le escribe a Rosa.", "La escuela pide *500 alfajores*.", "Rosa sabe: ¡son cinco cajas!", "Hoy: *los números hasta 500*."]},
 {"t": "agrupar", "niveles": [{"nombre": "DECENA", "valor": "10", "icono": "pack"}, {"nombre": "CENTENA", "valor": "100", "icono": "caja"}], "salto": "×10",
  "voz": ["Un paquete tiene *10* alfajores.", "10 paquetes llenan una caja de *100*.", "¡Cinco cajas así son *500*!"]},
 {"t": "tren", "desde": 100, "hasta": 500, "paso": 100, "titulo": "CINCO CAJAS",
  "voz": ["Los camiones llevan una caja cada uno.", "100, 200, 300, 400, 500.", "¡Cinco cajas: *500*!"]},
 {"t": "recta", "min": 400, "max": 500, "paso": 10, "marcas": [{"v": 450, "txt": "450"}, {"v": 490, "txt": "490"}],
  "voz": ["Ahora de 10 en 10, del 400 al 500.", "Acá está el *450*.", "Y acá el *490*: falta un paquete."]},
 {"t": "pregunta", "pregunta": "¿Qué número viene antes del 500?", "opciones": ["499", "501", "400"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el 500.", "¿Qué número viene *antes*?", "¡*499*! Uno menos."]},
 {"t": "errores", "items": [{"mal": "Quinientos: 5100", "bien": "Quinientos: 500"}],
  "voz": ["Ojo con este error.", "Quinientos se escribe *500*: tres cifras."]},
 {"t": "resumen", "items": [["500", "cinco cajas"], ["DE 10 EN 10", "un paquete más"], ["499", "antes del 500"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cinco cajas son *500*.", "De 10 en 10 sumamos *un paquete*.", "Antes del 500 viene el *499*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Se borraron las etiquetas!", "bajada": "Rosa escribe los números", "emoji": "🏷️", "titulo": "LEER", "sub": "y escribir",
  "voz": ["¡Último momento: se borraron las etiquetas!", "Rosa tiene que escribir los números otra vez.", "Hoy: *leer y escribir números grandes*."]},
 {"t": "fichas", "fichas": ["2", "5", "8"], "grande": "258", "etiqueta": "DOSCIENTOS CINCUENTA Y OCHO",
  "voz": ["Mirá estas tres cifras: 2, 5 y 8.", "Juntas forman el *258*.", "Se lee: *doscientos cincuenta y ocho*."]},
 {"t": "comparar", "a": {"cab": "SE ESCRIBE", "texto": "307", "emoji": "✏️"}, "b": {"cab": "SE LEE", "texto": "trescientos siete", "emoji": "🗣️"}, "signo": "=",
  "voz": ["Con cifras se escribe: *307*.", "Con palabras se lee: *trescientos siete*.", "¡Es el mismo número!"]},
 {"t": "consejo", "titulo": "MIRÁ EL CERO", "texto": "El 0 guarda el lugar", "emoji": "0️⃣",
  "voz": ["Truco: el *cero* guarda el lugar vacío."]},
 {"t": "fichas", "fichas": ["4", "5", "0"], "grande": "450", "etiqueta": "CUATROCIENTOS CINCUENTA",
  "voz": ["Ahora, *cuatrocientos cincuenta*.", "Un 4, un 5 y un 0: *450*.", "No hay unidades: va un cero."]},
 {"t": "pregunta", "pregunta": "¿Cómo se escribe trescientos seis?", "opciones": ["36", "306", "3006"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cómo se escribe *trescientos seis*?", "Pensá: ¿hay decenas?", "¡*306*! El cero va en el medio."]},
 {"t": "errores", "items": [{"mal": "Trescientos siete: 3007", "bien": "Trescientos siete: 307"}],
  "voz": ["Ojo con este error.", "Son *tres cifras*: 307."]},
 {"t": "resumen", "items": [["ESCRIBIR", "con cifras: 258"], ["LEER", "con palabras"], ["EL CERO", "guarda el lugar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Escribimos con *cifras*: 258.", "Leemos con *palabras*: doscientos cincuenta y ocho.", "El *cero* guarda el lugar vacío.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m2-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 2 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
