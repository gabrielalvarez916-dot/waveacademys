# -*- coding: utf-8 -*-
"""Lengua y Literatura I · Misión 10 (Cartas, mails y formularios) y Misión 11 (La poesía)."""
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
# ================= MISIÓN 10 =================
A1=NV("Vas a distinguir una carta formal de una informal y reconocer sus partes.",["Para qué se escribe una carta","Las partes","Formal e informal","Cómo elegir"],[
 S(1,"La carta",[D("Carta","Texto escrito que una persona envía a otra para comunicarle algo, pedir o agradecer."),P("Aunque hoy casi todo se hace por mail, las cartas y los mensajes largos siguen la misma estructura.")]),
 S(1,"Las partes",[T("Estructura",["Parte","Qué lleva"],[["Lugar y fecha","Dónde y cuándo se escribe"],["Destinatario","A quién va dirigida"],["Saludo","Estimado/a..., Querido/a..."],["Cuerpo","El mensaje"],["Despedida","Atentamente, Un abrazo"],["Firma","Nombre de quien escribe"]])]),
 S(2,"Formal e informal",[T("Diferencias",["","Formal","Informal"],[["A quién","Alguien que no conozco o con autoridad","Familia, amigos"],["Saludo","Estimado Sr. Pérez","Querida Sofi"],["Despedida","Atentamente","Un beso grande"],["Lenguaje","Cuidado, sin abreviaturas ni chistes","Cercano y cotidiano"]])]),
 S(2,"Cómo elegir",[P("Preguntate <b>a quién le escribo</b> y <b>para qué</b>. Si pido un trabajo, un trámite o hablo con una autoridad, uso la carta formal. Si cuento algo a un amigo, la informal.")])],
 {"titulo":"elegir","planteo":"Vas a pedirle a la directora una autorización. ¿Carta formal o informal?","pasos":["Es una autoridad.","Es un pedido.","Formal: Estimada Directora..., Atentamente."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La persona a quien va dirigida la carta es el ___ .","La carta formal termina con una despedida como ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí el saludo y la despedida de una carta formal y de una informal."},
 {"titulo":"A quién y para qué","texto":"Antes de escribir, definí a quién le escribís y para qué."},
 ["Usar «Hola, qué tal» con una autoridad.","Olvidar la firma."],
 RS(("Partes","Lugar, destinatario, saludo, cuerpo, despedida, firma."),("Formal","Cuidado y respetuoso."),("Informal","Cercano."),("Elegir","A quién y para qué.")),
 G(("Destinatario","Persona a quien va dirigido un mensaje."),("Remitente","Quien envía el mensaje."),("Formal","Cuidado y respetuoso.")),
 ["¿Cómo se llama la persona a quien va dirigida una carta?","¿Qué despedida es formal: «Atentamente» o «Un beso grande»?","¿Cómo se llama quien envía el mensaje?","Una carta a un amigo, ¿es formal o informal?"],
 [["destinatario","el destinatario"],["atentamente"],["remitente","el remitente"],["informal","es informal"]],
 {"incompleto":"Destinatario. Atentamente.","solo":"Formal: Estimada Directora / Atentamente. Informal: Querida Sofi / Un abrazo.","carpeta":["Destinatario.","Atentamente.","Remitente.","Informal."]})
A2=NV("Vas a escribir un mail claro, con asunto, saludo, mensaje breve y cierre.",["Las partes de un mail","El asunto","Un mensaje claro","Antes de enviar"],[
 S(1,"Partes",[T("Un mail",["Parte","Para qué sirve"],[["Para","Destinatario principal"],["CC","Con copia visible a otras personas"],["CCO","Copia oculta"],["Asunto","Dice de qué trata"],["Cuerpo","El mensaje"],["Adjunto","Archivo que acompaña"]])]),
 S(1,"El asunto",[P("El <b>asunto</b> tiene que ser corto y concreto: «Consulta sobre la tarea de Lengua» sirve; «Hola» o «Importante» no.")]),
 S(2,"Un mensaje claro",[T("Estructura del cuerpo",["Paso","Ejemplo"],[["Saludo","Buenas tardes, profesora:"],["Motivo","Le escribo para consultarle..."],["Detalle","Una o dos frases claras"],["Cierre","Muchas gracias. Saludos cordiales."],["Firma","Nombre y curso"]])]),
 S(2,"Antes de enviar",[P("Revisá: ¿está el <b>adjunto</b>? ¿Escribí bien el destinatario? ¿Releí el texto en busca de errores? Un mail se puede reenviar: escribí como si lo fuera a leer alguien más.")])],
 {"titulo":"armar","planteo":"Escribí un mail a tu profesor para consultar una fecha.","pasos":["Asunto: Consulta sobre la fecha de entrega.","Saludo: Buenas tardes, profesor:","Motivo y detalle: ¿Podría confirmarme hasta cuándo se entrega el trabajo?","Cierre y firma: Muchas gracias. Saludos cordiales, Lucía, 1.º B."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El campo que dice de qué trata el mail es el ___ .","El archivo que acompaña un mail es el ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un mail a un docente pidiendo una aclaración."},
 {"titulo":"Un mail, un motivo","texto":"Si tenés dos pedidos distintos, escribí dos mails."},
 ["Dejar el asunto vacío.","Olvidar el adjunto."],
 RS(("Asunto","Corto y concreto."),("Cuerpo","Saludo, motivo, cierre."),("Adjunto","Archivo."),("Revisar","Antes de enviar.")),
 G(("Asunto","Tema del mail."),("Adjunto","Archivo que acompaña."),("CC","Con copia.")),
 ["¿Qué campo dice de qué trata el mail?","¿Cómo se llama el archivo que acompaña un mail?","¿Conviene revisar antes de enviar? Respondé sí o no.","¿Qué asunto sirve más: «Hola» o «Consulta sobre la tarea»?"],
 [["asunto","el asunto"],["adjunto","el adjunto"],["si","sí"],["consulta sobre la tarea","la segunda","consulta"]],
 {"incompleto":"Asunto. Adjunto.","solo":"Asunto: Consulta sobre la tarea. Buenas tardes, profesora: le escribo para... Muchas gracias. Saludos cordiales, Lucía.","carpeta":["El asunto.","Adjunto.","Sí.","Consulta sobre la tarea."]})
A3=NV("Vas a completar un formulario con datos exactos, sin dejar campos vacíos ni cometer errores.",["Para qué sirven los formularios","Leer antes de completar","Datos exactos","Revisar y firmar"],[
 S(1,"Formularios",[D("Formulario","Documento con campos para completar datos que pide una institución."),P("Se usan para inscribirse, pedir un trámite o dar datos personales.")]),
 S(1,"Leer primero",[T("Antes de escribir",["Mirá","Por qué"],[["Las instrucciones","Dicen cómo completar"],["Campos obligatorios","Sin ellos no se acepta"],["Formato de la fecha","día/mes/año, por ejemplo 05/10/2012"]])]),
 S(2,"Datos exactos",[P("Escribí tu <b>nombre completo</b> como figura en el documento, con letra clara (si es en papel) o sin errores de tipeo. Los números (DNI, teléfono) se escriben sin puntos si no se indica otra cosa.")]),
 S(2,"Revisar y firmar",[T("Lista final",["Chequeo","Sí / No"],[["¿Completé todos los campos obligatorios?",""],["¿Los datos son exactos?",""],["¿Firmé donde corresponde?",""],["¿Entregué a quien correspondía?",""]])])],
 {"titulo":"detectar","planteo":"Un formulario pide fecha de nacimiento «día/mes/año» y alguien escribió 2012/10/05. ¿Qué falla?","pasos":["El formato pide día primero.","Está escrito año primero.","Corrección: 05/10/2012."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Los campos que no se pueden dejar vacíos son los ___ .","Antes de completar, hay que leer las ___ ."]},
 {"titulo":"tu turno","planteo":"Completá con datos inventados un formulario de inscripción a un taller."},
 {"titulo":"Leer, completar, revisar","texto":"El orden es siempre el mismo: leer, completar y revisar."},
 ["Dejar un campo obligatorio vacío.","Escribir la fecha en otro formato."],
 RS(("Formulario","Datos para una institución."),("Instrucciones","Leer primero."),("Datos exactos","Sin errores."),("Firma","Al final.")),
 G(("Formulario","Documento con campos para completar."),("Campo","Espacio para un dato."),("Obligatorio","Que no se puede omitir.")),
 ["¿Qué se hace primero con un formulario: completarlo o leerlo?","¿Cómo se llaman los campos que no se pueden dejar vacíos?","¿Hay que revisar antes de entregar? Respondé sí o no.","¿Cómo se llama el espacio donde se escribe un dato?"],
 [["leerlo","leer","se lee"],["obligatorios","los obligatorios"],["si","sí"],["campo","un campo","el campo"]],
 {"incompleto":"Obligatorios. Instrucciones.","solo":"Nombre completo, fecha 05/10/2012, DNI sin puntos, firma.","carpeta":["Leerlo.","Obligatorios.","Sí.","Campo."]})
A4=NV("Vas a adaptar el registro de un mensaje al destinatario y a la situación.",["Qué es el registro","Formal, neutro e informal","Adaptar un mismo mensaje","Errores frecuentes"],[
 S(1,"Registro",[D("Registro","Manera de hablar o escribir que se elige según con quién hablo y en qué situación."),P("Una misma persona usa distintos registros: con sus amigos, con un profesor, con un médico.")]),
 S(1,"Tres registros",[T("Cómo suenan",["Registro","Cuándo","Ejemplo"],[["Formal","Con autoridades o desconocidos","Le solicito que me indique el horario"],["Neutro","En textos comunes","¿Me decís el horario?"],["Informal","Con amigos y familia","¿A qué hora es, che?"]])]),
 S(2,"Un mensaje, tres versiones",[T("Pedir una fecha",["Destinatario","Mensaje"],[["Directora","Le solicito que me informe la fecha de la muestra."],["Profesor","¿Podría decirme cuándo es la muestra?"],["Amiga","¿Cuándo es la muestra?"]])]),
 S(2,"Errores frecuentes",[P("Los errores más comunes son usar jerga con un adulto desconocido o ser demasiado rígido con un amigo. También conviene evitar abreviaturas de chat (<i>xq, tmb</i>) en textos formales.")])],
 {"titulo":"adaptar","planteo":"Reescribí con registro formal: «Che, pasame el horario».","pasos":["Eliminar el che y el imperativo informal.","Usar un pedido educado.","Versión: ¿Podría indicarme el horario, por favor?"]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La manera de escribir que se elige según el destinatario es el ___ .","Con una autoridad conviene el registro ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí el mismo pedido para una directora y para un amigo."},
 {"titulo":"A quién le hablo","texto":"Para elegir el registro, preguntate quién va a leer tu mensaje."},
 ["Usar abreviaturas de chat en un texto formal.","Ser rígido con un amigo."],
 RS(("Registro","Según el destinatario."),("Formal","Con autoridades."),("Informal","Con amigos."),("Adaptar","Cambia el mensaje.")),
 G(("Registro","Manera de escribir según la situación."),("Jerga","Lenguaje propio de un grupo."),("Rígido","Demasiado serio y duro.")),
 ["¿Cómo se llama la manera de escribir que se elige según el destinatario?","¿Qué registro uso con una autoridad?","¿Se usan abreviaturas de chat en un texto formal? Respondé sí o no.","¿Qué registro uso con un amigo?"],
 [["registro","el registro"],["formal","el formal"],["no"],["informal","el informal"]],
 {"incompleto":"Registro. Formal.","solo":"Directora: ¿Podría informarme la fecha? Amigo: ¿Cuándo es?","carpeta":["Registro.","Formal.","No.","Informal."]})
ACT10={"1":[{"t":"matching","p":"Uní cada parte de la carta con lo que lleva.","o":{"izquierda":["Saludo","Cuerpo","Despedida","Firma"],"derecha":["Estimado Sr. Pérez","El mensaje","Atentamente","Nombre de quien escribe"]},"r":{"pares":{"Saludo":"Estimado Sr. Pérez","Cuerpo":"El mensaje","Despedida":"Atentamente","Firma":"Nombre de quien escribe"}},"e":"Cada parte tiene su función."},TT("Tocá las palabras que muestran que la carta es formal: «Estimada directora: Le solicito que me autorice a participar. Atentamente».",["Estimada","directora","Le","solicito","que","me","autorice","a","participar","Atentamente"],[0,3,9],"Estimada, solicito y atentamente son formales.")],
 "2":[KW("Escribí un mail a un profesor para pedirle que te explique de nuevo un tema. Incluí asunto, saludo, motivo, cierre y firma.","Asunto corto, saludo, motivo claro, agradecimiento y firma.","Mail con asunto concreto, saludo formal, motivo claro (pedir una explicación), cierre educado y firma con nombre y curso.","Se evalúa estructura, claridad y registro."),{"t":"ordering","p":"Ordená las partes del cuerpo de un mail.","o":["Cierre","Saludo","Detalle","Motivo","Firma"],"r":{"orden":["Saludo","Motivo","Detalle","Cierre","Firma"]},"e":"De la presentación a la despedida."}],
 "3":[MS("¿Qué conviene hacer al completar un formulario?",["Leer las instrucciones","Completar los campos obligatorios","Escribir datos inventados","Revisar antes de entregar"],["Leer las instrucciones","Completar los campos obligatorios","Revisar antes de entregar"],"Los datos tienen que ser exactos."),FB("Si el formulario pide la fecha como día/mes/año, 05/10/2012 está ___ y 2012/10/05 está mal.",[["bien","correcto","correcta"]],"Respeta el formato pedido.")],
 "4":[{"t":"classify","p":"¿Qué registro es?","o":{"elementos":["Le solicito que me informe","¿Cuándo es, che?","¿Podría decirme el horario?","Atentamente"],"categorias":["Formal","Informal"]},"r":{"categorias":{"Le solicito que me informe":"Formal","¿Cuándo es, che?":"Informal","¿Podría decirme el horario?":"Formal","Atentamente":"Formal"}},"e":"Cuidado frente a cercanía."},VF("Las abreviaturas de chat sirven en un mail formal.","Falso","Conviene evitarlas.")],
 "5":[MC("Relámpago. La persona a quien va una carta es el…",["Destinatario","Remitente","Asunto"],"Destinatario","Recibe el mensaje.",tiempo=20),VF("Relámpago. El asunto de un mail puede quedar vacío.","Falso","Dice de qué trata.",tiempo=20),MC("Relámpago. Los campos obligatorios…",["No se pueden omitir","Son opcionales","Se borran"],"No se pueden omitir","Sin ellos no se acepta.",tiempo=20),VF("Relámpago. Con una autoridad conviene registro formal.","Verdadero","Es lo adecuado.",tiempo=20)]}
EX10=[[1,MC("¿Con qué despedida termina una carta formal?",["Atentamente","Un beso grande","Chau","Nos vemos"],"Atentamente","Es la despedida formal.")],
 [1,MS("Partes de una carta:",["Saludo","Cuerpo","Firma","Emoji"],["Saludo","Cuerpo","Firma"],"El emoji no es una parte.")],
 [1,VF("A un amigo se le puede escribir una carta informal.","Verdadero","Con lenguaje cercano.")],
 [2,MC("¿Qué dice el asunto de un mail?",["De qué trata","Quién lo recibe","Cuándo se envió","El adjunto"],"De qué trata","Corto y concreto.")],
 [2,FB("El archivo que acompaña un mail es el ___ .",[["adjunto"]],"Se envía junto con el mensaje.")],
 [2,VF("Antes de enviar un mail conviene revisarlo.","Verdadero","Se evitan errores.")],
 [3,MC("¿Qué se hace primero con un formulario?",["Leer las instrucciones","Firmar","Entregarlo","Dibujarlo"],"Leer las instrucciones","Dicen cómo completarlo.")],
 [3,MS("Datos de un formulario:",["Nombre completo","DNI","Fecha de nacimiento","Chiste"],["Nombre completo","DNI","Fecha de nacimiento"],"El chiste no es un dato.")],
 [3,VF("Un campo obligatorio puede quedar vacío.","Falso","No se acepta.")],
 [4,MC("El registro es…",["La manera de escribir según el destinatario","Un tipo de letra","Una lista","Un archivo"],"La manera de escribir según el destinatario","Se adapta.")],
 [4,MC("Con una autoridad conviene…",["Registro formal","Jerga","Abreviaturas de chat","Chistes"],"Registro formal","Respeto y cuidado.")],
 [4,FB("Un lenguaje cercano, para amigos, es el registro ___ .",[["informal","coloquial"]],"Para la familia y amigos.")],
 [4,VF("Con un amigo conviene ser muy rígido.","Falso","El registro es informal.")]]
M10={"subject_id":SID,"tema":10,"practica":"Práctica general: cartas, mails y formularios","examen_titulo":"Nivel jefe: cartas, mails y formularios","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT10,"examen":EX10}

# ================= MISIÓN 11: LA POESÍA =================
B1=NV("Vas a leer un poema en voz alta respetando versos, pausas y entonación, y a decir qué sentís al leerlo.",["Verso y estrofa","Ritmo y pausas","Entonación","Qué me transmite"],[
 S(1,"Verso y estrofa",[D("Verso","Cada línea de un poema."),D("Estrofa","Grupo de versos separado por un espacio."),P("Un poema se lee distinto que un cuento: importa cómo suena, no solo qué dice.")]),
 S(1,"Pausas",[T("Qué marcan",["Signo","Pausa"],[["Coma","Pausa corta"],["Punto","Pausa larga"],["Fin de verso sin signo","Pausa breve, seguí la idea"]])]),
 S(2,"Entonación",[P("Cambiá la <b>voz</b> según lo que el poema transmite: más suave si es tierno, más fuerte si es enojado, más lenta si es triste. Leé en voz alta dos veces: la segunda, con intención.")]),
 S(2,"Qué me transmite",[P("Después de leer, preguntate: ¿qué <b>emoción</b> sentí? ¿Qué <b>imagen</b> apareció en mi cabeza? Un mismo poema puede emocionar a cada lector de manera distinta.")])],
 {"titulo":"leer","planteo":"Leé con pausas: «La luna es un barco de papel / que navega sobre el techo de la noche».","pasos":["Cada línea es un verso.","Pausa breve al terminar el primero.","Voz suave: la imagen es tierna."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Cada línea de un poema es un ___ .","Un grupo de versos es una ___ ."]},
 {"titulo":"tu turno","planteo":"Leé en voz alta un poema que te guste y contá qué emoción te dio."},
 {"titulo":"Leelo dos veces","texto":"La primera para entender; la segunda para sentirlo."},
 ["Leer un poema como si fuera una lista.","Ignorar las pausas."],
 RS(("Verso","Una línea."),("Estrofa","Grupo de versos."),("Pausas","Según los signos."),("Entonación","Según la emoción.")),
 G(("Verso","Línea de un poema."),("Estrofa","Grupo de versos."),("Entonación","Tono de voz al leer.")),
 ["¿Cómo se llama cada línea de un poema?","¿Cómo se llama el grupo de versos?","¿Se lee un poema solo para entender o también para sentirlo?","¿Qué pausa marca un punto: corta o larga?"],
 [["verso","el verso"],["estrofa","la estrofa"],["tambien para sentirlo","también para sentirlo","tambien","también","sentirlo"],["larga","pausa larga"]],
 {"incompleto":"Verso. Estrofa.","solo":"Leí con voz suave el poema de la luna y me dio ternura.","carpeta":["Verso.","Estrofa.","También para sentirlo.","Larga."]})
B2=NV("Vas a reconocer metáforas, comparaciones y personificaciones, y a explicar qué imagen crean.",["Comparación","Metáfora","Personificación","Imagen sensorial"],[
 S(1,"Comparación y metáfora",[T("Dos recursos",["Recurso","Cómo es","Ejemplo propio"],[["Comparación","Une dos cosas con como o parece","Tus manos, como pájaros inquietos"],["Metáfora","Dice que una cosa es otra","Tus manos son pájaros inquietos"]])]),
 S(1,"Qué hacen",[P("Sirven para <b>ver algo de otra manera</b>. Al comparar las manos con pájaros, el lector imagina movimiento y ligereza.")]),
 S(2,"Personificación",[D("Personificación","Dar a un animal, objeto o fenómeno cualidades humanas."),P("Ejemplo: <i>«El viento susurró un secreto a las hojas»</i>. El viento no susurra: se le da una acción humana.")]),
 S(2,"Imagen sensorial",[P("Una <b>imagen sensorial</b> apela a un sentido: <i>«olor a lluvia sobre la tierra caliente»</i> (olfato), <i>«luz de miel»</i> (vista y gusto).")])],
 {"titulo":"analizar","planteo":"«La noche es un manto negro». ¿Qué recurso es y qué imagen crea?","pasos":["Dice que la noche ES un manto: sin como.","Es una metáfora.","Crea la imagen de algo que cubre y abriga."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Dar cualidades humanas a un objeto es una ___ .","La metáfora dice que una cosa ___ otra."]},
 {"titulo":"tu turno","planteo":"Inventá una comparación, una metáfora y una personificación sobre el mar."},
 {"titulo":"Mirar distinto","texto":"Una buena metáfora te hace ver algo conocido como si fuera nuevo."},
 ["Confundir comparación y metáfora.","Explicar la imagen de forma literal."],
 RS(("Comparación","Con como."),("Metáfora","Una cosa es otra."),("Personificación","Cualidades humanas."),("Imagen","Apela a un sentido.")),
 G(("Metáfora","Decir que una cosa es otra."),("Comparación","Relacionar con como."),("Personificación","Dar rasgos humanos a lo que no es humano.")),
 ["«El viento susurró», ¿es una personificación o una comparación?","«Sus ojos son estrellas», ¿es metáfora o comparación?","¿Qué palabra usa la comparación: como o es?","Una imagen que apela al olfato, ¿es sensorial? Respondé sí o no."],
 [["personificacion","personificación","una personificacion","una personificación"],["metafora","metáfora","es metafora","es metáfora"],["como"],["si","sí"]],
 {"incompleto":"Personificación. Es.","solo":"El mar es un gigante dormido; el mar ruge como un león; el mar nos abraza con sus olas.","carpeta":["Personificación.","Metáfora.","Como.","Sí."]})
B3=NV("Vas a reconocer la rima consonante, la rima asonante y el verso libre.",["Qué es la rima","Consonante y asonante","Verso libre","Cómo se mide un verso"],[
 S(1,"La rima",[D("Rima","Coincidencia de sonidos al final de los versos, a partir de la última vocal acentuada."),P("La rima da música al poema, pero no todos los poemas riman.")]),
 S(1,"Consonante y asonante",[T("Dos tipos",["Rima","Qué coincide","Ejemplo"],[["Consonante","Todos los sonidos (vocales y consonantes)","canción / corazón"],["Asonante","Solo las vocales","gato / lado"]])]),
 S(2,"Verso libre",[P("El <b>verso libre</b> no tiene rima ni medida fija: el poeta decide cuándo termina cada verso según el ritmo y la emoción. Hoy muchos poemas son de verso libre.")]),
 S(2,"Medida del verso",[P("Los versos se miden contando sílabas, pero para empezar alcanza con notar si son <b>cortos o largos</b> y qué ritmo producen.")])],
 {"titulo":"clasificar","planteo":"¿«Sol» y «farol» tienen rima consonante o asonante?","pasos":["Terminan en -ol: coinciden todos los sonidos.","Es rima consonante."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Si coinciden solo las vocales, la rima es ___ .","El poema sin rima ni medida fija es de verso ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí dos versos con rima consonante y dos con rima asonante."},
 {"titulo":"Escuchá el final","texto":"Leé en voz alta y fijate qué sonidos se repiten al final."},
 ["Creer que todo poema tiene que rimar.","Confundir rima asonante con consonante."],
 RS(("Rima","Sonidos finales."),("Consonante","Todos coinciden."),("Asonante","Solo vocales."),("Verso libre","Sin rima fija.")),
 G(("Rima","Coincidencia de sonidos finales."),("Consonante","Todos los sonidos coinciden."),("Asonante","Solo coinciden las vocales.")),
 ["Si coinciden todos los sonidos, ¿la rima es consonante o asonante?","«Gato» y «lado», ¿riman en consonante o asonante?","El poema sin rima fija es de verso…","¿Todos los poemas tienen que rimar? Respondé sí o no."],
 [["consonante","es consonante"],["asonante","es asonante"],["libre","verso libre"],["no"]],
 {"incompleto":"Asonante. Libre.","solo":"Consonante: sol, farol. Asonante: gato, lado.","carpeta":["Consonante.","Asonante.","Libre.","No."]})
B4=NV("Vas a escribir un poema breve con una imagen, un recurso y una emoción.",["Elegir qué decir","Buscar imágenes","Escribir los versos","Revisar leyendo en voz alta"],[
 S(1,"Elegir qué decir",[P("Empezá con una <b>emoción</b> o un <b>momento</b> que quieras contar: la lluvia, un recuerdo, un miedo. Después decidí cómo mostrarlo con imágenes, no con explicaciones.")]),
 S(1,"Imágenes",[T("Banco de recursos",["Recurso","Ejemplo propio"],[["Comparación","La tarde pasaba lenta como un caracol"],["Metáfora","La lluvia es un tambor en el techo"],["Personificación","La ciudad bostezaba"]])]),
 S(2,"Escribir",[T("Pasos",["Paso","Qué hago"],[["1","Anoto ideas e imágenes"],["2","Elijo tres"],["3","Las ordeno en versos"],["4","Elijo si rimo o uso verso libre"]])]),
 S(2,"Revisar",[P("Leé el poema <b>en voz alta</b>: ¿suena bien? ¿Algún verso sobra? Sacá lo que explica demasiado y quedate con lo que se ve y se siente.")])],
 {"titulo":"armar","planteo":"Poema sobre la lluvia.","pasos":["Emoción: calma.","Imagen: la lluvia es un tambor suave.","Versos: La lluvia es un tambor / que toca sobre mi ventana.","Cierre: y yo, tranquila, escucho."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un poema se arma con imágenes y no con ___ .","Para revisar un poema se lee en voz ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un poema breve de entre cuatro y ocho versos."},
 {"titulo":"Mostrá, no expliques","texto":"En lugar de «estoy triste», mostrá la tristeza con una imagen."},
 ["Explicar la emoción en lugar de mostrarla.","No leer el poema en voz alta."],
 RS(("Emoción","Punto de partida."),("Imágenes","Comparación, metáfora."),("Versos","Corto y largo."),("Revisar","Voz alta.")),
 G(("Imagen","Recurso que hace ver algo."),("Verso libre","Sin rima fija."),("Revisar","Leer de nuevo y mejorar.")),
 ["¿Con qué se arma un poema: con imágenes o con explicaciones?","¿Cómo se revisa un poema?","¿Hay que rimar siempre? Respondé sí o no.","¿Cuántos versos tiene el poema que se pide: entre cuatro y ocho o cien?"],
 [["imagenes","imágenes","con imagenes","con imágenes"],["en voz alta","leyendolo en voz alta","leyéndolo en voz alta"],["no"],["entre cuatro y ocho","cuatro y ocho","4 y 8"]],
 {"incompleto":"Explicaciones. Alta.","solo":"Poema breve sobre la lluvia con una metáfora y verso libre.","carpeta":["Imágenes.","En voz alta.","No.","Entre cuatro y ocho."]})
ACT11={"1":[{"t":"ordering","p":"Ordená de menor a mayor.","o":["Estrofa","Verso","Poema"],"r":{"orden":["Verso","Estrofa","Poema"]},"e":"Verso, estrofa, poema."},MS("¿Qué conviene hacer al leer un poema en voz alta?",["Respetar las pausas","Cambiar la entonación según la emoción","Leer rápido sin sentir","Leerlo dos veces"],["Respetar las pausas","Cambiar la entonación según la emoción","Leerlo dos veces"],"No se lee como una lista.")],
 "2":[TT("Tocá la personificación: «El viento susurró un secreto a las hojas».",["El","viento","susurró","un","secreto","a","las","hojas"],[2],"Susurrar es una acción humana."),{"t":"classify","p":"¿Comparación o metáfora?","o":{"elementos":["Tus manos, como pájaros","Tus manos son pájaros","La noche es un manto","Brilla como una estrella"],"categorias":["Comparación","Metáfora"]},"r":{"categorias":{"Tus manos, como pájaros":"Comparación","Tus manos son pájaros":"Metáfora","La noche es un manto":"Metáfora","Brilla como una estrella":"Comparación"}},"e":"Con como o es."}],
 "3":[{"t":"matching","p":"Uní cada par con su rima.","o":{"izquierda":["sol / farol","gato / lado","canción / corazón","casa / mesa"],"derecha":["Consonante","Asonante","Consonante","Asonante"]},"r":{"pares":{"sol / farol":"Consonante","gato / lado":"Asonante","canción / corazón":"Consonante","casa / mesa":"Asonante"}},"e":"Solo vocales o todos los sonidos."},FB("El poema sin rima ni medida fija es de verso ___ .",[["libre"]],"Libre.")],
 "4":[KW("Escribí un poema breve de cuatro a ocho versos con una emoción, una imagen (comparación, metáfora o personificación) y su título.","Mostrá la emoción con imágenes; leelo en voz alta para revisar.","Poema de cuatro a ocho versos con título, una emoción clara y al menos un recurso (comparación, metáfora o personificación); no explica la emoción.","Se evalúa imagen, recurso y emoción."),MS("¿Qué recursos podés usar en un poema?",["Comparación","Metáfora","Personificación","Fórmula matemática"],["Comparación","Metáfora","Personificación"],"Las fórmulas matemáticas no son recursos poéticos.")],
 "5":[MC("Relámpago. Cada línea de un poema es un…",["Verso","Párrafo","Capítulo"],"Verso","Grupo: estrofa.",tiempo=20),VF("Relámpago. «El mar es un gigante» es una metáfora.","Verdadero","Dice que una cosa es otra.",tiempo=20),MC("Relámpago. Coinciden solo las vocales: rima…",["Asonante","Consonante","Libre"],"Asonante","Solo vocales.",tiempo=20),VF("Relámpago. Todos los poemas riman.","Falso","Hay verso libre.",tiempo=20)]}
EX11=[[1,MC("Cada línea de un poema es un…",["Verso","Capítulo","Párrafo","Título"],"Verso","Un conjunto de versos es una estrofa.")],
 [1,MS("Al leer un poema en voz alta conviene…",["Respetar las pausas","Usar la entonación adecuada","Leer como una lista","Leerlo dos veces"],["Respetar las pausas","Usar la entonación adecuada","Leerlo dos veces"],"No como una lista.")],
 [1,VF("Un punto marca una pausa larga.","Verdadero","Más larga que la coma.")],
 [2,MC("«La noche es un manto negro» es…",["Una metáfora","Una comparación","Una rima","Una estrofa"],"Una metáfora","No usa como.")],
 [2,MC("«El viento susurró» es…",["Una personificación","Una rima","Una pregunta","Un título"],"Una personificación","Susurrar es humano.")],
 [2,FB("Una comparación usa la palabra ___ .",[["como"]],"O parece.")],
 [3,MC("La rima en la que coinciden todos los sonidos es…",["Consonante","Asonante","Libre","Muda"],"Consonante","Sol y farol.")],
 [3,MC("«Gato» y «lado» riman en…",["Asonante","Consonante","Libre","Nada"],"Asonante","Solo vocales.")],
 [3,VF("En un poema de verso libre no hay rima fija.","Verdadero","El poeta decide.")],
 [4,MC("Un poema se arma con…",["Imágenes","Solo explicaciones","Fórmulas","Listas de compras"],"Imágenes","Se muestra la emoción.")],
 [4,FB("Para revisar un poema conviene leerlo en voz ___ .",[["alta"]],"Se oye el ritmo.")],
 [4,MS("Recursos poéticos:",["Comparación","Metáfora","Personificación","Dividir fracciones"],["Comparación","Metáfora","Personificación"],"Dividir fracciones es de Matemática.")],
 [4,VF("Hay que explicar la emoción en lugar de mostrarla con imágenes.","Falso","Se muestra, no se explica.")]]
M11={"subject_id":SID,"tema":11,"practica":"Práctica general: la poesía","examen_titulo":"Nivel jefe: la poesía","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT11,"examen":EX11}
for n,m in ((10,M10),(11,M11)):
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
STEPS={(10,1):"a2e0c52f-97ec-44d1-b426-60559dcdb149",(10,2):"91442418-3617-464f-a336-3327015bc762",(10,3):"7e2ca836-429f-4346-9ed2-bf44fea7be53",(10,4):"91961844-9105-4676-a3ef-402708333f47",(11,1):"be53950a-a3e7-4ca1-932f-ecd2d657b98e",(11,2):"c0284020-79da-452d-a4a3-0839c75df444",(11,3):"73cdc080-b436-4934-a959-071f22710e5a",(11,4):"3f322f49-dfce-457f-b2ae-fda9c2419a59"}
TIT={(10,1):"Carta formal e informal",(10,2):"Escribo un mail",(10,3):"Completo un formulario",(10,4):"Registros y destinatarios",(11,1):"Leo poemas en voz alta",(11,2):"Metáfora y comparación",(11,3):"Rima y verso libre",(11,4):"Escribo un poema"}
TU=lambda t,v:{"t":"consejo","titulo":"TU TURNO","texto":t,"emoji":"✍️","voz":v}
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
CLS={(10,1):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Hola directora, ¿me das permiso? 😅"},{"yo":True,"txt":"Eso no suena bien en una carta formal"},{"yo":False,"txt":"Tenés razón, lo cambio"}],"titulo":"CARTA FORMAL E INFORMAL","sub":"según a quién le escribo","voz":["Lu escribe: hola directora, ¿me das permiso?","Juan: eso no suena bien en una carta formal.","Lu: tenés razón, lo cambio.","Hoy: *carta formal e informal*."]},
 TB("PARTES",["Parte","Qué lleva"],[["Lugar y fecha","Dónde y cuándo"],["Destinatario","A quién va"],["Saludo","Estimado/a"],["Cuerpo","El mensaje"],["Despedida","Atentamente"],["Firma","Quien escribe"]],["Una carta tiene seis partes.","*Lugar y fecha*.","*Destinatario*.","*Saludo*.","*Cuerpo*.","*Despedida*.","Y *firma*."]),
 CMP(("FORMAL","Estimado Sr. Pérez; atentamente","🎩"),("INFORMAL","Querida Sofi; un abrazo","😊"),"vs",["Dos registros.","La *formal* es cuidada y respetuosa.","La *informal* es cercana."]),
 CL([("FORMAL","🎩"),("INFORMAL","😊")],[("Atentamente",0),("Un beso grande",1),("Estimada directora",0),("Querida Sofi",1)],["¿Formal o informal?","*Atentamente* y *estimada directora*: formales.","*Un beso grande* y *querida Sofi*: informales."]),
 Q("¿A quién se le escribe una carta formal?",["A una autoridad","A mi mejor amiga","A mi hermano"],0,["Te toca: ¿a quién se le escribe una carta formal?","¿A una autoridad, a mi mejor amiga o a mi hermano?","A una *autoridad*."]),
 TU("Escribí el saludo y la despedida de una carta formal y de una informal",["Ahora te toca: el saludo y la despedida.","Uno *formal* y uno *informal*."]),
 ER([("Hola, qué tal con una autoridad","Estimado/a y atentamente"),("Olvidar la firma","Firmar al final")],["Errores típicos.","Usar *hola, qué tal* con una autoridad.","Y *olvidar la firma*."]),
 RES(["Repasemos.","La carta tiene *seis partes*.","La *formal* es respetuosa.","La *informal* es cercana.","Elegí según *a quién* y *para qué*.","¡Clase terminada! Ahora, *a practicar*."],[["PARTES","seis"],["FORMAL","autoridades"],["INFORMAL","amigos"],["ELEGIR","a quién y para qué"]])],
(10,2):[
 {"t":"noticia","cinta":"BANDEJA","titular":"Mail sin asunto queda sin responder","bajada":"Nadie sabe de qué trata","emoji":"📧","titulo":"ESCRIBO UN MAIL","sub":"claro y breve","voz":["Bandeja de entrada: un mail sin asunto queda sin responder.","Nadie sabe de qué trata.","Hoy: *escribo un mail*."]},
 TB("PARTES DE UN MAIL",["Campo","Para qué"],[["Para","Destinatario"],["Asunto","De qué trata"],["Cuerpo","El mensaje"],["Adjunto","Archivo"]],["Los campos.","*Para*: el destinatario.","*Asunto*: de qué trata.","*Cuerpo*: el mensaje.","*Adjunto*: un archivo."]),
 PA("CUERPO",[("Saludo","👋"),("Motivo","🎯"),("Detalle","📝"),("Cierre","🙏"),("Firma","✍️")],["El cuerpo, en cinco pasos.","*Saludo*.","*Motivo*.","*Detalle*.","*Cierre* educado.","Y *firma*."]),
 CL([("BUEN ASUNTO","✅"),("MAL ASUNTO","❌")],[("Consulta: la tarea",0),("Hola",1),("Importante",1)],["¿Buen asunto o no?","*Consulta: la tarea*: buen asunto.","*Hola* e *importante*: no dicen nada."]),
 Q("Antes de enviar un mail, ¿qué conviene revisar?",["Adjunto y destinatario","Solo el color","Nada"],0,["Te toca: antes de enviar, ¿qué conviene revisar?","¿Adjunto y destinatario, solo el color o nada?","*Adjunto y destinatario*."]),
 TU("Escribí un mail a un docente pidiendo una aclaración",["Ahora te toca: escribí un mail a un docente.","Con *asunto*, *saludo*, *motivo*, *cierre* y *firma*."]),
 ER([("Asunto vacío","Asunto concreto"),("Dos pedidos en un mail","Un mail, un motivo")],["Errores típicos.","Dejar el *asunto vacío*.","Y mezclar *dos pedidos* en un mail."]),
 RES(["Repasemos.","El *asunto* dice de qué trata.","El cuerpo lleva *saludo*, *motivo*, *cierre* y *firma*.","Revisá el *adjunto*.","Y un mail, *un motivo*.","¡Clase terminada! Ahora, *a practicar*."],[["ASUNTO","concreto"],["CUERPO","cinco pasos"],["ADJUNTO","revisarlo"],["MOTIVO","uno por mail"]])],
(10,3):[
 {"t":"reto","texto":"¿Qué se hace primero con un formulario?","segundos":6,"respuesta":"Leer las instrucciones","emoji":"📋","titulo":"COMPLETO UN FORMULARIO","sub":"datos exactos","voz":["Desafío: ¿qué se hace primero con un formulario? Seis segundos.","Leer las instrucciones.","Hoy: *completo un formulario*."]},
 DEF("Formulario","Documento con campos para completar datos","📋",["Un *formulario* tiene campos para completar datos.","Sirve para inscribirse o pedir un trámite."]),
 PA("ORDEN",[("Leer instrucciones","📖"),("Completar campos","✏️"),("Revisar","🔍"),("Firmar","✍️")],["El orden es siempre el mismo.","*Leer* las instrucciones.","*Completar* los campos.","*Revisar*.","Y *firmar*."]),
 CL([("OBLIGATORIO","⚠️"),("OPCIONAL","➖")],[("Nombre completo",0),("DNI",0),("Segundo teléfono",1)],["¿Obligatorio u opcional?","*Nombre completo* y *DNI*: obligatorios.","*Segundo teléfono*: opcional."]),
 DA("05/10/2012","fecha","bien escrita","Si el formulario pide día, mes y año, no la escribas al revés","📅",["Atención al formato de la fecha.","Si pide *día, mes y año*, se escribe 05/10/2012.","No al revés."]),
 Q("¿Qué se hace antes de entregar un formulario?",["Revisarlo","Dibujar en él","Perderlo"],0,["Te toca: antes de entregar un formulario.","¿Revisarlo, dibujar en él o perderlo?","*Revisarlo*."]),
 ER([("Dejar un campo obligatorio vacío","Completarlo siempre"),("Fecha en otro formato","Respetar el formato pedido")],["Errores típicos.","Dejar un *campo obligatorio vacío*.","Y escribir la *fecha* en otro formato."]),
 RES(["Repasemos.","Primero *leé* las instrucciones.","Completá los campos *obligatorios*.","Los datos tienen que ser *exactos*.","Y *revisá* antes de entregar.","¡Clase terminada! Ahora, *a practicar*."],[["LEER","primero"],["OBLIGATORIOS","no omitir"],["DATOS","exactos"],["REVISAR","antes de entregar"]])],
(10,4):[
 {"t":"antesdespues","antes":{"cab":"INFORMAL","emoji":"😎","texto":"Che, pasame el horario"},"despues":{"cab":"FORMAL","emoji":"🎩","texto":"¿Podría indicarme el horario, por favor?"},"titulo":"REGISTROS Y DESTINATARIOS","sub":"cambiar según a quién escribo","voz":["Informal: che, pasame el horario.","Formal: ¿podría indicarme el horario, por favor?","Hoy: *registros y destinatarios*."]},
 DEF("Registro","Manera de escribir según con quién hablo","🎚️",["El *registro* es la manera de escribir según con quién hablo.","Cambia según el destinatario y la situación."]),
 TB("TRES REGISTROS",["Registro","Cuándo"],[["Formal","Autoridades"],["Neutro","Textos comunes"],["Informal","Amigos y familia"]],["Tres registros.","*Formal*, con autoridades.","*Neutro*, en textos comunes.","*Informal*, con amigos y familia."]),
 CL([("FORMAL","🎩"),("INFORMAL","😎")],[("Le solicito",0),("¿Cuándo es, che?",1),("Atentamente",0)],["¿Formal o informal?","*Le solicito* y *atentamente*: formales.","*¿Cuándo es, che?*: informal."]),
 DEF("Evitar","Abreviaturas de chat en textos formales","🚫",["En un texto formal evitá las *abreviaturas de chat*.","Y la jerga con desconocidos."]),
 Q("¿Qué registro usás con una autoridad?",["Formal","Informal","Jerga"],0,["Te toca: ¿qué registro con una autoridad?","¿Formal, informal o jerga?","*Formal*."]),
 ER([("Jerga con un desconocido","Registro formal"),("Rígido con un amigo","Registro informal")],["Errores típicos.","Usar *jerga* con un desconocido.","Y ser *rígido* con un amigo."]),
 RES(["Repasemos.","El *registro* se elige según el destinatario.","*Formal* con autoridades.","*Informal* con amigos.","Y el mismo mensaje *cambia* según a quién va.","¡Clase terminada! Ahora, *a practicar*."],[["REGISTRO","según destinatario"],["FORMAL","autoridades"],["INFORMAL","amigos"],["ADAPTAR","mismo mensaje"]])],
(11,1):[
 {"t":"gancho","grande":"Cómo suena","emoji":"🎙️","final":"importa tanto como qué dice","titulo":"LEO POEMAS EN VOZ ALTA","sub":"versos, pausas y entonación","voz":["Un poema no es solo lo que dice.","Importa *cómo suena*.","Hoy: *leo poemas en voz alta*."]},
 DEF("Verso","Cada línea de un poema","📜",["Cada línea de un poema es un *verso*.","Un grupo de versos es una *estrofa*."]),
 TB("PAUSAS",["Signo","Pausa"],[["Coma","Corta"],["Punto","Larga"],["Fin de verso","Breve"]],["Las pausas.","La *coma*: pausa corta.","El *punto*: pausa larga.","El *fin de verso* sin signo: pausa breve."]),
 CAU(("Entonación según la emoción",'🎙️'),[("Ternura: voz suave","🌸"),("Enojo: voz fuerte","🔥"),("Tristeza: voz lenta","🌧️")],["Cambiá la voz según lo que transmite.","Si es tierno, *suave*.","Si es enojado, *fuerte*.","Si es triste, *lenta*."]),
 CL([("PAUSA CORTA","➖"),("PAUSA LARGA","⏸️")],[("Coma",0),("Punto",1)],["¿Pausa corta o larga?","La *coma*: corta.","El *punto*: larga."]),
 Q("¿Cómo se llama cada línea de un poema?",["Verso","Párrafo","Capítulo"],0,["Te toca: cada línea de un poema.","¿Verso, párrafo o capítulo?","*Verso*."]),
 ER([("Leer como una lista","Leer con ritmo y emoción"),("Ignorar las pausas","Respetarlas")],["Errores típicos.","Leer un poema *como una lista*.","Y *ignorar las pausas*."]),
 RES(["Repasemos.","El *verso* es una línea.","La *estrofa* es un grupo de versos.","Respetá las *pausas*.","Y cambiá la *entonación* según la emoción.","¡Clase terminada! Ahora, *a practicar*."],[["VERSO","línea"],["ESTROFA","grupo"],["PAUSAS","por signos"],["ENTONACIÓN","emoción"]])],
(11,2):[
 {"t":"reto","texto":"Completá: «La luna es un ___ de papel».","segundos":6,"respuesta":"Barco, por ejemplo: es una metáfora","emoji":"🌙","titulo":"METÁFORA Y COMPARACIÓN","sub":"ver de otra manera","voz":["Desafío: completá. La luna es un, qué, de papel. Seis segundos.","Barco, por ejemplo. Eso es una metáfora.","Hoy: *metáfora y comparación*."]},
 CMP(("COMPARACIÓN","Con «como»: manos como pájaros","🕊️"),("METÁFORA","Sin «como»: manos son pájaros","🕊️"),"vs",["Dos recursos.","La *comparación* usa *como*.","La *metáfora* dice que una cosa *es* otra."]),
 DEF("Personificación","Dar cualidades humanas a lo que no es humano","🌬️",["La *personificación* da cualidades humanas a un objeto.","El viento susurra un secreto: el viento no susurra, pero lo decimos así."]),
 CL([("COMPARACIÓN","➗"),("METÁFORA","🔁"),("PERSONIFICACIÓN","🧑")],[("Como una estrella",0),("Noche, un manto",1),("El viento susurró",2)],["¿Qué recurso es?","*Como una estrella*: comparación.","*Noche, un manto*: metáfora.","*El viento susurró*: personificación."]),
 DEF("Imagen sensorial","Apela a un sentido","👃",["Una *imagen sensorial* apela a un sentido.","Como el olor a lluvia sobre la tierra caliente."]),
 Q("«El mar es un gigante dormido» es una…",["Metáfora","Comparación","Rima"],0,["Te toca: «el mar es un gigante dormido».","¿Metáfora, comparación o rima?","Una *metáfora*: no usa como."]),
 ER([("Confundir comparación y metáfora","Mirar si usa como"),("Explicarla literalmente","Pensar la imagen")],["Errores típicos.","*Confundir* comparación y metáfora.","Y explicar la imagen *literalmente*."]),
 RES(["Repasemos.","La *comparación* usa como.","La *metáfora* dice que una cosa es otra.","La *personificación* da rasgos humanos.","Y la *imagen sensorial* apela a un sentido.","¡Clase terminada! Ahora, *a practicar*."],[["COMPARACIÓN","como"],["METÁFORA","es otra cosa"],["PERSONIFICACIÓN","rasgos humanos"],["IMAGEN","un sentido"]])],
(11,3):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Sol rima con farol 🌞"},{"yo":True,"txt":"¿Y gato con lado?"},{"yo":False,"txt":"Casi: solo coinciden las vocales"}],"titulo":"RIMA Y VERSO LIBRE","sub":"consonante y asonante","voz":["Lu dice: sol rima con farol.","Juan: ¿y gato con lado?","Lu: casi, solo coinciden las vocales.","Hoy: *rima y verso libre*."]},
 DEF("Rima","Coincidencia de sonidos al final del verso","🎶",["La *rima* es la coincidencia de sonidos al final de los versos.","Da música al poema."]),
 CMP(("CONSONANTE","Coinciden todos los sonidos: sol, farol","🔔"),("ASONANTE","Coinciden solo las vocales: gato, lado","🔕"),"vs",["Dos tipos de rima.","*Consonante*: coinciden todos los sonidos.","*Asonante*: coinciden solo las vocales."]),
 CL([("CONSONANTE","🔔"),("ASONANTE","🔕")],[("sol / farol",0),("gato / lado",1),("canción / corazón",0),("casa / mesa",1)],["¿Consonante o asonante?","*Sol / farol* y *canción / corazón*: consonantes.","*Gato / lado* y *casa / mesa*: asonantes."]),
 DEF("Verso libre","Sin rima ni medida fija","🕊️",["El *verso libre* no tiene rima ni medida fija.","El poeta decide según el ritmo y la emoción."]),
 Q("¿Todos los poemas tienen que rimar?",["No","Sí","Solo los de amor"],0,["Te toca: ¿todos los poemas tienen que rimar?","¿No, sí o solo los de amor?","*No*: hay verso libre."]),
 ER([("Todo poema rima","Hay verso libre"),("Asonante igual a consonante","Asonante solo vocales")],["Errores típicos.","Creer que *todo poema rima*.","Y confundir *asonante* con *consonante*."]),
 RES(["Repasemos.","La *rima* son sonidos finales.","*Consonante*: todos coinciden.","*Asonante*: solo las vocales.","Y el *verso libre* no rima.","¡Clase terminada! Ahora, *a practicar*."],[["RIMA","sonidos finales"],["CONSONANTE","todos"],["ASONANTE","vocales"],["VERSO LIBRE","sin rima fija"]])],
(11,4):[
 {"t":"noticia","cinta":"TALLER","titular":"Hoy escribís tu primer poema","bajada":"Con una imagen y una emoción","emoji":"🖋️","titulo":"ESCRIBO UN POEMA","sub":"mostrar, no explicar","voz":["Taller: hoy escribís tu primer poema.","Con una imagen y una emoción.","Hoy: *escribo un poema*."]},
 PA("PASOS",[("Anoto ideas","📝"),("Elijo tres imágenes","🖼️"),("Las ordeno en versos","📜"),("Leo en voz alta","🎙️")],["Cuatro pasos.","*Anotá* ideas.","*Elegí* tres imágenes.","*Ordenalas* en versos.","Y *leé en voz alta*."]),
 CMP(("EXPLICAR","Estoy triste","🙁"),("MOSTRAR","La tarde llueve en mi ventana","🌧️"),"→",["Mostrá, no expliques.","Explicar: *estoy triste*.","Mostrar: *la tarde llueve en mi ventana*."]),
 TB("BANCO DE RECURSOS",["Recurso","Ejemplo"],[["Comparación","Lenta como un caracol"],["Metáfora","La lluvia es un tambor"],["Personificación","La ciudad bostezaba"]],["Algunos recursos.","*Comparación*: lenta como un caracol.","*Metáfora*: la lluvia es un tambor.","*Personificación*: la ciudad bostezaba."]),
 Q("¿Cómo se revisa un poema?",["Leyéndolo en voz alta","Sin leerlo","Cambiando el título"],0,["Te toca: ¿cómo se revisa un poema?","¿Leyéndolo en voz alta, sin leerlo o cambiando el título?","*Leyéndolo en voz alta*."]),
 TU("Escribí un poema breve de entre cuatro y ocho versos",["Ahora te toca: escribí un poema breve.","Entre *cuatro y ocho versos*, con una *imagen* y una *emoción*."]),
 ER([("Explicar la emoción","Mostrarla con una imagen"),("No leerlo en voz alta","Leerlo para revisar")],["Errores típicos.","*Explicar* la emoción.","Y *no leerlo* en voz alta."]),
 RES(["Repasemos.","Partí de una *emoción*.","Mostrala con *imágenes*.","Ordenalas en *versos*.","Y *revisá* leyendo en voz alta.","¡Clase terminada! Ahora, *a practicar*."],[["EMOCIÓN","punto de partida"],["IMÁGENES","mostrar"],["VERSOS","ordenar"],["REVISAR","voz alta"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"leng1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Lengua y Literatura I","titulo":TIT[(m,n)],"sub":f"Lengua y Literatura I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"leng1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
