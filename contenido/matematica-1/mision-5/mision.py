# -*- coding: utf-8 -*-
"""Matemática I · Misión 5 · Múltiplos y divisores. Genera mision-5.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
N1={
"objetivo":"Vas a poder explicar qué es un múltiplo, encontrar múltiplos comunes y usar las regularidades de los múltiplos para resolver problemas.",
"vas_a_ver":["Qué es un múltiplo, con la definición formal","Por qué el 0 es múltiplo de todos","Múltiplos comunes de dos números","Patrones que se repiten en los múltiplos","Problemas de cosas que se repiten"],
"secciones":[
 S(1,"Qué es un múltiplo",[
  D("Múltiplo","Un número <b>a es múltiplo de b</b> si se puede escribir como <b>a = b × k</b>, con k un número natural o 0. Por ejemplo, 84 es múltiplo de 7 porque 84 = 7 × 12."),
  P("Los múltiplos de 6 son 0, 6, 12, 18, 24, 30… Son <b>infinitos</b>: siempre podés multiplicar por un número más grande."),
  IM("El 0","El 0 es múltiplo de todos los números, porque 0 = b × 0 para cualquier b."),
 ]),
 S(1,"Múltiplos comunes",[
  D("Múltiplo común","Un <b>múltiplo común</b> de dos números es un número que es múltiplo de los dos a la vez."),
  T("Múltiplos de 4 y de 6 hasta 36",["Número","Múltiplos"],[["4","0, 4, 8, 12, 16, 20, 24, 28, 32, 36"],["6","0, 6, 12, 18, 24, 30, 36"],["Comunes","0, 12, 24, 36"]],"Para encontrar los comunes hay que listar suficientes múltiplos de cada uno."),
 ]),
 S(2,"Patrones que se repiten",[
  P("Las últimas cifras de los múltiplos se repiten en un ciclo. Los de 5 terminan en 0, 5, 0, 5…; los de 4, en 4, 8, 2, 6, 0 y vuelve a empezar."),
  P("Esto sirve para descartar rápido: 1.003 no puede ser múltiplo de 5, porque termina en 3."),
 ]),
 S(2,"Problemas de cosas que se repiten",[
  P("Cuando algo pasa cada cierta cantidad de tiempo, los momentos en que pasa son múltiplos de esa cantidad."),
  E("El colectivo","Un colectivo sale de la terminal cada 15 minutos desde las 8:00. ¿Sale uno a las 9:30?",["De 8:00 a 9:30 pasan 90 minutos.","90 = 15 × 6: es múltiplo de 15.","Sí, sale uno a las 9:30 (el sexto después del de las 8:00)."]),
 ]),
],
"ejemplo_completo":{"titulo":"natación","planteo":"Ana va a natación cada 4 días y Beto cada 6. Hoy fueron los dos. ¿Dentro de cuántos días vuelven a coincidir? ¿Y la vez siguiente?","pasos":["Ana va los días que son múltiplos de 4: 4, 8, 12, 16, 20, 24…","Beto va los días que son múltiplos de 6: 6, 12, 18, 24…","Los múltiplos comunes (sin el 0) son 12, 24…","Vuelven a coincidir dentro de 12 días, y después dentro de 24."]},
"ejemplo_incompleto":{"titulo":"múltiplos de 8","planteo":"Completá los espacios.","pasos":["96 = 8 × ___ , así que 96 es múltiplo de 8.","Los múltiplos de 8 entre 50 y 70 son 56 y ___ ."]},
"ejemplo_solo":{"titulo":"comunes de 6 y 9","planteo":"Escribí los múltiplos comunes de 6 y 9 que están entre 1 y 60."},
"tip":{"titulo":"Listá de más","texto":"Para buscar múltiplos comunes, escribí varios múltiplos de cada número: si te quedás en los primeros, puede que no aparezca ninguno común."},
"ojo":["Confundir múltiplo con divisor: 24 es múltiplo de 6, y 6 es divisor de 24, no al revés.","Creer que el 0 no es múltiplo: 0 = 5 × 0, así que es múltiplo de 5."],
"resumen":[{"titulo":"Múltiplo","texto":"a = b × k. Ej.: 84 = 7 × 12."},{"titulo":"Infinitos","texto":"Todo número tiene infinitos múltiplos."},{"titulo":"El 0","texto":"Es múltiplo de todos: 0 = b × 0."},{"titulo":"Comunes","texto":"Múltiplos de los dos. Ej.: 4 y 6 → 12, 24, 36."},{"titulo":"Patrones","texto":"Las últimas cifras se repiten en ciclos."}],
"glosario":[{"palabra":"Múltiplo","significado":"Resultado de multiplicar un número por un natural o por 0."},{"palabra":"Múltiplo común","significado":"Número que es múltiplo de dos o más números."},{"palabra":"Infinito","significado":"Que no se termina nunca."},{"palabra":"Ciclo","significado":"Algo que se repite siempre en el mismo orden."}],
"carpeta":["Si el primer múltiplo de 7 es 7, ¿cuál es el quinto?","¿Cuántos múltiplos de 9 hay entre 1 y 50?","¿Cuál es el menor múltiplo común de 4 y 10, sin contar el 0?","Un compañero dice que 0 no es múltiplo de 5. Si escribís 0 = 5 × k, ¿cuánto vale k?"],
"respuestas_carpeta":[["35"],["5"],["20"],["0"]],
"soluciones":{"incompleto":"96 = 8 × 12. Los múltiplos son 56 y 64.","solo":"Múltiplos de 9: 9, 18, 27, 36, 45, 54. Los que también son de 6: 18, 36 y 54.","carpeta":["35: 7 × 5.","5: 9, 18, 27, 36 y 45.","20: múltiplos de 10: 10, 20…; 10 no es múltiplo de 4 y 20 sí.","0: 5 × 0 = 0, así que 0 es múltiplo de 5."]}
}
N2={
"objetivo":"Vas a poder encontrar todos los divisores de un número de forma ordenada, sin que se escape ninguno, y encontrar divisores comunes.",
"vas_a_ver":["Qué es un divisor","La relación entre divisor y múltiplo","Buscar divisores por parejas","Divisores comunes","Cuántos divisores tiene un número"],
"secciones":[
 S(1,"Qué es un divisor",[
  D("Divisor","Un número <b>b es divisor de a</b> si la división a ÷ b es <b>exacta</b> (resto 0). También se dice que b <b>divide</b> a a."),
  P("Divisor y múltiplo son la misma relación mirada al revés: 24 = 6 × 4, así que 6 y 4 son divisores de 24, y 24 es múltiplo de 6 y de 4."),
 ]),
 S(1,"Buscar divisores por parejas",[
  D("Búsqueda por parejas","Se prueba con 1, 2, 3… en orden. Cada vez que uno divide, se anota la <b>pareja</b>: el divisor y el cociente. Se termina cuando los números de la pareja se encuentran."),
  T("Divisores de 36",["Pareja","Producto"],[["1 y 36","1 × 36"],["2 y 18","2 × 18"],["3 y 12","3 × 12"],["4 y 9","4 × 9"],["6 y 6","6 × 6"]],"El 5 no divide a 36. Después del 6 las parejas se repetirían. Divisores: 1, 2, 3, 4, 6, 9, 12, 18 y 36."),
 ]),
 S(2,"Divisores comunes",[
  P("Un <b>divisor común</b> de dos números divide a los dos. Se listan los divisores de cada uno y se marcan los que se repiten."),
  E("Divisores comunes de 18 y 24","Listamos y comparamos.",["Divisores de 18: 1, 2, 3, 6, 9, 18.","Divisores de 24: 1, 2, 3, 4, 6, 8, 12, 24.","Comunes: 1, 2, 3 y 6."]),
 ]),
 S(2,"Cuántos divisores tiene",[
  P("Todo número mayor que 1 tiene al menos dos divisores: el 1 y él mismo. Por las parejas, la cantidad suele ser par; es <b>impar</b> solo cuando una pareja tiene dos números iguales, como 6 × 6 en el 36 (que tiene 9 divisores)."),
 ]),
],
"ejemplo_completo":{"titulo":"divisores de 60","planteo":"Encontrá todos los divisores de 60 por parejas.","pasos":["1 × 60 y 2 × 30.","3 × 20 y 4 × 15.","5 × 12 y 6 × 10.","7, 8 y 9 no dividen a 60; el 10 ya apareció: terminamos.","Divisores: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30 y 60. Son 12."]},
"ejemplo_incompleto":{"titulo":"divisores de 28","planteo":"Completá los espacios.","pasos":["1 × 28.","2 × ___ .","3 no divide a 28. 4 × ___ .","5 y 6 no dividen; el 7 ya apareció. 28 tiene ___ divisores."]},
"ejemplo_solo":{"titulo":"comunes de 20 y 30","planteo":"Encontrá los divisores comunes de 20 y 30."},
"tip":{"titulo":"Anotá la pareja enseguida","texto":"Cuando encontrás un divisor, escribí al mismo tiempo su pareja. Así no se te escapa ninguno y sabés cuándo parar."},
"ojo":["Olvidar el 1 y el propio número: los divisores de 15 son 1, 3, 5 y 15, no solo 3 y 5.","Parar antes de tiempo: hay que probar hasta que las parejas se encuentren."],
"resumen":[{"titulo":"Divisor","texto":"Divide en forma exacta. Ej.: 6 divide a 24."},{"titulo":"Relación","texto":"6 divide a 24 ↔ 24 es múltiplo de 6."},{"titulo":"Por parejas","texto":"36: 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6."},{"titulo":"Comunes","texto":"18 y 24 → 1, 2, 3, 6."},{"titulo":"Cantidad","texto":"Impar solo si hay una pareja de iguales."}],
"glosario":[{"palabra":"Divisor","significado":"Número que divide a otro en forma exacta."},{"palabra":"Dividir","significado":"Que la división da resto 0."},{"palabra":"Pareja de divisores","significado":"Dos números cuyo producto es el número."},{"palabra":"Divisor común","significado":"Número que divide a dos o más números."}],
"carpeta":["¿Cuántos divisores tiene 18?","¿Cuál es el mayor divisor de 45 que es menor que 45?","¿Cuántos divisores comunes tienen 12 y 18?","Un compañero escribió que los divisores de 15 son 3 y 5. ¿Cuántos divisores tiene 15 en realidad?"],
"respuestas_carpeta":[["6"],["15"],["4"],["4"]],
"soluciones":{"incompleto":"2 × 14. 4 × 7. 28 tiene 6 divisores: 1, 2, 4, 7, 14 y 28.","solo":"Divisores de 20: 1, 2, 4, 5, 10, 20. De 30: 1, 2, 3, 5, 6, 10, 15, 30. Comunes: 1, 2, 5 y 10.","carpeta":["6: 1, 2, 3, 6, 9 y 18.","15: 45 = 3 × 15 y la pareja más chica después del 1 es 3.","4: 1, 2, 3 y 6.","4: 1, 3, 5 y 15. Se olvidó del 1 y del 15."]}
}
N3={
"objetivo":"Vas a poder usar propiedades de la divisibilidad para justificar respuestas y mostrar con un contraejemplo que una afirmación es falsa.",
"vas_a_ver":["Divisibilidad en los enunciados","Si a divide a b y a c, divide a b + c","Si a divide a b, divide a sus múltiplos","Justificar con propiedades","Contraejemplos"],
"secciones":[
 S(1,"Divide a la suma",[
  D("Propiedad de la suma","Si un número <b>divide a b y a c</b>, entonces <b>divide a b + c</b> (y también a b − c)."),
  P("¿Por qué? 7 divide a 14 y a 21: 14 = 7 × 2 y 21 = 7 × 3. Entonces 14 + 21 = 7 × 2 + 7 × 3 = 7 × (2 + 3) = 7 × 5 = 35. Es la distributiva."),
  IM("Al revés no vale","3 divide a 4 + 5 = 9, pero no divide ni a 4 ni a 5."),
 ]),
 S(1,"Divide a los múltiplos",[
  D("Propiedad de los múltiplos","Si un número <b>divide a b</b>, también <b>divide a cualquier múltiplo de b</b>."),
  P("Ejemplo: 6 divide a 12, así que divide a 12 × 5 = 60 sin hacer la cuenta: 60 = 6 × 2 × 5 = 6 × 10."),
 ]),
 S(2,"Justificar",[
  P("Justificar es explicar <b>por qué</b> algo es verdad usando propiedades, no solo probar con un ejemplo. Un ejemplo que funciona no alcanza para decir que vale siempre."),
  E("Tres números consecutivos","¿La suma de tres números seguidos es siempre múltiplo de 3?",["Probamos: 4 + 5 + 6 = 15 = 3 × 5. Funciona, pero un ejemplo no alcanza.","El del medio es uno más que el primero, y el último es dos más.","Si sacamos 1 al último y se lo damos al primero, quedan tres números iguales al del medio: la suma es 3 veces el del medio.","Entonces siempre es múltiplo de 3."]),
 ]),
 S(2,"Contraejemplos",[
  P("Para mostrar que una afirmación es <b>falsa</b> alcanza con <b>un solo caso</b> donde no se cumple: un <b>contraejemplo</b>."),
  E("¿Divisible por 4 y por 6 implica divisible por 24?","Buscamos un caso que falle.",["24 es divisible por 4, por 6 y por 24: este caso cumple.","12 es divisible por 4 y por 6, pero 12 ÷ 24 no es exacta.","12 es un contraejemplo: la afirmación es falsa."]),
 ]),
],
"ejemplo_completo":{"titulo":"35 + 40 + 15","planteo":"¿Es 5 divisor de 35 + 40 + 15? Justificá sin hacer la suma primero.","pasos":["35 = 5 × 7, 40 = 5 × 8 y 15 = 5 × 3.","5 divide a cada sumando, así que divide a la suma.","35 + 40 + 15 = 5 × (7 + 8 + 3) = 5 × 18.","Comprobación: la suma es 90 y 90 ÷ 5 = 18."]},
"ejemplo_incompleto":{"titulo":"56 + 24","planteo":"¿8 divide a 56 + 24? Completá los espacios.","pasos":["56 = 8 × ___ .","24 = 8 × ___ .","56 + 24 = 8 × (7 + 3) = 8 × ___ . Sí, 8 divide a 80."]},
"ejemplo_solo":{"titulo":"un contraejemplo","planteo":"Mostrá con un contraejemplo que es falso: \"si un número es divisible por 2 y por 4, entonces es divisible por 8\"."},
"tip":{"titulo":"Para probar, propiedad; para refutar, contraejemplo","texto":"Si querés mostrar que algo vale siempre, usá una propiedad. Si querés mostrar que es falso, buscá un solo caso que falle."},
"ojo":["Responder sin justificar: decir \"sí\" no alcanza; hay que explicar por qué.","Generalizar con un solo ejemplo: que 24 funcione no prueba que funcione siempre."],
"resumen":[{"titulo":"Suma","texto":"Si a divide a b y a c, divide a b + c. Ej.: 7 divide a 14 + 21."},{"titulo":"Al revés no","texto":"3 divide a 4 + 5, pero no a 4."},{"titulo":"Múltiplos","texto":"Si a divide a b, divide a b × k."},{"titulo":"Justificar","texto":"Explicar con propiedades, no con un solo ejemplo."},{"titulo":"Contraejemplo","texto":"Un caso que falla alcanza para refutar."}],
"glosario":[{"palabra":"Divisible","significado":"Que se puede dividir en forma exacta por otro número."},{"palabra":"Justificar","significado":"Explicar por qué algo es verdad."},{"palabra":"Contraejemplo","significado":"Un caso que muestra que una afirmación es falsa."},{"palabra":"Consecutivos","significado":"Números seguidos, como 4, 5 y 6."}],
"carpeta":["Si 9 divide a 27 y a 45, ¿cuánto da (27 + 45) ÷ 9?","Calculá (6 × 13 + 18) ÷ 6.","¿Cuál es el menor número, sin contar el 0, que es divisible por 4 y por 6 pero no por 24?","Un compañero dice: \"como 3 divide a 6, divide a 6 + 4\". ¿Cuál es el resto de dividir 6 + 4 por 3?"],
"respuestas_carpeta":[["8"],["16"],["12"],["1"]],
"soluciones":{"incompleto":"56 = 8 × 7. 24 = 8 × 3. 8 × 10 = 80.","solo":"4 es divisible por 2 y por 4, pero no por 8 (también sirven 12 o 20).","carpeta":["8: 27 ÷ 9 = 3 y 45 ÷ 9 = 5; 3 + 5 = 8.","16: 78 + 18 = 96 y 96 ÷ 6 = 16.","12: los múltiplos comunes de 4 y 6 son 12, 24…; 12 no es divisible por 24.","1: 10 ÷ 3 = 3, resto 1. Para usar la propiedad, 3 tiene que dividir a los dos sumandos, y no divide a 4."]}
}
N4={
"objetivo":"Vas a poder resolver problemas de repartos y agrupamientos sin sobrantes, decidiendo si hay que buscar divisores o múltiplos.",
"vas_a_ver":["Repartir en partes iguales sin que sobre","Agrupar sin sobrantes","¿Divisores o múltiplos?","Cantidades posibles e imposibles","Problemas con varias pistas"],
"secciones":[
 S(1,"Repartos sin sobrantes",[
  D("Reparto exacto","Repartir una cantidad en partes iguales <b>sin que sobre</b> se puede solo si la cantidad de partes es un <b>divisor</b> de la cantidad total."),
  P("Ejemplo: 30 caramelos se pueden repartir sin que sobre entre 1, 2, 3, 5, 6, 10, 15 o 30 chicos, que son los divisores de 30. Entre 4 chicos, no: sobran 2."),
 ]),
 S(1,"¿Divisores o múltiplos?",[
  D("Cómo decidir","Si el <b>total está fijo</b> y buscás el tamaño o la cantidad de grupos, buscás <b>divisores</b>. Si el <b>tamaño del grupo está fijo</b> y buscás posibles totales, buscás <b>múltiplos</b>."),
  T("Dos preguntas parecidas",["Situación","Se busca"],[["Ubicar 24 alumnos en grupos iguales","Divisores de 24"],["Huevos en maples de 12 llenos","Múltiplos de 12"]]),
 ]),
 S(2,"Posibles e imposibles",[
  P("Las condiciones del problema dejan solo algunas opciones. Hay que revisar todas las posibles, no quedarse con la primera."),
  E("Las sillas","Hay 40 sillas para ubicar en filas iguales, con más de 5 y menos de 10 sillas por fila.",["Divisores de 40: 1, 2, 4, 5, 8, 10, 20, 40.","Entre 6 y 9 solo está el 8.","Se arman 5 filas de 8 sillas."]),
 ]),
 S(2,"Varias pistas",[
  P("Cuando hay varias pistas, se aplican una por una y se van tachando las opciones que no cumplen."),
  E("¿Cuántos alumnos?","Son entre 20 y 40. Se pueden agrupar de a 4 y de a 6 sin que sobre nadie. Son más de 30.",["Múltiplos comunes de 4 y 6 entre 20 y 40: 24 y 36.","Más de 30: queda solo 36.","Son 36 alumnos."]),
 ]),
],
"ejemplo_completo":{"titulo":"las bolsitas","planteo":"Hay 48 alfajores y 36 chocolates. Se arman bolsitas iguales, sin que sobre nada. ¿Cuántas bolsitas se pueden armar? Dá todas las opciones y la de más bolsitas.","pasos":["La cantidad de bolsitas tiene que dividir a 48 y a 36: es un divisor común.","Divisores de 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48.","Divisores de 36: 1, 2, 3, 4, 6, 9, 12, 18, 36.","Comunes: 1, 2, 3, 4, 6 y 12.","Con 12 bolsitas, cada una lleva 4 alfajores y 3 chocolates."]},
"ejemplo_incompleto":{"titulo":"los estantes","planteo":"Hay 42 libros para poner en estantes, la misma cantidad en cada uno, entre 5 y 10 libros por estante. Completá los espacios.","pasos":["42 = 6 × ___ .","42 = 7 × ___ .","5, 8, 9 y 10 no dividen a 42.","Se pueden poner 6 o ___ libros por estante."]},
"ejemplo_solo":{"titulo":"las figuritas","planteo":"Un chico tiene entre 50 y 70 figuritas. Si las agrupa de a 9 no sobra ninguna, y si las agrupa de a 2 tampoco. ¿Cuántas figuritas tiene?"},
"tip":{"titulo":"Preguntate qué está fijo","texto":"Total fijo → divisores. Tamaño del grupo fijo → múltiplos. Esa pregunta te ordena todo el problema."},
"ojo":["Tomar un múltiplo cuando hace falta un divisor: para repartir 24 en grupos iguales, 48 no sirve.","Probar pocos casos: revisá todas las opciones antes de responder."],
"resumen":[{"titulo":"Reparto exacto","texto":"La cantidad de partes divide al total."},{"titulo":"Total fijo","texto":"Se buscan divisores. Ej.: 24 alumnos en grupos."},{"titulo":"Grupo fijo","texto":"Se buscan múltiplos. Ej.: maples de 12."},{"titulo":"Pistas","texto":"Se aplican de a una y se tachan opciones."}],
"glosario":[{"palabra":"Reparto","significado":"Dividir una cantidad en partes iguales."},{"palabra":"Sobrante","significado":"Lo que queda sin repartir."},{"palabra":"Agrupar","significado":"Formar grupos con la misma cantidad."},{"palabra":"Condición","significado":"Algo que la respuesta tiene que cumplir."}],
"carpeta":["¿De cuántas formas se pueden repartir 20 caramelos en partes iguales entre más de 1 chico, sin que sobre ninguno?","Un maple lleva 30 huevos. ¿Cuántos huevos hay en 7 maples llenos?","Hay entre 30 y 50 chicos. Se pueden formar grupos de 7 y también filas de 5 sin que sobre nadie. ¿Cuántos chicos son?","Un compañero dice que 26 sillas se pueden ordenar en filas de 4 sin que sobre ninguna. ¿Cuántas sillas sobran?"],
"respuestas_carpeta":[["5"],["210"],["35"],["2"]],
"soluciones":{"incompleto":"42 = 6 × 7. 42 = 7 × 6. Se pueden poner 6 o 7 libros.","solo":"Tiene que ser múltiplo de 9 y de 2, o sea de 18: 18, 36, 54, 72… Entre 50 y 70 solo está 54.","carpeta":["5: entre 2, 4, 5, 10 o 20 chicos.","210: 30 × 7 (múltiplo de 30).","35: múltiplos comunes de 7 y 5: 35, 70… Entre 30 y 50, 35.","2: 26 = 4 × 6 + 2. El 4 no es divisor de 26."]}
}
ACT={
"1":[N("Si el primer múltiplo de {n} es {n}, ¿cuál es el múltiplo número {k}?",{"formula":"n*k"},"El múltiplo número k es n × k.",{"vars":{"n":{"min":3,"max":12},"k":{"min":4,"max":12}}}),
     VF("El 0 es múltiplo de todos los números.","Verdadero","0 = b × 0 para cualquier número b.")],
"2":[N("¿Cuántos divisores tiene 24?",{"acepta":[8]},"1 × 24, 2 × 12, 3 × 8 y 4 × 6: son 8 divisores."),
     {"t":"multi_select","p":"¿Cuáles de estos números son divisores de 30?","o":["4","5","6","9","15"],"r":{"correctas":["5","6","15"]},"e":"30 = 5 × 6 = 2 × 15. 4 y 9 no dividen a 30."}],
"3":[MC("Si 7 divide a 21 y a 35, ¿qué podés asegurar?",["7 divide a 56","7 divide a 22","35 divide a 7","21 divide a 35"],"7 divide a 56","Si divide a los dos sumandos, divide a la suma: 21 + 35 = 56."),
     MC("¿Qué número es un contraejemplo de \"todo número divisible por 3 es divisible por 6\"?",["12","18","9","24"],"9","9 es divisible por 3 pero no por 6. Los otros son divisibles por los dos.")],
"4":[N("Se reparten {t} caramelos entre {n} chicos en partes iguales, sin que sobre. ¿Cuántos recibe cada uno?",{"formula":"k"},"Se divide el total por la cantidad de chicos.",{"vars":{"n":{"min":3,"max":9},"k":{"min":4,"max":15}},"calculadas":{"t":"n*k"}}),
     MC("Hay 36 sillas. ¿En cuál de estas filas iguales NO se pueden acomodar sin que sobre ninguna?",["4 por fila","6 por fila","8 por fila","9 por fila"],"8 por fila","8 no es divisor de 36: 36 = 8 × 4 + 4.")],
"5":[VF("Relámpago. 36 es múltiplo de 9.","Verdadero","36 = 9 × 4.",tiempo=20),
     N("Relámpago. ¿Cuántos divisores tiene 16?",{"acepta":[5]},"1, 2, 4, 8 y 16.",tiempo=35),
     MC("Relámpago. Si 4 divide a 20 y a 12, ¿divide a 20 + 12?",["Sí","No"],"Sí","Si divide a los dos sumandos, divide a la suma: 32 = 4 × 8.",tiempo=20),
     N("Relámpago. Calculá 3 + 4 × 2 elevado a 2.",{"acepta":[19]},"Primero la potencia: 4 × 4 = 16; 3 + 16 = 19 (repaso de la misión 4).",tiempo=40)],
}
EXAMEN=[
 [1,N("¿Cuántos múltiplos de 6 hay entre 1 y 50?",{"acepta":[8]},"6, 12, 18, 24, 30, 36, 42 y 48.")],
 [1,MC("¿Cuál de estos números es múltiplo común de 4 y de 6?",["18","20","30","36"],"36","36 = 4 × 9 = 6 × 6.")],
 [1,VF("Los múltiplos de un número son infinitos.","Verdadero","Siempre se puede multiplicar por un número más grande.")],
 [2,N("¿Cuántos divisores tiene 36?",{"acepta":[9]},"1, 2, 3, 4, 6, 9, 12, 18 y 36.")],
 [2,{"t":"fill_blank","p":"Los divisores de 21 son 1, 3, ___ y ___.","o":[],"r":{"huecos":[["7"],["21"]]},"e":"21 = 1 × 21 = 3 × 7."}],
 [2,MC("¿Cuál de estos números NO es divisor de 48?",["6","8","12","18"],"18","48 ÷ 18 da 2 y sobran 12.")],
 [3,VF("Si 5 divide a 15 y a 25, entonces 5 divide a 40.","Verdadero","15 + 25 = 40, y si divide a los dos sumandos divide a la suma.")],
 [3,N("¿Cuál es el resto de dividir 25 + 14 por 5?",{"acepta":[4]},"39 = 5 × 7 + 4. El 5 no divide a 14.")],
 [3,MC("Un número divisible por 2 y por 6, ¿es siempre divisible por 12?",["Sí, siempre","No: 6 es un contraejemplo","No: 24 es un contraejemplo","Solo si es par"],"No: 6 es un contraejemplo","6 es divisible por 2 y por 6, pero no por 12.")],
 [4,N("Hay 48 alumnos y se forman grupos iguales de entre 5 y 7 alumnos, sin que sobre nadie. ¿De cuántos alumnos es cada grupo?",{"acepta":[6]},"De 5, 6 y 7, solo el 6 divide a 48.")],
 [4,N("Un número está entre 40 y 60 y es múltiplo de 7 y de 3. ¿Cuál es?",{"acepta":[42]},"Múltiplos de 21: 21, 42, 63. Entre 40 y 60 está 42.")],
 [4,N("¿Cuántas cajas de 8 alfajores se llenan completas con 100 alfajores?",{"acepta":[12]},"100 = 8 × 12 + 4: se llenan 12 cajas y sobran 4.")],
 [4,{"t":"classify","p":"Clasificá cada situación según lo que hay que buscar.","o":{"elementos":["Repartir 24 figuritas en partes iguales","Cuántos huevos hay en maples de 12 llenos","Cuántas personas sentar por mesa para ubicar 30 sin que sobre nadie","Cuántas ruedas hay en total en varios autos"],"categorias":["Divisores","Múltiplos"]},"r":{"categorias":{"Repartir 24 figuritas en partes iguales":"Divisores","Cuántos huevos hay en maples de 12 llenos":"Múltiplos","Cuántas personas sentar por mesa para ubicar 30 sin que sobre nadie":"Divisores","Cuántas ruedas hay en total en varios autos":"Múltiplos"}},"e":"Total fijo: divisores. Tamaño del grupo fijo: múltiplos."}],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":5,"practica":"Práctica general: múltiplos y divisores","examen_titulo":"Nivel jefe: múltiplos y divisores",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-5.json"),"w"),ensure_ascii=False)
print("ok")
