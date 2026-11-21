# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 11 · Dobles y sumas de iguales. Genera mision-11.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el espejo mágico de Sofi (lo que se pone delante aparece dos veces).
Niveles: 1 los dobles · 2 sumas de números iguales · 3 casi dobles · 4 cálculo mental con dobles. Resultados hasta 20."""
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
"objetivo": "Vas a saber qué es el doble de un número.",
"vas_a_ver": ["El espejo mágico", "Dos veces lo mismo", "El doble"],
"secciones": [
 S(1, "El espejo mágico", [
  P("Sofi pone <b>3</b> manzanas frente al espejo. ¡Aparecen <b>3</b> más!"),
  IMG("3 y 3", "3 + 3 = 6.", FG.juntar(("manzana", 3), ("manzana", 3), "6")),
 ]),
 S(1, "El doble", [
  D("El doble", "Es tener <b>dos veces</b> la misma cantidad."),
  P("El doble de <b>4</b> es <b>8</b>: 4 + 4 = 8."),
  IMG("4 y 4", "El doble de 4 es 8.", FG.juntar(("pelota", 4), ("pelota", 4), "8")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el espejo. Lo vas a usar en la carpeta."),
  IMG("Estrellas", "Contá cada lado.", FG.juntar(("estrella", 5), ("estrella", 5), "?")),
 ]),
],
"ejemplo_completo": {"titulo": "El doble de 2", "planteo": "2 globos frente al espejo.", "pasos": ["Aparecen 2 más.", "2 + 2 = 4.", "El doble de 2 es 4."]},
"ejemplo_incompleto": {"titulo": "El doble de 1", "planteo": "Completá.", "pasos": ["1 + 1 = ___ ."]},
"ejemplo_solo": {"titulo": "Tus manos", "planteo": "Tenés 5 dedos en cada mano. ¿Cuántos dedos son?"},
"tip": {"titulo": "Mirá tus manos", "texto": "Las dos manos son un doble: 5 + 5."},
"ojo": ["El doble suma el mismo número dos veces.", "El doble de 3 es 6, no 33."],
"resumen": [{"titulo": "Espejo", "texto": "Lo mismo dos veces."}, {"titulo": "Doble", "texto": "4 + 4 = 8."}, {"titulo": "Manos", "texto": "5 + 5 = 10."}],
"glosario": [{"palabra": "Doble", "significado": "Dos veces lo mismo."}, {"palabra": "Espejo", "significado": "Muestra lo mismo otra vez."}],
"carpeta": ["¿Cuántas estrellas hay de un lado?", "¿Cuántas estrellas hay del otro lado?", "¿Cuál es el doble de 5?"],
"respuestas_carpeta": [["5"], ["5"], ["10"]],
"soluciones": {"incompleto": "2.", "solo": "10 dedos.", "carpeta": ["5.", "5.", "10."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a sumar números iguales.",
"vas_a_ver": ["Sumas con el mismo número", "Dobles más grandes", "Sumar tres iguales"],
"secciones": [
 S(1, "Números iguales", [
  P("<b>6 + 6</b> es una suma de iguales. Es el doble de 6."),
  P("Contamos: 6… <b>7, 8, 9, 10, 11, 12</b>."),
  IMG("6 y 6", "6 + 6 = 12.", FG.juntar(("manzana", 6), ("manzana", 6), "12")),
 ]),
 S(1, "Tres iguales", [
  D("Sumar iguales", "Sumar el mismo número <b>varias veces</b>."),
  P("<b>2 + 2 + 2 = 6</b>. Tres veces el 2."),
  IMG("Tres grupos de 2", "2 + 2 + 2 = 6.", FG.grupos_letras([("A", "pelota", 2), ("B", "pelota", 2), ("C", "pelota", 2)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Grupos de 3", "Contá cada grupo.", FG.grupos_letras([("A", "estrella", 3), ("B", "estrella", 3), ("C", "estrella", 3)])),
 ]),
],
"ejemplo_completo": {"titulo": "7 + 7", "planteo": "¿Cuánto es 7 + 7?", "pasos": ["Empezamos en 7.", "Seguimos 7 más: 8, 9, 10, 11, 12, 13, 14.", "7 + 7 = 14."]},
"ejemplo_incompleto": {"titulo": "3 + 3 + 3", "planteo": "Completá.", "pasos": ["3 + 3 = ___ .", "Y 3 más: ___ ."]},
"ejemplo_solo": {"titulo": "Medias", "planteo": "Tenés 4 pares de medias. ¿Cuántas medias son?"},
"tip": {"titulo": "De a pares", "texto": "Las medias y los zapatos vienen de a 2."},
"ojo": ["Contá cuántas veces está el número.", "2 + 2 + 2 son tres veces el 2."],
"resumen": [{"titulo": "Iguales", "texto": "El mismo número."}, {"titulo": "Doble", "texto": "6 + 6 = 12."}, {"titulo": "Tres veces", "texto": "2 + 2 + 2 = 6."}],
"glosario": [{"palabra": "Iguales", "significado": "Que son lo mismo."}, {"palabra": "Par", "significado": "Dos cosas iguales."}],
"carpeta": ["¿Cuántos grupos hay?", "¿Cuántas estrellas hay en cada grupo?", "¿Cuánto es 3 + 3 + 3?"],
"respuestas_carpeta": [["3"], ["3"], ["9"]],
"soluciones": {"incompleto": "6. 9.", "solo": "8 medias.", "carpeta": ["3.", "3.", "9."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a usar los dobles para sumar casi dobles.",
"vas_a_ver": ["Uno más que el doble", "4 + 5 con el doble de 4", "Un truco rápido"],
"secciones": [
 S(1, "Casi iguales", [
  P("<b>4 + 5</b> es casi un doble. El 5 tiene <b>1 más</b> que el 4."),
  IMG("4 y 5", "4 + 5 = 9.", FG.juntar(("pelota", 4), ("pelota", 5), "9")),
 ]),
 S(1, "El truco", [
  D("Casi doble", "Dos números que están <b>uno al lado del otro</b>."),
  P("4 + 4 = 8. Uno más: <b>4 + 5 = 9</b>."),
  IMG("El doble y uno más", "4 + 4 y 1 más.", FG.agregar("pelota", 8, 1, "8 + 1 = 9")),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("3 y 4", "Usá el doble de 3.", FG.juntar(("manzana", 3), ("manzana", 4), "?")),
 ]),
],
"ejemplo_completo": {"titulo": "5 + 6", "planteo": "¿Cuánto es 5 + 6?", "pasos": ["5 + 5 = 10.", "Uno más.", "5 + 6 = 11."]},
"ejemplo_incompleto": {"titulo": "6 + 7", "planteo": "Completá.", "pasos": ["6 + 6 = ___ .", "Uno más: 6 + 7 = ___ ."]},
"ejemplo_solo": {"titulo": "Pensá", "planteo": "¿Qué doble te ayuda para 2 + 3?"},
"tip": {"titulo": "Doble y uno más", "texto": "Usá el doble del más chico y sumá 1."},
"ojo": ["Sumá 1, no 2.", "Usá el doble del número más chico."],
"resumen": [{"titulo": "Casi doble", "texto": "4 + 5."}, {"titulo": "Doble", "texto": "4 + 4 = 8."}, {"titulo": "Uno más", "texto": "4 + 5 = 9."}],
"glosario": [{"palabra": "Casi", "significado": "Muy cerca."}, {"palabra": "Al lado", "significado": "Como el 4 y el 5."}],
"carpeta": ["¿Cuánto es 3 + 3?", "¿Cuántas manzanas hay en el segundo grupo?", "¿Cuánto es 3 + 4?"],
"respuestas_carpeta": [["6"], ["4"], ["7"]],
"soluciones": {"incompleto": "12. 13.", "solo": "2 + 2 = 4, uno más: 5.", "carpeta": ["6.", "4.", "7."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a calcular rápido con los dobles.",
"vas_a_ver": ["La tabla de dobles", "Calcular sin contar", "Dobles en la vida"],
"secciones": [
 S(1, "Los dobles de memoria", [
  P("1 + 1 = 2. 2 + 2 = 4. 3 + 3 = 6. 4 + 4 = 8. 5 + 5 = 10."),
  IMG("Los dobles", "Del 1 al 5.", FG.cuentas([("1 + 1", 2), ("2 + 2", 4), ("3 + 3", 6), ("4 + 4", 8), ("5 + 5", 10)])),
 ]),
 S(1, "Dobles más grandes", [
  D("Cálculo mental", "Calcular <b>en la cabeza</b>, sin dibujar ni contar."),
  P("6 + 6 = 12. 7 + 7 = 14. 8 + 8 = 16. 9 + 9 = 18. 10 + 10 = 20."),
  IMG("Más dobles", "Del 6 al 10.", FG.cuentas([("6 + 6", 12), ("7 + 7", 14), ("8 + 8", 16), ("9 + 9", 18), ("10 + 10", 20)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá las tarjetas. Las vas a usar en la carpeta."),
  IMG("Completá", "Escribí el doble.", FG.cuentas([("2 + 2", 4), ("7 + 7", 14), ("9 + 9", 18)], ocultar=(0, 1, 2))),
 ]),
],
"ejemplo_completo": {"titulo": "8 + 8", "planteo": "¿Cuánto es 8 + 8?", "pasos": ["Es un doble.", "Lo sabemos: 16."]},
"ejemplo_incompleto": {"titulo": "Dobles", "planteo": "Completá.", "pasos": ["9 + 9 = ___ .", "10 + 10 = ___ ."]},
"ejemplo_solo": {"titulo": "Ruedas", "planteo": "Una bici tiene 2 ruedas. ¿Cuántas ruedas tienen 2 bicis?"},
"tip": {"titulo": "Saltan de a 2", "texto": "Los dobles son 2, 4, 6, 8, 10… ¡saltan de a 2!"},
"ojo": ["Los dobles siempre son números pares.", "10 + 10 es 20, no 1010."],
"resumen": [{"titulo": "Memoria", "texto": "Sin contar."}, {"titulo": "Hasta 10", "texto": "5 + 5 = 10."}, {"titulo": "Hasta 20", "texto": "10 + 10 = 20."}],
"glosario": [{"palabra": "Cálculo mental", "significado": "Calcular en la cabeza."}, {"palabra": "Par", "significado": "2, 4, 6, 8…"}],
"carpeta": ["¿Cuánto es 2 + 2?", "¿Cuánto es 7 + 7?", "¿Cuánto es 9 + 9?"],
"respuestas_carpeta": [["4"], ["14"], ["18"]],
"soluciones": {"incompleto": "18. 20.", "solo": "4 ruedas.", "carpeta": ["4.", "14.", "18."]},
}

ACT = {
"1": [N("¿CUÁL ES EL DOBLE DE 3?", 6, "3 + 3 = 6."),
      MC("EL DOBLE ES…", ["DOS VECES LO MISMO", "SACAR UNO", "UNO SOLO"], "DOS VECES LO MISMO", "COMO EN EL ESPEJO.")],
"2": [N("¿CUÁNTO ES 6 + 6?", 12, "EL DOBLE DE 6 ES 12."),
      N("¿CUÁNTO ES 2 + 2 + 2?", 6, "TRES VECES EL 2: 6.")],
"3": [N("SI 4 + 4 = 8, ¿CUÁNTO ES 4 + 5?", 9, "UNO MÁS QUE EL DOBLE."),
      MC("¿QUÉ DOBLE AYUDA PARA 5 + 6?", ["5 + 5", "6 + 1", "3 + 3"], "5 + 5", "5 + 5 = 10 Y UNO MÁS: 11.")],
"4": [N("¿CUÁNTO ES 8 + 8?", 16, "EL DOBLE DE 8 ES 16."),
      N("¿CUÁNTO ES 10 + 10?", 20, "EL DOBLE DE 10 ES 20.")],
"5": [N("RELÁMPAGO. ¿CUÁL ES EL DOBLE DE 5?", 10, "5 + 5 = 10.", tiempo=30),
      N("RELÁMPAGO. ¿CUÁNTO ES 7 + 7?", 14, "EL DOBLE DE 7.", tiempo=30),
      N("RELÁMPAGO. ¿CUÁNTO ES 3 + 4?", 7, "3 + 3 = 6 Y UNO MÁS.", tiempo=30),
      MC("RELÁMPAGO. ¿CUÁL ES UN DOBLE?", ["9 + 9", "9 + 2", "9 + 1"], "9 + 9", "EL MISMO NÚMERO DOS VECES.", tiempo=30)],
}
EXAMEN = [
 [1, N("¿CUÁL ES EL DOBLE DE 4?", 8, "4 + 4 = 8.")],
 [1, N("¿CUÁL ES EL DOBLE DE 1?", 2, "1 + 1 = 2.")],
 [1, MC("¿CUÁNTOS DEDOS HAY EN LAS DOS MANOS?", ["5", "10", "20"], "10", "5 + 5 = 10.")],
 [2, N("¿CUÁNTO ES 9 + 9?", 18, "EL DOBLE DE 9 ES 18.")],
 [2, N("¿CUÁNTO ES 3 + 3 + 3?", 9, "TRES VECES EL 3: 9.")],
 [2, N("TENÉS 3 PARES DE MEDIAS. ¿CUÁNTAS MEDIAS SON?", 6, "2 + 2 + 2 = 6.")],
 [3, N("SI 6 + 6 = 12, ¿CUÁNTO ES 6 + 7?", 13, "UNO MÁS QUE EL DOBLE.")],
 [3, N("¿CUÁNTO ES 2 + 3?", 5, "2 + 2 = 4 Y UNO MÁS.")],
 [3, MC("4 + 5 ES UN…", ["CASI DOBLE", "DOBLE", "NINGUNO"], "CASI DOBLE", "4 Y 5 ESTÁN UNO AL LADO DEL OTRO.")],
 [4, N("¿CUÁNTO ES 5 + 5?", 10, "EL DOBLE DE 5.")],
 [4, N("¿CUÁNTO ES 7 + 7?", 14, "EL DOBLE DE 7.")],
 [4, MC("¿CUÁNTO ES 10 + 10?", ["20", "1010", "11"], "20", "EL DOBLE DE 10 ES 20.")],
 [4, N("2 BICIS. CADA UNA TIENE 2 RUEDAS. ¿CUÁNTAS RUEDAS SON?", 4, "2 + 2 = 4.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 11, "estilo": "primeros",
     "practica": "Práctica general: dobles y sumas de iguales", "examen_titulo": "Nivel jefe: dobles y sumas de iguales",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-11.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
