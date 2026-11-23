# -*- coding: utf-8 -*-
"""Matemática II · Misión 8 · Ecuaciones de primer grado. Genera mision-8.json y 4 clases."""
from mat import *
DIL = lambda s, e, a, b, v: {"t":"dilema","situacion":s,"emoji":e,"a":{"txt":a[0],"consecuencia":a[1],"emoji":a[2]},"b":{"txt":b[0],"consecuencia":b[1],"emoji":b[2]},"voz":v}
B1=NV("Vas a resolver ecuaciones con paréntesis aplicando la propiedad distributiva y despejando la incógnita.",
 ["Quitar los paréntesis","Agrupar y despejar","Resolver paso a paso","Controlar los signos"],[
 S(1,"Ecuaciones con paréntesis",[D("Ecuación con paréntesis","Primero se <b>aplica la propiedad distributiva</b> para quitar los paréntesis y después se despeja la incógnita."),
  IM("Idea clave","2(x + 3) = 14 se transforma en 2x + 6 = 14.")]),
 S(1,"Sin paréntesis",[T("Distribuir",["Ecuación","Sin paréntesis"],[["2(x + 3) = 14","2x + 6 = 14"],["3(x − 1) = 12","3x − 3 = 12"],["4(x + 1) = 20","4x + 4 = 20"]])]),
 S(2,"Un ejemplo",[E("Resolver 2(x + 3) = 14","Se distribuye y se despeja.",["2x + 6 = 14.","2x = 8.","x = 4."])]),
 S(2,"Con resta",[E("Resolver 3(x − 1) = 12","Se distribuye el 3 también sobre el signo menos.",["3x − 3 = 12.","3x = 15.","x = 5."])])],
 {"titulo":"Distribuir y despejar","planteo":"Resolvé 2(x + 3) = 14.","pasos":["Se distribuye: 2x + 6 = 14.","Se resta 6: 2x = 8.","Se divide por 2: x = 4."]},
 {"titulo":"Completá","planteo":"Resolvé 3(x − 1) = 12.","pasos":["Se distribuye: 3x − 3 = 12.","Se suma 3: 3x = ___ .","x = 5."]},
 {"titulo":"tu turno","planteo":"Resolvé 4(x + 3) = 24 y comprobá el resultado."},
 {"titulo":"Distribuir todo","texto":"El número de afuera multiplica a todos los términos del paréntesis, también al que tiene signo menos."},
 ["Multiplicar solo el primer término del paréntesis.","Olvidar el signo menos al distribuir."],
 RS(("Distributiva","El número de afuera multiplica a cada término."),("Despejar","Pasar los términos para dejar sola la x."),("Operación inversa","Se deshace con la contraria."),("Comprobar","Reemplazar x en la ecuación.")),
 G(("Ecuación","Igualdad con una incógnita."),("Incógnita","Valor que hay que hallar."),("Miembro","Cada lado de la igualdad."),("Distribuir","Multiplicar por cada término.")),
 ["Resolvé 2(x + 3) = 14. ¿Cuánto vale x?","Resolvé 3(x − 1) = 12. ¿Cuánto vale x?","Resolvé 4(x + 3) = 24. ¿Cuánto vale x?","Un compañero resolvió 2(x + 3) = 14 como 2x + 3 = 14. ¿Cuánto vale x en realidad?"],
 ["aplicar","aplicar","aplicar","error"],
 [["4"],["5"],["3"],["4"]],
 {"incompleto":"5.","solo":"4x + 12 = 24, 4x = 12, x = 3.","carpeta":["4.","5.","3.","4: el 2 multiplica también al 3."]})
