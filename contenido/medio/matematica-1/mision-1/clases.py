# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 1 · Contar y comparar colecciones: las 4 clases animadas.
Metáfora de toda la misión: el cumple de Sofi. Regla de primeros años (tools/medio/primeros_anios.py).
Genera tools/medio/clase/lecciones/medio-mat1-m1-n<N>.json. Uso: python3 clases.py"""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '0fb43ae5-a858-4215-80a8-d6d7d79ff6ac', 2: '3f7aa6a4-8d30-49f0-a9bb-f16f608d01d8', 3: '4a4edbc8-87da-42de-b711-6e22b5687dc9', 4: 'a9e9bc77-044c-49c3-a195-6b17c0d028fb'}
TIT = {1: 'Contar objetos', 2: 'Más, menos e igual', 3: 'Comparar sin contar', 4: 'Armar colecciones iguales'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}

N1 = [
 {"t": "historia", "personaje": {"nombre": "Sofi", "emoji": "👧"}, "lugar": "🎂",
  "lineas": ["Mañana es el cumple de Sofi.", "Tiene que preparar todo.", "¿Cuántos globos tiene?"], "titulo": "CONTAR", "sub": "objetos",
  "voz": ["Mañana es el *cumple* de Sofi.", "Está feliz y tiene que preparar todo.", "Primero quiere saber cuántos globos tiene.", "Hoy vamos a aprender a *contar*."]},
 {"t": "contar", "titulo": "LOS GLOBOS", "emoji": "🎈", "cantidad": 5,
  "voz": ["Mirá los globos de Sofi.", "Contamos de a uno: 1, 2, 3, 4, 5.", "El último número dice cuántos hay: *5 globos*."]},
 {"t": "consejo", "titulo": "USÁ EL DEDO", "texto": "Tocá cada uno al contar", "emoji": "👉",
  "voz": ["Truco: tocá cada globo con el *dedo* al contar."]},
 {"t": "contar", "titulo": "LOS CHUPETINES", "emoji": "🍭", "cantidad": 8,
  "voz": ["Ahora, los chupetines para la mesa.", "Tocamos cada uno y decimos un número.", "¡Hay *8 chupetines*!"]},
 {"t": "errores", "items": [{"mal": "Contar uno dos veces", "bien": "Cada uno, una sola vez"}, {"mal": "Saltear uno", "bien": "Contar todos, sin apuro"}],
  "voz": ["Ojo con dos errores.", "No cuentes *dos veces* el mismo.", "Y no te *saltees* ninguno."]},
 {"t": "pregunta", "pregunta": "¿Cuántas coronas hay? 👑👑👑👑👑👑", "opciones": ["5", "6", "7"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cuántas coronas hay?", "Contalos con el dedo, despacio.", "¡Son *6 coronas*! ¡Muy bien!"]},
 {"t": "contar", "titulo": "LOS REGALOS", "emoji": "🎁", "cantidad": 10,
  "voz": ["Llegaron los regalos. ¡Cuántos!", "Contamos despacio, uno por uno.", "¡Hay *10 regalos*! Sofi está feliz."]},
 {"t": "resumen", "items": [["CONTAR", "de a uno, en orden"], ["EL DEDO", "toca cada objeto"], ["EL ÚLTIMO NÚMERO", "dice cuántos hay"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos *de a uno*, en orden.", "El *dedo* toca cada objeto.", "El *último número* dice cuántos hay.", "¡Muy bien! Ahora, *a practicar*."]},
]
N2 = [
 {"t": "reto", "texto": "Juan: 🍬🍬🍬🍬   Sofi: 🍬🍬  ¿Quién tiene más?", "segundos": 5, "respuesta": "¡Juan!", "emoji": "🍬", "titulo": "MÁS, MENOS", "sub": "e igual",
  "voz": ["Desafío: ¿quién tiene más caramelos? Tenés 5 segundos.", "¡Juan! Tiene más caramelos que Sofi.", "Hoy: *más*, *menos* e *igual*."]},
 {"t": "contar", "titulo": "LOS DE JUAN", "emoji": "🍬", "cantidad": 4,
  "voz": ["Contemos los caramelos de Juan.", "1, 2, 3, 4.", "Juan tiene *4 caramelos*."]},
 {"t": "contar", "titulo": "LOS DE SOFI", "emoji": "🍬", "cantidad": 2,
  "voz": ["Ahora, los caramelos de Sofi.", "1, 2.", "Sofi tiene *2 caramelos*."]},
 {"t": "comparar", "a": {"cab": "JUAN", "texto": "4: tiene más", "emoji": "👦"}, "b": {"cab": "SOFI", "texto": "2: tiene menos", "emoji": "👧"}, "signo": "y",
  "voz": ["Juan tiene 4: tiene *más*.", "Sofi tiene 2: tiene *menos*.", "4 es más que 2."]},
 {"t": "definicion", "palabra": "Igual", "texto": "La misma cantidad", "emoji": "🤝",
  "voz": ["¿Y si los dos tienen 3 caramelos?", "Entonces tienen *igual*: la misma cantidad."]},
 {"t": "pregunta", "pregunta": "Ana 🍎🍎🍎  Leo 🍎🍎🍎  ¿Quién tiene más?", "opciones": ["Ana", "Leo", "Tienen igual"], "correcta": 2,
  "voz": ["Ahora vos. Mirá las manzanas de Ana y Leo.", "¿Quién tiene más?", "¡Tienen *igual*! 3 y 3."]},
 {"t": "consejo", "titulo": "CONTÁ LOS DOS", "texto": "Gana el número más grande", "emoji": "🔢",
  "voz": ["Truco: contá los dos grupos y compará los números."]},
 {"t": "resumen", "items": [["MÁS", "el grupo más grande"], ["MENOS", "el grupo más chico"], ["IGUAL", "la misma cantidad"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Más*: el grupo más grande.", "*Menos*: el grupo más chico.", "*Igual*: la misma cantidad.", "¡Muy bien! Ahora, *a practicar*."]},
]
N3 = [
 {"t": "gancho", "emoji": "🥤", "final": "🤔", "titulo": "COMPARAR", "sub": "sin contar",
  "voz": ["Sofi tiene vasos para sus amigos.", "¿Alcanzan para todos? ¡Sin contar!", "Hoy aprendemos a *comparar sin contar*."]},
 {"t": "parejas", "a": {"emoji": "🧒", "n": 4}, "b": {"emoji": "🥤", "n": 6}, "texto": "Sobran vasos: hay más vasos",
  "voz": ["Ponemos un vaso para cada chico.", "Unimos *uno con uno*.", "Sobran vasos: hay *más vasos* que chicos."]},
 {"t": "consejo", "titulo": "UNO CON UNO", "texto": "Cada uno con su pareja", "emoji": "🤝",
  "voz": ["Unir *uno con uno* es armar *parejas*."]},
 {"t": "parejas", "a": {"emoji": "🧒", "n": 5}, "b": {"emoji": "🧁", "n": 3}, "texto": "Faltan tortitas: hay menos",
  "voz": ["Ahora, las tortitas.", "Unimos cada chico con una tortita.", "¡Faltan tortitas! Hay *menos tortitas* que chicos."]},
 {"t": "parejas", "a": {"emoji": "🧒", "n": 4}, "b": {"emoji": "🎈", "n": 4}, "texto": "¡No sobra ninguno: hay igual!",
  "voz": ["¿Y los globos?", "Un globo para cada chico.", "No sobra ni falta: hay *igual*."]},
 {"t": "pregunta", "pregunta": "🧒🧒🧒  🪑🪑  ¿Alcanzan las sillas?", "opciones": ["Sí, sobran", "No, faltan", "Hay igual"], "correcta": 1,
  "voz": ["Ahora vos. Mirá los chicos y las sillas.", "¿Alcanzan las sillas para todos?", "No: *falta una silla*."]},
 {"t": "errores", "items": [{"mal": "Un chico con dos vasos", "bien": "Un vaso para cada chico"}],
  "voz": ["Ojo con este error.", "Cada chico va con *un solo* vaso."]},
 {"t": "resumen", "items": [["UNO CON UNO", "armar parejas"], ["SOBRAN", "ese grupo tiene más"], ["FALTAN", "ese grupo tiene menos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Unimos *uno con uno*: parejas.", "Si *sobran*, ese grupo tiene más.", "Si *faltan*, ese grupo tiene menos.", "¡Muy bien! Ahora, *a practicar*."]},
]
N4 = [
 {"t": "historia", "personaje": {"nombre": "Sofi", "emoji": "👧"}, "lugar": "🛍️",
  "lineas": ["Sofi arma bolsitas de cumple.", "Una tiene 5 caramelos.", "¡La otra tiene 3!"], "titulo": "GRUPOS", "sub": "iguales",
  "voz": ["Sofi arma las *bolsitas* del cumple.", "En una bolsita puso 5 caramelos.", "Y en la otra, ¡solo 3!", "Hoy aprendemos a *armar grupos iguales*."]},
 {"t": "igualar", "a": {"emoji": "🍬", "n": 5}, "b": {"emoji": "🍬", "n": 3}, "accion": "agregar", "texto": "¡Ahora hay igual!",
  "voz": ["Una bolsita tiene 5 y la otra, 3.", "Agregamos a la que tiene *menos*: 4, 5.", "¡Listo! 5 y 5: hay *igual*."]},
 {"t": "consejo", "titulo": "AGREGAR", "texto": "Al grupo que tiene menos", "emoji": "➕",
  "voz": ["Para igualar, *agregamos* al grupo que tiene menos."]},
 {"t": "igualar", "a": {"emoji": "⚽", "n": 6}, "b": {"emoji": "⚽", "n": 4}, "accion": "quitar", "texto": "¡4 y 4: igual!",
  "voz": ["Otra forma de igualar: *quitar*.", "Sacamos pelotas del grupo que tiene *más*.", "Quedan 4 y 4: ¡*igual*!"]},
 {"t": "comparar", "a": {"cab": "AGREGAR", "texto": "al que tiene menos", "emoji": "➕"}, "b": {"cab": "QUITAR", "texto": "al que tiene más", "emoji": "➖"}, "signo": "o",
  "voz": ["Podemos *agregar* al grupo que tiene menos.", "O podemos *quitar* al grupo que tiene más.", "Las dos formas sirven para igualar."]},
 {"t": "pregunta", "pregunta": "🍎🍎🍎🍎  🍎🍎  ¿Cuántas agrego al grupo chico?", "opciones": ["1", "2", "3"], "correcta": 1,
  "voz": ["Ahora vos. Mirá los dos grupos de manzanas.", "¿Cuántas agregás al grupo chico para igualar?", "¡*2*! Así quedan 4 y 4."]},
 {"t": "resumen", "items": [["IGUAL", "la misma cantidad"], ["AGREGAR", "al grupo que tiene menos"], ["QUITAR", "al grupo que tiene más"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Igual* es la misma cantidad.", "Podemos *agregar* al que tiene menos.", "O *quitar* al que tiene más.", "¡Muy bien! Ahora, *a practicar*."]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m1-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
