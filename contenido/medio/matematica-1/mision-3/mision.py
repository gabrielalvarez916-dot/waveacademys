# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 3 · La serie numérica hasta 50. Genera mision-3.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el álbum de figuritas de Tomi (igual que clases.py)."""
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
"objetivo": "Vas a contar del 1 al 30.",
"vas_a_ver": ["El álbum del 1 al 30", "Filas de 10", "Los del veinte empiezan con 2"],
"secciones": [
 S(1, "El álbum de Tomi", [
  P("Tomi junta figuritas. Cada una tiene un número."),
  P("Su álbum va <b>del 1 al 30</b>."),
  IMG("El álbum", "Del 1 al 30, de a 10 por fila.", FG.cuadro(30)),
 ]),
 S(1, "Los del veinte", [
  D("Del 20 al 29", "Todos empiezan con <b>2</b>: 20, 21, 22… 29."),
  IMG("Los del veinte", "Están todos en la misma fila.", FG.cuadro(30, resaltar=range(20, 30))),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("El tren de figuritas", "Del 21 al 30.", FG.tren(21, 30, (24, 29))),
 ]),
],
"ejemplo_completo": {"titulo": "Contar desde el 18", "planteo": "Tomi cuenta desde el 18.", "pasos": ["18, 19.", "Después del 19 viene el 20.", "20, 21, 22."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí los que faltan.", "pasos": ["26, 27, ___ , 29, 30.", "19, ___ , 21."]},
"ejemplo_solo": {"titulo": "Contar", "planteo": "Contá en voz alta del 15 al 30."},
"tip": {"titulo": "Mirá el álbum", "texto": "Cada fila tiene 10 números."},
"ojo": ["Después del 29 viene el 30.", "Después del 19 viene el 20."],
"resumen": [{"titulo": "Hasta 30", "texto": "En orden."}, {"titulo": "Filas", "texto": "De a 10."}, {"titulo": "Del 20 al 29", "texto": "Empiezan con 2."}],
"glosario": [{"palabra": "Fila", "significado": "Números uno al lado del otro."}, {"palabra": "Veinte", "significado": "El número 20."}],
"carpeta": ["¿Qué número falta en el primer vagón con ?", "¿Qué número falta en el segundo vagón con ?", "¿Qué número viene después del 29?"],
"respuestas_carpeta": [["24"], ["29"], ["30"]],
"soluciones": {"incompleto": "28. 20.", "solo": "15, 16, 17… 30.", "carpeta": ["24.", "29.", "30."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar del 1 al 50 y descubrir secretos del cuadro.",
"vas_a_ver": ["El álbum hasta 50", "En una fila, todos empiezan igual", "En una columna, todos terminan igual"],
"secciones": [
 S(1, "Hasta el 50", [
  P("El álbum de Tomi creció: ahora llega al <b>50</b>."),
  IMG("El álbum hasta 50", "Cinco filas de 10.", FG.cuadro(50)),
 ]),
 S(1, "Secretos del cuadro", [
  D("Filas", "En una fila, todos <b>empiezan igual</b>: 31, 32, 33…"),
  D("Columnas", "En una columna, todos <b>terminan igual</b>: 5, 15, 25…"),
  IMG("La columna del 5", "Todos terminan en 5.", FG.cuadro(50, resaltar=(5, 15, 25, 35, 45))),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro con huecos", "Completá los números que faltan.", FG.cuadro(50, faltan=(33, 40, 46))),
 ]),
],
"ejemplo_completo": {"titulo": "La fila del 40", "planteo": "¿Cómo empiezan los números de la fila del 40?", "pasos": ["41, 42, 43…", "Todos empiezan con 4.", "Al final está el 50."]},
"ejemplo_incompleto": {"titulo": "La columna del 2", "planteo": "Completá.", "pasos": ["2, 12, ___ , 32, 42.", "Todos terminan en ___ ."]},
"ejemplo_solo": {"titulo": "Después del 39", "planteo": "¿Qué número viene después del 39?"},
"tip": {"titulo": "Mirá filas y columnas", "texto": "Te ayudan a encontrar cualquier número."},
"ojo": ["Después del 39 viene el 40.", "Después del 49 viene el 50."],
"resumen": [{"titulo": "Hasta 50", "texto": "Cinco filas."}, {"titulo": "Filas", "texto": "Empiezan igual."}, {"titulo": "Columnas", "texto": "Terminan igual."}],
"glosario": [{"palabra": "Columna", "significado": "Números uno debajo del otro."}, {"palabra": "Cincuenta", "significado": "El número 50."}],
"carpeta": ["¿Qué número falta en la fila del 30?", "¿Qué número falta al final de la fila del 40?", "¿Qué número falta en la columna del 6?"],
"respuestas_carpeta": [["33"], ["40"], ["46"]],
"soluciones": {"incompleto": "22. 2.", "solo": "40.", "carpeta": ["33.", "40.", "46."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a encontrar el anterior y el siguiente de un número.",
"vas_a_ver": ["El anterior", "El siguiente", "Buscarlos en el álbum y en la recta"],
"secciones": [
 S(1, "Antes y después", [
  D("Anterior y siguiente", "El <b>anterior</b> va antes. El <b>siguiente</b> va después."),
  P("El anterior del 27 es el 26. El siguiente es el 28."),
  IMG("En la recta", "26 va antes y 28 va después.", FG.recta_num(20, 30, [(26, "antes"), (27, ""), (28, "después")])),
 ]),
 S(1, "En el álbum", [
  P("En el álbum, el anterior está a la <b>izquierda</b>."),
  P("El siguiente está a la <b>derecha</b>."),
  IMG("La figurita 38", "37, 38 y 39.", FG.cuadro(40, resaltar=(37, 38, 39))),
 ]),
 S(2, "Para practicar", [
  P("Mirá la recta. La vas a usar en la carpeta."),
  IMG("La recta del 40 al 50", "Buscá el anterior y el siguiente.", FG.recta_num(40, 50, [(45, "45")])),
 ]),
],
"ejemplo_completo": {"titulo": "El 33", "planteo": "¿Cuál es el anterior y el siguiente del 33?", "pasos": ["Antes del 33 va el 32.", "Después del 33 va el 34.", "32, 33, 34."]},
"ejemplo_incompleto": {"titulo": "El 20", "planteo": "Completá.", "pasos": ["El anterior del 20 es el ___ .", "El siguiente del 20 es el ___ ."]},
"ejemplo_solo": {"titulo": "El 49", "planteo": "¿Cuál es el siguiente del 49?"},
"tip": {"titulo": "Contá para atrás", "texto": "El anterior es contar un número para atrás."},
"ojo": ["El siguiente del 29 es el 30.", "El anterior del 40 es el 39."],
"resumen": [{"titulo": "Anterior", "texto": "Va antes."}, {"titulo": "Siguiente", "texto": "Va después."}, {"titulo": "Dónde", "texto": "En el álbum o en la recta."}],
"glosario": [{"palabra": "Anterior", "significado": "El número que va antes."}, {"palabra": "Siguiente", "significado": "El número que va después."}],
"carpeta": ["¿Cuál es el anterior del 45?", "¿Cuál es el siguiente del 45?", "¿Cuál es el anterior del 30?"],
"respuestas_carpeta": [["44"], ["46"], ["29"]],
"soluciones": {"incompleto": "19. 21.", "solo": "50.", "carpeta": ["44.", "46.", "29."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a encontrar el número que falta.",
"vas_a_ver": ["Buscar el lugar vacío", "Contar desde el anterior", "Completar el número"],
"secciones": [
 S(1, "Huecos en el álbum", [
  P("A Tomi le faltan figuritas."),
  P("Para saber cuál falta, <b>contamos desde el anterior</b>."),
  IMG("El álbum con huecos", "Faltan el 8, el 17 y el 25.", FG.cuadro(30, faltan=(8, 17, 25))),
 ]),
 S(1, "En el tren", [
  D("Qué número falta", "Decí el número de antes y <b>seguí contando</b>."),
  IMG("El tren con huecos", "42, 43… falta el 44.", FG.tren(42, 49, (44, 47))),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro para completar", "Escribí los que faltan.", FG.cuadro(50, faltan=(12, 29, 41))),
 ]),
],
"ejemplo_completo": {"titulo": "23, 24, ___, 26", "planteo": "¿Qué número falta?", "pasos": ["Antes del hueco está el 24.", "Después del 24 viene el 25.", "Falta el 25."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí el que falta.", "pasos": ["35, 36, ___ , 38.", "48, ___ , 50."]},
"ejemplo_solo": {"titulo": "Contar", "planteo": "¿Qué número falta? 9, 10, ___, 12."},
"tip": {"titulo": "Contá desde antes", "texto": "Decí el anterior y seguí."},
"ojo": ["Mirá el número de antes del hueco.", "Contá de a uno, sin saltear."],
"resumen": [{"titulo": "Buscar", "texto": "El lugar vacío."}, {"titulo": "Contar", "texto": "Desde el anterior."}, {"titulo": "Completar", "texto": "El que falta."}],
"glosario": [{"palabra": "Hueco", "significado": "Un lugar vacío."}, {"palabra": "Faltar", "significado": "No estar."}],
"carpeta": ["¿Qué número falta en la fila del 10?", "¿Qué número falta en la fila del 20?", "¿Qué número falta en la fila del 40?"],
"respuestas_carpeta": [["12"], ["29"], ["41"]],
"soluciones": {"incompleto": "37. 49.", "solo": "11.", "carpeta": ["12.", "29.", "41."]},
}

ACT = {
"1": [N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 29?", 30, "DESPUÉS DEL 29 VIENE EL 30."),
      MC("¿CON QUÉ NÚMERO EMPIEZAN LOS DEL VEINTE?", ["1", "2", "3"], "2", "20, 21, 22… EMPIEZAN CON 2.")],
"2": [N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 39?", 40, "DESPUÉS DEL 39 VIENE EL 40."),
      MC("5, 15, 25, 35… ¿QUÉ SIGUE?", ["36", "45", "40"], "45", "TODOS TERMINAN EN 5.")],
"3": [N("¿CUÁL ES EL ANTERIOR DEL 33?", 32, "ANTES DEL 33 VA EL 32."),
      N("¿CUÁL ES EL SIGUIENTE DEL 19?", 20, "DESPUÉS DEL 19 VA EL 20.")],
"4": [N("¿QUÉ NÚMERO FALTA? 23, 24, ___, 26", 25, "DESPUÉS DEL 24 VIENE EL 25."),
      N("¿QUÉ NÚMERO FALTA? 47, 48, ___, 50", 49, "DESPUÉS DEL 48 VIENE EL 49.")],
"5": [N("RELÁMPAGO. ¿QUÉ SIGUE DESPUÉS DEL 49?", 50, "49, 50.", tiempo=30),
      N("RELÁMPAGO. ¿CUÁL ES EL ANTERIOR DEL 40?", 39, "39, 40.", tiempo=30),
      N("RELÁMPAGO. ¿QUÉ FALTA? 36, ___, 38", 37, "36, 37, 38.", tiempo=30),
      MC("RELÁMPAGO. ¿CON QUÉ EMPIEZAN LOS DEL TREINTA?", ["3", "2"], "3", "30, 31, 32…", tiempo=30)],
}
EXAMEN = [
 [1, N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 19?", 20, "19, 20.")],
 [1, N("¿QUÉ NÚMERO FALTA? 26, 27, ___, 29", 28, "27, 28, 29.")],
 [1, MC("¿CUÁNTOS NÚMEROS HAY EN CADA FILA DEL ÁLBUM?", ["5", "10", "20"], "10", "CADA FILA TIENE 10.")],
 [2, N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 39?", 40, "39, 40.")],
 [2, MC("¿CON QUÉ NÚMERO EMPIEZAN LOS DEL CUARENTA?", ["4", "5", "3"], "4", "41, 42, 43…")],
 [2, MC("2, 12, 22, 32… ¿QUÉ SIGUE?", ["42", "33", "23"], "42", "TODOS TERMINAN EN 2.")],
 [3, N("¿CUÁL ES EL ANTERIOR DEL 27?", 26, "26 VA ANTES DEL 27.")],
 [3, N("¿CUÁL ES EL SIGUIENTE DEL 27?", 28, "28 VA DESPUÉS DEL 27.")],
 [3, MC("¿CUÁL ES EL SIGUIENTE DEL 29?", ["30", "210", "20"], "30", "29, 30.")],
 [4, N("¿QUÉ NÚMERO FALTA? 43, ___, 45", 44, "43, 44, 45.")],
 [4, N("¿QUÉ NÚMERO FALTA? 18, 19, ___, 21", 20, "19, 20, 21.")],
 [4, N("¿QUÉ NÚMERO FALTA? 38, ___, 40", 39, "38, 39, 40.")],
 [4, MC("PARA SABER QUÉ NÚMERO FALTA, ¿QUÉ HACÉS?", ["CONTAR DESDE EL ANTERIOR", "ADIVINAR"], "CONTAR DESDE EL ANTERIOR", "DECÍS EL DE ANTES Y SEGUÍS.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: la serie numérica hasta 50", "examen_titulo": "Nivel jefe: la serie numérica hasta 50",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
