# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 14 · Singular y plural: las 4 clases animadas.
Vía fonológica: la voz no nombra letras (dice «se agrega el sonido sss» / «se agrega es»). Metáfora: el cuaderno viajero de Sofi en la granja.
Genera tools/medio/clase/lecciones/medio-leng2-m14-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'ed97ba02-b3f0-41fb-9904-0576793146bf', 2: '7ec301f3-24b5-43dd-886e-95c15134bc8c', 3: 'd63e52b8-3f55-4f1f-bc38-9fd5efc47976', 4: '40e7990c-0f1f-4119-820b-84bab8be5e09'}
TIT = {1: 'Uno y varios', 2: 'Plural con S y ES', 3: 'Concordar sustantivo y adjetivo', 4: 'Corregir oraciones'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🦆", "lineas": ["Sofi ve un pato en la laguna.", "¡Después llegan más!", "¿Cómo lo escribe?"], "titulo": "UNO", "sub": "y varios",
  "voz": ["Sofi ve *un pato* en la laguna.", "¡Después llegan *muchos más*!", "¿Cómo lo escribe?", "Hoy: *uno y varios*."]},
 {"t": "transforma", "titulo": "DE UNO A VARIOS", "pasos": [{"txt": "EL PATO", "nota": "uno: singular"}, {"txt": "LOS PATOS", "nota": "varios: plural"}],
  "voz": ["*El pato*: uno solo. Es *singular*.", "*Los patos*: varios. Es *plural*."]},
 {"t": "definicion", "palabra": "Singular y plural", "texto": "Singular: uno. Plural: varios", "emoji": "🔢",
  "voz": ["*Singular* nombra uno solo.", "*Plural* nombra varios."]},
 {"t": "quiz4", "pregunta": "¿Cuál está en plural?", "opciones": ["LA RANA", "LAS RANAS", "EL SOL", "LA FLOR"], "correcta": 1,
  "voz": ["¿Cuál nombra *varios*?", "Escuchá el final…", "¡*Las ranas*!"]},
 {"t": "consejo", "titulo": "¿CUÁNTOS?", "texto": "Uno: singular. Varios: plural", "emoji": "🖐️",
  "voz": ["Truco: preguntá *¿cuántos?*"]},
 {"t": "resumen", "items": [["SINGULAR", "uno solo"], ["PLURAL", "varios"], ["CAMBIAN", "EL → LOS, LA → LAS"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Singular*: uno solo.", "*Plural*: varios.", "También cambian *el* y *la*: *los* y *las*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¡Vi tres FLORS! 🌸"}, {"yo": True, "txt": "Mmm… ¿así se escribe?"}], "titulo": "PLURAL", "sub": "con S y ES",
  "voz": ["Tomi le escribe: ¡vi tres flores!", "Sofi mira cómo lo escribió…", "Hoy: *cómo se forma el plural*."]},
 {"t": "clasificar", "cajas": [{"cab": "+ S", "emoji": "🏠"}, {"cab": "+ ES", "emoji": "🌸"}], "fichas": [{"txt": "CASA → CASAS", "caja": 0}, {"txt": "PATO → PATOS", "caja": 0}, {"txt": "FLOR → FLORES", "caja": 1}, {"txt": "PAN → PANES", "caja": 1}],
  "voz": ["Separamos las palabras.", "Casa y pato terminan en vocal: sumamos *sss*.", "Flor y pan terminan distinto: sumamos *es*."]},
 {"t": "contrarreloj", "titulo": "PLURAL RÁPIDO", "segundos": 20, "items": [{"p": "MESA", "r": "MESAS"}, {"p": "SOL", "r": "SOLES"}, {"p": "RATÓN", "r": "RATONES"}],
  "voz": ["¡Plural rápido!", "Mesa: *mesas*.", "Sol: *soles*.", "Ratón: *ratones*."]},
 {"t": "escape", "titulo": "LA PUERTA DEL GALLINERO", "candados": [{"p": "LORO →", "r": "LOROS"}, {"p": "FLOR →", "r": "FLORES"}],
  "voz": ["¡Para abrir el gallinero, decimos el plural!", "Loro: *loros*.", "Flor: *flores*.", "¡Abrimos!"]},
 {"t": "consejo", "titulo": "MIRÁ EL FINAL", "texto": "Vocal: S. Consonante: ES", "emoji": "👀",
  "voz": ["Truco: mirá cómo *termina* la palabra."]},
 {"t": "resumen", "items": [["VOCAL", "agregar S"], ["CONSONANTE", "agregar ES"], ["EJEMPLOS", "CASAS, FLORES"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Si termina en *vocal*, sumamos *sss*.", "Si no, sumamos *es*.", "Como en *casas* y *flores*.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "GRANJA", "titular": "¡Las palabras se pelean!", "bajada": "Una dice uno y otra dice varios", "emoji": "😤", "titulo": "CONCORDAR", "sub": "ir juntos",
  "voz": ["¡Noticia: las palabras se pelean!", "Una dice *uno* y otra dice *varios*.", "Hoy: *concordar*."]},
 {"t": "definicion", "palabra": "Concordar", "texto": "Sustantivo y adjetivo van juntos", "emoji": "🤝",
  "voz": ["*Concordar* es ir juntos.", "Si el sustantivo es plural, el adjetivo también."]},
 {"t": "unir", "titulo": "CADA UNO CON SU PAREJA", "pares": [["LOS PATOS", "BLANCOS"], ["LA FLOR", "ROJA"], ["LOS RATONES", "GRISES"]],
  "voz": ["Unimos cada uno con su adjetivo.", "Los patos *blancos*.", "La flor *roja*.", "Los ratones *grises*."]},
 {"t": "completa", "antes": "LAS RANAS", "despues": "", "opciones": ["VERDES", "VERDE"], "correcta": 0,
  "voz": ["Completá: las ranas…", "¿Verde o verdes?", "¡*Verdes*! Las dos en plural."]},
 {"t": "consejo", "titulo": "LOS DOS JUNTOS", "texto": "Si uno cambia, cambia el otro", "emoji": "👯",
  "voz": ["Truco: si uno cambia, cambia *el otro*."]},
 {"t": "resumen", "items": [["CONCORDAR", "ir juntos"], ["SINGULAR", "EL PATO BLANCO"], ["PLURAL", "LOS PATOS BLANCOS"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Concordar* es ir juntos.", "*El pato blanco*: todo singular.", "*Los patos blancos*: todo plural.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "¿Qué está mal? LOS GATO DUERMEN", "segundos": 8, "respuesta": "¡LOS GATOS DUERMEN!", "emoji": "🐱", "titulo": "CORREGIR", "sub": "oraciones",
  "voz": ["Desafío: ¿qué está mal? Los gato duermen.", "¡*Los gatos* duermen!", "Hoy: *corregir oraciones*."]},
 {"t": "corrige", "titulo": "SOFI CORRIGE", "cambios": [{"antes": "LOS GATO", "despues": "LOS GATOS", "motivo": "son varios"}, {"antes": "LA FLORES", "despues": "LAS FLORES", "motivo": "todo en plural"}, {"antes": "EL NIDOS", "despues": "EL NIDO", "motivo": "es uno solo"}],
  "voz": ["¡Encontramos errores!", "Los gatos: son *varios*.", "Las flores: todo en *plural*.", "El nido: es *uno solo*."]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Mezclado", "emoji": "🌀"}, "preguntas": [{"p": "LOS LORO HABLAN", "r": "LOS LOROS HABLAN"}, {"p": "LAS NUBE BLANCAS", "r": "LAS NUBES BLANCAS"}],
  "voz": ["¡Apareció el *Monstruo Mezclado*!", "Corregimos sus oraciones.", "*Los loros* hablan.", "¡*Las nubes blancas*! ¡Ganamos!"]},
 {"t": "pasos", "titulo": "CÓMO REVISO", "items": [{"txt": "¿Uno o varios?", "emoji": "🔢"}, {"txt": "¿Todas dicen lo mismo?", "emoji": "🤝"}, {"txt": "Corrijo", "emoji": "✏️"}],
  "voz": ["¿Cómo revisamos?", "¿Es *uno* o *varios*?", "¿Todas las palabras dicen lo mismo?", "Y *corregimos*."]},
 {"t": "consejo", "titulo": "TODAS DE ACUERDO", "texto": "Todas dicen uno o todas dicen varios", "emoji": "✅",
  "voz": ["Truco: todas las palabras tienen que estar *de acuerdo*."]},
 {"t": "resumen", "items": [["BUSCAR", "¿uno o varios?"], ["CORREGIR", "todas de acuerdo"], ["REVISAR", "el adjetivo también"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Buscamos*: ¿uno o varios?", "*Corregimos*: todas de acuerdo.", "*Revisamos* también el adjetivo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m14-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 14 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
