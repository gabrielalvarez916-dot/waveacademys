# -*- coding: utf-8 -*-
"""Matemática I · Misión 4 · Operaciones combinadas. Genera mision-4.json (se carga con cargar_mision)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
N1={
"objetivo":"Vas a poder resolver cálculos con varias operaciones respetando el orden correcto: primero multiplicaciones y divisiones, después sumas y restas.",
"vas_a_ver":["Por qué importa el orden de las operaciones","La jerarquía: × y ÷ antes que + y −","Operaciones del mismo nivel: de izquierda a derecha","Separar en términos","Cálculos con y sin paréntesis"],
"secciones":[
 S(1,"La jerarquía de las operaciones",[
  D("Jerarquía","En un cálculo con varias operaciones, <b>primero se resuelven las multiplicaciones y divisiones</b>, y <b>después las sumas y restas</b>. Así todos obtienen el mismo resultado."),
  T("Un mismo cálculo, dos órdenes",["Cálculo","Orden correcto","Orden incorrecto"],[["5 + 3 × 4","5 + 12 = 17","8 × 4 = 32"]],"Solo 17 es correcto: la multiplicación va antes que la suma."),
 ]),
 S(1,"Mismo nivel: de izquierda a derecha",[
  D("Operaciones del mismo nivel","Si hay solo multiplicaciones y divisiones, o solo sumas y restas, se resuelven <b>en el orden en que aparecen, de izquierda a derecha</b>."),
  P("Ejemplos: 24 ÷ 4 × 2 = 6 × 2 = 12 (no 24 ÷ 8 = 3). 20 − 8 + 3 = 12 + 3 = 15 (no 20 − 11 = 9)."),
 ]),
 S(2,"Separar en términos",[
  P("Los signos + y − <b>separan el cálculo en términos</b>. Cada término se resuelve por separado y al final se suman y restan los resultados."),
  E("Separar 6 × 2 + 20 ÷ 4 − 3","Marcamos los términos.",["Términos: 6 × 2 | 20 ÷ 4 | 3.","6 × 2 = 12 y 20 ÷ 4 = 5.","12 + 5 − 3 = 14."]),
 ]),
 S(2,"Con y sin paréntesis",[
  P("Los <b>paréntesis</b> cambian el orden: lo que está adentro se resuelve primero. Por eso el mismo cálculo puede dar distinto con paréntesis o sin ellos."),
  E("Comparar","Los mismos números, distinto orden.",["5 + 3 × 4 = 5 + 12 = 17.","(5 + 3) × 4 = 8 × 4 = 32.","El paréntesis obligó a sumar primero."]),
 ]),
],
"ejemplo_completo":{"titulo":"40 − 3 × 5 + 18 ÷ 6","planteo":"Resolvé separando en términos.","pasos":["Términos: 40 | 3 × 5 | 18 ÷ 6.","3 × 5 = 15.","18 ÷ 6 = 3.","40 − 15 + 3: de izquierda a derecha, 40 − 15 = 25 y 25 + 3 = 28.","Resultado: 28."]},
"ejemplo_incompleto":{"titulo":"7 × 3 + 36 ÷ 9 − 5","planteo":"Resolvé separando en términos. Completá los espacios.","pasos":["7 × 3 = ___ .","36 ÷ 9 = ___ .","21 + 4 − 5 = ___ ."]},
"ejemplo_solo":{"titulo":"100 − 6 × 8 + 45 ÷ 5","planteo":"Resolvé separando en términos."},
"tip":{"titulo":"Marcá los términos","texto":"Antes de calcular, hacé una rayita vertical en cada + y −. Cada parte que queda es un término que resolvés por separado."},
"ojo":["Resolver todo de izquierda a derecha: en 10 + 5 × 2, sumar primero da 30, pero el resultado es 20.","Dividir mal entre operaciones del mismo nivel: 24 ÷ 4 × 2 es 12, no 3."],
"resumen":[{"titulo":"Jerarquía","texto":"Primero × y ÷, después + y −. Ej.: 5 + 3 × 4 = 17."},{"titulo":"Mismo nivel","texto":"De izquierda a derecha. Ej.: 24 ÷ 4 × 2 = 12."},{"titulo":"Términos","texto":"Los separan + y −. Cada uno se resuelve aparte."},{"titulo":"Paréntesis","texto":"Lo de adentro va primero. Ej.: (5 + 3) × 4 = 32."}],
"glosario":[{"palabra":"Jerarquía","significado":"El orden en que se resuelven las operaciones."},{"palabra":"Término","significado":"Cada parte de un cálculo separada por + o −."},{"palabra":"Cálculo combinado","significado":"Cuenta con más de una operación."},{"palabra":"Paréntesis","significado":"Signo ( ) que indica qué resolver primero."},{"palabra":"Nivel","significado":"Grupo de operaciones con la misma prioridad."}],
"carpeta":["Calculá 8 + 2 × 6.","Calculá 30 ÷ 5 × 3.","Calculá 50 − 4 × 7 + 12 ÷ 3.","Un compañero resolvió 10 + 5 × 2 y le dio 30. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["20"],["18"],["26"],["20"]],
"soluciones":{"incompleto":"21. 4. 21 + 4 − 5 = 20.","solo":"6 × 8 = 48 y 45 ÷ 5 = 9. 100 − 48 + 9 = 61.","carpeta":["20: 2 × 6 = 12 y 8 + 12 = 20.","18: de izquierda a derecha, 30 ÷ 5 = 6 y 6 × 3 = 18.","26: 4 × 7 = 28 y 12 ÷ 3 = 4. 50 − 28 + 4 = 26.","20: primero 5 × 2 = 10, después 10 + 10 = 20. Sumó antes de multiplicar."]}
}
N2={
"objetivo":"Vas a poder resolver cálculos con paréntesis, corchetes y llaves, ubicar paréntesis para obtener un resultado y escribir enunciados como cálculos.",
"vas_a_ver":["Paréntesis, corchetes y llaves","Resolver de adentro hacia afuera","Dónde agregar paréntesis para obtener un resultado","Pasar un enunciado a un cálculo"],
"secciones":[
 S(1,"Signos de agrupación",[
  D("Signos de agrupación","Los <b>paréntesis ( )</b>, <b>corchetes [ ]</b> y <b>llaves { }</b> agrupan partes de un cálculo que se resuelven primero. Cuando hay uno adentro de otro, se usan en ese orden: ( ) adentro, [ ] en el medio, { } afuera."),
  P("Adentro de cada signo se respeta la jerarquía de siempre: primero × y ÷, después + y −."),
 ]),
 S(1,"De adentro hacia afuera",[
  D("Orden de resolución","Se resuelve <b>primero el paréntesis, después el corchete y al final la llave</b>: de adentro hacia afuera."),
  E("Resolver [(3 + 5) × 2 − 4] ÷ 3","Vamos de adentro hacia afuera.",["Paréntesis: 3 + 5 = 8.","Corchete: 8 × 2 − 4 = 16 − 4 = 12.","Afuera: 12 ÷ 3 = 4."]),
 ]),
 S(2,"Agregar paréntesis",[
  P("Mover o agregar paréntesis cambia el resultado. A veces te piden <b>ubicarlos para que el cálculo dé un número dado</b>: probás dónde ponerlos y calculás."),
  E("¿Dónde van los paréntesis?","Queremos que 12 − 4 ÷ 2 dé 4.",["Sin paréntesis: 12 − 2 = 10. No sirve.","Con (12 − 4) ÷ 2: 8 ÷ 2 = 4. ¡Sirve!"]),
 ]),
 S(2,"De enunciado a cálculo",[
  P("Las palabras dicen qué se agrupa. \"El doble de la suma\" obliga a sumar primero, así que la suma va entre paréntesis."),
  E("Traducir","Dos enunciados.",["El doble de la suma de 7 y 8: 2 × (7 + 8) = 2 × 15 = 30.","A 50 restale el triple de 6: 50 − 3 × 6 = 50 − 18 = 32 (no hace falta paréntesis)."]),
 ]),
],
"ejemplo_completo":{"titulo":"2 × {30 − [4 × (6 − 1) + 3]}","planteo":"Resolvé de adentro hacia afuera.","pasos":["Paréntesis: 6 − 1 = 5.","Corchete: 4 × 5 + 3 = 20 + 3 = 23.","Llave: 30 − 23 = 7.","Afuera: 2 × 7 = 14."]},
"ejemplo_incompleto":{"titulo":"[(9 + 3) ÷ 4 + 5] × 2","planteo":"Resolvé de adentro hacia afuera. Completá los espacios.","pasos":["Paréntesis: 9 + 3 = ___ .","Corchete: 12 ÷ 4 + 5 = ___ .","Afuera: 8 × 2 = ___ ."]},
"ejemplo_solo":{"titulo":"100 − {5 × [2 + (12 − 4)]}","planteo":"Resolvé de adentro hacia afuera."},
"tip":{"titulo":"Reescribí en cada paso","texto":"Cada vez que resolvés un signo de agrupación, copiá el cálculo de nuevo con ese resultado. Así no te salteás nada."},
"ojo":["Resolver afuera antes que adentro: en 2 × [10 − (3 + 1)], hacer primero 2 × 10 da 16, pero es 2 × 6 = 12.","Saltear un signo anidado: si hay ( ) adentro de [ ], el paréntesis va primero."],
"resumen":[{"titulo":"Signos","texto":"( ) adentro, [ ] en el medio, { } afuera."},{"titulo":"Orden","texto":"De adentro hacia afuera. Ej.: [(3 + 5) × 2 − 4] ÷ 3 = 4."},{"titulo":"Agregar paréntesis","texto":"Cambia el resultado. Ej.: (12 − 4) ÷ 2 = 4."},{"titulo":"Enunciados","texto":"\"El doble de la suma\": 2 × (7 + 8)."}],
"glosario":[{"palabra":"Paréntesis","significado":"Signo ( ) que agrupa lo que se resuelve primero."},{"palabra":"Corchete","significado":"Signo [ ] que agrupa a un paréntesis."},{"palabra":"Llave","significado":"Signo { } que agrupa a un corchete."},{"palabra":"Anidado","significado":"Que está adentro de otro."},{"palabra":"Doble, triple","significado":"Multiplicar por 2, por 3."}],
"carpeta":["Calculá (7 + 3) × 4.","Calculá [20 − (2 + 3) × 2] ÷ 5.","Escribí el cálculo y resolvé: el triple de la diferencia entre 15 y 9.","Un compañero resolvió 2 × [10 − (3 + 1)] haciendo primero 2 × 10 y le dio 16. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["40"],["2"],["18"],["12"]],
"soluciones":{"incompleto":"12. 3 + 5 = 8. 16.","solo":"12 − 4 = 8; 2 + 8 = 10; 5 × 10 = 50; 100 − 50 = 50.","carpeta":["40: 10 × 4.","2: (2 + 3) × 2 = 10; 20 − 10 = 10; 10 ÷ 5 = 2.","18: 3 × (15 − 9) = 3 × 6 = 18.","12: 3 + 1 = 4; 10 − 4 = 6; 2 × 6 = 12."]}
}
N3={
"objetivo":"Vas a poder resolver cálculos combinados que tienen potencias y raíces, en el orden correcto y escribiendo el paso a paso.",
"vas_a_ver":["El orden completo: paréntesis, potencias y raíces, × y ÷, + y −","La raíz como signo de agrupación","Cálculos largos con una igualdad por línea","Cómo verificar el resultado"],
"secciones":[
 S(1,"El orden completo",[
  D("Jerarquía completa","1.º lo que está entre <b>paréntesis</b>; 2.º <b>potencias y raíces</b>; 3.º <b>multiplicaciones y divisiones</b>; 4.º <b>sumas y restas</b>."),
  T("Antes o después del paréntesis",["Cálculo","Se resuelve","Resultado"],[["3 + 2²","3 + 4","7"],["(3 + 2)²","5²","25"],["3 + 2³ × 5","3 + 8 × 5 = 3 + 40","43"]],"La potencia se aplica solo al número que tiene pegado, salvo que haya un paréntesis."),
 ]),
 S(1,"La raíz agrupa",[
  D("La raíz como agrupación","Todo lo que está <b>debajo de la raíz</b> se resuelve primero, como si estuviera entre paréntesis. Después se saca la raíz."),
  P("Ejemplo: √(16 + 9) = √25 = 5. No se puede sacar la raíz de cada número por separado: √16 + √9 = 4 + 3 = 7, que es otra cosa."),
 ]),
 S(2,"Cálculos largos, paso a paso",[
  P("En un cálculo largo escribí <b>una igualdad por línea</b>: copiás el cálculo con lo que ya resolviste. Cada línea tiene que valer lo mismo que la anterior."),
  E("Resolver 5² − √36 × 2 + 10 ÷ 2","Una igualdad por línea.",["= 25 − 6 × 2 + 10 ÷ 2 (potencias y raíces).","= 25 − 12 + 5 (multiplicación y división).","= 18 (sumas y restas, de izquierda a derecha)."]),
 ]),
 S(2,"Verificar",[
  P("Para controlar, repasá cada línea: ¿resolviste lo que tocaba? ¿Copiaste bien los números que no tocaste? Una forma rápida es volver a calcular cada término por separado y comparar."),
 ]),
],
"ejemplo_completo":{"titulo":"(4 + 2)² ÷ 4 − √(50 − 1)","planteo":"Resolvé con una igualdad por línea.","pasos":["Paréntesis y debajo de la raíz: = 6² ÷ 4 − √49.","Potencia y raíz: = 36 ÷ 4 − 7.","División: = 9 − 7.","Resta: = 2."]},
"ejemplo_incompleto":{"titulo":"2⁴ + √(20 + 5) × 3","planteo":"Resolvé. Completá los espacios.","pasos":["2⁴ = ___ .","√(20 + 5) = √25 = ___ .","16 + 5 × 3 = ___ ."]},
"ejemplo_solo":{"titulo":"10² − 3 × √81 + 2³","planteo":"Resolvé con una igualdad por línea."},
"tip":{"titulo":"Subrayá lo que toca","texto":"En cada línea subrayá lo que vas a resolver según la jerarquía. Lo demás se copia igual."},
"ojo":["Sacar la raíz de cada término: √(9 + 16) es √25 = 5, no 3 + 4 = 7.","Encadenar igualdades falsas: no escribas 3 + 4 = 7 × 2 = 14, porque 3 + 4 no es 14. Una igualdad por línea."],
"resumen":[{"titulo":"Orden","texto":"Paréntesis; potencias y raíces; × y ÷; + y −."},{"titulo":"Potencia","texto":"Solo al número pegado. Ej.: 3 + 2² = 7; (3 + 2)² = 25."},{"titulo":"Raíz","texto":"Agrupa: √(16 + 9) = √25 = 5."},{"titulo":"Paso a paso","texto":"Una igualdad por línea."}],
"glosario":[{"palabra":"Jerarquía","significado":"Orden en que se resuelven las operaciones."},{"palabra":"Igualdad","significado":"Dos expresiones que valen lo mismo, unidas por =."},{"palabra":"Radicando","significado":"Lo que está debajo de la raíz."},{"palabra":"Verificar","significado":"Revisar que cada paso esté bien."}],
"carpeta":["Calculá 4 + 3².","Calculá √(36 + 64).","Calculá 2³ × 5 − √49.","Un compañero calculó √(9 + 16) como 3 + 4 = 7. ¿Cuál es el resultado correcto?"],
"respuestas_carpeta":[["13"],["10"],["33"],["5"]],
"soluciones":{"incompleto":"16. 5. 16 + 15 = 31.","solo":"= 100 − 3 × 9 + 8 = 100 − 27 + 8 = 81.","carpeta":["13: 3² = 9 y 4 + 9 = 13.","10: 36 + 64 = 100 y √100 = 10.","33: 8 × 5 − 7 = 40 − 7 = 33.","5: primero la suma, 9 + 16 = 25, y √25 = 5."]}
}
N4={
"objetivo":"Vas a poder usar la calculadora científica para cálculos combinados, ingresar bien los paréntesis y controlar el resultado con una estimación.",
"vas_a_ver":["Cómo calcula una calculadora científica","Cómo ingresar paréntesis","Estimar antes de calcular","Errores comunes al tipear"],
"secciones":[
 S(1,"La calculadora científica",[
  D("Calculadora científica","La <b>calculadora científica</b> respeta la jerarquía de las operaciones y tiene teclas de paréntesis, potencia y raíz. Muchas calculadoras comunes, en cambio, resuelven a medida que tipeás, de izquierda a derecha."),
  T("El mismo cálculo en dos calculadoras",["Se tipea","Científica","Común"],[["5 + 3 × 4","17","32"]],"Solo 17 es correcto. Con una calculadora común hay que hacer primero la multiplicación."),
 ]),
 S(1,"Ingresar paréntesis",[
  D("Paréntesis en la calculadora","La calculadora no adivina qué querés agrupar: <b>los paréntesis se tipean</b> igual que en la carpeta."),
  P("Para 120 ÷ (4 + 2) se tipea con paréntesis y da 20. Si te los olvidás, la calculadora resuelve 120 ÷ 4 + 2 = 32."),
 ]),
 S(2,"Estimar antes",[
  P("La calculadora <b>controla</b> la cuenta, pero no reemplaza a tu cabeza. Estimá antes: si el resultado queda muy lejos de la estimación, algo se tipeó mal."),
  E("Controlar 498 × 21","Estimamos y comparamos.",["Estimación: 500 × 20 = 10.000.","La calculadora muestra 10.458: está cerca, es razonable.","Si mostrara 4.980, estaría muy lejos: seguro se tipeó mal."]),
 ]),
 S(2,"Errores de tipeo",[
  P("Los errores más comunes: confundir la tecla de potencia con la de multiplicar (3 elevado a 4 es 81, pero 3 × 4 es 12), olvidar un paréntesis o apretar un número de más."),
 ]),
],
"ejemplo_completo":{"titulo":"(365 − 89) × 12","planteo":"Estimá, calculá con la calculadora y controlá.","pasos":["Estimación: 365 − 89 es casi 300; 300 × 10 = 3.000. El resultado tiene que andar por ahí.","Se tipea con paréntesis: (365 − 89) × 12.","La calculadora muestra 3.312: 276 × 12. Está cerca de la estimación.","Sin paréntesis daría 365 − 1.068, un número negativo: ese resultado avisa que falta el paréntesis."]},
"ejemplo_incompleto":{"titulo":"(1.200 + 840) ÷ 15","planteo":"Completá los espacios.","pasos":["Estimación: 2.000 ÷ 20 = ___ .","Con paréntesis, la calculadora muestra ___ .","Sin paréntesis calcula 1.200 + 840 ÷ 15 = 1.200 + 56 = ___ ."]},
"ejemplo_solo":{"titulo":"49 × 51","planteo":"Estimá 49 × 51 y escribí qué resultado tiene que mostrar la calculadora."},
"tip":{"titulo":"Estimá primero, tipeá después","texto":"Si ya sabés más o menos cuánto tiene que dar, un error de tipeo salta a la vista."},
"ojo":["Confiar en la calculadora sin estimar: si tipeaste mal, el resultado está mal aunque lo diga la pantalla.","Confundir la tecla de potencia con la de multiplicar: 2 elevado a 5 es 32, no 10."],
"resumen":[{"titulo":"Científica","texto":"Respeta la jerarquía. Ej.: 5 + 3 × 4 = 17."},{"titulo":"Paréntesis","texto":"Se tipean. Ej.: 120 ÷ (4 + 2) = 20."},{"titulo":"Estimar","texto":"Antes de calcular. Ej.: 498 × 21 ≈ 10.000."},{"titulo":"Errores","texto":"Tecla equivocada, paréntesis olvidado, número de más."}],
"glosario":[{"palabra":"Calculadora científica","significado":"La que respeta la jerarquía y tiene potencia y raíz."},{"palabra":"Tipear","significado":"Escribir con las teclas."},{"palabra":"Estimar","significado":"Calcular aproximadamente."},{"palabra":"Pantalla","significado":"Donde la calculadora muestra el resultado."}],
"carpeta":["Una calculadora científica: ¿qué resultado muestra para 6 + 4 × 5?","¿Qué resultado da 90 ÷ (3 + 6)?","Estimá 302 × 19 redondeando a 300 × 20.","Un compañero quería calcular 2⁵ y tipeó 2 × 5. ¿Qué resultado tenía que obtener?"],
"respuestas_carpeta":[["26"],["10"],["6000"],["32"]],
"soluciones":{"incompleto":"100. 136. 1.256.","solo":"Estimación: 50 × 50 = 2.500. La calculadora tiene que mostrar un número cercano: 2.499.","carpeta":["26: 4 × 5 = 20 y 6 + 20 = 26.","10: 3 + 6 = 9 y 90 ÷ 9 = 10.","6.000: 300 × 20.","32: 2 × 2 × 2 × 2 × 2 = 32. Tipeó multiplicación en vez de potencia."]}
}
ACT={
"1":[N("Calculá {a} + {b} × {c}.",{"formula":"a+b*c"},"Primero la multiplicación, después la suma.",{"vars":{"a":{"min":2,"max":30},"b":{"min":2,"max":9},"c":{"min":2,"max":9}}}),
     {"t":"tap_text","p":"Detective del error: tocá el paso que está mal y escribí el resultado correcto del cálculo.","o":{"modo":"palabras","segmentos":["12 + 3 × 2","=","15 × 2","=","30"],"pide_correccion":"Escribí el resultado correcto"},"r":{"tocar":[2],"correccion":["18"]},"e":"Sumó antes de multiplicar. 3 × 2 = 6 y 12 + 6 = 18."}],
"2":[N("Calculá [{a} − ({b} + {c})] × 2.",{"formula":"(a-(b+c))*2"},"Primero el paréntesis, después el corchete y al final se multiplica.",{"vars":{"a":{"min":20,"max":50},"b":{"min":2,"max":9},"c":{"min":2,"max":9}}}),
     MC("¿Dónde van los paréntesis para que 4 + 6 × 3 dé 30?",["(4 + 6) × 3","4 + (6 × 3)","4 × (6 + 3)","No hacen falta"],"(4 + 6) × 3","(4 + 6) × 3 = 10 × 3 = 30. Sin paréntesis da 22.")],
"3":[N("Calculá {a} elevado a 2 + {b} × 3.",{"formula":"a^2+b*3"},"Primero la potencia, después la multiplicación y al final la suma.",{"vars":{"a":{"min":2,"max":9},"b":{"min":2,"max":9}}}),
     {"t":"ordering","p":"Ordená los pasos para resolver 3 + 2 elevado a 3 × 5.","o":["Sumar 3 + 40 = 43","Calcular 2 elevado a 3 = 8","Multiplicar 8 × 5 = 40"],"r":{"orden":["Calcular 2 elevado a 3 = 8","Multiplicar 8 × 5 = 40","Sumar 3 + 40 = 43"]},"e":"Potencia, multiplicación y suma, en ese orden."}],
"4":[MC("Una calculadora común, que resuelve a medida que tipeás, muestra 32 para 5 + 3 × 4. ¿Cuál es el resultado correcto?",["17","32","20","60"],"17","Primero 3 × 4 = 12 y después 5 + 12 = 17."),
     N("Calculá con la calculadora y controlá con una estimación: 498 × 21.",{"acepta":[10458]},"Estimación: 500 × 20 = 10.000. Resultado: 10.458.")],
"5":[MC("Relámpago. ¿Qué se resuelve primero en 6 + 8 ÷ 2?",["La suma","La división"],"La división","× y ÷ van antes que + y −.",tiempo=15),
     N("Relámpago. Calculá 2 × (15 − 3 elevado a 2).",{"acepta":[12]},"3 elevado a 2 = 9; 15 − 9 = 6; 2 × 6 = 12.",tiempo=40),
     VF("Relámpago. La raíz cuadrada de (16 + 9) es igual a 4 + 3.","Falso","√(16 + 9) = √25 = 5.",tiempo=25),
     N("Relámpago. Calculá la raíz cuadrada de 144.",{"acepta":[12]},"12 × 12 = 144 (repaso de la misión 3).",tiempo=30)],
}
EXAMEN=[
 [1,N("Calculá {a} − {b} × {c} + {d}.",{"formula":"a-b*c+d"},"Primero la multiplicación; después restas y sumas de izquierda a derecha.",{"vars":{"a":{"min":30,"max":90},"b":{"min":2,"max":6},"c":{"min":2,"max":6},"d":{"min":1,"max":9}},"reglas":["a>b*c"]})],
 [1,N("Calculá 48 ÷ 6 × 2.",{"acepta":[16]},"De izquierda a derecha: 48 ÷ 6 = 8 y 8 × 2 = 16.")],
 [1,VF("En 20 − 5 + 3 se resta primero y después se suma, porque se resuelve de izquierda a derecha.","Verdadero","20 − 5 = 15 y 15 + 3 = 18.")],
 [2,N("Calculá {[30 − (4 + 2) × 3] + 2} × 5.",{"acepta":[70]},"(4 + 2) = 6; 6 × 3 = 18; 30 − 18 = 12; 12 + 2 = 14; 14 × 5 = 70.")],
 [2,MC("¿Qué cálculo corresponde a \"el doble de la suma de 7 y 8\"?",["2 × 7 + 8","2 × (7 + 8)","2 + 7 × 8","(2 + 7) × 8"],"2 × (7 + 8)","Primero se suma y después se duplica: la suma va entre paréntesis.")],
 [2,{"t":"fill_blank","p":"(12 − 4) ÷ 2 = ___ y 12 − 4 ÷ 2 = ___.","o":[],"r":{"huecos":[["4"],["10"]]},"e":"Con paréntesis: 8 ÷ 2 = 4. Sin paréntesis: 12 − 2 = 10."}],
 [3,N("Calculá {a} elevado a 2 − {b} × 2.",{"formula":"a^2-b*2"},"Primero la potencia, después la multiplicación y al final la resta.",{"vars":{"a":{"min":3,"max":12},"b":{"min":2,"max":9}},"reglas":["a*a>2*b"]})],
 [3,N("Calculá la raíz cuadrada de (50 − 1) + 2 elevado a 3.",{"acepta":[15]},"√49 = 7 y 2 elevado a 3 = 8; 7 + 8 = 15.")],
 [3,MC("¿Cuánto vale (3 + 2) elevado a 2?",["13","25","10","11"],"25","Primero el paréntesis: 5 elevado a 2 = 25.")],
 [4,MC("Para calcular 120 ÷ (4 + 2) en la calculadora, ¿qué hay que tipear?",["120 ÷ 4 + 2","120 ÷ (4 + 2)","(120 ÷ 4) + 2","120 + 4 ÷ 2"],"120 ÷ (4 + 2)","Los paréntesis se tipean igual que en la carpeta.")],
 [4,N("La calculadora mostró 4.980 para 498 × 21. ¿Qué resultado tenía que mostrar?",{"acepta":[10458]},"Estimación: 500 × 20 = 10.000. El resultado correcto es 10.458.")],
 [4,MC("¿Cuál es la mejor estimación de 302 × 19?",["600","6.000","60.000","600.000"],"6.000","300 × 20 = 6.000.")],
 [4,VF("Si la calculadora muestra un resultado, no hace falta estimar.","Falso","Si se tipeó mal, el resultado está mal: la estimación sirve para controlarlo.")],
]
M={"subject_id":"1260de30-041b-4324-b819-2de1a344f189","tema":4,"practica":"Práctica general: operaciones combinadas","examen_titulo":"Nivel jefe: operaciones combinadas",
   "niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-4.json"),"w"),ensure_ascii=False)
print("ok")
