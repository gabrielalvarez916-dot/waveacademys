# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 9 · Sumas con algoritmo: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (sueltos, paquetes de 10 y cajas de 100).
Usa la plantilla nueva «columnas» (cuenta en columnas con U, D y C, me llevo 1). Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat2-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'e76dcc09-4786-48eb-9883-b98f1cd373f3', 2: '6cc17141-16d3-4d42-bd60-9325693be71c', 3: '908b8cd5-dc95-43ac-a870-11622cc4ef5a', 4: '964dbad6-7dc4-4c82-9e51-93fd334e1f62'}
TIT = {1: 'Sumar en columnas', 2: 'Sumas sin reagrupar', 3: 'Sumas con reagrupamiento', 4: 'Controlar el resultado'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa junta dos pedidos.", "234 y 52 alfajores.", "¿Cómo los suma?"], "titulo": "SUMAR", "sub": "en columnas",
  "voz": ["Rosa junta *dos pedidos*.", "Uno de 234 y otro de 52.", "¿Cómo hace la cuenta?", "Hoy: *sumar en columnas*."]},
 {"t": "clasificar", "cajas": [{"cab": "CENTENAS", "emoji": "📦"}, {"cab": "DECENAS", "emoji": "🍫"}, {"cab": "UNIDADES", "emoji": "🍪"}], "fichas": [{"txt": "2", "caja": 0}, {"txt": "3", "caja": 1}, {"txt": "5", "caja": 1}, {"txt": "4", "caja": 2}, {"txt": "2", "caja": 2}],
  "voz": ["Cada cifra va en su columna.", "Centenas con centenas.", "Decenas con decenas.", "¡Y unidades con unidades!"]},
 {"t": "columnas", "a": "234", "b": "52", "op": "+", "resultado": "286", "titulo": "234 + 52",
  "voz": ["Armamos la cuenta: el 52 va corrido a la derecha.", "Empezamos por las unidades: 4 más 2, *6*.", "Decenas: 3 más 5, *8*.", "Centenas: baja el *2*. ¡Da *286*!"]},
 {"t": "personaje", "personaje": ROSA, "lineas": [{"txt": "¡Empezá por la derecha!", "animo": "ojo"}, {"txt": "Primero las unidades", "animo": "feliz"}],
  "voz": ["Rosa avisa: ¡empezá por la *derecha*!", "Primero siempre las *unidades*."]},
 {"t": "quiz4", "pregunta": "En 413 + 75, ¿debajo de qué va el 7?", "opciones": ["Del 1", "Del 4", "Del 3"], "correcta": 0,
  "voz": ["Ahora vos: 413 más 75.", "¿Debajo de qué cifra va el *7*?", "¡Del *1*! Decenas con decenas."]},
 {"t": "resumen", "items": [["COLUMNAS", "U con U, D con D"], ["EMPEZAR", "por las unidades"], ["RESULTADO", "abajo de la raya"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cada cifra va en *su columna*.", "Empezamos por las *unidades*.", "El resultado va *abajo de la raya*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cuánto es 342 + 125?", "segundos": 8, "respuesta": "¡467!", "emoji": "📦", "titulo": "SUMAS", "sub": "sin reagrupar",
  "voz": ["Desafío: ¿cuánto es 342 más 125?", "¡*467*!", "Hoy: *sumas sin reagrupar*."]},
 {"t": "columnas", "a": "342", "b": "125", "op": "+", "resultado": "467", "titulo": "342 + 125",
  "voz": ["Armamos la cuenta en columnas.", "Unidades: 2 más 5, *7*.", "Decenas: 4 más 2, *6*.", "Centenas: 3 más 1, *4*. ¡*467*!"]},
 {"t": "columnas", "a": "503", "b": "284", "op": "+", "resultado": "787", "titulo": "CON UN CERO",
  "voz": ["Ahora una con un *cero*.", "Unidades: 3 más 4, *7*.", "Decenas: 0 más 8, *8*.", "Centenas: 5 más 2, *7*. ¡*787*!"]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "2 + 5", "r": "7"}, {"p": "0 + 8", "r": "8"}, {"p": "4 + 3", "r": "7"}],
  "voz": ["¡Ronda rápida de columnas!", "2 más 5: *7*.", "0 más 8: *8*.", "4 más 3: *7*."]},
 {"t": "errores", "items": [{"mal": "Saltear una columna", "bien": "Una columna por vez"}],
  "voz": ["Ojo con este error.", "Hacé *una columna por vez*, sin saltear."]},
 {"t": "resumen", "items": [["UNIDADES", "primero"], ["DECENAS", "después"], ["CENTENAS", "al final"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero las *unidades*.", "Después las *decenas*.", "Al final, las *centenas*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, 7 + 5 me da 12"}, {"yo": True, "txt": "¡No entra en la columna!"}, {"yo": False, "txt": "¿Y qué hago?"}], "titulo": "SUMAS", "sub": "con reagrupamiento",
  "voz": ["Tomi le escribe a Rosa.", "7 más 5 le da 12.", "¡Pero el 12 no entra en una columna!", "Hoy: *sumas con reagrupamiento*."]},
 {"t": "agrupar", "niveles": [{"nombre": "10 SUELTOS", "valor": "10", "icono": "alf"}, {"nombre": "1 PAQUETE", "valor": "10", "icono": "pack"}], "salto": "→",
  "voz": ["Rosa junta *10 sueltos*.", "¡Los mete en *un paquete*!", "12 sueltos son 1 paquete y 2 sueltos."]},
 {"t": "columnas", "a": "147", "b": "235", "op": "+", "resultado": "382", "marcas": [{"col": "D", "txt": "1", "paso": 1}], "titulo": "ME LLEVO 1",
  "voz": ["Sumamos 147 más 235.", "7 más 5 es 12: escribo 2, *me llevo 1*.", "Decenas: 4 más 3 más 1, *8*.", "Centenas: 1 más 2, *3*. ¡*382*!"], "sticker": {"txt": "📦", "paso": 1}},
 {"t": "vof", "afirmacion": "En 147 + 235, abajo escribo 12", "emoji": "🤔", "verdadero": False, "explicacion": "Escribo 2 y me llevo 1",
  "voz": ["¿Verdadero o falso? Abajo escribo el 12.", "Pensá en el paquete…", "¡*Falso*! Escribo 2 y *me llevo 1*."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 268 + 125?", "opciones": ["393", "383", "3813"], "correcta": 0,
  "voz": ["Ahora vos: 268 más 125.", "8 más 5 es 13: ¿te llevás 1?", "¡*393*! No te olvides del 1."]},
 {"t": "resumen", "items": [["PASA DE 10", "me llevo 1"], ["ESCRIBO", "solo las unidades"], ["EL 1", "va a la otra columna"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Si pasa de 10, *me llevo 1*.", "Abajo escribo *solo las unidades*.", "El 1 se suma en *la otra columna*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Error en la fábrica!", "bajada": "Una cuenta salió rarísima", "emoji": "🚨", "titulo": "CONTROLAR", "sub": "el resultado",
  "voz": ["¡Último momento: error en la fábrica!", "Una cuenta dio un resultado rarísimo.", "Hoy: *controlar el resultado*."]},
 {"t": "deslizador", "titulo": "¿MÁS O MENOS?", "min": 0, "max": 1000, "emoji": "📦", "paradas": [{"v": 300, "txt": "298 es casi 300"}, {"v": 400, "txt": "405 es casi 400"}, {"v": 700, "txt": "300 + 400 = 700"}],
  "voz": ["298 es casi *300*.", "405 es casi *400*.", "Más o menos da *700*."]},
 {"t": "versus", "titulo": "¿CUÁL TIENE SENTIDO?", "a": {"txt": "703", "emoji": "✅", "datos": ["cerca de 700"]}, "b": {"txt": "1.003", "emoji": "❌", "datos": ["muy lejos"]}, "gana": "a", "veredicto": "¡703 está cerca de 700!",
  "voz": ["Dos chicos hicieron 298 más 405.", "Uno dice *703*: está cerca de 700.", "Otro dice *1.003*: ¡está muy lejos!", "¡Gana el *703*! Tiene sentido."]},
 {"t": "jefe", "jefe": {"nombre": "Robot Raro", "emoji": "🤖"}, "preguntas": [{"p": "199 + 302 ≈ ?", "r": "500"}, {"p": "410 + 290 ≈ ?", "r": "700"}],
  "voz": ["¡El *Robot Raro* hace cuentas mal!", "Lo vencemos estimando.", "199 más 302: más o menos *500*.", "410 más 290: más o menos *700*. ¡Ganamos!"]},
 {"t": "pregunta", "pregunta": "Alguien dice: 301 + 299 = 900. ¿Tiene sentido?", "opciones": ["No", "Sí"], "correcta": 0,
  "voz": ["Ahora vos: 301 más 299 dio 900.", "Estimá: 300 más 300…", "¡*No* tiene sentido! Da cerca de *600*."]},
 {"t": "resumen", "items": [["ESTIMAR", "más o menos"], ["COMPARAR", "¿está cerca?"], ["REVISAR", "si está lejos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Estimamos* con números redondos.", "Comparamos: ¿el resultado *está cerca*?", "Si está lejos, *revisamos* la cuenta.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m9-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 9 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
