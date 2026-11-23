# -*- coding: utf-8 -*-
"""Matemática 2 (Nivel Medio, 2.º año) · Misión 1 · La serie numérica hasta 200. Genera mision-1.json.
Regla de primeros años (tools/medio/primeros_anios.py): frases cortas, un dibujo por sección; el PDF sale solo en imprenta mayúscula.
Metáfora de la misión: la fábrica de alfajores de la abuela Rosa (igual que en las clases animadas, clases.py).
Niveles: 1 contar hasta 100 y más · 2 hasta 200 · 3 escalas de 10 en 10 · 4 series que suben y bajan."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), "matematica-1"))  # dibujos compartidos del Medio
import figuras as FG

D = lambda t, x: {"tipo": "definicion", "titulo": t, "texto": x}
P = lambda x: {"tipo": "parrafo", "texto": x}
IMG = lambda t, pie, b64: {"tipo": "imagen", "imagen_tipo": "ilustracion", "titulo": t, "texto": pie, "png_base64": b64}
S = lambda e, t, b: {"etapa": e, "titulo": t, "bloques": b}
MC = lambda p, o, ok, e, **k: {"t": "multiple_choice", "p": p, "o": o, "r": {"correcta": ok}, "e": e, **k}
N = lambda p, r, e, **k: {"t": "numeric", "p": p, "o": {}, "r": {"acepta": [r]}, "e": e, **k}
ORD = lambda p, desorden, orden, e, **k: {"t": "ordering", "p": p, "o": desorden, "r": {"orden": orden}, "e": e, **k}
ESTILO = {"estilo": "primeros"}

N1 = {**ESTILO,
"objetivo": "Vas a contar hasta 100 y seguir después.",
"vas_a_ver": ["Paquetes de 10", "10 paquetes son 100", "Después del 100: 101, 102…"],
"secciones": [
 S(1, "Paquetes de 10", [
  P("La abuela Rosa cuenta sus alfajores."),
  P("Cada paquete tiene <b>10</b> alfajores: es una <b>decena</b>."),
  D("Cien", "<b>10</b> paquetes de 10 son <b>100</b> alfajores."),
  IMG("Diez paquetes", "10 paquetes de 10: 100 alfajores.", FG.bloques(0, 10, 0)),
 ]),
 S(1, "Después del 100", [
  P("Después del 99 viene el <b>100</b>."),
  P("Y después del 100 seguimos: <b>101, 102, 103…</b>"),
  IMG("El tren sigue", "Después del 100 viene el 101.", FG.tren(98, 105)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cuadro. Lo vas a usar en la carpeta."),
  IMG("Cuadro hasta 100", "Faltan algunos números.", FG.cuadro(100, faltan=(45, 78, 100))),
 ]),
],
"ejemplo_completo": {"titulo": "Paquetes y sueltos", "planteo": "Rosa tiene 10 paquetes y 2 sueltos.", "pasos": ["10 paquetes son 100.", "Sumamos los sueltos: 101, 102.", "Son 102 alfajores."]},
"ejemplo_incompleto": {"titulo": "Seguí contando", "planteo": "Completá.", "pasos": ["98, 99, ___ , 101.", "103, 104, ___ , 106."]},
"ejemplo_solo": {"titulo": "Después del 109", "planteo": "¿Qué número viene después del 109?"},
"tip": {"titulo": "No te frenes en el 100", "texto": "Después del 100, seguí contando: 101, 102…"},
"ojo": ["Después del 100 viene el 101, no el 200.", "Ciento uno se escribe 101, no 1001."],
"resumen": [{"titulo": "Decena", "texto": "Un paquete de 10."}, {"titulo": "Cien", "texto": "10 paquetes de 10."}, {"titulo": "Después del 100", "texto": "101, 102, 103…"}],
"glosario": [{"palabra": "Decena", "significado": "Un grupo de 10."}, {"palabra": "Cien", "significado": "Diez decenas: 100."}],
"carpeta": ["En el cuadro, ¿qué número falta después del 44?", "¿Qué número falta después del 99?", "Rosa tiene 10 paquetes y 3 sueltos. ¿Cuántos alfajores son?"],
"carpeta_nivel": ["recordar", "recordar", "aplicar"],
"respuestas_carpeta": [["45"], ["100", "cien"], ["103"]],
"soluciones": {"incompleto": "100. 105.", "solo": "110.", "carpeta": ["45.", "100.", "103: 100 y 3 sueltos."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a contar números hasta el 200.",
"vas_a_ver": ["Una caja de 100 y más", "Contar cajas, paquetes y sueltos", "Del 199 al 200"],
"secciones": [
 S(1, "Una caja y más", [
  P("Una caja de Rosa tiene <b>100</b> alfajores."),
  P("Primero la caja, después los paquetes y al final los sueltos."),
  P("1 caja, 4 paquetes y 3 sueltos son <b>143</b>."),
  IMG("El pedido de 143", "1 caja, 4 paquetes y 3 sueltos.", FG.bloques(1, 4, 3)),
 ]),
 S(1, "Hasta el 200", [
  D("Doscientos", "Dos cajas de 100 son <b>200</b> alfajores."),
  P("Después del 199 viene el <b>200</b>."),
  IMG("El tren llega al 200", "193, 194… hasta el 200.", FG.tren(193, 200)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el pedido. Lo vas a usar en la carpeta."),
  IMG("Otro pedido", "Contá la caja, los paquetes y los sueltos.", FG.bloques(1, 6, 2)),
 ]),
],
"ejemplo_completo": {"titulo": "Un pedido", "planteo": "Hay 1 caja, 2 paquetes y 5 sueltos.", "pasos": ["La caja: 100.", "Los paquetes: 110, 120.", "Los sueltos: 121, 122, 123, 124, 125.", "Son 125 alfajores."]},
"ejemplo_incompleto": {"titulo": "Cerca del 200", "planteo": "Completá.", "pasos": ["196, 197, ___ , 199.", "198, 199, ___ ."]},
"ejemplo_solo": {"titulo": "Dos cajas", "planteo": "¿Cuántos alfajores hay en 2 cajas de 100?"},
"tip": {"titulo": "Contá en orden", "texto": "Primero la caja, después paquetes, al final sueltos."},
"ojo": ["Después del 199 viene el 200.", "Ciento cincuenta es 150, no 10050."],
"resumen": [{"titulo": "Caja", "texto": "100 alfajores."}, {"titulo": "Contar", "texto": "Caja, paquetes y sueltos."}, {"titulo": "200", "texto": "Dos cajas de 100."}],
"glosario": [{"palabra": "Centena", "significado": "Un grupo de 100."}, {"palabra": "Doscientos", "significado": "Dos centenas: 200."}],
"carpeta": ["¿Cuántas cajas de 100 hay en el pedido?", "¿Cuántos alfajores hay en total en el pedido?", "Lucía dice que después del 199 viene el 1100. ¿Qué número viene?"],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"respuestas_carpeta": [["1", "una"], ["162"], ["200", "doscientos"]],
"soluciones": {"incompleto": "198. 200.", "solo": "200.", "carpeta": ["1 caja.", "162: 100, 160 y 2 sueltos.", "200. Lucía se equivocó."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a contar de 10 en 10 hasta el 200.",
"vas_a_ver": ["Saltar de 10 en 10", "Qué cifra cambia", "Escalas que no empiezan en 0"],
"secciones": [
 S(1, "Saltar de 10 en 10", [
  P("Contar de 10 en 10 es sumar un paquete."),
  P("110, 120, 130, 140… hasta el <b>200</b>."),
  IMG("El tren de 10 en 10", "Cada vagón suma un paquete.", FG.tren_paso(110, 200, 10)),
 ]),
 S(1, "Qué cambia", [
  D("Escala de 10", "En cada salto cambia la cifra de las <b>decenas</b>."),
  P("Las unidades no cambian: 103, 113, 123."),
  IMG("Siempre termina en 3", "103, 113, 123… La última cifra queda igual.", FG.tren_paso(103, 193, 10)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el tren. Lo vas a usar en la carpeta."),
  IMG("Vagones vacíos", "Faltan dos números.", FG.tren_paso(120, 200, 10, faltan=(150, 180))),
 ]),
],
"ejemplo_completo": {"titulo": "Desde el 125", "planteo": "Contá de 10 en 10 desde el 125.", "pasos": ["Sumamos un paquete: 135.", "Otro paquete: 145.", "Otro más: 155.", "La última cifra siempre es 5."]},
"ejemplo_incompleto": {"titulo": "Seguí la escala", "planteo": "Completá.", "pasos": ["160, 170, ___ , 190.", "107, 117, ___ , 137."]},
"ejemplo_solo": {"titulo": "Desde el 142", "planteo": "Contá de 10 en 10: 142, 152, ¿qué sigue?"},
"tip": {"titulo": "Mirá las decenas", "texto": "De 10 en 10, sube la cifra del medio."},
"ojo": ["De 10 en 10, 190 sigue con 200.", "No cambies las unidades: 113 sigue con 123."],
"resumen": [{"titulo": "De 10 en 10", "texto": "Sumar un paquete."}, {"titulo": "Cambia", "texto": "La cifra de las decenas."}, {"titulo": "No cambia", "texto": "La cifra de las unidades."}],
"glosario": [{"palabra": "Escala", "significado": "Contar saltando siempre lo mismo."}, {"palabra": "Salto", "significado": "Lo que sumamos cada vez."}],
"carpeta": ["En el tren, ¿qué número falta después del 140?", "¿Qué número falta después del 170?", "Contá de 10 en 10 desde el 135. ¿Qué número sigue?"],
"carpeta_nivel": ["recordar", "recordar", "aplicar"],
"respuestas_carpeta": [["150"], ["180"], ["145"]],
"soluciones": {"incompleto": "180. 127.", "solo": "162.", "carpeta": ["150.", "180.", "145."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a seguir series que suben y series que bajan.",
"vas_a_ver": ["Series que suben", "Series que bajan", "Encontrar el número que falta"],
"secciones": [
 S(1, "Series que suben", [
  P("Una serie <b>sube</b> cuando sumamos cada vez."),
  P("De 1 en 1: 150, 151, 152, 153."),
  IMG("La serie sube", "Cada salto suma 1.", FG.recta_num(150, 158, flechas=[(150, 151), (151, 152), (152, 153)])),
 ]),
 S(1, "Series que bajan", [
  D("Serie que baja", "Una serie <b>baja</b> cuando restamos cada vez."),
  P("De 10 en 10 para atrás: 200, 190, 180, 170."),
  IMG("Los camiones bajan", "Cada camión lleva 10 menos.", FG.camiones([200, 190, 180, 170])),
 ]),
 S(2, "Para practicar", [
  P("Mirá los camiones. Los vas a usar en la carpeta."),
  IMG("Seguí la serie", "La serie baja de 10 en 10.", FG.camiones([190, 180, 170])),
 ]),
],
"ejemplo_completo": {"titulo": "Una serie que baja", "planteo": "Seguí: 125, 124, 123…", "pasos": ["Cada vez resta 1.", "Después del 123 va el 122.", "Después, el 121."]},
"ejemplo_incompleto": {"titulo": "Sube o baja", "planteo": "Completá.", "pasos": ["140, 150, 160, ___ .", "180, 170, 160, ___ ."]},
"ejemplo_solo": {"titulo": "Para atrás", "planteo": "Seguí la serie: 110, 109, 108, ¿qué sigue?"},
"tip": {"titulo": "Mirá dos números", "texto": "Si crece, sube. Si achica, baja."},
"ojo": ["Antes del 100 viene el 99.", "Una serie que baja va del más grande al más chico."],
"resumen": [{"titulo": "Sube", "texto": "Sumamos cada vez."}, {"titulo": "Baja", "texto": "Restamos cada vez."}, {"titulo": "El salto", "texto": "Siempre es igual."}],
"glosario": [{"palabra": "Serie", "significado": "Números que siguen una regla."}, {"palabra": "Bajar", "significado": "Restar cada vez."}],
"carpeta": ["Seguí la serie que baja: 190, 180, 170, ___", "La serie 120, 130, 140, ¿sube o baja?", "Tomi escribió 200, 190, 170. ¿Qué número se olvidó?"],
"carpeta_nivel": ["aplicar", "analizar", "error"],
"respuestas_carpeta": [["160"], ["sube", "sube de 10 en 10"], ["180"]],
"soluciones": {"incompleto": "170. 150.", "solo": "107.", "carpeta": ["160.", "Sube: suma 10 cada vez.", "180: va entre el 190 y el 170."]},
}

ACT = {
"1": [N("📦 10 PAQUETES DE 10. ¿CUÁNTOS ALFAJORES SON?", 100, "10, 20, 30… 100.", n="recordar"),
      N("ROSA TIENE 100 ALFAJORES Y LE TRAEN 4 MÁS. ¿CUÁNTOS TIENE?", 104, "101, 102, 103, 104.", n="aplicar")],
"2": [N("1 CAJA, 5 PAQUETES Y 3 SUELTOS. ¿CUÁNTOS SON?", 153, "100 + 50 + 3 = 153.", n="aplicar"),
      MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 199?", ["200", "1.100", "190"], "200", "DESPUÉS DEL 199 VIENE EL 200.", n="recordar")],
"3": [MC("DE 10 EN 10: 130, 140, 150, ___", ["160", "151", "250"], "160", "SUMAMOS UN PAQUETE.", n="aplicar"),
      N("DE 10 EN 10 DESDE EL 104: 104, 114, ___", 124, "LA ÚLTIMA CIFRA SIGUE SIENDO 4.", n="aplicar")],
"4": [MC("LA SERIE 160, 150, 140, ¿SUBE O BAJA?", ["SUBE", "BAJA"], "BAJA", "CADA VEZ RESTA 10.", n="analizar"),
      ORD("ORDENÁ PARA QUE LA SERIE BAJE.", ["180", "200", "190"], ["200", "190", "180"], "DEL MÁS GRANDE AL MÁS CHICO.", n="aplicar")],
"5": [N("RELÁMPAGO. ¿QUÉ VIENE DESPUÉS DEL 100?", 101, "100, 101.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁNTO ES 2 CAJAS DE 100?", ["200", "20"], "200", "100 Y 100 SON 200.", tiempo=30, n="recordar"),
      N("RELÁMPAGO. DE 10 EN 10: 170, 180, ___", 190, "SUMAMOS 10.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. 150, 149, 148… ¿QUÉ SIGUE?", ["147", "149"], "147", "BAJA DE 1 EN 1.", tiempo=40, n="aplicar")],
}
EXAMEN = [
 [1, N("¿CUÁNTO ES 10 PAQUETES DE 10?", 100, "10 DECENAS SON 100.", n="recordar")],
 [1, MC("¿QUÉ NÚMERO VIENE DESPUÉS DEL 109?", ["110", "1.010", "100"], "110", "109, 110.", n="recordar")],
 [1, N("ROSA TIENE 10 PAQUETES Y 6 SUELTOS. ¿CUÁNTOS SON?", 106, "100 Y 6 SUELTOS.", n="aplicar")],
 [2, N("1 CAJA, 7 PAQUETES Y 2 SUELTOS. ¿CUÁNTOS SON?", 172, "100 + 70 + 2 = 172.", n="aplicar")],
 [2, MC("¿CÓMO SE ESCRIBE CIENTO CINCUENTA?", ["150", "10050", "105"], "150", "1 CAJA Y 5 PAQUETES.", n="recordar")],
 [2, MC("TOMI DICE: DESPUÉS DEL 199 VIENE EL 1100. ¿QUÉ VIENE?", ["200", "1100", "190"], "200", "TOMI SE EQUIVOCÓ: VIENE EL 200.", n="error")],
 [3, MC("DE 10 EN 10: 110, 120, 130, ___", ["140", "131", "230"], "140", "SUMAMOS UN PAQUETE.", n="aplicar")],
 [3, N("DE 10 EN 10 DESDE EL 126: 126, 136, ___", 146, "LA ÚLTIMA CIFRA SIGUE SIENDO 6.", n="aplicar")],
 [3, MC("DE 10 EN 10, ¿QUÉ CIFRA CAMBIA?", ["LA DE LAS DECENAS", "LA DE LAS UNIDADES"], "LA DE LAS DECENAS", "SUBE UN PAQUETE CADA VEZ.", n="analizar")],
 [4, MC("LA SERIE 130, 140, 150, ¿SUBE O BAJA?", ["SUBE", "BAJA"], "SUBE", "CADA VEZ SUMA 10.", n="analizar")],
 [4, N("SEGUÍ LA SERIE QUE BAJA: 200, 190, 180, ___", 170, "CADA VEZ RESTA 10.", n="aplicar")],
 [4, N("¿QUÉ NÚMERO VIENE ANTES DEL 100?", 99, "99, 100.", n="recordar")],
]
M = {"subject_id": "1a53eca0-e27f-4ab1-9ab6-b23941c7d920", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: la serie numérica hasta 200", "examen_titulo": "Nivel jefe: la serie numérica hasta 200",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
