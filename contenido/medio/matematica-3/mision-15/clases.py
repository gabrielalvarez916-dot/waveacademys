# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 15 · División con resto: las 4 clases animadas.
Metáfora de toda la misión: el taller de juguetes de Bruno (repartir piezas en cajas iguales).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m15-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '843261e0-334c-4ca3-9976-80806eb31f8c', 2: '6b7fe869-4b85-4388-912b-c458f7c5cf63', 3: '8ba3b8db-693a-4b09-b8c9-11ed59b7bd24', 4: '0f315c2f-815e-49a8-abfb-d5480fa31ac2'}
TIT = {1: 'Dividir restando', 2: 'Dividir con la tabla pitagórica', 3: 'El resto', 4: 'Comprobar con una multiplicación'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
BRUNO = {"nombre": "Bruno", "emoji": "🧑‍🔧"}

N1 = [
 {"t": "gancho", "emoji": "🧸", "final": "🤔", "titulo": "DIVIDIR", "sub": "restando",
  "voz": ["Bruno arma juguetes con *20 ruedas*.", "Cada auto lleva 4. ¿Cuántos autos salen?", "Hoy: *dividir restando*."]},
 {"t": "saltos", "titulo": "SACAMOS DE A 4", "min": 0, "max": 20, "cada": 4, "inicio": 20, "saltos": [{"a": 16, "txt": "− 4"}, {"a": 12, "txt": "− 4"}, {"a": 8, "txt": "− 4"}, {"a": 4, "txt": "− 4"}, {"a": 0, "txt": "− 4"}],
  "voz": ["Empezamos con 20 ruedas.", "Sacamos 4: quedan *16*.", "Sacamos 4: quedan *12*.", "Sacamos 4: quedan *8*.", "Sacamos 4: quedan *4*.", "¡Sacamos 4: quedan *0*!"]},
 {"t": "dato", "numero": "5", "antes": "20 − 4 − 4 − 4 − 4 − 4", "despues": "veces", "texto": "20 ÷ 4 = 5", "emoji": "🚗",
  "voz": ["Contamos cuántas veces sacamos 4: *5* veces.", "¡20 entre 4 es *5* autos!"]},
 {"t": "vof", "afirmacion": "Para dividir 15 ÷ 5 restamos 5 tres veces", "emoji": "🤔", "verdadero": True, "explicacion": "15, 10, 5, 0",
  "voz": ["¿Verdadero o falso? 15 entre 5: restamos 5 tres veces.", "15, 10, 5, 0…", "¡*Verdadero*! 15 entre 5 es 3."]},
 {"t": "errores", "items": [{"mal": "Contar cuánto queda en vez de las veces", "bien": "El resultado es cuántas veces restamos"}],
  "voz": ["Ojo con este error.", "El resultado es *cuántas veces* restamos."]},
 {"t": "resumen", "items": [["RESTAR", "siempre lo mismo"], ["CONTAR", "las veces"], ["LO QUE QUEDA", "el resto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Restamos* siempre la misma cantidad.", "*Contamos* las veces que restamos.", "Lo que queda al final es *el resto*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Bruno descubrió un atajo!", "bajada": "Usa la tabla pitagórica para dividir", "emoji": "🔢", "titulo": "DIVIDIR", "sub": "con la tabla",
  "voz": ["¡Último momento: Bruno descubrió un *atajo*!", "Usa la *tabla pitagórica* para dividir.", "Hoy: *dividir con la tabla pitagórica*."]},
 {"t": "ranking", "titulo": "TABLA DEL 6 HASTA 38", "items": [{"txt": "6 × 6 = 36", "emoji": "✅", "dato": "el más cerca"}, {"txt": "6 × 5 = 30", "emoji": "🔵", "dato": "menos"}, {"txt": "6 × 7 = 42", "emoji": "❌", "dato": "se pasa"}],
  "voz": ["Queremos 38 entre 6. Miramos la tabla del 6.", "6 por 7 es 42: *se pasa*.", "6 por 5 es 30: queda lejos.", "¡6 por 6 es *36*: el más cerca sin pasarse!"]},
 {"t": "balanza", "izq": {"cab": "6 × 6", "items": ["36"]}, "der": {"cab": "TENEMOS", "items": ["38"]}, "gana": "der",
  "voz": ["6 por 6 es 36.", "Tenemos 38: un poquito más.", "¡38 entre 6 es *6* y sobran 2!"]},
 {"t": "escape", "titulo": "CANDADOS DE LA TABLA", "candados": [{"p": "45 ÷ 9", "r": "5"}, {"p": "29 ÷ 7", "r": "4, sobra 1"}],
  "voz": ["¡Escape! Usamos la tabla.", "45 entre 9: 9 por 5 es 45, *5*.", "29 entre 7: *4* y sobra 1.", "¡Escapamos!"]},
 {"t": "errores", "items": [{"mal": "38 ÷ 6 = 7", "bien": "6 × 7 = 42 se pasa: es 6"}],
  "voz": ["Ojo con este error.", "El número de la tabla *no se puede pasar*."]},
 {"t": "resumen", "items": [["TABLA", "del divisor"], ["BUSCAR", "el más cerca"], ["SIN PASARSE", "nunca"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Usamos la *tabla* del número que divide.", "Buscamos el *más cerca*.", "¡Pero *sin pasarnos*!", CIERRE]},
]
N3 = [
 {"t": "historia", "personaje": BRUNO, "lugar": "🧸", "lineas": ["Bruno tiene 31 tornillos.", "Los guarda en cajas de 5.", "¡Quedan tornillos sueltos!"], "titulo": "EL", "sub": "resto",
  "voz": ["Bruno tiene *31 tornillos*.", "Los guarda en cajas de *5*.", "¡Quedan tornillos sueltos!", "Hoy: *el resto*."]},
 {"t": "grupos", "emoji": "🔩", "grupos": 6, "cada": 5, "texto": "31 ÷ 5 = 6 · resto 1", "titulo": "CAJAS DE 5",
  "voz": ["Llenamos cajas de 5.", "Contamos: 5, 10, 15, 20, 25, 30.", "¡Salen *6* cajas y queda *1* tornillo suelto!"]},
 {"t": "bloques", "titulo": "LAS PARTES", "items": [{"cab": "DIVIDENDO", "txt": "31"}, {"cab": "COCIENTE", "txt": "6"}, {"cab": "RESTO", "txt": "1"}],
  "voz": ["La división tiene partes con nombre.", "Lo que repartimos: *dividendo*, 31.", "Cuánto sale: *cociente*, 6.", "Lo que sobra: *resto*, 1."]},
 {"t": "prediccion", "pregunta": "Dividimos por 5. ¿El resto puede ser 7?", "a": {"txt": "No", "emoji": "😎"}, "b": {"txt": "Sí", "emoji": "🤔"}, "correcta": "a", "resultado": "¡No! Con 7 se llena otra caja",
  "voz": ["Dividimos por 5. ¿El resto puede ser 7?", "Con 7 tornillos se llena otra caja…", "¡*No*! El resto siempre es menor que 5."]},
 {"t": "errores", "items": [{"mal": "El resto es más grande que el divisor", "bien": "El resto siempre es más chico"}],
  "voz": ["Ojo con este error.", "El resto siempre es *más chico* que el divisor."]},
 {"t": "resumen", "items": [["DIVIDENDO", "lo que repartimos"], ["COCIENTE", "cuánto sale"], ["RESTO", "lo que sobra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *dividendo* es lo que repartimos.", "El *cociente* es cuánto sale.", "El *resto* es lo que sobra, siempre más chico.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Bruno", "emoji": "🧑‍🔧"}, "mensajes": [{"yo": False, "txt": "Dividí 31 ÷ 5 = 6 y sobra 1"}, {"yo": True, "txt": "¿Cómo sabés que está bien?"}, {"yo": False, "txt": "¡Con una multiplicación!"}], "titulo": "COMPROBAR", "sub": "multiplicando",
  "voz": ["Bruno escribe: 31 entre 5 es 6 y sobra 1.", "¿Cómo sabemos que está bien?", "¡Con una *multiplicación*!", "Hoy: *comprobar con una multiplicación*."]},
 {"t": "transforma", "titulo": "LA PRUEBA", "pasos": [{"txt": "6 × 5 = 30"}, {"txt": "30 + 1", "nota": "más el resto"}, {"txt": "= 31 ✓"}],
  "voz": ["Multiplicamos el cociente por el divisor: 6 por 5, 30.", "Le sumamos el resto: 30 más 1.", "¡Da *31*, el número del principio!"]},
 {"t": "comparar", "a": {"cab": "BIEN", "texto": "4 × 7 + 1 = 29 ✓", "emoji": "✅"}, "b": {"cab": "MAL", "texto": "5 × 7 + 1 = 36 ✗", "emoji": "❌"}, "signo": "y",
  "voz": ["Con 4, sobra 1: da *29*. ¡Bien!", "Con 5, sobra 1: da 36. ¡*Mal*!", "La prueba nos *avisa* del error."]},
 {"t": "quiz4", "pregunta": "Para comprobar 23 ÷ 4 = 5 resto 3…", "opciones": ["5 × 4 + 3", "5 + 4 + 3", "23 − 5"], "correcta": 0,
  "voz": ["Ahora vos: ¿cómo comprobamos 23 entre 4?", "Cociente por divisor, más el resto…", "¡5 por 4 más 3: *23*!"]},
 {"t": "errores", "items": [{"mal": "Olvidar sumar el resto en la prueba", "bien": "Cociente × divisor + resto"}],
  "voz": ["Ojo con este error.", "En la prueba, ¡no te olvides de *sumar el resto*!"]},
 {"t": "resumen", "items": [["MULTIPLICAR", "cociente × divisor"], ["SUMAR", "el resto"], ["COMPARAR", "con el dividendo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Multiplicamos* el cociente por el divisor.", "*Sumamos* el resto.", "Y *comparamos* con el número del principio.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m15-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 15 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
