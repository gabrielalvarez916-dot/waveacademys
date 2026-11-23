# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 11 · Ortografía: R y RR. Genera mision-11.json.
Regla de primeros años y vía fonológica (la VOZ de las clases dice sonidos —suave como en «pera», fuerte «rrr» como en «perro»—,
nunca nombres de letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (Sofi, detective de palabras, otra vez).
Niveles: 1 sonido suave y sonido fuerte · 2 R al principio · 3 RR entre vocales · 4 dictado con R y RR."""
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
"objetivo": "Vas a escuchar el sonido suave y el sonido fuerte.",
"vas_a_ver": ["Sonido suave", "Sonido fuerte", "PERA y PERRA"],
"secciones": [
 S(1, "Dos sonidos", [
  P("Sofi, la detective, escucha dos palabras: PERA y PERRO."),
  P("En PERA el sonido es <b>suave</b>."),
  P("En PERRO el sonido es <b>fuerte</b>: rrr."),
  IMG("PERA y PERRO", "Suave con R. Fuerte con RR.", FG.tiras(["PERA → SUAVE → R", "PERRO → FUERTE → RR"], numeros=False, cols=1)),
 ]),
 S(1, "Cambia la palabra", [
  P("Si cambia el sonido, cambia la palabra."),
  P("CARO no es lo mismo que CARRO."),
  IMG("Parejas", "Una letra cambia todo.", FG.tiras(["PERA · PERRA", "CARO · CARRO", "CORO · CORRO"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Decí las palabras en voz alta. Las vas a usar en la carpeta."),
  IMG("¿Suave o fuerte?", "Escuchá con atención.", FG.nombres(["LORO", "TORRE", "TORO", "BURRO"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Escuchar", "planteo": "¿CARO o CARRO?", "pasos": ["CARO suena suave.", "CARRO suena fuerte.", "Son palabras distintas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿Suave o fuerte?", "pasos": ["PERA suena ___ .", "PERRO suena ___ ."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Buscá en tu casa una palabra con sonido fuerte."},
"tip": {"titulo": "Decilo en voz alta", "texto": "El sonido fuerte vibra más."},
"ojo": ["PERA y PERRA son palabras distintas.", "Escuchá antes de escribir."],
"resumen": [{"titulo": "Suave", "texto": "PERA, LORO."}, {"titulo": "Fuerte", "texto": "PERRO, TORRE."}, {"titulo": "Cuidado", "texto": "Cambia la palabra."}],
"glosario": [{"palabra": "Sonido", "significado": "Lo que escuchamos."}, {"palabra": "Vibrar", "significado": "Temblar rápido."}],
"carpeta": ["¿Qué palabras del dibujo suenan suave?", "¿Qué palabras del dibujo suenan fuerte?", "Tomi dice que CARO y CARRO son iguales. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("LORO Y TORO") + low("LORO, TORO") + low("TORO Y LORO"), low("TORRE Y BURRO") + low("TORRE, BURRO") + low("BURRO Y TORRE"), ["NO", "no", "No"]],
"soluciones": {"incompleto": "SUAVE. FUERTE.", "solo": "Por ejemplo: GORRA.", "carpeta": ["LORO y TORO.", "TORRE y BURRO.", "No: son palabras distintas."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a escribir palabras que empiezan con R.",
"vas_a_ver": ["R al principio", "Suena fuerte", "Una sola R"],
"secciones": [
 S(1, "R al principio", [
  P("RATÓN, RANA, ROSA: empiezan con sonido <b>fuerte</b>."),
  D("La regla", "Al principio suena fuerte, pero va <b>una sola R</b>."),
  IMG("Con R inicial", "Suenan fuerte con una R.", FG.objetos([("raton", "RATÓN"), ("rana", "RANA"), ("flor", "ROSA")])),
 ]),
 S(1, "Más palabras", [
  P("RUEDA, REGALO, RISA, ROJO, RELOJ."),
  IMG("Palabras con R al principio", "Siempre una sola R.", FG.letras("RELOJ", resaltar=(0,))),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Cuál está bien?", "Pensá en la regla.", FG.nombres(["RRATÓN", "RATÓN", "RROSA", "ROSA"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "RUEDA", "planteo": "¿Con una R o con dos?", "pasos": ["Está al principio.", "Suena fuerte.", "Va una sola R: RUEDA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí la letra que falta.", "pasos": ["_ANA.", "_ISA."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Escribí tres palabras que empiecen con R."},
"tip": {"titulo": "Al principio, una", "texto": "Nunca empieza una palabra con RR."},
"ojo": ["RRATÓN está mal.", "Se escribe RATÓN."],
"resumen": [{"titulo": "Al principio", "texto": "Suena fuerte."}, {"titulo": "Se escribe", "texto": "Una sola R."}, {"titulo": "Ejemplos", "texto": "RATÓN, ROSA."}],
"glosario": [{"palabra": "Inicial", "significado": "La que va al principio."}, {"palabra": "Regla", "significado": "Algo que siempre se cumple."}],
"carpeta": ["¿Cómo se escribe bien el animal del dibujo?", "¿Cómo se escribe bien la flor del dibujo?", "Tomi escribió RREGALO. ¿Cómo va?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("RATÓN") + low("raton"), low("ROSA"), low("REGALO")],
"soluciones": {"incompleto": "R. R.", "solo": "Por ejemplo: RISA, ROJO, RUEDA.", "carpeta": ["RATÓN.", "ROSA.", "REGALO, con una R."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir palabras con RR.",
"vas_a_ver": ["Entre dos vocales", "Sonido fuerte", "Palabras con RR"],
"secciones": [
 S(1, "RR en el medio", [
  P("En PERRO, el sonido fuerte está <b>en el medio</b>."),
  D("La regla", "Fuerte <b>entre dos vocales</b>: se escribe <b>RR</b>."),
  IMG("PERRO", "RR entre E y O.", FG.letras("PERRO", resaltar=(2, 3))),
 ]),
 S(1, "Más palabras con RR", [
  P("TORRE, GORRA, BURRO, CARRO, ARROZ."),
  IMG("Con RR", "Todas suenan fuerte en el medio.", FG.nombres(["TORRE", "GORRA", "BURRO", "ARROZ"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras con huecos", "¿R o RR?", FG.nombres(["CA_O (AUTO)", "PE_A (FRUTA)", "GO_A"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "GORRA", "planteo": "¿R o RR?", "pasos": ["Suena fuerte.", "Está entre O y A.", "Va RR: GORRA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí R o RR.", "pasos": ["BU__O.", "TO__E."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Buscá en un libro dos palabras con RR."},
"tip": {"titulo": "Fuerte en el medio", "texto": "Si suena fuerte entre vocales, va RR."},
"ojo": ["PERO suena suave: una R.", "PERRO suena fuerte: RR."],
"resumen": [{"titulo": "RR", "texto": "Fuerte entre vocales."}, {"titulo": "R", "texto": "Suave entre vocales."}, {"titulo": "Ejemplos", "texto": "PERRO, TORRE."}],
"glosario": [{"palabra": "Vocales", "significado": "A, E, I, O, U."}, {"palabra": "Gorra", "significado": "Sombrero con visera."}],
"carpeta": ["Completá CA_O si es un auto. ¿R o RR?", "Completá PE_A si es una fruta. ¿R o RR?", "Tomi escribió GORA. ¿Cómo se escribe?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("RR") + low("CARRO"), low("R") + low("PERA"), low("GORRA")],
"soluciones": {"incompleto": "RR. RR.", "solo": "Dos palabras con RR.", "carpeta": ["RR: CARRO.", "R: PERA.", "GORRA, con RR."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con R y RR en un dictado.",
"vas_a_ver": ["Escuchar el sonido", "Mirar dónde está", "Escribir y revisar"],
"secciones": [
 S(1, "Tres preguntas", [
  P("¿Suena <b>suave</b> o <b>fuerte</b>?"),
  P("Si es fuerte, ¿está al <b>principio</b> o en el <b>medio</b>?"),
  IMG("Cómo decido", "Tres casos.", FG.tiras(["SUAVE → R (PERA)", "FUERTE AL PRINCIPIO → R (RATÓN)", "FUERTE EN EL MEDIO → RR (PERRO)"], numeros=False, cols=1)),
 ]),
 S(1, "Oraciones dictadas", [
  P("Escuchamos la oración entera y escribimos."),
  IMG("Para dictar", "Con mayúscula y punto.", FG.tiras(["EL PERRO COME ARROZ.", "LA RANA SALTA EN LA TORRE."], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Pedile a alguien que te dicte estas palabras."),
  IMG("Para dictar", "Escribilas en tu carpeta.", FG.nombres(["RISA", "CARRO", "LORO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Dictado", "planteo": "Me dictan: BURRO.", "pasos": ["Suena fuerte.", "Está en el medio.", "Escribo BURRO con RR."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Me dictan: EL _ATÓN Y EL PE_O.", "pasos": ["RATÓN: ___ .", "PERRO: ___ ."]},
"ejemplo_solo": {"titulo": "Tu dictado", "planteo": "Pedí que te dicten: LA GORRA ES ROJA."},
"tip": {"titulo": "Revisá al final", "texto": "Mirá cada palabra con R o RR."},
"ojo": ["Nunca RR al principio.", "Suave en el medio: una R."],
"resumen": [{"titulo": "Suave", "texto": "Una R."}, {"titulo": "Fuerte al principio", "texto": "Una R."}, {"titulo": "Fuerte en el medio", "texto": "RR."}],
"glosario": [{"palabra": "Dictado", "significado": "Escribir lo que otro dice."}, {"palabra": "Revisar", "significado": "Mirar de nuevo para corregir."}],
"carpeta": ["Te dictan: el animal que dice burro. ¿Cómo se escribe?", "Te dictan: el pájaro que habla. ¿Cómo se escribe?", "Tomi escribió RRISA en el dictado. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("BURRO"), low("LORO"), low("RISA")],
"soluciones": {"incompleto": "R. RR.", "solo": "LA GORRA ES ROJA.", "carpeta": ["BURRO.", "LORO.", "RISA, con una R."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA SUENA FUERTE?", ["PERRO", "PERA", "LORO"], "PERRO", "PERRO SUENA FUERTE.", n="aplicar"),
      TF("CARO Y CARRO SON LA MISMA PALABRA.", "FALSO", "CAMBIA EL SONIDO Y CAMBIA LA PALABRA.", n="error")],
"2": [MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["RATÓN", "RRATÓN"], "RATÓN", "AL PRINCIPIO, UNA SOLA R.", n="aplicar"),
      SA("ESCRIBÍ BIEN: _UEDA", low("RUEDA"), "RUEDA, CON UNA R.", n="aplicar")],
"3": [MC("TO_E. ¿QUÉ VA?", ["RR", "R"], "RR", "FUERTE EN EL MEDIO.", n="aplicar"),
      UNI("UNÍ CADA PALABRA CON SU SONIDO.", [("PERRO", "FUERTE"), ("PERA", "SUAVE"), ("GORRA", "FUERTE")], "ESCUCHÁ EL SONIDO.", n="analizar")],
"4": [SA("ESCRIBÍ LA PALABRA: EL ANIMAL QUE LADRA ES EL ___", low("PERRO"), "PERRO, CON RR.", n="aplicar"),
      SA("ESCRIBÍ LA PALABRA: LA FLOR CON ESPINAS ES LA ___", low("ROSA"), "ROSA, CON UNA R.", n="aplicar")],
"5": [MC("RELÁMPAGO. AL PRINCIPIO VA…", ["UNA R", "RR"], "UNA R", "NUNCA RR AL PRINCIPIO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. FUERTE EN EL MEDIO VA…", ["RR", "UNA R"], "RR", "COMO EN PERRO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ESTÁ BIEN?", ["BURRO", "BURO"], "BURRO", "SUENA FUERTE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ESTÁ BIEN?", ["LORO", "LORRO"], "LORO", "SUENA SUAVE.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ PALABRA SUENA SUAVE?", ["PERA", "PERRO", "TORRE"], "PERA", "PERA SUENA SUAVE.", n="aplicar")],
 [1, TF("PERRO SUENA FUERTE EN EL MEDIO.", "VERDADERO", "POR ESO LLEVA RR.", n="recordar")],
 [1, UNI("UNÍ CADA PALABRA CON SU SONIDO.", [("TORO", "SUAVE"), ("TORRE", "FUERTE"), ("LORO", "SUAVE")], "DECILAS EN VOZ ALTA.", n="analizar")],
 [2, MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["ROSA", "RROSA"], "ROSA", "AL PRINCIPIO, UNA SOLA R.", n="aplicar")],
 [2, SA("ESCRIBÍ BIEN: _EGALO", low("REGALO"), "REGALO.", n="aplicar")],
 [2, TF("RRANA ESTÁ BIEN ESCRITA.", "FALSO", "SE ESCRIBE RANA.", n="error")],
 [3, MC("GO_A. ¿QUÉ VA?", ["RR", "R"], "RR", "FUERTE EN EL MEDIO.", n="aplicar")],
 [3, SA("ESCRIBÍ BIEN: A_OZ", low("ARROZ"), "ARROZ, CON RR.", n="aplicar")],
 [3, TF("PERO Y PERRO SE ESCRIBEN IGUAL.", "FALSO", "PERO SUAVE, PERRO FUERTE.", n="error")],
 [4, SA("ESCRIBÍ LA PALABRA: EL AUTO TAMBIÉN SE LLAMA ___", low("CARRO"), "CARRO, CON RR.", n="aplicar")],
 [4, MC("¿CUÁL ESTÁ MAL ESCRITA?", ["RRISA", "LORO", "BURRO"], "RRISA", "AL PRINCIPIO, UNA SOLA R.", n="error")],
 [4, SA("CORREGÍ: TORE", low("TORRE"), "TORRE, CON RR.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 11, "estilo": "primeros",
     "practica": "Práctica general: R y RR", "examen_titulo": "Nivel jefe: R y RR",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-11.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
