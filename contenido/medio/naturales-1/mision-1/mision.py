# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 1 · Mi cuerpo, otra vez. Genera mision-1.json.
Regla de primeros años: frases cortas, un dibujo por sección, consignas de carpeta para contar, unir, dibujar.
Metáfora: el cuerpo es un equipo (cada parte tiene su trabajo).
Niveles: 1 partes del cuerpo y para qué sirven · 2 lo que cambió desde el jardín · 3 lavado de manos y salud · 4 registro lo que observo."""
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
"objetivo": "Vas a conocer las partes de tu cuerpo y para qué sirven.",
"vas_a_ver": ["Cabeza, tronco y extremidades", "Los sentidos", "Para qué sirve cada parte"],
"secciones": [
 S(1, "Las partes grandes", [
  P("Tu cuerpo tiene <b>cabeza</b>, <b>tronco</b> y <b>extremidades</b>: brazos y piernas."),
  IMG("Mi cuerpo", "Cuatro partes grandes.", FG.nombres(["CABEZA", "TRONCO", "BRAZOS", "PIERNAS"], cols=2)),
 ]),
 S(1, "Para qué sirven", [
  D("Sentidos", "Con los ojos vemos. Con las orejas oímos."),
  P("Con la nariz olemos. Con la lengua probamos. Con la piel tocamos."),
  IMG("Cada parte, un trabajo", "Parte y trabajo.", FG.tiras(["OJOS: VER", "OREJAS: OÍR", "NARIZ: OLER", "LENGUA: PROBAR", "PIEL: TOCAR", "PIERNAS: CAMINAR"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los carteles. Los vas a usar en la carpeta."),
  IMG("Partes", "¿Para qué sirve cada una?", FG.nombres(["OJOS", "MANOS", "PIERNAS"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Los ojos", "planteo": "¿Para qué sirven los ojos?", "pasos": ["Están en la cabeza.", "Sirven para ver.", "Con ellos miramos colores."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las orejas sirven para…", "pasos": ["Las orejas sirven para ___."]},
"ejemplo_solo": {"titulo": "Tocá", "planteo": "Tocá tu cabeza, tu tronco, un brazo y una pierna."},
"tip": {"titulo": "Un equipo", "texto": "Tu cuerpo es un equipo: cada parte ayuda."},
"ojo": ["Los brazos y las piernas son extremidades.", "La piel también es un sentido."],
"resumen": [{"titulo": "Partes", "texto": "Cabeza, tronco, extremidades."}, {"titulo": "Sentidos", "texto": "Ver, oír, oler, probar, tocar."}, {"titulo": "Equipo", "texto": "Todas ayudan."}],
"glosario": [{"palabra": "Tronco", "significado": "Parte del medio del cuerpo."}, {"palabra": "Sentidos", "significado": "Nos dejan conocer lo que nos rodea."}],
"carpeta": ["¿Para qué sirven los ojos?", "¿Con qué parte agarrás una pelota?", "¿Cuántas piernas tenés?"],
"respuestas_carpeta": [acepta("VER", "PARA VER", "MIRAR", "PARA MIRAR"), acepta("MANOS", "LAS MANOS", "MANO", "CON LAS MANOS"), ["2", "dos", "DOS", "Dos"]],
"carpeta_nivel": ["recordar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "OÍR.", "solo": "Lo hiciste con tu cuerpo.", "carpeta": ["VER.", "LAS MANOS.", "2."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver cómo cambió tu cuerpo desde el jardín.",
"vas_a_ver": ["Crecer", "Los dientes", "Lo que ahora puedo hacer"],
"secciones": [
 S(1, "Crecer", [
  P("Desde el jardín, <b>creciste</b>: sos más alto y tus pies son más grandes."),
  IMG("Antes y ahora", "Creciste.", FG.tiras(["JARDÍN: MÁS BAJITO", "AHORA: MÁS ALTO"], numeros=False, cols=2)),
 ]),
 S(1, "Los dientes", [
  D("Dientes de leche", "Son los primeros dientes. Se caen y salen otros."),
  P("A muchos chicos de primer grado se les mueve un diente."),
  IMG("Cambian", "Sale un diente nuevo.", FG.tiras(["SE MUEVE", "SE CAE", "SALE UNO NUEVO"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Pensá en lo que ahora podés hacer."),
  IMG("Ahora puedo", "Cosas nuevas.", FG.tiras(["ATARME LAS ZAPATILLAS", "LEER MI NOMBRE", "SALTAR LA SOGA"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Mis zapatillas", "planteo": "¿Me entran las del jardín?", "pasos": ["Pruebo las viejas.", "Me quedan chicas.", "Mis pies crecieron."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los dientes de leche…", "pasos": ["Se caen y sale uno ___."]},
"ejemplo_solo": {"titulo": "Preguntá", "planteo": "Preguntá en tu casa cuánto medías al nacer."},
"tip": {"titulo": "Mirá fotos", "texto": "Compará una foto del jardín con una de hoy."},
"ojo": ["Cada chico crece a su ritmo.", "Que se caiga un diente es normal."],
"resumen": [{"titulo": "Crecer", "texto": "Más alto, pies más grandes."}, {"titulo": "Dientes", "texto": "Se caen y salen nuevos."}, {"titulo": "Puedo", "texto": "Hacer cosas nuevas."}],
"glosario": [{"palabra": "Crecer", "significado": "Hacerse más grande."}, {"palabra": "Jardín", "significado": "La escuela de antes de primer grado."}],
"carpeta": ["¿Qué pasa con los dientes de leche?", "¿Por qué te quedan chicas las zapatillas viejas?", "Escribí algo que ahora podés hacer."],
"respuestas_carpeta": [acepta("SE CAEN", "SE CAE", "SE CAEN Y SALEN OTROS"), acepta("CRECÍ", "CRECI", "PORQUE CRECÍ", "PORQUE CRECI", "CRECIERON MIS PIES", "CRECIÓ MI PIE"), acepta("LEER", "SALTAR", "ESCRIBIR", "ATARME", "CORRER", "CONTAR")],
"carpeta_nivel": ["recordar", "analizar", "aplicar"],
"soluciones": {"incompleto": "NUEVO.", "solo": "La respuesta es de tu familia.", "carpeta": ["SE CAEN Y SALEN OTROS.", "PORQUE CRECÍ.", "Por ejemplo: LEER."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a aprender a lavarte bien las manos.",
"vas_a_ver": ["Los microbios", "Los pasos", "Cuándo lavarse"],
"secciones": [
 S(1, "Los microbios", [
  P("En las manos hay <b>microbios</b>. Son tan chiquitos que no se ven."),
  IMG("No se ven", "Algunos nos enferman.", FG.tiras(["MANO SUCIA: MICROBIOS", "MANO LIMPIA: SIN MICROBIOS"], numeros=False, cols=2)),
 ]),
 S(1, "Los pasos", [
  D("Lavarse bien", "Agua, jabón, frotar, enjuagar y secar."),
  P("Frotá mientras contás hasta <b>20</b>."),
  IMG("Paso a paso", "En orden.", FG.tiras(["MOJAR", "JABÓN", "FROTAR HASTA 20", "ENJUAGAR", "SECAR"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("¿Cuándo te lavás las manos?"),
  IMG("Cuándo", "Momentos importantes.", FG.tiras(["ANTES DE COMER", "DESPUÉS DEL BAÑO", "AL VOLVER DEL RECREO"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Antes de comer", "planteo": "Sofi va a almorzar.", "pasos": ["Moja las manos.", "Pone jabón y frota hasta 20.", "Enjuaga y seca."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Falta un paso.", "pasos": ["MOJAR, JABÓN, FROTAR, ___, SECAR."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Lavate las manos contando hasta 20."},
"tip": {"titulo": "Contá hasta 20", "texto": "Frotá hasta contar 20, sin apurarte."},
"ojo": ["Solo con agua no alcanza: va jabón.", "Frotá entre los dedos también."],
"resumen": [{"titulo": "Microbios", "texto": "No se ven."}, {"titulo": "Pasos", "texto": "Agua, jabón, frotar, enjuagar, secar."}, {"titulo": "Cuándo", "texto": "Antes de comer."}],
"glosario": [{"palabra": "Microbio", "significado": "Ser vivo muy chiquito."}, {"palabra": "Enjuagar", "significado": "Sacar el jabón con agua."}],
"carpeta": ["¿Hasta qué número contás al frotar?", "¿Qué va después de mojar las manos?", "Tomi se lavó solo con agua. ¿Qué le faltó?"],
"respuestas_carpeta": [["20", "veinte", "VEINTE", "Veinte"], acepta("JABÓN", "JABON", "EL JABÓN", "PONER JABÓN"), acepta("JABÓN", "JABON", "EL JABÓN", "EL JABON")],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"soluciones": {"incompleto": "ENJUAGAR.", "solo": "Lo hiciste en tu casa.", "carpeta": ["20.", "EL JABÓN.", "EL JABÓN."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a registrar lo que observás.",
"vas_a_ver": ["Observar", "Registrar", "Comparar"],
"secciones": [
 S(1, "Observar", [
  P("<b>Observar</b> es mirar con atención, usando los sentidos."),
  IMG("Observo", "Con los sentidos.", FG.tiras(["MIRO", "TOCO", "HUELO", "ESCUCHO"], numeros=False, cols=2)),
 ]),
 S(1, "Registrar", [
  D("Registro", "Es anotar o dibujar lo que observo para no olvidarlo."),
  P("Sofi midió su mano con una tira de lana: <b>4 cuadraditos</b>."),
  IMG("Mi registro", "Una tabla.", FG.tiras(["MANO: 4", "PIE: 6", "BRAZO: 10"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el registro. Lo vas a usar en la carpeta."),
  IMG("Registro de Tomi", "Cuadraditos de lana.", FG.tiras(["MANO: 5", "PIE: 7", "BRAZO: 11"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Mi mano", "planteo": "Observo y registro.", "pasos": ["Miro mi mano.", "Cuento los dedos: 5.", "Anoto: MANO, 5 DEDOS."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Registrá.", "pasos": ["MIS OJOS SON DE COLOR ___."]},
"ejemplo_solo": {"titulo": "Tu registro", "planteo": "Dibujá tu mano y anotá cuántos dedos tiene."},
"tip": {"titulo": "Anotá enseguida", "texto": "Anotá apenas observás, así no te olvidás."},
"ojo": ["Registrar es anotar lo que ves, no lo que imaginás.", "Usá siempre la misma forma de medir."],
"resumen": [{"titulo": "Observar", "texto": "Mirar con atención."}, {"titulo": "Registrar", "texto": "Anotar o dibujar."}, {"titulo": "Comparar", "texto": "Ver qué es más largo."}],
"glosario": [{"palabra": "Observar", "significado": "Mirar con mucha atención."}, {"palabra": "Registro", "significado": "Lo que anotamos."}],
"carpeta": ["¿Cuánto mide el pie de Tomi?", "¿Qué parte de Tomi es la más larga?", "¿Quién tiene la mano más larga: Sofi o Tomi?"],
"respuestas_carpeta": [["7", "siete", "SIETE", "Siete", "7 CUADRADITOS"], acepta("BRAZO", "EL BRAZO"), acepta("TOMI")],
"carpeta_nivel": ["aplicar", "analizar", "analizar"],
"soluciones": {"incompleto": "Por ejemplo: MARRÓN.", "solo": "5 dedos.", "carpeta": ["7.", "EL BRAZO.", "TOMI."]},
}

ACT = {
"1": [MC("¿PARA QUÉ SIRVEN LAS OREJAS?", ["PARA OÍR", "PARA VER", "PARA OLER"], "PARA OÍR", "CON LAS OREJAS OÍMOS.", n="recordar"),
      MC("¿CON QUÉ SENTÍS EL OLOR DE UNA FLOR?", ["CON LA NARIZ", "CON LOS OJOS", "CON LAS OREJAS"], "CON LA NARIZ", "LA NARIZ HUELE.", n="aplicar")],
"2": [MC("¿QUÉ LES PASA A LOS DIENTES DE LECHE?", ["SE CAEN Y SALEN OTROS", "SE PONEN AZULES", "CRECEN SIN PARAR"], "SE CAEN Y SALEN OTROS", "SALEN DIENTES NUEVOS.", n="recordar"),
      MC("LAS ZAPATILLAS DEL JARDÍN TE QUEDAN CHICAS. ¿POR QUÉ?", ["CRECIERON TUS PIES", "SE ACHICARON SOLAS", "LAS LAVASTE"], "CRECIERON TUS PIES", "CRECISTE.", n="analizar")],
"3": [ORD("ORDENÁ LOS PASOS.", ["SECAR", "MOJAR", "ENJUAGAR", "JABÓN Y FROTAR"], ["MOJAR", "JABÓN Y FROTAR", "ENJUAGAR", "SECAR"], "MOJAR, JABÓN Y FROTAR, ENJUAGAR, SECAR.", n="aplicar"),
      MC("TOMI SE LAVÓ SOLO CON AGUA. ¿QUÉ LE FALTÓ?", ["EL JABÓN", "UNA TOALLA ROJA", "NADA"], "EL JABÓN", "SOLO CON AGUA NO ALCANZA.", n="error")],
"4": [SA("SOFI CONTÓ LOS DEDOS DE SU MANO. ¿QUÉ ANOTÓ?", ["5", "cinco", "CINCO", "Cinco", "5 DEDOS", "5 dedos"], "5 DEDOS.", n="aplicar"),
      MC("¿QUÉ ES REGISTRAR?", ["ANOTAR LO QUE OBSERVO", "INVENTAR UN CUENTO", "BORRAR TODO"], "ANOTAR LO QUE OBSERVO", "ANOTAR O DIBUJAR.", n="recordar")],
"5": [MC("RELÁMPAGO. ¿CON QUÉ VEMOS?", ["CON LOS OJOS", "CON LA NARIZ", "CON LAS MANOS"], "CON LOS OJOS", "LOS OJOS VEN.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿HASTA QUÉ NÚMERO FROTÁS LAS MANOS?", ["20", "veinte", "VEINTE"], "HASTA 20.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁNDO TE LAVÁS LAS MANOS?", ["ANTES DE COMER", "AL DORMIR", "AL MIRAR LA TELE"], "ANTES DE COMER", "ANTES DE COMER.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. BRAZOS Y PIERNAS SON…", ["EXTREMIDADES", "SENTIDOS", "DIENTES"], "EXTREMIDADES", "EXTREMIDADES.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿CUÁLES SON LAS PARTES GRANDES DEL CUERPO?", ["CABEZA, TRONCO Y EXTREMIDADES", "OJOS, NARIZ Y BOCA", "MANOS Y PIES"], "CABEZA, TRONCO Y EXTREMIDADES", "LAS TRES PARTES.", n="recordar")],
 [1, MC("¿CON QUÉ SENTIDO PROBÁS SI LA SOPA ESTÁ RICA?", ["CON LA LENGUA", "CON LOS OJOS", "CON LAS OREJAS"], "CON LA LENGUA", "LA LENGUA PRUEBA.", n="aplicar")],
 [1, SA("¿PARA QUÉ SIRVEN LOS OJOS?", acepta("VER", "PARA VER", "MIRAR", "PARA MIRAR"), "PARA VER.", n="recordar")],
 [2, MC("DESDE EL JARDÍN, TU CUERPO…", ["CRECIÓ", "SE ACHICÓ", "NO CAMBIÓ"], "CRECIÓ", "CRECISTE.", n="recordar")],
 [2, MC("A SOFI SE LE MUEVE UN DIENTE. ¿QUÉ VA A PASAR?", ["SE CAE Y SALE OTRO", "SE QUEDA ASÍ", "SE PONE GRANDE"], "SE CAE Y SALE OTRO", "ES UN DIENTE DE LECHE.", n="aplicar")],
 [2, MC("TOMI DICE QUE TODOS CRECEN IGUAL DE RÁPIDO. ¿ES ASÍ?", ["NO: CADA UNO A SU RITMO", "SÍ: TODOS IGUAL", "SÍ: SOLO LOS VARONES"], "NO: CADA UNO A SU RITMO", "CADA CHICO CRECE A SU RITMO.", n="error")],
 [3, ORD("ORDENÁ LOS PASOS PARA LAVARTE LAS MANOS.", ["ENJUAGAR", "SECAR", "MOJAR", "JABÓN Y FROTAR"], ["MOJAR", "JABÓN Y FROTAR", "ENJUAGAR", "SECAR"], "EN ORDEN.", n="aplicar")],
 [3, MC("¿POR QUÉ NOS LAVAMOS LAS MANOS?", ["PARA SACAR LOS MICROBIOS", "PARA QUE CREZCAN", "PARA PINTARLAS"], "PARA SACAR LOS MICROBIOS", "ALGUNOS NOS ENFERMAN.", n="analizar")],
 [3, SA("¿HASTA QUÉ NÚMERO CONTÁS MIENTRAS FROTÁS?", ["20", "veinte", "VEINTE"], "HASTA 20.", n="recordar")],
 [3, MC("¿CUÁNDO HAY QUE LAVARSE LAS MANOS?", ["DESPUÉS DEL BAÑO", "ANTES DE DORMIR LA SIESTA", "AL CANTAR"], "DESPUÉS DEL BAÑO", "DESPUÉS DEL BAÑO.", n="aplicar")],
 [4, MC("OBSERVAR ES…", ["MIRAR CON ATENCIÓN", "CERRAR LOS OJOS", "CORRER RÁPIDO"], "MIRAR CON ATENCIÓN", "CON LOS SENTIDOS.", n="recordar")],
 [4, SA("EN EL REGISTRO DE TOMI, ¿CUÁNTO MIDE SU MANO? (MANO: 5, PIE: 7)", ["5", "cinco", "CINCO"], "5 CUADRADITOS.", n="aplicar")],
 [4, MC("SOFI ANOTÓ: MI MANO TIENE 7 DEDOS. ¿QUÉ PASÓ?", ["CONTÓ MAL: SON 5", "ESTÁ BIEN", "LE FALTAN DEDOS"], "CONTÓ MAL: SON 5", "HAY QUE ANOTAR LO QUE SE VE.", n="error")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: mi cuerpo", "examen_titulo": "Nivel jefe: mi cuerpo",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
