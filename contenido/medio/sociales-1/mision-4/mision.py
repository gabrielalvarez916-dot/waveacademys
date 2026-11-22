# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 4 · Instituciones que cuidan a las personas. Genera mision-4.json.
Regla de primeros años. Metáfora: los ayudantes del barrio. Misión COMÚN: sin nombres propios de un país (sirve para todos).
Niveles: 1 centros de salud y hospitales · 2 bibliotecas y clubes del barrio · 3 qué trabajo hace cada institución · 4 respeto y cooperación en la convivencia."""
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
"objetivo": "Vas a conocer los centros de salud y los hospitales.",
"vas_a_ver": ["Para qué vamos", "Quiénes trabajan", "Cuidar la salud"],
"secciones": [
 S(1, "Centros de salud", [
  D("Centro de salud", "Lugar donde nos atienden para cuidar la salud."),
  P("Vamos para <b>vacunarnos</b>, hacernos <b>controles</b> y cuando estamos <b>enfermos</b>."),
  IMG("Vamos para", "Tres motivos.", FG.tiras(["VACUNAS", "CONTROLES", "SI ESTOY ENFERMO"], numeros=False, cols=3)),
 ]),
 S(1, "Quiénes trabajan", [
  P("Trabajan <b>médicas</b>, <b>enfermeros</b> y <b>dentistas</b>."),
  IMG("Trabajan", "Nos cuidan.", FG.tiras(["MÉDICA: REVISA", "ENFERMERO: VACUNA", "DENTISTA: DIENTES"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los casos. Los vas a usar en la carpeta."),
  IMG("¿Quién te ayuda?", "Pensá.", FG.tiras(["ME DUELE UNA MUELA", "TOCA UNA VACUNA", "TENGO FIEBRE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El control", "planteo": "Tomi va al centro de salud.", "pasos": ["La médica lo pesa.", "Lo mide.", "Le dice que está sano."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El dentista cuida…", "pasos": ["Los ___."]},
"ejemplo_solo": {"titulo": "Tu centro de salud", "planteo": "Preguntá en casa dónde queda el centro de salud del barrio."},
"tip": {"titulo": "Con un adulto", "texto": "Al médico se va siempre con un adulto."},
"ojo": ["Las vacunas nos protegen.", "Los remedios los da un adulto."],
"resumen": [{"titulo": "Centro de salud", "texto": "Cuida la salud."}, {"titulo": "Trabajan", "texto": "Médicas, enfermeros."}, {"titulo": "Vamos", "texto": "Vacunas y controles."}],
"glosario": [{"palabra": "Vacuna", "significado": "Nos protege de enfermedades."}, {"palabra": "Control", "significado": "Visita para ver que estamos bien."}],
"carpeta": ["Te duele una muela. ¿Quién te ayuda?", "Toca una vacuna. ¿Quién te la pone?", "¿Para qué sirven las vacunas?"],
"respuestas_carpeta": [acepta("DENTISTA", "EL DENTISTA", "LA DENTISTA"), acepta("ENFERMERO", "EL ENFERMERO", "ENFERMERA", "LA ENFERMERA"), acepta("PARA PROTEGERNOS", "PROTEGER", "PROTEGERNOS", "NO ENFERMARNOS", "PARA NO ENFERMARNOS")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "DIENTES.", "solo": "Lo que te contaron.", "carpeta": ["EL DENTISTA.", "EL ENFERMERO.", "PARA PROTEGERNOS."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer bibliotecas y clubes del barrio.",
"vas_a_ver": ["La biblioteca", "El club", "Lo que tienen en común"],
"secciones": [
 S(1, "La biblioteca", [
  D("Biblioteca", "Lugar donde se guardan libros y se prestan."),
  P("En la biblioteca <b>leemos</b> y nos <b>prestan</b> libros."),
  IMG("En la biblioteca", "Libros para todos.", FG.tiras(["LEER", "PEDIR PRESTADO", "DEVOLVER"], numeros=True, cols=3)),
 ]),
 S(1, "El club", [
  P("En el club hacemos <b>deporte</b> y nos <b>encontramos</b> con otros."),
  IMG("En el club", "Deporte y amigos.", FG.tiras(["FÚTBOL", "NATACIÓN", "BÁSQUET"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las actividades. Las vas a usar en la carpeta."),
  IMG("¿Dónde?", "Biblioteca o club.", FG.tiras(["NADAR", "LEER UN CUENTO", "JUGAR AL BÁSQUET"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El libro prestado", "planteo": "Sofi va a la biblioteca.", "pasos": ["Elige un cuento.", "Se lo llevan a casa.", "Lo devuelve a la semana."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el club…", "pasos": ["En el club hacemos ___."]},
"ejemplo_solo": {"titulo": "Tu barrio", "planteo": "Preguntá si hay una biblioteca o un club en tu barrio."},
"tip": {"titulo": "Devolvé a tiempo", "texto": "Así otro chico también puede leerlo."},
"ojo": ["Los libros prestados se cuidan.", "En el club respetamos al otro equipo."],
"resumen": [{"titulo": "Biblioteca", "texto": "Leer y pedir libros."}, {"titulo": "Club", "texto": "Deporte."}, {"titulo": "Los dos", "texto": "Para encontrarnos."}],
"glosario": [{"palabra": "Prestar", "significado": "Dar algo por un tiempo."}, {"palabra": "Devolver", "significado": "Dar otra vez lo prestado."}],
"carpeta": ["¿Dónde nadás?", "¿Dónde leés un cuento?", "Tomi no devuelve el libro. ¿Qué problema hay?"],
"respuestas_carpeta": [acepta("CLUB", "EN EL CLUB"), acepta("BIBLIOTECA", "EN LA BIBLIOTECA"), acepta("OTROS NO LO PUEDEN LEER", "NADIE MÁS LO LEE", "NADIE MAS LO LEE", "LOS OTROS NO PUEDEN LEERLO")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "DEPORTE.", "solo": "Lo que averiguaste.", "carpeta": ["EN EL CLUB.", "EN LA BIBLIOTECA.", "OTROS NO LO PUEDEN LEER."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver qué trabajo hace cada institución.",
"vas_a_ver": ["Instituciones del barrio", "Su trabajo", "Nos ayudan a todos"],
"secciones": [
 S(1, "Instituciones", [
  D("Institución", "Lugar con personas que hacen un trabajo para todos."),
  P("En el barrio hay <b>escuela</b>, <b>hospital</b>, <b>bomberos</b> y <b>biblioteca</b>."),
  IMG("En el barrio", "Instituciones.", FG.tiras(["ESCUELA", "HOSPITAL", "BOMBEROS", "BIBLIOTECA"], numeros=False, cols=2)),
 ]),
 S(1, "Su trabajo", [
  P("Cada una tiene su <b>trabajo</b>: enseñar, curar, apagar incendios, prestar libros."),
  IMG("Cada una", "Su trabajo.", FG.tiras(["ESCUELA: ENSEÑA", "HOSPITAL: CURA", "BOMBEROS: APAGAN FUEGO", "BIBLIOTECA: PRESTA LIBROS"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los casos. Los vas a usar en la carpeta."),
  IMG("¿Quién ayuda?", "Pensá.", FG.tiras(["HAY UN INCENDIO", "QUIERO UN LIBRO", "ME QUEBRÉ UN BRAZO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El incendio", "planteo": "Se quema un pastizal.", "pasos": ["Un adulto llama a los bomberos.", "Llegan con el camión.", "Apagan el fuego."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El hospital…", "pasos": ["El hospital ___ a los enfermos."]},
"ejemplo_solo": {"titulo": "Dibujá", "planteo": "Dibujá una institución de tu barrio y su trabajo."},
"tip": {"titulo": "Para todos", "texto": "Las instituciones ayudan a todas las personas."},
"ojo": ["En una emergencia, avisá a un adulto.", "Cada institución hace un trabajo distinto."],
"resumen": [{"titulo": "Instituciones", "texto": "Trabajan para todos."}, {"titulo": "Cada una", "texto": "Su trabajo."}, {"titulo": "Ayudan", "texto": "A todos."}],
"glosario": [{"palabra": "Emergencia", "significado": "Algo peligroso que pasa de golpe."}, {"palabra": "Bombero", "significado": "Persona que apaga incendios."}],
"carpeta": ["Hay un incendio. ¿Quién ayuda?", "Quiero un libro. ¿Adónde voy?", "Me quebré un brazo. ¿Adónde voy?"],
"respuestas_carpeta": [acepta("BOMBEROS", "LOS BOMBEROS"), acepta("BIBLIOTECA", "A LA BIBLIOTECA"), acepta("HOSPITAL", "AL HOSPITAL", "CENTRO DE SALUD", "AL CENTRO DE SALUD")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "CURA.", "solo": "Tu dibujo.", "carpeta": ["LOS BOMBEROS.", "A LA BIBLIOTECA.", "AL HOSPITAL."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver cómo convivir con respeto y cooperación.",
"vas_a_ver": ["Respetar", "Cooperar", "Convivir"],
"secciones": [
 S(1, "Respetar", [
  D("Respeto", "Tratar bien a los demás, aunque piensen distinto."),
  P("Respetamos cuando <b>escuchamos</b> y <b>esperamos el turno</b>."),
  IMG("Respeto", "Así se ve.", FG.tiras(["ESCUCHO", "ESPERO MI TURNO", "PIDO PERMISO"], numeros=False, cols=3)),
 ]),
 S(1, "Cooperar", [
  D("Cooperar", "Ayudarnos entre todos para lograr algo."),
  P("Si cooperamos, las cosas salen <b>mejor</b> y más <b>rápido</b>."),
  IMG("Cooperar", "Entre todos.", FG.tiras(["SOLO: CUESTA", "ENTRE TODOS: ¡SALE!"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las acciones. Las vas a usar en la carpeta."),
  IMG("¿Respeta o no?", "Pensá.", FG.tiras(["SE BURLA DE UN COMPAÑERO", "PRESTA SU LÁPIZ", "INTERRUMPE AL QUE HABLA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Limpiar el aula", "planteo": "El grado limpia.", "pasos": ["Sofi junta papeles.", "Tomi ordena las sillas.", "¡Terminan rápido!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cooperar es…", "pasos": ["___ entre todos."]},
"ejemplo_solo": {"titulo": "Tu ayuda", "planteo": "Pensá cómo podés cooperar hoy en tu casa."},
"tip": {"titulo": "Ponete en su lugar", "texto": "Pensá cómo se siente el otro."},
"ojo": ["Las burlas lastiman: no se hacen.", "Si alguien no respeta, se avisa a un adulto."],
"resumen": [{"titulo": "Respeto", "texto": "Tratar bien."}, {"titulo": "Cooperar", "texto": "Ayudarnos."}, {"titulo": "Convivir", "texto": "Estar bien juntos."}],
"glosario": [{"palabra": "Convivir", "significado": "Vivir o estar juntos en paz."}, {"palabra": "Cooperar", "significado": "Ayudarnos entre todos."}],
"carpeta": ["Se burla de un compañero, ¿respeta?", "Presta su lápiz, ¿coopera?", "¿Qué hacés si alguien interrumpe siempre?"],
"respuestas_carpeta": [acepta("NO"), acepta("SÍ", "SI"), acepta("LE PIDO QUE ESPERE", "AVISO A LA MAESTRA", "AVISO A UN ADULTO", "LE DIGO QUE ESPERE SU TURNO", "HABLO CON ÉL")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "AYUDARNOS.", "solo": "Por ejemplo: poner la mesa.", "carpeta": ["NO.", "SÍ.", "LE PIDO QUE ESPERE SU TURNO."]},
}

ACT = {
"1": [MC("¿PARA QUÉ VAMOS AL CENTRO DE SALUD?", ["PARA CUIDAR LA SALUD", "PARA COMPRAR ROPA", "PARA JUGAR AL FÚTBOL"], "PARA CUIDAR LA SALUD", "VACUNAS Y CONTROLES.", n="recordar"),
      MC("TE DUELE UNA MUELA. ¿QUIÉN TE AYUDA?", ["EL DENTISTA", "EL BOMBERO", "EL PANADERO"], "EL DENTISTA", "CUIDA LOS DIENTES.", n="aplicar")],
"2": [MC("¿QUÉ HACE LA BIBLIOTECA?", ["PRESTA LIBROS", "VENDE PAN", "APAGA INCENDIOS"], "PRESTA LIBROS", "PRESTA LIBROS.", n="recordar"),
      MC("¿QUÉ TIENEN EN COMÚN EL CLUB Y LA BIBLIOTECA?", ["NOS ENCONTRAMOS CON OTROS", "VENDEN COMIDA", "CURAN"], "NOS ENCONTRAMOS CON OTROS", "SON LUGARES DE ENCUENTRO.", n="analizar")],
"3": [MC("HAY UN INCENDIO. ¿QUIÉN AYUDA?", ["LOS BOMBEROS", "LA BIBLIOTECA", "EL CLUB"], "LOS BOMBEROS", "APAGAN EL FUEGO.", n="aplicar"),
      MC("SOFI DICE QUE EL HOSPITAL PRESTA LIBROS. ¿QUÉ ESTÁ MAL?", ["ESO LO HACE LA BIBLIOTECA", "ESTÁ BIEN", "LO HACEN LOS BOMBEROS"], "ESO LO HACE LA BIBLIOTECA", "EL HOSPITAL CURA.", n="error")],
"4": [MC("¿QUÉ ES COOPERAR?", ["AYUDARNOS ENTRE TODOS", "PELEAR", "ESCONDERSE"], "AYUDARNOS ENTRE TODOS", "ENTRE TODOS SALE MEJOR.", n="recordar"),
      MC("UN COMPAÑERO SE BURLA DE OTRO. ¿QUÉ HACÉS?", ["AVISO A UN ADULTO", "ME RÍO", "NADA"], "AVISO A UN ADULTO", "LAS BURLAS LASTIMAN.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿QUIÉN PONE VACUNAS?", ["ENFERMERO", "BOMBERO", "PORTERO"], "ENFERMERO", "EL ENFERMERO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿DÓNDE HACÉS DEPORTE?", ["CLUB", "BIBLIOTECA", "HOSPITAL"], "CLUB", "EN EL CLUB.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿QUIÉN APAGA INCENDIOS?", acepta("BOMBEROS", "LOS BOMBEROS", "BOMBERO"), "LOS BOMBEROS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ES RESPETAR?", ["ESPERAR MI TURNO", "EMPUJAR", "GRITAR"], "ESPERAR MI TURNO", "RESPETAMOS EL TURNO.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("UN CENTRO DE SALUD ES…", ["DONDE CUIDAN NUESTRA SALUD", "DONDE VENDEN JUGUETES", "DONDE HAY UNA PILETA"], "DONDE CUIDAN NUESTRA SALUD", "VACUNAS Y CONTROLES.", n="recordar")],
 [1, MC("¿PARA QUÉ SIRVEN LAS VACUNAS?", ["PARA PROTEGERNOS", "PARA DORMIR MÁS", "PARA CRECER ALTO"], "PARA PROTEGERNOS", "NOS PROTEGEN DE ENFERMEDADES.", n="analizar")],
 [1, SA("¿QUIÉN CUIDA LOS DIENTES?", acepta("DENTISTA", "EL DENTISTA", "LA DENTISTA"), "EL DENTISTA.", n="recordar")],
 [2, MC("EN LA BIBLIOTECA NOS…", ["PRESTAN LIBROS", "VACUNAN", "CORTAN EL PELO"], "PRESTAN LIBROS", "Y LOS DEVOLVEMOS.", n="recordar")],
 [2, SA("¿DÓNDE PODÉS NADAR EN EL BARRIO?", acepta("CLUB", "EN EL CLUB", "EL CLUB"), "EN EL CLUB.", n="aplicar")],
 [2, MC("TOMI SE QUEDA CON EL LIBRO PRESTADO. ¿QUÉ PASA?", ["OTROS NO LO PUEDEN LEER", "ESTÁ BIEN", "LA BIBLIOTECA GANA"], "OTROS NO LO PUEDEN LEER", "HAY QUE DEVOLVERLO.", n="error")],
 [3, MC("¿QUÉ HACE EL HOSPITAL?", ["CURA A LOS ENFERMOS", "PRESTA LIBROS", "ENSEÑA A LEER"], "CURA A LOS ENFERMOS", "CUIDA LA SALUD.", n="recordar")],
 [3, MC("ME QUEBRÉ UN BRAZO. ¿ADÓNDE VOY?", ["AL HOSPITAL", "A LA BIBLIOTECA", "AL CLUB"], "AL HOSPITAL", "AHÍ ME CURAN.", n="aplicar")],
 [3, MC("¿POR QUÉ LAS INSTITUCIONES SON IMPORTANTES?", ["NOS AYUDAN A TODOS", "SON GRANDES", "TIENEN PUERTA"], "NOS AYUDAN A TODOS", "TRABAJAN PARA TODOS.", n="analizar")],
 [4, MC("RESPETAR ES…", ["TRATAR BIEN A LOS DEMÁS", "BURLARSE DEL OTRO", "INTERRUMPIR AL OTRO"], "TRATAR BIEN A LOS DEMÁS", "AUNQUE PIENSEN DISTINTO.", n="recordar")],
 [4, SA("SI COOPERAMOS, LAS COSAS SALEN MÁS…", acepta("RÁPIDO", "RAPIDO", "FÁCIL", "FACIL", "MEJOR"), "MÁS RÁPIDO Y MEJOR.", n="aplicar")],
 [4, MC("SOFI INTERRUMPE A TOMI CUANDO HABLA. ¿QUÉ CONVIENE?", ["ESPERAR SU TURNO", "GRITAR MÁS FUERTE", "IRSE"], "ESPERAR SU TURNO", "ASÍ NOS RESPETAMOS.", n="error")],
 [4, MC("EL GRADO LIMPIA EL AULA ENTRE TODOS. ESO ES…", ["COOPERAR", "PELEAR", "JUGAR"], "COOPERAR", "AYUDARNOS ENTRE TODOS.", n="aplicar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: instituciones del barrio", "examen_titulo": "Nivel jefe: instituciones que cuidan a las personas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
