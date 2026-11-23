# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 2 · Numbers 1 to 10: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: el tren de los números de Tomi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 2
TIT = {1: 'Counting from 1 to 5', 2: 'Counting from 6 to 10', 3: 'How old are you?', 4: 'Number songs and games'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "gancho", "emoji": "🖐️", "final": "🤔", "titulo": "ONE, TWO, THREE!", "sub": "del 1 al 5",
  "voz": ["Tomi mira su mano.", "¿Cómo se cuentan los dedos en inglés?", "Hoy: *contar del 1 al 5 en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "ONE", "emoji": "1️⃣", "trad": "uno", "pron": "uán"}, {"palabra": "TWO", "emoji": "2️⃣", "trad": "dos", "pron": "tú"}, {"palabra": "THREE", "emoji": "3️⃣", "trad": "tres", "pron": "zrí"}, {"palabra": "FOUR", "emoji": "4️⃣", "trad": "cuatro", "pron": "for"}, {"palabra": "FIVE", "emoji": "5️⃣", "trad": "cinco", "pron": "fáiv"}],
  "voz": ["One!", "Two!", "Three!", "Four!", "Five!"], "voz_en": [0, 1, 2, 3, 4]},
 {"t": "contar", "titulo": "HOW MANY STARS?", "emoji": "⭐", "cantidad": 5, "etiqueta": "FIVE STARS!",
  "voz": ["Contemos las estrellas en inglés.", "1, 2, 3, 4, 5!", "Five stars!"], "voz_en": [1, 2]},
 {"t": "pregunta", "pregunta": "¿Cómo se dice 3 en inglés?", "opciones": ["THREE", "TWO", "FIVE"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el número tres.", "¿Cómo se dice en inglés?", "Three!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "UN DEDO POR NÚMERO", "texto": "Tocá cada cosa al contar", "emoji": "☝️",
  "voz": ["Truco: *tocá* cada cosa al contar."]},
 {"t": "resumen", "items": [["ONE, TWO", "1 y 2"], ["THREE, FOUR", "3 y 4"], ["FIVE", "5"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "One, two, three, four, five!", "Con una mano llegamos a *five*.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎈", "lineas": ["Es el cumple de Sofi.", "Hay muchos globos.", "¿Cuántos hay? ¡Más de cinco!"], "titulo": "SIX TO TEN", "sub": "del 6 al 10",
  "voz": ["Es el *cumple* de Sofi.", "Hay muchos *globos*.", "¡Son más de cinco!", "Hoy: *contar del 6 al 10 en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "SIX", "emoji": "6️⃣", "trad": "seis", "pron": "sics"}, {"palabra": "SEVEN", "emoji": "7️⃣", "trad": "siete", "pron": "séven"}, {"palabra": "EIGHT", "emoji": "8️⃣", "trad": "ocho", "pron": "éit"}, {"palabra": "NINE", "emoji": "9️⃣", "trad": "nueve", "pron": "náin"}, {"palabra": "TEN", "emoji": "🔟", "trad": "diez", "pron": "ten"}],
  "voz": ["Six!", "Seven!", "Eight!", "Nine!", "Ten!"], "voz_en": [0, 1, 2, 3, 4]},
 {"t": "tren", "titulo": "EL TREN DEL 1 AL 10", "desde": 1, "hasta": 10, "paso": 1,
  "voz": ["Llega el tren de los *números*.", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10!", "Ten! ¡Llegamos al diez!"], "voz_en": [1]},
 {"t": "pregunta", "pregunta": "¿Cómo se dice 8 en inglés?", "opciones": ["EIGHT", "SIX", "TEN"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el número ocho.", "¿Cómo se dice en inglés?", "Eight!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "DOS MANOS", "texto": "Con las dos manos llegás a TEN", "emoji": "🙌",
  "voz": ["Truco: con las *dos manos* llegás a diez."]},
 {"t": "resumen", "items": [["SIX, SEVEN", "6 y 7"], ["EIGHT, NINE", "8 y 9"], ["TEN", "10"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Six, seven, eight, nine, ten!", "Ya contamos hasta *diez*.", CIERRE], "voz_en": [1]},
]
N3 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "HOW OLD ARE YOU?"}, {"yo": True, "txt": "I AM SIX!"}, {"yo": False, "txt": "I AM SEVEN!"}], "titulo": "HOW OLD ARE YOU?", "sub": "mi edad en inglés",
  "voz": ["Tomi le escribe a Sofi.", "How old are you?", "Le pregunta cuántos años tiene.", "Hoy: *mi edad en inglés*."], "voz_en": [1]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "TOMI", "emoji": "👦"}], "lineas": [{"quien": 1, "txt": "HOW OLD ARE YOU?", "trad": "¿cuántos años tenés?"}, {"quien": 0, "txt": "I AM SIX.", "trad": "tengo seis"}, {"quien": 0, "txt": "AND YOU?", "trad": "¿y vos?"}, {"quien": 1, "txt": "I AM SEVEN.", "trad": "tengo siete"}],
  "voz": ["How old are you?", "I am six.", "And you?", "I am seven."], "voz_en": [0, 1, 2, 3]},
 {"t": "barras", "titulo": "LOS AÑOS DE MIS AMIGOS", "unidad": "años", "items": [{"txt": "SOFI", "valor": 6}, {"txt": "TOMI", "valor": 7}, {"txt": "LEO", "valor": 5}],
  "voz": ["Comparamos los años de los chicos.", "Sofi: I am six.", "Tomi: I am seven.", "Leo: I am five."], "voz_en": [1, 2, 3]},
 {"t": "pregunta", "pregunta": "Tenés 6 años. ¿Qué decís?", "opciones": ["I AM SIX", "I AM TEN", "I AM SAD"], "correcta": 0,
  "voz": ["Ahora vos. Tenés seis años.", "¿Qué decís en inglés?", "I am six!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "MOSTRÁ LOS DEDOS", "texto": "Mostrá tus años con los dedos", "emoji": "🖐️",
  "voz": ["Truco: mostrá tus *años* con los dedos."]},
 {"t": "resumen", "items": [["HOW OLD ARE YOU?", "¿cuántos años tenés?"], ["I AM SIX", "tengo seis"], ["AGE", "edad"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "How old are you?", "Contestamos con el número.", "I am six!", CIERRE], "voz_en": [1, 3]},
]
N4 = [
 {"t": "reto", "texto": "¿Podés contar hasta TEN en inglés?", "segundos": 8, "respuesta": "¡ONE… TEN!", "emoji": "🎵", "titulo": "NUMBER GAMES", "sub": "cantar y jugar",
  "voz": ["Desafío: ¿podés contar hasta diez en inglés?", "One, two, three, four, five, six, seven, eight, nine, ten!", "Hoy: *cantar y jugar con números*."], "voz_en": [1]},
 {"t": "juntar", "a": {"emoji": "🚗", "n": 3}, "b": {"emoji": "🚗", "n": 2}, "texto": "THREE + TWO = FIVE",
  "voz": ["Tomi tiene tres autos y dos más.", "Los juntamos.", "Three and two is five!"], "voz_en": [2]},
 {"t": "recta", "min": 1, "max": 10, "paso": 1, "marcas": [{"v": 2, "txt": "TWO"}, {"v": 5, "txt": "FIVE"}, {"v": 9, "txt": "NINE"}],
  "voz": ["Saltamos por los números del uno al diez.", "Two!", "Five!", "Nine!"], "voz_en": [1, 2, 3]},
 {"t": "pregunta", "pregunta": "TWO + TWO = ?", "opciones": ["FOUR", "THREE", "SIX"], "correcta": 0,
  "voz": ["Ahora vos. Juntá dos y dos.", "¿Cuánto da en inglés?", "Four!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "APLAUDÍ", "texto": "Da un aplauso por cada número", "emoji": "👏",
  "voz": ["Juego: da un *aplauso* por cada número."]},
 {"t": "resumen", "items": [["CANCIÓN", "del ONE al TEN"], ["JUNTAR", "sumar jugando"], ["SALTAR", "por los números"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Cantamos* del uno al diez.", "*Juntamos* cosas y contamos.", "Y *saltamos* por los números.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
