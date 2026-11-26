# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 6 · Dinero hasta 1.000. Genera mision-6.json.
VARIANTE: lo que nombra los pesos lleva su parte "neutro" (dinero, sin nombre de moneda) para alumnos de otros países.
Regla de primeros años. Metáfora: el kiosco de alfajores de la abuela Rosa.
Niveles: 1 billetes y monedas · 2 formar un monto · 3 calcular el vuelto · 4 comprar y comparar precios."""
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
NEU = lambda p: {"neutro": {"p": p}}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a conocer billetes y monedas hasta $1.000.",
"vas_a_ver": ["Billetes y monedas", "El número dice cuánto vale", "Contar billetes iguales"],
"secciones": [
 S(1, "El kiosco de Rosa", [
  P("En el kiosco de Rosa pagan con <b>pesos</b>.", neutro={"texto": "En el kiosco de Rosa pagan con <b>dinero</b>."}),
  D("Billete y moneda", "El <b>billete</b> es de papel. La <b>moneda</b> es de metal."),
  IMG("Billetes y monedas", "El número dice cuánto vale.", FG.dinero([10, 20, 50, 100, 200, 500])),
 ]),
 S(1, "Billetes iguales", [
  P("Tres billetes de $100: <b>100, 200, 300</b>."),
  P("Son <b>$300</b>.", neutro={"texto": "Son <b>$300</b>."}),
  IMG("Tres billetes de $100", "Son $300.", FG.dinero([100, 100, 100], "$300")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los billetes. Los vas a usar en la carpeta."),
  IMG("La caja de Rosa", "Contá los billetes.", FG.dinero([100, 100, 100, 100, 100])),
 ]),
],
"ejemplo_completo": {"titulo": "Billetes de $200", "planteo": "Rosa tiene 3 billetes de $200.", "pasos": ["200.", "400.", "600.", "Tiene $600."]},
"ejemplo_incompleto": {"titulo": "Billetes de $100", "planteo": "Completá.", "pasos": ["$100, $200, $300, ___ .", "4 billetes de $100 son ___ ."]},
"ejemplo_solo": {"titulo": "Dos billetes", "planteo": "¿Cuánto son 2 billetes de $500?"},
"tip": {"titulo": "Mirá el número", "texto": "El número del billete dice cuánto vale."},
"ojo": ["Un billete de $100 vale 100, no 1.", "Contá sumando lo que vale cada uno."],
"resumen": [{"titulo": "Billete", "texto": "De papel."}, {"titulo": "Moneda", "texto": "De metal."}, {"titulo": "El número", "texto": "Dice cuánto vale."}],
"glosario": [{"palabra": "Billete", "significado": "Dinero de papel."}, {"palabra": "Moneda", "significado": "Dinero de metal."}],
"carpeta": ["¿Cuántos billetes hay en la caja?", "¿Cuánto dinero hay en total?", "Tomi dice que 5 billetes de $100 son $5. ¿Cuánto son?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["5"], ["500", "$500"], ["500", "$500"]],
"soluciones": {"incompleto": "$400. $400.", "solo": "$1.000.", "carpeta": ["5 billetes.", "$500.", "$500: cada billete vale 100."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a juntar billetes para formar un monto.",
"vas_a_ver": ["Empezar por el que más vale", "Contar sumando", "Formar el mismo monto de otra forma"],
"secciones": [
 S(1, "Primero el más grande", [
  P("Rosa cuenta la plata empezando por el billete que más vale.", neutro={"texto": "Rosa cuenta el dinero empezando por el billete que más vale."}),
  P("$200, $100 y $50: <b>200, 300, 350</b>."),
  IMG("Formar $350", "200, 300, 350.", FG.dinero([200, 100, 50], "$350")),
 ]),
 S(1, "Otra forma", [
  D("Monto", "El <b>monto</b> es cuánto dinero hay en total."),
  P("$350 también se forma con $100, $100, $100 y $50."),
  IMG("Otra forma de $350", "100, 200, 300, 350.", FG.dinero([100, 100, 100, 50], "$350")),
 ]),
 S(2, "Para practicar", [
  P("Mirá la plata. La vas a usar en la carpeta.", neutro={"texto": "Mirá el dinero. Lo vas a usar en la carpeta."}),
  IMG("Plata de Tomi", "Contá empezando por el más grande.", FG.dinero([500, 200, 100, 20])),
 ]),
],
"ejemplo_completo": {"titulo": "Formar $720", "planteo": "¿Con qué billetes formo $720?", "pasos": ["Un billete de $500.", "Uno de $200: 700.", "Uno de $20: 720."]},
"ejemplo_incompleto": {"titulo": "Contar", "planteo": "$500, $100 y $10. Completá.", "pasos": ["500, ___ , ___ .", "Son $ ___ ."]},
"ejemplo_solo": {"titulo": "Tu monto", "planteo": "¿Cuánto son $200, $200 y $50?"},
"tip": {"titulo": "Del más grande al más chico", "texto": "Así contás más rápido."},
"ojo": ["$200 + $50 es $250, no $20050.", "Un mismo monto se forma de varias formas."],
"resumen": [{"titulo": "Monto", "texto": "Dinero en total."}, {"titulo": "Contar", "texto": "Del billete más grande al más chico."}, {"titulo": "Formas", "texto": "Hay más de una."}],
"glosario": [{"palabra": "Monto", "significado": "Cuánto dinero hay en total."}, {"palabra": "Formar", "significado": "Juntar billetes hasta llegar al monto."}],
"carpeta": ["¿Cuánto dinero tiene Tomi en total?", "¿Cuánto son $200, $100 y $100?", "Sofi contó $500 y $50 y dijo $50050. ¿Cuánto es?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["820", "$820"], ["400", "$400"], ["550", "$550"]],
"soluciones": {"incompleto": "600, 610. $610.", "solo": "$450.", "carpeta": ["$820.", "$400.", "$550."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a calcular el vuelto.",
"vas_a_ver": ["Lo que te devuelven", "Contar para adelante", "Pagar justo"],
"secciones": [
 S(1, "Lo que te devuelven", [
  P("Un alfajor cuesta <b>$80</b>. Tomi paga con <b>$100</b>."),
  D("Vuelto", "El <b>vuelto</b> es lo que te devuelven si pagás de más.", neutro={"texto": "El <b>cambio</b> es lo que te devuelven si pagás de más."}),
  P("Rosa le devuelve <b>$20</b>."),
  IMG("Pagar con $100", "Paga $100 por $80: le devuelven $20.", FG.dinero([100], "Le devuelven $20")),
 ]),
 S(1, "Contar para adelante", [
  P("Desde el precio contamos hasta lo que pagamos."),
  P("De 80 a 100: <b>90, 100</b>. Son 2 saltos de 10: <b>$20</b>."),
  IMG("Saltos de 10", "De 80 a 100 hay 20.", FG.recta_num(80, 100, marcas=[(80, "precio"), (100, "pago")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los precios. Los vas a usar en la carpeta."),
  IMG("Precios del kiosco", "Cada cosa con su precio.", FG.precios([("caramelo", 70), ("vaso", 150), ("estrella", 350)])),
 ]),
],
"ejemplo_completo": {"titulo": "Pagar con $500", "planteo": "Un jugo cuesta $300. Pago con $500.", "pasos": ["Desde 300 cuento hasta 500.", "400, 500: dos saltos de 100.", "Me devuelven $200."]},
"ejemplo_incompleto": {"titulo": "Pagar con $200", "planteo": "Algo cuesta $150. Completá.", "pasos": ["Desde 150 cuento: ___ , 200.", "Me devuelven $ ___ ."]},
"ejemplo_solo": {"titulo": "Tu vuelto", "planteo": "Pagás $100 por algo de $60. ¿Cuánto te devuelven?"},
"tip": {"titulo": "Contá para adelante", "texto": "Desde el precio hasta lo que pagaste."},
"ojo": ["Te devuelven lo que sobra, no lo que pagaste.", "Si pagás justo, no te devuelven nada."],
"resumen": [{"titulo": "Vuelto", "texto": "Lo que te devuelven."}, {"titulo": "Contar", "texto": "Desde el precio hasta el pago."}, {"titulo": "Justo", "texto": "Sin vuelto."}],
"glosario": [{"palabra": "Vuelto", "significado": "Dinero que te devuelven."}, {"palabra": "Precio", "significado": "Lo que cuesta algo."}],
"carpeta": ["Pagás el caramelo con $100. ¿Cuánto te devuelven?", "Pagás el vaso con $200. ¿Cuánto te devuelven?", "Pagás la estrella con $500. ¿Cuánto te devuelven?"],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"respuestas_carpeta": [["30", "$30"], ["50", "$50"], ["150", "$150"]],
"soluciones": {"incompleto": "160… 200. $50.", "solo": "$40.", "carpeta": ["$30.", "$50.", "$150."]},
}
N3["resumen"][0] = {"titulo": "Vuelto", "texto": "Lo que te devuelven.", "neutro": {"titulo": "Cambio", "texto": "Lo que te devuelven."}}
N3["glosario"][0] = {"palabra": "Vuelto", "significado": "Dinero que te devuelven.", "neutro": {"palabra": "Cambio", "significado": "Dinero que te devuelven."}}

N4 = {**ESTILO,
"objetivo": "Vas a comprar y comparar precios.",
"vas_a_ver": ["Más caro y más barato", "Sumar precios", "¿Me alcanza?"],
"secciones": [
 S(1, "Más caro, más barato", [
  P("Un globo cuesta <b>$900</b>. Una estrella cuesta <b>$300</b>."),
  D("Comparar precios", "El precio más alto es el <b>más caro</b>. El más bajo, el <b>más barato</b>."),
  IMG("Precios", "El globo es el más caro.", FG.precios([("caramelo", 150), ("estrella", 300), ("globo", 900)])),
 ]),
 S(1, "¿Me alcanza?", [
  P("Tomi tiene <b>$500</b>. Quiere un alfajor de $300 y un jugo de $250."),
  P("300 + 250 = <b>550</b>. ¡No le alcanza! Le faltan $50."),
  IMG("La plata de Tomi", "Tiene $500.", FG.dinero([200, 200, 100], "$500")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los precios. Los vas a usar en la carpeta."),
  IMG("Precios del kiosco", "Cada cosa con su precio.", FG.precios([("manzana", 200), ("vaso", 450), ("pelota", 600)])),
 ]),
],
"ejemplo_completo": {"titulo": "Dos cosas", "planteo": "Compro algo de $200 y algo de $450.", "pasos": ["Sumo las centenas: 200 + 400 = 600.", "Sumo lo que queda: 600 + 50 = 650.", "Gasto $650."]},
"ejemplo_incompleto": {"titulo": "¿Cuál es más caro?", "planteo": "Completá.", "pasos": ["$450 o $540: el más caro es ___ .", "$600 o $200: el más barato es ___ ."]},
"ejemplo_solo": {"titulo": "¿Te alcanza?", "planteo": "Tenés $500. ¿Te alcanza para algo de $200 y algo de $250?"},
"tip": {"titulo": "Sumá antes de pagar", "texto": "Si la suma es mayor que tu plata, no alcanza.", "neutro": {"titulo": "Sumá antes de pagar", "texto": "Si la suma es mayor que tu dinero, no alcanza."}},
"ojo": ["Para comparar, mirá primero las centenas.", "Sumá todos los precios antes de pagar."],
"resumen": [{"titulo": "Más caro", "texto": "Precio más alto."}, {"titulo": "Más barato", "texto": "Precio más bajo."}, {"titulo": "¿Alcanza?", "texto": "Sumá y compará."}],
"glosario": [{"palabra": "Caro", "significado": "Que cuesta mucho."}, {"palabra": "Barato", "significado": "Que cuesta poco."}],
"carpeta": ["¿Cuál es la cosa más cara del dibujo?", "¿Cuánto cuestan juntas la manzana y el vaso?", "Tenés $700. ¿Cuánto te sobra si comprás la pelota?"],
"carpeta_nivel": ["recordar", "aplicar", "aplicar"],
"respuestas_carpeta": [["pelota", "la pelota", "600", "$600"], ["650", "$650"], ["100", "$100"]],
"soluciones": {"incompleto": "$540. $200.", "solo": "Sí: 200 + 250 = 450.", "carpeta": ["La pelota: $600.", "$650.", "$100."]},
}

# ---------- LECCIÓN INTERACTIVA (escrita en sesión, docs/reglas-leccion-interactiva.md, primer ciclo: poco texto, todo visual) ----------
LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LP = lambda x: {"tipo": "parrafo", "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}
ORD = lambda p, o, orden, e, **k: {"t": "ordering", "p": p, "o": o, "r": {"orden": orden}, "e": e, **k}
UNIR = lambda p, iz, de, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": iz, "derecha": de}, "r": {"pares": pares}, "e": e, **k}
CLAS = lambda p, el, cats, r, e, **k: {"t": "classify", "p": p, "o": {"elementos": el, "categorias": cats}, "r": {"categorias": r}, "e": e, **k}
FB = lambda p, huecos, e, **k: {"t": "fill_blank", "p": p, "o": {}, "r": {"huecos": huecos}, "e": e, **k}
A, AN, RE, ER = {"n": "aplicar"}, {"n": "analizar"}, {"n": "recordar"}, {"n": "error"}
N1["leccion"] = {"temas": [
 T("BILLETES Y MONEDAS", [LD("EL DINERO", "HAY BILLETES DE <b>$50, $100, $200 Y $500</b>. EL NÚMERO DICE CUÁNTO VALE."),
   LL("UN BILLETE DE $500 VALE 500.", "NO IMPORTA EL TAMAÑO.")],
   {"modo": "dinero2"}, {"modo": "dinero2"}),
 T("BILLETES IGUALES", [LD("CONTAR IGUALES", "PARA CONTAR BILLETES <b>IGUALES</b>, SALTAMOS DE A LO QUE VALE CADA UNO."),
   LL("3 DE $100: 100, 200, 300.", "5 DE $100 SON $500, NO $5.")],
   {"modo": "serie", "de": 100, "desde": 100, "hasta": 100}, {"modo": "dinero2"}),
], "recuerda": [
 RC("EL VALOR", "EL NÚMERO DEL BILLETE DICE CUÁNTO VALE.", "UN BILLETE DE $200 VALE 200"),
 RC("IGUALES", "SALTAMOS DE A LO QUE VALE CADA BILLETE.", "2 DE $500 SON $1.000"),
]}

N2["leccion"] = {"temas": [
 T("EMPEZAR POR EL QUE MÁS VALE", [LD("EL ORDEN", "PARA CONTAR DINERO, EMPEZÁ POR EL BILLETE QUE <b>MÁS VALE</b>."),
   LL("$200, $100 Y $50: 200, 300, 350.", "ASÍ NO TE PERDÉS.")],
   {"modo": "dinero2"}, {"modo": "dinero2"}),
 T("EL MISMO MONTO", [LD("OTRA FORMA", "EL MISMO MONTO SE PUEDE FORMAR CON <b>DISTINTOS</b> BILLETES."),
   LL("$600 = $500 + $100.", "$600 = $200 + $200 + $200.")],
   {"modo": "dinero2"}, {"modo": "dinero2"}),
], "recuerda": [
 RC("EL ORDEN", "EMPEZAMOS POR EL BILLETE QUE MÁS VALE Y SEGUIMOS SUMANDO.", "500, 700, 750"),
 RC("OTRA FORMA", "UN MONTO SE PUEDE ARMAR CON BILLETES DISTINTOS.", "$300 = $200 + $100"),
]}

N3["leccion"] = {"temas": [
 T("LO QUE TE DEVUELVEN", [LD("DEVOLVER", "SI PAGÁS CON <b>MÁS</b> DE LO QUE CUESTA, TE DEVUELVEN LA DIFERENCIA."),
   LL("CUESTA $80 Y PAGÁS $100: TE DEVUELVEN $20.", "SI PAGÁS JUSTO, NO TE DEVUELVEN NADA.")],
   {"modo": "dinero2", "que": "vuelto"}, {"modo": "dinero2", "que": "vuelto"}),
 T("CONTAR PARA ADELANTE", [LD("ADELANTE", "PARA SABER CUÁNTO TE DEVUELVEN, CONTÁ <b>DESDE EL PRECIO</b> HASTA LO QUE PAGASTE."),
   LL("DE 300 A 500: 400, 500.", "SON DOS SALTOS DE 100: $200.")],
   {"modo": "dinero2", "que": "vuelto"}, {"modo": "dinero2", "que": "vuelto"}),
], "recuerda": [
 RC("DEVOLVER", "ES LA DIFERENCIA ENTRE LO QUE PAGAMOS Y EL PRECIO.", "PAGO $100 POR $70: ME DAN $30"),
 RC("CONTAR PARA ADELANTE", "CONTAMOS DESDE EL PRECIO HASTA LO QUE PAGAMOS.", "DE 150 A 200 HAY 50"),
]}

N4["leccion"] = {"temas": [
 T("MÁS CARO Y MÁS BARATO", [LD("COMPARAR", "COMPARAMOS PRECIOS COMO NÚMEROS: PRIMERO LAS <b>CENTENAS</b>."),
   LL("$540 ES MÁS CARO QUE $450.", "$702 ES MÁS BARATO QUE $720.")],
   {"modo": "dinero2", "que": "caro"}, {"modo": "dinero2", "que": "caro"}),
 T("SUMAR PRECIOS", [LD("JUNTOS", "PARA SABER CUÁNTO CUESTAN <b>JUNTAS</b> DOS COSAS, SUMAMOS LOS PRECIOS."),
   LL("$300 + $250 = $550.", "SI TENÉS $500, NO TE ALCANZA.")],
   {"modo": "dinero2", "que": "sumar"}, {"modo": "dinero2", "que": "sumar"}),
], "recuerda": [
 RC("MÁS CARO", "ES EL PRECIO MÁS GRANDE; MIRAMOS PRIMERO LAS CENTENAS.", "$720 ES MÁS CARO QUE $270"),
 RC("SUMAR PRECIOS", "SUMAMOS PARA SABER CUÁNTO CUESTA TODO.", "$400 + $350 = $750"),
]}

ACT = {
"1": [N("💵 3 BILLETES DE $100. ¿CUÁNTO DINERO ES?", 300, "100, 200, 300.", n="aplicar"),
      MC("¿CUÁNTO VALE UN BILLETE DE $500?", ["500", "5", "50"], "500", "EL NÚMERO DICE CUÁNTO VALE.", n="recordar"),
      MC("LEO DICE QUE 4 BILLETES DE $100 SON $4. ¿CUÁNTO SON DE VERDAD?", ["$400", "$4", "$104"], "$400", "100, 200, 300, 400.", n="error"),
      UNIR("UNÍ CADA GRUPO DE BILLETES CON SU TOTAL.", ["2 DE $100", "2 DE $200", "2 DE $500"], ["$1.000", "$200", "$400"], {"2 DE $100": "$200", "2 DE $200": "$400", "2 DE $500": "$1.000"}, "100 + 100, 200 + 200 Y 500 + 500.", n="aplicar")],
"2": [N("$200, $100 Y $50. ¿CUÁNTO ES?", 350, "200, 300, 350.", n="aplicar"),
      MC("¿CON QUÉ BILLETES FORMÁS $600?", ["$500 Y $100", "$200 Y $200", "$500 Y $50"], "$500 Y $100", "500 + 100 = 600.", n="analizar", **NEU("¿CON QUÉ BILLETES FORMAS $600?")),
      ORD("ORDENÁ LOS BILLETES PARA CONTAR: PRIMERO EL QUE MÁS VALE.", ["$50", "$500", "$100", "$200"], ["$500", "$200", "$100", "$50"], "DEL QUE MÁS VALE AL QUE MENOS.", n="aplicar"),
      MC("SOFI CONTÓ $500 Y $50 Y DIJO $50050. ¿CUÁNTO ES?", ["$550", "$50050", "$505"], "$550", "500 + 50 = 550.", n="error")],
"3": [N("ALGO CUESTA $80. PAGÁS CON $100. ¿CUÁNTO TE DEVUELVEN?", 20, "DE 80 A 100 HAY 20.", n="aplicar", **NEU("ALGO CUESTA $80. PAGAS CON $100. ¿CUÁNTO TE DEVUELVEN?")),
      MC("PAGÁS JUSTO. ¿CUÁNTO TE DEVUELVEN?", ["NADA", "TODO", "LA MITAD"], "NADA", "SI PAGÁS JUSTO, NO SOBRA.", n="analizar", **NEU("PAGAS JUSTO. ¿CUÁNTO TE DEVUELVEN?")),
      FB("COMPLETÁ: CUESTA $350 Y PAGÁS $500. TE DEVUELVEN $___", [["150"]], "DE 350 A 500 HAY 150.", n="aplicar", **NEU("COMPLETA: CUESTA $350 Y PAGAS $500. TE DEVUELVEN $___")),
      MC("JUAN PAGÓ $200 POR ALGO DE $120 Y LE DIERON $180. ¿CUÁNTO LE TENÍAN QUE DAR?", ["$80", "$180", "$120"], "$80", "DE 120 A 200 HAY 80.", n="error")],
"4": [MC("¿CUÁL ES MÁS CARO?", ["$540", "$450"], "$540", "5 CENTENAS ES MÁS QUE 4.", n="analizar"),
      N("UN ALFAJOR DE $300 Y UN JUGO DE $250. ¿CUÁNTO CUESTAN JUNTOS?", 550, "300 + 250 = 550.", n="aplicar", **NEU("UNA GALLETA DE $300 Y UN JUGO DE $250. ¿CUÁNTO CUESTAN JUNTOS?")),
      ORD("ORDENÁ DEL MÁS BARATO AL MÁS CARO.", ["$720", "$270", "$702"], ["$270", "$702", "$720"], "270, 702 Y 720.", n="aplicar"),
      N("[[problema]] TENÉS $700 Y COMPRÁS UNA PELOTA DE $450. ¿CUÁNTO DINERO TE SOBRA?", 250, "DE 450 A 700 HAY 250.", n="analizar", **NEU("TIENES $700 Y COMPRAS UNA PELOTA DE $450. ¿CUÁNTO DINERO TE SOBRA?"))],
"5": [N("RELÁMPAGO. 2 BILLETES DE $200. ¿CUÁNTO ES?", 400, "200, 400.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ES MÁS BARATO?", ["$200", "$600"], "$200", "200 ES MENOS QUE 600.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. PAGÁS $100 POR $90. ¿VUELTO?", 10, "DE 90 A 100 HAY 10.", tiempo=30, n="aplicar", **NEU("RELÁMPAGO. PAGAS $100 POR $90. ¿CAMBIO?")),
      N("RELÁMPAGO. $500 + $200 + $20 = ___", 720, "500, 700, 720.", tiempo=40, n="aplicar")],
}
EXAMEN = [
 [1, N("5 BILLETES DE $100. ¿CUÁNTO DINERO ES?", 500, "100, 200, 300, 400, 500.", n="aplicar")],
 [1, MC("¿CUÁNTO VALE UN BILLETE DE $200?", ["200", "2", "20"], "200", "EL NÚMERO DICE CUÁNTO VALE.", n="recordar")],
 [1, MC("TOMI DICE: 2 BILLETES DE $500 SON $10. ¿CUÁNTO SON?", ["$1.000", "$10", "$500"], "$1.000", "TOMI SE EQUIVOCÓ: 500 + 500 = 1.000.", n="error")],
 [2, N("$500, $200 Y $50. ¿CUÁNTO ES?", 750, "500, 700, 750.", n="aplicar")],
 [2, MC("¿QUÉ BILLETES FORMAN $300?", ["$200 Y $100", "$200 Y $200", "$100 Y $20"], "$200 Y $100", "200 + 100 = 300.", n="analizar")],
 [2, N("$100, $100, $100 Y $20. ¿CUÁNTO ES?", 320, "100, 200, 300, 320.", n="aplicar")],
 [3, N("ALGO CUESTA $70. PAGÁS CON $100. ¿CUÁNTO TE DEVUELVEN?", 30, "DE 70 A 100 HAY 30.", n="aplicar", **NEU("ALGO CUESTA $70. PAGAS CON $100. ¿CUÁNTO TE DEVUELVEN?"))],
 [3, N("UN JUGO CUESTA $300. PAGÁS CON $500. ¿CUÁNTO TE DEVUELVEN?", 200, "400, 500: DOS SALTOS DE 100.", n="aplicar", **NEU("UN JUGO CUESTA $300. PAGAS CON $500. ¿CUÁNTO TE DEVUELVEN?"))],
 [3, MC("PAGÁS $200 POR ALGO DE $150. ROSA TE DA $50. ¿ESTÁ BIEN?", ["SÍ", "NO"], "SÍ", "DE 150 A 200 HAY 50.", n="analizar", **NEU("PAGAS $200 POR ALGO DE $150. ROSA TE DA $50. ¿ESTÁ BIEN?"))],
 [4, MC("¿CUÁL ES MÁS CARO?", ["$720", "$270", "$702"], "$720", "TIENE MÁS CENTENAS Y MÁS DECENAS.", n="analizar")],
 [4, N("ALGO DE $400 Y ALGO DE $350. ¿CUÁNTO CUESTAN JUNTOS?", 750, "400 + 350 = 750.", n="aplicar")],
 [4, MC("TENÉS $500. ¿TE ALCANZA PARA ALGO DE $300 Y ALGO DE $250?", ["SÍ", "NO"], "NO", "300 + 250 = 550: FALTAN $50.", n="analizar", **NEU("TIENES $500. ¿TE ALCANZA PARA ALGO DE $300 Y ALGO DE $250?"))],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 6, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: dinero hasta 1.000", "examen_titulo": "Nivel jefe: dinero hasta 1.000",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
