# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 13 · Cartas y mensajes para otros. Genera mision-13.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (hoy viaja con una carta para Tomi).
Niveles: 1 partes de una carta · 2 escribir una carta a un compañero · 3 un correo electrónico · 4 responder una carta."""
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
CARTA = [("Lugar y fecha", ["Córdoba, 23 de noviembre"]), ("Saludo", ["Querido Tomi:"]), ("Cuerpo", ["Te cuento que fui a la plaza.", "Vi un hornero en su nido."]), ("Despedida", ["Un abrazo,"]), ("Firma", ["Sofi"])]

N1 = {**ESTILO,
"objetivo": "Vas a conocer las partes de una carta.",
"vas_a_ver": ["Para qué sirve una carta", "Las cinco partes", "Dónde va cada una"],
"secciones": [
 S(1, "Una carta", [
  P("Sofi le escribe una <b>carta</b> a Tomi."),
  D("Carta", "Mensaje escrito para <b>otra persona</b>."),
  IMG("La carta de Sofi", "Así se ve una carta.", FG.carta(CARTA)),
 ]),
 S(1, "Las partes", [
  P("<b>Lugar y fecha</b> arriba. Después el <b>saludo</b>."),
  P("En el medio, el <b>cuerpo</b>: lo que contamos."),
  P("Al final, la <b>despedida</b> y la <b>firma</b>."),
  IMG("Las cinco partes", "Cada parte en su lugar.", FG.carta(CARTA, marcar=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la carta de las partes. La vas a usar en la carpeta."),
  IMG("Otra carta", "Buscá cada parte.", FG.carta([("Lugar y fecha", ["Rosario, 5 de mayo"]), ("Saludo", ["Hola, abuela:"]), ("Cuerpo", ["Te extraño mucho."]), ("Despedida", ["Besos,"]), ("Firma", ["Tomi"])])),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar el saludo", "planteo": "¿Cuál es el saludo de la carta de Sofi?", "pasos": ["Está después de la fecha.", "Dice: Querido Tomi.", "Ese es el saludo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La carta de Sofi.", "pasos": ["La firma es ___ .", "La despedida es ___ ."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá en tu casa una carta vieja y mirá sus partes."},
"tip": {"titulo": "De arriba a abajo", "texto": "Fecha, saludo, cuerpo, despedida y firma."},
"ojo": ["La firma va al final.", "El saludo termina con dos puntos."],
"resumen": [{"titulo": "Arriba", "texto": "Lugar y fecha, saludo."}, {"titulo": "Medio", "texto": "El cuerpo."}, {"titulo": "Final", "texto": "Despedida y firma."}],
"glosario": [{"palabra": "Carta", "significado": "Mensaje escrito para otra persona."}, {"palabra": "Firma", "significado": "El nombre de quien escribe."}],
"carpeta": ["En la carta de Tomi, ¿cuál es el saludo?", "¿Quién firma esa carta?", "Tomi dice que la firma va arriba. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("HOLA, ABUELA") + low("HOLA ABUELA") + low("HOLA, ABUELA:"), low("TOMI"), NO],
"soluciones": {"incompleto": "SOFI. UN ABRAZO.", "solo": "Las partes que encuentres.", "carpeta": ["Hola, abuela.", "Tomi.", "No: va al final."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a escribir una carta a un compañero.",
"vas_a_ver": ["Pensar qué contar", "Escribir cada parte", "Revisar"],
"secciones": [
 S(1, "Qué contar", [
  P("Primero pensamos: ¿a quién le escribo? ¿Qué le cuento?"),
  P("Sofi le cuenta a Tomi que fue a la plaza."),
  IMG("Pensar antes", "A quién y qué.", FG.ficha([("¿A quién?", "a Tomi"), ("¿Qué le cuento?", "fui a la plaza")], titulo="Antes de escribir")),
 ]),
 S(1, "Escribir", [
  P("Escribimos cada parte <b>en su lugar</b>."),
  P("El cuerpo cuenta algo en <b>oraciones cortas</b>."),
  IMG("La carta lista", "Con sus cinco partes.", FG.carta(CARTA, marcar=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la carta. La vas a usar en la carpeta."),
  IMG("Carta incompleta", "Le faltan partes.", FG.carta([("Saludo", ["Querida Sofi:"]), ("Cuerpo", ["Mañana juego al fútbol."]), ("Despedida", ["Chau,"])])),
 ]),
],
"ejemplo_completo": {"titulo": "Saludo", "planteo": "Le escribo a mi amiga Lu.", "pasos": ["Pienso un saludo.", "Querida Lu:", "Con dos puntos al final."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Le escribo a Tomi.", "pasos": ["___ Tomi:", "Un ___ ,"]},
"ejemplo_solo": {"titulo": "Tu carta", "planteo": "Escribí una carta corta a un compañero o compañera."},
"tip": {"titulo": "Pensá antes", "texto": "¿A quién le escribo? ¿Qué le cuento?"},
"ojo": ["No te olvides de firmar.", "Contá algo en oraciones cortas."],
"resumen": [{"titulo": "Pensar", "texto": "A quién y qué contar."}, {"titulo": "Escribir", "texto": "Cada parte en su lugar."}, {"titulo": "Revisar", "texto": "Que estén las cinco."}],
"glosario": [{"palabra": "Compañero", "significado": "Alguien de tu grado."}, {"palabra": "Contar", "significado": "Decir algo que pasó."}],
"carpeta": ["En la carta del dibujo, ¿qué cuenta el cuerpo?", "¿Qué parte falta al final de esa carta?", "Tomi escribió una carta sin lugar y fecha. ¿Está completa?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [low("MAÑANA JUEGO AL FÚTBOL") + low("manana juego al futbol") + low("QUE JUEGA AL FÚTBOL") + low("que juega al futbol"), low("LA FIRMA") + low("FIRMA"), NO],
"soluciones": {"incompleto": "QUERIDO. ABRAZO.", "solo": "Tu carta con las cinco partes.", "carpeta": ["Mañana juego al fútbol.", "La firma.", "No: le falta el lugar y la fecha."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer el correo electrónico.",
"vas_a_ver": ["Una carta por computadora", "Para y asunto", "Enviar"],
"secciones": [
 S(1, "El correo electrónico", [
  D("Correo electrónico", "Carta que se manda por <b>computadora</b> o celular."),
  P("Llega en un ratito, sin estampilla."),
  IMG("Un correo", "Así se ve en la pantalla.", FG.correo("tomi@escuela.com", "Mi ficha", ["Hola, Tomi:", "Te mando mi ficha del yaguareté.", "Saludos, Sofi"])),
 ]),
 S(1, "Sus partes", [
  P("<b>PARA</b>: la dirección de quien lo recibe."),
  P("<b>ASUNTO</b>: de qué trata, en pocas palabras."),
  P("Después, el <b>mensaje</b> y el botón <b>ENVIAR</b>."),
  IMG("Las partes", "Para, asunto y mensaje.", FG.tiras(["PARA: TOMI@ESCUELA.COM", "ASUNTO: MI FICHA", "MENSAJE: HOLA, TOMI…"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el correo. Lo vas a usar en la carpeta."),
  IMG("Correo de la maestra", "Leelo con atención.", FG.correo("sofi@escuela.com", "Paseo al zoo", ["Hola, Sofi:", "El viernes vamos al zoo.", "Saludos, la seño Ana"])),
 ]),
],
"ejemplo_completo": {"titulo": "El asunto", "planteo": "Sofi manda su ficha.", "pasos": ["¿De qué trata?", "De su ficha.", "Asunto: MI FICHA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Correo para Tomi.", "pasos": ["PARA: ___ ."]},
"ejemplo_solo": {"titulo": "Con un adulto", "planteo": "Con un adulto, mirá cómo se escribe un correo."},
"tip": {"titulo": "Asunto corto", "texto": "Pocas palabras que digan de qué trata."},
"ojo": ["Revisá la dirección antes de enviar.", "Usá el correo siempre con un adulto."],
"resumen": [{"titulo": "Correo", "texto": "Carta por computadora."}, {"titulo": "Para", "texto": "A quién va."}, {"titulo": "Asunto", "texto": "De qué trata."}],
"glosario": [{"palabra": "Asunto", "significado": "De qué trata el mensaje."}, {"palabra": "Enviar", "significado": "Mandar."}],
"carpeta": ["En el correo de la maestra, ¿cuál es el asunto?", "¿A quién le escribe la maestra?", "Tomi mandó un correo sin asunto. ¿Está completo?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PASEO AL ZOO"), low("A SOFI") + low("SOFI"), NO],
"soluciones": {"incompleto": "TOMI@ESCUELA.COM.", "solo": "Un correo visto con un adulto.", "carpeta": ["Paseo al zoo.", "A Sofi.", "No: le falta el asunto."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a responder una carta.",
"vas_a_ver": ["Leer la carta", "Contestar lo que pregunta", "Escribir la respuesta"],
"secciones": [
 S(1, "Tomi responde", [
  P("Tomi recibió la carta de Sofi. Ahora le <b>responde</b>."),
  P("Primero lee bien: ¿qué le cuenta? ¿Qué le pregunta?"),
  IMG("La carta de Sofi", "Con una pregunta al final.", FG.carta([("Saludo", ["Querido Tomi:"]), ("Cuerpo", ["Vi un hornero en la plaza.", "¿Vos viste uno alguna vez?"]), ("Firma", ["Sofi"])])),
 ]),
 S(1, "La respuesta", [
  P("Tomi <b>contesta</b> la pregunta y cuenta algo suyo."),
  IMG("La carta de Tomi", "Responde y cuenta.", FG.carta([("Saludo", ["Querida Sofi:"]), ("Cuerpo", ["¡Sí! Vi uno en el campo.", "Hacía su nido de barro."]), ("Despedida", ["Un abrazo,"]), ("Firma", ["Tomi"])])),
 ]),
 S(2, "Para practicar", [
  P("Leé la carta. La vas a usar en la carpeta."),
  IMG("Carta de la abuela", "Tiene una pregunta.", FG.carta([("Saludo", ["Querida Sofi:"]), ("Cuerpo", ["Te mando un beso grande.", "¿Qué fruta te gusta más?"]), ("Firma", ["La abuela"])])),
 ]),
],
"ejemplo_completo": {"titulo": "Responder", "planteo": "La abuela pregunta qué fruta te gusta.", "pasos": ["Leo la pregunta.", "Pienso mi respuesta.", "Escribo: me gusta la manzana."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Le respondo a la abuela.", "pasos": ["Querida ___ :", "Me gusta la ___ ."]},
"ejemplo_solo": {"titulo": "Tu respuesta", "planteo": "Escribí la respuesta a la abuela con todas las partes."},
"tip": {"titulo": "Buscá la pregunta", "texto": "Si la carta pregunta algo, contestalo."},
"ojo": ["Saludá a quien te escribió.", "Firmá con tu nombre."],
"resumen": [{"titulo": "Leer", "texto": "La carta entera."}, {"titulo": "Contestar", "texto": "La pregunta."}, {"titulo": "Escribir", "texto": "Con todas las partes."}],
"glosario": [{"palabra": "Responder", "significado": "Contestar."}, {"palabra": "Recibir", "significado": "Que te llegue algo."}],
"carpeta": ["¿Qué pregunta la abuela en su carta?", "¿A quién va el saludo de tu respuesta?", "Tomi respondió sin contestar la pregunta. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("QUÉ FRUTA TE GUSTA MÁS") + low("que fruta te gusta mas") + low("¿QUÉ FRUTA TE GUSTA MÁS?") + low("QUÉ FRUTA ME GUSTA"), low("A LA ABUELA") + low("LA ABUELA") + low("ABUELA") + low("QUERIDA ABUELA"), NO],
"soluciones": {"incompleto": "ABUELA. MANZANA (o tu fruta).", "solo": "Tu carta de respuesta.", "carpeta": ["Qué fruta te gusta más.", "A la abuela.", "No: hay que contestar la pregunta."]},
}

ACT = {
"1": [ORD("ORDENÁ LAS PARTES DE LA CARTA.", ["FIRMA", "SALUDO", "CUERPO", "LUGAR Y FECHA", "DESPEDIDA"], ["LUGAR Y FECHA", "SALUDO", "CUERPO", "DESPEDIDA", "FIRMA"], "DE ARRIBA A ABAJO.", n="analizar"),
      MC("QUERIDO TOMI: ¿QUÉ PARTE ES?", ["EL SALUDO", "LA FIRMA", "LA FECHA"], "EL SALUDO", "VA ARRIBA, DESPUÉS DE LA FECHA.", n="aplicar")],
"2": [MC("¿QUÉ PENSAMOS ANTES DE ESCRIBIR?", ["A QUIÉN Y QUÉ CONTAR", "EL COLOR DEL PAPEL"], "A QUIÉN Y QUÉ CONTAR", "ASÍ SABEMOS QUÉ ESCRIBIR.", n="recordar"),
      TF("UNA CARTA SIN FIRMA ESTÁ COMPLETA.", "FALSO", "HAY QUE FIRMAR.", n="error")],
"3": [UNI("UNÍ CADA PARTE DEL CORREO CON LO QUE DICE.", [("PARA", "A QUIÉN VA"), ("ASUNTO", "DE QUÉ TRATA"), ("ENVIAR", "MANDARLO")], "CADA PARTE TIENE SU TAREA.", n="analizar"),
      MC("¿CÓMO SE MANDA UN CORREO ELECTRÓNICO?", ["POR COMPUTADORA O CELULAR", "CON ESTAMPILLA", "CON UNA PALOMA"], "POR COMPUTADORA O CELULAR", "LLEGA EN UN RATITO.", n="recordar")],
"4": [MC("LA CARTA PREGUNTA: ¿VISTE UN HORNERO? ¿QUÉ HAGO?", ["CONTESTO LA PREGUNTA", "NO DIGO NADA"], "CONTESTO LA PREGUNTA", "SE RESPONDE LO QUE PREGUNTAN.", n="aplicar"),
      SA("LA ABUELA TE ESCRIBIÓ. COMPLETÁ EL SALUDO: QUERIDA ___", low("ABUELA"), "QUERIDA ABUELA.", n="aplicar")],
"5": [MC("RELÁMPAGO. LA FIRMA VA…", ["AL FINAL", "ARRIBA"], "AL FINAL", "CIERRA LA CARTA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL ASUNTO DICE…", ["DE QUÉ TRATA", "LA HORA"], "DE QUÉ TRATA", "EN POCAS PALABRAS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. UN ABRAZO ES…", ["DESPEDIDA", "SALUDO"], "DESPEDIDA", "VA ANTES DE LA FIRMA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL CORREO SE USA CON…", ["UN ADULTO", "NADIE"], "UN ADULTO", "SIEMPRE ACOMPAÑADOS.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ VA ARRIBA DE TODO EN LA CARTA?", ["LUGAR Y FECHA", "LA FIRMA", "LA DESPEDIDA"], "LUGAR Y FECHA", "VA ARRIBA.", n="recordar")],
 [1, ORD("ORDENÁ LAS PARTES.", ["DESPEDIDA", "SALUDO", "FIRMA"], ["SALUDO", "DESPEDIDA", "FIRMA"], "SALUDO, DESPEDIDA Y FIRMA.", n="analizar")],
 [1, TF("EL CUERPO ES LO QUE CONTAMOS EN LA CARTA.", "VERDADERO", "VA EN EL MEDIO.", n="recordar")],
 [2, MC("¿CUÁL ES UN SALUDO?", ["QUERIDA LU", "UN ABRAZO", "SOFI"], "QUERIDA LU", "VA AL PRINCIPIO.", n="aplicar")],
 [2, SA("ESCRIBÍ UNA DESPEDIDA PARA UNA CARTA.", low("UN ABRAZO") + low("BESOS") + low("CHAU") + low("SALUDOS") + low("HASTA PRONTO") + low("UN BESO") + low("ABRAZOS"), "POR EJEMPLO: UN ABRAZO.", n="aplicar")],
 [2, TF("TOMI ESCRIBIÓ SU CARTA SIN SALUDO. ESTÁ COMPLETA.", "FALSO", "LE FALTA EL SALUDO.", n="error")],
 [3, MC("EN UN CORREO, ¿DÓNDE VA LA DIRECCIÓN DE QUIEN LO RECIBE?", ["EN PARA", "EN ASUNTO", "EN EL MENSAJE"], "EN PARA", "PARA DICE A QUIÉN VA.", n="aplicar")],
 [3, SA("LA SEÑO ESCRIBE SOBRE EL PASEO AL ZOO. ¿CUÁL ES UN BUEN ASUNTO?", low("PASEO AL ZOO") + low("EL ZOO") + low("ZOO") + low("PASEO"), "PASEO AL ZOO.", n="aplicar")],
 [3, TF("ANTES DE ENVIAR HAY QUE REVISAR LA DIRECCIÓN.", "VERDADERO", "ASÍ LLEGA BIEN.", n="recordar")],
 [4, MC("PARA RESPONDER UNA CARTA, PRIMERO…", ["LA LEO ENTERA", "LA TIRO", "LA DIBUJO"], "LA LEO ENTERA", "ASÍ SÉ QUÉ CONTESTAR.", n="aplicar")],
 [4, SA("LA ABUELA PREGUNTA QUÉ FRUTA TE GUSTA. ESCRIBÍ UNA FRUTA.", low("MANZANA") + low("BANANA") + low("PERA") + low("NARANJA") + low("UVA") + low("UVAS") + low("FRUTILLA") + low("DURAZNO") + low("SANDÍA") + low("sandia") + low("MANDARINA") + low("KIWI") + low("CEREZA") + low("MELÓN") + low("melon") + low("ANANÁ") + low("anana"), "POR EJEMPLO: MANZANA.", n="aplicar")],
 [4, TF("TOMI RESPONDIÓ SIN CONTESTAR LA PREGUNTA. ESTÁ BIEN.", "FALSO", "HAY QUE CONTESTAR LO QUE PREGUNTAN.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 13, "estilo": "primeros",
     "practica": "Práctica general: cartas y mensajes", "examen_titulo": "Nivel jefe: cartas y mensajes",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-13.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
