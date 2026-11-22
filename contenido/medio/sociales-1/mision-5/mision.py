# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 5 · El campo y la ciudad. Genera mision-5.json.
Regla de primeros años. Metáfora: el viaje en micro de la ciudad al campo.
Niveles: 1 paisajes del campo · 2 paisajes de la ciudad · 3 qué hay en el campo y en la ciudad · 4 comparamos un pueblo y una ciudad."""
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
"objetivo": "Vas a conocer los paisajes del campo.",
"vas_a_ver": ["Qué es un paisaje", "Cómo es el campo", "Quiénes viven ahí"],
"secciones": [
 S(1, "El paisaje", [
  D("Paisaje", "Todo lo que vemos en un lugar."),
  P("En el campo hay <b>mucho espacio</b>, <b>plantaciones</b> y <b>animales</b>."),
  IMG("El campo", "Lo que vemos.", FG.tiras(["CAMPOS SEMBRADOS", "VACAS Y CABALLOS", "POCAS CASAS", "CAMINOS DE TIERRA"], numeros=False, cols=2)),
 ]),
 S(1, "Vivir en el campo", [
  P("Las casas están <b>lejos</b> unas de otras. Hay mucho <b>silencio</b>."),
  IMG("En el campo", "Así se vive.", FG.tiras(["CASAS LEJOS", "SILENCIO", "CIELO GRANDE"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que vio Sofi. Lo vas a usar en la carpeta."),
  IMG("El viaje de Sofi", "Por la ventana.", FG.tiras(["VACAS: 10", "CASAS: 2", "TRACTORES: 1"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Desde el micro", "planteo": "Sofi mira por la ventana.", "pasos": ["Ve campos verdes.", "Ve vacas.", "Ve pocas casas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el campo las casas…", "pasos": ["Están ___ unas de otras."]},
"ejemplo_solo": {"titulo": "Dibujá", "planteo": "Dibujá un paisaje del campo."},
"tip": {"titulo": "Mirá todo", "texto": "El paisaje es todo lo que ves: cielo, suelo, casas."},
"ojo": ["En el campo también vive gente.", "Hay campos con cultivos y campos con animales."],
"resumen": [{"titulo": "Paisaje", "texto": "Lo que vemos."}, {"titulo": "Campo", "texto": "Espacio, plantas, animales."}, {"titulo": "Casas", "texto": "Lejos unas de otras."}],
"glosario": [{"palabra": "Paisaje", "significado": "Todo lo que vemos en un lugar."}, {"palabra": "Cultivo", "significado": "Plantas que siembra la gente."}],
"carpeta": ["¿Cuántas vacas vio Sofi?", "¿Qué vio más: casas o vacas?", "¿Cómo están las casas en el campo?"],
"respuestas_carpeta": [["10", "diez", "DIEZ", "Diez"], acepta("VACAS", "LAS VACAS"), acepta("LEJOS", "SEPARADAS", "LEJOS UNAS DE OTRAS")],
"carpeta_nivel": ["aplicar", "analizar", "recordar"],
"soluciones": {"incompleto": "LEJOS.", "solo": "Tu dibujo.", "carpeta": ["10.", "VACAS.", "LEJOS."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer los paisajes de la ciudad.",
"vas_a_ver": ["Cómo es la ciudad", "Mucho movimiento", "Vivir en la ciudad"],
"secciones": [
 S(1, "La ciudad", [
  P("En la ciudad hay <b>edificios</b>, <b>calles asfaltadas</b>, <b>semáforos</b> y <b>negocios</b>."),
  IMG("La ciudad", "Lo que vemos.", FG.tiras(["EDIFICIOS", "SEMÁFOROS", "COLECTIVOS", "NEGOCIOS"], numeros=False, cols=2)),
 ]),
 S(1, "Mucho movimiento", [
  D("Ciudad", "Lugar con muchas casas, edificios y gente."),
  P("Pasan muchos <b>autos</b> y <b>colectivos</b>. Hay <b>ruido</b>."),
  IMG("Movimiento", "Mucha gente.", FG.tiras(["MUCHOS AUTOS", "MUCHA GENTE", "RUIDO"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que contó Tomi en un minuto. Lo vas a usar en la carpeta."),
  IMG("En la esquina", "Autos que pasaron.", FG.tiras(["CIUDAD: 20 AUTOS", "CAMPO: 1 AUTO"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "La esquina", "planteo": "Tomi espera para cruzar.", "pasos": ["Mira el semáforo.", "Espera la luz verde.", "Cruza con su mamá."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En la ciudad hay…", "pasos": ["Muchos edificios y ___."]},
"ejemplo_solo": {"titulo": "Escuchá", "planteo": "Cerrá los ojos en la vereda. ¿Qué ruidos escuchás?"},
"tip": {"titulo": "El semáforo", "texto": "Con luz verde para peatones se cruza."},
"ojo": ["En la ciudad, cruzá siempre con un adulto.", "En la ciudad también hay plazas y árboles."],
"resumen": [{"titulo": "Ciudad", "texto": "Edificios y gente."}, {"titulo": "Movimiento", "texto": "Autos, colectivos."}, {"titulo": "Ruido", "texto": "Mucho más que el campo."}],
"glosario": [{"palabra": "Semáforo", "significado": "Luces que dicen cuándo cruzar."}, {"palabra": "Edificio", "significado": "Construcción alta con muchos pisos."}],
"carpeta": ["¿Cuántos autos pasaron en la ciudad?", "¿Dónde pasaron más autos?", "¿Cuántos más pasaron en la ciudad que en el campo?"],
"respuestas_carpeta": [["20", "veinte", "VEINTE"], acepta("CIUDAD", "EN LA CIUDAD", "LA CIUDAD"), ["19", "diecinueve", "DIECINUEVE"]],
"carpeta_nivel": ["aplicar", "analizar", "aplicar"],
"soluciones": {"incompleto": "GENTE.", "solo": "Autos, bocinas, gente.", "carpeta": ["20.", "EN LA CIUDAD.", "19."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a comparar el campo y la ciudad.",
"vas_a_ver": ["Solo en el campo", "Solo en la ciudad", "En los dos"],
"secciones": [
 S(1, "Campo y ciudad", [
  P("En el campo hay <b>tractores</b> y <b>vacas</b>. En la ciudad, <b>edificios</b> y <b>semáforos</b>."),
  IMG("Distintos", "Cada uno lo suyo.", FG.tiras(["CAMPO: TRACTOR, VACAS", "CIUDAD: EDIFICIOS, SEMÁFOROS"], numeros=False, cols=1)),
 ]),
 S(1, "En los dos", [
  D("Comparar", "Ver en qué se parecen y en qué son distintos."),
  P("En los dos hay <b>escuelas</b>, <b>casas</b> y <b>familias</b>."),
  IMG("En los dos", "Se parecen.", FG.tiras(["ESCUELAS", "CASAS", "FAMILIAS"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("¿Campo o ciudad?", "Pensá.", FG.nombres(["TRACTOR", "SEMÁFORO", "ESCUELA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Comparamos", "planteo": "Sofi vive en la ciudad. Su prima, en el campo.", "pasos": ["Las dos van a la escuela.", "Sofi va en colectivo.", "Su prima va a caballo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el campo y en la ciudad hay…", "pasos": ["Escuelas y ___."]},
"ejemplo_solo": {"titulo": "Tu lugar", "planteo": "¿Vivís en el campo o en la ciudad? Dibujá algo de tu lugar."},
"tip": {"titulo": "Parecido y distinto", "texto": "Buscá primero lo que se parece."},
"ojo": ["Ningún lugar es mejor que otro.", "En los dos lugares hay gente que trabaja."],
"resumen": [{"titulo": "Campo", "texto": "Tractores, vacas."}, {"titulo": "Ciudad", "texto": "Edificios, semáforos."}, {"titulo": "Los dos", "texto": "Escuelas y familias."}],
"glosario": [{"palabra": "Comparar", "significado": "Buscar parecidos y diferencias."}, {"palabra": "Tractor", "significado": "Máquina para trabajar el campo."}],
"carpeta": ["El tractor, ¿campo o ciudad?", "El semáforo, ¿campo o ciudad?", "La escuela, ¿campo, ciudad o los dos?"],
"respuestas_carpeta": [acepta("CAMPO", "EL CAMPO", "EN EL CAMPO"), acepta("CIUDAD", "LA CIUDAD", "EN LA CIUDAD"), acepta("LOS DOS", "EN LOS DOS", "AMBOS")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "CASAS.", "solo": "Tu dibujo.", "carpeta": ["CAMPO.", "CIUDAD.", "LOS DOS."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a comparar un pueblo y una ciudad.",
"vas_a_ver": ["El pueblo", "La ciudad", "Un pueblo que crece"],
"secciones": [
 S(1, "El pueblo", [
  D("Pueblo", "Lugar con pocas calles, donde casi todos se conocen."),
  P("En el pueblo hay una <b>plaza</b>, una <b>escuela</b> y pocos <b>negocios</b>."),
  IMG("Pueblo y ciudad", "Tamaños.", FG.tiras(["PUEBLO: CHICO", "CIUDAD: GRANDE"], numeros=False, cols=2)),
 ]),
 S(1, "Un pueblo que crece", [
  P("Con el tiempo, un pueblo puede <b>crecer</b> y hacerse ciudad."),
  IMG("Crece", "Con el tiempo.", FG.tiras(["POCAS CASAS", "MÁS CASAS", "EDIFICIOS"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las frases. Las vas a usar en la carpeta."),
  IMG("¿Pueblo o ciudad?", "Pensá.", FG.tiras(["TODOS SE CONOCEN", "HAY SUBTE Y EDIFICIOS", "UNA SOLA PLAZA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El pueblo del abuelo", "planteo": "El abuelo cuenta.", "pasos": ["Había pocas casas.", "Después hicieron más.", "Hoy es una ciudad."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el pueblo…", "pasos": ["Casi todos se ___."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntá en casa si tu lugar era más chico antes."},
"tip": {"titulo": "Mirá el tamaño", "texto": "Pocas calles: pueblo. Muchas calles: ciudad."},
"ojo": ["Los pueblos y las ciudades cambian con el tiempo.", "Los dos tienen escuelas y familias."],
"resumen": [{"titulo": "Pueblo", "texto": "Chico, todos se conocen."}, {"titulo": "Ciudad", "texto": "Grande, mucha gente."}, {"titulo": "Cambia", "texto": "Un pueblo puede crecer."}],
"glosario": [{"palabra": "Pueblo", "significado": "Lugar chico con pocas calles."}, {"palabra": "Crecer", "significado": "Hacerse más grande."}],
"carpeta": ["Todos se conocen, ¿pueblo o ciudad?", "Hay subte y edificios, ¿pueblo o ciudad?", "¿Un pueblo puede hacerse ciudad?"],
"respuestas_carpeta": [acepta("PUEBLO", "EL PUEBLO"), acepta("CIUDAD", "LA CIUDAD"), acepta("SÍ", "SI", "SÍ, SI CRECE")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "CONOCEN.", "solo": "Lo que te contaron.", "carpeta": ["PUEBLO.", "CIUDAD.", "SÍ."]},
}

ACT = {
"1": [MC("¿QUÉ HAY EN EL CAMPO?", ["VACAS Y SEMBRADOS", "SUBTES Y EDIFICIOS", "SEMÁFOROS"], "VACAS Y SEMBRADOS", "Y POCAS CASAS.", n="recordar"),
      MC("EN UN LUGAR LAS CASAS ESTÁN MUY LEJOS. ¿DÓNDE ES?", ["EN EL CAMPO", "EN EL CENTRO DE LA CIUDAD", "EN UN EDIFICIO"], "EN EL CAMPO", "HAY MUCHO ESPACIO.", n="analizar")],
"2": [MC("¿QUÉ HAY EN LA CIUDAD?", ["EDIFICIOS Y SEMÁFOROS", "SOLO VACAS", "SOLO CAMPOS"], "EDIFICIOS Y SEMÁFOROS", "Y MUCHA GENTE.", n="recordar"),
      SA("EN LA CIUDAD PASARON 20 AUTOS Y EN EL CAMPO 1. ¿CUÁNTOS MÁS EN LA CIUDAD?", ["19", "diecinueve", "DIECINUEVE"], "20 − 1 = 19.", n="aplicar")],
"3": [MC("¿QUÉ HAY EN EL CAMPO Y EN LA CIUDAD?", ["ESCUELAS", "TRACTORES", "SUBTES"], "ESCUELAS", "HAY EN LOS DOS.", n="analizar"),
      MC("TOMI DICE QUE EN EL CAMPO NO VIVE NADIE. ¿ESTÁ BIEN?", ["NO: VIVEN FAMILIAS", "SÍ: NO HAY NADIE", "SÍ: SOLO VACAS"], "NO: VIVEN FAMILIAS", "EN EL CAMPO TAMBIÉN VIVE GENTE.", n="error")],
"4": [MC("¿QUÉ ES UN PUEBLO?", ["UN LUGAR CHICO CON POCAS CALLES", "UNA CIUDAD GIGANTE", "UN EDIFICIO ALTO DEL CENTRO"], "UN LUGAR CHICO CON POCAS CALLES", "CASI TODOS SE CONOCEN.", n="recordar"),
      ORD("ORDENÁ CÓMO CRECE UN PUEBLO.", ["EDIFICIOS", "POCAS CASAS", "MÁS CASAS"], ["POCAS CASAS", "MÁS CASAS", "EDIFICIOS"], "CON EL TIEMPO CRECE.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿DÓNDE HAY TRACTORES?", ["CAMPO", "CIUDAD", "SUBTE"], "CAMPO", "EN EL CAMPO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿DÓNDE HAY MÁS RUIDO?", ["CIUDAD", "CAMPO", "IGUAL"], "CIUDAD", "MÁS AUTOS Y GENTE.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. TODO LO QUE VEMOS EN UN LUGAR ES EL…", acepta("PAISAJE", "EL PAISAJE"), "PAISAJE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿DÓNDE CASI TODOS SE CONOCEN?", ["PUEBLO", "CIUDAD GRANDE", "AEROPUERTO"], "PUEBLO", "EN EL PUEBLO.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("EL PAISAJE ES…", ["TODO LO QUE VEMOS", "UNA COMIDA", "UN JUEGO"], "TODO LO QUE VEMOS", "CIELO, SUELO, CASAS.", n="recordar")],
 [1, MC("¿CÓMO SON LOS CAMINOS EN EL CAMPO?", ["MUCHOS SON DE TIERRA", "TODOS TIENEN SEMÁFORO", "SON DE AGUA"], "MUCHOS SON DE TIERRA", "CAMINOS DE TIERRA.", n="recordar")],
 [1, SA("SOFI VIO 10 VACAS Y 2 CASAS. ¿CUÁNTAS COSAS VIO?", ["12", "doce", "DOCE"], "10 + 2 = 12.", n="aplicar")],
 [2, MC("EN LA CIUDAD, ¿PARA QUÉ SIRVE EL SEMÁFORO?", ["PARA SABER CUÁNDO CRUZAR", "PARA ILUMINAR LA PLAZA", "PARA DECORAR"], "PARA SABER CUÁNDO CRUZAR", "LUZ VERDE PARA CRUZAR.", n="analizar")],
 [2, MC("¿DÓNDE HAY MÁS EDIFICIOS?", ["EN LA CIUDAD", "EN EL CAMPO", "IGUAL"], "EN LA CIUDAD", "LA CIUDAD TIENE EDIFICIOS.", n="aplicar")],
 [2, MC("SOFI CRUZA LA AVENIDA SOLA Y CON LUZ ROJA. ¿QUÉ ESTÁ MAL?", ["CRUZA SOLA Y CON ROJO", "NADA", "CAMINA DESPACIO"], "CRUZA SOLA Y CON ROJO", "SE CRUZA CON UN ADULTO Y CON VERDE.", n="error")],
 [3, MC("¿QUÉ HAY SOLO EN EL CAMPO?", ["TRACTORES Y SEMBRADOS", "ESCUELAS", "FAMILIAS"], "TRACTORES Y SEMBRADOS", "ES DEL CAMPO.", n="aplicar")],
 [3, SA("EL SEMÁFORO, ¿CAMPO O CIUDAD?", acepta("CIUDAD", "LA CIUDAD", "EN LA CIUDAD"), "CIUDAD.", n="aplicar")],
 [3, MC("COMPARAR ES…", ["BUSCAR PARECIDOS Y DIFERENCIAS", "CONTAR HASTA DIEZ", "PINTAR UN DIBUJO"], "BUSCAR PARECIDOS Y DIFERENCIAS", "PARECIDO Y DISTINTO.", n="recordar")],
 [4, MC("EN EL PUEBLO…", ["CASI TODOS SE CONOCEN", "HAY MILES DE EDIFICIOS", "HAY SUBTES"], "CASI TODOS SE CONOCEN", "ES CHICO.", n="recordar")],
 [4, ORD("ORDENÁ CÓMO CRECE UN PUEBLO.", ["MÁS CASAS", "EDIFICIOS", "POCAS CASAS"], ["POCAS CASAS", "MÁS CASAS", "EDIFICIOS"], "CON EL TIEMPO.", n="aplicar")],
 [4, MC("TOMI DICE QUE LA CIUDAD ES MEJOR QUE EL PUEBLO. ¿QUÉ PENSÁS?", ["NINGUNO ES MEJOR", "LA CIUDAD ES MEJOR", "EL PUEBLO NO SIRVE"], "NINGUNO ES MEJOR", "SON DISTINTOS.", n="error")],
 [4, SA("UN PUEBLO PUEDE CRECER Y HACERSE…", acepta("CIUDAD", "UNA CIUDAD"), "CIUDAD.", n="aplicar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: el campo y la ciudad", "examen_titulo": "Nivel jefe: el campo y la ciudad",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
