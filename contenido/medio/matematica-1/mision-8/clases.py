# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 8 · Juntar y agregar: las 4 clases animadas.
Metáfora: el picnic de Sofi en la plaza (manzanas, pelotas, globos y vasos). Regla de primeros años.
Plantillas nuevas de esta misión: `juntar` y `agregar` (tools/medio/clase/motor/t-mate.js).
Genera tools/medio/clase/lecciones/medio-mat1-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '3b05b278-3486-40c2-99f9-29a2264da122', 2: '9839bcd7-75f7-4dfa-948d-9684689a98c8', 3: '19357bd1-91e5-4d5e-a5c0-a5c3d44f256a', 4: 'fa15af9b-eb44-4fa7-85f0-c9d24d04fa5b'}
TIT = {1: 'Juntar colecciones', 2: 'Agregar elementos', 3: 'Sumar con dibujos', 4: 'Escribir la suma'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🧺", "lineas": ["Sofi va de picnic a la plaza.", "Lleva una canasta con manzanas.", "¡Tomi trae otra canasta!"], "titulo": "JUNTAR", "sub": "dos grupos",
  "voz": ["Sofi va de *picnic* a la plaza.", "Lleva una canasta con manzanas.", "¡Y Tomi trae otra canasta!", "Hoy: *juntar colecciones*."]},
 {"t": "juntar", "a": {"emoji": "🍎", "n": 3}, "b": {"emoji": "🍎", "n": 2}, "texto": "3 Y 2 SON 5",
  "voz": ["Sofi tiene *3* manzanas. Tomi tiene *2*.", "Las ponemos todas juntas en la manta.", "Contamos todo: ¡son *5* manzanas!"]},
 {"t": "definicion", "palabra": "JUNTAR", "texto": "Poner dos grupos en uno solo", "emoji": "🤝",
  "voz": ["*Juntar* es poner dos grupos en uno.", "Después contamos *todo* junto."]},
 {"t": "juntar", "a": {"emoji": "⚽", "n": 4}, "b": {"emoji": "⭐", "n": 3}, "texto": "4 Y 3 SON 7",
  "voz": ["Ahora juntamos 4 pelotas y 3 estrellas.", "Todo va al mismo grupo.", "Contamos: ¡son *7* cosas!"]},
 {"t": "consejo", "titulo": "CONTÁ TODO", "texto": "Contá cada cosa una sola vez", "emoji": "👆",
  "voz": ["Truco: contá cada cosa *una sola vez*."]},
 {"t": "pregunta", "pregunta": "4 pelotas y 4 pelotas. ¿Cuántas son?", "opciones": ["4", "6", "8"], "correcta": 2,
  "voz": ["Ahora vos. Juntamos 4 y 4 pelotas.", "¿Cuántas pelotas hay en total?", "¡*8*! Contamos todo junto."]},
 {"t": "resumen", "items": [["DOS GRUPOS", "los contamos"], ["JUNTAR", "un solo grupo"], ["TOTAL", "contamos todo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Tenemos *dos grupos*.", "Los *juntamos* en uno solo.", "Y contamos el *total*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Hay 4 manzanas. Llegan 3 más. ¿Cuántas hay?", "segundos": 6, "respuesta": "¡7!", "emoji": "🍎", "titulo": "AGREGAR", "sub": "elementos",
  "voz": ["Desafío: hay 4 manzanas y llegan 3.", "¡Son *7*!", "Hoy: *agregar elementos*."]},
 {"t": "agregar", "emoji": "🍎", "n": 4, "mas": 3, "texto": "4 Y 3 MÁS SON 7",
  "voz": ["En la manta hay *4* manzanas.", "Sofi agrega más: 5, 6, 7.", "¡Ahora hay *7* manzanas!"]},
 {"t": "definicion", "palabra": "AGREGAR", "texto": "Poner más cosas en un grupo", "emoji": "➕",
  "voz": ["*Agregar* es poner más cosas en un grupo.", "¡El grupo se hace *más grande*!"]},
 {"t": "agregar", "emoji": "🎈", "n": 5, "mas": 3, "texto": "5 Y 3 MÁS SON 8",
  "voz": ["Hay *5* globos atados al árbol.", "Tomi trae más: 6, 7, 8.", "¡Ahora hay *8* globos!"]},
 {"t": "consejo", "titulo": "SEGUÍ CONTANDO", "texto": "No empieces de nuevo desde 1", "emoji": "🔢",
  "voz": ["Truco: *seguí contando* desde el número que tenés."]},
 {"t": "pregunta", "pregunta": "Hay 5 vasos. Llegan 2. ¿Cuántos hay?", "opciones": ["7", "5", "3"], "correcta": 0,
  "voz": ["Ahora vos. Hay 5 vasos y llegan 2.", "¿Cuántos vasos hay ahora?", "¡*7*! Cinco, seis, siete."]},
 {"t": "errores", "items": [{"mal": "Empezar a contar de nuevo", "bien": "Seguir desde el número"}],
  "voz": ["Ojo con este error.", "No empieces de nuevo: *seguí contando*."]},
 {"t": "resumen", "items": [["GRUPO", "lo que había"], ["AGREGAR", "llegan más"], ["AHORA", "hay más que antes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero hay un *grupo*.", "Después *agregamos* más.", "¡Ahora hay *más que antes*!", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "✏️", "final": "🍎", "titulo": "SUMAR", "sub": "con dibujos",
  "voz": ["Sofi quiere contar las manzanas del picnic.", "¡Pero se las comieron! ¿Qué hace?", "Hoy: *sumar con dibujos*."]},
 {"t": "contar", "titulo": "UN PALITO POR MANZANA", "emoji": "✏️", "cantidad": 3, "etiqueta": "3 MANZANAS",
  "voz": ["Sofi dibuja un palito por cada manzana.", "1, 2, 3.", "¡*3 palitos* son 3 manzanas!"]},
 {"t": "juntar", "a": {"emoji": "✏️", "n": 3}, "b": {"emoji": "✏️", "n": 4}, "texto": "3 MÁS 4 SON 7",
  "voz": ["Tomi comió 4. Sofi dibuja 4 palitos más.", "Juntamos todos los palitos.", "Contamos: ¡son *7*!"]},
 {"t": "definicion", "palabra": "SUMAR", "texto": "Juntar o agregar y contar todo", "emoji": "➕",
  "voz": ["*Sumar* es juntar o agregar y contar todo.", "Se dice *más*: 3 más 4 es 7."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 2 más 6?", "opciones": ["4", "8", "9"], "correcta": 1,
  "voz": ["Ahora vos. Dibujá 2 palitos y 6 más.", "¿Cuántos palitos hay en total?", "¡*8*! Dos más seis es ocho."]},
 {"t": "errores", "items": [{"mal": "Un palito para todo el grupo", "bien": "Un palito por cada cosa"}],
  "voz": ["Ojo con este error.", "Dibujá *un palito por cada cosa*."]},
 {"t": "resumen", "items": [["DIBUJAR", "un palito por cosa"], ["SUMAR", "juntar y contar"], ["MÁS", "así se dice"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Dibujamos* un palito por cosa.", "*Sumar* es juntar y contar.", "Y se dice *más*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Cuántas manzanas llevamos?"}, {"yo": True, "txt": "Yo 3 y vos 2"}, {"yo": False, "txt": "¿Cómo lo anoto?"}], "titulo": "ESCRIBIR", "sub": "la suma",
  "voz": ["Tomi le escribe a Sofi.", "Sofi lleva 3 manzanas y Tomi 2.", "¿Cómo se anota eso?", "Hoy: *escribir la suma*."]},
 {"t": "definicion", "palabra": "+", "texto": "Se lee MÁS", "emoji": "➕",
  "voz": ["Este es el signo *más*.", "Va entre los dos números que juntamos."]},
 {"t": "definicion", "palabra": "=", "texto": "Se lee IGUAL", "emoji": "🟰",
  "voz": ["Este es el signo *igual*.", "Después del igual va el *resultado*."]},
 {"t": "fichas", "fichas": ["3", "+", "2", "=", "5"], "grande": "3 + 2 = 5", "etiqueta": "TRES MÁS DOS IGUAL A CINCO",
  "voz": ["Ponemos el 3, el más y el 2.", "Después el igual y el *5*.", "Se lee: *tres más dos igual a cinco*."]},
 {"t": "cuenta", "filas": ["4", "5"], "op": "+", "resultado": "9",
  "voz": ["Otra suma: 4 vasos más 5 vasos.", "¡4 más 5 es igual a *9*!"]},
 {"t": "pregunta", "pregunta": "¿Cómo se escribe 5 manzanas y 1 más?", "opciones": ["5 + 1 = 6", "5 = 1 + 6", "5 + 6 = 1"], "correcta": 0,
  "voz": ["Ahora vos. 5 manzanas y 1 más.", "¿Cuál es la suma bien escrita?", "¡*5 más 1 igual a 6*!"]},
 {"t": "errores", "items": [{"mal": "Poner el resultado antes del =", "bien": "El resultado va después del ="}],
  "voz": ["Ojo con este error.", "El *resultado* va después del igual."]},
 {"t": "resumen", "items": [["+", "se lee más"], ["=", "se lee igual"], ["SUMA", "3 + 2 = 5"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El signo *más* junta los números.", "Después del *igual* va el resultado.", "Tres más dos igual a *cinco*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m8-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 8 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