B2=NV("Vas a resolver ecuaciones con denominadores multiplicando ambos miembros por el mínimo común múltiplo.",
 ["Quitar denominadores","El mínimo común múltiplo","Resolver ecuaciones","Comprobar"],[
 S(1,"Denominadores",[D("Ecuación con denominadores","Para quitar los denominadores se <b>multiplican ambos miembros por el mínimo común múltiplo</b> de los denominadores."),
  IM("Idea clave","x/2 = 6 se resuelve multiplicando por 2: x = 12.")]),
 S(1,"Ejemplos",[T("Multiplicar por el mcm",["Ecuación","Se multiplica por","Resultado"],[["x/2 = 6","2","x = 12"],["x/3 + 1 = 5","3","x = 12"],["x/2 + x/3 = 5","6","x = 6"]])]),
 S(2,"Un denominador",[E("Resolver x/3 + 1 = 5","Primero se resta 1 y después se multiplica.",["Se resta 1: x/3 = 4.","Se multiplica por 3.","x = 12."])]),
 S(2,"Dos denominadores",[E("Resolver x/2 + x/3 = 5","El mcm de 2 y 3 es 6.",["Se multiplica por 6: 3x + 2x = 30.","5x = 30.","x = 6."])])],
 {"titulo":"Quitar el denominador","planteo":"Resolvé x/3 + 1 = 5.","pasos":["Se resta 1: x/3 = 4.","Se multiplica por 3.","x = 12."]},
 {"titulo":"Completá","planteo":"Resolvé x/2 + x/3 = 5.","pasos":["Se multiplica por 6: 3x + 2x = 30.","5x = 30, entonces x = ___ .","x = 6."]},
 {"titulo":"tu turno","planteo":"Resolvé x/5 + 2 = 6 y x/2 + x/4 = 6."},
 {"titulo":"Multiplicar todo","texto":"Cuando multiplicás por el mcm, multiplicá todos los términos de los dos miembros, no solo los que tienen denominador."},
 ["Multiplicar solo la fracción por el mcm.","Sumar los denominadores como si fueran números."],
 RS(("mcm","Mínimo común múltiplo de los denominadores."),("Multiplicar","Todos los términos por el mcm."),("Despejar","Dejar sola la x."),("Comprobar","Reemplazar en la ecuación original.")),
 G(("Denominador","Número de abajo de la fracción."),("mcm","Menor múltiplo común."),("Miembro","Lado de la igualdad."),("Término","Cada sumando de la ecuación.")),
 ["Resolvé x/2 = 6. ¿Cuánto vale x?","Resolvé x/5 + 2 = 6. ¿Cuánto vale x?","Resolvé x/2 + x/3 = 5. ¿Cuánto vale x?","Un compañero sumó x/2 + x/4 como 2x/6. Resolvé x/2 + x/4 = 6 bien. ¿Cuánto vale x?"],
 ["aplicar","aplicar","aplicar","error"],
 [["12"],["20"],["6"],["8"]],
 {"incompleto":"6.","solo":"x/5 = 4, entonces x = 20. Con x/2 + x/4 = 6 se multiplica por 4: 2x + x = 24, x = 8.","carpeta":["12.","20.","6.","8: el mcm es 4, no se suman los denominadores."]})
B3=NV("Vas a reconocer ecuaciones sin solución, con una solución y con infinitas soluciones (identidades).",
 ["Una, ninguna o infinitas","Sin solución","Identidades","Cómo decidir"],[
 S(1,"Tres casos",[D("Sin solución e identidad","Si al despejar queda una igualdad falsa, como 3 = 5, la ecuación <b>no tiene solución</b>. Si queda siempre verdadera, como 4 = 4, es una <b>identidad</b> con infinitas soluciones."),
  IM("Idea clave","x + 1 = x + 2 no tiene solución; 2x = x + x es una identidad.")]),
 S(1,"Clasificar",[T("Los tres casos",["Ecuación","Queda","Tipo"],[["x + 1 = x + 2","1 = 2","Sin solución"],["2x + 4 = 2(x + 2)","4 = 4","Identidad"],["3x = x + 4","x = 2","Una solución"]])]),
 S(2,"Sin solución",[E("Resolver 2x + 3 = 2x + 5","Se resta 2x en ambos miembros.",["Se resta 2x: 3 = 5.","Esa igualdad es falsa.","La ecuación no tiene solución."])]),
 S(2,"Identidad",[E("Resolver 3(x + 1) = 3x + 3","Se distribuye y se compara.",["3x + 3 = 3x + 3.","Se resta 3x: 3 = 3.","Siempre es verdadera: es una identidad."])])],
 {"titulo":"Sin solución","planteo":"Resolvé 2x + 3 = 2x + 5.","pasos":["Se resta 2x en los dos miembros.","Queda 3 = 5, que es falso.","No tiene solución."]},
 {"titulo":"Completá","planteo":"Resolvé 3x = x + 4.","pasos":["Se resta x: 2x = 4.","x = ___ .","La solución es 2."]},
 {"titulo":"tu turno","planteo":"Resolvé 4x + 2 = 2x + 10 y 5x − 3 = 3x + 7."},
 {"titulo":"Mirar el final","texto":"Después de despejar, mirá cómo queda: una igualdad falsa, siempre verdadera, o un valor para x."},
 ["Decir que x vale 1 cuando queda 3 = 5.","Confundir identidad con ecuación sin solución."],
 RS(("Sin solución","Queda una igualdad falsa."),("Identidad","Queda una igualdad siempre verdadera."),("Una solución","Queda x igual a un número."),("Decidir","Mirar cómo queda al despejar.")),
 G(("Sin solución","Ningún valor cumple la ecuación."),("Identidad","Todos los valores la cumplen."),("Igualdad falsa","Por ejemplo 3 = 5."),("Igualdad verdadera","Por ejemplo 4 = 4.")),
 ["Resolvé 3x = x + 4. ¿Cuánto vale x?","Resolvé 4x + 2 = 2x + 10. ¿Cuánto vale x?","Resolvé 5x − 3 = 3x + 7. ¿Cuánto vale x?","Un compañero dijo que 2x + 3 = 2x + 5 tiene solución x = 1. ¿Cuántas soluciones tiene en realidad? Escribí 0 si ninguna."],
 ["aplicar","aplicar","aplicar","error"],
 [["2"],["4"],["5"],["0"]],
 {"incompleto":"2.","solo":"4x + 2 = 2x + 10 da x = 4 y 5x − 3 = 3x + 7 da x = 5.","carpeta":["2.","4.","5.","0: queda 3 = 5, que es falso."]})
