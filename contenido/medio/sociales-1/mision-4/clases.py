# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 4 · Instituciones que cuidan a las personas: las 4 clases animadas.
Metáfora: los ayudantes del barrio. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 4
TIT = {1: 'Centros de salud y hospitales', 2: 'Bibliotecas y clubes del barrio', 3: 'Qué trabajo hace cada institución', 4: 'Respeto y cooperación en la convivencia'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Mañana me toca una vacuna!"}, {"yo": True, "txt": "¿VAS AL CENTRO DE SALUD?"}, {"yo": False, "txt": "Sí, con mi mamá."}], "titulo": "CENTROS DE SALUD", "sub": "y hospitales",
  "voz": ["Tomi le escribe a Sofi.", "¡Mañana me toca una *vacuna*!", "Va al *centro de salud* con su mamá.", "Hoy: *centros de salud y hospitales*."]},
 {"t": "causas", "causa": {"txt": "VAMOS AL CENTRO DE SALUD", "emoji": "🏥"}, "items": ["PARA VACUNARNOS", "PARA UN CONTROL", "SI ESTAMOS ENFERMOS"],
  "voz": ["¿Para qué vamos al *centro de salud*?", "Para *vacunarnos*.", "Para hacernos un *control*.", "Y cuando estamos *enfermos*."]},
 {"t": "bloques", "titulo": "QUIÉNES NOS CUIDAN", "items": [{"cab": "👩‍⚕️ MÉDICA", "txt": "NOS REVISA"}, {"cab": "🧑‍⚕️ ENFERMERO", "txt": "NOS VACUNA"}, {"cab": "🦷 DENTISTA", "txt": "CUIDA LOS DIENTES"}],
  "voz": ["Muchas personas nos *cuidan*.", "La médica nos *revisa*.", "El enfermero nos *vacuna*.", "El dentista cuida los *dientes*."]},
 {"t": "pregunta", "pregunta": "Te duele una muela. ¿Quién te ayuda?", "opciones": ["BOMBERO", "DENTISTA", "PANADERO"], "correcta": 1,
  "voz": ["Ahora vos. Te duele una muela.", "¿Quién te ayuda?", "¡El *dentista*!"]},
 {"t": "consejo", "titulo": "CON UN ADULTO", "texto": "Al médico se va acompañado", "emoji": "🧑",
  "voz": ["Recordá: al médico se va *con un adulto*."]},
 {"t": "resumen", "items": [["CENTRO DE SALUD", "cuida la salud"], ["TRABAJAN", "médicas, enfermeros"], ["VAMOS", "vacunas y controles"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *centro de salud* cuida la salud.", "Ahí trabajan *médicas* y enfermeros.", "Vamos para *vacunas* y controles.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📚", "lineas": ["Sofi va a la biblioteca.", "Elige un cuento de dragones.", "¡Se lo prestan para llevar!"], "titulo": "BIBLIOTECAS", "sub": "y clubes",
  "voz": ["Sofi va a la *biblioteca*.", "Elige un cuento de dragones.", "¡Se lo *prestan* para llevar!", "Hoy: *bibliotecas y clubes del barrio*."]},
 {"t": "comparar", "a": {"cab": "BIBLIOTECA", "texto": "LEER Y PEDIR LIBROS", "emoji": "📚"}, "b": {"cab": "CLUB", "texto": "HACER DEPORTE", "emoji": "⚽"}, "signo": "y",
  "voz": ["En la *biblioteca* leemos y pedimos libros.", "En el *club* hacemos deporte.", "¡Dos lugares del barrio!"]},
 {"t": "venn", "a": "BIBLIOTECA", "b": "CLUB", "itemsA": ["LEER", "PEDIR LIBROS"], "itemsB": ["NADAR", "JUGAR AL FÚTBOL"], "ambos": ["ENCONTRARNOS"],
  "voz": ["Separamos lo que hacemos en cada uno.", "En la biblioteca: *leer* y pedir libros.", "En el club: *nadar* y jugar.", "¡En los dos nos *encontramos* con otros!"]},
 {"t": "pregunta", "pregunta": "¿Dónde nadás?", "opciones": ["BIBLIOTECA", "CLUB", "HOSPITAL"], "correcta": 1,
  "voz": ["Ahora vos. Querés nadar.", "¿Adónde vas?", "¡Al *club*!"]},
 {"t": "consejo", "titulo": "DEVOLVÉ A TIEMPO", "texto": "Así otro chico también lo lee", "emoji": "📖",
  "voz": ["Truco: devolvé el libro *a tiempo*."]},
 {"t": "resumen", "items": [["BIBLIOTECA", "leer y pedir libros"], ["CLUB", "deporte"], ["LOS DOS", "para encontrarnos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En la *biblioteca* leemos.", "En el *club* hacemos deporte.", "En los dos nos *encontramos*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Quién apaga un incendio?", "segundos": 6, "respuesta": "¡LOS BOMBEROS!", "emoji": "🚒", "titulo": "CADA INSTITUCIÓN", "sub": "su trabajo",
  "voz": ["Desafío: ¿quién apaga un incendio?", "¡Los *bomberos*!", "Hoy: *qué trabajo hace cada institución*."]},
 {"t": "matriz", "titulo": "¿QUÉ HACE CADA UNA?", "celdas": [{"cab": "🏫 ESCUELA", "txt": "ENSEÑA"}, {"cab": "🏥 HOSPITAL", "txt": "CURA"}, {"cab": "🚒 BOMBEROS", "txt": "APAGAN FUEGO"}, {"cab": "📚 BIBLIOTECA", "txt": "PRESTA LIBROS"}],
  "voz": ["Cada institución tiene su *trabajo*.", "La escuela *enseña*.", "El hospital *cura*.", "Los bomberos *apagan* el fuego.", "La biblioteca *presta* libros."]},
 {"t": "corrige", "titulo": "¿ESTÁ BIEN?", "cambios": [{"antes": "EL HOSPITAL PRESTA LIBROS", "despues": "LA BIBLIOTECA PRESTA LIBROS", "motivo": "el hospital cura"}, {"antes": "LA ESCUELA APAGA INCENDIOS", "despues": "LOS BOMBEROS APAGAN INCENDIOS", "motivo": "la escuela enseña"}],
  "voz": ["¡Ups! Hay frases mezcladas.", "La que presta libros es la *biblioteca*.", "Los que apagan incendios son los *bomberos*."]},
 {"t": "pregunta", "pregunta": "Me quebré un brazo. ¿Adónde voy?", "opciones": ["CLUB", "HOSPITAL", "BIBLIOTECA"], "correcta": 1,
  "voz": ["Ahora vos. Te quebraste un brazo.", "¿Adónde vas?", "¡Al *hospital*!"]},
 {"t": "consejo", "titulo": "AVISÁ A UN ADULTO", "texto": "En una emergencia, avisá enseguida", "emoji": "🚨",
  "voz": ["Importante: en una emergencia, avisá a un *adulto*."]},
 {"t": "resumen", "items": [["INSTITUCIONES", "trabajan para todos"], ["CADA UNA", "su trabajo"], ["AYUDAN", "a todos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *instituciones* trabajan para todos.", "Cada una tiene *su trabajo*.", "¡Nos *ayudan* a todos!", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡EL GRADO LIMPIÓ LA PLAZA!", "bajada": "Lo hicieron entre todos", "emoji": "🤝", "titulo": "RESPETO", "sub": "y cooperación",
  "voz": ["¡Último momento! El grado limpió la *plaza*.", "Lo hicieron *entre todos*.", "Hoy: *respeto y cooperación*."]},
 {"t": "antesdespues", "antes": {"cab": "CADA UNO SOLO", "emoji": "😓", "texto": "Cuesta mucho"}, "despues": {"cab": "ENTRE TODOS", "emoji": "😃", "texto": "¡Sale rápido!"},
  "voz": ["Solos, las cosas *cuestan* mucho.", "Entre todos, ¡salen *rápido*!"]},
 {"t": "ciclo", "titulo": "PARA CONVIVIR", "items": ["ESCUCHO", "RESPETO", "AYUDO", "COMPARTO"],
  "voz": ["Así convivimos *bien*.", "*Escucho* al otro.", "Lo *respeto*.", "Lo *ayudo*.", "Y *comparto*. ¡Y vuelta a empezar!"]},
 {"t": "pregunta", "pregunta": "Un compañero se burla de otro. ¿Qué hacés?", "opciones": ["ME RÍO", "AVISO A UN ADULTO", "NADA"], "correcta": 1,
  "voz": ["Ahora vos. Alguien se burla de otro.", "¿Qué hacés?", "¡Aviso a un *adulto*! Las burlas lastiman."]},
 {"t": "consejo", "titulo": "PONETE EN SU LUGAR", "texto": "Pensá cómo se siente el otro", "emoji": "💛",
  "voz": ["Truco: pensá cómo se *siente* el otro."]},
 {"t": "resumen", "items": [["RESPETO", "tratar bien"], ["COOPERAR", "ayudarnos"], ["CONVIVIR", "estar bien juntos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Respetar* es tratar bien.", "*Cooperar* es ayudarnos.", "Así *convivimos* mejor.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
