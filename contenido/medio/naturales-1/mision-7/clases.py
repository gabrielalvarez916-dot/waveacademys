# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 7 · El cielo de día y de noche: las 4 clases animadas.
Metáfora: el diario del cielo de Sofi. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m7-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 7
TIT = {1: 'El sol sale y se pone', 2: 'El día y la noche', 3: 'La luna y sus cambios', 4: 'Dibujo el cielo'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Ya salió el sol!"}, {"yo": True, "txt": "¡Y A LA TARDE SE PONE!"}, {"yo": False, "txt": "¿Por dónde?"}], "titulo": "EL SOL", "sub": "sale y se pone",
  "voz": ["Tomi le escribe a Sofi.", "¡Ya salió el *sol*!", "Y a la tarde *se pone*.", "Hoy: *el camino del sol*."]},
 {"t": "linea", "titulo": "EL CAMINO DEL SOL", "eventos": [{"fecha": "MAÑANA", "txt": "SALE", "emoji": "🌅"}, {"fecha": "MEDIODÍA", "txt": "ARRIBA", "emoji": "☀️"}, {"fecha": "TARDE", "txt": "SE PONE", "emoji": "🌇"}],
  "voz": ["A la *mañana*, el sol sale.", "Al *mediodía*, está muy arriba.", "A la *tarde*, se pone."]},
 {"t": "comparar", "a": {"cab": "AMANECER", "texto": "El sol sale", "emoji": "🌅"}, "b": {"cab": "ATARDECER", "texto": "El sol se pone", "emoji": "🌇"}, "signo": "vs",
  "voz": ["Cuando sale el sol: *amanecer*.", "Cuando se pone: *atardecer*.", "¡Sale por un lado y se pone por el otro!"]},
 {"t": "pregunta", "pregunta": "¿Dónde está el sol al mediodía?", "opciones": ["ESCONDIDO", "MUY ARRIBA", "SALIENDO"], "correcta": 1,
  "voz": ["Ahora vos. Es la hora del almuerzo.", "¿Dónde está el sol?", "¡*Muy arriba*!"]},
 {"t": "consejo", "titulo": "CUIDÁ TUS OJOS", "texto": "Nunca mires el sol directo", "emoji": "😎",
  "voz": ["Importante: nunca mires el sol *directo*."]},
 {"t": "resumen", "items": [["AMANECER", "el sol sale"], ["MEDIODÍA", "está arriba"], ["ATARDECER", "se pone"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En el *amanecer*, el sol sale.", "Al *mediodía*, está arriba.", "En el *atardecer*, se pone.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🌍", "lineas": ["Sofi juega con un trompo.", "Gira y gira sin parar.", "¡La Tierra hace lo mismo!"], "titulo": "DÍA", "sub": "y noche",
  "voz": ["Sofi juega con un *trompo*.", "Gira y gira sin parar.", "¡La *Tierra* hace lo mismo!", "Hoy: *el día y la noche*."]},
 {"t": "ciclo", "titulo": "UN DÍA ENTERO", "items": ["MAÑANA", "TARDE", "NOCHE", "MADRUGADA"],
  "voz": ["La Tierra gira y todo se *repite*.", "Primero, la *mañana*.", "Después, la *tarde*.", "Llega la *noche*.", "Y la *madrugada*. ¡Otra vez mañana!"]},
 {"t": "bloques", "titulo": "¿QUÉ HACEMOS?", "items": [{"cab": "☀️ DÍA", "txt": "ESCUELA Y JUEGOS"}, {"cab": "🌙 NOCHE", "txt": "CENAR Y DORMIR"}],
  "voz": ["Cada momento tiene lo suyo.", "De *día*: escuela y juegos.", "De *noche*: cenar y dormir."]},
 {"t": "pregunta", "pregunta": "¿Por qué hay día y noche?", "opciones": ["EL SOL SE APAGA", "LA TIERRA GIRA", "LA LUNA TAPA"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el trompo.", "¿Por qué hay día y noche?", "¡Porque la *Tierra gira*!"]},
 {"t": "consejo", "titulo": "EN OTRO LUGAR", "texto": "Cuando acá es de noche, allá es de día", "emoji": "🌏",
  "voz": ["Acá es de noche, allá es *de día*."]},
 {"t": "resumen", "items": [["GIRA", "como un trompo"], ["DÍA", "mira al sol"], ["NOCHE", "no mira al sol"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La Tierra *gira* como un trompo.", "La parte que mira al sol tiene *día*.", "La otra tiene *noche*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué brilla de noche y cambia de forma?", "segundos": 6, "respuesta": "¡LA LUNA!", "emoji": "🌙", "titulo": "LA LUNA", "sub": "y sus cambios",
  "voz": ["Desafío: ¿qué brilla de noche y cambia de forma?", "¡La *luna*!", "Hoy: *la luna y sus cambios*."]},
 {"t": "ciclo", "titulo": "LAS FASES", "items": ["NUEVA", "CRECIENTE", "LLENA", "MENGUANTE"],
  "voz": ["La luna parece *cambiar*.", "Luna *nueva*: no se ve.", "Luna *creciente*: va creciendo.", "Luna *llena*: redonda entera.", "Luna *menguante*: se va achicando."]},
 {"t": "zoom", "niveles": [{"emoji": "🌃", "txt": "EL CIELO"}, {"emoji": "🌕", "txt": "LA LUNA LLENA"}, {"emoji": "🔭", "txt": "SUS MANCHAS"}],
  "voz": ["Miramos el *cielo* de noche.", "Ahí está la *luna llena*.", "¡Con un telescopio vemos sus *manchas*!"]},
 {"t": "pregunta", "pregunta": "¿Cómo es la luna llena?", "opciones": ["NO SE VE", "REDONDA ENTERA", "COMO UNA BANANA"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la luna llena.", "¿Cómo se ve?", "¡*Redonda entera*!"]},
 {"t": "consejo", "titulo": "MIRALA CADA NOCHE", "texto": "Así la ves cambiar", "emoji": "📅",
  "voz": ["Truco: mirá la luna *varias noches*."]},
 {"t": "resumen", "items": [["LUNA", "de noche y a veces de día"], ["FASES", "sus formas"], ["CICLO", "se repite"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *luna* brilla en el cielo.", "Sus formas son las *fases*.", "Y se *repiten* siempre.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "DIARIO DEL CIELO", "titular": "¡SOFI DIBUJA EL CIELO!", "bajada": "De día y de noche", "emoji": "🖍️", "titulo": "DIBUJO", "sub": "el cielo",
  "voz": ["¡Sofi arma el *diario del cielo*!", "Lo dibuja de día y de noche.", "Hoy: *dibujo el cielo*."]},
 {"t": "flujo", "titulo": "CÓMO LO HAGO", "items": ["MIRO", "DIBUJO", "ANOTO LA HORA", "COMPARO"],
  "voz": ["Primero, *miro* el cielo.", "Después, lo *dibujo*.", "*Anoto la hora*.", "Y al final, *comparo*."]},
 {"t": "matriz", "titulo": "¿QUÉ HAY EN EL CIELO?", "celdas": [{"cab": "☀️ DÍA", "txt": "SOL"}, {"cab": "☁️ DÍA", "txt": "NUBES"}, {"cab": "🌙 NOCHE", "txt": "LUNA"}, {"cab": "⭐ NOCHE", "txt": "ESTRELLAS"}],
  "voz": ["Miramos qué hay en el cielo.", "De día, el *sol*.", "De día también, las *nubes*.", "De noche, la *luna*.", "Y de noche, las *estrellas*."]},
 {"t": "consejo", "titulo": "ANOTÁ LA HORA", "texto": "Así podés comparar", "emoji": "⏰",
  "voz": ["Truco: anotá la *hora* al lado del dibujo."]},
 {"t": "pregunta", "pregunta": "¿Qué dibujás en el cielo de noche?", "opciones": ["EL SOL", "LA LUNA", "EL ARCOÍRIS"], "correcta": 1,
  "voz": ["Ahora vos. Es de noche.", "¿Qué dibujás en el cielo?", "¡La *luna* y las estrellas!"]},
 {"t": "resumen", "items": [["DÍA", "sol y nubes"], ["NOCHE", "luna y estrellas"], ["REGISTRO", "dibujo y hora"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "De *día*: sol y nubes.", "De *noche*: luna y estrellas.", "Dibujamos y anotamos la *hora*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
