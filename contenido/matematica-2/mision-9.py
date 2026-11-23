# -*- coding: utf-8 -*-
"""Matemática II · Misión 9 · Problemas con ecuaciones y despeje de fórmulas. Genera mision-9.json y 4 clases."""
from mat import *
B1=NV("Vas a traducir enunciados al lenguaje algebraico, plantear la ecuación y resolverla.",
 ["Traducir una frase","Plantear la ecuación","Resolver","Responder el problema"],[
 S(1,"Del enunciado a la ecuación",[D("Plantear un problema","Para resolver un problema con ecuaciones se <b>elige la incógnita</b>, se traduce el enunciado a una ecuación, se resuelve y se responde con palabras."),
  IM("Idea clave","El doble de un número es 18 se escribe 2x = 18.")]),
 S(1,"Traducir",[T("Enunciado y ecuación",["Enunciado","Ecuación"],[["El doble de un número es 18","2x = 18"],["Un número más 7 es 19","x + 7 = 19"],["El triple de un número menos 4 es 14","3x − 4 = 14"]])]),
 S(2,"Un número y su doble",[E("Un número y su doble suman 21","Si el número es x, su doble es 2x.",["x + 2x = 21.","3x = 21.","x = 7."])]),
 S(2,"Triple menos cuatro",[E("El triple de un número menos 4 es 14","Se traduce y se despeja.",["3x − 4 = 14.","3x = 18.","x = 6."])])],
 {"titulo":"Plantear","planteo":"Un número y su doble suman 21. ¿Cuál es el número?","pasos":["Si el número es x, su doble es 2x.","x + 2x = 21, entonces 3x = 21.","x = 7."]},
 {"titulo":"Completá","planteo":"El triple de un número menos 4 es 14.","pasos":["Se plantea: 3x − 4 = 14.","3x = 18, entonces x = ___ .","El número es 6."]},
 {"titulo":"tu turno","planteo":"La suma de un número y 9 es 25. Plantear la ecuación y resolverla."},
 {"titulo":"Elegir la incógnita","texto":"Antes de escribir la ecuación, decí qué representa la x. Al final, respondé con palabras, no solo con el número."},
 ["Traducir 'el doble más 5' como 2(x + 5).","Dejar el resultado sin responder la pregunta."],
 RS(("Incógnita","Lo que se busca, representado con una letra."),("Plantear","Traducir el enunciado a una ecuación."),("Resolver","Despejar la incógnita."),("Responder","Contestar con palabras y unidades.")),
 G(("Enunciado","Texto del problema."),("Incógnita","Valor desconocido."),("Plantear","Escribir la ecuación."),("Doble","Dos veces un número.")),
 ["Un número y su doble suman 21. ¿Cuál es el número?","El triple de un número menos 4 es 14. ¿Cuál es el número?","La suma de un número y 9 es 25. ¿Cuál es el número?","Un compañero escribió el doble de un número más 5 es 17 como 2(x + 5) = 17. Con la ecuación correcta 2x + 5 = 17, ¿cuál es el número?"],
 ["aplicar","aplicar","aplicar","error"],
 [["7"],["6"],["16"],["6"]],
 {"incompleto":"6.","solo":"x + 9 = 25, entonces x = 16.","carpeta":["7.","6.","16.","6: el doble más 5 es 2x + 5."]})