B4=NV("Vas a verificar si un valor es solución de una ecuación reemplazándolo y a escribir la solución completa.",
 ["Reemplazar el valor","Comparar los dos miembros","Escribir la solución","Detectar errores"],[
 S(1,"Verificar",[D("Verificar una solución","Para comprobar una solución se <b>reemplaza el valor en la ecuación</b> original: si los dos miembros dan lo mismo, la solución es correcta."),
  IM("Idea clave","Si x = 4 en 2x + 1 = 9, entonces 2 · 4 + 1 = 9: es correcto.")]),
 S(1,"Ejemplos",[T("¿Verifica?",["Ecuación","Valor","¿Verifica?"],[["2x + 1 = 9","x = 4","Sí"],["3x − 2 = 10","x = 5","No"],["x/2 + 1 = 4","x = 6","Sí"]])]),
 S(2,"Sí verifica",[E("Verificar x = 4 en 2x + 1 = 9","Se reemplaza y se calcula.",["2 · 4 + 1.","8 + 1 = 9.","Los dos miembros coinciden: es solución."])]),
 S(2,"No verifica",[E("Verificar x = 5 en 3x − 2 = 10","Se reemplaza y se calcula.",["3 · 5 − 2.","15 − 2 = 13.","13 no es 10: no es solución."])])],
 {"titulo":"Reemplazar","planteo":"Verificá si x = 4 es solución de 2x + 1 = 9.","pasos":["Se reemplaza: 2 · 4 + 1.","8 + 1 = 9.","Coincide con 9: sí es solución."]},
 {"titulo":"Completá","planteo":"Verificá si x = 6 es solución de x/2 + 1 = 4.","pasos":["Se reemplaza: 6 / 2 + 1.","3 + 1 = ___ .","Coincide con 4: sí es solución."]},
 {"titulo":"tu turno","planteo":"Resolvé 3x − 2 = 10 y verificá tu respuesta."},
 {"titulo":"Siempre comprobá","texto":"Reemplazar el valor en la ecuación original te avisa si te equivocaste al despejar."},
 ["Reemplazar en la ecuación ya transformada y no en la original.","Dar por buena la solución sin comprobar."],
 RS(("Verificar","Reemplazar el valor en la ecuación original."),("Coinciden","Los dos miembros dan lo mismo."),("No coinciden","El valor no es solución."),("Escribir","x = valor.")),
 G(("Verificar","Comprobar una solución."),("Reemplazar","Poner el número en lugar de la letra."),("Solución","Valor que cumple la ecuación."),("Miembro","Cada lado de la igualdad.")),
 ["Reemplazá x = 4 en 2x + 1. ¿Cuánto da?","Reemplazá x = 6 en x/2 + 1. ¿Cuánto da?","Resolvé 3x − 2 = 10. ¿Cuánto vale x?","Un compañero dijo que x = 5 es solución de 3x − 2 = 10. ¿Cuánto da 3x − 2 con x = 5?"],
 ["aplicar","aplicar","aplicar","error"],
 [["9"],["4"],["4"],["13"]],
 {"incompleto":"4.","solo":"3x = 12, entonces x = 4. Con x = 4: 3 · 4 − 2 = 10.","carpeta":["9.","4.","4.","13: no es 10, entonces x = 5 no es solución."]})
