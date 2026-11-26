# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 6 · Algoritmos de suma y resta: las 4 clases animadas.
Metáfora de toda la misión: la granja de manzanas de Ana (cajones, canastos y manzanas sueltas).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '05442b53-1b69-46ff-8245-a9505f7c12b4', 2: '550a7b4a-b5c7-4020-93c0-928eb3ff5887', 3: '63ce5d94-b9ab-45da-8a6a-447c71f2bb0d', 4: 'b4d361cb-b94b-44ce-b7bf-6239f0a06d80'}
TIT = {1: 'Suma en columnas', 2: 'Resta en columnas', 3: 'Reagrupar y canjear', 4: 'Controlar los resultados'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ANA = {"nombre": "Ana", "emoji": "👩‍🌾"}

N1 = [
 {"t": "historia", "personaje": ANA, "lugar": "🍎", "lineas": ["Ana cosechó 3.241 manzanas el lunes.", "El martes cosechó 2.516.", "¿Cuántas juntó?"], "titulo": "SUMA", "sub": "en columnas",
  "voz": ["Ana tiene una *granja de manzanas*.", "El lunes cosechó *3.241*. El martes, *2.516*.", "¿Cuántas juntó?", "Hoy: *la suma en columnas*."]},
 {"t": "tabla", "titulo": "3.241 + 2.516", "columnas": ["", "M", "C", "D", "U"], "filas": [["", "3", "2", "4", "1"], ["+", "2", "5", "1", "6"], ["=", "5", "7", "5", "7"]],
  "voz": ["Ponemos un número *debajo* del otro.", "Unidades debajo de unidades, decenas debajo de decenas.", "Sumamos de *derecha a izquierda*: 7, 5, 7 y 5.", "¡Juntó *5.757* manzanas!"]},
 {"t": "columnas", "a": "432", "b": "251", "op": "+", "resultado": "683", "titulo": "DE DERECHA A IZQUIERDA",
  "voz": ["Probemos con una más corta: 432 más 251.", "Unidades: 2 más 1, *3*.", "Decenas: 3 más 5, *8*.", "Centenas: 4 más 2, *6*. ¡*683*!"]},
 {"t": "quiz4", "pregunta": "¿Por dónde empezamos a sumar?", "opciones": ["Por las unidades", "Por los miles", "Por el medio"], "correcta": 0,
  "voz": ["Ahora vos: ¿por dónde empezamos?", "Pensá en la derecha…", "¡Por las *unidades*!"]},
 {"t": "errores", "items": [{"mal": "Poner las cifras corridas", "bien": "Unidades debajo de unidades"}],
  "voz": ["Ojo con este error.", "Si las cifras quedan *corridas*, la suma da mal."]},
 {"t": "resumen", "items": [["ENCOLUMNAR", "cada cifra en su lugar"], ["EMPEZAR", "por las unidades"], ["SUMAR", "columna por columna"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cada cifra va en *su columna*.", "Empezamos por las *unidades*.", "Sumamos *columna por columna*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Ana", "emoji": "👩‍🌾"}, "mensajes": [{"yo": False, "txt": "Tenía 7.586 manzanas"}, {"yo": True, "txt": "¿Y cuántas vendiste?"}, {"yo": False, "txt": "Vendí 2.345. ¿Cuántas quedan?"}], "titulo": "RESTA", "sub": "en columnas",
  "voz": ["Ana escribe: tenía *7.586* manzanas.", "Vendió *2.345*.", "¿Cuántas le quedan?", "Hoy: *la resta en columnas*."]},
 {"t": "flujo", "titulo": "7.586 − 2.345", "items": [{"txt": "6 − 5 = 1", "emoji": "1️⃣"}, {"txt": "8 − 4 = 4", "emoji": "🔟"}, {"txt": "5 − 3 = 2", "emoji": "💯"}, {"txt": "7 − 2 = 5", "emoji": "🚚"}],
  "voz": ["El *más grande* va arriba. Unidades: 6 menos 5, *1*.", "Decenas: 8 menos 4, *4*.", "Centenas: 5 menos 3, *2*.", "Miles: 7 menos 2, *5*. ¡Le quedan *5.241*!"]},
 {"t": "columnas", "a": "869", "b": "425", "op": "−", "resultado": "444", "titulo": "869 − 425",
  "voz": ["Otra más corta: 869 menos 425.", "Unidades: 9 menos 5, *4*.", "Decenas: 6 menos 2, *4*.", "Centenas: 8 menos 4, *4*. ¡*444*!"]},
 {"t": "vof", "afirmacion": "En la resta, el número más chico va arriba", "emoji": "🤔", "verdadero": False, "explicacion": "El más grande va arriba",
  "voz": ["¿Verdadero o falso? El más chico va arriba.", "Pensá: ¿de dónde sacamos?", "¡*Falso*! El *más grande* va arriba."]},
 {"t": "errores", "items": [{"mal": "Restar el de arriba menos el de abajo al revés", "bien": "Siempre arriba menos abajo"}],
  "voz": ["Ojo con este error.", "En cada columna es *arriba menos abajo*."]},
 {"t": "resumen", "items": [["ARRIBA", "el más grande"], ["EMPEZAR", "por las unidades"], ["RESTAR", "arriba menos abajo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Arriba va el *más grande*.", "Empezamos por las *unidades*.", "En cada columna, *arriba menos abajo*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "7 manzanas + 8 manzanas. ¿Entran en una columna?", "segundos": 8, "respuesta": "¡15: me llevo 1!", "emoji": "🍎", "titulo": "REAGRUPAR", "sub": "y canjear",
  "voz": ["Desafío: 7 más 8 en las unidades.", "¡Da *15*! No entra en una sola columna.", "Hoy: *reagrupar y canjear*."]},
 {"t": "columnas", "a": "268", "b": "125", "op": "+", "resultado": "393", "marcas": [{"col": "U", "txt": "13", "paso": 1}], "titulo": "ME LLEVO 1",
  "voz": ["Sumamos 268 más 125.", "Unidades: 8 más 5, 13.", "Escribo 3 y *me llevo 1*.", "Decenas: 6 más 2 más 1, *9*.", "Centenas: 2 más 1, *3*. ¡*393*!"]},
 {"t": "canje", "titulo": "ABRIMOS UN CANASTO", "grande": {"n": 4, "txt": "10"}, "chico": {"n": 2, "txt": "1"}, "sueltos": 0, "ec1": "4 canastos y 2 sueltas", "ec2": "3 canastos y 12 sueltas",
  "voz": ["En la resta, a veces *no alcanza*.", "Hay 4 canastos de 10 y 2 sueltas.", "¡Abrimos un canasto! Salen *10 sueltas*.", "Antes: 4 canastos y 2 sueltas.", "¡Ahora: *3 canastos y 12 sueltas*!"]},
 {"t": "columnas", "a": "342", "b": "127", "op": "−", "resultado": "215", "marcas": [{"col": "U", "txt": "12", "paso": 1}], "tachar": [{"col": "D", "nuevo": "3", "paso": 1}], "titulo": "EL CANJE",
  "voz": ["Restamos 342 menos 127.", "2 menos 7 no alcanza: el 4 pasa a 3.", "Ahora 12 menos 7, 5. Decenas: 3 menos 2, *1*.", "Centenas: 3 menos 1, *2*. ¡*215*!"]},
 {"t": "errores", "items": [{"mal": "268 + 125 = 3.813", "bien": "268 + 125 = 393"}],
  "voz": ["Ojo con este error.", "Si da más de 9, *te llevás 1*."]},
 {"t": "resumen", "items": [["SUMA", "me llevo 1"], ["RESTA", "abro un canasto"], ["10 SUELTAS", "un canasto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la suma, si pasa de 9, *me llevo 1*.", "En la resta, si no alcanza, *abro un canasto*.", "Diez sueltas forman *un canasto*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Error en la cuenta de la granja!", "bien": "", "bajada": "Ana revisa sus números", "emoji": "🔍", "titulo": "CONTROLAR", "sub": "los resultados",
  "voz": ["¡Último momento: hay un *error* en la granja!", "Ana revisa sus números.", "Hoy: *controlar los resultados*."]},
 {"t": "transforma", "titulo": "CONTROLAR UNA RESTA", "pasos": [{"txt": "5.214 − 1.538 = 3.676"}, {"txt": "3.676 + 1.538", "nota": "sumamos"}, {"txt": "= 5.214 ✓"}],
  "voz": ["Ana restó: 5.214 menos 1.538, da 3.676.", "Para controlar, sumamos el resultado y lo que restamos.", "¡Da *5.214*! La cuenta está bien."]},
 {"t": "prediccion", "pregunta": "2.768 + 1.455 = 3.000. ¿Está bien?", "a": {"txt": "Sí", "emoji": "😎"}, "b": {"txt": "No", "emoji": "🤔"}, "correcta": "b", "resultado": "¡No! Da cerca de 4.000",
  "voz": ["¿Qué creés? 2.768 más 1.455 da 3.000.", "Estimá: 3.000 más 1.000…", "¡No! Da cerca de *4.000*. Es 4.223."]},
 {"t": "pasos", "titulo": "DOS CONTROLES", "items": [{"txt": "Estimar con redondos", "emoji": "🎯"}, {"txt": "Hacer la cuenta al revés", "emoji": "🔄"}],
  "voz": ["Tenemos dos formas de controlar.", "*Estimar* con números redondos.", "Y hacer la cuenta *al revés*."]},
 {"t": "errores", "items": [{"mal": "Si la cuenta está hecha, está bien", "bien": "Siempre conviene controlarla"}],
  "voz": ["Ojo con este error.", "Siempre conviene *controlar* la cuenta."]},
 {"t": "resumen", "items": [["ESTIMAR", "da cerca"], ["AL REVÉS", "resta con suma"], ["SI NO DA", "revisar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Estimamos: el resultado tiene que dar *cerca*.", "Controlamos la resta *con una suma*.", "Si no da, *revisamos* la cuenta.", CIERRE]},
]
del N4[0]["bien"]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m6-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 6 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
