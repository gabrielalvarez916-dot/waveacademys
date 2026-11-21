# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 11 · Dobles y sumas de iguales: las 4 clases animadas.
Metáfora: el espejo mágico de Sofi. Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat1-m11-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '7d8b1edd-ceae-47c3-a8c3-fc63ac2f48fd', 2: '2c89ae28-15ee-4f20-af3d-bfb8b98c12dd', 3: '84d8c211-a1aa-4baf-a02e-e54874f2e83e', 4: '9cf8c48f-2983-47e5-9980-9f9fd8e54e3a'}
TIT = {1: 'Los dobles', 2: 'Sumas de números iguales', 3: 'Casi dobles', 4: 'Cálculo mental con dobles'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🪞", "lineas": ["Sofi encontró un espejo mágico.", "Pone algo delante…", "¡y aparece dos veces!"], "titulo": "LOS DOBLES", "sub": "el espejo mágico",
  "voz": ["Sofi encontró un *espejo mágico*.", "Pone algo delante del espejo…", "¡y aparece *dos veces*!", "Hoy: *los dobles*."]},
 {"t": "juntar", "a": {"emoji": "🍎", "n": 3}, "b": {"emoji": "🍎", "n": 3}, "texto": "3 + 3 = 6",
  "voz": ["Sofi pone *3* manzanas. ¡Aparecen 3 más!", "Juntamos las de los dos lados.", "¡Son *6*! El doble de 3 es 6."]},
 {"t": "definicion", "palabra": "EL DOBLE", "texto": "Dos veces la misma cantidad", "emoji": "🪞",
  "voz": ["*El doble* es tener dos veces lo mismo.", "Como en el espejo mágico."]},
 {"t": "juntar", "a": {"emoji": "⚽", "n": 4}, "b": {"emoji": "⚽", "n": 4}, "texto": "4 + 4 = 8",
  "voz": ["Ahora pone *4* pelotas frente al espejo.", "Aparecen 4 más. Las juntamos.", "¡El doble de 4 es *8*!"]},
 {"t": "consejo", "titulo": "MIRÁ TUS MANOS", "texto": "Las dos manos son un doble: 5 + 5", "emoji": "🙌",
  "voz": ["Truco: tus manos son un doble. ¡*5 más 5*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es el doble de 2?", "opciones": ["2", "4", "22"], "correcta": 1,
  "voz": ["Ahora vos. Dos globos frente al espejo.", "¿Cuál es el doble de 2?", "¡*4*! 2 más 2 es 4."]},
 {"t": "resumen", "items": [["ESPEJO", "lo mismo dos veces"], ["DOBLE", "4 + 4 = 8"], ["MANOS", "5 + 5 = 10"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *espejo* muestra lo mismo dos veces.", "El *doble* de 4 es 8.", "Tus manos: *5 más 5 es 10*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cuánto es 2 + 2 + 2?", "segundos": 6, "respuesta": "¡6!", "emoji": "🧦", "titulo": "SUMAR", "sub": "números iguales",
  "voz": ["Desafío: ¿cuánto es 2 más 2 más 2?", "¡*6*!", "Hoy: *sumas de números iguales*."]},
 {"t": "agregar", "emoji": "🍎", "n": 6, "mas": 6, "texto": "6 + 6 = 12",
  "voz": ["Hay *6* manzanas y el espejo pone 6 más.", "Seguimos: 7, 8, 9, 10, 11, 12.", "¡6 más 6 es *12*!"]},
 {"t": "definicion", "palabra": "SUMAR IGUALES", "texto": "Sumar el mismo número varias veces", "emoji": "🔁",
  "voz": ["*Sumar iguales* es repetir el mismo número.", "Lo podemos repetir dos, tres o más veces."]},
 {"t": "saltos", "titulo": "TRES VECES EL 2", "min": 0, "max": 10, "cada": 1, "inicio": 0, "saltos": [{"a": 2, "txt": "+2"}, {"a": 2, "txt": "+2"}, {"a": 2, "txt": "+2"}],
  "voz": ["Saltamos de a 2 en la recta.", "Primer salto: llegamos al 2.", "Segundo salto: llegamos al 4.", "Tercer salto: ¡llegamos al *6*!"]},
 {"t": "pregunta", "pregunta": "3 pares de medias. ¿Cuántas medias son?", "opciones": ["3", "5", "6"], "correcta": 2,
  "voz": ["Ahora vos. Un par son 2 medias.", "¿Cuántas medias hay en 3 pares?", "¡*6*! 2 más 2 más 2."]},
 {"t": "errores", "items": [{"mal": "Sumar el 2 solo una vez", "bien": "Contar cuántas veces está"}],
  "voz": ["Ojo con este error.", "Contá *cuántas veces* está el número."]},
 {"t": "resumen", "items": [["IGUALES", "el mismo número"], ["DOBLE", "6 + 6 = 12"], ["TRES VECES", "2 + 2 + 2 = 6"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Sumamos el *mismo número*.", "6 más 6 es *12*.", "Tres veces el 2 es *6*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "🪞", "final": "➕", "titulo": "CASI DOBLES", "sub": "uno más",
  "voz": ["¡El espejo mágico se equivocó!", "Puso *una* manzana de más.", "Hoy: *casi dobles*."]},
 {"t": "juntar", "a": {"emoji": "⚽", "n": 4}, "b": {"emoji": "⚽", "n": 5}, "texto": "4 + 5 = 9",
  "voz": ["De un lado hay 4, del otro 5.", "¡Es casi un doble! El 5 tiene uno más.", "Juntamos todo: ¡son *9*!"]},
 {"t": "pasos", "titulo": "EL TRUCO", "items": [{"txt": "4 + 5", "emoji": "🤔"}, {"txt": "4 + 4 = 8", "emoji": "🪞"}, {"txt": "Uno más: 9", "emoji": "➕"}],
  "voz": ["Así se hace el *truco*.", "Miramos la suma: 4 más 5.", "Usamos el doble: 4 más 4 es 8.", "Uno más: ¡*9*!"]},
 {"t": "definicion", "palabra": "CASI DOBLE", "texto": "Dos números uno al lado del otro", "emoji": "👯",
  "voz": ["Un *casi doble* son dos números vecinos.", "Como el 4 y el 5."]},
 {"t": "pregunta", "pregunta": "Si 5 + 5 = 10, ¿cuánto es 5 + 6?", "opciones": ["10", "11", "12"], "correcta": 1,
  "voz": ["Ahora vos. Usá el doble del 5.", "¿Cuánto es 5 más 6?", "¡*11*! 10 y uno más."]},
 {"t": "errores", "items": [{"mal": "Sumar 2 al doble", "bien": "Sumar solo 1"}],
  "voz": ["Ojo con este error.", "Al doble le sumamos *solo 1*."]},
 {"t": "resumen", "items": [["CASI DOBLE", "4 + 5"], ["DOBLE", "4 + 4 = 8"], ["UNO MÁS", "4 + 5 = 9"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "4 más 5 es un *casi doble*.", "Usamos el *doble*: 4 más 4 es 8.", "Y *uno más*: 9.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "CAMPEONATO", "titular": "¡CARRERA DE DOBLES!", "bajada": "Gana quien responde sin contar", "emoji": "🏁", "titulo": "CÁLCULO MENTAL", "sub": "con dobles",
  "voz": ["¡Campeonato en la escuela de Sofi!", "Gana quien dice los dobles *sin contar*.", "Hoy: *cálculo mental con dobles*."]},
 {"t": "tabla", "titulo": "LOS DOBLES", "columnas": ["DOBLE", "DA"], "filas": [["1 + 1", "2"], ["2 + 2", "4"], ["3 + 3", "6"], ["4 + 4", "8"], ["5 + 5", "10"]],
  "voz": ["Estos son los primeros *dobles*.", "1 más 1 es 2.", "2 más 2 es 4.", "3 más 3 es 6.", "4 más 4 es 8.", "Y 5 más 5 es *10*."]},
 {"t": "tabla", "titulo": "DOBLES MÁS GRANDES", "columnas": ["DOBLE", "DA"], "filas": [["6 + 6", "12"], ["7 + 7", "14"], ["8 + 8", "16"], ["9 + 9", "18"], ["10 + 10", "20"]],
  "voz": ["Ahora, *dobles más grandes*.", "6 más 6 es 12.", "7 más 7 es 14.", "8 más 8 es 16.", "9 más 9 es 18.", "¡Y 10 más 10 es *20*!"]},
 {"t": "consejo", "titulo": "SALTAN DE A 2", "texto": "Los dobles son 2, 4, 6, 8, 10…", "emoji": "🐸",
  "voz": ["Truco: los resultados *saltan de a 2*."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 8 + 8?", "opciones": ["16", "18", "88"], "correcta": 0,
  "voz": ["Ahora vos. ¡Sin contar!", "¿Cuánto es 8 más 8?", "¡*16*!"]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 10 + 10?", "opciones": ["1010", "20", "11"], "correcta": 1,
  "voz": ["La última de la carrera.", "¿Cuánto es 10 más 10?", "¡*20*! ¡Ganaste!"]},
 {"t": "resumen", "items": [["MEMORIA", "sin contar"], ["HASTA 10", "5 + 5 = 10"], ["HASTA 20", "10 + 10 = 20"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los dobles se saben *de memoria*.", "5 más 5 es *10*.", "Y 10 más 10 es *20*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m11-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 11 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
