# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 13 · La multiplicación como suma repetida. Genera mision-13.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (bandejas con la misma cantidad).
Niveles: 1 sumar muchas veces lo mismo · 2 series de números · 3 escribir con multiplicación · 4 problemas de grupos iguales."""
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
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a sumar muchas veces el mismo número.",
"vas_a_ver": ["Grupos iguales", "Sumar lo mismo", "Contar los grupos"],
"secciones": [
 S(1, "Bandejas iguales", [
  P("Rosa pone 4 alfajores en cada bandeja. Llenó 3 bandejas."),
  D("Grupos iguales", "Todos los grupos tienen la <b>misma cantidad</b>."),
  P("4 + 4 + 4 = <b>12</b>."),
  IMG("Tres bandejas de 4", "4, 8, 12.", FG.grupos("manzana", 3, 4, "4 + 4 + 4 = 12")),
 ]),
 S(1, "Contar los grupos", [
  P("Hay que mirar dos cosas: <b>cuántos grupos</b> y <b>cuántos en cada uno</b>."),
  P("5 bandejas de 2: 2 + 2 + 2 + 2 + 2 = <b>10</b>."),
  IMG("Cinco bandejas de 2", "2, 4, 6, 8, 10.", FG.grupos("estrella", 5, 2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bandejas. Las vas a usar en la carpeta."),
  IMG("Bandejas de Rosa", "Contá grupos y objetos.", FG.grupos("caramelo", 4, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "Platos con galletitas", "planteo": "Hay 3 platos con 5 galletitas cada uno.", "pasos": ["5 + 5 + 5.", "5, 10, 15.", "Hay 15 galletitas."]},
"ejemplo_incompleto": {"titulo": "Bolsitas", "planteo": "4 bolsitas de 2 caramelos. Completá.", "pasos": ["2 + 2 + 2 + 2 = ___ .", "Hay ___ caramelos."]},
"ejemplo_solo": {"titulo": "Tus grupos", "planteo": "Hay 2 cajas con 10 lápices cada una. ¿Cuántos lápices hay?"},
"tip": {"titulo": "Contá saltando", "texto": "Si cada grupo tiene 4, contá 4, 8, 12."},
"ojo": ["Los grupos tienen que ser iguales.", "No sumes los grupos: sumá lo que hay en cada uno."],
"resumen": [{"titulo": "Grupos iguales", "texto": "Misma cantidad."}, {"titulo": "Sumar", "texto": "Lo mismo varias veces."}, {"titulo": "Mirar", "texto": "Grupos y cuántos en cada uno."}],
"glosario": [{"palabra": "Grupo", "significado": "Cosas que van juntas."}, {"palabra": "Igual", "significado": "La misma cantidad."}],
"carpeta": ["¿Cuántas bandejas hay?", "¿Cuántos caramelos hay en cada bandeja?", "¿Cuántos caramelos hay en total?"],
"carpeta_nivel": ["recordar", "recordar", "aplicar"],
"respuestas_carpeta": [["4"], ["3"], ["12"]],
"soluciones": {"incompleto": "8. 8.", "solo": "20.", "carpeta": ["4.", "3.", "12: 3 + 3 + 3 + 3."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar saltando de 2, de 5 y de 10.",
"vas_a_ver": ["De 2 en 2", "De 5 en 5", "De 10 en 10"],
"secciones": [
 S(1, "Contar saltando", [
  P("Los alfajores vienen de a 2: <b>2, 4, 6, 8, 10</b>."),
  D("Serie", "Una serie salta siempre <b>lo mismo</b>."),
  IMG("De 2 en 2", "2, 4, 6, 8, 10.", FG.recta_num(0, 10, marcas=[(2, ""), (4, ""), (6, ""), (8, ""), (10, "")], flechas=[(0, 2), (2, 4), (4, 6), (6, 8), (8, 10)])),
 ]),
 S(1, "De 5 y de 10", [
  P("De 5 en 5: <b>5, 10, 15, 20, 25</b>."),
  P("De 10 en 10: <b>10, 20, 30, 40, 50</b>."),
  IMG("De 5 en 5", "Cada vagón suma 5.", FG.tren_paso(5, 30, 5)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Vagones vacíos", "De 5 en 5.", FG.tren_paso(5, 40, 5, faltan=(20, 35))),
 ]),
],
"ejemplo_completo": {"titulo": "De 2 en 2", "planteo": "Contá los pares de zapatillas: 4 pares.", "pasos": ["2, 4, 6, 8.", "Hay 8 zapatillas."]},
"ejemplo_incompleto": {"titulo": "De 10 en 10", "planteo": "Completá.", "pasos": ["10, 20, ___ , 40.", "40, ___ , 60."]},
"ejemplo_solo": {"titulo": "Tu serie", "planteo": "Contá de 5 en 5 hasta 50."},
"tip": {"titulo": "Mirá el salto", "texto": "Siempre se suma el mismo número."},
"ojo": ["De 5 en 5 los números terminan en 5 o en 0.", "De 2 en 2 los números son pares."],
"resumen": [{"titulo": "De 2 en 2", "texto": "2, 4, 6, 8."}, {"titulo": "De 5 en 5", "texto": "5, 10, 15, 20."}, {"titulo": "De 10 en 10", "texto": "10, 20, 30, 40."}],
"glosario": [{"palabra": "Serie", "significado": "Números que saltan lo mismo."}, {"palabra": "Par", "significado": "Número de la serie del 2."}],
"carpeta": ["En el tren, ¿qué número falta después del 15?", "¿Qué número falta después del 30?", "Tomi contó de 5 en 5: 5, 10, 15, 21. ¿Qué número va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["20"], ["35"], ["20"]],
"soluciones": {"incompleto": "30. 50.", "solo": "5, 10, 15, 20, 25, 30, 35, 40, 45, 50.", "carpeta": ["20.", "35.", "20: después del 15 viene el 20."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir sumas repetidas con el signo ×.",
"vas_a_ver": ["Veces", "El signo por", "De la suma a la multiplicación"],
"secciones": [
 S(1, "Veces", [
  P("4 + 4 + 4 es sumar <b>3 veces 4</b>."),
  D("Multiplicación", "Se escribe <b>3 × 4</b> y se lee «3 por 4». Da 12."),
  IMG("3 veces 4", "3 × 4 = 12.", FG.grupos("manzana", 3, 4, "3 × 4 = 12")),
 ]),
 S(1, "De la suma a la multiplicación", [
  P("2 + 2 + 2 + 2 + 2 es <b>5 × 2</b> = 10."),
  P("10 + 10 + 10 es <b>3 × 10</b> = 30."),
  IMG("Sumas y multiplicaciones", "Lo mismo, escrito más corto.", FG.cuentas([("5 × 2", 10), ("3 × 10", 30), ("4 × 5", 20)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bandejas. Las vas a usar en la carpeta."),
  IMG("Bandejas para escribir", "¿Cuántas veces? ¿Cuántos?", FG.grupos("pelota", 2, 5)),
 ]),
],
"ejemplo_completo": {"titulo": "6 + 6", "planteo": "Escribí con ×.", "pasos": ["Sumo 2 veces 6.", "Se escribe 2 × 6.", "2 × 6 = 12."]},
"ejemplo_incompleto": {"titulo": "5 + 5 + 5 + 5", "planteo": "Completá.", "pasos": ["Son ___ veces 5.", "Se escribe ___ × 5 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu multiplicación", "planteo": "Escribí 3 + 3 + 3 + 3 con el signo ×."},
"tip": {"titulo": "Contá las veces", "texto": "Primero cuántas veces, después cuánto."},
"ojo": ["3 × 4 no es 3 + 4.", "El × se lee «por»."],
"resumen": [{"titulo": "Veces", "texto": "Cuántos grupos."}, {"titulo": "×", "texto": "Se lee «por»."}, {"titulo": "3 × 4", "texto": "4 + 4 + 4 = 12."}],
"glosario": [{"palabra": "Multiplicación", "significado": "Sumar varias veces lo mismo."}, {"palabra": "Por", "significado": "Cómo se lee el ×."}],
"carpeta": ["¿Cuántas bandejas hay?", "¿Cuántas pelotas hay en total?", "Sofi dice que 2 × 5 = 7. ¿Cuánto da?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["2"], ["10"], ["10"]],
"soluciones": {"incompleto": "4. 4 × 5 = 20.", "solo": "4 × 3 = 12.", "carpeta": ["2.", "10: 2 × 5.", "10: Sofi sumó 2 + 5."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas con grupos iguales.",
"vas_a_ver": ["Encontrar los grupos", "Cuántos en cada grupo", "Resolver con ×"],
"secciones": [
 S(1, "Encontrar los grupos", [
  P("Rosa arma 5 cajitas con 2 alfajores cada una. ¿Cuántos usa?"),
  D("Problema de grupos", "Buscamos <b>cuántos grupos</b> y <b>cuántos en cada uno</b>."),
  P("5 grupos de 2: 5 × 2 = <b>10</b>."),
  IMG("Cinco cajitas", "5 × 2 = 10.", FG.grupos("caramelo", 5, 2, "5 × 2 = 10")),
 ]),
 S(1, "Otro problema", [
  P("Tomi tiene 4 bolsas con 10 figuritas. 4 × 10 = <b>40</b>."),
  P("Respondemos: Tomi tiene 40 figuritas."),
  IMG("Bolsas de 10", "10, 20, 30, 40.", FG.tren_paso(10, 40, 10)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bandejas. Las vas a usar en la carpeta."),
  IMG("Las bandejas de Rosa", "¿Cuántos alfajores hay?", FG.grupos("manzana", 3, 5)),
 ]),
],
"ejemplo_completo": {"titulo": "Las mesas", "planteo": "Hay 3 mesas con 4 sillas cada una. ¿Cuántas sillas?", "pasos": ["3 grupos de 4.", "3 × 4 = 12.", "Hay 12 sillas."]},
"ejemplo_incompleto": {"titulo": "Los autos", "planteo": "2 autos con 4 ruedas. Completá.", "pasos": ["Son ___ grupos de 4.", "2 × 4 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Hay 5 manos. ¿Cuántos dedos hay?"},
"tip": {"titulo": "Grupos × cantidad", "texto": "Cuántos grupos, por cuántos en cada uno."},
"ojo": ["No sumes grupos y cantidad.", "Escribí la respuesta con palabras."],
"resumen": [{"titulo": "Grupos", "texto": "¿Cuántos hay?"}, {"titulo": "Cada uno", "texto": "¿Cuántos tiene?"}, {"titulo": "×", "texto": "Grupos por cantidad."}],
"glosario": [{"palabra": "Cada uno", "significado": "Lo que tiene un grupo."}, {"palabra": "Total", "significado": "Todo junto."}],
"carpeta": ["¿Cuántas bandejas hay?", "¿Cuántos alfajores hay en total?", "Tomi dice que son 8. ¿Qué hizo mal?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["3"], ["15"], ["sumó", "sumó 3 + 5", "sumo"]],
"soluciones": {"incompleto": "2. 8.", "solo": "25: 5 × 5.", "carpeta": ["3.", "15: 3 × 5.", "Sumó 3 + 5 en vez de multiplicar."]},
}

ACT = {
"1": [N("3 BANDEJAS CON 4 ALFAJORES CADA UNA. ¿CUÁNTOS SON?", 12, "4 + 4 + 4 = 12.", n="aplicar"),
      TF("2 + 2 + 2 ES SUMAR VARIAS VECES LO MISMO.", "VERDADERO", "TRES VECES 2.", n="recordar")],
"2": [N("DE 5 EN 5: 5, 10, 15, ___", 20, "SUMAMOS 5.", n="aplicar"),
      UNI("UNÍ CADA SERIE CON SU SALTO.", [("2, 4, 6", "DE 2 EN 2"), ("5, 10, 15", "DE 5 EN 5"), ("10, 20, 30", "DE 10 EN 10")], "MIRÁ CUÁNTO SALTA.", n="analizar")],
"3": [MC("¿CÓMO SE ESCRIBE 4 + 4 + 4?", ["3 POR 4", "4 POR 4", "3 MÁS 4"], "3 POR 4", "TRES VECES 4.", n="aplicar"),
      N("¿CUÁNTO ES 5 × 2?", 10, "2 + 2 + 2 + 2 + 2 = 10.", n="aplicar")],
"4": [N("ROSA ARMA 4 CAJITAS CON 5 ALFAJORES. ¿CUÁNTOS USA?", 20, "4 × 5 = 20.", n="aplicar"),
      MC("3 MESAS CON 4 SILLAS. ¿QUÉ CUENTA HAGO?", ["3 POR 4", "3 MÁS 4", "4 MENOS 3"], "3 POR 4", "3 GRUPOS DE 4.", n="analizar")],
"5": [N("RELÁMPAGO. 10 + 10 + 10 = ___", 30, "3 VECES 10.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. DE 2 EN 2: 2, 4, 6, ___", 8, "SUMAMOS 2.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 2 × 5 = ___", 10, "5 + 5.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. 3 × 4 SE LEE…", ["3 POR 4", "3 MÁS 4"], "3 POR 4", "EL × SE LEE POR.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("5 BOLSITAS CON 2 CARAMELOS. ¿CUÁNTOS CARAMELOS?", 10, "2 + 2 + 2 + 2 + 2.", n="aplicar")],
 [1, TF("3 BANDEJAS DE 4 Y 3 BANDEJAS DE 5 SON GRUPOS IGUALES.", "FALSO", "UNAS TIENEN 4 Y OTRAS 5.", n="analizar")],
 [1, N("4 PLATOS CON 3 GALLETITAS. ¿CUÁNTAS GALLETITAS?", 12, "3 + 3 + 3 + 3 = 12.", n="aplicar")],
 [2, N("DE 10 EN 10: 10, 20, 30, ___", 40, "SUMAMOS 10.", n="aplicar")],
 [2, N("DE 2 EN 2: 10, 12, 14, ___", 16, "SUMAMOS 2.", n="aplicar")],
 [2, TF("TOMI CONTÓ DE 5 EN 5: 5, 10, 15, 21.", "FALSO", "DESPUÉS DEL 15 VIENE EL 20.", n="error")],
 [3, MC("¿CÓMO SE ESCRIBE 2 + 2 + 2 + 2?", ["4 POR 2", "2 POR 2", "4 MÁS 2"], "4 POR 2", "CUATRO VECES 2.", n="aplicar")],
 [3, N("¿CUÁNTO ES 3 × 10?", 30, "10 + 10 + 10.", n="aplicar")],
 [3, MC("SOFI DICE: 2 × 5 = 7. ¿QUÉ HIZO?", ["SUMÓ 2 + 5", "MULTIPLICÓ BIEN", "RESTÓ"], "SUMÓ 2 + 5", "2 × 5 = 10.", n="error")],
 [4, N("HAY 5 MANOS. ¿CUÁNTOS DEDOS?", 25, "5 × 5 = 25.", n="aplicar")],
 [4, N("2 AUTOS CON 4 RUEDAS. ¿CUÁNTAS RUEDAS?", 8, "2 × 4 = 8.", n="aplicar")],
 [4, UNI("UNÍ CADA PROBLEMA CON SU CUENTA.", [("3 MESAS DE 4 SILLAS", "3 × 4"), ("4 BOLSAS DE 10", "4 × 10"), ("5 CAJITAS DE 2", "5 × 2")], "GRUPOS POR CANTIDAD.", n="analizar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 13, "estilo": "primeros",
     "practica": "Práctica general: la multiplicación como suma repetida", "examen_titulo": "Nivel jefe: la multiplicación como suma repetida",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-13.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
