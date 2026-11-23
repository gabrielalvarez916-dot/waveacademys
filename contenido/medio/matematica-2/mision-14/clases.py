# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 14 · Organizaciones rectangulares: las 4 clases animadas.
Metáfora de toda la misión: la fábrica de alfajores de la abuela Rosa (alfajores ordenados en filas en las bandejas grandes).
Usa la plantilla nueva «arreglo» (filas y columnas). Regla de primeros años.
Genera tools/medio/clase/lecciones/medio-mat2-m14-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '454a78bf-d8c7-4b6a-a466-4421fabe00d4', 2: '552a12f8-2edb-4bb7-8600-5398c1fb4b97', 3: 'c8ac471f-55c5-4000-bf3e-dcc35c231470', 4: '609eda3c-d2f3-4c9e-a9e9-56d232615d3e'}
TIT = {1: 'Contar filas y columnas', 2: 'Arreglos rectangulares', 3: 'Multiplicar para contar', 4: 'Problemas con filas y columnas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Rosa", "emoji": "👵"}

N1 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🏭", "lineas": ["Rosa tiene una bandeja grande.", "Ordena los alfajores.", "¡En filas y columnas!"], "titulo": "FILAS", "sub": "y columnas",
  "voz": ["Rosa tiene una *bandeja grande*.", "Ordena los alfajores con cuidado.", "¡Los pone en filas y columnas!", "Hoy: *contar filas y columnas*."]},
 {"t": "comparar", "a": {"cab": "FILA", "texto": "acostada ➡️", "emoji": "🍫"}, "b": {"cab": "COLUMNA", "texto": "parada ⬇️", "emoji": "🍫"}, "signo": "y",
  "voz": ["La *fila* va acostada: de lado a lado.", "La *columna* va parada: de arriba abajo.", "¡Fila acostada, columna parada!"]},
 {"t": "pizarra", "titulo": "LA BANDEJA DE ROSA", "lineas": [{"txt": "🍫 🍫 🍫 🍫  fila 1"}, {"txt": "🍫 🍫 🍫 🍫  fila 2"}, {"txt": "🍫 🍫 🍫 🍫  fila 3", "color": "sol", "marca": "subraya"}],
  "voz": ["Rosa pone la primera fila: 4 alfajores.", "La segunda fila: 4 más.", "¡La tercera! *3 filas* y *4 columnas*."]},
 {"t": "quiz4", "pregunta": "¿Cómo va la columna?", "opciones": ["Parada", "Acostada"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Cómo va la *columna*?", "¡*Parada*! De arriba abajo."]},
 {"t": "errores", "items": [{"mal": "Contar columnas como filas", "bien": "Fila acostada, columna parada"}],
  "voz": ["Ojo con este error.", "No confundas: fila *acostada*, columna *parada*."]},
 {"t": "resumen", "items": [["FILA", "de lado a lado"], ["COLUMNA", "de arriba abajo"], ["CONTAR", "las dos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *fila* va de lado a lado.", "La *columna* va de arriba abajo.", "Contamos *las dos*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Abu, ¿cómo ordeno 12 alfajores?"}, {"yo": True, "txt": "¡En filas iguales!"}, {"yo": False, "txt": "¿Cómo?"}], "titulo": "ARREGLOS", "sub": "rectangulares",
  "voz": ["Tomi le escribe a Rosa.", "¿Cómo ordeno 12 alfajores?", "Rosa le dice: ¡en *filas iguales*!", "Hoy: *arreglos rectangulares*."]},
 {"t": "arreglo", "emoji": "🍪", "filas": 3, "cols": 5, "texto": "3 filas de 5 = 15", "titulo": "UN ARREGLO",
  "voz": ["Un *arreglo* tiene filas iguales.", "Contamos de fila en fila: 5, 10, 15.", "¡3 filas de 5 son *15*!"]},
 {"t": "versus", "titulo": "¿ES UN ARREGLO?", "a": {"txt": "2 filas de 6", "emoji": "✅", "datos": ["filas iguales"]}, "b": {"txt": "una de 6 y otra de 4", "emoji": "❌", "datos": ["filas distintas"]}, "gana": "a", "veredicto": "¡Las filas tienen que ser iguales!",
  "voz": ["¿Cuál es un arreglo?", "Dos filas de 6: *iguales*.", "Una de 6 y otra de 4: *distintas*.", "¡Gana el de filas iguales!"]},
 {"t": "memoria", "titulo": "FORMAS DE ORDENAR 12", "items": ["2 filas de 6", "3 filas de 4", "4 filas de 3", "6 filas de 2"], "falta": 1,
  "voz": ["12 alfajores se ordenan de muchas formas.", "Se tapan… ¡y una desapareció!", "¡Faltaba *3 filas de 4*!"]},
 {"t": "pregunta", "pregunta": "4 filas de 5 pelotas. ¿Cuántas son?", "opciones": ["20", "9", "45"], "correcta": 0,
  "voz": ["Ahora vos: 4 filas de 5.", "Contá: 5, 10, 15…", "¡*20*!"]},
 {"t": "resumen", "items": [["ARREGLO", "filas iguales"], ["FORMA", "un rectángulo"], ["CONTAR", "de fila en fila"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *arreglo* tiene filas iguales.", "Forma un *rectángulo*.", "Contamos *de fila en fila*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Cuántos alfajores hay en 3 filas de 4? ¡Sin contar de a uno!", "segundos": 6, "respuesta": "¡12!", "emoji": "⚡", "titulo": "MULTIPLICAR", "sub": "para contar",
  "voz": ["Desafío: 3 filas de 4, sin contar de a uno.", "¡*12*! 3 por 4.", "Hoy: *multiplicar para contar*."]},
 {"t": "arreglo", "emoji": "🍫", "filas": 3, "cols": 4, "texto": "3 × 4 = 12", "titulo": "FILAS × COLUMNAS",
  "voz": ["Mirá la bandeja: 3 filas de 4.", "4, 8, 12.", "¡3 por 4 es *12*!"]},
 {"t": "prediccion", "pregunta": "Si giro la bandeja, ¿cambia el total?", "a": {"txt": "Sí, cambia", "emoji": "😱"}, "b": {"txt": "No, da igual", "emoji": "😎"}, "correcta": "b", "resultado": "4 × 3 = 12. ¡Da lo mismo!",
  "voz": ["¿Qué creés? Si giro la bandeja…", "¿Cambia la cantidad de alfajores?", "¡*No*! 4 por 3 también es *12*."], "sticker": {"txt": "🔄", "paso": 2}},
 {"t": "arreglo", "emoji": "🍫", "filas": 4, "cols": 3, "texto": "4 × 3 = 12", "titulo": "GIRADA",
  "voz": ["Ahora quedan 4 filas de 3.", "3, 6, 9, 12.", "¡También son *12*!"]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "2 filas de 5", "r": "10"}, {"p": "3 filas de 10", "r": "30"}, {"p": "5 filas de 2", "r": "10"}],
  "voz": ["¡Ronda rápida de arreglos!", "2 filas de 5: *10*.", "3 filas de 10: *30*.", "5 filas de 2: *10*."]},
 {"t": "resumen", "items": [["FILAS × COLUMNAS", "da el total"], ["RÁPIDO", "no contamos de a uno"], ["GIRAR", "da lo mismo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Multiplicamos *filas por columnas*.", "Es *más rápido* que contar de a uno.", "Si giramos el arreglo, *da lo mismo*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Acto en la escuela!", "bajada": "Hay que poner las sillas", "emoji": "🪑", "titulo": "PROBLEMAS", "sub": "con filas y columnas",
  "voz": ["¡Último momento: hay acto en la escuela!", "Ponen las sillas en filas.", "Hoy: *problemas con filas y columnas*."]},
 {"t": "historieta", "titulo": "LAS SILLAS DEL ACTO", "vinetas": [{"emojis": ["🪑", "🪑"], "txt": "4 filas de 10 sillas", "quien": "Tomi"}, {"emojis": ["🤔"], "txt": "¿Cuántas sillas?", "quien": "Tomi"}, {"emojis": ["👵", "✖️"], "txt": "4 × 10 = 40", "quien": "Rosa"}],
  "voz": ["Tomi ve 4 filas de 10 sillas.", "¿Cuántas sillas hay?", "Rosa multiplica: 4 por 10, ¡*40*!"]},
 {"t": "arreglo", "emoji": "🥚", "filas": 2, "cols": 6, "texto": "2 × 6 = 12 huevos", "titulo": "LA CAJA DE HUEVOS",
  "voz": ["Una caja de huevos: 2 filas de 6.", "6, 12.", "¡2 por 6 es *12* huevos!"]},
 {"t": "pistas", "problema": "Una barra de chocolate tiene 3 filas de 5 cuadraditos. ¿Cuántos tiene?", "pistas": ["Hay 3 filas", "Cada fila tiene 5", "3 × 5"], "respuesta": "15 cuadraditos",
  "voz": ["Ahora vos: una barra de chocolate.", "Pista uno: hay *3 filas*.", "Pista dos: cada fila tiene *5*.", "Pista tres: 3 por 5.", "¡*15* cuadraditos!"]},
 {"t": "jefe", "jefe": {"nombre": "Rey Rectángulo", "emoji": "🤴"}, "preguntas": [{"p": "5 filas de 4 baldosas", "r": "20"}, {"p": "2 filas de 10 libros", "r": "20"}],
  "voz": ["¡Llegó el *Rey Rectángulo*!", "Resolvemos sus problemas.", "5 filas de 4 baldosas: *20*.", "¡2 filas de 10 libros: *20*! ¡Ganamos!"]},
 {"t": "resumen", "items": [["BUSCAR", "filas y columnas"], ["MULTIPLICAR", "filas × columnas"], ["RESPONDER", "con palabras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Buscamos las *filas y columnas*.", "*Multiplicamos* filas por columnas.", "Respondemos *con palabras*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat2-m14-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 2", "titulo": TIT[n], "sub": f"Matemática 2 · Misión 14 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
