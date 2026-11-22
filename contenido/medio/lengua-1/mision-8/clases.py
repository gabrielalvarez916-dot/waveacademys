# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 8 · La oración: las 4 clases animadas.
Metáfora: el tren de las palabras. Regla de primeros años, vía fonológica (la voz nunca nombra letras) y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-leng1-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'eee219b3-9188-4e94-be06-223054ed5a57'
TIT = {1: 'Palabras que forman oraciones', 2: 'Mayúscula y punto', 3: 'Ordenar palabras para armar oraciones', 4: 'Escribir mis primeras oraciones'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "reto", "texto": "¿Cuántas palabras dice: EL OSO TOMA SOPA?", "segundos": 6, "respuesta": "¡4 PALABRAS!", "emoji": "🐻", "titulo": "LA ORACIÓN", "sub": "un tren de palabras",
  "voz": ["Desafío: ¿cuántas palabras escuchás?", "El oso toma sopa: ¡*4 palabras*!", "Hoy: *el tren de las palabras*."]},
 {"t": "bloques", "titulo": "EL TREN", "items": [{"cab": "🚃 1", "txt": "EL"}, {"cab": "🚃 2", "txt": "OSO"}, {"cab": "🚃 3", "txt": "TOMA"}, {"cab": "🚃 4", "txt": "SOPA"}],
  "voz": ["Cada palabra es un *vagón*.", "Primer vagón: *el*.", "Segundo vagón: *oso*.", "Tercer vagón: *toma*.", "Cuarto vagón: *sopa*."]},
 {"t": "texto", "oracion": "EL SOL SALE", "marcas": [{"desde": 0, "hasta": 0, "etiqueta": "1", "color": "sol"}, {"desde": 1, "hasta": 1, "etiqueta": "2", "color": "sol"}, {"desde": 2, "hasta": 2, "etiqueta": "3", "color": "sol"}],
  "voz": ["Juntas, las palabras dicen algo.", "*El*: una.", "*Sol*: dos.", "*Sale*: tres. ¡Es una *oración*!"]},
 {"t": "consejo", "titulo": "UN APLAUSO", "texto": "Un aplauso por cada palabra", "emoji": "👏",
  "voz": ["Truco: un *aplauso* por cada palabra."]},
 {"t": "pregunta", "pregunta": "¿Cuál es una oración?", "opciones": ["SOL EL", "EL SOL SALE", "SALE SOL"], "correcta": 1,
  "voz": ["Ahora vos. ¿Cuál dice algo?", "Pensá cuál se entiende.", "¡*El sol sale*! Se entiende."]},
 {"t": "resumen", "items": [["VAGÓN", "cada palabra"], ["TREN", "la oración"], ["DICE ALGO", "se entiende"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cada palabra es un *vagón*.", "El tren es la *oración*.", "La oración *dice algo*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🚂", "lineas": ["Sofi maneja el tren.", "Arranca con la mayúscula.", "¡Y frena en el punto!"], "titulo": "MAYÚSCULA", "sub": "y punto",
  "voz": ["Sofi maneja el *tren* de palabras.", "Arranca con la *mayúscula*.", "¡Y frena en el *punto*!", "Hoy: *cómo empieza y cómo termina*."]},
 {"t": "parrafo", "titulo": "MAMÁ MIMA A SOFI.", "lineas": ["Mamá mima a Sofi."], "marcas": [{"linea": 0, "pos": "inicio", "txt": "MAYÚSCULA"}, {"linea": 0, "pos": "fin", "txt": "PUNTO"}],
  "voz": ["Leemos: mamá mima a Sofi.", "Al principio, la letra *grande*: *mayúscula*.", "Al final, un puntito: el *punto*."]},
 {"t": "antesdespues", "antes": {"cab": "ARRANCA", "emoji": "🚂", "texto": "Mayúscula"}, "despues": {"cab": "FRENA", "emoji": "🛑", "texto": "Punto"},
  "voz": ["La mayúscula *arranca* el tren.", "El punto lo *frena*."]},
 {"t": "corrige", "titulo": "ARREGLAMOS", "cambios": [{"antes": "el pato nada", "despues": "El pato nada.", "motivo": "mayúscula y punto"}],
  "voz": ["¡Ups! A esta oración le faltan cosas.", "Le ponemos *mayúscula* y *punto*."]},
 {"t": "pregunta", "pregunta": "¿Qué va al final de la oración?", "opciones": ["UN PUNTO", "UNA MAYÚSCULA", "NADA"], "correcta": 0,
  "voz": ["Ahora vos. ¿Qué frena el tren?", "Pensá qué va al final.", "¡*Un punto*!"]},
 {"t": "resumen", "items": [["MAYÚSCULA", "al principio"], ["PUNTO", "al final"], ["REVISAR", "mirar las dos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *mayúscula* va al principio.", "El *punto* va al final.", "Siempre *revisamos* las dos.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SE MEZCLÓ EL TREN!", "bajada": "Las palabras no se entienden", "emoji": "🚃", "titulo": "ORDENAR", "sub": "palabras",
  "voz": ["¡Último momento! ¡Se mezcló el *tren*!", "Las palabras quedaron revueltas.", "Hoy: *ordenar palabras*."]},
 {"t": "fichas", "fichas": ["SOPA", "TOMA", "OSO", "EL"], "grande": "EL OSO TOMA SOPA", "etiqueta": "¿QUIÉN? · ¿QUÉ HACE?",
  "voz": ["Sopa, toma, oso, el. ¡No se entiende!", "Primero, ¿quién? *El oso*.", "¿Qué hace? *Toma sopa*."]},
 {"t": "balanza", "izq": {"cab": "MEZCLADA", "items": ["NADA PATO EL"]}, "der": {"cab": "ORDENADA", "items": ["EL PATO NADA"]}, "gana": "der",
  "voz": ["Comparamos las dos.", "Nada pato el: no se entiende.", "*El pato nada*: ¡esta gana!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra va primero? SALE SOL EL", "opciones": ["SALE", "EL", "SOL"], "correcta": 1,
  "voz": ["Ahora vos. Sale, sol, el.", "¿Qué palabra va primero?", "¡*El*! El sol sale."]},
 {"t": "consejo", "titulo": "LEÉ PARA REVISAR", "texto": "Si se entiende, está bien", "emoji": "👀",
  "voz": ["Truco: leé la oración y fijate si *se entiende*."]},
 {"t": "resumen", "items": [["MEZCLADAS", "no se entiende"], ["ORDENAR", "quién y qué hace"], ["REVISAR", "leer otra vez"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Mezcladas, *no se entienden*.", "Primero *quién*, después *qué hace*.", "Y *leemos otra vez*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Qué hace tu papá?"}, {"yo": True, "txt": "MI PAPÁ TOMA MATE."}, {"yo": False, "txt": "¡Qué linda oración!"}], "titulo": "ESCRIBIR", "sub": "mis oraciones",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué hace tu papá?", "Sofi escribe una *oración*.", "Hoy: *escribir mis oraciones*."]},
 {"t": "flujo", "titulo": "CÓMO ESCRIBO", "items": ["PIENSO", "LO DIGO", "LO ESCRIBO", "LO LEO"],
  "voz": ["Primero, *pienso* qué decir.", "Después, lo *digo* en voz alta.", "Ahora, lo *escribo*.", "Al final, lo *leo*."]},
 {"t": "comparar", "a": {"cab": "SIN ESPACIOS", "texto": "ELSOLSALE", "emoji": "😵"}, "b": {"cab": "CON ESPACIOS", "texto": "EL SOL SALE.", "emoji": "😃"}, "signo": "vs",
  "voz": ["Todo pegado, no se puede leer.", "Con *espacios*, ¡sí se lee!", "Dejá un espacio entre palabras."]},
 {"t": "corrige", "titulo": "REVISO", "cambios": [{"antes": "mi mamá toma té", "despues": "Mi mamá toma té.", "motivo": "mayúscula y punto"}, {"antes": "ELOSO", "despues": "EL OSO", "motivo": "espacio"}],
  "voz": ["Sofi revisa lo que escribió.", "Pone *mayúscula* y *punto*.", "Y separa con un *espacio*."]},
 {"t": "pregunta", "pregunta": "¿Cuál está bien escrita?", "opciones": ["MIPAPÁTOMAMATE", "MI PAPÁ TOMA MATE.", "mi papá toma mate"], "correcta": 1,
  "voz": ["Ahora vos. Mirá las tres.", "¿Cuál tiene espacios, mayúscula y punto?", "¡*Mi papá toma mate*!"]},
 {"t": "resumen", "items": [["PENSAR", "decir en voz alta"], ["ESCRIBIR", "con espacios"], ["REVISAR", "mayúscula y punto"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Primero *pensamos* y decimos.", "Escribimos con *espacios*.", "Y revisamos *mayúscula y punto*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m8-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": 8, "nivel": n}, "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 8 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
