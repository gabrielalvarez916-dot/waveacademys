# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 5 · El campo y la ciudad: las 4 clases animadas.
Metáfora: el viaje en micro de la ciudad al campo. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 5
TIT = {1: 'Paisajes del campo', 2: 'Paisajes de la ciudad', 3: 'Qué hay en el campo y qué hay en la ciudad', 4: 'Comparamos un pueblo y una ciudad'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🚌", "lineas": ["Sofi viaja en micro.", "Sale de la ciudad.", "¡Por la ventana ve el campo!"], "titulo": "EL CAMPO", "sub": "sus paisajes",
  "voz": ["Sofi viaja en *micro*.", "Sale de la ciudad.", "¡Por la ventana ve el *campo*!", "Hoy: *paisajes del campo*."]},
 {"t": "zoom", "niveles": [{"emoji": "🏞️", "txt": "EL CAMPO"}, {"emoji": "🏡", "txt": "UNA GRANJA"}, {"emoji": "🐄", "txt": "UNA VACA"}],
  "voz": ["Miramos el *campo* desde lejos.", "Nos acercamos a una *granja*.", "¡Y vemos una *vaca*!"]},
 {"t": "bloques", "titulo": "EN EL CAMPO HAY", "items": [{"cab": "🌾", "txt": "SEMBRADOS"}, {"cab": "🐎", "txt": "ANIMALES"}, {"cab": "🏠", "txt": "POCAS CASAS"}, {"cab": "🛤️", "txt": "CAMINOS DE TIERRA"}],
  "voz": ["Miramos el *paisaje* del campo.", "Hay campos *sembrados*.", "Hay *animales*.", "Hay *pocas casas*.", "Y *caminos de tierra*."]},
 {"t": "pregunta", "pregunta": "¿Cómo están las casas en el campo?", "opciones": ["MUY JUNTAS", "LEJOS", "UNA ARRIBA DE OTRA"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el campo.", "¿Cómo están las casas?", "¡*Lejos* unas de otras!"]},
 {"t": "consejo", "titulo": "MIRÁ TODO", "texto": "El paisaje es todo lo que ves", "emoji": "👀",
  "voz": ["Truco: el *paisaje* es todo lo que ves."]},
 {"t": "resumen", "items": [["PAISAJE", "lo que vemos"], ["CAMPO", "espacio, plantas, animales"], ["CASAS", "lejos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *paisaje* es lo que vemos.", "El *campo* tiene espacio y animales.", "Las casas están *lejos*.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Qué luces te dicen cuándo cruzar?", "segundos": 6, "respuesta": "¡EL SEMÁFORO!", "emoji": "🚦", "titulo": "LA CIUDAD", "sub": "sus paisajes",
  "voz": ["Desafío: ¿qué luces te dicen cuándo cruzar?", "¡El *semáforo*!", "Hoy: *paisajes de la ciudad*."]},
 {"t": "partes", "emoji": "🏙️", "titulo": "LA CIUDAD", "partes": [{"txt": "EDIFICIOS", "x": -0.4, "y": -0.6}, {"txt": "SEMÁFORO", "x": 0.6, "y": -0.2}, {"txt": "COLECTIVO", "x": -0.5, "y": 0.5}, {"txt": "VEREDA", "x": 0.5, "y": 0.7}],
  "voz": ["Miramos la *ciudad*.", "Hay *edificios* altos.", "Hay *semáforos*.", "Pasan *colectivos*.", "Y la gente camina por la *vereda*."]},
 {"t": "barras", "titulo": "AUTOS EN UN MINUTO", "unidad": "autos", "items": [{"txt": "CAMPO", "valor": 1}, {"txt": "CIUDAD", "valor": 20}],
  "voz": ["Tomi cuenta *autos* en un minuto.", "En el campo: *1*.", "¡En la ciudad: *20*!"]},
 {"t": "pregunta", "pregunta": "¿Dónde hay más ruido?", "opciones": ["CAMPO", "CIUDAD", "IGUAL"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en los autos.", "¿Dónde hay más ruido?", "¡En la *ciudad*!"]},
 {"t": "consejo", "titulo": "CON UN ADULTO", "texto": "En la ciudad cruzá siempre acompañado", "emoji": "🚸",
  "voz": ["Importante: cruzá siempre *con un adulto*."]},
 {"t": "resumen", "items": [["CIUDAD", "edificios y gente"], ["MOVIMIENTO", "autos, colectivos"], ["RUIDO", "más que el campo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *ciudad* tiene edificios.", "Hay mucho *movimiento*.", "Y más *ruido* que el campo.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": {"nombre": "Prima Lu", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "¡Hoy fui a la escuela a caballo!"}, {"yo": True, "txt": "¡YO FUI EN COLECTIVO!"}, {"yo": False, "txt": "¡Las dos fuimos a la escuela!"}], "titulo": "CAMPO", "sub": "y ciudad",
  "voz": ["La prima Lu vive en el *campo*.", "Fue a la escuela a caballo.", "Sofi vive en la ciudad y fue en *colectivo*.", "Hoy: *qué hay en el campo y en la ciudad*."]},
 {"t": "venn", "a": "CAMPO", "b": "CIUDAD", "itemsA": ["TRACTOR", "VACAS"], "itemsB": ["EDIFICIOS", "SEMÁFOROS"], "ambos": ["ESCUELAS", "FAMILIAS"],
  "voz": ["Comparamos el campo y la ciudad.", "En el *campo*: tractores y vacas.", "En la *ciudad*: edificios y semáforos.", "¡En los *dos*: escuelas y familias!"]},
 {"t": "matriz", "titulo": "¿CÓMO VAN A LA ESCUELA?", "celdas": [{"cab": "🐴 CAMPO", "txt": "A CABALLO"}, {"cab": "🚜 CAMPO", "txt": "EN CAMIONETA"}, {"cab": "🚌 CIUDAD", "txt": "EN COLECTIVO"}, {"cab": "🚶 CIUDAD", "txt": "CAMINANDO"}],
  "voz": ["Cada chico llega distinto.", "En el campo, algunos van *a caballo*.", "Otros, en *camioneta*.", "En la ciudad, en *colectivo*.", "O *caminando*."]},
 {"t": "pregunta", "pregunta": "¿Qué hay en los dos?", "opciones": ["TRACTORES", "ESCUELAS", "SEMÁFOROS"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el campo y la ciudad.", "¿Qué hay en los dos?", "¡*Escuelas*!"]},
 {"t": "consejo", "titulo": "TODOS VALEN", "texto": "Ningún lugar es mejor que otro", "emoji": "💛",
  "voz": ["Recordá: ningún lugar es *mejor* que otro."]},
 {"t": "resumen", "items": [["CAMPO", "tractores, vacas"], ["CIUDAD", "edificios, semáforos"], ["LOS DOS", "escuelas y familias"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En el *campo* hay tractores.", "En la *ciudad* hay edificios.", "En los *dos* hay escuelas.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡EL PUEBLO DEL ABUELO CRECIÓ!", "bajada": "Ahora es una ciudad", "emoji": "🏘️", "titulo": "PUEBLO", "sub": "y ciudad",
  "voz": ["¡Último momento! El pueblo del abuelo *creció*.", "Ahora es una ciudad.", "Hoy: *comparamos un pueblo y una ciudad*."]},
 {"t": "comparar", "a": {"cab": "PUEBLO", "texto": "CHICO, TODOS SE CONOCEN", "emoji": "🏡"}, "b": {"cab": "CIUDAD", "texto": "GRANDE, MUCHA GENTE", "emoji": "🏙️"}, "signo": "vs",
  "voz": ["El *pueblo* es chico: todos se conocen.", "La *ciudad* es grande: hay mucha gente.", "¡Los dos tienen escuela y plaza!"]},
 {"t": "linea", "titulo": "EL PUEBLO CRECE", "eventos": [{"fecha": "HACE MUCHO", "txt": "POCAS CASAS", "emoji": "🏠"}, {"fecha": "DESPUÉS", "txt": "MÁS CASAS", "emoji": "🏘️"}, {"fecha": "HOY", "txt": "EDIFICIOS", "emoji": "🏙️"}],
  "voz": ["Hace mucho, había *pocas casas*.", "Después, hicieron *más casas*.", "¡Hoy hay *edificios*!"]},
 {"t": "pregunta", "pregunta": "¿Dónde casi todos se conocen?", "opciones": ["PUEBLO", "CIUDAD GRANDE", "AEROPUERTO"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en un lugar chico.", "¿Dónde todos se conocen?", "¡En el *pueblo*!"]},
 {"t": "consejo", "titulo": "PREGUNTÁ", "texto": "Los abuelos saben cómo era antes", "emoji": "👴",
  "voz": ["Truco: preguntá a los *abuelos* cómo era antes."]},
 {"t": "resumen", "items": [["PUEBLO", "chico, todos se conocen"], ["CIUDAD", "grande, mucha gente"], ["CAMBIA", "un pueblo crece"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *pueblo* es chico.", "La *ciudad* es grande.", "Y un pueblo puede *crecer*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
