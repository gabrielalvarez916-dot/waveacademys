# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 2 · Los números hasta 20: las 4 clases animadas.
Metáfora de toda la misión: el tren de los números de Tomi. Regla de primeros años (tools/medio/primeros_anios.py).
Genera tools/medio/clase/lecciones/medio-mat1-m2-n<N>.json. Uso: python3 clases.py"""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '7319a71d-3fc1-4559-86ac-bc89a2911b3c', 2: '643adad2-3677-4bea-8ec9-6d577e042839', 3: 'da6c3011-c082-45b5-bc35-61c07a894bfa', 4: 'bb036a33-f292-403e-b37e-4f5841e4931e'}
TIT = {1: 'Del 1 al 10', 2: 'Del 11 al 20', 3: 'Escribir y leer números', 4: 'Ordenar números hasta 20'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."

N1 = [
 {"t": "historia", "personaje": {"nombre": "Tomi", "emoji": "👦"}, "lugar": "🚂",
  "lineas": ["Tomi viaja en el tren de los números.", "Cada vagón tiene un número.", "¿Los conocés?"], "titulo": "DEL 1", "sub": "al 10",
  "voz": ["Tomi viaja en el *tren de los números*.", "Cada vagón tiene su número pintado.", "¿Los conocés? ¡Vamos a verlos!", "Hoy: *los números del 1 al 10*."]},
 {"t": "tren", "desde": 1, "hasta": 10, "titulo": "EL TREN DE TOMI",
  "voz": ["¡Acá llega el tren! Contemos los vagones.", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.", "¡Diez vagones! El último es el *10*."]},
 {"t": "consejo", "titulo": "TUS DOS MANOS", "texto": "Diez dedos: ¡hasta el 10!", "emoji": "🙌",
  "voz": ["Truco: con tus *dos manos* tenés 10 dedos."]},
 {"t": "contar", "titulo": "LAS MANZANAS", "emoji": "🍎", "cantidad": 7,
  "voz": ["El tren lleva manzanas. ¡Contemos!", "1, 2, 3, 4, 5, 6, 7.", "¡Hay *7 manzanas*!"]},
 {"t": "pregunta", "pregunta": "¿Cuántas estrellas hay? ⭐⭐⭐⭐⭐⭐⭐⭐⭐", "opciones": ["8", "9", "10"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cuántas estrellas hay?", "Contalas con el dedo, despacio.", "¡Son *9 estrellas*! ¡Muy bien!"]},
 {"t": "errores", "items": [{"mal": "Saltear el 6", "bien": "Decir todos, en orden"}],
  "voz": ["Ojo con este error.", "No te saltees ninguno: 5, *6*, 7."]},
 {"t": "resumen", "items": [["DEL 1 AL 10", "en orden"], ["DOS MANOS", "diez dedos"], ["EL ÚLTIMO", "dice cuántos hay"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos *del 1 al 10*, en orden.", "Dos manos tienen *diez dedos*.", "El *último número* dice cuántos hay.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué número viene después del 10?", "segundos": 5, "respuesta": "¡El 11!", "emoji": "🚂", "titulo": "DEL 11", "sub": "al 20",
  "voz": ["Desafío: ¿qué número viene después del 10?", "¡El *11*! Once.", "Hoy: *los números del 11 al 20*."]},
 {"t": "diezymas", "emoji": "🍬", "n": 13, "texto": "10 y 3 son 13",
  "voz": ["Esta caja tiene *10 caramelos*.", "Seguimos contando: 11, 12, 13.", "*10 y 3* son *13*."]},
 {"t": "definicion", "palabra": "Diez y algo más", "texto": "Del 11 al 19: una caja de 10 y sueltos", "emoji": "📦",
  "voz": ["Truco: del 11 al 19 son *diez y algo más*."]},
 {"t": "diezymas", "emoji": "⭐", "n": 17, "texto": "10 y 7 son 17",
  "voz": ["Otra caja de 10, ahora con estrellas.", "11, 12, 13, 14, 15, 16, 17.", "*10 y 7* son *17*."]},
 {"t": "diezymas", "emoji": "⚽", "n": 20, "texto": "10 y 10 son 20",
  "voz": ["¿Y si hay dos grupos de 10?", "11, 12, 13, 14, 15, 16, 17, 18, 19, 20.", "*10 y 10* son *20*: ¡veinte!"]},
 {"t": "tren", "desde": 11, "hasta": 20, "titulo": "EL TREN SIGUE",
  "voz": ["El tren de Tomi sigue viaje.", "11, 12, 13, 14, 15, 16, 17, 18, 19, 20.", "¡Llegamos al *20*!"]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 10 y 5?", "opciones": ["15", "14", "50"], "correcta": 0,
  "voz": ["Ahora vos. Una caja de 10 y 5 sueltos.", "¿Cuántos son en total?", "¡*15*! Diez y cinco, quince."]},
 {"t": "resumen", "items": [["11 AL 19", "diez y algo más"], ["20", "diez y diez"], ["CONTAR", "seguir desde el 10"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Del 11 al 19: *diez y algo más*.", "El *20* es diez y diez.", "Para contar, *seguimos desde el 10*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "✏️", "final": "🔢", "titulo": "ESCRIBIR", "sub": "y leer números",
  "voz": ["Tomi quiere pintar el número de su vagón.", "¿Cómo se escribe *doce*?", "Hoy: *escribir y leer números*."]},
 {"t": "fichas", "fichas": ["1", "2"], "grande": "12", "etiqueta": "DOCE",
  "voz": ["Doce tiene *dos cifras*: un 1 y un 2.", "Juntas forman el *12*.", "Y se lee: *doce*."]},
 {"t": "comparar", "a": {"cab": "SE ESCRIBE", "texto": "15", "emoji": "✏️"}, "b": {"cab": "SE LEE", "texto": "quince", "emoji": "🗣️"}, "signo": "=",
  "voz": ["Con cifras se escribe así: *15*.", "Con palabras se lee así: *quince*.", "¡Es el mismo número!"]},
 {"t": "errores", "items": [{"mal": "Escribir 21 para doce", "bien": "Primero el 1, después el 2"}],
  "voz": ["Ojo con este error.", "*Doce* es un 1 y un 2: no al revés."]},
 {"t": "fichas", "fichas": ["1", "8"], "grande": "18", "etiqueta": "DIECIOCHO",
  "voz": ["Ahora, *dieciocho*.", "Un 1 y un 8: *18*.", "Se lee *dieciocho*."]},
 {"t": "pregunta", "pregunta": "¿Cómo se escribe catorce?", "opciones": ["41", "14", "4"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cómo se escribe *catorce*?", "Pensá: ¿qué cifra va primero?", "¡*14*! Un 1 y un 4."]},
 {"t": "consejo", "titulo": "MIRÁ EL PRIMERO", "texto": "Del 10 al 19 empiezan con 1", "emoji": "👀",
  "voz": ["Truco: del 10 al 19, todos empiezan con *1*."]},
 {"t": "resumen", "items": [["ESCRIBIR", "con cifras: 12"], ["LEER", "con palabras: doce"], ["ORDEN", "primero el 1"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Escribimos con *cifras*: 12.", "Leemos con *palabras*: doce.", "Del 10 al 19, primero va el *1*.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": {"nombre": "Tomi", "emoji": "👦"}, "lugar": "🚂",
  "lineas": ["¡Se desarmó el tren!", "Los vagones quedaron mezclados.", "Hay que ordenarlos."], "titulo": "ORDENAR", "sub": "números hasta 20",
  "voz": ["¡Oh, no! ¡Se *desarmó* el tren de Tomi!", "Los vagones quedaron todos mezclados.", "Hay que ponerlos en orden.", "Hoy: *ordenar números hasta 20*."]},
 {"t": "tren", "desde": 5, "hasta": 12, "faltan": [8, 11], "titulo": "¿QUÉ VAGONES FALTAN?",
  "voz": ["Mirá el tren: faltan dos vagones.", "5, 6, 7… ¿y después? 9, 10… ¿y después? 12.", "¡Faltan el *8* y el *11*!"]},
 {"t": "definicion", "palabra": "Anterior y siguiente", "texto": "El que está antes y el que viene después", "emoji": "↔️",
  "voz": ["El *anterior* es el número que está antes.", "El *siguiente* es el que viene después."]},
 {"t": "recta", "min": 10, "max": 20, "paso": 1, "marcas": [{"v": 13, "txt": "anterior: 13"}, {"v": 14, "txt": "14"}, {"v": 15, "txt": "siguiente: 15"}],
  "voz": ["Mirá la recta del 10 al 20.", "El *13* va antes del 14: es el anterior.", "Este es el *14*.", "El *15* va después: es el siguiente."]},
 {"t": "comparar", "a": {"cab": "MAYOR", "texto": "18", "emoji": "🐘"}, "b": {"cab": "MENOR", "texto": "12", "emoji": "🐭"}, "signo": "y",
  "voz": ["El *18* es mayor: está más lejos del cero.", "El *12* es menor: está más cerca del cero.", "Mayor es *más*; menor es *menos*."]},
 {"t": "pregunta", "pregunta": "¿Qué número va después del 16?", "opciones": ["15", "17", "18"], "correcta": 1,
  "voz": ["Ahora vos. ¿Qué número va *después* del 16?", "Pensá en el tren de los números.", "¡El *17*! Es el siguiente."]},
 {"t": "pregunta", "pregunta": "¿Cuál es mayor?", "opciones": ["19", "11"], "correcta": 0,
  "voz": ["Otra más. Mirá estos dos números.", "¿Cuál es *mayor*: 19 u 11?", "¡El *19*! Está más lejos del cero."]},
 {"t": "resumen", "items": [["ANTERIOR", "el que va antes"], ["SIGUIENTE", "el que va después"], ["MAYOR", "más lejos del 0"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *anterior* va antes.", "El *siguiente* va después.", "El *mayor* está más lejos del cero.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m2-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 2 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
