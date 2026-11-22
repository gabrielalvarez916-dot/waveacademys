# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 6 · Del campo a mi mesa. Genera mision-6.json.
Regla de primeros años. Metáfora: el viaje de un tomate hasta la mesa.
Niveles: 1 la manzana, el tomate y la yerba mate · 2 las etapas de producir un alimento · 3 herramientas y técnicas de cultivo · 4 trabajos para todas las personas."""
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
"objetivo": "Vas a ver de dónde vienen algunos alimentos.",
"vas_a_ver": ["La manzana", "El tomate", "La yerba mate"],
"secciones": [
 S(1, "Vienen del campo", [
  D("Alimento", "Lo que comemos o tomamos para vivir."),
  P("La <b>manzana</b> crece en un árbol. El <b>tomate</b>, en una planta baja."),
  IMG("De dónde vienen", "Plantas distintas.", FG.tiras(["MANZANA: ÁRBOL", "TOMATE: PLANTA", "YERBA: ARBUSTO"], numeros=False, cols=3)),
 ]),
 S(1, "La yerba mate", [
  P("La <b>yerba mate</b> sale de las <b>hojas</b> de un arbusto. Se secan y se muelen."),
  IMG("La yerba", "De la hoja al paquete.", FG.tiras(["HOJAS", "SE SECAN", "SE MUELEN", "PAQUETE"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los alimentos. Los vas a usar en la carpeta."),
  IMG("¿Qué parte se come?", "Pensá.", FG.tiras(["MANZANA: FRUTO", "YERBA: HOJAS", "TOMATE: FRUTO"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El tomate", "planteo": "Sofi mira la planta.", "pasos": ["Primero está verde.", "Después se pone rojo.", "¡Ya se puede cosechar!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La manzana crece en un…", "pasos": ["La manzana crece en un ___."]},
"ejemplo_solo": {"titulo": "En tu heladera", "planteo": "Buscá en tu casa un alimento que venga del campo."},
"tip": {"titulo": "Pensá de dónde viene", "texto": "Todo lo que comés empezó en algún lugar."},
"ojo": ["La fruta se lava antes de comer.", "Muchos alimentos vienen de plantas."],
"resumen": [{"titulo": "Manzana", "texto": "Del árbol."}, {"titulo": "Tomate", "texto": "De una planta."}, {"titulo": "Yerba", "texto": "Hojas secas y molidas."}],
"glosario": [{"palabra": "Cosechar", "significado": "Juntar lo que dio la planta."}, {"palabra": "Fruto", "significado": "Parte de la planta que tiene semillas."}],
"carpeta": ["¿Dónde crece la manzana?", "¿Qué parte de la planta da la yerba?", "¿De qué color es el tomate maduro?"],
"respuestas_carpeta": [acepta("ÁRBOL", "ARBOL", "EN UN ÁRBOL", "EN UN ARBOL"), acepta("HOJAS", "LAS HOJAS"), acepta("ROJO")],
"carpeta_nivel": ["recordar", "recordar", "aplicar"],
"soluciones": {"incompleto": "ÁRBOL.", "solo": "Por ejemplo: la lechuga.", "carpeta": ["EN UN ÁRBOL.", "LAS HOJAS.", "ROJO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer las etapas para producir un alimento.",
"vas_a_ver": ["Sembrar y cuidar", "Cosechar", "Llevar y vender"],
"secciones": [
 S(1, "Las etapas", [
  D("Etapa", "Cada paso de un trabajo, uno después de otro."),
  P("Primero se <b>siembra</b>, después se <b>cuida</b> y se <b>cosecha</b>."),
  IMG("En el campo", "Paso a paso.", FG.tiras(["SIEMBRO", "CUIDO", "COSECHO"], numeros=True, cols=3)),
 ]),
 S(1, "Hasta la mesa", [
  P("Después se <b>transporta</b> en camión, se <b>vende</b> y llega a tu <b>mesa</b>."),
  IMG("Hasta mi casa", "Paso a paso.", FG.tiras(["TRANSPORTO", "VENDO", "COMO"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las etapas mezcladas. Las vas a usar en la carpeta."),
  IMG("Mezcladas", "Ordenalas.", FG.tiras(["COSECHO", "SIEMBRO", "VENDO"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El tomate viaja", "planteo": "Del campo a la verdulería.", "pasos": ["La agricultora lo cosecha.", "El camionero lo lleva.", "El verdulero lo vende."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Primero se siembra, después…", "pasos": ["Se ___ la planta."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntá en la verdulería de dónde vienen los tomates."},
"tip": {"titulo": "Una cadena", "texto": "Cada etapa necesita la anterior."},
"ojo": ["Sin sembrar no hay cosecha.", "En cada etapa trabaja gente distinta."],
"resumen": [{"titulo": "Campo", "texto": "Sembrar, cuidar, cosechar."}, {"titulo": "Viaje", "texto": "Transportar."}, {"titulo": "Mesa", "texto": "Vender y comer."}],
"glosario": [{"palabra": "Sembrar", "significado": "Poner semillas en la tierra."}, {"palabra": "Transportar", "significado": "Llevar de un lugar a otro."}],
"carpeta": ["¿Qué etapa va primero?", "¿Qué etapa va al final?", "Tomi dice que primero se cosecha y después se siembra. ¿Está bien?"],
"respuestas_carpeta": [acepta("SIEMBRO", "SEMBRAR", "SIEMBRA"), acepta("VENDO", "VENDER"), acepta("NO", "NO, PRIMERO SE SIEMBRA")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "CUIDA.", "solo": "Lo que te contaron.", "carpeta": ["SIEMBRO.", "VENDO.", "NO: PRIMERO SE SIEMBRA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer herramientas y técnicas para cultivar.",
"vas_a_ver": ["Herramientas", "Antes y ahora", "Técnicas"],
"secciones": [
 S(1, "Herramientas", [
  D("Herramienta", "Objeto que ayuda a hacer un trabajo."),
  P("Se usan <b>pala</b>, <b>azada</b>, <b>regadera</b> y <b>tractor</b>."),
  IMG("Herramientas", "Para cultivar.", FG.tiras(["PALA", "AZADA", "REGADERA", "TRACTOR"], numeros=False, cols=2)),
 ]),
 S(1, "Antes y ahora", [
  P("Antes se trabajaba <b>a mano</b>. Ahora hay <b>máquinas</b> que ayudan."),
  IMG("Cambió", "Con el tiempo.", FG.tiras(["ANTES: A MANO", "AHORA: CON TRACTOR"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tareas. Las vas a usar en la carpeta."),
  IMG("¿Qué herramienta?", "Pensá.", FG.tiras(["REGAR LA HUERTA", "HACER UN POZO", "ARAR UN CAMPO GRANDE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La huerta", "planteo": "La abuela cultiva.", "pasos": ["Hace surcos con la azada.", "Pone semillas.", "Riega con la regadera."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para regar uso…", "pasos": ["La ___."]},
"ejemplo_solo": {"titulo": "Tu huerta", "planteo": "Plantá una semilla en un vaso. ¿Qué herramienta usaste?"},
"tip": {"titulo": "Cada una sirve", "texto": "Cada herramienta sirve para un trabajo."},
"ojo": ["Las herramientas se usan con cuidado y con un adulto.", "El tractor lo maneja un adulto."],
"resumen": [{"titulo": "Herramientas", "texto": "Pala, azada, regadera."}, {"titulo": "Antes", "texto": "A mano."}, {"titulo": "Ahora", "texto": "Con máquinas."}],
"glosario": [{"palabra": "Surco", "significado": "Zanja en la tierra para sembrar."}, {"palabra": "Arar", "significado": "Abrir la tierra para sembrar."}],
"carpeta": ["¿Qué usás para regar la huerta?", "¿Qué usás para hacer un pozo?", "¿Qué conviene para arar un campo grande?"],
"respuestas_carpeta": [acepta("REGADERA", "LA REGADERA"), acepta("PALA", "LA PALA"), acepta("TRACTOR", "EL TRACTOR", "UN TRACTOR")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "REGADERA.", "solo": "Por ejemplo: una cuchara como pala.", "carpeta": ["LA REGADERA.", "LA PALA.", "EL TRACTOR."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver que todos los trabajos son para todas las personas.",
"vas_a_ver": ["Muchos trabajos", "Mujeres y varones", "Todos ayudan"],
"secciones": [
 S(1, "Muchos trabajos", [
  P("Para que la manzana llegue a tu mesa trabajan <b>muchas personas</b>."),
  IMG("Trabajan", "En cada etapa.", FG.tiras(["AGRICULTORA", "CAMIONERO", "VERDULERA"], numeros=False, cols=3)),
 ]),
 S(1, "Para todas las personas", [
  D("Igualdad", "Todas las personas pueden hacer cualquier trabajo."),
  P("Mujeres y varones pueden <b>manejar un tractor</b>, <b>cosechar</b> o <b>vender</b>."),
  IMG("Todos pueden", "Mujeres y varones.", FG.tiras(["ELLA MANEJA EL TRACTOR", "ÉL COCINA", "ELLA VENDE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las frases. Las vas a usar en la carpeta."),
  IMG("¿Está bien?", "Pensá.", FG.tiras(["SOLO LOS VARONES MANEJAN", "TODOS PUEDEN COSECHAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La chacra de Ana", "planteo": "Ana tiene una chacra.", "pasos": ["Maneja el tractor.", "Cosecha tomates.", "Su hermano los vende."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los trabajos son…", "pasos": ["Para ___ las personas."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntá en casa en qué trabaja cada persona."},
"tip": {"titulo": "Todos pueden", "texto": "No hay trabajos solo de mujeres o solo de varones."},
"ojo": ["Todos los trabajos son importantes.", "Cada persona elige lo que le gusta."],
"resumen": [{"titulo": "Muchos", "texto": "Trabajan muchas personas."}, {"titulo": "Igualdad", "texto": "Todos pueden."}, {"titulo": "Importantes", "texto": "Todos los trabajos."}],
"glosario": [{"palabra": "Igualdad", "significado": "Todos con los mismos derechos."}, {"palabra": "Chacra", "significado": "Campo chico donde se cultiva."}],
"carpeta": ["Solo los varones manejan, ¿está bien?", "Todos pueden cosechar, ¿está bien?", "¿Quiénes pueden manejar un tractor?"],
"respuestas_carpeta": [acepta("NO"), acepta("SÍ", "SI"), acepta("TODOS", "TODAS LAS PERSONAS", "MUJERES Y VARONES", "CUALQUIERA")],
"carpeta_nivel": ["error", "aplicar", "analizar"],
"soluciones": {"incompleto": "TODAS.", "solo": "Lo que te contaron.", "carpeta": ["NO.", "SÍ.", "TODAS LAS PERSONAS."]},
}

ACT = {
"1": [MC("¿DÓNDE CRECE LA MANZANA?", ["EN UN ÁRBOL", "EN EL MAR", "EN UNA FÁBRICA"], "EN UN ÁRBOL", "EN EL MANZANO.", n="recordar"),
      MC("EL TOMATE ESTÁ VERDE. ¿YA SE PUEDE COSECHAR?", ["NO: FALTA QUE MADURE", "SÍ: YA ESTÁ", "NUNCA"], "NO: FALTA QUE MADURE", "SE COSECHA ROJO.", n="analizar")],
"2": [ORD("ORDENÁ LAS ETAPAS.", ["COSECHO", "VENDO", "SIEMBRO"], ["SIEMBRO", "COSECHO", "VENDO"], "SIEMBRO, COSECHO, VENDO.", n="aplicar"),
      MC("SIN EL CAMIONERO, ¿QUÉ PASA?", ["EL TOMATE NO LLEGA", "NO PASA NADA", "SE SIEMBRA SOLO"], "EL TOMATE NO LLEGA", "CADA ETAPA ES IMPORTANTE.", n="analizar")],
"3": [MC("¿CON QUÉ REGÁS LA HUERTA?", ["REGADERA", "TRACTOR", "PALA"], "REGADERA", "LA REGADERA.", n="aplicar"),
      MC("ANTES SE TRABAJABA A MANO. ¿QUÉ AYUDA AHORA?", ["LAS MÁQUINAS", "NADA", "LA TELE"], "LAS MÁQUINAS", "COMO EL TRACTOR.", n="recordar")],
"4": [MC("¿QUIÉN PUEDE MANEJAR UN TRACTOR?", ["TODAS LAS PERSONAS", "SOLO LOS VARONES", "NADIE"], "TODAS LAS PERSONAS", "MUJERES Y VARONES.", n="recordar"),
      MC("TOMI DICE QUE COCINAR ES SOLO DE MUJERES. ¿ESTÁ BIEN?", ["NO: ES PARA TODOS", "SÍ: SOLO MUJERES", "SÍ: SOLO ABUELAS"], "NO: ES PARA TODOS", "TODOS PUEDEN COCINAR.", n="error")],
"5": [MC("RELÁMPAGO. ¿DE QUÉ PARTE SALE LA YERBA?", ["HOJAS", "RAÍZ", "FLOR"], "HOJAS", "HOJAS SECAS Y MOLIDAS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ VA PRIMERO?", ["SEMBRAR", "VENDER", "COMER"], "SEMBRAR", "SIN SEMBRAR NO HAY COSECHA.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. ¿CON QUÉ HACÉS UN POZO?", acepta("PALA", "CON UNA PALA", "LA PALA"), "PALA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿PARA QUIÉN SON LOS TRABAJOS?", ["PARA TODOS", "SOLO VARONES", "SOLO MUJERES"], "PARA TODOS", "IGUALDAD.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("EL TOMATE CRECE EN…", ["UNA PLANTA", "UN ÁRBOL ALTO", "EL MAR"], "UNA PLANTA", "UNA PLANTA BAJA.", n="recordar")],
 [1, ORD("ORDENÁ CÓMO SE HACE LA YERBA.", ["SE MUELEN", "HOJAS", "SE SECAN"], ["HOJAS", "SE SECAN", "SE MUELEN"], "HOJAS, SECAR, MOLER.", n="aplicar")],
 [1, SA("¿DE QUÉ COLOR ES EL TOMATE MADURO?", acepta("ROJO"), "ROJO.", n="recordar")],
 [2, MC("SEMBRAR ES…", ["PONER SEMILLAS EN LA TIERRA", "VENDER EN LA VERDULERÍA", "COMER LA FRUTA"], "PONER SEMILLAS EN LA TIERRA", "LA PRIMERA ETAPA.", n="recordar")],
 [2, ORD("ORDENÁ EL VIAJE DEL TOMATE.", ["TRANSPORTO", "COSECHO", "COMO", "VENDO"], ["COSECHO", "TRANSPORTO", "VENDO", "COMO"], "DEL CAMPO A LA MESA.", n="aplicar")],
 [2, MC("¿QUÉ PASA SI NO SE SIEMBRA?", ["NO HAY COSECHA", "HAY MÁS TOMATES", "NADA"], "NO HAY COSECHA", "CADA ETAPA NECESITA LA ANTERIOR.", n="analizar")],
 [3, MC("UNA HERRAMIENTA ES…", ["UN OBJETO QUE AYUDA A TRABAJAR", "UNA FRUTA DEL CAMPO", "UN ANIMAL DE GRANJA"], "UN OBJETO QUE AYUDA A TRABAJAR", "PALA, AZADA, REGADERA.", n="recordar")],
 [3, MC("¿QUÉ CONVIENE PARA ARAR UN CAMPO GRANDE?", ["UN TRACTOR", "UNA CUCHARA", "UNA REGADERA"], "UN TRACTOR", "ES MÁS RÁPIDO.", n="analizar")],
 [3, SA("¿CON QUÉ HERRAMIENTA SE RIEGA?", acepta("REGADERA", "LA REGADERA", "CON LA REGADERA"), "REGADERA.", n="aplicar")],
 [4, MC("IGUALDAD QUIERE DECIR QUE…", ["TODOS PUEDEN HACER CUALQUIER TRABAJO", "SOLO ALGUNOS TRABAJAN", "NADIE TRABAJA EN EL CAMPO"], "TODOS PUEDEN HACER CUALQUIER TRABAJO", "MUJERES Y VARONES.", n="recordar")],
 [4, MC("ANA MANEJA EL TRACTOR DE SU CHACRA. ¿ESTÁ BIEN?", ["SÍ: TODOS PUEDEN", "NO: ES DE VARONES", "NO: ES DE GRANDES"], "SÍ: TODOS PUEDEN", "NO HAY TRABAJOS DE UN SOLO GRUPO.", n="aplicar")],
 [4, MC("SOFI DICE QUE SOLO LOS VARONES COSECHAN. ¿QUÉ ESTÁ MAL?", ["TODOS PUEDEN COSECHAR", "NADA", "SOLO COSECHAN LOS CHICOS"], "TODOS PUEDEN COSECHAR", "IGUALDAD.", n="error")],
 [4, SA("¿QUIÉN LLEVA EL TOMATE EN CAMIÓN?", acepta("CAMIONERO", "EL CAMIONERO", "CAMIONERA", "LA CAMIONERA"), "EL CAMIONERO O LA CAMIONERA.", n="aplicar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: del campo a mi mesa", "examen_titulo": "Nivel jefe: del campo a mi mesa",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
