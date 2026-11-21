# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 3 · La serie numérica hasta 50: las 4 clases animadas.
Metáfora: el álbum de figuritas de Tomi. Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat1-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'c152a1aa-f6fb-4106-bbdb-e465ae5743f1', 2: '5b055fbf-1d1b-4fae-895d-766f32766886', 3: '8bd884bd-736e-400d-8a24-d37a4e20da79', 4: 'c70b6e5a-08a2-4048-bd93-02969b52dc6a'}
TIT = {1: 'Contar hasta 30', 2: 'Contar hasta 50', 3: 'El anterior y el siguiente', 4: 'Qué número falta'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "📒", "lineas": ["Tomi junta figuritas.", "Cada una tiene un número.", "¡Su álbum llega al 30!"], "titulo": "CONTAR", "sub": "hasta 30",
  "voz": ["Tomi junta *figuritas* en su álbum.", "Cada figurita tiene su número.", "¡Su álbum llega hasta el 30!", "Hoy: *contar hasta 30*."]},
 {"t": "cuadro", "desde": 0, "hasta": 30, "titulo": "EL ÁLBUM DE TOMI",
  "voz": ["Este es el álbum: del 0 al 30.", "20, 21, 22, 23, 24, 25, 26, 27, 28, 29.", "¡Los del veinte empiezan con *2*!"]},
 {"t": "consejo", "titulo": "DE A 10", "texto": "Cada fila tiene 10 números", "emoji": "📏",
  "voz": ["Truco: cada fila del álbum tiene *10* figuritas."]},
 {"t": "tren", "desde": 21, "hasta": 30, "titulo": "EL TREN DE FIGURITAS",
  "voz": ["Las figuritas viajan en tren. ¡Contemos!", "21, 22, 23, 24, 25, 26, 27, 28, 29, 30.", "¡Llegamos al *30*!"]},
 {"t": "pregunta", "pregunta": "¿Qué número viene después del 29?", "opciones": ["30", "20", "28"], "correcta": 0,
  "voz": ["Ahora vos. ¿Qué número viene después del 29?", "Pensá en el álbum de Tomi.", "¡El *30*! Treinta."]},
 {"t": "errores", "items": [{"mal": "Después del 29 decir 20", "bien": "Después del 29 viene el 30"}],
  "voz": ["Ojo con este error.", "Después del 29 viene el *30*, no el 20."]},
 {"t": "resumen", "items": [["HASTA 30", "en orden"], ["DE A 10", "una fila"], ["LOS VEINTE", "empiezan con 2"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos *hasta el 30*, en orden.", "Cada fila tiene *10* números.", "Los del veinte empiezan con *2*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué número viene después del 39?", "segundos": 5, "respuesta": "¡El 40!", "emoji": "📒", "titulo": "CONTAR", "sub": "hasta 50",
  "voz": ["Desafío: ¿qué número viene después del 39?", "¡El *40*! Cuarenta.", "Hoy: *contar hasta 50*."]},
 {"t": "cuadro", "desde": 0, "hasta": 50, "titulo": "EL ÁLBUM CRECIÓ",
  "voz": ["¡El álbum de Tomi ahora llega al 50!", "30, 31, 32, 33, 34, 35, 36, 37, 38, 39.", "¡Los del treinta empiezan con *3*!"]},
 {"t": "cuadro", "desde": 0, "hasta": 50, "titulo": "UN SECRETO DEL ÁLBUM",
  "voz": ["Mirá la columna del 5.", "5, 15, 25, 35, 45.", "¡Todos terminan en *5*!"]},
 {"t": "consejo", "titulo": "MIRÁ LAS FILAS", "texto": "En una fila, todos empiezan igual", "emoji": "👀",
  "voz": ["Truco: en cada fila, todos *empiezan igual*."]},
 {"t": "tren", "desde": 41, "hasta": 50, "titulo": "EL ÚLTIMO TRAMO",
  "voz": ["El último tramo del álbum. ¡Contemos!", "41, 42, 43, 44, 45, 46, 47, 48, 49, 50.", "¡Llegamos al *50*!"]},
 {"t": "pregunta", "pregunta": "¿Qué número viene después del 45?", "opciones": ["46", "44", "55"], "correcta": 0,
  "voz": ["Ahora vos. ¿Qué número viene después del 45?", "Pensá: 43, 44, 45…", "¡El *46*!"]},
 {"t": "resumen", "items": [["HASTA 50", "en orden"], ["FILAS", "empiezan igual"], ["COLUMNAS", "terminan igual"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Contamos *hasta el 50*.", "En una fila, todos *empiezan igual*.", "En una columna, todos *terminan igual*.", CIERRE]},
]
N3 = [
 {"t": "gancho", "emoji": "📒", "final": "↔️", "titulo": "EL ANTERIOR", "sub": "y el siguiente",
  "voz": ["Tomi pega la figurita 27.", "¿Qué figurita va antes? ¿Y cuál va después?", "Hoy: *el anterior y el siguiente*."]},
 {"t": "definicion", "palabra": "Anterior y siguiente", "texto": "El que va antes y el que va después", "emoji": "↔️",
  "voz": ["El *anterior* es el número que va antes.", "El *siguiente* es el número que va después."]},
 {"t": "recta", "min": 20, "max": 30, "paso": 1, "marcas": [{"v": 26, "txt": "anterior: 26"}, {"v": 27, "txt": "27"}, {"v": 28, "txt": "siguiente: 28"}],
  "voz": ["Mirá la recta del 20 al 30.", "El *26* va antes del 27: es el anterior.", "Esta es la figurita *27*.", "El *28* va después: es el siguiente."]},
 {"t": "cuadro", "desde": 0, "hasta": 40, "titulo": "LA FIGURITA 38",
  "voz": ["Busquemos la figurita 38 en el álbum.", "37, 38, 39.", "El 37 va antes y el 39, después."]},
 {"t": "pregunta", "pregunta": "¿Cuál es el anterior del 40?", "opciones": ["41", "39", "30"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cuál es el *anterior* del 40?", "Pensá: ¿qué número va antes?", "¡El *39*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es el siguiente del 19?", "opciones": ["20", "18", "10"], "correcta": 0,
  "voz": ["Otra más. ¿Cuál es el *siguiente* del 19?", "Pensá: ¿qué número va después?", "¡El *20*!"]},
 {"t": "errores", "items": [{"mal": "El siguiente del 29 es 210", "bien": "El siguiente del 29 es 30"}],
  "voz": ["Ojo con este error.", "El siguiente del 29 es el *30*."]},
 {"t": "resumen", "items": [["ANTERIOR", "va antes"], ["SIGUIENTE", "va después"], ["ÁLBUM", "del 0 al 50"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *anterior* va antes.", "El *siguiente* va después.", "Los buscamos en el álbum o en la recta.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": TOMI, "lugar": "📒", "lineas": ["¡A Tomi le faltan figuritas!", "Hay huecos en el álbum.", "¿Qué números faltan?"], "titulo": "¿QUÉ NÚMERO", "sub": "falta?",
  "voz": ["¡A Tomi le *faltan figuritas*!", "Hay lugares vacíos en su álbum.", "¿Qué números faltan? ¡Vamos a buscarlos!", "Hoy: *qué número falta*."]},
 {"t": "cuadro", "desde": 0, "hasta": 30, "faltan": [8, 17, 25], "titulo": "LOS HUECOS DEL ÁLBUM",
  "voz": ["Mirá el álbum de Tomi.", "Buscá los lugares vacíos.", "¡Faltan el *8*, el *17* y el *25*!"]},
 {"t": "tren", "desde": 42, "hasta": 49, "faltan": [44, 47], "titulo": "¿QUÉ VAGONES FALTAN?",
  "voz": ["En el tren también faltan figuritas.", "42, 43… ¿y? 45, 46… ¿y? 48, 49.", "¡Faltan el *44* y el *47*!"]},
 {"t": "consejo", "titulo": "CONTÁ DESDE ANTES", "texto": "Decí el anterior y seguí contando", "emoji": "🔍",
  "voz": ["Truco: decí el número de antes y *seguí contando*."]},
 {"t": "pregunta", "pregunta": "¿Qué número falta? 23, 24, ___, 26", "opciones": ["25", "27", "22"], "correcta": 0,
  "voz": ["Ahora vos. 23, 24… ¿y? 26.", "¿Qué número falta?", "¡El *25*!"]},
 {"t": "pregunta", "pregunta": "¿Qué número falta? 38, ___, 40", "opciones": ["39", "41", "30"], "correcta": 0,
  "voz": ["Otra más. 38… ¿y? 40.", "¿Qué número falta?", "¡El *39*!"]},
 {"t": "resumen", "items": [["BUSCAR", "el lugar vacío"], ["CONTAR", "desde el anterior"], ["COMPLETAR", "el que falta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Buscamos el *lugar vacío*.", "Contamos *desde el anterior*.", "Y completamos el número que *falta*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat1-m3-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 1", "titulo": TIT[n], "sub": f"Matemática 1 · Misión 3 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
