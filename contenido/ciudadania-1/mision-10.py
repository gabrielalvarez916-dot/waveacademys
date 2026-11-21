# -*- coding: utf-8 -*-
"""Ciudadanía I · Misión 10 (proyecto: propuesta de participación juvenil) · VARIANTE."""
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
# ============ MISIÓN 10: PROYECTO · UNA PROPUESTA DE PARTICIPACIÓN JUVENIL ============
B1=NV("Vas a elegir un problema real de tu comunidad y formularlo para poder trabajar en una propuesta.",["Qué es un proyecto de participación","Dónde buscar problemas","Cómo elegir bien","Cómo formular el problema"],[
 S(1,"Qué es un proyecto de participación",[D("Proyecto de participación","Plan para mejorar algo de la comunidad con una acción concreta, pensada y presentada por jóvenes."),P("No se trata de quejarse ni de esperar que otros lo resuelvan: se parte de un problema real, se investiga, se diseña una propuesta y se presenta a quienes pueden decidir.")]),
 S(1,"Dónde buscar problemas",[T("Ámbitos posibles",["Ámbito","Ejemplo de problema"],[["Espacios públicos","Una plaza sin luz ni bancos"],["Ambiente","Basura acumulada en un arroyo"],["Salud y bienestar","Pocos lugares para hacer deporte"],["Transporte","Colectivos que no pasan de noche"],["Internet","Burlas y acoso en las redes"]])]),
 S(2,"Cómo elegir bien",[T("Criterios para elegir",["Criterio","Pregunta para hacerte"],[["Me afecta","¿Lo vivo yo o gente cercana?"],["Es concreto","¿Puedo describirlo con un ejemplo?"],["Se puede mejorar","¿Hay una acción posible para jóvenes?"],["Hay información","¿Puedo conseguir datos y testimonios?"]])]),
 S(2,"Cómo formular el problema",[P("Un problema se escribe como una situación, no como una solución. Mal: «Falta un semáforo». Bien: «Cruzar la avenida es peligroso para quienes van a pie». Así se pueden pensar varias soluciones."),IM("Una oración clara","Quién, qué ocurre, dónde y desde cuándo.")])],
 {"titulo":"elegir","planteo":"Tres ideas: «arreglar el mundo», «falta iluminación en la plaza de mi ciudad» y «que todos sean felices». ¿Cuál sirve como problema?","pasos":["«Arreglar el mundo» es demasiado grande.","«Que todos sean felices» no se puede medir.","«Falta iluminación en la plaza» es concreto y se puede mejorar."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un problema se escribe como una situación, no como una ___ .","Un problema ___ se puede describir con un ejemplo."]},
 {"titulo":"tu turno","planteo":"Escribí un problema de tu comunidad en una oración: quién, qué ocurre y dónde."},
 {"titulo":"Empezá por lo cercano","texto":"Elegí un problema que veas o vivas: sabés más y cuesta menos investigarlo."},
 ["Elegir un problema enorme que nadie puede abordar.","Escribir una solución en vez del problema."],
 RS(("Proyecto","Plan para mejorar algo."),("Ámbitos","Espacios, ambiente, salud, redes."),("Criterios","Me afecta, concreto, posible."),("Formular","Quién, qué, dónde.")),
 G(("Comunidad","Grupo que comparte un lugar."),("Problema","Situación que hay que mejorar."),("Concreto","Que se puede describir con ejemplos."),("Formular","Expresar con claridad.")),
 ["¿Cómo se llama el plan para mejorar algo de la comunidad con una acción concreta?","¿Un problema se escribe como una situación o como una solución? Respondé situación o solución.","¿Hay que elegir un problema que se pueda describir con un ejemplo? Respondé sí o no.","¿Qué criterio pregunta si lo vivo yo o gente cercana: «me afecta» o «es concreto»?"],
 [["proyecto","proyecto de participacion","proyecto de participación","un proyecto"],["situacion","situación","una situacion","una situación"],["si","sí"],["me afecta","afecta"]],
 {"incompleto":"Solución. Concreto.","solo":"Las plazas de mi ciudad tienen poca luz y de noche nadie pasa por ahí.","carpeta":["Proyecto.","Situación.","Sí.","Me afecta."]})
B2=NV("Vas a investigar un problema con fuentes confiables y con la voz de las personas afectadas.",["Tipos de fuentes","Primarias y secundarias","Fuentes confiables","Escuchar y anotar"],[
 S(1,"Tipos de fuentes",[T("Fuentes que podés usar",["Tipo","Ejemplo"],[["Observación","Mirar y anotar lo que pasa en el lugar"],["Encuesta","Preguntas cortas a muchas personas"],["Entrevista","Conversar con una persona afectada o experta"],["Documentos","Noticias, informes, leyes y datos oficiales"]])]),
 S(1,"Primarias y secundarias",[D("Fuente primaria","Información que obtenés vos mismo: observaciones, encuestas, entrevistas."),D("Fuente secundaria","Información que ya reunió otra persona: noticias, informes, estadísticas."),P("Un buen proyecto combina las dos.")]),
 S(2,"Fuentes confiables",[T("Cómo saber si una fuente sirve",["Pregunta","Qué mirar"],[["¿Quién lo dice?","Persona u organismo identificable"],["¿Cuándo?","Fecha reciente"],["¿Con qué datos?","Cifras y de dónde salen"],["¿Hay otra que coincida?","Contrastar con otra fuente"]])]),
 S(2,"Escuchar y anotar",[P("Las personas afectadas conocen el problema mejor que nadie: escucharlas da ideas y fuerza al proyecto. Cada dato se anota con su fuente (quién, dónde y cuándo) para poder citarlo."),IM("Dato + fuente","Un dato sin fuente no convence a nadie.")])],
 {"titulo":"evaluar","planteo":"Un video anónimo dice que «el 90 % de las plazas es peligroso». ¿Sirve como fuente?","pasos":["No se sabe quién lo dice ni cuándo.","No explica de dónde sale el 90 %.","No sirve solo: hay que contrastarlo con otra fuente."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Una encuesta que hacés vos es una fuente ___ .","Un dato sin ___ no convence."]},
 {"titulo":"tu turno","planteo":"Escribí tres preguntas para una encuesta o entrevista sobre tu problema."},
 {"titulo":"Contrastá siempre","texto":"Si dos fuentes distintas coinciden, el dato es más confiable."},
 ["Usar una sola fuente.","Anotar un dato sin saber de dónde sale."],
 RS(("Tipos","Observación, encuesta, entrevista, documentos."),("Primaria","La obtenés vos."),("Confiable","Autor, fecha y datos."),("Dato","Siempre con su fuente.")),
 G(("Fuente","Origen de la información."),("Encuesta","Preguntas a muchas personas."),("Contrastar","Comparar fuentes."),("Estadística","Datos en cifras.")),
 ["¿Cómo se llama la información que obtenés vos mismo con una encuesta?","¿Un dato sin fuente convence? Respondé sí o no.","¿Comparar varias fuentes para ver si coinciden es contrastar? Respondé sí o no.","¿Una entrevista que hacés vos es una fuente primaria o secundaria?"],
 [["fuente primaria","primaria","una fuente primaria"],["no"],["si","sí"],["primaria","fuente primaria"]],
 {"incompleto":"Primaria. Fuente.","solo":"¿Qué es lo que más te molesta del lugar? ¿Cuántas veces por semana lo usás? ¿Qué cambiarías primero?","carpeta":["Fuente primaria.","No.","Sí.","Primaria."]})
B3=NV("Vas a diseñar una propuesta con objetivo, acciones, responsables, recursos y forma de medir resultados.",["Objetivo","Acciones y responsables","Recursos y tiempos","Cómo medir resultados"],[
 S(1,"Objetivo",[D("Objetivo","Lo que se quiere lograr con la propuesta; debe ser claro, posible y medible."),P("Ejemplo: «Lograr que la plaza tenga luz en todos sus caminos antes de fin de año».")]),
 S(1,"Acciones y responsables",[T("Plan de acción",["Qué","Cómo se define"],[["Acción","Paso concreto que se va a hacer"],["Responsable","Quién se encarga de cada paso"],["Aliados","Quiénes pueden ayudar"],["Destinatarios","A quién beneficia"]])]),
 S(2,"Recursos y tiempos",[P("Se listan los recursos necesarios (personas, materiales, permisos, dinero) y un cronograma con fechas. Una propuesta realista es mejor que una enorme que no se puede cumplir.")]),
 S(2,"Cómo medir resultados",[T("Indicadores",["Si el objetivo es…","Se puede medir…"],[["Más luz en la plaza","Cantidad de luminarias nuevas"],["Menos basura en el arroyo","Kilos recogidos por mes"],["Más deporte","Personas que participan por semana"]])])],
 {"titulo":"armar","planteo":"Objetivo: reducir la basura en un arroyo. ¿Qué acción, responsable e indicador convienen?","pasos":["Acción: una jornada mensual de limpieza.","Responsable: un equipo de cinco jóvenes con apoyo de las autoridades locales.","Indicador: kilos de basura recogidos por mes."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que se quiere lograr con la propuesta es el ___ .","Quien se encarga de cada paso es el ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí el objetivo de tu propuesta y tres acciones con su responsable."},
 {"titulo":"Pequeño y posible","texto":"Una acción chica que se cumple vale más que una enorme que queda en el papel."},
 ["Escribir objetivos vagos como «mejorar todo».","Olvidarse de los recursos y las fechas."],
 RS(("Objetivo","Claro, posible y medible."),("Acciones","Pasos con responsables."),("Recursos","Personas, materiales, permisos."),("Indicadores","Cómo medir resultados.")),
 G(("Cronograma","Calendario de las acciones."),("Responsable","Quien se encarga de un paso."),("Indicador","Dato que mide un resultado."),("Destinatarios","Quienes se benefician.")),
 ["¿Cómo se llama lo que se quiere lograr con la propuesta?","¿Cómo se llama el calendario con las fechas de las acciones?","¿Conviene que un objetivo sea medible? Respondé sí o no.","¿Cómo se llama el dato que sirve para medir un resultado?"],
 [["objetivo","el objetivo"],["cronograma","el cronograma"],["si","sí"],["indicador","el indicador"]],
 {"incompleto":"Objetivo. Responsable.","solo":"Objetivo: que la plaza tenga luz en todos sus caminos. Acciones: pedir una reunión, juntar firmas y proponer un plan.","carpeta":["Objetivo.","Cronograma.","Sí.","Indicador."]})
B4=NV("Vas a presentar tu propuesta, escuchar devoluciones y mejorarla.",["Estructura de la presentación","Comunicar claro","A quién presentarla","Devoluciones y evaluación"],[
 S(1,"Estructura de la presentación",[T("Qué incluye",["Parte","Contenido"],[["Problema","Qué ocurre, a quién afecta, con datos"],["Propuesta","Objetivo y acciones"],["Plan","Responsables, recursos y tiempos"],["Pedido","Qué se solicita y a quién"]])]),
 S(1,"Comunicar claro",[P("Una buena presentación es breve, ordenada y usa ejemplos y datos con su fuente. Se ensaya en voz alta y se cuida el tiempo.")]),
 S(2,"A quién presentarla",[PN("En la Argentina, desde 2012 se puede votar a partir de los 16 años, y las propuestas juveniles también se presentan ante autoridades locales y organizaciones de la comunidad.","En varios países se puede votar desde los 16 años, y las propuestas juveniles también se presentan ante autoridades locales y organizaciones de la comunidad.")]),
 S(2,"Devoluciones y evaluación",[P("Una devolución es una opinión sobre lo presentado. Se escucha sin interrumpir, se pregunta para entender y se decide qué ajustar. Al final se evalúa qué salió bien, qué se aprendió y qué se mejoraría."),IM("Críticas que ayudan","Una devolución sirve cuando se convierte en una mejora.")])],
 {"titulo":"recibir","planteo":"Alguien dice: «Tu plan no tiene fechas». ¿Cómo responder?","pasos":["Escuchar sin interrumpir.","Reconocer que falta el cronograma.","Agregar las fechas y volver a presentarlo."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que se solicita a quien puede decidir es el ___ .","Una opinión sobre lo presentado es una ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí en cuatro frases tu presentación: problema, propuesta, plan y pedido."},
 {"titulo":"Ensayá en voz alta","texto":"Practicar tu presentación te ayuda a ajustar el tiempo y a tener más confianza."},
 ["Leer todo sin mirar a quien escucha.","Tomar una devolución como un ataque."],
 RS(("Partes","Problema, propuesta, plan, pedido."),("Comunicar","Breve y con datos."),("Devolución","Escuchar y mejorar."),("Evaluar","Qué salió bien y qué ajustar.")),
 G(("Devolución","Opinión sobre lo presentado."),("Pedido","Lo que se solicita."),("Evaluar","Revisar lo hecho."),("Autoridades locales","Quienes gobiernan una ciudad o zona.")),
 ["¿Cómo se llama la opinión que recibís sobre lo que presentaste?","¿Cómo se llama lo que se solicita a quien puede decidir?","¿Conviene escuchar una devolución sin interrumpir? Respondé sí o no.","¿Una devolución sirve cuando se convierte en una mejora? Respondé sí o no."],
 [["devolucion","devolución","una devolucion","una devolución"],["pedido","el pedido"],["si","sí"],["si","sí"]],
 {"incompleto":"Pedido. Devolución.","solo":"Hay un problema de luz en la plaza que afecta a muchos. Propongo una jornada de reclamos. Ya hay un plan con fechas. Pido una reunión con las autoridades.","carpeta":["Devolución.","Pedido.","Sí.","Sí."]})
ACT10={"1":[{"t":"classify","p":"¿Es un problema o una solución?","o":{"elementos":["Cruzar la avenida es peligroso","Poner un semáforo","Falta luz en la plaza","Instalar más faroles"],"categorias":["Problema","Solución"]},"r":{"categorias":{"Cruzar la avenida es peligroso":"Problema","Poner un semáforo":"Solución","Falta luz en la plaza":"Problema","Instalar más faroles":"Solución"}},"e":"El problema describe la situación; la solución, lo que se hace."},FB("Un problema se escribe como una ___ , no como una solución.",[["situacion","situación"]],"Así se pueden pensar varias soluciones.")],
 "2":[{"t":"matching","p":"Uní cada fuente con su ejemplo.","o":{"izquierda":["Observación","Encuesta","Entrevista","Documentos"],"derecha":["Mirar y anotar en el lugar","Preguntas a muchas personas","Conversar con una persona","Informes y estadísticas"]},"r":{"pares":{"Observación":"Mirar y anotar en el lugar","Encuesta":"Preguntas a muchas personas","Entrevista":"Conversar con una persona","Documentos":"Informes y estadísticas"}},"e":"Cada fuente, su ejemplo."},MS("¿Qué conviene mirar para saber si una fuente es confiable?",["Quién lo dice","La fecha","Cuántos likes tiene","De dónde salen los datos"],["Quién lo dice","La fecha","De dónde salen los datos"],"Los likes no prueban que un dato sea cierto.")],
 "3":[TT("Tocá lo que vuelve medible el objetivo: «Plantar cien árboles antes de diciembre».",["Plantar","cien","árboles","antes","de","diciembre."],[1,5],"Una cantidad y una fecha lo hacen medible."),FB("El dato que sirve para medir un resultado es el ___ .",[["indicador"]],"Mide si el objetivo se logró.")],
 "4":[{"t":"ordering","p":"Ordená las partes de una presentación.","o":["Pedido","Problema","Plan","Propuesta"],"r":{"orden":["Problema","Propuesta","Plan","Pedido"]},"e":"Primero el problema, al final lo que se pide."},MC("Ante una devolución conviene…",["Escuchar y decidir qué ajustar","Interrumpir","Ignorarla","Tomarla como ataque"],"Escuchar y decidir qué ajustar","Sirve para mejorar.")]}
EX10=[[1,MC("¿Cuál es un problema bien formulado?",["Cruzar la avenida es peligroso para quienes van a pie","Hay que poner un semáforo","Arreglar todo","Que nadie se queje"],"Cruzar la avenida es peligroso para quienes van a pie","Describe una situación, no una solución.")],
 [1,VF("Un problema concreto se puede describir con un ejemplo.","Verdadero","Eso lo hace abordable.")],
 [1,MC("Un proyecto de participación parte de…",["Un problema real","Una queja sin datos","Una solución impuesta","Una moda"],"Un problema real","Se parte de lo que ocurre.")],
 [2,MC("Una encuesta propia es una fuente…",["Primaria","Secundaria","Anónima","Falsa"],"Primaria","La obtiene quien investiga.")],
 [2,VF("Contrastar fuentes aumenta la confianza en un dato.","Verdadero","Si coinciden, es más confiable.")],
 [2,MS("Para evaluar una fuente conviene mirar…",["Quién lo dice","La fecha","El color de la página","De dónde salen los datos"],["Quién lo dice","La fecha","De dónde salen los datos"],"El color no dice nada.")],
 [3,MC("Un objetivo bien formulado es…",["Claro, posible y medible","Enorme y vago","Sin fechas","Solo un deseo"],"Claro, posible y medible","Permite saber si se logró.")],
 [3,FB("El calendario con las fechas de las acciones es el ___ .",[["cronograma"]],"Ordena los tiempos.")],
 [3,VF("Una propuesta realista vale más que una enorme que no se cumple.","Verdadero","Lo posible se concreta.")],
 [4,MC("El «pedido» de una presentación es…",["Lo que se solicita a quien puede decidir","Un resumen del problema","Un dato","La despedida"],"Lo que se solicita a quien puede decidir","Dice qué se pide y a quién.")],
 [4,VF("Una devolución sirve cuando se convierte en una mejora.","Verdadero","Ese es su valor.")],
 [4,MC("Ante una devolución conviene…",["Escuchar y decidir qué ajustar","Interrumpir","Ignorarla","Tomarla como ataque"],"Escuchar y decidir qué ajustar","Permite mejorar.")],
 [4,MS("¿Cuáles son partes de una presentación?",["Problema","Propuesta","Plan","Chismes"],["Problema","Propuesta","Plan"],"Y también el pedido.")]]
M10={"subject_id":SID,"tema":10,"practica":"Práctica general: una propuesta de participación juvenil","examen_titulo":"Nivel jefe: una propuesta de participación juvenil","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT10,"examen":EX10}
os.makedirs(os.path.join(AQUI,"mision-10"),exist_ok=True)
M10["act"]["5"]=PRACTICA[10]
json.dump(M10,open(os.path.join(AQUI,"mision-10","mision-10.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={1:"2a8a5b8b-dd13-47b0-99c6-3e787cea9d0b",2:"56cac442-b7ef-4e9c-a677-b450c0214232",3:"4dff95f7-75ec-4d87-9d7d-e9b7908455aa",4:"8dbe3585-8d24-4fae-8c6c-222e092a56f8"}
TIT={1:"Elijo un problema que me afecta",2:"Investigo y consulto fuentes",3:"Diseño una propuesta",4:"Presento y recibo devoluciones"}
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
 RET("¿Un problema se escribe como situación o como solución?",6,"Situación","🎯","ELEGIR UN PROBLEMA","que me afecta",["Desafío: ¿un problema se escribe como situación o como solución? Seis segundos.","Situación.","Hoy: *elegir un problema que me afecta*."]),
 DEF("Proyecto de participación","Plan para mejorar la comunidad","🌱",["Un *proyecto de participación* es un plan para mejorar algo de la comunidad.","Lo piensan y lo presentan jóvenes."]),
 TB("CRITERIOS",["Criterio","Pregunta"],[["Me afecta","¿Lo vivo?"],["Concreto","¿Tiene ejemplo?"],["Posible","¿Hay acción?"],["Con datos","¿Hay información?"]],["Cómo elegir un problema.","*Me afecta*: ¿lo vivo?","*Concreto*: ¿tiene ejemplo?","*Posible*: ¿hay una acción?","Y *con datos*: ¿hay información?"]),
 CL([("PROBLEMA","⚠️"),("SOLUCIÓN","✅")],[("Falta luz",0),("Poner faroles",1),("Calle peligrosa",0),("Hacer una ronda",1)],["¿Problema o solución?","*Falta luz* y *calle peligrosa*: problemas.","*Poner faroles* y *hacer una ronda*: soluciones."]),
 Q("Un problema bien formulado describe…",["Una situación","Una solución","Un deseo"],0,["Te toca: un problema bien formulado describe…","¿Una situación, una solución o un deseo?","Una *situación*."]),
 ER([("Elegir un problema enorme","Elegir uno concreto"),("Escribir una solución","Describir la situación")],["Errores típicos.","Elegir un problema *enorme*.","Y escribir una *solución* en vez del problema."]),
 RES(["Repasemos.","Un *proyecto de participación* mejora algo de la comunidad.","Se elige un problema que *me afecta*.","Tiene que ser *concreto* y posible.","Y se escribe como una *situación*.","¡Clase terminada! Ahora, *a practicar*."],[["PROYECTO","mejorar la comunidad"],["CRITERIOS","afecta, concreto"],["PROBLEMA","una situación"],["SIGUE","investigar"]])],
2:[
 NOT("INVESTIGAR","Un dato sin fuente","No convence a nadie","🔎","INVESTIGO Y CONSULTO","fuentes",["Noticia: un dato sin fuente no convence a nadie.","Hay que investigar bien.","Hoy: *investigar y consultar fuentes*."]),
 TB("TIPOS DE FUENTES",["Tipo","Ejemplo"],[["Observación","Mirar y anotar"],["Encuesta","Muchas personas"],["Entrevista","Una persona"],["Documentos","Informes y datos"]],["Tipos de fuentes.","La *observación*: mirar y anotar.","La *encuesta*: a muchas personas.","La *entrevista*: a una persona.","Y los *documentos*."]),
 DEF("Fuente primaria","La obtenés vos mismo","📝",["Una *fuente primaria* la obtenés vos mismo.","Por ejemplo, una encuesta o una entrevista."]),
 DEF("Fuente secundaria","Ya la reunió otra persona","📚",["Una *fuente secundaria* ya la reunió otra persona.","Por ejemplo, una noticia o un informe."]),
 CL([("PRIMARIA","📝"),("SECUNDARIA","📚")],[("Mi encuesta",0),("Un informe",1),("Mi entrevista",0),("Una noticia",1)],["¿Primaria o secundaria?","*Mi encuesta* y *mi entrevista*: primarias.","*Un informe* y *una noticia*: secundarias."]),
 Q("Un dato sin fuente…",["No convence","Convence siempre","Es oficial"],0,["Te toca: un dato sin fuente.","¿No convence, convence siempre o es oficial?","*No convence*."]),
 ER([("Usar una sola fuente","Contrastar varias"),("Anotar sin la fuente","Anotar dato y fuente")],["Errores típicos.","Usar *una sola fuente*.","Y anotar un dato *sin su fuente*."]),
 RES(["Repasemos.","Hay varios *tipos* de fuentes.","La *primaria* la obtengo yo.","La *secundaria* ya existe.","Y todo dato va con su *fuente*.","¡Clase terminada! Ahora, *a practicar*."],[["TIPOS","observar, preguntar"],["PRIMARIA","la obtengo yo"],["SECUNDARIA","ya existe"],["DATO","con su fuente"]])],
3:[
 RET("¿Cómo se llama lo que se quiere lograr con la propuesta?",5,"Objetivo","🎯","DISEÑO","una propuesta",["Desafío: ¿cómo se llama lo que se quiere lograr con la propuesta? Cinco segundos.","Objetivo.","Hoy: *diseñar una propuesta*."]),
 DEF("Objetivo","Lo que se quiere lograr","🎯",["El *objetivo* es lo que se quiere lograr.","Debe ser claro, posible y medible."]),
 PA("PLAN DE ACCIÓN",[("Definir acciones","📌"),("Elegir responsables","👥"),("Listar recursos","🧰"),("Poner fechas","📅")],["Plan de acción.","Definir *acciones*.","Elegir *responsables*.","Listar *recursos*.","Y poner *fechas*."]),
 TB("INDICADORES",["Objetivo","Se mide con"],[["Más luz","Luminarias nuevas"],["Menos basura","Kilos por mes"],["Más deporte","Personas por semana"]],["Cómo medir resultados.","*Más luz*: luminarias nuevas.","*Menos basura*: kilos por mes.","Y *más deporte*: personas por semana."]),
 Q("El calendario con las fechas es el…",["Cronograma","Indicador","Pedido"],0,["Te toca: el calendario con las fechas.","¿Cronograma, indicador o pedido?","El *cronograma*."]),
 ER([("Objetivos vagos","Claros y medibles"),("Sin fechas","Con cronograma")],["Errores típicos.","Escribir objetivos *vagos*.","Y olvidar las *fechas*."]),
 RES(["Repasemos.","El *objetivo* es claro y medible.","Las *acciones* tienen responsables.","Se listan *recursos* y fechas.","Y un *indicador* mide el resultado.","¡Clase terminada! Ahora, *a practicar*."],[["OBJETIVO","claro y medible"],["ACCIONES","con responsables"],["RECURSOS","y fechas"],["INDICADOR","mide resultados"]])],
4:[
 RET("¿Cómo se llama la opinión que recibís sobre lo que presentaste?",6,"Devolución","🗣️","PRESENTO","y recibo devoluciones",["Desafío: ¿cómo se llama la opinión que recibís sobre lo que presentaste? Seis segundos.","Devolución.","Hoy: *presentar y recibir devoluciones*."]),
 TB("QUÉ INCLUYE",["Parte","Contenido"],[["Problema","Con datos"],["Propuesta","Objetivo y acciones"],["Plan","Responsables y fechas"],["Pedido","Qué se solicita"]],["Una presentación incluye cuatro partes.","El *problema*, con datos.","La *propuesta*.","El *plan*.","Y el *pedido*."]),
 DEF("Devolución","Opinión sobre lo presentado","💬",["Una *devolución* es una opinión sobre lo presentado.","Sirve cuando se convierte en una mejora."]),
 CMP(("DEFENDERSE","Tomarlo como ataque","🛡️"),("ESCUCHAR","Usarlo para mejorar","👂"),"vs",["Dos actitudes.","*Defenderse* cierra la conversación.","*Escuchar* ayuda a mejorar."]),
 CL([("AYUDA","✅"),("NO AYUDA","❌")],[("Escuchar",0),("Interrumpir",1),("Preguntar",0),("Ignorar",1)],["¿Ayuda o no ayuda?","*Escuchar* y *preguntar*: ayudan.","*Interrumpir* e *ignorar*: no ayudan."]),
 Q("Ante una devolución conviene…",["Escuchar y ajustar","Ignorarla","Discutir"],0,["Te toca: ante una devolución.","¿Escuchar y ajustar, ignorarla o discutir?","*Escuchar y ajustar*."]),
 RES(["Repasemos.","Una presentación tiene *problema*, propuesta, plan y pedido.","Se comunica *breve* y con datos.","Las *devoluciones* ayudan a mejorar.","Y al final se *evalúa* el proyecto.","¡Clase terminada! Ahora, *a practicar*."],[["PARTES","problema, propuesta"],["COMUNICAR","breve y con datos"],["DEVOLUCIÓN","escuchar y mejorar"],["EVALUAR","qué ajustar"]])]}
for n,es in CLS.items():
    json.dump({"sin_variante":True,"slug":f"ciud1-m10-n{n}","step_id":STEPS[n],"materia":"Ciudadanía I","titulo":TIT[n],"sub":f"Ciudadanía I · Misión 10 · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"ciud1-m10-n{n}.json"),"w"),ensure_ascii=False)
print("ok")
