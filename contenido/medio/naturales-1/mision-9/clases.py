# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 9 · Luz, sombras y sonidos: las 4 clases animadas.
Metáfora: el teatro de sombras y la banda del grado. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 9
TIT = {1: 'Objetos que dejan pasar la luz', 2: 'Sombras largas y cortas', 3: 'El sonido y las vibraciones', 4: 'Instrumentos y sonidos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Se cortó la luz en casa!"}, {"yo": True, "txt": "¡USÁ UNA LINTERNA!"}, {"yo": False, "txt": "¡Ahora veo todo!"}], "titulo": "LA LUZ", "sub": "¿pasa o no pasa?",
  "voz": ["Tomi le escribe a Sofi.", "¡Se cortó la luz en casa!", "Sofi le dice: usá una *linterna*.", "Hoy: *objetos que dejan pasar la luz*."]},
 {"t": "matriz", "titulo": "¿PASA LA LUZ?", "celdas": [{"cab": "🪟 VIDRIO", "txt": "PASA"}, {"cab": "📄 PAPEL FINO", "txt": "PASA UN POCO"}, {"cab": "🚪 MADERA", "txt": "NO PASA"}, {"cab": "📕 LIBRO", "txt": "NO PASA"}],
  "voz": ["Alumbramos cosas con la linterna.", "Por el *vidrio*, pasa.", "Por el *papel fino*, pasa un poco.", "Por la *madera*, no pasa.", "Por el *libro*, tampoco."]},
 {"t": "zoom", "niveles": [{"emoji": "🏠", "txt": "LA CASA"}, {"emoji": "🪟", "txt": "LA VENTANA"}, {"emoji": "☀️", "txt": "ENTRA LA LUZ"}],
  "voz": ["Miramos una *casa*.", "Nos acercamos a la *ventana*.", "¡Por el vidrio entra la *luz* del sol!"]},
 {"t": "pregunta", "pregunta": "¿Por cuál pasa la luz?", "opciones": ["LIBRO", "VIDRIO", "PARED"], "correcta": 1,
  "voz": ["Ahora vos. Libro, vidrio, pared.", "¿Por cuál pasa la luz?", "¡Por el *vidrio*!"]},
 {"t": "consejo", "titulo": "CUIDÁ LOS OJOS", "texto": "No apuntes la linterna a los ojos", "emoji": "🔦",
  "voz": ["Importante: no apuntes la linterna a los *ojos*."]},
 {"t": "resumen", "items": [["LUZ", "sol, lámpara, linterna"], ["PASA", "vidrio"], ["NO PASA", "madera, libro"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *luz* viene del sol y las lámparas.", "Por el vidrio *pasa*.", "Por la madera *no pasa*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎭", "lineas": ["Sofi arma un teatro de sombras.", "Pone la mano frente a la linterna.", "¡Aparece un perrito en la pared!"], "titulo": "SOMBRAS", "sub": "largas y cortas",
  "voz": ["Sofi arma un *teatro de sombras*.", "Pone la mano frente a la linterna.", "¡Aparece un *perrito* en la pared!", "Hoy: *sombras largas y cortas*."]},
 {"t": "linea", "titulo": "MI SOMBRA EN EL DÍA", "eventos": [{"fecha": "MAÑANA", "txt": "LARGA", "emoji": "🌅"}, {"fecha": "MEDIODÍA", "txt": "CORTA", "emoji": "☀️"}, {"fecha": "TARDE", "txt": "LARGA", "emoji": "🌇"}],
  "voz": ["A la *mañana*, mi sombra es larga.", "Al *mediodía*, es cortita.", "A la *tarde*, otra vez larga."]},
 {"t": "comparar", "a": {"cab": "SOL BAJO", "texto": "SOMBRA LARGA", "emoji": "🌇"}, "b": {"cab": "SOL ALTO", "texto": "SOMBRA CORTA", "emoji": "☀️"}, "signo": "vs",
  "voz": ["Con el sol *bajo*, la sombra es larga.", "Con el sol *alto*, la sombra es corta.", "¡El sol decide el largo!"]},
 {"t": "pregunta", "pregunta": "¿Cómo es tu sombra al mediodía?", "opciones": ["LARGA", "CORTA", "NO HAY"], "correcta": 1,
  "voz": ["Ahora vos. Es la hora del almuerzo.", "¿Cómo es tu sombra?", "¡*Corta*! El sol está arriba."]},
 {"t": "consejo", "titulo": "SIN LUZ NO HAY", "texto": "La sombra necesita luz", "emoji": "💡",
  "voz": ["Truco: *sin luz*, no hay sombra."]},
 {"t": "resumen", "items": [["SOMBRA", "algo tapa la luz"], ["LARGA", "mañana y tarde"], ["CORTA", "mediodía"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *sombra* aparece si algo tapa la luz.", "Es *larga* a la mañana y a la tarde.", "Es *corta* al mediodía.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Tocá tu garganta y hablá. ¿Qué sentís?", "segundos": 6, "respuesta": "¡VIBRA!", "emoji": "🗣️", "titulo": "EL SONIDO", "sub": "y las vibraciones",
  "voz": ["Desafío: tocá tu garganta y hablá.", "¿Qué sentís? ¡*Vibra*!", "Hoy: *el sonido y las vibraciones*."]},
 {"t": "flujo", "titulo": "CÓMO LLEGA EL SONIDO", "items": ["ALGO VIBRA", "VIAJA POR EL AIRE", "LLEGA A MI OREJA"],
  "voz": ["Primero, algo *vibra*.", "El sonido *viaja* por el aire.", "Y llega a mi *oreja*."]},
 {"t": "experimento", "titulo": "¿SUENA EL ELÁSTICO?", "variable": "LA VIBRACIÓN", "a": {"cab": "QUIETO", "emojis": ["➖", "🤫"], "txt": "No lo toco", "res": "NO SUENA"}, "b": {"cab": "LO TOCO", "emojis": ["〰️", "🎶"], "txt": "Vibra", "res": "¡SUENA!"},
  "voz": ["Sofi estira un *elástico*.", "Quieto, no suena.", "¡Lo toca, *vibra* y suena!"]},
 {"t": "pregunta", "pregunta": "¿Qué hace sonar a las cosas?", "opciones": ["LA LUZ", "LA VIBRACIÓN", "EL COLOR"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el elástico.", "¿Qué hace que suene?", "¡La *vibración*!"]},
 {"t": "consejo", "titulo": "CUIDÁ LAS OREJAS", "texto": "Los sonidos muy fuertes lastiman", "emoji": "👂",
  "voz": ["Importante: los sonidos muy *fuertes* lastiman."]},
 {"t": "resumen", "items": [["VIBRAR", "moverse rápido"], ["VIAJA", "por el aire"], ["OÍR", "con las orejas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El sonido nace cuando algo *vibra*.", "*Viaja* por el aire.", "Y lo *oímos* con las orejas.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡EL GRADO ARMA UNA BANDA!", "bajada": "Cada uno trae un instrumento", "emoji": "🥁", "titulo": "INSTRUMENTOS", "sub": "y sonidos",
  "voz": ["¡Último momento! El grado arma una *banda*.", "Cada uno trae un instrumento.", "Hoy: *instrumentos y sonidos*."]},
 {"t": "bloques", "titulo": "CÓMO SE TOCAN", "items": [{"cab": "🥁 TAMBOR", "txt": "SE GOLPEA"}, {"cab": "🪇 MARACAS", "txt": "SE SACUDEN"}, {"cab": "🪈 FLAUTA", "txt": "SE SOPLA"}, {"cab": "🎸 GUITARRA", "txt": "CUERDAS"}],
  "voz": ["Cada instrumento se toca distinto.", "El tambor se *golpea*.", "Las maracas se *sacuden*.", "La flauta se *sopla*.", "La guitarra se toca con las *cuerdas*."]},
 {"t": "comparar", "a": {"cab": "GOLPE FUERTE", "texto": "SUENA FUERTE", "emoji": "🔊"}, "b": {"cab": "GOLPE SUAVE", "texto": "SUENA SUAVE", "emoji": "🔈"}, "signo": "vs",
  "voz": ["Si golpeás *fuerte*, suena fuerte.", "Si golpeás *suave*, suena suave.", "¡Vos elegís cómo suena!"]},
 {"t": "pregunta", "pregunta": "¿Cómo se toca la flauta?", "opciones": ["SE GOLPEA", "SE SOPLA", "SE SACUDE"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la flauta.", "¿Cómo se toca?", "¡Se *sopla*!"]},
 {"t": "consejo", "titulo": "EMPEZÁ SUAVE", "texto": "Después probá más fuerte", "emoji": "🎵",
  "voz": ["Truco: empezá tocando *suave*."]},
 {"t": "resumen", "items": [["GOLPEAR", "tambor"], ["SOPLAR", "flauta"], ["CUERDAS", "guitarra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Unos se *golpean*.", "Otros se *soplan*.", "Y otros tienen *cuerdas*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
