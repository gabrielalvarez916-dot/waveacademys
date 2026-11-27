# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 13 · Organizaciones rectangulares: las 4 clases animadas.
Metáfora de toda la misión: la feria de la escuela (sillas en filas, butacas del teatro, ropa y heladería de la feria).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m13-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'cd36d06d-e6e5-471a-82d5-3d1a0acb111d', 2: 'aa0d99e3-ecf2-485f-883f-47ef174c47dd', 3: '701fa710-2302-4635-811d-9fd0afb9190f', 4: '8e82756d-bc32-478c-9d0a-8f7124f7ea90'}
TIT = {1: 'Filas y columnas', 2: 'Arreglos grandes', 3: 'Combinar prendas y sabores', 4: 'Problemas de combinaciones'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "gancho", "emoji": "🪑", "final": "🤔", "titulo": "FILAS", "sub": "y columnas",
  "voz": ["Para la feria, ponen sillas en *filas* ordenadas.", "¿Cómo las contamos rápido, sin contar de a una?", "Hoy: *filas y columnas*."]},
 {"t": "arreglo", "emoji": "🪑", "filas": 3, "cols": 5, "texto": "3 × 5 = 15", "titulo": "3 FILAS DE 5",
  "voz": ["Hay 3 filas y en cada fila hay *5* sillas.", "Contamos de 5 en 5: 5, 10, 15.", "¡3 por 5 es *15* sillas!"]},
 {"t": "definicion", "palabra": "Organización rectangular", "texto": "Cosas en filas y columnas iguales: filas por columnas.", "emoji": "▦",
  "voz": ["Cuando las cosas forman un *rectángulo*, multiplicamos.", "Filas *por* columnas."]},
 {"t": "versus", "a": {"txt": "3 FILAS DE 5", "emoji": "🪑", "datos": ["15 sillas"]}, "b": {"txt": "5 FILAS DE 3", "emoji": "🪑", "datos": ["15 sillas"]}, "gana": "a", "veredicto": "¡Empate! Dan lo mismo",
  "voz": ["Comparamos: 3 filas de 5 y 5 filas de 3.", "3 por 5 es 15.", "5 por 3 es 15.", "¡Empate! Si giramos el rectángulo, da *lo mismo*."]},
 {"t": "errores", "items": [{"mal": "3 filas de 5: 3 + 5 = 8", "bien": "3 × 5 = 15"}],
  "voz": ["Ojo con este error.", "Filas y columnas se *multiplican*, no se suman."]},
 {"t": "resumen", "items": [["RECTÁNGULO", "filas y columnas"], ["MULTIPLICAR", "filas por columnas"], ["GIRAR", "da lo mismo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las cosas forman un *rectángulo*.", "Multiplicamos *filas por columnas*.", "Si lo giramos, da *lo mismo*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Sofi", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "El teatro tiene 12 filas de 8 butacas"}, {"yo": True, "txt": "¡Son un montón!"}, {"yo": False, "txt": "Partamos las filas"}], "titulo": "ARREGLOS", "sub": "grandes",
  "voz": ["Sofi escribe: el teatro tiene *12 filas* de 8 butacas.", "¡Son un montón para contar!", "Partamos las filas en dos grupos.", "Hoy: *arreglos grandes*."]},
 {"t": "grilla", "titulo": "EL TEATRO", "filas": 12, "cols": 8, "resaltar": [{"fila": 10, "col": 8, "txt": "80"}, {"fila": 12, "col": 8, "txt": "96"}],
  "voz": ["Las primeras 10 filas: 10 por 8, *80*.", "Con 2 filas más llegamos a la fila 12.", "¡En total hay *96* butacas!"]},
 {"t": "pizarra", "titulo": "12 × 8", "lineas": [{"txt": "10 × 8 = 80"}, {"txt": "2 × 8 = 16"}, {"txt": "80 + 16 = 96", "color": "verde", "marca": "subraya"}],
  "voz": ["Partimos el 12 en 10 y 2.", "10 por 8 es 80. 2 por 8 es *16*.", "¡80 más 16 es *96*!"]},
 {"t": "completa", "antes": "15 filas de 4: 10 × 4 + 5 × 4 =", "despues": "butacas", "opciones": ["60", "19", "54"], "correcta": 0,
  "voz": ["Completá: 15 filas de 4.", "40 más 20…", "¡*60* butacas!"]},
 {"t": "errores", "items": [{"mal": "12 × 8 = 10 × 8 = 80", "bien": "Faltan las otras 2 filas: 96"}],
  "voz": ["Ojo con este error.", "No te olvides de las filas que *sobran*."]},
 {"t": "resumen", "items": [["PARTIR", "en 10 y el resto"], ["MULTIPLICAR", "cada parte"], ["SUMAR", "todo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Partimos las filas en *10 y el resto*.", "Multiplicamos *cada parte*.", "Y *sumamos* todo al final.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Muestra de ropa en la feria!", "bajada": "3 camisetas y 2 pantalones", "emoji": "👕", "titulo": "COMBINAR", "sub": "prendas y sabores",
  "voz": ["¡Último momento: hay una *muestra de ropa* en la feria!", "Sofi tiene 3 camisetas y 2 pantalones.", "Hoy: *combinar prendas y sabores*."]},
 {"t": "tabla", "titulo": "CAMISETAS Y PANTALONES", "columnas": ["", "👖", "🩳"], "filas": [["🟥", "🟥👖", "🟥🩳"], ["🟦", "🟦👖", "🟦🩳"], ["🟩", "🟩👖", "🟩🩳"]],
  "voz": ["Armamos un cuadro: camisetas a un lado, pantalones arriba.", "La camiseta roja va con los *dos* pantalones.", "La azul también, y la verde también.", "¡Son *6* combinaciones!"]},
 {"t": "escala", "titulo": "MÁS PRENDAS, MÁS COMBINACIONES", "items": [{"txt": "2 × 2 = 4", "emoji": "👕", "valor": 4}, {"txt": "3 × 2 = 6", "emoji": "👕", "valor": 6}, {"txt": "3 × 3 = 9", "emoji": "👕", "valor": 9}],
  "voz": ["2 camisetas y 2 pantalones: *4*.", "3 camisetas y 2 pantalones: *6*.", "¡3 y 3: *9* combinaciones!"]},
 {"t": "quiz4", "pregunta": "4 sabores y 2 conos. ¿Cuántos helados?", "opciones": ["8", "6", "42"], "correcta": 0,
  "voz": ["Ahora vos: 4 sabores y 2 tipos de cono.", "Cada sabor va con cada cono…", "¡*8* helados distintos!"]},
 {"t": "errores", "items": [{"mal": "3 camisetas y 2 pantalones: 3 + 2 = 5", "bien": "3 × 2 = 6"}],
  "voz": ["Ojo con este error.", "Cada camiseta va con *cada* pantalón: multiplicamos."]},
 {"t": "resumen", "items": [["CUADRO", "una fila por cada uno"], ["CADA UNO", "con cada otro"], ["MULTIPLICAR", "las cantidades"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Armamos un *cuadro* para no perder ninguna.", "Cada uno va con *cada* uno del otro grupo.", "Y *multiplicamos* las cantidades.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🍦", "lineas": ["En la heladería hay 5 sabores.", "Y 3 tipos de cono.", "¿Cuántos helados distintos hay?"], "titulo": "PROBLEMAS", "sub": "de combinaciones",
  "voz": ["En la heladería de la feria hay *5 sabores*.", "Y hay *3* tipos de cono.", "¿Cuántos helados distintos se pueden armar?", "Hoy: *problemas de combinaciones*."]},
 {"t": "flujo", "titulo": "CÓMO LO PENSAMOS", "items": [{"txt": "Dos grupos", "emoji": "🍓"}, {"txt": "Cada uno con cada uno", "emoji": "🔗"}, {"txt": "5 × 3 = 15", "emoji": "✖️"}],
  "voz": ["Hay *dos grupos*: sabores y conos.", "Cada sabor va con *cada* cono.", "¡5 por 3: *15* helados!"]},
 {"t": "pistas", "problema": "4 tipos de pan y 3 rellenos. ¿Cuántos sándwiches distintos?", "pistas": ["Cada pan con cada relleno", "4 × 3"], "respuesta": "12",
  "voz": ["Otro: 4 panes y 3 rellenos. ¿Cuántos sándwiches?", "Pista: cada pan va con *cada* relleno.", "Pista: multiplicamos 4 por 3.", "¡Hay *12* sándwiches distintos!"]},
 {"t": "memoria", "titulo": "COMBINACIONES", "items": ["2 × 3 = 6", "3 × 3 = 9", "4 × 2 = 8", "5 × 3 = 15"], "falta": 1,
  "voz": ["Mirá estas combinaciones.", "Se tapan… ¿cuál desapareció?", "¡Faltaba 3 por 3, *9*!"]},
 {"t": "errores", "items": [{"mal": "5 sabores y 3 conos: 8 helados", "bien": "5 × 3 = 15 helados"}],
  "voz": ["Ojo con este error.", "Para combinar, *multiplicamos*: no sumamos."]},
 {"t": "resumen", "items": [["DOS GRUPOS", "a combinar"], ["MULTIPLICAR", "uno por otro"], ["RESPONDER", "con oración"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Buscamos los *dos grupos* que se combinan.", "*Multiplicamos* uno por el otro.", "Y respondemos *con una oración*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m13-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 13 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
