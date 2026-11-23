# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 5 · Valor posicional con centenas: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (sueltos, paquetes de 10 y cajas de 100).
Regla de primeros años (tools/medio/primeros_anios.py). Genera tools/medio/clase/lecciones/medio-mat2-m5-n<N>.json.
Plantillas de plataformas de la misión: pizarra, quiz4, transforma, pistas, unir, patron."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'a06fa749-a97d-465e-81fc-cc4ca8b2a7ab', 2: '9a56b164-c90f-4a92-96a0-18f2c9606115', 3: '6b8b5d0b-2f18-41a2-b62c-79500881f437', 4: '318619af-234a-47ab-a260-8ac5b3726832'}
TIT = {1: 'El valor de cada cifra', 2: 'Descomponer en centenas, decenas y unidades', 3: 'Armar números a partir de sus partes', 4: 'Cambiar una cifra'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}
CDU = ["CENTENAS", "DECENAS", "UNIDADES"]

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa escribió 333.", "¡Tres treses iguales!", "¿Valen lo mismo?"], "titulo": "EL VALOR", "sub": "de cada cifra",
  "voz": ["Rosa escribió un número raro: *333*.", "¡Tiene tres treses iguales!", "¿Valen todos lo mismo?", "Hoy: *el valor de cada cifra*."]},
 {"t": "estante", "numero": "333", "cab": CDU, "dig": ["3", "3", "3"], "val": ["300", "30", "3"], "destacar": 0, "etiqueta": "CADA 3 EN SU LUGAR",
  "voz": ["Ponemos el 333 en el estante.", "Cada cifra va en su *lugar*.", "Centenas, decenas y unidades.", "El primer 3 vale *300*. El segundo, *30*.", "¡Y el último vale *3*!"]},
 {"t": "pizarra", "titulo": "EL 452", "lineas": [{"txt": "4 → 400", "color": "sol"}, {"txt": "5 → 50", "color": "coral", "marca": "circulo"}, {"txt": "2 → 2", "color": "verde"}],
  "voz": ["En el 452, el 4 vale *400*.", "El 5 vale *50*: está en las decenas.", "Y el 2 vale *2*."]},
 {"t": "consejo", "titulo": "MIRÁ EL LUGAR", "texto": "El lugar dice cuánto vale", "emoji": "📍",
  "voz": ["Truco: el *lugar* dice cuánto vale la cifra."]},
 {"t": "quiz4", "pregunta": "¿Cuánto vale el 7 en 718?", "opciones": ["7", "70", "700"], "correcta": 2,
  "voz": ["Ahora vos. Mirá el 718.", "¿Cuánto vale el *7*?", "¡*700*! Está en las centenas."]},
 {"t": "errores", "items": [{"mal": "En 452, el 5 vale 5", "bien": "En 452, el 5 vale 50"}],
  "voz": ["Ojo con este error.", "En 452, el 5 vale *50*."]},
 {"t": "resumen", "items": [["CENTENAS", "valen cientos"], ["DECENAS", "valen dieces"], ["UNIDADES", "valen unos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las cifras de las *centenas* valen cientos.", "Las de las *decenas* valen dieces.", "Las de las *unidades* valen unos.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Desarmá el 465 en cajas, paquetes y sueltos", "segundos": 8, "respuesta": "4 cajas, 6 paquetes, 5 sueltos", "emoji": "📦", "titulo": "DESARMAR", "sub": "números",
  "voz": ["Desafío: desarmá el 465.", "¡4 cajas, 6 paquetes y 5 sueltos!", "Hoy: *descomponer números*."]},
 {"t": "cdu", "c": 4, "d": 6, "u": 5, "texto": "4 centenas, 6 decenas, 5 unidades",
  "voz": ["Armamos el pedido de 465.", "Las cajas: 100, 200, 300, 400.", "Los paquetes: 410, 420, 430, 440, 450, 460.", "Los sueltos: 461, 462, 463, 464, 465.", "¡4 centenas, 6 decenas y 5 unidades!"]},
 {"t": "descomponer", "numero": "465", "titulo": "DESARMAMOS EL 465", "partes": ["400", "60", "5"], "resultado": "= 465 ✓",
  "voz": ["Ahora lo escribimos como *suma*.", "Cada cifra da una parte.", "400, más 60, más 5.", "Una parte por cifra.", "¡400 más 60 más 5 es *465*!"]},
 {"t": "transforma", "titulo": "CON UN CERO", "pasos": [{"txt": "708"}, {"txt": "700 + 0 + 8", "nota": "no hay paquetes"}, {"txt": "700 + 8"}],
  "voz": ["Mirá el *708*.", "Es 700, más 0, más 8.", "¡El cero no suma: *700 más 8*!"]},
 {"t": "pistas", "problema": "Desarmá el 738", "pistas": ["El 7 vale 700", "El 3 vale 30", "El 8 vale 8"], "respuesta": "700 + 30 + 8",
  "voz": ["Ahora vos. Desarmá el *738*.", "Pista uno: el 7 vale *700*.", "Pista dos: el 3 vale *30*.", "Pista tres: el 8 vale *8*.", "¡*700 más 30 más 8*!"]},
 {"t": "errores", "items": [{"mal": "465 = 4 + 6 + 5", "bien": "465 = 400 + 60 + 5"}],
  "voz": ["Ojo con este error.", "465 es *400 más 60 más 5*."]},
 {"t": "resumen", "items": [["DESARMAR", "escribir una suma"], ["PARTES", "una por cifra"], ["EL CERO", "no suma"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Desarmar* es escribir una suma.", "Cada cifra da *una parte*.", "El *cero* no suma nada.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, tengo 500 + 20 + 7"}, {"yo": True, "txt": "¡Armemos el número!"}, {"yo": False, "txt": "¿Cuál es?"}], "titulo": "ARMAR", "sub": "números",
  "voz": ["Tomi le escribe a Rosa.", "Tiene 500, más 20, más 7.", "Rosa le dice: ¡armemos el número!", "Hoy: *armar números con sus partes*."]},
 {"t": "cdu", "c": 5, "d": 2, "u": 7, "texto": "¡Es el 527!",
  "voz": ["Juntamos las partes de Tomi.", "500: cinco cajas. 100, 200, 300, 400, 500.", "20: dos paquetes. 510, 520.", "7 sueltos: 521, 522, 523, 524, 525, 526, 527.", "¡Es el *527*!"]},
 {"t": "unir", "titulo": "UNÍ CADA SUMA", "pares": [["300 + 40 + 5", "345"], ["600 + 8", "608"], ["200 + 90", "290"]],
  "voz": ["Uní cada suma con su número.", "300 más 40 más 5: *345*.", "600 más 8: *608*.", "200 más 90: *290*."]},
 {"t": "consejo", "titulo": "SI FALTA, UN 0", "texto": "El lugar vacío lleva 0", "emoji": "0️⃣",
  "voz": ["Truco: si falta una parte, va un *cero*."]},
 {"t": "quiz4", "pregunta": "¿Qué número es 800 + 50 + 1?", "opciones": ["851", "8.501", "158"], "correcta": 0,
  "voz": ["Ahora vos. 800, más 50, más 1.", "¿Qué número es?", "¡*851*! Ochocientos cincuenta y uno."]},
 {"t": "errores", "items": [{"mal": "600 + 8 = 68", "bien": "600 + 8 = 608"}],
  "voz": ["Ojo con este error.", "600 más 8 es *608*: va un cero."]},
 {"t": "resumen", "items": [["ARMAR", "juntar las partes"], ["CADA CIFRA", "a su lugar"], ["SI FALTA", "va un 0"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Armar* es juntar las partes.", "Cada cifra va a *su lugar*.", "Si falta una parte, va un *cero*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Llegó una caja más!", "bajada": "Cambió una cifra", "emoji": "🚚", "titulo": "CAMBIAR", "sub": "una cifra",
  "voz": ["¡Último momento: llegó una caja más!", "Rosa tenía 352. ¿Qué número cambió?", "Hoy: *cambiar una cifra*."]},
 {"t": "calculadora", "teclas": ["3", "5", "2", "+", "1", "0", "0"], "resultado": "452", "texto": "352 + 100 = 452", "titulo": "UNA CAJA MÁS",
  "voz": ["Rosa prueba con la calculadora.", "Aprieta 352, más 100.", "¡*452*! Solo cambió el primer número."]},
 {"t": "pizarra", "titulo": "UNA CIFRA POR VEZ", "lineas": [{"txt": "352 + 100 = 452", "color": "sol", "marca": "subraya"}, {"txt": "352 + 10 = 362", "color": "coral", "marca": "subraya"}, {"txt": "352 + 1 = 353", "color": "verde", "marca": "subraya"}],
  "voz": ["Más 100: cambian las *centenas*.", "Más 10: cambian las *decenas*.", "Más 1: cambian las *unidades*."]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["125", "135", "145"], "falta": "155", "regla": "Sumamos 10: cambian las decenas",
  "voz": ["Mirá: 125, 135, 145…", "¿Qué número sigue?", "¡*155*! Cambia la cifra del medio."]},
 {"t": "pregunta", "pregunta": "Rosa tiene 518. Llega una caja de 100. ¿Cuánto tiene?", "opciones": ["519", "528", "618"], "correcta": 2,
  "voz": ["Ahora vos. Rosa tiene 518.", "Llega una caja de 100. ¿Cuánto tiene?", "¡*618*! Cambiaron las centenas."]},
 {"t": "errores", "items": [{"mal": "352 + 100 = 353", "bien": "352 + 100 = 452"}],
  "voz": ["Ojo con este error.", "Más 100 cambia las *centenas*: 452."]},
 {"t": "resumen", "items": [["+ 100", "cambian centenas"], ["+ 10", "cambian decenas"], ["+ 1", "cambian unidades"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Más 100 cambia las *centenas*.", "Más 10 cambia las *decenas*.", "Más 1 cambia las *unidades*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m5-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 5 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
