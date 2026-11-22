# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 3 · Mi barrio y sus lugares: las 4 clases animadas.
Metáfora: el paseo por el barrio. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 3
TIT = {1: 'Recorremos y observamos el barrio', 2: 'Croquis de la manzana de la escuela', 3: 'Lugares para jugar y encontrarnos', 4: 'Placas y monumentos con historia'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🏘️", "lineas": ["Sofi sale a caminar con su papá.", "Mira las casas y los negocios.", "¡Descubre su barrio!"], "titulo": "MI BARRIO", "sub": "lo recorro",
  "voz": ["Sofi sale a caminar con su *papá*.", "Mira las casas y los negocios.", "¡Descubre su *barrio*!", "Hoy: *recorremos el barrio*."]},
 {"t": "bloques", "titulo": "EN MI BARRIO HAY", "items": [{"cab": "🏠", "txt": "CASAS"}, {"cab": "🏪", "txt": "NEGOCIOS"}, {"cab": "🌳", "txt": "PLAZA"}, {"cab": "🏫", "txt": "ESCUELA"}],
  "voz": ["Miramos qué hay en el *barrio*.", "Hay *casas*.", "Hay *negocios*.", "Hay una *plaza*.", "¡Y hay una *escuela*!"]},
 {"t": "flujo", "titulo": "CÓMO OBSERVO", "items": ["SALGO CON UN ADULTO", "MIRO", "ESCUCHO", "ANOTO"],
  "voz": ["Primero, salgo con un *adulto*.", "Después, *miro* todo.", "*Escucho* los sonidos.", "Y *anoto* lo que vi."]},
 {"t": "pregunta", "pregunta": "¿Con quién recorrés el barrio?", "opciones": ["SOLO", "CON UN ADULTO", "CON MI PERRO"], "correcta": 1,
  "voz": ["Ahora vos. Vas a salir a caminar.", "¿Con quién vas?", "¡*Con un adulto*!"]},
 {"t": "consejo", "titulo": "POR LA ESQUINA", "texto": "La calle se cruza por la esquina", "emoji": "🚸",
  "voz": ["Importante: cruzá siempre por la *esquina*."]},
 {"t": "resumen", "items": [["BARRIO", "donde vive la gente"], ["LUGARES", "casas, negocios, plaza"], ["OBSERVAR", "mirar y anotar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *barrio* es donde vive la gente.", "Tiene muchos *lugares*.", "Lo *observamos* y anotamos.", CIERRE]},
]
N2 = [
 {"t": "reto", "texto": "¿Cómo se ve la escuela desde un avión?", "segundos": 6, "respuesta": "¡COMO UN CUADRADITO!", "emoji": "✈️", "titulo": "EL CROQUIS", "sub": "de la manzana",
  "voz": ["Desafío: ¿cómo se ve la escuela desde un *avión*?", "¡Como un *cuadradito*!", "Hoy: *el croquis de la manzana*."]},
 {"t": "zoom", "niveles": [{"emoji": "🏙️", "txt": "LA CIUDAD"}, {"emoji": "🏘️", "txt": "EL BARRIO"}, {"emoji": "🟩", "txt": "LA MANZANA"}],
  "voz": ["Miramos la *ciudad* desde arriba.", "Nos acercamos al *barrio*.", "¡Y vemos la *manzana* de la escuela!"]},
 {"t": "partes", "emoji": "🟩", "titulo": "MI MANZANA", "partes": [{"txt": "ESCUELA", "x": 0.0, "y": -0.6}, {"txt": "KIOSCO", "x": -0.6, "y": -0.2}, {"txt": "CASA DE SOFI", "x": 0.6, "y": -0.2}, {"txt": "PANADERÍA", "x": 0.0, "y": 0.6}],
  "voz": ["Este es el *croquis* de la manzana.", "Acá está la *escuela*.", "A un lado, el *kiosco*.", "Al otro lado, la *casa de Sofi*.", "Y atrás, la *panadería*."]},
 {"t": "pregunta", "pregunta": "¿Cuántas calles rodean la manzana?", "opciones": ["2", "4", "10"], "correcta": 1,
  "voz": ["Ahora vos. Mirá los lados.", "¿Cuántas calles la rodean?", "¡*4 calles*!"]},
 {"t": "consejo", "titulo": "COMO UN PÁJARO", "texto": "Imaginá que mirás desde arriba", "emoji": "🐦",
  "voz": ["Truco: imaginá que sos un *pájaro*."]},
 {"t": "resumen", "items": [["MANZANA", "cuatro calles"], ["CROQUIS", "dibujo desde arriba"], ["UBICAR", "al lado, atrás"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *manzana* tiene cuatro calles.", "El *croquis* es un dibujo desde arriba.", "Ubicamos qué hay *al lado*.", CIERRE]},
]
N3 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Vamos a la plaza?"}, {"yo": True, "txt": "¡SÍ! NOS VEMOS EN LAS HAMACAS"}, {"yo": False, "txt": "¡Llevo la pelota!"}], "titulo": "LUGARES", "sub": "para jugar",
  "voz": ["Tomi le escribe a Sofi.", "¿Vamos a la plaza?", "¡Nos vemos en las *hamacas*!", "Hoy: *lugares para jugar y encontrarnos*."]},
 {"t": "matriz", "titulo": "LUGARES PARA ENCONTRARNOS", "celdas": [{"cab": "🌳 PLAZA", "txt": "JUGAR"}, {"cab": "⚽ CLUB", "txt": "DEPORTE"}, {"cab": "📚 BIBLIOTECA", "txt": "LEER"}, {"cab": "🎭 CENTRO CULTURAL", "txt": "ARTE"}],
  "voz": ["En el barrio hay lugares para *todos*.", "En la *plaza*, jugamos.", "En el *club*, hacemos deporte.", "En la *biblioteca*, leemos.", "En el *centro cultural*, hacemos arte."]},
 {"t": "comparar", "a": {"cab": "PLAZA", "texto": "SÍ SE JUEGA", "emoji": "🛝"}, "b": {"cab": "CALLE", "texto": "NO: PASAN AUTOS", "emoji": "🚗"}, "signo": "vs",
  "voz": ["En la *plaza* jugamos tranquilos.", "En la *calle* pasan autos.", "¡En la calle *no* se juega!"]},
 {"t": "pregunta", "pregunta": "¿De quién es la plaza?", "opciones": ["DE NADIE", "DE TODOS", "DE UNO"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en la plaza.", "¿De quién es?", "¡De *todos*! Es un espacio público."]},
 {"t": "consejo", "titulo": "LO CUIDAMOS", "texto": "Lo que es de todos, lo cuidamos todos", "emoji": "🤝",
  "voz": ["Recordá: lo que es de todos, lo *cuidamos* todos."]},
 {"t": "resumen", "items": [["PLAZA", "para jugar"], ["PÚBLICO", "es de todos"], ["CUIDAR", "entre todos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *plaza* es para jugar.", "Es un espacio *público*.", "Y lo *cuidamos* entre todos.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "HISTORIAS DEL BARRIO", "titular": "¡HAY UNA PLACA EN LA PLAZA!", "bajada": "Recuerda algo importante", "emoji": "🗿", "titulo": "PLACAS", "sub": "y monumentos",
  "voz": ["¡Historias del barrio! Hay una *placa* en la plaza.", "Recuerda algo importante.", "Hoy: *placas y monumentos con historia*."]},
 {"t": "antesdespues", "antes": {"cab": "HACE MUCHO", "emoji": "🟫", "texto": "Plaza de tierra"}, "despues": {"cab": "HOY", "emoji": "🛝", "texto": "¡Con juegos y árboles!"},
  "voz": ["Hace mucho, la plaza era de *tierra*.", "Hoy tiene *juegos* y árboles."]},
 {"t": "linea", "titulo": "LA HISTORIA DE LA PLAZA", "eventos": [{"fecha": "HACE MUCHO", "txt": "TIERRA", "emoji": "🟫"}, {"fecha": "DESPUÉS", "txt": "ÁRBOLES", "emoji": "🌳"}, {"fecha": "MÁS TARDE", "txt": "MONUMENTO", "emoji": "🗿"}, {"fecha": "HOY", "txt": "JUEGOS", "emoji": "🛝"}],
  "voz": ["Hace mucho, era de *tierra*.", "Después, plantaron *árboles*.", "Más tarde, pusieron un *monumento*.", "¡Hoy tiene *juegos*!"]},
 {"t": "pregunta", "pregunta": "¿Para qué sirve un monumento?", "opciones": ["PARA JUGAR", "PARA RECORDAR", "PARA COMER"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el monumento.", "¿Para qué sirve?", "¡Para *recordar* algo importante!"]},
 {"t": "consejo", "titulo": "PREGUNTÁ", "texto": "Los abuelos saben cómo era antes", "emoji": "👵",
  "voz": ["Truco: preguntá a los *abuelos* cómo era antes."]},
 {"t": "resumen", "items": [["MONUMENTO", "recuerda algo"], ["PLACA", "quién y cuándo"], ["CAMBIOS", "antes y hoy"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *monumento* recuerda algo importante.", "La *placa* dice quién y cuándo.", "El barrio *cambia* con el tiempo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
