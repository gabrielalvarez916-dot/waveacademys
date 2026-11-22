# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 2 · Animales por fuera. Genera mision-2.json.
Regla de primeros años. Metáfora: el zoológico de Sofi (cada animal con su ropa, su forma de moverse y su comida).
Niveles: 1 cubiertos de pelos, plumas o escamas · 2 cómo se desplazan · 3 de qué se alimentan · 4 agrupo animales por sus rasgos."""
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
"objetivo": "Vas a ver de qué está cubierto el cuerpo de los animales.",
"vas_a_ver": ["Pelos", "Plumas", "Escamas"],
"secciones": [
 S(1, "La ropa de los animales", [
  P("Los animales tienen el cuerpo cubierto: con <b>pelos</b>, <b>plumas</b> o <b>escamas</b>."),
  IMG("Cubiertos", "Cada uno con lo suyo.", FG.tiras(["PERRO: PELOS", "LORO: PLUMAS", "PEZ: ESCAMAS"], numeros=False, cols=3)),
 ]),
 S(1, "Para qué sirven", [
  D("Cubierta", "Lo que tapa el cuerpo del animal y lo protege."),
  P("Los pelos dan calor. Las plumas ayudan a volar. Las escamas protegen en el agua."),
  IMG("Sirven para", "Protegen.", FG.tiras(["PELOS: CALOR", "PLUMAS: VOLAR", "ESCAMAS: PROTEGER"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("Animales", "¿Pelos, plumas o escamas?", FG.nombres(["GATO", "GALLINA", "VÍBORA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El gato", "planteo": "¿De qué está cubierto?", "pasos": ["Lo miro y lo toco.", "Es suave.", "Tiene pelos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El loro tiene…", "pasos": ["El loro está cubierto de ___."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá un animal en tu casa o en un libro. ¿De qué está cubierto?"},
"tip": {"titulo": "Mirá la piel", "texto": "Mirá de cerca: ¿pelos, plumas o escamas?"},
"ojo": ["La víbora tiene escamas, aunque no viva en el agua.", "Solo las aves tienen plumas."],
"resumen": [{"titulo": "Pelos", "texto": "Perro, gato."}, {"titulo": "Plumas", "texto": "Aves."}, {"titulo": "Escamas", "texto": "Peces, víboras."}],
"glosario": [{"palabra": "Escama", "significado": "Plaquita dura que cubre a peces y víboras."}, {"palabra": "Ave", "significado": "Animal con plumas."}],
"carpeta": ["¿De qué está cubierto el gato?", "¿De qué está cubierta la gallina?", "¿De qué está cubierta la víbora?"],
"respuestas_carpeta": [acepta("PELOS", "DE PELOS", "PELO"), acepta("PLUMAS", "DE PLUMAS", "PLUMA"), acepta("ESCAMAS", "DE ESCAMAS", "ESCAMA")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "PLUMAS.", "solo": "Depende del animal.", "carpeta": ["PELOS.", "PLUMAS.", "ESCAMAS."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver cómo se mueven los animales.",
"vas_a_ver": ["Caminar y saltar", "Volar y nadar", "Reptar"],
"secciones": [
 S(1, "Se mueven distinto", [
  P("Unos <b>caminan</b>, otros <b>vuelan</b>, otros <b>nadan</b>."),
  IMG("Cómo se mueven", "Cada uno a su manera.", FG.tiras(["PERRO: CAMINA", "PÁJARO: VUELA", "PEZ: NADA", "RANA: SALTA"], numeros=False, cols=2)),
 ]),
 S(1, "Reptar", [
  D("Reptar", "Moverse arrastrando el cuerpo por el suelo."),
  P("La víbora y el gusano reptan."),
  IMG("Reptan", "Sin patas.", FG.nombres(["VÍBORA", "GUSANO"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("Animales", "¿Cómo se mueven?", FG.nombres(["PALOMA", "CABALLO", "DELFÍN"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El pato", "planteo": "¿Cómo se mueve?", "pasos": ["Camina con sus patas.", "Nada en la laguna.", "¡Y también vuela!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El pez…", "pasos": ["El pez se mueve ___."]},
"ejemplo_solo": {"titulo": "Imitá", "planteo": "Moverte como una rana: ¡saltá!"},
"tip": {"titulo": "Mirá las patas", "texto": "Las patas, alas y aletas te dan la pista."},
"ojo": ["Algunos animales se mueven de varias formas: el pato.", "Las víboras no tienen patas."],
"resumen": [{"titulo": "Caminar", "texto": "Con patas."}, {"titulo": "Volar y nadar", "texto": "Con alas o aletas."}, {"titulo": "Reptar", "texto": "Arrastrándose."}],
"glosario": [{"palabra": "Aleta", "significado": "Parte del pez para nadar."}, {"palabra": "Desplazarse", "significado": "Ir de un lugar a otro."}],
"carpeta": ["¿Cómo se mueve la paloma?", "¿Cómo se mueve el caballo?", "¿Cómo se mueve el delfín?"],
"respuestas_carpeta": [acepta("VUELA", "VOLANDO", "VOLAR", "CAMINA Y VUELA"), acepta("CAMINA", "CORRE", "CAMINANDO", "CORRIENDO", "CAMINAR", "CORRER"), acepta("NADA", "NADANDO", "NADAR")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "NADANDO.", "solo": "Saltaste como una rana.", "carpeta": ["VUELA.", "CAMINA.", "NADA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver qué comen los animales.",
"vas_a_ver": ["Comen plantas", "Comen otros animales", "Comen de todo"],
"secciones": [
 S(1, "Comen plantas", [
  P("La vaca y el conejo comen <b>plantas</b>: pasto, hojas, zanahorias."),
  IMG("Comen plantas", "Pasto y hojas.", FG.tiras(["VACA: PASTO", "CONEJO: ZANAHORIA"], numeros=False, cols=2)),
 ]),
 S(1, "Comen animales", [
  D("Comen carne", "Son los animales que comen otros animales."),
  P("El león y el tiburón comen <b>otros animales</b>. La gallina come <b>de todo</b>."),
  IMG("Qué comen", "Carne o de todo.", FG.tiras(["LEÓN: CARNE", "TIBURÓN: PECES", "GALLINA: DE TODO"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("Animales", "¿Qué comen?", FG.nombres(["CABALLO", "TIGRE", "OSO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El conejo", "planteo": "¿Qué come?", "pasos": ["Come pasto.", "Come zanahorias.", "Come plantas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El león come…", "pasos": ["El león come ___."]},
"ejemplo_solo": {"titulo": "Tu mascota", "planteo": "Preguntá en tu casa qué come una mascota."},
"tip": {"titulo": "Mirá los dientes", "texto": "Dientes filosos: come carne. Dientes chatos: come plantas."},
"ojo": ["Algunos comen de todo: el oso.", "No todos los animales grandes comen carne: la vaca."],
"resumen": [{"titulo": "Plantas", "texto": "Vaca, conejo."}, {"titulo": "Animales", "texto": "León, tiburón."}, {"titulo": "De todo", "texto": "Gallina, oso."}],
"glosario": [{"palabra": "Filoso", "significado": "Que corta."}, {"palabra": "Alimento", "significado": "Lo que se come."}],
"carpeta": ["¿Qué come el caballo?", "¿Qué come el tigre?", "Tomi dice que el oso solo come carne. ¿Está bien?"],
"respuestas_carpeta": [acepta("PASTO", "PLANTAS", "PASTO Y PLANTAS"), acepta("CARNE", "ANIMALES", "OTROS ANIMALES"), acepta("NO", "NO, COME DE TODO", "NO COME DE TODO")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "OTROS ANIMALES.", "solo": "Depende de la mascota.", "carpeta": ["PASTO.", "CARNE.", "NO: COME DE TODO."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a agrupar animales por cómo son.",
"vas_a_ver": ["Mirar rasgos", "Armar grupos", "Uno en dos grupos"],
"secciones": [
 S(1, "Los rasgos", [
  P("Un <b>rasgo</b> es algo que vemos: si tiene plumas, si vuela, si nada."),
  IMG("Rasgos", "Lo que vemos.", FG.tiras(["CUBIERTA", "CÓMO SE MUEVE", "QUÉ COME"], numeros=False, cols=3)),
 ]),
 S(1, "Armar grupos", [
  D("Agrupar", "Juntar los que se parecen en algo."),
  P("Con plumas: <b>LORO, GALLINA, PATO</b>. Con pelos: <b>PERRO, GATO, VACA</b>."),
  IMG("Dos grupos", "Plumas y pelos.", FG.tiras(["PLUMAS: LORO, GALLINA, PATO", "PELOS: PERRO, GATO, VACA"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("Animales", "Agrupalos.", FG.nombres(["PEZ", "PALOMA", "TIBURÓN", "PATO"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Los que nadan", "planteo": "Agrupo por cómo se mueven.", "pasos": ["El pez nada.", "El delfín nada.", "Grupo: los que nadan."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿Qué grupo?", "pasos": ["El loro va con los de ___."]},
"ejemplo_solo": {"titulo": "Tus grupos", "planteo": "Elegí 4 animales y armá 2 grupos."},
"tip": {"titulo": "Elegí un rasgo", "texto": "Primero elegí qué mirar. Después agrupá."},
"ojo": ["Un animal puede estar en dos grupos: el pato nada y vuela.", "Agrupá por un rasgo a la vez."],
"resumen": [{"titulo": "Rasgo", "texto": "Algo que vemos."}, {"titulo": "Grupo", "texto": "Los que se parecen."}, {"titulo": "Dos grupos", "texto": "Puede pasar."}],
"glosario": [{"palabra": "Rasgo", "significado": "Algo que tiene un animal y se ve."}, {"palabra": "Grupo", "significado": "Varios juntos."}],
"carpeta": ["¿Qué animales tienen escamas?", "¿Qué animales tienen plumas?", "¿Cuál nada y también vuela?"],
"respuestas_carpeta": [acepta("PEZ Y TIBURÓN", "PEZ Y TIBURON", "EL PEZ Y EL TIBURÓN", "TIBURÓN Y PEZ"), acepta("PALOMA Y PATO", "PATO Y PALOMA", "LA PALOMA Y EL PATO"), acepta("PATO", "EL PATO")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "PLUMAS.", "solo": "Por ejemplo: con pelos y con plumas.", "carpeta": ["PEZ Y TIBURÓN.", "PALOMA Y PATO.", "EL PATO."]},
}

ACT = {
"1": [MC("¿DE QUÉ ESTÁ CUBIERTO EL PERRO?", ["PELOS", "PLUMAS", "ESCAMAS"], "PELOS", "EL PERRO TIENE PELOS.", n="recordar"),
      MC("TOMI DICE QUE EL PEZ TIENE PLUMAS. ¿QUÉ TIENE EN REALIDAD?", ["ESCAMAS", "PELOS", "NADA"], "ESCAMAS", "LOS PECES TIENEN ESCAMAS.", n="error")],
"2": [MC("¿CÓMO SE MUEVE LA VÍBORA?", ["REPTA", "VUELA", "SALTA"], "REPTA", "SE ARRASTRA.", n="recordar"),
      MC("UN ANIMAL TIENE ALETAS. ¿CÓMO SE MUEVE?", ["NADA", "VUELA", "REPTA"], "NADA", "LAS ALETAS SIRVEN PARA NADAR.", n="analizar")],
"3": [MC("¿QUÉ COME LA VACA?", ["PASTO", "CARNE", "PECES"], "PASTO", "COME PLANTAS.", n="recordar"),
      MC("UN ANIMAL TIENE DIENTES MUY FILOSOS. ¿QUÉ COME?", ["CARNE", "PASTO", "HOJAS"], "CARNE", "LOS DIENTES FILOSOS CORTAN CARNE.", n="analizar")],
"4": [SA("¿CUÁL VA CON LOS DE PLUMAS? GATO · LORO · PEZ", acepta("LORO", "EL LORO"), "EL LORO TIENE PLUMAS.", n="aplicar"),
      MC("¿QUÉ TIENEN EN COMÚN EL PATO Y LA PALOMA?", ["TIENEN PLUMAS", "TIENEN ESCAMAS", "REPTAN"], "TIENEN PLUMAS", "LOS DOS SON AVES.", n="analizar")],
"5": [MC("RELÁMPAGO. ¿QUIÉN TIENE PLUMAS?", ["GALLINA", "GATO", "PEZ"], "GALLINA", "ES UN AVE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUIÉN VUELA?", ["PALOMA", "CABALLO", "VÍBORA"], "PALOMA", "TIENE ALAS.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUIÉN COME CARNE?", ["LEÓN", "CONEJO", "VACA"], "LEÓN", "COME OTROS ANIMALES.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿CÓMO SE MUEVE EL PEZ?", acepta("NADA", "NADANDO"), "NADA.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿DE QUÉ ESTÁ CUBIERTO EL LORO?", ["PLUMAS", "PELOS", "ESCAMAS"], "PLUMAS", "ES UN AVE.", n="recordar")],
 [1, SA("¿DE QUÉ ESTÁ CUBIERTA LA VÍBORA?", acepta("ESCAMAS", "DE ESCAMAS"), "ESCAMAS.", n="aplicar")],
 [1, MC("¿PARA QUÉ LE SIRVEN LOS PELOS AL OSO?", ["PARA TENER CALOR", "PARA NADAR", "PARA VOLAR"], "PARA TENER CALOR", "LOS PELOS ABRIGAN.", n="analizar")],
 [2, MC("¿CÓMO SE MUEVE EL CABALLO?", ["CAMINA Y CORRE", "VUELA", "REPTA"], "CAMINA Y CORRE", "TIENE 4 PATAS.", n="recordar")],
 [2, MC("SOFI DICE QUE EL PATO SOLO CAMINA. ¿QUÉ LE FALTÓ?", ["TAMBIÉN NADA Y VUELA", "TAMBIÉN REPTA", "NADA, ESTÁ BIEN"], "TAMBIÉN NADA Y VUELA", "EL PATO SE MUEVE DE VARIAS FORMAS.", n="error")],
 [2, SA("¿CÓMO SE MUEVE LA RANA?", acepta("SALTA", "SALTANDO", "SALTA Y NADA", "NADA Y SALTA"), "SALTA.", n="aplicar")],
 [3, MC("¿QUÉ COME EL CONEJO?", ["PLANTAS", "CARNE", "PECES"], "PLANTAS", "PASTO Y ZANAHORIAS.", n="recordar")],
 [3, MC("¿QUIÉN COME DE TODO?", ["LA GALLINA", "LA VACA", "EL LEÓN"], "LA GALLINA", "COME SEMILLAS Y BICHITOS.", n="recordar")],
 [3, SA("¿QUÉ COME EL LEÓN?", acepta("CARNE", "ANIMALES", "OTROS ANIMALES"), "OTROS ANIMALES.", n="aplicar")],
 [4, MC("¿QUÉ GRUPO TIENE PELOS?", ["PERRO, GATO, VACA", "LORO, PATO, GALLINA", "PEZ, VÍBORA, TIBURÓN"], "PERRO, GATO, VACA", "LOS TRES TIENEN PELOS.", n="aplicar")],
 [4, ORD("ORDENÁ ASÍ: VUELA, NADA, REPTA.", ["VÍBORA", "PEZ", "PALOMA"], ["PALOMA", "PEZ", "VÍBORA"], "PALOMA VUELA, PEZ NADA, VÍBORA REPTA.", n="aplicar")],
 [4, MC("¿CUÁL NO VA EN EL GRUPO? LORO · GALLINA · GATO", ["GATO", "LORO", "GALLINA"], "GATO", "EL GATO NO TIENE PLUMAS.", n="analizar")],
 [4, MC("¿QUÉ ES UN RASGO?", ["ALGO QUE VEMOS DEL ANIMAL", "EL NOMBRE DEL ANIMAL", "LA CASA DEL ANIMAL"], "ALGO QUE VEMOS DEL ANIMAL", "PLUMAS, PATAS, ALETAS.", n="recordar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 2, "estilo": "primeros",
     "practica": "Práctica general: animales por fuera", "examen_titulo": "Nivel jefe: animales por fuera",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
