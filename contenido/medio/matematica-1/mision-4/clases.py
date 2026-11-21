# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 4 · Los números hasta 100: las 4 clases animadas.
Metáfora: el álbum nuevo de Tomi, de 100 figuritas. Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '8d29186b-ec68-4156-a8ff-bdebac145ec4', 2: 'a06eee1e-e762-45a6-83b9-12a56bc4a520', 3: 'c02423b4-20bc-4122-b688-df4c677de7aa', 4: '5b25d5d3-8159-43fe-b7d1-22521691bf69'}
TIT = {1: 'La serie hasta 100', 2: 'La tabla de cien', 3: 'Regularidades en la tabla', 4: 'Contar de a 2, 5 y 10'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "📒", "lineas": ["¡Tomi tiene un álbum nuevo!", "Tiene 100 figuritas.", "¿Sabés contar hasta 100?"], "titulo": "LA SERIE", "sub": "hasta 100",
  "voz": ["¡Tomi tiene un *álbum nuevo*!", "Este álbum tiene *100 figuritas*.", "¿Sabés contar hasta 100? ¡Vamos!", "Hoy: *la serie hasta 100*."]},
 {"t": "tren", "desde": 10, "hasta": 100, "paso": 10, "titulo": "LOS NÚMEROS REDONDOS",
  "voz": ["Primero, los números *redondos*.", "10, 20, 30, 40, 50, 60, 70, 80, 90, 100.", "¡Llegamos al *100*: cien!"]},
 {"t": "tren", "desde": 61, "hasta": 70, "titulo": "LOS DEL SESENTA",
  "voz": ["Ahora contamos los del sesenta.", "61, 62, 63, 64, 65, 66, 67, 68, 69, 70.", "Después del 69 viene el *70*."]},
 {"t": "consejo", "titulo": "DESPUÉS DEL 9", "texto": "Después de un 9 viene un redondo", "emoji": "🔁",
  "voz": ["Truco: después de un *9*, viene un número redondo."]},
 {"t": "tren", "desde": 91, "hasta": 100, "titulo": "EL ÚLTIMO TRAMO",
  "voz": ["¡El último tramo del álbum!", "91, 92, 93, 94, 95, 96, 97, 98, 99, 100.", "¡*Cien*! Completamos el álbum."]},
 {"t": "pregunta", "pregunta": "¿Qué número viene después del 79?", "opciones": ["80", "70", "710"], "correcta": 0,
  "voz": ["Ahora vos. ¿Qué número viene después del 79?", "Pensá: después de un 9…", "¡El *80*! Ochenta."]},
 {"t": "resumen", "items": [["HASTA 100", "en orden"], ["REDONDOS", "10, 20, 30…"], ["DESPUÉS DEL 9", "viene un redondo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos *hasta el 100*.", "Los *redondos*: 10, 20, 30…", "Después de un 9, viene un *redondo*.", CIERRE]},
]
N2 = [
 {"t": "gancho", "emoji": "🔢", "final": "💯", "titulo": "LA TABLA", "sub": "de cien",
  "voz": ["Tomi pegó todas sus figuritas.", "Quedó una tabla con *100 números*.", "Hoy: *la tabla de cien*."]},
 {"t": "cuadro", "hasta": 100, "titulo": "LA TABLA DE CIEN",
  "voz": ["Son diez filas de diez números.", "81, 82, 83, 84, 85, 86, 87, 88, 89, 90.", "Esta es la fila de los *ochenta*."]},
 {"t": "definicion", "palabra": "Fila y columna", "texto": "Fila: de costado. Columna: para abajo.", "emoji": "📐",
  "voz": ["Una *fila* va de costado.", "Una *columna* va para abajo."]},
 {"t": "cuadro", "hasta": 100, "titulo": "BUSCAMOS EL 57",
  "voz": ["Busquemos el 57 en la tabla.", "50… ¡57!", "El 57 está en la fila del *cincuenta*."]},
 {"t": "pregunta", "pregunta": "¿En qué fila está el 34?", "opciones": ["La del 30", "La del 40", "La del 20"], "correcta": 0,
  "voz": ["Ahora vos. Buscá el 34.", "¿En qué fila está?", "¡En la fila del *treinta*!"]},
 {"t": "consejo", "titulo": "BUSCÁ LA FILA", "texto": "La primera cifra te dice la fila", "emoji": "🔍",
  "voz": ["Truco: la *primera cifra* te dice la fila."]},
 {"t": "resumen", "items": [["TABLA", "100 números"], ["FILA", "de costado"], ["COLUMNA", "para abajo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La tabla tiene *100 números*.", "Una *fila* va de costado.", "Una *columna* va para abajo.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué tienen en común 7, 17, 27 y 37?", "segundos": 6, "respuesta": "¡Terminan en 7!", "emoji": "🔍", "titulo": "REGULARIDADES", "sub": "en la tabla",
  "voz": ["Desafío: ¿qué tienen en común 7, 17, 27 y 37?", "¡Todos terminan en *7*!", "Hoy: *regularidades en la tabla*."]},
 {"t": "cuadro", "hasta": 100, "titulo": "LA COLUMNA DEL 3",
  "voz": ["Mirá la columna del 3.", "3, 13, 23, 33, 43, 53, 63, 73, 83, 93.", "¡En una columna, todos *terminan igual*!"]},
 {"t": "cuadro", "hasta": 100, "titulo": "LA FILA DEL 40",
  "voz": ["Ahora mirá la fila del 40.", "41, 42, 43, 44, 45, 46, 47, 48, 49.", "¡En una fila, todos *empiezan igual*!"]},
 {"t": "cuadro", "hasta": 100, "faltan": [36, 64, 88], "titulo": "FIGURITAS PERDIDAS",
  "voz": ["Hay figuritas perdidas en la tabla.", "Usá los secretos de filas y columnas.", "¡Faltan el *36*, el *64* y el *88*!"]},
 {"t": "pregunta", "pregunta": "¿Qué número va debajo del 45?", "opciones": ["55", "46", "54"], "correcta": 0,
  "voz": ["Ahora vos. Mirá el 45.", "¿Qué número va justo *debajo*?", "¡El *55*! Abajo, suma 10."]},
 {"t": "consejo", "titulo": "ABAJO SUMA 10", "texto": "Bajar una fila es sumar 10", "emoji": "👇",
  "voz": ["Truco: bajar una fila es *sumar 10*."]},
 {"t": "resumen", "items": [["FILAS", "empiezan igual"], ["COLUMNAS", "terminan igual"], ["ABAJO", "suma 10"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En una fila, todos *empiezan igual*.", "En una columna, todos *terminan igual*.", "Bajar una fila es *sumar 10*.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🧦", "lineas": ["Tomi cuenta medias de a pares.", "De a 2 es más rápido.", "¿Y de a 5? ¿Y de a 10?"], "titulo": "CONTAR", "sub": "de a 2, 5 y 10",
  "voz": ["Tomi cuenta medias de *a pares*.", "¡De a 2 es más rápido!", "¿Y si cuenta de a 5? ¿Y de a 10?", "Hoy: *contar de a 2, 5 y 10*."]},
 {"t": "tren", "desde": 2, "hasta": 20, "paso": 2, "titulo": "DE A 2",
  "voz": ["Contamos de a 2.", "2, 4, 6, 8, 10, 12, 14, 16, 18, 20.", "¡Saltamos de a dos!"]},
 {"t": "tren", "desde": 5, "hasta": 50, "paso": 5, "titulo": "DE A 5",
  "voz": ["Ahora de a 5, como una mano.", "5, 10, 15, 20, 25, 30, 35, 40, 45, 50.", "¡Terminan en *5* o en *0*!"]},
 {"t": "tren", "desde": 10, "hasta": 100, "paso": 10, "titulo": "DE A 10",
  "voz": ["Y de a 10, ¡el más rápido!", "10, 20, 30, 40, 50, 60, 70, 80, 90, 100.", "¡Llegamos al *100*!"]},
 {"t": "pregunta", "pregunta": "2, 4, 6, 8… ¿qué sigue?", "opciones": ["9", "10", "12"], "correcta": 1,
  "voz": ["Ahora vos. Contamos de a 2.", "2, 4, 6, 8… ¿qué sigue?", "¡El *10*!"]},
 {"t": "pregunta", "pregunta": "5, 10, 15… ¿qué sigue?", "opciones": ["16", "20", "25"], "correcta": 1,
  "voz": ["Otra más. Contamos de a 5.", "5, 10, 15… ¿qué sigue?", "¡El *20*!"]},
 {"t": "resumen", "items": [["DE A 2", "2, 4, 6…"], ["DE A 5", "5, 10, 15…"], ["DE A 10", "10, 20, 30…"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*De a 2*: 2, 4, 6.", "*De a 5*: 5, 10, 15.", "*De a 10*: 10, 20, 30.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m4-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 4 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
