# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 1 · Hello! Greetings and Names. Genera mision-1.json.
Regla de primeros años. Metáfora: los títeres amigos de Sofi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 hello y goodbye · 2 what is your name · 3 how are you, happy y sad · 4 nice to meet you con títeres."""
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
"objetivo": "Vas a saludar y despedirte en inglés.",
"vas_a_ver": ["Hello: hola", "Goodbye: chau", "Cuándo usar cada uno"],
"secciones": [
 S(1, "Saludar", [
  D("Saludo", "Lo que decimos cuando llegamos o nos vamos."),
  P("En inglés, para decir hola decimos <b>HELLO</b> o <b>HI</b>."),
  IMG("Hola", "Así saludamos.", FG.tiras(["HELLO = HOLA", "HI = HOLA"], numeros=False, cols=2)),
 ]),
 S(1, "Despedirse", [
  P("Para decir chau decimos <b>GOODBYE</b> o <b>BYE</b>."),
  IMG("Chau", "Así nos despedimos.", FG.tiras(["GOODBYE = CHAU", "BYE = CHAU"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que hace Sofi. Lo vas a usar en la carpeta."),
  IMG("El día de Sofi", "¿Llega o se va?", FG.tiras(["LLEGA A LA ESCUELA", "SE VA A SU CASA", "VE A SU AMIGO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi llega", "planteo": "Sofi entra al aula.", "pasos": ["Ve a la maestra.", "Mueve la mano.", "Dice: HELLO!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cuando me voy digo…", "pasos": ["___!"]},
"ejemplo_solo": {"titulo": "En casa", "planteo": "Saludá a tu familia en inglés: HELLO!"},
"tip": {"titulo": "Con la mano", "texto": "Mové la mano cuando saludás."},
"ojo": ["HELLO es para llegar.", "GOODBYE es para irse."],
"resumen": [{"titulo": "HELLO", "texto": "Hola."}, {"titulo": "HI", "texto": "Hola."}, {"titulo": "GOODBYE", "texto": "Chau."}],
"glosario": [{"palabra": "HELLO", "significado": "Hola."}, {"palabra": "GOODBYE", "significado": "Chau."}],
"carpeta": ["Sofi llega a la escuela. ¿Qué dice?", "Sofi se va a su casa. ¿Qué dice?", "Sofi ve a su amigo. ¿Qué dice?"],
"respuestas_carpeta": [acepta("HELLO", "HI", "HELLO!", "HI!"), acepta("GOODBYE", "BYE", "GOODBYE!", "BYE!", "GOOD BYE"), acepta("HELLO", "HI", "HELLO!", "HI!")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "GOODBYE!", "solo": "Tu saludo.", "carpeta": ["HELLO!", "GOODBYE!", "HI!"]},
}

N2 = {**ESTILO,
"objetivo": "Vas a decir tu nombre en inglés.",
"vas_a_ver": ["La pregunta", "La respuesta", "Decir mi nombre"],
"secciones": [
 S(1, "La pregunta", [
  D("Nombre", "Cómo nos llamamos."),
  P("Para saber el nombre de alguien preguntamos: <b>WHAT IS YOUR NAME?</b>"),
  IMG("La pregunta", "Quiere decir: ¿cómo te llamás?", FG.tiras(["WHAT IS YOUR NAME?"], numeros=False, cols=1)),
 ]),
 S(1, "La respuesta", [
  P("Contestamos: <b>MY NAME IS</b> y nuestro nombre."),
  IMG("La respuesta", "Quiere decir: me llamo…", FG.tiras(["MY NAME IS SOFI", "MY NAME IS TOMI"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá a los chicos. Los vas a usar en la carpeta."),
  IMG("Los chicos", "Sus nombres.", FG.tiras(["SOFI", "TOMI", "ANA"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi pregunta", "planteo": "Tomi conoce a Sofi.", "pasos": ["Tomi: WHAT IS YOUR NAME?", "Sofi: MY NAME IS SOFI.", "¡Ya se conocen!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "MY ___ IS TOMI.", "pasos": ["MY ___ IS TOMI."]},
"ejemplo_solo": {"titulo": "Tu nombre", "planteo": "Decí en voz alta: MY NAME IS y tu nombre."},
"tip": {"titulo": "Señalate", "texto": "Al decir MY, tocate el pecho."},
"ojo": ["YOUR es de vos.", "MY es mío."],
"resumen": [{"titulo": "Pregunta", "texto": "WHAT IS YOUR NAME?"}, {"titulo": "Respuesta", "texto": "MY NAME IS…"}, {"titulo": "NAME", "texto": "Nombre."}],
"glosario": [{"palabra": "NAME", "significado": "Nombre."}, {"palabra": "MY", "significado": "Mi."}],
"carpeta": ["Completá: MY NAME IS ___ (la nena).", "Completá: MY ___ IS TOMI.", "Tomi dice: MY NAME TOMI. ¿Qué falta?"],
"respuestas_carpeta": [acepta("SOFI", "MY NAME IS SOFI"), acepta("NAME"), acepta("IS", "FALTA IS", "MY NAME IS TOMI")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "NAME.", "solo": "Tu nombre en voz alta.", "carpeta": ["SOFI.", "NAME.", "FALTA IS."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a preguntar y decir cómo estás en inglés.",
"vas_a_ver": ["How are you?", "Happy: feliz", "Sad: triste"],
"secciones": [
 S(1, "¿Cómo estás?", [
  D("Emoción", "Lo que sentimos: alegría o tristeza."),
  P("Para preguntar cómo estás decimos: <b>HOW ARE YOU?</b>"),
  IMG("Contestamos", "Así me siento.", FG.tiras(["I AM FINE = ESTOY BIEN", "I AM HAPPY = ESTOY FELIZ", "I AM SAD = ESTOY TRISTE"], numeros=False, cols=1)),
 ]),
 S(1, "Caras", [
  P("<b>HAPPY</b> es una cara que sonríe. <b>SAD</b> es una cara que llora."),
  IMG("Caras", "Feliz y triste.", FG.tiras(["HAPPY = FELIZ", "SAD = TRISTE"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá a los chicos. Los vas a usar en la carpeta."),
  IMG("¿Cómo están?", "Mirá sus caras.", FG.tiras(["SOFI GANÓ UN PREMIO", "TOMI PERDIÓ SU PELOTA", "ANA ESTÁ BIEN"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi pregunta", "planteo": "Sofi ve a Tomi.", "pasos": ["Sofi: HOW ARE YOU?", "Tomi sonríe.", "Tomi: I AM HAPPY!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Una cara que llora está…", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu cara", "planteo": "Dibujá tu cara de hoy y escribí HAPPY o SAD."},
"tip": {"titulo": "Hacé la cara", "texto": "Sonreí al decir HAPPY."},
"ojo": ["HAPPY es feliz.", "SAD es triste."],
"resumen": [{"titulo": "HOW ARE YOU?", "texto": "¿Cómo estás?"}, {"titulo": "HAPPY", "texto": "Feliz."}, {"titulo": "SAD", "texto": "Triste."}],
"glosario": [{"palabra": "HAPPY", "significado": "Feliz."}, {"palabra": "SAD", "significado": "Triste."}],
"carpeta": ["Sofi ganó un premio. ¿HAPPY o SAD?", "Tomi perdió su pelota. ¿HAPPY o SAD?", "Ana dice: I AM HAPPY y llora. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("HAPPY"), acepta("SAD"), acepta("SAD", "I AM SAD")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "SAD.", "solo": "Tu cara.", "carpeta": ["HAPPY.", "SAD.", "I AM SAD."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a presentarte con títeres en inglés.",
"vas_a_ver": ["Nice to meet you", "Una charla completa", "Mi títere"],
"secciones": [
 S(1, "Mucho gusto", [
  D("Presentarse", "Decir quién soy a alguien nuevo."),
  P("Cuando conocemos a alguien decimos: <b>NICE TO MEET YOU!</b> Quiere decir: ¡mucho gusto!"),
  IMG("Mucho gusto", "Al conocer a alguien.", FG.tiras(["NICE TO MEET YOU!"], numeros=False, cols=1)),
 ]),
 S(1, "Una charla", [
  P("Juntamos todo en una <b>charla</b>."),
  IMG("La charla", "En orden.", FG.tiras(["HELLO!", "WHAT IS YOUR NAME?", "MY NAME IS LEO.", "NICE TO MEET YOU!", "GOODBYE!"], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los títeres. Los vas a usar en la carpeta."),
  IMG("Los títeres", "Leo y Mia.", FG.tiras(["LEO, EL PERRITO", "MIA, LA GATITA"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "Leo y Mia", "planteo": "Los títeres se conocen.", "pasos": ["Leo: HELLO! MY NAME IS LEO.", "Mia: MY NAME IS MIA.", "Los dos: NICE TO MEET YOU!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "NICE TO ___ YOU!", "pasos": ["NICE TO ___ YOU!"]},
"ejemplo_solo": {"titulo": "Tu títere", "planteo": "Hacé un títere con una media y presentalo en inglés."},
"tip": {"titulo": "Sonreí", "texto": "Al conocer a alguien, mirá y sonreí."},
"ojo": ["Primero saludamos.", "Al final decimos GOODBYE."],
"resumen": [{"titulo": "NICE TO MEET YOU", "texto": "Mucho gusto."}, {"titulo": "Charla", "texto": "Saludo, nombre y chau."}, {"titulo": "Títeres", "texto": "Para practicar."}],
"glosario": [{"palabra": "NICE TO MEET YOU", "significado": "Mucho gusto."}, {"palabra": "Títere", "significado": "Muñeco que se mueve con la mano."}],
"carpeta": ["Leo conoce a Mia. ¿Qué le dice?", "Mia quiere saber el nombre de Leo. ¿Qué pregunta?", "Mia dice GOODBYE al llegar. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("NICE TO MEET YOU", "NICE TO MEET YOU!", "HELLO", "HELLO!"), acepta("WHAT IS YOUR NAME?", "WHAT IS YOUR NAME", "WHATS YOUR NAME", "WHAT'S YOUR NAME?", "WHAT'S YOUR NAME"), acepta("HELLO", "HELLO!", "HI", "HI!")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "MEET.", "solo": "Tu títere.", "carpeta": ["NICE TO MEET YOU!", "WHAT IS YOUR NAME?", "HELLO!"]},
}

ACT = {
"1": [MC("PARA DECIR HOLA EN INGLÉS DECIMOS…", ["HELLO", "GOODBYE", "SAD"], "HELLO", "HELLO ES HOLA.", n="recordar"),
      MC("SOFI SE VA A SU CASA. ¿QUÉ DICE?", ["GOODBYE", "HELLO", "HAPPY"], "GOODBYE", "AL IRSE: GOODBYE.", n="aplicar")],
"2": [MC("COMPLETÁ: MY ___ IS TOMI.", ["NAME", "HELLO", "SAD"], "NAME", "MY NAME IS TOMI.", n="aplicar"),
      MC("TOMI TE PREGUNTA WHAT IS YOUR NAME. ¿QUÉ CONTESTÁS?", ["MY NAME IS…", "GOODBYE", "I AM SAD"], "MY NAME IS…", "DECIMOS NUESTRO NOMBRE.", n="aplicar")],
"3": [MC("UNA CARA QUE SONRÍE ESTÁ…", ["HAPPY", "SAD", "GOODBYE"], "HAPPY", "HAPPY ES FELIZ.", n="aplicar"),
      MC("TOMI LLORA Y DICE I AM HAPPY. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR SAD", "ESTÁ BIEN", "DEBE DECIR HELLO"], "DEBE DECIR SAD", "SI LLORA, ESTÁ SAD.", n="error")],
"4": [MC("CONOCÉS A ALGUIEN NUEVO. ¿QUÉ DECÍS?", ["NICE TO MEET YOU", "I AM SAD", "GOODBYE"], "NICE TO MEET YOU", "QUIERE DECIR MUCHO GUSTO.", n="aplicar"),
      ORD("ORDENÁ LA CHARLA.", ["GOODBYE!", "HELLO!", "MY NAME IS LEO."], ["HELLO!", "MY NAME IS LEO.", "GOODBYE!"], "SALUDO, NOMBRE Y CHAU.", n="analizar")],
"5": [MC("RELÁMPAGO. HOLA EN INGLÉS ES…", ["HELLO", "BYE", "SAD"], "HELLO", "HELLO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. TRISTE EN INGLÉS ES…", ["SAD", "HAPPY", "NAME"], "SAD", "SAD.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. TE VAS DE LA ESCUELA. DECÍS…", ["GOODBYE", "HELLO", "HAPPY"], "GOODBYE", "GOODBYE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. COMPLETÁ: NICE TO ___ YOU.", ["MEET", "NAME", "SAD"], "MEET", "NICE TO MEET YOU.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("CHAU EN INGLÉS ES…", ["GOODBYE", "HELLO", "HI"], "GOODBYE", "GOODBYE ES CHAU.", n="recordar")],
 [1, MC("SOFI LLEGA A LA ESCUELA Y DICE GOODBYE. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR HELLO", "ESTÁ BIEN", "DEBE DECIR SAD"], "DEBE DECIR HELLO", "AL LLEGAR: HELLO.", n="error")],
 [1, SA("VES A TU AMIGO EN LA PLAZA. ESCRIBÍ QUÉ LE DECÍS.", acepta("HI", "HELLO", "HI!", "HELLO!"), "HI O HELLO.", n="aplicar")],
 [2, MC("WHAT IS YOUR NAME QUIERE DECIR…", ["¿CÓMO TE LLAMÁS?", "¿CÓMO ESTÁS?", "CHAU"], "¿CÓMO TE LLAMÁS?", "NAME ES NOMBRE.", n="recordar")],
 [2, ORD("ORDENÁ LA FRASE.", ["IS", "MY", "NAME", "SOFI"], ["MY", "NAME", "IS", "SOFI"], "MY NAME IS SOFI.", n="aplicar")],
 [2, MC("TOMI DICE MY NAME TOMI. ¿QUÉ FALTA?", ["IS", "HELLO", "SAD"], "IS", "MY NAME IS TOMI.", n="error")],
 [3, MC("HOW ARE YOU QUIERE DECIR…", ["¿CÓMO ESTÁS?", "¿CÓMO TE LLAMÁS?", "HOLA"], "¿CÓMO ESTÁS?", "HOW ARE YOU.", n="recordar")],
 [3, MC("SOFI GANÓ UN PREMIO. ¿CÓMO ESTÁ?", ["HAPPY", "SAD", "GOODBYE"], "HAPPY", "ESTÁ FELIZ.", n="aplicar")],
 [3, SA("TOMI PERDIÓ SU PELOTA. ESCRIBÍ CÓMO ESTÁ: HAPPY O SAD.", acepta("SAD", "I AM SAD", "HE IS SAD"), "ESTÁ SAD.", n="aplicar")],
 [4, MC("NICE TO MEET YOU QUIERE DECIR…", ["MUCHO GUSTO", "CHAU", "ESTOY TRISTE"], "MUCHO GUSTO", "AL CONOCER A ALGUIEN.", n="recordar")],
 [4, ORD("ORDENÁ LA CHARLA DE LOS TÍTERES.", ["NICE TO MEET YOU!", "HELLO!", "GOODBYE!"], ["HELLO!", "NICE TO MEET YOU!", "GOODBYE!"], "SALUDO, GUSTO Y CHAU.", n="analizar")],
 [4, MC("LEO DICE SU NOMBRE. ¿QUÉ DICE?", ["MY NAME IS LEO", "I AM SAD", "GOODBYE"], "MY NAME IS LEO", "ASÍ DICE SU NOMBRE.", n="aplicar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: Hello!", "examen_titulo": "Nivel jefe: Hello!",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
