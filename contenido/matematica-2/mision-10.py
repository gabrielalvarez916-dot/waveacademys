# -*- coding: utf-8 -*-
"""Matemática II · Misión 10 · Funciones: concepto, tablas y gráficos. Genera mision-10.json y 4 clases."""
from mat import *
B1=NV("Vas a reconocer cuándo una relación es una función, a identificar la variable independiente y la dependiente, y a calcular valores.",
 ["Qué es una función","Variable independiente y dependiente","Calcular valores","Cuándo no es función"],[
 S(1,"Función",[D("Función","Una función es una relación en la que <b>a cada valor de x le corresponde un único valor de y</b>. La x es la variable independiente y la y, la dependiente."),
  IM("Idea clave","En y = 2x + 1, si x = 3 entonces y = 7.")]),
 S(1,"¿Es función?",[T("Relaciones",["Relación","¿Es función?"],[["Cada alumno y su edad","Sí"],["Cada edad y sus alumnos","No"],["x y 2x + 1","Sí"]])]),
 S(2,"Calcular y",[E("Calcular y = 2x + 1 para x = 3","Se reemplaza x por 3.",["y = 2 · 3 + 1.","y = 6 + 1.","y = 7."])]),
 S(2,"No es función",[E("A x = 2 le corresponden y = 4 e y = 5","Se mira cuántos valores de y tiene cada x.",["Al valor x = 2 le corresponden dos valores de y.","Una función da un solo valor para cada x.","No es una función."])])],
 {"titulo":"Calcular","planteo":"Calculá y para x = 3 en y = 2x + 1.","pasos":["Se reemplaza: y = 2 · 3 + 1.","y = 6 + 1.","y = 7."]},
 {"titulo":"Completá","planteo":"Calculá y para x = 4 en y = 3x − 2.","pasos":["Se reemplaza: y = 3 · 4 − 2.","y = 12 − 2 = ___ .","y = 10."]},
 {"titulo":"tu turno","planteo":"Calculá y para x = 5 en y = x². Después decidí si una relación con dos valores de y para x = 2 es función."},
 {"titulo":"Un solo valor","texto":"En una función, cada x tiene un solo y. Si a una x le tocan dos valores de y, no es función."},
 ["Pensar que dos valores de y para una misma x es una función.","Cambiar x por y al reemplazar."],
 RS(("Función","A cada x le corresponde un único y."),("Variable independiente","La x, la que elijo."),("Variable dependiente","La y, la que se calcula."),("No es función","Una x con dos valores de y.")),
 G(("Función","Relación con un único y para cada x."),("Variable independiente","Se elige libremente."),("Variable dependiente","Depende de la x."),("Fórmula","Regla que calcula y a partir de x.")),
 ["Si y = 2x + 1, ¿cuánto vale y para x = 3?","Si y = 3x − 2, ¿cuánto vale y para x = 4?","Si y = x², ¿cuánto vale y para x = 5?","Un compañero dijo que una relación donde x = 2 corresponde a y = 4 e y = 5 es una función. ¿Cuántos valores de y puede tener cada x en una función?"],
 ["aplicar","aplicar","aplicar","error"],
 [["7"],["10"],["25"],["1"]],
 {"incompleto":"10.","solo":"y = 5² = 25. Con dos valores de y para x = 2 no es función.","carpeta":["7.","10.","25.","1: cada x tiene un único y."]})
