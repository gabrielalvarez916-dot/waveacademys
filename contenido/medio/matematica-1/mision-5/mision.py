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

ACT = {
"1": [MC("¿CUÁL ES MAYOR?", ["56", "65"], "65", "65 TIENE 6 DECENAS."),
      MC("¿CUÁL ES MENOR?", ["48", "45"], "45", "EMPATAN EN DECENAS; 5 ES MENOS QUE 8.")],
"2": [MC("DE MENOR A MAYOR, ¿CUÁL VA PRIMERO?", ["47", "74", "40"], "40", "ES EL MÁS CHICO."),
      MC("¿CUÁL ESTÁ ORDENADO DE MENOR A MAYOR?", ["12, 25, 52", "52, 25, 12", "25, 12, 52"], "12, 25, 52", "DEL CHICO AL GRANDE.")],
"3": [MC("DE MAYOR A MENOR, ¿CUÁL VA PRIMERO?", ["38", "83", "80"], "83", "ES EL MÁS GRANDE."),
      MC("¿CUÁL ESTÁ ORDENADO DE MAYOR A MENOR?", ["99, 90, 19", "19, 90, 99", "90, 99, 19"], "99, 90, 19", "DEL GRANDE AL CHICO.")],
"4": [N("ESTÁS EN EL 4 Y SALTÁS 3. ¿A QUÉ NÚMERO LLEGÁS?", 7, "4, 5, 6, 7."),
      MC("¿CUÁL ESTÁ MÁS A LA DERECHA EN LA RECTA?", ["29", "92"], "92", "ES EL MAYOR.")],
"5": [MC("RELÁMPAGO. ¿CUÁL ES MAYOR?", ["39", "40"], "40", "4 DECENAS.", tiempo=30),
      MC("RELÁMPAGO. DE MENOR A MAYOR, ¿CUÁL VA PRIMERO?", ["80", "8", "18"], "8", "ES EL MÁS CHICO.", tiempo=30),
      MC("RELÁMPAGO. DE MAYOR A MENOR, ¿CUÁL VA PRIMERO?", ["55", "5", "50"], "55", "ES EL MÁS GRANDE.", tiempo=30),
      N("RELÁMPAGO. ESTÁS EN EL 12 Y VOLVÉS 2. ¿A QUÉ NÚMERO LLEGÁS?", 10, "12, 11, 10.", tiempo=40)],
}
EXAMEN = [
 [1, MC("¿CUÁL ES MAYOR?", ["34", "43"], "43", "TIENE 4 DECENAS.")],
 [1, MC("¿CUÁL ES MENOR?", ["27", "72"], "27", "TIENE 2 DECENAS.")],
 [1, MC("¿CUÁL ES MAYOR?", ["68", "61"], "68", "EMPATAN EN DECENAS; 8 ES MÁS QUE 1.")],
 [2, MC("DE MENOR A MAYOR, ¿CUÁL VA PRIMERO?", ["63", "36", "33"], "33", "ES EL MÁS CHICO.")],
 [2, MC("DE MENOR A MAYOR, ¿CUÁL VA ÚLTIMO?", ["18", "71", "59"], "71", "ES EL MÁS GRANDE.")],
 [2, MC("¿CUÁL ESTÁ ORDENADO DE MENOR A MAYOR?", ["8, 18, 80", "80, 18, 8", "18, 8, 80"], "8, 18, 80", "DEL CHICO AL GRANDE.")],
 [3, MC("DE MAYOR A MENOR, ¿CUÁL VA PRIMERO?", ["70", "17", "77"], "77", "ES EL MÁS GRANDE.")],
 [3, MC("DE MAYOR A MENOR, ¿CUÁL VA ÚLTIMO?", ["92", "30", "75"], "30", "ES EL MÁS CHICO.")],
 [3, MC("¿CUÁL ESTÁ ORDENADO DE MAYOR A MENOR?", ["41, 40, 14", "14, 40, 41", "40, 41, 14"], "41, 40, 14", "DEL GRANDE AL CHICO.")],
 [4, N("ESTÁS EN EL 7 Y SALTÁS 5. ¿A QUÉ NÚMERO LLEGÁS?", 12, "8, 9, 10, 11, 12.")],
 [4, N("ESTÁS EN EL 10 Y VOLVÉS 3. ¿A QUÉ NÚMERO LLEGÁS?", 7, "9, 8, 7.")],
 [4, MC("EN LA RECTA, ¿CUÁL ESTÁ MÁS A LA DERECHA?", ["30", "70"], "70", "ES EL MAYOR.")],
 [4, MC("EN LA RECTA, ¿CUÁL ESTÁ MÁS CERCA DEL 0?", ["15", "51"], "15", "ES EL MENOR.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: comparar y ordenar números", "examen_titulo": "Nivel jefe: comparar y ordenar números",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
