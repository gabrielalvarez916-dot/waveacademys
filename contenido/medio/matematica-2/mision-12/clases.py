# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 12 · Propiedades de la suma: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa.
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat2-m12-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'ed6db453-0ca6-4513-8b32-45ed961bd7c3', 2: 'c97d4a72-4344-459b-a98f-6f36101956c7', 3: '67350050-4158-475b-b56a-ea79a9d5539c', 4: 'c4c9e3e8-3b94-48a9-860b-0966c7fa9589'}
TIT = {1: 'Cambiar el orden de los números', 2: 'Agrupar para calcular mejor', 3: 'Usar sumas conocidas para resolver nuevas', 4: 'La suma y la resta se relacionan'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿30 + 40 o 40 + 30?"}, {"yo": True, "txt": "¡Da lo mismo!"}, {"yo": False, "txt": "¿En serio? 😮"}], "titulo": "CAMBIAR", "sub": "el orden",
  "voz": ["Tomi le pregunta a Rosa.", "¿Es igual 30 más 40 que 40 más 30?", "Rosa dice: ¡da lo mismo!", "Hoy: *cambiar el orden de los números*."]},
 {"t": "juntar", "a": {"emoji": "🍫", "n": 3}, "b": {"emoji": "🍪", "n": 4}, "texto": "3 + 4 = 4 + 3 = 7",
  "voz": ["Tres alfajores de chocolate.", "Cuatro de dulce.", "¡Juntos son 7, en cualquier orden!"]},
 {"t": "vof", "afirmacion": "30 + 40 da lo mismo que 40 + 30", "emoji": "🔄", "verdadero": True, "explicacion": "En la suma, el orden no cambia",
  "voz": ["Mirá: 30 más 40 es igual a 40 más 30.", "¿Verdadero o falso? Pensá en los alfajores…", "¡*Verdadero*! Los dos dan *70*."]},
 {"t": "saltos", "titulo": "DESDE EL GRANDE", "min": 95, "max": 100, "cada": 1, "inicio": 98, "saltos": [{"a": 1, "txt": "+1"}, {"a": 1, "txt": "+1"}],
  "voz": ["2 más 98 es difícil. ¡Lo damos vuelta!", "98 más 1: *99*.", "Más 1: ¡*100*! Mucho más fácil."]},
 {"t": "errores", "items": [{"mal": "8 − 3 = 3 − 8", "bien": "En la resta no se da vuelta"}],
  "voz": ["Ojo con este error.", "En la *resta* no se puede dar vuelta."]},
 {"t": "resumen", "items": [["ORDEN", "no cambia la suma"], ["TRUCO", "empezá por el grande"], ["RESTA", "no se da vuelta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la suma, el *orden* no cambia el resultado.", "Conviene empezar por el *grande*.", "En la *resta* no se da vuelta.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa suma 37 + 25 + 3.", "¡Son tres números!", "¿Por dónde empieza?"], "titulo": "AGRUPAR", "sub": "para calcular mejor",
  "voz": ["Rosa tiene que sumar *tres números*.", "37, 25 y 3.", "¿Por cuál empieza?", "Hoy: *agrupar para calcular mejor*."]},
 {"t": "unir", "titulo": "PAREJAS AMIGAS", "pares": [["37", "3"], ["60", "40"], ["8", "2"]],
  "voz": ["Buscamos *parejas amigas*: dan redondo.", "37 y 3: *40*.", "60 y 40: *100*.", "8 y 2: *10*."]},
 {"t": "pizarra", "titulo": "37 + 25 + 3", "lineas": [{"txt": "37 + 3 = 40", "color": "sol", "marca": "circulo"}, {"txt": "40 + 25 = 65", "color": "verde"}],
  "voz": ["Primero juntamos los amigos: 37 más 3, *40*.", "Después: 40 más 25, ¡*65*!"]},
 {"t": "prediccion", "pregunta": "¿Cambia el resultado si junto distinto?", "a": {"txt": "Sí, cambia", "emoji": "😱"}, "b": {"txt": "No, da igual", "emoji": "😎"}, "correcta": "b", "resultado": "¡Da 65 de las dos formas!",
  "voz": ["¿Qué creés? Si junto distinto, ¿cambia el resultado?", "¿Sí o no? Pensá…", "¡*No*! Da 65 de las dos formas."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 70 + 18 + 30?", "opciones": ["118", "108", "128"], "correcta": 0,
  "voz": ["Ahora vos: 70 más 18 más 30.", "Juntá los amigos: 70 y 30.", "¡100 más 18: *118*!"]},
 {"t": "resumen", "items": [["AGRUPAR", "juntar los amigos"], ["REDONDO", "más fácil"], ["DESPUÉS", "lo que queda"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Juntamos primero los *amigos*.", "Así queda un número *redondo*.", "Después sumamos *lo que queda*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Si 25 + 25 = 50, ¿cuánto es 25 + 26?", "segundos": 6, "respuesta": "¡51!", "emoji": "🧠", "titulo": "SUMAS", "sub": "conocidas",
  "voz": ["Desafío: si 25 más 25 es 50…", "¡25 más 26 es *51*! Uno más.", "Hoy: *usar sumas conocidas*."]},
 {"t": "transforma", "titulo": "DEL DOBLE A OTRA", "pasos": [{"txt": "25 + 25 = 50", "nota": "lo que sé"}, {"txt": "25 + 26", "nota": "uno más"}, {"txt": "= 51"}],
  "voz": ["Rosa ya sabe un doble: 25 más 25 es 50.", "Ahora tiene 25 más 26: uno más.", "¡El resultado también sube uno: *51*!"]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["40 + 40 = 80", "40 + 41 = 81", "40 + 42 = 82"], "falta": "40 + 43 = 83", "regla": "Uno más, uno más",
  "voz": ["Mirá: 40 más 40, más 41, más 42.", "¿Qué sigue?", "¡40 más 43: *83*!"]},
 {"t": "versus", "titulo": "¿QUIÉN ACERTÓ?", "a": {"txt": "30 + 40 = 70", "emoji": "✅", "datos": ["sube 10"]}, "b": {"txt": "30 + 40 = 61", "emoji": "❌", "datos": ["sube 1"]}, "gana": "a", "veredicto": "¡40 es 10 más que 30!",
  "voz": ["Dos chicos usaron 30 más 30 es 60.", "Uno dice 30 más 40 es *70*.", "Otro dice *61*.", "¡Gana el 70! El 40 es *10 más*."]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "50 + 51", "r": "101"}, {"p": "100 + 99", "r": "199"}, {"p": "15 + 16", "r": "31"}],
  "voz": ["¡Ronda rápida de dobles!", "50 más 51: *101*.", "100 más 99: *199*.", "15 más 16: *31*."]},
 {"t": "resumen", "items": [["DOBLES", "los que ya sabés"], ["UNO MÁS", "resultado + 1"], ["UNO MENOS", "resultado − 1"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Usamos los *dobles* que ya sabemos.", "Si uno sube 1, el resultado *sube 1*.", "Si baja 1, el resultado *baja 1*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡La suma y la resta son familia!", "bajada": "Descubrimiento en la fábrica", "emoji": "👨‍👩‍👧", "titulo": "SUMA", "sub": "y resta",
  "voz": ["¡Último momento: la suma y la resta son familia!", "Lo descubrió Rosa en la fábrica.", "Hoy: *la suma y la resta se relacionan*."]},
 {"t": "memoria", "titulo": "LA FAMILIA", "items": ["25 + 15 = 40", "15 + 25 = 40", "40 − 15 = 25", "40 − 25 = 15"], "falta": 2,
  "voz": ["Mirá la familia de 25, 15 y 40.", "Se tapan… ¡y una desapareció!", "¡Faltaba 40 menos 15: *25*!"]},
 {"t": "historieta", "titulo": "IDA Y VUELTA", "vinetas": [{"emojis": ["📦", "➕"], "txt": "300 + 200 = 500", "quien": "Rosa"}, {"emojis": ["🚚", "➖"], "txt": "500 − 200 = 300", "quien": "Rosa"}],
  "voz": ["Rosa junta 300 y 200: *500*.", "Se llevan 200: ¡vuelve a *300*!"]},
 {"t": "completa", "antes": "Si 70 + 30 = 100, entonces 100 − 30 =", "despues": "", "opciones": ["70", "130", "30"], "correcta": 0,
  "voz": ["Completá: si 70 más 30 es 100…", "¿100 menos 30?", "¡*70*! La suma nos ayuda."]},
 {"t": "jefe", "jefe": {"nombre": "Robot Familia", "emoji": "🤖"}, "preguntas": [{"p": "45 + 55 = 100 → 100 − 55 = ?", "r": "45"}, {"p": "8 + 5 = 13 → 13 − 8 = ?", "r": "5"}],
  "voz": ["¡El *Robot Familia* te desafía!", "Usá la suma para la resta.", "100 menos 55: *45*.", "¡13 menos 8: *5*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["FAMILIA", "3 números, 4 cuentas"], ["SUMA", "junta"], ["RESTA", "deshace la suma"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Con 3 números armamos *4 cuentas*.", "La suma *junta*.", "La resta *deshace* la suma.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m12-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 12 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
