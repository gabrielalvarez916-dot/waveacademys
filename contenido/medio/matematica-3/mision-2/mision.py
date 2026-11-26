# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 2 · Comparar y ordenar hasta 10.000. Genera mision-2.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: los puntos del videojuego de Nico.
Niveles: 1 mayor y menor · 2 ordenar · 3 anterior y siguiente · 4 la recta hasta 10.000."""
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
"objetivo": "Vas a comparar números hasta el 10.000.",
"vas_a_ver": ["Mayor y menor", "Primero los miles", "Si empatan, las centenas"],
"secciones": [
 S(1, "Los puntos de Nico", [
  P("Nico hizo 4.735 puntos. Su hermana, 4.753."),
  P("Miles y centenas empatan. Gana <b>4.753</b>."),
  IMG("¿Quién ganó?", "Comparamos lugar por lugar.", FG.tarjetas([("4.735", "Nico"), ("4.753", "su hermana")])),
 ]),
 S(1, "Cómo comparar", [
  D("Comparar", "Miramos primero los <b>miles</b>. Si empatan, las centenas."),
  P("Más cifras, número más grande."),
  IMG("Mayor y menor", "6.190 es mayor que 6.099.", FG.tarjetas([("6.190", "mayor"), ("6.099", "menor")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas para comparar", "Elegí el mayor de cada par.", FG.tarjetas([("8.214", ""), ("8.241", ""), ("999", ""), ("1.001", "")])),
 ]),
],
"ejemplo_completo": {"titulo": "Comparar", "planteo": "¿Cuál es mayor: 5.618 o 5.681?", "pasos": ["Miles y centenas empatan.", "Decenas: 1 y 8. Gana 5.681."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Poné > o <.", "pasos": ["3.205 ___ 3.502", "9.000 ___ 8.999"]},
"ejemplo_solo": {"titulo": "Elegí", "planteo": "¿Cuál es menor: 7.430 o 7.403?"},
"tip": {"titulo": "De izquierda a derecha", "texto": "Compará cifra por cifra."},
"ojo": ["999 es menor que 1.000.", "Si empatan, mirá el lugar de al lado."],
"resumen": [{"titulo": "Primero", "texto": "Los miles."}, {"titulo": "Empate", "texto": "Las centenas."}, {"titulo": "Más cifras", "texto": "Más grande."}],
"glosario": [{"palabra": "Mayor", "significado": "El que tiene más."}, {"palabra": "Menor", "significado": "El que tiene menos."}],
"carpeta": ["En las tarjetas, ¿cuál es mayor: 8.214 o 8.241?", "¿Cuál es mayor: 999 o 1.001?", "Leo dice que 999 es mayor que 1.001 porque tiene nueves. ¿Cuál es mayor?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["8241", "8.241"], ["1001", "1.001"], ["1001", "1.001"]],
"soluciones": {"incompleto": "<. >.", "solo": "7.403.", "carpeta": ["8.241.", "1.001.", "1.001: tiene cuatro cifras."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ordenar números de cuatro cifras.",
"vas_a_ver": ["De menor a mayor", "De mayor a menor", "La tabla de puntos"],
"secciones": [
 S(1, "La tabla de puntos", [
  P("Mía 5.280, Nico 5.208 y Leo 2.850."),
  P("De mayor a menor: <b>5.280, 5.208, 2.850</b>."),
  IMG("Tabla de puntos", "De mayor a menor.", FG.tarjetas([("5.280", "Mía"), ("5.208", "Nico"), ("2.850", "Leo")])),
 ]),
 S(1, "Ordenar", [
  D("Ordenar", "Buscamos el más chico, después el que sigue y así."),
  P("De menor a mayor: 2.850, 5.208, 5.280."),
  IMG("De menor a mayor", "Cada vagón es más grande.", FG.tren_paso(2000, 6000, 1000)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Tarjetas para ordenar", "Ordená de menor a mayor.", FG.tarjetas([("3.420", ""), ("3.042", ""), ("3.402", "")])),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenar", "planteo": "Ordená 6.150, 1.650 y 6.105.", "pasos": ["El más chico: 1.650.", "Después 6.105 y 6.150."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "De menor a mayor.", "pasos": ["4.009, ___ , 4.900", "Usá: 4.090"]},
"ejemplo_solo": {"titulo": "Ordená", "planteo": "De mayor a menor: 7.300, 7.030, 7.003."},
"tip": {"titulo": "Uno por uno", "texto": "Buscá primero el más chico."},
"ojo": ["El cero también cuenta.", "Mirá los miles primero."],
"resumen": [{"titulo": "Ordenar", "texto": "De a uno."}, {"titulo": "Menor a mayor", "texto": "Sube."}, {"titulo": "Mayor a menor", "texto": "Baja."}],
"glosario": [{"palabra": "Ordenar", "significado": "Poner en fila según el tamaño."}, {"palabra": "Tabla", "significado": "Lista ordenada."}],
"carpeta": ["En las tarjetas, ¿qué número va primero de menor a mayor?", "¿Qué número va último de menor a mayor?", "Sofi puso 3.420 primero. ¿Cuál va primero de menor a mayor?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3042", "3.042"], ["3420", "3.420"], ["3042", "3.042"]],
"soluciones": {"incompleto": "4.090.", "solo": "7.300, 7.030, 7.003.", "carpeta": ["3.042.", "3.420.", "3.042."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a buscar el anterior y el siguiente.",
"vas_a_ver": ["Uno más", "Uno menos", "Cuando se llena un mil"],
"secciones": [
 S(1, "Uno más y uno menos", [
  P("El <b>siguiente</b> es uno más. El <b>anterior</b> es uno menos."),
  P("Anterior de 6.215: 6.214. Siguiente: 6.216."),
  IMG("Vecinos", "Anterior, número y siguiente.", FG.recta_num(6213, 6218, marcas=[(6214, "ANTERIOR"), (6216, "SIGUIENTE")])),
 ]),
 S(1, "Se llena un mil", [
  D("Siguiente", "Después del <b>3.999</b> viene el <b>4.000</b>."),
  P("Antes del 7.000 va el 6.999."),
  IMG("Del 3.999 al 4.000", "Se llena un mil.", FG.recta_num(3996, 4002, marcas=[(3999, ""), (4000, "4.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los vecinos. Los vas a usar en la carpeta."),
  IMG("Vecinos para completar", "Escribí el anterior y el siguiente.", FG.cuentas([("antes de 5.000", 4999), ("después de 8.499", 8500)], ocultar=(0, 1))),
 ]),
],
"ejemplo_completo": {"titulo": "Vecinos", "planteo": "Anterior y siguiente de 2.540.", "pasos": ["Uno menos: 2.539.", "Uno más: 2.541."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí los vecinos.", "pasos": ["___ , 1.300, 1.301", "8.998, 8.999, ___"]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuál es el anterior de 3.000?"},
"tip": {"titulo": "Cuidado con el 9", "texto": "Después del 9, cambia el lugar de al lado."},
"ojo": ["Antes del 7.000 va el 6.999.", "No es 7.999."],
"resumen": [{"titulo": "Siguiente", "texto": "Uno más."}, {"titulo": "Anterior", "texto": "Uno menos."}, {"titulo": "3.999", "texto": "Y después 4.000."}],
"glosario": [{"palabra": "Anterior", "significado": "El que va antes."}, {"palabra": "Siguiente", "significado": "El que va después."}],
"carpeta": ["¿Qué número va antes del 5.000?", "¿Qué número va después del 8.499?", "Leo dice que antes del 7.000 va el 7.999. ¿Qué número va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["4999", "4.999"], ["8500", "8.500"], ["6999", "6.999"]],
"soluciones": {"incompleto": "1.299. 9.000.", "solo": "2.999.", "carpeta": ["4.999.", "8.500.", "6.999."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ubicar números en la recta hasta 10.000.",
"vas_a_ver": ["La recta de mil en mil", "La mitad: 5.000", "Entre qué miles"],
"secciones": [
 S(1, "La recta", [
  P("La recta va del 0 al 10.000, de mil en mil."),
  P("El <b>5.000</b> está en la mitad."),
  IMG("Recta hasta 10.000", "De mil en mil.", FG.recta_miles([(5000, "MITAD")])),
 ]),
 S(1, "Entre qué miles", [
  D("Ubicar", "Miramos los <b>miles</b>: 6.400 está entre 6.000 y 7.000."),
  P("Más a la derecha, más grande."),
  IMG("El 6.400", "Entre 6.000 y 7.000.", FG.recta_miles([(6400, "6.400")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la recta. La vas a usar en la carpeta."),
  IMG("Recta para completar", "¿Qué números son?", FG.recta_miles([(3000, "A"), (8500, "B")])),
 ]),
],
"ejemplo_completo": {"titulo": "Ubicar", "planteo": "¿Dónde va el 2.500?", "pasos": ["Tiene 2 miles.", "Va entre 2.000 y 3.000, en el medio."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Entre qué miles está.", "pasos": ["4.700: entre 4.000 y ___ .", "9.100: entre ___ y 10.000."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Qué está más a la derecha: 3.800 o 8.300?"},
"tip": {"titulo": "Mirá los miles", "texto": "Los miles dicen dónde empieza."},
"ojo": ["Los grandes van a la derecha.", "5.000 es la mitad de 10.000."],
"resumen": [{"titulo": "Recta", "texto": "De mil en mil."}, {"titulo": "5.000", "texto": "La mitad."}, {"titulo": "Derecha", "texto": "Más grande."}],
"glosario": [{"palabra": "Recta", "significado": "Línea con los números en orden."}, {"palabra": "Mitad", "significado": "El medio justo."}],
"carpeta": ["En la recta, ¿qué número es la letra A?", "¿Qué número es la letra B?", "Nico pone el 900 a la derecha del 9.000. ¿Cuál va a la derecha?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["3000", "3.000"], ["8500", "8.500"], ["9000", "9.000"]],
"soluciones": {"incompleto": "5.000. 9.000.", "solo": "8.300.", "carpeta": ["3.000.", "8.500.", "9.000."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("MAYOR Y MENOR", [LD("COMPARAR", "MIRAMOS PRIMERO LOS <b>MILES</b>. SI EMPATAN, LAS CENTENAS."),
   LL("GANA EL QUE TIENE MÁS.", "SI EMPATAN, SEGUIMOS AL LADO.")],
   {"modo": "comparar4"}, {"modo": "comparar4"}),
 T("CIFRA POR CIFRA", [LD("EMPATE", "SI LOS MILES EMPATAN, MIRAMOS <b>CENTENAS</b>, DESPUÉS DECENAS Y UNIDADES."),
   LL("DE IZQUIERDA A DERECHA.", "LA PRIMERA DIFERENTE DECIDE.")],
   {"modo": "comparar4"}, {"modo": "comparar4"}),
], "recuerda": [
 RC("COMPARAR", "MIRAMOS LOS MILES Y, SI EMPATAN, LAS CENTENAS.", "6.190 ES MAYOR QUE 6.099"),
 RC("MÁS CIFRAS", "UN NÚMERO DE CUATRO CIFRAS LE GANA A UNO DE TRES.", "1.000 ES MAYOR QUE 999"),
]}
N2["leccion"] = {"temas": [
 T("DE MENOR A MAYOR", [LD("ORDENAR", "BUSCAMOS EL MÁS <b>CHICO</b>, DESPUÉS EL QUE SIGUE Y ASÍ."),
   LL("PRIMERO LOS MILES.", "SI EMPATAN, LAS CENTENAS.")],
   {"modo": "orden4"}, {"modo": "orden4"}),
 T("DE MAYOR A MENOR", [LD("AL REVÉS", "PARA BAJAR, EMPEZAMOS POR EL MÁS <b>GRANDE</b>."),
   LL("COMO UNA TABLA DE PUNTOS.", "EL PRIMERO ES EL QUE GANA.")],
   {"modo": "orden4", "orden": "desc"}, {"modo": "orden4", "orden": "desc"}),
], "recuerda": [
 RC("MENOR A MAYOR", "EMPEZAMOS POR EL NÚMERO MÁS CHICO.", "2.850, 5.208, 5.280"),
 RC("MAYOR A MENOR", "EMPEZAMOS POR EL NÚMERO MÁS GRANDE.", "7.300, 7.030, 7.003"),
]}
N3["leccion"] = {"temas": [
 T("ANTERIOR Y SIGUIENTE", [LD("VECINOS", "EL <b>ANTERIOR</b> ES UNO MENOS Y EL <b>SIGUIENTE</b>, UNO MÁS."),
   LL("EL ANTERIOR VA A LA IZQUIERDA.", "EL SIGUIENTE VA A LA DERECHA.")],
   {"modo": "vecinos4"}, {"modo": "vecinos4"}),
 T("CUANDO SE LLENA UN MIL", [LD("CAMBIO", "DESPUÉS DEL <b>3.999</b> VIENE EL <b>4.000</b>: SE LLENA UN MIL."),
   LL("ANTES DEL 7.000 VA EL 6.999.", "CAMBIAN VARIAS CIFRAS JUNTAS.")],
   {"modo": "serie", "de": 1, "desde": 2996, "hasta": 2996}, {"modo": "vecinos4"}),
], "recuerda": [
 RC("SIGUIENTE", "EL SIGUIENTE ES EL NÚMERO QUE TIENE UNO MÁS.", "DESPUÉS DEL 2.540 VA EL 2.541"),
 RC("ANTERIOR", "EL ANTERIOR ES EL NÚMERO QUE TIENE UNO MENOS.", "ANTES DEL 3.000 VA EL 2.999"),
]}
N4["leccion"] = {"temas": [
 T("LA RECTA HASTA 10.000", [LD("LA RECTA NUMÉRICA", "LOS NÚMEROS VAN EN FILA; CADA MARCA SUMA <b>1.000</b>."),
   LL("CERO A LA IZQUIERDA, DIEZ MIL AL FINAL.", "CUANTO MÁS LEJOS DEL CERO, MAYOR.")],
   {"modo": "recta10000"}, {"modo": "recta10000"}),
 T("ENTRE QUÉ MILES", [LD("UBICAR", "MIRAMOS LOS <b>MILES</b>: 6.400 ESTÁ ENTRE 6.000 Y 7.000."),
   LL("LOS MILES DICEN DÓNDE EMPIEZA.", "EL 500 ES LA MITAD DEL TRAMO.")],
   {"modo": "recta10000"}, {"modo": "recta10000", "que": "entre"}),
], "recuerda": [
 RC("LA RECTA", "LOS NÚMEROS VAN EN ORDEN DE MIL EN MIL.", "0, 1.000, 2.000… 10.000"),
 RC("UBICAR", "LOS MILES DICEN ENTRE QUÉ MARCAS ESTÁ EL NÚMERO.", "4.700 ESTÁ ENTRE 4.000 Y 5.000"),
]}

ACT = {
"1": [MC("¿CUÁL ES MAYOR: 5.618 O 5.681?", ["5.681", "5.618"], "5.681", "DECENAS: 8 LE GANA A 1.", n="aplicar"),
      MC("LEO DICE QUE 999 ES MAYOR QUE 1.001 PORQUE TIENE NUEVES. ¿CUÁL ES MAYOR?", ["1.001", "999"], "1.001", "TIENE CUATRO CIFRAS.", n="error"),
      CLAS("¿ES MAYOR O MENOR QUE 5.000?", ["4.999", "5.010", "6.000", "999"], ["MENOR QUE 5.000", "MAYOR QUE 5.000"],
           {"4.999": "MENOR QUE 5.000", "5.010": "MAYOR QUE 5.000", "6.000": "MAYOR QUE 5.000", "999": "MENOR QUE 5.000"}, "MIRÁ LOS MILES.", n="analizar"),
      FB("PONÉ > O <: 3.205 ___ 3.502", [["<"]], "3 CENTENAS Y 5 CENTENAS.", n="aplicar")],
"2": [ORD("ORDENÁ DE MENOR A MAYOR.", ["6.150", "1.650", "6.105"], ["1.650", "6.105", "6.150"], "PRIMERO LOS MILES.", n="aplicar"),
      ORD("ORDENÁ DE MAYOR A MENOR.", ["7.030", "7.003", "7.300"], ["7.300", "7.030", "7.003"], "MIRÁ LAS CENTENAS.", n="aplicar"),
      MC("SOFI ORDENÓ: 3.420, 3.042, 3.402. ¿CUÁL VA PRIMERO DE MENOR A MAYOR?", ["3.042", "3.420", "3.402"], "3.042", "TIENE 0 CENTENAS.", n="error"),
      N("[[problema]] EN LA TABLA HAY 4.090, 4.009 Y 4.900 PUNTOS. ¿CUÁNTOS TIENE EL QUE GANA?", 4900, "4.900 TIENE 9 CENTENAS.", n="analizar")],
"3": [N("¿QUÉ NÚMERO VA DESPUÉS DEL 2.540?", 2541, "UNO MÁS.", n="aplicar"),
      N("¿QUÉ NÚMERO VA ANTES DEL 3.000?", 2999, "UNO MENOS: 2.999.", n="aplicar"),
      MC("LEO DICE QUE ANTES DEL 7.000 VA EL 7.999. ¿QUÉ NÚMERO VA?", ["6.999", "7.999", "7.001"], "6.999", "BAJA UN MIL.", n="error"),
      UNIR("UNÍ CADA NÚMERO CON SU SIGUIENTE.", ["1.299", "1.209", "1.290"], ["1.291", "1.300", "1.210"], {"1.299": "1.300", "1.209": "1.210", "1.290": "1.291"}, "SUMÁ UNO.", n="analizar")],
"4": [N("¿QUÉ NÚMERO ESTÁ EN LA MITAD DEL 0 Y EL 10.000?", 5000, "LA MITAD ES 5.000.", n="aplicar"),
      MC("¿ENTRE QUÉ MILES ESTÁ EL 4.700?", ["4.000 Y 5.000", "7.000 Y 8.000", "3.000 Y 4.000"], "4.000 Y 5.000", "TIENE 4 MILES.", n="aplicar"),
      MC("NICO DICE QUE 900 VA MÁS A LA DERECHA QUE 9.000. ¿CUÁL VA MÁS A LA DERECHA?", ["9.000", "900"], "9.000", "LOS GRANDES VAN A LA DERECHA.", n="error"),
      ORD("ORDENÁ COMO EN LA RECTA, DE IZQUIERDA A DERECHA.", ["8.300", "3.800", "3.080"], ["3.080", "3.800", "8.300"], "A LA IZQUIERDA, LOS MÁS CHICOS.", n="analizar")],
"5": [MC("RELÁMPAGO. ¿CUÁL ES MAYOR?", ["2.010", "2.001"], "2.010", "1 DECENA.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿QUÉ VA DESPUÉS DEL 5.999?", 6000, "6.000.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ES MENOR?", ["8.888", "8.898"], "8.888", "DECENAS: 8 Y 9.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. ¿QUÉ VA ANTES DEL 1.000?", 999, "999.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿CUÁL ES MAYOR: 7.430 O 7.403?", ["7.430", "7.403"], "7.430", "DECENAS: 3 Y 0.", n="aplicar")],
 [1, TF("9.000 ES MAYOR QUE 8.999.", "VERDADERO", "TIENE 9 MILES.", n="recordar")],
 [1, MC("MÍA DICE QUE 4.099 ES MAYOR QUE 4.100. ¿CUÁL ES MAYOR?", ["4.100", "4.099"], "4.100", "CENTENAS: 1 LE GANA A 0.", n="error")],
 [2, ORD("ORDENÁ DE MENOR A MAYOR.", ["9.120", "1.920", "9.012"], ["1.920", "9.012", "9.120"], "PRIMERO LOS MILES.", n="aplicar")],
 [2, MC("DE MAYOR A MENOR, ¿CUÁL VA PRIMERO?", ["6.510", "6.501", "6.150"], "6.510", "MIRÁ LAS DECENAS.", n="aplicar")],
 [2, N("[[problema]] LEO HIZO 3.300 PUNTOS. MÍA HIZO 3.030. NICO HIZO 3.003. ¿CUÁNTOS HIZO EL ÚLTIMO?", 3003, "EL MÁS CHICO ES 3.003.", n="analizar")],
 [3, N("¿QUÉ NÚMERO VA DESPUÉS DEL 6.299?", 6300, "SE LLENA UNA CENTENA.", n="aplicar")],
 [3, N("¿QUÉ NÚMERO VA ANTES DEL 9.000?", 8999, "UNO MENOS.", n="aplicar")],
 [3, TF("EL ANTERIOR DE 5.000 ES 5.999.", "FALSO", "ES 4.999.", n="error")],
 [4, MC("¿CUÁL ES LA MITAD DE LA RECTA HASTA 10.000?", ["5.000", "1.000", "9.000"], "5.000", "LA MITAD.", n="recordar")],
 [4, MC("¿ENTRE QUÉ MILES ESTÁ EL 2.500?", ["2.000 Y 3.000", "5.000 Y 6.000", "1.000 Y 2.000"], "2.000 Y 3.000", "TIENE 2 MILES.", n="aplicar")],
 [4, CLAS("EN LA RECTA, ¿VA ANTES O DESPUÉS DEL 5.000?", ["4.800", "5.200", "7.000", "500"], ["ANTES", "DESPUÉS"], {"4.800": "ANTES", "5.200": "DESPUÉS", "7.000": "DESPUÉS", "500": "ANTES"}, "LOS MÁS CHICOS VAN ANTES.", n="analizar")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 2, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: comparar y ordenar hasta 10.000", "examen_titulo": "Nivel jefe: comparar y ordenar hasta 10.000",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-2.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
