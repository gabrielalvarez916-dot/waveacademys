# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 6 · Sustantivos: las 4 clases animadas.
Vía fonológica: la voz no nombra letras. Metáfora: el cuaderno viajero de Sofi en la plaza.
Genera tools/medio/clase/lecciones/medio-leng2-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '3eefcb8e-1517-4b5c-b0fd-2b0704f05da5', 2: '92d31ea5-2829-46a3-a972-d6f029fa51d4', 3: '640a6d88-1179-4ef7-8962-dc9e41d4f5b6', 4: '27fd048c-39e5-423d-ac37-91f73adb9572'}
TIT = {1: 'Palabras que nombran', 2: 'Sustantivos propios y comunes', 3: 'Buscar sustantivos en un cuento', 4: 'Clasificar sustantivos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🌳", "lineas": ["Sofi va a la plaza.", "Lleva su cuaderno viajero.", "Anota todo lo que ve."], "titulo": "PALABRAS", "sub": "que nombran",
  "voz": ["Sofi va a la *plaza*.", "Lleva su *cuaderno viajero*.", "Anota todo lo que ve: perro, pelota, banco.", "Hoy: *palabras que nombran*."]},
 {"t": "definicion", "palabra": "Sustantivo", "texto": "Palabra que nombra algo", "emoji": "🏷️",
  "voz": ["Las palabras que nombran se llaman *sustantivos*.", "Perro, pelota y banco son sustantivos."]},
 {"t": "zoom", "niveles": [{"emoji": "👩", "txt": "PERSONAS: MAMÁ"}, {"emoji": "🐶", "txt": "ANIMALES: PERRO"}, {"emoji": "⚽", "txt": "COSAS: PELOTA"}, {"emoji": "🏫", "txt": "LUGARES: ESCUELA"}],
  "voz": ["Los sustantivos nombran *personas*, como mamá.", "Nombran *animales*, como perro.", "Nombran *cosas*, como pelota.", "¡Y nombran *lugares*, como escuela!"]},
 {"t": "quiz4", "pregunta": "¿Cuál es un sustantivo?", "opciones": ["CORRE", "GATO", "LINDO", "SALTA"], "correcta": 1,
  "voz": ["¿Cuál de estas palabras *nombra* algo?", "Pensá: ¿cuál podés señalar?", "¡*Gato*! Nombra un animal."]},
 {"t": "unir", "titulo": "¿QUÉ NOMBRA?", "pares": [["MAESTRA", "persona"], ["PALOMA", "animal"], ["SILLA", "cosa"], ["PLAZA", "lugar"]], "mezclar": True,
  "voz": ["Unimos cada palabra con lo que nombra.", "Maestra: una *persona*.", "Paloma: un *animal*.", "Silla: una *cosa*.", "Plaza: un *lugar*."]},
 {"t": "resumen", "items": [["SUSTANTIVO", "nombra algo"], ["NOMBRA", "personas y animales"], ["TAMBIÉN", "cosas y lugares"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *sustantivo* es una palabra que nombra.", "Nombra *personas* y *animales*.", "También *cosas* y *lugares*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¡Tengo un perro nuevo! 🐶"}, {"yo": True, "txt": "¿Cómo se llama?"}, {"yo": False, "txt": "¡Se llama Pancho!"}], "titulo": "PROPIOS", "sub": "y comunes",
  "voz": ["Tomi le cuenta a Sofi: ¡tengo un perro nuevo!", "Sofi pregunta: ¿cómo se llama?", "¡Se llama *Pancho*!", "Hoy: *sustantivos propios y comunes*."]},
 {"t": "comparar", "a": {"cab": "PERRO", "texto": "cualquier perro", "emoji": "🐕"}, "b": {"cab": "Pancho", "texto": "un perro solo", "emoji": "🐶"}, "signo": "≠", "def": {"cab": "COMÚN Y PROPIO", "texto": "propio: nombre de uno solo"},
  "voz": ["*Perro* nombra a cualquier perro: es *común*.", "*Pancho* es el nombre de uno solo: es *propio*.", "Son dos tipos de sustantivos.", "El propio es el nombre de *uno solo*."]},
 {"t": "pizarra", "titulo": "CON MAYÚSCULA", "lineas": [{"txt": "Sofi", "marca": "circulo"}, {"txt": "Pancho", "marca": "circulo", "color": "coral"}, {"txt": "Córdoba", "marca": "circulo", "color": "verde"}],
  "voz": ["Los propios empiezan con *mayúscula*: Sofi.", "Pancho, también con mayúscula.", "¡Y Córdoba, el nombre de una ciudad!"]},
 {"t": "escape", "titulo": "¡A ESCAPAR DE LA PLAZA!", "candados": [{"p": "RÍO: ¿común o propio?", "r": "COMÚN"}, {"p": "PARANÁ: ¿común o propio?", "r": "PROPIO"}],
  "voz": ["¡La puerta de la plaza tiene candados!", "Río nombra a cualquiera: es *común*.", "Paraná es el nombre de uno: es *propio*.", "¡Escapamos!"]},
 {"t": "consejo", "titulo": "¿UNO SOLO?", "texto": "Si es el nombre de uno solo, es propio", "emoji": "☝️",
  "voz": ["Truco: si es el nombre de *uno solo*, es propio."]},
 {"t": "resumen", "items": [["COMÚN", "nombra a cualquiera"], ["PROPIO", "nombre de uno solo"], ["MAYÚSCULA", "en los propios"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *común* nombra a cualquiera.", "El *propio* es el nombre de uno solo.", "Los propios van con *mayúscula*.", CIERRE]},
]
N3 = [
 {"t": "historieta", "titulo": "EL CUENTO DE SOFI", "vinetas": [{"emojis": ["🐱", "🏠"], "txt": "Un gato vivía en una casa."}, {"emojis": ["🐱", "🐭"], "txt": "Un día vio un ratón."}, {"emojis": ["🐭", "👟"], "txt": "El ratón se escondió en un zapato."}],
  "voz": ["Un gato vivía en una casa.", "Un día vio un ratón.", "El ratón se escondió en un zapato. Hoy: *buscar sustantivos*."]},
 {"t": "texto", "oracion": "Un gato vivía en una casa", "marcas": [{"desde": 1, "hasta": 1, "etiqueta": "ANIMAL"}, {"desde": 5, "hasta": 5, "etiqueta": "LUGAR"}],
  "voz": ["Leemos despacio: un gato vivía en una casa.", "*Gato* nombra un animal: es sustantivo.", "*Casa* nombra un lugar: ¡también es sustantivo!"]},
 {"t": "texto", "oracion": "El ratón se escondió en un zapato", "marcas": [{"desde": 1, "hasta": 1, "etiqueta": "ANIMAL"}, {"desde": 6, "hasta": 6, "etiqueta": "COSA"}],
  "voz": ["Otra oración: el ratón se escondió en un zapato.", "*Ratón* nombra un animal.", "*Zapato* nombra una cosa."]},
 {"t": "consejo", "titulo": "UNA PISTA", "texto": "Antes del sustantivo va EL, LA, UN o UNA", "emoji": "🔎",
  "voz": ["Pista: antes suele ir *el*, *la*, *un* o *una*."]},
 {"t": "quiz4", "pregunta": "La nena come una manzana. ¿Cuál es sustantivo?", "opciones": ["COME", "UNA", "MANZANA", "LA"], "correcta": 2,
  "voz": ["Ahora vos: la nena come una manzana.", "¿Cuál nombra una fruta?", "¡*Manzana*! Es un sustantivo."]},
 {"t": "resumen", "items": [["LEER", "despacio"], ["BUSCAR", "palabras que nombran"], ["PISTA", "el, la, un, una"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos el cuento *despacio*.", "Buscamos las palabras que *nombran*.", "La pista: antes va *el*, *la*, *un* o *una*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "¿Qué es PATO: persona, animal, cosa o lugar?", "segundos": 8, "respuesta": "¡Un animal!", "emoji": "🦆", "titulo": "CLASIFICAR", "sub": "sustantivos",
  "voz": ["Desafío: ¿pato es persona, animal, cosa o lugar?", "¡Un *animal*!", "Hoy: *clasificar sustantivos*."]},
 {"t": "clasificar", "cajas": [{"cab": "PERSONAS", "emoji": "👩"}, {"cab": "ANIMALES", "emoji": "🐾"}, {"cab": "COSAS", "emoji": "📦"}, {"cab": "LUGARES", "emoji": "📍"}], "fichas": [{"txt": "NENE", "caja": 0}, {"txt": "GATO", "caja": 1}, {"txt": "VASO", "caja": 2}, {"txt": "PLAZA", "caja": 3}, {"txt": "MAMÁ", "caja": 0}, {"txt": "SILLA", "caja": 2}],
  "voz": ["Sofi arma cuatro cajas.", "Nene y mamá van a *personas*.", "Gato va a *animales*.", "Vaso y silla van a *cosas*.", "Plaza va a *lugares*."]},
 {"t": "mazo", "titulo": "TARJETAS DE SOFI", "items": [{"frente": "ESCUELA", "dorso": "LUGAR", "emoji": "🏫"}, {"frente": "Pancho", "dorso": "PROPIO", "emoji": "🐶"}, {"frente": "pelota", "dorso": "COSA · COMÚN", "emoji": "⚽"}],
  "voz": ["Escuela: es un *lugar*.", "Pancho: es un sustantivo *propio*.", "Pelota: es una *cosa*, y es común."]},
 {"t": "pistas", "problema": "¿Qué sustantivo es?", "pistas": ["Es un lugar", "Tiene hamacas y tobogán", "Sofi fue hoy"], "respuesta": "PLAZA",
  "voz": ["Adivinanza: ¿qué sustantivo es?", "Pista uno: es un *lugar*.", "Pista dos: tiene hamacas y tobogán.", "Pista tres: Sofi fue hoy.", "¡La *plaza*!"]},
 {"t": "errores", "items": [{"mal": "PLAZA en COSAS", "bien": "PLAZA en LUGARES"}],
  "voz": ["Cuidado con este error.", "Plaza no es una cosa: va en *lugares*."]},
 {"t": "resumen", "items": [["CUATRO CAJAS", "personas, animales, cosas, lugares"], ["DOS CAJAS", "comunes y propios"], ["PREGUNTA", "¿qué nombra?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cuatro cajas: personas, animales, cosas y lugares.", "Dos cajas más: *comunes* y *propios*.", "Siempre preguntamos: ¿qué nombra?", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m6-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 6 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
