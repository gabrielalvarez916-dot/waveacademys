# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 5 · Calentar y enfriar. Genera mision-5.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (hoy en la cocina, siempre con un adulto).
Niveles: 1 qué pasa al calentar · 2 derretir y solidificar · 3 evaporar y condensar · 4 qué cambia al cocinar."""
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
"objetivo": "Vas a ver qué pasa cuando algo se calienta.",
"vas_a_ver": ["Calentar", "El termómetro", "Cuidado con el calor"],
"secciones": [
 S(1, "Calentar", [
  P("Tomi deja un chocolate al <b>sol</b>. ¡Se pone blandito!"),
  D("Calentar", "Darle <b>calor</b> a algo. Puede cambiar cómo es."),
  IMG("Con calor", "Algunas cosas cambian.", FG.tiras(["CHOCOLATE AL SOL: SE ABLANDA", "MANTECA EN LA SARTÉN: SE DERRITE", "AGUA EN LA OLLA: HIERVE"], numeros=False, cols=1)),
 ]),
 S(1, "El termómetro", [
  D("Termómetro", "Mide si algo está <b>frío</b> o <b>caliente</b>."),
  P("Mucho calor: número <b>alto</b>. Frío: número <b>bajo</b>."),
  IMG("Frío y caliente", "Para comparar.", FG.nombres(["HELADO: FRÍO", "SOPA: CALIENTE"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cosas. Las vas a usar en la carpeta."),
  IMG("¿Frío o caliente?", "Pensá en cada una.", FG.nombres(["HIELO", "TÉ RECIÉN HECHO", "AGUA DE LA HELADERA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La manteca", "planteo": "¿Qué pasa con la manteca en la sartén?", "pasos": ["La sartén está caliente.", "La manteca recibe calor.", "Se derrite."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El termómetro mide…", "pasos": ["Si algo está frío o ___ ."]},
"ejemplo_solo": {"titulo": "Observá", "planteo": "Con un adulto, mirá qué pasa con un cubito al sol."},
"tip": {"titulo": "Siempre con un adulto", "texto": "Las cosas calientes queman."},
"ojo": ["Nunca toques la olla caliente.", "La cocina, siempre con un adulto."],
"resumen": [{"titulo": "Calentar", "texto": "Dar calor."}, {"titulo": "Cambia", "texto": "Se ablanda, se derrite."}, {"titulo": "Termómetro", "texto": "Mide frío y calor."}],
"glosario": [{"palabra": "Termómetro", "significado": "Mide frío y calor."}, {"palabra": "Hervir", "significado": "Cuando el agua burbujea por el calor."}],
"carpeta": ["¿Qué cosa del dibujo está más caliente?", "¿Qué cosa está más fría?", "Tomi quiere tocar la olla con agua hirviendo. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("TÉ RECIÉN HECHO") + low("te recien hecho") + low("EL TÉ") + low("TÉ") + low("te"), low("HIELO") + low("EL HIELO"), NO],
"soluciones": {"incompleto": "CALIENTE.", "solo": "Lo que pasó con el cubito.", "carpeta": ["El té recién hecho.", "El hielo.", "No: quema. Siempre con un adulto."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver cómo se derrite y se congela el agua.",
"vas_a_ver": ["Derretir", "Solidificar", "Ida y vuelta"],
"secciones": [
 S(1, "Derretir", [
  D("Derretir", "Con <b>calor</b>, lo sólido se hace <b>líquido</b>: el hielo se hace agua."),
  IMG("El hielo se derrite", "Con calor.", FG.tiras(["HIELO (SÓLIDO)", "+ CALOR", "AGUA (LÍQUIDO)"], numeros=False, cols=3)),
 ]),
 S(1, "Solidificar", [
  D("Solidificar", "Con <b>frío</b>, lo líquido se hace <b>sólido</b>: el agua se hace hielo."),
  P("Si ponemos agua en el congelador, ¡se hace hielo!"),
  IMG("El agua se congela", "Con frío.", FG.tiras(["AGUA (LÍQUIDO)", "+ FRÍO", "HIELO (SÓLIDO)"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Qué pasó?", "Pensá si hubo calor o frío.", FG.tiras(["1. EL HELADO SE HIZO LÍQUIDO", "2. EL JUGO SE HIZO HIELO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El helado", "planteo": "¿Por qué el helado se derrite?", "pasos": ["Hace calor.", "El helado recibe calor.", "Se hace líquido."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El agua en el congelador…", "pasos": ["…se hace ___ ."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Con un adulto, poné jugo en el congelador. Miralo mañana."},
"tip": {"titulo": "Calor o frío", "texto": "Calor derrite. Frío solidifica."},
"ojo": ["El hielo derretido vuelve a ser agua.", "Ese agua se puede volver a congelar."],
"resumen": [{"titulo": "Derretir", "texto": "Con calor: sólido a líquido."}, {"titulo": "Solidificar", "texto": "Con frío: líquido a sólido."}, {"titulo": "Ida y vuelta", "texto": "Se puede repetir."}],
"glosario": [{"palabra": "Sólido", "significado": "Tiene forma propia, como el hielo."}, {"palabra": "Líquido", "significado": "Se derrama, como el agua."}],
"carpeta": ["En la tarjeta 1, ¿hubo calor o frío?", "En la tarjeta 2, ¿hubo calor o frío?", "Tomi dice que el hielo derretido no se congela más. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("CALOR"), low("FRÍO") + low("frio"), NO],
"soluciones": {"incompleto": "HIELO.", "solo": "Lo que pasó con el jugo.", "carpeta": ["Calor.", "Frío.", "No: se puede congelar otra vez."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver cómo el agua se evapora y se condensa.",
"vas_a_ver": ["Evaporar", "Condensar", "El vapor"],
"secciones": [
 S(1, "Evaporar", [
  D("Evaporar", "Con mucho <b>calor</b>, el agua se hace <b>vapor</b> y sube."),
  P("Cuando el agua de la olla hierve, sale <b>vapor</b>."),
  IMG("El agua se evapora", "Con calor.", FG.tiras(["AGUA (LÍQUIDO)", "+ MUCHO CALOR", "VAPOR (GAS)"], numeros=False, cols=3)),
 ]),
 S(1, "Condensar", [
  D("Condensar", "Cuando el <b>vapor</b> toca algo <b>frío</b>, se hace <b>gotitas</b>."),
  P("Las gotitas en la tapa de la olla son vapor condensado."),
  IMG("El vapor se condensa", "En la tapa fría.", FG.tiras(["VAPOR (GAS)", "+ FRÍO", "GOTITAS (LÍQUIDO)"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Evapora o condensa?", "Pensá en cada una.", FG.tiras(["1. EL ESPEJO DEL BAÑO SE EMPAÑA", "2. EL CHARCO DESAPARECE AL SOL"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La tapa", "planteo": "¿Por qué la tapa tiene gotitas?", "pasos": ["El agua hierve y sale vapor.", "El vapor toca la tapa.", "Se hace gotitas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El charco al sol…", "pasos": ["…se ___ ."]},
"ejemplo_solo": {"titulo": "Observá", "planteo": "Después de bañarte, mirá el espejo. ¿Qué tiene?"},
"tip": {"titulo": "Calor y frío", "texto": "Calor evapora. Frío condensa."},
"ojo": ["El vapor quema: no lo toques.", "El agua no desaparece: se hace vapor."],
"resumen": [{"titulo": "Evaporar", "texto": "Agua a vapor."}, {"titulo": "Condensar", "texto": "Vapor a gotitas."}, {"titulo": "Vapor", "texto": "Agua que no vemos."}],
"glosario": [{"palabra": "Vapor", "significado": "Agua en forma de gas."}, {"palabra": "Empañar", "significado": "Cubrir de gotitas."}],
"carpeta": ["¿La tarjeta 1 es evaporar o condensar?", "¿La tarjeta 2 es evaporar o condensar?", "Tomi dice que el agua del charco desaparece para siempre. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("CONDENSAR") + low("CONDENSA") + low("SE CONDENSA"), low("EVAPORAR") + low("EVAPORA") + low("SE EVAPORA"), NO],
"soluciones": {"incompleto": "EVAPORA.", "solo": "Gotitas: vapor condensado.", "carpeta": ["Condensar.", "Evaporar.", "No: se hace vapor."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver qué cambia en la comida al cocinarla.",
"vas_a_ver": ["Crudo y cocido", "Cambios que no vuelven", "Cocinar con cuidado"],
"secciones": [
 S(1, "Crudo y cocido", [
  P("El <b>huevo crudo</b> es líquido. Al cocinarlo, se pone <b>duro</b>."),
  P("El <b>pan</b> se hace <b>tostada</b>. La papa cruda es dura y cocida es <b>blanda</b>."),
  IMG("Al cocinar", "La comida cambia.", FG.tiras(["HUEVO: LÍQUIDO → DURO", "PAN → TOSTADA", "PAPA: DURA → BLANDA"], numeros=False, cols=1)),
 ]),
 S(1, "No vuelve atrás", [
  P("El hielo puede volver a ser agua. Pero el huevo cocido <b>no vuelve</b> a ser crudo."),
  IMG("Ida y vuelta o solo ida", "Comparamos.", FG.tiras(["HIELO ↔ AGUA: VUELVE", "HUEVO CRUDO → COCIDO: NO VUELVE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Vuelve o no?", "Pensá en cada una.", FG.nombres(["TOSTADA", "HIELO", "HUEVO DURO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El huevo", "planteo": "¿Qué le pasa al huevo al hervirlo?", "pasos": ["Estaba líquido.", "Recibe calor.", "Se pone duro y no vuelve."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El pan en la tostadora…", "pasos": ["…se hace ___ ."]},
"ejemplo_solo": {"titulo": "En la cocina", "planteo": "Con un adulto, mirá cómo cambia un alimento al cocinarlo."},
"tip": {"titulo": "Comparar", "texto": "Mirá el alimento antes y después."},
"ojo": ["Cocinar, siempre con un adulto.", "La tostada no vuelve a ser pan."],
"resumen": [{"titulo": "Crudo", "texto": "Antes de cocinar."}, {"titulo": "Cocido", "texto": "Después del calor."}, {"titulo": "No vuelve", "texto": "Huevo, tostada."}],
"glosario": [{"palabra": "Crudo", "significado": "Sin cocinar."}, {"palabra": "Cocido", "significado": "Cocinado con calor."}],
"carpeta": ["¿Qué tarjeta del dibujo SÍ puede volver atrás?", "¿La tostada puede volver a ser pan?", "Tomi dice que el huevo duro, frío, vuelve a ser crudo. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [low("HIELO") + low("EL HIELO"), NO, NO],
"soluciones": {"incompleto": "TOSTADA.", "solo": "El cambio que viste.", "carpeta": ["El hielo.", "No.", "No: el huevo cocido no vuelve."]},
}

ACT = {
"1": [MC("¿QUÉ LE PASA A LA MANTECA EN LA SARTÉN CALIENTE?", ["SE DERRITE", "SE CONGELA"], "SE DERRITE", "RECIBE CALOR.", n="aplicar"),
      TF("EL TERMÓMETRO MIDE SI ALGO ESTÁ FRÍO O CALIENTE.", "VERDADERO", "MIDE LA TEMPERATURA.", n="recordar")],
"2": [UNI("UNÍ CADA CAMBIO CON LO QUE LO CAUSA.", [("HIELO A AGUA", "CALOR"), ("AGUA A HIELO", "FRÍO")], "CALOR DERRITE, FRÍO SOLIDIFICA.", n="analizar"),
      SA("EL AGUA EN EL CONGELADOR SE HACE…", low("HIELO"), "HIELO.", n="aplicar")],
"3": [MC("¿QUÉ SALE CUANDO EL AGUA HIERVE?", ["VAPOR", "HIELO"], "VAPOR", "EL AGUA SE EVAPORA.", n="recordar"),
      MC("¿POR QUÉ SE EMPAÑA EL ESPEJO DEL BAÑO?", ["EL VAPOR SE CONDENSA", "SE ROMPE"], "EL VAPOR SE CONDENSA", "SE HACEN GOTITAS.", n="analizar")],
"4": [MC("¿QUÉ CAMBIO NO VUELVE ATRÁS?", ["COCINAR UN HUEVO", "DERRETIR HIELO"], "COCINAR UN HUEVO", "EL HUEVO COCIDO NO VUELVE A SER CRUDO.", n="analizar"),
      TF("LA TOSTADA PUEDE VOLVER A SER PAN.", "FALSO", "ES UN CAMBIO QUE NO VUELVE.", n="error")],
"5": [MC("RELÁMPAGO. EL HIELO CON CALOR…", ["SE DERRITE", "CRECE"], "SE DERRITE", "SE HACE AGUA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL VAPOR EN LA TAPA FRÍA…", ["SE CONDENSA", "SE QUEMA"], "SE CONDENSA", "SE HACE GOTITAS.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL CHARCO AL SOL…", ["SE EVAPORA", "SE CONGELA"], "SE EVAPORA", "SE HACE VAPOR.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LA COCINA, SIEMPRE CON…", ["UN ADULTO", "NADIE"], "UN ADULTO", "LAS COSAS CALIENTES QUEMAN.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿QUÉ INSTRUMENTO MIDE FRÍO Y CALOR?", ["EL TERMÓMETRO", "LA REGLA"], "EL TERMÓMETRO", "MIDE LA TEMPERATURA.", n="recordar")],
 [1, TF("SE PUEDE TOCAR LA OLLA CALIENTE.", "FALSO", "QUEMA.", n="error")],
 [1, SA("¿QUÉ LE PASA AL CHOCOLATE AL SOL?", low("SE DERRITE") + low("SE ABLANDA") + low("SE PONE BLANDO") + low("SE HACE LÍQUIDO"), "SE ABLANDA Y SE DERRITE.", n="aplicar")],
 [2, ORD("ORDENÁ: DEL HIELO AL AGUA.", ["AGUA", "HIELO", "CALOR"], ["HIELO", "CALOR", "AGUA"], "CON CALOR SE DERRITE.", n="analizar")],
 [2, MC("¿QUÉ HACE QUE EL AGUA SE HAGA HIELO?", ["EL FRÍO", "EL CALOR"], "EL FRÍO", "SE SOLIDIFICA.", n="aplicar")],
 [2, TF("EL AGUA DE UN HIELO DERRETIDO SE PUEDE VOLVER A CONGELAR.", "VERDADERO", "ES IDA Y VUELTA.", n="analizar")],
 [3, MC("¿QUÉ ES EL VAPOR?", ["AGUA EN FORMA DE GAS", "HIELO MOLIDO"], "AGUA EN FORMA DE GAS", "SALE AL HERVIR.", n="recordar")],
 [3, SA("LAS GOTITAS EN LA TAPA DE LA OLLA SON VAPOR QUE SE…", low("CONDENSÓ") + low("condenso") + low("CONDENSA") + low("CONDENSAR"), "CONDENSÓ.", n="aplicar")],
 [3, TF("EL AGUA DEL CHARCO DESAPARECE PARA SIEMPRE.", "FALSO", "SE HACE VAPOR.", n="error")],
 [4, MC("¿CÓMO ES EL HUEVO CRUDO?", ["LÍQUIDO", "DURO"], "LÍQUIDO", "AL COCINARLO SE PONE DURO.", n="recordar")],
 [4, UNI("UNÍ CADA ALIMENTO CON SU CAMBIO.", [("PAN", "TOSTADA"), ("HUEVO", "DURO"), ("PAPA", "BLANDA")], "AL COCINAR CAMBIAN.", n="analizar")],
 [4, TF("EL HUEVO DURO VUELVE A SER CRUDO SI SE ENFRÍA.", "FALSO", "NO VUELVE ATRÁS.", n="error")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: calentar y enfriar", "examen_titulo": "Nivel jefe: calentar y enfriar",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
