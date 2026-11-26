# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 10 · Sumas y complementos a 10. Genera mision-10.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: los bolos de Sofi (10 bolos: los que caen y los que quedan parados).
Niveles: 1 las sumas que dan 10 · 2 complementos a 10 · 3 sumas hasta 10 de memoria · 4 juegos de sumas. Dibujo central: el cuadro de 10."""
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
"objetivo": "Vas a encontrar las sumas que dan 10.",
"vas_a_ver": ["El cuadro de 10", "Dos colores que llenan el cuadro", "Muchas sumas dan 10"],
"secciones": [
 S(1, "El cuadro de 10", [
  P("Sofi juega a los bolos. Hay <b>10</b> bolos."),
  P("El cuadro de 10 tiene <b>10</b> lugares: dos filas de 5."),
  IMG("6 y 4", "6 + 4 = 10.", FG.marco10(6, "pelota", "estrella", 4, "6 + 4 = 10")),
 ]),
 S(1, "Muchas sumas dan 10", [
  D("Sumas que dan 10", "Dos números que juntos llenan el cuadro de 10."),
  IMG("7 y 3", "7 + 3 = 10.", FG.marco10(7, "manzana", "pelota", 3, "7 + 3 = 10")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro de 10", "Contá cada color.", FG.marco10(8, "estrella", "manzana", 2, "8 + ? = 10")),
 ]),
],
"ejemplo_completo": {"titulo": "5 y 5", "planteo": "5 pelotas y 5 estrellas.", "pasos": ["Una fila de pelotas.", "Una fila de estrellas.", "5 + 5 = 10."]},
"ejemplo_incompleto": {"titulo": "9 y 1", "planteo": "Completá.", "pasos": ["9 + 1 = ___ ."]},
"ejemplo_solo": {"titulo": "Tus dedos", "planteo": "Levantá 4 dedos. ¿Cuántos dedos quedan bajos?"},
"tip": {"titulo": "Tus manos", "texto": "Tenés 10 dedos. ¡Usalos para sumar hasta 10!"},
"ojo": ["El cuadro tiene 10 lugares.", "Contá los dos colores."],
"resumen": [{"titulo": "Cuadro", "texto": "10 lugares."}, {"titulo": "Dos colores", "texto": "Llenan el cuadro."}, {"titulo": "Sumas", "texto": "Dan 10."}],
"glosario": [{"palabra": "Cuadro de 10", "significado": "Dos filas de 5."}, {"palabra": "Diez", "significado": "Los dedos de tus manos."}],
"carpeta": ["¿Cuántas estrellas hay?", "¿Cuántas manzanas hay?", "¿Cuánto es 8 + 2?"],
"respuestas_carpeta": [["8"], ["2"], ["10"]],
"soluciones": {"incompleto": "10.", "solo": "6 dedos.", "carpeta": ["8.", "2.", "10."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver cuánto falta para llegar a 10.",
"vas_a_ver": ["Lugares vacíos", "Cuánto falta para 10", "El amigo del 10"],
"secciones": [
 S(1, "Lugares vacíos", [
  P("Sofi tira la bola. Caen <b>7</b> bolos."),
  P("¿Cuántos quedan parados? Mirá los lugares vacíos."),
  IMG("Faltan 3", "7 + 3 = 10.", FG.marco10(7, "manzana", texto="FALTAN 3")),
 ]),
 S(1, "El amigo del 10", [
  D("Complemento a 10", "Lo que le falta a un número para llegar a <b>10</b>."),
  P("El amigo del <b>6</b> es el <b>4</b>. El amigo del <b>8</b> es el <b>2</b>."),
  IMG("Faltan 4", "6 + 4 = 10.", FG.marco10(6, "pelota", texto="FALTAN 4")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro de 10", "Contá los vacíos.", FG.marco10(5, "estrella", texto="¿CUÁNTOS FALTAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "El 9", "planteo": "¿Cuánto le falta al 9 para 10?", "pasos": ["Ponemos 9 en el cuadro.", "Queda 1 lugar vacío.", "Le falta 1: 9 + 1 = 10."]},
"ejemplo_incompleto": {"titulo": "El 3", "planteo": "Completá.", "pasos": ["3 + ___ = 10."]},
"ejemplo_solo": {"titulo": "Bolos", "planteo": "Caen 2 bolos. ¿Cuántos quedan parados?"},
"tip": {"titulo": "Contá los vacíos", "texto": "Los lugares vacíos son lo que falta."},
"ojo": ["Contá los vacíos, no los llenos.", "Los dos números suman 10."],
"resumen": [{"titulo": "Vacíos", "texto": "Lo que falta."}, {"titulo": "Amigo del 10", "texto": "Completa el 10."}, {"titulo": "Ejemplo", "texto": "7 y 3."}],
"glosario": [{"palabra": "Faltar", "significado": "No estar todavía."}, {"palabra": "Complemento", "significado": "Lo que falta para 10."}],
"carpeta": ["¿Cuántas estrellas hay?", "¿Cuántos lugares vacíos hay?", "¿Cuánto le falta al 5 para llegar a 10?"],
"respuestas_carpeta": [["5"], ["5"], ["5"]],
"soluciones": {"incompleto": "7.", "solo": "8 bolos.", "carpeta": ["5.", "5.", "5."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a aprender de memoria las sumas que dan 10.",
"vas_a_ver": ["Las parejas del 10", "Pensar sin contar", "Sumas rápidas"],
"secciones": [
 S(1, "Las parejas del 10", [
  P("<b>1 + 9</b>, <b>2 + 8</b>, <b>3 + 7</b>, <b>4 + 6</b>, <b>5 + 5</b>."),
  P("¡Todas dan <b>10</b>!"),
  IMG("4 y 6", "4 + 6 = 10.", FG.marco10(4, "pelota", "manzana", 6, "4 + 6 = 10")),
 ]),
 S(1, "De memoria", [
  D("De memoria", "Saber la respuesta sin contar. ¡Se aprende practicando!"),
  P("Si sabés que <b>3 + 7 = 10</b>, también sabés <b>7 + 3 = 10</b>."),
  IMG("3 y 7", "3 + 7 = 10.", FG.marco10(3, "estrella", "pelota", 7, "3 + 7 = 10")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro de 10", "Contá cada grupo.", FG.marco10(1, "manzana", "estrella", 9, "1 + 9 = ?")),
 ]),
],
"ejemplo_completo": {"titulo": "2 + 8", "planteo": "¿Cuánto es 2 + 8?", "pasos": ["Es una pareja del 10.", "2 + 8 = 10."]},
"ejemplo_incompleto": {"titulo": "Parejas", "planteo": "Completá.", "pasos": ["5 + ___ = 10.", "8 + ___ = 10."]},
"ejemplo_solo": {"titulo": "Decilo rápido", "planteo": "¿Cuánto es 6 + 4?"},
"tip": {"titulo": "Dalo vuelta", "texto": "3 + 7 y 7 + 3 dan lo mismo."},
"ojo": ["Si los números se dan vuelta, el resultado no cambia.", "5 + 5 también da 10."],
"resumen": [{"titulo": "Parejas", "texto": "1 y 9, 2 y 8…"}, {"titulo": "Memoria", "texto": "Sin contar."}, {"titulo": "Vuelta", "texto": "3 + 7 = 7 + 3."}],
"glosario": [{"palabra": "De memoria", "significado": "Sin contar."}, {"palabra": "Pareja", "significado": "Dos números que dan 10."}],
"carpeta": ["¿Cuántas manzanas hay?", "¿Cuántas estrellas hay?", "¿Cuánto es 1 + 9?"],
"respuestas_carpeta": [["1"], ["9"], ["10"]],
"soluciones": {"incompleto": "5. 2.", "solo": "10.", "carpeta": ["1.", "9.", "10."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a jugar con sumas hasta 10.",
"vas_a_ver": ["El juego de los bolos", "Sumas con dados", "Sumas que no llegan a 10"],
"secciones": [
 S(1, "Los bolos", [
  P("Sofi tira dos veces. Primero caen <b>4</b> bolos. Después caen <b>3</b>."),
  P("<b>4 + 3 = 7</b>. Cayeron 7 bolos."),
  IMG("4 y 3", "4 + 3 = 7.", FG.marco10(4, "pelota", "estrella", 3, "4 + 3 = 7")),
 ]),
 S(1, "Los dados", [
  D("Juego de dados", "Tirás dos dados y sumás los puntos."),
  P("Sale <b>5</b> y sale <b>2</b>: <b>5 + 2 = 7</b>."),
  IMG("5 y 2", "5 + 2 = 7.", FG.marco10(5, "manzana", "pelota", 2, "5 + 2 = 7")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro de 10", "Contá cada grupo.", FG.marco10(3, "estrella", "manzana", 5, "3 + 5 = ?")),
 ]),
],
"ejemplo_completo": {"titulo": "Dados", "planteo": "Sale 3 y sale 3.", "pasos": ["3 + 3.", "Contamos: 4, 5, 6.", "3 + 3 = 6."]},
"ejemplo_incompleto": {"titulo": "Bolos", "planteo": "Completá.", "pasos": ["Caen 2 y después 6.", "2 + 6 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu juego", "planteo": "Inventá una suma que dé 9."},
"tip": {"titulo": "Empezá por el grande", "texto": "En 2 + 6, empezá en 6 y seguí: 7, 8."},
"ojo": ["No todas las sumas dan 10.", "Contá desde el número más grande."],
"resumen": [{"titulo": "Bolos", "texto": "Sumamos los que caen."}, {"titulo": "Dados", "texto": "Sumamos los puntos."}, {"titulo": "Truco", "texto": "Empezar por el grande."}],
"glosario": [{"palabra": "Dado", "significado": "Cubo con puntos del 1 al 6."}, {"palabra": "Tirar", "significado": "Jugar una vez."}],
"carpeta": ["¿Cuántas estrellas hay?", "¿Cuántas manzanas hay?", "¿Cuánto es 3 + 5?"],
"respuestas_carpeta": [["3"], ["5"], ["8"]],
"soluciones": {"incompleto": "8.", "solo": "Por ejemplo, 5 + 4 = 9.", "carpeta": ["3.", "5.", "8."]},
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
 T("EL CUADRO DE 10", [LD("DIEZ LUGARES", "EL <b>CUADRO DE 10</b> TIENE DOS FILAS DE 5: DIEZ LUGARES."),
   LL("SI ESTÁ LLENO, HAY 10.", "PODEMOS LLENARLO CON DOS COLORES.")],
   {"modo": "diez", "que": "cuadro"}, {"modo": "diez", "que": "cuadro"}),
 T("MUCHAS SUMAS DAN 10", [LD("DOS COLORES", "SI DOS COLORES LLENAN EL CUADRO, SU SUMA <b>DA 10</b>."),
   LL("7 ROJOS Y 3 AZULES: 7 + 3 = 10.", "6 + 4 Y 8 + 2 TAMBIÉN DAN 10.")],
   {"modo": "diez", "que": "cuadro"}, {"modo": "diez", "que": "parejas"}),
], "recuerda": [
 RC("EL CUADRO DE 10", "TIENE DOS FILAS DE CINCO LUGARES.", "LLENO SON 10"),
 RC("SUMAS QUE DAN 10", "SON LAS QUE LLENAN EL CUADRO CON DOS COLORES.", "6 + 4 = 10"),
]}

N2["leccion"] = {"temas": [
 T("LUGARES VACÍOS", [LD("LO QUE FALTA", "LOS LUGARES <b>VACÍOS</b> DEL CUADRO DICEN CUÁNTO FALTA PARA 10."),
   LL("HAY 6: QUEDAN 4 VACÍOS.", "AL 6 LE FALTAN 4.")],
   {"modo": "diez", "que": "falta"}, {"modo": "diez", "que": "falta"}),
 T("EL AMIGO DEL 10", [LD("AMIGOS", "EL <b>AMIGO DEL 10</b> DE UN NÚMERO ES LO QUE LE FALTA PARA LLEGAR A 10."),
   LL("EL AMIGO DEL 7 ES EL 3.", "EL AMIGO DEL 5 ES EL 5.")],
   {"modo": "diez", "que": "falta"}, {"modo": "diez", "que": "cuadro"}),
], "recuerda": [
 RC("LO QUE FALTA", "SE VE CONTANDO LOS LUGARES VACÍOS DEL CUADRO.", "AL 6 LE FALTAN 4"),
 RC("EL AMIGO DEL 10", "ES EL NÚMERO QUE COMPLETA HASTA 10.", "EL AMIGO DEL 8 ES 2"),
]}

N3["leccion"] = {"temas": [
 T("LAS PAREJAS DEL 10", [LD("PAREJAS", "LAS <b>PAREJAS DEL 10</b> SON 1 + 9, 2 + 8, 3 + 7, 4 + 6 Y 5 + 5."),
   LL("SI LAS DAMOS VUELTA, SIGUEN DANDO 10.", "9 + 1 TAMBIÉN ES 10.")],
   {"modo": "diez", "que": "parejas"}, {"modo": "diez", "que": "parejas"}),
 T("PENSAR SIN CONTAR", [LD("DE MEMORIA", "CUANDO LAS SABEMOS <b>DE MEMORIA</b>, CONTESTAMOS RÁPIDO SIN CONTAR."),
   LL("3 + ___ = 10: ES 7.", "PRACTICÁ HASTA QUE SALGA SOLO.")],
   {"modo": "diez", "que": "parejas"}, {"modo": "diez", "que": "cuadro"}),
], "recuerda": [
 RC("PAREJAS DEL 10", "SON LAS SUMAS DE DOS NÚMEROS QUE DAN 10.", "2 + 8 Y 4 + 6"),
 RC("DAR VUELTA", "CAMBIAR EL ORDEN NO CAMBIA EL RESULTADO.", "3 + 7 = 7 + 3 = 10"),
]}

N4["leccion"] = {"temas": [
 T("SUMAS CON DADOS", [LD("EL MÁS GRANDE", "PARA SUMAR DOS DADOS, EMPEZÁ POR EL <b>MÁS GRANDE</b> Y SEGUÍ CONTANDO."),
   LL("5 Y 2: 5… 6, 7.", "ASÍ CONTÁS MENOS.")],
   {"modo": "diez", "que": "dados"}, {"modo": "diez", "que": "dados"}),
 T("SUMAS QUE NO LLEGAN A 10", [LD("MENOS DE 10", "NO TODAS LAS SUMAS DAN 10: ALGUNAS <b>NO LLEGAN</b>."),
   LL("3 + 5 = 8: FALTAN 2 PARA 10.", "EN EL CUADRO QUEDAN LUGARES VACÍOS.")],
   {"modo": "sumar", "que": "cuenta"}, {"modo": "sumar", "que": "cuenta"}),
], "recuerda": [
 RC("CON DADOS", "EMPEZAMOS POR EL MÁS GRANDE Y SEGUIMOS CONTANDO.", "6 Y 3: 7, 8, 9"),
 RC("NO LLEGAN A 10", "SI QUEDAN LUGARES VACÍOS, LA SUMA ES MENOS DE 10.", "4 + 4 = 8"),
]}

# ---------- ACTIVIDADES (4 por nivel + 4 generales) y EXAMEN, con su nivel "n" ----------
ACT = {
"1": [N("¿CUÁNTO ES 6 + 4?", 10, "6 Y 4 LLENAN EL CUADRO DE 10.", **A),
      MC("¿QUÉ SUMA DA 10?", ["7 + 3", "5 + 3", "6 + 2"], "7 + 3", "7 Y 3 SON 10.", **A),
      CLAS("¿DA 10 O NO DA 10?", ["8 + 2", "4 + 5", "1 + 9", "3 + 3"], ["DA 10", "NO DA 10"],
           {"8 + 2": "DA 10", "4 + 5": "NO DA 10", "1 + 9": "DA 10", "3 + 3": "NO DA 10"}, "8 + 2 Y 1 + 9 LLENAN EL CUADRO.", **AN),
      MC("LEO DICE QUE 5 + 4 DA 10. ¿CUÁNTO DA DE VERDAD?", ["9", "10", "54"], "9", "5 Y 4 SON 9: FALTA 1 PARA 10.", **ER)],
"2": [N("CAEN 8 BOLOS DE 10. ¿CUÁNTOS QUEDAN PARADOS?", 2, "8 + 2 = 10.", **A),
      N("¿CUÁNTO LE FALTA AL 6 PARA LLEGAR A 10?", 4, "6 + 4 = 10.", **A),
      UNIR("UNÍ CADA NÚMERO CON SU AMIGO DEL 10.", ["7", "2", "5"], ["8", "5", "3"], {"7": "3", "2": "8", "5": "5"}, "7 + 3, 2 + 8 Y 5 + 5 DAN 10.", **A),
      N("[[problema]] SOFI QUIERE JUNTAR 10 FIGURITAS Y YA TIENE 3. ¿CUÁNTAS LE FALTAN?", 7, "3 + 7 = 10.", **AN)],
"3": [FB("COMPLETÁ: 5 + ___ = 10", [["5"]], "5 Y 5 SON 10.", **A),
      MC("SI 3 + 7 = 10, ENTONCES 7 + 3 ES…", ["10", "4", "37"], "10", "DAR VUELTA NO CAMBIA EL RESULTADO.", **A),
      UNIR("UNÍ CADA PAREJA DEL 10.", ["1 +", "4 +", "8 +"], ["2", "9", "6"], {"1 +": "9", "4 +": "6", "8 +": "2"}, "1 + 9, 4 + 6 Y 8 + 2.", **A),
      MC("TOMI DICE QUE 6 + 4 Y 4 + 6 DAN DISTINTO. ¿TIENE RAZÓN?", ["NO, LAS DOS DAN 10", "SÍ, DAN DISTINTO"], "NO, LAS DOS DAN 10", "DAR VUELTA NO CAMBIA EL RESULTADO.", **ER)],
"4": [N("SALE 4 EN UN DADO Y 2 EN EL OTRO. ¿CUÁNTO ES?", 6, "4… 5, 6.", **A),
      N("CAEN 5 BOLOS Y DESPUÉS 3. ¿CUÁNTOS CAYERON?", 8, "5… 6, 7, 8.", **A),
      MC("PARA SUMAR 2 + 6, ¿DESDE QUÉ NÚMERO CONVIENE EMPEZAR A CONTAR?", ["DESDE EL 6", "DESDE EL 2", "DESDE EL 1"], "DESDE EL 6", "EMPEZAMOS POR EL MÁS GRANDE: 7, 8.", **AN),
      CLAS("¿LLEGA A 10 O NO LLEGA?", ["3 + 5", "6 + 4", "2 + 2"], ["LLEGA A 10", "NO LLEGA"], {"3 + 5": "NO LLEGA", "6 + 4": "LLEGA A 10", "2 + 2": "NO LLEGA"}, "SOLO 6 + 4 LLENA EL CUADRO.", **A)],
"5": [N("RELÁMPAGO. ¿CUÁNTO ES 9 + 1?", 10, "9 Y 1 SON 10.", tiempo=30, **A),
      N("RELÁMPAGO. 2 + ___ = 10", 8, "2 Y 8 SON 10.", tiempo=30, **A),
      N("RELÁMPAGO. ¿CUÁNTO ES 3 + 4?", 7, "4… 5, 6, 7.", tiempo=30, **A),
      MC("RELÁMPAGO. ¿CUÁL ES EL AMIGO DEL 10 DEL 7?", ["3", "7", "10"], "3", "7 + 3 = 10.", tiempo=30, **RE)],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 8 + 2?", 10, "8 Y 2 SON 10.", **A)],
 [1, MC("¿CUÁNTOS LUGARES TIENE EL CUADRO DE 10?", ["5", "10", "2"], "10", "DOS FILAS DE 5.", **RE)],
 [1, MC("¿QUÉ SUMA DA 10?", ["4 + 6", "4 + 4", "3 + 5"], "4 + 6", "4 Y 6 SON 10.", **A)],
 [2, N("¿CUÁNTO LE FALTA AL 9 PARA LLEGAR A 10?", 1, "9 + 1 = 10.", **A)],
 [2, N("CAEN 3 BOLOS DE 10. ¿CUÁNTOS QUEDAN PARADOS?", 7, "3 + 7 = 10.", **A)],
 [2, N("[[problema]] EN EL CUADRO DE 10 HAY 4 ESTRELLAS. ¿CUÁNTOS LUGARES QUEDAN VACÍOS?", 6, "4 + 6 = 10.", **AN)],
 [3, FB("COMPLETÁ: 1 + ___ = 10", [["9"]], "1 Y 9 SON 10.", **A)],
 [3, N("¿CUÁNTO ES 5 + 5?", 10, "5 Y 5 SON 10.", **A)],
 [3, MC("SI 2 + 8 = 10, ENTONCES 8 + 2 ES…", ["6", "10", "28"], "10", "DAR VUELTA NO CAMBIA EL RESULTADO.", **A)],
 [4, N("SALE 6 EN UN DADO Y 3 EN EL OTRO. ¿CUÁNTO ES?", 9, "6… 7, 8, 9.", **A)],
 [4, N("¿CUÁNTO ES 2 + 5?", 7, "5… 6, 7.", **A)],
 [4, MC("JUAN SUMÓ 1 + 6 EMPEZANDO A CONTAR DESDE EL 1. ¿DESDE DÓNDE CONVENÍA EMPEZAR?", ["DESDE EL 6", "DESDE EL 1"], "DESDE EL 6", "EMPEZAMOS POR EL GRANDE: 7.", **ER)],
 [4, N("CAEN 4 BOLOS Y DESPUÉS 4. ¿CUÁNTOS CAYERON?", 8, "4… 5, 6, 7, 8.", **A)],
]

M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 10, "estilo": "primeros", "actualizar_preguntas": True,
     "practica": "Práctica general: sumas y complementos a 10", "examen_titulo": "Nivel jefe: sumas y complementos a 10",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-10.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
