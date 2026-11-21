# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 10 · Sumas y complementos a 10: las 4 clases animadas.
Metáfora: los bolos de Sofi (10 bolos). Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat1-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '2026982e-ae33-428c-bac4-61156d654461', 2: '4c4f19df-f78a-4140-979c-545709dbf509', 3: 'd16dfa89-2392-46eb-93ef-f43185c451fc', 4: '4b39f530-b503-4bd1-8a3b-1c8e57a25a8d'}
TIT = {1: 'Las sumas que dan 10', 2: 'Complementos a 10', 3: 'Sumas hasta 10 de memoria', 4: 'Juegos de sumas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎳", "lineas": ["Sofi juega a los bolos.", "Hay 10 bolos parados.", "¡Tira la bola!"], "titulo": "SUMAS", "sub": "que dan 10",
  "voz": ["Sofi juega a los *bolos*.", "Hay 10 bolos parados.", "¡Tira la bola con fuerza!", "Hoy: *las sumas que dan 10*."]},
 {"t": "contar", "titulo": "LOS BOLOS", "emoji": "🎳", "cantidad": 10, "etiqueta": "10 BOLOS",
  "voz": ["Contamos los bolos de Sofi.", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.", "¡Hay *10* bolos!"]},
 {"t": "juntar", "a": {"emoji": "🎳", "n": 6}, "b": {"emoji": "🎳", "n": 4}, "texto": "6 + 4 = 10",
  "voz": ["Caen *6* bolos y quedan *4* parados.", "Juntamos los que cayeron y los parados.", "¡Son *10*! 6 más 4 es 10."]},
 {"t": "juntar", "a": {"emoji": "⚽", "n": 7}, "b": {"emoji": "⭐", "n": 3}, "texto": "7 + 3 = 10",
  "voz": ["Otra suma: 7 pelotas y 3 estrellas.", "Las juntamos todas.", "¡También dan *10*!"]},
 {"t": "consejo", "titulo": "TUS MANOS", "texto": "Tenés 10 dedos para sumar", "emoji": "🙌",
  "voz": ["Truco: tenés *10 dedos*. ¡Usalos para sumar!"]},
 {"t": "pregunta", "pregunta": "¿Qué suma da 10?", "opciones": ["5 + 3", "8 + 2", "6 + 2"], "correcta": 1,
  "voz": ["Ahora vos. Mirá las tres sumas.", "¿Cuál da *10*?", "¡*8 más 2*! Da 10."]},
 {"t": "resumen", "items": [["10 BOLOS", "10 lugares"], ["DOS GRUPOS", "llenan el 10"], ["6 + 4", "es 10"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Hay *10* bolos.", "Dos grupos pueden *llenar el 10*.", "Por ejemplo: 6 más 4 es *10*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Caen 7 bolos. ¿Cuántos quedan parados?", "segundos": 6, "respuesta": "¡3!", "emoji": "🎳", "titulo": "COMPLEMENTOS", "sub": "a 10",
  "voz": ["Desafío: caen 7 bolos de 10.", "¡Quedan *3* parados!", "Hoy: *complementos a 10*."]},
 {"t": "agregar", "emoji": "🎳", "n": 7, "mas": 3, "texto": "7 + 3 = 10",
  "voz": ["Tenemos *7*. ¿Cuánto falta para 10?", "Seguimos contando: 8, 9, 10.", "¡Faltan *3*! 7 más 3 es 10."]},
 {"t": "definicion", "palabra": "EL AMIGO DEL 10", "texto": "Lo que falta para llegar a 10", "emoji": "🤝",
  "voz": ["El *amigo del 10* es lo que falta.", "El amigo del 7 es el *3*."]},
 {"t": "agregar", "emoji": "🎳", "n": 6, "mas": 4, "texto": "6 + 4 = 10",
  "voz": ["Ahora tenemos *6*. ¿Cuánto falta?", "Seguimos contando: 7, 8, 9, 10.", "¡Faltan *4*! El amigo del 6 es el 4."]},
 {"t": "pregunta", "pregunta": "¿Cuánto le falta al 8 para llegar a 10?", "opciones": ["2", "8", "10"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el 8.", "¿Cuánto le falta para llegar a 10?", "¡*2*! 8 más 2 es 10."]},
 {"t": "errores", "items": [{"mal": "Contar los que ya están", "bien": "Contar los que faltan"}],
  "voz": ["Ojo con este error.", "Contá *los que faltan*, no los que ya están."]},
 {"t": "resumen", "items": [["FALTAN", "los lugares vacíos"], ["AMIGO DEL 10", "completa el 10"], ["7 Y 3", "son amigos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Lo que *falta* son los vacíos.", "El *amigo del 10* completa el 10.", "7 y 3 son *amigos del 10*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "🧠", "final": "🔟", "titulo": "DE MEMORIA", "sub": "sumas hasta 10",
  "voz": ["¿Podés sumar sin contar con los dedos?", "¡Sí! Si lo sabés *de memoria*.", "Hoy: *sumas hasta 10 de memoria*."]},
 {"t": "tabla", "titulo": "PAREJAS DEL 10", "columnas": ["SUMA", "DA"], "filas": [["1 + 9", "10"], ["2 + 8", "10"], ["3 + 7", "10"], ["4 + 6", "10"], ["5 + 5", "10"]],
  "voz": ["Estas son las *parejas del 10*.", "1 más 9.", "2 más 8.", "3 más 7.", "4 más 6.", "Y 5 más 5. ¡Todas dan *10*!"]},
 {"t": "fichas", "fichas": ["3", "+", "7"], "grande": "7 + 3 = 10", "etiqueta": "DAR VUELTA NO CAMBIA",
  "voz": ["Si 3 más 7 es 10…", "¡7 más 3 también es *10*!", "Dar vuelta *no cambia* el resultado."]},
 {"t": "pregunta", "pregunta": "5 + ___ = 10", "opciones": ["5", "10", "0"], "correcta": 0,
  "voz": ["Ahora vos. Sin contar.", "¿Qué número va con el 5?", "¡*5*! 5 más 5 es 10."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 4 + 6?", "opciones": ["8", "10", "12"], "correcta": 1,
  "voz": ["Otra más, bien rápido.", "¿Cuánto es 4 más 6?", "¡*10*! Es una pareja del 10."]},
 {"t": "consejo", "titulo": "PRACTICÁ", "texto": "Decilas en voz alta todos los días", "emoji": "🗣️",
  "voz": ["Truco: decí las parejas en voz alta *todos los días*."]},
 {"t": "resumen", "items": [["PAREJAS", "1 y 9, 2 y 8…"], ["MEMORIA", "sin contar"], ["VUELTA", "3 + 7 = 7 + 3"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Hay cinco *parejas del 10*.", "Las sabemos *de memoria*.", "Y dar vuelta *no cambia* nada.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "TORNEO DE BOLOS", "titular": "¡SOFI JUEGA LA FINAL!", "bajada": "Tira dos veces y suma", "emoji": "🏆", "titulo": "JUEGOS", "sub": "de sumas",
  "voz": ["¡Torneo de bolos en la plaza!", "Sofi juega la *final*.", "Hoy: *juegos de sumas*."]},
 {"t": "agregar", "emoji": "🎳", "n": 4, "mas": 3, "texto": "4 + 3 = 7",
  "voz": ["Primera tirada: caen *4* bolos.", "Segunda tirada: 5, 6, 7.", "¡Cayeron *7* bolos en total!"]},
 {"t": "juntar", "a": {"emoji": "🎲", "n": 5}, "b": {"emoji": "🎲", "n": 2}, "texto": "5 + 2 = 7",
  "voz": ["Ahora jugamos con dados: sale 5 y 2.", "Juntamos los puntos de los dos dados.", "¡5 más 2 es *7*!"]},
 {"t": "consejo", "titulo": "EMPEZÁ POR EL GRANDE", "texto": "En 2 + 6, empezá en 6", "emoji": "🚀",
  "voz": ["Truco: empezá por *el número más grande*."]},
 {"t": "cuenta", "filas": ["6", "2"], "op": "+", "resultado": "8",
  "voz": ["Empezamos en 6 y seguimos: 7, 8.", "¡6 más 2 es *8*!"]},
 {"t": "pregunta", "pregunta": "Sale 3 y sale 4. ¿Cuánto es?", "opciones": ["7", "6", "10"], "correcta": 0,
  "voz": ["Ahora vos. Sale 3 y sale 4.", "¿Cuántos puntos son en total?", "¡*7*! Cuatro, cinco, seis, siete."]},
 {"t": "errores", "items": [{"mal": "Pensar que todas dan 10", "bien": "Cada suma da su número"}],
  "voz": ["Ojo con este error.", "No todas las sumas dan *10*."]},
 {"t": "resumen", "items": [["BOLOS", "sumamos los que caen"], ["DADOS", "sumamos los puntos"], ["TRUCO", "empezar por el grande"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Con *bolos* sumamos los que caen.", "Con *dados* sumamos los puntos.", "Y empezamos por *el grande*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m10-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 10 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
