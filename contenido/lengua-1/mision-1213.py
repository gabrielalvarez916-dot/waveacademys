# -*- coding: utf-8 -*-
"""Lengua y Literatura I · Misión 12 (Clases de palabras) y Misión 13 (Argumentar una opinión)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}
SID = "e1b0726d-08aa-4d9e-9060-18489f529da2"

FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,ref,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":ref,"e":e,**k}
# ================= MISIÓN 12: CLASES DE PALABRAS =================
A1=NV("Vas a reconocer sustantivos y adjetivos, sus clases y cómo concuerdan.",["El sustantivo","Clases de sustantivos","El adjetivo","La concordancia"],[
 S(1,"El sustantivo",[D("Sustantivo","Palabra que nombra personas, animales, cosas, lugares, ideas o sentimientos."),T("Clases",["Clase","Ejemplo"],[["Común","niña, ciudad, perro"],["Propio","Sofía, Córdoba, Rex"],["Concreto","mesa, río, gato"],["Abstracto","alegría, libertad, miedo"]])]),
 S(1,"Género y número",[P("El sustantivo tiene <b>género</b> (masculino o femenino) y <b>número</b> (singular o plural): <i>el gato, las gatas</i>.")]),
 S(2,"El adjetivo",[D("Adjetivo","Palabra que acompaña al sustantivo y dice cómo es: calificativos (alto, simpática) o determinativos (esta, tres, mi)."),P("Los adjetivos <b>concuerdan</b> con el sustantivo en género y número: <i>casas blancas</i>.")]),
 S(2,"Concordancia",[T("Corregí",["Mal","Bien"],[["los niños cansada","los niños cansados"],["una casa grandes","una casa grande"],["mis amigo simpático","mis amigos simpáticos"]])])],
 {"titulo":"clasificar","planteo":"¿«Alegría» es concreto o abstracto?","pasos":["No se puede tocar ni ver.","Es un sentimiento.","Es un sustantivo abstracto."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los sustantivos que nombran sentimientos o ideas son ___ .","El adjetivo concuerda con el sustantivo en género y ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí cuatro sustantivos de clases distintas y un adjetivo para cada uno."},
 {"titulo":"Quién acompaña a quién","texto":"Para saber si concuerdan, buscá el sustantivo y fijate en su género y número."},
 ["Dejar el adjetivo en singular con un sustantivo plural.","Confundir abstracto con propio."],
 RS(("Sustantivo","Nombra."),("Clases","Común, propio, concreto, abstracto."),("Adjetivo","Dice cómo es."),("Concordancia","Género y número.")),
 G(("Sustantivo","Palabra que nombra."),("Adjetivo","Palabra que dice cómo es algo."),("Concordancia","Acuerdo en género y número.")),
 ["¿«Libertad» es sustantivo concreto o abstracto?","¿«Córdoba» es sustantivo común o propio?","¿Qué palabra acompaña al sustantivo y dice cómo es?","Corregí: «las flores blanco». Escribí solo el adjetivo correcto."],
 [["abstracto","es abstracto"],["propio","es propio"],["adjetivo","el adjetivo"],["blancas"]],
 {"incompleto":"Abstractos. Número.","solo":"Perro (común), Rex (propio), mesa (concreto), alegría (abstracto).","carpeta":["Abstracto.","Propio.","El adjetivo.","Blancas."]})
A2=NV("Vas a reconocer las formas del verbo y distinguir sus modos: indicativo, subjuntivo e imperativo.",["Persona, número y tiempo","El modo","Formas no personales","Practicar"],[
 S(1,"Persona, número y tiempo",[D("Verbo","Palabra que expresa acciones, estados o procesos y varía en persona, número, tiempo y modo."),T("Un verbo conjugado",["Forma","Persona","Número","Tiempo"],[["canto","1.ª","singular","presente"],["cantaron","3.ª","plural","pasado"],["cantaremos","1.ª","plural","futuro"]])]),
 S(1,"El modo",[T("Tres modos",["Modo","Expresa","Ejemplo"],[["Indicativo","Hechos reales","Estudio todos los días"],["Subjuntivo","Deseos, dudas, posibilidades","Ojalá estudie más"],["Imperativo","Órdenes, pedidos","Estudiá ahora"]])]),
 S(2,"Formas no personales",[T("No indican persona",["Forma","Terminación","Ejemplo"],[["Infinitivo","-ar, -er, -ir","cantar"],["Gerundio","-ando, -iendo","cantando"],["Participio","-ado, -ido","cantado"]])]),
 S(2,"Practicar",[P("Para reconocer el modo, preguntate: ¿afirmo un hecho (indicativo), deseo o dudo (subjuntivo) o doy una orden (imperativo)?")])],
 {"titulo":"identificar","planteo":"¿En qué modo está «Ojalá llueva mañana»?","pasos":["Expresa un deseo.","El deseo va con subjuntivo.","Modo subjuntivo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El modo que expresa órdenes es el ___ .","Los hechos reales se expresan en modo ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una oración en cada modo."},
 {"titulo":"Hecho, deseo u orden","texto":"El modo depende de lo que querés decir, no del tiempo."},
 ["Confundir tiempo con modo.","Creer que el gerundio es una persona."],
 RS(("Verbo","Persona, número, tiempo, modo."),("Indicativo","Hechos."),("Subjuntivo","Deseos y dudas."),("Imperativo","Órdenes.")),
 G(("Modo","Manera de expresar la acción."),("Conjugar","Cambiar el verbo según persona, número, tiempo y modo."),("Gerundio","Forma terminada en -ando o -iendo.")),
 ["¿En qué modo está «Cerrá la puerta»?","¿En qué modo está «Ojalá gane»?","¿Cuál es el infinitivo de «cantaron»?","¿«Cantando» es gerundio o participio?"],
 [["imperativo","en imperativo","modo imperativo"],["subjuntivo","en subjuntivo","modo subjuntivo"],["cantar"],["gerundio","es gerundio"]],
 {"incompleto":"Imperativo. Indicativo.","solo":"Indicativo: leo. Subjuntivo: ojalá lea. Imperativo: leé.","carpeta":["Imperativo.","Subjuntivo.","Cantar.","Gerundio."]})
A3=NV("Vas a reconocer adverbios y preposiciones y explicar qué función cumplen.",["El adverbio","Clases de adverbios","La preposición","Practicar"],[
 S(1,"El adverbio",[D("Adverbio","Palabra invariable que modifica a un verbo, un adjetivo u otro adverbio."),P("No cambia de género ni de número: <i>corre rápido, corren rápido</i>.")]),
 S(1,"Clases",[T("Qué indican",["Clase","Ejemplos"],[["Lugar","aquí, allá, cerca, lejos"],["Tiempo","hoy, ayer, siempre, nunca"],["Modo","bien, mal, rápido, despacio"],["Cantidad","muy, poco, mucho, bastante"],["Afirmación y negación","sí, claro, no, tampoco"]])]),
 S(2,"La preposición",[D("Preposición","Palabra invariable que une una palabra con su complemento."),P("Las preposiciones son: <b>a, ante, bajo, con, contra, de, desde, en, entre, hacia, hasta, para, por, según, sin, sobre, tras</b>.")]),
 S(2,"Practicar",[P("En <i>Vivo cerca de la plaza</i>, <b>cerca</b> es adverbio de lugar y <b>de</b> es preposición que une con <i>la plaza</i>.")])],
 {"titulo":"clasificar","planteo":"¿Qué clase de adverbio es «siempre»?","pasos":["Dice cuándo ocurre algo.","Es un adverbio de tiempo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las palabras invariables que modifican un verbo son los ___ .","Las que unen una palabra con su complemento son las ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una oración con un adverbio de lugar y una preposición."},
 {"titulo":"No cambian","texto":"Adverbios y preposiciones son invariables: no tienen género ni número."},
 ["Poner plural a un adverbio.","Confundir adverbio con adjetivo."],
 RS(("Adverbio","Modifica."),("Clases","Lugar, tiempo, modo, cantidad."),("Preposición","Une."),("Invariables","Sin género ni número.")),
 G(("Adverbio","Palabra invariable que modifica un verbo."),("Preposición","Palabra que une."),("Invariable","Que no cambia de forma.")),
 ["¿«Aquí» es adverbio de lugar o de tiempo?","¿«Mucho» es adverbio de cantidad o de modo?","¿«Sin» es preposición o adverbio?","¿Los adverbios cambian de género y número? Respondé sí o no."],
 [["lugar","de lugar","adverbio de lugar"],["cantidad","de cantidad","adverbio de cantidad"],["preposicion","preposición","es preposicion","es preposición"],["no"]],
 {"incompleto":"Adverbios. Preposiciones.","solo":"Vivo cerca de la plaza: cerca (adverbio de lugar), de (preposición).","carpeta":["De lugar.","De cantidad.","Preposición.","No."]})
A4=NV("Vas a reconocer pronombres y conjunciones y usar cada uno para evitar repeticiones y unir ideas.",["El pronombre","Clases de pronombres","La conjunción","Unir oraciones"],[
 S(1,"El pronombre",[D("Pronombre","Palabra que reemplaza a un sustantivo para no repetirlo."),P("<i>Sofía llegó tarde. Ella se disculpó.</i> «Ella» reemplaza a «Sofía».")]),
 S(1,"Clases",[T("Pronombres",["Clase","Ejemplos"],[["Personales","yo, tú/vos, él, ella, nosotros"],["Posesivos","mío, tuyo, suyo, nuestro"],["Demostrativos","este, ese, aquel"]])]),
 S(2,"La conjunción",[D("Conjunción","Palabra invariable que une palabras u oraciones."),T("Clases",["Función","Conjunciones"],[["Suma","y, e, ni"],["Opción","o, u"],["Oposición","pero, sino, aunque"],["Causa","porque"]])]),
 S(2,"Unir oraciones",[P("Para evitar repeticiones: <i>Tengo un perro. El perro es grande.</i> → <i>Tengo un perro y es grande.</i>")])],
 {"titulo":"reemplazar","planteo":"Evitá repetir: «Lucas compró un libro. Lucas leyó el libro enseguida».","pasos":["Reemplazar el segundo Lucas por él.","Reemplazar el libro por lo.","Lucas compró un libro y lo leyó enseguida."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La palabra que reemplaza a un sustantivo es el ___ .","La palabra invariable que une ideas es la ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí dos oraciones repetitivas y mejorá cada una con un pronombre."},
 {"titulo":"Menos repeticiones","texto":"Si repetís una palabra, probá con un pronombre."},
 ["Repetir el sustantivo en cada oración.","Confundir pero con porque."],
 RS(("Pronombre","Reemplaza."),("Clases","Personales, posesivos."),("Conjunción","Une."),("Oposición","Pero.")),
 G(("Pronombre","Reemplaza a un sustantivo."),("Conjunción","Une palabras u oraciones."),("Nexo","Palabra que une.")),
 ["¿Qué palabra reemplaza a un sustantivo?","¿«Pero» es una conjunción de oposición o de causa?","¿«Este» es pronombre demostrativo o personal?","En «Sofía llegó y ella se disculpó», ¿qué pronombre reemplaza a Sofía?"],
 [["pronombre","el pronombre"],["oposicion","oposición","de oposicion","de oposición"],["demostrativo","es demostrativo"],["ella"]],
 {"incompleto":"Pronombre. Conjunción.","solo":"Lucas compró un libro y lo leyó enseguida.","carpeta":["El pronombre.","De oposición.","Demostrativo.","Ella."]})
ACT12={"1":[TT("Tocá los adjetivos: «La casa grande tiene ventanas azules».",["La","casa","grande","tiene","ventanas","azules"],[2,5],"Grande y azules dicen cómo son."),{"t":"classify","p":"¿Concreto o abstracto?","o":{"elementos":["mesa","alegría","río","libertad"],"categorias":["Concreto","Abstracto"]},"r":{"categorias":{"mesa":"Concreto","alegría":"Abstracto","río":"Concreto","libertad":"Abstracto"}},"e":"Lo que se toca o ve es concreto."}],
 "2":[{"t":"matching","p":"Uní cada modo con su expresión.","o":{"izquierda":["Indicativo","Subjuntivo","Imperativo"],"derecha":["Hechos reales","Deseos y dudas","Órdenes"]},"r":{"pares":{"Indicativo":"Hechos reales","Subjuntivo":"Deseos y dudas","Imperativo":"Órdenes"}},"e":"Cada modo tiene su valor."},FB("Cantar, cantando y cantado son formas ___ personales.",[["no"]],"No indican persona.")],
 "3":[FB("«Hoy» es un adverbio de ___ .",[["tiempo"]],"Dice cuándo."),MS("Marcá las preposiciones:",["con","rápido","sin","aquí","sobre"],["con","sin","sobre"],"Rápido y aquí son adverbios.")],
 "4":[{"t":"classify","p":"¿Pronombre o conjunción?","o":{"elementos":["ella","pero","yo","porque"],"categorias":["Pronombre","Conjunción"]},"r":{"categorias":{"ella":"Pronombre","pero":"Conjunción","yo":"Pronombre","porque":"Conjunción"}},"e":"Reemplazar o unir."},{"t":"ordering","p":"Ordená para armar la oración.","o":["se disculpó","Ella","llegó tarde y"],"r":{"orden":["Ella","llegó tarde y","se disculpó"]},"e":"Sujeto, verbo y conjunción."}],
 "5":[MC("Relámpago. «Alegría» es sustantivo…",["Abstracto","Concreto","Propio"],"Abstracto","Un sentimiento.",tiempo=20),VF("Relámpago. «Ojalá venga» está en subjuntivo.","Verdadero","Expresa un deseo.",tiempo=20),MC("Relámpago. «Siempre» es adverbio de…",["Tiempo","Lugar","Modo"],"Tiempo","Cuándo.",tiempo=20),VF("Relámpago. Los pronombres unen oraciones.","Falso","Reemplazan sustantivos.",tiempo=20)]}
EX12=[[1,MC("¿Qué palabra nombra personas, cosas o ideas?",["Sustantivo","Verbo","Adverbio","Preposición"],"Sustantivo","Nombra.")],
 [1,MC("«Libertad» es un sustantivo…",["Abstracto","Concreto","Propio","Plural"],"Abstracto","Es una idea.")],
 [1,VF("El adjetivo concuerda con el sustantivo en género y número.","Verdadero","Casas blancas.")],
 [2,MC("El modo que expresa órdenes es…",["Imperativo","Indicativo","Subjuntivo","Gerundio"],"Imperativo","Cerrá la puerta.")],
 [2,MS("Formas no personales del verbo:",["Infinitivo","Gerundio","Participio","Imperativo"],["Infinitivo","Gerundio","Participio"],"El imperativo es un modo.")],
 [2,FB("Los hechos reales se expresan en modo ___ .",[["indicativo"]],"Indicativo.")],
 [3,MC("«Aquí» es adverbio de…",["Lugar","Tiempo","Modo","Cantidad"],"Lugar","Dice dónde.")],
 [3,MS("Preposiciones:",["con","sin","rápido","hacia"],["con","sin","hacia"],"Rápido es adverbio.")],
 [3,VF("Los adverbios cambian de género y número.","Falso","Son invariables.")],
 [4,MC("El pronombre…",["Reemplaza a un sustantivo","Une oraciones","Nombra","Modifica al verbo"],"Reemplaza a un sustantivo","Evita repeticiones.")],
 [4,MC("«Pero» es una conjunción de…",["Oposición","Suma","Opción","Causa"],"Oposición","Contrasta ideas.")],
 [4,FB("La palabra que une ideas se llama ___ .",[["conjuncion","conjunción","nexo"]],"Une palabras u oraciones.")],
 [4,VF("«Este» puede ser un pronombre demostrativo.","Verdadero","Señala algo.")]]
M12={"subject_id":SID,"tema":12,"practica":"Práctica general: clases de palabras","examen_titulo":"Nivel jefe: clases de palabras","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT12,"examen":EX12}

# ================= MISIÓN 13: ARGUMENTAR UNA OPINIÓN =================
B1=NV("Vas a distinguir un hecho de una opinión y reconocer las marcas de la subjetividad.",["Hecho","Opinión","Marcas de opinión","Cómo comprobar"],[
 S(1,"Hecho y opinión",[T("No son lo mismo",["","Hecho","Opinión"],[["Qué es","Algo que se puede comprobar","Lo que alguien piensa o siente"],["Ejemplo","El colegio abre a las 8","El colegio es aburrido"],["Cómo se prueba","Con datos","No se prueba: se argumenta"]])]),
 S(1,"Marcas de opinión",[T("Qué delata una opinión",["Marca","Ejemplo"],[["Verbos de pensamiento","creo, pienso, me parece"],["Adjetivos valorativos","injusto, genial, aburrido"],["Exageraciones","siempre, nunca, todos"]])]),
 S(2,"Comprobar",[P("Para saber si algo es un hecho, preguntate: ¿puedo <b>verificarlo</b> con una fuente, un número o una prueba? Si la respuesta es no, es una opinión.")]),
 S(2,"Mezcla",[P("Muchas oraciones mezclan ambos: <i>\"El nuevo parque, que abrió el año pasado, es hermoso\"</i>. Abrir el año pasado es un hecho; hermoso es una opinión.")])],
 {"titulo":"clasificar","planteo":"¿«La ciudad tiene tres millones de habitantes» es hecho u opinión?","pasos":["Se puede verificar con datos.","Es un hecho."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que se puede comprobar es un ___ .","Lo que alguien piensa o siente es una ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres hechos y tres opiniones sobre tu escuela."},
 {"titulo":"¿Puedo probarlo?","texto":"Si lo podés probar con datos, es un hecho; si no, es una opinión."},
 ["Creer que una opinión es siempre falsa.","Tomar un dato dudoso como hecho."],
 RS(("Hecho","Se comprueba."),("Opinión","Se argumenta."),("Marcas","Creo, adjetivos, siempre."),("Mezcla","Pueden ir juntos.")),
 G(("Hecho","Lo que se puede comprobar."),("Opinión","Lo que alguien piensa."),("Valorativo","Que expresa un juicio.")),
 ["«El colegio abre a las 8», ¿es hecho u opinión?","«El colegio es aburrido», ¿es hecho u opinión?","¿«Creo que» marca un hecho o una opinión?","¿Se puede comprobar una opinión con datos? Respondé sí o no."],
 [["hecho","es un hecho"],["opinion","opinión","es una opinion","es una opinión"],["opinion","opinión","una opinion","una opinión"],["no"]],
 {"incompleto":"Hecho. Opinión.","solo":"Hechos: hay 40 alumnos. Opiniones: la escuela es linda.","carpeta":["Hecho.","Opinión.","Opinión.","No."]})
B2=NV("Vas a armar una opinión con tesis y argumentos de distintos tipos.",["La tesis","Tipos de argumentos","Conectores","Un párrafo argumentativo"],[
 S(1,"La tesis",[D("Tesis","Idea principal que se defiende en un texto argumentativo."),P("Se formula con claridad: <i>Los celulares deberían usarse en el aula con fines educativos.</i>")]),
 S(1,"Tipos de argumentos",[T("Cómo se apoya una tesis",["Tipo","Ejemplo"],[["Ejemplo","En mi curso, usamos el celular para buscar datos"],["Dato","Según una encuesta, el 80 % usa el celular para estudiar"],["Autoridad","Una docente de Ciencias lo recomienda"],["Causa y efecto","Si lo usamos bien, aprendemos más"]])]),
 S(2,"Conectores",[T("Para argumentar",["Función","Conectores"],[["Introducir un argumento","en primer lugar, además"],["Dar un ejemplo","por ejemplo"],["Explicar una causa","porque, ya que"],["Concluir","por lo tanto, en conclusión"]])]),
 S(2,"Un párrafo",[P("Un buen párrafo: <b>tesis + argumento + ejemplo + cierre</b>. <i>Creo que el recreo debería durar más. Porque descansar mejora la atención; por ejemplo, después del recreo participamos más. Por eso conviene extenderlo.</i>")])],
 {"titulo":"argumentar","planteo":"Tesis: «Debería haber más espacios verdes en la escuela».","pasos":["Argumento: los espacios verdes mejoran el ánimo.","Ejemplo: en el patio con árboles, los chicos juegan más tranquilos.","Cierre: por lo tanto, conviene plantar más árboles."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La idea que se defiende es la ___ .","Las razones que la apoyan son los ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una tesis y dos argumentos de tipos distintos."},
 {"titulo":"Una razón por vez","texto":"Cada argumento tiene que apoyar la tesis, no repetirla."},
 ["Repetir la tesis como argumento.","Argumentar con insultos."],
 RS(("Tesis","Lo que defiendo."),("Argumentos","Razones."),("Tipos","Ejemplo, dato, autoridad, causa."),("Cierre","Vuelve a la tesis.")),
 G(("Tesis","Idea que se defiende."),("Argumento","Razón que apoya una tesis."),("Autoridad","Persona experta en un tema.")),
 ["¿Cómo se llama la idea principal que defendés?","¿Cómo se llaman las razones que la apoyan?","¿Qué tipo de argumento usa números de una encuesta?","¿Qué conector uso para dar un ejemplo?"],
 [["tesis","la tesis"],["argumentos","los argumentos"],["dato","de dato","un dato","argumento de dato"],["por ejemplo"]],
 {"incompleto":"Tesis. Argumentos.","solo":"Tesis: más recreo. Argumento: descansar mejora la atención. Ejemplo: después del recreo participamos más.","carpeta":["La tesis.","Los argumentos.","De dato.","Por ejemplo."]})
B3=NV("Vas a escribir una carta de lectores con tesis, argumentos, cierre y datos del remitente.",["Qué es una carta de lectores","Partes","Tono y registro","Antes de enviarla"],[
 S(1,"Qué es",[D("Carta de lectores","Texto breve que un lector envía a un diario o revista para opinar sobre un tema o responder a una nota."),P("Se publica con el nombre de quien la escribe y busca convencer a otros lectores.")]),
 S(1,"Partes",[T("Estructura",["Parte","Qué lleva"],[["Título","Resume el tema"],["Saludo","Señor director:"],["Tesis","Lo que opino"],["Argumentos","Razones con ejemplos"],["Cierre","Conclusión"],["Firma y datos","Nombre y localidad"]])]),
 S(2,"Tono y registro",[P("El tono es <b>respetuoso y formal</b>: sin insultos ni abreviaturas de chat. Se puede opinar con fuerza, pero siempre con respeto y razones.")]),
 S(2,"Antes de enviarla",[P("Verificá que: la tesis se entienda en la primera frase, haya al menos dos argumentos, no pase de unas 150 palabras y esté firmada.")])],
 {"titulo":"armar","planteo":"Tema: más ciclovías en la ciudad.","pasos":["Título: Más ciclovías, menos tránsito.","Saludo: Señor director:","Tesis: Creo que hacen falta más ciclovías.","Argumentos: reducen el tránsito y mejoran la salud.","Cierre y firma: Por eso pido al municipio ampliarlas. Lucía Gómez, Rosario."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La carta de lectores se envía a un diario o ___ .","El tono de la carta es respetuoso y ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una carta de lectores sobre un tema que te importe."},
 {"titulo":"Primero la tesis","texto":"Que el lector sepa qué pensás ya desde la primera frase."},
 ["Insultar a quien piensa distinto.","Olvidar la firma."],
 RS(("Carta de lectores","Opinión pública."),("Partes","Título, tesis, argumentos, cierre."),("Tono","Respetuoso."),("Firma","Nombre y localidad.")),
 G(("Remitente","Quien envía la carta."),("Tono","Actitud con la que se escribe."),("Localidad","Lugar donde vive el remitente.")),
 ["¿A dónde se envía una carta de lectores: a un diario o a una tienda?","¿Qué tono se usa: respetuoso o agresivo?","¿Lleva firma? Respondé sí o no.","¿Qué parte dice lo que opina quien escribe?"],
 [["diario","a un diario","revista","a una revista"],["respetuoso","respetuoso y formal"],["si","sí"],["tesis","la tesis"]],
 {"incompleto":"Revista. Formal.","solo":"Carta con título, saludo, tesis, dos argumentos, cierre y firma.","carpeta":["A un diario.","Respetuoso.","Sí.","La tesis."]})
B4=NV("Vas a responder a otra opinión reconociendo lo valioso, discrepando con razones y proponiendo una alternativa.",["Responder con respeto","Pasos de una respuesta","Contraargumentar","Conectores"],[
 S(1,"Responder con respeto",[P("Responder no es atacar: es <b>discrepar con razones</b>. Se critica la idea, no a la persona.")]),
 S(1,"Pasos",[T("Estructura de la respuesta",["Paso","Ejemplo"],[["Reconozco","Es cierto que el celular distrae"],["Discrepo","Sin embargo, no creo que haya que prohibirlo"],["Argumento","Porque puede usarse para buscar información"],["Propongo","Se podría usar solo con permiso del docente"]])]),
 S(2,"Contraargumentar",[D("Contraargumento","Razón que se opone al argumento de otro."),P("Para contraargumentar, mostrá una <b>falla</b> en la razón del otro: un dato que no es cierto, un caso que no se cumple o una consecuencia que no se tuvo en cuenta.")]),
 S(2,"Conectores",[T("Para discrepar",["Función","Conectores"],[["Reconocer","es cierto que, tienes razón en que"],["Oponer","sin embargo, en cambio, pero"],["Concesión","aunque, si bien"],["Proponer","por eso, una alternativa es"]])])],
 {"titulo":"responder","planteo":"Opinión ajena: «Hay que prohibir los celulares en la escuela».","pasos":["Reconozco: es cierto que a veces distraen.","Discrepo: sin embargo, no hace falta prohibirlos.","Argumento: sirven para buscar información y organizarse.","Propongo: usarlos con reglas claras."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La razón que se opone al argumento de otro es un ___ .","Se critica la idea y no a la ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una respuesta a una opinión con la que no estás de acuerdo."},
 {"titulo":"Idea, no persona","texto":"Cuando discrepás, discutí lo que dijo, no cómo es quien lo dijo."},
 ["Atacar a la persona en lugar de la idea.","Discrepar sin dar razones."],
 RS(("Respeto","Se critica la idea."),("Pasos","Reconozco, discrepo, argumento, propongo."),("Contraargumento","Razón en contra."),("Conectores","Sin embargo, aunque.")),
 G(("Contraargumento","Razón que se opone a otra."),("Discrepar","No estar de acuerdo."),("Concesión","Reconocer algo del otro.")),
 ["¿Cómo se llama la razón que se opone al argumento de otro?","¿Se critica la idea o a la persona?","¿Qué conector introduce una oposición: sin embargo o por ejemplo?","¿Conviene reconocer algo valioso del otro? Respondé sí o no."],
 [["contraargumento","un contraargumento","el contraargumento"],["la idea","idea"],["sin embargo"],["si","sí"]],
 {"incompleto":"Contraargumento. Persona.","solo":"Es cierto que distraen; sin embargo, sirven para buscar información; propongo usarlos con reglas.","carpeta":["Contraargumento.","La idea.","Sin embargo.","Sí."]})
ACT13={"1":[{"t":"classify","p":"¿Hecho u opinión?","o":{"elementos":["El colegio abre a las 8","El colegio es aburrido","Hay 40 alumnos","La clase es genial"],"categorias":["Hecho","Opinión"]},"r":{"categorias":{"El colegio abre a las 8":"Hecho","El colegio es aburrido":"Opinión","Hay 40 alumnos":"Hecho","La clase es genial":"Opinión"}},"e":"Los hechos se comprueban."},MS("¿Qué marcas delatan una opinión?",["creo que","injusto","hay 40 alumnos","siempre"],["creo que","injusto","siempre"],"Hay 40 alumnos es un dato.")],
 "2":[{"t":"matching","p":"Uní cada tipo de argumento con su ejemplo.","o":{"izquierda":["Ejemplo","Dato","Autoridad","Causa y efecto"],"derecha":["En mi curso","El 80 % lo usa","Una docente lo recomienda","Si lo usamos bien, aprendemos más"]},"r":{"pares":{"Ejemplo":"En mi curso","Dato":"El 80 % lo usa","Autoridad":"Una docente lo recomienda","Causa y efecto":"Si lo usamos bien, aprendemos más"}},"e":"Cada tipo apoya la tesis de otra forma."},FB("La idea principal que se defiende es la ___ .",[["tesis"]],"La tesis.")],
 "3":[KW("Escribí una carta de lectores de unas 100 palabras sobre un tema que te importe, con título, saludo, tesis, dos argumentos, cierre y firma.","Tono respetuoso, tesis clara en la primera frase y dos argumentos distintos.","Carta de lectores con título, saludo formal (Señor director:), tesis clara, dos argumentos de tipos distintos con un ejemplo, cierre y firma con nombre y localidad; tono respetuoso.","Se evalúa estructura, argumentos y tono."),{"t":"ordering","p":"Ordená las partes de la carta.","o":["Argumentos","Título","Firma","Tesis","Saludo","Cierre"],"r":{"orden":["Título","Saludo","Tesis","Argumentos","Cierre","Firma"]},"e":"De arriba hacia abajo."}],
 "4":[TT("Tocá el conector que introduce una oposición: «Es cierto que distraen; sin embargo, pueden ayudar».",["Es","cierto","que","distraen;","sin","embargo,","pueden","ayudar"],[4,5],"Sin embargo opone ideas."),KW("Respondé a esta opinión: «Hay que prohibir los celulares en la escuela». Reconocé algo, discrepá con una razón y proponé una alternativa.","Usá sin embargo, porque y una propuesta.","Respuesta que reconoce algo valioso, discrepa con una razón (contraargumento) y propone una alternativa, en tono respetuoso y con conectores.","Se evalúa respeto, razones y propuesta.")],
 "5":[MC("Relámpago. Lo que se puede comprobar es un…",["Hecho","Deseo","Título"],"Hecho","Se verifica.",tiempo=20),VF("Relámpago. La tesis es la idea que se defiende.","Verdadero","Principal.",tiempo=20),MC("Relámpago. «Sin embargo» introduce…",["Una oposición","Una suma","Un saludo"],"Una oposición","Contrasta ideas.",tiempo=20),VF("Relámpago. Al discrepar se ataca a la persona.","Falso","Se critica la idea.",tiempo=20)]}
EX13=[[1,MC("«El colegio abre a las 8» es…",["Un hecho","Una opinión","Una tesis","Un deseo"],"Un hecho","Se puede comprobar.")],
 [1,MS("Marcas de opinión:",["Creo que","Adjetivos valorativos","Fechas exactas","Siempre y nunca"],["Creo que","Adjetivos valorativos","Siempre y nunca"],"Las fechas exactas son datos.")],
 [1,VF("Una opinión se prueba con una medición.","Falso","Se argumenta.")],
 [2,MC("La idea principal que se defiende es…",["La tesis","El saludo","La firma","El título"],"La tesis","Se apoya con argumentos.")],
 [2,MC("Un argumento que usa un número de una encuesta es de…",["Dato","Ejemplo","Autoridad","Causa"],"Dato","Cifras.")],
 [2,FB("Para dar un ejemplo uso el conector «por ___ ».",[["ejemplo"]],"Por ejemplo.")],
 [3,MC("Una carta de lectores se envía a…",["Un diario o revista","Un amigo","Un banco","Un médico"],"Un diario o revista","Para opinar públicamente.")],
 [3,MS("Partes de una carta de lectores:",["Título","Tesis","Argumentos","Receta"],["Título","Tesis","Argumentos"],"La receta no es parte.")],
 [3,VF("Una carta de lectores usa un tono respetuoso.","Verdadero","Sin insultos.")],
 [4,MC("Un contraargumento es…",["Una razón que se opone a otra","Un saludo","Una firma","Un hecho"],"Una razón que se opone a otra","Muestra una falla.")],
 [4,MC("Al discrepar se critica…",["La idea","A la persona","Su ropa","Nada"],"La idea","Con respeto.")],
 [4,FB("«Sin embargo» es un conector de ___ .",[["oposicion","oposición"]],"Contrasta.")],
 [4,VF("Conviene reconocer algo valioso de la otra opinión.","Verdadero","Da respeto y fuerza.")]]
M13={"subject_id":SID,"tema":13,"practica":"Práctica general: argumentar una opinión","examen_titulo":"Nivel jefe: argumentar una opinión","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT13,"examen":EX13}
for n,m in ((12,M12),(13,M13)):
    os.makedirs(os.path.join(AQUI,f"mision-{n}"),exist_ok=True); json.dump(m,open(os.path.join(AQUI,f"mision-{n}",f"mision-{n}.json"),"w"),ensure_ascii=False)

# ================= CLASES ANIMADAS =================
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={(5,1):"3029e488-5ba8-4032-b5fd-dd5a3a00cfa3",(5,2):"e6acbef3-5c27-474d-bb7c-54247c97bec1",(5,3):"dd05e528-5f20-4e8f-9a40-107f5b9ebd8a",(5,4):"06577aa6-32ec-469f-b28d-f43f2316036a",(6,1):"5e1454b9-74fb-43f0-9f22-19c1bf1a9c6f",(6,2):"0ef71248-d8a1-4e6a-9c78-7f8eacf2bcde",(6,3):"2a1555cb-959d-402a-aa6c-e7e544072c25",(6,4):"fed71c24-110e-4701-9ac7-ce1834d85f60"}
TIT={(5,1):"Recursos que se renuevan y recursos que se agotan",(5,2):"Petróleo, gas y carbón: recursos estratégicos",(5,3):"El agua: un recurso que no se reparte parejo",(5,4):"Minerales y cultivos que mueven la economía mundial",(6,1):"Suelos que se degradan: erosión y expansión agrícola",(6,2):"Contaminación del aire, el agua y la tierra",(6,3):"Cambio climático y fenómenos extremos",(6,4):"Políticas ambientales: de las cumbres a la comunidad"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
def NEU(e,**k): e=dict(e); e["neutro"]=k; return e
STEPS={(12,1):"5b873e4d-3ac2-4900-a5d4-dcb3564d430e",(12,2):"bd232aa5-3e5a-415b-a1dd-e2a146736cab",(12,3):"ccce7fff-1b21-4add-971f-683902c6906b",(12,4):"9b6ebe52-340e-4dd4-8b15-57295f27e190",(13,1):"9e6fbdf0-9fa1-4a4d-89a1-b42d973d2964",(13,2):"a5cfd8a1-47eb-43d8-a731-35f01eb078ce",(13,3):"a1960988-06bc-432b-b2c4-f62e6822ae5b",(13,4):"8ce6d0f4-0b6e-4f36-8f49-d67bce61e893"}
TIT={(12,1):"Sustantivos y adjetivos",(12,2):"El verbo y sus modos",(12,3):"Adverbios y preposiciones",(12,4):"Pronombres y conjunciones",(13,1):"Hecho y opinión",(13,2):"Opinión, tesis y argumentos",(13,3):"Escribo una carta de lectores",(13,4):"Respondo a otra opinión"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
TU=lambda t,v:{"t":"consejo","titulo":"TU TURNO","texto":t,"emoji":"✍️","voz":v}
CLS={(12,1):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Alegría es un sustantivo 😄"},{"yo":True,"txt":"¿Y no se puede tocar?"},{"yo":False,"txt":"Justo: es abstracto"}],"titulo":"SUSTANTIVOS Y ADJETIVOS","sub":"clases y concordancia","voz":["Lu dice que alegría es un sustantivo.","Juan: ¿y no se puede tocar?","Lu: justo, es abstracto.","Hoy: *sustantivos y adjetivos*."]},
 DEF("Sustantivo","Nombra personas, cosas, lugares e ideas","🏷️",["El *sustantivo* nombra personas, animales, cosas, lugares e ideas.","Tiene *género* y *número*."]),
 CL([("CONCRETO","🪑"),("ABSTRACTO","💭")],[("mesa",0),("alegría",1),("río",0),("libertad",1)],["¿Concreto o abstracto?","*Mesa* y *río*: concretos.","*Alegría* y *libertad*: abstractos."]),
 DEF("Adjetivo","Dice cómo es el sustantivo","🎨",["El *adjetivo* acompaña al sustantivo y dice cómo es.","Concuerda en *género* y *número*."]),
 ER([("Los niños cansada","Los niños cansados"),("Una casa grandes","Una casa grande")],["Errores de concordancia.","*Los niños cansada* debe ser *cansados*.","*Una casa grandes* debe ser *grande*."]),
 Q("«Córdoba» es un sustantivo…",["Propio","Común","Abstracto"],0,["Te toca: «Córdoba» es un sustantivo…","¿Propio, común o abstracto?","*Propio*."]),
 RES(["Repasemos.","El *sustantivo* nombra.","Puede ser *común* o *propio*, *concreto* o *abstracto*.","El *adjetivo* dice cómo es.","Y *concuerda* en género y número.","¡Clase terminada! Ahora, *a practicar*."],[["SUSTANTIVO","nombra"],["CLASES","común, propio"],["ADJETIVO","cómo es"],["CONCORDANCIA","género y número"]])],
(12,2):[
 {"t":"reto","texto":"¿En qué modo está «Cerrá la puerta»?","segundos":6,"respuesta":"Imperativo","emoji":"🚪","titulo":"EL VERBO Y SUS MODOS","sub":"hecho, deseo u orden","voz":["Desafío: ¿en qué modo está cerrá la puerta? Seis segundos.","Imperativo.","Hoy: *el verbo y sus modos*."]},
 DEF("Verbo","Persona, número, tiempo y modo","🏃",["El *verbo* expresa acciones, estados o procesos.","Varía en *persona*, *número*, *tiempo* y *modo*."]),
 TB("TRES MODOS",["Modo","Expresa"],[["Indicativo","Hechos reales"],["Subjuntivo","Deseos y dudas"],["Imperativo","Órdenes"]],["Los tres modos.","*Indicativo*: hechos reales.","*Subjuntivo*: deseos y dudas.","*Imperativo*: órdenes."]),
 CL([("INDICATIVO","✅"),("SUBJUNTIVO","🌠"),("IMPERATIVO","📢")],[("Estudio",0),("Ojalá estudie",1),("Estudiá",2)],["¿Qué modo?","*Estudio*: indicativo.","*Ojalá estudie*: subjuntivo.","*Estudiá*: imperativo."]),
 TB("FORMAS NO PERSONALES",["Forma","Terminación"],[["Infinitivo","-ar, -er, -ir"],["Gerundio","-ando, -iendo"],["Participio","-ado, -ido"]],["Tres formas no personales.","*Infinitivo*: cantar.","*Gerundio*: cantando.","*Participio*: cantado."]),
 Q("«Ojalá llueva» está en modo…",["Subjuntivo","Indicativo","Imperativo"],0,["Te toca: «ojalá llueva».","¿Subjuntivo, indicativo o imperativo?","*Subjuntivo*: expresa un deseo."]),
 ER([("Confundir tiempo y modo","El modo depende de lo que digo"),("El gerundio es una persona","Es una forma no personal")],["Errores típicos.","*Confundir* tiempo con modo.","Y creer que el gerundio es una *persona*."]),
 RES(["Repasemos.","El verbo varía en *persona*, *número*, *tiempo* y *modo*.","*Indicativo*, hechos.","*Subjuntivo*, deseos.","*Imperativo*, órdenes.","¡Clase terminada! Ahora, *a practicar*."],[["VERBO","cuatro variaciones"],["INDICATIVO","hechos"],["SUBJUNTIVO","deseos"],["IMPERATIVO","órdenes"]])],
(12,3):[
 {"t":"gancho","grande":"Invariables","emoji":"🔒","final":"no cambian de género ni de número","titulo":"ADVERBIOS Y PREPOSICIONES","sub":"palabras que no cambian","voz":["Hay palabras que nunca cambian.","No tienen género ni número.","Hoy: *adverbios* y *preposiciones*."]},
 DEF("Adverbio","Modifica a un verbo, un adjetivo u otro adverbio","🧭",["El *adverbio* modifica al verbo, a un adjetivo o a otro adverbio.","Es *invariable*."]),
 TB("CLASES DE ADVERBIOS",["Clase","Ejemplo"],[["Lugar","aquí, cerca"],["Tiempo","hoy, nunca"],["Modo","bien, rápido"],["Cantidad","muy, poco"]],["Cuatro clases.","*Lugar*: aquí, cerca.","*Tiempo*: hoy, nunca.","*Modo*: bien, rápido.","*Cantidad*: muy, poco."]),
 CL([("LUGAR","📍"),("TIEMPO","⏰"),("CANTIDAD","📊")],[("allá",0),("ayer",1),("mucho",2)],["¿Qué clase?","*Allá*: lugar.","*Ayer*: tiempo.","*Mucho*: cantidad."]),
 DEF("Preposición","Une una palabra con su complemento","🔗",["La *preposición* une una palabra con su complemento.","Como *a*, *con*, *de*, *en*, *para*, *por*, *sin* y *sobre*."]),
 Q("«Sin» es…",["Una preposición","Un adverbio","Un verbo"],0,["Te toca: «sin» es…","¿Una preposición, un adverbio o un verbo?","*Una preposición*."]),
 ER([("Poner plural a un adverbio","Son invariables"),("Confundir adverbio con adjetivo","El adverbio no concuerda")],["Errores típicos.","Poner *plural* a un adverbio.","Y confundirlo con un *adjetivo*."]),
 RES(["Repasemos.","El *adverbio* modifica al verbo.","Hay de *lugar*, *tiempo*, *modo* y *cantidad*.","La *preposición* une.","Ambos son *invariables*.","¡Clase terminada! Ahora, *a practicar*."],[["ADVERBIO","modifica"],["CLASES","lugar, tiempo, modo"],["PREPOSICIÓN","une"],["INVARIABLES","no cambian"]])],
(12,4):[
 {"t":"antesdespues","antes":{"cab":"REPETIDO","emoji":"🔁","texto":"Lucas compró un libro. Lucas leyó el libro."},"despues":{"cab":"MEJORADO","emoji":"✨","texto":"Lucas compró un libro y lo leyó."},"titulo":"PRONOMBRES Y CONJUNCIONES","sub":"evitar repeticiones y unir ideas","voz":["Repetido: Lucas compró un libro. Lucas leyó el libro.","Mejorado: Lucas compró un libro y lo leyó.","Hoy: *pronombres* y *conjunciones*."]},
 DEF("Pronombre","Reemplaza a un sustantivo","👤",["El *pronombre* reemplaza a un sustantivo para no repetirlo.","Como *ella* por *Sofía*."]),
 TB("CLASES DE PRONOMBRES",["Clase","Ejemplo"],[["Personales","yo, ella"],["Posesivos","mío, suyo"],["Demostrativos","este, ese"]],["Tres clases.","*Personales*: yo, ella.","*Posesivos*: mío, suyo.","*Demostrativos*: este, ese."]),
 DEF("Conjunción","Une palabras u oraciones","🔗",["La *conjunción* une palabras u oraciones.","Es *invariable*."]),
 CL([("SUMA","➕"),("OPOSICIÓN","↔️"),("CAUSA","❓")],[("y",0),("pero",1),("porque",2)],["¿Qué idea une?","*Y*: suma.","*Pero*: oposición.","*Porque*: causa."]),
 Q("¿Qué palabra reemplaza a un sustantivo?",["Pronombre","Conjunción","Adverbio"],0,["Te toca: ¿qué palabra reemplaza a un sustantivo?","¿Pronombre, conjunción o adverbio?","El *pronombre*."]),
 ER([("Repetir el sustantivo siempre","Usar pronombres"),("Confundir pero con porque","Oposición y causa")],["Errores típicos.","*Repetir* el sustantivo.","Y confundir *pero* con *porque*."]),
 RES(["Repasemos.","El *pronombre* reemplaza.","Hay *personales*, *posesivos* y *demostrativos*.","La *conjunción* une.","Evitá *repeticiones*.","¡Clase terminada! Ahora, *a practicar*."],[["PRONOMBRE","reemplaza"],["CLASES","personales, posesivos"],["CONJUNCIÓN","une"],["MEJORA","menos repetición"]])],
(13,1):[
 {"t":"reto","texto":"«El colegio es aburrido»: ¿hecho u opinión?","segundos":6,"respuesta":"Opinión","emoji":"🏫","titulo":"HECHO Y OPINIÓN","sub":"qué se comprueba","voz":["Desafío: el colegio es aburrido, ¿hecho u opinión? Seis segundos.","Opinión.","Hoy: *hecho y opinión*."]},
 CMP(("HECHO","Se puede comprobar","📊"),("OPINIÓN","Lo que alguien piensa","💭"),"vs",["No son lo mismo.","El *hecho* se puede comprobar.","La *opinión* es lo que alguien piensa."]),
 CL([("HECHO","📊"),("OPINIÓN","💭")],[("Abre a las ocho",0),("Es aburrido",1),("Hay 40 alumnos",0),("Es genial",1)],["¿Hecho u opinión?","*Abre a las ocho* y *hay 40 alumnos*: hechos.","*Es aburrido* y *es genial*: opiniones."]),
 TB("MARCAS DE OPINIÓN",["Marca","Ejemplo"],[["Verbos de pensamiento","creo, me parece"],["Adjetivos valorativos","injusto, genial"],["Exageraciones","siempre, nunca"]],["Cómo reconocer una opinión.","Verbos de pensamiento: *creo*, *me parece*.","Adjetivos valorativos: *injusto*, *genial*.","Exageraciones: *siempre*, *nunca*."]),
 Q("Para saber si es un hecho, ¿qué te preguntás?",["¿Puedo verificarlo?","¿Me gusta?","¿Es largo?"],0,["Te toca: ¿qué te preguntás para saber si es un hecho?","¿Puedo verificarlo, me gusta o es largo?","*¿Puedo verificarlo?*"]),
 ER([("Una opinión es siempre falsa","Se argumenta"),("Tomar un dato dudoso como hecho","Verificarlo")],["Errores típicos.","Creer que una opinión es *siempre falsa*.","Y tomar un dato *dudoso* como hecho."]),
 RES(["Repasemos.","El *hecho* se comprueba.","La *opinión* se argumenta.","Hay *marcas* de opinión.","Y se pueden *mezclar*.","¡Clase terminada! Ahora, *a practicar*."],[["HECHO","se comprueba"],["OPINIÓN","se argumenta"],["MARCAS","creo, adjetivos"],["MEZCLA","pueden ir juntos"]])],
(13,2):[
 {"t":"noticia","cinta":"DEBATE","titular":"¿Más tiempo de recreo? Opinan los alumnos","bajada":"Cada uno defiende su idea","emoji":"🗣️","titulo":"TESIS Y ARGUMENTOS","sub":"armar una opinión","voz":["Debate: ¿más tiempo de recreo? Opinan los alumnos.","Cada uno defiende su idea.","Hoy: *opinión, tesis y argumentos*."]},
 DEF("Tesis","La idea principal que se defiende","🎯",["La *tesis* es la idea principal que se defiende.","Se dice con claridad."]),
 TB("TIPOS DE ARGUMENTOS",["Tipo","Ejemplo"],[["Ejemplo","En mi curso..."],["Dato","El 80 %..."],["Autoridad","Una docente dice..."],["Causa y efecto","Si..., entonces..."]],["Cuatro tipos.","De *ejemplo*.","De *dato*.","De *autoridad*.","Y de *causa y efecto*."]),
 CL([("EJEMPLO","📝"),("DATO","📊"),("AUTORIDAD","🎓")],[("En mi curso",0),("El 80 % lo usa",1),("Lo dice una docente",2)],["¿Qué tipo?","*En mi curso*: ejemplo.","*El 80 % lo usa*: dato.","*Lo dice una docente*: autoridad."]),
 PA("UN PÁRRAFO",[("Tesis","🎯"),("Argumento","💡"),("Ejemplo","📝"),("Cierre","🔚")],["Un buen párrafo tiene cuatro partes.","*Tesis*.","*Argumento*.","*Ejemplo*.","Y *cierre*."]),
 Q("¿Qué conector uso para dar un ejemplo?",["Por ejemplo","En conclusión","Pero"],0,["Te toca: ¿qué conector doy para un ejemplo?","¿Por ejemplo, en conclusión o pero?","*Por ejemplo*."]),
 ER([("Repetir la tesis como argumento","Dar una razón nueva"),("Argumentar con insultos","Dar razones")],["Errores típicos.","*Repetir* la tesis.","Y argumentar con *insultos*."]),
 RES(["Repasemos.","La *tesis* es lo que defiendo.","Los *argumentos* la apoyan.","Hay de *ejemplo*, *dato*, *autoridad* y *causa*.","Y se *cierra* volviendo a la tesis.","¡Clase terminada! Ahora, *a practicar*."],[["TESIS","lo que defiendo"],["ARGUMENTOS","razones"],["TIPOS","cuatro"],["CIERRE","vuelve a la tesis"]])],
(13,3):[
 {"t":"noticia","cinta":"CARTAS","titular":"Una lectora pide más ciclovías","bajada":"Su carta se publicó hoy","emoji":"📰","titulo":"CARTA DE LECTORES","sub":"opinar en un diario","voz":["Cartas: una lectora pide más ciclovías.","Su carta se publicó hoy.","Hoy: *escribo una carta de lectores*."]},
 DEF("Carta de lectores","Texto que se envía a un diario para opinar","📰",["La *carta de lectores* se envía a un diario o revista para opinar.","Se publica con el nombre de quien la escribe."]),
 PA("PARTES",[("Título","🏷️"),("Saludo","👋"),("Tesis","🎯"),("Argumentos","💡"),("Cierre y firma","✍️")],["Las partes.","*Título*.","*Saludo*.","*Tesis*.","*Argumentos*.","Y *cierre y firma*."]),
 CL([("SÍ","✅"),("NO","🚫")],[("Tono respetuoso",0),("Insultos",1),("Dos argumentos",0),("Chat abreviado",1)],["¿Va en una carta de lectores?","*Tono respetuoso* y *dos argumentos*: sí.","*Insultos* y *chat abreviado*: no."]),
 Q("¿Qué parte dice lo que opina quien escribe?",["La tesis","La firma","El saludo"],0,["Te toca: ¿qué parte dice lo que opina quien escribe?","¿La tesis, la firma o el saludo?","*La tesis*."]),
 TU("Escribí una carta de lectores sobre un tema que te importe",["Ahora te toca: escribí una carta de lectores.","Con *título*, *tesis*, *dos argumentos*, *cierre* y *firma*."]),
 ER([("Insultar a quien piensa distinto","Tono respetuoso"),("Olvidar la firma","Firmar con nombre y localidad")],["Errores típicos.","*Insultar* a quien piensa distinto.","Y *olvidar la firma*."]),
 RES(["Repasemos.","La carta va a un *diario*.","Tiene *título*, *tesis*, *argumentos*, *cierre* y *firma*.","El tono es *respetuoso*.","Y la tesis va *primero*.","¡Clase terminada! Ahora, *a practicar*."],[["DESTINO","diario o revista"],["PARTES","cinco"],["TONO","respetuoso"],["TESIS","primero"]])],
(13,4):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Hay que prohibir los celulares 📵"},{"yo":True,"txt":"Es cierto que distraen, pero..."},{"yo":True,"txt":"podemos usarlos con reglas 🙂"}],"titulo":"RESPONDO A OTRA OPINIÓN","sub":"discrepar con razones","voz":["Lu dice que hay que prohibir los celulares.","Juan responde: es cierto que distraen, pero podemos usarlos con reglas.","Reconoce, discrepa y propone.","Hoy: *respondo a otra opinión*."]},
 PA("PASOS",[("Reconozco","🤝"),("Discrepo","↔️"),("Argumento","💡"),("Propongo","🛠️")],["Una respuesta tiene cuatro pasos.","*Reconozco* algo valioso.","*Discrepo* con respeto.","*Argumento*.","Y *propongo* una alternativa."]),
 DEF("Contraargumento","Razón que se opone al argumento de otro","⚖️",["El *contraargumento* es una razón que se opone al argumento de otro.","Muestra una falla en lo que dijo."]),
 TB("CONECTORES PARA DISCREPAR",["Función","Conectores"],[["Reconocer","es cierto que"],["Oponer","sin embargo"],["Conceder","aunque"],["Proponer","por eso"]],["Conectores útiles.","*Es cierto que*, para reconocer.","*Sin embargo*, para oponer.","*Aunque*, para conceder.","*Por eso*, para proponer."]),
 CMP(("IDEA","Se critica lo que dijo","💡"),("PERSONA","No se ataca a nadie","🚫"),"≠",["Cuando discrepás, cuidá esto.","Se critica la *idea*.","No se ataca a la *persona*."]),
 Q("¿Qué conector introduce una oposición?",["Sin embargo","Por ejemplo","En primer lugar"],0,["Te toca: ¿qué conector introduce una oposición?","¿Sin embargo, por ejemplo o en primer lugar?","*Sin embargo*."]),
 ER([("Atacar a la persona","Criticar la idea"),("Discrepar sin razones","Dar un contraargumento")],["Errores típicos.","*Atacar a la persona*.","Y discrepar *sin razones*."]),
 RES(["Repasemos.","Respondé con *respeto*.","*Reconocé*, *discrepá*, *argumentá* y *proponé*.","Usá *contraargumentos*.","Y *conectores* de oposición.","¡Clase terminada! Ahora, *a practicar*."],[["RESPETO","la idea"],["PASOS","cuatro"],["CONTRAARGUMENTO","razón en contra"],["CONECTORES","sin embargo"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"leng1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Lengua y Literatura I","titulo":TIT[(m,n)],"sub":f"Lengua y Literatura I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"leng1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
