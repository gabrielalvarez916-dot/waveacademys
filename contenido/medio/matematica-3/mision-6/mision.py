# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 6 · Algoritmos de suma y resta. Genera mision-6.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la granja de manzanas de Ana.
Niveles: 1 suma en columnas · 2 resta en columnas · 3 reagrupar y canjear · 4 controlar."""
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
"objetivo": "Vas a sumar en columnas.",
"vas_a_ver": ["Encolumnar", "Empezar por las unidades", "Sumar columna por columna"],
"secciones": [
 S(1, "Encolumnar", [
  P("Ana cosechó 3.241 y 2.516 manzanas."),
  P("Unidades debajo de unidades. Sumamos de <b>derecha a izquierda</b>."),
  IMG("3.241 + 2.516", "Columna por columna.", FG.columnas(3241, 2516, "+", 5757)),
 ]),
 S(1, "Paso a paso", [
  D("Suma en columnas", "Ponemos cada cifra en <b>su columna</b> y sumamos empezando por las unidades."),
  P("7, 5, 7 y 5: da 5.757."),
  IMG("432 + 251", "Con tres cifras también.", FG.columnas(432, 251, "+", 683)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la cuenta. La vas a usar en la carpeta."),
  IMG("Cuenta para resolver", "Completá el resultado.", FG.columnas(4132, 3405, "+", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Sumar", "planteo": "2.314 + 1.452.", "pasos": ["Unidades: 6. Decenas: 6.", "Centenas: 7. Miles: 3. Da 3.766."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "5.203 + 1.694.", "pasos": ["Unidades: ___ . Decenas: 9.", "Centenas: 8. Miles: ___ ."]},
"ejemplo_solo": {"titulo": "Sumá", "planteo": "¿Cuánto es 6.031 + 2.546?"},
"tip": {"titulo": "Derecha", "texto": "Siempre empezá por la derecha."},
"ojo": ["No corras las cifras.", "Unidades debajo de unidades."],
"resumen": [{"titulo": "Columnas", "texto": "Cada cifra en su lugar."}, {"titulo": "Empezar", "texto": "Por las unidades."}, {"titulo": "Sumar", "texto": "Columna por columna."}],
"glosario": [{"palabra": "Columna", "significado": "Fila hacia abajo de un mismo lugar."}, {"palabra": "Encolumnar", "significado": "Poner cada cifra en su columna."}],
"carpeta": ["Resolvé la cuenta en columnas: 4.132 + 3.405.", "¿Cuánto es 2.314 + 1.452?", "Leo corrió las cifras y le dio 7.000. ¿Cuánto es 4.132 + 3.405?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["7537", "7.537"], ["3766", "3.766"], ["7537", "7.537"]],
"soluciones": {"incompleto": "7. 6.", "solo": "8.577.", "carpeta": ["7.537.", "3.766.", "7.537."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a restar en columnas.",
"vas_a_ver": ["El más grande arriba", "Arriba menos abajo", "Columna por columna"],
"secciones": [
 S(1, "Arriba el más grande", [
  P("Ana tenía 7.586. Vendió 2.345."),
  P("Restamos de derecha a izquierda: <b>5.241</b>."),
  IMG("7.586 − 2.345", "Arriba menos abajo.", FG.columnas(7586, 2345, "−", 5241)),
 ]),
 S(1, "Paso a paso", [
  D("Resta en columnas", "El número <b>más grande</b> va arriba. En cada columna, arriba menos abajo."),
  P("Empezamos por las unidades."),
  IMG("869 − 425", "Con tres cifras también.", FG.columnas(869, 425, "−", 444)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la cuenta. La vas a usar en la carpeta."),
  IMG("Cuenta para resolver", "Completá el resultado.", FG.columnas(9874, 3512, "−", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Restar", "planteo": "6.958 − 4.023.", "pasos": ["Unidades: 5. Decenas: 3.", "Centenas: 9. Miles: 2. Da 2.935."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "8.769 − 5.142.", "pasos": ["Unidades: ___ . Decenas: 2.", "Centenas: 6. Miles: ___ ."]},
"ejemplo_solo": {"titulo": "Restá", "planteo": "¿Cuánto es 4.586 − 1.264?"},
"tip": {"titulo": "Arriba", "texto": "El más grande siempre arriba."},
"ojo": ["Arriba menos abajo.", "No des vuelta los números."],
"resumen": [{"titulo": "Arriba", "texto": "El más grande."}, {"titulo": "Empezar", "texto": "Por las unidades."}, {"titulo": "Restar", "texto": "Arriba menos abajo."}],
"glosario": [{"palabra": "Restar", "significado": "Sacar una cantidad."}, {"palabra": "Diferencia", "significado": "Lo que da la resta."}],
"carpeta": ["Resolvé la cuenta en columnas: 9.874 − 3.512.", "¿Cuánto es 6.958 − 4.023?", "Mía puso 3.512 arriba y 9.874 abajo. ¿Cuánto da bien la resta?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["6362", "6.362"], ["2935", "2.935"], ["6362", "6.362"]],
"soluciones": {"incompleto": "7. 3.", "solo": "3.322.", "carpeta": ["6.362.", "2.935.", "6.362."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a reagrupar y canjear.",
"vas_a_ver": ["Me llevo 1", "Abro un canasto", "Diez forman uno"],
"secciones": [
 S(1, "Me llevo 1", [
  P("8 + 5 = 13: escribo 3 y me llevo 1."),
  P("268 + 125 = <b>393</b>."),
  IMG("Me llevo 1", "El 1 va arriba de las decenas.", FG.columnas(268, 125, "+", 393, marcas=[("D", 1)])),
 ]),
 S(1, "Abro un canasto", [
  D("Canje", "Si arriba <b>no alcanza</b>, pedimos 1 a la columna de al lado: son 10 más."),
  P("342 − 127: 2 − 7 no alcanza. Queda 12 − 7."),
  IMG("El canje", "El 4 pasa a 3.", FG.columnas(342, 127, "−", 215, marcas=[("U", 12)], tachar=[("D", 3)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("Cuenta para resolver", "Con canje.", FG.columnas(5214, 1538, "−", vacio=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Me llevo 1", "planteo": "2.768 + 1.455.", "pasos": ["13: escribo 3, me llevo 1.", "Sigue igual. Da 4.223."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "3.506 − 1.248.", "pasos": ["6 − 8 no alcanza: 16 − 8 = ___ .", "Da ___ ."]},
"ejemplo_solo": {"titulo": "Resolvé", "planteo": "¿Cuánto es 4.587 + 2.635?"},
"tip": {"titulo": "Anotá arriba", "texto": "Escribí chiquito lo que te llevás."},
"ojo": ["Si pasa de 9, te llevás 1.", "Si no alcanza, pedí al lado."],
"resumen": [{"titulo": "Suma", "texto": "Me llevo 1."}, {"titulo": "Resta", "texto": "Canje."}, {"titulo": "Diez", "texto": "Forman uno."}],
"glosario": [{"palabra": "Reagrupar", "significado": "Juntar diez en uno."}, {"palabra": "Canjear", "significado": "Cambiar uno por diez."}],
"carpeta": ["Resolvé con canje: 5.214 − 1.538.", "¿Cuánto es 2.768 + 1.455?", "Tomi hizo 268 + 125 y le dio 3.813. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3676", "3.676"], ["4223", "4.223"], ["393"]],
"soluciones": {"incompleto": "8. 2.258.", "solo": "7.222.", "carpeta": ["3.676.", "4.223.", "393."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a controlar tus cuentas.",
"vas_a_ver": ["Estimar", "La resta con una suma", "Si no da, revisar"],
"secciones": [
 S(1, "Estimar", [
  P("2.768 + 1.455 da cerca de 3.000 + 1.000."),
  P("Si te da 3.000, hay un error: es <b>4.223</b>."),
  IMG("Estimar", "Tiene que dar cerca.", FG.cuentas([("3.000 + 1.000", "4.000"), ("exacto", "4.223")])),
 ]),
 S(1, "La resta con una suma", [
  D("Controlar", "Para controlar una resta, sumamos el <b>resultado</b> y lo que restamos."),
  P("5.214 − 1.538 = 3.676. Y 3.676 + 1.538 = 5.214."),
  IMG("Al revés", "Tiene que dar el de arriba.", FG.columnas(3676, 1538, "+", 5214)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las cuentas. Las vas a usar en la carpeta."),
  IMG("¿Están bien?", "Controlá cada una.", FG.cuentas([("4.500 − 1.200", "3.300"), ("6.300 + 2.400", "9.700")])),
 ]),
],
"ejemplo_completo": {"titulo": "Controlar", "planteo": "7.000 − 2.600 = 4.400.", "pasos": ["4.400 + 2.600 = 7.000.", "Está bien."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "8.300 − 3.100 = 5.200.", "pasos": ["5.200 + 3.100 = ___ .", "¿Está bien? ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Está bien 3.900 + 2.050 = 4.950?"},
"tip": {"titulo": "Dos controles", "texto": "Estimá y hacé la cuenta al revés."},
"ojo": ["Toda cuenta se puede controlar.", "Si no da, buscá el error."],
"resumen": [{"titulo": "Estimar", "texto": "Da cerca."}, {"titulo": "Al revés", "texto": "Resta con suma."}, {"titulo": "Revisar", "texto": "Si no da."}],
"glosario": [{"palabra": "Controlar", "significado": "Ver si está bien."}, {"palabra": "Error", "significado": "Algo que salió mal."}],
"carpeta": ["¿Está bien 4.500 − 1.200 = 3.300? Escribí la suma que lo controla.", "¿Está bien 6.300 + 2.400 = 9.700? ¿Cuánto da?", "Sofi dice que 2.768 + 1.455 = 3.000. ¿Cuánto da?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["4500", "4.500"], ["8700", "8.700"], ["4223", "4.223"]],
"soluciones": {"incompleto": "8.300. Sí.", "solo": "No: da 5.950.", "carpeta": ["3.300 + 1.200 = 4.500: está bien.", "No: da 8.700.", "4.223."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("ENCOLUMNAR", [LD("EN SU COLUMNA", "UNIDADES DEBAJO DE UNIDADES, DECENAS DEBAJO DE DECENAS, <b>Y ASÍ</b>."),
   LL("SI QUEDAN CORRIDAS, DA MAL.", "EL SIGNO VA A LA IZQUIERDA.")],
   {"modo": "columna", "cifras": 4}, {"modo": "columna", "cifras": 4}),
 T("DE DERECHA A IZQUIERDA", [LD("EMPEZAR", "SUMAMOS PRIMERO LAS <b>UNIDADES</b> Y VAMOS HACIA LA IZQUIERDA."),
   LL("UNA COLUMNA POR VEZ.", "EL RESULTADO VA ABAJO DE LA RAYA.")],
   {"modo": "columna", "cifras": 4}, {"modo": "columna", "cifras": 4}),
], "recuerda": [
 RC("ENCOLUMNAR", "CADA CIFRA VA DEBAJO DE OTRA DEL MISMO LUGAR.", "LAS UNIDADES DEL 3.241 SOBRE LAS DEL 2.516"),
 RC("SUMAR EN COLUMNAS", "EMPEZAMOS POR LAS UNIDADES Y SEGUIMOS A LA IZQUIERDA.", "2.314 + 1.452 = 3.766"),
]}
N2["leccion"] = {"temas": [
 T("EL MÁS GRANDE ARRIBA", [LD("ORDENAR LA CUENTA", "EN LA RESTA, EL NÚMERO <b>MÁS GRANDE</b> VA ARRIBA."),
   LL("ES DE DONDE SACAMOS.", "EL OTRO VA DEBAJO.")],
   {"modo": "columna", "cifras": 4, "op": "resta"}, {"modo": "columna", "cifras": 4, "op": "resta"}),
 T("ARRIBA MENOS ABAJO", [LD("CADA COLUMNA", "RESTAMOS <b>ARRIBA MENOS ABAJO</b>, EMPEZANDO POR LAS UNIDADES."),
   LL("NUNCA AL REVÉS.", "UNA COLUMNA POR VEZ.")],
   {"modo": "columna", "cifras": 4, "op": "resta"}, {"modo": "columna", "cifras": 4, "op": "resta"}),
], "recuerda": [
 RC("ARRIBA", "EN LA RESTA EL NÚMERO MÁS GRANDE VA ARRIBA.", "9.874 ARRIBA Y 3.512 ABAJO"),
 RC("RESTAR EN COLUMNAS", "EN CADA COLUMNA RESTAMOS ARRIBA MENOS ABAJO.", "6.958 − 4.023 = 2.935"),
]}
N3["leccion"] = {"temas": [
 T("ME LLEVO 1", [LD("REAGRUPAR", "SI UNA COLUMNA DA <b>10 O MÁS</b>, PASAMOS 1 AL LADO."),
   LL("DIEZ UNIDADES FORMAN UNA DECENA.", "EL 1 SE ANOTA ARRIBA.")],
   {"modo": "columna", "cifras": 4, "lleva": True}, {"modo": "columna", "cifras": 4, "lleva": True}),
 T("ABRO UN CANASTO", [LD("CANJEAR", "SI ARRIBA HAY <b>MENOS</b>, PEDIMOS AYUDA A LA IZQUIERDA."),
   LL("ESA CIFRA PIERDE UNO.", "LA NUESTRA GANA DIEZ.")],
   {"modo": "columna", "cifras": 4, "op": "resta", "lleva": True}, {"modo": "columna", "cifras": 4, "op": "resta", "lleva": True}),
], "recuerda": [
 RC("REAGRUPAR", "DIEZ DE UN LUGAR SE CAMBIAN POR UNO DE AL LADO.", "8 + 5 = 13: ESCRIBO 3 Y ME LLEVO 1"),
 RC("CANJEAR", "UNO DE AL LADO SE CAMBIA POR DIEZ.", "2 − 7 NO ALCANZA: 12 − 7 = 5"),
]}
N4["leccion"] = {"temas": [
 T("ESTIMAR PARA CONTROLAR", [LD("DA CERCA", "REDONDEAMOS AL MIL: EL RESULTADO TIENE QUE QUEDAR <b>CERCA</b>."),
   LL("SI DA MUY LEJOS, HAY UN ERROR.", "SE HACE ANTES O DESPUÉS.")],
   {"modo": "sumar4", "que": "estimar"}, {"modo": "columna", "cifras": 4, "que": "estimar"}),
 T("LA CUENTA AL REVÉS", [LD("CONTROLAR UNA RESTA", "SUMAMOS EL <b>RESULTADO</b> Y LO QUE RESTAMOS: TIENE QUE DAR EL DE ARRIBA."),
   LL("LA SUMA DESHACE LA RESTA.", "SI NO DA, REVISAMOS.")],
   {"modo": "columna", "cifras": 4, "op": "resta"}, {"modo": "columna", "cifras": 4, "op": "resta", "que": "control"}),
], "recuerda": [
 RC("ESTIMAR", "EL RESULTADO EXACTO TIENE QUE QUEDAR CERCA DEL ESTIMADO.", "2.768 + 1.455 DA CERCA DE 4.000"),
 RC("AL REVÉS", "UNA RESTA SE CONTROLA CON UNA SUMA.", "3.676 + 1.538 = 5.214"),
]}

ACT = {
"1": [N("¿CUÁNTO ES 2.314 + 1.452?", 3766, "COLUMNA POR COLUMNA.", n="aplicar"),
      N("¿CUÁNTO ES 6.031 + 2.546?", 8577, "UNIDADES: 7. DECENAS: 7.", n="aplicar"),
      MC("¿POR DÓNDE SE EMPIEZA A SUMAR EN COLUMNAS?", ["POR LAS UNIDADES", "POR LOS MILES", "POR EL MEDIO"], "POR LAS UNIDADES", "DE DERECHA A IZQUIERDA.", n="recordar"),
      MC("LEO CORRIÓ LAS CIFRAS EN 4.132 + 3.405. ¿CUÁNTO DA BIEN?", ["7.537", "7.000", "4.473"], "7.537", "UNIDADES DEBAJO DE UNIDADES.", n="error")],
"2": [N("¿CUÁNTO ES 6.958 − 4.023?", 2935, "ARRIBA MENOS ABAJO.", n="aplicar"),
      N("¿CUÁNTO ES 4.586 − 1.264?", 3322, "COLUMNA POR COLUMNA.", n="aplicar"),
      MC("MÍA PUSO 3.512 ARRIBA Y 9.874 ABAJO. ¿QUÉ VA ARRIBA?", ["9.874", "3.512"], "9.874", "EL MÁS GRANDE ARRIBA.", n="error"),
      N("[[problema]] ANA TENÍA 8.769 MANZANAS. VENDIÓ 5.142. ¿CUÁNTAS LE QUEDAN?", 3627, "8.769 − 5.142.", n="analizar")],
"3": [N("¿CUÁNTO ES 2.768 + 1.455?", 4223, "ME LLEVO 1 EN UNIDADES, DECENAS Y CENTENAS.", n="aplicar"),
      N("¿CUÁNTO ES 5.214 − 1.538?", 3676, "CANJE EN UNIDADES, DECENAS Y CENTENAS.", n="aplicar"),
      MC("TOMI HIZO 268 + 125 Y LE DIO 3.813. ¿CUÁNTO DA?", ["393", "3.813", "383"], "393", "ESCRIBO 3 Y ME LLEVO 1.", n="error"),
      MC("EN 342 − 127, ¿QUÉ PASA EN LAS UNIDADES?", ["NO ALCANZA: HAGO UN CANJE", "RESTO 7 − 2", "PONGO 0"], "NO ALCANZA: HAGO UN CANJE", "2 − 7 NO SE PUEDE.", n="analizar")],
"4": [MC("2.768 + 1.455 DA CERCA DE…", ["4.000", "3.000", "6.000"], "4.000", "3.000 + 1.000.", n="aplicar"),
      N("PARA CONTROLAR 7.000 − 2.600 = 4.400, ¿CUÁNTO DA 4.400 + 2.600?", 7000, "DA EL DE ARRIBA: ESTÁ BIEN.", n="aplicar"),
      MC("SOFI DICE QUE 6.300 + 2.400 = 9.700. ¿ESTÁ BIEN?", ["NO: DA 8.700", "SÍ"], "NO: DA 8.700", "6 + 2 = 8 MILES.", n="error"),
      CLAS("¿ESTÁ BIEN O MAL?", ["4.500 − 1.200 = 3.300", "3.900 + 2.050 = 4.950", "8.300 − 3.100 = 5.200", "2.000 + 2.500 = 5.500"], ["BIEN", "MAL"],
           {"4.500 − 1.200 = 3.300": "BIEN", "3.900 + 2.050 = 4.950": "MAL", "8.300 − 3.100 = 5.200": "BIEN", "2.000 + 2.500 = 5.500": "MAL"}, "ESTIMÁ O HACÉ LA CUENTA AL REVÉS.", n="analizar")],
"5": [N("RELÁMPAGO. 1.234 + 2.345 = ___", 3579, "3.579.", tiempo=40, n="aplicar"),
      N("RELÁMPAGO. 5.678 − 1.234 = ___", 4444, "4.444.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. 9 + 6 EN LAS UNIDADES…", ["ME LLEVO 1", "NO ME LLEVO"], "ME LLEVO 1", "DA 15.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. EN LA RESTA, ¿QUÉ VA ARRIBA?", ["EL MÁS GRANDE", "EL MÁS CHICO"], "EL MÁS GRANDE", "DE AHÍ SACAMOS.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 5.203 + 1.694?", 6897, "COLUMNA POR COLUMNA.", n="aplicar")],
 [1, N("¿CUÁNTO ES 3.120 + 4.567?", 7687, "DE DERECHA A IZQUIERDA.", n="aplicar")],
 [1, TF("EN LA SUMA EN COLUMNAS SE EMPIEZA POR LOS MILES.", "FALSO", "SE EMPIEZA POR LAS UNIDADES.", n="recordar")],
 [2, N("¿CUÁNTO ES 8.769 − 5.142?", 3627, "ARRIBA MENOS ABAJO.", n="aplicar")],
 [2, N("[[problema]] ANA TENÍA 9.874 MANZANAS. VENDIÓ 3.512. ¿CUÁNTAS LE QUEDAN?", 6362, "9.874 − 3.512.", n="analizar")],
 [2, MC("LEO PUSO 2.345 ARRIBA Y 7.586 ABAJO PARA RESTAR. ¿QUÉ HIZO MAL?", ["PUSO EL CHICO ARRIBA", "NADA"], "PUSO EL CHICO ARRIBA", "EL MÁS GRANDE VA ARRIBA.", n="error")],
 [3, N("¿CUÁNTO ES 4.587 + 2.635?", 7222, "ME LLEVO 1 VARIAS VECES.", n="aplicar")],
 [3, N("¿CUÁNTO ES 3.506 − 1.248?", 2258, "CANJE EN LAS UNIDADES.", n="aplicar")],
 [3, MC("EN 8 + 5 = 13, ¿QUÉ ESCRIBO?", ["3 Y ME LLEVO 1", "13", "1 Y ME LLEVO 3"], "3 Y ME LLEVO 1", "LA DECENA PASA AL LADO.", n="analizar")],
 [4, MC("¿CON QUÉ SE CONTROLA 5.214 − 1.538 = 3.676?", ["3.676 + 1.538", "3.676 − 1.538", "5.214 + 1.538"], "3.676 + 1.538", "LA SUMA DESHACE LA RESTA.", n="analizar")],
 [4, N("¿CUÁNTO DA BIEN 3.900 + 2.050?", 5950, "CERCA DE 6.000.", n="aplicar")],
 [4, MC("NICO HIZO 2.900 + 3.100 = 50.000. ¿ESTÁ BIEN?", ["NO: DA 6.000", "SÍ"], "NO: DA 6.000", "ESTIMÁ: 3.000 + 3.000.", n="error")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 6, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: algoritmos de suma y resta", "examen_titulo": "Nivel jefe: algoritmos de suma y resta",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
