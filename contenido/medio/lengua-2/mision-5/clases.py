# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 5 · Ortografía: M antes de P y B: las 4 clases animadas.
Vía fonológica: la VOZ dice sonidos (mmm, nnn, pa, ba), nunca nombres de letras; la pantalla muestra las letras.
Metáfora: Sofi, detective de palabras. Genera tools/medio/clase/lecciones/medio-leng2-m5-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '92bdd477-1dc4-4b47-9299-98aed0ff4ef4', 2: 'aa2e3b66-8e16-49b5-8ec7-677867cb1dd4', 3: '89e5bab3-ac53-4f55-9c5e-7f45a29ff0b2', 4: '545031f8-f35a-4568-9cc7-278bc9fa1d9a'}
TIT = {1: 'Palabras con MP', 2: 'Palabras con MB', 3: 'Dictado con MP y MB', 4: 'Corregir palabras con M y N'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "🕵️‍♀️"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🔍", "lineas": ["Sofi es detective de palabras.", "Busca una pista escondida.", "¡Está en CAMPO!"], "titulo": "PALABRAS", "sub": "con MP",
  "voz": ["Sofi es *detective de palabras*.", "Hoy busca una pista escondida.", "¡La encontró en la palabra *campo*!", "Hoy: *palabras con mp*."]},
 {"t": "silabas", "palabra": "CAMPO", "silabas": ["CAM", "PO"], "tonica": 0, "tipo": "grave",
  "voz": ["Escuchá: cam… po.", "En *cam* escuchamos mmm al final.", "¡Y después viene *po*! Por eso va mmm."]},
 {"t": "definicion", "palabra": "La pista", "texto": "Antes de P, siempre M", "emoji": "🔎",
  "voz": ["Esta es la *pista* de la detective.", "Antes del sonido pa, siempre se escribe con mmm."]},
 {"t": "completa", "antes": "CA", "despues": "PANA", "opciones": ["M", "N"], "correcta": 0,
  "voz": ["Completá la palabra: campana.", "¿Va mmm o nnn?", "¡Va *mmm*! Porque después viene pa."]},
 {"t": "memoria", "titulo": "PALABRAS CON MP", "items": ["CAMPO", "LÁMPARA", "TROMPETA", "SIEMPRE"], "falta": 2,
  "voz": ["Mirá estas palabras con mp.", "Se tapan… ¡y una desapareció!", "¡Faltaba *trompeta*!"]},
 {"t": "resumen", "items": [["LA PISTA", "antes de P, M"], ["EJEMPLOS", "CAMPO, LÁMPARA"], ["SIEMPRE", "no falla"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Antes de pa, se escribe con *mmm*.", "Como en *campo* y *lámpara*.", "¡*Siempre* es así!", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¡Me compré un TANBOR! 🥁"}, {"yo": True, "txt": "¡Ojo cómo lo escribiste!"}, {"yo": False, "txt": "¿Está mal?"}], "titulo": "PALABRAS", "sub": "con MB",
  "voz": ["Tomi le escribe a Sofi: ¡me compré un tambor!", "Sofi mira bien la palabra…", "¡Hay que revisar cómo la escribió!", "Hoy: *palabras con mb*."]},
 {"t": "silabas", "palabra": "TAMBOR", "silabas": ["TAM", "BOR"], "tonica": 1, "tipo": "aguda",
  "voz": ["Escuchá: tam… bor.", "En *tam* escuchamos mmm al final.", "¡Y después viene *bor*! Por eso va mmm."]},
 {"t": "clasificar", "cajas": [{"cab": "MP", "emoji": "🔔"}, {"cab": "MB", "emoji": "🥁"}], "fichas": [{"txt": "CAMPANA", "caja": 0}, {"txt": "LÁMPARA", "caja": 0}, {"txt": "TAMBOR", "caja": 1}, {"txt": "BOMBERO", "caja": 1}],
  "voz": ["Separamos las palabras.", "Campana y lámpara: después viene pa.", "Tambor y bombero: después viene ba o bo."]},
 {"t": "vof", "afirmacion": "TANBOR está bien escrito", "emoji": "🥁", "verdadero": False, "explicacion": "Se escribe TAMBOR",
  "voz": ["¿Verdadero o falso? Así escribió Tomi.", "Pensá en la pista de la detective…", "¡*Falso*! Antes de bor va mmm: *tambor*."]},
 {"t": "pregunta", "pregunta": "SO_BRERO: ¿qué letra va?", "opciones": ["M", "N"], "correcta": 0,
  "voz": ["Ahora vos: sombrero.", "¿Va mmm o nnn?", "¡*Mmm*! Después viene bre."]},
 {"t": "resumen", "items": [["MB", "antes de B, M"], ["MP", "antes de P, M"], ["EJEMPLOS", "TAMBOR, CAMPO"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Antes de ba, va *mmm*.", "Antes de pa, también *mmm*.", "Como en *tambor* y *campo*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Escribí en tu carpeta: CAMPANA", "segundos": 8, "respuesta": "CAMPANA, con MP", "emoji": "✏️", "titulo": "DICTADO", "sub": "con MP y MB",
  "voz": ["Desafío: escribí en tu carpeta *campana*.", "¡Campana! Con mmm antes de pa.", "Hoy: *dictado*."]},
 {"t": "pasos", "titulo": "CÓMO HAGO EL DICTADO", "items": [{"txt": "Escucho toda la palabra", "emoji": "👂"}, {"txt": "Pienso la pista", "emoji": "🔎"}, {"txt": "Escribo y reviso", "emoji": "✏️"}],
  "voz": ["¿Cómo hacemos un dictado?", "Escuchamos *toda* la palabra.", "Pensamos la *pista* de la detective.", "Escribimos y *revisamos*."]},
 {"t": "tipeo", "titulo": "DICTADO", "items": [{"p": "El que apaga incendios", "r": "BOMBERO"}, {"p": "Da luz en la mesa", "r": "LÁMPARA"}, {"p": "Suena en la escuela", "r": "CAMPANA"}],
  "voz": ["Primera palabra: *bombero*.", "Segunda palabra: *lámpara*.", "Tercera palabra: *campana*."]},
 {"t": "contrarreloj", "titulo": "RONDA RÁPIDA", "segundos": 20, "items": [{"p": "HO_BRE", "r": "M"}, {"p": "SIE_PRE", "r": "M"}, {"p": "TA_BIÉN", "r": "M"}],
  "voz": ["¡Ronda rápida de la detective!", "Hombre: va *mmm*.", "Siempre: va *mmm*.", "También: va *mmm*."]},
 {"t": "consejo", "titulo": "REVISÁ AL FINAL", "texto": "Mirá cada palabra con MP o MB", "emoji": "🔍",
  "voz": ["Truco: al final, *revisá* cada palabra."]},
 {"t": "resumen", "items": [["ESCUCHAR", "toda la palabra"], ["PENSAR", "la pista"], ["REVISAR", "al final"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Escuchamos* toda la palabra.", "*Pensamos* la pista.", "Y *revisamos* al final.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Errores en el cuaderno de Tomi!", "bajada": "La detective los va a encontrar", "emoji": "🚨", "titulo": "CORREGIR", "sub": "M y N",
  "voz": ["¡Último momento: hay errores en el cuaderno de Tomi!", "La detective Sofi los va a encontrar.", "Hoy: *corregir palabras con mmm y nnn*."]},
 {"t": "corrige", "titulo": "LA DETECTIVE CORRIGE", "cambios": [{"antes": "CANPO", "despues": "CAMPO", "motivo": "antes de P va M"}, {"antes": "TANBOR", "despues": "TAMBOR", "motivo": "antes de B va M"}, {"antes": "SIENPRE", "despues": "SIEMPRE", "motivo": "antes de P va M"}],
  "voz": ["¡Encontramos errores!", "Campo: antes de po, va mmm.", "Tambor: antes de bor, va mmm.", "Siempre: antes de pre, va mmm."]},
 {"t": "versus", "titulo": "¿CUÁL ESTÁ BIEN?", "a": {"txt": "CANTO", "emoji": "✅", "datos": ["después viene T"]}, "b": {"txt": "SONBRERO", "emoji": "❌", "datos": ["después viene B"]}, "gana": "a", "veredicto": "¡CANTO está bien!",
  "voz": ["Comparamos dos palabras.", "*Canto*: después viene to. ¡Está bien con nnn!", "*Sombrero* con nnn: ¡está mal!", "¡Gana *canto*!"]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Borrón", "emoji": "👹"}, "preguntas": [{"p": "LANPARA", "r": "LÁMPARA"}, {"p": "HONBRE", "r": "HOMBRE"}],
  "voz": ["¡Apareció el *Monstruo Borrón*!", "Corregimos sus palabras.", "*Lámpara*, con mmm.", "¡*Hombre*, con mmm! ¡Ganamos!"]},
 {"t": "consejo", "titulo": "MIRÁ LO QUE SIGUE", "texto": "P o B: M. Otra letra: puede ser N", "emoji": "👀",
  "voz": ["Truco: mirá el sonido que *sigue*."]},
 {"t": "resumen", "items": [["ERROR", "N antes de P o B"], ["CORREGIR", "cambiar por M"], ["N", "antes de otras letras"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Nnn antes de pa o ba es un *error*.", "Lo *corregimos* con mmm.", "Antes de otros sonidos, puede ir nnn.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m5-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 5 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
