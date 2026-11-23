# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 5 · My Family. Genera mision-5.json.
Regla de primeros años. Metáfora: la familia de Sofi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 mum, dad, baby · 2 brother, sister, grandma, grandpa · 3 this is my family · 4 who is he, who is she."""
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
low = lambda w: [w, w.lower(), w.capitalize()]
def acepta(*ws):
    out = []
    for w in ws: out += [w, w.lower(), w.capitalize()]
    return out


N1 = {**ESTILO,
"objetivo": "Vas a nombrar a mamá, papá y al bebé en inglés.",
"vas_a_ver": ["MUM: mamá", "DAD: papá", "BABY: bebé"],
"secciones": [
 S(1, "Mi familia", [
  D("Familia", "Las personas que viven con nosotros y nos cuidan."),
  P("Mamá es <b>MUM</b>, papá es <b>DAD</b> y bebé es <b>BABY</b>."),
  IMG("En inglés", "Cada uno en inglés.", FG.tiras(["MAMÁ = MUM", "PAPÁ = DAD", "BEBÉ = BABY"], numeros=False, cols=1)),
 ]),
 S(1, "Cada familia es distinta", [
  P("Hay familias grandes y chicas. Todas son <b>familias</b>."),
  IMG("Familias", "Distintas y lindas.", FG.tiras(["MUM AND ME", "DAD AND ME", "MUM, DAD AND BABY"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la familia de Sofi. La vas a usar en la carpeta."),
  IMG("La familia de Sofi", "¿Quién es quién?", FG.tiras(["LA MAMÁ DE SOFI", "EL PAPÁ DE SOFI", "EL HERMANITO BEBÉ"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi presenta", "planteo": "Sofi muestra una foto.", "pasos": ["Señala a su mamá.", "Dice: MUM!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Papá en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "Dibujá a tu familia y escribí MUM, DAD o BABY."},
"tip": {"titulo": "Con cariño", "texto": "Decí MUM y DAD con una sonrisa."},
"ojo": ["MUM es mamá.", "DAD es papá."],
"resumen": [{"titulo": "MUM", "texto": "Mamá."}, {"titulo": "DAD", "texto": "Papá."}, {"titulo": "BABY", "texto": "Bebé."}],
"glosario": [{"palabra": "MUM", "significado": "Mamá."}, {"palabra": "BABY", "significado": "Bebé."}],
"carpeta": ["Señalás a tu mamá. ¿Qué decís?", "Señalás a tu papá. ¿Qué decís?", "Sofi señala al bebé y dice DAD. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("MUM", "MOM", "MUMMY"), acepta("DAD", "DADDY"), acepta("BABY")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "DAD.", "solo": "Tu familia.", "carpeta": ["MUM.", "DAD.", "BABY."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a nombrar hermanos y abuelos en inglés.",
"vas_a_ver": ["BROTHER y SISTER", "GRANDMA y GRANDPA", "Varón o nena"],
"secciones": [
 S(1, "Hermanos", [
  D("Hermanos", "Hijos de la misma familia."),
  P("Hermano es <b>BROTHER</b> y hermana es <b>SISTER</b>."),
  IMG("Hermanos", "En inglés.", FG.tiras(["HERMANO = BROTHER", "HERMANA = SISTER"], numeros=False, cols=1)),
 ]),
 S(1, "Abuelos", [
  P("Abuela es <b>GRANDMA</b> y abuelo es <b>GRANDPA</b>."),
  IMG("Abuelos", "En inglés.", FG.tiras(["ABUELA = GRANDMA", "ABUELO = GRANDPA"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la familia de Tomi. La vas a usar en la carpeta."),
  IMG("La familia de Tomi", "¿Quién es?", FG.tiras(["SU HERMANA LUCÍA", "SU ABUELO PEPE", "SU ABUELA ROSA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi presenta", "planteo": "Tomi muestra a Lucía.", "pasos": ["Lucía es su hermana.", "Tomi dice: SISTER!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Abuela en inglés es ___.", "pasos": ["___."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "¿Tenés BROTHER, SISTER, GRANDMA o GRANDPA? Decilo en inglés."},
"tip": {"titulo": "GRAND", "texto": "GRANDMA y GRANDPA empiezan igual."},
"ojo": ["BROTHER es varón.", "SISTER es nena."],
"resumen": [{"titulo": "BROTHER", "texto": "Hermano."}, {"titulo": "SISTER", "texto": "Hermana."}, {"titulo": "GRANDMA / GRANDPA", "texto": "Abuela y abuelo."}],
"glosario": [{"palabra": "SISTER", "significado": "Hermana."}, {"palabra": "GRANDPA", "significado": "Abuelo."}],
"carpeta": ["Lucía es la hermana de Tomi. ¿Qué es?", "Pepe es el abuelo de Tomi. ¿Qué es?", "Tomi dice que su abuela Rosa es GRANDPA. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("SISTER"), acepta("GRANDPA", "GRANDAD", "GRANDFATHER"), acepta("GRANDMA", "GRANNY", "GRANDMOTHER")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "GRANDMA.", "solo": "Tu familia.", "carpeta": ["SISTER.", "GRANDPA.", "GRANDMA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a presentar a tu familia en inglés.",
"vas_a_ver": ["THIS IS MY…", "Presentar a cada uno", "Todas las familias"],
"secciones": [
 S(1, "Presentar", [
  D("Presentar", "Decir quién es alguien."),
  P("Para presentar decimos: <b>THIS IS MY</b> y quién es. Quiere decir: este es mi…"),
  IMG("Presentar", "Así presentamos.", FG.tiras(["THIS IS MY MUM.", "THIS IS MY BROTHER."], numeros=False, cols=1)),
 ]),
 S(1, "Todas las familias", [
  P("Cada familia es distinta. ¡Todas se presentan con <b>THIS IS MY</b>!"),
  IMG("Familias", "Distintas formas.", FG.tiras(["THIS IS MY GRANDMA.", "THIS IS MY DAD.", "THIS IS MY SISTER."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las fotos de Sofi. Las vas a usar en la carpeta."),
  IMG("Las fotos", "¿A quién presenta?", FG.tiras(["FOTO DE SU MAMÁ", "FOTO DE SU ABUELO", "FOTO DE SU HERMANO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi presenta", "planteo": "Sofi muestra a su papá.", "pasos": ["Lo señala.", "Dice: THIS IS MY DAD.", "¡Hola, papá de Sofi!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "THIS IS ___ MUM.", "pasos": ["THIS IS ___ MUM."]},
"ejemplo_solo": {"titulo": "Tu foto", "planteo": "Mostrá una foto y decí THIS IS MY…"},
"tip": {"titulo": "Señalá", "texto": "Señalá a la persona al presentarla."},
"ojo": ["THIS es este o esta.", "MY es mi."],
"resumen": [{"titulo": "THIS IS MY…", "texto": "Este es mi…"}, {"titulo": "Presentar", "texto": "Decir quién es."}, {"titulo": "Familias", "texto": "Todas distintas."}],
"glosario": [{"palabra": "THIS", "significado": "Este o esta."}, {"palabra": "MY", "significado": "Mi."}],
"carpeta": ["Sofi muestra a su mamá. Completá: THIS IS MY ___.", "Sofi muestra a su abuelo. Completá: THIS IS MY ___.", "Sofi muestra a su hermano y dice THIS IS MY SISTER. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("MUM", "MOM"), acepta("GRANDPA", "GRANDAD"), acepta("THIS IS MY BROTHER", "BROTHER")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "MY.", "solo": "Tu foto.", "carpeta": ["MUM.", "GRANDPA.", "THIS IS MY BROTHER."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a preguntar quién es alguien en inglés.",
"vas_a_ver": ["HE: él", "SHE: ella", "WHO IS HE? WHO IS SHE?"],
"secciones": [
 S(1, "Él y ella", [
  D("Él y ella", "Palabras para hablar de un varón o de una nena."),
  P("Para un varón decimos <b>HE</b>. Para una nena o mujer decimos <b>SHE</b>."),
  IMG("Él y ella", "En inglés.", FG.tiras(["ÉL = HE", "ELLA = SHE"], numeros=False, cols=1)),
 ]),
 S(1, "¿Quién es?", [
  P("Preguntamos: <b>WHO IS HE?</b> o <b>WHO IS SHE?</b>"),
  IMG("Preguntar", "Y contestar.", FG.tiras(["WHO IS SHE? SHE IS MY MUM.", "WHO IS HE? HE IS MY DAD."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la foto de Tomi. La vas a usar en la carpeta."),
  IMG("La foto de Tomi", "¿Quién es?", FG.tiras(["SU ABUELA", "SU HERMANO", "SU PAPÁ"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Sofi pregunta", "planteo": "Sofi ve una foto de Tomi.", "pasos": ["Sofi: WHO IS SHE?", "Tomi: SHE IS MY GRANDMA.", "¡Qué linda!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "WHO IS ___? HE IS MY DAD.", "pasos": ["WHO IS ___?"]},
"ejemplo_solo": {"titulo": "A preguntar", "planteo": "Mirá fotos con tu familia y preguntá WHO IS HE? o WHO IS SHE?"},
"tip": {"titulo": "HE y SHE", "texto": "SHE tiene una letra más: S."},
"ojo": ["HE es él.", "SHE es ella."],
"resumen": [{"titulo": "HE", "texto": "Él."}, {"titulo": "SHE", "texto": "Ella."}, {"titulo": "WHO IS…?", "texto": "¿Quién es…?"}],
"glosario": [{"palabra": "WHO", "significado": "Quién."}, {"palabra": "SHE", "significado": "Ella."}],
"carpeta": ["Es la abuela. ¿WHO IS HE o WHO IS SHE?", "Es el hermano. ¿HE o SHE?", "Tomi muestra a su papá y dice SHE IS MY DAD. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("WHO IS SHE", "WHO IS SHE?", "SHE"), acepta("HE"), acepta("HE IS MY DAD", "HE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "HE.", "solo": "Tu juego.", "carpeta": ["WHO IS SHE?", "HE.", "HE IS MY DAD."]},
}

ACT = {
"1": [MC("MAMÁ EN INGLÉS ES…", ["MUM", "DAD", "BABY"], "MUM", "MUM ES MAMÁ.", n="recordar"),
      MC("SEÑALÁS AL BEBÉ. ¿QUÉ DECÍS?", ["BABY", "DAD", "MUM"], "BABY", "BEBÉ ES BABY.", n="aplicar"),
      MC("SOFI SEÑALA A SU PAPÁ. ¿QUÉ DICE?", ["DAD", "MUM", "BABY"], "DAD", "PAPÁ ES DAD.", n="aplicar")],
"2": [MC("LUCÍA ES LA HERMANA DE TOMI. ES SU…", ["SISTER", "BROTHER", "GRANDPA"], "SISTER", "HERMANA ES SISTER.", n="aplicar"),
      MC("EL ABUELO EN INGLÉS ES…", ["GRANDPA", "GRANDMA", "BROTHER"], "GRANDPA", "ABUELO ES GRANDPA.", n="aplicar")],
"3": [MC("SOFI MUESTRA A SU MAMÁ. ¿QUÉ DICE?", ["THIS IS MY MUM", "THIS IS MY DAD", "I AM SIX"], "THIS IS MY MUM", "ASÍ PRESENTA.", n="aplicar"),
      ORD("ORDENÁ LA FRASE.", ["MY", "THIS", "DAD", "IS"], ["THIS", "IS", "MY", "DAD"], "THIS IS MY DAD.", n="aplicar")],
"4": [MC("ES TU MAMÁ. ¿QUÉ PREGUNTA TU AMIGO?", ["WHO IS SHE?", "WHO IS HE?", "HOW OLD ARE YOU?"], "WHO IS SHE?", "MAMÁ ES MUJER: SHE.", n="aplicar"),
      MC("TOMI DICE SHE IS MY BROTHER. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR HE", "ESTÁ BIEN", "DEBE DECIR MUM"], "DEBE DECIR HE", "BROTHER ES VARÓN: HE.", n="error")],
"5": [MC("RELÁMPAGO. PAPÁ EN INGLÉS ES…", ["DAD", "MUM", "BABY"], "DAD", "DAD.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. HERMANO EN INGLÉS ES…", ["BROTHER", "SISTER", "GRANDMA"], "BROTHER", "BROTHER.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ES TU ABUELA. DECÍS THIS IS MY…", ["GRANDMA", "GRANDPA", "DAD"], "GRANDMA", "GRANDMA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. PARA UNA NENA DECIMOS…", ["SHE", "HE", "MY"], "SHE", "SHE.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("BEBÉ EN INGLÉS ES…", ["BABY", "MUM", "DAD"], "BABY", "BABY ES BEBÉ.", n="recordar")],
 [1, SA("SEÑALÁS A TU MAMÁ. ESCRIBÍ MAMÁ EN INGLÉS.", acepta("MUM", "MOM", "MUMMY"), "MUM.", n="aplicar")],
 [1, MC("SOFI SEÑALA A SU MAMÁ Y DICE DAD. ¿QUÉ ESTÁ MAL?", ["DEBE DECIR MUM", "ESTÁ BIEN", "DEBE DECIR BABY"], "DEBE DECIR MUM", "MAMÁ ES MUM.", n="error")],
 [2, MC("HERMANA EN INGLÉS ES…", ["SISTER", "BROTHER", "BABY"], "SISTER", "SISTER ES HERMANA.", n="recordar")],
 [2, SA("PEPE ES EL ABUELO DE TOMI. ESCRIBÍ ABUELO EN INGLÉS.", acepta("GRANDPA", "GRANDAD", "GRANDFATHER"), "GRANDPA.", n="aplicar")],
 [2, MC("ROSA ES LA ABUELA DE TOMI. ES SU…", ["GRANDMA", "GRANDPA", "SISTER"], "GRANDMA", "ABUELA ES GRANDMA.", n="aplicar")],
 [3, MC("THIS IS MY MUM QUIERE DECIR…", ["ESTA ES MI MAMÁ", "ESTE ES MI PAPÁ", "HOLA, MAMÁ"], "ESTA ES MI MAMÁ", "THIS IS MY = ESTE ES MI.", n="recordar")],
 [3, ORD("ORDENÁ LA FRASE.", ["SISTER", "IS", "THIS", "MY"], ["THIS", "IS", "MY", "SISTER"], "THIS IS MY SISTER.", n="aplicar")],
 [3, MC("TOMI MUESTRA A SU ABUELO Y DICE THIS IS MY GRANDMA. ¿QUÉ ESTÁ MAL?", ["ES GRANDPA", "ESTÁ BIEN", "ES BABY"], "ES GRANDPA", "ABUELO ES GRANDPA.", n="error")],
 [4, MC("WHO IS SHE QUIERE DECIR…", ["¿QUIÉN ES ELLA?", "¿QUIÉN ES ÉL?", "¿CÓMO ESTÁS?"], "¿QUIÉN ES ELLA?", "SHE ES ELLA.", n="recordar")],
 [4, MC("ES TU PAPÁ. ¿QUÉ DECÍS?", ["HE IS MY DAD", "SHE IS MY DAD", "HE IS MY MUM"], "HE IS MY DAD", "PAPÁ ES VARÓN: HE.", n="aplicar")],
 [4, MC("ES TU HERMANA. ¿QUÉ DECÍS?", ["SHE IS MY SISTER", "HE IS MY SISTER", "SHE IS MY BROTHER"], "SHE IS MY SISTER", "HERMANA: SHE.", n="aplicar")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 5, "estilo": "primeros",
     "practica": "Práctica general: My Family", "examen_titulo": "Nivel jefe: My Family",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-5.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
