# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 9 · Multiplicación y series proporcionales. Genera mision-9.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la panadería de Doña Rosa.
Niveles: 1 grupos iguales · 2 series proporcionales · 3 tablas · 4 problemas de series."""
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
"objetivo": "Vas a multiplicar grupos iguales.",
"vas_a_ver": ["Grupos iguales", "El signo ×", "Filas y columnas"],
"secciones": [
 S(1, "Bandejas iguales", [
  P("Doña Rosa pone 4 galletas en cada bandeja. Tiene 5 bandejas."),
  P("4, 8, 12, 16, 20: <b>5 × 4 = 20</b>."),
  IMG("5 grupos de 4", "Contamos de 4 en 4.", FG.grupos("estrella", 5, 4, "5 × 4 = 20")),
 ]),
 S(1, "Filas iguales", [
  D("Multiplicar", "Juntar <b>grupos iguales</b>. 3 filas de 6 es 3 × 6."),
  P("6, 12, 18: son 18."),
  IMG("3 filas de 6", "Un arreglo.", FG.arreglo("manzana", 3, 6, "3 × 6 = 18")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Grupos para contar", "¿Cuántos hay?", FG.grupos("pelota", 4, 5)),
 ]),
],
"ejemplo_completo": {"titulo": "Multiplicar", "planteo": "2 bandejas de 7.", "pasos": ["7, 14.", "2 × 7 = 14."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "3 grupos de 5.", "pasos": ["5, 10, ___ .", "3 × 5 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 4 filas de 3?"},
"tip": {"titulo": "Iguales", "texto": "Solo se multiplica con grupos iguales."},
"ojo": ["5 × 4 no es 5 + 4.", "Los grupos tienen que ser iguales."],
"resumen": [{"titulo": "Grupos", "texto": "Iguales."}, {"titulo": "×", "texto": "Veces."}, {"titulo": "Filas", "texto": "Arreglo."}],
"glosario": [{"palabra": "Grupo", "significado": "Cosas juntas."}, {"palabra": "Por", "significado": "El signo ×."}],
"carpeta": ["En los grupos para contar, ¿cuántas pelotas hay?", "¿Cuánto es 4 × 5?", "Leo dice que 5 × 4 = 9. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["20"], ["20"], ["20"]],
"soluciones": {"incompleto": "15. 15.", "solo": "12.", "carpeta": ["20.", "20.", "20: son 5 grupos de 4."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a completar series proporcionales.",
"vas_a_ver": ["Sumar siempre lo mismo", "De 6 en 6", "Qué número sigue"],
"secciones": [
 S(1, "Cajas de 6", [
  P("1 caja tiene 6 pastelitos. 2 cajas, 12."),
  P("Cada caja suma 6: <b>6, 12, 18, 24</b>."),
  IMG("De 6 en 6", "Cada vagón suma 6.", FG.tren_paso(6, 30, 6)),
 ]),
 S(1, "Serie proporcional", [
  D("Serie proporcional", "Cada vez sumamos <b>la misma cantidad</b>."),
  P("Con 0 cajas hay 0."),
  IMG("De 8 en 8", "8, 16, 24…", FG.tren_paso(8, 40, 8)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Tren para completar", "Faltan dos vagones.", FG.tren_paso(7, 42, 7, faltan=(21, 35))),
 ]),
],
"ejemplo_completo": {"titulo": "Serie", "planteo": "De 4 en 4.", "pasos": ["4, 8, 12, 16.", "Sigue 20."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "De 9 en 9.", "pasos": ["9, 18, ___ , 36.", "36, ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Qué sigue? 5, 10, 15, 20…"},
"tip": {"titulo": "Mirá el salto", "texto": "Restá dos vecinos para saber cuánto suma."},
"ojo": ["6, 12, 18, 24, no 20.", "Siempre se suma lo mismo."],
"resumen": [{"titulo": "Serie", "texto": "Suma igual."}, {"titulo": "Salto", "texto": "Siempre el mismo."}, {"titulo": "0", "texto": "Da 0."}],
"glosario": [{"palabra": "Serie", "significado": "Números en orden."}, {"palabra": "Salto", "significado": "Lo que se suma."}],
"carpeta": ["En el tren, ¿qué número falta después del 14?", "¿Qué número falta después del 28?", "Sofi escribió 6, 12, 18, 20. ¿Qué número va después del 18?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["21"], ["35"], ["24"]],
"soluciones": {"incompleto": "27. 45.", "solo": "25.", "carpeta": ["21.", "35.", "24."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a completar tablas de una cantidad que se repite.",
"vas_a_ver": ["La tabla", "El doble", "Sin contar de a uno"],
"secciones": [
 S(1, "Bolsas de pan", [
  P("Cada bolsa lleva 5 panes."),
  P("1 bolsa: 5. 2 bolsas: 10. 4 bolsas: <b>20</b>."),
  IMG("Bolsas y panes", "La tabla.", FG.cuentas([("1 bolsa", 5), ("2 bolsas", 10), ("4 bolsas", 20), ("8 bolsas", 40)])),
 ]),
 S(1, "El doble", [
  D("Doble", "Si hay el <b>doble</b> de bolsas, hay el doble de panes."),
  P("4 bolsas: 20. 8 bolsas: 40."),
  IMG("Doble", "20 + 20 = 40.", FG.cuentas([("4 bolsas", 20), ("8 bolsas", 40)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla. La vas a usar en la carpeta."),
  IMG("Tabla para completar", "Cada caja tiene 6.", FG.cuentas([("1 caja", 6), ("3 cajas", "?"), ("6 cajas", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Completar", "planteo": "Cada caja tiene 3.", "pasos": ["2 cajas: 6. 4 cajas: 12.", "8 cajas: 24."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cada bolsa tiene 9.", "pasos": ["2 bolsas: ___ .", "4 bolsas: ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "Si 5 cajas tienen 40, ¿cuánto tienen 10?"},
"tip": {"titulo": "Doble", "texto": "Usá el doble para ir más rápido."},
"ojo": ["El doble de bolsas no suma 5: duplica.", "Revisá que cada fila sume lo mismo."],
"resumen": [{"titulo": "Tabla", "texto": "Ordena la serie."}, {"titulo": "Doble", "texto": "Doble y doble."}, {"titulo": "Rápido", "texto": "Sin contar de a uno."}],
"glosario": [{"palabra": "Tabla", "significado": "Cuadro con filas y columnas."}, {"palabra": "Doble", "significado": "Dos veces lo mismo."}],
"carpeta": ["En la tabla, ¿cuánto tienen 3 cajas?", "¿Cuánto tienen 6 cajas?", "Leo dice que 6 cajas tienen 24 porque suma 6. ¿Cuánto tienen?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["18"], ["36"], ["36"]],
"soluciones": {"incompleto": "18. 36.", "solo": "80.", "carpeta": ["18.", "36: el doble de 18.", "36."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas de series.",
"vas_a_ver": ["Armar la tabla", "Multiplicar", "Responder"],
"secciones": [
 S(1, "Cajas de galletas", [
  P("Piden 7 cajas de 8 galletas."),
  P("8, 16, 24, 32, 40, 48, 56: son <b>56</b>."),
  IMG("7 cajas de 8", "De 8 en 8.", FG.tren_paso(8, 56, 8)),
 ]),
 S(1, "Más corto", [
  D("Multiplicar", "En vez de sumar muchas veces, <b>multiplicamos</b>: 7 × 8."),
  P("Respondemos: son 56 galletas."),
  IMG("7 × 8", "Siete grupos de ocho.", FG.cuentas([("7 × 8", 56)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el problema. Lo vas a usar en la carpeta."),
  IMG("Bandejas", "Cada una tiene 9.", FG.grupos("caramelo", 4, 9)),
 ]),
],
"ejemplo_completo": {"titulo": "Problema", "planteo": "6 bolsas de 5 panes.", "pasos": ["5, 10, 15, 20, 25, 30.", "6 × 5 = 30 panes."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "3 cajas de 10 lápices.", "pasos": ["10, 20, ___ .", "Son ___ lápices."]},
"ejemplo_solo": {"titulo": "Resolvé", "planteo": "Cada paquete trae 4 estampas. ¿Cuántas en 9 paquetes?"},
"tip": {"titulo": "Tabla o por", "texto": "Elegí la tabla o la multiplicación."},
"ojo": ["7 cajas de 8 no es 7 + 8.", "Respondé con una oración."],
"resumen": [{"titulo": "Tabla", "texto": "O multiplicar."}, {"titulo": "Grupos", "texto": "Por cantidad."}, {"titulo": "Responder", "texto": "Con oración."}],
"glosario": [{"palabra": "Problema", "significado": "Pregunta con datos."}, {"palabra": "Multiplicar", "significado": "Sumar grupos iguales."}],
"carpeta": ["Cada bandeja tiene 9 caramelos. ¿Cuántos hay en 4 bandejas?", "¿Cuántos habría en 8 bandejas?", "Juan sumó 4 + 9 = 13. ¿Cuántos caramelos hay en 4 bandejas?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["36"], ["72"], ["36"]],
"soluciones": {"incompleto": "30. 30.", "solo": "36.", "carpeta": ["36.", "72: el doble de 36.", "36."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("GRUPOS IGUALES", [LD("MULTIPLICAR", "SI TODOS LOS GRUPOS TIENEN <b>LO MISMO</b>, PODEMOS MULTIPLICAR."),
   LL("EL SIGNO × SE LEE «POR».", "CONTAMOS DE A GRUPO, NO DE A UNO.")],
   {"modo": "mult", "que": "grupos"}, {"modo": "mult", "que": "grupos"}),
 T("FILAS Y COLUMNAS", [LD("ARREGLO", "COSAS EN <b>FILAS IGUALES</b> TAMBIÉN SON GRUPOS: CADA FILA ES UNO."),
   LL("FILAS POR CUÁNTAS HAY EN CADA UNA.", "SI LO GIRAMOS, DA LO MISMO.")],
   {"modo": "mult", "que": "arreglo"}, {"modo": "mult", "que": "arreglo"}),
], "recuerda": [
 RC("MULTIPLICAR", "JUNTAMOS GRUPOS QUE TIENEN LA MISMA CANTIDAD.", "2 BANDEJAS DE 7 = 2 × 7 = 14"),
 RC("ARREGLO", "LAS FILAS IGUALES SE CUENTAN CON UNA MULTIPLICACIÓN.", "4 FILAS DE 3 = 12"),
]}
N2["leccion"] = {"temas": [
 T("SERIES PROPORCIONALES", [LD("SERIE", "CADA CAJA AGREGA <b>LA MISMA CANTIDAD</b> QUE LA ANTERIOR."),
   LL("SI NO HAY CAJAS, HAY CERO.", "EL SALTO SIEMPRE ES IGUAL.")],
   {"modo": "serie_prop"}, {"modo": "serie_prop"}),
], "recuerda": [
 RC("SERIE PROPORCIONAL", "EN CADA PASO SUMAMOS SIEMPRE LA MISMA CANTIDAD.", "4, 8, 12, 16, 20"),
 RC("EL SALTO", "PARA SABER EL SALTO RESTAMOS DOS NÚMEROS VECINOS.", "18 − 9 = 9: VA DE 9 EN 9"),
]}
N3["leccion"] = {"temas": [
 T("TABLAS Y DOBLES", [LD("USAR EL DOBLE", "SI DUPLICAMOS LAS CAJAS, SE <b>DUPLICA</b> LO QUE HAY ADENTRO."),
   LL("NO HACE FALTA CONTAR DE A UNO.", "LA TABLA ORDENA TODO.")],
   {"modo": "serie_prop", "que": "tabla"}, {"modo": "serie_prop", "que": "tabla"}),
], "recuerda": [
 RC("TABLA", "ORDENA CUÁNTO HAY SEGÚN LA CANTIDAD DE CAJAS.", "CAJAS DE 3: 2 → 6, 4 → 12"),
 RC("DOBLE", "CON EL DOBLE DE CAJAS HAY EL DOBLE DE COSAS.", "5 CAJAS: 40. 10 CAJAS: 80"),
]}
N4["leccion"] = {"temas": [
 T("PROBLEMAS DE SERIES", [LD("RESOLVER", "ARMAMOS UNA <b>TABLA</b> O MULTIPLICAMOS GRUPOS POR LO QUE TIENE CADA UNO."),
   LL("NO SE SUMAN GRUPOS Y CANTIDAD.", "CONTESTAMOS CON PALABRAS.")],
   {"modo": "serie_prop", "que": "problema"}, {"modo": "serie_prop", "que": "problema"}),
], "recuerda": [
 RC("PROBLEMA DE SERIE", "MULTIPLICAMOS LA CANTIDAD DE GRUPOS POR LO QUE TIENE CADA UNO.", "6 BOLSAS DE 5 = 30 PANES"),
 RC("RESPONDER", "ESCRIBIMOS UNA ORACIÓN CON EL NÚMERO Y LO QUE CUENTA.", "SON 36 ESTAMPAS"),
]}

ACT = {
"1": [N("¿CUÁNTO ES 2 BANDEJAS DE 7?", 14, "7, 14.", n="aplicar"),
      N("¿CUÁNTO ES 4 FILAS DE 3?", 12, "3, 6, 9, 12.", n="aplicar"),
      MC("LEO DICE QUE 5 × 4 = 9. ¿CUÁNTO ES?", ["20", "9", "54"], "20", "5 GRUPOS DE 4.", n="error"),
      CLAS("¿SE PUEDE MULTIPLICAR?", ["3 BOLSAS DE 5", "BOLSAS DE 2, 4 Y 7", "6 FILAS DE 6", "UNA CAJA DE 3 Y OTRA DE 9"], ["SÍ", "NO"], {"3 BOLSAS DE 5": "SÍ", "BOLSAS DE 2, 4 Y 7": "NO", "6 FILAS DE 6": "SÍ", "UNA CAJA DE 3 Y OTRA DE 9": "NO"}, "SOLO CON GRUPOS IGUALES.", n="analizar")],
"2": [FB("COMPLETÁ: 9, 18, ___, 36", [["27"]], "SUMA 9.", n="aplicar"),
      N("¿QUÉ SIGUE? 5, 10, 15, 20, ___", 25, "SUMA 5.", n="aplicar"),
      MC("SOFI ESCRIBIÓ 6, 12, 18, 20. ¿QUÉ VA DESPUÉS DEL 18?", ["24", "20", "19"], "24", "SIEMPRE SUMA 6.", n="error"),
      MC("¿DE CUÁNTO EN CUÁNTO VA 8, 16, 24?", ["DE 8 EN 8", "DE 6 EN 6", "DE 2 EN 2"], "DE 8 EN 8", "16 − 8 = 8.", n="analizar")],
"3": [N("CADA CAJA TIENE 3. ¿CUÁNTO TIENEN 4 CAJAS?", 12, "3, 6, 9, 12.", n="aplicar"),
      N("SI 5 CAJAS TIENEN 40, ¿CUÁNTO TIENEN 10?", 80, "EL DOBLE.", n="analizar"),
      MC("LEO DICE QUE SI 3 CAJAS TIENEN 18, 6 CAJAS TIENEN 24. ¿CUÁNTO TIENEN?", ["36", "24", "21"], "36", "EL DOBLE DE 18.", n="error"),
      UNIR("CADA BOLSA TIENE 9. UNÍ BOLSAS Y CANTIDAD.", ["2 BOLSAS", "4 BOLSAS", "1 BOLSA"], ["36", "9", "18"], {"2 BOLSAS": "18", "4 BOLSAS": "36", "1 BOLSA": "9"}, "4 ES EL DOBLE DE 2.", n="aplicar")],
"4": [N("CADA PAQUETE TRAE 4 ESTAMPAS. ¿CUÁNTAS EN 9 PAQUETES?", 36, "9 × 4.", n="aplicar"),
      N("[[problema]] 3 CAJAS DE 10 LÁPICES. ¿CUÁNTOS LÁPICES?", 30, "10, 20, 30.", n="aplicar"),
      MC("JUAN SUMÓ 4 + 9 = 13 PARA 4 BANDEJAS DE 9. ¿CUÁNTOS SON?", ["36", "13", "49"], "36", "4 GRUPOS DE 9.", n="error"),
      MC("¿QUÉ CUENTA RESUELVE «6 BOLSAS DE 5 PANES»?", ["6 × 5", "6 + 5", "6 − 5"], "6 × 5", "GRUPOS IGUALES.", n="analizar")],
"5": [N("RELÁMPAGO. 3 × 5 = ___", 15, "15.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿QUÉ SIGUE? 7, 14, 21, ___", 28, "28.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 2 CAJAS: 16. ¿4 CAJAS?", 32, "EL DOBLE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿SE MULTIPLICA CON GRUPOS…?", ["IGUALES", "DISTINTOS"], "IGUALES", "SIEMPRE IGUALES.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 3 GRUPOS DE 5?", 15, "5, 10, 15.", n="aplicar")],
 [1, MC("¿QUÉ CUENTA ES «4 FILAS DE 6»?", ["4 × 6", "4 + 6", "6 − 4"], "4 × 6", "FILAS IGUALES.", n="analizar")],
 [1, TF("SE PUEDE MULTIPLICAR CON GRUPOS DISTINTOS.", "FALSO", "SOLO CON GRUPOS IGUALES.", n="error")],
 [2, N("¿QUÉ SIGUE? 4, 8, 12, 16, ___", 20, "SUMA 4.", n="aplicar")],
 [2, FB("COMPLETÁ: 8, 16, ___, 32", [["24"]], "SUMA 8.", n="aplicar")],
 [2, MC("EN UNA SERIE PROPORCIONAL, ¿CUÁNTO HAY CON 0 CAJAS?", ["0", "1", "10"], "0", "SIN CAJAS NO HAY NADA.", n="recordar")],
 [3, N("CADA BOLSA TIENE 9. ¿CUÁNTO TIENEN 2 BOLSAS?", 18, "9 + 9.", n="aplicar")],
 [3, N("SI 4 BOLSAS TIENEN 36, ¿CUÁNTO TIENEN 8?", 72, "EL DOBLE.", n="analizar")],
 [3, MC("TOMI DICE QUE EL DOBLE DE CAJAS SUMA 5 MÁS. ¿QUÉ PASA?", ["SE DUPLICA", "SUMA 5"], "SE DUPLICA", "DOBLE Y DOBLE.", n="error")],
 [4, N("7 CAJAS DE 8 GALLETAS. ¿CUÁNTAS GALLETAS?", 56, "7 × 8.", n="aplicar")],
 [4, N("[[problema]] CADA BANDEJA TIENE 9 PANES. ¿CUÁNTOS HAY EN 4 BANDEJAS?", 36, "9, 18, 27, 36.", n="aplicar")],
 [4, MC("NICO DICE QUE 6 BOLSAS DE 5 SON 11. ¿CUÁNTOS SON?", ["30", "11", "65"], "30", "6 × 5.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 9, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: multiplicación y series proporcionales", "examen_titulo": "Nivel jefe: multiplicación y series proporcionales",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
