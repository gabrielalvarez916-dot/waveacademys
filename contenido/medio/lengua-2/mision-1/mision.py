# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 1 · Palabras y oraciones que ya sabemos. Genera mision-1.json.
Regla de primeros años y vía fonológica (la voz no nombra letras). Repaso de primer grado al empezar segundo.
Metáfora: el cuaderno viajero de Sofi (cada día escribe oraciones sobre lo que pasa en su casa y en la escuela).
Niveles: 1 leer oraciones cortas · 2 escribir oraciones con mayúscula y punto · 3 ordenar palabras · 4 completar oraciones."""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), "lengua-1"))  # dibujos de Lengua del Medio
import figuras as FG


def abecedario_pares():
    """Abecedario de imprenta: arriba la mayúscula, abajo la minúscula de cada letra."""
    L = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"; cols = 9; filas = 3
    W = 1.1 * cols + .3; H = 1.75 * filas + .3
    fig, ax = FG.lienzo(W, H, W, H, 0, 0)
    for i, ch in enumerate(L):
        x = .15 + 1.1 * (i % cols); y = H - .15 - 1.75 * (i // cols + 1) + .1
        ax.add_patch(FG.FancyBboxPatch((x, y), 1.0, 1.6, boxstyle="round,pad=0.02,rounding_size=0.12", color="white", ec=FG.COLS[i % len(FG.COLS)], lw=2.2))
        ax.text(x + .5, y + 1.12, ch, ha="center", va="center", fontsize=27, color=FG.OSC, **FG.F)
        ax.text(x + .5, y + .45, ch.lower(), ha="center", va="center", fontsize=27, color=FG.CORAL, **FG.F)
    return FG.png(fig)

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

N1 = {**ESTILO,
"objetivo": "Vas a leer oraciones cortas y entender qué dicen.",
"vas_a_ver": ["El cuaderno viajero", "Leer una oración", "¿Quién? ¿Qué hace?"],
"secciones": [
 S(1, "El cuaderno viajero", [
  P("Sofi tiene un <b>cuaderno viajero</b>. Cada día escribe algo."),
  P("Hoy escribió: <b>MI GATO DUERME AL SOL.</b>"),
  IMG("Lo que escribió Sofi", "Una oración por renglón.", FG.tiras(["MI GATO DUERME AL SOL.", "TOMI JUEGA A LA PELOTA."], numeros=True)),
 ]),
 S(1, "¿Quién? ¿Qué hace?", [
  D("Leer una oración", "Leemos todas las palabras y pensamos: <b>¿de quién habla?</b> <b>¿Qué hace?</b>"),
  P("MI GATO DUERME AL SOL. ¿Quién? <b>Mi gato</b>. ¿Qué hace? <b>Duerme</b>."),
  IMG("Palabra por palabra", "Cinco palabras.", FG.nombres(["MI", "GATO", "DUERME", "AL", "SOL."], cols=5)),
 ]),
 S(2, "Para practicar", [
  P("Leé la oración. La vas a usar en la carpeta."),
  IMG("Otra oración", "Leela despacito.", FG.nombres(["LA", "MAESTRA", "LEE", "UN", "CUENTO."], cols=5)),
 ]),
],
"ejemplo_completo": {"titulo": "Una oración", "planteo": "TOMI JUEGA A LA PELOTA.", "pasos": ["¿Quién? Tomi.", "¿Qué hace? Juega a la pelota.", "¡La entendimos!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "EL PERRO COME HUESOS.", "pasos": ["¿Quién? El ___ .", "¿Qué hace? ___ huesos."]},
"ejemplo_solo": {"titulo": "Tu lectura", "planteo": "Leé: MAMÁ CANTA EN LA COCINA. ¿Quién canta?"},
"tip": {"titulo": "Leé despacito", "texto": "Leé todas las palabras, sin saltear."},
"ojo": ["Las palabras cortas también se leen: AL, LA, UN.", "Si no entendés, leé otra vez."],
"resumen": [{"titulo": "Leer", "texto": "Todas las palabras."}, {"titulo": "¿Quién?", "texto": "De quién habla."}, {"titulo": "¿Qué hace?", "texto": "Lo que pasa."}],
"glosario": [{"palabra": "Oración", "significado": "Palabras juntas que dicen algo."}, {"palabra": "Cuaderno viajero", "significado": "Un cuaderno que va de casa a la escuela."}],
"carpeta": ["¿Quién lee en la oración?", "¿Qué lee?", "¿Cuántas palabras tiene la oración?"],
"carpeta_nivel": ["aplicar", "aplicar", "aplicar"],
"respuestas_carpeta": [low("LA MAESTRA") + low("MAESTRA"), low("UN CUENTO") + low("CUENTO"), ["5", "cinco", "CINCO"]],
"soluciones": {"incompleto": "PERRO. COME.", "solo": "Mamá.", "carpeta": ["La maestra.", "Un cuento.", "5."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a escribir oraciones con mayúscula y punto.",
"vas_a_ver": ["Empieza con mayúscula", "Mayúscula y minúscula: dos formas de cada letra", "Termina con punto", "Revisar lo que escribo"],
"secciones": [
 S(1, "Mayúscula y punto", [
  D("Mayúscula", "La oración empieza con <b>letra grande</b>: la mayúscula."),
  D("Punto", "La oración termina con un <b>punto</b>. Dice: terminó."),
  IMG("Sofi escribió", "Mayúscula al principio, punto al final.", FG.letras("Hoy llueve.", resaltar=(0,))),
 ]),
 S(1, "Mayúscula y minúscula", [
  D("Dos formas de cada letra", "Cada letra tiene dos formas: la <b>mayúscula</b>, que es la grande, y la <b>minúscula</b>, que es la chica. Es la misma letra."),
  P("La <b>mayúscula</b> va al principio de la oración y en los nombres. Todo lo demás se escribe con <b>minúscula</b>."),
  IMG("El abecedario de imprenta", "Arriba, la mayúscula. Abajo, la minúscula.", abecedario_pares()),
  P("Para pasar de mayúscula a minúscula: la primera letra queda grande y las demás se achican. <b>SOFI</b> se escribe <b>Sofi</b>."),
 ]),
 S(1, "Revisar", [
  P("Tomi escribió: <b>hoy fuimos a la plaza</b>."),
  P("Le falta la mayúscula y el punto: <b>Hoy fuimos a la plaza.</b>"),
  IMG("Antes y después", "Así queda bien.", FG.tiras(["hoy fuimos a la plaza", "Hoy fuimos a la plaza."], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las oraciones. Las vas a usar en la carpeta."),
  IMG("Oraciones para revisar", "¿Qué les falta?", FG.tiras(["mi abuela hace tortas", "El perro ladra"], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Revisar", "planteo": "el sol sale", "pasos": ["Pongo mayúscula: El.", "Pongo punto al final.", "El sol sale."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "la luna brilla", "pasos": ["Empieza con ___ : La.", "Termina con ___ ."]},
"ejemplo_solo": {"titulo": "Tu oración", "planteo": "Escribí una oración sobre tu mascota o tu juguete preferido."},
"tip": {"titulo": "Mirá el principio y el final", "texto": "Revisá siempre las dos puntas."},
"ojo": ["Sin punto, no se sabe dónde termina.", "Los nombres de personas también llevan mayúscula."],
"resumen": [{"titulo": "Mayúscula", "texto": "Al principio."}, {"titulo": "Punto", "texto": "Al final."}, {"titulo": "Revisar", "texto": "Las dos puntas."}],
"glosario": [{"palabra": "Mayúscula", "significado": "La letra grande."}, {"palabra": "Punto", "significado": "El que cierra la oración."}],
"carpeta": ["¿Qué le falta a la oración 1 al principio?", "¿Qué le falta a la oración 2 al final?", "Copiá bien la oración 1."],
"carpeta_nivel": ["analizar", "analizar", "error"],
"respuestas_carpeta": [low("MAYÚSCULA") + low("LA MAYÚSCULA") + low("mayuscula"), low("PUNTO") + low("EL PUNTO") + low("UN PUNTO"), ["Mi abuela hace tortas.", "MI ABUELA HACE TORTAS."]],
"soluciones": {"incompleto": "Mayúscula. Punto.", "solo": "Por ejemplo: Mi perro se llama Toby.", "carpeta": ["La mayúscula.", "El punto.", "Mi abuela hace tortas."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a ordenar palabras para que la oración se entienda.",
"vas_a_ver": ["Palabras mezcladas", "Buscar quién y qué hace", "Armar la oración"],
"secciones": [
 S(1, "Palabras mezcladas", [
  P("El viento desordenó el cuaderno de Sofi."),
  P("<b>PAN COMPRA PAPÁ</b> no se entiende."),
  IMG("Mezcladas", "Así no se entiende.", FG.nombres(["PAN", "COMPRA", "PAPÁ"], cols=3)),
 ]),
 S(1, "Armar la oración", [
  D("Ordenar", "Buscamos <b>quién</b>, después <b>qué hace</b>, y al final lo demás."),
  P("Quién: <b>Papá</b>. Qué hace: <b>compra</b>. Qué: <b>pan</b>. Papá compra pan."),
  IMG("Ordenadas", "Ahora sí se entiende.", FG.nombres(["PAPÁ", "COMPRA", "PAN."], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Para ordenar", "Buscá quién empieza.", FG.nombres(["FLORES", "RIEGA", "LA ABUELA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Ordenar", "planteo": "SALTA EL CONEJO", "pasos": ["¿Quién? El conejo.", "¿Qué hace? Salta.", "El conejo salta."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "LECHE TOMA TOMI", "pasos": ["¿Quién? ___ .", "Oración: Tomi ___ leche."]},
"ejemplo_solo": {"titulo": "Tu turno", "planteo": "Ordená: PELOTA LA PATEA SOFI."},
"tip": {"titulo": "¿Quién va primero?", "texto": "Casi siempre empieza por quién hace algo."},
"ojo": ["La primera palabra lleva mayúscula.", "No te olvides del punto al final."],
"resumen": [{"titulo": "Mezcladas", "texto": "No se entienden."}, {"titulo": "Quién", "texto": "Va primero."}, {"titulo": "Ordenada", "texto": "Se entiende."}],
"glosario": [{"palabra": "Ordenar", "significado": "Poner cada cosa en su lugar."}, {"palabra": "Desordenado", "significado": "Mezclado."}],
"carpeta": ["¿Quién hace algo en las palabras del dibujo?", "¿Qué hace?", "Escribí la oración ordenada."],
"carpeta_nivel": ["analizar", "analizar", "aplicar"],
"respuestas_carpeta": [low("LA ABUELA") + low("ABUELA"), low("RIEGA") + low("RIEGA FLORES"), ["La abuela riega flores.", "LA ABUELA RIEGA FLORES.", "La abuela riega las flores."]],
"soluciones": {"incompleto": "Tomi. toma.", "solo": "Sofi patea la pelota.", "carpeta": ["La abuela.", "Riega.", "La abuela riega flores."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a completar oraciones con la palabra que falta.",
"vas_a_ver": ["La palabra que falta", "Elegir la que tiene sentido", "Escribir la oración completa"],
"secciones": [
 S(1, "La palabra que falta", [
  P("Se borró una palabra del cuaderno: <b>EL PÁJARO ___ EN EL ÁRBOL.</b>"),
  D("Completar", "Buscamos una palabra que haga que la oración <b>tenga sentido</b>."),
  IMG("¿Qué falta?", "Pensá qué hace el pájaro.", FG.tiras(["EL PÁJARO ___ EN EL ÁRBOL."], numeros=False, cols=1)),
 ]),
 S(1, "Elegir bien", [
  P("CANTA tiene sentido: <b>El pájaro canta en el árbol.</b>"),
  P("MESA no tiene sentido: el pájaro no mesa."),
  IMG("Con sentido", "Así sí.", FG.tiras(["EL PÁJARO CANTA EN EL ÁRBOL."], numeros=False, cols=1)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las oraciones. Las vas a usar en la carpeta."),
  IMG("Para completar", "Una palabra en cada hueco.", FG.tiras(["LA VACA DA ___ .", "EN INVIERNO HACE ___ ."], numeros=True)),
 ]),
],
"ejemplo_completo": {"titulo": "Completar", "planteo": "TOMI SE LAVA LOS ___ .", "pasos": ["¿Qué se lava? Algo del cuerpo.", "Dientes tiene sentido.", "Tomi se lava los dientes."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "EL ___ LADRA.", "pasos": ["¿Quién ladra? El ___ .", "Oración: El ___ ladra."]},
"ejemplo_solo": {"titulo": "Tu turno", "planteo": "Completá: EN VERANO VAMOS A LA ___ ."},
"tip": {"titulo": "Leé la oración entera", "texto": "Leela con la palabra puesta. ¿Se entiende?"},
"ojo": ["Puede haber más de una palabra que sirva.", "Releé al final para controlar."],
"resumen": [{"titulo": "Falta", "texto": "Una palabra."}, {"titulo": "Elegir", "texto": "La que tiene sentido."}, {"titulo": "Releer", "texto": "Para controlar."}],
"glosario": [{"palabra": "Completar", "significado": "Poner lo que falta."}, {"palabra": "Sentido", "significado": "Que se entiende."}],
"carpeta": ["¿Qué da la vaca?", "¿Qué hace en invierno?", "Tomi completó: LA VACA DA MESA. ¿Qué palabra va?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("LECHE"), low("FRÍO") + low("frio"), low("LECHE")],
"soluciones": {"incompleto": "PERRO. PERRO.", "solo": "Playa, pileta o plaza.", "carpeta": ["Leche.", "Frío.", "Leche: mesa no tiene sentido."]},
}

ACT = {
"1": [MC("MI GATO DUERME AL SOL. ¿QUIÉN DUERME?", ["MI GATO", "EL SOL", "MAMÁ"], "MI GATO", "¿QUIÉN? MI GATO.", n="aplicar"),
      MC("TOMI JUEGA A LA PELOTA. ¿QUÉ HACE TOMI?", ["JUEGA", "DUERME", "LEE"], "JUEGA", "¿QUÉ HACE? JUEGA.", n="aplicar")],
"2": [TF("ESTA ORACIÓN ESTÁ BIEN ESCRITA: hoy llueve", "FALSO", "LE FALTAN LA MAYÚSCULA Y EL PUNTO.", n="error"),
      MC("¿QUÉ LE FALTA A: El perro ladra", ["EL PUNTO", "LA MAYÚSCULA", "NADA"], "EL PUNTO", "TERMINA CON PUNTO.", n="analizar")],
"3": [ORD("ORDENÁ LA ORACIÓN.", ["PAN.", "PAPÁ", "COMPRA"], ["PAPÁ", "COMPRA", "PAN."], "QUIÉN, QUÉ HACE, QUÉ.", n="aplicar"),
      ORD("ORDENÁ LA ORACIÓN.", ["SALTA.", "EL CONEJO"], ["EL CONEJO", "SALTA."], "PRIMERO QUIÉN.", n="aplicar")],
"4": [MC("EL PÁJARO ___ EN EL ÁRBOL.", ["CANTA", "MESA", "AZUL"], "CANTA", "CANTA TIENE SENTIDO.", n="aplicar"),
      SA("COMPLETÁ: LA VACA DA ___ .", low("LECHE"), "LA VACA DA LECHE.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿CON QUÉ EMPIEZA LA ORACIÓN?", ["MAYÚSCULA", "PUNTO"], "MAYÚSCULA", "LA LETRA GRANDE.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CON QUÉ TERMINA?", ["PUNTO", "MAYÚSCULA"], "PUNTO", "EL PUNTO CIERRA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. EL PERRO ___ .", ["LADRA", "MESA"], "LADRA", "TIENE SENTIDO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿CUÁL VA PRIMERO?", ["SOFI", "LEE"], "SOFI", "PRIMERO QUIÉN.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("LA MAESTRA LEE UN CUENTO. ¿QUIÉN LEE?", ["LA MAESTRA", "EL CUENTO", "SOFI"], "LA MAESTRA", "¿QUIÉN? LA MAESTRA.", n="aplicar")],
 [1, SA("EL PERRO COME HUESOS. ¿QUÉ COME EL PERRO?", low("HUESOS"), "COME HUESOS.", n="aplicar")],
 [1, TF("MI GATO DUERME AL SOL TIENE 5 PALABRAS.", "VERDADERO", "MI, GATO, DUERME, AL, SOL.", n="analizar")],
 [2, MC("¿QUÉ LE FALTA A: la luna brilla.", ["LA MAYÚSCULA", "EL PUNTO", "NADA"], "LA MAYÚSCULA", "EMPIEZA CON MAYÚSCULA.", n="error")],
 [2, MC("¿QUÉ LE FALTA A: hoy fuimos a la plaza", ["MAYÚSCULA Y PUNTO", "SOLO EL PUNTO", "NADA"], "MAYÚSCULA Y PUNTO", "LAS DOS PUNTAS.", n="analizar")],
 [2, UNI("UNÍ CADA COSA CON SU LUGAR.", [("MAYÚSCULA", "AL PRINCIPIO"), ("PUNTO", "AL FINAL")], "LAS DOS PUNTAS.", n="recordar")],
 [3, ORD("ORDENÁ LA ORACIÓN.", ["LA PELOTA.", "SOFI", "PATEA"], ["SOFI", "PATEA", "LA PELOTA."], "QUIÉN, QUÉ HACE, QUÉ.", n="aplicar")],
 [3, ORD("ORDENÁ LA ORACIÓN.", ["LECHE.", "TOMA", "TOMI"], ["TOMI", "TOMA", "LECHE."], "PRIMERO QUIÉN.", n="aplicar")],
 [3, TF("PAN COMPRA PAPÁ SE ENTIENDE BIEN.", "FALSO", "ORDENADA: PAPÁ COMPRA PAN.", n="error")],
 [4, MC("TOMI SE LAVA LOS ___ .", ["DIENTES", "ÁRBOLES", "PERROS"], "DIENTES", "TIENE SENTIDO.", n="aplicar")],
 [4, SA("COMPLETÁ: EL ___ LADRA.", low("PERRO"), "EL PERRO LADRA.", n="aplicar")],
 [4, MC("EN INVIERNO HACE ___ .", ["FRÍO", "VERANO", "PLAYA"], "FRÍO", "TIENE SENTIDO.", n="aplicar")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 1, "estilo": "primeros",
     "practica": "Práctica general: palabras y oraciones", "examen_titulo": "Nivel jefe: palabras y oraciones",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-1.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
