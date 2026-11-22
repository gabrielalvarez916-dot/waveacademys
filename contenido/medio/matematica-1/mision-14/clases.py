# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 14 · Problemas de resta: las 4 clases animadas.
Metáfora: el cumple de Tomi. Regla de primeros años y regla de variedad del banco.
Genera tools/medio/clase/lecciones/medio-mat1-m14-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '00ff0dc2-573b-4f4e-a9ef-97e14127cc65', 2: '31b08949-7ca9-4d82-914f-9b540bb44836', 3: '5a5a0412-8940-4893-8c5e-791dab5f06e0', 4: '004eb6d1-a767-4a19-8e3e-588eacaaaa97'}
TIT = {1: 'Quitar y perder', 2: 'Comparar con la resta', 3: 'Cuánto falta', 4: 'Armar problemas de resta'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🎂", "lineas": ["Es el cumple de Tomi.", "Hay globos por todos lados.", "¡Pum! ¡Se pinchan algunos!"], "titulo": "QUITAR", "sub": "y perder",
  "voz": ["¡Es el *cumple* de Tomi!", "Hay globos por todos lados.", "¡Pum! ¡Se pinchan algunos!", "Hoy: *problemas de quitar y perder*."]},
 {"t": "sacar", "emoji": "🎈", "n": 8, "menos": 3, "texto": "8 − 3 = 5",
  "voz": ["Había *8* globos en la fiesta.", "Se pinchan 3.", "¡Quedan *5* globos!"]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "🍬", "texto": "Tomi tiene 10 caramelos"}, "despues": {"cab": "DESPUÉS", "emoji": "😋", "texto": "Come 4: le quedan 6"},
  "voz": ["*Antes*: Tomi tiene 10 caramelos.", "*Después* de comer 4, le quedan *6*."]},
 {"t": "sacar", "emoji": "🍪", "n": 7, "menos": 2, "texto": "7 − 2 = 5",
  "voz": ["Sofi tiene *7* galletitas.", "Le regala 2 a Tomi.", "¡Le quedan *5*!"]},
 {"t": "consejo", "titulo": "¿SE VA ALGO?", "texto": "Si se pierde, se come o se regala: restá", "emoji": "➖",
  "voz": ["Truco: si algo *se va*, restamos."]},
 {"t": "pregunta", "pregunta": "Hay 6 pelotas. Se pierden 4. ¿Cuántas quedan?", "opciones": ["10", "2", "4"], "correcta": 1,
  "voz": ["Ahora vos. Hay 6 y se pierden 4.", "¿Cuántas pelotas quedan?", "¡*2*! 6 menos 4."]},
 {"t": "resumen", "items": [["HABÍA", "el primer número"], ["SE VA", "restamos"], ["QUEDAN", "menos que antes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero miramos lo que *había*.", "Si algo *se va*, restamos.", "Al final *quedan menos*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "Tomi tiene 9 regalos y Sofi 6. ¿Cuántos más tiene Tomi?", "segundos": 6, "respuesta": "¡3!", "emoji": "🎁", "titulo": "COMPARAR", "sub": "con la resta",
  "voz": ["Desafío: Tomi tiene 9 regalos, Sofi 6.", "¡Tomi tiene *3* más!", "Hoy: *comparar con la resta*."]},
 {"t": "parejas", "a": {"emoji": "🎁", "n": 9}, "b": {"emoji": "🎁", "n": 6}, "texto": "¡TOMI TIENE 3 MÁS!",
  "voz": ["Arriba, los de Tomi. Abajo, los de Sofi.", "Unimos uno con uno.", "¡Sobran *3*: Tomi tiene 3 más!"]},
 {"t": "comparar", "a": {"cab": "TOMI", "texto": "9 regalos", "emoji": "👦"}, "b": {"cab": "SOFI", "texto": "6 regalos", "emoji": "👧"}, "signo": "−",
  "voz": ["Tomi tiene *9* regalos.", "Sofi tiene *6* regalos.", "Restamos: 9 menos 6 es *3*."]},
 {"t": "cuenta", "filas": ["9", "6"], "op": "−", "resultado": "3",
  "voz": ["Escribimos la resta: grande menos chico.", "9 menos 6 es igual a *3*."]},
 {"t": "pregunta", "pregunta": "Sofi tiene 10. Tomi tiene 7. ¿Cuántos más tiene Sofi?", "opciones": ["3", "17", "7"], "correcta": 0,
  "voz": ["Ahora vos. Sofi 10, Tomi 7.", "¿Cuántos más tiene Sofi?", "¡*3*! 10 menos 7."]},
 {"t": "errores", "items": [{"mal": "Sumar para comparar", "bien": "Restar: grande menos chico"}],
  "voz": ["Ojo con este error.", "Para comparar *restamos*, no sumamos."]},
 {"t": "resumen", "items": [["COMPARAR", "¿cuántos más?"], ["RESTAR", "grande menos chico"], ["EJEMPLO", "9 − 6 = 3"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Comparar* es ver cuántos más.", "Restamos *grande menos chico*.", "9 menos 6 es *3*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "Vienen 10 amigos al cumple"}, {"yo": True, "txt": "Hay solo 6 vasos"}, {"yo": False, "txt": "¿Cuántos faltan?"}], "titulo": "CUÁNTO", "sub": "falta",
  "voz": ["Tomi le escribe a Sofi.", "Vienen 10 amigos al cumple.", "Pero hay solo 6 vasos.", "Hoy: *cuánto falta*."]},
 {"t": "igualar", "a": {"emoji": "🥤", "n": 6}, "b": {"emoji": "🧒", "n": 10}, "accion": "agregar", "texto": "¡FALTAN 4 VASOS!",
  "voz": ["Hay *6* vasos y *10* chicos.", "Agregamos vasos: 7, 8, 9, 10.", "¡Faltan *4* vasos!"]},
 {"t": "cuenta", "filas": ["10", "6"], "op": "−", "resultado": "4",
  "voz": ["Con una resta: necesito menos tengo.", "10 menos 6 es *4*."]},
 {"t": "cuenta", "filas": ["6", "4"], "op": "+", "resultado": "10",
  "voz": ["Comprobamos con una suma.", "6 más 4 es *10*. ¡Está bien!"]},
 {"t": "pregunta", "pregunta": "Se necesitan 9 sillas. Hay 5. ¿Cuántas faltan?", "opciones": ["14", "4", "5"], "correcta": 1,
  "voz": ["Ahora vos. Se necesitan 9 sillas.", "Hay 5. ¿Cuántas faltan?", "¡*4*! 9 menos 5."]},
 {"t": "consejo", "titulo": "COMPROBÁ", "texto": "Tengo + falta = necesito", "emoji": "✅",
  "voz": ["Truco: sumá lo que tenés y lo que *falta*."]},
 {"t": "resumen", "items": [["NECESITO", "el grande"], ["TENGO", "el chico"], ["FALTA", "grande menos chico"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Lo que *necesito* es el grande.", "Lo que *tengo* es el chico.", "Lo que *falta*: los restamos.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "CONCURSO", "titular": "¡PROBLEMAS DE RESTA!", "bajada": "Tomi inventa el mejor", "emoji": "🏆", "titulo": "ARMAR", "sub": "problemas de resta",
  "voz": ["¡Nuevo concurso en la escuela!", "Hay que inventar *problemas de resta*.", "Hoy: *armar problemas de resta*."]},
 {"t": "linea", "titulo": "LA HISTORIA DE TOMI", "eventos": [{"fecha": "1", "txt": "Tomi tiene 7 globos", "emoji": "🎈"}, {"fecha": "2", "txt": "Regala 3", "emoji": "🎁"}, {"fecha": "3", "txt": "¿Cuántos le quedan?", "emoji": "❓"}],
  "voz": ["Primero: Tomi tiene *7* globos.", "Después: *regala* 3.", "Al final, la *pregunta*: ¿cuántos le quedan?"]},
 {"t": "sacar", "emoji": "🎈", "n": 7, "menos": 3, "texto": "7 − 3 = 4",
  "voz": ["Resolvemos el problema de Tomi.", "Se van los 3 que regala.", "¡Le quedan *4* globos!"]},
 {"t": "bloques", "titulo": "PALABRAS QUE RESTAN", "items": [{"cab": "PIERDE", "txt": "se le cae, no lo encuentra"}, {"cab": "COME", "txt": "ya no está"}, {"cab": "REGALA", "txt": "se lo da a otro"}],
  "voz": ["Estas palabras nos dicen *restá*.", "*Pierde*: no lo encuentra más.", "*Come*: ya no está.", "*Regala*: se lo da a otro."]},
 {"t": "pregunta", "pregunta": "¿Qué problema se resuelve con 8 − 5?", "opciones": ["Tengo 8 y gano 5", "Tengo 8 y pierdo 5", "Tengo 5"], "correcta": 1,
  "voz": ["Ahora vos. Mirá la cuenta 8 menos 5.", "¿Qué problema se resuelve con ella?", "¡*Tengo 8 y pierdo 5*!"]},
 {"t": "resumen", "items": [["QUIÉN", "Tomi, Sofi…"], ["SE VA", "pierde, come…"], ["PREGUNTA", "¿cuántos quedan?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Elegimos *quién*.", "Contamos qué *se va*.", "Y hacemos la *pregunta*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m14-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 14 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
