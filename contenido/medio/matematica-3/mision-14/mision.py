# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 14 · Repartos y particiones. Genera mision-14.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: el campamento de la escuela.
Niveles: 1 repartir cantidades grandes · 2 armar grupos · 3 lo que sobra · 4 problemas con resto."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), "matematica-1"))  # dibujos compartidos del Medio
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
N = lambda p, r, e, **k: {"t": "numeric", "p": p, "o": {}, "r": {"acepta": [r]}, "e": e, **k}
TF = lambda p, ok, e, **k: {"t": "true_false", "p": p, "o": ["VERDADERO", "FALSO"], "r": {"correcta": ok}, "e": e, **k}
ORD = lambda p, o, orden, e, **k: {"t": "ordering", "p": p, "o": o, "r": {"orden": orden}, "e": e, **k}
UNIR = lambda p, iz, de, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": iz, "derecha": de}, "r": {"pares": pares}, "e": e, **k}
CLAS = lambda p, el, cats, r, e, **k: {"t": "classify", "p": p, "o": {"elementos": el, "categorias": cats}, "r": {"categorias": r}, "e": e, **k}
FB = lambda p, huecos, e, **k: {"t": "fill_blank", "p": p, "o": {}, "r": {"huecos": huecos}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a repartir cantidades grandes.",
"vas_a_ver": ["Partir el número", "Repartir cada parte", "Sumar lo que toca"],
"secciones": [
 S(1, "Linternas", [
  P("Hay 84 linternas para 4 grupos."),
  P("80 ÷ 4 = 20 y 4 ÷ 4 = 1. A cada grupo, <b>21</b>."),
  IMG("84 ÷ 4", "Dos partes.", FG.cuentas([("80 ÷ 4", 20), ("4 ÷ 4", 1), ("20 + 1", 21)])),
 ]),
 S(1, "Partir", [
  D("Repartir en partes", "Partimos el número en <b>partes fáciles</b>, repartimos cada una y sumamos."),
  P("66 ÷ 3: 60 ÷ 3 = 20 y 6 ÷ 3 = 2. Son 22."),
  IMG("66 ÷ 3", "Dos partes.", FG.cuentas([("60 ÷ 3", 20), ("6 ÷ 3", 2)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Repartos", "Partí y repartí.", FG.cuentas([("48 ÷ 4", 12), ("55 ÷ 5", 11)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Repartir", "planteo": "39 ÷ 3.", "pasos": ["30 ÷ 3 = 10. 9 ÷ 3 = 3.", "A cada uno, 13."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "86 ÷ 2.", "pasos": ["80 ÷ 2 = ___ . 6 ÷ 2 = ___ .", "A cada uno, 43."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto le toca a cada uno si repartimos 64 entre 2?"},
"tip": {"titulo": "Partes fáciles", "texto": "Usá decenas que se repartan justo."},
"ojo": ["Repartí todas las partes.", "Sumá lo que toca de cada parte."],
"resumen": [{"titulo": "Partir", "texto": "En partes fáciles."}, {"titulo": "Repartir", "texto": "Cada parte."}, {"titulo": "Sumar", "texto": "Lo que toca."}],
"glosario": [{"palabra": "Repartir", "significado": "Dar a cada uno lo mismo."}, {"palabra": "Partir", "significado": "Separar en partes."}],
"carpeta": ["Repartimos 48 entre 4. ¿Cuánto le toca a cada uno?", "Repartimos 55 entre 5. ¿Cuánto le toca a cada uno?", "Leo repartió solo el 80 de 84 entre 4 y dijo 20. ¿Cuánto le toca a cada uno?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["12"], ["11"], ["21"]],
"soluciones": {"incompleto": "40. 3.", "solo": "32.", "carpeta": ["12.", "11.", "21."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a armar grupos iguales.",
"vas_a_ver": ["Grupos de la misma cantidad", "Contar los grupos", "Dividir"],
"secciones": [
 S(1, "Carpas", [
  P("Hay 24 chicos. En cada carpa duermen 4."),
  P("4, 8, 12, 16, 20, 24: <b>6 carpas</b>."),
  IMG("Carpas de 4", "6 grupos.", FG.grupos("pelota", 6, 4, "24 ÷ 4 = 6")),
 ]),
 S(1, "Agrupar", [
  D("Armar grupos", "Sabemos <b>cuánto va en cada grupo</b> y buscamos cuántos grupos salen."),
  P("También es una división: 24 ÷ 4 = 6."),
  IMG("30 de a 5", "6 grupos.", FG.grupos("estrella", 6, 5, "30 ÷ 5 = 6")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Grupos", "¿Cuántos grupos?", FG.cuentas([("18 de a 3", 6), ("28 de a 4", 7)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Agrupar", "planteo": "20 lápices en cajas de 5.", "pasos": ["5, 10, 15, 20.", "4 cajas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "36 huevos en cajas de 6.", "pasos": ["6 × ___ = 36.", "Son ___ cajas."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuántos equipos de 7 se arman con 21 chicos?"},
"tip": {"titulo": "Tabla", "texto": "Buscá en la tabla qué número da justo."},
"ojo": ["Para agrupar se divide.", "No se suma."],
"resumen": [{"titulo": "Agrupar", "texto": "Misma cantidad."}, {"titulo": "Contar", "texto": "Los grupos."}, {"titulo": "Dividir", "texto": "24 ÷ 4 = 6."}],
"glosario": [{"palabra": "Grupo", "significado": "Conjunto de cosas juntas."}, {"palabra": "Carpa", "significado": "Casa de tela para acampar."}],
"carpeta": ["¿Cuántos grupos de 3 se arman con 18 chicos?", "¿Cuántos grupos de 4 se arman con 28 chicos?", "Mía sumó 24 + 4 para carpas de 4 chicos. ¿Cuántas carpas son?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["6"], ["7"], ["6"]],
"soluciones": {"incompleto": "6. 6.", "solo": "3.", "carpeta": ["6.", "7.", "6."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a decidir qué hacer con lo que sobra.",
"vas_a_ver": ["El resto", "Menor que los grupos", "Depende de la situación"],
"secciones": [
 S(1, "Galletas", [
  P("23 galletas para 4 chicos."),
  P("5 a cada uno y sobran <b>3</b>."),
  IMG("23 ÷ 4", "5 a cada uno.", FG.grupos("caramelo", 4, 5, "sobran 3")),
 ]),
 S(1, "El resto", [
  D("Resto", "Lo que sobra y <b>no alcanza</b> para otra vuelta."),
  P("Siempre es menor que la cantidad de grupos."),
  IMG("Qué hacer", "Depende.", FG.cuentas([("galletas", "se parten"), ("chicos", "auto más")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los repartos. Los vas a usar en la carpeta."),
  IMG("Repartos", "¿Cuánto sobra?", FG.cuentas([("17 entre 3", "?"), ("29 entre 5", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Resto", "planteo": "14 globos entre 4 mesas.", "pasos": ["3 en cada mesa: 12.", "Sobran 2."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "19 lápices entre 6.", "pasos": ["___ a cada uno.", "Sobra ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "Si repartimos 25 entre 4, ¿cuánto sobra?"},
"tip": {"titulo": "Menor", "texto": "Si sobra mucho, da otra vuelta."},
"ojo": ["El resto es menor que los grupos.", "Con 7 entre 4 todavía da otra vuelta."],
"resumen": [{"titulo": "Resto", "texto": "Lo que sobra."}, {"titulo": "Menor", "texto": "Que los grupos."}, {"titulo": "Decidir", "texto": "Según el caso."}],
"glosario": [{"palabra": "Resto", "significado": "Lo que sobra."}, {"palabra": "Sobrar", "significado": "Quedar sin repartir."}],
"carpeta": ["Repartimos 17 entre 3. ¿Cuánto sobra?", "Repartimos 29 entre 5. ¿Cuánto sobra?", "Juan repartió 23 entre 4: dio 4 a cada uno y le sobraron 7. ¿Cuánto debía sobrar?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["2"], ["4"], ["3"]],
"soluciones": {"incompleto": "3. 1.", "solo": "1.", "carpeta": ["2.", "4.", "3: 5 a cada uno."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas de reparto con resto.",
"vas_a_ver": ["Dividir", "Mirar el resto", "Responder con sentido"],
"secciones": [
 S(1, "Autos para el paseo", [
  P("Van 26 chicos. En cada auto entran 4."),
  P("26 ÷ 4 = 6 y sobran 2. Hacen falta <b>7 autos</b>."),
  IMG("26 ÷ 4", "Uno más.", FG.cuentas([("26 ÷ 4", "6, sobran 2"), ("autos", 7)])),
 ]),
 S(1, "Decidir", [
  D("Problema con resto", "Dividimos y después <b>pensamos qué pasa</b> con lo que sobra."),
  P("30 globos en 4 mesas: 7 en cada una, sobran 2."),
  IMG("Globos", "Quedan guardados.", FG.cuentas([("30 ÷ 4", "7, sobran 2")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el problema. Lo vas a usar en la carpeta."),
  IMG("Bancos", "34 chicos, bancos de 3.", FG.cuentas([("34 ÷ 3", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Problema", "planteo": "19 chicos, mesas de 5.", "pasos": ["19 ÷ 5 = 3 y sobran 4.", "Hacen falta 4 mesas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "22 caramelos en bolsas de 5.", "pasos": ["Se llenan ___ bolsas.", "Sobran ___ ."]},
"ejemplo_solo": {"titulo": "Resolvé", "planteo": "33 libros en estantes de 8. ¿Cuántos estantes llenos?"},
"tip": {"titulo": "Pensá", "texto": "¿Lo que sobra necesita su lugar?"},
"ojo": ["Si sobran chicos, hace falta otro lugar.", "Respondé con una oración."],
"resumen": [{"titulo": "Dividir", "texto": "Primero."}, {"titulo": "Resto", "texto": "Mirarlo."}, {"titulo": "Responder", "texto": "Con sentido."}],
"glosario": [{"palabra": "Lugar", "significado": "Espacio para alguien."}, {"palabra": "Sentido", "significado": "Que es lógico."}],
"carpeta": ["Hay 34 chicos y en cada banco se sientan 3. ¿Cuántos bancos hacen falta?", "34 chicos en bancos de 3: ¿cuántos quedan en el último banco?", "Leo dice: 26 chicos, autos de 4, alcanzan 6. ¿Cuántos autos hacen falta?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["12"], ["1"], ["7"]],
"soluciones": {"incompleto": "4. 2.", "solo": "4.", "carpeta": ["12: 11 llenos y uno más.", "1.", "7."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("REPARTIR POR PARTES", [LD("PARTES FÁCILES", "SEPARAMOS UNA PARTE QUE SE REPARTE <b>JUSTO</b> Y DESPUÉS LO QUE QUEDA."),
   LL("CADA PARTE SE REPARTE APARTE.", "AL FINAL SE JUNTA LO QUE TOCA.")],
   {"modo": "divide3", "que": "grande"}, {"modo": "divide3", "que": "grande"}),
], "recuerda": [
 RC("REPARTIR", "DAR A CADA UNO LA MISMA CANTIDAD.", "39 ENTRE 3: 13 A CADA UNO"),
 RC("PARTIR", "SEPARAMOS EL NÚMERO EN PARTES QUE SE REPARTEN FÁCIL.", "86 = 80 + 6"),
]}
N2["leccion"] = {"temas": [
 T("ARMAR GRUPOS", [LD("DE A TANTOS", "LLENAMOS GRUPOS HASTA <b>NO TENER MÁS</b> Y LOS CONTAMOS."),
   LL("SE RESUELVE DIVIDIENDO.", "LA TABLA DICE EL NÚMERO EXACTO.")],
   {"modo": "divide3", "que": "grupos"}, {"modo": "divide3", "que": "grupos"}),
], "recuerda": [
 RC("AGRUPAR", "ARMAMOS GRUPOS IGUALES Y CONTAMOS CUÁNTOS SALEN.", "20 LÁPICES EN CAJAS DE 5: 4 CAJAS"),
 RC("TABLA", "BUSCAMOS QUÉ NÚMERO POR EL DEL GRUPO DA EL TOTAL.", "6 × 6 = 36: 6 CAJAS"),
]}
N3["leccion"] = {"temas": [
 T("LO QUE SOBRA", [LD("RESTO", "LO QUE QUEDA CUANDO <b>NO ALCANZA</b> PARA DAR OTRA VUELTA."),
   LL("ES MÁS CHICO QUE LA CANTIDAD DE GRUPOS.", "SE DECIDE QUÉ HACER CON ÉL.")],
   {"modo": "divide3"}, {"modo": "divide3"}),
], "recuerda": [
 RC("RESTO", "LO QUE SOBRA DESPUÉS DE REPARTIR EN PARTES IGUALES.", "14 ENTRE 4: 3 Y SOBRAN 2"),
 RC("MENOR", "EL RESTO SIEMPRE ES MÁS CHICO QUE LOS GRUPOS.", "19 ENTRE 6: SOBRA 1"),
]}
N4["leccion"] = {"temas": [
 T("¿Y LO QUE SOBRA?", [LD("PENSAR EL RESTO", "DESPUÉS DE DIVIDIR, VEMOS SI LO QUE SOBRA <b>NECESITA SU LUGAR</b>."),
   LL("SI SOBRAN PERSONAS, HACE FALTA UNO MÁS.", "SI SOBRAN COSAS, A VECES SE GUARDAN.")],
   {"modo": "divide3", "que": "problema"}, {"modo": "divide3", "que": "problema"}),
], "recuerda": [
 RC("PROBLEMA CON RESTO", "DIVIDIMOS Y DECIDIMOS QUÉ HACER CON LO QUE SOBRA.", "19 CHICOS EN MESAS DE 5: 4 MESAS"),
 RC("RESPONDER", "LA RESPUESTA TIENE QUE TENER SENTIDO EN LA HISTORIA.", "NO PUEDEN QUEDAR CHICOS SIN AUTO"),
]}

ACT = {
"1": [N("REPARTIMOS 39 ENTRE 3. ¿CUÁNTO LE TOCA A CADA UNO?", 13, "10 + 3.", n="aplicar"),
      FB("COMPLETÁ: 86 ÷ 2 = 40 + ___", [["3"]], "6 ÷ 2.", n="aplicar"),
      MC("LEO REPARTIÓ SOLO EL 80 DE 84 ENTRE 4. ¿CUÁNTO LE TOCA A CADA UNO?", ["21", "20", "80"], "21", "FALTA REPARTIR EL 4.", n="error"),
      UNIR("UNÍ CADA REPARTO CON LO QUE TOCA.", ["64 ÷ 2", "66 ÷ 3", "48 ÷ 4"], ["12", "32", "22"], {"64 ÷ 2": "32", "66 ÷ 3": "22", "48 ÷ 4": "12"}, "PARTÍ EN DECENAS Y UNIDADES.", n="analizar")],
"2": [N("¿CUÁNTAS CAJAS DE 5 SE ARMAN CON 20 LÁPICES?", 4, "5, 10, 15, 20.", n="aplicar"),
      N("¿CUÁNTOS EQUIPOS DE 7 SE ARMAN CON 21 CHICOS?", 3, "7 × 3 = 21.", n="aplicar"),
      MC("MÍA SUMÓ 24 + 4 PARA LAS CARPAS DE 4. ¿CUÁNTAS SON?", ["6", "28", "20"], "6", "SE DIVIDE.", n="error"),
      MC("«36 HUEVOS EN CAJAS DE 6», ¿QUÉ SE BUSCA?", ["CUÁNTAS CAJAS", "CUÁNTOS HUEVOS POR CAJA", "CUÁNTOS SOBRAN"], "CUÁNTAS CAJAS", "SABEMOS CUÁNTO VA EN CADA UNA.", n="analizar")],
"3": [N("REPARTIMOS 25 ENTRE 4. ¿CUÁNTO SOBRA?", 1, "6 A CADA UNO.", n="aplicar"),
      N("REPARTIMOS 14 GLOBOS ENTRE 4 MESAS. ¿CUÁNTOS EN CADA UNA?", 3, "SOBRAN 2.", n="aplicar"),
      MC("JUAN REPARTIÓ 23 ENTRE 4: DIO 4 Y SOBRARON 7. ¿ESTÁ BIEN?", ["NO: ALCANZA PARA DAR 5", "SÍ"], "NO: ALCANZA PARA DAR 5", "7 ES MÁS QUE 4.", n="error"),
      CLAS("¿QUÉ HACEMOS CON LO QUE SOBRA?", ["SOBRAN CHICOS", "SOBRA PIZZA", "SOBRAN PASAJEROS", "SOBRAN CARAMELOS"], ["HACE FALTA UNO MÁS", "SE GUARDA O SE PARTE"],
           {"SOBRAN CHICOS": "HACE FALTA UNO MÁS", "SOBRA PIZZA": "SE GUARDA O SE PARTE", "SOBRAN PASAJEROS": "HACE FALTA UNO MÁS", "SOBRAN CARAMELOS": "SE GUARDA O SE PARTE"}, "DEPENDE DE LA SITUACIÓN.", n="analizar")],
"4": [N("19 CHICOS Y MESAS DE 5. ¿CUÁNTAS MESAS HACEN FALTA?", 4, "3 LLENAS Y UNA MÁS.", n="aplicar"),
      N("[[problema]] 33 LIBROS EN ESTANTES DE 8. ¿CUÁNTOS ESTANTES QUEDAN LLENOS?", 4, "8 × 4 = 32.", n="analizar"),
      MC("LEO DICE: 26 CHICOS, AUTOS DE 4, ALCANZAN 6. ¿CUÁNTOS HACEN FALTA?", ["7", "6", "26"], "7", "LOS 2 QUE SOBRAN TAMBIÉN VIAJAN.", n="error"),
      ORD("ORDENÁ LOS PASOS.", ["RESPONDO", "DIVIDO", "MIRO EL RESTO"], ["DIVIDO", "MIRO EL RESTO", "RESPONDO"], "PRIMERO DIVIDIR.", n="recordar")],
"5": [N("RELÁMPAGO. 48 ÷ 4 = ___", 12, "12.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿CUÁNTOS GRUPOS DE 5 HAY EN 35?", 7, "7.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 17 ENTRE 3: ¿CUÁNTO SOBRA?", 2, "5 Y SOBRAN 2.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. EL RESTO ES…", ["MENOR QUE LOS GRUPOS", "MAYOR QUE LOS GRUPOS"], "MENOR QUE LOS GRUPOS", "SI NO, SE DA OTRA VUELTA.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("REPARTIMOS 64 ENTRE 2. ¿CUÁNTO LE TOCA A CADA UNO?", 32, "30 + 2.", n="aplicar")],
 [1, N("REPARTIMOS 55 ENTRE 5. ¿CUÁNTO LE TOCA A CADA UNO?", 11, "10 + 1.", n="aplicar")],
 [1, TF("PARA REPARTIR 84 ENTRE 4 ALCANZA CON REPARTIR EL 80.", "FALSO", "FALTA EL 4.", n="error")],
 [2, N("¿CUÁNTOS GRUPOS DE 3 SE ARMAN CON 18 CHICOS?", 6, "3 × 6 = 18.", n="aplicar")],
 [2, N("¿CUÁNTAS CAJAS DE 6 SE ARMAN CON 36 HUEVOS?", 6, "6 × 6 = 36.", n="aplicar")],
 [2, MC("ARMAR GRUPOS IGUALES ES UNA…", ["DIVISIÓN", "SUMA", "RESTA"], "DIVISIÓN", "24 ÷ 4 = 6.", n="recordar")],
 [3, N("REPARTIMOS 29 ENTRE 5. ¿CUÁNTO SOBRA?", 4, "5 × 5 = 25.", n="aplicar")],
 [3, MC("REPARTIMOS ENTRE 4. ¿PUEDEN SOBRAR 6?", ["NO", "SÍ"], "NO", "CON 6 SE DA OTRA VUELTA.", n="analizar")],
 [3, FB("COMPLETÁ: 19 ENTRE 6 = 3 Y SOBRA ___", [["1"]], "6 × 3 = 18.", n="aplicar")],
 [4, N("[[problema]] HAY 34 CHICOS Y EN CADA BANCO SE SIENTAN 3. ¿CUÁNTOS BANCOS HACEN FALTA?", 12, "11 LLENOS Y UNO MÁS.", n="analizar")],
 [4, N("22 CARAMELOS EN BOLSAS DE 5. ¿CUÁNTAS BOLSAS SE LLENAN?", 4, "5 × 4 = 20.", n="aplicar")],
 [4, MC("NICO DICE: 19 CHICOS, MESAS DE 5, ALCANZAN 3. ¿CUÁNTAS HACEN FALTA?", ["4", "3", "5"], "4", "LOS 4 QUE SOBRAN NECESITAN MESA.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 14, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: repartos y particiones", "examen_titulo": "Nivel jefe: repartos y particiones",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-14.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
