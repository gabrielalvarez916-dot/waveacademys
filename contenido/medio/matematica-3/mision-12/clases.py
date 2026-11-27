# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 12 · Multiplicación por una cifra: las 4 clases animadas.
Metáfora de toda la misión: la huerta de Nina (cajones con la misma cantidad de plantines).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m12-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '37ba5ec1-4ab0-4014-8f94-234a19aa8017', 2: '2626c786-2742-4bff-91da-2f24c7597f63', 3: '9ee3d124-24e6-4fab-abc0-19a5ded75ce3', 4: '9e879efd-0001-4e59-833b-e3c565c66778'}
TIT = {1: 'Multiplicar descomponiendo', 2: 'Multiplicar en columnas', 3: 'Multiplicar con reagrupamiento', 4: 'Controlar con estimaciones'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
NINA = {"nombre": "Nina", "emoji": "👩‍🌾"}

N1 = [
 {"t": "chat", "contacto": {"nombre": "Nina", "emoji": "👩‍🌾"}, "mensajes": [{"yo": False, "txt": "Tengo 4 cajones con 23 plantines"}, {"yo": True, "txt": "¡23 no está en la tabla!"}, {"yo": False, "txt": "Desarmémoslo"}], "titulo": "DESCOMPONER", "sub": "para multiplicar",
  "voz": ["Nina escribe: tengo 4 cajones con *23 plantines*.", "¡El 23 no está en la tabla!", "Desarmémoslo en partes.", "Hoy: *multiplicar descomponiendo*."]},
 {"t": "descomponer", "numero": "23", "titulo": "DESARMAMOS EL 23", "partes": ["20", "3"], "resultado": "= 23 ✓",
  "voz": ["Tomamos el *23* de los plantines.", "Tiene 2 decenas: *20*.", "Y tiene 3 unidades sueltas: *3*.", "20 más 3.", "¡Es 23!"]},
 {"t": "pizarra", "titulo": "4 × 23", "lineas": [{"txt": "4 × 20 = 80"}, {"txt": "4 × 3 = 12"}, {"txt": "80 + 12 = 92", "color": "verde", "marca": "circulo"}],
  "voz": ["Primero multiplicamos 4 por 20: *80*.", "Después multiplicamos 4 por 3: *12*.", "¡Sumamos: 80 más 12, *92* plantines!"]},
 {"t": "quiz4", "pregunta": "¿Cuánto es 3 × 14?", "opciones": ["42", "312", "17"], "correcta": 0,
  "voz": ["Ahora vos: 3 por 14.", "30 más 12…", "¡*42*!"]},
 {"t": "errores", "items": [{"mal": "4 × 23 = 4 × 20 = 80", "bien": "Falta 4 × 3: son 92"}],
  "voz": ["Ojo con este error.", "Hay que multiplicar *las dos partes*, no una sola."]},
 {"t": "resumen", "items": [["DESARMAR", "decenas y unidades"], ["MULTIPLICAR", "cada parte"], ["SUMAR", "las partes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Desarmamos* el número en decenas y unidades.", "Multiplicamos *cada parte*.", "Y al final *sumamos* las partes.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡La huerta tiene 3 canteros de 32 lechugas!", "bajada": "Nina las cuenta en columnas", "emoji": "🥬", "titulo": "EN COLUMNAS", "sub": "multiplicar",
  "voz": ["¡Último momento: la huerta tiene *3 canteros* de 32 lechugas!", "Nina las cuenta en columnas.", "Hoy: *multiplicar en columnas*."]},
 {"t": "tabla", "titulo": "32 × 3", "columnas": ["", "D", "U"], "filas": [["", "3", "2"], ["×", "", "3"], ["=", "9", "6"]],
  "voz": ["Ponemos el 32 arriba.", "El 3 va abajo, en las unidades.", "Unidades: 3 por 2, *6*. Decenas: 3 por 3, *9*.", "¡Son *96* lechugas!"]},
 {"t": "mazo", "titulo": "CIFRA POR CIFRA", "items": [{"frente": "21 × 4: unidades", "dorso": "4 × 1 = 4"}, {"frente": "21 × 4: decenas", "dorso": "4 × 2 = 8"}, {"frente": "21 × 4", "dorso": "84"}],
  "voz": ["Unidades: 4 por 1, *4*.", "Decenas: 4 por 2, *8*.", "¡21 por 4 es *84*!"]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "21 × 4", "r": "84"}, {"p": "13 × 3", "r": "39"}, {"p": "42 × 2", "r": "84"}],
  "voz": ["¡Ronda rápida en columnas!", "21 por 4 es *84*.", "13 por 3 es *39*.", "42 por 2 es *84*."]},
 {"t": "errores", "items": [{"mal": "Multiplicar solo las unidades", "bien": "Multiplicar todas las cifras"}],
  "voz": ["Ojo con este error.", "El número de abajo multiplica a *todas* las cifras."]},
 {"t": "resumen", "items": [["ABAJO", "en las unidades"], ["EMPEZAR", "por las unidades"], ["TODAS", "las cifras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El número chico va *abajo*, en las unidades.", "Empezamos por las *unidades*.", "Multiplicamos *todas* las cifras.", CIERRE]},
]
N3 = [
 {"t": "historia", "personaje": NINA, "lugar": "🌱", "lineas": ["Nina tiene 4 bandejas de 47 semillas.", "7 por 4 da 28.", "¡No entra en una columna!"], "titulo": "ME LLEVO", "sub": "al multiplicar",
  "voz": ["Nina tiene 4 bandejas de *47 semillas*.", "En las unidades, 7 por 4 da *28*.", "¡No entra en una sola columna!", "Hoy: *multiplicar con reagrupamiento*."]},
 {"t": "tabla", "titulo": "47 × 4", "columnas": ["", "C", "D", "U"], "filas": [["", "", "²4", "7"], ["×", "", "", "4"], ["=", "1", "8", "8"]],
  "voz": ["Unidades: 7 por 4, 28.", "Escribo 8 y *me llevo 2*.", "Decenas: 4 por 4, 16, más 2: *18*.", "¡Son *188* semillas!"]},
 {"t": "balanza", "izq": {"cab": "SIN LLEVAR", "items": ["47 × 4 = 168"]}, "der": {"cab": "LLEVANDO", "items": ["47 × 4 = 188"]}, "gana": "der",
  "voz": ["Si nos olvidamos lo que llevamos, da 168.", "Si lo sumamos, da *188*.", "¡La correcta es *188*!"]},
 {"t": "prediccion", "pregunta": "25 × 3: ¿me llevo algo?", "a": {"txt": "Sí: 1", "emoji": "😎"}, "b": {"txt": "No", "emoji": "🤔"}, "correcta": "a", "resultado": "¡5 × 3 = 15: me llevo 1!",
  "voz": ["25 por 3: ¿nos llevamos algo?", "5 por 3 da 15…", "¡Sí: escribimos 5 y *nos llevamos 1*! Da 75."]},
 {"t": "errores", "items": [{"mal": "Olvidar sumar lo que me llevo", "bien": "Sumarlo después de multiplicar"}],
  "voz": ["Ojo con este error.", "Lo que nos llevamos se *suma* después de multiplicar."]},
 {"t": "resumen", "items": [["PASA DE 9", "me llevo"], ["ANOTO", "arriba"], ["SUMO", "después de multiplicar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Si da más de 9, *nos llevamos* las decenas.", "Lo *anotamos* arriba, chiquito.", "Y lo *sumamos* después de multiplicar.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "Nina calculó 38 × 6 = 2.280. ¿Puede ser?", "segundos": 8, "respuesta": "¡No! Da cerca de 240", "emoji": "🔍", "titulo": "CONTROLAR", "sub": "estimando",
  "voz": ["Desafío: Nina calculó 38 por 6 y le dio *2.280*.", "¡No puede ser! Da cerca de *240*.", "Hoy: *controlar con estimaciones*."]},
 {"t": "transforma", "titulo": "ESTIMAMOS", "pasos": [{"txt": "38 × 6"}, {"txt": "40 × 6", "nota": "redondeamos"}, {"txt": "CERCA DE 240"}],
  "voz": ["Tenemos 38 por 6.", "El 38 está cerca del *40*: 40 por 6.", "¡Da cerca de *240*!"]},
 {"t": "dato", "numero": "228", "antes": "38 × 6", "despues": "cerca de 240", "texto": "La cuenta exacta", "emoji": "✅",
  "voz": ["La cuenta exacta da *228*.", "Está cerca de 240: ¡tiene sentido!"]},
 {"t": "unir", "titulo": "¿CERCA DE CUÁNTO?", "pares": [["19 × 5", "cerca de 100"], ["31 × 4", "cerca de 120"], ["52 × 3", "cerca de 150"]],
  "voz": ["Uní cada cuenta con su estimación.", "19 por 5: cerca de *100*.", "31 por 4: cerca de *120*.", "52 por 3: cerca de *150*."]},
 {"t": "errores", "items": [{"mal": "38 × 6 = 2.280", "bien": "Da cerca de 240: es 228"}],
  "voz": ["Ojo con este error.", "Si da *muy lejos* de lo estimado, revisá la cuenta."]},
 {"t": "resumen", "items": [["REDONDEAR", "a la decena"], ["ESTIMAR", "antes"], ["COMPARAR", "con la cuenta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Redondeamos* a la decena más cercana.", "*Estimamos* antes de calcular.", "Y *comparamos* con la cuenta exacta.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m12-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 12 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
