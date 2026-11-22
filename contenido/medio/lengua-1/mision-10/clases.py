# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 10 · Rimas y poemas para leer: las 4 clases animadas.
Metáfora: la caja de música (las rimas suenan igual al final). Regla de primeros años, vía fonológica y variedad del banco.
Poemas originales de la misión ("El sapo Pepe", "La luna") y la rima tradicional "Sana, sana".
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-leng1-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'eee219b3-9188-4e94-be06-223054ed5a57'
TIT = {1: 'Leer rimas conocidas', 2: 'Encontrar palabras que riman', 3: 'Leer un poema en voz alta', 4: 'Copiar mi verso preferido'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Me caí y me dolió!"}, {"yo": True, "txt": "SANA, SANA, COLITA DE RANA"}, {"yo": False, "txt": "¡Ja! ¡Ya estoy mejor!"}], "titulo": "RIMAS", "sub": "que ya conocés",
  "voz": ["Tomi se cayó y le escribe a Sofi.", "¡Me caí y me dolió!", "Sofi le manda una *rima*.", "Hoy: *rimas que ya conocés*."]},
 {"t": "parrafo", "titulo": "SANA, SANA", "lineas": ["Sana, sana,", "colita de rana."], "marcas": [{"linea": 0, "pos": "fin", "txt": "SANA"}, {"linea": 1, "pos": "fin", "txt": "RANA"}],
  "voz": ["Leemos: sana, sana, colita de rana.", "El primer renglón termina en *sana*.", "El segundo termina en *rana*: ¡suenan igual!"]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "MAMÁ", "emoji": "👩"}], "lineas": [{"quien": 0, "txt": "¡ME DUELE EL DEDO!"}, {"quien": 1, "txt": "SANA, SANA,"}, {"quien": 1, "txt": "COLITA DE RANA."}],
  "voz": ["Sofi dice: ¡me duele el dedo!", "Mamá contesta: sana, sana,", "colita de *rana*."]},
 {"t": "consejo", "titulo": "CON PALMAS", "texto": "Marcá el ritmo con las manos", "emoji": "👏",
  "voz": ["Truco: decí la rima con *palmas*."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra suena igual que SANA?", "opciones": ["SOPA", "RANA", "SOL"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá el final: sa… na.", "¿Qué palabra suena igual?", "¡*RANA*! Sana y rana *riman*."]},
 {"t": "resumen", "items": [["RIMA", "suena igual al final"], ["SANA · RANA", "riman"], ["RITMO", "con palmas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *rima* suena igual al final.", "*Sana* y *rana* riman.", "La decimos con *palmas*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎵", "lineas": ["Sofi abre una caja de música.", "Salen palabras que suenan igual.", "¡Gato y pato!"], "titulo": "PALABRAS", "sub": "que riman",
  "voz": ["Sofi abre una *caja de música*.", "Salen palabras que suenan igual.", "¡*Gato* y *pato*!", "Hoy: *buscar palabras que riman*."]},
 {"t": "matriz", "titulo": "PAREJAS QUE RIMAN", "celdas": [{"cab": "🐱", "txt": "GATO · PATO"}, {"cab": "🌙", "txt": "LUNA · CUNA"}, {"cab": "🦭", "txt": "FOCA · BOCA"}, {"cab": "🍓", "txt": "MESA · FRESA"}],
  "voz": ["Juntamos las parejas que *riman*.", "*Gato* y *pato*.", "*Luna* y *cuna*.", "*Foca* y *boca*.", "*Mesa* y *fresa*."]},
 {"t": "comparar", "a": {"cab": "RIMAN", "texto": "GATO · PATO", "emoji": "🎵"}, "b": {"cab": "NO RIMAN", "texto": "GATO · GOMA", "emoji": "🙉"}, "signo": "vs",
  "voz": ["*Gato* y *pato* terminan igual: riman.", "*Gato* y *goma* empiezan igual.", "Pero el final es distinto: ¡no riman!"]},
 {"t": "pregunta", "pregunta": "¿Qué palabra rima con FOCA?", "opciones": ["FOTO", "BOCA", "FIDEO"], "correcta": 1,
  "voz": ["Ahora vos. Escuchá el final de foca.", "¿Qué palabra termina igual?", "¡*BOCA*! Foca y boca."]},
 {"t": "consejo", "titulo": "ESCUCHÁ EL FINAL", "texto": "La rima está al final", "emoji": "👂",
  "voz": ["Truco: escuchá cómo *termina* la palabra."]},
 {"t": "resumen", "items": [["FINAL", "suena igual"], ["PAREJAS", "gato · pato"], ["OJO", "empezar igual no alcanza"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Riman si el *final* suena igual.", "*Gato* y *pato* son pareja.", "Empezar igual *no alcanza*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué sale de noche en el cielo?", "segundos": 6, "respuesta": "¡LA LUNA!", "emoji": "🌙", "titulo": "UN POEMA", "sub": "en voz alta",
  "voz": ["Desafío: ¿qué sale de noche en el cielo?", "¡La *LUNA*!", "Hoy: *leer un poema en voz alta*."]},
 {"t": "parrafo", "titulo": "LA LUNA", "lineas": ["La luna de noche", "sale a pasear,", "la mira la foca", "desde el mar."], "marcas": [{"linea": 1, "pos": "fin", "txt": "PASEAR"}, {"linea": 3, "pos": "fin", "txt": "MAR"}],
  "voz": ["Leemos el poema de la luna.", "*Pasear* está al final de un renglón.", "*Mar* también: ¡riman!"]},
 {"t": "bloques", "titulo": "LOS VERSOS", "items": [{"cab": "1", "txt": "LA LUNA DE NOCHE"}, {"cab": "2", "txt": "SALE A PASEAR"}, {"cab": "3", "txt": "LA MIRA LA FOCA"}, {"cab": "4", "txt": "DESDE EL MAR"}],
  "voz": ["Cada renglón es un *verso*.", "Verso uno: la luna de noche.", "Verso dos: sale a pasear.", "Verso tres: la mira la foca.", "Verso cuatro: desde el mar."]},
 {"t": "consejo", "titulo": "UNA PAUSA", "texto": "Al final de cada verso, parás un ratito", "emoji": "⏸️",
  "voz": ["Truco: después de cada verso, una *pausa*."]},
 {"t": "pregunta", "pregunta": "¿Cuántos versos tiene el poema?", "opciones": ["2", "4", "6"], "correcta": 1,
  "voz": ["Ahora vos. Contá los renglones.", "¿Cuántos versos tiene?", "¡*4 versos*!"]},
 {"t": "resumen", "items": [["POEMA", "renglones cortos"], ["VERSO", "cada renglón"], ["LEER", "con pausas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *poema* tiene renglones cortos.", "Cada renglón es un *verso*.", "Lo leemos con *pausas*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SOFI ELIGE SU VERSO!", "bajada": "Lo va a copiar en su cuaderno", "emoji": "📓", "titulo": "COPIAR", "sub": "mi verso preferido",
  "voz": ["¡Último momento! Sofi elige su *verso*.", "Lo va a copiar en su cuaderno.", "Hoy: *copiar mi verso preferido*."]},
 {"t": "flujo", "titulo": "CÓMO COPIO", "items": ["ELIJO", "MIRO", "ESCRIBO", "COMPARO"],
  "voz": ["Primero, *elijo* el verso.", "Después, *miro* una palabra.", "La *escribo* en el cuaderno.", "Al final, *comparo* con el poema."]},
 {"t": "corrige", "titulo": "REVISO LA COPIA", "cambios": [{"antes": "LA LUNA DE NOCE", "despues": "LA LUNA DE NOCHE", "motivo": "faltaba una letra"}, {"antes": "SEPONE UN GORRO", "despues": "SE PONE UN GORRO", "motivo": "espacio"}],
  "voz": ["Sofi compara su copia con el poema.", "En *noche* faltaba una letra.", "Y separa con un *espacio*."]},
 {"t": "pregunta", "pregunta": "¿Cuál está bien copiado?", "opciones": ["EL SAPOPEPE", "EL SAPO PEPE", "EL SAPO PEPA"], "correcta": 1,
  "voz": ["Ahora vos. El verso es: el sapo Pepe.", "¿Cuál está igual?", "¡El del *medio*!"]},
 {"t": "consejo", "titulo": "CON EL DEDO", "texto": "Seguí cada palabra con el dedo", "emoji": "☝️",
  "voz": ["Truco: seguí cada palabra con el *dedo*."]},
 {"t": "resumen", "items": [["ELEGIR", "el que más te gusta"], ["COPIAR", "palabra por palabra"], ["REVISAR", "comparar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Elegimos* el verso preferido.", "Copiamos *palabra por palabra*.", "Y *comparamos* con el poema.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m10-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": 10, "nivel": n}, "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 10 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
