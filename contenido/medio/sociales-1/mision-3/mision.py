# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 3 · Mi barrio y sus lugares. Genera mision-3.json.
Regla de primeros años. Metáfora: el paseo por el barrio. Misión COMÚN: sin nombres propios de un país (sirve para todos).
Niveles: 1 recorremos y observamos el barrio · 2 croquis de la manzana de la escuela · 3 lugares para jugar y encontrarnos · 4 placas y monumentos con historia."""
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
"objetivo": "Vas a recorrer y observar tu barrio.",
"vas_a_ver": ["Qué es un barrio", "Qué hay en el barrio", "Observar al caminar"],
"secciones": [
 S(1, "El barrio", [
  D("Barrio", "Parte de una ciudad o pueblo donde vive la gente."),
  P("En el barrio hay <b>casas</b>, <b>negocios</b>, <b>plazas</b> y <b>escuelas</b>."),
  IMG("Mi barrio", "Lo que hay.", FG.tiras(["CASAS", "NEGOCIOS", "PLAZA", "ESCUELA"], numeros=False, cols=2)),
 ]),
 S(1, "Observar al caminar", [
  P("Al caminar <b>miramos</b>, <b>escuchamos</b> y <b>anotamos</b>."),
  IMG("Recorrido", "Paso a paso.", FG.tiras(["SALGO CON UN ADULTO", "MIRO", "ESCUCHO", "ANOTO"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que anotó Sofi. Lo vas a usar en la carpeta."),
  IMG("Registro de Sofi", "En su cuadra.", FG.tiras(["CASAS: 6", "NEGOCIOS: 2", "ÁRBOLES: 4"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La cuadra", "planteo": "Sofi camina con su papá.", "pasos": ["Ve una panadería.", "Escucha autos.", "Anota: PANADERÍA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el barrio hay…", "pasos": ["Casas, negocios y ___."]},
"ejemplo_solo": {"titulo": "Tu barrio", "planteo": "Con un adulto, mirá tu cuadra y dibujá lo que hay."},
"tip": {"titulo": "Siempre acompañado", "texto": "Recorré el barrio con un adulto."},
"ojo": ["Cruzá la calle por la esquina y con un adulto.", "Cada barrio es distinto."],
"resumen": [{"titulo": "Barrio", "texto": "Donde vive la gente."}, {"titulo": "Lugares", "texto": "Casas, negocios, plaza."}, {"titulo": "Observar", "texto": "Mirar y anotar."}],
"glosario": [{"palabra": "Cuadra", "significado": "Calle entre dos esquinas."}, {"palabra": "Negocio", "significado": "Lugar donde se vende algo."}],
"carpeta": ["¿Cuántas casas contó Sofi?", "¿Qué había más: negocios o árboles?", "¿Con quién se recorre el barrio?"],
"respuestas_carpeta": [["6", "seis", "SEIS", "Seis"], acepta("ÁRBOLES", "ARBOLES", "LOS ÁRBOLES"), acepta("CON UN ADULTO", "UN ADULTO", "ADULTO", "CON MI FAMILIA")],
"carpeta_nivel": ["aplicar", "analizar", "recordar"],
"soluciones": {"incompleto": "PLAZAS.", "solo": "Tu dibujo.", "carpeta": ["6.", "ÁRBOLES.", "CON UN ADULTO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a dibujar un croquis de la manzana de la escuela.",
"vas_a_ver": ["La manzana", "Qué es un croquis", "Ubicar lugares"],
"secciones": [
 S(1, "La manzana", [
  D("Manzana", "Grupo de casas rodeado por cuatro calles."),
  P("La manzana tiene <b>cuatro esquinas</b> y <b>cuatro calles</b>."),
  IMG("Una manzana", "Cuatro lados.", FG.tiras(["CALLE 1", "CALLE 2", "CALLE 3", "CALLE 4"], numeros=False, cols=2)),
 ]),
 S(1, "El croquis", [
  D("Croquis", "Dibujo simple de un lugar visto desde arriba."),
  P("En el croquis marcás la <b>escuela</b> y lo que hay <b>al lado</b>."),
  IMG("Croquis", "Visto desde arriba.", FG.tiras(["KIOSCO", "ESCUELA", "CASA", "PANADERÍA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el croquis. Lo vas a usar en la carpeta."),
  IMG("¿Qué hay al lado?", "Mirá bien.", FG.tiras(["KIOSCO", "ESCUELA", "CASA DE SOFI"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi croquis", "planteo": "Tomi dibuja.", "pasos": ["Dibuja un cuadrado: la manzana.", "Marca la escuela.", "Escribe qué hay al lado."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La manzana tiene…", "pasos": ["Cuatro ___."]},
"ejemplo_solo": {"titulo": "Tu croquis", "planteo": "Dibujá un croquis de tu manzana."},
"tip": {"titulo": "Desde arriba", "texto": "Imaginá que sos un pájaro mirando de arriba."},
"ojo": ["En el croquis no hace falta dibujar todo.", "Usá palabras cortas para marcar."],
"resumen": [{"titulo": "Manzana", "texto": "Cuatro calles."}, {"titulo": "Croquis", "texto": "Dibujo desde arriba."}, {"titulo": "Ubicar", "texto": "Al lado, enfrente."}],
"glosario": [{"palabra": "Croquis", "significado": "Dibujo simple de un lugar."}, {"palabra": "Esquina", "significado": "Donde se juntan dos calles."}],
"carpeta": ["¿Qué hay a un lado de la escuela?", "¿Qué hay al otro lado?", "¿Cuántas esquinas tiene una manzana?"],
"respuestas_carpeta": [acepta("KIOSCO", "EL KIOSCO", "CASA DE SOFI", "LA CASA DE SOFI"), acepta("CASA DE SOFI", "LA CASA DE SOFI", "KIOSCO", "EL KIOSCO"), ["4", "cuatro", "CUATRO", "Cuatro"]],
"carpeta_nivel": ["aplicar", "aplicar", "recordar"],
"soluciones": {"incompleto": "CALLES.", "solo": "Tu croquis.", "carpeta": ["EL KIOSCO.", "LA CASA DE SOFI.", "4."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer lugares para jugar y encontrarnos.",
"vas_a_ver": ["La plaza", "Otros lugares", "Cuidarlos"],
"secciones": [
 S(1, "La plaza", [
  D("Espacio público", "Lugar que es de todos y lo puede usar cualquiera."),
  P("En la <b>plaza</b> jugamos, charlamos y nos encontramos."),
  IMG("En la plaza", "Para todos.", FG.tiras(["HAMACAS", "TOBOGÁN", "BANCOS", "ÁRBOLES"], numeros=False, cols=2)),
 ]),
 S(1, "Otros lugares", [
  P("También nos encontramos en el <b>club</b>, la <b>biblioteca</b> y el <b>centro cultural</b>."),
  IMG("Lugares", "Para encontrarnos.", FG.tiras(["PLAZA: JUGAR", "CLUB: DEPORTE", "BIBLIOTECA: LEER"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las actividades. Las vas a usar en la carpeta."),
  IMG("¿Dónde?", "Pensá el lugar.", FG.tiras(["JUGAR AL FÚTBOL", "HAMACARME", "LEER UN CUENTO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El domingo", "planteo": "Sofi va a la plaza.", "pasos": ["Se hamaca.", "Se encuentra con Tomi.", "Juegan juntos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La plaza es…", "pasos": ["La plaza es de ___."]},
"ejemplo_solo": {"titulo": "Tu lugar", "planteo": "Dibujá tu lugar preferido del barrio para jugar."},
"tip": {"titulo": "Es de todos", "texto": "Lo que es de todos, lo cuidamos todos."},
"ojo": ["En la calle no se juega: pasan autos.", "Esperá tu turno en las hamacas."],
"resumen": [{"titulo": "Plaza", "texto": "Para jugar."}, {"titulo": "Público", "texto": "Es de todos."}, {"titulo": "Cuidar", "texto": "Entre todos."}],
"glosario": [{"palabra": "Público", "significado": "De todos."}, {"palabra": "Club", "significado": "Lugar para hacer deporte y encontrarse."}],
"carpeta": ["¿Dónde jugás al fútbol?", "¿Dónde te hamacás?", "Tomi juega a la pelota en la calle. ¿Está bien?"],
"respuestas_carpeta": [acepta("CLUB", "EN EL CLUB", "PLAZA", "EN LA PLAZA"), acepta("PLAZA", "EN LA PLAZA"), acepta("NO", "NO, PASAN AUTOS")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "TODOS.", "solo": "Tu dibujo.", "carpeta": ["EN EL CLUB.", "EN LA PLAZA.", "NO: PASAN AUTOS."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer placas y monumentos con historia.",
"vas_a_ver": ["Monumentos", "Placas", "Cómo cambia el barrio"],
"secciones": [
 S(1, "Monumentos", [
  D("Monumento", "Estatua u obra que recuerda a una persona o un hecho importante."),
  P("En muchas plazas hay un <b>monumento</b>."),
  IMG("El monumento", "Sus partes.", FG.tiras(["ESTATUA", "BASE", "PLACA"], numeros=False, cols=3)),
 ]),
 S(1, "Placas", [
  D("Placa", "Cartel de metal o piedra con algo escrito para recordar."),
  P("La placa dice <b>quién</b> es y <b>cuándo</b> pasó."),
  IMG("Una placa", "Para recordar.", FG.tiras(["QUIÉN", "QUÉ HIZO", "CUÁNDO"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá cómo cambió la plaza. Lo vas a usar en la carpeta."),
  IMG("La plaza", "Antes y hoy.", FG.tiras(["HACE MUCHO: TIERRA", "DESPUÉS: ÁRBOLES", "HOY: JUEGOS"], numeros=True, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La placa", "planteo": "Sofi lee una placa.", "pasos": ["Tiene un nombre.", "Tiene una fecha.", "Recuerda a una persona."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Un monumento sirve para…", "pasos": ["___ a alguien importante."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Con un adulto, buscá una placa en tu barrio. ¿Qué dice?"},
"tip": {"titulo": "Preguntá a los grandes", "texto": "Los abuelos saben cómo era el barrio antes."},
"ojo": ["Los monumentos no se rayan ni se trepan.", "El barrio cambia con el tiempo."],
"resumen": [{"titulo": "Monumento", "texto": "Recuerda algo importante."}, {"titulo": "Placa", "texto": "Quién y cuándo."}, {"titulo": "Cambios", "texto": "Antes y hoy."}],
"glosario": [{"palabra": "Recordar", "significado": "Traer algo a la memoria."}, {"palabra": "Estatua", "significado": "Figura de piedra o metal."}],
"carpeta": ["Hace mucho, ¿cómo era la plaza?", "¿Qué hay hoy en la plaza?", "Tomi raya el monumento. ¿Está bien?"],
"respuestas_carpeta": [acepta("DE TIERRA", "TIERRA"), acepta("JUEGOS", "HAY JUEGOS"), acepta("NO", "NO, SE CUIDA")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "RECORDAR.", "solo": "Lo que dice la placa.", "carpeta": ["DE TIERRA.", "JUEGOS.", "NO: SE CUIDA."]},
}

ACT = {
"1": [MC("¿QUÉ HAY EN UN BARRIO?", ["CASAS Y NEGOCIOS", "SOLO MAR", "SOLO NIEVE"], "CASAS Y NEGOCIOS", "Y PLAZAS Y ESCUELAS.", n="recordar"),
      MC("SOFI QUIERE RECORRER EL BARRIO. ¿QUÉ HACE PRIMERO?", ["PIDE QUE LA ACOMPAÑE UN ADULTO", "SALE SOLA", "CRUZA CORRIENDO"], "PIDE QUE LA ACOMPAÑE UN ADULTO", "SIEMPRE CON UN ADULTO.", n="aplicar")],
"2": [MC("¿QUÉ ES UN CROQUIS?", ["UN DIBUJO DESDE ARRIBA", "UN CUENTO", "UNA CANCIÓN"], "UN DIBUJO DESDE ARRIBA", "DIBUJO SIMPLE DE UN LUGAR.", n="recordar"),
      SA("¿CUÁNTAS CALLES RODEAN UNA MANZANA?", ["4", "cuatro", "CUATRO"], "CUATRO CALLES.", n="aplicar")],
"3": [MC("¿DE QUIÉN ES LA PLAZA?", ["DE TODOS", "DE NADIE", "DE UNO SOLO"], "DE TODOS", "ES UN ESPACIO PÚBLICO.", n="recordar"),
      MC("¿POR QUÉ NO SE JUEGA EN LA CALLE?", ["PASAN AUTOS", "ES ABURRIDA", "ES CHIQUITA"], "PASAN AUTOS", "ES PELIGROSO.", n="analizar")],
"4": [MC("¿PARA QUÉ SIRVE UN MONUMENTO?", ["PARA RECORDAR", "PARA JUGAR", "PARA COMER"], "PARA RECORDAR", "RECUERDA ALGO IMPORTANTE.", n="recordar"),
      ORD("ORDENÁ CÓMO CAMBIÓ LA PLAZA.", ["HOY: JUEGOS", "HACE MUCHO: TIERRA", "DESPUÉS: ÁRBOLES"], ["HACE MUCHO: TIERRA", "DESPUÉS: ÁRBOLES", "HOY: JUEGOS"], "DE ANTES A HOY.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿DÓNDE TE HAMACÁS?", ["PLAZA", "CALLE", "KIOSCO"], "PLAZA", "EN LA PLAZA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA CALLE ENTRE DOS ESQUINAS ES UNA…", ["CUADRA", "PLAZA", "PLACA"], "CUADRA", "CUADRA.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿CON QUIÉN SE CRUZA LA CALLE?", acepta("CON UN ADULTO", "UN ADULTO", "ADULTO"), "CON UN ADULTO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿QUÉ TIENE ESCRITO UNA PLACA?", ["QUIÉN Y CUÁNDO", "UN CHISTE", "NADA"], "QUIÉN Y CUÁNDO", "PARA RECORDAR.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("UN BARRIO ES…", ["PARTE DE UNA CIUDAD O PUEBLO", "UN ANIMAL DEL CAMPO", "UN JUEGO DE PATIO"], "PARTE DE UNA CIUDAD O PUEBLO", "DONDE VIVE LA GENTE.", n="recordar")],
 [1, SA("SOFI CONTÓ 6 CASAS Y 2 NEGOCIOS. ¿CUÁNTOS LUGARES CONTÓ?", ["8", "ocho", "OCHO"], "6 + 2 = 8.", n="aplicar")],
 [1, MC("TOMI CRUZA LA CALLE A MITAD DE CUADRA. ¿QUÉ CONVIENE?", ["CRUZAR POR LA ESQUINA", "CORRER MÁS RÁPIDO", "CERRAR LOS OJOS"], "CRUZAR POR LA ESQUINA", "Y CON UN ADULTO.", n="error")],
 [2, MC("LA MANZANA ESTÁ RODEADA POR…", ["CUATRO CALLES", "UN RÍO", "UNA PARED"], "CUATRO CALLES", "TIENE CUATRO LADOS.", n="recordar")],
 [2, MC("EN EL CROQUIS DIBUJAMOS EL LUGAR VISTO…", ["DESDE ARRIBA", "DESDE ADENTRO", "CON LOS OJOS CERRADOS"], "DESDE ARRIBA", "COMO UN PÁJARO.", n="recordar")],
 [2, MC("EN EL CROQUIS: KIOSCO, ESCUELA, CASA DE SOFI. ¿QUÉ HAY ENTRE EL KIOSCO Y LA CASA?", ["LA ESCUELA", "LA PLAZA", "EL CLUB"], "LA ESCUELA", "ESTÁ EN EL MEDIO.", n="analizar")],
 [3, MC("UN ESPACIO PÚBLICO ES…", ["DE TODOS", "DE UNA SOLA PERSONA", "SOLO PARA GRANDES"], "DE TODOS", "COMO LA PLAZA.", n="recordar")],
 [3, SA("¿DÓNDE PODÉS LEER UN CUENTO EN EL BARRIO?", acepta("BIBLIOTECA", "EN LA BIBLIOTECA", "LA BIBLIOTECA"), "EN LA BIBLIOTECA.", n="aplicar")],
 [3, MC("HAY UNA FILA EN LAS HAMACAS. ¿QUÉ HACÉS?", ["ESPERO MI TURNO", "EMPUJO", "ME VOY ENOJADO"], "ESPERO MI TURNO", "RESPETAMOS EL TURNO.", n="aplicar")],
 [4, MC("UNA PLACA SIRVE PARA…", ["RECORDAR ALGO IMPORTANTE", "JUGAR A LA PELOTA", "TAPAR UN POZO"], "RECORDAR ALGO IMPORTANTE", "DICE QUIÉN Y CUÁNDO.", n="recordar")],
 [4, MC("¿CÓMO SABÉS CÓMO ERA EL BARRIO ANTES?", ["PREGUNTO A LOS ABUELOS", "LO INVENTO", "NO SE PUEDE"], "PREGUNTO A LOS ABUELOS", "ELLOS RECUERDAN.", n="analizar")],
 [4, MC("SOFI SE TREPA AL MONUMENTO. ¿QUÉ PROBLEMA HAY?", ["PUEDE ROMPERLO Y CAERSE", "NINGUNO", "LO LIMPIA"], "PUEDE ROMPERLO Y CAERSE", "LOS MONUMENTOS SE CUIDAN.", n="error")],
 [4, ORD("ORDENÁ: DE ANTES A HOY.", ["HOY", "HACE MUCHO", "DESPUÉS"], ["HACE MUCHO", "DESPUÉS", "HOY"], "EL TIEMPO PASA.", n="aplicar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: mi barrio", "examen_titulo": "Nivel jefe: mi barrio y sus lugares",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
