# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 8 · Distintas costumbres, mismos derechos: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (entrevista a familias de distintos lugares).
Genera tools/medio/clase/lecciones/medio-soc2-m8-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '06f0cb57-392a-4de4-894f-f723f608277b', 2: 'ee42f41a-3a19-47ce-8db9-bb571e7df302', 3: 'f8b9ef7c-f72b-4959-ac89-bb7a4af0ae4d', 4: '240f9df3-52ba-47ac-a5be-694a5d114781'}
TIT = {1: 'Crianza, comidas y ropa en distintas culturas', 2: 'Historias de vida y cuentos que se heredan', 3: 'Prejuicios y discriminación', 4: 'Carnaval y otras fiestas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
LOLA = {"nombre": "Lola", "emoji": "👧🎤"}

N1 = [
 {"t": "historia", "personaje": LOLA, "lugar": "🏘️", "lineas": ["Lola recorre su barrio.", "Hay familias de muchos lugares.", "¡Cada una tiene sus costumbres!"], "titulo": "DISTINTAS", "sub": "culturas",
  "voz": ["Lola recorre su *barrio* con el micrófono.", "Viven familias de *muchos lugares*.", "¡Cada una tiene sus costumbres!", "Hoy: *distintas culturas*."]},
 {"t": "unir", "titulo": "¿CÓMO LLEVAN AL BEBÉ?", "pares": [["AGUAYO", "a la espalda"], ["COCHECITO", "con ruedas"], ["MOCHILA DE TELA", "adelante"]], "mezclar": True,
  "voz": ["Hay muchas formas de llevar a un bebé.", "En un *aguayo*, a la espalda.", "En un *cochecito*, con ruedas.", "En una *mochila de tela*, adelante."]},
 {"t": "quiz4", "pregunta": "¿Cuál de estas comidas es de una cultura?", "opciones": ["TODAS", "SOLO LAS EMPANADAS", "SOLO LAS AREPAS", "NINGUNA"], "correcta": 0,
  "voz": ["Empanadas, arepas, tortillas: ¿cuál es de una *cultura*?", "Pensá en las familias del barrio.", "¡*Todas*! Cada comida es de una cultura."]},
 {"t": "pasos", "titulo": "LA FAMILIA DE YANINA", "items": [{"txt": "Usa aguayo", "emoji": "🧣"}, {"txt": "Come sopa de maní", "emoji": "🥣"}, {"txt": "Usa ponchos", "emoji": "🧥"}],
  "voz": ["Lola entrevista a la familia de *Yanina*.", "Yanina lleva a su hermanito en *aguayo*.", "En su casa comen *sopa de maní*.", "Y en invierno usan *ponchos* de colores."]},
 {"t": "pregunta", "pregunta": "¿Una costumbre es mejor que otra?", "opciones": ["NO, SON DISTINTAS", "SÍ"], "correcta": 0,
  "voz": ["Ahora vos: ¿una costumbre es mejor que otra?", "Pensá en el barrio de Lola.", "¡*No*! Son distintas, y todas valen."]},
 {"t": "consejo", "titulo": "DISTINTO NO ES PEOR", "texto": "Cada costumbre es valiosa", "emoji": "🌈",
  "voz": ["Truco: *distinto* no es peor."]},
 {"t": "resumen", "items": [["CULTURA", "forma de vivir"], ["COSTUMBRES", "comida, ropa, crianza"], ["DERECHOS", "los mismos para todos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *cultura* es la forma de vivir.", "Hay *costumbres* de comida, ropa y crianza.", "Y todos tenemos los mismos *derechos*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Doña Rosa", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "¿Querés que te cuente mi historia? 📖"}, {"yo": True, "txt": "¡Sí! Traigo el micrófono"}], "titulo": "HISTORIAS", "sub": "que se heredan",
  "voz": ["Doña Rosa escribe: ¿querés que te cuente mi historia?", "Lola responde: ¡sí, traigo el *micrófono*!", "Hoy: *historias y cuentos que se heredan*."]},
 {"t": "personaje", "personaje": {"nombre": "Doña Rosa", "emoji": "👵"}, "lineas": [{"txt": "Nací en el campo, hace muchos años.", "animo": "feliz"}, {"txt": "Viajé en tren hasta la ciudad.", "animo": "piensa"}, {"txt": "Trabajé de costurera.", "animo": "feliz"}, {"txt": "¡Y hoy soy abuela!", "animo": "sorpresa"}],
  "voz": ["Nací en el *campo*, hace muchos años.", "Viajé en *tren* hasta la ciudad.", "Trabajé de *costurera*.", "¡Y hoy soy *abuela*!"]},
 {"t": "transforma", "titulo": "EL CUENTO VIAJA", "pasos": [{"txt": "ABUELA 👵", "nota": "lo cuenta"}, {"txt": "MAMÁ 👩", "nota": "lo aprende"}, {"txt": "LOLA 👧", "nota": "¡lo hereda!"}],
  "voz": ["La *abuela* le contó un cuento a la mamá.", "La *mamá* lo aprendió y lo guardó.", "¡Hoy se lo cuenta a *Lola*: lo heredó!"]},
 {"t": "pasos", "titulo": "UNA ENTREVISTA", "items": [{"txt": "¿Dónde naciste?", "emoji": "🏡"}, {"txt": "¿En qué trabajaste?", "emoji": "🧵"}, {"txt": "Ordeno lo que contó", "emoji": "📝"}],
  "voz": ["¿Cómo armamos una historia de vida? Paso a paso.", "Pregunto: ¿*dónde* naciste?", "Pregunto: ¿en qué *trabajaste*?", "Después *ordeno* todo lo que me contó."]},
 {"t": "pregunta", "pregunta": "¿Qué es heredar un cuento?", "opciones": ["RECIBIRLO DE LOS MAYORES", "COMPRARLO"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué es heredar un cuento?", "Pensá en la abuela.", "¡Recibirlo de los *mayores*!"]},
 {"t": "consejo", "titulo": "ESCUCHÁ", "texto": "Las historias de los mayores enseñan", "emoji": "👂",
  "voz": ["Truco: *escuchá* las historias de los mayores."]},
 {"t": "resumen", "items": [["HISTORIA DE VIDA", "lo que le pasó a alguien"], ["HEREDAR", "recibir de los mayores"], ["CUENTOS", "de abuelos a nietos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *historia de vida* cuenta lo que pasó.", "*Heredar* es recibir de los mayores.", "Los *cuentos* pasan de abuelos a nietos.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Llega un chico nuevo. ¿Ya sabés cómo es?", "segundos": 8, "respuesta": "¡No! Primero hay que conocerlo", "emoji": "🧒", "titulo": "PREJUICIOS", "sub": "y discriminación",
  "voz": ["Desafío: llega un chico nuevo. ¿Ya sabés cómo es?", "¡No! Primero hay que *conocerlo*.", "Hoy: *prejuicios y discriminación*."]},
 {"t": "comparar", "a": {"cab": "PREJUICIO", "texto": "OPINO SIN CONOCER", "emoji": "🙈"}, "b": {"cab": "CONOCER", "texto": "PREGUNTO Y JUEGO", "emoji": "🤗"}, "signo": "↔",
  "voz": ["Comparamos dos formas de actuar.", "*Prejuicio*: opino sin conocer a la persona.", "*Conocer*: pregunto, escucho y juego con ella."]},
 {"t": "vof", "afirmacion": "Se puede dejar afuera a alguien por hablar otro idioma", "emoji": "🗣️", "verdadero": False, "explicacion": "Eso es discriminar",
  "voz": ["¿Verdadero o falso? Se deja afuera por el idioma.", "Pensá en los derechos…", "¡*Falso*! Eso es *discriminar*, y está mal."]},
 {"t": "pasos", "titulo": "LOLA Y KENJI", "items": [{"txt": "Llega Kenji", "emoji": "🧒"}, {"txt": "Lola lo invita", "emoji": "🤝"}, {"txt": "Juegan juntos", "emoji": "⚽"}, {"txt": "¡Son amigos!", "emoji": "💛"}],
  "voz": ["Veamos qué pasó con Kenji.", "Kenji llega al grado y habla *poco* castellano.", "Lola lo *invita* a jugar.", "Juegan *juntos* al fútbol.", "¡Y se hacen *amigos*!"]},
 {"t": "pregunta", "pregunta": "Si ves que discriminan a alguien, ¿qué hacés?", "opciones": ["AVISO A UN ADULTO", "ME RÍO"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué hacés si discriminan a alguien?", "Pensá en cuidar al otro.", "¡Aviso a un *adulto*!"]},
 {"t": "consejo", "titulo": "PRIMERO CONOCÉ", "texto": "Preguntá y escuchá antes de opinar", "emoji": "💬",
  "voz": ["Truco: primero *conocé*, después opiná."]},
 {"t": "resumen", "items": [["PREJUICIO", "opinar sin conocer"], ["DISCRIMINAR", "dejar afuera"], ["RESPETAR", "invitar y conocer"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *prejuicio* es opinar sin conocer.", "*Discriminar* es dejar afuera por ser distinto.", "*Respetar* es invitar y conocer.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "FIESTA", "titular": "¡Llegó el carnaval al barrio!", "bajada": "Murgas, disfraces y espuma", "emoji": "🎭", "titulo": "CARNAVAL", "sub": "y otras fiestas",
  "voz": ["¡Noticia: llegó el *carnaval* al barrio!", "Hay murgas, disfraces y espuma.", "Hoy: *carnaval y otras fiestas*."]},
 {"t": "documental", "emojis": ["🥁", "🪶", "🎭"], "lugar": "🎉", "rotulos": [{"txt": "MURGA", "sub": "canta y baila"}, {"txt": "COMPARSA", "sub": "desfila con plumas"}, {"txt": "DISFRACES", "sub": "y máscaras"}],
  "voz": ["La *murga* canta y baila con bombos.", "La *comparsa* desfila con plumas y brillos.", "Y todos se ponen *disfraces* y máscaras."]},
 {"t": "memoria", "titulo": "FIESTAS", "items": ["CARNAVAL", "AÑO NUEVO CHINO", "PACHAMAMA", "CUMPLEAÑOS"], "falta": 2,
  "voz": ["Mirá estas fiestas de muchas culturas.", "Se tapan… ¡y una desapareció!", "¡Faltaba la *Pachamama*: la madre tierra!"]},
 {"t": "pasos", "titulo": "EL TRAJE DE LOLA", "items": [{"txt": "Elige colores", "emoji": "🎨"}, {"txt": "Cose lentejuelas", "emoji": "🧵"}, {"txt": "Ensaya el baile", "emoji": "💃"}, {"txt": "¡Sale con la murga!", "emoji": "🥁"}],
  "voz": ["Lola prepara su traje de murga, paso a paso.", "Primero *elige* los colores.", "Después le cose *lentejuelas* brillantes.", "*Ensaya* el baile con sus amigos.", "¡Y sale a bailar con la *murga*!"]},
 {"t": "pregunta", "pregunta": "¿Qué fiesta se festeja con dragones?", "opciones": ["AÑO NUEVO CHINO", "CARNAVAL"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué fiesta tiene dragones?", "Pensá en otras culturas.", "¡El *Año Nuevo chino*!"]},
 {"t": "consejo", "titulo": "COMPARTÍ", "texto": "Invitá a tus amigos a tus fiestas", "emoji": "🎊",
  "voz": ["Truco: *compartí* tus fiestas con tus amigos."]},
 {"t": "resumen", "items": [["CARNAVAL", "música y disfraces"], ["MURGA", "canta y baila"], ["OTRAS FIESTAS", "cada cultura, la suya"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El *carnaval* tiene música y disfraces.", "La *murga* canta y baila.", "Cada cultura tiene sus *fiestas*. ¡Todas valen!", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m8-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 8 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
