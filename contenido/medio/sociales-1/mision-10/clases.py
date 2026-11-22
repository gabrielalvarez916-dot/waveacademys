# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 10 · Fiestas y derechos de niñas y niños: las 4 clases animadas.
VARIANTE: el nivel 1 (fechas patrias argentinas) lleva su parte "neutro"; los niveles 2 a 4 son iguales para todos ("sin_variante"). Metáfora: la gran fiesta del grado. Regla de primeros años y variedad del banco.
Usa "destino" (la máquina busca sola el paso de video de cada nivel).
Genera tools/medio/clase/lecciones/medio-soc1-m10-n<N>.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
SUBJECT = '67d2ad89-caaa-4e82-8d25-8bbb08147818'
TEMA = 10
TIT = {1: 'Las fechas patrias que celebramos', 2: 'Fiestas y costumbres de mi familia', 3: 'Los derechos de niñas y niños', 4: 'Mi álbum de lo que aprendí'}
FIN = {'titulo': '¡CLASE TERMINADA!', 'sub': 'Ahora, a practicar 🚀'}
CIERRE = "¡Muy bien! Ahora, *a practicar*."
SOFI = {"nombre": "Sofi", "emoji": "👧"}
TOMI = {"nombre": "Tomi", "emoji": "👦"}


