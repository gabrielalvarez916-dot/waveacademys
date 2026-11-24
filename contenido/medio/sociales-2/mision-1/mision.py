# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 1 · De la materia prima al producto. Genera mision-1.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy visita una fábrica).
Niveles: 1 del tomate a la salsa · 2 de la leche al queso y al helado · 3 las etapas de una producción · 4 quiénes trabajan en una fábrica."""
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
"objetivo": "Vas a ver cómo un tomate se hace salsa.",
"vas_a_ver": ["Materia prima", "Producto", "Del tomate a la salsa"],
"secciones": [
 S(1, "Materia prima y producto", [
  D("Materia prima", "Lo que sale de la <b>naturaleza</b>, como el tomate."),
  D("Producto", "Lo que se <b>hace</b> con la materia prima, como la salsa."),
  IMG("Del campo al frasco", "Materia prima y producto.", FG.tiras(["MATERIA PRIMA: TOMATE", "PRODUCTO: SALSA"], numeros=False, cols=1)),
 ]),
 S(1, "Cómo se hace la salsa", [
  P("Lola visita una fábrica de salsa. ¡Mirá los pasos!"),
  P("Los tomates llegan en cajones desde la huerta. Una máquina los lava con agua. Después se cocinan en ollas gigantes."),
  IMG("Los pasos", "Del tomate a la salsa.", FG.tiras(["1. COSECHAN LOS TOMATES", "2. LOS LAVAN", "3. LOS COCINAN", "4. LOS ENVASAN"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Qué es cada uno?", "Pensá: ¿naturaleza o fábrica?", FG.tiras(["1. UN TOMATE DE LA HUERTA", "2. UN FRASCO DE SALSA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La salsa", "planteo": "¿De dónde sale la salsa?", "pasos": ["Del tomate, que es la materia prima.", "En la fábrica lo cocinan.", "Lo envasan: ¡ya es producto!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El tomate es la materia…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "En tu cocina", "planteo": "Buscá un frasco o paquete. ¿De qué materia prima está hecho?"},
"tip": {"titulo": "¿Naturaleza o fábrica?", "texto": "Si sale de la naturaleza, es materia prima."},
"ojo": ["Un producto puede tener varias materias primas.", "Muchas personas trabajan para hacer un producto."],
"resumen": [{"titulo": "Materia prima", "texto": "De la naturaleza."}, {"titulo": "Producto", "texto": "Hecho en la fábrica."}, {"titulo": "Salsa", "texto": "Viene del tomate."}],
"glosario": [{"palabra": "Frasco", "significado": "Envase de vidrio con tapa."}, {"palabra": "Envasar", "significado": "Poner en frascos o paquetes."}],
"carpeta": ["¿La tarjeta 1 es materia prima o producto?", "¿Y la tarjeta 2?", "Lola dice que la salsa sale sola de la planta. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MATERIA PRIMA") + low("ES MATERIA PRIMA"), low("PRODUCTO") + low("ES UN PRODUCTO") + low("UN PRODUCTO"), NO],
"soluciones": {"incompleto": "PRIMA.", "solo": "La materia prima del producto.", "carpeta": ["Materia prima.", "Producto.", "No: la hacen en una fábrica."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver qué se hace con la leche.",
"vas_a_ver": ["El tambo", "La leche", "Queso, yogur y helado"],
"secciones": [
 S(1, "El tambo", [
  D("Tambo", "Lugar en el campo donde se <b>ordeñan</b> las vacas."),
  P("La leche viaja en camión a la <b>fábrica</b>, bien fría."),
  IMG("Del tambo a la fábrica", "El viaje de la leche.", FG.tiras(["1. ORDEÑAN LA VACA", "2. LA LECHE SE ENFRÍA", "3. VIAJA EN CAMIÓN", "4. LLEGA A LA FÁBRICA"], numeros=False)),
 ]),
 S(1, "Muchos productos", [
  P("Con una sola materia prima, la <b>leche</b>, se hacen muchos productos."),
  P("Para el queso, la leche se cuaja y se aprieta. Para el helado, se mezcla con azúcar y se congela."),
  IMG("Productos de la leche", "Todos vienen de la vaca.", FG.nombres(["QUESO", "YOGUR", "HELADO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("¿Viene de la leche?", "Pensá en cada uno.", FG.nombres(["MANTECA", "MERMELADA", "DULCE DE LECHE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El queso", "planteo": "¿Cómo llega el queso a la mesa?", "pasos": ["Ordeñan la vaca.", "En la fábrica hacen el queso.", "Lo venden en el almacén."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el tambo se ordeñan las…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "En tu heladera", "planteo": "¿Qué productos de la leche hay en tu heladera?"},
"tip": {"titulo": "Una y muchos", "texto": "Una materia prima puede dar muchos productos."},
"ojo": ["La leche tiene que viajar fría.", "La mermelada no viene de la leche."],
"resumen": [{"titulo": "Tambo", "texto": "Se ordeñan las vacas."}, {"titulo": "Leche", "texto": "Materia prima."}, {"titulo": "Productos", "texto": "Queso, yogur, helado."}],
"glosario": [{"palabra": "Ordeñar", "significado": "Sacar la leche de la vaca."}, {"palabra": "Tambo", "significado": "Lugar donde se ordeña."}],
"carpeta": ["¿Qué producto de la lista NO viene de la leche?", "Nombrá uno que SÍ viene de la leche.", "Lola dice que el helado viene del tomate. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MERMELADA") + low("LA MERMELADA"), low("MANTECA") + low("LA MANTECA") + low("DULCE DE LECHE") + low("EL DULCE DE LECHE"), NO],
"soluciones": {"incompleto": "VACAS.", "solo": "Los productos de tu heladera.", "carpeta": ["La mermelada.", "Manteca o dulce de leche.", "No: viene de la leche."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ordenar las etapas de una producción.",
"vas_a_ver": ["En el campo", "En la fábrica", "En el negocio"],
"secciones": [
 S(1, "Las etapas", [
  P("Para hacer un producto hay <b>etapas</b>, una después de la otra."),
  IMG("Las cuatro etapas", "Siempre en orden.", FG.tiras(["1. CAMPO: SE OBTIENE", "2. FÁBRICA: SE TRANSFORMA", "3. CAMIÓN: SE TRANSPORTA", "4. NEGOCIO: SE VENDE"], numeros=False)),
 ]),
 S(1, "Un ejemplo: el pan", [
  P("El <b>trigo</b> crece en el campo. En el molino se hace <b>harina</b>."),
  P("En la panadería se hace el <b>pan</b>, y lo compramos."),
  P("Entre el campo y la panadería viajan camiones. Cada etapa necesita personas que trabajen. Si falta una, el pan no llega."),
  IMG("Del trigo al pan", "Tres lugares.", FG.nombres(["CAMPO", "MOLINO", "PANADERÍA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Qué va primero?", FG.tiras(["SE VENDE EN EL NEGOCIO", "SE OBTIENE EN EL CAMPO", "SE TRANSFORMA EN LA FÁBRICA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El jugo", "planteo": "¿Cuáles son las etapas del jugo?", "pasos": ["Cosechan naranjas en el campo.", "En la fábrica hacen jugo.", "Un camión lo lleva al negocio."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En la fábrica la materia prima se…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Dibujalo", "planteo": "Dibujá las etapas de un producto que te guste."},
"tip": {"titulo": "En orden", "texto": "Campo, fábrica, camión y negocio."},
"ojo": ["No se puede vender antes de fabricar.", "El transporte une el campo con la ciudad."],
"resumen": [{"titulo": "Campo", "texto": "Se obtiene."}, {"titulo": "Fábrica", "texto": "Se transforma."}, {"titulo": "Negocio", "texto": "Se vende."}],
"glosario": [{"palabra": "Etapa", "significado": "Un paso de algo más largo."}, {"palabra": "Transformar", "significado": "Cambiar una cosa en otra."}],
"carpeta": ["De las tarjetas, ¿qué va primero?", "¿Qué va al final?", "Lola dice que el pan se vende antes de hacerse. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("SE OBTIENE EN EL CAMPO") + low("EL CAMPO") + low("CAMPO"), low("SE VENDE EN EL NEGOCIO") + low("EL NEGOCIO") + low("NEGOCIO"), NO],
"soluciones": {"incompleto": "TRANSFORMA.", "solo": "Tu dibujo de las etapas.", "carpeta": ["Se obtiene en el campo.", "Se vende en el negocio.", "No: primero se hace."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer quiénes trabajan para hacer un producto.",
"vas_a_ver": ["En el campo", "En la fábrica", "Cuidarse al trabajar"],
"secciones": [
 S(1, "Muchos trabajos", [
  P("Para hacer un producto trabajan <b>muchas personas</b>."),
  IMG("Quiénes trabajan", "Cada uno hace una parte.", FG.tiras(["AGRICULTOR: COSECHA", "OPERARIA: USA LAS MÁQUINAS", "CHOFER: MANEJA EL CAMIÓN", "VENDEDORA: ATIENDE"], numeros=False)),
 ]),
 S(1, "Cuidarse al trabajar", [
  P("En la fábrica usan <b>guantes</b>, <b>gorro</b> y <b>barbijo</b>."),
  P("Así se cuidan y los alimentos quedan limpios."),
  P("Las operarias trabajan con horarios. Descansan para comer. Cuando terminan, otra persona sigue con la máquina."),
  IMG("Para cuidarse", "Ropa de trabajo.", FG.nombres(["GUANTES", "GORRO", "BARBIJO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Quién es?", "Pensá en cada trabajo.", FG.tiras(["1. MANEJA EL CAMIÓN HASTA EL NEGOCIO", "2. COSECHA EN EL CAMPO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La operaria", "planteo": "¿Qué hace la operaria?", "pasos": ["Se pone guantes y gorro.", "Usa las máquinas.", "Ayuda a hacer el producto."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El chofer maneja el…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Entrevista", "planteo": "Preguntale a un adulto de tu casa: ¿en qué trabajás?"},
"tip": {"titulo": "Todos importan", "texto": "Si falta un trabajo, el producto no llega."},
"ojo": ["Todos los trabajos son importantes.", "En la fábrica hay que cuidarse."],
"resumen": [{"titulo": "Campo", "texto": "Agricultor."}, {"titulo": "Fábrica", "texto": "Operaria."}, {"titulo": "Camino y negocio", "texto": "Chofer y vendedora."}],
"glosario": [{"palabra": "Operaria", "significado": "Persona que trabaja con máquinas."}, {"palabra": "Barbijo", "significado": "Tela que tapa nariz y boca."}],
"carpeta": ["¿Quién es la pista 1?", "¿Quién es la pista 2?", "Lola dice que un producto lo hace una sola persona. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("CHOFER") + low("EL CHOFER") + low("LA CHOFER") + low("CAMIONERO") + low("EL CAMIONERO"), low("AGRICULTOR") + low("EL AGRICULTOR") + low("AGRICULTORA") + low("LA AGRICULTORA"), NO],
"soluciones": {"incompleto": "CAMIÓN.", "solo": "Lo que te contaron.", "carpeta": ["El chofer.", "El agricultor.", "No: trabajan muchas personas."]},
}

ACT = {
"1": [MC("EL TOMATE ES…", ["MATERIA PRIMA", "PRODUCTO"], "MATERIA PRIMA", "SALE DE LA NATURALEZA.", n="aplicar"),
      ORD("ORDENÁ: DEL TOMATE A LA SALSA.", ["LOS COCINAN", "COSECHAN LOS TOMATES", "LOS ENVASAN"], ["COSECHAN LOS TOMATES", "LOS COCINAN", "LOS ENVASAN"], "PRIMERO SE COSECHA.", n="analizar")],
"2": [UNI("UNÍ CADA LUGAR CON LO QUE PASA.", [("TAMBO", "ORDEÑAN"), ("CAMIÓN", "VIAJA LA LECHE"), ("FÁBRICA", "HACEN QUESO")], "EL VIAJE DE LA LECHE.", n="analizar"),
      TF("LA MERMELADA VIENE DE LA LECHE.", "FALSO", "VIENE DE LA FRUTA.", n="error")],
"3": [ORD("ORDENÁ LAS ETAPAS.", ["NEGOCIO", "CAMPO", "FÁBRICA"], ["CAMPO", "FÁBRICA", "NEGOCIO"], "PRIMERO EL CAMPO.", n="analizar"),
      MC("¿DÓNDE SE HACE LA HARINA?", ["EN EL MOLINO", "EN EL NEGOCIO"], "EN EL MOLINO", "SE MUELE EL TRIGO.", n="aplicar")],
"4": [UNI("UNÍ CADA TRABAJO.", [("AGRICULTOR", "COSECHA"), ("CHOFER", "MANEJA"), ("VENDEDORA", "ATIENDE")], "CADA UNO HACE UNA PARTE.", n="analizar"),
      TF("EN LA FÁBRICA USAN GUANTES Y GORRO.", "VERDADERO", "PARA CUIDARSE.", n="recordar")],
"5": [MC("RELÁMPAGO. LA SALSA ES…", ["PRODUCTO", "MATERIA PRIMA"], "PRODUCTO", "SE HACE EN LA FÁBRICA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL QUESO VIENE DE…", ["LA LECHE", "EL TOMATE"], "LA LECHE", "DEL TAMBO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. PRIMERA ETAPA…", ["EL CAMPO", "EL NEGOCIO"], "EL CAMPO", "SE OBTIENE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. MANEJA EL CAMIÓN…", ["EL CHOFER", "LA VENDEDORA"], "EL CHOFER", "LLEVA LOS PRODUCTOS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES LA MATERIA PRIMA?", ["LO QUE SALE DE LA NATURALEZA", "LO QUE SE HACE EN LA FÁBRICA"], "LO QUE SALE DE LA NATURALEZA", "COMO EL TOMATE.", n="recordar")],
 [1, SA("¿QUÉ PRODUCTO SE HACE CON TOMATE?", low("SALSA") + low("LA SALSA") + low("PURÉ DE TOMATE") + low("KÉTCHUP") + low("ketchup"), "LA SALSA.", n="aplicar")],
 [1, TF("LA SALSA SALE SOLA DE LA PLANTA.", "FALSO", "LA HACEN EN UNA FÁBRICA.", n="error")],
 [2, MC("¿DÓNDE SE ORDEÑAN LAS VACAS?", ["EN EL TAMBO", "EN EL NEGOCIO"], "EN EL TAMBO", "EN EL CAMPO.", n="recordar")],
 [2, SA("NOMBRÁ UN PRODUCTO DE LA LECHE.", low("QUESO") + low("YOGUR") + low("HELADO") + low("MANTECA") + low("DULCE DE LECHE") + low("EL QUESO") + low("EL YOGUR") + low("EL HELADO") + low("LA MANTECA"), "POR EJEMPLO: QUESO.", n="aplicar")],
 [2, TF("CON LA LECHE SE HACEN MUCHOS PRODUCTOS.", "VERDADERO", "QUESO, YOGUR, HELADO.", n="recordar")],
 [3, ORD("ORDENÁ: DEL TRIGO AL PAN.", ["PANADERÍA", "CAMPO", "MOLINO"], ["CAMPO", "MOLINO", "PANADERÍA"], "TRIGO, HARINA, PAN.", n="analizar")],
 [3, MC("EN LA FÁBRICA, LA MATERIA PRIMA SE…", ["TRANSFORMA", "COSECHA"], "TRANSFORMA", "CAMBIA EN PRODUCTO.", n="aplicar")],
 [3, TF("EL PAN SE VENDE ANTES DE HACERSE.", "FALSO", "PRIMERO SE HACE.", n="error")],
 [4, UNI("UNÍ CADA LUGAR CON QUIÉN TRABAJA.", [("CAMPO", "AGRICULTOR"), ("FÁBRICA", "OPERARIA")], "CADA UNO EN SU LUGAR.", n="analizar")],
 [4, SA("¿QUÉ SE PONEN EN LA FÁBRICA PARA CUIDARSE?", low("GUANTES") + low("GORRO") + low("BARBIJO") + low("GUANTES Y GORRO") + low("LOS GUANTES") + low("EL GORRO") + low("EL BARBIJO"), "GUANTES, GORRO Y BARBIJO.", n="aplicar")],
 [4, TF("UN PRODUCTO LO HACE UNA SOLA PERSONA.", "FALSO", "TRABAJAN MUCHAS PERSONAS.", n="error")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: de la materia prima al producto", "examen_titulo": "Nivel jefe: de la materia prima al producto",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
