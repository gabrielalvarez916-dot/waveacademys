# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 8 · Estaciones y orientación. Genera mision-8.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (hoy mira el cielo y usa la brújula).
Niveles: 1 la luna y sus fases · 2 las cuatro estaciones · 3 los puntos cardinales · 4 orientarse con el sol."""
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
"objetivo": "Vas a conocer las caras de la luna.",
"vas_a_ver": ["La luna", "Sus fases", "Luz del sol"],
"secciones": [
 S(1, "La luna", [
  P("De noche, Tomi mira la <b>luna</b>. ¡Cada noche se ve distinta!"),
  P("La luna <b>no tiene luz propia</b>: la ilumina el <b>sol</b>."),
  D("Fases de la luna", "Las formas que vemos de la luna, que <b>cambian</b> de a poco."),
  IMG("La luna y el sol", "El sol ilumina la luna.", FG.nombres(["SOL", "LUNA", "TIERRA"], cols=3)),
 ]),
 S(1, "Las cuatro fases", [
  P("Primero casi no se ve. Después crece, se ve redonda y achica."),
  IMG("Las fases", "Se repiten siempre.", FG.tiras(["1. LUNA NUEVA: NO SE VE", "2. CRECIENTE: CRECE", "3. LLENA: REDONDA", "4. MENGUANTE: ACHICA"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Qué fase es?", "Pensá en cada una.", FG.tiras(["1. SE VE TODA REDONDA", "2. CASI NO SE VE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Luna llena", "planteo": "¿Cómo es la luna llena?", "pasos": ["Se ve toda redonda.", "Brilla mucho.", "Después empieza a achicarse."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "A la luna la ilumina…", "pasos": ["…el ___ ."]},
"ejemplo_solo": {"titulo": "Mirá la luna", "planteo": "Esta noche mirá la luna con un adulto. Dibujá su forma."},
"tip": {"titulo": "Un ciclo", "texto": "Las fases se repiten todos los meses."},
"ojo": ["La luna no cambia de verdad: cambia lo que vemos.", "La luna no tiene luz propia."],
"resumen": [{"titulo": "Luna", "texto": "La ilumina el sol."}, {"titulo": "Fases", "texto": "Nueva, creciente, llena, menguante."}, {"titulo": "Ciclo", "texto": "Se repiten."}],
"glosario": [{"palabra": "Fase", "significado": "Forma que vemos de la luna."}, {"palabra": "Menguante", "significado": "Que se achica."}],
"carpeta": ["¿Qué fase es la tarjeta 1?", "¿Qué fase es la tarjeta 2?", "Tomi dice que la luna tiene luz propia. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("LLENA") + low("LUNA LLENA") + low("LA LUNA LLENA"), low("NUEVA") + low("LUNA NUEVA") + low("LA LUNA NUEVA"), NO],
"soluciones": {"incompleto": "SOL.", "solo": "Tu dibujo de la luna.", "carpeta": ["Luna llena.", "Luna nueva.", "No: la ilumina el sol."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer las cuatro estaciones.",
"vas_a_ver": ["Verano y otoño", "Invierno y primavera", "Cómo nos vestimos"],
"secciones": [
 S(1, "Las estaciones", [
  P("El año tiene cuatro <b>estaciones</b>: verano, otoño, invierno y primavera."),
  IMG("Las cuatro estaciones", "Cada una es distinta.", FG.tiras(["VERANO: CALOR", "OTOÑO: CAEN LAS HOJAS", "INVIERNO: FRÍO", "PRIMAVERA: FLORES"], numeros=False)),
 ]),
 S(1, "Cómo nos vestimos", [
  P("En <b>verano</b> usamos ropa liviana. En <b>invierno</b>, abrigo."),
  IMG("Ropa para cada estación", "Elegimos según el tiempo.", FG.nombres(["MALLA", "CAMPERA", "BUFANDA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué estación es?", "Pensá en cada pista.", FG.tiras(["1. LOS ÁRBOLES SE LLENAN DE FLORES", "2. HACE MUCHO FRÍO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El otoño", "planteo": "¿Cómo me doy cuenta de que es otoño?", "pasos": ["Las hojas se ponen marrones.", "Se caen de los árboles.", "Empieza a refrescar."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En invierno usamos…", "pasos": ["…ropa de ___ ."]},
"ejemplo_solo": {"titulo": "Hoy", "planteo": "¿En qué estación estamos hoy? ¿Cómo te diste cuenta?"},
"tip": {"titulo": "En orden", "texto": "Verano, otoño, invierno, primavera… ¡y otra vez!"},
"ojo": ["Las estaciones se repiten cada año.", "En verano, cuidate del sol."],
"resumen": [{"titulo": "Verano", "texto": "Calor."}, {"titulo": "Otoño", "texto": "Caen las hojas."}, {"titulo": "Invierno y primavera", "texto": "Frío y flores."}],
"glosario": [{"palabra": "Estación", "significado": "Parte del año con su clima."}, {"palabra": "Abrigo", "significado": "Ropa para el frío."}],
"carpeta": ["¿Qué estación es la pista 1?", "¿Qué estación es la pista 2?", "Tomi dice que en verano se usa bufanda. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PRIMAVERA") + low("LA PRIMAVERA") + low("EN PRIMAVERA"), low("INVIERNO") + low("EL INVIERNO") + low("EN INVIERNO"), NO],
"soluciones": {"incompleto": "ABRIGO.", "solo": "La estación de hoy.", "carpeta": ["Primavera.", "Invierno.", "No: en verano hace calor."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer los puntos cardinales.",
"vas_a_ver": ["Norte y sur", "Este y oeste", "La brújula"],
"secciones": [
 S(1, "Los puntos cardinales", [
  D("Puntos cardinales", "Norte, sur, este y oeste. Sirven para <b>ubicarnos</b>."),
  P("Por el <b>este</b> sale el sol. Por el <b>oeste</b> se esconde."),
  IMG("Los cuatro puntos", "Norte, sur, este y oeste.", FG.tiras(["NORTE", "SUR", "ESTE: SALE EL SOL", "OESTE: SE ESCONDE"], numeros=False)),
 ]),
 S(1, "La brújula", [
  P("La <b>brújula</b> tiene una aguja que siempre apunta al <b>norte</b>."),
  IMG("Para ubicarnos", "Objetos que ayudan.", FG.nombres(["BRÚJULA", "MAPA", "EL SOL"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué punto es?", "Pensá en el sol.", FG.tiras(["1. POR ACÁ SALE EL SOL", "2. POR ACÁ SE ESCONDE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La brújula", "planteo": "¿Para dónde apunta la aguja?", "pasos": ["Pongo la brújula quieta.", "La aguja se mueve.", "Apunta al norte."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El sol sale por el…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu casa", "planteo": "A la mañana, mirá por dónde sale el sol en tu casa."},
"tip": {"titulo": "Cuatro puntos", "texto": "Norte y sur son opuestos. Este y oeste, también."},
"ojo": ["Nunca mires el sol directo.", "La aguja de la brújula apunta al norte."],
"resumen": [{"titulo": "Este", "texto": "Sale el sol."}, {"titulo": "Oeste", "texto": "Se esconde."}, {"titulo": "Brújula", "texto": "Apunta al norte."}],
"glosario": [{"palabra": "Brújula", "significado": "Aparato que señala el norte."}, {"palabra": "Opuesto", "significado": "Del otro lado."}],
"carpeta": ["¿Qué punto es la pista 1?", "¿Qué punto es la pista 2?", "Tomi dice que el sol sale por el oeste. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ESTE") + low("EL ESTE"), low("OESTE") + low("EL OESTE"), NO],
"soluciones": {"incompleto": "ESTE.", "solo": "Por dónde sale el sol.", "carpeta": ["El este.", "El oeste.", "No: sale por el este."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a usar el sol para ubicarte.",
"vas_a_ver": ["Mañana, mediodía y tarde", "El truco del brazo", "Las sombras"],
"secciones": [
 S(1, "El sol en el día", [
  P("A la <b>mañana</b>, el sol está bajo, del lado del este."),
  P("Al <b>mediodía</b> está alto. A la <b>tarde</b> baja hacia el oeste."),
  IMG("El viaje del sol", "Lo vemos moverse en el cielo.", FG.tiras(["MAÑANA: ESTE", "MEDIODÍA: ARRIBA", "TARDE: OESTE"], numeros=False, cols=1)),
 ]),
 S(1, "El truco del brazo", [
  P("Señalá con el brazo <b>derecho</b> donde sale el sol."),
  P("Adelante tenés el <b>norte</b>. Atrás, el <b>sur</b>."),
  IMG("Mi cuerpo, mi brújula", "Brazo derecho al este.", FG.tiras(["DERECHA: ESTE", "IZQUIERDA: OESTE", "ADELANTE: NORTE", "ATRÁS: SUR"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Dónde está el sol?", "Pensá en la hora.", FG.tiras(["1. SON LAS 8 DE LA MAÑANA", "2. SON LAS 6 DE LA TARDE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Ubicarme", "planteo": "¿Dónde queda el norte?", "pasos": ["Busco por dónde salió el sol.", "Lo señalo con la derecha.", "Adelante está el norte."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "A la tarde, el sol baja hacia el…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "En el patio, hacé el truco del brazo. ¿Qué ves adelante?"},
"tip": {"titulo": "Sombras", "texto": "Al mediodía la sombra es cortita."},
"ojo": ["Nunca mires el sol directo.", "Usá gorra si estás al sol."],
"resumen": [{"titulo": "Mañana", "texto": "Sol al este."}, {"titulo": "Tarde", "texto": "Sol al oeste."}, {"titulo": "Truco", "texto": "Derecha al este: norte adelante."}],
"glosario": [{"palabra": "Mediodía", "significado": "Mitad del día."}, {"palabra": "Sombra", "significado": "Lugar oscuro donde no llega el sol."}],
"carpeta": ["En la tarjeta 1, ¿hacia qué lado está el sol?", "¿Y en la tarjeta 2?", "Tomi dice que con la derecha al este, adelante está el sur. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ESTE") + low("AL ESTE") + low("EL ESTE"), low("OESTE") + low("AL OESTE") + low("EL OESTE"), NO],
"soluciones": {"incompleto": "OESTE.", "solo": "Lo que viste adelante.", "carpeta": ["Al este.", "Al oeste.", "No: adelante está el norte."]},
}

ACT = {
"1": [ORD("ORDENÁ LAS FASES.", ["LLENA", "NUEVA", "CRECIENTE"], ["NUEVA", "CRECIENTE", "LLENA"], "PRIMERO NO SE VE.", n="analizar"),
      TF("LA LUNA TIENE LUZ PROPIA.", "FALSO", "LA ILUMINA EL SOL.", n="error")],
"2": [UNI("UNÍ CADA ESTACIÓN.", [("VERANO", "CALOR"), ("OTOÑO", "CAEN LAS HOJAS"), ("PRIMAVERA", "FLORES")], "CADA UNA TIENE LO SUYO.", n="analizar"),
      MC("¿QUÉ USAMOS EN INVIERNO?", ["BUFANDA", "MALLA"], "BUFANDA", "PARA EL FRÍO.", n="aplicar")],
"3": [MC("¿POR DÓNDE SALE EL SOL?", ["POR EL ESTE", "POR EL OESTE"], "POR EL ESTE", "Y SE ESCONDE POR EL OESTE.", n="recordar"),
      SA("¿A QUÉ PUNTO APUNTA LA BRÚJULA?", low("NORTE") + low("AL NORTE") + low("EL NORTE"), "AL NORTE.", n="recordar")],
"4": [MC("A LA TARDE, EL SOL ESTÁ…", ["HACIA EL OESTE", "HACIA EL ESTE"], "HACIA EL OESTE", "SE VA A ESCONDER.", n="aplicar"),
      TF("CON LA DERECHA AL ESTE, ADELANTE ESTÁ EL NORTE.", "VERDADERO", "ES EL TRUCO DEL BRAZO.", n="analizar")],
"5": [MC("RELÁMPAGO. LA LUNA REDONDA ES…", ["LLENA", "NUEVA"], "LLENA", "SE VE TODA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. CAEN LAS HOJAS EN…", ["OTOÑO", "VERANO"], "OTOÑO", "LAS HOJAS SE SECAN.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL SOL SE ESCONDE POR…", ["EL OESTE", "EL NORTE"], "EL OESTE", "AL ATARDECER.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA SOMBRA MÁS CORTA ES…", ["AL MEDIODÍA", "A LA TARDE"], "AL MEDIODÍA", "EL SOL ESTÁ ALTO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUIÉN ILUMINA LA LUNA?", ["EL SOL", "LAS ESTRELLAS"], "EL SOL", "NO TIENE LUZ PROPIA.", n="recordar")],
 [1, SA("¿CÓMO SE LLAMA LA LUNA QUE SE ACHICA?", low("MENGUANTE") + low("LUNA MENGUANTE"), "MENGUANTE.", n="recordar")],
 [1, TF("LAS FASES DE LA LUNA SE REPITEN.", "VERDADERO", "ES UN CICLO.", n="recordar")],
 [2, ORD("ORDENÁ LAS ESTACIONES.", ["INVIERNO", "VERANO", "OTOÑO"], ["VERANO", "OTOÑO", "INVIERNO"], "DESPUÉS VIENE LA PRIMAVERA.", n="analizar")],
 [2, SA("¿EN QUÉ ESTACIÓN HAY MÁS FLORES?", low("PRIMAVERA") + low("EN PRIMAVERA") + low("LA PRIMAVERA"), "EN PRIMAVERA.", n="aplicar")],
 [2, TF("EN VERANO USAMOS CAMPERA Y BUFANDA.", "FALSO", "EN VERANO HACE CALOR.", n="error")],
 [3, UNI("UNÍ CADA PUNTO.", [("ESTE", "SALE EL SOL"), ("OESTE", "SE ESCONDE EL SOL")], "PENSÁ EN EL SOL.", n="analizar")],
 [3, MC("¿CUÁL ES EL OPUESTO DEL NORTE?", ["EL SUR", "EL ESTE"], "EL SUR", "ESTÁN DE LADOS CONTRARIOS.", n="aplicar")],
 [3, TF("LA AGUJA DE LA BRÚJULA APUNTA AL SUR.", "FALSO", "APUNTA AL NORTE.", n="error")],
 [4, MC("A LA MAÑANA, EL SOL ESTÁ…", ["HACIA EL ESTE", "HACIA EL OESTE"], "HACIA EL ESTE", "RECIÉN SALIÓ.", n="aplicar")],
 [4, SA("CON LA DERECHA AL ESTE, ¿QUÉ TENÉS ATRÁS?", low("SUR") + low("EL SUR"), "EL SUR.", n="analizar")],
 [4, TF("NO HAY QUE MIRAR EL SOL DIRECTO.", "VERDADERO", "LASTIMA LOS OJOS.", n="recordar")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 8, "estilo": "primeros",
     "practica": "Práctica general: estaciones y orientación", "examen_titulo": "Nivel jefe: estaciones y orientación",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
