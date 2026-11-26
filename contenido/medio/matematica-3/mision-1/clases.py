# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 1 · Los números hasta 10.000: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de lápices de Lola (cajas de 10, cajones de 100 y camiones de 1.000).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '22ca20aa-6616-43b5-93f7-4c8eabf95aa1', 2: 'ce6f573d-0b3a-4f94-82e5-e4655151ad47', 3: 'ab4179aa-e4b8-4077-bad5-93e1217b5635', 4: 'd8230580-45e6-4f78-9910-9fe15ca13d98'}
TIT = {1: 'Los miles', 2: 'Hasta 5.000', 3: 'Hasta 10.000', 4: 'Leer y escribir números de cuatro cifras'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LOLA = {"nombre": "Lola", "emoji": "👩‍🔧"}

N1 = [
 {"t": "historia", "personaje": LOLA, "lugar": "🏭", "lineas": ["Lola llena cajones de 100.", "Diez cajones van al camión.", "¿Cuántos lápices lleva?"], "titulo": "LOS MILES", "sub": "1.000",
  "voz": ["Lola llena *cajones* de 100 lápices.", "Diez cajones suben al *camión*.", "¿Cuántos lápices lleva el camión?", "Hoy: *los miles*."]},
 {"t": "agrupar", "niveles": [{"nombre": "1 CAJÓN", "valor": "100", "icono": "caja"}, {"nombre": "10 CAJONES", "valor": "1.000", "icono": "camion"}], "salto": "×10",
  "voz": ["Un cajón tiene *100* lápices.", "Contamos: cien, doscientos, trescientos…", "Diez cajones son *1.000*.", "¡Mil es un camión lleno!"]},
 {"t": "definicion", "palabra": "Mil", "texto": "Diez cientos forman mil: 1.000", "emoji": "🚚",
  "voz": ["Diez cientos forman *mil*.", "Se escribe 1, punto, tres ceros."]},
 {"t": "escala", "titulo": "CAMIONES", "items": [{"txt": "1.000", "emoji": "🚚", "valor": 1000}, {"txt": "2.000", "emoji": "🚚", "valor": 2000}, {"txt": "3.000", "emoji": "🚚", "valor": 3000}],
  "voz": ["Un camión: *mil*.", "Dos camiones: *dos mil*.", "¡Tres camiones: *tres mil*!"]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["1.000", "2.000", "3.000", "4.000"], "falta": "5.000", "regla": "Sumamos mil",
  "voz": ["Mirá: mil, dos mil, tres mil, cuatro mil…", "¿Qué sigue?", "¡*Cinco mil*! Un camión más."]},
 {"t": "quiz4", "pregunta": "¿Cuántos cajones de 100 hay en 1.000?", "opciones": ["10", "100", "1"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuántos cajones forman mil?", "Pensá en el camión…", "¡*10* cajones!"]},
 {"t": "resumen", "items": [["MIL", "diez cientos"], ["1.000", "un camión"], ["DE MIL EN MIL", "2.000, 3.000"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Mil* son diez cientos.", "Un camión lleva *1.000* lápices.", "Contamos *de mil en mil*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "2 camiones, 3 cajones y 5 lápices. ¿Cuántos son?", "segundos": 8, "respuesta": "¡2.305!", "emoji": "🚚", "titulo": "HASTA", "sub": "5.000",
  "voz": ["Desafío: 2 camiones, 3 cajones y 5 lápices.", "¡*2.305*! Dos mil trescientos cinco.", "Hoy: *los números hasta 5.000*."]},
 {"t": "tabla", "titulo": "2.305", "columnas": ["M", "C", "D", "U"], "filas": [["2", "3", "0", "5"]],
  "voz": ["Mirá el 2.305 en la tabla.", "Tiene 2 miles y 3 cientos.", "Tiene 0 dieces y 5 unidades.", "El *cero* guarda el lugar de las decenas."]},
 {"t": "versus", "a": {"txt": "3.400", "emoji": "🚚", "datos": ["3 camiones", "4 cajones"]}, "b": {"txt": "4.300", "emoji": "🚚", "datos": ["4 camiones", "3 cajones"]}, "gana": "b", "veredicto": "4.300 es mayor: tiene más miles",
  "voz": ["¿Cuál es más grande?", "3.400 tiene 3 miles.", "4.300 tiene *4 miles*.", "¡Gana *4.300*: mirá primero los miles!"]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["4.997", "4.998", "4.999"], "falta": "5.000", "regla": "Sumamos 1",
  "voz": ["Mirá: 4.997, 4.998, 4.999…", "¿Qué número sigue?", "¡*Cinco mil*! Se llena otro camión."]},
 {"t": "errores", "items": [{"mal": "Después del 4.999 va el 41.000", "bien": "Después del 4.999 va el 5.000"}],
  "voz": ["Ojo con este error.", "Después del 4.999 viene el *5.000*."]},
 {"t": "resumen", "items": [["MILES", "van primero"], ["EL CERO", "guarda el lugar"], ["4.999", "y después 5.000"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *miles* van primero.", "El *cero* guarda el lugar.", "Después del 4.999 viene el *5.000*.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡La fábrica llegó a 10.000 lápices!", "bajada": "Diez camiones llenos", "emoji": "🎉", "titulo": "HASTA", "sub": "10.000",
  "voz": ["¡Último momento: la fábrica llegó a *10.000* lápices!", "Son diez camiones llenos.", "Hoy: *los números hasta 10.000*."]},
 {"t": "agrupar", "niveles": [{"nombre": "1 CAMIÓN", "valor": "1.000", "icono": "camion"}, {"nombre": "10 CAMIONES", "valor": "10.000", "icono": "🏭"}], "salto": "×10",
  "voz": ["Un camión lleva *1.000*.", "Contamos camiones: mil, dos mil, tres mil…", "Seguimos hasta llegar a nueve mil.", "Diez camiones son *10.000*.", "¡Diez mil! Un número de *cinco cifras*."]},
 {"t": "memoria", "titulo": "DE MIL EN MIL", "items": ["6.000", "7.000", "8.000", "9.000", "10.000"], "falta": 2,
  "voz": ["Mirá: 6.000, 7.000, 8.000, 9.000, 10.000.", "Se tapan… ¡y uno desapareció!", "¡Faltaba el *8.000*!"]},
 {"t": "prediccion", "pregunta": "¿Qué viene después del 9.999?", "a": {"txt": "10.000", "emoji": "😎"}, "b": {"txt": "9.1000", "emoji": "😱"}, "correcta": "a", "resultado": "¡10.000! Diez mil",
  "voz": ["¿Qué creés? Después del 9.999…", "¿10.000 o 9.1000? Pensá…", "¡*Diez mil*!"]},
 {"t": "errores", "items": [{"mal": "10.000 tiene 4 cifras", "bien": "10.000 tiene 5 cifras"}],
  "voz": ["Ojo con este error.", "Diez mil tiene *cinco cifras*.", "Es un 1 y cuatro ceros."]},
 {"t": "resumen", "items": [["10 CAMIONES", "10.000"], ["DE MIL EN MIL", "hasta 10.000"], ["9.999", "y después 10.000"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Diez camiones son *10.000*.", "Contamos *de mil en mil*.", "Después del 9.999 viene el *10.000*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Lola, ¿cómo escribo tres mil cuarenta?"}, {"yo": True, "txt": "Fijate dónde van los ceros"}, {"yo": False, "txt": "¿3.040?"}], "titulo": "LEER Y ESCRIBIR", "sub": "cuatro cifras",
  "voz": ["Tomi pregunta: ¿cómo escribo tres mil cuarenta?", "Lola le dice: fijate dónde van los *ceros*.", "¿3.040?", "Hoy: *leer y escribir números de cuatro cifras*."]},
 {"t": "transforma", "titulo": "ESCRIBIR", "pasos": [{"txt": "TRES MIL CUARENTA"}, {"txt": "3 MILES · 0 CIENTOS · 4 DIECES · 0", "nota": "cada lugar"}, {"txt": "3.040"}],
  "voz": ["Queremos escribir tres mil cuarenta.", "Tres miles, *cero* cientos, cuatro dieces y cero unidades.", "¡Se escribe *3.040*!"]},
 {"t": "unir", "titulo": "UNÍ", "pares": [["2.015", "dos mil quince"], ["2.150", "dos mil ciento cincuenta"], ["2.501", "dos mil quinientos uno"]],
  "voz": ["Uní cada número con su nombre.", "2.015: *dos mil quince*.", "2.150: *dos mil ciento cincuenta*.", "2.501: *dos mil quinientos uno*."]},
 {"t": "vof", "afirmacion": "Seis mil ocho se escribe 6.8", "emoji": "🤔", "verdadero": False, "explicacion": "Se escribe 6.008",
  "voz": ["¿Verdadero o falso? Seis mil ocho es 6.8.", "Contá las cifras…", "¡*Falso*! Es *6.008*: los ceros guardan lugar."]},
 {"t": "errores", "items": [{"mal": "tres mil cinco = 30005", "bien": "tres mil cinco = 3.005"}],
  "voz": ["Ojo con este error.", "Tres mil cinco es *3.005*: cuatro cifras."]},
 {"t": "resumen", "items": [["CUATRO CIFRAS", "M, C, D y U"], ["EL CERO", "guarda el lugar"], ["LEER", "primero los miles"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Son *cuatro cifras*: miles, cientos, dieces y unidades.", "El *cero* guarda el lugar.", "Para leer, primero los *miles*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m1-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
