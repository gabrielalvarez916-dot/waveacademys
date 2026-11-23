# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 7 · Animals. Genera mision-7.json.
Regla de primeros años. Metáfora: la granja y el zoológico de Tomi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 mascotas: dog, cat, fish · 2 animales de granja · 3 animales salvajes · 4 sonidos de animales, juego de adivinar."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
SA = lambda p, acepta, e, **k: {"t": "short_answer", "p": p, "o": {}, "r": {"acepta": acepta}, "e": e, **k}
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
low = lambda w: [w, w.lower(), w.capitalize()]
def acepta(*ws):
    out = []
    for w in ws: out += [w, w.lower(), w.capitalize()]
    return out


N1 = {**ESTILO,
"objetivo": "Vas a nombrar mascotas en inglés.",
"vas_a_ver": ["DOG: perro", "CAT: gato", "FISH: pez"],
"secciones": [
 S(1, "Mascotas", [
  D("Mascota", "Animal que vive en casa con nosotros."),
  P("Perro es <b>DOG</b>, gato es <b>CAT</b> y pez es <b>FISH</b>."),
  IMG("Mascotas", "En inglés.", FG.tiras(["PERRO = DOG", "GATO = CAT", "PEZ = FISH"], numeros=False, cols=1)),
 ]),
 S(1, "Cuidarlas", [
  P("Las mascotas necesitan comida, agua y <b>cariño</b>."),
  IMG("Cuidar", "Lo que necesitan.", FG.tiras(["COMIDA", "AGUA", "CARIÑO"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las mascotas de los chicos. Las vas a usar en la carpeta."),
  IMG("Las mascotas", "¿Qué animal es?", FG.tiras(["TOMI TIENE UN PERRO", "SOFI TIENE UN GATO", "LEO TIENE UN PEZ"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La mascota de Tomi", "planteo": "Tomi tiene un perro.", "pasos": ["Se llama Toby.", "Tomi dice: MY DOG!", "¡Qué lindo!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Gato en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu mascota", "planteo": "Dibujá una mascota y escribí su nombre en inglés."},
"tip": {"titulo": "Sonidos", "texto": "Pensá en cómo suena cada animal."},
"ojo": ["DOG es perro.", "CAT es gato."],
"resumen": [{"titulo": "DOG", "texto": "Perro."}, {"titulo": "CAT", "texto": "Gato."}, {"titulo": "FISH", "texto": "Pez."}],
"glosario": [{"palabra": "DOG", "significado": "Perro."}, {"palabra": "FISH", "significado": "Pez."}],
"carpeta": ["Tomi tiene un perro. ¿Cómo se dice?", "Leo tiene un pez. ¿Cómo se dice?", "Sofi tiene un gato y dice DOG. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("DOG"), acepta("FISH"), acepta("CAT")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "CAT.", "solo": "Tu dibujo.", "carpeta": ["DOG.", "FISH.", "CAT."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a nombrar animales de la granja en inglés.",
"vas_a_ver": ["COW y PIG", "HORSE y SHEEP", "Lo que nos dan"],
"secciones": [
 S(1, "En la granja", [
  D("Granja", "Lugar del campo donde viven animales."),
  P("En la granja viven <b>COW</b>, <b>PIG</b>, <b>HORSE</b> y <b>SHEEP</b>."),
  IMG("La granja", "En inglés.", FG.tiras(["VACA = COW", "CHANCHO = PIG", "CABALLO = HORSE", "OVEJA = SHEEP"], numeros=False, cols=1)),
 ]),
 S(1, "Lo que nos dan", [
  P("La <b>COW</b> nos da leche. La <b>SHEEP</b> nos da lana."),
  IMG("Nos dan", "Cosas del campo.", FG.tiras(["COW: LECHE", "SHEEP: LANA", "HEN: HUEVOS"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la granja de Tomi. La vas a usar en la carpeta."),
  IMG("La granja de Tomi", "¿Qué animal es?", FG.tiras(["DA LECHE", "DA LANA", "TIENE CRIN Y GALOPA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi en la granja", "planteo": "Tomi ve una vaca.", "pasos": ["La vaca come pasto.", "Tomi dice: COW!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Caballo en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu granja", "planteo": "Dibujá una granja y escribí COW, PIG, HORSE y SHEEP."},
"tip": {"titulo": "Pensá en lo que dan", "texto": "COW da leche, SHEEP da lana."},
"ojo": ["PIG es chancho.", "HORSE es caballo."],
"resumen": [{"titulo": "COW / PIG", "texto": "Vaca y chancho."}, {"titulo": "HORSE", "texto": "Caballo."}, {"titulo": "SHEEP", "texto": "Oveja."}],
"glosario": [{"palabra": "COW", "significado": "Vaca."}, {"palabra": "SHEEP", "significado": "Oveja."}],
"carpeta": ["Este animal da leche. ¿Cuál es?", "Este animal da lana. ¿Cuál es?", "Tomi ve un caballo y dice PIG. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("COW"), acepta("SHEEP"), acepta("HORSE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "HORSE.", "solo": "Tu granja.", "carpeta": ["COW.", "SHEEP.", "HORSE."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a nombrar animales salvajes en inglés.",
"vas_a_ver": ["LION y ELEPHANT", "MONKEY y GIRAFFE", "Granja o selva"],
"secciones": [
 S(1, "Animales salvajes", [
  D("Salvaje", "Animal que vive libre en la naturaleza."),
  P("En la selva viven <b>LION</b>, <b>ELEPHANT</b>, <b>MONKEY</b> y <b>GIRAFFE</b>."),
  IMG("Salvajes", "En inglés.", FG.tiras(["LEÓN = LION", "ELEFANTE = ELEPHANT", "MONO = MONKEY", "JIRAFA = GIRAFFE"], numeros=False, cols=1)),
 ]),
 S(1, "¿Dónde viven?", [
  P("La <b>COW</b> vive en la granja. El <b>LION</b> vive en la selva."),
  IMG("Dos lugares", "Granja y selva.", FG.tiras(["GRANJA: COW, PIG", "SELVA: LION, MONKEY"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas de Sofi. Las vas a usar en la carpeta."),
  IMG("Pistas", "¿Qué animal es?", FG.tiras(["CUELLO MUY LARGO", "TROMPA GRANDE", "COME BANANAS"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi en el zoológico", "planteo": "Sofi ve un animal con melena.", "pasos": ["Ruge fuerte.", "Sofi dice: LION!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Mono en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu animal", "planteo": "Elegí tu animal salvaje preferido y decilo en inglés."},
"tip": {"titulo": "Pistas", "texto": "Mirá cómo es el animal para adivinar."},
"ojo": ["LION es león.", "GIRAFFE es jirafa."],
"resumen": [{"titulo": "LION / ELEPHANT", "texto": "León y elefante."}, {"titulo": "MONKEY", "texto": "Mono."}, {"titulo": "GIRAFFE", "texto": "Jirafa."}],
"glosario": [{"palabra": "LION", "significado": "León."}, {"palabra": "MONKEY", "significado": "Mono."}],
"carpeta": ["Tiene el cuello muy largo. ¿Cuál es?", "Tiene una trompa grande. ¿Cuál es?", "Sofi ve un mono comiendo bananas y dice LION. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("GIRAFFE", "GIRAFE"), acepta("ELEPHANT", "ELEFANT"), acepta("MONKEY")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "MONKEY.", "solo": "Tu animal.", "carpeta": ["GIRAFFE.", "ELEPHANT.", "MONKEY."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a adivinar animales por su sonido en inglés.",
"vas_a_ver": ["Los sonidos", "WHAT IS IT?", "Jugar a adivinar"],
"secciones": [
 S(1, "Sonidos en inglés", [
  D("Sonido", "Lo que se escucha: ruidos, voces, música."),
  P("En inglés, el perro hace <b>WOOF</b> y el gato hace <b>MEOW</b>."),
  IMG("Sonidos", "Así suenan.", FG.tiras(["DOG: WOOF", "CAT: MEOW", "COW: MOO", "DUCK: QUACK"], numeros=False, cols=1)),
 ]),
 S(1, "¿Qué es?", [
  P("Para adivinar preguntamos <b>WHAT IS IT?</b> y contestamos <b>IT IS A…</b>"),
  IMG("Adivinar", "Pregunta y respuesta.", FG.tiras(["WHAT IS IT?", "IT IS A DOG!"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Escuchá los sonidos de Tomi. Los vas a usar en la carpeta."),
  IMG("Los sonidos", "¿Quién es?", FG.tiras(["MOO!", "MEOW!", "QUACK!"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi adivina", "planteo": "Sofi hace: WOOF!", "pasos": ["Tomi: WHAT IS IT?", "Tomi piensa.", "Tomi: IT IS A DOG!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La vaca hace ___.", "pasos": ["___!"]},
"ejemplo_solo": {"titulo": "A jugar", "planteo": "Hacé un sonido de animal y que tu familia adivine en inglés."},
"tip": {"titulo": "Distintos", "texto": "En inglés los animales suenan distinto."},
"ojo": ["WOOF es el perro.", "MOO es la vaca."],
"resumen": [{"titulo": "WOOF / MEOW", "texto": "Perro y gato."}, {"titulo": "MOO / QUACK", "texto": "Vaca y pato."}, {"titulo": "WHAT IS IT?", "texto": "¿Qué es?"}],
"glosario": [{"palabra": "DUCK", "significado": "Pato."}, {"palabra": "WHAT", "significado": "Qué."}],
"carpeta": ["Escuchás MOO. ¿Qué animal es?", "Escuchás MEOW. ¿Qué animal es?", "Escuchás QUACK y Tomi dice IT IS A COW. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("COW", "IT IS A COW"), acepta("CAT", "IT IS A CAT"), acepta("IT IS A DUCK", "DUCK")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "MOO.", "solo": "Tu juego.", "carpeta": ["COW.", "CAT.", "IT IS A DUCK."]},
}

ACT = {
"1": [MC("PERRO EN INGLÉS ES…", ["DOG", "CAT", "FISH"], "DOG", "DOG ES PERRO.", n="recordar"),
      MC("LEO TIENE UNA MASCOTA QUE NADA. ¿CUÁL ES?", ["FISH", "DOG", "CAT"], "FISH", "EL PEZ NADA: FISH.", n="aplicar"),
      MC("SOFI TIENE UN GATO. ¿CÓMO SE DICE?", ["CAT", "DOG", "FISH"], "CAT", "GATO ES CAT.", n="aplicar")],
"2": [MC("ESTE ANIMAL DA LECHE. ¿CUÁL ES?", ["COW", "PIG", "HORSE"], "COW", "LA COW DA LECHE.", n="aplicar"),
      MC("TOMI VE UNA OVEJA. ¿QUÉ DICE?", ["SHEEP", "COW", "PIG"], "SHEEP", "OVEJA ES SHEEP.", n="aplicar")],
"3": [MC("TIENE EL CUELLO MUY LARGO. ¿CUÁL ES?", ["GIRAFFE", "LION", "MONKEY"], "GIRAFFE", "LA JIRAFA ES GIRAFFE.", n="aplicar"),
      MC("¿DÓNDE VIVE EL LION?", ["EN LA SELVA", "EN LA GRANJA", "EN UNA PECERA"], "EN LA SELVA", "EL LEÓN ES SALVAJE.", n="analizar")],
"4": [MC("ESCUCHÁS WOOF. ¿QUÉ ANIMAL ES?", ["DOG", "CAT", "COW"], "DOG", "EL PERRO HACE WOOF.", n="aplicar"),
      MC("SOFI DICE QUE EL GATO HACE MOO. ¿QUÉ ESTÁ MAL?", ["EL GATO HACE MEOW", "ESTÁ BIEN", "EL GATO HACE QUACK"], "EL GATO HACE MEOW", "MOO ES LA VACA.", n="error")],
"5": [MC("RELÁMPAGO. GATO EN INGLÉS ES…", ["CAT", "DOG", "PIG"], "CAT", "CAT.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. CABALLO EN INGLÉS ES…", ["HORSE", "SHEEP", "LION"], "HORSE", "HORSE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. TIENE TROMPA. ES UN…", ["ELEPHANT", "MONKEY", "FISH"], "ELEPHANT", "ELEPHANT.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ESCUCHÁS QUACK. ES UN…", ["DUCK", "DOG", "COW"], "DUCK", "DUCK.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("PEZ EN INGLÉS ES…", ["FISH", "DOG", "CAT"], "FISH", "FISH ES PEZ.", n="recordar")],
 [1, SA("TOMI TIENE UN PERRO. ESCRIBÍ PERRO EN INGLÉS.", acepta("DOG"), "DOG.", n="aplicar")],
 [1, MC("SOFI TIENE UN GATO Y DICE FISH. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR CAT", "ESTÁ BIEN", "DEBE DECIR DOG"], "DEBE DECIR CAT", "GATO ES CAT.", n="error")],
 [2, MC("CHANCHO EN INGLÉS ES…", ["PIG", "COW", "HORSE"], "PIG", "PIG ES CHANCHO.", n="recordar")],
 [2, SA("ESTE ANIMAL DA LANA. ESCRIBÍ SU NOMBRE EN INGLÉS.", acepta("SHEEP"), "SHEEP.", n="aplicar")],
 [2, MC("TOMI VE UN CABALLO. ¿QUÉ DICE?", ["HORSE", "PIG", "SHEEP"], "HORSE", "CABALLO ES HORSE.", n="aplicar")],
 [3, MC("LEÓN EN INGLÉS ES…", ["LION", "MONKEY", "GIRAFFE"], "LION", "LION ES LEÓN.", n="recordar")],
 [3, SA("COME BANANAS Y TREPA ÁRBOLES. ESCRIBÍ SU NOMBRE EN INGLÉS.", acepta("MONKEY"), "MONKEY.", n="aplicar")],
 [3, MC("TOMI DICE QUE LA COW VIVE EN LA SELVA. ¿QUÉ ESTÁ MAL?", ["VIVE EN LA GRANJA", "ESTÁ BIEN", "VIVE EN EL MAR"], "VIVE EN LA GRANJA", "LA COW ES DE GRANJA.", n="error")],
 [4, MC("WHAT IS IT QUIERE DECIR…", ["¿QUÉ ES?", "¿QUIÉN ES?", "¿DÓNDE ESTÁ?"], "¿QUÉ ES?", "WHAT ES QUÉ.", n="recordar")],
 [4, MC("ESCUCHÁS MOO. ¿QUÉ DECÍS?", ["IT IS A COW", "IT IS A DOG", "IT IS A CAT"], "IT IS A COW", "LA VACA HACE MOO.", n="aplicar")],
 [4, MC("ESCUCHÁS MEOW. ¿QUÉ DECÍS?", ["IT IS A CAT", "IT IS A DUCK", "IT IS A PIG"], "IT IS A CAT", "EL GATO HACE MEOW.", n="aplicar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: Animals", "examen_titulo": "Nivel jefe: Animals",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
