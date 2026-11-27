# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 11 · Multiplicar por 10, 100 y 1.000: las 4 clases animadas.
Metáfora de toda la misión: la imprenta de Valen (paquetes de 10, cajas de 100 y pallets de 1.000 hojas).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m11-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'fe9aa1b6-1fe0-436d-922c-803b6f2326f4', 2: 'd7116f69-70cb-4584-b77f-73a5a523fde5', 3: '6bff37bb-5bdc-4c56-af29-8a16d38570e6', 4: 'eb1bb9cb-6e78-450f-a099-c5f275fefd43'}
TIT = {1: 'Regularidad al multiplicar por 10, 100 y 1.000', 2: 'Multiplicar por 100 y por 1.000', 3: 'Multiplicar por números redondos', 4: 'Problemas con números redondos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
VALEN = {"nombre": "Valen", "emoji": "🧑‍🔧"}

N1 = [
 {"t": "historia", "personaje": VALEN, "lugar": "🖨️", "lineas": ["Valen trabaja en una imprenta.", "Arma paquetes de 10 hojas.", "Hoy armó 23 paquetes."], "titulo": "POR 10", "sub": "la regularidad",
  "voz": ["Valen trabaja en una *imprenta*.", "Arma paquetes de *10 hojas*.", "Hoy armó 23 paquetes. ¿Cuántas hojas son?", "Hoy: *multiplicar por 10, 100 y 1.000*."]},
 {"t": "estante", "numero": "230", "cab": ["CENTENAS", "DECENAS", "UNIDADES"], "dig": ["2", "3", "0"], "val": ["200", "30", "0"], "destacar": 1, "etiqueta": "23 × 10 = 230",
  "voz": ["23 por 10 es *230*.", "El 2 y el 3 se corren un lugar.", "El 3 pasa a las decenas.", "El 2 pasa a las centenas.", "¡Y en las unidades queda un *cero*!"]},
 {"t": "pizarra", "titulo": "LA REGLA", "lineas": [{"txt": "7 × 10 = 70"}, {"txt": "7 × 100 = 700"}, {"txt": "7 × 1.000 = 7.000", "color": "verde", "marca": "subraya"}],
  "voz": ["Mirá el 7: por 10 es *70*.", "Por 100 es *700*.", "¡Por 1.000 es *7.000*! Un cero, dos ceros, tres ceros."]},
 {"t": "quiz4", "pregunta": "¿Cuánto es 45 × 10?", "opciones": ["450", "4.500", "55"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuánto es 45 por 10?", "Agregamos *un cero*…", "¡*450*!"]},
 {"t": "errores", "items": [{"mal": "23 × 10 = 33", "bien": "23 × 10 = 230"}],
  "voz": ["Ojo con este error.", "Multiplicar por 10 no es *sumar* 10."]},
 {"t": "resumen", "items": [["× 10", "un cero"], ["× 100", "dos ceros"], ["× 1.000", "tres ceros"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Por 10, agregamos *un cero*.", "Por 100, *dos ceros*.", "Por 1.000, *tres ceros*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡La imprenta recibió 8 pallets!", "bajada": "Cada uno trae 1.000 hojas", "emoji": "📦", "titulo": "POR 100", "sub": "y por 1.000",
  "voz": ["¡Último momento: la imprenta recibió *8 pallets*!", "Cada pallet trae *1.000* hojas.", "Hoy: *multiplicar por 100 y por 1.000*."]},
 {"t": "agrupar", "niveles": [{"nombre": "PAQUETE", "valor": "10", "icono": "pack"}, {"nombre": "CAJA", "valor": "100", "icono": "caja"}, {"nombre": "PALLET", "valor": "1.000", "icono": "camion"}], "salto": "×10",
  "voz": ["Un paquete de la imprenta tiene *10* hojas.", "Diez paquetes forman una caja: *100*.", "¡Diez cajas forman un pallet: *1.000*!"]},
 {"t": "deslizador", "titulo": "PALLETS DE 1.000", "min": 0, "max": 8000, "emoji": "📦", "paradas": [{"v": 2000, "txt": "2 pallets"}, {"v": 5000, "txt": "5 pallets"}, {"v": 8000, "txt": "8 pallets"}],
  "voz": ["Dos pallets: 2 por 1.000, *2.000*.", "Cinco pallets: 5 por 1.000, *5.000*.", "¡Ocho pallets: *8.000* hojas!"]},
 {"t": "mazo", "titulo": "POR 100", "items": [{"frente": "4 × 100", "dorso": "400"}, {"frente": "36 × 100", "dorso": "3.600"}, {"frente": "50 × 100", "dorso": "5.000"}],
  "voz": ["4 por 100: agregamos dos ceros, *400*.", "36 por 100 es *3.600*.", "¡50 por 100 es *5.000*!"]},
 {"t": "errores", "items": [{"mal": "36 × 100 = 3.610", "bien": "36 × 100 = 3.600"}],
  "voz": ["Ojo con este error.", "Por 100 agregamos *dos ceros* al final."]},
 {"t": "resumen", "items": [["× 100", "dos ceros"], ["× 1.000", "tres ceros"], ["LAS CIFRAS", "se corren"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Por 100, agregamos *dos ceros*.", "Por 1.000, agregamos *tres ceros*.", "Las cifras se *corren* a la izquierda.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Valen", "emoji": "🧑‍🔧"}, "mensajes": [{"yo": False, "txt": "Necesito 4 cajas de 30 sobres"}, {"yo": True, "txt": "¿30 no está en la tabla?"}, {"yo": False, "txt": "¡Pero es 3 por 10!"}], "titulo": "POR REDONDOS", "sub": "20, 30, 40…",
  "voz": ["Valen escribe: necesito 4 cajas de *30 sobres*.", "¿El 30 no está en la tabla?", "¡Pero 30 es 3 por 10!", "Hoy: *multiplicar por números redondos*."]},
 {"t": "transforma", "titulo": "4 × 30", "pasos": [{"txt": "4 × 30"}, {"txt": "4 × 3 = 12", "nota": "la cuenta chica"}, {"txt": "12 × 10 = 120"}],
  "voz": ["Queremos 4 por 30.", "Primero la cuenta chica: 4 por 3, *12*.", "Después por 10: agregamos un cero. ¡*120*!"]},
 {"t": "escape", "titulo": "CANDADOS REDONDOS", "candados": [{"p": "6 × 20", "r": "120"}, {"p": "5 × 40", "r": "200"}, {"p": "7 × 30", "r": "210"}],
  "voz": ["¡Escape! Tres candados para abrir.", "6 por 20: 6 por 2 es 12, *120*.", "5 por 40: 5 por 4 es 20, *200*.", "7 por 30: 7 por 3 es 21, *210*.", "¡Escapamos!"]},
 {"t": "vof", "afirmacion": "5 × 40 = 20", "emoji": "🤔", "verdadero": False, "explicacion": "Es 200",
  "voz": ["¿Verdadero o falso? 5 por 40 es 20.", "No te olvides del cero…", "¡*Falso*! Es *200*."]},
 {"t": "errores", "items": [{"mal": "Olvidar el cero del final", "bien": "Cuenta chica y después el cero"}],
  "voz": ["Ojo con este error.", "Después de la cuenta chica, *agregamos el cero*."]},
 {"t": "resumen", "items": [["REDONDO", "número por 10"], ["CUENTA CHICA", "primero"], ["EL CERO", "al final"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un redondo es un número *por 10*.", "Primero hacemos la *cuenta chica*.", "Y al final agregamos *el cero*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "6 cajas con 40 cuadernos. ¿Cuántos cuadernos?", "segundos": 8, "respuesta": "¡240!", "emoji": "📚", "titulo": "PROBLEMAS", "sub": "con redondos",
  "voz": ["Desafío: 6 cajas con 40 cuadernos cada una.", "¿Cuántos cuadernos hay? ¡*240*!", "Hoy: *problemas con números redondos*."]},
 {"t": "flujo", "titulo": "CÓMO LO RESOLVEMOS", "items": [{"txt": "Grupos iguales", "emoji": "📦"}, {"txt": "6 × 4 = 24", "emoji": "✖️"}, {"txt": "Agrego el cero: 240", "emoji": "0️⃣"}, {"txt": "Respondo", "emoji": "✅"}],
  "voz": ["Son *grupos iguales*: multiplicamos.", "La cuenta chica: 6 por 4, *24*.", "Agregamos el cero: *240*.", "¡Respondemos: hay 240 cuadernos!"]},
 {"t": "pistas", "problema": "La imprenta hace 300 hojas por hora. ¿Cuántas en 3 horas?", "pistas": ["Son 3 grupos de 300", "3 × 3 = 9, y dos ceros"], "respuesta": "900",
  "voz": ["Hace 300 hojas por hora. ¿Y en 3 horas?", "Pista: son *3 grupos de 300*.", "Pista: 3 por 3 es 9, y agregamos *dos ceros*.", "¡Son *900* hojas!"]},
 {"t": "quiz4", "pregunta": "8 paquetes de 50 hojas. ¿Cuántas hojas?", "opciones": ["400", "58", "4.000"], "correcta": 0,
  "voz": ["Ahora vos: 8 paquetes de 50 hojas cada uno.", "8 por 5 es 40, y agregamos el cero…", "¡*400* hojas!"]},
 {"t": "errores", "items": [{"mal": "6 cajas de 40: 6 + 40 = 46", "bien": "6 × 40 = 240"}],
  "voz": ["Ojo con este error.", "Con grupos iguales, *multiplicamos*: no sumamos."]},
 {"t": "resumen", "items": [["GRUPOS", "multiplicar"], ["CUENTA CHICA", "y los ceros"], ["RESPONDER", "con oración"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Con grupos iguales, *multiplicamos*.", "Hacemos la cuenta chica y agregamos *los ceros*.", "Y respondemos *con una oración*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m11-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 11 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
