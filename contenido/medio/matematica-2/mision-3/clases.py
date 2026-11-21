# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 3 · Los números hasta 1.000: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (sueltos, paquetes de 10 y cajas de 100).
Regla de primeros años (tools/medio/primeros_anios.py). Genera tools/medio/clase/lecciones/medio-mat2-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'f6d0f3e9-bced-4b67-be01-3ff3f5996026', 2: '0740802b-f444-4c4e-9be6-0f7eac8b275a', 3: '00342da5-caa9-4192-947f-cc373c8a8b3e', 4: '083d5306-b626-406f-8b81-47d1d859237a'}
TIT = {1: 'Las centenas', 2: 'Hasta 1.000', 3: 'Leer y escribir hasta 1.000', 4: 'Centenas, decenas y unidades'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["La abuela Rosa hace alfajores.", "Los guarda en paquetes y cajas.", "¿Cuántos hay?"], "titulo": "LAS CENTENAS", "sub": "grupos de 100",
  "voz": ["La abuela Rosa tiene una *fábrica de alfajores*.", "Los guarda en paquetes y en cajas.", "¿Cómo sabe cuántos hay? ¡Vamos a ver!", "Hoy: *las centenas*."]},
 {"t": "agrupar", "niveles": [{"nombre": "UNIDAD", "valor": "1", "icono": "alf"}, {"nombre": "DECENA", "valor": "10", "icono": "pack"}, {"nombre": "CENTENA", "valor": "100", "icono": "caja"}], "salto": "×10",
  "voz": ["Un alfajor suelto es una *unidad*.", "10 alfajores llenan un paquete: una *decena*.", "10 paquetes llenan una caja: una *centena*.", "¡Una caja tiene *100 alfajores*!"]},
 {"t": "consejo", "titulo": "10 DECENAS", "texto": "10 paquetes de 10 son 100", "emoji": "📦",
  "voz": ["Truco: *10 decenas* forman *1 centena*."]},
 {"t": "cdu", "c": 4, "d": 0, "u": 0, "texto": "4 centenas son 400",
  "voz": ["Rosa llenó varias cajas. ¡Contemos!", "100, 200, 300, 400.", "No hay paquetes sueltos.", "Tampoco hay alfajores sueltos.", "¡*4 cajas* son *400* alfajores!"]},
 {"t": "recta", "min": 0, "max": 1000, "paso": 100, "marcas": [{"v": 300, "txt": "300"}, {"v": 800, "txt": "800"}],
  "voz": ["En la recta contamos *de 100 en 100*.", "Acá está el *300*: tres centenas.", "Y acá el *800*: ocho centenas."]},
 {"t": "pregunta", "pregunta": "¿Cuántos alfajores hay en 5 cajas de 100?", "opciones": ["5", "50", "500"], "correcta": 2,
  "voz": ["Ahora vos. Rosa tiene 5 cajas llenas.", "¿Cuántos alfajores hay en total?", "¡*500*! Cinco centenas."]},
 {"t": "resumen", "items": [["UNIDAD", "1 suelto"], ["DECENA", "paquete de 10"], ["CENTENA", "caja de 100"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *unidad* es un suelto.", "Una *decena* es un paquete de 10.", "Una *centena* es una caja de 100.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué número viene después del 999?", "segundos": 5, "respuesta": "¡El 1.000!", "emoji": "🏭", "titulo": "HASTA", "sub": "el 1.000",
  "voz": ["Desafío: ¿qué número viene después del 999?", "¡El *1.000*! Mil.", "Hoy: *los números hasta 1.000*."]},
 {"t": "cdu", "c": 2, "d": 3, "u": 5, "texto": "¡Son 235 alfajores!",
  "voz": ["Mirá lo que preparó Rosa hoy.", "Las cajas: 100, 200.", "Los paquetes: 210, 220, 230.", "Los sueltos: 231, 232, 233, 234, 235.", "¡Son *235 alfajores*!"]},
 {"t": "consejo", "titulo": "DE 10 EN 10", "texto": "Contá paquetes: 10, 20, 30…", "emoji": "🔟",
  "voz": ["Truco: los paquetes se cuentan *de 10 en 10*."]},
 {"t": "saltos", "titulo": "DE 10 EN 10", "min": 300, "max": 400, "cada": 10, "inicio": 340, "saltos": [{"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}],
  "voz": ["Contemos de 10 en 10 desde el 340.", "*350*.", "*360*.", "*370*."]},
 {"t": "agrupar", "niveles": [{"nombre": "CENTENA", "valor": "100", "icono": "caja"}, {"nombre": "UNIDAD DE MIL", "valor": "1.000", "icono": "camion"}], "salto": "×10",
  "voz": ["Una caja tiene *100* alfajores.", "¡Y 10 cajas llenan un camión!", "Un camión lleva *1.000* alfajores: ¡mil!"]},
 {"t": "pregunta", "pregunta": "¿Qué número viene después del 499?", "opciones": ["500", "400", "4.100"], "correcta": 0,
  "voz": ["Ahora vos. ¿Qué número viene después del 499?", "Pensá: 497, 498, 499…", "¡El *500*! Cinco centenas."]},
 {"t": "resumen", "items": [["DE 10 EN 10", "contar paquetes"], ["DE 100 EN 100", "contar cajas"], ["1.000", "10 centenas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los paquetes se cuentan *de 10 en 10*.", "Las cajas se cuentan *de 100 en 100*.", "*10 centenas* son *1.000*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "🏷️", "final": "🔢", "titulo": "LEER Y ESCRIBIR", "sub": "hasta 1.000",
  "voz": ["Rosa escribe etiquetas para sus cajas.", "¿Cómo se escribe *trescientos cuarenta y cinco*?", "Hoy: *leer y escribir números hasta 1.000*."]},
 {"t": "fichas", "fichas": ["3", "4", "5"], "grande": "345", "etiqueta": "TRESCIENTOS CUARENTA Y CINCO",
  "voz": ["Tiene *tres cifras*: un 3, un 4 y un 5.", "Juntas forman el *345*.", "Se lee: *trescientos cuarenta y cinco*."]},
 {"t": "comparar", "a": {"cab": "SE ESCRIBE", "texto": "708", "emoji": "✏️"}, "b": {"cab": "SE LEE", "texto": "setecientos ocho", "emoji": "🗣️"}, "signo": "=",
  "voz": ["Con cifras se escribe: *708*.", "Con palabras se lee: *setecientos ocho*.", "¡Es el mismo número!"]},
 {"t": "errores", "items": [{"mal": "Escribir 7008", "bien": "708: el 0 guarda el lugar"}],
  "voz": ["Ojo con este error.", "Setecientos ocho es *708*: el cero guarda el lugar."]},
 {"t": "fichas", "fichas": ["9", "1", "0"], "grande": "910", "etiqueta": "NOVECIENTOS DIEZ",
  "voz": ["Ahora, *novecientos diez*.", "Un 9, un 1 y un 0: *910*.", "Se lee *novecientos diez*."]},
 {"t": "pregunta", "pregunta": "¿Cómo se escribe quinientos seis?", "opciones": ["56", "506", "5.006"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cómo se escribe *quinientos seis*?", "Pensá: ¿hay decenas?", "¡*506*! El cero va en las decenas."]},
 {"t": "consejo", "titulo": "MIRÁ EL CERO", "texto": "El 0 guarda un lugar vacío", "emoji": "0️⃣",
  "voz": ["Truco: el *cero* guarda el lugar que está vacío."]},
 {"t": "resumen", "items": [["ESCRIBIR", "con cifras: 345"], ["LEER", "con palabras"], ["EL CERO", "guarda el lugar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Escribimos con *cifras*: 345.", "Leemos con *palabras*: trescientos cuarenta y cinco.", "El *cero* guarda el lugar vacío.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa tiene que mandar un pedido.", "Son 243 alfajores.", "¿Cómo los arma?"], "titulo": "CENTENAS", "sub": "decenas y unidades",
  "voz": ["Rosa tiene que mandar un *pedido*.", "El cliente quiere 243 alfajores.", "¿Cuántas cajas, paquetes y sueltos arma?", "Hoy: *centenas, decenas y unidades*."]},
 {"t": "cdu", "c": 2, "d": 4, "u": 3, "texto": "2 centenas, 4 decenas y 3 unidades",
  "voz": ["Armamos el pedido de *243*.", "2 cajas: 100, 200.", "4 paquetes: 210, 220, 230, 240.", "3 sueltos: 241, 242, 243.", "¡*2 centenas, 4 decenas y 3 unidades*!"]},
 {"t": "estante", "numero": "243", "cab": ["CENTENAS", "DECENAS", "UNIDADES"], "dig": ["2", "4", "3"], "val": ["200", "40", "3"], "destacar": 0, "etiqueta": "CADA CIFRA EN SU LUGAR",
  "voz": ["Mirá el número *243*.", "Cada cifra va en su *lugar*.", "Centenas, decenas y unidades.", "El 2 vale *200*, el 4 vale *40*.", "¡Y el 3 vale *3*!"]},
 {"t": "descomponer", "numero": "243", "titulo": "DESARMAMOS EL 243", "partes": ["200", "40", "3"], "resultado": "= 243 ✓",
  "voz": ["Ahora *desarmamos* el 243.", "Lo escribimos como una suma.", "200, más 40, más 3.", "Cada parte sale de una cifra.", "200 más 40 más 3 es *243*."]},
 {"t": "pregunta", "pregunta": "¿Cuánto vale el 6 en 365?", "opciones": ["6", "60", "600"], "correcta": 1,
  "voz": ["Ahora vos. Mirá el número 365.", "¿Cuánto vale el *6*?", "¡*60*! Está en las decenas."]},
 {"t": "pregunta", "pregunta": "4 centenas y 7 unidades, ¿qué número es?", "opciones": ["47", "407", "470"], "correcta": 1,
  "voz": ["Otra más. Cuatro cajas y siete sueltos.", "¿Qué número es?", "¡*407*! El cero va en las decenas."]},
 {"t": "resumen", "items": [["CENTENAS", "cajas de 100"], ["DECENAS", "paquetes de 10"], ["UNIDADES", "sueltos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *centenas* son cajas de 100.", "Las *decenas* son paquetes de 10.", "Las *unidades* son los sueltos.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m3-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 3 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
