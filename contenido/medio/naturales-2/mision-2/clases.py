# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 2 · Las crías de los animales: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Tomi, científico explorador con su lupa.
Genera tools/medio/clase/lecciones/medio-nat2-m2-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'cf56847a-8959-4695-bdff-0ea6841e4579', 2: '4beffacb-79a7-4256-a78a-6e5b3361fb5f', 3: 'cce13d4d-0bd0-4e84-a9e3-ef8ba7560c17', 4: 'ed4f5d1f-5c98-45aa-8934-ca2ee61c460a'}
TIT = {1: 'Nacen de huevos o de la panza', 2: 'Crías que se parecen a sus padres', 3: 'Quién cuida a las crías', 4: 'Animales que viven en grupo'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
TOMI = {"nombre": "Tomi", "emoji": "🧑‍🔬"}

N1 = [
 {"t": "historia", "personaje": TOMI, "lugar": "🐔", "lineas": ["Tomi visita la granja.", "¡La gallina puso huevos!", "Y la vaca tuvo un ternero."], "titulo": "CÓMO NACEN", "sub": "los animales",
  "voz": ["Tomi, el científico, visita la *granja*.", "¡La gallina puso *huevos*!", "Y la vaca tuvo un *ternero*.", "Hoy: *cómo nacen los animales*."]},
 {"t": "versus", "titulo": "DOS FORMAS DE NACER", "a": {"txt": "DE UN HUEVO", "emoji": "🥚", "datos": ["gallina", "pato", "tortuga"]}, "b": {"txt": "DE LA PANZA", "emoji": "🤰", "datos": ["perro", "gato", "vaca"]}, "gana": "empate", "veredicto": "¡Las dos son formas de nacer!",
  "voz": ["Hay dos formas de nacer.", "*De un huevo*: gallina, pato, tortuga.", "*De la panza* de la mamá: perro, gato, vaca.", "¡Las dos son formas de nacer!"]},
 {"t": "zoom", "niveles": [{"emoji": "🥚", "txt": "UN HUEVO"}, {"emoji": "🐣", "txt": "SE ROMPE"}, {"emoji": "🐥", "txt": "¡UN POLLITO!"}],
  "voz": ["Miramos de cerca un *huevo*.", "De a poco, *se rompe*.", "¡Sale un *pollito*!"]},
 {"t": "clasificar", "cajas": [{"cab": "DE HUEVO", "emoji": "🥚"}, {"cab": "DE LA PANZA", "emoji": "🤰"}], "fichas": [{"txt": "GALLINA", "caja": 0}, {"txt": "TORTUGA", "caja": 0}, {"txt": "GATO", "caja": 1}, {"txt": "OVEJA", "caja": 1}],
  "voz": ["Separamos los animales.", "Gallina y tortuga: nacen de *huevo*.", "Gato y oveja: nacen de la *panza*."]},
 {"t": "consejo", "titulo": "DOS FORMAS", "texto": "Huevo o panza: así nacen los animales", "emoji": "🔍",
  "voz": ["Truco: nacen de un *huevo* o de la *panza*."]},
 {"t": "resumen", "items": [["HUEVO", "gallina, pato, tortuga"], ["PANZA", "perro, gato, vaca"], ["CRÍA", "el animal bebé"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "De *huevo*: gallina, pato, tortuga.", "De la *panza*: perro, gato, vaca.", "La *cría* es el animal bebé.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "LAGUNA", "titular": "¡Un animal que cambia de forma!", "bajada": "Tomi lo encontró en la laguna", "emoji": "🐸", "titulo": "LAS CRÍAS", "sub": "¿se parecen?",
  "voz": ["¡Noticia: un animal que *cambia de forma*!", "Tomi lo encontró en la laguna.", "Hoy: *¿las crías se parecen a sus padres?*"]},
 {"t": "transforma", "titulo": "DEL RENACUAJO A LA RANA", "pasos": [{"txt": "RENACUAJO 🐟", "nota": "con cola"}, {"txt": "LE SALEN PATAS 🦵", "nota": "va cambiando"}, {"txt": "RANA 🐸", "nota": "¡adulta!"}],
  "voz": ["Primero es un *renacuajo*, con cola.", "Después le salen *patas*.", "¡Y se convierte en *rana*!"]},
 {"t": "pistas", "problema": "¿Qué cría es?", "pistas": ["Es chiquita y come hojas", "Arma un capullo", "Sale con alas de colores"], "respuesta": "LA ORUGA 🐛 → MARIPOSA 🦋",
  "voz": ["Adivinanza: ¿qué cría es?", "Pista uno: es chiquita y come hojas.", "Pista dos: arma un *capullo*.", "Pista tres: sale con alas de colores.", "¡La *oruga*, que se convierte en mariposa!"]},
 {"t": "pregunta", "pregunta": "¿Qué cría se parece a su mamá?", "opciones": ["EL PERRITO", "EL RENACUAJO"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué cría se parece a su mamá?", "Pensá en un perro chiquito.", "¡El *perrito*!"]},
 {"t": "consejo", "titulo": "MIRÁ BIEN", "texto": "Algunas crías cambian mucho", "emoji": "🔍",
  "voz": ["Truco: algunas crías *cambian mucho* al crecer."]},
 {"t": "resumen", "items": [["PARECIDAS", "perrito, potrillo"], ["CAMBIAN", "renacuajo, oruga"], ["CRECEN", "y se hacen adultos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Algunas crías son *parecidas*: perrito, potrillo.", "Otras *cambian*: renacuajo, oruga.", "Todas *crecen* y se hacen adultas.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Quién le da leche al ternero?", "segundos": 8, "respuesta": "¡La vaca, su mamá!", "emoji": "🐄", "titulo": "QUIÉN CUIDA", "sub": "a las crías",
  "voz": ["Desafío: ¿quién le da leche al ternero?", "¡La *vaca*, su mamá!", "Hoy: *quién cuida a las crías*."]},
 {"t": "personaje", "personaje": {"nombre": "Gallina Pepa", "emoji": "🐔"}, "lineas": [{"txt": "¡Hola! Yo cuido a mis pollitos.", "animo": "feliz"}, {"txt": "Los abrigo debajo de mis alas.", "animo": "piensa"}, {"txt": "¡Y les enseño a buscar comida!", "animo": "feliz"}],
  "voz": ["¡Hola! Yo cuido a mis pollitos.", "Los *abrigo* debajo de mis alas.", "¡Y les enseño a buscar *comida*!"]},
 {"t": "unir", "titulo": "¿CÓMO CUIDAN?", "pares": [["VACA 🐄", "da leche"], ["GALLINA 🐔", "abriga"], ["TORTUGA 🐢", "se va"]], "mezclar": True,
  "voz": ["Unimos cada mamá con lo que hace.", "La vaca: da *leche*.", "La gallina: *abriga*.", "La tortuga: ¡se va! Sus crías se arreglan solas."]},
 {"t": "pregunta", "pregunta": "¿Las tortuguitas tienen quien las cuide?", "opciones": ["NO, SE ARREGLAN SOLAS", "SÍ, LA MAMÁ"], "correcta": 0,
  "voz": ["Ahora vos: ¿quién cuida a las tortuguitas?", "Pensá en la arena…", "¡Nadie! Se *arreglan solas*."]},
 {"t": "consejo", "titulo": "CADA ANIMAL", "texto": "Cada uno cuida distinto a sus crías", "emoji": "🐾",
  "voz": ["Truco: cada animal cuida *distinto* a sus crías."]},
 {"t": "resumen", "items": [["CUIDAN", "vaca, gallina, hornero"], ["SOLAS", "tortuguitas"], ["CÓMO", "comida y abrigo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Algunas mamás *cuidan*: vaca, gallina, hornero.", "Las tortuguitas se arreglan *solas*.", "Cuidar es dar *comida* y *abrigo*.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Sofi", "emoji": "👧"}, "mensajes": [{"yo": False, "txt": "¡Vi muchas hormigas en fila! 🐜"}, {"yo": True, "txt": "¡Viven en grupo! Te cuento"}], "titulo": "EN GRUPO", "sub": "animales que viven juntos",
  "voz": ["Sofi le escribe: ¡vi muchas hormigas en fila!", "Tomi responde: ¡viven en grupo! Te cuento.", "Hoy: *animales que viven en grupo*."]},
 {"t": "documental", "emojis": ["🐜", "🐝", "🐑"], "lugar": "🌳", "rotulos": [{"txt": "HORMIGAS", "sub": "en el hormiguero"}, {"txt": "ABEJAS", "sub": "en la colmena"}, {"txt": "OVEJAS", "sub": "en el rebaño"}],
  "voz": ["Las *hormigas* viven en el hormiguero.", "Las *abejas* viven en la colmena.", "Las *ovejas* andan en rebaño."]},
 {"t": "escape", "titulo": "LA PUERTA DEL HORMIGUERO", "candados": [{"p": "Grupo de peces", "r": "CARDUMEN"}, {"p": "Casa de las abejas", "r": "COLMENA"}],
  "voz": ["¡Para entrar al hormiguero, abrimos los candados!", "Grupo de peces: *cardumen*.", "Casa de las abejas: *colmena*.", "¡Entramos!"]},
 {"t": "pregunta", "pregunta": "¿Para qué viven en grupo?", "opciones": ["PARA CUIDARSE Y COMER", "PARA PELEAR"], "correcta": 0,
  "voz": ["Ahora vos: ¿para qué viven en grupo?", "Pensá en las hormigas.", "¡Para *cuidarse* y buscar *comida* juntas!"]},
 {"t": "consejo", "titulo": "MIRÁ DE LEJOS", "texto": "No molestes a las hormigas ni a las abejas", "emoji": "👀",
  "voz": ["Truco: mirá de *lejos*, sin molestar."]},
 {"t": "resumen", "items": [["GRUPO", "viven juntos"], ["EJEMPLOS", "hormigas, abejas, ovejas"], ["SIRVE", "para cuidarse"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Algunos animales viven en *grupo*.", "Como hormigas, abejas y ovejas.", "Así se *cuidan* y buscan comida.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-nat2-m2-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Naturales 2", "titulo": TIT[n], "sub": f"Ciencias Naturales 2 · Misión 2 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
