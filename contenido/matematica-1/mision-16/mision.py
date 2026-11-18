# -*- coding: utf-8 -*-
"""Matemática I · Misión 16 · Ecuaciones de primer grado sencillas. Genera mision-16.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mision-4"))
from base import *
neg=lambda n:["-%s"%n,"−%s"%n]
SI=["si","sí"]
N1={
"objetivo":"Vas a poder reconocer una ecuación, entender qué es su solución y verificar si un número es solución.",
"vas_a_ver":["Igualdad y ecuación","Incógnita y solución","Verificar reemplazando","Ecuaciones como balanzas"],
"secciones":[
 S(1,"Igualdad y ecuación",[
  D("Ecuación","Una <b>ecuación</b> es una igualdad con un número desconocido, la <b>incógnita</b>, representado por una letra: x + 4 = 7."),
  T("¿Qué es cada cosa?",["Escritura","Es"],[["3 + 4 = 7","Igualdad numérica"],["x + 4 = 7","Ecuación"],["2x + 1","Expresión (no tiene =)"]]),
  P("Cada lado del = es un <b>miembro</b>. El signo = no significa \"da como resultado\": significa que los dos miembros valen lo mismo."),
 ]),
 S(1,"Solución",[
  D("Solución","La <b>solución</b> de una ecuación es el valor de la incógnita que hace verdadera la igualdad. En x + 4 = 7, la solución es x = 3."),
 ]),
 S(2,"Verificar",[
  P("Para saber si un número es solución, se <b>reemplaza</b> y se comprueba que los dos miembros den igual."),
  E("¿4 o 5?","Ecuación 3x − 5 = 7.",["Con x = 4: 3 × 4 − 5 = 12 − 5 = 7. Da 7: es solución.","Con x = 5: 3 × 5 − 5 = 10. No da 7: no es solución."]),
 ]),
 S(2,"Balanzas",[
  P("Una ecuación es como una balanza en equilibrio: los dos platillos pesan lo mismo. Si sacás o agregás lo mismo de los dos lados, sigue en equilibrio. Esa idea sirve para resolverlas."),
 ]),
],
"ejemplo_completo":{"titulo":"la balanza","planteo":"En un platillo hay 3 bolsitas iguales y una pesa de 2 kg; en el otro, 14 kg. La balanza está en equilibrio. ¿Cuánto pesa cada bolsita?","pasos":["Ecuación: 3x + 2 = 14.","Sacamos 2 kg de cada platillo: 3x = 12.","Repartimos en 3: x = 4.","Verificación: 3 × 4 + 2 = 14. Cada bolsita pesa 4 kg."]},
"ejemplo_incompleto":{"titulo":"verificar 2x + 3 = 11","planteo":"¿Es 4 solución de 2x + 3 = 11? Completá los espacios.","pasos":["2 × 4 + 3 = ___ .","¿Es solución? ___ ."]},
"ejemplo_solo":{"titulo":"¿cuál es solución?","planteo":"¿Cuál de los números 2, 3 o 6 es solución de 5x − 4 = 11?"},
"tip":{"titulo":"Verificá siempre","texto":"Reemplazar la solución en la ecuación te asegura que está bien. Lleva un minuto."},
"ojo":["Confundir ecuación con expresión: sin el signo = no hay ecuación.","No verificar: un error de cuenta pasa desapercibido."],
"resumen":[{"titulo":"Ecuación","texto":"Igualdad con incógnita. Ej.: x + 4 = 7."},{"titulo":"Solución","texto":"Valor que la hace verdadera. Ej.: x = 3."},{"titulo":"Verificar","texto":"Reemplazar y comparar los miembros."},{"titulo":"Balanza","texto":"Lo mismo de los dos lados."}],
"glosario":[{"palabra":"Ecuación","significado":"Igualdad con un número desconocido."},{"palabra":"Incógnita","significado":"El número desconocido, escrito con una letra."},{"palabra":"Solución","significado":"El valor que hace verdadera la ecuación."},{"palabra":"Miembro","significado":"Cada lado del signo =."}],
"carpeta":["¿Qué valor de x hace verdadera x + 9 = 15?","¿Es 7 solución de 2x − 4 = 10? Respondé sí o no.","Una balanza en equilibrio tiene 4 cajas iguales en un platillo y 20 kg en el otro. ¿Cuánto pesa cada caja?","Un compañero dice que 5 es solución de 3x + 1 = 14. ¿Cuánto da 3 × 5 + 1?"],
"respuestas_carpeta":[["6"],SI,["5"],["16"]],
"soluciones":{"incompleto":"11. Sí.","solo":"Con 3: 5 × 3 − 4 = 11. La solución es 3.","carpeta":["6: 6 + 9 = 15.","Sí: 2 × 7 − 4 = 10.","5 kg: 4 × 5 = 20.","16: no da 14, así que 5 no es solución."]}
}
N2={
"objetivo":"Vas a poder resolver ecuaciones de la forma ax + b = c usando operaciones inversas en los dos miembros, también con números enteros.",
"vas_a_ver":["Operaciones inversas","Hacer lo mismo en los dos miembros","Resolver paso a paso","Ecuaciones con enteros","Verificar"],
"secciones":[
 S(1,"Operaciones inversas",[
  D("Despejar","Para encontrar x se <b>deshacen</b> las operaciones con su inversa (suma ↔ resta, multiplicación ↔ división), <b>haciendo lo mismo en los dos miembros</b>. Primero se saca lo que se suma o resta; después, lo que multiplica."),
 ]),
 S(1,"Paso a paso",[
  E("3x + 5 = 20","Deshacemos en orden.",["Restamos 5 en los dos miembros: 3x = 15.","Dividimos por 3 en los dos miembros: x = 5.","Verificación: 3 × 5 + 5 = 20."]),
 ]),
 S(2,"Con enteros",[
  E("Soluciones negativas","Dos ecuaciones.",["2x − 7 = −13: sumamos 7: 2x = −6; dividimos por 2: x = −3. Verificación: 2 × (−3) − 7 = −13.","−4x + 1 = 9: restamos 1: −4x = 8; dividimos por −4: x = −2. Verificación: −4 × (−2) + 1 = 9."]),
 ]),
 S(2,"Verificar",[
  P("Al final, siempre reemplazá la solución en la ecuación original. Si los dos miembros no dan igual, revisá los pasos: muchas veces el error está en un signo."),
 ]),
],
"ejemplo_completo":{"titulo":"5x − 8 = 27","planteo":"Resolvé y verificá.","pasos":["Sumamos 8 en los dos miembros: 5x = 35.","Dividimos por 5: x = 7.","Verificación: 5 × 7 − 8 = 35 − 8 = 27."]},
"ejemplo_incompleto":{"titulo":"4x + 6 = 30","planteo":"Completá los espacios.","pasos":["Restamos 6: 4x = ___ .","Dividimos por 4: x = ___ ."]},
"ejemplo_solo":{"titulo":"3x + 11 = 2","planteo":"Resolvé y verificá."},
"tip":{"titulo":"Primero lo que suma, después lo que multiplica","texto":"Es al revés que la jerarquía: para deshacer, empezás por la suma o la resta."},
"ojo":["Operar de un solo lado: si restás 6 a la izquierda, tenés que restar 6 a la derecha.","Equivocar el signo: en 2x − 7 = −13, para sacar el −7 se suma 7."],
"resumen":[{"titulo":"Inversas","texto":"Suma ↔ resta; multiplicación ↔ división."},{"titulo":"Mismo en los dos","texto":"Lo que hacés de un lado, lo hacés del otro."},{"titulo":"Orden","texto":"Primero sacar b, después dividir por a."},{"titulo":"Verificar","texto":"Reemplazar al final."}],
"glosario":[{"palabra":"Despejar","significado":"Dejar sola la incógnita."},{"palabra":"Operación inversa","significado":"La que deshace a otra."},{"palabra":"Coeficiente","significado":"El número que multiplica a la incógnita."}],
"carpeta":["Resolvé 2x + 3 = 17.","Resolvé 6x − 4 = 32.","Resolvé 3x + 10 = 1.","Un compañero resolvió 2x + 6 = 20 restando 6 solo del lado izquierdo y le dio x = 10. ¿Cuál es la solución correcta?"],
"respuestas_carpeta":[["7"],["6"],neg(3),["7"]],
"soluciones":{"incompleto":"24. 6.","solo":"Restamos 11: 3x = −9. Dividimos por 3: x = −3. Verificación: 3 × (−3) + 11 = 2.","carpeta":["7: 2x = 14.","6: 6x = 36.","−3: 3x = −9.","7: restando 6 de los dos lados, 2x = 14."]}
}
N3={
"objetivo":"Vas a poder resolver ecuaciones con la incógnita en los dos miembros, juntando las x de un lado y los números del otro.",
"vas_a_ver":["Ecuaciones con x en los dos miembros","Juntar los términos con x","Juntar los números","Verificar"],
"secciones":[
 S(1,"x en los dos miembros",[
  D("Estrategia","Se juntan los <b>términos con x en un miembro</b> y los <b>números en el otro</b>, haciendo siempre la misma operación en los dos lados."),
  E("5x + 3 = 2x + 18","Paso a paso.",["Restamos 2x en los dos miembros: 3x + 3 = 18.","Restamos 3: 3x = 15.","Dividimos por 3: x = 5.","Verificación: 5 × 5 + 3 = 28 y 2 × 5 + 18 = 28."]),
 ]),
 S(1,"\"Pasar\" un término",[
  D("Pasar de miembro","Decir que un término \"pasa al otro miembro con la operación contraria\" es una forma corta de hacer lo mismo en los dos lados: un +2x pasa como −2x."),
 ]),
 S(2,"Con negativos",[
  E("2x + 9 = 5x − 3","Conviene juntar las x donde quedan positivas.",["Restamos 2x: 9 = 3x − 3.","Sumamos 3: 12 = 3x.","Dividimos por 3: x = 4.","Verificación: 2 × 4 + 9 = 17 y 5 × 4 − 3 = 17."]),
 ]),
 S(2,"Verificar",[
  P("Con x en los dos miembros es fácil equivocarse con un signo: calculá cada miembro por separado con la solución y compará."),
 ]),
],
"ejemplo_completo":{"titulo":"6x − 5 = 2x + 7","planteo":"Resolvé y verificá.","pasos":["Restamos 2x: 4x − 5 = 7.","Sumamos 5: 4x = 12.","Dividimos por 4: x = 3.","Verificación: 6 × 3 − 5 = 13 y 2 × 3 + 7 = 13."]},
"ejemplo_incompleto":{"titulo":"8x + 1 = 3x + 21","planteo":"Completá los espacios.","pasos":["Restamos 3x: ___ + 1 = 21.","Restamos 1: 5x = ___ .","Dividimos por 5: x = ___ ."]},
"ejemplo_solo":{"titulo":"x + 14 = 4x − 1","planteo":"Resolvé y verificá."},
"tip":{"titulo":"Mové la x más chica","texto":"Restá la x que tenga menor coeficiente: así la incógnita te queda con coeficiente positivo."},
"ojo":["Cambiar mal el signo al pasar: en 6x + 2 = 4x + 10, el 4x pasa restando: 2x = 8.","Sumar términos distintos: 3x + 3 no es 6x."],
"resumen":[{"titulo":"Estrategia","texto":"x de un lado, números del otro."},{"titulo":"Pasar","texto":"Con la operación contraria."},{"titulo":"Ejemplo","texto":"5x + 3 = 2x + 18 → x = 5."},{"titulo":"Verificar","texto":"Cada miembro por separado."}],
"glosario":[{"palabra":"Miembro","significado":"Cada lado de la ecuación."},{"palabra":"Término independiente","significado":"Número sin letra."},{"palabra":"Agrupar","significado":"Juntar términos del mismo tipo."}],
"carpeta":["Resolvé 4x + 2 = x + 14.","Resolvé 9x − 5 = 4x + 20.","Resolvé 2x + 1 = 5x + 10.","Un compañero, en 6x + 2 = 4x + 10, pasó el 4x sumando y le quedó 10x = 8. ¿Cuál es la solución correcta?"],
"respuestas_carpeta":[["4"],["5"],neg(3),["4"]],
"soluciones":{"incompleto":"5x. 20. 4.","solo":"Restamos x: 14 = 3x − 1. Sumamos 1: 15 = 3x. x = 5. Verificación: 19 = 19.","carpeta":["4: 3x = 12.","5: 5x = 25.","−3: 1 − 10 = 5x − 2x; −9 = 3x.","4: el 4x pasa restando: 2x = 8."]}
}
N4={
"objetivo":"Vas a poder resolver problemas planteando una ecuación, resolviéndola, verificándola y respondiendo con la unidad correcta.",
"vas_a_ver":["Elegir la incógnita","Plantear la ecuación","Resolver y verificar","Interpretar y responder","Problemas de edades, dinero y geometría"],
"secciones":[
 S(1,"Cinco pasos",[
  D("Resolver un problema con ecuaciones","1) Elegir qué es x. 2) Escribir los otros datos con x. 3) Plantear la ecuación. 4) Resolver y verificar. 5) <b>Responder</b> la pregunta con la unidad."),
 ]),
 S(1,"Edades",[
  E("Juan y su hermano","Juan tiene el triple de la edad de su hermano. Juntos suman 32 años.",["x: edad del hermano. Juan: 3x.","x + 3x = 32, o sea 4x = 32.","x = 8.","El hermano tiene 8 años y Juan, 3 × 8 = 24 años."]),
 ]),
 S(2,"Dinero",[
  E("Los cuadernos","Pagué $5.300 por 3 cuadernos iguales y una lapicera de $800.",["x: precio de un cuaderno.","3x + 800 = 5.300.","3x = 4.500, x = 1.500.","Cada cuaderno cuesta $1.500."]),
 ]),
 S(2,"Geometría",[
  E("El rectángulo","El largo mide 4 cm más que el ancho y el perímetro es 40 cm.",["x: ancho. Largo: x + 4.","Perímetro: x + x + x + 4 + x + 4 = 4x + 8.","4x + 8 = 40, 4x = 32, x = 8.","Ancho 8 cm y largo 12 cm. Verificación: 8 + 8 + 12 + 12 = 40."]),
 ]),
],
"ejemplo_completo":{"titulo":"un número y su doble","planteo":"Un número sumado con su doble da 45. ¿Cuál es el número?","pasos":["x: el número. Su doble: 2x.","x + 2x = 45, o sea 3x = 45.","x = 15.","Verificación: 15 + 30 = 45. El número es 15."]},
"ejemplo_incompleto":{"titulo":"la lapicera","planteo":"Pagué $5.300 por 3 cuadernos iguales y una lapicera de $800. Completá los espacios.","pasos":["3x + 800 = 5.300.","3x = ___ .","x = ___ ."]},
"ejemplo_solo":{"titulo":"las hermanas","planteo":"Sofía tiene $200 más que Lucía y entre las dos tienen $1.400. ¿Cuánto tiene cada una?"},
"tip":{"titulo":"Volvé a la pregunta","texto":"Cuando encontrás x, releé qué pregunta el problema: a veces la respuesta no es x sino 3x o x + 4."},
"ojo":["Dar la solución sin interpretarla: si x es la edad del hermano, la de Juan es 3x.","No controlar el sentido: una edad, un precio o un largo no pueden ser negativos."],
"resumen":[{"titulo":"Plantear","texto":"Elegir x y escribir los datos con x."},{"titulo":"Resolver","texto":"Operaciones inversas en los dos miembros."},{"titulo":"Verificar","texto":"Con los datos del enunciado."},{"titulo":"Responder","texto":"Con la unidad y lo que se pregunta."}],
"glosario":[{"palabra":"Plantear","significado":"Escribir la ecuación a partir del enunciado."},{"palabra":"Interpretar","significado":"Explicar qué significa la solución en el problema."},{"palabra":"Perímetro","significado":"La medida del borde de una figura."}],
"carpeta":["Un número multiplicado por 4 y aumentado en 6 da 50. ¿Cuál es el número?","La suma de dos números consecutivos es 37. ¿Cuál es el menor?","Sofía tiene $200 más que Lucía y entre las dos tienen $1.400. ¿Cuánto tiene Lucía?","En el problema de Juan (el triple de su hermano, suman 32), un compañero respondió que Juan tiene 8 años. ¿Cuántos años tiene Juan?"],
"respuestas_carpeta":[["11"],["18"],["600"],["24"]],
"soluciones":{"incompleto":"4.500. 1.500.","solo":"x + x + 200 = 1.400; 2x = 1.200; x = 600. Lucía tiene $600 y Sofía $800.","carpeta":["11: 4x + 6 = 50; 4x = 44.","18: x + x + 1 = 37; 2x = 36.","$600: x + x + 200 = 1.400.","24: x = 8 es el hermano; Juan tiene 3 × 8."]}
}
ACT={
"1":[MC("¿Cuál de estas es una ecuación?",["3 + 4 = 7","2x + 1","x + 5 = 9","5 > 3"],"x + 5 = 9","Tiene un signo = y una incógnita."),
     N("¿Qué número hace verdadera la igualdad x − 6 = 13?",{"acepta":[19]},"19 − 6 = 13.")],
"2":[N("Resolvé {a}x + {b} = {c}. Escribí el valor de x.",{"formula":"s"},"Se resta el número y se divide por el coeficiente.",{"vars":{"a":{"min":2,"max":9},"s":{"min":1,"max":12},"b":{"min":1,"max":20}},"calculadas":{"c":"a*s+b"}}),
     {"t":"tap_text","p":"Detective del error: tocá el paso que está mal y escribí el valor correcto de x.","o":{"modo":"palabras","segmentos":["2x + 6 = 20","→","2x = 26","→","x = 13"],"pide_correccion":"Escribí el valor correcto de x"},"r":{"tocar":[2],"correccion":["7"]},"e":"Para sacar el +6 hay que restar 6: 2x = 14, x = 7."}],
"3":[N("Resolvé 7x − 4 = 3x + 12. Escribí el valor de x.",{"acepta":[4]},"4x = 16."),
     MC("En 5x + 3 = 2x + 18, ¿qué conviene hacer primero para juntar las x?",["Restar 2x en los dos miembros","Sumar 2x en los dos miembros","Dividir por 5","Restar 18"],"Restar 2x en los dos miembros","Así las x quedan de un solo lado: 3x + 3 = 18.")],
"4":[N("El doble de un número más 7 es 31. ¿Cuál es el número?",{"acepta":[12]},"2x + 7 = 31; 2x = 24."),
     N("La suma de un número y su triple es 60. ¿Cuál es el número?",{"acepta":[15]},"x + 3x = 60; 4x = 60.")],
"5":[N("Relámpago. Resolvé x + 8 = 20.",{"acepta":[12]},"Se resta 8.",tiempo=20),
     N("Relámpago. Resolvé 3x = 21.",{"acepta":[7]},"Se divide por 3.",tiempo=20),
     VF("Relámpago. En una ecuación se hace la misma operación en los dos miembros.","Verdadero","Como en una balanza.",tiempo=20),
     N("Relámpago. Si n = 4, ¿cuánto vale 2n + 3?",{"acepta":[11]},"Repaso de la misión 15.",tiempo=25)],
}
EXAMEN=[
 [1,VF("x = 3 es solución de 4x − 2 = 10.","Verdadero","4 × 3 − 2 = 10.")],
 [1,MC("En la ecuación 2x + 5 = 13, ¿qué es x?",["La incógnita","La solución","Un coeficiente","El resultado"],"La incógnita","Es el número desconocido.")],
 [1,N("Una balanza en equilibrio tiene 5 paquetes iguales en un platillo y 35 kg en el otro. ¿Cuánto pesa cada paquete?",{"acepta":[7]},"5x = 35.")],
 [2,N("Resolvé 4x − 9 = 23. Escribí el valor de x.",{"acepta":[8]},"4x = 32.")],
 [2,N("Resolvé 2x + 15 = 5. Escribí el valor de x.",{"acepta":[-5]},"2x = −10.")],
 [2,{"t":"ordering","p":"Ordená los pasos para resolver 3x + 4 = 19.","o":["Dividir por 3: x = 5","Verificar: 3 × 5 + 4 = 19","Restar 4 en los dos miembros: 3x = 15"],"r":{"orden":["Restar 4 en los dos miembros: 3x = 15","Dividir por 3: x = 5","Verificar: 3 × 5 + 4 = 19"]},"e":"Primero se saca el número, después se divide y al final se verifica."}],
 [3,N("Resolvé 5x + 1 = 2x + 16. Escribí el valor de x.",{"acepta":[5]},"3x = 15.")],
 [3,N("Resolvé 3x − 7 = 5x + 1. Escribí el valor de x.",{"acepta":[-4]},"−7 − 1 = 5x − 3x; −8 = 2x.")],
 [3,MC("En 3x = −2x + 10, al pasar el −2x al primer miembro, queda…",["x = 10","5x = 10","3x − 2x = 10","−5x = 10"],"5x = 10","−2x pasa sumando: 3x + 2x = 10.")],
 [4,N("Un número aumentado en su mitad da 30. ¿Cuál es el número?",{"acepta":[20]},"x + x/2 = 30: 20 + 10 = 30.")],
 [4,N("Tres cuadernos iguales y una regla de $500 cuestan $4.100. ¿Cuánto cuesta cada cuaderno?",{"acepta":[1200]},"3x + 500 = 4.100; 3x = 3.600.")],
 [4,N("El largo de un rectángulo mide 3 cm más que el ancho y su perímetro es 30 cm. ¿Cuánto mide el ancho, en cm?",{"acepta":[6]},"4x + 6 = 30; 4x = 24.")],
 [4,MC("Después de resolver una ecuación de un problema y obtener x = 8, ¿qué falta hacer?",["Nada","Interpretar qué es x en el problema y responder","Dividir por 8","Sumar 8"],"Interpretar qué es x en el problema y responder","La respuesta puede ser x o algo que depende de x.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":16,"practica":"Práctica general: ecuaciones","examen_titulo":"Nivel jefe: ecuaciones",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-16.json"),"w"),ensure_ascii=False)
print("ok")
