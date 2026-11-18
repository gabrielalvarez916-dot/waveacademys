# -*- coding: utf-8 -*-
"""Matemática I · Misión 6 · Criterios de divisibilidad y números primos. Genera mision-6.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
SI=["si","sí"]
N1={
"objetivo":"Vas a poder decidir si un número es divisible por 2, 3, 5, 9 o 10 sin hacer la división, y explicar por qué funcionan esos criterios.",
"vas_a_ver":["Criterios por 2, 5 y 10: la última cifra","Criterios por 3 y 9: la suma de las cifras","Por qué funcionan","Cómo usarlos en números grandes"],
"secciones":[
 S(1,"Por 2, 5 y 10: la última cifra",[
  D("Criterios por 2, 5 y 10","Un número es divisible <b>por 2</b> si termina en 0, 2, 4, 6 u 8; <b>por 5</b> si termina en 0 o 5; <b>por 10</b> si termina en 0."),
  T("Mirando la última cifra",["Número","Por 2","Por 5","Por 10"],[["340","Sí","Sí","Sí"],["725","No","Sí","No"],["618","Sí","No","No"]]),
 ]),
 S(1,"Por 3 y 9: la suma de las cifras",[
  D("Criterios por 3 y 9","Un número es divisible <b>por 3</b> si la suma de sus cifras es múltiplo de 3, y <b>por 9</b> si la suma de sus cifras es múltiplo de 9."),
  P("Ejemplo: 2.457 → 2 + 4 + 5 + 7 = 18. Como 18 es múltiplo de 9 (y de 3), 2.457 es divisible por 9 y por 3: 2.457 = 9 × 273."),
 ]),
 S(2,"Por qué funcionan",[
  P("<b>Última cifra:</b> todo número es \"decenas × 10 + última cifra\". Como 10 es múltiplo de 2 y de 5, la parte de las decenas siempre se divide; solo decide la última cifra (es la propiedad de la suma de la misión anterior)."),
  P("<b>Suma de cifras:</b> 10 = 9 + 1, 100 = 99 + 1, 1.000 = 999 + 1. Entonces 2.457 = 2 × 999 + 4 × 99 + 5 × 9 + (2 + 4 + 5 + 7). Lo primero siempre es múltiplo de 9; lo que decide es la suma de las cifras. Por eso el resto de dividir por 9 es el mismo que el de la suma de cifras."),
 ]),
 S(2,"Números grandes",[
  E("Un número de nueve cifras","¿123.456.789 es divisible por 2, 5, 3 o 9?",["Termina en 9: no es divisible por 2, ni por 5, ni por 10.","Suma de cifras: 1 + 2 + … + 9 = 45.","45 es múltiplo de 9: es divisible por 9 y por 3."]),
 ]),
],
"ejemplo_completo":{"titulo":"7.320","planteo":"¿Por cuáles de 2, 3, 5, 9 y 10 es divisible 7.320?","pasos":["Termina en 0: es divisible por 2, por 5 y por 10.","Suma de cifras: 7 + 3 + 2 + 0 = 12.","12 es múltiplo de 3 pero no de 9.","7.320 es divisible por 2, 3, 5 y 10, pero no por 9."]},
"ejemplo_incompleto":{"titulo":"4.185","planteo":"Completá los espacios.","pasos":["Termina en 5: es divisible por ___ y no por 2.","Suma de cifras: 4 + 1 + 8 + 5 = ___ .","Es divisible por 3 y por ___ ."]},
"ejemplo_solo":{"titulo":"5.346","planteo":"¿Por cuáles de 2, 3, 5, 9 y 10 es divisible 5.346?"},
"tip":{"titulo":"Sumá de nuevo si es grande","texto":"Si la suma de cifras te da un número grande, sumá sus cifras otra vez: 45 → 4 + 5 = 9."},
"ojo":["Confundir 3 y 9: todo múltiplo de 9 es múltiplo de 3, pero no al revés. 12 es múltiplo de 3 y no de 9.","Creer que terminar en 5 alcanza para el 10: 345 es divisible por 5, pero no por 10."],
"resumen":[{"titulo":"Por 2","texto":"Termina en cifra par."},{"titulo":"Por 5 y por 10","texto":"Termina en 0 o 5; en 0."},{"titulo":"Por 3 y por 9","texto":"La suma de cifras es múltiplo de 3; de 9."},{"titulo":"Por qué","texto":"10, 100, 1.000 son 9 + 1, 99 + 1, 999 + 1."}],
"glosario":[{"palabra":"Criterio","significado":"Regla rápida para saber algo sin hacer la cuenta."},{"palabra":"Divisible","significado":"Que se divide en forma exacta."},{"palabra":"Cifra","significado":"Cada uno de los símbolos de un número."},{"palabra":"Suma de cifras","significado":"Lo que da sumar todas las cifras de un número."}],
"carpeta":["¿Cuánto da la suma de las cifras de 8.172?","¿8.172 es divisible por 9? Respondé sí o no.","¿Qué cifra hay que poner en el lugar vacío de 4 _ 6 para que el número sea divisible por 9?","Un compañero dice que 345 es divisible por 10 porque termina en 5. ¿Cuál es el resto de dividir 345 por 10?"],
"respuestas_carpeta":[["18"],SI,["8"],["5"]],
"soluciones":{"incompleto":"Por 5. Suma 18. Por 9.","solo":"Termina en 6: por 2 sí; por 5 y 10 no. Suma 18: por 3 y por 9 sí. Es divisible por 2, 3 y 9.","carpeta":["18: 8 + 1 + 7 + 2.","Sí: la suma es 18, múltiplo de 9 (8.172 = 9 × 908).","8: 4 + 8 + 6 = 18. Con otra cifra no se llega a 9 ni a 27.","5: 345 = 10 × 34 + 5. Para el 10 tiene que terminar en 0."]}
}
N2={
"objetivo":"Vas a poder usar los criterios por 4, 6, 8, 10 y 11, y combinar criterios para decidir si un número es divisible.",
"vas_a_ver":["Criterios por 4 y por 8: las últimas cifras","Criterio por 6: el 2 y el 3 juntos","Criterio por 11: las sumas alternadas","Combinar criterios"],
"secciones":[
 S(1,"Por 4 y por 8",[
  D("Criterios por 4 y por 8","Un número es divisible <b>por 4</b> si sus <b>dos últimas cifras</b> forman un múltiplo de 4, y <b>por 8</b> si sus <b>tres últimas cifras</b> forman un múltiplo de 8."),
  P("Funciona porque 100 es múltiplo de 4 y 1.000 es múltiplo de 8: lo de adelante siempre se divide. Ejemplos: 3.716 → 16 = 4 × 4, es divisible por 4. 5.240 → 240 = 8 × 30, es divisible por 8."),
 ]),
 S(1,"Por 6 y por 10",[
  D("Criterio por 6","Un número es divisible <b>por 6</b> si es divisible <b>por 2 y por 3 a la vez</b>."),
  P("234 es par y su suma de cifras es 9: es divisible por 6 (234 = 6 × 39). 410 es par, pero su suma es 5: no es divisible por 6. Recordá que por 10 alcanza con terminar en 0."),
 ]),
 S(2,"Por 11: sumas alternadas",[
  P("Sumá las cifras en los lugares impares contando desde la derecha (1.ª, 3.ª…) y, aparte, las de los lugares pares (2.ª, 4.ª…). Si la diferencia entre las dos sumas (mayor menos menor) es 0 o un múltiplo de 11, el número es divisible <b>por 11</b>."),
  E("Probar con 2.728 y 5.137","Sumas alternadas desde la derecha.",["2.728: cifras 8, 2, 7, 2. Sumas: 8 + 7 = 15 y 2 + 2 = 4. Diferencia 11: es divisible (2.728 = 11 × 248).","5.137: cifras 7, 3, 1, 5. Sumas: 7 + 1 = 8 y 3 + 5 = 8. Diferencia 0: es divisible (5.137 = 11 × 467)."]),
 ]),
 S(2,"Combinar criterios",[
  P("Para 15 alcanza con 3 y 5; para 6, con 2 y 3. Pero ojo: para 12 hay que usar <b>3 y 4</b>, no 2 y 6. Por ejemplo, 18 es divisible por 2 y por 6, y no por 12."),
 ]),
],
"ejemplo_completo":{"titulo":"7.392","planteo":"¿Por cuáles de 2, 3, 4, 6, 8, 9 y 11 es divisible 7.392?","pasos":["Es par: por 2 sí. Suma de cifras 21: por 3 sí, por 9 no. Entonces por 6 sí.","Dos últimas cifras 92 = 4 × 23: por 4 sí. Tres últimas 392 = 8 × 49: por 8 sí.","Por 11: cifras desde la derecha 2, 9, 3, 7. Sumas 2 + 3 = 5 y 9 + 7 = 16. Diferencia 11: sí.","Es divisible por 2, 3, 4, 6, 8 y 11; no por 9."]},
"ejemplo_incompleto":{"titulo":"1.452","planteo":"Completá los espacios.","pasos":["Dos últimas cifras: ___ = 4 × 13. Es divisible por 4.","Por 11: sumas 2 + 4 = 6 y 5 + 1 = ___ .","Diferencia ___ : es divisible por 11."]},
"ejemplo_solo":{"titulo":"3.528","planteo":"¿Es 3.528 divisible por 6? ¿Y por 8?"},
"tip":{"titulo":"Para 6, los dos criterios","texto":"Que sea par no alcanza: fijate también la suma de cifras."},
"ojo":["Usar solo el 2 para el 6: 1.034 es par, pero su suma de cifras es 8; no es divisible por 6.","Mirar una sola cifra para el 4: en 3.716 hay que mirar 16, no solo el 6."],
"resumen":[{"titulo":"Por 4","texto":"Dos últimas cifras. Ej.: 3.716 → 16."},{"titulo":"Por 8","texto":"Tres últimas cifras. Ej.: 5.240 → 240."},{"titulo":"Por 6","texto":"Por 2 y por 3 a la vez."},{"titulo":"Por 11","texto":"Diferencia de sumas alternadas: 0 o múltiplo de 11."},{"titulo":"Combinar","texto":"Para 12: 3 y 4, no 2 y 6."}],
"glosario":[{"palabra":"Alternadas","significado":"Una sí y una no, salteando."},{"palabra":"Diferencia","significado":"El resultado de restar."},{"palabra":"Combinar","significado":"Usar dos criterios juntos."}],
"carpeta":["¿Cuál de estos números es divisible por 4: 314, 516 o 722?","¿Cuánto da la diferencia entre las sumas alternadas de 8.371 (mayor menos menor)?","Escribí el menor número de tres cifras divisible por 6.","Un compañero dice que 1.034 es divisible por 6 porque es par. ¿Cuánto da la suma de sus cifras?"],
"respuestas_carpeta":[["516"],["11"],["102"],["8"]],
"soluciones":{"incompleto":"52. 6. Diferencia 0.","solo":"Por 6: es par y su suma es 18, sí. Por 8: 528 = 8 × 66, sí.","carpeta":["516: 16 es múltiplo de 4; 14 y 22 no.","11: cifras desde la derecha 1, 7, 3, 8. Sumas 1 + 3 = 4 y 7 + 8 = 15. Es divisible por 11.","102: es par y su suma es 3.","8: 1 + 0 + 3 + 4 = 8, que no es múltiplo de 3. No es divisible por 6."]}
}
N3={
"objetivo":"Vas a poder clasificar números en primos y compuestos, encontrar primos con la criba de Eratóstenes y decidir si un número es primo.",
"vas_a_ver":["Qué es un número primo y uno compuesto","Por qué el 1 no es ninguno de los dos","La criba de Eratóstenes","Cómo saber si un número es primo","Primos gemelos"],
"secciones":[
 S(1,"Primos y compuestos",[
  D("Número primo","Un número es <b>primo</b> si tiene <b>exactamente dos divisores</b>: el 1 y él mismo. Es <b>compuesto</b> si tiene más de dos divisores."),
  T("Clasificar",["Número","Divisores","Es"],[["1","1","Ni primo ni compuesto"],["2","1 y 2","Primo"],["9","1, 3 y 9","Compuesto"],["13","1 y 13","Primo"]],"El 1 tiene un solo divisor. El 2 es el único primo par."),
 ]),
 S(1,"La criba de Eratóstenes",[
  D("Criba de Eratóstenes","Es un método para encontrar los primos: escribís los números desde el 2, y vas <b>tachando los múltiplos</b> de cada primo (sin tachar el primo). Los que quedan sin tachar son primos."),
  P("Hasta 50 alcanza con tachar múltiplos de 2, 3, 5 y 7, porque 7 × 7 = 49 y el siguiente primo, 11, ya da 121. Quedan: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43 y 47."),
 ]),
 S(2,"¿Es primo?",[
  P("Para saber si un número es primo, probá dividirlo por los primos 2, 3, 5, 7, 11… Si ninguno lo divide, y ya probaste hasta el primo cuyo cuadrado supera al número, es primo. Usá los criterios para ir rápido."),
  E("91 y 97","Probamos con primos chicos.",["91: no por 2, ni por 3 (suma 10), ni por 5. Por 7: 91 = 7 × 13. Es compuesto.","97: no por 2, 3, 5 ni 7. Como 11 × 11 = 121 es mayor que 97, ya no hace falta seguir. Es primo."]),
 ]),
 S(2,"Primos gemelos",[
  P("Son pares de primos que se diferencian en 2: (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)."),
 ]),
],
"ejemplo_completo":{"titulo":"¿es primo 113?","planteo":"Decidí si 113 es primo.","pasos":["Por 2 no: es impar. Por 3 no: la suma es 5. Por 5 no: termina en 3.","Por 7: 7 × 16 = 112 y sobra 1. No.","11 × 11 = 121 es mayor que 113: no hace falta seguir.","113 es primo."]},
"ejemplo_incompleto":{"titulo":"¿es primo 87?","planteo":"Completá los espacios.","pasos":["Suma de cifras: 8 + 7 = ___ .","Es divisible por ___ .","87 = 3 × ___ . Es compuesto."]},
"ejemplo_solo":{"titulo":"¿es primo 101?","planteo":"Decidí si 101 es primo y justificá."},
"tip":{"titulo":"Pará a tiempo","texto":"No hace falta probar todos los números: cuando el cuadrado del primo que vas a probar supera al número, podés parar."},
"ojo":["Pensar que el 1 es primo: tiene un solo divisor.","Creer que todos los impares son primos: 9, 15 y 21 son impares y compuestos."],
"resumen":[{"titulo":"Primo","texto":"Exactamente dos divisores. Ej.: 13."},{"titulo":"Compuesto","texto":"Más de dos divisores. Ej.: 9."},{"titulo":"El 1 y el 2","texto":"1 no es ninguno; 2 es el único primo par."},{"titulo":"Criba","texto":"Se tachan múltiplos; quedan los primos."},{"titulo":"¿Es primo?","texto":"Dividir por primos hasta que el cuadrado supere."}],
"glosario":[{"palabra":"Primo","significado":"Número con exactamente dos divisores."},{"palabra":"Compuesto","significado":"Número con más de dos divisores."},{"palabra":"Criba","significado":"Método para separar los primos tachando múltiplos."},{"palabra":"Gemelos","significado":"Dos primos que se diferencian en 2."}],
"carpeta":["¿Cuántos números primos hay entre 1 y 20?","¿Cuál es el único número primo par?","¿Cuál es el menor número compuesto impar?","Un compañero dice que 51 es primo porque es impar. Si 51 = 3 × ___, ¿qué número va en el espacio?"],
"respuestas_carpeta":[["8"],["2"],["9"],["17"]],
"soluciones":{"incompleto":"15. Por 3. 87 = 3 × 29.","solo":"No es divisible por 2, ni por 3 (suma 2), ni por 5, ni por 7 (7 × 14 = 98, sobran 3). 11 × 11 = 121 supera a 101. Es primo.","carpeta":["8: 2, 3, 5, 7, 11, 13, 17 y 19.","2: los demás pares son divisibles por 2.","9: tiene los divisores 1, 3 y 9.","17: 51 = 3 × 17. Es compuesto."]}
}
N4={
"objetivo":"Vas a poder descomponer un número en factores primos, escribirlo con potencias y usar esa descomposición para encontrar sus divisores.",
"vas_a_ver":["Qué es descomponer en factores primos","Cómo hacerlo dividiendo por primos","Escribir la descomposición con potencias","La descomposición es única","Contar y encontrar los divisores"],
"secciones":[
 S(1,"Descomponer en factores primos",[
  D("Descomposición en factores primos","Es escribir un número como una <b>multiplicación de números primos</b>. Se divide por el menor primo posible, después el cociente otra vez, hasta llegar a 1."),
  T("Descomponer 60",["Número","Se divide por"],[["60","2"],["30","2"],["15","3"],["5","5"],["1",""]],"Los primos de la derecha son los factores: 60 = 2 × 2 × 3 × 5."),
 ]),
 S(1,"Con potencias",[
  D("Escritura con potencias","Los factores que se repiten se escriben como potencia: 60 = 2² × 3 × 5."),
  P("Ejemplo: 72 = 2 × 2 × 2 × 3 × 3 = 2³ × 3². Y 36 = 2² × 3²."),
 ]),
 S(2,"Siempre la misma",[
  P("Empieces por donde empieces, la descomposición en primos de un número es <b>siempre la misma</b>. 72 = 8 × 9 = 2³ × 3², y 72 = 6 × 12 = (2 × 3) × (2 × 2 × 3) = 2³ × 3²."),
 ]),
 S(2,"Divisores desde la descomposición",[
  P("Cada divisor se arma eligiendo una potencia de cada primo, con exponente desde 0 hasta el que tiene. Para contarlos, se suma 1 a cada exponente y se multiplica."),
  E("Divisores de 12 = 2² × 3","Combinamos potencias.",["Potencias de 2: 1, 2, 4. Potencias de 3: 1, 3.","Divisores: 1, 2, 4, 3, 6, 12.","Cantidad: (2 + 1) × (1 + 1) = 6."]),
 ]),
],
"ejemplo_completo":{"titulo":"180","planteo":"Descomponé 180 en factores primos y calculá cuántos divisores tiene.","pasos":["180 ÷ 2 = 90; 90 ÷ 2 = 45.","45 ÷ 3 = 15; 15 ÷ 3 = 5; 5 ÷ 5 = 1.","180 = 2² × 3² × 5.","Cantidad de divisores: (2 + 1) × (2 + 1) × (1 + 1) = 18."]},
"ejemplo_incompleto":{"titulo":"84","planteo":"Descomponé 84. Completá los espacios.","pasos":["84 ÷ 2 = ___ .","42 ÷ 2 = 21.","21 ÷ 3 = ___ .","84 = 2² × 3 × ___ ."]},
"ejemplo_solo":{"titulo":"150","planteo":"Descomponé 150 en factores primos y escribilo con potencias."},
"tip":{"titulo":"Usá los criterios","texto":"Para saber por qué primo dividir, usá los criterios de divisibilidad: par → 2; suma de cifras múltiplo de 3 → 3; termina en 0 o 5 → 5."},
"ojo":["Dejar un factor compuesto: 90 = 2 × 9 × 5 no está terminado, porque 9 = 3 × 3.","Olvidar factores repetidos: 72 = 2³ × 3², no 2 × 3."],
"resumen":[{"titulo":"Descomponer","texto":"Escribir como producto de primos. Ej.: 60 = 2 × 2 × 3 × 5."},{"titulo":"Potencias","texto":"60 = 2² × 3 × 5."},{"titulo":"Única","texto":"Siempre se llega a la misma."},{"titulo":"Divisores","texto":"Sumar 1 a cada exponente y multiplicar. Ej.: 12 → 6."}],
"glosario":[{"palabra":"Factor","significado":"Cada número de una multiplicación."},{"palabra":"Factor primo","significado":"Factor que es un número primo."},{"palabra":"Descomponer","significado":"Escribir un número como producto de otros."},{"palabra":"Única","significado":"Que hay una sola."}],
"carpeta":["Si 48 = 2ᵃ × 3, ¿cuánto vale a?","¿Qué número es 2³ × 5²?","¿Cuántos divisores tiene 2³ × 3?","Un compañero escribió 90 = 2 × 9 × 5 y dijo que terminó. ¿Qué factor no es primo?"],
"respuestas_carpeta":[["4"],["200"],["8"],["9"]],
"soluciones":{"incompleto":"42. 7. 84 = 2² × 3 × 7.","solo":"150 ÷ 2 = 75; 75 ÷ 3 = 25; 25 ÷ 5 = 5; 5 ÷ 5 = 1. 150 = 2 × 3 × 5².","carpeta":["4: 48 = 16 × 3 = 2⁴ × 3.","200: 8 × 25.","8: (3 + 1) × (1 + 1).","9: 9 = 3 × 3. La descomposición es 90 = 2 × 3² × 5."]}
}
ACT={
"1":[{"t":"multi_select","p":"¿Por cuáles de estos números es divisible 1.785?","o":["2","3","5","9","10"],"r":{"correctas":["3","5"]},"e":"Es impar; suma de cifras 21 (múltiplo de 3, no de 9); termina en 5."},
     N("¿Qué cifra va en el lugar vacío de 5 _ 1 para que el número sea divisible por 9?",{"acepta":[3]},"5 + 3 + 1 = 9.")],
"2":[VF("Un número divisible por 2 y por 4 es siempre divisible por 8.","Falso","4 es divisible por 2 y por 4, pero no por 8."),
     N("¿Cuánto da la diferencia entre las sumas alternadas de 6.193 (mayor menos menor)?",{"acepta":[11]},"Cifras desde la derecha 3, 9, 1, 6: 3 + 1 = 4 y 9 + 6 = 15. Diferencia 11: es divisible por 11.")],
"3":[{"t":"multi_select","p":"¿Cuáles de estos números son primos?","o":["1","2","9","17","21","23"],"r":{"correctas":["2","17","23"]},"e":"1 no es primo; 9 = 3 × 3 y 21 = 3 × 7 son compuestos."},
     MC("¿Por qué el 1 no es primo?",["Porque es impar","Porque tiene un solo divisor","Porque es muy chico","Porque divide a todos"],"Porque tiene un solo divisor","Un primo tiene exactamente dos divisores.")],
"4":[{"t":"fill_blank","p":"60 = 2 elevado a ___ × 3 × 5.","o":[],"r":{"huecos":[["2"]]},"e":"60 = 2 × 2 × 3 × 5."},
     N("¿Cuántos divisores tiene 2 elevado a 2 × 3 elevado a 2?",{"acepta":[9]},"(2 + 1) × (2 + 1) = 9. Es el 36.")],
"5":[VF("Relámpago. El 2 es un número primo.","Verdadero","Sus únicos divisores son 1 y 2.",tiempo=15),
     N("Relámpago. ¿Cuánto da la suma de las cifras de 4.572?",{"acepta":[18]},"4 + 5 + 7 + 2 = 18.",tiempo=30),
     MC("Relámpago. ¿4.572 es divisible por 9?",["Sí","No"],"Sí","La suma de sus cifras es 18, múltiplo de 9.",tiempo=20),
     N("Relámpago. ¿Cuántos divisores tiene 30?",{"acepta":[8]},"1, 2, 3, 5, 6, 10, 15 y 30 (repaso de la misión 5).",tiempo=40)],
}
EXAMEN=[
 [1,MC("¿Cuál de estos números es divisible por 3 pero no por 9?",["135","243","312","729"],"312","312 suma 6; los otros suman 9 o 18.")],
 [1,VF("Todo número que termina en 5 es divisible por 10.","Falso","Para el 10 tiene que terminar en 0. Por ejemplo, 15 no es divisible por 10.")],
 [1,N("¿Cuál es el resto de dividir 2.461 por 9? Usá la suma de las cifras.",{"acepta":[4]},"2 + 4 + 6 + 1 = 13, y 13 ÷ 9 da resto 4. 2.461 = 9 × 273 + 4.")],
 [2,MC("¿Cuál de estos números es divisible por 4?",["1.322","2.514","3.736","4.810"],"3.736","Sus dos últimas cifras, 36, son múltiplo de 4.")],
 [2,N("Para que un número sea divisible por 6, ¿por qué otro número de una cifra, además del 2, tiene que ser divisible?",{"acepta":[3]},"6 = 2 × 3: tiene que ser divisible por 2 y por 3.")],
 [2,VF("4.334 es divisible por 11.","Verdadero","Sumas alternadas: 4 + 3 = 7 y 3 + 4 = 7. Diferencia 0.")],
 [3,N("¿Cuántos números primos hay entre 20 y 40?",{"acepta":[4]},"23, 29, 31 y 37.")],
 [3,MC("¿Cuál de estos números es compuesto?",["29","31","51","53"],"51","51 = 3 × 17.")],
 [3,{"t":"classify","p":"Clasificá cada número.","o":{"elementos":["1","2","15","19","27","41"],"categorias":["Primo","Compuesto","Ni primo ni compuesto"]},"r":{"categorias":{"1":"Ni primo ni compuesto","2":"Primo","15":"Compuesto","19":"Primo","27":"Compuesto","41":"Primo"}},"e":"15 = 3 × 5 y 27 = 3 × 9. El 1 tiene un solo divisor."}],
 [4,N("¿Qué número es 2 elevado a 2 × 3 × 7?",{"acepta":[84]},"4 × 3 × 7 = 84.")],
 [4,{"t":"fill_blank","p":"100 = 2 elevado a ___ × 5 elevado a ___.","o":[],"r":{"huecos":[["2"],["2"]]},"e":"100 = 4 × 25 = 2 × 2 × 5 × 5."}],
 [4,N("¿Cuántos divisores tiene 2 elevado a 4 × 5?",{"acepta":[10]},"(4 + 1) × (1 + 1) = 10.")],
 [4,MC("¿Cuál es la descomposición en factores primos de 36?",["4 × 9","2 elevado a 2 × 3 elevado a 2","6 elevado a 2","2 × 18"],"2 elevado a 2 × 3 elevado a 2","Solo esa tiene todos los factores primos: 4, 9, 6 y 18 son compuestos.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":6,"practica":"Práctica general: criterios de divisibilidad y números primos","examen_titulo":"Nivel jefe: criterios de divisibilidad y números primos",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-6.json"),"w"),ensure_ascii=False)
print("ok")
