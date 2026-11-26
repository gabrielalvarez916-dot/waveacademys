# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 7 · Dinero y números. Genera mision-7.json.
VARIANTE: lo que nombra los pesos lleva su parte "neutro" para alumnos de otros países. Regla de primeros años."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
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
"objetivo": "Vas a conocer las monedas y los billetes.",
"vas_a_ver": ["Monedas y billetes", "El número dice cuánto vale", "Juntar dinero"],
"secciones": [
 S(1, "Monedas y billetes", [
  P("En Argentina pagamos con <b>pesos</b>.", neutro={"texto": "Para comprar usamos <b>dinero</b>."}),
  D("Moneda y billete", "La <b>moneda</b> es de metal. El <b>billete</b> es de papel."),
  IMG("Monedas y billetes", "El número dice cuánto vale.", FG.dinero([1, 2, 5, 10, 20, 50])),
 ]),
 S(1, "Juntar dinero", [
  P("Tres monedas de 10: <b>10, 20, 30</b>."),
  IMG("Tres monedas de 10", "Son 30.", FG.dinero([10, 10, 10], "$30")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el dinero. Lo vas a usar en la carpeta."),
  IMG("Dinero de Sofi", "Contá monedas y billetes.", FG.dinero([20, 10, 5])),
 ]),
],
"ejemplo_completo": {"titulo": "Dos monedas de 5", "planteo": "¿Cuánto son?", "pasos": ["Una de 5: 5.", "Otra de 5: 10.", "Son $10."]},
"ejemplo_incompleto": {"titulo": "Un billete y una moneda", "planteo": "$20 y $10. Completá.", "pasos": ["Billete: ___ .", "Con la moneda: ___ ."]},
"ejemplo_solo": {"titulo": "Tu alcancía", "planteo": "Si tenés 2 monedas de 10, ¿cuánto tenés?"},
"tip": {"titulo": "Mirá el número", "texto": "El número dice cuánto vale."},
"ojo": ["Una moneda de 10 vale 10, no 1.", "Billete y moneda sirven para pagar."],
"resumen": [{"titulo": "Moneda", "texto": "De metal."}, {"titulo": "Billete", "texto": "De papel."}, {"titulo": "Número", "texto": "Dice cuánto vale."}],
"glosario": [{"palabra": "Moneda", "significado": "Dinero de metal."}, {"palabra": "Billete", "significado": "Dinero de papel."}],
"carpeta": ["¿Cuántos billetes hay?", "¿Cuántas monedas hay?", "¿Cuánto dinero vale el billete del dibujo?"],
"respuestas_carpeta": [["1"], ["2"], ["20"]],
"soluciones": {"incompleto": "20. 30.", "solo": "$20.", "carpeta": ["1.", "2.", "20."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar dinero sumando.",
"vas_a_ver": ["Contar sumando", "Empezar por lo que más vale", "El total"],
"secciones": [
 S(1, "La caja de Sofi", [
  P("Sofi cuenta: <b>10, 20, 25, 26, 27</b>."),
  IMG("La caja", "Hay $27.", FG.dinero([10, 10, 5, 1, 1], "$27")),
 ]),
 S(1, "Primero lo grande", [
  D("Contar dinero", "Sumamos lo que <b>vale</b> cada una. Empezamos por la que <b>más vale</b>."),
  IMG("Otra cuenta", "20, 30, 35.", FG.dinero([20, 10, 5], "$35")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el dinero. Lo vas a usar en la carpeta."),
  IMG("Para contar", "Empezá por el billete.", FG.dinero([20, 10, 2])),
 ]),
],
"ejemplo_completo": {"titulo": "Contar $10, $5 y $1", "planteo": "¿Cuánto hay?", "pasos": ["10.", "10 y 5: 15.", "15 y 1: 16."]},
"ejemplo_incompleto": {"titulo": "Contar $20 y $5", "planteo": "Completá.", "pasos": ["20.", "20 y 5: ___ ."]},
"ejemplo_solo": {"titulo": "Tus monedas", "planteo": "¿Cuánto son 3 monedas de 10?"},
"tip": {"titulo": "Primero lo grande", "texto": "Empezá por el que más vale."},
"ojo": ["No cuentes monedas: sumá lo que valen.", "3 monedas de 10 son 30, no 3."],
"resumen": [{"titulo": "Contar", "texto": "Sumando lo que vale."}, {"titulo": "Empezar", "texto": "Por lo que más vale."}, {"titulo": "Total", "texto": "Todo junto."}],
"glosario": [{"palabra": "Total", "significado": "Todo junto."}, {"palabra": "Valer", "significado": "Lo que se puede comprar con eso."}],
"carpeta": ["¿Cuánto vale el billete?", "¿Cuánto valen las dos monedas juntas?", "¿Cuánto hay en total?"],
"respuestas_carpeta": [["20"], ["12"], ["32"]],
"soluciones": {"incompleto": "25.", "solo": "$30.", "carpeta": ["20.", "12.", "32."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a pagar justo, ni más ni menos.",
"vas_a_ver": ["Pagar justo", "Contar hasta el precio", "Cuando no alcanza"],
"secciones": [
 S(1, "Pagar justo", [
  P("El alfajor cuesta <b>$15</b>. Tomi da <b>$10 y $5</b>.", neutro={"texto": "La galleta cuesta <b>$15</b>. Tomi da <b>$10 y $5</b>."}),
  IMG("Paga justo", "10, 15. ¡Justo!", FG.dinero([10, 5], "$15")),
 ]),
 S(1, "Cuando no alcanza", [
  D("Pagar justo", "Dar <b>lo mismo</b> que el precio. Si falta, <b>no alcanza</b>."),
  IMG("Precios del kiosco", "Cada cosa con su precio.", FG.precios([("caramelo", 5), ("manzana", 10), ("pelota", 20)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los precios. Los vas a usar en la carpeta."),
  IMG("Para pagar", "¿Con qué pagás justo?", FG.precios([("vaso", 12), ("estrella", 25)])),
 ]),
],
"ejemplo_completo": {"titulo": "Pagar $20", "planteo": "Una pelota cuesta $20.", "pasos": ["Doy $10: 10.", "Doy otra de $10: 20.", "¡Justo!"]},
"ejemplo_incompleto": {"titulo": "Pagar $7", "planteo": "Completá.", "pasos": ["Doy $5: 5.", "Me faltan ___ ."]},
"ejemplo_solo": {"titulo": "Un caramelo", "planteo": "Un caramelo cuesta $5. ¿Alcanza con $2?"},
"tip": {"titulo": "Contá hasta el precio", "texto": "Pagar justo es llegar al precio."},
"ojo": ["Con $10 no alcanza para $15.", "Pagar justo: ni más ni menos."],
"resumen": [{"titulo": "Justo", "texto": "Ni más ni menos."}, {"titulo": "Contar", "texto": "Hasta el precio."}, {"titulo": "Si falta", "texto": "No alcanza."}],
"glosario": [{"palabra": "Precio", "significado": "Lo que cuesta algo."}, {"palabra": "Alcanzar", "significado": "Tener lo que hace falta."}],
"carpeta": ["¿Cuánto cuesta el vaso?", "¿Cuánto cuesta la estrella?", "Para el vaso das $10. ¿Cuánto falta?"],
"respuestas_carpeta": [["12"], ["25"], ["2"]],
"soluciones": {"incompleto": "2.", "solo": "No. Faltan 3.", "carpeta": ["12.", "25.", "2."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a comparar precios.",
"vas_a_ver": ["Más caro", "Más barato", "El precio"],
"secciones": [
 S(1, "Más caro y más barato", [
  P("El jugo cuesta <b>$20</b>. El chupetín, <b>$5</b>.", neutro={"texto": "El jugo cuesta <b>$20</b>. La paleta, <b>$5</b>."}),
  D("Comparar precios", "El número <b>más grande</b> es el <b>más caro</b>."),
  IMG("Precios", "¿Cuál es más caro?", FG.precios([("caramelo", 5), ("vaso", 20)])),
 ]),
 S(1, "Ordenar precios", [
  P("Del más barato al más caro: <b>$5, $10, $20</b>."),
  IMG("En orden", "Del más barato al más caro.", FG.precios([("caramelo", 5), ("manzana", 10), ("pelota", 20)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los precios. Los vas a usar en la carpeta."),
  IMG("Para comparar", "Compará los precios.", FG.precios([("globo", 15), ("estrella", 8), ("pelota", 30)])),
 ]),
],
"ejemplo_completo": {"titulo": "$10 y $30", "planteo": "¿Cuál es más caro?", "pasos": ["30 es más que 10.", "El de $30 es más caro."]},
"ejemplo_incompleto": {"titulo": "$8 y $18", "planteo": "Completá.", "pasos": ["___ es más que 8.", "El más barato es el de $ ___ ."]},
"ejemplo_solo": {"titulo": "Elegí", "planteo": "¿Qué es más barato: algo de $20 o algo de $12?"},
"tip": {"titulo": "Mirá el número", "texto": "El más grande es el más caro."},
"ojo": ["Más caro no es más grande de tamaño.", "Comparamos los números del precio."],
"resumen": [{"titulo": "Más caro", "texto": "Número más grande."}, {"titulo": "Más barato", "texto": "Número más chico."}, {"titulo": "Precio", "texto": "Lo que cuesta."}],
"glosario": [{"palabra": "Caro", "significado": "Que cuesta mucho."}, {"palabra": "Barato", "significado": "Que cuesta poco."}],
"carpeta": ["¿Cuánto cuesta lo más caro?", "¿Cuánto cuesta lo más barato?", "¿Cuánto cuesta el globo que está dibujado?"],
"respuestas_carpeta": [["30"], ["8"], ["15"]],
"soluciones": {"incompleto": "18. 8.", "solo": "El de $12.", "carpeta": ["30.", "8.", "15."]},
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
for _N in (N1, N2, N3, N4): _N["carpeta_nivel"] = ["aplicar", "aplicar", "aplicar"]

N1["leccion"] = {"temas": [
 T("MONEDAS Y BILLETES", [LD("EL DINERO", "EL DINERO TIENE <b>MONEDAS</b> DE METAL Y <b>BILLETES</b> DE PAPEL."),
   LL("EL NÚMERO DICE CUÁNTO VALE.", "UNA MONEDA DE $5 VALE 5.")],
   {"modo": "dinero", "que": "contar"}, {"modo": "dinero", "que": "contar"}),
 T("JUNTAR DINERO", [LD("JUNTAR", "PARA SABER CUÁNTO HAY, SUMAMOS LO QUE <b>VALE</b> CADA UNO."),
   LL("3 MONEDAS DE $10 SON $30, NO $3.", "CONTAMOS 10, 20, 30.")],
   {"modo": "dinero", "que": "contar"}, {"modo": "dinero", "que": "contar"}),
], "recuerda": [
 RC("MONEDAS Y BILLETES", "LAS MONEDAS SON DE METAL Y LOS BILLETES DE PAPEL.", "UN BILLETE DE $20 VALE 20"),
 RC("JUNTAR", "SUMAMOS LO QUE VALE CADA MONEDA O BILLETE.", "$10 + $10 = $20"),
]}

N2["leccion"] = {"temas": [
 T("EMPEZAR POR LO QUE MÁS VALE", [LD("EL ORDEN", "PARA CONTAR DINERO, EMPEZÁ POR LO QUE <b>MÁS VALE</b> Y SEGUÍ SUMANDO."),
   LL("$10 + $10 + $5: 10, 20, 25.", "DESPUÉS SUMÁS LAS MONEDAS DE $1.")],
   {"modo": "dinero", "que": "contar"}, {"modo": "dinero", "que": "contar"}),
 T("EL TOTAL", [LD("CUÁNTO HAY", "EL <b>TOTAL</b> ES TODO EL DINERO JUNTO, DESPUÉS DE SUMAR."),
   LL("$20 + $10 + $2 = $32.", "SI TE PERDÉS, VOLVÉ A EMPEZAR.")],
   {"modo": "dinero", "que": "contar"}, {"modo": "dinero", "que": "contar"}),
], "recuerda": [
 RC("PRIMERO LO QUE MÁS VALE", "ASÍ CONTAMOS MÁS RÁPIDO Y SIN PERDERNOS.", "10, 20, 25, 26"),
 RC("EL TOTAL", "ES TODO EL DINERO JUNTO DESPUÉS DE SUMAR.", "$20 + $5 = $25"),
]}

N3["leccion"] = {"temas": [
 T("PAGAR JUSTO", [LD("JUSTO", "PAGAR <b>JUSTO</b> ES DAR EL MISMO DINERO QUE EL PRECIO: NI MÁS NI MENOS."),
   LL("SI CUESTA $15: $10 + $5.", "CONTÁ HASTA LLEGAR AL PRECIO.")],
   {"modo": "dinero", "que": "pagar"}, {"modo": "dinero", "que": "pagar"}),
 T("CUANDO NO ALCANZA", [LD("FALTA", "SI DAS MENOS QUE EL PRECIO, <b>NO ALCANZA</b>: FALTA DINERO."),
   LL("CUESTA $7 Y DAS $5: FALTAN $2.", "CONTÁ DESDE LO QUE DAS HASTA EL PRECIO.")],
   {"modo": "dinero", "que": "falta"}, {"modo": "dinero", "que": "falta"}),
], "recuerda": [
 RC("PAGAR JUSTO", "ES DAR EL MISMO DINERO QUE DICE EL PRECIO.", "CUESTA $12: $10 + $1 + $1"),
 RC("CUÁNTO FALTA", "CONTAMOS DESDE LO QUE DAMOS HASTA EL PRECIO.", "DE $10 A $12 FALTAN $2"),
]}

N4["leccion"] = {"temas": [
 T("MÁS CARO Y MÁS BARATO", [LD("COMPARAR PRECIOS", "LO MÁS <b>CARO</b> TIENE EL PRECIO MÁS GRANDE Y LO MÁS <b>BARATO</b>, EL MÁS CHICO."),
   LL("$20 ES MÁS CARO QUE $5.", "COMPARÁ COMO COMPARÁS NÚMEROS.")],
   {"modo": "dinero", "que": "caro"}, {"modo": "dinero", "que": "caro"}),
 T("EL PRECIO", [LD("EL PRECIO", "EL <b>PRECIO</b> ES EL NÚMERO QUE DICE CUÁNTO CUESTA ALGO."),
   LL("UN GLOBO DE $15 CUESTA 15.", "PARA COMPRARLO HAY QUE JUNTAR ESE DINERO.")],
   {"modo": "dinero", "que": "pagar"}, {"modo": "dinero", "que": "caro"}),
], "recuerda": [
 RC("MÁS CARO", "ES LO QUE TIENE EL PRECIO MÁS GRANDE.", "$30 ES MÁS CARO QUE $8"),
 RC("MÁS BARATO", "ES LO QUE TIENE EL PRECIO MÁS CHICO.", "$8 ES MÁS BARATO QUE $30"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [MC("¿CUÁNTO VALE UNA MONEDA DE $5?", ["1", "5", "10"], "5", "LO DICE SU NÚMERO.", **RE),
      N("🪙 $10 + 🪙 $10 + 🪙 $10. ¿CUÁNTOS PESOS SON?", 30, "10, 20, 30.", **A, **NEU("🪙 $10 + 🪙 $10 + 🪙 $10. ¿CUÁNTO ES?")),
      MC("LEO TIENE 3 MONEDAS DE $10 Y DICE QUE TIENE $3. ¿CUÁNTO TIENE DE VERDAD?", ["$30", "$3", "$13"], "$30", "CADA MONEDA VALE 10: 10, 20, 30.", **ER),
      CLAS("¿ES MONEDA O BILLETE?", ["DE METAL", "DE PAPEL", "REDONDA Y CHICA", "RECTANGULAR"], ["MONEDA", "BILLETE"],
           {"DE METAL": "MONEDA", "DE PAPEL": "BILLETE", "REDONDA Y CHICA": "MONEDA", "RECTANGULAR": "BILLETE"}, "LAS MONEDAS SON DE METAL; LOS BILLETES, DE PAPEL.", **A)],
"2": [N("$10 + $10 + $5 + $1 + $1. ¿CUÁNTO ES?", 27, "10, 20, 25, 26, 27.", **A),
      N("$20 + $10 + $5. ¿CUÁNTO ES?", 35, "20, 30, 35.", **A),
      ORD("ORDENÁ PARA CONTAR: PRIMERO LO QUE MÁS VALE.", ["$1", "$10", "$5", "$20"], ["$20", "$10", "$5", "$1"], "DE LO QUE MÁS VALE A LO QUE MENOS.", **A),
      N("[[problema]] SOFI TIENE UN BILLETE DE $20 Y DOS MONEDAS DE $1. ¿CUÁNTO DINERO TIENE?", 22, "20, 21, 22.", **AN)],
"3": [MC("EL ALFAJOR CUESTA $15. ¿QUÉ DAS PARA PAGAR JUSTO?", ["$10 + $5", "$10", "$5 + $5"], "$10 + $5", "10, 15. ¡JUSTO!", **A, **NEU("LA GALLETA CUESTA $15. ¿QUÉ DAS PARA PAGAR JUSTO?")),
      N("ALGO CUESTA $7. DAS $5. ¿CUÁNTO FALTA?", 2, "5, 6, 7: FALTAN 2.", **A),
      MC("JUAN QUIERE UN JUGO DE $12 Y DA $10. DICE QUE LE ALCANZA. ¿TIENE RAZÓN?", ["NO, FALTAN $2", "SÍ, ALCANZA", "NO, FALTAN $10"], "NO, FALTAN $2", "10 ES MENOS QUE 12: FALTAN 2.", **ER),
      FB("COMPLETÁ PARA PAGAR $16 JUSTO: $10 + $5 + $___", [["1"]], "10, 15, 16.", **A)],
"4": [MC("¿CUÁL DE LOS DOS CUESTA MÁS?", ["🧃 $20", "🍭 $5"], "🧃 $20", "20 ES MÁS QUE 5.", **A),
      MC("¿CUÁL DE LOS DOS CUESTA MENOS?", ["🍎 $10", "⚽ $30"], "🍎 $10", "10 ES MENOS QUE 30.", **A),
      ORD("ORDENÁ DEL MÁS BARATO AL MÁS CARO.", ["🎈 $15", "⚽ $30", "🍎 $8"], ["🍎 $8", "🎈 $15", "⚽ $30"], "8, 15 Y 30: DEL PRECIO MÁS CHICO AL MÁS GRANDE.", **AN),
      MC("MICA DICE QUE UN LÁPIZ DE $9 ES MÁS CARO QUE UNA GOMA DE $12 PORQUE 9 ES UN NÚMERO GRANDE. ¿CUÁL ES MÁS CARO?", ["LA GOMA", "EL LÁPIZ"], "LA GOMA", "12 ES MÁS QUE 9.", **ER)],
"5": [N("RELÁMPAGO. $10 + $10. ¿CUÁNTO ES?", 20, "10, 20.", tiempo=30, **A),
      N("RELÁMPAGO. $20 + $5. ¿CUÁNTO ES?", 25, "20, 25.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿CUÁL ES MÁS CARO?", ["$8", "$18"], "$18", "18 ES MÁS QUE 8.", tiempo=30, **A),
      N("RELÁMPAGO. ALGO CUESTA $12. DAS $10. ¿CUÁNTO FALTA?", 2, "10, 11, 12.", tiempo=30, **A)],
}
EXAMEN = [
 [1, MC("LA MONEDA ES DE…", ["PAPEL", "METAL"], "METAL", "EL BILLETE ES DE PAPEL.", **RE)],
 [1, MC("¿CUÁNTO VALE UN BILLETE DE $20?", ["2", "20", "200"], "20", "LO DICE SU NÚMERO.", **RE)],
 [1, N("TRES MONEDAS DE $10. ¿CUÁNTOS PESOS SON?", 30, "10, 20, 30.", **A, **NEU("TRES MONEDAS DE $10. ¿CUÁNTO ES?"))],
 [2, N("$10 + $5 + $1. ¿CUÁNTO ES?", 16, "10, 15, 16.", **A)],
 [2, N("$20 + $10 + $2. ¿CUÁNTO ES?", 32, "20, 30, 32.", **A)],
 [2, MC("TOMI TIENE 3 MONEDAS DE $10 Y DICE QUE SON $3. ¿CUÁNTO ES DE VERDAD?", ["$30", "$3"], "$30", "SUMAMOS LO QUE VALEN.", **ER)],
 [3, MC("ALGO CUESTA $12. ¿QUÉ DAS PARA PAGAR JUSTO?", ["$10 + $1 + $1", "$10 + $5", "$5 + $5"], "$10 + $1 + $1", "10, 11, 12. ¡JUSTO!", **A)],
 [3, FB("COMPLETÁ PARA PAGAR $25 JUSTO: $20 + $___", [["5"]], "20, 25.", **A)],
 [3, N("ALGO CUESTA $20. DAS $10. ¿CUÁNTO FALTA?", 10, "10, 20: FALTAN 10.", **A)],
 [4, MC("¿CUÁL DE LOS DOS CUESTA MÁS?", ["$8", "$18"], "$18", "18 ES MÁS QUE 8.", **A)],
 [4, MC("¿CUÁL DE LOS DOS CUESTA MENOS?", ["$20", "$12"], "$12", "12 ES MENOS QUE 20.", **A)],
 [4, ORD("ORDENÁ DEL MÁS BARATO AL MÁS CARO.", ["$25", "$9", "$14"], ["$9", "$14", "$25"], "9, 14 Y 25.", **A)],
 [4, MC("[[problema]] UN JUGO CUESTA $20 Y UN CHUPETÍN $5. ¿CUÁL ES MÁS CARO?", ["EL JUGO", "EL DE $5"], "EL JUGO", "20 ES MÁS QUE 5.", **AN, **NEU("UN JUGO CUESTA $20 Y UNA PALETA $5. ¿CUÁL ES MÁS CARO?"))],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 7, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: dinero y números", "examen_titulo": "Nivel jefe: dinero y números",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
