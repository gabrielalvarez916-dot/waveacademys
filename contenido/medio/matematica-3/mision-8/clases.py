# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 8 · Estimar y calcular con calculadora: las 4 clases animadas.
Metáfora de toda la misión: la campaña de tapitas solidarias de la escuela, con Tomi como encargado de la calculadora.
Regla de primeros años. Genera tools/medio/clase/lecciones/medio-mat3-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '373731a4-a5b3-4d3a-ba76-432f6a45817b', 2: '61658faa-70d5-4194-8424-18f89730ff3e', 3: '1a68d468-bff4-4e47-9b70-1f3ff88a1be9', 4: '72f158e2-5bb7-47b5-bacf-b5d8771bdd4b'}
TIT = {1: 'Estimar antes de calcular', 2: 'La calculadora como control', 3: 'Teclas que no funcionan', 4: 'Resolver problemas con calculadora'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "Juntamos 3.890 y 2.105 tapitas"}, {"yo": True, "txt": "¿Usamos la calculadora?"}, {"yo": False, "txt": "Primero pensemos cuánto puede dar"}], "titulo": "ESTIMAR", "sub": "antes de calcular",
  "voz": ["Tomi escribe: juntamos 3.890 y 2.105 tapitas.", "¿Usamos la calculadora?", "Primero pensemos *cuánto puede dar*.", "Hoy: *estimar antes de calcular*."]},
 {"t": "pizarra", "titulo": "ESTIMAMOS", "lineas": [{"txt": "3.890 → 4.000"}, {"txt": "2.105 → 2.000"}, {"txt": "CERCA DE 6.000", "color": "verde", "marca": "circulo"}],
  "voz": ["El 3.890 está muy cerca del *4.000*.", "El 2.105 está muy cerca del *2.000*.", "¡Tiene que dar *cerca de 6.000*!"]},
 {"t": "calculadora", "titulo": "AHORA SÍ", "teclas": ["3", "8", "9", "0", "+", "2", "1", "0", "5"], "resultado": "5995", "texto": "3890 + 2105",
  "voz": ["Ahora sí, apretamos las teclas con mucho cuidado.", "3.890, más, 2.105, igual.", "¡Sale *5.995*: está cerca de 6.000!"]},
 {"t": "quiz4", "pregunta": "4.120 + 2.950 da cerca de…", "opciones": ["7.000", "70.000", "700"], "correcta": 0,
  "voz": ["Ahora vos: 4.120 más 2.950, ¿cerca de cuánto da?", "4.000 más 3.000…", "¡Cerca de *7.000*!"]},
 {"t": "errores", "items": [{"mal": "Estimar después de la cuenta", "bien": "Estimar antes, para saber qué esperar"}],
  "voz": ["Ojo con este error.", "Estimamos *antes*, para saber qué número esperar."]},
 {"t": "resumen", "items": [["ESTIMAR", "antes de calcular"], ["REDONDOS", "al mil cercano"], ["COMPARAR", "con la pantalla"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Estimamos *antes* de calcular.", "Usamos números *redondos*.", "Después comparamos con la *pantalla*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡La calculadora dio 29.130 tapitas!", "bajada": "¿Será verdad?", "emoji": "🧮", "titulo": "CONTROLAR", "sub": "con la calculadora",
  "voz": ["¡Último momento: la calculadora dio *29.130* tapitas!", "¿Será verdad?", "Hoy: *la calculadora como control*."]},
 {"t": "dato", "numero": "4.223", "antes": "2.768 + 1.455", "despues": "no 29.130", "texto": "Se apretó una tecla de más", "emoji": "🔍",
  "voz": ["Pero la cuenta era 2.768 más 1.455.", "¡Da *4.223*! Se apretó una tecla de más."]},
 {"t": "transforma", "titulo": "DOS CAMINOS", "pasos": [{"txt": "3.400 + 1.500 = 4.900"}, {"txt": "LO HAGO A MANO", "nota": "o con calculadora"}, {"txt": "¡IGUAL! ✓"}],
  "voz": ["Hicimos una suma con lápiz y papel: 4.900.", "Después la hacemos otra vez con la *calculadora*.", "¡Dan *igual*: la cuenta está bien!"]},
 {"t": "vof", "afirmacion": "La calculadora nunca se equivoca", "emoji": "🤔", "verdadero": False, "explicacion": "Hace lo que apretamos",
  "voz": ["¿Verdadero o falso? La calculadora nunca se equivoca.", "Pensá quién aprieta las teclas…", "¡*Falso*! Hace *lo que apretamos*."]},
 {"t": "errores", "items": [{"mal": "Creer cualquier resultado", "bien": "Comparar con lo estimado"}],
  "voz": ["Ojo con este error.", "Siempre comparamos la pantalla con lo *estimado*."]},
 {"t": "resumen", "items": [["CONTROLAR", "con la calculadora"], ["ESTIMAR", "para revisar"], ["APRETAR", "con cuidado"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La calculadora sirve para *controlar*.", "Estimamos para *revisar* lo que sale.", "Y apretamos las teclas *con cuidado*.", CIERRE]},
]
N3 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🧮", "lineas": ["A la calculadora de Tomi se le rompió el 5.", "Necesita escribir 3.500.", "¿Cómo hace?"], "titulo": "TECLAS", "sub": "que no funcionan",
  "voz": ["A la calculadora de Tomi se le rompió el *5*.", "Necesita escribir *3.500*.", "¿Cómo hace?", "Hoy: *teclas que no funcionan*."]},
 {"t": "descomponer", "numero": "3.500", "titulo": "SIN EL 5", "partes": ["3.400", "100"], "resultado": "= 3.500 ✓",
  "voz": ["Buscamos dos números *sin el 5*.", "3.400 no tiene 5.", "100 tampoco tiene 5.", "Los sumamos.", "¡3.400 más 100 es *3.500*!"]},
 {"t": "calculadora", "titulo": "SIN TOCAR EL 5", "teclas": ["3", "4", "0", "0", "+", "1", "0", "0"], "resultado": "3500", "texto": "3400 + 100",
  "voz": ["Apretamos 3.400.", "Después más 100, igual.", "¡Aparece *3.500* sin tocar el 5!"]},
 {"t": "escape", "titulo": "LA TECLA 7 NO ANDA", "candados": [{"p": "¿Cómo hago 2.700?", "r": "2.600 + 100"}, {"p": "¿Cómo hago 7.000?", "r": "6.000 + 1.000"}],
  "voz": ["¡Escape! La tecla 7 no anda.", "2.700: 2.600 más *100*.", "7.000: 6.000 más *1.000*.", "¡Escapamos!"]},
 {"t": "errores", "items": [{"mal": "Usar un número que tiene la tecla rota", "bien": "Revisar cada número"}],
  "voz": ["Ojo con este error.", "Revisá que *ningún número* tenga la tecla rota."]},
 {"t": "resumen", "items": [["TECLA ROTA", "buscar otro camino"], ["DESARMAR", "en partes"], ["REVISAR", "cada número"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Con una tecla rota, buscamos *otro camino*.", "*Desarmamos* el número en partes.", "Y *revisamos* cada número.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "Tres grados juntaron 2.350, 1.870 y 960 tapitas. ¿Cuántas?", "segundos": 8, "respuesta": "¡5.180!", "emoji": "🧮", "titulo": "PROBLEMAS", "sub": "con calculadora",
  "voz": ["Desafío: tres grados juntaron tapitas.", "2.350, 1.870 y 960.", "¡Son *5.180*!", "Hoy: *problemas con calculadora*."]},
 {"t": "flujo", "titulo": "CÓMO LO HACEMOS", "items": [{"txt": "Leo el problema", "emoji": "👀"}, {"txt": "Estimo", "emoji": "🎯"}, {"txt": "Calculo", "emoji": "🧮"}, {"txt": "Comparo", "emoji": "✅"}],
  "voz": ["Primero *leemos* el problema con atención.", "Después *estimamos*: cerca de 5.000.", "*Calculamos* con la calculadora.", "Y *comparamos*: ¡5.180 tiene sentido!"]},
 {"t": "pistas", "problema": "Tienen 5.180 tapitas. Quieren llegar a 8.000.", "pistas": ["Es una distancia", "8.000 − 5.180"], "respuesta": "2.820",
  "voz": ["Ahora quieren llegar a *8.000* tapitas.", "Pista: es una *distancia*.", "Pista: en la calculadora, 8.000 menos 5.180.", "¡Les faltan *2.820*!"]},
 {"t": "contrarreloj", "titulo": "¿TIENE SENTIDO?", "segundos": 20, "items": [{"p": "1.900 + 2.100 = 4.000", "r": "SÍ"}, {"p": "3.000 + 2.000 = 50.000", "r": "NO"}, {"p": "6.000 − 1.000 = 5.000", "r": "SÍ"}],
  "voz": ["¡Ronda rápida! ¿Tiene sentido?", "1.900 más 2.100, 4.000: *sí*.", "3.000 más 2.000, 50.000: *no*.", "6.000 menos 1.000, 5.000: *sí*."]},
 {"t": "errores", "items": [{"mal": "Escribir la respuesta sin mirar si tiene sentido", "bien": "Comparar con lo estimado"}],
  "voz": ["Ojo con este error.", "Antes de responder, mirá si *tiene sentido*."]},
 {"t": "resumen", "items": [["LEER", "el problema"], ["ESTIMAR", "y calcular"], ["RESPONDER", "con sentido"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero *leemos* el problema.", "*Estimamos* y después calculamos.", "Respondemos si *tiene sentido*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-mat3-m8-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Matemática 3", "titulo": TIT[n], "sub": f"Matemática 3 · Misión 8 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