L1=[SA("Resolvé 2(x + 3) = 14. ¿Cuánto vale x?",["4"],"2x + 6 = 14.",n="aplicar"),
   MC("3(x − 1) = 12. ¿Cuánto vale x?",["5","3","4","13"],"5","3x − 3 = 12.",n="aplicar"),
   FB("4(x + 1) = 4x + ___",[["4"]],"4 × 1.",n="aplicar")]
L2=[SA("Resolvé x/2 = 6. ¿Cuánto vale x?",["12"],"6 × 2.",n="aplicar"),
   MAT("Uní cada ecuación con su solución.",["x/3 + 1 = 5","x/5 + 2 = 6","x/2 + x/3 = 5","x/4 = 3"],["x = 12","x = 20","x = 6","x = 12 (de x/4)"],"Se multiplica por el mcm.",n="aplicar"),
   ORD("Ordená los pasos para resolver x/3 + 1 = 5.",["x = 12","x/3 = 4","x/3 + 1 = 5"],["x/3 + 1 = 5","x/3 = 4","x = 12"],"Primero se resta 1.",n="aplicar")]
L2[1]=CLF("¿Con qué número se multiplica para quitar los denominadores?",["x/2 = 6","x/3 + 1 = 5","x/2 + x/3 = 5","x/5 + 2 = 6"],["Por 2","Por 3","Por 6","Por 5"],{"x/2 = 6":"Por 2","x/3 + 1 = 5":"Por 3","x/2 + x/3 = 5":"Por 6","x/5 + 2 = 6":"Por 5"},"Se usa el mcm de los denominadores.",n="aplicar")
L3=[SA("Resolvé 3x = x + 4. ¿Cuánto vale x?",["2"],"2x = 4.",n="aplicar"),
   VF("La ecuación 2x + 3 = 2x + 5 tiene solución.","Falso","Queda 3 = 5, que es falso.",n="error"),
   MC("Si al despejar queda 4 = 4, la ecuación es…",["Una identidad","Sin solución","Con una solución"],"Una identidad","La igualdad es siempre verdadera.",n="analizar")]
L4=[SA("Reemplazá x = 4 en 2x + 1. ¿Cuánto da?",["9"],"2 · 4 + 1.",n="aplicar"),
   SA("¿Cuánto da x/2 + 1 con x = 6? Escribí solo el número.",["4"],"3 + 1.",n="aplicar"),
   MS("¿Cuáles valores son solución de 3x − 2 = 10?",["x = 4","x = 5","x = 3","x = 12"],["x = 4"],"3 · 4 − 2 = 10.",n="analizar")]
REL=[MC("Relámpago. 2(x + 1) =",["2x + 2","2x + 1","x + 2"],"2x + 2","Se distribuye.",tiempo=20,n="recordar"),
   N("Relámpago. x/3 = 4. ¿Cuánto vale x?",{"acepta":[12]},"4 × 3.",tiempo=25,n="recordar"),
   VF("Relámpago. Si queda 3 = 5, la ecuación no tiene solución.","Verdadero","Es una igualdad falsa.",tiempo=15,n="recordar"),
   FB("Relámpago. 2x + 1 con x = 4 da ___",[["9"]],"2 · 4 + 1.",tiempo=25,n="recordar")]
