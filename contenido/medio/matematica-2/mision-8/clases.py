# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 8 · Cálculo mental de restas: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (los alfajores que se venden).
Regla de primeros años (tools/medio/primeros_anios.py). Genera tools/medio/clase/lecciones/medio-mat2-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '7c11ff24-8c12-43a8-b49d-d8300b2eda58', 2: '71ea8741-f828-4205-9d20-51e67ff8d933', 3: '68563df7-4429-4a7a-8f96-c9e5d334287e', 4: '12195659-61b9-4ee1-ad76-678c61b0297d'}
TIT = {1: 'Restar decenas y unidades de memoria', 2: 'Restar contando hacia adelante', 3: 'Restar descomponiendo', 4: 'Restas de memoria'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa tenía 5 cajas.", "Vendió 2 cajas.", "¿Cuántas le quedan?"], "titulo": "RESTAR", "sub": "de memoria",
  "voz": ["Rosa tenía *5 cajas* de alfajores.", "Hoy vendió *2 cajas*.", "¿Cuántos alfajores le quedan?", "Hoy: *restar de memoria*."]},
 {"t": "sacar", "emoji": "📦", "n": 5, "menos": 2, "texto": "5 − 2 = 3",
  "voz": ["Mirá las cinco cajas de Rosa.", "Se van dos cajas en el camión.", "¡Quedan *3 cajas*: 300 alfajores!"]},
 {"t": "transforma", "titulo": "LA CUENTA CHICA", "pasos": [{"txt": "8 − 3 = 5"}, {"txt": "80 − 30 = 50", "nota": "paquetes"}, {"txt": "800 − 300 = 500", "nota": "cajas"}],
  "voz": ["Si sabés que 8 menos 3 es 5…", "…sabés que 80 menos 30 es *50*.", "¡Y que 800 menos 300 es *500*!"]},
 {"t": "vof", "afirmacion": "47 − 5 = 2", "emoji": "🤔", "verdadero": False, "explicacion": "Solo cambian los sueltos: 42",
  "voz": ["¿Verdadero o falso? 47 menos 5 es 2.", "Pensá: ¿qué cambia, los paquetes o los sueltos?", "¡*Falso*! Solo cambian los sueltos: *42*."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 90 − 60?", "opciones": ["30", "3", "300"], "correcta": 0,
  "voz": ["Ahora vos. 90 menos 60.", "Pensá: 9 menos 6 es 3.", "¡*30*! Tres paquetes."]},
 {"t": "resumen", "items": [["CAJAS", "500 − 200 = 300"], ["PAQUETES", "80 − 30 = 50"], ["SUELTOS", "47 − 5 = 42"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cajas: 500 menos 200 es *300*.", "Paquetes: 80 menos 30 es *50*.", "Sueltos: 47 menos 5 es *42*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿cuántos vendiste?"}, {"yo": True, "txt": "Tenía 100 y me quedan 70"}, {"yo": False, "txt": "¡Contemos!"}], "titulo": "RESTAR", "sub": "contando para adelante",
  "voz": ["Tomi le pregunta a Rosa cuántos vendió.", "Tenía 100 y le quedan 70.", "¡Contemos para saberlo!", "Hoy: *restar contando hacia adelante*."]},
 {"t": "saltos", "titulo": "DE 70 A 100", "min": 60, "max": 100, "cada": 10, "inicio": 70, "saltos": [{"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}, {"a": 10, "txt": "+10"}],
  "voz": ["Empezamos en el número chico: 70.", "Un salto: *80*.", "Dos saltos: *90*.", "¡Tres saltos: *100*! Vendió *30*."]},
 {"t": "personaje", "personaje": ROSA, "lineas": [{"txt": "Contá los saltos", "animo": "ojo"}, {"txt": "¡No los números!", "animo": "sorpresa"}],
  "voz": ["Rosa avisa: contá los *saltos*.", "¡No cuentes los números!"]},
 {"t": "tren", "desde": 300, "hasta": 500, "paso": 100, "titulo": "500 − 300",
  "voz": ["Ahora 500 menos 300.", "300, 400, 500.", "¡Dos saltos de 100: *200*!"]},
 {"t": "completa", "antes": "100 − 80 =", "despues": "", "opciones": ["20", "2", "180"], "correcta": 0,
  "voz": ["Completá: 100 menos 80.", "Desde 80: 90, 100.", "¡*20*! Dos saltos de 10."]},
 {"t": "resumen", "items": [["CONTAR", "del chico al grande"], ["SALTOS DE 10", "100 − 70 = 30"], ["SALTOS DE 100", "500 − 300 = 200"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos *del chico al grande*.", "De 70 a 100 hay *30*.", "De 300 a 500 hay *200*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Rosa tiene 365 y vende 42. ¿Cuántos quedan?", "segundos": 8, "respuesta": "¡323!", "emoji": "🚚", "titulo": "RESTAR", "sub": "descomponiendo",
  "voz": ["Desafío: Rosa tiene 365 y vende 42.", "¡Le quedan *323*!", "Hoy: *restar descomponiendo*."]},
 {"t": "cdu", "c": 3, "d": 6, "u": 5, "texto": "365 alfajores",
  "voz": ["Mirá lo que tiene Rosa.", "Las cajas: 100, 200, 300.", "Los paquetes: 310, 320, 330, 340, 350, 360.", "Los sueltos: 361, 362, 363, 364, 365.", "¡Tiene *365 alfajores*!"]},
 {"t": "pizarra", "titulo": "365 − 42", "lineas": [{"txt": "42 = 40 + 2", "color": "azul"}, {"txt": "60 − 40 = 20", "color": "coral"}, {"txt": "5 − 2 = 3", "color": "verde"}, {"txt": "300 + 20 + 3 = 323", "color": "sol", "marca": "circulo"}],
  "voz": ["Desarmamos el 42: 40 y 2.", "Paquetes: 60 menos 40, *20*.", "Sueltos: 5 menos 2, *3*.", "¡Quedan 300, 20 y 3: *323*!"]},
 {"t": "pistas", "problema": "¿Cuánto es 178 − 35?", "pistas": ["Cajas: 100", "70 − 30 = 40", "8 − 5 = 3"], "respuesta": "143",
  "voz": ["Ahora vos: 178 menos 35.", "Pista uno: la caja queda, *100*.", "Pista dos: 70 menos 30, *40*.", "Pista tres: 8 menos 5, *3*.", "¡Quedan *143*!"]},
 {"t": "errores", "items": [{"mal": "Restar 40 de los sueltos", "bien": "Paquetes de paquetes"}],
  "voz": ["Ojo con este error.", "Restá *paquetes de paquetes*, sueltos de sueltos."]},
 {"t": "resumen", "items": [["DESARMAR", "42 = 40 + 2"], ["RESTAR", "cada parte de su igual"], ["JUNTAR", "lo que queda"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Desarmamos* el número que restamos.", "Restamos cada parte de *su igual*.", "Al final, *juntamos* lo que queda.", CIERRE]},
]
N4 = [
 {"t": "gancho", "emoji": "🧠", "final": "⚡", "titulo": "RESTAS", "sub": "de memoria",
  "voz": ["¿Se puede restar *sin papel*?", "¡Sí! Con trucos que ya sabés.", "Hoy: *restas de memoria*."]},
 {"t": "versus", "titulo": "¿QUÉ CAMBIA?", "a": {"txt": "364 − 10", "emoji": "📦", "datos": ["= 354", "cambian decenas"]}, "b": {"txt": "364 − 100", "emoji": "🚚", "datos": ["= 264", "cambian centenas"]}, "gana": "empate", "veredicto": "¡Cambia una sola cifra!",
  "voz": ["Comparamos dos restas.", "364 menos 10 es *354*.", "364 menos 100 es *264*.", "¡En las dos cambia *una sola cifra*!"]},
 {"t": "memoria", "titulo": "PAREJAS DE 100", "items": ["100 − 60 = 40", "100 − 90 = 10", "100 − 50 = 50", "100 − 20 = 80"], "falta": 1,
  "voz": ["Mirá estas restas desde 100.", "Se tapan… ¡y una desapareció!", "¡Faltaba 100 menos 90: *10*!"]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "800 − 100", "r": "700"}, {"p": "100 − 30", "r": "70"}, {"p": "256 − 10", "r": "246"}],
  "voz": ["¡Ronda rápida de restas!", "800 menos 100: *700*.", "100 menos 30: *70*.", "256 menos 10: *246*."], "sticker": {"txt": "⚡", "paso": 3}},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Resta", "emoji": "👹"}, "preguntas": [{"p": "500 − 300", "r": "200"}, {"p": "100 − 70", "r": "30"}],
  "voz": ["¡Apareció el *Monstruo Resta*!", "Dos restas y lo vencemos.", "500 menos 300: *200*.", "¡100 menos 70: *30*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["− 10", "cambian decenas"], ["− 100", "cambian centenas"], ["DESDE 100", "usá las parejas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Menos 10 cambia las *decenas*.", "Menos 100 cambia las *centenas*.", "Desde 100, usá las *parejas*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m8-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 8 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
