# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 3 · Plantas por fuera. Genera mision-3.json.
Regla de primeros años. Metáfora: el paseo por la plaza (exploradores de plantas).
Niveles: 1 las hojas, formas y bordes · 2 árboles, arbustos y hierbas · 3 dónde crecen mejor · 4 mi cuaderno de campo."""
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
"objetivo": "Vas a mirar las hojas: sus formas y sus bordes.",
"vas_a_ver": ["Formas de hojas", "Bordes", "Comparar hojas"],
"secciones": [
 S(1, "Formas", [
  P("Las hojas tienen formas distintas: <b>redondas</b>, <b>alargadas</b>, <b>como una mano</b>."),
  IMG("Formas", "Cada planta, su hoja.", FG.tiras(["REDONDA", "ALARGADA", "COMO UNA MANO"], numeros=False, cols=3)),
 ]),
 S(1, "Bordes", [
  D("Borde", "La orilla de la hoja."),
  P("Hay bordes <b>lisos</b> y bordes <b>con dientes</b>, como una sierra."),
  IMG("Bordes", "Liso o con dientes.", FG.tiras(["LISO", "CON DIENTES"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Juntá 3 hojas del patio o de la plaza."),
  IMG("Mis hojas", "Miralas de cerca.", FG.tiras(["HOJA 1", "HOJA 2", "HOJA 3"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La hoja del limonero", "planteo": "La miro.", "pasos": ["Es alargada.", "El borde es liso.", "Es verde y brillante."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La hoja de la rosa…", "pasos": ["Tiene el borde con ___."]},
"ejemplo_solo": {"titulo": "Calcá", "planteo": "Poné una hoja bajo un papel y pasá un crayón."},
"tip": {"titulo": "Tocá el borde", "texto": "Pasá el dedo despacio por la orilla."},
"ojo": ["No arranques hojas de plantas vivas: juntá las del suelo.", "Dos hojas de la misma planta se parecen."],
"resumen": [{"titulo": "Forma", "texto": "Redonda, alargada…"}, {"titulo": "Borde", "texto": "Liso o con dientes."}, {"titulo": "Comparar", "texto": "Ver cuál es distinta."}],
"glosario": [{"palabra": "Borde", "significado": "La orilla de la hoja."}, {"palabra": "Calcar", "significado": "Copiar pasando por encima."}],
"carpeta": ["¿Cómo puede ser el borde de una hoja?", "La hoja del limonero, ¿es redonda o alargada?", "¿Dónde juntás las hojas?"],
"respuestas_carpeta": [acepta("LISO", "CON DIENTES", "LISO O CON DIENTES"), acepta("ALARGADA"), acepta("DEL SUELO", "EN EL SUELO", "SUELO")],
"carpeta_nivel": ["recordar", "aplicar", "analizar"],
"soluciones": {"incompleto": "DIENTES.", "solo": "Aparece el dibujo de la hoja.", "carpeta": ["LISO O CON DIENTES.", "ALARGADA.", "DEL SUELO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer árboles, arbustos y hierbas.",
"vas_a_ver": ["Árboles", "Arbustos", "Hierbas"],
"secciones": [
 S(1, "Árboles", [
  P("El <b>árbol</b> es alto y tiene un <b>tronco</b> grueso y duro."),
  IMG("Tres tipos", "Del más alto al más bajo.", FG.tiras(["ÁRBOL: MUY ALTO", "ARBUSTO: MEDIANO", "HIERBA: BAJITA"], numeros=False, cols=3)),
 ]),
 S(1, "Arbustos y hierbas", [
  D("Arbusto", "Planta mediana con muchos tallos duros desde abajo."),
  P("La <b>hierba</b> es bajita y su tallo es blando y verde."),
  IMG("Tallos", "Duro o blando.", FG.tiras(["TRONCO: DURO", "TALLITOS: DUROS", "TALLO: BLANDO"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las plantas. Las vas a usar en la carpeta."),
  IMG("Plantas", "¿Árbol, arbusto o hierba?", FG.nombres(["PINO", "ROSAL", "PASTO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El pino", "planteo": "¿Qué es?", "pasos": ["Es muy alto.", "Tiene un tronco duro.", "Es un árbol."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El pasto…", "pasos": ["El pasto es una ___."]},
"ejemplo_solo": {"titulo": "En la plaza", "planteo": "Buscá un árbol, un arbusto y una hierba."},
"tip": {"titulo": "Mirá el tallo", "texto": "¿Es duro o blando? ¿Uno o muchos?"},
"ojo": ["Un árbol chiquito sigue siendo árbol.", "La hierba tiene tallo blando."],
"resumen": [{"titulo": "Árbol", "texto": "Alto, tronco duro."}, {"titulo": "Arbusto", "texto": "Mediano, muchos tallos."}, {"titulo": "Hierba", "texto": "Bajita, tallo blando."}],
"glosario": [{"palabra": "Tallo", "significado": "Parte que sostiene la planta."}, {"palabra": "Tronco", "significado": "Tallo grueso y duro del árbol."}],
"carpeta": ["El pino, ¿qué es?", "El rosal, ¿qué es?", "El pasto, ¿qué es?"],
"respuestas_carpeta": [acepta("ÁRBOL", "ARBOL", "UN ÁRBOL", "UN ARBOL"), acepta("ARBUSTO", "UN ARBUSTO"), acepta("HIERBA", "UNA HIERBA")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "HIERBA.", "solo": "Lo buscaste en la plaza.", "carpeta": ["ÁRBOL.", "ARBUSTO.", "HIERBA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver qué necesitan las plantas para crecer.",
"vas_a_ver": ["Luz", "Agua", "Tierra"],
"secciones": [
 S(1, "Lo que necesitan", [
  P("Las plantas necesitan <b>luz</b>, <b>agua</b> y <b>tierra</b>."),
  IMG("Necesitan", "Tres cosas.", FG.tiras(["LUZ", "AGUA", "TIERRA"], numeros=False, cols=3)),
 ]),
 S(1, "Una prueba", [
  D("Experimento", "Una prueba para ver qué pasa."),
  P("Una planta al sol crece verde. Una planta en el placard se pone amarilla."),
  IMG("Con luz y sin luz", "Mirá la diferencia.", FG.tiras(["CON LUZ: VERDE", "SIN LUZ: AMARILLA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Pensá dónde pondrías una planta."),
  IMG("¿Dónde?", "Elegí el mejor lugar.", FG.tiras(["VENTANA CON SOL", "PLACARD OSCURO"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "El poroto", "planteo": "Sofi planta un poroto.", "pasos": ["Lo pone en tierra.", "Lo riega.", "Lo deja al sol: ¡crece!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las plantas necesitan…", "pasos": ["LUZ, AGUA Y ___."]},
"ejemplo_solo": {"titulo": "Tu planta", "planteo": "Plantá un poroto en algodón húmedo y miralo cada día."},
"tip": {"titulo": "Ni mucha ni poca", "texto": "Regá un poco: mucha agua también hace mal."},
"ojo": ["Sin luz, la planta se pone amarilla.", "Mucha agua también daña."],
"resumen": [{"titulo": "Luz", "texto": "La pone verde."}, {"titulo": "Agua", "texto": "Justa."}, {"titulo": "Tierra", "texto": "Para las raíces."}],
"glosario": [{"palabra": "Regar", "significado": "Echar agua a las plantas."}, {"palabra": "Raíz", "significado": "Parte de la planta bajo la tierra."}],
"carpeta": ["¿Dónde crece mejor la planta?", "¿Qué le pasa a una planta sin luz?", "Tomi riega su planta con un balde entero cada día. ¿Está bien?"],
"respuestas_carpeta": [acepta("VENTANA", "EN LA VENTANA", "VENTANA CON SOL", "AL SOL", "CON SOL"), acepta("SE PONE AMARILLA", "AMARILLA", "SE SECA", "SE MUERE"), acepta("NO", "NO, MUCHA AGUA", "NO MUCHA AGUA HACE MAL")],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"soluciones": {"incompleto": "TIERRA.", "solo": "Lo vas a ver crecer.", "carpeta": ["EN LA VENTANA CON SOL.", "SE PONE AMARILLA.", "NO: MUCHA AGUA HACE MAL."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a armar tu cuaderno de campo.",
"vas_a_ver": ["Salir a observar", "Dibujar y anotar", "Partes de la hoja"],
"secciones": [
 S(1, "Cuaderno de campo", [
  D("Cuaderno de campo", "Cuaderno donde los científicos dibujan y anotan lo que ven."),
  P("Salís, <b>observás</b>, <b>dibujás</b> y <b>anotás</b>."),
  IMG("Los pasos", "En orden.", FG.tiras(["SALGO", "OBSERVO", "DIBUJO", "ANOTO"], numeros=True, cols=2)),
 ]),
 S(1, "Las partes de la hoja", [
  P("La hoja tiene parte ancha, <b>rayitas</b> y un <b>palito</b>."),
  IMG("Partes", "Para dibujar bien.", FG.tiras(["PARTE ANCHA", "RAYITAS: NERVADURAS", "PALITO: PECÍOLO"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la página. La vas a usar en la carpeta."),
  IMG("Página de Sofi", "Su cuaderno.", FG.tiras(["PLANTA: ROSAL", "TIPO: ARBUSTO", "BORDE: CON DIENTES", "LUGAR: PLAZA"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi página", "planteo": "Observo un pino.", "pasos": ["Lo dibujo.", "Anoto: PINO, ÁRBOL.", "Anoto el lugar: PLAZA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las rayitas de la hoja…", "pasos": ["Se llaman ___."]},
"ejemplo_solo": {"titulo": "Tu página", "planteo": "Dibujá una planta de tu casa y anotá su tipo."},
"tip": {"titulo": "Anotá el lugar", "texto": "Escribí dónde viste la planta."},
"ojo": ["Dibujá lo que ves, no lo que imaginás.", "Anotá enseguida, así no te olvidás."],
"resumen": [{"titulo": "Observar", "texto": "Mirar con atención."}, {"titulo": "Dibujar y anotar", "texto": "En el cuaderno."}, {"titulo": "Partes", "texto": "Nervaduras y pecíolo."}],
"glosario": [{"palabra": "Nervadura", "significado": "Rayita de la hoja."}, {"palabra": "Pecíolo", "significado": "Palito que une la hoja a la planta."}],
"carpeta": ["¿Qué planta observó Sofi?", "¿Dónde la vio?", "¿Qué tipo de planta es?"],
"respuestas_carpeta": [acepta("ROSAL", "UN ROSAL", "EL ROSAL"), acepta("PLAZA", "EN LA PLAZA", "LA PLAZA"), acepta("ARBUSTO", "UN ARBUSTO")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "NERVADURAS.", "solo": "Tu página del cuaderno.", "carpeta": ["UN ROSAL.", "EN LA PLAZA.", "ARBUSTO."]},
}

ACT = {
"1": [MC("¿CÓMO PUEDE SER EL BORDE DE UNA HOJA?", ["LISO O CON DIENTES", "DE PLUMAS", "DE ESCAMAS"], "LISO O CON DIENTES", "LISO O COMO UNA SIERRA.", n="recordar"),
      MC("TOMI ARRANCA HOJAS DE UNA PLANTA VIVA PARA OBSERVAR. ¿QUÉ CONVIENE?", ["JUNTAR LAS DEL SUELO", "ARRANCAR MÁS", "CORTAR LA PLANTA"], "JUNTAR LAS DEL SUELO", "ASÍ CUIDAMOS LA PLANTA.", n="error")],
"2": [MC("¿QUÉ PLANTA TIENE UN TRONCO GRUESO?", ["EL ÁRBOL", "LA HIERBA", "EL PASTO"], "EL ÁRBOL", "EL ÁRBOL TIENE TRONCO.", n="recordar"),
      MC("UNA PLANTA ES BAJITA Y TIENE TALLO BLANDO. ¿QUÉ ES?", ["UNA HIERBA", "UN ÁRBOL", "UN ARBUSTO"], "UNA HIERBA", "TALLO BLANDO: HIERBA.", n="analizar")],
"3": [MC("¿QUÉ NECESITAN LAS PLANTAS?", ["LUZ, AGUA Y TIERRA", "SOLO OSCURIDAD", "JUGO Y GALLETITAS"], "LUZ, AGUA Y TIERRA", "LAS TRES COSAS.", n="recordar"),
      MC("UNA PLANTA ESTUVO EN EL PLACARD Y ESTÁ AMARILLA. ¿QUÉ LE FALTÓ?", ["LUZ", "OSCURIDAD", "FRÍO"], "LUZ", "SIN LUZ SE PONE AMARILLA.", n="analizar")],
"4": [ORD("ORDENÁ LOS PASOS DEL CUADERNO DE CAMPO.", ["ANOTO", "SALGO", "DIBUJO", "OBSERVO"], ["SALGO", "OBSERVO", "DIBUJO", "ANOTO"], "SALGO, OBSERVO, DIBUJO, ANOTO.", n="aplicar"),
      SA("¿CÓMO SE LLAMAN LAS RAYITAS DE LA HOJA?", acepta("NERVADURAS", "NERVADURA", "LAS NERVADURAS"), "NERVADURAS.", n="recordar")],
"5": [MC("RELÁMPAGO. ¿CUÁL ES UN ÁRBOL?", ["PINO", "PASTO", "ROSAL"], "PINO", "ES ALTO CON TRONCO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. SIN LUZ, LA PLANTA SE PONE…", ["AMARILLA", "AZUL", "MÁS VERDE"], "AMARILLA", "LE FALTA LUZ.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. EL PASTO ES UNA…", acepta("HIERBA"), "HIERBA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL BORDE ES LA… DE LA HOJA", ["ORILLA", "RAÍZ", "FLOR"], "ORILLA", "EL BORDE ES LA ORILLA.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES EL BORDE DE UNA HOJA?", ["SU ORILLA", "SU RAÍZ", "SU FLOR"], "SU ORILLA", "LA ORILLA.", n="recordar")],
 [1, MC("LA HOJA DEL LIMONERO ES…", ["ALARGADA", "COMO UNA MANO", "CUADRADA"], "ALARGADA", "ALARGADA Y LISA.", n="aplicar")],
 [1, SA("¿CÓMO ES EL BORDE DE LA HOJA DE LA ROSA?", acepta("CON DIENTES", "DENTADO"), "CON DIENTES.", n="aplicar")],
 [2, MC("EL ROSAL ES MEDIANO Y TIENE MUCHOS TALLOS. ES…", ["UN ARBUSTO", "UN ÁRBOL", "UNA HIERBA"], "UN ARBUSTO", "MEDIANO, CON MUCHOS TALLOS.", n="aplicar")],
 [2, MC("SOFI VE UN PINO CHIQUITO Y DICE QUE ES HIERBA. ¿ESTÁ BIEN?", ["NO: ES UN ÁRBOL", "SÍ: ES CHIQUITO", "SÍ: ES VERDE"], "NO: ES UN ÁRBOL", "UN ÁRBOL CHIQUITO SIGUE SIENDO ÁRBOL.", n="error")],
 [2, SA("¿CÓMO SE LLAMA EL TALLO GRUESO Y DURO DEL ÁRBOL?", acepta("TRONCO", "EL TRONCO"), "TRONCO.", n="recordar")],
 [3, MC("¿DÓNDE CRECE MEJOR UNA PLANTA?", ["EN LA VENTANA CON SOL", "EN EL PLACARD", "EN LA HELADERA"], "EN LA VENTANA CON SOL", "NECESITA LUZ.", n="aplicar")],
 [3, MC("¿POR QUÉ LA PLANTA DEL PLACARD SE PUSO AMARILLA?", ["LE FALTÓ LUZ", "LE SOBRÓ LUZ", "TUVO MUCHO SOL"], "LE FALTÓ LUZ", "SIN LUZ SE PONE AMARILLA.", n="analizar")],
 [3, SA("COMPLETÁ: LAS PLANTAS NECESITAN LUZ, AGUA Y ___", acepta("TIERRA"), "TIERRA.", n="recordar")],
 [4, ORD("ORDENÁ LOS PASOS.", ["DIBUJO", "OBSERVO", "SALGO", "ANOTO"], ["SALGO", "OBSERVO", "DIBUJO", "ANOTO"], "EN ORDEN.", n="aplicar")],
 [4, MC("EL PALITO QUE UNE LA HOJA A LA PLANTA ES…", ["EL PECÍOLO", "LA RAÍZ", "EL BORDE"], "EL PECÍOLO", "PECÍOLO.", n="recordar")],
 [4, MC("TOMI DIBUJÓ UNA HOJA CON OJOS Y BOCA. ¿QUÉ PASÓ?", ["DIBUJÓ LO QUE IMAGINÓ", "DIBUJÓ LO QUE VIO", "ESTÁ PERFECTO"], "DIBUJÓ LO QUE IMAGINÓ", "SE DIBUJA LO QUE SE VE.", n="error")],
 [4, MC("¿PARA QUÉ SIRVE EL CUADERNO DE CAMPO?", ["ANOTAR Y DIBUJAR LO QUE VEO", "JUGAR A LA PELOTA", "GUARDAR HOJAS SECAS"], "ANOTAR Y DIBUJAR LO QUE VEO", "COMO LOS CIENTÍFICOS.", n="recordar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: plantas por fuera", "examen_titulo": "Nivel jefe: plantas por fuera",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
