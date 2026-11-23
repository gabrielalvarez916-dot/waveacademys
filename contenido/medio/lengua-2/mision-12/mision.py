# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 12 · Fábulas de Esopo y Samaniego. Genera mision-12.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Fábulas de trabajo (dominio público, contadas con palabras simples, sin copiar versos): «La zorra y las uvas» y «La liebre y la tortuga».
Metáfora: el cuaderno viajero de Sofi (hoy pega dos fábulas).
Niveles: 1 La zorra y las uvas · 2 La liebre y la tortuga · 3 qué enseña cada fábula · 4 escribir una moraleja."""
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
"objetivo": "Vas a leer la fábula La zorra y las uvas.",
"vas_a_ver": ["Qué es una fábula", "Lo que pasa", "La zorra y su excusa"],
"secciones": [
 S(1, "Una fábula", [
  D("Fábula", "Cuento corto con <b>animales</b> que deja una <b>enseñanza</b>."),
  P("Las escribieron <b>Esopo</b>, hace muchísimo, y <b>Samaniego</b>, en España."),
  IMG("Los personajes", "Una zorra y unas uvas.", FG.objetos([("zorra", "LA ZORRA"), ("uvas", "LAS UVAS")])),
 ]),
 S(1, "Lo que pasa", [
  IMG("La zorra y las uvas", "La fábula en cuatro partes.", FG.tiras(["UNA ZORRA TENÍA HAMBRE.", "VIO UVAS MUY ALTAS.", "SALTÓ Y SALTÓ, PERO NO LLEGÓ.", "DIJO: ESTÁN VERDES. Y SE FUE."], numeros=True)),
  P("La zorra dice que las uvas están verdes."),
  P("¡Pero es una <b>excusa</b>! No pudo alcanzarlas."),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tiras. Las vas a usar en la carpeta."),
  IMG("Tiras desordenadas", "¿Qué pasó primero?", FG.tiras(["DIJO: ESTÁN VERDES.", "VIO UVAS MUY ALTAS.", "SALTÓ Y NO LLEGÓ."], numeros=False)),
 ]),
],
"ejemplo_completo": {"titulo": "Personajes", "planteo": "¿Quiénes están en la fábula?", "pasos": ["Hay una zorra.", "Hay unas uvas.", "La zorra es la protagonista."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La zorra quería comer…", "pasos": ["La zorra quería comer ___ ."]},
"ejemplo_solo": {"titulo": "Contala", "planteo": "Contale la fábula a alguien de tu casa."},
"tip": {"titulo": "Animales que hablan", "texto": "En las fábulas los animales hablan y piensan."},
"ojo": ["Las uvas no estaban verdes.", "La zorra puso una excusa."],
"resumen": [{"titulo": "Fábula", "texto": "Cuento corto con animales."}, {"titulo": "Autores", "texto": "Esopo y Samaniego."}, {"titulo": "La zorra", "texto": "Puso una excusa."}],
"glosario": [{"palabra": "Fábula", "significado": "Cuento con animales y enseñanza."}, {"palabra": "Excusa", "significado": "Razón falsa para no admitir algo."}],
"carpeta": ["En las tiras, ¿qué pasó primero?", "¿Qué pasó al final?", "Tomi dice que las uvas estaban verdes de verdad. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("VIO UVAS MUY ALTAS") + ["Vio uvas muy altas.", "vio las uvas", "VIO LAS UVAS"], low("DIJO: ESTÁN VERDES") + low("DIJO ESTÁN VERDES") + low("dijo estan verdes") + ["Dijo que estaban verdes", "dijo que estaban verdes"], NO],
"soluciones": {"incompleto": "UVAS.", "solo": "La fábula con tus palabras.", "carpeta": ["Vio uvas muy altas.", "Dijo: están verdes.", "No: era una excusa."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a leer la fábula La liebre y la tortuga.",
"vas_a_ver": ["La carrera", "La liebre se duerme", "Gana la tortuga"],
"secciones": [
 S(1, "Una carrera", [
  P("La liebre se reía de la tortuga: ¡sos muy lenta!"),
  P("La tortuga le dijo: hagamos una <b>carrera</b>."),
  IMG("Las dos corredoras", "Una rápida y una lenta.", FG.objetos([("liebre", "LA LIEBRE"), ("tortuga", "LA TORTUGA")])),
 ]),
 S(1, "Lo que pasa", [
  IMG("La carrera", "La fábula en cuatro partes.", FG.tiras(["LA LIEBRE SALIÓ MUY RÁPIDO.", "SE CONFIÓ Y SE DURMIÓ.", "LA TORTUGA SIGUIÓ SIN PARAR.", "¡GANÓ LA TORTUGA!"], numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Leé las oraciones. Las vas a usar en la carpeta."),
  IMG("¿Quién?", "Pensá en la fábula.", FG.tiras(["1. SE DURMIÓ EN EL CAMINO.", "2. CAMINÓ DESPACIO SIN PARAR."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "¿Por qué perdió?", "planteo": "La liebre era más rápida.", "pasos": ["Se confió.", "Se durmió.", "Por eso perdió."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La carrera la ganó…", "pasos": ["Ganó la ___ ."]},
"ejemplo_solo": {"titulo": "Dibujala", "planteo": "Dibujá el final de la carrera."},
"tip": {"titulo": "Mirá el final", "texto": "El final de la fábula muestra la enseñanza."},
"ojo": ["La más rápida no ganó.", "La tortuga no se rindió."],
"resumen": [{"titulo": "Liebre", "texto": "Rápida, pero se confió."}, {"titulo": "Tortuga", "texto": "Lenta, pero no paró."}, {"titulo": "Final", "texto": "Ganó la tortuga."}],
"glosario": [{"palabra": "Liebre", "significado": "Animal parecido al conejo, muy rápido."}, {"palabra": "Confiarse", "significado": "Creer que ya ganaste antes de tiempo."}],
"carpeta": ["¿Quién hizo lo de la oración 1?", "¿Quién hizo lo de la oración 2?", "Tomi dice que ganó la liebre. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("LA LIEBRE") + low("LIEBRE"), low("LA TORTUGA") + low("TORTUGA"), NO],
"soluciones": {"incompleto": "TORTUGA.", "solo": "Tu dibujo del final.", "carpeta": ["La liebre.", "La tortuga.", "No: ganó la tortuga."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a descubrir qué enseña cada fábula.",
"vas_a_ver": ["La moraleja", "Moraleja de la zorra", "Moraleja de la liebre"],
"secciones": [
 S(1, "La moraleja", [
  D("Moraleja", "La <b>enseñanza</b> de la fábula."),
  P("Suele estar <b>al final</b>."),
  IMG("Dos fábulas, dos enseñanzas", "Cada una enseña algo.", FG.objetos([("zorra", "LA ZORRA"), ("tortuga", "LA TORTUGA")])),
 ]),
 S(1, "Qué enseñan", [
  P("<b>La zorra</b>: no hay que poner excusas cuando algo no sale."),
  P("<b>La liebre y la tortuga</b>: despacio y sin parar se llega lejos."),
  IMG("Las moralejas", "Lo que aprendemos.", FG.tiras(["ZORRA → NO PONER EXCUSAS", "TORTUGA → DESPACIO Y SIN PARAR"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Leé las moralejas. Las vas a usar en la carpeta."),
  IMG("¿De qué fábula?", "Uní cada moraleja.", FG.tiras(["1. NO TE CONFÍES ANTES DE TIEMPO.", "2. NO DIGAS QUE NO TE GUSTA LO QUE NO PUDISTE TENER."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar la moraleja", "planteo": "La liebre se confió y perdió.", "pasos": ["¿Qué le pasó?", "Perdió por confiarse.", "Moraleja: no te confíes."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La tortuga ganó porque…", "pasos": ["No ___ de caminar."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Alguna vez pusiste una excusa como la zorra? Contalo."},
"tip": {"titulo": "Preguntá ¿qué aprendo?", "texto": "La respuesta es la moraleja."},
"ojo": ["La moraleja no cuenta lo que pasó.", "Dice lo que aprendemos."],
"resumen": [{"titulo": "Moraleja", "texto": "La enseñanza."}, {"titulo": "Zorra", "texto": "No poner excusas."}, {"titulo": "Tortuga", "texto": "Despacio y sin parar."}],
"glosario": [{"palabra": "Moraleja", "significado": "Enseñanza de una fábula."}, {"palabra": "Enseñanza", "significado": "Lo que aprendemos."}],
"carpeta": ["¿De qué fábula es la moraleja 1?", "¿De qué fábula es la moraleja 2?", "Tomi dice que la moraleja es: la liebre se durmió. ¿Es una enseñanza?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("LA LIEBRE Y LA TORTUGA") + low("LIEBRE Y TORTUGA") + low("LA LIEBRE") + low("LA TORTUGA"), low("LA ZORRA Y LAS UVAS") + low("LA ZORRA") + low("ZORRA"), NO],
"soluciones": {"incompleto": "PARÓ.", "solo": "Tu historia.", "carpeta": ["La liebre y la tortuga.", "La zorra y las uvas.", "No: cuenta lo que pasó."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir una moraleja.",
"vas_a_ver": ["Pensar qué pasó", "Pensar qué aprendemos", "Escribir la moraleja"],
"secciones": [
 S(1, "Una fábula nueva", [
  P("Sofi lee otra fábula: un ratón ayudó a un león."),
  P("Después, el león quedó atrapado y el ratón lo salvó."),
  IMG("El ratón ayuda", "Chiquito, pero muy útil.", FG.objetos([("raton", "EL RATÓN")])),
 ]),
 S(1, "Escribir la moraleja", [
  P("1. ¿Qué pasó? 2. ¿Qué aprendemos?"),
  P("Moraleja: <b>todos podemos ayudar, aunque seamos chicos</b>."),
  IMG("Del cuento a la moraleja", "Una oración corta.", FG.tiras(["PASÓ: EL RATÓN SALVÓ AL LEÓN.", "APRENDO: TODOS PODEMOS AYUDAR."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Leé las moralejas. Las vas a usar en la carpeta."),
  IMG("¿Cuál es moraleja?", "Una enseña y otra solo cuenta.", FG.tiras(["1. EL RATÓN ERA CHIQUITO.", "2. HAY QUE AYUDAR A LOS DEMÁS."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Moraleja", "planteo": "La hormiga guardó comida y no pasó hambre.", "pasos": ["¿Qué pasó? Guardó comida.", "¿Qué aprendo? Hay que prepararse.", "Moraleja: es bueno prepararse."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El ratón ayudó al león.", "pasos": ["Moraleja: todos podemos ___ ."]},
"ejemplo_solo": {"titulo": "Tu moraleja", "planteo": "Inventá una moraleja para una historia que te haya pasado."},
"tip": {"titulo": "Corta y para todos", "texto": "La moraleja sirve para cualquier persona."},
"ojo": ["No cuentes la historia otra vez.", "Escribí lo que aprendemos."],
"resumen": [{"titulo": "¿Qué pasó?", "texto": "Pensar la historia."}, {"titulo": "¿Qué aprendo?", "texto": "La enseñanza."}, {"titulo": "Escribir", "texto": "Una oración corta."}],
"glosario": [{"palabra": "Atrapado", "significado": "Que no puede salir."}, {"palabra": "Prepararse", "significado": "Hacer algo antes para estar listo."}],
"carpeta": ["¿Qué oración del dibujo es una moraleja?", "Completá: el ratón ayudó al león. Todos podemos…", "Tomi escribió como moraleja: el león era grande. ¿Es una enseñanza?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [["2", "LA 2", "la 2", "La 2"] + low("HAY QUE AYUDAR A LOS DEMÁS") + low("hay que ayudar a los demas"), low("AYUDAR"), NO],
"soluciones": {"incompleto": "AYUDAR.", "solo": "Tu moraleja.", "carpeta": ["La 2.", "Ayudar.", "No: solo dice cómo era."]},
}

ACT = {
"1": [MC("¿QUÉ ES UNA FÁBULA?", ["UN CUENTO CON ANIMALES Y ENSEÑANZA", "UNA RECETA", "UNA FICHA DE DATOS"], "UN CUENTO CON ANIMALES Y ENSEÑANZA", "DEJA UNA ENSEÑANZA.", n="recordar"),
      TF("LA ZORRA PUDO ALCANZAR LAS UVAS.", "FALSO", "NO LLEGÓ Y PUSO UNA EXCUSA.", n="aplicar")],
"2": [MC("¿QUIÉN GANÓ LA CARRERA?", ["LA TORTUGA", "LA LIEBRE"], "LA TORTUGA", "NO PARÓ DE CAMINAR.", n="recordar"),
      ORD("ORDENÁ LA FÁBULA.", ["SE DURMIÓ", "LA LIEBRE SALIÓ RÁPIDO", "GANÓ LA TORTUGA"], ["LA LIEBRE SALIÓ RÁPIDO", "SE DURMIÓ", "GANÓ LA TORTUGA"], "PRIMERO SALIÓ, DESPUÉS SE DURMIÓ.", n="analizar")],
"3": [UNI("UNÍ CADA FÁBULA CON SU MORALEJA.", [("LA ZORRA Y LAS UVAS", "NO PONER EXCUSAS"), ("LA LIEBRE Y LA TORTUGA", "DESPACIO Y SIN PARAR")], "CADA FÁBULA ENSEÑA ALGO.", n="analizar"),
      MC("LA MORALEJA ES…", ["LA ENSEÑANZA", "EL TÍTULO", "UN PERSONAJE"], "LA ENSEÑANZA", "LO QUE APRENDEMOS.", n="recordar")],
"4": [MC("¿CUÁL ES UNA MORALEJA?", ["HAY QUE AYUDAR A LOS DEMÁS", "EL RATÓN ERA CHIQUITO"], "HAY QUE AYUDAR A LOS DEMÁS", "ES UNA ENSEÑANZA.", n="analizar"),
      SA("EL RATÓN AYUDÓ AL LEÓN. COMPLETÁ: TODOS PODEMOS ___", low("AYUDAR"), "AYUDAR.", n="aplicar")],
"5": [MC("RELÁMPAGO. EN LAS FÁBULAS HABLAN…", ["ANIMALES", "COMPUTADORAS"], "ANIMALES", "ANIMALES QUE HABLAN.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA LIEBRE SE…", ["DURMIÓ", "GANÓ"], "DURMIÓ", "SE CONFIÓ.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA ZORRA PUSO UNA…", ["EXCUSA", "CORONA"], "EXCUSA", "DIJO QUE ESTABAN VERDES.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA MORALEJA VA…", ["AL FINAL", "AL PRINCIPIO"], "AL FINAL", "SUELE IR AL FINAL.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ QUERÍA COMER LA ZORRA?", ["UVAS", "PAN", "QUESO"], "UVAS", "UVAS MUY ALTAS.", n="recordar")],
 [1, TF("LAS UVAS ESTABAN VERDES DE VERDAD.", "FALSO", "FUE UNA EXCUSA DE LA ZORRA.", n="error")],
 [1, SA("¿QUIÉN ESCRIBIÓ FÁBULAS HACE MUCHÍSIMO TIEMPO?", low("ESOPO") + low("SAMANIEGO"), "ESOPO.", n="recordar")],
 [2, MC("¿POR QUÉ PERDIÓ LA LIEBRE?", ["SE CONFIÓ Y SE DURMIÓ", "ERA MUY LENTA", "SE PERDIÓ EN EL MAR"], "SE CONFIÓ Y SE DURMIÓ", "SE CONFIÓ.", n="analizar")],
 [2, ORD("ORDENÁ LA FÁBULA.", ["GANÓ LA TORTUGA", "HICIERON UNA CARRERA", "LA LIEBRE SE DURMIÓ"], ["HICIERON UNA CARRERA", "LA LIEBRE SE DURMIÓ", "GANÓ LA TORTUGA"], "CARRERA, SIESTA Y FINAL.", n="analizar")],
 [2, TF("LA TORTUGA CAMINÓ SIN PARAR.", "VERDADERO", "POR ESO GANÓ.", n="recordar")],
 [3, UNI("UNÍ CADA FÁBULA CON SU MORALEJA.", [("LA ZORRA Y LAS UVAS", "NO PONER EXCUSAS"), ("LA LIEBRE Y LA TORTUGA", "NO CONFIARSE")], "LO QUE ENSEÑA CADA UNA.", n="analizar")],
 [3, MC("¿DÓNDE SUELE ESTAR LA MORALEJA?", ["AL FINAL", "EN EL TÍTULO", "EN EL DIBUJO"], "AL FINAL", "CIERRA LA FÁBULA.", n="recordar")],
 [3, TF("LA LIEBRE SE DURMIÓ ES UNA MORALEJA.", "FALSO", "CUENTA LO QUE PASÓ, NO ENSEÑA.", n="error")],
 [4, MC("UN RATÓN SALVÓ A UN LEÓN. ¿CUÁL ES LA MORALEJA?", ["TODOS PODEMOS AYUDAR", "LOS LEONES RUGEN", "EL RATÓN ES GRIS"], "TODOS PODEMOS AYUDAR", "ES LA ENSEÑANZA.", n="analizar")],
 [4, SA("LA HORMIGA GUARDÓ COMIDA Y NO PASÓ HAMBRE. COMPLETÁ: ES BUENO ___", low("PREPARARSE") + low("GUARDAR") + low("AHORRAR") + low("TRABAJAR") + low("GUARDAR COMIDA"), "PREPARARSE.", n="aplicar")],
 [4, TF("UNA MORALEJA CUENTA OTRA VEZ TODA LA HISTORIA.", "FALSO", "DICE LO QUE APRENDEMOS.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 12, "estilo": "primeros",
     "practica": "Práctica general: fábulas", "examen_titulo": "Nivel jefe: fábulas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-12.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
