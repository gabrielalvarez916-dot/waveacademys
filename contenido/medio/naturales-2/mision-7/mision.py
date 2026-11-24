# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 7 · El ciclo del agua. Genera mision-7.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (hoy mira el cielo un día de lluvia).
Niveles: 1 lluvia y nubes · 2 ríos, lagos y mares · 3 el agua vuelve al cielo · 4 medimos la lluvia."""
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
"objetivo": "Vas a ver de dónde viene la lluvia.",
"vas_a_ver": ["Las nubes", "La lluvia", "Granizo y nieve"],
"secciones": [
 S(1, "Las nubes", [
  P("Tomi mira el cielo: hay <b>nubes</b> grises."),
  D("Nube", "Muchas <b>gotitas de agua</b> juntas, allá arriba."),
  P("Cuando las gotitas se hacen grandes y pesadas, ¡<b>llueve</b>!"),
  IMG("De la nube a la lluvia", "Las gotitas caen.", FG.tiras(["GOTITAS EN LA NUBE", "SE JUNTAN", "SE HACEN PESADAS", "¡LLUEVE!"], numeros=True)),
 ]),
 S(1, "Granizo y nieve", [
  P("Si hace mucho <b>frío</b> arriba, el agua cae como <b>granizo</b> o <b>nieve</b>."),
  IMG("Agua que cae", "Lluvia, granizo o nieve.", FG.nombres(["LLUVIA", "GRANIZO", "NIEVE"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Qué pasa primero?", FG.tiras(["LLUEVE", "GOTITAS EN LA NUBE", "SE HACEN PESADAS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La lluvia", "planteo": "¿Por qué llueve?", "pasos": ["En la nube hay gotitas.", "Se juntan y pesan.", "Caen: ¡llueve!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La nube tiene…", "pasos": ["…muchas ___ de agua."]},
"ejemplo_solo": {"titulo": "Mirá el cielo", "planteo": "Mirá el cielo hoy. ¿Cómo son las nubes?"},
"tip": {"titulo": "Nubes grises", "texto": "Las nubes grises y oscuras traen lluvia."},
"ojo": ["Las nubes son de agua, no de algodón.", "La nieve también es agua."],
"resumen": [{"titulo": "Nube", "texto": "Gotitas juntas."}, {"titulo": "Lluvia", "texto": "Gotitas que caen."}, {"titulo": "Frío", "texto": "Granizo o nieve."}],
"glosario": [{"palabra": "Nube", "significado": "Gotitas de agua juntas en el cielo."}, {"palabra": "Granizo", "significado": "Piedritas de hielo que caen."}],
"carpeta": ["De las tarjetas del dibujo, ¿qué pasa primero?", "¿Qué pasa al final?", "Tomi dice que las nubes son de algodón. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("GOTITAS EN LA NUBE") + low("LAS GOTITAS EN LA NUBE"), low("LLUEVE"), NO],
"soluciones": {"incompleto": "GOTITAS.", "solo": "Cómo eran las nubes.", "carpeta": ["Gotitas en la nube.", "Llueve.", "No: son gotitas de agua."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer dónde está el agua.",
"vas_a_ver": ["Ríos", "Lagos y lagunas", "Mares"],
"secciones": [
 S(1, "Agua en movimiento y quieta", [
  P("El <b>río</b> corre. El <b>lago</b> y la <b>laguna</b> están quietos."),
  P("El agua del río y del lago es <b>dulce</b>."),
  IMG("Dónde hay agua", "Ríos, lagos y mares.", FG.tiras(["RÍO: CORRE", "LAGO: QUIETO", "MAR: SALADO Y GRANDE"], numeros=False, cols=1)),
 ]),
 S(1, "El mar", [
  D("Mar", "Agua <b>salada</b> y enorme, con olas."),
  P("El río <b>Paraná</b> corre por la Argentina. El mar <b>Argentino</b> moja la costa."),
  IMG("Dulce o salada", "Comparamos.", FG.nombres(["RÍO PARANÁ: DULCE", "MAR ARGENTINO: SALADA"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué es?", "Pensá en cada una.", FG.tiras(["1. CORRE Y TIENE AGUA DULCE", "2. TIENE OLAS Y AGUA SALADA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El río", "planteo": "¿Cómo es un río?", "pasos": ["Tiene agua dulce.", "El agua corre.", "Va hacia el mar."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El agua del mar es…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu lugar", "planteo": "¿Hay un río, lago o laguna cerca de donde vivís? ¿Cómo se llama?"},
"tip": {"titulo": "¿Dulce o salada?", "texto": "Solo el mar tiene agua salada."},
"ojo": ["El agua del mar no se toma.", "Cerca del agua, siempre con un adulto."],
"resumen": [{"titulo": "Río", "texto": "Corre, dulce."}, {"titulo": "Lago", "texto": "Quieto, dulce."}, {"titulo": "Mar", "texto": "Salado y grande."}],
"glosario": [{"palabra": "Agua dulce", "significado": "Agua sin sal."}, {"palabra": "Laguna", "significado": "Lago chiquito."}],
"carpeta": ["Leé la pista 1 y compará: ¿río o mar?", "Leé la pista 2 y compará: ¿río o mar?", "Tomi dice que el agua del río es salada. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("RÍO") + low("rio") + low("UN RÍO") + low("un rio") + low("EL RÍO") + low("el rio"), low("MAR") + low("EL MAR") + low("UN MAR"), NO],
"soluciones": {"incompleto": "SALADA.", "solo": "El nombre del lugar.", "carpeta": ["Un río.", "El mar.", "No: es dulce."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver cómo el agua vuelve al cielo.",
"vas_a_ver": ["El sol calienta", "El vapor sube", "Un ciclo"],
"secciones": [
 S(1, "El agua sube", [
  P("El <b>sol</b> calienta el agua del mar y de los charcos."),
  P("El agua se <b>evapora</b>: se hace vapor y <b>sube</b>."),
  P("Arriba hace frío: el vapor se <b>condensa</b> y forma <b>nubes</b>."),
  IMG("El ciclo del agua", "Siempre se repite.", FG.tiras(["1. EL SOL CALIENTA EL AGUA", "2. EL VAPOR SUBE", "3. SE FORMAN NUBES", "4. LLUEVE"], numeros=False)),
 ]),
 S(1, "Un ciclo", [
  D("Ciclo del agua", "El viaje del agua: sube, forma nubes, llueve y <b>vuelve a empezar</b>."),
  IMG("Para siempre", "El agua va y viene.", FG.nombres(["EVAPORA", "CONDENSA", "LLUEVE"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "Ordená el ciclo.", FG.tiras(["SE FORMAN NUBES", "EL SOL CALIENTA EL AGUA", "LLUEVE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El charco", "planteo": "¿Adónde va el charco al sol?", "pasos": ["El sol lo calienta.", "Se evapora.", "Sube y forma nubes."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Después de las nubes…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Dibujalo", "planteo": "Dibujá el ciclo del agua con flechas."},
"tip": {"titulo": "Un círculo", "texto": "El ciclo no termina: vuelve a empezar."},
"ojo": ["El agua no se pierde: viaja.", "El sol es el que empieza el ciclo."],
"resumen": [{"titulo": "Evapora", "texto": "El sol calienta."}, {"titulo": "Condensa", "texto": "Forma nubes."}, {"titulo": "Llueve", "texto": "Y vuelve a empezar."}],
"glosario": [{"palabra": "Ciclo", "significado": "Algo que se repite en círculo."}, {"palabra": "Evaporar", "significado": "Agua que se hace vapor."}],
"carpeta": ["De las tarjetas, ¿qué va primero?", "¿Qué va después de SE FORMAN NUBES?", "Tomi dice que el agua del charco se pierde para siempre. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("EL SOL CALIENTA EL AGUA") + low("EL SOL CALIENTA"), low("LLUEVE"), NO],
"soluciones": {"incompleto": "LLUEVE.", "solo": "Tu dibujo del ciclo.", "carpeta": ["El sol calienta el agua.", "Llueve.", "No: sube y vuelve a caer."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a medir cuánto llueve.",
"vas_a_ver": ["El pluviómetro", "Medir", "Anotar"],
"secciones": [
 S(1, "El pluviómetro", [
  D("Pluviómetro", "Un frasco que <b>junta la lluvia</b> para medir cuánto llovió."),
  P("Tomi arma uno con una <b>botella</b> cortada y una <b>regla</b>."),
  IMG("Mi pluviómetro", "Botella, regla y cinta.", FG.tiras(["1. CORTO UNA BOTELLA (CON UN ADULTO)", "2. PEGO UNA REGLA", "3. LO DEJO AFUERA", "4. MIDO DESPUÉS DE LLOVER"], numeros=False)),
 ]),
 S(1, "Anotar", [
  P("Después de cada lluvia, Tomi mira la regla y <b>anota</b>."),
  IMG("Lo que anotó Tomi", "Un día por renglón.", FG.ficha([("Lunes:", "2 cm"), ("Miércoles:", "5 cm"), ("Viernes:", "nada")], titulo="Mi pluviómetro")),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla de Tomi. La vas a usar en la carpeta."),
  IMG("¿Qué día llovió más?", "Compará los números.", FG.ficha([("Lunes:", "2 cm"), ("Miércoles:", "5 cm"), ("Viernes:", "nada")], titulo="Mi pluviómetro")),
 ]),
],
"ejemplo_completo": {"titulo": "Medir", "planteo": "¿Cuánto llovió el lunes?", "pasos": ["Miro el agua en la botella.", "Llega al 2 de la regla.", "Llovió 2 cm."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El viernes…", "pasos": ["…no ___ ."]},
"ejemplo_solo": {"titulo": "Tu pluviómetro", "planteo": "Con un adulto, armá tu pluviómetro y anotá la próxima lluvia."},
"tip": {"titulo": "Vaciá la botella", "texto": "Después de anotar, vaciala para la próxima."},
"ojo": ["El corte de la botella lo hace un adulto.", "Ponelo en un lugar abierto."],
"resumen": [{"titulo": "Pluviómetro", "texto": "Junta la lluvia."}, {"titulo": "Medir", "texto": "Con una regla."}, {"titulo": "Anotar", "texto": "Cada lluvia."}],
"glosario": [{"palabra": "Pluviómetro", "significado": "Frasco para medir la lluvia."}, {"palabra": "Medir", "significado": "Ver cuánto hay."}],
"carpeta": ["En la tabla de Tomi, ¿qué día llovió más?", "¿Qué día no llovió?", "Tomi dice que el lunes llovió más que el miércoles. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [low("MIÉRCOLES") + low("miercoles") + low("EL MIÉRCOLES") + low("el miercoles"), low("VIERNES") + low("EL VIERNES"), NO],
"soluciones": {"incompleto": "LLOVIÓ.", "solo": "Lo que anotaste.", "carpeta": ["El miércoles.", "El viernes.", "No: el miércoles llovió más."]},
}

ACT = {
"1": [ORD("ORDENÁ: CÓMO LLUEVE.", ["LLUEVE", "GOTITAS EN LA NUBE", "SE HACEN PESADAS"], ["GOTITAS EN LA NUBE", "SE HACEN PESADAS", "LLUEVE"], "PRIMERO LAS GOTITAS.", n="analizar"),
      TF("LAS NUBES SON DE GOTITAS DE AGUA.", "VERDADERO", "MUCHAS GOTITAS JUNTAS.", n="recordar")],
"2": [UNI("UNÍ CADA LUGAR CON CÓMO ES.", [("RÍO", "CORRE"), ("LAGO", "QUIETO"), ("MAR", "SALADO")], "CADA UNO ES DISTINTO.", n="analizar"),
      MC("¿DÓNDE HAY AGUA SALADA?", ["EN EL MAR", "EN EL RÍO"], "EN EL MAR", "SOLO EL MAR ES SALADO.", n="aplicar")],
"3": [ORD("ORDENÁ EL CICLO.", ["SE FORMAN NUBES", "LLUEVE", "EL SOL CALIENTA EL AGUA"], ["EL SOL CALIENTA EL AGUA", "SE FORMAN NUBES", "LLUEVE"], "EMPIEZA EL SOL.", n="analizar"),
      TF("EL AGUA DEL CHARCO SE PIERDE PARA SIEMPRE.", "FALSO", "SUBE Y VUELVE A CAER.", n="error")],
"4": [MC("¿PARA QUÉ SIRVE EL PLUVIÓMETRO?", ["PARA MEDIR LA LLUVIA", "PARA REGAR"], "PARA MEDIR LA LLUVIA", "JUNTA EL AGUA.", n="recordar"),
      SA("LUNES 2 CM, MIÉRCOLES 5 CM. ¿QUÉ DÍA LLOVIÓ MÁS?", low("MIÉRCOLES") + low("miercoles") + low("EL MIÉRCOLES") + low("el miercoles"), "EL MIÉRCOLES.", n="analizar")],
"5": [MC("RELÁMPAGO. LA LLUVIA CAE DE…", ["LAS NUBES", "LOS ÁRBOLES"], "LAS NUBES", "GOTITAS QUE CAEN.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL MAR ES…", ["SALADO", "DULCE"], "SALADO", "AGUA SALADA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL CICLO EMPIEZA CON…", ["EL SOL", "LA LUNA"], "EL SOL", "CALIENTA EL AGUA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA LLUVIA SE MIDE CON…", ["PLUVIÓMETRO", "TERMÓMETRO"], "PLUVIÓMETRO", "JUNTA LA LLUVIA.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ HAY EN UNA NUBE?", ["GOTITAS DE AGUA", "ALGODÓN"], "GOTITAS DE AGUA", "MUCHAS JUNTAS.", n="recordar")],
 [1, SA("SI HACE MUCHO FRÍO, EL AGUA CAE COMO NIEVE O…", low("GRANIZO") + low("EL GRANIZO"), "GRANIZO.", n="aplicar")],
 [1, TF("LAS NUBES GRISES PUEDEN TRAER LLUVIA.", "VERDADERO", "ESTÁN LLENAS DE GOTITAS.", n="recordar")],
 [2, MC("¿CÓMO ES EL AGUA DEL RÍO?", ["DULCE", "SALADA"], "DULCE", "SOLO EL MAR ES SALADO.", n="aplicar")],
 [2, UNI("UNÍ CADA UNO.", [("RÍO PARANÁ", "AGUA DULCE"), ("MAR ARGENTINO", "AGUA SALADA")], "DULCE O SALADA.", n="analizar")],
 [2, TF("SE PUEDE TOMAR AGUA DEL MAR.", "FALSO", "ES SALADA.", n="error")],
 [3, ORD("ORDENÁ EL CICLO.", ["LLUEVE", "EL VAPOR SUBE", "SE FORMAN NUBES"], ["EL VAPOR SUBE", "SE FORMAN NUBES", "LLUEVE"], "SUBE, NUBES, LLUVIA.", n="analizar")],
 [3, SA("¿QUÉ CALIENTA EL AGUA PARA QUE SUBA?", low("EL SOL") + low("SOL"), "EL SOL.", n="recordar")],
 [3, MC("¿EL CICLO DEL AGUA TERMINA?", ["NO, VUELVE A EMPEZAR", "SÍ, UNA VEZ Y LISTO"], "NO, VUELVE A EMPEZAR", "ES UN CÍRCULO.", n="aplicar")],
 [4, MC("¿CON QUÉ SE ARMA UN PLUVIÓMETRO CASERO?", ["BOTELLA Y REGLA", "PELOTA Y SOGA"], "BOTELLA Y REGLA", "JUNTA Y MIDE.", n="recordar")],
 [4, SA("MARTES 3 CM, JUEVES 1 CM. ¿QUÉ DÍA LLOVIÓ MENOS?", low("JUEVES") + low("EL JUEVES"), "EL JUEVES.", n="analizar")],
 [4, TF("DESPUÉS DE MEDIR, HAY QUE VACIAR LA BOTELLA.", "VERDADERO", "PARA LA PRÓXIMA LLUVIA.", n="aplicar")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: el ciclo del agua", "examen_titulo": "Nivel jefe: el ciclo del agua",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