B2=NV("Vas a completar tablas de valores de una función, a calcular y a partir de x y a hallar x a partir de y.",
 ["Tablas de valores","Completar una tabla","Hallar x conociendo y","Detectar errores en tablas"],[
 S(1,"Tabla de valores",[D("Tabla de valores","Una tabla de valores muestra <b>pares (x, y)</b> de una función. Se arma reemplazando distintos valores de x en la fórmula."),
  IM("Idea clave","Para y = 2x + 1: x = 0, 1, 2, 3 da y = 1, 3, 5, 7.")]),
 S(1,"Ejemplo",[T("y = 2x + 1",["x","Cuenta","y"],[["0","2 · 0 + 1","1"],["1","2 · 1 + 1","3"],["2","2 · 2 + 1","5"],["3","2 · 3 + 1","7"]])]),
 S(2,"Completar",[E("Completar con x = 2 en y = 3x − 1","Se reemplaza x.",["y = 3 · 2 − 1.","y = 6 − 1.","y = 5."])]),
 S(2,"Hallar x",[E("¿Qué x da y = 9 en y = 2x + 1?","Se plantea una ecuación.",["2x + 1 = 9.","2x = 8.","x = 4."])])],
 {"titulo":"Completar","planteo":"Completá la tabla de y = 3x − 1 para x = 2.","pasos":["Se reemplaza: 3 · 2 − 1.","6 − 1 = 5.","y = 5."]},
 {"titulo":"Completá","planteo":"¿Qué valor de x da y = 9 en y = 2x + 1?","pasos":["Se plantea: 2x + 1 = 9.","2x = 8, entonces x = ___ .","x = 4."]},
 {"titulo":"tu turno","planteo":"Armá la tabla de y = 2x + 1 con x = 0, 1, 2, 3 y buscá qué x da y = 7."},
 {"titulo":"Cada fila, un par","texto":"Cada fila de la tabla es un par (x, y). Si cambiás el valor de x, tenés que volver a calcular y."},
 ["Copiar el mismo valor de y en todas las filas.","Calcular y y no verificar con la fórmula."],
 RS(("Tabla","Lista de pares (x, y)."),("Completar","Reemplazar x en la fórmula."),("Hallar x","Plantear la ecuación con y."),("Controlar","Verificar con la fórmula.")),
 G(("Tabla de valores","Pares (x, y) de una función."),("Par ordenado","(x, y)."),("Reemplazar","Poner un número en lugar de la letra."),("Fórmula","Regla de la función.")),
 ["En y = 2x + 1, ¿cuánto vale y cuando x = 0?","En y = 3x − 1, ¿cuánto vale y cuando x = 2?","En y = 2x + 1, ¿qué valor de x da y = 9?","Un compañero completó la tabla de y = 2x + 1 con x = 2 y escribió 4. ¿Cuál es el valor correcto de y?"],
 ["aplicar","aplicar","aplicar","error"],
 [["1"],["5"],["4"],["5"]],
 {"incompleto":"4.","solo":"Con y = 2x + 1: x = 0, 1, 2, 3 da y = 1, 3, 5, 7. Para y = 7, x = 3.","carpeta":["1.","5.","4.","5: 2 · 2 + 1 = 5."]})
B3=NV("Vas a ubicar puntos en el plano cartesiano, a leer pares ordenados y a graficar puntos de una función.",
 ["Los ejes","Pares ordenados","Ubicar puntos","Graficar una función"],[
 S(1,"Plano cartesiano",[D("Plano cartesiano","El plano cartesiano tiene dos ejes: el <b>horizontal (x)</b> y el <b>vertical (y)</b>. Cada punto es un <b>par ordenado (x, y)</b>."),
  IM("Idea clave","El punto (3, 2) está 3 unidades a la derecha y 2 hacia arriba del origen.")]),
 S(1,"Ejemplos",[T("Dónde está cada punto",["Punto","Ubicación"],[["(3, 2)","3 a la derecha, 2 arriba"],["(−1, 4)","1 a la izquierda, 4 arriba"],["(0, −3)","3 abajo, sobre el eje y"]])]),
 S(2,"Ubicar un punto",[E("Ubicar el punto (3, 2)","Se parte del origen.",["Se avanza 3 sobre el eje x.","Se sube 2 sobre el eje y.","Se marca el punto."])]),
 S(2,"Graficar",[E("Graficar y = x + 1 con x = 2","Se calcula y y se marca el par.",["y = 2 + 1 = 3.","El par ordenado es (2, 3).","Se marca el punto (2, 3)."])])],
 {"titulo":"Ubicar","planteo":"Ubicá el punto (3, 2) en el plano.","pasos":["Se avanza 3 sobre el eje x.","Se sube 2 sobre el eje y.","El punto está en (3, 2)."]},
 {"titulo":"Completá","planteo":"Graficar un punto de y = x + 1 con x = 2.","pasos":["y = 2 + 1 = ___ .","El par ordenado es (2, 3).","Se marca el punto (2, 3)."]},
 {"titulo":"tu turno","planteo":"Calcular los pares de y = x + 1 para x = 0, 1, 2 y ubicarlos en el plano."},
 {"titulo":"Primero x, después y","texto":"En un par ordenado, el primer número es x, el horizontal; el segundo es y, el vertical. El orden importa."},
 ["Intercambiar x con y al ubicar el punto.","Contar desde cualquier lugar y no desde el origen."],
 RS(("Ejes","Horizontal x y vertical y."),("Par ordenado","(x, y), el orden importa."),("Origen","El punto (0, 0)."),("Graficar","Calcular pares y marcarlos.")),
 G(("Plano cartesiano","Plano con dos ejes."),("Eje x","Eje horizontal."),("Eje y","Eje vertical."),("Origen","Punto donde se cruzan los ejes.")),
 ["El punto (3, 2) está a 3 unidades a la derecha del origen. ¿Cuántas unidades sube?","Para y = x + 1, ¿cuánto vale y si x = 2?","El punto (−1, 4). ¿Cuántas unidades sube desde el origen?","Un compañero ubicó (3, 2) avanzando 2 en x y 3 en y. ¿Cuántas unidades se avanza en x?"],
 ["aplicar","aplicar","aplicar","error"],
 [["2"],["3"],["4"],["3"]],
 {"incompleto":"3.","solo":"Para x = 0, 1, 2 en y = x + 1 se obtiene (0, 1), (1, 2) y (2, 3).","carpeta":["2.","3.","4.","3: la primera coordenada es x."]})
