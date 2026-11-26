# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 15 · Multiplicar por 10 y por 100: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (paquetes de 10 y cajas de 100).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat2-m15-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'b73396c3-57c3-4333-a6f8-77dbcae4fa1d', 2: 'f7628e18-7953-4bd6-9881-ab5150aaa9c2', 3: '41055c46-b0f2-42cd-bb9e-ed10e7e5c2d0', 4: '5776913c-1be0-40f4-9925-bc19e0bcce5d'}
TIT = {1: 'Multiplicar por 10', 2: 'Multiplicar por 100', 3: 'Qué pasa con las cifras', 4: 'Problemas con 10 y 100'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "reto", "texto": "¿Cuántos alfajores hay en 4 paquetes de 10?", "segundos": 6, "respuesta": "¡40!", "emoji": "📦", "titulo": "POR 10", "sub": "paquetes",
  "voz": ["Desafío: 4 paquetes de 10 alfajores.", "¡*40*! 10, 20, 30, 40.", "Hoy: *multiplicar por 10*."]},
 {"t": "agrupar", "niveles": [{"nombre": "1 ALFAJOR", "valor": "1", "icono": "alf"}, {"nombre": "1 PAQUETE", "valor": "10", "icono": "pack"}], "salto": "×10",
  "voz": ["Diez alfajores llenan un paquete.", "Un paquete tiene *10*.", "Contamos paquetes de 10 en 10."]},
 {"t": "definicion", "palabra": "Por 10", "texto": "Agregamos un 0 al final", "emoji": "0️⃣",
  "voz": ["Multiplicar por 10 tiene un truco.", "Agregamos *un cero* al final."]},
 {"t": "transforma", "titulo": "UN 0 AL FINAL", "pasos": [{"txt": "6 × 10"}, {"txt": "6 → 60", "nota": "agregamos un 0"}, {"txt": "6 × 10 = 60"}],
  "voz": ["Mirá: 6 por 10.", "Al 6 le pegamos un *cero*.", "¡6 por 10 es *60*!"]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["10", "20", "30", "40"], "falta": "50", "regla": "Sumamos un paquete",
  "voz": ["Mirá: 10, 20, 30, 40…", "¿Qué número sigue?", "¡El *50*! Cinco paquetes."]},
 {"t": "vof", "afirmacion": "7 × 10 = 17", "emoji": "🤔", "verdadero": False, "explicacion": "No se suma: es 70",
  "voz": ["¿Verdadero o falso? 7 por 10 es 17.", "Pensá en los paquetes…", "¡*Falso*! Es *70*."]},
 {"t": "resumen", "items": [["PAQUETE", "tiene 10"], ["POR 10", "un 0 al final"], ["7 × 10", "es 70"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un paquete tiene *10*.", "Por 10, *un cero* al final.", "7 por 10 es *70*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa llena cajas grandes.", "En cada caja entran 100.", "¿Cuántos hay en 3 cajas?"], "titulo": "POR 100", "sub": "cajas",
  "voz": ["Rosa llena *cajas grandes*.", "En cada caja entran *100* alfajores.", "¿Cuántos hay en 3 cajas?", "Hoy: *multiplicar por 100*."]},
 {"t": "escala", "titulo": "CAJAS QUE CRECEN", "items": [{"txt": "100", "emoji": "📦", "valor": 100}, {"txt": "200", "emoji": "📦", "valor": 200}, {"txt": "300", "emoji": "📦", "valor": 300}],
  "voz": ["Una caja: *100*.", "Dos cajas: *200*.", "¡Tres cajas: *300*!"]},
 {"t": "transforma", "titulo": "DOS CEROS", "pasos": [{"txt": "4 × 100"}, {"txt": "4 → 400", "nota": "agregamos dos 0"}, {"txt": "4 × 100 = 400"}],
  "voz": ["Ahora: 4 por 100.", "Al 4 le pegamos *dos ceros*.", "¡4 por 100 es *400*!"]},
 {"t": "unir", "titulo": "UNÍ", "pares": [["2 × 100", "200"], ["5 × 100", "500"], ["8 × 100", "800"]],
  "voz": ["Uní cada cuenta con su resultado.", "2 por 100: *200*.", "5 por 100: *500*.", "8 por 100: *800*."]},
 {"t": "quiz4", "pregunta": "¿Cuánto es 6 × 100?", "opciones": ["600", "60", "106"], "correcta": 0,
  "voz": ["Ahora vos: 6 por 100.", "Pensá: ¿cuántos ceros van?", "¡*600*! Dos ceros."]},
 {"t": "errores", "items": [{"mal": "6 × 100 = 60", "bien": "6 × 100 = 600"}],
  "voz": ["Ojo con este error.", "Por 100 van *dos ceros*: 600."]},
 {"t": "resumen", "items": [["CAJA", "tiene 100"], ["POR 100", "dos 0 al final"], ["3 × 100", "es 300"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una caja tiene *100*.", "Por 100, *dos ceros* al final.", "3 por 100 es *300*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿24 × 10 es 2410?"}, {"yo": True, "txt": "¡No! Mirá las cifras"}, {"yo": False, "txt": "¿Se corren?"}], "titulo": "LAS CIFRAS", "sub": "se corren",
  "voz": ["Tomi pregunta: ¿24 por 10 es 2410?", "Rosa le dice: ¡no! Mirá las cifras.", "¿Las cifras se *corren*?", "Hoy: *qué pasa con las cifras*."]},
 {"t": "tabla", "titulo": "24 POR 10", "columnas": ["C", "D", "U"], "filas": [["", "2", "4"], ["2", "4", "0"]],
  "voz": ["Mirá el 24 en la tabla.", "Tiene 2 decenas y 4 unidades.", "Por 10, cada cifra se corre *un lugar*. ¡240!"]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "🔢", "texto": "3 unidades"}, "despues": {"cab": "DESPUÉS", "emoji": "🚀", "texto": "3 × 100 = 300"},
  "voz": ["*Antes*: el 3 estaba en las unidades.", "*Después* de por 100, ¡está en las centenas: *300*!"]},
 {"t": "prediccion", "pregunta": "¿Cuánto da 35 × 10?", "a": {"txt": "3510", "emoji": "😱"}, "b": {"txt": "350", "emoji": "😎"}, "correcta": "b", "resultado": "¡350! Se corren un lugar",
  "voz": ["¿Qué creés? ¿Cuánto da 35 por 10?", "¿3510 o 350? Pensá…", "¡*350*! Las cifras se corren un lugar."]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["1", "10", "100"], "falta": "1.000", "regla": "Por 10 cada vez",
  "voz": ["Mirá: 1, 10, 100…", "Cada vez, por 10. ¿Qué sigue?", "¡El *mil*! Otro cero más."]},
 {"t": "errores", "items": [{"mal": "24 × 10 = 2410", "bien": "24 × 10 = 240"}],
  "voz": ["Ojo con este error.", "Se agrega *un cero*, no un 10: 240."]},
 {"t": "resumen", "items": [["POR 10", "se corren un lugar"], ["POR 100", "se corren dos lugares"], ["ATRÁS", "van los ceros"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Por 10, las cifras se corren *un lugar*.", "Por 100, se corren *dos lugares*.", "Atrás van los *ceros*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Llega un pedido gigante!", "bajada": "Paquetes de 10 y cajas de 100", "emoji": "🚚", "titulo": "PROBLEMAS", "sub": "con 10 y 100",
  "voz": ["¡Último momento: llega un pedido gigante!", "Hay paquetes de 10 y cajas de 100.", "Hoy: *problemas con 10 y 100*."]},
 {"t": "pistas", "problema": "Rosa tiene 8 paquetes de 10. ¿Cuántos alfajores tiene?", "pistas": ["Cada paquete tiene 10", "Son 8 veces 10", "8 × 10"], "respuesta": "80 alfajores",
  "voz": ["Primer problema: 8 paquetes de 10.", "Pista uno: cada paquete tiene *10*.", "Pista dos: son *8 veces* 10.", "Pista tres: 8 por 10.", "¡*80* alfajores!"]},
 {"t": "calculadora", "titulo": "LA CALCULADORA DE ROSA", "teclas": ["5", "×", "1", "0", "0"], "resultado": "500", "texto": "5 CAJAS DE 100",
  "voz": ["Rosa controla con la *calculadora*.", "5 cajas de 100: 5 por 100.", "¡En la pantalla dice *500*!"]},
 {"t": "jefe", "jefe": {"nombre": "Pulpo de los Ceros", "emoji": "🐙"}, "preguntas": [{"p": "9 × 10", "r": "90"}, {"p": "3 × 100", "r": "300"}, {"p": "12 × 10", "r": "120"}],
  "voz": ["¡Apareció el *Pulpo de los Ceros*!", "Lo vencemos con por 10 y por 100.", "9 por 10: *90*.", "3 por 100: *300*.", "¡12 por 10: *120*! ¡Ganamos!"]},
 {"t": "errores", "items": [{"mal": "5 paquetes de 10 = 15", "bien": "5 × 10 = 50"}],
  "voz": ["Ojo con este error.", "No se suma: 5 por 10 es *50*."]},
 {"t": "resumen", "items": [["PAQUETES", "por 10"], ["CAJAS", "por 100"], ["RESPONDER", "con palabras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Paquetes de 10: multiplicamos *por 10*.", "Cajas de 100: *por 100*.", "Respondemos *con palabras*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m15-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 15 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
