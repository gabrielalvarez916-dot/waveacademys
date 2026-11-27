# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 13 · Organizaciones rectangulares. Genera mision-13.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la feria de la escuela.
Niveles: 1 filas y columnas · 2 arreglos grandes · 3 combinar · 4 problemas de combinaciones."""
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
"objetivo": "Vas a contar cosas ordenadas en filas y columnas.",
"vas_a_ver": ["Filas iguales", "Filas por columnas", "Girar el rectángulo"],
"secciones": [
 S(1, "Sillas de la feria", [
  P("Las sillas están en 3 filas de 5."),
  P("5, 10, 15: <b>3 × 5 = 15</b>."),
  IMG("3 filas de 5", "Un rectángulo.", FG.arreglo("pelota", 3, 5, "3 × 5 = 15")),
 ]),
 S(1, "Filas por columnas", [
  D("Organización rectangular", "Cosas en <b>filas y columnas</b> iguales: filas por columnas."),
  P("Si lo giramos, 5 × 3 también da 15."),
  IMG("5 filas de 3", "Girado.", FG.arreglo("pelota", 5, 3, "5 × 3 = 15")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el rectángulo. Lo vas a usar en la carpeta."),
  IMG("Rectángulo", "Contá filas y columnas.", FG.arreglo("estrella", 4, 6)),
 ]),
],
"ejemplo_completo": {"titulo": "Contar", "planteo": "2 filas de 7.", "pasos": ["7, 14.", "2 × 7 = 14."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "4 filas de 5.", "pasos": ["5, 10, 15, ___ .", "4 × 5 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuántas sillas hay en 6 filas de 3?"},
"tip": {"titulo": "Girar", "texto": "Si se gira el rectángulo, da lo mismo."},
"ojo": ["3 filas de 5 no es 8.", "Se multiplica."],
"resumen": [{"titulo": "Rectángulo", "texto": "Filas y columnas."}, {"titulo": "Multiplicar", "texto": "Filas × columnas."}, {"titulo": "Girar", "texto": "Igual."}],
"glosario": [{"palabra": "Fila", "significado": "Cosas una al lado de otra."}, {"palabra": "Columna", "significado": "Cosas una debajo de otra."}],
"carpeta": ["Hay 4 filas con 6 estrellas cada una. ¿Cuántas estrellas hay?", "Si las ponemos en 6 filas de 4, ¿cuántas hay?", "Leo sumó 4 + 6 para 4 filas de 6. ¿Cuántas hay?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["24"], ["24"], ["24"]],
"soluciones": {"incompleto": "20. 20.", "solo": "18.", "carpeta": ["24.", "24: da lo mismo.", "24."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar arreglos grandes.",
"vas_a_ver": ["Partir las filas", "10 y el resto", "Sumar las partes"],
"secciones": [
 S(1, "El teatro", [
  P("Hay 12 filas de 8 butacas."),
  P("10 × 8 = 80 y 2 × 8 = 16. Son <b>96</b>."),
  IMG("12 × 8", "10 filas y 2 filas.", FG.cuentas([("10 × 8", 80), ("2 × 8", 16), ("80 + 16", 96)])),
 ]),
 S(1, "Partir", [
  D("Arreglo grande", "Partimos las filas en <b>10 y el resto</b>, multiplicamos y sumamos."),
  P("15 filas de 4: 40 + 20 = 60."),
  IMG("15 × 4", "Dos partes.", FG.cuentas([("10 × 4", 40), ("5 × 4", 20)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Teatros", "Partí las filas.", FG.cuentas([("13 filas de 6", "?"), ("11 filas de 9", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Partir", "planteo": "14 filas de 5.", "pasos": ["10 × 5 = 50. 4 × 5 = 20.", "Son 70."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "16 filas de 3.", "pasos": ["10 × 3 = ___ . 6 × 3 = ___ .", "Son 48."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuántas butacas hay en 18 filas de 2?"},
"tip": {"titulo": "Diez", "texto": "Las primeras 10 filas son fáciles."},
"ojo": ["No te olvides del resto de las filas.", "Sumá las dos partes."],
"resumen": [{"titulo": "Partir", "texto": "10 y el resto."}, {"titulo": "Multiplicar", "texto": "Cada parte."}, {"titulo": "Sumar", "texto": "Todo."}],
"glosario": [{"palabra": "Butaca", "significado": "Asiento del teatro."}, {"palabra": "Partir", "significado": "Separar en partes."}],
"carpeta": ["¿Cuántas butacas hay en 13 filas de 6?", "¿Cuántas butacas hay en 11 filas de 9?", "Mía hizo 12 filas de 8 = 80. ¿Cuántas hay?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["78"], ["99"], ["96"]],
"soluciones": {"incompleto": "30. 18.", "solo": "36.", "carpeta": ["78.", "99.", "96."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a combinar prendas y sabores.",
"vas_a_ver": ["El cuadro", "Cada uno con cada uno", "Multiplicar"],
"secciones": [
 S(1, "Muestra de ropa", [
  P("Sofi tiene 3 camisetas y 2 pantalones."),
  P("Cada camiseta va con cada pantalón: <b>3 × 2 = 6</b>."),
  IMG("Combinaciones", "3 × 2.", FG.cuentas([("roja", "2"), ("azul", "2"), ("verde", "2")])),
 ]),
 S(1, "Combinar", [
  D("Combinar", "Juntamos <b>cada uno</b> de un grupo con cada uno del otro."),
  P("4 sabores y 2 conos: 8 helados."),
  IMG("Helados", "4 × 2.", FG.cuentas([("4 sabores × 2 conos", 8)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Grupos", "Para combinar.", FG.cuentas([("3 gorras y 3 bufandas", "?"), ("5 sabores y 2 conos", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Combinar", "planteo": "2 camisetas y 4 pantalones.", "pasos": ["Cada camiseta, 4 pantalones.", "2 × 4 = 8."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "3 panes y 2 rellenos.", "pasos": ["Cada pan, ___ rellenos.", "3 × 2 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuántos conjuntos con 4 gorras y 3 bufandas?"},
"tip": {"titulo": "Cuadro", "texto": "Armá un cuadro para no perder ninguna."},
"ojo": ["3 camisetas y 2 pantalones no son 5.", "Cada uno va con cada uno."],
"resumen": [{"titulo": "Cuadro", "texto": "Ordena."}, {"titulo": "Cada uno", "texto": "Con cada uno."}, {"titulo": "Multiplicar", "texto": "Las cantidades."}],
"glosario": [{"palabra": "Combinar", "significado": "Juntar de distintas formas."}, {"palabra": "Combinación", "significado": "Una forma de juntar."}],
"carpeta": ["¿Cuántos conjuntos se arman con 3 gorras y 3 bufandas?", "¿Cuántos helados con 5 sabores y 2 conos?", "Tomi sumó 3 + 2 para 3 camisetas y 2 pantalones. ¿Cuántas combinaciones hay?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["9"], ["10"], ["6"]],
"soluciones": {"incompleto": "2. 6.", "solo": "12.", "carpeta": ["9.", "10.", "6."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas de combinaciones.",
"vas_a_ver": ["Encontrar los dos grupos", "Multiplicar", "Responder"],
"secciones": [
 S(1, "La heladería", [
  P("Hay 5 sabores y 3 tipos de cono."),
  P("Cada sabor con cada cono: <b>5 × 3 = 15</b> helados."),
  IMG("Helados", "5 × 3.", FG.cuentas([("5 sabores × 3 conos", 15)])),
 ]),
 S(1, "Sándwiches", [
  D("Problema de combinar", "Buscamos los <b>dos grupos</b>, multiplicamos y respondemos."),
  P("4 panes y 3 rellenos: 12 sándwiches."),
  IMG("Sándwiches", "4 × 3.", FG.cuentas([("4 panes × 3 rellenos", 12)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el problema. Lo vas a usar en la carpeta."),
  IMG("Menú", "6 platos y 2 postres.", FG.cuentas([("6 × 2", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Problema", "planteo": "3 jugos y 4 galletas.", "pasos": ["Cada jugo con cada galleta.", "3 × 4 = 12 meriendas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "2 colores de mochila y 5 llaveros.", "pasos": ["2 × 5 = ___ .", "Son ___ mochilas distintas."]},
"ejemplo_solo": {"titulo": "Resolvé", "planteo": "4 bicis y 4 cascos. ¿Cuántas formas de elegir?"},
"tip": {"titulo": "Dos grupos", "texto": "Marcá los dos grupos que se combinan."},
"ojo": ["5 sabores y 3 conos no son 8.", "Respondé con una oración."],
"resumen": [{"titulo": "Grupos", "texto": "Dos."}, {"titulo": "Multiplicar", "texto": "Uno por otro."}, {"titulo": "Responder", "texto": "Con oración."}],
"glosario": [{"palabra": "Menú", "significado": "Lista de comidas para elegir."}, {"palabra": "Elegir", "significado": "Tomar uno entre varios."}],
"carpeta": ["En un menú hay 6 platos y 2 postres. ¿Cuántos almuerzos distintos hay?", "Si agregan 1 postre más, ¿cuántos almuerzos hay?", "Juan dice que con 5 sabores y 3 conos hay 8 helados. ¿Cuántos hay?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["12"], ["18"], ["15"]],
"soluciones": {"incompleto": "10. 10.", "solo": "16.", "carpeta": ["12.", "18: 6 × 3.", "15."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("FILAS POR COLUMNAS", [LD("RECTÁNGULO", "SI TODAS LAS FILAS TIENEN LO MISMO, MULTIPLICAMOS <b>FILAS POR COLUMNAS</b>."),
   LL("NO HACE FALTA CONTAR DE A UNO.", "GIRADO DA EL MISMO TOTAL.")],
   {"modo": "combina"}, {"modo": "combina"}),
], "recuerda": [
 RC("ORGANIZACIÓN RECTANGULAR", "COSAS ORDENADAS EN FILAS Y COLUMNAS IGUALES.", "2 FILAS DE 7 = 14"),
 RC("GIRAR", "SI GIRAMOS EL RECTÁNGULO, EL TOTAL NO CAMBIA.", "4 × 5 = 5 × 4 = 20"),
]}
N2["leccion"] = {"temas": [
 T("MUCHAS FILAS", [LD("PARTIR LAS FILAS", "SEPARAMOS <b>10 FILAS</b> Y LAS QUE SOBRAN; CALCULAMOS CADA GRUPO."),
   LL("DIEZ FILAS SON FÁCILES DE CONTAR.", "AL FINAL JUNTAMOS LOS DOS GRUPOS.")],
   {"modo": "combina", "que": "grande"}, {"modo": "combina", "que": "grande"}),
], "recuerda": [
 RC("PARTIR", "SEPARAMOS LAS FILAS EN 10 Y LAS QUE SOBRAN.", "14 FILAS = 10 + 4"),
 RC("JUNTAR", "SUMAMOS LO QUE DA CADA GRUPO DE FILAS.", "14 FILAS DE 5: 50 + 20 = 70"),
]}
N3["leccion"] = {"temas": [
 T("COMBINAR", [LD("CADA UNO CON CADA UNO", "UN CUADRO MUESTRA <b>TODAS LAS PAREJAS</b>: CADA ELEMENTO CON TODOS LOS DEL OTRO GRUPO."),
   LL("NINGUNA PAREJA SE REPITE.", "EL TOTAL ES UNA MULTIPLICACIÓN.")],
   {"modo": "combina", "que": "prendas"}, {"modo": "combina", "que": "prendas"}),
], "recuerda": [
 RC("COMBINAR", "JUNTAMOS CADA UNO DE UN GRUPO CON CADA UNO DEL OTRO.", "2 CAMISETAS Y 4 PANTALONES = 8"),
 RC("CUADRO", "ORDENA TODAS LAS COMBINACIONES PARA NO PERDER NINGUNA.", "3 PANES Y 2 RELLENOS = 6"),
]}
N4["leccion"] = {"temas": [
 T("PROBLEMAS DE COMBINAR", [LD("RESOLVER", "BUSCAMOS LOS <b>DOS GRUPOS</b> QUE SE MEZCLAN Y MULTIPLICAMOS SUS CANTIDADES."),
   LL("NO SE SUMAN LOS GRUPOS.", "CONTESTAMOS CON PALABRAS.")],
   {"modo": "combina", "que": "problema"}, {"modo": "combina", "que": "problema"}),
], "recuerda": [
 RC("PROBLEMA", "MULTIPLICAMOS LA CANTIDAD DE UN GRUPO POR LA DEL OTRO.", "3 JUGOS Y 4 GALLETAS = 12 MERIENDAS"),
 RC("RESPONDER", "ESCRIBIMOS UNA ORACIÓN CON EL NÚMERO Y LO QUE CUENTA.", "SE PUEDEN ARMAR 16 PAREJAS"),
]}

ACT = {
"1": [N("¿CUÁNTAS SILLAS HAY EN 6 FILAS DE 3?", 18, "6 × 3.", n="aplicar"),
      FB("COMPLETÁ: 4 FILAS DE 5 = ___", [["20"]], "4 × 5.", n="aplicar"),
      MC("LEO SUMÓ 4 + 6 PARA 4 FILAS DE 6. ¿CUÁNTAS HAY?", ["24", "10", "46"], "24", "SE MULTIPLICA.", n="error"),
      MC("3 FILAS DE 5 Y 5 FILAS DE 3…", ["DAN LO MISMO", "DAN DISTINTO"], "DAN LO MISMO", "GIRAR NO CAMBIA EL TOTAL.", n="analizar")],
"2": [N("¿CUÁNTAS BUTACAS HAY EN 14 FILAS DE 5?", 70, "50 + 20.", n="aplicar"),
      FB("COMPLETÁ: 16 FILAS DE 3 = 30 + ___", [["18"]], "6 × 3.", n="aplicar"),
      MC("MÍA HIZO 12 FILAS DE 8 = 80. ¿CUÁNTAS HAY?", ["96", "80", "20"], "96", "FALTAN 2 FILAS.", n="error"),
      N("[[problema]] UN TEATRO TIENE 18 FILAS DE 2 BUTACAS. ¿CUÁNTAS HAY?", 36, "20 + 16.", n="analizar")],
"3": [N("2 CAMISETAS Y 4 PANTALONES. ¿CUÁNTAS COMBINACIONES?", 8, "2 × 4.", n="aplicar"),
      N("4 GORRAS Y 3 BUFANDAS. ¿CUÁNTOS CONJUNTOS?", 12, "4 × 3.", n="aplicar"),
      MC("TOMI SUMÓ 3 + 2 PARA 3 CAMISETAS Y 2 PANTALONES. ¿CUÁNTAS HAY?", ["6", "5", "32"], "6", "CADA UNO CON CADA UNO.", n="error"),
      UNIR("UNÍ CADA GRUPO CON SUS COMBINACIONES.", ["2 Y 3", "3 Y 3", "2 Y 5"], ["10", "6", "9"], {"2 Y 3": "6", "3 Y 3": "9", "2 Y 5": "10"}, "MULTIPLICÁ.", n="analizar")],
"4": [N("5 SABORES Y 3 CONOS. ¿CUÁNTOS HELADOS DISTINTOS?", 15, "5 × 3.", n="aplicar"),
      N("[[problema]] 3 JUGOS Y 4 GALLETAS. ¿CUÁNTAS MERIENDAS DISTINTAS?", 12, "3 × 4.", n="aplicar"),
      MC("JUAN DICE QUE CON 5 SABORES Y 3 CONOS HAY 8 HELADOS. ¿CUÁNTOS HAY?", ["15", "8", "53"], "15", "SE MULTIPLICA.", n="error"),
      MC("¿QUÉ CUENTA RESUELVE «6 PLATOS Y 2 POSTRES»?", ["6 × 2", "6 + 2", "6 − 2"], "6 × 2", "CADA PLATO CON CADA POSTRE.", n="analizar")],
"5": [N("RELÁMPAGO. 3 FILAS DE 7 = ___", 21, "21.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 11 FILAS DE 4 = ___", 44, "40 + 4.", tiempo=40, n="aplicar"),
      N("RELÁMPAGO. 3 PANES Y 3 RELLENOS = ___", 9, "3 × 3.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. PARA COMBINAR…", ["MULTIPLICAMOS", "SUMAMOS"], "MULTIPLICAMOS", "CADA UNO CON CADA UNO.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTAS ESTRELLAS HAY EN 4 FILAS DE 6?", 24, "4 × 6.", n="aplicar")],
 [1, MC("¿QUÉ CUENTA ES «5 FILAS DE 8»?", ["5 × 8", "5 + 8", "8 − 5"], "5 × 8", "FILAS POR COLUMNAS.", n="analizar")],
 [1, TF("SI GIRAMOS EL RECTÁNGULO, CAMBIA EL TOTAL.", "FALSO", "DA LO MISMO.", n="error")],
 [2, N("¿CUÁNTAS BUTACAS HAY EN 13 FILAS DE 6?", 78, "60 + 18.", n="aplicar")],
 [2, N("¿CUÁNTAS BUTACAS HAY EN 11 FILAS DE 9?", 99, "90 + 9.", n="aplicar")],
 [2, MC("PARA 15 FILAS DE 4, PARTIMOS EN…", ["10 Y 5", "1 Y 5", "15 Y 4"], "10 Y 5", "10 FILAS Y EL RESTO.", n="recordar")],
 [3, N("3 GORRAS Y 3 BUFANDAS. ¿CUÁNTOS CONJUNTOS?", 9, "3 × 3.", n="aplicar")],
 [3, N("5 SABORES Y 2 CONOS. ¿CUÁNTOS HELADOS?", 10, "5 × 2.", n="aplicar")],
 [3, CLAS("¿HAY MÁS O MENOS DE 10 COMBINACIONES?", ["2 Y 3", "4 Y 3", "3 Y 3", "5 Y 4"], ["MENOS DE 10", "MÁS DE 10"], {"2 Y 3": "MENOS DE 10", "4 Y 3": "MÁS DE 10", "3 Y 3": "MENOS DE 10", "5 Y 4": "MÁS DE 10"}, "6, 12, 9 Y 20.", n="analizar")],
 [4, N("[[problema]] 6 PLATOS Y 2 POSTRES. ¿CUÁNTOS ALMUERZOS DISTINTOS?", 12, "6 × 2.", n="aplicar")],
 [4, N("4 BICIS Y 4 CASCOS. ¿CUÁNTAS FORMAS DE ELEGIR?", 16, "4 × 4.", n="aplicar")],
 [4, MC("NICO DICE QUE 4 PANES Y 3 RELLENOS DAN 7 SÁNDWICHES. ¿CUÁNTOS SON?", ["12", "7", "43"], "12", "SE MULTIPLICA.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 13, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: organizaciones rectangulares", "examen_titulo": "Nivel jefe: organizaciones rectangulares",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-13.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