B4=NV("Vas a leer gráficos y tablas: reconocer si una función crece, decrece o se mantiene constante, y hallar el valor de y cuando x = 0.",
 ["Crecer, decrecer o mantenerse","Cuánto cambia y","Valor inicial","Interpretar con un contexto"],[
 S(1,"Interpretar un gráfico",[D("Interpretar un gráfico","Una función es <b>creciente</b> si y aumenta cuando x aumenta, <b>decreciente</b> si y disminuye y <b>constante</b> si y no cambia."),
  IM("Idea clave","La ordenada al origen es el valor de y cuando x = 0.")]),
 S(1,"Ejemplos",[T("Comportamiento",["Valores de y","Función"],[["2, 4, 6","Creciente"],["9, 6, 3","Decreciente"],["5, 5, 5","Constante"]])]),
 S(2,"Creciente",[E("Puntos (0, 2), (1, 4) y (2, 6)","Se mira cómo cambia y.",["y aumenta de 2 a 4 y a 6.","Cuando x crece, y crece.","La función es creciente."])]),
 S(2,"Ordenada al origen",[E("Función que pasa por (0, 3) y (2, 7)","Se busca el y cuando x = 0.",["La ordenada al origen es el y cuando x = 0.","En el punto (0, 3), y vale 3.","La ordenada al origen es 3."])])],
 {"titulo":"Crece o decrece","planteo":"Los puntos son (0, 2), (1, 4) y (2, 6). ¿La función crece o decrece?","pasos":["y pasa de 2 a 4 y a 6.","Cuando x aumenta, y aumenta.","La función es creciente."]},
 {"titulo":"Completá","planteo":"La función pasa por (0, 3) y (2, 7). ¿Cuál es su ordenada al origen?","pasos":["Es el valor de y cuando x = ___ .","En (0, 3), y vale 3.","La ordenada al origen es 3."]},
 {"titulo":"tu turno","planteo":"Una función pasa por (0, 9), (1, 6) y (2, 3). Decidí si crece o decrece y cuánto cambia y por cada unidad de x."},
 {"titulo":"Mirar los valores","texto":"Para saber si una función crece o decrece, comparás los valores de y en orden. No alcanza con mirar uno solo."},
 ["Decir que crece cuando y baja.","Confundir el valor de y con el de x al leer un punto."],
 RS(("Creciente","y aumenta cuando x aumenta."),("Decreciente","y disminuye cuando x aumenta."),("Constante","y no cambia."),("Ordenada al origen","El y cuando x = 0.")),
 G(("Creciente","Sube de izquierda a derecha."),("Decreciente","Baja de izquierda a derecha."),("Constante","Se mantiene igual."),("Ordenada al origen","Valor de y en x = 0.")),
 ["La función pasa por (0, 2), (1, 4) y (2, 6). ¿Cuánto aumenta y por cada unidad que aumenta x?","Una función pasa por (0, 3) y (2, 7). ¿Cuánto vale y cuando x = 0?","Una función pasa por (0, 5), (1, 5) y (2, 5). ¿Cuánto vale y cuando x = 4?","Un compañero dijo que y = 9, 6, 3 es una función creciente. ¿Cuánto disminuye y cada vez que x aumenta 1?"],
 ["aplicar","aplicar","analizar","error"],
 [["2"],["3"],["5"],["3"]],
 {"incompleto":"3.","solo":"La función pasa por (0, 9), (1, 6) y (2, 3): es decreciente y y disminuye 3 por cada unidad de x.","carpeta":["2.","3.","5: es constante.","3: es decreciente, no creciente."]})
