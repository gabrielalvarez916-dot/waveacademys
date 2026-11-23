# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 11 · Problemas de suma y resta. Genera mision-11.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (pedidos que llegan y se van).
Niveles: 1 agregar y quitar · 2 comparar · 3 completar hasta un número · 4 problemas con varias cuentas."""
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
UNI = lambda p, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": [a for a, _ in pares], "derecha": [b for _, b in pares]}, "r": {"pares": dict(pares)}, "e": e, **k}
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a saber cuándo un problema se resuelve sumando o restando.",
"vas_a_ver": ["Agregar es sumar", "Quitar es restar", "Las palabras que ayudan"],
"secciones": [
 S(1, "Agregar", [
  P("Rosa tenía 230 alfajores. Hizo 150 más."),
  D("Agregar", "Si llegan más, <b>sumamos</b>: 230 + 150 = <b>380</b>."),
  IMG("Llegan más", "230 + 150 = 380.", FG.columnas(230, 150, "+", 380)),
 ]),
 S(1, "Quitar", [
  P("Rosa tenía 380 alfajores. Vendió 120."),
  D("Quitar", "Si se van, <b>restamos</b>: 380 − 120 = <b>260</b>."),
  IMG("Se van", "380 − 120 = 260.", FG.columnas(380, 120, "−", 260)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("¿Suma o resta?", "Leé el problema y elegí.", FG.cuentas([("250 + 140", 390), ("470 − 130", 340)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Un problema", "planteo": "Tomi tenía 125 figuritas. Le regalaron 40. ¿Cuántas tiene?", "pasos": ["Le regalaron: llegan más.", "Sumamos: 125 + 40.", "Tiene 165 figuritas."]},
"ejemplo_incompleto": {"titulo": "Otro problema", "planteo": "En el colectivo iban 48 personas. Bajaron 15. Completá.", "pasos": ["Bajaron: se van. Hay que ___ .", "48 − 15 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Rosa tenía 300 alfajores y hizo 200 más. ¿Cuántos tiene?"},
"tip": {"titulo": "Pensá qué pasa", "texto": "¿Llegan más o se van?"},
"ojo": ["No sumes siempre: mirá si se van.", "Escribí la respuesta con palabras."],
"resumen": [{"titulo": "Agregar", "texto": "Llegan más: sumamos."}, {"titulo": "Quitar", "texto": "Se van: restamos."}, {"titulo": "Respuesta", "texto": "Con palabras."}],
"glosario": [{"palabra": "Problema", "significado": "Una pregunta que se resuelve con cuentas."}, {"palabra": "Respuesta", "significado": "Lo que contesta la pregunta."}],
"carpeta": ["Rosa tenía 250 alfajores y hizo 140 más. ¿Cuántos tiene?", "Rosa tenía 470 y vendió 130. ¿Cuántos le quedan?", "Tomi resolvió el segundo sumando. ¿Cuánto da bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["390"], ["340"], ["340"]],
"soluciones": {"incompleto": "Restar. 33.", "solo": "500.", "carpeta": ["390.", "340.", "340: vendió, entonces se resta."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a comparar dos cantidades: cuánto más y cuánto menos.",
"vas_a_ver": ["¿Quién tiene más?", "¿Cuántos más?", "Comparar restando"],
"secciones": [
 S(1, "¿Quién tiene más?", [
  P("Rosa hizo 450 alfajores. Ana hizo 320."),
  P("450 es más que 320: Rosa hizo <b>más</b>."),
  IMG("Dos pedidos", "450 y 320.", FG.camiones([450, 320])),
 ]),
 S(1, "¿Cuántos más?", [
  D("Comparar", "Para saber <b>cuántos más</b>, restamos el chico al grande."),
  P("450 − 320 = <b>130</b>. Rosa hizo 130 más."),
  IMG("La diferencia", "450 − 320 = 130.", FG.columnas(450, 320, "−", 130)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los camiones. Los vas a usar en la carpeta."),
  IMG("Dos camiones", "¿Cuál lleva más?", FG.camiones([580, 350])),
 ]),
],
"ejemplo_completo": {"titulo": "¿Cuántos menos?", "planteo": "Tomi tiene 85 figuritas. Sofi tiene 60. ¿Cuántas menos tiene Sofi?", "pasos": ["Restamos el chico al grande.", "85 − 60 = 25.", "Sofi tiene 25 menos."]},
"ejemplo_incompleto": {"titulo": "Comparar", "planteo": "Un camión lleva 760. Otro lleva 540. Completá.", "pasos": ["El que lleva más es el de ___ .", "760 − 540 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Rosa hizo 300 y Ana 200. ¿Cuántos más hizo Rosa?"},
"tip": {"titulo": "Grande menos chico", "texto": "La diferencia se encuentra restando."},
"ojo": ["«Cuántos más» no siempre es sumar.", "Restá el grande menos el chico."],
"resumen": [{"titulo": "Más", "texto": "El número más grande."}, {"titulo": "Cuántos más", "texto": "Restamos."}, {"titulo": "Diferencia", "texto": "Lo que hay de más."}],
"glosario": [{"palabra": "Diferencia", "significado": "Cuánto más tiene uno que otro."}, {"palabra": "Comparar", "significado": "Ver cuál es más."}],
"carpeta": ["¿Cuál camión lleva más alfajores?", "¿Cuántos más lleva?", "Sofi dice que lleva 930 más. ¿Cuántos más lleva de verdad?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["580", "el de 580"], ["230"], ["230"]],
"soluciones": {"incompleto": "760. 220.", "solo": "100.", "carpeta": ["El de 580.", "230.", "230: Sofi sumó en vez de restar."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a encontrar cuánto falta para llegar a un número.",
"vas_a_ver": ["¿Cuánto falta?", "Contar para adelante", "Restar para saber"],
"secciones": [
 S(1, "¿Cuánto falta?", [
  P("Rosa tiene que entregar 500 alfajores. Ya hizo 350."),
  D("Cuánto falta", "Contamos <b>desde lo que hay</b> hasta lo que queremos."),
  P("De 350 a 400 hay 50. De 400 a 500 hay 100. Faltan <b>150</b>."),
  IMG("De 350 a 500", "50 + 100 = 150.", FG.recta_cien([(350, "350"), (500, "500")])),
 ]),
 S(1, "Restar para saber", [
  P("También se puede restar: 500 − 350 = <b>150</b>."),
  IMG("La resta", "500 − 350 = 150.", FG.columnas(500, 350, "−", 150, marcas=[("D", "10")], tachar=[("C", "4")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la recta. La vas a usar en la carpeta."),
  IMG("¿Cuánto falta?", "De 600 a 1.000.", FG.recta_cien([(600, "600"), (1000, "1.000")])),
 ]),
],
"ejemplo_completo": {"titulo": "Juntar 100", "planteo": "Tomi tiene 70 figuritas. Quiere 100. ¿Cuántas le faltan?", "pasos": ["Desde 70: 80, 90, 100.", "Son 3 saltos de 10.", "Le faltan 30."]},
"ejemplo_incompleto": {"titulo": "Llegar a 800", "planteo": "Hay 500. Quiero 800. Completá.", "pasos": ["Desde 500: 600, 700, ___ .", "Faltan ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Rosa hizo 250. Tiene que hacer 300. ¿Cuántos le faltan?"},
"tip": {"titulo": "Desde lo que hay", "texto": "Contá hasta lo que querés."},
"ojo": ["Faltan no siempre es sumar los dos.", "Contá los saltos, no los números."],
"resumen": [{"titulo": "Falta", "texto": "Lo que hay que agregar."}, {"titulo": "Contar", "texto": "Desde lo que hay."}, {"titulo": "Restar", "texto": "Lo que quiero − lo que hay."}],
"glosario": [{"palabra": "Faltar", "significado": "No estar todavía."}, {"palabra": "Completar", "significado": "Llegar a lo que queremos."}],
"carpeta": ["Rosa tiene 600 y quiere 1.000. ¿Cuántos le faltan?", "Tiene 750 y quiere 1.000. ¿Cuántos le faltan?", "Tomi dice que de 600 a 1.000 faltan 1.600. ¿Cuántos faltan?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["400"], ["250"], ["400"]],
"soluciones": {"incompleto": "800. 300.", "solo": "50.", "carpeta": ["400.", "250.", "400: Tomi sumó los dos."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas que necesitan dos cuentas.",
"vas_a_ver": ["Leer todo el problema", "Primera cuenta", "Segunda cuenta"],
"secciones": [
 S(1, "Dos cuentas", [
  P("Rosa tenía 400 alfajores. Hizo 200 más. Después vendió 350."),
  D("Problema de dos pasos", "Hacemos <b>una cuenta</b> y con ese resultado, <b>otra</b>."),
  P("400 + 200 = 600. Después 600 − 350 = <b>250</b>."),
  IMG("Paso por paso", "Primero sumo, después resto.", FG.cuentas([("400 + 200", 600), ("600 − 350", 250)])),
 ]),
 S(1, "Ordenar los pasos", [
  P("Leé todo el problema antes de empezar."),
  P("Anotá qué pasa primero y qué pasa después."),
  IMG("Los camiones", "Llega uno, se va otro.", FG.camiones([400, 200, 350])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Dos pasos", "Completá las cuentas.", FG.cuentas([("150 + 250", 400), ("400 − 120", 280)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "En el colectivo", "planteo": "Iban 30. Subieron 15. Bajaron 20. ¿Cuántos van?", "pasos": ["30 + 15 = 45.", "45 − 20 = 25.", "Van 25 personas."]},
"ejemplo_incompleto": {"titulo": "Las figuritas", "planteo": "Tomi tenía 50. Ganó 30. Regaló 10. Completá.", "pasos": ["50 + 30 = ___ .", "___ − 10 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Rosa tenía 300. Hizo 100. Vendió 250. ¿Cuántos tiene?"},
"tip": {"titulo": "Paso por paso", "texto": "Usá el resultado de la primera cuenta en la segunda."},
"ojo": ["No te quedes con la primera cuenta.", "Fijate qué pasa primero."],
"resumen": [{"titulo": "Leer", "texto": "Todo el problema."}, {"titulo": "Primer paso", "texto": "Una cuenta."}, {"titulo": "Segundo paso", "texto": "Con ese resultado."}],
"glosario": [{"palabra": "Paso", "significado": "Cada cuenta del problema."}, {"palabra": "Resultado", "significado": "Lo que da una cuenta."}],
"carpeta": ["Rosa tenía 150 y hizo 250. ¿Cuántos tiene?", "Después vende 120. ¿Cuántos le quedan?", "Sofi contestó 400. ¿Qué se olvidó?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["400"], ["280"], ["restar", "restar 120", "la segunda cuenta"]],
"soluciones": {"incompleto": "80. 80 − 10 = 70.", "solo": "150.", "carpeta": ["400.", "280.", "Se olvidó de restar los 120."]},
}

ACT = {
"1": [N("ROSA TENÍA 230 ALFAJORES Y HIZO 150 MÁS. ¿CUÁNTOS TIENE?", 380, "LLEGAN MÁS: SUMAMOS.", n="aplicar"),
      UNI("UNÍ CADA PROBLEMA CON SU CUENTA.", [("LLEGAN MÁS", "SUMA"), ("SE VAN", "RESTA")], "AGREGAR ES SUMAR, QUITAR ES RESTAR.", n="analizar")],
"2": [N("ROSA HIZO 450 Y ANA 320. ¿CUÁNTOS MÁS HIZO ROSA?", 130, "450 − 320 = 130.", n="aplicar"),
      TF("PARA SABER CUÁNTOS MÁS, SIEMPRE SE SUMA.", "FALSO", "SE RESTA EL CHICO AL GRANDE.", n="error")],
"3": [N("ROSA TIENE 350 Y QUIERE 500. ¿CUÁNTOS LE FALTAN?", 150, "DE 350 A 500 HAY 150.", n="aplicar"),
      MC("TOMI TIENE 70 Y QUIERE 100. ¿QUÉ CUENTA SIRVE?", ["RESTAR 100 MENOS 70", "SUMAR 100 MÁS 70", "RESTAR 70 MENOS 100"], "RESTAR 100 MENOS 70", "LO QUE QUIERO MENOS LO QUE HAY.", n="analizar")],
"4": [N("ROSA TENÍA 400, HIZO 200 Y VENDIÓ 350. ¿CUÁNTOS TIENE?", 250, "400 + 200 = 600. 600 − 350 = 250.", n="aplicar"),
      ORD("ORDENÁ LOS PASOS DEL PROBLEMA.", ["RESTO LO QUE VENDIÓ", "LEO TODO", "SUMO LO QUE HIZO"], ["LEO TODO", "SUMO LO QUE HIZO", "RESTO LO QUE VENDIÓ"], "PRIMERO LEO, DESPUÉS CADA PASO.", n="analizar")],
"5": [N("RELÁMPAGO. TENÍA 200 Y LLEGARON 300. ¿CUÁNTOS HAY?", 500, "200 + 300.", tiempo=40, n="aplicar"),
      N("RELÁMPAGO. TENÍA 600 Y SE FUERON 200. ¿CUÁNTOS QUEDAN?", 400, "600 − 200.", tiempo=40, n="aplicar"),
      N("RELÁMPAGO. HAY 80 Y QUIERO 100. ¿CUÁNTOS FALTAN?", 20, "80, 90, 100.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. «SE FUERON» ES…", ["RESTAR", "SUMAR"], "RESTAR", "QUITAR ES RESTAR.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("EN LA FÁBRICA HAY 320 ALFAJORES. HACEN 250 MÁS. ¿CUÁNTOS HAY?", 570, "320 + 250 = 570.", n="aplicar")],
 [1, N("HABÍA 680 ALFAJORES. SE VENDIERON 250. ¿CUÁNTOS QUEDAN?", 430, "680 − 250 = 430.", n="aplicar")],
 [1, MC("«SE VENDIERON 250». ¿QUÉ CUENTA HAGO?", ["RESTA", "SUMA"], "RESTA", "SE VAN: RESTAMOS.", n="analizar")],
 [2, N("UN CAMIÓN LLEVA 760 Y OTRO 540. ¿CUÁNTOS MÁS LLEVA EL PRIMERO?", 220, "760 − 540 = 220.", n="aplicar")],
 [2, TF("SI ROSA HIZO 300 Y ANA 200, ROSA HIZO 500 MÁS.", "FALSO", "300 − 200 = 100 MÁS.", n="error")],
 [2, MC("TOMI TIENE 85 Y SOFI 60. ¿QUIÉN TIENE MÁS?", ["TOMI", "SOFI"], "TOMI", "85 ES MÁS QUE 60.", n="recordar")],
 [3, N("ROSA TIENE 750 Y QUIERE 1000. ¿CUÁNTOS LE FALTAN?", 250, "1000 − 750 = 250.", n="aplicar")],
 [3, N("HAY 400 Y QUIERO 900. ¿CUÁNTOS FALTAN?", 500, "500, 600, 700, 800, 900.", n="aplicar")],
 [3, TF("TOMI DICE: DE 600 A 1000 FALTAN 1600.", "FALSO", "FALTAN 400.", n="error")],
 [4, N("IBAN 30 PERSONAS. SUBIERON 15 Y BAJARON 20. ¿CUÁNTAS VAN?", 25, "30 + 15 = 45. 45 − 20 = 25.", n="aplicar")],
 [4, N("ROSA TENÍA 300, HIZO 100 Y VENDIÓ 250. ¿CUÁNTOS TIENE?", 150, "300 + 100 = 400. 400 − 250 = 150.", n="aplicar")],
 [4, MC("EN UN PROBLEMA DE DOS PASOS, ¿QUÉ HACÉS CON EL PRIMER RESULTADO?", ["LO USO EN LA OTRA CUENTA", "LO TACHO", "ES LA RESPUESTA"], "LO USO EN LA OTRA CUENTA", "PASO POR PASO.", n="analizar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 11, "estilo": "primeros",
     "practica": "Práctica general: problemas de suma y resta", "examen_titulo": "Nivel jefe: problemas de suma y resta",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-11.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
