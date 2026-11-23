# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 5 · My Family: las 4 clases animadas.
Explicación en castellano; las frases en inglés van en "voz_en" (se dicen con voz en inglés). Metáfora: la familia de Sofi.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-ing1-m4-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = 'e2d48bb4-83ea-4f78-b7f0-ba50b1154664'
TEMA = 5
TIT = {1: 'Mum, dad and baby', 2: 'Brother, sister, grandma and grandpa', 3: 'This is my family', 4: 'Who is he? Who is she?'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": SOFI, "mensajes": [{"yo": False, "txt": "📷 THIS IS MY FAMILY!"}, {"yo": True, "txt": "¡Qué linda!"}, {"yo": False, "txt": "MUM, DAD AND BABY!"}], "titulo": "MY FAMILY", "sub": "mamá, papá y bebé",
  "voz": ["Sofi le manda una foto a Tomi.", "This is my family!", "Es la foto de su *familia*.", "Hoy: *mamá, papá y bebé en inglés*."], "voz_en": [1]},
 {"t": "vocab", "items": [{"palabra": "MUM", "emoji": "👩", "trad": "mamá", "pron": "mam"}, {"palabra": "DAD", "emoji": "👨", "trad": "papá", "pron": "dad"}, {"palabra": "BABY", "emoji": "👶", "trad": "bebé", "pron": "béibi"}],
  "voz": ["Mum!", "Dad!", "Baby!"], "voz_en": [0, 1, 2]},
 {"t": "bloques", "titulo": "CADA FAMILIA ES DISTINTA", "items": [{"cab": "👩👧", "txt": "MUM AND ME"}, {"cab": "👨👦", "txt": "DAD AND ME"}, {"cab": "👩👨👶", "txt": "MUM, DAD AND BABY"}],
  "voz": ["Hay familias de muchas formas.", "Mum and me!", "Dad and me!", "Mum, dad and baby!"], "voz_en": [1, 2, 3]},
 {"t": "pregunta", "pregunta": "¿Cómo se dice bebé?", "opciones": ["BABY", "MUM", "DAD"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en un bebé.", "¿Cómo se dice en inglés?", "Baby!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "TODAS SON FAMILIAS", "texto": "Grandes o chicas, todas son familias", "emoji": "💛",
  "voz": ["Recordá: grandes o chicas, todas son *familias*."]},
 {"t": "resumen", "items": [["MUM", "mamá"], ["DAD", "papá"], ["BABY", "bebé"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Mum, dad, baby!", "Mamá, papá y *bebé*.", CIERRE], "voz_en": [1]},
]
N2 = [
 {"t": "reto", "texto": "¿Cómo se dice abuela en inglés?", "segundos": 6, "respuesta": "¡GRANDMA!", "emoji": "👵", "titulo": "MY FAMILY", "sub": "hermanos y abuelos",
  "voz": ["Desafío: ¿cómo se dice abuela en inglés?", "Grandma!", "Hoy: *hermanos y abuelos en inglés*."], "voz_en": [1]},
 {"t": "vocab", "items": [{"palabra": "BROTHER", "emoji": "👦", "trad": "hermano", "pron": "bráder"}, {"palabra": "SISTER", "emoji": "👧", "trad": "hermana", "pron": "síster"}, {"palabra": "GRANDMA", "emoji": "👵", "trad": "abuela", "pron": "granmá"}, {"palabra": "GRANDPA", "emoji": "👴", "trad": "abuelo", "pron": "granpá"}],
  "voz": ["Brother!", "Sister!", "Grandma!", "Grandpa!"], "voz_en": [0, 1, 2, 3]},
 {"t": "venn", "a": "VARONES", "b": "NENAS Y MUJERES", "itemsA": ["BROTHER", "GRANDPA", "DAD"], "itemsB": ["SISTER", "GRANDMA", "MUM"], "ambos": ["BABY"],
  "voz": ["Separamos las palabras.", "Para varones: brother, grandpa, dad.", "Para nenas y mujeres: sister, grandma, mum.", "¡Baby sirve para los dos!"], "voz_en": []},
 {"t": "pregunta", "pregunta": "Lucía es la hermana de Tomi. Es su…", "opciones": ["SISTER", "BROTHER", "GRANDPA"], "correcta": 0,
  "voz": ["Ahora vos. Lucía es la hermana de Tomi.", "¿Cómo se dice hermana?", "Sister!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "GRAND", "texto": "GRANDMA y GRANDPA empiezan igual", "emoji": "👵👴",
  "voz": ["Truco: abuela y abuelo empiezan *igual* en inglés."]},
 {"t": "resumen", "items": [["BROTHER", "hermano"], ["SISTER", "hermana"], ["GRANDMA / GRANDPA", "abuela y abuelo"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Brother, sister!", "Grandma, grandpa!", CIERRE], "voz_en": [1, 2]},
]
N3 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡SOFI PRESENTA A SU FAMILIA!", "bajada": "Y lo hace en inglés", "emoji": "🖼️", "titulo": "THIS IS MY FAMILY", "sub": "presentar a mi familia",
  "voz": ["¡Último momento! Sofi presenta a su *familia*.", "¡Y lo hace en inglés!", "Hoy: *presentar a mi familia*."]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "TOMI", "emoji": "👦"}], "lineas": [{"quien": 0, "txt": "THIS IS MY MUM.", "trad": "esta es mi mamá"}, {"quien": 1, "txt": "HELLO!", "trad": "¡hola!"}, {"quien": 0, "txt": "THIS IS MY GRANDPA.", "trad": "este es mi abuelo"}, {"quien": 1, "txt": "NICE TO MEET YOU!", "trad": "¡mucho gusto!"}],
  "voz": ["This is my mum.", "Hello!", "This is my grandpa.", "Nice to meet you!"], "voz_en": [0, 1, 2, 3]},
 {"t": "matriz", "titulo": "THIS IS MY…", "celdas": [{"cab": "👩", "txt": "THIS IS MY MUM"}, {"cab": "👴", "txt": "THIS IS MY GRANDPA"}, {"cab": "👦", "txt": "THIS IS MY BROTHER"}, {"cab": "👧", "txt": "THIS IS MY SISTER"}],
  "voz": ["Presentamos a cada uno.", "This is my mum.", "This is my grandpa.", "This is my brother.", "This is my sister."], "voz_en": [1, 2, 3, 4]},
 {"t": "pregunta", "pregunta": "Mostrás a tu papá. ¿Qué decís?", "opciones": ["THIS IS MY DAD", "I AM SIX", "GOODBYE"], "correcta": 0,
  "voz": ["Ahora vos. Mostrás a tu papá.", "¿Qué decís en inglés?", "This is my dad!"], "voz_en": [2]},
 {"t": "consejo", "titulo": "SEÑALÁ", "texto": "Señalá a la persona al presentarla", "emoji": "👉",
  "voz": ["Truco: *señalá* a la persona al presentarla."]},
 {"t": "resumen", "items": [["THIS IS MY…", "este es mi…"], ["PRESENTAR", "decir quién es"], ["FAMILIAS", "todas distintas"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "This is my family!", "Así presentamos a cada uno.", CIERRE], "voz_en": [1]},
]
N4 = [
 {"t": "gancho", "emoji": "🖼️", "final": "❓", "titulo": "WHO IS SHE?", "sub": "¿quién es?",
  "voz": ["Tomi ve una foto en la pared.", "¿Quién será esa señora?", "Hoy: *preguntar quién es en inglés*."]},
 {"t": "comparar", "a": {"cab": "HE", "texto": "Él: un varón", "emoji": "👦"}, "b": {"cab": "SHE", "texto": "Ella: una nena", "emoji": "👧"}, "signo": "vs",
  "voz": ["Dos palabras nuevas: él y ella.", "He!", "She!"], "voz_en": [1, 2]},
 {"t": "clasificar", "cajas": [{"cab": "HE", "emoji": "👦"}, {"cab": "SHE", "emoji": "👧"}], "fichas": [{"txt": "DAD", "caja": 0}, {"txt": "BROTHER", "caja": 0}, {"txt": "MUM", "caja": 1}, {"txt": "GRANDMA", "caja": 1}],
  "voz": ["¿He o she?", "Dad y brother: he!", "Mum y grandma: she!"], "voz_en": [1, 2]},
 {"t": "corrige", "titulo": "¿ESTÁ BIEN?", "cambios": [{"antes": "SHE IS MY BROTHER", "despues": "HE IS MY BROTHER", "motivo": "es varón"}, {"antes": "HE IS MY MUM", "despues": "SHE IS MY MUM", "motivo": "es mujer"}],
  "voz": ["Tomi se equivocó. Lo arreglamos.", "He is my brother.", "She is my mum."], "voz_en": [1, 2]},
 {"t": "pregunta", "pregunta": "Es tu abuela. ¿Qué preguntan?", "opciones": ["WHO IS SHE?", "WHO IS HE?", "HOW OLD ARE YOU?"], "correcta": 0,
  "voz": ["Ahora vos. En la foto está tu abuela.", "¿Qué pregunta tu amigo?", "Who is she?"], "voz_en": [2]},
 {"t": "consejo", "titulo": "HE Y SHE", "texto": "SHE tiene una letra más: la S", "emoji": "🔤",
  "voz": ["Truco: she tiene una *letra más*."]},
 {"t": "resumen", "items": [["HE", "él"], ["SHE", "ella"], ["WHO IS…?", "¿quién es…?"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Who is he? Who is she?", "Así preguntamos *quién es*.", CIERRE], "voz_en": [1]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-ing1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Inglés 1", "titulo": TIT[n], "sub": f"Inglés 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
