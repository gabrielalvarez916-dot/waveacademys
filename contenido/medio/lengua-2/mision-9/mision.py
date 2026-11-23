# -*- coding: utf-8 -*-
"""Lengua 2 (Nivel Medio, 2.º año) · Misión 9 · Poemas de Rafael Pombo. Genera mision-9.json.
Regla de primeros años y vía fonológica (la VOZ de las clases no nombra letras; el PDF muestra las letras).
Poema de trabajo: «El renacuajo paseador» de Rafael Pombo (1867, dominio público; se citan solo la primera estrofa,
el «¡Muchacho, no salgas!» y la estrofa final; el resto se cuenta con palabras simples).
Metáfora: el cuaderno viajero de Sofi (hoy le pega un poema).
Niveles: 1 escuchar el poema · 2 leer en voz alta con ritmo · 3 imaginar y dibujar los personajes · 4 inventar una estrofa."""
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
E1 = ["El hijo de Rana, Rinrín Renacuajo,", "salió esta mañana muy tieso y muy majo,", "con pantalón corto, corbata a la moda,", "sombrero encintado y chupa de boda."]
E1R = [(0, "ajo"), (1, "ajo"), (2, "oda"), (3, "oda")]
EF = ["Y así concluyeron, uno, dos y tres,", "Ratón y Ratona, y el Rana después;", "los gatos comieron y el Pato cenó,", "¡y mamá Ranita solita quedó!"]