L1=[SA("Si y = 2x + 1, ¿cuánto vale y para x = 3?",["7"],"2 · 3 + 1.",n="aplicar"),
   MC("¿Cuál de estas relaciones es una función?",["Cada alumno y su edad","Cada edad y todos sus alumnos","Cada país y sus ciudades"],"Cada alumno y su edad","Cada alumno tiene una sola edad.",n="analizar"),
   FB("En y = 2x + 1, la variable independiente es la ___",[["x"]],"La x se elige libremente.",n="recordar")]
L2=[ORD("Ordená los pasos para completar y = 3x − 1 con x = 2.",["y = 5","y = 3 · 2 − 1","y = 6 − 1"],["y = 3 · 2 − 1","y = 6 − 1","y = 5"],"Primero se reemplaza.",n="aplicar"),
   N("En y = 2x + 1, ¿qué valor de x da y = 9?",{"acepta":[4]},"2x + 1 = 9.",n="aplicar"),
   VF("En una tabla de y = 2x + 1, todas las filas tienen el mismo valor de y.","Falso","Al cambiar x, cambia y.",n="error")]
L3=[MAT("Uní cada punto con su ubicación.",["(3, 2)","(0, 4)","(2, 0)","(1, 1)"],["3 a la derecha y 2 arriba","sobre el eje y, 4 arriba","sobre el eje x, 2 a la derecha","1 a la derecha y 1 arriba"],"El primero es x y el segundo es y.",n="aplicar"),
   CLF("¿Sobre qué eje está cada punto?",["(0, 5)","(4, 0)","(0, −2)","(−3, 0)"],["Eje x","Eje y"],{"(0, 5)":"Eje y","(4, 0)":"Eje x","(0, −2)":"Eje y","(−3, 0)":"Eje x"},"Si x vale 0, está sobre el eje y; si y vale 0, sobre el eje x.",n="analizar"),
   FB("Para y = x + 1, el par ordenado con x = 2 es (2, ___ )",[["3"]],"y = 2 + 1.",n="aplicar")]
L4=[MC("Si y pasa de 9 a 6 a 3, la función es…",["Decreciente","Creciente","Constante"],"Decreciente","y disminuye.",n="aplicar"),
   N("La función pasa por (0, 3) y (2, 7). ¿Cuánto vale y cuando x = 0?",{"acepta":[3]},"Es la ordenada al origen.",n="aplicar"),
   MS("¿Cuáles son funciones crecientes?",["y: 1, 3, 5","y: 9, 6, 3","y: 2, 4, 8","y: 5, 5, 5"],["y: 1, 3, 5","y: 2, 4, 8"],"y aumenta al aumentar x.",n="analizar")]
REL=[MC("Relámpago. En una función, cada x tiene…",["Un solo y","Dos y","Ningún y"],"Un solo y","Esa es la definición.",tiempo=20,n="recordar"),
   N("Relámpago. y = x + 1 con x = 4 da…",{"acepta":[5]},"4 + 1.",tiempo=25,n="recordar"),
   VF("Relámpago. El par (3, 2) tiene x = 3 e y = 2.","Verdadero","El primero es x.",tiempo=15,n="recordar"),
   FB("Relámpago. Si y no cambia, la función es ___",[["constante"]],"Se mantiene igual.",tiempo=25,n="recordar")]
