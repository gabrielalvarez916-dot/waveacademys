# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 6 · Cuentos que ya conocemos: las 4 clases animadas.
Metáfora: la ronda de cuentos en la biblioteca. Cuentos tradicionales de dominio público. Regla de primeros años, vía fonológica y variedad del banco.
Genera tools/medio/clase/lecciones/medio-leng1-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '1962ca64-fce2-4c04-bbd5-8b675b0219d8', 2: '5d5e7f94-b421-4aa2-b311-016926bcce66', 3: 'be1314a5-4f11-40d0-b565-ce218a63417c', 4: '82507333-95b7-4acf-b04d-037bd70a0352'}
TIT = {1: 'Leer títulos de cuentos conocidos', 2: 'Ordenar las escenas del cuento', 3: 'Escribir los nombres de los personajes', 4: 'Leer una frase del cuento'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📚", "lineas": ["Hoy hay ronda de cuentos.", "La seño trae muchos libros.", "¿Cuál vamos a leer?"], "titulo": "CUENTOS", "sub": "que ya conocemos",
  "voz": ["¡Hoy hay *ronda de cuentos*!", "La seño trae muchos libros.", "¿Cuál vamos a leer?", "Hoy: *leer títulos de cuentos*."]},
 {"t": "zoom", "niveles": [{"emoji": "📕", "txt": "LA TAPA"}, {"emoji": "🔤", "txt": "EL TÍTULO"}, {"emoji": "👧", "txt": "CAPERUCITA ROJA"}],
  "voz": ["Miramos la *tapa* del libro.", "Arriba, con letras grandes, está el *título*.", "Dice: *Caperucita Roja*."]},
 {"t": "bloques", "titulo": "TÍTULOS DE CUENTOS", "items": [{"cab": "CAPERUCITA ROJA", "txt": "una nena y un lobo"}, {"cab": "LOS TRES CHANCHITOS", "txt": "tres casitas"}, {"cab": "EL PATITO FEO", "txt": "un patito distinto"}],
  "voz": ["Leemos más títulos.", "*Caperucita Roja*: una nena y un lobo.", "*Los tres chanchitos*: tres casitas.", "*El patito feo*: un patito distinto."]},
 {"t": "definicion", "palabra": "TÍTULO", "texto": "El nombre del cuento", "emoji": "🏷️",
  "voz": ["El *título* es el nombre del cuento.", "Nos dice de qué se trata."]},
 {"t": "pregunta", "pregunta": "¿Qué cuento tiene un lobo y una nena?", "opciones": ["El patito feo", "Caperucita Roja", "Los tres chanchitos"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en los títulos.", "¿Qué cuento tiene un lobo y una nena?", "¡*Caperucita Roja*!"]},
 {"t": "resumen", "items": [["TÍTULO", "el nombre del cuento"], ["TAPA", "ahí está el título"], ["BUSCAR", "leyendo títulos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *título* es el nombre del cuento.", "Está en la *tapa*.", "Leyendo títulos *buscamos* cuentos.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué pasa primero en Caperucita?", "segundos": 6, "respuesta": "¡SALE DE SU CASA!", "emoji": "🏠", "titulo": "ORDENAR", "sub": "las escenas",
  "voz": ["Desafío: ¿qué pasa primero en Caperucita?", "¡Sale de su *casa*!", "Hoy: *ordenar las escenas del cuento*."]},
 {"t": "orden", "titulo": "CAPERUCITA ROJA", "items": [{"txt": "Sale de su casa", "emoji": "🏠"}, {"txt": "Se encuentra al lobo", "emoji": "🐺"}, {"txt": "El lobo corre", "emoji": "💨"}, {"txt": "El cazador las salva", "emoji": "🪓"}], "relato": [3, 1, 0, 2],
  "voz": ["¡Se mezclaron las escenas del cuento!", "Las ponemos en *orden*.", "Casa, lobo, corre y el cazador las salva."]},
 {"t": "linea", "titulo": "LAS PARTES DEL CUENTO", "eventos": [{"fecha": "1", "txt": "PRINCIPIO", "emoji": "🏠"}, {"fecha": "2", "txt": "MEDIO", "emoji": "🐺"}, {"fecha": "3", "txt": "FINAL", "emoji": "🎉"}],
  "voz": ["*Principio*: Caperucita sale de su casa.", "*Medio*: aparece el lobo.", "*Final*: el cazador las salva."]},
 {"t": "pregunta", "pregunta": "¿Qué pasa al final?", "opciones": ["Sale de su casa", "El cazador las salva", "Se encuentra al lobo"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el final.", "¿Qué pasa al final del cuento?", "¡El cazador *las salva*!"]},
 {"t": "consejo", "titulo": "PREGUNTÁ", "texto": "¿Qué pasó primero? ¿Y después?", "emoji": "❓",
  "voz": ["Truco: preguntá *qué pasó primero* y qué después."]},
 {"t": "resumen", "items": [["PRINCIPIO", "cómo empieza"], ["MEDIO", "el problema"], ["FINAL", "cómo termina"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *principio*: cómo empieza.", "El *medio*: el problema.", "El *final*: cómo termina.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Quiénes están en Caperucita?"}, {"yo": True, "txt": "¡Te los escribo!"}, {"yo": False, "txt": "¡Dale!"}], "titulo": "PERSONAJES", "sub": "sus nombres",
  "voz": ["Tomi le escribe a Sofi.", "¿Quiénes están en Caperucita?", "¡Sofi se los escribe!", "Hoy: *escribir los nombres de los personajes*."]},
 {"t": "matriz", "titulo": "LOS PERSONAJES", "celdas": [{"cab": "CAPERUCITA", "txt": "la nena 👧"}, {"cab": "LOBO", "txt": "el malo 🐺"}, {"cab": "ABUELA", "txt": "está en la cama 👵"}, {"cab": "CAZADOR", "txt": "las salva 🪓"}],
  "voz": ["Los *personajes* hacen cosas en el cuento.", "*Caperucita*, la nena.", "El *lobo*, el malo.", "La *abuela*, en la cama.", "Y el *cazador*, que las salva."]},
 {"t": "fichas", "fichas": ["L", "O", "B", "O"], "grande": "LOBO", "etiqueta": "LO · BO",
  "voz": ["Sofi dice despacio: lll… o… bo.", "Escribe y se forma *LOBO*.", "¡Dos sílabas: LO, BO!"]},
 {"t": "pregunta", "pregunta": "¿Quién es un personaje de Caperucita?", "opciones": ["El patito", "El lobo", "El chanchito"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el cuento.", "¿Quién está en Caperucita?", "¡El *lobo*!"]},
 {"t": "consejo", "titulo": "DECILO LENTO", "texto": "Decí el nombre despacio y escribí cada sonido", "emoji": "🐢",
  "voz": ["Truco: decí el nombre *despacio* y escribí cada sonido."]},
 {"t": "resumen", "items": [["PERSONAJE", "hace cosas en el cuento"], ["NOMBRES", "LOBO, ABUELA"], ["ESCRIBIR", "sílaba por sílaba"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *personaje* hace cosas en el cuento.", "*Lobo*, *abuela*, *cazador*.", "Los escribimos *sílaba por sílaba*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "TEATRO DEL GRADO", "titular": "¡ACTUAMOS CAPERUCITA!", "bajada": "Hay que leer con emoción", "emoji": "🎭", "titulo": "UNA FRASE", "sub": "del cuento",
  "voz": ["¡El grado va a actuar *Caperucita*!", "Hay que leer *con emoción*.", "Hoy: *leer una frase del cuento*."]},
 {"t": "dialogo", "personas": [{"nombre": "CAPERUCITA", "emoji": "👧"}, {"nombre": "LOBO", "emoji": "🐺"}], "lineas": [{"quien": 0, "txt": "¡QUÉ OJOS TAN GRANDES!"}, {"quien": 1, "txt": "¡PARA VERTE MEJOR!"}, {"quien": 0, "txt": "¡QUÉ BOCA TAN GRANDE!"}],
  "voz": ["Caperucita dice: ¡qué ojos tan grandes!", "El lobo contesta: ¡para verte mejor!", "Caperucita: ¡qué boca tan grande!"]},
 {"t": "texto", "oracion": "¡QUÉ OJOS TAN GRANDES!", "marcas": [{"desde": 0, "hasta": 0, "etiqueta": "¡ ABRE", "color": "sol"}, {"desde": 3, "hasta": 3, "etiqueta": "! CIERRA", "color": "sol"}],
  "voz": ["Mirá los signos de la frase.", "Este *abre* la emoción.", "Y este la *cierra*."]},
 {"t": "pregunta", "pregunta": "¿Quién dice ¡PARA VERTE MEJOR!?", "opciones": ["La abuela", "El lobo", "Caperucita"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el cuento.", "¿Quién dice: para verte mejor?", "¡El *lobo*!"]},
 {"t": "consejo", "titulo": "MIRÁ LOS SIGNOS", "texto": "Con ¡ ! se lee con emoción", "emoji": "😮",
  "voz": ["Truco: si ves esos signos, leé *con emoción*."]},
 {"t": "resumen", "items": [["FRASE", "lo que dice un personaje"], ["¡ !", "con emoción"], ["LEER", "palabra por palabra"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *frase* es lo que dice un personaje.", "Con estos signos leemos *con emoción*.", "Leemos *palabra por palabra*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m6-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 6 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
