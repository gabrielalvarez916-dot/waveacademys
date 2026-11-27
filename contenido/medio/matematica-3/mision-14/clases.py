# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 14 · Repartos y particiones: las 4 clases animadas.
Metáfora de toda la misión: el campamento de la escuela (repartir provisiones, armar carpas y grupos, autos para el paseo).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m14-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '873ef20d-ed24-4627-aa5e-34387a0ad45b', 2: 'be071863-cff7-4f7d-8fda-de1f5355867a', 3: '93ab0678-9dd2-4d25-acb2-a3ee29cd21fe', 4: 'b541572e-dfb2-4f4d-b99c-194bde10e0ff'}
TIT = {1: 'Repartir cantidades grandes', 2: 'Armar grupos', 3: 'Qué hacer con lo que sobra', 4: 'Problemas de reparto con resto'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
PROFE = {"nombre": "La profe Ana", "emoji": "👩‍🏫"}

N1 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Nos vamos de campamento!", "bajada": "Hay 84 linternas para 4 grupos", "emoji": "⛺", "titulo": "REPARTIR", "sub": "cantidades grandes",
  "voz": ["¡Último momento: nos vamos de *campamento*!", "Hay *84* linternas para repartir entre 4 grupos.", "Hoy: *repartir cantidades grandes*."]},
 {"t": "descomponer", "numero": "84", "titulo": "PARTIMOS EL 84", "partes": ["80", "4"], "resultado": "= 84 ✓",
  "voz": ["El 84 es grande para repartir de a una.", "Lo partimos en partes fáciles.", "Una parte: *80*.", "La otra parte: *4*.", "¡80 más 4 es 84!"]},
 {"t": "mazo", "titulo": "REPARTIMOS CADA PARTE", "items": [{"frente": "80 ÷ 4", "dorso": "20"}, {"frente": "4 ÷ 4", "dorso": "1"}, {"frente": "84 ÷ 4", "dorso": "20 + 1 = 21"}],
  "voz": ["80 entre 4: a cada grupo le tocan *20*.", "4 entre 4: le toca *1* más.", "¡En total, *21* linternas por grupo!"]},
 {"t": "quiz4", "pregunta": "¿Cuánto le toca a cada uno si repartimos 66 entre 3?", "opciones": ["22", "63", "33"], "correcta": 0,
  "voz": ["Ahora vos: 66 entre 3.", "20 y 2…", "¡*22* a cada uno!"]},
 {"t": "errores", "items": [{"mal": "84 ÷ 4: repartir solo el 80", "bien": "Repartir también el 4: son 21"}],
  "voz": ["Ojo con este error.", "Hay que repartir *todas* las partes."]},
 {"t": "resumen", "items": [["PARTIR", "en partes fáciles"], ["REPARTIR", "cada parte"], ["SUMAR", "lo que toca"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Partimos* el número en partes fáciles.", "*Repartimos* cada parte.", "Y *sumamos* lo que le toca a cada uno.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": PROFE, "lugar": "⛺", "lineas": ["Hay 24 chicos en el campamento.", "En cada carpa duermen 4.", "¿Cuántas carpas armamos?"], "titulo": "ARMAR", "sub": "grupos",
  "voz": ["Hay *24 chicos* en el campamento.", "En cada carpa duermen *4*.", "¿Cuántas carpas hay que armar?", "Hoy: *armar grupos*."]},
 {"t": "grupos", "emoji": "🧒", "grupos": 6, "cada": 4, "texto": "24 ÷ 4 = 6", "titulo": "CARPAS DE 4",
  "voz": ["Ponemos 4 chicos en cada carpa.", "Contamos: 4, 8, 12, 16, 20, 24.", "¡Son *6* carpas!"]},
 {"t": "comparar", "a": {"cab": "REPARTIR", "texto": "24 entre 4 carpas: ¿cuántos en cada una?", "emoji": "🎁"}, "b": {"cab": "AGRUPAR", "texto": "24 de a 4: ¿cuántas carpas?", "emoji": "📦"}, "signo": "y",
  "voz": ["Repartir: sabemos cuántos grupos, buscamos *cuánto va en cada uno*.", "Agrupar: sabemos cuánto va en cada uno, buscamos *cuántos grupos*.", "¡Las dos se resuelven *dividiendo*!"]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "18 de a 3", "r": "6 grupos"}, {"p": "30 de a 5", "r": "6 grupos"}, {"p": "28 de a 4", "r": "7 grupos"}],
  "voz": ["¡Ronda rápida! ¿Cuántos grupos?", "18 de a 3: *6* grupos.", "30 de a 5: *6* grupos.", "28 de a 4: *7* grupos."]},
 {"t": "errores", "items": [{"mal": "24 chicos de a 4: 24 + 4 = 28 carpas", "bien": "24 ÷ 4 = 6 carpas"}],
  "voz": ["Ojo con este error.", "Para armar grupos, *dividimos*: no sumamos."]},
 {"t": "resumen", "items": [["AGRUPAR", "de a la misma cantidad"], ["CONTAR", "los grupos"], ["DIVIDIR", "24 ÷ 4 = 6"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Armamos grupos con la *misma cantidad*.", "Contamos *cuántos grupos* salen.", "Es una *división*: 24 entre 4, 6.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "La profe Ana", "emoji": "👩‍🏫"}, "mensajes": [{"yo": False, "txt": "Tengo 23 galletas para 4 chicos"}, {"yo": True, "txt": "¡No da justo!"}, {"yo": False, "txt": "¿Qué hacemos con las que sobran?"}], "titulo": "LO QUE", "sub": "sobra",
  "voz": ["La profe escribe: tengo *23 galletas* para 4 chicos.", "¡No da justo!", "¿Qué hacemos con las que sobran?", "Hoy: *qué hacer con lo que sobra*."]},
 {"t": "grupos", "emoji": "🍪", "grupos": 4, "cada": 5, "texto": "23 ÷ 4 = 5 · sobran 3", "titulo": "5 A CADA UNO",
  "voz": ["Damos 5 galletas a cada uno.", "4 chicos por 5: 20 galletas repartidas.", "¡Sobran *3*! No alcanzan para otra vuelta."]},
 {"t": "definicion", "palabra": "Resto", "texto": "Lo que sobra en un reparto y no alcanza para otra vuelta.", "emoji": "🍪",
  "voz": ["Lo que sobra se llama *resto*.", "Siempre es *menor* que la cantidad de chicos."]},
 {"t": "zoom", "niveles": [{"emoji": "🍪", "txt": "Galletas: se pueden partir"}, {"emoji": "🎈", "txt": "Globos: quedan guardados"}, {"emoji": "🚗", "txt": "Chicos: hace falta un auto más"}],
  "voz": ["Las galletas que sobran se pueden *partir* en pedacitos.", "Los globos que sobran quedan *guardados*.", "¡Y si sobran chicos, hace falta *un auto más*!"]},
 {"t": "errores", "items": [{"mal": "23 entre 4: 5 a cada uno y sobran 7", "bien": "Sobran 3: con 7 se da otra vuelta"}],
  "voz": ["Ojo con este error.", "Si sobran *más* que los chicos, hay otra vuelta."]},
 {"t": "resumen", "items": [["RESTO", "lo que sobra"], ["MENOR", "que los grupos"], ["DECIDIR", "según la situación"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Lo que sobra se llama *resto*.", "Siempre es *menor* que la cantidad de grupos.", "Qué hacemos con él *depende de la situación*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "Van 26 chicos al paseo. En cada auto entran 4. ¿Cuántos autos?", "segundos": 8, "respuesta": "¡7 autos!", "emoji": "🚗", "titulo": "PROBLEMAS", "sub": "con resto",
  "voz": ["Desafío: van *26* chicos y en cada auto entran 4.", "¿Cuántos autos? ¡*7*!", "Hoy: *problemas de reparto con resto*."]},
 {"t": "transforma", "titulo": "26 ÷ 4", "pasos": [{"txt": "26 ÷ 4 = 6, SOBRAN 2"}, {"txt": "2 CHICOS SIN LUGAR", "nota": "no se quedan"}, {"txt": "6 + 1 = 7 AUTOS"}],
  "voz": ["Dividimos: se llenan *6* autos y sobran 2 chicos.", "¡Los 2 chicos no se pueden quedar!", "Hace falta un auto más: *7* autos."]},
 {"t": "prediccion", "pregunta": "30 globos para 4 mesas. ¿Cuántos en cada una?", "a": {"txt": "7", "emoji": "😎"}, "b": {"txt": "8", "emoji": "🤔"}, "correcta": "a", "resultado": "¡7 y sobran 2!",
  "voz": ["30 globos para 4 mesas, todas iguales.", "4 por 7 es 28, 4 por 8 es 32…", "¡*7* en cada mesa y sobran 2!"]},
 {"t": "unir", "titulo": "¿QUÉ HACEMOS CON EL RESTO?", "pares": [["Sobran chicos", "Un auto más"], ["Sobran caramelos", "Quedan en la bolsa"], ["Sobra una pizza", "Se corta en porciones"]],
  "voz": ["Uní cada resto con lo que hacemos.", "Si sobran chicos: *un auto más*.", "Si sobran caramelos: *quedan en la bolsa*.", "Si sobra una pizza: *se corta en porciones*."]},
 {"t": "errores", "items": [{"mal": "26 chicos, autos de 4: 6 autos", "bien": "7 autos: los 2 que sobran también viajan"}],
  "voz": ["Ojo con este error.", "Los que sobran *también* tienen que viajar."]},
 {"t": "resumen", "items": [["DIVIDIR", "primero"], ["MIRAR", "el resto"], ["DECIDIR", "y responder"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero *dividimos*.", "Después *miramos* qué pasa con el resto.", "Y *respondemos* con sentido.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m14-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 14 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
