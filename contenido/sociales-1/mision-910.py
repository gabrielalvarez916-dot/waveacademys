# -*- coding: utf-8 -*-
"""Ciencias Sociales Integradas I · Misión 9 (Los primeros humanos y la vida paleolítica) y Misión 10 (La Revolución Neolítica). Ambas COMUN."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}
SID = "a5f9b6fc-7f3b-4743-977d-da7f4f3a37bb"

# ================= MISIÓN 9 =================
A1=NV("Vas a explicar cómo cambiaron los homínidos hasta llegar al Homo sapiens y qué los hizo humanos.",["Qué es la hominización","Las especies principales","Los grandes cambios","Cómo lo sabemos"],[
 S(1,"Hominización",[D("Hominización","Proceso de millones de años por el cual aparecieron los humanos actuales a partir de antepasados que caminaban erguidos."),P("Nació en África. No fue una línea recta: convivieron varias especies al mismo tiempo.")]),
 S(1,"Especies principales",[T("De las más antiguas a la actual",["Especie","Cuándo","Rasgo clave"],[["Australopithecus","Hace unos 4 a 2 millones de años","Caminaba erguido"],["Homo habilis","Hace unos 2,4 millones de años","Fabricaba herramientas de piedra"],["Homo erectus","Desde hace unos 1,9 millones de años","Usó el fuego y salió de África"],["Homo sapiens","Hace unos 300.000 años","Cerebro grande, lenguaje y arte"]])]),
 S(2,"Los grandes cambios",[T("Qué cambió",["Cambio","Consecuencia"],[["Bipedismo","Las manos quedan libres para usar herramientas"],["Cerebro más grande","Más capacidad de aprender y planificar"],["Fuego","Cocción, calor, defensa y vida en grupo"],["Lenguaje","Se transmite lo aprendido"]])]),
 S(2,"Cómo lo sabemos",[P("Los científicos estudian <b>fósiles</b> (huesos), herramientas de piedra y análisis de ADN. Cada hallazgo nuevo puede cambiar fechas y teorías: la ciencia revisa lo que sabe.")])],
 {"titulo":"explicar","planteo":"¿Por qué caminar erguidos fue un cambio tan importante?","pasos":["Las manos quedaron libres.","Con las manos libres se podían fabricar y usar herramientas.","Eso favoreció el desarrollo del cerebro."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El proceso por el que aparecieron los humanos actuales es la ___ .","La especie que usó el fuego y salió de África fue el Homo ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un cambio (bipedismo, cerebro, fuego o lenguaje) y explicá qué permitió hacer."},
 {"titulo":"No es una escalera","texto":"No pienses una fila de especies que se reemplazan: varias convivieron y se cruzaron."},
 ["Creer que descendemos de los monos actuales: compartimos antepasados.","Pensar que la evolución humana fue una línea recta."],
 RS(("Hominización","Proceso de cambio."),("Especies","Australopithecus a sapiens."),("Cambios","Bipedismo, cerebro, fuego."),("Fuentes","Fósiles y herramientas.")),
 G(("Homínido","Grupo de seres de los que desciende el ser humano."),("Bipedismo","Caminar sobre dos pies."),("Fósil","Resto de un ser vivo del pasado."),("Hominización","Proceso por el que aparecieron los humanos.")),
 ["¿En qué continente comenzó la hominización?","¿Qué especie fabricó las primeras herramientas de piedra: el Homo habilis o el Homo sapiens?","¿Cómo se llama caminar sobre dos pies?","¿Los humanos descienden de los monos actuales? Respondé sí o no."],
 [["africa","áfrica","en africa","en áfrica"],["homo habilis","habilis","el homo habilis"],["bipedismo","el bipedismo"],["no"]],
 {"incompleto":"Hominización. Erectus.","solo":"El lenguaje: permitió transmitir lo aprendido a las nuevas generaciones.","carpeta":["En África.","El Homo habilis.","Bipedismo.","No."]})
A2=NV("Vas a describir cómo vivían los cazadores y recolectores, cómo se repartían el trabajo y cómo se tomaban las decisiones.",["Nómadas","La división del trabajo","Autoridad y decisiones","Herramientas y refugio"],[
 S(1,"Nómadas",[D("Cazadores y recolectores","Grupos que obtenían su alimento cazando, pescando y recolectando frutos y raíces, sin cultivar ni criar animales."),P("Eran <b>nómadas</b>: se movían siguiendo a los animales y las estaciones. Vivían en bandas de unas 20 a 50 personas.")]),
 S(1,"División del trabajo",[P("Las tareas se repartían según la edad y las habilidades: algunas personas cazaban, otras recolectaban frutos, semillas y raíces, y otras cuidaban a los niños. Casi todo lo que se obtenía se <b>compartía</b>.")]),
 S(2,"Autoridad",[P("No había jefes permanentes ni grandes diferencias de riqueza. Tenían más influencia quienes mostraban experiencia, y las decisiones importantes se discutían entre todos, por ejemplo adónde mudarse.")]),
 S(2,"Herramientas y refugio",[T("Qué usaban",["Recurso","Para qué"],[["Piedra tallada","Cortar, raspar, cazar"],["Hueso y madera","Agujas, lanzas, arpones"],["Fuego","Calor, cocción, defensa"],["Cuevas y toldos de pieles","Refugio"]])])],
 {"titulo":"razonar","planteo":"¿Por qué los cazadores y recolectores no acumulaban cosas?","pasos":["Se movían todo el tiempo.","Cargar muchas cosas era un obstáculo.","Compartían lo que conseguían."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los grupos que se desplazan de un lugar a otro son ___ .","Las tareas se repartían según la edad y las ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí dos tareas de la vida paleolítica y quién podía hacerlas."},
 {"titulo":"Compartir para sobrevivir","texto":"En un grupo chico, ayudarse era la mejor forma de asegurar la comida de todos."},
 ["Creer que había reyes en el Paleolítico.","Pensar que vivían en el mismo lugar todo el año."],
 RS(("Nómadas","Se movían."),("Trabajo","Se repartía."),("Autoridad","Experiencia, sin jefes fijos."),("Herramientas","Piedra, hueso, fuego.")),
 G(("Nómada","Que se desplaza de un lugar a otro."),("Recolectar","Juntar frutos, semillas y raíces."),("Banda","Grupo chico de personas que viven juntas.")),
 ["¿Cómo se llaman los grupos que se desplazan de un lugar a otro?","¿Cuántas personas tenía aproximadamente una banda? Respondé \"entre 20 y 50\" o \"miles\".","Los cazadores y recolectores, ¿cultivaban la tierra? Respondé sí o no.","¿Qué hacían con lo que conseguían: lo compartían o lo acumulaban?"],
 [["nomades","nómades","los nomades","los nómades"],["entre 20 y 50","20 y 50","20 a 50"],["no"],["lo compartian","lo compartían","compartian","compartían","compartirlo","lo compartian"]],
 {"incompleto":"Nómadas. Habilidades.","solo":"Cazar: personas con fuerza y experiencia. Recolectar: personas de varias edades.","carpeta":["Nómadas.","Entre 20 y 50.","No.","Lo compartían."]})
A3=NV("Vas a explicar qué nos dicen el arte, los entierros y los rituales sobre las creencias de la prehistoria.",["Arte rupestre","Entierros y rituales","Creer sin escritura","Qué nos dicen"],[
 S(1,"Arte rupestre",[D("Arte rupestre","Pinturas y grabados en las paredes de cuevas y rocas."),P("Se pintaba con pigmentos naturales (ocre, carbón) mezclados con grasa o agua. Hay ejemplos famosos en Altamira (España), Lascaux (Francia) y la Cueva de las Manos (Santa Cruz, Argentina), con manos pintadas hace miles de años.")]),
 S(1,"Entierros y rituales",[P("Algunos grupos enterraban a sus muertos con ofrendas, como herramientas, adornos y flores. Eso muestra que pensaban que había algo después de la muerte o que los muertos merecían respeto.")]),
 S(2,"Creer sin escritura",[T("Posibles sentidos de las imágenes",["Hipótesis","Idea"],[["Magia de la caza","Pintar animales traería suerte para cazar"],["Ritual","Las cuevas serían lugares sagrados"],["Registro","Cuentan lo que vivía el grupo"]]),P("Nadie puede estar seguro: son <b>hipótesis</b>, porque no hay escritura que lo explique.")]),
 S(2,"Qué nos dicen",[P("El arte y los entierros muestran que ya había <b>pensamiento simbólico</b>: representar con imágenes lo que no se tiene delante. Es una característica propia del Homo sapiens.")])],
 {"titulo":"interpretar","planteo":"En una cueva hay manos pintadas y animales. ¿Qué podemos decir?","pasos":["Alguien dedicó tiempo y materiales a pintar: era importante.","Los animales eran su alimento y su vida.","No sabemos el sentido exacto: hay hipótesis."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las pinturas en paredes de cuevas son arte ___ .","Representar con imágenes lo que no se tiene delante es pensamiento ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una hipótesis sobre el sentido de las pinturas y explicá por qué te convence."},
 {"titulo":"Hipótesis, no certeza","texto":"Cuando no hay escritura, decí \"podría ser\" y no \"seguro fue\"."},
 ["Creer que sabemos con certeza el significado de las pinturas.","Pensar que no tenían ideas ni creencias."],
 RS(("Rupestre","En cuevas y rocas."),("Entierros","Ofrendas."),("Hipótesis","Posibles sentidos."),("Simbólico","Representar con imágenes.")),
 G(("Rupestre","De las rocas y cuevas."),("Pigmento","Sustancia que da color."),("Ofrenda","Objeto que se deja a un muerto o a una divinidad."),("Hipótesis","Explicación posible, no comprobada.")),
 ["¿Cómo se llama el arte pintado en las paredes de las cuevas?","¿En qué país está la Cueva de las Manos?","Las ofrendas en los entierros, ¿muestran que había creencias? Respondé sí o no.","El sentido de las pinturas, ¿se conoce con certeza o son hipótesis?"],
 [["arte rupestre","rupestre","el arte rupestre"],["argentina","en argentina"],["si","sí"],["hipotesis","hipótesis","son hipotesis","son hipótesis"]],
 {"incompleto":"Rupestre. Simbólico.","solo":"Hipótesis: era un ritual para tener suerte en la caza, porque pintaban muchos animales.","carpeta":["Arte rupestre.","En Argentina.","Sí.","Son hipótesis."]})
A4=NV("Vas a explicar cómo el Homo sapiens se extendió desde África hasta ocupar todos los continentes.",["Salida de África","Los caminos","Llegar a América","Por qué se movían"],[
 S(1,"Salida de África",[P("El Homo sapiens apareció en África hace unos 300.000 años y salió de allí en distintas oleadas, hace unos 70.000 años o más. Se extendió por Asia, Europa y Oceanía.")]),
 S(1,"Los caminos",[T("Algunas etapas",["Región","Cuándo (aprox.)"],[["Asia","Hace más de 60.000 años"],["Australia","Hace unos 50.000 años"],["Europa","Hace unos 45.000 años"],["América","Hace más de 15.000 años"]])]),
 S(2,"Llegar a América",[P("Durante las glaciaciones el nivel del mar bajó y apareció una franja de tierra entre Siberia y Alaska: <b>Beringia</b>. Por allí, o bordeando la costa en botes, llegaron los primeros pobladores. Después avanzaron hacia el sur hasta Tierra del Fuego.")]),
 S(2,"Por qué se movían",[T("Motivos",["Motivo","Ejemplo"],[["Seguir los animales","La caza se desplazaba"],["Cambios del clima","Los hielos avanzaban y retrocedían"],["Crecimiento del grupo","Había que buscar nuevos territorios"]])])],
 {"titulo":"ordenar","planteo":"Ordená: Australia, África, América.","pasos":["Primero África: el origen.","Después Australia, hace unos 50.000 años.","Por último América, hace más de 15.000 años."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La franja de tierra entre Siberia y Alaska se llama ___ .","El Homo sapiens apareció en el continente ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá con tus palabras por qué las glaciaciones facilitaron llegar a América."},
 {"titulo":"Fechas aproximadas","texto":"Las fechas son cálculos que pueden cambiar con nuevos descubrimientos: usá siempre \"hace unos\"."},
 ["Pensar que llegaron a América en barcos de metal o con mapas.","Creer que las fechas son exactas."],
 RS(("Origen","África."),("Oleadas","Hace unos 70.000 años."),("América","Por Beringia o la costa."),("Motivos","Animales, clima, grupo.")),
 G(("Glaciación","Período de mucho frío con grandes hielos."),("Beringia","Franja de tierra entre Siberia y Alaska."),("Poblamiento","Ocupación de un territorio por una población.")),
 ["¿En qué continente apareció el Homo sapiens?","¿Cómo se llama la franja de tierra que unió Siberia y Alaska?","¿Qué llegó antes: Australia o América?","Las fechas del poblamiento, ¿son exactas o aproximadas?"],
 [["africa","áfrica","en africa","en áfrica"],["beringia"],["australia"],["aproximadas","son aproximadas","aproximada"]],
 {"incompleto":"África. Beringia.","solo":"Con tanto hielo el mar bajó y apareció una franja de tierra para cruzar caminando.","carpeta":["África.","Beringia.","Australia.","Aproximadas."]})
ACT9={"1":[{"t":"ordering","p":"Ordená de la más antigua a la más reciente.","o":["Homo erectus","Australopithecus","Homo sapiens","Homo habilis"],"r":{"orden":["Australopithecus","Homo habilis","Homo erectus","Homo sapiens"]},"e":"De los más antiguos a nosotros."},MC("¿Qué permitió el bipedismo?",["Liberar las manos","Volar","Nadar mejor","Vivir bajo tierra"],"Liberar las manos","Para usar herramientas.")],
 "2":[{"t":"classify","p":"¿Cazadores-recolectores o primeros agricultores?","o":{"elementos":["Nómadas","Compartían lo conseguido","Sin jefes permanentes","Acumulaban cosechas"],"categorias":["Paleolítico","No era del Paleolítico"]},"r":{"categorias":{"Nómadas":"Paleolítico","Compartían lo conseguido":"Paleolítico","Sin jefes permanentes":"Paleolítico","Acumulaban cosechas":"No era del Paleolítico"}},"e":"Acumular cosechas es de la agricultura."},MC("El grupo típico del Paleolítico tenía…",["Entre 20 y 50 personas","Miles de personas","Una sola familia siempre","Cien mil personas"],"Entre 20 y 50 personas","Eran bandas chicas.")],
 "3":[{"t":"matching","p":"Uní cada término con su significado.","o":{"izquierda":["Arte rupestre","Ofrenda","Hipótesis","Pigmento"],"derecha":["Pintura en cuevas","Objeto dejado a un muerto","Explicación posible","Sustancia que da color"]},"r":{"pares":{"Arte rupestre":"Pintura en cuevas","Ofrenda":"Objeto dejado a un muerto","Hipótesis":"Explicación posible","Pigmento":"Sustancia que da color"}},"e":"Vocabulario clave."},MC("Las pinturas rupestres, ¿se pueden explicar con certeza?",["No: hay hipótesis","Sí: está escrito","Sí: lo dicen los fósiles","Nunca se pintó nada"],"No: hay hipótesis","No hay escritura.")],
 "4":[{"t":"ordering","p":"Ordená el poblamiento.","o":["América","África","Australia"],"r":{"orden":["África","Australia","América"]},"e":"Del origen al continente más tardío."},MC("¿Cómo pudieron cruzar hacia América los primeros pobladores?",["Por Beringia o bordeando la costa","En aviones","Por un túnel","En trenes"],"Por Beringia o bordeando la costa","El mar estaba más bajo.")],
 "5":[MC("Relámpago. La hominización comenzó en…",["África","Europa","Oceanía"],"África","Allí apareció el Homo sapiens.",tiempo=20),MC("Relámpago. Los cazadores y recolectores eran…",["Nómadas","Sedentarios","Reyes"],"Nómadas","Se movían.",tiempo=20),MC("Relámpago. El arte en las cuevas es arte…",["Rupestre","Moderno","Digital"],"Rupestre","En las rocas.",tiempo=20),MC("Relámpago. La franja Siberia–Alaska se llama…",["Beringia","Atlántida","Pangea"],"Beringia","Con el mar bajo.",tiempo=20)]}
EX9=[[1,MC("¿Qué fue la hominización?",["El proceso por el que aparecieron los humanos actuales","Un tipo de herramienta","Una pintura","Un lugar"],"El proceso por el que aparecieron los humanos actuales","Nació en África.")],
 [1,MC("¿Qué especie usó el fuego y salió de África?",["Homo erectus","Australopithecus","Homo sapiens moderno","Ninguna"],"Homo erectus","Hace casi dos millones de años.")],
 [1,VF("Los humanos descienden de los monos actuales.","Falso","Compartimos antepasados comunes.")],
 [2,MC("Los cazadores y recolectores eran…",["Nómadas","Sedentarios","Comerciantes","Soldados"],"Nómadas","Se movían siguiendo el alimento.")],
 [2,MC("¿Cómo se tomaban las decisiones en las bandas?",["Se discutían entre todos y pesaba la experiencia","Las decidía un rey","Las decidía un ejército","Por sorteo"],"Se discutían entre todos y pesaba la experiencia","No había jefes permanentes.")],
 [2,VF("Los cazadores y recolectores cultivaban la tierra.","Falso","Obtenían el alimento de la naturaleza.")],
 [3,MC("El arte rupestre es…",["Pintura o grabado en cuevas y rocas","Una escultura moderna","Un tipo de herramienta","Un idioma"],"Pintura o grabado en cuevas y rocas","Hay ejemplos en Altamira y en la Cueva de las Manos.")],
 [3,MC("Las ofrendas en los entierros indican…",["Creencias sobre la muerte","Que no había creencias","Que eran nómadas","Que cultivaban"],"Creencias sobre la muerte","Respeto o idea de otra vida.")],
 [3,VF("El sentido exacto de las pinturas se conoce con certeza.","Falso","Son hipótesis.")],
 [4,MC("¿Dónde apareció el Homo sapiens?",["África","América","Oceanía","Antártida"],"África","Hace unos 300.000 años.")],
 [4,MC("Beringia fue…",["Una franja de tierra entre Siberia y Alaska","Un río","Una montaña","Una isla del Caribe"],"Una franja de tierra entre Siberia y Alaska","Apareció cuando el mar bajó.")],
 [4,MC("¿Qué provocaron las glaciaciones?",["Que bajara el nivel del mar","Que subiera el mar","Que no hubiera hielo","Que no hubiera animales"],"Que bajara el nivel del mar","Eso dejó tierra a la vista.")],
 [4,VF("Las fechas del poblamiento son exactas.","Falso","Son aproximadas.")]]
M9={"subject_id":SID,"tema":9,"practica":"Práctica general: los primeros humanos","examen_titulo":"Nivel jefe: los primeros humanos","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT9,"examen":EX9}

# ================= MISIÓN 10 =================
B1=NV("Vas a explicar cómo se pasó de cazar y recolectar a sembrar y criar animales.",["Cómo empezó la agricultura","Domesticar plantas y animales","Del nomadismo al sedentarismo","Una vida distinta"],[
 S(1,"Cómo empezó",[P("Hace unos 12.000 años, al terminar la última glaciación, el clima se volvió más templado. En varias regiones, algunos grupos empezaron a <b>sembrar</b> plantas y a <b>criar</b> animales: es la Revolución Neolítica.")]),
 S(1,"Domesticar",[D("Domesticación","Proceso por el cual las personas seleccionan y cuidan plantas y animales para que den más alimento y sean más fáciles de manejar."),T("Ejemplos",["Plantas","Animales"],[["Trigo y cebada","Ovejas y cabras"],["Arroz y mijo","Cerdos y gallinas"],["Maíz, frijol y papa","Llamas y pavos"]])]),
 S(2,"Sedentarismo",[P("Para cuidar los cultivos había que quedarse cerca: surgió el <b>sedentarismo</b>. Las familias construyeron casas de barro, piedra o adobe, y aparecieron las primeras aldeas.")]),
 S(2,"Una vida distinta",[T("Cambios en la vida cotidiana",["Antes","Después"],[["Movimiento constante","Vida en un lugar"],["Alimentos variados","Menos variedad, pero más cantidad"],["Pocas pertenencias","Cerámica, graneros y herramientas pulidas"]])])],
 {"titulo":"explicar","planteo":"¿Por qué el cultivo llevó al sedentarismo?","pasos":["Las plantas necesitan cuidado durante meses.","Quien las siembra debe estar presente en la cosecha.","Por eso se quedaron cerca de los campos."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Criar y seleccionar plantas y animales se llama ___ .","Vivir de forma estable en un lugar es el ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí dos cambios que trajo la agricultura a la vida cotidiana."},
 {"titulo":"Un proceso lento","texto":"No fue un invento de un día: llevó miles de años de probar y seleccionar."},
 ["Creer que la agricultura apareció de golpe.","Pensar que todos dejaron de cazar enseguida."],
 RS(("Neolítico","Piedra nueva."),("Domesticación","Plantas y animales."),("Sedentarismo","Vida en un lugar."),("Aldeas","Primeras casas fijas.")),
 G(("Neolítico","Período de la piedra pulida y la agricultura."),("Domesticar","Criar y seleccionar plantas y animales."),("Sedentario","Que vive en un lugar fijo."),("Cosecha","Recolección de lo sembrado.")),
 ["¿Cómo se llama el proceso de criar y seleccionar plantas y animales?","¿Cómo se llama vivir de forma estable en un lugar?","¿Qué planta se domesticó en Mesoamérica: el trigo o el maíz?","La agricultura, ¿apareció de golpe o en un proceso lento?"],
 [["domesticacion","domesticación","la domesticacion","la domesticación"],["sedentarismo","el sedentarismo"],["maiz","maíz","el maiz","el maíz"],["lento","proceso lento","en un proceso lento"]],
 {"incompleto":"Domesticación. Sedentarismo.","solo":"Más comida y casas fijas; pero también más trabajo.","carpeta":["Domesticación.","Sedentarismo.","El maíz.","En un proceso lento."]})
B2=NV("Vas a explicar cómo el excedente y las aldeas llevaron a una nueva división del trabajo y a desigualdades.",["Las primeras aldeas","El excedente","División del trabajo","Desigualdades"],[
 S(1,"Aldeas",[P("Las aldeas neolíticas, como Jericó o Çatalhöyük, reunían decenas o cientos de familias. Tenían casas, graneros y a veces murallas.")]),
 S(1,"El excedente",[D("Excedente","Cantidad de alimento que sobra después de cubrir las necesidades del grupo."),P("El excedente se podía guardar en graneros para tiempos malos o intercambiar con otros grupos.")]),
 S(2,"División del trabajo",[T("Nuevas ocupaciones",["Ocupación","Qué hacía"],[["Agricultores y pastores","Producir alimentos"],["Alfareros","Fabricar vasijas para guardar granos y agua"],["Tejedores","Hacer telas de lana o lino"],["Constructores","Levantar casas y graneros"]])]),
 S(2,"Desigualdades",[P("Con el excedente y la propiedad de la tierra, algunas familias acumularon más que otras. Aparecieron <b>desigualdades</b> y personas que dirigían el reparto, la defensa o los rituales.")])],
 {"titulo":"razonar","planteo":"¿Qué cambió cuando un grupo logró tener excedente?","pasos":["No todos tenían que producir alimento.","Algunas personas pudieron dedicarse a otros oficios.","Algunas familias acumularon más y crecieron las desigualdades."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El alimento que sobra es el ___ .","Los oficios distintos son la división del ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un oficio nuevo del Neolítico y por qué antes no existía."},
 {"titulo":"Excedente = cambio","texto":"Casi todos los cambios sociales del Neolítico empiezan por el excedente."},
 ["Creer que todos eran iguales en las aldeas.","Pensar que los oficios existieron desde siempre."],
 RS(("Aldea","Casas y graneros."),("Excedente","Lo que sobra."),("Oficios","Alfarero, tejedor."),("Desigualdad","Algunos acumulan más.")),
 G(("Excedente","Alimento que sobra."),("División del trabajo","Reparto de tareas entre personas."),("Alfarero","Quien fabrica objetos de arcilla."),("Propiedad","Derecho sobre algo.")),
 ["¿Cómo se llama el alimento que sobra después de cubrir las necesidades?","¿Qué oficio fabrica vasijas de arcilla?","¿Qué aparece cuando algunas familias acumulan más que otras?","¿Todos tenían que producir alimento cuando hubo excedente? Respondé sí o no."],
 [["excedente","el excedente"],["alfarero","alfareros","el alfarero","alfareria","alfarería"],["desigualdad","desigualdades","la desigualdad"],["no"]],
 {"incompleto":"Excedente. Trabajo.","solo":"Tejedor: hacer telas exigía tiempo que antes se usaba solo en conseguir comida.","carpeta":["El excedente.","Alfarero.","Desigualdades.","No."]})
B3=NV("Vas a ubicar y comparar los centros donde surgió la agricultura de manera independiente.",["Cuatro centros","Medio Oriente y China","Mesoamérica y Andes","Qué tienen en común"],[
 S(1,"Cuatro centros",[T("Centros y cultivos",["Región","Plantas","Animales"],[["Medio Oriente (Creciente Fértil)","Trigo, cebada, lentejas","Ovejas, cabras"],["China","Arroz, mijo","Cerdos"],["Mesoamérica","Maíz, frijol, calabaza","Pavos"],["Andes","Papa, quinoa","Llamas, alpacas"]])]),
 S(1,"Medio Oriente y China",[P("En el <b>Creciente Fértil</b> (entre los ríos Tigris y Éufrates y el Mediterráneo oriental) apareció el cultivo de cereales hace unos 12.000 años. En China, a orillas del río Amarillo y el Yangtsé, se cultivaron mijo y arroz.")]),
 S(2,"Mesoamérica y Andes",[P("En Mesoamérica se domesticó el <b>maíz</b> a partir de una planta silvestre llamada teosinte, y se cultivó junto al frijol y la calabaza. En los Andes se domesticaron la <b>papa</b> y la quinoa, y la llama, que sirvió para carga y lana.")]),
 S(2,"Qué tienen en común",[P("Cada región <b>domesticó</b> sus propias especies, sin copiarse: el cambio surgió en lugares distintos y casi al mismo tiempo, lo que muestra que respondía a condiciones parecidas: clima templado y grupos que ya conocían muy bien las plantas.")])],
 {"titulo":"comparar","planteo":"¿Qué diferencia hay entre los cultivos de Mesoamérica y los del Medio Oriente?","pasos":["Medio Oriente: trigo, cebada y lentejas.","Mesoamérica: maíz, frijol y calabaza.","Cada región domesticó plantas distintas."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El maíz se domesticó en ___ .","La papa se domesticó en los ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una región y escribí qué cultivaba y qué animal criaba."},
 {"titulo":"Mismo cambio, distintos cultivos","texto":"Cada región dependió de las plantas y animales que tenía cerca."},
 ["Creer que la agricultura se difundió desde un solo lugar.","Pensar que en América se cultivaba trigo desde el principio."],
 RS(("Medio Oriente","Trigo y ovejas."),("China","Arroz y mijo."),("Mesoamérica","Maíz y frijol."),("Andes","Papa y llama.")),
 G(("Creciente Fértil","Región de Medio Oriente donde surgió la agricultura."),("Mesoamérica","Región cultural del actual México y América Central."),("Teosinte","Planta silvestre antecesora del maíz.")),
 ["¿Qué cereal se domesticó en el Creciente Fértil: el trigo o el maíz?","¿Qué cultivo de los Andes es muy conocido: la papa o el arroz?","¿Qué animal domesticaron en los Andes para carga y lana?","¿La agricultura apareció en un solo lugar o en varios? Respondé \"un solo lugar\" o \"varios\"."],
 [["trigo","el trigo"],["papa","la papa"],["llama","la llama","llamas"],["varios","en varios","varios lugares"]],
 {"incompleto":"Maíz. Papa.","solo":"China: arroz y mijo; cerdos.","carpeta":["El trigo.","La papa.","La llama.","Varios."]})
B4=NV("Vas a evaluar si el Neolítico fue realmente una revolución, qué cambió y qué siguió igual.",["Qué es una revolución","Los cambios","Las continuidades","Costos y beneficios"],[
 S(1,"Revolución",[P("El historiador Gordon Childe llamó a este período <b>Revolución Neolítica</b> porque cambió profundamente la forma de vivir. Hoy se discute el nombre: duró miles de años, así que fue una transformación muy lenta.")]),
 S(1,"Cambios",[T("Qué cambió",["Aspecto","Cambio"],[["Alimentación","Se produce el alimento"],["Vivienda","Casas y aldeas fijas"],["Sociedad","Más población, oficios y desigualdades"],["Tecnología","Cerámica, piedra pulida, tejidos"]])]),
 S(2,"Continuidades",[P("No todo cambió: muchos grupos siguieron cazando y recolectando, otros combinaron las dos formas de vida, y siguieron la cooperación familiar y las creencias en rituales.")]),
 S(2,"Costos y beneficios",[T("Balance",["Beneficios","Costos"],[["Más alimento y más población","Más trabajo diario"],["Vivienda segura","Enfermedades por vivir juntos y con animales"],["Almacenar en tiempos malos","Dependencia de las cosechas y desigualdades"]])])],
 {"titulo":"argumentar","planteo":"¿Fue una revolución o un cambio lento?","pasos":["Cambió casi todo: alimentación, vivienda y sociedad.","Pero tardó miles de años y no ocurrió en todos lados.","Se puede llamar revolución por sus efectos, aunque fue lenta."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El historiador que usó la expresión Revolución Neolítica fue Gordon ___ .","Lo que sigue igual a pesar de un cambio se llama ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un beneficio y un costo de la agricultura."},
 {"titulo":"Cambios y continuidades","texto":"Cuando analices un proceso histórico, buscá qué cambió y qué siguió igual."},
 ["Pensar que fue solo un progreso sin costos.","Creer que cambió todo para todos a la vez."],
 RS(("Childe","Nombre de la revolución."),("Cambios","Alimento, aldeas, oficios."),("Continuidades","Caza, rituales."),("Balance","Beneficios y costos.")),
 G(("Revolución","Cambio profundo."),("Continuidad","Lo que se mantiene en el tiempo."),("Balance","Comparación de ventajas y desventajas.")),
 ["¿Cómo se llama lo que sigue igual a pesar de un cambio?","¿Duró la Revolución Neolítica pocos años o miles de años?","¿Todos los grupos dejaron de cazar y recolectar? Respondé sí o no.","Un costo de la agricultura: ¿más trabajo o menos trabajo?"],
 [["continuidad","continuidades","la continuidad"],["miles de años","miles"],["no"],["mas trabajo","más trabajo"]],
 {"incompleto":"Childe. Continuidad.","solo":"Beneficio: más alimento. Costo: más trabajo y enfermedades.","carpeta":["Continuidad.","Miles de años.","No.","Más trabajo."]})
ACT10={"1":[{"t":"ordering","p":"Ordená el proceso.","o":["Aldeas","Sembrar y criar","Cazar y recolectar","Sedentarismo"],"r":{"orden":["Cazar y recolectar","Sembrar y criar","Sedentarismo","Aldeas"]},"e":"De la vida nómada a las aldeas."},MC("La domesticación es…",["Criar y seleccionar plantas y animales","Cazar animales","Pintar cuevas","Viajar"],"Criar y seleccionar plantas y animales","Para tener más alimento.")],
 "2":[{"t":"matching","p":"Uní cada ocupación con su tarea.","o":{"izquierda":["Alfarero","Tejedor","Pastor","Constructor"],"derecha":["Fabrica vasijas","Hace telas","Cuida animales","Levanta casas"]},"r":{"pares":{"Alfarero":"Fabrica vasijas","Tejedor":"Hace telas","Pastor":"Cuida animales","Constructor":"Levanta casas"}},"e":"Oficios del Neolítico."},MC("El excedente permitió…",["Que algunos se dedicaran a otros oficios","Que desaparecieran las aldeas","Que no hubiera comida","Volver a cazar"],"Que algunos se dedicaran a otros oficios","Ya no todos producían alimento.")],
 "3":[{"t":"classify","p":"¿De qué centro es cada cultivo?","o":{"elementos":["Trigo","Maíz","Papa","Arroz"],"categorias":["Medio Oriente","China","Mesoamérica","Andes"]},"r":{"categorias":{"Trigo":"Medio Oriente","Maíz":"Mesoamérica","Papa":"Andes","Arroz":"China"}},"e":"Cada región domesticó sus especies."},MC("¿Qué animal se domesticó en los Andes?",["La llama","La oveja","El cerdo","El caballo"],"La llama","Para carga y lana.")],
 "4":[{"t":"classify","p":"¿Cambio o continuidad?","o":{"elementos":["Aldeas fijas","Se siguió cazando","Cerámica","Creencias en rituales"],"categorias":["Cambio","Continuidad"]},"r":{"categorias":{"Aldeas fijas":"Cambio","Se siguió cazando":"Continuidad","Cerámica":"Cambio","Creencias en rituales":"Continuidad"}},"e":"Algo cambió, algo siguió."},MC("¿Fue la agricultura solo un progreso sin costos?",["No: tuvo costos","Sí","Solo en China","Solo en América"],"No: tuvo costos","Más trabajo y enfermedades.")],
 "5":[MC("Relámpago. Criar y seleccionar plantas y animales es…",["Domesticar","Cazar","Migrar"],"Domesticar","Origen de la agricultura.",tiempo=20),MC("Relámpago. El alimento que sobra es el…",["Excedente","Déficit","Impuesto"],"Excedente","Se guarda o se intercambia.",tiempo=20),MC("Relámpago. El maíz se domesticó en…",["Mesoamérica","China","Europa"],"Mesoamérica","Junto con el frijol.",tiempo=20),MC("Relámpago. El Neolítico duró…",["Miles de años","Un año","Un día"],"Miles de años","Fue un proceso lento.",tiempo=20)]}
EX10=[[1,MC("La Revolución Neolítica comenzó con…",["La agricultura y la ganadería","La escritura","Los metales","Las ciudades-estado"],"La agricultura y la ganadería","Hace unos 12.000 años.")],
 [1,MC("El sedentarismo es…",["Vivir de forma estable en un lugar","Viajar siempre","Cazar mamuts","Pintar cuevas"],"Vivir de forma estable en un lugar","Surgió al cultivar.")],
 [1,VF("La agricultura apareció de golpe y en un solo año.","Falso","Fue un proceso muy lento.")],
 [2,MC("El excedente es…",["El alimento que sobra","Una herramienta","Un oficio","Una aldea"],"El alimento que sobra","Se guarda o se intercambia.")],
 [2,MC("¿Qué oficio nuevo apareció gracias al excedente?",["Alfarero","Cazador de mamuts","Recolector nómada","Ninguno"],"Alfarero","Fabrica vasijas.")],
 [2,VF("En las aldeas neolíticas aparecieron desigualdades.","Verdadero","Algunas familias acumularon más.")],
 [3,MC("¿Dónde surgió el cultivo de trigo y cebada?",["Medio Oriente","Mesoamérica","Los Andes","Oceanía"],"Medio Oriente","En el Creciente Fértil.")],
 [3,MC("El maíz se domesticó en…",["Mesoamérica","China","África","Europa"],"Mesoamérica","A partir del teosinte.")],
 [3,VF("La agricultura se difundió desde un único lugar.","Falso","Surgió de forma independiente en varios.")],
 [4,MC("¿Quién llamó \"Revolución Neolítica\" a este período?",["Gordon Childe","Charles Darwin","Heródoto","Colón"],"Gordon Childe","Hoy se discute el nombre.")],
 [4,MC("Una continuidad en el Neolítico fue…",["Que muchos siguieron cazando y recolectando","Que todos eran agricultores","Que no hubo aldeas","Que no había rituales"],"Que muchos siguieron cazando y recolectando","No todo cambió.")],
 [4,MC("Un costo de la agricultura fue…",["Más trabajo y enfermedades","Menos población","Menos casas","Menos alimentos siempre"],"Más trabajo y enfermedades","Convivir con animales trajo contagios.")],
 [4,VF("La agricultura trajo solo ventajas.","Falso","También tuvo costos.")]]
M10={"subject_id":SID,"tema":10,"practica":"Práctica general: la Revolución Neolítica","examen_titulo":"Nivel jefe: la Revolución Neolítica","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT10,"examen":EX10}
for n,m in ((9,M9),(10,M10)):
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
STEPS={(9,1):"d4e4225e-02f7-438c-898d-943e06a50da6",(9,2):"59a74de9-a303-4770-801f-4e7340e68369",(9,3):"6cc141b8-e6de-4276-93c4-1bf68c3b3fc8",(9,4):"024d10be-6a43-454b-bbcb-9d92b4f03213",(10,1):"d8a631ca-09a4-4c42-b3bd-f635ec081f06",(10,2):"1eea37cc-64cd-4ce9-b65e-e1c7088ce11b",(10,3):"2076fbd9-36e6-41a2-96b5-4c2af1382f74",(10,4):"c5309a61-217d-4f97-812e-dc02460d309f"}
TIT={(9,1):"Hominización: cómo llegamos a ser humanos",(9,2):"Cazadores y recolectores: trabajo y autoridad",(9,3):"Arte, rituales y creencias en la prehistoria",(9,4):"Un planeta que se puebla: de África a América",(10,1):"Sembrar y criar: el comienzo de la agricultura y la ganadería",(10,2):"Aldeas, excedente y división del trabajo",(10,3):"El Neolítico en el mundo: Medio Oriente, China, Mesoamérica y los Andes",(10,4):"¿Una revolución? Cambios y continuidades"}
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
LN=lambda t,ev,v:{"t":"linea","titulo":t,"eventos":[{"fecha":a,"txt":b,"emoji":c} for a,b,c in ev],"voz":v}
CLS={(9,1):[
 {"t":"reto","texto":"¿Qué dos cosas cambiaron al caminar erguidos?","segundos":6,"respuesta":"Las manos quedaron libres y se vio más lejos","emoji":"🚶","titulo":"HOMINIZACIÓN","sub":"cómo llegamos a ser humanos","voz":["Desafío: ¿qué cambió al caminar erguidos? Seis segundos.","Las manos quedaron libres y se podía ver más lejos.","Hoy: *la hominización*."]},
 DEF("Hominización","El proceso por el que aparecieron los humanos actuales","🦴",["La *hominización* es el proceso de millones de años por el que aparecieron los humanos actuales.","Empezó en *África*."]),
 LN("LAS ESPECIES",[("4 millones","Australopithecus","🦴"),("2,4 millones","Homo habilis","🪨"),("1,9 millones","Homo erectus","🔥"),("300.000","Homo sapiens","🧠")],["Cuatro especies clave, de las más antiguas a la actual.","El *Australopithecus*, hace unos cuatro millones de años: caminaba erguido.","El *Homo habilis*: fabricaba herramientas de piedra.","El *Homo erectus*: usó el fuego y salió de África.","Y el *Homo sapiens*, hace unos trescientos mil años."]),
 CAU(("Grandes cambios",'🧬'),[("Bipedismo","🚶"),("Cerebro grande","🧠"),("Fuego","🔥"),("Lenguaje","💬")],["¿Qué cambió?","El *bipedismo* liberó las manos.","El *cerebro* creció.","El *fuego* dio calor y cocción.","Y el *lenguaje* permitió transmitir lo aprendido."]),
 CL([("CAMBIO FÍSICO","🦴"),("CAMBIO CULTURAL","🔥")],[("Caminar erguido",0),("Usar fuego",1),("Cerebro más grande",0),("Hablar",1)],["¿Físico o cultural?","*Caminar erguido* y *cerebro más grande*: físicos.","*Usar fuego* y *hablar*: culturales."]),
 Q("¿Qué especie fabricó las primeras herramientas de piedra?",["Homo habilis","Homo sapiens","Australopithecus"],0,["Te toca: ¿quién fabricó las primeras herramientas de piedra?","¿Homo habilis, Homo sapiens o Australopithecus?","El *Homo habilis*."]),
 DEF("Fósil","Resto de un ser vivo del pasado","🦴",["Los científicos estudian *fósiles*: huesos de seres del pasado.","También herramientas y ADN."]),
 ER([("Descendemos de los monos actuales","Compartimos antepasados"),("Una línea recta de especies","Varias convivieron")],["Errores típicos.","Creer que *descendemos de los monos actuales*.","Y pensar en una *línea recta* de especies."]),
 RES(["Repasemos.","La *hominización* empezó en África.","Hubo varias especies.","El *bipedismo*, el *cerebro*, el *fuego* y el *lenguaje* fueron claves.","Y la ciencia revisa lo que sabe.","¡Clase terminada! Ahora, *a practicar*."],[["ORIGEN","África"],["ESPECIES","varias"],["CAMBIOS","bipedismo, fuego"],["FUENTES","fósiles"]])],
(9,2):[
 {"t":"historia","personaje":{"nombre":"Kai","emoji":"🧒"},"lugar":"🏕️","lineas":["Kai vive en una banda de treinta personas.","Hoy toca mudarse: se acabó la comida cerca."],"titulo":"CAZADORES Y RECOLECTORES","sub":"trabajo y autoridad","voz":["Kai vive en una banda de treinta personas.","Hoy toca mudarse: se acabó la comida cerca.","Hoy: *cazadores y recolectores*."]},
 DEF("Nómadas","Se desplazaban siguiendo el alimento","🚶",["Los cazadores y recolectores eran *nómadas*.","Se movían siguiendo a los animales y las estaciones."]),
 CAU(("Cómo se repartían el trabajo",'🧰'),[("Cazar","🏹"),("Recolectar","🌰"),("Cuidar a los niños","🧸")],["Las tareas se repartían según edad y habilidades.","Algunos *cazaban*.","Otros *recolectaban* frutos, semillas y raíces.","Y otros *cuidaban a los niños*."]),
 CMP(("AUTORIDAD","Experiencia, sin jefes fijos","🗣️"),("RIQUEZA","Casi sin diferencias","⚖️"),"+",["Casi no había desigualdades.","Tenía influencia quien mostraba *experiencia*.","Y las decisiones se *discutían entre todos*."]),
 TB("QUÉ USABAN",["Recurso","Para qué"],[["Piedra tallada","Cortar y cazar"],["Hueso","Agujas y arpones"],["Fuego","Calor y cocción"]],["Sus herramientas.","La *piedra tallada*: cortar y cazar.","El *hueso*: agujas y arpones.","El *fuego*: calor y cocción."]),
 CL([("PALEOLÍTICO","🏹"),("NO PALEOLÍTICO","🌾")],[("Nómadas",0),("Acumular cosechas",1),("Compartir lo cazado",0)],["¿Paleolítico o no?","*Nómadas* y *compartir lo cazado*: sí.","*Acumular cosechas*: es de la agricultura."]),
 Q("¿Cómo se tomaban las decisiones en una banda?",["Se discutían entre todos","Las decidía un rey","Las decidía un ejército"],0,["Te toca: ¿cómo se tomaban las decisiones?","¿Entre todos, por un rey o por un ejército?","*Entre todos*: no había jefes permanentes."]),
 ER([("Había reyes","No había jefes permanentes"),("Vivían fijos en un lugar","Eran nómadas")],["Errores típicos.","Creer que había *reyes*.","Y pensar que vivían *fijos* en un lugar."]),
 RES(["Repasemos.","Eran *nómadas*.","Vivían en bandas de *veinte a cincuenta* personas.","El trabajo se *repartía* y se *compartía*.","Y las decisiones eran de todos.","¡Clase terminada! Ahora, *a practicar*."],[["NÓMADAS","se movían"],["BANDAS","20 a 50"],["TRABAJO","se repartía"],["DECISIONES","entre todos"]])],
(9,3):[
 {"t":"noticia","cinta":"HALLAZGO","titular":"Manos pintadas hace miles de años","bajada":"Una cueva guarda mensajes de la prehistoria","emoji":"🖐️","titulo":"ARTE Y CREENCIAS","sub":"en la prehistoria","voz":["Hallazgo: manos pintadas hace miles de años.","Una cueva guarda mensajes de la prehistoria.","Hoy: *arte, rituales y creencias*."]},
 DEF("Arte rupestre","Pinturas y grabados en cuevas y rocas","🎨",["El *arte rupestre* son pinturas y grabados en cuevas y rocas.","Se hacían con pigmentos naturales, como ocre y carbón."]),
 TB("CUEVAS FAMOSAS",["Cueva","País"],[["Altamira","España"],["Lascaux","Francia"],["Cueva de las Manos","Argentina"]],["Tres cuevas famosas.","*Altamira*, en España.","*Lascaux*, en Francia.","Y la *Cueva de las Manos*, en Santa Cruz, Argentina."]),
 DEF("Entierros","Muertos enterrados con ofrendas","⚱️",["Algunos grupos enterraban a sus muertos con ofrendas.","Eso muestra *creencias* sobre la muerte."]),
 CAU(("Qué significaban las pinturas",'❓'),[("Magia de la caza","🏹"),("Ritual","🕯️"),("Registro","📜")],["¿Qué significaban?","*Magia de la caza*: pintar animales traería suerte.","*Ritual*: la cueva sería un lugar sagrado.","*Registro*: contar lo que vivía el grupo."]),
 CL([("SE SABE","✅"),("HIPÓTESIS","❓")],[("Se pintaba con ocre",0),("Pintar para cazar",1),("Había entierros",0)],["¿Se sabe o es hipótesis?","Que se pintaba con *ocre* y que había *entierros*, se sabe.","Que se pintaba *para cazar*, es hipótesis."]),
 Q("El sentido de las pinturas rupestres, ¿se conoce con certeza?",["No: hay hipótesis","Sí: está escrito","Sí: lo dicen las vasijas"],0,["Te toca: ¿se conoce con certeza el sentido de las pinturas?","¿No y hay hipótesis, sí porque está escrito, o sí por las vasijas?","*No*: sin escritura, son hipótesis."]),
 ER([("Sabemos qué significaban","Son hipótesis"),("No tenían creencias","Hay entierros y arte")],["Errores típicos.","Creer que *sabemos* qué significaban.","Y pensar que *no tenían creencias*."]),
 RES(["Repasemos.","El *arte rupestre* pinta cuevas y rocas.","Los *entierros* muestran creencias.","El sentido es una *hipótesis*.","Y era *pensamiento simbólico*.","¡Clase terminada! Ahora, *a practicar*."],[["RUPESTRE","cuevas y rocas"],["ENTIERROS","ofrendas"],["SENTIDO","hipótesis"],["SIMBÓLICO","imágenes"]])],
(9,4):[
 {"t":"gancho","grande":"70.000 años","emoji":"👣","final":"todos los continentes","titulo":"EL POBLAMIENTO","sub":"de África a América","voz":["Hace unos setenta mil años, unos pocos grupos salieron de África.","Y terminaron ocupando todos los continentes.","Hoy: *el poblamiento del planeta*."]},
 LN("EL VIAJE",[("300.000","Aparece el Homo sapiens","🌍"),("70.000","Sale de África","👣"),("50.000","Llega a Australia","🦘"),("15.000","Llega a América","🏔️")],["Las etapas, con fechas aproximadas.","Hace unos *trescientos mil años*, el Homo sapiens aparece en África.","Hace unos *setenta mil*, sale de África.","Hace unos *cincuenta mil*, llega a Australia.","Y hace más de *quince mil*, llega a América."]),
 DEF("Beringia","Tierra entre Siberia y Alaska","🧊",["Durante las glaciaciones el mar bajó.","Apareció *Beringia*, una franja de tierra entre Siberia y Alaska."]),
 CAU(("Por qué se movían",'🧭'),[("Seguir animales","🦌"),("Cambios del clima","🌡️"),("Crecía el grupo","👪")],["¿Por qué se movían?","Para *seguir a los animales*.","Por los *cambios del clima*.","Y porque el *grupo crecía*."]),
 CL([("ANTES","⏪"),("DESPUÉS","⏩")],[("África",0),("Australia",1),("América",1)],["¿Antes o después?","*África*: el origen.","*Australia* y *América*: llegadas posteriores."]),
 Q("¿Cómo se llama la franja de tierra que unió Siberia y Alaska?",["Beringia","Pangea","Atlántida"],0,["Te toca: ¿cómo se llama la franja de tierra entre Siberia y Alaska?","¿Beringia, Pangea o Atlántida?","*Beringia*."]),
 DEF("Fechas aproximadas","Pueden cambiar con nuevos hallazgos","📅",["Las fechas son *aproximadas*.","Pueden cambiar con nuevos descubrimientos."]),
 ER([("Fechas exactas","Fechas aproximadas"),("Llegaron en barcos de metal","Por Beringia o la costa")],["Errores típicos.","Creer que las fechas son *exactas*.","Y pensar que llegaron en *barcos de metal*."]),
 RES(["Repasemos.","El Homo sapiens *salió de África*.","Se extendió por *todos los continentes*.","A América llegó por *Beringia* o la costa.","Las fechas son *aproximadas*.","¡Clase terminada! Ahora, *a practicar*."],[["ORIGEN","África"],["SALIDA","hace 70.000 años"],["AMÉRICA","Beringia"],["FECHAS","aproximadas"]])],
(10,1):[
 {"t":"historia","personaje":{"nombre":"Noa","emoji":"👧"},"lugar":"🌾","lineas":["Noa guardó semillas de las plantas más grandes.","Al año siguiente, las sembró cerca de su casa."],"titulo":"SEMBRAR Y CRIAR","sub":"el comienzo de la agricultura","voz":["Noa guardó las semillas de las plantas más grandes.","Al año siguiente, las sembró cerca de su casa.","Hoy: *el comienzo de la agricultura*."]},
 DA("12.000","años atrás","empezó la agricultura","Al terminar la última glaciación, el clima se volvió más templado","🌱",["Hace unos *doce mil años* empezó la agricultura.","Al terminar la última glaciación, el clima se volvió más templado."]),
 DEF("Domesticación","Criar y seleccionar plantas y animales","🐑",["La *domesticación* es criar y seleccionar plantas y animales.","Así dan más alimento y son más fáciles de manejar."]),
 TB("EJEMPLOS",["Plantas","Animales"],[["Trigo","Ovejas"],["Arroz","Cerdos"],["Maíz","Pavos"]],["Algunas domesticaciones.","*Trigo* y *ovejas*, en Medio Oriente.","*Arroz* y *cerdos*, en China.","*Maíz* y *pavos*, en Mesoamérica."]),
 AD(("ANTES","🏕️","vida nómada"),("DESPUÉS","🏘️","aldeas fijas"),["Un cambio de vida.","Antes, vida *nómada*.","Después, *aldeas fijas*: el sedentarismo."]),
 CL([("VIDA NÓMADA","🏕️"),("VIDA SEDENTARIA","🏘️")],[("Cazar",0),("Sembrar",1),("Graneros",1)],["¿Nómada o sedentaria?","*Cazar*: nómada.","*Sembrar* y *graneros*: sedentaria."]),
 Q("Criar y seleccionar plantas y animales se llama…",["Domesticación","Migración","Excavación"],0,["Te toca: criar y seleccionar plantas y animales.","¿Domesticación, migración o excavación?","*Domesticación*."]),
 ER([("Apareció de golpe","Fue un proceso lento"),("Todos dejaron de cazar","Muchos siguieron")],["Errores típicos.","Creer que apareció *de golpe*.","Y pensar que *todos dejaron de cazar*."]),
 RES(["Repasemos.","Hace unos *doce mil años* empezó la agricultura.","Se *domesticaron* plantas y animales.","Surgió el *sedentarismo*.","Y fue un proceso *lento*.","¡Clase terminada! Ahora, *a practicar*."],[["INICIO","hace 12.000 años"],["DOMESTICACIÓN","plantas y animales"],["SEDENTARISMO","vida en un lugar"],["PROCESO","lento"]])],
(10,2):[
 {"t":"noticia","cinta":"ARQUEOLOGÍA","titular":"Hallan graneros de hace 10.000 años","bajada":"Guardaban granos para los tiempos malos","emoji":"🏺","titulo":"ALDEAS Y EXCEDENTE","sub":"y división del trabajo","voz":["Arqueología: hallan graneros de hace diez mil años.","Guardaban granos para los tiempos malos.","Hoy: *aldeas*, *excedente* y *división del trabajo*."]},
 DEF("Excedente","El alimento que sobra","🌾",["El *excedente* es el alimento que sobra.","Se guardaba o se intercambiaba."]),
 CAU(("Qué permitió el excedente",'🌾'),[("Guardar en graneros","🏺"),("Intercambiar","🤝"),("Nuevos oficios","🧵")],["¿Qué permitió el excedente?","*Guardar* en graneros para tiempos malos.","*Intercambiar* con otros grupos.","Y que aparecieran *nuevos oficios*."]),
 TB("NUEVOS OFICIOS",["Oficio","Tarea"],[["Alfarero","Vasijas"],["Tejedor","Telas"],["Constructor","Casas y graneros"]],["Algunos oficios.","El *alfarero* fabricaba vasijas.","El *tejedor*, telas.","Y el *constructor*, casas y graneros."]),
 CMP(("IGUALDAD","Antes, pocas diferencias","⚖️"),("DESIGUALDAD","Después, algunos acumulan","📈"),"→",["Un cambio social importante.","Antes, casi *sin diferencias*.","Después, algunas familias *acumularon más* y hubo desigualdad."]),
 CL([("OFICIO NUEVO","🧵"),("YA EXISTÍA","🏹")],[("Alfarero",0),("Cazador",1),("Tejedor",0)],["¿Oficio nuevo o ya existía?","*Alfarero* y *tejedor*: nuevos.","*Cazador*: ya existía."]),
 Q("¿Qué permitió que algunas personas se dedicaran a otros oficios?",["El excedente","El fuego","El nomadismo"],0,["Te toca: ¿qué permitió que se dedicaran a otros oficios?","¿El excedente, el fuego o el nomadismo?","El *excedente*: ya no todos producían alimento."]),
 ER([("Todos eran iguales","Aparecieron desigualdades"),("Los oficios existieron siempre","Surgieron con el excedente")],["Errores típicos.","Creer que *todos eran iguales*.","Y pensar que los oficios *existieron siempre*."]),
 RES(["Repasemos.","El *excedente* es el alimento que sobra.","Permitió *guardar* e *intercambiar*.","Aparecieron *nuevos oficios*.","Y también *desigualdades*.","¡Clase terminada! Ahora, *a practicar*."],[["EXCEDENTE","lo que sobra"],["GRANEROS","guardar"],["OFICIOS","alfarero, tejedor"],["DESIGUALDAD","acumular"]])],
(10,3):[
 {"t":"chat","contacto":{"nombre":"Lola","emoji":"👩"},"mensajes":[{"yo":False,"txt":"¿Sabías que el maíz viene de una planta silvestre?"},{"yo":True,"txt":"¿En serio? 🌽"},{"yo":False,"txt":"Del teosinte, en Mesoamérica"}],"titulo":"EL NEOLÍTICO EN EL MUNDO","sub":"cuatro centros","voz":["Lola le cuenta a Mati que el maíz viene de una planta silvestre.","Mati no lo puede creer.","Lola: del teosinte, en Mesoamérica.","Hoy: *el Neolítico en el mundo*."]},
 TB("CUATRO CENTROS",["Región","Cultivos","Animales"],[["Medio Oriente","Trigo, cebada","Ovejas, cabras"],["China","Arroz, mijo","Cerdos"],["Mesoamérica","Maíz, frijol","Pavos"],["Andes","Papa, quinoa","Llamas"]],["Cuatro centros independientes.","*Medio Oriente*: trigo y cebada; ovejas y cabras.","*China*: arroz y mijo; cerdos.","*Mesoamérica*: maíz y frijol; pavos.","*Los Andes*: papa y quinoa; llamas."]),
 {"t":"mapa","zona":"mundo","pasos":[{"resaltar":["Irak","Siria"],"color":"#d9a441","texto":"Medio Oriente"},{"resaltar":["China"],"color":"#c0392b","texto":"China"},{"resaltar":["México","Guatemala"],"color":"#3fa07a","texto":"Mesoamérica"},{"resaltar":["Perú","Bolivia"],"color":"#8a6bbf","texto":"Andes"}],"voz":["Dónde surgió la agricultura.","En el *Medio Oriente*.","En *China*.","En *Mesoamérica*.","Y en los *Andes*."]},
 DEF("Creciente Fértil","Región de Medio Oriente donde surgió el cultivo de cereales","🌾",["El *Creciente Fértil* está entre los ríos Tigris y Éufrates y el Mediterráneo oriental.","Allí surgió el cultivo de cereales."]),
 CMP(("MESOAMÉRICA","Maíz, frijol y calabaza","🌽"),("ANDES","Papa, quinoa y llama","🥔"),"vs",["Dos centros de América.","*Mesoamérica*: maíz, frijol y calabaza.","Los *Andes*: papa, quinoa y la llama."]),
 CL([("MEDIO ORIENTE","🌾"),("AMÉRICA","🌽")],[("Trigo",0),("Maíz",1),("Papa",1),("Ovejas",0)],["¿Medio Oriente o América?","*Trigo* y *ovejas*: Medio Oriente.","*Maíz* y *papa*: América."]),
 Q("¿Dónde se domesticó el maíz?",["Mesoamérica","China","Medio Oriente"],0,["Te toca: ¿dónde se domesticó el maíz?","¿Mesoamérica, China o Medio Oriente?","En *Mesoamérica*."]),
 ER([("Se difundió desde un solo lugar","Surgió en varios"),("En América se cultivaba trigo","Maíz, papa y otros")],["Errores típicos.","Creer que se difundió *desde un solo lugar*.","Y pensar que en América se cultivaba *trigo*."]),
 RES(["Repasemos.","Hubo *cuatro centros* independientes.","Cada región *domesticó* lo suyo.","El *maíz*, en Mesoamérica.","La *papa* y la *llama*, en los Andes.","¡Clase terminada! Ahora, *a practicar*."],[["CENTROS","cuatro"],["MEDIO ORIENTE","trigo"],["MESOAMÉRICA","maíz"],["ANDES","papa y llama"]])],
(10,4):[
 {"t":"reto","texto":"¿Fue una revolución o un cambio muy lento?","segundos":6,"respuesta":"Cambió todo, pero tardó miles de años","emoji":"🤔","titulo":"¿UNA REVOLUCIÓN?","sub":"cambios y continuidades","voz":["Desafío: ¿fue una revolución o un cambio muy lento? Seis segundos.","Cambió casi todo, pero tardó miles de años.","Hoy: *cambios y continuidades*."]},
 DEF("Revolución Neolítica","Nombre que le dio Gordon Childe","📚",["El historiador *Gordon Childe* llamó *Revolución Neolítica* a este período.","Hoy se discute el nombre, porque fue muy lento."]),
 TB("QUÉ CAMBIÓ",["Aspecto","Cambio"],[["Alimentación","Se produce"],["Vivienda","Aldeas"],["Sociedad","Oficios y desigualdad"]],["Los cambios.","La *alimentación*: ahora se produce.","La *vivienda*: aldeas fijas.","La *sociedad*: oficios y desigualdades."]),
 CMP(("CAMBIO","Aldeas, cerámica","🏘️"),("CONTINUIDAD","Se siguió cazando, rituales","🏹"),"+",["Pero no todo cambió.","*Cambio*: aldeas y cerámica.","*Continuidad*: muchos siguieron cazando y los rituales continuaron."]),
 CAU(("Costos de la agricultura",'⚠️'),[("Más trabajo","🛠️"),("Enfermedades","🤒"),("Dependencia de la cosecha","🌧️")],["La agricultura tuvo costos.","*Más trabajo* diario.","*Enfermedades* por vivir juntos y con animales.","Y *dependencia* de las cosechas."]),
 CL([("BENEFICIO","✅"),("COSTO","⚠️")],[("Más alimento",0),("Más trabajo",1),("Graneros",0),("Enfermedades",1)],["¿Beneficio o costo?","*Más alimento* y *graneros*: beneficios.","*Más trabajo* y *enfermedades*: costos."]),
 Q("¿La agricultura trajo solo ventajas?",["No: también costos","Sí","Solo en América"],0,["Te toca: ¿la agricultura trajo solo ventajas?","¿No, sí o solo en América?","*No*: tuvo ventajas y costos."]),
 ER([("Fue solo progreso","Tuvo costos"),("Cambió todo a la vez","Fue lento y desigual")],["Errores típicos.","Creer que fue *solo progreso*.","Y pensar que *cambió todo a la vez*."]),
 RES(["Repasemos.","Cambió la *alimentación*, la vivienda y la sociedad.","Hubo *continuidades*.","Tuvo *beneficios* y *costos*.","Y fue un proceso *lento*.","¡Clase terminada! Ahora, *a practicar*."],[["CAMBIOS","alimento, aldeas"],["CONTINUIDADES","caza, rituales"],["BALANCE","ventajas y costos"],["RITMO","lento"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"soc1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciencias Sociales Integradas I","titulo":TIT[(m,n)],"sub":f"Ciencias Sociales Integradas I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"soc1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
