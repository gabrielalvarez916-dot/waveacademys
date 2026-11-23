# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 15 · Ortografía: GUE, GUI, QUE y QUI. Genera mision-15.json.
Regla de primeros años y vía fonológica (la VOZ dice sonidos —que, qui, gue, gui, güe— y «la letra del medio no suena», nunca nombres de letras).
Metáfora: Sofi, detective de palabras (la letra escondida que no suena).
Niveles: 1 QUE y QUI · 2 GUE y GUI · 3 GÜE y GÜI · 4 dictado con las cuatro reglas."""
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
TF = lambda p, ok, e, **k: {"t": "true_false", "p": p, "o": ["VERDADERO", "FALSO"], "r": {"correcta": ok}, "e": e, **k}
UNI = lambda p, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": [a for a, _ in pares], "derecha": [b for _, b in pares]}, "r": {"pares": dict(pares)}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
low = lambda w: [w, w.lower(), w.capitalize()]
NO = ["NO", "no", "No"]

N1 = {**ESTILO,
"objetivo": "Vas a escribir palabras con QUE y QUI.",
"vas_a_ver": ["QUE y QUI", "La U que no suena", "Palabras con QUE y QUI"],
"secciones": [
 S(1, "Una letra escondida", [
  P("La detective Sofi encontró algo raro en <b>QUESO</b>."),
  D("QUE y QUI", "Se escriben con <b>U</b>, pero la U <b>no suena</b>."),
  IMG("QUESO", "La U no suena.", FG.letras("QUESO", resaltar=(1,))),
 ]),
 S(1, "Más palabras", [
  P("QUESO, QUINCE, PAQUETE, MOSQUITO, MÁQUINA."),
  IMG("Con QUE y QUI", "Siempre con U.", FG.nombres(["QUESO", "QUINCE", "PAQUETE", "MOSQUITO"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Qué falta?", "Pensá en la regla.", FG.nombres(["Q_ESO", "MOS_ITO", "PA_ETE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "QUINCE", "planteo": "¿Cómo se escribe QUINCE?", "pasos": ["Suena QUI.", "Se escribe Q, U, I.", "QUINCE."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí lo que falta.", "pasos": ["Q_ESO.", "PA_ _ETE."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Buscá en tu casa una palabra con QUE o QUI."},
"tip": {"titulo": "QUE y QUI", "texto": "Para ese sonido con E o I, va QU."},
"ojo": ["QESO está mal.", "Se escribe QUESO."],
"resumen": [{"titulo": "QUE · QUI", "texto": "Con U que no suena."}, {"titulo": "Ejemplos", "texto": "QUESO, QUINCE."}, {"titulo": "Ojo", "texto": "Nunca QE ni QI."}],
"glosario": [{"palabra": "Mosquito", "significado": "Insecto chiquito que pica."}, {"palabra": "Máquina", "significado": "Aparato que hace un trabajo."}],
"carpeta": ["¿Qué letra falta en Q_ESO?", "¿Qué falta en MOS_ITO?", "Tomi escribió PAQETE. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("U"), low("QU"), low("PAQUETE")],
"soluciones": {"incompleto": "U. QU.", "solo": "Por ejemplo: QUESO.", "carpeta": ["U.", "QU: MOSQUITO.", "PAQUETE."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a escribir palabras con GUE y GUI.",
"vas_a_ver": ["GA, GO, GU", "GUE y GUI", "La U que no suena"],
"secciones": [
 S(1, "GA, GO, GU", [
  P("En GATO, GOMA y GUSANO, la G suena suave."),
  P("Para que suene igual con E y con I, ponemos <b>U</b>."),
  IMG("GUE y GUI", "La U no suena.", FG.tiras(["GA · GUE · GUI · GO · GU"], numeros=False, cols=1)),
 ]),
 S(1, "Palabras con GUE y GUI", [
  P("GUITARRA, GUISO, MANGUERA, JUGUETE."),
  IMG("Con GUE y GUI", "La U escondida.", FG.nombres(["GUITARRA", "GUISO", "MANGUERA", "JUGUETE"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Qué falta?", "Pensá en la regla.", FG.nombres(["G_ITARRA", "JUG_ETE", "G_SANO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "GUISO", "planteo": "¿Cómo se escribe GUISO?", "pasos": ["Suena GUI.", "Se escribe G, U, I.", "GUISO."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí lo que falta.", "pasos": ["G_ITARRA.", "MANG_ERA."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Buscá un juguete y escribí su nombre."},
"tip": {"titulo": "Con E e I, U", "texto": "GUE y GUI llevan una U que no suena."},
"ojo": ["GITARRA está mal.", "Se escribe GUITARRA."],
"resumen": [{"titulo": "GA · GO · GU", "texto": "Sin U extra."}, {"titulo": "GUE · GUI", "texto": "Con U que no suena."}, {"titulo": "Ejemplos", "texto": "GUITARRA, JUGUETE."}],
"glosario": [{"palabra": "Manguera", "significado": "Tubo largo para regar."}, {"palabra": "Guiso", "significado": "Comida con caldo."}],
"carpeta": ["¿Qué letra falta en G_ITARRA?", "¿Qué letra falta en JUG_ETE?", "¿G_SANO lleva una U escondida o no?"],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"respuestas_carpeta": [low("U"), low("U"), low("NO") + low("GUSANO")],
"soluciones": {"incompleto": "U. U.", "solo": "El nombre de tu juguete.", "carpeta": ["U.", "U.", "No: GUSANO, la U suena."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir palabras con GÜE y GÜI.",
"vas_a_ver": ["Cuando la U sí suena", "La diéresis", "Palabras con GÜE y GÜI"],
"secciones": [
 S(1, "La U que sí suena", [
  P("En <b>PINGÜINO</b>, la U <b>sí suena</b>: pin-güi-no."),
  D("Diéresis", "Dos <b>puntitos</b> arriba de la U (Ü). Avisan: ¡esta U suena!"),
  IMG("PINGÜINO", "La Ü con sus puntitos.", FG.letras("PINGÜINO", resaltar=(4,))),
 ]),
 S(1, "Más palabras", [
  P("PINGÜINO, PARAGÜERO, CIGÜEÑA, AGÜITA."),
  IMG("Con GÜE y GÜI", "La U suena.", FG.nombres(["PINGÜINO", "CIGÜEÑA", "PARAGÜERO", "AGÜITA"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿U o Ü?", "Escuchá si suena.", FG.nombres(["PING_INO", "G_ISO", "CIG_EÑA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "CIGÜEÑA", "planteo": "¿La U suena en CIGÜEÑA?", "pasos": ["Digo: ci-güe-ña.", "Sí, la U suena.", "Va Ü: CIGÜEÑA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "¿U o Ü?", "pasos": ["PING_INO.", "G_ISO."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Decí despacio PINGÜINO y GUISO. ¿En cuál suena la U?"},
"tip": {"titulo": "¿Suena?", "texto": "Si la U suena, lleva los dos puntitos."},
"ojo": ["GUISO no lleva puntitos: la U no suena.", "PINGÜINO sí lleva: la U suena."],
"resumen": [{"titulo": "GUE · GUI", "texto": "La U no suena."}, {"titulo": "GÜE · GÜI", "texto": "La U suena."}, {"titulo": "Diéresis", "texto": "Los dos puntitos."}],
"glosario": [{"palabra": "Diéresis", "significado": "Dos puntitos arriba de la U."}, {"palabra": "Cigüeña", "significado": "Ave de patas y pico largos."}],
"carpeta": ["¿PING_INO lleva U o Ü?", "¿G_ISO lleva U o Ü?", "Tomi escribió PINGUINO sin puntitos. ¿Está bien?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("Ü") + low("PINGÜINO"), low("U") + low("GUISO"), NO],
"soluciones": {"incompleto": "Ü. U.", "solo": "En PINGÜINO.", "carpeta": ["Ü: PINGÜINO.", "U: GUISO.", "No: va PINGÜINO."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a escribir palabras con las cuatro reglas en un dictado.",
"vas_a_ver": ["Escuchar el sonido", "Elegir la regla", "Escribir y revisar"],
"secciones": [
 S(1, "Las cuatro reglas", [
  IMG("Las reglas de la detective", "Para el dictado.", FG.tiras(["QUE · QUI: CON U (QUESO)", "GUE · GUI: CON U (GUISO)", "GÜE · GÜI: CON Ü (PINGÜINO)", "GA · GO · GU: SIN U EXTRA (GATO)"], numeros=False)),
 ]),
 S(1, "Oraciones dictadas", [
  P("Escuchamos la oración entera y escribimos."),
  IMG("Para dictar", "Con mayúscula y punto.", FG.tiras(["EL PINGÜINO COME QUESO.", "TOMI TOCA LA GUITARRA."], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Pedile a alguien que te dicte estas palabras."),
  IMG("Para dictar", "Escribilas en tu carpeta.", FG.nombres(["MÁQUINA", "JUGUETE", "CIGÜEÑA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Dictado", "planteo": "Me dictan: MANGUERA.", "pasos": ["Escucho GUE.", "La U no suena: GUE.", "MANGUERA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Me dictan: EL MOSQUITO Y LA CIGÜEÑA.", "pasos": ["MOS_ITO: ___ .", "CIG_EÑA: ___ ."]},
"ejemplo_solo": {"titulo": "Tu dictado", "planteo": "Pedí que te dicten: QUIERO UN JUGUETE."},
"tip": {"titulo": "Revisá al final", "texto": "Buscá cada QU, GU y GÜ."},
"ojo": ["Nunca QE ni QI.", "Si la U suena, puntitos."],
"resumen": [{"titulo": "QUE · QUI", "texto": "Con U."}, {"titulo": "GUE · GUI", "texto": "Con U muda."}, {"titulo": "GÜE · GÜI", "texto": "Con Ü."}],
"glosario": [{"palabra": "Dictado", "significado": "Escribir lo que otro dice."}, {"palabra": "Regla", "significado": "Algo que siempre se cumple."}],
"carpeta": ["Te dictan el ave que vive en el hielo. ¿Cómo se escribe?", "Te dictan el instrumento con cuerdas. ¿Cómo se escribe?", "Tomi escribió MAQINA en el dictado. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PINGÜINO") + low("EL PINGÜINO"), low("GUITARRA") + low("LA GUITARRA"), low("MÁQUINA") + low("maquina")],
"soluciones": {"incompleto": "QU. Ü.", "solo": "QUIERO UN JUGUETE.", "carpeta": ["PINGÜINO.", "GUITARRA.", "MÁQUINA."]},
}

ACT = {
"1": [MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["QUESO", "QESO", "KESO"], "QUESO", "QUE LLEVA U.", n="aplicar"),
      SA("COMPLETÁ: MOS_ITO", low("MOSQUITO"), "MOSQUITO.", n="aplicar")],
"2": [MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["GUITARRA", "GITARRA"], "GUITARRA", "GUI LLEVA U.", n="aplicar"),
      TF("EN GUISO LA U SUENA.", "FALSO", "LA U NO SUENA.", n="analizar")],
"3": [UNI("UNÍ CADA PALABRA CON SU REGLA.", [("PINGÜINO", "LA U SUENA"), ("GUISO", "LA U NO SUENA"), ("QUESO", "QUE CON U")], "ESCUCHÁ LA U.", n="analizar"),
      SA("ESCRIBÍ BIEN: PING_INO", low("PINGÜINO") + low("pinguino"), "PINGÜINO, CON Ü.", n="aplicar")],
"4": [SA("ESCRIBÍ LA PALABRA: EL AVE QUE VIVE EN EL HIELO", low("PINGÜINO") + low("EL PINGÜINO"), "PINGÜINO.", n="aplicar"),
      SA("ESCRIBÍ LA PALABRA: LO QUE SE HACE CON LECHE Y TIENE AGUJEROS", low("QUESO") + low("EL QUESO"), "QUESO.", n="aplicar")],
"5": [MC("RELÁMPAGO. QUE Y QUI LLEVAN…", ["U", "NADA"], "U", "UNA U QUE NO SUENA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ESTÁ BIEN?", ["JUGUETE", "JUGETE"], "JUGUETE", "GUE CON U.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ESTÁ BIEN?", ["CIGÜEÑA", "CIGEÑA"], "CIGÜEÑA", "LA U SUENA: Ü.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. LOS DOS PUNTITOS SE LLAMAN…", ["DIÉRESIS", "ACENTO"], "DIÉRESIS", "VAN SOBRE LA U.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["PAQUETE", "PAQETE"], "PAQUETE", "QUE CON U.", n="aplicar")],
 [1, SA("COMPLETÁ: Q_INCE", low("QUINCE") + low("U"), "QUINCE.", n="aplicar")],
 [1, TF("EN QUESO LA U SUENA.", "FALSO", "NO SUENA.", n="analizar")],
 [2, MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["MANGUERA", "MANGERA"], "MANGUERA", "GUE CON U.", n="aplicar")],
 [2, SA("COMPLETÁ: JUG_ETE", low("JUGUETE") + low("U"), "JUGUETE.", n="aplicar")],
 [2, TF("GITARRA ESTÁ BIEN ESCRITO.", "FALSO", "VA GUITARRA.", n="error")],
 [3, MC("¿EN CUÁL SUENA LA U?", ["PINGÜINO", "GUISO", "QUESO"], "PINGÜINO", "LLEVA Ü.", n="analizar")],
 [3, SA("ESCRIBÍ BIEN: CIG_EÑA", low("CIGÜEÑA") + low("ciguena") + low("cigueña"), "CIGÜEÑA.", n="aplicar")],
 [3, MC("¿CÓMO SE LLAMAN LOS DOS PUNTITOS DE LA Ü?", ["DIÉRESIS", "PUNTO FINAL", "ACENTO"], "DIÉRESIS", "AVISAN QUE LA U SUENA.", n="recordar")],
 [4, SA("ESCRIBÍ LA PALABRA: INSECTO QUE PICA", low("MOSQUITO") + low("EL MOSQUITO"), "MOSQUITO.", n="aplicar")],
 [4, MC("¿CUÁL ESTÁ MAL ESCRITA?", ["MAQINA", "GUISO", "PINGÜINO"], "MAQINA", "VA MÁQUINA.", n="error")],
 [4, UNI("UNÍ CADA PALABRA CON CÓMO SE ESCRIBE.", [("QUESO", "QUE"), ("GUISO", "GUI SIN PUNTITOS"), ("PINGÜINO", "GÜI CON PUNTITOS")], "LAS CUATRO REGLAS.", n="analizar")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 15, "estilo": "primeros",
     "practica": "Práctica general: GUE, GUI, QUE y QUI", "examen_titulo": "Nivel jefe: GUE, GUI, QUE y QUI",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-15.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
