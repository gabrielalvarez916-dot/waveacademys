# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 10 · Fiestas y derechos de niñas y niños. Genera mision-10.json.
VARIANTE: lo que nombra las fechas patrias argentinas lleva su parte "neutro" para alumnos de otros países. Regla de primeros años. Metáfora: la gran fiesta del grado.
Niveles: 1 las fechas patrias que celebramos · 2 fiestas y costumbres de mi familia · 3 los derechos de niñas y niños · 4 mi álbum de lo que aprendí."""
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
P2 = lambda x, **k: {"tipo": "parrafo", "texto": x, **k}
NEU = lambda p: {"neutro": {"p": p}}

N1 = {**ESTILO, "meses_ok": True,
"objetivo": "Vas a conocer las fechas patrias que celebramos.",
"vas_a_ver": ["Qué es una fecha patria", "Las fechas de nuestro país", "El acto escolar"],
"secciones": [
 S(1, "Las fechas patrias", [
  D("Fecha patria", "Día en que recordamos algo importante de nuestro país."),
  P2("En esas fechas hacemos <b>actos</b> en la escuela."),
  IMG("Un acto", "Lo que hacemos.", FG.tiras(["IZAMOS LA BANDERA", "CANTAMOS EL HIMNO", "BAILAMOS"], numeros=False, cols=3)),
 ]),
 S(1, "Nuestras fechas", [
  P2("En Argentina recordamos <b>tres</b> fechas muy importantes.", neutro={"texto": "Cada país tiene sus <b>fechas</b> importantes."}),
  P2("<b>25 de Mayo</b>, <b>20 de junio</b> y <b>9 de Julio</b>.", neutro={"texto": "Por ejemplo, el día de la <b>bandera</b> y de la <b>independencia</b>."}),
  IMG("Recordamos", "Días del país.", FG.tiras(["LA BANDERA", "LA INDEPENDENCIA", "LA PATRIA"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P2("Mirá el acto. Lo vas a usar en la carpeta."),
  IMG("En el acto", "¿Qué hacemos?", FG.tiras(["LA BANDERA SUBE", "EL HIMNO SUENA", "LOS CHICOS BAILAN"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El acto", "planteo": "Sofi va al acto.", "pasos": ["Se para derecha.", "Canta el himno.", "Aplaude el baile."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el acto cantamos el…", "pasos": ["El ___."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntá en casa qué fecha patria les gusta más."},
"tip": {"titulo": "Respeto", "texto": "Durante el himno nos quedamos quietos y en silencio."},
"ojo": ["La bandera se cuida: no se tira al piso.", "Cada país tiene sus propias fechas."],
"resumen": [{"titulo": "Fecha patria", "texto": "Recuerda algo del país."}, {"titulo": "Acto", "texto": "Bandera e himno."}, {"titulo": "Respeto", "texto": "Silencio en el himno."}],
"glosario": [{"palabra": "Himno", "significado": "Canción del país."}, {"palabra": "Independencia", "significado": "Cuando un país se hace libre."}],
"carpeta": ["¿Qué cantamos en el acto?", "¿Qué sube en el acto?", "¿Qué hacemos durante el himno?"],
"respuestas_carpeta": [acepta("EL HIMNO", "HIMNO"), acepta("LA BANDERA", "BANDERA"), acepta("SILENCIO", "NOS QUEDAMOS QUIETOS", "ESCUCHAMOS", "CANTAMOS", "LO CANTAMOS")],
"carpeta_nivel": ["recordar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "HIMNO.", "solo": "Lo que te contaron.", "carpeta": ["EL HIMNO.", "LA BANDERA.", "NOS QUEDAMOS QUIETOS."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer las fiestas y costumbres de las familias.",
"vas_a_ver": ["Fiestas en familia", "Costumbres", "Cada familia es distinta"],
"secciones": [
 S(1, "Fiestas en familia", [
  D("Costumbre", "Algo que una familia hace siempre igual."),
  P2("Las familias festejan <b>cumpleaños</b>, <b>fin de año</b> y otras fiestas."),
  IMG("Fiestas", "En familia.", FG.tiras(["CUMPLEAÑOS", "FIN DE AÑO", "FIESTA DEL BARRIO"], numeros=False, cols=3)),
 ]),
 S(1, "Cada familia es distinta", [
  P2("Cada familia tiene sus <b>comidas</b>, <b>canciones</b> y <b>juegos</b>."),
  IMG("Costumbres", "Distintas.", FG.tiras(["COMIDA DE LA ABUELA", "CANCIÓN DE CUMPLE", "JUEGO EN FAMILIA"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P2("Mirá lo que contó Tomi. Lo vas a usar en la carpeta."),
  IMG("La familia de Tomi", "Su costumbre.", FG.tiras(["EN SU CUMPLE COMEN TORTA", "CANTAN UNA CANCIÓN", "LA ABUELA HACE EMPANADAS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El cumple de Sofi", "planteo": "Sofi cumple 7.", "pasos": ["Viene la familia.", "Comen torta.", "Le cantan el feliz cumpleaños."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Algo que una familia hace siempre igual es una…", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "Dibujá una fiesta de tu familia."},
"tip": {"titulo": "Contá", "texto": "Contale al grado una costumbre de tu casa."},
"ojo": ["Cada familia festeja a su manera.", "Respetamos las costumbres de los demás."],
"resumen": [{"titulo": "Fiestas", "texto": "Cumpleaños, fin de año."}, {"titulo": "Costumbres", "texto": "Comidas, canciones."}, {"titulo": "Respeto", "texto": "Cada una es distinta."}],
"glosario": [{"palabra": "Costumbre", "significado": "Algo que se hace siempre igual."}, {"palabra": "Festejar", "significado": "Celebrar con alegría."}],
"carpeta": ["¿Qué comen en el cumple de Tomi?", "¿Qué hace la abuela?", "¿Todas las familias festejan igual?"],
"respuestas_carpeta": [acepta("TORTA", "UNA TORTA"), acepta("EMPANADAS", "HACE EMPANADAS"), acepta("NO")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "COSTUMBRE.", "solo": "Tu dibujo.", "carpeta": ["TORTA.", "EMPANADAS.", "NO."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer los derechos de niñas y niños.",
"vas_a_ver": ["Qué es un derecho", "Nuestros derechos", "Quién nos cuida"],
"secciones": [
 S(1, "Los derechos", [
  D("Derecho", "Algo que todos los chicos tienen que tener."),
  P2("Todos los chicos tienen <b>los mismos</b> derechos."),
  IMG("Derechos", "Para todos.", FG.tiras(["A JUGAR", "A IR A LA ESCUELA", "A LA SALUD", "A TENER UN NOMBRE"], numeros=False, cols=2)),
 ]),
 S(1, "Ser escuchados", [
  P2("También tenemos derecho a <b>opinar</b> y a ser <b>escuchados</b>."),
  IMG("Más derechos", "También.", FG.tiras(["A SER ESCUCHADOS", "A UNA FAMILIA", "A SER CUIDADOS"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P2("Mirá las frases. Las vas a usar en la carpeta."),
  IMG("¿Es un derecho?", "Pensá.", FG.tiras(["JUGAR", "IR A LA ESCUELA", "TENER UN CELULAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El derecho a jugar", "planteo": "Tomi juega en la plaza.", "pasos": ["Juega con amigos.", "Se divierte.", "Es su derecho."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Todos los chicos tienen derecho a ir a la…", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu derecho", "planteo": "Dibujá tu derecho preferido."},
"tip": {"titulo": "Los grandes cuidan", "texto": "Los adultos tienen que cuidar nuestros derechos."},
"ojo": ["Los derechos son de todos los chicos.", "Un deseo no es lo mismo que un derecho."],
"resumen": [{"titulo": "Derecho", "texto": "Lo que todos deben tener."}, {"titulo": "Ejemplos", "texto": "Jugar, escuela, salud."}, {"titulo": "Todos", "texto": "Los mismos derechos."}],
"glosario": [{"palabra": "Derecho", "significado": "Lo que todos los chicos deben tener."}, {"palabra": "Opinar", "significado": "Decir lo que pensamos."}],
"carpeta": ["Jugar, ¿es un derecho?", "Ir a la escuela, ¿es un derecho?", "Tener un celular, ¿es un derecho?"],
"respuestas_carpeta": [acepta("SÍ", "SI"), acepta("SÍ", "SI"), acepta("NO", "NO, ES UN DESEO")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "ESCUELA.", "solo": "Tu dibujo.", "carpeta": ["SÍ.", "SÍ.", "NO: ES UN DESEO."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a armar un álbum de lo que aprendiste.",
"vas_a_ver": ["Recordar", "Elegir", "Mostrar"],
"secciones": [
 S(1, "Lo que aprendí", [
  P2("Este año conociste tu <b>familia</b>, tu <b>escuela</b> y tu <b>barrio</b>."),
  IMG("Mi año", "Lo que vimos.", FG.tiras(["FAMILIA", "ESCUELA", "BARRIO", "EL CAMPO Y LA CIUDAD"], numeros=False, cols=2)),
 ]),
 S(1, "Armar el álbum", [
  D("Álbum", "Libro con dibujos y fotos de lo que vivimos."),
  P2("Elegís, <b>dibujás</b>, <b>escribís</b> y lo <b>mostrás</b>."),
  IMG("Pasos", "En orden.", FG.tiras(["ELIJO", "DIBUJO", "ESCRIBO", "MUESTRO"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P2("Mirá el álbum de Sofi. Lo vas a usar en la carpeta."),
  IMG("Álbum de Sofi", "Sus páginas.", FG.tiras(["MI FAMILIA", "MI BARRIO", "MIS DERECHOS"], numeros=True, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Una página", "planteo": "Sofi arma su página.", "pasos": ["Elige: su barrio.", "Dibuja la plaza.", "Escribe: MI BARRIO."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El último paso es…", "pasos": ["___ el álbum."]},
"ejemplo_solo": {"titulo": "Tu álbum", "planteo": "Hacé una página de tu álbum sobre tu familia."},
"tip": {"titulo": "Lo que más te gustó", "texto": "Elegí lo que más te gustó aprender."},
"ojo": ["Escribí poco y dibujá mucho.", "Mostralo con orgullo."],
"resumen": [{"titulo": "Recordar", "texto": "Lo que aprendí."}, {"titulo": "Armar", "texto": "Dibujar y escribir."}, {"titulo": "Mostrar", "texto": "A la familia."}],
"glosario": [{"palabra": "Álbum", "significado": "Libro de recuerdos."}, {"palabra": "Página", "significado": "Cada hoja del álbum."}],
"carpeta": ["¿Cuál es la primera página del álbum de Sofi?", "¿Cuántas páginas tiene?", "¿Qué va en la página 3?"],
"respuestas_carpeta": [acepta("MI FAMILIA", "FAMILIA"), ["3", "tres", "TRES", "Tres"], acepta("MIS DERECHOS", "DERECHOS")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "MOSTRAR.", "solo": "Tu página.", "carpeta": ["MI FAMILIA.", "3.", "MIS DERECHOS."]},
}

ACT = {
"1": [MC("¿QUÉ RECUERDA UNA FECHA PATRIA?", ["ALGO IMPORTANTE DEL PAÍS", "UN CUMPLEAÑOS", "UN PARTIDO DE FÚTBOL"], "ALGO IMPORTANTE DEL PAÍS", "RECORDAMOS AL PAÍS.", n="recordar"),
      MC("¿QUÉ SE RECUERDA EL 9 DE JULIO?", ["EL PAÍS SE HIZO LIBRE", "EMPIEZA LA PRIMAVERA", "ES NAVIDAD"], "EL PAÍS SE HIZO LIBRE", "LA INDEPENDENCIA.", n="aplicar", **NEU("¿QUÉ SE RECUERDA EL DÍA DE LA INDEPENDENCIA?"))],
"2": [MC("¿QUÉ ES UNA COSTUMBRE?", ["ALGO QUE SE HACE SIEMPRE IGUAL", "UN JUGUETE NUEVO", "UNA PALABRA DIFÍCIL"], "ALGO QUE SE HACE SIEMPRE IGUAL", "COMO LA TORTA DEL CUMPLE.", n="recordar"),
      MC("TOMI SE RÍE DE LA COMIDA DE LA FAMILIA DE SOFI. ¿QUÉ CONVIENE?", ["RESPETAR SU COSTUMBRE", "REÍRSE MÁS", "NO HABLARLE"], "RESPETAR SU COSTUMBRE", "CADA FAMILIA ES DISTINTA.", n="error")],
"3": [MC("¿CUÁL ES UN DERECHO DE LOS CHICOS?", ["JUGAR", "TENER CELULAR", "COMER CARAMELOS"], "JUGAR", "TODOS TIENEN DERECHO A JUGAR.", n="aplicar"),
      MC("UN CHICO NO PUEDE IR A LA ESCUELA. ¿QUÉ PASA?", ["NO SE CUMPLE SU DERECHO", "ESTÁ BIEN", "ES SU DESEO"], "NO SE CUMPLE SU DERECHO", "TIENE DERECHO A IR.", n="analizar")],
"4": [ORD("ORDENÁ LOS PASOS DEL ÁLBUM.", ["MUESTRO", "ELIJO", "DIBUJO"], ["ELIJO", "DIBUJO", "MUESTRO"], "ELEGIR, DIBUJAR, MOSTRAR.", n="aplicar"),
      SA("NOMBRÁ ALGO QUE APRENDISTE ESTE AÑO EN SOCIALES.", acepta("FAMILIA", "LA FAMILIA", "ESCUELA", "LA ESCUELA", "BARRIO", "EL BARRIO", "DERECHOS", "LOS DERECHOS", "CAMPO", "CIUDAD", "SERVICIOS"), "POR EJEMPLO: MI BARRIO.", n="aplicar")],
"5": [MC("RELÁMPAGO. EN EL ACTO CANTAMOS EL…", ["HIMNO", "FELIZ CUMPLE", "ARRORRÓ"], "HIMNO", "EL HIMNO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿TODAS LAS FAMILIAS FESTEJAN IGUAL?", ["NO", "SÍ", "NUNCA FESTEJAN"], "NO", "CADA UNA A SU MANERA.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. JUGAR ES UN…", acepta("DERECHO", "UN DERECHO"), "DERECHO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ VA EN UN ÁLBUM?", ["DIBUJOS Y FOTOS", "PIEDRAS", "COMIDA"], "DIBUJOS Y FOTOS", "RECUERDOS.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("UNA FECHA PATRIA ES…", ["UN DÍA IMPORTANTE DEL PAÍS", "UN DÍA DE LLUVIA", "UN CUMPLEAÑOS"], "UN DÍA IMPORTANTE DEL PAÍS", "LO RECORDAMOS.", n="recordar")],
 [1, MC("EL 20 DE JUNIO RECORDAMOS A LA…", ["BANDERA", "PRIMAVERA", "LUNA"], "BANDERA", "DÍA DE LA BANDERA.", n="recordar", **NEU("EN EL DÍA DE LA BANDERA HONRAMOS A LA…"))],
 [1, MC("SOFI HABLA FUERTE DURANTE EL HIMNO. ¿QUÉ CONVIENE?", ["QUEDARSE EN SILENCIO", "GRITAR MÁS", "IRSE"], "QUEDARSE EN SILENCIO", "ES UN MOMENTO DE RESPETO.", n="error")],
 [2, MC("¿QUÉ FIESTA SE HACE EN FAMILIA?", ["CUMPLEAÑOS", "EXAMEN", "RECREO"], "CUMPLEAÑOS", "SE FESTEJA EN FAMILIA.", n="aplicar")],
 [2, SA("ALGO QUE UNA FAMILIA HACE SIEMPRE IGUAL ES UNA…", acepta("COSTUMBRE", "UNA COSTUMBRE"), "COSTUMBRE.", n="recordar")],
 [2, MC("¿POR QUÉ LAS FAMILIAS FESTEJAN DISTINTO?", ["CADA UNA TIENE SUS COSTUMBRES", "UNAS SON MEJORES", "NO SABEN FESTEJAR"], "CADA UNA TIENE SUS COSTUMBRES", "Y LAS RESPETAMOS.", n="analizar")],
 [3, MC("UN DERECHO ES…", ["ALGO QUE TODOS DEBEN TENER", "UN JUGUETE CARO", "UN PREMIO"], "ALGO QUE TODOS DEBEN TENER", "LOS MISMOS PARA TODOS.", n="recordar")],
 [3, MC("TENER UN CELULAR, ¿ES UN DERECHO?", ["NO: ES UN DESEO", "SÍ: ES UN DERECHO", "SÍ: PARA TODOS"], "NO: ES UN DESEO", "UN DESEO NO ES UN DERECHO.", n="analizar")],
 [3, MC("TOMI DICE QUE SOLO ALGUNOS CHICOS TIENEN DERECHOS. ¿ESTÁ BIEN?", ["NO: TODOS LOS TIENEN", "SÍ: SOLO ALGUNOS", "SÍ: LOS GRANDES"], "NO: TODOS LOS TIENEN", "TODOS LOS MISMOS.", n="error")],
 [3, SA("¿QUIÉNES TIENEN QUE CUIDAR LOS DERECHOS DE LOS CHICOS?", acepta("LOS ADULTOS", "ADULTOS", "LOS GRANDES", "LA FAMILIA", "TODOS"), "LOS ADULTOS.", n="aplicar")],
 [4, ORD("ORDENÁ LOS PASOS DEL ÁLBUM.", ["ESCRIBO", "MUESTRO", "ELIJO", "DIBUJO"], ["ELIJO", "DIBUJO", "ESCRIBO", "MUESTRO"], "ELIJO, DIBUJO, ESCRIBO, MUESTRO.", n="aplicar")],
 [4, MC("UN ÁLBUM ES UN LIBRO DE…", ["RECUERDOS", "CUENTAS", "RECETAS"], "RECUERDOS", "CON DIBUJOS Y FOTOS.", n="recordar")],
 [4, MC("¿A QUIÉN LE MOSTRÁS TU ÁLBUM?", ["A MI FAMILIA", "A NADIE NUNCA", "LO TIRO"], "A MI FAMILIA", "LO MOSTRAMOS CON ORGULLO.", n="aplicar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 10, "estilo": "primeros",
     "practica": "Práctica general: fiestas y derechos", "examen_titulo": "Nivel jefe: fiestas y derechos de niñas y niños",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
