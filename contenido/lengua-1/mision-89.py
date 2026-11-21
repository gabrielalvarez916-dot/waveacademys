# -*- coding: utf-8 -*-
"""Lengua y Literatura I · Misión 8 (La descripción) y Misión 9 (El fantasma de Canterville, segunda parte)."""
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
# ================= MISIÓN 8: LA DESCRIPCIÓN =================
A1=NV("Vas a describir a una persona: cómo es por fuera, cómo es por dentro y cómo se junta todo en un retrato.",["Retrato físico","Retrato psicológico","Orden de la descripción","Un retrato completo"],[
 S(1,"Qué es describir",[D("Descripción","Texto que muestra cómo es algo o alguien con palabras, para que el lector lo pueda imaginar."),P("Describir no es hacer una lista: es elegir los rasgos que mejor muestran a la persona.")]),
 S(1,"Dos retratos",[T("Cómo se describe a una persona",["Tipo","Qué muestra","Ejemplo"],[["Retrato físico","Cómo se ve","Alta, de pelo corto y ojos claros"],["Retrato psicológico","Cómo es su carácter","Generosa, impaciente, divertida"]])]),
 S(2,"Orden",[P("Conviene seguir un orden: de lo general a lo particular (altura, edad, cuerpo), después los rasgos del rostro y por último la forma de ser. También se puede empezar por un detalle que llame la atención.")]),
 S(2,"Retrato completo",[P("Un buen retrato une lo físico con el carácter: <i>\"Tenía las manos curtidas y la mirada cansada, pero cuando reía se le llenaba la cara de arrugas simpáticas\"</i>. El rasgo físico sugiere cómo es por dentro.")])],
 {"titulo":"mejorar","planteo":"Mejorá: «Mi abuelo es grande y bueno».","pasos":["Elegir un rasgo físico concreto: manos grandes y arrugadas.","Elegir un rasgo de carácter con un ejemplo: siempre guarda caramelos para sus nietos.","Versión: Mi abuelo tiene manos grandes y arrugadas, y siempre guarda caramelos para sus nietos."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La descripción de cómo se ve alguien es el retrato ___ .","La descripción de su carácter es el retrato ___ ."]},
 {"titulo":"tu turno","planteo":"Describí a una persona que conozcas con un rasgo físico y un rasgo de carácter."},
 {"titulo":"Mostrá con detalles","texto":"En vez de \"es simpático\", contá algo que haga y que lo muestre simpático."},
 ["Hacer una lista de rasgos sin ordenar.","Usar solo adjetivos vagos como lindo o bueno."],
 RS(("Descripción","Muestra cómo es."),("Físico","Cómo se ve."),("Psicológico","Cómo es su carácter."),("Orden","De lo general a lo particular.")),
 G(("Retrato","Descripción de una persona."),("Rasgo","Característica que distingue a alguien."),("Carácter","Forma de ser de una persona.")),
 ["¿Cómo se llama la descripción del aspecto de una persona?","¿Cómo se llama la descripción de la forma de ser de una persona?","Un buen retrato, ¿es una lista de rasgos o una selección de rasgos? Respondé \"lista\" o \"selección\".","¿Qué conviene mostrar: un ejemplo de lo que hace o un adjetivo vago?"],
 [["retrato fisico","retrato físico","fisico","físico","descripcion fisica","descripción física"],["retrato psicologico","retrato psicológico","psicologico","psicológico","descripcion psicologica","descripción psicológica"],["seleccion","selección"],["un ejemplo","ejemplo","un ejemplo de lo que hace"]],
 {"incompleto":"Físico. Psicológico.","solo":"Mi abuela es baja y de manos fuertes; siempre tiene un mate listo para quien llega.","carpeta":["Retrato físico.","Retrato psicológico.","Selección.","Un ejemplo."]})
A2=NV("Vas a describir un lugar con orden, usando los sentidos y conectores de ubicación.",["Orden espacial","Los cinco sentidos","Conectores de lugar","Un lugar con atmósfera"],[
 S(1,"Orden espacial",[P("Para describir un lugar se recorre con la mirada en un orden: de afuera hacia adentro, de arriba hacia abajo o de izquierda a derecha. Así el lector puede armarse el lugar en la cabeza.")]),
 S(1,"Los sentidos",[T("No solo se ve",["Sentido","Ejemplo"],[["Vista","Paredes descascaradas, luz amarilla"],["Oído","El zumbido de la heladera"],["Olfato","Olor a pan recién hecho"],["Tacto","El frío del piso de baldosas"],["Gusto","Un aire con sabor a sal"]])]),
 S(2,"Conectores de lugar",[T("Para ubicar",["Función","Ejemplos"],[["Cerca","junto a, al lado de, frente a"],["Lejos","al fondo, más allá, detrás de"],["Arriba y abajo","sobre, debajo de, en lo alto"]])]),
 S(2,"Atmósfera",[P("Los detalles elegidos crean una <b>atmósfera</b>: si hablo de sombras, humedad y silencio, el lugar parece triste o misterioso; si hablo de luz, risas y olor a pan, parece cálido.")])],
 {"titulo":"ordenar","planteo":"Ordená la descripción de una habitación.","pasos":["Primero lo que se ve al entrar: una puerta de madera.","Después, al fondo, una ventana con cortinas.","Por último, sobre el escritorio, una lámpara encendida."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Recorrer un lugar de afuera hacia adentro es un orden ___ .","El conjunto de sensaciones que transmite un lugar es la ___ ."]},
 {"titulo":"tu turno","planteo":"Describí tu habitación usando al menos tres sentidos."},
 {"titulo":"Cerrá los ojos","texto":"Imaginate en el lugar y anotá qué oís, qué olés y qué tocás, no solo qué ves."},
 ["Describir saltando de un lado a otro sin orden.","Describir solo con la vista."],
 RS(("Orden","De afuera hacia adentro."),("Sentidos","Vista, oído, olfato, tacto, gusto."),("Conectores","Junto a, al fondo."),("Atmósfera","Lo que transmite.")),
 G(("Atmósfera","Clima que transmite un lugar."),("Espacial","Del espacio."),("Conector","Palabra que une ideas.")),
 ["¿Cómo se llama el clima que transmite un lugar?","¿Cuántos sentidos conviene usar: solo la vista o varios?","¿Qué conector uso para ubicar algo cerca: junto a o más allá?","Recorrer el lugar con un orden, ¿ayuda al lector? Respondé sí o no."],
 [["atmosfera","atmósfera","la atmosfera","la atmósfera"],["varios","varios sentidos"],["junto a"],["si","sí"]],
 {"incompleto":"Espacial. Atmósfera.","solo":"Al entrar, un piso de baldosas frías; al fondo, una ventana con olor a jazmín.","carpeta":["Atmósfera.","Varios.","Junto a.","Sí."]})
A3=NV("Vas a elegir adjetivos precisos y usar comparaciones y metáforas para que la descripción diga más.",["Adjetivos precisos","Evitar palabras vagas","Comparación y metáfora","Elegir el mejor"],[
 S(1,"Adjetivos precisos",[D("Adjetivo calificativo","Palabra que dice cómo es un sustantivo."),T("Vago y preciso",["Vago","Preciso"],[["Una casa linda","Una casa luminosa y ordenada"],["Un chico malo","Un chico caprichoso"],["Una comida rica","Una comida picante y humeante"]])]),
 S(1,"Palabras vagas",[P("Palabras como <b>lindo, bueno, malo, cosa</b> dicen poco. Reemplazalas por adjetivos que muestren: no \"un día feo\", sino \"un día gris y ventoso\".")]),
 S(2,"Comparación y metáfora",[T("Dos recursos",["Recurso","Cómo funciona","Ejemplo"],[["Comparación","Usa como o parece","Sus manos eran frías como el hielo"],["Metáfora","Dice que una cosa es otra","Sus manos eran dos bloques de hielo"]])]),
 S(2,"Elegir",[P("No hace falta llenar todo de adjetivos: conviene elegir <b>pocos y buenos</b>. Un adjetivo exacto vale más que tres que se parecen.")])],
 {"titulo":"reemplazar","planteo":"Reemplazá lindo: «una plaza linda».","pasos":["Pensar qué hace linda a la plaza.","Hay árboles y sombra: frondosa.","Versión: una plaza frondosa y tranquila."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La comparación usa la palabra ___ o parece.","La metáfora dice que una cosa ___ otra."]},
 {"titulo":"tu turno","planteo":"Escribí tres oraciones con un adjetivo preciso, una comparación y una metáfora."},
 {"titulo":"Mostrar, no decir","texto":"Un buen adjetivo muestra algo que el lector puede ver, oír o sentir."},
 ["Repetir lindo y bueno.","Usar tres adjetivos que significan lo mismo."],
 RS(("Calificativo","Dice cómo es."),("Vago","Lindo, bueno."),("Comparación","Con como."),("Metáfora","Una cosa es otra.")),
 G(("Calificativo","Adjetivo que dice cómo es algo."),("Metáfora","Decir que una cosa es otra."),("Comparación","Relación entre dos cosas con como.")),
 ["«Sus ojos eran como dos luces», ¿es una comparación o una metáfora?","«Sus ojos eran dos luces», ¿es una comparación o una metáfora?","¿Qué palabra es más vaga: lindo o luminoso?","¿Conviene usar muchos adjetivos parecidos o pocos y exactos? Respondé \"muchos\" o \"pocos\"."],
 [["comparacion","comparación","es una comparacion","es una comparación"],["metafora","metáfora","es una metafora","es una metáfora"],["lindo","lindo."],["pocos","pocos y exactos"]],
 {"incompleto":"Como. Es.","solo":"Una plaza frondosa; sus ramas eran como paraguas; el sol era una moneda.","carpeta":["Comparación.","Metáfora.","Lindo.","Pocos."]})
A4=NV("Vas a revisar una descripción pobre y reescribirla con rasgos concretos, sentidos y orden.",["Qué falla","Revisar con preguntas","Reescribir","Comparar versiones"],[
 S(1,"Qué falla",[T("Problemas comunes",["Problema","Ejemplo"],[["Palabras vagas","Era una casa linda"],["Sin orden","Salto de la puerta al techo y vuelvo al jardín"],["Repeticiones","Tiene, tiene, tiene"],["Sin sentidos","Solo dice cómo se ve"]])]),
 S(1,"Preguntas de revisión",[T("Preguntate",["Pregunta","Si la respuesta es no..."],[["¿Se entiende cómo es?","Agregar rasgos concretos"],["¿Hay orden?","Reordenar"],["¿Uso más de un sentido?","Sumar sentidos"],["¿Hay palabras vagas?","Cambiarlas"]])]),
 S(2,"Reescribir",[P("Reescribir no es copiar: es <b>conservar la idea y mejorar la forma</b>. Cambiá lo vago por lo preciso, ordená y sumá un detalle de otro sentido.")]),
 S(2,"Comparar versiones",[T("Antes y después",["Antes","Después"],[["La casa era linda y tenía cosas","La casa, de paredes amarillas, olía a pan y tenía un patio con macetas"]])])],
 {"titulo":"reescribir","planteo":"Reescribí: «Mi barrio es lindo y hay gente».","pasos":["Cambiar lindo por un adjetivo preciso: tranquilo.","Cambiar gente por un detalle: vecinos que toman mate en la vereda.","Versión: Mi barrio es tranquilo, con vecinos que toman mate en la vereda."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Reescribir es conservar la idea y mejorar la ___ .","Lo vago se cambia por lo ___ ."]},
 {"titulo":"tu turno","planteo":"Reescribí una descripción tuya mejorando tres cosas."},
 {"titulo":"Tres mejoras","texto":"Cambiá una palabra vaga, sumá un sentido y ordená los datos."},
 ["Copiar el texto sin cambiarlo.","Corregir solo las tildes y creer que ya mejoró."],
 RS(("Revisar","Con preguntas."),("Reescribir","Mejorar la forma."),("Concreto","Mejor que vago."),("Orden","Antes de escribir.")),
 G(("Reescribir","Escribir de nuevo mejorando."),("Concreto","Que se puede ver o sentir.")),
 ["Reescribir, ¿es copiar o mejorar?","¿Qué se cambia por lo preciso?","Una descripción con solo vista, ¿puede mejorar sumando sentidos? Respondé sí o no.","¿Qué se conserva al reescribir: la idea o la forma?"],
 [["mejorar"],["lo vago","vago","las palabras vagas"],["si","sí"],["la idea","idea"]],
 {"incompleto":"Forma. Preciso.","solo":"Mi barrio es tranquilo, con vecinos que toman mate en la vereda.","carpeta":["Mejorar.","Lo vago.","Sí.","La idea."]})
ACT8={"1":[TT("Tocá las palabras que describen el aspecto físico: «Es un hombre alto, de pelo canoso, muy generoso y bromista».",["Es","un","hombre","alto","de","pelo","canoso","muy","generoso","y","bromista"],[3,5,6],"Alto y pelo canoso son rasgos físicos; generoso y bromista son de carácter."),MS("¿Qué rasgos son del retrato psicológico?",["Generosa","De ojos claros","Impaciente","De pelo corto"],["Generosa","Impaciente"],"El carácter es la forma de ser.")],
 "2":[FB("Para describir un lugar se recorre de ___ hacia adentro, usando varios ___ .",[["afuera"],["sentidos"]],"Orden espacial y sentidos."),{"t":"classify","p":"¿Qué sentido aparece?","o":{"elementos":["Olor a pan","Paredes descascaradas","El zumbido de la heladera","El frío del piso"],"categorias":["Vista","Oído","Olfato","Tacto"]},"r":{"categorias":{"Olor a pan":"Olfato","Paredes descascaradas":"Vista","El zumbido de la heladera":"Oído","El frío del piso":"Tacto"}},"e":"Cada detalle apela a un sentido."}],
 "3":[VF("«Sus manos eran dos bloques de hielo» es una comparación.","Falso","Es una metáfora: no usa como."),{"t":"ordering","p":"Ordená de más vago a más preciso.","o":["una casa luminosa y ordenada","una casa","una casa linda"],"r":{"orden":["una casa","una casa linda","una casa luminosa y ordenada"]},"e":"Cada versión dice más."}],
 "4":[KW("Reescribí esta descripción pobre: «Mi abuela es buena y tiene una casa linda con cosas». Cambiá lo vago por lo concreto, sumá un sentido y mantené un orden.","Usá adjetivos precisos, al menos un detalle de olor, sonido o tacto, y un orden claro.","Descripción reescrita con adjetivos precisos (no lindo ni bueno), un rasgo de carácter con ejemplo, detalle de otro sentido (olor, sonido o tacto) y orden espacial claro.","Se evalúa precisión, orden y sentidos."),FB("Reescribir es conservar la ___ y mejorar la forma.",[["idea"]],"La idea se mantiene.")],
 "5":[MC("Relámpago. La descripción del carácter es el retrato…",["Psicológico","Físico","Digital"],"Psicológico","Cómo es por dentro.",tiempo=20),VF("Relámpago. Un lugar se describe solo con la vista.","Falso","Conviene usar varios sentidos.",tiempo=20),MC("Relámpago. «Sus ojos eran como luces» es…",["Una comparación","Una metáfora","Un título"],"Una comparación","Usa como.",tiempo=20),VF("Relámpago. Reescribir es copiar el texto.","Falso","Es mejorarlo.",tiempo=20)]}
EX8=[[1,MC("¿Qué es una descripción?",["Un texto que muestra cómo es algo o alguien","Un texto que da órdenes","Una noticia","Una carta"],"Un texto que muestra cómo es algo o alguien","Para que el lector lo imagine.")],
 [1,MS("Rasgos del retrato físico:",["Alta","Generosa","De pelo corto","Impaciente"],["Alta","De pelo corto"],"Lo físico es lo que se ve.")],
 [1,VF("Un buen retrato es una lista de rasgos sin orden.","Falso","Se eligen y ordenan los rasgos.")],
 [2,MC("Un orden espacial posible es…",["De afuera hacia adentro","Al azar","Solo por tamaño de letra","Alfabético"],"De afuera hacia adentro","Ayuda a imaginar el lugar.")],
 [2,FB("La descripción de un lugar usa varios ___ además de la vista.",[["sentidos"]],"Oído, olfato, tacto y gusto.")],
 [2,VF("«Junto a» es un conector de lugar.","Verdadero","Sirve para ubicar.")],
 [3,MC("¿Cuál es el adjetivo más preciso?",["frondosa","linda","buena","cosa"],"frondosa","Muestra algo concreto.")],
 [3,MC("«Sus manos eran dos bloques de hielo» es…",["Una metáfora","Una comparación","Un diálogo","Una rima"],"Una metáfora","No usa como.")],
 [3,VF("Conviene usar pocos adjetivos exactos.","Verdadero","Valen más que muchos parecidos.")],
 [4,MC("Reescribir es…",["Mejorar la forma conservando la idea","Copiar","Borrar todo","Cambiar la idea"],"Mejorar la forma conservando la idea","No es copiar.")],
 [4,MS("¿Qué conviene revisar en una descripción?",["Palabras vagas","Orden","Sentidos","El color del papel"],["Palabras vagas","Orden","Sentidos"],"El papel no cambia el texto.")],
 [4,FB("Lo vago se cambia por lo ___ .",[["preciso","concreto"]],"Preciso o concreto.")],
 [4,VF("Corregir solo tildes mejora la descripción.","Falso","También hay que mejorar el contenido.")]]
M8={"subject_id":SID,"tema":8,"practica":"Práctica general: la descripción","examen_titulo":"Nivel jefe: la descripción","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT8,"examen":EX8}

# ================= MISIÓN 9: CANTERVILLE, SEGUNDA PARTE =================
B1=NV("Vas a reconocer cómo se resuelve el conflicto de «El fantasma de Canterville» y por qué su final sorprende.",["El giro","Virginia y el fantasma","El final","Por qué sorprende"],[
 S(1,"El giro",[P("Hasta aquí el fantasma intentó asustar y la familia lo ignoró. En la segunda parte cambia el tono: Sir Simon está cansado y <b>necesita ayuda</b>. Esa es la <b>crisis</b>: el conflicto se vuelve serio.")]),
 S(1,"Virginia y el fantasma",[D("Clímax","Momento de mayor tensión de una historia, donde el conflicto llega a su punto más alto."),P("Virginia, la hija de los Otis, es la única que lo escucha. El fantasma le cuenta su historia y le pide que rece por él para poder descansar en paz.")]),
 S(2,"El final",[T("Qué ocurre",["Momento","Hecho"],[["Pedido","Sir Simon pide a Virginia que rece por él"],["Prueba","Virginia lo acompaña y reza"],["Resolución","El fantasma encuentra la paz"],["Cierre","La familia recibe un cofre de joyas"]])]),
 S(2,"Por qué sorprende",[P("El final sorprende porque la historia empezó como una <b>parodia</b> y termina con un gesto serio y emotivo: lo gracioso deja lugar a la compasión. Virginia, que sentía pena por el fantasma, logra lo que nadie había conseguido.")])],
 {"titulo":"identificar","planteo":"¿Qué cambia entre el comienzo y el final del cuento?","pasos":["Al comienzo se ríen del fantasma.","Al final alguien lo comprende y lo ayuda.","El humor da paso a la compasión."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["El momento de mayor tensión de una historia es el ___ .","La hija de los Otis que ayuda al fantasma es ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí en dos oraciones por qué el final te sorprende o no."},
 {"titulo":"Buscá el giro","texto":"Un final sorprende cuando cambia lo que esperabas desde el comienzo."},
 ["Pensar que el cuento sigue siendo solo una burla.","Olvidar quién ayuda al fantasma."],
 RS(("Crisis","El fantasma pide ayuda."),("Clímax","Máxima tensión."),("Resolución","Descansa en paz."),("Sorpresa","Del humor a la compasión.")),
 G(("Clímax","Punto de mayor tensión."),("Resolución","Cómo se resuelve el conflicto."),("Compasión","Pena por el sufrimiento de otro.")),
 ["¿Quién ayuda al fantasma?","¿Qué le pide Sir Simon a Virginia?","¿Cómo se llama el momento de mayor tensión?","El final, ¿es solo humorístico o también emotivo? Respondé \"humorístico\" o \"emotivo\"."],
 [["virginia"],["que rece","rezar","que rece por el","que rece por él","una oracion","una oración"],["climax","clímax","el climax","el clímax"],["emotivo","tambien emotivo","también emotivo"]],
 {"incompleto":"Clímax. Virginia.","solo":"Me sorprende porque esperaba que siguiera la burla y termina con compasión.","carpeta":["Virginia.","Que rece por él.","Clímax.","Emotivo."]})
B2=NV("Vas a distinguir personajes que cambian de los que no cambian y explicar qué los transforma.",["Personajes dinámicos y estáticos","Cómo cambia Sir Simon","Cómo cambia Virginia","Qué los transforma"],[
 S(1,"Dinámicos y estáticos",[T("Dos clases",["Clase","Qué pasa","Ejemplo"],[["Dinámico","Cambia a lo largo de la historia","Sir Simon: de orgulloso a agradecido"],["Estático","Casi no cambia","Los Otis: siempre prácticos"]])]),
 S(1,"Cómo cambia Sir Simon",[P("Al principio quiere asustar y se siente muy orgulloso. Al final está cansado, triste y agradecido: pide ayuda y descansa. Cambia porque nadie le tiene miedo y porque alguien se compadece de él.")]),
 S(2,"Cómo cambia Virginia",[P("Virginia empieza como una chica común y termina mostrando <b>valentía y compasión</b>: se atreve a acompañar al fantasma y a ayudarlo. Es el personaje que más madura.")]),
 S(2,"Qué los transforma",[T("Causas del cambio",["Personaje","Qué lo cambia"],[["Sir Simon","El fracaso y la compasión de Virginia"],["Virginia","Enfrentarse al miedo para ayudar"]])])],
 {"titulo":"clasificar","planteo":"¿Sir Simon es dinámico o estático?","pasos":["Al principio es orgulloso y quiere asustar.","Al final está agradecido y descansa.","Cambió: es dinámico."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Un personaje que cambia es ___ .","Virginia muestra valentía y ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí cómo era un personaje al principio y cómo es al final."},
 {"titulo":"Antes y después","texto":"Para ver el cambio, compará cómo es al principio y cómo es al final."},
 ["Creer que todos los personajes cambian.","Decir que cambia sin explicar por qué."],
 RS(("Dinámico","Cambia."),("Estático","No cambia."),("Sir Simon","Del orgullo a la gratitud."),("Virginia","Valentía y compasión.")),
 G(("Dinámico","Que cambia."),("Estático","Que no cambia."),("Valentía","Valor para enfrentar el miedo.")),
 ["Un personaje que cambia, ¿es dinámico o estático?","Los Otis, ¿son dinámicos o estáticos?","¿Qué valor muestra Virginia al enfrentar el miedo?","Sir Simon pasa del orgullo a la…"],
 [["dinamico","dinámico","es dinamico","es dinámico"],["estaticos","estáticos","son estaticos","son estáticos"],["valentia","valentía","valor","coraje"],["gratitud","agradecimiento","tristeza"]],
 {"incompleto":"Dinámico. Compasión.","solo":"Virginia: al principio una chica común; al final valiente y compasiva.","carpeta":["Dinámico.","Estáticos.","Valentía.","Gratitud."]})
B3=NV("Vas a comparar el libro con una versión audiovisual (película, serie o dibujo animado) y reconocer qué cambia al adaptar.",["Qué es una adaptación","Qué se compara","Ventajas de cada medio","Una comparación"],[
 S(1,"Adaptación",[D("Adaptación","Versión de una obra en otro medio, por ejemplo de un libro a una película."),P("Adaptar es transformar: se cambia el lenguaje (palabras por imágenes y sonido), y a menudo se agregan, sacan o modifican escenas.")]),
 S(1,"Qué se compara",[T("Criterios",["Criterio","Pregunta"],[["Personajes","¿Son como en el libro?"],["Ambiente","¿Cómo se ve el castillo?"],["Hechos","¿Qué se agregó o se sacó?"],["Final","¿Es igual o distinto?"],["Humor","¿Se mantiene la ironía?"]])]),
 S(2,"Ventajas de cada medio",[T("Libro y pantalla",["Libro","Versión audiovisual"],[["Cada lector imagina a su manera","Muestra rostros, lugares y sonidos"],["Cuenta pensamientos con palabras","Usa música, luz y actuación"],["Se lee a su ritmo","Dura un tiempo fijo"]])]),
 S(2,"Comparar con orden",[P("Para comparar, usá un cuadro con los criterios y anotá qué pasa en cada versión. Después sacá una <b>conclusión fundamentada</b>: cuál te gustó más y por qué, con ejemplos.")])],
 {"titulo":"comparar","planteo":"¿Qué puede mostrar mejor una película que el libro?","pasos":["Los rostros y gestos de los personajes.","El castillo y la música de misterio.","El libro, en cambio, muestra pensamientos con palabras."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Una versión de una obra en otro medio es una ___ .","Para comparar uso un cuadro de ___ ."]},
 {"titulo":"tu turno","planteo":"Elegí un criterio y comparé el libro con una versión audiovisual."},
 {"titulo":"Cuadro primero","texto":"Armá el cuadro antes de opinar: así tu conclusión tiene pruebas."},
 ["Decir que la película es mejor sin explicar por qué.","Olvidar que cada medio tiene sus ventajas."],
 RS(("Adaptación","Otro medio."),("Criterios","Personajes, ambiente, hechos."),("Medios","Cada uno con ventajas."),("Conclusión","Con ejemplos.")),
 G(("Adaptación","Versión de una obra en otro medio."),("Criterio","Aspecto que se compara."),("Medio","Forma de comunicar.")),
 ["¿Cómo se llama una versión de un libro en otro medio?","¿Qué se arma antes de opinar: un cuadro o un chiste?","¿Qué puede mostrar mejor la pantalla: rostros o pensamientos con palabras?","¿Cada medio tiene ventajas propias? Respondé sí o no."],
 [["adaptacion","adaptación","una adaptacion","una adaptación"],["cuadro","un cuadro"],["rostros","los rostros"],["si","sí"]],
 {"incompleto":"Adaptación. Criterios.","solo":"En el libro los pensamientos se cuentan con palabras; la película muestra gestos y música.","carpeta":["Adaptación.","Un cuadro.","Rostros.","Sí."]})
B4=NV("Vas a escribir una reseña con datos, resumen sin adelantar el final, valoración y recomendación.",["Qué es una reseña","Partes","Sin adelantar el final","Valorar con argumentos"],[
 S(1,"Qué es una reseña",[D("Reseña","Texto breve que presenta una obra, la resume y da una opinión fundamentada para recomendarla o no."),P("Se escribe para que otro lector decida si quiere leer la obra.")]),
 S(1,"Partes",[T("Estructura",["Parte","Qué lleva"],[["Datos","Título, autor, género"],["Resumen","De qué trata, sin contar el final"],["Valoración","Opinión con argumentos"],["Recomendación","A quién le puede gustar"]])]),
 S(2,"Sin adelantar el final",[P("En el resumen se cuenta el comienzo y el conflicto, pero <b>no el final</b>: arruinar la sorpresa le quita gusto al lector.")]),
 S(2,"Valorar con argumentos",[P("Una valoración vale cuando se apoya en ejemplos: \"me hizo reír porque el fantasma se toma muy en serio\". Usá conectores como <b>porque, por ejemplo, en conclusión</b>.")])],
 {"titulo":"armar","planteo":"Armá una reseña breve de «El fantasma de Canterville».","pasos":["Datos: escrito por Oscar Wilde, relato gótico y humorístico.","Resumen: una familia compra un castillo con fantasma y no se asusta.","Valoración: es divertido porque el fantasma se toma muy en serio.","Recomendación: para quienes disfrutan del humor y el misterio."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Una reseña da una opinión ___ .","En el resumen no se cuenta el ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí una reseña breve de un libro, película o serie que conozcas."},
 {"titulo":"Sin spoilers","texto":"Contá lo suficiente para despertar interés, pero guardá el final."},
 ["Contar el final en el resumen.","Opinar sin dar razones."],
 RS(("Reseña","Presenta y valora."),("Datos","Título y autor."),("Resumen","Sin final."),("Recomendación","A quién le gusta.")),
 G(("Reseña","Texto que presenta y valora una obra."),("Valoración","Opinión sobre la obra."),("Spoiler","Adelantar el final.")),
 ["¿Cómo se llama el texto que presenta una obra y da una opinión?","¿Qué no se cuenta en el resumen de una reseña?","¿La valoración necesita argumentos? Respondé sí o no.","¿Qué parte dice a quién le puede gustar la obra?"],
 [["resena","reseña","una resena","una reseña"],["el final","final"],["si","sí"],["recomendacion","recomendación","la recomendacion","la recomendación"]],
 {"incompleto":"Fundamentada. Final.","solo":"Reseña breve con datos, resumen sin final, valoración con ejemplo y recomendación.","carpeta":["Reseña.","El final.","Sí.","Recomendación."]})
ACT9={"1":[MS("¿Qué ocurre en el final del cuento?",["El fantasma pide ayuda a Virginia","Virginia reza por él","El fantasma encuentra la paz","La familia huye del castillo"],["El fantasma pide ayuda a Virginia","Virginia reza por él","El fantasma encuentra la paz"],"La familia no huye."),{"t":"ordering","p":"Ordená la segunda parte.","o":["El fantasma descansa en paz","El fantasma pide ayuda","Virginia reza por él"],"r":{"orden":["El fantasma pide ayuda","Virginia reza por él","El fantasma descansa en paz"]},"e":"Crisis, clímax y resolución."}],
 "2":[{"t":"classify","p":"¿Dinámico o estático?","o":{"elementos":["Sir Simon","Los Otis","Virginia"],"categorias":["Dinámico","Estático"]},"r":{"categorias":{"Sir Simon":"Dinámico","Los Otis":"Estático","Virginia":"Dinámico"}},"e":"Sir Simon y Virginia cambian."},FB("Sir Simon pasa del orgullo a la ___ .",[["gratitud","agradecimiento"]],"Al final agradece.")],
 "3":[{"t":"matching","p":"Uní cada criterio con su pregunta.","o":{"izquierda":["Personajes","Ambiente","Hechos","Final"],"derecha":["¿Son como en el libro?","¿Cómo se ve el castillo?","¿Qué se agregó o sacó?","¿Es igual o distinto?"]},"r":{"pares":{"Personajes":"¿Son como en el libro?","Ambiente":"¿Cómo se ve el castillo?","Hechos":"¿Qué se agregó o sacó?","Final":"¿Es igual o distinto?"}},"e":"Cada criterio tiene su pregunta."},VF("Una adaptación es siempre idéntica al libro.","Falso","Se cambian cosas al pasar de medio.")],
 "4":[KW("Escribí una reseña breve de «El fantasma de Canterville» (o de otra obra que conozcas) con datos, un resumen sin el final, una valoración con un argumento y una recomendación.","Usá las cuatro partes y al menos un conector (porque, por ejemplo).","Reseña con datos (título, autor, género), resumen breve sin contar el final, valoración con argumento y ejemplo, y recomendación final.","Se evalúa estructura, argumentos y que no cuente el final."),TT("Tocá las palabras que son una opinión: «El cuento es divertido y el fantasma, muy gracioso».",["El","cuento","es","divertido","y","el","fantasma","muy","gracioso"],[3,8],"Divertido y gracioso son valoraciones.")],
 "5":[MC("Relámpago. El momento de mayor tensión es el…",["Clímax","Título","Prólogo"],"Clímax","Máxima tensión.",tiempo=20),VF("Relámpago. Los Otis cambian mucho a lo largo del cuento.","Falso","Son estáticos.",tiempo=20),MC("Relámpago. Una versión en otro medio es una…",["Adaptación","Rima","Fábula"],"Adaptación","Libro a película.",tiempo=20),VF("Relámpago. La reseña cuenta el final.","Falso","Se evita.",tiempo=20)]}
EX9=[[1,MC("¿Quién ayuda al fantasma?",["Virginia","Washington","Lord Canterville","Los gemelos"],"Virginia","Reza por él.")],
 [1,MS("Hechos del final:",["Virginia reza por el fantasma","El fantasma descansa","El castillo se destruye","Los Otis se mudan"],["Virginia reza por el fantasma","El fantasma descansa"],"El castillo sigue.")],
 [1,VF("El final sorprende porque pasa del humor a la compasión.","Verdadero","Cambia el tono.")],
 [2,MC("Un personaje que cambia es…",["Dinámico","Estático","Secundario","Plano"],"Dinámico","Evoluciona.")],
 [2,FB("Virginia muestra valentía y ___ .",[["compasion","compasión"]],"Ayuda al fantasma.")],
 [2,VF("Los Otis son personajes estáticos.","Verdadero","Casi no cambian.")],
 [3,MC("Una versión de una obra en otro medio es…",["Una adaptación","Una reseña","Un prólogo","Una rima"],"Una adaptación","Cambia el lenguaje.")],
 [3,MS("Criterios para comparar libro y película:",["Personajes","Ambiente","Final","Tamaño del cine"],["Personajes","Ambiente","Final"],"El tamaño del cine no es un criterio.")],
 [3,VF("Cada medio tiene ventajas propias.","Verdadero","El libro cuenta pensamientos; la pantalla muestra imágenes.")],
 [4,MC("Una reseña…",["Presenta y valora una obra","Cuenta todo el final","Es una orden","Es una carta"],"Presenta y valora una obra","Con argumentos.")],
 [4,FB("En el resumen de una reseña no se cuenta el ___ .",[["final"]],"Para no arruinar la sorpresa.")],
 [4,MC("¿Qué parte dice a quién le puede gustar la obra?",["Recomendación","Datos","Resumen","Título"],"Recomendación","Cierra la reseña.")],
 [4,VF("Una valoración necesita argumentos.","Verdadero","Si no, es solo gusto.")]]
M9={"subject_id":SID,"tema":9,"practica":"Práctica general: El fantasma de Canterville, segunda parte","examen_titulo":"Nivel jefe: El fantasma de Canterville, segunda parte","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT9,"examen":EX9}
for n,m in ((8,M8),(9,M9)):
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
STEPS={(8,1):"7d3f3e86-c42b-42d3-97e8-0f7779389453",(8,2):"1172a97d-f35b-4a8c-ae05-fb7bd81bb1fb",(8,3):"1ef00669-9876-46bd-b080-5eafa8fc8892",(8,4):"d0f0e51e-61c7-48d4-8110-fb33d5c1a4ec",(9,1):"94351222-b38d-4ae2-bdd6-915c413fecbc",(9,2):"b920ef72-c182-4ebd-87c6-9ffaaa804b76",(9,3):"c5cfa4f1-f01d-4846-b1dd-d74d4ada8387",(9,4):"a8476b20-35d3-4d28-b1eb-aae7b765ba9b"}
TIT={(8,1):"Describir una persona",(8,2):"Describir un lugar",(8,3):"Adjetivos que dicen más",(8,4):"Reescribo una descripción",(9,1):"Un final que sorprende",(9,2):"Los personajes cambian",(9,3):"Comparo el libro con una versión audiovisual",(9,4):"Escribo una reseña"}
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
CLS={(8,1):[
 {"t":"reto","texto":"Describí a tu abuelo en una oración sin usar «bueno» ni «grande».","segundos":8,"respuesta":"Con un rasgo concreto, por ejemplo: manos arrugadas","emoji":"🧓","titulo":"DESCRIBIR UNA PERSONA","sub":"retrato físico y psicológico","voz":["Desafío: describí a tu abuelo en una oración, sin usar bueno ni grande. Ocho segundos.","Con un rasgo concreto, por ejemplo, manos arrugadas.","Hoy: *describir una persona*."]},
 DEF("Descripción","Muestra cómo es alguien con palabras","🖼️",["Una *descripción* muestra cómo es algo o alguien con palabras.","No es una lista: se eligen los *rasgos* que mejor lo muestran."]),
 CMP(("FÍSICO","Cómo se ve","👀"),("PSICOLÓGICO","Cómo es su carácter","💭"),"+",["Hay dos retratos.","El *físico* dice cómo se ve.","El *psicológico* dice cómo es su carácter."]),
 CL([("FÍSICO","👀"),("CARÁCTER","💭")],[("Pelo corto",0),("Generosa",1),("Ojos claros",0),("Impaciente",1)],["¿Físico o carácter?","*Pelo corto* y *ojos claros*: físicos.","*Generosa* e *impaciente*: de carácter."]),
 PA("ORDEN",[("Rasgos generales","📏"),("Rostro","🙂"),("Forma de ser","💭")],["Conviene seguir un orden.","Primero los *rasgos generales*.","Después el *rostro*.","Y por último la *forma de ser*."]),
 Q("¿Qué conviene mostrar en lugar de un adjetivo vago?",["Algo que la persona hace","Otro adjetivo vago","Nada"],0,["Te toca: en lugar de un adjetivo vago.","¿Algo que la persona hace, otro adjetivo vago o nada?","*Algo que hace*."]),
 TU("Describí a una persona que conozcas con un rasgo físico y uno de carácter",["Ahora te toca: describí a una persona que conozcas.","Un *rasgo físico* y uno de *carácter*."]),
 ER([("Una lista sin orden","Rasgos elegidos y ordenados"),("Solo «lindo» y «bueno»","Detalles concretos")],["Errores típicos.","Hacer una *lista sin orden*.","Y usar solo *adjetivos vagos*."]),
 RES(["Repasemos.","Describir es *mostrar*.","Hay retrato *físico* y *psicológico*.","Se sigue un *orden*.","Y se usan detalles *concretos*.","¡Clase terminada! Ahora, *a practicar*."],[["DESCRIPCIÓN","mostrar"],["FÍSICO","cómo se ve"],["CARÁCTER","cómo es"],["ORDEN","general a particular"]])],
(8,2):[
 {"t":"gancho","grande":"5 sentidos","emoji":"👃","final":"para describir un lugar","titulo":"DESCRIBIR UN LUGAR","sub":"orden y sentidos","voz":["Un lugar no se describe solo con los ojos.","Tenés cinco sentidos para usar.","Hoy: *describir un lugar*."]},
 CAU(("Orden posible",'🧭'),[("De afuera hacia adentro","🚪"),("De arriba hacia abajo","⬇️"),("De izquierda a derecha","➡️")],["Para ordenar un lugar hay tres caminos.","De *afuera hacia adentro*.","De *arriba hacia abajo*.","O de *izquierda a derecha*."]),
 TB("LOS SENTIDOS",["Sentido","Ejemplo"],[["Vista","Paredes descascaradas"],["Oído","Zumbido de la heladera"],["Olfato","Olor a pan"],["Tacto","Piso frío"]],["Un ejemplo de cada sentido.","*Vista*: paredes descascaradas.","*Oído*: el zumbido de la heladera.","*Olfato*: olor a pan.","*Tacto*: el piso frío."]),
 TB("CONECTORES DE LUGAR",["Función","Ejemplo"],[["Cerca","junto a"],["Lejos","al fondo"],["Arriba","sobre"]],["Conectores para ubicar.","*Junto a* para lo que está cerca.","*Al fondo* para lo lejano.","*Sobre* para lo que está arriba."]),
 DEF("Atmósfera","El clima que transmite un lugar","🌫️",["La *atmósfera* es el clima que transmite un lugar.","Con sombras y silencio, un lugar parece misterioso."]),
 CL([("VISTA","👀"),("OÍDO","👂"),("OLFATO","👃")],[("Luz amarilla",0),("Zumbido",1),("Olor a café",2)],["¿Qué sentido?","*Luz amarilla*: vista.","*Zumbido*: oído.","*Olor a café*: olfato."]),
 Q("¿Cuántos sentidos conviene usar al describir un lugar?",["Varios","Solo uno","Ninguno"],0,["Te toca: ¿cuántos sentidos conviene usar?","¿Varios, solo uno o ninguno?","*Varios*."]),
 TU("Describí tu habitación con al menos tres sentidos",["Ahora te toca: describí tu habitación.","Usá al menos *tres sentidos*."]),
 RES(["Repasemos.","Describí con un *orden*.","Usá varios *sentidos*.","Ubicá con *conectores*.","Y cuidá la *atmósfera*.","¡Clase terminada! Ahora, *a practicar*."],[["ORDEN","de afuera adentro"],["SENTIDOS","cinco"],["CONECTORES","junto a, al fondo"],["ATMÓSFERA","clima"]])],
(8,3):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Mi casa es linda 🏠"},{"yo":True,"txt":"¿Linda cómo? No la veo 🤔"},{"yo":False,"txt":"Luminosa, con olor a pan"}],"titulo":"ADJETIVOS QUE DICEN MÁS","sub":"precisión","voz":["Lu dice que su casa es linda.","Juan: ¿linda cómo? No la veo.","Lu: luminosa y con olor a pan. Ahora sí.","Hoy: *adjetivos que dicen más*."]},
 TB("VAGO Y PRECISO",["Vago","Preciso"],[["Casa linda","Casa luminosa"],["Chico malo","Chico caprichoso"],["Comida rica","Comida picante"]],["Del vago al preciso.","*Casa linda* pasa a *casa luminosa*.","*Chico malo* pasa a *chico caprichoso*.","*Comida rica* pasa a *comida picante*."]),
 CMP(("COMPARACIÓN","Usa «como»","🧊"),("METÁFORA","Dice que una cosa es otra","🧊"),"vs",["Dos recursos.","La *comparación* usa *como*.","La *metáfora* dice que una cosa *es* otra."]),
 CL([("COMPARACIÓN","➗"),("METÁFORA","🔁")],[("Frías como el hielo",0),("Manos de hielo",1),("Luz como una moneda",0),("Sol, una moneda",1)],["¿Comparación o metáfora?","Con *como*: comparación.","Sin *como*: metáfora."]),
 DEF("Pocos y exactos","Un adjetivo exacto vale más que tres parecidos","🎯",["Conviene usar *pocos* adjetivos y *exactos*.","Uno exacto vale más que tres parecidos."]),
 Q("«Sus ojos eran dos luces», ¿es una…?",["Metáfora","Comparación","Rima"],0,["Te toca: «sus ojos eran dos luces».","¿Metáfora, comparación o rima?","Es una *metáfora*: no usa como."]),
 ER([("Repetir lindo y bueno","Adjetivos precisos"),("Tres adjetivos iguales","Uno exacto")],["Errores típicos.","*Repetir* lindo y bueno.","Y usar *tres adjetivos iguales*."]),
 RES(["Repasemos.","Los *calificativos* dicen cómo es algo.","Mejor lo *preciso* que lo vago.","La *comparación* usa como.","Y la *metáfora* dice que una cosa es otra.","¡Clase terminada! Ahora, *a practicar*."],[["CALIFICATIVO","cómo es"],["VAGO","lindo, bueno"],["COMPARACIÓN","como"],["METÁFORA","es otra cosa"]])],
(8,4):[
 {"t":"antesdespues","antes":{"cab":"ANTES","emoji":"😐","texto":"Mi barrio es lindo y hay gente"},"despues":{"cab":"DESPUÉS","emoji":"😍","texto":"Mi barrio es tranquilo, con vecinos que toman mate"},"titulo":"REESCRIBO UNA DESCRIPCIÓN","sub":"mejorar la forma","voz":["Antes: mi barrio es lindo y hay gente.","Después: mi barrio es tranquilo, con vecinos que toman mate.","Hoy: *reescribo una descripción*."]},
 DEF("Reescribir","Conservar la idea y mejorar la forma","✏️",["*Reescribir* es conservar la idea y mejorar la forma.","No es copiar."]),
 TB("QUÉ FALLA",["Problema","Ejemplo"],[["Vago","Casa linda"],["Sin orden","Salta de lugar"],["Repite","Tiene, tiene"],["Un sentido","Solo vista"]],["Problemas comunes.","Palabras *vagas*.","Falta de *orden*.","*Repeticiones*.","Y un solo *sentido*."]),
 PA("REVISAR",[("¿Se entiende?","❓"),("¿Hay orden?","🧭"),("¿Más de un sentido?","👃"),("¿Palabras vagas?","✂️")],["Cuatro preguntas para revisar.","¿Se *entiende*?","¿Hay *orden*?","¿Hay más de un *sentido*?","¿Quedan palabras *vagas*?"]),
 CL([("MEJORA","✅"),("NO MEJORA","❌")],[("Lindo a luminoso",0),("Copiar igual",1),("Sumar un olor",0)],["¿Mejora o no?","*Lindo a luminoso* y *sumar un olor*: mejoran.","*Copiar igual*: no mejora."]),
 Q("Reescribir, ¿es copiar o mejorar?",["Mejorar","Copiar","Borrar"],0,["Te toca: reescribir.","¿Mejorar, copiar o borrar?","*Mejorar*."]),
 TU("Reescribí una descripción tuya mejorando tres cosas",["Ahora te toca: reescribí una descripción tuya.","Mejorá *tres cosas*: lo vago, los sentidos y el orden."]),
 ER([("Copiar el texto","Mejorar la forma"),("Corregir solo tildes","Mejorar el contenido")],["Errores típicos.","*Copiar* el texto.","Y corregir *solo tildes*."]),
 RES(["Repasemos.","*Reescribir* es mejorar.","Se revisa con *preguntas*.","Se cambia lo *vago* por lo *concreto*.","Y se suman *sentidos*.","¡Clase terminada! Ahora, *a practicar*."],[["REESCRIBIR","mejorar"],["REVISAR","preguntas"],["VAGO","concreto"],["SENTIDOS","sumar"]])],
(9,1):[
 {"t":"noticia","cinta":"ÚLTIMA HORA","titular":"El fantasma pide ayuda a una chica","bajada":"Está cansado y quiere descansar","emoji":"👻","titulo":"UN FINAL QUE SORPRENDE","sub":"segunda parte","voz":["Última hora: el fantasma le pide ayuda a una chica.","Está cansado y quiere descansar.","Hoy: *un final que sorprende*."]},
 DEF("Crisis","El fantasma necesita ayuda","🆘",["La *crisis* llega cuando Sir Simon *necesita ayuda*.","El tono cambia: el conflicto se vuelve serio."]),
 DEF("Clímax","Máxima tensión","⚡",["El *clímax* es el momento de mayor tensión.","Aquí, cuando *Virginia* acompaña al fantasma."]),
 LN("EL FINAL",[("1","Sir Simon pide ayuda","🆘"),("2","Virginia reza por él","🙏"),("3","El fantasma descansa","🕊️"),("4","Un cofre de joyas","💎")],["Los hechos en orden.","Sir Simon *pide ayuda*.","Virginia *reza* por él.","El fantasma *descansa en paz*.","Y la familia recibe un *cofre de joyas*."]),
 CMP(("COMIENZO","Humor y burla","😂"),("FINAL","Compasión y emoción","🥹"),"→",["El tono cambia.","Al comienzo, *humor* y burla.","Al final, *compasión* y emoción."]),
 Q("¿Quién ayuda al fantasma?",["Virginia","Washington","Lord Canterville"],0,["Te toca: ¿quién ayuda al fantasma?","¿Virginia, Washington o Lord Canterville?","*Virginia*."]),
 TU("Escribí en dos oraciones por qué el final te sorprende o no",["Ahora te toca: escribí en dos oraciones.","Explicá por qué el *final* te sorprende o no."]),
 ER([("Sigue siendo solo una burla","Termina con compasión"),("Los Otis ayudan al fantasma","Ayuda Virginia")],["Errores típicos.","Creer que sigue siendo *solo burla*.","Y olvidar que ayuda *Virginia*."]),
 RES(["Repasemos.","La *crisis*: el fantasma pide ayuda.","El *clímax*: Virginia lo acompaña.","La *resolución*: descansa en paz.","Y la sorpresa: del humor a la *compasión*.","¡Clase terminada! Ahora, *a practicar*."],[["CRISIS","pide ayuda"],["CLÍMAX","máxima tensión"],["RESOLUCIÓN","descansa"],["SORPRESA","compasión"]])],
(9,2):[
 {"t":"reto","texto":"¿Sir Simon cambia a lo largo del cuento?","segundos":6,"respuesta":"Sí: de orgulloso a agradecido","emoji":"👻","titulo":"LOS PERSONAJES CAMBIAN","sub":"dinámicos y estáticos","voz":["Desafío: ¿Sir Simon cambia a lo largo del cuento? Seis segundos.","Sí: de orgulloso a agradecido.","Hoy: *los personajes cambian*."]},
 CMP(("DINÁMICO","Cambia","🔄"),("ESTÁTICO","Casi no cambia","⏸️"),"vs",["Dos clases de personajes.","El *dinámico* cambia.","El *estático* casi no cambia."]),
 CL([("DINÁMICO","🔄"),("ESTÁTICO","⏸️")],[("Sir Simon",0),("Los Otis",1),("Virginia",0)],["¿Dinámico o estático?","*Sir Simon* y *Virginia*: dinámicos.","*Los Otis*: estáticos."]),
 AD(("AL PRINCIPIO","😠","Orgulloso y quiere asustar"),("AL FINAL","🙏","Cansado y agradecido"),["Sir Simon cambia.","Al principio, *orgulloso* y quiere asustar.","Al final, *cansado* y *agradecido*."]),
 DEF("Valentía","Valor para enfrentar el miedo","💪",["*Virginia* muestra *valentía* y *compasión*.","Se atreve a acompañar al fantasma."]),
 Q("Un personaje que cambia es…",["Dinámico","Estático","Fantasma"],0,["Te toca: un personaje que cambia es…","¿Dinámico, estático o fantasma?","*Dinámico*."]),
 ER([("Todos los personajes cambian","Algunos son estáticos"),("Cambia sin motivo","Explicar qué lo cambia")],["Errores típicos.","Creer que *todos cambian*.","Y decir que cambia *sin explicar por qué*."]),
 RES(["Repasemos.","El *dinámico* cambia.","El *estático* no.","Sir Simon va del *orgullo* a la *gratitud*.","Y Virginia muestra *valentía* y *compasión*.","¡Clase terminada! Ahora, *a practicar*."],[["DINÁMICO","cambia"],["ESTÁTICO","no cambia"],["SIR SIMON","orgullo a gratitud"],["VIRGINIA","valentía"]])],
(9,3):[
 {"t":"chat","contacto":{"nombre":"Lu","emoji":"👧"},"mensajes":[{"yo":False,"txt":"Vi la película del fantasma 🎬"},{"yo":True,"txt":"¿Es igual al libro?"},{"yo":False,"txt":"No, cambian cosas 😮"}],"titulo":"LIBRO Y PANTALLA","sub":"comparo con una versión audiovisual","voz":["Lu vio una película del fantasma.","Juan: ¿es igual al libro?","Lu: no, cambian cosas.","Hoy: *comparo el libro con una versión audiovisual*."]},
 DEF("Adaptación","Versión de una obra en otro medio","🎬",["Una *adaptación* es una versión de una obra en otro medio.","Como pasar de un libro a una película."]),
 TB("QUÉ SE COMPARA",["Criterio","Pregunta"],[["Personajes","¿Son como en el libro?"],["Ambiente","¿Cómo se ve el castillo?"],["Hechos","¿Qué se agregó o sacó?"],["Final","¿Es igual?"]],["Los criterios.","*Personajes*: ¿son como en el libro?","*Ambiente*: ¿cómo se ve el castillo?","*Hechos*: ¿qué se agregó o sacó?","*Final*: ¿es igual?"]),
 CMP(("LIBRO","Pensamientos con palabras","📖"),("PANTALLA","Imagen, música y actuación","🎬"),"vs",["Cada medio tiene ventajas.","El *libro* cuenta pensamientos con palabras.","La *pantalla* muestra imágenes, música y actuación."]),
 CL([("LIBRO","📖"),("PANTALLA","🎬")],[("Cada lector imagina",0),("Música de misterio",1),("Se lee a tu ritmo",0),("Rostros y gestos",1)],["¿Libro o pantalla?","*Cada lector imagina* y *se lee a tu ritmo*: libro.","*Música* y *rostros*: pantalla."]),
 Q("¿Qué se arma antes de opinar?",["Un cuadro de criterios","Un chiste","Un dibujo"],0,["Te toca: ¿qué se arma antes de opinar?","¿Un cuadro de criterios, un chiste o un dibujo?","*Un cuadro de criterios*."]),
 ER([("La película es mejor porque sí","Dar razones con ejemplos"),("Una adaptación es idéntica","Siempre cambia algo")],["Errores típicos.","Opinar *sin razones*.","Y creer que una adaptación es *idéntica*."]),
 RES(["Repasemos.","Una *adaptación* cambia de medio.","Se comparan *criterios*.","Cada medio tiene *ventajas*.","Y la conclusión lleva *ejemplos*.","¡Clase terminada! Ahora, *a practicar*."],[["ADAPTACIÓN","otro medio"],["CRITERIOS","personajes, final"],["MEDIOS","ventajas"],["CONCLUSIÓN","con ejemplos"]])],
(9,4):[
 {"t":"noticia","cinta":"RECOMENDADO","titular":"Una reseña te cuenta si vale la pena","bajada":"Sin arruinar el final","emoji":"⭐","titulo":"ESCRIBO UNA RESEÑA","sub":"presentar y valorar","voz":["Recomendado: una reseña te cuenta si vale la pena.","Sin arruinar el final.","Hoy: *escribo una reseña*."]},
 DEF("Reseña","Presenta una obra y da una opinión fundamentada","⭐",["Una *reseña* presenta una obra y da una opinión *fundamentada*.","Sirve para que otro decida si la quiere leer."]),
 TB("PARTES",["Parte","Qué lleva"],[["Datos","Título y autor"],["Resumen","Sin el final"],["Valoración","Opinión con razones"],["Recomendación","A quién le gusta"]],["Las cuatro partes.","*Datos*: título y autor.","*Resumen*: sin el final.","*Valoración*: opinión con razones.","*Recomendación*: a quién le gusta."]),
 DEF("Spoiler","Adelantar el final","🚫",["Un *spoiler* es adelantar el final.","En una reseña se evita."]),
 CL([("SÍ","✅"),("NO","🚫")],[("Contar el comienzo",0),("Contar el final",1),("Dar un ejemplo",0)],["¿Va en una reseña?","*Contar el comienzo* y *dar un ejemplo*: sí.","*Contar el final*: no."]),
 Q("¿La valoración necesita argumentos?",["Sí","No","A veces nada"],0,["Te toca: ¿la valoración necesita argumentos?","¿Sí, no o a veces nada?","*Sí*."]),
 TU("Escribí una reseña breve de un libro, película o serie que conozcas",["Ahora te toca: escribí una reseña breve.","Con *datos*, *resumen sin final*, *valoración* y *recomendación*."]),
 ER([("Contar el final","Guardar la sorpresa"),("Opinar sin razones","Dar un ejemplo")],["Errores típicos.","*Contar el final*.","Y *opinar sin razones*."]),
 RES(["Repasemos.","La *reseña* presenta y valora.","Tiene *datos*, *resumen*, *valoración* y *recomendación*.","El resumen *no cuenta el final*.","Y la valoración lleva *argumentos*.","¡Clase terminada! Ahora, *a practicar*."],[["RESEÑA","presenta y valora"],["PARTES","cuatro"],["RESUMEN","sin final"],["VALORACIÓN","con razones"]])]}
for (m,n),es in CLS.items():
    json.dump({"slug":f"leng1-m{m}-n{n}","step_id":STEPS[(m,n)],"materia":"Lengua y Literatura I","titulo":TIT[(m,n)],"sub":f"Lengua y Literatura I · Misión {m} · Nivel {n}","escenas":es},open(os.path.join(RAIZ,f"leng1-m{m}-n{n}.json"),"w"),ensure_ascii=False,indent=1)
print("ok")
