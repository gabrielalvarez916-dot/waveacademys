# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 8 · El tiempo atmosférico. Genera mision-8.json.
Regla de primeros años. Metáfora: Sofi, la presentadora del pronóstico.
Niveles: 1 nubes y lluvia · 2 el viento y sus efectos · 3 medimos la temperatura · 4 calendario del tiempo."""
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
"objetivo": "Vas a ver de dónde viene la lluvia.",
"vas_a_ver": ["Las nubes", "La lluvia", "Después de llover"],
"secciones": [
 S(1, "Las nubes", [
  D("Nube", "Montón de gotitas de agua en el cielo."),
  P("Hay nubes <b>blancas</b> y nubes <b>grises</b>. Las grises traen lluvia."),
  IMG("Nubes", "Blancas o grises.", FG.tiras(["BLANCAS: BUEN TIEMPO", "GRISES: LLUVIA"], numeros=False, cols=2)),
 ]),
 S(1, "La lluvia", [
  P("Las gotitas se juntan, se hacen pesadas y <b>caen</b>: es la lluvia."),
  IMG("Así llueve", "Paso a paso.", FG.tiras(["GOTITAS EN LA NUBE", "SE JUNTAN", "CAEN: LLUEVE", "QUEDAN CHARCOS"], numeros=True, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá el cielo de hoy. Lo vas a usar en la carpeta."),
  IMG("El cielo", "¿Cómo está?", FG.tiras(["DESPEJADO", "NUBLADO", "LLUVIOSO"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Va a llover", "planteo": "Sofi mira el cielo.", "pasos": ["Ve nubes grises.", "El cielo se oscurece.", "Lleva paraguas."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Las nubes grises…", "pasos": ["Las nubes grises traen ___."]},
"ejemplo_solo": {"titulo": "Mirá el cielo", "planteo": "Mirá por la ventana. ¿Hay nubes? ¿De qué color?"},
"tip": {"titulo": "Mirá el color", "texto": "Nubes grises y oscuras: llevá paraguas."},
"ojo": ["Con tormenta y rayos, quedate adentro.", "Las nubes son agua, no algodón."],
"resumen": [{"titulo": "Nubes", "texto": "Gotitas de agua."}, {"titulo": "Grises", "texto": "Traen lluvia."}, {"titulo": "Lluvia", "texto": "Las gotas caen."}],
"glosario": [{"palabra": "Despejado", "significado": "Cielo sin nubes."}, {"palabra": "Nublado", "significado": "Cielo con muchas nubes."}],
"carpeta": ["¿De qué están hechas las nubes?", "¿Qué nubes traen lluvia?", "Tomi dice que las nubes son de algodón. ¿Está bien?"],
"respuestas_carpeta": [acepta("AGUA", "DE AGUA", "GOTITAS", "GOTITAS DE AGUA"), acepta("GRISES", "LAS GRISES", "OSCURAS"), acepta("NO", "NO, SON DE AGUA", "NO SON DE AGUA")],
"carpeta_nivel": ["recordar", "recordar", "error"],
"soluciones": {"incompleto": "LLUVIA.", "solo": "Depende del día.", "carpeta": ["DE GOTITAS DE AGUA.", "LAS GRISES.", "NO: SON DE AGUA."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver qué hace el viento.",
"vas_a_ver": ["El viento", "Qué mueve", "Fuerte o suave"],
"secciones": [
 S(1, "El viento", [
  D("Viento", "Aire que se mueve."),
  P("El viento <b>no se ve</b>, pero vemos lo que <b>mueve</b>."),
  IMG("Lo que mueve", "El viento empuja.", FG.tiras(["HOJAS", "BARRILETE", "ROPA EN LA SOGA"], numeros=False, cols=3)),
 ]),
 S(1, "Fuerte o suave", [
  P("Una <b>brisa</b> es viento suave. Un <b>ventarrón</b> es viento muy fuerte."),
  IMG("Viento", "Suave o fuerte.", FG.tiras(["BRISA: SUAVE", "VENTARRÓN: FUERTE"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las imágenes. Las vas a usar en la carpeta."),
  IMG("¿Hay viento?", "Mirá qué se mueve.", FG.tiras(["BANDERA QUIETA", "BANDERA FLAMEANDO"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "El molinete", "planteo": "Sofi sale al patio.", "pasos": ["Levanta su molinete.", "¡Gira rápido!", "Hay viento."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El viento es aire…", "pasos": ["El viento es aire que se ___."]},
"ejemplo_solo": {"titulo": "Soplá", "planteo": "Soplá un papelito sobre la mesa. ¡Hiciste viento!"},
"tip": {"titulo": "Mirá los árboles", "texto": "Si las hojas se mueven, hay viento."},
"ojo": ["El viento fuerte puede tirar cosas: cuidado.", "El viento no se ve, pero se siente."],
"resumen": [{"titulo": "Viento", "texto": "Aire que se mueve."}, {"titulo": "Mueve", "texto": "Hojas, barriletes."}, {"titulo": "Fuerza", "texto": "Brisa o ventarrón."}],
"glosario": [{"palabra": "Brisa", "significado": "Viento suave."}, {"palabra": "Flamear", "significado": "Moverse con el viento, como una bandera."}],
"carpeta": ["¿Qué es el viento?", "¿En qué bandera hay viento?", "¿Para qué sirve el viento en un barrilete?"],
"respuestas_carpeta": [acepta("AIRE QUE SE MUEVE", "AIRE"), acepta("FLAMEANDO", "LA QUE FLAMEA", "LA SEGUNDA", "LA BANDERA FLAMEANDO"), acepta("PARA VOLAR", "LO HACE VOLAR", "VOLAR", "LO LEVANTA")],
"carpeta_nivel": ["recordar", "analizar", "aplicar"],
"soluciones": {"incompleto": "MUEVE.", "solo": "El papelito se movió.", "carpeta": ["AIRE QUE SE MUEVE.", "LA QUE FLAMEA.", "PARA VOLAR."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a medir la temperatura con un termómetro.",
"vas_a_ver": ["Calor y frío", "El termómetro", "Leer el número"],
"secciones": [
 S(1, "Calor y frío", [
  P("En verano hace <b>calor</b>. En invierno hace <b>frío</b>."),
  IMG("El tiempo", "Calor o frío.", FG.tiras(["VERANO: CALOR", "INVIERNO: FRÍO"], numeros=False, cols=2)),
 ]),
 S(1, "El termómetro", [
  D("Termómetro", "Instrumento que mide la temperatura."),
  P("Cuando hace calor, la rayita <b>sube</b>. Con frío, <b>baja</b>."),
  IMG("Sube y baja", "Mirá la rayita.", FG.tiras(["CALOR: SUBE", "FRÍO: BAJA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los números. Los vas a usar en la carpeta."),
  IMG("Termómetro", "Tres días.", FG.tiras(["LUNES: 10", "MARTES: 25", "MIÉRCOLES: 15"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Hoy", "planteo": "Sofi mira el termómetro.", "pasos": ["La rayita llega al 30.", "Es un número alto.", "Hace calor."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Con frío, la rayita…", "pasos": ["Con frío, la rayita ___."]},
"ejemplo_solo": {"titulo": "¿Qué ropa?", "planteo": "Mirá la temperatura de hoy con un adulto. ¿Qué ropa te ponés?"},
"tip": {"titulo": "Número alto", "texto": "Número alto: calor. Número bajo: frío."},
"ojo": ["El termómetro se lee con un adulto.", "No se toca la parte de la punta."],
"resumen": [{"titulo": "Calor", "texto": "La rayita sube."}, {"titulo": "Frío", "texto": "La rayita baja."}, {"titulo": "Termómetro", "texto": "Mide la temperatura."}],
"glosario": [{"palabra": "Temperatura", "significado": "Cuánto calor o frío hace."}, {"palabra": "Grado", "significado": "Lo que marca el termómetro."}],
"carpeta": ["¿Qué día hizo más calor?", "¿Qué día hizo más frío?", "¿Qué mide el termómetro?"],
"respuestas_carpeta": [acepta("MARTES", "EL MARTES"), acepta("LUNES", "EL LUNES"), acepta("TEMPERATURA", "LA TEMPERATURA", "EL CALOR", "CALOR Y FRÍO", "CALOR Y FRIO")],
"carpeta_nivel": ["analizar", "analizar", "recordar"],
"soluciones": {"incompleto": "BAJA.", "solo": "Depende del día.", "carpeta": ["EL MARTES.", "EL LUNES.", "LA TEMPERATURA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a armar un calendario del tiempo.",
"vas_a_ver": ["Observar cada día", "Anotar con dibujos", "Contar"],
"secciones": [
 S(1, "Cada día", [
  D("Calendario del tiempo", "Cuadro donde anoto cómo está el tiempo cada día."),
  P("Cada día dibujás un <b>sol</b>, una <b>nube</b> o <b>gotas</b>."),
  IMG("Dibujos", "Sol, nube, lluvia.", FG.tiras(["SOL: SOLEADO", "NUBE: NUBLADO", "GOTAS: LLUVIA"], numeros=False, cols=3)),
 ]),
 S(1, "Contar", [
  P("Al final de la semana contás <b>cuántos</b> días de cada uno hubo."),
  IMG("La semana de Sofi", "Cinco días.", FG.tiras(["LUNES: SOL", "MARTES: SOL", "MIÉRCOLES: LLUVIA", "JUEVES: NUBE", "VIERNES: SOL"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la semana de Sofi. La vas a usar en la carpeta."),
  IMG("Resumen", "Contá.", FG.tiras(["SOL: 3", "NUBE: 1", "LLUVIA: 1"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El lunes", "planteo": "Sofi mira el cielo.", "pasos": ["No hay nubes.", "Brilla el sol.", "Dibuja un sol."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Si llueve, dibujo…", "pasos": ["Si llueve, dibujo ___."]},
"ejemplo_solo": {"titulo": "Tu semana", "planteo": "Armá tu calendario del tiempo esta semana."},
"tip": {"titulo": "Siempre a la misma hora", "texto": "Mirá el cielo cada día a la misma hora."},
"ojo": ["Anotá lo que ves, no lo que querés.", "Un día puede cambiar: anotá cómo estaba al mirar."],
"resumen": [{"titulo": "Observar", "texto": "Cada día."}, {"titulo": "Anotar", "texto": "Con dibujos."}, {"titulo": "Contar", "texto": "Al final de la semana."}],
"glosario": [{"palabra": "Soleado", "significado": "Día con sol."}, {"palabra": "Semana", "significado": "Siete días seguidos."}],
"carpeta": ["¿Cuántos días de sol hubo?", "¿Qué día llovió?", "¿Qué tiempo hubo más veces?"],
"respuestas_carpeta": [["3", "tres", "TRES", "Tres"], acepta("MIÉRCOLES", "MIERCOLES", "EL MIÉRCOLES", "EL MIERCOLES"), acepta("SOL", "SOLEADO", "EL SOL")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "GOTAS.", "solo": "Tu calendario.", "carpeta": ["3.", "EL MIÉRCOLES.", "SOL."]},
}

ACT = {
"1": [MC("¿QUÉ NUBES TRAEN LLUVIA?", ["GRISES", "BLANCAS", "ROSADAS"], "GRISES", "LAS GRISES Y OSCURAS.", n="recordar"),
      MC("EL CIELO ESTÁ GRIS Y OSCURO. ¿QUÉ LLEVÁS?", ["PARAGUAS", "ANTEOJOS DE SOL", "PELOTA"], "PARAGUAS", "PUEDE LLOVER.", n="aplicar")],
"2": [MC("¿QUÉ ES EL VIENTO?", ["AIRE QUE SE MUEVE", "AGUA QUE CAE", "LUZ DEL SOL"], "AIRE QUE SE MUEVE", "NO SE VE, PERO SE SIENTE.", n="recordar"),
      MC("LAS HOJAS DEL ÁRBOL SE MUEVEN MUCHO. ¿QUÉ PASA?", ["HAY VIENTO", "ESTÁ LLOVIENDO", "ES DE NOCHE"], "HAY VIENTO", "EL VIENTO LAS MUEVE.", n="analizar")],
"3": [MC("¿CON QUÉ SE MIDE LA TEMPERATURA?", ["TERMÓMETRO", "REGLA", "RELOJ"], "TERMÓMETRO", "TERMÓMETRO.", n="recordar"),
      MC("EL TERMÓMETRO MARCA 30. ¿QUÉ ROPA TE PONÉS?", ["REMERA", "CAMPERA Y BUFANDA", "GUANTES"], "REMERA", "HACE CALOR.", n="aplicar")],
"4": [SA("EN LA SEMANA HUBO SOL, SOL Y LLUVIA. ¿CUÁNTOS DÍAS DE SOL?", ["2", "dos", "DOS"], "2 DÍAS.", n="aplicar"),
      MC("TOMI DIBUJÓ UN SOL, PERO ESTABA LLOVIENDO. ¿QUÉ PASÓ?", ["ANOTÓ MAL", "ESTÁ BIEN", "EL SOL LLUEVE"], "ANOTÓ MAL", "HAY QUE ANOTAR LO QUE SE VE.", n="error")],
"5": [MC("RELÁMPAGO. ¿DE QUÉ SON LAS NUBES?", ["AGUA", "ALGODÓN", "HUMO"], "AGUA", "GOTITAS DE AGUA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. VIENTO SUAVE ES…", ["BRISA", "VENTARRÓN", "TORMENTA"], "BRISA", "BRISA.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. CON CALOR, LA RAYITA DEL TERMÓMETRO…", acepta("SUBE"), "SUBE.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. SI LLUEVE, EN EL CALENDARIO DIBUJO…", ["GOTAS", "UN SOL", "UNA LUNA"], "GOTAS", "GOTAS.", tiempo=30, n="aplicar")],
}
EXAMEN = [
 [1, MC("¿QUÉ ES UNA NUBE?", ["GOTITAS DE AGUA EN EL CIELO", "HUMO DE FÁBRICA", "ALGODÓN DEL CIELO"], "GOTITAS DE AGUA EN EL CIELO", "SON DE AGUA.", n="recordar")],
 [1, ORD("ORDENÁ CÓMO LLUEVE.", ["CAEN", "GOTITAS EN LA NUBE", "SE JUNTAN"], ["GOTITAS EN LA NUBE", "SE JUNTAN", "CAEN"], "SE JUNTAN Y CAEN.", n="aplicar")],
 [1, MC("HAY TORMENTA CON RAYOS. ¿QUÉ HACÉS?", ["ME QUEDO ADENTRO", "SALGO A JUGAR", "ME SUBO A UN ÁRBOL"], "ME QUEDO ADENTRO", "ES MÁS SEGURO.", n="aplicar")],
 [2, SA("EL AIRE QUE SE MUEVE SE LLAMA…", acepta("VIENTO", "EL VIENTO"), "VIENTO.", n="recordar")],
 [2, MC("EL MOLINETE GIRA RÁPIDO. ¿POR QUÉ?", ["HAY VIENTO", "ESTÁ ROTO", "ES DE NOCHE"], "HAY VIENTO", "EL VIENTO LO EMPUJA.", n="analizar")],
 [2, MC("SOFI DICE QUE EL VIENTO NO EXISTE PORQUE NO SE VE. ¿TIENE RAZÓN?", ["NO: SE SIENTE Y MUEVE COSAS", "SÍ: NO SE VE", "SÍ: ES INVISIBLE"], "NO: SE SIENTE Y MUEVE COSAS", "VEMOS LO QUE MUEVE.", n="error")],
 [3, MC("EL TERMÓMETRO MIDE…", ["LA TEMPERATURA", "LA LLUVIA", "EL VIENTO"], "LA TEMPERATURA", "CALOR O FRÍO.", n="recordar")],
 [3, MC("EL LUNES MARCA 10 Y EL MARTES 25. ¿QUÉ DÍA HIZO MÁS CALOR?", ["MARTES", "LUNES", "IGUAL"], "MARTES", "25 ES MÁS QUE 10.", n="analizar")],
 [3, SA("CON FRÍO, LA RAYITA DEL TERMÓMETRO…", acepta("BAJA"), "BAJA.", n="aplicar")],
 [4, MC("EN EL CALENDARIO DEL TIEMPO, ¿QUÉ DIBUJÁS SI HAY SOL?", ["UN SOL", "GOTAS", "UNA NUBE GRIS"], "UN SOL", "SOLEADO.", n="aplicar")],
 [4, SA("SOL: 3, NUBE: 1, LLUVIA: 1. ¿CUÁNTOS DÍAS HAY EN TOTAL?", ["5", "cinco", "CINCO"], "3 + 1 + 1 = 5.", n="aplicar")],
 [4, MC("¿POR QUÉ CONVIENE MIRAR EL CIELO SIEMPRE A LA MISMA HORA?", ["PARA COMPARAR", "PARA DORMIR", "PARA JUGAR"], "PARA COMPARAR", "ASÍ LOS DÍAS SE PUEDEN COMPARAR.", n="analizar")],
 [4, MC("¿QUÉ ES UN DÍA NUBLADO?", ["CON MUCHAS NUBES", "SIN NUBES", "CON NIEVE"], "CON MUCHAS NUBES", "NUBLADO.", n="recordar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 8, "estilo": "primeros",
     "practica": "Práctica general: el tiempo atmosférico", "examen_titulo": "Nivel jefe: el tiempo atmosférico",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-8.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
