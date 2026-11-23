# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 1 · Palabras y oraciones que ya sabemos: las 4 clases animadas.
Metáfora: el cuaderno viajero de Sofi. Regla de primeros años y vía fonológica (la voz no nombra letras).
Genera tools/medio/clase/lecciones/medio-leng2-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '25e364ed-834f-40bc-a1b6-c2458923574d', 2: '7c681484-145f-43c1-9f0c-3d637312c7ef', 3: 'f774fb98-34c9-4966-8bbc-a4cc6d0c0aa3', 4: 'db1e409f-4923-440a-8772-f417c3b735fb'}
TIT = {1: 'Leer oraciones cortas', 2: 'Escribir oraciones con mayúscula y punto', 3: 'Ordenar palabras de una oración', 4: 'Completar oraciones'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}

N1 = [
 {"t": "historia", "personaje": SOFI, "lugar": "📒", "lineas": ["Sofi tiene un cuaderno viajero.", "Cada día escribe algo.", "¿Qué escribió hoy?"], "titulo": "LEER", "sub": "oraciones cortas",
  "voz": ["Sofi tiene un *cuaderno viajero*.", "Cada día escribe algo nuevo.", "¿Qué escribió hoy? ¡Leamos!", "Hoy: *leer oraciones cortas*."]},
 {"t": "texto", "oracion": "MI GATO DUERME AL SOL", "marcas": [{"desde": 0, "hasta": 1, "etiqueta": "¿QUIÉN?", "color": "sol"}, {"desde": 2, "hasta": 2, "etiqueta": "¿QUÉ HACE?", "color": "verde"}],
  "voz": ["Sofi escribió: mi gato duerme al sol.", "¿De quién habla? De *mi gato*.", "¿Qué hace? *Duerme*."]},
 {"t": "historieta", "titulo": "EL CUADERNO DE SOFI", "vinetas": [{"emojis": ["🐱", "☀️"], "txt": "Mi gato duerme al sol.", "quien": "Sofi"}, {"emojis": ["👦", "⚽"], "txt": "Tomi juega a la pelota.", "quien": "Sofi"}, {"emojis": ["👩‍🏫", "📖"], "txt": "La maestra lee un cuento.", "quien": "Sofi"}],
  "voz": ["Mi gato duerme al sol.", "Tomi juega a la pelota.", "La maestra lee un cuento."]},
 {"t": "quiz4", "pregunta": "Tomi juega a la pelota. ¿Qué hace Tomi?", "opciones": ["Juega", "Duerme", "Lee"], "correcta": 0,
  "voz": ["Ahora vos: Tomi juega a la pelota.", "¿Qué hace Tomi?", "¡*Juega*!"]},
 {"t": "consejo", "titulo": "LEÉ DESPACITO", "texto": "Todas las palabras, sin saltear", "emoji": "🐢",
  "voz": ["Truco: leé *despacito*, sin saltear palabras."]},
 {"t": "resumen", "items": [["LEER", "todas las palabras"], ["¿QUIÉN?", "de quién habla"], ["¿QUÉ HACE?", "lo que pasa"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Leemos *todas las palabras*.", "Pensamos *de quién* habla.", "Y *qué hace*.", CIERRE]},
]
N2 = [
 {"t": "chat", "contacto": {"nombre": "Tomi", "emoji": "👦"}, "mensajes": [{"yo": False, "txt": "hoy fuimos a la plaza"}, {"yo": True, "txt": "¡Te faltó algo! 🤔"}, {"yo": False, "txt": "¿Qué me faltó?"}], "titulo": "MAYÚSCULA", "sub": "y punto",
  "voz": ["Tomi le manda un mensaje a Sofi.", "Escribió: hoy fuimos a la plaza.", "Sofi le dice: ¡te faltó algo!", "Hoy: *mayúscula y punto*."]},
 {"t": "comparar", "a": {"cab": "MAYÚSCULA", "texto": "A B C D"}, "b": {"cab": "minúscula", "texto": "a b c d"}, "signo": "=",
  "def": {"cab": "LA MISMA LETRA", "texto": "Cada letra tiene dos formas: la grande y la chica."},
  "voz": ["Cada letra tiene dos formas.", "Una es la *mayúscula*, la letra grande.", "La otra es la *minúscula*, la letra chica.", "Es la *misma letra*, en dos tamaños."]},
 {"t": "tabla", "titulo": "EL ABECEDARIO", "columnas": ["MAYÚSCULA", "minúscula"],
  "filas": [["A B C D E F G", "a b c d e f g"], ["H I J K L M N", "h i j k l m n"], ["Ñ O P Q R S T", "ñ o p q r s t"], ["U V W X Y Z", "u v w x y z"]],
  "voz": ["Mirá el abecedario completo, con las dos formas.", "Primero, las primeras siete: arriba las grandes, al lado las chicas.", "Después, las siguientes siete.", "Luego, otras siete.", "Y al final, las últimas seis."]},
 {"t": "corrige", "titulo": "DE MAYÚSCULA A MINÚSCULA", "cambios": [{"antes": "SOFI", "despues": "Sofi", "motivo": "solo la primera queda grande"}, {"antes": "MI CASA", "despues": "Mi casa", "motivo": "las demás se achican"}],
  "voz": ["Pasemos de mayúscula a minúscula.", "Si todas las letras son grandes, solo la primera queda *grande*.", "Las demás se *achican*. Así queda bien escrito."]},
 {"t": "parrafo", "titulo": "HOY LLUEVE.", "lineas": ["Hoy llueve."], "marcas": [{"linea": 0, "pos": "inicio", "txt": "MAYÚSCULA"}, {"linea": 0, "pos": "fin", "txt": "PUNTO"}],
  "voz": ["Sofi escribió: hoy llueve.", "Al principio, la letra grande: *mayúscula*.", "Al final, un puntito: el *punto*."]},
 {"t": "corrige", "titulo": "ARREGLAMOS", "cambios": [{"antes": "hoy fuimos a la plaza", "despues": "Hoy fuimos a la plaza.", "motivo": "mayúscula y punto"}, {"antes": "mi abuela hace tortas", "despues": "Mi abuela hace tortas.", "motivo": "mayúscula y punto"}],
  "voz": ["¡Arreglemos las oraciones!", "Le ponemos *mayúscula* y *punto* a la de Tomi.", "Y a la de la abuela, ¡también!"]},
 {"t": "vof", "afirmacion": "El perro ladra — está bien escrita", "emoji": "🐶", "verdadero": False, "explicacion": "Le falta el punto al final",
  "voz": ["¿Verdadero o falso? Mirá esta oración.", "¿Tiene mayúscula? ¿Tiene punto?", "¡*Falso*! Le falta el *punto*."]},
 {"t": "pregunta", "pregunta": "¿Dónde va la mayúscula?", "opciones": ["Al principio", "Al final", "En el medio"], "correcta": 0,
  "voz": ["Ahora vos.", "¿Dónde va la mayúscula?", "¡*Al principio*!"]},
 {"t": "resumen", "items": [["MAYÚSCULA", "al principio"], ["PUNTO", "al final"], ["REVISAR", "las dos puntas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *mayúscula* va al principio.", "El *punto* va al final.", "Siempre revisamos *las dos puntas*.", CIERRE]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡El viento desordenó el cuaderno!", "bajada": "Las palabras quedaron mezcladas", "emoji": "🌬️", "titulo": "ORDENAR", "sub": "palabras",
  "voz": ["¡Último momento: el viento desordenó el cuaderno!", "Las palabras quedaron *mezcladas*.", "Hoy: *ordenar palabras de una oración*."]},
 {"t": "fichas", "consigna": "Ordená: PAN COMPRA PAPÁ", "fichas": ["Papá", "compra", "pan."], "desorden": [2, 1, 0], "traduccion": "¡Ahora se entiende!",
  "voz": ["Pan compra papá… ¡no se entiende!", "Primero quién: papá. Después qué hace: compra pan.", "¡*Papá compra pan*! Ahora se entiende."]},
 {"t": "pasos", "titulo": "CÓMO ORDENO", "items": [{"txt": "¿Quién?", "emoji": "👤"}, {"txt": "¿Qué hace?", "emoji": "🏃"}, {"txt": "Lo demás", "emoji": "📦"}],
  "voz": ["¿Cómo ordenamos las palabras?", "Primero buscamos *quién*.", "Después, *qué hace*.", "Y al final, *lo demás*."]},
 {"t": "orden", "titulo": "LA ORACIÓN", "etq1": "MEZCLADAS", "etq2": "ORDENADAS", "items": [{"txt": "La abuela", "emoji": "👵"}, {"txt": "riega", "emoji": "💧"}, {"txt": "las flores.", "emoji": "🌷"}], "relato": [2, 1, 0],
  "voz": ["Estas palabras están mezcladas.", "Flores, riega, la abuela.", "Ordenadas: la abuela riega las flores."]},
 {"t": "pregunta", "pregunta": "¿Cuál va primero en: SALTA EL CONEJO?", "opciones": ["El conejo", "Salta"], "correcta": 0,
  "voz": ["Ahora vos: salta el conejo.", "¿Qué palabra va primero?", "¡*El conejo*! Primero quién."]},
 {"t": "resumen", "items": [["MEZCLADAS", "no se entienden"], ["QUIÉN", "va primero"], ["ORDENADA", "se entiende"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las palabras *mezcladas* no se entienden.", "Primero va *quién*.", "Ordenada, la oración *se entiende*.", CIERRE]},
]
N4 = [
 {"t": "reto", "texto": "El pájaro ___ en el árbol. ¿Qué palabra falta?", "segundos": 6, "respuesta": "¡CANTA!", "emoji": "🐦", "titulo": "COMPLETAR", "sub": "oraciones",
  "voz": ["Desafío: el pájaro… ¿qué? en el árbol.", "¡*Canta*! El pájaro canta en el árbol.", "Hoy: *completar oraciones*."]},
 {"t": "completa", "antes": "El pájaro", "despues": "en el árbol.", "opciones": ["canta", "mesa", "azul"], "correcta": 0,
  "voz": ["Se borró una palabra del cuaderno.", "¿Canta, mesa o azul?", "¡*Canta*! Es la que tiene sentido."]},
 {"t": "versus", "titulo": "¿CUÁL TIENE SENTIDO?", "a": {"txt": "La vaca da leche.", "emoji": "🐄", "datos": ["se entiende"]}, "b": {"txt": "La vaca da mesa.", "emoji": "🪑", "datos": ["no se entiende"]}, "gana": "a", "veredicto": "¡Gana la que tiene sentido!",
  "voz": ["Tomi completó de dos formas.", "La vaca da *leche*: se entiende.", "La vaca da *mesa*: ¡no tiene sentido!", "¡Gana *leche*!"]},
 {"t": "jefe", "jefe": {"nombre": "Borrador Loco", "emoji": "👾"}, "preguntas": [{"p": "El ___ ladra.", "r": "perro"}, {"p": "En invierno hace ___ .", "r": "frío"}],
  "voz": ["¡El *Borrador Loco* borró palabras!", "Las completamos para ganarle.", "El *perro* ladra.", "En invierno hace *frío*. ¡Ganamos!"]},
 {"t": "consejo", "titulo": "RELEÉ", "texto": "Leé la oración con la palabra puesta", "emoji": "🔁",
  "voz": ["Truco: *releé* la oración con la palabra puesta."]},
 {"t": "resumen", "items": [["FALTA", "una palabra"], ["ELEGIR", "la que tiene sentido"], ["RELEER", "para controlar"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "A la oración le *falta* una palabra.", "Elegimos la que tiene *sentido*.", "Al final, *releemos*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-leng2-m1-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Lengua 2", "titulo": TIT[n], "sub": f"Lengua 2 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
