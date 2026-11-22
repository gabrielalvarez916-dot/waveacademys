# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 1 · Hello! Greetings and Names: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: los títeres amigos de Sofi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 1
TIT = {1: 'Hello and goodbye', 2: "What's your name?", 3: 'How are you? Happy and sad', 4: 'Nice to meet you: puppet friends'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🏫", "lineas": ["Sofi llega a la escuela.", "Ve a su maestra de inglés.", "¡La maestra la saluda!"], "titulo": "HELLO!", "sub": "hola y chau",
  "voz": ["Sofi llega a la escuela.", "Ve a su maestra de *inglés*.", "Hello, Sofi!", "Hoy: *hola y chau en inglés*."], "voz_en": [2]},
 {"t": "vocab", "items": [{"palabra": "HELLO", "emoji": "👋", "trad": "hola", "pron": "jelóu"}, {"palabra": "HI", "emoji": "🙂", "trad": "hola", "pron": "jái"}, {"palabra": "GOODBYE", "emoji": "🚪", "trad": "chau", "pron": "gudbái"}, {"palabra": "BYE", "emoji": "✋", "trad": "chau", "pron": "bái"}],
  "voz": ["Hello!", "Hi!", "Goodbye!", "Bye!"], "voz_en": [0, 1, 2, 3]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "MAESTRA", "emoji": "👩‍🏫"}], "lineas": [{"quien": 0, "txt": "HELLO!", "trad": "¡hola!"}, {"quien": 1, "txt": "HI, SOFI!", "trad": "¡hola, Sofi!"}, {"quien": 0, "txt": "GOODBYE!", "trad": "¡chau!"}],
  "voz": ["Hello!", "Hi, Sofi!", "Goodbye!"], "voz_en": [0, 1, 2]},
 {"t": "pregunta", "pregunta": "Te vas a tu casa. ¿Qué decís?", "opciones": ["GOODBYE", "HELLO", "HI"], "correcta": 0,
  "voz": ["Ahora vos. Te vas a tu casa.", "¿Qué decís en inglés?", "Goodbye!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "CON LA MANO", "texto": "Mové la mano cuando saludás", "emoji": "👋",
  "voz": ["Truco: *mové la mano* cuando saludás."]},
 {"t": "resumen", "items": [["HELLO", "hola"], ["HI", "hola"], ["GOODBYE", "chau"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Para llegar decimos *hello*.", "También decimos *hi*.", "Para irnos decimos *goodbye*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "HI! WHAT IS YOUR NAME?"}, {"yo": True, "txt": "MY NAME IS SOFI!"}, {"yo": False, "txt": "¡Genial!"}], "titulo": "MY NAME IS…", "sub": "mi nombre en inglés",
  "voz": ["Tomi le escribe a una nena nueva.", "Le pregunta su *nombre*.", "My name is Sofi!", "Hoy: *mi nombre en inglés*."], "voz_en": [2]},
 {"t": "dialogo", "personas": [{"nombre": "TOMI", "emoji": "👦"}, {"nombre": "SOFI", "emoji": "👧"}], "lineas": [{"quien": 0, "txt": "WHAT IS YOUR NAME?", "trad": "¿cómo te llamás?"}, {"quien": 1, "txt": "MY NAME IS SOFI.", "trad": "me llamo Sofi"}, {"quien": 1, "txt": "AND YOU?", "trad": "¿y vos?"}, {"quien": 0, "txt": "MY NAME IS TOMI.", "trad": "me llamo Tomi"}],
  "voz": ["What is your name?", "My name is Sofi.", "And you?", "My name is Tomi."], "voz_en": [0, 1, 2, 3]},
 {"t": "comparar", "a": {"cab": "PREGUNTO", "texto": "WHAT IS YOUR NAME?", "emoji": "❓"}, "b": {"cab": "CONTESTO", "texto": "MY NAME IS…", "emoji": "🙋"}, "signo": "→",
  "voz": ["Para *preguntar* el nombre.", "What is your name?", "Para *contestar*, decís tu nombre.", "My name is…"], "voz_en": [1, 3]},
 {"t": "pregunta", "pregunta": "¿Qué falta? MY ___ IS TOMI", "opciones": ["NAME", "HELLO", "BYE"], "correcta": 0,
  "voz": ["Ahora vos. Mirá la frase de Tomi.", "¿Qué palabra falta?", "Name!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "SEÑALATE", "texto": "Al decir MY, tocate el pecho", "emoji": "🙋",
  "voz": ["Truco: al decir *my*, tocate el pecho."]},
 {"t": "resumen", "items": [["WHAT IS YOUR NAME?", "¿cómo te llamás?"], ["MY NAME IS…", "me llamo…"], ["NAME", "nombre"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Preguntamos el nombre en inglés.", "Contestamos con *my name is*.", "*Name* es nombre.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Cómo se dice feliz en inglés?", "segundos": 6, "respuesta": "¡HAPPY!", "emoji": "😀", "titulo": "HOW ARE YOU?", "sub": "feliz y triste",
  "voz": ["Desafío: ¿cómo se dice feliz en inglés?", "Happy!", "Hoy: *cómo estás en inglés*."], "voz_en": [1]},
 {"t": "vocab", "items": [{"palabra": "HAPPY", "emoji": "😀", "trad": "feliz", "pron": "jápi"}, {"palabra": "SAD", "emoji": "😢", "trad": "triste", "pron": "sad"}, {"palabra": "FINE", "emoji": "🙂", "trad": "bien", "pron": "fáin"}],
  "voz": ["Happy!", "Sad!", "Fine!"], "voz_en": [0, 1, 2]},
 {"t": "comparar", "a": {"cab": "HAPPY", "texto": "Sonríe", "emoji": "😀"}, "b": {"cab": "SAD", "texto": "Llora", "emoji": "😢"}, "signo": "vs",
  "voz": ["Mirá las dos caras.", "*Happy* sonríe: está feliz.", "*Sad* llora: está triste."]},
 {"t": "clasificar", "cajas": [{"cab": "HAPPY", "emoji": "😀"}, {"cab": "SAD", "emoji": "😢"}], "fichas": [{"txt": "GANÉ UN PREMIO", "caja": 0}, {"txt": "ES MI CUMPLE", "caja": 0}, {"txt": "PERDÍ MI PELOTA", "caja": 1}, {"txt": "ROMPÍ MI JUGUETE", "caja": 1}],
  "voz": ["¿Cómo se siente cada uno?", "Ganar un premio y el cumple: *happy*.", "Perder la pelota o romper un juguete: *sad*."]},
 {"t": "pregunta", "pregunta": "Tomi perdió su pelota. ¿Cómo está?", "opciones": ["SAD", "HAPPY", "HELLO"], "correcta": 0,
  "voz": ["Ahora vos. Tomi perdió su pelota.", "¿Cómo está Tomi?", "¡*Sad*! Está triste."]},
 {"t": "consejo", "titulo": "HACÉ LA CARA", "texto": "Sonreí al decir HAPPY", "emoji": "😀",
  "voz": ["Truco: *sonreí* al decir happy."]},
 {"t": "resumen", "items": [["HOW ARE YOU?", "¿cómo estás?"], ["HAPPY", "feliz"], ["SAD", "triste"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "How are you?", "*Happy* es feliz.", "*Sad* es triste.", CIERRE], "voz_en": [1]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡LLEGAN LOS TÍTERES!", "bajada": "Leo y Mia hablan inglés", "emoji": "🧸", "titulo": "NICE TO MEET YOU!", "sub": "títeres amigos",
  "voz": ["¡Último momento! Llegan los *títeres*.", "Leo y Mia hablan *inglés*.", "Hoy: *mucho gusto en inglés*."]},
 {"t": "dialogo", "personas": [{"nombre": "LEO", "emoji": "🐶"}, {"nombre": "MIA", "emoji": "🐱"}], "lineas": [{"quien": 0, "txt": "HELLO! MY NAME IS LEO.", "trad": "¡hola! me llamo Leo"}, {"quien": 1, "txt": "HI! MY NAME IS MIA.", "trad": "¡hola! me llamo Mia"}, {"quien": 0, "txt": "NICE TO MEET YOU!", "trad": "¡mucho gusto!"}, {"quien": 1, "txt": "NICE TO MEET YOU!", "trad": "¡mucho gusto!"}],
  "voz": ["Hello! My name is Leo.", "Hi! My name is Mia.", "Nice to meet you!", "Nice to meet you too!"], "voz_en": [0, 1, 2, 3]},
 {"t": "flujo", "titulo": "UNA CHARLA", "items": ["HELLO!", "MY NAME IS…", "NICE TO MEET YOU!", "GOODBYE!"],
  "voz": ["Primero, *saludo*.", "Después, digo mi *nombre*.", "Digo *mucho gusto*.", "Y al final, *goodbye*."]},
 {"t": "pregunta", "pregunta": "Conocés a alguien nuevo. ¿Qué decís?", "opciones": ["NICE TO MEET YOU", "I AM SAD", "GOODBYE"], "correcta": 0,
  "voz": ["Ahora vos. Conocés a alguien nuevo.", "¿Qué le decís?", "Nice to meet you!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "TU TÍTERE", "texto": "Hacé un títere con una media", "emoji": "🧦",
  "voz": ["Idea: hacé un *títere* con una media."]},
 {"t": "resumen", "items": [["NICE TO MEET YOU", "mucho gusto"], ["CHARLA", "saludo, nombre, chau"], ["TÍTERES", "para practicar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Nice to meet you!", "Una charla: saludo, nombre y chau.", "¡Y practicamos con *títeres*!", CIERRE], "voz_en": [1]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