B2=NV("Vas a resolver problemas de edades, de dinero y de repartos planteando una ecuación con una sola incógnita.",
 ["Problemas de edades","Problemas de dinero","Repartos desiguales","Verificar la respuesta"],[
 S(1,"Tres tipos de problema",[D("Edades, dinero y repartos","En estos problemas se elige como incógnita <b>la cantidad más chica</b> o la que sirve de referencia, y las otras se expresan a partir de ella."),
  IM("Idea clave","Si Ana tiene el doble de edad que Beto, y Beto tiene x años, Ana tiene 2x.")]),
 S(1,"Ejemplos",[T("Tres situaciones",["Situación","Ecuación","Solución"],[["Ana tiene el doble que Beto; suman 36","x + 2x = 36","Beto 12"],["3 cuadernos y una lapicera de 50; total 230","3x + 50 = 230","Cuaderno 60"],["120 repartidos; uno recibe 20 más","x + (x + 20) = 120","50 y 70"]])]),
 S(2,"Edades",[E("Ana tiene el doble de edad que Beto y entre los dos suman 36 años","Beto tiene x años y Ana 2x.",["x + 2x = 36.","3x = 36.","Beto tiene 12 años y Ana, 24."])]),
 S(2,"Reparto",[E("Se reparten 120 pesos y una persona recibe 20 más","La que recibe menos tiene x y la otra x + 20.",["x + (x + 20) = 120.","2x = 100.","Reciben 50 y 70 pesos."])])],
 {"titulo":"Edades","planteo":"Ana tiene el doble de edad que Beto y suman 36 años. ¿Cuántos años tiene Beto?","pasos":["Beto tiene x y Ana 2x.","x + 2x = 36, entonces 3x = 36.","Beto tiene 12 años."]},
 {"titulo":"Completá","planteo":"Tres cuadernos iguales y una lapicera de 50 pesos cuestan 230.","pasos":["Se plantea: 3x + 50 = 230.","3x = 180, entonces x = ___ .","Cada cuaderno cuesta 60 pesos."]},
 {"titulo":"tu turno","planteo":"Se reparten 120 pesos entre dos personas y una recibe 20 más que la otra. ¿Cuánto recibe cada una?"},
 {"titulo":"Comprobar con el enunciado","texto":"Después de resolver, volvé al enunciado y fijate que los números cumplan lo que dice el problema."},
 ["Plantear x + 20 = 120 en el reparto.","Olvidar que hay dos personas y dar solo un valor."],
 RS(("Edades","Se expresa la otra edad a partir de la incógnita."),("Dinero","Se suma lo que cuesta cada cosa."),("Reparto","Las partes suman el total."),("Comprobar","Los resultados cumplen el enunciado.")),
 G(("Reparto","Dividir una cantidad entre varios."),("Total","Suma de todas las partes."),("Doble","Dos veces una cantidad."),("Diferencia","Cuánto más tiene uno que otro.")),
 ["Ana tiene el doble de edad que Beto y suman 36 años. ¿Cuántos años tiene Beto?","Tres cuadernos iguales y una lapicera de 50 pesos cuestan 230 pesos. ¿Cuánto cuesta un cuaderno?","Se reparten 120 pesos entre dos personas y una recibe 20 más. ¿Cuánto recibe la que recibe menos?","Un compañero resolvió el reparto con x + 20 = 120 y obtuvo 100. ¿Cuánto recibe en realidad la que recibe menos?"],
 ["aplicar","aplicar","aplicar","error"],
 [["12"],["60"],["50"],["50"]],
 {"incompleto":"60.","solo":"x + (x + 20) = 120, 2x = 100, x = 50. Reciben 50 y 70 pesos.","carpeta":["12.","60.","50.","50: las dos partes suman 120."]})
B3=NV("Vas a despejar una variable en fórmulas de geometría usando operaciones inversas, y a calcular con los datos.",
 ["Qué es despejar","Fórmulas de áreas","Fórmulas de perímetros","Reemplazar los datos"],[
 S(1,"Despejar una fórmula",[D("Despejar","Despejar una variable es <b>dejarla sola</b> de un lado de la fórmula usando operaciones inversas, igual que en una ecuación."),
  IM("Idea clave","De A = b · h se obtiene h = A / b.")]),
 S(1,"Ejemplos",[T("Fórmulas de geometría",["Fórmula","Se despeja","Resultado"],[["A = b · h","h","h = A / b"],["A = b · h / 2","h","h = 2A / b"],["P = 2b + 2h","h","h = (P − 2b) / 2"]])]),
 S(2,"Rectángulo",[E("Hallar h si el área es 30 y la base es 5","Se usa h = A / b.",["h = A / b.","h = 30 / 5.","h = 6."])]),
 S(2,"Triángulo",[E("Hallar h si el área del triángulo es 20 y la base es 8","Se usa h = 2A / b.",["h = 2A / b.","h = 40 / 8.","h = 5."])])],
 {"titulo":"Despejar y calcular","planteo":"Un rectángulo tiene área 30 y base 5. ¿Cuánto mide la altura?","pasos":["Se despeja: h = A / b.","h = 30 / 5.","La altura es 6."]},
 {"titulo":"Completá","planteo":"Un triángulo tiene área 20 y base 8.","pasos":["Se despeja: h = 2A / b.","h = 40 / 8 = ___ .","La altura es 5."]},
 {"titulo":"tu turno","planteo":"Un rectángulo tiene perímetro 24 y base 7. Despejar h en P = 2b + 2h y calcular."},
 {"titulo":"Primero despejar","texto":"Conviene despejar la letra que se busca antes de reemplazar los números. Así la cuenta queda más corta y ordenada."},
 ["Despejar h de A = b · h como h = A · b.","Olvidar el 2 en la fórmula del triángulo."],
 RS(("Despejar","Dejar la letra sola."),("Operación inversa","Se deshace con la contraria."),("Área","A = b · h en el rectángulo."),("Triángulo","A = b · h / 2.")),
 G(("Fórmula","Regla con letras que relaciona magnitudes."),("Despejar","Aislar una letra."),("Perímetro","Suma de los lados."),("Altura","Distancia desde la base hasta el lado opuesto.")),
 ["Un rectángulo tiene área 30 y base 5. ¿Cuánto mide la altura?","Un triángulo tiene área 20 y base 8. ¿Cuánto mide la altura?","Un rectángulo tiene perímetro 24 y base 7. ¿Cuánto mide la altura?","Un compañero despejó h de A = b · h como h = A · b. ¿Cuánto da h con A = 30 y b = 5 usando la fórmula correcta?"],
 ["aplicar","aplicar","aplicar","error"],
 [["6"],["5"],["5"],["6"]],
 {"incompleto":"5.","solo":"2h = 24 − 14 = 10, entonces h = 5.","carpeta":["6.","5.","5.","6: h = A / b, se divide."]})
