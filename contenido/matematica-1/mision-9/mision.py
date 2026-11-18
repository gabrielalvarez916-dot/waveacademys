# -*- coding: utf-8 -*-
"""Matemática I · Misión 9 · Operaciones con fracciones. Genera mision-9.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
N1={
"objetivo":"Vas a poder sumar y restar fracciones, con igual o distinto denominador y con números mixtos, y usarlas para resolver problemas.",
"vas_a_ver":["Sumar y restar con igual denominador","Buscar el denominador común con el MCM","Sumar y restar números mixtos","Problemas de suma y resta"],
"secciones":[
 S(1,"Igual denominador",[
  D("Suma y resta con igual denominador","Si las fracciones tienen el <b>mismo denominador</b>, se suman o restan los <b>numeradores</b> y se deja el denominador: 2/7 + 3/7 = 5/7."),
  P("Es como sumar porciones del mismo tamaño: 2 séptimos más 3 séptimos son 5 séptimos. Ejemplo de resta: 5/8 − 1/8 = 4/8 = 1/2 (siempre se simplifica al final)."),
 ]),
 S(1,"Distinto denominador",[
  D("Denominador común","Si los denominadores son distintos, primero se pasan a fracciones equivalentes con un <b>denominador común</b>. El más cómodo es el <b>MCM</b> de los denominadores."),
  E("1/4 + 1/6","El MCM de 4 y 6 es 12.",["1/4 = 3/12 y 1/6 = 2/12.","3/12 + 2/12 = 5/12."]),
 ]),
 S(2,"Números mixtos",[
  P("Se pueden pasar a fracciones impropias, o sumar los enteros por un lado y las fracciones por otro."),
  E("2 1/3 + 1 1/2","Dos formas.",["Impropias: 7/3 + 3/2 = 14/6 + 9/6 = 23/6 = 3 5/6.","Por partes: 2 + 1 = 3 y 1/3 + 1/2 = 5/6. Total 3 5/6."]),
 ]),
 S(2,"Problemas",[
  E("La torta","Ana comió 1/3 de una torta y Beto 1/4. ¿Cuánto comieron? ¿Cuánto queda?",["1/3 + 1/4 = 4/12 + 3/12 = 7/12.","La torta entera es 12/12.","Queda 12/12 − 7/12 = 5/12."]),
 ]),
],
"ejemplo_completo":{"titulo":"5/6 − 3/8","planteo":"Calculá 5/6 − 3/8.","pasos":["MCM(6, 8) = 24.","5/6 = 20/24 y 3/8 = 9/24.","20/24 − 9/24 = 11/24.","11/24 ya es irreducible."]},
"ejemplo_incompleto":{"titulo":"3/4 + 1/6","planteo":"Completá los espacios.","pasos":["MCM(4, 6) = ___ .","3/4 = ___ /12 y 1/6 = 2/12.","3/4 + 1/6 = ___ /12."]},
"ejemplo_solo":{"titulo":"3 1/2 − 1 2/3","planteo":"Calculá 3 1/2 − 1 2/3 y escribí el resultado como número mixto."},
"tip":{"titulo":"Simplificá al final","texto":"Después de sumar o restar, fijate si el resultado se puede simplificar: 4/8 es 1/2."},
"ojo":["Sumar numeradores y denominadores: 1/2 + 1/4 no es 2/6; es 2/4 + 1/4 = 3/4.","Usar un denominador que no es múltiplo de los dos: para 1/4 y 1/6, 10 no sirve."],
"resumen":[{"titulo":"Igual denominador","texto":"Se suman los numeradores. Ej.: 2/7 + 3/7 = 5/7."},{"titulo":"Distinto","texto":"Denominador común con el MCM. Ej.: 1/4 + 1/6 = 5/12."},{"titulo":"Mixtos","texto":"Impropias o por partes. Ej.: 2 1/3 + 1 1/2 = 3 5/6."},{"titulo":"Al final","texto":"Simplificar el resultado."}],
"glosario":[{"palabra":"Denominador común","significado":"El mismo denominador para varias fracciones."},{"palabra":"MCM","significado":"El menor múltiplo común: el denominador común más chico."},{"palabra":"Número mixto","significado":"Enteros más una fracción propia."}],
"carpeta":["Calculá 2/9 + 5/9.","Calculá 1/2 + 1/3.","Calculá 7/10 − 1/5 y simplificá el resultado.","Un compañero hizo 1/2 + 1/4 = 2/6. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["7/9"],["5/6"],["1/2"],["3/4"]],
"soluciones":{"incompleto":"MCM 12. 3/4 = 9/12. Resultado: 11/12.","solo":"7/2 − 5/3 = 21/6 − 10/6 = 11/6 = 1 5/6.","carpeta":["7/9: mismo denominador.","5/6: 3/6 + 2/6.","1/2: 7/10 − 2/10 = 5/10 = 1/2.","3/4: 2/4 + 1/4. No se suman los denominadores."]}
}
N2={
"objetivo":"Vas a poder multiplicar fracciones, simplificar antes de multiplicar y calcular la fracción de una fracción.",
"vas_a_ver":["Cómo se multiplican dos fracciones","Por qué el producto puede achicar","Simplificar antes de multiplicar","Fracción de una fracción","Multiplicar con enteros y números mixtos"],
"secciones":[
 S(1,"El producto de fracciones",[
  D("Multiplicar fracciones","Se multiplican <b>numerador por numerador</b> y <b>denominador por denominador</b>: a/b × c/d = (a × c)/(b × d). No hace falta denominador común."),
  P("Ejemplo: 2/3 × 4/5 = 8/15. En un rectángulo, si pintás 2/3 de alto y 4/5 de ancho, la parte pintada dos veces es 8 de las 15 partes. Por eso, al multiplicar por una fracción menor que 1, el resultado <b>achica</b>."),
 ]),
 S(1,"Fracción de una fracción",[
  D("\"De\" es por","Calcular una fracción <b>de</b> otra es multiplicarlas: 1/2 de 3/4 = 1/2 × 3/4 = 3/8."),
  P("La mitad de tres cuartos de pizza son tres octavos de pizza."),
 ]),
 S(2,"Simplificar antes",[
  P("Antes de multiplicar, se puede simplificar <b>un numerador con un denominador</b> (aunque estén en fracciones distintas). Así los números quedan más chicos."),
  E("4/9 × 3/8","Simplificamos cruzado.",["4 y 8 se dividen por 4: quedan 1 y 2.","3 y 9 se dividen por 3: quedan 1 y 3.","1/3 × 1/2 = 1/6."]),
 ]),
 S(2,"Con enteros y mixtos",[
  P("Un entero se escribe como fracción con denominador 1: 3 × 2/5 = 3/1 × 2/5 = 6/5. Un número mixto se pasa a impropia: 1 1/2 × 2/3 = 3/2 × 2/3 = 6/6 = 1."),
 ]),
],
"ejemplo_completo":{"titulo":"2 1/4 × 8/15","planteo":"Calculá 2 1/4 × 8/15.","pasos":["2 1/4 = 9/4.","9/4 × 8/15: 9 y 15 se simplifican por 3 (quedan 3 y 5); 4 y 8 por 4 (quedan 1 y 2).","3/1 × 2/5 = 6/5.","6/5 = 1 1/5."]},
"ejemplo_incompleto":{"titulo":"3/4 de 2/5","planteo":"Completá los espacios.","pasos":["3/4 de 2/5 = 3/4 × 2/5.","3 × 2 = 6 y 4 × 5 = 20: ___ /20.","Simplificado: ___ ."]},
"ejemplo_solo":{"titulo":"5/6 × 9/10","planteo":"Calculá 5/6 × 9/10 simplificando antes de multiplicar."},
"tip":{"titulo":"Simplificá cruzado","texto":"Mirá cada numerador con cada denominador: si comparten un divisor, simplificá antes. El resultado sale irreducible."},
"ojo":["Buscar denominador común para multiplicar: no hace falta, eso es para sumar.","Perder el entero: 1 1/2 × 2 no es 1 × 2 + 1/2; se pasa primero a 3/2."],
"resumen":[{"titulo":"Producto","texto":"Arriba por arriba, abajo por abajo. Ej.: 2/3 × 4/5 = 8/15."},{"titulo":"\"De\"","texto":"1/2 de 3/4 = 3/8."},{"titulo":"Simplificar antes","texto":"4/9 × 3/8 = 1/6."},{"titulo":"Enteros y mixtos","texto":"3 = 3/1; 1 1/2 = 3/2."}],
"glosario":[{"palabra":"Producto","significado":"El resultado de una multiplicación."},{"palabra":"Simplificar cruzado","significado":"Dividir un numerador y un denominador de distintas fracciones por el mismo número."},{"palabra":"Fracción de una fracción","significado":"Una parte de una parte: se multiplica."}],
"carpeta":["Calculá 2/3 × 3/7.","¿Cuánto es 1/2 de 4/5?","Calculá 4 × 3/8.","Un compañero, para calcular 1/2 × 1/3, buscó denominador común. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["2/7","6/21"],["2/5","4/10"],["3/2","12/8"],["1/6"]],
"soluciones":{"incompleto":"6/20. Simplificado: 3/10.","solo":"5 y 10 por 5: 1 y 2. 9 y 6 por 3: 3 y 2. 1/2 × 3/2 = 3/4.","carpeta":["2/7: 6/21 simplificado por 3.","2/5: 4/10 simplificado.","3/2: 12/8 simplificado por 4.","1/6: 1 × 1 = 1 y 2 × 3 = 6. Para multiplicar no hace falta denominador común."]}
}
N3={
"objetivo":"Vas a poder dividir fracciones multiplicando por el inverso y resolver problemas de \"cuántas veces entra\".",
"vas_a_ver":["El inverso de una fracción","Dividir es multiplicar por el inverso","Por qué dividir por una fracción puede agrandar","Dividir con enteros y mixtos","Problemas de reparto"],
"secciones":[
 S(1,"El inverso",[
  D("Inverso multiplicativo","El <b>inverso</b> de a/b es <b>b/a</b>: se da vuelta la fracción. Una fracción por su inverso da 1: 3/4 × 4/3 = 12/12 = 1."),
  P("El inverso de 5 (o 5/1) es 1/5. El 0 no tiene inverso."),
 ]),
 S(1,"Dividir con el inverso",[
  D("División de fracciones","Para dividir, se <b>multiplica la primera por el inverso de la segunda</b>: a/b ÷ c/d = a/b × d/c."),
  P("Ejemplo: 3/4 ÷ 2/5 = 3/4 × 5/2 = 15/8. Se da vuelta solo la segunda fracción, la que divide."),
 ]),
 S(2,"Cuántas veces entra",[
  P("Dividir también responde <b>cuántas veces entra</b> un número en otro. En 3 enteros entran 12 cuartos: 3 ÷ 1/4 = 3 × 4 = 12. Por eso, dividir por una fracción menor que 1 <b>agranda</b> el resultado."),
  E("La botella","Una botella tiene 3/4 litro. ¿Cuántos vasos de 1/8 litro se llenan?",["3/4 ÷ 1/8 = 3/4 × 8/1 = 24/4.","24/4 = 6.","Se llenan 6 vasos."]),
 ]),
 S(2,"Con enteros y mixtos",[
  P("Los mixtos se pasan a impropias y los enteros se escriben con denominador 1. Ejemplos: 2 1/2 ÷ 5/4 = 5/2 × 4/5 = 20/10 = 2. Y 6/7 ÷ 3 = 6/7 × 1/3 = 6/21 = 2/7."),
 ]),
],
"ejemplo_completo":{"titulo":"1 1/3 ÷ 2/9","planteo":"Calculá 1 1/3 ÷ 2/9 y comprobá.","pasos":["1 1/3 = 4/3.","4/3 ÷ 2/9 = 4/3 × 9/2.","Simplificamos: 4 y 2 por 2 (2 y 1); 9 y 3 por 3 (3 y 1). Queda 2 × 3 = 6.","Comprobación: 6 × 2/9 = 12/9 = 4/3."]},
"ejemplo_incompleto":{"titulo":"5/6 ÷ 5/12","planteo":"Completá los espacios.","pasos":["El inverso de 5/12 es ___ .","5/6 × 12/5 = ___ /30.","Simplificado: ___ ."]},
"ejemplo_solo":{"titulo":"los frascos","planteo":"¿Cuántos frascos de 3/8 kg se llenan con 6 kg de dulce?"},
"tip":{"titulo":"Solo se da vuelta la segunda","texto":"La primera fracción queda igual; la que divide se invierte, y después se multiplica."},
"ojo":["Invertir la fracción equivocada: en 4/5 ÷ 2/3 se invierte el 2/3, no el 4/5.","Creer que dividir siempre achica: 3 ÷ 1/4 = 12."],
"resumen":[{"titulo":"Inverso","texto":"Se da vuelta: 3/4 → 4/3."},{"titulo":"Dividir","texto":"Multiplicar por el inverso. Ej.: 3/4 ÷ 2/5 = 15/8."},{"titulo":"Cuántas veces entra","texto":"3 ÷ 1/4 = 12."},{"titulo":"Mixtos","texto":"Se pasan a impropias."}],
"glosario":[{"palabra":"Inverso","significado":"La fracción dada vuelta; multiplicada por la original da 1."},{"palabra":"Divisor","significado":"El número por el que se divide."},{"palabra":"Reparto","significado":"Partir una cantidad en partes iguales."}],
"carpeta":["¿Cuál es el inverso de 7/3?","Calculá 2/3 ÷ 1/6.","¿Cuántos vasos de 1/4 litro se llenan con 5 litros?","Un compañero hizo 4/5 ÷ 2/3 invirtiendo la primera fracción. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["3/7"],["4"],["20"],["6/5","12/10"]],
"soluciones":{"incompleto":"12/5. 60/30. Simplificado: 2.","solo":"6 ÷ 3/8 = 6 × 8/3 = 48/3 = 16 frascos.","carpeta":["3/7: se da vuelta.","4: 2/3 × 6 = 12/3 = 4.","20: 5 ÷ 1/4 = 5 × 4.","6/5: 4/5 × 3/2 = 12/10 = 6/5. Se invierte la segunda."]}
}
N4={
"objetivo":"Vas a poder resolver cálculos combinados con fracciones respetando la jerarquía, con paréntesis y potencias, y resolver problemas de varios pasos.",
"vas_a_ver":["La jerarquía con fracciones","Paréntesis y fracciones","Potencias de fracciones","Problemas de varios pasos"],
"secciones":[
 S(1,"Jerarquía con fracciones",[
  D("Mismo orden de siempre","Con fracciones se respeta la misma jerarquía: <b>paréntesis</b>, después <b>potencias</b>, después <b>× y ÷</b>, y al final <b>+ y −</b>."),
  T("Con y sin paréntesis",["Cálculo","Se resuelve","Resultado"],[["1/2 + 1/3 × 3/4","1/2 + 1/4","3/4"],["(1/2 + 1/3) × 3/4","5/6 × 3/4","5/8"]]),
 ]),
 S(1,"Potencias de fracciones",[
  D("Potencia de una fracción","Se eleva el <b>numerador y el denominador</b>: (2/3)² = 2²/3² = 4/9."),
  P("Ejemplo: (1/2)³ = 1/8. Ojo: 2/3² no es lo mismo que (2/3)²; sin paréntesis, la potencia es solo del 3."),
 ]),
 S(2,"Cuidado al simplificar",[
  P("Solo se simplifica dentro de una fracción o entre factores de una multiplicación. <b>No se simplifica entre sumandos</b>: en 3/4 + 4/9 no se puede tachar el 4 de arriba con el de abajo."),
 ]),
 S(2,"Problemas de varios pasos",[
  E("El dinero de Juan","Juan gastó 1/3 de su dinero en libros y 1/4 de lo que le quedó en comida.",["Después de los libros le queda 1 − 1/3 = 2/3.","Comida: 1/4 de 2/3 = 1/4 × 2/3 = 2/12 = 1/6.","Le queda 1 − 1/3 − 1/6 = 6/6 − 2/6 − 1/6 = 3/6 = 1/2."]),
 ]),
],
"ejemplo_completo":{"titulo":"(3/4 − 1/2)² + 2/3 ÷ 4","planteo":"Resolvé con una igualdad por línea.","pasos":["Paréntesis: 3/4 − 1/2 = 1/4. Queda (1/4)² + 2/3 ÷ 4.","Potencia: 1/16. División: 2/3 × 1/4 = 2/12 = 1/6.","1/16 + 1/6: MCM 48. 3/48 + 8/48.","Resultado: 11/48."]},
"ejemplo_incompleto":{"titulo":"2/5 + 3/5 × 1/3","planteo":"Completá los espacios.","pasos":["Primero la multiplicación: 3/5 × 1/3 = ___ .","Después la suma: 2/5 + 1/5 = ___ ."]},
"ejemplo_solo":{"titulo":"(1/2)² + 3/4 × 2/3","planteo":"Resolvé respetando la jerarquía."},
"tip":{"titulo":"Estimá con referentes","texto":"Antes de terminar, mirá si el resultado tiene sentido: si sumás algo cercano a 1/2 con algo cercano a 1/4, el resultado tiene que estar cerca de 3/4."},
"ojo":["Resolver de izquierda a derecha: 1/4 + 1/4 × 2 no es 1; es 1/4 + 1/2 = 3/4.","Simplificar entre sumandos: no se tacha un número de una fracción con otro de otra fracción que se suma."],
"resumen":[{"titulo":"Jerarquía","texto":"Paréntesis, potencias, × y ÷, + y −."},{"titulo":"Potencia","texto":"(2/3)² = 4/9."},{"titulo":"Simplificar","texto":"Solo entre factores, nunca entre sumandos."},{"titulo":"Problemas","texto":"\"De lo que quedó\": primero lo que queda, después la fracción."}],
"glosario":[{"palabra":"Jerarquía","significado":"Orden en que se resuelven las operaciones."},{"palabra":"Sumando","significado":"Cada número que se suma."},{"palabra":"Factor","significado":"Cada número que se multiplica."}],
"carpeta":["Calculá (1/3)².","Calculá 1/2 + 1/2 × 1/2.","Calculá (1/2 + 1/4) × 4.","Un compañero resolvió 1/4 + 1/4 × 2 de izquierda a derecha y le dio 1. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["1/9"],["3/4"],["3"],["3/4"]],
"soluciones":{"incompleto":"3/15 = 1/5. 3/5.","solo":"1/4 + 1/2 = 1/4 + 2/4 = 3/4.","carpeta":["1/9: 1²/3².","3/4: 1/2 + 1/4.","3: 3/4 × 4 = 3.","3/4: primero 1/4 × 2 = 1/2; después 1/4 + 1/2 = 3/4."]}
}
ACT={
"1":[MC("¿Cuánto da 2/5 + 1/3?",["3/8","11/15","3/15","2/15"],"11/15","6/15 + 5/15 = 11/15."),
     {"t":"tap_text","p":"Detective del error: tocá el resultado que está mal y escribí el correcto.","o":{"modo":"palabras","segmentos":["1/3 + 1/4","=","2/7"],"pide_correccion":"Escribí el resultado correcto"},"r":{"tocar":[2],"correccion":["7/12"]},"e":"Sumó numeradores y denominadores. 4/12 + 3/12 = 7/12."}],
"2":[MC("¿Cuánto da 3/4 × 2/9?",["1/6","5/13","27/8","5/36"],"1/6","6/36 = 1/6. Simplificando antes: 3 con 9 y 2 con 4."),
     N("Calculá 6 × 5/3.",{"acepta":[10]},"6/1 × 5/3 = 30/3 = 10.")],
"3":[MC("¿Cuál es el inverso de 5/8?",["5/8","8/5","1/8","5/1"],"8/5","Se da vuelta la fracción: 5/8 × 8/5 = 1."),
     N("¿Cuántas botellas de 1/2 litro se llenan con {n} litros?",{"formula":"n*2"},"n ÷ 1/2 = n × 2.",{"vars":{"n":{"min":2,"max":20}}})],
"4":[MC("¿Cuánto da 1/3 + 2/3 × 1/2?",["2/3","1/2","5/6","1/6"],"2/3","Primero 2/3 × 1/2 = 1/3; después 1/3 + 1/3 = 2/3."),
     MC("¿Cuánto es (2/3) elevado a 2?",["4/6","4/9","2/9","4/3"],"4/9","Se elevan numerador y denominador.")],
"5":[MC("Relámpago. 3/8 + 2/8 =",["5/8","5/16","6/8","1/8"],"5/8","Mismo denominador: se suman los numeradores.",tiempo=20),
     MC("Relámpago. 1/2 × 1/2 =",["1","1/4","2/4","1/2"],"1/4","1 × 1 = 1 y 2 × 2 = 4.",tiempo=20),
     VF("Relámpago. Dividir por 1/2 es lo mismo que multiplicar por 2.","Verdadero","El inverso de 1/2 es 2.",tiempo=20),
     MC("Relámpago. ¿Cuál es mayor?",["3/5","2/3"],"2/3","9/15 < 10/15 (repaso de la misión 8).",tiempo=30)],
}
EXAMEN=[
 [1,MC("¿Cuánto da 5/6 − 1/4?",["4/2","7/12","1/2","4/24"],"7/12","10/12 − 3/12 = 7/12.")],
 [1,N("Calculá 1/2 + 3/4 + 1/4. Podés escribir el resultado como fracción.",{"acepta":[1.5]},"3/4 + 1/4 = 1, y 1/2 + 1 = 3/2.")],
 [1,VF("Para sumar 1/3 + 1/5 se suman numeradores y denominadores: 2/8.","Falso","5/15 + 3/15 = 8/15.")],
 [2,MC("¿Cuánto da 4/5 × 10/12?",["2/3","14/17","40/12","1/3"],"2/3","40/60 = 2/3.")],
 [2,N("¿Cuánto es 3/4 de 1/2 de 80?",{"acepta":[30]},"1/2 de 80 es 40, y 3/4 de 40 es 30.")],
 [2,MC("Al multiplicar 12 por 2/3, el resultado es…",["Mayor que 12","Menor que 12","Igual a 12"],"Menor que 12","Multiplicar por una fracción menor que 1 achica: da 8.")],
 [3,MC("¿Cuánto da 3/5 ÷ 9/10?",["2/3","27/50","1/3","3/2"],"2/3","3/5 × 10/9 = 30/45 = 2/3.")],
 [3,N("¿Cuántos paquetes de 3/4 kg se arman con 9 kg?",{"acepta":[12]},"9 ÷ 3/4 = 9 × 4/3 = 12.")],
 [3,VF("Dividir por una fracción siempre achica el resultado.","Falso","Dividir por una fracción menor que 1 agranda: 3 ÷ 1/4 = 12.")],
 [4,N("Calculá (1/2 + 1/3) × 6.",{"acepta":[5]},"5/6 × 6 = 5.")],
 [4,MC("¿Cuánto da 1/2 + 1/4 × 2?",["1","3/2","3/4","1/4"],"1","Primero 1/4 × 2 = 1/2; después 1/2 + 1/2 = 1.")],
 [4,N("Pedro tenía $8.000. Gastó 1/4 en un libro y la mitad de lo que le quedó en ropa. ¿Cuánto dinero le queda?",{"acepta":[3000]},"Libro: 2.000; le quedan 6.000. Ropa: 3.000. Le quedan 3.000.")],
 [4,MC("¿Cuánto es (1/2) elevado a 3?",["3/2","1/6","1/8","3/8"],"1/8","1/2 × 1/2 × 1/2 = 1/8.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":9,"practica":"Práctica general: operaciones con fracciones","examen_titulo":"Nivel jefe: operaciones con fracciones",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-9.json"),"w"),ensure_ascii=False)
print("ok")
