# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 4 · Los servicios de la ciudad. Genera mision-4.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy recorre la ciudad).
Niveles: 1 qué servicios tiene una ciudad · 2 trabajadores y técnicas · 3 normas de los servicios · 4 servicios en el pueblo y el campo."""
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
"objetivo": "Vas a conocer los servicios de la ciudad.",
"vas_a_ver": ["Qué es un servicio", "Servicios de la casa", "Servicios para todos"],
"secciones": [
 S(1, "Los servicios", [
  D("Servicio", "Algo que la ciudad nos da para <b>vivir mejor</b>."),
  P("En casa usamos <b>agua</b>, <b>luz</b> y <b>gas</b>."),
  P("El agua llega por caños. La luz llega por cables."),
  IMG("Servicios de la casa", "Llegan por caños y cables.", FG.nombres(["AGUA", "LUZ", "GAS"], cols=3)),
 ]),
 S(1, "Para todos", [
  P("Otros servicios son para <b>todos</b>: el colectivo, el hospital, la escuela."),
  IMG("Servicios para todos", "Los usamos todos.", FG.tiras(["RECOLECCIÓN DE BASURA", "COLECTIVO", "HOSPITAL", "ESCUELA"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué servicio es?", "Pensá en cada pista.", FG.tiras(["1. SALE DE LA CANILLA", "2. NOS LLEVA DE UN LUGAR A OTRO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La luz", "planteo": "¿Cómo llega la luz a casa?", "pasos": ["Viene por cables.", "Entra a la casa.", "¡Prendemos la lámpara!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El agua sale de la…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "En tu casa", "planteo": "¿Qué servicios usaste hoy? Escribí dos."},
"tip": {"titulo": "Cuidarlos", "texto": "Apagá la luz y cerrá la canilla."},
"ojo": ["Los servicios hay que cuidarlos.", "Algunos son de la casa y otros, de todos."],
"resumen": [{"titulo": "Servicio", "texto": "Para vivir mejor."}, {"titulo": "En casa", "texto": "Agua, luz, gas."}, {"titulo": "Para todos", "texto": "Colectivo, hospital, escuela."}],
"glosario": [{"palabra": "Servicio", "significado": "Lo que la ciudad nos da."}, {"palabra": "Recolección", "significado": "Juntar la basura."}],
"carpeta": ["¿Qué servicio es la pista 1?", "¿Qué servicio es la pista 2?", "Lola dice que la escuela no es un servicio. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("AGUA") + low("EL AGUA"), low("COLECTIVO") + low("EL COLECTIVO") + low("TRANSPORTE") + low("EL TRANSPORTE"), NO],
"soluciones": {"incompleto": "CANILLA.", "solo": "Los servicios que usaste.", "carpeta": ["El agua.", "El colectivo.", "No: es un servicio."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer quiénes trabajan en los servicios.",
"vas_a_ver": ["Trabajadores", "Sus herramientas", "Cómo trabajan"],
"secciones": [
 S(1, "Quiénes trabajan", [
  P("Cada servicio tiene <b>trabajadores</b> con sus herramientas."),
  P("El electricista sube a los postes con escalera y casco. La enfermera mide la fiebre. El chofer sigue siempre el mismo recorrido."),
  IMG("Trabajos de la ciudad", "Cada uno con su herramienta.", FG.tiras(["RECOLECTOR: CAMIÓN DE BASURA", "ELECTRICISTA: CABLES Y PINZA", "CHOFER: COLECTIVO", "ENFERMERA: TERMÓMETRO"], numeros=False)),
 ]),
 S(1, "A toda hora", [
  P("Algunos trabajan de <b>noche</b>: los recolectores, los médicos de guardia."),
  P("Así, cuando nos levantamos, la calle ya está limpia."),
  IMG("De día y de noche", "La ciudad no para.", FG.nombres(["RECOLECTOR", "MÉDICA", "POLICÍA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Quién es?", "Pensá en cada pista.", FG.tiras(["1. ARREGLA LOS CABLES DE LA LUZ", "2. JUNTA LA BASURA DE NOCHE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El recolector", "planteo": "¿Qué hace el recolector?", "pasos": ["Pasa con el camión.", "Junta las bolsas.", "Deja la calle limpia."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La enfermera usa un…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Entrevista", "planteo": "Preguntá a alguien del barrio en qué servicio trabaja."},
"tip": {"titulo": "Agradecé", "texto": "Decí gracias a quienes trabajan para todos."},
"ojo": ["Algunos trabajan de noche.", "Cada servicio necesita personas."],
"resumen": [{"titulo": "Recolector", "texto": "Junta la basura."}, {"titulo": "Electricista", "texto": "Arregla la luz."}, {"titulo": "Enfermera", "texto": "Cuida la salud."}],
"glosario": [{"palabra": "Herramienta", "significado": "Lo que se usa para trabajar."}, {"palabra": "Guardia", "significado": "Trabajo de noche o sin cerrar."}],
"carpeta": ["¿Quién es la pista 1?", "¿Quién es la pista 2?", "Lola dice que nadie trabaja de noche. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ELECTRICISTA") + low("EL ELECTRICISTA") + low("LA ELECTRICISTA"), low("RECOLECTOR") + low("EL RECOLECTOR") + low("LOS RECOLECTORES") + low("LA RECOLECTORA"), NO],
"soluciones": {"incompleto": "TERMÓMETRO.", "solo": "Lo que te contaron.", "carpeta": ["El electricista.", "El recolector.", "No: algunos trabajan de noche."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer normas de los servicios.",
"vas_a_ver": ["La basura", "El colectivo", "El semáforo"],
"secciones": [
 S(1, "Normas para todos", [
  P("Los servicios funcionan mejor si respetamos <b>normas</b>."),
  P("Si sacamos la basura a cualquier hora, la calle se ensucia. Si no esperamos en la parada, el colectivo no para."),
  IMG("Algunas normas", "Para que todo funcione.", FG.tiras(["SACAR LA BASURA EN SU HORARIO", "ESPERAR EL COLECTIVO EN LA PARADA", "CRUZAR CON EL SEMÁFORO"], numeros=False, cols=1)),
 ]),
 S(1, "El semáforo", [
  P("<b>Verde</b>: cruzamos. <b>Amarillo</b>: atención. <b>Rojo</b>: esperamos."),
  P("Los autos también miran el semáforo. Así nadie se choca."),
  IMG("Los colores", "Para cruzar seguros.", FG.nombres(["ROJO: ESPERO", "AMARILLO: ATENCIÓN", "VERDE: CRUZO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Está bien?", "Pensá en cada una.", FG.tiras(["1. CRUZAR CON EL SEMÁFORO EN ROJO", "2. ESPERAR EN LA PARADA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Cruzar la calle", "planteo": "¿Cómo cruzo?", "pasos": ["Voy de la mano de un adulto.", "Miro el semáforo.", "Cruzo con verde."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Con el semáforo en rojo…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu barrio", "planteo": "¿A qué hora pasa el camión de la basura por tu casa?"},
"tip": {"titulo": "Por la senda", "texto": "Cruzá siempre por la senda peatonal."},
"ojo": ["Los chicos cruzan con un adulto.", "Las normas nos cuidan a todos."],
"resumen": [{"titulo": "Basura", "texto": "En su horario."}, {"titulo": "Colectivo", "texto": "En la parada."}, {"titulo": "Semáforo", "texto": "Verde: cruzo."}],
"glosario": [{"palabra": "Semáforo", "significado": "Luces que ordenan el tránsito."}, {"palabra": "Senda peatonal", "significado": "Rayas blancas para cruzar."}],
"carpeta": ["¿La tarjeta 1 está bien o mal?", "¿La tarjeta 2 está bien o mal?", "Lola dice que con rojo se cruza. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MAL") + low("ESTÁ MAL") + low("esta mal"), low("BIEN") + low("ESTÁ BIEN") + low("esta bien"), NO],
"soluciones": {"incompleto": "ESPERO.", "solo": "La hora del camión.", "carpeta": ["Mal.", "Bien.", "No: con rojo esperamos."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a comparar servicios de la ciudad y del campo.",
"vas_a_ver": ["En la ciudad", "En el pueblo", "En el campo"],
"secciones": [
 S(1, "Ciudad y campo", [
  P("En la <b>ciudad</b> hay muchos servicios cerca."),
  P("En el <b>campo</b>, las casas están lejos y algunos servicios no llegan."),
  IMG("Comparamos", "Ciudad y campo.", FG.tiras(["CIUDAD: HOSPITAL CERCA", "CAMPO: HOSPITAL LEJOS"], numeros=False, cols=1)),
 ]),
 S(1, "Otras formas", [
  P("En el campo, el agua puede salir de un <b>pozo</b>. La luz, de un <b>panel solar</b>."),
  P("Los chicos viajan lejos para ir a la escuela."),
  IMG("Servicios del campo", "Otras soluciones.", FG.nombres(["POZO DE AGUA", "PANEL SOLAR", "ESCUELA RURAL"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Ciudad o campo?", "Pensá en cada una.", FG.tiras(["1. EL AGUA SALE DE UN POZO", "2. EL COLECTIVO PASA CADA RATO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La escuela rural", "planteo": "¿Cómo va Juan a la escuela?", "pasos": ["Vive en el campo.", "Viaja en caballo o en combi.", "Llega a la escuela rural."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el campo, la luz puede venir de un panel…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Qué servicio te gustaría que llegue a todos lados?"},
"tip": {"titulo": "Comparar", "texto": "Preguntá: ¿está cerca o lejos?"},
"ojo": ["Todos tienen derecho a los servicios.", "En el campo se buscan otras formas."],
"resumen": [{"titulo": "Ciudad", "texto": "Servicios cerca."}, {"titulo": "Campo", "texto": "Servicios lejos."}, {"titulo": "Soluciones", "texto": "Pozo y panel solar."}],
"glosario": [{"palabra": "Rural", "significado": "Del campo."}, {"palabra": "Pozo", "significado": "Agujero hondo para sacar agua."}],
"carpeta": ["¿La tarjeta 1 es de la ciudad o del campo?", "¿Y la tarjeta 2?", "Lola dice que en el campo hay un hospital en cada esquina. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("CAMPO") + low("DEL CAMPO") + low("EL CAMPO"), low("CIUDAD") + low("DE LA CIUDAD") + low("LA CIUDAD"), NO],
"soluciones": {"incompleto": "SOLAR.", "solo": "El servicio que elegiste.", "carpeta": ["Del campo.", "De la ciudad.", "No: queda lejos."]},
}

ACT = {
"1": [UNI("UNÍ CADA SERVICIO.", [("AGUA", "CANILLA"), ("LUZ", "LÁMPARA"), ("GAS", "COCINA")], "LOS USAMOS EN CASA.", n="analizar"),
      TF("EL HOSPITAL ES UN SERVICIO PARA TODOS.", "VERDADERO", "CUIDA LA SALUD.", n="recordar")],
"2": [MC("¿QUIÉN JUNTA LA BASURA?", ["EL RECOLECTOR", "LA ENFERMERA"], "EL RECOLECTOR", "CON EL CAMIÓN.", n="aplicar"),
      UNI("UNÍ CADA TRABAJADOR CON SU HERRAMIENTA.", [("ELECTRICISTA", "PINZA"), ("ENFERMERA", "TERMÓMETRO")], "CADA UNO LA SUYA.", n="analizar")],
"3": [MC("CON EL SEMÁFORO EN VERDE…", ["CRUZO", "ESPERO"], "CRUZO", "CON CUIDADO.", n="aplicar"),
      TF("EL COLECTIVO SE ESPERA EN LA PARADA.", "VERDADERO", "ES UNA NORMA.", n="recordar")],
"4": [MC("EN EL CAMPO, EL AGUA PUEDE SALIR DE…", ["UN POZO", "UN SEMÁFORO"], "UN POZO", "SE SACA DE ABAJO.", n="aplicar"),
      UNI("UNÍ: ¿CIUDAD O CAMPO?", [("HOSPITAL CERCA", "CIUDAD"), ("PANEL SOLAR EN LA CASA", "CAMPO")], "PENSÁ: CERCA O LEJOS.", n="analizar")],
"5": [MC("RELÁMPAGO. LA LUZ LLEGA POR…", ["CABLES", "RÍOS"], "CABLES", "HASTA LA CASA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA ENFERMERA USA…", ["TERMÓMETRO", "PINZA"], "TERMÓMETRO", "CUIDA LA SALUD.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. CON ROJO…", ["ESPERO", "CRUZO"], "ESPERO", "ES PELIGROSO CRUZAR.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ESCUELA DEL CAMPO…", ["RURAL", "URBANA"], "RURAL", "RURAL ES DEL CAMPO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UN SERVICIO?", ["ALGO PARA VIVIR MEJOR", "UN JUGUETE"], "ALGO PARA VIVIR MEJOR", "COMO EL AGUA O LA LUZ.", n="recordar")],
 [1, SA("NOMBRÁ UN SERVICIO DE TU CASA.", low("AGUA") + low("LUZ") + low("GAS") + low("EL AGUA") + low("LA LUZ") + low("EL GAS") + low("INTERNET"), "POR EJEMPLO: EL AGUA.", n="aplicar")],
 [1, TF("LA ESCUELA NO ES UN SERVICIO.", "FALSO", "ES UN SERVICIO PARA TODOS.", n="error")],
 [2, UNI("UNÍ CADA TRABAJO.", [("RECOLECTOR", "BASURA"), ("CHOFER", "COLECTIVO")], "¿QUÉ HACE CADA UNO?", n="analizar")],
 [2, SA("¿QUIÉN ARREGLA LOS CABLES DE LA LUZ?", low("ELECTRICISTA") + low("EL ELECTRICISTA") + low("LA ELECTRICISTA"), "EL ELECTRICISTA.", n="aplicar")],
 [2, TF("ALGUNOS TRABAJAN DE NOCHE.", "VERDADERO", "COMO LOS RECOLECTORES.", n="recordar")],
 [3, MC("¿POR DÓNDE SE CRUZA LA CALLE?", ["POR LA SENDA PEATONAL", "POR EL MEDIO"], "POR LA SENDA PEATONAL", "LAS RAYAS BLANCAS.", n="aplicar")],
 [3, SA("CON EL SEMÁFORO EN ROJO, ¿QUÉ HACEMOS?", low("ESPERAMOS") + low("ESPERAR") + low("ESPERO") + low("NOS QUEDAMOS QUIETOS"), "ESPERAMOS.", n="aplicar")],
 [3, TF("LA BASURA SE SACA A CUALQUIER HORA.", "FALSO", "SE SACA EN SU HORARIO.", n="error")],
 [4, MC("¿DÓNDE ESTÁN LOS SERVICIOS MÁS CERCA?", ["EN LA CIUDAD", "EN EL CAMPO"], "EN LA CIUDAD", "EN EL CAMPO, LEJOS.", n="aplicar")],
 [4, SA("EN EL CAMPO, ¿DE DÓNDE PUEDE VENIR LA LUZ?", low("PANEL SOLAR") + low("UN PANEL SOLAR") + low("DEL PANEL SOLAR") + low("DEL SOL") + low("EL SOL"), "DE UN PANEL SOLAR.", n="aplicar")],
 [4, TF("TODOS TIENEN DERECHO A LOS SERVICIOS.", "VERDADERO", "EN LA CIUDAD Y EN EL CAMPO.", n="recordar")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: los servicios de la ciudad", "examen_titulo": "Nivel jefe: los servicios de la ciudad",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
