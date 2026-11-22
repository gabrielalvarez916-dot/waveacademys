# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 1 · Mi cuerpo, otra vez: las 4 clases animadas.
Metáfora: el cuerpo es un equipo. Regla de primeros años y variedad del banco (partes, experimento, zoom, barras…).
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TIT = {1: 'Partes de mi cuerpo y para qué sirven', 2: 'Lo que cambió desde el jardín', 3: 'Lavado de manos y salud', 4: 'Registro lo que observo'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "⚽", "lineas": ["Sofi juega a la pelota.", "Corre, mira y patea.", "¡Todo su cuerpo ayuda!"], "titulo": "MI CUERPO", "sub": "un gran equipo",
  "voz": ["Sofi juega a la *pelota*.", "Corre, mira y patea.", "¡Todo su cuerpo ayuda!", "Hoy: *las partes de mi cuerpo*."]},
 {"t": "partes", "emoji": "🧍", "titulo": "MI CUERPO", "partes": [{"txt": "CABEZA", "x": 0.1, "y": -0.8}, {"txt": "TRONCO", "x": -0.1, "y": -0.1}, {"txt": "BRAZOS", "x": 0.5, "y": -0.2}, {"txt": "PIERNAS", "x": -0.2, "y": 0.7}],
  "voz": ["Este es nuestro *cuerpo*.", "Arriba está la *cabeza*.", "En el medio, el *tronco*.", "A los costados, los *brazos*.", "Abajo, las *piernas*."]},
 {"t": "bloques", "titulo": "CADA UNO, SU TRABAJO", "items": [{"cab": "👀 OJOS", "txt": "VER"}, {"cab": "👂 OREJAS", "txt": "OÍR"}, {"cab": "👃 NARIZ", "txt": "OLER"}, {"cab": "👅 LENGUA", "txt": "PROBAR"}, {"cab": "✋ PIEL", "txt": "TOCAR"}],
  "voz": ["Cada parte tiene su *trabajo*.", "Con los ojos, *vemos*.", "Con las orejas, *oímos*.", "Con la nariz, *olemos*.", "Con la lengua, *probamos*.", "Con la piel, *tocamos*."]},
 {"t": "pregunta", "pregunta": "¿Con qué olés una flor?", "opciones": ["OJOS", "NARIZ", "OREJAS"], "correcta": 1,
  "voz": ["Ahora vos. Hay una flor linda.", "¿Con qué sentís su olor?", "¡Con la *nariz*!"]},
 {"t": "consejo", "titulo": "UN EQUIPO", "texto": "Todas las partes ayudan", "emoji": "🤝",
  "voz": ["Tu cuerpo es un *equipo*: todas ayudan."]},
 {"t": "resumen", "items": [["PARTES", "cabeza, tronco, extremidades"], ["SENTIDOS", "ver, oír, oler, probar, tocar"], ["EQUIPO", "todas ayudan"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Cabeza, *tronco* y extremidades.", "Cinco *sentidos* para conocer.", "Todas las partes son un *equipo*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Te entran las zapatillas del jardín?", "segundos": 6, "respuesta": "¡NO! ¡CRECÍ!", "emoji": "👟", "titulo": "CRECER", "sub": "desde el jardín",
  "voz": ["Desafío: ¿te entran las zapatillas del jardín?", "¡No! ¡Tus pies *crecieron*!", "Hoy: *lo que cambió desde el jardín*."]},
 {"t": "antesdespues", "antes": {"cab": "EN EL JARDÍN", "emoji": "🧒", "texto": "Más bajito"}, "despues": {"cab": "AHORA", "emoji": "🧑", "texto": "Más alto"},
  "voz": ["En el jardín eras más *bajito*.", "Ahora sos más *alto*."]},
 {"t": "linea", "titulo": "MI DIENTE", "eventos": [{"fecha": "1", "txt": "SE MUEVE", "emoji": "🦷"}, {"fecha": "2", "txt": "SE CAE", "emoji": "😁"}, {"fecha": "3", "txt": "SALE UNO NUEVO", "emoji": "✨"}],
  "voz": ["Primero, el diente se *mueve*.", "Después, se *cae*.", "Y sale un diente *nuevo*."]},
 {"t": "pregunta", "pregunta": "¿Qué pasa con los dientes de leche?", "opciones": ["SE PONEN AZULES", "SE CAEN Y SALEN OTROS", "NUNCA CAMBIAN"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en los dientes.", "¿Qué pasa con los de leche?", "¡Se *caen* y salen otros!"]},
 {"t": "consejo", "titulo": "A TU RITMO", "texto": "Cada chico crece a su tiempo", "emoji": "🌱",
  "voz": ["Truco: cada chico crece a *su ritmo*."]},
 {"t": "resumen", "items": [["CRECER", "más alto"], ["DIENTES", "se caen y salen"], ["RITMO", "cada uno el suyo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Desde el jardín, *creciste*.", "Los dientes de leche se *caen*.", "Cada uno crece a *su ritmo*.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡HAY MICROBIOS EN LAS MANOS!", "bajada": "Son tan chiquitos que no se ven", "emoji": "🦠", "titulo": "MANOS LIMPIAS", "sub": "y salud",
  "voz": ["¡Último momento! Hay *microbios* en las manos.", "Son tan chiquitos que no se ven.", "Hoy: *lavarnos bien las manos*."]},
 {"t": "zoom", "niveles": [{"emoji": "✋", "txt": "MI MANO"}, {"emoji": "🔍", "txt": "CON LUPA"}, {"emoji": "🦠", "txt": "MICROBIOS"}],
  "voz": ["Miramos una *mano*.", "La miramos con una lupa gigante.", "¡Aparecen los *microbios*!"]},
 {"t": "experimento", "titulo": "¿AGUA SOLA O CON JABÓN?", "variable": "EL JABÓN", "a": {"cab": "SOLO AGUA", "emojis": ["✋", "💧"], "txt": "Sin jabón", "res": "QUEDAN MICROBIOS"}, "b": {"cab": "AGUA Y JABÓN", "emojis": ["✋", "🧼"], "txt": "Con jabón", "res": "¡MANOS LIMPIAS!"},
  "voz": ["Tomi lava una mano solo con agua.", "La otra, con agua y *jabón*.", "¡Con jabón, los microbios se van!"]},
 {"t": "pasos", "titulo": "PASO A PASO", "items": [{"txt": "MOJAR", "emoji": "💧"}, {"txt": "JABÓN", "emoji": "🧼"}, {"txt": "FROTAR HASTA 20", "emoji": "👐"}, {"txt": "ENJUAGAR", "emoji": "🚿"}, {"txt": "SECAR", "emoji": "🧻"}],
  "voz": ["Así nos lavamos las manos.", "Primero, *mojamos*.", "Ponemos *jabón*.", "Frotamos contando hasta *20*.", "*Enjuagamos* con agua.", "Y *secamos*."]},
 {"t": "pregunta", "pregunta": "¿Cuándo te lavás las manos?", "opciones": ["ANTES DE COMER", "AL DORMIR", "AL CANTAR"], "correcta": 0,
  "voz": ["Ahora vos. Pensá un momento importante.", "¿Cuándo te lavás las manos?", "¡*Antes de comer*!"]},
 {"t": "resumen", "items": [["MICROBIOS", "no se ven"], ["JABÓN", "siempre"], ["CUÁNDO", "antes de comer"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *microbios* no se ven.", "Siempre con agua y *jabón*.", "Y *antes de comer*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Cuánto mide tu mano?"}, {"yo": True, "txt": "¡4 CUADRADITOS DE LANA!"}, {"yo": False, "txt": "¡La mía mide 5!"}], "titulo": "OBSERVO", "sub": "y registro",
  "voz": ["Tomi le escribe a Sofi.", "¿Cuánto mide tu mano?", "Sofi la midió con lana.", "Hoy: *observar y registrar*."]},
 {"t": "matriz", "titulo": "OBSERVO CON…", "celdas": [{"cab": "👀", "txt": "MIRO"}, {"cab": "✋", "txt": "TOCO"}, {"cab": "👃", "txt": "HUELO"}, {"cab": "👂", "txt": "ESCUCHO"}],
  "voz": ["Observar es mirar con *atención*.", "Con los ojos, *miro*.", "Con las manos, *toco*.", "Con la nariz, *huelo*.", "Con las orejas, *escucho*."]},
 {"t": "barras", "titulo": "REGISTRO DE TOMI", "unidad": "cuadraditos", "items": [{"txt": "MANO", "valor": 5}, {"txt": "PIE", "valor": 7}, {"txt": "BRAZO", "valor": 11}],
  "voz": ["Tomi anota lo que *midió*.", "Su mano: *5* cuadraditos.", "Su pie: *7*.", "Su brazo: *11*. ¡El más largo!"]},
 {"t": "pregunta", "pregunta": "¿Qué parte de Tomi es la más larga?", "opciones": ["MANO", "PIE", "BRAZO"], "correcta": 2,
  "voz": ["Ahora vos. Mirá el registro.", "¿Qué parte es la más larga?", "¡El *brazo*!"]},
 {"t": "consejo", "titulo": "ANOTÁ ENSEGUIDA", "texto": "Así no te olvidás", "emoji": "✏️",
  "voz": ["Truco: anotá *enseguida* lo que observás."]},
 {"t": "resumen", "items": [["OBSERVAR", "mirar con atención"], ["REGISTRAR", "anotar o dibujar"], ["COMPARAR", "cuál es más largo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Observar* es mirar con atención.", "*Registrar* es anotar o dibujar.", "Y así podemos *comparar*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m1-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": 1, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