ACT={"1":L1,"2":L2,"3":L3,"4":L4,"5":REL}
EX=[[1,SA("Resolvé 4(x + 3) = 24. ¿Cuánto vale x?",["3"],"4x + 12 = 24.",n="aplicar")],
 [1,SA("Un compañero resolvió 2(x + 3) = 14 como 2x + 3 = 14. ¿Cuánto vale x en realidad?",["4"],"El 2 multiplica también al 3.",n="error")],
 [1,MC("5(x − 1) = 15. ¿Cuánto vale x?",["4","2","3","16"],"4","5x − 5 = 15.",n="aplicar")],
 [2,SA("Resolvé x/5 + 2 = 6. ¿Cuánto vale x?",["20"],"x/5 = 4.",n="aplicar")],
 [2,FB("En x/2 + x/3 = 5, se multiplica por ___",[["6"]],"El mcm de 2 y 3 es 6.",n="aplicar")],
 [2,N("Resolvé x/2 + x/4 = 6. ¿Cuánto vale x?",{"acepta":[8]},"2x + x = 24.",n="error")],
 [3,SA("Resolvé 4x + 2 = 2x + 10. ¿Cuánto vale x?",["4"],"2x = 8.",n="aplicar")],
 [3,CLF("¿Una solución, sin solución o identidad?",["x + 1 = x + 2","2x + 4 = 2(x + 2)","3x = x + 4"],["Sin solución","Identidad","Una solución"],{"x + 1 = x + 2":"Sin solución","2x + 4 = 2(x + 2)":"Identidad","3x = x + 4":"Una solución"},"Se mira cómo queda al despejar.",n="analizar")],
 [3,MC("Resolvé 5x − 3 = 3x + 7. ¿Cuánto vale x?",["5","2","10","4"],"5","2x = 10.",n="aplicar")],
 [4,SA("Reemplazá x = 6 en x/2 + 1. ¿Cuánto da?",["4"],"3 + 1.",n="aplicar")],
 [4,ORD("Ordená los pasos para verificar x = 4 en 2x + 1 = 9.",["9 = 9","2 · 4 + 1","8 + 1"],["2 · 4 + 1","8 + 1","9 = 9"],"Se reemplaza, se calcula y se compara.",n="aplicar")],
 [4,MS("¿En cuáles ecuaciones x = 5 es solución?",["2x − 3 = 7","3x − 2 = 10","x + 1 = 6","x/5 = 2"],["2x − 3 = 7","x + 1 = 6"],"Se reemplaza el 5 en cada una.",n="analizar")],
 [4,N("Un compañero dijo que x = 5 es solución de 3x − 2 = 10. ¿Cuánto da 3x − 2 con x = 5?",{"acepta":[13]},"15 − 2 = 13, no 10.",n="error")]]
