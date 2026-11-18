# -*- coding: utf-8 -*-
"""Matemática I · Misión 11 · Números enteros: concepto, orden y recta. Genera mision-11.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
neg=lambda n:["-%s"%n,"−%s"%n]  # acepta guion o signo menos
N1={
"objetivo":"Vas a poder usar números negativos para describir situaciones, reconocer positivos, negativos y el cero, y encontrar el opuesto de un número.",
"vas_a_ver":["Situaciones que necesitan números negativos","Positivos, negativos y el cero","El signo del número y el signo de restar","El opuesto de un número","El conjunto de los enteros"],
"secciones":[
 S(1,"Por qué hacen falta",[
  D("Números negativos","Los <b>números negativos</b> sirven para indicar cantidades <b>por debajo de un punto de referencia</b>, el cero. Se escriben con el signo −: −3."),
  T("Situaciones",["Situación","Número"],[["3 °C bajo cero","−3"],["Debo $500","−500"],["Segundo subsuelo","−2"],["Al nivel del mar","0"],["Piso 4","4"]],"El cero es la referencia: la planta baja, el nivel del mar, cero grados, no deber ni tener."),
 ]),
 S(1,"Positivos, negativos y cero",[
  D("Clasificación","Los números mayores que 0 son <b>positivos</b> (se pueden escribir con + o sin signo); los menores que 0 son <b>negativos</b>. El <b>0 no es ni positivo ni negativo</b>."),
  IM("Dos usos del signo","En 8 − 3 el signo indica una resta. En −3 indica que el número es negativo."),
 ]),
 S(2,"El opuesto",[
  P("El <b>opuesto</b> de un número es el que está a la misma distancia del 0, pero del otro lado: el opuesto de 5 es −5 y el opuesto de −3 es 3. El opuesto de 0 es 0. En situaciones: ganar $200 y perder $200 son opuestos."),
 ]),
 S(2,"Los números enteros",[
  P("Los naturales, el cero y los negativos forman el conjunto de los <b>números enteros</b>: …, −3, −2, −1, 0, 1, 2, 3, … No tiene principio ni fin."),
 ]),
],
"ejemplo_completo":{"titulo":"el buzo y el avión","planteo":"Escribí con números enteros: un buzo a 15 m bajo el agua, un avión a 3.000 m de altura y el nivel del mar. Después escribí el opuesto de cada uno.","pasos":["El nivel del mar es la referencia: 0.","Buzo: −15. Avión: 3.000.","Opuestos: el de −15 es 15; el de 3.000 es −3.000; el de 0 es 0."]},
"ejemplo_incompleto":{"titulo":"el saldo","planteo":"Completá los espacios.","pasos":["Un saldo deudor de $800 se escribe ___ .","Su opuesto es ___ .","El opuesto de 0 es ___ ."]},
"ejemplo_solo":{"titulo":"escribir enteros","planteo":"Escribí como número entero: 12 °C bajo cero; el piso 3; el opuesto de −25."},
"tip":{"titulo":"Buscá la referencia","texto":"Antes de poner el signo, preguntate dónde está el cero en esa situación: planta baja, nivel del mar, cero grados."},
"ojo":["Creer que el 0 es negativo: no es ni positivo ni negativo.","Confundir el signo de resta con el del número: en 8 − 3 no hay ningún número negativo."],
"resumen":[{"titulo":"Negativos","texto":"Menores que 0. Ej.: −3 °C."},{"titulo":"El cero","texto":"Ni positivo ni negativo: es la referencia."},{"titulo":"Opuesto","texto":"Del otro lado del 0. Ej.: 5 y −5."},{"titulo":"Enteros","texto":"…, −2, −1, 0, 1, 2, …"}],
"glosario":[{"palabra":"Negativo","significado":"Número menor que 0."},{"palabra":"Positivo","significado":"Número mayor que 0."},{"palabra":"Opuesto","significado":"Número a la misma distancia del 0, del otro lado."},{"palabra":"Enteros","significado":"Los naturales, el 0 y los negativos."}],
"carpeta":["¿Qué número entero representa 8 °C bajo cero?","¿Cuál es el opuesto de −14?","¿Cuál es el opuesto del opuesto de 6?","Un compañero dice que el 0 es negativo. ¿Cuál es el opuesto de 0?"],
"respuestas_carpeta":[neg(8),["14"],["6"],["0"]],
"soluciones":{"incompleto":"−800. 800. 0.","solo":"−12; 3; 25.","carpeta":["−8: bajo cero es negativo.","14: del otro lado del 0.","6: el opuesto de 6 es −6, y el opuesto de −6 es 6.","0: el 0 es su propio opuesto; no es ni positivo ni negativo."]}
}
N2={
"objetivo":"Vas a poder ubicar números enteros en la recta numérica y calcular la distancia entre dos enteros, aunque crucen el cero.",
"vas_a_ver":["La recta numérica entera","Dónde van los negativos","Simetría respecto del cero","Distancia entre dos enteros"],
"secciones":[
 S(1,"La recta entera",[
  D("Recta numérica entera","Se marca el 0 y se dejan <b>espacios iguales</b> hacia los dos lados: a la <b>derecha</b> van los positivos (1, 2, 3…) y a la <b>izquierda</b> los negativos (−1, −2, −3…)."),
  P("Los negativos se numeran alejándose del cero: primero −1, después −2, después −3. Si los espacios no son iguales, la recta engaña."),
 ]),
 S(1,"Simetría",[
  D("Simétricos","Un número y su opuesto están a la <b>misma distancia del 0</b>, uno a cada lado: −4 y 4 están los dos a 4 unidades del cero."),
 ]),
 S(2,"Distancia entre enteros",[
  P("La distancia entre dos enteros es la cantidad de unidades que hay de uno a otro en la recta. Siempre es un número positivo (o cero)."),
  E("Contar en la recta","Tres casos.",["Del mismo lado: de −8 a −2 hay 6 unidades.","Cruzando el cero: de −3 a 4 hay 3 hasta el 0 y 4 más: 7.","Del 0 a −5 hay 5 unidades."]),
 ]),
 S(2,"Situaciones",[
  E("El ascensor","Un ascensor va del subsuelo −2 al piso 5.",["Del −2 al 0 (planta baja): 2 pisos.","Del 0 al 5: 5 pisos.","Recorre 7 pisos."]),
 ]),
],
"ejemplo_completo":{"titulo":"de −5 a 3","planteo":"¿Qué distancia hay entre −5 y 3?","pasos":["Están de lados distintos del cero.","De −5 a 0 hay 5 unidades.","De 0 a 3 hay 3 unidades.","Distancia: 5 + 3 = 8."]},
"ejemplo_incompleto":{"titulo":"distancias","planteo":"Completá los espacios.","pasos":["De −6 a −1, contando en la recta, hay ___ unidades.","De −2 a 5: 2 + 5 = ___ ."]},
"ejemplo_solo":{"titulo":"el ascensor","planteo":"Un ascensor está en el subsuelo −3 y sube al piso 6. ¿Cuántos pisos recorre?"},
"tip":{"titulo":"Si cruza el cero, sumá","texto":"Si un número es negativo y el otro positivo, la distancia es la suma de las distancias de cada uno al cero."},
"ojo":["Numerar los negativos al revés: a la izquierda del 0 va primero el −1.","Contar mal cuando se cruza el cero: de −3 a 5 hay 8, no 2."],
"resumen":[{"titulo":"Recta","texto":"Positivos a la derecha, negativos a la izquierda, espacios iguales."},{"titulo":"Simetría","texto":"−4 y 4 están a 4 del cero."},{"titulo":"Mismo lado","texto":"De −8 a −2: 6."},{"titulo":"Cruzando el cero","texto":"De −3 a 4: 3 + 4 = 7."}],
"glosario":[{"palabra":"Recta numérica","significado":"Línea con los números ubicados en orden y a igual distancia."},{"palabra":"Distancia","significado":"Cantidad de unidades entre dos números."},{"palabra":"Simétrico","significado":"A la misma distancia, del otro lado."}],
"carpeta":["¿Qué distancia hay entre −4 y 0?","¿Qué distancia hay entre −7 y 2?","¿Qué número está a la misma distancia del 0 que −9, pero del otro lado?","Un compañero contó la distancia entre −3 y 5 y le dio 2. ¿Cuál es la distancia correcta?"],
"respuestas_carpeta":[["4"],["9"],["9"],["8"]],
"soluciones":{"incompleto":"5 unidades. 7.","solo":"Del −3 al 0: 3 pisos. Del 0 al 6: 6 pisos. Recorre 9 pisos.","carpeta":["4: cuatro unidades hasta el cero.","9: 7 + 2.","9: es el opuesto de −9.","8: 3 hasta el 0 y 5 más. Restó 5 − 3."]}
}
N3={
"objetivo":"Vas a poder comparar y ordenar números enteros, incluidos los negativos, y listar los enteros de un intervalo.",
"vas_a_ver":["Comparar en la recta","Por qué −5 es menor que −2","Ordenar de menor a mayor y de mayor a menor","Los enteros entre dos números"],
"secciones":[
 S(1,"Comparar en la recta",[
  D("Mayor y menor","En la recta, de dos números es <b>mayor el que está más a la derecha</b>. Por eso todo positivo es mayor que 0, y 0 es mayor que todo negativo."),
  P("Se escribe con los signos < (menor que) y > (mayor que): −3 < 0 < 2."),
 ]),
 S(1,"Los negativos",[
  D("Entre negativos","Entre dos negativos, es <b>menor el que está más lejos del cero</b>: −5 < −2."),
  T("Temperaturas de una semana",["Día","Lunes","Martes","Miércoles","Jueves"],[["Temperatura","−4 °C","−1 °C","2 °C","−6 °C"]],"El día más frío fue el jueves (−6 °C) y el más templado, el miércoles (2 °C)."),
 ]),
 S(2,"Ordenar",[
  E("De menor a mayor","Ordenamos 3, −8, 0, −1, −12 y 5.",["Primero los negativos, del más lejano al más cercano al cero: −12, −8, −1.","Después el 0.","Después los positivos: 3, 5.","−12 < −8 < −1 < 0 < 3 < 5."]),
 ]),
 S(2,"Enteros de un intervalo",[
  P("Los enteros mayores que −3 y menores que 2 son −2, −1, 0 y 1. Ojo de no olvidar el cero."),
 ]),
],
"ejemplo_completo":{"titulo":"temperaturas","planteo":"Ordená de menor a mayor las temperaturas de la tabla: −4, −1, 2 y −6.","pasos":["Negativos, del más lejano al cero: −6, −4, −1.","Después el positivo: 2.","−6 < −4 < −1 < 2."]},
"ejemplo_incompleto":{"titulo":"comparar","planteo":"Completá los espacios.","pasos":["Entre −5 y −9, el mayor es ___ .","Los enteros mayores que −3 y menores que 1 son −2, ___ y 0."]},
"ejemplo_solo":{"titulo":"de mayor a menor","planteo":"Ordená de mayor a menor: −6, 4, −2, 0, −10."},
"tip":{"titulo":"Pensá en temperaturas","texto":"−10 °C es más frío que −2 °C: el que está más lejos del cero hacia abajo es el menor."},
"ojo":["Ordenar los negativos como si fueran positivos: −6 es menor que −2, aunque 6 sea mayor que 2.","Olvidar el cero al listar los enteros de un intervalo."],
"resumen":[{"titulo":"Mayor","texto":"El de más a la derecha."},{"titulo":"Negativos","texto":"Más lejos del 0, más chico. Ej.: −5 < −2."},{"titulo":"Orden","texto":"Negativos < 0 < positivos."},{"titulo":"Intervalo","texto":"Entre −3 y 2: −2, −1, 0, 1."}],
"glosario":[{"palabra":"Orden creciente","significado":"De menor a mayor."},{"palabra":"Orden decreciente","significado":"De mayor a menor."},{"palabra":"Intervalo","significado":"Los números que están entre dos dados."}],
"carpeta":["¿Cuál es mayor: −5 o −2?","¿Cuántos enteros hay entre −4 y 3, sin contar a −4 ni a 3?","¿Cuál es el menor de estos números: −1, −15, 0, −7?","Un compañero escribió −2 < −6 porque 2 es menor que 6. ¿Cuál de los dos es el menor?"],
"respuestas_carpeta":[neg(2),["6"],neg(15),neg(6)],
"soluciones":{"incompleto":"−5. −1.","solo":"4 > 0 > −2 > −6 > −10.","carpeta":["−2: está más cerca del cero.","6: −3, −2, −1, 0, 1 y 2.","−15: es el más lejano del cero hacia la izquierda.","−6: está más a la izquierda en la recta."]}
}
N4={
"objetivo":"Vas a poder calcular el valor absoluto de un entero como una distancia, diferenciarlo del opuesto y usarlo en problemas.",
"vas_a_ver":["El valor absoluto como distancia al cero","El opuesto de un número","Valor absoluto y opuesto juntos","Problemas de distancia"],
"secciones":[
 S(1,"Valor absoluto",[
  D("Valor absoluto","El <b>valor absoluto</b> de un número es su <b>distancia al cero</b>. Se escribe entre barras: |−7| = 7 y |7| = 7. Como es una distancia, <b>nunca es negativo</b>."),
  P("|0| = 0. Y |−3| no es −3: es 3, porque −3 está a 3 unidades del cero."),
 ]),
 S(1,"Opuesto",[
  D("Opuesto","El <b>opuesto</b> de un número es el que está del otro lado del cero, a la misma distancia. El opuesto de 5 es −5; el de −8 es 8."),
 ]),
 S(2,"No son lo mismo",[
  T("Valor absoluto y opuesto",["Número","Valor absoluto","Opuesto"],[["−3","3","3"],["5","5","−5"],["0","0","0"]],"Para un negativo coinciden; para un positivo, no. El valor absoluto nunca da negativo; el opuesto sí puede."),
 ]),
 S(2,"Problemas de distancia",[
  E("Los buzos","Un buzo está a −12 m y otro a −30 m. ¿Cuántos metros los separan?",["|−12| = 12 y |−30| = 30.","Los dos están del mismo lado del cero.","Los separan 30 − 12 = 18 m."]),
 ]),
],
"ejemplo_completo":{"titulo":"−9 y 4","planteo":"Compará −9 y 4, y compará sus valores absolutos.","pasos":["En la recta, −9 está a la izquierda: −9 < 4.","|−9| = 9 y |4| = 4.","Entonces |−9| > |4|.","El menor número tiene el mayor valor absoluto: está más lejos del cero."]},
"ejemplo_incompleto":{"titulo":"−15 y 15","planteo":"Completá los espacios.","pasos":["|−15| = ___ .","El opuesto de −15 es ___ .","El opuesto de 15 es ___ .","|15| = 15."]},
"ejemplo_solo":{"titulo":"dos ciudades","planteo":"Un termómetro marca −6 °C en una ciudad y 4 °C en otra. ¿Cuál está más lejos de 0 °C? ¿Qué diferencia de temperatura hay entre las dos?"},
"tip":{"titulo":"Pensá en distancia","texto":"Para el valor absoluto, preguntate a cuántos pasos del cero está el número. No es una regla de cambiar signos."},
"ojo":["Creer que el valor absoluto siempre cambia el signo: |5| = 5.","Confundir opuesto con valor absoluto: el opuesto de 5 es −5, pero |5| = 5."],
"resumen":[{"titulo":"Valor absoluto","texto":"Distancia al 0. Ej.: |−7| = 7."},{"titulo":"Nunca negativo","texto":"|−3| = 3, no −3."},{"titulo":"Opuesto","texto":"Del otro lado. Ej.: 5 → −5."},{"titulo":"Distancias","texto":"Buzos a −12 y −30: 18 m."}],
"glosario":[{"palabra":"Valor absoluto","significado":"Distancia de un número al cero."},{"palabra":"Barras","significado":"El signo | | del valor absoluto."},{"palabra":"Opuesto","significado":"El número del otro lado del cero, a la misma distancia."}],
"carpeta":["Calculá |−23|.","Escribí el número negativo cuyo valor absoluto es 8.","¿Cuál es el opuesto de |−5|?","Un compañero escribió |−3| = −3. ¿Cuánto vale |−3|?"],
"respuestas_carpeta":[["23"],neg(8),neg(5),["3"]],
"soluciones":{"incompleto":"15. 15. −15.","solo":"|−6| = 6 y |4| = 4: la de −6 °C está más lejos de 0. Diferencia: 6 + 4 = 10 grados.","carpeta":["23: está a 23 del cero.","−8: |−8| = 8.","−5: |−5| = 5 y su opuesto es −5.","3: es una distancia, no puede ser negativa."]}
}
ACT={
"1":[MC("¿Qué número representa \"debo $300\"?",["300","−300","0","3"],"−300","Deber es estar por debajo del cero."),
     VF("El 0 es un número negativo.","Falso","El 0 no es ni positivo ni negativo.")],
"2":[N("¿Qué distancia hay entre {a} y {b}?",{"formula":"x+b"},"Se cruza el cero: se suman las distancias de cada uno al cero.",{"vars":{"x":{"min":1,"max":9},"b":{"min":1,"max":9}},"calculadas":{"a":"0-x"}}),
     MC("En la recta numérica, ¿de qué lado del 0 están los negativos?",["A la izquierda","A la derecha"],"A la izquierda","Los positivos van a la derecha.")],
"3":[MC("¿Cuál es mayor?",["−8","−3"],"−3","Está más cerca del cero, más a la derecha."),
     {"t":"ordering","p":"Ordená de menor a mayor.","o":["0","−4","2","−9"],"r":{"orden":["−9","−4","0","2"]},"e":"Primero el negativo más lejano del cero."}],
"4":[N("Calculá |{a}|.",{"formula":"x"},"El valor absoluto es la distancia al cero.",{"vars":{"x":{"min":2,"max":50}},"calculadas":{"a":"0-x"}}),
     MC("¿Cuál es el opuesto de 6 y cuál es su valor absoluto?",["−6 y 6","6 y −6","−6 y −6","6 y 6"],"−6 y 6","El opuesto está del otro lado; el valor absoluto es la distancia.")],
"5":[MC("Relámpago. ¿Cuál es menor?",["0","−1"],"−1","Todo negativo es menor que 0.",tiempo=15),
     N("Relámpago. Calculá |−12|.",{"acepta":[12]},"Está a 12 del cero.",tiempo=20),
     N("Relámpago. ¿Qué distancia hay entre −2 y 3?",{"acepta":[5]},"2 + 3 = 5.",tiempo=30),
     N("Relámpago. Calculá 0,5 + 0,25.",{"acepta":[0.75]},"Repaso de la misión 10.",tiempo=30)],
}
EXAMEN=[
 [1,MC("¿Qué número representa \"dos subsuelos debajo de la planta baja\"?",["2","−2","0","−20"],"−2","La planta baja es el 0.")],
 [1,N("¿Cuál es el opuesto de −31?",{"acepta":[31]},"Del otro lado del cero.")],
 [1,{"t":"classify","p":"Clasificá cada número.","o":{"elementos":["−7","0","12","−1","5"],"categorias":["Positivo","Negativo","Ni positivo ni negativo"]},"r":{"categorias":{"−7":"Negativo","0":"Ni positivo ni negativo","12":"Positivo","−1":"Negativo","5":"Positivo"}},"e":"El 0 no es ni positivo ni negativo."}],
 [2,N("¿Qué distancia hay entre −8 y 5?",{"acepta":[13]},"8 + 5 = 13.")],
 [2,VF("−4 y 4 están a la misma distancia del 0.","Verdadero","Son opuestos: los dos están a 4 unidades.")],
 [2,N("¿Qué distancia hay entre −10 y −3?",{"acepta":[7]},"Del mismo lado: 10 − 3 = 7.")],
 [3,MC("¿Cuál es el mayor?",["−20","−2","−12","−7"],"−2","Es el más cercano al cero.")],
 [3,{"t":"ordering","p":"Ordená de menor a mayor.","o":["−1","−11","6","0","−5"],"r":{"orden":["−11","−5","−1","0","6"]},"e":"Negativos del más lejano al más cercano al cero, después el 0 y los positivos."}],
 [3,N("¿Cuántos números enteros hay que sean mayores que −5 y menores que 2?",{"acepta":[6]},"−4, −3, −2, −1, 0 y 1.")],
 [4,N("Calculá |−18|.",{"acepta":[18]},"Distancia al cero.")],
 [4,MC("¿Qué número tiene valor absoluto 9 y es menor que 0?",["9","−9","0","1/9"],"−9","|−9| = 9 y es negativo.")],
 [4,VF("El valor absoluto de un número nunca es negativo.","Verdadero","Es una distancia.")],
 [4,N("Un buzo está a −12 m y otro a −30 m. ¿Cuántos metros los separan?",{"acepta":[18]},"30 − 12 = 18.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":11,"practica":"Práctica general: números enteros","examen_titulo":"Nivel jefe: números enteros",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-11.json"),"w"),ensure_ascii=False)
print("ok")
