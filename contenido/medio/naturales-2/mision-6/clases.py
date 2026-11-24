# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 6 · Empujar y tirar: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (en el patio y la plaza).
Genera tools/medio/clase/lecciones/medio-nat2-m6-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '15c1cd5d-3639-4788-8c14-dff382ec4e41', 2: '1912322f-775c-4335-a540-08f18c016902', 3: '1f98c7b6-2ee4-45e0-843e-dbab3a06737f', 4: '81fcc891-c126-4e51-b420-c7ac2b05fbec'}
TIT = {1: 'Empujar, tirar y mover', 2: 'Rápido y despacio', 3: 'El rozamiento', 4: 'Los imanes atraen'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🛒", "lineas": ["Tomi lleva un carrito.", "Primero lo empuja.", "Después tira de una soga."], "titulo": "EMPUJAR", "sub": "y tirar",
  "voz": ["Tomi lleva un *carrito*.", "Primero lo *empuja*.", "Después *tira* de una soga.", "Hoy: *empujar y tirar*."]},
 {"t": "versus", "titulo": "EMPUJAR O TIRAR", "a": {"txt": "EMPUJAR", "emoji": "👐", "datos": ["aleja", "hamaca, puerta"]}, "b": {"txt": "TIRAR", "emoji": "🪢", "datos": ["acerca", "cajón, soga"]}, "gana": "empate", "veredicto": "¡Las dos son fuerzas!",
  "voz": ["Comparamos dos formas de mover.", "*Empujar*: aleja. Como la hamaca.", "*Tirar*: acerca. Como el cajón.", "¡Las dos son *fuerzas*!"]},
 {"t": "unir", "titulo": "¿EMPUJO O TIRO?", "pares": [["HAMACA", "empujo"], ["CAJÓN", "tiro"], ["CHANGUITO", "empujo"]], "mezclar": True,
  "voz": ["Unimos cada cosa con lo que hacemos.", "La hamaca: la *empujo*.", "El cajón: *tiro*.", "El changuito: lo *empujo*."]},
 {"t": "pregunta", "pregunta": "¿Una pelota quieta se mueve sola?", "opciones": ["NO, NECESITA FUERZA", "SÍ, SOLA"], "correcta": 0,
  "voz": ["Ahora vos: ¿una pelota quieta se mueve sola?", "Pensá en la fuerza.", "¡No! Necesita una *fuerza*."]},
 {"t": "consejo", "titulo": "¿SE ALEJA O SE ACERCA?", "texto": "Se aleja: empujás. Se acerca: tirás", "emoji": "↔️",
  "voz": ["Truco: si se *aleja*, empujás. Si se *acerca*, tirás."]},
 {"t": "resumen", "items": [["EMPUJAR", "aleja"], ["TIRAR", "acerca"], ["FUERZA", "hace mover"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Empujar* aleja.", "*Tirar* acerca.", "La *fuerza* hace mover las cosas.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Sofi", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "¡Pateé la pelota re lejos! ⚽"}, {"yo": True, "txt": "¡La pateaste fuerte!"}], "titulo": "RÁPIDO", "sub": "y despacio",
  "voz": ["Sofi le escribe: ¡pateé la pelota muy lejos!", "Tomi responde: ¡la pateaste *fuerte*!", "Hoy: *rápido y despacio*."]},
 {"t": "escala", "titulo": "MÁS FUERZA, MÁS LEJOS", "items": [{"txt": "SUAVE", "emoji": "🐢", "valor": 2}, {"txt": "MEDIANA", "emoji": "🚶", "valor": 5}, {"txt": "FUERTE", "emoji": "🚀", "valor": 10}],
  "voz": ["Patada *suave*: la pelota va cerca.", "Patada *mediana*: va un poco más lejos.", "Patada *fuerte*: ¡llega lejísimos!"]},
 {"t": "pistas", "problema": "¿Quién frena la pelota?", "pistas": ["Está en el arco", "Usa guantes", "Ataja con las manos"], "respuesta": "EL ARQUERO 🧤",
  "voz": ["Adivinanza: ¿quién *frena* la pelota?", "Pista uno: está en el arco.", "Pista dos: usa guantes.", "Pista tres: ataja con las manos.", "¡El *arquero*! Frenar también es fuerza."]},
 {"t": "pregunta", "pregunta": "¿Con qué patada la pelota va más lejos?", "opciones": ["FUERTE", "SUAVE"], "correcta": 0,
  "voz": ["Ahora vos: ¿con qué patada va más lejos?", "Pensá en la fuerza.", "¡Con la *fuerte*!"]},
 {"t": "consejo", "titulo": "JUGÁ CON CUIDADO", "texto": "Sin golpear a nadie", "emoji": "⚽",
  "voz": ["Truco: jugá con fuerza, pero sin golpear a nadie."]},
 {"t": "resumen", "items": [["SUAVE", "despacio y cerca"], ["FUERTE", "rápido y lejos"], ["FRENAR", "también es fuerza"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Fuerza *suave*: despacio y cerca.", "Fuerza *fuerte*: rápido y lejos.", "*Frenar* también es una fuerza.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Por qué la pelota que rueda al final para?", "segundos": 8, "respuesta": "¡El piso la frena!", "emoji": "⚽", "titulo": "EL ROZAMIENTO", "sub": "lo que frena",
  "voz": ["Desafío: ¿por qué la pelota al final *para*?", "¡El piso la *frena*!", "Hoy: *el rozamiento*."]},
 {"t": "zoom", "niveles": [{"emoji": "👟", "txt": "UNA ZAPATILLA"}, {"emoji": "🔍", "txt": "LA SUELA"}, {"emoji": "〰️", "txt": "¡DIBUJITOS PARA NO RESBALAR!"}],
  "voz": ["Miramos de cerca una *zapatilla*.", "Más cerca: la *suela*.", "¡Tiene *dibujitos* para no resbalar!"]},
 {"t": "escape", "titulo": "LA PISTA DE PATINAJE", "candados": [{"p": "¿Dónde resbalamos más?", "r": "EN EL HIELO"}, {"p": "¿Qué frena más?", "r": "LA ALFOMBRA"}],
  "voz": ["¡Para salir de la pista, abrimos los candados!", "Resbalamos más en el *hielo*.", "Frena más la *alfombra*.", "¡Salimos!"]},
 {"t": "definicion", "palabra": "Rozamiento", "texto": "Cuando algo se arrastra, el piso lo frena", "emoji": "🛑",
  "voz": ["Eso se llama *rozamiento*.", "Lo áspero frena *más* que lo liso."]},
 {"t": "consejo", "titulo": "CUIDADO", "texto": "Los pisos mojados resbalan", "emoji": "⚠️",
  "voz": ["Truco: cuidado con los pisos *mojados*: ¡resbalan!"]},
 {"t": "resumen", "items": [["ROZAMIENTO", "frena"], ["LISO", "frena menos"], ["ÁSPERO", "frena más"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *rozamiento* frena lo que se arrastra.", "Lo *liso* frena menos.", "Lo *áspero* frena más.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "LABORATORIO", "titular": "¡Los clips saltan solos!", "bajada": "Tomi tiene un imán", "emoji": "🧲", "titulo": "LOS IMANES", "sub": "atraen",
  "voz": ["¡Noticia: los clips *saltan* solos!", "Tomi tiene un *imán*.", "Hoy: *los imanes atraen*."]},
 {"t": "personaje", "personaje": {"nombre": "Imán Iván", "emoji": "🧲"}, "lineas": [{"txt": "¡Hola! Yo atraigo clips y clavos.", "animo": "feliz"}, {"txt": "¡Sin tocarlos!", "animo": "sorpresa"}, {"txt": "Pero el papel y la madera, no.", "animo": "piensa"}],
  "voz": ["¡Hola! Yo *atraigo* clips y clavos.", "¡Sin tocarlos!", "Pero el *papel* y la *madera*, no."]},
 {"t": "clasificar", "cajas": [{"cab": "ATRAE", "emoji": "🧲"}, {"cab": "NO ATRAE", "emoji": "🚫"}], "fichas": [{"txt": "CLIP", "caja": 0}, {"txt": "CLAVO", "caja": 0}, {"txt": "PAPEL", "caja": 1}, {"txt": "GOMA", "caja": 1}],
  "voz": ["Probamos con el imán.", "El clip y el clavo: ¡los *atrae*!", "El papel y la goma: *no* los atrae."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Confundido", "emoji": "🤖"}, "preguntas": [{"p": "¿El imán atrae un tornillo?", "r": "SÍ"}, {"p": "¿Atrae una cuchara de madera?", "r": "NO"}],
  "voz": ["¡Apareció el *Monstruo Confundido*!", "No sabe qué atrae el imán.", "¿Un tornillo? ¡*Sí*!", "¿Una cuchara de madera? ¡*No*! ¡Ganamos!"]},
 {"t": "consejo", "titulo": "PROBÁ Y ANOTÁ", "texto": "Dos listas: atrae y no atrae", "emoji": "📝",
  "voz": ["Truco: probá y anotá en *dos listas*."]},
 {"t": "resumen", "items": [["IMÁN", "atrae sin tocar"], ["ATRAE", "clips, clavos"], ["NO ATRAE", "papel, madera"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *imán* atrae sin tocar.", "*Atrae* clips y clavos.", "*No atrae* papel ni madera.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m6-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 6 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