B4=NV("Vas a despejar variables en fórmulas de velocidad, densidad y fuerza, y a calcular con los datos y sus unidades.",
 ["Fórmulas de física","Despejar el tiempo","Despejar la masa","Despejar la aceleración"],[
 S(1,"Fórmulas de física",[D("Fórmulas de física","En física se relacionan magnitudes con fórmulas: <b>v = d / t</b>, <b>δ = m / V</b> y <b>F = m · a</b>. Se despeja la letra que se busca."),
  IM("Idea clave","De v = d / t se obtiene t = d / v.")]),
 S(1,"Ejemplos",[T("Despejes frecuentes",["Fórmula","Se despeja","Resultado"],[["v = d / t","t","t = d / v"],["δ = m / V","m","m = δ · V"],["F = m · a","a","a = F / m"]])]),
 S(2,"Tiempo",[E("Un auto recorre 150 km a 50 km/h","Se despeja el tiempo.",["t = d / v.","t = 150 / 50.","Tarda 3 horas."])]),
 S(2,"Masa",[E("Un objeto tiene densidad 4 g/cm³ y volumen 50 cm³","Se despeja la masa.",["m = δ · V.","m = 4 · 50.","La masa es 200 g."])])],
 {"titulo":"Despejar el tiempo","planteo":"Un auto recorre 150 km a 50 km/h. ¿Cuántas horas tarda?","pasos":["Se despeja: t = d / v.","t = 150 / 50.","Tarda 3 horas."]},
 {"titulo":"Completá","planteo":"Una fuerza de 60 N actúa sobre una masa de 12 kg.","pasos":["Se despeja: a = F / m.","a = 60 / 12 = ___ .","La aceleración es 5 m/s²."]},
 {"titulo":"tu turno","planteo":"Un objeto de densidad 4 g/cm³ tiene 50 cm³. Despejar m y calcular su masa."},
 {"titulo":"Unidades","texto":"Después de calcular, escribí la unidad: horas, gramos o metros por segundo al cuadrado."},
 ["Despejar t de v = d / t como t = v / d.","Calcular sin escribir la unidad."],
 RS(("Velocidad","v = d / t."),("Densidad","δ = m / V."),("Fuerza","F = m · a."),("Despejar","Aislar la letra que busco.")),
 G(("Velocidad","Distancia por unidad de tiempo."),("Densidad","Masa por unidad de volumen."),("Fuerza","Masa por aceleración."),("Newton","Unidad de fuerza.")),
 ["Un auto recorre 150 km a 50 km/h. ¿Cuántas horas tarda?","Un objeto tiene densidad 4 g/cm³ y volumen 50 cm³. ¿Cuál es su masa, en gramos?","Una fuerza de 60 N actúa sobre una masa de 12 kg. ¿Cuánto vale la aceleración?","Un compañero despejó t de v = d / t como t = v / d. ¿Cuánto da t con d = 150 y v = 50 usando la fórmula correcta?"],
 ["aplicar","aplicar","aplicar","error"],
 [["3"],["200"],["5"],["3"]],
 {"incompleto":"5.","solo":"m = δ · V = 4 · 50 = 200 g.","carpeta":["3.","200.","5.","3: t = d / v."]})
