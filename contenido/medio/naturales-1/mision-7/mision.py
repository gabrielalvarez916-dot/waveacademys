# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 7 · El cielo de día y de noche. Genera mision-7.json.
Regla de primeros años. Metáfora: el diario del cielo de Sofi. Nunca mirar el sol directo.
Niveles: 1 el sol sale y se pone · 2 el día y la noche · 3 la luna y sus cambios · 4 dibujo el cielo."""
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
"objetivo": "Vas a ver cómo el sol sale y se pone.",
"vas_a_ver": ["El amanecer", "El mediodía", "El atardecer"],
"secciones": [
 S(1, "El sol sale", [
  P("A la mañana el sol <b>sale</b> por un lado del cielo: es el <b>amanecer</b>."),
  IMG("El camino del sol", "Mañana, mediodía, tarde.", FG.tiras(["MAÑANA: SALE", "MEDIODÍA: ARRIBA", "TARDE: SE PONE"], numeros=True, cols=3)),
 ]),
 S(1, "El sol se pone", [
  D("Atardecer", "Cuando el sol se esconde y empieza la noche."),
  P("A la tarde el sol <b>se pone</b> por el otro lado."),
  IMG("Sale y se pone", "Por lados distintos.", FG.tiras(["AMANECER", "ATARDECER"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los momentos. Los vas a usar en la carpeta."),
  IMG("¿Dónde está el sol?", "Pensá.", FG.tiras(["DESAYUNO", "ALMUERZO", "MERIENDA"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi sombra", "planteo": "Miro mi sombra al mediodía.", "pasos": ["El sol está muy arriba.", "Mi sombra es cortita.", "A la tarde se hace larga."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "A la mañana el sol…", "pasos": ["A la mañana el sol ___."]},
"ejemplo_solo": {"titulo": "Desde tu ventana", "planteo": "Fijate por dónde sale el sol en tu casa."},
"tip": {"titulo": "Mirá la sombra", "texto": "La sombra te dice dónde está el sol."},
"ojo": ["Nunca mires el sol directo: lastima los ojos.", "El sol no se apaga: se esconde."],
"resumen": [{"titulo": "Amanecer", "texto": "El sol sale."}, {"titulo": "Mediodía", "texto": "Está arriba."}, {"titulo": "Atardecer", "texto": "Se pone."}],
"glosario": [{"palabra": "Amanecer", "significado": "Cuando sale el sol."}, {"palabra": "Sombra", "significado": "Lugar oscuro detrás de algo que tapa la luz."}],
"carpeta": ["¿Dónde está el sol en el almuerzo?", "¿Qué hace el sol en la merienda?", "¿Cómo es tu sombra al mediodía?"],
"respuestas_carpeta": [acepta("ARRIBA", "MUY ARRIBA", "EN EL MEDIO"), acepta("SE PONE", "BAJA", "SE ESCONDE", "SE ESTÁ PONIENDO"), acepta("CORTA", "CORTITA", "CHIQUITA")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "SALE.", "solo": "Siempre por el mismo lado.", "carpeta": ["ARRIBA.", "SE PONE.", "CORTITA."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver por qué hay día y noche.",
"vas_a_ver": ["La Tierra gira", "El día", "La noche"],
"secciones": [
 S(1, "La Tierra gira", [
  P("La Tierra <b>gira</b> como un trompo. Una parte mira al sol y otra no."),
  IMG("Gira", "Una vuelta por día.", FG.tiras(["MIRA AL SOL: DÍA", "NO MIRA AL SOL: NOCHE"], numeros=False, cols=2)),
 ]),
 S(1, "Día y noche", [
  D("Día", "Cuando hay luz del sol."),
  P("De día jugamos y vamos a la escuela. De noche dormimos."),
  IMG("Qué hacemos", "Día y noche.", FG.tiras(["DÍA: ESCUELA", "NOCHE: DORMIR"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las actividades. Las vas a usar en la carpeta."),
  IMG("¿Día o noche?", "Pensá.", FG.tiras(["DESAYUNAR", "VER LA LUNA", "IR A LA PLAZA"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La linterna", "planteo": "Alumbramos una pelota.", "pasos": ["La linterna es el sol.", "Un lado de la pelota se ilumina.", "El otro queda oscuro: noche."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La Tierra…", "pasos": ["La Tierra ___ como un trompo."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Alumbrá una pelota con una linterna y girala."},
"tip": {"titulo": "Como un trompo", "texto": "La Tierra da vueltas sin parar."},
"ojo": ["El sol no se va a dormir: la Tierra gira.", "Cuando acá es de noche, en otro lugar es de día."],
"resumen": [{"titulo": "Gira", "texto": "Como un trompo."}, {"titulo": "Día", "texto": "Mira al sol."}, {"titulo": "Noche", "texto": "No mira al sol."}],
"glosario": [{"palabra": "Girar", "significado": "Dar vueltas."}, {"palabra": "Trompo", "significado": "Juguete que gira."}],
"carpeta": ["Desayunar, ¿de día o de noche?", "Ver la luna, ¿de día o de noche?", "Tomi dice que de noche el sol se apaga. ¿Está bien?"],
"respuestas_carpeta": [acepta("DÍA", "DIA", "DE DÍA", "DE DIA"), acepta("NOCHE", "DE NOCHE"), acepta("NO", "NO, LA TIERRA GIRA", "NO LA TIERRA GIRA")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "GIRA.", "solo": "Un lado se ilumina.", "carpeta": ["DE DÍA.", "DE NOCHE.", "NO: LA TIERRA GIRA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver cómo cambia la luna.",
"vas_a_ver": ["La luna", "Sus formas", "Un ciclo"],
"secciones": [
 S(1, "La luna", [
  P("La <b>luna</b> se ve de noche y a veces también de día."),
  IMG("La luna", "En el cielo.", FG.tiras(["DE NOCHE", "A VECES DE DÍA"], numeros=False, cols=2)),
 ]),
 S(1, "Sus formas", [
  D("Fases", "Las formas que vemos de la luna."),
  P("La luna parece cambiar: <b>nueva</b>, <b>creciente</b>, <b>llena</b> y <b>menguante</b>."),
  IMG("Las fases", "En orden.", FG.tiras(["NUEVA: NO SE VE", "CRECIENTE", "LLENA: REDONDA", "MENGUANTE"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las fases. Las vas a usar en la carpeta."),
  IMG("¿Cuál es?", "Pensá.", FG.tiras(["REDONDA ENTERA", "NO SE VE"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "Luna llena", "planteo": "Sofi mira el cielo.", "pasos": ["La luna está redonda.", "Brilla mucho.", "Es luna llena."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La luna redonda…", "pasos": ["Es luna ___."]},
"ejemplo_solo": {"titulo": "Mirá la luna", "planteo": "Esta noche mirá la luna. Dibujá su forma."},
"tip": {"titulo": "Mirá cada noche", "texto": "Si la mirás varios días, la ves cambiar."},
"ojo": ["La luna no se rompe: cambia lo que vemos.", "La luna no tiene luz propia: la ilumina el sol."],
"resumen": [{"titulo": "Luna", "texto": "De noche y a veces de día."}, {"titulo": "Fases", "texto": "Sus formas."}, {"titulo": "Ciclo", "texto": "Se repite."}],
"glosario": [{"palabra": "Fase", "significado": "Forma de la luna que vemos."}, {"palabra": "Ciclo", "significado": "Algo que se repite."}],
"carpeta": ["¿Cómo se llama la luna redonda entera?", "¿Cómo se llama la luna que no se ve?", "¿Qué fase viene después de la creciente?"],
"respuestas_carpeta": [acepta("LLENA", "LUNA LLENA"), acepta("NUEVA", "LUNA NUEVA"), acepta("LLENA", "LUNA LLENA")],
"carpeta_nivel": ["recordar", "recordar", "aplicar"],
"soluciones": {"incompleto": "LLENA.", "solo": "Tu dibujo de la luna.", "carpeta": ["LLENA.", "NUEVA.", "LLENA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a dibujar el cielo de día y de noche.",
"vas_a_ver": ["El cielo de día", "El cielo de noche", "Mi registro"],
"secciones": [
 S(1, "De día y de noche", [
  P("De día vemos el <b>sol</b> y las <b>nubes</b>. De noche, la <b>luna</b> y las <b>estrellas</b>."),
  IMG("El cielo", "Día y noche.", FG.tiras(["DÍA: SOL, NUBES", "NOCHE: LUNA, ESTRELLAS"], numeros=False, cols=2)),
 ]),
 S(1, "Mi registro", [
  D("Registro del cielo", "Dibujo con la hora y lo que vi."),
  P("Mirás, dibujás, anotás la hora y comparás."),
  IMG("Los pasos", "En orden.", FG.tiras(["MIRO", "DIBUJO", "ANOTO LA HORA", "COMPARO"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el registro de Sofi. Lo vas a usar en la carpeta."),
  IMG("Registro de Sofi", "Dos dibujos.", FG.tiras(["MAÑANA: SOL Y NUBES", "NOCHE: LUNA LLENA"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi dibujo", "planteo": "Dibujo el cielo de la tarde.", "pasos": ["Miro: hay nubes.", "Las dibujo.", "Anoto: TARDE."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "De noche vemos…", "pasos": ["LA LUNA Y LAS ___."]},
"ejemplo_solo": {"titulo": "Tu cielo", "planteo": "Dibujá el cielo de hoy a la mañana y a la noche."},
"tip": {"titulo": "Anotá la hora", "texto": "Así podés comparar después."},
"ojo": ["Nunca mires el sol directo.", "Dibujá lo que ves, no lo que imaginás."],
"resumen": [{"titulo": "Día", "texto": "Sol y nubes."}, {"titulo": "Noche", "texto": "Luna y estrellas."}, {"titulo": "Registro", "texto": "Dibujo y hora."}],
"glosario": [{"palabra": "Estrella", "significado": "Punto de luz en el cielo de noche."}, {"palabra": "Nube", "significado": "Montón de gotitas en el cielo."}],
"carpeta": ["¿Qué vio Sofi a la mañana?", "¿Qué luna vio Sofi de noche?", "Tomi dibujó el sol en el cielo de noche. ¿Está bien?"],
"respuestas_carpeta": [acepta("SOL Y NUBES", "EL SOL Y LAS NUBES", "NUBES Y SOL"), acepta("LLENA", "LUNA LLENA", "LA LUNA LLENA"), acepta("NO", "NO, DE NOCHE NO SE VE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "ESTRELLAS.", "solo": "Tus dos dibujos.", "carpeta": ["SOL Y NUBES.", "LUNA LLENA.", "NO: DE NOCHE NO SE VE EL SOL."]},
}

ACT = {
"1": [MC("¿QUÉ HACE EL SOL A LA MAÑANA?", ["SALE", "SE PONE", "SE APAGA"], "SALE", "ES EL AMANECER.", n="recordar"),
      MC("TU SOMBRA ES CORTITA. ¿DÓNDE ESTÁ EL SOL?", ["MUY ARRIBA", "ESCONDIDO", "MUY ABAJO"], "MUY ARRIBA", "AL MEDIODÍA, SOMBRA CORTA.", n="analizar")],
"2": [MC("¿POR QUÉ HAY DÍA Y NOCHE?", ["LA TIERRA GIRA", "EL SOL SE APAGA", "LA LUNA TAPA AL SOL"], "LA TIERRA GIRA", "COMO UN TROMPO.", n="analizar"),
      MC("¿CUÁNDO VAMOS A LA ESCUELA?", ["DE DÍA", "DE NOCHE", "NUNCA"], "DE DÍA", "CON LUZ DEL SOL.", n="aplicar")],
"3": [MC("LA LUNA REDONDA ENTERA ES LA LUNA…", ["LLENA", "NUEVA", "MENGUANTE"], "LLENA", "LUNA LLENA.", n="recordar"),
      ORD("ORDENÁ LAS FASES DE LA LUNA.", ["LLENA", "NUEVA", "MENGUANTE", "CRECIENTE"], ["NUEVA", "CRECIENTE", "LLENA", "MENGUANTE"], "NUEVA, CRECIENTE, LLENA, MENGUANTE.", n="aplicar")],
"4": [MC("¿QUÉ VEMOS EN EL CIELO DE NOCHE?", ["LUNA Y ESTRELLAS", "SOL Y ARCOÍRIS", "SOLO NUBES"], "LUNA Y ESTRELLAS", "DE NOCHE.", n="recordar"),
      MC("SOFI DIBUJÓ EL CIELO PERO NO ANOTÓ LA HORA. ¿QUÉ PROBLEMA HAY?", ["NO PUEDE COMPARAR", "NINGUNO", "EL DIBUJO SE BORRA"], "NO PUEDE COMPARAR", "LA HORA AYUDA A COMPARAR.", n="error")],
"5": [MC("RELÁMPAGO. ¿CÓMO SE LLAMA CUANDO SALE EL SOL?", ["AMANECER", "ATARDECER", "NOCHE"], "AMANECER", "AMANECER.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ GIRA COMO UN TROMPO?", ["LA TIERRA", "LA LUNA LLENA", "LA NUBE"], "LA TIERRA", "LA TIERRA.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. LA LUNA QUE NO SE VE ES LA LUNA…", acepta("NUEVA"), "NUEVA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿SE PUEDE MIRAR EL SOL DIRECTO?", ["NO", "SÍ", "SOLO A LA TARDE"], "NO", "LASTIMA LOS OJOS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("A LA TARDE, EL SOL…", ["SE PONE", "SALE", "SE APAGA"], "SE PONE", "ES EL ATARDECER.", n="recordar")],
 [1, MC("¿POR QUÉ NO HAY QUE MIRAR EL SOL DIRECTO?", ["LASTIMA LOS OJOS", "SE APAGA", "SE ESCONDE"], "LASTIMA LOS OJOS", "SIEMPRE CUIDAR LOS OJOS.", n="analizar")],
 [1, ORD("ORDENÁ EL CAMINO DEL SOL.", ["SE PONE", "SALE", "ESTÁ ARRIBA"], ["SALE", "ESTÁ ARRIBA", "SE PONE"], "MAÑANA, MEDIODÍA, TARDE.", n="aplicar")],
 [2, MC("¿POR QUÉ ES DE NOCHE?", ["NUESTRA PARTE NO MIRA AL SOL", "EL SOL SE APAGÓ", "LA LUNA SE COMIÓ AL SOL"], "NUESTRA PARTE NO MIRA AL SOL", "LA TIERRA GIRA.", n="analizar")],
 [2, SA("VER LA LUNA, ¿DE DÍA O DE NOCHE?", acepta("NOCHE", "DE NOCHE"), "DE NOCHE.", n="aplicar")],
 [2, MC("TOMI DICE QUE EL SOL SE VA A DORMIR. ¿QUÉ PASA EN REALIDAD?", ["LA TIERRA GIRA", "EL SOL DUERME", "EL SOL SE APAGA"], "LA TIERRA GIRA", "EL SOL NO DUERME.", n="error")],
 [3, MC("LAS FORMAS QUE VEMOS DE LA LUNA SON…", ["SUS FASES", "SUS NUBES", "SUS RAYOS"], "SUS FASES", "NUEVA, CRECIENTE, LLENA, MENGUANTE.", n="recordar")],
 [3, MC("¿QUÉ FASE VIENE DESPUÉS DE LA LUNA NUEVA?", ["CRECIENTE", "LLENA", "MENGUANTE"], "CRECIENTE", "NUEVA Y DESPUÉS CRECIENTE.", n="aplicar")],
 [3, SA("LA LUNA REDONDA ENTERA ES LA LUNA…", acepta("LLENA"), "LLENA.", n="recordar")],
 [4, MC("¿QUÉ VEMOS EN EL CIELO DE DÍA?", ["SOL Y NUBES", "LUNA LLENA Y ESTRELLAS", "SOLO ESTRELLAS"], "SOL Y NUBES", "DE DÍA.", n="recordar")],
 [4, ORD("ORDENÁ LOS PASOS DEL REGISTRO.", ["COMPARO", "MIRO", "ANOTO LA HORA", "DIBUJO"], ["MIRO", "DIBUJO", "ANOTO LA HORA", "COMPARO"], "EN ORDEN.", n="aplicar")],
 [4, MC("SOFI DIBUJÓ ESTRELLAS EN EL CIELO DEL MEDIODÍA. ¿QUÉ PASÓ?", ["DIBUJÓ LO QUE IMAGINÓ", "DIBUJÓ LO QUE VIO", "ESTÁ BIEN"], "DIBUJÓ LO QUE IMAGINÓ", "DE DÍA NO SE VEN.", n="error")],
 [4, SA("¿QUÉ SE ANOTA AL LADO DEL DIBUJO DEL CIELO?", acepta("LA HORA", "HORA", "EL MOMENTO"), "LA HORA.", n="recordar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: el cielo", "examen_titulo": "Nivel jefe: el cielo de día y de noche",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
