# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 8 · Toys and Games. Genera mision-8.json.
Regla de primeros años. Metáfora: la caja de juguetes de Sofi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 ball, doll, car · 2 I have a ball · 3 big y small · 4 yes or no: el juego de los juguetes."""
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
"objetivo": "Vas a nombrar tus juguetes en inglés.",
"vas_a_ver": ["BALL: pelota", "DOLL: muñeca", "CAR: auto"],
"secciones": [
 S(1, "Mis juguetes", [
  D("Juguete", "Cosa que usamos para jugar."),
  P("Pelota es <b>BALL</b>, muñeca es <b>DOLL</b> y auto es <b>CAR</b>."),
  IMG("Mis juguetes", "En inglés.", FG.tiras(["PELOTA = BALL", "MUÑECA = DOLL", "AUTO = CAR"], numeros=False, cols=1)),
 ]),
 S(1, "Uno más", [
  P("El osito de peluche es <b>TEDDY</b>. ¡Todos podemos jugar con todos los juguetes!"),
  IMG("El osito", "En inglés.", FG.tiras(["OSITO = TEDDY"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la caja de juguetes de Sofi. La vas a usar en la carpeta."),
  IMG("La caja de Sofi", "¿Qué juguete es?", FG.tiras(["UNA PELOTA", "UN AUTITO", "UNA MUÑECA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi juega", "planteo": "Sofi saca una pelota.", "pasos": ["La hace rebotar.", "Dice: BALL!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Auto en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tus juguetes", "planteo": "Mostrá tus juguetes y nombralos en inglés."},
"tip": {"titulo": "Jugá y decí", "texto": "Decí el nombre cuando agarrás el juguete."},
"ojo": ["BALL es pelota.", "DOLL es muñeca."],
"resumen": [{"titulo": "BALL", "texto": "Pelota."}, {"titulo": "DOLL", "texto": "Muñeca."}, {"titulo": "CAR / TEDDY", "texto": "Auto y osito."}],
"glosario": [{"palabra": "BALL", "significado": "Pelota."}, {"palabra": "TEDDY", "significado": "Osito de peluche."}],
"carpeta": ["Sofi saca una pelota. ¿Cómo se dice?", "Sofi saca un autito. ¿Cómo se dice?", "Sofi saca una muñeca y dice BALL. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("BALL"), acepta("CAR"), acepta("DOLL")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "CAR.", "solo": "Tus juguetes.", "carpeta": ["BALL.", "CAR.", "DOLL."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a decir qué juguete tenés en inglés.",
"vas_a_ver": ["I HAVE A…", "Decir lo que tengo", "Mis amigos tienen"],
"secciones": [
 S(1, "Yo tengo", [
  D("Tener", "Algo es nuestro, está con nosotros."),
  P("Para decir que tenemos algo decimos <b>I HAVE A</b> y el juguete."),
  IMG("Yo tengo", "Quiere decir: tengo un…", FG.tiras(["I HAVE A BALL.", "I HAVE A CAR."], numeros=False, cols=1)),
 ]),
 S(1, "Mis amigos", [
  P("Cada amigo dice lo que tiene con <b>I HAVE A</b>."),
  IMG("Los chicos", "Lo que tienen.", FG.tiras(["TOMI: I HAVE A CAR.", "SOFI: I HAVE A DOLL.", "LEO: I HAVE A TEDDY."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que tienen los chicos. Lo vas a usar en la carpeta."),
  IMG("¿Qué tienen?", "Sus juguetes.", FG.tiras(["TOMI TIENE UNA PELOTA", "SOFI TIENE UN OSITO", "LEO TIENE UN AUTO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi cuenta", "planteo": "Tomi muestra su auto.", "pasos": ["Lo levanta.", "Dice: I HAVE A CAR!", "¡Qué lindo auto!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "I ___ A BALL.", "pasos": ["I ___ A BALL."]},
"ejemplo_solo": {"titulo": "Tu juguete", "planteo": "Mostrá tu juguete preferido y decí I HAVE A…"},
"tip": {"titulo": "Mostrá", "texto": "Mostrá el juguete al decir I HAVE A."},
"ojo": ["HAVE es tener.", "I es yo."],
"resumen": [{"titulo": "I HAVE A…", "texto": "Tengo un…"}, {"titulo": "HAVE", "texto": "Tener."}, {"titulo": "Mostrar", "texto": "Decir lo que tengo."}],
"glosario": [{"palabra": "HAVE", "significado": "Tener."}, {"palabra": "I", "significado": "Yo."}],
"carpeta": ["Tomi tiene una pelota. Completá: I HAVE A ___.", "Sofi tiene un osito. Completá: I HAVE A ___.", "Leo tiene un auto y dice I HAVE A DOLL. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("BALL"), acepta("TEDDY", "TEDDY BEAR"), acepta("I HAVE A CAR", "CAR")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "HAVE.", "solo": "Tu juguete.", "carpeta": ["BALL.", "TEDDY.", "I HAVE A CAR."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a decir si un juguete es grande o chico en inglés.",
"vas_a_ver": ["BIG: grande", "SMALL: chico", "Comparar juguetes"],
"secciones": [
 S(1, "Grande y chico", [
  D("Tamaño", "Qué tan grande o chica es una cosa."),
  P("Grande es <b>BIG</b> y chico es <b>SMALL</b>."),
  IMG("Tamaños", "En inglés.", FG.tiras(["GRANDE = BIG", "CHICO = SMALL"], numeros=False, cols=1)),
 ]),
 S(1, "Juguetes grandes y chicos", [
  P("Decimos el tamaño antes del juguete: <b>A BIG BALL</b>."),
  IMG("Ejemplos", "Tamaño y juguete.", FG.tiras(["A BIG BALL", "A SMALL CAR", "A BIG TEDDY"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los juguetes de Tomi. Los vas a usar en la carpeta."),
  IMG("Los juguetes de Tomi", "¿Grande o chico?", FG.tiras(["UN OSO ENORME", "UN AUTITO CHIQUITO", "UNA PELOTA GIGANTE"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi compara", "planteo": "Sofi tiene dos pelotas.", "pasos": ["Una es enorme.", "La otra es chiquita.", "BIG BALL y SMALL BALL."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Un auto chiquito: A ___ CAR.", "pasos": ["A ___ CAR."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "Buscá un juguete BIG y uno SMALL."},
"tip": {"titulo": "Con las manos", "texto": "BIG: abrí los brazos. SMALL: juntá los dedos."},
"ojo": ["BIG es grande.", "SMALL es chico."],
"resumen": [{"titulo": "BIG", "texto": "Grande."}, {"titulo": "SMALL", "texto": "Chico."}, {"titulo": "A BIG BALL", "texto": "Una pelota grande."}],
"glosario": [{"palabra": "BIG", "significado": "Grande."}, {"palabra": "SMALL", "significado": "Chico."}],
"carpeta": ["Un oso enorme. ¿BIG o SMALL?", "Un autito chiquito. ¿BIG o SMALL?", "Una pelota gigante y Tomi dice A SMALL BALL. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("BIG"), acepta("SMALL"), acepta("A BIG BALL", "BIG BALL", "BIG")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "SMALL.", "solo": "Tus juguetes.", "carpeta": ["BIG.", "SMALL.", "A BIG BALL."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a jugar a adivinar juguetes con YES y NO.",
"vas_a_ver": ["IS IT A BALL?", "YES o NO", "El juego de los juguetes"],
"secciones": [
 S(1, "Adivinar", [
  D("Juego", "Actividad para divertirnos con reglas."),
  P("Uno esconde un juguete. El otro pregunta: <b>IS IT A BALL?</b>"),
  IMG("La pregunta", "Para adivinar.", FG.tiras(["IS IT A BALL?", "IS IT A DOLL?"], numeros=False, cols=1)),
 ]),
 S(1, "Sí o no", [
  P("Contestamos <b>YES</b> si es, o <b>NO</b> si no es."),
  IMG("Respuestas", "Sí o no.", FG.tiras(["YES, IT IS!", "NO, IT ISN'T."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá qué escondió Sofi. Lo vas a usar en la carpeta."),
  IMG("Lo que escondió", "¿Qué es?", FG.tiras(["SOFI ESCONDE UN AUTO", "TOMI ESCONDE UN OSITO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "A jugar", "planteo": "Sofi esconde un auto.", "pasos": ["Tomi: IS IT A BALL?", "Sofi: NO, IT ISN'T.", "Tomi: IS IT A CAR? YES!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "IS IT A CAR? ___, IT IS!", "pasos": ["___, IT IS!"]},
"ejemplo_solo": {"titulo": "A jugar", "planteo": "Escondé un juguete y que tu familia adivine en inglés."},
"tip": {"titulo": "Turnos", "texto": "Esperá tu turno para preguntar."},
"ojo": ["YES es sí.", "NO es no."],
"resumen": [{"titulo": "IS IT A…?", "texto": "¿Es un…?"}, {"titulo": "YES", "texto": "Sí."}, {"titulo": "NO", "texto": "No."}],
"glosario": [{"palabra": "YES", "significado": "Sí."}, {"palabra": "NO", "significado": "No."}],
"carpeta": ["Sofi esconde un auto. IS IT A CAR?", "Sofi esconde un auto. IS IT A BALL?", "Tomi esconde un osito y dice NO a IS IT A TEDDY? ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("YES", "YES, IT IS", "YES IT IS"), acepta("NO", "NO, IT ISN'T", "NO IT ISNT", "NO IT ISN'T"), acepta("YES", "YES, IT IS", "YES IT IS")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "YES.", "solo": "Tu juego.", "carpeta": ["YES.", "NO.", "YES, IT IS."]},
}

ACT = {
"1": [MC("PELOTA EN INGLÉS ES…", ["BALL", "DOLL", "CAR"], "BALL", "BALL ES PELOTA.", n="recordar"),
      MC("SOFI SACA UNA MUÑECA. ¿QUÉ DICE?", ["DOLL", "BALL", "CAR"], "DOLL", "MUÑECA ES DOLL.", n="aplicar"),
      MC("TOMI JUEGA CON SU OSITO. ¿CÓMO SE DICE?", ["TEDDY", "CAR", "BALL"], "TEDDY", "OSITO ES TEDDY.", n="aplicar")],
"2": [MC("TOMI TIENE UN AUTO. ¿QUÉ DICE?", ["I HAVE A CAR", "I HAVE A DOLL", "I AM SIX"], "I HAVE A CAR", "TIENE UN CAR.", n="aplicar"),
      ORD("ORDENÁ LA FRASE.", ["HAVE", "BALL", "I", "A"], ["I", "HAVE", "A", "BALL"], "I HAVE A BALL.", n="aplicar")],
"3": [MC("UN OSO ENORME ES…", ["BIG", "SMALL", "RED"], "BIG", "ENORME ES BIG.", n="aplicar"),
      MC("TOMI DICE QUE UN AUTITO CHIQUITO ES BIG. ¿QUÉ ESTÁ MAL?", ["ES SMALL", "ESTÁ BIEN", "ES BLUE"], "ES SMALL", "CHIQUITO ES SMALL.", n="error")],
"4": [MC("SOFI ESCONDE UNA PELOTA. IS IT A BALL?", ["YES, IT IS", "NO, IT ISN'T", "GOODBYE"], "YES, IT IS", "SÍ, ES UNA PELOTA.", n="aplicar"),
      MC("SOFI ESCONDE UNA MUÑECA. IS IT A CAR?", ["NO, IT ISN'T", "YES, IT IS", "I HAVE A CAR"], "NO, IT ISN'T", "NO ES UN AUTO.", n="aplicar")],
"5": [MC("RELÁMPAGO. AUTO EN INGLÉS ES…", ["CAR", "BALL", "DOLL"], "CAR", "CAR.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. GRANDE EN INGLÉS ES…", ["BIG", "SMALL", "YES"], "BIG", "BIG.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. TENÉS UNA MUÑECA. DECÍS I HAVE A…", ["DOLL", "BALL", "CAR"], "DOLL", "DOLL.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. UN AUTITO CHIQUITO ES…", ["SMALL", "BIG", "NO"], "SMALL", "SMALL.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("MUÑECA EN INGLÉS ES…", ["DOLL", "BALL", "TEDDY"], "DOLL", "DOLL ES MUÑECA.", n="recordar")],
 [1, SA("SOFI SACA UNA PELOTA. ESCRIBÍ PELOTA EN INGLÉS.", acepta("BALL"), "BALL.", n="aplicar")],
 [1, MC("TOMI SACA UN AUTO Y DICE DOLL. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR CAR", "ESTÁ BIEN", "DEBE DECIR BALL"], "DEBE DECIR CAR", "AUTO ES CAR.", n="error")],
 [2, MC("I HAVE A BALL QUIERE DECIR…", ["TENGO UNA PELOTA", "ES UNA PELOTA", "QUIERO UNA PELOTA"], "TENGO UNA PELOTA", "HAVE ES TENER.", n="recordar")],
 [2, SA("SOFI TIENE UN OSITO. COMPLETÁ: I HAVE A…", acepta("TEDDY", "TEDDY BEAR"), "TEDDY.", n="aplicar")],
 [2, MC("LEO TIENE UN AUTO. ¿QUÉ DICE?", ["I HAVE A CAR", "I HAVE A DOLL", "IT IS A BALL"], "I HAVE A CAR", "TIENE UN CAR.", n="aplicar")],
 [3, MC("CHICO EN INGLÉS ES…", ["SMALL", "BIG", "BALL"], "SMALL", "SMALL ES CHICO.", n="recordar")],
 [3, SA("UNA PELOTA GIGANTE. ESCRIBÍ BIG O SMALL.", acepta("BIG"), "BIG.", n="aplicar")],
 [3, MC("UN OSITO CHIQUITO Y SOFI DICE A BIG TEDDY. ¿QUÉ ESTÁ MAL?", ["ES SMALL", "ESTÁ BIEN", "ES RED"], "ES SMALL", "CHIQUITO ES SMALL.", n="error")],
 [4, MC("IS IT A DOLL QUIERE DECIR…", ["¿ES UNA MUÑECA?", "TENGO UNA MUÑECA", "¿DÓNDE ESTÁ LA MUÑECA?"], "¿ES UNA MUÑECA?", "IS IT A = ¿ES UN?", n="recordar")],
 [4, MC("TOMI ESCONDE UN OSITO. IS IT A TEDDY?", ["YES, IT IS", "NO, IT ISN'T", "I HAVE A CAR"], "YES, IT IS", "SÍ, ES UN OSITO.", n="aplicar")],
 [4, MC("TOMI ESCONDE UN OSITO. IS IT A BALL?", ["NO, IT ISN'T", "YES, IT IS", "IT IS BIG"], "NO, IT ISN'T", "NO ES UNA PELOTA.", n="aplicar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 8, "estilo": "primeros",
     "practica": "Práctica general: Toys and Games", "examen_titulo": "Nivel jefe: Toys and Games",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
