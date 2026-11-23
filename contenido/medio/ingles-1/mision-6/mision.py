# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 6 · My Body. Genera mision-6.json.
Regla de primeros años. Metáfora: las canciones de Tomi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 head, shoulders, knees, toes · 2 eyes, nose, mouth, ears · 3 touch your nose · 4 hands and feet."""
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
"objetivo": "Vas a nombrar partes del cuerpo en inglés.",
"vas_a_ver": ["HEAD y SHOULDERS", "KNEES y TOES", "Tocar y decir"],
"secciones": [
 S(1, "Arriba", [
  D("Cuerpo", "Todo lo que somos: cabeza, brazos, piernas…"),
  P("Cabeza es <b>HEAD</b> y hombros es <b>SHOULDERS</b>."),
  IMG("Arriba", "En inglés.", FG.tiras(["CABEZA = HEAD", "HOMBROS = SHOULDERS"], numeros=False, cols=1)),
 ]),
 S(1, "Abajo", [
  P("Rodillas es <b>KNEES</b> y dedos del pie es <b>TOES</b>."),
  IMG("Abajo", "En inglés.", FG.tiras(["RODILLAS = KNEES", "DEDOS DEL PIE = TOES"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que toca Tomi. Lo vas a usar en la carpeta."),
  IMG("Tomi toca", "¿Qué parte es?", FG.tiras(["SU CABEZA", "SUS RODILLAS", "SUS HOMBROS"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi juega", "planteo": "Tomi se toca la cabeza.", "pasos": ["Pone las manos arriba.", "Dice: HEAD!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Rodillas en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu cuerpo", "planteo": "Tocá tu cabeza, hombros, rodillas y pies diciendo cada palabra."},
"tip": {"titulo": "De arriba a abajo", "texto": "Empezá por HEAD y bajá hasta TOES."},
"ojo": ["HEAD es cabeza.", "TOES son los dedos del pie."],
"resumen": [{"titulo": "HEAD", "texto": "Cabeza."}, {"titulo": "SHOULDERS", "texto": "Hombros."}, {"titulo": "KNEES / TOES", "texto": "Rodillas y dedos del pie."}],
"glosario": [{"palabra": "HEAD", "significado": "Cabeza."}, {"palabra": "KNEES", "significado": "Rodillas."}],
"carpeta": ["Tomi se toca la cabeza. ¿Cómo se dice?", "Tomi se toca las rodillas. ¿Cómo se dice?", "Tomi se toca los hombros y dice TOES. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("HEAD"), acepta("KNEES", "KNEE"), acepta("SHOULDERS", "SHOULDER")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "KNEES.", "solo": "Tu juego.", "carpeta": ["HEAD.", "KNEES.", "SHOULDERS."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a nombrar las partes de la cara en inglés.",
"vas_a_ver": ["EYES y EARS", "NOSE y MOUTH", "Para qué sirven"],
"secciones": [
 S(1, "Mi cara", [
  D("Cara", "La parte de adelante de la cabeza."),
  P("En la cara tenemos <b>EYES</b>, <b>NOSE</b>, <b>MOUTH</b> y <b>EARS</b>."),
  IMG("Mi cara", "En inglés.", FG.tiras(["OJOS = EYES", "NARIZ = NOSE", "BOCA = MOUTH", "OREJAS = EARS"], numeros=False, cols=1)),
 ]),
 S(1, "Para qué sirven", [
  P("Con los <b>EYES</b> vemos. Con las <b>EARS</b> oímos."),
  IMG("Sirven para", "Cada parte hace algo.", FG.tiras(["EYES: VER", "EARS: OÍR", "NOSE: OLER", "MOUTH: COMER Y HABLAR"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que hace Sofi. Lo vas a usar en la carpeta."),
  IMG("Sofi", "¿Qué usa?", FG.tiras(["MIRA UNA FLOR", "HUELE UNA FLOR", "ESCUCHA MÚSICA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi come", "planteo": "Sofi come una manzana.", "pasos": ["Usa la boca.", "Dice: MOUTH!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Nariz en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu cara", "planteo": "Dibujá tu cara y escribí EYES, NOSE, MOUTH y EARS."},
"tip": {"titulo": "Señalá", "texto": "Señalá cada parte de tu cara."},
"ojo": ["EYES son los ojos.", "EARS son las orejas."],
"resumen": [{"titulo": "EYES", "texto": "Ojos."}, {"titulo": "NOSE", "texto": "Nariz."}, {"titulo": "MOUTH / EARS", "texto": "Boca y orejas."}],
"glosario": [{"palabra": "NOSE", "significado": "Nariz."}, {"palabra": "MOUTH", "significado": "Boca."}],
"carpeta": ["Sofi mira una flor. ¿Qué usa?", "Sofi huele una flor. ¿Qué usa?", "Sofi escucha música y dice EYES. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("EYES", "EYE"), acepta("NOSE"), acepta("EARS", "EAR")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "NOSE.", "solo": "Tu cara.", "carpeta": ["EYES.", "NOSE.", "EARS."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a seguir órdenes con tu cuerpo en inglés.",
"vas_a_ver": ["TOUCH: tocá", "TOUCH YOUR NOSE", "Jugar a escuchar"],
"secciones": [
 S(1, "Tocar", [
  D("Orden", "Algo que nos piden hacer."),
  P("<b>TOUCH</b> es tocar. <b>TOUCH YOUR NOSE</b> es tocá tu nariz."),
  IMG("Tocar", "Órdenes.", FG.tiras(["TOUCH YOUR NOSE", "TOUCH YOUR HEAD", "TOUCH YOUR EARS"], numeros=False, cols=1)),
 ]),
 S(1, "A jugar", [
  P("Uno dice la orden y los demás la hacen. ¡Hay que <b>escuchar</b> bien!"),
  IMG("El juego", "Escuchar y hacer.", FG.tiras(["ESCUCHO", "TOCO", "¡MUY BIEN!"], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que hace Tomi. Lo vas a usar en la carpeta."),
  IMG("Tomi juega", "¿Qué orden escuchó?", FG.tiras(["SE TOCA LA NARIZ", "SE TOCA LA CABEZA", "SE TOCA LAS OREJAS"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi juega", "planteo": "La maestra dice: TOUCH YOUR HEAD!", "pasos": ["Sofi escucha.", "Se toca la cabeza.", "¡Lo hizo bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "TOUCH YOUR ___ (nariz).", "pasos": ["TOUCH YOUR ___."]},
"ejemplo_solo": {"titulo": "A jugar", "planteo": "Jugá con tu familia: decí TOUCH YOUR… y que lo hagan."},
"tip": {"titulo": "Escuchá", "texto": "Esperá a escuchar la parte del cuerpo."},
"ojo": ["TOUCH es tocar.", "YOUR es tu."],
"resumen": [{"titulo": "TOUCH", "texto": "Tocar."}, {"titulo": "YOUR", "texto": "Tu."}, {"titulo": "Juego", "texto": "Escuchar y hacer."}],
"glosario": [{"palabra": "TOUCH", "significado": "Tocar."}, {"palabra": "YOUR", "significado": "Tu."}],
"carpeta": ["Tomi se toca la nariz. ¿Qué orden escuchó?", "Tomi se toca la cabeza. ¿Qué orden escuchó?", "La orden es TOUCH YOUR EARS y Tomi se toca la nariz. ¿Qué debía tocar?"],
"respuestas_carpeta": [acepta("TOUCH YOUR NOSE"), acepta("TOUCH YOUR HEAD"), acepta("LAS OREJAS", "OREJAS", "EARS", "SUS OREJAS")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "NOSE.", "solo": "Tu juego.", "carpeta": ["TOUCH YOUR NOSE.", "TOUCH YOUR HEAD.", "LAS OREJAS."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a moverte con canciones en inglés.",
"vas_a_ver": ["HANDS y FEET", "CLAP y STAMP", "Bailar y cantar"],
"secciones": [
 S(1, "Manos y pies", [
  D("Movimiento", "Lo que hacemos con el cuerpo: saltar, aplaudir."),
  P("Manos es <b>HANDS</b> y pies es <b>FEET</b>."),
  IMG("Manos y pies", "En inglés.", FG.tiras(["MANOS = HANDS", "PIES = FEET"], numeros=False, cols=1)),
 ]),
 S(1, "A moverse", [
  P("<b>CLAP YOUR HANDS</b> es aplaudir. <b>STAMP YOUR FEET</b> es zapatear."),
  IMG("Movimientos", "Con canciones.", FG.tiras(["CLAP YOUR HANDS = APLAUDÍ", "STAMP YOUR FEET = ZAPATEÁ", "JUMP = SALTÁ"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá cómo baila Sofi. Lo vas a usar en la carpeta."),
  IMG("Sofi baila", "¿Qué hace?", FG.tiras(["APLAUDE", "ZAPATEA", "SALTA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La canción", "planteo": "Suena la música.", "pasos": ["Dice: CLAP YOUR HANDS!", "Sofi aplaude.", "¡Qué lindo!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "STAMP YOUR ___ (pies).", "pasos": ["STAMP YOUR ___."]},
"ejemplo_solo": {"titulo": "A bailar", "planteo": "Poné música y bailá: CLAP, STAMP y JUMP."},
"tip": {"titulo": "Con ritmo", "texto": "Seguí el ritmo de la música."},
"ojo": ["HANDS son las manos.", "FEET son los pies."],
"resumen": [{"titulo": "HANDS", "texto": "Manos."}, {"titulo": "FEET", "texto": "Pies."}, {"titulo": "CLAP / STAMP / JUMP", "texto": "Aplaudir, zapatear y saltar."}],
"glosario": [{"palabra": "CLAP", "significado": "Aplaudir."}, {"palabra": "FEET", "significado": "Pies."}],
"carpeta": ["Sofi aplaude. ¿Qué orden escuchó?", "Sofi zapatea. ¿Qué orden escuchó?", "La orden es JUMP y Sofi aplaude. ¿Qué debía hacer?"],
"respuestas_carpeta": [acepta("CLAP YOUR HANDS", "CLAP"), acepta("STAMP YOUR FEET", "STAMP"), acepta("SALTAR", "SALTA", "JUMP")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "FEET.", "solo": "Tu baile.", "carpeta": ["CLAP YOUR HANDS.", "STAMP YOUR FEET.", "SALTAR."]},
}

ACT = {
"1": [MC("CABEZA EN INGLÉS ES…", ["HEAD", "KNEES", "TOES"], "HEAD", "HEAD ES CABEZA.", n="recordar"),
      MC("TOMI SE TOCA LAS RODILLAS. ¿QUÉ DICE?", ["KNEES", "HEAD", "SHOULDERS"], "KNEES", "RODILLAS ES KNEES.", n="aplicar"),
      MC("TOMI SE TOCA LOS DEDOS DEL PIE. ¿QUÉ DICE?", ["TOES", "HEAD", "KNEES"], "TOES", "DEDOS DEL PIE ES TOES.", n="aplicar")],
"2": [MC("SOFI MIRA UNA FLOR. ¿QUÉ USA?", ["EYES", "EARS", "MOUTH"], "EYES", "CON LOS EYES VEMOS.", n="aplicar"),
      MC("SOFI COME UNA MANZANA. ¿QUÉ USA?", ["MOUTH", "NOSE", "EARS"], "MOUTH", "CON LA MOUTH COMEMOS.", n="aplicar")],
"3": [MC("LA ORDEN ES TOUCH YOUR NOSE. ¿QUÉ TOCÁS?", ["LA NARIZ", "LA CABEZA", "LOS PIES"], "LA NARIZ", "NOSE ES NARIZ.", n="aplicar"),
      MC("LA ORDEN ES TOUCH YOUR HEAD Y TOMI SE TOCA LA BOCA. ¿QUÉ ESTÁ MAL?", ["DEBÍA TOCAR LA CABEZA", "ESTÁ BIEN", "DEBÍA SALTAR"], "DEBÍA TOCAR LA CABEZA", "HEAD ES CABEZA.", n="error")],
"4": [MC("CLAP YOUR HANDS QUIERE DECIR…", ["APLAUDÍ", "SALTÁ", "SENTATE"], "APLAUDÍ", "CLAP ES APLAUDIR.", n="aplicar"),
      MC("LA CANCIÓN DICE STAMP YOUR FEET. ¿QUÉ HACÉS?", ["ZAPATEO", "APLAUDO", "ME SIENTO"], "ZAPATEO", "STAMP ES ZAPATEAR.", n="aplicar")],
"5": [MC("RELÁMPAGO. PIES EN INGLÉS ES…", ["FEET", "HANDS", "HEAD"], "FEET", "FEET.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. NARIZ EN INGLÉS ES…", ["NOSE", "EYES", "EARS"], "NOSE", "NOSE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ESCUCHÁS MÚSICA CON LAS…", ["EARS", "EYES", "TOES"], "EARS", "EARS.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. JUMP ES…", ["SALTAR", "APLAUDIR", "TOCAR"], "SALTAR", "JUMP.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("HOMBROS EN INGLÉS ES…", ["SHOULDERS", "KNEES", "TOES"], "SHOULDERS", "SHOULDERS ES HOMBROS.", n="recordar")],
 [1, SA("TOMI SE TOCA LA CABEZA. ESCRIBÍ CABEZA EN INGLÉS.", acepta("HEAD"), "HEAD.", n="aplicar")],
 [1, MC("TOMI SE TOCA LAS RODILLAS Y DICE HEAD. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR KNEES", "ESTÁ BIEN", "DEBE DECIR TOES"], "DEBE DECIR KNEES", "RODILLAS ES KNEES.", n="error")],
 [2, MC("BOCA EN INGLÉS ES…", ["MOUTH", "NOSE", "EARS"], "MOUTH", "MOUTH ES BOCA.", n="recordar")],
 [2, SA("SOFI HUELE UNA FLOR. ESCRIBÍ NARIZ EN INGLÉS.", acepta("NOSE"), "NOSE.", n="aplicar")],
 [2, MC("SOFI ESCUCHA MÚSICA. ¿QUÉ USA?", ["EARS", "EYES", "MOUTH"], "EARS", "CON LAS EARS OÍMOS.", n="aplicar")],
 [3, MC("TOUCH QUIERE DECIR…", ["TOCAR", "SALTAR", "MIRAR"], "TOCAR", "TOUCH ES TOCAR.", n="recordar")],
 [3, SA("TOMI SE TOCA LA NARIZ. ESCRIBÍ LA ORDEN: TOUCH YOUR…", acepta("NOSE", "TOUCH YOUR NOSE"), "NOSE.", n="aplicar")],
 [3, MC("LA ORDEN ES TOUCH YOUR EARS Y SOFI SE TOCA LOS OJOS. ¿QUÉ DEBÍA TOCAR?", ["LAS OREJAS", "LA NARIZ", "LA BOCA"], "LAS OREJAS", "EARS SON LAS OREJAS.", n="error")],
 [4, MC("MANOS EN INGLÉS ES…", ["HANDS", "FEET", "TOES"], "HANDS", "HANDS ES MANOS.", n="recordar")],
 [4, MC("LA CANCIÓN DICE JUMP. ¿QUÉ HACÉS?", ["SALTO", "APLAUDO", "ME SIENTO"], "SALTO", "JUMP ES SALTAR.", n="aplicar")],
 [4, MC("PARA ZAPATEAR USAMOS LOS…", ["FEET", "HANDS", "EARS"], "FEET", "ZAPATEAMOS CON LOS PIES.", n="aplicar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: My Body", "examen_titulo": "Nivel jefe: My Body",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
