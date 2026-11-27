# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 15 · División con resto. Genera mision-15.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: el taller de juguetes de Bruno.
Niveles: 1 dividir restando · 2 con la tabla · 3 el resto · 4 comprobar."""
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
"objetivo": "Vas a dividir restando.",
"vas_a_ver": ["Restar siempre lo mismo", "Contar las veces", "Lo que queda"],
"secciones": [
 S(1, "Ruedas", [
  P("Bruno tiene 20 ruedas. Cada auto lleva 4."),
  P("20, 16, 12, 8, 4, 0: restamos <b>5 veces</b>."),
  IMG("Restando", "De 4 en 4 para atrás.", FG.cuentas([("20 − 4", 16), ("16 − 4", 12), ("12 − 4", 8), ("8 − 4", 4), ("4 − 4", 0)])),
 ]),
 S(1, "Contar las veces", [
  D("Dividir restando", "Restamos <b>siempre lo mismo</b> y contamos cuántas veces."),
  P("20 ÷ 4 = 5."),
  IMG("15 ÷ 5", "3 veces.", FG.cuentas([("15 − 5", 10), ("10 − 5", 5), ("5 − 5", 0)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Dividir restando", "¿Cuántas veces?", FG.cuentas([("18 ÷ 6", "?"), ("21 ÷ 7", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Restando", "planteo": "12 ÷ 3.", "pasos": ["12, 9, 6, 3, 0.", "4 veces: 12 ÷ 3 = 4."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "10 ÷ 2.", "pasos": ["10, 8, 6, ___ , ___ , 0.", "___ veces."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuántas veces se resta 5 al 25?"},
"tip": {"titulo": "Contá", "texto": "Marcá con un palito cada resta."},
"ojo": ["El resultado son las veces.", "No es lo que queda."],
"resumen": [{"titulo": "Restar", "texto": "Lo mismo."}, {"titulo": "Contar", "texto": "Las veces."}, {"titulo": "Queda", "texto": "El resto."}],
"glosario": [{"palabra": "Dividir", "significado": "Ver cuántas veces entra un número."}, {"palabra": "Vez", "significado": "Cada una de las restas."}],
"carpeta": ["¿Cuántas veces se puede restar 6 al 18?", "¿Cuántas veces se puede restar 7 al 21?", "Leo restó 4 al 20 y dijo que da 0. ¿Cuánto es 20 ÷ 4?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3"], ["3"], ["5"]],
"soluciones": {"incompleto": "4. 2. 5.", "solo": "5.", "carpeta": ["3.", "3.", "5."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a dividir con la tabla pitagórica.",
"vas_a_ver": ["La tabla del divisor", "El más cerca sin pasarse", "Cociente y resto"],
"secciones": [
 S(1, "Un atajo", [
  P("38 ÷ 6: en la tabla del 6, 6 × 6 = 36 y 6 × 7 = 42."),
  P("36 es el más cerca sin pasarse: <b>6</b> y sobran 2."),
  IMG("Tabla del 6", "36 y 42.", FG.cuentas([("6 × 6", 36), ("6 × 7", 42)])),
 ]),
 S(1, "Sin pasarse", [
  D("Dividir con la tabla", "Buscamos en la tabla el número <b>más cercano sin pasarnos</b>."),
  P("45 ÷ 9 = 5, porque 9 × 5 = 45."),
  IMG("Tabla del 9", "Justo.", FG.cuentas([("9 × 5", 45)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Divisiones", "Con la tabla.", FG.cuentas([("29 ÷ 7", "?"), ("50 ÷ 8", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Con la tabla", "planteo": "27 ÷ 4.", "pasos": ["4 × 6 = 24. 4 × 7 = 28 se pasa.", "6 y sobran 3."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "33 ÷ 5.", "pasos": ["5 × ___ = 30.", "Sobran ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto es 56 ÷ 7?"},
"tip": {"titulo": "Sin pasarse", "texto": "Si te pasás, bajá uno."},
"ojo": ["38 ÷ 6 no es 7: 42 se pasa.", "Restá para saber cuánto sobra."],
"resumen": [{"titulo": "Tabla", "texto": "Del divisor."}, {"titulo": "Cerca", "texto": "Sin pasarse."}, {"titulo": "Sobra", "texto": "La diferencia."}],
"glosario": [{"palabra": "Cociente", "significado": "Lo que da la división."}, {"palabra": "Divisor", "significado": "El número que divide."}],
"carpeta": ["¿Cuánto es 29 ÷ 7? Escribí el cociente.", "¿Cuál es el cociente de 50 ÷ 8?", "Mía dice que 38 ÷ 6 = 7. ¿Cuál es el cociente?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["4"], ["6"], ["6"]],
"soluciones": {"incompleto": "6. 3.", "solo": "8.", "carpeta": ["4 y sobra 1.", "6 y sobran 2.", "6: 6 × 7 = 42 se pasa."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer el resto de una división.",
"vas_a_ver": ["Dividendo, cociente y resto", "El resto es menor", "Encontrar el resto"],
"secciones": [
 S(1, "Tornillos", [
  P("31 tornillos en cajas de 5."),
  P("6 cajas y queda <b>1</b> suelto."),
  IMG("31 ÷ 5", "Resto 1.", FG.grupos("caramelo", 6, 5, "31 ÷ 5 = 6, resto 1")),
 ]),
 S(1, "Las partes", [
  D("Resto", "Lo que sobra en la división. Siempre es <b>menor que el divisor</b>."),
  P("Dividendo 31, divisor 5, cociente 6, resto 1."),
  IMG("Partes", "Cada una con su nombre.", FG.cuentas([("dividendo", 31), ("divisor", 5), ("cociente", 6), ("resto", 1)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Restos", "¿Cuánto sobra?", FG.cuentas([("23 ÷ 4", "?"), ("40 ÷ 6", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Resto", "planteo": "17 ÷ 3.", "pasos": ["3 × 5 = 15.", "Resto: 17 − 15 = 2."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "26 ÷ 4.", "pasos": ["4 × 6 = ___ .", "Resto: ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuál es el resto de 35 ÷ 8?"},
"tip": {"titulo": "Menor", "texto": "Si el resto es grande, falta otra vuelta."},
"ojo": ["El resto nunca es mayor que el divisor.", "Puede ser 0."],
"resumen": [{"titulo": "Dividendo", "texto": "Lo que repartimos."}, {"titulo": "Cociente", "texto": "Lo que sale."}, {"titulo": "Resto", "texto": "Lo que sobra."}],
"glosario": [{"palabra": "Dividendo", "significado": "El número que se reparte."}, {"palabra": "Resto", "significado": "Lo que sobra."}],
"carpeta": ["¿Cuál es el resto de 23 ÷ 4?", "¿Cuál es el resto de 40 ÷ 6?", "Juan dice que el resto de 31 ÷ 5 es 6. ¿Cuál es el resto?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3"], ["4"], ["1"]],
"soluciones": {"incompleto": "24. 2.", "solo": "3.", "carpeta": ["3.", "4.", "1: el 6 es el cociente."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a comprobar divisiones con una multiplicación.",
"vas_a_ver": ["Cociente por divisor", "Más el resto", "Comparar"],
"secciones": [
 S(1, "La prueba", [
  P("31 ÷ 5 = 6 y sobra 1."),
  P("6 × 5 = 30. 30 + 1 = <b>31</b>. ¡Está bien!"),
  IMG("Prueba", "Vuelve al 31.", FG.cuentas([("6 × 5", 30), ("30 + 1", 31)])),
 ]),
 S(1, "Comprobar", [
  D("Comprobar", "Multiplicamos <b>cociente por divisor</b> y sumamos el resto: tiene que dar el dividendo."),
  P("Si no da, hay un error."),
  IMG("29 ÷ 7", "4 y resto 1.", FG.cuentas([("4 × 7 + 1", 29)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las divisiones. Las vas a usar en la carpeta."),
  IMG("¿Están bien?", "Comprobá.", FG.cuentas([("23 ÷ 4 = 5, resto 3", "?"), ("40 ÷ 6 = 7, resto 2", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Comprobar", "planteo": "17 ÷ 3 = 5, resto 2.", "pasos": ["5 × 3 = 15.", "15 + 2 = 17: bien."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "26 ÷ 4 = 6, resto 2.", "pasos": ["6 × 4 = ___ .", "___ + 2 = 26."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Está bien 35 ÷ 8 = 4, resto 3?"},
"tip": {"titulo": "Volver", "texto": "La prueba te devuelve al número del principio."},
"ojo": ["No te olvides de sumar el resto.", "Si no da, revisá la división."],
"resumen": [{"titulo": "Multiplicar", "texto": "Cociente × divisor."}, {"titulo": "Sumar", "texto": "El resto."}, {"titulo": "Comparar", "texto": "Con el dividendo."}],
"glosario": [{"palabra": "Comprobar", "significado": "Ver si está bien."}, {"palabra": "Prueba", "significado": "Cuenta para controlar."}],
"carpeta": ["Comprobá 23 ÷ 4 = 5, resto 3. ¿Cuánto da 5 × 4 + 3?", "¿Está bien 40 ÷ 6 = 7, resto 2? ¿Cuánto da 7 × 6 + 2?", "Sofi probó 31 ÷ 5 = 6, resto 1, y le dio 30. ¿Qué le faltó sumar?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["23"], ["44"], ["1", "el resto"]],
"soluciones": {"incompleto": "24. 24.", "solo": "Sí: 4 × 8 + 3 = 35.", "carpeta": ["23: está bien.", "44: está mal, es 6 y resto 4.", "El resto: 1."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("RESTAR VARIAS VECES", [LD("CUÁNTAS VECES", "SACAMOS EL MISMO NÚMERO MUCHAS VECES: LAS VECES SON EL <b>RESULTADO</b>."),
   LL("PARAMOS CUANDO NO SE PUEDE SACAR MÁS.", "LO QUE QUEDA ES EL RESTO.")],
   {"modo": "divide3", "que": "restando"}, {"modo": "divide3", "que": "restando"}),
], "recuerda": [
 RC("DIVIDIR RESTANDO", "RESTAMOS SIEMPRE EL MISMO NÚMERO Y CONTAMOS LAS VECES.", "12, 9, 6, 3, 0: 4 VECES"),
 RC("LO QUE QUEDA", "CUANDO NO SE PUEDE RESTAR MÁS, LO QUE QUEDA ES EL RESTO.", "14 MENOS 4 TRES VECES: QUEDA 2"),
]}
N2["leccion"] = {"temas": [
 T("USAR LA TABLA", [LD("EL MÁS CERCANO", "EN LA TABLA DEL DIVISOR BUSCAMOS EL <b>MÁS GRANDE SIN PASARNOS</b>."),
   LL("LA FILA NOS DA EL COCIENTE.", "LA DIFERENCIA ES LO QUE SOBRA.")],
   {"modo": "divide3", "que": "tabla"}, {"modo": "divide3", "que": "tabla"}),
], "recuerda": [
 RC("CON LA TABLA", "BUSCAMOS EL NÚMERO MÁS CERCANO SIN PASARNOS.", "27 ÷ 4: 4 × 6 = 24"),
 RC("SIN PASARSE", "SI EL RESULTADO DE LA TABLA SE PASA, BAJAMOS UNO.", "4 × 7 = 28 SE PASA DE 27"),
]}
N3["leccion"] = {"temas": [
 T("EL RESTO", [LD("LO QUE SOBRA", "DESPUÉS DE ARMAR GRUPOS IGUALES, LO QUE QUEDA ES EL <b>RESTO</b>."),
   LL("ES MÁS CHICO QUE EL DIVISOR.", "SI DA CERO, LA DIVISIÓN ES EXACTA.")],
   {"modo": "divide3", "que": "tabla"}, {"modo": "divide3"}),
], "recuerda": [
 RC("RESTO", "LO QUE SOBRA EN UNA DIVISIÓN; ES MENOR QUE EL DIVISOR.", "17 ÷ 3 = 5 Y RESTO 2"),
 RC("EXACTA", "CUANDO EL RESTO ES CERO, NO SOBRA NADA.", "45 ÷ 9 = 5 Y RESTO 0"),
]}
N4["leccion"] = {"temas": [
 T("LA PRUEBA DE LA DIVISIÓN", [LD("COMPROBAR", "COCIENTE POR DIVISOR, <b>MÁS EL RESTO</b>, TIENE QUE DAR EL DIVIDENDO."),
   LL("SI DA IGUAL, ESTÁ BIEN.", "SI NO DA, BUSCAMOS EL ERROR.")],
   {"modo": "divide3", "que": "comprobar"}, {"modo": "divide3", "que": "comprobar"}),
], "recuerda": [
 RC("COMPROBAR", "MULTIPLICAMOS COCIENTE POR DIVISOR Y SUMAMOS EL RESTO.", "5 × 3 + 2 = 17"),
 RC("SI NO DA", "SI LA PRUEBA NO DA EL DIVIDENDO, LA DIVISIÓN ESTÁ MAL.", "7 × 6 + 2 = 44, NO 40"),
]}

ACT = {
"1": [N("¿CUÁNTAS VECES SE RESTA 3 AL 12 HASTA LLEGAR A 0?", 4, "12, 9, 6, 3, 0.", n="aplicar"),
      N("¿CUÁNTAS VECES SE RESTA 5 AL 25?", 5, "25, 20, 15, 10, 5, 0.", n="aplicar"),
      MC("LEO RESTÓ 4 AL 20 HASTA 0 Y DIJO QUE DA 0. ¿CUÁNTO ES 20 ÷ 4?", ["5", "0", "4"], "5", "SON LAS VECES.", n="error"),
      FB("COMPLETÁ: 10, 8, 6, ___, 2, 0", [["4"]], "DE 2 EN 2 PARA ATRÁS.", n="aplicar")],
"2": [N("¿CUÁNTO ES 56 ÷ 7?", 8, "7 × 8 = 56.", n="aplicar"),
      MC("27 ÷ 4: ¿QUÉ NÚMERO DE LA TABLA DEL 4 USAMOS?", ["24", "28", "20"], "24", "28 SE PASA.", n="analizar"),
      MC("MÍA DICE QUE 38 ÷ 6 = 7. ¿CUÁL ES EL COCIENTE?", ["6", "7", "8"], "6", "6 × 7 = 42 SE PASA.", n="error"),
      N("¿CUÁL ES EL COCIENTE DE 33 ÷ 5?", 6, "5 × 6 = 30.", n="aplicar")],
"3": [N("¿CUÁL ES EL RESTO DE 17 ÷ 3?", 2, "17 − 15.", n="aplicar"),
      N("¿CUÁL ES EL RESTO DE 35 ÷ 8?", 3, "35 − 32.", n="aplicar"),
      MC("JUAN DICE QUE EL RESTO DE 31 ÷ 5 ES 6. ¿CUÁL ES?", ["1", "6", "5"], "1", "EL 6 ES EL COCIENTE.", n="error"),
      UNIR("UNÍ CADA PARTE DE 26 ÷ 4 CON SU NÚMERO.", ["DIVIDENDO", "DIVISOR", "RESTO"], ["4", "2", "26"], {"DIVIDENDO": "26", "DIVISOR": "4", "RESTO": "2"}, "26 ÷ 4 = 6 Y RESTO 2.", n="analizar")],
"4": [N("¿CUÁNTO DA 5 × 3 + 2 PARA COMPROBAR 17 ÷ 3?", 17, "DA EL DIVIDENDO.", n="aplicar"),
      MC("¿ESTÁ BIEN 35 ÷ 8 = 4, RESTO 3?", ["SÍ", "NO"], "SÍ", "4 × 8 + 3 = 35.", n="aplicar"),
      MC("SOFI COMPROBÓ 31 ÷ 5 CON 6 × 5 = 30. ¿QUÉ LE FALTÓ?", ["SUMAR EL RESTO", "RESTAR 5", "NADA"], "SUMAR EL RESTO", "30 + 1 = 31.", n="error"),
      MC("¿ESTÁ BIEN 40 ÷ 6 = 7, RESTO 2?", ["NO", "SÍ"], "NO", "7 × 6 + 2 = 44.", n="analizar")],
"5": [N("RELÁMPAGO. 45 ÷ 9 = ___", 5, "5.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. RESTO DE 23 ÷ 4 = ___", 3, "3.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EL RESTO ES MENOR QUE…", ["EL DIVISOR", "EL COCIENTE"], "EL DIVISOR", "SI NO, HAY OTRA VUELTA.", tiempo=30, n="recordar"),
      N("RELÁMPAGO. 6 × 4 + 2 = ___", 26, "26.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, N("¿CUÁNTAS VECES SE RESTA 6 AL 18?", 3, "18, 12, 6, 0.", n="aplicar")],
 [1, N("¿CUÁNTAS VECES SE RESTA 7 AL 21?", 3, "21, 14, 7, 0.", n="aplicar")],
 [1, TF("AL DIVIDIR RESTANDO, EL RESULTADO ES LO QUE QUEDA AL FINAL.", "FALSO", "ES CUÁNTAS VECES RESTAMOS.", n="error")],
 [2, N("¿CUÁL ES EL COCIENTE DE 29 ÷ 7?", 4, "7 × 4 = 28.", n="aplicar")],
 [2, N("¿CUÁL ES EL COCIENTE DE 50 ÷ 8?", 6, "8 × 6 = 48.", n="aplicar")],
 [2, MC("PARA DIVIDIR CON LA TABLA BUSCAMOS EL NÚMERO…", ["MÁS CERCA SIN PASARSE", "MÁS GRANDE", "MÁS CHICO"], "MÁS CERCA SIN PASARSE", "NO SE PUEDE PASAR.", n="recordar")],
 [3, N("¿CUÁL ES EL RESTO DE 23 ÷ 4?", 3, "23 − 20.", n="aplicar")],
 [3, N("¿CUÁL ES EL RESTO DE 40 ÷ 6?", 4, "40 − 36.", n="aplicar")],
 [3, MC("SI DIVIDIMOS POR 5, ¿EL RESTO PUEDE SER 7?", ["NO", "SÍ"], "NO", "ES MENOR QUE 5.", n="analizar")],
 [4, N("COMPROBÁ 26 ÷ 4 = 6, RESTO 2: ¿CUÁNTO DA 6 × 4 + 2?", 26, "DA EL DIVIDENDO.", n="aplicar")],
 [4, MC("¿ESTÁ BIEN 23 ÷ 4 = 5, RESTO 3?", ["SÍ", "NO"], "SÍ", "5 × 4 + 3 = 23.", n="aplicar")],
 [4, MC("NICO COMPROBÓ 17 ÷ 3 = 5 HACIENDO SOLO 5 × 3. ¿QUÉ LE FALTÓ?", ["SUMAR EL RESTO 2", "NADA", "RESTAR 3"], "SUMAR EL RESTO 2", "15 + 2 = 17.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 15, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: división con resto", "examen_titulo": "Nivel jefe: división con resto",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-15.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
