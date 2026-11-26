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
"vas_a_ver": ["El álbum del 0 al 30", "Filas de 10", "Los del veinte empiezan con 2"],
"secciones": [
 S(1, "El álbum de Tomi", [
  P("Tomi junta figuritas. Cada una tiene un número."),
  P("Su álbum va <b>del 0 al 30</b>."),
  IMG("El álbum", "Del 0 al 30, de a 10 por fila.", FG.cuadro(30, desde=0)),
 ]),
 S(1, "Los del veinte", [
  D("Del 20 al 29", "Todos empiezan con <b>2</b>: 20, 21, 22… 29."),
  IMG("Los del veinte", "Están todos en la misma fila.", FG.cuadro(30, desde=0, resaltar=range(20, 30))),
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
"carpeta": ["¿Qué número falta en el primer vagón vacío?", "¿Qué número falta en el segundo vagón vacío?", "¿Qué número viene después del 29?"],
"respuestas_carpeta": [["24"], ["29"], ["30"]],
"soluciones": {"incompleto": "28. 20.", "solo": "15, 16, 17… 30.", "carpeta": ["24.", "29.", "30."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar del 1 al 50 y descubrir secretos del cuadro.",
"vas_a_ver": ["El álbum hasta 50", "En una fila, todos empiezan igual", "En una columna, todos terminan igual"],
"secciones": [
 S(1, "Hasta el 50", [
  P("El álbum de Tomi creció: ahora llega al <b>50</b>."),
  IMG("El álbum hasta 50", "Filas de 10. Cada fila empieza con un redondo.", FG.cuadro(50, desde=0)),
 ]),
 S(1, "Secretos del cuadro", [
  D("Filas", "En una fila, todos <b>empiezan igual</b>: 31, 32, 33…"),
  D("Columnas", "En una columna, todos <b>terminan igual</b>: 5, 15, 25…"),
  IMG("La columna del 5", "Todos terminan en 5.", FG.cuadro(50, desde=0, resaltar=(5, 15, 25, 35, 45))),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro con huecos", "Completá los números que faltan.", FG.cuadro(50, desde=0, faltan=(33, 40, 46))),
 ]),
],
"ejemplo_completo": {"titulo": "La fila del 40", "planteo": "¿Cómo empiezan los números de la fila del 40?", "pasos": ["40, 41, 42…", "Todos empiezan con 4.", "Al final está el 49."]},
"ejemplo_incompleto": {"titulo": "La columna del 2", "planteo": "Completá.", "pasos": ["2, 12, ___ , 32, 42.", "Todos terminan en ___ ."]},
"ejemplo_solo": {"titulo": "Después del 39", "planteo": "¿Qué número viene después del 39?"},
"tip": {"titulo": "Mirá filas y columnas", "texto": "Te ayudan a encontrar cualquier número."},
"ojo": ["Después del 39 viene el 40.", "Después del 49 viene el 50."],
"resumen": [{"titulo": "Hasta 50", "texto": "Filas de 10."}, {"titulo": "Filas", "texto": "Empiezan igual."}, {"titulo": "Columnas", "texto": "Terminan igual."}],
"glosario": [{"palabra": "Columna", "significado": "Números uno debajo del otro."}, {"palabra": "Cincuenta", "significado": "El número 50."}],
"carpeta": ["¿Qué número falta en la fila del 30?", "¿Qué número falta al principio de la fila del 40?", "¿Qué número falta en la columna del 6?"],
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
  IMG("La figurita 38", "37, 38 y 39.", FG.cuadro(40, desde=0, resaltar=(37, 38, 39))),
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
  IMG("El álbum con huecos", "Faltan el 8, el 17 y el 25.", FG.cuadro(30, desde=0, faltan=(8, 17, 25))),
 ]),
 S(1, "En el tren", [
  D("Qué número falta", "Decí el número de antes y <b>seguí contando</b>."),
  IMG("El tren con huecos", "42, 43… falta el 44.", FG.tren(42, 49, (44, 47))),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro para completar", "Escribí los que faltan.", FG.cuadro(50, desde=0, faltan=(12, 29, 41))),
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
 T("EL ÁLBUM DEL 0 AL 30", [LD("FILAS DE 10", "EN EL ÁLBUM, CADA FILA TIENE <b>10 NÚMEROS</b> Y EMPIEZA CON UN REDONDO."),
   LL("LA PRIMERA FILA VA DEL 0 AL 9.", "DESPUÉS DEL 9 VIENE EL 10.")],
   {"modo": "cuadro", "que": "contar", "hasta": 30}, {"modo": "cuadro", "que": "falta", "hasta": 30}),
 T("LOS DEL VEINTE", [LD("DEL 20 AL 29", "TODOS LOS NÚMEROS DEL 20 AL 29 <b>EMPIEZAN CON 2</b>."),
   LP("DESPUÉS DEL 29 VIENE EL 30, QUE ES UN NÚMERO REDONDO.")],
   {"modo": "tren", "desde": 19, "hasta": 30}, {"modo": "falta", "desde": 18, "hasta": 30}),
], "recuerda": [
 RC("FILAS DE 10", "CADA FILA DEL ÁLBUM TIENE DIEZ NÚMEROS EN ORDEN.", "20, 21, 22… 29"),
 RC("LOS DEL VEINTE", "LOS NÚMEROS DEL 20 AL 29 EMPIEZAN CON 2.", "DESPUÉS DEL 29 VIENE EL 30"),
]}

N2["leccion"] = {"temas": [
 T("EL ÁLBUM HASTA 50", [LD("HASTA 50", "EL ÁLBUM SIGUE CON LAS FILAS DEL <b>30</b> Y DEL <b>40</b> Y LLEGA AL 50."),
   LL("CADA FILA EMPIEZA CON UN REDONDO.", "DESPUÉS DEL 49 VIENE EL 50.")],
   {"modo": "cuadro", "que": "contar", "hasta": 50}, {"modo": "cuadro", "que": "falta", "hasta": 50}),
 T("EN UNA FILA", [LD("UNA FILA", "EN UNA <b>FILA</b> DEL CUADRO, TODOS LOS NÚMEROS EMPIEZAN IGUAL."),
   LL("LA FILA VA DE COSTADO.", "41, 42, 43… EMPIEZAN CON 4.")],
   {"modo": "cuadro", "que": "fila", "hasta": 50}, {"modo": "cuadro", "que": "fila", "hasta": 50}),
 T("EN UNA COLUMNA", [LD("UNA COLUMNA", "EN UNA <b>COLUMNA</b> DEL CUADRO, TODOS LOS NÚMEROS TERMINAN IGUAL."),
   LL("LA COLUMNA VA PARA ABAJO.", "5, 15, 25, 35 Y 45 TERMINAN EN 5.")],
   {"modo": "cuadro", "que": "columna", "hasta": 50}, {"modo": "cuadro", "que": "columna", "hasta": 50}),
], "recuerda": [
 RC("LA FILA", "VA DE COSTADO Y SUS NÚMEROS EMPIEZAN IGUAL.", "31, 32, 33 EMPIEZAN CON 3"),
 RC("LA COLUMNA", "VA PARA ABAJO Y SUS NÚMEROS TERMINAN IGUAL.", "7, 17, 27 TERMINAN EN 7"),
]}

N3["leccion"] = {"temas": [
 T("ANTERIOR Y SIGUIENTE", [LD("ANTES Y DESPUÉS", "EL <b>ANTERIOR</b> VA JUSTO ANTES Y EL <b>SIGUIENTE</b> VA JUSTO DESPUÉS."),
   LL("EL ANTERIOR DEL 35 ES 34.", "EL SIGUIENTE DEL 35 ES 36.")],
   {"modo": "anterior_siguiente", "min": 21, "max": 49}, {"modo": "anterior_siguiente", "min": 21, "max": 49}),
 T("DESPUÉS DE UN 9", [LD("UN 9 Y UN REDONDO", "DESPUÉS DE UN NÚMERO QUE TERMINA EN 9 VIENE UN <b>REDONDO</b>."),
   LL("DESPUÉS DEL 39 VIENE EL 40.", "ANTES DEL 30 VA EL 29.")],
   {"modo": "tren", "desde": 28, "hasta": 41}, {"modo": "redondo", "max": 50}),
], "recuerda": [
 RC("ANTERIOR", "ES EL NÚMERO QUE VA JUSTO ANTES.", "EL ANTERIOR DEL 42 ES 41"),
 RC("SIGUIENTE", "ES EL NÚMERO QUE VA JUSTO DESPUÉS.", "EL SIGUIENTE DEL 42 ES 43"),
 RC("DESPUÉS DE UN 9", "SIEMPRE VIENE UN NÚMERO REDONDO.", "29 Y DESPUÉS 30"),
]}

N4["leccion"] = {"temas": [
 T("EL VAGÓN VACÍO", [LD("EL QUE FALTA", "PARA SABER QUÉ NÚMERO FALTA, MIRÁ EL <b>DE ANTES</b> Y SEGUÍ CONTANDO."),
   LL("31, 32, ?, 34: FALTA EL 33.", "NO HACE FALTA EMPEZAR DESDE EL 1.")],
   {"modo": "tren", "desde": 30, "hasta": 38}, {"modo": "falta", "desde": 20, "hasta": 50}),
 T("EN EL CUADRO", [LD("EL CASILLERO VACÍO", "EN EL CUADRO, EL QUE FALTA <b>SIGUE</b> AL NÚMERO DE SU IZQUIERDA."),
   LP("SI ESTÁ AL PRINCIPIO DE LA FILA, ES UN NÚMERO REDONDO.")],
   {"modo": "cuadro", "que": "fila", "hasta": 50}, {"modo": "cuadro", "que": "falta", "hasta": 50}),
], "recuerda": [
 RC("EL QUE FALTA", "SE ENCUENTRA CONTANDO DESDE EL NÚMERO DE ANTES.", "26, 27, ?, 29: ES EL 28"),
 RC("AL PRINCIPIO DE LA FILA", "EL QUE FALTA ES UN NÚMERO REDONDO.", "?, 41, 42: ES EL 40"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [FB("COMPLETÁ EL TREN: 25, 26, ___, 28, ___, 30", [["27"], ["29"]], "DESPUÉS DEL 26 VA EL 27 Y DESPUÉS DEL 28 VA EL 29.", **A),
      N("[[problema]] TOMI TIENE LA FIGURITA 19 Y LE DAN LA QUE SIGUE. ¿QUÉ NÚMERO TIENE LA NUEVA?", 20, "DESPUÉS DEL 19 VIENE EL 20.", **A),
      MC("¿CON QUÉ NÚMERO EMPIEZAN LOS DEL VEINTE?", ["1", "2", "3"], "2", "20, 21, 22… EMPIEZAN CON 2.", **RE),
      ORD("ORDENÁ LAS FIGURITAS DE MENOR A MAYOR.", ["27", "21", "30", "24"], ["21", "24", "27", "30"], "21, 24, 27 Y 30: EN ORDEN.", **A)],
"2": [CLAS("¿EN QUÉ FILA DEL CUADRO VA CADA FIGURITA?", ["34", "41", "38", "46"], ["FILA DEL 30", "FILA DEL 40"],
           {"34": "FILA DEL 30", "41": "FILA DEL 40", "38": "FILA DEL 30", "46": "FILA DEL 40"}, "34 Y 38 EMPIEZAN CON 3; 41 Y 46 EMPIEZAN CON 4.", **A),
      MC("MIRÁ LA COLUMNA: 7, 17, 27, 37… ¿QUÉ NÚMERO SIGUE ABAJO?", ["38", "47", "40"], "47", "EN LA COLUMNA TODOS TERMINAN EN 7.", **A),
      MC("LEO DICE QUE EL 43 ESTÁ EN LA FILA DEL 30. ¿EN QUÉ FILA ESTÁ DE VERDAD?", ["LA DEL 40", "LA DEL 30", "LA DEL 3"], "LA DEL 40", "43 EMPIEZA CON 4: ESTÁ EN LA FILA DEL 40.", **ER),
      N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 39?", 40, "DESPUÉS DEL 39 VIENE EL 40.", **A)],
"3": [N("¿CUÁL ES EL ANTERIOR DEL 33?", 32, "ANTES DEL 33 VA EL 32.", **A),
      UNIR("UNÍ CADA NÚMERO CON SU SIGUIENTE.", ["32", "35", "38"], ["39", "33", "36"], {"32": "33", "35": "36", "38": "39"}, "EL SIGUIENTE ES EL QUE VA JUSTO DESPUÉS: 33, 36 Y 39.", **A),
      MC("SOFI DICE QUE EL SIGUIENTE DEL 29 ES EL 210. ¿CUÁL ES DE VERDAD?", ["30", "210", "20"], "30", "DESPUÉS DE UN 9 VIENE UN REDONDO: 30.", **ER),
      N("[[problema]] EN LA FILA PARA ENTRAR, ANA TIENE EL TURNO 41. ¿QUÉ TURNO TIENE EL QUE ESTÁ JUSTO ANTES?", 40, "EL ANTERIOR DEL 41 ES EL 40.", **AN)],
"4": [FB("COMPLETÁ: 46, 47, ___, 49, ___", [["48"], ["50"]], "47, 48, 49 Y DESPUÉS 50.", **A),
      N("¿QUÉ NÚMERO FALTA? 18, 19, ___, 21", 20, "DESPUÉS DEL 19 VIENE EL 20.", **A),
      MC("PARA SABER QUÉ FALTA EN 33, ___, 35, ¿QUÉ CONVIENE HACER?", ["DECIR EL 33 Y SEGUIR", "EMPEZAR DESDE EL 1", "ADIVINAR"], "DECIR EL 33 Y SEGUIR", "DECÍS EL DE ANTES Y SEGUÍS: 33, 34.", **AN),
      MC("JUAN COMPLETÓ ASÍ: 37, 38, 40. ¿QUÉ NÚMERO SE SALTEÓ?", ["39", "36", "41"], "39", "DESPUÉS DEL 38 VA EL 39.", **ER)],
"5": [N("RELÁMPAGO. ¿QUÉ SIGUE DESPUÉS DEL 49?", 50, "49, 50.", tiempo=30, **A),
      N("RELÁMPAGO. ¿CUÁL ES EL ANTERIOR DEL 40?", 39, "39, 40.", tiempo=30, **A),
      N("RELÁMPAGO. ¿QUÉ FALTA? 36, ___, 38", 37, "36, 37, 38.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿CON QUÉ EMPIEZAN LOS DEL TREINTA?", ["3", "2"], "3", "30, 31, 32…", tiempo=30, **RE)],
}
EXAMEN = [
 [1, N("¿QUÉ NÚMERO VIENE DESPUÉS DEL 19?", 20, "19, 20.", **A)],
 [1, FB("COMPLETÁ: 27, 28, ___, 30", [["29"]], "28, 29, 30.", **A)],
 [1, MC("¿CUÁNTOS NÚMEROS HAY EN CADA FILA DEL ÁLBUM?", ["5", "10", "20"], "10", "CADA FILA TIENE 10.", **RE)],
 [2, MC("¿CON QUÉ NÚMERO EMPIEZAN LOS DEL CUARENTA?", ["4", "5", "3"], "4", "41, 42, 43…", **RE)],
 [2, MC("EN UNA COLUMNA ESTÁN EL 2, EL 12, EL 22 Y EL 32. ¿QUÉ NÚMERO SIGUE?", ["42", "33", "23"], "42", "TODOS TERMINAN EN 2.", **A)],
 [2, CLAS("¿EN QUÉ FILA VA CADA NÚMERO?", ["25", "31", "29", "36"], ["FILA DEL 20", "FILA DEL 30"],
          {"25": "FILA DEL 20", "31": "FILA DEL 30", "29": "FILA DEL 20", "36": "FILA DEL 30"}, "25 Y 29 EMPIEZAN CON 2; 31 Y 36 CON 3.", **A)],
 [3, N("¿CUÁL ES EL ANTERIOR DEL 27?", 26, "26 VA ANTES DEL 27.", **A)],
 [3, N("¿CUÁL ES EL SIGUIENTE DEL 45?", 46, "46 VA DESPUÉS DEL 45.", **A)],
 [3, MC("MICA DICE QUE DESPUÉS DEL 39 VIENE EL 310. ¿QUÉ NÚMERO VIENE DE VERDAD?", ["40", "310", "30"], "40", "DESPUÉS DE UN 9 VIENE UN REDONDO.", **ER)],
 [4, N("¿QUÉ NÚMERO FALTA? 43, ___, 45", 44, "43, 44, 45.", **A)],
 [4, ORD("ORDENÁ DE MENOR A MAYOR.", ["38", "42", "35", "40"], ["35", "38", "40", "42"], "35, 38, 40 Y 42.", **A)],
 [4, MC("EN EL TREN 28, 29, ___, 31 FALTA UN VAGÓN. ¿CUÁL ES?", ["30", "210", "32"], "30", "DESPUÉS DEL 29 VIENE EL 30.", **A)],
 [4, MC("TOMI ESCRIBIÓ 47, 48, 50. ¿QUÉ NÚMERO SE OLVIDÓ?", ["49", "46", "51"], "49", "DESPUÉS DEL 48 VA EL 49.", **ER)],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 3, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: la serie numérica hasta 50", "examen_titulo": "Nivel jefe: la serie numérica hasta 50",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
