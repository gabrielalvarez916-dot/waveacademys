# -*- coding: utf-8 -*-
"""Ciencias Naturales 1 (Nivel Medio, 1.º año) · Misión 4 · Quién vive dónde. Genera mision-4.json.
Regla de primeros años. Metáfora: la excursión a la laguna.
Niveles: 1 ambientes de tierra, de agua y de aire · 2 qué necesitan para vivir · 3 un ambiente y sus habitantes · 4 seres vivos y cosas no vivas."""
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
"objetivo": "Vas a conocer ambientes de tierra, de agua y de aire.",
"vas_a_ver": ["Ambiente de tierra", "Ambiente de agua", "Los que vuelan"],
"secciones": [
 S(1, "Los ambientes", [
  D("Ambiente", "Lugar donde vive un ser vivo."),
  P("Hay ambientes de <b>tierra</b> y de <b>agua</b>."),
  IMG("Ambientes", "Tierra y agua.", FG.tiras(["TIERRA: CAMPO, BOSQUE", "AGUA: MAR, LAGUNA"], numeros=False, cols=2)),
 ]),
 S(1, "Quién vive dónde", [
  P("La vaca vive en la tierra. El pez vive en el agua. El pájaro vuela por el <b>aire</b>."),
  IMG("Habitantes", "Cada uno en su lugar.", FG.tiras(["VACA: TIERRA", "PEZ: AGUA", "PÁJARO: AIRE", "RANA: AGUA Y TIERRA"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Mirá los animales. Los vas a usar en la carpeta."),
  IMG("Animales", "¿Dónde viven?", FG.nombres(["CABALLO", "PULPO", "HORNERO"], cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "La ballena", "planteo": "¿Dónde vive?", "pasos": ["Nada.", "Está en el mar.", "Vive en el agua."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El caballo…", "pasos": ["El caballo vive en la ___."]},
"ejemplo_solo": {"titulo": "Tu barrio", "planteo": "Nombrá un animal que veas en tu barrio. ¿Dónde vive?"},
"tip": {"titulo": "Mirá cómo se mueve", "texto": "Si nada, vive en el agua. Si camina, en la tierra."},
"ojo": ["La rana vive en el agua y en la tierra.", "Los pájaros vuelan, pero hacen el nido en árboles."],
"resumen": [{"titulo": "Tierra", "texto": "Campo, bosque."}, {"titulo": "Agua", "texto": "Mar, laguna."}, {"titulo": "Aire", "texto": "Los que vuelan."}],
"glosario": [{"palabra": "Ambiente", "significado": "Lugar donde vive un ser vivo."}, {"palabra": "Laguna", "significado": "Agua quieta, más chica que un lago."}],
"carpeta": ["¿Dónde vive el caballo?", "¿Dónde vive el pulpo?", "La rana, ¿dónde vive?"],
"respuestas_carpeta": [acepta("TIERRA", "EN LA TIERRA", "CAMPO", "EN EL CAMPO"), acepta("AGUA", "EN EL AGUA", "MAR", "EN EL MAR"), acepta("AGUA Y TIERRA", "TIERRA Y AGUA", "LAGUNA")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "TIERRA.", "solo": "Depende de tu barrio.", "carpeta": ["EN LA TIERRA.", "EN EL AGUA.", "EN EL AGUA Y EN LA TIERRA."]},
}

N2 = {**ESTILO,
"objetivo": "Vas a ver qué necesitan los seres vivos para vivir.",
"vas_a_ver": ["Agua y alimento", "Aire", "Un lugar"],
"secciones": [
 S(1, "Lo que necesitan", [
  P("Todos los seres vivos necesitan <b>agua</b>, <b>alimento</b>, <b>aire</b> y un <b>lugar</b>."),
  IMG("Necesitan", "Cuatro cosas.", FG.tiras(["AGUA", "ALIMENTO", "AIRE", "UN LUGAR"], numeros=False, cols=2)),
 ]),
 S(1, "Sin agua", [
  D("Ser vivo", "Nace, crece, se alimenta y necesita agua."),
  P("Una planta sin agua se seca. Con agua, se pone verde."),
  IMG("Antes y después", "El agua ayuda.", FG.tiras(["SIN AGUA: SECA", "CON AGUA: VERDE"], numeros=False, cols=2)),
 ]),
 S(2, "Para practicar", [
  P("Pensá en tu mascota o en un animal."),
  IMG("Mi mascota necesita", "Para vivir.", FG.tiras(["AGUA", "COMIDA", "UN LUGAR"], numeros=False, cols=3)),
 ]),
],
"ejemplo_completo": {"titulo": "El pez", "planteo": "¿Qué necesita?", "pasos": ["Agua para vivir.", "Alimento.", "Una pecera o el mar."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "Los seres vivos necesitan…", "pasos": ["AGUA, ALIMENTO, AIRE Y UN ___."]},
"ejemplo_solo": {"titulo": "Cuidar", "planteo": "Dibujá cómo cuidás a una planta o mascota."},
"tip": {"titulo": "Pensá en vos", "texto": "Vos también necesitás agua, comida, aire y casa."},
"ojo": ["Las plantas también necesitan agua y aire.", "Cada ser vivo come cosas distintas."],
"resumen": [{"titulo": "Agua", "texto": "Todos la necesitan."}, {"titulo": "Alimento y aire", "texto": "Para vivir."}, {"titulo": "Lugar", "texto": "Su ambiente."}],
"glosario": [{"palabra": "Alimento", "significado": "Lo que come un ser vivo."}, {"palabra": "Secarse", "significado": "Quedarse sin agua."}],
"carpeta": ["¿Qué le pasa a una planta sin agua?", "¿Qué necesita un perro para vivir?", "Tomi dice que las plantas no necesitan agua. ¿Está bien?"],
"respuestas_carpeta": [acepta("SE SECA", "SE MUERE", "SECA"), acepta("AGUA", "COMIDA", "AGUA Y COMIDA", "AGUA Y ALIMENTO", "ALIMENTO"), acepta("NO", "NO, NECESITAN AGUA", "NO NECESITAN AGUA")],
"carpeta_nivel": ["analizar", "aplicar", "error"],
"soluciones": {"incompleto": "LUGAR.", "solo": "Tu dibujo.", "carpeta": ["SE SECA.", "AGUA Y COMIDA.", "NO: NECESITAN AGUA."]},
}

N3 = {**ESTILO,
"objetivo": "Vas a conocer un ambiente y sus habitantes.",
"vas_a_ver": ["La laguna", "Sus habitantes", "Dónde está cada uno"],
"secciones": [
 S(1, "La laguna", [
  P("En la laguna hay <b>agua</b>, <b>barro</b> y <b>plantas</b> en la orilla."),
  IMG("La laguna", "Agua y orilla.", FG.tiras(["AGUA", "ORILLA CON BARRO", "PLANTAS: JUNCOS"], numeros=False, cols=3)),
 ]),
 S(1, "Sus habitantes", [
  D("Habitante", "Ser vivo que vive en un lugar."),
  P("Viven el <b>pato</b>, el <b>pez</b>, la <b>rana</b> y los <b>juncos</b>."),
  IMG("Habitantes", "Todos en la laguna.", FG.nombres(["PATO", "PEZ", "RANA", "JUNCO"], cols=4)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("¿Dónde están?", "Agua u orilla.", FG.tiras(["PEZ: EN EL AGUA", "JUNCO: EN LA ORILLA", "RANA: EN LOS DOS"], numeros=False, cols=1)),
 ]),
],
"ejemplo_completo": {"titulo": "El pato", "planteo": "¿Dónde está?", "pasos": ["Nada en el agua.", "Camina en la orilla.", "Está en los dos lugares."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "El pez…", "pasos": ["El pez vive en el ___."]},
"ejemplo_solo": {"titulo": "Otro ambiente", "planteo": "Dibujá la plaza con sus habitantes."},
"tip": {"titulo": "Plantas también", "texto": "Las plantas también son habitantes."},
"ojo": ["Los juncos son plantas: también son habitantes.", "El agua y el barro no son habitantes."],
"resumen": [{"titulo": "Ambiente", "texto": "La laguna."}, {"titulo": "Habitantes", "texto": "Pato, pez, rana, junco."}, {"titulo": "Lugar", "texto": "Agua u orilla."}],
"glosario": [{"palabra": "Habitante", "significado": "Ser vivo que vive en un lugar."}, {"palabra": "Junco", "significado": "Planta de la orilla de la laguna."}],
"carpeta": ["¿Dónde vive el pez?", "¿Dónde crece el junco?", "¿Quién está en el agua y en la orilla?"],
"respuestas_carpeta": [acepta("AGUA", "EN EL AGUA"), acepta("ORILLA", "EN LA ORILLA"), acepta("RANA", "LA RANA", "PATO", "EL PATO")],
"carpeta_nivel": ["aplicar", "aplicar", "analizar"],
"soluciones": {"incompleto": "AGUA.", "solo": "Tu dibujo de la plaza.", "carpeta": ["EN EL AGUA.", "EN LA ORILLA.", "LA RANA."]},
}

N4 = {**ESTILO,
"objetivo": "Vas a diferenciar seres vivos y cosas no vivas.",
"vas_a_ver": ["Seres vivos", "Cosas no vivas", "El ciclo de la vida"],
"secciones": [
 S(1, "Seres vivos", [
  D("Ser vivo", "Nace, crece, se alimenta y se muere."),
  P("El perro, la planta y vos son <b>seres vivos</b>."),
  IMG("Seres vivos", "Nacen y crecen.", FG.nombres(["PERRO", "PLANTA", "NENA"], cols=3)),
 ]),
 S(1, "Cosas no vivas", [
  P("La piedra, el agua y la pelota <b>no</b> nacen ni crecen."),
  IMG("No vivas", "No crecen.", FG.nombres(["PIEDRA", "AGUA", "PELOTA"], cols=3)),
 ]),
 S(2, "Para practicar", [
  P("Mirá la lista. La vas a usar en la carpeta."),
  IMG("¿Vivo o no vivo?", "Pensá si crece.", FG.nombres(["GATO", "SILLA", "ÁRBOL", "ROCA"], cols=4)),
 ]),
],
"ejemplo_completo": {"titulo": "El árbol", "planteo": "¿Es un ser vivo?", "pasos": ["Nació de una semilla.", "Crece.", "Sí: es un ser vivo."]},
"ejemplo_incompleto": {"titulo": "Completá", "planteo": "La piedra…", "pasos": ["La piedra no ___."]},
"ejemplo_solo": {"titulo": "Buscá", "planteo": "Buscá en tu casa un ser vivo y una cosa no viva."},
"tip": {"titulo": "Preguntá si crece", "texto": "Si nace y crece, es un ser vivo."},
"ojo": ["Moverse no alcanza: el auto se mueve y no está vivo.", "Las plantas no caminan, pero están vivas."],
"resumen": [{"titulo": "Vivos", "texto": "Nacen, crecen, se mueren."}, {"titulo": "No vivos", "texto": "No crecen."}, {"titulo": "Ojo", "texto": "Moverse no alcanza."}],
"glosario": [{"palabra": "Ciclo", "significado": "Algo que se repite."}, {"palabra": "Semilla", "significado": "De ella nace una planta."}],
"carpeta": ["¿Cuáles son seres vivos?", "¿Cuáles no son seres vivos?", "Sofi dice que el auto está vivo porque se mueve. ¿Está bien?"],
"respuestas_carpeta": [acepta("GATO Y ÁRBOL", "GATO Y ARBOL", "EL GATO Y EL ÁRBOL", "ÁRBOL Y GATO"), acepta("SILLA Y ROCA", "LA SILLA Y LA ROCA", "ROCA Y SILLA"), acepta("NO", "NO, NO CRECE", "NO NO CRECE")],
"carpeta_nivel": ["aplicar", "aplicar", "error"],
"soluciones": {"incompleto": "CRECE.", "solo": "Por ejemplo: una planta y una mesa.", "carpeta": ["GATO Y ÁRBOL.", "SILLA Y ROCA.", "NO: NO NACE NI CRECE."]},
}

ACT = {
"1": [MC("¿DÓNDE VIVE LA BALLENA?", ["EN EL AGUA", "EN LA TIERRA", "EN UN ÁRBOL"], "EN EL AGUA", "VIVE EN EL MAR.", n="aplicar"),
      MC("¿QUÉ ES UN AMBIENTE?", ["EL LUGAR DONDE VIVE", "LO QUE COME", "CÓMO SE MUEVE"], "EL LUGAR DONDE VIVE", "COMO EL MAR O EL CAMPO.", n="recordar")],
"2": [MC("¿QUÉ NECESITAN TODOS LOS SERES VIVOS?", ["AGUA", "UNA PELOTA", "UN AUTO"], "AGUA", "TODOS NECESITAN AGUA.", n="recordar"),
      MC("UN PERRO TIENE COMIDA PERO NO AGUA. ¿QUÉ LE FALTA PARA VIVIR?", ["AGUA", "UN JUGUETE", "NADA"], "AGUA", "TAMBIÉN NECESITA AGUA.", n="analizar")],
"3": [SA("NOMBRÁ UN HABITANTE DE LA LAGUNA.", acepta("PATO", "PEZ", "RANA", "JUNCO", "JUNCOS"), "PATO, PEZ, RANA O JUNCO.", n="aplicar"),
      MC("EN LA LAGUNA, ¿CUÁL NO ES UN HABITANTE?", ["EL BARRO", "EL PATO", "EL JUNCO"], "EL BARRO", "EL BARRO NO ES UN SER VIVO.", n="analizar")],
"4": [MC("¿CUÁL ES UN SER VIVO?", ["EL ÁRBOL", "LA PIEDRA", "LA SILLA"], "EL ÁRBOL", "NACE Y CRECE.", n="aplicar"),
      MC("TOMI DICE QUE LA PLANTA NO ESTÁ VIVA PORQUE NO CAMINA. ¿TIENE RAZÓN?", ["NO: NACE Y CRECE", "SÍ: NO CAMINA", "SÍ: ES VERDE"], "NO: NACE Y CRECE", "LAS PLANTAS ESTÁN VIVAS.", n="error")],
"5": [MC("RELÁMPAGO. ¿DÓNDE VIVE EL PEZ?", ["AGUA", "TIERRA", "AIRE"], "AGUA", "EN EL AGUA.", tiempo=30, n="recordar"),
      MC("RELÁMPAGO. ¿CUÁL NO ES UN SER VIVO?", ["PELOTA", "GATO", "FLOR"], "PELOTA", "NO CRECE.", tiempo=30, n="aplicar"),
      SA("RELÁMPAGO. ¿QUÉ NECESITA UNA PLANTA PARA NO SECARSE?", acepta("AGUA"), "AGUA.", tiempo=30, n="aplicar"),
      MC("RELÁMPAGO. ¿QUIÉN VIVE EN EL AGUA Y EN LA TIERRA?", ["RANA", "VACA", "PEZ"], "RANA", "LA RANA.", tiempo=30, n="recordar")],
}
EXAMEN = [
 [1, MC("¿DÓNDE VIVE EL PULPO?", ["EN EL MAR", "EN EL CAMPO", "EN UN NIDO"], "EN EL MAR", "AMBIENTE DE AGUA.", n="aplicar")],
 [1, SA("¿DÓNDE VIVE LA VACA? ¿EN LA TIERRA O EN EL AGUA?", acepta("TIERRA", "EN LA TIERRA"), "EN LA TIERRA.", n="aplicar")],
 [1, MC("SOFI DICE QUE LA RANA SOLO VIVE EN EL AGUA. ¿QUÉ LE FALTÓ?", ["TAMBIÉN VIVE EN LA TIERRA", "TAMBIÉN VUELA", "NADA"], "TAMBIÉN VIVE EN LA TIERRA", "VIVE EN LOS DOS.", n="error")],
 [2, MC("¿QUÉ NECESITAN LOS SERES VIVOS?", ["AGUA, ALIMENTO Y AIRE", "JUGUETES Y PELOTAS", "SOLO RUIDO Y LUZ"], "AGUA, ALIMENTO Y AIRE", "LAS CUATRO COSAS.", n="recordar")],
 [2, MC("¿POR QUÉ SE SECÓ LA PLANTA?", ["LE FALTÓ AGUA", "TUVO MUCHA AGUA", "TUVO AIRE"], "LE FALTÓ AGUA", "SIN AGUA SE SECA.", n="analizar")],
 [2, SA("COMPLETÁ: TODOS LOS SERES VIVOS NECESITAN ___", acepta("AGUA", "ALIMENTO", "AIRE", "COMIDA"), "AGUA, ALIMENTO Y AIRE.", n="recordar")],
 [3, MC("¿QUIÉN VIVE EN LA LAGUNA?", ["EL PATO", "EL CAMELLO", "EL OSO POLAR"], "EL PATO", "NADA EN LA LAGUNA.", n="aplicar")],
 [3, MC("LOS JUNCOS SON…", ["PLANTAS DE LA ORILLA", "PECES", "PIEDRAS"], "PLANTAS DE LA ORILLA", "CRECEN EN LA ORILLA.", n="recordar")],
 [3, MC("¿QUÉ ES UN HABITANTE?", ["UN SER VIVO DE UN LUGAR", "UNA PIEDRA DEL LUGAR", "EL AGUA DEL LUGAR"], "UN SER VIVO DE UN LUGAR", "COMO EL PATO EN LA LAGUNA.", n="recordar")],
 [4, ORD("ORDENÁ LA VIDA DE UNA PLANTA.", ["CRECE", "NACE", "DA SEMILLAS"], ["NACE", "CRECE", "DA SEMILLAS"], "NACE, CRECE, DA SEMILLAS.", n="aplicar")],
 [4, MC("¿CUÁL NO ES UN SER VIVO?", ["LA ROCA", "EL GATO", "EL ÁRBOL"], "LA ROCA", "NO NACE NI CRECE.", n="aplicar")],
 [4, MC("EL AUTO SE MUEVE. ¿ESTÁ VIVO?", ["NO: NO NACE NI CRECE", "SÍ: SE MUEVE", "SÍ: HACE RUIDO"], "NO: NO NACE NI CRECE", "MOVERSE NO ALCANZA.", n="error")],
 [4, SA("NOMBRÁ UN SER VIVO DE TU CASA.", acepta("PERRO", "GATO", "PLANTA", "MAMÁ", "MAMA", "PAPÁ", "PAPA", "YO", "PEZ", "PÁJARO", "HERMANO", "HERMANA", "FLOR"), "POR EJEMPLO: UNA PLANTA.", n="aplicar")],
]
M = {"subject_id": "a3d2a4e5-78ec-4a92-9233-9f5f558a7ca0", "tema": 4, "estilo": "primeros",
     "practica": "Práctica general: quién vive dónde", "examen_titulo": "Nivel jefe: quién vive dónde",
     "niveles": {"1": N1, "2": N2, "3": N3, "4": N4}, "act": ACT, "examen": EXAMEN}
json.dump(M, open(os.path.join(AQUI, "mision-4.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
