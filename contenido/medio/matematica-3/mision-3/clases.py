# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 3 · Valor posicional con miles: las 4 clases animadas.
Metáfora de toda la misión: la tienda de bloques de Mía (cubitos, barras de 10, placas de 100 y cubos de 1.000).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '2c99ef28-e290-43f0-86d0-de1f07a0a672', 2: 'df63ef73-1ba9-4820-a13e-350e3944787b', 3: 'dbadd26d-01cd-4343-b401-7cabfc436689', 4: 'f72af676-4d91-4baf-bba5-3217b04e5ac9'}
TIT = {1: 'Unidades, decenas, centenas y miles', 2: 'Descomponer con sumas', 3: 'Armar números con tarjetas', 4: 'Cambiar una cifra y ver qué pasa'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
MIA = {"nombre": "Mía", "emoji": "👧"}

N1 = [
 {"t": "chat", "contacto": {"nombre": "Mía", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "Tengo bloques de todos los tamaños"}, {"yo": True, "txt": "¿Cuántos cubitos hay en total?"}, {"yo": False, "txt": "¡Contemos juntos!"}], "titulo": "LOS CUATRO", "sub": "lugares",
  "voz": ["Mía tiene bloques de *todos los tamaños*.", "¿Cuántos cubitos hay en total?", "¡Contemos juntos!", "Hoy: *unidades, decenas, centenas y miles*."]},
 {"t": "zoom", "niveles": [{"emoji": "🟫", "txt": "1 cubito"}, {"emoji": "📏", "txt": "barra: 10"}, {"emoji": "🟧", "txt": "placa: 100"}, {"emoji": "📦", "txt": "cubo: 1.000"}],
  "voz": ["Un *cubito* vale 1.", "Diez cubitos forman una *barra*: 10.", "Diez barras forman una *placa*: 100.", "¡Diez placas forman un *cubo*: 1.000!"]},
 {"t": "estante", "numero": "2.476", "cab": ["MILES", "CENTENAS", "DECENAS", "UNIDADES"], "dig": ["2", "4", "7", "6"], "val": ["2.000", "400", "70", "6"], "destacar": 0, "etiqueta": "CADA CIFRA EN SU LUGAR",
  "voz": ["Mía tiene 2 cubos y 4 placas.", "Y también 7 barras y 6 cubitos.", "Es el *2.476*.", "El 2 de los miles vale *2.000*.", "El 4 de las centenas vale *400*.", "¡El 7 vale 70 y el 6 vale 6!"]},
 {"t": "quiz4", "pregunta": "¿Cuánto vale el 5 en 5.381?", "opciones": ["5", "500", "5.000"], "correcta": 2,
  "voz": ["Ahora vos: ¿cuánto vale el 5 en 5.381?", "Está en el lugar de los miles…", "¡Vale *5.000*!"]},
 {"t": "errores", "items": [{"mal": "En 3.814, el 8 vale 8", "bien": "En 3.814, el 8 vale 800"}],
  "voz": ["Ojo con este error.", "El 8 está en las *centenas*: vale 800."]},
 {"t": "resumen", "items": [["CUBITO", "1"], ["BARRA Y PLACA", "10 y 100"], ["CUBO", "1.000"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *cubito* vale 1.", "Una *barra* vale 10 y una *placa*, 100.", "¡Un *cubo* vale 1.000!", CIERRE]},
]
N2 = [
 {"t": "gancho", "emoji": "📦", "final": "✂️", "titulo": "DESCOMPONER", "sub": "con sumas",
  "voz": ["Mía guarda sus bloques en cajas separadas.", "¿Cómo desarmamos un número grande?", "Hoy: *descomponer con sumas*."]},
 {"t": "descomponer", "numero": "3.608", "titulo": "DESARMAMOS EL 3.608", "partes": ["3.000", "600", "8"], "resultado": "= 3.608 ✓",
  "voz": ["Tomamos el número *3.608*.", "El 3 de los miles vale *3.000*.", "El 6 de las centenas vale *600*.", "No hay decenas. El 8 vale *8*.", "3.000 + 600 + 8 = *3.608*."]},
 {"t": "definicion", "palabra": "Descomponer", "texto": "Escribir un número como suma del valor de cada cifra.", "emoji": "➕",
  "voz": ["*Descomponer* es escribir el número como una suma.", "Sumamos lo que vale *cada cifra*."]},
 {"t": "mazo", "titulo": "DE LA SUMA AL NÚMERO", "items": [{"frente": "5.000 + 200 + 40 + 1", "dorso": "5.241"}, {"frente": "7.000 + 30", "dorso": "7.030"}, {"frente": "9.000 + 900 + 9", "dorso": "9.909"}],
  "voz": ["5.000 + 200 + 40 + 1 es *5.241*.", "7.000 + 30 es *7.030*: los ceros guardan lugar.", "¡9.000 + 900 + 9 es *9.909*!"]},
 {"t": "errores", "items": [{"mal": "7.000 + 30 = 730", "bien": "7.000 + 30 = 7.030"}],
  "voz": ["Ojo con este error.", "Son *cuatro cifras*: 7.030."]},
 {"t": "resumen", "items": [["DESCOMPONER", "en una suma"], ["CADA CIFRA", "con su valor"], ["EL CERO", "guarda el lugar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Descomponer* es armar una suma.", "Cada cifra va con *su valor*.", "Y el *cero* guarda el lugar.", CIERRE]},
]
N3 = [
 {"t": "historia", "personaje": MIA, "lugar": "🃏", "lineas": ["Mía tiene cuatro tarjetas: 3, 8, 1 y 6.", "Quiere armar el número más grande.", "¿Cómo las pone?"], "titulo": "ARMAR NÚMEROS", "sub": "con tarjetas",
  "voz": ["Mía tiene cuatro tarjetas: 3, 8, 1 y 6.", "Quiere armar el número *más grande*.", "¿Cómo las pone?", "Hoy: *armar números con tarjetas*."]},
 {"t": "fichas", "fichas": ["8", "6", "3", "1"], "grande": "8.631", "etiqueta": "EL MÁS GRANDE",
  "voz": ["En los miles va la cifra *más grande*: el 8.", "Después el 6, el 3 y el 1.", "¡El más grande es *8.631*!"]},
 {"t": "fichas", "fichas": ["1", "3", "6", "8"], "grande": "1.368", "etiqueta": "EL MÁS CHICO",
  "voz": ["Para el más chico, al revés.", "En los miles va la *más chica*: el 1.", "¡El más chico es *1.368*!"]},
 {"t": "vof", "afirmacion": "Con 2, 9, 4 y 7, el más grande es 2.947", "emoji": "🤔", "verdadero": False, "explicacion": "Es 9.742",
  "voz": ["¿Verdadero o falso?", "Con 2, 9, 4 y 7, el mayor es 2.947.", "Mirá qué cifra va en los miles…", "¡*Falso*! Es *9.742*."]},
 {"t": "errores", "items": [{"mal": "El más chico empieza con la cifra más grande", "bien": "El más chico empieza con la cifra más chica"}],
  "voz": ["Ojo con este error.", "El más chico empieza con la cifra *más chica*."]},
 {"t": "resumen", "items": [["EL MÁS GRANDE", "la mayor adelante"], ["EL MÁS CHICO", "la menor adelante"], ["LOS MILES", "deciden"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Para el más grande, la cifra *mayor* adelante.", "Para el más chico, la *menor* adelante.", "¡Los *miles* deciden!", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "Mía tiene 3.452 cubitos. Le dan un cubo de 1.000. ¿Cuántos tiene?", "segundos": 8, "respuesta": "¡4.452!", "emoji": "📦", "titulo": "CAMBIAR", "sub": "una cifra",
  "voz": ["Desafío: Mía tiene 3.452.", "Le dan un *cubo* de 1.000.", "¡*4.452*! Cambió solo una cifra.", "Hoy: *cambiar una cifra y ver qué pasa*."]},
 {"t": "transforma", "titulo": "SUMAMOS 100", "pasos": [{"txt": "3.452"}, {"txt": "+ UNA PLACA DE 100", "nota": "centenas"}, {"txt": "3.552"}],
  "voz": ["Tenemos el *3.452*.", "Le sumamos una *placa* de 100.", "¡Queda *3.552*! Cambió solo la cifra de las centenas."]},
 {"t": "comparar", "a": {"cab": "+ 10", "texto": "3.452 → 3.462", "emoji": "📏"}, "b": {"cab": "+ 1.000", "texto": "3.452 → 4.452", "emoji": "📦"}, "signo": "y",
  "voz": ["Si sumamos *10*, cambian las decenas: 3.462.", "Si sumamos *1.000*, cambian los miles: 4.452.", "¡Las demás cifras quedan *igual*!"]},
 {"t": "pistas", "problema": "¿Cuánto es 2.950 + 100?", "pistas": ["Cambian las centenas", "9 centenas y 1 más son 10"], "respuesta": "3.050",
  "voz": ["Un caso difícil: ¿cuánto es 2.950 + 100?", "Pista: cambian las *centenas*.", "Pista: 9 centenas y una más son 10.", "¡Se llena un mil!", "¡Es *3.050*!"]},
 {"t": "errores", "items": [{"mal": "4.271 + 10 = 5.271", "bien": "4.271 + 10 = 4.281"}],
  "voz": ["Ojo con este error.", "Sumar 10 cambia las *decenas*: 4.281."]},
 {"t": "resumen", "items": [["+ 1, + 10, + 100", "cambia un lugar"], ["+ 1.000", "cambian los miles"], ["SI LLEGA A 10", "pasa al lado"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Sumar 1, 10 o 100 cambia *un lugar*.", "Sumar 1.000 cambia los *miles*.", "Si llega a 10, *pasa al lugar de al lado*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m3-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 3 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