ACT={"1":L1,"2":L2,"3":L3,"4":L4,"5":REL}
EX=[[1,MC("Si y = 3x − 2, ¿cuánto vale y para x = 4?",["10","14","7","12"],"10","3 · 4 − 2.",n="aplicar")],
 [1,SA("Si y = x², ¿cuánto vale y para x = 5?",["25"],"5².",n="aplicar")],
 [1,SA("Un compañero dijo que x = 2 con y = 4 e y = 5 es una función. ¿Cuántos valores de y puede tener cada x en una función?",["1","uno"],"Un único valor.",n="error")],
 [2,MC("En y = 3x − 1, ¿cuánto vale y cuando x = 2?",["5","6","7","4"],"5","3 · 2 − 1.",n="aplicar")],
 [2,SA("En y = 2x + 1, ¿cuánto vale y cuando x = 0?",["1"],"2 · 0 + 1.",n="aplicar")],
 [2,SA("Un compañero completó y = 2x + 1 con x = 2 y escribió 4. ¿Cuál es el valor correcto de y?",["5"],"2 · 2 + 1.",n="error")],
 [3,MAT("Uní cada par ordenado con su ubicación.",["(3, 2)","(0, 4)","(2, 0)","(1, 1)"],["3 a la derecha y 2 arriba","sobre el eje y, 4 arriba","sobre el eje x, 2 a la derecha","1 a la derecha y 1 arriba"],"El primero es x y el segundo es y.",n="aplicar")],
 [3,N("Para y = x + 1, ¿cuánto vale y si x = 2?",{"acepta":[3]},"2 + 1.",n="aplicar")],
 [3,SA("Un compañero ubicó (3, 2) avanzando 2 en x y 3 en y. ¿Cuántas unidades se avanza en x?",["3"],"El primer número es x.",n="error")],
 [4,SA("La función pasa por (0, 2), (1, 4) y (2, 6). ¿Cuánto aumenta y por cada unidad de x?",["2"],"y sube 2 cada vez.",n="aplicar")],
 [4,MC("Una función pasa por (0, 5), (1, 5) y (2, 5). Es…",["Constante","Creciente","Decreciente"],"Constante","y no cambia.",n="analizar")],
 [4,MS("¿Cuáles son funciones decrecientes?",["y: 9, 6, 3","y: 1, 3, 5","y: 10, 7, 4","y: 4, 4, 4"],["y: 9, 6, 3","y: 10, 7, 4"],"y disminuye al aumentar x.",n="analizar")],
 [4,SA("Un compañero dijo que y = 9, 6, 3 es creciente. ¿Cuánto disminuye y cada vez que x aumenta 1?",["3"],"9 − 6 = 3.",n="error")]]
