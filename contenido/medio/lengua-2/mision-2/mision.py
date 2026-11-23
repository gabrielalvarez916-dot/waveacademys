# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 2 · Letra cursiva. Genera mision-2.json.
Regla de primeros años y vía fonológica. Los dibujos usan la letra escolar Playwrite Argentina (fuentes/, licencia OFL).
Metáfora: el cuaderno viajero de Sofi (en segundo grado Sofi aprende a escribir «de corrido», con letras de la mano).
Niveles: 1 trazos para escribir en cursiva · 2 cursiva con vocales · 3 cursiva con las primeras consonantes · 4 copiar mi nombre en cursiva."""
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
"objetivo": "Vas a practicar los trazos de la letra cursiva.",
"vas_a_ver": ["Qué es la cursiva", "Bucles, puentes y ondas", "Sin levantar el lápiz"],
"secciones": [
 S(1, "La letra cursiva", [
  D("Letra cursiva", "Es la letra de la mano. Las letras van <b>unidas</b>, sin levantar el lápiz."),
  P("Sofi ya escribe en imprenta. Ahora aprende la cursiva."),
  IMG("Imprenta y cursiva", "La misma palabra, de dos formas.", FG.cursiva(["mamá", "sol"], imprenta=["mamá", "sol"])),
 ]),
 S(1, "Los trazos", [
  P("Antes de escribir, practicamos <b>trazos</b>: bucles, puentes y ondas."),
  P("Se hacen de izquierda a derecha, sin levantar el lápiz."),
  IMG("Trazos para repasar", "Repasá con el lápiz.", FG.cursiva(["llllll   eeeeee", "mmmmm   uuuuu"], repasar=True)),
 ]),
 S(2, "Para practicar", [
  P("Repasá los trazos en tu carpeta. Después hacelos solo."),
  IMG("Más trazos", "Bucles y puentes.", FG.cursiva(["eeeeeeee", "nnnnnnn"], repasar=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Un bucle", "planteo": "¿Cómo hago un bucle?", "pasos": ["Subo inclinado.", "Doy la vuelta arriba.", "Bajo y sigo sin levantar el lápiz."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Completá con una palabra.", "pasos": ["En cursiva las letras van ___ ."]},
"ejemplo_solo": {"titulo": "Tu renglón", "planteo": "Hacé un renglón entero de bucles en tu carpeta."},
"tip": {"titulo": "Sin apuro", "texto": "Despacio sale más lindo."},
"ojo": ["No levantes el lápiz en el medio del trazo.", "Escribí apoyado en el renglón."],
"resumen": [{"titulo": "Cursiva", "texto": "Letras unidas."}, {"titulo": "Trazos", "texto": "Bucles, puentes y ondas."}, {"titulo": "Lápiz", "texto": "No se levanta."}],
"glosario": [{"palabra": "Cursiva", "significado": "Letra de la mano, con letras unidas."}, {"palabra": "Trazo", "significado": "Una línea que hacemos con el lápiz."}],
"carpeta": ["¿Cómo van las letras en la cursiva?", "¿Hacia dónde se hacen los trazos: a la derecha o a la izquierda?", "Tomi levanta el lápiz en cada letra. ¿Qué no tiene que hacer?"],
"carpeta_nivel": ["recordar", "recordar", "error"],
"respuestas_carpeta": [low("UNIDAS") + low("JUNTAS"), low("A LA DERECHA") + low("DERECHA"), low("LEVANTAR EL LÁPIZ") + low("levantar el lapiz") + low("LEVANTARLO")],
"soluciones": {"incompleto": "UNIDAS.", "solo": "Un renglón de bucles.", "carpeta": ["Unidas.", "A la derecha.", "Levantar el lápiz."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a escribir las vocales en cursiva.",
"vas_a_ver": ["Las cinco vocales", "Unir vocales", "Palabras con vocales"],
"secciones": [
 S(1, "Las vocales en cursiva", [
  P("Las vocales son: a, e, i, o, u."),
  P("En cursiva, cada una tiene un <b>trazo de salida</b>."),
  P("Con esa salida se une con la que sigue."),
  IMG("Las vocales", "Imprenta y cursiva.", FG.cursiva(["a   e   i   o   u"], imprenta=["A E I O U"])),
 ]),
 S(1, "Unir vocales", [
  D("Unir", "La salida de una letra es la <b>entrada</b> de la otra."),
  P("Así escribimos <b>ae</b>, <b>io</b>, <b>ua</b> sin levantar el lápiz."),
  IMG("Vocales unidas", "Sin levantar el lápiz.", FG.cursiva(["ae   io   ua   oi"])),
 ]),
 S(2, "Para practicar", [
  P("Repasá las vocales en tu carpeta."),
  IMG("Para repasar", "Despacito.", FG.cursiva(["a a a   e e e", "i i i   o o o   u u u"], repasar=True)),
 ]),
],
"ejemplo_completo": {"titulo": "La a", "planteo": "¿Cómo escribo la a en cursiva?", "pasos": ["Hago una ronda.", "Subo y bajo pegado a la ronda.", "Salgo hacia la derecha."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Completá las vocales.", "pasos": ["a, e, ___ , o, ___ ."]},
"ejemplo_solo": {"titulo": "Tu renglón", "planteo": "Escribí en cursiva: aeiou, sin levantar el lápiz."},
"tip": {"titulo": "La salida", "texto": "Cada letra termina con una colita para unirse."},
"ojo": ["El punto de la i se pone al final.", "La e en cursiva tiene un bucle chiquito."],
"resumen": [{"titulo": "Vocales", "texto": "a, e, i, o, u."}, {"titulo": "Salida", "texto": "Una colita a la derecha."}, {"titulo": "Unir", "texto": "La salida es la entrada."}],
"glosario": [{"palabra": "Vocal", "significado": "a, e, i, o, u."}, {"palabra": "Unir", "significado": "Juntar una letra con la otra."}],
"carpeta": ["¿Cuántas vocales hay?", "¿Cuándo se pone el punto de la i?", "Sofi escribió las vocales separadas. ¿Cómo van en cursiva?"],
"carpeta_nivel": ["recordar", "recordar", "error"],
"respuestas_carpeta": [["5", "cinco", "CINCO"], low("AL FINAL") + low("AL TERMINAR") + low("DESPUÉS") + low("despues"), low("UNIDAS") + low("JUNTAS")],
"soluciones": {"incompleto": "I. U.", "solo": "aeiou unidas.", "carpeta": ["5.", "Al final.", "Unidas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir en cursiva sílabas y palabras cortas.",
"vas_a_ver": ["Consonantes en cursiva", "Sílabas unidas", "Palabras cortas"],
"secciones": [
 S(1, "Primeras consonantes", [
  P("Con las vocales y algunas consonantes ya armamos palabras."),
  IMG("Consonantes", "Imprenta y cursiva.", FG.cursiva(["m   l   s   p   t"], imprenta=["M L S P T"])),
 ]),
 S(1, "Sílabas y palabras", [
  D("Sílaba", "Una consonante unida a una vocal: <b>ma</b>, <b>lo</b>, <b>sa</b>, <b>pe</b>, <b>tu</b>."),
  P("Juntamos sílabas y salen palabras: <b>mesa</b>, <b>sapo</b>, <b>pato</b>."),
  IMG("Palabras en cursiva", "Todo unido.", FG.cursiva(["mesa", "sapo", "pato"], imprenta=["mesa", "sapo", "pato"])),
 ]),
 S(2, "Para practicar", [
  P("Repasá las palabras. Después copialas solo."),
  IMG("Para repasar", "Sin levantar el lápiz.", FG.cursiva(["mamá   sol", "lupa   taza"], repasar=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Escribir sapo", "planteo": "¿Cómo escribo sapo en cursiva?", "pasos": ["Escribo sa.", "Sin levantar, sigo con po.", "Queda sapo, todo unido."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Completá la palabra.", "pasos": ["me + sa = ___ ."]},
"ejemplo_solo": {"titulo": "Tu palabra", "planteo": "Escribí en cursiva el nombre de tu fruta preferida."},
"tip": {"titulo": "Pensá la sílaba", "texto": "Decila despacito mientras la escribís."},
"ojo": ["La palabra va toda unida.", "Entre palabra y palabra, un espacio."],
"resumen": [{"titulo": "Consonante", "texto": "Se une a la vocal."}, {"titulo": "Sílaba", "texto": "ma, lo, sa."}, {"titulo": "Palabra", "texto": "Toda unida."}],
"glosario": [{"palabra": "Sílaba", "significado": "Un pedacito de palabra."}, {"palabra": "Consonante", "significado": "Las letras que no son vocales."}],
"carpeta": ["¿Qué palabra se forma con me + sa?", "¿Qué palabra se forma con pa + to?", "Tomi escribió sa po, separado. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MESA"), low("PATO"), low("SAPO") + low("unido") + low("todo unido")],
"soluciones": {"incompleto": "MESA.", "solo": "Por ejemplo: pera.", "carpeta": ["Mesa.", "Pato.", "Sapo, todo unido."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir tu nombre en cursiva.",
"vas_a_ver": ["La mayúscula cursiva", "Tu nombre unido", "Firmar tus trabajos"],
"secciones": [
 S(1, "La mayúscula cursiva", [
  D("Mayúscula cursiva", "Los nombres empiezan con <b>mayúscula</b>. En cursiva, es más grande y con adornos."),
  IMG("Nombres en cursiva", "Con mayúscula al principio.", FG.cursiva(["Sofi", "Tomi", "Ana"], imprenta=["Sofi", "Tomi", "Ana"])),
 ]),
 S(1, "Tu nombre", [
  P("Primero escribí tu nombre en imprenta. Después, mirá cada letra."),
  P("Copialo en cursiva, <b>sin levantar el lápiz</b> después de la mayúscula."),
  IMG("Más nombres", "Mirá la mayúscula.", FG.cursiva(["Lola", "Mateo", "Pedro"], imprenta=["Lola", "Mateo", "Pedro"])),
 ]),
 S(2, "Para practicar", [
  P("Repasá estos nombres. Después escribí el tuyo."),
  IMG("Para repasar", "Despacito.", FG.cursiva(["Sofi   Tomi", "Ana   Lola"], repasar=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Firmar", "planteo": "Sofi firma su dibujo.", "pasos": ["Empieza con la mayúscula.", "Sigue con ofi, todo unido.", "Queda: Sofi."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Completá.", "pasos": ["Los nombres empiezan con ___ ."]},
"ejemplo_solo": {"titulo": "Tu firma", "planteo": "Escribí tu nombre en cursiva en todos tus trabajos de esta semana."},
"tip": {"titulo": "Practicá tu nombre", "texto": "Escribilo un renglón entero."},
"ojo": ["El nombre empieza con mayúscula.", "No mezcles cursiva con imprenta."],
"resumen": [{"titulo": "Mayúscula", "texto": "Al principio del nombre."}, {"titulo": "Unido", "texto": "Todo el nombre."}, {"titulo": "Firmar", "texto": "En tus trabajos."}],
"glosario": [{"palabra": "Firma", "significado": "Tu nombre escrito por vos."}, {"palabra": "Nombre propio", "significado": "El nombre de una persona."}],
"carpeta": ["¿Con qué letra empieza un nombre?", "¿Cómo va el nombre en cursiva: unido o separado?", "Tomi escribió su nombre con minúscula. ¿Con qué tiene que empezar?"],
"carpeta_nivel": ["recordar", "recordar", "error"],
"respuestas_carpeta": [low("MAYÚSCULA") + low("mayuscula") + low("CON MAYÚSCULA"), low("UNIDO"), low("MAYÚSCULA") + low("mayuscula") + low("CON MAYÚSCULA")],
"soluciones": {"incompleto": "MAYÚSCULA.", "solo": "Tu nombre en cursiva.", "carpeta": ["Mayúscula.", "Unido.", "Con mayúscula."]},
}

ACT = {
"1": [MC("EN LA CURSIVA, LAS LETRAS VAN…", ["UNIDAS", "SEPARADAS", "AL REVÉS"], "UNIDAS", "SIN LEVANTAR EL LÁPIZ.", n="recordar"),
      TF("LOS TRAZOS SE HACEN DE DERECHA A IZQUIERDA.", "FALSO", "DE IZQUIERDA A DERECHA.", n="error")],
"2": [ORD("ORDENÁ LAS VOCALES.", ["O", "A", "U", "E", "I"], ["A", "E", "I", "O", "U"], "A, E, I, O, U.", n="aplicar"),
      MC("¿CUÁNDO SE PONE EL PUNTO DE LA I EN CURSIVA?", ["AL TERMINAR LA PALABRA", "ANTES DE EMPEZAR", "NUNCA"], "AL TERMINAR LA PALABRA", "PARA NO LEVANTAR EL LÁPIZ.", n="analizar")],
"3": [UNI("UNÍ LAS SÍLABAS CON SU PALABRA.", [("ME + SA", "MESA"), ("SA + PO", "SAPO"), ("PA + TO", "PATO")], "SÍLABAS UNIDAS.", n="aplicar"),
      SA("¿QUÉ PALABRA SE FORMA CON LU + PA?", low("LUPA"), "LUPA.", n="aplicar")],
"4": [MC("¿CON QUÉ EMPIEZA UN NOMBRE?", ["CON MAYÚSCULA", "CON MINÚSCULA", "CON UN PUNTO"], "CON MAYÚSCULA", "LOS NOMBRES LLEVAN MAYÚSCULA.", n="recordar"),
      TF("CONVIENE MEZCLAR CURSIVA E IMPRENTA EN EL NOMBRE.", "FALSO", "TODO EN CURSIVA.", n="analizar")],
"5": [MC("RELÁMPAGO. LA CURSIVA ES LETRA…", ["UNIDA", "SEPARADA"], "UNIDA", "DE CORRIDO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁNTAS VOCALES HAY?", ["5", "3"], "5", "A, E, I, O, U.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ME + SA ES…", ["MESA", "SAME"], "MESA", "ME-SA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. UN NOMBRE EMPIEZA CON…", ["MAYÚSCULA", "MINÚSCULA"], "MAYÚSCULA", "SIEMPRE.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES LA LETRA CURSIVA?", ["LETRA DE LA MANO, UNIDA", "LETRA DE IMPRENTA", "LETRA DE NÚMEROS"], "LETRA DE LA MANO, UNIDA", "LETRAS UNIDAS.", n="recordar")],
 [1, TF("TOMI LEVANTA EL LÁPIZ EN CADA LETRA Y ESTÁ BIEN.", "FALSO", "EN CURSIVA NO SE LEVANTA.", n="error")],
 [1, UNI("UNÍ CADA TRAZO CON SU NOMBRE.", [("LLLL", "BUCLES"), ("MMMM", "PUENTES"), ("UUUU", "ONDAS")], "LOS TRAZOS DE LA CURSIVA.", n="analizar")],
 [2, MC("¿CUÁL ES UNA VOCAL?", ["E", "M", "S"], "E", "A, E, I, O, U.", n="recordar")],
 [2, TF("LA SALIDA DE UNA LETRA ES LA ENTRADA DE LA OTRA.", "VERDADERO", "ASÍ SE UNEN.", n="analizar")],
 [2, ORD("ORDENÁ LAS VOCALES.", ["U", "I", "A", "O", "E"], ["A", "E", "I", "O", "U"], "A, E, I, O, U.", n="aplicar")],
 [3, SA("¿QUÉ PALABRA SE FORMA CON SA + PO?", low("SAPO"), "SAPO.", n="aplicar")],
 [3, MC("¿CÓMO SE ESCRIBE UNA PALABRA EN CURSIVA?", ["TODA UNIDA", "LETRA POR LETRA SEPARADA", "AL REVÉS"], "TODA UNIDA", "SIN LEVANTAR EL LÁPIZ.", n="aplicar")],
 [3, SA("¿QUÉ PALABRA SE FORMA CON TA + ZA?", low("TAZA"), "TAZA.", n="aplicar")],
 [4, MC("¿CÓMO SE ESCRIBE BIEN EL NOMBRE?", ["SOFI, CON MAYÚSCULA", "sofi, todo en minúscula", "SoFi, mezclado"], "SOFI, CON MAYÚSCULA", "MAYÚSCULA AL PRINCIPIO.", n="error")],
 [4, TF("EN LOS TRABAJOS PODÉS FIRMAR CON TU NOMBRE EN CURSIVA.", "VERDADERO", "ES TU FIRMA.", n="recordar")],
 [4, MC("DESPUÉS DE LA MAYÚSCULA, EL NOMBRE VA…", ["UNIDO", "SEPARADO"], "UNIDO", "TODO EN CURSIVA.", n="aplicar")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: letra cursiva", "examen_titulo": "Nivel jefe: letra cursiva",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