L1=[N("El doble de un número es 18. ¿Cuál es el número?",{"acepta":[9]},"2x = 18.",n="aplicar"),
   MC("¿Qué ecuación traduce 'un número más 7 es 19'?",["x + 7 = 19","7x = 19","x + 19 = 7"],"x + 7 = 19","Más se escribe con suma.",n="aplicar"),
   FB("El triple de un número menos 4 se escribe 3x ___ 4",[["−","-","menos"]],"Menos se escribe con signo menos.",n="recordar")]
L2=[MAT("Uní cada situación con su ecuación.",["Ana tiene el doble que Beto; suman 36","3 cuadernos y una lapicera de 50; total 230","120 repartidos; uno recibe 20 más","Un número y su triple suman 40"],["x + 2x = 36","3x + 50 = 230","x + (x + 20) = 120","x + 3x = 40"],"Se elige la incógnita y se expresan las otras cantidades.",n="aplicar"),
   N("Beto y Ana suman 36 años y Ana tiene el doble. ¿Cuántos años tiene Ana?",{"acepta":[24]},"Beto tiene 12 y Ana 24.",n="aplicar"),
   VF("En un reparto donde una persona recibe 20 más, la ecuación es x + 20 = total.","Falso","Las dos partes suman el total: x + (x + 20).",n="error")]
L3=[ORD("Ordená los pasos para hallar h si A = 30 y b = 5.",["h = 6","h = 30 / 5","h = A / b"],["h = A / b","h = 30 / 5","h = 6"],"Primero se despeja.",n="aplicar"),
   MC("De A = b · h / 2, ¿cuál es h?",["h = 2A / b","h = A / 2b","h = A · b / 2","h = A / b"],"h = 2A / b","Se multiplica por 2 y se divide por b.",n="aplicar"),
   N("Un rectángulo tiene perímetro 24 y base 7. ¿Cuánto mide la altura?",{"acepta":[5]},"2h = 24 − 14.",n="aplicar")]
L4=[MC("De v = d / t, ¿cuál es el tiempo?",["t = d / v","t = v / d","t = 2d","t = d + 5"],"t = d / v","Se despeja t.",n="aplicar"),
   N("δ = 4 g/cm³ y V = 50 cm³. ¿Cuál es la masa, en gramos?",{"acepta":[200]},"m = δ · V.",n="aplicar"),
   CLF("¿Qué letra se despeja en cada caso?",["Hallar el tiempo","Hallar la masa","Hallar la aceleración"],["t","m","a"],{"Hallar el tiempo":"t","Hallar la masa":"m","Hallar la aceleración":"a"},"Se despeja la letra que se busca.",n="analizar")]
REL=[MC("Relámpago. El doble de un número es…",["2x","x + 2","x²"],"2x","El doble es por 2.",tiempo=20,n="recordar"),
   N("Relámpago. x + 2x = 21. ¿Cuánto vale x?",{"acepta":[7]},"3x = 21.",tiempo=25,n="recordar"),
   VF("Relámpago. De A = b · h se obtiene h = A / b.","Verdadero","Se divide por b.",tiempo=15,n="recordar"),
   FB("Relámpago. De v = d / t se obtiene t = d ÷ ___",[["v"]],"t = d / v.",tiempo=25,n="recordar")]
