# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 1 · Cómo crecemos y cambiamos. Genera mision-1.json.
Regla de primeros años: frases cortas, un dibujo por sección, consignas de carpeta para contar, unir, dibujar.
Metáfora del año: Tomi, científico explorador con su lupa (observa, pregunta y anota).
Niveles: 1 antes y ahora · 2 lo que necesita cada edad · 3 alimentos para crecer · 4 las vacunas y la salud."""
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
ETAPAS = [("Bebé", .5), ("Niño", 1.0), ("Adolescente", 1.4), ("Adulto", 1.7)]

N1 = {**ESTILO,
"objetivo": "Vas a ver cómo cambiaste desde que eras bebé.",
"vas_a_ver": ["Antes y ahora", "Lo que cambió", "Lo que sigue igual"],
"secciones": [
 S(1, "Antes y ahora", [
  P("Tomi, el científico, mira una foto de cuando era <b>bebé</b>."),
  P("Antes era chiquito. Ahora es más <b>alto</b> y más <b>fuerte</b>."),
  IMG("Crecemos", "De bebé a grande.", FG.crecimiento(ETAPAS)),
 ]),
 S(1, "Lo que cambió", [
  D("Crecer", "Es <b>cambiar</b>: el cuerpo se hace más grande y aprendemos cosas nuevas."),
  IMG("Tomi antes y ahora", "Cosas que cambiaron.", FG.tiras(["ANTES: GATEABA", "AHORA: CORRE", "ANTES: TOMABA LECHE", "AHORA: COME DE TODO"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Antes o ahora?", "Pensá en vos.", FG.nombres(["GATEAR", "LEER", "USAR PAÑALES"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Antes y ahora", "planteo": "¿Qué cambió en Tomi?", "pasos": ["Antes gateaba.", "Ahora corre.", "¡Creció!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Pensá en vos.", "pasos": ["Antes yo ___ .", "Ahora yo ___ ."]},
"ejemplo_solo": {"titulo": "Tu foto", "planteo": "Pedí una foto de cuando eras bebé y compará."},
"tip": {"titulo": "Mirá fotos", "texto": "Las fotos muestran cómo cambiamos."},
"ojo": ["Todos crecemos, cada uno a su ritmo.", "Algunas cosas siguen iguales: tu nombre."],
"resumen": [{"titulo": "Crecer", "texto": "Es cambiar."}, {"titulo": "Antes", "texto": "Bebé."}, {"titulo": "Ahora", "texto": "Más alto y fuerte."}],
"glosario": [{"palabra": "Crecer", "significado": "Hacerse más grande."}, {"palabra": "Gatear", "significado": "Caminar con manos y rodillas."}],
"carpeta": ["¿Qué tarjeta del dibujo hacías cuando eras bebé?", "¿Qué tarjeta hacés ahora?", "Tomi dice que todos crecen igual de rápido. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("GATEAR") + low("USAR PAÑALES") + low("usar panales"), low("LEER"), NO],
"soluciones": {"incompleto": "Por ejemplo: gateaba. Corro.", "solo": "Lo que cambió en vos.", "carpeta": ["GATEAR o USAR PAÑALES.", "LEER.", "No: cada uno a su ritmo."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer lo que necesita cada edad.",
"vas_a_ver": ["Las etapas de la vida", "Lo que necesita un bebé", "Lo que necesitamos todos"],
"secciones": [
 S(1, "Las etapas", [
  P("Primero somos <b>bebés</b>. Después <b>niños</b>, <b>adolescentes</b> y <b>adultos</b>."),
  IMG("Las etapas de la vida", "En orden.", FG.crecimiento(ETAPAS)),
 ]),
 S(1, "Lo que necesitan", [
  P("Un <b>bebé</b> necesita que lo alimenten, lo bañen y lo cuiden."),
  P("Todos necesitamos <b>comer bien</b>, <b>dormir</b>, <b>jugar</b> y que nos <b>quieran</b>."),
  IMG("Cada edad", "Lo que necesita.", FG.tiras(["BEBÉ: QUE LO CUIDEN", "NIÑO: JUGAR Y APRENDER", "ADULTO: TRABAJAR Y CUIDAR"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Quién lo necesita?", "Pensá en cada edad.", FG.nombres(["MAMADERA", "ESCUELA", "PAÑALES"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Necesidades", "planteo": "¿Qué necesita un bebé?", "pasos": ["No puede comer solo.", "Necesita que lo cuiden.", "Mamadera y abrazos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las etapas en orden.", "pasos": ["Bebé, niño, ___ , adulto."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "¿Hay un bebé o un abuelo en tu familia? ¿Qué necesita?"},
"tip": {"titulo": "Cuidarnos", "texto": "En cada edad necesitamos cuidados."},
"ojo": ["Los bebés no pueden solos.", "Los adultos también necesitan dormir y comer bien."],
"resumen": [{"titulo": "Etapas", "texto": "Bebé, niño, adolescente, adulto."}, {"titulo": "Bebé", "texto": "Que lo cuiden."}, {"titulo": "Todos", "texto": "Comer, dormir, jugar."}],
"glosario": [{"palabra": "Etapa", "significado": "Una parte de la vida."}, {"palabra": "Adolescente", "significado": "Entre niño y adulto."}],
"carpeta": ["¿Quién usa MAMADERA?", "¿Quién va a la ESCUELA como vos?", "Tomi ordenó: adulto, bebé, niño. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("EL BEBÉ") + low("BEBÉ") + low("bebe") + low("el bebe"), low("EL NIÑO") + low("NIÑO") + low("nino") + low("LOS NIÑOS") + low("YO"), NO],
"soluciones": {"incompleto": "ADOLESCENTE.", "solo": "Lo que necesita.", "carpeta": ["El bebé.", "El niño.", "No: bebé, niño, adolescente, adulto."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer los alimentos que ayudan a crecer.",
"vas_a_ver": ["Comer variado", "Grupos de alimentos", "El agua"],
"secciones": [
 S(1, "Comer variado", [
  P("Para crecer sanos necesitamos comer <b>de todo un poco</b>."),
  IMG("Alimentos", "Variados y ricos.", FG.dibujo_palabra([("manzana", "FRUTAS"), ("vaso", "LECHE"), ("caramelo", "DULCES")])),
 ]),
 S(1, "Grupos de alimentos", [
  P("<b>Frutas y verduras</b>, <b>leche y quesos</b>, <b>carnes y huevos</b>, <b>cereales</b>."),
  P("Las <b>golosinas</b>, solo de vez en cuando. Y mucha <b>agua</b>."),
  IMG("Los grupos", "Un poco de cada uno.", FG.tiras(["FRUTAS Y VERDURAS", "LECHE Y QUESOS", "CARNES Y HUEVOS", "CEREALES Y PAN"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los alimentos. Los vas a usar en la carpeta."),
  IMG("¿De qué grupo?", "Pensá en cada uno.", FG.nombres(["ZANAHORIA", "YOGUR", "HUEVO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Un plato variado", "planteo": "Almuerzo de Tomi.", "pasos": ["Arroz: cereal.", "Carne: carnes.", "Ensalada: verduras."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para tomar.", "pasos": ["La mejor bebida es el ___ ."]},
"ejemplo_solo": {"titulo": "Tu plato", "planteo": "Dibujá tu comida preferida y escribí de qué grupos es."},
"tip": {"titulo": "Colores en el plato", "texto": "Un plato con colores tiene de todo."},
"ojo": ["Las golosinas no ayudan a crecer.", "El agua es la mejor bebida."],
"resumen": [{"titulo": "Variado", "texto": "De todo un poco."}, {"titulo": "Grupos", "texto": "Frutas, leche, carnes, cereales."}, {"titulo": "Agua", "texto": "La mejor bebida."}],
"glosario": [{"palabra": "Alimento", "significado": "Lo que comemos para vivir."}, {"palabra": "Variado", "significado": "De muchos tipos."}],
"carpeta": ["¿De qué grupo es la ZANAHORIA?", "¿De qué grupo es el YOGUR?", "Tomi dice que puede comer solo golosinas. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("VERDURAS") + low("FRUTAS Y VERDURAS") + low("VERDURA"), low("LECHE Y QUESOS") + low("LECHE") + low("LÁCTEOS") + low("lacteos"), NO],
"soluciones": {"incompleto": "AGUA.", "solo": "Tu plato con sus grupos.", "carpeta": ["Verduras.", "Leche y quesos.", "No: hay que comer variado."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer cómo cuidamos la salud.",
"vas_a_ver": ["Las vacunas", "La libreta de vacunas", "Otros cuidados"],
"secciones": [
 S(1, "Las vacunas", [
  D("Vacuna", "Ayuda al cuerpo a <b>defenderse</b> de algunas enfermedades."),
  P("Se aplican en el <b>centro de salud</b>, en distintas edades."),
  IMG("Para cuidarnos", "Vacunas y controles.", FG.tiras(["VACUNAS", "CONTROLES CON EL DOCTOR"], numeros=False, cols=1)),
 ]),
 S(1, "La libreta", [
  P("Las vacunas se anotan en una <b>libreta</b> o <b>carnet</b>."),
  P("También nos cuidamos al <b>lavarnos las manos</b> y <b>dormir bien</b>."),
  IMG("Cuidados de todos los días", "Hábitos sanos.", FG.tiras(["LAVARSE LAS MANOS", "DORMIR BIEN", "COMER VARIADO", "JUGAR Y MOVERSE"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Cuida la salud?", "Pensá en cada una.", FG.nombres(["DORMIR BIEN", "NO LAVARSE", "VACUNARSE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Cuidarse", "planteo": "¿Qué hizo Tomi hoy por su salud?", "pasos": ["Se lavó las manos.", "Comió una fruta.", "¡Se cuidó!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las vacunas ayudan al cuerpo a…", "pasos": ["…___ de algunas enfermedades."]},
"ejemplo_solo": {"titulo": "Tu libreta", "planteo": "Con un adulto, mirá tu libreta de vacunas."},
"tip": {"titulo": "Todos los días", "texto": "Cuidar la salud es cosa de todos los días."},
"ojo": ["Las vacunas las pone el personal de salud.", "Lavarse las manos también protege."],
"resumen": [{"titulo": "Vacunas", "texto": "Ayudan a defenderse."}, {"titulo": "Libreta", "texto": "Ahí se anotan."}, {"titulo": "Hábitos", "texto": "Manos limpias, dormir, comer bien."}],
"glosario": [{"palabra": "Vacuna", "significado": "Ayuda al cuerpo a defenderse."}, {"palabra": "Hábito", "significado": "Algo que hacemos siempre."}],
"carpeta": ["¿Qué tarjetas del dibujo cuidan la salud?", "¿Qué tarjeta NO cuida la salud?", "Tomi dice que lavarse las manos no sirve. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("DORMIR BIEN Y VACUNARSE") + low("VACUNARSE Y DORMIR BIEN") + low("DORMIR BIEN, VACUNARSE"), low("NO LAVARSE"), NO],
"soluciones": {"incompleto": "DEFENDERSE.", "solo": "Tu libreta, mirada con un adulto.", "carpeta": ["Dormir bien y vacunarse.", "No lavarse.", "No: lavarse las manos nos protege."]},
}

ACT = {
"1": [MC("¿QUÉ HACÍAS CUANDO ERAS BEBÉ?", ["GATEABA", "LEÍA LIBROS", "ANDABA EN BICI"], "GATEABA", "LOS BEBÉS GATEAN.", n="aplicar"),
      TF("CRECER ES CAMBIAR.", "VERDADERO", "EL CUERPO Y LO QUE SABEMOS CAMBIAN.", n="recordar")],
"2": [ORD("ORDENÁ LAS ETAPAS.", ["ADULTO", "BEBÉ", "ADOLESCENTE", "NIÑO"], ["BEBÉ", "NIÑO", "ADOLESCENTE", "ADULTO"], "DE CHIQUITO A GRANDE.", n="analizar"),
      MC("¿QUIÉN NECESITA PAÑALES?", ["EL BEBÉ", "EL ADULTO"], "EL BEBÉ", "TODAVÍA NO VA AL BAÑO SOLO.", n="aplicar")],
"3": [UNI("UNÍ CADA ALIMENTO CON SU GRUPO.", [("MANZANA", "FRUTAS"), ("QUESO", "LÁCTEOS"), ("HUEVO", "CARNES Y HUEVOS")], "CADA UNO TIENE SU GRUPO.", n="analizar"),
      MC("¿CUÁL ES LA MEJOR BEBIDA?", ["EL AGUA", "LA GASEOSA"], "EL AGUA", "EL AGUA ES SANA.", n="recordar")],
"4": [TF("LAS VACUNAS AYUDAN AL CUERPO A DEFENDERSE.", "VERDADERO", "DE ALGUNAS ENFERMEDADES.", n="recordar"),
      MC("¿QUÉ CUIDA LA SALUD?", ["LAVARSE LAS MANOS", "NO DORMIR"], "LAVARSE LAS MANOS", "SACA LOS MICROBIOS.", n="aplicar")],
"5": [MC("RELÁMPAGO. CRECER ES…", ["CAMBIAR", "QUEDARSE IGUAL"], "CAMBIAR", "CAMBIAMOS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ VA PRIMERO?", ["BEBÉ", "ADULTO"], "BEBÉ", "LA PRIMERA ETAPA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LAS GOLOSINAS SE COMEN…", ["DE VEZ EN CUANDO", "TODO EL DÍA"], "DE VEZ EN CUANDO", "NO AYUDAN A CRECER.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LAS VACUNAS SE ANOTAN EN LA…", ["LIBRETA", "HELADERA"], "LIBRETA", "LA LIBRETA DE VACUNAS.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ CAMBIA CUANDO CRECEMOS?", ["EL CUERPO CRECE", "EL NOMBRE", "NADA DE NADA"], "EL CUERPO CRECE", "Y APRENDEMOS COSAS NUEVAS.", n="recordar")],
 [1, TF("TODOS CRECEMOS IGUAL DE RÁPIDO.", "FALSO", "CADA UNO A SU RITMO.", n="error")],
 [1, SA("ANTES GATEABA. AHORA… (ESCRIBÍ ALGO QUE HACÉS)", low("CORRO") + low("CAMINO") + low("LEO") + low("ESCRIBO") + low("SALTO") + low("JUEGO") + low("CORRE") + low("CAMINA"), "POR EJEMPLO: CORRO.", n="aplicar")],
 [2, ORD("ORDENÁ LAS ETAPAS.", ["NIÑO", "ADULTO", "BEBÉ"], ["BEBÉ", "NIÑO", "ADULTO"], "BEBÉ, NIÑO, ADULTO.", n="analizar")],
 [2, MC("¿QUÉ NECESITAMOS TODOS?", ["COMER, DORMIR Y JUGAR", "SOLO MIRAR TELE"], "COMER, DORMIR Y JUGAR", "Y QUE NOS QUIERAN.", n="aplicar")],
 [2, SA("¿QUIÉN USA MAMADERA?", low("EL BEBÉ") + low("BEBÉ") + low("bebe") + low("el bebe") + low("LOS BEBÉS"), "EL BEBÉ.", n="aplicar")],
 [3, UNI("UNÍ CADA ALIMENTO CON SU GRUPO.", [("ZANAHORIA", "VERDURAS"), ("YOGUR", "LÁCTEOS"), ("PAN", "CEREALES")], "CADA UNO TIENE SU GRUPO.", n="analizar")],
 [3, TF("PARA CRECER SANOS HAY QUE COMER VARIADO.", "VERDADERO", "DE TODO UN POCO.", n="recordar")],
 [3, MC("TOMI COME SOLO GOLOSINAS. ¿QUÉ LE FALTA?", ["COMER VARIADO", "MÁS GOLOSINAS"], "COMER VARIADO", "FRUTAS, VERDURAS, LECHE…", n="error")],
 [4, MC("¿DÓNDE SE PONEN LAS VACUNAS?", ["EN EL CENTRO DE SALUD", "EN LA PLAZA"], "EN EL CENTRO DE SALUD", "LAS PONE EL PERSONAL DE SALUD.", n="recordar")],
 [4, SA("ESCRIBÍ UN HÁBITO QUE CUIDA LA SALUD.", low("LAVARSE LAS MANOS") + low("LAVARME LAS MANOS") + low("DORMIR") + low("DORMIR BIEN") + low("COMER BIEN") + low("COMER VARIADO") + low("JUGAR") + low("VACUNARSE") + low("TOMAR AGUA") + low("BAÑARSE") + low("CEPILLARSE LOS DIENTES"), "POR EJEMPLO: LAVARSE LAS MANOS.", n="aplicar")],
 [4, TF("LAVARSE LAS MANOS NO SIRVE PARA NADA.", "FALSO", "NOS PROTEGE DE MICROBIOS.", n="error")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: cómo crecemos y cambiamos", "examen_titulo": "Nivel jefe: cómo crecemos y cambiamos",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
