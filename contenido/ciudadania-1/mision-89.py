# -*- coding: utf-8 -*-
"""Ciudadanía I y Ciudadanía I Argentina · Misiones 8 y 9 (VARIANTE)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
def NE(b,**k): b=dict(b); b["neutro"]=k; return b
def PN(a,b): return {"tipo":"parrafo","texto":a,"neutro":{"texto":b}}

FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,ref,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":ref,"e":e,**k}
SID = "a549d16a-c872-4df7-b243-e4b508bd8668"
# ============ MISIÓN 8: PREJUICIOS Y DISCRIMINACIÓN ============
A1=NV("Vas a explicar cómo un prejuicio se convierte en estereotipo y en discriminación.",["Prejuicio","Estereotipo","Discriminación","Cómo se pasa de uno a otro"],[
 S(1,"Prejuicio",[D("Prejuicio","Opinión o actitud negativa hacia una persona o grupo, formada antes de conocerlos y sin pruebas."),P("Los prejuicios se aprenden en la familia, en los medios, en la escuela y en la calle.")]),
 S(1,"Estereotipo",[D("Estereotipo","Imagen simplificada y repetida sobre un grupo, que se aplica a todas las personas que lo integran."),P("Ejemplo: «los adolescentes solo piensan en el celular». Ignora que cada persona es distinta.")]),
 S(2,"Discriminación",[D("Discriminación","Trato desigual e injusto hacia una persona o grupo por su origen, color de piel, religión, género, discapacidad, aspecto o condición social."),P("Se puede discriminar con palabras, con gestos, con burlas, con exclusiones o con leyes y reglas injustas.")]),
 S(2,"Cómo se pasa de uno a otro",[T("De la idea al hecho",["Paso","Qué ocurre"],[["Prejuicio","Pienso mal de alguien sin conocerlo"],["Estereotipo","Lo repito como si valiera para todos"],["Discriminación","Lo trato peor o lo dejo afuera"]])])],
 {"titulo":"identificar","planteo":"Un grupo no deja jugar a un compañero porque «los de su barrio son problemáticos». ¿Qué hay?","pasos":["Hay una idea formada sin conocerlo: prejuicio.","Se aplica a todo un grupo: estereotipo.","Lo dejan afuera: discriminación."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La opinión negativa formada sin conocer es un ___ .","El trato desigual e injusto es la ___ ."]},
 {"titulo":"tu turno","planteo":"Pensá un estereotipo que escuchaste y explicá por qué es injusto."},
 {"titulo":"Conocer antes","texto":"Antes de opinar sobre alguien, conocelo."},
 ["Creer que los prejuicios son «inocentes».","Pensar que discriminar es solo insultar."],
 RS(("Prejuicio","Opinión sin conocer."),("Estereotipo","Imagen simplificada."),("Discriminación","Trato desigual e injusto."),("Camino","De la idea al hecho.")),
 G(("Prejuicio","Juicio previo sin pruebas."),("Estereotipo","Imagen simplificada de un grupo."),("Discriminar","Tratar peor por una característica."),("Exclusión","Dejar afuera.")),
 ["¿Cómo se llama la opinión negativa formada antes de conocer?","¿Cómo se llama la imagen simplificada que se aplica a todo un grupo?","¿Cómo se llama el trato desigual e injusto hacia una persona?","¿Se puede discriminar con burlas? Respondé sí o no."],
 [["prejuicio","un prejuicio","el prejuicio"],["estereotipo","un estereotipo","el estereotipo"],["discriminacion","discriminación","la discriminacion","la discriminación"],["si","sí"]],
 {"incompleto":"Prejuicio. Discriminación.","solo":"Estereotipo: «todos los jóvenes son iguales». Es injusto porque cada persona es distinta.","carpeta":["Prejuicio.","Estereotipo.","Discriminación.","Sí."]})
A2=NV("Vas a distinguir racismo, xenofobia, sexismo y otras formas de exclusión y entender sus consecuencias.",["Racismo","Xenofobia","Otras formas","Consecuencias"],[
 S(1,"Racismo",[D("Racismo","Creencia de que unas personas valen más que otras por su color de piel, su origen étnico o sus rasgos físicos."),P("No hay bases científicas: todas las personas pertenecen a una misma especie.")]),
 S(1,"Xenofobia",[D("Xenofobia","Rechazo, miedo o desprecio hacia las personas extranjeras o migrantes."),P("Se expresa en burlas, en negarles trabajo o vivienda, o en culparlos de los problemas de un país.")]),
 S(2,"Otras formas",[T("Formas de discriminación",["Tipo","Ejemplo"],[["Sexismo","Tratar peor por ser mujer, varón o por el género"],["Capacitismo","Subestimar a personas con discapacidad"],["Religiosa","Burlarse de una creencia"],["Por apariencia","Excluir por el aspecto o el cuerpo"],["Clasismo","Despreciar a alguien por su nivel económico"]])]),
 S(2,"Consecuencias",[P("Discriminar daña la salud, la autoestima y las oportunidades de quien lo sufre. También empobrece a la comunidad, porque pierde la riqueza de la diversidad.")])],
 {"titulo":"clasificar","planteo":"Rechazar a una persona porque nació en otro país: ¿qué tipo de discriminación es?","pasos":["Se rechaza por ser extranjera.","Es una xenofobia.","Daña a quien la sufre."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Creer que algunas personas valen más por su color de piel es ___ .","El rechazo a las personas extranjeras es la ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres formas de discriminación y una acción para evitar cada una."},
 {"titulo":"Diversidad","texto":"La diversidad no divide: suma."},
 ["Creer que el racismo tiene base científica.","Pensar que la discriminación afecta solo a quien la sufre."],
 RS(("Racismo","Por origen o color."),("Xenofobia","Rechazo al extranjero."),("Otras","Sexismo, capacitismo, clasismo."),("Consecuencias","Daño y pérdida de diversidad.")),
 G(("Racismo","Jerarquizar por rasgos físicos."),("Xenofobia","Rechazo a extranjeros."),("Capacitismo","Discriminar por discapacidad."),("Diversidad","Variedad de personas.")),
 ["¿Cómo se llama el rechazo hacia las personas extranjeras o migrantes?","¿Cómo se llama discriminar por el color de piel o el origen étnico?","¿Discriminar puede dañar la salud y la autoestima? Respondé sí o no.","¿Cómo se llama discriminar por la situación económica: clasismo o xenofobia?"],
 [["xenofobia","la xenofobia"],["racismo","el racismo"],["si","sí"],["clasismo","el clasismo"]],
 {"incompleto":"Racismo. Xenofobia.","solo":"Xenofobia: rechazar a alguien por haber nacido en otro país.","carpeta":["Xenofobia.","Racismo.","Sí.","Clasismo."]})
A3=NV("Vas a explicar qué dicen las leyes contra la discriminación y qué derechos protegen.",["Igualdad y no discriminación","Normas internacionales","Normas nacionales","Qué hacen"],[
 S(1,"Igualdad y no discriminación",[P("La igualdad ante la ley y la no discriminación son principios de los derechos humanos. El Estado debe tratar a todas las personas con igualdad y sancionar los actos discriminatorios.")]),
 S(1,"Normas internacionales",[T("Instrumentos",["Instrumento","Qué establece"],[["Declaración Universal (1948)","Todos somos iguales en dignidad y derechos"],["Convención contra la discriminación racial (1965)","Condena el racismo"],["Convención contra la discriminación de la mujer (1979)","Igualdad de las mujeres"],["Convención sobre los Derechos de las Personas con Discapacidad (2006)","Igualdad y accesibilidad"]])]),
 S(2,"Normas nacionales",[PN("En la Argentina, una ley antidiscriminatoria de 1988 sanciona a quien discrimina o incita al odio por motivos de raza, religión, nacionalidad o ideología, entre otros. La Constitución Nacional reconoce además la igualdad ante la ley.","Muchos países tienen leyes antidiscriminatorias que sancionan actos de discriminación y de incitación al odio. Las constituciones, además, reconocen la igualdad ante la ley.")]),
 S(2,"Qué hacen",[P("Estas normas permiten denunciar, reparar el daño y prevenir. También orientan políticas públicas: educación, accesibilidad y campañas de respeto.")])],
 {"titulo":"relacionar","planteo":"¿Para qué sirve una ley contra la discriminación?","pasos":["Establece que discriminar está mal.","Permite denunciar y sancionar.","Protege a quienes más lo necesitan."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La Declaración Universal es de ___ .","Una norma que sanciona la discriminación es una ley ___ ."]},
 {"titulo":"tu turno","planteo":"Explicá por qué no alcanza con que la discriminación sea «mal vista»: ¿para qué hace falta que sea ilegal?"},
 {"titulo":"Ley y respeto","texto":"La ley protege, pero el respeto empieza en lo cotidiano."},
 ["Pensar que una ley alcanza por sí sola.","Creer que la discriminación no se puede denunciar."],
 RS(("Principio","Igualdad y no discriminación."),("Internacional","Declaraciones y convenciones."),("Nacional","Leyes y constitución."),("Función","Prevenir y sancionar.")),
 G(("Antidiscriminatoria","Que sanciona la discriminación."),("Incitar al odio","Empujar a odiar."),("Accesibilidad","Posibilidad de usar un lugar o servicio."),("Convención","Tratado sobre un tema.")),
 ["¿Qué principio dice que todas las personas deben ser tratadas por igual: la igualdad o el privilegio?","¿Cómo se llama la ley que sanciona la discriminación: antidiscriminatoria o impositiva?","¿La discriminación se puede denunciar? Respondé sí o no.","¿La Declaración Universal dice que todos somos iguales en dignidad? Respondé sí o no."],
 [["igualdad","la igualdad"],["antidiscriminatoria","ley antidiscriminatoria","una ley antidiscriminatoria"],["si","sí"],["si","sí"]],
 {"incompleto":"Igualdad. Antidiscriminatoria.","solo":"Hace falta una ley para poder denunciar y sancionar a quien discrimina.","carpeta":["La igualdad.","Antidiscriminatoria.","Sí.","Sí."]})
A4=NV("Vas a explicar cómo actuar ante la discriminación: como víctima, como testigo y como comunidad.",["Si me pasa a mí","Si lo veo","Qué no hacer","Entre todos"],[
 S(1,"Si me pasa a mí",[T("Qué hacer",["Paso","Qué implica"],[["Frenar","Decir con calma que no está bien"],["Guardar pruebas","Capturas, mensajes, fechas"],["Contar","Hablar con una persona adulta de confianza"],["Denunciar","Acudir a la escuela o a un organismo"]])]),
 S(1,"Si lo veo",[P("Quien presencia una situación puede ser <b>aliado</b>: acompañar a la víctima, no reírse, cortar la burla, avisar a un adulto y no compartir el contenido ofensivo. Mirar sin hacer nada ayuda al agresor.")]),
 S(2,"Qué no hacer",[T("Evitá",["Conducta","Por qué daña"],[["Reírse o aplaudir","Refuerza al que agrede"],["Compartir memes ofensivos","Multiplica el daño"],["Callar «para evitar problemas»","Deja sola a la víctima"],["Responder con más violencia","Agrava el conflicto"]])]),
 S(2,"Entre todos",[PN("Las escuelas y las comunidades pueden prevenir con educación, reglas de convivencia claras y espacios donde denunciar. En la Argentina funcionan líneas de ayuda y organismos que reciben denuncias por discriminación y violencia.","Las escuelas y las comunidades pueden prevenir con educación, reglas de convivencia claras y espacios donde denunciar. En muchos países funcionan líneas de ayuda y organismos que reciben denuncias por discriminación y violencia.")])],
 {"titulo":"aplicar","planteo":"En un chat de curso, alguien se burla de un compañero por su origen. ¿Qué podés hacer?","pasos":["No reír ni compartir.","Decir que no está bien y acompañar al compañero.","Avisar a un adulto y guardar capturas."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Quien acompaña a la víctima y frena la burla es un ___ .","Antes de denunciar conviene guardar las ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un plan de cinco pasos para actuar si vieras una situación de discriminación."},
 {"titulo":"Ser aliado","texto":"Mirar sin hacer nada es elegir un lado."},
 ["Pensar que reírse no hace daño.","Creer que callar protege a la víctima."],
 RS(("Si me pasa","Frenar, guardar pruebas, contar."),("Si lo veo","Ser aliado."),("No hacer","Reírse, compartir."),("Comunidad","Prevenir y denunciar.")),
 G(("Aliado","Quien acompaña a la víctima."),("Prueba","Dato que respalda lo ocurrido."),("Denunciar","Informar a quien corresponde."),("Prevención","Evitar que ocurra.")),
 ["¿Cómo se llama quien acompaña a la víctima y frena la burla?","¿Qué conviene guardar antes de denunciar: pruebas o rumores?","¿Compartir un meme ofensivo multiplica el daño? Respondé sí o no.","¿Hablar con una persona adulta de confianza ayuda? Respondé sí o no."],
 [["aliado","un aliado","el aliado"],["pruebas","las pruebas"],["si","sí"],["si","sí"]],
 {"incompleto":"Aliado. Pruebas.","solo":"No río, acompaño al compañero, aviso a un adulto y guardo capturas.","carpeta":["Aliado.","Pruebas.","Sí.","Sí."]})
ACT8={"1":[{"t":"ordering","p":"Ordená de la idea al hecho.","o":["Discriminación","Prejuicio","Estereotipo"],"r":{"orden":["Prejuicio","Estereotipo","Discriminación"]},"e":"Primero se piensa, luego se repite, luego se actúa."},FB("La imagen simplificada que se aplica a todo un grupo es un ___ .",[["estereotipo"]],"Estereotipo.")],
 "2":[{"t":"matching","p":"Uní cada forma de discriminación con su descripción.","o":{"izquierda":["Racismo","Xenofobia","Capacitismo","Clasismo"],"derecha":["Por color o origen étnico","Rechazo a extranjeros","Subestimar a personas con discapacidad","Despreciar por nivel económico"]},"r":{"pares":{"Racismo":"Por color o origen étnico","Xenofobia":"Rechazo a extranjeros","Capacitismo":"Subestimar a personas con discapacidad","Clasismo":"Despreciar por nivel económico"}},"e":"Cada forma, su descripción."},VF("El racismo tiene bases científicas.","Falso","Todas las personas son una misma especie.")],
 "3":[MS("¿Qué permiten las leyes contra la discriminación?",["Denunciar","Sancionar","Reparar el daño","Discriminar con permiso"],["Denunciar","Sancionar","Reparar el daño"],"Nunca permiten discriminar."),VF("Una ley alcanza por sí sola para eliminar la discriminación.","Falso","También hace falta educación y respeto cotidiano.")],
 "4":[{"t":"classify","p":"¿Ayuda o daña?","o":{"elementos":["Acompañar a la víctima","Reírse de la burla","Guardar capturas","Compartir un meme ofensivo"],"categorias":["Ayuda","Daña"]},"r":{"categorias":{"Acompañar a la víctima":"Ayuda","Reírse de la burla":"Daña","Guardar capturas":"Ayuda","Compartir un meme ofensivo":"Daña"}},"e":"Ser aliado ayuda."},TT("Tocá a quienes ayudan: «El aliado y la persona adulta de confianza ayudan a frenar la discriminación».",["El","aliado","y","la","persona","adulta","de","confianza","ayudan","a","frenar","la","discriminación"],[1,5],"El aliado y la persona adulta.")],
 "5":[MC("Relámpago. La opinión negativa formada sin conocer es un…",["Prejuicio","Derecho","Aval"],"Prejuicio","Se forma antes de conocer.",tiempo=20),VF("Relámpago. La xenofobia es rechazo a personas extranjeras.","Verdadero","Es su definición.",tiempo=20),MC("Relámpago. Quien acompaña a la víctima es un…",["Aliado","Cómplice","Testigo mudo"],"Aliado","Frena la burla.",tiempo=20),VF("Relámpago. Callar siempre protege a la víctima.","Falso","La deja sola.",tiempo=20)]}
EX8=[[1,MC("Un prejuicio es…",["Una opinión negativa formada sin conocer","Un derecho","Una ley","Un delito"],"Una opinión negativa formada sin conocer","Sin pruebas.")],
 [1,FB("La imagen simplificada sobre un grupo es un ___ .",[["estereotipo"]],"Estereotipo.")],
 [1,VF("Se puede discriminar con burlas y exclusiones.","Verdadero","Hay muchas formas.")],
 [2,MC("La xenofobia es…",["Rechazo a personas extranjeras","Miedo a las alturas","Rechazo a las leyes","Gusto por viajar"],"Rechazo a personas extranjeras","Y migrantes.")],
 [2,MC("El racismo jerarquiza a las personas por…",["Color de piel u origen étnico","Edad","Estudios","Talla"],"Color de piel u origen étnico","No tiene base científica.")],
 [2,VF("Discriminar daña la autoestima y la salud.","Verdadero","Además empobrece a la comunidad.")],
 [3,MC("¿Qué principio establece que todas las personas son iguales ante la ley?",["Igualdad","Privilegio","Mayoría","Jerarquía"],"Igualdad","Es un principio de derechos humanos.")],
 [3,MC("Una ley antidiscriminatoria sirve para…",["Sancionar actos discriminatorios","Cobrar impuestos","Elegir autoridades","Cambiar la constitución"],"Sancionar actos discriminatorios","Y proteger a las personas.")],
 [3,VF("La discriminación puede denunciarse.","Verdadero","Hay organismos y normas.")],
 [4,MC("Quien acompaña a la víctima y frena la burla es…",["Un aliado","Un cómplice","Un espectador","Un agresor"],"Un aliado","Actúa en favor de la víctima.")],
 [4,MS("Qué ayuda ante la discriminación:",["Guardar pruebas","Contar a un adulto","Compartir el meme","Acompañar a la víctima"],["Guardar pruebas","Contar a un adulto","Acompañar a la víctima"],"Compartir el meme multiplica el daño.")],
 [4,FB("Antes de denunciar conviene guardar las ___ .",[["pruebas"]],"Capturas, mensajes, fechas.")],
 [4,VF("Reírse de una burla no daña a nadie.","Falso","Refuerza al agresor.")]]
M8={"subject_id":SID,"tema":8,"practica":"Práctica general: prejuicios y discriminación","examen_titulo":"Nivel jefe: prejuicios y discriminación","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT8,"examen":EX8}

# ============ MISIÓN 9: ADOLESCENCIAS, VÍNCULOS Y CONSENTIMIENTO ============
B1=NV("Vas a explicar qué cambios trae la adolescencia y cómo se construye la identidad.",["Qué es la adolescencia","Cambios","Identidad","Grupos y presión"],[
 S(1,"Qué es la adolescencia",[P("La adolescencia es una etapa de la vida con muchos cambios. No todas las personas la viven igual: hay <b>muchas adolescencias</b>, según la historia, la cultura, la familia y el contexto de cada uno.")]),
 S(1,"Cambios",[T("Qué cambia",["Tipo","Ejemplos"],[["Físicos","Crecimiento, cambios en el cuerpo"],["Emocionales","Emociones intensas, cambios de ánimo"],["Sociales","Los amigos pesan más, aparecen nuevas responsabilidades"],["De pensamiento","Más capacidad de razonar y de cuestionar"]])]),
 S(2,"Identidad",[D("Identidad","Idea que cada persona va formando sobre quién es: sus gustos, valores, ideas y pertenencias."),P("Se construye con el tiempo, probando y reflexionando. Está bien cambiar de opinión y de intereses.")]),
 S(2,"Grupos y presión",[PN("Los grupos de amigos son muy importantes, pero a veces ejercen <b>presión</b> para hacer algo que uno no quiere. Una persona puede decir que no y seguir perteneciendo. En la Argentina, la ley de Educación Sexual Integral reconoce el derecho de las y los estudiantes a recibir información sobre estos temas.","Los grupos de amigos son muy importantes, pero a veces ejercen <b>presión</b> para hacer algo que uno no quiere. Una persona puede decir que no y seguir perteneciendo. En muchos países, los programas de educación integral reconocen el derecho de los estudiantes a recibir información sobre estos temas.")])],
 {"titulo":"relacionar","planteo":"Un grupo te presiona para hacer algo que no querés. ¿Qué podés hacer?","pasos":["Reconocer que no estás de acuerdo.","Decir que no, con firmeza y sin culpa.","Buscar apoyo en una persona adulta de confianza."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La idea que cada persona tiene de quién es se llama ___ .","Cuando un grupo empuja a hacer algo que uno no quiere, hay ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres cosas que te definen y una que cambió en el último año."},
 {"titulo":"Tu manera","texto":"Podés cambiar y seguir siendo vos."},
 ["Pensar que todas las adolescencias son iguales.","Creer que decir que no es traicionar al grupo."],
 RS(("Adolescencia","Etapa de cambios."),("Cambios","Físicos, emocionales, sociales."),("Identidad","Quién soy."),("Presión","Se puede decir que no.")),
 G(("Adolescencia","Etapa entre la niñez y la adultez."),("Identidad","Idea de quién soy."),("Presión de grupo","Empuje a hacer algo."),("Autoestima","Valoración de uno mismo.")),
 ["¿Cómo se llama la idea de quién es cada persona?","¿Cómo se llama el empuje de un grupo a hacer algo que uno no quiere?","¿Todas las adolescencias son iguales? Respondé sí o no.","¿Se puede decir que no a una presión y seguir perteneciendo al grupo? Respondé sí o no."],
 [["identidad","la identidad"],["presion","presión","presion de grupo","presión de grupo","la presion","la presión"],["no"],["si","sí"]],
 {"incompleto":"Identidad. Presión.","solo":"Cambié de gustos y de amigos, y sigo siendo yo.","carpeta":["Identidad.","Presión.","No.","Sí."]})
B2=NV("Vas a describir cómo son las relaciones afectivas respetuosas: amistad y noviazgo.",["Qué las caracteriza","Comunicación","Límites","Señales saludables"],[
 S(1,"Qué las caracteriza",[T("Rasgos de una relación respetuosa",["Rasgo","Qué significa"],[["Respeto","Se valoran las ideas y los tiempos del otro"],["Confianza","No hace falta controlar"],["Igualdad","Las decisiones se toman entre los dos"],["Libertad","Cada uno conserva sus amistades y gustos"],["Cuidado","Se busca el bienestar del otro"]])]),
 S(1,"Comunicación",[P("En una relación sana se habla con claridad: se dice qué se siente, se escucha y se pueden tener desacuerdos sin humillar ni gritar. Resolver un conflicto no es ganar, es encontrar un acuerdo.")]),
 S(2,"Límites",[P("Los <b>límites</b> son lo que cada persona acepta y lo que no. Se pueden poner y deben respetarse. Un «no» o un «no quiero» es una respuesta válida y no hace falta justificarla.")]),
 S(2,"Señales saludables",[T("Cómo se siente",["Señal","Qué indica"],[["Me siento tranquilo y seguro","Hay confianza"],["Puedo decir lo que pienso","Hay respeto"],["Me alegro de los logros del otro","Hay cuidado"],["Puedo estar con otras personas","Hay libertad"]])])],
 {"titulo":"identificar","planteo":"¿Qué señal es sana: «me pide la clave de mi celular» o «me alegra cuando me va bien»?","pasos":["Pedir las claves es control.","Alegrarse del otro es cuidado.","La señal sana es la segunda."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Lo que cada persona acepta y lo que no son sus ___ .","En una relación sana se resuelven los conflictos sin ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí cinco cosas que esperás de una amistad respetuosa."},
 {"titulo":"Un no vale","texto":"Un «no» se respeta, sin pedir explicaciones."},
 ["Pensar que los celos son una prueba de amor.","Creer que controlar es cuidar."],
 RS(("Rasgos","Respeto, confianza, igualdad."),("Comunicar","Hablar y escuchar."),("Límites","Se ponen y se respetan."),("Señales","Seguridad y libertad.")),
 G(("Límite","Lo que una persona acepta o no."),("Confianza","Creer en el otro sin controlarlo."),("Respeto","Valorar al otro."),("Acuerdo","Solución aceptada por ambos.")),
 ["¿Cómo se llama lo que cada persona acepta y lo que no?","¿Cómo se llama creer en el otro sin controlarlo?","¿Los celos son una prueba de amor? Respondé sí o no.","¿Un «no» debe respetarse sin pedir explicaciones? Respondé sí o no."],
 [["limites","límites","los limites","los límites","limite","límite"],["confianza","la confianza"],["no"],["si","sí"]],
 {"incompleto":"Límites. Confianza.","solo":"Espero respeto, confianza, que me escuchen, que no me controlen y que me cuiden.","carpeta":["Límites.","Confianza.","No.","Sí."]})
B3=NV("Vas a reconocer señales de violencia en las relaciones de pareja y saber a quién pedir ayuda.",["Qué es","Tipos","Señales de alerta","Pedir ayuda"],[
 S(1,"Qué es",[D("Violencia en el noviazgo","Cualquier conducta que busca controlar, dañar o humillar a la pareja. Puede ocurrir también entre adolescentes y a través de las redes."),P("La violencia no es amor ni es normal, aunque se repita en películas, canciones o grupos de amigos.")]),
 S(1,"Tipos",[T("Formas",["Tipo","Ejemplo"],[["Psicológica","Humillar, insultar, hacer sentir culpa"],["Física","Golpes, empujones, pellizcos"],["Digital","Revisar el celular, exigir contraseñas, difundir fotos"],["Económica","Controlar el dinero"],["De aislamiento","Impedir ver a amigos y familia"]])]),
 S(2,"Señales de alerta",[T("Cuidado si...",["Señal","Por qué preocupa"],[["Celos excesivos","Busca controlar"],["Te aísla de tus amistades","Te deja sin apoyo"],["Te humilla o te insulta","Daña tu autoestima"],["Revisa tu celular","Invade tu intimidad"],["Te amenaza o te asusta","Es violencia"]])]),
 S(2,"Pedir ayuda",[PN("Si te pasa o le pasa a alguien, lo primero es hablar con una persona adulta de confianza. En la Argentina funcionan la línea 144 (violencia de género) y la línea 102 (derechos de niñas, niños y adolescentes). También ayudan los equipos de orientación de la escuela.","Si te pasa o le pasa a alguien, lo primero es hablar con una persona adulta de confianza. En muchos países existen líneas gratuitas de ayuda para situaciones de violencia y para niñas, niños y adolescentes. También ayudan los equipos de orientación de la escuela.")])],
 {"titulo":"identificar","planteo":"Una pareja le exige a la otra sus contraseñas «para demostrar confianza». ¿Qué señal es?","pasos":["Pedir claves invade la intimidad.","Busca controlar.","Es una señal de alerta, no de confianza."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Revisar el celular de la pareja es violencia ___ .","Si algo nos preocupa, lo primero es hablar con una persona ___ de confianza."]},
 {"titulo":"tu turno","planteo":"Escribí qué le dirías a una amiga que cuenta que su pareja le revisa el celular y no la deja salir."},
 {"titulo":"No es amor","texto":"Si da miedo, controla o humilla, no es amor."},
 ["Pensar que los celos son amor.","Creer que la violencia solo es física."],
 RS(("Qué es","Controlar, dañar o humillar."),("Tipos","Psicológica, física, digital."),("Señales","Celos, aislamiento, amenazas."),("Ayuda","Adulto de confianza y líneas.")),
 G(("Violencia","Conducta que daña o controla."),("Aislamiento","Separar de amigos y familia."),("Intimidad","Vida privada."),("Denunciar","Informar a quien corresponde.")),
 ["¿Cómo se llama la conducta que busca controlar, dañar o humillar a la pareja?","¿Revisar el celular de la pareja es violencia digital? Respondé sí o no.","¿Los celos excesivos son una señal de alerta? Respondé sí o no.","¿A quién conviene contar una situación de violencia: a una persona adulta de confianza o a nadie?"],
 [["violencia","la violencia"],["si","sí"],["si","sí"],["persona adulta de confianza","adulta de confianza","a una persona adulta de confianza","una persona adulta de confianza","un adulto de confianza","adulto de confianza"]],
 {"incompleto":"Violencia. Adulta.","solo":"Le diría que no es normal, que no está sola y que hable con un adulto de confianza.","carpeta":["Violencia.","Sí.","Sí.","Una persona adulta de confianza."]})
B4=NV("Vas a explicar qué es el consentimiento, cómo se da y se retira, y por qué es parte del cuidado mutuo.",["Qué es el consentimiento","Características","Cuidado mutuo","En el mundo digital"],[
 S(1,"Qué es el consentimiento",[D("Consentimiento","Acuerdo claro y libre de una persona para hacer algo o para que otra persona haga algo que la involucra."),P("Se aplica a muchas situaciones: un abrazo, una foto, compartir un secreto, ir a algún lugar.")]),
 S(1,"Características",[T("Cómo es un consentimiento válido",["Rasgo","Qué significa"],[["Libre","Sin presión, amenazas ni chantaje"],["Informado","Se sabe de qué se trata"],["Específico","Vale para una cosa y no para todas"],["Reversible","Se puede cambiar de opinión cuando se quiera"],["Entusiasta","Se expresa con ganas, no por compromiso"]])]),
 S(2,"Cuidado mutuo",[P("El silencio, el miedo o la duda <b>no</b> son un sí. Si alguien dice que no, o duda, se frena y se respeta. Cuidarse mutuamente es preguntar, escuchar y aceptar la respuesta.")]),
 S(2,"En el mundo digital",[PN("El consentimiento también vale en internet: no se comparten fotos, videos ni datos de otra persona sin su permiso. En la Argentina, difundir imágenes íntimas sin consentimiento puede tener consecuencias legales.","El consentimiento también vale en internet: no se comparten fotos, videos ni datos de otra persona sin su permiso. En muchos países, difundir imágenes íntimas sin consentimiento puede tener consecuencias legales.")])],
 {"titulo":"identificar","planteo":"Un amigo te pide una foto tuya y vos dudás. ¿Qué respuesta vale?","pasos":["La duda no es un sí.","Podés decir que no, sin dar explicaciones.","Él debe respetar tu respuesta."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un consentimiento que se puede cambiar cuando uno quiere es ___ .","El silencio, el miedo o la duda no son un ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres situaciones cotidianas donde hay que pedir permiso."},
 {"titulo":"Cuando dicen que no","texto":"Cuando alguien dice que no, yo paro."},
 ["Pensar que el silencio es un sí.","Creer que el consentimiento dado antes vale para siempre."],
 RS(("Consentimiento","Acuerdo libre."),("Rasgos","Libre, informado, reversible."),("No es sí","Silencio o duda."),("Digital","También cuenta.")),
 G(("Consentimiento","Acuerdo libre y claro."),("Reversible","Se puede cambiar de opinión."),("Chantaje","Presión con amenazas."),("Cuidado mutuo","Cuidarse entre todos.")),
 ["¿Cómo se llama el acuerdo libre y claro de una persona?","¿Un consentimiento puede retirarse cuando la persona quiera? Respondé sí o no.","¿El silencio es un sí? Respondé sí o no.","¿Se puede compartir la foto de otra persona sin su permiso? Respondé sí o no."],
 [["consentimiento","el consentimiento"],["si","sí"],["no"],["no"]],
 {"incompleto":"Consentimiento. Reversible.","solo":"Si dudo, no hace falta que diga que sí: puedo decir que no.","carpeta":["Consentimiento.","Sí.","No.","No."]})
ACT9={"1":[MS("¿Qué cambia en la adolescencia?",["El cuerpo","Las emociones","Los vínculos sociales","El grupo sanguíneo"],["El cuerpo","Las emociones","Los vínculos sociales"],"El grupo sanguíneo no cambia."),VF("Todas las adolescencias son iguales.","Falso","Hay muchas adolescencias.")],
 "2":[{"t":"classify","p":"¿Señal sana o señal de alerta?","o":{"elementos":["Respeta mis tiempos","Revisa mi celular","Celebra mis logros","Me aísla de mis amigos"],"categorias":["Sana","De alerta"]},"r":{"categorias":{"Respeta mis tiempos":"Sana","Revisa mi celular":"De alerta","Celebra mis logros":"Sana","Me aísla de mis amigos":"De alerta"}},"e":"Una relación sana da seguridad y libertad."},FB("Lo que cada persona acepta y lo que no son sus ___ .",[["limites","límites"]],"Se ponen y se respetan.")],
 "3":[{"t":"matching","p":"Uní cada tipo de violencia con su ejemplo.","o":{"izquierda":["Psicológica","Digital","Económica","De aislamiento"],"derecha":["Humillar o insultar","Revisar el celular","Controlar el dinero","Impedir ver a los amigos"]},"r":{"pares":{"Psicológica":"Humillar o insultar","Digital":"Revisar el celular","Económica":"Controlar el dinero","De aislamiento":"Impedir ver a los amigos"}},"e":"Cada tipo, su ejemplo."},VF("Los celos excesivos son una señal de alerta.","Verdadero","Buscan controlar.")],
 "4":[{"t":"ordering","p":"Ordená qué hacer si alguien dice que no.","o":["Respetar la respuesta","Frenar","Escuchar","No insistir"],"r":{"orden":["Frenar","Escuchar","Respetar la respuesta","No insistir"]},"e":"Se frena y se respeta."},TT("Tocá lo que no es un sí: «El silencio, el miedo y la duda no son un sí».",["El","silencio,","el","miedo","y","la","duda","no","son","un","sí"],[1,3,6],"No equivalen a aceptar.")],
 "5":[MC("Relámpago. La idea de quién es cada persona es la…",["Identidad","Presión","Veda"],"Identidad","Se construye con el tiempo.",tiempo=20),VF("Relámpago. Controlar es una forma de cuidar.","Falso","Es una señal de alerta.",tiempo=20),MC("Relámpago. Un consentimiento válido es…",["Libre","Obligado","Callado"],"Libre","Sin presión.",tiempo=20),VF("Relámpago. El consentimiento se puede retirar.","Verdadero","Es reversible.",tiempo=20)]}
EX9=[[1,MC("La identidad es…",["La idea de quién es cada persona","Un documento","Un grupo","Un derecho"],"La idea de quién es cada persona","Se construye con el tiempo.")],
 [1,VF("Está bien cambiar de opinión y de intereses.","Verdadero","La identidad se va formando.")],
 [1,MC("Ante una presión de grupo, una persona puede…",["Decir que no y seguir perteneciendo","Obedecer siempre","Aislarse","Esconderse"],"Decir que no y seguir perteneciendo","Un no es válido.")],
 [2,MC("Un rasgo de una relación respetuosa es…",["Respeto","Control","Chantaje","Amenaza"],"Respeto","Y confianza.")],
 [2,FB("Lo que cada persona acepta y lo que no son sus ___ .",[["limites","límites"]],"Se respetan.")],
 [2,VF("Un «no» debe respetarse sin pedir explicaciones.","Verdadero","Es una respuesta válida.")],
 [3,MC("Revisar el celular de la pareja es una forma de violencia…",["Digital","Física","Económica","Ninguna"],"Digital","Invade la intimidad.")],
 [3,MS("Señales de alerta:",["Celos excesivos","Aislamiento","Humillaciones","Respeto mutuo"],["Celos excesivos","Aislamiento","Humillaciones"],"El respeto mutuo es sano.")],
 [3,VF("Lo primero ante una situación de violencia es hablar con una persona adulta de confianza.","Verdadero","Y pedir ayuda.")],
 [4,MC("Un consentimiento válido es…",["Libre, informado y reversible","Obligado","Callado","Eterno"],"Libre, informado y reversible","Se puede retirar.")],
 [4,VF("El silencio es un sí.","Falso","No equivale a aceptar.")],
 [4,MC("Si alguien dice que no, hay que…",["Frenar y respetar","Insistir","Presionar","Ignorarlo"],"Frenar y respetar","Es cuidado mutuo.")],
 [4,VF("Compartir la foto de otra persona sin permiso está mal.","Verdadero","El consentimiento también cuenta en línea.")]]
M9={"subject_id":SID,"tema":9,"practica":"Práctica general: adolescencias, vínculos y consentimiento","examen_titulo":"Nivel jefe: adolescencias, vínculos y consentimiento","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT9,"examen":EX9}
for n,m in ((8,M8),(9,M9)):
    os.makedirs(os.path.join(AQUI,f"mision-{n}"),exist_ok=True); json.dump(m,open(os.path.join(AQUI,f"mision-{n}",f"mision-{n}.json"),"w"),ensure_ascii=False)
RAIZ=os.path.join(AQUI,"..","..","tools","clase","lecciones")
STEPS={(8,1):"8b05b13a-0459-45c0-b37f-55935141b1fc",(8,2):"a54d9c31-de20-47c6-b927-f6e69af0d3c0",(8,3):"5db2b85e-fe2c-43c0-b63d-0a6dfa2c0c5c",(8,4):"c79ad7f3-a47b-4a1d-a7f3-fffd3cb2f2bf",(9,1):"79e3a1cb-f983-45b5-a1c0-b6aea48ac1b0",(9,2):"9b9cd876-f62e-4973-9322-76ad32080769",(9,3):"88904d84-d7c2-4ab2-8bc4-149ff39da8f2",(9,4):"9ae6ac87-287d-4baf-9f42-4785e1cd960e"}
TIT={(8,1):"Del prejuicio a la discriminación",(8,2):"Racismo, xenofobia y exclusión",(8,3):"Leyes contra la discriminación",(8,4):"Cómo actuar ante la discriminación",(9,1):"Identidad y cambios en la adolescencia",(9,2):"Relaciones afectivas respetuosas",(9,3):"Violencia en las relaciones de pareja",(9,4):"Consentimiento y cuidado mutuo"}
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
CLS={(8,1):[
 RET("¿Cómo se llama la opinión negativa formada antes de conocer a alguien?",6,"Prejuicio","💭","DEL PREJUICIO","a la discriminación",["Desafío: ¿cómo se llama la opinión negativa formada antes de conocer a alguien? Seis segundos.","Prejuicio.","Hoy: *del prejuicio a la discriminación*."]),
 DEF("Prejuicio","Opinión negativa formada sin conocer","💭",["Un *prejuicio* es una opinión negativa formada sin conocer.","Se aprende en la familia, los medios y la calle."]),
 DEF("Estereotipo","Imagen simplificada de un grupo","🧩",["Un *estereotipo* es una imagen simplificada de un grupo.","Se aplica a todas las personas que lo integran."]),
 DEF("Discriminación","Trato desigual e injusto","🚫",["La *discriminación* es un trato desigual e injusto.","Puede ser con palabras, burlas o exclusiones."]),
 PA("DE LA IDEA AL HECHO",[("Prejuicio","💭"),("Estereotipo","🧩"),("Discriminación","🚫")],["Cómo se llega a discriminar.","Primero, un *prejuicio*.","Luego, un *estereotipo*.","Y al final, la *discriminación*."]),
 CL([("IDEA","💭"),("ACCIÓN","🚫")],[("Prejuicio",0),("Excluir a alguien",1),("Estereotipo",0)],["¿Idea o acción?","*Prejuicio* y *estereotipo*: ideas.","*Excluir a alguien*: acción."]),
 Q("La imagen simplificada de todo un grupo es un…",["Estereotipo","Derecho","Aval"],0,["Te toca: la imagen simplificada de un grupo.","¿Estereotipo, derecho o aval?","Un *estereotipo*."]),
 ER([("Los prejuicios son inocentes","Pueden terminar en daño"),("Discriminar es solo insultar","Hay muchas formas")],["Errores típicos.","Creer que los prejuicios son *inocentes*.","Y que discriminar es *solo insultar*."]),
 RES(["Repasemos.","Un *prejuicio* se forma sin conocer.","Un *estereotipo* simplifica a un grupo.","La *discriminación* es trato injusto.","Conocer a las personas lo *evita*.","¡Clase terminada! Ahora, *a practicar*."],[["PREJUICIO","sin conocer"],["ESTEREOTIPO","imagen simple"],["DISCRIMINACIÓN","trato injusto"],["CAMINO","idea a hecho"]])],
(8,2):[
 NOT("ESCUELA","Rechazan a un alumno nuevo","Por haber nacido en otro país","🏫","RACISMO, XENOFOBIA","y exclusión",["Noticia: rechazan a un alumno nuevo.","Por haber nacido en otro país.","Hoy: *racismo, xenofobia y exclusión*."]),
 DEF("Racismo","Jerarquizar por color u origen","🚫",["El *racismo* cree que unas personas valen más que otras.","Por su color de piel u origen étnico."]),
 DEF("Xenofobia","Rechazo a personas extranjeras","🌍",["La *xenofobia* es el rechazo a las personas extranjeras.","Se expresa en burlas, exclusión o culpas."]),
 TB("OTRAS FORMAS",["Tipo","Ejemplo"],[["Sexismo","Por género"],["Capacitismo","Por discapacidad"],["Clasismo","Por dinero"],["Por apariencia","Por el aspecto"]],["Otras formas de discriminar.","El *sexismo*, por género.","El *capacitismo*, por discapacidad.","El *clasismo*, por dinero.","Y por *apariencia*."]),
 CL([("DAÑA","💔"),("SUMA","🤝")],[("Burlarse",0),("Compartir culturas",1),("Excluir",0),("Valorar lo distinto",1)],["¿Daña o suma?","*Burlarse* y *excluir*: dañan.","*Compartir culturas* y *valorar lo distinto*: suman."]),
 Q("El rechazo a personas extranjeras es…",["Xenofobia","Sexismo","Clasismo"],0,["Te toca: rechazo a personas extranjeras.","¿Xenofobia, sexismo o clasismo?","*Xenofobia*."]),
 ER([("El racismo tiene base científica","Somos una sola especie"),("Solo daña a la víctima","Empobrece a todos")],["Errores típicos.","Creer que el racismo tiene *base científica*.","Y que *solo* daña a la víctima."]),
 RES(["Repasemos.","El *racismo* jerarquiza por color u origen.","La *xenofobia* rechaza al extranjero.","Hay *sexismo*, capacitismo y clasismo.","Y *todos* perdemos con la discriminación.","¡Clase terminada! Ahora, *a practicar*."],[["RACISMO","por color u origen"],["XENOFOBIA","rechazo al extranjero"],["OTRAS","sexismo, clasismo"],["EFECTO","daño"]])],
(8,3):[
 {"t":"gancho","grande":"Todos iguales","emoji":"⚖️","final":"ante la ley y en dignidad","titulo":"LEYES CONTRA","sub":"la discriminación","voz":["Todas las personas son iguales en dignidad y derechos.","Las leyes lo protegen.","Hoy: *leyes contra la discriminación*."]},
 DEF("No discriminación","Igualdad de trato","⚖️",["La *no discriminación* es un principio de derechos humanos.","El Estado debe tratar a todos con igualdad."]),
 TB("NORMAS INTERNACIONALES",["Norma","Año"],[["Declaración Universal","1948"],["Contra el racismo","1965"],["Contra la discriminación de la mujer","1979"],["Personas con discapacidad","2006"]],["Algunos instrumentos.","La *Declaración Universal*, mil novecientos cuarenta y ocho.","La convención *contra el racismo*, sesenta y cinco.","La de la *mujer*, setenta y nueve.","Y la de *discapacidad*, dos mil seis."]),
 CMP(("NORMA","Dice qué está prohibido","📜"),("EDUCACIÓN","Cambia las actitudes","🎓"),"+",["Se necesitan las dos cosas.","La *norma* dice qué está prohibido.","La *educación* cambia las actitudes."]),
 CL([("LA LEY PERMITE","✅"),("NO LA PERMITE","❌")],[("Denunciar",0),("Discriminar",1),("Reparar el daño",0),("Incitar al odio",1)],["¿Lo permite la ley?","*Denunciar* y *reparar el daño*: sí.","*Discriminar* e *incitar al odio*: no."]),
 Q("¿Qué principio dice que todas las personas son tratadas por igual?",["Igualdad","Privilegio","Mayoría"],0,["Te toca: tratadas por igual.","¿Igualdad, privilegio o mayoría?","La *igualdad*."]),
 ER([("Una ley alcanza por sí sola","Hace falta educación"),("No se puede denunciar","Se puede denunciar")],["Errores típicos.","Creer que una ley *alcanza por sí sola*.","Y que *no se puede denunciar*."]),
 RES(["Repasemos.","La *igualdad* es un principio.","Hay *convenciones* internacionales.","Las leyes permiten *denunciar* y sancionar.","Y la *educación* completa la tarea.","¡Clase terminada! Ahora, *a practicar*."],[["PRINCIPIO","igualdad"],["INTERNACIONAL","convenciones"],["LEYES","denunciar y sancionar"],["EDUCACIÓN","cambia actitudes"]])],
(8,4):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Se burlan de un compañero en el grupo 😞"},{"yo":True,"txt":"¿Y vos qué hacés?"},{"yo":False,"txt":"No sé, no quiero problemas"}],"titulo":"ACTUAR ANTE","sub":"la discriminación","voz":["Lu cuenta que se burlan de un compañero en el grupo.","Juan: ¿y vos qué hacés?","Lu: no sé, no quiero problemas.","Hoy: *cómo actuar ante la discriminación*."]},
 PA("SI ME PASA A MÍ",[("Frenar con calma","✋"),("Guardar pruebas","📸"),("Contar a un adulto","🧑"),("Denunciar","📣")],["Si me pasa a mí.","*Frenar* con calma.","*Guardar* pruebas.","*Contar* a un adulto de confianza.","Y *denunciar*."]),
 DEF("Aliado","Quien acompaña a la víctima","🤝",["Un *aliado* acompaña a la víctima.","Frena la burla y avisa a un adulto."]),
 CL([("AYUDA","✅"),("DAÑA","❌")],[("Acompañar",0),("Reírse",1),("Guardar capturas",0),("Compartir el meme",1)],["¿Ayuda o daña?","*Acompañar* y *guardar capturas*: ayudan.","*Reírse* y *compartir el meme*: dañan."]),
 CMP(("CALLAR","Deja sola a la víctima","🤐"),("ACTUAR","Frena la discriminación","🗣️"),"vs",["Dos opciones.","*Callar* deja sola a la víctima.","*Actuar* frena la discriminación."]),
 Q("Quien acompaña a la víctima y frena la burla es…",["Un aliado","Un cómplice","Un espectador"],0,["Te toca: quien acompaña a la víctima.","¿Un aliado, un cómplice o un espectador?","Un *aliado*."]),
 ER([("Reírse no daña","Refuerza al agresor"),("Callar protege","Deja sola a la víctima")],["Errores típicos.","Creer que *reírse* no daña.","Y que *callar* protege."]),
 RES(["Repasemos.","Si me pasa: *frenar*, guardar pruebas y contar.","Si lo veo: ser *aliado*.","No hay que *reírse* ni compartir.","Y la *comunidad* previene.","¡Clase terminada! Ahora, *a practicar*."],[["SI ME PASA","frenar y contar"],["SI LO VEO","ser aliado"],["NO HACER","reírse"],["COMUNIDAD","prevenir"]])],
(9,1):[
 NOT("ADOLESCENCIAS","Cada persona la vive distinto","No hay una sola manera","🌱","IDENTIDAD Y CAMBIOS","en la adolescencia",["Noticia: cada persona vive la adolescencia distinto.","No hay una sola manera.","Hoy: *identidad y cambios en la adolescencia*."]),
 TB("QUÉ CAMBIA",["Tipo","Ejemplos"],[["Físicos","El cuerpo"],["Emocionales","Ánimo intenso"],["Sociales","Los amigos pesan"],["De pensamiento","Se cuestiona más"]],["Los cambios.","Los *físicos*: el cuerpo.","Los *emocionales*: ánimo intenso.","Los *sociales*: los amigos pesan más.","Y los de *pensamiento*."]),
 DEF("Identidad","La idea de quién es cada persona","🪞",["La *identidad* es la idea de quién sos.","Se construye con el tiempo."]),
 DEF("Presión de grupo","Empuje a hacer algo que uno no quiere","👥",["La *presión de grupo* empuja a hacer algo que uno no quiere.","Se puede decir que no y seguir perteneciendo."]),
 CL([("PUEDO DECIDIR","✅"),("PRESIÓN","⚠️")],[("Elegir mis gustos",0),("Hacerlo por miedo",1),("Decir que no",0)],["¿Decisión o presión?","*Elegir mis gustos* y *decir que no*: decisión.","*Hacerlo por miedo*: presión."]),
 Q("La idea de quién es cada persona es la…",["Identidad","Presión","Veda"],0,["Te toca: la idea de quién es cada persona.","¿Identidad, presión o veda?","La *identidad*."]),
 ER([("Todas las adolescencias son iguales","Hay muchas"),("Decir que no es traicionar","Es cuidarse")],["Errores típicos.","Creer que todas son *iguales*.","Y que decir que no es *traicionar*."]),
 RES(["Repasemos.","La adolescencia trae *cambios*.","Hay *muchas* adolescencias.","La *identidad* se va construyendo.","Y se puede decir *que no*.","¡Clase terminada! Ahora, *a practicar*."],[["CAMBIOS","físicos, emocionales"],["ADOLESCENCIAS","muchas"],["IDENTIDAD","quién soy"],["PRESIÓN","decir que no"]])],
(9,2):[
 RET("¿Cómo se llama lo que cada persona acepta y lo que no?",5,"Límites","🚧","RELACIONES AFECTIVAS","respetuosas",["Desafío: ¿cómo se llama lo que cada persona acepta y lo que no? Cinco segundos.","Límites.","Hoy: *relaciones afectivas respetuosas*."]),
 TB("RASGOS",["Rasgo","Significa"],[["Respeto","Se valora al otro"],["Confianza","Sin controlar"],["Igualdad","Se decide entre dos"],["Libertad","Cada uno sigue con lo suyo"],["Cuidado","Se busca el bienestar"]],["Rasgos de una relación sana.","*Respeto*.","*Confianza*, sin controlar.","*Igualdad*.","*Libertad*.","Y *cuidado*."]),
 DEF("Límite","Lo que una persona acepta o no","🚧",["Un *límite* es lo que una persona acepta o no.","Se pone y se respeta."]),
 CL([("SEÑAL SANA","💚"),("SEÑAL DE ALERTA","🚩")],[("Respeta mis tiempos",0),("Revisa mi celular",1),("Celebra mis logros",0),("Me aísla",1)],["¿Sana o de alerta?","*Respeta mis tiempos* y *celebra mis logros*: sanas.","*Revisa mi celular* y *me aísla*: de alerta."]),
 CMP(("CONTROLAR","No es cuidar","🔒"),("CUIDAR","Busca el bienestar del otro","💚"),"vs",["No es lo mismo.","*Controlar* no es cuidar.","*Cuidar* busca el bienestar del otro."]),
 Q("Un «no» en una relación…",["Se respeta","Se discute","Se ignora"],0,["Te toca: un no en una relación.","¿Se respeta, se discute o se ignora?","Se *respeta*."]),
 ER([("Los celos son amor","Son una señal de alerta"),("Controlar es cuidar","No lo es")],["Errores típicos.","Creer que los *celos* son amor.","Y que *controlar* es cuidar."]),
 RES(["Repasemos.","Una relación sana tiene *respeto* y *confianza*.","Se *comunica* con claridad.","Los *límites* se respetan.","Y hay señales *sanas* y de alerta.","¡Clase terminada! Ahora, *a practicar*."],[["RASGOS","respeto, confianza"],["COMUNICAR","hablar y escuchar"],["LÍMITES","se respetan"],["SEÑALES","sanas o de alerta"]])],
(9,3):[
 NOT("ALERTA","Le pide la contraseña del celular","Dice que es por amor","📱","VIOLENCIA EN EL NOVIAZGO","señales y ayuda",["Alerta: le pide la contraseña del celular.","Dice que es por amor.","Hoy: *violencia en las relaciones de pareja*."]),
 DEF("Violencia","Conducta que controla, daña o humilla","🚩",["La *violencia* busca controlar, dañar o humillar.","No es amor ni es normal."]),
 TB("TIPOS",["Tipo","Ejemplo"],[["Psicológica","Humillar"],["Física","Golpes"],["Digital","Revisar el celular"],["Aislamiento","Alejar de amigos"]],["Tipos de violencia.","La *psicológica*: humillar.","La *física*: golpes.","La *digital*: revisar el celular.","Y el *aislamiento*."]),
 TB("SEÑALES DE ALERTA",["Señal","Por qué preocupa"],[["Celos excesivos","Busca controlar"],["Te aísla","Te deja sin apoyo"],["Te humilla","Daña tu autoestima"],["Te asusta","Es violencia"]],["Señales de alerta.","*Celos excesivos*.","Te *aísla*.","Te *humilla*.","Y te *asusta*."]),
 CL([("AMOR SANO","💚"),("VIOLENCIA","🚩")],[("Respeta amistades",0),("Te insulta",1),("Te escucha",0),("Te controla",1)],["¿Amor sano o violencia?","*Respeta amistades* y *te escucha*: amor sano.","*Te insulta* y *te controla*: violencia."]),
 Q("¿A quién conviene contar una situación de violencia?",["A una persona adulta de confianza","A nadie","Solo a un grupo de amigos"],0,["Te toca: ¿a quién conviene contar?","¿A una persona adulta de confianza, a nadie o a amigos?","A una *persona adulta de confianza*."]),
 ER([("La violencia es solo física","Hay muchos tipos"),("Es normal si se repite en películas","No es normal")],["Errores típicos.","Creer que la violencia es *solo física*.","Y que es *normal* porque se ve en películas."]),
 RES(["Repasemos.","La *violencia* controla, daña o humilla.","Hay varios *tipos*.","Hay *señales* de alerta.","Y siempre se puede *pedir ayuda*.","¡Clase terminada! Ahora, *a practicar*."],[["VIOLENCIA","controla y daña"],["TIPOS","varios"],["SEÑALES","celos, aislamiento"],["AYUDA","adulto y líneas"]])],
(9,4):[
 RET("Si alguien dice que no, ¿qué hacés?",5,"Paro y respeto","🛑","CONSENTIMIENTO","y cuidado mutuo",["Desafío: si alguien dice que no, ¿qué hacés? Cinco segundos.","Paro y respeto.","Hoy: *consentimiento y cuidado mutuo*."]),
 DEF("Consentimiento","Acuerdo libre y claro","🤝",["El *consentimiento* es un acuerdo libre y claro.","Vale para abrazos, fotos, secretos y planes."]),
 TB("RASGOS",["Rasgo","Significa"],[["Libre","Sin presión"],["Informado","Se sabe de qué se trata"],["Específico","Vale para una cosa"],["Reversible","Se puede cambiar"]],["Cómo es un consentimiento válido.","*Libre*: sin presión.","*Informado*.","*Específico*: vale para una cosa.","Y *reversible*."]),
 DEF("No es un sí","Silencio, miedo o duda","🛑",["El *silencio*, el *miedo* o la *duda* no son un sí.","Si hay duda, se frena."]),
 CL([("ES UN SÍ","✅"),("NO ES UN SÍ","🛑")],[("Un sí claro y libre",0),("Silencio",1),("Duda",1),("Entusiasmo",0)],["¿Es un sí o no?","*Un sí claro y libre* y *entusiasmo*: es un sí.","*Silencio* y *duda*: no es un sí."]),
 Q("El silencio…",["No es un sí","Es un sí","Siempre vale"],0,["Te toca: el silencio.","¿No es un sí, es un sí o siempre vale?","*No es un sí*."]),
 ER([("El sí vale para siempre","Se puede retirar"),("Compartir fotos sin permiso","Hace falta permiso")],["Errores típicos.","Creer que el sí *vale para siempre*.","Y *compartir* fotos sin permiso."]),
 RES(["Repasemos.","El *consentimiento* es libre y claro.","Es *informado* y *reversible*.","El *silencio* no es un sí.","Y también cuenta *en línea*.","¡Clase terminada! Ahora, *a practicar*."],[["CONSENTIMIENTO","libre y claro"],["RASGOS","informado, reversible"],["NO ES SÍ","silencio, duda"],["ONLINE","también cuenta"]])]}
for (m,n),es in CLS.items():
    json.dump({"sin_variante":True,"slug":f"ciud1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Ciudadanía I","titulo":TIT[(m,n)],"sub":f"Ciudadanía I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"ciud1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
