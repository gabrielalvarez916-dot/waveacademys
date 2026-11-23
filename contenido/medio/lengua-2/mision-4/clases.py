# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 4 · Qué pasó primero y qué pasó después: las 4 clases animadas.
Cuento de trabajo: Los tres chanchitos. Metáfora: el cuaderno viajero de Sofi. Regla de primeros años y vía fonológica.
Genera tools/medio/clase/lecciones/medio-leng2-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '96783c94-f2aa-4cca-be21-10657e8fec3a', 2: 'be978385-b39e-43a5-8cd5-020dd0b95b78', 3: 'fad0effe-582c-4304-b4f7-8fc28ba91d6c', 4: 'cc6679d8-8bb9-4692-a726-4af145ea120e'}
TIT = {1: 'Ordenar las escenas', 2: 'Palabras que ordenan: primero, luego, al final', 3: 'Resumir en tres oraciones', 4: 'Contar el cuento ordenado'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Se mezclaron las escenas!", "bajada": "El cuaderno de Sofi se cayó", "emoji": "📒", "titulo": "ORDENAR", "sub": "las escenas",
  "voz": ["¡Último momento: se mezclaron las escenas del cuento!", "El cuaderno de Sofi se cayó al piso.", "Hoy: *ordenar las escenas*."]},
 {"t": "historieta", "titulo": "LOS TRES CHANCHITOS", "vinetas": [{"emojis": ["🐷", "🏠"], "txt": "Hacen sus casas."}, {"emojis": ["🐺", "💨"], "txt": "El lobo sopla."}, {"emojis": ["🧱", "🐷"], "txt": "¡Se salvan!"}],
  "voz": ["Tres chanchitos hicieron casas de paja, madera y ladrillos.", "Vino el lobo y sopló dos casas.", "¡La de ladrillos no se cayó y se salvaron!"]},
 {"t": "orden", "titulo": "LAS ESCENAS", "etq1": "MEZCLADAS", "etq2": "EN ORDEN", "items": [{"txt": "Hacen casas", "emoji": "🏠"}, {"txt": "Sopla la paja", "emoji": "🌾"}, {"txt": "Sopla la madera", "emoji": "🪵"}, {"txt": "¡Se salvan!", "emoji": "🧱"}], "relato": [3, 0, 2, 1],
  "voz": ["Las escenas quedaron mezcladas.", "Se salvan, hacen casas, sopla la madera, sopla la paja.", "En orden: casas, paja, madera, ¡se salvan!"]},
 {"t": "vof", "afirmacion": "El cuento empieza cuando se salvan", "emoji": "🐷", "verdadero": False, "explicacion": "Eso es el final",
  "voz": ["¿Verdadero o falso? El cuento empieza cuando se salvan.", "Pensá: ¿qué pasa antes?", "¡*Falso*! Eso es el *final*."]},
 {"t": "pregunta", "pregunta": "¿Qué casa sopla primero el lobo?", "opciones": ["La de paja", "La de ladrillos"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Qué casa sopla primero el lobo?", "¡La de *paja*!"]},
 {"t": "resumen", "items": [["ESCENA", "una parte del cuento"], ["ORDEN", "primero, después, al final"], ["MEZCLADO", "no se entiende"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *escena* es una parte del cuento.", "Las escenas van *en orden*.", "Mezcladas, *no se entienden*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🌅", "lineas": ["Sofi cuenta su mañana.", "Usa palabras especiales.", "¡Ordenan lo que pasa!"], "titulo": "PALABRAS", "sub": "que ordenan",
  "voz": ["Sofi escribe su mañana en el cuaderno.", "Usa unas palabras especiales.", "¡Esas palabras *ordenan* lo que pasa!", "Hoy: *primero, luego, al final*."]},
 {"t": "linea", "titulo": "LA MAÑANA DE SOFI", "eventos": [{"fecha": "PRIMERO", "txt": "Me levanto", "emoji": "🛏️"}, {"fecha": "LUEGO", "txt": "Desayuno", "emoji": "🥛"}, {"fecha": "AL FINAL", "txt": "Voy a la escuela", "emoji": "🎒"}],
  "voz": ["*Primero*, me levanto.", "*Luego*, desayuno.", "*Al final*, voy a la escuela."]},
 {"t": "completa", "antes": "", "despues": ", el lobo sopla la casa.", "opciones": ["Luego", "Primero", "Al final"], "correcta": 0,
  "voz": ["Completá la oración del cuento.", "¿Primero, luego o al final?", "¡*Luego*! Es lo que sigue."]},
 {"t": "bloques", "titulo": "PALABRAS QUE ORDENAN", "items": [{"cab": "1️⃣", "txt": "Primero"}, {"cab": "2️⃣", "txt": "Luego, después"}, {"cab": "3️⃣", "txt": "Al final, por último"}],
  "voz": ["Estas son las palabras que ordenan.", "Para empezar: *primero*.", "Para seguir: *luego* o *después*.", "Para terminar: *al final* o *por último*."]},
 {"t": "pregunta", "pregunta": "¿Qué palabra va para lo último?", "opciones": ["Al final", "Primero"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Qué palabra usamos para lo último?", "¡*Al final*!"]},
 {"t": "resumen", "items": [["PRIMERO", "lo que pasa antes"], ["LUEGO", "lo que sigue"], ["AL FINAL", "lo último"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Primero*: lo que pasa antes.", "*Luego*: lo que sigue.", "*Al final*: lo último.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿De qué trata tu cuento?"}, {"yo": True, "txt": "¡Te lo cuento cortito!"}, {"yo": False, "txt": "¿En tres oraciones?"}], "titulo": "RESUMIR", "sub": "en tres oraciones",
  "voz": ["Tomi le pregunta a Sofi por el cuento.", "Sofi le dice: ¡te lo cuento cortito!", "¿En solo tres oraciones?", "Hoy: *resumir en tres oraciones*."]},
 {"t": "pasos", "titulo": "CÓMO RESUMO", "items": [{"txt": "Principio", "emoji": "🏠"}, {"txt": "Medio", "emoji": "🐺"}, {"txt": "Final", "emoji": "🧱"}],
  "voz": ["Un resumen tiene *tres partes*.", "Una oración para el *principio*.", "Una para el *medio*.", "Y una para el *final*."]},
 {"t": "clasificar", "cajas": [{"cab": "VA", "emoji": "✅"}, {"cab": "NO VA", "emoji": "❌"}], "fichas": [{"txt": "El lobo sopla", "caja": 0}, {"txt": "Se salvan", "caja": 0}, {"txt": "Bigotes del lobo", "caja": 1}, {"txt": "Paja amarilla", "caja": 1}],
  "voz": ["¿Qué va en el resumen?", "Que el lobo sopla y que se salvan: ¡*va*!", "Los bigotes y el color: *no va*."]},
 {"t": "pizarra", "titulo": "EL RESUMEN", "lineas": [{"txt": "1. Tres chanchitos hacen casas."}, {"txt": "2. El lobo sopla dos casas."}, {"txt": "3. Se salvan en la de ladrillos.", "color": "sol", "marca": "subraya"}],
  "voz": ["Tres chanchitos hacen casas.", "El lobo sopla dos casas.", "Se salvan en la de ladrillos. ¡Listo el resumen!"]},
 {"t": "quiz4", "pregunta": "¿Qué es resumir?", "opciones": ["Contar corto lo importante", "Contar todo", "Dibujar"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Qué es *resumir*?", "¡Contar *corto* lo importante!"]},
 {"t": "resumen", "items": [["RESUMIR", "contar corto"], ["TRES ORACIONES", "principio, medio y final"], ["IMPORTANTE", "lo que no se saca"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Resumir* es contar corto.", "Usamos *tres oraciones*.", "Solo lo *importante*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "¿Podés contar el cuento en orden, sin mirar?", "segundos": 8, "respuesta": "¡Casas, lobo, se salvan!", "emoji": "🎤", "titulo": "CONTAR", "sub": "el cuento ordenado",
  "voz": ["Desafío: contá el cuento en orden, sin mirar.", "¡Casas, lobo y se salvan!", "Hoy: *contar el cuento ordenado*."]},
 {"t": "fichas", "consigna": "Armá el principio del cuento", "fichas": ["Primero,", "los", "chanchitos", "hacen", "casas."], "desorden": [3, 0, 4, 1, 2], "traduccion": "¡Empezó el cuento!",
  "voz": ["Armamos la primera oración del cuento.", "Primero, los chanchitos hacen casas.", "¡Así empieza el cuento!"]},
 {"t": "corrige", "titulo": "REVISAMOS", "cambios": [{"antes": "Primero, se salvan.", "despues": "Primero, hacen sus casas.", "motivo": "el orden"}, {"antes": "Al final, hacen sus casas.", "despues": "Al final, se salvan.", "motivo": "el orden"}],
  "voz": ["Tomi contó el cuento. ¡Revisemos!", "Empezó por el final: lo arreglamos.", "Y terminó por el principio: ¡también!"]},
 {"t": "jefe", "jefe": {"nombre": "Lobo Feroz", "emoji": "🐺"}, "preguntas": [{"p": "¿Qué pasa primero?", "r": "Hacen sus casas"}, {"p": "¿Qué pasa luego?", "r": "El lobo sopla"}, {"p": "¿Qué pasa al final?", "r": "Se salvan"}],
  "voz": ["¡Apareció el *Lobo Feroz*!", "Le ganamos contando en orden.", "Primero: hacen sus casas.", "Luego: el lobo sopla.", "¡Al final: se salvan! ¡Ganamos!"]},
 {"t": "consejo", "titulo": "CONTÁ CON CALMA", "texto": "Usá primero, luego y al final", "emoji": "🐢",
  "voz": ["Truco: contá con calma y en *orden*."]},
 {"t": "resumen", "items": [["CONTAR", "en voz alta"], ["ORDENAR", "primero, luego, al final"], ["REVISAR", "que esté en orden"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Contamos* en voz alta.", "Usamos palabras que *ordenan*.", "Y *revisamos* que esté en orden.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m4-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 4 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
