# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 1 · Mi familia y las familias de hoy. Genera mision-1.json.
Regla de primeros años. Metáfora: el álbum de las familias.
Niveles: 1 familias de distintos tipos · 2 quién hace qué en casa · 3 las viviendas y sus materiales · 4 mi historia familiar en un álbum."""
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
"objetivo": "Vas a conocer familias de distintos tipos.",
"vas_a_ver": ["Qué es una familia", "Familias distintas", "Todas valen"],
"secciones": [
 S(1, "La familia", [
  D("Familia", "Personas que se quieren, se cuidan y viven o comparten la vida."),
  P("Hay familias <b>grandes</b> y familias <b>chicas</b>."),
  IMG("Familias", "Grandes y chicas.", FG.tiras(["FAMILIA GRANDE", "FAMILIA CHICA"], numeros=False, cols=2)),
 ]),
 S(1, "Familias distintas", [
  P("Algunos viven con mamá y papá. Otros con la abuela, o con mamá sola."),
  IMG("Cada familia", "Distintas formas.", FG.tiras(["MAMÁ, PAPÁ Y HERMANOS", "MAMÁ Y ABUELA", "PAPÁ Y YO", "ABUELOS Y NIETOS"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Pensá en tu familia. La vas a usar en la carpeta."),
  IMG("Mi familia", "¿Quiénes son?", FG.tiras(["YO", "CON QUIÉN VIVO", "QUIÉN ME CUIDA"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La familia de Sofi", "planteo": "Sofi cuenta.", "pasos": ["Vive con su mamá.", "Y con su abuela.", "Es una familia de 3."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Una familia es…", "pasos": ["Personas que se ___ y se cuidan."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "Dibujá a tu familia y escribí sus nombres."},
"tip": {"titulo": "Todas valen", "texto": "Ninguna familia es mejor que otra."},
"ojo": ["No hay una sola forma de ser familia.", "Respetamos todas las familias."],
"resumen": [{"titulo": "Familia", "texto": "Se quieren y se cuidan."}, {"titulo": "Distintas", "texto": "Grandes y chicas."}, {"titulo": "Respeto", "texto": "Todas valen."}],
"glosario": [{"palabra": "Familia", "significado": "Personas que se quieren y se cuidan."}, {"palabra": "Respetar", "significado": "Tratar bien a todos."}],
"carpeta": ["¿Cuántas personas hay en la familia de Sofi?", "¿Con quién vive Sofi?", "Tomi dice que una familia siempre tiene mamá y papá. ¿Está bien?"],
"respuestas_carpeta": [["3", "tres", "TRES", "Tres"], acepta("MAMÁ Y ABUELA", "MAMA Y ABUELA", "CON SU MAMÁ Y SU ABUELA", "SU MAMÁ Y SU ABUELA"), acepta("NO", "NO, HAY MUCHAS FORMAS")],
"carpeta_nivel": ["aplicar", "recordar", "error"],
"soluciones": {"incompleto": "QUIEREN.", "solo": "Tu dibujo.", "carpeta": ["3.", "CON SU MAMÁ Y SU ABUELA.", "NO: HAY MUCHAS FORMAS DE FAMILIA."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver quién hace qué en casa.",
"vas_a_ver": ["Las tareas de la casa", "Todos ayudan", "Lo que puedo hacer yo"],
"secciones": [
 S(1, "Las tareas", [
  P("En casa hay que <b>cocinar</b>, <b>lavar</b>, <b>ordenar</b> y <b>hacer las compras</b>."),
  IMG("Tareas", "Hay muchas.", FG.tiras(["COCINAR", "LAVAR", "ORDENAR", "COMPRAR"], numeros=False, cols=2)),
 ]),
 S(1, "Todos ayudan", [
  D("Tarea", "Trabajo que hay que hacer."),
  P("Las tareas las pueden hacer <b>todos</b>: grandes y chicos."),
  IMG("Yo también", "Tareas para chicos.", FG.tiras(["PONER LA MESA", "GUARDAR JUGUETES", "REGAR PLANTAS"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tareas. Las vas a usar en la carpeta."),
  IMG("¿Quién lo hace?", "En la casa de Tomi.", FG.tiras(["PAPÁ: COCINA", "MAMÁ: LAVA", "TOMI: PONE LA MESA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La cena", "planteo": "En casa de Sofi.", "pasos": ["La abuela cocina.", "Mamá lava los platos.", "Sofi pone la mesa."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las tareas de la casa…", "pasos": ["Las pueden hacer ___."]},
"ejemplo_solo": {"titulo": "Tu ayuda", "planteo": "Elegí una tarea para ayudar en casa esta semana."},
"tip": {"titulo": "Entre todos", "texto": "Si todos ayudan, se termina más rápido."},
"ojo": ["Las tareas no son de una sola persona.", "Los chicos no usan el horno ni cuchillos."],
"resumen": [{"titulo": "Tareas", "texto": "Cocinar, lavar, ordenar."}, {"titulo": "Todos", "texto": "Grandes y chicos."}, {"titulo": "Yo", "texto": "Pongo la mesa."}],
"glosario": [{"palabra": "Tarea", "significado": "Trabajo que hay que hacer."}, {"palabra": "Compartir", "significado": "Hacer algo entre varios."}],
"carpeta": ["En casa de Tomi, ¿quién cocina?", "¿Qué hace Tomi?", "¿Qué tarea podés hacer vos?"],
"respuestas_carpeta": [acepta("PAPÁ", "PAPA", "EL PAPÁ", "SU PAPÁ"), acepta("PONE LA MESA", "PONER LA MESA"), acepta("PONER LA MESA", "GUARDAR JUGUETES", "REGAR", "REGAR PLANTAS", "ORDENAR", "TENDER LA CAMA")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "TODOS.", "solo": "Por ejemplo: guardar juguetes.", "carpeta": ["PAPÁ.", "PONE LA MESA.", "Por ejemplo: GUARDAR JUGUETES."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer las viviendas y sus materiales.",
"vas_a_ver": ["Tipos de vivienda", "Partes de la casa", "Materiales"],
"secciones": [
 S(1, "Tipos de vivienda", [
  D("Vivienda", "Lugar donde vive una familia."),
  P("Hay <b>casas</b>, <b>departamentos</b> y casas de <b>campo</b>."),
  IMG("Viviendas", "Distintas.", FG.tiras(["CASA", "DEPARTAMENTO", "CASA DE CAMPO"], numeros=False, cols=3)),
 ]),
 S(1, "Materiales", [
  P("Se hacen con <b>ladrillos</b>, <b>madera</b>, <b>chapa</b> o <b>adobe</b>."),
  IMG("Materiales", "Para construir.", FG.tiras(["LADRILLO", "MADERA", "CHAPA", "ADOBE: BARRO Y PAJA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las partes. Las vas a usar en la carpeta."),
  IMG("Partes de la casa", "¿De qué son?", FG.tiras(["TECHO: CHAPA", "PARED: LADRILLO", "PUERTA: MADERA"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La casa de Tomi", "planteo": "Tomi la mira.", "pasos": ["Las paredes son de ladrillo.", "El techo es de chapa.", "La puerta es de madera."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El adobe se hace con…", "pasos": ["Barro y ___."]},
"ejemplo_solo": {"titulo": "Tu casa", "planteo": "Dibujá tu vivienda. ¿De qué material es?"},
"tip": {"titulo": "Mirá y tocá", "texto": "Tocá la pared: ¿es dura y fría?"},
"ojo": ["Todas las viviendas sirven para protegernos.", "No hay viviendas mejores ni peores."],
"resumen": [{"titulo": "Vivienda", "texto": "Donde vivimos."}, {"titulo": "Tipos", "texto": "Casa, departamento."}, {"titulo": "Materiales", "texto": "Ladrillo, madera, chapa."}],
"glosario": [{"palabra": "Adobe", "significado": "Ladrillo de barro y paja."}, {"palabra": "Departamento", "significado": "Vivienda dentro de un edificio."}],
"carpeta": ["¿De qué es el techo?", "¿De qué es la pared?", "¿Para qué sirve una vivienda?"],
"respuestas_carpeta": [acepta("CHAPA", "DE CHAPA"), acepta("LADRILLO", "DE LADRILLO", "LADRILLOS"), acepta("PARA VIVIR", "VIVIR", "PROTEGERNOS", "PARA PROTEGERNOS", "CUIDARNOS")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "PAJA.", "solo": "Tu dibujo.", "carpeta": ["CHAPA.", "LADRILLO.", "PARA VIVIR Y PROTEGERNOS."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a armar un álbum de tu historia familiar.",
"vas_a_ver": ["Mi historia", "Buscar fotos", "Armar el álbum"],
"secciones": [
 S(1, "Mi historia", [
  P("Tu historia empieza cuando <b>naciste</b> y sigue hasta <b>hoy</b>."),
  IMG("Mi vida", "En orden.", FG.tiras(["NACÍ", "PRIMEROS PASOS", "JARDÍN", "PRIMER GRADO"], numeros=True, cols=2)),
 ]),
 S(1, "El álbum", [
  D("Álbum", "Libro con fotos o dibujos ordenados."),
  P("Buscás fotos, <b>preguntás</b> en casa, las <b>ordenás</b> y las <b>pegás</b>."),
  IMG("Pasos", "Para armarlo.", FG.tiras(["BUSCO FOTOS", "PREGUNTO", "ORDENO", "PEGO"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el álbum de Sofi. Lo vas a usar en la carpeta."),
  IMG("Álbum de Sofi", "¿Está en orden?", FG.tiras(["PRIMER GRADO", "NACÍ", "JARDÍN"], numeros=True, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi primera foto", "planteo": "Sofi pregunta.", "pasos": ["¿Cuándo nací?", "Mamá le muestra una foto.", "La pega primero."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Primero naciste, después…", "pasos": ["Primero NACÍ, después ___."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntá en casa: ¿cuál fue tu primera palabra?"},
"tip": {"titulo": "Preguntá a los grandes", "texto": "Ellos recuerdan cuando eras bebé."},
"ojo": ["Si no hay fotos, hacé dibujos.", "Las fotos se cuidan: pedí permiso."],
"resumen": [{"titulo": "Historia", "texto": "Desde que nací."}, {"titulo": "Preguntar", "texto": "A la familia."}, {"titulo": "Ordenar", "texto": "Antes y después."}],
"glosario": [{"palabra": "Álbum", "significado": "Libro de fotos."}, {"palabra": "Recuerdo", "significado": "Algo que guardamos en la memoria."}],
"carpeta": ["En el álbum de Sofi, ¿qué foto está mal ubicada?", "¿Qué va primero?", "¿Qué va al final?"],
"respuestas_carpeta": [acepta("PRIMER GRADO", "LA DE PRIMER GRADO"), acepta("NACÍ", "NACI", "CUANDO NACÍ"), acepta("PRIMER GRADO")],
"carpeta_nivel": ["error", "aplicar", "aplicar"],
"soluciones": {"incompleto": "PRIMEROS PASOS.", "solo": "Lo que te contaron.", "carpeta": ["PRIMER GRADO.", "NACÍ.", "PRIMER GRADO."]},
}

ACT = {
"1": [MC("¿QUÉ ES UNA FAMILIA?", ["PERSONAS QUE SE QUIEREN", "UN JUEGO DE MESA", "UN EDIFICIO ALTO"], "PERSONAS QUE SE QUIEREN", "SE QUIEREN Y SE CUIDAN.", n="recordar"),
      MC("LU VIVE CON SU PAPÁ Y SUS ABUELOS. ¿ES UNA FAMILIA?", ["SÍ", "NO", "SOLO SI HAY MAMÁ"], "SÍ", "HAY MUCHAS FORMAS DE FAMILIA.", n="analizar")],
"2": [MC("¿QUIÉN PUEDE HACER LAS TAREAS DE LA CASA?", ["TODOS", "SOLO MAMÁ", "SOLO PAPÁ"], "TODOS", "GRANDES Y CHICOS.", n="recordar"),
      MC("SOFI DICE QUE LAVAR ES SOLO DE MAMÁ. ¿ESTÁ BIEN?", ["NO: ES DE TODOS", "SÍ: SOLO MAMÁ", "SÍ: SOLO LOS GRANDES"], "NO: ES DE TODOS", "LAS TAREAS SE COMPARTEN.", n="error")],
"3": [MC("¿QUÉ ES UNA VIVIENDA?", ["DONDE VIVE UNA FAMILIA", "UN MEDIO DE TRANSPORTE", "UNA COMIDA RICA"], "DONDE VIVE UNA FAMILIA", "CASA O DEPARTAMENTO.", n="recordar"),
      SA("¿DE QUÉ MATERIAL ES LA PUERTA DE TOMI?", acepta("MADERA", "DE MADERA"), "MADERA.", n="aplicar")],
"4": [ORD("ORDENÁ LA HISTORIA.", ["JARDÍN", "NACÍ", "PRIMER GRADO"], ["NACÍ", "JARDÍN", "PRIMER GRADO"], "DE ANTES A AHORA.", n="aplicar"),
      MC("NO TENÉS FOTOS DE CUANDO ERAS BEBÉ. ¿QUÉ HACÉS?", ["UN DIBUJO", "NADA", "LLORO"], "UN DIBUJO", "SI NO HAY FOTOS, DIBUJÁS.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿HAY UNA SOLA FORMA DE FAMILIA?", ["NO", "SÍ", "A VECES"], "NO", "HAY MUCHAS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ TAREA PUEDE HACER UN CHICO?", ["PONER LA MESA", "USAR EL HORNO", "MANEJAR"], "PONER LA MESA", "PONER LA MESA.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. EL ADOBE SE HACE CON BARRO Y…", acepta("PAJA"), "PAJA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ VA PRIMERO EN TU HISTORIA?", ["NACÍ", "PRIMER GRADO", "JARDÍN"], "NACÍ", "NACÍ.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("UNA FAMILIA ES…", ["PERSONAS QUE SE CUIDAN", "UN LUGAR DE JUEGO", "UN EDIFICIO"], "PERSONAS QUE SE CUIDAN", "SE QUIEREN Y SE CUIDAN.", n="recordar")],
 [1, MC("TOMI VIVE CON SU MAMÁ Y SU ABUELA. SU FAMILIA ES…", ["UNA FAMILIA", "NO ES FAMILIA", "MEDIA FAMILIA"], "UNA FAMILIA", "TODAS LAS FAMILIAS VALEN.", n="aplicar")],
 [1, MC("¿QUÉ FAMILIA ES MEJOR?", ["NINGUNA: TODAS VALEN", "LA MÁS GRANDE", "LA MÁS CHICA"], "NINGUNA: TODAS VALEN", "LAS RESPETAMOS A TODAS.", n="analizar")],
 [2, MC("¿QUÉ ES UNA TAREA DE LA CASA?", ["ORDENAR", "JUGAR A LA PELOTA", "DORMIR LA SIESTA"], "ORDENAR", "HAY QUE HACERLA.", n="recordar")],
 [2, SA("NOMBRÁ UNA TAREA QUE PODÉS HACER EN CASA.", acepta("PONER LA MESA", "GUARDAR JUGUETES", "REGAR", "REGAR PLANTAS", "ORDENAR", "TENDER LA CAMA", "ORDENAR MI PIEZA"), "POR EJEMPLO: PONER LA MESA.", n="aplicar")],
 [2, MC("SI TODOS AYUDAN EN CASA…", ["SE TERMINA MÁS RÁPIDO", "TARDA MÁS", "NADIE COME"], "SE TERMINA MÁS RÁPIDO", "ENTRE TODOS ES MÁS FÁCIL.", n="analizar")],
 [3, MC("¿QUÉ ES UN DEPARTAMENTO?", ["UNA VIVIENDA EN UN EDIFICIO", "UNA ESCUELA CON PATIO", "UNA PLAZA DEL BARRIO"], "UNA VIVIENDA EN UN EDIFICIO", "ES UN TIPO DE VIVIENDA.", n="recordar")],
 [3, MC("¿CON QUÉ SE CONSTRUYEN LAS PAREDES?", ["LADRILLOS", "PAPEL", "TELA"], "LADRILLOS", "SON DUROS Y FUERTES.", n="aplicar")],
 [3, MC("SOFI DICE QUE LAS CASAS DE ADOBE NO SIRVEN. ¿ESTÁ BIEN?", ["NO: TAMBIÉN PROTEGEN", "SÍ: NO SIRVEN", "SÍ: SON FEAS"], "NO: TAMBIÉN PROTEGEN", "TODAS LAS VIVIENDAS NOS PROTEGEN.", n="error")],
 [4, ORD("ORDENÁ LOS PASOS DEL ÁLBUM.", ["PEGO", "BUSCO FOTOS", "ORDENO"], ["BUSCO FOTOS", "ORDENO", "PEGO"], "BUSCAR, ORDENAR Y PEGAR.", n="aplicar")],
 [4, MC("¿A QUIÉN LE PREGUNTÁS CÓMO ERAS DE BEBÉ?", ["A MI FAMILIA", "A UN DESCONOCIDO", "A NADIE"], "A MI FAMILIA", "ELLOS RECUERDAN.", n="aplicar")],
 [4, SA("¿QUÉ VA PRIMERO: JARDÍN O NACÍ?", acepta("NACÍ", "NACI"), "PRIMERO NACÍ.", n="aplicar")],
 [4, MC("UN ÁLBUM ES…", ["UN LIBRO DE FOTOS", "UN JUGUETE", "UNA COMIDA"], "UN LIBRO DE FOTOS", "FOTOS ORDENADAS.", n="recordar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: mi familia", "examen_titulo": "Nivel jefe: mi familia y las familias de hoy",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
