# -*- coding: utf-8 -*-
"""Ciencias Sociales 1 (Nivel Medio, 1.º año) · Misión 8 · Cómo vivían antes. Genera mision-8.json.
Regla de primeros años. Metáfora: la máquina del tiempo de Sofi.
Niveles: 1 entrevista a una persona mayor · 2 objetos que cambiaron con el tiempo · 3 una familia del antiguo Egipto · 4 qué cambió y qué sigue igual."""
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
"objetivo": "Vas a entrevistar a una persona mayor.",
"vas_a_ver": ["Qué es una entrevista", "Preparar preguntas", "Escuchar y anotar"],
"secciones": [
 S(1, "La entrevista", [
  D("Entrevista", "Charla para preguntar y aprender de otra persona."),
  P("Los <b>abuelos</b> saben cómo se vivía <b>antes</b>."),
  IMG("Preguntas", "Para el abuelo.", FG.tiras(["¿A QUÉ JUGABAS?", "¿CÓMO ERA TU ESCUELA?", "¿QUÉ COMÍAS?"], numeros=True, cols=1)),
 ]),
 S(1, "Los pasos", [
  P("Preparo las preguntas, <b>pregunto</b>, <b>escucho</b> y <b>anoto</b>."),
  IMG("Pasos", "En orden.", FG.tiras(["PREPARO", "PREGUNTO", "ESCUCHO", "ANOTO"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá lo que contó la abuela. Lo vas a usar en la carpeta."),
  IMG("La abuela contó", "Respuestas.", FG.tiras(["JUGABA A LA RAYUELA", "IBA A LA ESCUELA CAMINANDO", "NO HABÍA TELE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La entrevista de Sofi", "planteo": "Sofi entrevista a su abuela.", "pasos": ["Le pregunta a qué jugaba.", "La abuela dice: a la rayuela.", "Sofi lo anota."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "En una entrevista…", "pasos": ["Pregunto, escucho y ___."]},
"ejemplo_solo": {"titulo": "Tu entrevista", "planteo": "Preguntale a una persona mayor a qué jugaba."},
"tip": {"titulo": "Escuchá", "texto": "Mirá a la persona y no la interrumpas."},
"ojo": ["Pedí permiso antes de preguntar.", "Agradecé al final."],
"resumen": [{"titulo": "Entrevista", "texto": "Preguntar y aprender."}, {"titulo": "Pasos", "texto": "Preparo, pregunto, anoto."}, {"titulo": "Escuchar", "texto": "Sin interrumpir."}],
"glosario": [{"palabra": "Entrevista", "significado": "Charla para preguntar y aprender."}, {"palabra": "Rayuela", "significado": "Juego de saltar en cuadros."}],
"carpeta": ["¿A qué jugaba la abuela?", "¿Cómo iba a la escuela?", "¿Había tele cuando era chica?"],
"respuestas_carpeta": [acepta("RAYUELA", "A LA RAYUELA", "LA RAYUELA"), acepta("CAMINANDO", "A PIE"), acepta("NO")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "ANOTO.", "solo": "Lo que te contó.", "carpeta": ["A LA RAYUELA.", "CAMINANDO.", "NO."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver objetos que cambiaron con el tiempo.",
"vas_a_ver": ["Antes y ahora", "El teléfono", "Por qué cambian"],
"secciones": [
 S(1, "Antes y ahora", [
  P("Muchos objetos <b>cambiaron</b>: el teléfono, la radio, la plancha."),
  IMG("Cambiaron", "Antes y ahora.", FG.tiras(["TELÉFONO DE DISCO: CELULAR", "RADIO GRANDE: PARLANTE", "LÁMPARA DE ACEITE: FOCO"], numeros=False, cols=1)),
 ]),
 S(1, "El teléfono", [
  D("Cambio", "Algo que antes era de una forma y ahora es de otra."),
  P("Antes el teléfono tenía <b>cable</b>. Ahora lo llevamos en el <b>bolsillo</b>."),
  IMG("El teléfono", "Con el tiempo.", FG.tiras(["CON DISCO", "CON BOTONES", "CELULAR"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los objetos. Los vas a usar en la carpeta."),
  IMG("¿Antes o ahora?", "Pensá.", FG.tiras(["CARTA EN PAPEL", "MENSAJE EN CELULAR", "LÁMPARA DE ACEITE"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "La plancha", "planteo": "La abuela cuenta.", "pasos": ["Antes se calentaba en el fuego.", "Era muy pesada.", "Ahora es eléctrica."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Antes el teléfono tenía…", "pasos": ["Un ___."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá en casa un objeto viejo. Preguntá para qué servía."},
"tip": {"titulo": "Preguntá", "texto": "Los grandes recuerdan cómo eran las cosas."},
"ojo": ["Lo viejo no es feo: sirvió mucho tiempo.", "Algunos objetos casi no cambiaron: la cuchara."],
"resumen": [{"titulo": "Cambios", "texto": "Los objetos cambian."}, {"titulo": "Teléfono", "texto": "Disco, botones, celular."}, {"titulo": "Igual", "texto": "Algunos casi no cambian."}],
"glosario": [{"palabra": "Antiguo", "significado": "De hace mucho tiempo."}, {"palabra": "Cambio", "significado": "Cuando algo pasa a ser distinto."}],
"carpeta": ["La carta en papel, ¿antes o ahora?", "El mensaje en celular, ¿antes o ahora?", "¿Qué objeto casi no cambió?"],
"respuestas_carpeta": [acepta("ANTES"), acepta("AHORA"), acepta("CUCHARA", "LA CUCHARA", "EL VASO", "VASO", "LA SILLA", "SILLA", "LA MESA", "MESA")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "CABLE.", "solo": "Lo que te contaron.", "carpeta": ["ANTES.", "AHORA.", "LA CUCHARA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer cómo vivía una familia del antiguo Egipto.",
"vas_a_ver": ["Junto al río Nilo", "Sus casas", "Sus juegos"],
"secciones": [
 S(1, "Hace muchísimo tiempo", [
  D("Antiguo Egipto", "Pueblo que vivió hace miles de años junto al río Nilo."),
  P("Vivían cerca del <b>río Nilo</b>, en casas de <b>adobe</b>."),
  IMG("Su vida", "Junto al río.", FG.tiras(["RÍO NILO", "CASAS DE ADOBE", "CAMPOS DE TRIGO"], numeros=False, cols=3)),
 ]),
 S(1, "Cómo vivían", [
  P("Comían <b>pan</b> y <b>pescado</b>. Los chicos jugaban con <b>muñecas</b> y <b>pelotas</b>."),
  IMG("Una familia", "Su día.", FG.tiras(["COMIDA: PAN Y PESCADO", "ROPA: LINO", "JUEGOS: MUÑECAS Y PELOTAS"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la tabla. La vas a usar en la carpeta."),
  IMG("Egipto y hoy", "Comparar.", FG.tiras(["EGIPTO: PAPIRO", "HOY: CUADERNO"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "Un chico egipcio", "planteo": "Se levanta temprano.", "pasos": ["Ayuda en el campo.", "Come pan con su familia.", "Juega con una pelota."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Vivían junto al río…", "pasos": ["El río ___."]},
"ejemplo_solo": {"titulo": "Dibujá", "planteo": "Dibujá una casa de adobe junto al río."},
"tip": {"titulo": "Compará", "texto": "Buscá qué se parece a tu vida."},
"ojo": ["Pasó hace miles de años.", "También jugaban, como vos."],
"resumen": [{"titulo": "Nilo", "texto": "Vivían junto al río."}, {"titulo": "Casas", "texto": "De adobe."}, {"titulo": "Juegos", "texto": "Muñecas y pelotas."}],
"glosario": [{"palabra": "Papiro", "significado": "Papel hecho con una planta del río."}, {"palabra": "Lino", "significado": "Tela hecha con una planta."}],
"carpeta": ["¿En qué escribían en Egipto?", "¿En qué escribimos hoy?", "¿En qué se parecen los chicos de Egipto a vos?"],
"respuestas_carpeta": [acepta("PAPIRO", "EN PAPIRO"), acepta("CUADERNO", "EN CUADERNO", "EN EL CUADERNO", "PAPEL"), acepta("JUGABAN", "JUEGAN", "TAMBIÉN JUGABAN", "JUGABAN A LA PELOTA", "TENÍAN FAMILIA")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "NILO.", "solo": "Tu dibujo.", "carpeta": ["EN PAPIRO.", "EN CUADERNO.", "TAMBIÉN JUGABAN."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver qué cambió y qué sigue igual.",
"vas_a_ver": ["Lo que cambió", "Lo que sigue igual", "Comparar"],
"secciones": [
 S(1, "Lo que cambió", [
  D("Cambio y permanencia", "Cosas que cambian y cosas que siguen igual."),
  P("Cambiaron los <b>teléfonos</b>, la <b>luz</b> y los <b>autos</b>."),
  IMG("Cambió", "Antes y hoy.", FG.tiras(["LÁMPARA DE ACEITE: FOCO", "CARRETA: AUTO"], numeros=False, cols=1)),
 ]),
 S(1, "Lo que sigue igual", [
  P("Siempre hubo <b>familias</b>. Siempre los chicos <b>jugaron</b>."),
  IMG("Sigue igual", "Siempre.", FG.tiras(["FAMILIAS", "JUGAR", "COMER JUNTOS"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("¿Cambió o sigue igual?", "Pensá.", FG.tiras(["EL TELÉFONO", "JUGAR CON AMIGOS", "LA FORMA DE VIAJAR"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Viajar", "planteo": "Antes y ahora.", "pasos": ["Antes se viajaba en carreta.", "Ahora en auto o colectivo.", "Cambió la forma de viajar."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Siempre hubo…", "pasos": ["Siempre hubo ___."]},
"ejemplo_solo": {"titulo": "Tu familia", "planteo": "Pensá algo que tu familia hace igual que los abuelos."},
"tip": {"titulo": "Dos columnas", "texto": "Hacé dos listas: cambió y sigue igual."},
"ojo": ["No todo cambia.", "Las personas siempre necesitaron familia y amigos."],
"resumen": [{"titulo": "Cambió", "texto": "Teléfono, luz, autos."}, {"titulo": "Sigue igual", "texto": "Familia, jugar."}, {"titulo": "Comparar", "texto": "Antes y ahora."}],
"glosario": [{"palabra": "Carreta", "significado": "Carro tirado por animales."}, {"palabra": "Permanecer", "significado": "Seguir igual."}],
"carpeta": ["El teléfono, ¿cambió o sigue igual?", "Jugar con amigos, ¿cambió o sigue igual?", "La forma de viajar, ¿cambió o sigue igual?"],
"respuestas_carpeta": [acepta("CAMBIÓ", "CAMBIO"), acepta("SIGUE IGUAL", "IGUAL"), acepta("CAMBIÓ", "CAMBIO")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "FAMILIAS.", "solo": "Por ejemplo: comer juntos.", "carpeta": ["CAMBIÓ.", "SIGUE IGUAL.", "CAMBIÓ."]},
}

ACT = {
"1": [MC("¿QUÉ ES UNA ENTREVISTA?", ["UNA CHARLA PARA PREGUNTAR", "UN JUEGO DE PATIO", "UNA COMIDA RICA"], "UNA CHARLA PARA PREGUNTAR", "PREGUNTAR Y APRENDER.", n="recordar"),
      MC("TOMI INTERRUMPE AL ABUELO TODO EL TIEMPO. ¿QUÉ CONVIENE?", ["ESCUCHAR SIN INTERRUMPIR", "GRITAR MÁS", "IRSE"], "ESCUCHAR SIN INTERRUMPIR", "EN UNA ENTREVISTA SE ESCUCHA.", n="error")],
"2": [MC("DE ESTOS TRES, ¿CUÁL SE USA AHORA?", ["EL CELULAR", "EL TELÉFONO DE DISCO", "LA CARTA EN PAPEL"], "EL CELULAR", "ES DE AHORA.", n="aplicar"),
      ORD("ORDENÁ LOS TELÉFONOS DEL MÁS VIEJO AL MÁS NUEVO.", ["CELULAR", "CON DISCO", "CON BOTONES"], ["CON DISCO", "CON BOTONES", "CELULAR"], "DISCO, BOTONES, CELULAR.", n="aplicar")],
"3": [MC("¿JUNTO A QUÉ RÍO VIVÍAN LOS EGIPCIOS?", ["NILO", "PARANÁ", "AMAZONAS"], "NILO", "EL RÍO NILO.", n="recordar"),
      MC("¿EN QUÉ SE PARECE UN CHICO DE EGIPTO A VOS?", ["TAMBIÉN JUGABA", "TENÍA CELULAR", "MIRABA LA TELE"], "TAMBIÉN JUGABA", "JUGABAN CON MUÑECAS Y PELOTAS.", n="analizar")],
"4": [MC("¿QUÉ SIGUE IGUAL DESDE HACE MUCHO?", ["JUGAR CON AMIGOS", "EL TELÉFONO", "LA LUZ"], "JUGAR CON AMIGOS", "SIEMPRE SE JUGÓ.", n="analizar"),
      SA("ANTES SE VIAJABA EN CARRETA. ¿Y AHORA?", acepta("AUTO", "EN AUTO", "COLECTIVO", "EN COLECTIVO", "TREN", "AVIÓN", "AVION"), "EN AUTO O COLECTIVO.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿QUIÉN SABE CÓMO ERA ANTES?", ["LOS ABUELOS", "UN BEBÉ", "UN PERRO"], "LOS ABUELOS", "ELLOS RECUERDAN.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿EN QUÉ ESCRIBÍAN EN EGIPTO?", ["PAPIRO", "CELULAR", "PIZARRÓN"], "PAPIRO", "PAPIRO.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿CÓMO ERAN LAS CASAS EN EGIPTO?", acepta("DE ADOBE", "ADOBE"), "DE ADOBE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL TELÉFONO, ¿CAMBIÓ O SIGUE IGUAL?", ["CAMBIÓ", "SIGUE IGUAL", "NO EXISTE"], "CAMBIÓ", "AHORA ES CELULAR.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, ORD("ORDENÁ LOS PASOS DE LA ENTREVISTA.", ["ANOTO", "PREPARO", "PREGUNTO"], ["PREPARO", "PREGUNTO", "ANOTO"], "PREPARAR, PREGUNTAR, ANOTAR.", n="aplicar")],
 [1, MC("¿A QUIÉN ENTREVISTÁS PARA SABER CÓMO ERA ANTES?", ["A UNA PERSONA MAYOR", "A UN BEBÉ", "A UN PERRO"], "A UNA PERSONA MAYOR", "ELLOS RECUERDAN.", n="aplicar")],
 [1, MC("AL TERMINAR LA ENTREVISTA…", ["AGRADEZCO", "ME VOY SIN SALUDAR", "GRITO"], "AGRADEZCO", "DECIMOS GRACIAS.", n="recordar")],
 [2, MC("ANTES EL TELÉFONO TENÍA…", ["CABLE Y DISCO", "PANTALLA TÁCTIL", "CÁMARA"], "CABLE Y DISCO", "ERA DE DISCO.", n="recordar")],
 [2, MC("¿QUÉ OBJETO CASI NO CAMBIÓ?", ["LA CUCHARA", "EL TELÉFONO", "LA RADIO"], "LA CUCHARA", "ES PARECIDA A LA DE ANTES.", n="analizar")],
 [2, SA("LA CARTA EN PAPEL, ¿ANTES O AHORA?", acepta("ANTES"), "ANTES SE USABA MÁS.", n="aplicar")],
 [3, MC("LOS EGIPCIOS VIVÍAN EN CASAS DE…", ["ADOBE", "VIDRIO", "PLÁSTICO"], "ADOBE", "BARRO Y PAJA.", n="recordar")],
 [3, MC("¿QUÉ COMÍAN EN EGIPTO?", ["PAN Y PESCADO", "HAMBURGUESAS", "PIZZA"], "PAN Y PESCADO", "PAN Y PESCADO.", n="recordar")],
 [3, MC("SOFI DICE QUE LOS CHICOS DE EGIPTO NO JUGABAN. ¿ESTÁ BIEN?", ["NO: JUGABAN CON MUÑECAS Y PELOTAS", "SÍ: NO JUGABAN", "SÍ: SOLO TRABAJABAN"], "NO: JUGABAN CON MUÑECAS Y PELOTAS", "TAMBIÉN JUGABAN.", n="error")],
 [4, MC("¿QUÉ CAMBIÓ CON EL TIEMPO?", ["LA FORMA DE VIAJAR", "TENER FAMILIA", "JUGAR"], "LA FORMA DE VIAJAR", "DE CARRETA A AUTO.", n="aplicar")],
 [4, SA("JUGAR CON AMIGOS, ¿CAMBIÓ O SIGUE IGUAL?", acepta("SIGUE IGUAL", "IGUAL"), "SIEMPRE SE JUGÓ.", n="aplicar")],
 [4, MC("TOMI DICE QUE ANTES TODO ERA DISTINTO. ¿QUÉ LE FALTA PENSAR?", ["ALGUNAS COSAS SIGUEN IGUAL", "NADA", "ANTES NO HABÍA GENTE"], "ALGUNAS COSAS SIGUEN IGUAL", "LA FAMILIA, JUGAR.", n="error")],
 [4, MC("LÁMPARA DE ACEITE Y FOCO, ¿QUÉ ES MÁS NUEVO?", ["EL FOCO", "LA LÁMPARA DE ACEITE", "IGUAL"], "EL FOCO", "EL FOCO ES DE AHORA.", n="analizar")],
]
M = {"subject_id": "67d2ad89-caaa-4e82-8d25-8bbb08147818", "tema": 8, "estilo": "primeros",
     "practica": "Práctica general: cómo vivían antes", "examen_titulo": "Nivel jefe: cómo vivían antes",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
