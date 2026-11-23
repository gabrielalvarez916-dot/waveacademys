# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 6 · My Body: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: las canciones de Tomi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 6
TIT = {1: 'Head, shoulders, knees and toes', 2: 'Eyes, nose, mouth and ears', 3: 'Touch your nose!', 4: 'Hands and feet: action songs'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🎵", "lineas": ["Tomi escucha una canción.", "La canción nombra el cuerpo.", "¡Tomi se toca cada parte!"], "titulo": "MY BODY", "sub": "cabeza, hombros, rodillas y pies",
  "voz": ["Tomi escucha una *canción*.", "La canción nombra partes del *cuerpo*.", "¡Y Tomi se toca cada una!", "Hoy: *el cuerpo en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "HEAD", "emoji": "🙂", "trad": "cabeza", "pron": "jed"}, {"palabra": "SHOULDERS", "emoji": "🤷", "trad": "hombros", "pron": "shóulders"}, {"palabra": "KNEES", "emoji": "🦵", "trad": "rodillas", "pron": "nís"}, {"palabra": "TOES", "emoji": "🦶", "trad": "dedos del pie", "pron": "tóus"}],
  "voz": ["Head!", "Shoulders!", "Knees!", "Toes!"], "voz_en": [0, 1, 2, 3]},
 {"t": "partes", "emoji": "🧍", "titulo": "MY BODY", "partes": [{"txt": "HEAD", "x": 0.0, "y": -0.85}, {"txt": "SHOULDERS", "x": 0.65, "y": -0.45}, {"txt": "KNEES", "x": -0.6, "y": 0.35}, {"txt": "TOES", "x": 0.55, "y": 0.85}],
  "voz": ["Miramos el cuerpo de arriba a abajo.", "Head!", "Shoulders!", "Knees!", "Toes!"], "voz_en": [1, 2, 3, 4]},
 {"t": "pregunta", "pregunta": "¿Cómo se dice cabeza?", "opciones": ["HEAD", "KNEES", "TOES"], "correcta": 0,
  "voz": ["Ahora vos. Tocate la cabeza.", "¿Cómo se dice en inglés?", "Head!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "DE ARRIBA A ABAJO", "texto": "Empezá por la cabeza y bajá hasta los pies", "emoji": "⬇️",
  "voz": ["Truco: empezá por la *cabeza* y bajá."]},
 {"t": "resumen", "items": [["HEAD", "cabeza"], ["SHOULDERS", "hombros"], ["KNEES / TOES", "rodillas y dedos del pie"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Head, shoulders, knees and toes!", "Cabeza, hombros, rodillas y *pies*.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "chat", "contacto": SOFI, "mensajes": [{"yo": False, "txt": "🤳 LOOK! MY FACE!"}, {"yo": True, "txt": "¡Jaja, qué linda!"}, {"yo": False, "txt": "EYES, NOSE, MOUTH!"}], "titulo": "MY FACE", "sub": "ojos, nariz, boca y orejas",
  "voz": ["Sofi le manda una selfie a Tomi.", "Look! My face!", "Le muestra su *cara*.", "Hoy: *la cara en inglés*."], "voz_en": [1]},
 {"t": "vocab", "items": [{"palabra": "EYES", "emoji": "👀", "trad": "ojos", "pron": "áis"}, {"palabra": "NOSE", "emoji": "👃", "trad": "nariz", "pron": "nóus"}, {"palabra": "MOUTH", "emoji": "👄", "trad": "boca", "pron": "máuz"}, {"palabra": "EARS", "emoji": "👂", "trad": "orejas", "pron": "íars"}],
  "voz": ["Eyes!", "Nose!", "Mouth!", "Ears!"], "voz_en": [0, 1, 2, 3]},
 {"t": "matriz", "titulo": "¿PARA QUÉ SIRVEN?", "celdas": [{"cab": "👀 EYES", "txt": "VER"}, {"cab": "👂 EARS", "txt": "OÍR"}, {"cab": "👃 NOSE", "txt": "OLER"}, {"cab": "👄 MOUTH", "txt": "COMER Y HABLAR"}],
  "voz": ["Cada parte de la cara sirve para algo.", "Con los ojos *vemos*.", "Con las orejas *oímos*.", "Con la nariz *olemos*.", "Con la boca *comemos* y hablamos."]},
 {"t": "pregunta", "pregunta": "Sofi huele una flor. ¿Qué usa?", "opciones": ["NOSE", "EARS", "EYES"], "correcta": 0,
  "voz": ["Ahora vos. Sofi huele una flor.", "¿Qué parte usa en inglés?", "Nose!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "SEÑALÁ", "texto": "Señalá cada parte de tu cara", "emoji": "👉",
  "voz": ["Truco: *señalá* cada parte de tu cara."]},
 {"t": "resumen", "items": [["EYES", "ojos"], ["NOSE", "nariz"], ["MOUTH / EARS", "boca y orejas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Eyes, nose, mouth and ears!", "Ojos, nariz, boca y *orejas*.", CIERRE], "voz_en": [1]},
]
N3 = [
 {"t": "reto", "texto": "Escuchá y hacé: TOUCH YOUR NOSE!", "segundos": 5, "respuesta": "¡TE TOCASTE LA NARIZ!", "emoji": "👃", "titulo": "TOUCH YOUR NOSE!", "sub": "escuchar y tocar",
  "voz": ["Desafío: escuchá y hacé.", "Touch your nose!", "Hoy: *escuchar y tocar*."], "voz_en": [1]},
 {"t": "flujo", "titulo": "TOUCH YOUR…", "items": ["NOSE 👃", "EARS 👂", "HEAD 🙂", "KNEES 🦵"],
  "voz": ["Touch your nose!", "Touch your ears!", "Touch your head!", "Touch your knees!"], "voz_en": [0, 1, 2, 3]},
 {"t": "ciclo", "titulo": "EL JUEGO", "items": ["ESCUCHO", "TOCO", "¡MUY BIEN!"],
  "voz": ["Así se juega.", "Primero *escucho* la orden.", "Después *toco* la parte del cuerpo.", "¡Y otra vez!"]},
 {"t": "pregunta", "pregunta": "TOUCH YOUR HEAD. ¿Qué tocás?", "opciones": ["LA CABEZA", "LA NARIZ", "LOS PIES"], "correcta": 0,
  "voz": ["Ahora vos. Escuchá la orden.", "Touch your head!", "¡La *cabeza*!"], "voz_en": [1]},
 {"t": "consejo", "titulo": "ESCUCHÁ", "texto": "Esperá a escuchar la parte del cuerpo", "emoji": "👂",
  "voz": ["Truco: *esperá* a escuchar la parte del cuerpo."]},
 {"t": "resumen", "items": [["TOUCH", "tocar"], ["YOUR", "tu"], ["JUEGO", "escuchar y hacer"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Touch your nose!", "Escuchamos y *tocamos*.", CIERRE], "voz_en": [1]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡FIESTA DE BAILE EN INGLÉS!", "bajada": "Con manos y pies", "emoji": "💃", "titulo": "HANDS AND FEET", "sub": "manos y pies",
  "voz": ["¡Último momento! Hay fiesta de *baile*.", "¡Y bailamos en inglés!", "Hoy: *manos y pies en inglés*."]},
 {"t": "vocab", "items": [{"palabra": "HANDS", "emoji": "👐", "trad": "manos", "pron": "jands"}, {"palabra": "FEET", "emoji": "🦶", "trad": "pies", "pron": "fit"}, {"palabra": "CLAP", "emoji": "👏", "trad": "aplaudir", "pron": "clap"}, {"palabra": "JUMP", "emoji": "🤸", "trad": "saltar", "pron": "yamp"}],
  "voz": ["Hands!", "Feet!", "Clap!", "Jump!"], "voz_en": [0, 1, 2, 3]},
 {"t": "antesdespues", "antes": {"cab": "HANDS", "emoji": "👏", "texto": "Aplaudimos"}, "despues": {"cab": "FEET", "emoji": "🦶", "texto": "Zapateamos"},
  "voz": ["Clap your hands!", "Stamp your feet!"], "voz_en": [0, 1]},
 {"t": "pregunta", "pregunta": "La canción dice JUMP. ¿Qué hacés?", "opciones": ["SALTO", "APLAUDO", "ME SIENTO"], "correcta": 0,
  "voz": ["Ahora vos. Escuchá la canción.", "Jump!", "¡*Saltás*!"], "voz_en": [1]},
 {"t": "consejo", "titulo": "CON RITMO", "texto": "Seguí el ritmo de la música", "emoji": "🎶",
  "voz": ["Truco: seguí el *ritmo* de la música."]},
 {"t": "resumen", "items": [["HANDS", "manos"], ["FEET", "pies"], ["CLAP / JUMP", "aplaudir y saltar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Clap your hands! Stamp your feet!", "¡Y jump, a *saltar*!", CIERRE], "voz_en": [1]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
