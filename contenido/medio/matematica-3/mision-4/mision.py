# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 4 · Dinero y números grandes. Genera mision-4.json.
VARIANTE: lo que dice "vuelto" lleva su parte "neutro" ("cambio") para alumnos de otros países. Sin nombre de moneda: solo $ y dinero.
Regla de primeros años. Metáfora: la bicicletería de Don Beto (billetes de $100, $500, $1.000 y $2.000).
Niveles: 1 billetes de miles · 2 formar montos · 3 comparar precios · 4 pagar y calcular el vuelto."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), "matematica-1"))  # dibujos compartidos del Medio
import figuras as FG

D = lambda t, x, **k: {"tipo": "definicion", "titulo": t, "texto": x, **k}
P = lambda x, **k: {"tipo": "parrafo", "texto": x, **k}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
N = lambda p, r, e, **k: {"t": "numeric", "p": p, "o": {}, "r": {"acepta": [r]}, "e": e, **k}
TF = lambda p, ok, e, **k: {"t": "true_false", "p": p, "o": ["VERDADERO", "FALSO"], "r": {"correcta": ok}, "e": e, **k}
ORD = lambda p, o, orden, e, **k: {"t": "ordering", "p": p, "o": o, "r": {"orden": orden}, "e": e, **k}
UNIR = lambda p, iz, de, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": iz, "derecha": de}, "r": {"pares": pares}, "e": e, **k}
CLAS = lambda p, el, cats, r, e, **k: {"t": "classify", "p": p, "o": {"elementos": el, "categorias": cats}, "r": {"categorias": r}, "e": e, **k}
FB = lambda p, huecos, e, **k: {"t": "fill_blank", "p": p, "o": {}, "r": {"huecos": huecos}, "e": e, **k}
NEU = lambda p: {"neutro": {"p": p}}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a conocer billetes de miles.",
"vas_a_ver": ["Billetes de $100 y $500", "Billetes de $1.000 y $2.000", "Cuánto vale cada uno"],
"secciones": [
 S(1, "Los billetes", [
  P("En la bicicletería de Don Beto se paga con billetes."),
  P("Hay de $100, $500, <b>$1.000</b> y <b>$2.000</b>."),
  IMG("Billetes", "El número dice cuánto vale.", FG.dinero([100, 500, 1000, 2000])),
 ]),
 S(1, "Cambiar billetes", [
  D("Billete de mil", "Un billete de <b>$1.000</b> vale lo mismo que diez de $100."),
  P("Uno de $2.000 vale dos de $1.000."),
  IMG("Lo mismo", "$1.000 = diez de $100.", FG.cuentas([("10 de $100", "$1.000"), ("2 de $1.000", "$2.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los billetes. Los vas a usar en la carpeta."),
  IMG("Billetes para contar", "¿Cuánto dinero hay?", FG.dinero([2000, 1000, 1000, 500])),
 ]),
],
"ejemplo_completo": {"titulo": "Contar", "planteo": "Un billete de $2.000 y uno de $500.", "pasos": ["2.000 + 500.", "Hay $2.500."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Cambiá billetes.", "pasos": ["$1.000 = ___ billetes de $100.", "$2.000 = ___ billetes de $1.000."]},
"ejemplo_solo": {"titulo": "Contá", "planteo": "¿Cuánto son 3 billetes de $1.000?"},
"tip": {"titulo": "El que más vale", "texto": "Empezá a contar por el billete más grande."},
"ojo": ["Dos de $500 valen $1.000.", "El número del billete dice cuánto vale."],
"resumen": [{"titulo": "$1.000", "texto": "Diez de $100."}, {"titulo": "$2.000", "texto": "Dos de $1.000."}, {"titulo": "Contar", "texto": "Del más grande."}],
"glosario": [{"palabra": "Billete", "significado": "Papel que vale dinero."}, {"palabra": "Valor", "significado": "Cuánto dinero es."}],
"carpeta": ["En los billetes para contar, ¿cuánto dinero hay?", "¿Cuántos billetes de $100 forman $1.000?", "Leo cree que $500 y $1.000 valen igual. ¿Cuántos de $500 forman $1.000?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["4500", "4.500"], ["10"], ["2"]],
"soluciones": {"incompleto": "10. 2.", "solo": "$3.000.", "carpeta": ["$4.500.", "10.", "2."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a juntar montos grandes con billetes.",
"vas_a_ver": ["Separar miles y cientos", "Billetes para los miles", "Billetes para los cientos"],
"secciones": [
 S(1, "Separar", [
  P("El casco cuesta $3.700."),
  P("Lo separamos: <b>$3.000 + $700</b>."),
  IMG("El casco", "$3.000 y $700.", FG.cuentas([("miles", "$3.000"), ("cientos", "$700")])),
 ]),
 S(1, "Juntar con billetes", [
  D("Formar un monto", "Miles con billetes de <b>$1.000</b>. Cientos con $500 y $100."),
  P("Tres de $1.000, uno de $500 y dos de $100."),
  IMG("$3.700", "Billetes para el casco.", FG.dinero([1000, 1000, 1000, 500, 100, 100])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los montos. Los vas a usar en la carpeta."),
  IMG("Montos para formar", "¿Cuántos billetes?", FG.cuentas([("$5.300", "?"), ("$2.800", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Formar", "planteo": "Juntá $4.200.", "pasos": ["Cuatro de $1.000.", "Dos de $100."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Juntá $6.100.", "pasos": ["___ billetes de $1.000.", "___ billete de $100."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Cuánto son 2 de $2.000 y 3 de $100?"},
"tip": {"titulo": "Separá", "texto": "Primero los miles, después los cientos."},
"ojo": ["Miles con miles, cientos con cientos.", "4 de $1.000 y 3 de $100 son $4.300."],
"resumen": [{"titulo": "Separar", "texto": "Miles y cientos."}, {"titulo": "Miles", "texto": "Billetes de $1.000."}, {"titulo": "Cientos", "texto": "$500 y $100."}],
"glosario": [{"palabra": "Monto", "significado": "Cantidad de dinero."}, {"palabra": "Formar", "significado": "Juntar hasta llegar."}],
"carpeta": ["Para $5.300, ¿cuántos billetes de $1.000 usás?", "Para $2.800, ¿cuántos billetes de $100 usás si no usás de $500?", "Mía dice que 4 de $1.000 y 3 de $100 son $7.000. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["5"], ["8"], ["4300", "4.300"]],
"soluciones": {"incompleto": "6. 1.", "solo": "$4.300.", "carpeta": ["5.", "8.", "$4.300."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a comparar precios grandes.",
"vas_a_ver": ["Más caro y más barato", "Primero los miles", "Ordenar precios"],
"secciones": [
 S(1, "Más caro", [
  P("La bici cuesta $4.250. El monopatín, $4.520."),
  P("Miles empatan. Centenas: 2 y 5. Es más caro el <b>monopatín</b>."),
  IMG("Precios", "Comparamos como números.", FG.tarjetas([("$4.250", "bici"), ("$4.520", "monopatín")])),
 ]),
 S(1, "Ordenar precios", [
  D("Más caro", "Es el precio con el número <b>mayor</b>. Miramos primero los miles."),
  P("$8.900, $3.200 y $1.950."),
  IMG("Del más caro al más barato", "Miles primero.", FG.tarjetas([("$8.900", "bici grande"), ("$3.200", "patines"), ("$1.950", "casco")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los precios. Los vas a usar en la carpeta."),
  IMG("Precios para comparar", "¿Cuál es más caro?", FG.tarjetas([("$1.080", "timbre"), ("$1.800", "luz"), ("$1.008", "canasto")])),
 ]),
],
"ejemplo_completo": {"titulo": "Comparar", "planteo": "$6.080 o $6.800.", "pasos": ["Miles empatan.", "$6.800 es más caro."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Poné > o <.", "pasos": ["$2.900 ___ $3.100", "$7.450 ___ $7.405"]},
"ejemplo_solo": {"titulo": "Elegí", "planteo": "¿Cuál es más barato: $5.010 o $5.100?"},
"tip": {"titulo": "Como números", "texto": "Los precios se comparan como números."},
"ojo": ["$999 es más barato que $1.200.", "El cero también cuenta."],
"resumen": [{"titulo": "Primero", "texto": "Los miles."}, {"titulo": "Empate", "texto": "Las centenas."}, {"titulo": "Caro", "texto": "Número mayor."}],
"glosario": [{"palabra": "Caro", "significado": "Cuesta más."}, {"palabra": "Barato", "significado": "Cuesta menos."}],
"carpeta": ["En los precios para comparar, ¿cuál es el más caro?", "¿Cuál es el más barato?", "Tomi dice que $1.080 es más caro que $1.800. ¿Cuál es más caro?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["1800", "1.800"], ["1008", "1.008"], ["1800", "1.800"]],
"soluciones": {"incompleto": "<. >.", "solo": "$5.010.", "carpeta": ["$1.800 (la luz).", "$1.008 (el canasto).", "$1.800."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a pagar y calcular el vuelto.",
"neutro": {"objetivo": "Vas a pagar y calcular el cambio."},
"vas_a_ver": ["Pagar con más", "Contar para adelante", "Llegar al mil"],
"secciones": [
 S(1, "Pagar con más", [
  P("Tomi compra un timbre de $3.700. Paga con $4.000."),
  P("De 3.700 a 4.000 hay <b>300</b>."),
  IMG("Contar para adelante", "Tres saltos de 100.", FG.cuentas([("3.700 → 4.000", 300)])),
 ]),
 S(1, "El vuelto", [
  D("Vuelto", "Es lo que te devuelven cuando pagás <b>de más</b>.", neutro={"titulo": "Cambio", "texto": "Es lo que te devuelven cuando pagas <b>de más</b>."}),
  P("Cuesta $7.600, paga $10.000: le devuelven $2.400."),
  IMG("Dos saltos", "400 y 2.000.", FG.cuentas([("7.600 → 8.000", 400), ("8.000 → 10.000", "2.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las compras. Las vas a usar en la carpeta."),
  IMG("Compras", "Precio y pago.", FG.cuentas([("cuesta $1.800", "paga $2.000"), ("cuesta $5.500", "paga $6.000")])),
 ]),
],
"ejemplo_completo": {"titulo": "Contar", "planteo": "Cuesta $2.600. Paga $3.000.", "pasos": ["2.700, 2.800, 2.900, 3.000.", "Le devuelven $400."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿Cuánto le devuelven?", "pasos": ["Cuesta $4.900, paga $5.000: ___ .", "Cuesta $8.500, paga $9.000: ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "Cuesta $6.200. Paga con $7.000. ¿Cuánto le devuelven?"},
"tip": {"titulo": "Hasta el mil", "texto": "Primero saltá hasta el mil más cercano."},
"tip_neutro": None,
"ojo": ["De 3.700 a 4.000 hay 300, no 700.", "Si paga justo, no le devuelven nada."],
"resumen": [{"titulo": "Vuelto", "texto": "Lo que sobra.", "neutro": {"titulo": "Cambio", "texto": "Lo que sobra."}}, {"titulo": "Contar", "texto": "Del precio al pago."}, {"titulo": "Saltos", "texto": "Hasta el mil."}],
"glosario": [{"palabra": "Vuelto", "significado": "Dinero que te devuelven.", "neutro": {"palabra": "Cambio", "significado": "Dinero que te devuelven."}}, {"palabra": "Pagar", "significado": "Dar dinero por algo."}],
"carpeta": ["Cuesta $1.800 y paga $2.000. ¿Cuánto le devuelven?", "Cuesta $5.500 y paga $6.000. ¿Cuánto le devuelven?", "Leo dice que si cuesta $3.700 y paga $4.000 le devuelven $700. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["200"], ["500"], ["300"]],
"soluciones": {"incompleto": "$100. $500.", "solo": "$800.", "carpeta": ["$200.", "$500.", "$300."]},
}
del N4["tip_neutro"]

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("CONTAR BILLETES", [LD("CONTAR DINERO", "EMPEZAMOS POR EL BILLETE QUE <b>MÁS VALE</b> Y SUMAMOS LOS DEMÁS."),
   LL("HAY DE $100, $500, $1.000 Y $2.000.", "EL NÚMERO DICE CUÁNTO VALE.")],
   {"modo": "dinero4"}, {"modo": "dinero4"}),
 T("BILLETES QUE VALEN LO MISMO", [LD("CAMBIAR", "PODEMOS CAMBIAR UN BILLETE GRANDE POR <b>VARIOS CHICOS</b> QUE SUMAN IGUAL."),
   LL("CINCO DE CIEN SON QUINIENTOS.", "CUATRO DE QUINIENTOS SON DOS MIL.")],
   {"modo": "dinero4"}, {"modo": "dinero4"}),
], "recuerda": [
 RC("CONTAR DINERO", "SUMAMOS EMPEZANDO POR EL BILLETE QUE MÁS VALE.", "$2.000 + $500 = $2.500"),
 RC("CAMBIAR", "VARIOS BILLETES CHICOS PUEDEN VALER LO MISMO QUE UNO GRANDE.", "10 DE $100 = $1.000"),
]}
N2["leccion"] = {"temas": [
 T("SEPARAR EL MONTO", [LD("SEPARAR", "PARTIMOS EL MONTO EN <b>MILES</b> Y <b>CIENTOS</b>."),
   LL("$3.700 = $3.000 + $700.", "LOS MILES PRIMERO.")],
   {"modo": "dinero4", "que": "formar"}, {"modo": "dinero4", "que": "formar"}),
 T("JUNTAR CON BILLETES", [LD("FORMAR", "ELEGIMOS BILLETES PARA CADA PARTE HASTA <b>LLEGAR JUSTO</b> AL MONTO."),
   LL("PARA 6.100: SEIS DE MIL Y UNO DE CIEN.", "SE PUEDE ARMAR DE VARIAS MANERAS.")],
   {"modo": "dinero4", "que": "formar"}, {"modo": "dinero4"}),
], "recuerda": [
 RC("SEPARAR", "UN MONTO GRANDE SE PARTE EN MILES Y CIENTOS.", "$5.300 = $5.000 + $300"),
 RC("FORMAR", "PARA CADA PARTE ELEGIMOS LOS BILLETES QUE SIRVEN.", "$2.800: DOS DE $1.000 Y OCHO DE $100"),
]}
N3["leccion"] = {"temas": [
 T("MÁS CARO Y MÁS BARATO", [LD("COMPARAR PRECIOS", "LOS PRECIOS SE COMPARAN COMO NÚMEROS: PRIMERO LOS <b>MILES</b>."),
   LL("EL MAYOR ES EL MÁS CARO.", "EL MENOR ES EL MÁS BARATO.")],
   {"modo": "dinero4", "que": "caro"}, {"modo": "dinero4", "que": "caro"}),
 T("CUANDO LOS MILES EMPATAN", [LD("EMPATE", "SI LOS MILES SON IGUALES, MIRAMOS LAS <b>CENTENAS</b>."),
   LL("$4.520 ES MÁS CARO QUE $4.250.", "EL CERO TAMBIÉN CUENTA.")],
   {"modo": "dinero4", "que": "caro"}, {"modo": "comparar4"}),
], "recuerda": [
 RC("MÁS CARO", "ES EL PRECIO CON EL NÚMERO MAYOR.", "$6.800 ES MÁS CARO QUE $6.080"),
 RC("EMPATE", "SI LOS MILES SON IGUALES, DECIDEN LAS CENTENAS.", "$7.450 ES MÁS CARO QUE $7.405"),
]}
N4["leccion"] = {"temas": [
 T("CONTAR PARA ADELANTE", [LD("LO QUE TE DEVUELVEN", "CONTAMOS DESDE EL <b>PRECIO</b> HASTA LO QUE PAGAMOS."),
   LL("SALTAMOS DE 100 EN 100.", "LOS SALTOS SON LO QUE SOBRA.")],
   {"modo": "dinero4", "que": "vuelto"}, {"modo": "dinero4", "que": "vuelto"}),
 T("PAGAR CON 10.000", [LD("DOS SALTOS", "PRIMERO HASTA EL <b>MIL</b> MÁS CERCANO, DESPUÉS HASTA LO QUE PAGAMOS."),
   LL("$7.600 → $8.000: 400.", "$8.000 → $10.000: 2.000.")],
   {"modo": "dinero4", "que": "vuelto", "pago": 10000}, {"modo": "dinero4", "que": "vuelto", "pago": 10000}),
], "recuerda": [
 RC("CONTAR PARA ADELANTE", "VAMOS DEL PRECIO AL PAGO Y SUMAMOS LOS SALTOS.", "CUESTA $2.600, PAGAMOS $3.000: NOS DEVUELVEN $400"),
 RC("DOS SALTOS", "PRIMERO HASTA EL MIL Y DESPUÉS HASTA EL PAGO.", "CUESTA $7.600, PAGAMOS $10.000: NOS DEVUELVEN $2.400"),
]}

ACT = {
"1": [N("¿CUÁNTO SON 3 BILLETES DE $1.000?", 3000, "1.000, 2.000, 3.000.", n="aplicar"),
      N("¿CUÁNTOS BILLETES DE $100 FORMAN $1.000?", 10, "DIEZ DE CIEN.", n="aplicar"),
      MC("LEO DICE QUE UNO DE $500 VALE IGUAL QUE UNO DE $1.000. ¿CUÁNTOS DE $500 FORMAN $1.000?", ["2", "1", "5"], "2", "500 + 500 = 1.000.", n="error"),
      UNIR("UNÍ CADA GRUPO CON LO QUE VALE.", ["2 DE $1.000", "4 DE $500", "1 DE $2.000 Y 1 DE $500"], ["$2.500", "$2.000 ", "$2.000"], {"2 DE $1.000": "$2.000", "4 DE $500": "$2.000 ", "1 DE $2.000 Y 1 DE $500": "$2.500"}, "SUMÁ LOS BILLETES.", n="analizar", **NEU("UNE CADA GRUPO CON LO QUE VALE."))],
"2": [N("¿CUÁNTOS BILLETES DE $1.000 HACEN FALTA PARA $5.300?", 5, "LOS MILES: 5.", n="aplicar"),
      MC("¿CON QUÉ BILLETES SE FORMA $3.700?", ["3 DE $1.000, 1 DE $500 Y 2 DE $100", "3 DE $1.000 Y 7 DE $1.000", "37 DE $1.000"], "3 DE $1.000, 1 DE $500 Y 2 DE $100", "3.000 + 500 + 200.", n="analizar"),
      MC("MÍA DICE QUE 4 DE $1.000 Y 3 DE $100 SON $7.000. ¿CUÁNTO ES?", ["$4.300", "$7.000", "$430"], "$4.300", "MILES CON MILES.", n="error"),
      N("[[problema]] DON BETO JUNTA 2 DE $2.000 Y 3 DE $100. ¿CUÁNTO DINERO TIENE?", 4300, "4.000 + 300.", n="aplicar")],
"3": [MC("¿CUÁL ES MÁS CARO: $6.080 O $6.800?", ["$6.800", "$6.080"], "$6.800", "CENTENAS: 8 Y 0.", n="aplicar"),
      ORD("ORDENÁ DEL MÁS BARATO AL MÁS CARO.", ["$3.200", "$8.900", "$1.950"], ["$1.950", "$3.200", "$8.900"], "PRIMERO LOS MILES.", n="aplicar", **NEU("ORDENA DEL MÁS BARATO AL MÁS CARO.")),
      MC("TOMI DICE QUE $1.080 ES MÁS CARO QUE $1.800. ¿CUÁL ES MÁS CARO?", ["$1.800", "$1.080"], "$1.800", "CENTENAS: 8 Y 0.", n="error"),
      CLAS("¿CUESTA MÁS O MENOS DE $5.000?", ["$4.990", "$5.100", "$900", "$7.000"], ["MENOS DE $5.000", "MÁS DE $5.000"], {"$4.990": "MENOS DE $5.000", "$5.100": "MÁS DE $5.000", "$900": "MENOS DE $5.000", "$7.000": "MÁS DE $5.000"}, "MIRÁ LOS MILES.", n="analizar")],
"4": [N("CUESTA $2.600 Y PAGA $3.000. ¿CUÁNTO LE DEVUELVEN?", 400, "2.700, 2.800, 2.900, 3.000.", n="aplicar"),
      N("[[problema]] UN INFLADOR CUESTA $7.600. PAGA CON $10.000. ¿CUÁNTO LE DEVUELVEN?", 2400, "400 + 2.000.", n="analizar"),
      MC("LEO DICE QUE SI CUESTA $3.700 Y PAGA $4.000 LE DEVUELVEN $700. ¿CUÁNTO ES?", ["$300", "$700", "$1.300"], "$300", "DE 3.700 A 4.000 HAY 300.", n="error"),
      TF("SI PAGA JUSTO, NO LE DAN VUELTO.", "VERDADERO", "NO SOBRA NADA.", n="recordar", **NEU("SI PAGA JUSTO, NO LE DAN CAMBIO."))],
"5": [N("RELÁMPAGO. 2 BILLETES DE $2.000 SON $___", 4000, "4.000.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ES MÁS BARATO?", ["$5.010", "$5.100"], "$5.010", "CENTENAS.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. CUESTA $4.900, PAGA $5.000. ¿VUELTO?", 100, "100.", tiempo=30, n="aplicar", **NEU("RELÁMPAGO. CUESTA $4.900, PAGA $5.000. ¿CAMBIO?")),
      N("RELÁMPAGO. ¿CUÁNTOS DE $500 FORMAN $2.000?", 4, "4.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 1 DE $2.000, 2 DE $1.000 Y 1 DE $500?", 4500, "2.000 + 2.000 + 500.", n="aplicar")],
 [1, MC("¿CUÁNTOS BILLETES DE $1.000 FORMAN $2.000?", ["2", "20", "1"], "2", "MIL Y MIL.", n="recordar")],
 [1, TF("DIEZ BILLETES DE $100 VALEN LO MISMO QUE UNO DE $1.000.", "VERDADERO", "10 × 100 = 1.000.", n="recordar")],
 [2, N("PARA $6.100, ¿CUÁNTOS BILLETES DE $1.000 SE USAN?", 6, "LOS MILES: 6.", n="aplicar")],
 [2, N("[[problema]] TOMI TIENE 3 DE $1.000 Y 6 DE $100. ¿CUÁNTO DINERO TIENE?", 3600, "3.000 + 600.", n="aplicar")],
 [2, MC("SOFI FORMA $2.800 CON 2 DE $1.000 Y 8 DE $1.000. ¿ESTÁ BIEN?", ["NO: SON 8 DE $100", "SÍ"], "NO: SON 8 DE $100", "LOS CIENTOS VAN CON $100.", n="error")],
 [3, MC("¿CUÁL ES MÁS CARO: $7.450 O $7.405?", ["$7.450", "$7.405"], "$7.450", "DECENAS: 5 Y 0.", n="aplicar")],
 [3, ORD("ORDENÁ DEL MÁS CARO AL MÁS BARATO.", ["$2.090", "$9.020", "$2.900"], ["$9.020", "$2.900", "$2.090"], "MILES Y DESPUÉS CENTENAS.", n="analizar", **NEU("ORDENA DEL MÁS CARO AL MÁS BARATO."))],
 [3, TF("$999 ES MÁS CARO QUE $1.200.", "FALSO", "1.200 TIENE CUATRO CIFRAS.", n="error")],
 [4, N("CUESTA $6.200 Y PAGA CON $7.000. ¿CUÁNTO LE DEVUELVEN?", 800, "DE 6.200 A 7.000 HAY 800.", n="aplicar")],
 [4, N("[[problema]] UNA BICI CUESTA $8.500. PAGA CON $10.000. ¿CUÁNTO LE DEVUELVEN?", 1500, "500 + 1.000.", n="analizar")],
 [4, MC("CUESTA $5.500 Y PAGA $6.000. LE DAN $500. ¿ESTÁ BIEN?", ["SÍ", "NO"], "SÍ", "DE 5.500 A 6.000 HAY 500.", n="analizar")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 4, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: dinero y números grandes", "examen_titulo": "Nivel jefe: dinero y números grandes",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
