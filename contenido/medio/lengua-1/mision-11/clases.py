# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 11 · Letras V, Ñ y LL: las 4 clases animadas.
Vía fonológica: la VOZ dice sonidos y palabras ancla («como en vaca», «ñññ como en ñandú»), nunca nombres de letras.
Metáfora: un día de lluvia en la granja de la abuela. Genera tools/medio/clase/lecciones/medio-leng1-m11-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '5db780ac-cfa8-43d1-84c2-a76585171737', 2: 'a5661981-f786-436c-86bb-851c0afe0651', 3: 'f34508e4-f898-491a-b2c9-dbde29472752', 4: '222fd634-804e-41c6-8d61-9f004f5224b0'}
TIT = {1: 'Conocer la V', 2: 'Conocer la Ñ y la LL', 3: 'Leer palabras con V, Ñ y LL', 4: 'Escribir palabras con V, Ñ y LL'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🐄", "lineas": ["Sofi visita la granja de la abuela.", "¡Hay una vaca!", "Muuu…"], "titulo": "LETRA NUEVA", "sub": "la de VACA",
  "voz": ["Sofi visita la *granja* de la abuela.", "¡Hay una *vaca*!", "Muuu…", "Hoy: *una letra nueva*."]},
 {"t": "silabas", "palabra": "VACA", "silabas": ["VA", "CA"], "tonica": 0, "tipo": "grave",
  "voz": ["Escuchá: va… ca.", "Esta letra nueva suena como en *vaca*.", "Va, ve, vi, vo, vu."]},
 {"t": "comparar", "a": {"cab": "VACA", "texto": "va", "emoji": "🐄"}, "b": {"cab": "BOTE", "texto": "bo", "emoji": "⛵"}, "signo": "=",
  "voz": ["*Vaca* y *bote* empiezan con el mismo sonido.", "¡Pero se escriben con letras distintas!", "Hay que mirar bien cómo se escribe."]},
 {"t": "pregunta", "pregunta": "¿Cuál empieza como VACA?", "opciones": ["VASO", "PATO", "MESA"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuál empieza como vaca?", "Mirá la primera letra.", "¡*Vaso*!"]},
 {"t": "consejo", "titulo": "MIRÁ LA PALABRA", "texto": "Suenan igual: fijate cómo se escribe", "emoji": "👀",
  "voz": ["Truco: suenan igual, así que *mirá* cómo se escribe."]},
 {"t": "resumen", "items": [["VACA", "va, ve, vi, vo, vu"], ["SUENA", "igual que BOTE"], ["PALABRAS", "VASO, UVA"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La letra de *vaca*: va, ve, vi, vo, vu.", "Suena igual que la de *bote*.", "Como en *vaso* y *uva*.", CIERRE]},
]
N2 = [
 {"t": "noticia", "cinta": "LA GRANJA", "titular": "¡Empezó a llover!", "bajada": "Y apareció un ñandú", "emoji": "🌧️", "titulo": "DOS LETRAS", "sub": "nuevas",
  "voz": ["¡Noticia en la granja: empezó a *llover*!", "Y apareció un *ñandú*.", "Hoy: *dos letras nuevas*."]},
 {"t": "definicion", "palabra": "La del sombrerito", "texto": "Ñ: ÑA, ÑE, ÑI, ÑO, ÑU", "emoji": "🎩",
  "voz": ["Esta letra tiene un *sombrerito*.", "Suena ñññ, como en *ñandú* y *niño*."]},
 {"t": "patron", "titulo": "¿QUÉ SÍLABA SIGUE?", "items": ["ÑA", "ÑE", "ÑI", "ÑO", "ÑU"], "falta": 3, "regla": "Con las vocales en orden",
  "voz": ["Ña, ñe, ñi…", "¿Qué sigue?", "¡*Ño*, como en niño!"]},
 {"t": "mazo", "titulo": "DOS JUNTAS", "items": [{"frente": "🔑", "dorso": "LLAVE", "emoji": "🔑"}, {"frente": "🌧️", "dorso": "LLUVIA", "emoji": "🌧️"}, {"frente": "🐥", "dorso": "POLLITO", "emoji": "🐥"}],
  "voz": ["*Llave*: dos letras juntas, un solo sonido.", "*Lluvia*: igual.", "*Pollito*: ¡también!"]},
 {"t": "consejo", "titulo": "MIRÁ EL SOMBRERITO", "texto": "Sin sombrerito es N. Con sombrerito es Ñ", "emoji": "🎩",
  "voz": ["Truco: mirá si tiene *sombrerito*."]},
 {"t": "resumen", "items": [["ÑANDÚ", "ña, ñe, ñi, ño, ñu"], ["LLAVE", "dos letras juntas"], ["PALABRAS", "NIÑO, LLUVIA"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La del *sombrerito*: como en ñandú.", "Las *dos juntas*: como en llave.", "Como en *niño* y *lluvia*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "Leé: EL POLLITO VE LA LLUVIA", "segundos": 8, "respuesta": "¡El pollito ve la lluvia!", "emoji": "🐥", "titulo": "LEER", "sub": "palabras nuevas",
  "voz": ["Desafío: leé la oración de Sofi.", "¡El pollito ve la lluvia!", "Hoy: *leer palabras nuevas*."]},
 {"t": "tipeo", "titulo": "JUNTAMOS SÍLABAS", "items": [{"p": "VA · SO", "r": "VASO"}, {"p": "PI · ÑA", "r": "PIÑA"}, {"p": "PO · LLO", "r": "POLLO"}],
  "voz": ["Va… so: *vaso*.", "Pi… ña: *piña*.", "Po… llo: *pollo*."]},
 {"t": "contrarreloj", "titulo": "LECTURA RÁPIDA", "segundos": 20, "items": [{"p": "U · ÑA", "r": "UÑA"}, {"p": "SI · LLA", "r": "SILLA"}, {"p": "U · VA", "r": "UVA"}],
  "voz": ["¡Lectura rápida!", "U… ña: *uña*.", "Si… lla: *silla*.", "U… va: *uva*."]},
 {"t": "consejo", "titulo": "DE A UNA", "texto": "Leé sílaba por sílaba y después juntá", "emoji": "🐢",
  "voz": ["Truco: leé *de a una* sílaba y después juntá."]},
 {"t": "pregunta", "pregunta": "¿Qué dice? PO · LLI · TO", "opciones": ["POLLITO", "PALITO"], "correcta": 0,
  "voz": ["Ahora vos: po… lli… to.", "¿Qué dice?", "¡*Pollito*!"]},
 {"t": "resumen", "items": [["SÍLABAS", "de a una"], ["JUNTAR", "todo junto"], ["ORACIÓN", "leer despacio"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos las *sílabas* de a una.", "Después las *juntamos*.", "Y leemos la *oración* despacio.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Abuela", "emoji": "👵"}, "mensajes": [{"yo": False, "txt": "Sofi, ¿me escribís lo que viste en la granja? 🐄"}, {"yo": True, "txt": "¡Sí, abuela!"}], "titulo": "ESCRIBIR", "sub": "palabras nuevas",
  "voz": ["La abuela le pide: ¿me escribís lo que viste?", "Sofi responde: ¡sí, abuela!", "Hoy: *escribir palabras nuevas*."]},
 {"t": "completa", "antes": "ESTRE", "despues": "A", "opciones": ["LL", "Ñ"], "correcta": 0,
  "voz": ["Completá: estre… a.", "¿Las dos juntas o la del sombrerito?", "¡Las *dos juntas*: estrella!"]},
 {"t": "jefe", "jefe": {"nombre": "Monstruo Borrón", "emoji": "👹"}, "preguntas": [{"p": "MO_O (para el pelo)", "r": "Ñ"}, {"p": "_ASO", "r": "V"}],
  "voz": ["¡Apareció el *Monstruo Borrón*! Borró letras.", "Las volvemos a escribir.", "Moño: la del *sombrerito*.", "Vaso: la de *vaca*. ¡Ganamos!"]},
 {"t": "errores", "items": [{"mal": "NINO", "bien": "NIÑO"}, {"mal": "ESTRELA", "bien": "ESTRELLA"}],
  "voz": ["Cuidado con estos errores.", "Niño lleva el *sombrerito*.", "Estrella lleva *dos juntas*."]},
 {"t": "consejo", "titulo": "DECILO DESPACIO", "texto": "Escuchá cada sílaba antes de escribir", "emoji": "👂",
  "voz": ["Truco: decí la palabra *despacio* antes de escribir."]},
 {"t": "resumen", "items": [["VASO", "la de vaca"], ["MOÑO", "la del sombrerito"], ["ESTRELLA", "dos juntas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Vaso*, con la de vaca.", "*Moño*, con la del sombrerito.", "*Estrella*, con las dos juntas.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng1-m11-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 1", "titulo": TIT[n], "sub": f"Lengua 1 · Misión 11 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
