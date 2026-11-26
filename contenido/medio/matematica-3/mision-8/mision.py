# -*- coding: utf-8 -*-
"""Matemática 3 (Nivel Medio, 3.º año) · Misión 8 · Estimar y calcular con calculadora. Genera mision-8.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la campaña de tapitas solidarias de la escuela.
Niveles: 1 estimar antes · 2 calculadora como control · 3 teclas rotas · 4 problemas con calculadora."""
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
"objetivo": "Vas a estimar antes de usar la calculadora.",
"vas_a_ver": ["Redondear al mil", "Estimar", "Comparar con la pantalla"],
"secciones": [
 S(1, "Pensar antes", [
  P("Juntaron 3.890 y 2.105 tapitas."),
  P("4.000 + 2.000 = 6.000: da <b>cerca de 6.000</b>."),
  IMG("Estimamos", "Con redondos.", FG.cuentas([("3.890 → 4.000", ""), ("2.105 → 2.000", "")])),
 ]),
 S(1, "Después calculamos", [
  D("Estimar", "Calcular <b>más o menos</b> antes de hacer la cuenta."),
  P("La calculadora da 5.995: está cerca."),
  IMG("La pantalla", "5.995.", FG.calculadora("5995", texto="3890 + 2105")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sumas. Las vas a usar en la carpeta."),
  IMG("Sumas para estimar", "¿Cerca de cuánto?", FG.cuentas([("4.120 + 2.950", "?"), ("6.030 + 1.980", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Estimar", "planteo": "5.210 + 3.840.", "pasos": ["5.000 + 4.000.", "Cerca de 9.000."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Redondeá al mil.", "pasos": ["1.920 → ___", "7.150 → ___"]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿2.870 + 3.020 da cerca de 6.000 o de 60.000?"},
"tip": {"titulo": "Antes", "texto": "Estimá antes de apretar teclas."},
"ojo": ["Estimar no es la cuenta exacta.", "Redondeá al mil más cercano."],
"resumen": [{"titulo": "Estimar", "texto": "Antes."}, {"titulo": "Redondos", "texto": "Al mil."}, {"titulo": "Comparar", "texto": "Con la pantalla."}],
"glosario": [{"palabra": "Estimar", "significado": "Calcular más o menos."}, {"palabra": "Pantalla", "significado": "Donde se ve el número."}],
"carpeta": ["¿4.120 + 2.950 da cerca de qué número?", "¿6.030 + 1.980 da cerca de qué número?", "Leo dice que 3.890 + 2.105 da cerca de 60.000. ¿Cerca de cuánto da?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["7000", "7.000"], ["8000", "8.000"], ["6000", "6.000"]],
"soluciones": {"incompleto": "2.000. 7.000.", "solo": "6.000.", "carpeta": ["7.000.", "8.000.", "6.000."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a usar la calculadora para controlar.",
"vas_a_ver": ["La calculadora hace lo que apretamos", "Controlar una cuenta", "Revisar si no da"],
"secciones": [
 S(1, "¿Será verdad?", [
  P("La pantalla dice 29.130. La cuenta era 2.768 + 1.455."),
  P("Tiene que dar cerca de 4.000: <b>se apretó mal</b>."),
  IMG("Pantalla equivocada", "29.130 está muy lejos.", FG.calculadora("29130", texto="¿ESTÁ BIEN?")),
 ]),
 S(1, "Controlar", [
  D("Controlar", "Hacemos la cuenta <b>de dos maneras</b> y vemos si da igual."),
  P("A mano y con la calculadora."),
  IMG("Dos caminos", "A mano y con calculadora.", FG.cuentas([("a mano", "4.900"), ("calculadora", "4.900")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las pantallas. Las vas a usar en la carpeta."),
  IMG("¿Están bien?", "Estimá cada una.", FG.cuentas([("1.500 + 2.500", "4.000"), ("3.000 + 2.000", "50.000")])),
 ]),
],
"ejemplo_completo": {"titulo": "Controlar", "planteo": "La pantalla dice 2.300 + 1.200 = 3.500.", "pasos": ["Estimo: 2.000 + 1.000 = 3.000.", "3.500 está cerca: tiene sentido."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La pantalla dice 4.100 + 1.900 = 60.000.", "pasos": ["Estimo: ___ .", "¿Está bien? ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Está bien 7.200 − 2.100 = 5.100?"},
"tip": {"titulo": "Desconfiá", "texto": "Si da muy lejos, hacé la cuenta otra vez."},
"ojo": ["La calculadora hace lo que apretamos.", "Compará siempre con lo estimado."],
"resumen": [{"titulo": "Controlar", "texto": "Dos maneras."}, {"titulo": "Estimar", "texto": "Para revisar."}, {"titulo": "Teclas", "texto": "Con cuidado."}],
"glosario": [{"palabra": "Controlar", "significado": "Ver si está bien."}, {"palabra": "Tecla", "significado": "Botón de la calculadora."}],
"carpeta": ["¿Está bien 1.500 + 2.500 = 4.000? Escribí sí o no.", "¿Está bien 3.000 + 2.000 = 50.000? ¿Cuánto da?", "Sofi cree que la calculadora nunca se equivoca. ¿Quién se equivoca?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["si", "sí"], ["5000", "5.000"], ["el que aprieta", "nosotros", "quien aprieta", "la persona"]],
"soluciones": {"incompleto": "6.000. No.", "solo": "Sí.", "carpeta": ["Sí.", "No: da 5.000.", "El que aprieta mal las teclas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a calcular aunque una tecla no ande.",
"vas_a_ver": ["La tecla rota", "Desarmar el número", "Otro camino"],
"secciones": [
 S(1, "Se rompió el 5", [
  P("Tomi necesita escribir 3.500 y el 5 no anda."),
  P("3.400 + 100 = <b>3.500</b>. ¡Sin el 5!"),
  IMG("Sin el 5", "3.400 + 100.", FG.calculadora("3500", texto="3400 + 100")),
 ]),
 S(1, "Otro camino", [
  D("Tecla rota", "Buscamos números <b>sin esa cifra</b> que sumen lo mismo."),
  P("Revisamos cada número."),
  IMG("Sin el 7", "2.600 + 100 = 2.700.", FG.cuentas([("2.600 + 100", "2.700"), ("6.000 + 1.000", "7.000")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los números. Los vas a usar en la carpeta."),
  IMG("Tecla 3 rota", "¿Cómo los hacés?", FG.cuentas([("sin el 3", "1.300"), ("sin el 3", "3.000")])),
 ]),
],
"ejemplo_completo": {"titulo": "Tecla rota", "planteo": "No anda el 8. Quiero 4.800.", "pasos": ["4.700 + 100.", "Da 4.800."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "No anda el 6. Quiero 6.000.", "pasos": ["5.000 + ___ .", "Da 6.000."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "No anda el 2. ¿Cómo hacés 2.200?"},
"tip": {"titulo": "Revisá", "texto": "Mirá que ningún número tenga la tecla rota."},
"ojo": ["3.000 + 500 usa el 5.", "Siempre hay otro camino."],
"resumen": [{"titulo": "Tecla rota", "texto": "Otro camino."}, {"titulo": "Desarmar", "texto": "En partes."}, {"titulo": "Revisar", "texto": "Cada número."}],
"glosario": [{"palabra": "Rota", "significado": "Que no funciona."}, {"palabra": "Camino", "significado": "Forma de hacer algo."}],
"carpeta": ["No anda el 3. ¿Cuánto le sumás a 1.200 para tener 1.300?", "No anda el 3. ¿Cuánto le sumás a 2.000 para tener 3.000?", "Leo hizo 3.000 + 500 con el 5 roto. ¿Qué número usó mal?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [["100"], ["1000", "1.000"], ["500"]],
"soluciones": {"incompleto": "1.000.", "solo": "1.100 + 1.100.", "carpeta": ["100.", "1.000.", "500: tiene un 5."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a resolver problemas con calculadora.",
"vas_a_ver": ["Leer y estimar", "Calcular", "Ver si tiene sentido"],
"secciones": [
 S(1, "Tres grados", [
  P("Juntaron 2.350, 1.870 y 960 tapitas."),
  P("Estimamos: cerca de 5.000. La calculadora da <b>5.180</b>."),
  IMG("La suma", "Tres números.", FG.calculadora("5180", texto="2350 + 1870 + 960")),
 ]),
 S(1, "¿Tiene sentido?", [
  D("Resolver", "Leemos, <b>estimamos</b>, calculamos y miramos si tiene sentido."),
  P("Faltan 8.000 − 5.180 = 2.820 para la meta."),
  IMG("Hasta la meta", "Una distancia.", FG.cuentas([("8.000 − 5.180", "2.820")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá el problema. Lo vas a usar en la carpeta."),
  IMG("Tapitas", "4.150, 2.380 y 1.070.", FG.cuentas([("4.150 + 2.380 + 1.070", "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Problema", "planteo": "Juntaron 1.250 y 3.480.", "pasos": ["Estimo: cerca de 4.000.", "Calculadora: 4.730. Tiene sentido."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Tienen 6.300. Quieren 9.000.", "pasos": ["Cuenta: 9.000 − ___ .", "Faltan ___ ."]},
"ejemplo_solo": {"titulo": "Resolvé", "planteo": "Juntaron 2.020, 1.530 y 990. ¿Cuántas son?"},
"tip": {"titulo": "Estimá", "texto": "Antes y después de la calculadora."},
"ojo": ["Mirá si la respuesta tiene sentido.", "Respondé con una oración."],
"resumen": [{"titulo": "Leer", "texto": "El problema."}, {"titulo": "Estimar", "texto": "Y calcular."}, {"titulo": "Sentido", "texto": "Revisar."}],
"glosario": [{"palabra": "Meta", "significado": "A donde se quiere llegar."}, {"palabra": "Sentido", "significado": "Que es lógico."}],
"carpeta": ["Juntaron 4.150, 2.380 y 1.070 tapitas. ¿Cuántas son?", "Si la meta es 9.000, ¿cuántas les faltan?", "Mía respondió 76.000 tapitas. ¿Cuántas son de verdad?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["7600", "7.600"], ["1400", "1.400"], ["7600", "7.600"]],
"soluciones": {"incompleto": "6.300. 2.700.", "solo": "4.540.", "carpeta": ["7.600.", "1.400.", "7.600."]},
}

LD = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
LL = lambda *it: {"tipo": "lista", "items": list(it)}
T = lambda tit, bl, ej, ex: {"titulo": tit, "explicacion": bl, "ejemplo": {"motor": "primeros", "p": ej}, "ejercicio": {"motor": "primeros_x", "p": ex}}
RC = lambda c, d, e: {"concepto": c, "definicion": d, "ejemplo": e}

N1["leccion"] = {"temas": [
 T("EL MIL MÁS CERCANO", [LD("REDONDEAR", "CAMBIAMOS UN NÚMERO POR EL <b>MIL</b> QUE TIENE MÁS CERCA."),
   LL("MIRAMOS LAS CENTENAS.", "500 O MÁS: VA AL MIL DE ARRIBA.")],
   {"modo": "recta10000"}, {"modo": "recta10000", "que": "entre"}),
 T("ESTIMAR ANTES DE CALCULAR", [LD("ESTIMAR", "ANTES DE APRETAR TECLAS, PENSAMOS <b>MÁS O MENOS</b> CUÁNTO DA."),
   LL("SUMAMOS LOS REDONDOS.", "DESPUÉS MIRAMOS SI LA PANTALLA SE PARECE.")],
   {"modo": "calcu4"}, {"modo": "calcu4"}),
], "recuerda": [
 RC("REDONDEAR", "CAMBIAMOS EL NÚMERO POR EL MIL QUE ESTÁ MÁS CERCA.", "5.210 ESTÁ CERCA DEL 5.000"),
 RC("ESTIMAR", "PENSAMOS CUÁNTO DA MÁS O MENOS ANTES DE CALCULAR.", "5.210 + 3.840 DA CERCA DE 9.000"),
]}
N2["leccion"] = {"temas": [
 T("¿LO QUE DICE LA PANTALLA ESTÁ BIEN?", [LD("CONTROLAR", "LA CALCULADORA HACE <b>LO QUE APRETAMOS</b>: SI APRETAMOS MAL, DA MAL."),
   LL("COMPARAMOS CON LO ESTIMADO.", "SI DA MUY LEJOS, LA REPETIMOS.")],
   {"modo": "calcu4", "que": "control"}, {"modo": "calcu4", "que": "control"}),
 T("DOS CAMINOS", [LD("LÁPIZ Y TECLAS", "RESOLVEMOS EN <b>COLUMNAS</b> CON LÁPIZ Y COMPARAMOS CON LA PANTALLA."),
   LL("SI COINCIDEN, PODEMOS CONFIAR.", "SI NO COINCIDEN, BUSCAMOS EL ERROR.")],
   {"modo": "columna", "cifras": 4}, {"modo": "columna", "cifras": 4, "que": "control"}),
], "recuerda": [
 RC("CONTROLAR", "COMPARAMOS LO QUE DICE LA PANTALLA CON LO QUE ESTIMAMOS.", "4.100 + 1.900 NO PUEDE DAR 60.000"),
 RC("DOS CAMINOS", "SI A MANO Y CON CALCULADORA DA IGUAL, ESTÁ BIEN.", "2.300 + 1.200 = 3.500 DE LAS DOS MANERAS"),
]}
N3["leccion"] = {"temas": [
 T("CUANDO UNA TECLA NO ANDA", [LD("OTRO CAMINO", "ARMAMOS EL NÚMERO CON OTROS QUE <b>NO TIENEN</b> ESA CIFRA."),
   LL("LO DESARMAMOS EN DOS PARTES.", "REVISAMOS QUE NINGUNA PARTE USE LA TECLA ROTA.")],
   {"modo": "calcu4", "que": "rota"}, {"modo": "calcu4", "que": "rota"}),
], "recuerda": [
 RC("TECLA ROTA", "BUSCAMOS NÚMEROS SIN ESA CIFRA QUE SUMEN LO MISMO.", "SIN EL 8: 4.700 + 100 = 4.800"),
 RC("REVISAR", "CADA NÚMERO QUE APRETAMOS TIENE QUE ESTAR SIN LA TECLA ROTA.", "SIN EL 5 NO SIRVE 3.000 + 500"),
]}
N4["leccion"] = {"temas": [
 T("PROBLEMAS CON CALCULADORA", [LD("PROBLEMAS LARGOS", "LA CALCULADORA AYUDA CON <b>NÚMEROS GRANDES</b>; EL PLAN ES NUESTRO."),
   LL("PRIMERO DECIDIMOS QUÉ CUENTA HACER.", "AL FINAL CONTESTAMOS CON PALABRAS.")],
   {"modo": "problema4", "tipo": "pasos"}, {"modo": "calcu4", "que": "problema"}),
], "recuerda": [
 RC("RESOLVER", "LEEMOS, ESTIMAMOS, CALCULAMOS Y REVISAMOS EL RESULTADO.", "1.250 + 3.480 = 4.730, CERCA DE 4.000"),
 RC("TIENE SENTIDO", "LA RESPUESTA TIENE QUE PARECERSE A LO QUE ESTIMAMOS.", "NO PUEDEN SER 76.000 TAPITAS"),
]}

ACT = {
"1": [MC("5.210 + 3.840 DA CERCA DE…", ["9.000", "90.000", "900"], "9.000", "5.000 + 4.000.", n="aplicar"),
      N("¿A QUÉ MIL ESTÁ MÁS CERCA EL 7.150?", 7000, "150 ES POCO.", n="aplicar"),
      MC("LEO DICE QUE 3.890 + 2.105 DA CERCA DE 60.000. ¿CERCA DE CUÁNTO DA?", ["6.000", "60.000", "600"], "6.000", "4.000 + 2.000.", n="error"),
      CLAS("¿PUEDE SER EL RESULTADO DE 2.870 + 3.020?", ["5.890", "58.900", "589", "5.900"], ["PUEDE SER", "NO PUEDE SER"], {"5.890": "PUEDE SER", "58.900": "NO PUEDE SER", "589": "NO PUEDE SER", "5.900": "PUEDE SER"}, "TIENE QUE DAR CERCA DE 6.000.", n="analizar")],
"2": [MC("LA PANTALLA DICE 4.100 + 1.900 = 60.000. ¿ESTÁ BIEN?", ["NO", "SÍ"], "NO", "DA CERCA DE 6.000.", n="aplicar"),
      MC("¿ESTÁ BIEN 7.200 − 2.100 = 5.100?", ["SÍ", "NO"], "SÍ", "7.000 − 2.000 = 5.000.", n="aplicar"),
      MC("SOFI CREE QUE LA CALCULADORA NUNCA SE EQUIVOCA. ¿QUÉ PASA?", ["HACE LO QUE APRETAMOS", "NUNCA FALLA", "SIEMPRE FALLA"], "HACE LO QUE APRETAMOS", "SI APRETAMOS MAL, DA MAL.", n="error"),
      N("[[problema]] LA PANTALLA DIO 29.130 PARA 2.768 + 1.455. ¿CUÁNTO DA BIEN?", 4223, "CERCA DE 4.000.", n="analizar")],
"3": [MC("NO ANDA EL 5. ¿CÓMO HACÉS 3.500?", ["3.400 + 100", "3.000 + 500", "3.500 + 0"], "3.400 + 100", "NINGUNO TIENE 5.", n="aplicar"),
      N("NO ANDA EL 6. 5.000 + ___ = 6.000", 1000, "1.000 NO TIENE 6.", n="aplicar"),
      MC("LEO HIZO 3.000 + 500 CON EL 5 ROTO. ¿QUÉ USÓ MAL?", ["EL 500", "EL 3.000", "EL +"], "EL 500", "500 TIENE UN 5.", n="error"),
      UNIR("NO ANDA EL 7. UNÍ CADA NÚMERO CON SU CUENTA.", ["2.700", "7.000", "1.700"], ["6.000 + 1.000", "1.600 + 100", "2.600 + 100"], {"2.700": "2.600 + 100", "7.000": "6.000 + 1.000", "1.700": "1.600 + 100"}, "NINGUNA USA EL 7.", n="analizar")],
"4": [N("JUNTARON 1.250 Y 3.480 TAPITAS. ¿CUÁNTAS SON?", 4730, "CERCA DE 4.000.", n="aplicar"),
      N("[[problema]] TIENEN 6.300. LA META ES 9.000. ¿CUÁNTAS FALTAN?", 2700, "9.000 − 6.300.", n="analizar"),
      MC("MÍA RESPONDIÓ 76.000 PARA 4.150 + 2.380 + 1.070. ¿CUÁNTO ES?", ["7.600", "76.000", "760"], "7.600", "ESTIMÁ: CERCA DE 7.000.", n="error"),
      ORD("ORDENÁ LOS PASOS.", ["CALCULO", "LEO", "ESTIMO", "REVISO"], ["LEO", "ESTIMO", "CALCULO", "REVISO"], "PRIMERO LEER.", n="recordar")],
"5": [MC("RELÁMPAGO. 1.900 + 2.100 DA CERCA DE…", ["4.000", "40.000"], "4.000", "2.000 + 2.000.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. NO ANDA EL 4. ¿4.000 ES…?", ["3.000 + 1.000", "2.000 + 2.000 + 0 + 4"], "3.000 + 1.000", "SIN EL 4.", tiempo=30, n="aplicar"),
      N("RELÁMPAGO. 8.000 − 5.180 = ___", 2820, "2.820.", tiempo=40, n="aplicar"),
      MC("RELÁMPAGO. ¿LA CALCULADORA HACE…?", ["LO QUE APRETAMOS", "LO QUE PENSAMOS"], "LO QUE APRETAMOS", "POR ESO ESTIMAMOS.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("6.030 + 1.980 DA CERCA DE…", ["8.000", "80.000", "7.000"], "8.000", "6.000 + 2.000.", n="aplicar")],
 [1, N("¿A QUÉ MIL ESTÁ MÁS CERCA EL 1.920?", 2000, "FALTAN 80.", n="aplicar")],
 [1, TF("ESTIMAR ES HACER LA CUENTA EXACTA.", "FALSO", "ES CALCULAR MÁS O MENOS.", n="recordar")],
 [2, MC("LA PANTALLA DICE 3.000 + 2.000 = 50.000. ¿ESTÁ BIEN?", ["NO", "SÍ"], "NO", "DA 5.000.", n="aplicar")],
 [2, MC("SI LA CUENTA A MANO Y LA CALCULADORA DAN IGUAL…", ["ESTÁ BIEN", "ESTÁ MAL"], "ESTÁ BIEN", "LOS DOS CAMINOS COINCIDEN.", n="analizar")],
 [2, MC("TOMI APRETÓ 2768 + 14555. ¿QUÉ PASÓ?", ["APRETÓ UNA TECLA DE MÁS", "ESTÁ BIEN"], "APRETÓ UNA TECLA DE MÁS", "ERA 1.455.", n="error")],
 [3, MC("NO ANDA EL 8. ¿CÓMO HACÉS 4.800?", ["4.700 + 100", "4.000 + 800", "4.800 + 0"], "4.700 + 100", "SIN EL 8.", n="aplicar")],
 [3, N("NO ANDA EL 2. 1.100 + ___ = 2.200", 1100, "1.100 NO TIENE 2.", n="analizar")],
 [3, TF("SI UNA TECLA NO ANDA, NO SE PUEDE HACER LA CUENTA.", "FALSO", "SIEMPRE HAY OTRO CAMINO.", n="error")],
 [4, N("JUNTARON 2.020, 1.530 Y 990. ¿CUÁNTAS SON?", 4540, "CERCA DE 4.500.", n="aplicar")],
 [4, N("[[problema]] TIENEN 5.180 TAPITAS. QUIEREN 8.000. ¿CUÁNTAS FALTAN?", 2820, "8.000 − 5.180.", n="analizar")],
 [4, MC("¿QUÉ HACEMOS DESPUÉS DE CALCULAR?", ["VER SI TIENE SENTIDO", "BORRAR TODO", "NADA"], "VER SI TIENE SENTIDO", "COMPARAMOS CON LO ESTIMADO.", n="recordar")],
]
M = {"subject_id": "651eda34-d09a-45f2-82bf-e28abcc0c9ae", "tema": 8, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: estimar y calcular con calculadora", "examen_titulo": "Nivel jefe: estimar y calcular con calculadora",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
