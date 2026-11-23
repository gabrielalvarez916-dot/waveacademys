# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 6 · Sustantivos. Genera mision-6.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (hoy junta «palabras que nombran» en la plaza).
Niveles: 1 palabras que nombran · 2 sustantivos propios y comunes · 3 buscar sustantivos en un cuento · 4 clasificar sustantivos."""
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

N1 = {**ESTILO,
"objetivo": "Vas a conocer las palabras que nombran.",
"vas_a_ver": ["Qué es un sustantivo", "Nombran personas, animales y cosas", "También nombran lugares"],
"secciones": [
 S(1, "Palabras que nombran", [
  P("Sofi lleva su <b>cuaderno viajero</b> a la plaza."),
  P("Anota todo lo que ve: PERRO, NENA, PELOTA, PLAZA."),
  D("Sustantivo", "Es una palabra que <b>nombra</b> algo."),
  IMG("Lo que ve Sofi", "Cada cosa tiene su nombre.", FG.dibujo_palabra([("pelota", "PELOTA"), ("globo", "GLOBO"), ("chico", "NENE")])),
 ]),
 S(1, "¿Qué nombran?", [
  P("Nombran <b>personas</b>: MAMÁ, MAESTRA, NENE."),
  P("Nombran <b>animales</b>: PERRO, GATO, PALOMA."),
  P("Nombran <b>cosas</b>: SILLA, VASO, PELOTA."),
  P("Nombran <b>lugares</b>: PLAZA, CASA, ESCUELA."),
  IMG("Cuatro grupos", "Personas, animales, cosas y lugares.", FG.nombres(["MAMÁ", "PERRO", "SILLA", "PLAZA"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Cuáles nombran?", "Algunas nombran y otras no.", FG.nombres(["GATO", "CORRE", "ESCUELA", "LINDO"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "PERRO", "planteo": "¿PERRO es un sustantivo?", "pasos": ["PERRO nombra un animal.", "Nombra algo.", "Sí, es un sustantivo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿Qué nombra cada palabra?", "pasos": ["MAESTRA nombra una ___ .", "ESCUELA nombra un ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuaderno viajero", "planteo": "Mirá tu cuarto. Escribí tres sustantivos."},
"tip": {"titulo": "Preguntá ¿qué es?", "texto": "Si podés señalarlo, es un sustantivo."},
"ojo": ["CORRE no nombra: dice lo que se hace.", "LINDO no nombra: dice cómo es."],
"resumen": [{"titulo": "Sustantivo", "texto": "Palabra que nombra."}, {"titulo": "Nombra", "texto": "Personas, animales, cosas, lugares."}, {"titulo": "Ejemplos", "texto": "MAMÁ, PERRO, SILLA, PLAZA."}],
"glosario": [{"palabra": "Sustantivo", "significado": "Palabra que nombra."}, {"palabra": "Nombrar", "significado": "Decir cómo se llama algo."}],
"carpeta": ["¿Qué palabra del dibujo nombra un animal?", "¿Qué palabra del dibujo nombra un lugar?", "Tomi dice que CORRE es un sustantivo. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("GATO"), low("ESCUELA"), ["NO", "no", "No"]],
"soluciones": {"incompleto": "PERSONA. LUGAR.", "solo": "Por ejemplo: CAMA, MESA, LÁMPARA.", "carpeta": ["GATO.", "ESCUELA.", "No: CORRE dice lo que se hace."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a distinguir sustantivos propios y comunes.",
"vas_a_ver": ["Sustantivos comunes", "Sustantivos propios", "La mayúscula"],
"secciones": [
 S(1, "Comunes y propios", [
  P("En la plaza hay un <b>perro</b>. Se llama <b>Pancho</b>."),
  D("Común", "Nombra a <b>cualquiera</b>: perro, nena, ciudad."),
  D("Propio", "Es el nombre de <b>uno solo</b>: Pancho, Sofi, Córdoba."),
  IMG("Común y propio", "Perro es común. Pancho es propio.", FG.tiras(["PERRO → COMÚN", "PANCHO → PROPIO"], numeros=False)),
 ]),
 S(1, "La mayúscula", [
  P("Los propios se escriben con <b>mayúscula</b> al principio."),
  P("Sofi, Pancho, Tomi, Córdoba, Argentina."),
  IMG("Con mayúscula", "Nombres de personas, mascotas y lugares.", FG.lista(["Sofi", "Pancho", "Córdoba"], titulo="NOMBRES PROPIOS")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Común o propio?", "Pensá si nombra a uno solo.", FG.nombres(["GATO", "MICHI", "RÍO", "PARANÁ"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Córdoba", "planteo": "¿Córdoba es común o propio?", "pasos": ["Es el nombre de una ciudad.", "Nombra a una sola.", "Es propio: va con mayúscula."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí un propio para cada común.", "pasos": ["PERRO: ___ .", "NENA: ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuaderno viajero", "planteo": "Escribí tu nombre y el de tu ciudad."},
"tip": {"titulo": "¿Uno solo?", "texto": "Si es el nombre de uno solo, es propio."},
"ojo": ["Pancho va con mayúscula.", "perro va con minúscula en la oración."],
"resumen": [{"titulo": "Común", "texto": "Nombra a cualquiera."}, {"titulo": "Propio", "texto": "Nombre de uno solo."}, {"titulo": "Mayúscula", "texto": "Los propios la llevan."}],
"glosario": [{"palabra": "Común", "significado": "De cualquiera."}, {"palabra": "Propio", "significado": "De uno solo."}],
"carpeta": ["¿Qué palabra del dibujo es el nombre de un gato?", "¿Qué palabra del dibujo es el nombre de un río?", "Tomi escribió pancho con minúscula. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MICHI"), low("PARANÁ") + low("parana"), ["Pancho", "PANCHO", "Con mayúscula", "con mayúscula", "con mayuscula"]],
"soluciones": {"incompleto": "Por ejemplo: PANCHO. SOFI.", "solo": "Tu nombre y tu ciudad, con mayúscula.", "carpeta": ["MICHI.", "PARANÁ.", "Pancho: con mayúscula."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a buscar sustantivos en un cuento.",
"vas_a_ver": ["Leer el cuento", "Buscar palabras que nombran", "Marcar los sustantivos"],
"secciones": [
 S(1, "El cuento de Sofi", [
  P("Sofi pegó un cuento corto en su cuaderno."),
  IMG("El cuento", "Leelo despacio.", FG.tiras(["UN GATO VIVÍA EN UNA CASA.", "UN DÍA VIO UN RATÓN.", "EL RATÓN SE ESCONDIÓ EN UN ZAPATO."], numeros=True, cols=1)),
 ]),
 S(1, "Buscar los sustantivos", [
  P("Buscamos palabras que <b>nombran</b>."),
  P("GATO, CASA, DÍA, RATÓN, ZAPATO."),
  IMG("Los sustantivos", "Del cuento de Sofi.", FG.objetos([("raton", "RATÓN"), ("zapato", "ZAPATO"), ("castillo", "CASA")])),
 ]),
 S(2, "Para practicar", [
  P("Leé esta oración. La vas a usar en la carpeta."),
  IMG("Otra oración", "Buscá las palabras que nombran.", FG.tiras(["LA NENA COME UNA MANZANA EN LA PLAZA."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar", "planteo": "UN GATO VIVÍA EN UNA CASA.", "pasos": ["GATO nombra un animal.", "CASA nombra un lugar.", "Hay dos sustantivos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "EL RATÓN SE ESCONDIÓ EN UN ZAPATO.", "pasos": ["Un sustantivo es ___ .", "Otro sustantivo es ___ ."]},
"ejemplo_solo": {"titulo": "Tu cuento", "planteo": "Elegí un cuento. Copiá tres sustantivos."},
"tip": {"titulo": "Mirá antes", "texto": "Antes de un sustantivo suele ir EL, LA, UN o UNA."},
"ojo": ["VIVÍA no nombra: dice lo que hace.", "EN no nombra nada."],
"resumen": [{"titulo": "Leer", "texto": "Despacio, todo el cuento."}, {"titulo": "Buscar", "texto": "Palabras que nombran."}, {"titulo": "Pista", "texto": "Antes va EL, LA, UN, UNA."}],
"glosario": [{"palabra": "Cuento", "significado": "Historia que se cuenta."}, {"palabra": "Marcar", "significado": "Señalar algo con color."}],
"carpeta": ["En la oración del dibujo, ¿qué sustantivo nombra una fruta?", "En la oración, ¿qué sustantivo nombra un lugar?", "Tomi marcó COME como sustantivo. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MANZANA"), low("PLAZA"), ["NO", "no", "No"]],
"soluciones": {"incompleto": "RATÓN. ZAPATO.", "solo": "Tres palabras que nombran.", "carpeta": ["MANZANA.", "PLAZA.", "No: COME dice lo que se hace."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ordenar sustantivos en grupos.",
"vas_a_ver": ["Personas, animales, cosas y lugares", "Comunes y propios", "Armar los grupos"],
"secciones": [
 S(1, "Cuatro cajas", [
  P("Sofi arma <b>cajas</b> en su cuaderno."),
  P("Una para <b>personas</b>, otra para <b>animales</b>."),
  P("Otra para <b>cosas</b> y otra para <b>lugares</b>."),
  IMG("Las cajas de Sofi", "Cada palabra va a su caja.", FG.tiras(["PERSONAS: MAMÁ, NENE", "ANIMALES: GATO, PATO", "COSAS: VASO, SILLA", "LUGARES: PLAZA, CASA"], numeros=False)),
 ]),
 S(1, "Dos cajas más", [
  P("También separa <b>comunes</b> y <b>propios</b>."),
  IMG("Comunes y propios", "Los propios van con mayúscula.", FG.tiras(["COMUNES: perro, nena, río", "PROPIOS: Pancho, Sofi, Paraná"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Para ordenar", "¿A qué caja va cada una?", FG.dibujo_palabra([("vaso", "VASO"), ("estrella", "ESTRELLA"), ("manzana", "MANZANA")])),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenar", "planteo": "¿A qué caja va PATO?", "pasos": ["PATO nombra un animal.", "Va a la caja de animales.", "Es común."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿A qué caja va cada uno?", "pasos": ["MAESTRA: ___ .", "ESCUELA: ___ ."]},
"ejemplo_solo": {"titulo": "Tus cajas", "planteo": "Armá cuatro cajas. Poné dos palabras en cada una."},
"tip": {"titulo": "Preguntá", "texto": "¿Es persona, animal, cosa o lugar?"},
"ojo": ["Una palabra va a una sola caja.", "Los propios llevan mayúscula."],
"resumen": [{"titulo": "Cuatro cajas", "texto": "Personas, animales, cosas, lugares."}, {"titulo": "Dos cajas", "texto": "Comunes y propios."}, {"titulo": "Pregunta", "texto": "¿Qué nombra?"}],
"glosario": [{"palabra": "Clasificar", "significado": "Ordenar en grupos."}, {"palabra": "Grupo", "significado": "Cosas que van juntas."}],
"carpeta": ["¿A qué caja va VASO: personas, animales, cosas o lugares?", "¿Qué palabra del dibujo nombra una fruta?", "Tomi puso PLAZA en la caja de cosas. ¿Dónde va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("COSAS") + low("cosa"), low("MANZANA"), low("LUGARES") + low("lugar") + ["en lugares", "En lugares"]],
"soluciones": {"incompleto": "PERSONAS. LUGARES.", "solo": "Dos palabras en cada caja.", "carpeta": ["COSAS.", "MANZANA.", "En LUGARES."]},
}

ACT = {
"1": [MC("¿CUÁL ES UN SUSTANTIVO?", ["PERRO", "CORRE", "LINDO"], "PERRO", "PERRO NOMBRA UN ANIMAL.", n="aplicar"),
      UNI("UNÍ CADA PALABRA CON LO QUE NOMBRA.", [("MAMÁ", "PERSONA"), ("GATO", "ANIMAL"), ("PLAZA", "LUGAR")], "CADA SUSTANTIVO NOMBRA ALGO.", n="analizar")],
"2": [MC("¿CUÁL ES UN SUSTANTIVO PROPIO?", ["PANCHO", "PERRO", "GATO"], "PANCHO", "ES EL NOMBRE DE UNO SOLO.", n="aplicar"),
      TF("LOS SUSTANTIVOS PROPIOS VAN CON MAYÚSCULA.", "VERDADERO", "SOFI, PANCHO, CÓRDOBA.", n="recordar")],
"3": [MC("UN GATO VIVÍA EN UNA CASA. ¿CUÁL ES UN SUSTANTIVO?", ["CASA", "VIVÍA", "EN"], "CASA", "CASA NOMBRA UN LUGAR.", n="aplicar"),
      SA("EL RATÓN SE ESCONDIÓ EN UN ZAPATO. ESCRIBÍ UN SUSTANTIVO.", low("RATÓN") + low("raton") + low("ZAPATO"), "RATÓN O ZAPATO.", n="aplicar")],
"4": [UNI("UNÍ CADA PALABRA CON SU CAJA.", [("NENE", "PERSONAS"), ("PATO", "ANIMALES"), ("SILLA", "COSAS")], "PREGUNTÁ QUÉ NOMBRA.", n="analizar"),
      TF("PLAZA VA EN LA CAJA DE COSAS.", "FALSO", "PLAZA ES UN LUGAR.", n="error")],
"5": [MC("RELÁMPAGO. ¿CUÁL NOMBRA UNA COSA?", ["VASO", "SALTA"], "VASO", "VASO ES UNA COSA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ES PROPIO?", ["SOFI", "NENA"], "SOFI", "NOMBRE DE UNA SOLA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL NOMBRA UN LUGAR?", ["ESCUELA", "MAESTRA"], "ESCUELA", "ES UN LUGAR.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CÓMO SE ESCRIBE?", ["CÓRDOBA CON MAYÚSCULA", "CÓRDOBA CON MINÚSCULA"], "CÓRDOBA CON MAYÚSCULA", "ES PROPIO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿CUÁL ES UN SUSTANTIVO?", ["SILLA", "SALTA", "ALTO"], "SILLA", "SILLA NOMBRA UNA COSA.", n="aplicar")],
 [1, TF("CORRE ES UN SUSTANTIVO.", "FALSO", "CORRE DICE LO QUE SE HACE.", n="error")],
 [1, SA("ESCRIBÍ UN SUSTANTIVO QUE NOMBRE UN ANIMAL.", low("PERRO") + low("GATO") + low("PATO") + low("PALOMA") + low("VACA") + low("CABALLO") + low("PÁJARO") + low("pajaro") + low("RATÓN") + low("raton") + low("LEÓN") + low("leon") + low("OSO") + low("PEZ"), "POR EJEMPLO: PERRO.", n="recordar")],
 [2, MC("¿CUÁL ES UN SUSTANTIVO COMÚN?", ["CIUDAD", "CÓRDOBA", "SOFI"], "CIUDAD", "NOMBRA A CUALQUIERA.", n="aplicar")],
 [2, UNI("UNÍ CADA COMÚN CON UN PROPIO.", [("PERRO", "PANCHO"), ("NENA", "SOFI"), ("RÍO", "PARANÁ")], "EL PROPIO ES EL NOMBRE DE UNO.", n="analizar")],
 [2, TF("PANCHO SE ESCRIBE CON MINÚSCULA.", "FALSO", "VA CON MAYÚSCULA: ES PROPIO.", n="error")],
 [3, MC("LA NENA COME UNA MANZANA. ¿CUÁL ES UN SUSTANTIVO?", ["NENA", "COME", "UNA"], "NENA", "NENA NOMBRA UNA PERSONA.", n="aplicar")],
 [3, SA("UN GATO VIVÍA EN UNA CASA. ESCRIBÍ EL SUSTANTIVO QUE NOMBRA UN ANIMAL.", low("GATO"), "GATO.", n="aplicar")],
 [3, TF("EN LA ORACIÓN EL RATÓN SE ESCONDIÓ, ESCONDIÓ ES UN SUSTANTIVO.", "FALSO", "ESCONDIÓ DICE LO QUE HIZO.", n="error")],
 [4, UNI("UNÍ CADA PALABRA CON SU CAJA.", [("MAESTRA", "PERSONAS"), ("PALOMA", "ANIMALES"), ("ESCUELA", "LUGARES")], "PREGUNTÁ QUÉ NOMBRA.", n="analizar")],
 [4, MC("¿A QUÉ CAJA VA PELOTA?", ["COSAS", "LUGARES", "PERSONAS"], "COSAS", "PELOTA ES UNA COSA.", n="aplicar")],
 [4, SA("TOMI PUSO CASA EN LA CAJA DE ANIMALES. ¿EN QUÉ CAJA VA?", low("LUGARES") + low("lugar"), "CASA ES UN LUGAR.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: sustantivos", "examen_titulo": "Nivel jefe: sustantivos",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
