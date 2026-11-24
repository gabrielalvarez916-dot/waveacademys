# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 2 · Artesanía e industria. Genera mision-2.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy investiga cómo se hacen los alfajores).
Niveles: 1 un alfajor a mano · 2 miles en una fábrica · 3 herramientas y máquinas · 4 el mismo producto en distintos lugares."""
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
TF = lambda p, ok, e, **k: {"t": "true_false", "p": p, "o": ["VERDADERO", "FALSO"], "r": {"correcta": ok}, "e": e, **k}
UNI = lambda p, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": [a for a, _ in pares], "derecha": [b for _, b in pares]}, "r": {"pares": dict(pares)}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
low = lambda w: [w, w.lower(), w.capitalize()]
NO = ["NO", "no", "No"]

N1 = {**ESTILO,
"objetivo": "Vas a ver cómo se hace un alfajor a mano.",
"vas_a_ver": ["Qué es artesanal", "Los pasos", "Pocos alfajores"],
"secciones": [
 S(1, "Hecho a mano", [
  D("Artesanal", "Hecho <b>a mano</b>, de a poco, por pocas personas."),
  P("Doña Elsa hace alfajores en su cocina. Lola la visita."),
  P("Doña Elsa aprendió la receta de su abuela. Usa harina, manteca, azúcar y huevos. Mide todo con una taza. Trabaja sola o con su hija."),
  IMG("Los pasos de Doña Elsa", "Todo a mano.", FG.tiras(["1. HACE LA MASA", "2. CORTA LAS TAPITAS", "3. LAS HORNEA", "4. PONE DULCE DE LECHE"], numeros=False)),
 ]),
 S(1, "Pocos y distintos", [
  P("Doña Elsa hace <b>pocos</b> alfajores por día. ¡Ninguno es igual a otro!"),
  P("Algunos salen más grandes y otros más chicos. Los vende a sus vecinos y en la feria del barrio."),
  IMG("Sus herramientas", "Simples y de cocina.", FG.nombres(["PALOTE", "CUCHARA", "HORNO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Qué va primero?", FG.tiras(["PONE DULCE DE LECHE", "HACE LA MASA", "HORNEA LAS TAPITAS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La masa", "planteo": "¿Cómo hace la masa Doña Elsa?", "pasos": ["Mezcla harina, manteca y azúcar.", "Amasa con las manos.", "La estira con el palote."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Artesanal quiere decir hecho a…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "¿Qué cosa se hace a mano en tu casa?"},
"tip": {"titulo": "Mirá las manos", "texto": "Si se hace con las manos, es artesanal."},
"ojo": ["Lo artesanal se hace de a poco.", "Cada pieza sale un poco distinta."],
"resumen": [{"titulo": "Artesanal", "texto": "Hecho a mano."}, {"titulo": "Pocos", "texto": "Se hacen de a poco."}, {"titulo": "Herramientas", "texto": "Simples."}],
"glosario": [{"palabra": "Palote", "significado": "Palo para estirar la masa."}, {"palabra": "Artesana", "significado": "Persona que hace cosas a mano."}],
"carpeta": ["De las tarjetas, ¿qué va primero?", "¿Qué va al final?", "Lola dice que Doña Elsa hace miles de alfajores por día. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("HACE LA MASA") + low("LA MASA"), low("PONE DULCE DE LECHE") + low("DULCE DE LECHE") + low("EL DULCE DE LECHE"), NO],
"soluciones": {"incompleto": "MANO.", "solo": "Algo hecho a mano.", "carpeta": ["Hace la masa.", "Pone dulce de leche.", "No: hace pocos."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver cómo se hacen miles de alfajores.",
"vas_a_ver": ["Qué es la industria", "La fábrica", "Muchos iguales"],
"secciones": [
 S(1, "La industria", [
  D("Industria", "Fábrica donde se hacen <b>muchos</b> productos iguales, con <b>máquinas</b>."),
  P("En la fábrica de alfajores trabajan muchas personas y muchas máquinas."),
  P("Unas personas controlan las máquinas. Otras revisan que los alfajores salgan bien. Otras los cargan en cajas para los camiones."),
  IMG("En la fábrica", "Todo en una cinta.", FG.tiras(["1. LA MÁQUINA HACE LA MASA", "2. OTRA CORTA LAS TAPITAS", "3. UN HORNO GIGANTE", "4. LA MÁQUINA ENVUELVE"], numeros=False)),
 ]),
 S(1, "Miles iguales", [
  P("La fábrica hace <b>miles</b> de alfajores por día, ¡todos iguales!"),
  P("Todos tienen el mismo tamaño y el mismo envoltorio. Viajan a kioscos de todo el país."),
  IMG("Artesanal o industrial", "Comparamos.", FG.tiras(["A MANO: POCOS Y DISTINTOS", "EN LA FÁBRICA: MILES E IGUALES"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Mano o fábrica?", "Pensá en cada una.", FG.tiras(["1. MILES DE ALFAJORES IGUALES", "2. POCOS ALFAJORES EN LA COCINA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La cinta", "planteo": "¿Cómo viajan los alfajores en la fábrica?", "pasos": ["Van sobre una cinta.", "Pasan por cada máquina.", "Salen envueltos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En la industria se usan…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Mirá el envoltorio", "planteo": "Buscá un alfajor de kiosco. ¿Qué fábrica lo hizo?"},
"tip": {"titulo": "Mirá cuántos", "texto": "Muchos e iguales: industria."},
"ojo": ["En la fábrica también trabajan personas.", "Las máquinas hacen todo más rápido."],
"resumen": [{"titulo": "Industria", "texto": "Fábrica con máquinas."}, {"titulo": "Miles", "texto": "Muchos productos."}, {"titulo": "Iguales", "texto": "Todos parecidos."}],
"glosario": [{"palabra": "Industria", "significado": "Fábrica con máquinas."}, {"palabra": "Cinta", "significado": "Camino que se mueve en la fábrica."}],
"carpeta": ["¿La tarjeta 1 es artesanal o industrial?", "¿Y la tarjeta 2?", "Lola dice que en la fábrica no trabaja ninguna persona. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("INDUSTRIAL") + low("INDUSTRIA") + low("DE FÁBRICA"), low("ARTESANAL") + low("A MANO"), NO],
"soluciones": {"incompleto": "MÁQUINAS.", "solo": "El nombre de la fábrica.", "carpeta": ["Industrial.", "Artesanal.", "No: trabajan personas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a comparar herramientas y máquinas.",
"vas_a_ver": ["Herramientas", "Máquinas", "Para qué sirven"],
"secciones": [
 S(1, "Herramientas", [
  D("Herramienta", "Objeto que se usa <b>con la mano</b>, como un palote."),
  P("La herramienta ayuda, pero la fuerza la pone la persona. El carpintero usa martillo. La costurera usa aguja."),
  IMG("Herramientas", "Se usan a mano.", FG.nombres(["PALOTE", "CUCHILLO", "MARTILLO"], cols=3)),
 ]),
 S(1, "Máquinas", [
  D("Máquina", "Aparato que trabaja con <b>motor</b> o electricidad."),
  P("La máquina hace todo mucho más <b>rápido</b>."),
  P("Batir a mano lleva mucho tiempo. Con una batidora, se termina enseguida. En la fábrica hay máquinas enormes. Las manejan personas que aprendieron a usarlas."),
  IMG("Máquinas", "Tienen motor.", FG.nombres(["BATIDORA", "HORNO GIGANTE", "CINTA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Herramienta o máquina?", "Pensá: ¿tiene motor?", FG.tiras(["1. UNA CUCHARA DE MADERA", "2. UNA BATIDORA ELÉCTRICA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Batir", "planteo": "¿Cómo bato los huevos?", "pasos": ["A mano, con un batidor.", "O con una batidora.", "¡La batidora es más rápida!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La máquina trabaja con…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "En tu cocina", "planteo": "Escribí una herramienta y una máquina de tu cocina."},
"tip": {"titulo": "¿Tiene motor?", "texto": "Con motor: máquina. Sin motor: herramienta."},
"ojo": ["Las máquinas las usan los adultos.", "Una herramienta necesita la mano."],
"resumen": [{"titulo": "Herramienta", "texto": "Se usa a mano."}, {"titulo": "Máquina", "texto": "Tiene motor."}, {"titulo": "Rápido", "texto": "La máquina."}],
"glosario": [{"palabra": "Motor", "significado": "Lo que hace mover una máquina."}, {"palabra": "Batidora", "significado": "Máquina que bate."}],
"carpeta": ["¿La pista 1 es herramienta o máquina?", "¿Y la pista 2?", "Lola dice que el martillo tiene motor. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("HERRAMIENTA") + low("UNA HERRAMIENTA") + low("ES HERRAMIENTA"), low("MÁQUINA") + low("maquina") + low("UNA MÁQUINA") + low("una maquina"), NO],
"soluciones": {"incompleto": "MOTOR.", "solo": "Una herramienta y una máquina.", "carpeta": ["Herramienta.", "Máquina.", "No: se usa a mano."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver el mismo producto en distintos lugares.",
"vas_a_ver": ["Alfajores distintos", "En la ciudad", "En el pueblo"],
"secciones": [
 S(1, "Alfajores de todos lados", [
  P("En la Argentina se hacen alfajores en <b>muchos lugares</b>."),
  P("Cada lugar los hace <b>distinto</b>: de maicena, con chocolate, con merengue."),
  IMG("Muchos alfajores", "El mismo producto, distinto.", FG.nombres(["DE MAICENA", "DE CHOCOLATE", "CON MERENGUE"], cols=3)),
 ]),
 S(1, "Pueblo y ciudad", [
  P("En un <b>pueblo</b> los hace una familia, a mano."),
  P("En una <b>ciudad grande</b>, una fábrica los hace con máquinas."),
  P("Los dos son alfajores ricos. Cambia la forma de hacerlos y cuántos se hacen."),
  IMG("Dos lugares", "Dos formas de hacer.", FG.tiras(["PUEBLO: FAMILIA Y A MANO", "CIUDAD: FÁBRICA Y MÁQUINAS"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Dónde se hizo?", "Pensá en cada una.", FG.tiras(["1. UNA FAMILIA LOS HACE EN SU CASA", "2. UNA MÁQUINA LOS ENVUELVE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El dulce de leche", "planteo": "¿Dónde se hace?", "pasos": ["En el campo, a mano, en una olla.", "En la ciudad, en una fábrica.", "¡Es el mismo producto!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el pueblo, los alfajores los hace una…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntale a un adulto qué alfajor le gusta más."},
"tip": {"titulo": "Mismo producto", "texto": "Puede hacerse a mano o en fábrica."},
"ojo": ["Los dos modos son trabajo.", "Cada lugar tiene su receta."],
"resumen": [{"titulo": "Pueblo", "texto": "Familia y a mano."}, {"titulo": "Ciudad", "texto": "Fábrica y máquinas."}, {"titulo": "Distintos", "texto": "Cada lugar con su receta."}],
"glosario": [{"palabra": "Receta", "significado": "Cómo se prepara una comida."}, {"palabra": "Taller", "significado": "Lugar chico donde se hacen cosas a mano."}],
"carpeta": ["¿La tarjeta 1 es del pueblo o de la fábrica?", "¿Y la tarjeta 2?", "Lola dice que los alfajores son iguales en todos lados. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PUEBLO") + low("DEL PUEBLO") + low("EL PUEBLO"), low("FÁBRICA") + low("fabrica") + low("DE LA FÁBRICA") + low("de la fabrica") + low("LA FÁBRICA"), NO],
"soluciones": {"incompleto": "FAMILIA.", "solo": "El alfajor favorito.", "carpeta": ["Del pueblo.", "De la fábrica.", "No: cada lugar los hace distinto."]},
}

ACT = {
"1": [ORD("ORDENÁ: EL ALFAJOR DE DOÑA ELSA.", ["HORNEA", "HACE LA MASA", "PONE DULCE DE LECHE"], ["HACE LA MASA", "HORNEA", "PONE DULCE DE LECHE"], "PRIMERO LA MASA.", n="analizar"),
      TF("ARTESANAL QUIERE DECIR HECHO A MANO.", "VERDADERO", "DE A POCO.", n="recordar")],
"2": [MC("EN LA FÁBRICA SE HACEN…", ["MILES IGUALES", "POCOS DISTINTOS"], "MILES IGUALES", "CON MÁQUINAS.", n="aplicar"),
      TF("EN LA FÁBRICA NO TRABAJAN PERSONAS.", "FALSO", "TRABAJAN MUCHAS PERSONAS.", n="error")],
"3": [UNI("UNÍ: ¿HERRAMIENTA O MÁQUINA?", [("PALOTE", "HERRAMIENTA"), ("BATIDORA", "MÁQUINA")], "¿TIENE MOTOR?", n="analizar"),
      MC("JUANA BATE CON BATIDORA Y PEDRO A MANO. ¿QUIÉN TERMINA PRIMERO?", ["JUANA", "PEDRO"], "JUANA", "LA MÁQUINA ES MÁS RÁPIDA.", n="analizar")],
"4": [MC("EN EL PUEBLO, LOS ALFAJORES LOS HACE…", ["UNA FAMILIA", "UNA CINTA"], "UNA FAMILIA", "A MANO.", n="aplicar"),
      UNI("UNÍ CADA LUGAR.", [("PUEBLO", "A MANO"), ("CIUDAD", "CON MÁQUINAS")], "DOS FORMAS DE HACER.", n="analizar")],
"5": [MC("RELÁMPAGO. HECHO A MANO ES…", ["ARTESANAL", "INDUSTRIAL"], "ARTESANAL", "COMO DOÑA ELSA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA FÁBRICA USA…", ["MÁQUINAS", "SOLO LAS MANOS"], "MÁQUINAS", "Y HACE MILES.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL PALOTE ES…", ["HERRAMIENTA", "MÁQUINA"], "HERRAMIENTA", "NO TIENE MOTOR.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL MISMO PRODUCTO…", ["CAMBIA SEGÚN EL LUGAR", "ES IGUAL EN TODOS LADOS"], "CAMBIA SEGÚN EL LUGAR", "CADA UNO CON SU RECETA.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ QUIERE DECIR ARTESANAL?", ["HECHO A MANO", "HECHO CON MOTOR"], "HECHO A MANO", "DE A POCO.", n="recordar")],
 [1, SA("¿CON QUÉ ESTIRA LA MASA DOÑA ELSA?", low("PALOTE") + low("EL PALOTE") + low("CON EL PALOTE") + low("UN PALOTE"), "CON EL PALOTE.", n="aplicar")],
 [1, TF("DOÑA ELSA HACE MILES DE ALFAJORES POR DÍA.", "FALSO", "HACE POCOS.", n="error")],
 [2, MC("¿QUÉ ES LA INDUSTRIA?", ["FÁBRICA CON MÁQUINAS", "UNA COCINA CHICA"], "FÁBRICA CON MÁQUINAS", "HACE MUCHOS IGUALES.", n="recordar")],
 [2, UNI("UNÍ CADA FORMA DE HACER.", [("A MANO", "POCOS Y DISTINTOS"), ("FÁBRICA", "MILES E IGUALES")], "COMPARÁ.", n="analizar")],
 [2, SA("¿SOBRE QUÉ VIAJAN LOS ALFAJORES EN LA FÁBRICA?", low("CINTA") + low("UNA CINTA") + low("LA CINTA"), "SOBRE UNA CINTA.", n="aplicar")],
 [3, MC("¿QUÉ TIENE UNA MÁQUINA?", ["MOTOR", "PLUMAS"], "MOTOR", "O ELECTRICIDAD.", n="recordar")],
 [3, SA("PARA ESTIRAR LA MASA A MANO, ¿QUÉ HERRAMIENTA USÁS?", low("PALOTE") + low("CUCHARA") + low("CUCHILLO") + low("BATIDOR") + low("TENEDOR") + low("EL PALOTE") + low("LA CUCHARA") + low("UNA CUCHARA"), "EL PALOTE.", n="aplicar")],
 [3, TF("LUIS DICE QUE EL MARTILLO TIENE MOTOR.", "FALSO", "ES UNA HERRAMIENTA.", n="error")],
 [4, MC("EN LA CIUDAD GRANDE, LOS ALFAJORES LOS HACE…", ["UNA FÁBRICA", "UNA ABUELA SOLA"], "UNA FÁBRICA", "CON MÁQUINAS.", n="aplicar")],
 [4, TF("CADA LUGAR TIENE SU RECETA.", "VERDADERO", "POR ESO SON DISTINTOS.", n="recordar")],
 [4, TF("LOS ALFAJORES SON IGUALES EN TODOS LADOS.", "FALSO", "HAY DE MAICENA, DE CHOCOLATE…", n="error")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: artesanía e industria", "examen_titulo": "Nivel jefe: artesanía e industria",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