M={"subject_id":SID,"tema":8,"practica":"Práctica general: ecuaciones de primer grado","examen_titulo":"Nivel jefe: ecuaciones de primer grado","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT,"examen":EX}
STEPS={1:"591085ab-931d-47fc-b62e-5b43c7ac829f",2:"6c7c84f2-d195-44c5-b5e9-fc89bd9b2eca",3:"c464b151-37aa-4c64-a700-0ffdd4ff86db",4:"aee503c9-e5b6-4ffe-abd1-b049d1a4acb0"}
TIT={1:"Ecuaciones con paréntesis",2:"Ecuaciones con denominadores",3:"Ecuaciones sin solución e identidades",4:"Verificar y escribir la solución"}
CLS={1:[
 DEF("Ecuación con paréntesis","Igualdad con una incógnita en la que primero se distribuye el número de afuera.","🧮",["Una *ecuación con paréntesis* se resuelve distribuyendo primero.","Dos por equis más tres es *dos equis más seis*."]),
 PIZ([("2(x + 3) = 14","sol","subraya"),("2x + 6 = 14","verde","circulo"),("2x = 8 y x = 4","coral",None)],["Una ecuación con paréntesis.","Se distribuye: *dos equis más seis* igual catorce.","Se resta seis y se divide por dos: *equis es cuatro*."]),
 FL("PASOS CON PARÉNTESIS",[("Distribuir","📤"),("Agrupar","🧩"),("Despejar","🔄"),("Verificar","✅")],["Primero, *distribuir*.","Después, *agrupar* los términos.","Luego, *despejar* la incógnita.","Y al final, *verificar* el resultado."]),
 Q("En 3(x − 1) = 12, x vale…",["5","3","4"],0,["Te toca: tres por equis menos uno igual doce.","¿Cinco, tres o cuatro?","*Cinco*: tres equis menos tres es doce."]),
 RES(["Repasemos.","Primero se *distribuye* el número de afuera.","Después se *despeja* la incógnita.","Siempre conviene *comprobar*.","¡Clase terminada! Ahora, *a practicar*."],[["DISTRIBUIR","antes de despejar"],["DESPEJAR","operación inversa"],["COMPROBAR","reemplazar"]])],
2:[
 DIL("¿Conviene multiplicar por el mcm?","🔢",("Sí","Se eliminan todos los denominadores","✅"),("No","Quedan fracciones y es más difícil","❌"),["Un dilema de ecuaciones.","Si se multiplica por el *mínimo común múltiplo*, desaparecen los denominadores.","Si no, *quedan fracciones* y es más difícil."]),
 UNI("ECUACIÓN Y SOLUCIÓN",[("x/2 = 6","x = 12"),("x/5 + 2 = 6","x = 20"),("x/2 + x/4 = 6","x = 8")],["Tres ecuaciones para unir.","Equis sobre dos igual seis: *equis es doce*.","Equis sobre cinco más dos igual seis: *equis es veinte*.","Y equis sobre dos más equis sobre cuatro igual seis: *equis es ocho*."]),
 AD(("ANTES","🔢","x/2 = 6"),("DESPUÉS","✅","x = 12"),["Equis sobre dos igual seis...","...al multiplicar por dos, *equis es doce*."]),
 Q("El mcm de 2 y 3 es…",["6","5","1"],0,["Te toca: el mínimo común múltiplo de dos y tres.","¿Seis, cinco o uno?","*Seis*."]),
 RES(["Repasemos.","Se multiplica por el *mcm* de los denominadores.","Se multiplican *todos los términos*.","Después se despeja y se *comprueba*.","¡Clase terminada! Ahora, *a practicar*."],[["MCM","menor múltiplo común"],["MULTIPLICAR","todos los términos"],["COMPROBAR","reemplazar"]])],
3:[
 {"t":"mazo","titulo":"TRES TIPOS DE ECUACIÓN","items":[{"frente":"x + 1 = x + 2","dorso":"Sin solución","emoji":"🚫"},{"frente":"2(x + 2) = 2x + 4","dorso":"Identidad","emoji":"♾️"},{"frente":"3x = x + 4","dorso":"x = 2","emoji":"1️⃣"}],"voz":["Tres cartas, tres tipos de ecuación.","Equis más uno igual equis más dos *no tiene solución*.","Dos por equis más dos es *identidad*, y tres equis igual equis más cuatro *tiene una solución*."]},
 BAL(("2x + 3",["2x","3"]),("2x + 5",["2x","5"]),"der",["¿Qué pesa más?","Dos equis más tres, contra dos equis más cinco.","Pesa más la *derecha*: tres no es igual a cinco, *no hay solución*."]),
 CMP(("SIN SOLUCIÓN","3 = 5","🚫"),("IDENTIDAD","4 = 4","♾️"),"vs",["Dos casos.","Si queda una igualdad *falsa*, no hay solución.","Si queda *siempre verdadera*, es una identidad."]),
 Q("Si queda 4 = 4, la ecuación es…",["Una identidad","Sin solución","De una solución"],0,["Te toca: queda cuatro igual cuatro.","¿Una identidad, sin solución o de una solución?","*Una identidad*: siempre es verdadera."]),
 RES(["Repasemos.","Si queda una igualdad *falsa*, no hay solución.","Si queda *siempre verdadera*, es una identidad.","Si queda *equis igual a un número*, hay una solución.","¡Clase terminada! Ahora, *a practicar*."],[["FALSA","sin solución"],["VERDADERA","identidad"],["UN VALOR","una solución"]])],
4:[
 EQ(["2x + 1 = 9","x = 4","2 · 4 + 1 = 9"],["la ecuación","la solución","se reemplaza"],["Tenemos *dos equis más uno igual nueve*.","Una posible solución es *equis igual cuatro*.","Se reemplaza: *dos por cuatro más uno* da nueve, y coincide."]),
 TB("VERIFICAR",["Ecuación","Valor","Resultado"],[["2x + 1 = 9","x = 4","9 = 9 ✓"],["3x − 2 = 10","x = 5","13 ≠ 10"],["x/2 + 1 = 4","x = 6","4 = 4 ✓"]],["Se reemplaza el valor y se compara.","Con *equis cuatro*, nueve es igual a nueve: *sí es solución*.","Con *equis cinco*, trece no es diez: *no es solución*.","Y con *equis seis*, cuatro es igual a cuatro: *sí es solución*."]),
 CMP(("VERIFICA","9 = 9","✅"),("NO VERIFICA","13 ≠ 10","❌"),"vs",["Dos casos.","Si los dos miembros *coinciden*, el valor verifica.","Si no coinciden, *no es solución*."]),
 Q("¿x = 5 es solución de 3x − 2 = 10?",["No","Sí"],0,["Te toca: tres equis menos dos igual diez, con equis igual cinco.","¿Es solución o no?","*No*: da trece, no diez."]),
 RES(["Repasemos.","Para verificar, se *reemplaza* en la ecuación original.","Si los dos miembros *coinciden*, es solución.","Si no, hay que *revisar* el despeje.","¡Clase terminada! Ahora, *a practicar*."],[["VERIFICAR","reemplazar"],["COINCIDEN","es solución"],["NO COINCIDEN","revisar"]])]}
escribir(8, M, STEPS, TIT, CLS)
