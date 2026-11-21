# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 9 · Quitar y comparar: las 4 clases animadas.
Metáfora: el picnic de Sofi en la plaza (sigue de la misión 8). Regla de primeros años.
Plantilla nueva de esta misión: `sacar` (tools/medio/clase/motor/t-mate.js).
Genera tools/medio/clase/lecciones/medio-mat1-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '389262b5-4821-4222-aa2f-05aa7c8f9020', 2: 'f4175551-3934-41ca-9b81-1259fb0c501e', 3: '0ce8ad75-f9f7-4259-b7dc-85bb80b683bb', 4: 'dcdb98ae-6cc6-456e-af0b-ffb8438d13d6'}
TIT = {1: 'Sacar elementos', 2: 'Perder y gastar', 3: 'Comparar cantidades', 4: 'Escribir la resta'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🧺", "lineas": ["Sofi está de picnic en la plaza.", "Tiene 7 manzanas en la canasta.", "¡Sus amigos tienen hambre!"], "titulo": "SACAR", "sub": "elementos",
  "voz": ["Sofi sigue de *picnic* en la plaza.", "Tiene 7 manzanas en la canasta.", "¡Y sus amigos tienen hambre!", "Hoy: *sacar elementos*."]},
 {"t": "sacar", "emoji": "🍎", "n": 7, "menos": 3, "texto": "7 MENOS 3 SON 4",
  "voz": ["En la canasta hay *7* manzanas.", "Sofi saca 3 para sus amigos.", "Contamos las otras: ¡quedan *4*!"]},
 {"t": "definicion", "palabra": "SACAR", "texto": "Quitar cosas de un grupo", "emoji": "✋",
  "voz": ["*Sacar* es quitar cosas de un grupo.", "¡El grupo se hace *más chico*!"]},
 {"t": "sacar", "emoji": "⚽", "n": 5, "menos": 2, "texto": "5 MENOS 2 SON 3",
  "voz": ["Hay *5* pelotas en el pasto.", "Tomi se lleva 2 pelotas.", "¡Quedan *3* pelotas!"]},
 {"t": "consejo", "titulo": "TACHÁ PRIMERO", "texto": "Después contá las que quedan", "emoji": "❌",
  "voz": ["Truco: tachá las que sacás y contá *las otras*."]},
 {"t": "pregunta", "pregunta": "Hay 5 manzanas. Sacamos 2. ¿Cuántas quedan?", "opciones": ["7", "3", "2"], "correcta": 1,
  "voz": ["Ahora vos. Hay 5 manzanas y sacamos 2.", "¿Cuántas manzanas quedan?", "¡*3*! Al sacar quedan menos."]},
 {"t": "resumen", "items": [["GRUPO", "lo que había"], ["SACAR", "quitar algunas"], ["QUEDAN", "contamos las otras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero hay un *grupo*.", "Después *sacamos* algunas.", "Y contamos las que *quedan*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SE VUELAN LOS GLOBOS!", "bajada": "Viento fuerte en la plaza", "emoji": "🎈", "titulo": "PERDER", "sub": "y gastar",
  "voz": ["¡Último momento! Hay viento en la plaza.", "¡Se vuelan los globos de Sofi!", "Hoy: *perder y gastar*."]},
 {"t": "sacar", "emoji": "🎈", "n": 6, "menos": 2, "texto": "LE QUEDAN 4",
  "voz": ["Sofi tenía *6* globos.", "El viento se lleva 2.", "¡Le quedan *4* globos!"]},
 {"t": "definicion", "palabra": "PERDER Y GASTAR", "texto": "Nos quedan menos que antes", "emoji": "📉",
  "voz": ["Cuando *perdemos* o *gastamos* algo…", "¡nos quedan *menos* que antes!"]},
 {"t": "sacar", "emoji": "🍬", "n": 8, "menos": 3, "texto": "LE QUEDAN 5",
  "voz": ["Tomi tiene *8* caramelos y come 3.", "Contamos para atrás: 7, 6, 5.", "¡Le quedan *5* caramelos!"]},
 {"t": "consejo", "titulo": "PARA ATRÁS", "texto": "Contá para atrás desde tu número", "emoji": "⏪",
  "voz": ["Truco: contá *para atrás* desde tu número."]},
 {"t": "pregunta", "pregunta": "Tomi tiene 6 caramelos. Come 2. ¿Cuántos le quedan?", "opciones": ["8", "4", "2"], "correcta": 1,
  "voz": ["Ahora vos. Tomi tiene 6 y come 2.", "¿Cuántos caramelos le quedan?", "¡*4*! Seis, cinco, cuatro."]},
 {"t": "errores", "items": [{"mal": "Sumar cuando se pierde algo", "bien": "Perder es sacar: quedan menos"}],
  "voz": ["Ojo con este error.", "Si perdés algo, te quedan *menos*."]},
 {"t": "resumen", "items": [["PERDER", "se va algo"], ["GASTAR", "usamos algo"], ["QUEDAN", "menos que antes"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Perder* es cuando se va algo.", "*Gastar* es cuando lo usamos.", "Al final quedan *menos*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "6 pelotas y 4 estrellas. ¿Qué hay más?", "segundos": 6, "respuesta": "¡PELOTAS!", "emoji": "⚽", "titulo": "COMPARAR", "sub": "cantidades",
  "voz": ["Desafío: ¿hay más pelotas o estrellas?", "¡Hay más *pelotas*!", "Hoy: *comparar cantidades*."]},
 {"t": "parejas", "a": {"emoji": "⚽", "n": 6}, "b": {"emoji": "⭐", "n": 4}, "texto": "¡HAY 2 ⚽ MÁS!",
  "voz": ["Arriba, pelotas. Abajo, estrellas.", "Unimos uno con uno.", "¡Sobran *2* pelotas: hay 2 más!"]},
 {"t": "definicion", "palabra": "COMPARAR", "texto": "Ver cuántos más tiene un grupo", "emoji": "⚖️",
  "voz": ["*Comparar* es mirar dos grupos.", "Vemos cuántos *más* tiene uno."]},
 {"t": "parejas", "a": {"emoji": "🧒", "n": 5}, "b": {"emoji": "🥤", "n": 7}, "texto": "¡SOBRAN 2 🥤!",
  "voz": ["Cinco chicos y siete vasos.", "Un vaso para cada chico.", "¡Sobran *2* vasos!"]},
 {"t": "pregunta", "pregunta": "Sofi tiene 7 manzanas. Tomi tiene 4. ¿Cuántas más tiene Sofi?", "opciones": ["3", "11", "4"], "correcta": 0,
  "voz": ["Ahora vos. Sofi tiene 7, Tomi 4.", "¿Cuántas manzanas más tiene Sofi?", "¡*3*! Las que sobran."]},
 {"t": "consejo", "titulo": "MIRÁ LO QUE SOBRA", "texto": "Lo que sobra dice cuántos más", "emoji": "👀",
  "voz": ["Truco: *lo que sobra* dice cuántos más hay."]},
 {"t": "resumen", "items": [["UNO CON UNO", "unimos los grupos"], ["SOBRAN", "los que quedan solos"], ["MÁS", "lo que sobra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Unimos *uno con uno*.", "Miramos los que *sobran*.", "Eso dice cuántos *más* hay.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Cuántas manzanas quedan?"}, {"yo": True, "txt": "Había 7 y comimos 3"}, {"yo": False, "txt": "¿Cómo lo anoto?"}], "titulo": "ESCRIBIR", "sub": "la resta",
  "voz": ["Tomi le escribe a Sofi.", "Había 7 manzanas y comieron 3.", "¿Cómo se anota eso?", "Hoy: *escribir la resta*."]},
 {"t": "definicion", "palabra": "−", "texto": "Se lee MENOS", "emoji": "➖",
  "voz": ["Este es el signo *menos*.", "Lo usamos cuando *sacamos* cosas."]},
 {"t": "fichas", "fichas": ["7", "−", "3", "=", "4"], "grande": "7 − 3 = 4", "etiqueta": "SIETE MENOS TRES IGUAL A CUATRO",
  "voz": ["Primero el 7, lo que había.", "Después menos 3, igual a *4*.", "Se lee: *siete menos tres igual a cuatro*."]},
 {"t": "cuenta", "filas": ["9", "5"], "op": "−", "resultado": "4",
  "voz": ["Otra resta: 9 pelotas menos 5.", "¡9 menos 5 es igual a *4*!"]},
 {"t": "pregunta", "pregunta": "¿Cómo se escribe 8 vasos y sacamos 2?", "opciones": ["8 − 2 = 6", "2 − 8 = 6", "8 + 2 = 6"], "correcta": 0,
  "voz": ["Ahora vos. 8 vasos y sacamos 2.", "¿Cuál es la resta bien escrita?", "¡*8 menos 2 igual a 6*!"]},
 {"t": "errores", "items": [{"mal": "Poner primero lo que sacamos", "bien": "Primero va lo que había"}],
  "voz": ["Ojo con este error.", "Primero va *lo que había*."]},
 {"t": "resumen", "items": [["−", "se lee menos"], ["PRIMERO", "lo que había"], ["RESTA", "7 − 3 = 4"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El signo *menos* es para sacar.", "Primero va *lo que había*.", "Siete menos tres igual a *cuatro*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m9-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 9 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
