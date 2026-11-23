# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 7 · Cálculo mental de sumas: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (sueltos, paquetes de 10 y cajas de 100).
Regla de primeros años (tools/medio/primeros_anios.py). Genera tools/medio/clase/lecciones/medio-mat2-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '4b3c7bcf-ea0e-4c96-8d5c-4cc4d731891b', 2: 'bafb5757-89d3-40d7-ba51-0c2d180c459b', 3: '4ee85131-a3a4-470f-af42-54858d5491da', 4: '3c1f2efc-c397-4b2f-999e-a8902ec8ad0b'}
TIT = {1: 'Sumar decenas y centenas', 2: 'Complementos a 100', 3: 'Sumar descomponiendo', 4: 'Sumas de memoria'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa tiene 3 cajas.", "Le traen 2 cajas más.", "¿Cuántos alfajores hay?"], "titulo": "SUMAR", "sub": "decenas y centenas",
  "voz": ["Rosa tiene *3 cajas* de alfajores.", "Le traen *2 cajas* más.", "¿Cuántos alfajores hay ahora?", "Hoy: *sumar decenas y centenas*."]},
 {"t": "transforma", "titulo": "LA CUENTA CHICA", "pasos": [{"txt": "3 + 2 = 5", "nota": "la cuenta chica"}, {"txt": "300 + 200", "nota": "cajas de 100"}, {"txt": "300 + 200 = 500"}],
  "voz": ["Primero pensamos la cuenta chica: 3 más 2 es 5.", "Pero son cajas de 100.", "¡300 más 200 es *500*!"], "sticker": {"txt": "🤯", "paso": 2}},
 {"t": "historieta", "titulo": "EL TRUCO DE ROSA", "vinetas": [{"emojis": ["👵"], "txt": "4 + 3 = 7", "quien": "Rosa"}, {"emojis": ["📦"], "txt": "40 + 30 = 70", "quien": "Rosa"}, {"emojis": ["🚚"], "txt": "400 + 300 = 700", "quien": "Rosa"}],
  "voz": ["Rosa sabe que 4 más 3 es *7*.", "Entonces 40 más 30 es *70*.", "¡Y 400 más 300 es *700*!"]},
 {"t": "vof", "afirmacion": "200 + 300 = 50", "emoji": "🤔", "verdadero": False, "explicacion": "Son 5 cajas: 500",
  "voz": ["¿Verdadero o falso? 200 más 300 es 50.", "Pensá en las cajas…", "¡*Falso*! Son cinco cajas: *500*."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 50 + 40?", "opciones": ["90", "9", "900"], "correcta": 0,
  "voz": ["Ahora vos. 50 más 40.", "Pensá: 5 más 4 es 9.", "¡*90*! Nueve paquetes."]},
 {"t": "resumen", "items": [["CAJAS", "300 + 200 = 500"], ["PAQUETES", "40 + 30 = 70"], ["TRUCO", "la cuenta chica"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cajas: 300 más 200 es *500*.", "Paquetes: 40 más 30 es *70*.", "El truco: pensá la *cuenta chica*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cuánto le falta a 70 para llegar a 100?", "segundos": 6, "respuesta": "¡30!", "emoji": "📦", "titulo": "COMPLEMENTOS", "sub": "a 100",
  "voz": ["Desafío: ¿cuánto le falta a 70 para 100?", "¡*30*! 70 más 30 es 100.", "Hoy: *complementos a 100*."]},
 {"t": "recta", "min": 0, "max": 100, "paso": 10, "marcas": [{"v": 70, "txt": "70"}, {"v": 100, "txt": "100"}],
  "voz": ["Rosa tiene 70 alfajores en la caja.", "Están en el *70*.", "Para llenar la caja faltan 3 paquetes: *30*."]},
 {"t": "unir", "titulo": "PAREJAS DE 100", "pares": [["60", "40"], ["80", "20"], ["90", "10"]],
  "voz": ["Uní las parejas que suman 100.", "60 con *40*.", "80 con *20*.", "90 con *10*."]},
 {"t": "jefe", "jefe": {"nombre": "Señor Cien", "emoji": "👾"}, "preguntas": [{"p": "50 + ? = 100", "r": "50"}, {"p": "30 + ? = 100", "r": "70"}, {"p": "45 + ? = 100", "r": "55"}],
  "voz": ["¡Apareció el *Señor Cien*!", "Para ganarle, completamos el 100.", "50 más *50*.", "30 más *70*.", "¡Y 45 más *55*! ¡Le ganamos!"], "sticker": {"txt": "💥", "paso": 4}},
 {"t": "errores", "items": [{"mal": "A 70 le faltan 3", "bien": "A 70 le faltan 30"}],
  "voz": ["Ojo con este error.", "A 70 le faltan *30*, no 3."]},
 {"t": "resumen", "items": [["PAREJAS DE 10", "7 + 3"], ["PAREJAS DE 100", "70 + 30"], ["COMPLEMENTO", "lo que falta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "7 más 3 es 10.", "Entonces 70 más 30 es *100*.", "El *complemento* es lo que falta.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿cuánto es 245 + 32?"}, {"yo": True, "txt": "¡Desarmalo!"}, {"yo": False, "txt": "¿Cómo?"}], "titulo": "SUMAR", "sub": "descomponiendo",
  "voz": ["Tomi le escribe a Rosa.", "¿Cuánto es 245 más 32?", "Rosa le contesta: ¡desarmalo!", "Hoy: *sumar descomponiendo*."]},
 {"t": "descomponer", "numero": "245", "titulo": "DESARMAMOS EL 245", "partes": ["200", "40", "5"], "resultado": "= 245 ✓",
  "voz": ["Primero desarmamos el *245*.", "Cajas, paquetes y sueltos.", "200, 40 y 5.", "El 32 es 30 y 2.", "¡Ya tenemos todas las partes!"]},
 {"t": "pizarra", "titulo": "PARTE POR PARTE", "lineas": [{"txt": "Cajas: 200", "color": "sol"}, {"txt": "40 + 30 = 70", "color": "coral"}, {"txt": "5 + 2 = 7", "color": "verde"}, {"txt": "200 + 70 + 7 = 277", "color": "sol", "marca": "circulo"}],
  "voz": ["Las cajas: *200*.", "Paquetes con paquetes: 40 más 30, *70*.", "Sueltos con sueltos: 5 más 2, *7*.", "¡Todo junto: *277*!"]},
 {"t": "versus", "titulo": "¿CUÁL ESTÁ BIEN?", "a": {"txt": "277", "emoji": "✅", "datos": ["paquetes con paquetes"]}, "b": {"txt": "565", "emoji": "❌", "datos": ["mezcla los lugares"]}, "gana": "a", "veredicto": "¡Cada parte con su igual!",
  "voz": ["Dos chicos sumaron 245 más 32.", "Uno juntó paquetes con paquetes: 277.", "El otro mezcló los lugares: 565.", "¡Gana el *277*! Cada parte con su igual."]},
 {"t": "pregunta", "pregunta": "¿Cuánto es 123 + 45?", "opciones": ["168", "573", "158"], "correcta": 0,
  "voz": ["Ahora vos. 123 más 45.", "Desarmá: 100, 20 más 40, 3 más 5.", "¡*168*!"]},
 {"t": "resumen", "items": [["DESARMAR", "cajas, paquetes, sueltos"], ["SUMAR", "cada uno con su igual"], ["JUNTAR", "todo al final"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Desarmamos* en cajas, paquetes y sueltos.", "Sumamos cada parte con *su igual*.", "Al final, *juntamos* todo.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Carrera de sumas!", "bajada": "Gana quien suma sin papel", "emoji": "🏁", "titulo": "SUMAS", "sub": "de memoria",
  "voz": ["¡Último momento: carrera de sumas en la fábrica!", "Gana quien suma *sin papel*.", "Hoy: *sumas de memoria*."]},
 {"t": "calculadora", "teclas": ["2", "5", "4", "+", "1", "0"], "resultado": "264", "texto": "254 + 10 = 264", "titulo": "MÁS 10",
  "voz": ["Tomi prueba: 254 más 10.", "Aprieta las teclas…", "¡*264*! Solo cambió el del medio."]},
 {"t": "patron", "titulo": "LOS DOBLES", "items": ["10 + 10 = 20", "20 + 20 = 40", "30 + 30 = 60"], "falta": "40 + 40 = 80", "regla": "Un número más él mismo",
  "voz": ["Mirá estos *dobles*: 10, 20 y 30.", "¿Qué sigue?", "¡40 más 40 es *80*!"]},
 {"t": "quiz4", "pregunta": "¿Cuánto es 365 + 100?", "opciones": ["465", "375", "366"], "correcta": 0,
  "voz": ["Ahora vos. 365 más 100.", "¿Qué cifra cambia?", "¡*465*! Cambian las centenas."]},
 {"t": "jefe", "jefe": {"nombre": "Robot Suma", "emoji": "🤖"}, "preguntas": [{"p": "60 + 40", "r": "100"}, {"p": "200 + 200", "r": "400"}, {"p": "123 + 10", "r": "133"}],
  "voz": ["¡El *Robot Suma* te desafía!", "Respondé rápido.", "60 más 40: *100*.", "200 más 200: *400*.", "¡123 más 10: *133*! ¡Ganaste!"]},
 {"t": "resumen", "items": [["+ 10", "cambian decenas"], ["+ 100", "cambian centenas"], ["DOBLES", "un número + él mismo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Más 10 cambia las *decenas*.", "Más 100 cambia las *centenas*.", "Los *dobles* son fáciles de recordar.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m7-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 7 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
