# -*- coding: utf-8 -*-
"""Ciudadanía I y Ciudadanía I Argentina · Misión 1 (VARIANTE las dos)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
sys.path.insert(0, AQUI)
from practica import P as PRACTICA
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}

FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,ref,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":ref,"e":e,**k}
SID = "a549d16a-c872-4df7-b243-e4b508bd8668"
A1=NV("Vas a explicar qué es una comunidad, qué nos une y qué significa cuidar el bien común.",["Comunidad","Lo que nos une","Bien común","Convivir en la diferencia"],[
 S(1,"Comunidad",[D("Comunidad","Grupo de personas que comparten un lugar, intereses, normas o una historia y se reconocen como parte del mismo conjunto."),P("Una comunidad puede ser pequeña (una familia, un curso) o muy grande (un barrio, un país).")]),
 S(1,"Lo que nos une",[T("Vínculos",["Qué une","Ejemplo"],[["Lugar","Vivir en el mismo barrio"],["Intereses","Un club o un equipo"],["Normas","Reglas de convivencia"],["Historia y cultura","Fiestas, tradiciones, idioma"]])]),
 S(2,"Bien común",[PN("Cuando una comunidad cuida lo que es de todos (la plaza, la escuela, el agua), cuida el <b>bien común</b>. En la Argentina, por ejemplo, las plazas, las escuelas y los hospitales públicos son de todos.","Cuando una comunidad cuida lo que es de todos (la plaza, la escuela, el agua), cuida el <b>bien común</b>. En cada país, las plazas, las escuelas y los hospitales públicos son de todos.")]),
 S(2,"Convivir en la diferencia",[P("Las comunidades están formadas por personas distintas. Convivir es respetar las diferencias y resolver los conflictos sin violencia, con diálogo y con normas acordadas.")])],
 {"titulo":"relacionar","planteo":"¿Por qué una plaza descuidada es un problema de toda la comunidad?","pasos":["La plaza es un bien de todos.","Si se rompe o se ensucia, nadie puede disfrutarla bien.","Cuidarla es una responsabilidad compartida."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que es de todos y conviene a todos es el ___ común.","Convivir es resolver los conflictos con ___ y no con violencia."]},
 {"titulo":"tu turno","planteo":"Elegí una comunidad a la que pertenezcas y escribí tres cosas que te unen a ella."},
 {"titulo":"De todos","texto":"Preguntate siempre: ¿esto es de uno o es de todos?"},
 ["Creer que una comunidad es solo un lugar.","Pensar que cuidar lo común es tarea de otros."],
 RS(("Comunidad","Personas que se reconocen parte de un conjunto."),("Lo que une","Lugar, intereses, normas, cultura."),("Bien común","Lo que es de todos."),("Convivir","Respetar y dialogar.")),
 G(("Comunidad","Grupo que comparte algo y se reconoce unido."),("Bien común","Lo que conviene a todos."),("Convivencia","Vivir juntos respetándose."),("Pertenencia","Sentirse parte de un grupo.")),
 ["¿Cómo se llama el grupo de personas que comparten un lugar, normas o historia?","¿Cómo se llama lo que es de todos y conviene a todos?","¿Se puede ser parte de más de una comunidad? Respondé sí o no.","¿Con qué se resuelven los conflictos en una convivencia sana: con diálogo o con violencia?"],
 [["comunidad","una comunidad"],["bien comun","bien común","el bien comun","el bien común"],["si","sí"],["dialogo","diálogo","con dialogo","con diálogo"]],
 {"incompleto":"Comunidad. Diálogo.","solo":"Mi curso: compartimos aula, intereses y normas de convivencia.","carpeta":["Comunidad.","Bien común.","Sí.","Diálogo."]})
A2=NV("Vas a distinguir normas sociales, morales y jurídicas y explicar qué hace especial a una ley.",["Para qué sirven las normas","Tipos de normas","Costumbres","Qué es una ley"],[
 S(1,"Para qué sirven",[P("Las normas son reglas que orientan cómo comportarnos. Hacen posible la convivencia: sin ellas, cada uno haría lo que quiere y los conflictos se resolverían por la fuerza.")]),
 S(1,"Tipos de normas",[T("Tres grupos",["Tipo","Quién la impone","Qué pasa si no se cumple"],[["Moral","La conciencia de cada persona","Culpa o vergüenza"],["Social (costumbre)","El grupo","Rechazo o crítica"],["Jurídica (ley)","El Estado","Sanción obligatoria"]])]),
 S(2,"Costumbres",[PN("Las costumbres cambian de un lugar a otro y con el tiempo. Por ejemplo, en la Argentina es común saludar con un beso en la mejilla; en otros países se saluda de otra forma.","Las costumbres cambian de un lugar a otro y con el tiempo. Por ejemplo, el modo de saludar (un beso, un apretón de manos, una reverencia) varía según el país.")]),
 S(2,"Qué es una ley",[D("Ley","Norma jurídica general y obligatoria, dictada por una autoridad competente, que prevé una sanción si no se cumple."),P("Para que una ley sea justa debe valer para todos por igual y haber sido dictada por el procedimiento que fija la Constitución.")])],
 {"titulo":"clasificar","planteo":"¿Qué tipo de norma es «ceder el asiento a una persona mayor»?","pasos":["Nadie te obliga con una sanción legal.","El grupo lo espera y lo valora.","Es una norma social."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La norma que impone el Estado y tiene sanción es la norma ___ .","Una norma que depende de tu conciencia es una norma ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una norma moral, una social y una jurídica que conozcas."},
 {"titulo":"Sanción","texto":"Si incumplirla trae una sanción del Estado, es una ley."},
 ["Pensar que toda costumbre es una ley.","Creer que las leyes valen solo para algunos."],
 RS(("Normas","Reglas para convivir."),("Tipos","Moral, social, jurídica."),("Costumbre","Cambia según lugar y época."),("Ley","Obligatoria, con sanción.")),
 G(("Norma","Regla que orienta la conducta."),("Costumbre","Hábito repetido por un grupo."),("Sanción","Consecuencia por incumplir."),("Jurídica","Relativa al derecho y las leyes.")),
 ["¿Cómo se llama la regla que orienta cómo comportarnos?","¿Qué tipo de norma impone el Estado y tiene sanción: la jurídica o la moral?","¿Una costumbre puede cambiar con el tiempo? Respondé sí o no.","¿Una ley justa vale para todos por igual? Respondé sí o no."],
 [["norma","una norma"],["juridica","jurídica","la juridica","la jurídica"],["si","sí"],["si","sí"]],
 {"incompleto":"Jurídica. Moral.","solo":"Moral: no mentir. Social: saludar. Jurídica: pagar los impuestos.","carpeta":["Norma.","La jurídica.","Sí.","Sí."]})
A3=NV("Vas a distinguir derechos y responsabilidades y explicar por qué los derechos de uno terminan donde empiezan los de otro.",["Qué es un derecho","Responsabilidades","Derechos y límites","En la vida pública"],[
 S(1,"Qué es un derecho",[D("Derecho","Facultad que tienen todas las personas, reconocida por las normas, para vivir con dignidad y libertad."),PN("Algunos derechos básicos son la vida, la educación, la salud, la libertad de expresión y la igualdad ante la ley. En la Argentina están reconocidos en la Constitución Nacional.","Algunos derechos básicos son la vida, la educación, la salud, la libertad de expresión y la igualdad ante la ley. En la mayoría de los países están reconocidos en la Constitución.")]),
 S(1,"Responsabilidades",[T("Derecho y responsabilidad",["Derecho","Responsabilidad que lo acompaña"],[["Educación","Estudiar y respetar a docentes y compañeros"],["Expresarse","Hacerlo sin agredir ni difamar"],["Circular","Respetar las normas de tránsito"],["Un ambiente sano","Cuidar los espacios comunes"]])]),
 S(2,"Derechos y límites",[P("Mis derechos terminan donde empiezan los de otra persona. Por eso la libertad tiene límites: no puedo usar mi libertad para dañar a otros.")]),
 S(2,"En la vida pública",[P("Participar en la vida pública también es una responsabilidad: informarse, opinar con respeto, votar cuando corresponde y cuidar lo común.")])],
 {"titulo":"relacionar","planteo":"Poner la música muy fuerte de noche: ¿qué derechos chocan?","pasos":["Mi libertad de escuchar música.","El derecho de los vecinos al descanso.","Mi derecho termina donde empieza el de ellos."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["A cada derecho lo acompaña una ___ .","Mi libertad tiene ___ cuando daña a otros."]},
 {"titulo":"tu turno","planteo":"Elegí un derecho y escribí dos responsabilidades que lo acompañan."},
 {"titulo":"Derecho con deber","texto":"Cada vez que reclames un derecho, preguntate qué responsabilidad lo acompaña."},
 ["Creer que los derechos no tienen límites.","Pensar que las responsabilidades son castigos."],
 RS(("Derecho","Facultad reconocida."),("Responsabilidad","Lo que corresponde hacer."),("Límite","Donde empiezan los otros."),("Vida pública","Informarse y participar.")),
 G(("Derecho","Facultad reconocida por las normas."),("Responsabilidad","Obligación asumida con otros."),("Límite","Hasta dónde llega la libertad."),("Vida pública","Asuntos que afectan a toda la comunidad.")),
 ["¿Cómo se llama la facultad de todas las personas, reconocida por las normas?","¿Qué acompaña a cada derecho: una responsabilidad o un premio?","¿Mis derechos terminan donde empiezan los de otros? Respondé sí o no.","¿Informarse y votar son formas de participar en la vida pública? Respondé sí o no."],
 [["derecho","un derecho"],["responsabilidad","una responsabilidad"],["si","sí"],["si","sí"]],
 {"incompleto":"Derecho. Responsabilidad.","solo":"Derecho a la educación: estudiar y respetar a mis compañeros.","carpeta":["Derecho.","Responsabilidad.","Sí.","Sí."]})
A4=NV("Vas a explicar para qué existe el poder político y cómo se organiza y se limita en una democracia.",["Qué es el poder","Autoridad legítima","El Estado","Dividir el poder"],[
 S(1,"Qué es el poder",[D("Poder político","Capacidad de tomar decisiones obligatorias para toda la sociedad y de hacerlas cumplir."),P("Existe para ordenar la convivencia, resolver conflictos y proteger los derechos de todos.")]),
 S(1,"Autoridad legítima",[T("Poder y autoridad",["Idea","Qué significa"],[["Fuerza","Imponer por la violencia"],["Autoridad legítima","Se acepta porque se obtuvo por un procedimiento aceptado"],["Legitimidad","Que la comunidad reconozca ese poder como justo"]])]),
 S(2,"El Estado",[PN("El <b>Estado</b> es la organización política de una sociedad en un territorio: tiene gobierno, leyes y población. En la Argentina, el Estado nacional se organiza según la Constitución Nacional.","El <b>Estado</b> es la organización política de una sociedad en un territorio: tiene gobierno, leyes y población. En cada país, el Estado se organiza según su Constitución.")]),
 S(2,"Dividir el poder",[T("Tres poderes",["Poder","Función"],[["Legislativo","Hace las leyes"],["Ejecutivo","Gobierna y aplica las leyes"],["Judicial","Interpreta las leyes y resuelve conflictos"]]),P("Dividir el poder evita que alguien lo concentre y abuse. Esto se llama <b>división de poderes</b>.")])],
 {"titulo":"explicar","planteo":"¿Por qué conviene que el poder esté dividido?","pasos":["Si una sola persona hiciera, aplicara y juzgara las leyes, podría abusar.","Con tres poderes, cada uno controla a los otros.","Así se protegen los derechos."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El poder que hace las leyes es el ___ .","El poder que resuelve conflictos aplicando las leyes es el ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá con un ejemplo cotidiano por qué no conviene que una sola persona decida todo."},
 {"titulo":"Control mutuo","texto":"Un poder dividido es un poder controlado."},
 ["Confundir poder con fuerza.","Pensar que el Estado y el gobierno son lo mismo."],
 RS(("Poder","Decisiones obligatorias."),("Legitimidad","Aceptado por la comunidad."),("Estado","Organización política."),("Tres poderes","Legislativo, ejecutivo, judicial.")),
 G(("Poder político","Capacidad de decidir para todos."),("Legitimidad","Reconocimiento como justo."),("Estado","Organización política de una sociedad."),("División de poderes","Reparto de funciones del poder.")),
 ["¿Cómo se llama el poder que hace las leyes?","¿Cómo se llama el poder que resuelve conflictos aplicando las leyes?","¿La división de poderes evita los abusos? Respondé sí o no.","¿Cómo se llama la organización política de una sociedad en un territorio?"],
 [["legislativo","el legislativo","poder legislativo"],["judicial","el judicial","poder judicial"],["si","sí"],["estado","el estado"]],
 {"incompleto":"Legislativo. Judicial.","solo":"Si una sola persona decidiera todo, podría abusar; dividido, se controla.","carpeta":["Legislativo.","Judicial.","Sí.","Estado."]})
ACT={"1":[{"t":"classify","p":"¿Qué une a cada comunidad?","o":{"elementos":["Vivir en la misma calle","Hinchar por el mismo club","Hablar el mismo idioma","Compartir un barrio"],"categorias":["Lugar","Intereses o cultura"]},"r":{"categorias":{"Vivir en la misma calle":"Lugar","Hinchar por el mismo club":"Intereses o cultura","Hablar el mismo idioma":"Intereses o cultura","Compartir un barrio":"Lugar"}},"e":"Algunos vínculos son de lugar y otros de intereses o cultura."},FB("Lo que es de todos y conviene a todos es el bien ___ .",[["comun","común"]],"Bien común.")],
 "2":[{"t":"matching","p":"Uní cada norma con su tipo.","o":{"izquierda":["No mentir","Ceder el asiento","Pagar impuestos","Saludar al entrar"],"derecha":["Moral","Social","Jurídica","Social"]},"r":{"pares":{"No mentir":"Moral","Ceder el asiento":"Social","Pagar impuestos":"Jurídica","Saludar al entrar":"Social"}},"e":"Cada norma, su tipo."},VF("Toda costumbre es una ley.","Falso","Solo las normas jurídicas son leyes.")],
 "3":[MS("¿Qué responsabilidades acompañan al derecho a la educación?",["Estudiar","Respetar a docentes y compañeros","Faltar sin motivo","Cuidar la escuela"],["Estudiar","Respetar a docentes y compañeros","Cuidar la escuela"],"Faltar sin motivo no es una responsabilidad."),{"t":"ordering","p":"Ordená los pasos para resolver un choque de derechos.","o":["Buscar un acuerdo","Identificar los derechos en conflicto","Escuchar a cada parte","Respetar lo acordado"],"r":{"orden":["Identificar los derechos en conflicto","Escuchar a cada parte","Buscar un acuerdo","Respetar lo acordado"]},"e":"Primero entender, después acordar."}],
 "4":[TT("Tocá los tres poderes: «El poder legislativo, ejecutivo y judicial se controlan entre sí».",["El","poder","legislativo,","ejecutivo","y","judicial","se","controlan","entre","sí"],[2,3,5],"Son los tres poderes."),{"t":"classify","p":"¿Qué poder hace cada cosa?","o":{"elementos":["Sancionar una ley","Gobernar y aplicar las leyes","Dictar una sentencia","Debatir un proyecto"],"categorias":["Legislativo","Ejecutivo","Judicial"]},"r":{"categorias":{"Sancionar una ley":"Legislativo","Gobernar y aplicar las leyes":"Ejecutivo","Dictar una sentencia":"Judicial","Debatir un proyecto":"Legislativo"}},"e":"Cada poder tiene su función."}],
 "5":[MC("Relámpago. La norma impuesta por el Estado con sanción es…",["Jurídica","Moral","Social"],"Jurídica","Es la ley.",tiempo=20),VF("Relámpago. Los derechos no tienen límites.","Falso","Terminan donde empiezan los de otros.",tiempo=20),MC("Relámpago. El poder que hace las leyes es el…",["Legislativo","Judicial","Ejecutivo"],"Legislativo","Sanciona las leyes.",tiempo=20),VF("Relámpago. Dividir el poder evita abusos.","Verdadero","Se controlan entre sí.",tiempo=20)]}
EX=[[1,MC("¿Qué es el bien común?",["Lo que conviene a todos","Lo que le sirve a uno","Un impuesto","Un barrio"],"Lo que conviene a todos","Es lo de todos.")],
 [1,VF("Una persona puede pertenecer a más de una comunidad.","Verdadero","Familia, curso, club, barrio.")],
 [1,FB("Convivir es resolver los conflictos con ___ .",[["dialogo","diálogo"]],"Sin violencia.")],
 [2,MC("La norma que impone el Estado y tiene sanción es la…",["Jurídica","Moral","Social","Religiosa"],"Jurídica","Es la ley.")],
 [2,MC("Ceder el asiento a una persona mayor es una norma…",["Social","Jurídica","Penal","Fiscal"],"Social","El grupo la espera.")],
 [2,VF("Una ley justa vale para todos por igual.","Verdadero","Sin privilegios.")],
 [3,MC("A cada derecho lo acompaña…",["Una responsabilidad","Un castigo","Un premio","Un impuesto"],"Una responsabilidad","Son dos caras.")],
 [3,VF("Mis derechos terminan donde empiezan los de otros.","Verdadero","Esa es la regla de la convivencia.")],
 [3,MS("Formas de participar en la vida pública:",["Informarse","Votar cuando corresponde","Cuidar lo común","Ignorar los problemas"],["Informarse","Votar cuando corresponde","Cuidar lo común"],"Ignorar no es participar.")],
 [4,MC("El poder político sirve para…",["Ordenar la convivencia y proteger derechos","Imponer por la fuerza","Evitar las leyes","Cobrar impuestos"],"Ordenar la convivencia y proteger derechos","Es su función.")],
 [4,MC("¿Quién hace las leyes?",["El poder legislativo","El poder judicial","El poder ejecutivo","Los vecinos"],"El poder legislativo","Las sanciona.")],
 [4,FB("El poder que resuelve conflictos aplicando las leyes es el ___ .",[["judicial"]],"Poder judicial.")],
 [4,VF("La división de poderes evita que alguien concentre el poder.","Verdadero","Se controlan entre sí.")]]
M1={"subject_id":SID,"tema":1,"practica":"Práctica general: vivir juntos","examen_titulo":"Nivel jefe: vivir juntos","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT,"examen":EX}
M1["act"]["5"]=PRACTICA[1]; os.makedirs(os.path.join(AQUI,"mision-1"),exist_ok=True); json.dump(M1,open(os.path.join(AQUI,"mision-1","mision-1.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"780cd451-1abd-4408-842f-311f0d721c07",2:"4adad691-2b06-476e-ab25-ad8e03b87b3e",3:"afaf490e-c9d0-47c6-a89b-4e3900a05602",4:"ab284c98-f924-4066-9efa-d0dece855c51"}
TIT={1:"Qué nos une como comunidad",2:"Normas, leyes y costumbres",3:"Derechos y responsabilidades en la vida pública",4:"Para qué existe el poder político"}
def NEU(e,**k): e=dict(e); e["neutro"]=k; return e
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
RET=lambda tx,seg,resp,em,ti,sub,v:{"t":"reto","texto":tx,"segundos":seg,"respuesta":resp,"emoji":em,"titulo":ti,"sub":sub,"voz":v}
NOT=lambda ci,ti,ba,em,tt,sub,v:{"t":"noticia","cinta":ci,"titular":ti,"bajada":ba,"emoji":em,"titulo":tt,"sub":sub,"voz":v}
CLS={1:[
 NEU({"t":"gancho","grande":"Somos muchos","emoji":"🏘️","final":"y vivimos juntos todos los días","titulo":"QUÉ NOS UNE","sub":"como comunidad argentina","voz":["Todos los días compartimos calles, escuelas y plazas.","¿Qué nos une como comunidad?","Hoy: *qué nos une como comunidad*."]},sub="como comunidad",voz=["Todos los días compartimos calles, escuelas y plazas.","¿Qué nos une como comunidad?","Hoy: *qué nos une como comunidad*."]),
 DEF("Comunidad","Grupo que se reconoce parte de un conjunto","🏘️",["Una *comunidad* es un grupo que comparte algo y se reconoce unido.","Puede ser chica o enorme."]),
 TB("LO QUE NOS UNE",["Vínculo","Ejemplo"],[["Lugar","Barrio"],["Intereses","Club"],["Normas","Convivencia"],["Cultura","Fiestas"]],["Qué une a las personas.","El *lugar*.","Los *intereses*.","Las *normas*.","Y la *cultura*."]),
 DEF("Bien común","Lo que conviene a todos","🌳",["El *bien común* es lo que conviene a todos.","La plaza, la escuela y el agua son bienes comunes."]),
 CL([("DE TODOS","🌳"),("DE UNO","🏠")],[("Plaza",0),("Mi mochila",1),("Escuela pública",0)],["¿De todos o de uno?","*Plaza* y *escuela pública*: de todos.","*Mi mochila*: de uno."]),
 CAU(("Convivir",'🤝'),[("Respetar diferencias","🌈"),("Dialogar","💬"),("Acordar normas","📜")],["Convivir se logra con tres cosas.","*Respetar* las diferencias.","*Dialogar*.","Y *acordar* normas."]),
 Q("¿Qué es el bien común?",["Lo que conviene a todos","Lo que conviene a uno","Un impuesto"],0,["Te toca: ¿qué es el bien común?","¿Lo que conviene a todos, a uno o un impuesto?","*Lo que conviene a todos*."]),
 ER([("Una comunidad es solo un lugar","También intereses y normas"),("Cuidar lo común es tarea de otros","Es de todos")],["Errores típicos.","Creer que una comunidad es *solo un lugar*.","Y que cuidar lo común es *tarea de otros*."]),
 RES(["Repasemos.","Una *comunidad* se reconoce unida.","Nos une el *lugar*, los *intereses* y la *cultura*.","El *bien común* conviene a todos.","Y se convive con *diálogo*.","¡Clase terminada! Ahora, *a practicar*."],[["COMUNIDAD","se reconoce unida"],["VÍNCULOS","lugar, intereses"],["BIEN COMÚN","de todos"],["CONVIVIR","dialogar"]])],
2:[
 RET("¿Cómo se llama una regla que orienta cómo comportarnos?",5,"Norma","📜","NORMAS, LEYES","y costumbres",["Desafío: ¿cómo se llama una regla que orienta cómo comportarnos? Cinco segundos.","Norma.","Hoy: *normas, leyes y costumbres*."]),
 DEF("Norma","Regla que orienta la conducta","📜",["Una *norma* es una regla que orienta cómo comportarnos.","Hace posible la convivencia."]),
 TB("TRES TIPOS",["Tipo","Quién la impone"],[["Moral","Tu conciencia"],["Social","El grupo"],["Jurídica","El Estado"]],["Tres tipos de normas.","La *moral*: tu conciencia.","La *social*: el grupo.","La *jurídica*: el Estado."]),
 CMP(("COSTUMBRE","Cambia con el lugar y el tiempo","🎎"),("LEY","Obligatoria, con sanción","⚖️"),"vs",["Costumbre y ley.","La *costumbre* cambia.","La *ley* es obligatoria y tiene sanción."]),
 CL([("MORAL","💭"),("SOCIAL","👥"),("JURÍDICA","⚖️")],[("No mentir",0),("Ceder el asiento",1),("Pagar impuestos",2)],["¿Qué tipo de norma?","*No mentir*: moral.","*Ceder el asiento*: social.","*Pagar impuestos*: jurídica."]),
 Q("¿Qué norma impone el Estado y tiene sanción?",["Jurídica","Moral","Social"],0,["Te toca: ¿qué norma impone el Estado?","¿Jurídica, moral o social?","La *jurídica*."]),
 ER([("Toda costumbre es una ley","Solo las jurídicas lo son"),("Las leyes valen para algunos","Valen para todos")],["Errores típicos.","Creer que toda *costumbre* es ley.","Y que las leyes valen solo para *algunos*."]),
 RES(["Repasemos.","Las *normas* ordenan la convivencia.","Hay *morales*, *sociales* y *jurídicas*.","Las *costumbres* cambian.","Y la *ley* es obligatoria.","¡Clase terminada! Ahora, *a practicar*."],[["NORMAS","reglas"],["TIPOS","moral, social, jurídica"],["COSTUMBRE","cambia"],["LEY","con sanción"]])],
3:[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Mi vecino pone música a las 2 am 😩"},{"yo":True,"txt":"Es su derecho, ¿no?"},{"yo":False,"txt":"¿Y mi derecho a dormir?"}],"titulo":"DERECHOS Y","sub":"responsabilidades","voz":["Lu cuenta que su vecino pone música a las dos de la mañana.","Juan: es su derecho, ¿no?","Lu: ¿y mi derecho a dormir?","Hoy: *derechos y responsabilidades*."]},
 DEF("Derecho","Facultad reconocida para vivir con dignidad","⚖️",["Un *derecho* es una facultad reconocida a todas las personas.","Sirve para vivir con dignidad y libertad."]),
 TB("DERECHO Y DEBER",["Derecho","Responsabilidad"],[["Educación","Estudiar"],["Expresarse","Sin agredir"],["Circular","Respetar tránsito"],["Ambiente sano","Cuidar lo común"]],["Cada derecho tiene su responsabilidad.","*Educación*: estudiar.","*Expresarse*: sin agredir.","*Circular*: respetar el tránsito.","*Ambiente sano*: cuidar lo común."]),
 DEF("Límite","Donde empiezan los derechos de otros","🚧",["Mis derechos terminan donde empiezan los de otros.","Ese es el *límite* de la libertad."]),
 CL([("DERECHO","⚖️"),("RESPONSABILIDAD","🤲")],[("Estudiar",1),("Opinar",0),("Cuidar la plaza",1)],["¿Derecho o responsabilidad?","*Opinar*: derecho.","*Estudiar* y *cuidar la plaza*: responsabilidades."]),
 Q("Mis derechos terminan donde…",["Empiezan los de otros","Termina el día","Empieza la ley"],0,["Te toca: mis derechos terminan donde...","¿Empiezan los de otros, termina el día o empieza la ley?","Donde *empiezan los de otros*."]),
 ER([("Los derechos no tienen límites","Terminan donde empiezan los de otros"),("Las responsabilidades son castigos","Son parte del derecho")],["Errores típicos.","Creer que los derechos *no tienen límites*.","Y que las responsabilidades son *castigos*."]),
 RES(["Repasemos.","Un *derecho* es una facultad reconocida.","Lo acompaña una *responsabilidad*.","La libertad tiene *límites*.","Y participar es *responsabilidad*.","¡Clase terminada! Ahora, *a practicar*."],[["DERECHO","facultad reconocida"],["RESPONSABILIDAD","lo acompaña"],["LÍMITE","los otros"],["VIDA PÚBLICA","participar"]])],
4:[
 NOT("PODER","Nadie puede decidirlo todo","Por eso el poder se divide","🏛️","EL PODER POLÍTICO","para qué existe",["Noticia: nadie puede decidirlo todo.","Por eso el poder se divide.","Hoy: *para qué existe el poder político*."]),
 DEF("Poder político","Capacidad de decidir para todos","🏛️",["El *poder político* es la capacidad de tomar decisiones obligatorias para toda la sociedad.","Existe para ordenar la convivencia."]),
 CMP(("FUERZA","Se impone por violencia","👊"),("AUTORIDAD LEGÍTIMA","La comunidad la reconoce justa","🤝"),"vs",["Dos formas de ejercer poder.","La *fuerza* se impone.","La *autoridad legítima* es reconocida."]),
 TB("TRES PODERES",["Poder","Función"],[["Legislativo","Hace las leyes"],["Ejecutivo","Gobierna"],["Judicial","Resuelve conflictos"]],["Los tres poderes.","El *legislativo* hace las leyes.","El *ejecutivo* gobierna.","El *judicial* resuelve conflictos."]),
 CL([("LEGISLATIVO","📜"),("EJECUTIVO","🏛️"),("JUDICIAL","⚖️")],[("Sancionar una ley",0),("Gobernar",1),("Dictar sentencia",2)],["¿Qué poder?","*Sancionar una ley*: legislativo.","*Gobernar*: ejecutivo.","*Dictar sentencia*: judicial."]),
 Q("¿Qué poder hace las leyes?",["Legislativo","Judicial","Ejecutivo"],0,["Te toca: ¿qué poder hace las leyes?","¿Legislativo, judicial o ejecutivo?","El *legislativo*."]),
 ER([("Poder igual fuerza","Poder es decidir con legitimidad"),("Estado y gobierno son lo mismo","El gobierno es parte del Estado")],["Errores típicos.","Confundir *poder* con fuerza.","Y *Estado* con gobierno."]),
 RES(["Repasemos.","El *poder político* ordena la convivencia.","Necesita *legitimidad*.","El *Estado* es la organización política.","Y el poder se *divide* en tres.","¡Clase terminada! Ahora, *a practicar*."],[["PODER","decide para todos"],["LEGITIMIDAD","reconocida"],["ESTADO","organización"],["TRES PODERES","se controlan"]])]}
for n,es in CLS.items():
    json.dump(({"sin_variante":True} if n>1 else {})|{"slug":f"ciud1-m1-n{n}","step_id":STEPS[n],"materia":"Ciudadanía I","titulo":TIT[n],"sub":f"Ciudadanía I · Misión 1 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"ciud1-m1-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
