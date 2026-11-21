# -*- coding: utf-8 -*-
"""Ciencias Naturales Integradas I · Misión 8 (Flujo de materia y energía), 9 (Las personas y el ambiente) y 10 (La materia y sus estados)."""
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
# ================= MISIÓN 8 =================
A1=NV("Vas a explicar cómo fluye la energía por los niveles tróficos y por qué se pierde en cada paso.",["Niveles tróficos","La regla del 10 %","Pirámides","Qué pasa con la energía"],[
 S(1,"Niveles tróficos",[T("Quién ocupa cada nivel",["Nivel","Quién es","Ejemplo"],[["Productores","Fabrican su alimento con luz","Plantas, algas"],["Consumidores primarios","Comen productores","Conejo, vaca"],["Consumidores secundarios","Comen herbívoros","Zorro, rana"],["Consumidores terciarios","Comen carnívoros","Águila, puma"],["Descomponedores","Degradan restos y devuelven nutrientes","Hongos, bacterias"]])]),
 S(1,"La regla del 10 %",[D("Eficiencia ecológica","Porcentaje de la energía de un nivel que llega al siguiente."),P("En promedio pasa cerca del <b>10 %</b>: el resto se usa para vivir (moverse, mantener la temperatura) y se pierde como <b>calor</b>.")]),
 S(2,"Pirámides",[P("Por eso las <b>pirámides de energía</b> siempre son más angostas arriba: cada nivel recibe menos energía. También explica por qué hay pocos carnívoros grandes y muchos productores.")]),
 S(2,"Energía y materia",[P("La energía <b>fluye en un solo sentido</b> (del Sol a los seres vivos y se pierde como calor), mientras que la materia se <b>recicla</b>.")])],
 {"titulo":"calcular","planteo":"Un productor almacena 1.000 kJ. ¿Cuánta energía llega al consumidor primario?","pasos":["Pasa cerca del 10 %.","10 % de 1.000 = 100.","Llegan unos 100 kJ."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los seres que fabrican su alimento con luz son los ___ .","La energía que no pasa al siguiente nivel se pierde como ___ ."]},
 {"titulo":"tu turno","planteo":"Armá una cadena de cuatro eslabones y calculá la energía que llega a cada uno si el productor tiene 10.000 kJ."},
 {"titulo":"Un diez por ciento","texto":"Para pasar de un nivel al siguiente, dividí la energía por diez."},
 ["Creer que toda la energía pasa al siguiente nivel.","Confundir productor con consumidor."],
 RS(("Niveles","Productor a consumidores."),("Eficiencia","Cerca del 10 %."),("Pérdida","Calor."),("Pirámide","Más angosta arriba.")),
 G(("Productor","Ser vivo que fabrica su alimento."),("Consumidor","Ser vivo que se alimenta de otros."),("Descomponedor","Degrada restos."),("kJ","Kilojoule: unidad de energía.")),
 ["¿Cómo se llaman los seres que fabrican su propio alimento?","¿Qué porcentaje de energía pasa en promedio de un nivel al siguiente: 10 % o 90 %? Respondé solo el número.","¿En qué forma se pierde la mayor parte de la energía?","¿La energía se recicla o fluye en un solo sentido?"],
 [["productores","los productores"],["10"],["calor","en forma de calor"],["fluye en un solo sentido","un solo sentido","fluye"]],
 {"incompleto":"Productores. Calor.","solo":"10.000 → 1.000 → 100 → 10 kJ.","carpeta":["Productores.","10.","Calor.","Fluye en un solo sentido."]})
A2=NV("Vas a describir los ciclos del agua, el carbono, el nitrógeno y el fósforo y explicar por qué la materia se recicla.",["Agua","Carbono","Nitrógeno","Fósforo"],[
 S(1,"Ciclo del agua",[P("El Sol evapora el agua; el vapor se enfría y se <b>condensa</b> en nubes; luego <b>precipita</b> como lluvia o nieve y vuelve a ríos, suelos y mares. Los seres vivos la toman y la devuelven al respirar y transpirar.")]),
 S(1,"Ciclo del carbono",[T("Cómo circula",["Proceso","Qué pasa con el carbono"],[["Fotosíntesis","El CO₂ pasa a materia orgánica"],["Respiración","La materia orgánica vuelve a CO₂"],["Descomposición","Los restos devuelven CO₂"],["Combustión","Quemar combustibles libera CO₂ guardado hace millones de años"]])]),
 S(2,"Ciclo del nitrógeno",[P("El nitrógeno es el gas más abundante del aire, pero los seres vivos no pueden usarlo así. Algunas <b>bacterias</b> lo transforman en formas aprovechables (<b>fijación</b>), las plantas lo toman del suelo y otras bacterias lo devuelven al aire.")]),
 S(2,"Ciclo del fósforo",[P("El fósforo no tiene fase gaseosa importante: pasa de las <b>rocas</b> al suelo, a las plantas y a los animales, y al final vuelve a los suelos y sedimentos. Es un ciclo muy lento.")])],
 {"titulo":"relacionar","planteo":"¿Qué proceso devuelve CO₂ al aire cuando un animal respira?","pasos":["La respiración quema materia orgánica.","El producto es CO₂.","Vuelve a la atmósfera."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las plantas transforman el CO₂ en materia orgánica por la ___ .","Las bacterias que fijan el nitrógeno lo vuelven ___ para las plantas."]},
 {"titulo":"tu turno","planteo":"Dibujá el ciclo del agua con flechas y rotulá cuatro procesos."},
 {"titulo":"La materia vuelve","texto":"En los ciclos, los átomos no se crean ni se destruyen: se reorganizan."},
 ["Pensar que el CO₂ solo lo producen las fábricas.","Creer que las plantas toman el nitrógeno del aire directamente."],
 RS(("Agua","Evapora, condensa, precipita."),("Carbono","Fotosíntesis y respiración."),("Nitrógeno","Bacterias."),("Fósforo","Rocas y suelos.")),
 G(("Ciclo biogeoquímico","Recorrido de un elemento entre seres vivos y ambiente."),("Fijación","Transformación del nitrógeno del aire."),("Sedimento","Material que se deposita.")),
 ["¿Cómo se llama el proceso por el que el vapor se convierte en líquido en las nubes?","¿Qué gas toman las plantas para hacer fotosíntesis?","¿Quiénes fijan el nitrógeno: las bacterias o los minerales?","¿El ciclo del fósforo tiene una fase gaseosa importante? Respondé sí o no."],
 [["condensacion","condensación","la condensacion","la condensación"],["co2","co₂","dioxido de carbono","dióxido de carbono"],["bacterias","las bacterias"],["no"]],
 {"incompleto":"Fotosíntesis. Aprovechable.","solo":"Evaporación, condensación, precipitación, escurrimiento.","carpeta":["Condensación.","Dióxido de carbono.","Las bacterias.","No."]})
A3=NV("Vas a explicar qué es la productividad de un ecosistema y qué factores la determinan.",["Producción primaria","Bruta y neta","Factores","Ecosistemas productivos"],[
 S(1,"Producción primaria",[D("Productividad primaria","Cantidad de materia orgánica que fabrican los productores en un tiempo dado."),P("Es la base de toda la red trófica: de ella depende cuánta vida puede sostener un ecosistema.")]),
 S(1,"Bruta y neta",[T("Dos medidas",["Medida","Qué es"],[["Productividad bruta (PPB)","Todo lo que fabrican las plantas por fotosíntesis"],["Productividad neta (PPN)","Lo que queda después de que las plantas respiran"]]),P("<b>PPN = PPB − respiración</b>. La PPN es lo que está disponible para los consumidores.")]),
 S(2,"Factores",[T("Qué la limita",["Factor","Cómo influye"],[["Luz","Sin luz no hay fotosíntesis"],["Agua","Sin agua se cierran los estomas"],["Temperatura","Muy fría o muy cálida frena el proceso"],["Nutrientes","Sin nitrógeno ni fósforo no crecen"]])]),
 S(2,"Más y menos productivos",[T("Comparar",["Más productivos","Menos productivos"],[["Selvas tropicales","Desiertos"],["Humedales y estuarios","Mar abierto"],["Arrecifes de coral","Tundra"]])])],
 {"titulo":"calcular","planteo":"Un pastizal produce 1.200 unidades de PPB y las plantas gastan 400 al respirar. ¿Cuánta PPN hay?","pasos":["PPN = PPB − respiración.","1.200 − 400 = 800.","La PPN es de 800 unidades."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La productividad que queda después de la respiración es la ___ .","El ecosistema más productivo entre estos es la ___ tropical."]},
 {"titulo":"tu turno","planteo":"Elegí un ecosistema y explicá qué factor limita más su productividad."},
 {"titulo":"Lo que queda","texto":"Siempre restá la respiración: la neta es lo que realmente alimenta a otros."},
 ["Confundir bruta con neta.","Creer que el desierto es muy productivo."],
 RS(("Productividad","Materia que fabrican los productores."),("PPN","PPB menos respiración."),("Factores","Luz, agua, temperatura, nutrientes."),("Ejemplos","Selva alta; desierto baja.")),
 G(("PPB","Productividad bruta."),("PPN","Productividad neta."),("Estoma","Poro de las hojas.")),
 ["¿Cómo se llama la productividad que queda después de restar la respiración?","¿Cuál es el ecosistema más productivo: la selva tropical o el desierto?","¿Qué factor es necesario para la fotosíntesis: la luz o la sal?","¿Los nutrientes limitan la productividad? Respondé sí o no."],
 [["productividad neta","neta","la neta","ppn"],["selva tropical","selva","la selva tropical"],["luz","la luz"],["si","sí"]],
 {"incompleto":"Neta. Selva.","solo":"En el desierto limita el agua, por eso la productividad es baja.","carpeta":["Productividad neta.","La selva tropical.","La luz.","Sí."]})
A4=NV("Vas a armar un modelo de un ecosistema con componentes, flujos de materia y energía y límites, y usarlo para predecir.",["Qué es un modelo","Componentes","Flujos","Predecir con el modelo"],[
 S(1,"Qué es un modelo",[D("Modelo","Representación simplificada de un sistema que sirve para entenderlo y hacer predicciones."),P("Un modelo no es la realidad: deja afuera detalles para mostrar lo importante.")]),
 S(1,"Componentes",[T("Qué incluir",["Componente","Ejemplo en una laguna"],[["Productores","Algas, plantas acuáticas"],["Consumidores","Peces, ranas, aves"],["Descomponedores","Bacterias"],["Factores no vivos","Luz, agua, temperatura, nutrientes"]])]),
 S(2,"Flujos",[T("Qué se mueve",["Flujo","Cómo se dibuja"],[["Energía","Flecha del Sol y de un nivel al siguiente; sale como calor"],["Materia","Flechas circulares: nutrientes que vuelven"],["Entradas y salidas","Luz entra; calor sale"]])]),
 S(2,"Predecir",[P("Con el modelo se puede preguntar: <b>¿qué pasa si…?</b> Por ejemplo, si se contaminan las algas, bajan los peces. Un buen modelo permite anticipar efectos y se corrige cuando los datos no coinciden.")])],
 {"titulo":"modelar","planteo":"Armá un modelo simple de una laguna.","pasos":["Productores: algas.","Consumidores: peces y aves.","Flujos: el Sol entra, la energía pasa de nivel a nivel y sale como calor; los nutrientes vuelven por los descomponedores."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Una representación simplificada de un sistema es un ___ .","La energía que sale de un ecosistema lo hace como ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá un modelo de un ecosistema que conozcas y escribí una predicción."},
 {"titulo":"¿Qué pasa si...?","texto":"Un modelo sirve cuando te permite hacer una pregunta y anticipar la respuesta."},
 ["Pensar que un modelo es una copia exacta.","Dejar afuera los factores no vivos."],
 RS(("Modelo","Simplifica."),("Componentes","Vivos y no vivos."),("Flujos","Energía y materia."),("Predicción","¿Qué pasa si...?")),
 G(("Modelo","Representación simplificada."),("Flujo","Movimiento de energía o materia."),("Predicción","Anticipo de lo que va a pasar.")),
 ["¿Cómo se llama una representación simplificada de un sistema?","¿La energía se recicla o sale como calor?","Si se contaminan las algas de una laguna, ¿los peces aumentan o disminuyen?","¿Un modelo es una copia exacta de la realidad? Respondé sí o no."],
 [["modelo","un modelo"],["sale como calor","calor","sale como calor."],["disminuyen","disminuyen.","bajan"],["no"]],
 {"incompleto":"Modelo. Calor.","solo":"Modelo con algas, peces, bacterias, Sol, flujos y predicción.","carpeta":["Un modelo.","Sale como calor.","Disminuyen.","No."]})
ACT8={"1":[N("Un productor almacena {a} kJ. Si pasa el 10 % al consumidor primario, ¿cuántos kJ llegan?",{"formula":"a/10"},"10 % es dividir por 10.",{"vars":{"a":{"min":100,"max":900}},"reglas":["a%100==0"]}),{"t":"ordering","p":"Ordená la cadena trófica de menor a mayor energía.","o":["Águila","Productor","Ratón","Serpiente"],"r":{"orden":["Productor","Ratón","Serpiente","Águila"]},"e":"La energía disminuye en cada paso."}],
 "2":[{"t":"matching","p":"Uní cada ciclo con una característica.","o":{"izquierda":["Agua","Carbono","Nitrógeno","Fósforo"],"derecha":["Evaporación y condensación","Fotosíntesis y respiración","Bacterias fijadoras","Rocas y suelo"]},"r":{"pares":{"Agua":"Evaporación y condensación","Carbono":"Fotosíntesis y respiración","Nitrógeno":"Bacterias fijadoras","Fósforo":"Rocas y suelo"}},"e":"Cada ciclo tiene sus procesos."},VF("Las plantas toman el nitrógeno del aire directamente.","Falso","Lo toman del suelo, después de la fijación.")],
 "3":[N("Un ecosistema tiene PPB de {a} y la respiración gasta {b}. ¿Cuánta es la PPN?",{"formula":"a-b"},"PPN = PPB − respiración.",{"vars":{"a":{"min":800,"max":2000},"b":{"min":100,"max":500}},"reglas":["a%100==0","b%100==0"]}),MS("¿Qué factores limitan la productividad?",["Luz","Agua","Nutrientes","Color del cielo"],["Luz","Agua","Nutrientes"],"El color del cielo no influye.")],
 "4":[TT("Tocá los componentes vivos de la laguna: «En la laguna hay algas, peces, agua y bacterias».",["En","la","laguna","hay","algas,","peces,","agua","y","bacterias"],[4,5,8],"El agua es un factor no vivo."),{"t":"classify","p":"¿Entra o sale del ecosistema?","o":{"elementos":["Luz del Sol","Calor","Lluvia","Energía perdida"],"categorias":["Entra","Sale"]},"r":{"categorias":{"Luz del Sol":"Entra","Calor":"Sale","Lluvia":"Entra","Energía perdida":"Sale"}},"e":"La energía entra como luz y sale como calor."}],
 "5":[MC("Relámpago. La energía que pasa de un nivel al siguiente es cerca de…",["10 %","90 %","100 %"],"10 %","Regla del 10 %.",tiempo=20),VF("Relámpago. Los descomponedores devuelven nutrientes.","Verdadero","Reciclan la materia.",tiempo=20),MC("Relámpago. La PPN se calcula…",["PPB menos respiración","PPB más respiración","PPB por dos"],"PPB menos respiración","Es lo que queda.",tiempo=20),VF("Relámpago. La energía se recicla en el ecosistema.","Falso","Fluye en un solo sentido.",tiempo=20)]}
EX8=[[1,MC("¿Quiénes fabrican su alimento con luz?",["Productores","Consumidores","Descomponedores","Parásitos"],"Productores","Hacen fotosíntesis.")],
 [1,N("Un nivel tiene 2.000 kJ. ¿Cuántos pasan al siguiente si pasa el 10 %?",{"acepta":[200]},"10 % de 2.000 es 200.")],
 [1,VF("Toda la energía de un nivel pasa al siguiente.","Falso","Cerca del 10 %.")],
 [2,MC("¿Qué proceso devuelve CO₂ al aire?",["La respiración","La fotosíntesis","La condensación","La fijación"],"La respiración","Y la descomposición.")],
 [2,MC("¿Quiénes fijan el nitrógeno?",["Algunas bacterias","Las rocas","Las nubes","Los peces"],"Algunas bacterias","Lo vuelven aprovechable.")],
 [2,FB("El vapor que se enfría y forma nubes se ___ .",[["condensa"]],"Condensación.")],
 [3,MC("La productividad neta es…",["PPB menos respiración","PPB más respiración","Solo la respiración","El agua"],"PPB menos respiración","Es lo disponible.")],
 [3,MC("¿Cuál es el ecosistema más productivo?",["Selva tropical","Desierto","Tundra","Mar abierto"],"Selva tropical","Mucha luz, agua y calor.")],
 [3,VF("La luz limita la fotosíntesis.","Verdadero","Sin luz no hay.")],
 [4,MC("Un modelo es…",["Una representación simplificada","Una copia exacta","Un animal","Un ciclo"],"Una representación simplificada","Muestra lo importante.")],
 [4,MS("Componentes de un modelo de ecosistema:",["Productores","Consumidores","Descomponedores","Factores no vivos"],["Productores","Consumidores","Descomponedores","Factores no vivos"],"Todos son parte.")],
 [4,FB("La energía sale del ecosistema como ___ .",[["calor"]],"No se recicla.")],
 [4,VF("Con un modelo se pueden hacer predicciones.","Verdadero","¿Qué pasa si...?")]]
M8={"subject_id":SID,"tema":8,"practica":"Práctica general: flujo de materia y energía","examen_titulo":"Nivel jefe: flujo de materia y energía","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT8,"examen":EX8}

# ================= MISIÓN 9 =================
B1=NV("Vas a identificar las fuentes y los efectos de la contaminación del agua y del aire.",["Contaminantes del agua","Contaminantes del aire","Efectos","Cómo se mide"],[
 S(1,"Agua",[T("Fuentes",["Contaminante","Origen","Efecto"],[["Nutrientes (fertilizantes)","Agricultura, cloacas","Eutrofización: crecen algas que quitan oxígeno"],["Residuos sólidos","Basura","Dañan animales y obstruyen"],["Petróleo","Derrames","Cubre y ahoga a la fauna"],["Metales pesados","Industrias, minería","Se acumulan en los seres vivos"]])]),
 S(1,"Aire",[T("Fuentes",["Contaminante","Origen","Efecto"],[["Dióxido de carbono","Combustión","Aumenta el efecto invernadero"],["Material particulado","Humo, polvo","Problemas respiratorios"],["Óxidos de nitrógeno y de azufre","Vehículos, industrias","Lluvia ácida"],["Ozono a nivel del suelo","Reacción de contaminantes con luz","Irrita los pulmones"]])]),
 S(2,"Efectos",[P("La contaminación daña la salud de las personas y la vida de los ecosistemas. La <b>lluvia ácida</b> afecta a los bosques y a los lagos; la <b>eutrofización</b> deja sin oxígeno a los peces.")]),
 S(2,"Cómo se mide",[P("Se miden indicadores: el <b>pH</b> del agua, el oxígeno disuelto, la turbidez, la concentración de partículas en el aire. Esos datos permiten comparar con valores seguros.")])],
 {"titulo":"relacionar","planteo":"¿Por qué un exceso de fertilizantes en un lago hace morir peces?","pasos":["Los nutrientes hacen crecer muchas algas.","Cuando las algas mueren, se descomponen y gastan oxígeno.","Los peces quedan sin oxígeno."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El exceso de nutrientes en el agua provoca la ___ .","Los óxidos de azufre y de nitrógeno causan la lluvia ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un contaminante, explicá de dónde viene y qué daña."},
 {"titulo":"Origen y efecto","texto":"Para cada contaminante, preguntate de dónde viene y qué daña."},
 ["Pensar que el agua clara es siempre limpia.","Creer que el CO₂ no es un contaminante."],
 RS(("Agua","Nutrientes, residuos, petróleo."),("Aire","CO₂, partículas, óxidos."),("Efectos","Salud y ecosistemas."),("Medición","pH, oxígeno.")),
 G(("Eutrofización","Exceso de nutrientes en el agua."),("Particulado","Partículas sólidas en el aire."),("pH","Medida de acidez.")),
 ["¿Cómo se llama el exceso de nutrientes que causa el crecimiento excesivo de algas?","¿Qué lluvia causan los óxidos de azufre y de nitrógeno?","¿La basura plástica daña a los animales? Respondé sí o no.","¿Cómo se llama la medida de acidez?"],
 [["eutrofizacion","eutrofización","la eutrofizacion","la eutrofización"],["acida","ácida","lluvia acida","lluvia ácida"],["si","sí"],["ph","el ph"]],
 {"incompleto":"Eutrofización. Ácida.","solo":"Petróleo: viene de derrames; cubre y ahoga a la fauna.","carpeta":["Eutrofización.","Ácida.","Sí.","pH."]})
B2=NV("Vas a explicar las causas y las consecuencias de la pérdida de biodiversidad.",["Qué es la biodiversidad","Causas","Extinción","Consecuencias"],[
 S(1,"Biodiversidad",[D("Biodiversidad","Variedad de seres vivos de un lugar: especies, genes y ecosistemas."),P("Más biodiversidad hace a los ecosistemas más estables y resistentes.")]),
 S(1,"Causas",[T("Principales causas",["Causa","Ejemplo"],[["Pérdida del hábitat","Desmonte, urbanización"],["Sobreexplotación","Pesca y caza excesivas"],["Especies invasoras","Compiten con las nativas"],["Contaminación","Envenena agua y suelo"],["Cambio climático","Altera los climas"]])]),
 S(2,"Extinción",[P("Una especie se <b>extingue</b> cuando muere el último individuo. Hoy las especies se extinguen mucho más rápido que de manera natural, principalmente por la actividad humana.")]),
 S(2,"Consecuencias",[T("Qué se pierde",["Se pierde","Consecuencia"],[["Polinizadores","Menos cultivos"],["Bosques","Menos agua y suelo fértil"],["Especies clave","Efectos en cadena"],["Recursos médicos y genéticos","Menos descubrimientos"]])])],
 {"titulo":"relacionar","planteo":"¿Por qué la pérdida de abejas afecta los cultivos?","pasos":["Las abejas polinizan.","Sin polinizadores, muchas plantas dan menos frutos.","Hay menos cultivos."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cuando muere el último individuo de una especie, esta se ___ .","Una especie que llega de otro lugar y daña es ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una causa de pérdida de biodiversidad y proponé dos acciones."},
 {"titulo":"Pérdida en cadena","texto":"Cada especie que se pierde puede arrastrar a otras."},
 ["Pensar que la extinción solo ocurre naturalmente.","Creer que una sola especie no importa."],
 RS(("Biodiversidad","Variedad de vida."),("Causas","Hábitat, caza, invasoras."),("Extinción","Se pierde la especie."),("Consecuencias","En cadena.")),
 G(("Biodiversidad","Variedad de seres vivos."),("Extinción","Desaparición de una especie."),("Polinizador","Animal que lleva polen.")),
 ["¿Cómo se llama la variedad de seres vivos de un lugar?","¿Cómo se llama la desaparición total de una especie?","¿Las especies invasoras pueden dañar a las nativas? Respondé sí o no.","¿Cuál es la principal causa de pérdida de biodiversidad: la pérdida del hábitat o la lluvia?"],
 [["biodiversidad","la biodiversidad"],["extincion","extinción","la extincion","la extinción"],["si","sí"],["perdida del habitat","pérdida del hábitat","la perdida del habitat","la pérdida del hábitat"]],
 {"incompleto":"Extingue. Invasora.","solo":"Causa: desmonte. Acciones: proteger bosques y reforestar con especies nativas.","carpeta":["La biodiversidad.","Extinción.","Sí.","Pérdida del hábitat."]})
B3=NV("Vas a calcular y reducir la huella de carbono de una actividad cotidiana.",["Qué es la huella","Fuentes","Calcular","Reducir"],[
 S(1,"Huella de carbono",[D("Huella de carbono","Cantidad de gases de efecto invernadero (medida en CO₂ equivalente) que produce una persona, un producto o una actividad."),P("Cuanto más energía de combustibles fósiles se usa, mayor es la huella.")]),
 S(1,"Fuentes",[T("De dónde sale",["Fuente","Ejemplo"],[["Transporte","Auto, avión, colectivo"],["Energía","Electricidad y gas de la casa"],["Alimentación","Carne, productos importados"],["Consumo","Ropa y electrónicos nuevos"]])]),
 S(2,"Calcular",[P("Se calcula con <b>actividad × factor de emisión</b>. Por ejemplo, si un auto emite cerca de <b>0,2 kg de CO₂ por km</b>, un viaje de 50 km emite 50 × 0,2 = <b>10 kg</b>.")]),
 S(2,"Reducir",[T("Qué hacer",["Acción","Efecto"],[["Caminar o ir en bici","Emisión casi cero"],["Compartir el auto","Reparte la emisión"],["Ahorrar energía","Menos combustión"],["Comer más vegetales","Menos emisiones agrícolas"],["Reutilizar y reparar","Evita fabricar"]])])],
 {"titulo":"calcular","planteo":"Un auto emite 0,2 kg de CO₂ por km. ¿Cuánto emite en 30 km?","pasos":["Actividad: 30 km.","Factor: 0,2 kg por km.","30 × 0,2 = 6 kg."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La cantidad de gases de efecto invernadero que produce algo es su huella de ___ .","Se calcula multiplicando la actividad por el factor de ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí una actividad diaria, calculá su huella aproximada y proponé una forma de reducirla."},
 {"titulo":"Actividad por factor","texto":"Para estimar una huella, multiplicá cuánto hacés por cuánto emite cada unidad."},
 ["Creer que solo cuentan las fábricas.","Pensar que una acción individual no sirve de nada."],
 RS(("Huella","Gases emitidos."),("Fuentes","Transporte, energía, alimentación."),("Cálculo","Actividad por factor."),("Reducir","Ahorrar y compartir.")),
 G(("Huella de carbono","Gases que produce una actividad."),("Factor de emisión","Emisión por unidad de actividad."),("Combustible fósil","Petróleo, gas o carbón.")),
 ["¿Cómo se llama la cantidad de gases de efecto invernadero que produce una actividad?","¿Cuánto CO₂ emite un auto que recorre 50 km si emite 0,2 kg por km? Respondé solo el número.","¿Caminar tiene más o menos huella que ir en auto?","¿El consumo de energía de la casa suma a la huella? Respondé sí o no."],
 [["huella de carbono","la huella de carbono","huella"],["10"],["menos","menos huella"],["si","sí"]],
 {"incompleto":"Carbono. Emisión.","solo":"Colectivo 20 km: 20 × 0,1 = 2 kg; ir en bici lo evita.","carpeta":["Huella de carbono.","10.","Menos.","Sí."]})
B4=NV("Vas a evaluar soluciones sostenibles y explicar cómo contribuyen al desarrollo sostenible.",["Desarrollo sostenible","Las tres R","Energías renovables","Acción colectiva"],[
 S(1,"Desarrollo sostenible",[D("Desarrollo sostenible","Forma de satisfacer las necesidades actuales sin comprometer los recursos de las generaciones futuras."),P("Combina tres dimensiones: <b>ambiental, social y económica</b>.")]),
 S(1,"Las tres R",[T("Jerarquía",["R","Qué es","Ejemplo"],[["Reducir","Consumir menos","Evitar envases"],["Reutilizar","Dar otro uso","Frascos como vasos"],["Reciclar","Procesar para fabricar de nuevo","Papel, vidrio, plástico"]])]),
 S(2,"Energías renovables",[T("Opciones",["Fuente","Origen"],[["Solar","Luz del Sol"],["Eólica","Viento"],["Hidráulica","Agua en movimiento"],["Biomasa","Restos orgánicos"]]),P("No se agotan a escala humana y emiten mucho menos CO₂ que los combustibles fósiles.")]),
 S(2,"Acción colectiva",[P("Las soluciones más fuertes combinan <b>decisiones personales</b> (consumir con criterio), <b>acciones comunitarias</b> (compostaje, huertas, limpieza) y <b>políticas públicas</b> (leyes, transporte público, energías limpias).")])],
 {"titulo":"evaluar","planteo":"¿Qué es mejor para el ambiente: reciclar un envase o evitar usarlo?","pasos":["Reciclar ahorra materia prima, pero consume energía.","Reducir evita producir el residuo.","Por eso reducir va primero en la jerarquía."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las tres R son reducir, reutilizar y ___ .","La energía que viene del viento es la ___ ."]},
 {"titulo":"tu turno","planteo":"Proponé un plan escolar sostenible con tres acciones."},
 {"titulo":"Primero reducir","texto":"La mejor basura es la que no se genera."},
 ["Creer que reciclar alcanza para resolver todo.","Pensar que las energías renovables no emiten nada."],
 RS(("Sostenible","Presente y futuro."),("Tres R","Reducir, reutilizar, reciclar."),("Renovables","Solar, eólica."),("Colectivo","Personas, comunidades, Estado.")),
 G(("Sostenible","Que se puede mantener sin agotar recursos."),("Renovable","Energía que no se agota."),("Compostaje","Transformar restos orgánicos en abono.")),
 ["¿Cuáles son las tres R: reducir, reutilizar y qué?","¿Qué R va primero en la jerarquía?","¿La energía solar es renovable o fósil?","¿Las soluciones sostenibles combinan acciones personales y colectivas? Respondé sí o no."],
 [["reciclar","reciclar."],["reducir","la reducción","reduccion"],["renovable","es renovable"],["si","sí"]],
 {"incompleto":"Reciclar. Eólica.","solo":"Reducir envases, reutilizar frascos y reciclar papel en la escuela.","carpeta":["Reciclar.","Reducir.","Renovable.","Sí."]})
ACT9={"1":[{"t":"classify","p":"¿Contamina el agua o el aire?","o":{"elementos":["Derrame de petróleo","Humo de escape","Fertilizante en el río","Partículas de polvo"],"categorias":["Agua","Aire"]},"r":{"categorias":{"Derrame de petróleo":"Agua","Humo de escape":"Aire","Fertilizante en el río":"Agua","Partículas de polvo":"Aire"}},"e":"Según dónde actúa el contaminante."},FB("El exceso de nutrientes en el agua provoca la ___ .",[["eutrofizacion","eutrofización"]],"Muchas algas y poco oxígeno.")],
 "2":[MS("¿Cuáles son causas de pérdida de biodiversidad?",["Pérdida de hábitat","Especies invasoras","Sobreexplotación","Plantar especies nativas"],["Pérdida de hábitat","Especies invasoras","Sobreexplotación"],"Plantar nativas ayuda."),VF("Una especie se extingue cuando muere el último individuo.","Verdadero","Desaparece del planeta.")],
 "3":[N("Un auto emite 0,2 kg de CO₂ por km. ¿Cuántos kg emite en {a} km?",{"formula":"a/5"},"Distancia por 0,2.",{"vars":{"a":{"min":10,"max":90}},"reglas":["a%5==0"]}),{"t":"ordering","p":"Ordená de menor a mayor huella.","o":["Auto","Bicicleta","Avión","Colectivo"],"r":{"orden":["Bicicleta","Colectivo","Auto","Avión"]},"e":"Depende de la distancia y de cuántos viajan; en un trayecto largo el avión es el mayor."}],
 "4":[{"t":"matching","p":"Uní cada energía con su origen.","o":{"izquierda":["Solar","Eólica","Hidráulica","Biomasa"],"derecha":["Luz del Sol","Viento","Agua en movimiento","Restos orgánicos"]},"r":{"pares":{"Solar":"Luz del Sol","Eólica":"Viento","Hidráulica":"Agua en movimiento","Biomasa":"Restos orgánicos"}},"e":"Cada fuente, su origen."},TT("Tocá la R que va primero: «Reducir, reutilizar, reciclar».",["Reducir,","reutilizar,","reciclar"],[0],"Primero evitar producir residuos.")],
 "5":[MC("Relámpago. El gas principal del efecto invernadero emitido por combustión es…",["CO₂","Oxígeno","Nitrógeno"],"CO₂","Se libera al quemar.",tiempo=20),VF("Relámpago. La extinción es la desaparición de una especie.","Verdadero","Del planeta.",tiempo=20),MC("Relámpago. La R que va primero es…",["Reducir","Reciclar","Reparar"],"Reducir","Evita generar.",tiempo=20),VF("Relámpago. La energía solar es una fuente renovable.","Verdadero","No se agota.",tiempo=20)]}
EX9=[[1,MC("El exceso de nutrientes en el agua provoca…",["Eutrofización","Condensación","Fotosíntesis","Sublimación"],"Eutrofización","Muchas algas.")],
 [1,MC("La lluvia ácida se debe a…",["Óxidos de azufre y de nitrógeno","Polvo","Agua salada","Vapor"],"Óxidos de azufre y de nitrógeno","Salen de vehículos e industrias.")],
 [1,VF("El agua clara siempre está limpia.","Falso","Puede tener contaminantes disueltos.")],
 [2,MC("La biodiversidad es…",["La variedad de seres vivos","Un tipo de suelo","Un gas","Un río"],"La variedad de seres vivos","De especies, genes y ecosistemas.")],
 [2,MS("Causas de pérdida de biodiversidad:",["Pérdida del hábitat","Sobreexplotación","Especies invasoras","Reforestación con nativas"],["Pérdida del hábitat","Sobreexplotación","Especies invasoras"],"Reforestar ayuda.")],
 [2,VF("Hoy las especies se extinguen más rápido que de forma natural.","Verdadero","Por la actividad humana.")],
 [3,N("Un auto emite 0,2 kg de CO₂ por km. ¿Cuánto emite en 40 km?",{"acepta":[8]},"40 × 0,2 = 8.")],
 [3,MC("La huella de carbono se calcula…",["Actividad por factor de emisión","Sumando años","Dividiendo por dos","Midiendo agua"],"Actividad por factor de emisión","Cantidad por emisión unitaria.")],
 [3,VF("Caminar tiene menos huella que ir en auto.","Verdadero","Casi sin emisiones.")],
 [4,MC("El desarrollo sostenible satisface las necesidades actuales sin…",["Comprometer a las generaciones futuras","Usar energía","Producir alimentos","Vivir en ciudades"],"Comprometer a las generaciones futuras","Cuida los recursos.")],
 [4,MC("¿Qué R va primero?",["Reducir","Reciclar","Reutilizar","Reparar"],"Reducir","Evita residuos.")],
 [4,MS("Energías renovables:",["Solar","Eólica","Hidráulica","Carbón"],["Solar","Eólica","Hidráulica"],"El carbón es fósil.")],
 [4,VF("Las soluciones sostenibles combinan acciones personales y colectivas.","Verdadero","Todas suman.")]]
M9={"subject_id":SID,"tema":9,"practica":"Práctica general: las personas y el ambiente","examen_titulo":"Nivel jefe: las personas y el ambiente","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT9,"examen":EX9}

# ================= MISIÓN 10 =================
C1=NV("Vas a explicar los estados de la materia con la teoría cinético-molecular.",["Los postulados","Sólido, líquido y gas","Espacios y fuerzas","Usar el modelo"],[
 S(1,"Los postulados",[D("Teoría cinético-molecular","Modelo que explica que la materia está formada por partículas en constante movimiento, con espacios entre ellas y fuerzas que las atraen."),T("Ideas clave",["Idea","Qué dice"],[["Partículas","La materia está hecha de partículas diminutas"],["Movimiento","Siempre se mueven; más rápido si hay más temperatura"],["Espacios","Entre ellas hay espacio vacío"],["Fuerzas","Se atraen con distinta intensidad"]])]),
 S(1,"Tres estados",[T("Cómo son las partículas",["Estado","Orden","Movimiento","Fuerzas"],[["Sólido","Muy ordenadas","Vibran en su lugar","Muy fuertes"],["Líquido","Poco ordenadas","Se deslizan","Intermedias"],["Gas","Desordenadas","Muy rápido y libres","Muy débiles"]])]),
 S(2,"Forma y volumen",[T("Qué se observa",["Estado","Forma","Volumen"],[["Sólido","Propia","Propio"],["Líquido","Del recipiente","Propio"],["Gas","Del recipiente","Ocupa todo el recipiente"]])]),
 S(2,"Usar el modelo",[P("Con el modelo se explica por qué los gases se comprimen (hay mucho espacio) y los líquidos casi no (poco espacio), y por qué un sólido mantiene su forma (partículas fijas).")])],
 {"titulo":"explicar","planteo":"¿Por qué un gas ocupa todo el recipiente?","pasos":["Sus partículas se mueven muy rápido.","Las fuerzas entre ellas son muy débiles.","Se separan hasta ocupar todo el espacio."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Las partículas de un sólido ___ en su lugar.","Entre las partículas de un gas hay mucho ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá cómo se ven las partículas de un sólido, un líquido y un gas."},
 {"titulo":"Pensá en partículas","texto":"Cada vez que veas un estado, imaginá cómo se mueven sus partículas."},
 ["Creer que las partículas de un sólido están quietas.","Pensar que entre las partículas hay aire."],
 RS(("Partículas","Siempre en movimiento."),("Sólido","Ordenadas."),("Líquido","Se deslizan."),("Gas","Libres y rápidas.")),
 G(("Partícula","Unidad mínima de la materia en el modelo."),("Comprimir","Reducir el volumen."),("Vibrar","Moverse en el lugar.")),
 ["¿Cómo se mueven las partículas de un sólido: vibran o se deslizan?","¿Qué estado tiene partículas muy rápidas y libres?","¿Un líquido tiene volumen propio? Respondé sí o no.","¿Qué hay entre las partículas: aire o espacio vacío?"],
 [["vibran","vibran en su lugar"],["gas","el gas","gaseoso"],["si","sí"],["espacio vacio","espacio vacío","vacio","vacío"]],
 {"incompleto":"Vibran. Espacio.","solo":"Sólido: ordenadas y vibran; líquido: se deslizan; gas: libres y rápidas.","carpeta":["Vibran.","Gas.","Sí.","Espacio vacío."]})
C2=NV("Vas a explicar los cambios de estado según el modelo cinético-molecular.",["Los seis cambios","Energía y movimiento","Evaporación y ebullición","Sublimación"],[
 S(1,"Los seis cambios",[T("Nombres",["Cambio","De...","A..."],[["Fusión","Sólido","Líquido"],["Solidificación","Líquido","Sólido"],["Vaporización","Líquido","Gas"],["Condensación","Gas","Líquido"],["Sublimación","Sólido","Gas"],["Sublimación inversa","Gas","Sólido"]])]),
 S(1,"Energía y movimiento",[P("Cuando se <b>entrega calor</b>, las partículas se mueven más rápido y pueden vencer las fuerzas que las unen: <b>fusión</b> y <b>vaporización</b>. Cuando se <b>quita calor</b>, se mueven más despacio y las fuerzas las juntan: <b>solidificación</b> y <b>condensación</b>.")]),
 S(2,"Evaporación y ebullición",[T("Dos formas de vaporizar",["","Evaporación","Ebullición"],[["Dónde ocurre","Solo en la superficie","En todo el líquido"],["Temperatura","A cualquier temperatura","A la temperatura de ebullición"],["Velocidad","Lenta","Rápida, con burbujas"]])]),
 S(2,"Sublimación",[P("En la sublimación, las partículas pasan directo de sólido a gas sin pasar por líquido. Ejemplos: el hielo seco (CO₂ sólido) y la naftalina.")])],
 {"titulo":"explicar","planteo":"¿Por qué el hielo se derrite al calentarlo?","pasos":["El calor aumenta el movimiento de las partículas.","Vencen las fuerzas que las mantenían fijas.","Pasan a deslizarse: líquido."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El pasaje de sólido a líquido es la ___ .","El pasaje de gas a líquido es la ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un cambio de estado de tu casa y explicá qué pasa con las partículas."},
 {"titulo":"Calor entra, calor sale","texto":"Si el cambio necesita calor, las partículas se separan; si lo libera, se juntan."},
 ["Creer que el agua hierve solo a 100 °C en cualquier lugar.","Confundir condensación con evaporación."],
 RS(("Seis cambios","Fusión a sublimación inversa."),("Calor entra","Se separan."),("Calor sale","Se juntan."),("Evaporar","Solo la superficie.")),
 G(("Fusión","Sólido a líquido."),("Ebullición","Vaporización en todo el líquido."),("Sublimación","Sólido a gas.")),
 ["¿Cómo se llama el pasaje de líquido a gas?","¿Cómo se llama el pasaje de gas a líquido?","El hielo seco pasa directo de sólido a gas, ¿es sublimación o fusión?","¿La evaporación ocurre solo en la superficie? Respondé sí o no."],
 [["vaporizacion","vaporización"],["condensacion","condensación"],["sublimacion","sublimación"],["si","sí"]],
 {"incompleto":"Fusión. Condensación.","solo":"El hielo se funde: el calor acelera sus partículas y se deslizan.","carpeta":["Vaporización.","Condensación.","Sublimación.","Sí."]})
C3=NV("Vas a explicar la presión de un gas con el modelo y cómo cambia con el volumen y la temperatura.",["Qué es la presión","Presión y volumen","Presión y temperatura","Aplicaciones"],[
 S(1,"Presión de un gas",[D("Presión","Fuerza que ejercen las partículas del gas al chocar contra las paredes del recipiente, por unidad de superficie."),P("Más choques por segundo o choques más fuertes significan <b>más presión</b>.")]),
 S(1,"Presión y volumen",[P("Si la temperatura no cambia y se <b>reduce el volumen</b>, las partículas chocan más seguido contra las paredes: la presión <b>aumenta</b>. Es la <b>ley de Boyle</b>: al duplicar la presión, el volumen se reduce a la mitad.")]),
 S(2,"Presión y temperatura",[P("Si el volumen es fijo y <b>sube la temperatura</b>, las partículas se mueven más rápido y chocan con más fuerza: la presión <b>aumenta</b>. Por eso un envase cerrado puede explotar al calentarse.")]),
 S(2,"Aplicaciones",[T("Ejemplos cotidianos",["Situación","Explicación"],[["Inflar una pelota","Más partículas: más presión"],["Jeringa tapada","Al apretar el émbolo, la presión sube"],["Olla a presión","Mayor presión, mayor temperatura de ebullición"]])])],
 {"titulo":"predecir","planteo":"Un globo se deja al sol. ¿Qué le pasa a la presión del aire adentro?","pasos":["El calor aumenta la temperatura.","Las partículas chocan con más fuerza.","La presión sube y el globo puede explotar."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Si se reduce el volumen de un gas, la presión ___ .","Si sube la temperatura de un gas en un recipiente rígido, la presión ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá con partículas por qué una jeringa tapada es difícil de apretar."},
 {"titulo":"Choques","texto":"Presión es choques: más choques o más fuertes, más presión."},
 ["Creer que la presión viene del peso del gas.","Pensar que el gas ocupa solo parte del recipiente."],
 RS(("Presión","Choques."),("Boyle","Menos volumen, más presión."),("Temperatura","Más calor, más presión."),("Ejemplos","Globo, jeringa, olla.")),
 G(("Presión","Fuerza por superficie."),("Ley de Boyle","Relación inversa entre presión y volumen."),("Émbolo","Pieza que se mueve en una jeringa.")),
 ["Si se reduce el volumen de un gas a temperatura constante, ¿la presión aumenta o disminuye?","Si sube la temperatura en un recipiente rígido, ¿la presión aumenta o disminuye?","¿La presión de un gas se debe a los choques de las partículas? Respondé sí o no.","Un gas ocupa 6 L a 1 atm. Si la presión pasa a 2 atm (misma temperatura), ¿cuántos litros ocupa? Respondé solo el número."],
 [["aumenta","aumenta."],["aumenta","aumenta."],["si","sí"],["3"]],
 {"incompleto":"Aumenta. Aumenta.","solo":"Al apretar, el volumen baja y las partículas chocan más: la presión sube.","carpeta":["Aumenta.","Aumenta.","Sí.","3."]})
C4=NV("Vas a leer e interpretar una curva de calentamiento y explicar las mesetas con el modelo.",["Qué es una curva","Las mesetas","Calor latente","Leer una curva"],[
 S(1,"Curva de calentamiento",[D("Curva de calentamiento","Gráfico de temperatura en función del tiempo mientras se entrega calor a una sustancia."),P("Se mide con un termómetro cada minuto y se arma el gráfico.")]),
 S(1,"Las mesetas",[T("Agua a nivel del mar",["Tramo","Qué pasa","Temperatura"],[["Hielo","Sube","Hasta 0 °C"],["Fusión","Meseta: coexisten hielo y agua","0 °C"],["Agua líquida","Sube","De 0 a 100 °C"],["Ebullición","Meseta: coexisten agua y vapor","100 °C"],["Vapor","Sube","Más de 100 °C"]])]),
 S(2,"Calor latente",[P("En las mesetas el calor sigue entrando, pero la temperatura no sube: la energía se usa para <b>vencer las fuerzas entre partículas</b>, no para moverlas más rápido. Ese calor se llama <b>latente</b>.")]),
 S(2,"Leer una curva",[T("Cómo interpretarla",["Si ves...","Significa..."],[["Tramo inclinado","Una sola fase calentándose"],["Tramo horizontal","Cambio de estado"],["Temperatura de la meseta","Punto de fusión o de ebullición"]])])],
 {"titulo":"interpretar","planteo":"En una curva, la temperatura se queda en 100 °C varios minutos. ¿Qué pasa?","pasos":["Es un tramo horizontal: hay cambio de estado.","A 100 °C el agua hierve.","El calor se usa para pasar de líquido a vapor."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El tramo horizontal de la curva es la ___ .","El calor que se usa en el cambio de estado sin subir la temperatura es el calor ___ ."]},
 {"titulo":"tu turno","planteo":"Dibujá la curva de calentamiento del agua y rotulá las dos mesetas."},
 {"titulo":"Horizontal es cambio","texto":"Si la línea es horizontal, se está produciendo un cambio de estado."},
 ["Pensar que en la meseta no entra calor.","Creer que la temperatura siempre sube con el calor."],
 RS(("Curva","Temperatura y tiempo."),("Mesetas","Cambios de estado."),("Latente","Rompe fuerzas."),("Lectura","Horizontal es cambio.")),
 G(("Curva","Gráfico de una variable."),("Meseta","Tramo horizontal."),("Calor latente","Calor que cambia el estado sin cambiar la temperatura.")),
 ["¿A qué temperatura se produce la fusión del hielo?","¿A qué temperatura hierve el agua a nivel del mar?","¿Cómo se llama el tramo horizontal de una curva de calentamiento?","¿En la meseta sigue entrando calor? Respondé sí o no."],
 [["0","0 °c","0°c","0 grados"],["100","100 °c","100°c","100 grados"],["meseta","la meseta"],["si","sí"]],
 {"incompleto":"Meseta. Latente.","solo":"En la meseta de 100 °C el agua pasa de líquido a vapor.","carpeta":["0 °C.","100 °C.","Meseta.","Sí."]})
ACT10={"1":[{"t":"classify","p":"¿Qué estado es?","o":{"elementos":["Partículas ordenadas que vibran","Partículas que se deslizan","Partículas libres y muy rápidas","Forma propia y volumen propio"],"categorias":["Sólido","Líquido","Gas"]},"r":{"categorias":{"Partículas ordenadas que vibran":"Sólido","Partículas que se deslizan":"Líquido","Partículas libres y muy rápidas":"Gas","Forma propia y volumen propio":"Sólido"}},"e":"Según el modelo."},FB("Entre las partículas de la materia hay ___ vacío.",[["espacio"]],"El modelo supone espacios.")],
 "2":[{"t":"matching","p":"Uní cada cambio con su pasaje.","o":{"izquierda":["Fusión","Solidificación","Vaporización","Condensación"],"derecha":["Sólido a líquido","Líquido a sólido","Líquido a gas","Gas a líquido"]},"r":{"pares":{"Fusión":"Sólido a líquido","Solidificación":"Líquido a sólido","Vaporización":"Líquido a gas","Condensación":"Gas a líquido"}},"e":"Cada nombre, su pasaje."},VF("En la evaporación el líquido hierve en todo su volumen.","Falso","Eso es la ebullición.")],
 "3":[N("Un gas ocupa {a} L a 1 atm. Si la presión pasa a 2 atm a temperatura constante, ¿cuántos litros ocupa?",{"formula":"a/2"},"Se reduce a la mitad.",{"vars":{"a":{"min":4,"max":20}},"reglas":["a%2==0"]}),MS("¿Qué aumenta la presión de un gas en un recipiente rígido?",["Calentarlo","Agregar más gas","Enfriarlo","Sacar gas"],["Calentarlo","Agregar más gas"],"Más choques o más fuertes.")],
 "4":[{"t":"ordering","p":"Ordená los tramos de la curva del agua al calentarla.","o":["Ebullición","Fusión","Hielo que sube","Vapor que sube","Agua líquida que sube"],"r":{"orden":["Hielo que sube","Fusión","Agua líquida que sube","Ebullición","Vapor que sube"]},"e":"Alternan tramos inclinados y mesetas."},TT("Tocá las temperaturas de las mesetas: «El agua tiene mesetas a 0 °C y a 100 °C».",["El","agua","tiene","mesetas","a","0","°C","y","a","100","°C"],[5,9],"Fusión y ebullición.")],
 "5":[MC("Relámpago. El pasaje de líquido a gas es…",["Vaporización","Fusión","Solidificación"],"Vaporización","Calor entra.",tiempo=20),VF("Relámpago. Las partículas de un sólido están quietas.","Falso","Vibran.",tiempo=20),MC("Relámpago. Si el volumen baja, la presión…",["Aumenta","Disminuye","No cambia"],"Aumenta","Ley de Boyle.",tiempo=20),VF("Relámpago. En una meseta la temperatura sube.","Falso","Se mantiene.",tiempo=20)]}
EX10=[[1,MC("Las partículas de un sólido…",["Vibran en su lugar","Se mueven libres","Se deslizan","No existen"],"Vibran en su lugar","Muy ordenadas.")],
 [1,MC("¿Qué estado ocupa todo el recipiente?",["Gas","Sólido","Líquido","Ninguno"],"Gas","Partículas libres.")],
 [1,VF("Entre las partículas hay espacio vacío.","Verdadero","Según el modelo.")],
 [2,MC("El pasaje de sólido a líquido es…",["Fusión","Condensación","Sublimación","Vaporización"],"Fusión","Se entrega calor.")],
 [2,MC("El pasaje de gas a líquido es…",["Condensación","Fusión","Ebullición","Sublimación"],"Condensación","Se quita calor.")],
 [2,FB("El pasaje directo de sólido a gas es la ___ .",[["sublimacion","sublimación"]],"Sin pasar por líquido.")],
 [3,MC("La presión de un gas se debe a…",["Los choques de las partículas","El peso","El color","La forma"],"Los choques de las partículas","Contra las paredes.")],
 [3,N("Un gas ocupa 8 L a 1 atm. Si la presión pasa a 2 atm (misma temperatura), ¿cuántos litros ocupa?",{"acepta":[4]},"Se reduce a la mitad.")],
 [3,VF("Si sube la temperatura de un gas en un recipiente rígido, la presión sube.","Verdadero","Más choques, más fuertes.")],
 [4,MC("En una curva de calentamiento, un tramo horizontal indica…",["Un cambio de estado","Que no entra calor","Que la sustancia es sólida","Un error"],"Un cambio de estado","La temperatura se mantiene.")],
 [4,FB("El agua hierve a ___ °C a nivel del mar.",[["100"]],"Meseta de ebullición.")],
 [4,MC("El calor que cambia el estado sin subir la temperatura es el calor…",["Latente","Específico","Solar","Residual"],"Latente","Rompe fuerzas.")],
 [4,VF("En la meseta no entra calor.","Falso","Entra y se usa en el cambio.")]]
M10={"subject_id":SID,"tema":10,"practica":"Práctica general: la materia y sus estados","examen_titulo":"Nivel jefe: la materia y sus estados","niveles":{"1":C1,"2":C2,"3":C3,"4":C4},"act":ACT10,"examen":EX10}
for n,m in ((8,M8),(9,M9),(10,M10)):
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
STEPS={(8,1):"48f8d34e-85f0-4c1b-a001-31636e6d2fed",(8,2):"82cb00a0-a8ea-443a-a0a3-184581a5c958",(8,3):"ce0edb51-473d-4830-bffb-49aa831e7f08",(8,4):"aea76935-c587-4079-961d-b08d8e4f13f4",(9,1):"9712f47f-2d38-4f4a-abff-48ff6b85fc34",(9,2):"6826e898-8a97-4049-a5d7-51a716a3f03a",(9,3):"896af0d4-abc7-4709-acda-d0d0a227f0b3",(9,4):"454a882c-8175-4452-b37d-8da09f7fb976",(10,1):"158eeda1-ed9f-407b-82a4-e44aefe2eb90",(10,2):"27bf9d22-c4b2-47db-b172-972902b72b87",(10,3):"8853c7bd-ff59-47f8-9534-cab470b48a23",(10,4):"356de49b-fb07-46f8-8bac-fdb57d1d3396"}
TIT={(8,1):"Niveles tróficos y eficiencia",(8,2):"Ciclos biogeoquímicos",(8,3):"Productividad de un ecosistema",(8,4):"Modelo de un ecosistema",(9,1):"Contaminación del agua y del aire",(9,2):"Pérdida de biodiversidad",(9,3):"Huella de carbono",(9,4):"Soluciones sostenibles",(10,1):"Teoría cinético-molecular",(10,2):"Cambios de estado según el modelo",(10,3):"Presión y temperatura en los gases",(10,4):"Curvas de calentamiento"}
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
RET=lambda tx,seg,resp,em,ti,sub,v:{"t":"reto","texto":tx,"segundos":seg,"respuesta":resp,"emoji":em,"titulo":ti,"sub":sub,"voz":v}
NOT=lambda ci,ti,ba,em,tt,sub,v:{"t":"noticia","cinta":ci,"titular":ti,"bajada":ba,"emoji":em,"titulo":tt,"sub":sub,"voz":v}
CLS={(8,1):[
 RET("¿Cuánta energía pasa de un nivel al siguiente?",6,"Cerca del 10 %","⚡","NIVELES TRÓFICOS","y eficiencia",["Desafío: ¿cuánta energía pasa de un nivel al siguiente? Seis segundos.","Cerca del diez por ciento.","Hoy: *niveles tróficos y eficiencia*."]),
 TB("NIVELES",["Nivel","Quién es"],[["Productor","Planta, alga"],["Consumidor 1.º","Herbívoro"],["Consumidor 2.º","Carnívoro"],["Descomponedor","Hongo, bacteria"]],["Los niveles.","El *productor* fabrica su alimento.","El *consumidor primario* come productores.","El *secundario* come herbívoros.","Y el *descomponedor* degrada restos."]),
 DA("10 %","pasa","90 % se pierde","La mayor parte se pierde como calor","🔥",["En promedio pasa cerca del *diez por ciento*.","El resto se pierde, sobre todo como *calor*."]),
 CAU(("1.000 kJ en el productor",'🌱'),[("100 kJ al herbívoro","🐰"),("10 kJ al carnívoro","🦊"),("1 kJ al superdepredador","🦅")],["Un ejemplo con números.","Mil *kJ* en el productor.","Cien al *herbívoro*.","Diez al *carnívoro*.","Y uno al *superdepredador*."]),
 DEF("Pirámide de energía","Cada nivel recibe menos","🔺",["La *pirámide de energía* es más angosta arriba.","Cada nivel recibe menos energía."]),
 CL([("SE RECICLA","♻️"),("FLUYE","➡️")],[("Materia",0),("Energía",1),("Nutrientes",0)],["¿Se recicla o fluye?","*Materia* y *nutrientes*: se reciclan.","*Energía*: fluye en un solo sentido."]),
 Q("¿Qué porcentaje de energía pasa en promedio al siguiente nivel?",["10 %","90 %","100 %"],0,["Te toca: ¿qué porcentaje pasa al siguiente nivel?","¿Diez, noventa o cien por ciento?","*Diez por ciento*."]),
 ER([("Toda la energía pasa","Cerca del 10 %"),("Confundir productor y consumidor","El productor fabrica")],["Errores típicos.","Creer que *toda* la energía pasa.","Y confundir *productor* con consumidor."]),
 RES(["Repasemos.","Hay *productores*, *consumidores* y *descomponedores*.","Pasa cerca del *diez por ciento*.","El resto se pierde como *calor*.","Y la *pirámide* se angosta arriba.","¡Clase terminada! Ahora, *a practicar*."],[["NIVELES","productor a consumidores"],["EFICIENCIA","10 %"],["PÉRDIDA","calor"],["PIRÁMIDE","angosta arriba"]])],
(8,2):[
 {"t":"gancho","grande":"Los mismos átomos","emoji":"♻️","final":"circulan desde hace millones de años","titulo":"CICLOS BIOGEOQUÍMICOS","sub":"la materia se recicla","voz":["Los átomos de tu cuerpo ya estuvieron en otros seres vivos.","La materia se recicla.","Hoy: *ciclos biogeoquímicos*."]},
 CAU(("Ciclo del agua",'💧'),[("Evaporación","☀️"),("Condensación","☁️"),("Precipitación","🌧️"),("Escurrimiento","🏞️")],["El agua recorre cuatro pasos.","*Evaporación*.","*Condensación*.","*Precipitación*.","Y *escurrimiento*."]),
 TB("CICLO DEL CARBONO",["Proceso","Qué pasa"],[["Fotosíntesis","CO₂ a materia"],["Respiración","Materia a CO₂"],["Descomposición","Restos a CO₂"],["Combustión","Libera CO₂"]],["El carbono circula.","La *fotosíntesis* lo fija.","La *respiración* lo devuelve.","La *descomposición* también.","Y la *combustión* libera el carbono guardado."]),
 DEF("Fijación del nitrógeno","Bacterias lo vuelven aprovechable","🦠",["Las plantas no pueden usar el nitrógeno del aire.","Algunas *bacterias* lo *fijan* en formas aprovechables."]),
 DEF("Ciclo del fósforo","Va de rocas a suelo y seres vivos","🪨",["El *fósforo* pasa de las rocas al suelo, a las plantas y a los animales.","No tiene fase gaseosa importante."]),
 CL([("CARBONO","⚫"),("NITRÓGENO","🟣"),("AGUA","💧")],[("Fotosíntesis",0),("Bacterias fijadoras",1),("Precipitación",2)],["¿De qué ciclo?","*Fotosíntesis*: carbono.","*Bacterias fijadoras*: nitrógeno.","*Precipitación*: agua."]),
 Q("¿Qué proceso devuelve CO₂ al aire cuando respiramos?",["Respiración","Fotosíntesis","Condensación"],0,["Te toca: ¿qué devuelve CO₂ al aire?","¿Respiración, fotosíntesis o condensación?","La *respiración*."]),
 ER([("El CO₂ solo lo producen fábricas","También los seres vivos"),("Las plantas toman el N del aire","Lo toman del suelo")],["Errores típicos.","Creer que el CO₂ solo viene de *fábricas*.","Y que las plantas toman el *nitrógeno del aire*."]),
 RES(["Repasemos.","La *materia* se recicla.","El *agua* evapora y condensa.","El *carbono* va y vuelve.","El *nitrógeno* lo fijan bacterias.","¡Clase terminada! Ahora, *a practicar*."],[["AGUA","evapora y precipita"],["CARBONO","fotosíntesis y respiración"],["NITRÓGENO","bacterias"],["FÓSFORO","rocas y suelo"]])],
(8,3):[
 NOT("CAMPO","Dos ecosistemas, mucha diferencia","Uno rebosa de vida y el otro casi no","🌴","PRODUCTIVIDAD","de un ecosistema",["Campo: dos ecosistemas, mucha diferencia.","Uno rebosa de vida y el otro casi no.","Hoy: *productividad de un ecosistema*."]),
 DEF("Productividad primaria","Materia que fabrican los productores","🌱",["La *productividad primaria* es la materia que fabrican los productores en un tiempo.","Es la base de la red trófica."]),
 CMP(("PPB","Todo lo que fabrican","🌿"),("PPN","Lo que queda tras respirar","🌱"),"−",["Dos medidas.","La *PPB* es todo lo que fabrican las plantas.","La *PPN* es lo que queda después de la respiración."]),
 CAU(("Factores",'⚙️'),[("Luz","☀️"),("Agua","💧"),("Temperatura","🌡️"),("Nutrientes","🌱")],["La productividad depende de cuatro factores.","La *luz*.","El *agua*.","La *temperatura*.","Y los *nutrientes*."]),
 CL([("MUY PRODUCTIVO","📈"),("POCO PRODUCTIVO","📉")],[("Selva",0),("Desierto",1),("Arrecife",0),("Tundra",1)],["¿Productivo o no?","*Selva* y *arrecife*: muy productivos.","*Desierto* y *tundra*: poco productivos."]),
 Q("La PPN se calcula…",["PPB menos respiración","PPB más respiración","PPB por dos"],0,["Te toca: ¿cómo se calcula la PPN?","¿PPB menos respiración, más respiración o por dos?","*PPB menos respiración*."]),
 ER([("Confundir bruta con neta","Restar la respiración"),("El desierto es muy productivo","Tiene poca agua")],["Errores típicos.","*Confundir* bruta con neta.","Y creer que el *desierto* es muy productivo."]),
 RES(["Repasemos.","La *productividad* es materia fabricada.","*PPN* es PPB menos respiración.","Dependen de *luz*, *agua*, *temperatura* y *nutrientes*.","Y la selva es muy *productiva*.","¡Clase terminada! Ahora, *a practicar*."],[["PRODUCTIVIDAD","materia fabricada"],["PPN","PPB menos respiración"],["FACTORES","luz, agua"],["SELVA","muy productiva"]])],
(8,4):[
 RET("¿Un modelo es una copia exacta de la realidad?",6,"No: simplifica","🧩","MODELO DE UN ECOSISTEMA","predecir con modelos",["Desafío: ¿un modelo es una copia exacta de la realidad? Seis segundos.","No: simplifica.","Hoy: *modelo de un ecosistema*."]),
 DEF("Modelo","Representación simplificada de un sistema","🧩",["Un *modelo* es una representación simplificada de un sistema.","Sirve para entender y predecir."]),
 TB("COMPONENTES",["Componente","Ejemplo"],[["Productores","Algas"],["Consumidores","Peces"],["Descomponedores","Bacterias"],["No vivos","Luz, agua"]],["Qué incluir en el modelo.","*Productores*: algas.","*Consumidores*: peces.","*Descomponedores*: bacterias.","Y *factores no vivos*: luz y agua."]),
 CL([("ENTRA","⬇️"),("SALE","⬆️")],[("Luz del Sol",0),("Calor",1),("Lluvia",0)],["¿Entra o sale?","*Luz del Sol* y *lluvia*: entran.","*Calor*: sale."]),
 CAU(("Se contaminan las algas",'☠️'),[("Faltan productores","🌿"),("Bajan los peces","🐟"),("Menos aves","🦆")],["Una predicción con el modelo.","Si se contaminan las algas...","Faltan *productores*.","Bajan los *peces*.","Y hay menos *aves*."]),
 Q("¿Cómo sale la energía de un ecosistema?",["Como calor","Como materia","No sale"],0,["Te toca: ¿cómo sale la energía de un ecosistema?","¿Como calor, como materia o no sale?","*Como calor*."]),
 ER([("Un modelo es una copia exacta","Simplifica"),("Dejar afuera lo no vivo","Incluirlo")],["Errores típicos.","Creer que un modelo es *copia exacta*.","Y dejar afuera lo *no vivo*."]),
 RES(["Repasemos.","Un *modelo* simplifica.","Incluye componentes *vivos* y *no vivos*.","Muestra *flujos* de energía y materia.","Y permite *predecir*.","¡Clase terminada! Ahora, *a practicar*."],[["MODELO","simplifica"],["COMPONENTES","vivos y no vivos"],["FLUJOS","energía y materia"],["USO","predecir"]])],
(9,1):[
 NOT("ALERTA","Un lago se llena de algas","Los peces aparecen sin vida","🌊","CONTAMINACIÓN","del agua y del aire",["Alerta: un lago se llena de algas.","Los peces aparecen sin vida.","Hoy: *contaminación del agua y del aire*."]),
 TB("AGUA",["Contaminante","Efecto"],[["Nutrientes","Eutrofización"],["Basura","Daña animales"],["Petróleo","Ahoga la fauna"],["Metales pesados","Se acumulan"]],["Contaminantes del agua.","Los *nutrientes* causan eutrofización.","La *basura* daña animales.","El *petróleo* ahoga la fauna.","Los *metales pesados* se acumulan."]),
 TB("AIRE",["Contaminante","Efecto"],[["CO₂","Efecto invernadero"],["Partículas","Problemas respiratorios"],["Óxidos","Lluvia ácida"]],["Contaminantes del aire.","El *CO₂* aumenta el efecto invernadero.","Las *partículas* afectan la respiración.","Los *óxidos* causan lluvia ácida."]),
 CAU(("Eutrofización",'🟢'),[("Crecen las algas","🌿"),("Se gasta el oxígeno","🫧"),("Mueren los peces","🐟")],["Así actúa el exceso de nutrientes.","Crecen las *algas*.","Se gasta el *oxígeno*.","Y mueren los *peces*."]),
 CL([("AGUA","💧"),("AIRE","💨")],[("Derrame",0),("Humo",1),("Fertilizante",0),("Polvo",1)],["¿Agua o aire?","*Derrame* y *fertilizante*: agua.","*Humo* y *polvo*: aire."]),
 Q("El exceso de nutrientes en el agua provoca…",["Eutrofización","Condensación","Lluvia ácida"],0,["Te toca: el exceso de nutrientes en el agua.","¿Eutrofización, condensación o lluvia ácida?","*Eutrofización*."]),
 ER([("Agua clara igual a agua limpia","Puede tener contaminantes disueltos"),("El CO₂ no contamina","Aumenta el efecto invernadero")],["Errores típicos.","Creer que agua *clara* es limpia.","Y que el *CO₂* no es un contaminante."]),
 RES(["Repasemos.","El agua se contamina con *nutrientes*, *basura* y *petróleo*.","El aire, con *CO₂*, *partículas* y *óxidos*.","Hay *eutrofización* y *lluvia ácida*.","Y se mide con *indicadores*.","¡Clase terminada! Ahora, *a practicar*."],[["AGUA","nutrientes, petróleo"],["AIRE","CO₂, partículas"],["EFECTOS","salud y ecosistemas"],["MEDIR","pH"]])],
(9,2):[
 DA("Millones","de especies","en el planeta","Cada una cumple un papel","🌍",["El planeta tiene millones de especies.","Cada una cumple un *papel*."]),
 DEF("Biodiversidad","Variedad de seres vivos","🦋",["La *biodiversidad* es la variedad de seres vivos de un lugar.","Hace al ecosistema más estable."]),
 TB("CAUSAS",["Causa","Ejemplo"],[["Hábitat","Desmonte"],["Sobreexplotación","Pesca excesiva"],["Invasoras","Compiten"],["Contaminación","Envenena"],["Clima","Cambios"]],["Las causas.","*Pérdida del hábitat*: desmonte.","*Sobreexplotación*: pesca excesiva.","*Especies invasoras*.","*Contaminación*.","Y *cambio climático*."]),
 DEF("Extinción","Desaparece el último individuo","🦕",["Una especie se *extingue* cuando muere el último individuo.","Hoy ocurre mucho más rápido que de forma natural."]),
 CAU(("Faltan los polinizadores",'🐝'),[("Menos frutos","🍎"),("Menos cultivos","🌾"),("Menos alimento","🍽️")],["Una consecuencia concreta.","Faltan los *polinizadores*.","Hay *menos frutos*.","Menos *cultivos*.","Y menos *alimento*."]),
 Q("Cuando muere el último individuo de una especie, esta se…",["Extingue","Adapta","Reproduce"],0,["Te toca: cuando muere el último individuo.","¿Se extingue, se adapta o se reproduce?","Se *extingue*."]),
 ER([("Una sola especie no importa","Cada una arrastra a otras"),("Solo hay extinciones naturales","Hoy las causa la actividad humana")],["Errores típicos.","Creer que *una especie* no importa.","Y pensar que la extinción es *solo natural*."]),
 RES(["Repasemos.","La *biodiversidad* es variedad de vida.","Se pierde por *hábitat*, *sobreexplotación* e *invasoras*.","La *extinción* es definitiva.","Y causa efectos en *cadena*.","¡Clase terminada! Ahora, *a practicar*."],[["BIODIVERSIDAD","variedad"],["CAUSAS","hábitat, caza"],["EXTINCIÓN","definitiva"],["EFECTOS","en cadena"]])],
(9,3):[
 RET("Un auto emite 0,2 kg de CO₂ por km. ¿Cuánto emite en 50 km?",10,"10 kg","🚗","HUELLA DE CARBONO","calcular y reducir",["Desafío: un auto emite cero coma dos kilos de CO₂ por kilómetro. ¿Cuánto emite en cincuenta kilómetros? Diez segundos.","Diez kilos.","Hoy: *huella de carbono*."]),
 DEF("Huella de carbono","Gases que produce una actividad","👣",["La *huella de carbono* es la cantidad de gases de efecto invernadero que produce algo.","Se mide en CO₂ equivalente."]),
 TB("FUENTES",["Fuente","Ejemplo"],[["Transporte","Auto, avión"],["Energía","Electricidad, gas"],["Alimentación","Carne"],["Consumo","Ropa nueva"]],["De dónde sale.","*Transporte*.","*Energía*.","*Alimentación*.","Y *consumo*."]),
 PA("CÁLCULO",[("Actividad","📏"),("Factor de emisión","🏭"),("Multiplicar","✖️")],["Para calcular.","Tomá la *actividad*.","Buscá el *factor de emisión*.","Y *multiplicá*."]),
 CL([("MENOS HUELLA","🌱"),("MÁS HUELLA","🏭")],[("Caminar",0),("Auto solo",1),("Ahorrar energía",0),("Avión",1)],["¿Menos o más huella?","*Caminar* y *ahorrar energía*: menos.","*Auto solo* y *avión*: más."]),
 Q("La huella se calcula…",["Actividad por factor","Sumando años","Dividiendo por dos"],0,["Te toca: ¿cómo se calcula la huella?","¿Actividad por factor, sumando años o dividiendo por dos?","*Actividad por factor*."]),
 ER([("Solo cuentan las fábricas","Cuenta todo lo que hacemos"),("Una acción no sirve","Todas suman")],["Errores típicos.","Creer que solo cuentan las *fábricas*.","Y que una acción individual *no sirve*."]),
 RES(["Repasemos.","La *huella* mide los gases que emitimos.","Viene del *transporte*, la *energía* y la *alimentación*.","Se calcula con *actividad por factor*.","Y se reduce con *pequeñas decisiones*.","¡Clase terminada! Ahora, *a practicar*."],[["HUELLA","gases emitidos"],["FUENTES","transporte, energía"],["CÁLCULO","actividad por factor"],["REDUCIR","ahorrar"]])],
(9,4):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"¿Reciclar o reducir? ♻️"},{"yo":True,"txt":"Primero reducir 😉"},{"yo":False,"txt":"¿Por qué?"}],"titulo":"SOLUCIONES SOSTENIBLES","sub":"reducir, reutilizar, reciclar","voz":["Lu pregunta: ¿reciclar o reducir?","Juan: primero reducir.","Lu: ¿por qué?","Hoy: *soluciones sostenibles*."]},
 DEF("Desarrollo sostenible","Satisfacer necesidades sin comprometer el futuro","🌍",["El *desarrollo sostenible* satisface las necesidades actuales sin comprometer a las generaciones futuras.","Combina lo ambiental, lo social y lo económico."]),
 PA("LAS TRES R",[("Reducir","🔽"),("Reutilizar","🔁"),("Reciclar","♻️")],["Las tres R en orden.","*Reducir*: consumir menos.","*Reutilizar*: dar otro uso.","*Reciclar*: procesar para fabricar de nuevo."]),
 TB("ENERGÍAS RENOVABLES",["Fuente","Origen"],[["Solar","Sol"],["Eólica","Viento"],["Hidráulica","Agua"],["Biomasa","Restos orgánicos"]],["Energías renovables.","La *solar*, del Sol.","La *eólica*, del viento.","La *hidráulica*, del agua.","Y la *biomasa*, de restos orgánicos."]),
 CL([("RENOVABLE","♻️"),("FÓSIL","⛽")],[("Solar",0),("Carbón",1),("Eólica",0),("Petróleo",1)],["¿Renovable o fósil?","*Solar* y *eólica*: renovables.","*Carbón* y *petróleo*: fósiles."]),
 Q("¿Qué R va primero?",["Reducir","Reciclar","Reutilizar"],0,["Te toca: ¿qué R va primero?","¿Reducir, reciclar o reutilizar?","*Reducir*: evita generar residuos."]),
 ER([("Reciclar alcanza","Primero reducir"),("Renovables no emiten nada","Emiten mucho menos")],["Errores típicos.","Creer que *reciclar* alcanza.","Y que las renovables *no emiten nada*."]),
 RES(["Repasemos.","Lo *sostenible* cuida el futuro.","Las *tres R*: reducir, reutilizar, reciclar.","Las *renovables* no se agotan.","Y la acción es *personal* y *colectiva*.","¡Clase terminada! Ahora, *a practicar*."],[["SOSTENIBLE","cuida el futuro"],["TRES R","reducir primero"],["RENOVABLES","solar, eólica"],["ACCIÓN","entre todos"]])],
(10,1):[
 {"t":"gancho","grande":"Invisibles","emoji":"🔬","final":"las partículas que forman todo","titulo":"TEORÍA CINÉTICO-MOLECULAR","sub":"un modelo de la materia","voz":["No las podés ver, pero están en todo.","Las partículas se mueven siempre.","Hoy: *la teoría cinético-molecular*."]},
 TB("IDEAS CLAVE",["Idea","Qué dice"],[["Partículas","La materia las tiene"],["Movimiento","Siempre se mueven"],["Espacios","Hay espacio vacío"],["Fuerzas","Se atraen"]],["Cuatro ideas.","La materia está hecha de *partículas*.","Siempre se *mueven*.","Hay *espacio vacío* entre ellas.","Y se *atraen* con fuerzas."]),
 TB("TRES ESTADOS",["Estado","Partículas"],[["Sólido","Ordenadas, vibran"],["Líquido","Se deslizan"],["Gas","Libres y rápidas"]],["Cómo son en cada estado.","*Sólido*: ordenadas y vibran.","*Líquido*: se deslizan.","*Gas*: libres y rápidas."]),
 CL([("SÓLIDO","🧊"),("LÍQUIDO","💧"),("GAS","💨")],[("Forma propia",0),("Forma del envase",1),("Ocupa todo",2)],["¿Qué estado?","*Forma propia*: sólido.","*Forma del recipiente*: líquido.","*Ocupa todo*: gas."]),
 DEF("Compresión","Reducir el volumen","🗜️",["Los gases se *comprimen* porque hay mucho espacio entre sus partículas.","Los líquidos casi no."]),
 Q("¿Cómo se mueven las partículas de un sólido?",["Vibran","Se deslizan","Vuelan"],0,["Te toca: ¿cómo se mueven las partículas de un sólido?","¿Vibran, se deslizan o vuelan?","*Vibran* en su lugar."]),
 ER([("Un sólido está quieto","Sus partículas vibran"),("Entre las partículas hay aire","Hay espacio vacío")],["Errores típicos.","Creer que un sólido está *quieto*.","Y que entre las partículas hay *aire*."]),
 RES(["Repasemos.","La materia son *partículas en movimiento*.","Hay *espacio vacío* y *fuerzas*.","*Sólido*, *líquido* y *gas* se explican con el modelo.","Y los gases se *comprimen*.","¡Clase terminada! Ahora, *a practicar*."],[["PARTÍCULAS","siempre se mueven"],["SÓLIDO","vibran"],["LÍQUIDO","se deslizan"],["GAS","libres y rápidas"]])],
(10,2):[
 RET("¿Cómo se llama pasar de sólido a líquido?",5,"Fusión","🧊","CAMBIOS DE ESTADO","según el modelo",["Desafío: ¿cómo se llama pasar de sólido a líquido? Cinco segundos.","Fusión.","Hoy: *cambios de estado según el modelo*."]),
 TB("SEIS CAMBIOS",["Cambio","De a"],[["Fusión","Sólido a líquido"],["Solidificación","Líquido a sólido"],["Vaporización","Líquido a gas"],["Condensación","Gas a líquido"],["Sublimación","Sólido a gas"]],["Los cambios.","*Fusión*: sólido a líquido.","*Solidificación*: líquido a sólido.","*Vaporización*: líquido a gas.","*Condensación*: gas a líquido.","*Sublimación*: sólido a gas."]),
 CMP(("SE ENTREGA CALOR","Se mueven más rápido y se separan","🔥"),("SE QUITA CALOR","Se mueven más lento y se juntan","❄️"),"vs",["La energía decide.","Con *calor*, las partículas se separan.","Sin calor, se *juntan*."]),
 CMP(("EVAPORACIÓN","Solo en la superficie","💧"),("EBULLICIÓN","En todo el líquido","🫧"),"vs",["Dos formas de vaporizar.","La *evaporación* ocurre en la superficie.","La *ebullición*, en todo el líquido."]),
 CL([("CON CALOR","🔥"),("SIN CALOR","❄️")],[("Fusión",0),("Condensación",1),("Vaporización",0),("Solidificación",1)],["¿Entra o sale calor?","*Fusión* y *vaporización*: entra calor.","*Condensación* y *solidificación*: sale calor."]),
 Q("El pasaje directo de sólido a gas es…",["Sublimación","Fusión","Condensación"],0,["Te toca: de sólido a gas directo.","¿Sublimación, fusión o condensación?","*Sublimación*."]),
 ER([("Evaporar es hervir","Evaporar es en la superficie"),("Condensar es evaporar","Es gas a líquido")],["Errores típicos.","Confundir *evaporar* con hervir.","Y confundir *condensar* con evaporar."]),
 RES(["Repasemos.","Hay *seis* cambios de estado.","Con *calor* las partículas se separan.","Sin calor se *juntan*.","Y la *sublimación* salta el estado líquido.","¡Clase terminada! Ahora, *a practicar*."],[["CAMBIOS","seis"],["CALOR","separa"],["SIN CALOR","junta"],["SUBLIMACIÓN","sólido a gas"]])],
(10,3):[
 NOT("SEGURIDAD","Una lata cerrada explota al sol","El calor aumentó la presión","💥","PRESIÓN EN LOS GASES","y temperatura",["Seguridad: una lata cerrada explota al sol.","El calor aumentó la presión.","Hoy: *presión y temperatura en los gases*."]),
 DEF("Presión","Choques de las partículas contra las paredes","💥",["La *presión* de un gas viene de los choques de sus partículas contra las paredes.","Más choques o más fuertes, más presión."]),
 CMP(("MENOS VOLUMEN","Más choques","🗜️"),("MÁS PRESIÓN","Ley de Boyle","⬆️"),"→",["A temperatura constante.","Con *menos volumen*, hay más choques.","Entonces, *más presión*."]),
 CMP(("MÁS TEMPERATURA","Partículas más rápidas","🌡️"),("MÁS PRESIÓN","Choques más fuertes","⬆️"),"→",["Con volumen fijo.","Con *más temperatura*, van más rápido.","Y chocan con *más fuerza*."]),
 CL([("SUBE LA PRESIÓN","⬆️"),("BAJA LA PRESIÓN","⬇️")],[("Reducir el volumen",0),("Ampliar el volumen",1),("Calentar",0),("Enfriar",1)],["¿Sube o baja?","*Reducir el volumen* y *calentar*: sube.","*Ampliar el volumen* y *enfriar*: baja."]),
 Q("Si se reduce el volumen de un gas, la presión…",["Aumenta","Disminuye","No cambia"],0,["Te toca: se reduce el volumen de un gas.","¿La presión aumenta, disminuye o no cambia?","*Aumenta*."]),
 ER([("La presión viene del peso del gas","Viene de los choques"),("El gas ocupa parte del recipiente","Ocupa todo")],["Errores típicos.","Creer que la presión viene del *peso*.","Y que el gas ocupa *parte* del recipiente."]),
 RES(["Repasemos.","La *presión* viene de los choques.","Menos *volumen*, más presión.","Más *temperatura*, más presión.","Y se ve en globos y jeringas.","¡Clase terminada! Ahora, *a practicar*."],[["PRESIÓN","choques"],["BOYLE","menos volumen"],["TEMPERATURA","más choques"],["EJEMPLOS","globo, jeringa"]])],
(10,4):[
 RET("Si la temperatura no sube mientras entra calor, ¿qué está pasando?",8,"Un cambio de estado","📈","CURVAS DE CALENTAMIENTO","leer mesetas",["Desafío: si la temperatura no sube mientras entra calor, ¿qué está pasando? Ocho segundos.","Un cambio de estado.","Hoy: *curvas de calentamiento*."]),
 DEF("Curva de calentamiento","Temperatura en función del tiempo","📈",["Una *curva de calentamiento* muestra la temperatura en función del tiempo.","Mientras se entrega calor."]),
 {"t":"linea","titulo":"EL AGUA AL CALENTARSE","eventos":[{"fecha":"-10 °C","txt":"Hielo que sube","emoji":"🧊"},{"fecha":"0 °C","txt":"Meseta: fusión","emoji":"💧"},{"fecha":"50 °C","txt":"Agua que sube","emoji":"🌡️"},{"fecha":"100 °C","txt":"Meseta: ebullición","emoji":"♨️"}],"voz":["El agua al calentarse tiene cinco tramos.","El hielo sube hasta *cero grados*.","Meseta de *fusión*.","El agua líquida sube hasta *cien grados*.","Meseta de *ebullición*."]},
 DEF("Calor latente","Cambia el estado sin cambiar la temperatura","🔥",["El *calor latente* se usa para vencer las fuerzas entre partículas.","Por eso la temperatura no sube."]),
 CL([("TRAMO INCLINADO","📈"),("MESETA","➖")],[("Una sola fase",0),("Cambio de estado",1),("Temperatura sube",0),("Temp. constante",1)],["¿Inclinado o meseta?","*Una sola fase* y *temperatura sube*: inclinado.","*Cambio de estado* y *temperatura constante*: meseta."]),
 Q("¿A qué temperatura hierve el agua a nivel del mar?",["100 °C","0 °C","50 °C"],0,["Te toca: ¿a qué temperatura hierve el agua?","¿Cien, cero o cincuenta grados?","*Cien grados Celsius*."]),
 ER([("En la meseta no entra calor","Entra y cambia el estado"),("La temperatura siempre sube","En las mesetas no")],["Errores típicos.","Creer que en la meseta *no entra calor*.","Y que la temperatura *siempre sube*."]),
 RES(["Repasemos.","La *curva* muestra temperatura y tiempo.","Las *mesetas* son cambios de estado.","El *calor latente* rompe fuerzas.","Y *horizontal* significa cambio.","¡Clase terminada! Ahora, *a practicar*."],[["CURVA","temperatura y tiempo"],["MESETAS","cambios de estado"],["LATENTE","rompe fuerzas"],["LECTURA","horizontal es cambio"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"cni1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciencias Naturales Integradas I","titulo":TIT[(m,n)],"sub":f"Ciencias Naturales Integradas I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"cni1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
