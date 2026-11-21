# -*- coding: utf-8 -*-
"""Ciencias Naturales Integradas I · Misión 6 (Ecosistemas argentinos, VARIANTE) y Misión 7 (Relaciones en el ecosistema)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}
SID = "9fa85d7b-ee7a-4853-8486-a69f9b539c12"

FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,ref,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":ref,"e":e,**k}
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}
# ================= MISIÓN 6: ECOSISTEMAS ARGENTINOS (VARIANTE) =================
A1=NV("Vas a explicar qué es una ecorregión y cómo el clima y el relieve explican la diversidad de ambientes de un país extenso.",["Ecorregión","Factores del clima","Climas de un país extenso","Clima y vida"],[
 S(1,"Ecorregión",[D("Ecorregión","Gran área con un clima, un relieve y una vida (plantas y animales) característicos."),PN("La Argentina es muy larga y tiene muchas ecorregiones: selvas en el norte, estepas en el sur, montañas en el oeste y llanuras en el centro.","Un país extenso tiene muchas ecorregiones: selvas, estepas, montañas, llanuras y costas, según su ubicación y su relieve.")]),
 S(1,"Factores del clima",[T("Qué decide el clima",["Factor","Cómo influye"],[["Latitud","Cerca del ecuador hace más calor; cerca de los polos, más frío"],["Altitud","Cuanto más alto, más frío"],["Cercanía al mar","El mar suaviza las temperaturas"],["Vientos y corrientes","Traen humedad o aire seco"]])]),
 S(2,"Climas de un país extenso",[PN("En la Argentina hay climas cálidos y lluviosos en el noreste, árido en el oeste y centro-oeste, templado en la Pampa y frío en la Patagonia y en las cumbres de los Andes.","Según su latitud y su relieve, un país extenso puede tener climas cálidos y lluviosos, áridos, templados y fríos."),T("Clima y precipitaciones",["Clima","Lluvias","Temperatura"],[["Cálido húmedo","Abundantes","Alta todo el año"],["Árido","Muy escasas","Cambia mucho entre el día y la noche"],["Templado","Moderadas","Estaciones marcadas"],["Frío","Variables","Baja gran parte del año"]])]),
 S(2,"Clima y vida",[P("El clima decide qué seres vivos pueden vivir en un lugar. Con mucha lluvia y calor hay <b>selvas</b>; con poca lluvia, <b>desiertos y arbustales</b>; con lluvias moderadas, <b>pastizales</b>; con frío, <b>estepas</b> y bosques de árboles resistentes.")])],
 {"titulo":"relacionar","planteo":"¿Por qué en una zona de mucha lluvia y calor hay selva y no desierto?","pasos":["El agua abundante permite que crezcan árboles muy altos.","El calor constante acelera el crecimiento.","Por eso hay selva."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Una gran área con clima, relieve y vida característicos es una ___ .","Cuanto más alto está un lugar, más ___ es su clima."]},
 {"titulo":"tu turno","planteo":"Elegí un lugar que conozcas y explicá cómo el clima influye en sus plantas."},
 {"titulo":"Clima primero","texto":"Para entender un ecosistema, empezá por su clima y su relieve."},
 ["Pensar que todo el país tiene el mismo clima.","Olvidar que la altura enfría."],
 RS(("Ecorregión","Clima, relieve y vida."),("Factores","Latitud, altitud, mar, vientos."),("Climas","Cálido, árido, templado, frío."),("Vida","Depende del clima.")),
 G(("Ecorregión","Área con clima y vida característicos."),("Latitud","Distancia al ecuador."),("Altitud","Altura sobre el nivel del mar."),("Árido","Con muy pocas lluvias.")),
 ["¿Cómo se llama una gran área con clima, relieve y vida característicos?","¿Qué factor hace que haga más frío cuanto más alto estás: latitud o altitud?","¿Qué clima tiene muy pocas lluvias?","¿Un mismo país puede tener muchos climas? Respondé sí o no."],
 [["ecorregion","ecorregión","una ecorregion","una ecorregión"],["altitud","la altitud"],["arido","árido","el arido","el árido"],["si","sí"]],
 {"incompleto":"Ecorregión. Frío.","solo":"En mi lugar llueve poco, por eso hay arbustos y no selva.","carpeta":["Ecorregión.","Altitud.","Árido.","Sí."]})
A2=NV("Vas a describir los ambientes de pastizal, monte y selva: clima, plantas, animales y suelo.",["Pastizal","Monte","Selva","Comparar"],[
 S(1,"Pastizal",[PN("En el Pastizal pampeano, una llanura de clima templado y suelos muy fértiles, predominan los pastos. Viven el ñandú, la vizcacha y el venado de las pampas. Hoy gran parte se usa para agricultura y ganadería.","El pastizal es una llanura de clima templado y suelos fértiles donde predominan los pastos. Allí viven aves corredoras y roedores. Hoy gran parte se usa para agricultura y ganadería.")]),
 S(1,"Monte",[PN("El Monte y el Chaco seco tienen clima árido o semiárido. Dominan arbustos con hojas pequeñas, como la jarilla, y árboles como el algarrobo y el quebracho. Viven el guanaco, el puma y muchos reptiles.","Los montes y chacos secos tienen clima árido o semiárido. Dominan arbustos con hojas pequeñas y árboles de raíces profundas. Viven mamíferos medianos, felinos y muchos reptiles.")]),
 S(2,"Selva",[PN("Las Yungas (en el noroeste) y la selva misionera (en el noreste) tienen mucha lluvia y calor. Hay árboles muy altos, lianas y epífitas. Viven el yaguareté, el tucán y los monos carayá.","Las selvas tienen mucha lluvia y calor. Hay árboles muy altos, lianas y epífitas. Viven grandes felinos, tucanes y monos.")]),
 S(2,"Comparar",[T("Tres ambientes",["Ambiente","Clima","Vegetación"],[["Pastizal","Templado","Pastos"],["Monte","Árido","Arbustos"],["Selva","Cálido y muy lluvioso","Árboles altos y lianas"]])])],
 {"titulo":"comparar","planteo":"¿Qué diferencia hay entre pastizal y selva?","pasos":["Pastizal: clima templado, pastos, pocos árboles.","Selva: clima cálido y muy lluvioso, árboles muy altos.","Cambia la cantidad de agua y, por eso, la vegetación."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["En el pastizal predominan los ___ .","La selva tiene mucha lluvia y ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí uno de los tres ambientes y describí su clima, una planta y un animal."},
 {"titulo":"Agua y vegetación","texto":"Cuanta más agua, más vegetación: la lluvia explica el paisaje."},
 ["Pensar que el monte es un lugar sin vida.","Confundir pastizal con estepa."],
 RS(("Pastizal","Pastos y suelo fértil."),("Monte","Árido, arbustos."),("Selva","Lluvia y calor."),("Comparar","Agua y vegetación.")),
 G(("Pastizal","Ambiente de pastos."),("Epífita","Planta que vive sobre otra sin dañarla."),("Fértil","Con muchos nutrientes."),("Semiárido","Con pocas lluvias.")),
 ["¿Qué ambiente tiene pastos y suelos fértiles?","¿En qué ambiente hay árboles muy altos y lianas?","¿Qué clima tiene el monte: árido o muy lluvioso?","¿Una planta epífita vive sobre otra o bajo tierra?"],
 [["pastizal","el pastizal"],["selva","la selva"],["arido","árido","semiarido","semiárido"],["sobre otra","sobre otra planta","sobre"]],
 {"incompleto":"Pastos. Calor.","solo":"El monte es árido, tiene jarilla y algarrobos y vive el puma.","carpeta":["Pastizal.","Selva.","Árido.","Sobre otra."]})
A3=NV("Vas a describir los ambientes de montaña y de mar y cómo viven allí plantas y animales.",["Montaña","Estepa y bosque andino","Mar","Adaptaciones"],[
 S(1,"Montaña",[PN("En los Andes argentinos, la vida cambia con la altura: a mucha altura hay pastos duros y pocos árboles; en la Puna viven la vicuña, la llama y el cóndor andino.","En las montañas, la vida cambia con la altura: a mucha altura hay pastos duros y pocos árboles. Allí viven camélidos andinos y grandes aves.")]),
 S(1,"Estepa y bosque",[PN("En la Patagonia hay estepa, con arbustos bajos y viento constante, y en la cordillera, el bosque andino-patagónico, con lengas, ñires y cipreses. El guanaco y el choique viven en la estepa.","En el extremo sur de Sudamérica hay estepa, con arbustos bajos y viento constante, y en la cordillera bosques de árboles resistentes al frío. En la estepa viven camélidos y aves corredoras.")]),
 S(2,"Mar",[PN("El Mar Argentino es frío y rico en plancton. Allí viven la ballena franca austral (en Península Valdés), el lobo marino, el pingüino de Magallanes y muchos peces.","Los mares fríos son ricos en plancton. Allí viven ballenas, lobos marinos, pingüinos y muchos peces.")]),
 S(2,"Adaptaciones",[T("Para sobrevivir",["Ambiente","Adaptación"],[["Altura","Pulmones y sangre que aprovechan poco oxígeno"],["Estepa","Arbustos bajos que resisten el viento"],["Mar frío","Capa de grasa que abriga"]])])],
 {"titulo":"relacionar","planteo":"¿Por qué los animales de mar frío tienen una capa de grasa?","pasos":["El agua fría quita calor al cuerpo.","La grasa aísla del frío.","Así mantienen la temperatura."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los pequeños organismos que flotan y alimentan al mar son el ___ .","En las alturas, la vida cambia con la ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un animal de montaña o de mar y explicá cómo se adapta."},
 {"titulo":"Abrigo y viento","texto":"En lugares fríos y ventosos, los seres vivos son bajos y resistentes."},
 ["Pensar que el mar frío tiene poca vida.","Creer que la altura no cambia la vegetación."],
 RS(("Montaña","La vida cambia con la altura."),("Estepa","Arbustos bajos."),("Mar","Plancton."),("Adaptación","Grasa, viento.")),
 G(("Plancton","Seres muy pequeños que flotan en el agua."),("Estepa","Llanura de arbustos bajos."),("Camélido","Mamífero andino como la llama."),("Adaptación","Rasgo que ayuda a sobrevivir.")),
 ["¿Cómo se llaman los seres diminutos que flotan en el mar y alimentan a otros?","¿La vegetación de montaña cambia con la altura? Respondé sí o no.","¿Qué ambiente tiene arbustos bajos y viento constante?","¿Qué abriga a los animales del mar frío: una capa de grasa o plumas largas?"],
 [["plancton","el plancton"],["si","sí"],["estepa","la estepa"],["capa de grasa","grasa","una capa de grasa"]],
 {"incompleto":"Plancton. Altura.","solo":"El lobo marino tiene grasa que lo abriga en el agua fría.","carpeta":["Plancton.","Sí.","Estepa.","Capa de grasa."]})
A4=NV("Vas a explicar por qué algunas ecorregiones están en riesgo, qué las amenaza y cómo se pueden proteger.",["Amenazas","Especies en peligro","Áreas protegidas","Qué podemos hacer"],[
 S(1,"Amenazas",[T("Qué las daña",["Amenaza","Cómo daña"],[["Desmonte","Se talan bosques para sembrar o criar animales"],["Incendios","Destruyen la vegetación y el hábitat"],["Sobrepesca","Se saca más de lo que el mar repone"],["Contaminación","Envenena agua y suelo"],["Especies invasoras","Compiten con las nativas"]])]),
 S(1,"Especies en peligro",[PN("En la Argentina están en peligro el yaguareté, el huemul y el venado de las pampas. Cuando se pierde su hábitat, no tienen dónde vivir.","Muchos grandes mamíferos están en peligro, como el yaguareté y el huemul. Cuando se pierde su hábitat, no tienen dónde vivir.")]),
 S(2,"Áreas protegidas",[PN("Los parques nacionales y las reservas protegen ambientes y especies. En la Argentina hay parques como Iguazú, Los Glaciares y Nahuel Huapi.","Los parques nacionales y las reservas protegen ambientes y especies, y permiten visitas controladas y estudios científicos.")]),
 S(2,"Qué podemos hacer",[T("Acciones",["Quién","Qué hace"],[["Estado","Leyes y control"],["Comunidades","Cuidan su ambiente"],["Escuelas","Educación ambiental"],["Cada persona","Consumo responsable y no dejar residuos"]])])],
 {"titulo":"relacionar","planteo":"¿Por qué el desmonte pone en peligro a un animal?","pasos":["Pierde el bosque donde vive y se alimenta.","Se reduce su territorio.","Con menos espacio, su población baja."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Talar bosques para sembrar es el ___ .","Los lugares que se cuidan por ley son las áreas ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una amenaza y proponé dos acciones para reducirla."},
 {"titulo":"Hábitat","texto":"Proteger a una especie empieza por proteger su hogar."},
 ["Pensar que proteger es no usar nunca nada.","Creer que cuidar depende solo del Estado."],
 RS(("Amenazas","Desmonte, incendios, sobrepesca."),("Peligro","Sin hábitat."),("Áreas protegidas","Parques y reservas."),("Acciones","Entre todos.")),
 G(("Desmonte","Tala de bosques."),("Hábitat","Lugar donde vive una especie."),("Especie invasora","Especie que llega de otro lugar y daña.")),
 ["¿Cómo se llama talar un bosque para otros usos?","¿Cómo se llama el lugar donde vive una especie?","¿Los parques nacionales protegen ambientes? Respondé sí o no.","¿Quién puede cuidar el ambiente: solo el Estado o todos?"],
 [["desmonte","el desmonte"],["habitat","hábitat","el habitat","el hábitat"],["si","sí"],["todos","todas las personas"]],
 {"incompleto":"Desmonte. Protegidas.","solo":"Amenaza: incendios. Acciones: no hacer fuego en el campo y avisar a los bomberos.","carpeta":["Desmonte.","Hábitat.","Sí.","Todos."]})
ACT6={"1":[FB("Las ecorregiones se explican por el ___ y el relieve.",[["clima"]],"El clima decide la vida.",neutro={"p":"Las ecorregiones se explican por el ___ y el relieve."}),MS("¿Qué factores influyen en el clima?",["Latitud","Altitud","Cercanía al mar","El color del suelo"],["Latitud","Altitud","Cercanía al mar"],"El color del suelo no decide el clima.")],
 "2":[{"t":"classify","p":"¿Qué ambiente es?","o":{"elementos":["Pastos y suelo fértil","Arbustos y poca lluvia","Árboles altos y lianas","Llanura templada"],"categorias":["Pastizal","Monte","Selva"]},"r":{"categorias":{"Pastos y suelo fértil":"Pastizal","Arbustos y poca lluvia":"Monte","Árboles altos y lianas":"Selva","Llanura templada":"Pastizal"}},"e":"La vegetación depende de la lluvia."},TT("Tocá las palabras que describen la selva: «La selva es cálida, muy lluviosa y tiene árboles altos».",["La","selva","es","cálida,","muy","lluviosa","y","tiene","árboles","altos"],[3,5,8,9],"Cálida, lluviosa y árboles altos.")],
 "3":[{"t":"matching","p":"Uní cada ambiente con su rasgo.","o":{"izquierda":["Estepa","Mar frío","Montaña alta","Bosque de montaña"],"derecha":["Arbustos bajos y viento","Plancton y grasa","Poco oxígeno","Árboles resistentes al frío"]},"r":{"pares":{"Estepa":"Arbustos bajos y viento","Mar frío":"Plancton y grasa","Montaña alta":"Poco oxígeno","Bosque de montaña":"Árboles resistentes al frío"}},"e":"Cada ambiente tiene su rasgo."},VF("La vegetación de montaña no cambia con la altura.","Falso","Cambia a medida que se sube.")],
 "4":[MS("¿Qué amenaza a las ecorregiones?",["Desmonte","Incendios","Sobrepesca","Plantar árboles nativos"],["Desmonte","Incendios","Sobrepesca"],"Plantar árboles nativos ayuda."),{"t":"ordering","p":"Ordená: del problema a la solución.","o":["Se crea un parque","Se pierde el bosque","La especie se recupera"],"r":{"orden":["Se pierde el bosque","Se crea un parque","La especie se recupera"]},"e":"Amenaza, protección y recuperación."}],
 "5":[MC("Relámpago. El clima con muy pocas lluvias es…",["Árido","Selvático","Polar"],"Árido","Pocas lluvias.",tiempo=20),VF("Relámpago. La selva es cálida y lluviosa.","Verdadero","Mucha agua.",tiempo=20),MC("Relámpago. Seres diminutos que flotan en el mar:",["Plancton","Epífitas","Líquenes"],"Plancton","Base alimentaria.",tiempo=20),VF("Relámpago. El desmonte protege el hábitat.","Falso","Lo destruye.",tiempo=20)]}
EX6=[[1,MC("Una ecorregión es…",["Un área con clima, relieve y vida característicos","Un país","Un río","Un animal"],"Un área con clima, relieve y vida característicos","Se explica por el clima.")],
 [1,MC("Cuanto más alto, el clima es…",["Más frío","Más cálido","Igual","Más húmedo"],"Más frío","La altitud enfría.")],
 [1,VF("Un país extenso puede tener muchos climas.","Verdadero","Latitud y relieve cambian.")],
 [2,MC("¿Qué ambiente tiene suelos fértiles y pastos?",["Pastizal","Selva","Estepa","Mar"],"Pastizal","Llanura templada.")],
 [2,MC("¿Qué ambiente tiene mucha lluvia y calor?",["Selva","Monte","Estepa","Pastizal"],"Selva","Árboles altos.")],
 [2,FB("En el monte predominan los ___ .",[["arbustos"]],"Clima árido.")],
 [3,MC("¿Qué son los seres diminutos que flotan en el mar?",["Plancton","Corales","Líquenes","Algas rojas"],"Plancton","Base de la cadena.")],
 [3,MC("Una capa de grasa ayuda a…",["Abrigar del frío","Volar","Correr","Ver mejor"],"Abrigar del frío","Aísla el cuerpo.")],
 [3,VF("La estepa tiene árboles muy altos.","Falso","Tiene arbustos bajos.")],
 [4,MC("Talar bosques para otros usos es…",["Desmonte","Reforestación","Fotosíntesis","Erosión"],"Desmonte","Destruye el hábitat.")],
 [4,MS("Acciones para proteger:",["Crear áreas protegidas","Educación ambiental","Quemar pastizales","Control de la caza"],["Crear áreas protegidas","Educación ambiental","Control de la caza"],"Quemar no protege.")],
 [4,FB("El lugar donde vive una especie es su ___ .",[["habitat","hábitat"]],"Su hogar natural.")],
 [4,VF("Cuidar el ambiente depende solo del Estado.","Falso","Depende de todos.")]]
M6={"subject_id":SID,"tema":6,"practica":"Práctica general: ecosistemas argentinos","examen_titulo":"Nivel jefe: ecosistemas argentinos","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT6,"examen":EX6}

# ================= MISIÓN 7: RELACIONES EN EL ECOSISTEMA =================
B1=NV("Vas a distinguir competencia y depredación y explicar cómo cada una regula las poblaciones.",["Competencia","Depredación","Adaptaciones","Equilibrio"],[
 S(1,"Competencia",[D("Competencia","Relación en la que los seres vivos luchan por un mismo recurso limitado: alimento, agua, luz, espacio o pareja."),T("Dos tipos",["Tipo","Ejemplo"],[["Intraespecífica (misma especie)","Dos leones disputan un territorio"],["Interespecífica (distintas especies)","Cebras y ñus comen los mismos pastos"]])]),
 S(1,"Depredación",[D("Depredación","Relación en la que un animal (depredador) caza y se alimenta de otro (presa)."),P("Ejemplo: el puma caza al guanaco; el águila caza roedores.")]),
 S(2,"Adaptaciones",[T("Cómo se defienden",["Presa","Depredador"],[["Camuflaje, velocidad, veneno","Garras, colmillos, vista aguda"],["Moverse en grupo","Cazar en manada"]])]),
 S(2,"Equilibrio",[P("La depredación y la competencia <b>regulan</b> las poblaciones: si hay demasiadas presas, los depredadores aumentan y las reducen; si bajan las presas, los depredadores disminuyen.")])],
 {"titulo":"identificar","planteo":"Dos arbustos crecen juntos y se quitan la luz. ¿Qué relación es?","pasos":["Disputan un recurso: la luz.","Es una competencia.","Si son de la misma especie, intraespecífica."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El animal que caza a otro es el ___ .","El animal cazado es la ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un ejemplo de competencia y uno de depredación que hayas visto o leído."},
 {"titulo":"Recurso o alimento","texto":"Preguntate: ¿se pelean por lo mismo (competencia) o uno se come al otro (depredación)?"},
 ["Pensar que el depredador siempre es malo para el ecosistema.","Confundir competencia con depredación."],
 RS(("Competencia","Mismo recurso."),("Tipos","Intra e interespecífica."),("Depredación","Cazar y comer."),("Equilibrio","Regulan poblaciones.")),
 G(("Competencia","Disputa por un recurso."),("Depredador","Animal que caza."),("Presa","Animal cazado."),("Población","Conjunto de individuos de una especie.")),
 ["¿Cómo se llama el animal cazado?","¿Cómo se llama el animal que caza?","Dos leones que disputan territorio, ¿es competencia intraespecífica o interespecífica?","¿La depredación ayuda a regular las poblaciones? Respondé sí o no."],
 [["presa","la presa"],["depredador","el depredador"],["intraespecifica","intraespecífica","es intraespecifica","es intraespecífica"],["si","sí"]],
 {"incompleto":"Depredador. Presa.","solo":"Competencia: dos plantas por luz. Depredación: el águila y el ratón.","carpeta":["Presa.","Depredador.","Intraespecífica.","Sí."]})
B2=NV("Vas a reconocer el mutualismo y el comensalismo y distinguirlos por quién gana, quién pierde y quién no se ve afectado.",["Relaciones de ayuda","Mutualismo","Comensalismo","Comparar"],[
 S(1,"Relaciones de ayuda",[D("Simbiosis","Relación estrecha y duradera entre individuos de especies distintas."),P("Hay simbiosis en que <b>ambos ganan</b> (mutualismo) y otras en que <b>uno gana y el otro no se afecta</b> (comensalismo).")]),
 S(1,"Mutualismo",[T("Ambos se benefician",["Ejemplo","Qué gana cada uno"],[["Abeja y flor","La abeja obtiene néctar; la flor se poliniza"],["Hongo y alga (liquen)","El hongo da protección; el alga hace fotosíntesis"],["Hormiga y acacia","La acacia da refugio; la hormiga la defiende"]])]),
 S(2,"Comensalismo",[D("Comensalismo","Relación en la que una especie se beneficia y la otra no gana ni pierde."),T("Ejemplos",["Ejemplo","Qué pasa"],[["Rémora y tiburón","La rémora come restos del tiburón; este no se ve afectado"],["Garcilla bueyera y vaca","La garcilla caza insectos que la vaca levanta al caminar"],["Epífita y árbol","La planta crece sobre el árbol sin dañarlo"]])]),
 S(2,"Comparar",[T("Quién gana",["Relación","Especie A","Especie B"],[["Mutualismo","Gana","Gana"],["Comensalismo","Gana","Ni gana ni pierde"],["Parasitismo","Gana","Pierde"]])])],
 {"titulo":"clasificar","planteo":"Una orquídea crece sobre un árbol sin dañarlo. ¿Qué relación es?","pasos":["La orquídea gana lugar y luz.","El árbol no gana ni pierde.","Es comensalismo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cuando ambos ganan, la relación es ___ .","Cuando uno gana y el otro no se afecta, es ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un ejemplo de mutualismo y uno de comensalismo y explicá quién gana."},
 {"titulo":"Mirá a los dos","texto":"Para clasificar una relación, anotá qué le pasa a cada especie: gana, pierde o nada."},
 ["Creer que una relación de ayuda siempre favorece a ambos.","Confundir comensalismo con parasitismo."],
 RS(("Simbiosis","Relación estrecha."),("Mutualismo","Ambos ganan."),("Comensalismo","Uno gana."),("Parasitismo","Uno pierde.")),
 G(("Mutualismo","Ambos se benefician."),("Comensalismo","Uno gana y el otro no se afecta."),("Simbiosis","Relación estrecha entre especies."),("Polinizar","Llevar polen de una flor a otra.")),
 ["¿Cómo se llama la relación en que ambos ganan?","¿Cómo se llama la relación en que uno gana y el otro no se afecta?","¿Abeja y flor es mutualismo o comensalismo?","¿Un liquen es la unión de un hongo y un alga? Respondé sí o no."],
 [["mutualismo","el mutualismo"],["comensalismo","el comensalismo"],["mutualismo","es mutualismo"],["si","sí"]],
 {"incompleto":"Mutualismo. Comensalismo.","solo":"Mutualismo: abeja y flor, ambas ganan. Comensalismo: rémora y tiburón, la rémora gana.","carpeta":["Mutualismo.","Comensalismo.","Mutualismo.","Sí."]})
B3=NV("Vas a reconocer el parasitismo, sus tipos y cómo se diferencia de la depredación.",["Parásito y hospedador","Tipos de parásitos","Parasitismo y depredación","Prevención"],[
 S(1,"Parásito y hospedador",[D("Parasitismo","Relación en la que un ser vivo (parásito) se alimenta de otro (hospedador) y lo perjudica, pero casi nunca lo mata enseguida."),P("Al parásito le conviene que su hospedador siga vivo.")]),
 S(1,"Tipos",[T("Dónde viven",["Tipo","Dónde","Ejemplo"],[["Ectoparásito","Fuera del cuerpo","Pulga, garrapata, piojo"],["Endoparásito","Dentro del cuerpo","Tenia, lombriz intestinal"]])]),
 S(2,"Parásito y depredador",[T("Diferencias",["","Parasitismo","Depredación"],[["Qué hace","Se alimenta sin matar enseguida","Mata para comer"],["Tamaño","El parásito es más chico","El depredador suele ser más grande"],["Duración","Larga","Corta"]])]),
 S(2,"Prevención",[P("Para evitar parásitos en las personas y las mascotas se usa <b>higiene</b>, agua segura, cocción de los alimentos, desparasitación y consulta al veterinario o médico.")])],
 {"titulo":"clasificar","planteo":"Una garrapata se alimenta de la sangre de un perro. ¿Qué es cada uno?","pasos":["La garrapata se alimenta y perjudica: parásito (ectoparásito).","El perro es el hospedador.","Es parasitismo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El ser vivo que se alimenta de otro y lo perjudica es el ___ .","El que lo alberga es el ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres medidas para prevenir parásitos."},
 {"titulo":"No lo mata","texto":"Si lo mata enseguida es depredación; si lo perjudica de a poco, es parasitismo."},
 ["Pensar que todo parásito mata rápido.","Confundir parásito con depredador."],
 RS(("Parasitismo","Uno vive a costa del otro."),("Tipos","Ecto y endoparásito."),("Diferencia","No mata enseguida."),("Prevención","Higiene.")),
 G(("Parásito","Ser vivo que se alimenta de otro."),("Hospedador","Ser vivo que alberga al parásito."),("Ectoparásito","Parásito externo."),("Endoparásito","Parásito interno.")),
 ["¿Cómo se llama el ser vivo que se alimenta de otro y lo perjudica?","¿Cómo se llama el ser vivo que lo alberga?","Una pulga, ¿es ectoparásito o endoparásito?","La tenia, ¿es ectoparásito o endoparásito?"],
 [["parasito","parásito","el parasito","el parásito"],["hospedador","el hospedador"],["ectoparasito","ectoparásito","es ectoparasito","es ectoparásito"],["endoparasito","endoparásito","es endoparasito","es endoparásito"]],
 {"incompleto":"Parásito. Hospedador.","solo":"Higiene, agua segura y desparasitar a las mascotas.","carpeta":["Parásito.","Hospedador.","Ectoparásito.","Endoparásito."]})
B4=NV("Vas a explicar cómo las relaciones forman redes y qué ocurre en el ecosistema cuando una de ellas cambia.",["Una trama de relaciones","Redes tróficas","Efectos en cadena","Cuidar el equilibrio"],[
 S(1,"Una trama de relaciones",[P("Una especie rara vez tiene una sola relación: compite, es presa, es parasitada y a veces ayuda a otras. Todas esas relaciones forman una <b>red de interacciones</b>.")]),
 S(1,"Redes tróficas",[D("Red trófica","Conjunto de cadenas alimentarias conectadas entre sí en un ecosistema."),P("Si desaparece un eslabón, las demás especies se ven afectadas.")]),
 S(2,"Efectos en cadena",[T("Un ejemplo",["Cambio","Efecto"],[["Desaparecen los depredadores","Crecen las presas"],["Hay demasiadas presas","Comen toda la vegetación"],["Falta vegetación","Pierden alimento otros animales"]])]),
 S(2,"Cuidar el equilibrio",[P("Un ecosistema en equilibrio mantiene sus poblaciones estables. Las <b>especies invasoras</b> o la pérdida de una especie clave pueden desequilibrarlo. Por eso importa proteger todas las relaciones, no solo algunas especies.")])],
 {"titulo":"predecir","planteo":"Si desaparecen los zorros de un campo, ¿qué puede pasar?","pasos":["Hay menos depredadores de roedores.","Los roedores aumentan.","Comen más plantas y bajan los recursos de otros animales."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las cadenas alimentarias conectadas forman una red ___ .","Una especie que llega de otro lugar y daña es una especie ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá una red con cinco seres vivos y marcá tres relaciones distintas."},
 {"titulo":"Todo está conectado","texto":"Cuando cambia un eslabón, buscá a quién afecta después."},
 ["Pensar que sacar una especie no afecta a las demás.","Creer que el equilibrio es estático."],
 RS(("Red","Muchas relaciones."),("Red trófica","Cadenas conectadas."),("Efecto en cadena","Un cambio afecta a otros."),("Equilibrio","Poblaciones estables.")),
 G(("Red trófica","Cadenas alimentarias conectadas."),("Equilibrio","Estabilidad de las poblaciones."),("Especie clave","Especie de la que dependen muchas otras.")),
 ["¿Cómo se llama el conjunto de cadenas alimentarias conectadas?","¿Qué pasa con las presas si desaparecen sus depredadores: aumentan o disminuyen?","¿Quitar una especie afecta a las demás? Respondé sí o no.","¿Una especie que llega de otro lugar y daña es invasora o nativa?"],
 [["red trofica","red trófica","la red trofica","la red trófica"],["aumentan","aumenta","crecen"],["si","sí"],["invasora","es invasora"]],
 {"incompleto":"Trófica. Invasora.","solo":"Sin zorros aumentan los roedores y comen más plantas.","carpeta":["Red trófica.","Aumentan.","Sí.","Invasora."]})
ACT7={"1":[{"t":"classify","p":"¿Competencia o depredación?","o":{"elementos":["Dos plantas por luz","El puma caza un guanaco","Dos aves por el nido","El águila caza un ratón"],"categorias":["Competencia","Depredación"]},"r":{"categorias":{"Dos plantas por luz":"Competencia","El puma caza un guanaco":"Depredación","Dos aves por el nido":"Competencia","El águila caza un ratón":"Depredación"}},"e":"Recurso o alimento."},FB("El animal que caza a otro es el ___ .",[["depredador"]],"Caza a la presa.")],
 "2":[{"t":"matching","p":"Uní cada ejemplo con su relación.","o":{"izquierda":["Abeja y flor","Rémora y tiburón","Hongo y alga","Epífita y árbol"],"derecha":["Mutualismo","Comensalismo","Mutualismo","Comensalismo"]},"r":{"pares":{"Abeja y flor":"Mutualismo","Rémora y tiburón":"Comensalismo","Hongo y alga":"Mutualismo","Epífita y árbol":"Comensalismo"}},"e":"Quién gana y quién no se afecta."},TT("Tocá la especie que no se afecta: «La rémora come restos del tiburón y el tiburón no se ve afectado».",["La","rémora","come","restos","del","tiburón","y","el","tiburón","no","se","ve","afectado"],[7,8],"El tiburón ni gana ni pierde.")],
 "3":[MS("¿Cuáles son ectoparásitos?",["Pulga","Garrapata","Tenia","Piojo"],["Pulga","Garrapata","Piojo"],"La tenia vive dentro."),VF("Un parásito suele matar enseguida a su hospedador.","Falso","Le conviene que siga vivo.")],
 "4":[{"t":"ordering","p":"Ordená el efecto en cadena.","o":["Los roedores comen más plantas","Desaparecen los zorros","Aumentan los roedores"],"r":{"orden":["Desaparecen los zorros","Aumentan los roedores","Los roedores comen más plantas"]},"e":"Cada cambio produce el siguiente."},MC("Una red trófica es…",["Cadenas alimentarias conectadas","Una cadena sola","Un tipo de parásito","Una planta"],"Cadenas alimentarias conectadas","Muchas relaciones.")],
 "5":[MC("Relámpago. Ambos ganan en el…",["Mutualismo","Parasitismo","Depredación"],"Mutualismo","Los dos se benefician.",tiempo=20),VF("Relámpago. La garrapata es un ectoparásito.","Verdadero","Vive fuera.",tiempo=20),MC("Relámpago. El animal cazado es la…",["Presa","Parásito","Planta"],"Presa","Lo caza el depredador.",tiempo=20),VF("Relámpago. Quitar una especie no afecta a otras.","Falso","Hay efecto en cadena.",tiempo=20)]}
EX7=[[1,MC("La competencia es una relación…",["Por un recurso limitado","De ayuda mutua","De caza","De parásitos"],"Por un recurso limitado","Luz, agua, alimento o espacio.")],
 [1,MC("El animal cazado es…",["La presa","El depredador","El parásito","El hospedador"],"La presa","La caza el depredador.")],
 [1,VF("La depredación ayuda a regular las poblaciones.","Verdadero","Mantiene el equilibrio.")],
 [2,MC("Si ambos se benefician, es…",["Mutualismo","Comensalismo","Parasitismo","Competencia"],"Mutualismo","Ambos ganan.")],
 [2,MC("Rémora y tiburón es un ejemplo de…",["Comensalismo","Mutualismo","Parasitismo","Depredación"],"Comensalismo","La rémora gana; el tiburón no se afecta.")],
 [2,VF("Un liquen es la unión de un hongo y un alga.","Verdadero","Ambos se benefician.")],
 [3,MC("El ser vivo que alberga al parásito es el…",["Hospedador","Depredador","Competidor","Productor"],"Hospedador","Es perjudicado.")],
 [3,MC("La tenia es un…",["Endoparásito","Ectoparásito","Depredador","Productor"],"Endoparásito","Vive dentro.")],
 [3,VF("Un parásito suele matar enseguida a su hospedador.","Falso","Le conviene que siga vivo.")],
 [4,MC("Una red trófica es…",["Cadenas alimentarias conectadas","Un tipo de planta","Un río","Un depredador"],"Cadenas alimentarias conectadas","Muchas relaciones.")],
 [4,MC("Si desaparecen los depredadores, las presas…",["Aumentan","Desaparecen","No cambian","Se vuelven parásitos"],"Aumentan","Hay menos control.")],
 [4,MS("Efectos de un desequilibrio:",["Una población crece de más","Se pierde vegetación","Otros animales pierden alimento","Todo sigue igual"],["Una población crece de más","Se pierde vegetación","Otros animales pierden alimento"],"No todo sigue igual.")],
 [4,VF("Una especie invasora puede desequilibrar un ecosistema.","Verdadero","Compite con las nativas.")]]
M7={"subject_id":SID,"tema":7,"practica":"Práctica general: relaciones en el ecosistema","examen_titulo":"Nivel jefe: relaciones en el ecosistema","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT7,"examen":EX7}
for n,m in ((6,M6),(7,M7)):
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
STEPS={(6,1):"dd3e77f8-2905-42a1-8c53-30863bcefdf1",(6,2):"378d6b2d-2678-439f-adc8-935dd1961f9f",(6,3):"a6caf0fb-d900-405e-a4e9-13a8fec47f57",(6,4):"5252ebe1-d6a9-42b9-9097-194b1ee94ba9",(7,1):"238823cb-e109-46fd-ad59-c2a535a61cd9",(7,2):"210dfc69-9354-470d-bd0b-a25d51871286",(7,3):"ae9b96d5-9e1f-412d-b27a-cc8df31b01de",(7,4):"9eeb21c2-a038-4fe4-ab5d-e3148dff9945"}
TIT={(6,1):"Regiones y clima",(6,2):"Pastizal, monte y selva",(6,3):"Ambientes de montaña y de mar",(6,4):"Ecorregiones en riesgo",(7,1):"Competencia y depredación",(7,2):"Mutualismo y comensalismo",(7,3):"Parasitismo",(7,4):"Redes de interacciones"}
def NEU(e,**k): e=dict(e); e["neutro"]=k; return e
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
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
CLS={(6,1):[
 NEU({"t":"gancho","grande":"Muchos climas","emoji":"🌎","final":"en un solo país","titulo":"REGIONES Y CLIMA","sub":"ecorregiones argentinas","voz":["Un país muy largo tiene selvas, desiertos, montañas y mar.","Todos esos ambientes dependen del clima.","Hoy: *regiones y clima* de la Argentina."]},sub="ecorregiones de un país extenso",voz=["Un país muy extenso tiene selvas, desiertos, montañas y mar.","Todos esos ambientes dependen del clima.","Hoy: *regiones y clima* de un país extenso."]),
 DEF("Ecorregión","Área con clima, relieve y vida característicos","🗺️",["Una *ecorregión* es una gran área con clima, relieve y vida característicos.","Cada una tiene sus plantas y animales."]),
 TB("FACTORES DEL CLIMA",["Factor","Cómo influye"],[["Latitud","Más cerca del ecuador, más calor"],["Altitud","Más alto, más frío"],["Mar","Suaviza el clima"],["Vientos","Traen humedad o aire seco"]],["Cuatro factores.","La *latitud*: cerca del ecuador hace más calor.","La *altitud*: cuanto más alto, más frío.","El *mar* suaviza el clima.","Y los *vientos* traen humedad o aire seco."]),
 CL([("CÁLIDO LLUVIOSO","🌧️"),("ÁRIDO","🏜️"),("FRÍO","❄️")],[("Selva",0),("Desierto",1),("Estepa fría",2)],["¿Qué clima?","*Selva*: cálido y lluvioso.","*Desierto*: árido.","*Estepa fría*: frío."]),
 CAU(("Clima y vida",'🌿'),[("Mucha lluvia: selva","🌳"),("Poca lluvia: arbustos","🌵"),("Lluvia moderada: pastos","🌾")],["El clima decide la vida.","Con *mucha lluvia*: selva.","Con *poca lluvia*: arbustos.","Con *lluvia moderada*: pastizal."]),
 Q("¿Qué factor enfría un lugar cuanto más alto está?",["Altitud","Latitud","Mar"],0,["Te toca: ¿qué factor enfría cuanto más alto?","¿Altitud, latitud o mar?","La *altitud*."]),
 ER([("Todo el país tiene el mismo clima","Hay muchos climas"),("La altura no influye","La altura enfría")],["Errores típicos.","Pensar que hay *un solo clima*.","Y olvidar que la *altura* enfría."]),
 RES(["Repasemos.","Una *ecorregión* tiene clima, relieve y vida propios.","Influyen *latitud*, *altitud*, *mar* y *vientos*.","El *clima* decide la vegetación.","Y un país extenso tiene *muchos ambientes*.","¡Clase terminada! Ahora, *a practicar*."],[["ECORREGIÓN","clima y vida"],["FACTORES","cuatro"],["CLIMA","decide la vida"],["PAÍS","muchos ambientes"]])],
(6,2):[
 {"t":"reto","texto":"¿Qué ambiente tiene mucha lluvia, calor y árboles altos?","segundos":6,"respuesta":"La selva","emoji":"🌳","titulo":"PASTIZAL, MONTE Y SELVA","sub":"tres ambientes","voz":["Desafío: ¿qué ambiente tiene mucha lluvia, calor y árboles altos? Seis segundos.","La selva.","Hoy: *pastizal*, *monte* y *selva*."]},
 NEU(DEF("Pastizal pampeano","Llanura templada de suelos fértiles","🌾",["El *pastizal pampeano* es una llanura templada de suelos muy fértiles.","Viven el ñandú y la vizcacha."]),palabra="Pastizal",texto="Llanura templada de suelos fértiles",voz=["El *pastizal* es una llanura templada de suelos muy fértiles.","Viven aves corredoras y roedores."]),
 TB("TRES AMBIENTES",["Ambiente","Clima","Vegetación"],[["Pastizal","Templado","Pastos"],["Monte","Árido","Arbustos"],["Selva","Cálido y lluvioso","Árboles altos"]],["Compará los tres.","*Pastizal*: templado, pastos.","*Monte*: árido, arbustos.","*Selva*: cálido y lluvioso, árboles altos."]),
 CL([("PASTIZAL","🌾"),("MONTE","🌵"),("SELVA","🌳")],[("Pastos",0),("Arbustos",1),("Lianas",2)],["¿Qué ambiente?","*Pastos*: pastizal.","*Arbustos*: monte.","*Lianas*: selva."]),
 NEU(DEF("Yungas y Misiones","Selvas del noroeste y del noreste","🐆",["Las *Yungas* y la selva *misionera* son selvas argentinas.","Viven el yaguareté y el tucán."]),palabra="Selvas",texto="Mucha lluvia, calor y gran diversidad",voz=["Las *selvas* tienen mucha lluvia y calor.","Viven grandes felinos y tucanes."]),
 Q("¿Qué ambiente tiene arbustos y poca lluvia?",["Monte","Selva","Pastizal"],0,["Te toca: ¿qué ambiente tiene arbustos y poca lluvia?","¿Monte, selva o pastizal?","El *monte*."]),
 ER([("El monte no tiene vida","Tiene plantas y animales adaptados"),("Pastizal igual a estepa","Son ambientes distintos")],["Errores típicos.","Creer que el *monte* no tiene vida.","Y confundir *pastizal* con estepa."]),
 RES(["Repasemos.","El *pastizal* tiene pastos.","El *monte* es árido y de arbustos.","La *selva* es cálida y lluviosa.","Y la *lluvia* explica el paisaje.","¡Clase terminada! Ahora, *a practicar*."],[["PASTIZAL","pastos"],["MONTE","arbustos"],["SELVA","árboles altos"],["CLAVE","la lluvia"]])],
(6,3):[
 {"t":"gancho","grande":"4.000 m","emoji":"🏔️","final":"y la vida cambia con la altura","titulo":"MONTAÑA Y MAR","sub":"ambientes extremos","voz":["A cuatro mil metros de altura el aire casi no tiene oxígeno.","Y aun así hay vida.","Hoy: *ambientes de montaña y de mar*."]},
 NEU(DEF("Puna y estepa","Ambientes fríos y ventosos de altura y del sur","🌬️",["La *Puna* es una montaña muy alta y seca.","La *estepa* patagónica tiene arbustos bajos y viento."]),palabra="Montaña y estepa",texto="Ambientes fríos y ventosos",voz=["En las *montañas altas* hay poco oxígeno y mucho frío.","La *estepa* tiene arbustos bajos y viento."]),
 CAU(("Adaptaciones",'🧬'),[("Altura: poco oxígeno","🏔️"),("Estepa: viento","🌬️"),("Mar frío: grasa","🐧")],["Cada ambiente exige algo.","En la *altura*: pulmones eficientes.","En la *estepa*: plantas bajas.","En el *mar frío*: capa de grasa."]),
 NEU(TB("MAR FRÍO",["Animal","Rasgo"],[["Ballena franca","Se alimenta de plancton"],["Lobo marino","Grasa que abriga"],["Pingüino","Plumas impermeables"]],["Animales del mar argentino.","La *ballena franca* come plancton.","El *lobo marino* tiene grasa.","El *pingüino*, plumas impermeables."]),titulo="MAR FRÍO",voz=["Animales de los mares fríos.","Las *ballenas* comen plancton.","El *lobo marino* tiene grasa.","El *pingüino*, plumas impermeables."]),
 DEF("Plancton","Seres diminutos que flotan en el agua","🔬",["El *plancton* son seres diminutos que flotan en el agua.","Alimenta a muchos animales marinos."]),
 Q("¿Qué abriga a los animales del mar frío?",["Una capa de grasa","Plumas largas","Pelo largo"],0,["Te toca: ¿qué abriga a los animales del mar frío?","¿Una capa de grasa, plumas largas o pelo largo?","Una *capa de grasa*."]),
 ER([("El mar frío tiene poca vida","Es rico en plancton"),("La altura no cambia la vegetación","Sí la cambia")],["Errores típicos.","Creer que el mar frío *tiene poca vida*.","Y pensar que la *altura* no cambia la vegetación."]),
 RES(["Repasemos.","En la *montaña*, la vida cambia con la altura.","La *estepa* tiene arbustos bajos.","El *mar frío* es rico en plancton.","Y cada ambiente exige *adaptaciones*.","¡Clase terminada! Ahora, *a practicar*."],[["MONTAÑA","la altura cambia todo"],["ESTEPA","arbustos bajos"],["MAR","plancton"],["ADAPTACIÓN","grasa y viento"]])],
(6,4):[
 {"t":"noticia","cinta":"ALERTA","titular":"Un gran felino pierde su selva","bajada":"Cada año hay menos bosque","emoji":"🚨","titulo":"ECORREGIONES EN RIESGO","sub":"amenazas y cuidado","voz":["Alerta: un gran felino pierde su selva.","Cada año hay menos bosque.","Hoy: *ecorregiones en riesgo*."]},
 TB("AMENAZAS",["Amenaza","Daño"],[["Desmonte","Se tala el bosque"],["Incendios","Se quema el hábitat"],["Sobrepesca","Se pesca de más"],["Invasoras","Compiten con las nativas"]],["Las amenazas.","El *desmonte*: se tala el bosque.","Los *incendios*: se quema el hábitat.","La *sobrepesca*: se pesca de más.","Y las *invasoras*: compiten con las nativas."]),
 DEF("Hábitat","Lugar donde vive una especie","🏠",["El *hábitat* es el lugar donde vive una especie.","Si se destruye, la especie queda en peligro."]),
 NEU(DEF("Áreas protegidas","Parques nacionales y reservas","🌲",["Los *parques nacionales* y las *reservas* protegen ambientes y especies.","Como Iguazú y Los Glaciares en la Argentina."]),texto="Parques nacionales y reservas",voz=["Los *parques nacionales* y las *reservas* protegen ambientes y especies.","Permiten visitas controladas y estudios científicos."]),
 CL([("AYUDA","✅"),("DAÑA","🚫")],[("Parque nacional",0),("Desmonte",1),("Educación ambiental",0),("Incendio",1)],["¿Ayuda o daña?","*Parque nacional* y *educación ambiental*: ayudan.","*Desmonte* e *incendio*: dañan."]),
 Q("Talar un bosque para otros usos se llama…",["Desmonte","Reforestación","Erosión"],0,["Te toca: talar un bosque para otros usos.","¿Desmonte, reforestación o erosión?","*Desmonte*."]),
 ER([("Cuidar es solo del Estado","Cuidamos entre todos"),("Proteger es no usar nada","Se usa con cuidado")],["Errores típicos.","Creer que cuidar es solo del *Estado*.","Y pensar que proteger es *no usar nada*."]),
 RES(["Repasemos.","Amenazan el *desmonte*, los *incendios* y la *sobrepesca*.","Sin *hábitat*, las especies peligran.","Los *parques* protegen.","Y cuidamos *entre todos*.","¡Clase terminada! Ahora, *a practicar*."],[["AMENAZAS","desmonte, incendios"],["HÁBITAT","su hogar"],["PARQUES","protegen"],["CUIDAR","entre todos"]])],
(7,1):[
 {"t":"reto","texto":"Dos plantas se quitan la luz. ¿Qué relación es?","segundos":6,"respuesta":"Competencia","emoji":"🌿","titulo":"COMPETENCIA Y DEPREDACIÓN","sub":"dos relaciones","voz":["Desafío: dos plantas se quitan la luz. ¿Qué relación es? Seis segundos.","Competencia.","Hoy: *competencia y depredación*."]},
 DEF("Competencia","Disputa por un recurso limitado","⚔️",["La *competencia* es la disputa por un recurso limitado.","Puede ser por alimento, agua, luz o espacio."]),
 CMP(("INTRAESPECÍFICA","Misma especie","🦁"),("INTERESPECÍFICA","Especies distintas","🦓"),"vs",["Hay dos tipos.","*Intraespecífica*: entre la misma especie.","*Interespecífica*: entre especies distintas."]),
 DEF("Depredación","Un animal caza a otro para comer","🐆",["En la *depredación*, un depredador caza a una presa para alimentarse.","Como el puma que caza al guanaco."]),
 CL([("COMPETENCIA","⚔️"),("DEPREDACIÓN","🐆")],[("Dos aves, un nido",0),("Águila caza ratón",1),("Plantas por luz",0)],["¿Competencia o depredación?","*Dos aves, un nido* y *plantas por luz*: competencia.","*Águila caza ratón*: depredación."]),
 Q("¿Cómo se llama el animal cazado?",["Presa","Depredador","Parásito"],0,["Te toca: ¿cómo se llama el animal cazado?","¿Presa, depredador o parásito?","La *presa*."]),
 ER([("El depredador es siempre malo","Regula las poblaciones"),("Competencia igual a depredación","Una lucha por recursos, otra caza")],["Errores típicos.","Creer que el depredador es *siempre malo*.","Y *confundir* competencia con depredación."]),
 RES(["Repasemos.","La *competencia* es por un recurso.","Puede ser *intra* o *interespecífica*.","La *depredación* es cazar para comer.","Y ambas *regulan* las poblaciones.","¡Clase terminada! Ahora, *a practicar*."],[["COMPETENCIA","un recurso"],["TIPOS","intra e inter"],["DEPREDACIÓN","cazar"],["EQUILIBRIO","regulan"]])],
(7,2):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"La abeja toma néctar 🐝"},{"yo":True,"txt":"¿Y la flor qué gana?"},{"yo":False,"txt":"Se poliniza 🌸"}],"titulo":"MUTUALISMO Y COMENSALISMO","sub":"quién gana","voz":["Lu cuenta que la abeja toma néctar.","Juan: ¿y la flor qué gana?","Lu: se poliniza.","Hoy: *mutualismo y comensalismo*."]},
 DEF("Mutualismo","Ambos se benefician","🤝",["En el *mutualismo*, ambos se benefician.","Como la abeja y la flor."]),
 DEF("Comensalismo","Uno gana y el otro no se afecta","🦈",["En el *comensalismo*, uno gana y el otro no se afecta.","Como la rémora y el tiburón."]),
 TB("QUIÉN GANA",["Relación","A","B"],[["Mutualismo","Gana","Gana"],["Comensalismo","Gana","Nada"],["Parasitismo","Gana","Pierde"]],["Quién gana en cada relación.","*Mutualismo*: ambos ganan.","*Comensalismo*: uno gana y el otro nada.","*Parasitismo*: uno gana y el otro pierde."]),
 CL([("MUTUALISMO","🤝"),("COMENSALISMO","🦈")],[("Abeja y flor",0),("Rémora y tiburón",1),("Hongo y alga",0),("Epífita y árbol",1)],["¿Qué relación?","*Abeja y flor* y *hongo y alga*: mutualismo.","*Rémora y tiburón* y *epífita y árbol*: comensalismo."]),
 Q("Si ambos se benefician, la relación es…",["Mutualismo","Comensalismo","Parasitismo"],0,["Te toca: si ambos se benefician.","¿Mutualismo, comensalismo o parasitismo?","*Mutualismo*."]),
 ER([("Toda ayuda favorece a ambos","Puede favorecer a uno"),("Comensalismo igual a parasitismo","En el comensalismo nadie pierde")],["Errores típicos.","Creer que toda ayuda favorece a *ambos*.","Y confundir *comensalismo* con parasitismo."]),
 RES(["Repasemos.","La *simbiosis* es una relación estrecha.","En el *mutualismo*, ambos ganan.","En el *comensalismo*, uno gana y el otro no se afecta.","Mirá siempre a *los dos*.","¡Clase terminada! Ahora, *a practicar*."],[["SIMBIOSIS","relación estrecha"],["MUTUALISMO","ambos ganan"],["COMENSALISMO","uno gana"],["CLAVE","mirar a los dos"]])],
(7,3):[
 {"t":"noticia","cinta":"MASCOTAS","titular":"Una garrapata viaja en un perro","bajada":"Y se alimenta de su sangre","emoji":"🐕","titulo":"PARASITISMO","sub":"parásito y hospedador","voz":["Mascotas: una garrapata viaja en un perro.","Y se alimenta de su sangre.","Hoy: *parasitismo*."]},
 DEF("Parasitismo","Uno se alimenta de otro y lo perjudica","🦟",["En el *parasitismo*, el parásito se alimenta del hospedador y lo perjudica.","No suele matarlo enseguida."]),
 CL([("ECTOPARÁSITO","🪲"),("ENDOPARÁSITO","🪱")],[("Pulga",0),("Tenia",1),("Garrapata",0),("Lombriz",1)],["¿Dónde viven?","*Pulga* y *garrapata*: ectoparásitos, fuera del cuerpo.","*Tenia* y *lombriz*: endoparásitos, dentro del cuerpo."]),
 TB("PARÁSITO Y DEPREDADOR",["","Parásito","Depredador"],[["Mata","No enseguida","Sí"],["Tamaño","Más chico","Más grande"],["Duración","Larga","Corta"]],["Diferencias.","El parásito *no mata enseguida*.","Suele ser *más chico*.","Y la relación es *larga*."]),
 PA("PREVENCIÓN",[("Higiene","🧼"),("Agua segura","🚰"),("Cocinar bien","🍳"),("Desparasitar","💊")],["Para prevenir parásitos.","Mantené la *higiene*.","Tomá *agua segura*.","*Cociná bien* los alimentos.","Y *desparasitá* a las mascotas."]),
 Q("El ser vivo que alberga al parásito es el…",["Hospedador","Depredador","Productor"],0,["Te toca: el que alberga al parásito.","¿Hospedador, depredador o productor?","El *hospedador*."]),
 ER([("El parásito mata enseguida","No suele hacerlo"),("Parásito igual a depredador","Se alimenta sin matar enseguida")],["Errores típicos.","Creer que el parásito *mata enseguida*.","Y *confundirlo* con el depredador."]),
 RES(["Repasemos.","El *parásito* perjudica a su *hospedador*.","Puede ser *ecto* o *endoparásito*.","No suele *matar enseguida*.","Y se previene con *higiene*.","¡Clase terminada! Ahora, *a practicar*."],[["PARÁSITO","perjudica"],["HOSPEDADOR","lo alberga"],["TIPOS","ecto y endo"],["PREVENCIÓN","higiene"]])],
(7,4):[
 {"t":"reto","texto":"Si desaparecen los zorros de un campo, ¿qué pasa con los roedores?","segundos":6,"respuesta":"Aumentan","emoji":"🦊","titulo":"REDES DE INTERACCIONES","sub":"todo está conectado","voz":["Desafío: si desaparecen los zorros de un campo, ¿qué pasa con los roedores? Seis segundos.","Aumentan.","Hoy: *redes de interacciones*."]},
 DEF("Red trófica","Cadenas alimentarias conectadas","🕸️",["Una *red trófica* son cadenas alimentarias conectadas.","Si cambia un eslabón, cambian los demás."]),
 CAU(("Desaparecen los zorros",'🦊'),[("Aumentan los roedores","🐭"),("Comen más plantas","🌱"),("Otros pierden alimento","🦉")],["Un efecto en cadena.","Aumentan los *roedores*.","Comen *más plantas*.","Y otros animales *pierden alimento*."]),
 CL([("SE DESEQUILIBRA","⚠️"),("SE MANTIENE","⚖️")],[("Llega una invasora",0),("Todo estable",1),("Falta especie clave",0)],["¿Se desequilibra o se mantiene?","*Una invasora* y *perder una especie clave*: se desequilibra.","*Todo estable*: se mantiene."]),
 DEF("Equilibrio","Poblaciones estables en el tiempo","⚖️",["El *equilibrio* es cuando las poblaciones se mantienen estables.","Las relaciones lo sostienen."]),
 Q("Si quitás una especie, ¿afecta a las demás?",["Sí","No","Solo a las plantas"],0,["Te toca: si quitás una especie, ¿afecta a las demás?","¿Sí, no o solo a las plantas?","*Sí*: hay efectos en cadena."]),
 ER([("Sacar una especie no afecta a otras","Todo está conectado"),("El equilibrio es fijo","Cambia y se ajusta")],["Errores típicos.","Creer que sacar una especie *no afecta*.","Y pensar que el equilibrio es *fijo*."]),
 RES(["Repasemos.","Las relaciones forman *redes*.","Una *red trófica* conecta cadenas.","Un cambio produce *efectos en cadena*.","Y hay que cuidar el *equilibrio*.","¡Clase terminada! Ahora, *a practicar*."],[["REDES","muchas relaciones"],["TRÓFICA","cadenas conectadas"],["CADENA","un cambio afecta a otros"],["EQUILIBRIO","poblaciones estables"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"cni1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciencias Naturales Integradas I","titulo":TIT[(m,n)],"sub":f"Ciencias Naturales Integradas I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"cni1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
