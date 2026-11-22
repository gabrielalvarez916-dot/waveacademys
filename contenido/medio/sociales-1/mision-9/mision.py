# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 9 · Ordenar el tiempo. Genera mision-9.json.
Regla de primeros años. Metáfora: el calendario mágico de Sofi.
Niveles: 1 ayer, hoy y mañana en mi día · 2 los días y los meses del calendario escolar · 3 mi línea de tiempo personal · 4 huellas del pasado en fotos y objetos."""
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
"objetivo": "Vas a ordenar lo que pasó ayer, hoy y mañana.",
"vas_a_ver": ["Ayer", "Hoy", "Mañana"],
"secciones": [
 S(1, "Ayer, hoy y mañana", [
  D("Tiempo", "Lo que pasa uno después de otro: antes, ahora y después."),
  P("<b>Ayer</b> ya pasó. <b>Hoy</b> es ahora. <b>Mañana</b> todavía no llegó."),
  IMG("Los días", "En orden.", FG.tiras(["AYER", "HOY", "MAÑANA"], numeros=True, cols=3)),
 ]),
 S(1, "Mi día", [
  P("El día tiene <b>mañana</b>, <b>tarde</b> y <b>noche</b>."),
  IMG("Mi día", "Lo que hago.", FG.tiras(["MAÑANA: ESCUELA", "TARDE: JUGAR", "NOCHE: DORMIR"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que contó Sofi. Lo vas a usar en la carpeta."),
  IMG("Lo que contó Sofi", "¿Ayer, hoy o mañana?", FG.tiras(["FUI A LA PLAZA", "ESTOY EN LA ESCUELA", "VOY A UN CUMPLE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi cuenta", "planteo": "Ordenamos.", "pasos": ["Ayer jugó al fútbol.", "Hoy fue a la escuela.", "Mañana visita a la abuela."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Lo que ya pasó es…", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu día", "planteo": "Dibujá algo que hiciste ayer y algo que harás mañana."},
"tip": {"titulo": "Palabras del tiempo", "texto": "Antes, ahora y después ordenan lo que pasa."},
"ojo": ["Mañana puede ser el día que viene o la mañana de hoy.", "Ayer no vuelve: ya pasó."],
"resumen": [{"titulo": "Ayer", "texto": "Ya pasó."}, {"titulo": "Hoy", "texto": "Ahora."}, {"titulo": "Mañana", "texto": "Todavía no llegó."}],
"glosario": [{"palabra": "Ayer", "significado": "El día que ya pasó."}, {"palabra": "Mañana", "significado": "El día que viene."}],
"carpeta": ["Fui a la plaza: ¿ayer, hoy o mañana?", "Estoy en la escuela: ¿ayer, hoy o mañana?", "Voy a un cumple: ¿ayer, hoy o mañana?"],
"respuestas_carpeta": [acepta("AYER"), acepta("HOY"), acepta("MAÑANA", "MANANA")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "AYER.", "solo": "Tus dibujos.", "carpeta": ["AYER.", "HOY.", "MAÑANA."]},
}

N2 = {**ESTILO, "meses_ok": True,
"objetivo": "Vas a conocer los días y los meses del calendario.",
"vas_a_ver": ["Los días de la semana", "Los meses del año", "El calendario escolar"],
"secciones": [
 S(1, "Los días", [
  D("Semana", "Siete días seguidos."),
  P("De <b>lunes a viernes</b> vamos a la escuela. <b>Sábado y domingo</b> descansamos."),
  IMG("La semana", "Siete días.", FG.tiras(["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"], numeros=True, cols=4)),
 ]),
 S(1, "Los meses", [
  D("Calendario", "Hoja que muestra los días y los meses del año."),
  P("El año tiene <b>12 meses</b>. El calendario escolar marca clases y vacaciones."),
  IMG("Los meses", "Doce meses.", FG.tiras(["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"], numeros=True, cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la semana. La vas a usar en la carpeta."),
  IMG("Mi semana", "¿Hay escuela?", FG.tiras(["LUNES", "SÁBADO", "MIÉRCOLES"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi cumple", "planteo": "Sofi busca su cumple.", "pasos": ["Busca el mes.", "Busca el número.", "¡Lo marca con un corazón!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Después del lunes viene el…", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu cumple", "planteo": "Buscá en un calendario el mes de tu cumpleaños."},
"tip": {"titulo": "Cantá", "texto": "Decí los días como una canción."},
"ojo": ["La semana tiene 7 días.", "El año tiene 12 meses."],
"resumen": [{"titulo": "Semana", "texto": "7 días."}, {"titulo": "Año", "texto": "12 meses."}, {"titulo": "Calendario", "texto": "Clases y vacaciones."}],
"glosario": [{"palabra": "Calendario", "significado": "Muestra días y meses."}, {"palabra": "Vacaciones", "significado": "Días sin clases."}],
"carpeta": ["El lunes, ¿hay escuela?", "El sábado, ¿hay escuela?", "¿Cuántos días tiene la semana?"],
"respuestas_carpeta": [acepta("SÍ", "SI"), acepta("NO"), ["7", "siete", "SIETE", "Siete"]],
"carpeta_nivel": ["aplicar", "aplicar", "recordar"],
"soluciones": {"incompleto": "MARTES.", "solo": "El mes de tu cumple.", "carpeta": ["SÍ.", "NO.", "7."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a armar tu línea de tiempo.",
"vas_a_ver": ["Qué es una línea de tiempo", "Mis momentos", "Ordenar"],
"secciones": [
 S(1, "La línea de tiempo", [
  D("Línea de tiempo", "Línea donde ponemos los hechos en orden."),
  P("A la izquierda va lo de <b>antes</b>. A la derecha, lo de <b>ahora</b>."),
  IMG("Mi línea", "De antes a ahora.", FG.tiras(["NACÍ", "CAMINÉ", "JARDÍN", "PRIMER GRADO"], numeros=True, cols=4)),
 ]),
 S(1, "Mis momentos", [
  P("Elegís <b>momentos</b> importantes y los ponés en orden."),
  IMG("Momentos", "Importantes.", FG.tiras(["MI PRIMER DIENTE", "MI PRIMERA PALABRA", "APRENDÍ A LEER"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la línea de Tomi. La vas a usar en la carpeta."),
  IMG("La línea de Tomi", "¿Está en orden?", FG.tiras(["JARDÍN", "NACÍ", "PRIMER GRADO"], numeros=True, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La línea de Sofi", "planteo": "Sofi ordena.", "pasos": ["Primero: nací.", "Después: fui al jardín.", "Ahora: primer grado."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En la línea, lo de antes va…", "pasos": ["A la ___."]},
"ejemplo_solo": {"titulo": "Tu línea", "planteo": "Dibujá tu línea de tiempo con 3 momentos."},
"tip": {"titulo": "Preguntá en casa", "texto": "Tu familia recuerda cuándo pasó cada cosa."},
"ojo": ["Primero va lo más viejo.", "Al final va lo de ahora."],
"resumen": [{"titulo": "Línea", "texto": "Hechos en orden."}, {"titulo": "Antes", "texto": "A la izquierda."}, {"titulo": "Ahora", "texto": "A la derecha."}],
"glosario": [{"palabra": "Hecho", "significado": "Algo que pasó."}, {"palabra": "Orden", "significado": "Uno después de otro."}],
"carpeta": ["¿Qué foto está mal ubicada en la línea de Tomi?", "¿Qué va primero?", "¿Qué va al final?"],
"respuestas_carpeta": [acepta("JARDÍN", "JARDIN", "NACÍ", "NACI"), acepta("NACÍ", "NACI"), acepta("PRIMER GRADO")],
"carpeta_nivel": ["error", "aplicar", "aplicar"],
"soluciones": {"incompleto": "IZQUIERDA.", "solo": "Tu línea.", "carpeta": ["JARDÍN Y NACÍ ESTÁN AL REVÉS.", "NACÍ.", "PRIMER GRADO."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a buscar huellas del pasado en fotos y objetos.",
"vas_a_ver": ["Qué es una huella del pasado", "Fotos viejas", "Objetos viejos"],
"secciones": [
 S(1, "Huellas del pasado", [
  D("Huella del pasado", "Algo que nos cuenta cómo era antes."),
  P("Una <b>foto vieja</b> o un <b>objeto</b> nos cuentan cómo se vivía."),
  IMG("Huellas", "Nos cuentan.", FG.tiras(["FOTO VIEJA", "JUGUETE ANTIGUO", "CARTA"], numeros=False, cols=3)),
 ]),
 S(1, "Qué nos cuentan", [
  P("En una foto miramos <b>quiénes</b> están, <b>dónde</b> y <b>cómo</b> se vestían."),
  IMG("Una foto", "Preguntas.", FG.tiras(["¿QUIÉNES?", "¿DÓNDE?", "¿CÓMO SE VESTÍAN?"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que vio Sofi en la foto. Lo vas a usar en la carpeta."),
  IMG("La foto de la abuela", "Lo que se ve.", FG.tiras(["BLANCO Y NEGRO", "LA ABUELA DE CHICA", "UNA CARRETA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La foto", "planteo": "Sofi mira una foto vieja.", "pasos": ["Es en blanco y negro.", "Está la abuela de chica.", "Hay una carreta: era hace mucho."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Una huella del pasado nos cuenta…", "pasos": ["Cómo era ___."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá en casa una foto vieja y contá qué ves."},
"tip": {"titulo": "Cuidalas", "texto": "Las fotos viejas se tocan con cuidado."},
"ojo": ["Pedí permiso para mirar fotos de la familia.", "Antes muchas fotos eran en blanco y negro."],
"resumen": [{"titulo": "Huella", "texto": "Cuenta cómo era antes."}, {"titulo": "Fotos", "texto": "Quiénes, dónde, cómo."}, {"titulo": "Objetos", "texto": "Juguetes, cartas."}],
"glosario": [{"palabra": "Pasado", "significado": "Lo que ya pasó."}, {"palabra": "Antiguo", "significado": "Muy viejo."}],
"carpeta": ["¿De qué color era la foto?", "¿Quién estaba en la foto?", "¿Cómo sabés que la foto es vieja?"],
"respuestas_carpeta": [acepta("BLANCO Y NEGRO", "EN BLANCO Y NEGRO"), acepta("LA ABUELA", "ABUELA", "LA ABUELA DE CHICA"), acepta("HAY UNA CARRETA", "POR LA CARRETA", "ES EN BLANCO Y NEGRO", "BLANCO Y NEGRO", "LA ABUELA ES CHICA")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "ANTES.", "solo": "Lo que viste.", "carpeta": ["BLANCO Y NEGRO.", "LA ABUELA.", "POR LA CARRETA."]},
}

ACT = {
"1": [MC("LO QUE YA PASÓ ES…", ["AYER", "MAÑANA", "HOY"], "AYER", "AYER YA PASÓ.", n="recordar"),
      ORD("ORDENÁ.", ["MAÑANA", "AYER", "HOY"], ["AYER", "HOY", "MAÑANA"], "AYER, HOY, MAÑANA.", n="aplicar")],
"2": [SA("¿CUÁNTOS MESES TIENE EL AÑO?", ["12", "doce", "DOCE"], "12 MESES.", n="recordar"),
      MC("¿QUÉ DÍA VIENE DESPUÉS DEL VIERNES?", ["SÁBADO", "LUNES", "JUEVES"], "SÁBADO", "VIERNES, SÁBADO.", n="aplicar")],
"3": [MC("EN LA LÍNEA DE TIEMPO, ¿QUÉ VA PRIMERO?", ["LO MÁS VIEJO", "LO DE AHORA", "LO QUE QUIERO"], "LO MÁS VIEJO", "DE ANTES A AHORA.", n="recordar"),
      MC("TOMI PUSO PRIMER GRADO ANTES QUE NACÍ. ¿QUÉ PASÓ?", ["ESTÁ AL REVÉS", "ESTÁ BIEN", "FALTA EL JARDÍN"], "ESTÁ AL REVÉS", "PRIMERO NACÍ.", n="error")],
"4": [MC("¿QUÉ ES UNA HUELLA DEL PASADO?", ["ALGO QUE CUENTA CÓMO ERA ANTES", "UNA MARCA DE ZAPATILLA", "UN DIBUJO NUEVO"], "ALGO QUE CUENTA CÓMO ERA ANTES", "COMO UNA FOTO VIEJA.", n="recordar"),
      MC("EN UNA FOTO HAY UNA CARRETA. ¿QUÉ NOS DICE?", ["ES DE HACE MUCHO", "ES DE HOY", "ES DE MAÑANA"], "ES DE HACE MUCHO", "ANTES SE VIAJABA EN CARRETA.", n="analizar")],
"5": [MC("RELÁMPAGO. ¿QUÉ VIENE DESPUÉS DE HOY?", ["MAÑANA", "AYER", "ANTES"], "MAÑANA", "MAÑANA.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿CUÁNTOS DÍAS TIENE LA SEMANA?", ["7", "siete", "SIETE"], "7.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL SÁBADO, ¿HAY ESCUELA?", ["NO", "SÍ", "A VECES"], "NO", "ES FIN DE SEMANA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. UNA FOTO VIEJA ES UNA…", ["HUELLA DEL PASADO", "COSA DEL FUTURO", "RECETA"], "HUELLA DEL PASADO", "NOS CUENTA EL PASADO.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("HOY ES…", ["AHORA", "LO QUE PASÓ", "LO QUE VIENE"], "AHORA", "HOY ES AHORA.", n="recordar")],
 [1, MC("TOMI DICE: AYER VOY A IR AL CINE. ¿QUÉ ESTÁ MAL?", ["TIENE QUE DECIR MAÑANA", "NADA", "TIENE QUE DECIR HOY"], "TIENE QUE DECIR MAÑANA", "AYER YA PASÓ.", n="error")],
 [1, ORD("ORDENÁ EL DÍA.", ["NOCHE", "MAÑANA", "TARDE"], ["MAÑANA", "TARDE", "NOCHE"], "MAÑANA, TARDE, NOCHE.", n="aplicar")],
 [2, SA("¿QUÉ DÍA VIENE DESPUÉS DEL LUNES?", acepta("MARTES", "EL MARTES"), "MARTES.", n="aplicar")],
 [2, MC("EL CALENDARIO MUESTRA…", ["DÍAS Y MESES", "ANIMALES", "COMIDAS"], "DÍAS Y MESES", "DÍAS Y MESES.", n="recordar")],
 [2, MC("¿QUÉ DÍAS NO HAY ESCUELA?", ["SÁBADO Y DOMINGO", "LUNES Y MARTES", "MIÉRCOLES"], "SÁBADO Y DOMINGO", "FIN DE SEMANA.", n="aplicar")],
 [3, MC("EN LA LÍNEA DE TIEMPO, LO DE AHORA VA…", ["AL FINAL", "AL PRINCIPIO", "EN NINGÚN LADO"], "AL FINAL", "A LA DERECHA.", n="recordar")],
 [3, ORD("ORDENÁ LA LÍNEA DE SOFI.", ["PRIMER GRADO", "NACÍ", "JARDÍN"], ["NACÍ", "JARDÍN", "PRIMER GRADO"], "DE ANTES A AHORA.", n="aplicar")],
 [3, MC("¿QUIÉN TE AYUDA A SABER CUÁNDO CAMINASTE?", ["MI FAMILIA", "UN DESCONOCIDO", "NADIE"], "MI FAMILIA", "ELLOS RECUERDAN.", n="analizar")],
 [4, MC("¿CUÁL ES UNA HUELLA DEL PASADO?", ["UNA FOTO VIEJA", "UN CELULAR NUEVO", "UNA TELE NUEVA"], "UNA FOTO VIEJA", "CUENTA CÓMO ERA ANTES.", n="aplicar")],
 [4, MC("UNA FOTO EN BLANCO Y NEGRO PROBABLEMENTE ES…", ["DE HACE MUCHO", "DE HOY", "DE MAÑANA"], "DE HACE MUCHO", "ANTES ERAN ASÍ.", n="analizar")],
 [4, MC("SOFI AGARRA LAS FOTOS VIEJAS SIN PERMISO. ¿QUÉ CONVIENE?", ["PEDIR PERMISO", "ESCONDERLAS", "RECORTARLAS"], "PEDIR PERMISO", "SON DE LA FAMILIA.", n="error")],
 [4, SA("¿CÓMO SE LLAMA ALGO QUE NOS CUENTA CÓMO ERA ANTES?", acepta("HUELLA DEL PASADO", "UNA HUELLA DEL PASADO", "HUELLA"), "HUELLA DEL PASADO.", n="recordar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: ordenar el tiempo", "examen_titulo": "Nivel jefe: ordenar el tiempo",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
