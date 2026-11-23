# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 5 · Ortografía: M antes de P y B. Genera mision-5.json.
Regla de primeros años y vía fonológica (la VOZ de las clases dice sonidos, no nombres de letras; el PDF muestra las letras).
Metáfora: el cuaderno viajero de Sofi (Sofi es «detective de palabras»).
Niveles: 1 palabras con MP · 2 palabras con MB · 3 dictado con MP y MB · 4 corregir palabras con M y N."""
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
TF = lambda p, ok, e, **k: {"t": "true_false", "p": p, "o": ["VERDADERO", "FALSO"], "r": {"correcta": ok}, "e": e, **k}
UNI = lambda p, pares, e, **k: {"t": "matching", "p": p, "o": {"izquierda": [a for a, _ in pares], "derecha": [b for _, b in pares]}, "r": {"pares": dict(pares)}, "e": e, **k}
ESTILO = {"estilo": "primeros"}
low = lambda w: [w, w.lower(), w.capitalize()]

N1 = {**ESTILO,
"objetivo": "Vas a escribir bien palabras con MP.",
"vas_a_ver": ["Antes de P va M", "Palabras con MP", "Encontrar MP en un texto"],
"secciones": [
 S(1, "Antes de P va M", [
  P("Sofi es <b>detective de palabras</b>. Hoy busca una pista."),
  D("La regla", "Antes de <b>P</b> siempre se escribe <b>M</b>."),
  IMG("Palabras con MP", "La M antes de la P.", FG.letras("CAMPO", resaltar=(2, 3))),
 ]),
 S(1, "Palabras con MP", [
  P("CAMPANA, LÁMPARA, TROMPETA, COMPRAR, SIEMPRE."),
  IMG("Más palabras", "Todas tienen MP.", FG.nombres(["CAMPANA", "LÁMPARA", "TROMPETA", "SIEMPRE"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras con huecos", "¿Qué letra falta?", FG.nombres(["CA_PO", "LÁ_PARA", "CO_PRAR"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "TROMPETA", "planteo": "¿Con qué se escribe TROMPETA?", "pasos": ["Después viene la P.", "Antes de P va M.", "TROMPETA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí la letra que falta.", "pasos": ["CA_PANA.", "SIE_PRE."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Buscá en tu casa una palabra con MP."},
"tip": {"titulo": "Mirá la letra que sigue", "texto": "Si sigue P, va M."},
"ojo": ["CAMPO, no CANPO.", "La regla es siempre igual."],
"resumen": [{"titulo": "La regla", "texto": "Antes de P va M."}, {"titulo": "Ejemplos", "texto": "CAMPO, LÁMPARA."}, {"titulo": "Siempre", "texto": "No tiene excepciones."}],
"glosario": [{"palabra": "Regla", "significado": "Algo que siempre se cumple."}, {"palabra": "Ortografía", "significado": "Escribir las palabras bien."}],
"carpeta": ["Completá: CA_PO. ¿Qué letra va?", "Escribí bien la palabra LÁ_PARA.", "Tomi escribió CONPRAR. ¿Cómo se escribe?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("M"), low("LÁMPARA") + low("lampara"), low("COMPRAR")],
"soluciones": {"incompleto": "M. M.", "solo": "Por ejemplo: LÁMPARA.", "carpeta": ["M.", "LÁMPARA.", "COMPRAR: antes de P va M."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a escribir bien palabras con MB.",
"vas_a_ver": ["Antes de B va M", "Palabras con MB", "MP y MB juntas"],
"secciones": [
 S(1, "Antes de B va M", [
  D("La regla", "Antes de <b>B</b> también se escribe <b>M</b>."),
  IMG("Palabras con MB", "La M antes de la B.", FG.letras("HOMBRE", resaltar=(2, 3))),
 ]),
 S(1, "Palabras con MB", [
  P("TAMBOR, SOMBRERO, BOMBERO, HAMBRE, TAMBIÉN."),
  IMG("Más palabras", "Todas tienen MB.", FG.nombres(["TAMBOR", "SOMBRERO", "BOMBERO", "TAMBIÉN"], cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Palabras con huecos", "¿Qué letra falta?", FG.nombres(["TA_BOR", "SO_BRERO", "HA_BRE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "BOMBERO", "planteo": "¿Con qué se escribe BOMBERO?", "pasos": ["Después viene la B.", "Antes de B va M.", "BOMBERO."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí la letra que falta.", "pasos": ["TA_BIÉN.", "HO_BRE."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Escribí una oración con la palabra BOMBERO."},
"tip": {"titulo": "P y B, amigas de M", "texto": "Antes de P y de B, siempre M."},
"ojo": ["TAMBIÉN, no TANBIÉN.", "Antes de V no hay regla de M."],
"resumen": [{"titulo": "MB", "texto": "Antes de B va M."}, {"titulo": "MP", "texto": "Antes de P va M."}, {"titulo": "Ejemplos", "texto": "TAMBOR, CAMPO."}],
"glosario": [{"palabra": "Sombrero", "significado": "Lo que se usa en la cabeza."}, {"palabra": "Tambor", "significado": "Instrumento que se golpea."}],
"carpeta": ["Completá: TA_BOR. ¿Qué letra va?", "Escribí bien la palabra SO_BRERO.", "Sofi escribió TANBIÉN. ¿Cómo se escribe?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("M"), low("SOMBRERO"), low("TAMBIÉN") + low("tambien")],
"soluciones": {"incompleto": "M. M.", "solo": "Por ejemplo: El bombero apaga el fuego.", "carpeta": ["M.", "SOMBRERO.", "TAMBIÉN: antes de B va M."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a escribir palabras con MP y MB en un dictado.",
"vas_a_ver": ["Escuchar con atención", "Pensar la regla", "Escribir y revisar"],
"secciones": [
 S(1, "El dictado", [
  D("Dictado", "Alguien dice palabras y vos las <b>escribís</b>."),
  P("Escuchá la palabra entera. Pensá: ¿viene P o B?"),
  IMG("Palabras para el dictado", "Con MP y con MB.", FG.nombres(["CAMPANA", "TAMBOR", "LÁMPARA", "HOMBRE"], cols=2)),
 ]),
 S(1, "Pensar la regla", [
  P("Antes de <b>P</b> y de <b>B</b> va <b>M</b>."),
  P("Después del dictado, <b>revisá</b> cada palabra."),
  IMG("Oraciones dictadas", "Con mayúscula y punto.", FG.tiras(["EL BOMBERO TOCA LA CAMPANA.", "SIEMPRE COMPRO PAN."], numeros=True, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Pedile a alguien que te dicte estas palabras."),
  IMG("Para dictar", "Escribilas en tu carpeta.", FG.nombres(["SOMBRERO", "COMPRAR", "TAMBIÉN"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Dictado", "planteo": "Me dictan: CAMPANA.", "pasos": ["Escucho: cam-pa-na.", "Viene P: va M.", "Escribo CAMPANA."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Me dictan: EL HOMBRE TIENE HAMBRE.", "pasos": ["EL HO_BRE TIENE HA_BRE."]},
"ejemplo_solo": {"titulo": "Tu dictado", "planteo": "Pedí que te dicten: LA LÁMPARA ESTÁ PRENDIDA."},
"tip": {"titulo": "Revisá al final", "texto": "Mirá cada palabra con MP o MB."},
"ojo": ["Escuchá la palabra entera antes de escribir.", "No te olvides de la mayúscula y el punto."],
"resumen": [{"titulo": "Escuchar", "texto": "Toda la palabra."}, {"titulo": "Pensar", "texto": "Antes de P y B, M."}, {"titulo": "Revisar", "texto": "Al final."}],
"glosario": [{"palabra": "Dictado", "significado": "Escribir lo que otro dice."}, {"palabra": "Revisar", "significado": "Mirar de nuevo para corregir."}],
"carpeta": ["¿Cómo se escribe la palabra que nombra el que apaga incendios?", "¿Cómo se escribe lo que da luz y empieza con LÁ?", "Tomi escribió CANPANA en el dictado. ¿Cómo va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("BOMBERO"), low("LÁMPARA") + low("lampara"), low("CAMPANA")],
"soluciones": {"incompleto": "M. M.", "solo": "LA LÁMPARA ESTÁ PRENDIDA.", "carpeta": ["BOMBERO.", "LÁMPARA.", "CAMPANA: antes de P va M."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a corregir palabras mal escritas con M y N.",
"vas_a_ver": ["Encontrar el error", "Cambiar N por M", "Cuándo va N"],
"secciones": [
 S(1, "Encontrar el error", [
  P("Tomi escribió: <b>CANPO</b> y <b>TANBOR</b>. ¡Hay errores!"),
  D("Corregir", "Buscamos el error y escribimos la palabra <b>bien</b>."),
  IMG("Antes y después", "Cambiamos N por M.", FG.tiras(["CANPO → CAMPO", "TANBOR → TAMBOR"], numeros=False)),
 ]),
 S(1, "Cuándo va N", [
  P("Antes de otras letras puede ir <b>N</b>: CANTO, MANDO, PONGO."),
  P("Pero antes de <b>P</b> y <b>B</b>, siempre <b>M</b>."),
  IMG("Con N", "Estas están bien.", FG.nombres(["CANTO", "MANDO", "PONGO"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Están bien?", "Revisá cada una.", FG.nombres(["SONBRERO", "CANTO", "SIENPRE"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Corregir", "planteo": "INVIERNO, ¿está bien?", "pasos": ["Después de N viene V.", "Antes de V no hay regla de M.", "INVIERNO está bien."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Corregí: LANPARA.", "pasos": ["Antes de P va ___ .", "Se escribe ___ ."]},
"ejemplo_solo": {"titulo": "Detective", "planteo": "Revisá un texto tuyo y buscá palabras con MP o MB."},
"tip": {"titulo": "Mirá la letra que sigue", "texto": "P o B: M. Otra letra: puede ser N."},
"ojo": ["CANTO está bien: después viene T.", "SIENPRE está mal: después viene P."],
"resumen": [{"titulo": "Error", "texto": "N antes de P o B."}, {"titulo": "Corregir", "texto": "Cambiar por M."}, {"titulo": "N", "texto": "Va antes de otras letras."}],
"glosario": [{"palabra": "Error", "significado": "Algo que está mal."}, {"palabra": "Corregir", "significado": "Arreglar el error."}],
"carpeta": ["¿Cuál palabra del dibujo está bien escrita?", "Corregí SONBRERO.", "Corregí SIENPRE."],
"carpeta_nivel": ["analizar", "error", "error"],
"respuestas_carpeta": [low("CANTO"), low("SOMBRERO"), low("SIEMPRE")],
"soluciones": {"incompleto": "M. LÁMPARA.", "solo": "Las palabras que encuentres.", "carpeta": ["CANTO.", "SOMBRERO.", "SIEMPRE."]},
}

ACT = {
"1": [MC("CA_PO. ¿QUÉ LETRA FALTA?", ["M", "N"], "M", "ANTES DE P VA M.", n="aplicar"),
      SA("ESCRIBÍ BIEN: LÁ_PARA", low("LÁMPARA") + low("lampara"), "LÁMPARA.", n="aplicar")],
"2": [MC("TA_BOR. ¿QUÉ LETRA FALTA?", ["M", "N"], "M", "ANTES DE B VA M.", n="aplicar"),
      UNI("UNÍ CADA PALABRA CON SU PAR.", [("TAMBOR", "MB"), ("CAMPANA", "MP"), ("HOMBRE", "MB")], "MIRÁ LA LETRA QUE SIGUE A LA M.", n="analizar")],
"3": [SA("ESCRIBÍ LA PALABRA: EL QUE APAGA INCENDIOS ES EL ___", low("BOMBERO"), "BOMBERO, CON MB.", n="aplicar"),
      SA("ESCRIBÍ LA PALABRA: LA QUE SUENA EN LA ESCUELA ES LA ___", low("CAMPANA"), "CAMPANA, CON MP.", n="aplicar")],
"4": [TF("CANPO ESTÁ BIEN ESCRITO.", "FALSO", "SE ESCRIBE CAMPO.", n="error"),
      MC("¿CUÁL ESTÁ BIEN ESCRITA?", ["CANTO", "TANBOR", "SIENPRE"], "CANTO", "ANTES DE T PUEDE IR N.", n="analizar")],
"5": [MC("RELÁMPAGO. ANTES DE P VA…", ["M", "N"], "M", "SIEMPRE M.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ANTES DE B VA…", ["M", "N"], "M", "SIEMPRE M.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL ESTÁ BIEN?", ["SOMBRERO", "SONBRERO"], "SOMBRERO", "MB.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL ESTÁ BIEN?", ["SIEMPRE", "SIENPRE"], "SIEMPRE", "MP.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("TRO_PETA. ¿QUÉ LETRA FALTA?", ["M", "N"], "M", "ANTES DE P VA M.", n="aplicar")],
 [1, SA("ESCRIBÍ BIEN: CO_PRAR", low("COMPRAR"), "COMPRAR.", n="aplicar")],
 [1, TF("ANTES DE P SIEMPRE SE ESCRIBE M.", "VERDADERO", "ES LA REGLA.", n="recordar")],
 [2, MC("HA_BRE. ¿QUÉ LETRA FALTA?", ["M", "N"], "M", "ANTES DE B VA M.", n="aplicar")],
 [2, SA("ESCRIBÍ BIEN: TA_BIÉN", low("TAMBIÉN") + low("tambien"), "TAMBIÉN.", n="aplicar")],
 [2, UNI("UNÍ CADA PALABRA CON SU PAR.", [("BOMBERO", "MB"), ("LÁMPARA", "MP"), ("SOMBRERO", "MB")], "MIRÁ LA LETRA QUE SIGUE.", n="analizar")],
 [3, SA("ESCRIBÍ LA PALABRA: SE TOCA CON PALILLOS, ES UN ___", low("TAMBOR"), "TAMBOR, CON MB.", n="aplicar")],
 [3, SA("ESCRIBÍ LA PALABRA: DA LUZ EN LA MESA DE LUZ, ES UNA ___", low("LÁMPARA") + low("lampara"), "LÁMPARA, CON MP.", n="aplicar")],
 [3, TF("TOMI ESCRIBIÓ CANPANA EN EL DICTADO Y ESTÁ BIEN.", "FALSO", "SE ESCRIBE CAMPANA.", n="error")],
 [4, MC("¿CUÁL ESTÁ MAL ESCRITA?", ["SIENPRE", "CANTO", "MANDO"], "SIENPRE", "ANTES DE P VA M.", n="error")],
 [4, SA("CORREGÍ: SONBRERO", low("SOMBRERO"), "SOMBRERO.", n="error")],
 [4, TF("CANTO ESTÁ BIEN ESCRITO.", "VERDADERO", "ANTES DE T PUEDE IR N.", n="analizar")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: M antes de P y B", "examen_titulo": "Nivel jefe: M antes de P y B",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
