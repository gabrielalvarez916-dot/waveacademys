# -*- coding: utf-8 -*-
"""Matemática I · Misión 1 · Sistemas de numeración (rehecha a partir del video). Genera mision-1.json."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
N1={
"objetivo":"Vas a poder explicar por qué nuestro sistema es decimal y posicional, leer y escribir números grandes y descomponerlos de forma aditiva y multiplicativa.",
"vas_a_ver":["Las 10 cifras y la base 10","Agrupar de a 10: unidades, decenas, centenas","El valor posicional: la misma cifra vale distinto según su lugar","Leer y escribir números de hasta 12 cifras","Descomposición aditiva y multiplicativa"],
"secciones":[
 S(1,"Un sistema de base 10",[
  D("Sistema decimal","Usamos <b>10 cifras</b> (0, 1, 2, …, 9) para escribir cualquier número, por grande que sea. Por eso se dice que es un sistema <b>decimal</b> o de <b>base 10</b>."),
  P("Cuando juntamos 10 elementos formamos un grupo que <b>pasa al lugar de la izquierda</b>: 10 unidades forman 1 decena, 10 decenas forman 1 centena y 10 centenas forman 1 unidad de mil."),
  E("Escribir 23 caramelos","Agrupamos de a 10.",["Con 23 caramelos se arman 2 grupos de 10 y sobran 3.","Los 2 grupos van al lugar de las decenas y los 3 sueltos, al de las unidades.","Se escribe 23: 2 decenas y 3 unidades."]),
 ]),
 S(1,"Valor posicional",[
  D("Valor posicional","El valor de una cifra <b>depende del lugar que ocupa</b>. En 353, el 3 de la izquierda vale 300 y el 3 de la derecha vale 3."),
  T("Valor de cada cifra en 4.808",["Cifra","Lugar","Valor"],[["4","Unidades de mil","4.000"],["8","Centenas","800"],["0","Decenas","0"],["8","Unidades","8"]],"El mismo 8 vale 800 o 8 según dónde esté."),
  IM("El cero","El 0 marca un lugar vacío. En 4.808 no hay decenas, pero el 0 hace falta para que el 8 de las centenas no se corra de lugar."),
 ]),
 S(2,"Números grandes",[
  P("Para leer un número grande se separan las cifras <b>de a tres, de derecha a izquierda</b>: unidades, miles, millones y miles de millones. Cada grupo se lee como un número de hasta tres cifras y se le agrega su nombre."),
  T("Un número de 12 cifras",["Miles de millones","Millones","Miles","Unidades"],[["845","302","017","650"]],"Se lee: ochocientos cuarenta y cinco mil trescientos dos millones diecisiete mil seiscientos cincuenta."),
 ]),
 S(2,"Descomponer un número",[
  D("Descomposición aditiva","Escribir el número como <b>suma de los valores de sus cifras</b>: 3.506 = 3.000 + 500 + 6."),
  D("Descomposición multiplicativa","Cada valor se escribe como <b>cifra por 1, 10, 100, 1.000…</b>: 3.506 = 3 × 1.000 + 5 × 100 + 6 × 1."),
 ]),
],
"ejemplo_completo":{"titulo":"Leer y descomponer 60.723","planteo":"Leé el número y hacé las dos descomposiciones.","pasos":["Separamos de a tres desde la derecha: 60 | 723.","Se lee: sesenta mil setecientos veintitrés.","Aditiva: 60.000 + 700 + 20 + 3.","Multiplicativa: 6 × 10.000 + 7 × 100 + 2 × 10 + 3 × 1.","El 0 de las unidades de mil vale 0, por eso no se escribe en la descomposición."]},
"ejemplo_incompleto":{"titulo":"Descomponer 9.045","planteo":"Completá los espacios.","pasos":["Aditiva: 9.000 + ___ + 5.","Multiplicativa: 9 × ___ + 4 × 10 + 5 × 1.","El 0 está en el lugar de las ___ ."]},
"ejemplo_solo":{"titulo":"7.250.008","planteo":"Escribí cómo se lee y hacé la descomposición aditiva."},
"tip":{"titulo":"Contá lugares desde la derecha","texto":"Para saber cuánto vale una cifra, contá desde la derecha: 1.º unidades, 2.º decenas, 3.º centenas, 4.º unidades de mil…"},
"ojo":["Olvidar el cero: cuatro mil cinco se escribe 4.005, no 45.","Sumar las cifras en vez de sus valores: 352 no es 3 + 5 + 2, es 300 + 50 + 2."],
"resumen":[{"titulo":"Base 10","texto":"10 cifras. Cada 10 se forma un grupo que pasa a la izquierda."},{"titulo":"Valor posicional","texto":"En 353, el primer 3 vale 300 y el último, 3."},{"titulo":"Números grandes","texto":"Se separan de a tres desde la derecha."},{"titulo":"Descomponer","texto":"3.506 = 3.000 + 500 + 6 = 3 × 1.000 + 5 × 100 + 6 × 1."}],
"glosario":[{"palabra":"Cifra","significado":"Cada uno de los símbolos 0 a 9 con que se escriben los números."},{"palabra":"Base","significado":"De a cuánto se agrupa. En el sistema decimal, de a 10."},{"palabra":"Valor posicional","significado":"Lo que vale una cifra según el lugar que ocupa."},{"palabra":"Decena, centena","significado":"Grupo de 10 y grupo de 100."},{"palabra":"Descomposición","significado":"Escribir un número separado en partes según sus cifras."}],
"carpeta":["¿Cuánto vale el 7 en 47.215?","Escribí con cifras: dos millones treinta mil cuatro.","Hacé la descomposición aditiva de 8.064.","Un compañero escribió \"cuatro mil cinco\" como 45. ¿Cómo se escribe bien?"],
"respuestas_carpeta":[["7000"],["2030004"],["8000+60+4","8000+0+60+4"],["4005"]],
"soluciones":{"incompleto":"40. 1.000. Centenas.","solo":"Siete millones doscientos cincuenta mil ocho. 7.000.000 + 200.000 + 50.000 + 8.","carpeta":["7.000: está en el lugar de las unidades de mil.","2.030.004: 2 | 030 | 004.","8.000 + 60 + 4.","4.005: el 0 ocupa los lugares vacíos de las centenas y las decenas."]}
}
N2={
"objetivo":"Vas a poder escribir los lugares del sistema decimal como potencias de 10, descomponer números con ellas, multiplicar y dividir por 10, 100 y 1.000 y comparar números grandes.",
"vas_a_ver":["Cada lugar es una potencia de 10","Por qué 10⁰ = 1","Descomposición con potencias de 10","Multiplicar y dividir por 10, 100 y 1.000","Orden de magnitud y comparación de números grandes"],
"secciones":[
 S(1,"Cada lugar es una potencia de 10",[
  D("Potencia de 10","Es 10 multiplicado por sí mismo varias veces: 10³ = 10 × 10 × 10 = 1.000. El <b>exponente</b> dice cuántas veces se multiplica el 10 y coincide con la cantidad de ceros."),
  T("Lugares y potencias",["Lugar","Grupos de","Potencia"],[["Unidades","1","10⁰"],["Decenas","10","10¹"],["Centenas","100","10²"],["Unidades de mil","1.000","10³"],["Decenas de mil","10.000","10⁴"]]),
  IM("10⁰ = 1","El lugar de las unidades corresponde a 10⁰, que vale 1: son grupos de a uno."),
 ]),
 S(1,"Descomponer con potencias",[
  P("Cada cifra se multiplica por la <b>potencia de 10 de su lugar</b> y se suman los resultados."),
  E("Descomponer 3.152","Cifra por potencia.",["3 × 10³ + 1 × 10² + 5 × 10¹ + 2 × 10⁰.","= 3 × 1.000 + 1 × 100 + 5 × 10 + 2 × 1.","= 3.000 + 100 + 50 + 2 = 3.152."]),
 ]),
 S(2,"Multiplicar y dividir por 10, 100 y 1.000",[
  D("Regla","Multiplicar por 10, 100 o 1.000 <b>agrega</b> 1, 2 o 3 ceros: cada cifra sube 1, 2 o 3 lugares. Dividir, cuando el número termina en esos ceros, los <b>saca</b>."),
  T("Ejemplos",["Cálculo","Resultado"],[["45 × 100","4.500"],["7 × 1.000","7.000"],["38.000 ÷ 10","3.800"],["520.000 ÷ 1.000","520"]]),
 ]),
 S(2,"Orden de magnitud y comparación",[
  D("Orden de magnitud","Es la potencia de 10 del lugar de la <b>primera cifra</b> del número. 4.700 es del orden de los miles (10³)."),
  P("Para comparar números naturales: el que tiene <b>más cifras</b> es mayor. Si tienen la misma cantidad, se comparan las cifras de izquierda a derecha hasta encontrar una distinta."),
  E("Comparar 98.700 y 102.000","Contamos cifras.",["98.700 tiene 5 cifras y 102.000 tiene 6.","102.000 es mayor, aunque empiece con 1."]),
 ]),
],
"ejemplo_completo":{"titulo":"Descomponer 40.608 con potencias de 10","planteo":"Escribí cada cifra por su potencia y controlá.","pasos":["Lugares: 4 en 10⁴, 0 en 10³, 6 en 10², 0 en 10¹, 8 en 10⁰.","Los ceros no se escriben: 4 × 10⁴ + 6 × 10² + 8 × 10⁰.","Control: 40.000 + 600 + 8 = 40.608."]},
"ejemplo_incompleto":{"titulo":"Descomponer 5.230","planteo":"Completá los espacios.","pasos":["El 5 está en el lugar de 10 elevado a ___ .","El 3 está en el lugar de 10 elevado a ___ .","Control: 5.000 + ___ + 30 = 5.230."]},
"ejemplo_solo":{"titulo":"63 × 1.000 y 63.000 ÷ 100","planteo":"Resolvé los dos cálculos y decí el orden de magnitud de cada resultado."},
"tip":{"titulo":"Contá los ceros","texto":"En una potencia de 10, el exponente es la cantidad de ceros: 10⁵ = 100.000."},
"ojo":["Creer que 10⁰ es 0: vale 1.","Confundir 10³ con 10 × 3: 10³ = 1.000, no 30."],
"resumen":[{"titulo":"Potencias de 10","texto":"10⁰ = 1, 10¹ = 10, 10² = 100, 10³ = 1.000."},{"titulo":"Descomponer","texto":"3.152 = 3 × 10³ + 1 × 10² + 5 × 10¹ + 2 × 10⁰."},{"titulo":"× y ÷ por 10, 100, 1.000","texto":"Agregan o sacan ceros. Ej.: 45 × 100 = 4.500."},{"titulo":"Comparar","texto":"Más cifras, mayor. Si empatan, de izquierda a derecha."}],
"glosario":[{"palabra":"Potencia","significado":"Multiplicación de un número por sí mismo varias veces."},{"palabra":"Exponente","significado":"El número chiquito arriba: cuántas veces se multiplica."},{"palabra":"Orden de magnitud","significado":"La potencia de 10 del lugar de la primera cifra."},{"palabra":"Descomposición polinómica","significado":"Cifra por potencia de 10, sumadas."}],
"carpeta":["Calculá 10⁴.","Escribí el número: 7 × 10³ + 2 × 10² + 5 × 10⁰.","Calculá 340 × 100.","¿Cuál es mayor: 99.999 o 100.001?"],
"respuestas_carpeta":[["10000"],["7205"],["34000"],["100001"]],
"soluciones":{"incompleto":"3. 1. 200.","solo":"63.000, del orden de las decenas de mil (10⁴). 630, del orden de las centenas (10²).","carpeta":["10.000.","7.205: 7.000 + 200 + 5 (no hay decenas).","34.000: se agregan dos ceros.","100.001: tiene 6 cifras y 99.999 tiene 5."]}
}
N3={
"objetivo":"Vas a poder explicar cómo funciona el sistema binario y pasar números de decimal a binario y de binario a decimal.",
"vas_a_ver":["Base 2: solo dos cifras, 0 y 1","Los lugares son potencias de 2","Cómo se escribe y se lee un número en otra base","De decimal a binario: divisiones sucesivas y restas sucesivas","De binario a decimal"],
"secciones":[
 S(1,"Base 2",[
  D("Sistema binario","Usa solo <b>dos cifras: 0 y 1</b>. Es el sistema de las computadoras y los aparatos electrónicos: 0 es apagado (sin corriente) y 1 es encendido."),
  P("También es posicional, pero en vez de agrupar de a 10 se agrupa <b>de a 2</b>. Por eso cada lugar vale el doble que el anterior: son las potencias de 2."),
  T("Lugares del binario",["Potencia","2⁰","2¹","2²","2³","2⁴","2⁵"],[["Vale","1","2","4","8","16","32"]]),
 ]),
 S(1,"Cómo se escribe y se lee",[
  IM("La base se indica","La base se escribe chiquita abajo: 101₂. Se lee cifra por cifra: \"uno, cero, uno en base 2\". No se dice \"ciento uno\", porque centena y decena son palabras de la base 10."),
  P("Lo mismo pasa con cualquier base. En base 8 se agrupa de a 8: 11 objetos son 1 grupo de 8 y 3 sueltos, o sea 13₈."),
 ]),
 S(2,"De decimal a binario",[
  P("Se divide por 2 una y otra vez (<b>divisiones sucesivas</b>) hasta llegar a cociente 0. Cada división arma grupos de 2 y su resto es lo que queda suelto en ese lugar. El número binario se forma con los <b>restos leídos de abajo hacia arriba</b>."),
  E("Pasar 11 a binario","Divisiones sucesivas.",["11 ÷ 2 = 5, resto 1.","5 ÷ 2 = 2, resto 1.","2 ÷ 2 = 1, resto 0.","1 ÷ 2 = 0, resto 1.","Restos de abajo hacia arriba: 11 = 1011₂."]),
  P("Otra forma son las <b>restas sucesivas</b>: se resta la potencia de 2 más grande que entra; cada potencia que se pudo restar es un 1 y cada una que no, un 0. Ej.: 20 = 16 + 4, así que 20 = 10100₂."),
 ]),
 S(2,"De binario a decimal",[
  P("Se multiplica cada cifra por el valor de su lugar (1, 2, 4, 8… desde la derecha) y se suma."),
  E("Pasar 1110₂ a decimal","Cifra por lugar.",["De derecha a izquierda: 0 × 1 + 1 × 2 + 1 × 4 + 1 × 8.","= 0 + 2 + 4 + 8.","= 14."]),
 ]),
],
"ejemplo_completo":{"titulo":"Pasar 19 a binario y comprobar","planteo":"Usá divisiones sucesivas.","pasos":["19 ÷ 2 = 9, resto 1.","9 ÷ 2 = 4, resto 1.","4 ÷ 2 = 2, resto 0.","2 ÷ 2 = 1, resto 0.","1 ÷ 2 = 0, resto 1.","Restos de abajo hacia arriba: 10011₂.","Comprobación: 16 + 0 + 0 + 2 + 1 = 19."]},
"ejemplo_incompleto":{"titulo":"Pasar 10110₂ a decimal","planteo":"Completá los espacios.","pasos":["De derecha a izquierda: 0 × 1 + 1 × 2 + 1 × 4 + 0 × 8 + 1 × ___ .","= 0 + 2 + 4 + 0 + ___ .","= ___ ."]},
"ejemplo_solo":{"titulo":"Pasar 26 a binario","planteo":"Usá divisiones sucesivas y comprobá el resultado."},
"tip":{"titulo":"Armá la tabla de potencias","texto":"Antes de empezar escribí 1, 2, 4, 8, 16, 32… de derecha a izquierda. Te sirve para ir y volver entre binario y decimal."},
"ojo":["Leer los restos de arriba hacia abajo: para 6 los restos son 0, 1, 1 y el número es 110₂, no 011₂.","Leer 101₂ como \"ciento uno\": se lee uno, cero, uno en base 2 y vale 5."],
"resumen":[{"titulo":"Base 2","texto":"Solo 0 y 1. Lo usan las computadoras."},{"titulo":"Lugares","texto":"1, 2, 4, 8, 16, 32… (potencias de 2)."},{"titulo":"Decimal → binario","texto":"Dividir por 2 y leer los restos de abajo hacia arriba."},{"titulo":"Binario → decimal","texto":"Cifra por lugar y sumar. Ej.: 1110₂ = 14."}],
"glosario":[{"palabra":"Binario","significado":"Sistema de base 2, con las cifras 0 y 1."},{"palabra":"Divisiones sucesivas","significado":"Dividir varias veces seguidas el cociente anterior."},{"palabra":"Resto","significado":"Lo que sobra en una división."},{"palabra":"Subíndice","significado":"Número chiquito abajo que indica la base."}],
"carpeta":["Pasá 9 a binario.","Pasá 111₂ a decimal.","Pasá 12 a binario.","Un compañero pasó 6 a binario y escribió 011₂. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["1001","1001₂","1001(2)"],["7"],["1100","1100₂","1100(2)"],["110","110₂","110(2)"]],
"soluciones":{"incompleto":"16. 16. 22.","solo":"26 ÷ 2 = 13 r 0; 13 ÷ 2 = 6 r 1; 6 ÷ 2 = 3 r 0; 3 ÷ 2 = 1 r 1; 1 ÷ 2 = 0 r 1. 26 = 11010₂. Comprobación: 16 + 8 + 2 = 26.","carpeta":["1001₂: 8 + 1 = 9.","7: 4 + 2 + 1.","1100₂: 8 + 4 = 12.","110₂: leyó los restos al revés; van de abajo hacia arriba."]}
}
N4={
"objetivo":"Vas a poder usar el sistema sexagesimal para medir el tiempo y los ángulos, pasar de una unidad a otra y sumar y restar medidas.",
"vas_a_ver":["Un sistema que agrupa de a 60","Horas, minutos y segundos","Pasar de una unidad a otra","Sumar y restar tiempos","Grados, minutos y segundos en los ángulos"],
"secciones":[
 S(1,"Agrupar de a 60",[
  D("Sistema sexagesimal","Agrupa <b>de a 60</b>: 60 segundos forman 1 minuto y 60 minutos forman 1 hora. Lo usamos para medir el tiempo y los ángulos."),
  T("Equivalencias",["Unidad","Equivale a"],[["1 hora (h)","60 minutos"],["1 minuto (min)","60 segundos"],["1 hora","3.600 segundos"]]),
 ]),
 S(1,"Pasar de una unidad a otra",[
  P("Para pasar a una unidad <b>más chica</b> se multiplica por 60. Para pasar a una <b>más grande</b> se divide por 60: el cociente son las unidades grandes y el resto, las que sobran."),
  E("Pasar 150 minutos a horas","Dividimos por 60.",["150 ÷ 60 = 2, resto 30.","150 min = 2 h 30 min."]),
 ]),
 S(2,"Sumar y restar tiempos",[
  P("Se suman o restan horas con horas, minutos con minutos y segundos con segundos. Si los minutos llegan a 60 o más, se canjean por horas. Si en una resta no alcanza, se pide 1 hora prestada, que son 60 minutos."),
  E("Sumar 1 h 45 min + 2 h 30 min","Por columnas.",["Horas: 1 + 2 = 3. Minutos: 45 + 30 = 75.","75 min = 1 h 15 min.","Total: 4 h 15 min."]),
  E("Restar 3 h 10 min − 1 h 40 min","Pedimos prestado.",["10 min no alcanza para restar 40 min.","Pedimos 1 h: queda 2 h 70 min.","2 h 70 min − 1 h 40 min = 1 h 30 min."]),
 ]),
 S(2,"Los ángulos",[
  D("Grados, minutos y segundos","Los ángulos se miden en <b>grados (°)</b>. 1° = 60 minutos (60′) y 1′ = 60 segundos (60″). Se opera igual que con el tiempo."),
  P("Ejemplo: 25° 40′ + 10° 35′ = 35° 75′ = 36° 15′."),
 ]),
],
"ejemplo_completo":{"titulo":"¿A qué hora termina la película?","planteo":"Una película dura 135 minutos y empieza a las 20:50.","pasos":["135 ÷ 60 = 2, resto 15: dura 2 h 15 min.","20 h 50 min + 2 h 15 min = 22 h 65 min.","65 min = 1 h 5 min.","Termina a las 23:05."]},
"ejemplo_incompleto":{"titulo":"Pasar 3 h 20 min a minutos","planteo":"Completá los espacios.","pasos":["3 h = 3 × 60 = ___ min.","180 + 20 = ___ min."]},
"ejemplo_solo":{"titulo":"5 h 15 min − 2 h 50 min","planteo":"Resolvé la resta. Pensá si hace falta pedir prestado."},
"tip":{"titulo":"Pensá en el reloj","texto":"Cuando los minutos llegan a 60, el reloj suma una hora y vuelve a 0. Así funciona cada canje de 60."},
"ojo":["No canjear: 1 h 50 min + 20 min no es 1 h 70 min, es 2 h 10 min.","Pedir prestado 100 en vez de 60: 1 hora prestada son 60 minutos."],
"resumen":[{"titulo":"Base 60","texto":"60 s = 1 min; 60 min = 1 h."},{"titulo":"Pasar de unidad","texto":"A más chica, × 60. A más grande, ÷ 60 (el resto sobra)."},{"titulo":"Sumar y restar","texto":"Por columnas, canjeando de a 60."},{"titulo":"Ángulos","texto":"1° = 60′ y 1′ = 60″."}],
"glosario":[{"palabra":"Sexagesimal","significado":"Sistema que agrupa de a 60."},{"palabra":"Canjear","significado":"Cambiar 60 unidades chicas por 1 grande."},{"palabra":"Grado (°)","significado":"Unidad para medir ángulos."},{"palabra":"Minuto (′) y segundo (″)","significado":"Partes del grado, igual que en el reloj."}],
"carpeta":["¿Cuántos minutos son 4 horas?","Pasá 200 minutos a horas y minutos.","Sumá 2 h 40 min + 1 h 35 min.","Un compañero restó 4 h 10 min − 1 h 30 min pidiendo prestados 100 minutos y le dio 2 h 80 min. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["240"],["3h20min","3h20m","3h20","3:20","3horas20minutos"],["4h15min","4h15m","4h15","4:15","4horas15minutos"],["2h40min","2h40m","2h40","2:40","2horas40minutos"]],
"soluciones":{"incompleto":"180. 200.","solo":"Pedimos 1 h: 4 h 75 min − 2 h 50 min = 2 h 25 min.","carpeta":["240: 4 × 60.","3 h 20 min: 200 ÷ 60 = 3, resto 20.","4 h 15 min: 3 h 75 min y 75 min = 1 h 15 min.","2 h 40 min: 1 h prestada son 60 min, así que queda 3 h 70 min − 1 h 30 min."]}
}
V=lambda **d:{"vars":{k:{"min":a,"max":b} for k,(a,b) in d.items()}}
ACT={
"1":[MC("En 5.252, ¿cuánto vale el 5 de la izquierda?",["5","50","500","5.000"],"5.000","Está en el lugar de las unidades de mil: vale 5.000."),
     N("Escribí el número que forman {a} unidades de mil, {b} centenas y {c} unidades.",{"formula":"a*1000+b*100+c"},"No hay decenas: en ese lugar va un 0.",V(a=(1,9),b=(1,9),c=(1,9)))],
"2":[N("Escribí el número: {a} × 10³ + {b} × 10² + {c} × 10⁰.",{"formula":"a*1000+b*100+c"},"10³ = 1.000, 10² = 100 y 10⁰ = 1. No hay decenas.",V(a=(1,9),b=(1,9),c=(1,9))),
     MC("¿Cuál es mayor?",["98.765","100.234","Son iguales"],"100.234","100.234 tiene 6 cifras y 98.765 tiene 5.")],
"3":[N("Pasá 1010₂ a decimal.",{"acepta":[10]},"0 × 1 + 1 × 2 + 0 × 4 + 1 × 8 = 10."),
     N("Pasá 23 a binario. Escribí solo las cifras.",{"acepta":[10111]},"Restos de 23 ÷ 2 sucesivas: 1, 1, 1, 0, 1. De abajo hacia arriba: 10111₂ (16 + 4 + 2 + 1).")],
"4":[N("¿Cuántos minutos son {h} h {m} min?",{"formula":"h*60+m"},"Las horas se multiplican por 60 y se suman los minutos.",V(h=(1,5),m=(1,59))),
     MC("Sumá 1 h 50 min + 1 h 25 min.",["2 h 75 min","3 h 15 min","3 h 75 min","2 h 15 min"],"3 h 15 min","50 + 25 = 75 min = 1 h 15 min; 2 h + 1 h 15 min = 3 h 15 min.")],
"5":[MC("Relámpago. ¿Cuánto vale el 3 en 4.307?",["3","30","300","3.000"],"300","Está en el lugar de las centenas.",tiempo=15),
     N("Relámpago. Pasá 110₂ a decimal.",{"acepta":[6]},"4 + 2 + 0 = 6.",tiempo=30),
     VF("Relámpago. 10³ es igual a 30.","Falso","10³ = 10 × 10 × 10 = 1.000.",tiempo=15),
     N("Relámpago. ¿Cuántos segundos son 3 minutos?",{"acepta":[180]},"3 × 60 = 180.",tiempo=20)],
}
EXAMEN=[
 [1,N("Escribí el número que forman {a} decenas de mil, {b} centenas y {c} unidades.",{"formula":"a*10000+b*100+c"},"Las unidades de mil y las decenas quedan vacías: van ceros.",V(a=(1,9),b=(1,9),c=(1,9)))],
 [1,MC("¿Cuál es la descomposición aditiva de 7.408?",["7.000 + 400 + 8","7 + 4 + 0 + 8","7.000 + 40 + 8","700 + 40 + 8"],"7.000 + 400 + 8","Se suman los valores de las cifras, no las cifras.")],
 [1,MC("¿Cómo se escribe con cifras \"tres millones cuarenta mil doce\"?",["3.040.012","3.400.012","3.040.120","340.012"],"3.040.012","3 | 040 | 012.")],
 [2,N("Calculá 10⁵.",{"acepta":[100000]},"Un 1 seguido de 5 ceros: 100.000.")],
 [2,N("Calculá {a} × 1.000.",{"formula":"a*1000"},"Multiplicar por 1.000 agrega tres ceros.",V(a=(2,99)))],
 [2,MC("¿Qué número es 6 × 10⁴ + 3 × 10² + 5 × 10⁰?",["60.305","6.305","60.035","635"],"60.305","60.000 + 300 + 5 = 60.305.")],
 [3,N("Pasá 1100₂ a decimal.",{"acepta":[12]},"8 + 4 + 0 + 0 = 12.")],
 [3,N("Pasá 18 a binario. Escribí solo las cifras.",{"acepta":[10010]},"18 = 16 + 2: 10010₂.")],
 [3,VF("En el sistema binario se usan solo las cifras 0 y 1.","Verdadero","Es un sistema de base 2: dos cifras.")],
 [4,N("¿Cuántos segundos son {m} minutos?",{"formula":"m*60"},"Cada minuto tiene 60 segundos.",V(m=(2,20)))],
 [4,MC("¿Cuánto es 190 minutos en horas y minutos?",["1 h 90 min","3 h 10 min","1 h 9 min","3 h 1 min"],"3 h 10 min","190 ÷ 60 = 3, resto 10.")],
 [4,MC("Restá 5 h 20 min − 2 h 45 min.",["3 h 25 min","2 h 35 min","2 h 75 min","3 h 35 min"],"2 h 35 min","Pedimos 1 h: 4 h 80 min − 2 h 45 min = 2 h 35 min.")],
 [4,MC("¿A cuántos minutos (′) equivale 1 grado?",["10","60","100","360"],"60","1° = 60′.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":1,"practica":"Práctica general: sistemas de numeración","examen_titulo":"Nivel jefe: sistemas de numeración",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-1.json"),"w"),ensure_ascii=False)
print("ok")
