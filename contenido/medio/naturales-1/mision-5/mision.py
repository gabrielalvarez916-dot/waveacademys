# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 5 · Los objetos y sus materiales. Genera mision-5.json.
Regla de primeros años. Metáfora: el taller del abuelo (cada objeto, con su material).
Niveles: 1 objetos y materiales · 2 transparente, opaco y translúcido · 3 flexible y rígido · 4 elijo el material adecuado."""
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
"objetivo": "Vas a ver de qué materiales están hechos los objetos.",
"vas_a_ver": ["Objetos", "Materiales", "Un objeto, varios materiales"],
"secciones": [
 S(1, "Objetos y materiales", [
  D("Material", "Aquello con lo que está hecho un objeto."),
  P("La mesa es de <b>madera</b>. El vaso es de <b>vidrio</b>. La cuchara es de <b>metal</b>."),
  IMG("De qué están hechos", "Objeto y material.", FG.tiras(["MESA: MADERA", "VASO: VIDRIO", "CUCHARA: METAL", "BOTELLA: PLÁSTICO"], numeros=False, cols=2)),
 ]),
 S(1, "Varios materiales", [
  P("Algunos objetos tienen <b>varios materiales</b>. El lápiz tiene madera y grafito."),
  IMG("El lápiz", "Dos materiales.", FG.tiras(["MADERA", "GRAFITO"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los objetos. Los vas a usar en la carpeta."),
  IMG("Objetos", "¿De qué están hechos?", FG.nombres(["SILLA", "LLAVE", "BALDE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La cuchara", "planteo": "¿De qué es?", "pasos": ["Es fría y dura.", "Brilla.", "Es de metal."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La botella…", "pasos": ["La botella es de ___."]},
"ejemplo_solo": {"titulo": "En tu mochila", "planteo": "Buscá 3 objetos en tu mochila. ¿De qué son?"},
"tip": {"titulo": "Tocá y mirá", "texto": "¿Es frío, duro, liviano? Te da pistas."},
"ojo": ["El objeto no es el material: la mesa es de madera.", "Un objeto puede tener varios materiales."],
"resumen": [{"titulo": "Objeto", "texto": "Mesa, vaso."}, {"titulo": "Material", "texto": "Madera, vidrio, metal."}, {"titulo": "Varios", "texto": "El lápiz."}],
"glosario": [{"palabra": "Material", "significado": "Con lo que se hace un objeto."}, {"palabra": "Objeto", "significado": "Cosa que se puede usar."}],
"carpeta": ["¿De qué es la silla?", "¿De qué es la llave?", "¿De qué es el balde?"],
"respuestas_carpeta": [acepta("MADERA", "DE MADERA", "PLÁSTICO", "PLASTICO", "METAL"), acepta("METAL", "DE METAL"), acepta("PLÁSTICO", "PLASTICO", "DE PLÁSTICO", "METAL")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "PLÁSTICO.", "solo": "Depende de tu mochila.", "carpeta": ["MADERA.", "METAL.", "PLÁSTICO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver qué materiales dejan pasar la luz.",
"vas_a_ver": ["Transparente", "Opaco", "Translúcido"],
"secciones": [
 S(1, "Transparente y opaco", [
  P("<b>Transparente</b>: se ve a través, como el vidrio. <b>Opaco</b>: no se ve, como la madera."),
  IMG("Dos tipos", "¿Se ve o no?", FG.tiras(["VIDRIO: SE VE", "MADERA: NO SE VE"], numeros=False, cols=2)),
 ]),
 S(1, "Translúcido", [
  D("Translúcido", "Deja pasar un poco de luz, pero no se ve bien."),
  P("El papel de calcar y la cortina fina son translúcidos."),
  IMG("Tres tipos", "Mucha, poca o nada de luz.", FG.tiras(["TRANSPARENTE: MUCHA", "TRANSLÚCIDO: POCA", "OPACO: NADA"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Probá con una linterna. Lo vas a usar en la carpeta."),
  IMG("Probá", "¿Pasa la luz?", FG.nombres(["VENTANA", "CARTÓN", "CORTINA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La ventana", "planteo": "¿Cómo es?", "pasos": ["Miro a través.", "Veo la calle.", "Es transparente."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La puerta de madera…", "pasos": ["Es ___."]},
"ejemplo_solo": {"titulo": "Linterna", "planteo": "Alumbrá una hoja, un vaso y un cuaderno. ¿Qué pasa?"},
"tip": {"titulo": "Mirá a través", "texto": "Poné el objeto frente a tus ojos."},
"ojo": ["Translúcido no es transparente: no se ve bien.", "El vidrio pintado puede ser opaco."],
"resumen": [{"titulo": "Transparente", "texto": "Se ve a través."}, {"titulo": "Translúcido", "texto": "Pasa poca luz."}, {"titulo": "Opaco", "texto": "No pasa luz."}],
"glosario": [{"palabra": "Linterna", "significado": "Lámpara chiquita de mano."}, {"palabra": "A través", "significado": "De un lado al otro."}],
"carpeta": ["La ventana, ¿cómo es?", "El cartón, ¿cómo es?", "La cortina fina, ¿cómo es?"],
"respuestas_carpeta": [acepta("TRANSPARENTE"), acepta("OPACO"), acepta("TRANSLÚCIDA", "TRANSLUCIDA", "TRANSLÚCIDO", "TRANSLUCIDO")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "OPACA.", "solo": "Algunos dejan pasar la luz.", "carpeta": ["TRANSPARENTE.", "OPACO.", "TRANSLÚCIDA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver qué materiales se doblan y cuáles no.",
"vas_a_ver": ["Flexible", "Rígido", "Probar"],
"secciones": [
 S(1, "Flexible", [
  D("Flexible", "Se dobla sin romperse."),
  P("La goma, el papel y la tela son <b>flexibles</b>."),
  IMG("Flexibles", "Se doblan.", FG.nombres(["GOMA", "PAPEL", "TELA"], cols=3)),
 ]),
 S(1, "Rígido", [
  D("Rígido", "No se dobla."),
  P("La piedra, la madera gruesa y el vidrio son <b>rígidos</b>."),
  IMG("Rígidos", "No se doblan.", FG.nombres(["PIEDRA", "MADERA", "VIDRIO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los objetos. Los vas a usar en la carpeta."),
  IMG("Objetos", "¿Flexible o rígido?", FG.nombres(["MEDIA", "LADRILLO", "SORBETE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La regla", "planteo": "¿Se dobla?", "pasos": ["La regla de madera no se dobla.", "La de plástico fino sí.", "Depende del material."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La piedra…", "pasos": ["La piedra es ___."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Doblá con cuidado una hoja y un lápiz. ¿Qué pasa?"},
"tip": {"titulo": "Con cuidado", "texto": "Probá despacio: lo rígido se puede romper."},
"ojo": ["El vidrio es rígido: se rompe si lo doblás.", "El mismo objeto puede ser de materiales distintos."],
"resumen": [{"titulo": "Flexible", "texto": "Se dobla."}, {"titulo": "Rígido", "texto": "No se dobla."}, {"titulo": "Probar", "texto": "Con cuidado."}],
"glosario": [{"palabra": "Doblar", "significado": "Torcer algo."}, {"palabra": "Sorbete", "significado": "Tubito para tomar."}],
"carpeta": ["La media, ¿flexible o rígida?", "El ladrillo, ¿flexible o rígido?", "El sorbete, ¿flexible o rígido?"],
"respuestas_carpeta": [acepta("FLEXIBLE"), acepta("RÍGIDO", "RIGIDO"), acepta("FLEXIBLE")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "RÍGIDA.", "solo": "La hoja se dobla; el lápiz no.", "carpeta": ["FLEXIBLE.", "RÍGIDO.", "FLEXIBLE."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a elegir el mejor material para cada objeto.",
"vas_a_ver": ["Para qué sirve", "Qué material conviene", "Probar"],
"secciones": [
 S(1, "Pensar para qué sirve", [
  P("Primero pensás <b>para qué</b> sirve el objeto. Después elegís el material."),
  IMG("Pasos", "En orden.", FG.tiras(["¿PARA QUÉ SIRVE?", "¿QUÉ NECESITA?", "ELIJO", "PRUEBO"], numeros=True, cols=2)),
 ]),
 S(1, "El material adecuado", [
  D("Adecuado", "El que sirve mejor."),
  P("La ventana es de vidrio para <b>ver</b>. El paraguas es de plástico para <b>no mojarte</b>."),
  IMG("Bien elegido", "Material y razón.", FG.tiras(["VENTANA: VIDRIO", "PARAGUAS: PLÁSTICO", "PELOTA: GOMA", "PUERTA: MADERA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los objetos. Los vas a usar en la carpeta."),
  IMG("¿Qué material?", "Elegí el mejor.", FG.tiras(["CAMPERA PARA LA LLUVIA", "VASO PARA VER EL JUGO", "PELOTA PARA PICAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El paraguas", "planteo": "¿De qué lo hago?", "pasos": ["Sirve para la lluvia.", "Necesita no dejar pasar el agua.", "Elijo plástico."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Una ventana de madera…", "pasos": ["No sirve: no se puede ___."]},
"ejemplo_solo": {"titulo": "Inventá", "planteo": "Dibujá un objeto y escribí de qué material lo harías."},
"tip": {"titulo": "Preguntá para qué", "texto": "Siempre empezá por: ¿para qué sirve?"},
"ojo": ["Un paraguas de papel se rompe con la lluvia.", "El material lindo no siempre es el mejor."],
"resumen": [{"titulo": "Para qué", "texto": "Primero pensar."}, {"titulo": "Elegir", "texto": "El adecuado."}, {"titulo": "Probar", "texto": "Ver si sirve."}],
"glosario": [{"palabra": "Adecuado", "significado": "El que sirve mejor."}, {"palabra": "Impermeable", "significado": "No deja pasar el agua."}],
"carpeta": ["¿De qué material hacés la campera para la lluvia?", "¿De qué material hacés el vaso para ver el jugo?", "Tomi hizo un paraguas de papel. ¿Qué pasa?"],
"respuestas_carpeta": [acepta("PLÁSTICO", "PLASTICO", "NAILON", "NYLON"), acepta("VIDRIO", "PLÁSTICO TRANSPARENTE", "PLASTICO TRANSPARENTE"), acepta("SE MOJA", "SE ROMPE", "SE MOJA Y SE ROMPE", "NO SIRVE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "VER.", "solo": "Tu objeto y su material.", "carpeta": ["PLÁSTICO.", "VIDRIO.", "SE MOJA Y SE ROMPE."]},
}

ACT = {
"1": [MC("¿DE QUÉ ES LA CUCHARA?", ["METAL", "PAPEL", "TELA"], "METAL", "ES DE METAL.", n="aplicar"),
      MC("SOFI DICE QUE LA MESA ES UN MATERIAL. ¿QUÉ ES EN REALIDAD?", ["UN OBJETO DE MADERA", "UN MATERIAL", "UN SER VIVO"], "UN OBJETO DE MADERA", "LA MADERA ES EL MATERIAL.", n="error")],
"2": [MC("¿QUÉ MATERIAL ES TRANSPARENTE?", ["VIDRIO", "MADERA", "CARTÓN"], "VIDRIO", "SE VE A TRAVÉS.", n="recordar"),
      MC("NO SE VE NADA A TRAVÉS DE LA PUERTA. ¿CÓMO ES?", ["OPACA", "TRANSPARENTE", "TRANSLÚCIDA"], "OPACA", "NO PASA LA LUZ.", n="analizar")],
"3": [MC("¿CUÁL ES FLEXIBLE?", ["LA GOMA", "LA PIEDRA", "EL LADRILLO"], "LA GOMA", "SE DOBLA.", n="aplicar"),
      SA("UN OBJETO NO SE DOBLA. ¿CÓMO ES?", acepta("RÍGIDO", "RIGIDO", "RÍGIDA", "RIGIDA"), "RÍGIDO.", n="aplicar")],
"4": [MC("¿DE QUÉ HACÉS UN PARAGUAS?", ["PLÁSTICO", "PAPEL", "MADERA"], "PLÁSTICO", "NO DEJA PASAR EL AGUA.", n="aplicar"),
      MC("¿POR QUÉ LA VENTANA ES DE VIDRIO?", ["PARA VER AFUERA", "PARA QUE PESE", "PARA QUE SE DOBLE"], "PARA VER AFUERA", "EL VIDRIO ES TRANSPARENTE.", n="analizar")],
"5": [MC("RELÁMPAGO. ¿DE QUÉ ES LA BOTELLA?", ["PLÁSTICO", "MADERA", "TELA"], "PLÁSTICO", "PLÁSTICO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ES OPACO?", ["CARTÓN", "VIDRIO", "AGUA"], "CARTÓN", "NO PASA LA LUZ.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. LA TELA, ¿FLEXIBLE O RÍGIDA?", acepta("FLEXIBLE"), "FLEXIBLE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CON QUÉ SE HACE UNA PELOTA QUE PICA?", ["GOMA", "VIDRIO", "PIEDRA"], "GOMA", "LA GOMA REBOTA.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UN MATERIAL?", ["CON LO QUE SE HACE ALGO", "UN JUEGO DE PATIO", "UN ANIMAL DE CAMPO"], "CON LO QUE SE HACE ALGO", "MADERA, METAL, VIDRIO.", n="recordar")],
 [1, SA("¿DE QUÉ ES LA LLAVE?", acepta("METAL", "DE METAL"), "METAL.", n="aplicar")],
 [1, MC("EL LÁPIZ TIENE…", ["MADERA Y GRAFITO", "SOLO VIDRIO", "SOLO TELA"], "MADERA Y GRAFITO", "DOS MATERIALES.", n="recordar")],
 [2, MC("¿CÓMO ES LA VENTANA?", ["TRANSPARENTE", "OPACA", "FLEXIBLE"], "TRANSPARENTE", "SE VE A TRAVÉS.", n="aplicar")],
 [2, MC("LA CORTINA FINA DEJA PASAR UN POCO DE LUZ. ES…", ["TRANSLÚCIDA", "TRANSPARENTE", "OPACA"], "TRANSLÚCIDA", "PASA POCA LUZ.", n="analizar")],
 [2, MC("TOMI DICE QUE EL CARTÓN ES TRANSPARENTE. ¿ESTÁ BIEN?", ["NO: ES OPACO", "SÍ: ES TRANSPARENTE", "SÍ: ES FLEXIBLE"], "NO: ES OPACO", "NO PASA LA LUZ.", n="error")],
 [3, MC("¿CUÁL ES RÍGIDO?", ["EL LADRILLO", "LA MEDIA", "EL PAPEL"], "EL LADRILLO", "NO SE DOBLA.", n="aplicar")],
 [3, SA("LA GOMA SE DOBLA SIN ROMPERSE. ES…", acepta("FLEXIBLE"), "FLEXIBLE.", n="aplicar")],
 [3, MC("¿QUÉ PASA SI DOBLÁS UN VIDRIO?", ["SE ROMPE", "SE ESTIRA", "SE DOBLA"], "SE ROMPE", "EL VIDRIO ES RÍGIDO.", n="analizar")],
 [4, ORD("ORDENÁ LOS PASOS PARA ELEGIR UN MATERIAL.", ["ELIJO", "PRUEBO", "¿PARA QUÉ SIRVE?"], ["¿PARA QUÉ SIRVE?", "ELIJO", "PRUEBO"], "PRIMERO PENSAR, DESPUÉS ELEGIR Y PROBAR.", n="aplicar")],
 [4, MC("¿DE QUÉ HACÉS UNA PELOTA QUE PICA?", ["GOMA", "VIDRIO", "PAPEL"], "GOMA", "LA GOMA REBOTA.", n="aplicar")],
 [4, MC("SOFI HIZO UNA VENTANA DE MADERA. ¿QUÉ PROBLEMA HAY?", ["NO SE VE AFUERA", "SE MOJA LA CASA", "NINGUNO"], "NO SE VE AFUERA", "LA MADERA ES OPACA.", n="error")],
 [4, SA("¿DE QUÉ MATERIAL ES UN BUEN PARAGUAS?", acepta("PLÁSTICO", "PLASTICO", "NAILON", "NYLON", "TELA IMPERMEABLE"), "PLÁSTICO.", n="aplicar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: objetos y materiales", "examen_titulo": "Nivel jefe: objetos y materiales",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