ACT={"1":L1,"2":L2,"3":L3,"4":L4,"5":REL}
EX=[[1,N("Un número y su doble suman 21. ¿Cuál es el número?",{"acepta":[7]},"x + 2x = 21.",n="aplicar")],
 [1,MC("La suma de un número y 9 es 25. ¿Cuál es el número?",["16","34","15","25"],"16","x + 9 = 25.",n="aplicar")],
 [1,SA("Un compañero escribió el doble de un número más 5 es 17 como 2(x + 5) = 17. Con 2x + 5 = 17, ¿cuál es el número?",["6"],"2x = 12.",n="error")],
 [2,N("Ana tiene el doble de edad que Beto y suman 36 años. ¿Cuántos años tiene Beto?",{"acepta":[12]},"x + 2x = 36.",n="aplicar")],
 [2,MC("Tres cuadernos iguales y una lapicera de 50 pesos cuestan 230. ¿Cuánto cuesta un cuaderno?",["60","180","93","50"],"60","3x + 50 = 230.",n="aplicar")],
 [2,SA("Un compañero resolvió el reparto de 120 pesos (uno recibe 20 más) con x + 20 = 120. ¿Cuánto recibe en realidad la que recibe menos?",["50"],"x + (x + 20) = 120.",n="error")],
 [3,MC("Un triángulo tiene área 20 y base 8. ¿Cuánto mide la altura?",["5","2.5","10","160"],"5","h = 2A / b.",n="aplicar")],
 [3,ORD("Ordená los pasos para despejar h de P = 2b + 2h.",["h = (P − 2b) / 2","2h = P − 2b","P = 2b + 2h"],["P = 2b + 2h","2h = P − 2b","h = (P − 2b) / 2"],"Se resta 2b y se divide por 2.",n="aplicar")],
 [3,SA("Un compañero despejó h de A = b · h como h = A · b. ¿Cuánto da h con A = 30 y b = 5 con la fórmula correcta?",["6"],"h = A / b.",n="error")],
 [4,SA("Un auto recorre 150 km a 50 km/h. ¿Cuántas horas tarda?",["3"],"t = d / v.",n="aplicar")],
 [4,MC("Una fuerza de 60 N actúa sobre 12 kg. ¿Cuánto vale la aceleración?",["5","720","48","0.2"],"5","a = F / m.",n="aplicar")],
 [4,MAT("Uní cada fórmula con su despeje.",["v = d / t","δ = m / V","F = m · a","A = b · h"],["t = d / v","m = δ · V","a = F / m","h = A / b"],"Se despeja la letra que se busca.",n="analizar")],
 [4,SA("Un compañero despejó t de v = d / t como t = v / d. ¿Cuánto da t con d = 150 y v = 50 con la fórmula correcta?",["3"],"t = d / v.",n="error")]]
