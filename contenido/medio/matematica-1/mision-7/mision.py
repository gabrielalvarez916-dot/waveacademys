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
"carpeta": ["¿Cuántos billetes hay?", "¿Cuántas monedas hay?", "¿Cuánto vale el billete?"],
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
"carpeta": ["¿Cuánto cuesta lo más caro?", "¿Cuánto cuesta lo más barato?", "¿Cuánto cuesta el globo?"],
"respuestas_carpeta": [["30"], ["8"], ["15"]],
"soluciones": {"incompleto": "18. 8.", "solo": "El de $12.", "carpeta": ["30.", "8.", "15."]},
}

ACT = {
"1": [MC("¿CUÁNTO VALE UNA MONEDA DE $5?", ["1", "5", "10"], "5", "LO DICE SU NÚMERO."),
      N("🪙 $10 + 🪙 $10 + 🪙 $10. ¿CUÁNTOS PESOS SON?", 30, "10, 20, 30.", **NEU("🪙 $10 + 🪙 $10 + 🪙 $10. ¿CUÁNTO ES?"))],
"2": [N("$10 + $10 + $5 + $1 + $1. ¿CUÁNTO ES?", 27, "10, 20, 25, 26, 27."),
      N("$20 + $10 + $5. ¿CUÁNTO ES?", 35, "20, 30, 35.")],
"3": [MC("EL ALFAJOR CUESTA $15. ¿QUÉ DAS PARA PAGAR JUSTO?", ["$10 + $5", "$10", "$5 + $5"], "$10 + $5", "10, 15. ¡JUSTO!", **NEU("LA GALLETA CUESTA $15. ¿QUÉ DAS PARA PAGAR JUSTO?")),
      N("ALGO CUESTA $7. DAS $5. ¿CUÁNTO FALTA?", 2, "5, 6, 7: FALTAN 2.")],
"4": [MC("¿QUÉ ES MÁS CARO?", ["🧃 $20", "🍭 $5"], "🧃 $20", "20 ES MÁS QUE 5."),
      MC("¿QUÉ ES MÁS BARATO?", ["🍎 $10", "⚽ $30"], "🍎 $10", "10 ES MENOS QUE 30.")],
"5": [N("RELÁMPAGO. $10 + $10. ¿CUÁNTO ES?", 20, "10, 20.", tiempo=30),
      N("RELÁMPAGO. $20 + $5. ¿CUÁNTO ES?", 25, "20, 25.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES MÁS CARO?", ["$8", "$18"], "$18", "18 ES MÁS QUE 8.", tiempo=30),
      N("RELÁMPAGO. ALGO CUESTA $12. DAS $10. ¿CUÁNTO FALTA?", 2, "10, 11, 12.", tiempo=30)],
}
EXAMEN = [
 [1, MC("LA MONEDA ES DE…", ["PAPEL", "METAL"], "METAL", "EL BILLETE ES DE PAPEL.")],
 [1, MC("¿CUÁNTO VALE UN BILLETE DE $20?", ["2", "20", "200"], "20", "LO DICE SU NÚMERO.")],
 [1, N("TRES MONEDAS DE $10. ¿CUÁNTOS PESOS SON?", 30, "10, 20, 30.", **NEU("TRES MONEDAS DE $10. ¿CUÁNTO ES?"))],
 [2, N("$10 + $5 + $1. ¿CUÁNTO ES?", 16, "10, 15, 16.")],
 [2, N("$20 + $10 + $2. ¿CUÁNTO ES?", 32, "20, 30, 32.")],
 [2, MC("3 MONEDAS DE $10, ¿SON 3 O 30?", ["3", "30"], "30", "SUMAMOS LO QUE VALEN.")],
 [3, MC("ALGO CUESTA $12. ¿QUÉ DAS?", ["$10 + $2", "$10 + $5", "$5 + $5"], "$10 + $2", "10, 12. ¡JUSTO!")],
 [3, MC("UN CARAMELO CUESTA $5. ¿ALCANZA CON $2?", ["SÍ", "NO"], "NO", "2 ES MENOS QUE 5.")],
 [3, N("ALGO CUESTA $20. DAS $10. ¿CUÁNTO FALTA?", 10, "10, 20: FALTAN 10.")],
 [4, MC("¿QUÉ ES MÁS CARO?", ["$8", "$18"], "$18", "18 ES MÁS QUE 8.")],
 [4, MC("¿QUÉ ES MÁS BARATO?", ["$20", "$12"], "$12", "12 ES MENOS QUE 20.")],
 [4, MC("UN JUGO DE $20 Y UN CHUPETÍN DE $5. ¿CUÁL ES MÁS CARO?", ["EL JUGO", "EL DE $5"], "EL JUGO", "20 ES MÁS QUE 5.", **NEU("UN JUGO DE $20 Y UNA PALETA DE $5. ¿CUÁL ES MÁS CARO?"))],
 [4, N("¿CUÁNTO CUESTA LO MÁS CARO: $15, $8 O $30?", 30, "30 ES EL NÚMERO MÁS GRANDE.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 7, "estilo": "primeros",
     "practica": "Práctica general: dinero y números", "examen_titulo": "Nivel jefe: dinero y números",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-7.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
