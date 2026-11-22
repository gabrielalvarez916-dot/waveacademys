# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 2 · Animales por fuera: las 4 clases animadas.
Metáfora: el zoológico de Sofi. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-nat1-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0'
TEMA = 2
TIT = {1: 'Cubiertos de pelos, plumas o escamas', 2: 'Cómo se desplazan', 3: 'De qué se alimentan', 4: 'Agrupo animales por sus rasgos'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}

N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¿Qué viste en el zoológico?"}, {"yo": True, "txt": "¡UN OSO, UN LORO Y UN PEZ!"}, {"yo": False, "txt": "¿Y cómo eran?"}], "titulo": "ANIMALES", "sub": "por fuera",
  "voz": ["Tomi le escribe a Sofi.", "¿Qué viste en el zoológico?", "Un oso, un loro y un pez.", "Hoy: *de qué están cubiertos*."]},
 {"t": "matriz", "titulo": "¿DE QUÉ ESTÁN CUBIERTOS?", "celdas": [{"cab": "🐻 OSO", "txt": "PELOS"}, {"cab": "🦜 LORO", "txt": "PLUMAS"}, {"cab": "🐟 PEZ", "txt": "ESCAMAS"}, {"cab": "🐍 VÍBORA", "txt": "ESCAMAS"}],
  "voz": ["Cada animal tiene su *ropa*.", "El oso tiene *pelos*.", "El loro tiene *plumas*.", "El pez tiene *escamas*.", "¡La víbora también tiene *escamas*!"]},
 {"t": "zoom", "niveles": [{"emoji": "🐟", "txt": "UN PEZ"}, {"emoji": "🔍", "txt": "DE CERCA"}, {"emoji": "🔷", "txt": "ESCAMAS"}],
  "voz": ["Miramos un *pez*.", "Nos acercamos con la lupa.", "¡Vemos sus *escamas*!"]},
 {"t": "pregunta", "pregunta": "¿Quién tiene plumas?", "opciones": ["GATO", "GALLINA", "PEZ"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en las plumas.", "¿Quién tiene plumas?", "¡La *gallina*! Es un ave."]},
 {"t": "consejo", "titulo": "MIRÁ DE CERCA", "texto": "¿Pelos, plumas o escamas?", "emoji": "🔍",
  "voz": ["Truco: mirá la piel *de cerca*."]},
 {"t": "resumen", "items": [["PELOS", "oso, perro"], ["PLUMAS", "aves"], ["ESCAMAS", "peces, víboras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "El oso y el perro: *pelos*.", "Las aves: *plumas*.", "Peces y víboras: *escamas*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🦁", "lineas": ["Sofi pasea por el zoológico.", "Un mono salta y un pez nada.", "¡Cada uno se mueve distinto!"], "titulo": "CÓMO", "sub": "se mueven",
  "voz": ["Sofi pasea por el *zoológico*.", "Un mono salta y un pez nada.", "¡Cada uno se mueve *distinto*!", "Hoy: *cómo se mueven los animales*."]},
 {"t": "bloques", "titulo": "SE MUEVEN ASÍ", "items": [{"cab": "🐕 PERRO", "txt": "CAMINA"}, {"cab": "🐦 PÁJARO", "txt": "VUELA"}, {"cab": "🐟 PEZ", "txt": "NADA"}, {"cab": "🐸 RANA", "txt": "SALTA"}, {"cab": "🐍 VÍBORA", "txt": "REPTA"}],
  "voz": ["Miramos cómo se mueven.", "El perro *camina*.", "El pájaro *vuela*.", "El pez *nada*.", "La rana *salta*.", "La víbora se arrastra: *repta*."]},
 {"t": "comparar", "a": {"cab": "ALAS", "texto": "PARA VOLAR", "emoji": "🐦"}, "b": {"cab": "ALETAS", "texto": "PARA NADAR", "emoji": "🐟"}, "signo": "vs",
  "voz": ["El pájaro tiene *alas* para volar.", "El pez tiene *aletas* para nadar.", "¡Su cuerpo los ayuda a moverse!"]},
 {"t": "pregunta", "pregunta": "¿Cómo se mueve la víbora?", "opciones": ["VUELA", "REPTA", "SALTA"], "correcta": 1,
  "voz": ["Ahora vos. La víbora no tiene patas.", "¿Cómo se mueve?", "¡*Repta*! Se arrastra por el suelo."]},
 {"t": "resumen", "items": [["CAMINAR", "con patas"], ["VOLAR Y NADAR", "alas y aletas"], ["REPTAR", "arrastrarse"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Unos *caminan* con patas.", "Otros *vuelan* o *nadan*.", "Y otros *reptan*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Qué come el conejo?", "segundos": 6, "respuesta": "¡ZANAHORIAS!", "emoji": "🐰", "titulo": "QUÉ COMEN", "sub": "los animales",
  "voz": ["Desafío: ¿qué come el conejo?", "¡*Zanahorias* y pasto!", "Hoy: *qué comen los animales*."]},
 {"t": "venn", "a": "PLANTAS", "b": "ANIMALES", "itemsA": ["VACA", "CONEJO"], "itemsB": ["LEÓN", "TIBURÓN"], "ambos": ["GALLINA", "OSO"],
  "voz": ["Separamos por lo que *comen*.", "La vaca y el conejo comen *plantas*.", "El león y el tiburón comen *animales*.", "¡La gallina y el oso comen *de todo*!"]},
 {"t": "comparar", "a": {"cab": "VACA", "texto": "DIENTES CHATOS", "emoji": "🐄"}, "b": {"cab": "LEÓN", "texto": "DIENTES FILOSOS", "emoji": "🦁"}, "signo": "vs",
  "voz": ["La vaca tiene dientes *chatos*: muele pasto.", "El león tiene dientes *filosos*: corta carne.", "¡Los dientes nos dan una pista!"]},
 {"t": "pregunta", "pregunta": "¿Qué come el tiburón?", "opciones": ["PASTO", "PECES", "ZANAHORIAS"], "correcta": 1,
  "voz": ["Ahora vos. El tiburón vive en el mar.", "¿Qué come?", "¡*Peces*! Come otros animales."]},
 {"t": "consejo", "titulo": "MIRÁ LOS DIENTES", "texto": "Filosos o chatos", "emoji": "🦷",
  "voz": ["Truco: mirá los *dientes* del animal."]},
 {"t": "resumen", "items": [["PLANTAS", "vaca, conejo"], ["ANIMALES", "león, tiburón"], ["DE TODO", "gallina, oso"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Unos comen *plantas*.", "Otros comen *animales*.", "Y otros comen *de todo*.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "NOTICIAS DEL ZOO", "titular": "¡SE MEZCLARON LOS CARTELES!", "bajada": "Hay que armar los grupos", "emoji": "🦓", "titulo": "AGRUPAR", "sub": "animales",
  "voz": ["¡Noticias del zoológico! Se mezclaron los *carteles*.", "Hay que armar los grupos otra vez.", "Hoy: *agrupar animales*."]},
 {"t": "clasificar", "cajas": [{"cab": "PLUMAS", "emoji": "🪶"}, {"cab": "PELOS", "emoji": "🐾"}], "fichas": [{"txt": "LORO", "caja": 0}, {"txt": "PERRO", "caja": 1}, {"txt": "PATO", "caja": 0}, {"txt": "VACA", "caja": 1}],
  "voz": ["Agrupamos por su *cubierta*.", "En una caja, los de *plumas*.", "En la otra, los de *pelos*."]},
 {"t": "matriz", "titulo": "RASGOS DEL PATO", "celdas": [{"cab": "🪶", "txt": "PLUMAS"}, {"cab": "🚶", "txt": "CAMINA"}, {"cab": "🏊", "txt": "NADA"}, {"cab": "🕊️", "txt": "VUELA"}],
  "voz": ["Miramos los *rasgos* del pato.", "Tiene *plumas*.", "*Camina* con sus patas.", "*Nada* en la laguna.", "¡Y también *vuela*!"]},
 {"t": "venn", "a": "NADAN", "b": "VUELAN", "itemsA": ["PEZ", "DELFÍN"], "itemsB": ["PALOMA", "LORO"], "ambos": ["PATO"],
  "voz": ["Ahora agrupamos por cómo se *mueven*.", "El pez y el delfín *nadan*.", "La paloma y el loro *vuelan*.", "¡El pato está en los *dos grupos*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál no va con los de plumas?", "opciones": ["LORO", "GATO", "GALLINA"], "correcta": 1,
  "voz": ["Ahora vos. Loro, gato, gallina.", "¿Cuál no tiene plumas?", "¡El *gato*! Tiene pelos."]},
 {"t": "resumen", "items": [["RASGO", "algo que vemos"], ["GRUPO", "los que se parecen"], ["DOS GRUPOS", "el pato"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *rasgo* es algo que vemos.", "Un *grupo* junta los parecidos.", "Algunos van en *dos grupos*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Naturales 1", "titulo": TIT[n], "sub": f"Ciencias Naturales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
