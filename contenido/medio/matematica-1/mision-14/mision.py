# -*- coding: utf-8 -*-
"""Matemática 1 (Nivel Medio, 1.º año) · Misión 14 · Problemas de resta. Genera mision-14.json.
Regla de primeros años (tools/medio/primeros_anios.py). Metáfora: el cumple de Tomi (globos, golosinas y regalos).
Niveles: 1 quitar y perder · 2 comparar con la resta · 3 cuánto falta · 4 armar problemas de resta. Todo hasta 20."""
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
"objetivo": "Vas a resolver problemas de quitar y perder.",
"vas_a_ver": ["Problemas donde se va algo", "Hacer la resta", "Responder"],
"secciones": [
 S(1, "Se pinchan globos", [
  P("En el cumple de Tomi hay <b>8</b> globos. Se pinchan <b>3</b>. ¿Cuántos quedan?"),
  IMG("Quedan 5", "8 − 3 = 5.", FG.sacar("globo", 8, 3, "8 − 3 = 5")),
 ]),
 S(1, "Quitar y perder", [
  D("Problema de resta", "Una historia donde se <b>va</b> algo: se pierde, se come o se regala."),
  P("Tomi tiene <b>10</b> caramelos. Come <b>4</b>. <b>10 − 4 = 6</b>."),
  IMG("Caramelos", "Le quedan 6.", FG.sacar("caramelo", 10, 4, "10 − 4 = 6")),
 ]),
 S(2, "Para practicar", [
  P("Mirá las manzanas. Las vas a usar en la carpeta."),
  IMG("Manzanas", "Las tachadas se comen.", FG.sacar("manzana", 9, 2, "¿CUÁNTAS QUEDAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "Figuritas", "planteo": "Sofi tiene 7 figuritas. Regala 2. ¿Cuántas le quedan?", "pasos": ["Se van: es una resta.", "7 − 2 = 5.", "Le quedan 5 figuritas."]},
"ejemplo_incompleto": {"titulo": "Pelotas", "planteo": "Completá.", "pasos": ["Hay 6 pelotas. Se pierden 4.", "6 − 4 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Tenés 12 lápices. Prestás 2. ¿Cuántos te quedan?"},
"tip": {"titulo": "¿Se va algo?", "texto": "Si se pierde, se come o se regala, restá."},
"ojo": ["Primero va lo que había.", "Quedan menos que al principio."],
"resumen": [{"titulo": "Había", "texto": "El primer número."}, {"titulo": "Se va", "texto": "Restamos."}, {"titulo": "Quedan", "texto": "Menos que antes."}],
"glosario": [{"palabra": "Perder", "significado": "Ya no tener algo."}, {"palabra": "Quedar", "significado": "Lo que sigue estando."}],
"carpeta": ["¿Cuántas manzanas había?", "¿Cuántas se comen?", "¿Cuántas quedan?"],
"respuestas_carpeta": [["9"], ["2"], ["7"]],
"soluciones": {"incompleto": "2.", "solo": "10 lápices.", "carpeta": ["9.", "2.", "7."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a comparar con una resta: cuántos más o menos.",
"vas_a_ver": ["Dos cantidades", "Cuántos más tiene uno", "La resta compara"],
"secciones": [
 S(1, "¿Quién tiene más?", [
  P("Tomi tiene <b>9</b> regalos. Sofi tiene <b>6</b>. ¿Cuántos más tiene Tomi?"),
  IMG("Uno con uno", "Sobran 3.", FG.parejas(("estrella", 9), ("estrella", 6), "TOMI TIENE 3 MÁS")),
 ]),
 S(1, "La resta compara", [
  D("Comparar con la resta", "Al grande le restamos el chico. Así sabemos <b>cuántos más</b>."),
  P("<b>9 − 6 = 3</b>. Tomi tiene 3 más. Sofi tiene 3 menos."),
  IMG("La cuenta", "9 − 6 = 3.", FG.cuentas([("9 − 6", 3)])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los grupos. Los vas a usar en la carpeta."),
  IMG("Pelotas", "Uní uno con uno.", FG.parejas(("pelota", 8), ("pelota", 5), "¿CUÁNTAS MÁS?")),
 ]),
],
"ejemplo_completo": {"titulo": "Autitos", "planteo": "Sofi tiene 10. Tomi tiene 7.", "pasos": ["Grande menos chico.", "10 − 7 = 3.", "Sofi tiene 3 más."]},
"ejemplo_incompleto": {"titulo": "Globos", "planteo": "Completá.", "pasos": ["Tomi: 8. Sofi: 4.", "8 − 4 = ___ ."]},
"ejemplo_solo": {"titulo": "Tus cosas", "planteo": "Tenés 6 lápices y 11 hojas. ¿Cuántas hojas más tenés?"},
"tip": {"titulo": "Grande menos chico", "texto": "Para comparar, restá el chico al grande."},
"ojo": ["No sumes: comparar es restar.", "Siempre grande menos chico."],
"resumen": [{"titulo": "Comparar", "texto": "¿Cuántos más?"}, {"titulo": "Restar", "texto": "Grande menos chico."}, {"titulo": "Ejemplo", "texto": "9 − 6 = 3."}],
"glosario": [{"palabra": "Comparar", "significado": "Ver la diferencia."}, {"palabra": "Diferencia", "significado": "Cuántos más hay."}],
"carpeta": ["¿Cuántas pelotas hay arriba?", "¿Cuántas pelotas hay abajo?", "¿Cuántas más hay arriba?"],
"respuestas_carpeta": [["8"], ["5"], ["3"]],
"soluciones": {"incompleto": "4.", "solo": "5 hojas más.", "carpeta": ["8.", "5.", "3."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a calcular cuánto falta con una resta.",
"vas_a_ver": ["Tengo y necesito", "Restar para saber cuánto falta", "Comprobar con una suma"],
"secciones": [
 S(1, "Faltan vasos", [
  P("Vienen <b>10</b> chicos al cumple. Hay <b>6</b> vasos. ¿Cuántos faltan?"),
  IMG("Completamos", "Faltan 4.", FG.marco10(6, "vaso", texto="10 − 6 = 4")),
 ]),
 S(1, "Restar para saber", [
  D("Cuánto falta", "Lo que necesito menos lo que tengo."),
  P("<b>10 − 6 = 4</b>. Comprobamos: <b>6 + 4 = 10</b>."),
  IMG("Comprobar", "6 y 4 más son 10.", FG.agregar("vaso", 6, 4, "6 + 4 = 10")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro de 10", "Contá los vacíos.", FG.marco10(3, "manzana", texto="¿CUÁNTOS FALTAN?")),
 ]),
],
"ejemplo_completo": {"titulo": "Sillas", "planteo": "Se necesitan 9 sillas. Hay 5.", "pasos": ["9 − 5 = 4.", "Comprobamos: 5 + 4 = 9.", "Faltan 4 sillas."]},
"ejemplo_incompleto": {"titulo": "Platos", "planteo": "Completá.", "pasos": ["Se necesitan 8. Hay 2.", "8 − 2 = ___ ."]},
"ejemplo_solo": {"titulo": "Tu álbum", "planteo": "El álbum tiene 20 figuritas. Tenés 15. ¿Cuántas te faltan?"},
"tip": {"titulo": "Comprobá", "texto": "Sumá lo que tenés y lo que falta."},
"ojo": ["Necesito menos tengo.", "Si sumás, tiene que dar lo que necesitás."],
"resumen": [{"titulo": "Necesito", "texto": "El grande."}, {"titulo": "Tengo", "texto": "El chico."}, {"titulo": "Falta", "texto": "Grande menos chico."}],
"glosario": [{"palabra": "Necesitar", "significado": "Hacer falta."}, {"palabra": "Comprobar", "significado": "Ver si está bien."}],
"carpeta": ["¿Cuántas manzanas hay?", "¿Cuántos lugares tiene el cuadro?", "¿Cuántas manzanas faltan?"],
"respuestas_carpeta": [["3"], ["10"], ["7"]],
"soluciones": {"incompleto": "6.", "solo": "5 figuritas.", "carpeta": ["3.", "10.", "7."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a inventar tus propios problemas de resta.",
"vas_a_ver": ["Las partes del problema", "Algo que se va", "La pregunta"],
"secciones": [
 S(1, "Una historia que resta", [
  P("Tomi tiene <b>7</b> globos. Regala <b>3</b>. ¿Cuántos le quedan?"),
  IMG("El problema", "7 − 3 = 4.", FG.sacar("globo", 7, 3, "7 − 3 = 4")),
 ]),
 S(1, "Inventar", [
  D("Problema de resta", "Quién, qué tiene, qué <b>se va</b> y la pregunta."),
  P("Palabras que restan: <b>pierde, come, regala, se rompe, se va</b>."),
  IMG("Palabras", "Todas restan.", FG.sacar("estrella", 6, 2, "6 − 2 = 4")),
 ]),
 S(2, "Para practicar", [
  P("Mirá el dibujo. Lo vas a usar en la carpeta."),
  IMG("Pelotas", "Inventá la historia.", FG.sacar("pelota", 10, 5, "10 − 5 = ?")),
 ]),
],
"ejemplo_completo": {"titulo": "Mi problema", "planteo": "Con 9 y 4.", "pasos": ["Sofi tiene 9 galletitas.", "Come 4.", "¿Cuántas le quedan? 9 − 4 = 5."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Escribí la pregunta.", "pasos": ["Tomi tiene 8 peces. Regala 3.", "¿___ ?"]},
"ejemplo_solo": {"titulo": "Tu problema", "planteo": "Inventá un problema con la cuenta 10 − 6."},
"tip": {"titulo": "Algo se va", "texto": "En un problema de resta, algo se va."},
"ojo": ["Sin pregunta no es un problema.", "El número grande va primero."],
"resumen": [{"titulo": "Quién", "texto": "Tomi, Sofi…"}, {"titulo": "Se va", "texto": "Pierde, come…"}, {"titulo": "Pregunta", "texto": "¿Cuántos quedan?"}],
"glosario": [{"palabra": "Regalar", "significado": "Dar algo."}, {"palabra": "Romperse", "significado": "Dejar de servir."}],
"carpeta": ["¿Cuántas pelotas había?", "¿Cuántas pelotas se van?", "¿Cuánto es 10 − 5?"],
"respuestas_carpeta": [["10"], ["5"], ["5"]],
"soluciones": {"incompleto": "¿Cuántos peces le quedan?", "solo": "Por ejemplo: tengo 10 caramelos y como 6. ¿Cuántos quedan? 4.", "carpeta": ["10.", "5.", "5."]},
}

ACT = {
"1": [N("HAY 8 GLOBOS. SE PINCHAN 3. ¿CUÁNTOS QUEDAN?", 5, "8 − 3 = 5."),
      N("TOMI TIENE 10 CARAMELOS. COME 4. ¿CUÁNTOS LE QUEDAN?", 6, "10 − 4 = 6.")],
"2": [N("TOMI TIENE 9 REGALOS Y SOFI 6. ¿CUÁNTOS MÁS TIENE TOMI?", 3, "9 − 6 = 3."),
      MC("PARA COMPARAR, HACEMOS…", ["GRANDE MENOS CHICO", "CHICO MENOS GRANDE", "UNA SUMA"], "GRANDE MENOS CHICO", "LA RESTA COMPARA.")],
"3": [N("VIENEN 10 CHICOS. HAY 6 VASOS. ¿CUÁNTOS VASOS FALTAN?", 4, "10 − 6 = 4."),
      N("EL ÁLBUM TIENE 20 FIGURITAS. TENÉS 17. ¿CUÁNTAS FALTAN?", 3, "20 − 17 = 3.")],
"4": [MC("¿QUÉ PALABRA NOS DICE QUE HAY QUE RESTAR?", ["PIERDE", "GANA", "LE DAN"], "PIERDE", "SI SE PIERDE, RESTAMOS."),
      MC("¿QUÉ PROBLEMA SE RESUELVE CON 7 − 2?", ["TENGO 7 Y REGALO 2", "TENGO 7 Y ME DAN 2", "TENGO 2"], "TENGO 7 Y REGALO 2", "SE VA ALGO: RESTO.")],
"5": [N("RELÁMPAGO. HAY 6 GALLETITAS. COMEN 2. ¿CUÁNTAS QUEDAN?", 4, "6 − 2 = 4.", tiempo=30),
      N("RELÁMPAGO. SOFI TIENE 12 Y TOMI 10. ¿CUÁNTOS MÁS TIENE SOFI?", 2, "12 − 10 = 2.", tiempo=30),
      N("RELÁMPAGO. NECESITO 9. TENGO 5. ¿CUÁNTOS FALTAN?", 4, "9 − 5 = 4.", tiempo=30),
      MC("RELÁMPAGO. SI ALGO SE ROMPE, HACEMOS UNA…", ["RESTA", "SUMA"], "RESTA", "SE VA ALGO.", tiempo=30)],
}
EXAMEN = [
 [1, N("HAY 9 PELOTAS. SE PIERDEN 4. ¿CUÁNTAS QUEDAN?", 5, "9 − 4 = 5.")],
 [1, N("SOFI TIENE 7 FLORES. REGALA 7. ¿CUÁNTAS LE QUEDAN?", 0, "7 − 7 = 0.")],
 [1, MC("SI COMEMOS CARAMELOS, NOS QUEDAN…", ["MÁS", "MENOS"], "MENOS", "COMER ES QUITAR.")],
 [2, N("TOMI TIENE 10 AUTITOS Y SOFI 4. ¿CUÁNTOS MÁS TIENE TOMI?", 6, "10 − 4 = 6.")],
 [2, N("HAY 7 NENES Y 9 NENAS. ¿CUÁNTAS NENAS MÁS HAY?", 2, "9 − 7 = 2.")],
 [2, MC("PARA SABER CUÁNTOS MÁS, HACEMOS UNA…", ["RESTA", "SUMA"], "RESTA", "LA RESTA COMPARA.")],
 [3, N("SE NECESITAN 8 SILLAS. HAY 3. ¿CUÁNTAS FALTAN?", 5, "8 − 3 = 5.")],
 [3, N("NECESITO 10 PLATOS. TENGO 9. ¿CUÁNTOS FALTAN?", 1, "10 − 9 = 1.")],
 [3, MC("SI 10 − 6 = 4, ¿CÓMO COMPRUEBO?", ["6 + 4 = 10", "6 − 4 = 2", "10 + 4 = 14"], "6 + 4 = 10", "SUMO LO QUE TENGO Y LO QUE FALTA.")],
 [4, MC("¿QUÉ PROBLEMA SE RESUELVE CON 8 − 5?", ["TENGO 8 Y PIERDO 5", "TENGO 8 Y GANO 5", "TENGO 5"], "TENGO 8 Y PIERDO 5", "SE VA ALGO: RESTO.")],
 [4, MC("¿QUÉ PALABRA RESTA?", ["SE ROMPE", "LE REGALAN", "JUNTA"], "SE ROMPE", "SI SE ROMPE, YA NO ESTÁ.")],
 [4, N("TOMI TIENE 11 FIGURITAS Y PIERDE 1. ¿CUÁNTAS TIENE?", 10, "11 − 1 = 10.")],
 [4, N("HAY 15 GLOBOS Y SE VUELAN 5. ¿CUÁNTOS QUEDAN?", 10, "15 − 5 = 10.")],
]
M = {"subject_id": "37dacb79-7f3f-4f6f-a520-5dd41b97ebb3", "tema": 14, "estilo": "primeros",
     "practica": "Práctica general: problemas de resta", "examen_titulo": "Nivel jefe: problemas de resta",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-14.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
