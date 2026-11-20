# -*- coding: utf-8 -*-
"""Ciencias Naturales Integradas I · Misión 1 · Ciencia y método. Genera mision-1.json (se carga con cargar_mision)."""
import os, sys, io, base64, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "matematica-1", "mision-4"))
from base import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
V, O, C = "#0e7c7b", "#243b3f", "#d8f0ea"
def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=16); o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()
def IMG(t, pie, desc, b64): return {"tipo":"imagen","imagen_tipo":"diagrama","titulo":t,"texto":pie,"imagen_descripcion":desc,"imagen_fuente":"Dibujo propio (matplotlib).","png_base64":b64}
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
N1=NV("Vas a reconocer el sujeto y el predicado de una oración.",["Sujeto y predicado","Cómo encontrar el sujeto","La concordancia","Sujeto al final"],[
 S(1,"Sujeto y predicado",[D("Sujeto","De quién se habla en la oración."),D("Predicado","Lo que se dice del sujeto."),T("Ejemplo",["Sujeto","Predicado"],[["Los vecinos del último piso","discutían a los gritos cada noche."]])]),
 S(1,"Cómo encontrar el sujeto",[P("Buscá el <b>verbo</b> y preguntale <b>¿quién?</b>: la respuesta es el sujeto. ¿Quién juega? Los chicos del barrio.")]),
 S(2,"Sujeto compuesto",[D("Sujeto compuesto","Tiene dos o más núcleos unidos por un nexo (y, ni, o). El verbo va en plural: \"Mi hermana y su mejor amiga viajaron a Bariloche\".")]),
 S(2,"Concordancia y orden",[P("Sujeto y verbo <b>concuerdan</b> en número: el chico juega / los chicos juegan. El sujeto <b>no siempre va primero</b>: \"Desde la ventanilla del tren se veían las sierras cordobesas\" (¿qué se veía? las sierras: el verbo está en plural porque el sujeto es plural).")])],
 {"titulo":"encontrar el sujeto","planteo":"\"En verano florecen los jacarandás.\"","pasos":["Verbo: florecen.","¿Qué florece? Los jacarandás.","Sujeto: los jacarandás. Predicado: en verano florecen."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Para encontrar el sujeto, le pregunto ___ al verbo.","\"Los chicos juega\" está mal: sujeto y verbo deben ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres oraciones sobre tu familia y subrayá el sujeto de cada una."},
 {"titulo":"Pasalo a plural","texto":"Si dudás cuál es el sujeto, pasá la oración a plural: la palabra que obliga a cambiar el verbo es parte del sujeto."},
 ["Creer que el sujeto siempre va primero.","No hacer concordar sujeto y verbo."],
 RS(("Sujeto","De quién se habla."),("Predicado","Lo que se dice."),("Truco","Verbo + ¿quién?"),("Concordancia","Mismo número.")),
 G(("Oración","Unidad con sentido completo."),("Sujeto","De quién se habla."),("Predicado","Lo que se dice del sujeto."),("Concordancia","Acuerdo en número entre sujeto y verbo.")),
 ["¿Cuál es el sujeto de \"Mis primos llegaron tarde\"?","¿Cuál es el verbo de \"Los perros ladran fuerte\"?","¿Qué pregunta se le hace al verbo para encontrar el sujeto?","Corregí: \"Los chicos juega\". Escribí solo el verbo correcto."],
 [["mis primos"],["ladran"],["quien","quién","¿quién?","¿quien?"],["juegan"]],
 {"incompleto":"¿Quién? Concordar.","solo":"Respuesta personal: el sujeto responde a ¿quién?","carpeta":["Mis primos.","Ladran.","¿Quién?","Juegan."]})
N2=NV("Vas a reconocer los núcleos y los modificadores del sujeto.",["El núcleo","Modificador directo","Modificador indirecto","Aposición"],[
 S(1,"El núcleo",[D("Núcleo","La palabra más importante: en el sujeto, un sustantivo (N); en el predicado, el verbo (NV).")]),
 S(1,"Los modificadores",[T("Modificadores del sujeto",["Nombre","Qué es","Ejemplo"],[["MD (directo)","Artículo o adjetivo pegado al núcleo","la perra, perra flaca"],["MI (indirecto)","Preposición + palabra","perra de Juan"],["Aposición","Sustantivo que aclara, entre comas","Juan, mi vecino,"]])]),
 S(2,"Análisis completo",[T("El hermano menor de Sofía, un fanático del ajedrez, ganó el torneo.",["Palabras","Función"],[["El","MD"],["hermano","N"],["menor","MD"],["de Sofía","MI"],["un fanático del ajedrez","aposición"],["ganó","NV"]])]),
 S(2,"Preposiciones",[P("El MI siempre empieza con una preposición: a, ante, bajo, con, contra, de, desde, en, entre, hacia, hasta, para, por, sin, sobre, tras.")])],
 {"titulo":"analizar","planteo":"\"El gato negro del vecino duerme.\"","pasos":["Verbo: duerme (NV).","¿Quién duerme? El gato negro del vecino: sujeto.","Núcleo: gato. MD: el, negro. MI: del vecino."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["En \"la casa de piedra\", \"de piedra\" es un ___ .","La aposición va entre ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un sujeto con MD, MI y aposición sobre alguien que conozcas."},
 {"titulo":"Buscá la preposición","texto":"Si un modificador empieza con de, con, en, sin o para, es indirecto."},
 ["Marcar un MI sin preposición.","Olvidar las comas de la aposición."],
 RS(("Núcleo","Sustantivo o verbo."),("MD","Artículo o adjetivo."),("MI","Preposición + palabra."),("Aposición","Entre comas.")),
 G(("Núcleo","Palabra principal."),("Sustantivo","Palabra que nombra."),("Preposición","Palabra que enlaza: de, con, en…"),("Aposición","Sustantivo que aclara, entre comas.")),
 ["¿Cuál es el núcleo de \"La perra de Juan\"?","En \"el té sin azúcar\", ¿qué es \"sin azúcar\": MD o MI?","¿Entre qué signos va la aposición?","En \"El gato negro duerme\", ¿qué es \"negro\": MD o MI?"],
 [["perra"],["mi","modificador indirecto"],["comas","entre comas"],["md","modificador directo"]],
 {"incompleto":"MI. Comas.","solo":"Respuesta personal con MD, MI y aposición.","carpeta":["Perra.","MI.","Entre comas.","MD."]})
N3=NV("Vas a reconocer oraciones con sujeto tácito y oraciones unimembres.",["Sujeto tácito","Bimembres y unimembres","Unimembres típicas"],[
 S(1,"Sujeto tácito",[D("Sujeto tácito","No está escrito, pero se sabe por la terminación del verbo."),E("Fuimos al cine el sábado","¿Quiénes fuimos?",["La terminación -imos indica nosotros.","Sujeto tácito: nosotros.","Toda la oración es predicado."])]),
 S(1,"Bimembres y unimembres",[D("Bimembre","Tiene sujeto y predicado."),D("Unimembre","No se puede dividir en sujeto y predicado.")]),
 S(2,"Unimembres típicas",[T("Unimembres",["Tipo","Ejemplo"],[["Clima","Llueve. Amanece."],["Hay / hace","Hay pan. Hace frío."],["Exclamaciones","¡Qué lindo día!"],["Sin verbo","Prohibido fumar."]]),P("Ojo: en \"Hay muchos libros\", <b>muchos libros no es sujeto</b>. Con hay, la oración es unimembre.")])],
 {"titulo":"clasificar","planteo":"\"Comimos pizza\" y \"Hace calor\".","pasos":["Comimos: sujeto tácito nosotros. Es bimembre.","Hace calor: nadie hace la acción. Es unimembre."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["En \"Salieron temprano\", el sujeto tácito es ___ .","\"Nieva en la montaña\" es una oración ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí dos oraciones unimembres sobre el clima de hoy y una con sujeto tácito."},
 {"titulo":"¿Quién lo hace?","texto":"Si no hay nadie que haga la acción (llueve, hay, hace), es unimembre; si alguien la hace pero no está escrito, es tácito."},
 ["Creer que con hay hay sujeto.","Confundir tácito con sin sujeto."],
 RS(("Tácito","Se sabe por el verbo."),("Bimembre","Sujeto + predicado."),("Unimembre","No se divide."),("Típicas","Clima, hay, hace.")),
 G(("Tácito","Que no está escrito pero se entiende."),("Desinencia","Terminación del verbo."),("Bimembre","De dos miembros."),("Unimembre","De un solo miembro.")),
 ["¿Cuál es el sujeto tácito de \"Fuimos al cine\"?","\"Llueve mucho\": ¿bimembre o unimembre?","\"Hay pan en la mesa\": ¿bimembre o unimembre?","¿Cuál es el sujeto tácito de \"Estudié toda la tarde\"?"],
 [["nosotros","nosotras"],["unimembre"],["unimembre"],["yo"]],
 {"incompleto":"Ellos o ellas. Unimembre.","solo":"Respuesta personal.","carpeta":["Nosotros.","Unimembre.","Unimembre.","Yo."]})
N4=NV("Vas a analizar oraciones completas y escribir oraciones expandidas.",["Análisis en 5 pasos","Expandir una oración"],[
 S(1,"Análisis en 5 pasos",[T("Pasos",["Paso","Qué hago"],[["1","Marco el verbo (NV)"],["2","Pregunto ¿quién? y encuentro el sujeto"],["3","Marco el núcleo del sujeto"],["4","Marco MD, MI y aposición"],["5","Digo si es bimembre o unimembre"]])]),
 S(1,"Un análisis completo",[T("Mi abuela, una gran cocinera, prepara empanadas.",["Palabras","Función"],[["Mi","MD"],["abuela","N"],["una gran cocinera","aposición"],["prepara","NV"],["Clase","bimembre"]])]),
 S(2,"Expandir",[P("Una oración pobre dice poco: \"Perro ladró\". Con modificadores se entiende y se ve: \"El perro negro del vecino ladró toda la noche\".")])],
 {"titulo":"expandir","planteo":"Expandí \"Chica canta\".","pasos":["Agrego MD: La chica.","Agrego MI: La chica de rulos.","Agrego aposición: La chica de rulos, mi prima,","Resultado: La chica de rulos, mi prima, canta en el coro."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El primer paso del análisis es marcar el ___ .","Para agregar un MI uso una ___ ."]},
 {"titulo":"tu turno","planteo":"Expandí \"Auto frenó\" con MD, MI y aposición, y analizá tu oración."},
 {"titulo":"Empezá por el verbo","texto":"Sin el verbo no hay pregunta, y sin pregunta no aparece el sujeto."},
 ["Analizar sin encontrar primero el verbo.","Escribir oraciones sin modificadores que no se entienden."],
 RS(("Paso 1","El verbo."),("Paso 2","¿Quién? → sujeto."),("Pasos 3 y 4","Núcleo y modificadores."),("Escribir","Expandir.")),
 G(("Analizar","Separar una oración en sus partes."),("Expandir","Agregar modificadores."),("NV","Núcleo verbal.")),
 ["¿Cuál es el núcleo del sujeto en \"Mi abuela, una gran cocinera, prepara empanadas\"?","En esa oración, ¿cuál es el verbo?","¿Qué es \"una gran cocinera\" en esa oración?","¿Cuál es el primer paso del análisis: buscar el verbo o el sujeto?"],
 [["abuela"],["prepara"],["aposicion","aposición","una aposición","una aposicion"],["verbo","el verbo","buscar el verbo"]],
 {"incompleto":"Verbo. Preposición.","solo":"Respuesta personal: revisá MD, MI y aposición.","carpeta":["Abuela.","Prepara.","Aposición.","Buscar el verbo."]})
ACT={"1":[{"t":"tap_text","p":"Tocá las palabras del sujeto: \"Los chicos del barrio juegan en la plaza\".","o":{"segmentos":["Los","chicos","del","barrio","juegan","en","la","plaza"],"modo":"palabras"},"r":{"tocar":[0,1,2,3]},"e":"¿Quién juega? Los chicos del barrio."},MC("¿Cuál es el sujeto de \"En la esquina de mi casa abrió una heladería artesanal\"?",["En la esquina de mi casa","una heladería artesanal","mi casa","abrió"],"una heladería artesanal","¿Qué abrió? Lo que empieza con preposición nunca es sujeto.")],
"2":[MC("En \"La casa de piedra\", \"de piedra\" es…",["MD","MI","Aposición","Núcleo"],"MI","Empieza con preposición."),{"t":"matching","p":"Uní cada parte con su función.","o":{"izquierda":["La","perra","de Juan","una galga"],"derecha":["MD","N","MI","Aposición"]},"r":{"pares":{"La":"MD","perra":"N","de Juan":"MI","una galga":"Aposición"}},"e":"La perra de Juan, una galga, corre."}],
"3":[{"t":"classify","p":"¿Sujeto tácito o unimembre?","o":{"elementos":["Comimos pizza.","Salió temprano.","Hace calor.","Llovió anoche."],"categorias":["Sujeto tácito","Unimembre"]},"r":{"categorias":{"Comimos pizza.":"Sujeto tácito","Salió temprano.":"Sujeto tácito","Hace calor.":"Unimembre","Llovió anoche.":"Unimembre"}},"e":"En las unimembres nadie hace la acción."},MC("\"Hay muchos libros\" es…",["Bimembre","Unimembre"],"Unimembre","Con hay no hay sujeto.")],
"4":[{"t":"ordering","p":"Ordená los pasos del análisis.","o":["Marco MD, MI y aposición","Marco el verbo","Marco el núcleo del sujeto","Pregunto ¿quién?"],"r":{"orden":["Marco el verbo","Pregunto ¿quién?","Marco el núcleo del sujeto","Marco MD, MI y aposición"]},"e":"Siempre se empieza por el verbo."},MC("¿Cuál es la oración más expandida?",["Perro ladró.","El perro ladró.","El perro negro del vecino ladró toda la noche.","Ladró."],"El perro negro del vecino ladró toda la noche.","Tiene MD, MI y más información.")],
"5":[MC("Relámpago. El sujeto responde a…",["¿Quién?","¿Cuándo?","¿Dónde?"],"¿Quién?","Se pregunta al verbo.",tiempo=20),MC("Relámpago. El MI empieza con…",["Una preposición","Un artículo","Un verbo"],"Una preposición","De, con, en…",tiempo=20),MC("Relámpago. \"Nieva\" es…",["Unimembre","Bimembre"],"Unimembre","Clima.",tiempo=20),MC("Relámpago. La aposición va…",["Entre comas","Entre paréntesis siempre","Sin signos"],"Entre comas","Aclara al núcleo.",tiempo=20)]}
EXAMEN=[[1,MC("\"Mi tío y su socio abrieron una panadería.\" ¿Cómo es el sujeto?",["Compuesto: dos núcleos","Simple: un núcleo","Tácito","No tiene sujeto"],"Compuesto: dos núcleos","Tío y socio, unidos por y.")],[1,MC("¿Cuál es el sujeto de \"En verano florecen los jacarandás\"?",["En verano","florecen","los jacarandás","verano"],"los jacarandás","¿Qué florece?")],[1,VF("El sujeto siempre está al principio de la oración.","Falso","Puede ir al final.")],
[2,MC("En \"El té sin azúcar está frío\", ¿qué es \"sin azúcar\"?",["MD","MI","Aposición","NV"],"MI","Empieza con preposición.")],[2,MC("\"El perro del vecino, un ovejero alemán, ladraba toda la noche.\" ¿Qué es \"un ovejero alemán\"?",["Aposición","MI","MD","Núcleo"],"Aposición","Sustantivo con modificadores, entre comas, que aclara.")],[2,VF("La aposición va entre comas.","Verdadero","Aclara al núcleo.")],
[3,MC("¿Cuál es el sujeto tácito de \"Fuimos al cine\"?",["Yo","Nosotros","Ellos","No tiene"],"Nosotros","Lo indica el verbo.")],[3,MC("\"Hubo varios accidentes en la ruta.\" ¿Qué oración es?",["Unimembre","Bimembre con sujeto \"varios accidentes\"","Con sujeto tácito \"ellos\"","Bimembre con sujeto \"la ruta\""],"Unimembre","El verbo no concuerda: hubo un accidente, hubo varios.")],[3,VF("En \"Hay pan\", \"pan\" es el sujeto.","Falso","Con hay la oración es unimembre.")],
[4,MC("¿Cuál es el primer paso del análisis?",["Marcar el verbo","Marcar la aposición","Contar palabras","Buscar comas"],"Marcar el verbo","Después se pregunta ¿quién?")],[4,MC("En \"Mi abuela, una gran cocinera, prepara empanadas\", ¿qué es \"prepara\"?",["NV","N","MD","MI"],"NV","Es el núcleo del predicado.")],[4,MC("¿Qué hace un MI a una oración?",["Agrega información con preposición","Cambia el verbo","La vuelve unimembre","Nada"],"Agrega información con preposición","Expande el sujeto.")],[4,VF("\"Perro ladró\" es una oración bien expandida.","Falso","Le faltan modificadores.")]]
M={"subject_id":"e1b0726d-08aa-4d9e-9060-18489f529da2","tema":4,"practica":"Práctica general: sujeto y predicado","examen_titulo":"Nivel jefe: sujeto y predicado","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-4.json"),"w"),ensure_ascii=False); print("ok")
