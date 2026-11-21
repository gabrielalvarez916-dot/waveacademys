# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 6 · Decenas y unidades: las 4 clases animadas.
Metáfora: el kiosco de la escuela de Sofi (bolsitas de 10 caramelos y caramelos sueltos). Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat1-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '8454576d-815e-4ea3-8d0b-fb74e4609cd6', 2: '04b8c66a-62ed-4672-a21f-efdbd1050817', 3: 'ef83b0cd-48d2-4a19-9051-683976a5c2c3', 4: 'c447a03d-4001-4578-a18e-7edd8bff79dd'}
TIT = {1: 'Agrupar de a diez', 2: 'Decenas y unidades sueltas', 3: 'Escribir números con decenas', 4: 'Armar y desarmar números'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
BOL = {"cabD": "BOLSITAS DE 10", "cabU": "SUELTOS"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍬", "lineas": ["Sofi atiende el kiosco de la escuela.", "Tiene muchos caramelos sueltos.", "¡Hay que guardarlos!"], "titulo": "AGRUPAR", "sub": "de a diez",
  "voz": ["Sofi atiende el *kiosco* de la escuela.", "Tiene un montón de caramelos sueltos.", "¿Cómo los cuenta rápido? ¡Agrupando!", "Hoy: *agrupar de a diez*."]},
 {"t": "contar", "titulo": "UNA BOLSITA", "emoji": "🍬", "cantidad": 10,
  "voz": ["Sofi mete caramelos en una bolsita.", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.", "¡*10 caramelos* llenan una bolsita!"]},
 {"t": "agrupar", "niveles": [{"nombre": "UNIDAD", "valor": "1", "icono": "🍬"}, {"nombre": "DECENA", "valor": "10", "icono": "🛍️"}], "salto": "×10",
  "voz": ["Un caramelo suelto es una *unidad*.", "10 caramelos en una bolsita son una *decena*.", "¡Una decena es igual a *10 unidades*!"]},
 {"t": "diezymas", "emoji": "🍬", "n": 14, "texto": "1 bolsita y 4 sueltos: 14",
  "voz": ["Una bolsita de 10 y algunos sueltos.", "11, 12, 13, 14.", "*1 decena y 4 unidades*: ¡14!"]},
 {"t": "consejo", "titulo": "DE A 10", "texto": "Agrupar de a 10 ayuda a contar", "emoji": "🛍️",
  "voz": ["Truco: agrupar de a 10 hace más fácil *contar*."]},
 {"t": "pregunta", "pregunta": "¿Cuántos caramelos van en una bolsita?", "opciones": ["5", "10", "100"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en las bolsitas de Sofi.", "¿Cuántos caramelos van en cada una?", "¡*10*! Una decena."]},
 {"t": "resumen", "items": [["UNIDAD", "un suelto"], ["DECENA", "una bolsita de 10"], ["AGRUPAR", "de a 10"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *unidad* es un suelto.", "Una *decena* es una bolsita de 10.", "Agrupar de a 10 ayuda a *contar*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cuántos caramelos hay en 3 bolsitas de 10?", "segundos": 6, "respuesta": "¡30!", "emoji": "🛍️", "titulo": "DECENAS", "sub": "y unidades sueltas",
  "voz": ["Desafío: ¿cuántos caramelos hay en 3 bolsitas?", "¡*30*! 10, 20, 30.", "Hoy: *decenas y unidades sueltas*."]},
 {"t": "cdu", "d": 3, "u": 5, "texto": "3 decenas y 5 unidades: 35", **BOL,
  "voz": ["Mirá lo que vendió Sofi hoy.", "Bolsitas: 10, 20, 30.", "Sueltos: 31, 32, 33, 34, 35.", "¡*3 decenas y 5 unidades*: 35!"]},
 {"t": "cdu", "d": 5, "u": 2, "texto": "5 decenas y 2 unidades: 52", **BOL,
  "voz": ["Otro pedido para el recreo.", "Bolsitas: 10, 20, 30, 40, 50.", "Sueltos: 51, 52.", "¡*5 decenas y 2 unidades*: 52!"]},
 {"t": "comparar", "a": {"cab": "DECENA", "texto": "bolsita de 10", "emoji": "🛍️"}, "b": {"cab": "UNIDAD", "texto": "1 suelto", "emoji": "🍬"}, "signo": "y",
  "voz": ["Una *decena* es una bolsita de 10.", "Una *unidad* es un caramelo suelto.", "¡Con las dos armamos cualquier número!"]},
 {"t": "pregunta", "pregunta": "¿Cuántas decenas tiene el 47?", "opciones": ["4", "7", "47"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el 47.", "¿Cuántas *decenas* tiene?", "¡*4*! Cuatro bolsitas de 10."]},
 {"t": "errores", "items": [{"mal": "Contar la bolsita como 1", "bien": "Una bolsita vale 10"}],
  "voz": ["Ojo con este error.", "Una bolsita vale *10*, no 1."]},
 {"t": "resumen", "items": [["DECENAS", "bolsitas de 10"], ["UNIDADES", "sueltos"], ["JUNTAS", "forman el número"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *decenas* son bolsitas de 10.", "Las *unidades* son los sueltos.", "Juntas *forman el número*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "✏️", "final": "🔢", "titulo": "ESCRIBIR", "sub": "con decenas",
  "voz": ["Sofi anota lo que vende en un cuaderno.", "¿Cómo escribe 6 bolsitas y 3 sueltos?", "Hoy: *escribir números con decenas*."]},
 {"t": "estante", "numero": "63", "cab": ["DECENAS", "UNIDADES"], "dig": ["6", "3"], "val": ["60", "3"], "destacar": 0, "etiqueta": "CADA CIFRA EN SU LUGAR",
  "voz": ["Mirá el número *63*.", "Tiene dos lugares.", "Decenas a la izquierda, unidades a la derecha.", "El 6 son *6 bolsitas*: vale 60.", "¡Y el 3 son *3 sueltos*!"]},
 {"t": "fichas", "fichas": ["6", "3"], "grande": "63", "etiqueta": "SESENTA Y TRES",
  "voz": ["Primero las decenas: un *6*. Después, un *3*.", "Juntas forman el *63*.", "Se lee: *sesenta y tres*."]},
 {"t": "errores", "items": [{"mal": "Escribir 36 para sesenta y tres", "bien": "Primero las decenas: 63"}],
  "voz": ["Ojo con este error.", "Primero van las *decenas*: 63, no 36."]},
 {"t": "pregunta", "pregunta": "4 bolsitas y 8 sueltos, ¿qué número es?", "opciones": ["48", "84", "12"], "correcta": 0,
  "voz": ["Ahora vos. 4 bolsitas y 8 sueltos.", "¿Qué número es?", "¡*48*! Cuarenta y ocho."]},
 {"t": "consejo", "titulo": "PRIMERO LAS BOLSITAS", "texto": "Las decenas van a la izquierda", "emoji": "⬅️",
  "voz": ["Truco: las *decenas* se escriben a la izquierda."]},
 {"t": "resumen", "items": [["DECENAS", "a la izquierda"], ["UNIDADES", "a la derecha"], ["LEER", "sesenta y tres"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *decenas* van a la izquierda.", "Las *unidades* van a la derecha.", "Y lo leemos: *sesenta y tres*.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍬", "lineas": ["Sofi recibe un pedido de 47.", "¿Cuántas bolsitas arma?", "¿Y cuántos sueltos?"], "titulo": "ARMAR", "sub": "y desarmar números",
  "voz": ["Sofi recibe un pedido de *47 caramelos*.", "¿Cuántas bolsitas arma?", "¿Y cuántos caramelos sueltos?", "Hoy: *armar y desarmar números*."]},
 {"t": "cdu", "d": 4, "u": 7, "texto": "47 = 40 + 7", **BOL,
  "voz": ["Armamos el pedido de 47.", "Bolsitas: 10, 20, 30, 40.", "Sueltos: 41, 42, 43, 44, 45, 46, 47.", "¡*4 bolsitas y 7 sueltos*!"]},
 {"t": "descomponer", "numero": "47", "titulo": "DESARMAMOS EL 47", "partes": ["40", "7"], "resultado": "= 47 ✓",
  "voz": ["Ahora *desarmamos* el 47.", "Lo escribimos como una suma.", "40 más 7.", "El 4 vale 40 y el 7 vale 7.", "40 más 7 es *47*."]},
 {"t": "descomponer", "numero": "85", "titulo": "DESARMAMOS EL 85", "partes": ["80", "5"], "resultado": "= 85 ✓",
  "voz": ["Otro más: el 85.", "Lo desarmamos en una suma.", "80 más 5.", "El 8 vale *80*.", "80 más 5 es *85*."]},
 {"t": "pregunta", "pregunta": "¿Qué número es 30 + 6?", "opciones": ["36", "63", "9"], "correcta": 0,
  "voz": ["Ahora vos. Armamos un número.", "¿Qué número es 30 más 6?", "¡El *36*!"]},
 {"t": "pregunta", "pregunta": "¿Cómo se desarma el 52?", "opciones": ["50 + 2", "5 + 2", "20 + 5"], "correcta": 0,
  "voz": ["Otra más. Desarmamos el 52.", "¿Cuál es la suma correcta?", "¡*50 más 2*!"]},
 {"t": "resumen", "items": [["ARMAR", "40 + 7 = 47"], ["DESARMAR", "47 = 40 + 7"], ["DECENAS", "valen 10 cada una"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Armar*: 40 más 7 es 47.", "*Desarmar*: 47 es 40 más 7.", "Cada decena vale *10*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m6-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 6 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
