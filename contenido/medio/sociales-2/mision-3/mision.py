# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 3 · Normas que protegen a trabajadores y consumidores. Genera mision-3.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy investiga las reglas que nos cuidan).
Niveles: 1 normas de seguridad · 2 etiquetas y vencimiento · 3 derechos de los consumidores · 4 trabajos con y sin descanso."""
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
"objetivo": "Vas a conocer las normas que cuidan a los trabajadores.",
"vas_a_ver": ["Qué es una norma", "Ropa que protege", "Trabajar seguro"],
"secciones": [
 S(1, "Las normas", [
  D("Norma", "Una <b>regla</b> que todos tienen que cumplir."),
  P("En el trabajo, las normas de <b>seguridad</b> cuidan a las personas."),
  P("El casco protege la cabeza si cae algo. Los guantes cuidan las manos. Las botas fuertes cuidan los pies."),
  IMG("Para trabajar seguro", "Cada trabajo se protege.", FG.tiras(["ALBAÑIL: CASCO", "BOMBERA: TRAJE ESPECIAL", "COCINERO: GORRO Y DELANTAL"], numeros=False, cols=1)),
 ]),
 S(1, "Más cuidados", [
  P("También hay <b>carteles</b> que avisan peligros y salidas."),
  IMG("Carteles del trabajo", "Avisan y cuidan.", FG.nombres(["PELIGRO", "SALIDA", "USAR CASCO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué se pone?", "Pensá en cada trabajo.", FG.tiras(["1. UN ALBAÑIL EN UNA OBRA", "2. UNA COCINERA EN UNA FÁBRICA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "En la obra", "planteo": "¿Cómo se cuida el albañil?", "pasos": ["Se pone el casco.", "Usa botas fuertes.", "Respeta los carteles."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Una norma es una…", "pasos": ["…___ que todos cumplen."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá un cartel de seguridad en tu escuela. ¿Qué dice?"},
"tip": {"titulo": "Mirá los carteles", "texto": "Los carteles de seguridad nos avisan."},
"ojo": ["Las normas cuidan a todos.", "Cada trabajo tiene su protección."],
"resumen": [{"titulo": "Norma", "texto": "Regla para todos."}, {"titulo": "Seguridad", "texto": "Cuida a las personas."}, {"titulo": "Protección", "texto": "Casco, guantes, gorro."}],
"glosario": [{"palabra": "Norma", "significado": "Regla que se cumple."}, {"palabra": "Seguridad", "significado": "Estar protegido."}],
"carpeta": ["¿Qué se pone el albañil de la pista 1?", "¿Qué se pone la cocinera de la pista 2?", "Lola dice que las normas no sirven para nada. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("CASCO") + low("UN CASCO") + low("EL CASCO"), low("GORRO") + low("UN GORRO") + low("GORRO Y DELANTAL") + low("DELANTAL") + low("EL GORRO"), NO],
"soluciones": {"incompleto": "REGLA.", "solo": "Lo que dice el cartel.", "carpeta": ["Un casco.", "Gorro y delantal.", "No: cuidan a las personas."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a leer una etiqueta.",
"vas_a_ver": ["Qué tiene una etiqueta", "La fecha de vencimiento", "Elegir bien"],
"secciones": [
 S(1, "La etiqueta", [
  P("Los productos tienen una <b>etiqueta</b> con información."),
  IMG("La etiqueta del yogur", "Así se lee.", FG.ficha([("Nombre:", "YOGUR DE FRUTILLA"), ("Ingredientes:", "leche, frutilla"), ("Peso:", "190 g"), ("Vence:", "20/12")], titulo="Etiqueta")),
 ]),
 S(1, "El vencimiento", [
  D("Fecha de vencimiento", "Hasta cuándo se puede comer el producto <b>sin peligro</b>."),
  P("Si ya pasó la fecha, ¡<b>no se come</b>!"),
  P("En el súper, mirá la fecha antes de comprar. Si está vencido, avisale a un adulto."),
  IMG("¿Vencido?", "Mirá siempre la fecha.", FG.tiras(["ANTES DE LA FECHA: SE PUEDE COMER", "DESPUÉS: NO SE COME"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la etiqueta. La vas a usar en la carpeta."),
  IMG("La etiqueta de la galletita", "Leé cada renglón.", FG.ficha([("Nombre:", "GALLETITAS DE AVENA"), ("Ingredientes:", "harina, avena"), ("Vence:", "15/01")], titulo="Etiqueta")),
 ]),
],
"ejemplo_completo": {"titulo": "Leer la etiqueta", "planteo": "¿Qué miro en el yogur?", "pasos": ["El nombre.", "Los ingredientes.", "La fecha de vencimiento."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Lo que tiene adentro un alimento son sus…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "Buscá la fecha de vencimiento de un producto. Copiala."},
"tip": {"titulo": "Mirá la fecha", "texto": "Antes de comer, mirá el vencimiento."},
"ojo": ["Un producto vencido puede hacer mal.", "La etiqueta dice qué tiene adentro."],
"resumen": [{"titulo": "Etiqueta", "texto": "Información del producto."}, {"titulo": "Ingredientes", "texto": "Lo que tiene."}, {"titulo": "Vencimiento", "texto": "Hasta cuándo se come."}],
"glosario": [{"palabra": "Etiqueta", "significado": "Papel con datos del producto."}, {"palabra": "Ingrediente", "significado": "Lo que tiene un alimento."}],
"carpeta": ["En la etiqueta, ¿cómo se llama el producto?", "¿Qué ingrediente tiene además de harina?", "Lola dice que un producto vencido se puede comer igual. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("GALLETITAS DE AVENA") + low("GALLETITAS") + low("LAS GALLETITAS DE AVENA"), low("AVENA") + low("LA AVENA"), NO],
"soluciones": {"incompleto": "INGREDIENTES.", "solo": "La fecha que copiaste.", "carpeta": ["Galletitas de avena.", "Avena.", "No: puede hacer mal."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer los derechos de los que compran.",
"vas_a_ver": ["Qué es un consumidor", "Sus derechos", "Reclamar"],
"secciones": [
 S(1, "El consumidor", [
  D("Consumidor", "La persona que <b>compra</b> y usa un producto."),
  P("Los consumidores tienen <b>derechos</b>: cosas que se tienen que respetar."),
  IMG("Derechos del consumidor", "Al comprar.", FG.tiras(["SABER EL PRECIO", "PRODUCTOS SANOS", "INFORMACIÓN CLARA", "CAMBIAR LO QUE VINO MAL"], numeros=False)),
 ]),
 S(1, "Reclamar", [
  P("Si un producto vino <b>roto</b> o <b>vencido</b>, podemos <b>reclamar</b>."),
  P("Lo decimos con respeto, y lo tienen que cambiar."),
  P("También tenemos derecho a saber el <b>precio</b> antes de comprar. Los precios tienen que estar a la vista."),
  IMG("Para reclamar", "Con respeto.", FG.nombres(["TICKET", "PRODUCTO", "RESPETO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Se puede reclamar?", "Pensá en cada una.", FG.tiras(["1. EL JUGUETE VINO ROTO", "2. ME GUSTÓ MUCHO EL JUGUETE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El reclamo", "planteo": "Compré un yogur vencido.", "pasos": ["Vuelvo al almacén con el ticket.", "Explico con respeto.", "Me lo cambian."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Quien compra es el…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Qué dirías para reclamar con respeto?"},
"tip": {"titulo": "Guardá el ticket", "texto": "El ticket muestra que lo compraste ahí."},
"ojo": ["Reclamar es un derecho.", "Siempre con respeto, sin gritar."],
"resumen": [{"titulo": "Consumidor", "texto": "Quien compra."}, {"titulo": "Derechos", "texto": "Precio, info, productos sanos."}, {"titulo": "Reclamar", "texto": "Con respeto."}],
"glosario": [{"palabra": "Derecho", "significado": "Algo que nos tienen que respetar."}, {"palabra": "Reclamar", "significado": "Pedir que arreglen algo."}],
"carpeta": ["¿Se puede reclamar en la tarjeta 1?", "¿Y en la tarjeta 2?", "Lola dice que para reclamar hay que gritar. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("SÍ") + low("si") + low("SE PUEDE"), NO, NO],
"soluciones": {"incompleto": "CONSUMIDOR.", "solo": "Lo que dirías.", "carpeta": ["Sí.", "No.", "No: con respeto."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver cómo cambió el trabajo.",
"vas_a_ver": ["Antes", "Ahora", "Los chicos no trabajan"],
"secciones": [
 S(1, "Antes y ahora", [
  P("Hace mucho tiempo, muchas personas trabajaban <b>todo el día</b>, sin descanso."),
  P("Hoy hay <b>leyes</b>: horario, descanso y vacaciones."),
  P("Los trabajadores se juntaron para pedir estos derechos. Con el tiempo, se hicieron leyes. Hoy todos los tienen que respetar."),
  IMG("El trabajo cambió", "Antes y ahora.", FG.tiras(["ANTES: SIN DESCANSO", "AHORA: HORARIO Y DESCANSO"], numeros=False, cols=1)),
 ]),
 S(1, "Los chicos", [
  P("Los chicos <b>no trabajan</b>: tienen derecho a estudiar y jugar."),
  IMG("Derechos de los trabajadores", "Hoy los cuidan.", FG.nombres(["HORARIO", "DESCANSO", "VACACIONES"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Antes o ahora?", "Pensá en cada una.", FG.tiras(["1. TRABAJAR TODO EL DÍA SIN PARAR", "2. TENER VACACIONES"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Un día de trabajo hoy", "planteo": "¿Cómo trabaja la operaria?", "pasos": ["Tiene un horario.", "Para a descansar.", "Tiene vacaciones."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los días libres para descansar se llaman…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Entrevista", "planteo": "Preguntale a un adulto: ¿cuándo descansás en tu trabajo?"},
"tip": {"titulo": "Leyes", "texto": "Las leyes cuidan a los trabajadores."},
"ojo": ["Los chicos no deben trabajar.", "Descansar también es un derecho."],
"resumen": [{"titulo": "Antes", "texto": "Sin descanso."}, {"titulo": "Ahora", "texto": "Horario y vacaciones."}, {"titulo": "Chicos", "texto": "Estudian y juegan."}],
"glosario": [{"palabra": "Ley", "significado": "Norma que hace el gobierno para todos."}, {"palabra": "Vacaciones", "significado": "Días para descansar."}],
"carpeta": ["¿La tarjeta 1 es de antes o de ahora?", "¿Y la tarjeta 2?", "Lola dice que los chicos tienen que trabajar. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ANTES") + low("DE ANTES"), low("AHORA") + low("DE AHORA") + low("HOY"), NO],
"soluciones": {"incompleto": "VACACIONES.", "solo": "Lo que te contaron.", "carpeta": ["De antes.", "De ahora.", "No: estudian y juegan."]},
}

ACT = {
"1": [UNI("UNÍ CADA TRABAJO CON SU PROTECCIÓN.", [("ALBAÑIL", "CASCO"), ("BOMBERA", "TRAJE ESPECIAL"), ("COCINERO", "GORRO")], "CADA UNO SE CUIDA.", n="analizar"),
      TF("EN LA OBRA, PEDRO SE PONE CASCO: CUMPLE UNA NORMA.", "VERDADERO", "LA NORMA LO CUIDA.", n="aplicar")],
"2": [MC("¿QUÉ DICE LA FECHA DE VENCIMIENTO?", ["HASTA CUÁNDO SE COME", "CUÁNTO CUESTA"], "HASTA CUÁNDO SE COME", "MIRALA SIEMPRE.", n="recordar"),
      TF("UN PRODUCTO VENCIDO SE PUEDE COMER.", "FALSO", "PUEDE HACER MAL.", n="error")],
"3": [MC("ANA COMPRA UN JUGO EN EL KIOSCO. ¿QUÉ ES ANA?", ["CONSUMIDORA", "FABRICANTE"], "CONSUMIDORA", "COMPRA Y USA EL PRODUCTO.", n="aplicar"),
      ORD("ORDENÁ: CÓMO RECLAMO.", ["ME LO CAMBIAN", "VUELVO CON EL TICKET", "EXPLICO CON RESPETO"], ["VUELVO CON EL TICKET", "EXPLICO CON RESPETO", "ME LO CAMBIAN"], "PRIMERO VUELVO.", n="analizar")],
"4": [UNI("UNÍ: ¿ANTES O AHORA?", [("SIN DESCANSO", "ANTES"), ("CON VACACIONES", "AHORA")], "EL TRABAJO CAMBIÓ.", n="analizar"),
      TF("LOS CHICOS TIENEN DERECHO A JUGAR.", "VERDADERO", "Y A ESTUDIAR.", n="recordar")],
"5": [MC("RELÁMPAGO. EL ALBAÑIL USA…", ["CASCO", "MALLA"], "CASCO", "PARA CUIDAR LA CABEZA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ANTES DE COMER, MIRO…", ["EL VENCIMIENTO", "EL COLOR"], "EL VENCIMIENTO", "PARA COMER SANO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. RECLAMO CON…", ["RESPETO", "GRITOS"], "RESPETO", "SIEMPRE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LOS CHICOS…", ["ESTUDIAN Y JUEGAN", "TRABAJAN"], "ESTUDIAN Y JUEGAN", "ES SU DERECHO.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UNA NORMA?", ["UNA REGLA", "UN JUEGO"], "UNA REGLA", "QUE TODOS CUMPLEN.", n="recordar")],
 [1, SA("¿QUÉ SE PONE EL ALBAÑIL EN LA CABEZA?", low("CASCO") + low("UN CASCO") + low("EL CASCO"), "UN CASCO.", n="aplicar")],
 [1, TF("LAS NORMAS DE SEGURIDAD NO SIRVEN.", "FALSO", "CUIDAN A LAS PERSONAS.", n="error")],
 [2, UNI("UNÍ CADA PARTE DE LA ETIQUETA.", [("INGREDIENTES", "LO QUE TIENE"), ("VENCIMIENTO", "HASTA CUÁNDO SE COME")], "LEÉ LA ETIQUETA.", n="analizar")],
 [2, SA("¿QUÉ FECHA HAY QUE MIRAR ANTES DE COMER?", low("VENCIMIENTO") + low("LA DE VENCIMIENTO") + low("LA FECHA DE VENCIMIENTO") + low("EL VENCIMIENTO"), "LA DE VENCIMIENTO.", n="aplicar")],
 [2, MC("SI LA FECHA YA PASÓ, EL PRODUCTO…", ["NO SE COME", "SE COME IGUAL"], "NO SE COME", "ESTÁ VENCIDO.", n="aplicar")],
 [3, MC("SI EL JUGUETE VINO ROTO…", ["PUEDO RECLAMAR", "ME LO QUEDO ASÍ"], "PUEDO RECLAMAR", "ES MI DERECHO.", n="aplicar")],
 [3, SA("¿QUÉ PAPEL MUESTRA QUE LO COMPRASTE AHÍ?", low("TICKET") + low("EL TICKET") + low("LA FACTURA") + low("FACTURA"), "EL TICKET.", n="recordar")],
 [3, TF("MATEO DICE QUE PARA RECLAMAR HAY QUE GRITAR.", "FALSO", "SE RECLAMA CON RESPETO.", n="error")],
 [4, MC("¿QUÉ TIENEN HOY LOS TRABAJADORES?", ["HORARIO Y DESCANSO", "NADA"], "HORARIO Y DESCANSO", "LO DICEN LAS LEYES.", n="recordar")],
 [4, SA("¿QUÉ DÍAS SON PARA DESCANSAR DEL TRABAJO?", low("VACACIONES") + low("LAS VACACIONES"), "LAS VACACIONES.", n="aplicar")],
 [4, TF("JULIA DICE QUE LOS CHICOS TIENEN QUE TRABAJAR.", "FALSO", "ESTUDIAN Y JUEGAN.", n="error")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: normas que nos protegen", "examen_titulo": "Nivel jefe: normas que nos protegen",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
