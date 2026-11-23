# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 2 · Numbers 1 to 10. Genera mision-2.json.
Regla de primeros años. Metáfora: el tren de los números de Tomi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 one a five · 2 six a ten · 3 how old are you · 4 canciones y juegos con números."""
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
"objetivo": "Vas a contar del 1 al 5 en inglés.",
"vas_a_ver": ["ONE, TWO, THREE", "FOUR, FIVE", "Contar cosas"],
"secciones": [
 S(1, "Del 1 al 5", [
  D("Contar", "Decir los números en orden: 1, 2, 3…"),
  P("En inglés contamos: <b>ONE, TWO, THREE, FOUR, FIVE</b>."),
  IMG("Del 1 al 5", "Cada número en inglés.", FG.tiras(["1 = ONE", "2 = TWO", "3 = THREE", "4 = FOUR", "5 = FIVE"], numeros=False, cols=1)),
 ]),
 S(1, "Con los dedos", [
  P("Levantá un dedo por cada número. ¡Con una mano llegás a <b>FIVE</b>!"),
  IMG("Mi mano", "Cinco dedos.", FG.tiras(["UNA MANO = FIVE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cosas de Tomi. Las vas a usar en la carpeta."),
  IMG("Las cosas de Tomi", "¿Cuántas hay?", FG.tiras(["3 PELOTAS", "5 LÁPICES", "2 AUTITOS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi cuenta", "planteo": "Tomi tiene pelotas.", "pasos": ["Señala cada una.", "Dice: ONE, TWO, THREE.", "¡Tiene THREE pelotas!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "ONE, TWO, ___, FOUR.", "pasos": ["ONE, TWO, ___, FOUR."]},
"ejemplo_solo": {"titulo": "Tus dedos", "planteo": "Contá tus dedos de una mano en inglés."},
"tip": {"titulo": "Un dedo por número", "texto": "Tocá cada cosa al contar."},
"ojo": ["TWO es el 2.", "FIVE es el 5."],
"resumen": [{"titulo": "ONE, TWO", "texto": "1 y 2."}, {"titulo": "THREE, FOUR", "texto": "3 y 4."}, {"titulo": "FIVE", "texto": "5."}],
"glosario": [{"palabra": "ONE", "significado": "Uno."}, {"palabra": "FIVE", "significado": "Cinco."}],
"carpeta": ["Tomi tiene 3 pelotas. ¿Cómo se dice?", "Tomi tiene 5 lápices. ¿Cómo se dice?", "Tomi cuenta: ONE, THREE, FOUR. ¿Qué falta?"],
"respuestas_carpeta": [acepta("THREE"), acepta("FIVE"), acepta("TWO", "FALTA TWO")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "THREE.", "solo": "ONE, TWO, THREE, FOUR, FIVE.", "carpeta": ["THREE.", "FIVE.", "FALTA TWO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar del 6 al 10 en inglés.",
"vas_a_ver": ["SIX, SEVEN, EIGHT", "NINE, TEN", "Contar hasta TEN"],
"secciones": [
 S(1, "Del 6 al 10", [
  D("Seguir contando", "Después del 5 vienen más números."),
  P("Seguimos: <b>SIX, SEVEN, EIGHT, NINE, TEN</b>."),
  IMG("Del 6 al 10", "Cada número en inglés.", FG.tiras(["6 = SIX", "7 = SEVEN", "8 = EIGHT", "9 = NINE", "10 = TEN"], numeros=False, cols=1)),
 ]),
 S(1, "Dos manos", [
  P("Con las dos manos llegás a <b>TEN</b>."),
  IMG("Mis manos", "Diez dedos.", FG.tiras(["DOS MANOS = TEN"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los globos del cumple. Los vas a usar en la carpeta."),
  IMG("El cumple", "¿Cuántos hay?", FG.tiras(["7 GLOBOS", "10 VELITAS", "8 REGALOS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi cuenta", "planteo": "Sofi tiene globos.", "pasos": ["Ya contó FIVE.", "Sigue: SIX, SEVEN.", "¡Tiene SEVEN globos!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "SIX, SEVEN, ___, NINE.", "pasos": ["SIX, SEVEN, ___, NINE."]},
"ejemplo_solo": {"titulo": "Tus dedos", "planteo": "Contá tus diez dedos en inglés."},
"tip": {"titulo": "Seguí contando", "texto": "Después de FIVE viene SIX."},
"ojo": ["EIGHT es el 8.", "TEN es el 10."],
"resumen": [{"titulo": "SIX, SEVEN", "texto": "6 y 7."}, {"titulo": "EIGHT, NINE", "texto": "8 y 9."}, {"titulo": "TEN", "texto": "10."}],
"glosario": [{"palabra": "SEVEN", "significado": "Siete."}, {"palabra": "TEN", "significado": "Diez."}],
"carpeta": ["Hay 7 globos. ¿Cómo se dice?", "Hay 10 velitas. ¿Cómo se dice?", "Sofi cuenta: SIX, SEVEN, NINE. ¿Qué falta?"],
"respuestas_carpeta": [acepta("SEVEN"), acepta("TEN"), acepta("EIGHT", "FALTA EIGHT")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "EIGHT.", "solo": "ONE a TEN.", "carpeta": ["SEVEN.", "TEN.", "FALTA EIGHT."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a decir cuántos años tenés en inglés.",
"vas_a_ver": ["La pregunta", "I AM SIX", "Los años de mis amigos"],
"secciones": [
 S(1, "¿Cuántos años tenés?", [
  D("Edad", "Los años que tenemos."),
  P("Para saber la edad preguntamos: <b>HOW OLD ARE YOU?</b>"),
  IMG("La pregunta", "Quiere decir: ¿cuántos años tenés?", FG.tiras(["HOW OLD ARE YOU?"], numeros=False, cols=1)),
 ]),
 S(1, "La respuesta", [
  P("Contestamos: <b>I AM</b> y el número."),
  IMG("La respuesta", "Quiere decir: tengo…", FG.tiras(["I AM SIX = TENGO 6", "I AM SEVEN = TENGO 7"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá a los chicos. Los vas a usar en la carpeta."),
  IMG("Los chicos", "¿Cuántos años tienen?", FG.tiras(["SOFI: 6 AÑOS", "TOMI: 7 AÑOS", "LEO: 5 AÑOS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi pregunta", "planteo": "Sofi conoce a Tomi.", "pasos": ["Sofi: HOW OLD ARE YOU?", "Tomi: I AM SEVEN.", "¡Tomi tiene 7!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "I AM ___ (6).", "pasos": ["I AM ___."]},
"ejemplo_solo": {"titulo": "Tu edad", "planteo": "Decí en voz alta: I AM y tus años."},
"tip": {"titulo": "Mostrá los dedos", "texto": "Mostrá tus años con los dedos."},
"ojo": ["OLD es para la edad.", "I AM es yo tengo."],
"resumen": [{"titulo": "Pregunta", "texto": "HOW OLD ARE YOU?"}, {"titulo": "Respuesta", "texto": "I AM SIX."}, {"titulo": "Edad", "texto": "Los años."}],
"glosario": [{"palabra": "OLD", "significado": "Para la edad."}, {"palabra": "I AM", "significado": "Yo tengo."}],
"carpeta": ["Sofi tiene 6. Completá: I AM ___.", "Tomi tiene 7. Completá: I AM ___.", "Leo tiene 5 y dice I AM SIX. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("SIX", "I AM SIX"), acepta("SEVEN", "I AM SEVEN"), acepta("FIVE", "I AM FIVE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "SIX.", "solo": "Tu edad.", "carpeta": ["SIX.", "SEVEN.", "I AM FIVE."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a jugar y cantar con los números en inglés.",
"vas_a_ver": ["Una canción para contar", "Juegos de números", "Sumar jugando"],
"secciones": [
 S(1, "Cantar y contar", [
  D("Canción", "Música con palabras para cantar."),
  P("Cantamos los números en orden, del <b>ONE</b> al <b>TEN</b>."),
  IMG("La canción", "Contamos cantando.", FG.tiras(["ONE, TWO, THREE, FOUR, FIVE", "SIX, SEVEN, EIGHT, NINE, TEN"], numeros=False, cols=1)),
 ]),
 S(1, "Juntar", [
  P("También jugamos a <b>juntar</b>. TWO y THREE son FIVE."),
  IMG("Juntamos", "Dos grupos.", FG.tiras(["TWO + THREE = FIVE", "FOUR + FOUR = EIGHT"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el juego de Tomi. Lo vas a usar en la carpeta."),
  IMG("El juego", "Juntá y contá.", FG.tiras(["1 PELOTA + 1 PELOTA", "3 AUTOS + 2 AUTOS", "5 + 5"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Juntar autos", "planteo": "Tomi tiene 3 autos y 2 más.", "pasos": ["Junta los autos.", "Cuenta: ONE… FIVE.", "¡Son FIVE!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "ONE + ONE = ___", "pasos": ["ONE + ONE = ___"]},
"ejemplo_solo": {"titulo": "A cantar", "planteo": "Cantá los números del ONE al TEN con tu familia."},
"tip": {"titulo": "Aplaudí", "texto": "Da un aplauso por cada número."},
"ojo": ["Primero contamos.", "Después juntamos."],
"resumen": [{"titulo": "Canción", "texto": "Del ONE al TEN."}, {"titulo": "Juntar", "texto": "Sumar jugando."}, {"titulo": "Contar", "texto": "En orden."}],
"glosario": [{"palabra": "Juntar", "significado": "Poner todo junto."}, {"palabra": "TEN", "significado": "Diez."}],
"carpeta": ["1 pelota y 1 pelota. ¿Cuántas en inglés?", "3 autos y 2 autos. ¿Cuántos en inglés?", "Tomi dice: 5 y 5 son NINE. ¿Qué está mal?"],
"respuestas_carpeta": [acepta("TWO"), acepta("FIVE"), acepta("TEN", "SON TEN", "ES TEN")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "TWO.", "solo": "La canción.", "carpeta": ["TWO.", "FIVE.", "SON TEN."]},
}

ACT = {
"1": [MC("¿CÓMO SE DICE 3 EN INGLÉS?", ["THREE", "TWO", "FIVE"], "THREE", "3 ES THREE.", n="recordar"),
      MC("TOMI TIENE 4 PELOTAS. ¿CUÁNTAS TIENE?", ["FOUR", "FIVE", "ONE"], "FOUR", "4 ES FOUR.", n="aplicar"),
      MC("COMPLETÁ: ONE, TWO, ___.", ["THREE", "FIVE", "FOUR"], "THREE", "DESPUÉS DE TWO VIENE THREE.", n="aplicar")],
"2": [MC("¿CÓMO SE DICE 10 EN INGLÉS?", ["TEN", "SIX", "NINE"], "TEN", "10 ES TEN.", n="recordar"),
      MC("HAY 8 REGALOS. ¿CUÁNTOS HAY?", ["EIGHT", "SEVEN", "SIX"], "EIGHT", "8 ES EIGHT.", n="aplicar"),
      MC("SOFI CUENTA SIX, EIGHT. ¿QUÉ SALTEÓ?", ["SEVEN", "NINE", "TEN"], "SEVEN", "FALTA SEVEN.", n="error")],
"3": [MC("SOFI TIENE 6 AÑOS. ¿QUÉ DICE?", ["I AM SIX", "I AM TEN", "I AM SAD"], "I AM SIX", "TIENE SIX.", n="aplicar"),
      MC("TOMI TE PREGUNTA HOW OLD ARE YOU. ¿QUÉ QUIERE SABER?", ["TU EDAD", "TU NOMBRE", "TU COLOR"], "TU EDAD", "OLD ES PARA LA EDAD.", n="aplicar")],
"4": [MC("TWO + TWO = …", ["FOUR", "THREE", "FIVE"], "FOUR", "2 + 2 = 4.", n="aplicar"),
      ORD("ORDENÁ LOS NÚMEROS.", ["THREE", "ONE", "TWO"], ["ONE", "TWO", "THREE"], "1, 2, 3.", n="aplicar")],
"5": [MC("RELÁMPAGO. 1 EN INGLÉS ES…", ["ONE", "TWO", "TEN"], "ONE", "ONE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. 9 EN INGLÉS ES…", ["NINE", "FIVE", "SIX"], "NINE", "NINE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. TENÉS 5 DEDOS EN UNA MANO. DECÍS…", ["FIVE", "FOUR", "TEN"], "FIVE", "FIVE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. TRES + UNO = …", ["FOUR", "THREE", "SIX"], "FOUR", "FOUR.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("2 EN INGLÉS ES…", ["TWO", "THREE", "TEN"], "TWO", "2 ES TWO.", n="recordar")],
 [1, SA("TOMI TIENE 5 LÁPICES. ESCRIBÍ EL NÚMERO EN INGLÉS.", acepta("FIVE"), "FIVE.", n="aplicar")],
 [1, MC("TOMI CUENTA ONE, TWO, FOUR. ¿QUÉ FALTA?", ["THREE", "FIVE", "ONE"], "THREE", "1, 2, 3, 4.", n="error")],
 [2, MC("7 EN INGLÉS ES…", ["SEVEN", "SIX", "EIGHT"], "SEVEN", "7 ES SEVEN.", n="recordar")],
 [2, SA("HAY 10 VELITAS. ESCRIBÍ EL NÚMERO EN INGLÉS.", acepta("TEN"), "TEN.", n="aplicar")],
 [2, ORD("ORDENÁ LOS NÚMEROS.", ["NINE", "SIX", "EIGHT", "SEVEN"], ["SIX", "SEVEN", "EIGHT", "NINE"], "6, 7, 8, 9.", n="aplicar")],
 [3, MC("HOW OLD ARE YOU QUIERE DECIR…", ["¿CUÁNTOS AÑOS TENÉS?", "¿CÓMO TE LLAMÁS?", "¿CÓMO ESTÁS?"], "¿CUÁNTOS AÑOS TENÉS?", "OLD ES PARA LA EDAD.", n="recordar")],
 [3, MC("TOMI TIENE 7 AÑOS. ¿QUÉ DICE?", ["I AM SEVEN", "I AM SIX", "I AM HAPPY"], "I AM SEVEN", "TIENE SEVEN.", n="aplicar")],
 [3, MC("LEO TIENE 5 Y DICE I AM TEN. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR FIVE", "ESTÁ BIEN", "DEBE DECIR HELLO"], "DEBE DECIR FIVE", "TIENE FIVE.", n="error")],
 [4, MC("ONE + ONE = …", ["TWO", "ONE", "THREE"], "TWO", "1 + 1 = 2.", n="aplicar")],
 [4, MC("FIVE + FIVE = …", ["TEN", "NINE", "FIVE"], "TEN", "5 + 5 = 10.", n="aplicar")],
 [4, MC("LA CANCIÓN EMPIEZA EN ONE. ¿EN QUÉ TERMINA?", ["TEN", "FIVE", "SIX"], "TEN", "DEL ONE AL TEN.", n="recordar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: Numbers", "examen_titulo": "Nivel jefe: Numbers",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
