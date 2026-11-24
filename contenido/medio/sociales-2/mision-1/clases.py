# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 1 · De la materia prima al producto: las 4 clases animadas.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (visita una fábrica).
Genera tools/medio/clase/lecciones/medio-soc2-m1-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
STEP = {1: '38c36bec-2d8f-47f4-8c53-cb72c9cf0007', 2: 'c7857f85-4e26-4e8a-a724-d206d5023b3b', 3: 'bb2e94e0-b414-40c8-82c4-79d93bd97edf', 4: '8a41c621-c57d-4878-9706-e805a7035a1d'}
TIT = {1: 'Del tomate a la salsa', 2: 'De la leche al queso y al helado', 3: 'Las etapas de una producción', 4: 'Quiénes trabajan en una fábrica'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."

N1 = [
 {"t": "noticia", "cinta": "REPORTAJE", "titular": "¡Lola visita una fábrica de salsa!", "bajada": "Del tomate al frasco", "emoji": "🍅", "titulo": "DEL TOMATE", "sub": "a la salsa",
  "voz": ["¡Noticia: Lola visita una fábrica de *salsa*!", "Va a ver cómo se hace.", "Hoy: *del tomate a la salsa*."]},
 {"t": "transforma", "titulo": "DEL TOMATE A LA SALSA", "pasos": [{"txt": "TOMATE 🍅", "nota": "en la huerta"}, {"txt": "SE COCINA 🍲", "nota": "en la fábrica"}, {"txt": "SALSA 🫙", "nota": "¡en el frasco!"}],
  "voz": ["Primero, el *tomate* en la huerta.", "En la fábrica, se *cocina*.", "¡Y se envasa: ya es *salsa*!"]},
 {"t": "comparar", "a": {"cab": "MATERIA PRIMA", "texto": "TOMATE", "emoji": "🍅"}, "b": {"cab": "PRODUCTO", "texto": "SALSA", "emoji": "🫙"}, "signo": "→",
  "voz": ["Comparamos dos palabras nuevas.", "La *materia prima* sale de la naturaleza: el tomate.", "El *producto* se hace con ella: la salsa."]},
 {"t": "pregunta", "pregunta": "¿El tomate es materia prima o producto?", "opciones": ["MATERIA PRIMA", "PRODUCTO"], "correcta": 0,
  "voz": ["Ahora vos: ¿el tomate qué es?", "Pensá: ¿sale de la naturaleza?", "¡*Materia prima*!"]},
 {"t": "consejo", "titulo": "¿NATURALEZA O FÁBRICA?", "texto": "De la naturaleza: materia prima", "emoji": "🤔",
  "voz": ["Truco: si sale de la *naturaleza*, es materia prima."]},
 {"t": "resumen", "items": [["MATERIA PRIMA", "de la naturaleza"], ["PRODUCTO", "hecho en la fábrica"], ["SALSA", "viene del tomate"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "La *materia prima* sale de la naturaleza.", "El *producto* se hace en la fábrica.", "La *salsa* viene del tomate.", CIERRE]},
]
N2 = [
 {"t": "historieta", "titulo": "LOLA EN EL TAMBO", "vinetas": [{"emojis": ["🐄", "🥛"], "txt": "Ordeñan la vaca"}, {"emojis": ["🚛", "❄️"], "txt": "La leche viaja fría"}, {"emojis": ["🏭", "🧀"], "txt": "¡En la fábrica, queso!"}],
  "voz": ["Lola visita un *tambo*: ordeñan la vaca.", "La leche viaja *fría* en camión.", "¡En la fábrica hacen *queso*! Hoy: *la leche*."]},
 {"t": "documental", "emojis": ["🧀", "🍦", "🥣"], "lugar": "🏭", "rotulos": [{"txt": "QUESO", "sub": "de la leche"}, {"txt": "HELADO", "sub": "de la leche"}, {"txt": "YOGUR", "sub": "de la leche"}],
  "voz": ["Con leche se hace el *queso*.", "También el *helado*.", "Y el *yogur*. ¡Todos de la leche!"]},
 {"t": "prediccion", "pregunta": "¿La mermelada viene de la leche?", "a": {"txt": "NO, DE LA FRUTA", "emoji": "🍓"}, "b": {"txt": "SÍ, DE LA LECHE", "emoji": "🥛"}, "correcta": "a", "resultado": "La mermelada se hace con fruta",
  "voz": ["¿La *mermelada* viene de la leche?", "Pensá…", "¡No! Se hace con *fruta*."]},
 {"t": "pregunta", "pregunta": "¿Dónde se ordeñan las vacas?", "opciones": ["EN EL TAMBO", "EN EL NEGOCIO"], "correcta": 0,
  "voz": ["Ahora vos: ¿dónde se ordeñan las vacas?", "Pensá en el campo.", "¡En el *tambo*!"]},
 {"t": "consejo", "titulo": "UNA Y MUCHOS", "texto": "Una materia prima da muchos productos", "emoji": "🥛",
  "voz": ["Truco: una materia prima puede dar *muchos* productos."]},
 {"t": "resumen", "items": [["TAMBO", "se ordeñan las vacas"], ["LECHE", "materia prima"], ["PRODUCTOS", "queso, yogur, helado"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En el *tambo* se ordeñan las vacas.", "La *leche* es la materia prima.", "Da queso, yogur y *helado*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Cuántos lugares recorre el pan hasta tu mesa?", "segundos": 8, "respuesta": "¡Campo, molino y panadería!", "emoji": "🍞", "titulo": "LAS ETAPAS", "sub": "de una producción",
  "voz": ["Desafío: ¿cuántos lugares recorre el *pan*?", "¡Campo, *molino* y panadería!", "Hoy: *las etapas de una producción*."]},
 {"t": "linea", "titulo": "LAS ETAPAS", "eventos": [{"fecha": "1", "txt": "campo: se obtiene", "emoji": "🌾"}, {"fecha": "2", "txt": "fábrica: se transforma", "emoji": "🏭"}, {"fecha": "3", "txt": "camión: se transporta", "emoji": "🚚"}, {"fecha": "4", "txt": "negocio: se vende", "emoji": "🏪"}],
  "voz": ["En el *campo*, se obtiene.", "En la *fábrica*, se transforma.", "En el *camión*, se transporta.", "En el *negocio*, se vende."]},
 {"t": "quiz4", "pregunta": "¿Dónde se hace la harina?", "opciones": ["EN EL MOLINO", "EN LA PLAZA", "EN LA ESCUELA", "EN EL RÍO"], "correcta": 0,
  "voz": ["¿Dónde se hace la *harina*?", "Pensá en el trigo.", "¡En el *molino*!"]},
 {"t": "pregunta", "pregunta": "¿Cuál es la primera etapa?", "opciones": ["EL CAMPO", "EL NEGOCIO"], "correcta": 0,
  "voz": ["Ahora vos: ¿cuál es la primera etapa?", "Pensá de dónde sale todo.", "¡El *campo*!"]},
 {"t": "consejo", "titulo": "EN ORDEN", "texto": "Campo, fábrica, camión y negocio", "emoji": "➡️",
  "voz": ["Truco: campo, fábrica, camión y *negocio*."]},
 {"t": "resumen", "items": [["CAMPO", "se obtiene"], ["FÁBRICA", "se transforma"], ["NEGOCIO", "se vende"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En el *campo* se obtiene.", "En la *fábrica* se transforma.", "En el *negocio* se vende.", CIERRE]},
]
N4 = [
 {"t": "chat", "contacto": {"nombre": "Papá", "emoji": "👨"}, "mensajes": [{"yo": False, "txt": "¿Quién hizo este yogur? 🥣"}, {"yo": True, "txt": "¡Muchas personas!"}], "titulo": "QUIÉNES", "sub": "trabajan",
  "voz": ["Papá pregunta: ¿quién hizo este yogur?", "Lola responde: ¡*muchas* personas!", "Hoy: *quiénes trabajan en una fábrica*."]},
 {"t": "mazo", "titulo": "TRABAJOS", "items": [{"frente": "👨‍🌾", "dorso": "AGRICULTOR: COSECHA", "emoji": "👨‍🌾"}, {"frente": "👩‍🏭", "dorso": "OPERARIA: USA MÁQUINAS", "emoji": "👩‍🏭"}, {"frente": "🚚", "dorso": "CHOFER: MANEJA", "emoji": "🚚"}, {"frente": "🛒", "dorso": "VENDEDORA: ATIENDE", "emoji": "🛒"}],
  "voz": ["El *agricultor* cosecha en el campo.", "La *operaria* usa las máquinas.", "El *chofer* maneja el camión.", "La *vendedora* atiende el negocio."]},
 {"t": "personaje", "personaje": {"nombre": "Marta, operaria", "emoji": "👩‍🏭"}, "lineas": [{"txt": "¡Hola! Trabajo en la fábrica de yogur.", "animo": "feliz"}, {"txt": "Me pongo guantes, gorro y barbijo.", "animo": "piensa"}, {"txt": "¡Así el yogur queda limpio!", "animo": "sorpresa"}],
  "voz": ["¡Hola! Trabajo en la fábrica de *yogur*.", "Me pongo *guantes*, gorro y barbijo.", "¡Así el yogur queda *limpio*!"]},
 {"t": "pregunta", "pregunta": "¿Qué usan en la fábrica para cuidarse?", "opciones": ["GUANTES Y GORRO", "MALLA"], "correcta": 0,
  "voz": ["Ahora vos: ¿qué usan para cuidarse?", "Pensá en las manos y el pelo.", "¡*Guantes* y gorro!"]},
 {"t": "consejo", "titulo": "TODOS IMPORTAN", "texto": "Si falta uno, el producto no llega", "emoji": "🤝",
  "voz": ["Truco: *todos* los trabajos son importantes."]},
 {"t": "resumen", "items": [["CAMPO", "agricultor"], ["FÁBRICA", "operaria"], ["CAMINO Y NEGOCIO", "chofer y vendedora"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "En el campo, el *agricultor*.", "En la fábrica, la *operaria*.", "Después, el *chofer* y la *vendedora*.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc2-m1-n{n}'
    L = {"slug": slug, "step_id": STEP[n], "materia": "Ciencias Sociales 2", "titulo": TIT[n], "sub": f"Ciencias Sociales 2 · Misión 1 · Nivel {n}", "estilo": "primeros", "escenas": E}
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
