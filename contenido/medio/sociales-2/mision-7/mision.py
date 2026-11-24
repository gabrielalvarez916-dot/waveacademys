# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 7 · Conflictos del pasado. Genera mision-7.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy investiga desacuerdos de antes y de hoy).
VARIANTE: lleva su parte "neutro" para alumnos de otros países.
Niveles: 1 conflictos por un territorio · 2 reclamos de los trabajadores · 3 cómo se resolvía antes · 4 cómo resolvemos hoy."""
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
"objetivo": "Vas a conocer conflictos por las tierras.",
"vas_a_ver": ["Qué es un conflicto", "Un territorio", "Dos grupos que querían lo mismo"],
"secciones": [
 S(1, "Un conflicto", [
  D("Conflicto", "Dos personas o grupos que <b>no están de acuerdo</b>."),
  P("Los conflictos pasan en la escuela, en la familia y entre pueblos."),
  P("Lola investiga conflictos de hace mucho tiempo. ¡Y cómo se resolvían!"),
  IMG("Conflictos de todos los días", "Pequeños y grandes.", FG.tiras(["DOS CHICOS QUIEREN LA MISMA PELOTA", "DOS VECINOS QUIEREN EL MISMO LUGAR", "DOS PUEBLOS QUIEREN LA MISMA TIERRA"], numeros=False, cols=1)),
 ]),
 S(1, "El territorio", [
  D("Territorio", "La tierra que un grupo usa para vivir y sembrar."),
  {**P("Hace mucho tiempo, aquí vivían los <b>pueblos originarios</b>. Cazaban, sembraban y tenían sus casas."), "neutro": {"texto": "Hace mucho tiempo, en América vivían los <b>pueblos originarios</b>. Cazaban, sembraban y tenían sus casas."}},
  P("Cuando llegaron los españoles, quisieron esas mismas tierras. Hubo <b>luchas</b> y muchos pueblos perdieron su lugar."),
  IMG("Querían lo mismo", "Un conflicto por la tierra.", FG.nombres(["PUEBLOS ORIGINARIOS", "TIERRA", "ESPAÑOLES"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Hay conflicto?", "Pensá en cada una.", FG.tiras(["1. DOS GRUPOS QUIEREN EL MISMO CAMPO", "2. TODOS JUEGAN JUNTOS Y CONTENTOS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La pelota", "planteo": "Ana y Luis quieren la misma pelota.", "pasos": ["Los dos la quieren usar.", "No se ponen de acuerdo.", "¡Es un conflicto!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El lugar de tierra que usa un grupo es su…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "Contá un desacuerdo que tuviste con un amigo."},
"tip": {"titulo": "¿Quieren lo mismo?", "texto": "Si dos quieren lo mismo, puede haber conflicto."},
"ojo": ["Los pueblos originarios vivían aquí antes.", "Un conflicto no siempre termina en pelea."],
"resumen": [{"titulo": "Conflicto", "texto": "No estar de acuerdo."}, {"titulo": "Territorio", "texto": "Tierra para vivir."}, {"titulo": "Antes", "texto": "Hubo luchas por la tierra."}],
"glosario": [{"palabra": "Conflicto", "significado": "Desacuerdo entre personas o grupos."}, {"palabra": "Territorio", "significado": "Tierra que usa un grupo."}],
"carpeta": ["En la tarjeta 1, ¿hay conflicto? ¿Por qué?", "En la tarjeta 2, ¿hay conflicto?", "Lola dice que antes nadie vivía en estas tierras. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [low("SÍ") + low("si") + low("SÍ, QUIEREN LO MISMO") + low("si, quieren lo mismo"), NO, NO],
"soluciones": {"incompleto": "TERRITORIO.", "solo": "Tu desacuerdo.", "carpeta": ["Sí: quieren lo mismo.", "No.", "No: vivían los pueblos originarios."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer los reclamos de los trabajadores.",
"vas_a_ver": ["Qué es un reclamo", "La huelga", "Lo que pedían"],
"secciones": [
 S(1, "Los reclamos", [
  D("Reclamo", "Pedir algo que es justo y no se está cumpliendo."),
  P("Hace mucho tiempo, muchos trabajadores trabajaban muchas horas por poco dinero."),
  P("No tenían descanso ni vacaciones. Por eso, empezaron a <b>reclamar</b>."),
  IMG("Lo que pedían", "Reclamos justos.", FG.tiras(["MENOS HORAS DE TRABAJO", "UN PAGO JUSTO", "DÍAS DE DESCANSO"], numeros=False, cols=1)),
 ]),
 S(1, "La huelga", [
  D("Huelga", "Cuando los trabajadores <b>dejan de trabajar</b> todos juntos para reclamar."),
  P("Se juntaban en un <b>sindicato</b>. Hacían carteles y marchaban por la calle."),
  P("Así, de a poco, consiguieron leyes que los cuidan."),
  IMG("Para reclamar", "Juntos se escucha más.", FG.nombres(["CARTELES", "SINDICATO", "MARCHA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué es?", "Pensá en cada pista.", FG.tiras(["1. DEJAN DE TRABAJAR TODOS JUNTOS", "2. GRUPO DE TRABAJADORES QUE SE UNEN"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Un reclamo", "planteo": "Los obreros de una fábrica trabajan todo el día.", "pasos": ["Se juntan en el sindicato.", "Piden menos horas.", "Hacen huelga hasta que los escuchan."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cuando dejan de trabajar todos juntos, hacen una…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntale a un adulto si alguna vez reclamó algo en su trabajo."},
"tip": {"titulo": "Juntos", "texto": "Un reclamo de muchos se escucha más."},
"ojo": ["Reclamar lo justo es un derecho.", "Se reclama sin lastimar a nadie."],
"resumen": [{"titulo": "Reclamo", "texto": "Pedir lo justo."}, {"titulo": "Huelga", "texto": "Dejar de trabajar juntos."}, {"titulo": "Sindicato", "texto": "Trabajadores unidos."}],
"glosario": [{"palabra": "Sindicato", "significado": "Grupo de trabajadores que se unen."}, {"palabra": "Obrero", "significado": "Persona que trabaja en una fábrica."}],
"carpeta": ["Leé la pista 1 y compará: ¿huelga o sindicato?", "Leé la pista 2 y compará: ¿huelga o sindicato?", "Lola dice que los trabajadores de antes tenían vacaciones. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("HUELGA") + low("UNA HUELGA") + low("LA HUELGA"), low("SINDICATO") + low("UN SINDICATO") + low("EL SINDICATO"), NO],
"soluciones": {"incompleto": "HUELGA.", "solo": "Lo que te contaron.", "carpeta": ["Una huelga.", "Un sindicato.", "No: no tenían descanso."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver cómo se resolvían los conflictos antes.",
"vas_a_ver": ["El más fuerte", "El que mandaba", "Sin escuchar a todos"],
"secciones": [
 S(1, "Antes", [
  P("Hace mucho tiempo, muchos conflictos se resolvían con <b>peleas</b> o guerras."),
  P("Muchas veces ganaba el <b>más fuerte</b>, aunque no tuviera razón."),
  {**P("Otras veces decidía el <b>rey</b> o un jefe, sin preguntar a nadie."), "neutro": {"texto": "Otras veces decidía un <b>rey</b> o un jefe, sin preguntar a nadie."}},
  IMG("Cómo se resolvía antes", "No siempre era justo.", FG.tiras(["CON PELEAS", "GANABA EL MÁS FUERTE", "DECIDÍA EL QUE MANDABA"], numeros=False, cols=1)),
 ]),
 S(1, "No era justo", [
  P("Las mujeres, los pobres y los pueblos originarios casi <b>no podían opinar</b>."),
  P("Sus ideas no se escuchaban. Por eso muchas soluciones eran <b>injustas</b>."),
  IMG("Los que no opinaban", "Hoy todos opinamos.", FG.nombres(["MUJERES", "POBRES", "PUEBLOS ORIGINARIOS"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Era justo?", "Pensá en cada una.", FG.tiras(["1. GANA EL MÁS FUERTE AUNQUE NO TENGA RAZÓN", "2. SE ESCUCHA A TODOS ANTES DE DECIDIR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Un conflicto de antes", "planteo": "Dos grupos querían un río.", "pasos": ["No hablaron.", "Se pelearon.", "Ganó el más fuerte."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Antes, muchas veces ganaba el más…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Te parece justo que gane el más fuerte? ¿Por qué?"},
"tip": {"titulo": "¿Escucharon a todos?", "texto": "Si no, la solución no era justa."},
"ojo": ["La fuerza no da la razón.", "Antes, muchos no podían opinar."],
"resumen": [{"titulo": "Peleas", "texto": "Así se resolvía."}, {"titulo": "El más fuerte", "texto": "Muchas veces ganaba."}, {"titulo": "Injusto", "texto": "No opinaban todos."}],
"glosario": [{"palabra": "Guerra", "significado": "Lucha entre pueblos o países."}, {"palabra": "Injusto", "significado": "Que no es justo."}],
"carpeta": ["¿La tarjeta 1 es justa o injusta?", "¿Y la tarjeta 2?", "Lola dice que ganar por ser fuerte da la razón. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("INJUSTA") + low("ES INJUSTA") + low("INJUSTO"), low("JUSTA") + low("ES JUSTA") + low("JUSTO"), NO],
"soluciones": {"incompleto": "FUERTE.", "solo": "Tu opinión.", "carpeta": ["Injusta.", "Justa.", "No: la fuerza no da la razón."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a aprender a resolver conflictos hoy.",
"vas_a_ver": ["Hablar y escuchar", "Llegar a un acuerdo", "Votar"],
"secciones": [
 S(1, "Hablar y escuchar", [
  P("Hoy resolvemos los conflictos <b>hablando</b>. Cada uno dice lo que quiere."),
  P("Después <b>escuchamos</b> al otro, sin interrumpir."),
  D("Acuerdo", "Cuando todos aceptan una solución <b>después de hablar</b>."),
  IMG("Para resolver un conflicto", "Paso a paso.", FG.tiras(["1. DIGO LO QUE PASA", "2. ESCUCHO AL OTRO", "3. BUSCAMOS IDEAS", "4. HACEMOS UN ACUERDO"], numeros=False)),
 ]),
 S(1, "Votar", [
  P("Si somos muchos, podemos <b>votar</b>. Gana la idea que eligen más personas."),
  P("También hay leyes y jueces que ayudan a resolver conflictos grandes."),
  IMG("Formas de resolver", "Sin pelear.", FG.nombres(["DIÁLOGO", "ACUERDO", "VOTACIÓN"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Qué va primero?", FG.tiras(["HACEMOS UN ACUERDO", "DIGO LO QUE PASA", "ESCUCHO AL OTRO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El recreo", "planteo": "Medio grado quiere fútbol y medio quiere mancha.", "pasos": ["Cada grupo explica qué quiere.", "Escuchan al otro grupo.", "Acuerdan: un recreo cada juego."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cuando todos aceptan una solución, hay un…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "La próxima vez que discutas, probá hablar y escuchar."},
"tip": {"titulo": "Turnos", "texto": "Uno habla y el otro escucha."},
"ojo": ["Pelear no resuelve el conflicto.", "Todas las opiniones valen."],
"resumen": [{"titulo": "Hablar", "texto": "Digo lo que pasa."}, {"titulo": "Escuchar", "texto": "Sin interrumpir."}, {"titulo": "Acuerdo o votación", "texto": "Para decidir."}],
"glosario": [{"palabra": "Votar", "significado": "Elegir una idea entre varias."}, {"palabra": "Diálogo", "significado": "Hablar y escuchar por turnos."}],
"carpeta": ["De las tarjetas, ¿qué va primero?", "¿Qué va al final?", "Lola dice que la mejor forma de resolver es pelear. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("DIGO LO QUE PASA") + low("DECIR LO QUE PASA"), low("HACEMOS UN ACUERDO") + low("UN ACUERDO") + low("EL ACUERDO"), NO],
"soluciones": {"incompleto": "ACUERDO.", "solo": "Cómo te fue.", "carpeta": ["Digo lo que pasa.", "Hacemos un acuerdo.", "No: hablando y escuchando."]},
}

ACT = {
"1": [MC("ANA Y LUIS QUIEREN USAR LA MISMA HAMACA A LA VEZ. ¿QUÉ PASA?", ["HAY UN CONFLICTO", "NO PASA NADA"], "HAY UN CONFLICTO", "QUIEREN LO MISMO.", n="aplicar", neutro={"p": "ANA Y LUIS QUIEREN USAR LA MISMA HAMACA A LA VEZ. ¿QUÉ PASA?"}),
      TF("SOFÍA DICE QUE ANTES NADIE VIVÍA EN ESTAS TIERRAS.", "FALSO", "VIVÍAN LOS PUEBLOS ORIGINARIOS.", n="error")],
"2": [UNI("UNÍ CADA PALABRA.", [("HUELGA", "DEJAR DE TRABAJAR"), ("SINDICATO", "TRABAJADORES UNIDOS"), ("RECLAMO", "PEDIR LO JUSTO")], "PENSÁ EN LOS TRABAJADORES.", n="analizar"),
      MC("UNOS OBREROS TRABAJAN TODO EL DÍA SIN DESCANSO. ¿QUÉ PUEDEN HACER?", ["RECLAMAR JUNTOS", "QUEDARSE CALLADOS"], "RECLAMAR JUNTOS", "ES SU DERECHO.", n="aplicar")],
"3": [MC("ANTES, DOS GRUPOS QUERÍAN UN RÍO Y SE PELEARON. ¿QUIÉN GANABA?", ["EL MÁS FUERTE", "EL QUE TENÍA RAZÓN"], "EL MÁS FUERTE", "NO SIEMPRE ERA JUSTO.", n="analizar"),
      TF("MARCOS DICE QUE ANTES TODOS PODÍAN OPINAR.", "FALSO", "MUCHOS NO PODÍAN.", n="error")],
"4": [ORD("ORDENÁ: CÓMO RESOLVEMOS UN CONFLICTO.", ["HACEMOS UN ACUERDO", "DIGO LO QUE PASA", "ESCUCHO AL OTRO"], ["DIGO LO QUE PASA", "ESCUCHO AL OTRO", "HACEMOS UN ACUERDO"], "PRIMERO HABLO.", n="analizar"),
      MC("EL GRADO NO SE PONE DE ACUERDO EN EL NOMBRE DEL EQUIPO. ¿QUÉ HACEN?", ["VOTAN", "SE PELEAN"], "VOTAN", "GANA LA IDEA MÁS ELEGIDA.", n="aplicar")],
"5": [MC("RELÁMPAGO. NO ESTAR DE ACUERDO ES UN…", ["CONFLICTO", "JUEGO"], "CONFLICTO", "QUIEREN COSAS DISTINTAS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. DEJAR DE TRABAJAR JUNTOS ES…", ["HUELGA", "VACACIONES"], "HUELGA", "PARA RECLAMAR.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ANTES, MUCHAS VECES GANABA…", ["EL MÁS FUERTE", "EL MÁS CHICO"], "EL MÁS FUERTE", "NO ERA JUSTO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. HOY RESOLVEMOS…", ["HABLANDO", "PELEANDO"], "HABLANDO", "Y ESCUCHANDO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UN CONFLICTO?", ["UN DESACUERDO", "UNA FIESTA"], "UN DESACUERDO", "QUIEREN COSAS DISTINTAS.", n="recordar")],
 [1, MC("LOS ESPAÑOLES QUERÍAN LAS TIERRAS DE LOS PUEBLOS ORIGINARIOS. ¿QUÉ HUBO?", ["UN CONFLICTO", "UN ACUERDO DE TODOS"], "UN CONFLICTO", "HUBO LUCHAS.", n="analizar")],
 [1, TF("TOMÁS DICE QUE UN CONFLICTO SIEMPRE TERMINA EN PELEA.", "FALSO", "SE PUEDE RESOLVER HABLANDO.", n="error")],
 [2, MC("¿QUÉ ES UN SINDICATO?", ["TRABAJADORES UNIDOS", "UNA FÁBRICA"], "TRABAJADORES UNIDOS", "RECLAMAN JUNTOS.", n="recordar")],
 [2, SA("LOS TRABAJADORES DEJAN DE TRABAJAR JUNTOS PARA RECLAMAR. ¿CÓMO SE LLAMA?", low("HUELGA") + low("UNA HUELGA") + low("LA HUELGA") + low("PARO") + low("UN PARO"), "HUELGA.", n="aplicar")],
 [2, TF("LUCÍA DICE QUE LOS TRABAJADORES DE ANTES TENÍAN VACACIONES.", "FALSO", "NO TENÍAN DESCANSO.", n="error")],
 [3, UNI("UNÍ: ¿ANTES O HOY?", [("GANABA EL MÁS FUERTE", "ANTES"), ("SE VOTA", "HOY")], "COMPARÁ.", n="analizar")],
 [3, MC("ANTES DECIDÍA SOLO EL REY. ¿ESO ERA JUSTO PARA TODOS?", ["NO, NO ESCUCHABA A TODOS", "SÍ, SIEMPRE"], "NO, NO ESCUCHABA A TODOS", "MUCHOS NO OPINABAN.", n="analizar", neutro={"p": "ANTES DECIDÍA SOLO UN JEFE. ¿ESO ERA JUSTO PARA TODOS?"})],
 [3, TF("ANTES LAS MUJERES CASI NO PODÍAN OPINAR.", "VERDADERO", "HOY SÍ OPINAN.", n="recordar")],
 [4, ORD("ORDENÁ: EL CONFLICTO DEL RECREO.", ["ACUERDAN", "CADA GRUPO EXPLICA", "SE ESCUCHAN"], ["CADA GRUPO EXPLICA", "SE ESCUCHAN", "ACUERDAN"], "PRIMERO HABLAN.", n="analizar")],
 [4, SA("CUANDO TODOS ACEPTAN UNA SOLUCIÓN DESPUÉS DE HABLAR, HAY UN…", low("ACUERDO") + low("UN ACUERDO"), "UN ACUERDO.", n="aplicar")],
 [4, TF("JUAN DICE QUE PELEAR ES LA MEJOR FORMA DE RESOLVER.", "FALSO", "HABLAR Y ESCUCHAR ES MEJOR.", n="error")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: conflictos del pasado", "examen_titulo": "Nivel jefe: conflictos del pasado",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