N1 = {**ESTILO,
"objetivo": "Vas a escuchar el poema El renacuajo paseador.",
"vas_a_ver": ["Quién lo escribió", "Cómo empieza", "Qué le pasa a Rinrín"],
"secciones": [
 S(1, "Un poema de Rafael Pombo", [
  P("Sofi pegó un <b>poema</b> en su cuaderno viajero."),
  P("Lo escribió <b>Rafael Pombo</b>, un poeta de Colombia."),
  D("Poema", "Texto escrito en <b>versos</b>, con música."),
  IMG("Así empieza", "La primera estrofa.", FG.estrofa(E1, titulo="El renacuajo paseador")),
 ]),
 S(1, "Lo que pasa", [
  P("Su mamá le dice: «¡Muchacho, no salgas!»."),
  P("Pero Rinrín no escucha y se va de paseo."),
  P("Visita a doña Ratona con su amigo el ratón."),
  P("Llegan unos gatos. Al final, un pato se traga a Rinrín."),
  IMG("Los personajes", "Rinrín, su mamá y el pato.", FG.objetos([("renacuajo", "RINRÍN"), ("rana", "MAMÁ RANA"), ("raton", "EL RATÓN"), ("pato", "EL PATO")])),
 ]),
 S(2, "Para practicar", [
  P("Leé el final del poema. Lo vas a usar en la carpeta."),
  IMG("El final", "La última estrofa.", FG.estrofa(EF)),
 ]),
],
"ejemplo_completo": {"titulo": "El autor", "planteo": "¿Quién escribió el poema?", "pasos": ["Busco el nombre del poeta.", "Es Rafael Pombo.", "Era de Colombia."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El poema cuenta de un renacuajo.", "pasos": ["Se llama ___ Renacuajo."]},
"ejemplo_solo": {"titulo": "Contalo", "planteo": "Contale a alguien de tu casa qué le pasó a Rinrín."},
"tip": {"titulo": "Escuchá la música", "texto": "Los poemas suenan como una canción."},
"ojo": ["Rinrín no hizo caso a su mamá.", "Un poema también puede contar una historia."],
"resumen": [{"titulo": "Autor", "texto": "Rafael Pombo, de Colombia."}, {"titulo": "Poema", "texto": "Texto en versos."}, {"titulo": "Rinrín", "texto": "No hizo caso a su mamá."}],
"glosario": [{"palabra": "Renacuajo", "significado": "Rana bebé, con cola."}, {"palabra": "Poeta", "significado": "Persona que escribe poemas."}],
"carpeta": ["En el final del poema, ¿quién se quedó solita?", "¿Qué animal cenó al final?", "Tomi dice que Rinrín hizo caso a su mamá. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MAMÁ RANITA") + low("mama ranita") + low("LA MAMÁ") + low("la mama") + low("MAMÁ") + low("mama"), low("EL PATO") + low("PATO"), NO],
"soluciones": {"incompleto": "RINRÍN.", "solo": "Lo que te acuerdes del poema.", "carpeta": ["Mamá Ranita.", "El pato.", "No: salió igual."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a leer el poema en voz alta con ritmo.",
"vas_a_ver": ["Versos y estrofas", "La rima", "Leer con ritmo"],
"secciones": [
 S(1, "Versos y estrofas", [
  D("Verso", "Cada <b>renglón</b> del poema."),
  D("Estrofa", "Un <b>grupo</b> de versos."),
  IMG("Una estrofa", "Tiene cuatro versos.", FG.estrofa(E1)),
 ]),
 S(1, "La rima", [
  P("RENACUAJO y MAJO <b>terminan igual</b>."),
  P("MODA y BODA también. Eso es <b>rima</b>."),
  IMG("Palabras que riman", "El final suena igual.", FG.estrofa(E1, rimas=E1R)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("¿Riman?", "Escuchá cómo terminan.", FG.nombres(["GATO", "PATO", "SOL", "LUNA"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Rima", "planteo": "¿MODA rima con BODA?", "pasos": ["MODA termina en ODA.", "BODA termina en ODA.", "Sí, riman."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Buscá la rima.", "pasos": ["RENACUAJO rima con ___ ."]},
"ejemplo_solo": {"titulo": "En voz alta", "planteo": "Leé la primera estrofa en voz alta con ritmo."},
"tip": {"titulo": "Pausa al final", "texto": "Hacé una pausa al final de cada verso."},
"ojo": ["No leas todo pegado.", "La coma pide una pausa corta."],
"resumen": [{"titulo": "Verso", "texto": "Cada renglón."}, {"titulo": "Estrofa", "texto": "Grupo de versos."}, {"titulo": "Rima", "texto": "Finales que suenan igual."}],
"glosario": [{"palabra": "Majo", "significado": "Lindo, elegante."}, {"palabra": "Ritmo", "significado": "La música al leer."}],
"carpeta": ["¿Qué palabra del dibujo rima con GATO?", "¿Cuántos versos tiene la primera estrofa?", "Tomi dice que SOL rima con LUNA. ¿Tiene razón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("PATO"), ["4", "CUATRO", "cuatro", "Cuatro"], NO],
"soluciones": {"incompleto": "MAJO.", "solo": "La estrofa leída con pausas.", "carpeta": ["PATO.", "4.", "No: terminan distinto."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a imaginar y dibujar a los personajes.",
"vas_a_ver": ["Cómo se viste Rinrín", "Palabras que describen", "Dibujar"],
"secciones": [
 S(1, "Rinrín bien vestido", [
  P("El poema dice cómo se viste Rinrín."),
  P("<b>Pantalón corto</b>, <b>corbata</b> a la moda."),
  P("<b>Sombrero</b> con cinta y <b>chupa</b> de boda."),
  D("Chupa", "Una <b>chaqueta</b> elegante."),
  IMG("Rinrín", "Así lo imaginó Sofi.", FG.objetos([("renacuajo", "RINRÍN RENACUAJO")])),
 ]),
 S(1, "Imaginar", [
  P("Leemos y <b>pensamos</b> cómo es cada personaje."),
  P("Después lo <b>dibujamos</b> con esos detalles."),
  IMG("Lo que dice el poema", "Cada detalle se dibuja.", FG.tiras(["PANTALÓN CORTO", "CORBATA", "SOMBRERO", "CHUPA"], numeros=False)),
 ]),
 S(2, "Para practicar", [
  P("Leé las pistas. Las vas a usar en la carpeta."),
  IMG("¿Quién es?", "Pensá en el poema.", FG.tiras(["1. ES UNA RANA Y ES LA MAMÁ.", "2. ES BLANCO Y SE TRAGA A RINRÍN."], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Imaginar", "planteo": "¿Cómo es el sombrero de Rinrín?", "pasos": ["El poema dice: encintado.", "Tiene una cinta.", "Lo dibujo con cinta."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Rinrín lleva pantalón…", "pasos": ["Pantalón ___ ."]},
"ejemplo_solo": {"titulo": "Tu dibujo", "planteo": "Dibujá a Rinrín con todo lo que dice el poema."},
"tip": {"titulo": "Volvé al poema", "texto": "Los detalles están en los versos."},
"ojo": ["Dibujá lo que dice el poema.", "Podés agregar colores que imagines."],
"resumen": [{"titulo": "Leer", "texto": "Buscar cómo es."}, {"titulo": "Imaginar", "texto": "Pensar al personaje."}, {"titulo": "Dibujar", "texto": "Con los detalles."}],
"glosario": [{"palabra": "Chupa", "significado": "Chaqueta elegante."}, {"palabra": "Encintado", "significado": "Con una cinta."}],
"carpeta": ["¿Quién es el personaje de la pista 1?", "¿Quién es el personaje de la pista 2?", "Tomi dibujó a Rinrín con pantalón largo. ¿Cómo es el pantalón?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("MAMÁ RANA") + low("mama rana") + low("LA MAMÁ") + low("la mama") + low("MAMÁ RANITA") + low("mama ranita"), low("EL PATO") + low("PATO"), low("CORTO") + low("PANTALÓN CORTO") + low("pantalon corto") + low("ES CORTO")],
"soluciones": {"incompleto": "CORTO.", "solo": "Tu dibujo de Rinrín.", "carpeta": ["La mamá rana.", "El pato.", "Corto."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a inventar una estrofa que rime.",
"vas_a_ver": ["Copiar la forma", "Cambiar el personaje", "Buscar la rima"],
"secciones": [
 S(1, "Una estrofa nueva", [
  P("Sofi inventa un personaje: <b>Mimí Gatita</b>."),
  P("Copia la forma del poema y cambia las palabras."),
  IMG("La estrofa de Sofi", "GATITA rima con BONITA.", FG.estrofa(["La hija de Gata, Mimí Gatita,", "salió esta tarde muy linda y bonita."], rimas=[(0, "ita"), (1, "ita")])),
 ]),
 S(1, "Buscar la rima", [
  P("Pensamos palabras que <b>terminen igual</b>."),
  P("GATITA: BONITA, CHIQUITA, MANITA."),
  IMG("Rimas con ITA", "Todas terminan igual.", FG.nombres(["BONITA", "CHIQUITA", "MANITA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las palabras. Las vas a usar en la carpeta."),
  IMG("Para rimar", "Buscá la pareja.", FG.nombres(["RATÓN", "SOMBRERO", "BOTÓN", "MESA"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "Inventar", "planteo": "Personaje: PERRO PANCHO.", "pasos": ["El perro Pancho salió a pasear,", "con su corbata se fue a jugar.", "PASEAR rima con JUGAR."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Buscá la rima.", "pasos": ["El sapo Pepe tiene un sombrero,", "y lo cuida el día ___ ."]},
"ejemplo_solo": {"titulo": "Tu estrofa", "planteo": "Inventá dos versos que rimen sobre tu animal."},
"tip": {"titulo": "Primero la rima", "texto": "Elegí antes las dos palabras que riman."},
"ojo": ["Los versos son cortos.", "Las palabras del final tienen que rimar."],
"resumen": [{"titulo": "Forma", "texto": "Copiar la del poema."}, {"titulo": "Personaje", "texto": "Inventar uno nuevo."}, {"titulo": "Rima", "texto": "Finales iguales."}],
"glosario": [{"palabra": "Inventar", "significado": "Crear algo nuevo."}, {"palabra": "Estrofa", "significado": "Grupo de versos."}],
"carpeta": ["¿Qué palabra del dibujo rima con RATÓN?", "Completá: El sapo Pepe tiene un sombrero, y lo cuida el día…", "Tomi escribió: Mimí Gatita es muy grande. ¿Rima con GATITA?"],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"respuestas_carpeta": [low("BOTÓN") + low("boton"), low("ENTERO") + low("EL DÍA ENTERO") + low("el dia entero"), NO],
"soluciones": {"incompleto": "ENTERO.", "solo": "Dos versos que rimen.", "carpeta": ["BOTÓN.", "ENTERO.", "No: GRANDE no termina en ITA."]},
}

ACT = {
"1": [MC("¿QUIÉN ESCRIBIÓ EL RENACUAJO PASEADOR?", ["RAFAEL POMBO", "SOFI", "UN PATO"], "RAFAEL POMBO", "UN POETA DE COLOMBIA.", n="recordar"),
      TF("RINRÍN HIZO CASO A SU MAMÁ.", "FALSO", "SALIÓ IGUAL DE PASEO.", n="aplicar")],
"2": [MC("¿QUÉ PALABRA RIMA CON MODA?", ["BODA", "MESA", "SOL"], "BODA", "LAS DOS TERMINAN IGUAL.", n="aplicar"),
      UNI("UNÍ LAS PALABRAS QUE RIMAN.", [("RENACUAJO", "MAJO"), ("MODA", "BODA"), ("GATO", "PATO")], "TERMINAN IGUAL.", n="analizar")],
"3": [MC("¿QUÉ LLEVA RINRÍN EN LA CABEZA?", ["UN SOMBRERO", "UNA CORONA", "NADA"], "UN SOMBRERO", "SOMBRERO ENCINTADO.", n="recordar"),
      SA("RINRÍN LLEVA PANTALÓN… ¿LARGO O CORTO?", low("CORTO") + low("PANTALÓN CORTO") + low("pantalon corto"), "PANTALÓN CORTO.", n="aplicar")],
"4": [MC("¿QUÉ PALABRA RIMA CON GATITA?", ["BONITA", "GRANDE", "PERRO"], "BONITA", "TERMINAN EN ITA.", n="aplicar"),
      TF("EN UNA ESTROFA INVENTADA, LAS PALABRAS DEL FINAL PUEDEN RIMAR.", "VERDADERO", "COMO EN EL POEMA.", n="recordar")],
"5": [MC("RELÁMPAGO. CADA RENGLÓN DEL POEMA ES UN…", ["VERSO", "CUENTO"], "VERSO", "SE LLAMA VERSO.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿RIMAN SOL Y LUNA?", ["NO", "SÍ"], "NO", "TERMINAN DISTINTO.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. RINRÍN ES UN…", ["RENACUAJO", "GATO"], "RENACUAJO", "EL HIJO DE RANA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ RIMA CON RATÓN?", ["BOTÓN", "MESA"], "BOTÓN", "TERMINAN EN ÓN.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿DE DÓNDE ERA RAFAEL POMBO?", ["DE COLOMBIA", "DE LA LUNA", "DE UN CUENTO"], "DE COLOMBIA", "ERA UN POETA DE COLOMBIA.", n="recordar")],
 [1, SA("¿CÓMO SE LLAMA EL RENACUAJO DEL POEMA?", low("RINRÍN") + low("rinrin") + low("RINRÍN RENACUAJO") + low("rinrin renacuajo"), "RINRÍN RENACUAJO.", n="recordar")],
 [1, TF("AL FINAL DEL POEMA, UN PATO SE TRAGA A RINRÍN.", "VERDADERO", "EL PATO CENÓ.", n="aplicar")],
 [2, MC("UN GRUPO DE VERSOS SE LLAMA…", ["ESTROFA", "TÍTULO", "PUNTO"], "ESTROFA", "LA ESTROFA ES UN GRUPO DE VERSOS.", n="recordar")],
 [2, UNI("UNÍ LAS PALABRAS QUE RIMAN.", [("SOMBRERO", "ENTERO"), ("RATÓN", "BOTÓN"), ("PASEAR", "JUGAR")], "TERMINAN IGUAL.", n="analizar")],
 [2, TF("PARA LEER CON RITMO, HAY QUE LEER TODO PEGADO.", "FALSO", "SE HACE UNA PAUSA EN CADA VERSO.", n="error")],
 [3, MC("¿QUÉ ES UNA CHUPA?", ["UNA CHAQUETA", "UN SOMBRERO", "UN ZAPATO"], "UNA CHAQUETA", "UNA CHAQUETA ELEGANTE.", n="recordar")],
 [3, SA("¿QUÉ LLEVA RINRÍN EN EL CUELLO, A LA MODA?", low("CORBATA") + low("UNA CORBATA"), "UNA CORBATA.", n="aplicar")],
 [3, TF("TOMI DIBUJÓ A RINRÍN CON PANTALÓN LARGO. ESTÁ BIEN.", "FALSO", "EL POEMA DICE PANTALÓN CORTO.", n="error")],
 [4, MC("¿QUÉ PALABRA RIMA CON CHIQUITA?", ["MANITA", "MESA", "SOL"], "MANITA", "TERMINAN EN ITA.", n="aplicar")],
 [4, SA("COMPLETÁ CON UNA RIMA: EL PERRO PANCHO SALIÓ A PASEAR, CON SU CORBATA SE FUE A ___", low("JUGAR") + low("BAILAR") + low("CANTAR") + low("NADAR") + low("SALTAR") + low("LLORAR") + low("VOLAR") + low("ESTUDIAR"), "POR EJEMPLO: JUGAR.", n="aplicar")],
 [4, TF("MIMÍ GATITA ES MUY GRANDE. GRANDE RIMA CON GATITA.", "FALSO", "GRANDE NO TERMINA EN ITA.", n="error")],
]
M = {"subject_id": "71a9ccdf-909e-4fbd-84e4-a68e9be813c8", "tema": 9, "estilo": "primeros",
     "practica": "Práctica general: poemas de Rafael Pombo", "examen_titulo": "Nivel jefe: poemas de Rafael Pombo",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-9.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
