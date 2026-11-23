# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 10 · Project: My Little Book of English. Genera mision-10.json.
Regla de primeros años. Metáfora: el librito de inglés de Sofi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 elegir mis palabras · 2 dibujar y nombrar · 3 grabar mi voz · 4 compartir mi librito."""
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
"objetivo": "Vas a elegir tus palabras preferidas en inglés para tu librito.",
"vas_a_ver": ["Lo que aprendimos", "Elegir palabras", "Una por página"],
"secciones": [
 S(1, "Todo lo que aprendimos", [
  D("Proyecto", "Un trabajo especial que hacemos paso a paso."),
  P("Este año aprendimos muchas palabras en inglés. ¡Ahora armamos un <b>librito</b>!"),
  IMG("Lo que aprendimos", "Algunas palabras.", FG.tiras(["HELLO", "ONE, TWO, THREE", "RED, BLUE", "DOG, CAT"], numeros=False, cols=2)),
 ]),
 S(1, "Elegir", [
  P("Elegimos las palabras que <b>más nos gustan</b>. Una para cada página."),
  IMG("Mis palabras", "Ejemplo de Sofi.", FG.tiras(["PÁGINA 1: HELLO", "PÁGINA 2: RED", "PÁGINA 3: CAT", "PÁGINA 4: APPLE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los temas del año. Los vas a usar en la carpeta."),
  IMG("Temas del año", "¿Qué palabra elegís?", FG.tiras(["UN COLOR", "UN ANIMAL", "UNA FRUTA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi elige", "planteo": "Sofi piensa en su librito.", "pasos": ["Le gustan los gatos.", "Elige: CAT.", "¡Primera página lista!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Mi color preferido en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu lista", "planteo": "Escribí 4 palabras en inglés que te gusten."},
"tip": {"titulo": "Las que más te gustan", "texto": "Elegí palabras que te hagan sonreír."},
"ojo": ["Una palabra por página.", "Elegí de temas distintos."],
"resumen": [{"titulo": "Proyecto", "texto": "Mi librito de inglés."}, {"titulo": "Elegir", "texto": "Mis palabras preferidas."}, {"titulo": "Páginas", "texto": "Una palabra en cada una."}],
"glosario": [{"palabra": "Proyecto", "significado": "Trabajo especial paso a paso."}, {"palabra": "BOOK", "significado": "Libro."}],
"carpeta": ["Elegí un color en inglés.", "Elegí un animal en inglés.", "Sofi eligió MANZANA para la página de frutas. ¿Cómo va en inglés?"],
"respuestas_carpeta": [acepta("RED", "BLUE", "YELLOW", "GREEN", "ORANGE", "PINK", "BLACK", "WHITE", "BROWN"), acepta("DOG", "CAT", "FISH", "COW", "PIG", "HORSE", "SHEEP", "LION", "ELEPHANT", "MONKEY", "GIRAFFE", "DUCK"), acepta("APPLE", "AN APPLE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "Tu color.", "solo": "Tus palabras.", "carpeta": ["Un color.", "Un animal.", "APPLE."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a dibujar y nombrar en inglés cada página.",
"vas_a_ver": ["Dibujar", "Escribir el nombre", "Revisar"],
"secciones": [
 S(1, "Dibujo y nombre", [
  D("Rótulo", "Nombre que escribimos al lado de un dibujo."),
  P("En cada página hacemos un <b>dibujo</b> y escribimos su nombre en inglés."),
  IMG("Una página", "Dibujo y rótulo.", FG.tiras(["DIBUJO DE UN GATO", "ROTULO: CAT"], numeros=False, cols=1)),
 ]),
 S(1, "Paso a paso", [
  P("Primero <b>dibujo</b>, después <b>escribo</b> y al final <b>pinto</b>."),
  IMG("Pasos", "En orden.", FG.tiras(["DIBUJO", "ESCRIBO EL NOMBRE", "PINTO"], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las páginas de Tomi. Las vas a usar en la carpeta."),
  IMG("Las páginas de Tomi", "¿Qué nombre va?", FG.tiras(["DIBUJÓ UN PERRO", "DIBUJÓ UN SOL AMARILLO", "DIBUJÓ UNA PELOTA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La página de Sofi", "planteo": "Sofi dibuja una manzana.", "pasos": ["La pinta de rojo.", "Escribe: APPLE.", "¡Página lista!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Dibujo de un perro. Rótulo: ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu página", "planteo": "Hacé la primera página de tu librito con dibujo y nombre."},
"tip": {"titulo": "Letra clara", "texto": "Escribí en imprenta mayúscula grande."},
"ojo": ["Primero el dibujo.", "Después el nombre."],
"resumen": [{"titulo": "Dibujar", "texto": "Lo que elegí."}, {"titulo": "Rotular", "texto": "Escribir el nombre."}, {"titulo": "Pintar", "texto": "Con colores."}],
"glosario": [{"palabra": "Rótulo", "significado": "Nombre al lado del dibujo."}, {"palabra": "DRAW", "significado": "Dibujar."}],
"carpeta": ["Tomi dibujó un perro. ¿Qué rótulo va?", "Tomi dibujó una pelota. ¿Qué rótulo va?", "Tomi dibujó un sol amarillo y escribió BLUE. ¿Qué debería escribir?"],
"respuestas_carpeta": [acepta("DOG"), acepta("BALL"), acepta("YELLOW", "SUN")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "DOG.", "solo": "Tu página.", "carpeta": ["DOG.", "BALL.", "YELLOW."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a grabar tu voz diciendo las palabras del librito.",
"vas_a_ver": ["Escuchar", "Repetir", "Grabar"],
"secciones": [
 S(1, "Mi voz", [
  D("Grabar", "Guardar un sonido para escucharlo después."),
  P("Vamos a <b>grabar</b> nuestra voz diciendo cada palabra del librito."),
  IMG("Grabar", "Paso a paso.", FG.tiras(["ESCUCHO", "REPITO", "GRABO"], numeros=True, cols=1)),
 ]),
 S(1, "Hablar claro", [
  P("Hablamos <b>despacio</b> y <b>fuerte</b>, para que se entienda."),
  IMG("Cómo hablar", "Para que se entienda.", FG.tiras(["DESPACIO", "FUERTE", "CLARO"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá cómo graba Sofi. Lo vas a usar en la carpeta."),
  IMG("Sofi graba", "Su página.", FG.tiras(["PÁGINA DE LA MANZANA", "PÁGINA DEL GATO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi graba", "planteo": "Sofi abre su página del gato.", "pasos": ["Escucha: CAT.", "Repite: CAT.", "Graba: THIS IS A CAT!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Primero escucho, después ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu grabación", "planteo": "Con ayuda de un grande, grabá tu voz diciendo tus palabras."},
"tip": {"titulo": "Practicá", "texto": "Decí la palabra tres veces antes de grabar."},
"ojo": ["Hablá despacio.", "Hablá fuerte y claro."],
"resumen": [{"titulo": "Escuchar", "texto": "Cómo suena."}, {"titulo": "Repetir", "texto": "Practicar."}, {"titulo": "Grabar", "texto": "Guardar mi voz."}],
"glosario": [{"palabra": "Grabar", "significado": "Guardar un sonido."}, {"palabra": "VOICE", "significado": "Voz."}],
"carpeta": ["Sofi graba la página de la manzana. ¿Qué dice?", "Sofi graba la página del gato. ¿Qué dice?", "Tomi graba muy bajito y rápido. ¿Cómo debería hablar?"],
"respuestas_carpeta": [acepta("APPLE", "THIS IS AN APPLE", "AN APPLE"), acepta("CAT", "THIS IS A CAT", "A CAT"), acepta("DESPACIO Y FUERTE", "FUERTE Y DESPACIO", "DESPACIO", "FUERTE", "CLARO")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "Repito.", "solo": "Tu grabación.", "carpeta": ["APPLE.", "CAT.", "DESPACIO Y FUERTE."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a mostrar tu librito en inglés a tus compañeros.",
"vas_a_ver": ["Presentar el librito", "THIS IS MY BOOK", "Escuchar a los demás"],
"secciones": [
 S(1, "Mostrar", [
  D("Compartir", "Mostrar lo que hicimos a otras personas."),
  P("Para mostrar decimos: <b>THIS IS MY BOOK!</b> Quiere decir: ¡este es mi libro!"),
  IMG("Presentar", "Así empezamos.", FG.tiras(["HELLO!", "THIS IS MY BOOK!", "GOODBYE!"], numeros=True, cols=1)),
 ]),
 S(1, "Escuchar", [
  P("Cuando otro presenta, escuchamos y decimos <b>I LIKE YOUR BOOK!</b>"),
  IMG("Felicitar", "Con respeto.", FG.tiras(["I LIKE YOUR BOOK!", "VERY GOOD!"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la presentación de Tomi. La vas a usar en la carpeta."),
  IMG("Tomi presenta", "Su librito.", FG.tiras(["SALUDA", "MUESTRA SU LIBRO", "SE DESPIDE"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi presenta", "planteo": "Sofi pasa al frente.", "pasos": ["Dice: HELLO!", "Muestra: THIS IS MY BOOK!", "Al final: GOODBYE!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "THIS IS MY ___!", "pasos": ["THIS IS MY ___!"]},
"ejemplo_solo": {"titulo": "En casa", "planteo": "Mostrale tu librito a tu familia en inglés."},
"tip": {"titulo": "Orgullo", "texto": "¡Mostrá tu librito con orgullo!"},
"ojo": ["Primero saludamos.", "Al final nos despedimos."],
"resumen": [{"titulo": "THIS IS MY BOOK", "texto": "Este es mi libro."}, {"titulo": "I LIKE YOUR BOOK", "texto": "Me gusta tu libro."}, {"titulo": "Compartir", "texto": "Mostrar y escuchar."}],
"glosario": [{"palabra": "BOOK", "significado": "Libro."}, {"palabra": "YOUR", "significado": "Tu."}],
"carpeta": ["Tomi muestra su librito. ¿Qué dice?", "A Sofi le gusta el librito de Tomi. ¿Qué dice?", "Tomi empieza su presentación con GOODBYE. ¿Qué debería decir primero?"],
"respuestas_carpeta": [acepta("THIS IS MY BOOK", "THIS IS MY BOOK!"), acepta("I LIKE YOUR BOOK", "I LIKE YOUR BOOK!"), acepta("HELLO", "HELLO!", "HI", "HI!")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "BOOK.", "solo": "Tu presentación.", "carpeta": ["THIS IS MY BOOK!", "I LIKE YOUR BOOK!", "HELLO!"]},
}

ACT = {
"1": [MC("SOFI ELIGE UN ANIMAL PARA SU LIBRITO. ¿CUÁL ES EN INGLÉS?", ["CAT", "RED", "ONE"], "CAT", "CAT ES UN ANIMAL.", n="aplicar"),
      MC("TOMI ELIGE UNA FRUTA. ¿CUÁL ES?", ["BANANA", "BLUE", "DOG"], "BANANA", "BANANA ES UNA FRUTA.", n="aplicar")],
"2": [MC("TOMI DIBUJÓ UN PERRO. ¿QUÉ ESCRIBE?", ["DOG", "CAT", "BALL"], "DOG", "PERRO ES DOG.", n="aplicar"),
      ORD("ORDENÁ LOS PASOS.", ["PINTO", "DIBUJO", "ESCRIBO EL NOMBRE"], ["DIBUJO", "ESCRIBO EL NOMBRE", "PINTO"], "DIBUJO, ESCRIBO Y PINTO.", n="analizar")],
"3": [MC("¿CÓMO HABLAMOS AL GRABAR?", ["DESPACIO Y FUERTE", "MUY BAJITO", "MUY RÁPIDO"], "DESPACIO Y FUERTE", "ASÍ SE ENTIENDE.", n="aplicar"),
      MC("SOFI GRABA LA PÁGINA DEL PERRO. ¿QUÉ DICE?", ["DOG", "APPLE", "RED"], "DOG", "PERRO ES DOG.", n="aplicar")],
"4": [MC("TOMI MUESTRA SU LIBRITO. ¿QUÉ DICE?", ["THIS IS MY BOOK", "I AM SAD", "GOODBYE"], "THIS IS MY BOOK", "ASÍ PRESENTA.", n="aplicar"),
      MC("SOFI DICE I LIKE YOUR BOOK. ¿QUÉ QUIERE DECIR?", ["ME GUSTA TU LIBRO", "TENGO UN LIBRO", "CHAU"], "ME GUSTA TU LIBRO", "LIKE ES GUSTAR.", n="aplicar")],
"5": [MC("RELÁMPAGO. LIBRO EN INGLÉS ES…", ["BOOK", "BAG", "BALL"], "BOOK", "BOOK.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. UN COLOR EN INGLÉS ES…", ["RED", "DOG", "MILK"], "RED", "RED.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. AL PRESENTAR, PRIMERO DECÍS…", ["HELLO", "GOODBYE", "YUCK"], "HELLO", "HELLO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ME GUSTA TU LIBRO ES…", ["I LIKE YOUR BOOK", "I HAVE A BOOK", "THIS IS A BOOK"], "I LIKE YOUR BOOK", "I LIKE YOUR BOOK.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("SOFI ELIGE UN NÚMERO. ¿CUÁL ES EN INGLÉS?", ["THREE", "CAT", "PINK"], "THREE", "THREE ES UN NÚMERO.", n="aplicar")],
 [1, SA("ELEGÍ UNA FRUTA Y ESCRIBILA EN INGLÉS.", acepta("APPLE", "BANANA", "ORANGE", "AN APPLE", "AN ORANGE", "A BANANA"), "APPLE, BANANA U ORANGE.", n="aplicar")],
 [1, MC("TOMI QUIERE UN ANIMAL Y ELIGE RED. ¿QUÉ ESTÁ MAL?", ["RED ES UN COLOR", "ESTÁ BIEN", "RED ES UNA FRUTA"], "RED ES UN COLOR", "UN ANIMAL ES DOG O CAT.", n="error")],
 [2, MC("UN RÓTULO ES…", ["EL NOMBRE DEL DIBUJO", "EL COLOR DEL DIBUJO", "UNA CANCIÓN DEL AÑO"], "EL NOMBRE DEL DIBUJO", "ASÍ NOMBRAMOS EL DIBUJO.", n="recordar")],
 [2, SA("DIBUJASTE UN GATO. ESCRIBÍ EL RÓTULO EN INGLÉS.", acepta("CAT"), "CAT.", n="aplicar")],
 [2, MC("SOFI DIBUJÓ UNA PELOTA Y ESCRIBIÓ DOLL. ¿QUÉ ESTÁ MAL?", ["DEBE ESCRIBIR BALL", "ESTÁ BIEN", "DEBE ESCRIBIR CAR"], "DEBE ESCRIBIR BALL", "PELOTA ES BALL.", n="error")],
 [3, MC("¿QUÉ HACEMOS ANTES DE GRABAR?", ["ESCUCHAR Y REPETIR", "DESPEDIRNOS", "PINTAR"], "ESCUCHAR Y REPETIR", "ASÍ PRACTICAMOS.", n="analizar")],
 [3, SA("GRABÁS LA PÁGINA DE LA MANZANA. ESCRIBÍ QUÉ DECÍS.", acepta("APPLE", "AN APPLE", "THIS IS AN APPLE"), "APPLE.", n="aplicar")],
 [3, MC("TOMI GRABA MUY BAJITO. ¿QUÉ LE FALTA?", ["HABLAR MÁS FUERTE", "HABLAR MÁS RÁPIDO", "NADA"], "HABLAR MÁS FUERTE", "FUERTE PARA QUE SE OIGA.", n="error")],
 [4, MC("THIS IS MY BOOK QUIERE DECIR…", ["ESTE ES MI LIBRO", "ME GUSTA TU LIBRO", "TENGO UN LÁPIZ"], "ESTE ES MI LIBRO", "THIS IS MY = ESTE ES MI.", n="recordar")],
 [4, MC("TERMINÁS DE PRESENTAR. ¿QUÉ DECÍS?", ["GOODBYE!", "HELLO!", "YUCK!"], "GOODBYE!", "AL FINAL: GOODBYE.", n="aplicar")],
 [4, MC("TE GUSTÓ EL LIBRITO DE TU AMIGO. ¿QUÉ DECÍS?", ["I LIKE YOUR BOOK!", "I AM SIX!", "IT IS RED!"], "I LIKE YOUR BOOK!", "ASÍ FELICITAMOS.", n="aplicar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 10, "estilo": "primeros",
     "practica": "Práctica general: My Little Book", "examen_titulo": "Nivel jefe: My Little Book",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
