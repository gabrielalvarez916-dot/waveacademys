# -*- coding: utf-8 -*-
"""Lengua 1 (Nivel Medio, 1.º año) · Misión 3 · Letras M y P. Genera mision-3.json.
Regla de primeros años. Metáfora: la familia de Sofi (MAMÁ y PAPÁ) y sus cosas (MAPA, PIPA, PUMA…).
Niveles: 1 conocer la M y la P · 2 leer sílabas con M y P · 3 leer palabras con M y P · 4 escribir palabras con M y P."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
SA = lambda p, acepta, e, **k: {"t": "short_answer", "p": p, "o": {}, "r": {"acepta": acepta}, "e": e, **k}
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a conocer la letra M y la letra P.",
"vas_a_ver": ["La M de MAMÁ", "La P de PAPÁ", "Cómo suenan"],
"secciones": [
 S(1, "La M", [
  P("<b>M</b> de <b>MAMÁ</b>. Suena con la boca cerrada: mmm."),
  IMG("Palabras con M", "La M en rojo.", FG.dibujo_palabra([("manzana", "MANZANA"), ("chico", "MATEO")], "M")),
 ]),
 S(1, "La P", [
  D("Consonante", "Una letra que necesita una <b>vocal</b> para sonar. La M y la P son consonantes."),
  P("<b>P</b> de <b>PAPÁ</b>. Suena como un globo que explota: p."),
  IMG("Palabras con P", "La P en rojo.", FG.dibujo_palabra([("pelota", "PELOTA"), ("chico", "PAPÁ")], "P")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "¿Con qué letra empiezan?", FG.nombres(["MESA", "PATO", "MONO"], True, 3)),
 ]),
],
"ejemplo_completo": {"titulo": "MAMÁ", "planteo": "¿Cuántas M tiene MAMÁ?", "pasos": ["M-A-M-Á.", "Hay una M al principio.", "Y otra en el medio: tiene 2."]},
"ejemplo_incompleto": {"titulo": "PAPÁ", "planteo": "Completá.", "pasos": ["PAPÁ tiene ___ letras P."]},
"ejemplo_solo": {"titulo": "Tu casa", "planteo": "Pensá algo de tu casa que empiece con P."},
"tip": {"titulo": "Sentí la boca", "texto": "Para la M y la P, los labios se juntan."},
"ojo": ["La M y la P no son vocales.", "No confundas la P con la B."],
"resumen": [{"titulo": "M", "texto": "De MAMÁ."}, {"titulo": "P", "texto": "De PAPÁ."}, {"titulo": "Consonantes", "texto": "Necesitan vocales."}],
"glosario": [{"palabra": "Consonante", "significado": "Letra que no es vocal."}, {"palabra": "Labios", "significado": "Los bordes de la boca."}],
"carpeta": ["¿Con qué letra empieza MESA?", "¿Con qué letra empieza PATO?", "¿Con qué letra empieza MONO?"],
"respuestas_carpeta": [["M", "m"], ["P", "p"], ["M", "m"]],
"soluciones": {"incompleto": "2.", "solo": "Por ejemplo: PUERTA, PLATO.", "carpeta": ["M.", "P.", "M."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a leer sílabas con M y con P.",
"vas_a_ver": ["La M con cada vocal", "La P con cada vocal", "Leer de a dos"],
"secciones": [
 S(1, "La M con las vocales", [
  P("M con A dice <b>MA</b>. Así con todas: <b>MA, ME, MI, MO, MU</b>."),
  IMG("Sílabas con M", "MA, ME, MI, MO, MU.", FG.nombres(["MA", "ME", "MI", "MO", "MU"], cols=5)),
 ]),
 S(1, "La P con las vocales", [
  D("Sílaba", "Un pedacito de palabra que se dice <b>de un golpe</b>."),
  P("<b>PA, PE, PI, PO, PU</b>."),
  IMG("Sílabas con P", "PA, PE, PI, PO, PU.", FG.nombres(["PA", "PE", "PI", "PO", "PU"], cols=5)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las sílabas. Las vas a usar en la carpeta."),
  IMG("Sílabas", "Leelas en voz alta.", FG.nombres(["MI", "PO", "MU"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "PE", "planteo": "¿Cómo se lee P con E?", "pasos": ["Digo la P: p.", "Digo la E: e.", "Juntas: PE."]},
"ejemplo_incompleto": {"titulo": "MO", "planteo": "Completá.", "pasos": ["M con O dice ___ ."]},
"ejemplo_solo": {"titulo": "Tu sílaba", "planteo": "Elegí una vocal y juntala con la P. ¿Qué dice?"},
"tip": {"titulo": "De un golpe", "texto": "Leé la consonante y la vocal juntas, sin parar."},
"ojo": ["MA no es M y A separadas.", "Primero va la M o la P, después la vocal."],
"resumen": [{"titulo": "Sílaba", "texto": "De un golpe."}, {"titulo": "Con M", "texto": "MA, ME, MI, MO, MU."}, {"titulo": "Con P", "texto": "PA, PE, PI, PO, PU."}],
"glosario": [{"palabra": "Sílaba", "significado": "Pedacito de palabra."}, {"palabra": "Juntar", "significado": "Decir todo junto."}],
"carpeta": ["¿Con qué letra empieza MI?", "¿Qué vocal tiene PO?", "¿Cómo se escribe M con U?"],
"respuestas_carpeta": [["M", "m"], ["O", "o"], ["MU", "mu", "Mu"]],
"soluciones": {"incompleto": "MO.", "solo": "Por ejemplo: PA, PE.", "carpeta": ["M.", "O.", "MU."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a leer palabras con M y con P.",
"vas_a_ver": ["Juntar sílabas", "Leer palabras", "Palabras de la familia"],
"secciones": [
 S(1, "Juntar sílabas", [
  P("<b>MA</b> y <b>PA</b> forman <b>MAPA</b>. <b>PU</b> y <b>MA</b> forman <b>PUMA</b>."),
  IMG("Palabras", "Sílaba por sílaba.", FG.nombres(["MAPA", "PUMA", "PIPA"], cols=3)),
 ]),
 S(1, "Leer palabras", [
  D("Leer una palabra", "Leer cada sílaba y después <b>todo junto</b>."),
  P("PE-PE: <b>PEPE</b>. MI-MO: <b>MIMO</b>."),
  IMG("Más palabras", "PEPE y MIMO.", FG.nombres(["PEPE", "MIMO", "PAPÁ"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras", "Leelas en voz alta.", FG.nombres(["MAMÁ", "PUMA", "MAPA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "PIPA", "planteo": "Leemos PIPA.", "pasos": ["PI.", "PA.", "Todo junto: PIPA."]},
"ejemplo_incompleto": {"titulo": "MAPA", "planteo": "Completá.", "pasos": ["MA + ___ = MAPA."]},
"ejemplo_solo": {"titulo": "Leé", "planteo": "Leé en voz alta: MAMÁ MIMA A PEPE."},
"tip": {"titulo": "Sílaba por sílaba", "texto": "Si una palabra es difícil, leela de a pedacitos."},
"ojo": ["Leé las sílabas en orden.", "Al final, decí todo junto."],
"resumen": [{"titulo": "Sílabas", "texto": "MA + PA."}, {"titulo": "Juntar", "texto": "MAPA."}, {"titulo": "Leer", "texto": "Todo junto."}],
"glosario": [{"palabra": "Mapa", "significado": "Dibujo de un lugar."}, {"palabra": "Puma", "significado": "Un animal salvaje."}],
"carpeta": ["¿Qué palabra está primero?", "¿Con qué sílaba empieza PUMA?", "¿Con qué sílaba termina MAPA?"],
"respuestas_carpeta": [["MAMÁ", "MAMA", "mamá", "mama"], ["PU", "pu"], ["PA", "pa"]],
"soluciones": {"incompleto": "PA.", "solo": "MAMÁ MIMA A PEPE.", "carpeta": ["MAMÁ.", "PU.", "PA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con M y con P.",
"vas_a_ver": ["Escuchar las sílabas", "Escribir cada sílaba", "Revisar la palabra"],
"secciones": [
 S(1, "Escuchar y escribir", [
  P("Decimos <b>PU-MA</b>. Escribimos <b>PU</b> y después <b>MA</b>."),
  IMG("PUMA", "P, U, M, A.", FG.letras("PUMA", numeros=True)),
 ]),
 S(1, "Revisar", [
  D("Revisar", "Leer lo que escribiste para ver si está bien."),
  P("Escribimos MAPA. Leemos: MA-PA. ¡Está bien!"),
  IMG("Falta una letra", "MA_A: falta la P.", FG.letras("MAPA", ocultar=(2,), numeros=True)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la palabra. La vas a usar en la carpeta."),
  IMG("Completá", "PIPA con huecos.", FG.letras("PIPA", ocultar=(0, 2), numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "MIMO", "planteo": "Escribimos MIMO.", "pasos": ["Digo: MI-MO.", "Escribo MI.", "Escribo MO: MIMO."]},
"ejemplo_incompleto": {"titulo": "PEPE", "planteo": "Completá.", "pasos": ["P _ P _ ."]},
"ejemplo_solo": {"titulo": "Tu palabra", "planteo": "Escribí una palabra con M y P. Leela para revisar."},
"tip": {"titulo": "Decila mientras escribís", "texto": "Decí cada sílaba mientras la escribís."},
"ojo": ["No te comas letras.", "Revisá leyendo despacio."],
"resumen": [{"titulo": "Escuchar", "texto": "PU-MA."}, {"titulo": "Escribir", "texto": "Sílaba por sílaba."}, {"titulo": "Revisar", "texto": "Leer lo escrito."}],
"glosario": [{"palabra": "Revisar", "significado": "Mirar otra vez."}, {"palabra": "Escribir", "significado": "Poner letras."}],
"carpeta": ["¿Qué letra va en el lugar 1?", "¿Qué letra va en el lugar 3?", "¿Qué palabra se forma?"],
"respuestas_carpeta": [["P", "p"], ["P", "p"], ["PIPA", "pipa", "Pipa"]],
"soluciones": {"incompleto": "PEPE.", "solo": "Por ejemplo: MAPA.", "carpeta": ["P.", "P.", "PIPA."]},
}

ACT = {
"1": [MC("¿QUÉ PALABRA EMPIEZA CON M?", ["MESA", "PATO", "OSO"], "MESA", "M DE MESA."),
      MC("¿QUÉ PALABRA EMPIEZA CON P?", ["MONO", "PELOTA", "UVA"], "PELOTA", "P DE PELOTA.")],
"2": [MC("¿CÓMO SE LEE M CON A?", ["MA", "AM", "PA"], "MA", "PRIMERO LA M, DESPUÉS LA A."),
      SA("ESCRIBÍ P CON O.", ["PO", "po", "Po"], "P Y O: PO.")],
"3": [MC("¿QUÉ PALABRA FORMAN MA Y PA?", ["MAPA", "PAMA", "PAPA"], "MAPA", "MA-PA."),
      MC("¿CON QUÉ SÍLABA EMPIEZA PUMA?", ["PU", "MA", "PA"], "PU", "PU-MA.")],
"4": [ORD("ORDENÁ LAS SÍLABAS DE MAPA.", ["PA", "MA"], ["MA", "PA"], "MA-PA."),
      SA("¿QUÉ LETRA FALTA? MA_A", ["P", "p"], "MAPA.")],
"5": [MC("RELÁMPAGO. ¿CUÁL ES LA M?", ["M", "P", "A"], "M", "M DE MAMÁ.", tiempo=30),
      MC("RELÁMPAGO. ¿CÓMO SE LEE P CON I?", ["PI", "IP", "MI"], "PI", "P Y I.", tiempo=30),
      MC("RELÁMPAGO. ¿QUÉ PALABRA ES?  PI-PA", ["PIPA", "PAPI", "MIMO"], "PIPA", "PI-PA.", tiempo=30),
      SA("RELÁMPAGO. ¿QUÉ LETRA FALTA? _UMA", ["P", "p"], "PUMA.", tiempo=30)],
}
EXAMEN = [
 [1, MC("¿CON QUÉ LETRA EMPIEZA MAMÁ?", ["M", "P", "A"], "M", "M DE MAMÁ.")],
 [1, MC("¿CON QUÉ LETRA EMPIEZA PAPÁ?", ["P", "M", "B"], "P", "P DE PAPÁ.")],
 [1, MC("LA M Y LA P SON…", ["CONSONANTES", "VOCALES", "NÚMEROS"], "CONSONANTES", "NECESITAN UNA VOCAL.")],
 [2, MC("¿CÓMO SE LEE M CON E?", ["ME", "EM", "MI"], "ME", "M Y E: ME.")],
 [2, SA("ESCRIBÍ P CON A.", ["PA", "pa", "Pa"], "P Y A: PA.")],
 [2, MC("¿CUÁL ES UNA SÍLABA CON P?", ["PU", "MU", "UM"], "PU", "P Y U.")],
 [3, MC("¿QUÉ PALABRA FORMAN PU Y MA?", ["PUMA", "MAPU", "MAMA"], "PUMA", "PU-MA.")],
 [3, MC("¿QUÉ PALABRA DICE MI-MO?", ["MIMO", "MOMI", "PIPO"], "MIMO", "MI-MO.")],
 [3, MC("¿CON QUÉ SÍLABA TERMINA PIPA?", ["PA", "PI", "MA"], "PA", "PI-PA.")],
 [4, ORD("ORDENÁ LAS SÍLABAS DE PUMA.", ["MA", "PU"], ["PU", "MA"], "PU-MA.")],
 [4, SA("¿QUÉ LETRA FALTA? PE_E", ["P", "p"], "PEPE.")],
 [4, SA("¿QUÉ LETRA FALTA? _IMO", ["M", "m"], "MIMO.")],
 [4, MC("DESPUÉS DE ESCRIBIR, HAY QUE…", ["REVISAR LEYENDO", "BORRAR TODO", "NADA"], "REVISAR LEYENDO", "ASÍ VEMOS SI ESTÁ BIEN.")],
]
M = {"subject_id": "eee219b3-9188-4e94-be06-223054ed5a57", "tema": 3, "estilo": "primeros",
     "practica": "Práctica general: letras M y P", "examen_titulo": "Nivel jefe: letras M y P",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
