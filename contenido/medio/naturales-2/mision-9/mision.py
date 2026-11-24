# -*- coding: utf-8 -*-
"""Ciencias Naturales 2 (Nivel Medio, 2.º año) · Misión 9 · El suelo y las rocas. Genera mision-9.json.
Regla de primeros años. Metáfora del año: Tomi, científico explorador (hoy cava en la huerta con su lupa).
Niveles: 1 qué tiene el suelo · 2 rocas de distintos tipos · 3 seres vivos del suelo · 4 suelos para sembrar."""
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
"objetivo": "Vas a ver qué tiene el suelo.",
"vas_a_ver": ["Piedritas y arena", "Restos de hojas", "Agua y aire"],
"secciones": [
 S(1, "El suelo", [
  D("Suelo", "La capa de <b>tierra</b> que pisamos, donde crecen las plantas."),
  P("Tomi junta un poco de tierra y la mira con la <b>lupa</b>."),
  IMG("Lo que tiene el suelo", "Mirado con lupa.", FG.tiras(["PIEDRITAS", "ARENA", "RESTOS DE HOJAS", "AGUA Y AIRE"], numeros=False)),
 ]),
 S(1, "Un experimento", [
  P("Pone tierra y agua en un frasco, y lo deja quieto."),
  P("Abajo quedan las <b>piedritas</b>. Arriba flotan las <b>hojitas</b>."),
  IMG("El frasco", "Se separa en capas.", FG.tiras(["ARRIBA: HOJITAS", "EN EL MEDIO: TIERRA FINA", "ABAJO: PIEDRITAS"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el frasco de Tomi. Lo vas a usar en la carpeta."),
  IMG("¿Dónde quedó?", "Pensá en el peso.", FG.tiras(["ARRIBA: HOJITAS", "ABAJO: PIEDRITAS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Con la lupa", "planteo": "¿Qué vio Tomi en la tierra?", "pasos": ["Piedritas y arena.", "Pedacitos de hojas.", "¡Y un poco de agua!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En el frasco, abajo quedan…", "pasos": ["…las ___ ."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Con un adulto, hacé el frasco con tierra y agua."},
"tip": {"titulo": "Esperá", "texto": "El frasco necesita quedarse quieto un rato."},
"ojo": ["Lavate las manos después de tocar tierra.", "El suelo tiene muchas cosas mezcladas."],
"resumen": [{"titulo": "Suelo", "texto": "Tierra que pisamos."}, {"titulo": "Tiene", "texto": "Piedritas, hojas, agua, aire."}, {"titulo": "Frasco", "texto": "Se separa en capas."}],
"glosario": [{"palabra": "Lupa", "significado": "Vidrio que agranda lo que miramos."}, {"palabra": "Capa", "significado": "Una parte encima de otra."}],
"carpeta": ["En el frasco, ¿qué quedó arriba?", "¿Qué quedó abajo?", "Tomi dice que el suelo es solo tierra, sin nada más. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("HOJITAS") + low("LAS HOJITAS") + low("HOJAS") + low("LAS HOJAS"), low("PIEDRITAS") + low("LAS PIEDRITAS") + low("PIEDRAS"), NO],
"soluciones": {"incompleto": "PIEDRITAS.", "solo": "Cómo quedó tu frasco.", "carpeta": ["Las hojitas.", "Las piedritas.", "No: tiene piedritas, hojas, agua y aire."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer distintas rocas.",
"vas_a_ver": ["Rocas duras", "Rocas blandas", "Piedras del río"],
"secciones": [
 S(1, "Las rocas", [
  P("Las <b>rocas</b> son pedazos duros de la tierra. Las chiquitas son <b>piedras</b>."),
  P("Algunas son muy <b>duras</b>, como el granito. Otras son <b>blandas</b>, como la tiza."),
  IMG("Duras y blandas", "Comparamos.", FG.tiras(["GRANITO: MUY DURO", "TIZA: BLANDA, SE RAYA"], numeros=False, cols=1)),
 ]),
 S(1, "Piedras del río", [
  P("Las piedras del río son <b>redondas</b> y lisas: el agua las fue gastando."),
  IMG("Rocas distintas", "Cada una es diferente.", FG.nombres(["GRANITO", "TIZA", "CANTO RODADO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué roca es?", "Pensá en cada pista.", FG.tiras(["1. ES BLANDA Y SE USA EN EL PIZARRÓN", "2. ES REDONDA Y VIENE DEL RÍO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "¿Dura o blanda?", "planteo": "¿Cómo sé si una roca es blanda?", "pasos": ["La rayo con una moneda.", "Si se marca, es blanda.", "Si no, es dura."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El agua del río deja las piedras…", "pasos": ["…___ y lisas."]},
"ejemplo_solo": {"titulo": "Colección", "planteo": "Juntá tres piedras distintas. ¿En qué se parecen?"},
"tip": {"titulo": "Mirá y tocá", "texto": "Fijate el color, la forma y si es lisa."},
"ojo": ["No tires piedras: pueden lastimar.", "Las rocas pueden ser duras o blandas."],
"resumen": [{"titulo": "Granito", "texto": "Muy duro."}, {"titulo": "Tiza", "texto": "Blanda."}, {"titulo": "Canto rodado", "texto": "Redonda, del río."}],
"glosario": [{"palabra": "Roca", "significado": "Pedazo duro de la tierra."}, {"palabra": "Canto rodado", "significado": "Piedra redonda del río."}],
"carpeta": ["¿Qué roca es la pista 1?", "¿Qué roca es la pista 2?", "Tomi dice que todas las rocas son igual de duras. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("TIZA") + low("LA TIZA"), low("CANTO RODADO") + low("UN CANTO RODADO") + low("EL CANTO RODADO"), NO],
"soluciones": {"incompleto": "REDONDAS.", "solo": "En qué se parecen tus piedras.", "carpeta": ["La tiza.", "Un canto rodado.", "No: hay duras y blandas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer los bichitos del suelo.",
"vas_a_ver": ["Lombrices", "Hormigas", "Bichos bolita"],
"secciones": [
 S(1, "Vida bajo tierra", [
  P("En el suelo viven muchos <b>seres vivos</b>: lombrices, hormigas, bichos bolita."),
  IMG("Bichitos del suelo", "Viven bajo tierra.", FG.nombres(["LOMBRIZ", "HORMIGA", "BICHO BOLITA"], cols=3)),
 ]),
 S(1, "Las lombrices ayudan", [
  P("Las <b>lombrices</b> hacen túneles: así entran el <b>aire</b> y el agua."),
  P("Comen hojas secas y dejan la tierra más <b>rica</b> para las plantas."),
  IMG("Lombrices amigas", "Ayudan al suelo.", FG.tiras(["HACEN TÚNELES", "ENTRA AIRE Y AGUA", "LA TIERRA MEJORA"], numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Quién es?", "Pensá en cada pista.", FG.tiras(["1. SE HACE UNA BOLITA SI LO TOCÁS", "2. HACE TÚNELES Y NO TIENE PATAS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La lombriz", "planteo": "¿Cómo ayuda la lombriz?", "pasos": ["Hace túneles.", "Entra aire y agua.", "Las plantas crecen mejor."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las lombrices comen…", "pasos": ["…hojas ___ ."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Con un adulto, levantá una piedra del jardín. ¿Qué bichitos ves?"},
"tip": {"titulo": "Con cuidado", "texto": "Mirá los bichitos y dejalos en su lugar."},
"ojo": ["Algunas hormigas pican.", "Las lombrices son buenas para el suelo."],
"resumen": [{"titulo": "Lombriz", "texto": "Hace túneles."}, {"titulo": "Hormiga", "texto": "Vive en el hormiguero."}, {"titulo": "Bicho bolita", "texto": "Se hace bolita."}],
"glosario": [{"palabra": "Túnel", "significado": "Camino por debajo de la tierra."}, {"palabra": "Ser vivo", "significado": "Nace, crece y se alimenta."}],
"carpeta": ["¿Quién es la pista 1?", "¿Quién es la pista 2?", "Tomi dice que las lombrices le hacen mal al suelo. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("BICHO BOLITA") + low("EL BICHO BOLITA") + low("UN BICHO BOLITA"), low("LOMBRIZ") + low("LA LOMBRIZ") + low("UNA LOMBRIZ"), NO],
"soluciones": {"incompleto": "SECAS.", "solo": "Los bichitos que viste.", "carpeta": ["El bicho bolita.", "La lombriz.", "No: lo ayudan."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver qué suelo es mejor para sembrar.",
"vas_a_ver": ["Arena", "Arcilla", "Tierra negra"],
"secciones": [
 S(1, "Tres suelos", [
  P("La <b>arena</b> deja pasar el agua muy rápido."),
  P("La <b>arcilla</b> se pone dura y casi no deja pasar el agua."),
  P("La <b>tierra negra</b> guarda agua justa y tiene restos de hojas."),
  IMG("Tres suelos", "Cada uno es distinto.", FG.tiras(["ARENA: EL AGUA SE VA", "ARCILLA: EL AGUA QUEDA ARRIBA", "TIERRA NEGRA: JUSTO"], numeros=False, cols=1)),
 ]),
 S(1, "Para sembrar", [
  P("Tomi siembra porotos en los tres suelos. ¡Crecen mejor en la <b>tierra negra</b>!"),
  IMG("Mejor para sembrar", "La tierra negra gana.", FG.nombres(["ARENA", "ARCILLA", "TIERRA NEGRA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Qué suelo es?", "Pensá en el agua.", FG.tiras(["1. EL AGUA SE VA MUY RÁPIDO", "2. TIENE RESTOS DE HOJAS Y ES OSCURA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El poroto", "planteo": "¿Dónde crece mejor?", "pasos": ["Siembro en tres macetas.", "Riego igual a todas.", "Gana la tierra negra."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La mejor para sembrar es la tierra…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu huerta", "planteo": "Sembrá un poroto en una maceta con tierra negra."},
"tip": {"titulo": "Probá igual", "texto": "Para comparar, regá igual a todas las macetas."},
"ojo": ["La arena sola no guarda agua.", "La arcilla se pone dura al secarse."],
"resumen": [{"titulo": "Arena", "texto": "El agua se va."}, {"titulo": "Arcilla", "texto": "El agua queda."}, {"titulo": "Tierra negra", "texto": "La mejor para sembrar."}],
"glosario": [{"palabra": "Arcilla", "significado": "Tierra que se pone dura."}, {"palabra": "Sembrar", "significado": "Poner semillas en la tierra."}],
"carpeta": ["¿Qué suelo es la tarjeta 1?", "¿Qué suelo es la tarjeta 2?", "Tomi dice que la arena sola es la mejor para sembrar. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ARENA") + low("LA ARENA"), low("TIERRA NEGRA") + low("LA TIERRA NEGRA"), NO],
"soluciones": {"incompleto": "NEGRA.", "solo": "Cómo crece tu poroto.", "carpeta": ["La arena.", "La tierra negra.", "No: es mejor la tierra negra."]},
}

ACT = {
"1": [MC("¿QUÉ QUEDA ABAJO EN EL FRASCO?", ["LAS PIEDRITAS", "LAS HOJITAS"], "LAS PIEDRITAS", "SON MÁS PESADAS.", n="aplicar"),
      TF("EL SUELO TIENE AGUA Y AIRE.", "VERDADERO", "ENTRE LAS PIEDRITAS.", n="recordar")],
"2": [UNI("UNÍ CADA ROCA.", [("GRANITO", "MUY DURO"), ("TIZA", "BLANDA"), ("CANTO RODADO", "REDONDO")], "CADA ROCA ES DISTINTA.", n="analizar"),
      TF("TODAS LAS ROCAS SON IGUALES.", "FALSO", "HAY DURAS Y BLANDAS.", n="error")],
"3": [MC("¿QUIÉN HACE TÚNELES EN EL SUELO?", ["LA LOMBRIZ", "LA MARIPOSA"], "LA LOMBRIZ", "ASÍ ENTRA EL AIRE.", n="aplicar"),
      ORD("ORDENÁ: CÓMO AYUDA LA LOMBRIZ.", ["LA TIERRA MEJORA", "HACE TÚNELES", "ENTRA AIRE Y AGUA"], ["HACE TÚNELES", "ENTRA AIRE Y AGUA", "LA TIERRA MEJORA"], "PRIMERO LOS TÚNELES.", n="analizar")],
"4": [MC("¿DÓNDE CRECE MEJOR EL POROTO?", ["TIERRA NEGRA", "ARENA"], "TIERRA NEGRA", "GUARDA AGUA JUSTA.", n="aplicar"),
      SA("¿QUÉ SUELO SE PONE DURO AL SECARSE?", low("ARCILLA") + low("LA ARCILLA"), "LA ARCILLA.", n="recordar")],
"5": [MC("RELÁMPAGO. SE VE CON LUPA…", ["EL SUELO", "LA LUNA"], "EL SUELO", "MIRAMOS DE CERCA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA TIZA ES…", ["BLANDA", "MUY DURA"], "BLANDA", "SE RAYA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL BICHO BOLITA…", ["SE HACE BOLITA", "VUELA"], "SE HACE BOLITA", "SI LO TOCÁS.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL AGUA SE VA RÁPIDO EN…", ["LA ARENA", "LA ARCILLA"], "LA ARENA", "NO LA GUARDA.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES EL SUELO?", ["LA TIERRA QUE PISAMOS", "EL CIELO"], "LA TIERRA QUE PISAMOS", "DONDE CRECEN LAS PLANTAS.", n="recordar")],
 [1, SA("EN EL FRASCO, ¿QUÉ FLOTA ARRIBA?", low("HOJITAS") + low("LAS HOJITAS") + low("HOJAS") + low("LAS HOJAS"), "LAS HOJITAS.", n="aplicar")],
 [1, TF("EL SUELO ES SOLO TIERRA, SIN NADA MÁS.", "FALSO", "TIENE PIEDRITAS, HOJAS, AGUA Y AIRE.", n="error")],
 [2, MC("¿CÓMO SON LAS PIEDRAS DEL RÍO?", ["REDONDAS Y LISAS", "CON PUNTAS"], "REDONDAS Y LISAS", "EL AGUA LAS GASTA.", n="aplicar")],
 [2, SA("¿QUÉ ROCA BLANDA SE USA EN EL PIZARRÓN?", low("TIZA") + low("LA TIZA"), "LA TIZA.", n="recordar")],
 [2, TF("EL GRANITO ES UNA ROCA MUY DURA.", "VERDADERO", "CUESTA RAYARLO.", n="recordar")],
 [3, UNI("UNÍ CADA BICHITO.", [("LOMBRIZ", "HACE TÚNELES"), ("BICHO BOLITA", "SE HACE BOLITA")], "PENSÁ QUÉ HACE CADA UNO.", n="analizar")],
 [3, MC("¿QUÉ COMEN LAS LOMBRICES?", ["HOJAS SECAS", "PIEDRAS"], "HOJAS SECAS", "Y MEJORAN LA TIERRA.", n="recordar")],
 [3, TF("LAS LOMBRICES LE HACEN MAL AL SUELO.", "FALSO", "LO AYUDAN.", n="error")],
 [4, UNI("UNÍ CADA SUELO.", [("ARENA", "EL AGUA SE VA"), ("ARCILLA", "EL AGUA QUEDA"), ("TIERRA NEGRA", "JUSTO")], "PENSÁ EN EL AGUA.", n="analizar")],
 [4, SA("¿QUÉ SUELO ES MEJOR PARA SEMBRAR?", low("TIERRA NEGRA") + low("LA TIERRA NEGRA"), "LA TIERRA NEGRA.", n="aplicar")],
 [4, TF("PARA COMPARAR, HAY QUE REGAR IGUAL A TODAS.", "VERDADERO", "ASÍ ES JUSTO.", n="analizar")],
]
M = {"subject_id": "255a306f-d137-43b8-a9ce-c621b75c890a", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: el suelo y las rocas", "examen_titulo": "Nivel jefe: el suelo y las rocas",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
