# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 3 · La Cenicienta: las 4 clases animadas.
Metáfora: el cuaderno viajero de Sofi (lee el cuento con la abuela). Regla de primeros años y vía fonológica.
Genera tools/medio/clase/lecciones/medio-leng2-m3-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: 'd9a3964c-5050-48a6-9ac5-76b5c4854ffb', 2: '144b5f6a-6907-4a77-8d4b-034cebefe5d0', 3: 'ddb20994-6025-455a-a054-b43216e1ec39', 4: 'ec3aec1d-3173-436d-916d-0757b2782a03'}
TIT = {1: 'Escuchar La Cenicienta', 2: 'Los personajes y sus deseos', 3: 'Lugares y objetos mágicos', 4: 'Comparar con otros cuentos de hadas'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
CENI = {"nombre": "Cenicienta", "emoji": "👸"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📖", "lineas": ["La abuela le lee un cuento.", "Se llama La Cenicienta.", "¡Escuchemos!"], "titulo": "LA CENICIENTA", "sub": "un cuento de hadas",
  "voz": ["La abuela le lee un cuento a Sofi.", "Se llama *La Cenicienta*.", "¡Escuchemos juntos!", "Hoy: *escuchar La Cenicienta*."]},
 {"t": "historieta", "titulo": "HABÍA UNA VEZ…", "vinetas": [{"emojis": ["👸", "🧹"], "txt": "Cenicienta limpia toda la casa."}, {"emojis": ["🧚", "✨"], "txt": "El hada le da un vestido."}, {"emojis": ["🏰", "💃"], "txt": "¡Va al baile del castillo!"}],
  "voz": ["Había una vez una chica: Cenicienta. Limpiaba toda la casa.", "Un día, su hada madrina le dio un vestido.", "¡Y Cenicienta fue al baile del castillo!"]},
 {"t": "historieta", "titulo": "Y DESPUÉS…", "vinetas": [{"emojis": ["🕛", "🏃‍♀️"], "txt": "¡Suenan las doce!"}, {"emojis": ["👠"], "txt": "Pierde un zapatito."}, {"emojis": ["🤴", "👸"], "txt": "El príncipe la encuentra."}],
  "voz": ["¡Sonaron las doce! Cenicienta salió corriendo.", "En la escalera perdió un *zapatito de cristal*.", "El príncipe la buscó y ¡la encontró!"], "sticker": {"txt": "🕛", "paso": 0}},
 {"t": "orden", "titulo": "¿QUÉ PASÓ PRIMERO?", "etq1": "MEZCLADO", "etq2": "EN ORDEN", "items": [{"txt": "Limpia la casa", "emoji": "🧹"}, {"txt": "Va al baile", "emoji": "💃"}, {"txt": "Pierde el zapatito", "emoji": "👠"}], "relato": [2, 0, 1],
  "voz": ["Estas partes del cuento están mezcladas.", "Pierde el zapatito, limpia, va al baile.", "En orden: limpia, va al baile, pierde el zapatito."]},
 {"t": "quiz4", "pregunta": "¿Qué perdió Cenicienta?", "opciones": ["Un zapatito", "Una corona", "Un reloj"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Qué perdió Cenicienta?", "¡Un *zapatito de cristal*!"]},
 {"t": "resumen", "items": [["PRINCIPIO", "Cenicienta limpia"], ["MEDIO", "va al baile"], ["FINAL", "el príncipe la encuentra"]], "fin": FIN,
  "voz": ["Repasemos el cuento.", "Al *principio*, Cenicienta limpia.", "En el *medio*, va al baile.", "Al *final*, el príncipe la encuentra.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "¿Quiénes están en Cenicienta?"}, {"yo": True, "txt": "¡Muchos personajes!"}, {"yo": False, "txt": "¿Buenos o malos?"}], "titulo": "LOS PERSONAJES", "sub": "y sus deseos",
  "voz": ["Tomi le pregunta a Sofi por el cuento.", "¿Quiénes aparecen?", "¿Son buenos o malos?", "Hoy: *los personajes y sus deseos*."]},
 {"t": "clasificar", "cajas": [{"cab": "AYUDAN", "emoji": "💛"}, {"cab": "NO AYUDAN", "emoji": "😠"}], "fichas": [{"txt": "Hada", "caja": 0}, {"txt": "Príncipe", "caja": 0}, {"txt": "Madrastra", "caja": 1}, {"txt": "Hermanastras", "caja": 1}],
  "voz": ["Separamos los personajes.", "El hada y el príncipe *ayudan* a Cenicienta.", "La madrastra y las hermanastras *no la ayudan*."]},
 {"t": "personaje", "personaje": CENI, "lineas": [{"txt": "¡Quiero ir al baile!", "animo": "triste"}, {"txt": "¡Gracias, hada madrina!", "animo": "feliz"}],
  "voz": ["Cenicienta dice: ¡quiero ir al baile! Ese es su *deseo*.", "Y cuando el hada la ayuda: ¡gracias, hada madrina!"]},
 {"t": "unir", "titulo": "¿CÓMO ES CADA UNO?", "pares": [["Hada", "generosa"], ["Hermanastras", "malas"], ["Cenicienta", "trabajadora"]],
  "voz": ["Uní cada personaje con cómo es.", "El hada es *generosa*.", "Las hermanastras son *malas*.", "Cenicienta es *trabajadora*."]},
 {"t": "pregunta", "pregunta": "¿Qué desea el príncipe?", "opciones": ["Encontrar a Cenicienta", "Ir al bosque", "Ser hada"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Qué desea el príncipe?", "¡*Encontrar a Cenicienta*!"]},
 {"t": "resumen", "items": [["PERSONAJE", "quien hace cosas"], ["CÓMO ES", "por lo que hace"], ["DESEO", "lo que quiere"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *personaje* hace cosas en el cuento.", "Sabemos *cómo es* por lo que hace.", "Su *deseo* es lo que quiere.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡Una calabaza se hizo carroza!", "bajada": "Pasó en el cuento de Cenicienta", "emoji": "🎃", "titulo": "LUGARES", "sub": "y objetos mágicos",
  "voz": ["¡Último momento: una calabaza se hizo carroza!", "¿Cómo pudo pasar? ¡Con *magia*!", "Hoy: *lugares y objetos mágicos*."]},
 {"t": "comparar", "a": {"cab": "LA CASA", "texto": "Cenicienta limpia", "emoji": "🏠"}, "b": {"cab": "EL CASTILLO", "texto": "el gran baile", "emoji": "🏰"}, "signo": "y",
  "voz": ["El cuento pasa en dos lugares.", "En la *casa* limpia. En el *castillo* baila.", "¡Dos lugares muy distintos!"]},
 {"t": "zoom", "niveles": [{"emoji": "🪄", "txt": "La varita"}, {"emoji": "🎃", "txt": "La calabaza"}, {"emoji": "🛞", "txt": "¡Una carroza!"}],
  "voz": ["El hada mueve su *varita*.", "Toca la calabaza…", "¡Y se convierte en *carroza*!"], "sticker": {"txt": "✨", "paso": 2}},
 {"t": "prediccion", "pregunta": "¿Qué pasa a las doce?", "a": {"txt": "Sigue la magia", "emoji": "✨"}, "b": {"txt": "Se termina la magia", "emoji": "🕛"}, "correcta": "b", "resultado": "¡A las doce, todo vuelve a ser como antes!",
  "voz": ["¿Qué creés que pasa a las doce?", "¿Sigue la magia o se termina?", "¡Se *termina*! Todo vuelve a ser como antes."]},
 {"t": "pregunta", "pregunta": "¿En qué se convierten los ratones?", "opciones": ["En caballos", "En perros", "En pájaros"], "correcta": 0,
  "voz": ["Ahora vos.", "¿En qué se convierten los ratones?", "¡En *caballos*!"]},
 {"t": "resumen", "items": [["LUGARES", "la casa y el castillo"], ["MAGIA", "varita y carroza"], ["LAS DOCE", "termina la magia"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *lugares*: la casa y el castillo.", "La *magia*: la varita y la carroza.", "A las *doce*, la magia termina.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "¿Qué cuento tiene un lobo, Cenicienta o Caperucita?", "segundos": 5, "respuesta": "¡CAPERUCITA!", "emoji": "🐺", "titulo": "COMPARAR", "sub": "cuentos de hadas",
  "voz": ["Desafío: ¿qué cuento tiene un lobo?", "¡*Caperucita*!", "Hoy: *comparar cuentos de hadas*."]},
 {"t": "definicion", "palabra": "Cuento de hadas", "texto": "Tiene magia y final feliz", "emoji": "🧚",
  "voz": ["Un *cuento de hadas* tiene magia.", "Y casi siempre termina *feliz*."]},
 {"t": "venn", "a": "CENICIENTA", "b": "BLANCANIEVES", "itemsA": ["hada", "zapatito"], "itemsB": ["manzana", "enanitos"], "ambos": ["madrastra mala", "príncipe"],
  "voz": ["Comparamos dos cuentos.", "Cenicienta tiene un *hada* y un zapatito.", "Blancanieves tiene una *manzana* y enanitos.", "¡Los dos tienen madrastra mala y príncipe!"]},
 {"t": "vof", "afirmacion": "En Cenicienta hay un lobo", "emoji": "🐺", "verdadero": False, "explicacion": "El lobo es de Caperucita",
  "voz": ["¿Verdadero o falso? En Cenicienta hay un lobo.", "Pensá en los personajes…", "¡*Falso*! El lobo es de *Caperucita*."]},
 {"t": "memoria", "titulo": "¿DE QUÉ CUENTO?", "items": ["Zapatito", "Manzana", "Lobo", "Carroza"], "falta": 2,
  "voz": ["Mirá estas cosas de los cuentos.", "Se tapan… ¡y una desapareció!", "¡Faltaba el *lobo*, de Caperucita!"]},
 {"t": "resumen", "items": [["CUENTO DE HADAS", "magia y final feliz"], ["SE PARECEN", "madrastra, príncipe"], ["DISTINTOS", "hada, lobo, manzana"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Los *cuentos de hadas* tienen magia.", "Se *parecen*: madrastra y príncipe.", "Son *distintos*: hada, lobo, manzana.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m3-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 3 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
