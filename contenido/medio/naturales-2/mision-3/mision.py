# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 3 · De la flor al fruto. Genera mision-3.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador con su lupa (hoy en la huerta de la escuela).
Niveles: 1 flores y frutos · 2 cómo viajan las semillas · 3 plantas que nacen sin semillas · 4 armo mi semillero."""
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
"objetivo": "Vas a ver cómo una flor se convierte en fruto.",
"vas_a_ver": ["La flor", "El fruto", "Las semillas"],
"secciones": [
 S(1, "De la flor al fruto", [
  P("En la huerta, Tomi ve una planta de tomate con <b>flores</b> amarillas."),
  P("Días después, ¡en lugar de la flor hay un <b>tomate</b>!"),
  IMG("De la flor al fruto", "La flor se convierte en fruto.", FG.objetos([("flor", "FLOR"), ("fruto", "FRUTO"), ("semilla", "SEMILLAS")])),
 ]),
 S(1, "Adentro del fruto", [
  D("Fruto", "Se forma de la <b>flor</b> y guarda las <b>semillas</b> adentro."),
  P("Manzana, naranja, tomate y zapallo son frutos."),
  IMG("Frutos con semillas", "Las semillas van adentro.", FG.nombres(["MANZANA", "NARANJA", "TOMATE", "ZAPALLO"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("En orden", "¿Qué va primero?", FG.nombres(["FRUTO", "FLOR", "SEMILLA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El tomate", "planteo": "¿De dónde sale el tomate?", "pasos": ["La planta da una flor.", "La flor se convierte en fruto.", "Adentro hay semillas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El fruto guarda…", "pasos": ["El fruto guarda las ___ ."]},
"ejemplo_solo": {"titulo": "Investigá", "planteo": "Con un adulto, abrí una fruta y contá sus semillas."},
"tip": {"titulo": "Mirá adentro", "texto": "Si tiene semillas adentro, es un fruto."},
"ojo": ["El tomate también es un fruto.", "La flor viene antes que el fruto."],
"resumen": [{"titulo": "Flor", "texto": "Primero."}, {"titulo": "Fruto", "texto": "Sale de la flor."}, {"titulo": "Semillas", "texto": "Adentro del fruto."}],
"glosario": [{"palabra": "Fruto", "significado": "Sale de la flor y guarda semillas."}, {"palabra": "Huerta", "significado": "Lugar donde se cultivan plantas."}],
"carpeta": ["De las palabras del dibujo, ¿qué va primero en la planta?", "¿Qué hay adentro del fruto?", "Tomi dice que el tomate no es un fruto. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "recordar", "error"],
"respuestas_carpeta": [low("FLOR") + low("LA FLOR"), low("SEMILLAS") + low("LAS SEMILLAS") + low("SEMILLA"), NO],
"soluciones": {"incompleto": "SEMILLAS.", "solo": "Las semillas que contaste.", "carpeta": ["La flor.", "Semillas.", "No: tiene semillas, es un fruto."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a saber cómo viajan las semillas.",
"vas_a_ver": ["Con el viento", "Con los animales", "Con el agua"],
"secciones": [
 S(1, "Semillas viajeras", [
  P("Las semillas <b>viajan</b> lejos de la planta para crecer en otro lugar."),
  IMG("Cómo viajan", "Tres formas.", FG.tiras(["CON EL VIENTO: EL PANADERO", "CON LOS ANIMALES: SE PEGAN AL PELO", "CON EL AGUA: EL COCO"], numeros=False, cols=1)),
 ]),
 S(1, "Los animales ayudan", [
  P("Los pájaros comen frutos y dejan las semillas en otro lugar."),
  P("Algunas semillas tienen <b>pinches</b> y se pegan al pelo de los perros."),
  IMG("Los ayudantes", "Pájaros y perros.", FG.objetos([("hornero", "PÁJARO"), ("semilla", "SEMILLA")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las semillas. Las vas a usar en la carpeta."),
  IMG("¿Cómo viaja?", "Pensá en cada una.", FG.tiras(["1. LIVIANA, CON PELITOS", "2. CON PINCHES", "3. FLOTA EN EL AGUA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El panadero", "planteo": "¿Cómo viaja el panadero?", "pasos": ["Es muy liviano.", "Tiene pelitos.", "Lo lleva el viento."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los pájaros…", "pasos": ["Comen frutos y llevan las ___ ."]},
"ejemplo_solo": {"titulo": "Soplá", "planteo": "Si encontrás un panadero, soplalo y mirá cómo vuela."},
"tip": {"titulo": "Mirá la forma", "texto": "La forma de la semilla te dice cómo viaja."},
"ojo": ["No todas las semillas viajan igual.", "Viajar las ayuda a crecer lejos."],
"resumen": [{"titulo": "Viento", "texto": "Semillas livianas."}, {"titulo": "Animales", "texto": "Comen o se pegan."}, {"titulo": "Agua", "texto": "Semillas que flotan."}],
"glosario": [{"palabra": "Panadero", "significado": "Semilla liviana que vuela con el viento."}, {"palabra": "Pinche", "significado": "Puntita que se engancha."}],
"carpeta": ["¿Cómo viaja la semilla 1?", "¿Cómo viaja la semilla 2?", "Tomi dice que todas las semillas viajan igual. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("CON EL VIENTO") + low("VIENTO") + low("EL VIENTO"), low("CON LOS ANIMALES") + low("ANIMALES") + low("PEGADA A LOS ANIMALES") + low("CON ANIMALES"), NO],
"soluciones": {"incompleto": "SEMILLAS.", "solo": "Cómo voló el panadero.", "carpeta": ["Con el viento.", "Con los animales.", "No: viajan de distintas formas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer plantas que nacen sin semillas.",
"vas_a_ver": ["Un gajo", "La papa", "Plantas nuevas"],
"secciones": [
 S(1, "Un gajo", [
  D("Gajo", "Un <b>pedacito de tallo</b> que, en agua o tierra, echa raíces."),
  P("De un gajo nace una planta <b>nueva</b>, sin semillas."),
  IMG("Un gajo en agua", "Le salen raíces.", FG.tiras(["1. CORTO UN GAJO", "2. LO PONGO EN AGUA", "3. LE SALEN RAÍCES", "4. LO PLANTO"], numeros=False)),
 ]),
 S(1, "La papa", [
  P("Una <b>papa</b> vieja echa <b>brotes</b>. Si la plantamos, ¡crece otra planta!"),
  IMG("Sin semillas", "Gajos y papas.", FG.nombres(["GAJO", "PAPA", "BATATA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los pasos. Los vas a usar en la carpeta."),
  IMG("Pasos desordenados", "¿Qué va primero?", FG.tiras(["LE SALEN RAÍCES", "CORTO UN GAJO", "LO PONGO EN AGUA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Un gajo", "planteo": "¿Cómo nace una planta de un gajo?", "pasos": ["Corto un gajo.", "Lo pongo en agua.", "Echa raíces y lo planto."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La papa vieja…", "pasos": ["La papa vieja echa ___ ."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Con un adulto, poné un gajo en agua. Miralo cada día."},
"tip": {"titulo": "Paciencia", "texto": "Las raíces tardan varios días en salir."},
"ojo": ["No todas las plantas nacen de semillas.", "El agua del gajo hay que cambiarla."],
"resumen": [{"titulo": "Gajo", "texto": "Pedacito de tallo."}, {"titulo": "Raíces", "texto": "Le salen en agua."}, {"titulo": "Papa", "texto": "Echa brotes."}],
"glosario": [{"palabra": "Gajo", "significado": "Pedacito de tallo que echa raíces."}, {"palabra": "Brote", "significado": "Planta nueva que empieza a salir."}],
"carpeta": ["De los pasos del dibujo, ¿qué va primero?", "¿Qué va al final?", "Tomi dice que todas las plantas nacen de semillas. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("CORTO UN GAJO") + low("CORTAR UN GAJO"), low("LE SALEN RAÍCES") + low("le salen raices") + low("SALEN RAÍCES"), NO],
"soluciones": {"incompleto": "BROTES.", "solo": "Lo que viste cada día.", "carpeta": ["Corto un gajo.", "Le salen raíces.", "No: algunas nacen de gajos."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a armar tu propio semillero.",
"vas_a_ver": ["Los materiales", "Los pasos", "Observar y anotar"],
"secciones": [
 S(1, "Materiales", [
  P("Tomi arma un <b>semillero</b> para ver crecer una planta."),
  IMG("Lo que necesito", "Materiales.", FG.objetos([("maceta", "VASO CON TIERRA"), ("semilla", "SEMILLAS")])),
 ]),
 S(1, "Los pasos", [
  IMG("Cómo se arma", "En orden.", FG.tiras(["1. PONGO TIERRA EN UN VASO", "2. HAGO UN POZITO", "3. PONGO LAS SEMILLAS", "4. RIEGO UN POCO"], numeros=False)),
  P("Lo dejo en un lugar con <b>luz</b>. Cada día miro y <b>anoto</b> lo que pasa."),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla de Tomi. La vas a usar en la carpeta."),
  IMG("Lo que anotó Tomi", "Un día por renglón.", FG.ficha([("Día 1:", "siembro"), ("Día 5:", "sale un brote"), ("Día 10:", "tiene hojitas")], titulo="Mi semillero")),
 ]),
],
"ejemplo_completo": {"titulo": "Regar", "planteo": "¿Cuánta agua le pongo?", "pasos": ["Un poquito.", "Que la tierra quede húmeda.", "No hay que inundarla."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La planta necesita…", "pasos": ["Agua, tierra y ___ ."]},
"ejemplo_solo": {"titulo": "Tu semillero", "planteo": "Armá tu semillero con porotos o lentejas y anotá qué pasa."},
"tip": {"titulo": "Anotá todo", "texto": "Un científico anota lo que observa cada día."},
"ojo": ["Mucha agua pudre las semillas.", "Sin luz, la planta crece débil."],
"resumen": [{"titulo": "Materiales", "texto": "Vaso, tierra, semillas."}, {"titulo": "Pasos", "texto": "Tierra, semilla, agua, luz."}, {"titulo": "Anotar", "texto": "Lo que pasa cada día."}],
"glosario": [{"palabra": "Semillero", "significado": "Lugar para hacer crecer semillas."}, {"palabra": "Observar", "significado": "Mirar con atención."}],
"carpeta": ["En la tabla de Tomi, ¿qué pasó el día 5?", "¿Qué tenía la planta el día 10?", "Tomi dice que hay que inundar el vaso de agua. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("SALE UN BROTE") + low("SALIÓ UN BROTE") + low("salio un brote") + low("UN BROTE"), low("HOJITAS") + low("TIENE HOJITAS") + low("HOJAS"), NO],
"soluciones": {"incompleto": "LUZ.", "solo": "Lo que anotaste.", "carpeta": ["Sale un brote.", "Hojitas.", "No: solo un poco de agua."]},
}

ACT = {
"1": [ORD("ORDENÁ: DE LA FLOR AL FRUTO.", ["FRUTO", "FLOR", "SEMILLAS ADENTRO"], ["FLOR", "FRUTO", "SEMILLAS ADENTRO"], "PRIMERO LA FLOR.", n="analizar"),
      TF("EL TOMATE ES UN FRUTO.", "VERDADERO", "TIENE SEMILLAS ADENTRO.", n="aplicar")],
"2": [UNI("UNÍ CADA SEMILLA CON CÓMO VIAJA.", [("PANADERO", "VIENTO"), ("SEMILLA CON PINCHES", "ANIMALES"), ("COCO", "AGUA")], "MIRÁ SU FORMA.", n="analizar"),
      MC("¿QUÉ HACEN LOS PÁJAROS CON LAS SEMILLAS?", ["LAS LLEVAN LEJOS", "LAS ROMPEN TODAS"], "LAS LLEVAN LEJOS", "COMEN FRUTOS Y LAS DEJAN EN OTRO LUGAR.", n="aplicar")],
"3": [MC("¿QUÉ ES UN GAJO?", ["UN PEDACITO DE TALLO", "UNA SEMILLA"], "UN PEDACITO DE TALLO", "ECHA RAÍCES.", n="recordar"),
      TF("TODAS LAS PLANTAS NACEN DE SEMILLAS.", "FALSO", "ALGUNAS NACEN DE GAJOS.", n="error")],
"4": [ORD("ORDENÁ LOS PASOS DEL SEMILLERO.", ["RIEGO", "PONGO TIERRA", "PONGO LA SEMILLA"], ["PONGO TIERRA", "PONGO LA SEMILLA", "RIEGO"], "TIERRA, SEMILLA, AGUA.", n="analizar"),
      MC("¿DÓNDE DEJO EL SEMILLERO?", ["CON LUZ", "EN UN CAJÓN OSCURO"], "CON LUZ", "LA PLANTA NECESITA LUZ.", n="aplicar")],
"5": [MC("RELÁMPAGO. EL FRUTO SALE DE…", ["LA FLOR", "LA RAÍZ"], "LA FLOR", "LA FLOR SE CONVIERTE EN FRUTO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL PANADERO VIAJA CON…", ["EL VIENTO", "EL AGUA"], "EL VIENTO", "ES LIVIANO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA PAPA VIEJA ECHA…", ["BROTES", "FLORES DE PAPEL"], "BROTES", "Y CRECE OTRA PLANTA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL SEMILLERO SE RIEGA…", ["UN POCO", "MUCHÍSIMO"], "UN POCO", "TIERRA HÚMEDA.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ GUARDA EL FRUTO ADENTRO?", ["SEMILLAS", "PIEDRAS", "HOJAS"], "SEMILLAS", "LAS SEMILLAS VAN ADENTRO.", n="recordar")],
 [1, ORD("ORDENÁ.", ["FRUTO", "FLOR"], ["FLOR", "FRUTO"], "PRIMERO LA FLOR.", n="analizar")],
 [1, TF("LA MANZANA ES UN FRUTO.", "VERDADERO", "TIENE SEMILLAS.", n="aplicar")],
 [2, MC("¿CÓMO VIAJA UNA SEMILLA CON PINCHES?", ["PEGADA A LOS ANIMALES", "CON EL AGUA"], "PEGADA A LOS ANIMALES", "SE ENGANCHA EN EL PELO.", n="analizar")],
 [2, SA("¿CON QUÉ VIAJA EL PANADERO?", low("VIENTO") + low("EL VIENTO") + low("CON EL VIENTO"), "CON EL VIENTO.", n="recordar")],
 [2, TF("TODAS LAS SEMILLAS VIAJAN IGUAL.", "FALSO", "VIAJAN CON VIENTO, ANIMALES O AGUA.", n="error")],
 [3, MC("¿QUÉ LE SALE A UN GAJO EN AGUA?", ["RAÍCES", "FRUTOS"], "RAÍCES", "DESPUÉS SE PLANTA.", n="aplicar")],
 [3, SA("NOMBRÁ ALGO QUE NACE SIN SEMILLAS.", low("PAPA") + low("BATATA") + low("GAJO") + low("UN GAJO") + low("LA PAPA"), "POR EJEMPLO: LA PAPA.", n="aplicar")],
 [3, TF("UNA PLANTA NUEVA PUEDE NACER DE UN GAJO.", "VERDADERO", "SIN SEMILLAS.", n="recordar")],
 [4, ORD("ORDENÁ LOS PASOS.", ["RIEGO", "HAGO UN POZITO", "PONGO LAS SEMILLAS"], ["HAGO UN POZITO", "PONGO LAS SEMILLAS", "RIEGO"], "POZITO, SEMILLAS, AGUA.", n="analizar")],
 [4, MC("¿QUÉ HACE UN CIENTÍFICO CON SU SEMILLERO?", ["OBSERVA Y ANOTA", "LO TIRA"], "OBSERVA Y ANOTA", "CADA DÍA.", n="aplicar")],
 [4, TF("HAY QUE INUNDAR EL SEMILLERO CON MUCHA AGUA.", "FALSO", "SOLO UN POCO.", n="error")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: de la flor al fruto", "examen_titulo": "Nivel jefe: de la flor al fruto",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