M={"subject_id":SID,"tema":10,"practica":"Práctica general: funciones","examen_titulo":"Nivel jefe: funciones","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT,"examen":EX}
STEPS={1:"729eec67-9d01-4042-be28-2d9f0b8fcbb4",2:"e87c00d1-4c98-4395-a6a9-7320320f3102",3:"52101a30-8697-49d7-aa1e-b1271f3b0a3b",4:"5ad6ec58-3c90-4e44-9015-9c5dab03cecc"}
TIT={1:"Qué es una función",2:"Tablas de valores",3:"Gráficos cartesianos",4:"Leer e interpretar gráficos"}
CLS={1:[
 DEF("Función","Relación en la que a cada valor de equis le corresponde un único valor de ye.","📈",["Una *función* es una relación entre dos variables.","A cada valor de equis le corresponde *un único valor de ye*."]),
 CMP(("FUNCIÓN","a cada x un solo y","✅"),("NO ES FUNCIÓN","a una x dos y","❌"),"vs",["Dos casos.","En una *función*, cada equis tiene un solo ye.","Si a una equis le tocan *dos valores de ye*, no es función."]),
 AD(("x = 3","🔢","y = 7"),("y = 2x + 1","📈","7"),["Si equis vale tres...","...en dos equis más uno, *ye vale siete*."]),
 Q("En y = 3x − 2, con x = 4, y vale…",["10","14","12"],0,["Te toca: tres por cuatro menos dos.","¿Diez, catorce o doce?","*Diez*."]),
 RES(["Repasemos.","En una *función*, cada equis tiene un solo ye.","Equis es la variable *independiente*; ye, la *dependiente*.","Se calcula *reemplazando* en la fórmula.","¡Clase terminada! Ahora, *a practicar*."],[["FUNCIÓN","un solo y por x"],["INDEPENDIENTE","la x"],["DEPENDIENTE","la y"]])],
2:[
 TB("TABLA DE y = 2x + 1",["x","Cuenta","y"],[["0","2 · 0 + 1","1"],["1","2 · 1 + 1","3"],["2","2 · 2 + 1","5"],["3","2 · 3 + 1","7"]],["Una tabla de valores.","Con equis cero, *ye vale uno*.","Con equis uno, *ye vale tres*.","Con equis dos, *ye vale cinco*.","Y con equis tres, *ye vale siete*."]),
 PIZ([("y = 3x − 1","sol","subraya"),("x = 2: 3 · 2 − 1","verde","circulo"),("y = 5","coral",None)],["Una función y un valor de equis.","Se reemplaza equis por dos: *tres por dos menos uno*.","Y *ye vale cinco*."]),
 UNI("x Y SU y",[("y = 2x + 1, x = 0","y = 1"),("y = 2x + 1, x = 2","y = 5"),("y = 3x − 1, x = 2","y = 5"),("y = 2x + 1, x = 3","y = 7")],["Cuatro cálculos para unir.","Con equis cero, *ye es uno*.","Con equis dos, *ye es cinco*.","Con la otra fórmula y equis dos, también *cinco*.","Y con equis tres, *ye es siete*."]),
 Q("En y = 2x + 1, ¿qué x da y = 9?",["4","5","8"],0,["Te toca: dos equis más uno igual nueve.","¿Cuatro, cinco u ocho?","*Cuatro*: dos equis es ocho."]),
 RES(["Repasemos.","Una *tabla* es una lista de pares.","Se completa *reemplazando* equis.","Para hallar equis, se *plantea una ecuación*.","¡Clase terminada! Ahora, *a practicar*."],[["TABLA","pares (x, y)"],["COMPLETAR","reemplazar x"],["HALLAR X","ecuación con y"]])],
3:[
 {"t":"mazo","titulo":"PUNTOS EN EL PLANO","items":[{"frente":"(3, 2)","dorso":"3 a la derecha, 2 arriba","emoji":"📍"},{"frente":"(−1, 4)","dorso":"1 a la izquierda, 4 arriba","emoji":"⬆️"},{"frente":"(0, −3)","dorso":"3 abajo sobre el eje y","emoji":"⬇️"}],"voz":["Tres puntos en el plano.","El tres, dos está *tres a la derecha y dos arriba*.","Menos uno, cuatro está a la *izquierda*, y cero, menos tres está *abajo*."]}, 
 FL("PASOS PARA UBICAR UN PUNTO",[("Ir al origen","📍"),("Avanzar en x","➡️"),("Subir o bajar en y","⬆️"),("Marcar el punto","✏️")],["Primero, partir del *origen*.","Después, avanzar en *equis*.","Luego, subir o bajar en *ye*.","Y *marcar* el punto."]),
 DA("(3, 2)","par ordenado","x = 3 e y = 2","La primera coordenada es x y la segunda es y","📍",["Un dato clave.","En un par ordenado, primero va *equis* y después *ye*."]),
 Q("El punto (4, 1) está…",["4 a la derecha y 1 arriba","1 a la derecha y 4 arriba","4 arriba y 1 abajo"],0,["Te toca: el punto cuatro, uno.","¿Cuatro a la derecha y uno arriba, uno a la derecha y cuatro arriba, o cuatro arriba y uno abajo?","*Cuatro a la derecha y uno arriba*."]),
 RES(["Repasemos.","El plano tiene un eje *horizontal* y uno *vertical*.","Un punto es un *par ordenado*.","Primero va *equis* y después *ye*.","¡Clase terminada! Ahora, *a practicar*."],[["EJES","horizontal y vertical"],["PAR ORDENADO","(x, y)"],["ORIGEN","(0, 0)"]])],
4:[
 ZO([("🔭","y: 2, 4, 6 → creciente"),("🔬","y: 9, 6, 3 → decreciente"),("🧬","y: 5, 5, 5 → constante")],["Tres comportamientos.","Si ye sube, es *creciente*.","Si baja, es *decreciente*, y si no cambia, *constante*."]),
 ER([("Decir que 9, 6, 3 crece","Decir que decrece"),("Confundir x con y al leer un punto","Leer primero x")],["Errores típicos.","Decir que *crece* cuando ye baja.","Y *confundir equis con ye* al leer un punto."]),
 CMP(("CRECE","y sube","⬆️"),("DECRECE","y baja","⬇️"),"vs",["Dos comportamientos.","Si *ye sube* cuando equis aumenta, la función crece.","Si *ye baja*, la función decrece."]),
 Q("Si y: 9, 6, 3, la función es…",["Decreciente","Creciente","Constante"],0,["Te toca: ye vale nueve, seis, tres.","¿Decreciente, creciente o constante?","*Decreciente*."]),
 RES(["Repasemos.","*Creciente*: ye aumenta.","*Decreciente*: ye disminuye.","*Constante*: ye no cambia.","¡Clase terminada! Ahora, *a practicar*."],[["CRECIENTE","y sube"],["DECRECIENTE","y baja"],["CONSTANTE","y no cambia"]])]}
escribir(10, M, STEPS, TIT, CLS)
