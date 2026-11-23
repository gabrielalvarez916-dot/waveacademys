# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 11 · Problemas de suma y resta: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (pedidos que llegan y se van).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat2-m11-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'bcfff097-dfca-4c0b-b128-0acf8b0f7b09', 2: '707a8c81-25ba-48ab-ab38-4d66942bd600', 3: '3aaa945b-66ca-43fe-a479-ce6ebc64b25d', 4: 'd7b5a7b9-6d8d-42ad-8d5d-b0114b41c7c3'}
TIT = {1: 'Agregar y quitar', 2: 'Comparar en problemas de dos pasos', 3: 'Completar hasta un número', 4: 'Problemas con varias cuentas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa tenía 230 alfajores.", "Hizo 150 más.", "¿Suma o resta?"], "titulo": "AGREGAR", "sub": "y quitar",
  "voz": ["Rosa tenía *230* alfajores.", "Hoy hizo *150* más.", "¿Hay que sumar o restar?", "Hoy: *agregar y quitar*."]},
 {"t": "clasificar", "cajas": [{"cab": "SUMAR", "emoji": "➕"}, {"cab": "RESTAR", "emoji": "➖"}], "fichas": [{"txt": "llegan", "caja": 0}, {"txt": "hizo más", "caja": 0}, {"txt": "se fueron", "caja": 1}, {"txt": "vendió", "caja": 1}],
  "voz": ["Hay palabras que nos ayudan.", "Si llegan o hace más, *sumamos*.", "Si se van o vende, *restamos*."]},
 {"t": "columnas", "a": "230", "b": "150", "op": "+", "resultado": "380", "titulo": "LLEGAN MÁS",
  "voz": ["Rosa hizo más: sumamos 230 más 150.", "Unidades: 0 más 0, *0*.", "Decenas: 3 más 5, *8*.", "Centenas: 2 más 1, *3*. ¡Tiene *380*!"]},
 {"t": "dilema", "situacion": "Rosa tenía 380 y vendió 120. ¿Qué cuenta hace?", "emoji": "🤔", "a": {"txt": "380 + 120", "consecuencia": "¡No! Vendió: se van", "emoji": "❌"}, "b": {"txt": "380 − 120", "consecuencia": "¡Sí! Le quedan 260", "emoji": "✅"},
  "voz": ["Rosa tenía 380 y vendió 120.", "Si suma, se equivoca: ¡los alfajores se fueron!", "Si resta, acierta: le quedan *260*."]},
 {"t": "pregunta", "pregunta": "En el colectivo iban 48. Bajaron 15. ¿Qué cuenta hacés?", "opciones": ["48 − 15", "48 + 15"], "correcta": 0,
  "voz": ["Ahora vos. Iban 48 y bajaron 15.", "¿Sumás o restás?", "¡*Restamos*! Bajaron: se van."]},
 {"t": "resumen", "items": [["AGREGAR", "sumamos"], ["QUITAR", "restamos"], ["RESPUESTA", "con palabras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Si llegan más, *sumamos*.", "Si se van, *restamos*.", "La respuesta se escribe *con palabras*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Ana", "emoji": "👩‍🍳"}, "mensajes": [{"yo": False, "txt": "Hoy hice 320 alfajores 😎"}, {"yo": True, "txt": "¡Yo hice 450!"}, {"yo": False, "txt": "¿Cuántos más que yo?"}], "titulo": "COMPARAR", "sub": "cuántos más",
  "voz": ["Ana, la vecina, le escribe a Rosa.", "Ana hizo 320. Rosa hizo 450.", "¿Cuántos más hizo Rosa?", "Hoy: *comparar en problemas*."]},
 {"t": "balanza", "izq": {"cab": "ROSA", "items": ["450"]}, "der": {"cab": "ANA", "items": ["320"]}, "gana": "izq",
  "voz": ["Ponemos los dos en la balanza.", "Rosa: 450. Ana: 320.", "¡Rosa hizo *más*!"]},
 {"t": "transforma", "titulo": "¿CUÁNTOS MÁS?", "pasos": [{"txt": "450 y 320", "nota": "grande y chico"}, {"txt": "450 − 320"}, {"txt": "= 130", "nota": "Rosa hizo 130 más"}],
  "voz": ["Tenemos el grande y el chico.", "Restamos el chico al grande: 450 menos 320.", "¡*130*! Rosa hizo 130 más."]},
 {"t": "vof", "afirmacion": "Para saber cuántos más, siempre sumo", "emoji": "🤔", "verdadero": False, "explicacion": "Se resta el chico al grande",
  "voz": ["¿Verdadero o falso? Para saber cuántos más, sumo.", "Pensá en Rosa y Ana…", "¡*Falso*! Restamos el chico al grande."]},
 {"t": "pregunta", "pregunta": "Un camión lleva 580 y otro 350. ¿Cuántos más lleva el primero?", "opciones": ["230", "930", "220"], "correcta": 0,
  "voz": ["Ahora vos. 580 y 350.", "¿Cuántos más lleva el primero?", "¡*230*! 580 menos 350."]},
 {"t": "resumen", "items": [["MÁS", "el número grande"], ["CUÁNTOS MÁS", "restamos"], ["DIFERENCIA", "lo que hay de más"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El que tiene *más* tiene el número grande.", "Para saber *cuántos más*, restamos.", "Eso es la *diferencia*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Rosa tiene 350 y tiene que entregar 500. ¿Cuántos faltan?", "segundos": 8, "respuesta": "¡150!", "emoji": "🎯", "titulo": "COMPLETAR", "sub": "hasta un número",
  "voz": ["Desafío: Rosa tiene 350 y necesita 500.", "¡Le faltan *150*!", "Hoy: *completar hasta un número*."]},
 {"t": "saltos", "titulo": "DE 350 A 500", "min": 300, "max": 500, "cada": 50, "inicio": 350, "saltos": [{"a": 50, "txt": "+50"}, {"a": 100, "txt": "+100"}],
  "voz": ["Empezamos en lo que hay: 350.", "Un salto de 50: llegamos a *400*.", "Un salto de 100: ¡*500*! Faltaban *150*."]},
 {"t": "escala", "titulo": "LO QUE FALTA", "items": [{"txt": "hay 350", "emoji": "📦", "valor": 350}, {"txt": "quiero 500", "emoji": "🚚", "valor": 500}],
  "voz": ["Lo que hay: *350*.", "Lo que queremos: *500*. Faltan 150."]},
 {"t": "completa", "antes": "70 +", "despues": "= 100", "opciones": ["30", "170", "3"], "correcta": 0,
  "voz": ["Tomi tiene 70 figuritas y quiere 100.", "70 más ¿cuánto? es 100.", "¡*30*! Le faltan 30."]},
 {"t": "errores", "items": [{"mal": "Sumar lo que hay y lo que quiero", "bien": "Contar desde lo que hay"}],
  "voz": ["Ojo con este error.", "No sumes los dos: contá *desde lo que hay*."]},
 {"t": "resumen", "items": [["FALTA", "lo que hay que agregar"], ["CONTAR", "desde lo que hay"], ["RESTAR", "quiero − hay"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Falta* es lo que hay que agregar.", "Contamos *desde lo que hay*.", "O restamos: lo que quiero menos lo que hay.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Día movido en la fábrica!", "bajada": "Llegan y se van alfajores", "emoji": "🏭", "titulo": "VARIAS", "sub": "cuentas",
  "voz": ["¡Último momento: día movido en la fábrica!", "Hacen alfajores y después venden.", "Hoy: *problemas con varias cuentas*."]},
 {"t": "historieta", "titulo": "EL DÍA DE ROSA", "vinetas": [{"emojis": ["📦"], "txt": "Tenía 400", "quien": "Rosa"}, {"emojis": ["👩‍🍳", "➕"], "txt": "Hice 200 más: 600", "quien": "Rosa"}, {"emojis": ["🚚", "➖"], "txt": "Vendí 350: quedan 250", "quien": "Rosa"}],
  "voz": ["A la mañana, Rosa tenía *400*.", "Hizo 200 más: 400 más 200, *600*.", "Vendió 350: 600 menos 350, *250*."]},
 {"t": "pasos", "titulo": "CÓMO LO RESUELVO", "items": [{"txt": "Leo todo", "emoji": "👀"}, {"txt": "Primera cuenta", "emoji": "1️⃣"}, {"txt": "Uso ese resultado", "emoji": "2️⃣"}],
  "voz": ["¿Cómo resolvemos estos problemas?", "Primero *leemos todo*.", "Hacemos la *primera cuenta*.", "Y usamos ese resultado en la *segunda*."]},
 {"t": "pistas", "problema": "En el colectivo iban 30. Subieron 15 y bajaron 20. ¿Cuántos van?", "pistas": ["Subieron: 30 + 15 = 45", "Bajaron: 45 − 20 = 25"], "respuesta": "Van 25 personas",
  "voz": ["Ahora vos: iban 30, subieron 15, bajaron 20.", "Pista uno: subieron, sumamos. *45*.", "Pista dos: bajaron, restamos. *25*.", "¡Van *25* personas!"]},
 {"t": "jefe", "jefe": {"nombre": "Señor Problema", "emoji": "🧙"}, "preguntas": [{"p": "300 + 100 − 250", "r": "150"}, {"p": "50 + 30 − 10", "r": "70"}],
  "voz": ["¡Apareció el *Señor Problema*!", "Lo vencemos paso por paso.", "300 más 100 menos 250: *150*.", "¡50 más 30 menos 10: *70*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["LEER", "todo el problema"], ["PRIMER PASO", "una cuenta"], ["SEGUNDO PASO", "con ese resultado"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos *todo* el problema.", "Hacemos la *primera cuenta*.", "Con ese resultado, la *segunda*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m11-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 11 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
