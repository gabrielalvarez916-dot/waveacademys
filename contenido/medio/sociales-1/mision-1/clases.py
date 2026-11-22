# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 1 · Mi familia y las familias de hoy: las 4 clases animadas.
Metáfora: el álbum de las familias. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 1
TIT = {1: 'Familias de distintos tipos', 2: 'Quién hace qué en casa', 3: 'Las viviendas y sus materiales', 4: 'Mi historia familiar en un álbum'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📷", "lineas": ["Sofi lleva una foto al grado.", "Está con su mamá y su abuela.", "¡Es su familia!"], "titulo": "LAS FAMILIAS", "sub": "de distintos tipos",
  "voz": ["Sofi lleva una *foto* al grado.", "Está con su mamá y su abuela.", "¡Es su *familia*!", "Hoy: *familias de distintos tipos*."]},
 {"t": "matriz", "titulo": "FAMILIAS DEL GRADO", "celdas": [{"cab": "👧 SOFI", "txt": "MAMÁ Y ABUELA"}, {"cab": "👦 TOMI", "txt": "MAMÁ, PAPÁ Y HERMANA"}, {"cab": "🧒 LU", "txt": "PAPÁ"}, {"cab": "👶 MATI", "txt": "ABUELOS Y PRIMOS"}],
  "voz": ["Cada chico del grado trae su foto.", "Sofi vive con su *mamá* y su *abuela*.", "Tomi, con mamá, papá y su *hermana*.", "Lu vive con su *papá*.", "Mati, con sus *abuelos* y primos."]},
 {"t": "comparar", "a": {"cab": "FAMILIA GRANDE", "texto": "MUCHAS PERSONAS", "emoji": "👨‍👩‍👧‍👦"}, "b": {"cab": "FAMILIA CHICA", "texto": "POCAS PERSONAS", "emoji": "👨‍👧"}, "signo": "y",
  "voz": ["Hay familias *grandes*.", "Y hay familias *chicas*.", "¡Todas se quieren y se *cuidan*!"]},
 {"t": "pregunta", "pregunta": "Lu vive con su papá. ¿Es una familia?", "opciones": ["SÍ", "NO", "A MEDIAS"], "correcta": 0,
  "voz": ["Ahora vos. Lu vive con su papá.", "¿Es una familia?", "¡*Sí*! Se quieren y se cuidan."]},
 {"t": "consejo", "titulo": "TODAS VALEN", "texto": "Ninguna familia es mejor que otra", "emoji": "💛",
  "voz": ["Recordá: *todas* las familias valen."]},
 {"t": "resumen", "items": [["FAMILIA", "se quieren y se cuidan"], ["DISTINTAS", "grandes y chicas"], ["RESPETO", "todas valen"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Una *familia* se quiere y se cuida.", "Hay familias *distintas*.", "Y las *respetamos* a todas.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Qué hacés?"}, {"yo": True, "txt": "¡PONGO LA MESA PARA CENAR!"}, {"yo": False, "txt": "¡Yo guardo los juguetes!"}], "titulo": "QUIÉN HACE QUÉ", "sub": "en casa",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué hacés?", "Sofi pone la *mesa* para cenar.", "Hoy: *quién hace qué en casa*."]},
 {"t": "bloques", "titulo": "LAS TAREAS", "items": [{"cab": "🍳", "txt": "COCINAR"}, {"cab": "🧺", "txt": "LAVAR"}, {"cab": "🧹", "txt": "ORDENAR"}, {"cab": "🛒", "txt": "COMPRAR"}],
  "voz": ["En casa hay muchas *tareas*.", "Hay que *cocinar*.", "Hay que *lavar*.", "Hay que *ordenar*.", "Y hacer las *compras*."]},
 {"t": "antesdespues", "antes": {"cab": "ANTES", "emoji": "🧸", "texto": "Juguetes por todos lados"}, "despues": {"cab": "ENTRE TODOS", "emoji": "✨", "texto": "¡Todo ordenado!"},
  "voz": ["La pieza estaba *desordenada*.", "Entre todos la *ordenamos* rápido."]},
 {"t": "pregunta", "pregunta": "¿Quién puede ayudar en casa?", "opciones": ["SOLO MAMÁ", "TODOS", "NADIE"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en tu casa.", "¿Quién puede ayudar?", "¡*Todos*, grandes y chicos!"]},
 {"t": "consejo", "titulo": "CON CUIDADO", "texto": "El horno y los cuchillos son para grandes", "emoji": "⚠️",
  "voz": ["Importante: el *horno* es para los grandes."]},
 {"t": "resumen", "items": [["TAREAS", "cocinar, lavar, ordenar"], ["TODOS", "grandes y chicos"], ["YO", "pongo la mesa"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En casa hay muchas *tareas*.", "Las hacemos *entre todos*.", "Y *vos* también podés ayudar.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Dónde vive una familia?", "segundos": 6, "respuesta": "¡EN UNA VIVIENDA!", "emoji": "🏠", "titulo": "LAS VIVIENDAS", "sub": "y sus materiales",
  "voz": ["Desafío: ¿dónde vive una familia?", "¡En una *vivienda*!", "Hoy: *las viviendas y sus materiales*."]},
 {"t": "partes", "emoji": "🏠", "titulo": "LA CASA DE TOMI", "partes": [{"txt": "TECHO: CHAPA", "x": 0.2, "y": -0.8}, {"txt": "PARED: LADRILLO", "x": -0.6, "y": 0.0}, {"txt": "PUERTA: MADERA", "x": 0.3, "y": 0.6}, {"txt": "VENTANA: VIDRIO", "x": 0.6, "y": 0.0}],
  "voz": ["Miramos la casa de *Tomi*.", "El *techo* es de chapa.", "La *pared* es de ladrillo.", "La *puerta* es de madera.", "La *ventana* es de vidrio."]},
 {"t": "comparar", "a": {"cab": "CASA", "texto": "CON PATIO", "emoji": "🏡"}, "b": {"cab": "DEPARTAMENTO", "texto": "EN UN EDIFICIO", "emoji": "🏢"}, "signo": "y",
  "voz": ["Algunas familias viven en una *casa*.", "Otras viven en un *departamento*.", "¡Las dos son *viviendas*!"]},
 {"t": "pregunta", "pregunta": "¿De qué es la pared?", "opciones": ["PAPEL", "LADRILLO", "TELA"], "correcta": 1,
  "voz": ["Ahora vos. La pared es dura y fuerte.", "¿De qué está hecha?", "¡De *ladrillo*!"]},
 {"t": "consejo", "titulo": "NOS PROTEGEN", "texto": "Todas las viviendas nos cuidan", "emoji": "🛡️",
  "voz": ["Recordá: todas las viviendas nos *protegen*."]},
 {"t": "resumen", "items": [["VIVIENDA", "donde vivimos"], ["TIPOS", "casa, departamento"], ["MATERIALES", "ladrillo, madera, chapa"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *vivienda* es donde vivimos.", "Hay casas y *departamentos*.", "Se hacen con distintos *materiales*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SOFI ARMA SU ÁLBUM!", "bajada": "Con su historia desde bebé", "emoji": "📒", "titulo": "MI HISTORIA", "sub": "en un álbum",
  "voz": ["¡Último momento! Sofi arma su *álbum*.", "Con su historia desde que era *bebé*.", "Hoy: *mi historia familiar*."]},
 {"t": "linea", "titulo": "LA HISTORIA DE SOFI", "eventos": [{"fecha": "1", "txt": "NACÍ", "emoji": "👶"}, {"fecha": "2", "txt": "PRIMEROS PASOS", "emoji": "🚶"}, {"fecha": "3", "txt": "JARDÍN", "emoji": "🎨"}, {"fecha": "4", "txt": "PRIMER GRADO", "emoji": "🎒"}],
  "voz": ["Primero, Sofi *nació*.", "Después, dio sus *primeros pasos*.", "Fue al *jardín*.", "¡Y ahora está en *primer grado*!"]},
 {"t": "flujo", "titulo": "CÓMO ARMO EL ÁLBUM", "items": ["BUSCO FOTOS", "PREGUNTO EN CASA", "ORDENO", "PEGO"],
  "voz": ["Primero, *busco* fotos.", "Después, *pregunto* en casa.", "Las *ordeno*: de antes a ahora.", "Y las *pego*."]},
 {"t": "pregunta", "pregunta": "¿Qué foto va primero?", "opciones": ["PRIMER GRADO", "NACÍ", "JARDÍN"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en el orden.", "¿Qué foto va primero?", "¡Cuando *naciste*!"]},
 {"t": "consejo", "titulo": "SIN FOTOS", "texto": "Si no hay fotos, hacé dibujos", "emoji": "🖍️",
  "voz": ["Truco: si no hay fotos, hacé *dibujos*."]},
 {"t": "resumen", "items": [["HISTORIA", "desde que nací"], ["PREGUNTAR", "a la familia"], ["ORDENAR", "antes y después"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Mi *historia* empieza cuando nací.", "*Pregunto* a mi familia.", "Y *ordeno* de antes a ahora.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
