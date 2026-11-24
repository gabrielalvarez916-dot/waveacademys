# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 5 · Caminos y transportes entre el campo y la ciudad. Genera mision-5.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy viaja del campo a la ciudad).
Niveles: 1 rutas, caminos y vías · 2 camiones, trenes y barcos · 3 cómo llega la comida · 4 mapas de recorridos."""
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
"objetivo": "Vas a conocer los caminos que unen el campo y la ciudad.",
"vas_a_ver": ["Rutas", "Caminos de tierra", "Vías del tren"],
"secciones": [
 S(1, "Por dónde se viaja", [
  P("El campo y la ciudad están unidos por <b>caminos</b>."),
  P("Por esos caminos viajan personas, animales y mercaderías. Sin caminos, la comida no llegaría a la ciudad."),
  IMG("Caminos", "Cada uno es distinto.", FG.tiras(["RUTA: ASFALTADA Y LARGA", "CAMINO DE TIERRA: EN EL CAMPO", "VÍAS: PARA EL TREN", "RÍO: PARA LOS BARCOS"], numeros=False)),
 ]),
 S(1, "Con lluvia", [
  P("Cuando llueve, el camino de tierra se llena de <b>barro</b>."),
  P("La ruta asfaltada se puede usar igual."),
  P("Con mucha lluvia, algunos chicos del campo no llegan a la escuela."),
  IMG("Partes de una ruta", "Para viajar seguros.", FG.nombres(["CARTELES", "PUENTE", "BANQUINA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué camino es?", "Pensá en cada pista.", FG.tiras(["1. POR ACÁ PASA EL TREN", "2. CON LLUVIA SE LLENA DE BARRO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El viaje de Lola", "planteo": "¿Cómo va Lola al campo?", "pasos": ["Sale por la ruta.", "Cruza un puente.", "Sigue por un camino de tierra."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El tren va por las…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu barrio", "planteo": "¿La calle de tu casa es de tierra o asfaltada?"},
"tip": {"titulo": "¿Asfalto o tierra?", "texto": "Mirá de qué está hecho el camino."},
"ojo": ["Con barro, los caminos son peligrosos.", "Las vías del tren no se cruzan por cualquier lado."],
"resumen": [{"titulo": "Ruta", "texto": "Asfaltada."}, {"titulo": "Camino de tierra", "texto": "En el campo."}, {"titulo": "Vías", "texto": "Para el tren."}],
"glosario": [{"palabra": "Asfalto", "significado": "Material negro y duro de las rutas."}, {"palabra": "Banquina", "significado": "Costado de la ruta."}],
"carpeta": ["¿Qué camino es la pista 1?", "¿Qué camino es la pista 2?", "Lola dice que el tren va por la ruta. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("VÍAS") + low("vias") + low("LAS VÍAS") + low("las vias"), low("CAMINO DE TIERRA") + low("EL CAMINO DE TIERRA") + low("TIERRA"), NO],
"soluciones": {"incompleto": "VÍAS.", "solo": "Cómo es tu calle.", "carpeta": ["Las vías.", "El camino de tierra.", "No: va por las vías."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a conocer los transportes de carga.",
"vas_a_ver": ["Camiones", "Trenes", "Barcos"],
"secciones": [
 S(1, "Transportes de carga", [
  D("Carga", "Las cosas que lleva un transporte, como granos o frutas."),
  IMG("Para llevar carga", "Cada uno por su camino.", FG.tiras(["CAMIÓN: POR LA RUTA", "TREN: POR LAS VÍAS", "BARCO: POR EL RÍO Y EL MAR"], numeros=False, cols=1)),
 ]),
 S(1, "¿Cuál lleva más?", [
  P("El <b>camión</b> llega a muchos lugares. El <b>tren</b> lleva más carga."),
  P("El <b>barco</b> lleva muchísima, ¡y cruza el mar!"),
  P("Muchas veces se usan los tres. El camión saca la carga del campo. El tren la lleva lejos. El barco la lleva a otros países."),
  IMG("De menos a más", "Cuánta carga llevan.", FG.nombres(["CAMIÓN", "TREN", "BARCO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué transporte es?", "Pensá en cada pista.", FG.tiras(["1. VA POR EL RÍO CON MUCHA CARGA", "2. VA POR LA RUTA HASTA EL ALMACÉN"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La soja", "planteo": "¿Cómo viaja la soja?", "pasos": ["Un camión la saca del campo.", "Un tren la lleva al puerto.", "Un barco la lleva a otro país."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El barco va por el río y el…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Observá", "planteo": "¿Viste pasar un camión de carga? ¿Qué llevaba?"},
"tip": {"titulo": "¿Por dónde va?", "texto": "Ruta, vías o agua: así sabés qué transporte es."},
"ojo": ["Los transportes unen el campo y la ciudad.", "Algunos productos usan varios transportes."],
"resumen": [{"titulo": "Camión", "texto": "Por la ruta."}, {"titulo": "Tren", "texto": "Por las vías."}, {"titulo": "Barco", "texto": "Por el agua."}],
"glosario": [{"palabra": "Carga", "significado": "Lo que lleva un transporte."}, {"palabra": "Puerto", "significado": "Lugar donde paran los barcos."}],
"carpeta": ["¿Qué transporte es la pista 1?", "¿Qué transporte es la pista 2?", "Lola dice que el camión cruza el mar. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("BARCO") + low("EL BARCO") + low("UN BARCO"), low("CAMIÓN") + low("camion") + low("EL CAMIÓN") + low("el camion") + low("UN CAMIÓN"), NO],
"soluciones": {"incompleto": "MAR.", "solo": "Lo que llevaba.", "carpeta": ["El barco.", "El camión.", "No: el barco cruza el mar."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver cómo llega la comida a la ciudad.",
"vas_a_ver": ["Del campo", "Al mercado", "A la verdulería"],
"secciones": [
 S(1, "El viaje de la lechuga", [
  P("La <b>lechuga</b> crece en una quinta, cerca de la ciudad."),
  P("El quintero la cosecha de madrugada. La pone en cajones. Un camión la lleva enseguida para que llegue fresca."),
  IMG("Del campo a tu mesa", "Paso a paso.", FG.tiras(["1. LA COSECHAN EN LA QUINTA", "2. VIAJA EN CAMIÓN", "3. LLEGA AL MERCADO", "4. LA VENDEN EN LA VERDULERÍA"], numeros=False)),
 ]),
 S(1, "El mercado", [
  D("Mercado central", "Lugar grande donde llegan frutas y verduras para <b>vender</b>."),
  P("Los verduleros compran ahí, muy temprano."),
  P("Después la llevan a su negocio del barrio."),
  IMG("Quiénes trabajan", "Muchas personas.", FG.nombres(["QUINTERO", "CHOFER", "VERDULERA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Desordenadas", "¿Qué va primero?", FG.tiras(["LLEGA AL MERCADO", "LA COSECHAN EN LA QUINTA", "LA VENDEN EN LA VERDULERÍA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Las naranjas", "planteo": "¿Cómo llegan las naranjas?", "pasos": ["Las cosechan en el campo.", "Viajan en camión.", "Las compramos en la verdulería."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La lechuga crece en una…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Dibujalo", "planteo": "Dibujá el viaje de tu fruta favorita hasta tu mesa."},
"tip": {"titulo": "Sin transporte, no llega", "texto": "La comida necesita viajar hasta la ciudad."},
"ojo": ["La verdura viaja rápido para estar fresca.", "Muchas personas trabajan en el viaje."],
"resumen": [{"titulo": "Quinta", "texto": "Se cosecha."}, {"titulo": "Mercado", "texto": "Se vende a los negocios."}, {"titulo": "Verdulería", "texto": "La compramos."}],
"glosario": [{"palabra": "Quinta", "significado": "Campo donde se cultivan verduras."}, {"palabra": "Quintero", "significado": "Persona que trabaja la quinta."}],
"carpeta": ["De las tarjetas, ¿qué va primero?", "¿Qué va al final?", "Lola dice que la lechuga crece en la verdulería. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("LA COSECHAN EN LA QUINTA") + low("LA QUINTA") + low("QUINTA"), low("LA VENDEN EN LA VERDULERÍA") + low("LA VERDULERÍA") + low("verduleria") + low("la verduleria"), NO],
"soluciones": {"incompleto": "QUINTA.", "solo": "Tu dibujo del viaje.", "carpeta": ["La cosechan en la quinta.", "La venden en la verdulería.", "No: crece en la quinta."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a leer un mapa de recorrido.",
"vas_a_ver": ["Qué es un recorrido", "El mapa", "Las referencias"],
"secciones": [
 S(1, "El recorrido", [
  D("Recorrido", "El camino que hace alguien de un lugar a otro."),
  P("En el mapa, el recorrido se marca con una <b>línea</b> o flechas."),
  P("El mapa muestra los lugares vistos desde arriba, como si volaras. Así vemos calles, plazas y casas."),
  IMG("El recorrido del camión", "De la quinta a la verdulería.", FG.tiras(["QUINTA", "RUTA", "MERCADO", "VERDULERÍA"], numeros=True)),
 ]),
 S(1, "Las referencias", [
  D("Referencias", "Dibujitos que explican qué es cada cosa en el mapa."),
  IMG("Referencias", "Para leer el mapa.", FG.nombres(["LÍNEA ROJA: RUTA", "ÁRBOL: CAMPO", "CASITAS: CIUDAD"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el recorrido. Lo vas a usar en la carpeta."),
  IMG("El recorrido de Lola", "De su casa a la escuela.", FG.tiras(["CASA", "PLAZA", "KIOSCO", "ESCUELA"], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Leer el mapa", "planteo": "¿Cómo leo un recorrido?", "pasos": ["Busco dónde empieza.", "Sigo la línea.", "Llego al final."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los dibujitos que explican el mapa son las…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Tu recorrido", "planteo": "Dibujá el recorrido de tu casa a la escuela."},
"tip": {"titulo": "Seguí la línea", "texto": "Empezá por el número 1."},
"ojo": ["Mirá siempre las referencias.", "Un recorrido tiene principio y final."],
"resumen": [{"titulo": "Recorrido", "texto": "De un lugar a otro."}, {"titulo": "Línea", "texto": "Marca el camino."}, {"titulo": "Referencias", "texto": "Explican el mapa."}],
"glosario": [{"palabra": "Mapa", "significado": "Dibujo de un lugar visto de arriba."}, {"palabra": "Recorrido", "significado": "Camino de un lugar a otro."}],
"carpeta": ["En el recorrido de Lola, ¿por dónde pasa después de la plaza?", "¿Dónde termina?", "Lola dice que un mapa no necesita referencias. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"respuestas_carpeta": [low("KIOSCO") + low("EL KIOSCO") + low("POR EL KIOSCO"), low("ESCUELA") + low("EN LA ESCUELA") + low("LA ESCUELA"), NO],
"soluciones": {"incompleto": "REFERENCIAS.", "solo": "Tu recorrido.", "carpeta": ["Por el kiosco.", "En la escuela.", "No: las referencias explican el mapa."]},
}

ACT = {
"1": [UNI("UNÍ CADA CAMINO.", [("RUTA", "ASFALTADA"), ("VÍAS", "TREN"), ("RÍO", "BARCO")], "CADA UNO TIENE SU TRANSPORTE.", n="analizar"),
      TF("LLOVIÓ TODA LA NOCHE: EL CAMINO DE TIERRA TIENE BARRO.", "VERDADERO", "POR ESO ES PELIGROSO.", n="aplicar")],
"2": [MC("UNA FÁBRICA QUIERE MANDAR AUTOS A OTRO PAÍS POR MAR. ¿QUÉ USA?", ["EL BARCO", "EL CAMIÓN"], "EL BARCO", "VA POR EL AGUA.", n="aplicar"),
      ORD("ORDENÁ DE MENOS A MÁS CARGA.", ["BARCO", "CAMIÓN", "TREN"], ["CAMIÓN", "TREN", "BARCO"], "EL BARCO LLEVA MÁS.", n="analizar")],
"3": [ORD("ORDENÁ EL VIAJE DE LA LECHUGA.", ["MERCADO", "VERDULERÍA", "QUINTA"], ["QUINTA", "MERCADO", "VERDULERÍA"], "PRIMERO SE COSECHA.", n="analizar"),
      TF("LA LECHUGA CRECE EN LA VERDULERÍA.", "FALSO", "CRECE EN LA QUINTA.", n="error")],
"4": [MC("¿QUÉ EXPLICAN LAS REFERENCIAS?", ["QUÉ ES CADA COSA DEL MAPA", "LA HORA"], "QUÉ ES CADA COSA DEL MAPA", "SON DIBUJITOS.", n="recordar"),
      SA("CASA, PLAZA, KIOSCO, ESCUELA. ¿QUÉ VA DESPUÉS DE LA PLAZA?", low("KIOSCO") + low("EL KIOSCO"), "EL KIOSCO.", n="analizar")],
"5": [MC("RELÁMPAGO. EL TREN VA POR…", ["LAS VÍAS", "EL RÍO"], "LAS VÍAS", "SOBRE RIELES.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LLEVA MÁS CARGA…", ["EL BARCO", "EL CAMIÓN"], "EL BARCO", "MUCHÍSIMA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LA VERDURA LLEGA AL…", ["MERCADO", "PUERTO"], "MERCADO", "Y DE AHÍ A LA VERDULERÍA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL RECORRIDO SE MARCA CON…", ["UNA LÍNEA", "UN SELLO"], "UNA LÍNEA", "O FLECHAS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿CÓMO ES UNA RUTA?", ["ASFALTADA", "DE AGUA"], "ASFALTADA", "PARA AUTOS Y CAMIONES.", n="recordar")],
 [1, SA("¿POR DÓNDE VA EL TREN?", low("VÍAS") + low("vias") + low("LAS VÍAS") + low("las vias") + low("POR LAS VÍAS") + low("por las vias"), "POR LAS VÍAS.", n="recordar")],
 [1, TF("EL CAMPO Y LA CIUDAD ESTÁN UNIDOS POR CAMINOS.", "VERDADERO", "RUTAS, VÍAS Y RÍOS.", n="recordar")],
 [2, UNI("UNÍ CADA TRANSPORTE.", [("CAMIÓN", "RUTA"), ("BARCO", "MAR")], "¿POR DÓNDE VA?", n="analizar")],
 [2, SA("UN CAMPO TIENE MUCHÍSIMA SOJA PARA OTRO PAÍS. ¿QUÉ TRANSPORTE LLEVA MÁS?", low("BARCO") + low("EL BARCO"), "EL BARCO.", n="aplicar")],
 [2, TF("TOMÁS DICE QUE EL CAMIÓN CRUZA EL MAR.", "FALSO", "LO CRUZA EL BARCO.", n="error")],
 [3, MC("UN VERDULERO NECESITA COMPRAR TOMATES MUY TEMPRANO. ¿ADÓNDE VA?", ["EN EL MERCADO", "EN LA ESCUELA"], "EN EL MERCADO", "MUY TEMPRANO.", n="aplicar")],
 [3, SA("¿CÓMO SE LLAMA EL CAMPO DONDE CRECEN VERDURAS?", low("QUINTA") + low("LA QUINTA") + low("HUERTA") + low("LA HUERTA"), "LA QUINTA.", n="recordar")],
 [3, MC("¿POR QUÉ LA VERDURA VIAJA RÁPIDO?", ["PARA ESTAR FRESCA", "PARA JUGAR"], "PARA ESTAR FRESCA", "SI NO, SE ECHA A PERDER.", n="aplicar")],
 [4, MC("¿QUÉ ES UN RECORRIDO?", ["UN CAMINO ENTRE DOS LUGARES", "UN JUEGO DE MESA CHICO"], "UN CAMINO ENTRE DOS LUGARES", "SE MARCA EN EL MAPA.", n="recordar")],
 [4, ORD("ORDENÁ EL RECORRIDO DE LOLA.", ["ESCUELA", "CASA", "PLAZA"], ["CASA", "PLAZA", "ESCUELA"], "EMPIEZA EN LA CASA.", n="analizar")],
 [4, TF("LUCÍA DICE QUE UN MAPA NO NECESITA REFERENCIAS.", "FALSO", "LAS REFERENCIAS LO EXPLICAN.", n="error")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: caminos y transportes", "examen_titulo": "Nivel jefe: caminos y transportes",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
