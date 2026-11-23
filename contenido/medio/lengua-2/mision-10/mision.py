# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 10 · Adjetivos. Genera mision-10.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (hoy describe a los personajes y lugares que ya conoce).
Niveles: 1 palabras que dicen cómo es · 2 adjetivos para personajes · 3 adjetivos para lugares · 4 escribir descripciones."""
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
"objetivo": "Vas a conocer las palabras que dicen cómo es algo.",
"vas_a_ver": ["Qué es un adjetivo", "Tamaño, color y forma", "Adjetivo y sustantivo juntos"],
"secciones": [
 S(1, "¿Cómo es?", [
  P("Sofi mira el pato de la laguna."),
  P("Escribe: EL PATO <b>BLANCO</b>."),
  D("Adjetivo", "Palabra que dice <b>cómo es</b> algo."),
  IMG("El pato blanco", "BLANCO dice cómo es el pato.", FG.objetos([("pato", "PATO BLANCO")])),
 ]),
 S(1, "Muchos adjetivos", [
  P("Dicen el <b>tamaño</b>: GRANDE, CHICO."),
  P("Dicen el <b>color</b>: ROJO, VERDE."),
  P("Dicen <b>cómo se siente</b>: SUAVE, DURO."),
  IMG("Con adjetivo", "El sustantivo y su adjetivo.", FG.objetos([("rana", "RANA VERDE"), ("flor", "FLOR ROSADA"), ("yaguarete", "YAGUARETÉ GRANDE")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Cuál dice cómo es?", "Algunas nombran y otras dicen cómo es.", FG.nombres(["GATO", "PELUDO", "MESA", "REDONDA"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar", "planteo": "LA RANA VERDE.", "pasos": ["RANA nombra un animal.", "VERDE dice cómo es.", "VERDE es un adjetivo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Elegí un adjetivo.", "pasos": ["EL SOL ___ .", "LA PELOTA ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuaderno", "planteo": "Mirá tu mochila. Escribí dos adjetivos."},
"tip": {"titulo": "Preguntá ¿cómo es?", "texto": "La respuesta es un adjetivo."},
"ojo": ["GATO nombra: es sustantivo.", "PELUDO dice cómo es: es adjetivo."],
"resumen": [{"titulo": "Adjetivo", "texto": "Dice cómo es."}, {"titulo": "Dice", "texto": "Tamaño, color, forma."}, {"titulo": "Va junto", "texto": "Al sustantivo."}],
"glosario": [{"palabra": "Adjetivo", "significado": "Palabra que dice cómo es algo."}, {"palabra": "Describir", "significado": "Contar cómo es algo."}],
"carpeta": ["¿Qué palabra del dibujo dice cómo es el gato?", "¿Qué palabra del dibujo dice cómo es la mesa?", "Tomi dice que MESA es un adjetivo. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PELUDO"), low("REDONDA"), NO],
"soluciones": {"incompleto": "Por ejemplo: AMARILLO. GRANDE.", "solo": "Por ejemplo: AZUL, PESADA.", "carpeta": ["PELUDO.", "REDONDA.", "No: MESA nombra una cosa."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a usar adjetivos para describir personajes.",
"vas_a_ver": ["Cómo es por fuera", "Cómo es por dentro", "Personajes de cuentos"],
"secciones": [
 S(1, "Por fuera", [
  P("Rinrín es <b>elegante</b>. El lobo es <b>grande</b>."),
  P("Estos adjetivos dicen cómo se ven."),
  IMG("Rinrín Renacuajo", "ELEGANTE y PASEADOR.", FG.objetos([("renacuajo", "RINRÍN ELEGANTE")])),
 ]),
 S(1, "Por dentro", [
  P("Cenicienta es <b>buena</b>. La madrastra es <b>mala</b>."),
  P("Estos adjetivos dicen cómo son por dentro."),
  IMG("Personajes", "Cómo son por dentro.", FG.tiras(["CENICIENTA: BUENA", "MADRASTRA: MALA", "RINRÍN: DESOBEDIENTE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Leé las pistas. Las vas a usar en la carpeta."),
  IMG("¿Cómo es?", "Buscá el adjetivo.", FG.tiras(["EL CHANCHITO TRABAJADOR HIZO UNA CASA DE LADRILLOS.", "EL LOBO FEROZ SOPLÓ Y SOPLÓ."], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Describir", "planteo": "¿Cómo es Cenicienta?", "pasos": ["Ayuda a todos.", "Es buena.", "BUENA es un adjetivo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Elegí un adjetivo.", "pasos": ["EL LOBO ES ___ .", "EL HADA ES ___ ."]},
"ejemplo_solo": {"titulo": "Tu personaje", "planteo": "Describí a tu personaje preferido con dos adjetivos."},
"tip": {"titulo": "Por fuera y por dentro", "texto": "Usá adjetivos de los dos tipos."},
"ojo": ["El adjetivo dice cómo es, no lo que hace.", "SOPLÓ dice lo que hace: no es adjetivo."],
"resumen": [{"titulo": "Por fuera", "texto": "Grande, elegante."}, {"titulo": "Por dentro", "texto": "Buena, mala."}, {"titulo": "Personajes", "texto": "Se describen con adjetivos."}],
"glosario": [{"palabra": "Feroz", "significado": "Que da mucho miedo."}, {"palabra": "Desobediente", "significado": "Que no hace caso."}],
"carpeta": ["En la oración 1, ¿cómo es el chanchito?", "En la oración 2, ¿cómo es el lobo?", "Tomi dice que SOPLÓ es un adjetivo. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("TRABAJADOR"), low("FEROZ"), NO],
"soluciones": {"incompleto": "Por ejemplo: FEROZ. BUENA.", "solo": "Dos adjetivos de tu personaje.", "carpeta": ["TRABAJADOR.", "FEROZ.", "No: dice lo que hace."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a usar adjetivos para describir lugares.",
"vas_a_ver": ["Cómo es un lugar", "Ver, oír y sentir", "Lugares de los cuentos"],
"secciones": [
 S(1, "Un lugar", [
  P("El yaguareté vive en la selva."),
  P("La selva es <b>verde</b>, <b>húmeda</b> y <b>enorme</b>."),
  IMG("La selva", "Verde, húmeda y enorme.", FG.objetos([("yaguarete", "SELVA VERDE"), ("flor", "SELVA HÚMEDA")])),
 ]),
 S(1, "Con los sentidos", [
  P("¿Cómo se <b>ve</b>? ¿Cómo <b>suena</b>? ¿Cómo se <b>siente</b>?"),
  P("El castillo es <b>alto</b> y <b>brillante</b>."),
  IMG("El castillo de Cenicienta", "ALTO y BRILLANTE.", FG.objetos([("castillo", "CASTILLO ALTO")])),
 ]),
 S(2, "Para practicar", [
  P("Leé las oraciones. Las vas a usar en la carpeta."),
  IMG("Lugares", "Buscá los adjetivos.", FG.tiras(["LA PLAZA ES GRANDE Y RUIDOSA.", "LA LAGUNA ES FRÍA."], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Describir", "planteo": "¿Cómo es la plaza?", "pasos": ["Tiene muchos juegos.", "Hay chicos gritando.", "Es grande y ruidosa."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Describí la escuela.", "pasos": ["LA ESCUELA ES ___ ."]},
"ejemplo_solo": {"titulo": "Tu lugar", "planteo": "Describí tu cuarto con tres adjetivos."},
"tip": {"titulo": "Usá los sentidos", "texto": "Mirá, escuchá y tocá."},
"ojo": ["PLAZA es el lugar: es sustantivo.", "GRANDE dice cómo es: es adjetivo."],
"resumen": [{"titulo": "Lugares", "texto": "Se describen con adjetivos."}, {"titulo": "Sentidos", "texto": "Ver, oír, sentir."}, {"titulo": "Ejemplos", "texto": "Selva verde, castillo alto."}],
"glosario": [{"palabra": "Húmeda", "significado": "Un poco mojada."}, {"palabra": "Ruidosa", "significado": "Con mucho ruido."}],
"carpeta": ["En la oración 1, ¿qué adjetivos tiene la plaza?", "En la oración 2, ¿cómo es la laguna?", "Tomi dice que LAGUNA es un adjetivo. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("GRANDE Y RUIDOSA") + low("GRANDE, RUIDOSA") + low("RUIDOSA Y GRANDE"), low("FRÍA") + low("fria") + low("ES FRÍA"), NO],
"soluciones": {"incompleto": "Por ejemplo: LINDA.", "solo": "Tres adjetivos de tu cuarto.", "carpeta": ["GRANDE Y RUIDOSA.", "FRÍA.", "No: LAGUNA es un lugar."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir una descripción con adjetivos.",
"vas_a_ver": ["Elegir qué describir", "Sumar adjetivos", "Escribir oraciones"],
"secciones": [
 S(1, "Sumar adjetivos", [
  P("Sofi empieza con: EL PERRO."),
  P("Suma un adjetivo: EL PERRO <b>GRANDE</b>."),
  P("Suma otro: EL PERRO GRANDE Y <b>PELUDO</b>."),
  IMG("Paso a paso", "Cada vez sabemos más.", FG.tiras(["EL PERRO", "EL PERRO GRANDE", "EL PERRO GRANDE Y PELUDO"], numeros=True, cols=1)),
 ]),
 S(1, "La descripción de Sofi", [
  P("Sofi describe a su gato Michi."),
  IMG("Michi", "Una descripción con adjetivos.", FG.tiras(["MICHI ES CHIQUITO Y NEGRO.", "TIENE OJOS AMARILLOS.", "ES MIMOSO Y JUGUETÓN."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los dibujos. Los vas a usar en la carpeta."),
  IMG("Para describir", "Pensá cómo es cada uno.", FG.dibujo_palabra([("manzana", "MANZANA"), ("globo", "GLOBO"), ("estrella", "ESTRELLA")])),
 ]),
],
"ejemplo_completo": {"titulo": "Describir", "planteo": "LA MANZANA.", "pasos": ["¿De qué color es? Roja.", "¿Cómo es? Redonda.", "LA MANZANA ROJA Y REDONDA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Sumá adjetivos.", "pasos": ["EL GLOBO ___ Y ___ ."]},
"ejemplo_solo": {"titulo": "Tu descripción", "planteo": "Describí a tu mascota o a un animal con tres oraciones."},
"tip": {"titulo": "No repitas", "texto": "Usá adjetivos distintos en cada oración."},
"ojo": ["Cada oración con mayúscula y punto.", "Más adjetivos, más clara la descripción."],
"resumen": [{"titulo": "Elegir", "texto": "Qué describir."}, {"titulo": "Sumar", "texto": "Adjetivos."}, {"titulo": "Escribir", "texto": "Oraciones claras."}],
"glosario": [{"palabra": "Descripción", "significado": "Texto que cuenta cómo es algo."}, {"palabra": "Mimoso", "significado": "Que le gustan los mimos."}],
"carpeta": ["¿De qué color es la manzana del dibujo?", "¿Qué forma tiene la estrella del dibujo: redonda o con puntas?", "Tomi escribió: MICHI ES LINDO, LINDO Y LINDO. ¿Qué tiene que cambiar?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ROJA") + low("ES ROJA"), low("CON PUNTAS") + low("PUNTAS") + low("TIENE PUNTAS"), low("NO REPETIR") + low("no repetir") + low("USAR OTROS ADJETIVOS") + low("OTROS ADJETIVOS") + low("ADJETIVOS DISTINTOS") + low("no repetir lindo")],
"soluciones": {"incompleto": "Por ejemplo: ROJO Y REDONDO.", "solo": "Tres oraciones con adjetivos.", "carpeta": ["ROJA.", "CON PUNTAS.", "Usar adjetivos distintos."]},
}

ACT = {
"1": [MC("¿CUÁL ES UN ADJETIVO?", ["GRANDE", "PERRO", "CORRE"], "GRANDE", "DICE CÓMO ES.", n="aplicar"),
      TF("EN LA RANA VERDE, VERDE ES UN ADJETIVO.", "VERDADERO", "DICE CÓMO ES LA RANA.", n="aplicar")],
"2": [UNI("UNÍ CADA PERSONAJE CON SU ADJETIVO.", [("CENICIENTA", "BUENA"), ("LOBO", "FEROZ"), ("RINRÍN", "ELEGANTE")], "CADA UNO TIENE SU FORMA DE SER.", n="analizar"),
      MC("EL LOBO FEROZ SOPLÓ. ¿CUÁL ES EL ADJETIVO?", ["FEROZ", "LOBO", "SOPLÓ"], "FEROZ", "DICE CÓMO ES EL LOBO.", n="aplicar")],
"3": [MC("¿CÓMO ES LA SELVA?", ["VERDE Y HÚMEDA", "SECA Y VACÍA"], "VERDE Y HÚMEDA", "TIENE MUCHAS PLANTAS.", n="recordar"),
      SA("LA LAGUNA ES FRÍA. ESCRIBÍ EL ADJETIVO.", low("FRÍA") + low("fria"), "FRÍA.", n="aplicar")],
"4": [MC("¿CUÁL DESCRIBE MEJOR?", ["EL PERRO GRANDE Y PELUDO", "EL PERRO"], "EL PERRO GRANDE Y PELUDO", "TIENE ADJETIVOS.", n="analizar"),
      SA("COMPLETÁ CON UN COLOR: LA MANZANA ES ___", low("ROJA") + low("VERDE") + low("AMARILLA"), "POR EJEMPLO: ROJA.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿CUÁL ES ADJETIVO?", ["AZUL", "MESA"], "AZUL", "DICE CÓMO ES.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ES SUSTANTIVO?", ["CASA", "ALTA"], "CASA", "NOMBRA UN LUGAR.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL LOBO ES…", ["FEROZ", "CHIQUITO Y BUENO"], "FEROZ", "DA MIEDO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL ADJETIVO DICE…", ["CÓMO ES", "QUÉ HACE"], "CÓMO ES", "CÓMO ES ALGO.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UN ADJETIVO?", ["UNA PALABRA QUE DICE CÓMO ES", "UNA PALABRA QUE NOMBRA", "UN DIBUJO"], "UNA PALABRA QUE DICE CÓMO ES", "DICE CÓMO ES ALGO.", n="recordar")],
 [1, TF("GATO ES UN ADJETIVO.", "FALSO", "GATO NOMBRA: ES SUSTANTIVO.", n="error")],
 [1, SA("EL PATO BLANCO. ESCRIBÍ EL ADJETIVO.", low("BLANCO"), "BLANCO.", n="aplicar")],
 [2, MC("¿QUÉ ADJETIVO VA CON CENICIENTA?", ["BUENA", "FEROZ", "MALA"], "BUENA", "AYUDA A TODOS.", n="aplicar")],
 [2, UNI("UNÍ CADA PERSONAJE CON SU ADJETIVO.", [("MADRASTRA", "MALA"), ("CHANCHITO", "TRABAJADOR"), ("LOBO", "FEROZ")], "CADA UNO ES DISTINTO.", n="analizar")],
 [2, TF("EN EL LOBO SOPLÓ, SOPLÓ ES UN ADJETIVO.", "FALSO", "DICE LO QUE HACE.", n="error")],
 [3, MC("LA PLAZA ES GRANDE Y RUIDOSA. ¿CUÁNTOS ADJETIVOS HAY?", ["DOS", "UNO", "TRES"], "DOS", "GRANDE Y RUIDOSA.", n="analizar")],
 [3, SA("EL CASTILLO ES ALTO. ESCRIBÍ EL ADJETIVO.", low("ALTO"), "ALTO.", n="aplicar")],
 [3, TF("PARA DESCRIBIR UN LUGAR SIRVEN LOS SENTIDOS.", "VERDADERO", "VER, OÍR Y SENTIR.", n="recordar")],
 [4, MC("¿CUÁL ES UNA DESCRIPCIÓN?", ["MICHI ES CHIQUITO Y NEGRO", "MICHI CORRE", "MICHI"], "MICHI ES CHIQUITO Y NEGRO", "DICE CÓMO ES.", n="analizar")],
 [4, SA("COMPLETÁ: EL GLOBO ROJO Y ___", low("REDONDO") + low("GRANDE") + low("CHICO") + low("LINDO") + low("BRILLANTE") + low("LIVIANO"), "POR EJEMPLO: REDONDO.", n="aplicar")],
 [4, TF("TOMI ESCRIBIÓ MICHI ES LINDO, LINDO Y LINDO. ESTÁ BIEN DESCRIPTO.", "FALSO", "HAY QUE USAR ADJETIVOS DISTINTOS.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 10, "estilo": "primeros",
     "practica": "Práctica general: adjetivos", "examen_titulo": "Nivel jefe: adjetivos",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
