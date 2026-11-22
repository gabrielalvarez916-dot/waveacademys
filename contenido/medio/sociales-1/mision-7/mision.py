# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 7 · Servicios que llegan a casa. Genera mision-7.json.
Regla de primeros años. Metáfora: los caminos invisibles que llegan a casa.
Niveles: 1 la luz y el gas en mi casa · 2 el recorrido de la basura · 3 cartero, bomberos y policía · 4 quiénes trabajan en los servicios."""
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
"objetivo": "Vas a conocer la luz y el gas de tu casa.",
"vas_a_ver": ["Qué es un servicio", "La luz", "El gas"],
"secciones": [
 S(1, "Los servicios", [
  D("Servicio", "Algo que llega a las casas para que vivamos mejor."),
  P("La <b>luz</b>, el <b>gas</b> y el <b>agua</b> llegan por cables y caños."),
  IMG("Llegan a casa", "Tres servicios.", FG.tiras(["LUZ: POR CABLES", "GAS: POR CAÑOS", "AGUA: POR CAÑOS"], numeros=False, cols=3)),
 ]),
 S(1, "Para qué sirven", [
  P("La luz prende la <b>lámpara</b> y la <b>heladera</b>. El gas prende la <b>cocina</b>."),
  IMG("Sirven para", "En casa.", FG.tiras(["LUZ: LÁMPARA, HELADERA", "GAS: COCINA, ESTUFA"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los objetos. Los vas a usar en la carpeta."),
  IMG("¿Luz o gas?", "Pensá.", FG.nombres(["TELE", "COCINA", "HELADERA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Se cortó la luz", "planteo": "En casa de Tomi.", "pasos": ["No anda la lámpara.", "No anda la tele.", "Prenden una vela con un adulto."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La cocina funciona con…", "pasos": ["La cocina funciona con ___."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "Buscá en casa 3 cosas que usan luz."},
"tip": {"titulo": "Cuidar la luz", "texto": "Apagá la luz cuando salís de un lugar."},
"ojo": ["Los enchufes no se tocan con las manos mojadas.", "Si hay olor a gas, avisá enseguida a un adulto."],
"resumen": [{"titulo": "Servicio", "texto": "Llega a casa."}, {"titulo": "Luz", "texto": "Por cables."}, {"titulo": "Gas", "texto": "Por caños."}],
"glosario": [{"palabra": "Servicio", "significado": "Algo que llega a las casas para vivir mejor."}, {"palabra": "Caño", "significado": "Tubo por donde pasa agua o gas."}],
"carpeta": ["La tele, ¿funciona con luz o con gas?", "La cocina, ¿funciona con luz o con gas?", "Hay olor a gas. ¿Qué hacés?"],
"respuestas_carpeta": [acepta("LUZ", "CON LUZ"), acepta("GAS", "CON GAS"), acepta("AVISO A UN ADULTO", "AVISAR A UN ADULTO", "LE AVISO A UN ADULTO", "AVISO", "AVISO A MI MAMÁ", "AVISO A MI PAPÁ")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "GAS.", "solo": "Por ejemplo: lámpara, tele, heladera.", "carpeta": ["LUZ.", "GAS.", "AVISO A UN ADULTO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer el recorrido de la basura.",
"vas_a_ver": ["Del tacho a la vereda", "El camión", "Reciclar"],
"secciones": [
 S(1, "El recorrido", [
  P("Va al <b>tacho</b>, a la <b>vereda</b> y al <b>camión</b>."),
  IMG("El recorrido", "Paso a paso.", FG.tiras(["TACHO", "BOLSA EN LA VEREDA", "CAMIÓN", "PLANTA"], numeros=True, cols=2)),
 ]),
 S(1, "Reciclar", [
  D("Reciclar", "Usar la basura para hacer cosas nuevas."),
  P("Separamos <b>papel</b>, <b>plástico</b> y <b>vidrio</b> para reciclar."),
  IMG("Separamos", "Cada uno en su lugar.", FG.tiras(["PAPEL", "PLÁSTICO", "VIDRIO", "RESTOS DE COMIDA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la basura. La vas a usar en la carpeta."),
  IMG("¿Se recicla?", "Pensá.", FG.nombres(["BOTELLA", "DIARIO", "CÁSCARA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La botella", "planteo": "Sofi toma agua.", "pasos": ["Tira la botella al tacho de plástico.", "El camión la lleva.", "Con ella hacen otra cosa."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La basura la lleva el…", "pasos": ["La basura la lleva el ___."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "Ayudá a separar la basura en casa."},
"tip": {"titulo": "Separá", "texto": "Si separás, se puede reciclar más."},
"ojo": ["Sacá la basura a la hora en que pasa el camión.", "No toques vidrios rotos."],
"resumen": [{"titulo": "Recorrido", "texto": "Tacho, vereda, camión."}, {"titulo": "Separar", "texto": "Papel, plástico, vidrio."}, {"titulo": "Reciclar", "texto": "Cosas nuevas."}],
"glosario": [{"palabra": "Reciclar", "significado": "Hacer cosas nuevas con basura."}, {"palabra": "Recolector", "significado": "Persona que junta la basura."}],
"carpeta": ["La botella, ¿se recicla?", "El diario, ¿se recicla?", "¿Quién lleva la basura de la vereda?"],
"respuestas_carpeta": [acepta("SÍ", "SI"), acepta("SÍ", "SI"), acepta("CAMIÓN", "CAMION", "EL CAMIÓN", "EL RECOLECTOR", "RECOLECTOR", "LOS RECOLECTORES")],
"carpeta_nivel": ["aplicar", "aplicar", "recordar"],
"soluciones": {"incompleto": "CAMIÓN.", "solo": "Lo hiciste en tu casa.", "carpeta": ["SÍ.", "SÍ.", "EL CAMIÓN."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer al cartero, los bomberos y la policía.",
"vas_a_ver": ["El cartero", "Los bomberos", "La policía"],
"secciones": [
 S(1, "Nos ayudan", [
  D("Servicio público", "Trabajo que ayuda a todas las personas."),
  P("El <b>cartero</b> trae cartas. Los <b>bomberos</b> apagan incendios. La <b>policía</b> cuida."),
  IMG("Nos ayudan", "Cada uno a su modo.", FG.tiras(["CARTERO: CARTAS", "BOMBEROS: FUEGO", "POLICÍA: CUIDA"], numeros=False, cols=3)),
 ]),
 S(1, "En una emergencia", [
  P("Si hay un incendio, un <b>adulto</b> llama a los bomberos."),
  IMG("Emergencia", "Paso a paso.", FG.tiras(["VEO FUEGO", "AVISO A UN ADULTO", "LLAMA A BOMBEROS"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los casos. Los vas a usar en la carpeta."),
  IMG("¿Quién ayuda?", "Pensá.", FG.tiras(["LLEGA UN PAQUETE", "SE QUEMA UN PASTIZAL", "ME PERDÍ EN LA PLAZA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Una carta", "planteo": "La abuela le escribe a Sofi.", "pasos": ["Pone la carta en el correo.", "El cartero la lleva.", "Sofi la recibe."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los bomberos…", "pasos": ["Apagan el ___."]},
"ejemplo_solo": {"titulo": "Dibujá", "planteo": "Dibujá a una persona que ayuda en tu barrio."},
"tip": {"titulo": "Perdido", "texto": "Si te perdés, buscá a un policía."},
"ojo": ["No se juega con fuego.", "En una emergencia, avisá enseguida a un adulto."],
"resumen": [{"titulo": "Cartero", "texto": "Trae cartas."}, {"titulo": "Bomberos", "texto": "Apagan fuego."}, {"titulo": "Policía", "texto": "Cuida."}],
"glosario": [{"palabra": "Emergencia", "significado": "Algo peligroso que pasa de golpe."}, {"palabra": "Correo", "significado": "Lugar donde se mandan cartas."}],
"carpeta": ["Llega un paquete. ¿Quién lo trae?", "Se quema un pastizal. ¿Quién ayuda?", "Me perdí en la plaza. ¿A quién busco?"],
"respuestas_carpeta": [acepta("CARTERO", "EL CARTERO", "CARTERA", "LA CARTERA"), acepta("BOMBEROS", "LOS BOMBEROS"), acepta("POLICÍA", "POLICIA", "A UN POLICÍA", "A UN POLICIA", "UN POLICÍA", "UN ADULTO", "A UN ADULTO")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "FUEGO.", "solo": "Tu dibujo.", "carpeta": ["EL CARTERO.", "LOS BOMBEROS.", "A UN POLICÍA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer a quienes trabajan en los servicios.",
"vas_a_ver": ["Muchos trabajos", "Trabajan de noche", "Les agradecemos"],
"secciones": [
 S(1, "Muchos trabajos", [
  P("Trabajan <b>electricistas</b>, <b>gasistas</b>, <b>recolectores</b> y <b>carteros</b>."),
  IMG("Trabajan", "Para que todo funcione.", FG.tiras(["ELECTRICISTA: LUZ", "GASISTA: GAS", "RECOLECTOR: BASURA", "CARTERO: CARTAS"], numeros=False, cols=2)),
 ]),
 S(1, "Día y noche", [
  D("Turno", "Horario en que trabaja una persona."),
  P("Muchos trabajan de <b>noche</b> mientras dormimos."),
  IMG("El recolector", "Su noche.", FG.tiras(["SALE DE NOCHE", "RECORRE EL BARRIO", "DESCARGA LA BASURA", "VUELVE A CASA"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los problemas. Los vas a usar en la carpeta."),
  IMG("¿A quién llamamos?", "Pensá.", FG.tiras(["NO HAY LUZ EN CASA", "LA COCINA PIERDE GAS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Se cortó la luz", "planteo": "En el barrio no hay luz.", "pasos": ["Viene el electricista.", "Arregla el cable.", "¡Vuelve la luz!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El gasista arregla…", "pasos": ["El ___."]},
"ejemplo_solo": {"titulo": "Agradecé", "planteo": "Escribí GRACIAS en un cartel para el recolector."},
"tip": {"titulo": "Saludá", "texto": "Saludá a quienes trabajan en tu barrio."},
"ojo": ["Solo un adulto llama al electricista o al gasista.", "Todos los trabajos son importantes."],
"resumen": [{"titulo": "Trabajos", "texto": "Electricista, gasista, recolector."}, {"titulo": "Turnos", "texto": "Día y noche."}, {"titulo": "Gracias", "texto": "Nos ayudan a todos."}],
"glosario": [{"palabra": "Electricista", "significado": "Arregla la luz."}, {"palabra": "Gasista", "significado": "Arregla el gas."}],
"carpeta": ["No hay luz en casa. ¿Quién la arregla?", "La cocina pierde gas. ¿Quién la arregla?", "¿Cuándo trabaja el recolector?"],
"respuestas_carpeta": [acepta("ELECTRICISTA", "EL ELECTRICISTA"), acepta("GASISTA", "EL GASISTA"), acepta("DE NOCHE", "NOCHE", "A LA NOCHE")],
"carpeta_nivel": ["aplicar", "aplicar", "recordar"],
"soluciones": {"incompleto": "GAS.", "solo": "Tu cartel.", "carpeta": ["EL ELECTRICISTA.", "EL GASISTA.", "DE NOCHE."]},
}

ACT = {
"1": [MC("¿QUÉ SERVICIO PRENDE LA LÁMPARA?", ["LA LUZ", "EL GAS", "EL AGUA"], "LA LUZ", "LA LUZ LLEGA POR CABLES.", n="aplicar"),
      MC("TOMI TOCA EL ENCHUFE CON LAS MANOS MOJADAS. ¿QUÉ ESTÁ MAL?", ["ES PELIGROSO", "NADA", "SE MOJA EL ENCHUFE"], "ES PELIGROSO", "NUNCA CON MANOS MOJADAS.", n="error")],
"2": [ORD("ORDENÁ EL RECORRIDO DE LA BASURA.", ["CAMIÓN", "TACHO", "VEREDA"], ["TACHO", "VEREDA", "CAMIÓN"], "TACHO, VEREDA, CAMIÓN.", n="aplicar"),
      MC("¿POR QUÉ SEPARAMOS LA BASURA?", ["PARA RECICLAR", "PARA ENSUCIAR", "PARA JUGAR"], "PARA RECICLAR", "ASÍ SE HACEN COSAS NUEVAS.", n="analizar")],
"3": [MC("¿QUIÉN APAGA INCENDIOS?", ["LOS BOMBEROS", "EL CARTERO", "EL PANADERO"], "LOS BOMBEROS", "APAGAN EL FUEGO.", n="recordar"),
      MC("TE PERDISTE EN LA PLAZA. ¿QUÉ HACÉS?", ["BUSCO A UN POLICÍA", "ME VOY CON UN DESCONOCIDO", "ME ESCONDO"], "BUSCO A UN POLICÍA", "O A UN ADULTO DE CONFIANZA.", n="aplicar")],
"4": [MC("¿QUIÉN ARREGLA LA LUZ?", ["ELECTRICISTA", "GASISTA", "CARTERO"], "ELECTRICISTA", "ARREGLA LA LUZ.", n="recordar"),
      MC("¿POR QUÉ EL RECOLECTOR TRABAJA DE NOCHE?", ["HAY MENOS AUTOS", "LE GUSTA LA LUNA", "NO HAY BASURA DE DÍA"], "HAY MENOS AUTOS", "ASÍ RECORRE MÁS RÁPIDO.", n="analizar")],
"5": [MC("RELÁMPAGO. EL GAS LLEGA POR…", ["CAÑOS", "CABLES", "CARTAS"], "CAÑOS", "POR CAÑOS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ SE RECICLA?", ["BOTELLA", "CÁSCARA", "TIERRA"], "BOTELLA", "PLÁSTICO.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. ¿QUIÉN TRAE LAS CARTAS?", acepta("CARTERO", "EL CARTERO"), "EL CARTERO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUIÉN ARREGLA EL GAS?", ["GASISTA", "BOMBERO", "MAESTRA"], "GASISTA", "EL GASISTA.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("UN SERVICIO ES…", ["ALGO QUE LLEGA A LAS CASAS", "UN JUGUETE NUEVO", "UNA COMIDA RICA"], "ALGO QUE LLEGA A LAS CASAS", "LUZ, GAS, AGUA.", n="recordar")],
 [1, MC("¿QUÉ SERVICIO USA LA COCINA?", ["GAS", "LUZ", "TELÉFONO"], "GAS", "LA COCINA USA GAS.", n="aplicar")],
 [1, MC("HAY OLOR A GAS EN CASA. ¿QUÉ HACÉS?", ["AVISO A UN ADULTO", "PRENDO UN FÓSFORO", "ME QUEDO QUIETO"], "AVISO A UN ADULTO", "ES PELIGROSO.", n="aplicar")],
 [2, ORD("ORDENÁ EL RECORRIDO DE LA BASURA.", ["PLANTA", "CAMIÓN", "TACHO", "VEREDA"], ["TACHO", "VEREDA", "CAMIÓN", "PLANTA"], "DE CASA A LA PLANTA.", n="aplicar")],
 [2, MC("RECICLAR ES…", ["HACER COSAS NUEVAS CON BASURA", "TIRAR TODO JUNTO", "QUEMAR LA BASURA"], "HACER COSAS NUEVAS CON BASURA", "COMO UNA BOTELLA NUEVA.", n="recordar")],
 [2, MC("SOFI TIRA PAPEL, VIDRIO Y PLÁSTICO TODO JUNTO. ¿QUÉ CONVIENE?", ["SEPARARLOS", "TIRARLOS AL PISO", "NADA"], "SEPARARLOS", "ASÍ SE RECICLAN.", n="error")],
 [3, SA("¿QUIÉN APAGA LOS INCENDIOS?", acepta("BOMBEROS", "LOS BOMBEROS", "BOMBERO"), "LOS BOMBEROS.", n="recordar")],
 [3, MC("¿QUÉ HACE LA POLICÍA?", ["CUIDA A LAS PERSONAS", "TRAE CARTAS", "COCINA PAN"], "CUIDA A LAS PERSONAS", "NOS CUIDA.", n="recordar")],
 [3, MC("TOMI VE FUEGO EN UN PASTIZAL. ¿QUÉ HACE PRIMERO?", ["AVISA A UN ADULTO", "LO APAGA SOLO", "SE ACERCA A MIRAR"], "AVISA A UN ADULTO", "EL ADULTO LLAMA A BOMBEROS.", n="analizar")],
 [4, MC("LA COCINA PIERDE GAS. ¿A QUIÉN LLAMA UN ADULTO?", ["AL GASISTA", "AL CARTERO", "AL ELECTRICISTA"], "AL GASISTA", "ARREGLA EL GAS.", n="aplicar")],
 [4, SA("¿CUÁNDO TRABAJA MUCHAS VECES EL RECOLECTOR?", acepta("DE NOCHE", "NOCHE", "A LA NOCHE"), "DE NOCHE.", n="recordar")],
 [4, MC("TOMI DICE QUE EL TRABAJO DEL RECOLECTOR NO IMPORTA. ¿ESTÁ BIEN?", ["NO: TODOS IMPORTAN", "SÍ: NO IMPORTA", "SÍ: ES DE NOCHE"], "NO: TODOS IMPORTAN", "SIN ÉL, LA BASURA SE ACUMULA.", n="error")],
 [4, MC("UN TURNO ES…", ["EL HORARIO DE TRABAJO", "UN JUEGO DE CARTAS", "UN CAMIÓN GRANDE"], "EL HORARIO DE TRABAJO", "DE DÍA O DE NOCHE.", n="recordar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: servicios que llegan a casa", "examen_titulo": "Nivel jefe: servicios que llegan a casa",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
