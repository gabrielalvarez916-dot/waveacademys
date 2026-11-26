# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 2 · Comparar y ordenar hasta 10.000: las 4 clases animadas.
Metáfora de toda la misión: los puntos del videojuego de Nico.
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '308a395e-64e9-4ab1-b030-61aba69453d3', 2: '764fc11c-ed8f-4647-93eb-382a2c707ef9', 3: '3444e1e9-57a1-4c81-af47-283064cca485', 4: '09b6d8e7-cbe8-46f7-b9e7-46fbab71cd87'}
TIT = {1: 'Mayor y menor hasta diez mil', 2: 'Ordenar números de cuatro cifras', 3: 'Anterior y siguiente de números grandes', 4: 'La recta numérica hasta 10.000'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
NICO = {"nombre": "Nico", "emoji": "🎮"}

N1 = [
 {"t": "gancho", "emoji": "🎮", "final": "🤔", "titulo": "MAYOR Y MENOR", "sub": "hasta 10.000",
  "voz": ["Nico juega a su videojuego.", "Hizo *4.735* puntos. Su hermana hizo *4.753*.", "¿Quién ganó? Hoy: *mayor y menor*."]},
 {"t": "estante", "numero": "4.735", "cab": ["MILES", "CENTENAS", "DECENAS", "UNIDADES"], "dig": ["4", "7", "3", "5"], "val": ["4.000", "700", "30", "5"], "destacar": 0, "etiqueta": "CADA CIFRA EN SU LUGAR",
  "voz": ["Mirá los puntos de Nico: *4.735*.", "Tiene cuatro lugares.", "Primero los *miles*: 4.", "Después las *centenas*: 7.", "Y al final, decenas y unidades."]},
 {"t": "balanza", "izq": {"cab": "NICO", "items": ["4.735"]}, "der": {"cab": "SU HERMANA", "items": ["4.753"]}, "gana": "der",
  "voz": ["Comparamos lugar por lugar.", "Miles: 4 y 4. Centenas: 7 y 7. ¡Empatan!", "Decenas: 3 y 5. ¡Gana *4.753*!"]},
 {"t": "definicion", "palabra": "Comparar", "texto": "Miramos primero los miles. Si empatan, las centenas.", "emoji": "🔍",
  "voz": ["Para comparar, miramos primero los *miles*.", "Si empatan, seguimos con las *centenas*."]},
 {"t": "quiz4", "pregunta": "¿Cuál es mayor?", "opciones": ["6.099", "6.190", "6.019"], "correcta": 1,
  "voz": ["Ahora vos: ¿cuál es mayor?", "Todos tienen 6 miles. Mirá las centenas…", "¡*6.190*! Tiene una centena."]},
 {"t": "errores", "items": [{"mal": "999 es mayor que 1.000", "bien": "1.000 es mayor que 999"}],
  "voz": ["Ojo con este error.", "Cuatro cifras le ganan a *tres cifras*."]},
 {"t": "resumen", "items": [["PRIMERO", "los miles"], ["SI EMPATAN", "las centenas"], ["MÁS CIFRAS", "más grande"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero miramos los *miles*.", "Si empatan, las *centenas*.", "Con más cifras, el número es *más grande*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": NICO, "lugar": "🏆", "lineas": ["Nico juega con tres amigos.", "Quiere armar la tabla de puntos.", "¿Quién va primero?"], "titulo": "ORDENAR", "sub": "cuatro cifras",
  "voz": ["Nico juega con *tres amigos*.", "Quiere armar la *tabla de puntos*.", "¿Quién va primero?", "Hoy: *ordenar números de cuatro cifras*."]},
 {"t": "ranking", "titulo": "TABLA DE PUNTOS", "items": [{"txt": "MÍA", "emoji": "🥇", "dato": "5.280"}, {"txt": "NICO", "emoji": "🥈", "dato": "5.208"}, {"txt": "LEO", "emoji": "🥉", "dato": "2.850"}],
  "voz": ["Armamos la tabla de mayor a menor.", "Tercero, *Leo*: 2.850. Tiene solo 2 miles.", "Segundo, *Nico*: 5.208.", "¡Y primera, *Mía*: 5.280! Le gana en las decenas."]},
 {"t": "orden", "titulo": "DE MENOR A MAYOR", "items": [{"txt": "2.850", "emoji": "🟢"}, {"txt": "5.208", "emoji": "🟡"}, {"txt": "5.280", "emoji": "🔴"}], "relato": [2, 0, 1],
  "voz": ["Ahora al revés: de *menor a mayor*.", "Primero el más chico: *2.850*.", "Después *5.208* y al final *5.280*."]},
 {"t": "quiz4", "pregunta": "De menor a mayor, ¿cuál va primero?", "opciones": ["3.402", "3.240", "3.420"], "correcta": 1,
  "voz": ["Probá vos: ¿cuál va *primero*?", "Todos tienen 3 miles. Mirá las centenas…", "¡*3.240*! Tiene solo 2 centenas."]},
 {"t": "errores", "items": [{"mal": "5.208 va después de 5.280", "bien": "5.208 va antes de 5.280"}],
  "voz": ["Ojo con este error.", "5.208 tiene *0 decenas*: va antes que 5.280."]},
 {"t": "resumen", "items": [["ORDENAR", "de a uno"], ["EL MÁS CHICO", "va primero"], ["SI EMPATAN", "miramos al lado"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Para ordenar, buscamos *de a uno*.", "De menor a mayor, el más chico va *primero*.", "Si empatan, miramos el lugar *de al lado*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Nico tiene 3.999 puntos. Gana 1 más. ¿Cuántos tiene?", "segundos": 8, "respuesta": "¡4.000!", "emoji": "🎮", "titulo": "ANTERIOR", "sub": "y siguiente",
  "voz": ["Desafío: Nico tiene 3.999 puntos y gana uno más.", "¡*4.000*! Se llenó un mil.", "Hoy: *anterior y siguiente*."]},
 {"t": "recta", "min": 3996, "max": 4002, "paso": 1, "marcas": [{"v": 3998, "txt": "anterior"}, {"v": 3999, "txt": "3.999"}, {"v": 4000, "txt": "siguiente"}],
  "voz": ["Mirá la recta alrededor del 3.999.", "El *anterior* es uno menos: 3.998.", "Acá está el *3.999*.", "El *siguiente* es uno más: ¡4.000!"]},
 {"t": "definicion", "palabra": "Siguiente", "texto": "El siguiente es uno más. El anterior es uno menos.", "emoji": "➡️",
  "voz": ["El *siguiente* es uno más.", "El *anterior* es uno menos."]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "siguiente de 2.499", "r": "2.500"}, {"p": "anterior de 7.000", "r": "6.999"}, {"p": "siguiente de 5.090", "r": "5.091"}],
  "voz": ["¡Ronda rápida! Decí el número que falta.", "El siguiente de 2.499 es *2.500*.", "El anterior de 7.000 es *6.999*.", "El siguiente de 5.090 es *5.091*."]},
 {"t": "errores", "items": [{"mal": "El anterior de 7.000 es 7.999", "bien": "El anterior de 7.000 es 6.999"}],
  "voz": ["Ojo con este error.", "El anterior de 7.000 es *6.999*: baja un mil."]},
 {"t": "resumen", "items": [["SIGUIENTE", "uno más"], ["ANTERIOR", "uno menos"], ["3.999", "y después 4.000"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *siguiente* es uno más.", "El *anterior* es uno menos.", "Después del 3.999 viene el *4.000*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Nico pasó la mitad del juego!", "bajada": "Ya tiene 5.000 puntos", "emoji": "📍", "titulo": "LA RECTA", "sub": "hasta 10.000",
  "voz": ["¡Último momento: Nico pasó la *mitad* del juego!", "Ya tiene *5.000* puntos de 10.000.", "Hoy: *la recta numérica hasta 10.000*."]},
 {"t": "recta", "min": 0, "max": 10000, "paso": 1000, "marcas": [{"v": 5000, "txt": "la mitad"}, {"v": 6400, "txt": "6.400"}],
  "voz": ["La recta va del 0 al 10.000.", "Avanza *de mil en mil*.", "El 5.000 está justo en la *mitad*.", "El *6.400* está entre 6.000 y 7.000."]},
 {"t": "deslizador", "titulo": "DEL 0 AL 10.000", "min": 0, "max": 10000, "emoji": "🎮", "paradas": [{"v": 2000, "txt": "cerca del 0"}, {"v": 5000, "txt": "la mitad"}, {"v": 9000, "txt": "cerca del final"}],
  "voz": ["Con 2.000 puntos, Nico está *cerca del 0*.", "Con 5.000, está en la *mitad*.", "¡Con 9.000, está cerca del *final*!"]},
 {"t": "prediccion", "pregunta": "¿Dónde va el 7.500?", "a": {"txt": "Entre 7.000 y 8.000", "emoji": "😎"}, "b": {"txt": "Entre 6.000 y 7.000", "emoji": "🤔"}, "correcta": "a", "resultado": "¡Entre 7.000 y 8.000!",
  "voz": ["¿Dónde va el 7.500?", "Mirá los miles: tiene 7…", "¡Entre *7.000 y 8.000*, en el medio!"]},
 {"t": "errores", "items": [{"mal": "Los números grandes van a la izquierda", "bien": "Los números grandes van a la derecha"}],
  "voz": ["Ojo con este error.", "Los números más grandes van a la *derecha*."]},
 {"t": "resumen", "items": [["LA RECTA", "de mil en mil"], ["5.000", "la mitad"], ["A LA DERECHA", "más grande"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La recta va *de mil en mil*.", "El 5.000 está en la *mitad*.", "Más a la derecha, *más grande*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m2-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 2 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
