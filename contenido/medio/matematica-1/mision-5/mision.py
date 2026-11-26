# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 5 · Comparar y ordenar números. Genera mision-5.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: las bolitas de Sofi y Tomi y la carrera de la escuela."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
N = lambda p, r, e, **k: {"t": "numeric", "p": p, "o": {}, "r": {"acepta": [r]}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a comparar números y decir cuál es mayor.",
"vas_a_ver": ["Bolsitas de 10 y sueltas", "Mayor y menor", "Mirar primero las decenas"],
"secciones": [
 S(1, "Las bolitas", [
  P("Sofi tiene <b>34</b> bolitas. Tomi tiene <b>43</b>."),
  IMG("Las bolitas de Sofi", "3 bolsitas y 4 sueltas: 34.", FG.bolsitas(3, 4)),
  IMG("Las bolitas de Tomi", "4 bolsitas y 3 sueltas: 43.", FG.bolsitas(4, 3)),
 ]),
 S(1, "¿Quién tiene más?", [
  D("Comparar", "Mirá primero las <b>bolsitas de 10</b>. Más bolsitas, número mayor."),
  P("43 tiene 4 bolsitas. 34 tiene 3. <b>43 es mayor</b>."),
  IMG("34 y 43 en la recta", "43 está más a la derecha: es mayor.", FG.recta_num(30, 45, [(34, "34"), (43, "43")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las bolitas. Las vas a usar en la carpeta."),
  IMG("Las bolitas de Ana", "Contá bolsitas y sueltas.", FG.bolsitas(5, 6)),
  IMG("Las bolitas de Leo", "Contá bolsitas y sueltas.", FG.bolsitas(6, 5)),
 ]),
],
"ejemplo_completo": {"titulo": "27 y 72", "planteo": "¿Cuál es mayor?", "pasos": ["27 tiene 2 decenas.", "72 tiene 7 decenas.", "72 es mayor."]},
"ejemplo_incompleto": {"titulo": "48 y 45", "planteo": "Completá.", "pasos": ["Los dos tienen ___ decenas.", "Miramos las sueltas: 8 y 5.", "El mayor es ___ ."]},
"ejemplo_solo": {"titulo": "39 y 40", "planteo": "¿Cuál es mayor?"},
"tip": {"titulo": "Mirá las decenas", "texto": "Si empatan, mirá las sueltas."},
"ojo": ["56 no es mayor que 65.", "Mirá primero la primera cifra."],
"resumen": [{"titulo": "Mayor", "texto": "Tiene más."}, {"titulo": "Menor", "texto": "Tiene menos."}, {"titulo": "Decenas", "texto": "Se miran primero."}],
"glosario": [{"palabra": "Decena", "significado": "Una bolsita de 10."}, {"palabra": "Comparar", "significado": "Ver cuál tiene más."}],
"carpeta": ["¿Cuántas bolitas tiene Ana?", "¿Cuántas bolitas tiene Leo?", "¿Quién tiene más, Ana o Leo?"],
"respuestas_carpeta": [["56"], ["65"], ["leo"]],
"soluciones": {"incompleto": "4. 48.", "solo": "40: tiene 4 decenas.", "carpeta": ["56.", "65.", "Leo."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ordenar números de menor a mayor.",
"vas_a_ver": ["Buscar el más chico", "Ordenar de menor a mayor", "Ver el orden en la recta"],
"secciones": [
 S(1, "La carrera", [
  P("Los corredores de la escuela tienen su número."),
  IMG("Desordenados", "59, 18, 71 y 36.", FG.chicos_numero([59, 18, 71, 36])),
  P("De <b>menor a mayor</b>: del más chico al más grande."),
  IMG("Ordenados", "18, 36, 59 y 71.", FG.chicos_numero([18, 36, 59, 71])),
 ]),
 S(1, "En la recta", [
  D("Menor a mayor", "Buscá el <b>más chico</b> y ponelo primero. Después, el que sigue."),
  IMG("El orden en la recta", "De izquierda a derecha.", FG.recta_num(10, 20, [(12, ""), (15, ""), (19, "")])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los corredores. Los vas a usar en la carpeta."),
  IMG("Corredores para ordenar", "Ordenalos de menor a mayor.", FG.chicos_numero([47, 74, 40])),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenar 25, 52, 12", "planteo": "De menor a mayor.", "pasos": ["El más chico es 12.", "Después va 25.", "Último va 52.", "12, 25, 52."]},
"ejemplo_incompleto": {"titulo": "Ordenar 63, 36, 33", "planteo": "Completá.", "pasos": ["Primero va el ___ .", "Después el ___ .", "Último el ___ ."]},
"ejemplo_solo": {"titulo": "Tus números", "planteo": "Ordená de menor a mayor: 80, 8, 18."},
"tip": {"titulo": "Empezá por el chico", "texto": "Buscá el más chico primero."},
"ojo": ["No mires solo la última cifra.", "Mirá primero las decenas."],
"resumen": [{"titulo": "Menor a mayor", "texto": "Del chico al grande."}, {"titulo": "Primero", "texto": "El más chico."}, {"titulo": "Recta", "texto": "De izquierda a derecha."}],
"glosario": [{"palabra": "Ordenar", "significado": "Poner uno detrás de otro."}, {"palabra": "Menor", "significado": "El más chico."}],
"carpeta": ["De menor a mayor, ¿qué número va primero?", "¿Qué número va segundo?", "¿Qué número va último?"],
"respuestas_carpeta": [["40"], ["47"], ["74"]],
"soluciones": {"incompleto": "33. 36. 63.", "solo": "8, 18, 80.", "carpeta": ["40.", "47.", "74."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ordenar números de mayor a menor.",
"vas_a_ver": ["Buscar el más grande", "Ordenar de mayor a menor", "Es al revés de menor a mayor"],
"secciones": [
 S(1, "Los puntos", [
  P("Terminó la carrera. Ordenamos los puntos de <b>mayor a menor</b>."),
  IMG("Desordenados", "48, 92, 30 y 75.", FG.chicos_numero([48, 92, 30, 75])),
  IMG("De mayor a menor", "92, 75, 48 y 30.", FG.chicos_numero([92, 75, 48, 30])),
 ]),
 S(1, "Al revés", [
  D("Mayor a menor", "Empezamos por el <b>más grande</b>. Es al revés de menor a mayor."),
  IMG("Uno difícil", "99, 90, 19 y 9.", FG.chicos_numero([99, 90, 19, 9])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los equipos. Los vas a usar en la carpeta."),
  IMG("Equipos para ordenar", "Ordenalos de mayor a menor.", FG.chicos_numero([38, 83, 80])),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenar 14, 41, 40", "planteo": "De mayor a menor.", "pasos": ["El más grande es 41.", "Después va 40.", "Último va 14.", "41, 40, 14."]},
"ejemplo_incompleto": {"titulo": "Ordenar 70, 17, 77", "planteo": "Completá.", "pasos": ["Primero va el ___ .", "Después el ___ .", "Último el ___ ."]},
"ejemplo_solo": {"titulo": "Al revés", "planteo": "Ordená de mayor a menor: 5, 55, 50."},
"tip": {"titulo": "Empezá por el grande", "texto": "Buscá el más grande primero."},
"ojo": ["9 es menor que 19.", "Mayor a menor empieza por el más grande."],
"resumen": [{"titulo": "Mayor a menor", "texto": "Del grande al chico."}, {"titulo": "Primero", "texto": "El más grande."}, {"titulo": "Al revés", "texto": "Que menor a mayor."}],
"glosario": [{"palabra": "Mayor", "significado": "El más grande."}, {"palabra": "Decreciente", "significado": "De mayor a menor."}],
"carpeta": ["De mayor a menor, ¿qué número va primero?", "¿Qué número va segundo?", "¿Qué número va último?"],
"respuestas_carpeta": [["83"], ["80"], ["38"]],
"soluciones": {"incompleto": "77. 70. 17.", "solo": "55, 50, 5.", "carpeta": ["83.", "80.", "38."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ubicar números y saltar en la recta numérica.",
"vas_a_ver": ["La recta del 0 al 100", "Más a la derecha, más grande", "Saltos para adelante y para atrás"],
"secciones": [
 S(1, "La rayuela gigante", [
  P("La recta es como una rayuela: cada casillero tiene un número."),
  IMG("La recta del 0 al 20", "Los números en orden.", FG.recta_num(0, 20, [(7, "7"), (12, "12")])),
 ]),
 S(1, "Saltos", [
  D("Saltar", "Para adelante, el número <b>crece</b>. Para atrás, <b>achica</b>."),
  P("Del 4, Tomi salta 3 y llega al 7."),
  IMG("Un salto de 3", "Del 4 al 7.", FG.recta_num(0, 12, [(4, "4"), (7, "7")], [(4, 7)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá la recta. La vas a usar en la carpeta."),
  IMG("La recta del 40 al 50", "Mirá el número marcado.", FG.recta_num(40, 50, [(46, "?")])),
 ]),
],
"ejemplo_completo": {"titulo": "Saltar 5", "planteo": "Tomi está en el 7 y salta 5.", "pasos": ["Cuenta 5 saltos: 8, 9, 10, 11, 12.", "Llega al 12."]},
"ejemplo_incompleto": {"titulo": "Volver 2", "planteo": "Tomi está en el 12 y vuelve 2.", "pasos": ["Cuenta para atrás: 11, ___ .", "Llega al ___ ."]},
"ejemplo_solo": {"titulo": "Más a la derecha", "planteo": "¿Cuál está más a la derecha: 29 o 92?"},
"tip": {"titulo": "Contá los saltos", "texto": "Un salto es un número."},
"ojo": ["Para atrás, el número achica.", "Más a la derecha es más grande."],
"resumen": [{"titulo": "La recta", "texto": "Números en orden."}, {"titulo": "Derecha", "texto": "Más grande."}, {"titulo": "Saltos", "texto": "Adelante o atrás."}],
"glosario": [{"palabra": "Recta numérica", "significado": "Una línea con los números en orden."}, {"palabra": "Saltar", "significado": "Moverse en la recta."}],
"carpeta": ["¿Qué número va en el lugar del signo de pregunta en la recta?", "Si estás en el 4 y saltás 3, ¿a qué número llegás?", "¿Cuál está más a la derecha: 29 o 92?"],
"respuestas_carpeta": [["46"], ["7"], ["92"]],
"soluciones": {"incompleto": "10. 10.", "solo": "92.", "carpeta": ["46.", "7.", "92."]},
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
 T("MIRÁ PRIMERO LAS DECENAS", [LD("MAYOR Y MENOR", "PARA COMPARAR, MIRÁ PRIMERO LAS <b>DECENAS</b>: GANA EL QUE TIENE MÁS."),
   LL("65 ES MAYOR QUE 56: TIENE 6 DECENAS.", "NO ALCANZA CON MIRAR LA ÚLTIMA CIFRA.")],
   {"modo": "comparar2"}, {"modo": "comparar2"}),
 T("SI EMPATAN", [LD("EMPATE", "SI LAS DECENAS SON IGUALES, GANA EL QUE TIENE MÁS <b>UNIDADES</b>."),
   LL("48 Y 45: LOS DOS TIENEN 4 DECENAS.", "8 ES MÁS QUE 5: 48 ES MAYOR.")],
   {"modo": "comparar2"}, {"modo": "comparar2"}),
], "recuerda": [
 RC("PRIMERO LAS DECENAS", "EL QUE TIENE MÁS DECENAS ES EL MAYOR.", "72 ES MAYOR QUE 27"),
 RC("SI EMPATAN", "MIRAMOS LAS UNIDADES PARA DECIDIR.", "39 ES MAYOR QUE 31"),
]}

N2["leccion"] = {"temas": [
 T("DE MENOR A MAYOR", [LD("EN ORDEN", "ORDENAR <b>DE MENOR A MAYOR</b> ES IR DEL MÁS CHICO AL MÁS GRANDE."),
   LL("PRIMERO BUSCÁ EL MÁS CHICO.", "40, 47, 74: VAN CRECIENDO.")],
   {"modo": "ordenar3", "orden": "asc"}, {"modo": "ordenar3", "orden": "asc"}),
 T("EN LA RECTA", [LD("IZQUIERDA", "EN LA RECTA, EL MÁS CHICO QUEDA MÁS A LA <b>IZQUIERDA</b>."),
   LP("POR ESO LEER LA RECTA DE IZQUIERDA A DERECHA ES IR DE MENOR A MAYOR.")],
   {"modo": "recta100"}, {"modo": "recta100"}),
], "recuerda": [
 RC("DE MENOR A MAYOR", "EMPEZAMOS POR EL MÁS CHICO Y TERMINAMOS EN EL MÁS GRANDE.", "12, 25, 52"),
 RC("EN LA RECTA", "LOS MENORES QUEDAN A LA IZQUIERDA.", "EL 30 ESTÁ ANTES QUE EL 70"),
]}

N3["leccion"] = {"temas": [
 T("DE MAYOR A MENOR", [LD("AL REVÉS", "ORDENAR <b>DE MAYOR A MENOR</b> ES IR DEL MÁS GRANDE AL MÁS CHICO."),
   LL("PRIMERO BUSCÁ EL MÁS GRANDE.", "83, 80, 38: VAN BAJANDO.")],
   {"modo": "ordenar3", "orden": "desc"}, {"modo": "ordenar3", "orden": "desc"}),
 T("DOS ORDENES", [LD("DAR VUELTA", "SI DAS VUELTA UNA LISTA DE MENOR A MAYOR, QUEDA <b>DE MAYOR A MENOR</b>."),
   LL("19, 90, 99 AL REVÉS ES 99, 90, 19.", "FIJATE QUÉ ORDEN TE PIDEN.")],
   {"modo": "ordenar3", "orden": "asc"}, {"modo": "ordenar3", "orden": "desc"}),
], "recuerda": [
 RC("DE MAYOR A MENOR", "EMPEZAMOS POR EL MÁS GRANDE Y TERMINAMOS EN EL MÁS CHICO.", "99, 90, 19"),
 RC("AL REVÉS", "ES LA MISMA LISTA DE MENOR A MAYOR, DADA VUELTA.", "41, 40, 14"),
]}

N4["leccion"] = {"temas": [
 T("LA RECTA DEL 0 AL 100", [LD("UBICAR", "PARA UBICAR UN NÚMERO, BUSCÁ EL <b>REDONDO</b> DE ANTES Y AVANZÁ."),
   LL("EL 46 ESTÁ DESPUÉS DEL 40.", "MÁS A LA DERECHA, MÁS GRANDE.")],
   {"modo": "recta100"}, {"modo": "recta100"}),
 T("SALTAR PARA ADELANTE", [LD("ADELANTE", "SALTAR <b>PARA ADELANTE</b> EN LA RECTA HACE CRECER EL NÚMERO."),
   LL("DEL 4 SALTO 3: 5, 6, 7.", "CONTÁ CADA SALTO CON EL DEDO.")],
   {"modo": "recta100", "que": "saltar", "dir": "adelante"}, {"modo": "recta100", "que": "saltar", "dir": "adelante"}),
 T("SALTAR PARA ATRÁS", [LD("ATRÁS", "SALTAR <b>PARA ATRÁS</b> EN LA RECTA HACE ACHICAR EL NÚMERO."),
   LL("DEL 12 VUELVO 2: 11, 10.", "NO SE CUENTA EL NÚMERO DONDE ESTÁS.")],
   {"modo": "recta100", "que": "saltar", "dir": "atras"}, {"modo": "recta100", "que": "saltar", "dir": "atras"}),
], "recuerda": [
 RC("UBICAR EN LA RECTA", "BUSCAMOS EL REDONDO DE ANTES Y AVANZAMOS.", "EL 73 ESTÁ ENTRE EL 70 Y EL 80"),
 RC("ADELANTE", "SALTAR PARA ADELANTE HACE CRECER EL NÚMERO.", "DEL 7 SALTO 5 Y LLEGO AL 12"),
 RC("ATRÁS", "SALTAR PARA ATRÁS HACE ACHICAR EL NÚMERO.", "DEL 10 VUELVO 3 Y LLEGO AL 7"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [MC("¿CUÁL ES MAYOR?", ["56", "65"], "65", "65 TIENE 6 DECENAS.", **A),
      MC("¿CUÁL ES MENOR?", ["48", "45"], "45", "EMPATAN EN DECENAS; 5 ES MENOS QUE 8.", **A),
      MC("LEO DICE QUE 29 ES MAYOR QUE 31 PORQUE 9 ES MÁS QUE 1. ¿CUÁL ES MAYOR DE VERDAD?", ["31", "29"], "31", "PRIMERO SE MIRAN LAS DECENAS: 3 ES MÁS QUE 2.", **ER),
      CLAS("¿ES MAYOR O MENOR QUE 50?", ["38", "71", "49", "56"], ["MENOR QUE 50", "MAYOR QUE 50"],
           {"38": "MENOR QUE 50", "71": "MAYOR QUE 50", "49": "MENOR QUE 50", "56": "MAYOR QUE 50"}, "38 Y 49 TIENEN MENOS DECENAS QUE 50; 56 Y 71 MÁS.", **AN)],
"2": [N("DE MENOR A MAYOR: 47, 74, 40. ¿QUÉ NÚMERO VA PRIMERO?", 40, "ES EL MÁS CHICO.", **A),
      ORD("ORDENÁ DE MENOR A MAYOR.", ["52", "25", "12", "21"], ["12", "21", "25", "52"], "12, 21, 25 Y 52: VAN CRECIENDO.", **A),
      MC("[[problema]] ANA TIENE 34 FIGURITAS, LEO 43 Y MICA 30. ¿QUIÉN TIENE MENOS?", ["MICA", "ANA", "LEO"], "MICA", "30 ES EL MÁS CHICO.", **AN),
      MC("EN LA RECTA, ¿CUÁL QUEDA MÁS A LA IZQUIERDA?", ["60", "16"], "16", "EL MÁS CHICO QUEDA A LA IZQUIERDA.", **RE)],
"3": [N("DE MAYOR A MENOR: 38, 83, 80. ¿QUÉ NÚMERO VA PRIMERO?", 83, "ES EL MÁS GRANDE.", **A),
      ORD("ORDENÁ DE MAYOR A MENOR.", ["19", "99", "90", "91"], ["99", "91", "90", "19"], "99, 91, 90 Y 19: VAN BAJANDO.", **A),
      MC("SOFI ORDENÓ DE MAYOR A MENOR ASÍ: 14, 40, 41. ¿QUÉ HIZO MAL?", ["LO ORDENÓ AL REVÉS", "NADA, ESTÁ BIEN", "LE FALTA UN NÚMERO"], "LO ORDENÓ AL REVÉS", "DE MAYOR A MENOR ES 41, 40, 14.", **ER),
      N("DE MAYOR A MENOR: 77, 70, 17. ¿QUÉ NÚMERO VA ÚLTIMO?", 17, "EL ÚLTIMO ES EL MÁS CHICO.", **A)],
"4": [N("ESTÁS EN EL 4 Y SALTÁS 3. ¿A QUÉ NÚMERO LLEGÁS?", 7, "4, 5, 6, 7.", **A),
      MC("¿CUÁL ESTÁ MÁS A LA DERECHA EN LA RECTA?", ["29", "92"], "92", "ES EL MAYOR.", **A),
      MC("JUAN ESTÁ EN EL 9, VUELVE 2 Y DICE: 9, 8. ¿A QUÉ NÚMERO LLEGA DE VERDAD?", ["7", "8", "11"], "7", "EL 9 NO SE CUENTA: 8, 7.", **ER),
      N("[[problema]] EN EL JUEGO, TU FICHA ESTÁ EN EL 11 Y AVANZA 4. ¿EN QUÉ CASILLERO QUEDA?", 15, "12, 13, 14, 15.", **AN)],
"5": [MC("RELÁMPAGO. ¿CUÁL ES MAYOR?", ["39", "40"], "40", "4 DECENAS.", tiempo=30, **A),
      N("RELÁMPAGO. DE MENOR A MAYOR: 80, 8, 18. ¿CUÁL VA PRIMERO?", 8, "ES EL MÁS CHICO.", tiempo=30, **A),
      N("RELÁMPAGO. DE MAYOR A MENOR: 55, 5, 50. ¿CUÁL VA PRIMERO?", 55, "ES EL MÁS GRANDE.", tiempo=30, **A),
      N("RELÁMPAGO. ESTÁS EN EL 12 Y VOLVÉS 2. ¿A QUÉ NÚMERO LLEGÁS?", 10, "12, 11, 10.", tiempo=40, **A)],
}
EXAMEN = [
 [1, MC("¿CUÁL ES MAYOR?", ["34", "43"], "43", "TIENE 4 DECENAS.", **A)],
 [1, MC("¿CUÁL ES MAYOR?", ["68", "61"], "68", "EMPATAN EN DECENAS; 8 ES MÁS QUE 1.", **A)],
 [1, MC("TOMI DICE QUE 19 ES MAYOR QUE 21 PORQUE TIENE UN 9. ¿CUÁL ES MAYOR?", ["21", "19"], "21", "2 DECENAS ES MÁS QUE 1.", **ER)],
 [2, N("DE MENOR A MAYOR: 63, 36, 33. ¿QUÉ NÚMERO VA PRIMERO?", 33, "ES EL MÁS CHICO.", **A)],
 [2, ORD("ORDENÁ DE MENOR A MAYOR.", ["71", "18", "59"], ["18", "59", "71"], "DEL MÁS CHICO AL MÁS GRANDE.", **A)],
 [2, MC("EN LA RECTA, LOS NÚMEROS MÁS CHICOS QUEDAN A LA…", ["IZQUIERDA", "DERECHA"], "IZQUIERDA", "CRECEN HACIA LA DERECHA.", **RE)],
 [3, N("DE MAYOR A MENOR: 70, 17, 77. ¿QUÉ NÚMERO VA PRIMERO?", 77, "ES EL MÁS GRANDE.", **A)],
 [3, ORD("ORDENÁ DE MAYOR A MENOR.", ["30", "92", "75"], ["92", "75", "30"], "DEL MÁS GRANDE AL MÁS CHICO.", **A)],
 [3, MC("[[problema]] LEO TIENE 52 PUNTOS, ANA 25 Y JUAN 55. ¿QUIÉN TIENE MÁS?", ["JUAN", "LEO", "ANA"], "JUAN", "55 ES EL MAYOR.", **AN)],
 [4, N("ESTÁS EN EL 7 Y SALTÁS 5. ¿A QUÉ NÚMERO LLEGÁS?", 12, "8, 9, 10, 11, 12.", **A)],
 [4, N("ESTÁS EN EL 10 Y VOLVÉS 3. ¿A QUÉ NÚMERO LLEGÁS?", 7, "9, 8, 7.", **A)],
 [4, N("EN LA RECTA, ¿CUÁL ESTÁ MÁS A LA DERECHA: 30 O 70?", 70, "ES EL MAYOR.", **A)],
 [4, MC("EN LA RECTA, ¿CUÁL ESTÁ MÁS CERCA DEL 0?", ["15", "51"], "15", "ES EL MENOR.", **A)],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 5, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: comparar y ordenar números", "examen_titulo": "Nivel jefe: comparar y ordenar números",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
