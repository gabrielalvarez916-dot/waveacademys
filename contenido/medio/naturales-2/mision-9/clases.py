# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 9 · El suelo y las rocas: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (cava en la huerta con su lupa).
Genera tools/medio/clase/lecciones/medio-nat2-m9-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '9c48bd93-0b36-41b2-900c-2581835cc1c2', 2: '46f2368e-e5fe-43c6-ab58-bfdfbc7caf7b', 3: '490069b6-3784-4fa2-ba89-55ea73882e7d', 4: '6471639d-b400-40bf-b721-172b0b8dd31e'}
TIT = {1: 'Qué tiene el suelo', 2: 'Rocas de distintos tipos', 3: 'Seres vivos del suelo', 4: 'Suelos para sembrar'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."

N1 = [
 {"t": "historieta", "titulo": "TOMI EN LA HUERTA", "vinetas": [{"emojis": ["🧑‍🔬", "🪴"], "txt": "Tomi junta tierra"}, {"emojis": ["🔍", "🪨"], "txt": "La mira con la lupa"}, {"emojis": ["🍂", "💧"], "txt": "¡Hay de todo!"}],
  "voz": ["Tomi junta un poco de *tierra*.", "La mira con la *lupa*.", "¡Hay de todo! Hoy: *qué tiene el suelo*."]},
 {"t": "zoom", "niveles": [{"emoji": "🪴", "txt": "UN PUÑADO DE TIERRA"}, {"emoji": "🔍", "txt": "CON LUPA"}, {"emoji": "🪨", "txt": "¡PIEDRITAS, HOJITAS Y AGUA!"}],
  "voz": ["Miramos un puñado de *tierra*.", "Más cerca, con la *lupa*.", "¡Piedritas, hojitas y agua!"]},
 {"t": "experimento", "titulo": "EL FRASCO DE TOMI", "variable": "LO QUE PESA", "a": {"cab": "ABAJO", "emojis": ["🪨", "🪨"], "txt": "Lo pesado", "res": "PIEDRITAS"}, "b": {"cab": "ARRIBA", "emojis": ["🍂", "🍃"], "txt": "Lo liviano", "res": "HOJITAS"},
  "voz": ["Tierra y agua en un *frasco*.", "Abajo quedan las *piedritas*.", "Arriba flotan las *hojitas*."]},
 {"t": "pregunta", "pregunta": "¿El suelo tiene agua y aire?", "opciones": ["SÍ", "NO"], "correcta": 0,
  "voz": ["Ahora vos: ¿el suelo tiene agua y aire?", "Pensá en la lupa.", "¡*Sí*! Entre las piedritas."]},
 {"t": "consejo", "titulo": "MANOS LIMPIAS", "texto": "Después de tocar tierra, lavate", "emoji": "🧼",
  "voz": ["Truco: después de tocar tierra, *lavate* las manos."]},
 {"t": "resumen", "items": [["SUELO", "tierra que pisamos"], ["TIENE", "piedritas y hojas"], ["FRASCO", "se separa en capas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *suelo* es la tierra que pisamos.", "*Tiene* piedritas, hojas, agua y aire.", "En el *frasco*, se separa en capas.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "EXPLORACIÓN", "titular": "¡Tomi junta rocas!", "bajada": "Hay duras y blandas", "emoji": "🪨", "titulo": "LAS ROCAS", "sub": "de distintos tipos",
  "voz": ["¡Noticia: Tomi junta *rocas*!", "Hay duras y *blandas*.", "Hoy: *rocas de distintos tipos*."]},
 {"t": "mazo", "titulo": "MI COLECCIÓN", "items": [{"frente": "🪨", "dorso": "GRANITO: MUY DURO", "emoji": "🪨"}, {"frente": "🖍️", "dorso": "TIZA: BLANDA", "emoji": "🖍️"}, {"frente": "⚪", "dorso": "CANTO RODADO: REDONDO", "emoji": "⚪"}],
  "voz": ["El *granito*: muy duro.", "La *tiza*: blanda, se raya.", "El *canto rodado*: redondo, del río."]},
 {"t": "versus", "titulo": "DURA O BLANDA", "a": {"txt": "DURA", "emoji": "🪨", "datos": ["no se raya", "granito"]}, "b": {"txt": "BLANDA", "emoji": "🖍️", "datos": ["se raya", "tiza"]}, "gana": "empate", "veredicto": "¡Las dos son rocas!",
  "voz": ["Comparamos dos rocas.", "*Dura*: no se raya. Como el granito.", "*Blanda*: se raya. Como la tiza.", "¡Las dos son *rocas*!"]},
 {"t": "pregunta", "pregunta": "¿Cómo son las piedras del río?", "opciones": ["REDONDAS Y LISAS", "CON PUNTAS"], "correcta": 0,
  "voz": ["Ahora vos: ¿cómo son las piedras del río?", "Pensá en el agua.", "¡*Redondas* y lisas!"]},
 {"t": "consejo", "titulo": "NO TIRES PIEDRAS", "texto": "Pueden lastimar", "emoji": "⚠️",
  "voz": ["Truco: mirá las piedras, pero no las *tires*."]},
 {"t": "resumen", "items": [["GRANITO", "muy duro"], ["TIZA", "blanda"], ["CANTO RODADO", "redondo, del río"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *granito* es muy duro.", "La *tiza* es blanda.", "El *canto rodado* es redondo.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Quién vive debajo de una piedra del jardín?", "segundos": 8, "respuesta": "¡Bichitos del suelo!", "emoji": "🪱", "titulo": "SERES VIVOS", "sub": "del suelo",
  "voz": ["Desafío: ¿quién vive debajo de una piedra?", "¡Muchos *bichitos*!", "Hoy: *seres vivos del suelo*."]},
 {"t": "documental", "emojis": ["🪱", "🐜", "🐞"], "lugar": "🌱", "rotulos": [{"txt": "LOMBRIZ", "sub": "hace túneles"}, {"txt": "HORMIGA", "sub": "en el hormiguero"}, {"txt": "BICHO BOLITA", "sub": "se hace bolita"}],
  "voz": ["La *lombriz* hace túneles.", "La *hormiga* vive en el hormiguero.", "El *bicho bolita* se hace bolita."]},
 {"t": "vof", "afirmacion": "Las lombrices le hacen mal al suelo", "emoji": "🪱", "verdadero": False, "explicacion": "Hacen túneles y mejoran la tierra",
  "voz": ["¿Verdadero o falso? Las lombrices hacen mal.", "Pensá en los túneles…", "¡*Falso*! Mejoran la tierra."]},
 {"t": "pregunta", "pregunta": "¿Qué comen las lombrices?", "opciones": ["HOJAS SECAS", "PIEDRAS"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué comen las lombrices?", "Pensá en el suelo.", "¡Hojas *secas*!"]},
 {"t": "consejo", "titulo": "CON CUIDADO", "texto": "Mirá y dejalos en su lugar", "emoji": "🔍",
  "voz": ["Truco: mirá los bichitos y *dejalos* en su lugar."]},
 {"t": "resumen", "items": [["LOMBRIZ", "hace túneles"], ["HORMIGA", "hormiguero"], ["BICHO BOLITA", "se hace bolita"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *lombriz* hace túneles.", "La *hormiga* vive en el hormiguero.", "El *bicho bolita* se hace bolita.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Abuela Rosa", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "¿Dónde siembro los porotos? 🌱"}, {"yo": True, "txt": "¡Vamos a probar!"}], "titulo": "SUELOS", "sub": "para sembrar",
  "voz": ["La abuela pregunta: ¿dónde siembro los porotos?", "Tomi responde: ¡vamos a *probar*!", "Hoy: *suelos para sembrar*."]},
 {"t": "matriz", "titulo": "TRES SUELOS", "celdas": [{"cab": "ARENA 🏖️", "txt": "el agua se va"}, {"cab": "ARCILLA 🧱", "txt": "el agua queda arriba"}, {"cab": "TIERRA NEGRA 🌱", "txt": "¡justo para sembrar!"}],
  "voz": ["Probamos tres suelos.", "*Arena*: el agua se va rápido.", "*Arcilla*: el agua queda arriba.", "*Tierra negra*: ¡justo para sembrar!"]},
 {"t": "escala", "titulo": "¿CUÁNTO CRECIÓ EL POROTO?", "items": [{"txt": "ARCILLA", "emoji": "🧱", "valor": 2}, {"txt": "ARENA", "emoji": "🏖️", "valor": 4}, {"txt": "TIERRA NEGRA", "emoji": "🌱", "valor": 10}],
  "voz": ["En la *arcilla*, creció poquito.", "En la *arena*, un poco más.", "En la *tierra negra*, ¡muchísimo!"]},
 {"t": "pregunta", "pregunta": "¿Qué suelo es mejor para sembrar?", "opciones": ["TIERRA NEGRA", "ARENA"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué suelo es mejor?", "Pensá en el poroto.", "¡La *tierra negra*!"]},
 {"t": "consejo", "titulo": "REGÁ IGUAL", "texto": "Para comparar, igual agua a todas", "emoji": "🚿",
  "voz": ["Truco: para comparar, regá *igual* a todas."]},
 {"t": "resumen", "items": [["ARENA", "el agua se va"], ["ARCILLA", "el agua queda"], ["TIERRA NEGRA", "la mejor"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la *arena*, el agua se va.", "En la *arcilla*, el agua queda.", "La *tierra negra* es la mejor para sembrar.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m9-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 9 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