M={"subject_id":SID,"tema":9,"practica":"Práctica general: problemas con ecuaciones y despeje de fórmulas","examen_titulo":"Nivel jefe: problemas con ecuaciones y despeje de fórmulas","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT,"examen":EX}
STEPS={1:"b662110d-dbb9-4f03-b59d-041f8bc7e77f",2:"ca04556a-5706-4fe1-a0c5-f046009199ee",3:"ba312671-e400-4357-83a9-456606e89b12",4:"132bfb64-d020-4d4f-8484-0a8c56aa3e43"}
TIT={1:"Traducir enunciados a ecuaciones",2:"Problemas de edades, dinero y repartos",3:"Despeje en fórmulas de geometría",4:"Despeje en fórmulas de física"}
CLS={1:[
 NOT("ENUNCIADO","Un problema escrito con palabras","Se traduce a una ecuación","📝","PROBLEMAS","los problemas con ecuaciones",["Noticia: los problemas se pueden traducir a ecuaciones.","Se elige la incógnita y se escribe la igualdad.","Hoy: *problemas con ecuaciones*."]),
 CMP(("ENUNCIADO","El doble de un número","📝"),("ECUACIÓN","2x","🧮"),"vs",["Dos formas de decir lo mismo.","El *enunciado* usa palabras: el doble de un número.","La *ecuación* usa letras: dos equis."]),
 DA("2x = 18","el doble de un número es dieciocho","x = 9","Se divide ambos miembros por dos","✖️",["Un dato clave.","Dos equis igual dieciocho da *equis igual nueve*."]),
 Q("Un número y su doble suman 21. El número es…",["7","21","10"],0,["Te toca: equis más dos equis igual veintiuno.","¿Siete, veintiuno o diez?","*Siete*: tres equis es veintiuno."]),
 RES(["Repasemos.","Se elige la *incógnita*.","Se *traduce* el enunciado a una ecuación.","Se resuelve y se *responde con palabras*.","¡Clase terminada! Ahora, *a practicar*."],[["INCÓGNITA","lo que se busca"],["PLANTEAR","traducir"],["RESPONDER","con palabras"]])],
2:[
 PRED("Ana tiene el doble de edad que Beto y suman 36. ¿Beto tiene…?",("12 años","🟦"),("18 años","🟧"),"a","x + 2x = 36",["Predicción: Ana tiene el doble de edad que Beto y suman treinta y seis.","Tres, dos, uno…","*Beto tiene doce*: equis más dos equis es treinta y seis."]),
 BQ("PROBLEMA DE REPARTO",[("LA MENOR PARTE","Se llama x"),("LA MAYOR PARTE","Es x + 20")],["Dos pasos.","La *menor parte* se llama equis.","La *mayor* es equis más veinte, y las dos suman el total."]),
 ZO([("🔭","x + 2x = 36"),("🔬","3x + 50 = 230"),("🧬","x + (x + 20) = 120")],["Tres problemas, tres ecuaciones.","Las edades dan *equis más dos equis*.","Y el reparto da *equis más equis más veinte*."]),
 Q("Tres cuadernos y una lapicera de 50 cuestan 230. Un cuaderno cuesta…",["60","93","50"],0,["Te toca: tres equis más cincuenta igual doscientos treinta.","¿Sesenta, noventa y tres o cincuenta?","*Sesenta pesos*."]),
 RES(["Repasemos.","En las *edades*, la otra edad se expresa con la incógnita.","En el *dinero*, se suma lo que cuesta cada cosa.","En el *reparto*, las partes suman el total.","¡Clase terminada! Ahora, *a practicar*."],[["EDADES","a partir de la incógnita"],["DINERO","suma de costos"],["REPARTO","partes suman el total"]])],
3:[
 DA("A = b · h","área del rectángulo","h = A / b","Para hallar la altura se divide el área por la base","📐",["Un dato clave.","Si el área es *base por altura*, la altura es el área dividida la base."]),
 EQ(["A = b · h","h = A / b","h = 30 / 5 = 6"],["la fórmula","se despeja h","se reemplaza"],["La fórmula es *área igual base por altura*.","Se despeja la altura: *h es área sobre base*.","Con área treinta y base cinco, *h vale seis*."]),
 CL([("SE DIVIDE","➗"),("SE MULTIPLICA","✖️")],[("h = A / b",0),("A = b · h",1),("t = d / v",0),("m = δ · V",1)],["¿Se divide o se multiplica?","Para hallar *h* o *t*, se divide.","Para hallar el *área* o la *masa*, se multiplica."]),
 Q("De A = b · h se obtiene…",["h = A / b","h = A · b","h = b / A"],0,["Te toca: despejar h de área igual base por altura.","¿Área sobre base, área por base o base sobre área?","*Área sobre base*."]),
 RES(["Repasemos.","*Despejar* es dejar la letra sola.","Se usa la *operación inversa*.","Primero se despeja y *después se reemplaza*.","¡Clase terminada! Ahora, *a practicar*."],[["DESPEJAR","dejar la letra sola"],["INVERSA","la operación contraria"],["REEMPLAZAR","después de despejar"]])],
4:[
 RET("De v = d / t, ¿cuánto vale d?",8,"d = v · t","🚗","DESPEJE","el despeje en física",["Desafío: ¿cuánto vale d en v igual d sobre t? Ocho segundos.","*d es v por t*.","Hoy: *despeje en fórmulas de física*."]),
 PAT("DESPEJES",["v = d / t","t = d / v","δ = m / V"],"m = δ · V","se pasa multiplicando o dividiendo",["Tres fórmulas y su despeje.","Velocidad, tiempo y densidad.","¿Y la siguiente? *Masa igual densidad por volumen*."]),
 QZ("¿Cuánto es a en F = m · a si F = 60 y m = 12?",["5","720"],0,["Un quiz rápido: sesenta newtons y doce kilos.","¿Cinco o setecientos veinte?","*Cinco*: se divide la fuerza por la masa."]),
 Q("Un auto recorre 150 km a 50 km/h. Tarda…",["3 h","7500 h","200 h"],0,["Te toca: ciento cincuenta kilómetros a cincuenta por hora.","¿Tres horas, siete mil quinientas o doscientas?","*Tres horas*: distancia sobre velocidad."]),
 RES(["Repasemos.","De v = d / t se despeja *t = d / v* y *d = v · t*.","De δ = m / V se obtiene *m = δ · V*.","De F = m · a se obtiene *a = F / m*.","¡Clase terminada! Ahora, *a practicar*."],[["VELOCIDAD","d / t"],["DENSIDAD","m / V"],["FUERZA","m · a"]])]}
escribir(9, M, STEPS, TIT, CLS)
