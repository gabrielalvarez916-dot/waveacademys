# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 2 · Mi escuela es una institución. Genera mision-2.json.
Regla de primeros años. Metáfora: un día en la escuela.
Niveles: 1 para qué sirve una escuela · 2 los trabajos que hay en la escuela · 3 normas que nos cuidan en el aula · 4 los espacios de la escuela."""
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
"objetivo": "Vas a ver para qué sirve la escuela.",
"vas_a_ver": ["Qué es una institución", "Para qué vamos", "Mi escuela"],
"secciones": [
 S(1, "Una institución", [
  D("Institución", "Lugar con personas y reglas que cumple una tarea para todos."),
  P("La escuela es una <b>institución</b>: sirve para <b>aprender</b>."),
  IMG("La escuela", "Una institución.", FG.tiras(["ESCUELA", "HOSPITAL", "CLUB"], numeros=False, cols=3)),
 ]),
 S(1, "Para qué vamos", [
  P("En la escuela <b>aprendemos</b>, <b>jugamos</b> y hacemos <b>amigos</b>."),
  IMG("Vamos para", "Tres cosas.", FG.tiras(["APRENDER", "JUGAR", "HACER AMIGOS"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Pensá en tu escuela. La vas a usar en la carpeta."),
  IMG("Mi escuela", "Nombre y lugar.", FG.tiras(["NOMBRE DE MI ESCUELA", "MI GRADO", "MI MAESTRA O MAESTRO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Un día", "planteo": "Sofi llega a la escuela.", "pasos": ["Saluda a su maestra.", "Aprende a leer.", "Juega en el recreo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En la escuela…", "pasos": ["En la escuela ___ a leer y escribir."]},
"ejemplo_solo": {"titulo": "Tu escuela", "planteo": "Escribí el nombre de tu escuela."},
"tip": {"titulo": "Es de todos", "texto": "La escuela es un lugar para todos los chicos."},
"ojo": ["Todos los chicos tienen derecho a ir a la escuela.", "La escuela se cuida entre todos."],
"resumen": [{"titulo": "Institución", "texto": "Cumple una tarea para todos."}, {"titulo": "Aprender", "texto": "Leer, escribir, contar."}, {"titulo": "Compartir", "texto": "Jugar y hacer amigos."}],
"glosario": [{"palabra": "Institución", "significado": "Lugar que cumple una tarea para todos."}, {"palabra": "Derecho", "significado": "Algo que nos corresponde a todos."}],
"carpeta": ["¿Para qué sirve la escuela?", "Nombrá otra institución.", "¿Quiénes pueden ir a la escuela?"],
"respuestas_carpeta": [acepta("PARA APRENDER", "APRENDER"), acepta("HOSPITAL", "CLUB", "EL HOSPITAL", "EL CLUB", "BIBLIOTECA", "MUNICIPALIDAD"), acepta("TODOS", "TODOS LOS CHICOS", "LOS CHICOS")],
"carpeta_nivel": ["recordar", "aplicar", "analizar"],
"soluciones": {"incompleto": "APRENDEMOS.", "solo": "El nombre de tu escuela.", "carpeta": ["PARA APRENDER.", "EL HOSPITAL.", "TODOS LOS CHICOS."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer los trabajos que hay en la escuela.",
"vas_a_ver": ["Quiénes trabajan", "Qué hace cada uno", "Todos son importantes"],
"secciones": [
 S(1, "Quiénes trabajan", [
  P("En la escuela trabajan <b>maestras</b>, <b>directora</b>, <b>porteros</b> y <b>cocineros</b>."),
  IMG("Trabajan", "Muchas personas.", FG.tiras(["MAESTRA", "DIRECTORA", "PORTERO", "COCINERA"], numeros=False, cols=2)),
 ]),
 S(1, "Qué hace cada uno", [
  D("Trabajo", "Lo que hace una persona para ayudar y ganar su sueldo."),
  P("La maestra <b>enseña</b>. El portero <b>limpia</b>. La cocinera <b>cocina</b>."),
  IMG("Cada uno", "Su trabajo.", FG.tiras(["MAESTRA: ENSEÑA", "DIRECTORA: ORGANIZA", "PORTERO: LIMPIA", "COCINERA: COCINA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los trabajos. Los vas a usar en la carpeta."),
  IMG("¿Quién lo hace?", "Pensá.", FG.tiras(["ABRE LA PUERTA", "PREPARA EL ALMUERZO", "ENSEÑA A LEER"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El comedor", "planteo": "Es mediodía.", "pasos": ["La cocinera cocina.", "La maestra acompaña.", "Los chicos almuerzan."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La directora…", "pasos": ["La directora ___ la escuela."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntale a alguien que trabaja en tu escuela qué hace."},
"tip": {"titulo": "Saludá", "texto": "Saludá a todos los que trabajan en la escuela."},
"ojo": ["Todos los trabajos son importantes.", "Ayudamos dejando todo limpio."],
"resumen": [{"titulo": "Maestra", "texto": "Enseña."}, {"titulo": "Portero", "texto": "Limpia y cuida."}, {"titulo": "Todos", "texto": "Son importantes."}],
"glosario": [{"palabra": "Portero", "significado": "Persona que cuida y limpia la escuela."}, {"palabra": "Organizar", "significado": "Ordenar cómo se hacen las cosas."}],
"carpeta": ["¿Quién prepara el almuerzo?", "¿Quién enseña a leer?", "Tomi dice que solo la maestra es importante. ¿Está bien?"],
"respuestas_carpeta": [acepta("COCINERA", "LA COCINERA", "COCINERO", "EL COCINERO"), acepta("MAESTRA", "LA MAESTRA", "MAESTRO", "EL MAESTRO"), acepta("NO", "NO, TODOS SON IMPORTANTES")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "ORGANIZA.", "solo": "Lo que te contó.", "carpeta": ["LA COCINERA.", "LA MAESTRA.", "NO: TODOS SON IMPORTANTES."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer las normas que nos cuidan en el aula.",
"vas_a_ver": ["Qué es una norma", "Normas del aula", "Por qué las cumplimos"],
"secciones": [
 S(1, "Una norma", [
  D("Norma", "Regla que nos dice cómo comportarnos para estar bien."),
  P("Las normas nos <b>cuidan</b> a todos."),
  IMG("Normas del aula", "Las cumplimos.", FG.tiras(["LEVANTO LA MANO", "ESPERO MI TURNO", "CUIDO LOS MATERIALES"], numeros=False, cols=1)),
 ]),
 S(1, "Sin normas", [
  P("Si todos gritan, <b>nadie escucha</b>. Si corremos en el aula, <b>nos golpeamos</b>."),
  IMG("Sin normas", "¿Qué pasa?", FG.tiras(["TODOS GRITAN", "NADIE ESCUCHA", "SE ROMPEN COSAS"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las acciones. Las vas a usar en la carpeta."),
  IMG("¿Cumple la norma?", "Pensá.", FG.tiras(["GRITA PARA HABLAR", "LEVANTA LA MANO", "CORRE EN EL AULA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Quiero hablar", "planteo": "Sofi tiene una idea.", "pasos": ["Levanta la mano.", "Espera su turno.", "La maestra la escucha."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para hablar…", "pasos": ["Para hablar, levanto la ___."]},
"ejemplo_solo": {"titulo": "Tu norma", "planteo": "Pensá una norma nueva para tu aula."},
"tip": {"titulo": "Entre todos", "texto": "Las normas se pueden armar entre todos."},
"ojo": ["Las normas son para todos, también los grandes.", "Si alguien no cumple, se habla."],
"resumen": [{"titulo": "Norma", "texto": "Regla que nos cuida."}, {"titulo": "Aula", "texto": "Levantar la mano."}, {"titulo": "Para qué", "texto": "Estar bien todos."}],
"glosario": [{"palabra": "Norma", "significado": "Regla para convivir."}, {"palabra": "Convivir", "significado": "Vivir o estar juntos en paz."}],
"carpeta": ["Grita para hablar, ¿cumple la norma?", "Levanta la mano, ¿cumple la norma?", "¿Por qué no se corre en el aula?"],
"respuestas_carpeta": [acepta("NO"), acepta("SÍ", "SI"), acepta("NOS PODEMOS GOLPEAR", "NOS GOLPEAMOS", "PARA NO GOLPEARNOS", "PARA NO LASTIMARNOS", "NOS LASTIMAMOS")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "MANO.", "solo": "Por ejemplo: guardar los útiles.", "carpeta": ["NO.", "SÍ.", "PARA NO GOLPEARNOS."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer los espacios de la escuela y para qué sirven.",
"vas_a_ver": ["Los espacios", "Para qué sirve cada uno", "Cuidarlos"],
"secciones": [
 S(1, "Los espacios", [
  P("La escuela tiene <b>aulas</b>, <b>patio</b>, <b>baños</b>, <b>biblioteca</b> y <b>dirección</b>."),
  IMG("Espacios", "Muchos lugares.", FG.tiras(["AULA", "PATIO", "BIBLIOTECA", "BAÑO", "DIRECCIÓN", "COMEDOR"], numeros=False, cols=3)),
 ]),
 S(1, "Para qué sirven", [
  D("Espacio", "Lugar de la escuela con un uso."),
  P("En el aula <b>aprendemos</b>. En el patio <b>jugamos</b>. En la biblioteca <b>leemos</b>."),
  IMG("Cada espacio", "Su uso.", FG.tiras(["AULA: APRENDER", "PATIO: JUGAR", "BIBLIOTECA: LEER", "COMEDOR: COMER"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las actividades. Las vas a usar en la carpeta."),
  IMG("¿Dónde?", "Pensá el lugar.", FG.tiras(["BUSCAR UN CUENTO", "SALTAR LA SOGA", "ALMORZAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El recreo", "planteo": "Suena el timbre.", "pasos": ["Sofi sale del aula.", "Va al patio.", "Juega con Tomi."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para leer cuentos…", "pasos": ["Voy a la ___."]},
"ejemplo_solo": {"titulo": "Tu plano", "planteo": "Dibujá un plano de tu escuela con sus espacios."},
"tip": {"titulo": "Cada cosa en su lugar", "texto": "Usá cada espacio para lo que sirve."},
"ojo": ["En la biblioteca se habla bajito.", "Los espacios se cuidan y se dejan limpios."],
"resumen": [{"titulo": "Espacios", "texto": "Aula, patio, biblioteca."}, {"titulo": "Uso", "texto": "Cada uno sirve para algo."}, {"titulo": "Cuidar", "texto": "Dejarlos limpios."}],
"glosario": [{"palabra": "Biblioteca", "significado": "Lugar con libros para leer."}, {"palabra": "Plano", "significado": "Dibujo de un lugar visto desde arriba."}],
"carpeta": ["¿Dónde buscás un cuento?", "¿Dónde saltás la soga?", "¿Dónde almorzás?"],
"respuestas_carpeta": [acepta("BIBLIOTECA", "EN LA BIBLIOTECA"), acepta("PATIO", "EN EL PATIO"), acepta("COMEDOR", "EN EL COMEDOR")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "BIBLIOTECA.", "solo": "Tu plano.", "carpeta": ["EN LA BIBLIOTECA.", "EN EL PATIO.", "EN EL COMEDOR."]},
}

ACT = {
"1": [MC("¿PARA QUÉ SIRVE LA ESCUELA?", ["PARA APRENDER", "PARA DORMIR", "PARA COMPRAR"], "PARA APRENDER", "APRENDEMOS Y COMPARTIMOS.", n="recordar"),
      MC("¿CUÁL TAMBIÉN ES UNA INSTITUCIÓN?", ["EL HOSPITAL", "UNA PELOTA", "UN ÁRBOL"], "EL HOSPITAL", "CUMPLE UNA TAREA PARA TODOS.", n="analizar")],
"2": [MC("¿QUÉ HACE LA MAESTRA?", ["ENSEÑA", "COCINA", "MANEJA"], "ENSEÑA", "LA MAESTRA ENSEÑA.", n="recordar"),
      MC("EL PATIO ESTÁ LIMPIO A LA MAÑANA. ¿QUIÉN LO LIMPIÓ?", ["EL PORTERO", "LA DIRECTORA", "NADIE"], "EL PORTERO", "EL PORTERO LIMPIA Y CUIDA.", n="aplicar")],
"3": [MC("¿QUÉ ES UNA NORMA?", ["UNA REGLA QUE NOS CUIDA", "UN JUEGO DE PATIO", "UN LIBRO DE CUENTOS"], "UNA REGLA QUE NOS CUIDA", "NOS DICE CÓMO COMPORTARNOS.", n="recordar"),
      MC("TOMI GRITA PARA HABLAR. ¿QUÉ NORMA NO CUMPLE?", ["LEVANTAR LA MANO", "CUIDAR LAS PLANTAS", "COMER FRUTA"], "LEVANTAR LA MANO", "PRIMERO SE LEVANTA LA MANO.", n="error")],
"4": [MC("¿DÓNDE JUGÁS EN EL RECREO?", ["PATIO", "DIRECCIÓN", "BAÑO"], "PATIO", "EL PATIO ES PARA JUGAR.", n="aplicar"),
      SA("¿DÓNDE HAY LIBROS PARA LEER?", acepta("BIBLIOTECA", "EN LA BIBLIOTECA", "LA BIBLIOTECA"), "EN LA BIBLIOTECA.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿QUIÉN COCINA EN LA ESCUELA?", ["COCINERA", "MAESTRA", "DIRECTORA"], "COCINERA", "LA COCINERA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. PARA HABLAR EN CLASE…", ["LEVANTO LA MANO", "GRITO", "ME PARO EN LA SILLA"], "LEVANTO LA MANO", "ES UNA NORMA.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿DÓNDE APRENDEMOS?", acepta("AULA", "EN EL AULA", "EL AULA"), "EN EL AULA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA ESCUELA ES UNA…", ["INSTITUCIÓN", "PLANTA", "COMIDA"], "INSTITUCIÓN", "INSTITUCIÓN.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("LA ESCUELA ES UNA INSTITUCIÓN PORQUE…", ["CUMPLE UNA TAREA PARA TODOS", "TIENE UN PATIO MUY GRANDE", "ES UN EDIFICIO PINTADO"], "CUMPLE UNA TAREA PARA TODOS", "SIRVE PARA APRENDER.", n="analizar")],
 [1, SA("¿PARA QUÉ VAMOS A LA ESCUELA?", acepta("APRENDER", "PARA APRENDER", "JUGAR", "HACER AMIGOS"), "PARA APRENDER.", n="recordar")],
 [1, MC("¿QUIÉNES PUEDEN IR A LA ESCUELA?", ["TODOS LOS CHICOS", "SOLO ALGUNOS", "NADIE"], "TODOS LOS CHICOS", "ES UN DERECHO.", n="recordar")],
 [2, MC("¿QUÉ HACE LA DIRECTORA?", ["ORGANIZA LA ESCUELA", "COCINA EL ALMUERZO", "VENDE GOLOSINAS"], "ORGANIZA LA ESCUELA", "ORGANIZA.", n="recordar")],
 [2, SA("¿QUIÉN PREPARA EL ALMUERZO?", acepta("COCINERA", "LA COCINERA", "COCINERO", "EL COCINERO"), "LA COCINERA.", n="aplicar")],
 [2, MC("SOFI DICE QUE EL TRABAJO DEL PORTERO NO IMPORTA. ¿ESTÁ BIEN?", ["NO: TODOS SON IMPORTANTES", "SÍ: NO IMPORTA", "SÍ: NO ENSEÑA"], "NO: TODOS SON IMPORTANTES", "SIN ÉL LA ESCUELA ESTARÍA SUCIA.", n="error")],
 [3, MC("¿PARA QUÉ SIRVEN LAS NORMAS?", ["PARA CUIDARNOS", "PARA ABURRIRNOS", "PARA NADA"], "PARA CUIDARNOS", "ASÍ ESTAMOS BIEN TODOS.", n="analizar")],
 [3, MC("¿CUÁL ES UNA NORMA DEL AULA?", ["ESPERAR MI TURNO", "GRITAR FUERTE", "TIRAR PAPELES"], "ESPERAR MI TURNO", "ESPERAMOS EL TURNO.", n="aplicar")],
 [3, MC("SI TODOS GRITAN A LA VEZ…", ["NADIE ESCUCHA", "TODOS ENTIENDEN", "APRENDEMOS MÁS"], "NADIE ESCUCHA", "POR ESO LEVANTAMOS LA MANO.", n="analizar")],
 [4, MC("¿DÓNDE ALMORZAMOS?", ["COMEDOR", "BIBLIOTECA", "BAÑO"], "COMEDOR", "EN EL COMEDOR.", n="aplicar")],
 [4, ORD("ORDENÁ: PRIMERO EL AULA, DESPUÉS EL RECREO, AL FINAL LA SALIDA.", ["SALIDA", "AULA", "PATIO"], ["AULA", "PATIO", "SALIDA"], "UN DÍA DE ESCUELA.", n="aplicar")],
 [4, MC("TOMI GRITA EN LA BIBLIOTECA. ¿QUÉ PASA?", ["MOLESTA A LOS QUE LEEN", "ESTÁ BIEN", "LEE MEJOR"], "MOLESTA A LOS QUE LEEN", "EN LA BIBLIOTECA SE HABLA BAJITO.", n="error")],
 [4, SA("¿DÓNDE SALTÁS LA SOGA?", acepta("PATIO", "EN EL PATIO", "EL PATIO"), "EN EL PATIO.", n="aplicar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: mi escuela", "examen_titulo": "Nivel jefe: mi escuela es una institución",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
