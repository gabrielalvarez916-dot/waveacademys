# -*- coding: utf-8 -*-
"""Inglés 1 (Nivel Medio, 1.º año) · Misión 4 · My Things. Genera mision-4.json.
Regla de primeros años. Metáfora: la mochila de Tomi. Explicaciones en castellano, palabras en inglés.
Niveles: 1 pencil, book, bag · 2 órdenes (stand up, sit down) · 3 is it a pen? yes, it is · 4 in y on: where is it."""
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
"objetivo": "Vas a nombrar tus útiles en inglés.",
"vas_a_ver": ["PENCIL: lápiz", "BOOK: libro", "BAG: mochila"],
"secciones": [
 S(1, "Mis útiles", [
  D("Útiles", "Las cosas que usamos en la escuela."),
  P("Lápiz es <b>PENCIL</b>, libro es <b>BOOK</b> y mochila es <b>BAG</b>."),
  IMG("Mis útiles", "Cada cosa en inglés.", FG.tiras(["LÁPIZ = PENCIL", "LIBRO = BOOK", "MOCHILA = BAG"], numeros=False, cols=1)),
 ]),
 S(1, "Dos más", [
  P("La lapicera es <b>PEN</b> y la goma es <b>RUBBER</b>."),
  IMG("Dos más", "Más útiles.", FG.tiras(["LAPICERA = PEN", "GOMA = RUBBER"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la mochila de Tomi. La vas a usar en la carpeta."),
  IMG("La mochila de Tomi", "¿Qué hay adentro?", FG.tiras(["UN LÁPIZ", "UN LIBRO", "UNA GOMA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi abre su mochila", "planteo": "Tomi saca un libro.", "pasos": ["Lo muestra.", "Dice: BOOK!", "¡Muy bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El lápiz es ___.", "pasos": ["El lápiz es ___."]},
"ejemplo_solo": {"titulo": "Tu mochila", "planteo": "Sacá tus útiles y nombralos en inglés."},
"tip": {"titulo": "Tocá y decí", "texto": "Tocá cada útil al nombrarlo."},
"ojo": ["PEN es lapicera.", "PENCIL es lápiz."],
"resumen": [{"titulo": "PENCIL", "texto": "Lápiz."}, {"titulo": "BOOK", "texto": "Libro."}, {"titulo": "BAG", "texto": "Mochila."}],
"glosario": [{"palabra": "PENCIL", "significado": "Lápiz."}, {"palabra": "BAG", "significado": "Mochila."}],
"carpeta": ["Tomi saca un lápiz. ¿Cómo se dice?", "Tomi saca un libro. ¿Cómo se dice?", "Tomi muestra la goma y dice PEN. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("PENCIL"), acepta("BOOK"), acepta("RUBBER", "ERASER")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "PENCIL.", "solo": "Tus útiles.", "carpeta": ["PENCIL.", "BOOK.", "RUBBER."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a entender y hacer órdenes en inglés.",
"vas_a_ver": ["STAND UP y SIT DOWN", "OPEN y CLOSE", "Escuchar y hacer"],
"secciones": [
 S(1, "Arriba y abajo", [
  D("Orden", "Algo que nos piden hacer."),
  P("<b>STAND UP</b> es pararse. <b>SIT DOWN</b> es sentarse."),
  IMG("Órdenes", "Escuchá y hacé.", FG.tiras(["STAND UP = PARATE", "SIT DOWN = SENTATE"], numeros=False, cols=1)),
 ]),
 S(1, "Abrir y cerrar", [
  P("<b>OPEN YOUR BOOK</b> es abrir el libro. <b>CLOSE YOUR BOOK</b> es cerrarlo."),
  IMG("El libro", "Abrir y cerrar.", FG.tiras(["OPEN = ABRIR", "CLOSE = CERRAR"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que hace Sofi. Lo vas a usar en la carpeta."),
  IMG("Sofi en clase", "¿Qué orden escuchó?", FG.tiras(["SE PARA", "SE SIENTA", "ABRE EL LIBRO"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La maestra pide", "planteo": "La maestra dice: STAND UP!", "pasos": ["Sofi escucha.", "Sofi se para.", "¡Lo hizo bien!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Para sentarse: SIT ___.", "pasos": ["SIT ___."]},
"ejemplo_solo": {"titulo": "A jugar", "planteo": "Pedile a tu familia que te diga STAND UP y SIT DOWN."},
"tip": {"titulo": "Escuchá bien", "texto": "Primero escuchá, después hacé."},
"ojo": ["UP es arriba.", "DOWN es abajo."],
"resumen": [{"titulo": "STAND UP", "texto": "Pararse."}, {"titulo": "SIT DOWN", "texto": "Sentarse."}, {"titulo": "OPEN / CLOSE", "texto": "Abrir y cerrar."}],
"glosario": [{"palabra": "OPEN", "significado": "Abrir."}, {"palabra": "CLOSE", "significado": "Cerrar."}],
"carpeta": ["Sofi se para. ¿Qué orden escuchó?", "Sofi se sienta. ¿Qué orden escuchó?", "La maestra dice CLOSE y Tomi abre el libro. ¿Qué debía hacer?"],
"respuestas_carpeta": [acepta("STAND UP"), acepta("SIT DOWN"), acepta("CERRARLO", "CERRAR EL LIBRO", "CERRAR", "CLOSE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "DOWN.", "solo": "Tu juego.", "carpeta": ["STAND UP.", "SIT DOWN.", "CERRAR EL LIBRO."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a preguntar qué es algo y contestar sí o no.",
"vas_a_ver": ["IS IT A PEN?", "YES, IT IS", "NO, IT ISN'T"],
"secciones": [
 S(1, "¿Es una lapicera?", [
  D("Adivinar", "Decir qué es algo sin estar seguros."),
  P("Para adivinar preguntamos: <b>IS IT A PEN?</b> Quiere decir: ¿es una lapicera?"),
  IMG("La pregunta", "Para adivinar.", FG.tiras(["IS IT A PEN?", "IS IT A BOOK?"], numeros=False, cols=1)),
 ]),
 S(1, "Sí o no", [
  P("Si es, decimos <b>YES, IT IS</b>. Si no es, decimos <b>NO, IT ISN'T</b>."),
  IMG("Sí o no", "Dos respuestas.", FG.tiras(["YES, IT IS = SÍ, ES", "NO, IT ISN'T = NO, NO ES"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el juego de Sofi. Lo vas a usar en la carpeta."),
  IMG("¿Qué es?", "Sofi tiene algo en la mano.", FG.tiras(["SOFI TIENE UN LIBRO", "TOMI TIENE UN LÁPIZ"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Tomi adivina", "planteo": "Sofi esconde un lápiz.", "pasos": ["Tomi: IS IT A PEN?", "Sofi: NO, IT ISN'T.", "Tomi: IS IT A PENCIL? YES!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "IS IT A BOOK? YES, IT ___.", "pasos": ["YES, IT ___."]},
"ejemplo_solo": {"titulo": "A adivinar", "planteo": "Escondé un útil y que tu familia pregunte IS IT A…?"},
"tip": {"titulo": "Con la cabeza", "texto": "Mové la cabeza al decir YES o NO."},
"ojo": ["YES es sí.", "NO es no."],
"resumen": [{"titulo": "IS IT A…?", "texto": "¿Es un…?"}, {"titulo": "YES, IT IS", "texto": "Sí, es."}, {"titulo": "NO, IT ISN'T", "texto": "No, no es."}],
"glosario": [{"palabra": "YES", "significado": "Sí."}, {"palabra": "IS IT", "significado": "¿Es…?"}],
"carpeta": ["Sofi tiene un libro. IS IT A BOOK?", "Tomi tiene un lápiz. IS IT A BOOK?", "Es un libro y Tomi dice NO, IT ISN'T. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("YES, IT IS", "YES IT IS", "YES"), acepta("NO, IT ISN'T", "NO IT ISNT", "NO IT ISN'T", "NO"), acepta("YES, IT IS", "YES IT IS", "YES")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "IS.", "solo": "Tu juego.", "carpeta": ["YES, IT IS.", "NO, IT ISN'T.", "YES, IT IS."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a decir dónde están tus cosas en inglés.",
"vas_a_ver": ["IN: adentro", "ON: arriba", "WHERE IS IT?"],
"secciones": [
 S(1, "Adentro y arriba", [
  D("Lugar", "Dónde está una cosa."),
  P("<b>IN</b> es adentro. <b>ON</b> es arriba, apoyado."),
  IMG("Dónde está", "Dos lugares.", FG.tiras(["IN THE BAG = EN LA MOCHILA", "ON THE TABLE = EN LA MESA"], numeros=False, cols=1)),
 ]),
 S(1, "¿Dónde está?", [
  P("Preguntamos: <b>WHERE IS IT?</b> Quiere decir: ¿dónde está?"),
  IMG("La pregunta", "Para buscar.", FG.tiras(["WHERE IS IT?", "IT IS IN THE BAG."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuarto de Tomi. Lo vas a usar en la carpeta."),
  IMG("El cuarto de Tomi", "¿Dónde están sus cosas?", FG.tiras(["EL LIBRO: ARRIBA DE LA MESA", "EL LÁPIZ: ADENTRO DE LA MOCHILA"], numeros=True, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "¿Dónde está el lápiz?", "planteo": "Sofi busca su lápiz.", "pasos": ["Sofi: WHERE IS IT?", "Tomi mira la mochila.", "Tomi: IT IS IN THE BAG!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El libro está arriba de la mesa: ___ THE TABLE.", "pasos": ["___ THE TABLE."]},
"ejemplo_solo": {"titulo": "A esconder", "planteo": "Poné un lápiz IN o ON y decí dónde está."},
"tip": {"titulo": "Con las manos", "texto": "IN: mano adentro. ON: mano arriba."},
"ojo": ["IN es adentro.", "ON es arriba."],
"resumen": [{"titulo": "IN", "texto": "Adentro."}, {"titulo": "ON", "texto": "Arriba."}, {"titulo": "WHERE IS IT?", "texto": "¿Dónde está?"}],
"glosario": [{"palabra": "IN", "significado": "Adentro."}, {"palabra": "WHERE", "significado": "Dónde."}],
"carpeta": ["El lápiz está adentro de la mochila. ¿IN u ON?", "El libro está arriba de la mesa. ¿IN u ON?", "El lápiz está en la mochila y Tomi dice ON. ¿Qué debería decir?"],
"respuestas_carpeta": [acepta("IN"), acepta("ON"), acepta("IN", "IN THE BAG")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "ON.", "solo": "Tu juego.", "carpeta": ["IN.", "ON.", "IN."]},
}

ACT = {
"1": [MC("LIBRO EN INGLÉS ES…", ["BOOK", "BAG", "PEN"], "BOOK", "BOOK ES LIBRO.", n="recordar"),
      MC("TOMI GUARDA TODO EN LA MOCHILA. ¿CÓMO SE DICE?", ["BAG", "BOOK", "PENCIL"], "BAG", "MOCHILA ES BAG.", n="aplicar"),
      MC("SOFI ESCRIBE CON UN LÁPIZ. ¿QUÉ USA?", ["PENCIL", "RUBBER", "BAG"], "PENCIL", "LÁPIZ ES PENCIL.", n="aplicar")],
"2": [MC("LA MAESTRA DICE SIT DOWN. ¿QUÉ HACÉS?", ["ME SIENTO", "ME PARO", "ABRO EL LIBRO"], "ME SIENTO", "SIT DOWN ES SENTARSE.", n="aplicar"),
      MC("LA MAESTRA DICE OPEN YOUR BOOK. ¿QUÉ HACÉS?", ["ABRO EL LIBRO", "CIERRO EL LIBRO", "ME SIENTO"], "ABRO EL LIBRO", "OPEN ES ABRIR.", n="aplicar")],
"3": [MC("ES UN LIBRO. IS IT A BOOK?", ["YES, IT IS", "NO, IT ISN'T", "GOODBYE"], "YES, IT IS", "SÍ, ES UN LIBRO.", n="aplicar"),
      MC("ES UNA GOMA. TOMI DICE YES, IT IS A PEN. ¿QUÉ ESTÁ MAL?", ["NO ES UNA LAPICERA", "ESTÁ BIEN", "ES UN LIBRO"], "NO ES UNA LAPICERA", "ES UNA GOMA.", n="error")],
"4": [MC("EL LÁPIZ ESTÁ ADENTRO DE LA MOCHILA. ¿DÓNDE ESTÁ?", ["IN THE BAG", "ON THE BAG", "IN THE BOOK"], "IN THE BAG", "ADENTRO ES IN.", n="aplicar"),
      ORD("ORDENÁ LA PREGUNTA.", ["IT", "WHERE", "IS"], ["WHERE", "IS", "IT"], "WHERE IS IT?", n="aplicar")],
"5": [MC("RELÁMPAGO. MOCHILA EN INGLÉS ES…", ["BAG", "BOOK", "PEN"], "BAG", "BAG.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. PARARSE ES…", ["STAND UP", "SIT DOWN", "CLOSE"], "STAND UP", "STAND UP.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL LIBRO ESTÁ ARRIBA DE LA MESA. ES…", ["ON", "IN", "UP"], "ON", "ON.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ES UN LÁPIZ. IS IT A PENCIL?", ["YES, IT IS", "NO, IT ISN'T", "HELLO"], "YES, IT IS", "YES, IT IS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("LÁPIZ EN INGLÉS ES…", ["PENCIL", "PEN", "BOOK"], "PENCIL", "PENCIL ES LÁPIZ.", n="recordar")],
 [1, SA("TOMI LEE UN LIBRO. ESCRIBÍ LIBRO EN INGLÉS.", acepta("BOOK"), "BOOK.", n="aplicar")],
 [1, MC("SOFI MUESTRA LA MOCHILA Y DICE BOOK. ¿QUÉ ESTÁ MAL?", ["ES BAG", "ESTÁ BIEN", "ES PEN"], "ES BAG", "MOCHILA ES BAG.", n="error")],
 [2, MC("SIT DOWN QUIERE DECIR…", ["SENTATE", "PARATE", "ABRÍ"], "SENTATE", "SIT DOWN ES SENTARSE.", n="recordar")],
 [2, MC("LA MAESTRA DICE STAND UP. ¿QUÉ HACÉS?", ["ME PARO", "ME SIENTO", "CIERRO EL LIBRO"], "ME PARO", "STAND UP ES PARARSE.", n="aplicar")],
 [2, MC("LA MAESTRA DICE CLOSE YOUR BOOK Y SOFI LO ABRE. ¿QUÉ ESTÁ MAL?", ["DEBÍA CERRARLO", "ESTÁ BIEN", "DEBÍA PARARSE"], "DEBÍA CERRARLO", "CLOSE ES CERRAR.", n="error")],
 [3, MC("IS IT A PEN QUIERE DECIR…", ["¿ES UNA LAPICERA?", "¿DÓNDE ESTÁ?", "¿DE QUÉ COLOR ES?"], "¿ES UNA LAPICERA?", "PEN ES LAPICERA.", n="recordar")],
 [3, SA("ES UN LIBRO. IS IT A BOOK? ESCRIBÍ SÍ EN INGLÉS.", acepta("YES", "YES, IT IS", "YES IT IS"), "YES, IT IS.", n="aplicar")],
 [3, MC("ES UN LÁPIZ. IS IT A BOOK?", ["NO, IT ISN'T", "YES, IT IS", "IT IS RED"], "NO, IT ISN'T", "ES UN LÁPIZ, NO UN LIBRO.", n="aplicar")],
 [4, MC("WHERE IS IT QUIERE DECIR…", ["¿DÓNDE ESTÁ?", "¿QUÉ ES?", "¿CUÁNTOS HAY?"], "¿DÓNDE ESTÁ?", "WHERE ES DÓNDE.", n="recordar")],
 [4, SA("EL LIBRO ESTÁ ARRIBA DE LA MESA. ESCRIBÍ IN U ON.", acepta("ON", "ON THE TABLE"), "ON.", n="aplicar")],
 [4, MC("LA GOMA ESTÁ ADENTRO DE LA MOCHILA Y TOMI DICE ON. ¿QUÉ DEBERÍA DECIR?", ["IN", "UP", "YES"], "IN", "ADENTRO ES IN.", n="error")],
]
M = {"subject_id": "e2d48bb4-83ea-4f78-b7f0-ba50b1154664", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: My Things", "examen_titulo": "Nivel jefe: My Things",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
