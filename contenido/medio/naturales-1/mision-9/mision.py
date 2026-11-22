# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 9 · Luz, sombras y sonidos. Genera mision-9.json.
Regla de primeros años. Metáfora: el teatro de sombras y la banda del grado.
Niveles: 1 objetos que dejan pasar la luz · 2 sombras largas y cortas · 3 el sonido y las vibraciones · 4 instrumentos y sonidos."""
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
"objetivo": "Vas a ver qué objetos dejan pasar la luz.",
"vas_a_ver": ["La luz", "Pasa o no pasa", "Probar con linterna"],
"secciones": [
 S(1, "La luz", [
  D("Luz", "Lo que nos deja ver las cosas."),
  P("La luz viene del <b>sol</b>, de las <b>lámparas</b> y de las <b>linternas</b>."),
  IMG("Dan luz", "Tres ejemplos.", FG.tiras(["SOL", "LÁMPARA", "LINTERNA"], numeros=False, cols=3)),
 ]),
 S(1, "Pasa o no pasa", [
  P("Por el <b>vidrio</b> pasa la luz. Por la <b>madera</b> no pasa."),
  IMG("La luz", "Pasa o no.", FG.tiras(["VIDRIO: PASA", "PAPEL FINO: PASA UN POCO", "MADERA: NO PASA"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Probá con una linterna. Lo vas a usar en la carpeta."),
  IMG("Probá", "¿Pasa la luz?", FG.nombres(["BOLSA", "LIBRO", "VASO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La ventana", "planteo": "Entra el sol.", "pasos": ["La ventana es de vidrio.", "La luz pasa.", "La pieza se ilumina."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Por la puerta de madera…", "pasos": ["La luz no ___."]},
"ejemplo_solo": {"titulo": "Linterna", "planteo": "Alumbrá tu mano con una linterna. ¿Pasa un poco?"},
"tip": {"titulo": "Probá en lo oscuro", "texto": "Con la luz apagada se ve mejor."},
"ojo": ["No apuntes la linterna a los ojos.", "Nunca mires el sol directo."],
"resumen": [{"titulo": "Luz", "texto": "Sol, lámpara, linterna."}, {"titulo": "Pasa", "texto": "Vidrio."}, {"titulo": "No pasa", "texto": "Madera, libro."}],
"glosario": [{"palabra": "Iluminar", "significado": "Dar luz."}, {"palabra": "Linterna", "significado": "Luz chiquita de mano."}],
"carpeta": ["¿Pasa la luz por el vaso de vidrio?", "¿Pasa la luz por el libro?", "¿De dónde viene la luz de día?"],
"respuestas_carpeta": [acepta("SÍ", "SI", "SÍ PASA", "SI PASA"), acepta("NO", "NO PASA"), acepta("SOL", "DEL SOL", "EL SOL")],
"carpeta_nivel": ["aplicar", "aplicar", "recordar"],
"soluciones": {"incompleto": "PASA.", "solo": "Pasa un poquito: se ve rojiza.", "carpeta": ["SÍ.", "NO.", "DEL SOL."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver por qué las sombras son largas o cortas.",
"vas_a_ver": ["La sombra", "Larga o corta", "Cambia en el día"],
"secciones": [
 S(1, "La sombra", [
  D("Sombra", "Lugar oscuro detrás de algo que tapa la luz."),
  P("Al sol, tu cuerpo <b>tapa</b> la luz y hace sombra."),
  IMG("Mi sombra", "Me sigue.", FG.tiras(["SOL", "YO", "MI SOMBRA"], numeros=False, cols=3)),
 ]),
 S(1, "Larga o corta", [
  P("A la mañana y a la tarde la sombra es <b>larga</b>. Al mediodía es <b>corta</b>."),
  IMG("En el día", "Cambia.", FG.tiras(["MAÑANA: LARGA", "MEDIODÍA: CORTA", "TARDE: LARGA"], numeros=False, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los momentos. Los vas a usar en la carpeta."),
  IMG("¿Cómo es la sombra?", "Pensá.", FG.tiras(["RECREO DE LAS 12", "SALIDA DE LA TARDE"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "En el patio", "planteo": "Sofi mira su sombra al mediodía.", "pasos": ["El sol está arriba.", "La sombra queda a sus pies.", "Es cortita."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "A la tarde, la sombra…", "pasos": ["A la tarde, la sombra es ___."]},
"ejemplo_solo": {"titulo": "Teatro de sombras", "planteo": "Con una linterna, hacé un perrito de sombra con las manos."},
"tip": {"titulo": "Mirá el sol", "texto": "Sol bajo: sombra larga. Sol alto: sombra corta. ¡Sin mirarlo directo!"},
"ojo": ["La sombra va del lado contrario al sol.", "Sin luz no hay sombra."],
"resumen": [{"titulo": "Sombra", "texto": "Algo tapa la luz."}, {"titulo": "Larga", "texto": "Mañana y tarde."}, {"titulo": "Corta", "texto": "Mediodía."}],
"glosario": [{"palabra": "Tapar", "significado": "Poner algo delante."}, {"palabra": "Contrario", "significado": "Del otro lado."}],
"carpeta": ["¿Cómo es tu sombra en el recreo de las 12?", "¿Cómo es tu sombra a la salida de la tarde?", "Tomi dice que de noche, sin luz, tiene sombra. ¿Está bien?"],
"respuestas_carpeta": [acepta("CORTA", "CORTITA"), acepta("LARGA"), acepta("NO", "NO, SIN LUZ NO HAY SOMBRA")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "LARGA.", "solo": "Tu perrito de sombra.", "carpeta": ["CORTA.", "LARGA.", "NO: SIN LUZ NO HAY SOMBRA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ver que el sonido viene de algo que vibra.",
"vas_a_ver": ["Vibrar", "El sonido viaja", "Fuerte o suave"],
"secciones": [
 S(1, "Vibrar", [
  D("Vibrar", "Moverse muy rápido para un lado y para el otro."),
  P("Cuando algo <b>vibra</b>, hace sonido. Tocá tu garganta y hablá: ¡vibra!"),
  IMG("Vibran", "Y suenan.", FG.tiras(["ELÁSTICO ESTIRADO", "TAMBOR", "MI GARGANTA"], numeros=False, cols=3)),
 ]),
 S(1, "El sonido viaja", [
  P("El sonido viaja por el <b>aire</b> y llega a tus <b>orejas</b>."),
  IMG("Viaja", "Paso a paso.", FG.tiras(["ALGO VIBRA", "VIAJA POR EL AIRE", "LLEGA A MI OREJA"], numeros=True, cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los sonidos. Los vas a usar en la carpeta."),
  IMG("¿Fuerte o suave?", "Pensá.", FG.tiras(["BOCINA", "SUSURRO", "APLAUSO"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El elástico", "planteo": "Sofi estira un elástico.", "pasos": ["Lo toca con el dedo.", "Vibra muy rápido.", "¡Suena!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El sonido viaja por el…", "pasos": ["El sonido viaja por el ___."]},
"ejemplo_solo": {"titulo": "Tu garganta", "planteo": "Tocá tu garganta y cantá una canción. ¿Sentís la vibración?"},
"tip": {"titulo": "Tocá y sentí", "texto": "Si apoyás la mano, sentís la vibración."},
"ojo": ["Los sonidos muy fuertes lastiman las orejas.", "Si algo deja de vibrar, deja de sonar."],
"resumen": [{"titulo": "Vibrar", "texto": "Moverse rápido."}, {"titulo": "Viaja", "texto": "Por el aire."}, {"titulo": "Oír", "texto": "Con las orejas."}],
"glosario": [{"palabra": "Vibración", "significado": "Movimiento muy rápido."}, {"palabra": "Susurro", "significado": "Hablar muy bajito."}],
"carpeta": ["La bocina, ¿suena fuerte o suave?", "El susurro, ¿suena fuerte o suave?", "¿Qué pasa en tu garganta cuando hablás?"],
"respuestas_carpeta": [acepta("FUERTE"), acepta("SUAVE", "BAJITO"), acepta("VIBRA", "TIEMBLA", "SE MUEVE")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "AIRE.", "solo": "Sí, se siente.", "carpeta": ["FUERTE.", "SUAVE.", "VIBRA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a conocer instrumentos y cómo suenan.",
"vas_a_ver": ["Golpear", "Soplar", "Puntear cuerdas"],
"secciones": [
 S(1, "Cómo se tocan", [
  P("El tambor se <b>golpea</b>. La flauta se <b>sopla</b>. La guitarra se toca con las <b>cuerdas</b>."),
  IMG("Instrumentos", "Tres formas.", FG.tiras(["TAMBOR: GOLPEO", "FLAUTA: SOPLO", "GUITARRA: CUERDAS"], numeros=False, cols=3)),
 ]),
 S(1, "Fuerte o suave", [
  D("Instrumento", "Objeto que se usa para hacer música."),
  P("Si golpeás <b>fuerte</b>, suena fuerte. Si golpeás <b>suave</b>, suena suave."),
  IMG("Volumen", "Vos elegís.", FG.tiras(["GOLPE FUERTE: SUENA FUERTE", "GOLPE SUAVE: SUENA SUAVE"], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los instrumentos. Los vas a usar en la carpeta."),
  IMG("¿Cómo se tocan?", "Pensá.", FG.nombres(["MARACAS", "TROMPETA", "VIOLÍN"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Un tambor casero", "planteo": "Sofi arma un tambor.", "pasos": ["Usa una lata.", "Le pone un globo arriba.", "Lo golpea: ¡suena!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La flauta…", "pasos": ["La flauta se ___."]},
"ejemplo_solo": {"titulo": "Tu instrumento", "planteo": "Armá maracas con una botella y arroz."},
"tip": {"titulo": "Probá suave", "texto": "Empezá tocando suave y después más fuerte."},
"ojo": ["No hagas ruidos muy fuertes cerca de las orejas.", "Todos los instrumentos suenan porque algo vibra."],
"resumen": [{"titulo": "Golpear", "texto": "Tambor, maracas."}, {"titulo": "Soplar", "texto": "Flauta, trompeta."}, {"titulo": "Cuerdas", "texto": "Guitarra, violín."}],
"glosario": [{"palabra": "Maracas", "significado": "Instrumento que se sacude."}, {"palabra": "Cuerda", "significado": "Hilo de la guitarra que vibra."}],
"carpeta": ["¿Cómo se tocan las maracas?", "¿Cómo se toca la trompeta?", "¿Cómo se toca el violín?"],
"respuestas_carpeta": [acepta("SE SACUDEN", "SACUDIENDO", "SACUDIR", "SE AGITAN", "AGITANDO"), acepta("SE SOPLA", "SOPLANDO", "SOPLAR"), acepta("CON LAS CUERDAS", "CUERDAS", "CON EL ARCO", "ARCO")],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"soluciones": {"incompleto": "SOPLA.", "solo": "Tus maracas.", "carpeta": ["SE SACUDEN.", "SE SOPLA.", "CON LAS CUERDAS."]},
}

ACT = {
"1": [MC("¿POR CUÁL PASA LA LUZ?", ["VIDRIO", "MADERA", "LIBRO"], "VIDRIO", "EL VIDRIO DEJA PASAR LA LUZ.", n="aplicar"),
      MC("LA PIEZA QUEDÓ OSCURA CON LA PUERTA CERRADA. ¿POR QUÉ?", ["LA MADERA NO DEJA PASAR LA LUZ", "SE APAGÓ EL SOL", "LLOVIÓ ADENTRO"], "LA MADERA NO DEJA PASAR LA LUZ", "LA MADERA TAPA LA LUZ.", n="analizar")],
"2": [MC("¿CÓMO ES TU SOMBRA AL MEDIODÍA?", ["CORTA", "LARGA", "NO HAY"], "CORTA", "EL SOL ESTÁ ARRIBA.", n="aplicar"),
      MC("¿QUÉ HACE FALTA PARA QUE HAYA SOMBRA?", ["LUZ Y ALGO QUE LA TAPE", "SOLO OSCURIDAD", "AGUA"], "LUZ Y ALGO QUE LA TAPE", "SIN LUZ NO HAY SOMBRA.", n="recordar")],
"3": [MC("¿QUÉ PASA CUANDO ALGO VIBRA?", ["HACE SONIDO", "SE APAGA", "SE MOJA"], "HACE SONIDO", "LA VIBRACIÓN SUENA.", n="recordar"),
      MC("SOFI APRIETA LA CAMPANA CON LA MANO Y DEJA DE SONAR. ¿POR QUÉ?", ["YA NO VIBRA", "SE ROMPIÓ", "SE ESCONDIÓ"], "YA NO VIBRA", "SIN VIBRACIÓN NO HAY SONIDO.", n="analizar")],
"4": [MC("¿CÓMO SE TOCA LA FLAUTA?", ["SOPLANDO", "GOLPEANDO", "SACUDIENDO"], "SOPLANDO", "SE SOPLA.", n="recordar"),
      MC("TOMI DICE QUE EL TAMBOR SE SOPLA. ¿QUÉ ESTÁ MAL?", ["SE GOLPEA", "SE SACUDE", "ESTÁ BIEN"], "SE GOLPEA", "EL TAMBOR SE GOLPEA.", n="error")],
"5": [MC("RELÁMPAGO. ¿QUÉ DA LUZ?", ["LINTERNA", "PIEDRA", "LIBRO"], "LINTERNA", "LA LINTERNA DA LUZ.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. A LA TARDE LA SOMBRA ES…", ["LARGA", "CORTA", "AZUL"], "LARGA", "EL SOL ESTÁ BAJO.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. EL SONIDO VIAJA POR EL…", acepta("AIRE"), "AIRE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL SE SACUDE?", ["MARACAS", "FLAUTA", "GUITARRA"], "MARACAS", "SE SACUDEN.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ DEJA PASAR LA LUZ?", ["LA VENTANA DE VIDRIO", "LA PARED", "LA PUERTA DE MADERA"], "LA VENTANA DE VIDRIO", "EL VIDRIO.", n="aplicar")],
 [1, SA("NOMBRÁ ALGO QUE DA LUZ.", acepta("SOL", "EL SOL", "LÁMPARA", "LAMPARA", "LINTERNA", "VELA", "FOCO"), "POR EJEMPLO: EL SOL.", n="recordar")],
 [1, MC("SOFI APUNTA LA LINTERNA A LOS OJOS DE TOMI. ¿ESTÁ BIEN?", ["NO: LASTIMA LOS OJOS", "SÍ: ES DIVERTIDO", "SÍ: NO PASA NADA"], "NO: LASTIMA LOS OJOS", "NO SE APUNTA A LOS OJOS.", n="error")],
 [2, MC("LA SOMBRA ES…", ["UN LUGAR OSCURO QUE SE FORMA", "UNA LUZ FUERTE", "UN RUIDO"], "UN LUGAR OSCURO QUE SE FORMA", "ALGO TAPA LA LUZ.", n="recordar")],
 [2, MC("¿CUÁNDO ES MÁS LARGA TU SOMBRA?", ["A LA TARDE", "AL MEDIODÍA", "NUNCA"], "A LA TARDE", "EL SOL ESTÁ BAJO.", n="analizar")],
 [2, ORD("ORDENÁ LAS SOMBRAS DEL DÍA.", ["CORTA", "LARGA DE LA TARDE", "LARGA DE LA MAÑANA"], ["LARGA DE LA MAÑANA", "CORTA", "LARGA DE LA TARDE"], "MAÑANA, MEDIODÍA, TARDE.", n="aplicar")],
 [3, MC("EL SONIDO SE PRODUCE CUANDO ALGO…", ["VIBRA", "SE MOJA", "SE ENFRÍA"], "VIBRA", "SE MUEVE RÁPIDO.", n="recordar")],
 [3, ORD("ORDENÁ CÓMO LLEGA EL SONIDO.", ["LLEGA A MI OREJA", "ALGO VIBRA", "VIAJA POR EL AIRE"], ["ALGO VIBRA", "VIAJA POR EL AIRE", "LLEGA A MI OREJA"], "EN ORDEN.", n="aplicar")],
 [3, SA("UN SUSURRO, ¿SUENA FUERTE O SUAVE?", acepta("SUAVE", "BAJITO"), "SUAVE.", n="aplicar")],
 [4, MC("¿CÓMO SE TOCA LA GUITARRA?", ["CON LAS CUERDAS", "SOPLANDO", "SACUDIÉNDOLA"], "CON LAS CUERDAS", "LAS CUERDAS VIBRAN.", n="recordar")],
 [4, MC("GOLPEÁS EL TAMBOR MUY SUAVE. ¿CÓMO SUENA?", ["SUAVE", "MUY FUERTE", "NO SUENA"], "SUAVE", "GOLPE SUAVE, SONIDO SUAVE.", n="analizar")],
 [4, SA("¿CÓMO SE TOCA LA TROMPETA?", acepta("SOPLANDO", "SE SOPLA", "SOPLAR"), "SE SOPLA.", n="aplicar")],
 [4, MC("¿POR QUÉ SUENAN TODOS LOS INSTRUMENTOS?", ["ALGO VIBRA", "TIENEN LUZ", "SON DE COLORES"], "ALGO VIBRA", "LA VIBRACIÓN HACE SONIDO.", n="analizar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: luz, sombras y sonidos", "examen_titulo": "Nivel jefe: luz, sombras y sonidos",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