N1 = [
 {"t": "chat", "contacto": TOMI, "mensajes": [{"yo": False, "txt": "¡Mañana hay acto en la escuela!"}, {"yo": True, "txt": "¡YO LLEVO LA BANDERA!"}, {"yo": False, "txt": "¡Qué lindo!"}], "titulo": "FECHAS PATRIAS", "sub": "las celebramos",
  "voz": ["Tomi le escribe a Sofi.", "¡Mañana hay *acto* en la escuela!", "Sofi lleva la *bandera*.", "Hoy: *las fechas patrias*."]},
 {"t": "matriz", "titulo": "NUESTRAS FECHAS", "celdas": [{"cab": "25 DE MAYO", "txt": "REVOLUCIÓN"}, {"cab": "20 DE JUNIO", "txt": "BANDERA"}, {"cab": "9 DE JULIO", "txt": "INDEPENDENCIA"}, {"cab": "🇦🇷", "txt": "ACTOS EN LA ESCUELA"}],
  "voz": ["En Argentina recordamos fechas *importantes*.", "El 25 de Mayo, la *Revolución*.", "El 20 de junio, el día de la *Bandera*.", "El 9 de Julio, la *Independencia*.", "¡Y hacemos *actos* en la escuela!"],
  "neutro": {"titulo": "FECHAS DEL PAÍS", "celdas": [{"cab": "🚩", "txt": "DÍA DE LA BANDERA"}, {"cab": "🗽", "txt": "INDEPENDENCIA"}, {"cab": "🎉", "txt": "FIESTA NACIONAL"}, {"cab": "🏫", "txt": "ACTOS EN LA ESCUELA"}],
   "voz": ["Cada país recuerda fechas *importantes*.", "Hay un día de la *bandera*.", "Hay un día de la *independencia*.", "Hay *fiestas nacionales*.", "¡Y hacemos *actos* en la escuela!"]}},
 {"t": "partes", "emoji": "🏫", "titulo": "EL ACTO", "partes": [{"txt": "BANDERA", "x": 0.0, "y": -0.8}, {"txt": "ABANDERADOS", "x": -0.6, "y": -0.2}, {"txt": "HIMNO", "x": 0.6, "y": -0.2}, {"txt": "BAILE", "x": 0.0, "y": 0.7}],
  "voz": ["Miramos un *acto* escolar.", "Sube la *bandera*.", "Pasan los *abanderados*.", "Cantamos el *himno*.", "¡Y hay un *baile*!"]},
 {"t": "pregunta", "pregunta": "¿Qué cantamos en el acto?", "opciones": ["EL HIMNO", "FELIZ CUMPLE", "UNA CANCIÓN DE CUNA"], "correcta": 0,
  "voz": ["Ahora vos. Pensá en el acto.", "¿Qué cantamos todos?", "¡El *himno*!"]},
 {"t": "consejo", "titulo": "RESPETO", "texto": "En el himno, quietos y en silencio", "emoji": "🤫",
  "voz": ["Recordá: en el himno, *quietos* y en silencio."]},
 {"t": "resumen", "items": [["FECHA PATRIA", "recuerda algo del país"], ["ACTO", "bandera e himno"], ["RESPETO", "silencio en el himno"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las *fechas patrias* recuerdan al país.", "En el *acto* hay bandera e himno.", "Y escuchamos con *respeto*.", CIERRE]},
]
N2 = [
 {"t": "historia", "personaje": SOFI, "lugar": "🎂", "lineas": ["Hoy es el cumple de Sofi.", "Viene toda la familia.", "¡La abuela trae empanadas!"], "titulo": "FIESTAS", "sub": "de mi familia",
  "voz": ["Hoy es el *cumple* de Sofi.", "Viene toda la familia.", "¡La abuela trae *empanadas*!", "Hoy: *fiestas y costumbres de mi familia*."]},
 {"t": "venn", "a": "FAMILIA DE SOFI", "b": "FAMILIA DE TOMI", "itemsA": ["EMPANADAS", "BAILAR"], "itemsB": ["PIZZA", "JUEGOS"], "ambos": ["TORTA", "CANCIÓN DE CUMPLE"],
  "voz": ["Comparamos dos familias.", "La de Sofi come *empanadas* y baila.", "La de Tomi come *pizza* y juega.", "¡Las dos tienen *torta* y canción!"]},
 {"t": "dialogo", "personas": [{"nombre": "SOFI", "emoji": "👧"}, {"nombre": "ABUELA", "emoji": "👵"}], "lineas": [{"quien": 0, "txt": "¿POR QUÉ HACÉS EMPANADAS?"}, {"quien": 1, "txt": "MI MAMÁ LAS HACÍA."}, {"quien": 1, "txt": "¡ES UNA COSTUMBRE!"}],
  "voz": ["Sofi pregunta: ¿por qué hacés empanadas?", "La abuela dice: mi mamá las hacía.", "¡Es una *costumbre* de la familia!"]},
 {"t": "pregunta", "pregunta": "¿Todas las familias festejan igual?", "opciones": ["SÍ", "NO", "NUNCA FESTEJAN"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en las familias.", "¿Todas festejan igual?", "¡*No*! Cada una a su manera."]},
 {"t": "consejo", "titulo": "RESPETO", "texto": "Respetamos las costumbres de los demás", "emoji": "🤝",
  "voz": ["Recordá: *respetamos* las costumbres de todos."]},
 {"t": "resumen", "items": [["FIESTAS", "cumpleaños, fin de año"], ["COSTUMBRES", "comidas, canciones"], ["RESPETO", "cada una es distinta"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Las familias tienen *fiestas*.", "Y tienen *costumbres*.", "Cada una es distinta y la *respetamos*.", CIERRE]},
]
N3 = [
 {"t": "reto", "texto": "¿Jugar es un derecho o un premio?", "segundos": 6, "respuesta": "¡UN DERECHO!", "emoji": "⚽", "titulo": "MIS DERECHOS", "sub": "niñas y niños",
  "voz": ["Desafío: ¿jugar es un derecho o un premio?", "¡Es un *derecho*!", "Hoy: *los derechos de niñas y niños*."]},
 {"t": "bloques", "titulo": "TENEMOS DERECHO A…", "items": [{"cab": "⚽", "txt": "JUGAR"}, {"cab": "🏫", "txt": "IR A LA ESCUELA"}, {"cab": "🏥", "txt": "LA SALUD"}, {"cab": "🪪", "txt": "UN NOMBRE"}, {"cab": "👂", "txt": "SER ESCUCHADOS"}],
  "voz": ["Todos los chicos tienen *derechos*.", "Derecho a *jugar*.", "A ir a la *escuela*.", "A la *salud*.", "A tener un *nombre*.", "Y a ser *escuchados*."]},
 {"t": "corrige", "titulo": "¿ESTÁ BIEN?", "cambios": [{"antes": "SOLO ALGUNOS TIENEN DERECHOS", "despues": "TODOS TIENEN DERECHOS", "motivo": "son de todos"}, {"antes": "TENER CELULAR ES UN DERECHO", "despues": "TENER CELULAR ES UN DESEO", "motivo": "no es un derecho"}],
  "voz": ["Arreglamos frases que están mal.", "*Todos* los chicos tienen derechos.", "Un celular es un *deseo*, no un derecho."]},
 {"t": "pregunta", "pregunta": "¿Cuál es un derecho?", "opciones": ["TENER CELULAR", "IR A LA ESCUELA", "COMER CARAMELOS"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en los derechos.", "¿Cuál es un derecho?", "¡*Ir a la escuela*!"]},
 {"t": "consejo", "titulo": "LOS GRANDES CUIDAN", "texto": "Los adultos cuidan nuestros derechos", "emoji": "🛡️",
  "voz": ["Recordá: los *adultos* cuidan nuestros derechos."]},
 {"t": "resumen", "items": [["DERECHO", "lo que todos deben tener"], ["EJEMPLOS", "jugar, escuela, salud"], ["TODOS", "los mismos derechos"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "Un *derecho* es para todos.", "Jugar, *escuela* y salud.", "*Todos* tenemos los mismos.", CIERRE]},
]
N4 = [
 {"t": "noticia", "cinta": "ÚLTIMO MOMENTO", "titular": "¡TERMINA EL AÑO!", "bajada": "Sofi arma su álbum", "emoji": "📒", "titulo": "MI ÁLBUM", "sub": "de lo que aprendí",
  "voz": ["¡Último momento! Termina el *año*.", "Sofi arma su *álbum*.", "Hoy: *mi álbum de lo que aprendí*."]},
 {"t": "flujo", "titulo": "CÓMO LO ARMO", "items": ["ELIJO", "DIBUJO", "ESCRIBO", "MUESTRO"],
  "voz": ["Primero, *elijo* lo que más me gustó.", "Después, lo *dibujo*.", "*Escribo* un título.", "Y lo *muestro* a mi familia."]},
 {"t": "comparar", "a": {"cab": "AL EMPEZAR", "texto": "No sabía leer", "emoji": "🌱"}, "b": {"cab": "AHORA", "texto": "¡Leo y escribo!", "emoji": "🌳"}, "signo": "vs",
  "voz": ["Al *empezar* el año, no sabía leer.", "*Ahora* leo y escribo.", "¡Aprendí un *montón*!"]},
 {"t": "pregunta", "pregunta": "¿Qué va en un álbum?", "opciones": ["PIEDRAS", "DIBUJOS Y FOTOS", "COMIDA"], "correcta": 1,
  "voz": ["Ahora vos. Pensá en tu álbum.", "¿Qué va adentro?", "¡*Dibujos y fotos*!"]},
 {"t": "consejo", "titulo": "LO QUE MÁS TE GUSTÓ", "texto": "Elegí lo que más te gustó aprender", "emoji": "💛",
  "voz": ["Truco: elegí lo que *más te gustó*."]},
 {"t": "resumen", "items": [["RECORDAR", "lo que aprendí"], ["ARMAR", "dibujar y escribir"], ["MOSTRAR", "a la familia"]], "fin": FIN,
  "voz": ["Repasemos lo que aprendimos.", "*Recordamos* lo que aprendimos.", "*Armamos* el álbum.", "Y lo *mostramos* con orgullo.", CIERRE]},
]
for n, E in ((1, N1), (2, N2), (3, N3), (4, N4)):
    slug = f'medio-soc1-m{TEMA}-n{n}'
    L = {"slug": slug, "destino": {"subject_id": SUBJECT, "tema": TEMA, "nivel": n}, "materia": "Ciencias Sociales 1", "titulo": TIT[n], "sub": f"Ciencias Sociales 1 · Misión {TEMA} · Nivel {n}", "estilo": "primeros", "escenas": E}
    if n == 1: L["meses_ok"] = True
    else: L["sin_variante"] = True
    json.dump(L, open(os.path.join(RAIZ, 'tools', 'medio', 'clase', 'lecciones', slug + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, len(E), 'escenas')
