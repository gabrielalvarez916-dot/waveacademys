# -*- coding: utf-8 -*-
"""Ciencias Sociales 2 (Nivel Medio, 2.º año) · Misión 6 · Vida cotidiana en la época colonial. Genera mision-6.json.
Regla de primeros años. Metáfora del año: Lola, reportera del barrio (hoy viaja con la imaginación a la época colonial).
Niveles: 1 la casa colonial · 2 velas y faroles · 3 trabajos y jerarquías · 4 comparamos con hoy."""
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
"objetivo": "Vas a conocer cómo era una casa colonial.",
"vas_a_ver": ["La época colonial", "Las partes de la casa", "El agua del aljibe"],
"secciones": [
 S(1, "La época colonial", [
  {**D("Época colonial", "Hace más de doscientos años. Estas tierras dependían del rey de <b>España</b>."), "neutro": {"texto": "Hace más de doscientos años. Muchas tierras de América dependían de reyes de <b>Europa</b>."}},
  P("Lola visita un museo. Ahí hay una casa de esa época. ¡Es muy distinta a las de hoy!"),
  P("Las paredes eran gruesas, de <b>adobe</b> o ladrillo. Los techos eran de tejas."),
  IMG("La casa colonial", "Sus partes.", FG.tiras(["ZAGUÁN: LA ENTRADA", "PATIO: EN EL MEDIO", "HABITACIONES: ALREDEDOR", "ALJIBE: EL AGUA"], numeros=False)),
 ]),
 S(1, "El patio y el aljibe", [
  P("La casa tenía uno o más <b>patios</b>. Alrededor estaban las habitaciones."),
  P("No había canillas. El agua de lluvia se juntaba en el <b>aljibe</b>."),
  P("Las familias ricas tenían casas grandes. Las familias pobres vivían en ranchos chicos."),
  IMG("En el patio", "Ahí se juntaba la familia.", FG.nombres(["PATIO", "ALJIBE", "MACETAS"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Qué parte es?", "Pensá en cada pista.", FG.tiras(["1. SE ENTRA A LA CASA POR ACÁ", "2. ACÁ SE JUNTA EL AGUA DE LLUVIA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Buscar agua", "planteo": "¿Cómo tomaban agua en la casa colonial?", "pasos": ["Iban al aljibe del patio.", "Bajaban un balde con una soga.", "Subían el agua de lluvia."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El agua de lluvia se juntaba en el…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Dibujala", "planteo": "Dibujá una casa colonial con su patio y su aljibe."},
"tip": {"titulo": "Mirá el patio", "texto": "En la casa colonial, todo daba al patio."},
"ojo": ["No todas las casas eran iguales.", "Los más pobres vivían en ranchos."],
"resumen": [{"titulo": "Zaguán", "texto": "La entrada."}, {"titulo": "Patio", "texto": "En el medio."}, {"titulo": "Aljibe", "texto": "Para el agua."}],
"glosario": [{"palabra": "Aljibe", "significado": "Pozo que junta agua de lluvia."}, {"palabra": "Zaguán", "significado": "Pasillo de entrada de la casa."}],
"carpeta": ["En la pista 1, ¿qué parte de la casa es?", "En la pista 2, ¿qué parte de la casa es?", "Lola dice que en la casa colonial había canillas. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ZAGUÁN") + low("zaguan") + low("EL ZAGUÁN") + low("el zaguan"), low("ALJIBE") + low("EL ALJIBE"), NO],
"soluciones": {"incompleto": "ALJIBE.", "solo": "Tu dibujo.", "carpeta": ["El zaguán.", "El aljibe.", "No: usaban el aljibe."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver cómo se alumbraban antes.",
"vas_a_ver": ["Velas", "Faroles", "El farolero"],
"secciones": [
 S(1, "Sin luz eléctrica", [
  P("En la época colonial <b>no había luz eléctrica</b>. Cuando se hacía de noche, todo quedaba oscuro."),
  P("Para ver, prendían <b>velas</b>. Muchas se hacían con <b>sebo</b>, la grasa de las vacas."),
  P("Las velas de sebo tenían olor fuerte y hacían humo."),
  IMG("Para alumbrarse", "Con fuego.", FG.nombres(["VELA", "CANDIL", "FAROL"], cols=3)),
 ]),
 S(1, "El farolero", [
  D("Farolero", "Trabajador que prendía los <b>faroles</b> de la calle al atardecer."),
  P("Caminaba con una escalera. Subía y encendía cada farol."),
  P("A la mañana volvía para apagarlos. ¡Era un trabajo de todos los días!"),
  IMG("El trabajo del farolero", "Paso a paso.", FG.tiras(["1. LLEGA EL ATARDECER", "2. APOYA LA ESCALERA", "3. PRENDE EL FAROL", "4. SIGUE AL OTRO"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Antes u hoy?", "Pensá en cada una.", FG.tiras(["1. UNA VELA DE SEBO", "2. UNA LAMPARITA ELÉCTRICA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Una noche colonial", "planteo": "¿Cómo leían de noche?", "pasos": ["Prendían una vela.", "Se sentaban cerca.", "Leían con poca luz."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los faroles de la calle los prendía el…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Imaginá", "planteo": "¿Qué harías una noche sin luz eléctrica? Escribilo."},
"tip": {"titulo": "¿Fuego o electricidad?", "texto": "Antes, la luz venía del fuego."},
"ojo": ["Las velas se prenden solo con un adulto.", "El fuego puede ser peligroso."],
"resumen": [{"titulo": "Velas", "texto": "De sebo."}, {"titulo": "Faroles", "texto": "En la calle."}, {"titulo": "Farolero", "texto": "Los prendía."}],
"glosario": [{"palabra": "Sebo", "significado": "Grasa de vaca para hacer velas."}, {"palabra": "Candil", "significado": "Lámpara chica de aceite."}],
"carpeta": ["En la tarjeta 1, ¿es de antes o de hoy?", "En la tarjeta 2, ¿es de antes o de hoy?", "Lola dice que en la época colonial había lamparitas. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("ANTES") + low("DE ANTES"), low("HOY") + low("DE HOY") + low("AHORA"), NO],
"soluciones": {"incompleto": "FAROLERO.", "solo": "Lo que harías.", "carpeta": ["De antes.", "De hoy.", "No: usaban velas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer los trabajos de la época colonial.",
"vas_a_ver": ["Vendedores de la calle", "Trabajos de la casa", "No todos eran iguales"],
"secciones": [
 S(1, "Vendedores de la calle", [
  P("Por las calles pasaban muchos <b>vendedores</b>. Anunciaban lo que vendían a los gritos."),
  P("El <b>aguatero</b> vendía agua del río en un carro. El <b>lechero</b> llegaba a caballo."),
  P("La <b>mazamorrera</b> vendía mazamorra, un postre de maíz y leche."),
  IMG("Vendedores", "Pasaban por las casas.", FG.tiras(["AGUATERO: AGUA DEL RÍO", "LECHERO: LECHE A CABALLO", "MAZAMORRERA: MAZAMORRA", "VELERO: VELAS"], numeros=False)),
 ]),
 S(1, "No todos eran iguales", [
  P("En esa época, las personas <b>no tenían los mismos derechos</b>."),
  P("Algunas familias eran ricas y mandaban. Otras eran pobres."),
  D("Persona esclavizada", "Persona obligada a trabajar <b>sin pago</b> y sin libertad. Era muy injusto."),
  P("Hoy la ley dice que todas las personas son libres e iguales."),
  IMG("Hoy: todos iguales", "Lo dice la ley.", FG.nombres(["LIBERTAD", "IGUALDAD", "DERECHOS"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pistas. Las vas a usar en la carpeta."),
  IMG("¿Quién es?", "Pensá en cada pista.", FG.tiras(["1. VENDE AGUA DEL RÍO EN UN CARRO", "2. VENDE UN POSTRE DE MAÍZ Y LECHE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Comprar agua", "planteo": "¿Cómo compraban agua?", "pasos": ["Esperaban al aguatero.", "Él llenaba la tinaja.", "Le pagaban con monedas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La leche la traía el lechero a…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Pregoná", "planteo": "Inventá un grito para vender algo, como los vendedores."},
"tip": {"titulo": "¿Qué vende?", "texto": "El nombre del trabajo dice qué vende."},
"ojo": ["Esclavizar personas es injusto y hoy está prohibido.", "Todas las personas tienen derechos."],
"resumen": [{"titulo": "Aguatero", "texto": "Vendía agua."}, {"titulo": "Mazamorrera", "texto": "Vendía mazamorra."}, {"titulo": "Derechos", "texto": "Hoy, iguales para todos."}],
"glosario": [{"palabra": "Aguatero", "significado": "Vendedor de agua."}, {"palabra": "Mazamorra", "significado": "Postre de maíz y leche."}],
"carpeta": ["En la pista 1, ¿qué trabajo es?", "En la pista 2, ¿qué trabajo es?", "Lola dice que en esa época todos tenían los mismos derechos. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("AGUATERO") + low("EL AGUATERO"), low("MAZAMORRERA") + low("LA MAZAMORRERA"), NO],
"soluciones": {"incompleto": "CABALLO.", "solo": "Tu grito de vendedor.", "carpeta": ["El aguatero.", "La mazamorrera.", "No: no eran iguales."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a comparar la vida colonial con la de hoy.",
"vas_a_ver": ["Qué cambió", "Qué sigue igual", "Comparar"],
"secciones": [
 S(1, "Qué cambió", [
  P("Lola compara la vida de antes con la de hoy."),
  P("Antes el agua salía del aljibe. Hoy sale de la <b>canilla</b>."),
  P("Antes la luz venía de velas. Hoy usamos <b>electricidad</b>."),
  P("Antes se viajaba a caballo o en carreta. Hoy hay autos y colectivos."),
  IMG("Antes y hoy", "Comparamos.", FG.tiras(["AGUA: ALJIBE / CANILLA", "LUZ: VELA / LAMPARITA", "VIAJES: CABALLO / COLECTIVO"], numeros=False, cols=1)),
 ]),
 S(1, "Qué sigue igual", [
  P("Algunas cosas <b>siguen igual</b>. Las familias se juntan a comer."),
  P("Los chicos juegan a la rayuela y a la mancha. ¡Y seguimos comiendo empanadas y mazamorra!"),
  IMG("Siguen igual", "Desde hace mucho.", FG.nombres(["EMPANADAS", "JUEGOS", "FAMILIA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("¿Cambió o sigue igual?", "Pensá en cada una.", FG.tiras(["1. LA FORMA DE TENER AGUA EN CASA", "2. COMER EMPANADAS EN FAMILIA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La luz", "planteo": "¿Cómo cambió la luz?", "pasos": ["Antes: velas de sebo.", "Después: faroles de gas.", "Hoy: lamparitas eléctricas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Antes se viajaba a caballo. Hoy, en…", "pasos": ["…___ ."]},
"ejemplo_solo": {"titulo": "Entrevistá", "planteo": "Preguntale a un abuelo qué juego de su infancia sigue igual."},
"tip": {"titulo": "Dos columnas", "texto": "Anotá: cambió y sigue igual."},
"ojo": ["No todo cambió.", "Comparar ayuda a entender el pasado."],
"resumen": [{"titulo": "Cambió", "texto": "Agua, luz, viajes."}, {"titulo": "Sigue igual", "texto": "Familia y comidas."}, {"titulo": "Comparar", "texto": "Antes y hoy."}],
"glosario": [{"palabra": "Infancia", "significado": "Cuando una persona era chica."}, {"palabra": "Colonial", "significado": "De la época de la colonia."}],
"carpeta": ["En la tarjeta 1, ¿cambió o sigue igual?", "En la tarjeta 2, ¿cambió o sigue igual?", "Lola dice que todo cambió desde la época colonial. ¿Tiene razón?"],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("CAMBIÓ") + low("cambio"), low("SIGUE IGUAL") + low("IGUAL"), NO],
"soluciones": {"incompleto": "COLECTIVO (o auto).", "solo": "Lo que te contaron.", "carpeta": ["Cambió.", "Sigue igual.", "No: algunas cosas siguen igual."]},
}

ACT = {
"1": [MC("UNA FAMILIA COLONIAL NECESITA AGUA PARA COCINAR. ¿ADÓNDE VA?", ["AL ALJIBE", "A LA CANILLA"], "AL ALJIBE", "NO HABÍA CANILLAS.", n="aplicar"),
      UNI("UNÍ CADA PARTE DE LA CASA.", [("ZAGUÁN", "ENTRADA"), ("PATIO", "EN EL MEDIO"), ("ALJIBE", "AGUA")], "ASÍ ERA LA CASA.", n="analizar")],
"2": [MC("SE HIZO DE NOCHE EN LA ÉPOCA COLONIAL. ¿CON QUÉ SE ALUMBRAN?", ["CON VELAS", "CON LAMPARITAS"], "CON VELAS", "NO HABÍA ELECTRICIDAD.", n="aplicar"),
      ORD("ORDENÁ EL TRABAJO DEL FAROLERO.", ["PRENDE EL FAROL", "LLEGA EL ATARDECER", "APOYA LA ESCALERA"], ["LLEGA EL ATARDECER", "APOYA LA ESCALERA", "PRENDE EL FAROL"], "PRIMERO SE HACE DE NOCHE.", n="analizar")],
"3": [UNI("UNÍ CADA VENDEDOR CON LO QUE VENDÍA.", [("AGUATERO", "AGUA"), ("LECHERO", "LECHE"), ("MAZAMORRERA", "MAZAMORRA")], "EL NOMBRE AYUDA.", n="analizar"),
      TF("JUAN DICE QUE EN ESA ÉPOCA TODOS TENÍAN LOS MISMOS DERECHOS.", "FALSO", "NO ERAN IGUALES.", n="error")],
"4": [UNI("UNÍ: ¿ANTES O HOY?", [("ALJIBE", "ANTES"), ("CANILLA", "HOY")], "COMPARÁ.", n="analizar"),
      MC("LA FAMILIA DE LOLA COME EMPANADAS JUNTA. ¿ESO CAMBIÓ O SIGUE IGUAL?", ["SIGUE IGUAL", "CAMBIÓ"], "SIGUE IGUAL", "SE HACE DESDE HACE MUCHO.", n="analizar")],
"5": [MC("RELÁMPAGO. EL AGUA ESTABA EN EL…", ["ALJIBE", "LAVARROPAS"], "ALJIBE", "EN EL PATIO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. LAS VELAS ERAN DE…", ["SEBO", "PLÁSTICO"], "SEBO", "GRASA DE VACA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. VENDÍA AGUA EL…", ["AGUATERO", "FAROLERO"], "AGUATERO", "CON SU CARRO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. HOY LA LUZ ES…", ["ELÉCTRICA", "DE SEBO"], "ELÉCTRICA", "CON LAMPARITAS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("ENTRÁS A UNA CASA COLONIAL. ¿POR DÓNDE PASÁS PRIMERO?", ["POR EL ZAGUÁN", "POR EL ALJIBE"], "POR EL ZAGUÁN", "ES LA ENTRADA.", n="aplicar")],
 [1, ORD("ORDENÁ: CÓMO SACABAN AGUA DEL ALJIBE.", ["SUBÍAN EL AGUA", "IBAN AL PATIO", "BAJABAN EL BALDE"], ["IBAN AL PATIO", "BAJABAN EL BALDE", "SUBÍAN EL AGUA"], "PRIMERO AL PATIO.", n="analizar")],
 [1, TF("SOFÍA DICE QUE TODAS LAS CASAS COLONIALES ERAN GRANDES.", "FALSO", "LOS POBRES VIVÍAN EN RANCHOS.", n="error")],
 [2, MC("¿QUÉ TRABAJO HACÍA EL FAROLERO AL ATARDECER?", ["PRENDÍA LOS FAROLES", "VENDÍA LECHE"], "PRENDÍA LOS FAROLES", "CON SU ESCALERA.", n="recordar")],
 [2, SA("ERA DE NOCHE Y NO HABÍA ELECTRICIDAD. ¿QUÉ PRENDÍAN PARA VER?", low("VELAS") + low("UNA VELA") + low("VELA") + low("LAS VELAS") + low("FAROLES") + low("CANDIL"), "VELAS.", n="aplicar")],
 [2, TF("MARCOS DICE QUE LAS VELAS COLONIALES ERAN ELÉCTRICAS.", "FALSO", "ERAN DE SEBO.", n="error")],
 [3, UNI("UNÍ CADA TRABAJO.", [("FAROLERO", "FAROLES"), ("AGUATERO", "AGUA")], "¿QUÉ HACÍA CADA UNO?", n="analizar")],
 [3, MC("¿QUÉ ERA UNA PERSONA ESCLAVIZADA?", ["OBLIGADA A TRABAJAR SIN PAGO", "UNA PERSONA DE VACACIONES"], "OBLIGADA A TRABAJAR SIN PAGO", "ERA MUY INJUSTO.", n="recordar")],
 [3, TF("HOY LA LEY DICE QUE TODAS LAS PERSONAS SON LIBRES.", "VERDADERO", "Y TIENEN DERECHOS.", n="recordar")],
 [4, MC("ANTES EL AGUA SALÍA DEL ALJIBE. ¿Y HOY DE DÓNDE SALE?", ["DE LA CANILLA", "DEL FAROL"], "DE LA CANILLA", "CAMBIÓ.", n="aplicar")],
 [4, UNI("UNÍ: ¿CAMBIÓ O SIGUE IGUAL?", [("LA LUZ", "CAMBIÓ"), ("COMER EMPANADAS", "SIGUE IGUAL")], "PENSÁ EN ANTES Y HOY.", n="analizar")],
 [4, TF("LUCAS DICE QUE NADA CAMBIÓ DESDE LA ÉPOCA COLONIAL.", "FALSO", "CAMBIARON EL AGUA, LA LUZ Y LOS VIAJES.", n="error")],
]
M = {"subject_id": "dda5fe04-3df1-47cd-bcb6-a27259db9f3d", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: la época colonial", "examen_titulo": "Nivel jefe: la época colonial",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
