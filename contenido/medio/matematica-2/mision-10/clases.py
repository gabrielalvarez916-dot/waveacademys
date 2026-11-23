# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 10 · Restas con algoritmo: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (los alfajores que se venden; abrir un paquete = canje).
Usa la plantilla «columnas» (cuenta en columnas, con el canje tachado). Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat2-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'a82a4661-1e7c-45a2-98fe-ceff46c61eba', 2: 'dd20c56d-0069-45e7-9b7f-bfb31bd40701', 3: 'e51351af-263c-45b5-a7e9-ffae230708cc', 4: '30db8911-7343-4524-b33f-f02579c1029c'}
TIT = {1: 'Restar en columnas', 2: 'Restas sin canje', 3: 'Restas con canje', 4: 'Controlar una resta con la suma'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🚚", "lineas": ["Rosa tenía 576 alfajores.", "Vendió 234.", "¿Cuántos le quedan?"], "titulo": "RESTAR", "sub": "en columnas",
  "voz": ["Rosa tenía *576* alfajores.", "Hoy vendió *234*.", "¿Cuántos le quedan?", "Hoy: *restar en columnas*."]},
 {"t": "comparar", "a": {"cab": "ARRIBA", "texto": "576: lo que había", "emoji": "⬆️"}, "b": {"cab": "ABAJO", "texto": "234: lo que se fue", "emoji": "⬇️"}, "signo": "−",
  "voz": ["Arriba va lo que había: el *más grande*.", "Abajo va lo que se vendió.", "¡Del de arriba sacamos el de abajo!"]},
 {"t": "columnas", "a": "576", "b": "234", "op": "−", "resultado": "342", "titulo": "576 − 234",
  "voz": ["Armamos la resta en columnas.", "Unidades: 6 menos 4, *2*.", "Decenas: 7 menos 3, *4*.", "Centenas: 5 menos 2, *3*. ¡Quedan *342*!"]},
 {"t": "quiz4", "pregunta": "En una resta, ¿qué número va arriba?", "opciones": ["El más grande", "El más chico"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Qué número va arriba en la resta?", "¡El *más grande*! De él sacamos."]},
 {"t": "errores", "items": [{"mal": "Empezar por las centenas", "bien": "Empezar por las unidades"}],
  "voz": ["Ojo con este error.", "Siempre empezamos por las *unidades*."]},
 {"t": "resumen", "items": [["ARRIBA", "el más grande"], ["COLUMNAS", "U con U, D con D"], ["EMPEZAR", "por las unidades"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Arriba va el *más grande*.", "Cada cifra en *su columna*.", "Empezamos por las *unidades*.", CIERRE]},
]
N2 = [
 {"t": "gancho", "emoji": "🚚", "final": "📦", "titulo": "RESTAS", "sub": "sin canje",
  "voz": ["Salieron camiones llenos de alfajores.", "¿Cuántos quedan en la fábrica?", "Hoy: *restas sin canje*."]},
 {"t": "columnas", "a": "865", "b": "432", "op": "−", "resultado": "433", "titulo": "865 − 432",
  "voz": ["Rosa tenía 865 y vendió 432.", "Unidades: 5 menos 2, *3*.", "Decenas: 6 menos 3, *3*.", "Centenas: 8 menos 4, *4*. ¡*433*!"]},
 {"t": "pizarra", "titulo": "CUANDO DA CERO", "lineas": [{"txt": "579 − 274"}, {"txt": "7 − 7 = 0", "color": "coral", "marca": "circulo"}, {"txt": "= 305", "color": "sol"}],
  "voz": ["Ahora 579 menos 274.", "En las decenas: 7 menos 7 es *0*.", "¡El cero guarda el lugar: *305*!"]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["900 − 100 = 800", "800 − 100 = 700", "700 − 100 = 600"], "falta": "600 − 100 = 500", "regla": "Restamos 100 cada vez",
  "voz": ["Mirá: cada camión se lleva 100.", "¿Qué resta sigue?", "¡600 menos 100: *500*!"]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 796 − 352?", "opciones": ["444", "448", "1148"], "correcta": 0,
  "voz": ["Ahora vos: 796 menos 352.", "Columna por columna.", "¡*444*!"]},
 {"t": "resumen", "items": [["UNIDADES", "primero"], ["DECENAS", "después"], ["IGUALES", "da 0"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero las *unidades*, después las *decenas*.", "Al final, las *centenas*.", "Si son iguales, queda *0*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿2 − 8? ¡No alcanza!"}, {"yo": True, "txt": "¡Abrí un paquete!"}, {"yo": False, "txt": "¿Cómo?"}], "titulo": "RESTAS", "sub": "con canje",
  "voz": ["Tomi hace 352 menos 128.", "En las unidades: 2 menos 8. ¡No alcanza!", "Rosa le dice: ¡abrí un paquete!", "Hoy: *restas con canje*."]},
 {"t": "canje", "titulo": "ABRIMOS UN PAQUETE", "grande": {"n": 4, "txt": "10"}, "chico": {"n": 2, "txt": "1"}, "sueltos": 0, "ec1": "4 paquetes y 2 sueltos", "ec2": "3 paquetes y 12 sueltos",
  "voz": ["Mirá cómo se hace un *canje*.", "Hay 4 paquetes y 2 sueltos.", "¡Abrimos un paquete! Salen *10 sueltos*.", "Antes: 4 paquetes y 2 sueltos.", "¡Ahora: *3 paquetes y 12 sueltos*!"], "sticker": {"txt": "💥", "paso": 2}},
 {"t": "columnas", "a": "352", "b": "128", "op": "−", "resultado": "224", "marcas": [{"col": "U", "txt": "12", "paso": 1}], "tachar": [{"col": "D", "nuevo": "4", "paso": 1}], "titulo": "EL CANJE",
  "voz": ["Hacemos la resta en columnas.", "2 menos 8 no alcanza: el 5 pasa a 4.", "Decenas: 4 menos 2, *2*.", "Centenas: 3 menos 1, *2*. ¡Quedan *224*!"]},
 {"t": "vof", "afirmacion": "En 352 − 128, hago 8 − 2", "emoji": "🤔", "verdadero": False, "explicacion": "No se da vuelta: abro un paquete",
  "voz": ["¿Verdadero o falso? Hago 8 menos 2.", "Pensá: ¿se puede dar vuelta?", "¡*Falso*! Abrimos un paquete."]},
 {"t": "pistas", "problema": "¿Cuánto es 463 − 247?", "pistas": ["3 − 7 no alcanza: 13 − 7 = 6", "El 6 pasa a 5: 5 − 4 = 1", "4 − 2 = 2"], "respuesta": "216",
  "voz": ["Ahora vos: 463 menos 247.", "Pista uno: abrí un paquete. 13 menos 7, *6*.", "Pista dos: 5 menos 4, *1*.", "Pista tres: 4 menos 2, *2*.", "¡Quedan *216*!"]},
 {"t": "resumen", "items": [["NO ALCANZA", "arriba hay menos"], ["CANJE", "1 paquete = 10 sueltos"], ["DESPUÉS", "un paquete menos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Si arriba hay menos, *no alcanza*.", "Abrimos un paquete: *10 sueltos* más.", "Y queda *un paquete menos*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "¿Cómo sabés si una resta está bien?", "segundos": 6, "respuesta": "¡Con una suma!", "emoji": "🕵️", "titulo": "CONTROLAR", "sub": "con la suma",
  "voz": ["Desafío: ¿cómo sabés si una resta está bien?", "¡Con una *suma*!", "Hoy: *controlar una resta con la suma*."]},
 {"t": "historieta", "titulo": "IDA Y VUELTA", "vinetas": [{"emojis": ["📦", "🚚"], "txt": "352 − 128 = 224", "quien": "Rosa"}, {"emojis": ["🚚", "📦"], "txt": "224 + 128 = 352", "quien": "Rosa"}, {"emojis": ["✅"], "txt": "¡Volví al principio!", "quien": "Rosa"}],
  "voz": ["Rosa tenía 352, vendió 128 y le quedan 224.", "Si le devuelven los 128: 224 más 128.", "¡Vuelve a *352*! La resta está bien."]},
 {"t": "cuenta", "filas": ["224", "128"], "op": "+", "resultado": "352",
  "voz": ["Sumamos el resultado y lo que restamos: 224 más 128.", "¡Da *352*: el número de arriba!"]},
 {"t": "versus", "titulo": "¿QUIÉN ACERTÓ?", "a": {"txt": "463 − 247 = 216", "emoji": "✅", "datos": ["216 + 247 = 463"]}, "b": {"txt": "463 − 247 = 226", "emoji": "❌", "datos": ["226 + 247 = 473"]}, "gana": "a", "veredicto": "¡216 vuelve al 463!",
  "voz": ["Dos chicos hicieron 463 menos 247.", "Uno dice 216: 216 más 247 da *463*.", "Otro dice 226: la suma da *473*.", "¡Acertó el *216*!"]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Resta", "emoji": "👹"}, "preguntas": [{"p": "342 + 234 = ?", "r": "576"}, {"p": "433 + 432 = ?", "r": "865"}],
  "voz": ["¡Volvió el *Monstruo Resta*!", "Controlamos sus restas con sumas.", "342 más 234: *576*.", "¡433 más 432: *865*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["CONTROLAR", "con una suma"], ["SUMAR", "resultado + lo restado"], ["COMPARAR", "con el de arriba"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Controlamos la resta con una *suma*.", "Sumamos el resultado y *lo que restamos*.", "Tiene que dar *el número de arriba*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m10-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 10 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
