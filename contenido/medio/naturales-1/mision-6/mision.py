# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 6 · Mezclar y separar. Genera mision-6.json.
Regla de primeros años. Metáfora: la cocina de la abuela.
Niveles: 1 mezclas de sólidos · 2 mezclas con agua · 3 colar y filtrar · 4 qué se disuelve y qué no."""
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
"objetivo": "Vas a mezclar sólidos y separarlos.",
"vas_a_ver": ["Qué es una mezcla", "Mezclas de sólidos", "Separar con la mano"],
"secciones": [
 S(1, "Una mezcla", [
  D("Mezcla", "Dos o más cosas juntas."),
  P("La abuela junta <b>arroz</b> y <b>porotos</b>: es una mezcla."),
  IMG("Mezcla de sólidos", "Arroz y porotos.", FG.tiras(["ARROZ", "POROTOS", "MEZCLA"], numeros=False, cols=3)),
 ]),
 S(1, "Separar", [
  P("Los granos se ven. Los podés <b>separar con la mano</b>."),
  IMG("Separamos", "Cada uno en su lugar.", FG.tiras(["PILA DE ARROZ", "PILA DE POROTOS"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las mezclas. Las vas a usar en la carpeta."),
  IMG("Mezclas", "¿Qué tienen?", FG.tiras(["BOTONES Y FIDEOS", "PIEDRAS Y ARENA", "LENTEJAS Y MAÍZ"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "Botones y fideos", "planteo": "Están mezclados.", "pasos": ["Miro los dos.", "Saco los botones con la mano.", "Quedan los fideos solos."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Arroz con porotos…", "pasos": ["Es una ___."]},
"ejemplo_solo": {"titulo": "En la cocina", "planteo": "Buscá en tu cocina dos cosas secas para mezclar."},
"tip": {"titulo": "Mirá los tamaños", "texto": "Si se ven distintos, se pueden separar."},
"ojo": ["No te metas granitos en la boca ni en la nariz.", "Algunas mezclas tardan en separarse: arena y azúcar."],
"resumen": [{"titulo": "Mezcla", "texto": "Cosas juntas."}, {"titulo": "Sólidos", "texto": "Arroz, porotos."}, {"titulo": "Separar", "texto": "Con la mano."}],
"glosario": [{"palabra": "Sólido", "significado": "Algo duro que tiene forma, como una piedra."}, {"palabra": "Separar", "significado": "Poner cada cosa aparte."}],
"carpeta": ["¿Qué tiene la mezcla de botones?", "¿Cómo separás piedras de arena?", "Tomi dice que el arroz solo es una mezcla. ¿Está bien?"],
"respuestas_carpeta": [acepta("BOTONES Y FIDEOS", "FIDEOS Y BOTONES"), acepta("CON LA MANO", "CON LAS MANOS", "A MANO", "CON UN COLADOR"), acepta("NO", "NO, ES UNA SOLA COSA")],
"carpeta_nivel": ["recordar", "aplicar", "error"],
"soluciones": {"incompleto": "MEZCLA.", "solo": "Por ejemplo: arroz y lentejas.", "carpeta": ["BOTONES Y FIDEOS.", "CON LA MANO.", "NO: ES UNA SOLA COSA."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a mezclar cosas con agua.",
"vas_a_ver": ["Agua y arena", "Agua y aceite", "Agua y jugo"],
"secciones": [
 S(1, "Mezclas con agua", [
  P("Ponemos cosas en un vaso con <b>agua</b> y miramos qué pasa."),
  IMG("Con agua", "Pasan cosas distintas.", FG.tiras(["ARENA: SE VA AL FONDO", "ACEITE: FLOTA ARRIBA", "JUGO EN POLVO: SE PINTA"], numeros=False, cols=1)),
 ]),
 S(1, "Mirar con atención", [
  D("Flotar", "Quedarse arriba del agua."),
  P("La arena se va <b>al fondo</b>. El aceite <b>flota</b>."),
  IMG("Dos vasos", "Fondo y arriba.", FG.tiras(["AL FONDO: ARENA", "ARRIBA: ACEITE"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las mezclas. Las vas a usar en la carpeta."),
  IMG("¿Qué pasa?", "Agua y…", FG.nombres(["PIEDRA", "CORCHO", "TIERRA"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "Agua y tierra", "planteo": "Mezclamos.", "pasos": ["El agua se pone marrón.", "Esperamos un rato.", "La tierra baja al fondo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El aceite en el agua…", "pasos": ["El aceite ___ arriba."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Con un adulto, poné una piedrita en un vaso con agua."},
"tip": {"titulo": "Esperá un rato", "texto": "Algunas cosas tardan en bajar."},
"ojo": ["Hacé las pruebas con un adulto.", "No tomes las mezclas."],
"resumen": [{"titulo": "Al fondo", "texto": "Arena, piedra."}, {"titulo": "Flota", "texto": "Aceite, corcho."}, {"titulo": "Se pinta", "texto": "Jugo en polvo."}],
"glosario": [{"palabra": "Fondo", "significado": "La parte de abajo del vaso."}, {"palabra": "Corcho", "significado": "Tapón liviano de botella."}],
"carpeta": ["¿Qué hace la piedra en el agua?", "¿Qué hace el corcho en el agua?", "¿Dónde queda la tierra después de esperar?"],
"respuestas_carpeta": [acepta("SE HUNDE", "VA AL FONDO", "SE VA AL FONDO", "AL FONDO"), acepta("FLOTA", "QUEDA ARRIBA"), acepta("AL FONDO", "EN EL FONDO", "ABAJO")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "FLOTA.", "solo": "La piedrita se va al fondo.", "carpeta": ["SE VA AL FONDO.", "FLOTA.", "AL FONDO."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a separar con colador y con filtro.",
"vas_a_ver": ["El colador", "El filtro", "Cuál conviene"],
"secciones": [
 S(1, "El colador", [
  P("El <b>colador</b> tiene agujeros. Deja pasar el agua y atrapa los fideos."),
  IMG("Colar", "Pasos.", FG.tiras(["PONGO EL COLADOR", "VUELCO", "QUEDAN LOS FIDEOS"], numeros=True, cols=3)),
 ]),
 S(1, "El filtro", [
  D("Filtro", "Papel o tela con agujeritos muy chiquitos."),
  P("El filtro de café atrapa el polvo de café. Pasa solo el líquido."),
  IMG("Agujeros", "Grandes o chiquitos.", FG.tiras(["COLADOR: GRANDES", "FILTRO: CHIQUITOS"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá las mezclas. Las vas a usar en la carpeta."),
  IMG("¿Qué uso?", "Colador o filtro.", FG.tiras(["AGUA CON FIDEOS", "AGUA CON TIERRA"], numeros=False, cols=2)),
 ]),
],
"ejemplo_completo": {"titulo": "Los fideos", "planteo": "La abuela cuela.", "pasos": ["Pone el colador.", "Vuelca la olla.", "El agua pasa; los fideos quedan."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El colador deja pasar…", "pasos": ["El colador deja pasar el ___."]},
"ejemplo_solo": {"titulo": "Mirá", "planteo": "Mirá un colador de cerca. Contá algunos agujeros."},
"tip": {"titulo": "Mirá el tamaño", "texto": "Cosas grandes: colador. Cosas chiquitas: filtro."},
"ojo": ["El agua caliente quema: cuela un adulto.", "El agua filtrada de la calle no se toma."],
"resumen": [{"titulo": "Colador", "texto": "Agujeros grandes."}, {"titulo": "Filtro", "texto": "Agujeritos chiquitos."}, {"titulo": "Elegir", "texto": "Según el tamaño."}],
"glosario": [{"palabra": "Colar", "significado": "Separar con colador."}, {"palabra": "Filtrar", "significado": "Separar con filtro."}],
"carpeta": ["¿Qué usás para el agua con fideos?", "¿Qué usás para el agua con tierra?", "¿Por qué la tierra pasa por el colador?"],
"respuestas_carpeta": [acepta("COLADOR", "UN COLADOR", "EL COLADOR"), acepta("FILTRO", "UN FILTRO", "EL FILTRO"), acepta("ES CHIQUITA", "PORQUE ES CHIQUITA", "AGUJEROS GRANDES", "LOS AGUJEROS SON GRANDES")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "AGUA.", "solo": "Tiene muchos agujeros.", "carpeta": ["COLADOR.", "FILTRO.", "PORQUE ES CHIQUITA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a ver qué se disuelve en el agua y qué no.",
"vas_a_ver": ["Se disuelve", "No se disuelve", "Probar"],
"secciones": [
 S(1, "Se disuelve", [
  D("Disolverse", "Mezclarse tanto con el agua que ya no se ve."),
  P("El <b>azúcar</b> y la <b>sal</b> se disuelven: desaparecen en el agua."),
  IMG("Se disuelven", "Ya no se ven.", FG.nombres(["AZÚCAR", "SAL", "JUGO"], cols=3)),
 ]),
 S(1, "No se disuelve", [
  P("La <b>arena</b>, el <b>aceite</b> y la piedra <b>no</b> se disuelven: siguen viéndose."),
  IMG("No se disuelven", "Siguen ahí.", FG.nombres(["ARENA", "ACEITE", "PIEDRA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("¿Se disuelve?", "Pensá.", FG.nombres(["SAL", "BOTÓN", "CACAO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El azúcar", "planteo": "La ponemos en agua.", "pasos": ["Revuelvo con una cuchara.", "Espero un ratito.", "¡Ya no la veo: se disolvió!"]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La arena en el agua…", "pasos": ["La arena no se ___."]},
"ejemplo_solo": {"titulo": "Probá", "planteo": "Con un adulto, poné sal en agua y revolvé."},
"tip": {"titulo": "Revolvé", "texto": "Revolver ayuda a que se disuelva más rápido."},
"ojo": ["Que no se vea no quiere decir que no está: el agua queda dulce.", "Las pruebas se hacen con un adulto."],
"resumen": [{"titulo": "Se disuelve", "texto": "Azúcar, sal."}, {"titulo": "No se disuelve", "texto": "Arena, aceite."}, {"titulo": "Revolver", "texto": "Ayuda."}],
"glosario": [{"palabra": "Disolverse", "significado": "Mezclarse con el agua y no verse."}, {"palabra": "Revolver", "significado": "Mover con una cuchara."}],
"carpeta": ["La sal, ¿se disuelve?", "El botón, ¿se disuelve?", "Sofi dice que el azúcar desapareció del agua. ¿Por qué el agua sigue dulce?"],
"respuestas_carpeta": [acepta("SÍ", "SI", "SÍ, SE DISUELVE", "SI SE DISUELVE"), acepta("NO", "NO SE DISUELVE"), acepta("ESTÁ DISUELTA", "ESTA DISUELTA", "SE DISOLVIÓ", "SE DISOLVIO", "SIGUE AHÍ", "SIGUE AHI")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "DISUELVE.", "solo": "La sal ya no se ve.", "carpeta": ["SÍ.", "NO.", "PORQUE SIGUE AHÍ, DISUELTA."]},
}

ACT = {
"1": [MC("¿QUÉ ES UNA MEZCLA?", ["DOS O MÁS COSAS JUNTAS", "UNA SOLA COSA", "UN ANIMAL"], "DOS O MÁS COSAS JUNTAS", "COMO ARROZ Y POROTOS.", n="recordar"),
      MC("¿CÓMO SEPARÁS BOTONES DE FIDEOS?", ["CON LA MANO", "CON AGUA CALIENTE", "SOPLANDO"], "CON LA MANO", "SE VEN Y SE PUEDEN SACAR.", n="aplicar")],
"2": [MC("¿QUÉ HACE EL ACEITE EN EL AGUA?", ["FLOTA", "SE HUNDE", "DESAPARECE"], "FLOTA", "QUEDA ARRIBA.", n="recordar"),
      MC("MEZCLASTE AGUA Y TIERRA. ESPERÁS UN RATO. ¿QUÉ PASA?", ["LA TIERRA BAJA AL FONDO", "LA TIERRA FLOTA", "EL AGUA DESAPARECE"], "LA TIERRA BAJA AL FONDO", "HAY QUE ESPERAR.", n="analizar")],
"3": [MC("¿QUÉ USÁS PARA SEPARAR FIDEOS DEL AGUA?", ["UN COLADOR", "UN FILTRO DE CAFÉ", "UNA CUCHARA"], "UN COLADOR", "TIENE AGUJEROS GRANDES.", n="aplicar"),
      MC("TOMI QUIERE SEPARAR TIERRA DEL AGUA CON UN COLADOR. ¿QUÉ PASA?", ["LA TIERRA PASA", "QUEDA LA TIERRA", "SE SECA EL AGUA"], "LA TIERRA PASA", "CONVIENE UN FILTRO.", n="error")],
"4": [MC("¿QUÉ SE DISUELVE EN EL AGUA?", ["EL AZÚCAR", "LA ARENA", "LA PIEDRA"], "EL AZÚCAR", "YA NO SE VE.", n="aplicar"),
      SA("LA ARENA, ¿SE DISUELVE EN EL AGUA?", acepta("NO", "NO SE DISUELVE"), "NO: SIGUE VIÉNDOSE.", n="aplicar")],
"5": [MC("RELÁMPAGO. ¿QUÉ FLOTA?", ["CORCHO", "PIEDRA", "ARENA"], "CORCHO", "QUEDA ARRIBA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿QUÉ SE DISUELVE?", ["SAL", "BOTÓN", "PIEDRA"], "SAL", "YA NO SE VE.", tiempo=30, n="recordar"),
      SA("RELÁMPAGO. ¿CON QUÉ COLÁS LOS FIDEOS?", acepta("COLADOR", "CON UN COLADOR", "UN COLADOR"), "COLADOR.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ARROZ Y POROTOS JUNTOS ES UNA…", ["MEZCLA", "PLANTA", "PIEDRA"], "MEZCLA", "MEZCLA.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿CUÁL ES UNA MEZCLA?", ["ARROZ CON POROTOS", "SOLO ARROZ", "SOLO AGUA"], "ARROZ CON POROTOS", "DOS COSAS JUNTAS.", n="aplicar")],
 [1, MC("¿CÓMO SE SEPARAN LAS PIEDRAS DE LA ARENA?", ["CON LA MANO O UN COLADOR", "CON AGUA", "NO SE PUEDE"], "CON LA MANO O UN COLADOR", "LAS PIEDRAS SON GRANDES.", n="analizar")],
 [1, SA("¿CÓMO SE LLAMA JUNTAR DOS O MÁS COSAS?", acepta("MEZCLA", "MEZCLAR", "UNA MEZCLA"), "MEZCLA.", n="recordar")],
 [2, MC("¿QUÉ HACE LA PIEDRA EN EL AGUA?", ["SE VA AL FONDO", "FLOTA", "SE DISUELVE"], "SE VA AL FONDO", "SE HUNDE.", n="aplicar")],
 [2, SA("EL CORCHO EN EL AGUA…", acepta("FLOTA", "QUEDA ARRIBA"), "FLOTA.", n="aplicar")],
 [2, MC("SOFI DICE QUE EL ACEITE SE HUNDE. ¿ESTÁ BIEN?", ["NO: FLOTA", "SÍ: SE HUNDE", "SÍ: DESAPARECE"], "NO: FLOTA", "QUEDA ARRIBA DEL AGUA.", n="error")],
 [3, MC("EL COLADOR TIENE AGUJEROS…", ["GRANDES", "INVISIBLES", "CUADRADOS ROJOS"], "GRANDES", "DEJA PASAR EL AGUA.", n="recordar")],
 [3, MC("¿QUÉ USÁS PARA SEPARAR CAFÉ EN POLVO DEL LÍQUIDO?", ["UN FILTRO", "UN COLADOR GRANDE", "LA MANO"], "UN FILTRO", "AGUJERITOS CHIQUITOS.", n="aplicar")],
 [3, ORD("ORDENÁ LOS PASOS PARA COLAR.", ["VUELCO", "QUEDAN LOS FIDEOS", "PONGO EL COLADOR"], ["PONGO EL COLADOR", "VUELCO", "QUEDAN LOS FIDEOS"], "EN ORDEN.", n="aplicar")],
 [4, MC("¿QUÉ NO SE DISUELVE?", ["LA ARENA", "EL AZÚCAR", "LA SAL"], "LA ARENA", "SIGUE VIÉNDOSE.", n="aplicar")],
 [4, MC("¿QUÉ AYUDA A QUE EL AZÚCAR SE DISUELVA?", ["REVOLVER", "ESPERAR UN AÑO", "SOPLAR"], "REVOLVER", "CON UNA CUCHARA.", n="recordar")],
 [4, MC("EL AZÚCAR YA NO SE VE. ¿POR QUÉ EL AGUA ESTÁ DULCE?", ["ESTÁ DISUELTA", "SE FUE VOLANDO", "NO HABÍA AZÚCAR"], "ESTÁ DISUELTA", "SIGUE AHÍ AUNQUE NO SE VEA.", n="analizar")],
 [4, SA("LA SAL EN EL AGUA, ¿SE DISUELVE?", acepta("SÍ", "SI", "SÍ SE DISUELVE", "SI SE DISUELVE"), "SÍ.", n="aplicar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 6, "estilo": "primeros",
     "practica": "Práctica general: mezclar y separar", "examen_titulo": "Nivel jefe: mezclar y separar",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-6.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
