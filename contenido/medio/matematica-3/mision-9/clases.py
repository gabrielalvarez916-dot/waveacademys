# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 9 · Multiplicación y series proporcionales: las 4 clases animadas.
Metáfora de toda la misión: la panadería de Doña Rosa (bandejas, cajas y bolsas con la misma cantidad).
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'f29409f4-ff3f-4ada-b92e-8facd74e7f27', 2: 'ca9e85c8-a9d5-4205-bcde-5995c1d9d455', 3: 'b2009a77-9ccd-46be-aeb0-75ac68bc61c8', 4: '6f8409ed-74a0-4b26-9362-d2ad25f2745c'}
TIT = {1: 'Grupos iguales', 2: 'Series proporcionales', 3: 'Tablas de una cantidad que se repite', 4: 'Problemas de series'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
ROSA = {"nombre": "Doña Rosa", "emoji": "👵"}

N1 = [
 {"t": "gancho", "emoji": "🍪", "final": "🤔", "titulo": "GRUPOS", "sub": "iguales",
  "voz": ["Doña Rosa pone *4 galletas* en cada bandeja.", "Tiene *5 bandejas*. ¿Cuántas galletas hay?", "Hoy: *grupos iguales*."]},
 {"t": "grupos", "emoji": "🍪", "grupos": 5, "cada": 4, "texto": "5 × 4 = 20", "titulo": "5 BANDEJAS DE 4",
  "voz": ["Mirá las bandejas: todas tienen *4*.", "Contamos de 4 en 4: 4, 8, 12, 16, 20.", "¡5 veces 4 es *20*!"]},
 {"t": "definicion", "palabra": "Multiplicar", "texto": "Juntar grupos iguales: 5 grupos de 4 es 5 × 4.", "emoji": "✖️",
  "voz": ["*Multiplicar* es juntar grupos *iguales*.", "5 grupos de 4 se escribe *5 por 4*."]},
 {"t": "arreglo", "emoji": "🥖", "filas": 3, "cols": 6, "texto": "3 × 6 = 18", "titulo": "FILAS IGUALES",
  "voz": ["Ahora los panes están en *filas*.", "3 filas de 6: 6, 12, 18.", "¡3 por 6 es *18*!"]},
 {"t": "errores", "items": [{"mal": "Multiplicar grupos que no son iguales", "bien": "Solo con grupos iguales"}],
  "voz": ["Ojo con este error.", "Solo multiplicamos si los grupos son *iguales*."]},
 {"t": "resumen", "items": [["GRUPOS", "todos iguales"], ["×", "veces"], ["5 × 4", "5 grupos de 4"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los grupos tienen que ser *iguales*.", "El signo *por* quiere decir veces.", "5 por 4 son 5 grupos de 4.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "1 caja: 6 pastelitos. 2 cajas: 12. ¿Y 3 cajas?", "segundos": 8, "respuesta": "¡18!", "emoji": "📦", "titulo": "SERIES", "sub": "proporcionales",
  "voz": ["Desafío: una caja trae 6, dos cajas traen 12.", "¿Y tres cajas? ¡*18*!", "Hoy: *series proporcionales*."]},
 {"t": "saltos", "titulo": "DE 6 EN 6", "min": 0, "max": 30, "cada": 6, "inicio": 0, "saltos": [{"a": 6, "txt": "1 caja"}, {"a": 12, "txt": "2 cajas"}, {"a": 18, "txt": "3 cajas"}],
  "voz": ["Empezamos en el 0: sin cajas no hay nada.", "Una caja: *6*.", "Dos cajas: *12*.", "¡Tres cajas: *18*!"]},
 {"t": "patron", "titulo": "¿QUÉ SIGUE?", "items": ["6", "12", "18", "24"], "falta": "30", "regla": "Sumamos 6",
  "voz": ["Mirá la serie: 6, 12, 18, 24…", "¿Qué número sigue en la serie?", "¡*30*! Cada caja suma 6 más."]},
 {"t": "definicion", "palabra": "Serie proporcional", "texto": "Cada vez se suma la misma cantidad.", "emoji": "📈",
  "voz": ["En una *serie proporcional* siempre sumamos lo mismo.", "Si hay 0 cajas, hay *0* pastelitos."]},
 {"t": "errores", "items": [{"mal": "6, 12, 18, 20", "bien": "6, 12, 18, 24"}],
  "voz": ["Ojo con este error.", "Siempre se suma *6*: después del 18, el 24."]},
 {"t": "resumen", "items": [["SERIE", "suma siempre igual"], ["1 CAJA", "6"], ["3 CAJAS", "18"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la serie sumamos *siempre lo mismo*, cada vez.", "Una caja tiene *6*.", "Tres cajas tienen *18*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Doña Rosa", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "Cada bolsa lleva 5 panes"}, {"yo": True, "txt": "¿Y si vendo 8 bolsas?"}, {"yo": False, "txt": "¡Armemos una tabla!"}], "titulo": "TABLAS", "sub": "de una cantidad",
  "voz": ["Doña Rosa avisa: cada bolsa lleva *5 panes*.", "¿Y si vende *8 bolsas*?", "¡Armemos una tabla!", "Hoy: *tablas de una cantidad que se repite*."]},
 {"t": "tabla", "titulo": "BOLSAS Y PANES", "columnas": ["BOLSAS", "1", "2", "4", "8"], "filas": [["PANES", "5", "10", "20", "40"]],
  "voz": ["En la tabla, cada bolsa suma 5 panes.", "Uno, 5. Dos, *10*. Cuatro, *20*. Ocho, *40*."]},
 {"t": "versus", "a": {"txt": "4 bolsas", "emoji": "🛍️", "datos": ["20 panes"]}, "b": {"txt": "8 bolsas", "emoji": "🛍️", "datos": ["40 panes"]}, "gana": "b", "veredicto": "El doble de bolsas, el doble de panes",
  "voz": ["Comparamos 4 bolsas y 8 bolsas.", "4 bolsas tienen 20 panes.", "8 bolsas son el *doble*.", "¡El doble de bolsas tiene el *doble* de panes: 40!"]},
 {"t": "quiz4", "pregunta": "Si 3 bolsas tienen 15, ¿cuánto tienen 6?", "opciones": ["30", "18", "21"], "correcta": 0,
  "voz": ["Ahora vos: 3 bolsas tienen 15.", "6 bolsas son el doble…", "¡*30* panes!"]},
 {"t": "errores", "items": [{"mal": "El doble de bolsas tiene 5 panes más", "bien": "Tiene el doble de panes"}],
  "voz": ["Ojo con este error.", "Si se duplican las bolsas, se *duplican* los panes."]},
 {"t": "resumen", "items": [["TABLA", "ordena la serie"], ["DOBLE", "doble y doble"], ["SIN CONTAR", "de a uno"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *tabla* ordena la serie.", "Doble de bolsas, *doble* de panes.", "Así no contamos *de a uno*.", CIERRE]},
]
N4 = [
 {"t": "historia", "personaje": ROSA, "lugar": "🥖", "lineas": ["Un vecino pide 7 cajas de 8 galletas.", "Doña Rosa no quiere contar de a una.", "¿Cuántas galletas son?"], "titulo": "PROBLEMAS", "sub": "de series",
  "voz": ["Un vecino pide *7 cajas* de 8 galletas.", "Doña Rosa no quiere contar de a una.", "¿Cuántas galletas son?", "Hoy: *problemas de series*."]},
 {"t": "tabla", "titulo": "CAJAS Y GALLETAS", "columnas": ["CAJAS", "1", "2", "3", "4", "5", "6", "7"], "filas": [["GALLETAS", "8", "16", "24", "32", "40", "48", "56"]],
  "voz": ["Armamos la tabla: cada caja suma 8.", "8, 16, 24, 32, 40, 48, ¡*56*!"]},
 {"t": "transforma", "titulo": "MÁS CORTO", "pasos": [{"txt": "8 + 8 + 8 + 8 + 8 + 8 + 8"}, {"txt": "7 VECES 8", "nota": "grupos iguales"}, {"txt": "7 × 8 = 56"}],
  "voz": ["Sumar 8 siete veces es largo.", "Son 7 grupos de 8.", "¡7 por 8 es *56*!"]},
 {"t": "pistas", "problema": "Cada bandeja tiene 9 panes. ¿Cuántos hay en 4 bandejas?", "pistas": ["Son 4 grupos de 9", "9, 18, 27, 36"], "respuesta": "36",
  "voz": ["Cada bandeja tiene 9. ¿Cuántos en 4 bandejas?", "Pista: son *4 grupos de 9*.", "Pista: contamos 9, 18, 27, 36.", "¡Hay *36* panes!"]},
 {"t": "errores", "items": [{"mal": "7 cajas de 8: 7 + 8 = 15", "bien": "7 × 8 = 56"}],
  "voz": ["Ojo con este error.", "No se suman las cajas y las galletas: se *multiplica*."]},
 {"t": "resumen", "items": [["TABLA", "o multiplicar"], ["GRUPOS", "por cantidad"], ["RESPONDER", "con una oración"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Usamos una *tabla* o *multiplicamos*.", "Grupos *por* lo que tiene cada uno.", "Y respondemos *con una oración*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m9-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 9 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
